from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train the model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Predict for a sample flower
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)

print("Iris Flower Prediction:", iris.target_names[prediction[0]])