from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class MilesToKm(App):

    def build(self):
        Window.size = (400, 200)
        self.title = "Miles to km Converter"
        self.root = Builder.load_file("my_miles_to_km.kv")
        return self.root

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKm().run()
