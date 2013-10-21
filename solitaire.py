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
    for stack in tableau:
        dispTxt += '\n\t'
        for i in range(stack.cards_left()):
            if stack.top().get_hidden():
                dispTxt += 'XX, '
            else:
                dispTxt += str(stack.top()) + ', '
            stack.add_card_bottom(stack.deal())  # deal to bottom so when done the top card is top again
        dispTxt = dispTxt[0:-2]  # the slicing knocks off the last comma and space
    print(dispTxt)


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
    #force deal
    stock, tableau = dealStock(stock, tableau, foundation)
    #force deal
    stock, tableau = dealStock(stock, tableau, foundation)
    #force deal
    stock, tableau = dealStock(stock, tableau, foundation)
    #force deal
    stock, tableau = dealStock(stock, tableau, foundation)
    #force deal
    stock, tableau = dealStock(stock, tableau, foundation)


if __name__ == '__main__':
    main()
