from process_data import ProcessData
import calcerr
import svd


class Best_K(ProcessData):
    def __init__(self, dtm, parser):
        self.m = dtm.m
        self.nterms, self.ndocs = dtm.nterms, dtm.ndocs

    def execute(self):
        MIN_K = 10
        MAX_K = min(self.nterms, self.ndocs)
        STEP = 20
        MSE = {"best_k": 0, "least_err": float("inf")}
        FN = {"best_k": 0, "least_err": float("inf")}
        stop_mse = stop_fn = False
        print(f"k from {MIN_K} to {MAX_K} with step {STEP}.")
        for k in range(MIN_K, MAX_K + 1, STEP):
            print(f"k = {k}")
            svd_vals = svd.compute_svd(self.m, k)
            DTM_APPROX = svd.compute_A(svd_vals)
            if not stop_mse:
                err = calcerr.MSE(DTM_APPROX, self.m)
                print("MSE:", err)
                if err < MSE["least_err"]:
                    MSE["best_k"] = k
                    MSE["least_err"] = err
                else:
                    stop_mse = True
            if not stop_fn:
                err = calcerr.FN(DTM_APPROX, self.m)
                print("FN:", err)
                if err < FN["least_err"]:
                    FN["best_k"] = k
                    FN["least_err"] = err
                else:
                    stop_fn = True
            # Over time when k is too large, the error will increase
            # due to overfitting.
            if stop_mse and stop_fn:
                break
            print()
        print(f"MSE: k={MSE['best_k']} err={MSE['least_err']}")
        print(f"FN: k={FN['best_k']} err={FN['least_err']}")
