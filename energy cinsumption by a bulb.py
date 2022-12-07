def energy():
    lm = input("Enter the light made based on lumens: ")
    lm = float(lm)
    kh = input("Enter the power consumption: ")
    kh = float(kh)
    ef_rat= 0
    ef_rat = lm/kh
    if ef_rat >= 210:
        print("You have A class with:", ef_rat, "score")
    elif ef_rat < 210 and ef_rat >= 185:
        print("You have B class with:", ef_rat, "score")
    elif ef_rat < 185 and ef_rat >=160:
        print("You have C class with:", ef_rat, "score")
    elif ef_rat < 160 and ef_rat >= 135:
        print("You have D class with:", ef_rat, "score")
    elif ef_rat < 135 and ef_rat >= 110:
        print("You have E class with:", ef_rat, "score")
    elif ef_rat < 110 and ef_rat >= 85:
        print("You have F class with:", ef_rat, "score")
    elif ef_rat < 85:
        print("You have G class with:", ef_rat, "score")

energy()