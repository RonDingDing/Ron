import unicodedata
import string
def shave_marks(txt):
    norm_text = unicodedata.normalize("NFD", txt)
    shave = "".join(c for c in norm_text if not unicodedata.combining(c))
    return unicodedata.normalize("NFC", shaved)
