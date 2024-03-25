from setuptools import setup, find_packages

setup(
    name="Higher", 
    version="0.1.0",
    author="Your Name",
    author_email="s.k.oni0894@gmail.com",
    description="A simple task for Advanced Software Engineer",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SanjidaKohinurOni/ASE/edit/main/HigherStudy",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
