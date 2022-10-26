"""Some helpful utility functions for working with CSV files."""

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of the csv into a table."""
    result: list[dict[str, str]] = []
    # TODO: more work

    #Open handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    #Read that file

    csv_reader = DictReader(file_handle)



    #Read each row of CSV line-by-line
    for row in csv_reader:
        result.append(row)

    #close the filw when we're done to free its resources.
    file_handle.close()

    return result


def column_values(list_of_dicts: list[dict[str,str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column"""
    column_list: list[str] = []
    for dict in list_of_dicts:
        value: str = dict[column]
        column_list.append(value)
    return column_list

def columnar(list_of_dict: list[dict[str, str]]) -> dict(str, list[str]):
    """Transform a row-oriented table to a column-oriented table."""
    dict_of_list: dict[str, list[str]] = {}

    first_row: dict[str,str] = list_of_dict[0]
    for key in first_row:
        dict_of_list[key] = column_values(list_of_dict, key)
    return dict_of_list


print(read_csv_rows("../data/weather.csv"))