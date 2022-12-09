'''
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying 
the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the 
top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they 
still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf 
(with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these 
three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

To begin, get your puzzle input. https://adventofcode.com/2022/day/1/input
'''
#imports
import pandas as pd

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
        elf_name = (f'{"elf_"}{elf_number}')
        list_of_elfs.append((elf_name, total_calories))
        #print(list_of_elfs)
        elf_number +=1
        total_calories = 0
    #if no line break is detected continue summing calories for elf
    else:
        number = int(line)
        total_calories = total_calories + number

#turn list into a dataframe
df_of_elfs_n_calories = pd.DataFrame(list_of_elfs,columns=['elf','total_calories'])
#print(df_of_elfs_n_calories)
#print(df_of_elfs_n_calories.sort_values(by=['total_calories'], ascending=False))
top_three_elf_calorie_sum = df_of_elfs_n_calories.total_calories.nlargest(3).sum()
print(top_three_elf_calorie_sum)