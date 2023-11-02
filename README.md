# Poisson's Equation Solver

This repository contains a Python script for solving the Poisson's equation numerically.

## Description

The Poisson's equation is an  elliptic partial differential equation of the form:

<p align="center">
    $\nabla^2u=f$
</p>

In this framework, we solve the Poisson equation in a 2D domain using the finite difference method. Rewriting the Poisson's equation yields:

<p align="center">
    $\frac{\partial ^2 u}{\partial x^2} + \frac{\partial ^2 u}{\partial y^2} = f(x,y)$,
</p>

where the partial derivatives are computed using the second-order finite differnece method:

<p align="center">
   $\frac{u_{i+1,j} - 2u_{i,j} + u_{i-1,j}}{\Delta x^2} + \frac{u_{i,j+1} - 2u_{i,j} + u_{i,j-1}}{\Delta y^2} = f_{i,j}$.
</p>

Rearanging the above equation yields:

<p align="center">
$u_{i,j} = \frac{\Delta x^2 \Delta y^2 f_{i,j} + \Delta y^2 (u_{i-1,j} + u_{i+1,j}) + \Delta x^2 (u_{i,j-1} + u_{i,j+1})}{2(\Delta x^2 + \Delta y^2)}$
</p>


## Installation

To use this script, you need to have Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).

You also need to have the following Python libraries installed:

- NumPy
- Matplotlib

You can install these libraries using the following commands:

pip install numpy
pip install matlotlib


## Usage

To run the script, navigate to the directory containing the script and run the following command:

python3 main.py


This will solve the Poisson equation and display the results in a 3D plot.

