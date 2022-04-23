from models.user import User
import repositories.user_repository as user_repository

from models.trip import Trip
from models.city import City
from models.location import Location



user1 = User("Jimbo123", 28, "Beach, Cusine, Hiking")
user_repository.save(user1)

user2 = User("BiminiBabes", 32, "Hot Climate, 5 Star, Wildllife")
user_repository.save(user2)