import numpy as np
np.float_ = np.float64
import intvalpy as ip
from readDRS2024bin import rawData_instance

from DRSCalibrationData import *

# rawData_instance.plot_bin_by_lvl_frame_all_bins(-0.027, 1)
# rawData_instance.plot_bin_by_lvl_frame_all_bins(-0.027, 1, flag=False)
# rawData_instance.plot_bin_by_lvl_frame_channel(0, 0, 0)
# rawData_instance.plot_bin_by_lvl_frame_channel(0, 0, 0, True)
# for bin in rawData_instance.bins:
#     rawData_instance.plot_bin_by_lvl_frame_channel(bin.lvl, 2, 0, bin.last)

# rawData_instance.hist_bin_by_lvl_frame_all_bins(-0.027, 0)
# rawData_instance.hist_bin_by_lvl_frame_channel(-0.027, 2, 0)
# rawData_instance.hist_bin_by_lvl_frame_channel(0, 2, 0)
# rawData_instance.hist_bin_by_lvl_frame_channel(0, 2, 0, True)
# for bin in rawData_instance.bins:
#     rawData_instance.hist_bin_by_lvl_frame_channel(bin.lvl, 2, 0, bin.last)

# print(f"Date: {rawData_instance.date}")
# print("\n--> Reading directory: ")
# for i in range(len(rawData_instance.bins)):
#     print(f"lvl: {rawData_instance.bins[i].lvl}"
#           f" \n(side: {rawData_instance.bins[i].side};"
#           f" mode: {rawData_instance.bins[i].mode};"
#           f" number of frames: {rawData_instance.bins[i].frame_count})")
#     print(f"\n--> frames of data (1024 x 8):")
#     for j in range(len(rawData_instance.bins[i].frames)):
#         print(f"\n{j + 1} frame:")
#         print(f"{rawData_instance.bins[i].frames[j]}")

# bin1 = rawData_instance.get_bin_by_lvl(0)
# bin2 = rawData_instance.get_bin_by_lvl(0, last=True)
# print(calibration_data_int_by_bin(ch=0, cells=100, fn=bin1))
# print(calibration_data_int_by_bin(ch=0, cells=100, fn=bin2))
# print(calibration_data_int_all_bins(0, 1))

# print(rawData_instance.bins[-2], rawData_instance.bins[-2].lvl, rawData_instance.bins[-2].last)
# print(rawData_instance.bins[-1], rawData_instance.bins[-1].lvl, rawData_instance.bins[-1].last)
#
# print(rawData_instance.get_bin_by_lvl(0, False))
# print(rawData_instance.get_bin_by_lvl(0, True))
# print(rawData_instance.lvls)
