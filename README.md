# logging configurator
Logger for simultaneous file and shell logging

## installation

For installation with pip directly from this GitHub repository simply open a terminal and type
```
pip install git+ssh://git@github.com/rlipperts/logger.git
```
There are no PyPI releases. Neither are they planned.

## usage

Import the package and the default python logging
```python
import logging_configurator
import logging
```

Configure python logging
```python
logging_configurator.setup_root_logger()
```

Create a logging instance in your module as usual and log with it
```python
logger = logging.getLogger(__name__)
logger.info('Log Horizon')
```

### buffer initial output
If you need more complex argument parsing before you can configure the logger you can buffer it and have it logged once you configure your logger.

```python
initial_log = logging_configurator.buffer_log()
logger = logging.getLogger(__name__)
logger.info('Early log information')

# <your setup code goes here>

logging_configurator.setup_root_logger()
logger.debug(initial_log.getvalue())
```
The early log output currently can only be logged with one severity level.
