"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
import constants
from math import sin, cos, pi, sqrt


__author__ = "730572167"  


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, point_2: Point) -> float:
        """Returns the distance between to Point objects."""
        x1: float = self.x
        x2: float = point_2.x
        y1: float = self.y
        y2: float = point_2.y
        distance_between_points: float = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance_between_points


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Updates the location and immune status."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
    
    def contract_disease(self) -> None:
        """Returns the INFECTED constant to the 'sickness' atribute."""
        self.sickness = constants.INFECTED

    def immunize(self) -> None:
        """Immunizes a cell."""
        self.sickness = constants.IMMUNE

    def is_vulnerable(self) -> bool:
        """Returns True if the cell is infected and False if otherwise."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Returns True if the cell is infected and False if otherwise."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def is_immune(self) -> bool:
        """Returns True if a cell is immune and false if it isn't."""
        if self.sickness == constants.IMMUNE:
            return True
        else: 
            return False

    def color(self) -> str:
        """Returns a color string that differentiates between infected and vulnrable."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "green"

    def contact_with(self, another_cell: Cell) -> None: 
        """Infects a vulnrable cell if comes in contact with infected cell."""
        if self.is_infected() and another_cell.is_vulnerable():
            another_cell.contract_disease()
        if another_cell.is_infected() and self.is_vulnerable():
            self.contract_disease()


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected_cells >= cells or infected_cells <= 0:
            raise ValueError
        if immune_cells >= cells or immune_cells < 0:
            raise ValueError
        for _ in range(cells - infected_cells - immune_cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(infected_cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
            cell.contract_disease()
        for _ in range(immune_cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
            cell.immunize()            

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_X
            cell.direction.y *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Sees if two cells come in contact with eachother, and infecects a cell if that is true."""
        list_of_cells: list[Cell] = self.population
        i: int = 0 
        while i < (len(list_of_cells)):
            cell_a: Cell = list_of_cells[i]
            for b in range(i + 1, len(list_of_cells)):
                cell_b: Cell = list_of_cells[b]
                if cell_a.location.distance(cell_b.location) < constants.CELL_RADIUS:
                    cell_a.contact_with(cell_b)
            i += 1  

    def is_complete(self) -> bool:
        """Returns the bool 'True' if none of the Cell obejcts are still infected."""
        for cell in self.population:
            if cell.sickness >= constants.INFECTED:
                return False
        return True