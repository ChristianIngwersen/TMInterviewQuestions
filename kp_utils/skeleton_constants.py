import numpy as np


def get_QFull_joint_names():
    """ Names of the joints in the Qualisys Full set
    """
    return ['LKneeIn',
            'RKneeIn',
            'RKneeOut',
            'LKneeOut',
            'LAnkleIn',
            'LAnkleOut',
            'RAnkleIn',
            'RAnkleOut',
            'RToe',
            'LToe',
            'LHip',
            'RHip',
            'HipBack',
            'SpineLow',
            'SpineMid',
            'SpineTop',
            'LShoulder',
            'RShoulder',
            'LElbowIn',
            'LElbowOut',
            'RElbowIn',
            'RElbowOut',
            'LWristIn',
            'LWristOut',
            'RWristOut',
            'RWristIn',
            'RFinger',
            'LFinger',
            'HeadTop',
            'LHead',
            'RHead',
            'Sternum'
            ]

def get_QFull_skeleton():
    """ Joint mapping in the Qualisys Full set
    """
    return np.array(
        [
            # Left leg
            [ 0, 3 ], # LKneeIn - LKneeOut
            [ 0, 10 ], # LKneeIn - LHip
            [ 3, 10 ], # LKneeOut - LHip
            [ 3, 5 ], # LKneeOut - LAnkleOut
            [ 0, 4 ], # LKneeIn - LAnkleIn
            [ 5, 4 ], # LAnkleOut - LAnkleIn
            [ 5, 9 ], # LAnkleOut - LToe
            [ 4, 9 ], # LAnkleIn - LToe

            # Right leg
            [ 1, 11 ], # RKneeIn - RHip
            [ 2, 11 ], # RKneeOut - RHip
            [ 1, 6 ], # RKneeIn - RAnkleIn
            [ 1, 2 ], # RKneeIn - RKneeOut
            [ 2, 7 ], # RKneeOut - RAnkleOut
            [ 6, 7 ], # RAnkleIn - RAnkleOut
            [ 6, 8 ], # RAnkleIn - RToe
            [ 7, 8 ], # RAnkleOut - RToe
            
            # Spine and shoulders
            [ 10, 11 ], # LHip - RHip
            [ 10, 12 ], # LHip - HipBack
            [ 11, 12 ], # RHip - HipBack
            [ 12, 13 ], # HipBack - SpineLow
            [ 13, 14 ], # SpineLow - SpineMid
            [ 14, 15 ], # SpineMid - SpineTop
            [ 15, 16 ], # SpineTop - LShoulder
            [ 15, 17 ], # SpineTop - RShoulder
            [ 16, 17 ], # LShoulder - RShoulder
            
            # Sternum
            [ 31, 13 ], # Sternum - SpineLow
            [ 31, 14 ], # Sternum - SpineMid
            [ 31, 15 ], # Sternum - SpineTop
            [ 31, 16 ], # Sternum_- LShoulder
            [ 31, 17 ], # Sternum - RShoulder
            
            # Head
            [ 15, 29 ], # SpineTop - LHead
            [ 15, 30 ], # SpineTop - RHead
            [ 30, 29 ], # RHead - LHead
            [ 30, 28 ], # RHead - HeadTop
            [ 29, 28 ], # LHead - HeadTop
            
            # Left arm
            [ 16, 18 ], # LShoulder - LElbowIn
            [ 16, 19 ], # LShoulder - LElbowOut
            [ 18, 19 ], # LElbowIn - LElbowOut
            [ 18, 22 ], # LElbowIn - LWristIn
            [ 19, 23 ], # LElbowOut - LWristOut
            [ 22, 23 ], # LWristIn - LWristOut
            [ 22, 27 ], # LWristIn - LFinger
            [ 23, 27 ], # LWristOut - LFinger
            
            # Right arm
            [ 17, 20 ], # RShoulder - RElbowIn
            [ 17, 21 ], # RShoulder - RElbowOut
            [ 20, 21 ], # RElbowIn - RElbowOut
            [ 20, 25 ], # RElbowIn - RWristIn
            [ 21, 24 ], # RElbowOut - RWristOut
            [ 25, 24 ], # RWristIn - RWristOut
            [ 25, 26 ], # RWristIn - RFinger
            [ 24, 26 ], # RWristOut - RFinger
        ]
    )

def get_QSMPL_joint_names():
    """ Names of the joints in the Qualisys-SMPL set
    """
    return ['LeftToe',
            'RightToe',
            'LeftAnkle',
            'RightAnkle',
            'LeftKnee',
            'RightKnee',
            'LeftHip',
            'RightHip',
            'BackHip',
            'SpineLow',
            'SpineMid',
            'SpineTop',
            'LeftShoulder',
            'RightShoulder',
            'LeftElbow',
            'RightElbow',
            'LeftWrist',
            'RightWrist',
            'LeftHand',
            'RightHand',
            'Neck',
            'Head',
            ]
def get_QSMPL_skeleton():
    """ Joint mapping in the Qualisys-SMPL set
    """
    return np.array(
        [
            # Legs
            [ 0, 2 ], # LeftToe - LeftAnkle
            [ 2, 4 ], # LeftAnkle - LeftKnee
            [ 4, 6 ], # LeftKnee - LeftHip
            [ 1, 3 ], # RightToe - RightAnkle
            [ 3, 5 ], # RightAnkle - RightKnee
            [ 5, 7 ], # RightKnee - RightHip
            
            # Hips
            [ 6, 8 ], # LeftHip - BackHip
            [ 7, 8 ], # RightHip - BackHip
            [ 6, 7 ], # LeftHip - RightHip
            
            # Spine and Head
            [ 8, 9 ], # BackHip - SpineLow
            [ 9, 10 ], # SpineLow - SpineMid
            [ 10, 11 ], # SpineMid - SpineTop
            [ 11, 20 ], # SpineTop - Neck
            [ 20, 21 ], # Neck - Head
            
            # Arms
            [ 11, 12 ], # SpineTop - LeftShoulder
            [ 11, 13 ], # SpineTop - RightShoulder
            [ 12, 14 ], # LeftShoulder - LeftElbow
            [ 14, 16 ], # LeftElbow- LeftWrist
            [ 16, 18 ], # LeftWrist- LeftHand
            [ 13, 15 ], # RightShoulder - RightElbow
            [ 15, 17 ], # RightElbow- RightHand
            [ 17, 19 ], # RightWrist- RightWrist
            
        ]
    )