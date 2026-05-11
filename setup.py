from setuptools import setup

with open('README.md') as readme:
    readme_content = readme.read()

setup(
    name="razorpay",
    version="2.0.1",
    description="Razorpay Python Client",
    long_description=readme_content,
    long_description_content_type='text/markdown',
    url="https://github.com/razorpay/razorpay-python",
    author="Team Razorpay",
    license="MIT",
    python_requires='>=3.10',
    install_requires=["requests>=2.28.0"],
    include_package_data=True,
    package_dir={'razorpay': 'razorpay', 'razorpay.resources': 'razorpay/resources'},
    packages=['razorpay', 'razorpay.resources'],
    keywords='razorpay payment gateway india',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
