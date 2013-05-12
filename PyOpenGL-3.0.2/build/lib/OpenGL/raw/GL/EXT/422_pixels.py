'''OpenGL extension EXT.GL_422_pixels

Overview (from the spec)
    
    This extension provides support for converting 422 pixels in host
    memory to 444 pixels as part of the pixel storage operation.
    
    The pixel unpack storage operation treats a 422 pixel as a 2 element
    format where the first element is C (chrominance) and the second
    element is L (luminance). Luminance is present on all pixels; a full
    chrominance value requires two pixels.
    
    The pixel pack storage operation converts RGB to a 422 pixel defined as
    a 2 element format where the first element stored is C (chrominance)
    and the second element stored is L (luminance).  Luminance is present
    on all pixels; a full chrominance value requires two pixels.
    
    Both averaging and non-averaging is supported for green and blue
    assignments for pack and unpack operations.

The official definition of this extension is available here:
    http://oss.sgi.com/projects/ogl-sample/registry/EXT/GL_422_pixels.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_422_EXT = constant.Constant( 'GL_422_EXT', 0x80CC )
GL_422_REV_EXT = constant.Constant( 'GL_422_REV_EXT', 0x80CD )
GL_422_AVERAGE_EXT = constant.Constant( 'GL_422_AVERAGE_EXT', 0x80CE )
GL_422_REV_AVERAGE_EXT = constant.Constant( 'GL_422_REV_AVERAGE_EXT', 0x80CF )


def glInit422PixelsEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( 'GL_EXT_422_pixels' )