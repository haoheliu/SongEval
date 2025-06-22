from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="songeval",
    version="0.1.0",
    author="ASLP Lab",
    author_email="",
    description="A trained aesthetic evaluation toolkit for song quality assessment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ASLP-lab/SongEval",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "songeval": [
            "ckpt/*.safetensors",
            "config.yaml",
        ],
    },
    entry_points={
        "console_scripts": [
            "songeval=songeval.cli:main",
        ],
    },
) 