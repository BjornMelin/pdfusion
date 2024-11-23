"""
Tests for PDFusion's core functionality.

This module contains tests for the core functionality of the PDFusion package,
including PDF file discovery, merging, error handling, and CLI interactions.

Author: Bjorn Melin
Date: 11/23/2024
"""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest
from PyPDF2 import PdfReader

from pdfusion import (
    NoPDFsFoundError,
    PDFusionError,
    PDFusionMergeError,
    merge_pdfs,
)
from pdfusion.pdfusion import get_pdf_files, main


def test_get_pdf_files(sample_pdfs: Path, empty_dir: Path) -> None:
    """
    Test PDF file discovery and sorting.
    
    Parameters
    ----------
    sample_pdfs : Path
        A temporary directory containing sample PDF files.
    empty_dir : Path
        An empty temporary directory.
    
    Returns
    -------
    None
    """ 
    # Test with directory containing PDFs
    files = get_pdf_files(sample_pdfs)
    assert len(files) == 3
    assert all(f.suffix == ".pdf" for f in files)
    assert [f.name for f in files] == ["test_1.pdf", "test_2.pdf", "test_3.pdf"]

    # Test with empty directory
    with pytest.raises(NoPDFsFoundError) as exc_info:
        get_pdf_files(empty_dir)
    assert str(empty_dir) in str(exc_info.value)


def test_get_pdf_files_errors(tmp_path: Path) -> None:
    """
    Test error handling in get_pdf_files.
    
    Parameters
    ----------
    tmp_path : Path
        A temporary directory path provided by pytest.
    
    Returns
    -------
    None
    """
    # Test with non-existent directory
    non_existent = tmp_path / "non_existent"
    with pytest.raises(PDFusionError) as exc_info:
        get_pdf_files(non_existent)
    assert "not a directory" in str(exc_info.value).lower()

    # Test with file instead of directory
    test_file = tmp_path / "test.txt"
    test_file.touch()
    with pytest.raises(PDFusionError) as exc_info:
        get_pdf_files(test_file)
    assert "not a directory" in str(exc_info.value).lower()


def test_merge_pdfs_basic(sample_pdfs: Path) -> None:
    """
    Test basic PDF merging functionality.
    
    Parameters
    ----------
    sample_pdfs : Path
        A temporary directory containing sample PDF files.
    
    Returns
    -------
    None
    """
    # Test with default output name
    result = merge_pdfs(sample_pdfs)
    assert result.output_path.exists()
    assert result.files_merged == 3
    assert result.total_pages == 4  # 3 files, but second file has 2 pages

    # Verify merged PDF content
    with open(result.output_path, "rb") as f:
        pdf = PdfReader(f)
        assert len(pdf.pages) == 4


def test_merge_pdfs_custom_output(sample_pdfs: Path) -> None:
    """
    Test PDF merging with custom output filename.
    
    Parameters
    ----------
    sample_pdfs : Path
        A temporary directory containing sample PDF files.
    
    Returns
    -------
    None
    """
    output_name = "custom_output.pdf"
    result = merge_pdfs(sample_pdfs, output_name)

    assert result.output_path.name == output_name
    assert result.output_path.exists()

    # Test without .pdf extension
    output_name = "custom_output"
    result = merge_pdfs(sample_pdfs, output_name)
    assert result.output_path.name == f"{output_name}.pdf"


def test_merge_pdfs_verbose(sample_pdfs: Path, caplog) -> None:
    """
    Test verbose output during PDF merging.
    
    Parameters
    ----------
    sample_pdfs : Path
        A temporary directory containing sample PDF files.
    caplog : pytest.LogCaptureFixture
        Fixture to capture log messages.
    
    Returns
    -------
    None
    """
    merge_pdfs(sample_pdfs, verbose=True)

    # Check for detailed log messages
    assert any("Processing:" in message for message in caplog.messages)
    assert any("Successfully merged" in message for message in caplog.messages)


