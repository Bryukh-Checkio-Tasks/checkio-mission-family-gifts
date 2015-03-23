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
            "input": [['Doreen', 'Fred', 'Yolanda'], [['Doreen', 'Fred']]],
            "answer": [0,
                       [['Doreen', 'Fred', 'Yolanda'], [['Doreen', 'Fred']]]],
        },
        {
            "input": [['Nelson', 'Kaitlin', 'Amelia', 'Jack'],
                      [['Kaitlin', 'Jack'], ['Nelson', 'Amelia']]],
            "answer": [2,
                       [['Nelson', 'Kaitlin', 'Amelia', 'Jack'],
                        [['Kaitlin', 'Jack'], ['Nelson', 'Amelia']]]],
        },
        {
            "input": [['Allison', 'Robin', 'Petra', 'Curtis', 'Bobbie', 'Kelly'],
                      [['Allison', 'Curtis'], ['Robin', 'Kelly']]],
            "answer": [4,
                       [['Allison', 'Robin', 'Petra', 'Curtis', 'Bobbie', 'Kelly'],
                        [['Allison', 'Curtis'], ['Robin', 'Kelly']]]],
        },
        {
            "input": [['Melisa', 'Dee', 'Annmarie', 'Gerald', 'Rafael'],
                      [['Melisa', 'Gerald'], ['Rafael', 'Annmarie']]],
            "answer": [2,
                       [['Melisa', 'Dee', 'Annmarie', 'Gerald', 'Rafael'],
                        [['Melisa', 'Gerald'], ['Rafael', 'Annmarie']]]],
        },
        {
            "input": [['Ricardo', 'Eugene', 'Delia', 'Delores', 'Ella', 'Kurt'],
                      [['Eugene', 'Ella'], ['Delores', 'Kurt'], ['Ricardo', 'Delia']]],
            "answer": [4,
                       [['Ricardo', 'Eugene', 'Delia', 'Delores', 'Ella', 'Kurt'],
                        [['Eugene', 'Ella'], ['Delores', 'Kurt'], ['Ricardo', 'Delia']]]],
        },
        {
            "input": [
                ['Loraine', 'Leah', 'Jenifer', 'Russell', 'Benjamin', 'Todd', 'Maryanne', 'Penny',
                 'Matthew'], [['Loraine', 'Benjamin'], ['Leah', 'Matthew'], ['Todd', 'Jenifer']]],
            "answer": [6,
                       [['Loraine', 'Leah', 'Jenifer', 'Russell', 'Benjamin', 'Todd', 'Maryanne',
                         'Penny', 'Matthew'],
                        [['Loraine', 'Benjamin'], ['Leah', 'Matthew'], ['Todd', 'Jenifer']]]],
        },
    ],
    "Extra": [
        {
            "input": [['Alex', 'Monique', 'Tim', 'Robert', 'Joseph', 'Kitty', 'Eugenia', 'Tamika',
                       'Rene', 'Maggie'],
                      [['Kitty', 'Robert'], ['Tamika', 'Tim'], ['Joseph', 'Maggie'],
                       ['Alex', 'Eugenia'], ['Monique', 'Rene']]],
            "answer": [8,
                       [['Alex', 'Monique', 'Tim', 'Robert', 'Joseph', 'Kitty', 'Eugenia',
                         'Tamika', 'Rene', 'Maggie'],
                        [['Kitty', 'Robert'], ['Tamika', 'Tim'], ['Joseph', 'Maggie'],
                         ['Alex', 'Eugenia'], ['Monique', 'Rene']]]],
        },
        {
            "input": [['Dorothea', 'Vincent', 'Irene', 'Lula', 'Paulette', 'Bill', 'Virginia'],
                []],
            "answer": [5,
                       [['Dorothea', 'Vincent', 'Irene', 'Lula', 'Paulette', 'Bill', 'Virginia'],
                           []]],
        },
        {
            "input": [
                ['Winnie', 'Stella', 'Estela', 'Gordon', 'Jacklyn', 'Lela', 'Barbra', 'Lavonne',
                 'Maurice'], [['Maurice', 'Lela']]],
            "answer": [7,
                       [['Winnie', 'Stella', 'Estela', 'Gordon', 'Jacklyn', 'Lela', 'Barbra',
                         'Lavonne', 'Maurice'], [['Maurice', 'Lela']]]],
        },
        {
            "input": [
                ['Carl', 'Esperanza', 'Tabitha', 'Fred', 'Dixie', 'Delores', 'Erica', 'Samuel',
                 'Erin', 'Amber'], [['Carl', 'Erica'], ['Delores', 'Fred']]],
            "answer": [7,
                       [['Carl', 'Esperanza', 'Tabitha', 'Fred', 'Dixie', 'Delores', 'Erica',
                         'Samuel', 'Erin', 'Amber'], [['Carl', 'Erica'], ['Delores', 'Fred']]]],
        },
        {
            "input": [
                ['Louis', 'Theodore', 'Eleanor', 'Sondra', 'David', 'Herbert', 'Fay', 'Alexandria',
                 'Meghan', 'Nettie', 'Autumn', 'June', 'Jane', 'Jeffery', 'Herminia', 'Jeannie',
                 'Lynnette'], [['Theodore', 'Meghan'], ['Herbert', 'Eleanor'], ['Louis', 'Autumn'],
                               ['Nettie', 'David'], ['Jeffery', 'Fay']]],
            "answer": [14,
                       [['Louis', 'Theodore', 'Eleanor', 'Sondra', 'David', 'Herbert', 'Fay',
                         'Alexandria', 'Meghan', 'Nettie', 'Autumn', 'June', 'Jane', 'Jeffery',
                         'Herminia', 'Jeannie', 'Lynnette'],
                        [['Theodore', 'Meghan'], ['Herbert', 'Eleanor'], ['Louis', 'Autumn'],
                         ['Nettie', 'David'], ['Jeffery', 'Fay']]]],
        },
    ]
}
