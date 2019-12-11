from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        pass

    def loop(self):
        # Set things up here to run repeatedly
        sliders = self.get_slider_values()
        temperature = sliders[0]
        self.change_message('Temperature = ' + str(temperature))
        if 0 <= temperature < 32:
            self.set_light_state('blue', 'on')
            self.set_light_state('yellow', 'off')
            self.set_light_state('red', 'off')
        elif 32 <= temperature < 75:
            self.set_light_state('blue', 'off')
            self.set_light_state('yellow', 'on')
            self.set_light_state('red', 'off')
        else:
            self.set_light_state('blue', 'off')
            self.set_light_state('yellow', 'off')
            self.set_light_state('red', 'on')


# Start the simulator
MyUserApp().run()
