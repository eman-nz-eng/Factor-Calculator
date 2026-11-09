# ask the user for width and
# loop until they enter a number that is greater than zero

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
while True:
    to_factor = num_check("To factor: ")
    print ("You chose to factor: ", to_factor)

    if to_factor == "xxx":
        break