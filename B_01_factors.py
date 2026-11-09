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


# main routine goes here

# display the instructions if requested
want_instructions = input("Press <enter> to read the instructions or any key to continue ")
if want_instructions == "":
    instructions()


while True:
    to_factor = num_check("To factor: ")
    print ("You chose to factor: ", to_factor)

    if to_factor == "xxx":
        break