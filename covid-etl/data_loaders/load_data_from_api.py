import io
import pandas as pd
import requests


@data_loader
def load_data_from_api(*args, **kwargs):
    execution_date = kwargs['execution_date']
    date = execution_date.strftime("%d-%m-%Y")
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2021.csv'
    # url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv'
    response = requests.get(url)
    return pd.read_csv(io.StringIO(response.text), sep=',')

@test
def test_row_count(df, *args) -> None:
    assert len(df.index) >= 1000, 'The data does not have enough rows.'