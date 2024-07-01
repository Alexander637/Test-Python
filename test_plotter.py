import unittest
from plotter import Plotter
import os


class TestPlotter(unittest.TestCase):
    def test_draw_plots(self):
        plotter_instance = Plotter('deviation.json')
        plot_paths = plotter_instance.draw_plots()
        self.assertTrue(len(plot_paths) > 0)
        for path in plot_paths:
            self.assertTrue(os.path.exists(path))


if __name__ == '__main__':
    unittest.main()
