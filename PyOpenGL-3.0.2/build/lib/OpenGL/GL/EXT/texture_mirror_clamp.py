'''OpenGL extension EXT.texture_mirror_clamp

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.texture_mirror_clamp to provide a more 
Python-friendly API

Overview (from the spec)
	
	EXT_texture_mirror_clamp extends the set of texture wrap modes to
	include three modes (GL_MIRROR_CLAMP_EXT, GL_MIRROR_CLAMP_TO_EDGE_EXT,
	GL_MIRROR_CLAMP_TO_BORDER_EXT) that effectively use a texture map
	twice as large as the original image in which the additional half
	of the new image is a mirror image of the original image.
	
	This new mode relaxes the need to generate images whose opposite
	edges match by using the original image to generate a matching
	"mirror image".  This mode allows the texture to be mirrored only
	once in the negative s, t, and r directions.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/texture_mirror_clamp.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.texture_mirror_clamp import *
### END AUTOGENERATED SECTION