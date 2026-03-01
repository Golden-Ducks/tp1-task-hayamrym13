# //tp0
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



# tp1
 
numberr = {
 "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
 "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"
}
 
def normalize(text):
 text = text.lower()
 words = text.split()
 
 punct = ".,!?;:'\"()-[]{}"
 new = ""
 for char in text:
 if char not in punct:
 new += char
 
 numTex = ""
 for char in new:
 if char.isdigit() and char in numberr:
 numTex += numberr[char]
 else:
 numTex += char
 
 words = numTex.split()
 
 return words 
 
 
def remove_stopwords(words):
 stopwords = [
 "i", "am", "is", "are", "the", "and", "in", "on",
 "at", "it", "its", "a", "an", "to", "of", "for"
 ]
 
 filter = []
 for word in words:
 if word not in stopwords:
 filter.append(word)
 
 return filter
 
def tokenize(text):
 tokens = text.split()
 return tokens
 
 
text1 = "Sallem!!! I am AI student in 2026. It is really powerffuuuuuuuuul and interesting !."
 
normal = normalize(text1)
final = remove_stopwords(normal)
 
print("After Normalization:")
print(normal)
 
print("\nAfter Stopwords Removal:")
print(final)
 
D1 = "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza."
D2 = "Five pizza were ready, but 3 bourak burned!"
D3 = "We only had 8 chamiyya, no pizza, and one tea."
D4 = "Is 6 too much? I ate nine bourak lol."
 
print("D1 normalized:")
print(normalize(D1))
 
print("\nD2 normalized:")
print(normalize(D2))
 
print("\nD3 normalized:")
print(normalize(D3))
 
print("\nD4 normalized:")
print(normalize(D4))
 
text = "WEEEEEEE i am learning nlp In ramadan .just EHEHEHEHEHEHEHEHEH"
tokens = tokenize(text)
 
print("Tokens:")
print(tokens)
 
def simple_stem(word):
 T = ["ing", "ed", "ly", "es", "s"]
 
 for suffix in T:
 if word.endswith(suffix) and len(word) > len(suffix) + 2:
 stem = ""
 for i in range(len(word) - len(suffix)):
 stem += word[i]
 return stem
 
 return word
 
 
test = ['learning', 'played', 'really', 'cats', 'boxes']
 
result = [simple_stem(word) for word in test]
 
print("After Simple Stemming:")
print(result)
 
 
def lemmatize(word):
 
 dict = {
 "studied": "study",
 "running": "run",
 "went": "go",
 "children": "child",
 "mice": "mouse"
 }
 
 if word in dict:
 return dict[word]
 
 return word
 
token = ['running', 'better', 'children', 'learning']
 
lemmatized_tokens = [lemmatize(word) for word in token]
 
print("After Simple Lemmatization:")
print(lemmatized_tokens)
 
