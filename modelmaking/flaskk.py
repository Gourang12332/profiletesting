from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

# Load the spaCy model
nlp = spacy.load('en_core_web_md')

def preprocess_skills(skills):
    doc = nlp(skills.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return tokens

def calculate_skills_score(profile, ideal_skills):
    profile_skills = profile.get('skills', '')
    processed_skills = preprocess_skills(profile_skills)
    skill_score = sum(ideal_skills.get(skill, 0) for skill in processed_skills)
    max_possible_score = sum(ideal_skills.values())
    normalized_score = (skill_score / max_possible_score) * 10
    return normalized_score

def generate_personalized_feedback(profile, final_score, test_scores, ideal_skills):
    feedback = f"Dear {profile['name']},\n"
    feedback += f"Based on your profile score of {final_score:.2f}, here is some personalized feedback:\n\n"
    # Feedback generation logic here...
    return feedback

@app.route('/evaluate', methods=['POST'])~
def evaluate_profile():
    data = request.json
    profile = data['profile']
    test_scores = data['test_scores']
    ideal_skills = data['ideal_skills']

    skills_score = calculate_skills_score(profile, ideal_skills)
    profile['skills_score'] = skills_score

    final_score = calculate_profile_score(profile, test_scores)
    feedback = generate_personalized_feedback(profile, final_score, test_scores, ideal_skills)
    
    return jsonify({'final_score': final_score, 'feedback': feedback})

if __name__ == '__main__':
    app.run(debug=True)
