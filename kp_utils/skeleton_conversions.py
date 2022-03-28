import numpy as np

def find_middle(joint1, joint2):
    """ Interpolates the space directly in the middle
        between two joints in order:
            joint1 -> joint2.
        Expected size of joints: (N, 3)
    """
    assert joint1.ndim == 2 and joint2.ndim == 2
    assert joint1.shape[1] == 3 and joint2.shape[1] == 3
    diff = (joint2-joint1)/2
    joints = joint1 + diff
    return joints

def QFfull2QSMPL(skeleton_QFull):
    """ Converts a skeleton of Qualisys-Full format to
        Qualisys-SMPL format
        
        INPUT:
            skeleton_QFull - (N, 32, 3) or (32, 3)
        OUTPUT:
            skeleton_QSMPL - (N, 22, 3)
    """
    # Input should be (BATCH_SIZE, 32, 3)
    # or (32,3)
    assert skeleton_QFull.ndim in [2,3] 
    if skeleton_QFull.ndim == 2:
        skeleton_QFull = skeleton_QFull[None]
        
    bs, n_joints, ndim = skeleton_QFull.shape
    assert n_joints == 32 # Make sure joints are 
    assert ndim == 3 # Make sure there are 3 dimensions
    
    # Initialize new skeleton with 22 joints
    skeleton_QSMPL = np.zeros((bs, 22, ndim))

    skeleton_QSMPL[:,0,:] = skeleton_QFull[:,9,:]
    skeleton_QSMPL[:,1,:] = skeleton_QFull[:,8,:]
    skeleton_QSMPL[:,2,:] = find_middle(skeleton_QFull[:,5,:], 
                                               skeleton_QFull[:,4,:])
    skeleton_QSMPL[:,3,:] = find_middle(skeleton_QFull[:,7,:], 
                                               skeleton_QFull[:,6,:])
    
    skeleton_QSMPL[:,4,:] = find_middle(skeleton_QFull[:,3,:], 
                                               skeleton_QFull[:,0,:])
    skeleton_QSMPL[:,5,:] = find_middle(skeleton_QFull[:,2,:], 
                                               skeleton_QFull[:,1,:])
    skeleton_QSMPL[:,6,:] = skeleton_QFull[:,10,:]
    skeleton_QSMPL[:,7,:] = skeleton_QFull[:,11,:]
    skeleton_QSMPL[:,8,:] = skeleton_QFull[:,12,:]
    
    # Interpolate spine
    skeleton_QSMPL[:,9,:] = find_middle(skeleton_QFull[:,31,:], 
                                               skeleton_QFull[:,13,:])
    skeleton_QSMPL[:,10,:] = find_middle(skeleton_QFull[:,31,:], 
                                               skeleton_QFull[:,14,:])
    skeleton_QSMPL[:,11,:] = find_middle(skeleton_QFull[:,31,:], 
                                               skeleton_QFull[:,15,:])
    
    # Shoulders
    skeleton_QSMPL[:,12,:] = skeleton_QFull[:,16,:]
    skeleton_QSMPL[:,13,:] = skeleton_QFull[:,17,:]
    
    # Arms
    skeleton_QSMPL[:,14,:] = find_middle(skeleton_QFull[:,19,:], 
                                               skeleton_QFull[:,18,:])
    skeleton_QSMPL[:,15,:] = find_middle(skeleton_QFull[:,21,:], 
                                               skeleton_QFull[:,20,:])
    skeleton_QSMPL[:,16,:] = find_middle(skeleton_QFull[:,23,:], 
                                               skeleton_QFull[:,22,:])
    skeleton_QSMPL[:,17,:] = find_middle(skeleton_QFull[:,24,:], 
                                               skeleton_QFull[:,25,:])
    
    # Hands
    skeleton_QSMPL[:,18,:] = skeleton_QFull[:,27,:]
    skeleton_QSMPL[:,19,:] = skeleton_QFull[:,26,:]
    
    # Head
    skeleton_QSMPL[:,20,:] = find_middle(skeleton_QFull[:,30,:], 
                                               skeleton_QFull[:,29,:])
    skeleton_QSMPL[:,21,:] = skeleton_QFull[:,28,:]

    return skeleton_QSMPL