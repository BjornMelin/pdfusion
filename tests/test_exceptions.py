"""
Tests for PDFusion exceptions.

This module contains tests for the custom exceptions used in the PDFusion package.

Author: Bjorn Melin
Date: 11/23/2024
"""

import pytest

from pdfusion.exceptions import (
    PDFusionError,
    NoPDFsFoundError,
    PDFusionMergeError,
)


def test_base_exception() -> None:
    """
    Test the base PDFusionError exception.
    
    Returns
    -------
    None
    """
    msg = "Test error message"
    error = PDFusionError(msg)

    assert str(error) == msg
    assert error.message == msg
    assert isinstance(error, Exception)


def test_no_pdfs_found_error() -> None:
    """
    Test the NoPDFsFoundError exception.
    
    Returns
    -------
    None
    """
    test_dir = "/path/to/dir"

    # Test with default message
    error = NoPDFsFoundError(test_dir)
    assert test_dir in str(error)
    assert error.directory == test_dir
    assert isinstance(error, PDFusionError)

    # Test with custom message
    custom_msg = "Custom error message"
    error = NoPDFsFoundError(test_dir, message=custom_msg)
    assert str(error) == custom_msg
    assert error.directory == test_dir


def test_merge_error() -> None:
    """
    Test the PDFusionMergeError exception.
    
    Returns
    -------
    None
    """
    filename = "test.pdf"
    original_error = ValueError("Invalid PDF")

    # Test with original error
    error = PDFusionMergeError(filename, original_error)
    assert filename in str(error)
    assert str(original_error) in str(error)
    assert error.filename == filename
    assert error.original_error == original_error
    assert isinstance(error, PDFusionError)

    # Test with custom message
    custom_msg = "Custom merge error"
    error = PDFusionMergeError(filename, message=custom_msg)
    assert str(error) == custom_msg
    assert error.filename == filename
    assert error.original_error is None


def test_exception_hierarchy() -> None:
    """
    Test the exception hierarchy relationships.
    
    Returns
    -------
    None
    """
    # Create instances of each exception type
    base_error = PDFusionError("base")
    no_pdfs_error = NoPDFsFoundError("/test/dir")
    merge_error = PDFusionMergeError("test.pdf")

    # Test inheritance relationships
    assert isinstance(no_pdfs_error, PDFusionError)
    assert isinstance(merge_error, PDFusionError)

    # Test that exceptions are properly organized
    with pytest.raises(PDFusionError):
        raise base_error

    with pytest.raises(PDFusionError):
        raise no_pdfs_error

    with pytest.raises(NoPDFsFoundError):
        raise no_pdfs_error

    with pytest.raises(PDFusionError):
        raise merge_error

    with pytest.raises(PDFusionMergeError):
        raise merge_error
