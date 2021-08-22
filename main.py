import argparse
import sys
import install
import handler
def main(junk, *argv):
    parser = create_parser()

    if len(argv) <= 0:
        parser.print_help()
        sys.exit()

    args = parser.parse_args(argv)
    args.func(parser, args)

def create_parser():
    """Build and return an ArgumentParser.
    """
    common_parser = argparse.ArgumentParser(add_help=False)
    parser = argparse.ArgumentParser(
        prog='middleware', description=u'Pokepedia middleware',
        parents=[common_parser],
    )
    cmds = parser.add_subparsers(title='commands', metavar='<command>', help='commands')

    cmd_sync_pokemon_moves = cmds.add_parser(
        'syncpokemonmoves', help=u'Sync pokemon moves',
        parents=[common_parser])
    cmd_sync_pokemon_moves.set_defaults(func=command_sync_pokemon_moves)

    init_command = cmds.add_parser(
        'init', help=u'init project',
        parents=[common_parser])
    init_command.set_defaults(func=command_init)

    return parser



def command_sync_pokemon_moves(parser, args):
    handler.process_pokemon_move()


def command_init(parser, args):
    install.create_app_tables()
    install.fill_app_tables()

main(*sys.argv)
