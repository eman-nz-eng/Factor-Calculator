# Generate headings, e.g. ----- Heading -----

def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Display instructions
def instructions():
    statement_generator("Instructions", "-")

    print ('''
    To use this program, enter an integer between 1 and 200.
    The program will show the factors of your chosen integer.
    
    It will also tell you if your chosen number is a prime number (i.e. it has two factors only),
    a Unity - a single factor, or a perfect square.
    
    To exit the program, enter type 'xxx'.
    ''')

# main routine goes here

# display the instructions if requested
want_instructions = input("Press <enter> to read the instructions or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")
