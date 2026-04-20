# task1

# Class 1: Sports & Athletics (Context: Winning/Medals)
doc1 = "The gold medal price is high effort"
doc2 = "Winning a gold medal needs a high jump"
doc3 = "Market for a gold medal is a trade of sweat"
doc4 = "The athlete will trade all for a gold medal"

# Class 2: Finance & Economy (Context: Market/Investment)
doc5 = "The gold bars price is high today"
doc6 = "Investing in gold bars needs a high rate"
doc7 = "Market for gold bars is a trade of money"
doc8 = "The bank will trade all for gold bars"

import numpy as np
from sklearn.cluster import KMeans

# Your Task: Fill these functions

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  
    tokens = text.split()
    return tokens

def generate_ngrams(tokens, n):
    return [" ".join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]

def vectorize(docs, n_gram_size=1):
    processed_docs = []
    vocab = set()
    for doc in docs:
        tokens = preprocess_text(doc)
        ngrams = generate_ngrams(tokens, n_gram_size)
        processed_docs.append(ngrams)
        vocab.update(ngrams)
    vocab = sorted(list(vocab))
    vocab_index = {word:i for i,word in enumerate(vocab)}
    X = np.zeros((len(docs), len(vocab)))

    for i, doc in enumerate(processed_docs):
        counts = Counter(doc)
        for word, count in counts.items():
            X[i][vocab_index[word]] = count

    return X


# Training / Clustering

all_docs = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8]

# 1-gram Experiment
X1 = vectorize(all_docs, n_gram_size=1)
km1 = KMeans(n_clusters=2, random_state=42).fit(X1)

# 2-gram Experiment
X2 = vectorize(all_docs, n_gram_size=2)
km2 = KMeans(n_clusters=2, random_state=42).fit(X2)

print(f"1-gram clusters: {km1.labels_}")
print(f"2-gram clusters: {km2.labels_}")

# compare accuracy and precision
from sklearn.metrics import accuracy_score, precision_score

print("1-gram Accuracy:",
      accuracy_score(true_labels, km1.labels_))

print("2-gram Accuracy:",
      accuracy_score(true_labels, km2.labels_))

print("1-gram Precision:",
      precision_score(true_labels, km1.labels_))

print("2-gram Precision:",
      precision_score(true_labels, km2.labels_))



# task2
# Documents
D1 = "I love cats"
D2 = "Cats are chill"
D3 = "I am late"

# Your Task: implement context window vectorization
# with window size = 1 (so each window is 3 tokens wide)
# Use <s> and </s> padding flags

def add_padding(tokens):
    return ["<s>"] + tokens + ["</s>"]

def extract_windows(tokens, window_size=1):
    windows = []
    size = 2*window_size + 1
    for i in range(len(tokens) - size + 1):
        window = tokens[i:i+size]
        windows.append(" ".join(window))
    return windows

def build_vocab(all_windows):
    vocab = sorted(set(all_windows))
    vocab_index = {w:i for i,w in enumerate(vocab)}
    return vocab_index

def vectorize_doc(doc_windows, vocab):
    vec = np.zeros(len(vocab))
    for w in doc_windows:
        if w in vocab:
            vec[vocab[w]] = 1
    return vec


# Run
all_docs = [D1, D2, D3]
all_windows = []
doc_windows_list = []
for doc in all_docs:
    tokens = doc.lower().split()
    tokens = add_padding(tokens)
    windows = extract_windows(tokens, window_size=1)
    doc_windows_list.append(windows)
    all_windows.extend(windows)
vocab = build_vocab(all_windows)
X = []
for doc_windows in doc_windows_list:
    vec = vectorize_doc(doc_windows, vocab)
    X.append(vec)
X = np.array(X)


print("Vocabulry:", vocab)
print("\nDocument Vectrs:")
print(X)