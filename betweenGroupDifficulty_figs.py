#Conceptual Fig 
import gl
import sys
print(sys.version)
print(gl.version())
gl.resetdefaults()

#gl.loadimage('//cifs.rc.ufl.edu/ufrc/rachaelseidler/tfettrow/Crunch_Code/MR_Templates/Template_4_IXI555_MNI152_GS.nii')
gl.loadimage('//cifs.rc.ufl.edu/ufrc/rachaelseidler/tfettrow/Crunch_Code/MR_Templates/MNI_2mm.nii')
# OA_filename = ['//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/twosampTtest_Results/MRI_files/05_MotorImagery/flat/spmT_0002.nii']
# OA_filename = ['//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/twosampTtest_Results/MRI_files/05_MotorImagery/low/spmT_0002.nii']
# OA_filename = ['//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/twosampTtest_Results/MRI_files/05_MotorImagery/medium/spmT_0002.nii']
OA_filename = ['//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/twosampTtest_Results/MRI_files/05_MotorImagery/high/spmT_0002.nii']

gl.overlayload(OA_filename[0])
gl.minmax(1, 1, 5)
gl.colorname (1,"8redyell")
gl.opacity(1,80)
#gl.mosaic('l+ h -0.3 v -0.1 a 55 s x r 0')
gl.mosaic('a 55')
gl.colorbarposition(0)
#gl.linewidth(5)
gl.savebmp(OA_filename[0])

