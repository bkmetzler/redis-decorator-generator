# Contributing

## Setup environment

### Select one to clone environment
1) ```git clone git@github.com:bkmetzler/redis-decorator-generator.git```

2) ```git clone https://github.com/bkmetzler/redis-decorator-generator.git```

3) ```gh repo clone bkmetzler/redis-decorator-generator```


### Create a Virutal Environment
```python3 -m venv venv```


### Activate the Virtual Environment
```source venv/bin/activate```

### Install 'dev-requirements.txt'
```pip install -r dev-requirements.txt```

### Install [pre-commit](https://pre-commit.com/)
```pre-commit install```

#### Using pre-commit
1) Run on only git staged files
    ```pre-commit run```
2) Run on all files in repo
    ```pre-commit run --all-files```
