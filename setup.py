import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
  name = 'PremCNXprofile',      
  packages = ['PremCNX'], 
  version = '0.0.1',  
  license='MIT', 
  description = 'PremCNX Profile',
  long_description=DESCRIPTION,
  author = 'PremCNX',                 
  author_email = 'kt.premchai@gmail.com',     
  url = 'https://github.com/PremCNX/PremCNXmyprofile',  
  download_url = 'https://github.com/PremCNX/PremCNX/archive/v0.0.1.zip',  
  keywords = ['PremCNX'],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Education',     
    'Topic :: Software Development :: Utilities',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.10',
  ],
)