from setuptools import setup

setup(
    name="metcon",
    version="0.0.1.dev1",
    description="Configuration tool for configuration files",
    author="Renat Zhilkibaev",
    author_email="rzhilkibaev@gmail.com",
    license="MIT",
    url="https://github.com/rzhilkibaev/metaconfig",
    packages=["metaconfig"],
    install_requires=["docopt", "future", "jinja2"],
    entry_points={"console_scripts": ["metaconfig=metaconfig.metaconfig:main"]},
)
