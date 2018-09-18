from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DisplayNames(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Brandon", "Taleisha", "Caleb", "Scarlett", "Hunter"]

    def build(self):
        self.title = "All Names"
        self.root = Builder.load_file("display_names.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Button(text=name)
            self.root.ids.entries_box.add_widget(temp_label)

DisplayNames().run()
