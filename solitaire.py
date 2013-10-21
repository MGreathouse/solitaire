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
    # displayStatus()  # will call as of yet undefined function to display player visible status
    tempStats(stock, tableau, foundation)  # temporary display of everything

    return(stock, tableau)


#development function to show everything
def tempStats(stock, tableau, foundation):
    print('\nStock:', stock, '\n\nTableau:')
    for stack in tableau:
        print(str(stack).strip())
    print('\nFoundation:')
    for stack in foundation:
        print(str(stack).strip())


# shows status


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
    tempStats(stock, tableau, foundation)
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
