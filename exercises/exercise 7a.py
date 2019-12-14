from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Show the value of the sliders in the message')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly
        sliders = self.get_slider_values()
        message = ''
        for i in range(self.NUMBER_OF_SLIDERS):
            message += 'Slider {}: {}  '.format(i + 1, sliders[i])
        self.change_message(message)


# Start the simulator
MyUserApp().run()
