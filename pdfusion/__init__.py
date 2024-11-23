"""
PDFusion - A lightweight utility for merging multiple PDF files.

Example:
    >>> from pdfusion import merge_pdfs
    >>> output_path, num_files = merge_pdfs("/path/to/pdfs", "merged.pdf")
    >>> print(f"Successfully merged {num_files} files into {output_path}")
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

__author__ = "Your Name"
__email__ = "your.email@example.com"
__license__ = "MIT"
