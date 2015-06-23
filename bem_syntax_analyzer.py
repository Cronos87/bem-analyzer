#!/usr/bin/env python

import urllib.request
import re
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Please install BeautifulSoup4. See: https://pypi.python.org/pypi/beautifulsoup4")
    exit()

try:
    url = sys.argv[1]
except IndexError:
    print("Please enter an url as argument.")
    exit()

data = urllib.request.urlopen(url).read()

soup = BeautifulSoup(data)

bem_classes = soup.find_all(class_=re.compile("__|--"))

nb_error = 0


def error(label):
    """Display error label and incremente error counter."""
    global nb_error

    print(label)
    nb_error = nb_error + 1

for bem_class in bem_classes:
    classes = bem_class["class"]

    for item in classes:
        if "--" in item:
            block, modifier = item.split("--")

            if block not in classes:
                error("Modifier found without its element: %s" % item)

        if "__" in item:
            if item.count("__") > 1:
                error("Multiple element found: %s" % item)

            block = item.split("__", 1)[0]
            parent = bem_class.find_parents(class_=block)

            if len(parent) == 0:
                error("Element found without a block: %s" % item)

if nb_error > 0:
    print("%d errors found!" % nb_error)
