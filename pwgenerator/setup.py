from setuptools import setup

setup(
    name= "pwgenerator",
    version= "0.1",
    description= "Password generator with the desired number of characters",
    author= "Noname",
    author_email= "noname@xyz.com",
    packages= ["pwgenerator"],
    # requires =  Only the python builtin function i.e. String, and random is used. So no need to add additional pacakges.
)