from setuptools import setup

setup(
    name="iadmodels",
    version='0.0.1',
    packages=['iadmodels'],
    package_dir={
        "iadmodels": "src/iadmodels",
    },
    package_data={
        "iadmodels": ["data/*.txt"]
    },
    install_requires=[
        'numpy',
    ]
)
