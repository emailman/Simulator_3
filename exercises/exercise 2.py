from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Blink Red Light')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly
        light_color = self.get_light_color('red')
        if light_color == 'red':
            self.set_light_color('red', 'off')
        else:
            self.set_light_color('red', 'on')


# Start the simulator
MyUserApp().run()
