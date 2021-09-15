import random
import time

#def reset_game():
#    attempts = 0
#    correct = 0
#
#    word_list = ['sun', 'moon', 'planet']
#    rand_num = random.randint(0,2)
#
#    chosen_word = word_list[rand_num]
#    letters_of_word_list = list(chosen_word)
    
attempts = 0
correct = 0

word_list = ['sun', 'moon', 'planet']
rand_num = random.randint(0,2)

chosen_word = word_list[rand_num]
letters_of_word_list = list(chosen_word)

displayed_word = ' '
for i in range(len(letters_of_word_list)):
    displayed_word += "_ "
print(f'Here is your word:{displayed_word}')

word_so_far = ['_'] * len(letters_of_word_list)
def letter_in_word(letter_guessed, word_so_far):
    status = False
    for letter in letters_of_word_list:
        if letter_guessed == letter:
            letter_index = letters_of_word_list.index(letter)
            word_so_far[letter_index] = letter
            print(f'That is correct! Your word is now: {word_so_far}')
            letters_of_word_list[letter_index] = None
            status = True
    return status

def blank_spaces_left(l):
    for letter in l:
        if letter == '_':
            return True
    return False

while True:
    letter_guessed = str(input('What is your next letter? '))
    time.sleep(1)
    if letter_in_word(letter_guessed, word_so_far):
        correct += 1
        if not blank_spaces_left(word_so_far):
            print('You win!')
            again = input('Would you like to play again? Type yes or no: ')
            if str(again) == 'yes':
                pass
            else:
                break
    else:
        attempts += 1
        print(f'That is not correct. You have {5-attempts} attempts left.')
        if attempts == 5:
            print('Sorry. You lose!')
            again = input('Would you like to play again? Type yes or no: ')
            if str(again) == 'yes':
                pass
            else:
                break

