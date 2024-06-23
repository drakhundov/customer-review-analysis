import os
import sys
import pickle

from best_k import Best_K
from data_parser import CustomerReviewCSVParser
from doc_term_matrix import DTM
from review_query import ReviewQuery

MAIN_SCRIPT, CMD, CSV_FILE_NAME, *ARGS = sys.argv

COMMANDS_MAP = {"search": ReviewQuery, "best_k": Best_K}


# TODO
class ArgParser:
    def __init__(self):
        pass


def check_cache():
    paths = ["DTM", "terms", "dims"]
    for path in paths:
        if not os.path.exists(f"cache/{path}"):
            return False
    return True


def cache(dtm):
    if not os.path.exists("cache"):
        os.mkdir("cache")
    with open("cache/DTM", "wb") as f:
        pickle.dump(dtm.m, f)
    with open("cache/terms", "wb") as f:
        pickle.dump(dtm.terms, f)
    with open("cache/dims", "wb") as f:
        pickle.dump((dtm.nterms, dtm.ndocs), f)


if not COMMANDS_MAP.get(CMD):
    raise Exception("Unsupported command. Use 'search' or 'best_k'.")
elif not os.path.isfile(CSV_FILE_NAME):
    raise Exception("CSV file does not exist.")
else:
    parser = CustomerReviewCSVParser(CSV_FILE_NAME)
    parser.load_data()
    parser.tokenize_data()
    data_cached = check_cache()
    dtm = DTM(parser.tokens, parser.terms, retrieve_from_cache=data_cached)
    if not data_cached:
        cache(dtm)
    _process = COMMANDS_MAP[CMD](dtm, parser)
    _process.execute()
