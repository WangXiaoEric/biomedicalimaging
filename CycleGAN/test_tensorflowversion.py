import tensorflow as tf
print(tf.__version__)


print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print(tf.test.is_gpu_available())