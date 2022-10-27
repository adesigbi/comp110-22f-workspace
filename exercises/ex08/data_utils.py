"""Dictionary related utility functions."""

__author__ = "730572167"

# Define your functions below

from csv import DictReader

def read_csv_rows(csv_file_path: str)-> list[dict[str, str]]:
    """Reads the rows of a csv into a list of dicts table."""
    result: list[dict[str, str]] = []
    file_handle = open(csv_file_path, "r", encoding="utf8")

    read_csv = DictReader(file_handle)

    for row in read_csv:
        result.append(row)

    return result


def column_values(list_of_dicts_table: list[dict[str, str]], row_name: str) -> list[str]:
    """Gives you the column values of a particular row oriented table."""
    result: list[str] = []
    for dict in list_of_dicts_table: 
        if row_name in dict:
            result.append(dict[row_name])
    return result


def columnar(list_of_dicts_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Turns row oriented table into column oritened table"""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = list_of_dicts_table[0]
    for key in first_row:
        result[key] = column_values(list_of_dicts_table, key)
    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Presents the table with only 'n' number of rows."""
    result: dict[str, list[str]] = {}
    for key in column_table:
        new_column_list: list[str] = []
        old_column_list: list[str] = column_table[key]
        for i in range(n):
            new_column_list.append(old_column_list[i])
        result[key] = new_column_list
    return result


def select(column_table: dict[str, list[str]], column_name: list[str]) -> dict[str, list[str]]:
    """Returns the tale with only specified columns."""
    result: dict[str, list[str]] = {}
    for i in range(len(column_name)):
        column_list: list[str] = column_table[column_name[i]]
        result[column_name[i]] = column_list
    return result


def concat(column_table1: dict[str, list[str]], column_table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines data from two different column oriented tables."""
    result: dict[str, list[str]] = {}
    for key in column_table1:
        result[key] = column_table1[key]
    for key in column_table2:
        if key in result:
            old_list: list[str] = column_table2[key]
            for item in old_list:
                result[key].append(item)
        if key not in result:
            result[key] = column_table2[key]
    return result


def count(a_list: list[str]) -> dict[str, int]:
    """Counts frequency of a list and assigns the frequency to a string in a dict."""
    result: dict[str, int] = {}
    for item in a_list:
        if item in result:
            result[item] += 1
        if item not in result:
            result[item] = 1
    return result