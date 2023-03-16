class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []

    room0 = Room("Bedroom 2", 3, 1, None, None)
    room_list.append(room0)

    room1 = Room("South Hall", 4, 2, None, 0)
    room_list.append(room1)

    room2 = Room("Dining Room", 5, None, None, 1)
    room_list.append(room2)

    room3 = Room("Bedroom 1", None, 4, 0, None)
    room_list.append(room3)

    room4 = Room("North Hall", 6, 5, 1, 3)
    room_list.append(room4)

    room5 = Room("Kitchen", None, None, 2, 4)
    room_list.append(room5)

    room6 = Room("Balcony", None, None, 4, None)
    room_list.append(room6)

    current_room = 0

    print(room_list[current_room].description)


main()
