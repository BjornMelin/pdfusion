# PDFusion

A lightweight Python utility for effortlessly merging multiple PDF files into a single document.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)
[![GitHub](https://img.shields.io/badge/GitHub-BjornMelin-181717?logo=github)](https://github.com/BjornMelin)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Bjorn%20Melin-0077B5?logo=linkedin)](https://www.linkedin.com/in/bjorn-melin/)

## Description

PDFusion is a simple yet powerful command-line tool that makes it easy to combine multiple PDF files into a single document while preserving the original quality. Perfect for combining reports, consolidating documentation, or organizing digital paperwork.

### Key Features

- 📁 Merge all PDFs in a directory with a single command
- 🔄 Automatic alphabetical ordering of files
- ⏱️ Timestamp-based output naming option
- 🛠️ Both CLI and Python API support
- 💡 Clear progress feedback and error handling
- 🔒 Maintains original PDF quality
- 📝 Detailed logging of the merge process

## Why PDFusion?

The name "PDFusion" combines "PDF" with "fusion" to create a memorable and meaningful name that:

- Clearly indicates the tool's purpose (PDF merging)
- Suggests the idea of combining/fusion
- Is easy to remember and type
- Has a professional yet approachable feel
- Is unique enough to stand out in searches
- Works well as both a command name and package name

## Script Name

The main script is named `pdfusion.py`, following Python naming conventions with:

- All lowercase letters
- No spaces (using underscores if needed)
- Clear indication of purpose
- Easy to type and remember

The script can be invoked simply as:

```bash
python pdfusion.py /path/to/pdfs -o merged.pdf
```

## Repository Structure

```plaintext
pdfusion/
├── pdfusion.py
├── README.md
├── requirements.txt
├── setup.py
├── tests/
│   └── test_pdfusion.py
├── examples/
│   └── basic_usage.py
└── .gitignore
```

## Setting Up a Virtual Environment

To ensure that the project dependencies are isolated and do not interfere with other projects, it is recommended to use a virtual environment. Follow these steps to set up and activate a virtual environment:

1. Install the `virtualenv` package if you haven't already:

    ```bash
    pip install virtualenv
    ```

2. Create a new virtual environment in the project directory:

    ```bash
    virtualenv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Installation

```bash
pip install pdfusion
```

<!-- ## Usage

[Usage instructions would go here] -->

## Contributing

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

- [GitHub](https://github.com/BjornMelin)
- [LinkedIn](https://www.linkedin.com/in/bjorn-melin/)

Project Link: [https://github.com/BjornMelin/pdfusion](https://github.com/BjornMelin/pdfusion)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=bjornmelin/pdfusion&type=Date)](https://star-history.com/#bjornmelin/pdfusion&Date)

## 🙏 Acknowledgments

- [Python](https://www.python.org/)
- [pypdf2](https://pypdf.readthedocs.io/en/stable/)
- [GitHub Badges](https://shields.io/)

<div align="center">
    <strong>Built with Python 3.11 + pypdf2 by Bjorn Melin</strong>
</div>
