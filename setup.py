from setuptools import setup

version = open('config/VERSION').read().strip()

setup(
    name='twentyc.rpc',
    version=open('config/VERSION').read().rstrip(),
    author='20C',
    author_email='code@20c.com',
    description='client for 20c\'s RESTful API',
    long_description=open('README.md').read(),
    license='LICENSE',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=['twentyc.rpc'],
    namespace_packages=['twentyc'],
    url='https://github.com/20c/twentyc.rpc',
    download_url='https://github.com/20c/twentyc.rpc/%s'%version,
    include_package_data=True,
    maintainer='20C',
    maintainer_email='code@20c.com',
    zip_safe=False
)
