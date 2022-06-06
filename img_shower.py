import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
from scrollview import ScrollView

itk_image = sitk.ReadImage('data/KA53_20131213_nerka_guz_tetnice_ukm/D14F982C/guz nerka i tetnice/CT_S4_A1_SliceThickness1_25.mhd')
image_array = sitk.GetArrayViewFromImage(itk_image)

# print the image's dimensions
print(image_array.shape)

# plot the image

fig, ax = plt.subplots()
ScrollView(image_array).plot(ax)
plt.show()
