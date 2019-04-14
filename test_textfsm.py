#!/usr/bin/python -tt
# Project: Dropbox (Indigo Wire Networks)
# Filename: textfsm.py
# claudia
# PyCharm

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "2019-04-12"
__copyright__ = "Copyright (c) 2018 Claudia"
__license__ = "Python"

import argparse
import textfsm
import csv


def some_function():
    pass


def main():

    # Open the template file, and initialise a new TextFSM object with it.
    with open(arguments.template_file) as template_file_fh:
        fsm = textfsm.TextFSM(template_file_fh)

    # Read stdin until EOF, then pass this to the FSM for parsing.
    with open(arguments.output_file) as data_fh:
        input_data = data_fh.read()

    fsm_results = fsm.ParseText(input_data)

    if arguments.verbose:
        print("\nTextFSM Template Methods:")
        print(dir(fsm))
        print(f"\nFSM Values: \n\t{fsm.values}")
        print(f"\nFSM States: \n\t{fsm.states.keys()}")
        print(f"\nFSM States Full: \n\t{fsm.states}")
        print(f"\nFSM Value MAP:")
        for k,v in fsm.value_map.items():
            print(f"\tKey: {k} \tValue: {v}")

        print(f"\nTextFSM results variable is of type {type(fsm_results)} and has standard list Methods:")
        print(dir(fsm_results))

    print(f'\n\nTextFSM Results Header:\n{fsm.header}')
    print("="*40)
    for row in fsm_results:
        print(f"{row}")
    print("="*40)
    print("\n")
    # Save to Text
    with open('output.txt', 'w') as out_fh:
        out_fh.write(f"{fsm.header}\n")
        [out_fh.write(f"{line}\n") for line in fsm_results]

    # Save to CSV
    fsm_results.insert(0, fsm.header)
    with open('output.csv', 'w') as out_fh:
        csv_fh = csv.writer(out_fh)
        csv_fh.writerows(fsm_results)


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python textfsm.py <template file> <show output file>' ")

    parser.add_argument('template_file', help=" TextFSM Template File ")
    parser.add_argument('output_file', help=' Device data (show command) output')
    parser.add_argument('-v', '--verbose', help='Enable all of the extra print statements used to investigate the results ', action='store_true', default=False)
    arguments = parser.parse_args()

    main()
