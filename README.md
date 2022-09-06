# Halley's Comet Orbit using Fourth Order Runge-Kutta
Halley's comet's acceleration can be described using three differential equations for each 3d axis. This program implements a numerical solution that plots its estimated trajectory from 1986 onwards.

## Documentation
Found [here](https://drive.google.com/file/d/1CS6jZQn9kkoZWqBgkhiEiiqSDuUiSCQ8/view?usp=sharing).

## Installation

Clone this git repo into desired folder then run commands below.

```bash
pip install numpy
pip install matplotlib
```

## Usage
Running the command below will output plots into ``/plots``directory.
```python
py -3 main.py
```
Default settings are 
```python
h = 0.01            # time step
h_min = 1e-8        # minimum step size
tol_max = 1e-2      # max tolerance
tol_min = 1e-3      # minimum tolerance
```
