import matplotlib.pyplot as plt

def plot_profile_analysis(profile, test_scores, final_score):
    categories = ['Skills', 'Experience', 'Qualifications', 'Aptitude', 'Technical', 'Interview']
    values = [
        profile['skills_score'],
        profile['experience_years'],
        profile['qualifications_level'],
        test_scores['aptitude_test'],
        test_scores['technical_test'],
        test_scores['interview_score']
    ]
    
    plt.bar(categories, values)
    plt.title(f"Profile Analysis for {profile['name']}")
    plt.xlabel('Categories')
    plt.ylabel('Scores')
    plt.show()
