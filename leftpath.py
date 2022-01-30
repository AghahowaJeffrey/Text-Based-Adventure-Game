import sys

from termcolor import colored

from game import print1by1


def left():
    print1by1(colored("just one way to the right, move right (yes)?", 'blue'))

    player_reply = input()
    if player_reply == 'yes':
        print1by1(colored("You walked for a while then got to a junction btw right and left", 'blue'))
        print1by1(colored("Take right or left", 'blue'))
        player_reply = input()
        if player_reply == 'right':
            print1by1(colored("You got beaten by a snake", 'blue'))
            print1by1(colored("Get's dark, You die\n      GAME OVER!", 'blue'))
            sys.exit()
        else:
            print1by1(colored("You walk for a while then find a strange crystal", 'blue'))
            print1by1(colored("Pick or leave?", 'blue'))

            player_reply = input()
            from game import inventory
            if player_reply == 'pick':
                inventory['crystal'] += 1
            else:
                inventory['crystal'] = 0

        print1by1(colored("You got to a junction btw left and right", 'blue'))
        print1by1(colored("Take left or right?", 'blue'))

        player_reply = input()
        if player_reply == 'left':
            print1by1(colored("You walked back to were you started\n   GAME OVER", 'blue'))
            sys.exit()
        else:
            print1by1(colored("You walk for a while then see a left path", 'blue'))
            print1by1(colored("Take left or continue moving forward (left or forward)", 'blue'))

            player_reply = input()
            if player_reply == 'left':
                print1by1(colored("You walk aimlessly to a die end", 'blue'))
                print(colored("          GAME OVER!", 'blue'))
                sys.exit()
            else:
                print1by1(colored("You get to the entrance of a dark cave", 'blue'))
                if inventory['crystal'] == 0:
                    print1by1(colored("You walk into the cave but got killed by the dark creatures "
                                      "because you have no light crystal", 'blue'))
                    print1by1(colored("      GAME OVER", 'blue'))
                    sys.exit()
                else:
                    print1by1(colored("You walked into the cave and the crystal began to emit light", 'blue'))
                    print1by1(colored("wow, Am glad i found this", 'red'))
                    from cavepath import cave
                    cave()
    else:
        print1by1(colored("You can only move left", 'blue'))
        left()


if __name__ == '__main__':
    left()
