from middleware.db.tables import PokemonMoveAvailability
from middleware.formatter.dto.machinemove import MachineMove
from middleware.util.helper import generationhelper, machinehelper, languagehelper
from pokedex.db.tables import PokemonMoveMethod, Pokemon, Generation, VersionGroup, PokemonMove
from middleware.db import repository
from collections import OrderedDict
from middleware.connection.conn import session
import re
from pokedex.db import util

"""Format pokemon level moves from database into a pretty format
"""


def get_formatted_machine_database_moves(pokemon: Pokemon, generation: Generation, learn_method: PokemonMoveMethod,
                                         form_order: dict, step: int):
    return _get_pokemon_machine_move_forms(pokemon, generation, learn_method, form_order, step)


def _get_preformatteds_database_pokemon_machine_moves(pokemon: Pokemon, generation: Generation, step: int,
                                                      learn_method: PokemonMoveMethod):
    gen_number = generationhelper.gen_id_to_int(generation.identifier)
    preformatteds = {}

    if gen_number >= 1 <= 6 or gen_number == 8:
        version_group = repository.find_highest_version_group_by_generation(generation)

    elif gen_number == 7 and step == 1:
        version_group = util.get(session, VersionGroup, 'ultra-sun-ultra-moon')
    elif gen_number == 7 and step == 2:
        version_group = util.get(session, VersionGroup, 'lets-go-pikachu-lets-go-eevee')
    else:
        raise RuntimeError('Invalid generation/step condition')

    moves = repository.find_moves_by_pokemon_move_method_and_version_group(
        pokemon, learn_method,
        version_group
    )
    for pokemon_move_entity in moves:
        french_move_name = repository.get_french_move_by_pokemon_move_and_generation(pokemon_move_entity,
                                                                                     generation)
        if french_move_name in preformatteds:
            move = preformatteds[french_move_name]
        else:
            move = MachineMove()

        move = _fill_machine_move(move, french_move_name, pokemon_move_entity, generationhelper.gen_to_int(generation))

        preformatteds[french_move_name] = move

    return preformatteds


def _format_machine(move: MachineMove) -> str:
    return f"{move.item[2:]} / {move.name}"


def _sort_pokemon_machine_moves(formatteds: dict) -> list:
    sorted_moves = []

    sorteds_keys = sorted(formatteds, key=lambda k: k)
    for key in sorteds_keys:
        sorted_moves.append(formatteds[key])
    return sorted_moves


def _get_formatted_moves_by_pokemons(pokemon: Pokemon, generation: Generation, learn_method: PokemonMoveMethod,
                                     step: int):
    """
    Return the fully formatted list of pokemon machine move for a specific pokemon
    """
    pre_formatteds = _get_preformatteds_database_pokemon_machine_moves(pokemon, generation, step, learn_method)
    formatteds = {}

    for name, move in pre_formatteds.items():
        string = _format_machine(move)
        weight = _calculate_weight(move)
        formatteds[weight] = string

    formatteds = _sort_pokemon_machine_moves(formatteds)
    return formatteds


def _get_pokemon_machine_move_forms(pokemon: Pokemon, generation: Generation, learn_method: PokemonMoveMethod,
                                    form_order: dict, step):
    gen_number = generationhelper.gen_to_int(generation)
    """
    Return a list of  fully formatted pokemon machine move by forms
    """

    if gen_number >= 1 <= 6 or gen_number == 8:
        version_group = repository.find_highest_version_group_by_generation(generation)

    elif gen_number == 7 and step == 1:
        version_group = util.get(session, VersionGroup, 'ultra-sun-ultra-moon')
    elif gen_number == 7 and step == 2:
        version_group = util.get(session, VersionGroup, 'lets-go-pikachu-lets-go-eevee')
    else:
        raise RuntimeError('Invalid generation/step condition')

    availability = session.query(PokemonMoveAvailability) \
        .filter(PokemonMoveAvailability.version_group_id == version_group.id) \
        .filter(PokemonMoveAvailability.pokemon_id == pokemon.id) \
        .filter(PokemonMoveAvailability.has_pokepedia_page.is_(True)) \
        .one()

    move_forms = availability.forms

    if not move_forms or move_forms[0].has_pokepedia_page:
        # noinspection PyUnresolvedReferences
        specy = pokemon.species
        specy_name = specy.name_map[languagehelper.french].replace(' ', '_')  # M. Mime
        form_order_name = next(iter(form_order))
        if specy_name != form_order_name:  # handle case of pokemon with forms on different page like Sylveroy
            specy_name = form_order_name
        return {specy_name: _get_formatted_moves_by_pokemons(pokemon, generation, learn_method, step)}

    custom = move_forms[0].has_pokepedia_page

    if custom:
        # noinspection PyUnresolvedReferences
        specy_name = pokemon.specie.name_map(languagehelper.french)
        return {specy_name: _get_formatted_moves_by_pokemons(pokemon, generation, learn_method, step)}

    forms = OrderedDict()
    for form_name, form_extra in form_order.items():
        pokemon = repository.find_pokemon_by_french_form_name(pokemon, form_name)
        forms[form_name] = _get_formatted_moves_by_pokemons(pokemon, generation, learn_method, step)

    return forms


# noinspection PyUnresolvedReferences
def _fill_machine_move(move: MachineMove, name: str, pokemon_move_entity: PokemonMove,
                       generation: int) -> MachineMove:
    move.name = name

    move.is_hm = machinehelper.is_hm(pokemon_move_entity.machine, generation)
    move.item = pokemon_move_entity.machine.item.name_map[languagehelper.french]
    return move


def _calculate_weight(move: MachineMove):
    """
    Sort by no hm , then hm
    """
    return int(re.search(r'\d+', move.item).group(0)) * (1000 if move.is_hm else 1)
