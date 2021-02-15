# write some code using pytest to test some function


from helper_functions import AddySplit

def test_addy_split():
    """Test the columns value the dataframe the
    number of columns using pytest
    """
        addy_series = (
            ['890 Jennifer Brooks\nNorth Janet, WY 24785'],
            ['8394 Kim Meadow\nDarrenville, AK 27389'],
            ['379 Cain Plaza\nJosephburgh, WY 06332'],
            ['5303 Tina Hill\nAudreychester, VA 97036'])
        data=AddySplit(addy_series)
        df=data.addy_split(addy_series)

        assert (len(df.columns), 3)
        assert (df.iloc[0]['state'], 'WY')
        assert (df['state'][0], ['address', 'state', 'zip'])
        assert (df.iloc[0]['zip'], '24785') 
