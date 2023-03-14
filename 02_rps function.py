# checks for rock paper or scissors entered by player
def choice_checker(question):
    while True:

        response = input(question).lower()

        if response == "rock" or response == "r":
            return "rock"

        elif response == "paper" or response == "p":
            return "paper"

        elif response == "scissors" or response == "s":
            return "scissors"

        # gives an error if player enters an invalid answer
        else:
            print("")
            print(error)
            print("")


# presets variables
error = "please enter rock, paper or scissors as your response"


choice_checker("Rock Paper or Scissors: ")
