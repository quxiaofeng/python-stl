'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_EXT_texture_mirror_clamp'
_p.unpack_constants( """GL_MIRROR_CLAMP_EXT 0x8742
GL_MIRROR_CLAMP_TO_EDGE_EXT 0x8743
GL_MIRROR_CLAMP_TO_BORDER_EXT 0x8912""", globals())


def glInitTextureMirrorClampEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
