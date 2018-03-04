#!/usr/bin/env python
import sys

# These distance multiplers are as of 2018.03.04 as published on these pages:
# http://www.nyrr.org/new-race-procedures/calculated-pace-and-corral-updates
# https://help.nyrr.org/customer/portal/articles/1834337-best-pace?b_id=8313
DISTANCE_TO_MULTIPLIER = {
    '5k': 2.09,
    '4m': 1.60,
    '8k': 1.27,
    '5m': 1.26,
    '10k': 1.00,
    '12k': 0.82,
    '15k': 0.65,
    '10m': 0.60,
    '20k': 0.48,
    'half-marathon': 0.45,
    '25k': 0.38,
    '30k': 0.31,
    '20m': 0.29,
    'marathon': 0.22,
}


def calculate_best_pace(minutes, seconds, multiplier):
    decimal = seconds / 60
    ten_k_decimal_pace = ((minutes + decimal) * multiplier) / 6.2
    ten_k_seconds = round((ten_k_decimal_pace % 1) * 60)
    ten_k_minutes = int(ten_k_decimal_pace)
    return (ten_k_minutes, ten_k_seconds)


def parse_minutes_seconds(input_time):
    num_colons = input_time.count(':')
    if num_colons == 2:
        (hours, minutes, seconds) = input_time.split(':')
        (hours, minutes, seconds) = (int(hours), int(minutes), int(seconds))
        minutes += hours * 60
    elif num_colons == 1:
        (minutes, seconds) = input_time.split(':')
        (minutes, seconds) = (int(minutes), int(seconds))
    else:
        print(f'Invalid time: {input_time}')
        return None

    return (minutes, seconds)


def print_help():
    distances = ', '.join(DISTANCE_TO_MULTIPLIER.keys())
    print('To run: best_pace.py <RACE_TIME> <DISTANCE>')
    print('')
    print('Time format: 23:56 or 3:54:39')
    print('Distance is one of:')
    print(f'    {distances}')


def main(args):
    args = args[1:]
    if len(args) != 2:
        print_help()
        return

    input_time = args[0]
    input_distance = args[1]

    race_time = parse_minutes_seconds(input_time)
    if not race_time:
        return

    multiplier = DISTANCE_TO_MULTIPLIER.get(input_distance)
    if not multiplier:
        print(f'Unknown distance: {input_distance}')
        return

    (best_pace_minutes, best_pace_seconds) = calculate_best_pace(race_time[0], race_time[1], multiplier)
    print(f'{best_pace_minutes}:{best_pace_seconds:02d}')


if __name__ == '__main__':
    main(sys.argv)
