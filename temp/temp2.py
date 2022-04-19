from PIL import Image


from pdf2image import convert_from_path, convert_from_bytes

images = convert_from_path('/Users/yuanzhaoyi/Downloads/xxxxx.pdf')


def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

im0 = None
for p in ['/Users/yuanzhaoyi/Downloads/1.jpg',
             '/Users/yuanzhaoyi/Downloads/2.jpg',
             '/Users/yuanzhaoyi/Downloads/3.jpg',
             '/Users/yuanzhaoyi/Downloads/4.jpg',
             '/Users/yuanzhaoyi/Downloads/5.jpg',
             '/Users/yuanzhaoyi/Downloads/6.jpg']:
    print(p)
    im = Image.open(p)
    if im0:
        im0 = get_concat_v(im0, im)
    else:
        im0 = im

im0.save('/Users/yuanzhaoyi/Downloads/aaa.jpg')
