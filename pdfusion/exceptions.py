"""
Custom exceptions for the PDFusion package.

This module defines custom exceptions used in the PDFusion package to handle
specific error conditions.

Author: Bjorn Melin
Date: 11/23/2024
"""

from typing import Optional


class PDFusionError(Exception):
    """
    Base exception class for PDFusion errors.

    Attributes
    ----------
    message : str
        The error message.
    """

    def __init__(self, message: str, *args: object) -> None:
        self.message = message
        super().__init__(message, *args)


class NoPDFsFoundError(PDFusionError):
    """
    Raised when no PDF files are found in the specified directory.

    Attributes
    ----------
    directory : str
        The directory where no PDF files were found.
    """

    def __init__(self, directory: str, message: Optional[str] = None) -> None:
        self.directory = directory
        super().__init__(message or f"No PDF files found in directory: {directory}")


class PDFusionMergeError(PDFusionError):
    """
    Raised when an error occurs during the PDF merging process.

    Attributes
    ----------
    filename : str
        The name of the file that caused the error.
    original_error : Optional[Exception]
        The original exception that was raised.
    """

    def __init__(
        self,
        filename: str,
        original_error: Optional[Exception] = None,
        message: Optional[str] = None,
    ) -> None:
        self.filename = filename
        self.original_error = original_error
        super().__init__(
            message or f"Error merging file {filename}: {str(original_error)}"
        )
