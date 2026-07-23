def calculate_score(skills):
    score = 0 

    if len(skills) >= 12:
        score += 40
    elif len(skills) >= 8:
        score += 30
    elif len(skills) >= 5:
        score += 20
    else :
        score += 10
    return score