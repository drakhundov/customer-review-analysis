import csv
from typing import List

import pandas as pd
from nltk.stem import PorterStemmer, WordNetLemmatizer


class CustomerReviewCSVParser:
    def __init__(self, csv_file_name):
        self.CSV_FILE_NAME = csv_file_name
        if not hasattr(self, "STOPWORDS_LST"):
            with open("stopwords.csv", "r") as stopwords_f:
                self.STOPWORDS_LST = list(
                    [item for sublist in csv.reader(stopwords_f) for item in sublist]
                )
        self.PUNCTUATION = [
            ".",
            ",",
            "!",
            "?",
            ":",
            ";",
            "'",
            '"',
            "(",
            ")",
            "[",
            "]",
            "{",
            "}",
            "/",
            "\\",
            "$",
            "-",
            "x",
            "*",
        ]
        self.df = None
        self.tokens = None
        self.terms = None

    def _load_data_from_csv(self) -> pd.DataFrame:
        try:
            self.df = pd.read_csv(self.CSV_FILE_NAME)  # DataFrame
        except Exception as e:
            raise e

    def load_data(self):
        try:
            self._load_data_from_csv()  # DataFrame
            self.customer_reviews_lst = self.df["text"].astype(str)
        except Exception as e:
            raise e

    def _tokenize_text(self, text: str) -> List[str]:
        for punc in self.PUNCTUATION:
            text = text.replace(punc, " ")
        text = text.lower().split()
        i, n = 0, len(text)
        while i < n:
            word = text[i]
            if word in self.STOPWORDS_LST or any([c.isdigit() for c in word]):
                text.pop(i)
                n -= 1
            else:
                i += 1
        return text

    def tokenize_data(self):
        stemmer = PorterStemmer()
        lemmatizer = WordNetLemmatizer()
        self.tokens = []
        self.terms = set()
        for review in self.customer_reviews_lst:
            self.tokens.append(
                [
                    stemmer.stem(lemmatizer.lemmatize(token))
                    for token in self._tokenize_text(review)
                ]
            )
            self.terms.update(self.tokens[-1])
