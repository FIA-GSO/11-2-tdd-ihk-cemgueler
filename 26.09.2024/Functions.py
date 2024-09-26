
def calculateReachedPercentage(reachedPoints: int, possiblePoints: int) -> float:
    if not isinstance(reachedPoints, int):
        raise TypeError("Reached points must be an integer.")
    if not isinstance(possiblePoints, int):
        raise TypeError("Possible points must be an integer.")

    if reachedPoints < 0:
        raise ValueError("Reached points cannot be negative.")
    if possiblePoints <= 0:
        raise ValueError("Possible points must be greater than 0.")
    if reachedPoints > possiblePoints:
        raise ValueError("Reached points cannot be greater than possible points.")
    if possiblePoints > 100:
        raise ValueError("Possible points cannot be greater than 100.")

    calculatedResult = reachedPoints / possiblePoints * 100
    return calculatedResult


def getGradeFromPercentage(percentage: int) -> str:
    if not isinstance(percentage, int):
        raise TypeError("Percentage must be an integer.")
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be between 0 and 100.")

    if percentage >= 92:
        return 'sehr gut'
    elif percentage >= 81:
        return 'gut'
    elif percentage >= 67:
        return 'befriedigend'
    elif percentage >= 50:
        return 'ausreichend'
    elif percentage >= 30:
        return 'mangelhaft'
    else:
        return 'ungenügend'
