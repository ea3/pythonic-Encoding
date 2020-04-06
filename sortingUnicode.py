import pyuca
import unicodedata
import re


coll = pyuca.Collator()
fruits = ['cayu', 'atemoia', 'cajá', 'açai', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)


re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    print('U+%04x' % ord(char),
          char.center(6),
          're_dig' if re_digit.match(char) else '-',
          'isdig' if char.isdigit() else '-',
          'isnum' if char.isnumeric() else '-',
          format(unicodedata.numeric(char), '5.2f'),
          unicodedata.name(char),
          sep='\t'
          )

