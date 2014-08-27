from distutils.core import setup

setup(
    name='ConsoleTable',
    version='0.1.0',
    author='Aaron O. Ellis',
    author_email='aaronoellis@gmail.com',
    packages=['consoletable', 'consoletable.test'],
    scripts=[],
    url='https://github.com/aodin/ConsoleTable',
    license='LICENSE.txt',
    description='Pretty print tabular data to console.',
    long_description=open('README.txt').read(),
    install_requires=[
        "pytest"
    ],
)