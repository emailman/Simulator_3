from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Show a light corresponding to a simulated temperature')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly

        # Red slider simulates temperature
        temperature = self.get_slider_value('red')
        self.change_message('Temperature = ' + str(temperature))
        if temperature < 50:
            self.set_light_state('blue', 'on')
            self.set_light_state('red', 'off')
        else:
            self.set_light_state('blue', 'off')
            self.set_light_state('red', 'on')


# Start the simulator
MyUserApp().run()
