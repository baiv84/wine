# Online winery supermarket

Exclusive crimean wine online shop.

# Prepare database file

Firstly, you have to prepare database file to load wine data.

Repository includes example database file: `example.xlsx`.

By default, program uses this file to load winery information.

If you wish to use your own database - copy `example.xlsx` to the new file: `mydatabase.xlsx`.

Then, create project environment file `.env` and add string, like this: 

```console
DATAFILE=mydatabase.xlsx
```
Fill database file `mydatabase.xlsx` with your own winery data.


# Prepare virtual environment

Next step, it is time to install package `python3-venv` to work with python virtual environment.

Update packages on your system `!(it depends on your operating system)`
in this document I use Ubuntu as my operating system. 

So I run update command:

```console
$ sudo apt update
```

and run command:

```console
$ sudo apt install -y python3-venv
```

Then jump to project folder:

```console
$ cd wine
```

and create new python environment to run the code:
```console
$ python3 -m venv venv
```

Activate new virtual environment:

```console
$ source venv/bin/activate
```

As a result, you will see command line prompt like this:

```console
(venv) wine $
```

# Install dependencies

In the virtual environment run command:

```console
(venv) wine $  pip3 install -r requirements.txt
```
This command installs all necessary libraries into the project virtual environment.

# Run program 

To run site, execute command:
```console
  (venv) wine  $ python3 main.py
```

# Control results

In browser jump to [http://127.0.0.1:8000](http://127.0.0.1:8000)

`Site engine may start a little bit slowly due to dependencies import`

If site is `temporary unavailable in browser`, wait for a while please and try again later (in 1-2 minutes).

# Projects goals

This site was written as a study project for Python web development course [Devman](https://dvmn.org)
