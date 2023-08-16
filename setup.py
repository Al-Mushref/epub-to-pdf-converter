from setuptools import setup, find_packages

setup(
    name='epub-to-pdf-converter',
    version='0.1',  # Start with a development version
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=[
        'beautifulsoup4',
        'lxml',
        'pdfkit',
        # Add other dependencies if needed
    ],
    entry_points={
        'console_scripts': [
            'epub-to-pdf=epubconverter.bin.epub_to_pdf:main',  # This allows for command line execution
        ],
    },
    author='Al-Waleed Al-Salti',
    description='A command-line tool to convert EPUB to PDF.',
    license='MIT',  # Or another license if you prefer
    keywords='epub pdf converter',
    url='https://github.com/yourusername/epub-to-pdf-converter',  # Replace with your repository URL
)
