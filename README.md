# RIM DATA CONFIGURATION

This repo configures the data generated from successful runs of rim simulations into a more readable format that looks like this in Excel:

![End result in Excel](/helper_images/end_result.png)

## HOW TO RUN

- Upload your generated data in the folder called `input`.

- In `main.py`, you enter the desired run number in the place called for it, and you modify the input file name to fit the name of your generated data input.

- This repo uses Numpy, so in your terminal of choice, run:

```pip install -r requirements.txt```

or you can simply run:

```pip install numpy```

- Run `main.py`