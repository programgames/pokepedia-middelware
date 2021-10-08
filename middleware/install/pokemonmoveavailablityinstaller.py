from middleware.db import repository
from middleware.connection.conn import session
from middleware.db.tables import PokemonMoveAvailability
from pokedex.db.tables import VersionGroup

red_blue_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'red-blue').one()
yellow_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'yellow').one()
gold_silver_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'gold-silver').one()
crystal_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'crystal').one()
ruby_sapphir_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'ruby-sapphire').one()
firered_leafgreen_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'firered-leafgreen').one()
emerald_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'emerald').one()
fire_red_leaf_green_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'firered-leafgreen').one()
diamond_pearl_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'diamond-pearl').one()
platinum_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'platinum').one()
heart_gold_soul_silver_vg = session.query(VersionGroup).filter(
    VersionGroup.identifier == 'heartgold-soulsilver').one()
black_white_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'black-white').one()
black2_white2_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'black-2-white-2').one()
xy_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'x-y').one()
oras_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'omega-ruby-alpha-sapphire').one()
sun_moon_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'sun-moon').one()
ultra_sun_ultra_moon_vg = session.query(VersionGroup).filter(
    VersionGroup.identifier == 'ultra-sun-ultra-moon').one()
lgpe_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'lets-go-pikachu-lets-go-eevee').one()
sword_shield_vg = session.query(VersionGroup).filter(VersionGroup.identifier == 'sword-shield').one()


def load_basic_move_availabilities():
    save_availabilities(red_blue_vg, 1, 151)
    save_availabilities(yellow_vg, 1, 151)
    save_availabilities(crystal_vg, 1, 251)
    save_availabilities(gold_silver_vg, 1, 251)
    save_availabilities(fire_red_leaf_green_vg, 1, 386)
    save_availabilities(ruby_sapphir_vg, 1, 386)
    save_availabilities(emerald_vg, 1, 386)
    save_availabilities(diamond_pearl_vg, 1, 493)
    save_availabilities(platinum_vg, 1, 493)
    save_availabilities(heart_gold_soul_silver_vg, 1, 493)
    save_availabilities(black_white_vg, 1, 649)
    save_availabilities(black2_white2_vg, 1, 649)
    save_availabilities(xy_vg, 1, 721)
    save_availabilities(oras_vg, 1, 721)
    save_availabilities(sun_moon_vg, 1, 807)
    save_availabilities(ultra_sun_ultra_moon_vg, 1, 807)
    save_alola_pokemons(sun_moon_vg)
    save_alola_pokemons(ultra_sun_ultra_moon_vg)
    save_alola_pokemons(sword_shield_vg, True)
    save_galar_pokemons(sword_shield_vg)
    save_default_gen8_pokemons(sword_shield_vg)
    save_availabilities(lgpe_vg, 1, 151)
    save_availabilities(lgpe_vg, 808, 809)
    save_alola_pokemons(lgpe_vg)


