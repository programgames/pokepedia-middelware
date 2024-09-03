from middleware.formatter.database import pokemonlevelmoveformatter, pokemonmachinemoveformatter, \
    pokemoneggmoveformatter
from middleware.util.helper.pokemonmovehelper import LEVELING_UP_TYPE, MACHINE_TYPE, EGG_TYPE
from pokeapi.db.tables import Pokemon, Generation, PokemonMoveMethod


def get_database_pokemon_moves(pokemon: Pokemon, generation: Generation, learn_method: PokemonMoveMethod,
                               form_order: dict, step: int):
    if learn_method.identifier == LEVELING_UP_TYPE:
        return pokemonlevelmoveformatter.get_formatted_level_up_database_moves(pokemon, generation,
                                                                               learn_method,
                                                                               form_order)
    elif learn_method.identifier == MACHINE_TYPE:
        return pokemonmachinemoveformatter.get_formatted_machine_database_moves(pokemon, generation,
                                                                                learn_method, form_order,
                                                                                step)
    elif learn_method.identifier == EGG_TYPE:
        return pokemoneggmoveformatter.get_formatted_egg_database_moves(pokemon, generation,
                                                                                learn_method, form_order,
                                                                                step)
    else:
        raise NotImplementedError(f'Can\'t process pokemon move : invalid learn method'
                                  f' {learn_method.identifier}')
