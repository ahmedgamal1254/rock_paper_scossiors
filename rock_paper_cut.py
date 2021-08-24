# rock and paper and cut
import random
print('game stone paper scissors to play it you should follow instractions: :-')
print('You must choose 1 or 2 or 3')
print('Start..........................')

# set dictionary by contain some information
data={'stone':5,'paper':5,'scissors':5}
full_game=15
arr=['stone','paper','scissors']
while True:
    val=input('Enter value :- ')
    rand=random.choice(arr)
    print(val,'vs',rand)
    full_game-=1
    if val!=rand:
        if data['stone'] > 0:
            if val=='stone' and rand=='paper':
                print('Your Computer win')
                print('paper is win')
                data['stone']-=1
            elif val=='stone' and rand=='scissors':
                print('Your win')
                print('stone is win')
                data['stone'] -= 1
        else:
            print('stones is complete please choose paper or scissors')
        if data['paper'] > 0:
            if val=='paper' and rand=='stone':
                print('Your win')
                print('paper is win')
                data['paper'] -= 1
            elif val=='paper' and rand=='scissors':
                print('Your computer win')
                print('scissors is win')
                data['paper'] -= 1
        else:
            print('paprs is complete please choose paper or scissors')
        if data['scissors'] > 0:
            if val == 'scissors' and rand == 'paper':
                print('Your win')
                print('scissors is win')
                data['scissors'] -= 1
            elif val == 'scissors' and rand == 'stone':
                print('Your computer win')
                print('stone is win')
                data['scissors'] -= 1
        else:
            print('scissors is complete please choose paper or scissors')
        if full_game == 0: break
    else:
        print('not match')
print('Game Finished')