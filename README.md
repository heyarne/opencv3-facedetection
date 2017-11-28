# Face detection using OpenCV 3.3 and Python 3.6

## What is this?

A small python script detecting (frontal) faces in real time in the video feed coming from your webcam.

## Motivation

It felt a bit clunky for me to work through the OpenCV documentation and set everything up, everything would sometimes error with a cryptic message and in general it wasn't a straightforward experience. This repo should just work after cloning and setting up the pipenv.

## Set up

Dependencies are managed using [pipenv](https://docs.pipenv.org/), get started by entering

```
pipenv install
pipenv shell
```

The cascades are copied from the `share` folder shipping with opencv so there are no problems with paths either.

