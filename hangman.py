import random

print("H A N G M A N")

count_win = 0
count_lost = 0


def play_1():
    global count_win, count_lost
    words = ["python", "java", "swift", "javascript"]
    selected_word = random.choice(words)
    masked_word = list(len(selected_word) * "-")
    attempts = 8
    print(''.join(masked_word))
    guessed_letter = []
    suggested_letter = []
    while attempts > 0:
        input_letter = input("Input a letter: ")
        print()
        if len(input_letter) != 1:
            print("Please, input a single letter")
        elif not input_letter.isalpha() or input_letter.isupper():
            print("Please, enter a lowercase letter from the English alphabet.")
        elif input_letter not in selected_word:
            suggested_letter.append(input_letter)
            print("That letter doesn't appear in the word.")
            attempts -= 1
        elif input_letter in suggested_letter:
            print("You've already guessed this letter.")
            attempts -= 1
    
        else:
            for i, letter in enumerate(selected_word):
                if letter == input_letter:
                    masked_word[i] = input_letter
                    suggested_letter.append(input_letter)
        print(''.join(masked_word))
        if "-" not in masked_word:
            print("You guessed the word", ''.join(masked_word) + "!")
            print("You survived!")
            attempts = 0
            count_win += 1
    if "-" in masked_word:
        print("")
        print("You lost!")
        count_lost += 1
    

def result():
    print("You won:", str(count_win) + " times")
    print("You lost:", str(count_lost) + " times")


while True:
    c_w = 0
    c_l = 0
    a = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")
    print()
    if a == "play":
        play_1()
    elif a == "results":
        result()
    elif a == "exit":
        break
