import numpy as np
from nltk.stem import PorterStemmer, WordNetLemmatizer

from process_data import ProcessData


class ReviewQuery(ProcessData):
    def __init__(self, dtm, parser):
        # 'dtm' stand for document-term matrix.
        self.query = None
        self.m = dtm.m
        # DataFrame (CSV data). Matrix is used for searching but
        # a more extensive data is needed to provide search results.
        self.df = parser.df
        self.terms = list(dtm.terms)
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def get_input(self):
        self.query = input(">> ").split()

    def empty_query(self) -> bool:
        return not self.query

    def _normalize_word(self, word):
        self.lemmatizer.lemmatize(self.stemmer.stem(word))

    def _normalize_query(self):
        """Returns search results for a given query."""
        self.query = [self._normalize_word(word) for word in self.query]

    def execute(self):
        self.get_input()
        while not self.empty_query():
            qv = [0] * len(self.terms)  # Create a vector that represents the query.
            for word in self.query:
                word = self._normalize_word(word)
                if word in self.terms:
                    qv[self.terms.index(word)] = 1
            sim_mtrx = np.dot(np.array(qv), self.m)  # Similarity matrix.
            most_fitting_query_idx = np.argmax(sim_mtrx)
            print(
                f"Search Result:\n[{self.df['posted_on'][most_fitting_query_idx]}] {self.df['author'][most_fitting_query_idx]}  ({self.df['rating'][most_fitting_query_idx]})\n{self.df['text'][most_fitting_query_idx]}"
            )
            self.get_input()
