# 19. Write a program to create a class with methods to search for flights and hotels, 
# and to book and cancel reservations.



class Booking:
    def __init__(self):

        self.__flight = []
        self.__flights = [
        {
            "name": "IndiGo 6E-203",
            "start_location": "Indore",
            "end_location": "Delhi",
            "departure_time": "06:00 AM",
            "arrival_time": "07:30 AM",
            "journey_duration": "1 hour 30 minutes"
        },
        {
            "name": "Air India AI-401",
            "start_location": "Mumbai",
            "end_location": "Bangalore",
            "departure_time": "08:15 AM",
            "arrival_time": "09:55 AM",
            "journey_duration": "1 hour 40 minutes"
        },
        {
            "name": "SpiceJet SG-815",
            "start_location": "Delhi",
            "end_location": "Kolkata",
            "departure_time": "10:30 AM",
            "arrival_time": "12:45 PM",
            "journey_duration": "2 hours 15 minutes"
        },
        {
            "name": "Vistara UK-955",
            "start_location": "Pune",
            "end_location": "Hyderabad",
            "departure_time": "01:00 PM",
            "arrival_time": "02:20 PM",
            "journey_duration": "1 hour 20 minutes"
        },
        {
            "name": "Akasa Air QP-142",
            "start_location": "Chennai",
            "end_location": "Mumbai",
            "departure_time": "03:30 PM",
            "arrival_time": "05:35 PM",
            "journey_duration": "2 hours 5 minutes"
        },
        {
            "name": "IndiGo 6E-512",
            "start_location": "Bangalore",
            "end_location": "Kochi",
            "departure_time": "05:45 PM",
            "arrival_time": "06:50 PM",
            "journey_duration": "1 hour 5 minutes"
        },
        {
            "name": "Air India AI-672",
            "start_location": "Delhi",
            "end_location": "Goa",
            "departure_time": "07:00 PM",
            "arrival_time": "09:30 PM",
            "journey_duration": "2 hours 30 minutes"
        },
        {
            "name": "SpiceJet SG-290",
            "start_location": "Jaipur",
            "end_location": "Ahmedabad",
            "departure_time": "09:15 PM",
            "arrival_time": "10:30 PM",
            "journey_duration": "1 hour 15 minutes"
        }
        ]

        self.__hotel = []
        self.__hotels = [
            {
                "name": "The Grand Palace",
                "city": "Indore",
                "address": "MG Road, Near Rajwada Palace, Indore, Madhya Pradesh",
                "phone": "9876543210"
            },
            {
                "name": "Hotel Royal Orchid",
                "city": "Mumbai",
                "address": "Andheri East, Near Airport Road, Mumbai, Maharashtra",
                "phone": "9876543211"
            },
            {
                "name": "Taj Residency",
                "city": "Delhi",
                "address": "Connaught Place, New Delhi",
                "phone": "9876543212"
            },
            {
                "name": "Hotel Paradise",
                "city": "Jaipur",
                "address": "MI Road, Near City Centre, Jaipur, Rajasthan",
                "phone": "9876543213"
            },
            {
                "name": "The Green Leaf Hotel",
                "city": "Bangalore",
                "address": "Whitefield Main Road, Bangalore, Karnataka",
                "phone": "9876543214"
            },
            {
                "name": "Hotel Sunrise",
                "city": "Udaipur",
                "address": "Lake Pichola Road, Udaipur, Rajasthan",
                "phone": "9876543215"
            },
            {
                "name": "Ocean View Resort",
                "city": "Goa",
                "address": "Calangute Beach Road, Goa",
                "phone": "9876543216"
            },
            {
                "name": "Hotel Blue Diamond",
                "city": "Pune",
                "address": "FC Road, Shivajinagar, Pune, Maharashtra",
                "phone": "9876543217"
            }
        ]

    def book_flight(self):
        flt_name = input("Enter Flight Name : ").lower()
        ok = True
        for flt in self.__flights:
            if flt["name"].lower() == flt_name:
                name = input("Enter Your Name : ").lower()
                self.__name = name

                phone = int(input("Enter Phone No : "))
                if len(str(phone))!=10:
                    return print("Invalid No.")
                self.__phone = phone

                dic =  {"name":name,"phone":phone ,"flt_name": flt_name}
                self.__flight.append(dic)
                print("Flight Booked")
                ok = False
        if ok:
            print("No Flight ")            


    def search_flight(self):
        flt_start = input("Enter Starting Place : ").lower()
        flt_end = input("Enter Ending Place : ").lower()
        ok=True
        for place in self.__flights:
            if place["start_location"].lower() == flt_start and place["end_location"].lower() == flt_end:
                print(f"Availabe Flight : {place}")
                ok = False
        if ok:
            print("No flight Availabe")


    def cancel_flight(self):
        name = input("Enter Flight Name for cancel ").lower()
        for flt in self.__flight:
            if flt["flt_name"] == name:
                self.__flight.remove(flt)
            else:
                print("Invalid Item")

    def book_hotel(self):
        htl_name = input("Enter Hotel Name : ").lower()
        ok = True
        for htl in self.__hotels:
            if htl["name"].lower() == htl_name:
                name = input("Enter Your Name : ")
                self.__name = name

                phone = int(input("Enter Phone No : "))
                if len(str(phone))!=10:
                    return print("Invalid No.")
                self.__phone = phone

                dic =  {"name":name,"phone":phone,"htl_name":htl_name}
                print(dic)
                self.__hotel.append(dic)
                print("Hotel Booked")
                ok = False
        if ok:
            print("No Hotel Availabe ")            


    def search_hotel(self):
        city = input("Enter City : ").lower()
        ok=True
        for place in self.__hotels:
            if place["city"].lower() == city:
                print(f"Availabe hotel : {place}")
                ok = False
        if ok:
            print("No Hotel Availabe")


    def cancel_hotel(self):
        name = input("Enter hotel Name for cancel ").lower()
        ok = True
        for htl in self.__hotel:
            if htl["htl_name"].lower() == name:
                self.__hotel.remove(htl)
                print(f"hotel {name} reservation is cancelled")
                ok=False

        if ok:
            print("No hotel for Cancel")


person = Booking()
person.search_hotel()
person.book_hotel()
person.cancel_hotel()