def load_specific_pokemon_move_availabilities():
    # gen 3
    save_pokemon_move_availabilities_with_forms([ruby_sapphir_vg, emerald_vg, firered_leafgreen_vg],
                                                'deoxys-normal', ['deoxys-attack', 'deoxys-defense', 'deoxys-speed'],
                                                False, True, False, False, True)
    # gen4
    save_pokemon_move_availabilities_with_forms([diamond_pearl_vg, platinum_vg, heart_gold_soul_silver_vg],
                                                'deoxys-normal', ['deoxys-attack', 'deoxys-defense', 'deoxys-speed'],
                                                False, True, False, False, True)
    save_pokemon_move_availabilities_with_forms([diamond_pearl_vg, platinum_vg, heart_gold_soul_silver_vg],
                                                'wormadam-plant', ['wormadam-sandy', 'wormadam-trash'],
                                                False, True, True, False, True)
    save_pokemon_move_availabilities_with_forms([platinum_vg, heart_gold_soul_silver_vg, heart_gold_soul_silver_vg],
                                                'shaymin-land', ['shaymin-sky'],
                                                False, True, False, False, True)
    # gen 5
    save_pokemon_move_availabilities_with_forms([black_white_vg, black2_white2_vg],
                                                'deoxys-normal', ['deoxys-attack', 'deoxys-defense', 'deoxys-speed'],
                                                False, True, False, False, True)
    save_pokemon_move_availabilities_with_forms([black_white_vg, black2_white2_vg],
                                                'wormadam-plant', ['wormadam-sandy', 'wormadam-trash'],
                                                False, True, True, False, True)
    save_pokemon_move_availabilities_with_forms([black_white_vg, black2_white2_vg],
                                                'shaymin-land', ['shaymin-sky'],
                                                False, True, False, False, True)
    save_pokemon_move_availabilities_with_forms([black2_white2_vg],
                                                'kyurem', ['kyurem-black', 'kyurem-white'], True)
    # gen6
    # noinspection DuplicatedCode
    save_pokemon_move_availabilities_with_forms([xy_vg, oras_vg],
                                                'meowstic-male', ['meowstic-female'],
                                                False, True, False, False, False)
    save_pokemon_move_availabilities_with_forms([xy_vg, oras_vg],
                                                'deoxys-normal', ['deoxys-attack', 'deoxys-defense', 'deoxys-speed'],
                                                False, True, False, False, True)
    save_pokemon_move_availabilities_with_forms([xy_vg, oras_vg],
                                                'wormadam-plant', ['wormadam-sandy', 'wormadam-trash'],
                                                False, True, True, False, True)
    save_pokemon_move_availabilities_with_forms([xy_vg, oras_vg],
                                                'shaymin-land', ['shaymin-sky'],
                                                False, True, False, False, True)
    save_pokemon_move_availabilities_with_forms([xy_vg, oras_vg],
                                                'kyurem', ['kyurem-black', 'kyurem-white'], True)
    save_pokemon_move_availabilities_with_forms([xy_vg, oras_vg],
                                                'hoopa', ['hoopa-unbound'], False, True, False, False, False)
    # gen7
    # noinspection DuplicatedCode
    save_pokemon_move_availabilities_with_forms([sun_moon_vg, ultra_sun_ultra_moon_vg],
                                                'meowstic-male', ['meowstic-female'],
                                                False, True, False, False, False)
    save_pokemon_move_availabilities_with_forms([sun_moon_vg, ultra_sun_ultra_moon_vg],
                                                'deoxys-normal', ['deoxys-attack', 'deoxys-defense', 'deoxys-speed'],
                                                False, True, False, False, True)
    save_pokemon_move_availabilities_with_forms([sun_moon_vg, ultra_sun_ultra_moon_vg],
                                                'wormadam-plant', ['wormadam-sandy', 'wormadam-trash'],
                                                False, True, True, False, True)
    save_pokemon_move_availabilities_with_forms([sun_moon_vg, ultra_sun_ultra_moon_vg],
                                                'shaymin-land', ['shaymin-sky'],
                                                False, True, False, False, True)
    save_pokemon_move_availabilities_with_forms([sun_moon_vg, ultra_sun_ultra_moon_vg],
                                                'kyurem', ['kyurem-black', 'kyurem-white'], True)
    save_pokemon_move_availabilities_with_forms([sun_moon_vg, ultra_sun_ultra_moon_vg],
                                                'hoopa', ['hoopa-unbound'], False, True, False, False, False)
    save_pokemon_move_availabilities_with_forms([sun_moon_vg],
                                                'lycanroc-midday', ['lycanroc-midnight'],
                                                False, True, True, False, True)
    save_pokemon_move_availabilities_with_forms([ultra_sun_ultra_moon_vg],
                                                'lycanroc-midday', ['lycanroc-midnight', 'lycanroc-dusk'],
                                                False, True, True, False, True)
    save_pokemon_move_availabilities_with_forms([sun_moon_vg,ultra_sun_ultra_moon_vg],
                                                'thundurus-incarnate', ['thundurus-therian'],
                                                False, False, True, False, False)
    save_pokemon_move_availabilities_with_forms([ultra_sun_ultra_moon_vg],
                                                'necrozma', ['necrozma-dusk', 'necrozma-dawn'], True)
    # gen 8
    save_pokemon_move_availabilities_with_forms([sword_shield_vg],
                                                'meowstic-male', ['meowstic-female'],
                                                False, True, False, False, False)
    save_pokemon_move_availabilities_with_forms([sword_shield_vg],
                                                'indeedee-male', ['indeedee-female'])
    save_pokemon_move_availabilities_with_forms([sword_shield_vg],
                                                'lycanroc-midday', ['lycanroc-midnight', 'lycanroc-dusk'],
                                                False, True, True, False, True)
    save_pokemon_move_availabilities_with_forms([sword_shield_vg],
                                                'toxtricity-amped', ['toxtricity-low-key'])
    save_pokemon_move_availabilities_with_forms([sword_shield_vg],
                                                'urshifu-single-strike', ['urshifu-rapid-strike'])
    save_pokemon_move_availabilities_with_forms([sword_shield_vg],
                                                'calyrex', ['calyrex-ice', 'calyrex-shadow'], True)


