from setuptools import setup, find_packages

setup(
    name="task-turbo-gtd-20260529_201105",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'task=task:main',
        ],
    },
)
