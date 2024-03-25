import unittest
from sklearn.model_selection import train_test_split

class TestMLPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup once before all tests
        cls.X, cls.y = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=42)
        cls.X_train, cls.X_test, cls.y_train, cls.y_test = train_test_split(cls.X, cls.y, test_size=0.2, random_state=42)

    def test_pipeline_transformation(self):
        pipeline = MLPipeline(n_components=2)
        pipeline.fit(self.X_train, self.y_train)
        X_transformed = pipeline.transform(self.X_test)
        
        # Check if PCA reduced the dataset to 2 components
        self.assertEqual(X_transformed.shape[1], 2)

    def test_pipeline_prediction(self):
        pipeline = MLPipeline(n_components=2)
        pipeline.fit(self.X_train, self.y_train)
        predictions = pipeline.predict(self.X_test)
        
        # Check if predictions array has the correct length
        self.assertEqual(len(predictions), len(self.X_test))

    def test_model_evaluation_accuracy(self):
        pipeline = MLPipeline(n_components=2)
        pipeline.fit(self.X_train, self.y_train)
        accuracy = pipeline.evaluate(self.X_test, self.y_test)
        
        # Check if accuracy is a float and makes sense as a percentage
        self.assertIsInstance(accuracy, float)
        self.assertGreaterEqual(accuracy, 0.0)
        self.assertLessEqual(accuracy, 1.0)

    def test_incorrect_input_fit(self):
        pipeline = MLPipeline(n_components=2)
        
        # Pass incorrect inputs to fit method
        with self.assertRaises(ValueError):
            pipeline.fit("incorrect input", self.y_train)

    def test_predict_output_shape(self):
        pipeline = MLPipeline(n_components=2)
        pipeline.fit(self.X_train, self.y_train)
        predictions = pipeline.predict(self.X_test)
        
        # Check if the predict method returns an array with shape equal to the number of samples
        self.assertEqual(predictions.shape, (len(self.X_test),))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
