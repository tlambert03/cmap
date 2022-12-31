import sys

sys.stderr.write(
    """
===============================
Unsupported installation method
===============================
cmap does not support installation with `python setup.py install`.
Please use `python -m pip install .` instead.
"""
)
sys.exit(1)


# The below code will never execute, however GitHub is particularly
# picky about where it finds Python packaging metadata.
# See: https://github.com/github/feedback/discussions/6456
#
# To be removed once GitHub catches up.

setup(  # type: ignore # noqa
    name="cmap",
    install_requires=["numpy"],
)
