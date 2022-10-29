from setuptools import setup

setup(
    name='autodd_rev2',
    version='1.0.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'praw==7.1.4',
        'psaw==0.0.12',
        'pandas==1.2.1',
        'tabulate==0.8.7',
        'requests==2.25.1',
        'multitasking==0.0.9',
    ],
    url = 'https://github.com/DylanAlloy/AutoDD_Rev2',  
    download_url = 'https://github.com/DylanAlloy/AutoDD_Rev2/archive/v_100.tar.gz',
)
