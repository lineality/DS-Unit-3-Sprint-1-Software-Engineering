"""
This report for Acme will calculate and print the following two values:

1. The Number of unique product names in the product list
2. The Average (mean) price, weight, and flammability of listed products

Then:
At the bottom of acme_report.py you should put the following code:
"""

# using the """ """ method is for some reason breaking my IDE and terminals
# so I am going back to using "#"

def generate_products()
    #generate a given number of products (default 30),
    #randomly, and return them as a list
    return


def inventory_report()
    # generate a given number of products (default 30), randomly, and return them as a list
    return




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
