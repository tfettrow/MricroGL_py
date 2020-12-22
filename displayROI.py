import gl
import sys
import random
print(sys.version)
print(gl.version())
gl.resetdefaults()

rois_to_plot = ['neurosynth_acc_gmMasked', 'neurosynth_dlpfc_left_gmMasked', 'neurosynth_dlpfc_right_gmMasked']
# rois_to_plot = ['neurosynth_acc_mask', 'neurosynth_dlpfc_left_mask', 'neurosynth_dlpfc_right_mask']
# rois_to_plot = ['left_dlpfc', 'right_dlpfc', 'left_acc', 'right_acc']
######################################

gl.loadimage('//exasmb.rc.ufl.edu/blue/rachaelseidler/tfettrow/Crunch_Code/MR_Templates/MNI_2mm.nii')

gl.opacity(1,1)
######################################
# rois_plotted=1;
# this_index=0;
for this_roi in rois_to_plot:
    # gl.loadimage('//exasmb.rc.ufl.edu/blue/rachaelseidler/tfettrow/Crunch_Code/MR_Templates/MNI_2mm.nii')
    # gl.opacity(1,10)
    
    # gl.mosaic('a -36 -32 -28 -24 -20 -16 -10 -6 -2; 2 6 10 14 18 22 26 30 34; 38 42 46 50 54 58 62 66 70')
    # gl.mosaic("A R 0 C R 0 S R 0; A R -0 C R -0 S R -0");
    gl.mosaic("A R 0");
  
    gl.overlayload("//exasmb.rc.ufl.edu/blue/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/ROIs/"+this_roi)
    #gl.minmax(0,.01,.01)
    gl.colorbarposition(0)

    gl.colornode(1,2,255,0,0,255,255) # blue
    gl.colornode(2,2,255,255,0,0,255) # red
    gl.colornode(3,2,255,0,255,0,255) # green
    # gl.colornode(4,2,255,0,88,0,255) #darkgreen
    gl.backcolor(255,255,255)

    gl.savebmp("//exasmb.rc.ufl.edu/blue/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/ROIs/"+this_roi)
