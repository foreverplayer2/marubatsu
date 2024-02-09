import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.datasets import load_diabetes

dataset = load_diabetes()

x, t = dataset.data, dataset.target

