
class Place:
    def __init__(self,name,country,priority,is_visit):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visit = is_visit

    def __str__(self):
        if self.is_visit:
            status='v'
        else:
            status='n'
        return "{0} {1} {2} {3}".format(self.name,self.country,self.priority,status)


    def visited(self):
        self.is_visit= True

    def unvisit(self):
        self.is_visit= False