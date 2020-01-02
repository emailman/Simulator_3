from exercises.simulator import GuiApp
from math import pi


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Enter the radius of a circle, push any button to calculate the area')
        self.change_message('By Eric')
        self.change_prompt_1('Enter radius of circle')

    def loop(self):
        # Set things up here to run repeatedly
        pass

    def pb_clicked(self, number):
        radius = float(self.get_text_entry_1())
        area = pi * radius ** 2
        self.change_message('Area of the circle = ' + str(round(area, 2)))


# Start the simulator
MyUserApp().run()
