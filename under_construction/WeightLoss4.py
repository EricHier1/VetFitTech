import tkinter as tk
from tkinter import ttk

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

#Calculate time
def calculate_time_estimate(calorie_deficit):
    if calorie_deficit > 0:
        weeks = abs(int((calorie_deficit * 7) / 3500))
        return f"You can expect to lose about {weeks} pounds per week if you maintain this calorie deficit."
    else:
        return "You are not in a calorie deficit. To lose weight, you need to burn more calories than you consume."

# Function to suggest a calorie deficit
def suggest_calorie_deficit(daily_calories):
    calorie_deficit = int(daily_calories * 0.2)
    return calorie_deficit

# Function to provide personalized diet and exercise recommendations
def provide_recommendations(weight, height, age, gender, activity_level, target_weight, output_text):
    # Calculate daily calorie needs and suggest calorie deficit
    daily_calories = calculate_daily_calories(weight, height, age, gender, activity_level)
    if target_weight is not None:
        if weight > target_weight:
            calorie_deficit = int((weight - target_weight) * 3500 / 7)
        else:
            calorie_deficit = int((target_weight - weight) * 3500 / 7)
    else:
        calorie_deficit = suggest_calorie_deficit(daily_calories)
        output_text.insert(tk.END, "To lose weight, you should aim for a daily calorie deficit of: " + str(calorie_deficit) + "\n")
    time_estimate = calculate_time_estimate(calorie_deficit)
    output_text.insert(tk.END, time_estimate + "\n")

    # Calculate recommended daily calorie intake for weight loss
    if target_weight is not None:
        if weight > target_weight:
            calorie_intake = daily_calories - calorie_deficit
        else:
            calorie_intake = daily_calories + calorie_deficit
        # Clear previous output and insert new output in the Text widget
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Your daily calorie needs are: " + str(daily_calories) + "\n")
        output_text.insert(tk.END, "To reach your target weight of " + str(target_weight) + " you should aim for a daily calorie intake of: " + str(calorie_intake) + "\n")
        output_text.insert(tk.END, "To reach your target weight of " + str(target_weight) + " you should aim for a daily calorie deficit of: " + str(calorie_deficit) + "\n")
    else:
        calorie_intake = daily_calories - calorie_deficit
        output_text.insert(tk.END, "To lose weight, you should aim for a daily calorie deficit of: " + str(calorie_deficit) + "\n")

    # Print personalized recommendations
    output_text.insert(tk.END, "Here are some personalized diet and exercise recommendations:\n")
    output_text.insert(tk.END, "- Aim to eat a balanced diet that includes plenty of fruits, vegetables, lean protein, and whole grains.\n")
    output_text.insert(tk.END, "- Avoid processed foods and sugary drinks, which are often high in calories and low in nutrients.\n")
    output_text.insert(tk.END, "- Keep track of your daily calorie intake to ensure you're not eating more than you're burning.\n")
    output_text.insert(tk.END, "- Incorporate exercise into your daily routine. Aim for at least 30 minutes of moderate-intensity exercise most days of the week.\n")
    output_text.insert(tk.END, "- Get enough sleep each night to ensure your body is properly rested and recovered.\n")
    output_text.insert(tk.END, "- Drink plenty of water throughout the day to stay hydrated.\n")


def set_target_weight(target_weight_entry):
    target_weight = target_weight_entry.get()
    if target_weight:
        target_weight = int(target_weight)
        return target_weight
    else:
        return None

def submit_form():
    weight = int(weight_entry.get())
    height = int(height_entry.get())
    age = int(age_entry.get())
    gender = gender_combobox.get().lower()
    activity_level = activity_level_combobox.get().lower()
    target_weight = set_target_weight(target_weight_entry)

    provide_recommendations(weight, height, age, gender, activity_level, target_weight, output_text)

# Create the GUI window
root = tk.Tk()
root.title("Calorie Calculator")

# Create and position labels, entries, and comboboxes
tk.Label(root, text="Weight (pounds):").grid(row=0, column=0, sticky="w")
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

tk.Label(root, text="Height (inches):").grid(row=1, column=0, sticky="w")
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

tk.Label(root, text="Age (years):").grid(row=2, column=0, sticky="w")
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

tk.Label(root, text="Gender:").grid(row=3, column=0, sticky="w")
gender_combobox = ttk.Combobox(root, values=["Male", "Female"], state="readonly")
gender_combobox.grid(row=3, column=1)

tk.Label(root, text="Activity level:").grid(row=4, column=0, sticky="w")
activity_level_combobox = ttk.Combobox(root, values=["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"], state="readonly")
activity_level_combobox.grid(row=4, column=1)

tk.Label(root, text="Target weight (pounds, optional):").grid(row=5, column=0, sticky="w")
target_weight_entry = tk.Entry(root)
target_weight_entry.grid(row=5, column=1)

# Create and position the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=6, columnspan=2)

def reset_form():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_combobox.set('')
    activity_level_combobox.set('')
    target_weight_entry.delete(0, tk.END)
    output_text.delete(1.0, tk.END)

# Create and position the reset button
reset_button = tk.Button(root, text="Reset", command=reset_form)
reset_button.grid(row=6, column=1)

# Create and position the output Text widget
output_text = tk.Text(root, wrap=tk.WORD, width=80, height=20)
output_text.grid(row=7, columnspan=2)


# Run the GUI event loop
root.mainloop()

