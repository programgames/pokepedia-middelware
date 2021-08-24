from pokedex.db.tables import *

from db import MoveNameChangelog
from db.entity import PokemonMoveAvailability
from connection.conn import session
from util.helper.generationhelper import int_to_generation_indentifier
import functools


def get_default_gen8_national_dex_pokemon_number():
    return [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
        42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 72, 73, 77, 78, 79, 80,
        81, 82, 83, 90, 91, 92, 93, 94, 95, 98, 99, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114,
        115, 116, 117, 118,
        119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139,
        140, 141,
        142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 163, 164, 169, 170, 171, 172, 173, 174, 175, 176, 177,
        178, 182,
        183, 184, 185, 186, 194, 195, 196, 197, 199, 202, 206, 208, 211, 212, 213, 214, 215, 220, 221, 222, 223,
        224, 225,
        226, 227, 230, 233, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252,
        253, 254,
        255, 256, 257, 258, 259, 260, 263, 264, 270, 271, 272, 273, 274, 275, 278, 279, 280, 281, 282, 290, 291,
        292, 293,
        294, 295, 298, 302, 303, 304, 305, 306, 309, 310, 315, 318, 319, 320, 321, 324, 328, 329, 330, 333, 334,
        337, 338,
        339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 355, 356, 359, 360, 361, 362, 363, 364, 365,
        369, 371,
        372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 403, 404, 405, 406, 407, 415, 416,
        420, 421,
        422, 423, 425, 426, 427, 428, 434, 435, 436, 437, 438, 439, 440, 442, 443, 444, 445, 446, 447, 448, 449,
        450, 451, 452, 453, 454, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 470, 471, 473, 474, 475,
        477, 478, 479, 480,
        481, 482, 483, 484, 485, 486, 487, 488, 494, 506, 507, 508, 509, 510, 517, 518, 519, 520, 521, 524, 525,
        526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 543, 544, 545, 546, 547, 548, 549,
        550, 551,
        552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572,
        573, 574,
        575, 576, 577, 578, 579, 582, 583, 584, 587, 588, 589, 590, 591, 592, 593, 595, 596, 597, 598, 599, 600,
        601, 605,
        606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626,
        627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647,
        649, 659, 660, 661, 662, 663,
        674, 675, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695,
        696, 697,
        698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718,
        719, 721,
        722, 723, 724, 725, 726, 727, 728, 729, 730, 736, 737, 738, 742, 743, 744, 745, 746, 747, 748, 749, 750,
        751, 752,
        753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773,
        776, 777,
        778, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799,
        800, 801,
        802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822,
        823, 824,
        825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845,
        846, 847,
        848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868,
        869, 870,
        871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891,
        892, 893, 894, 895, 896, 897, 898
    ]


def find_default_pokemons_in_national_dex(start: int, end: int):
    national_pokedex = session.query(Pokedex).filter(Pokedex.identifier == 'national').one()
    id_results = session.query(PokemonSpecies.id) \
        .select_from(PokemonDexNumber) \
        .join(PokemonSpecies, PokemonSpecies.id == PokemonDexNumber.species_id) \
        .join(Pokedex, PokemonDexNumber.pokedex_id == national_pokedex.id) \
        .filter(PokemonDexNumber.pokedex_number >= start) \
        .filter(PokemonDexNumber.pokedex_number <= end) \
        .filter(Pokedex.id == national_pokedex.id) \
        .all()

    ids = []
    for result in id_results:
        ids.append(result.id)

    return session.query(Pokemon) \
        .join(PokemonSpecies, PokemonSpecies.id == Pokemon.species_id) \
        .filter(Pokemon.is_default == True) \
        .filter(PokemonSpecies.id.in_(ids)) \
        .all()


def find_alola_pokemons():
    forms = session.query(PokemonForm).filter(PokemonForm.form_identifier == 'alola').all()
    return list(map(lambda pokemonForm: pokemonForm.pokemon, forms))


def find_galar_pokemons():
    forms = session.query(PokemonForm).filter(PokemonForm.form_identifier == 'galar').all()
    return list(map(lambda pokemonForm: pokemonForm.pokemon, forms))


def find_default_gen8_pokemons():
    national_pokedex = session.query(Pokedex).filter(Pokedex.identifier == 'national').one()
    species_results = session.query(PokemonSpecies.id) \
        .select_from(PokemonDexNumber) \
        .join(PokemonSpecies, PokemonSpecies.id == PokemonDexNumber.species_id) \
        .join(Pokedex, PokemonDexNumber.pokedex_id == national_pokedex.id) \
        .filter(PokemonDexNumber.pokedex_number >= 1) \
        .filter(PokemonDexNumber.pokedex_number <= 898) \
        .filter(Pokedex.id == national_pokedex.id) \
        .filter(PokemonDexNumber.pokedex_number.in_(get_default_gen8_national_dex_pokemon_number())) \
        .all()

    species_ids = []
    for result in species_results:
        species_ids.append(result.id)

    return session.query(Pokemon).join(PokemonSpecies, PokemonSpecies.id == Pokemon.species_id).filter(
        Pokemon.is_default == True).filter(PokemonSpecies.id.in_(species_ids))


