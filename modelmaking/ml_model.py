from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Example training data
X = np.array([
    [3, 4, 85, 78, 90],
    [5, 3, 88, 82, 85],
    [2, 5, 80, 75, 88]
])
y = np.array([7.8, 8.5, 6.0])

# Train model
model = RandomForestRegressor()
model.fit(X, y)

def predict_profile_score(profile, test_scores):
    features = [
        profile['experience_years'],
        profile['qualifications_level'],
        test_scores['aptitude_test'],
        test_scores['technical_test'],
        test_scores['interview_score']
    ]
    return model.predict([features])[0]
