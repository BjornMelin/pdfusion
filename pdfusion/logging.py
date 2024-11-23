"""Logging configuration for the PDFusion package."""

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
    """Configuration for logging setup."""

    format: str = DEFAULT_LOG_FORMAT
    date_format: str = DEFAULT_DATE_FORMAT
    level: int = logging.INFO
    stream: TextIO = sys.stdout

    def create_formatter(self) -> logging.Formatter:
        """Create a formatter with the configured format."""
        return logging.Formatter(fmt=self.format, datefmt=self.date_format)


def setup_logging(verbose: bool = False, config: LogConfig | None = None) -> None:
    """Configure logging for the application.

    Args:
        verbose: Whether to enable debug logging.
        config: Optional logging configuration. If not provided,
               default configuration will be used.
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
    """Get a logger instance.

    Args:
        name: Optional name for the logger. If not provided,
              returns the root package logger.

    Returns:
        A configured logger instance.
    """
    if name:
        return logger.getChild(name)
    return logger


__all__ = [
    "LogConfig",
    "setup_logging",
    "get_logger",
    "logger",
]
