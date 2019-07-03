from setuptools import setup, find_packages

setup(
    name='truffleHogRegexes',
    version='0.0.8',
    description='These regexes power truffleHog.',
    url='https://github.com/LewisLebentz/truffleHogRegexes',
    author='Dylan Ayrey',
    author_email='dylanayrey@gmail.com',
    license='GNU',
    packages = find_packages(),
    package_data={'': ['regexes.json']},
)
