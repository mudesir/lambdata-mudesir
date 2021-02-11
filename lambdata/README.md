# lambdata-mudesir

## Instalation

'''sh
!pip install https://test.pypi.org/project/lambdata-mudesir/1.0/
'''

## Usage

'''py

from lambdata.helper_functions import null_count
df = pd.DataFrame({'column0': [np.nan, 4, 3], 'column1': [9, np.nan, np.nan], 'column2': [10, 2, 2]})

null_count(df)

from lambdata.helper_functions import 
train_test_split 
df = pd.DataFrame({'column0': [0, 3, 6], 'column1': [1, 4, 7], 'column2': [2, 5, 8]})

train_test_split(df, frac=0.2)

from lambdata.helper_functions import randomize
df = pd.DataFrame({'column0': [0, 3, 6], 'column1': [1, 4, 7], 'column2': [2, 5, 8]})
randomize(df, seed=101)

from lambdata.helper_functions import addy_split
addy_series = (['890 Jennifer Brooks\nNorth Janet, WY 24785'], ['8394 Kim Meadow\nDarrenville, AK 27389'], ['379 Cain Plaza\nJosephburgh, WY 06332'], ['5303 Tina Hill\nAudreychester, VA 97036'])
addy_split(addy_series)
'''

