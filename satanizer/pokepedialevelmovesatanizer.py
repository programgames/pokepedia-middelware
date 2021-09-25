import re

from exception import WrongHeaderError
from collections import OrderedDict


def check_and_sanitize_moves(moves: list) -> dict:
    template = None
    end = None
    form = None
    actual_form = None
    section = {
        'topComments': [],
        'forms': OrderedDict(),
        'botComments': [],
    }
    # TODO regex
    if moves[0] not in [
        '=== Par montée en [[niveau]] ===',
        '===Par montée en [[niveau]] ===',
        '==== Par montée en [[niveau]] ====',
        '====Par montée en [[niveau]] ====',
        '==== [[Septième génération]] ====',
        '==== [[Huitième génération]] ====',
    ]:
        raise WrongHeaderError('Invalid header: {}'.format(moves[0]))
    section['topComments'].append(moves[0])
    del moves[0]
    r = re.compile(r'.*{{#invoke:Apprentissage\|niveau\|.*')

    templates = len(list(filter(r.match, moves)))
    if templates == 0:
        raise RuntimeError('no level template found')

    forms = OrderedDict()
    if templates == 1:
        forms['uniq_form'] = {
            'topComments': [],
            'forms': OrderedDict(),
            'botComments': [],
        }
        for move in moves:
            if not template and not re.match(r'.*{{#invoke:Apprentissage\|niveau\|.*', move):
                section['topComments'].append(move)
            elif not template and re.match(r'.*{{#invoke:Apprentissage\|niveau\|.*', move):
                template = True
            elif template and re.match(r'.*}}.*', move):
                template = False
                end = True
            elif end:
                section['botComments'].append(move)
            else:
                if 'moves' not in forms['uniq_form']:
                    forms['uniq_form']['moves'] = []
                forms['uniq_form']['moves'].append(move)
        section['forms'] = forms
        return section

    for move in moves:
        if not template and not form and not bool(re.match(r'.*=.*=.*', move)):
            section['topComments'].append(move)
        elif not template and form and bool(re.match(r'.*{{#invoke:Apprentissage\|niveau\|.*', move)):
            template = True
        elif not template and bool(re.match(r'.*=.*=.*', move)):
            form = True
            end = False
            actual_form = move.strip().replace('=', '').strip()
            forms[actual_form] = {
                'topComments': [],
                'moves': [],
                'botComments': [],
            }
        elif template and re.match(r'.*}}.*', move):
            template = False
            end = True
        elif template and form and not re.match(r'.*}}.*', move):
            forms[actual_form]['moves'].append(move)
        elif form and not re.match('.*=.*=.*', move) and not template and not end:
            forms[actual_form]['topComments'].append(move)
        elif end:
            forms[actual_form]['botComments'].append(move)

    section['forms'] = forms

    return section
