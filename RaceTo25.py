__author__ = 'Harsha Payidiparty'

def a():
    '''
    Write a while loop that counts from 0 to 10, inclusive.
    Print out each number.
    :return: None
    '''

    a = 0
    while a <= 10:
        print(a)
        a += 1
    return None

def b1(n):
    '''
    Count from 0 to n inclusive. Print out each number.
    Use a while loop.
    :param n: an integer
    :return: None
    '''

    i = 0
    while i <= n:
        print(i)
        i += 1
    return None

def b2(n):
    '''
    Count from 0 to n inclusive. Print out each number.
    Use a for loop.
    :param n: an integer
    :return: None
    '''

    i = 0
    for x in range(n + 1):
      print(i)
      i = i + 1
    return None

def get_input():

    '''
    Continually prompt the user for a number, 1,2 or 3 until
    the user provides a good input.
    :return: The users chosen number as an integer
    '''

    n = input("Give me one of 1,2 or 3: ")          #ask user to input one of 1,2 or 3
    while n != "3" and n != "2" and n != "1":       #if user does not input one of 1,2 or 3
      print("Invalid input!")                       #send them a message saying invalid input!
      n =input("Give me one of 1,2 or 3: ")         #ask user again to input one of 1,2 or 3

    n = int(n)                                      #convert n to an integer
    return(n)

def c():
    '''
    Ask the user to input a 1,2 or 3.
    If the user enters anything else, then tell the user
    they did something wrong, and prompt them again for a good input.
    Once the user enters the number, counts from 0 to the number and then returns.
    :return: None
    '''
    n = get_input()                 #asks user for input 1,2 or 3. Same as get_input()

    n = int(n)                      #converts n to an integer
    i = 0
    while i <= n:
        print(i)
        i += 1                      #once user enters 1,2 or 3. Counts from 0 to n
    return None

def d():
    '''
    keep track of the total
    of all numbers (1,2,3) input so far. Exit when the total
    is 25 or more.
    :return: None
    '''
    print("Total is: 0")
    n = get_input()
    total = 0                                   #total counter starts at 0
    while total < 25:
        total = total + n
        print("Total is: " + str(total))        #print total amount after new added n value
        if total <25:
            n = get_input()
    return None

def e():
    '''
    Same as in d(), but this time, we make sure that the user can't enter
    a number that would put the total over 25.
    :return: None
    '''
    print("Total is: 0")
    total = 0
    while total < 25:
        n = get_input()
        if n + total > 25:                              #if input excess total count of 25 user must input a diff num
            print("The number you chose would put the total over 25. Try Again.")
            print("Total is: " + str(total))
        else:
            total = total + n
            print("Total is: " + str(total))
    return None

def get_input_from_player(player):
    '''
    This is the same as get_input, except this time, the prompt includes which player
    is supposed to supply the input.
    :param player: The player, either 1 or 2
    :return: An integer, either 1,2 or 3
    '''
    n = (input("Player " + str(player) + " give me one of 1,2 or 3: "))
    while n != "3" and n != "2" and n != "1":
      print("Invalid input!")
      n =(input("Player " + str(player) + " give me one of 1,2 or 3: "))

    n = int(n)
    return(n)

def f():
    '''
    Same as in e(), but ths time, print out which players move it is,
    on each turn. There are 2 players, Player 1 starts and they alternate.
    Hint: add a player variable, as well as use get_input_from_player(player)
    :return: None
    '''
    print("Total is: 0")
    x = 2                  # x= 2 represents player 2
    total = 0
    while total < 25:
        if x == 1:         # if x is currently player 1
            x = 2          # then change to player 2
        else:
            x = 1           #if not then change to player 1, since player 2 is currently selected
        n = get_input_from_player(x)        #get input from the selected player
        if n + total > 25:
            print("The number you chose would put the total over 25. Try Again.")
            print("Total is: " + str(total))
            if x == 1:      #since this player entered a wrong input, reprompt same player to enter a input agian
                x = 2
            else:
                x = 1
        else:
            total = total + n
            print("Total is: " + str(total))
    return None

def raceTo25():
    '''
    Same as in f(), but this time, print out which player won, before returning.
    :return: None
    '''
    print("Total is: 0")
    x = 2
    total = 0
    while total < 25:
        if x == 1:
            x = 2
        else:
            x = 1
        n = get_input_from_player(x)
        if n + total > 25:
            print("The number you chose would put the total over 25. Try Again.")
            print("Total is: " + str(total))
            if x == 1:
                x = 2
            else:
                x = 1
        else:
            total = total + n
            print("Total is: " + str(total))
    if total == 25:
        if x == 1:
            print("player 1 won!")
        else:
            print("Player 2 won!")
    return None

def raceTo(m):

    '''
    same as in raceTo25(), except you call parameter m to change the length of the game.
    :return: None
    '''

    print("Total is: 0")
    x = 2
    total = 0
    while total < m:
        if x == 1:
            x = 2
        else:
            x = 1
        n = get_input_from_player(x)
        if n + total > m:
            print("The number you chose would put the total over 25. Try Again.")
            print("Total is: " + str(total))
            if x == 1:
                x = 2
            else:
                x = 1
        else:
            total = total + n
            print("Total is: " + str(total))
    if total == m:
        if x == 1:
            print("player 1 won!")
        else:
            print("Player 2 won!")
    return None


#a()
#b1(0)
#b1(-5)
#b1(15)
#b2(0)
#b2(-5)
#b2(15)
#get_input()
#c()
#d()
#e()
#get_input_from_player("1")
#get_input_from_player("2")
#f()
#raceTo25()
#raceTo(25)
#raceTo(17)
#raceTo(100)
