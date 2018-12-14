import setuptools


with open('requirements.txt') as f:
    reqs = f.read().splitlines()


setuptools.setup(
    name='rest_sms_getway',
    version='0.0.1',
    author='Geraldo Castro',
    author_email='victormatheuscastro@gmail.com',
    packages=['rest_sms_getway'],
    install_requires=reqs,
    keywords='python api rest sms getway',
    license='LGPLv3',
    url='https://github.com/exageraldo/RestSMSGetway',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    ],
)