from exercises.simulator import GuiApp


class MyUserApp(GuiApp):
    counter = -10

    def once(self):
        # Set things up here to run once
        self.change_title('Mission to Mars')
        self.change_message('Begin Countdown')

    def loop(self):
        # Set things up here to run repeatedly
        if self.counter > 0:
            self.change_message('T: +{:3d}'.format(self.counter))
        elif self.counter < 0:
            self.change_message('T: -{:3d}'.format(abs(self.counter)))
        else:
            self.change_message('LIFTOFF')
            self.set_light_color('red', 'on')

        if self.counter == 10:
            self.change_message('First Stage Cutoff')
            self.set_light_color('red', 'off')

        elif self.counter == 11:
            self.change_message('Second Stage Ignition')
            self.set_light_color('yellow', 'on')

        elif self.counter == 20:
            self.change_message('Second Stage Cutoff')
            self.set_light_color('yellow', 'off')

        elif self.counter == 21:
            self.change_message('Third Stage Ignition')
            self.set_light_color('green', 'on')

        elif self.counter == 30:
            self.change_message('Third Stage Cutoff')
            self.set_light_color('green', 'off')

        elif self.counter == 31:
            self.change_title('On the Way to Mars')
            self.set_light_color('blue', 'on')

        self.counter += 1


# Start the simulator
MyUserApp().run()
