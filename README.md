# Mellitus-Diagnosis

Simple diabetes diagnosis app with scikit-learn module.

## Report

Being imported from `report`, it's a class to represent a diabetes diagnosis. Its mainly function is to calculate the diagnosis result and easily output the data in a way that our AI model can understand (see the function `raw` for more information).

## Dataset generation

It works by generating an almost equal quantity of diagnosis of each type based on random integers (with pre-determined ranges). For that, first it calculates the **oral tolerance test** based on the amount of each type already generated; then it can generates both **in fasting** and **casual** results. After all, returning the data is all that's needed to do. For more information, see the function `generate_dataset`.

## Logging

It's possible to observe the generated data by uncommenting the lines 58 and 59, as described by the comment in the line 57, all of these lines being part of `generate_dataset` function.
