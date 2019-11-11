"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    edit_matrix = [[0 for j in range(num_cols)] for i in range(num_rows)]
    return edit_matrix  


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    i = 0
    j = 0
    for cols in edit_matrix:
        edit_matrix[0][0] = 0
        edit_matrix[i][0] = edit_matrix[i - 1][0] + remove_weight
        i += 1
    for rows in edit_matrix[0]:
        edit_matrix[0][0] = 0
        edit_matrix[0][j] = edit_matrix[0][j - 1] + add_weight
        j += 1
    return edit_matrix



def minimum_value(numbers: tuple) -> int:
    return min(numbers)


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    remove = 0
    add = 0
    sub = 0
    subst = 0
    minimum = 0
    for i in range(1, len(edit_matrix)):
        for j in range(1, len(edit_matrix[0])):
            remove = edit_matrix[i - 1][j] + remove_weight
            add = edit_matrix[i][j - 1] + add_weight
            if original_word[i - 1] == target_word[j - 1]:
                subst = edit_matrix[i - 1][j - 1]
            elif original_word[i - 1] != target_word[j - 1]:
                subst = edit_matrix[i - 1][j - 1] + substitute_weight
            edit_matrix[i][j] = min(remove, add, subst)

def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    generate_edit_matrix(num_rows, num_cols)
    initialize_edit_matrix(edit_matrix, add_weight, remove_weight)
    fill_edit_matrix(edit_matrix, add_weight, remove_weight, substitute_weight, target_word, original_word)
    print(edit_matrix[num_rows - 1][num_cols - 1])
    return edit_matrix[num_rows - 1][num_cols - 1]


