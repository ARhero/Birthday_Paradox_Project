import random
from datetime import datetime, timedelta

def getBirthdays(num_birthdays):
    # Generate a list of random date objects representing birthdays
    start_date = datetime(2000, 1, 1)  # You can adjust the start date
    birthdays = [start_date + timedelta(days=random.randint(0, 365)) for _ in range(num_birthdays)]
    return birthdays

def getMatch(birthdays):
    # Identify a birthday that occurs more than once in the list
    seen = set()
    for birthday in birthdays:
        if birthday in seen:
            return birthday
        seen.add(birthday)
    return None

def runSimulation(group_size, num_simulations):
    matches = 0
    for _ in range(num_simulations):
        # Generate random birthdays for the group
        group_birthdays = getBirthdays(group_size)
        
        # Check for matching birthdays
        if getMatch(group_birthdays) is not None:
            matches += 1

    probability = (matches / num_simulations) * 100
    return probability

def main():
    while True:
        print("\nBirthday Paradox Simulation")

        # User input and validation
        while True:
            try:
                group_size = int(input("How many birthdays shall I generate? (Max 100) "))
                if 1 <= group_size <= 100:
                    break
                else:
                    print("Please enter a valid group size between 1 and 100.")
            except ValueError:
                print("Please enter a valid integer.")

        num_simulations = 100000  # You can adjust the number of simulations

        # Display generated birthdays for better readability
        birthdays = getBirthdays(group_size)
        print("\nHere are {} birthdays:".format(group_size))
        for birthday in birthdays:
            print(birthday.strftime("%b %d"))

        print("\nGenerating {} random birthdays {} times...".format(group_size, num_simulations))
        input("Press Enter to begin...")

        # Optimize simulation loop for progress updates
        print("\nLet's run another {} simulations.".format(num_simulations))
        for i in range(num_simulations + 1):
            if i % 10000 == 0:
                print("{} simulations run...".format(i))

        # Simulation results and statistics
        probability = runSimulation(group_size, num_simulations)
        print("\nOut of {} simulations of {} people, there was a".format(num_simulations, group_size))
        print("matching birthday in that group {} times. This means".format(round(probability)))
        print("that {} people have a {:.2f} % chance of".format(group_size, probability))
        print("having a matching birthday in their group.")

        # Additional statistics
        average_matches = probability / 100 * num_simulations
        print("On average, {:.2f} people share a birthday in a group of {}.".format(average_matches, group_size))

        # Replay option
        replay = input("\nDo you want to run another simulation? (yes/no) ").lower()
        if replay != 'yes':
            print("Thank you for using the Birthday Paradox Simulation. Goodbye!")
            break

if __name__ == "__main__":
    main()
