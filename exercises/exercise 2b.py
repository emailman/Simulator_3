from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Blink Red Light')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly
        light_state = self.get_light_state('red')
        if light_state == 'on':
            self.set_light_state('red', 'off')
        else:
            self.set_light_state('red', 'on')


# Start the simulator
MyUserApp().run()
