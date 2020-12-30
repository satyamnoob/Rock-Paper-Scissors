import random
def play(initial_score):
    final_score = initial_score
    win = ['paper-rock', 'scissors-paper', 'rock-scissors']
    lose = ['rock-paper', 'paper-scissors', 'scissors-rock']        
    options = ['rock', 'paper', 'scissors']
    while True:
        user_input = input()
        if user_input == '!exit':
            print('Bye!')
            break
        elif user_input == '!rating':
            print(final_score)
        elif user_input not in options:
            print('Invalid input')
        else:
            random_option = random.choice(options)
            combination = user_input + '-' + random_option
            if user_input == random_option:
                print("There is a draw ({})".format(random_option))
                final_score += 50
            elif combination in win:
                print("Well done. The computer chose {} and failed".format(random_option))
                final_score += 100
            else:
                print("Sorry, but the computer chose {}".format(random_option))
    return final_score
print('Enter your name: ', end='')
name_of_player = input()
flag = False
score_of_player = 0
print(f'Hello, {name_of_player}')
ratings = open('rating.txt', 'r')
name_database = ratings.readlines()
ratings.close()
index = -1
for name_and_score in name_database:
    index += 1
    name = name_and_score.split(" ")
    if name[0] == name_of_player:
        flag = True
        score_of_player = int(name[1])
        break
ratings = open('rating.txt', 'w')
if flag:
    final_score = play(score_of_player)
    name_database[index] = name_of_player + " " + str(final_score) + "\n"
    ratings.writelines(name_database)
else :
    final_score = play(score_of_player)
    name_database.append(name_of_player + " " + str(final_score) + "\n")
    ratings.writelines(name_database)
ratings.close()