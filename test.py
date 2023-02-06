import glob
import os
from pathlib import PurePath
import re
from lxml import etree

src = r'''http://zh.cppreference.com/w/cpp/container/unordered_set'''
file = r'''http://zh.cppreference.com/w/cpp/container/unordered_set'''

root = 'output/reference'

html = etree.parse('output/reference/en/index.html', etree.HTMLParser())
print(etree.dump(html.find('//head')))

print(glob.glob(os.path.join(root, 'common/*.ttf')))

# print(os.path.relpath(os.path.abspath(root), file))

# import commands.preprocess as preprocess

# preprocess.transform_link()
# relative_path = re.sub(r'''.*cppreference.com/w/(.*)(.html)?''', r'''\g<1>''', file)
# s = PurePath(relative_path).suffix == ''
# print(s)
# s = os.path.relpath(f"zh/{relative_path}", os.path.dirname(f"en/{relative_path}"))
# print(s)

# s = re.sub(r'''http://zh.cppreference.com/w/''', r'''''', src)
# print(s)

# print(os.path.relpath('output/reference/common/a.ttf', PurePath('output/reference/en/index.html').parent))