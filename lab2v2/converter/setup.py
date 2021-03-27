from setuptools import find_packages, setup


setup (
  name='convertator',
  version='1.0.0',
  description='this package convert .yaml/.toml/.pickle/.json into .yaml/.toml/.pickle/.json',
  author='dominuss_',
  author_email='kiril6701@gmail.com',
  url='https://github.com/dominuss-git',
  packages=find_packages(exclude=()),
  entry_points={
    'console_scripts' : [
      'convert = index.index:main',
    ]
  }
)