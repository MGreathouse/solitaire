import cards


def main():
    print("Let's play solitaire")

    # set up the main deck
    stock = cards.Deck()
    stock.shuffle()

    # set up the foundation decks (4)
    foundation = [cards.Deck(False), cards.Deck(False), cards.Deck(False), cards.Deck(False)]

    # set up the tableau decks (7)
    tableau = [cards.Deck(False), cards.Deck(False), cards.Deck(False),
            cards.Deck(False), cards.Deck(False), cards.Deck(False), cards.Deck(False)]
    # add 3 cards to each stack in the tableau
    for stack in tableau:
        stack.add_card_top(stock.deal())
        stack.add_card_top(stock.deal())
        stack.add_card_top(stock.deal())

    print(stock, '\n')
    for stack in tableau:
        print(str(stack).strip())
    for stack in foundation:
        print(str(stack).strip())


if __name__ == '__main__':
    main()
