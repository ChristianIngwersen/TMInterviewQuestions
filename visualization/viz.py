import numpy as np
import matplotlib.pyplot as plt
from kp_utils import skeleton_constants
from mpl_toolkits.mplot3d import Axes3D


def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5 * max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


def draw_skeleton3d(points, extra_points=None, elev=13, azi=174., create_fig=True, ax=None):
    # This flip is done because matplotlibs way of initing axes. Labels changed accordingly
    points = points[:, [0, 2, 1]]

    if create_fig:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

    for skeleton in skeleton_constants.get_QFull_skeleton():
        ax.plot(points[skeleton, 0], points[skeleton, 1], points[skeleton, 2])

    if extra_points is not None:
        ax.plot(extra_points[:, 0], extra_points[:, 1], extra_points[:, 2], "*b")
    ax.view_init(elev=elev, azim=azi)
    ax.set_xlim3d([-300, 1500])
    ax.set_ylim3d([-900, 900])
    ax.set_zlim3d([0, 1800])
    ax.set_box_aspect([1, 1, 1])
    set_axes_equal(ax)
    ax.set_xlabel("X")
    ax.set_ylabel("Z")
    ax.set_zlabel("Y")

    return ax


