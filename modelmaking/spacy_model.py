import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_md')

def get_skill_embedding(skill):
    doc = nlp(skill.lower())
    return doc.vector

def preprocess_skills(skills):
    doc = nlp(skills.lower())
    return [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]

def calculate_skills_score(profile, ideal_skills):
    profile_skills = profile.get('skills', '')
    processed_skills = preprocess_skills(profile_skills)
    
    skill_embeddings = {skill: get_skill_embedding(skill) for skill in ideal_skills}
    
    skill_score = 0
    for skill in processed_skills:
        if skill in skill_embeddings:
            skill_score += ideal_skills.get(skill, 0)

    max_possible_score = sum(ideal_skills.values())
    normalized_score = (skill_score / max_possible_score) * 10
    
   
    return normalized_score
