from setuptools import setup


VERSION = "0.1.1"

setup(
    name='Xlsxcursor',
    description="Xlsxcursor for xlsxwriter.",
    version=VERSION,
    packages=['xlsxcursor'],
    install_requires=[
        'xlsxwriter',
    ],
)
