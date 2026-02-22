from num2words import num2words
import string
import re 
with open("task1.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("== TEXTE ORIGINAL ===")
print(text)
print()
print("===CONVERTIR EN MINUSCULES ===")
text_lower = text.lower()
print(text_lower)
print()
print("==SUPPRIMER LA PONCTUATION ===")
text_no_punct = text_lower.translate(str.maketrans('', '', string.punctuation))
print(text_no_punct)
print()
print("==SUPPRIMER LES NOMBRES ===")
text_no_numbers = re.sub(r'\d+', '', text_no_punct)
print(text_no_numbers)
print()
print("===SUPPRIMER LES SYMBOLES SPECIAUX ====")
symbols = "@#$%^&*()_+=[]{}|\\<>/~`"
text_no_symbols = text_no_numbers.translate(str.maketrans('', '', symbols))
print(text_no_symbols)
print()
print("==SUPPRIMER LE BRUIT (–) ==")
text_no_noise = text_no_symbols.replace("–", " ")
print(text_no_noise)
print()
print("==SUPPRIMER LES ESPACES MULTIPLES ==")
final_text = re.sub(r'\s+', ' ', text_no_noise).strip()
print(final_text)
print()




with open("task2.txt", "r", encoding="utf-8") as f:
    text = f.read()
 
print("== TEXTE ORIGINAL ===")
print(text)
print()

contractions = {
    "i'm": "i am",
    "you're": "you are",
    "he's": "he is",
    "she's": "she is",
    "it's": "it is",
    "don't": "do not",
    "can't": "cannot",
    "won't": "will not",
    "didn't": "did not",
    "doesn't": "does not",
    "isn't": "is not",
    "aren't": "are not"
}
for key, value in contractions.items():
    text = re.sub(key, value, text, flags=re.IGNORECASE)

text = text.lower()
text = re.sub(r'\d+', lambda x: num2words(int(x.group())), text)
text = text.translate(str.maketrans('', '', string.punctuation))
text = re.sub(r'\s+', ' ', text).strip()

print("===== NORMALIZED TEXT =====")
print(text)