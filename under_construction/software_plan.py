import tkinter as tk
from tkinter import messagebox
import random

def main():
    create_gui()

def create_learning_plan():
    # Get level of the learning plan
    level = skill_var.get()

    # Create the LearningPlan instance
    plan = LearningPlan(name="Custom Plan", duration=4, study_time=60, level=level)

    # Add resources to the learning plan
    add_resources(plan, level)

    # Print the learning plan
    output_text.insert(tk.END, f"\nGenerated Learning Plan:\n{plan}")

class LearningPlan:
    def __init__(self, name, duration, study_time, level):
        self.name = name
        self.duration = duration
        self.study_time = study_time
        self.level = level
        self.resources = []

    def __str__(self):
        result = f"Learning Plan: {self.name}\nDuration: {self.duration} weeks\nDaily Study Time: {self.study_time} minutes\n\nResources:\n"
        for i, resource in enumerate(self.resources, 1):
            result += f"{i}. {resource['name']} - {resource['url']}\n"
            duration = resource.get('duration', 'unknown')
            result += f"   Duration: {duration}\n"
            description = resource.get('description', 'unknown')
            result += f"   Description: {description}\n\n"
        return result

    def add_resource(self, name, url, duration, description):
        self.resources.append({"name": name, "url": url, "duration": duration, "description": description})

def add_resources(plan, level):
    resources = {
        "Beginner": [
            {
                "name": "FreeCodeCamp",
                "url": "https://www.freecodecamp.org/",
                "duration": "4 weeks",
                "description": "Learn web development basics with interactive exercises and projects."
            },
            {
                "name": "Codecademy",
                "url": "https://www.codecademy.com/",
                "duration": "6 weeks",
                "description": "Engaging coding courses in various programming languages and frameworks."
            },
            {
                "name": "MDN Web Docs",
                "url": "https://developer.mozilla.org/",
                "duration": "2 weeks",
                "description": "An extensive reference for web technologies, including HTML, CSS, and JavaScript."
            },
            {
                "name": "Coursera",
                "url": "https://www.coursera.org/",
                "duration": "4 weeks",
                "description": "High-quality online courses from top universities and institutions."
            },
        ],
        "Intermediate": [
            {
                "name": "LeetCode",
                "url": "https://leetcode.com/",
                "duration": "4 weeks",
                "description": "Practice coding problems to improve problem-solving and algorithm skills."
            },
            {
                "name": "HackerRank",
                "url": "https://www.hackerrank.com/",
                "duration": "4 weeks",
                "description": "A platform for coding challenges and competitions in various domains."
            },
            {
                "name": "Exercism",
                "url": "https://exercism.io/",
                "duration": "6 weeks",
                "description": "Code practice and mentorship in multiple programming languages."
            },
            {
                "name": "EdX",
                "url": "https://www.edx.org/",
                "duration": "8 weeks",
                "description": "Online courses from top universities covering various topics and technologies."
            },
        ],
        "Advanced": [
            {
                "name": "Project Euler",
                "url": "https://projecteuler.net/",
                "duration": "4 weeks",
                "description": "A collection of challenging math-related programming problems."
            },
            {
                "name": "TopCoder",
                "url": "https://www.topcoder.com/",
                "duration": "4 weeks",
                "description": "Competitive programming platform with contests and practice problems."
            },
            {
                "name": "Kaggle",
                "url": "https://www.kaggle.com/",
                "duration": "6 weeks",
                "description": "A platform for data science and machine learning competitions."
            },
            {
                "name": "Codeforces",
                "url": "https://codeforces.com/",
                "duration": "4 weeks",
                "description": "Competitive programming contests and a large set of problems to practice."
            },
        ],
    }

    selected_resources = resources.get(level)

    if selected_resources:
        for resource in selected_resources:
            plan.add_resource(resource["name"], resource["url"], resource["duration"], resource["description"]) # include duration and description
    else:
        print(f"Invalid level: {level}")


def clear_text():
    output_text.delete(1.0, tk.END)

def create_gui():
    global skill_var, output_text

    master = tk.Tk()
    master.title("Learning Plan Generator")

    master.grid_rowconfigure(2, weight=1)
    master.grid_columnconfigure(1, weight=1)

    skill_label = tk.Label(master, text="Skill Level:")
    skill_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

    skill_var = tk.StringVar(master)
    skill_var.set("Beginner")
    skill_levels = ["Beginner", "Intermediate", "Advanced"]
    skill_menu = tk.OptionMenu(master, skill_var, *skill_levels)
    skill_menu.grid(row=0, column=1, padx=10, pady=10, sticky="W")

    output_label = tk.Label(master, text="Generated Learning Plan:")
    output_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    output_text = tk.Text(master, wrap=tk.WORD)
    output_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    generate_button = tk.Button(master, text="Generate Learning Plan", command=create_learning_plan)
    generate_button.grid(row=3, column=0, pady=10)

    clear_button = tk.Button(master, text="Clear", command=clear_text)
    clear_button.grid(row=3, column=1, pady=10)

    master.mainloop()


# Entry point
if __name__ == "__main__":
    main()

