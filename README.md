# NumScript

NumScript is a simple interpreter for a basic arithmetic expression language called NumScript Language Version 1.0. It allows users to input arithmetic expressions and generates corresponding code.

## Team Members
- **Deep Patel:** Project Manager
- **Darsh Patel:** Language Design/Architect
- **Dev Patel:** Compiler Engineer
- **Dravya Patel:** Quality Assurance/Testing, Documentation Specialist

## Usage

To run NumScript, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone git@github.com:Devv64bit/NumScript.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd NumScript
    ```

3. Run the NumScript interpreter:

    ```bash
    python numscript.py
    ```

4. You will be prompted to enter NumScript code. Type your NumScript code and press Enter to see the generated code.

5. To exit the NumScript interpreter, type "exit" and press Enter.

## How It Works

NumScript follows a multi-step process to interpret and generate code for arithmetic expressions:

1. **Lexical Analysis:** The input code is broken down into tokens by the Lexer.
2. **Parsing:** The Parser constructs a syntax tree to represent the structure of the code.
3. **Semantic Analysis:** The Semantic Analyzer ensures the correctness of the code.
4. **Code Generation:** The Code Generator translates the syntax tree into executable code.

## Sample Input and Output

### Input:
    2 + 3 * (4 - 1)

### Output:
    Generated code: 11


## Contribution

If you'd like to contribute to NumScript, feel free to fork the repository and submit a pull request. Contributions are welcome and appreciated!

