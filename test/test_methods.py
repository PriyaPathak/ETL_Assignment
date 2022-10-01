import os,sys
from pathlib import Path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
import pytest 
import pandas as pd
import numpy as np

@pytest.fixture()
def df():
    df = pd.DataFrame(
        {
            "Team Name": ["Team A", "Team B", "Team C","Team A", "Team B", "Team C"],
            "Year": [1990,1990,1990,1991,1991,1991],
            "Wins": [23,40,21,45,12,21],
        }
    )
    return df


def test_add_transformed_data_to_xl_max_wins(df):

    expected_df_max = pd.DataFrame(
        {
            "Year":[1990,1991],
            "Wins":[40,45]
        }
    )

    df_max = df.groupby(["Year"])["Wins"].agg('max').reset_index()
    
    pd.testing.assert_frame_equal(df_max,expected_df_max)

def test_add_transformed_data_to_xl_min_wins(df):

    expected_df_min = pd.DataFrame(
        {
            "Year":[1990,1991],
            "Losses":[21,12]

        }
    )

    df_min = df.groupby(["Year"])["Wins"].agg('min').reset_index()
    df_min.rename(columns={"Wins": "Losses"},inplace=True)
    pd.testing.assert_frame_equal(df_min,expected_df_min)

