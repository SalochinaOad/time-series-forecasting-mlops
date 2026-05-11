import numpy as np
from scipy.stats import ks_2samp

class DriftDetector:

    def compute_psi(self, train, test):
        return abs(np.mean(train) - np.mean(test)) / (np.mean(train) + 1e-6)

    def compute_ks(self, train, test):
        stat, _ = ks_2samp(train, test)
        return stat

    def detect(self, train_df, test_df):

        train = train_df["sales"]
        test = test_df["sales"]

        drift = abs(train.mean() - test.mean())
        psi = self.compute_psi(train, test)
        ks = self.compute_ks(train, test)
        std_diff = abs(train.std() - test.std())

        if drift > 12 or psi > 0.2 or ks > 0.1 or std_diff > 5:
            return True

        return False
