"""
This script creates stimulus lists for the emotional go-nogo task. 
In this task, negative and neutral images are presented with a 
circle or squared overlaid onto it. The circle and square indicate
go and no-go trials (balanced between individuals). 
"""

import pandas as pd
import numpy as np

# Options
n_lists = 100  # number of stimulus lsits
n_go_sets = 4  # Number of times each image is in go trial
n_nogo_sets = 1 # number of times each image is in nogo trial

# Load stimulus lists
stims = pd.read_csv('crit_stims.csv')

# Loop through and make sets
for i in np.arange(n_lists):

    # Make a go lists as empty dataframe and add crit stims
    sq_go_list = pd.DataFrame(columns=stims.columns)
    ci_go_list = pd.DataFrame(columns=stims.columns)
    for gi in np.arange(n_go_sets):
        sq_go_list = sq_go_list.append(stims)
        ci_go_list = ci_go_list.append(stims)

    # Update info in square go list
    sq_go_list['phase'] = 'real'
    sq_go_list['description'] = 'square_go'
    sq_go_list['trial_type'] = 'go'
    sq_go_list['gonogo_image'] = 'square.png'

    # Update info in circle go list
    ci_go_list['phase'] = 'real'
    ci_go_list['description'] = 'circle_go'
    ci_go_list['trial_type'] = 'go'
    ci_go_list['gonogo_image'] = 'circle.png'

    # Make no-go lists as empty dataframe and add crit stims
    sq_nogo_list = pd.DataFrame(columns=stims.columns)
    ci_nogo_list = pd.DataFrame(columns=stims.columns)
    for ngi in np.arange(n_nogo_sets):
        sq_nogo_list = sq_nogo_list.append(stims)
        ci_nogo_list = ci_nogo_list.append(stims)

    # Update info in square nogo list
    sq_nogo_list['phase'] = 'real'
    sq_nogo_list['description'] = 'square_nogo'
    sq_nogo_list['trial_type'] = 'nogo'
    sq_nogo_list['gonogo_image'] = 'square.png'

    # Update info in circle nogo list
    ci_nogo_list['phase'] = 'real'
    ci_nogo_list['description'] = 'circle_nogo'
    ci_nogo_list['trial_type'] = 'nogo'
    ci_nogo_list['gonogo_image'] = 'circle.png'

    # Make the square go block
    square_list = pd.concat([sq_go_list, ci_nogo_list]).sample(frac=1)
    square_list.to_csv(f'set-{i+1:03}_run-squarego.csv', index=False)

    # Make the circle go block
    circle_list = pd.concat([sq_nogo_list, ci_go_list]).sample(frac=1)
    circle_list.to_csv(f'set-{i+1:03}_run-circlego.csv', index=False)
