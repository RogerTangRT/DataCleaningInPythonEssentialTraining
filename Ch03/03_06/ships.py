# %%
import pandas as pd

df = pd.read_csv('ships.csv')
df
# %%
import pandera as pa
import numpy as np


schema = pa.DataFrameSchema(
    {
        "name": pa.Column(
            pa.String,
            unique=True,
            checks=pa.Check.str_length(min_value=2)
        ),

        "lat": pa.Column(
            pa.Float,
            nullable=True,
            checks=pa.Check.in_range(-90, 90)
        ),

        "lng": pa.Column(
            pa.Float,
            nullable=True,
            checks=pa.Check.in_range(-180, 180)
        ),
    },
    strict=True,
)


schema.validate(df)

# %%
