def resize_keypoint(keypoint, input_shape, output_shape):
    """Change values of keypoint according to paramters for resizing an image.

    The shape of keypoint is :math:`(K, 3)`. :math:`K` is the number of
    keypoint in the image.
    The last dimension is composed of :obj:`(x, y, valid)` in this order.
    These are discriptions of a corresponding keypoint.
    :obj;`x` and :obj:`y` are coordinates of the keypoint. :obj:`valid`
    is whether the keypoint is visible in the image or not.

    Args:
        keypoint (~numpy.ndarray): keypoint in the image. This can be
            either a float or integer array. Please see description
            above for more detail.
        input_shape (tuple): A tuple of length 2. The height and the width
            of the image before resized.
        output_shape (tuple): A tuple of length 2. The height and the width
            of the image after resized.

    Returns:
        ~numpy.ndarray:
        keypoint rescaled according to the given image shapes.

    """
    keypoint = keypoint.copy()
    h_scale = float(output_shape[1]) / input_shape[1]
    v_scale = float(output_shape[0]) / input_shape[0]
    keypoint[:, 0] = h_scale * keypoint[:, 0]
    keypoint[:, 1] = v_scale * keypoint[:, 1]
    return keypoint
