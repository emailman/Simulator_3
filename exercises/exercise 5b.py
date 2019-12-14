from exercises.simulator import GuiApp


class MyUserApp(GuiApp):
    ALL_LIGHTS = ['red', 'yellow', 'green', 'blue']

    def once(self):
        # Set things up here to run once
        self.change_title('Turn on the light corresponding to the button clicked')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly
        pass

    def pb_clicked(self, number):
        self.change_message('Button ' + str(number) + ' was clicked')
        self.set_light_state(self.ALL_LIGHTS[number - 1], 'on')


# Start the simulator
MyUserApp().run()
