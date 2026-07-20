class Movie:
    def __init__(self,title,duration):
        self.title = title
        self.duration = duration

    @classmethod
    def from_hours_minutes(cls,title,hours,minutes):
        duration = hours*60 + minutes
        return cls(title, duration)
    
    @staticmethod
    def is_valid_duration(minutes):
        if minutes < 0:
            return False
        else:
            return minutes > 0
    
p1 =Movie("spider-man",120)

print(p1.is_valid_duration(14))
p2 = Movie.from_hours_minutes("Avengers", 2, 30)
print(p2.title)
