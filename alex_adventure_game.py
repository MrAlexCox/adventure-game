import time
import random
import math
from random import randint


def print_pause(text):
    print(text)
    time.sleep(1)


def intro():
    print_pause("I've been in Germany for two days.")
    print_pause("I arrived with nothing. Just my clothes,"
                " a blanket and my lucky hat.")
    print_pause("I'm in Berlin and I need to get to Hannover.")
    print_pause("I heard there's shelter there...")
    print_pause("Now I need to get a donkey..")


def money_count(money):
    x = sum(money)
    yz = f"You now have: {x} euros"
    print_pause(yz)


def back_beg(money, items, alley_list, blackjack_total):
    print_pause("I lay out my lucky hat.")
    print_pause("I've been here two days. People have been kind...")
    money.append(20)
    money_count(money)
    choose_way(money, items, alley_list, blackjack_total)


def choose_way(money, items, alley_list, blackjack_total):
    print_pause("There are three ways I can go... should I:")
    way = input("1- Go down the dark alley\n2- "
                "Go to the open bar\n3- Maybe the casino...\n")
    if way == '1':
        dark_alley(money, items, alley_list, blackjack_total)
    elif way == '2':
        open_bar(money, items, alley_list, blackjack_total)
    elif way == '3':
        casino(money, items, alley_list, blackjack_total)
    else:
        print_pause("Sorry but choose 1,2, or 3...")
        choose_way(money, items, alley_list, blackjack_total)


def donkey_station(money, items, alley_list, blackjack_total):
    print_pause("I get to the donkey station")
    q = sum(money)
    if q < 59:
        print_pause("Sorry sir, you do not have money to ride the donkey")
        choose_way(money, items, alley_list, blackjack_total)
    else:
        print_pause("I see the board.. 60€ for the donkey ride. I pay.")
        print_pause("I wave goodbye. I get to Hannover, Life's good")
        print_pause("Ich liebe Deutschland!!!")


def fight_flight(money, items, alley_list, blackjack_total):
    fight = input("Should I:\n1- Fight\n2-Run Away\n")
    if fight == '1':
        if 'glass' in items:
            print_pause("I take a look deep into his eyes")
            print_pause("He's so ugly!")
            print_pause("I remember the glass and smash it over his head")
            print_pause("I keep walking and find the donkey station")
            donkey_station(money, items, alley_list, blackjack_total)
        else:
            print_pause("He was too strong for me...")
            print_pause("He took all my money....")
            print_pause("I'm going to have to go back to the station...")
            print_pause("And hope people are kind... ")
            money.clear()
            money_count(money)
            back_beg(money, items, alley_list, blackjack_total)
    elif fight == '2':
        print_pause("Well... might as well go back to the beginning")
        choose_way(money, items, alley_list, blackjack_total)
    else:
        print_pause("Choose... fight or flight...")
        fight_flight(money, items, alley_list, blackjack_total)


def dark_alley(money, items, alley_list, blackjack_total):
    print_pause("I'm walking down the alley, the sound of my steps"
                "echoing against the cold brick walls...")
    alley_man = random.choice(alley_list)
    if alley_man == 'little dwarf':
        print_pause("A little man walks out. He threatens me... ")
        print_pause("... but he's tiny. I smash his head against a"
                    "rock and move on and find the donkey station")
        donkey_station(money, items, alley_list, blackjack_total)

    elif alley_man == 'giant man':
        print_pause("Shit! It's a giant!")
        print_pause("Then suddenly, a giant of a man jumps out")
        print_pause("Give me all your money he says..."
                    " or I'll smash your head in")
        fight_flight(money, items, alley_list, blackjack_total)


def open_bar(money, items, alley_list, blackjack_total):
    print_pause("I get in the bar")
    print_pause("The smell of stale beer overwhelms my senses")
    bar_choice = input("I look around... what should I do:\n1-Have a drink\n"
                       "2-Speak to the sexy lady\n3-Leave\n")
    if bar_choice == '1':
        print_pause("Barman gets me a whiskey zinger. It's strong."
                    " It burns down the back of my throat "
                    "and explodes around my heart.")
        print_pause("Smashed, I realise I still have the cup.")
        print_pause("Whatever, might as well keep it you never know...")
        items.append("glass")
        money.append(-5)
        money_count(money)
        choose_way(money, items, alley_list, blackjack_total)
    elif bar_choice == '2':
        print_pause("I pull up to the girl at the bar")
        print_pause("Hey babe, whats your name?")
        print_pause("She looks at me... looks at the big dude sat at the bar")
        print_pause("He takes one look at me...")
        print_pause("Not today mate... not in here")
        print_pause("He takes me outside and beats me")
        print_pause("I'm beaten... but not broken. I head back to the station")
        choose_way(money, items, alley_list, blackjack_total)
    elif bar_choice == '3':
        print_pause("Good choice... What am I doing here...")
        print_pause("I need to get to Hannover!")
        choose_way(money, items, alley_list, blackjack_total)
    else:
        print_pause("Nah sorry... this is reality,"
                    " choice is limited. Choose 1, 2 or 3")
        open_bar(money, items, alley_list, blackjack_total)


