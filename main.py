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

