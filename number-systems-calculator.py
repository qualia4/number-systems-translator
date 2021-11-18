def next_letter(letter):
    return chr(ord(letter)+1)


def find_system(number):
    if number.isdigit():
        return 10
    elif number[-2] == 'x':
        return int(number[-1])
    elif number[-3] == 'x':
        return int(number[-2] + number[-1])


def cut_num(number, system):
    if system < 10:
        return number[:-2]
    else:
        return number[:-3]


def counter_to_tens(number, system, degree):
    if number[-1].isdigit():
        return int(number[-1])*(system**degree)
    else:
        return letter_to_number(number[-1])*(system**degree)


def letter_to_number(letter):
    lowest_num = 10
    lowest_letter = 'A'
    while True:
        if letter == lowest_letter:
            return lowest_num
        else:
            lowest_num += 1
            lowest_letter = next_letter(lowest_letter)


def number_to_str(number):
    if number <= 9:
        return str(number)
    else:
        return chr(64 + number - 9)


def transfer_from_tens(number, system):
    result = ''
    while number != 0:
        result = number_to_str(number % system) + result
        number = number // system
    return result


def transfer_to_tens(number):
    result = 0
    degree = 0
    translating_finished = False
    system = find_system(number)
    number = cut_num(number, system)
    while not translating_finished:
        if number != '':
            result += counter_to_tens(number, system, degree)
            degree += 1
            number = number[:-1]
        else:
            translating_finished = True
    return result


program_finished = False
while not program_finished:
    num = input("Enter number: ")
    system = find_system(num)
    system_to_transfer = int(input("What system you want it to be transfered in?: "))
    if system == 10:
        print("Your result:", transfer_from_tens(int(num), system_to_transfer))
    else:
        print("Your result:", transfer_from_tens(transfer_to_tens(num), system_to_transfer))
    want_to_continue = input("Do you want to continue?(yes or no): ")
    if want_to_continue == 'no':
        program_finished = True


