
#1 Guessing Game
# import random
# n = random.randrange(1,100)
# guess = int(input("Enter any number: "))
# while n!= guess:
#     if guess < n:
#         print("Too low")
#         guess = int(input("Enter number again: "))
#     elif guess > n:
#         print("Too high!")
#         guess = int(input("Enter number again: "))
#     else:
#       break
# print("you guessed it right!!")




#2 Group Anagrams using Python
# from collections import defaultdict

# def group_anagrams(a):
#     dfdict = defaultdict(list)
#     for i in a:
#         sorted_i = " ".join(sorted(i))
#         dfdict[sorted_i].append(i)
#     return dfdict.values()

# words = ["tea", "eat", "bat", "ate", "arc", "car"]
# print(group_anagrams(words))




# 3 Find Missing Number using Python
# Finding the missing number in an array means finding the numbers
# missing from the array according to the range of values inside the array.
# def findMissingNumbers(n):
#     numbers = set(n)
#     length = len(n)
#     output = []
#     for i in range(1, n[-1]):
#         if i not in numbers:
#             output.append(i)
#     return output
    
# listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16, 19, 25, 48, 60]
# print(findMissingNumbers(listOfNumbers))




# 4 Group Elements of Same Indices
# inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# outputLists = []
# index = 0

# for i in range(len(inputLists[0])):
#     outputLists.append([])
#     for j in range(len(inputLists)):
#         outputLists[index].append(inputLists[j][ index])
#     index = index + 1
# a, b, c = outputLists[0], outputLists[1], outputLists[2]
# print(a, b, c)




# 5 Mean Median and Mode
# Mean
# list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
# mean = sum(list1)/len(list1)
# print(mean)

# Median
# list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
# list1.sort()

# if len(list1) % 2 == 0:
#     m1 = list1[len(list1)//2]
#     m2 = list1[len(list1)//2 - 1]
#     median = (m1 + m2)/2
# else:
#     median = list1[len(list1)//2]
# print(median)

# Mode
# list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
# frequency = {}
# for i in list1:
#     frequency.setdefault(i, 0)
#     frequency[i]+=1

# frequent = max(frequency.values())
# for i, j in frequency.items():
#     if j == frequent:
#         mode = i
# print(mode)




# 6 Execution Time of a Python Program
# from time import time
# start = time()

# Python program to create acronyms
# word = "Artificial Intelligence"
# text = word.split()
# a = " "
# for i in text:
#     a = a+str(i[0]).upper()
# print(a)

# end = time()
# execution_time = end - start
# print("Execution Time : ", execution_time)




# 7 Count Number of Words in a Column
# import pandas as pd
# data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", encoding = 'latin1')
# print(data.head())

# data["Number of Words"] = data["Article"].apply(lambda n: len(n.split()))
# print(data.head())




# 8 Rock Paper Scissors Game
# import random

# player1 = input("Select Rock, Paper, or Scissor :").lower()
# player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
# print("Player 2 selected: ", player2)

# if player1 == "rock" and player2 == "paper":
#     print("Player 2 Won")
# elif player1 == "paper" and player2 == "scissor":
#     print("Player 2 Won")
# elif player1 == "scissor" and player2 == "rock":
#     print("Player 2 Won")
# elif player1 == player2:
#     print("Tie")
# else:
#     print("Player 1 Won")




# 9 Print Emojis
# import emoji

# print(emoji.emojize("I love reading books:books:"))
# print(emoji.emojize("Some people have a very sensitive heart:red_heart:, please be kind with them.:hibiscus:"))



# 10 Correct Spellings using Python
# from spellchecker import SpellChecker
# corrector = SpellChecker()

# word = input("Enter a Word : ")
# if word in corrector:
#     print("Correct")
# else:
#     correct_word = corrector.correction(word)
#     print("Correct Spelling is ", correct_word)




# 11 Scraping GitHub Profile using Python
# import requests
# from bs4 import BeautifulSoup as bs

# github_profile = "https://github.com/rayct"
# req = requests.get(github_profile)
# scraper = bs(req.content, "html.parser")
# profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
# print(profile_picture)