from distutils.core import setup
setup(
  name = 'leapfrog_msh_reader',        
  packages = ['leapfrog_msh_reader'],  
  #package_dir={"":"src"},
  version = '0.1',      
  license='LGPL 3.0',       
  description = 'A simple reader of leapfrog mesh files, without onerous installation requirements.',  
  author = 'Thomas Martin',                  
  author_email = 'tpm319@gmail.com',      
  url = 'https://github.com/ThomasMGeo/leapfrog_msh_reader',     
  keywords = ['leapfrog', 'mesh', '.msh'],   
  install_requires=[            
          'os',
          'numpy'
          'typing',
          'pathlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',  
    'Programming Language :: Python :: 3.6',
  ],
)