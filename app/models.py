users = []
rides = []

class User:
    def __init__(self, name, username,email,password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def add(self):
        users.append(self)

        for user in users:
            print(self.serialize(user))
    
    def serialize(self, user):
        return {
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

class Ride:
    ride_id = 1
    def __init__(self, name=None, pickup=None, dropoff=None,time=None):
        self.name = name
        self.pickup = pickup
        self.dropoff = dropoff
        self.time = time
        self.id = Ride.ride_id

        Ride.ride_id +=1

    def add(self):
        rides.append(self)

        for ride in rides:
            print(self.serialize(ride))

    def get_all(self):
        _rides = []
        for ride in rides:
            _rides.append(self.serialize(ride))
        return _rides

    def get_one(self, id):
        for ride in rides:
            if ride.id == id: 
                return self.serialize(ride)
        return None
    
    def serialize(self,ride):
        return {
            "name": ride.name,
            "pickup": ride.pickup,
            "dropoff": ride.dropoff,
            "time": ride.time,
            "id":ride.id

        }

    def delete(self, id):
        for ride in rides:
            if ride.id == id:
                ride.remove(rides)
                


