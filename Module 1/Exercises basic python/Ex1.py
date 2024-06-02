def evaluateClassification(tp, fp, fn):
    if (isinstance(tp, int) and isinstance(fp, int) and isinstance(fn, int)):
        if (tp > 0 and fp > 0 and fn > 0):
            precision = tp / (tp + fp)
            recall = tp / (tp + fn)
            f1_score = 2 * ((precision * recall) / (precision + recall))

            print(f"precision is {precision}")
            print(f"recall is {recall}")
            print(f"f1-score is {f1_score}")
        else:
            print("tp and fp and fn must be greater than zero")
    else:
        if not isinstance(tp, int):
            print("tp is not an integer.")
        if not isinstance(fp, int):
            print("fp is not an integer.")
        if not isinstance(fn, int):
            print("fn is not an integer.")

#Examples:
evaluateClassification( tp =2 , fp =3 , fn =4)
evaluateClassification( tp ="a", fp =3 , fn =4)
evaluateClassification( tp =2 , fp ="a", fn =4)
evaluateClassification( tp =2 , fp =3 , fn ="a")
evaluateClassification( tp =2 , fp =3 , fn =0)
evaluateClassification( tp =2.1 , fp =3 , fn =0)