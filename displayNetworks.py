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
#networks_to_plot = ['Gordon2016_Auditory_mask'];
#networks_to_plot = ['Gordon2016_Visual_mask'];
# networks_to_plot = ['Gordon2016_Visual_mask','Gordon2016_CinguloParietal_mask','Gordon2016_Salience_mask','Gordon2016_CinguloOperc_mask','Gordon2016_FrontoParietal_mask','Gordon2016_VentralAttn_mask','Gordon2016_SMmouth_mask','Gordon2016_SMhand_mask','Gordon2016_DorsalAttn_mask','Gordon2016_Default_mask','Gordon2016_Auditory_mask','Gordon2016_None_mask'];
# networks_to_plot = ['Gordon2016_SMhand_mask', 'Gordon2016_Default_mask', 'Gordon2016_SMmouth_mask', 'Gordon2016_Auditory_mask', 'Gordon2016_DorsalAttn_mask', 'Gordon2016_Salience_mask', 'Gordon2016_Visual_mask', 'Gordon2016_CinguloOperc_mask']
#left_hand_network_mask','medial_prefrontal_cortex_post_cingulate_network_mask','right_mouth_network_mask','left_aud_cortex_network_mask','right_post_ips_network_mask','left_insular_network_mask','visual_cortex_network_mask','dACC_network_mask'];

# s-v Networks
#networks_to_plot = ['left_hand_network_mask'];
#networks_to_plot = ['left_mouth_network_mask'];
#networks_to_plot = ['left_aud_cortex_network_mask'];
#networks_to_plot = ['medial_prefrontal_cortex_network_mask'];
#networks_to_plot = ['left_post_ips_network_mask'];
#networks_to_plot = ['left_insular_network_mask'];
#networks_to_plot = ['visual_cortex_network_mask'];
#networks_to_plot = ['left_ips_network_mask'];
#networks_to_plot = ['right_thalamus_network_mask'];
#networks_to_plot = ['left_rsc_network_mask'];
#networks_to_plot = ['post_cingulate_network_mask'];
#networks_to_plot = ['right_aud_cortex_network_mask'];
#networks_to_plot = ['right_post_ips_network_mask'];
#networks_to_plot = ['right_insular_network_mask'];
#networks_to_plot = ['right_ips_network_mask'];
#networks_to_plot = ['right_hand_network_mask'];
#networks_to_plot = ['right_mouth_network_mask'];
#networks_to_plot = ['right_rsc_network_mask'];
#networks_to_plot = ['left_dlpfc_network_mask'];
#networks_to_plot = ['right_dlpfc_network_mask'];
#networks_to_plot = ['left_acc_network_mask'];
#networks_to_plot = ['right_acc_network_mask'];
#networks_to_plot = ['dACC_network_mask']; 
#networks_to_plot = ['mpc_and_pc_network_mask'];

#color_array = ['1red','2green','3blue','4hot','7cool','8redyell','copper','NIH','jet']
#color_array = ['1red','distinct1']
# networks_to_plot = ['left_hand_network_mask','medial_prefrontal_cortex_post_cingulate_network_mask','right_mouth_network_mask','left_aud_cortex_network_mask','right_post_ips_network_mask','left_insular_network_mask','visual_cortex_network_mask','dACC_network_mask','left_dlpfc_network_mask'];
# networks_to_plot = ['left_hand_network_mask','medial_prefrontal_cortex_post_cingulate_network_mask','right_mouth_network_mask','left_aud_cortex_network_mask','right_post_ips_network_mask','left_insular_network_mask','visual_cortex_network_mask','dACC_network_mask','left_dlpfc_network_mask','left_acc_network_mask','right_dlpfc_network_mask','right_acc_network_mask'];
#networks_to_plot = ['left_hand_network_mask','medial_prefrontal_cortex_post_cingulate_network_mask','right_mouth_network_mask','left_aud_cortex_network_mask','right_post_ips_network_mask','left_insular_network_mask','visual_cortex_network_mask','dACC_network_mask'];
# networks_to_plot = ['medial_prefrontal_cortex_post_cingulate_network_CBmask','right_post_ips_network_CBmask','visual_cortex_network_CBmask','dACC_network_CBmask','right_dlpfc_network_CBmask'];
# networks_to_plot = ['left_acc_network_mask', 'right_acc_network_mask']
networks_to_plot = ['left_dlpfc_network_mask', 'right_dlpfc_network_mask']
######################################
# glass brain 
# gl.shadername('Shell')
# gl.shaderadjust('boundThresh', 0.35)
# gl.shaderadjust('edgeThresh', 0.7)
# gl.shaderadjust('edgeBoundMix',0.55)
# gl.shaderadjust('colorTemp', 0.8)
# gl.backcolor(255, 255,255)
gl.loadimage('//exasmb.rc.ufl.edu/blue/rachaelseidler/tfettrow/Crunch_Code/MR_Templates/MNI_2mm.nii')
# gl.loadimage('//exasmb.rc.ufl.edu/blue/rachaelseidler/tfettrow/Crunch_Code/MR_Templates/SUIT_Nobrainstem_2mm.nii')
# gl.loadimage('//exasmb.rc.ufl.edu/blue/rachaelseidler/tfettrow/Crunch_Code/spm_TF/spm12/toolbox/suit/atlas/Cerebellum-SUIT-maxprob.nii')

