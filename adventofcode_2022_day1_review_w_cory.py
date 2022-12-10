'''
--- Day 1: Calorie Counting ---

Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver 
presents on Christmas. For that, their favorite snack is a special type of star fruit that only grows deep 
in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th.
Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see 
along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent 
calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' 
expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of 
their supplies. One important consideration is food - in particular, the number of Calories each Elf is 
carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. 
that they've brought with them, one item per line. Each Elf separates their own inventory from the previous
Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

This list represents the Calories of the food carried by five Elves:

    The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
    The second Elf is carrying one food item with 4000 Calories.
    The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
    The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
    The fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: 
they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example
above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

To begin, get your puzzle input. https://adventofcode.com/2022/day/1/input
'''
#imports

#variables
file_name = "adventofcode_2022_day1_input.txt"
file_handle = open(file_name,"r")
total_calories = 0
elf_number = 1
list_of_elfs = []

#read file, and sum integers until break is encountered...
#...and enter that sum in a tupled list: example elf_1, 50000
#...order the list and find the elf with the most calories
for line in file_handle:
    line = line.rstrip()
    #detect a line beak and assign current sum to elf
    if line == '':
        elf_name = (f'{"elf_"}{elf_number}{ " total calories: "}')
        list_of_elfs.append((elf_name, total_calories))
        #print(list_of_elfs)
        elf_number +=1
        total_calories = 0
    #if no line break is detected continue summing calories for elf
    else:
        number = int(line)
        total_calories = total_calories + number

#sort the list
list_of_elfs = sorted(list_of_elfs, key=lambda x: x[1])

#uncomment below for list of elfs
#for elf in list_of_elfs:
    #print(elf)
print(list_of_elfs[-1])

#Notes: 
#dispose of file handle at end. use with open("input-1, txt", "r") as file so it will automatically close once open. 
# ...then: line = file.readline()
#but needs fixing, forgot last elf!
#if current_elf_calories != 0:
#   elves.append(current_elf_calories)
#   current_elf_calories = 0
#print(max(elves)) instead of sorting and grabbing end. but doesn't work with list of tuples needs to just be a list of integers
#YAGNI : you aint gonna need it. don't need elf number



        
