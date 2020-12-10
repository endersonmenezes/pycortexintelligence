# Py Cortex Intelligence 
## Release Notes
**v.0.0.9**
- adding developer guidelines to contributions

**v.0.0.8**
- using logging module
- update on file creation to `utf-8`
- create core/messages.py file
- update README.md

**v.0.0.7**
- creating a CLI for pycortexintelligence --> cortex.py

**v.0.0.6**
- fix bug with calling _upload_local_2_cube_ function.

**v.0.0.5**

- added support to data_format on upload_to_cortex

```python
dafault_data_format = {
    "charset": "UTF-8",
    "quote": "\"",
    "escape": "\/\/",
    "delimiter": ",",
    "fileType": "CSV"
}
```

## How to build locale
```shell
pip install wheel
python setup.py bdist_wheel
```

## How to update on PIP
```
python -m twine upload  dist/*
```

## How to use
```python
from pycortexintelligence import functions as cortexfunctions

# DataFormat are Optionally defined
dafault_data_format = {
    "charset": "UTF-8",
    "quote": "\"",
    "escape": "\/\/",
    "delimiter": ",",
    "fileType": "CSV"
}

# Upload to Cortex
cortexfunctions.upload_to_cortex(
    cubo_id='',
    file_path='',
    plataform_url='CLIENTE.cortex-intelligence.com',
    username='',
    password='',
    data_format=dafault_data_format
)
```

## CLI Usage
```bash
cortex.py --help
```

### Examples

```bash
cortex.py startproject --name "Project Name" --sname project_name
```

## How to Contribute

### Developers

Developers can access our development manual by [clicking here](CONTRIBUTING.md).

### Community

You can create a new Issue [clicking here](issues/new/choose), and we will start a description about the reported Bug or Feature. 
