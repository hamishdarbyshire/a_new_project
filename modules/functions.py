"""
=====================
Functions Description
=====================

Here we can type a description of the project

Sub heading
===========

paragraph.

Classes and Methods
===================
"""


def add_ten(param):
    """
    Very brief description of what it does. I.e adds ten.

    Args:
        param (float): The input number

    Returns:
        float: The output number

    Notes:
        This is great.

        .. image:: _static/sphinx.jpg
            :align: center

        .. math::

            \\alpha =& \\beta \\\\
            \\gamma =& \\int_0^x s .ds \\\\

        .. code-block:: python

            import pandas as pd
            df = pd.DataFrame()

        .. note:: A note here
        .. warning:: Some warning here!!!
    """
    return param + 10


def _add_one(param):
    """add new changes"""
    return param + 1
