class IncompleteSettings(Exception):
    def __init__(self):
        super().__init__("You are missing some necessary settings in your .env file, or it does not exist")