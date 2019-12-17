import math


REFERENCE_TEXTS = []


def clean_tokenize_corpus(texts: list) -> list:
    corpus = []
    if not isinstance(texts, list):
        return corpus
    illegal_signs = "1234567890^%~|[]<>{}@#&*-.,'+=()_₽$€¥£¢':;/?!`÷×§¶°¬¡¿™®©"
    for t in texts:
        if not isinstance(t, str):
            continue
        t = t.lower()
        t = t.replace('\n', ' ')
        t = t.replace('<br />', ' ')
        for sym in t:
            if sym in illegal_signs:
                t = t.replace(sym, '')
        while '  ' in t:
            t = t.replace('  ', ' ')
        t = t.split()
        corpus.append(t)
    return (corpus)


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        if not isinstance(self.corpus, list):
            return
        for t in self.corpus:
            if not isinstance(t, list):
                continue
            actual_words = len(t)
            for word in t:
                if not isinstance(word, str):
                    actual_words -= 1
            tf = {}
            for word in t:
                if not isinstance(word, str):
                    continue
                if word not in tf:
                    tf[word] = t.count(word) / actual_words
            if tf:
                self.tf_values.append(tf)

    def calculate_idf(self):
        if not isinstance(self.corpus, list):
            return
        actual_docs = len(self.corpus)
        for t in self.corpus:
            if not isinstance(t, list):
                actual_docs -= 1
        for t in self.corpus:
            if not isinstance(t, list) or t is None:
                continue
            for word in t:
                if not isinstance(word, str):
                    continue
                if word not in self.idf_values:
                    word_in_text = 0
                    for te in self.corpus:
                        if not isinstance(te, list):
                            continue
                        if word in te:
                            word_in_text += 1
                    self.idf_values[word] = math.log(actual_docs / word_in_text)
                    
    def calculate(self):
        if not self.idf_values or not self.tf_values:
            return
        for t in self.tf_values:
            tf_idf = {}
            for word, value in t.items():
                tf_idf[word] = value * self.idf_values[word]
            self.tf_idf_values.append(tf_idf)
       
    def report_on(self, word, document_index):
        report = ()
        if document_index >= len(self.corpus) or not self.tf_idf_values:
            return report
        tf_idf = self.tf_idf_values[document_index][word]
        rating = sorted(self.tf_idf_values[document_index], key=lambda v: int(self.tf_idf_values[document_index][v]),
                        reverse=True)
        place = rating.index(word)
        report = (tf_idf, place)
        return report

    
    def dump_report_csv(self):
        file = open('file.csv', 'w')
        headline = 'word'
        for name in self.file_names:
            headline += ', tf_{}'.format(name)
        headline += 'IDF'
        for name in self.file_names:
            headline += ', tf-idf_{}'.format(name)
        print (headline)
        for text in self.corpus:
            for word in text:
                word_line = '\n'
                word_line += word
                for dic in self.tf_values:
                    if word in dic:
                        word_line += ', ' + str(round(dic[word], 3))
                    else:
                        word_line += ', 0'
                word_line += ', ' + str(round(self.idf_values[word], 3))
                for di in self.tf_idf_values:
                    if word in di:
                        word_line += ', ' + str(round(di[word], 3))
                    else:
                        word_line += ', 0'
                file.write(word_line)    
        

                
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    tf_idf = TfIdfCalculator(test_texts)
    tf_idf.calculate_tf()
    tf_idf.calculate_idf()
    tf_idf.calculate()
    print(tf_idf.report_on('good', 0))
    print(tf_idf.report_on('and', 1))
