from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Show the light matching the picture')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly
        state = self.get_picture_state()
        if state == 'sun':
            self.set_light_state('yellow', 'on')
            self.set_light_state('blue', 'off')
        else:
            self.set_light_state('yellow', 'off')
            self.set_light_state('blue', 'on')


# Start the simulator
MyUserApp().run()
