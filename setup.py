from setuptools import setup

setup(
    name='images2gif',
    version='0.1',
    description='Provides functionality for reading and writing animated GIF images.',
    long_description="Use writeGif to write a series of numpy arrays or PIL images as an animated GIF. Use readGif to read an animated gif as a series of numpy arrays.",
    author="Almar Klein",
    author_email='almar.klein',
    url='https://github.com/therumpusroom/images2gif',
    packages=['images2gif'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        "License :: OSI Approved :: BSD License",
        'Programming Language :: Python :: 2.7',
    ],
)