"""
Nabil Arbouz

Valid Parenthesis
All Test Cases Passed on LeetCode

Test Cases:
Example 1:
    Input: "()"
    Output: true
Example 2:
    Input: "()[]{}"
    Output: true
Example 3:
    Input: "(]"
    Output: false
Example 4:
    Input: "([)]"
    Output: false
Example 5:
    Input: "{[]}"
    Output: true


"""
from hw6.Stack import Stack


def test_parentheses(test_string):
    # We store a dictionary to hold the parentheses values
    parentheses_dict = {')': '(', ']': '[', '}': '{'}
    # Stack to hold the right-type parentheses
    right_char_stack = Stack()
    # Stack for all the test string characters
    char_stack = Stack()

    # Push all of the characters into the stack
    for char in test_string:
        char_stack.push(char)

    # Check for the edge cases (Empty string, odd number of chars, bad starting
    # or ending characters
    if not char_stack:
        return True
    elif char_stack.size() % 2 != 0:
        return False
    elif char_stack.peek() not in parentheses_dict.keys() or \
            test_string[0] in parentheses_dict.keys():
        return False

    while char_stack.size() > 0:
        # We pop an item and check where it needs to go
        current_char = char_stack.pop()
        # Add it to the right-sided character stack if it is a right parentheses
        if current_char in parentheses_dict.keys():
            right_char_stack.push(current_char)
        # Compare the left character to its corresponding character in the right
        # character stack. If it matches, continue, if not return false
        elif current_char == parentheses_dict[right_char_stack.pop()]:
            continue
        else:
            return False
    # Final check for balance
    if right_char_stack.size() > 0:
        return False
    return True


def main():
    test_string = "{[]}"
    print(test_parentheses(test_string))


main()
