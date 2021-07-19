import logging
from io import StringIO
from pathlib import Path

from .file_log_formatter import UncoloredFileLogFormatter
from .shell_log_formatter import ColoredShellLogFormatter


def setup_root_logger(shell_logging=True, file_logging=True, shell_log_lvl="info", file_log_lvl="debug",
                      logfile=Path('run.log')):

    logger = logging.getLogger()
    logging.root.setLevel(logging.NOTSET)

    if shell_logging:
        shell = logging.StreamHandler()
        shell.setLevel(shell_log_lvl.upper())
        color_dict = ColoredShellLogFormatter.shell_colors
        shell_format = ColoredShellLogFormatter(color_dict, '{message}', style='{')
        shell.setFormatter(shell_format)
        logger.addHandler(shell)

    if file_logging:
        logfile.parent.mkdir(parents=True, exist_ok=True)
        file = logging.FileHandler(logfile, mode='w')
        file.setLevel(file_log_lvl.upper())
        file_format = UncoloredFileLogFormatter('{asctime} - {process} - {name} - {levelname} - {message}', style='{')
        file.setFormatter(file_format)
        logger.addHandler(file)


def buffer_log():
    buffer = StringIO()
    logging.basicConfig(stream=buffer, level=logging.NOTSET)
    return buffer
