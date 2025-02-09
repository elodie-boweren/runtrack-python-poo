class Chore:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status
    
    def __str__(self):
        return(f"""
    {self.title} = {self.description} - Status = {self.status}
              """)

class List_of_chores:
    def __init__(self):
        self.chores = []

    def add_chore(self, chore : Chore):
        self.chores.append(chore)

    def remove_chore(self, removal):
        for chore in self.chores:
            if chore == removal:
                self.chores.remove(chore)

    def mark_as_done(self, marked):
        for chore in self.chores:
            if marked == chore:
                chore.status = "done"
        
    def display_list(self):
        for chore in self.chores:
            print(chore.title)   

    def filter_list(self, status):
        for chore in self.chores:
            if status.lower() == chore.status:
                print(chore)


chore1 = Chore("Floors", "clean floors of the house", "ongoing")
chore2 = Chore("Trash", "take rubish out", "ongoing")
chore3 = Chore("Windows", "clean all windows", "ongoing")
chore4 = Chore("Food shopping", "go grocery shopping", "ongoing")
chore5 = Chore("Plan menus", "plan menus for the week", "ongoing")

Todolist = List_of_chores()
Todolist.add_chore(chore1)
Todolist.add_chore(chore4)
Todolist.add_chore(chore5)
# Todolist.display_list()

Todolist.remove_chore(chore1)
# Todolist.display_list()
Todolist.mark_as_done(chore4)
# print(str(chore4))


Todolist.display_list()

# Todolist.filter_list("ongoing")
Todolist.filter_list("DONE")