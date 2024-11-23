# 📄 PDFusion

A lightweight Python utility for effortlessly merging multiple PDF files into a single document.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)
[![GitHub](https://img.shields.io/badge/GitHub-BjornMelin-181717?logo=github)](https://github.com/BjornMelin)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Bjorn%20Melin-0077B5?logo=linkedin)](https://www.linkedin.com/in/bjorn-melin/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## 📋 Table of Contents

- [📝 Description](#-description)
  - [🚀 Key Features](#-key-features)
- [📂 Repository Structure](#-repository-structure)
- [💻 Installation](#-installation)
  - [For Users 🌟](#for-users-)
  - [For Developers 🔧](#for-developers-)
- [🎮 Usage](#-usage)
  - [Command Line Interface](#command-line-interface)
  - [Python API](#python-api)
- [🛠️ Development](#️-development)
  - [Running Tests](#running-tests)
- [🤝 Contributing](#-contributing)
- [👨‍💻 Author](#-author)
- [📜 License](#-license)
- [🌟 Star History](#-star-history)
- [🙏 Acknowledgments](#-acknowledgments)

## 📝 Description

PDFusion is a simple yet powerful command-line tool that makes it easy to combine multiple PDF files into a single document while preserving the original quality. Perfect for combining reports, consolidating documentation, or organizing digital paperwork.

### 🚀 Key Features

- 📁 Merge all PDFs in a directory with a single command
- 🔄 Automatic alphabetical ordering of files
- ⏱️ Timestamp-based output naming option
- 🛠️ Both CLI and Python API support
- 💡 Clear progress feedback and error handling
- 🔒 Maintains original PDF quality
- 📝 Detailed logging of the merge process
- 🔍 Type hints with full mypy support
- 🧪 Comprehensive test coverage (>90%)
- 📊 Performance benchmarks included
- 🐛 Custom exception handling
- 🎯 Supports Python 3.11+

## 📂 Repository Structure

```mermaid
graph TD
    A[pdfusion/] --> B[pdfusion/]
    A --> C[tests/]
    A --> D[examples/]
    A --> E[Documentation]
    
    B --> B1[__init__.py]
    B --> B2[exceptions.py]
    B --> B3[logging.py]
    B --> B4[pdfusion.py]
    B --> B5[py.typed]
    
    C --> C1[__init__.py]
    C --> C2[conftest.py]
    C --> C3[test files]
    
    D --> D1[basic_usage.py]
    
    E --> E1[README.md]
    E --> E2[LICENSE]
    E --> E3[CONTRIBUTING.md]
    E --> E4[Configuration Files]
```

## 💻 Installation

### For Users 🌟

```bash
pip install pdfusion
```

### For Developers 🔧

```mermaid
graph LR
    A[Clone Repository] --> B[Create Virtual Environment]
    B --> C[Activate Environment]
    C --> D[Install Dependencies]
    D --> E[Ready to Develop!]
```

1. Clone the repository:

    ```bash
    git clone https://github.com/BjornMelin/pdfusion.git
    cd pdfusion
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

    > **Note:** You can also use `virtualenv` instead of `venv`. See the [Virtual Environment Setup Guide](docs/virtualenv-setup.md) for more details.

3. Install development dependencies:

    ```bash
    pip install -r requirements-dev.txt
    ```

## 🎮 Usage

### Command Line Interface

```mermaid
graph LR
    A[Input Directory] --> B[PDFusion CLI]
    B --> C[Processing]
    C --> D[Merged PDF]
    style B fill:#f9f,stroke:#333,stroke-width:4px
```

```bash
# Basic usage
pdfusion /path/to/pdfs -o merged.pdf

# With verbose output
pdfusion /path/to/pdfs -v

# Auto timestamp filename
pdfusion /path/to/pdfs
```

### Python API

```python
from pdfusion import merge_pdfs

# Basic usage
result = merge_pdfs("/path/to/pdfs", "output.pdf")
print(f"Merged {result.files_merged} files into {result.output_path}")

# With verbose output
result = merge_pdfs("/path/to/pdfs", verbose=True)
print(f"Total pages in merged PDF: {result.total_pages}")
```

## 🛠️ Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=pdfusion

# Run performance benchmarks
pytest tests/test_pdfusion.py -v -m benchmark

# Run specific test file
pytest tests/test_pdfusion.py -v
```

## 🤝 Contributing

```mermaid
graph LR
    A[Fork Repository] --> B[Create Feature Branch]
    B --> C[Make Changes]
    C --> D[Commit Changes]
    D --> E[Push to Branch]
    E --> F[Open Pull Request]
    style F fill:#f96,stroke:#333,stroke-width:4px
```

1. Fork the repository
2. Create your feature branch (`git checkout -b feat/version/AmazingFeature`)
3. Commit your changes (`git commit -m 'type(scope): Add some AmazingFeature'`)
4. Push to the branch (`git push origin feat/version/AmazingFeature`)
5. Open a Pull Request (`feat(scope): Add some AmazingFeature`)

## 👨‍💻 Author

### Bjorn Melin

[![AWS Certified Solutions Architect](https://images.credly.com/size/110x110/images/0e284c3f-5164-4b21-8660-0d84737941bc/image.png)](https://www.credly.com/org/amazon-web-services/badge/aws-certified-solutions-architect-associate)
[![AWS Certified Developer](https://images.credly.com/size/110x110/images/b9feab85-1a43-4f6c-99a5-631b88d5461b/image.png)](https://www.credly.com/org/amazon-web-services/badge/aws-certified-developer-associate)
[![AWS Certified AI Practitioner](https://images.credly.com/size/110x110/images/4d4693bb-530e-4bca-9327-de07f3aa2348/image.png)](https://www.credly.com/org/amazon-web-services/badge/aws-certified-ai-practitioner)
[![AWS Certified Cloud Practitioner](https://images.credly.com/size/110x110/images/00634f82-b07f-4bbd-a6bb-53de397fc3a6/image.png)](https://www.credly.com/org/amazon-web-services/badge/aws-certified-cloud-practitioner)

AWS-certified Solutions Architect and Developer with expertise in cloud architecture and modern development practices. Connect with me on:

- 🌐 [GitHub](https://github.com/BjornMelin)
- 💼 [LinkedIn](https://www.linkedin.com/in/bjorn-melin/)

Project Link: [https://github.com/BjornMelin/pdfusion](https://github.com/BjornMelin/pdfusion)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=bjornmelin/pdfusion&type=Date)](https://star-history.com/#bjornmelin/pdfusion&Date)

## 🙏 Acknowledgments

- 🐍 [Python](https://www.python.org/)
- 📄 [pypdf2](https://pypdf.readthedocs.io/en/stable/)
- 🏷️ [GitHub Badges](https://shields.io/)

<div align="center">
    <h3>⚡ Built with Python 3.11 + pypdf2 by Bjorn Melin</h3>
</div>
