# James Chau
def encode_rle(flat_data):

    count = 1
    result = []

    for x, item in enumerate(flat_data):
        if x == 0:
            continue
        elif item == flat_data[x - 1]:
            count += 1
            if count >= 15:
                result.append(count)
                result.append((flat_data[x - 1]))
                count = 0
        else:
            result.append(count)
            result.append((flat_data[x - 1]))
            count = 1
            result.append(count)
            result.append((flat_data[len(flat_data) - 1]))
    return result

#Decode function by Abdullah Islam
def decode(password):
    encoded_num = ''
    for i in range(8):

        if str(int(password[i])) == '2':
            encoded_num += '9'
        elif str(int(password[i])) == '1':
            encoded_num += '8'
        elif str(int(password[i])) == '0':
            encoded_num += '7'
        else:
            encoded_num += str(int(password[i]) - 3)

    return encoded_num