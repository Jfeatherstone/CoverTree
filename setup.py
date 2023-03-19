import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='covertree',  
     version='1.0.0',
     author="Jack Featherstone",
     author_email="jack.featherstone@oist.jp",
     license='New BSD License',
     url='https://github.com/Jfeatherstone/CoverTree',
     description="Cover tree implementation for computing nearest neighbors in general metric spaces.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3.7",
         "Operating System :: OS Independent",
     ],
 )
