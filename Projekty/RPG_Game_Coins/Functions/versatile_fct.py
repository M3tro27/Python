# External import
from colorama import Fore, Style


def Menu(low, high, plus):
    '''
    Lets user enter his choice of movement in main menu. Controls that
    it is a number and that it is a defined option.

    Args:
        low(int):   The lowest number that the user can choose.
        high(int):  The highest number that the user can choose.
        plus(int):  Additional number that the user can choose.

    Returns:
        choice(int): Number that the player chose.
    '''

    # Local variable
    choice = 0      # variable storing the users choice

    while((choice < low) or (choice > high) and (choice != plus)):      # to enter choice again in case of a not valid previous choice
        
        try:
            choice = int(input(Fore.MAGENTA+"  I choose: "))
            print(Style.RESET_ALL)

            # Error when choice is not defined
            if((choice < low) or (choice > high) and (choice != plus)):     # not valid choice
                CantDoThat()
                choice = 0
            # Choice is defined
            else:       # valid choice
             return choice

        except:     # number is not entered
            print(Fore.RED+ "\n USE ONLY NUMBERS")
            print(Style.RESET_ALL)


def ActCompare(acts):
    '''
    This function lets user enter his desired command and compares it with list of
    commands that he is supposed to enter according to the storymaker.
    The loop of entering repeats itself until the user enters the right command.
    If the "help" is in acts, story continues, opposite to the case, where it is not
    int the acts.

    Args:
        actDef(str): action defined by storymaker, to be compared with user imput

    Returns:

    '''
    
    back = False

    while(back == False):
        actPl = input(Fore.MAGENTA+"\n I choose action: ")
        print(Style.RESET_ALL)
        
        actPl = actPl.lower()           # corrects command if it's not only in low case
        actPl = ArticleCheck(actPl)     # corrects command if there is an article

        if(actPl == "help"):
            PrintHelp()
            
            if("help" in acts):
                back = True
        
        else:
            if(actPl in acts):
                back = True
            else:
                CantDoThat()    # Error message


def PressEnter():
    # Lets user press enter to continue. Exists to stop loading loads of text all at once
    
    input(Fore.MAGENTA+ " Press enter to continue")
    print(Style.RESET_ALL)


def PrintHelp():
    # Prints all possible commands or parts of them
    
    print(Fore.YELLOW+ "------------------------------------------------------------------------\n HELP\n")
    print(Style.RESET_ALL+ "  Crucial commands:  help, save, exit, inventory, map")
    print("  Moving  commands:  go + /straight/back/left/right/down/up/to [place]")
    print("  Action  commands:  take/use/look at/open/break/pull/catch + [item]")
    print(Fore.YELLOW+ "------------------------------------------------------------------------", Style.RESET_ALL)


def ArticleCheck(command):
    # Checks for artickles in commands
    # If there is one, the function deletes it

    if(" the " in command):
            command = command.replace("the ", "")
    elif(" a " in command):
            command = command.replace("a ", "")
    elif(" an " in command):
            command = command.replace("an ", "")

    return command


def CantDoThat():
    # Error message

    print(Fore.RED+ "\n YOU CAN NOT DO THAT")
    print(Style.RESET_ALL)