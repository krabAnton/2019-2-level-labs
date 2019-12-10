"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        if isinstance(word, str) and word:
            if not self.storage:
                self.storage[word] = 1
            elif word not in self.storage:
                self.storage[word] = max(self.storage.values()) + 1
            return self.storage[word]
        return -1

    def get_id_of(self, word: str) -> int:
        if isinstance(word, str) and word and word in self.storage:
            return self.storage[word]
        return -1

    def get_original_by(self, id: int) -> str:
        for k, v in self.storage.items():
            if v == id:
                return k
        return 'UNK'

    def from_corpus(self, corpus: tuple):
        if isinstance(corpus, tuple) and tuple:
            for word in corpus:
                self.put(word)
            return self.storage
        return {}


class NGramTrie:
    def __init__(self, num):
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}
        self.size = num

    def fill_from_sentence(self, sentence: tuple) -> str:
        if isinstance(sentence, tuple) and sentence:
            grams = []
            for ind in range(len(sentence)):
                if ind < len(sentence) - self.size:
                    elem = sentence[ind: ind + self.size]
                elif ind == len(sentence) - self.size:
                    elem = sentence[ind:]
                else:
                    break
                grams.append(elem)
            for gr in grams:
                if gr not in self.gram_frequencies:
                    self.gram_frequencies[gr] = grams.count(gr)
            return 'OK'
        return 'ERROR'

    def calculate_log_probabilities(self):
        for gram in self.gram_frequencies:
            begin = gram[:-1]
            sum_of = 0
            for beg in self.gram_frequencies:
                if beg[:-1] == begin:
                    sum_of += self.gram_frequencies[beg]
            self.gram_log_probabilities[gram] = math.log(self.gram_frequencies[gram] / sum_of)

    def predict_next_sentence(self, prefix: tuple) -> list:
        if isinstance(prefix, tuple) and len(prefix) == self.size - 1:
            sent = []
            sent.extend(list(prefix))
            while True:
                variants = []
                for gram in self.gram_log_probabilities:
                    if gram[:-1] == prefix:
                        variants.append((self.gram_log_probabilities[gram],
                                         gram))
                if not variants:
                    break
                variants.sort(reverse=True)
                most_popular = variants[0][1]
                sent.append(most_popular[-1])
                prefix = most_popular[1:]
            return sent
        return []


def encode(storage_instance, corpus) -> list:
    encoded_corp = []
    for sent in corpus:
        encoded_sent = []
        for word in sent:
            encoded_sent.append(storage_instance[word])
        encoded_corp.append(encoded_sent)
    return encoded_corp


def split_by_sentence(text: str) -> list:
    if isinstance(text, str) and text and '.' in text:
        text = text.lower()
        text = text.replace('\n', ' ')
        illegal_signs = '1234567890^%~|[]<>{}@#&*-,+=()№;:_`'
        for i in text:
            if i in illegal_signs:
                text = text.replace(i, '')
            elif i in '!?':
                text = text.replace(i, '.')
        text = text.replace("'", '')
        sentences = text.split('. ')
        corpus = []
        for sent in sentences:
            new_sent = ['<s>']
            sent = sent.replace('.', '')
            new_sent.extend(sent.split())
            new_sent.append('</s>')
            corpus.append(new_sent)
        return corpus
    return []
