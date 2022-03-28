"""
Example script to load and plot a frame in the data. You can use any of the supplied files,
but they contain the same information
"""

import json
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from visualization import viz
from matplotlib import pyplot as plt
from kp_utils import skeleton_constants


with open("data/mha_fullswing_6iron_0000/measurement.json", "r") as fp:
    data = json.load(fp)
joints3d = np.asarray(data["data"])[:, :3, :]

# Here there will be some NAN values due to unlabeled data in the sequence.
# to filter them out use
joints3d = joints3d[:, :, np.array(data["metadata"]["valid_frames"])]

ax = viz.draw_skeleton3d(joints3d[:, :, 0])
plt.show()

# Note the order of the joints
print(skeleton_constants.get_QFull_joint_names())
