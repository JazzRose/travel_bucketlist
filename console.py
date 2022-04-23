from models.user import User
import repositories.user_repository as user_repository

from models.trip import Trip

from models.city import City
import repositories.city_repository as city_repository

from models.location import Location


# USERS
user1 = User("Jimbo123", 28, "Beach, Cusine, Hiking")
user_repository.save(user1)
user2 = User("BiminiBabes", 32, "Hot Climate, 5 Star, Wildllife")
user_repository.save(user2)

# CITIES
city1 = City(" Hanoi", "Hanoi, the capital of Vietnam, is known for its centuries-old architecture and a rich culture with Southeast Asian, Chinese and French influences. At its heart is the chaotic Old Quarter, where the narrow streets are roughly arranged by trade. There are many little temples, including Bach Ma, honoring a legendary horse, plus Đồng Xuân Market, selling household goods and street food")
city_repository.save(city1)
city2 = City("Ha Long Bay", "Hạ Long Bay, in northeast Vietnam, is known for its emerald waters and thousands of towering limestone islands topped by rainforests. Junk boat tours and sea kayak expeditions take visitors past islands named for their shapes, including Stone Dog and Teapot islets. The region is popular for scuba diving, rock climbing and hiking, particularly in mountainous Cát Bà National Park.")
city_repository.save(city2)
city3 = City("Mexico City", "Mexico City is, and has always been, the sun in the Mexican solar system. Though much-maligned in the past, these days the city is cleaning up its act. Revamped public spaces are springing back to life, the culinary scene is exploding and a cultural renaissance is flourishing.")
city_repository.save(city3)

# LOCATIONSga

