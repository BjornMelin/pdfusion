"""
Tests for PDFusion logging configuration.

This module contains tests for the logging configuration of the PDFusion package,
including default values, formatter creation, logging setup, logger retrieval, 
logger propagation, and logging at different levels.

Author: Bjorn Melin
Date: 11/7/2024
"""

import logging
from io import StringIO

import pytest

from pdfusion.logging import (
    DEFAULT_DATE_FORMAT,
    DEFAULT_LOG_FORMAT,
    LogConfig,
    get_logger,
    setup_logging,
)


def test_log_config_defaults() -> None:
    """
    Test LogConfig default values.
    
    Returns
    -------
    None
    """
    config = LogConfig()

    assert config.format == DEFAULT_LOG_FORMAT
    assert config.date_format == DEFAULT_DATE_FORMAT
    assert config.level == logging.INFO
    assert config.stream == sys.stdout


def test_create_formatter() -> None:
    """
    Test formatter creation with LogConfig.
    
    Returns
    -------
    None
    """
    config = LogConfig(format="%(levelname)s: %(message)s", date_format="%Y-%m-%d")

    formatter = config.create_formatter()
    assert isinstance(formatter, logging.Formatter)
    assert formatter._fmt == config.format
    assert formatter.datefmt == config.date_format


def test_setup_logging() -> None:
    """
    Test logging setup with different configurations.
    
    Returns
    -------
    None
    """
    # Test with default config
    setup_logging()
    logger = get_logger()
    assert logger.level == logging.INFO

    # Test verbose mode
    setup_logging(verbose=True)
    assert logger.level == logging.DEBUG

    # Test custom config
    stream = StringIO()
    custom_config = LogConfig(
        format="%(levelname)s - %(message)s", level=logging.WARNING, stream=stream
    )
    setup_logging(config=custom_config)

    logger = get_logger()
    assert logger.level == logging.WARNING

    # Test log output
    logger.warning("Test message")
    assert "WARNING - Test message" in stream.getvalue()


def test_get_logger() -> None:
    """
    Test logger retrieval.
    
    Returns
    -------
    None
    """
    # Test root logger
    root_logger = get_logger()
    assert root_logger.name == "pdfusion"

    # Test child logger
    child_name = "test_child"
    child_logger = get_logger(child_name)
    assert child_logger.name == f"pdfusion.{child_name}"

    # Test logger hierarchy
    assert child_logger.parent == root_logger


def test_logger_propagation() -> None:
    """
    Test that loggers don't propagate to root logger.
    
    Returns
    -------
    None
    """
    stream = StringIO()
    config = LogConfig(stream=stream)
    setup_logging(config=config)

    logger = get_logger()
    assert not logger.propagate

    # Test child logger
    child_logger = get_logger("child")
    assert not child_logger.propagate


@pytest.mark.parametrize(
    "level",
    [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL],
)
def test_log_levels(level: int) -> None:
    """
    Test logging at different levels.
    
    Parameters
    ----------
    level : int
        Logging level to test.
    
    Returns
    -------
    None
    """
    stream = StringIO()
    config = LogConfig(format="%(levelname)s - %(message)s", level=level, stream=stream)
    setup_logging(config=config)
    logger = get_logger()

    test_message = "Test log message"
    level_name = logging.getLevelName(level)

    # Log at the current level
    getattr(logger, level_name.lower())(test_message)
    log_output = stream.getvalue()

    assert f"{level_name} - {test_message}" in log_output
