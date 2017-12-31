import numpy as np
from keras import backend as K
from video_classifier.library.recurrent_networks import VGG16BidirectionalLSTMVideoClassifier
from video_classifier.utility.plot_utils import plot_and_save_history


K.set_image_dim_ordering('tf')


def main():
    input_dir_path = './very_large_data'
    output_dir_path = './models/UCF-101'
    report_dir_path = './reports/UCF-101'

    np.random.seed(42)

    classifier = VGG16BidirectionalLSTMVideoClassifier()

    history = classifier.fit(data_dir_path=input_dir_path, model_dir_path=output_dir_path)

    plot_and_save_history(history, VGG16BidirectionalLSTMVideoClassifier.model_name,
                          report_dir_path + '/' + VGG16BidirectionalLSTMVideoClassifier.model_name + '-history.png')


if __name__ == '__main__':
    main()
