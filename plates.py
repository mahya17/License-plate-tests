def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length
    if not (2 <= len(s) <= 6):
        return False

    # Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # No punctuation
    if not s.isalnum():
        return False

    # Digits must come only at the end
    digit_started = False
    for i, ch in enumerate(s):
        if ch.isdigit():
            if not digit_started:
                # First digit cannot be 0
                if ch == "0":
                    return False
                digit_started = True
        else:  # ch is a letter
            if digit_started:
                return False

    return True


if __name__ == "__main__":
    main()
