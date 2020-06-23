import gl
import sys
import random
print(sys.version)
print(gl.version())
gl.resetdefaults()

# Power 2011
#networks_to_plot = ['Default_mode', 'Auditory', 'Sensorimotor_Hand'];
#networks_to_plot = ['Power2011_Visual_mask'];
#networks_to_plot = ['Power2011_Ventral_attention_mask'];
#networks_to_plot = ['Power2011_Sensorimotor_mouth_mask'];
#networks_to_plot = ['Power2011_Sensorimotor_Hand_mask'];
#networks_to_plot = ['Power2011_Default_mode_mask'];
#networks_to_plot = ['Power2011_Cingulo-opercular_Control_mask'];
#networks_to_plot = ['Power2011_Auditory_mask'];
#networks_to_plot = ['Power2011_Dorsal_attention_mask'];
#networks_to_plot = ['Power2011_Fronto-parietal_Task_Control_mask'];
#networks_to_plot = ['Power2011_Salience_mask'];
#networks_to_plot = ['Power2011_RetrosplenialTemporal_mask'];

# Gordon 2016
#networks_to_plot = ['Gordon2016_Default_mask'];
#networks_to_plot = ['Gordon2016_DorsalAttn_mask'];
#networks_to_plot = ['Gordon2016_SMhand_mask'];
#networks_to_plot = ['Gordon2016_SMmouth_mask'];
#networks_to_plot = ['Gordon2016_VentralAttn_mask'];
#networks_to_plot = ['Gordon2016_FrontoParietal_mask']; 
#networks_to_plot = ['Gordon2016_CinguloOperc_mask']; 
#networks_to_plot = ['Gordon2016_Salience_mask'];
#networks_to_plot = ['Gordon2016_None_mask'];
#networks_to_plot = ['Gordon2016_CinguloParietal_mask'];
networks_to_plot = ['Gordon2016_Auditory_mask'];


gl.loadimage('//cifs.rc.ufl.edu/ufrc/rachaelseidler/tfettrow/Crunch_Code/MR_Templates/MNI_2mm.nii')
gl.opacity(1,10)
rois_plotted=1;
this_index=0;
for this_network in networks_to_plot:
    gl.overlayload("//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/ROIs/"+this_network)
    gl.minmax(rois_plotted,0.01,0.1)
    gl.colorname(rois_plotted,'1red')
    gl.colorfromzero(rois_plotted,1)
    gl.colorbarposition(0)
    # print(this_roi_name + " roi plotted for " + this_roi_network)
    rois_plotted += 1
    this_index += 1
    gl.savebmp("//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/ROIs/"+this_network)





# XXX Not needed right now XXX
#roi_settings_file = open("//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/ROI_settings_Gordon2016.txt", "r")


# def generate_colors(n):
#   rgb_values = []
#   hex_values = []
#   r = int(random.random() * 256)
#   g = int(random.random() * 256)
#   b = int(random.random() * 256)
#   step = 256 / n
#   for _ in range(n):
#     r += step
#     g += step
#     b += step
#     r = int(r) % 256
#     g = int(g) % 256
#     b = int(b) % 256
#     r_hex = hex(r)[2:]
#     g_hex = hex(g)[2:]
#     b_hex = hex(b)[2:]
#     hex_values.append('#' + r_hex + g_hex + b_hex)
#     rgb_values.append((r,g,b))
#   return rgb_values, hex_values
# color_count = 6
# # generate values and print them
# rgb_values, hex_values = generate_colors(len(networks_to_plot))
# print (rgb_values, hex_values)
# show generated colors

# rois_plotted=0;
# for this_roi_line in roi_settings_file:
#   this_roi_name=this_roi_line.split(',')[3]
#   this_roi_network=this_roi_line.split(',')[4]

#   ########## MRIcroGL maxes out at certain number of overlays... not good... implemented this break for testing purposes...
#   if rois_plotted > 5:
#     break

#   if this_roi_network in networks_to_plot:
#     gl.overlayload("//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/ROIs/"+this_roi_name)
#     gl.minmax(rois_plotted,0.01,0.1)
#     gl.colorname(rois_plotted,'1red')
#     gl.colorfromzero(rois_plotted,1)
#     gl.colorbarposition(0)
#     print(this_roi_name + " roi plotted for " + this_roi_network)
#     rois_plotted += 1
# XXX Not needed right now XXX
