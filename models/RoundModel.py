class RoundModel:
    def __init__(self):
        self.name = 'Round'
        self.match_list = []
        self.start_date = 'start_date'
        self.end_date = 'end_date'

    def __str__(self):
        return f"{self.name} {self.match_list}"  # TODO {self.start_date} {self.end_date}

    def __repr__(self):
        return f"{self.name} {self.match_list}"  # TODO {self.start_date} {self.end_date}

    def serialize(self):
        round_serialized = {
            "name": self.name,
            "matchList": self.match_list,
            "startDate": self.start_date,
            "startEnd": self.end_date,
        }

        return round_serialized

    def deserialize(self, round):
        self.name = round.get('name')
        self.match_list = round.get('matchList')
        self.start_date = round.get('startDate')
        self.end_date = round.get('endDate')

        return self
