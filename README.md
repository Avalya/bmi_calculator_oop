# Simple Calculator with PyQt (MVC Pattern)

This project implements a basic calculator application using the PyQt5 library for the graphical user interface (GUI) and follows the Model-View-Controller (MVC) design pattern.

## Project Structure

The project consists of the following file:

-   `calculator.py`: Contains the Python code for the calculator application, including the Model (`Calculator` class) and the Controller/View (`CalculatorWindow` class).

## Class Documentation

### `Calculator` (Model)

This class handles the core logic of the calculator.

**Attributes:**

-   `expression (str)`: Stores the current mathematical expression as a string.

**Methods:**

-   `__init__(self)`: Initializes a new `Calculator` object with an empty `expression`.
-   `add_to_expression(self, char: str)`: Appends the given character (`char`) to the current `expression`.
-   `remove_last_character(self)`: Removes the last character from the `expression`.
-   `clear_expression(self)`: Clears the entire `expression`, setting it back to an empty string.
-   `calculate(self)`: Evaluates the current mathematical `expression`.
    -   Returns:
        -   A numeric result (integer or float) if the expression is valid.
        -   An error message (string) if the expression is invalid (e.g., division by zero, malformed expression).
-   `get_expression(self)`: Returns the current `expression` as a string.

### `CalculatorWindow` (Controller/View)

This class creates the main window of the calculator application, handles user interactions (button clicks), and acts as the Controller by communicating with the `Calculator` model.

**Attributes:**

-   `input_field (QLineEdit)`: A display area for input and results.
-   `calculator (Calculator)`: An instance of the `Calculator` class (the Model).
-   `button0` to `button9 (QPushButton)`: Buttons for digits 0 through 9.
-   `button_plus`, `button_minus`, `button_mul`, `button_div (QPushButton)`: Buttons for arithmetic operators.
-   `clear_button (QPushButton)`: Button to clear the input.
-   `backspace_button (QPushButton)`: Button to remove the last character.
-   `buttons_layout (QGridLayout)`: Layout for the calculator buttons.
-   `layout (QVBoxLayout)`: Main layout for the window.
-   `central_widget (QWidget)`: The central widget of the main window.

**Event Handlers (Methods):**

-   `__init__(self)`: Initializes the `CalculatorWindow`, sets up the GUI elements, and connects button clicks to their respective handlers.
-   `on_button_click(self)`: Handles clicks on digit and operator buttons. Appends the button's text to the `input_field` and the `calculator`'s `expression`. If the "=" button is clicked, it triggers the calculation and displays the result.
-   `clear_input(self)`: Clears the `calculator`'s `expression` and the text in the `input_field`.
-   `backspace(self)`: Removes the last character from the `calculator`'s `expression` and updates the `input_field`.

## How to Run the Code

1.  **Prerequisites:**
    -   Make sure you have Python 3 installed on your system.
    -   Install the PyQt5 library if you haven't already. You can do this using pip:
        ```bash
        pip install PyQt5
        ```

2.  **Running the Application:**
    -   Save the Python code as `calculator.py` in a directory.
    -   Open a terminal or command prompt and navigate to that directory.
    -   Run the application using the command:
        ```bash
        python calculator.py
        ```
    -   A calculator window will appear, allowing you to perform basic arithmetic operations.

## Sample Runs (Input and Output)

Include screenshots here demonstrating different scenarios. Make sure you have taken actual screenshots of your running calculator and placed the image files (e.g., `addition.png`, `multiplication.png`, `division_by_zero.png`, `clear.png`, `backspace.png`) in a folder named `screenshots` within your repository.

**Sample Run 1: Addition**

![Addition](screenshots/addition.png)
**Input (Button Clicks):** `5` `+` `3` `=`
**Output (QLineEdit):** `8`

**Sample Run 2: Multiplication**

![Multiplication](screenshots/multiplication.png)
**
