try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="razorpay",
    version="0.1.0",
    description="Razorpay Python Wrapper",
    url="http://github.com/decached/razorpay",
    author="Akash Kothawale",
    author_email="akash@decached.com",
    license="MIT",
    install_requires=[
        "requests>=2.8.1"
    ],
    packages=["razorpay"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ]
)
