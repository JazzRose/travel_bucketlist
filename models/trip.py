class Trip:
    def __init__ (self, user_id, location_id ,review, rating, date, id = None):
        self.user_id = user_id
        self.location_id = location_id
        self.review = review
        self.rating = rating
        self.date = date
        self.id = id