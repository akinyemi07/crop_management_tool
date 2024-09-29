import joblib
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Sample data (replace this with your actual dataset)
data = {
    'Weather': ['Sunny', 'Rainy', 'Cloudy', 'Sunny', 'Rainy'],
    'Soil Type': ['Loam', 'Clay', 'Sandy', 'Loam', 'Clay'],
    'Crop': ['Wheat', 'Rice', 'Barley', 'Wheat', 'Rice']
}

df = pd.DataFrame(data)

# Convert categorical data to numerical
df['Weather'] = df['Weather'].astype('category')
df['Soil Type'] = df['Soil Type'].astype('category')
df['Crop'] = df['Crop'].astype('category')

# Prepare features and target variable
X = df[['Weather', 'Soil Type']].apply(lambda x: x.cat.codes)
y = df['Crop'].cat.codes

# Train the model
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Save the trained model to a file
joblib.dump(clf, 'crop_prediction_model.pkl')

# Save the mapping for weather, soil type, and crops to a file
mapping = {
    'Weather': dict(enumerate(df['Weather'].cat.categories)),
    'Soil Type': dict(enumerate(df['Soil Type'].cat.categories)),
    'Crop': dict(enumerate(df['Crop'].cat.categories))
}
joblib.dump(mapping, 'crop_mapping.pkl')

