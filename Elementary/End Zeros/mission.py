def end_zeros(num: int) -> int:
    # your code here
    if str(num).endswith('00'):
        return 2
    elif str(num).endswith('0'):
        return 1
    else:
        return 0


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
