from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Change message to the button clicked')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly
        pass

    def pb_clicked(self, number):
        self.change_message('Button ' + str(number) + ' was clicked')


# Start the simulator
MyUserApp().run()
