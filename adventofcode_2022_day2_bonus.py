'''
--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says 
how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, 
and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose 
so the round ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), 
    so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a 
    score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes 
exactly according to your strategy guide?

https://adventofcode.com/2022/day/2/input
'''
#imports

#variables
file_name = "adventofcode_2022_day2_input.txt"
file_handle = open(file_name,"r")
player_total_score = 0

#creae a dictionary of values
# A-X is Rock 1pt, B-Y is Paper 2pt, C-Z is Siccors 3pt
# 0 for a loss, 3 for a draw, 6 for a win
abc_xyz_value_key = [('A',1),('B',2),('C',3)]
round_score_key = [('X',0),('Y',3),('Z',6)]
loss_key = []
draw_key = []
win_key = []

#read line
for line in file_handle:
    opponent_play = line[0]
    play_to_make = line[2]
    
    #check what play player makes and score
    if opponent_play == 'A':
        if play_to_make == 'Z':
            player_total_score = player_total_score + 8
        elif play_to_make == 'Y':
            player_total_score = player_total_score + 4
        elif play_to_make == 'X':
            player_total_score = player_total_score + 3
    elif opponent_play == 'B':
        if play_to_make == 'Z':
            player_total_score = player_total_score + 9
        elif play_to_make == 'Y':
            player_total_score = player_total_score + 5
        elif play_to_make == 'X':
            player_total_score = player_total_score + 1
    elif opponent_play == 'C':
        if play_to_make == 'Z':
            player_total_score = player_total_score + 7
        elif play_to_make == 'Y':
            player_total_score = player_total_score + 6
        elif play_to_make == 'X':
            player_total_score = player_total_score + 2


    
    # #check how you are supposed to play the round
    # for round in round_score_key:
    #     # print(round[0])
    #     # print(line)
    #     if (round[0].strip()) == play_to_make.strip():
    #         player_total_score = player_total_score + round[1]
    #     # else:
    #     #     print("Error, no round match found")
    print(line)
    print(player_total_score)
        
    


