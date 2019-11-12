"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    if isinstance(num_cols, int) and isinstance(num_rows, int):
        edit_matrix = [[0 for j in range(num_cols)] for i in range(num_rows)]
    else:
        edit_matrix = [] 
    return edit_matrix 



def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    if isinstance(add_weight, int) and isinstance(remove_weight, int) and edit_matrix and edit_matrix[0]:
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
    return list(edit_matrix)


def minimum_value(numbers: tuple) -> int:
    return min(list(numbers))


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    if isinstance(add weight, int) and isinstance(remove_weight, int) and isinstance(substitute_weight, int) and isinstance(original_word, str) and isinstance(target_word, str):
        remove = 0
        add = 0
        sub = 0
        subst = 0
        minimum = 0
        for i in range(1, len(edit_matrix)):
            for j in range(1, len(edit_matrix[0])):
                remove = edit_matrix[i - 1][j] + remove_weight
                add = edit_matrix[i][j - 1] + add_weight
                subst = edit_matrix[i - 1][j - 1]
                if i <= len(original_word) and len(target_word) >= j and original_word[i - 1] == target_word[j - 1]:
                    subst = edit_matrix[i - 1][j - 1]
                else:
                    subst = edit_matrix[i - 1][j - 1] + substitute_weight

                edit_matrix[i][j] = minimum_value((remove, add, subst))
    return list(edit_matrix)
    

def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if isinstance(add_weight, int) and isinstance(remove_weight, int) and isinstance(substitute_weight, int) and isinstance(original_word, str) and isinstance(target_word, str) and substitute_weight != None:
        num_rows = len(original_word) + 1
        num_cols = len(target_word) + 1
        edit_matrix = generate_edit_matrix(num_rows, num_cols)
        tuple(edit_matrix)
        tuple(initialize_edit_matrix(edit_matrix, add_weight, remove_weight))
        tuple(fill_edit_matrix(edit_matrix, add_weight, remove_weight, substitute_weight, target_word, original_word))
        return edit_matrix[-1][-1]
    else:
        return -1

