'''
--- Day 2: Rock Paper Scissors ---

The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z

This strategy guide predicts and recommends the following:

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

To begin, get your puzzle input. https://adventofcode.com/2022/day/2/input
'''
#imports

#variables
file_name = "adventofcode_2022_day2_input.txt"
file_handle = open(file_name,"r")
player_total_score = 0

#creae a dictionary of values
# A-X is Rock 1pt, B-Y is Paper 2pt, C-Z is Siccors 3pt
# 0 for a loss, 3 for a draw, 6 for a win
abc_xyz_value_key = [('A',1),('X',1),('B',2),('Y',2),('C',3),('Z',3)]
round_score_key = [('C X',6),('B Z',6),('A Y',6),
('A X',3), ('B Y',3), ('C Z',3),
('A Z',0),('B X',0),('C Y',0)]

#read line
for line in file_handle:
    opponent_play = line[0]
    player_play = line[2]
    #check what player play score is
    for play in abc_xyz_value_key:
        if (play[0]) == player_play:
            player_total_score = player_total_score + play[1]
            break
    #check if play won round
    for round in round_score_key:
        # print(round[0])
        # print(line)
        if (round[0].strip()) == line.strip():
            player_total_score = player_total_score + round[1]
        # else:
        #     print("Error, no round match found")
    print(line)
    print(player_total_score)
        
    


