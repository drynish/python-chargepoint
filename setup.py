from setuptools import find_packages, setup

setup(name='python-chargepoint',
      version='1.0.1',
      description='Read and control Chargepoint based EV devices',
      url='http://github.com/drynish/python-chargepoint',
      author='@drynish',
      license='MIT',
      install_requires=[
            'aiohttp',
            'asyncio'
      ],
      packages=find_packages(exclude=["dist"]),
      zip_safe=True)
