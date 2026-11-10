
#Hotel Class
class Hotel:
      def __init__(self , name , roomAvailable , location , rating , pricePerRoom):
            self.name = name
            self.roomAvailable = roomAvailable
            self.location = location
            self.rating = rating
            self.pricePerRoom = pricePerRoom

#Users Class
class Users:
      def __init__(self , name , id , bookingCost ):
            self.name = name
            self.id = id
            self.bookingCost = bookingCost

# objects for hotels
hotel1 = Hotel("H4",3,"KSA",4,300)
hotel2 = Hotel("H3",5,"EG",4.8,700)
hotel3 = Hotel("H2",2,"GER",4.5,900)
hotel4 = Hotel("H1",1,"EG",3.5,350)

#objects for users 
user1 = Users("u1",1,1200)
user2 = Users("u2",2,3000)
user3 = Users("u3",3,500)

# Initialize empty lists
hotel_data = []
user_data = []

#list filled with data 
hotel_data.extend([hotel1 , hotel2 , hotel3 , hotel4])
user_data.extend([user1 , user2 , user3])

def printHotelsData(Hotels):
      for hotel in Hotels:
            print(f"The Hotel Name: {hotel.name}\nNumber Of Rooma That Available: {hotel.roomAvailable}")
            print(f"The Hotel Location: {hotel.location}\nHotel Rating: {hotel.rating}")
            print(f"The Hotel Room Price: {hotel.pricePerRoom}")

def printUsersData(HotelsUsers):
      for user in HotelsUsers:
            print(f"User Name: {user.name}")
            print(f"User Booking Cost: {user.bookingCost}")

def sortHotelsByName():
      sortedHotels = sorted(hotel_data , key=lambda hotel: hotel.name)
      printHotelsData(sortedHotels)

def sortHotelByHighestRating ():
      sortedHotels = sorted(hotel_data , key=lambda hotel: hotel.rating , reverse=True)
      printHotelsData(sortedHotels)

def sortHotelByLocation(targetLocation):
      sortedHotels = sorted(hotel_data , key=lambda hotel: hotel.location == targetLocation , reverse=True)
      printHotelsData(sortedHotels)

def sortHotelsByMaximumNumberOfRoomsAvailable():
      sortedHotels = sorted(hotel_data , key=lambda hotel: hotel.roomAvailable , reverse=True)
      printHotelsData(sortedHotels)

printHotelsData(hotel_data)
printUsersData(user_data)
sortHotelsByName()
sortHotelByHighestRating()
sortHotelByLocation("EG")
sortHotelsByMaximumNumberOfRoomsAvailable()