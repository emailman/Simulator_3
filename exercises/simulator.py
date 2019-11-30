import guizero
from abc import ABC, abstractmethod


class GuiApp(ABC):
    # Global constants
    WIDTH = 1050
    HEIGHT = 820
    LIGHTS = {'red': (0, 0), 'yellow': (0, 1), 'green': (0, 2), 'blue': (0, 3)}
    COLOR_LIST = list(LIGHTS.keys())
    NUMBER_OF_LIGHTS = NUMBER_OF_BUTTONS = len(LIGHTS)
    DARK_COLOR = 'grey'
    NUMBER_OF_SLIDERS = 3
    SLIDER_COLORS = ('red', 'green', 'blue')
    SLIDER_MIN = 0
    SLIDER_MAX = 100

    LOOP_DELAY = 1000  # milliseconds

    # Global variables
    # lights_on = True
    # light_on = [True] * NUMBER_OF_LIGHTS
    picture_toggle = True

    def __init__(self):
        super().__init__()

        # Setup app
        self.app = guizero.App(title='ITN160 Simulator', bg='tan',
                               width=self.WIDTH, height=self.HEIGHT)
        self.app.text_size = 16

        guizero.Text(self.app, size=8)

        self.txt_header = guizero.Text(self.app, size=20,
                                       text='Your Header Here')
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
            self.waf_lights[self.LIGHTS[color]].color = self.DARK_COLOR

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
        sld_list = []
        for i in range(self.NUMBER_OF_SLIDERS):
            sld_list.append(guizero.Slider(box_sliders, height='fill', width=10,
                                           start=self.SLIDER_MAX,
                                           end=self.SLIDER_MIN,
                                           horizontal=False, align='left',
                                           command=None))
            guizero.Text(box_sliders, text='S\nl\ni\nd\ne\nr\n\n' + str(i + 1),
                         width=2, align='left')

        for i in range(self.NUMBER_OF_SLIDERS):
            sld_list[i].text_color = self.SLIDER_COLORS[i]

        # Build and populate a box for misc widgets
        box_misc = guizero.Box(self.app, border=1, align='left',
                               width=200, height=self.HEIGHT - 150)

        guizero.Waffle(box_misc, height=1, width=1, dim=100,
                       dotty=True, color='black', pad=50)

        self.pb_picture = guizero.PushButton(box_misc, image='./pictures/sun.png',
                                             height=90, width=90,
                                             command=self.change_picture)
        guizero.Box(box_misc, height=100, width=100)
        guizero.PushButton(box_misc, text='QUIT', command=quit)

    @abstractmethod
    def once(self):
        pass

    @abstractmethod
    def loop(self):
        pass

    def pb_clicked(self, number):
        pass

    def change_title(self, new_header, color='black'):
        self.txt_header.value = new_header
        self.txt_header.text_color = color

    def change_message(self, new_message, color='black'):
        self.txt_message.value = new_message
        self.txt_message.text_color = color

    def change_picture(self):
        if self.picture_toggle:
            self.pb_picture.image = './pictures/moon.png'
            self.picture_toggle = False
        else:
            self.pb_picture.image = './pictures/sun.png'
            self.picture_toggle = True

    def set_light_color(self, light, state):
        if light in self.LIGHTS:
            if state == 'on':
                self.waf_lights[self.LIGHTS[light]].color = light
            elif state == 'off':
                self.waf_lights[self.LIGHTS[light]].color = self.DARK_COLOR
            else:
                guizero.error(title='Simulator Error',
                              text='Invalid State-' + state)
        else:
            guizero.error(title='Simulator Error',
                          text='Invalid Light-' + light)

    def get_light_color(self, light):
        if light in self.LIGHTS:
            return self.waf_lights[self.LIGHTS[light]].color

        else:
            guizero.error(title='Simulator Error', text='Invalid Light-' + light)
            return None

    def run(self):
        self.once()

        self.app.repeat(self.LOOP_DELAY, self.loop)

        self.app.display()
