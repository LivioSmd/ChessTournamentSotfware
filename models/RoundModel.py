class RoundModel:
    def __init__(self):
        self.name = 'Round'
        self.match_list = []
        self.start_date = 'Undefined'
        self.end_date = 'Undefined'

    def __str__(self):
        return f"{self.name} from: {self.start_date} to: {self.end_date}"

    def __repr__(self):
        return f"{self.name} from: {self.start_date} to: {self.end_date}"

    def serialize(self):
        """round serialization"""
        round_serialized = {
            "name": self.name,
            "matchList": self.match_list,
            "startDate": self.start_date,
            "endDate": self.end_date,
        }

        return round_serialized

    def deserialize(self, round):
        """round deserialization"""
        self.name = round.get('name')
        self.match_list = round.get('matchList')
        self.start_date = round.get('startDate')
        self.end_date = round.get('endDate')

        return self
