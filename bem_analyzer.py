#!/usr/bin/env python

try:
    from urllib.request import urlopen
    from urllib.parse import urlparse
except ImportError:
    from urllib2 import urlopen
    from urlparse import urlparse

import re
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Please install BeautifulSoup4. See: https://pypi.python.org/pypi/beautifulsoup4")
    exit()


def analyze(data):
    """Parse and return DOM elements with BEM errors."""
    url = urlparse(data)

    if url.scheme != "" and url.netloc != "":
        data = urlopen(url.geturl()).read()

    soup = BeautifulSoup(data)
    bem_classes = soup.find_all(class_=re.compile("__|--"))
    items_error = []

    for bem_class in bem_classes:
        classes = bem_class["class"]

        for item in classes:
            if "--" in item:
                block, modifier = item.split("--")

                if block not in classes:
                    items_error.append({"type": "modifier", "name": item, "element": bem_class})

            if "__" in item:
                if item.count("__") > 1:
                    items_error.append({"type": "element", "name": item, "element": bem_class})

                block = item.split("__", 1)[0]
                parent = bem_class.find_parents(class_=block)

                if len(parent) == 0:
                    items_error.append({"type": "block", "name": item, "element": bem_class})

    return items_error

def main():
    try:
        url = sys.argv[1]
    except IndexError:
        print("Please enter an url as argument.")
        exit()

    items = analyze(url)

    if len(items) > 0:
        for item in items:
            if item["type"] == "block":
                print("Element found without a block: %s" % item["name"])
            elif item["type"] == "element":
                print("Multiple element found: %s" % item["name"])
            elif item["type"] == "modifier":
                print("Modifier found without its element: %s" % item["name"])

        print("%d errors found!" % len(items))

if __name__ == '__main__':
    main()
