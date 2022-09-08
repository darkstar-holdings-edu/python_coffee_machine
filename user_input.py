def get(message: str, valid_responses: list[str]) -> str:
    """
    Retrieves and validates the user's input.

    Returns the user's response as a string.
    """
    response = None
    while True:
        response = input(message).lower()
        if response in valid_responses:
            break

        print("huh?")

    return response


def get_integer(message: str, min: int | None = None, max: int | None = None) -> str:
    """
    Retrieves and validates the user's integer input.

    Returns the user's response as an integer
    """
    response = None
    while True:
        try:
            response = int(input(message))
        except ValueError:
            print("huh?")
            continue

        if type(min) == int and response < min:
            print(f"Must be a value greater than {min}")
        elif type(max) == int and response > max:
            print(f"Must be a value less than {max}")
        else:
            break

    return response
