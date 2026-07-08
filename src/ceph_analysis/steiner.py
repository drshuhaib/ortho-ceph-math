import math

def calculate_angle_3_points(p1, vertex, p2):
    angle = math.degrees(math.atan2(p2[1] - vertex[1], p2[0] - vertex[0]) - 
                         math.atan2(p1[1] - vertex[1], p1[0] - vertex[0]))
    angle = abs(angle)
    if angle > 180:
        angle = 360 - angle
    return round(angle, 2)

def calculate_angle_between_lines(line1_p1, line1_p2, line2_p1, line2_p2):
    angle1 = math.atan2(line1_p2[1] - line1_p1[1], line1_p2[0] - line1_p1[0])
    angle2 = math.atan2(line2_p2[1] - line2_p1[1], line2_p2[0] - line2_p1[0])
    angle = math.degrees(angle1 - angle2)
    angle = abs(angle)
    if angle > 180:
        angle = 360 - angle
    if angle > 90 and angle < 180:
        angle = 180 - angle
    return round(angle, 2)

def run_steiner_analysis(points):
    sna = calculate_angle_3_points(points["S"], points["N"], points["A"])
    snb = calculate_angle_3_points(points["S"], points["N"], points["B"])
    anb = round(sna - snb, 2)
    
    u1_na_angle = calculate_angle_between_lines(points["U1A"], points["U1T"], points["N"], points["A"])
    l1_nb_angle = calculate_angle_between_lines(points["L1A"], points["L1T"], points["N"], points["B"])
    
    diagnosis = "Class II" if anb > 4.0 else "Class III" if anb < 0.0 else "Class I"
        
    return {
        "Diagnosis": diagnosis,
        "SNA": sna, "SNB": snb, "ANB": anb,
        "U1_NA": u1_na_angle, "L1_NB": l1_nb_angle
    }
