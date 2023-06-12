from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in font/__init__.py
from font import __version__ as version

setup(
	name="font",
	version=version,
	description="font",
	author="Trilogy",
	author_email="E.azab@trilogy.com.sa",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
