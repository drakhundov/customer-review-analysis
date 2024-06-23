import os
import pickle

import numpy as np


class DTM:
    def __init__(self, tokenized_customer_reviews=None, terms=None, retrieve_from_cache=False):
        if retrieve_from_cache:
            if os.path.exists("cache"):
                with open("cache/DTM", "rb") as f:
                    self.m = pickle.load(f)
                with open("cache/terms", "rb") as f:
                    self.terms = pickle.load(f)
                with open("cache/dims", "rb") as f:
                    self.nterms, self.ndocs = pickle.load(f)
            else:
                pass
        elif tokenized_customer_reviews is None or terms is None:
            raise ValueError("DTM(tokenized_customer_reviews, terms, retrieve_from_cache=False). Not enough arguments provided.")
        else:
            temp_m = []  # The document-term matrix himself.
            for term in terms:
                temp_m.append([doc.count(term) for doc in tokenized_customer_reviews])
            self.m = np.array(temp_m)
            self.terms = terms
            self.nterms, self.ndocs = self.m.shape
