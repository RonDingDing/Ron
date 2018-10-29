import sys
import unicodedata
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
# 'pýtĥöñ\x0cis\tawesome\r\n'

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}

a = s.translate(remap)
print(a)


cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b)
# 'pýtĥöñ is awesome\n'
print(b.translate(cmb_chrs))
# 'python is awesome\n'

digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))
# 460
# Arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))
# '123'
