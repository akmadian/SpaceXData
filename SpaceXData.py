from bokeh.plotting import figure, output_file, show
from bokeh.models import LinearAxis, Range1d
import ast

from os import path
from sys import argv

base_path = path.os.path.dirname(path.realpath(argv[0]))


class Launch:

    def __init__(self, launch_name):
        self.data_time = []
        self.data_velocity = []
        self.data_altitude = []
        self.load_data(launch_name)

    def load_data(self, launch_name):
        data_path = base_path + '/Launch-Data/' + launch_name + '.txt'
        with open(data_path, 'r') as data_file:
            for line in data_file.readlines():
                line_data = ast.literal_eval(str(line))
                for title, value in line_data.items():
                    if title == 'time':
                        self.data_time.append(value)
                    elif title == 'velocity':
                        self.data_velocity.append(value)
                    else:
                        self.data_altitude.append(value)

    def generate_graph(self):
        p = figure(plot_width=800, plot_height=500, y_range=(0, 150))
        p.line(self.data_time, self.data_altitude, line_width=2)
        p.extra_y_ranges = {'Velocity': Range1d(start=0, end=1800)}
        p.line(self.data_time, self.data_velocity, y_range_name='Velocity')
        p.add_layout(LinearAxis(y_range_name='Velocity'), 'right')
        show(p)

L = Launch('CRS-12')
print(L.data_time)
print(L.data_velocity)
print(L.data_altitude)
L.generate_graph()