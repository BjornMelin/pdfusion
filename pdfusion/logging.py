"""
Logging configuration for the PDFusion package.

This module provides functions and classes for configuring and using logging
within the PDFusion package.

Author: Bjorn Melin
Date: 11/23/2024
"""

from __future__ import annotations

import logging
import sys
from dataclasses import dataclass
from typing import Final, TextIO

# Constants
DEFAULT_DATE_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"
DEFAULT_LOG_FORMAT: Final[str] = "%(asctime)s - %(levelname)s - %(message)s"

# Create a default logger for the package
logger = logging.getLogger("pdfusion")


@dataclass
class LogConfig:
    """
    Configuration for logging setup.

    Attributes
    ----------
    format : str
        The log message format.
    date_format : str
        The date format for log messages.
    level : int
        The logging level.
    stream : TextIO
        The stream to which log messages will be written.
    """
    format: str = DEFAULT_LOG_FORMAT
    date_format: str = DEFAULT_DATE_FORMAT
    level: int = logging.INFO
    stream: TextIO = sys.stdout

    def create_formatter(self) -> logging.Formatter:
        """
        Create a formatter with the configured format.

        Returns
        -------
        logging.Formatter
            A logging formatter configured with the specified format and date format.
        """
        return logging.Formatter(fmt=self.format, datefmt=self.date_format)


def setup_logging(verbose: bool = False, config: LogConfig | None = None) -> None:
    """
    Configure logging for the application.

    Parameters
    ----------
    verbose : bool, optional
        Whether to enable debug logging (default is False).
    config : LogConfig, optional
        Optional logging configuration. If not provided, default configuration will be used.

    Returns
    -------
    None
    """
    # Use default config if none provided
    cfg = config or LogConfig()

    # Set log level based on verbose flag
    if verbose:
        cfg.level = logging.DEBUG

    # Remove any existing handlers
    logger.handlers.clear()

    # Create and configure handler
    handler = logging.StreamHandler(cfg.stream)
    handler.setFormatter(cfg.create_formatter())

    # Configure logger
    logger.addHandler(handler)
    logger.setLevel(cfg.level)

    # Prevent propagation to root logger
    logger.propagate = False


def get_logger(name: str | None = None) -> logging.Logger:
    """
    Get a logger instance.

    Parameters
    ----------
    name : str, optional
        Optional name for the logger. If not provided, returns the root package logger.

    Returns
    -------
    logging.Logger
        A configured logger instance.
    """
    if name:
        return logger.getChild(name)
    return logger


# Set up default logging configuration
__all__ = [
    "LogConfig",
    "setup_logging",
    "get_logger",
    "logger",
]
