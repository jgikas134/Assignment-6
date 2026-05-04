def main():
    # daily steps goal
    def set_steps_goal():
        goal = int(input("Enter your daily steps goal: "))
        return goal

    # daily steps for 7 days
    def record_daily_steps():
        total_steps = 0

        for day in range(1, 8):
            steps = int(input(f"Enter the number of steps for day {day}: "))
            total_steps = total_steps + steps

        return total_steps

    # evaluate weekly performance
    def evaluate_weekly_performance(goal, total_steps):
        average_steps = total_steps / 7

        print(f"Your average daily steps for the week is {average_steps:.2f}.")

        if average_steps > goal:
            print(f"You exceeded your daily steps goal on average.")
        elif average_steps == goal:
            print(f"You met your daily steps goal on average.")
        else:
            print(f"You did not meet your daily steps goal on average.")

    daily_goal = set_steps_goal()
    weekly_total = record_daily_steps()
    evaluate_weekly_performance(daily_goal, weekly_total)


main()