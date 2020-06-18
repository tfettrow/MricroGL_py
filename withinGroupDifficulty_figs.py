#Conceptual Fig 
import gl
import sys
print(sys.version)
print(gl.version())
gl.resetdefaults()

#gl.loadimage('//cifs.rc.ufl.edu/ufrc/rachaelseidler/tfettrow/Crunch_Code/MR_Templates/Template_4_IXI555_MNI152_GS.nii')
gl.loadimage('//cifs.rc.ufl.edu/ufrc/rachaelseidler/tfettrow/Crunch_Code/MR_Templates/MNI_2mm.nii')
OA_filename = ['//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/Level2_Results/MRI_files/05_MotorImagery/oldadult/spmT_0002.nii']
#OA_filename = ['//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/Level2_Results/MRI_files/05_MotorImagery/oldadult/spmT_0003.nii']
#OA_filename = ['//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/Level2_Results/MRI_files/05_MotorImagery/oldadult/spmT_0004.nii']
#OA_filename = ['//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/Level2_Results/MRI_files/05_MotorImagery/oldadult/spmT_0005.nii']

gl.overlayload(OA_filename[0])
gl.minmax(1, 1, 5)
gl.colorname (1,"8redyell")
gl.opacity(1,80)
#gl.mosaic('l+ h -0.3 v -0.1 a 55 s x r 0')
gl.mosaic('a 55')
gl.colorbarposition(0)
#gl.linewidth(5)
gl.savebmp(OA_filename[0])

gl.loadimage('//cifs.rc.ufl.edu/ufrc/rachaelseidler/tfettrow/Crunch_Code/MR_Templates/MNI_2mm.nii')
#YA_filename = ['//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/Level2_Results/MRI_files/05_MotorImagery/youngadult/spmT_0002.nii']
#YA_filename = ['//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/Level2_Results/MRI_files/05_MotorImagery/youngadult/spmT_0003.nii']
#YA_filename = ['//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/Level2_Results/MRI_files/05_MotorImagery/youngadult/spmT_0004.nii']
YA_filename = ['//cifs.rc.ufl.edu/ufrc/rachaelseidler/share/FromExternal/Research_Projects_UF/CRUNCH/MiM_Data/Level2_Results/MRI_files/05_MotorImagery/youngadult/spmT_0005.nii']

gl.overlayload(YA_filename[0])
gl.minmax(1, 1, 5)
gl.colorname (1,"8redyell")
gl.opacity(1,80)
#gl.mosaic('l+ h -0.3 v -0.1 a 55 s x r 0')
gl.mosaic('a 55')
gl.colorbarposition(0)
#gl.linewidth(5)
gl.savebmp(YA_filename[0])


# OAc_filenames=['C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/OAc_Flat', \
#  'C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/OAc_Low', \
# 'C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/OAc_Med', \
# 'C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/OAc_Hard' ]

# for this_index in range(0,len(OAc_filenames)):
# 	gl.overlaycloseall()
# 	gl.overlayload(OAc_filenames[this_index])
# 	gl.minmax(1, 0, 5)
# 	gl.colorname (1,"8redyell")
# 	gl.opacity(1,80)
# 	#gl.mosaic('l+ h -0.3 v -0.1 a 55 s x r 0')
# 	gl.mosaic('a 55')
# 	gl.colorbarposition(0)
# 	#gl.linewidth(5)
# 	gl.savebmp(OAc_filenames[this_index])