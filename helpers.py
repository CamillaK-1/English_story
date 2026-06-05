import sqlite3


# def calculate_ending(session):

#     fatigue = session.get("fatigue", 0)
#     belonging = session.get("belonging", 0)
#     selfworth = session.get("selfworth", 0)
#     tension = session.get("tension", 0)

#     if fatigue > 40:
#         return "burnout"

#     if belonging < -20:
#         return "isolation"

#     if selfworth < -30:
#         return "erosion"

#     return "reflection"