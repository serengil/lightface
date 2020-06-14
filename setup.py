import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lightface",  
    version="0.0.1",
    author="Sefik Ilkin Serengil",
    author_email="serengil@gmail.com",
    description="A lightweight deep face recognition framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/serengil/lightface",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5.5',
    install_requires=["numpy>=1.14.0", "pandas>=0.23.4"]
)
