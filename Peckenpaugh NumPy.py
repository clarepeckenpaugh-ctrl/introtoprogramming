#one

import numpy as np

print(np.__version__)

#two

array_zero_to_nine = np.arange(10)

print(array_zero_to_nine)

#three

import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

column_names = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"
]

iris_df = pd.read_csv(url, header=None, names=column_names)

print(iris_df.head())

#four

petal_width = iris_df["petal_width"].to_numpy()

first_position = np.where(petal_width > 1.0)[0][0]

print(first_position)

#five

np.random.seed(100)
a = np.random.uniform(1, 50, 20)

print("Original array:")
print(a)

a[a > 30] = 30
a[a < 10] = 10

print("Updated array:")
print(a)