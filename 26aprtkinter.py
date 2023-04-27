import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
from streprogen import Program

def validate_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")
            continue

def add_exercises(program, bench_start_weight, squat_start_weight, deadlift_start_weight, intensity):
    with program.Day("Day 1"):
        program.DynamicExercise(
            name="Squats", start_weight=squat_start_weight, min_reps=random_reps(3, 5), max_reps=random_reps(6, 10), intensity=intensity)
        program.DynamicExercise(
            name="Bench Press", start_weight=bench_start_weight, min_reps=random_reps(3, 5), max_reps=random_reps(6, 10), intensity=intensity)
        program.StaticExercise(
            "Pull-ups", "3 x 5 (weighted if possible)")
        program.StaticExercise("Dumbbell Chest Press", randomized_reps)
        program.StaticExercise("Dumbbell Rows", randomized_reps)
        program.StaticExercise(
            "Hammer Curls or Tricep Extensions", randomized_reps)

    with program.Day("Day 2"):
        program.DynamicExercise(
            name="Deadlifts", start_weight=deadlift_start_weight, min_reps=random_reps(3, 5), max_reps=random_reps(6, 10), intensity=intensity)
        program.DynamicExercise(
            name="Overhead Press", start_weight=(.5 * bench_start_weight), min_reps=random_reps(3, 5), max_reps=random_reps(7, 12), intensity=intensity)
        # ... (the rest of the exercises remain the same)
        program.StaticExercise("Dumbbell Rows", randomized_reps)
        program.StaticExercise("Barbell Lunges", randomized_reps)
        program.StaticExercise(
            "Dumbbell Lateral Raises", randomized_reps)
        program.StaticExercise(
            "Bicep Curls or Tricep Extensions", randomized_reps)


def export_program(program, name):
    export_options = {
        1: "Export to HTML",
        2: "Skip",
    }

    while True:
        print("\nExport Options")
        for key, value in export_options.items():
            print(f"{key}. {value}")
        export_choice = validate_input("Enter your choice (1 or 2): ", int)

        if export_choice == 1:
            # Save the program as a HTML file
            with open(f"{name}.html", "w", encoding="utf-8") as file:
                # Control table width (number of sets) by passing the 'table_width' argument
                file.write(program.to_html(table_width=6))
            break
        elif export_choice == 2:
            print("Skipping export...")
            break
        else:
            print("Invalid choice. Please try again.")


def randomized_reps(week):
    """A static function can return random strings."""
    return random.choice(["3 x 10", "4 x 8", "5 x 8", "2-3 x 20", "4 x 15"])


def random_reps(min_value, max_value):
    return random.randint(min_value, max_value)


class StrengthProgramGeneratorGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Strength Program Generator")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(column=0, row=0, sticky=(
            tk.W, tk.E, tk.N, tk.S), padx=20, pady=20)

        ttk.Label(self.main_frame, text="Strength Program Generator", font=(
            "Helvetica", 18, "bold")).grid(column=0, row=0, columnspan=2, pady=10)

        # Create input widgets
        ttk.Label(self.main_frame, text="Program Name:").grid(
            column=0, row=1, sticky=tk.W)
        self.program_name = ttk.Entry(self.main_frame)
        self.program_name.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=10)

        # Duration
        ttk.Label(self.main_frame, text="Program Duration:").grid(
            column=0, row=2, sticky=tk.W)
        self.duration_var = tk.StringVar(self)
        self.duration_var.set("4")
        self.program_duration = ttk.Combobox(
            self.main_frame, textvariable=self.duration_var)
        self.program_duration["values"] = (4, 8, 12, 16)
        self.program_duration.grid(
            column=1, row=2, sticky=(tk.W, tk.E), padx=10)

        # Reps per exercise
        ttk.Label(self.main_frame, text="Reps per Exercise:").grid(
            column=0, row=3, sticky=tk.W)
        self.reps_per_exercise = ttk.Entry(self.main_frame)
        self.reps_per_exercise.grid(
            column=1, row=3, sticky=(tk.W, tk.E), padx=10)

        # Weight unit
        ttk.Label(self.main_frame, text="Weight Unit:").grid(
            column=0, row=4, sticky=tk.W)
        self.weight_unit_var = tk.StringVar(self)
        self.weight_unit_var.set("kg")
        self.weight_unit = ttk.Combobox(
            self.main_frame, textvariable=self.weight_unit_var)
        self.weight_unit["values"] = ("kg", "lbs", "")
        self.weight_unit.grid(column=1, row=4, sticky=(tk.W, tk.E), padx=10)

        # Rounding interval
        ttk.Label(self.main_frame, text="Rounding Interval:").grid(
            column=0, row=5, sticky=tk.W)
        self.rounding_interval = ttk.Entry(self.main_frame)
        self.rounding_interval.grid(
            column=1, row=5, sticky=(tk.W, tk.E), padx=10)

        # Intensity
        ttk.Label(self.main_frame, text="Intensity (percentage of 1RM):").grid(
            column=0, row=6, sticky=tk.W)
        self.intensity = ttk.Entry(self.main_frame)
        self.intensity.grid(column=1, row=6, sticky=(tk.W, tk.E), padx=10)

        # Program Level
        ttk.Label(self.main_frame, text="Program Level:").grid(
            column=0, row=7, sticky=tk.W)
        self.level_var = tk.StringVar(self)
        self.level_var.set("1")
        self.program_level = ttk.Combobox(
            self.main_frame, textvariable=self.level_var)
        self.program_level["values"] = (1, 2, 3, 4)
        self.program_level.grid(column=1, row=7, sticky=(tk.W, tk.E), padx=10)

        # Generate button
        self.generate_button = ttk.Button(
            self.main_frame, text="Generate Program", command=self.generate_program)
        self.generate_button.grid(column=0, row=8, columnspan=2, pady=10)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)

    def generate_program(self):
        # Get user input
        name = self.program_name.get()
        duration = int(self.program_duration.get())
        reps_per_exercise = int(self.reps_per_exercise.get())
        weight_unit = self.weight_unit.get()
        rounding_interval = float(self.rounding_interval.get())
        intensity = int(self.intensity.get())
        program_level = int(self.program_level.get())

        # Get the level of the program and starting weights
        level_options = {
            1: (60, 80, 80),
            2: (80, 100, 100),
            3: (100, 120, 120),
            4: (120, 140, 140),
        }
        bench_start_weight, squat_start_weight, deadlift_start_weight = level_options[
            program_level]

        # Create the Program instance
        program = Program(
            name=name,
            duration=duration,
            reps_per_exercise=reps_per_exercise,
            units=weight_unit,
            round_to=rounding_interval,
            intensity=intensity,
        )

        # Add exercises to the program
        add_exercises(program, bench_start_weight,
                      squat_start_weight, deadlift_start_weight, intensity)

        # Render the program
        program.render()

        # Export the program to a file
        export_program(program, name)

        messagebox.showinfo("Generated Strength Program",
                            "Your strength program has been successfully generated and saved as an HTML file.")


def main():
    app = StrengthProgramGeneratorGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
