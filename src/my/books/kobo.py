from my.core import warnings

warnings.high('my.books.kobo is deprecated! Please use my.kobo instead!')

from my.core.util import __NOT_HPI_MODULE__  # noqa: F401
from my.kobo import *
