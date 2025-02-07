class Chores:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.status_to_do = True
        self.status_done = False

class List_of_chores:
    def __init__(self, chore : Chores, status_done, status_to_do):
        self.chores = []

    def add_chore(self, chore):
        self.chores += chore

    def remove_chore(self, chore):
        self.chores -= chore
    
    # def mark_as_done(self, chore, status_done):
        
    def display_list(self):
        f"""
            {self.chores}"""
    
    # def filter_list(self):

