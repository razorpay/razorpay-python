from setuptools import setup

with open('README.md') as readme:
    readme_content = readme.read()

setup(
    name="razorpay",
    version="1.4.2",
    description="Razorpay Python Client",
    long_description=readme_content,
    long_description_content_type='text/markdown',
    url="https://github.com/razorpay/razorpay-python",
    author="Team Razorpay",
    license="MIT",
    install_requires=["requests"],
    include_package_data=True,
    package_dir={'razorpay': 'razorpay', 'razorpay.resources': 'razorpay/resources'},
    packages=['razorpay', 'razorpay.resources'],
    keywords='razorpay payment gateway india',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",

        # List of supported Python versions
        # Make sure that this is reflected in .github/workflows/python.yml as well
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
