def string_reverse(string):
    if len(string) < 1:
        return string
    return string_reverse(string[1:]) + string[0]
