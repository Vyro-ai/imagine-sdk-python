from setuptools import setup
from setuptools import find_packages

setup(
    name="imaginesdk",
    version="1.0.0-beta02",
    description="Python client library for the Imagine API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Vyro-ai/imagine-sdk-python",
    author="Vyro",
    author_email="api.imagine@vyro.ai",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.6",
    extras_require={
        "embeddings": [
            "numpy",
            "Pillow",
            "requests",
        ]
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
)
