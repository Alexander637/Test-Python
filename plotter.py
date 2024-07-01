import pandas as pd
import matplotlib.pyplot as plt
import os


class Plotter:
    def __init__(self, json_file):
        self.data = pd.read_json(json_file)

    def draw_plots(self):
        plots_dir = 'plots'
        if not os.path.exists(plots_dir):
            os.makedirs(plots_dir)

        plots_paths = []

        for column in self.data.columns:
            if column not in ['name', 'gt_corners', 'rb_corners']:
                plt.figure()
                plt.plot(self.data['name'], self.data[column], label=column)
                plt.xlabel('Room Name')
                plt.ylabel('Deviation in Degrees')
                plt.title(f'Deviation of {column}')
                plt.legend()
                plot_path = os.path.join(plots_dir, f'{column}.png')
                plt.savefig(plot_path)
                plt.close()
                plots_paths.append(plot_path)

        return plots_paths
