# Function to calculate daily calorie needs
def calculate_daily_calories(weight, height, age, gender, activity_level):
    if gender == "male":
        daily_calories = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == "female":
        daily_calories = (10 * weight) + (6.25 * height) - (5 * age) - 161

    if activity_level == "sedentary":
        daily_calories *= 1.2
    elif activity_level == "lightly active":
        daily_calories *= 1.375
    elif activity_level == "moderately active":
        daily_calories *= 1.55
    elif activity_level == "very active":
        daily_calories *= 1.725
    elif activity_level == "extra active":
        daily_calories *= 1.9

    return int(daily_calories)

# Function to suggest a calorie deficit
def suggest_calorie_deficit(daily_calories):
    calorie_deficit = int(daily_calories * 0.2)
    return calorie_deficit

# Function to provide personalized diet and exercise recommendations
def provide_recommendations(weight, height, age, gender, activity_level, target_weight=None):
    # Calculate daily calorie needs and suggest calorie deficit
    daily_calories = calculate_daily_calories(weight, height, age, gender, activity_level)
    calorie_deficit = suggest_calorie_deficit(daily_calories)

    # Calculate recommended daily calorie intake for weight loss
    if target_weight is not None:
        if weight > target_weight:
            daily_calories = calculate_daily_calories(target_weight, height, age, gender, activity_level)
            calorie_deficit = suggest_calorie_deficit(daily_calories)
        else:
            calorie_surplus = int((target_weight - weight) * 3500 / 7 / 2)
            daily_calories += calorie_surplus
            calorie_deficit = daily_calories - calculate_daily_calories(target_weight, height, age, gender, activity_level)

        # Print recommended daily calorie intake and calorie deficit/surplus
        print("Your daily calorie needs are:", daily_calories)
        if weight > target_weight:
            print("To reach your target weight of", target_weight, "you should aim for a daily calorie deficit of:", calorie_deficit)
        else:
            print("To maintain your current weight and reach your target weight of", target_weight, "you should aim for a daily calorie intake of:", daily_calories)
            print("To reach your target weight of", target_weight, "you should aim for a daily calorie deficit of:", calorie_deficit)
    else:
        print("To lose weight, you should aim for a daily calorie deficit of:", calorie_deficit)

    # Print personalized recommendations
    print("Here are some personalized diet and exercise recommendations:")
    print("- Aim to eat a balanced diet that includes plenty of fruits, vegetables, lean protein, and whole grains.")
    print("- Avoid processed foods and sugary drinks, which are often high in calories and low in nutrients.")
    print("- Keep track of your daily calorie intake to ensure you're not eating more than you're burning.")
    print("- Incorporate exercise into your daily routine. Aim for at least 30 minutes of moderate-intensity exercise most days of the week.")
    print("- Get enough sleep each night to ensure your body is properly rested and recovered.")
    print("- Drink plenty of water throughout the day to stay hydrated.")

def set_target_weight():
    target_weight = input("Enter your target weight in pounds (press enter to skip): ")
    if target_weight:
        target_weight = int(target_weight)
        return target_weight
    else:
        return None

# Main function to run the program
def main():
    # Get user information
    while True:
        try:
            weight = int(input("Enter your weight in pounds: "))
            break
        except ValueError:
            print("Please enter a valid weight in pounds.")

    while True:
        try:
            height = int(input("Enter your height in inches: "))
            break
        except ValueError:
            print("Please enter a valid height in inches.")

    while True:
        try:
            age = int(input("Enter your age in years: "))
            break
        except ValueError:
            print("Please enter a valid age in years.")

    while True:
        gender = input("Enter your gender (male/female): ").lower()
        if gender not in ['male', 'female']:
            print("Please enter a valid gender.")
        else:
            break

    while True:
        activity_level = input("Enter your activity level (sedentary/lightly active/moderately active/very active/extra active): ").lower()
        if activity_level not in ['sedentary', 'lightly active', 'moderately active', 'very active', 'extra active']:
            print("Please enter a valid activity level.")
        else:
            break

    target_weight = set_target_weight()

    # Provide personalized recommendations
    provide_recommendations(weight, height, age, gender, activity_level, target_weight)

# Call the main function to run the program
if __name__ == "__main__":
    main()

