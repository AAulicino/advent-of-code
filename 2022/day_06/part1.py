import os

START_OF_PACKET_LEN = 4


def start_of_packet_marker(input):

    buffer = list()

    index = 0
    for character in input:
        if len(buffer) == START_OF_PACKET_LEN and len(set(buffer)) == len(buffer):
            return index

        buffer.append(character)

        if len(buffer) > START_OF_PACKET_LEN:
            del buffer[0]

        index += 1


with open(os.path.dirname(__file__) + "/input.txt") as f:
    print(start_of_packet_marker(f.readline()))
