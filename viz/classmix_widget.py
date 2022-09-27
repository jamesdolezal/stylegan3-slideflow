# Copyright (c) 2021, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

import imgui
from ..gui_utils import imgui_utils

#----------------------------------------------------------------------------

class ClassMixingWidget:
    def __init__(self, viz):
        self.viz        = viz
        self.header     = "StyleGAN"
        self.mix_class  = -1
        self.mix_frac   = 1

    @imgui_utils.scoped_by_object_id
    def __call__(self, show=True):
        viz = self.viz

        if show:
            imgui.text('Classmix')
            imgui.same_line(viz.label_w)
            with imgui_utils.item_width(viz.font_size * 2):
                _something, self.mix_class = imgui.input_int('Class', self.mix_class, step=0)
                viz.args.mix_class = self.mix_class

            imgui.same_line(viz.label_w + viz.font_size * 5 + viz.spacing)
            with imgui_utils.item_width(viz.font_size * 8):
                _changed, self.mix_frac = imgui.slider_float('##mix_fraction',
                                                    self.mix_frac,
                                                    min_value=0,
                                                    max_value=1,
                                                    format='Mix %.2f')
                viz.args.mix_frac = self.mix_frac

#----------------------------------------------------------------------------
