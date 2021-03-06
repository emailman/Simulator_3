from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Set the color of the circle based on 3 slider values')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly
        sliders = self.get_slider_values()
        red = int(sliders[0] * 2.55)
        green = int(sliders[1] * 2.55)
        blue = int(sliders[2] * 2.55)
        self.set_circle_color(red, green, blue)


# Start the simulator
MyUserApp().run()
