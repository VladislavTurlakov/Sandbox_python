def is_a_valid_message(message):
    message = [word for word in message]  #список элементов(str) message
    figures = "0123456789"  #цифры
    length = 0  #длина компоненты после числа
    number = 0  #само число
    status = True  #значение valid
    for i in range(len(message)-1):
        if message[i] in figures and message[i + 1] not in figures:
            if length != number:
                status = False
            else:
                length = 0
            number = int(message[i])
            continue
        length += 1
    return status

print(is_a_valid_message("3hey5hello2hi5"))