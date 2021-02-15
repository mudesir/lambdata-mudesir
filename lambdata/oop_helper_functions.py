# helper function with oop use class

class HelperFunctions:
    def __init__(self, df, frac, seed, addy_series)


import re
import pandas as pd
import numpy as np


def null_count(df):
    result = df.isna().sum().sum()
    return result


def train_test_split(df, frac):
    """Create a Train/Test split function for a dataframe and returns both the Training and Testing sets
    Frac referes to the percent of data you would like to set aside for training
    """

    result = train_test_split(df, frac)
    return result


def randomize(df, seed):
    """Develop a randomization function that randomizes all of a dataframes cells then
    returns that randomized dataframe"""

    result = df.sample(frac=seed)
    return result


def addy_split(addy_series):
    """Split the addresses into three columns
    detect the format and pull out important pieces
    """

    s = []
    z = []
    for j in range(len(addy_series)):

        if addy_series[j] != '':
            z.append(addy_series[j])
            for k in range(len(z)):
                txt = " ".join(str(x) for x in z[k])
                t = re.split(', |\n', txt)
        s.append(t)

    state_zip = []
    for x in s:
        state_zip.append(x[2])

    state = []
    zip = []
    for y in state_zip:
        y1 = re.split('\\W', y)
        state.append(y1[0])
        zip.append(y1[1])

    adress = []
    city = []
    for x in s:
        adress.append(x[0])
        city.append(x[1])

    # dictionary of adds_series
    dict = {'city': city, 'state': state, 'zip': zip}
    df = pd.DataFrame(dict)
    return df


def add_state_names_column(my_df):
    """
    Add a corresponding state names to a dataframe.
    parms (my_df) a DataFrame with a column called "abbrev" that has state abbreviation.
    Return a copy of the original dataframe, but with an extra column.
    """

    new_df = =my_df.copy()

    names_map = {
        "CA": "California",
        "CO": "Colorado",
        "CT": "Connecticut",
        "DC": "District of Columbia",
        "TX": "Texas"}

    new_df["name"] = new_df["abbrev"].map(names_map)

    return my_df


if __name__ == "__main__":

    df = pd.DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())

    mapped_df = add_state_names_column(df)
    print(mapped_df.head())


class AddySplit():
    def __init__(self, addy_series):
        self.addy_series = addy_series

    def addy_split(addy_series):
    """Split the addresses into three columns
    detect the format and pull out important pieces
    """

     s = []
      z = []
       for j in range(len(addy_series)):

            if addy_series[j] != '':
                z.append(addy_series[j])
                for k in range(len(z)):
                    txt = " ".join(str(x) for x in z[k])
                    t = re.split(', |\n', txt)
            s.append(t)

        state_zip = []
        for x in s:
            state_zip.append(x[2])

        state = []
        zip = []
        for y in state_zip:
            y1 = re.split('\\W', y)
            state.append(y1[0])
            zip.append(y1[1])

        adress = []
        city = []
        for x in s:
            adress.append(x[0])
            city.append(x[1])

        # dictionary of adds_series
        dict = {'city': city, 'state': state, 'zip': zip}
        df = pd.DataFrame(dict)
        return df


if __name__ == "__main__":

    # addy_series
    addy_series = (
        ['890 Jennifer Brooks\nNorth Janet, WY 24785'],
        ['8394 Kim Meadow\nDarrenville, AK 27389'],
        ['379 Cain Plaza\nJosephburgh, WY 06332'],
        ['5303 Tina Hill\nAudreychester, VA 97036'])

    data=AddySplit(addy_series)
    data.addy_split(addy_series)
