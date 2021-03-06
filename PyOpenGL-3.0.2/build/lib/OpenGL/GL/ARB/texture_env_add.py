'''OpenGL extension ARB.texture_env_add

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_env_add to provide a more 
Python-friendly API

Overview (from the spec)
	
	New texture environment function ADD is supported with the following
	equation:
	                    Cv = min(1, Cf + Ct)
	
	New function may be specified by calling TexEnv with ADD token.
	
	One possible application is to add a specular highlight texture to
	a Gouraud-shaded primitive to emulate Phong shading, in a single
	pass.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_env_add.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.texture_env_add import *
### END AUTOGENERATED SECTION