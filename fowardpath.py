import sys

from termcolor import colored

from game import print1by1


def forward():
    player_answer = input()
    from game import inventory
    if player_answer == 'take':
        inventory['crystal'] += 1
        print1by1(colored("What is it!", 'red'))
        print1by1(colored("You'll know when the time is right, NOW GO!", 'white'))
        print1by1(colored("Beware not all parts are friendly, hahahahaha", 'white'))
    else:
        if player_answer == 'reject':
            inventory['crystal'] = 0
            print1by1(colored("I don't need anything from you!", 'red'))
            print1by1(colored("Fare well, Jake!", 'white'))
            print1by1(colored("Beware not all parts are friendly, hahahahaha", 'white'))

    print1by1(colored("the figure disappears", 'blue'))
    print1by1(colored("I honestly don't know how i got myself into this but i can't afford to die.", 'red'))
    print1by1(colored("You walk straight ahead", 'blue'))
    print1by1(colored("just one way to the left, move left (yes)?", 'blue'))

    player_answer = input()
    if player_answer == 'yes':
        print1by1(colored("You walked for a while then got to a junction", 'blue'))
        print1by1(colored("Move right or forward", 'blue'))

        player_answer = input()
        if player_answer == 'forward':
            print1by1(colored("You fell into a dark hole", 'blue'))
            print(colored("      GAME OVER", 'blue'))
            sys.exit()
        else:
            print1by1(colored("You got to a junction, continue (forward) or go (left)", 'blue'))

            player_answer = input()
            if player_answer == 'left':
                print1by1(colored("You got eaten up by a sand worm", 'blue'))
                print(colored("      GAME OVER", 'blue'))
                sys.exit()
            else:
                print1by1(colored("You walked for a while then got to a junction", 'blue'))
                print1by1(colored("Move right or forward", 'blue'))

                player_answer = input()
                if player_answer == 'right':
                    print1by1(colored("You got eaten up by wolfs", 'blue'))
                    print(colored("      GAME OVER", 'blue'))
                    sys.exit()
                else:
                    print1by1(colored("You get to the entrance of a dark cave", 'blue'))
                    if inventory['crystal'] == 0:
                        print1by1(colored("You walk into the cave and got killed by the dark creatures "
                                          "because you have no light crystal", 'blue'))
                        print1by1(colored("      GAME OVER", 'blue'))
                        sys.exit()
                    else:
                        if inventory['crystal'] == 1:
                            print1by1(colored("You walked into the cave and the crystal began to emit light", 'blue'))
                            print1by1(colored("wow, Am glad i took this from him", 'red'))
                            from cavepath import cave
                            cave()

    else:
        print1by1(colored("You can only move left", 'blue'))
        forward()


if __name__ == '__main__':
    forward()