def save_pokemon_move_availabilities_with_forms(version_groups: list, original_name: str, forms: list,
                                                specific_page_forms=False, level=True, machine=True, egg=True,
                                                tutor=True):
    with session.no_autoflush:
        for version_group in version_groups:
            original_pokemon_availability = repository.find_availability_by_pkm_and_form(
                original_name, version_group)
            for form in forms:
                form_pokemon = repository.find_pokemon_by_identifier(form)
                availability = PokemonMoveAvailability()
                availability.version_group_id = version_group.id
                availability.pokemon_id = form_pokemon.id
                availability.has_pokepedia_page = specific_page_forms
                availability.is_default = False
                availability.level = level
                availability.machine = machine
                availability.egg = egg
                availability.tutor = tutor
                session.add(availability)

                original_pokemon_availability.forms.append(availability)
                session.add(original_pokemon_availability)
                session.commit()


def save_availabilities(version_group, start, end):
    pokemons = repository.find_default_pokemons_in_national_dex(start, end)
    for pokemon in pokemons:
        move_availability = PokemonMoveAvailability()
        move_availability.version_group_id = version_group.id
        move_availability.pokemon_id = pokemon.id
        session.add(move_availability)
    session.commit()


def save_alola_pokemons(version_group, gen8=False):
    excludeds = [
        'rattata-alola', 'raticate-alola', 'geodude-alola', 'graveler-alola', 'golem-alola', 'grimer-alola', 'muk-alola'
    ]

    pokemons = repository.find_alola_pokemons()
    for pokemon in pokemons:
        if gen8:
            if pokemon.identifier in excludeds:
                continue
        move_availability = PokemonMoveAvailability()
        move_availability.version_group_id = version_group.id
        move_availability.pokemon_id = pokemon.id
        move_availability.is_default = False
        session.add(move_availability)
    session.commit()


def save_galar_pokemons(version_group):
    pokemons = repository.find_galar_pokemons()
    for pokemon in pokemons:
        move_availability = PokemonMoveAvailability()
        move_availability.version_group_id = version_group.id
        move_availability.pokemon_id = pokemon.id
        move_availability.is_default = False
        session.add(move_availability)
    session.commit()


def save_default_gen8_pokemons(version_group):
    pokemons = repository.find_default_gen8_pokemons()
    for pokemon in pokemons:
        move_availability = PokemonMoveAvailability()
        move_availability.version_group_id = version_group.id
        move_availability.pokemon_id = pokemon.id
        session.add(move_availability)
    session.commit()
