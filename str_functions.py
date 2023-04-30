import random
from streprogen import Program
from tkinter import messagebox
import tkinter as tk

# All the functions from your original code


def main():
    # Set a seed for the random number generator for reproducible results
    random.seed(123)

    while True:
        print("\nFitTechVet Strength Program Generator")
        print("1. Create a new strength program")
        print("2. Exit")
        choice = validate_input("Enter your choice (1 or 2): ", int)

        if choice == 1:
            create_strength_program()
        elif choice == 2:
            print("Exiting the program...")
            break


def validate_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")
            continue


def create_strength_program():
    # Get program name
    name = input("Enter training program name: ")

    # Get program duration
    duration = get_program_duration()

    # Get number of reps per exercise
    reps_per_exercise = int(
        input("Enter number of reps per exercise (suggest 22-28 range): "))

    # Get unit for weights
    weight_unit = get_weight_unit()

    # Get rounding interval
    rounding_interval = float(
        input("Enter rounding interval (2.5 for kg, 5 for lbs): "))

    # Get intensity as a percentage of 1RM
    intensity = int(input("Enter intensity as a percentage of 1RM: "))

    # Get the level of the program and starting weights
    bench_start_weight, squat_start_weight, deadlift_start_weight = get_program_level()

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

    # Print the program
    print("\nGenerated Strength Program:")
    print(program)

    # Export the program to a file
    export_program(program, name)


def get_program_duration():
    duration_options = {
        1: 4,
        2: 8,
        3: 12,
        4: 16,
    }

    while True:
        print("\nProgram duration (in weeks):")
        for key, value in duration_options.items():
            print(f"{key}. {value} weeks")
        print("5. Custom")
        duration_choice = validate_input(
            "Enter your choice (1, 2, 3, 4, or 5): ", int)

        if duration_choice in duration_options:
            return duration_options[duration_choice]
        elif duration_choice == 5:
            return int(input("How many weeks do you want your program to be? "))
        else:
            print("Invalid choice. Please try again.")


def get_weight_unit():
    unit_options = {
        1: "kg",
        2: "lbs",
        3: "",
    }

    while True:
        print("\nUnit for weights:")
        for key, value in unit_options.items():
            print(f"{key}. {value}")
        unit_choice = validate_input("Enter your choice (1, 2, or 3): ", int)

        if unit_choice in unit_options:
            return unit_options[unit_choice]
        else:
            print("Invalid choice. Please try again.")


def get_program_level():
    level_options = {
        1: (60, 80, 80),
        2: (80, 100, 100),
        3: (100, 120, 120),
        4: (120, 140, 140),
    }

    while True:
        print("\nProgram Level:")
        for key in level_options.keys():
            print(f"{key}. Level {key}")
        print("5. Custom")
        level_choice = validate_input(
            "Enter your choice (1, 2, 3, 4, or 5): ", int)

        if level_choice in level_options:
            return level_options[level_choice]
        elif level_choice == 5:
            return (
                int(input("What is your starting everyday 1 rep max for Bench Press? ")),
                int(input("What is your starting everyday 1 rep max for Back Squat? ")),
                int(input("What is your starting everyday 1 rep max for Deadlift? "))
            )
        else:
            print("Invalid choice. Please try again.")


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

    with program.Day("Day 3"):
        program.DynamicExercise(
            name="Squats", start_weight=squat_start_weight, min_reps=random_reps(5, 6), max_reps=random_reps(7, 12), intensity=intensity)
        program.DynamicExercise(
            name="Bench Press", start_weight=bench_start_weight, min_reps=random_reps(5, 6), max_reps=random_reps(7, 12), intensity=intensity)
        # ... (the rest of the exercises remain the same)
        program.StaticExercise(
            "Chin-ups", "3 x 5 (weighted if possible)")
        program.StaticExercise(
            "Barbell Romanian Deadlifts", randomized_reps)
        program.StaticExercise(
            "Dumbbell Flyes or Push-ups", randomized_reps)
        program.StaticExercise("Stomach", randomized_reps)
    pass


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
    ...

# GUI


root = tk.Tk()


