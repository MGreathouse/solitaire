import cards


# deals card to each stack in the tableau
def dealStock(stock, tableau, foundation):
    print('\nStock Deals')
    # add 1 card to each stack in the tableau since the 
    for stack in tableau:
        # check to make sure there are cards in the stock
        if not stock.empty():
            stack.add_card_top(stock.deal())
            stack.top().show_card()  # makes the newly dealt card visible

    # show results of deal
    displayStatus(stock, tableau, foundation)

    return(stock, tableau)


# shows status
def displayStatus(stock, tableau, foundation):
    # display number of cards in the stock
    print('\nStock contains {0} cards.'.format(str(stock.cards_left())))

    # display top cards in foundation
    dispTxt = '\nFoundation top cards:\n\t'
    for stack in foundation:
        if not stack.empty():
            dispTxt += str(stack.top()) + ', '
        else:
            dispTxt += 'Empty, '
    print(dispTxt[0:-2])  # the slicing knocks off the last comma and space

    # display the cards in each stack in the tableau
    dispTxt = '\nTableau Cards:'

    which = 1
    for stack in tableau:
        dispTxt += '\n{0}:)\t'.format(str(which))
        for i in range(stack.cards_left()):
            if stack.top().get_hidden():
                dispTxt += ' XX, '
            else:
                dispTxt += str(stack.top()) + ', '
            stack.add_card_bottom(stack.deal())  # deal to bottom so when done the top card is top again
        dispTxt = dispTxt[0:-2]  # the slicing knocks off the last comma and space
        # update the list slot for next item
        which += 1

    print(dispTxt)


# If able, move top card of stack to the foundation
def moveFoundation(cardMoved, foundation):
    # top values in foundation
    foundationVals = []

    # fill foundation values
    for stack in foundation:
        if stack.empty():
            foundationVals.append('Empty')
        else:
            foundationVals.append(stack.top())
    print('\nFoundation Values:\n',foundationVals,'\n')

    # check if card is an ace
    if cardMoved.get_rank() == 1:
        # add to first empty slot in foundation
        for i in range(4):
            if foundationVals[i] == 'Empty':
                foundation[i].add_card_top(cardMoved)
                return(True, foundation)
    else:
        for i in range(4):
            # rally long just to see if the suit is the same and is the next in sequence
            if foundationVals[i] != 'Empty':
                if cardMoved.get_rank() == foundation[i].top().get_rank() + 1 and cardMoved.has_same_suit(foundation[i].top()):
                    foundation[i].add_card_top(cardMoved)
                    return(True, foundation)
                else:
                    if i == 3:
                        print('{0} cannot be moved to the foundation.'.format(str(cardMoved)))
                        return(False, foundation)
            elif i == 3:
                print('{0} cannot be moved to the foundation.'.format(str(cardMoved)))
                return(False, foundation)



# finds how many cards can be moved, gets amount from user and then tries to move to designated spot


# UI dialog instance
def runUI(stock, tableau, foundation):
    # give directions
    print('\nCommands:\nDeal:\t\t \'-d\'')
    print('Tableau:\t \'-t\'')
    print('Quit:\t\t \'-q\'\n')
    
    # get user input
    usrCmnd = input('Enter Command: ')

    # check input
    if usrCmnd == '-d':
        dealStock(stock, tableau, foundation)
    elif usrCmnd == '-t':
        # give directions
        print('\nMove to Foundation:\t\t \'-f\'')
        print('Move Within Tableau:\t\t \'-t\'')
        print('Quit:\t\t \'-q\'\n')

        # get user input
        usrCmnd = input('Enter Command: ')

        # check input
        if usrCmnd == '-f':
            displayStatus(stock, tableau, foundation)
            try:
                fromStack = int(input('\nFrom stack: '))
            except:
                print('Invalid Number.')

            # try to move it
            moved, foundation = moveFoundation(tableau[fromStack - 1].top(), foundation)

            if moved:
                print('{} moved to foundation.'.format(tableau[fromStack - 1].deal()))
                # auto flip the next card if face down
                if tableau[fromStack - 1].top().get_hidden():
                    tableau[fromStack - 1].top().show_card()

            displayStatus(stock, tableau, foundation)
        elif usrCmnd == '-t':
            displayStatus(stock, tableau, foundation)
            try:
                fromStack = int(input('\nFrom stack: '))
                toStack = int(input('To stack: '))
            except:
                print('Invalid Number.')
        else:
            return(False, stock, tableau, foundation)
    else:
        return(False, stock, tableau, foundation)

    #if this gets triggered, the loop continues
    return(True, stock, tableau, foundation)


# main function
def main():
    print("Let's play solitaire")

    # set up the main deck
    stock = cards.Deck()
    stock.shuffle()

    # set up the foundation stacks (4)
    foundation = [cards.Deck(False) for i in range(4)]

    # set up the tableau stacks (7)
    tableau = [cards.Deck(False) for i in range(7)]
    # add 3 cards to each stack in the tableau
    for stack in tableau:
        stack.add_card_top(stock.deal())
        stack.add_card_top(stock.deal())
        stack.add_card_top(stock.deal())
        stack.top().show_card()  # makes the last card dealt visible

    #show start
    displayStatus(stock, tableau, foundation)

    # loop to get and enact user input
    running = True
    while running:
        running, stock, tableau, foundation = runUI(stock, tableau, foundation)


if __name__ == '__main__':
    main()
else:
    print('This file is not instantiated as a class.')
