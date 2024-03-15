from typing import Callable

class SimulationError(Exception):
    pass


class Simulation:
    simulations = dict()

    # Singleton Pattern
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def add(cls, fun: Callable, num_id: int):
        cls.simulations[num_id] = fun

    def run(cls, num_id: int):
        if num_id not in cls.simulations:
            raise SimulationError(f'Simulation {num_id} does not exist')
        cls.simulations[num_id]()