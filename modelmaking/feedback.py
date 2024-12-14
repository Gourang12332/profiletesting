def generate_personalized_feedback(profile, final_score, test_scores, ideal_skills):
    feedback = f"Dear {profile['name']},\n"
    feedback += f"Based on your profile score of {final_score:.2f}, here is some personalized feedback:\n\n"

    # Feedback based on skills
    missing_skills = [skill for skill in ideal_skills if skill not in profile['skills'].lower()]
    if profile['skills_score'] < 7:
        feedback += "- Consider improving your skills in areas like: " + ", ".join(missing_skills) + ".\n"
    else:
        feedback += "- Your skills are strong. Keep up the good work!\n"

    # Feedback based on experience
    if profile['experience_years'] < 3:
        feedback += "- Gaining more professional experience will strengthen your profile.\n"
    else:
        feedback += "- Your experience level is good. Aim for leadership roles to further enhance your career.\n"

    # Feedback based on qualifications
    if profile['qualifications_level'] < 3:
        feedback += "- Consider pursuing additional qualifications or certifications to boost your profile.\n"
    else:
        feedback += "- Your qualifications are solid. Keep learning to stay ahead in your field.\n"

    # Feedback based on aptitude test score
    if test_scores['aptitude_test'] < 70:
        feedback += "- Improving your aptitude test performance could open more opportunities.\n"
    else:
        feedback += "- Your aptitude test performance is commendable. Continue honing your critical thinking skills.\n"

    # Feedback based on technical test score
    if test_scores['technical_test'] < 70:
        feedback += "- Focusing on technical skills will be beneficial. Consider more practice or courses.\n"
    else:
        feedback += "- Your technical skills are strong. Consider advanced topics to further excel.\n"

    # Feedback based on interview score
    if test_scores['interview_score'] < 80:
        feedback += "- Work on your interview skills. Practice common interview questions and refine your communication.\n"
    else:
        feedback += "- Great job on your interview performance! Consider mentoring others to solidify your knowledge.\n"

    return feedback
