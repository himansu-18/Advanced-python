class Movie:
    def __init__(self):
        self.bookings = {}

    def movie_details(self):
        self.title = input("Enter the movie title: ")
        self.genre = input("Enter the movie genre: ")
        self.duration = input("Enter the movie duration: ")
        self.bookings[self.title] = (self.genre, self.duration)
        print("Movie details added successfully.")

    def display_movies(self):
        if not self.bookings:
            print("No movies found.")
        else:
            for title, details in self.bookings.items():
                print("Title:", title)
                print("Genre:", details[0])
                print("Duration:", details[1])

    def book_ticket(self):
        self.movie_name = input("Enter the movie name to book: ")
        if self.movie_name in self.bookings:
            self.name = input("Enter your name: ")
            print("Ticket booked successfully for", self.name, "to watch", self.movie_name)
        else:
            print("Movie not found.")

    def ext(self):
        print("Exiting the program.")
        exit()

x = Movie()
while True: 
    
    
    print("1.Add Movie Details")
    print("2.Display Movies")
    print("3.Book Ticket")
    print("4.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        x.movie_details()
    elif choice == 2:
        x.display_movies()
    elif choice == 3:
        x.book_ticket()
    elif choice == 4:
        x.ext()