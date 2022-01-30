import sys

from termcolor import colored


from game import print1by1


def cave():
    print1by1(colored("You soon find out that the crystal not only shows you the way "
                      "but also repels the dark creatures", 'blue'))

    print1by1(colored("You will need more crystals", 'blue'))
    print1by1(colored("You walk for a while then see a left and right path", 'blue'))
    print1by1(colored("Move (left or forward)", 'blue'))
    player_reply = input()
    if player_reply == 'left':
        print1by1(colored("You walk aimlessly to a dead end, You crystal light goes off "
                          "You get killed by the dark creatures", 'blue'))
        print(colored("          GAME OVER!", 'blue'))
        sys.exit()
    else:
        print1by1(colored("You walk for a while then see a forward and right path", 'blue'))
        print1by1(colored("Move right or forward", 'blue'))
        player_reply = input()
        if player_reply == 'forward':
            print1by1(colored("You walk aimlessly to a die end, You crystal light goes off "
                              "You get killed by the dark creatures", 'blue'))
            print(colored("          GAME OVER!", 'blue'))
            sys.exit()
        else:
            print1by1(colored("You walk for a while then find a crystal in the middle of a left and right path "
                              "Just before the previous crystal goes off", 'blue'))
            print1by1(colored("I think i'm on the right path", 'red'))
            print1by1(colored("Go left or right", 'blue'))

            player_reply = input()
            if player_reply == 'right':
                print1by1(colored("You walk aimlessly to a dead end, Your crystal light goes off "
                                  "You get killed by the dark creatures", 'blue'))
                print(colored("          GAME OVER!", 'blue'))
                sys.exit()
            else:
                print1by1(colored("Just one way to the right, moves right? (yes)", 'blue'))

                player_reply = input()
                if player_reply == 'yes':
                    print1by1(colored("Just one way to the left, moves left? (yes)", 'blue'))

                    player_reply = input()
                    if player_reply == 'yes':
                        print1by1(colored("You walk for a while then see a forward and left path", 'blue'))
                        print1by1(colored("Move forward or left", 'blue'))

                        player_reply = input()
                        if player_reply == 'forward':
                            print1by1(colored("You walk aimlessly to a dead end, Your crystal light goes off "
                                              "You get killed by the dark creatures", 'blue'))
                            print(colored("          GAME OVER!", 'blue'))
                            sys.exit()
                        else:
                            print1by1(colored("Just one way to the left, moves left? (yes)", 'blue'))

                            player_reply = input()
                            if player_reply == 'yes':
                                print1by1(colored("You walk for a while then find a crystal in the middle of a left and"
                                                  " forward path Just before the previous crystal goes off", 'blue'))
                                print1by1(colored("Go left or forward", 'blue'))

                                player_reply = input()
                                if player_reply == 'left':
                                    print1by1(colored("You walk aimlessly to a dead end, Your crystal light goes off "
                                                      "You get killed by the dark creatures", 'blue'))
                                    print(colored("          GAME OVER!", 'blue'))
                                    sys.exit()

                                else:
                                    print1by1(colored("Just one way to the right, moves right? (yes)", 'blue'))

                                    player_reply = input()
                                    if player_reply == 'yes':
                                        print1by1(colored("You finally get to the end but there are 3 paths "
                                                          "Take path one(1), two(2) or three(3)", 'blue'))

                                        player_reply = int(input())
                                        if player_reply == 1:
                                            print1by1(
                                                colored("You walk aimlessly to a dead end, Your crystal light goes off "
                                                        "You get killed by the dark creatures", 'blue'))
                                            print(colored("          GAME OVER!", 'blue'))
                                            sys.exit()
                                        elif player_reply == 2:
                                            print1by1(
                                                colored("You walk aimlessly to a dead end, Your crystal light goes off "
                                                        "You get killed by the dark creatures", 'blue'))
                                            print(colored("          GAME OVER!", 'blue'))
                                            sys.exit()
                                        else:
                                            print1by1(
                                                colored("YOU BEAT THE GAME! "
                                                        "YOU WIN!", 'yellow'))
                                            sys.exit()


if __name__ == '__main__':
    cave()

