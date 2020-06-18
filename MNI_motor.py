#Conceptual Fig 
import gl
import sys
print(sys.version)
print(gl.version())
gl.resetdefaults()
gl.loadimage('//cifs.rc.ufl.edu/ufrc/rachaelseidler/tfettrow/Crunch_Code/MR_Templates/Template_4_IXI555_MNI152_GS.nii')

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

OAi_filenames=['C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/OAi_Flat', \
 'C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/OAi_Low', \
'C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/OAi_Med', \
'C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/OAi_Hard' ]

for this_index in range(0,len(OAi_filenames)):
	gl.overlaycloseall()
	gl.overlayload(OAi_filenames[this_index])
	gl.minmax(1, 0, 5)
	gl.colorname (1,"8redyell")
	gl.opacity(1,80)
	#gl.mosaic('l+ h -0.3 v -0.1 a 55 s x r 0')
	gl.mosaic('a 55')
	gl.colorbarposition(0)
	#gl.linewidth(5)
	gl.savebmp(OAi_filenames[this_index])

# YA_filenames=['C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/YA_Flat', \
#  'C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/YA_Low', \
# 'C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/YA_Med', \
# 'C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/YA_Hard' ]

# for this_index in range(0,len(YA_filenames)):
# 	gl.overlaycloseall()
# 	gl.overlayload(YA_filenames[this_index])
# 	gl.minmax(1, 0, 5)
# 	gl.colorname (1,"8redyell")
# 	gl.opacity(1,80)
# 	#gl.mosaic('l+ h -0.3 v -0.1 a 55 s x r 0')
# 	gl.mosaic('a 55')
# 	gl.colorbarposition(0)
# 	#gl.linewidth(5)
# 	gl.savebmp(YA_filenames[this_index])

# WM_filenames=['C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/WM_Flat', \
#  'C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/WM_Low', \
# 'C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/WM_Med', \
# 'C:/Users/tfettrow/Dropbox (UFL)/CrunchReview/Tables_and_Figs/WM_Hard' ]

# for this_index in range(0,len(WM_filenames)):
# 	gl.overlaycloseall()
# 	gl.overlayload(WM_filenames[this_index])
# 	gl.minmax(1, 0, 5)
# 	gl.colorname (1,"8redyell")
# 	gl.opacity(1,80)
# 	#gl.mosaic('l+ h -0.3 v -0.1 a 55 s x r 0')
# 	gl.mosaic('a 55')
# 	gl.colorbarposition(0)
# 	#gl.linewidth(5)
# 	gl.savebmp(WM_filenames[this_index])
