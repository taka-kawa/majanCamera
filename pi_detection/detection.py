import cv2
import keras
import threading
from keras.applications.imagenet_utils import preprocess_input
from keras.backend.tensorflow_backend import set_session
from keras.models import Model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imread
import tensorflow as tf

from pi_detection.config import config as c

from .ssd import SSD512, MultiboxLoss, BBoxUtility

class Detector:
    _instance = None
    _lock = threading.Lock()
    def __init__(self):
        pass

    def __new__(cls):
        with cls._lock:
            # 初期設定(最初の呼び出しだけ)
            if cls._instance is None:
                cls.config = tf.ConfigProto()
                cls.config.gpu_options.per_process_gpu_memory_fraction = 0.45
                set_session(tf.Session(config=cls.config))
                cls.voc_classes = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', \
                                    'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', \
                                    's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', \
                                    'e', 's', 'w', 'n', 'haku', 'hatsu', 'chun']
                cls.NUM_CLASSES = len(cls.voc_classes) + 1
                cls.input_shape=(512, 512, 3)
                cls.model = SSD512(cls.input_shape, num_classes=cls.NUM_CLASSES)
                cls.model.load_weights(c['detection']['weight_path'], by_name=True)
                cls.bbox_util = BBoxUtility(cls.NUM_CLASSES)
                cls._instance = super().__new__(cls)
            return cls._instance

    def load_model(self, model_path):
        """
        モデルをロードするメソッド
        将来的にモデルを新しくしていくため
        """
        # TODO 未実装
        self.model.load_weights(model_path, by_name=True)

    def detect(self, img_path):
        """
        イメージをもらって結果を返す
        return
        """
        # TODO 一個しかこない
        inputs = []
        images = []

        img = image.load_img(img_path, target_size=(512, 512))
        img = image.img_to_array(img)
        images.append(imread(img_path))
        inputs.append(img.copy())
        inputs = preprocess_input(np.array(inputs))

        # 予測
        preds = self.model.predict(inputs, batch_size=1, verbose=1)
        # 結果
        results = self.bbox_util.detection_out(preds)
        # 予測結果の格納
        det_label = results[0][:, 0]
        det_conf = results[0][:, 1]
        det_xmin = results[0][:, 2]
        det_ymin = results[0][:, 3]
        det_xmax = results[0][:, 4]
        det_ymax = results[0][:, 5]
        # Get detections with confidence higher than 0.6.
        # TODO 14牌にする
        top_indices = [i for i, conf in enumerate(det_conf) if conf >= 0.6]
        # 上位14牌の情報
        top_conf = det_conf[top_indices]
        top_label_indices = det_label[top_indices].tolist()
        top_xmin = det_xmin[top_indices]
        top_ymin = det_ymin[top_indices]
        top_xmax = det_xmax[top_indices]
        top_ymax = det_ymax[top_indices]
        # 返すjsonを作成
        result = {"pis":[]}
        for i, label_num in enumerate(top_label_indices):
            result['pis'].append({"name":self.voc_classes[int(label_num)],
                                  "xmin":top_xmin[i],
                                  "ymin":top_ymin[i],
                                  "xmax":top_xmax[i],
                                  "ymax":top_ymax[i],
                                  "conf":top_conf[i]})
        return result

