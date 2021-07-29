import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

test_deps = [
    'pytest',
    'flake8',
    'pylint',
    'mypy',
]
extras = {
    'test': test_deps
}

setuptools.setup(
    name="logging-configurator",
    version="0.0.2",
    author="Ruben Lipperts",
    author_email="",
    description="Simple logger configuration for simultaneous file and shell logging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rlipperts/logger",
    package_dir={'': 'src'},
    packages=['logging_configurator'],
    package_data={'logging_configurator': ['py.typed']},
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Logging",
    ],
    python_requires='~=3.9',
)
