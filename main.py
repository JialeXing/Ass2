"""
Name:Jiale Xing
Date:24/09/2020
Brief Project Description:
GitHub URL:
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from placecollection import PlaceCollection

class TravelTrackerApp(App):
    """..."""
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.list_place = PlaceCollection()


        self.top_label = Label(text="", id="count_label")
        self.status_label = Label(text="")
        self.sort_label = Label(text="Sort by:")


        self.spinner = Spinner(text='Name', values=('Name', 'Country', 'Priority', 'Visited'))
        self.add_label = Label(text="Add New Place...")
        self.name_label = Label(text="Country:")
        self.name_input = TextInput(write_tab=False, multiline=False)
        self.country_label = Label(text="Name:")
        self.country_input = TextInput(write_tab=False, multiline=False)
        self.priority_label = Label(text="Priority:")
        self.priority_input = TextInput(write_tab=False, multiline=False)


    def right_side(self):
        self. top_label.text="Visited: "+ str(self.list_place.visited_place())+". Unvisit: "+str(self.list_place.unvisit_place())

        for place in self.list_place.places:
            if place[0].is_visit == 'n':
                place_button = Button(text='' + place[0].name + ' ' + "in" + ' ' + place[0].country + ', ' + "priority" + ' ' + str(place[0].priority), id=place[0].name)
                place_button.background_color = [0, 88, 88, 0.4]
            else:
                place_button = Button(
                    text='' + place[0].name + ' ' + " in " + ' ' + place[0].country + ', ' + "priority" + ' '+ str(place[0].priority)+ ' '+ "(visited)", id=place[0].name)
                place_button.background_color = [88, 89, 0, 0.4]

            place_button.bind(on_release=self.click)
            self.root.ids.rightLayout.add_widget(place_button)

    def click(self,button):
        if self.list_place.get_place(button.id).status == 'v':
            self.list_place.get_place(button.id).status = 'n'
            self.root.ids.bottomLayout.text = "You need to visit " + str(self.list_place.get_place(button.id).name)
        else:
            self.list_place.get_place(button.id).status = 'v'
            self.root.ids.bottomLayout.text = "You have visited " + str(self.list_place.get_place(button.id).name)
        self.sort()
        self.root.ids.rightLayout.clear_widgets()
        self.right_side()

    def sort(self,*args):
        self.list_place.sort(self.spinner.text)
        self.root.ids.rightLayout.clear_widgets()
        self.right_side()

    def build(self):
        """
            This function is used to open the kivy app and put some object
        """
        self.title = "TravelTracker"
        self.root = Builder.load_file('app.kv')
        self.list_place.load_places()
        self.list_place.sort('Name')
        self.left_side()
        self.right_side()

    def left_side(self):

        self.add_button = Button(text='Add Place')
        self.clear_button = Button(text='Clear')

        self.root.ids.leftLayout.add_widget(self.sort_label)
        self.root.ids.leftLayout.add_widget(self.spinner)
        self.root.ids.leftLayout.add_widget(self.add_label)
        self.root.ids.leftLayout.add_widget(self.name_label)
        self.root.ids.leftLayout.add_widget(self.name_input)
        self.root.ids.leftLayout.add_widget(self.country_label)
        self.root.ids.leftLayout.add_widget(self.country_input)
        self.root.ids.leftLayout.add_widget(self.priority_label)
        self.root.ids.leftLayout.add_widget(self.priority_input)
        self.root.ids.leftLayout.add_widget(self.add_button)
        self.root.ids.leftLayout.add_widget(self.clear_button)
        self.root.ids.leftLayout.add_widget(self.top_label)

        self.spinner.bind(text=self.sort)
        self.add_button.bind(on_release=self.add_place)
        self.clear_button.bind(on_release=self.clear_input)

    def add_place(self,*args):
        if str(self.name_input.text).strip() == '' or str(self.country_input.text).strip() == '' or str(self.priority_input.text).strip() == '':
            self.root.ids.bottomLayout.text = "All fields must be completed"
        else:
            try:

                if int(self.priority_input.text) < 0:
                    self.root.ids.bottomLayout.text = "Please enter a valid number"

                else:
                    self.list_place.add_place(self.name_input.text, self.country_input.text, int(self.priority_input.text))
                    self.list_place.sort(self.spinner.text)
                    self.clear_input()
                    self.root.ids.rightLayout.clear_widgets()
                    self.right_side()
            # Print the error message when it is string error
            except ValueError:
                self.root.ids.bottomLayout.text = "Please enter a valid number"

    def clear_input(self,*args):
        self.name_input.text = ""
        self.country_input.text = ""
        self.priority_input.text = ""
        self.root.ids.bottomLayout.text = ""

    def save_files(self):
        self.list_place.save_places()




if __name__ == '__main__':
    TravelTrackerApp().run()