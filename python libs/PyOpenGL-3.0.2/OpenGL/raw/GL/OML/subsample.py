'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_OML_subsample'
_p.unpack_constants( """GL_FORMAT_SUBSAMPLE_24_24_OML 0x8982
GL_FORMAT_SUBSAMPLE_244_244_OML 0x8983""", globals())


def glInitSubsampleOML():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )