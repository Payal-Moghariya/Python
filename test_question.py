"""
Case 1 : If the number is in between of the list
Case 2 : If the number is in starting or the end of the list
Case 3 : If the number is not present in the list
Case 4 : If the list has numerous repetitive numbers
Case 5 : If the number is one of the repetitive number of the list
Case 6 : If the number is a negative number
Case 7 : If the list is an empty list
"""

import question1

def test_squence():
    # test for all scenarios

    tests = []

    #Case 0
    test = {
        "input" : {
            "cards" : [13,11,10,9,8,4,3],
            "query" : 10
        },
        "output" : 2
    }
    tests.append(test)

    test = {
        "input" : {
            "cards" : [13,11,10,9,8,4,3,2],
            "query" : 8
        },
        "output" : 4
    }
    tests.append(test)

    #case 1
    test = {
        "input" : {
            "cards" : [13,11,10,9,8,4,3],
            "query" : 3
        },
        "output" : 6
    }
    tests.append(test)

    #case 2
    test = {
        "input" : {
            "cards" : [13,11,10,9,8,4,3],
            "query" : 2
        },
        "output" : -1
    }
    tests.append(test)
    
    #case 3
    test = {
        "input" : {
            "cards" : [13,11,11,11,10,9,9,9,8,4,4,4,3,3],
            "query" : 10
        },
        "output" : 4
    }
    tests.append(test)

    #case 4
    test = {
        "input" : {
            "cards" : [13,11,11,11,10,9,9,9,8,4,4,4,3,3],
            "query" : 11
        },
        "output" : 1
    }
    tests.append(test)

    #case 5
    test = {
        "input" : {
            "cards" : [13,10,7,4,2,-1,-7,-9,-11],
            "query" : -7
        },
        "output" : 6
    }
    tests.append(test)

    #case 6
    test = {
        "input" : {
            "cards" : [],
            "query" : -7
        },
        "output" : -1
    }
    tests.append(test)



    for index, test in enumerate(tests):
        print("Cards : ", test["input"]["cards"])
        print("Query : ", test["input"]["query"])

        if test["output"] != question1.locate_card(test["input"]["cards"],test["input"]["query"]):
            print( "Incorrect for test sequence : ", index)
        else:
            print ("Success for case : ", index)

if __name__ == "__main__":
    test_squence()