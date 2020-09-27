
from place import Place


class PlaceCollection:
    def __init__(self):

        self.places = []

    def get_place(self,name):
        for place in self.places:
            if place[0].name==name:
                return place[0]



    def load_places(self):
        loadfile=open('place.csv','r')

        for place in loadfile:
            place_string = place.split(",")
            self.places.append([Place(place_string[0], place_string[1], int(place_string[2]), place_string[3].strip())])

        loadfile.close()


    def visited_place(self):
        visited_place = 0
        for place in self.places:
            if place[0].is_visit=='v':
                visited_place +=1
        return visited_place

    def unvisit_place(self):
        unvisit_place = 0
        for place in self.places:
            if place[0].is_visit=='n':
                unvisit_place +=1
        return unvisit_place


    def add_place(self,name,country,priority,):
        self.places.append(Place(name,country,priority,'n'))

    def save_places(self):
        writer=open('places.csv','w')
        for place in self.places:
            writer.write(place[0].name+","+place[0].country + "," + str(place[0].priority) + ","+place[0].is_visit+"\n")
            writer.close()

    def sort(self,sort_place):
        if sort_place == "Name":
            self.places.sort(key=lambda i: i[0].name)
        elif sort_place == "Country":
            self.places.sort(key=lambda i: (i[0].country, i[0].name))

        elif sort_place == "Priority":
            self.places.sort(key=lambda i: (i[0].priority, i[0].name))
        else:
            self.places.sort(key=lambda i: (i[0].is_visit, i[0].name))
