from simulations.simulation import *
import simulations.sim1
import sys


SUGGESTION = "Try 'python3 main.py 1'"


class InvalidInputError(Exception):
    pass


def validate_input(user_input: list[str]):
    if len(user_input) != 2:
        raise InvalidInputError('Error: expecting only 1 argument.')
    try: 
        int(user_input[1])
    except:
        raise InvalidInputError('Error: expecting an integer.')
        

def main(simulation_number):
    try:
        Simulation().run(simulation_number)
    except SimulationError as e:
        sys.exit(e)


if __name__ == "__main__":
    try:
        validate_input(sys.argv)
    except InvalidInputError as e:
        sys.exit(f'{e}, {SUGGESTION}')
    main(int(sys.argv[1]))
