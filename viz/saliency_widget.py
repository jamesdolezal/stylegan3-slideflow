# Copyright (c) 2021, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

import imgui
from gui_utils import imgui_utils
import slideflow.grad as grad

#----------------------------------------------------------------------------

class SaliencyWidget:

    def __init__(self, viz):
        self.viz        = viz
        self.enabled    = False
        self.overlay    = False
        self.method_idx = 0
        self._saliency_methods_all = {
            'Vanilla': grad.VANILLA,
            'Vanilla (Smoothed)': grad.VANILLA_SMOOTH,
            'Integrated Gradients': grad.INTEGRATED_GRADIENTS,
            'Integrated Gradients (Smooth)': grad.INTEGRATED_GRADIENTS_SMOOTH,
            'Guided Integrated Gradients': grad.GUIDED_INTEGRATED_GRADIENTS,
            'Guided Integrated Gradients (Smooth)': grad.GUIDED_INTEGRATED_GRADIENTS_SMOOTH,
            'Blur Integrated Gradients': grad.BLUR_INTEGRATED_GRADIENTS,
            'Blur Integrated Gradients (Smooth)': grad.BLUR_INTEGRATED_GRADIENTS_SMOOTH,
            #'XRAI': grad.XRAI,
            #'XRAI (Fast)': grad.XRAI_FAST,
        }
        self._saliency_methods_names = list(self._saliency_methods_all.keys())

    @imgui_utils.scoped_by_object_id
    def __call__(self, show=True):
        viz = self.viz

        if show:
            width = viz.font_size * 15
            height = imgui.get_text_line_height_with_spacing() * 10
            imgui.begin_child('##saliency_options', width=width, height=height, border=False)
            imgui.text('Saliency')
            imgui.same_line(viz.label_w)
            _clicked, self.enabled = imgui.checkbox('Enable', self.enabled)

            imgui.same_line(viz.label_w + viz.font_size * 5)
            with imgui_utils.grayed_out(not self.enabled):
                _clicked, self.overlay = imgui.checkbox('Overlay', self.overlay)

            with imgui_utils.item_width(viz.font_size * 15), imgui_utils.grayed_out(not self.enabled):
                _clicked, self.method_idx = imgui.listbox("##method", self.method_idx, self._saliency_methods_names)

            imgui.end_child()
            imgui.same_line()
            imgui.begin_child('##pred_image', width=-1, height=height, border=False)
            if viz._tex_obj is not None:
                imgui.image(viz._tex_obj.gl_id, viz.tile_px, viz.tile_px)
            imgui.end_child()

        viz.args.show_saliency = self.enabled
        viz.args.saliency_method = self.method_idx
        viz.args.saliency_overlay = self.overlay

#----------------------------------------------------------------------------
