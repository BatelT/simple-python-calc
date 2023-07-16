from setuptools import setup, find_packages

setup(
    name='calc',
    version='1.0.0',
    author='Batel',
    author_email='batel@jfrog.com',
    description='A simple calculator package',
    packages=find_packages("calc"),
    package_dir={'':"calc"},
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ]
)
