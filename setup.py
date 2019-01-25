from setuptools import setup

setup(
    name= 'cliExample',
    version = '0.1.0',
    packages = ['cliExample'],
    entry_points = {
        'console_scripts': [
            'cliExample = cliExample.__main__:executeMe'
        ]
    },
    install_requires = ['click']
)