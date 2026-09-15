"""
Name: D'Andre Brooks
Email: db3306@nyu.edu
"""

def make_dict(filename, sep=": "):
    result = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            key, value = line.split(sep, 1)
            result[key] = value

    return result 
