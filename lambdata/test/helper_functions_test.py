# write some code using unittest to test some function

import unittest
from helper_functions import AddySplit

class TestAddySplit(unittest.TestCase):
    
    
    def test_addy_split(self):
    """Test the columns value the dataframe the
    number of colums using unittest
    """
        addy_series = (
            ['890 Jennifer Brooks\nNorth Janet, WY 24785'],
            ['8394 Kim Meadow\nDarrenville, AK 27389'],
            ['379 Cain Plaza\nJosephburgh, WY 06332'],
            ['5303 Tina Hill\nAudreychester, VA 97036'])
        data=AddySplit(addy_series)
        df=data.addy_split(addy_series)

        self.assertEqual(len(df.columns), 3)
        self.assertEqual(df.iloc[0]['state'], 'WY')
        self.assertEqual(df['state'][0], ['address', 'state', 'zip'])
        self.assertEqual(df.iloc[0]['zip'], '24785') 

if __name__ == "__main__":

    unittest.main()