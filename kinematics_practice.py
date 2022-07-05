import math
import random


class PhysicsPractice:
    def __init__(self):
        self.session_questions = 0  # Number of questions to be solved this session
        self.total_questions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # number of questions to randomly choose from
        self.question = 0  # Current question number from list of questions
        self.vars = [0] * 6  # List of variables to be used for the question
        self.ans = 0  # Actual calculated answer for question
        self.error_threshold = 5  # Accepted percent error
        self.correct = 0  # Total number of correct answers in this session

    # 6 possible variables in the several kinematics equations, randomly generated here
    def randomize_variables(self, num_vars: int):
        for j in range(num_vars):
            self.vars[j] = round(random.uniform(5, 50), 3)

    def compute(self):
        # Get user-input and if not a float, raise error and try again
        ans_input = None
        while ans_input is None:
            try:
                ans_input = input("\nPlease input your answer, rounded to 3 decimal places: ")
                ans_input = round(float(ans_input), 3)
            except ValueError:
                print("Error: The answer needs to be an integer or decimal number.")

        if self.ans is not None:
            perc_diff = round(abs((ans_input - self.ans) / self.ans) * 100, 3)
            if perc_diff <= self.error_threshold:
                print("\nCORRECT!")
                self.correct += 1
            else:
                print("\nWrong answer :(")
            print("The actual answer is", self.ans)
            print("You were {}% off from the true value".format(perc_diff))
        else:
            print('Error')

    # Randomly assign a question from this series of kinematics questions
    def kinematics(self) -> float or None:
        a, d, t, k, vf, vi = self.vars[0], self.vars[1], self.vars[2], self.vars[3], self.vars[4], self.vars[5]
        self.question = random.choice(self.total_questions)
        print()
        if self.question == 1:
            if d <= k:
                d, k = k, d
            print("A ball thrown straight up reaches a height of", d,
                  "meters \nbefore starting to fall back to the ground. "
                  "At what velocity will \na person catch the ball",
                  k, "meters above the ground?")
            self.ans = round(-math.sqrt(19.6 * (d - k)), 3)
        elif self.question == 2:
            print("A race car accelerates uniformly from", vi, "m/s to", vf, "m/s \nin", t,
                  "seconds. What distance did the car travel in meters?")
            self.ans = round(vi * t + (a * t * t) / 2, 3)
        elif self.question == 3:
            print("A train traveling at", vi, "m/s accelerates at", a, "m/s/s for \na displacement of", d,
                  "m. What is the train's final velocity in m/s")
            self.ans = round(math.sqrt(vi * vi + 2 * a * d), 3)
        elif self.question == 4:
            print("A feather is dropped at a height of", d,
                  "meters on the moon\nwhere the acceleration of "
                  "gravity is 1/6 of Earth's gravitational acceleration."
                  "\nHow long does it take the feather to reach the ground in seconds?")
            self.ans = round(math.sqrt(2 * d / (9.8 / 6)), 3)
        elif self.question == 5:
            print("A bullet leaves a rifle with a muzzle velocity of", vf,
                  "m/s.\nWhile accelerating through the barrel of the rifle, the bullet moves a distance of", d,
                  "centimeters.\nWhat is the acceleration of the bullet in m/s/s")
            self.ans = round((50 * vf * vf) / (a * d), 3)
        elif self.question == 6:
            print("A jaguar begins to accelerate for", t, "seconds. In this time\nthe jaguar has traveled", d,
                  "meters.\nWhat is the jaguar's average acceleration?")
            self.ans = round((2 * d) / (t * t), 3)
        elif self.question == 7:
            print("A moving boat begins accelerating upstream at", a, "m/s/s\nagainst water that is moving at", k,
                  "m/s.\nIf the boat requires", t, "seconds to travel", d,
                  "meters\nwhat is the boat's initial velocity in m/s?")
            self.ans = round((2 * d - a * t * t) / t + k, 3)
        elif self.question == 8:
            print("A car traveling at a constant speed of", vi,
                  "m/s passes a highway patrol car, which is at rest."
                  "\nThe police officer accelerates at a constant rate of", a,
                  "m/s/s and\nmaintains this rate of acceleration until he pulls next to the speeding car."
                  "\nAssume that the police car starts to move at the moment the speeder passes the police car."
                  "\nWhat is the time required for the police officer to catch the speeder?")
            self.ans = round(vi / (a / 2), 3)
        elif self.question == 9:
            print("A stone thrown vertically upward on Earth was recorded at a\nvelocity of", k,
                  "m/s after travelling 2/3 of its maximum height.\nWhat is the stone's maximum height?")
            self.ans = round((3 * k * k) / 19.6, 3)
        elif self.question == 10:
            print("A plane at rest begins accelerating at", a, "m/s/s\nfor", t,
                  "seconds before taking off at the end of the runway.\nHow long is the runway?")
            self.ans = round(abs((a * t * t) / 2), 3)
        else:
            self.ans = None


if __name__ == '__main__':
    practice = PhysicsPractice()
    practice.session_questions = int(input("How many questions would you like to practice this session? "))
    for i in range(practice.session_questions):
        practice.randomize_variables(6)
        practice.kinematics()
        practice.compute()
    print(f"You got {practice.correct} out of {practice.session_questions} questions right."
          f"\nYour score is {practice.correct * 100 / practice.session_questions}%."
          "\nThanks for practicing kinematics today!")
