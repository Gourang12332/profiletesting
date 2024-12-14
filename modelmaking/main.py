from spacy_model import preprocess_skills, calculate_skills_score
from ml_model import predict_profile_score
from feedback import generate_personalized_feedback
from visualization import plot_profile_analysis

# Example profile and test scores
profile = {
    'name': 'John Doe',
    'skills': 'Python, SQL,',
    'experience_years': 0,
    'qualifications_level': 1
}

ideal_skills = {
    'python': 2,
    'sql': 1.5,
    'machine learning': 2.5,    ## they majorly will be on 
    'data analysis': 2,
    'java': 1,
    'big data': 2
}

test_scores = {
    'aptitude_test': 5,
    'technical_test': 8,
    'interview_score': 90
}

# Calculate skill score
skills_score = calculate_skills_score(profile, ideal_skills)
profile['skills_score'] = skills_score

# Predict final profile score
final_score = predict_profile_score(profile, test_scores)

# Generate personalized feedback
feedback = generate_personalized_feedback(profile, final_score,test_scores,ideal_skills)
print(feedback)

# Plot profile analysis
plot_profile_analysis(profile, test_scores, final_score)
