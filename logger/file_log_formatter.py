# Log formatter that prints colored to shell but uncolored to file
import logging
import re


class UncoloredFileLogFormatter(logging.Formatter):

    ansi_re = re.compile(r'\x1b\[[0-9;]*m')

    def format(self, record):
        s = super(UncoloredFileLogFormatter, self).format(record)
        return re.sub(UncoloredFileLogFormatter.ansi_re, '', s)
