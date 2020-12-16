# PoC for loading [Avro](https://avro.apache.org/) files to [datatable Frame](https://datatable.readthedocs.io/en/latest/api/frame.html)

## Setup
```shell script
virtualenv -p python3.6 env
source env/bin/activate
pip install -r requirements.txt
```

## Running
```shell script
python main.py <path/to/an_avro_file>
```
Sample Avro files can be found in the `test` directory.
