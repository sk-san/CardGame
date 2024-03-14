import random


def generateNumberArr(playerHand):
    rankArr = []
    for i in range(len(playerHand)):
        rankArr.append(playerHand[i][1:])

    return rankArr


def createHashmap(cardPower, numberArr):
    hashmap = {}

    for i in range(len(cardPower)):
        hashmap[cardPower[i]] = 0

    for i in range(len(numberArr)):
        hashmap[numberArr[i]] += 1
    return hashmap


def winnerPairOfCards(player1, player2):
    cardPower = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    numbers1 = generateNumberArr(player1)
    numbers2 = generateNumberArr(player2)

    hashmap1 = createHashmap(cardPower, numbers1)
    hashmap2 = createHashmap(cardPower, numbers2)

    winner = "draw"
    pairOfCards = 0

    for i in range(len(cardPower)):
        if hashmap1[cardPower[i]] > hashmap2[cardPower[i]]:
            if pairOfCards < hashmap1[cardPower[i]]:
                pairOfCards = hashmap1[cardPower[i]]
                winner = "player1"
        elif hashmap1[cardPower[i]] < hashmap2[cardPower[i]]:
            if pairOfCards < hashmap2[cardPower[i]]:
                pairOfCards = hashmap2[cardPower[i]]
                winner = "player2"
    return winner


class Card:
    def __init__(self, value, suit, intValue):
        self.value = value
        self.suit = suit
        self.intValue = intValue

    def getCardString(self):
        return self.suit + self.value + "(" + str(self.intValue) + ")"

    def tempCard(self):
        return str(self.suit + self.value)


class Deck:
    def __init__(self, gameMode=None):
        self.deck = self.generateDeck(gameMode)

    @staticmethod
    def generateDeck(self, gameMode=None):
        newDeck = []
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # blackJack
        blackJack = {"A": 1, "J": 10, "Q": 10, "K": 10}
        suits = ["♣︎", "♠︎", "❤︎", "♦︎"]

        for suit in suits:
            for i, value in enumerate(values):
                if gameMode == "21":
                    if value in blackJack.keys():
                        newDeck.append(Card(value, suit, (blackJack[value])))
                    else:
                        newDeck.append(Card(value, suit, int(value)))
                else:
                    newDeck.append(Card(value, suit, i + 1))
        return newDeck

    def draw(self):
        return self.deck.pop()

    def printDeck(self):
        print("Displaying Cards ...")
        for card in self.deck:
            print(card.getCardString())

    def shuffleDeck(self):
        deckSize = len(self.deck)
        for i in range(0, deckSize):
            j = random.randint(i, deckSize - 1)
            temp = self.deck[i]
            self.deck[i] = self.deck[j]
            self.deck[j] = temp


class Dealer:

    @staticmethod
    def startGame(AmountOfPlayers, gameMode):

        table = {
            "players": [],
            "gameMode": gameMode,
            "deck": Deck()
        }

        table["deck"].shuffleDeck()

        for person in range(AmountOfPlayers):
            playerCard = []
            for i in range(0, Dealer.initialCards(gameMode)):
                playerCard.append(table["deck"].draw())
            table["players"].append(playerCard)

        return table

    @staticmethod
    def initialCards(gameMode):
        if gameMode == "21":
            return 2
        elif gameMode == "poker":
            return 5

    @staticmethod
    def score21Individual(cards):
        value = 0
        for card in cards:
            value += card.intValue
        return value if 21 >= value >= 1 else 0

    @staticmethod
    def winnerOf21(table):
        points = []
        cache = {}
        for cards in table["players"]:
            point = Dealer.score21Individual(cards)
            points.append(point)
            if point in cache:
                cache[point] += 1
            else:
                cache[point] = 1
        print(points)

        maxIndex = HelperFunctions.maxInArrIndex(points)
        if cache[points[maxIndex]] > 1:
            return "It is a draw"
        elif cache[points[maxIndex]] >= 0:
            return "player " + str(maxIndex + 1) + " is the winner"
        else:
            return "No winners..."

    @staticmethod
    def printTableInformation(table):
        print(
            "Amount of players:" + str(len(table["players"])) + "...GameMode:" + table["gameMode"] + ". At this table")
        for i, player in enumerate(table["players"]):
            print(str(i + 1) + "player's cards:")
            for card in player:
                print(card.getCardString())

    @staticmethod
    def print_players_win_rate(win_rate_array):
        pass

    @staticmethod
    def checkWinner(table):
        p1 = []
        p2 = []
        change_flag = False
        for person in table["players"]:
            for card in person:
                if not change_flag:
                    p1.append(card.tempCard()[1:])
                if change_flag:
                    p2.append(card.tempCard()[1:])
            change_flag = True
        return "The winner is " + winnerPairOfCards(p1, p2)


class HelperFunctions:

    @staticmethod
    def maxInArrIndex(intArr):
        maxvalue = intArr[0]
        maxIndex = 0
        for i, value in enumerate(intArr):
            if value > maxvalue:
                maxIndex = i
                maxvalue = value

        return maxIndex


if __name__ == "__main__":
    # table = Dealer.startGame(4, "21")
    # Dealer.printTableInformation(table)
    # print(Dealer.checkWinner(table))
    print()

