import csv
from scripts.data_retrieval import get_symbol_id as get_id

def data_parse( name ):
    with open("/var/www/html/data/" + name + ".csv", newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        data = list(data)
        data.pop(0)
        sym_id = get_id(name)
        parsed_data = []
        for row in data:
            parsed_row = [sym_id]
            for col in row:
                parsed_row.append(col)
            parsed_row = tuple(parsed_row)
            parsed_data.append(parsed_row)

        return parsed_data

