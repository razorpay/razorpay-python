from setuptools import setup

setup(
    name="razorpay",
    version="0.2.0",
    description="Razorpay Python Client",
    url="https://github.com/razorpay/razorpay-python",
    author="Team Razorpay",
    author_email="support@razorpay.com",
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
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