def test_merge_pdfs_invalid_pdf(invalid_pdf_dir: Path) -> None:
    """
    Test handling of invalid PDF files.
    
    Parameters
    ----------
    invalid_pdf_dir : Path
        A temporary directory containing an invalid PDF file.
    
    Returns
    -------
    None
    """
    with pytest.raises(PDFusionMergeError) as exc_info:
        merge_pdfs(invalid_pdf_dir)

    assert "invalid.pdf" in str(exc_info.value)


def test_merge_pdfs_non_pdf_files(non_pdf_dir: Path) -> None:
    """
    Test behavior with non-PDF files.
    
    Parameters
    ----------
    non_pdf_dir : Path
        A temporary directory containing non-PDF files.
    
    Returns
    -------
    None
    """
    with pytest.raises(NoPDFsFoundError):
        merge_pdfs(non_pdf_dir)


@pytest.mark.parametrize(
    "permission_error",
    [
        "reading",  # Simulate read permission error
        "writing",  # Simulate write permission error
    ],
)
def test_merge_pdfs_permission_errors(
    sample_pdfs: Path, monkeypatch, permission_error: str
) -> None:
    """
    Test handling of permission errors.
    
    Parameters
    ----------
    sample_pdfs : Path
        A temporary directory containing sample PDF files.
    monkeypatch : pytest.MonkeyPatch
        Fixture to modify builtins and other modules.
    permission_error : str
        Type of permission error to simulate ("reading" or "writing").
    
    Returns
    -------
    None
    """

    def mock_open(*args, **kwargs):
        raise PermissionError(f"Permission denied: {permission_error}")

    if permission_error == "reading":
        monkeypatch.setattr("builtins.open", mock_open)
    else:
        monkeypatch.setattr("PyPDF2.PdfMerger.write", mock_open)

    with pytest.raises(PDFusionError) as exc_info:
        merge_pdfs(sample_pdfs)
    assert "permission denied" in str(exc_info.value).lower()


def test_merge_pdfs_memory_error_handling(sample_pdfs: Path, monkeypatch) -> None:
    """
    Test handling of memory errors during merge.
    
    Parameters
    ----------
    sample_pdfs : Path
        A temporary directory containing sample PDF files.
    monkeypatch : pytest.MonkeyPatch
        Fixture to modify builtins and other modules.
    
    Returns
    -------
    None
    """

    def mock_merge(*args, **kwargs):
        raise MemoryError("Not enough memory")

    monkeypatch.setattr("PyPDF2.PdfMerger.append", mock_merge)

    with pytest.raises(PDFusionMergeError) as exc_info:
        merge_pdfs(sample_pdfs)
    assert "memory" in str(exc_info.value).lower()


def test_cli_basic(sample_pdfs: Path, capsys) -> None:
    """
    Test basic CLI functionality.
    
    Parameters
    ----------
    sample_pdfs : Path
        A temporary directory containing sample PDF files.
    capsys : pytest.CaptureFixture
        Fixture to capture stdout and stderr.
    
    Returns
    -------
    None
    """
    test_args = ["pdfusion", str(sample_pdfs), "-o", "cli_test.pdf"]

    with patch.object(sys, "argv", test_args):
        main()

    captured = capsys.readouterr()
    assert "Successfully merged" in captured.out
    assert (sample_pdfs / "cli_test.pdf").exists()


def test_cli_errors(empty_dir: Path, capsys) -> None:
    """
    Test CLI error handling.
    
    Parameters
    ----------
    empty_dir : Path
        An empty temporary directory.
    capsys : pytest.CaptureFixture
        Fixture to capture stdout and stderr.
    
    Returns
    -------
    None
    """
    test_args = ["pdfusion", str(empty_dir)]

    with patch.object(sys, "argv", test_args), pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "No PDF files found" in captured.err


