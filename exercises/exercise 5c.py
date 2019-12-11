from exercises.simulator import GuiApp


class MyUserApp(GuiApp):
    ALL_LIGHTS = ['red', 'yellow', 'green', 'blue']

    def once(self):
        # Set things up here to run once
        pass

    def loop(self):
        # Set things up here to run repeatedly
        pass

    def pb_clicked(self, number):
        if self.get_light_state(self.ALL_LIGHTS[number - 1]) == 'off':
            self.set_light_state(self.ALL_LIGHTS[number - 1], 'on')
        else:
            self.set_light_state(self.ALL_LIGHTS[number - 1], 'off')


# Start the simulator
MyUserApp().run()
