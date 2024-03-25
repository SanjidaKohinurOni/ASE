from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
import numpy as np

class MLPipeline(BaseEstimator, TransformerMixin):
    def __init__(self, n_components=4, n_splits=5):
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=n_components)
        self.model = LogisticRegression()
        self.n_splits = n_splits
    
    def fit(self, X, y):
        X_scaled = self.scaler.fit_transform(X)
        X_pca = self.pca.fit_transform(X_scaled)
        self.model.fit(X_pca, y)
        return self
    
    def transform(self, X):
        """
        Transforms the input dataset by first scaling it and then applying PCA.
        """
        X_scaled = self.scaler.transform(X)
        X_pca = self.pca.transform(X_scaled)
        return X_pca
    
    def predict(self, X):
        X_transformed = self.transform(X)
        return self.model.predict(X_transformed)
    
    def evaluate(self, X, y):
        try:
            predictions = self.predict(X)
            accuracy = accuracy_score(y, predictions)
            return accuracy
        except Exception as e:
            print(f"An error occurred during model evaluation: {e}")
            return -1

    def cross_validate(self, X, y):
        kf = KFold(n_splits=self.n_splits, shuffle=True, random_state=42)
        accuracies = list(map(lambda _: self._kfold_evaluate(X, y, _), kf.split(X)))
        return np.mean(accuracies)

    def _kfold_evaluate(self, X, y, indices):
        train_index, test_index = indices
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        self.fit(X_train, y_train)
        return self.evaluate(X_test, y_test)

    # Higher-order function example: Apply a custom transformation
    def apply_transformation(self, X, transform_func):
        return transform_func(X)

    # Function returning a function: Custom scaling
    def get_custom_scaler(self, factor):
        return lambda X: X * factor

# Immutable Data Structure Example
def create_immutable_sequence(seq):
    return tuple(seq)

# Example Usage:
pipeline = MLPipeline()
X, y = create_immutable_sequence([[1, 2], [3, 4]]), create_immutable_sequence([0, 1])

# Applying a custom transformation with a higher-order function
custom_transform = pipeline.get_custom_scaler(0.5)
transformed_X = pipeline.apply_transformation(X, custom_transform)

# Cross-validation with functions as parameters
cv_score = pipeline.cross_validate(X, y)
print(f"CV Score: {cv_score}")
