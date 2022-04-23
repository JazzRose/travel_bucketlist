from models.city import City


class Trip:
    def __init__ (self, user, city ,review, rating, date, id = None):
        self.user = user
        self.city= city
        self.review = review
        self.rating = rating
        self.date = date
        self.id = id