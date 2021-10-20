import math


def Probability(rating1, rating2):
  
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

def EloRating(Ra, Rb, K, d):
    Pa = Probability(Rb, Ra)
    if (d == 1) :
        Ra = Ra + K * (1 - Pa)
    else :
        Ra = Ra + K * (0 - Pa)
    return Ra
  