def play_again(money, items, alley_list, blackjack_total):
    print_pause('Do you want to play again:')
    p_a = input('1- Yes 2- No\n')
    yyy = sum(money)
    if yyy < 10:
        print_pause("Sorry you bum no money no juego.")
        print_pause("Oh well... I guess I better go back to"
                    "the station and put my hat back out... ")
        back_beg(money, items, alley_list, blackjack_total)
    elif p_a == '1':
        print_pause('Lets go!')
        play_blackjack(money, items, alley_list, blackjack_total)
    elif p_a == '2':
        dd = sum(money)
        print_pause('Suppose thats wise...')
        choose_way(money, items, alley_list, blackjack_total)
    else:
        print_pause("Sorry, wrong option...")
        play_again(money, items, alley_list, blackjack_total)


def barmans_go(money, items, alley_list, blackjack_total):
    print_pause("It's the barmans go...")
    your_cards = sum(blackjack_total)
    for d in range(1):
        barmans_cards = randint(14, 30)
        print_pause("He gets:")
        print_pause(barmans_cards)
        if barmans_cards > 21:
            print_pause("You win!")
            blackjack_total.clear()
            money.append(30)
            money_count(money)
            play_again(money, items, alley_list, blackjack_total)
        elif barmans_cards == your_cards:
            print_pause('You have:')
            print_pause(your_cards)
            print_pause("You draw")
            blackjack_total.clear()
            money_count(money)
            play_again(money, items, alley_list, blackjack_total)
        elif barmans_cards > your_cards:
            print_pause('You have:')
            print_pause(your_cards)
            print_pause("You lose")
            blackjack_total.clear()
            money.append(-10)
            money_count(money)
            play_again(money, items, alley_list, blackjack_total)
        elif barmans_cards < your_cards:
            print_pause('You have:')
            print_pause(your_cards)
            print_pause("You win!")
            blackjack_total.clear()
            money.append(30)
            money_count(money)
            play_again(money, items, alley_list, blackjack_total)


def pick_second(money, items, alley_list, blackjack_total, first_card):
    hold = input('1- Pick another card\n2- Hold\n')
    if hold == '1':
        for d in range(1):
            second_card = randint(1, 10)
            print_pause(second_card)
            blackjack_total.append(second_card)
            total = first_card + second_card
            print_pause("You have:")
            print_pause(total)
            if total > 21:
                print_pause("You lose")
                money.append(-10)
                blackjack_total.clear()
                money_count(money)
                play_again(money, items, alley_list, blackjack_total)
            elif total <= 21:
                barmans_go(money, items, alley_list, blackjack_total)
    elif hold == '2':
        barmans_go(money, items, alley_list, blackjack_total)
    else:
        print_pause("Sorry, that's not an option")
        pick_second(money, items, alley_list, blackjack_total, first_card)


def play_blackjack(money, items, alley_list, blackjack_total):
    vvv = sum(money)
    if vvv < 10:
        print_pause("Sorry bum boy no $ no play...")
    else:
        print_pause("Its 10$ a hand...")
        print_pause("I'm in...")
        print_pause("The cards come out")
        for n in range(1):
            first_card = randint(14, 21)
            print(first_card)
            blackjack_total.append(first_card)
            print_pause("Do you want to:")
            pick_second(money, items, alley_list, blackjack_total, first_card)


def casino(money, items, alley_list, blackjack_total):
    print_pause("Hmmmm casino...")
    choice = input("Should I:\n1-Play Blackjack\n2-Leave\n")
    if choice == '1':
        play_blackjack(money, items, alley_list, blackjack_total)
    elif choice == '2':
        print_pause("I guess you're right...")
        print_pause("Leave it for another day")
        choose_way(money, items, alley_list, blackjack_total)
    else:
        print_pause("????!!! 1 or 2!!")
        casino(money, items, alley_list, blackjack_total)


def play_game():
    items = []
    money = [0]
    alley_list = ['little dwarf', 'giant man']
    blackjack_total = []
    intro()
    back_beg(money, items, alley_list, blackjack_total)


play_game()
