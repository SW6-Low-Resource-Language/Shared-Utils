# shared-resources/shared-resources/README.md

# Shared Resources

This repository contains utility functions for handling JSON and text file operations. The primary file is `file_service.py`, which includes functions such as `open_json`, `write_json`, `open_txt`, and `write_txt`.

## Installation

To use the shared resources in your projects, you can install this package using pip. Navigate to the root directory of the `shared-resources` repository and run:

```
pip install .
```

## Usage

Once installed, you can import the utility functions in your other repositories as follows:

```python
from shared_resources.src.file_service import open_json, write_json, open_txt, write_txt
```

## Functions

### open_json(file_path)

Opens a JSON file and returns the data.

### write_json(data, file_path)

Writes data to a JSON file.

### open_txt(file_path, separator='\n')

Opens a text file and returns the content split by the specified separator.

### write_txt(data, file_path, separator='\n')

Writes data to a text file, joining the elements with the specified separator.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the utility functions.