gl.opacity(1,10)
######################################
# rois_plotted=1;
# this_index=0;
for this_network in networks_to_plot:
    # gl.loadimage('//exasmb.rc.ufl.edu/blue/rachaelseidler/tfettrow/Crunch_Code/MR_Templates/MNI_2mm.nii')
    # gl.opacity(1,10)
    
    gl.mosaic('a -36 -32 -28 -24 -20 -16 -10 -6 -2; 2 6 10 14 18 22 26 30 34; 38 42 46 50 54 58 62 66 70')
    # gl.mosaic("A R 0 C R 0 S R 0; A R -0 C R -0 S R -0");
  
    gl.overlayload("//exasmb.rc.ufl.edu/blue/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/ROIs/"+this_network)
    #gl.minmax(1,.01,.01)
    #gl.minmax(2,.01,.01)
    #gl.minmax(3,.01,.01)
    #gl.minmax(4,.01,.01)
    #gl.minmax(5,.01,.01)
    #gl.minmax(6,.01,.01)
    #gl.minmax(7,.01,.05)
    #gl.minmax(8,.01,1)
    #gl.minmax(9,.02,.025)
    # print(color_array[rois_plotted])
    #gl.colorname(rois_plotted,color_array[this_index])
    # gl.colorfromzero(rois_plotted,1)
    gl.colorbarposition(0)
    # print(rois_plotted)

    #gl.coloreditor(1)
    #gl.colorname(0,'Grayscale')
    #colornode (built-in function): 
    #colornode(layer, index, intensity, r, g, b, a) -> Adjust color scheme for image.

    gl.colornode(1,2,255,0,0,255,255) # blue
    gl.colornode(2,2,255,255,0,0,255) # red
    #gl.colornode(3,2,255,0,255,0,255) # green
    #gl.colornode(4,2,255,0,0,44,255) #black?
    #gl.colornode(5,2,255,255,26,185,255) #pink
    #gl.colornode(6,2,255,255,211,0,255) #yellow
    #gl.colornode(7,2,255,0,88,0,255) #darkgreen
    #gl.colornode(8,2,255,132,132,255,255) #light blue
    # gl.colornode(9,2,255,158,79,70,255) #light brown
    # gl.colornode(10,2,255,0,255,194,255) #light tiel
    # gl.colornode(11,2,255,0,132,150,255) #dark tiel
    # gl.colornode(12,2,255,0,0,123,255) #purple
 
    # gl.colornode(1,2,255,255,0,0,255) # red
    # gl.colornode(2,2,255,255,26,185,255) #pink
    # gl.colornode(3,2,255,0,88,0,255) #darkgreen
    # gl.colornode(4,2,255,132,132,255,255) #light blue
    # gl.colornode(5,2,255,158,79,70,255) #light brown
    


    gl.savebmp("//exasmb.rc.ufl.edu/blue/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/ROIs/"+this_network)
    
    # print(this_roi_name + " roi plotted for " + this_roi_network)
    # rois_plotted += 1
    # this_index += 1




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
