from typing import Tuple, Optional


def find_closing_parenthesis(expression: str) -> int:
    nested = 0
    for i, char in enumerate(expression):
        if char == '(':
            nested += 1
        elif char == ')':
            nested -= 1
        if nested == 0:
            return i


def partition_first_contained_expression(expression: str) -> Tuple[Optional[str], str, Optional[str]]:
    first_open_parenthesis = expression.index('(')
    left_expression = expression[:first_open_parenthesis].strip()
    if left_expression == '':
        left_expression = None
    remaining_expression = expression[first_open_parenthesis:]
    closing_parenthesis = find_closing_parenthesis(remaining_expression)
    contained_expression = remaining_expression[1:closing_parenthesis]
    right_expression = remaining_expression[closing_parenthesis + 1:].strip()
    if right_expression == '':
        right_expression = None
    return left_expression, contained_expression, right_expression


def evaluate_expression(expression: str, addition_first: bool = False) -> str:
    if '(' in expression:
        left, contained, right = partition_first_contained_expression(expression)
        if left and right:
            return evaluate_expression(' '.join([left, evaluate_expression(contained, addition_first), right]), addition_first)
        elif left:
            return evaluate_expression(' '.join([left, evaluate_expression(contained, addition_first)]), addition_first)
        elif right:
            return evaluate_expression(' '.join([evaluate_expression(contained, addition_first), right]), addition_first)
        else:
            return evaluate_expression(contained, addition_first)

    expression_pieces = expression.split(' ')
    if len(expression_pieces) == 1:
        return expression

    left, operation, right = expression_pieces[:3]
    if len(expression_pieces) == 3:
        if operation == '*':
            return str(int(left) * int(right))
        elif operation == '+':
            return str(int(left) + int(right))
        else:
            raise ValueError('ERROR - unexpected operation')

    next_operation, next_right = expression_pieces[3:5]
    if addition_first and next_operation == '+' and operation == '*':
        updated_expression = ' '.join([left, operation, '(' + right, next_operation, next_right + ')'])
        remaining_expression = ' '.join(expression_pieces[5:])
        if remaining_expression != '':
            updated_expression = ' '.join([updated_expression, remaining_expression])
        return evaluate_expression(updated_expression, addition_first)

    first_result = evaluate_expression(' '.join([left, operation, right]), addition_first)
    remaining_expression = ' '.join(expression_pieces[3:])
    return evaluate_expression(' '.join([first_result, remaining_expression]), addition_first)


def main():
    with open('input_files/day_18.txt') as f:
        expressions = [line.strip() for line in f.readlines()]
    results = [int(evaluate_expression(expression)) for expression in expressions]
    print(f'the sum of all results is {sum(results)}')
    addition_first_results = [int(evaluate_expression(expression, True)) for expression in expressions]
    print(f'the sum of all results if addition takes precedence is {sum(addition_first_results)}')


if __name__ == '__main__':
    main()
