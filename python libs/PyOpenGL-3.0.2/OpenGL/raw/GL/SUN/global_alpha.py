'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SUN_global_alpha'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SUN_global_alpha',False)
_p.unpack_constants( """GL_GLOBAL_ALPHA_SUN 0x81D9
GL_GLOBAL_ALPHA_FACTOR_SUN 0x81DA""", globals())
glget.addGLGetConstant( GL_GLOBAL_ALPHA_FACTOR_SUN, (1,) )
@_f
@_p.types(None,_cs.GLbyte)
def glGlobalAlphaFactorbSUN( factor ):pass
@_f
@_p.types(None,_cs.GLshort)
def glGlobalAlphaFactorsSUN( factor ):pass
@_f
@_p.types(None,_cs.GLint)
def glGlobalAlphaFactoriSUN( factor ):pass
@_f
@_p.types(None,_cs.GLfloat)
def glGlobalAlphaFactorfSUN( factor ):pass
@_f
@_p.types(None,_cs.GLdouble)
def glGlobalAlphaFactordSUN( factor ):pass
@_f
@_p.types(None,_cs.GLubyte)
def glGlobalAlphaFactorubSUN( factor ):pass
@_f
@_p.types(None,_cs.GLushort)
def glGlobalAlphaFactorusSUN( factor ):pass
@_f
@_p.types(None,_cs.GLuint)
def glGlobalAlphaFactoruiSUN( factor ):pass


def glInitGlobalAlphaSUN():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
