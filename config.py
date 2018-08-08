num_parallel_calls = 4
input_shape = 416
max_boxes = 20
jitter = 0.3
hue = 0.1
sat = 1.0
cont = 0.8
bri = 0.1
weights_file = './model_data/yolo3.npy'
norm_decay = 0.99
norm_epsilon = 0.001
pre_train = True
num_anchors = 9
num_classes = 80
training = True
ignore_thresh = .5
learning_rate = 0.001
train_batch_size = 10
val_batch_size = 10
train_num = 118287
val_num = 5000
Epoch = 50
obj_threshold = 0.01
nms_threshold = 0.4
gpu_index = "0"
data_dir = './model_data'
model_dir = './test_model'
anchors_path = './model_data/yolo_anchors.txt'
classes_path = './model_data/coco_classes.txt'
train_data_file = '/data0/dataset/coco/train2017'
val_data_file = '/data0/dataset/coco/val2017'
train_annotations_file = '/data0/gaochen3/tensorflow-yolo3/annotations/instances_train2017.json'
val_annotations_file = '/data0/gaochen3/tensorflow-yolo3/annotations/instances_val2017.json'
