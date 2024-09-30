# Arithmetic Formatter

This project is a Python function that formats arithmetic problems in a vertical manner, making it easier to read and solve. The function handles basic addition and subtraction operations and validates the input for correct formatting.

## Function: `arithmetic_arranger`

### Description
The `arithmetic_arranger` function takes a list of arithmetic problems and returns them arranged vertically and side-by-side. It can also display the answers if requested.

### Parameters
- `problems` (list): A list of strings where each string represents an arithmetic problem (e.g., "32 + 698").
- `display_answers` (bool, optional): A boolean value indicating whether to display the answers. Default is `False`.

### Returns
- A string that represents the formatted arithmetic problems arranged vertically. If there are any errors in the input, it will return an appropriate error message.

### Error Handling
The function performs the following checks and returns error messages for:
- Too many problems: More than 5 problems provided.
- Invalid operator: Only '+' and '-' are accepted.
- Invalid numbers: Numbers must consist only of digits.
- Number length: Each number must not exceed four digits.

### Example Usage

```python
# Example 1
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# Output:
#    32      3801      45      123
# + 698    -    2    + 43    + 49
# -----    ------    ----    -----

# Example 2
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
# Output:
#     3      988
# + 855    +  40
# -----    -----
#   858     1028
```

### How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/arithmetic-formatter.git
   cd arithmetic-formatter
   ```
2. Open a Python environment (Python 3.x required).
3. Run the Python script containing the `arithmetic_arranger` function.

### Acknowledgments
This project was created as part of a learning exercise to practice Python programming and error handling.
