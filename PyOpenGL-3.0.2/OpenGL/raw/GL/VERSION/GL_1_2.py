'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_1_2'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_VERSION_GL_1_2',False)
_p.unpack_constants( """GL_UNSIGNED_BYTE_3_3_2 0x8032
GL_UNSIGNED_SHORT_4_4_4_4 0x8033
GL_UNSIGNED_SHORT_5_5_5_1 0x8034
GL_UNSIGNED_INT_8_8_8_8 0x8035
GL_UNSIGNED_INT_10_10_10_2 0x8036
GL_TEXTURE_BINDING_3D 0x806A
GL_PACK_SKIP_IMAGES 0x806B
GL_PACK_IMAGE_HEIGHT 0x806C
GL_UNPACK_SKIP_IMAGES 0x806D
GL_UNPACK_IMAGE_HEIGHT 0x806E
GL_TEXTURE_3D 0x806F
GL_PROXY_TEXTURE_3D 0x8070
GL_TEXTURE_DEPTH 0x8071
GL_TEXTURE_WRAP_R 0x8072
GL_MAX_3D_TEXTURE_SIZE 0x8073
GL_UNSIGNED_BYTE_2_3_3_REV 0x8362
GL_UNSIGNED_SHORT_5_6_5 0x8363
GL_UNSIGNED_SHORT_5_6_5_REV 0x8364
GL_UNSIGNED_SHORT_4_4_4_4_REV 0x8365
GL_UNSIGNED_SHORT_1_5_5_5_REV 0x8366
GL_UNSIGNED_INT_8_8_8_8_REV 0x8367
GL_UNSIGNED_INT_2_10_10_10_REV 0x8368
GL_BGR 0x80E0
GL_BGRA 0x80E1
GL_MAX_ELEMENTS_VERTICES 0x80E8
GL_MAX_ELEMENTS_INDICES 0x80E9
GL_CLAMP_TO_EDGE 0x812F
GL_TEXTURE_MIN_LOD 0x813A
GL_TEXTURE_MAX_LOD 0x813B
GL_TEXTURE_BASE_LEVEL 0x813C
GL_TEXTURE_MAX_LEVEL 0x813D
GL_SMOOTH_POINT_SIZE_RANGE 0xB12
GL_SMOOTH_POINT_SIZE_GRANULARITY 0xB13
GL_SMOOTH_LINE_WIDTH_RANGE 0xB22
GL_SMOOTH_LINE_WIDTH_GRANULARITY 0xB23
GL_ALIASED_LINE_WIDTH_RANGE 0x846E
GL_RESCALE_NORMAL 0x803A
GL_LIGHT_MODEL_COLOR_CONTROL 0x81F8
GL_SINGLE_COLOR 0x81F9
GL_SEPARATE_SPECULAR_COLOR 0x81FA
GL_ALIASED_POINT_SIZE_RANGE 0x846D""", globals())
glget.addGLGetConstant( GL_TEXTURE_BINDING_3D, (1,) )
glget.addGLGetConstant( GL_PACK_SKIP_IMAGES, (1,) )
glget.addGLGetConstant( GL_PACK_IMAGE_HEIGHT, (1,) )
glget.addGLGetConstant( GL_UNPACK_SKIP_IMAGES, (1,) )
glget.addGLGetConstant( GL_UNPACK_IMAGE_HEIGHT, (1,) )
glget.addGLGetConstant( GL_TEXTURE_3D, (1,) )
glget.addGLGetConstant( GL_MAX_3D_TEXTURE_SIZE, (1,) )
glget.addGLGetConstant( GL_MAX_ELEMENTS_VERTICES, (1,) )
glget.addGLGetConstant( GL_MAX_ELEMENTS_INDICES, (1,) )
glget.addGLGetConstant( GL_SMOOTH_POINT_SIZE_RANGE, (2,) )
glget.addGLGetConstant( GL_SMOOTH_POINT_SIZE_GRANULARITY, (1,) )
glget.addGLGetConstant( GL_SMOOTH_LINE_WIDTH_RANGE, (2,) )
glget.addGLGetConstant( GL_SMOOTH_LINE_WIDTH_GRANULARITY, (1,) )
glget.addGLGetConstant( GL_ALIASED_LINE_WIDTH_RANGE, (2,) )
glget.addGLGetConstant( GL_RESCALE_NORMAL, (1,) )
glget.addGLGetConstant( GL_LIGHT_MODEL_COLOR_CONTROL, (1,) )
glget.addGLGetConstant( GL_ALIASED_POINT_SIZE_RANGE, (2,) )
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glBlendColor( red,green,blue,alpha ):pass
@_f
@_p.types(None,_cs.GLenum)
def glBlendEquation( mode ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p)
def glDrawRangeElements( mode,start,end,count,type,indices ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexImage3D( target,level,internalformat,width,height,depth,border,format,type,pixels ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage3D( target,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyTexSubImage3D( target,level,xoffset,yoffset,zoffset,x,y,width,height ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glColorTable( target,internalformat,width,format,type,table ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glColorTableParameterfv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glColorTableParameteriv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyColorTable( target,internalformat,x,y,width ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetColorTable( target,format,type,table ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetColorTableParameterfv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetColorTableParameteriv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glColorSubTable( target,start,count,format,type,data ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyColorSubTable( target,start,x,y,width ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glConvolutionFilter1D( target,internalformat,width,format,type,image ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glConvolutionFilter2D( target,internalformat,width,height,format,type,image ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glConvolutionParameterf( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glConvolutionParameterfv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glConvolutionParameteri( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glConvolutionParameteriv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyConvolutionFilter1D( target,internalformat,x,y,width ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyConvolutionFilter2D( target,internalformat,x,y,width,height ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetConvolutionFilter( target,format,type,image ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetConvolutionParameterfv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetConvolutionParameteriv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void_p)
def glGetSeparableFilter( target,format,type,row,column,span ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p,ctypes.c_void_p)
def glSeparableFilter2D( target,internalformat,width,height,format,type,row,column ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLboolean,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetHistogram( target,reset,format,type,values ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetHistogramParameterfv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetHistogramParameteriv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLboolean,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetMinmax( target,reset,format,type,values ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetMinmaxParameterfv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetMinmaxParameteriv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLboolean)
def glHistogram( target,width,internalformat,sink ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLboolean)
def glMinmax( target,internalformat,sink ):pass
@_f
@_p.types(None,_cs.GLenum)
def glResetHistogram( target ):pass
@_f
@_p.types(None,_cs.GLenum)
def glResetMinmax( target ):pass
