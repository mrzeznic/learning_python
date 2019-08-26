import pandas as pd


def task_read13():
    print("hello from task13 read data")
    # query="https://data.colorado.gov/resource/tv8u-hswn.json"
    data_2013 = pd.read_json(
        "http://dummy.restapiexample.com/api/v1/employees")
    data_2013.to_csv('{$HOME}'+'/data/data_2013.csv')
