from exercises.simulator import GuiApp


class MyUserApp(GuiApp):
    ALL_LIGHTS = ['red', 'yellow', 'green', 'blue']

    def once(self):
        # Set things up here to run once
        self.change_title('Blink All Lights - Version 2')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly
        for light in self.ALL_LIGHTS:
            light_state = self.get_light_state(light)
            if light_state == 'on':
                self.set_light_state(light, 'off')
            else:
                self.set_light_state(light, 'on')


# Start the simulator
MyUserApp().run()
