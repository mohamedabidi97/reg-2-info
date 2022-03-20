# Reg2info

![version](https://img.shields.io/badge/version-1.0.0-blue)  ![Python](https://img.shields.io/badge/Language-Python-green) ![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg) [![License](https://img.shields.io/badge/license-MIT-red.svg)](https://opensource.org/licenses/MIT) 

**reg2info** is a Python package for getting meaningful information from a Linear regression model.




## Table of content

- [Installation](#where-to-get-it)
- [Dependencies](#dependencies)
- [Main Features](#pmain-features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

##  Where to get it

Binary installers for the latest released version are available at the  [Python Package Index (PyPI)](https://pypi.org/project/reg2info)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install reg2info :

```bash
pip install reg2info
```
## Dependencies
- Numpy
- Matplotlib

## Main Features
- A linear regression line has an equation of the form **_Y = a + bX_**, where **_X_** is the explanatory variable and **_Y_** is the dependent variable. The slope of the line is **_b_**, and **_a_** is the intercept (the value of **_y_** when **_x_** = 0).

- A regression line is the “best fit” line for your data. You basically draw a line that best represents the data points. It’s like an average of where all the points line up. In linear regression, the regression line is a perfectly straight line.

## Usage 

```python
import reg2info as r2i

lr = LinearRegression().fit(X_train, y_train)

# returns equation
eq = r2i.reg_equation(lr)

# returns line and data plot
plot = r2i.reg_plot(lr,X_train[feature], y_train)
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
