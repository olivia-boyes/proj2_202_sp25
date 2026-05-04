import csv
import math
from dataclasses import dataclass
from typing import *

#recursion limit
import sys
sys.setrecursionlimit(10_000)


# Put your data definitions first!
#Task 1: data definitions
@dataclass(frozen=True)
class Row:
    country:Optional[str]
    year:Optional[int]
    electricity_and_heat_co2_emissions: Optional[float]
    electricity_and_heat_co2_emissions_per_capita: Optional[float]
    energy_co2_emissions: Optional[float]
    energy_co2_emissions_per_capita:Optional[float]
    total_co2_emissions_excluding_lucf: Optional[float]
    total_co2_emissions_excluding_lucf_per_capita: Optional[float]

@dataclass(frozen=True)
class Node:
    value:Row
    next:'Node|None' = None

# Then your functions.
#task 2: Reading CSV File

#Validate header row, convert each row into a Row object, and return a linked list with each Node containing a Row object
def read_csv_lines(filename: str) -> Optional[Node]:

    with open(filename, newline="") as csvfile:
        csv_data = csv.reader(csvfile)
        headers = next(csv_data)
        #validate headers
        expected_headers = ["country","year","electricity_and_heat_co2_emissions",
                            "electricity_and_heat_co2_emissions_per_capita",
                            "energy_co2_emissions",
                            "energy_co2_emissions_per_capita",
                            "total_co2_emissions_excluding_lucf",
                            "total_co2_emissions_excluding_lucf_per_capita"]
        if headers != expected_headers:
            raise ValueError("Missing Header or Wrong Format")

        #recursively make a linked list of nodes with each node containing one line of csv data
        def build_list(data) -> Optional[Node]:
            try:
                line = next(data)
            except StopIteration:
                return None

            return Node(parse_row(line), build_list(data))

        return build_list(csv_data)

#convert row into Row object
def parse_row(fields: list[str]) -> Row:
    row_obj = Row(country=None if fields[0] == "" else fields[0],
                  year=None if fields[1] == "" else int(fields[1]),
                  electricity_and_heat_co2_emissions=None if fields[2] == "" else float(fields[2]),
                  electricity_and_heat_co2_emissions_per_capita=None if fields[3] == "" else float(fields[3]),
                  energy_co2_emissions=None if fields[4] == "" else float(fields[4]),
                  energy_co2_emissions_per_capita=None if fields[5] == "" else float(fields[5]),
                  total_co2_emissions_excluding_lucf=None if fields[6] == "" else float(fields[6]),
                  total_co2_emissions_excluding_lucf_per_capita=None if fields[7] == "" else float(fields[7]))
    return row_obj

#task 3
#count the number of rows in the linked list of csv data
def listlen(data: Optional[Node]) -> int:
    if data is None:
        return 0
    return 1 + listlen(data.next)

#task 4
#iterate through rows and return a new filtered linked list of Rows that match the provided condition

def filter_rows(data: Optional[Node],
                field_name: str,
                comparison: str,
                value: Union[str,float,int]) -> Optional[Node]:

    # check if data is empty
    if data is None:
        return None

    filtered = filter_rows(data.next, field_name, comparison, value)

    row:Row = data.value # row of csv data
    field_value = getattr(row, field_name)

    if field_value is None:
        return filtered

    match: bool = False

    # "equal" comparison
    if field_name == "country" and comparison != "equal":
        raise ValueError("Can only use 'equal' to compare the 'country' field.")

    if comparison == "equal":
        if field_value == value:
            match = True

    # "less than" comparison
    elif comparison == "less_than":
        if field_value < value:
            match = True

    # "greater than" comparison
    elif comparison == "greater_than":
        if field_value > value:
            match = True

    else:
        raise ValueError

    #create new filtered linked list
    if match == True:
        new_node:Node = Node(row, filtered)
        return new_node
    else:
        return filtered
