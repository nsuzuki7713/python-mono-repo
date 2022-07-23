import unicodedata

def unicode_test(value):
    # Unicode 文字を与えると、大文字の名前が返される。
    name = unicodedata.name(value)
    # 名前(大文字と小文字を区別しない)を与えると、Unicode文字が返される。
    value2 = unicodedata.lookup(name)
    print(f'value="{value}" name="{name}" value2="{value2}"')

unicode_test("A")
unicode_test("$")
unicode_test("\u00a2")
unicode_test("\u20ac")
unicode_test("あ")
unicode_test('\u2603')

import re
result = re.match(r'You', "Young Frankenstein")

source = "Young Frankenstein"
if m := re.match(r'Frank', source):
    print(m.group())