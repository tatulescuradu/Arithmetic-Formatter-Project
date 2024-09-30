def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes = ""
    results = ""

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_width = max(len(num1), len(num2)) + 2

        first_line += num1.rjust(max_width) + "    "
        second_line += operator + num2.rjust(max_width - 1) + "    "
        dashes += "-" * max_width + "    "

        if operator == '+':
            result = str(int(num1) + int(num2))
        else:
            result = str(int(num1) - int(num2))

        results += result.rjust(max_width) + "    "

    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    dashes = dashes.rstrip()
    results = results.rstrip()

    if display_answers:
        return first_line + "\n" + second_line + "\n" + dashes + "\n" + results
    else:
        return first_line + "\n" + second_line + "\n" + dashes
