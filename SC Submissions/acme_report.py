"""
This report for Acme will calculate and print the following two values:

1. The Number of unique product names in the product list
2. The Average (mean) price, weight, and flammability of listed products

Then:
At the bottom of acme_report.py you should put the following code:

"""


import numpy as np

"""
function returns number of unique value
"""
def uniqProductNames(x):
    x = np.array(x)
    return print(np.unique(x))


"""
mean price value
"""

def meanAvgPrice(x):
    return sum(x) / len(x)




print (meanAvgPrice(product_list))

print (uniqProductNames(product_list))


"""
The instructions said to incude a text blob
but that crashed pep8 check and would not format
in any way, so included separately.


"""
