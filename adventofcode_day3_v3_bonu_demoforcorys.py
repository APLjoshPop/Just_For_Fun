'''
--- Day 3: Rucksack Reorganization ---

--- Part Two ---

As you finish identifying the misplaced items, the Elves come to you with another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg

And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.

Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

To begin, get your puzzle input. https://adventofcode.com/2022/day/3/input

'''

#imports
score_list = []
total_score = 0

#variables
list_of_lines = []
list_index = 0
list_of_matches = []
number_of_lines = 0

#read the input
file_name = "adventofcode_2022_day3_input.txt"
# file_name = "adventofcode_2022_day3_input_test.txt"

file_handle = open(file_name,"r")

#put all lines in a list so the lines can be taken out as variables in order
for line in file_handle:
    list_of_lines.append(line)

#need to know how many lines to set limit on while loop
number_of_lines = len(list_of_lines)

#go through the list in groups of three and compare the lines to find matching letter
while number_of_lines > list_index:
    #perform loop until the list index is divisable by 3, this breaks list_of_lines into groups of three
    while (list_index + 1)%3 != 0:
        line_1 = list_of_lines[list_index]
        list_index +=1
        line_2 = list_of_lines[list_index]
        list_index +=1
        line_3 = list_of_lines[list_index]

    print(line_1)
    print(line_2)
    print(line_3)

    #create a set for each of the lines in a group and find the letter in each that is the same
    #using the intersection property of sets
    line_match = set(line_1) & set(line_2) & set(line_3)
    print(line_match)

    #when a match is found change it from a set to a list and add it to a list of matches
    line_match = list(line_match)
    list_of_matches.append(line_match)
    # print(list_of_matches)

    #incriment the list_index to get to the next set of three and so the while loop eventually terminates.
    list_index +=1

# print(list_of_matches)

#score the pack using the ASCII value. since values start at a =1 and increase alphabetically...
#...and linearly to Z = 52. an lower case and upper case ascii values increase linearly respectively.
for match in list_of_matches:
    match = match[0]
    if match.isupper():
        score = (ord(match)-38)
    else:
        score = (ord(match)-96)
        
    total_score = total_score + score

# print(score_list)
print(total_score)

    