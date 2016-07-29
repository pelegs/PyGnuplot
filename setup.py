from distutils.core import setup
setup(name='PyGnuplot',
      py_modules=['PyGnuplot'],
      version='0.7',
      license='MIT',
      description='Ultra light Python Gnuplot wrapper',
      author='Ben Schneider',
      author_email=' ',
      url='https://github.com/benschneider/PyGnuplot',
      download_url='https://github.com/benschneider/PyGnuplot/tarball/0.7',
      keywords=['gnuplot', 'plot'],
      install_requires=['numpy'],
      classifiers=["Topic :: Scientific/Engineering",
                   "License :: OSI Approved :: MIT License",
                   "Programming Language :: Python :: 2.7",
                   "Development Status :: 3 - Alpha"],
      )
