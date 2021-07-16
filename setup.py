import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loggin-configurator",
    version="0.0.2",
    author="Ruben Lipperts",
    author_email="",
    description="Simple logger configuration for simultaneous file and shell logging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rlipperts/logger",
    packages=setuptools.find_packages(include='logging_configurator'),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Benchmark",
    ],
    python_requires='~=3.9',
)
