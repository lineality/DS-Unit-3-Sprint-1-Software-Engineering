"""
lambdata - a collection of data science helper functions for lambda school
"""
import setuptools
REQUIRED = [
   "numpy",
   "pandas"
]
with open("README.md", "r") as fh:
   LONG_DESCRIPTION = fh.read()
   setuptools.setup(
   name="testpackagegga6",
   version = "0.1.1", # each time modified, this must incriment
   author = "lineality",
   description = "a collection of data science helper functions",
   long_description = LONG_DESCRIPTION,
   long_description_content_type="text/markdown",
   url="https://github.com/lineality/lambdata6",
   packages=setuptools.find_packages(),
   python_requires=">=3.5",
   install_requires = REQUIRED,
   classifiers=["Programming Language :: Python :: 3",
   "License :: OSI Approved :: MIT License",
   "Operating System :: OS Independent",
   ]
   )
