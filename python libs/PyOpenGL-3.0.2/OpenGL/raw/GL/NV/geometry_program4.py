'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_geometry_program4'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_geometry_program4',False)
_p.unpack_constants( """GL_LINES_ADJACENCY_EXT 0xA
GL_LINE_STRIP_ADJACENCY_EXT 0xB
GL_TRIANGLES_ADJACENCY_EXT 0xC
GL_TRIANGLE_STRIP_ADJACENCY_EXT 0xD
GL_GEOMETRY_PROGRAM_NV 0x8C26
GL_MAX_PROGRAM_OUTPUT_VERTICES_NV 0x8C27
GL_MAX_PROGRAM_TOTAL_OUTPUT_COMPONENTS_NV 0x8C28
GL_GEOMETRY_VERTICES_OUT_EXT 0x8DDA
GL_GEOMETRY_INPUT_TYPE_EXT 0x8DDB
GL_GEOMETRY_OUTPUT_TYPE_EXT 0x8DDC
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT 0x8C29
GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT 0x8DA7
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT 0x8DA8
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT 0x8DA9
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT 0x8CD4
GL_PROGRAM_POINT_SIZE_EXT 0x8642""", globals())
glget.addGLGetConstant( GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT, (1,) )
glget.addGLGetConstant( GL_PROGRAM_POINT_SIZE_EXT, (1,) )
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glProgramVertexLimitNV( target,limit ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glFramebufferTextureEXT( target,attachment,texture,level ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint)
def glFramebufferTextureLayerEXT( target,attachment,texture,level,layer ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLenum)
def glFramebufferTextureFaceEXT( target,attachment,texture,level,face ):pass


def glInitGeometryProgram4NV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )