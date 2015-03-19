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
        {
            "input": [
                ['Belinda', 'Concepcion', 'Shawna', 'Jaime', 'Madelyn', 'Ken', 'Aisha', 'Misty',
                 'Lance', 'Jeffrey'],
                [['Concepcion', 'Lance'], ['Misty', 'Jaime'], ['Madelyn', 'Jeffrey'],
                 ['Belinda', 'Ken']]],
            "answer": [7,
                       [['Belinda', 'Concepcion', 'Shawna', 'Jaime', 'Madelyn', 'Ken', 'Aisha',
                         'Misty', 'Lance', 'Jeffrey'],
                        [['Concepcion', 'Lance'], ['Misty', 'Jaime'], ['Madelyn', 'Jeffrey'],
                         ['Belinda', 'Ken']]]],
        },
        {
            "input": [['Jared', 'Pearlie', 'Ricardo', 'Lonnie', 'Loraine', 'Morris', 'Meredith',
                       'Deborah', 'Sergio', 'Philip', 'Jessie', 'Consuelo', 'Antonia', 'Sonja'],
                      [['Pearlie', 'Jessie'], ['Philip', 'Sonja'], ['Morris', 'Meredith'],
                       ['Lonnie', 'Deborah'], ['Jared', 'Antonia'], ['Ricardo', 'Consuelo'],
                       ['Sergio', 'Loraine']]],
            "answer": [11,
                       [['Jared', 'Pearlie', 'Ricardo', 'Lonnie', 'Loraine', 'Morris', 'Meredith',
                         'Deborah', 'Sergio', 'Philip', 'Jessie', 'Consuelo', 'Antonia', 'Sonja'],
                        [['Pearlie', 'Jessie'], ['Philip', 'Sonja'], ['Morris', 'Meredith'],
                         ['Lonnie', 'Deborah'], ['Jared', 'Antonia'], ['Ricardo', 'Consuelo'],
                         ['Sergio', 'Loraine']]]],
        },
        {
            "input": [
                ['Sidney', 'Francis', 'Earline', 'Cecil', 'Kimberly', 'Sybil', 'Ronald', 'Oscar',
                 'Corine', 'Jamie', 'Hope', 'Joel'],
                [['Sidney', 'Jamie'], ['Ronald', 'Earline'], ['Sybil', 'Joel']]],
            "answer": [8,
                       [['Sidney', 'Francis', 'Earline', 'Cecil', 'Kimberly', 'Sybil', 'Ronald',
                         'Oscar', 'Corine', 'Jamie', 'Hope', 'Joel'],
                        [['Sidney', 'Jamie'], ['Ronald', 'Earline'], ['Sybil', 'Joel']]]],
        },
        {
            "input": [
                ['Liz', 'Juan', 'Cory', 'Stefanie', 'Olive', 'Bettye', 'Ora', 'Dixie', 'Henry'],
                []],
            "answer": [7,
                       [['Liz', 'Juan', 'Cory', 'Stefanie', 'Olive', 'Bettye', 'Ora', 'Dixie',
                         'Henry'], []]],
        },
        {
            "input": [['Ricardo', 'Millicent', 'Shawna', 'Susanna', 'Bernice', 'Tyrone', 'Nathan',
                       'Larry', 'Katina', 'Cody', 'Goldie', 'Anastasia', 'Ilene', 'Kenneth',
                       'Rebekah'],
                      [['Bernice', 'Nathan'], ['Larry', 'Rebekah'], ['Ricardo', 'Anastasia'],
                       ['Tyrone', 'Millicent'], ['Katina', 'Cody']]],
            "answer": [12,
                       [['Ricardo', 'Millicent', 'Shawna', 'Susanna', 'Bernice', 'Tyrone',
                         'Nathan', 'Larry', 'Katina', 'Cody', 'Goldie', 'Anastasia', 'Ilene',
                         'Kenneth', 'Rebekah'],
                        [['Bernice', 'Nathan'], ['Larry', 'Rebekah'], ['Ricardo', 'Anastasia'],
                         ['Tyrone', 'Millicent'], ['Katina', 'Cody']]]],
        },
        {
            "input": [
                ['Earline', 'Tyrone', 'Frederick', 'Noelle', 'Derek', 'Julian', 'Peggy', 'Hugh',
                 'Nellie', 'Della', 'Arline', 'Guy', 'Robert', 'Virginia'],
                [['Noelle', 'Guy'], ['Derek', 'Peggy'], ['Julian', 'Nellie'], ['Hugh', 'Earline'],
                 ['Robert', 'Virginia'], ['Della', 'Frederick']]],
            "answer": [10,
                       [['Earline', 'Tyrone', 'Frederick', 'Noelle', 'Derek', 'Julian', 'Peggy',
                         'Hugh', 'Nellie', 'Della', 'Arline', 'Guy', 'Robert', 'Virginia'],
                        [['Noelle', 'Guy'], ['Derek', 'Peggy'], ['Julian', 'Nellie'],
                         ['Hugh', 'Earline'], ['Robert', 'Virginia'], ['Della', 'Frederick']]]],
        },
    ]
}
