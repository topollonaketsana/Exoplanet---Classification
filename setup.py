from setuptools import setup, find_packages

setup(
    name="exoplanet-classification",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy==1.21.0",
        "pandas==1.3.0",
        "scikit-learn==0.24.2",
        "matplotlib==3.4.2",
        "seaborn==0.11.2",
        "scipy==1.7.0",
        "astropy==5.1",
        "tensorflow==2.5.0",
        "jupyter==1.0.0"
    ],
    entry_points={
        'console_scripts': [
            'exoplanet_classify=exoplanet_classification.main:main_function',
        ],
    },
)


