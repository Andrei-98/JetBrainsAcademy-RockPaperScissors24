import random


class RockPaperScissors:

    def __init__(self):
        """this could CAN be shortened every thing after 8 steps beats the thing
        you picked until the thing u picked look into it"""
        self.game = ("rock", "paper", "scissors")
        self.user = None
        self.user_game = None
        self.user_input = None
        self.user_rating = 0
        self.players = None
        self.cpu = None
        self.menu()

    def menu(self):
        self.get_user()
        self.get_players()
        self.get_game()
        while self.user_input != "!exit":
            self.user_input = input()
            if self.user_input == "!exit" or self.check_user_input() is False:
                continue
            self.cpu = random.choice(list(self.game))
            self.check_win()
        self.push_rating()
        print("Bye!")

    def get_user(self):
        self.user = input("Enter your name: ")
        print(f"Hello, {self.user}")

    def get_players(self):
        """reads the scores transforms them into a string then a list then a dict, then sets the rating for the user"""
        self.players = [a.split() for a in open("rating.txt", "r").read().splitlines()]
        self.players = {a[0]: int(a[1]) for a in self.players}
        print(self.players)

        if self.user in self.players:
            self.user_rating = self.players[self.user]
        else:
            self.players[self.user] = 0

    def get_game(self):
        self.user_game = input()
        if self.user_game.strip() != "":
            self.game = ("rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper",
                         "sponge", "wolf", "tree", "human", "snake", "scissors", "fire")
        print("Okay, let's start")

    def check_user_input(self):
        if self.user_input == "!rating":
            print(f"Your rating: {self.user_rating}")
            return False
        elif self.user_input not in self.game:
            print("Invalid input")
            return False

    def check_win(self):
        if self.user_input == self.cpu:
            self.user_rating += 50
            print(f"There is a draw {self.cpu}")
        else:
            offset = (self.game.index(self.cpu) - self.game.index(self.user_input)) % len(self.game)
            if offset > len(self.game) // 2:
                self.user_rating += 100
                print(f"Well done. Computer chose {self.cpu} and failed")
            else:
                print(f"Sorry, but computer chose {self.cpu}")

    def push_rating(self):
        """updates the rating for current user in the dict then writes the list of players in rating.txt"""
        self.players[self.user] = self.user_rating

        file = open("rating.txt", "w")
        for i in self.players:
            file.write(f"{i} {self.players[i]}\n")
        file.close()


if __name__ == "__main__":
    RockPaperScissors()
