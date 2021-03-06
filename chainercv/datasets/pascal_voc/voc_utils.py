import os

from chainer.dataset import download

from chainercv import utils


root = 'pfnet/chainercv/pascal_voc'
urls = {
    '2012': 'http://host.robots.ox.ac.uk/pascal/VOC/voc2012/'
    'VOCtrainval_11-May-2012.tar',
    '2007': 'http://host.robots.ox.ac.uk/pascal/VOC/voc2007/'
    'VOCtrainval_06-Nov-2007.tar',
    '2007_test': 'http://host.robots.ox.ac.uk/pascal/VOC/voc2007/'
    'VOCtest_06-Nov-2007.tar'
}


def get_pascal_voc(year, mode):
    if year not in urls:
        raise ValueError
    key = year

    if mode == 'test' and year == '2007':
        key = '2007_test'

    data_root = download.get_dataset_directory(root)
    base_path = os.path.join(data_root, 'VOCdevkit/VOC{}'.format(year))
    mode_file = os.path.join(base_path, 'ImageSets/Main/{}.txt'.format(mode))
    if os.path.exists(mode_file):
        # skip downloading
        return base_path

    download_file_path = utils.cached_download(urls[key])
    ext = os.path.splitext(urls[key])[1]
    utils.extractall(download_file_path, data_root, ext)
    return base_path


pascal_voc_labels = (
    'background',
    'aeroplane',
    'bicycle',
    'bird',
    'boat',
    'bottle',
    'bus',
    'car',
    'cat',
    'chair',
    'cow',
    'diningtable',
    'dog',
    'horse',
    'motorbike',
    'person',
    'pottedplant',
    'sheep',
    'sofa',
    'train',
    'tvmonitor')
