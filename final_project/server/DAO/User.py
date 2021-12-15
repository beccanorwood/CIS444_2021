class User:
    def __init__(self, username, firstname, lastname, email):
        self.username = username
        self.firsname = firstname
        self.lastname = lastname
        self.email = email
        self.inRoom = False

    def setRoom(self):
        self.inRoom = True

    def getRoom(self):
        return self.inRoom
