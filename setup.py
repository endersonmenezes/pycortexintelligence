import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycortexintelligence",
    version="0.0.1",
    author="Enderson Menezes",
    author_email="endersonster@gmail.com",
    description="Cortex Intelligence Platform integration package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/endersonmenezes/pycortexintelligence",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)