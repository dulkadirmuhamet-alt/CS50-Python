def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    has_seen_number = False

    for char in s:
        if not char.isalnum():
            return False
        if char.isdigit():
            if not has_seen_number and char == '0':
                return False
            has_seen_number = True

        elif char.isalpha():
            if has_seen_number:
                return False
    return True
if __name__ == "__main__":
    main()






