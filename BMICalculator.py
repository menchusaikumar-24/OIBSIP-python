
def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight (in kg) and height (in meters).
    Formula: BMI = weight / (height * height)
    """
    return weight / (height ** 2)

def interpret_bmi(bmi):
    """
    Interpret BMI value and return corresponding category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)
    
    print("Your BMI is: {:.2f}".format(bmi))
    print("You are:", category)

if __name__ == "__main__":
    main()