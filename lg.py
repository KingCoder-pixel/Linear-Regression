import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import statistics as st
import random as rd
import pandas as pd
import numpy as np 

data_file = pd.read_csv("c114/main.csv")

data_file_height_list = data_file["TOEFL Score"]
data_file_weight_list = data_file["Chance of Admit "]


# to find the value of y in y = mx +c  using hit and trial method
# y = []
# m = 0.95
# c = 93

# for i in data_file_height_list:
#     y_value = m*i + c
#     y.append(y_value)

# # data_file_plot_graph = px.scatter(
# #     x=data_file_height_list, y=data_file_weight_list)

# # data_file_plot_graph.update_layout(shapes=[dict(type="line", y0=min(y), y1=max(
# #     y), x0=min(data_file_height_list), x1=max(data_file_height_list))])

# # # data_file_plot_graph.show()

x = 250 



# to write an algorithum to find the value of m and c  with out hit and trial method

# to convert list into arrary \
height_array = np.array(data_file_height_list)
weight_array = np.array(data_file_weight_list)

#  to find the slop
finding_m ,finding_c = np.polyfit(height_array,weight_array,1)
y = []

for i in height_array:
    y_value = finding_m*i + finding_c
    if y_value == 3.23:
        y.append(y_value)
        
predict_y = finding_m*x+finding_c
print("the weight of some with height ",x, "is",predict_y)

# data_file_plot_graph = px.scatter(
#     x=height_array, y=weight_array)

# data_file_plot_graph.update_layout(shapes=[dict(type="line", y0=min(y), y1=max(
#     y), x0=min(height_array), x1=max(height_array))])

# data_file_plot_graph.show()