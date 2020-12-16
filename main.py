import os
import sys

import datatable as dt
import fastavro as avro
import pandas as pd


def import_to_dt(data_path: str):
    if not avro.is_avro(data_path):
        raise ValueError(f"Path '{data_path}' does not point to an Avro file.")

    with open(data_path, 'rb') as fo:
        records = avro.reader(fo)
        data_frame = pd.DataFrame(records)
        table = dt.Frame(data_frame)
        return table


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing commandline argument. Please pass the path to the Avro file.')
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"Path '{path}' does not exists.")
        sys.exit(1)

    table = import_to_dt(path)
    for column in table:
        print(column)
