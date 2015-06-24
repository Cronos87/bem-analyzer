# BEM Syntax Analyzer

A simple script that parse a website and analyse BEM usage.

## Dependency

BeautifulSoup4 - See https://pypi.python.org/pypi/beautifulsoup4

## Launch script from terminal

```bash
python bem_analyzer.py http://www.site.com
```

This command will print something like this:

```
Element found without a block: tag-list__item
Multiple element found: article__body__link
Modifier found without its element: tag-list__item--first
3 errors found!
```

The first error mean that `tag-list__item` has no parent called `tag-list`.

The second error mean that `article__body__link` mustn't have multiple element.

These selectors are good:
  * article__body
  * article__link

The third error mean `tag-list__item--first` must have `tag-list__item` in the same class attribut.

Example:
```HTML
<div class="tag-list__item tag-list__item--first"></div>
```

## Compatibility

At the moment, the script is only compatible with Python 3. The support for Python 2 will arrive.
