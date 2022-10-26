"""Filtering Column-oriented Data using a list of booleans as seen in Numpy, Pandas, R, and More"""

col_data: dict[str, list[float]] = {
    "high": [77, 84, 78, 79, 65, 67, 74, 61, 55, 61],
    "low":  [67, 51, 64, 45, 43, 53, 56, 37, 34, 42],
    "rain": [.3, .2, .4, .8, 0., .2, .4, .5, .1, .1]
}

col_data