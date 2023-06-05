from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Loading Iris Dataset
iris = load_iris()

# Getting features and targets from the dataset
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


class NaiveBayesModel:
    def __init__(self):
        self.model = GaussianNB()

    def fit(self):
        self.model.fit(X_train, y_train)

    def predict(self, test_data):
        return self.model.predict(test_data)

    def get_evaluation_metrics(self):
        prediction = self.model.predict(X_test)
        report = metrics.classification_report(y_test, prediction, output_dict=True)
        return report


crf = NaiveBayesModel()


def get_model_instance():
    return crf


def get_target_idx(idx):
    return iris.target_names[idx]