def create_gui():
    global program  # Add this line to declare the 'program' variable globally
    program = None
    window = tk.Tk()
    window.title("FitVetTech Strength Program Generator")
    window.geometry("800x600")  # Width x Height

    # Labels
    tk.Label(window, text="Program Name: ").grid(row=0, column=0)
    tk.Label(window, text="Duration (weeks): ").grid(row=1, column=0)
    tk.Label(
        window, text="Reps per exercise (22-28 recommended): ").grid(row=2, column=0)
    tk.Label(window, text="Weight Unit (kg/lbs): ").grid(row=3, column=0)
    tk.Label(window, text="Rounding Interval (2.5 kg or 5 lbs): ").grid(
        row=4, column=0)
    tk.Label(
        window, text="Program Intensity (% of 1RM) (Suggest 80-85%): ").grid(row=5, column=0)
    tk.Label(window, text="Bench Press Starting Weight: ").grid(row=6, column=0)
    tk.Label(window, text="Squat Starting Weight: ").grid(row=7, column=0)
    tk.Label(window, text="Deadlift Starting Weight: ").grid(row=8, column=0)

    # Entries
    program_name_entry = tk.Entry(window)
    program_duration_entry = tk.Entry(window)
    reps_per_exercise_entry = tk.Entry(window)
    weight_unit_entry = tk.Entry(window)
    rounding_interval_entry = tk.Entry(window)
    intensity_entry = tk.Entry(window)
    bench_start_weight_entry = tk.Entry(window)
    squat_start_weight_entry = tk.Entry(window)
    deadlift_start_weight_entry = tk.Entry(window)

    program_name_entry.grid(row=0, column=1)
    program_duration_entry.grid(row=1, column=1)
    reps_per_exercise_entry.grid(row=2, column=1)
    weight_unit_entry.grid(row=3, column=1)
    rounding_interval_entry.grid(row=4, column=1)
    intensity_entry.grid(row=5, column=1)
    bench_start_weight_entry.grid(row=6, column=1)
    squat_start_weight_entry.grid(row=7, column=1)
    deadlift_start_weight_entry.grid(row=8, column=1)

    # Submit Button
    submit_button = tk.Button(window, text="Generate Program", command=lambda: on_submit(window, program_name_entry, program_duration_entry, reps_per_exercise_entry,
                              weight_unit_entry, rounding_interval_entry, intensity_entry, bench_start_weight_entry, squat_start_weight_entry, deadlift_start_weight_entry, output_text))
    submit_button.grid(row=9, column=0, columnspan=2)

    # Output Text widget
    tk.Label(window, text="Generated Strength Program: ").grid(
        row=10, column=0)
    output_text = tk.Text(window, wrap=tk.WORD, height=10, width=60)
    output_text.grid(row=11, column=0, columnspan=2,
                     sticky=tk.N+tk.S+tk.E+tk.W)

    # Export Button
    export_button = tk.Button(window, text="Export Program to HTML",
                              command=lambda: export_program_html(program, program_name_entry.get()))
    export_button.grid(row=12, column=0, columnspan=2)

    # Configure the grid to make the Text widget resizable
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(11, weight=1)

    window.mainloop()


def on_submit(window, program_name_entry, program_duration_entry, reps_per_exercise_entry, weight_unit_entry, rounding_interval_entry, intensity_entry, bench_start_weight_entry, squat_start_weight_entry, deadlift_start_weight_entry, output_text):
    global program  # Add this line to make the 'program' variable accessible globally
    window.after(0, validate_and_run_strength_program, window, program_name_entry, program_duration_entry, reps_per_exercise_entry, weight_unit_entry,
                 rounding_interval_entry, intensity_entry, bench_start_weight_entry, squat_start_weight_entry, deadlift_start_weight_entry, output_text)


def export_program_html(program, name):
    program  # Add this line to make the 'program' variable accessible globally

    if program is None:
        messagebox.showerror("No Program", "Please generate a program first.")
        return

    # Save the program as a HTML file
    with open(f"{name}.html", "w", encoding="utf-8") as file:
        # Control table width (number of sets) by passing the 'table_width' argument
        file.write(program.to_html(table_width=6))

    messagebox.showinfo("Export Success", f"Program exported as {name}.html")


def validate_and_run_strength_program(window, program_name_entry, program_duration_entry, reps_per_exercise_entry, weight_unit_entry, rounding_interval_entry, intensity_entry, bench_start_weight_entry, squat_start_weight_entry, deadlift_start_weight_entry, output_text):
    global program  # Add this line to make the 'program' variable accessible globally

    # Validate user inputs
    try:
        duration = int(program_duration_entry.get())
        reps_per_exercise = int(reps_per_exercise_entry.get())
        rounding_interval = float(rounding_interval_entry.get())
        intensity = float(intensity_entry.get())
        bench_start_weight = int(bench_start_weight_entry.get())
        squat_start_weight = int(squat_start_weight_entry.get())
        deadlift_start_weight = int(deadlift_start_weight_entry.get())
    except ValueError:
        messagebox.showerror(
            "Invalid input", "Please enter valid numeric values.")
        return

    weight_unit = weight_unit_entry.get().lower()

    if weight_unit not in ["kg", "lbs"]:
        messagebox.showerror(
            "Invalid input", "Please enter a valid weight unit (kg or lbs).")
        return

    program_name = program_name_entry.get()
    if not program_name:
        messagebox.showerror("Invalid input", "Please enter a program name.")
        return

    program = None

    # Create the Program instance
    program = Program(
        name=program_name,
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

    # Display the program in the Text widget
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, str(program))


root.after(0, create_gui)

root.mainloop()
