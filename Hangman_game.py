#         UR-CST / NYARUGENGE CAMPUS / Computer Science Year 1 / 2023 - 2024

#Contributors:
# 1.    Gedeon IRANKUNDA / reg_number: 223017888
# 2.    Philemon TUYISHIMIRE / reg_number: 220009467
# 3.    Latifa UWABERA / reg_number : 223018677

# Project:      HANGMAN GAME

import random

def game(my_list):

    secret_word = random.choice(my_list)

    hint = len(secret_word) * "-"

    user_word = ""
    found_characters = ""

    accepeted_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                            'o','p','q','r','s','t','u','v','w','x','y','z']

    vowels = ('a','e','i','o','u')
    consonants = ('b','c','d','f','g','h','j','k','l','m','n','p',
                    'q','r','s','t','v','w','x','y','z')
    guesses = 6
    warnings = 3
    index = 0
    rem_letters = secret_word  #rem letters being remaining letters to be found.

    print("Secret word:",hint, "(", len(secret_word), "characters )",end=' | ')
    print("Warning:",warnings, end=' | ')
    print("guesses:", guesses)


    while user_word != secret_word:
        
        user_guess = input("Enter your guess: ")
        user_guess = user_guess.lower()    # to avoid errors as python is a case sentive language

        if user_guess not in accepeted_characters: #check for symbol input

            print("Invalid Input")
            
            if warnings > 0:
                warnings -= 1
                print("Secret word:",user_word + "-" * len(rem_letters),end=' | ')
                print("Warning:",warnings, end=' | ')
                print("guesses:", guesses)
                

            elif guesses > 1:
                guesses -= 1
                print("Secret word:",user_word + "-" * len(rem_letters),end=' | ')
                print("Warning:",warnings, end=' | ')
                print("guesses:", guesses)
                
            
            else:
                print("Secret word:",user_word + "-" * len(rem_letters),end=' | ')
                print("Warning:",warnings, end=' | ')
                print("guesses:", 0)
                print("You LOSS !!!")
                return
        
        elif user_guess in found_characters and user_guess not in rem_letters: #checking rentering of a character
            print("You've already found that one")

            if warnings > 0:
                warnings -= 1
                print("Secret word:",user_word + "-" * len(rem_letters),end=' | ')
                print("Warning:",warnings, end=' | ')
                print("guesses:", guesses)
                

            elif guesses > 1:
                guesses -= 1
                print("Secret word:",user_word + "-" * len(rem_letters),end=' | ')
                print("Warning:",warnings, end=' | ')
                print("guesses:", guesses)
                
            
            else:
                print("Secret word:",user_word + "-" * len(rem_letters),end=' | ')
                print("Warning:",warnings, end=' | ')
                print("guesses:", 0)
                print("You LOSS !!!")
                return
                

        elif user_guess in rem_letters and user_guess == secret_word[index]:  #desired output

            found_characters = found_characters + user_guess
            hint = hint.replace("-","",1)   # hint.replace deletes 1 (-) in hint at time.
            user_word = user_word + user_guess + hint
            print("Secret word:",user_word,end=' | ')
            print("Warning:",warnings, end=' | ')
            print("guesses:", guesses)
            rem_letters = rem_letters.replace(user_guess,"",1)
            index += 1
            user_word = user_word.replace("-","") #removing (-) on the user word

        elif user_guess in rem_letters and user_guess != secret_word[index]:    # character in secret word

            print("Secret word:",user_word + "-" * len(rem_letters),end=' | ')
            print("Warning:",warnings, end=' | ')
            print("guesses:", guesses)
            

        elif user_guess not in rem_letters and user_guess in consonants:    #consonant not in secret word

            if guesses > 1:
                guesses -= 1
                print("Secret word:",user_word + "-" * len(rem_letters),end=' | ')
                print("Warning:",warnings, end=' | ')
                print("guesses:", guesses)
                
            else:
                print("Secret word:",user_word + "-" * len(rem_letters),end=' | ')
                print("Warning:",warnings, end=' | ')
                print("guesses:", 0)
                print("You LOSS !!")
                return
                
        elif user_guess not in rem_letters and user_guess in vowels:    #vowel not in secret word

            if guesses > 2:
                guesses -= 2
                print("Secret word:",user_word + "-" * len(rem_letters),end=' | ')
                print("Warning:",warnings, end=' | ')
                print("guesses:", guesses)
                
            
            else:
                print("Secret word:",user_word + "-" * len(rem_letters),end=' | ')
                print("Warning:",warnings, end=' | ')
                print("guesses:", 0)
                print("Your LOSS !!!")
                return
                
        
        if len(rem_letters) <= 0:           # Scores calculation

            scores = guesses * len(secret_word)
            print("You WIN !!!",end=' | ')
            print("Scores:", scores, '/', len(secret_word)*6)
            return


secret_words = ["world","docker", "python", "solid", "secret"]

game(secret_words)
