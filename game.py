# A Text-Based Adventure Game.

import sys

from termcolor import colored


inventory = {'crystal': 0}


def print1by1(text, delay=0.05):
    import time
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def main():
    print()
    print(colored("""                                  ########################
                                  #                      #
                                  #      MAZE RUNNER     #
                                  # Text-Based Adventure #
                                  #         Game         #
                                  #                      #
                                  ########################""", 'green'))
    print("             --------------------------------------------------------")
    print()

    while True:
        print1by1(colored("Aghhhh!... My head!", 'red'))
        print1by1(colored("What's going on?, where am i? and Why does my head hurt so much", 'red'))
        print1by1(colored("looks around and see nobody but only long, gigantic walls", 'blue'))
        print1by1(colored("Turns around but no where to go, only a long pathway in front of you "
                          "and a path by your left", 'blue'))
        print1by1(colored("Sees a shadow-like figure in the distance approaching you", 'blue'))
        print1by1(colored("Who's over there?, what's going on!, Where am i?", 'red'))
        print1by1(colored("The figure continues to walk towards you, getting closer and closer!", 'blue'))
        print1by1(colored("Run away using the left path or wait to see the outcome or "
                          "quit the game (run, wait, quit)", 'blue'))

        player_answer = input()
        from leftpath import left
        if player_answer == 'run':
            print1by1(colored("Who was that?, Why can't i remember anything?", 'red'))
            print1by1(colored("I don't know how i got here, but i think this is some sort of maze", 'red'))
            print1by1(colored("You run for a while", 'red'))
            left()

        elif player_answer == 'wait':
            print1by1(colored("The figure gets to you but you cant make out who or what it is", 'blue'))
            print1by1(colored("Jake!, that is your name", 'white'))
            print1by1(colored("My name is jake!, Who are you, why can't i remember anything "
                              "and where am i?", 'red'))
            print1by1(colored("You have been choosing by a greater cause to participate in this Game", 'white'))
            print1by1(colored("You are in a maze! and only one part can get you out alive", 'white'))
            print1by1(colored("Beat the game and you will get back your memory "
                              "and also be rewarded beyond your imagination", 'white'))

            print1by1(colored("Here have this, ", 'white'))
            print1by1(colored("The shadow-like figure stretches his hands towards you to reveal a crystal", 'blue'))
            print1by1(colored("take or reject", 'blue'))
            from fowardpath import forward
            forward()
        else:
            print1by1(colored("Bye!", 'blue'))
            sys.exit()


if __name__ == '__main__':
    main()
