# Copyright (c) 2017
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import os

from setuptools import setup


def get_static_files(path):
    return [os.path.join(dirpath.replace("luigi/", ""), ext)
            for (dirpath, dirnames, filenames) in os.walk(path)
            for ext in ["*.html", "*.js", "*.css", "*.png",
                        "*.eot", "*.svg", "*.ttf", "*.woff", "*.woff2"]]

readme_note = """\
.. note::

   For the latest source, discussion, etc, please visit the
   `GitHub repository <https://github.com/luigi-orchestrator/luigi-hadoop>`_\n\n
"""

with open('README.rst') as fobj:
    long_description = readme_note + fobj.read()

install_requires = [
    'luigi>=2.6.2',  # update to luigi version w/o hadoop
]

if os.environ.get('READTHEDOCS', None) == 'True':
    install_requires.append('sphinx>=1.4.4')  # Value mirrored in doc/conf.py

setup(
    name='luigi-hadoop',
    version='0.1.0',
    description='Hadoop & HDFS functionality for Spotify/Luigi',
    long_description=long_description,
    author='The Luigi Authors',
    url='https://github.com/luigi-orchestrator/luigi-hadoop',
    license='Apache License 2.0',
    packages=[
        'luigi-hadoop',
        'luigi-hadoop.hdfs',
    ],
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Monitoring',
    ],
)
