from setuptools import setup, find_packages

setup(
    name="wotd-jps",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
    entry_points={
        "console_scripts": [
            "wotd-jps=wotd.main:main_function",
        ],
    },
)
