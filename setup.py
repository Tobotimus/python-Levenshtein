from setuptools import setup
from distutils.core import Extension


setup(
    ext_modules=[
        Extension(
            "Levenshtein._levenshtein",
            sources=["Levenshtein/_levenshtein.c"],
        )
    ]
)
