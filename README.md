<p align="center">
  <img src="http://i.imgur.com/6VXbXnv.jpg" width="300px" />
</p>

Spear
=====

Product Hunt for Hackers - a CLI to Product Hunt. 

Built with [Hook](https://github.com/karan/Hook).

Install
=====

### Method 1 - Pip

```bash
$ pip install spear-cli
````

### Method 2 - Build from source

```bash
$ git clone git@github.com:karan/Spear.git
$ cd Spear
$ pip install -r requirements.txt
$ python setup.py install
```

Usage
====

### Get all today's products

```bash
$ hunt
```

### Get only the top 10 products

```bash
$ hunt -n 10  # or $ hunt --num 10
```

### Open a product in browser

```bash
$ hunt 2  # 2 is the rank of product
```
