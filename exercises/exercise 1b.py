from exercises.simulator import GuiApp


class MyUserApp(GuiApp):

    def once(self):
        # Set things up here to run once
        self.change_title('Hello World')

    def loop(self):
        # Set things up here to run repeatedly
        pass

    def pb_clicked(self, number):
        your_name = self.get_text_entry()
        self.change_message('Welcome ' + your_name)


# Start the simulator
MyUserApp().run()
