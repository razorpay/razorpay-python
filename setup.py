from setuptools import setup

setup(
    name="razorpay",
    version="0.1.0-alpha",
    description="Razorpay Python Client",
    url="https://github.com/decached/razorpay",
    author="Akash Kothawale",
    author_email="akash@decached.com",
    license="MIT",
    install_requires=["requests"],
    packages=["razorpay"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
