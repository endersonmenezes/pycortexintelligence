# WIP: PY Cprtex Intelligence

## Prepare your ambient
```shell
pip install -r requirements.txt
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
)
```

## TO DO

- [ ] Document Build
- [ ] Document Usage
- [ ] Create a CLI for testing
- [ ] How to contrib
- [ ] Contributors
- [ ] API Coverage Expand
