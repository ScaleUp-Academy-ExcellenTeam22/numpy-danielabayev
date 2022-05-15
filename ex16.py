import numpy
import numpy as np


def sort():
    """
    A NumPy program to sort the student id with increasing height of the students from given students id
    and height and then Print the integer indices that describe the sort order by multiple columns and the sorted data.
    """
    student_id = np.array([1, 2, 3, 4, 5, 6, 7])
    student_height = np.array([80., 85., 85., 81., 88., 84., 82.0])
    sort_height = np.lexsort((student_id, student_height))
    for element in sort_height:
        print(student_id[element], student_height[element])


if __name__ == '__main__':
    sort()
