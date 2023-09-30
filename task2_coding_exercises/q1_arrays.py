"""
Complete the following functions.
Test cases can be found in the "tests" folder
"""


def find_min_index(arr: list[int]) -> int:
    """
    Find index where minimum value first occurs in array.
    The array will always have at least 1 element.
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0
    eg. [100] => 0

    @param array of integers
    @returns integer index of minimum integer
    """

    # insert code here
    minNum = arr[0];
    minIndex = 0 

    for i in range(1, len(arr)):
        if arr[i] < minNum:
            minNum = arr[i]
            minIndex = i
    
    return minIndex
    pass 


def reverse_str_arr(s: str) -> list[str]:
    """
    Return array of string characters, but in reverse order.
    eg. "abc" => ['c', 'b', 'a']
    eg. "abba" => ['a', 'b', 'b', 'a']
    eg. "!!-.2" => ['2', '.', '-', '!', '!']

    @param string
    @returns array of characters
    """

    # insert code here
    length = len(s)
    newArr = []

    for x in range(length - 1, -1, -1):
        newArr.append(s[x])
    
    return newArr
    pass


def most_freq_element(arr: list[int]) -> int:
    """
    Find the value that appears the most frequently in the array.
    If there are multiple, return the value that appears first in the array.
    The array will always have at least 1 element.
    eg. [1, 33, 1, -2, 33] => 1
    eg. [1, 2, 3, 4] => 1
    eg. [3, 5, 1, 5, 3] => 3

    @param array of integers
    @returns integer value that appears the most frequently in the array
    """

    # insert code here
    most_freq = arr[0]
    max_count = 1

    for i in range(len(arr)):
        current_value = arr[i]
        current_count = 1

        for j in range(i + 1, len(arr)):
            if arr[j] == current_value:
                current_count += 1
    
        if current_count > max_count:
            most_freq = current_value
            max_count = current_count

    return most_freq

    pass
