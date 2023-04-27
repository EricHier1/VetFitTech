import tkinter as tk
from tkinter import messagebox

class TDEECalculator:
    def __init__(self, gender, weight, height, age, activity_level):
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age
        self.activity_level = activity_level
        self.bmr = None
        self.tdee = None

    def calculate_bmr(self):
        if self.gender == 'Male':
            self.bmr = 88.36 + (13.4 * self.weight) + (4.8 * self.height) - (5.7 * self.age)
        elif self.gender == 'Female':
            self.bmr = 447.6 + (9.2 * self.weight) + (3.1 * self.height) - (4.3 * self.age)

    def calculate_tdee(self):
        activity_levels = {
            'Sedentary': 1.2,
            'Lightly Active': 1.375,
            'Moderately Active': 1.55,
            'Very Active': 1.725,
            'Extremely Active': 1.9
        }
        self.tdee = self.bmr * activity_levels[self.activity_level]

class MealPlanGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title('Meal Plan Generator')

        # TDEE Calculator Frame
        tdee_frame = tk.LabelFrame(self.master, text='TDEE Calculator')
        tdee_frame.pack(padx=10, pady=10)

        gender_label = tk.Label(tdee_frame, text='Gender:')
        gender_label.grid(row=0, column=0, padx=10, pady=5, sticky='W')
        self.gender_var = tk.StringVar(value='Male')
        gender_radiobutton1 = tk.Radiobutton(tdee_frame, text='Male', variable=self.gender_var, value='Male')
        gender_radiobutton1.grid(row=0, column=1, padx=5, pady=5)
        gender_radiobutton2 = tk.Radiobutton(tdee_frame, text='Female', variable=self.gender_var, value='Female')
        gender_radiobutton2.grid(row=0, column=2, padx=5, pady=5)

        weight_label = tk.Label(tdee_frame, text='Weight (kg):')
        weight_label.grid(row=1, column=0, padx=10, pady=5, sticky='W')
        self.weight_entry = tk.Entry(tdee_frame)
        self.weight_entry.grid(row=1, column=1, padx=5, pady=5)

        height_label = tk.Label(tdee_frame, text='Height (cm):')
        height_label.grid(row=2, column=0, padx=10, pady=5, sticky='W')
        self.height_entry = tk.Entry(tdee_frame)
        self.height_entry.grid(row=2, column=1, padx=5, pady=5)

        age_label = tk.Label(tdee_frame, text='Age:')
        age_label.grid(row=3, column=0, padx=10, pady=5, sticky='W')
        self.age_entry = tk.Entry(tdee_frame)
        self.age_entry.grid(row=3, column=1, padx=5, pady=5)

        activity_level_label = tk.Label(tdee_frame, text='Activity Level:')
        activity_level_label.grid(row=4, column=0, padx=10, pady=5, sticky='W')
        activity_level_options = ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Extremely Active']
        self.activity_level_var = tk.StringVar(value=activity_level_options[0])
        activity_level_menu = tk.OptionMenu(tdee_frame, self.activity_level_var, *activity_level_options)
        activity_level_menu.grid(row=4, column=1, padx=5, pady=5)


        calculate_button = tk.Button(tdee_frame, text='Calculate', command=self.calculate_tdee)
        calculate_button.grid(row=5, column=0, padx=10, pady=5)

        clear_button = tk.Button(tdee_frame, text='Clear', command=self.clear_tdee_inputs)
        clear_button.grid(row=5, column=1, padx=10, pady=5)

        # Meal Plan Generator Frame
        meal_plan_frame = tk.LabelFrame(self.master, text='Meal Plan Generator')
        meal_plan_frame.pack(padx=10, pady=10)

        protein_label = tk.Label(meal_plan_frame, text='Protein (g):')
        protein_label.grid(row=0, column=0, padx=10, pady=5, sticky='W')
        self.protein_entry = tk.Entry(meal_plan_frame)
        self.protein_entry.grid(row=0, column=1, padx=5, pady=5)

        carb_label = tk.Label(meal_plan_frame, text='Carbohydrate (g):')
        carb_label.grid(row=1, column=0, padx=10, pady=5, sticky='W')
        self.carb_entry = tk.Entry(meal_plan_frame)
        self.carb_entry.grid(row=1, column=1, padx=5, pady=5)

        fat_label = tk.Label(meal_plan_frame, text='Fat (g):')
        fat_label.grid(row=2, column=0, padx=10, pady=5, sticky='W')
        self.fat_entry = tk.Entry(meal_plan_frame)
        self.fat_entry.grid(row=2, column=1, padx=5, pady=5)

        calories_label = tk.Label(meal_plan_frame, text='Calories:')
        calories_label.grid(row=3, column=0, padx=10, pady=5, sticky='W')
        self.calories_entry = tk.Entry(meal_plan_frame, state='readonly')
        self.calories_entry.grid(row=3, column=1, padx=5, pady=5)

        generate_button = tk.Button(meal_plan_frame, text='Generate Meal Plan', command=self.generate_meal_plan)
        generate_button.grid(row=4, column=0, padx=10, pady=5)

        clear_button = tk.Button(meal_plan_frame, text='Clear', command=self.clear_meal_plan_inputs)
        clear_button.grid(row=4, column=1, padx=10, pady=5)

    def calculate_tdee(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            age = int(self.age_entry.get())
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid inputs for weight, height, and age.')
            return

        self.activity_level = self.activity_level_var.get()

        self.tdee_calculator = TDEECalculator(self.gender_var.get(), weight, height, age, self.activity_level)
        self.tdee_calculator.calculate_bmr()
        self.tdee_calculator.calculate_tdee()

        if self.tdee_calculator.tdee:
            messagebox.showinfo('TDEE Result', f'Your TDEE is {self.tdee_calculator.tdee:.2f} calories per day.')
        else:
            messagebox.showerror('Error', 'An error occurred while calculating your TDEE. Please try again.')

    def clear_tdee_inputs(self):
        self.gender_var.set('Male')
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.activity_level_var.set('Sedentary')

    def generate_meal_plan(self):
        try:
            protein = float(self.protein_entry.get())
            carb = float(self.carb_entry.get())
            fat = float(self.fat_entry.get())
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid inputs for protein, carbohydrate, and fat.')
            return

        total_calories = (protein * 4) + (carb * 4) + (fat * 9)
        self.calories_entry.configure(state='normal')
        self.calories_entry.delete(0, tk.END)
        self.calories_entry.insert(0, f'{total_calories:.2f}')
        self.calories_entry.configure(state='readonly')

        if not self.tdee_calculator:
            messagebox.showerror('Error', 'Please calculate your TDEE first.')
            return

        calorie_difference = self.tdee_calculator.tdee - total_calories

        if calorie_difference < -500:
            messagebox.showerror('Error', 'You need to eat less.')
        elif calorie_difference < -250:
            messagebox.showwarning('Warning', 'You should eat less.')
        elif calorie_difference > 500:
            messagebox.showerror('Error', 'You need to eat more.')
        elif calorie_difference > 250:
            messagebox.showwarning('Warning', 'You should eat more.')
        else:
            messagebox.showinfo('Success', 'Your meal plan has been generated successfully.')

    def clear_meal_plan_inputs(self):
        self.protein_entry.delete(0, tk.END)
        self.carb_entry.delete(0, tk.END)
        self.fat_entry.delete(0, tk.END)
        self.calories_entry.configure(state='normal')
        self.calories_entry.delete(0, tk.END)
        self.calories_entry.configure(state='readonly')

        self.tdee_calculator = None

if __name__ == '__main__':
    root = tk.Tk()
    meal_plan_generator = MealPlanGenerator(root)
    root.mainloop()
