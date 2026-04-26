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
    country:str
    year:int
    electricity_and_heat_co2_emissions:float
    electricity_and_heat_co2_emissions_per_capita:float
    energy_co2_emissions:float
    energy_co2_emissions_per_capita:float
    total_co2_emissions_excluding_lucf:float
    total_co2_emissions_excluding_lucf_per_capita:float

@dataclass(frozen=True)
class Node:
    value:Row
    next:'Node|None' = None

# Then your functions.
#task 2: Reading CSV File

'''Uses the csv.reader class to load rows
Validates the header row
Converts each row into a Row object
Recursively builds and returns a linked list (Node → Node → ... → None)'''

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
        #convert row into Row object
        def row_parse(fields:list[str]) -> Row:
            row_obj = Row(country= None if fields[0] == "" else fields[0],
                          year=None if fields[1] == "" else int(fields[1]),
                          electricity_and_heat_co2_emissions= None if fields[2] == "" else float(fields[2]),
                          electricity_and_heat_co2_emissions_per_capita=None if fields[3] == "" else float(fields[3]),
                          energy_co2_emissions=None if fields[4] == "" else float(fields[4]),
                          energy_co2_emissions_per_capita=None if fields[5] == "" else float(fields[5]),
                          total_co2_emissions_excluding_lucf=None if fields[6] == "" else float(fields[6]),
                          total_co2_emissions_excluding_lucf_per_capita=None if fields[7] == "" else float(fields[7]))
            return row_obj

        def build_list(data) -> Optional[Node]:
            head = None
            tail = None
            for line in iter(data): #iterates through csv data
                node:Node = Node(row_parse(line)) #makes a Node with value = Row of a csv line

                if head is None: #for the first iteration, makes the head and tail equal to the node
                    head: Node = node
                    tail: Node = node
                else:
                    tail.next:Node = node #for the other iterations, makes the tail the next line of the CSV data as a node
                    tail:Node = node

            return head

        return build_list(csv_data)

def lenlist(data: Optional[Node]) -> int:
    if data is None:
        return 0
    return 1 + lenlist(data.next)


