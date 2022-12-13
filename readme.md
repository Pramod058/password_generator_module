#pwgenerator

pwgeneratoris a Python library for generating password of the user defined length.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pwgenerator.


```bash
pip install pwgenerator
```
   OR, in case of failure

```bash
python -m pip install pwgenerator
```
## Usage

```python
import pwgenerator

#returns 'Generated password with 10 characters' and
#returns "Something went wrong if any error occured.

pwgenerator.generatepass(10)

pwgenerator.CountChar("String")

## Contributing

Pull requests are welcome. 
