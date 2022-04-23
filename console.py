from models.user import User
import repositories.user_repository as user_repository

from models.trip import Trip
import repositories.trip_repository as trip_repository

from models.city import City
import repositories.city_repository as city_repository

from models.location import Location
import repositories.location_repository as location_repository


# USERS
user1 = User("Jimbo123", 28, "Beach, Cusine, Backpacking")
user_repository.save(user1)

user2 = User("BiminiBabes", 32, "Hot Climate, 5 Star, Wildllife")
user_repository.save(user2)



# LOCATIONS
location1 = Location("VietNam", "Backpacking","A land of staggering natural beauty and cultural complexities, of dynamic megacities and hill-tribe villages, Vietnam is both exotic and compelling.")
location_repository.save(location1)

location2 = Location("Mexico", "Cuisine","Palm-fringed beaches, chili-spiced cuisine, steamy jungles, teeming cities, fiesta fireworks, Frida’s angst: Mexico conjures up diverse, vivid dreams. And the reality lives up to them..")
location_repository.save(location2)


# CITIES
city1 = City(" Hanoi", "Hanoi, the capital of Vietnam, is known for its centuries-old architecture and a rich culture with Southeast Asian, Chinese and French influences. At its heart is the chaotic Old Quarter, where the narrow streets are roughly arranged by trade. There are many little temples, including Bach Ma, honoring a legendary horse, plus Đồng Xuân Market, selling household goods and street food",location1)
city_repository.save(city1)

city2 = City("Ha Long Bay", "Hạ Long Bay, in northeast Vietnam, is known for its emerald waters and thousands of towering limestone islands topped by rainforests. Junk boat tours and sea kayak expeditions take visitors past islands named for their shapes, including Stone Dog and Teapot islets. The region is popular for scuba diving, rock climbing and hiking, particularly in mountainous Cát Bà National Park.",location1)
city_repository.save(city2)

city3 = City("Mexico City", "Mexico City is, and has always been, the sun in the Mexican solar system. Though much-maligned in the past, these days the city is cleaning up its act. Revamped public spaces are springing back to life, the culinary scene is exploding and a cultural renaissance is flourishing.",location2)
city_repository.save(city3)

# TRIPS

trip1 = Trip(user1,city1,"Loved HaNoi! Make sure to try the local fresh beer and visit Hoan Kiem Lake!",5,"12/9/2012")
trip_repository.save(trip1)

trip2 = Trip(user2,city3,"Chilling in my 5 Star hotel in the sunshine was great! Enjoyed the tequila and partying, but no space on the airport suttle for my shoe collection",3,"20/7/2015")
trip_repository.save(trip2)
