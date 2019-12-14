from exercises.simulator import GuiApp
from math import pi


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Enter the radius of a circle, push any button to calculate the area')
        self.change_message('By Eric')
        self.change_prompt('Enter radius of circle')

    def loop(self):
        # Set things up here to run repeatedly
        pass

    def pb_clicked(self, number):
        if self.get_text_entry():
            try:
                radius = float(self.get_text_entry())
                if radius >= 0:
                    area = pi * radius ** 2
                    self.change_message('The area of a circle with radius {} = {}'.
                                        format(radius, round(area, 2)))
                else:
                    self.change_message('Entry must be greater or equal to 0', 'red')
            except ValueError:
                self.change_message('Entry must be numeric', 'red')
        else:
            self.change_message('No data entered', 'red')


# Start the simulator
MyUserApp().run()
