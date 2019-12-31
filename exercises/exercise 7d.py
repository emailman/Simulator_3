from exercises.simulator import GuiApp


class MyUserApp(GuiApp):
    slider = 'green'
    slider_value = 0
    slider_direction = 'up'

    def once(self):
        # Set things up here to run once
        self.change_title('Move the green slider between 40 and 60')
        self.change_message('By Eric')

    def loop(self):
        # Set things up here to run repeatedly
        if self.slider_direction == 'up':
            if self.slider_value == 0:
                self.slider_value = 39
            self.slider_value += 1
            if self.slider_value > 60:
                self.slider_value = 59
                self.slider_direction = 'down'
        else:
            self.slider_value -= 1
            if self.slider_value < 40:
                self.slider_value = 41
                self.slider_direction = 'up'

        self.set_slider_value(self.slider, self.slider_value)


# Start the simulator
MyUserApp().run()
