
from setuptools import setup, find_packages

setup(
    name='ElgatoWavePy',
    version='0.1.5',
    packages=find_packages(),
    install_requires=[
        'websocket-client',
        'websockets'
    ],
    author='SteepyTheFrenchMaker',
    description='Control Elgato WaveLink with Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Ste3py/ElgatoWavePy',
    project_urls={
        'Documentation': 'https://github.com/Ste3py/ElgatoWavePy/wiki',  # URL vers le wiki GitHub
        'Source': 'https://github.com/Ste3py/ElgatoWavePy',
    },
    
    
    
    
    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
