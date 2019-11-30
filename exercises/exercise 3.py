from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Blink All Lights')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly
        light_color = self.get_light_color('red')
        if light_color == 'red':
            self.set_light_color('red', 'off')
            self.set_light_color('yellow', 'off')
            self.set_light_color('green', 'off')
            self.set_light_color('blue', 'off')
        else:
            self.set_light_color('red', 'on')
            self.set_light_color('yellow', 'on')
            self.set_light_color('green', 'on')
            self.set_light_color('blue', 'on')


# Start the simulator
MyUserApp().run()
