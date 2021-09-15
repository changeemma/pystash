from setuptools import setup

setup(
    name="pystash",
    version="0.1.0",
    py_modules=["pystash"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "pystash = pystash.cli:cli",
        ],
    },
)
