import struct
import numpy as np
import visualization as v


def raw_file_idx3_process(file_path):
    with open(file_path, 'rb') as f:
        binary_data = f.read()
        off_set = 0
        fmt_header = '>iiii'
        magic_number, num_images, num_rows, num_cols = struct.unpack_from(fmt_header, binary_data, off_set)

        image_size = num_rows * num_cols
        off_set += struct.calcsize(fmt_header)
        fmt_image = '>' + str(image_size) + 'B'
        images = np.empty((num_images, 1,  num_rows, num_cols))

        print("\nfile idx3 decoding:")
        b = v.Progress_bar()
        for i in range(num_images):
            b.bar(i, num_images, "Preprocessed ")
            temp = np.array(struct.unpack_from(fmt_image, binary_data, off_set)).reshape((num_rows, num_cols)).reshape(-1,1)
            temp = temp / 255
            temp = temp.reshape(1, 28, 28)
            images[i][0] = temp
            off_set += struct.calcsize(fmt_image)
    return images


def raw_file_idx1_process(file_path):
    with open(file_path, 'rb') as f:
        binary_data = f.read()
        off_set = 0
        fmt_header = '>ii'
        magic_number, num_labels = struct.unpack_from(fmt_header, binary_data, off_set)

        off_set += struct.calcsize(fmt_header)
        fmt_label = '>B'
        labels = np.empty(num_labels)

        print("\nfile idx1 decoding:")
        b = v.Progress_bar()
        for i in range(num_labels):
            b.bar(i, num_labels, "Preprocessed ")
            labels[i] = np.array(struct.unpack_from(fmt_label, binary_data, off_set), dtype=np.int)
            off_set += struct.calcsize(fmt_label)
    return labels

