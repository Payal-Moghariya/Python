"""
QUESTION
Alice has some cards with numbers written on them. 
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
Write a function to help Bob locate the card.
"""
"""
Input : A list of cards sorted in decreasing order
Input : A number/query
Output : Find the position of that number/query
"""
def check_location(cards, query, mid):
    if cards[mid] == query:
        if mid - 1 >= 0 and cards[mid - 1] == query :
            return "left"
        else:
            return "found"
    elif cards[mid] > query:
            return "right"
    elif cards[mid] < query:
            return "left"



def locate_card(cards, query):
    first = 0
    last = len(cards) - 1

    while first <= last:
        mid = (first + last) // 2

        result = check_location(cards, query, mid)
        if result == "found":
            return mid
        elif result == "right":
            first = mid + 1
        elif result == "left":
            last = mid - 1
        
    return -1


if __name__ == "__main__":
    pass