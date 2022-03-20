import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reg2info",
    version="1.0.0",
    author="Mohamed Abidi",
    author_email="abidi.contact@gmail.com",
    description="An awesome package that allows getting meaningful information from a Linear regression model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohamedabidi97/reg2info.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),   
)