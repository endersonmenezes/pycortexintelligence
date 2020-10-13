# WIP: PY Cprtex Intelligence

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
    url_da_plataforma='CLIENTE.cortex-intelligence.com',
    login='',
    senha='',
)
```

## TO DO

- [ ] Document Build
- [ ] Document Usage
- [ ] Create a CLI for testing