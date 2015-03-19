"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [['Carolina', 'Eduardo'], [['Margret', 'Eduardo']]],
            "answer": [0,
                       [['Carolina', 'Eduardo'], [['Margret', 'Eduardo']]]],
        },
        {
            "input": [['Raul', 'Angel', 'Juliana'], [['Raul', 'Juliana'], ['Bianca', 'Angel']]],
            "answer": [2,
                       [['Raul', 'Angel', 'Juliana'], [['Raul', 'Juliana'], ['Bianca', 'Angel']]]],
        },
        {
            "input": [['Wesley', 'Lucile', 'Madelyn', 'Thelma', 'Della'],
                      [['Thelma', 'Bob'], ['Wesley', 'Lucile']]],
            "answer": [4,
                       [['Wesley', 'Lucile', 'Madelyn', 'Thelma', 'Della'],
                        [['Thelma', 'Bob'], ['Wesley', 'Lucile']]]],
        },
        {
            "input": [['Enrique', 'Eugene', 'Clarissa', 'Gwen', 'Virgil'],
                      [['Eugene', 'Clarissa'], ['Enrique', 'Kristina'], ['Gwen', 'Virgil']]],
            "answer": [3,
                       [['Enrique', 'Eugene', 'Clarissa', 'Gwen', 'Virgil'],
                        [['Eugene', 'Clarissa'], ['Enrique', 'Kristina'], ['Gwen', 'Virgil']]]],
        },
        {
            "input": [
                ['Laura', 'Helga', 'Phillip', 'Greta', 'Catherine', 'Andy', 'Floyd', 'Francisca'],
                [['Catherine', 'Calvin'], ['Andy', 'Helga'], ['Floyd', 'Francisca'],
                 ['Laura', 'Phillip']]],
            "answer": [6,
                       [['Laura', 'Helga', 'Phillip', 'Greta', 'Catherine', 'Andy', 'Floyd',
                         'Francisca'],
                        [['Catherine', 'Calvin'], ['Andy', 'Helga'], ['Floyd', 'Francisca'],
                         ['Laura', 'Phillip']]]],
        },
        {
            "input": [['Naomi', 'Carlos', 'Lenore', 'Jaime', 'Alexander'], []],
            "answer": [4,
                       [['Naomi', 'Carlos', 'Lenore', 'Jaime', 'Alexander'], []]],
        },
    ],
    "Extra": [

    ]
}
