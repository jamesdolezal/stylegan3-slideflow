# Copyright (c) 2021, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

import imgui
from array import array
from gui_utils import imgui_utils

#----------------------------------------------------------------------------

class PredictionWidget:
    def __init__(self, viz):
        self.viz            = viz

    @imgui_utils.scoped_by_object_id
    def __call__(self, show=True):
        viz = self.viz
        if viz._predictions is not None and isinstance(viz._predictions, list):
            for p, _pred_array in enumerate(viz._predictions):
                imgui.text(f'Pred {p}')
                imgui.same_line(viz.label_w)
                imgui.core.plot_histogram('##pred', array('f', _pred_array))
        elif viz._predictions is not None:
            imgui.text('Prediction')
            imgui.same_line(viz.label_w)
            imgui.core.plot_histogram('##pred', array('f', viz._predictions))