def test_cli_verbose(sample_pdfs: Path, capsys) -> None:
    """
    Test CLI verbose output.
    
    Parameters
    ----------
    sample_pdfs : Path
        A temporary directory containing sample PDF files.
    capsys : pytest.CaptureFixture
        Fixture to capture stdout and stderr.
    
    Returns
    -------
    None
    """
    test_args = ["pdfusion", str(sample_pdfs), "--verbose"]

    with patch.object(sys, "argv", test_args):
        main()

    captured = capsys.readouterr()
    assert "Processing:" in captured.out


@pytest.mark.parametrize(
    "signal_type",
    [
        KeyboardInterrupt,
        SystemExit,
    ],
)
def test_cli_interrupts(sample_pdfs: Path, signal_type, capsys) -> None:
    """
    Test CLI interrupt handling.
    
    Parameters
    ----------
    sample_pdfs : Path
        A temporary directory containing sample PDF files.
    signal_type : type
        Type of signal to simulate (KeyboardInterrupt or SystemExit).
    capsys : pytest.CaptureFixture
        Fixture to capture stdout and stderr.
    
    Returns
    -------
    None
    """

    def raise_interrupt(*args, **kwargs):
        raise signal_type()

    with (
        patch("pdfusion.pdfusion.merge_pdfs", side_effect=raise_interrupt),
        patch.object(sys, "argv", ["pdfusion", str(sample_pdfs)]),
        pytest.raises(SystemExit) as exc_info,
    ):
        main()

    assert exc_info.value.code == 1
    if signal_type == KeyboardInterrupt:
        captured = capsys.readouterr()
        assert "cancelled by user" in captured.err.lower()


def test_merge_pdfs_performance(sample_pdfs: Path, benchmark) -> None:
    """
    Test PDF merging performance.
    
    Parameters
    ----------
    sample_pdfs : Path
        A temporary directory containing sample PDF files.
    benchmark : pytest.BenchmarkFixture
        Fixture to benchmark the performance.
    
    Returns
    -------
    None
    """

    def merge_operation():
        return merge_pdfs(sample_pdfs, "benchmark.pdf")

    result = benchmark(merge_operation)
    assert result.files_merged == 3
    assert result.total_pages == 4


@pytest.mark.parametrize("num_files", [10, 50, 100])
def test_merge_pdfs_large_sets(tmp_path: Path, num_files: int, benchmark) -> None:
    """
    Test merging larger sets of PDFs.
    
    Parameters
    ----------
    tmp_path : Path
        A temporary directory path provided by pytest.
    num_files : int
        Number of PDF files to create and merge.
    benchmark : pytest.BenchmarkFixture
        Fixture to benchmark the performance.
    
    Returns
    -------
    None
    """
    # Create test PDFs
    for i in range(num_files):
        pdf_path = tmp_path / f"test_{i:03d}.pdf"
        writer = PdfWriter()
        writer.add_blank_page(width=595, height=842)
        with open(pdf_path, "wb") as f:
            writer.write(f)

    def merge_large_set():
        return merge_pdfs(tmp_path, f"large_set_{num_files}.pdf")

    result = benchmark(merge_large_set)
    assert result.files_merged == num_files
    assert result.total_pages == num_files


def test_merge_pdfs_resource_cleanup(sample_pdfs: Path) -> None:
    """
    Test proper resource cleanup after merging.
    
    Parameters
    ----------
    sample_pdfs : Path
        A temporary directory containing sample PDF files.
    
    Returns
    -------
    None
    """
    import psutil
    import os

    process = psutil.Process(os.getpid())
    initial_handles = process.num_fds()  # Unix

    # Perform multiple merges
    for i in range(5):
        merge_pdfs(sample_pdfs, f"cleanup_test_{i}.pdf")

    final_handles = process.num_fds()

    # Check for file descriptor leaks
    assert final_handles <= initial_handles + 1  # Allow for small variation
