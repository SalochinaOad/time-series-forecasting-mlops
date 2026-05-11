class RetrainingPipeline:

    def trigger(self, drift_flag):

        if drift_flag:
            print("Triggering retraining pipeline...")
        else:
            print("System stable - no retraining needed")