'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_EXT_separate_specular_color'
_p.unpack_constants( """GL_LIGHT_MODEL_COLOR_CONTROL_EXT 0x81F8
GL_SINGLE_COLOR_EXT 0x81F9
GL_SEPARATE_SPECULAR_COLOR_EXT 0x81FA""", globals())
glget.addGLGetConstant( GL_LIGHT_MODEL_COLOR_CONTROL_EXT, (1,) )


def glInitSeparateSpecularColorEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