def find_pokemon_by_identifier(name: str) -> Pokemon:
    return session.query(Pokemon).filter(Pokemon.identifier == name).one()


def find_pokemon_with_specific_page(start_at: int):
    national_dex = session.query(Pokedex).filter(Pokedex.identifier == 'national').one()
    species_results = session.query(PokemonSpecies.id) \
        .select_from(PokemonDexNumber) \
        .join(PokemonSpecies, PokemonSpecies.id == PokemonDexNumber.species_id) \
        .join(Pokedex, PokemonDexNumber.pokedex_id == national_dex.id) \
        .filter(PokemonDexNumber.pokedex_number >= start_at) \
        .filter(Pokedex.id == national_dex.id) \
        .all()

    species_ids = []
    for result in species_results:
        species_ids.append(result.id)

    availabilities = session.query(PokemonMoveAvailability) \
        .join(Pokemon).order_by(Pokemon.id.desc()).filter(PokemonMoveAvailability.has_pokepedia_page == True).all()

    pokemons = {}
    for availability in availabilities:
        pokemon = availability.pokemon  # type: Pokemon
        if pokemon.species.id in species_ids:
            pokemons[pokemon.id] = pokemon

    return pokemons


def is_pokemon_available_in_version_groups(self, pokemon: Pokemon, version_groups: list):
    return session.query(PokemonMoveAvailability) \
        .join(VersionGroup, VersionGroup.identifier.in_(version_groups)) \
        .join(Pokemon, PokemonMoveAvailability.pokemon_id == pokemon.id).one_or_none()


def find_availability_by_pkm_and_form(name: str, version_group: VersionGroup) -> PokemonMoveAvailability:
    return session.query(PokemonMoveAvailability) \
        .filter(PokemonMoveAvailability.version_group_id == version_group.id) \
        .join(Pokemon) \
        .filter(Pokemon.identifier == name) \
        .filter(PokemonMoveAvailability.version_group_id == version_group.id) \
        .one()


def find_moves_by_pokemon_move_method_and_version_group(pokemon: Pokemon, pokemon_move_method: PokemonMoveMethod,
                                                        version_group: VersionGroup):
    return session.query(PokemonMove) \
        .join(Pokemon, Pokemon.id == pokemon.id) \
        .join(PokemonMoveMethod, PokemonMoveMethod.id == pokemon_move_method.id) \
        .join(VersionGroup, VersionGroup.id == version_group.id) \
        .order_by(PokemonMove.id.asc()) \
        .all()


def find_french_move_by_pokemon_move_and_generation(pokemon_move: PokemonMove, generation: int):
    move = session.query(Move).join(PokemonMove, PokemonMove.move_id == pokemon_move.move_id).one()

    alias = session.query(MoveNameChangelog) \
        .join(Move, Move.id == MoveNameChangelog.move_id) \
        .join(Language, Language.identifier == 'fr') \
        .filter(MoveNameChangelog.generation.identifier == int_to_generation_indentifier(
        generation)).first()  # type: MoveNameChangelog

    if alias:
        return alias.name

    return move.name_map['fr']


def find_french_move_by_move_and_generation(move: Move, generation: int):
    alias = session.query(MoveNameChangelog) \
        .join(Move, Move.id == MoveNameChangelog.move_id) \
        .join(Language, Language.identifier == 'fr') \
        .filter(MoveNameChangelog.generation.identifier == int_to_generation_indentifier(
        generation)).first()  # type: MoveNameChangelog

    if alias:
        return alias.name

    return move.name_map['fr']


def find_pokepedia_move_methods_methods_repository() -> list:
    return session.query(PokemonMoveMethod).filter(
        PokemonMoveMethod.identifier.in_(['level-up', 'tutor', 'machine', 'egg'])).all()


def find_highest_version_group_by_generation(generation: Generation) -> VersionGroup:
    version_groups = session.query(VersionGroup) \
        .join(Generation, Generation.id == generation.id) \
        .filter(VersionGroup.identifier.not_in(['colosseum', 'xd', 'lets-go-pikachu-lets-go-eevee'])) \
        .all()  # type: list

    if len(version_groups) == 1:
        return version_groups[0]

    return functools.reduce(lambda a, b: a if a.order > b.order else b, version_groups)


def get_french_slot1_same_by_generation(pokemon: Pokemon, gen: int):
    generation = session.query(Generation).filter(Generation.identifier == int_to_generation_indentifier(gen)).one()


