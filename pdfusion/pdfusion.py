#!/usr/bin/env python3
"""
PDFusion - A lightweight utility for merging multiple PDF files.

This module provides both a command-line interface and a Python API
for combining multiple PDF files into a single document while preserving
quality and maintaining original file order.

Author: Bjorn Melin
Date: 11/23/2024
"""

from __future__ import annotations

from . import logging as log_utils
import sys
from datetime import datetime
from pathlib import Path
from typing import Final, NamedTuple, Sequence

from PyPDF2 import PdfMerger, PdfReader

from .exceptions import NoPDFsFoundError, PDFusionError, PDFusionMergeError

# Type aliases
PathLike = str | Path

# Constants
DEFAULT_GLOB_PATTERN: Final[str] = "*.pdf"
TIMESTAMP_FORMAT: Final[str] = "%Y%m%d_%H%M%S"
DEFAULT_FILE_PREFIX: Final[str] = "merged_pdf_"

# Configure logging
logger = log_utils.get_logger(__name__)


class MergeResult(NamedTuple):
    """
    Result of a PDF merge operation.

    Attributes
    ----------
    output_path : Path
        The path to the merged PDF file.
    files_merged : int
        The number of PDF files merged.
    total_pages : int
        The total number of pages in the merged PDF.
    """
    output_path: Path
    files_merged: int
    total_pages: int


def setup_logging(verbose: bool = False) -> None:
    """
    Configure logging for the application.

    Parameters
    ----------
    verbose : bool, optional
        Whether to enable debug logging (default is False).

    Returns
    -------
    None
    """
    log_utils.setup_logging(verbose=verbose)


def get_pdf_files(directory: PathLike) -> Sequence[Path]:
    """
    Get all PDF files from the specified directory.

    Parameters
    ----------
    directory : PathLike
        Path to the directory containing PDF files.

    Returns
    -------
    Sequence[Path]
        A sequence of paths to PDF files, sorted alphabetically.

    Raises
    ------
    NoPDFsFoundError
        If no PDF files are found in the directory.
    PDFusionError
        If there's an error accessing the directory.
    """
    dir_path = Path(directory)

    try:
        if not dir_path.is_dir():
            raise PDFusionError(f"Not a directory: {directory}")

        pdf_files = sorted(
            dir_path.glob(DEFAULT_GLOB_PATTERN), key=lambda x: x.name.lower()
        )
        pdf_list = list(pdf_files)

        if not pdf_list:
            raise NoPDFsFoundError(str(dir_path))

        return pdf_list

    except Exception as e:
        if isinstance(e, (NoPDFsFoundError, PDFusionError)):
            raise
        raise PDFusionError(f"Error accessing directory {directory}: {e}")


def merge_pdfs(
    input_dir: PathLike, output_filename: str | None = None, *, verbose: bool = False
) -> MergeResult:
    """
    Merge all PDF files in the specified directory into a single PDF file.

    Parameters
    ----------
    input_dir : PathLike
        Path to the directory containing PDF files.
    output_filename : str, optional
        Name for the output file. If not provided, a timestamp-based name will be used.
    verbose : bool, optional
        Whether to print detailed progress information (default is False).

    Returns
    -------
    MergeResult
        A named tuple containing output path and merge statistics.

    Raises
    ------
    PDFusionError
        Base class for all PDFusion-related errors.
    NoPDFsFoundError
        If no PDF files are found in the directory.
    PDFusionMergeError
        If an error occurs during the merging process.
    """
    setup_logging(verbose)
    merger = PdfMerger()
    total_pages = 0

    try:
        # Get list of PDF files
        input_path = Path(input_dir)
        pdf_files = get_pdf_files(input_path)

        # Create output filename if not provided
        if output_filename is None:
            timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
            output_filename = f"{DEFAULT_FILE_PREFIX}{timestamp}.pdf"
        elif not output_filename.lower().endswith(".pdf"):
            output_filename += ".pdf"

        output_path = input_path / output_filename

        # Merge PDFs
        for pdf_file in pdf_files:
            try:
                if verbose:
                    logger.debug(f"Processing: {pdf_file.name}")
                merger.append(str(pdf_file))
                with open(pdf_file, "rb") as f:
                    # Count pages in the PDF
                    total_pages += len(PdfReader(f).pages)
            except Exception as e:
                raise PDFusionMergeError(filename=str(pdf_file), original_error=e)

        # Write the merged PDF
        merger.write(str(output_path))
        num_files = len(pdf_files)
        logger.info(
            f"Successfully merged {num_files} PDF files "
            f"({total_pages} pages) into: {output_filename}"
        )

        return MergeResult(output_path, num_files, total_pages)

    except Exception as e:
        if isinstance(e, PDFusionError):
            raise
        raise PDFusionError(f"Unexpected error: {e}")

    finally:
        merger.close()


def main() -> None:
    """
    Command-line interface for PDFusion.

    Returns
    -------
    None
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Merge multiple PDF files into a single PDF",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "input_dir", type=Path, help="Directory containing PDF files to merge"
    )
    parser.add_argument(
        "-o", "--output", help="Output filename (optional)", default=None
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Print detailed progress information",
        action="store_true",
    )

    args = parser.parse_args()

    try:
        result = merge_pdfs(args.input_dir, args.output, verbose=args.verbose)
        sys.exit(0)

    except NoPDFsFoundError as e:
        logger.error(str(e))
        sys.exit(1)
    except PDFusionError as e:
        logger.error(f"Error: {str(e)}")
        sys.exit(1)
    except KeyboardInterrupt:
        logger.error("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
