import guizero
from abc import ABC, abstractmethod


class GuiApp(ABC):
    # Global constants
    WIDTH = 1050
    HEIGHT = 820

    LIGHTS = {'red': (0, 0), 'yellow': (0, 1), 'green': (0, 2), 'blue': (0, 3)}
    COLOR_LIST = list(LIGHTS.keys())
    NUMBER_OF_LIGHTS = NUMBER_OF_BUTTONS = len(LIGHTS)
    DARK_LIGHT_COLOR = 'grey'

    SLIDERS = {'red': 0, 'green': 1, 'blue': 2}
    NUMBER_OF_SLIDERS = len(SLIDERS)
    SLIDER_MIN = 0
    SLIDER_MAX = 100

    LOOP_DELAY = 1000  # milliseconds

    # Global variables
    # light_on = [True] * NUMBER_OF_LIGHTS
    picture_state = 'sun'
    sld_list = []

    def __init__(self):
        super().__init__()

        # Setup app
        self.app = guizero.App(title='ITN160 Simulator', bg='tan',
                               width=self.WIDTH, height=self.HEIGHT)
        self.app.text_size = 16

        guizero.Text(self.app, size=8)

        self.txt_title = guizero.Text(self.app, size=20,
                                      text='Your Title Here')
        guizero.Text(self.app, size=8)

        self.txt_message = guizero.Text(self.app, size=18,
                                        text='Your Message Here')
        guizero.Text(self.app, size=8)

        guizero.Box(self.app, width=50, height=50, align='left')  # Spacer

        # Build and populate a box for the waffle for the lights
        box_lights = guizero.Box(self.app, border=1, align='left',
                                 width=240, height=self.HEIGHT - 150)
        self.waf_lights = guizero.Waffle(box_lights, height=self.NUMBER_OF_LIGHTS,
                                         width=1, dim=80, pad=63, dotty=True)

        # Set the lights to the 'off' color
        for color in self.LIGHTS:
            self.waf_lights[self.LIGHTS[color]].color = self.DARK_LIGHT_COLOR

        # Build and populate a box for the push buttons
        box_pbs = guizero.Box(self.app, border=1, align='left',
                              width=200, height=self.HEIGHT - 150)

        pb_list = []
        for i in range(self.NUMBER_OF_BUTTONS):
            guizero.Text(box_pbs, size=44)
            pb_list.append(guizero.PushButton(box_pbs,
                                              text='Button ' + str(i + 1),
                                              command=self.pb_clicked,
                                              args=[i + 1]))

        # Build and populate a box for the sliders
        box_sliders = guizero.Box(self.app, border=1, align='left',
                                  width=300, height=self.HEIGHT - 150)

        for i in range(self.NUMBER_OF_SLIDERS):
            self.sld_list.append(guizero.Slider(box_sliders, height='fill', width=10,
                                                start=self.SLIDER_MAX, end=self.SLIDER_MIN,
                                                horizontal=False, align='left', command=None))
            guizero.Text(box_sliders, text='S\nl\ni\nd\ne\nr\n\n' + str(i + 1),
                         width=2, align='left')

        for i, slider_color in enumerate(self.SLIDERS.keys()):
            self.sld_list[i].text_color = slider_color

        # Build and populate a box for misc widgets
        box_misc = guizero.Box(self.app, border=1, align='left',
                               width=200, height=self.HEIGHT - 150)

        self.circle = guizero.Waffle(box_misc, height=1, width=1, dim=100,
                                     dotty=True, color='black', pad=50)

        self.pb_picture = guizero.PushButton(box_misc, image='./pictures/sun.gif',
                                             height=90, width=90,
                                             command=self.change_picture_state)
        guizero.Box(box_misc, height=50, width=75)

        self.txt_prompt_1 = guizero.Text(box_misc, text='Prompt 1:')
        self.tbx_entry_1 = guizero.TextBox(box_misc, width=16)
        guizero.Box(box_misc, height=30, width=75)

        self.txt_prompt_2 = guizero.Text(box_misc, text='Prompt 2:')
        self.tbx_entry_2 = guizero.TextBox(box_misc, width=16)
        guizero.Box(box_misc, height=30, width=75)

        guizero.PushButton(box_misc, text='QUIT', command=quit)

    # Required user functions
    @abstractmethod
    def once(self):
        pass

    @abstractmethod
    def loop(self):
        pass

    # Optional user functions
    def pb_clicked(self, number):
        pass

    def change_title(self, new_title, color='black'):
        self.txt_title.value = new_title
        self.txt_title.text_color = color

    def change_message(self, new_message, color='black'):
        self.txt_message.value = new_message
        self.txt_message.text_color = color

    def change_prompt_1(self, new_prompt, color='black'):
        self.txt_prompt_1.value = new_prompt
        self.txt_prompt_1.text_color = color

    def change_prompt_2(self, new_prompt, color='black'):
        self.txt_prompt_2.value = new_prompt
        self.txt_prompt_2.text_color = color

    def change_picture_state(self):
        if self.picture_state == 'sun':
            self.pb_picture.image = './pictures/moon.gif'
            self.picture_state = 'moon'
        else:
            self.pb_picture.image = './pictures/sun.gif'
            self.picture_state = 'sun'

    def get_picture_state(self):
        return self.picture_state

    def set_light_state(self, light, state):
        if light in self.LIGHTS:
            if state == 'on':
                self.waf_lights[self.LIGHTS[light]].color = light
            elif state == 'off':
                self.waf_lights[self.LIGHTS[light]].color = self.DARK_LIGHT_COLOR
            else:
                guizero.error(title='Simulator Error',
                              text='Invalid State-' + state)
        else:
            guizero.error(title='Simulator Error',
                          text='Invalid Light-' + light)

    def get_light_state(self, light):
        if light in self.LIGHTS:
            if self.waf_lights[self.LIGHTS[light]].color == light:
                return 'on'
            else:
                return 'off'

        else:
            guizero.error(title='Simulator Error', text='Invalid Light-' + light)
            return None

    def get_text_entry_1(self):
        return self.tbx_entry_1.value

    def get_text_entry_2(self):
        return self.tbx_entry_2.value

    def get_slider_values(self):
        slider_values = []
        for slider in self.sld_list:
            slider_values.append(slider.value)
        return slider_values

    def get_slider_value(self, slider):
        if slider in self.SLIDERS:
            slider_value = self.sld_list[self.SLIDERS[slider]].value
            return slider_value
        else:
            guizero.error(title='Simulator Error', text='Invalid Slider-' + slider)

    def set_slider_value(self, slider, slider_value):
        if slider in self.SLIDERS:
            if isinstance(slider_value, int) or isinstance(slider_value, float):
                if self.SLIDER_MIN <= slider_value <= self.SLIDER_MAX:
                    self.sld_list[self.SLIDERS[slider]].value = slider_value
                else:
                    guizero.error(title='Simulator Error', text='Invalid Slider Value: ' +
                                                                str(slider_value))
            else:
                guizero.error(title='Simulator Error', text='Invalid Slider Value: ' +
                                                            str(slider_value))
        else:
            guizero.error(title='Simulator Error', text='Invalid Slider-' + slider)

    def set_circle_color(self, red, green, blue):
        self.circle.set_pixel(0, 0, (red, green, blue))

    def get_circle_color(self):
        circle_color = self.circle.get_pixel(0, 0)
        red = int(circle_color[1:3], 16)
        green = int(circle_color[3:5], 16)
        blue = int(circle_color[5:7], 16)
        return red, green, blue

    def run(self):
        self.once()

        self.app.repeat(self.LOOP_DELAY, self.loop)

        self.app.display()
