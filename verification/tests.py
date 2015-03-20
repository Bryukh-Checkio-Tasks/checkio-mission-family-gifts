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
            "input": [['Cara', 'Adam', 'Veronica'], [['Adam', 'Veronica']]],
            "answer": [0,
                       [['Cara', 'Adam', 'Veronica'], [['Adam', 'Veronica']]]],
        },
        {
            "input": [['Brad', 'Amalia', 'Gilbert', 'Henrietta'],
                      [['Henrietta', 'Brad'], ['Gilbert', 'Amalia']]],
            "answer": [2,
                       [['Brad', 'Amalia', 'Gilbert', 'Henrietta'],
                        [['Henrietta', 'Brad'], ['Gilbert', 'Amalia']]]],
        },
        {
            "input": [['Madeline', 'Lorrie', 'Michael', 'Herbert', 'Jimmie', 'Leo'],
                      [['Michael', 'Lorrie'], ['Leo', 'Madeline']]],
            "answer": [3,
                       [['Madeline', 'Lorrie', 'Michael', 'Herbert', 'Jimmie', 'Leo'],
                        [['Michael', 'Lorrie'], ['Leo', 'Madeline']]]],
        },
        {
            "input": [['Joan', 'Madeline', 'Juan', 'Theodore', 'Claudette', 'Gerald'],
                      [['Madeline', 'Juan'], ['Theodore', 'Claudette'], ['Joan', 'Gerald']]],
            "answer": [3,
                       [['Joan', 'Madeline', 'Juan', 'Theodore', 'Claudette', 'Gerald'],
                        [['Madeline', 'Juan'], ['Theodore', 'Claudette'], ['Joan', 'Gerald']]]],
        },
        {
            "input": [['Alisha', 'Joan', 'Philip', 'Yvonne', 'Shawn', 'Erik', 'Chester', 'Eduardo',
                       'Mattie'], [['Philip', 'Shawn'], ['Chester', 'Yvonne'], ['Alisha', 'Erik'],
                                   ['Joan', 'Eduardo']]],
            "answer": [6,
                       [['Alisha', 'Joan', 'Philip', 'Yvonne', 'Shawn', 'Erik', 'Chester',
                         'Eduardo', 'Mattie'],
                        [['Philip', 'Shawn'], ['Chester', 'Yvonne'], ['Alisha', 'Erik'],
                         ['Joan', 'Eduardo']]]],
        },
        {
            "input": [['Melba', 'Brenda', 'Brandie', 'Ruby', 'Frances', 'Lee'], []],
            "answer": [4,
                       [['Melba', 'Brenda', 'Brandie', 'Ruby', 'Frances', 'Lee'], []]],
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
