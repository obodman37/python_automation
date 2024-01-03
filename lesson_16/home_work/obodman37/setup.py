import setuptools

with open('README.TXT', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='obodman37',
    version='0.0.1',
    author='Oleksandr Obodovskyi',
    description='ObodmaN Wheel Package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Windows :: Linux"
    ]
)
