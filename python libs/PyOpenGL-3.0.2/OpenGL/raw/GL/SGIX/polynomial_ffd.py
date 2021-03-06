'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_polynomial_ffd'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_polynomial_ffd',False)
_p.unpack_constants( """GL_GEOMETRY_DEFORMATION_SGIX 0x8194
GL_TEXTURE_DEFORMATION_SGIX 0x8195
GL_DEFORMATIONS_MASK_SGIX 0x8196
GL_MAX_DEFORMATION_ORDER_SGIX 0x8197""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLint,_cs.GLint,_cs.GLdouble,_cs.GLdouble,_cs.GLint,_cs.GLint,_cs.GLdouble,_cs.GLdouble,_cs.GLint,_cs.GLint,arrays.GLdoubleArray)
def glDeformationMap3dSGIX( target,u1,u2,ustride,uorder,v1,v2,vstride,vorder,w1,w2,wstride,worder,points ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLint,_cs.GLint,_cs.GLfloat,_cs.GLfloat,_cs.GLint,_cs.GLint,_cs.GLfloat,_cs.GLfloat,_cs.GLint,_cs.GLint,arrays.GLfloatArray)
def glDeformationMap3fSGIX( target,u1,u2,ustride,uorder,v1,v2,vstride,vorder,w1,w2,wstride,worder,points ):pass
@_f
@_p.types(None,_cs.GLbitfield)
def glDeformSGIX( mask ):pass
@_f
@_p.types(None,_cs.GLbitfield)
def glLoadIdentityDeformationMapSGIX( mask ):pass


def glInitPolynomialFfdSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
