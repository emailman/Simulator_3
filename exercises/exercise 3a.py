from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Blink All Lights')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly
        light_state = self.get_light_state('red')
        if light_state == 'red':
            self.set_light_state('red', 'off')
            self.set_light_state('yellow', 'off')
            self.set_light_state('green', 'off')
            self.set_light_state('blue', 'off')
        else:
            self.set_light_state('red', 'on')
            self.set_light_state('yellow', 'on')
            self.set_light_state('green', 'on')
            self.set_light_state('blue', 'on')


# Start the simulator
MyUserApp().run()
