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
print(list_of_elfs[-2])
print(list_of_elfs[-3])
top_3_elfs = [list_of_elfs[-1], list_of_elfs[-2], list_of_elfs[-3]]

#@Cory I'm not sure I understand how this sum function works...help?
top_three_elf_total_calories = sum(n for _, n in top_3_elfs)

print(f'The total calories of the three elfs carrying the most calories is: {top_three_elf_total_calories}')
        

