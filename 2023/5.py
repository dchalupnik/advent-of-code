import typing as tp
from dataclasses import dataclass

from utils import read_file


def solution():
    seeds, seed_map = generate_seed_map()
    return min(find_location(seed_map, seed, 'seed') for seed in seeds)


def find_location(seed_map, value, key):
    map_ = seed_map[key]
    for data_item in map_['data']:
        if data_item['source_start'] < value <= data_item['source_start'] + data_item['range']:
            new_value = data_item['destination_start'] + value - data_item['source_start']
            if map_['destination'] == 'location':
                return new_value

            return find_location(seed_map, new_value, map_['destination'])

    if map_['destination'] == 'location':
        return value

    return find_location(seed_map, value, map_['destination'])


def generate_seed_map():
    data = read_file(5)
    categories = data.split('\n\n')
    seed_map = dict([_generate_seed_map(it) for it in categories[1:]])
    seeds = list(generate_seeds(seed_map, categories[0].split(': ', 1)[1].split(' ')))
    return seeds, seed_map


def generate_seeds(seed_map, raw_seeds) -> tp.Generator[int, None, None]:
    for i in range(0, len(raw_seeds), 2):
        start_ = int(raw_seeds[i])
        range_ = int(raw_seeds[i+1])
        for it in range(start_, start_ + range_):
            yield it


def _generate_seed_map(raw_map: str) -> tp.Tuple[str,dict]:
    name, data = raw_map.rsplit(' map:\n')
    source, destination = name.split('-to-')
    return source, {
        "data": [_generate_seed_map_data(it) for it in data.split('\n')],
        "destination": destination
    }


def _generate_seed_map_data(raw_data: str) -> dict:
    destination_start, source_start, range_ = raw_data.split()
    return {
        'source_start': int(source_start),
        'destination_start': int(destination_start),
        'range': int(range_),
    }


print(solution())