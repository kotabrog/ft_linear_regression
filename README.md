# ft_linear_regression

![img](https://github.com/kotabrog/ft_linear_regression/blob/main/img/Figure_1.png)

## Overview

Linear regression, which I created myself as an assignment for 42

## Requirement

- python3.8

## Usage

```
git clone .....
cd ft_linear_regression
```

If you use venv

```
python3.8 -m venv .venv38
source .venv38/bin/activate
pip install -r requirements.txt
```

next

```
cd src
```

The following three functions are available.

- predict: Predicting data
- train: Learning data. Results can be graphed.
- data generate: A program that can retrieve a csv file of data points with a certain degree of scatter along a straight line.

### predict

sample

```
python predict.py 4 --file_name file.pickle
```

argument

- mileage: Predicted value
- --file_name: Data of learned parameters in pickle format output by train.py
- --theta0: Can specify `a + bx` a if file name is missing
- --theta1: Can specify `a + bx` b if file name is missing

### data generate

sample

```
python data_generator.py sample.csv -10000 -3.1 --x_min -30000 --x_max  30000 --sigma 100 --num 1000 --seed 32
```

argument

- output_name: Output file in csv format
- theta0: y-intercept of a straight line
- theta1: Inclination of a straight line
- --x_min: Minimum x-value to be generated
- --x_max: Maximum x-value to be generated
- --sigma: decentralization
- --num: Number of data to be generated
- --seed: Seed value of random number

### train

sample

```
python train.py ../data.csv --plot --polyfit --precision --epoch 1000
```

argument

- data_name: Data to be trained in csv format
- --output_name: Pickle format file name to save the learned parameter data
- --learning_rate: Learning rate
- --epoch: Number of times studied
- --verbose: Specify if you want to output detailed study progress
- --plot: Output a graph of data points and training results
- --polyfit: Output the result with numpy.polyfit
- --precision: Output the accuracy calculated by RMSE

## Author

[twitter](https://twitter.com/Kotabrog)

## Licence

[MIT](https://github.com/kotabrog/ft_linear_regression/blob/main/LICENSE)
