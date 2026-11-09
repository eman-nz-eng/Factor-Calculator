# Generate headings, e.g. ----- Heading -----
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Display instructions
def instructions():
    statement_generator("Factor Finder", "-")

    print('''
    To use this program, enter an integer between 1 and 200.
    The program will show the factors of your chosen integer.

    It will also tell you if your chosen number is a prime number (i.e. it has two factors only),
    Unity - a single factor, or a perfect square.

    To exit the program, enter type 'xxx'.
    ''')

# ask the user for width and loop until they enter a number that is greater than zero
def num_check(question):

    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        # ask the user for a number
        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # convert user's input into an integer
            response = int(response)

            # check if user's input is within the correct range
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# work out factors, returns sorted list
def factor (var_to_factor):
    factors = []

    for item in range(1, var_to_factor + 1):
        if item not in factors:
            remainder = var_to_factor % item
            if remainder == 0:
                factors.append(item)

    return factors

# main routine goes here

# display the instructions if requested
want_instructions = input("Press <enter> to read the instructions or any key to continue ")
if want_instructions == "":
    instructions()

while True:
    comment = ""
    to_factor = num_check("To factor: ")
    print ("You chose to factor: ", to_factor)

    all_factors = []

    if to_factor == "xxx":
        break
    elif to_factor != 1:
        all_factors = factor(to_factor)
    else:
        all_factors = ""
        print("One is Unity! It only has one factor - itself!")

    # check if Prime
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number."

    # elif check if a perfect square, i.e. the list has an odd number of factors
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square."

    # create headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    # output factors and comment
    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)
