"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730572167"


class Simpy:
    """Simpy class that has an attribute 'values' which is a list of floats."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructs a new 'Simpy' object."""
        self.values = values

    def __repr__(self) -> str:
        """Gives a human representation of a Simpy object."""
        return f"Simpy({self.values})"

    def fill(self, number: float, times: int) -> None:
        """Fills a Simpy's values with a specifc number of repeating values."""
        new_list: list[int] = []
        for _ in range(times):
            new_list.append(number)
        self.values = new_list

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Re-engineers a range function given start, stop and optional step parameters."""
        assert step != 0.0
        new_list: list[float] = []
        item: float = start
        if step < 0:
            while item > stop:
                new_list.append(item)
                item += step
        else:
            while item < stop:
                new_list.append(item)
                item += step
        self.values = new_list

    def sum(self) -> float: 
        """Finds the sum the values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Adds together two Simpy values lists or one values with an entered float."""
        result: Simpy = Simpy([])
        self_list: list[float] = self.values
        if isinstance(rhs, float):
            for num in self_list:
                summ: float = num + rhs
                result.values.append(summ)
        else:
            rhs_list = rhs.values
            assert len(rhs_list) == len(self_list)
            for i in range(len(self_list)):
                item_sum: float = self_list[i] + rhs_list[i]
                result.values.append(item_sum)
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raises the values of on simpy to the values of another or a specified float."""
        result: Simpy = Simpy([])
        self_list: list[float] = self.values
        if isinstance(rhs, float):
            for item in self_list:
                result.values.append(item ** rhs)
        else:
            rhs_list: list[float] = rhs.values
            assert len(rhs_list) == len(self_list)
            for i in range(len(rhs_list)):
                result.values.append(self_list[i] ** rhs_list[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Creates a mask based on the values list of two simpy objects or one simpy object and a float."""
        result: list[float] = []
        self_list: list[float] = self.values
        if isinstance(rhs, float):
            for item in self_list:
                result.append(item == rhs)
        else:
            rhs_list: list[float] = rhs.values
            assert len(rhs_list) == len(self_list)
            for i in range(len(rhs_list)):
                result.append(rhs_list[i] == self_list[i])
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Creates a mask based on the greater than relationship between values of another simpy object or values of a single float."""
        result: list[bool] = []
        self_list: list[float] = self.values
        if isinstance(rhs, float):
            for item in self_list:
                result.append(item > rhs)
        else:
            rhs_list: list[float] = rhs.values
            assert len(self_list) == len(rhs_list)
            for i in range(len(self_list)):
                result.append(self_list[i] > rhs_list[i])
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows for indexing of the values list or the creation of a new filtered list given a mask as a 'parameter'."""
        self_list: list[float] = self.values
        if isinstance(rhs, int):
            return self_list[rhs]
        else:
            result: Simpy = Simpy([])
            the_mask: list[bool] = rhs
            assert len(the_mask) == len(self_list)
            for i in range(len(self_list)):
                if the_mask[i]:
                    result.values.append(self_list[i])
            return result