# WIP: PY Cortex Intelligence
## Last Release Notes

v.0.0.5

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
python setup.py bdist_wheel
```

## How to update on PIP
```
python -m twine upload  dist/*
```

## How to use
```python
from pycortexintelligence import functions as cortexfunctions

# Upload to Cortex
cortexfunctions.upload_to_cortex(
    cubo_id='',
    file_path='',
    plataform_url='CLIENTE.cortex-intelligence.com',
    username='',
    password='',
    data_format=''
)
```

## TO DO

- [ ] Document Build
- [ ] Document Usage
- [ ] Create a CLI for testing
