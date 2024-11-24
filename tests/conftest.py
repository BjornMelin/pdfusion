"""
Test configuration and fixtures for PDFusion tests.

This file contains fixtures for setting up and tearing down test environments.

Author: Bjorn Melin
Date: 11/23/2024
"""

import os
import shutil
from pathlib import Path
from typing import Generator

import pytest
from PyPDF2 import PdfWriter


@pytest.fixture
def temp_dir(tmp_path: Path) -> Generator[Path, None, None]:
    """
    Create a temporary directory for tests.
    
    Parameters
    ----------
    tmp_path : Path
        The temporary directory path provided by pytest.
    
    Returns
    -------
    Generator[Path, None, None]
        The temporary directory path.
    
    Examples
    --------
    >>> def test_temp_dir(temp_dir: Path):
    ...     assert temp_dir.exists()
    """
    yield tmp_path
    # Cleanup after tests
    if tmp_path.exists():
        try:
            shutil.rmtree(tmp_path)
        except PermissionError:
            pass  # Handle PermissionError


@pytest.fixture
def sample_pdfs(temp_dir: Path) -> Generator[Path, None, None]:
    """
    Create sample PDF files for testing.
    
    Parameters
    ----------
    temp_dir : Path
        The temporary directory path for storing sample PDFs.
    
    Returns
    -------
    Generator[Path, None, None]
        The path to the directory containing sample PDFs.
    
    Examples
    --------
    >>> def test_sample_pdfs(sample_pdfs: Path):
    ...     assert len(list(sample_pdfs.glob("*.pdf"))) == 3
    """
    # Create three simple PDF files
    for i in range(1, 4):
        pdf_path = temp_dir / f"test_{i}.pdf"
        writer = PdfWriter()

        # Add a blank page to each PDF
        writer.add_blank_page(width=595, height=842)  # A4 size

        # Add a second page to the second PDF
        if i == 2:
            writer.add_blank_page(width=595, height=842)

        with open(pdf_path, "wb") as output_file:
            writer.write(output_file)

    yield temp_dir


@pytest.fixture
def empty_dir(temp_dir: Path) -> Generator[Path, None, None]:
    """
    Create an empty directory for testing.
    
    Parameters
    ----------
    temp_dir : Path
        The temporary directory path for creating an empty directory.
    
    Returns
    -------
    Generator[Path, None, None]
        The path to the empty directory.
    
    Examples
    --------
    >>> def test_empty_dir(empty_dir: Path):
    ...     assert empty_dir.exists()
    """
    empty_path = temp_dir / "empty"
    empty_path.mkdir(exist_ok=True)
    yield empty_path


@pytest.fixture
def invalid_pdf_dir(temp_dir: Path) -> Generator[Path, None, None]:
    """
    Create a directory with an invalid PDF file.
    
    Parameters
    ----------
    temp_dir : Path
        The temporary directory path for creating an invalid PDF file.
    
    Returns
    -------
    Generator[Path, None, None]
        The path to the directory containing the invalid PDF file.
    
    Examples
    --------
    >>> def test_invalid_pdf_dir(invalid_pdf_dir: Path):
    ...     assert (invalid_pdf_dir / "invalid.pdf").exists()
    """
    invalid_path = temp_dir / "invalid.pdf"
    with open(invalid_path, "w") as f:
        f.write("This is not a valid PDF file")
    yield temp_dir


@pytest.fixture
def non_pdf_dir(temp_dir: Path) -> Generator[Path, None, None]:
    """
    Create a directory with non-PDF files.
    
    Parameters
    ----------
    temp_dir : Path
        The temporary directory path for creating non-PDF files.
    
    Returns
    -------
    Generator[Path, None, None]
        The path to the directory containing non-PDF files.
    
    Examples
    --------
    >>> def test_non_pdf_dir(non_pdf_dir: Path):
    ...     assert len(list(non_pdf_dir.glob("*.*"))) == 3
    """
    files = ["test.txt", "test.doc", "test.jpg"]
    for filename in files:
        path = temp_dir / filename
        with open(path, "w") as f:
            f.write("Test content")
    yield temp_dir


@pytest.fixture(autouse=True)
def cleanup_files() -> Generator[None, None, None]:
    """
    Cleanup any test files after each test.
    
    Returns
    -------
    Generator[None, None, None]
        None
    
    Examples
    --------
    >>> def test_cleanup_files():
    ...     # Test code here
    """
    yield
    # Add any global cleanup here if needed
