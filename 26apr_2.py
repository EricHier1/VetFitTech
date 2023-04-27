import random
from streprogen import Program

        
def main():
    # Set a seed for the random number generator for reproducible results
    random.seed(123)

    while True:
        print("\nStrength Program Generator")
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
    name = input("Enter program name: ")

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


if __name__ == "__main__":
    main()
