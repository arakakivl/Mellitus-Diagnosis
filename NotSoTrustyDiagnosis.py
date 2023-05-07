'''
Grupo iamAware:
João Busar,
Larissa xyz,
Luiza Hubert,
Rafael Nunes,
Vitor Arakaki
'''

from sklearn import tree
from Report import Report
import random
import sys

# Outputs the disclaimer. Again: in order to check your real health status, you must too see a doctor.
def show_disclaimer():
    print("DISCLAIMER: This software isn't sufficient for a full diagnosis. In order to check your health status, it's recommended to see a doctor =)\n")

# Generates the oral tolerance value based on the diagnosis
def generate_oral_tolerance(diagnosis):
    if type(diagnosis) != int or (diagnosis < 0 or diagnosis > 2):
        raise ValueError("Invalid diagnosis type.")
    
    return random.randint(80, 139) if diagnosis == 0 else (random.randint(140, 199) if diagnosis == 1 else random.randint(200, 260))

# Generates a list of 'n' Report objects and returns it.
def generate_dataset(x):
    generated_data = []
    normal = pre = mellitus = 0
    
    for i in range(0, x):
        # The oral tolerance test.
        m = generate_oral_tolerance(0 if i < int(x / 3) else (1 if i < 2 * int((x / 3)) else 2))

        # In fasting test.
        n = random.randint(126, 3 * 126) if m >= 200 else (random.randint(0, 99) if m < 140 else random.randint(100, 125))

        # The casual test. o -ge than 200 if m >= 200 too.
        o = random.randint(200, 400) if m >= 200 else random.randint(0, 199)

        # Constructing a "Report" obj.
        report = Report(n, m, o)

        # Logging generated data
        if report.result == 0:
            normal += 1
        elif report.result == 1:
            pre += 1
        else:
            mellitus += 1

        # If u want to see the generated results, uncomment the following lines: 
        # print(f"n is {n}, m is {m} and o is {o}")
        # print(f"Report's diagnosis is {report.result}")

        # Appending it into the dataset
        generated_data.append(report)

    print(f"\nDiagnosis generated data --> Normal: {normal}, Pre: {pre}, Mellitus: {mellitus}")
    return generated_data

# Returns a predict model already ready for predicting.
def make_learn_model():    
    # Storing all data in a list of "Report" objects.
    dataset = generate_dataset(10000)

    # Generating classifier
    classifier = tree.DecisionTreeClassifier()
    
    # Fitting our model to our generated data.    
    # Also, converting each entry in our dataset into a "readable" one for our predict model (a multidimensional array) and its result (0, 1, 2).
    classifier.fit([data.raw() for data in dataset], [data.result for data in dataset])

    # Returning our predict model
    return classifier

# Gets a report from the user.
def input_report():
    try:
        inFasting = int(input("When fasting, your glycemia is... "))
        oralTolerance = int(input("What's the result of your oral tolerance test? "))
        casual = int(input("Your normal level of glycemia is... "))

        return Report(inFasting, oralTolerance, casual).raw()

    except:
        return []

# With a predict model and data, predicts and returns the diagnosis.
def predict(model, data):
    return model.predict([data])

# Shows the default menu, gets an inputted option from the user and validates it.
def show_menu(predict_model):
    while True:
        print("[0] --> Diagnosis.")
        print("[1] --> Exit.")

        try:
            opt = int(input("\nSelect an option: "))
            if opt == 1:
                print("\nBye bye!")
                sys.exit()

            elif opt == 0:
                print()

                data = input_report()
                diagnosis = predict(predict_model, data)
                
                if len(diagnosis) == 0:
                    raise ValueError("Invalid inputted data.")

                if diagnosis == [0]:
                    print("Diagnosis result: No diabetes.")
                elif diagnosis == [1]:
                    print("Diagnosis result: Prediabetes.")
                else:
                    print("Diagnosis result: Diabetes mellitus.")

            else:
                raise ValueError("Invalid option.")

        except Exception:
            print("Oops! Looks like your selected option isn't a valid one. Please, try again.\n")

show_disclaimer()

print("Starting software...")
print("Getting all reports and generating dataset...")
print("Our model is learning... please, wait a little.")

model = make_learn_model()
print("The predict model is ready!\n")

show_menu(model)

# Showing disclaimer (again =)
print()
show_disclaimer()
