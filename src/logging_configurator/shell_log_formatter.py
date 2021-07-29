# Log formatter that prints colored to shell but uncolored to file
import logging


class ColoredShellLogFormatter(logging.Formatter):
    shell_colors = {
        "NONE": '\033[0m',
        "DEBUG": '\033[0m',
        "INFO": '\033[0m',
        "HIGHLIGHT": '\033[36m',
        "WARNING": '\033[33m',
        "ERROR": '\033[31m',
    }

    def __init__(self, colors, fmt, style='%'):
        super().__init__(fmt=fmt, style=style)
        """ colors is a dict { loglevel : shell_color } """
        self.formatters = {}
        self.default_formatter = logging.Formatter(
            "Requested Formatter not found! - {module}: {message}", style=style)
        for loglevel in colors:
            self.formatters[loglevel] = logging.Formatter(
                ColoredShellLogFormatter.colorize(fmt, colors[loglevel]), style=style)

    def format(self, record):
        formatter = self.formatters.get(record.levelname, self.default_formatter)
        return formatter.format(record)

    @staticmethod
    def colorize(text, color_name):
        return color_name + text + ColoredShellLogFormatter.shell_colors['NONE']
