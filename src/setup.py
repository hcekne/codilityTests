from setuptools import setup, find_packages

setup(
    name="codilityTests",
    packages=find_packages(
        include=["codilityTests"]
    ),
    include_package_data=True,
    python_requires=">=3.8",
)