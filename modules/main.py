import pandas as pd
from modules.functions import add_ten

df = pd.DataFrame(data={
    'floats': [1.1, 2.2],
    'ints': [1, 2],
    'strings': ['ab', 'cd']
})

df['floats'] = df['floats'].apply(add_ten)

print(df)