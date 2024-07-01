from plotter import Plotter


def main():
    json_file = 'deviation.json'
    plotter_instance = Plotter(json_file)
    plot_paths = plotter_instance.draw_plots()

    for path in plot_paths:
        print(path)


if __name__ == "__main__":
    main()
