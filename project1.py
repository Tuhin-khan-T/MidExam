


class Star_Cinema:
    hall_list = []
    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
     self.rows = rows

     self.cols = cols

     self.hall_no = hall_no

     self.seats = {}

     self.show_list = []

     self.initialize_seats()

     Star_Cinema.entry_hall(self)

    def initialize_seats(self):

        for row in range(1, self.rows + 1):

            self.seats[row] = [0] * self.cols

    def entry_show(self, id, movie_name, time):

        show_info = (id, movie_name, time)
        
        self.show_list.append(show_info)

        self.seats[id] = [[0] * self.cols for _ in range(self.rows)]

    def book_seats(self, id, seat_list):

        if id in self.seats:

            for row, col in seat_list:

                if self.is_seat_available(id, row, col):

                    self.seats[id][row - 1][col - 1] = 1

                    print(f"Seat ({row}, {col}) booked successfully.")

                else:

                    print(f"Seat ({row}, {col}) is already booked or invalid.")
        else:

            print("Show not found.")

    def is_seat_available(self, id, row, col):

        if id in self.seats and 1 <= row <= self.rows and 1 <= col <= self.cols:

            return self.seats[id][row - 1][col - 1] == 0
        
        return False

    def view_show_list(self):

        print("List of Shows:")

        for id, movie_name, time in self.show_list:

            print(f"ID: {id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, id):

        if id in self.seats:

            print(f"Available Seats for Show {id}:")

            for row in range(1, self.rows + 1):

                for col in range(1, self.cols + 1):

                    if self.is_seat_available(id, row, col):

                        print(f"Seat ({row}, {col})")
        else:

            print("Show not found.")


hall1 = Hall(rows=4, cols=6, hall_no=101)
hall2 = Hall(rows=5, cols=8, hall_no=102)

hall1.entry_show(1, "The Avengers", "3:00 PM")
hall1.entry_show(2, "Spider-Man: I rone mane ", "6:00 PM")
hall2.entry_show(3, "Zawan ", "2:30 PM")
hall2.entry_show(4, "kike", "5:30 PM")

hall1.view_show_list()
hall2.view_show_list()

hall1.book_seats(1, [(1, 2), (2, 3), (3, 4)])
hall1.book_seats(2, [(1, 2), (2, 3), (3, 4)])  

hall1.view_available_seats(1)
