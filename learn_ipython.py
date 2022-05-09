from IPython import embed
import numpy as np
from os.path import join


# Qi why no return here
def load_data(rec_dir, output_list, valid_list, start, end):
    keypoints = np.load(join(rec_dir, 'keypoints.npz'))
    valid = np.load(join(rec_dir, 'valid_frame.npz'))
    keypoints_frame_id = keypoints['imgname']
    valid_frame_id = valid['imgname']
    keypoints_frame_id = [int(x.split('/')[-1][-9:-4]) for x in keypoints_frame_id]
    valid_frame_id = [int(x.split('/')[-1][-9:-4]) for x in valid_frame_id]
    for frame in range(start, end):
        try:
            valid_idx = valid_frame_id.index(frame)
        except ValueError:
            continue
        valid_list[frame - start] = {
            'imgname': valid['imgname'][valid_idx],
            'valid': valid['valid'][valid_idx],
        }
        if valid['valid'][valid_idx]:
            keypoints_idx = keypoints_frame_id.index(frame)
            output_list[frame - start] = {
                'center': keypoints['center'][keypoints_idx],
                'scale': keypoints['scale'][keypoints_idx],
                'keypoints': keypoints['keypoints'][keypoints_idx],
                'imgname': keypoints['imgname'][keypoints_idx],
                'gender': keypoints['gender'][keypoints_idx],
            }


rec_dir = '/media/qimaqi/My Passport/ego_data/hololens_data/record_20220215/recording_20220215_s1_01_qi_matias/2022-02-15-143227'

start = 1901
end = 4905
output_list = [None] * (end - start)
valid_list = [None] * (end - start)
load_data(rec_dir, output_list, valid_list, start, end)
# embed()
print('output_list',output_list)