from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Flip the Picture')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly
        self.change_picture()


# Start the simulator
MyUserApp().run()
