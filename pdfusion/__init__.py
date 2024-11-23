"""
PDFusion - A lightweight utility for merging multiple PDF files.

This module provides the main entry points for the PDFusion package, including
the merge_pdfs function and custom exceptions.

Example
-------
>>> from pdfusion import merge_pdfs
>>> output_path, num_files = merge_pdfs("/path/to/pdfs", "merged.pdf")
>>> print(f"Successfully merged {num_files} files into {output_path}")

Author: Bjorn Melin
Date: 11/23/2024
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pdfusion")
except PackageNotFoundError:  # pragma: no cover
    # Package is not installed
    __version__ = "unknown"

from .pdfusion import (
    merge_pdfs,
    PDFusionError,
    NoPDFsFoundError,
    PDFusionMergeError,
)

__all__ = [
    "merge_pdfs",
    "PDFusionError",
    "NoPDFsFoundError",
    "PDFusionMergeError",
]

__author__ = "Bjorn Melin"
__email__ = "bjornmelin16@gmail.com"
__license__ = "MIT"
