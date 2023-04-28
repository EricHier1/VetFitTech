# Weight Loss Program

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

# Function to provide diet and exercise recommendations
def provide_recommendations():
    print("Here are some basic diet and exercise recommendations:")
    print("- Aim to eat a balanced diet that includes plenty of fruits, vegetables, lean protein, and whole grains.")
    print("- Avoid processed foods and sugary drinks, which are often high in calories and low in nutrients.")
    print("- Keep track of your daily calorie intake to ensure you're not eating more than you're burning.")
    print("- Incorporate exercise into your daily routine. Aim for at least 30 minutes of moderate-intensity exercise most days of the week.")
    print("- Get enough sleep each night to ensure your body is properly rested and recovered.")
    print("- Drink plenty of water throughout the day to stay hydrated.")

# Main function to run the program
def main():
    # Get user information
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    age = int(input("Enter your age in years: "))
    gender = input("Enter your gender (male/female): ")
    activity_level = input("Enter your activity level (sedentary/lightly active/moderately active/very active/extra active): ")

    # Calculate daily calorie needs and suggest calorie deficit
    daily_calories = calculate_daily_calories(weight, height, age, gender, activity_level)
    calorie_deficit = suggest_calorie_deficit(daily_calories)

    # Print results
    print("Your daily calorie needs are:", daily_calories)
    print("To lose weight, you should aim for a calorie deficit of:", calorie_deficit)
    provide_recommendations()

# Call the main function to run the program
main()
