"""Custom exceptions for the PDFusion package."""

from typing import Optional


class PDFusionError(Exception):
    """Base exception class for PDFusion errors."""

    def __init__(self, message: str, *args: object) -> None:
        self.message = message
        super().__init__(message, *args)


class NoPDFsFoundError(PDFusionError):
    """Raised when no PDF files are found in the specified directory."""

    def __init__(self, directory: str, message: Optional[str] = None) -> None:
        self.directory = directory
        super().__init__(message or f"No PDF files found in directory: {directory}")


class PDFusionMergeError(PDFusionError):
    """Raised when an error occurs during the PDF merging process."""

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
