from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Hello World')
        self.change_message('From Eric', color='blue')

    def loop(self):
        # Set things up here to run repeatedly
        pass


# Start the simulator
MyUserApp().run()
