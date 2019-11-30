from exercises.simulator import GuiApp


class MyUserApp(GuiApp):
    ALL_LIGHTS = ['red', 'yellow', 'green', 'blue']

    def once(self):
        # Set things up here to run once
        self.change_title('Blink All Lights - Version 3')
        self.change_message('By Eric')

        self.set_light_color(self.ALL_LIGHTS[1], 'on')
        self.set_light_color(self.ALL_LIGHTS[3], 'on')

    def loop(self):
        # Set things up here to run repeatedly

        for light in self.ALL_LIGHTS:
            light_color = self.get_light_color(light)
            if light_color == light:
                self.set_light_color(light, 'off')
            else:
                self.set_light_color(light, 'on')


# Start the simulator
MyUserApp().run()
