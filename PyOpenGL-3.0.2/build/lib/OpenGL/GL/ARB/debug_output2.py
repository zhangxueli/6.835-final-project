'''OpenGL extension ARB.debug_output2

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.debug_output2 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension specifies how the existing ARB_debug_output functionality
	operates in both debug and non-debug contexts to allow the inclusion of
	ARB_debug_output into the OpenGL 4.3 core specification.
	
	Some existing implementations of ARB_debug_output only expose the
	ARB_debug_output extension string if the context was created with the
	debug flag {GLX|WGL}_CONTEXT_DEBUG_BIT_ARB as specified in
	{GLX|WGL}_ARB_create_context. The behavior is not obvious when the
	functionality is brought into the OpenGL core specification because the
	extension string and function entry points must always exist.
	
	This extension modifies the existing ARB_debug_output extension to
	allow implementations to always have an empty message log. The
	specific messages written to the message log or callback routines
	are already implementation defined, so this specification simply
	makes it explicit that it's fine for there to be zero messages
	generated, which is useful if the context is non-debug.
	
	Debug output can be enabled and disabled by changing the DEBUG_OUTPUT
	state. It is implementation defined how much debug output is generated
	if the context was created without the CONTEXT_DEBUG_BIT set. There is
	a new query bit added to the existing GL_CONTEXT_FLAGS state to specify
	whether the context was created with debug enabled.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/debug_output2.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.debug_output2 import *
### END AUTOGENERATED SECTION