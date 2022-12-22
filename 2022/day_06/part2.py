import os

START_OF_PACKET_LEN = 4
START_OF_MESSAGE_LEN = 14


def start_of_message_marker(input):

    buffer = list()

    start_of_packet = start_of_packet_marker(input)
    index = 0

    for character in input:
        if index > start_of_packet:
            if len(buffer) == START_OF_MESSAGE_LEN and len(set(buffer)) == len(buffer):
                return index

            buffer.append(character)

            if len(buffer) > START_OF_MESSAGE_LEN:
                del buffer[0]

        index += 1


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
    print(start_of_message_marker(f.readline()))
