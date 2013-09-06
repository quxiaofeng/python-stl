# BEGIN GENERATED CONTENT (do not edit below this line)

# This content is generated by ./gengl.py.
# Wrapper for /usr/include/GL/glx.h
from OpenGL import platform, constant
from ctypes import *
c_void = None


# H (/usr/include/GL/glx.h:26)
GLX_VERSION_1_1 = constant.Constant( 'GLX_VERSION_1_1', 1 )
GLX_VERSION_1_2 = constant.Constant( 'GLX_VERSION_1_2', 1 )
GLX_VERSION_1_3 = constant.Constant( 'GLX_VERSION_1_3', 1 )
GLX_VERSION_1_4 = constant.Constant( 'GLX_VERSION_1_4', 1 )
GLX_USE_GL = constant.Constant( 'GLX_USE_GL', 1 )
GLX_BUFFER_SIZE = constant.Constant( 'GLX_BUFFER_SIZE', 2 )
GLX_LEVEL = constant.Constant( 'GLX_LEVEL', 3 )
GLX_RGBA = constant.Constant( 'GLX_RGBA', 4 )
GLX_DOUBLEBUFFER = constant.Constant( 'GLX_DOUBLEBUFFER', 5 )
GLX_STEREO = constant.Constant( 'GLX_STEREO', 6 )
GLX_AUX_BUFFERS = constant.Constant( 'GLX_AUX_BUFFERS', 7 )
GLX_RED_SIZE = constant.Constant( 'GLX_RED_SIZE', 8 )
GLX_GREEN_SIZE = constant.Constant( 'GLX_GREEN_SIZE', 9 )
GLX_BLUE_SIZE = constant.Constant( 'GLX_BLUE_SIZE', 10 )
GLX_ALPHA_SIZE = constant.Constant( 'GLX_ALPHA_SIZE', 11 )
GLX_DEPTH_SIZE = constant.Constant( 'GLX_DEPTH_SIZE', 12 )
GLX_STENCIL_SIZE = constant.Constant( 'GLX_STENCIL_SIZE', 13 )
GLX_ACCUM_RED_SIZE = constant.Constant( 'GLX_ACCUM_RED_SIZE', 14 )
GLX_ACCUM_GREEN_SIZE = constant.Constant( 'GLX_ACCUM_GREEN_SIZE', 15 )
GLX_ACCUM_BLUE_SIZE = constant.Constant( 'GLX_ACCUM_BLUE_SIZE', 16 )
GLX_ACCUM_ALPHA_SIZE = constant.Constant( 'GLX_ACCUM_ALPHA_SIZE', 17 )
GLX_BAD_SCREEN = constant.Constant( 'GLX_BAD_SCREEN', 1 )
GLX_BAD_ATTRIBUTE = constant.Constant( 'GLX_BAD_ATTRIBUTE', 2 )
GLX_NO_EXTENSION = constant.Constant( 'GLX_NO_EXTENSION', 3 )
GLX_BAD_VISUAL = constant.Constant( 'GLX_BAD_VISUAL', 4 )
GLX_BAD_CONTEXT = constant.Constant( 'GLX_BAD_CONTEXT', 5 )
GLX_BAD_VALUE = constant.Constant( 'GLX_BAD_VALUE', 6 )
GLX_BAD_ENUM = constant.Constant( 'GLX_BAD_ENUM', 7 )
GLX_VENDOR = constant.Constant( 'GLX_VENDOR', 1 )
GLX_VERSION = constant.Constant( 'GLX_VERSION', 2 )
GLX_EXTENSIONS = constant.Constant( 'GLX_EXTENSIONS', 3 )
GLX_CONFIG_CAVEAT = constant.Constant( 'GLX_CONFIG_CAVEAT', 32 )
GLX_DONT_CARE = constant.Constant( 'GLX_DONT_CARE', 4294967295 )
GLX_X_VISUAL_TYPE = constant.Constant( 'GLX_X_VISUAL_TYPE', 34 )
GLX_TRANSPARENT_TYPE = constant.Constant( 'GLX_TRANSPARENT_TYPE', 35 )
GLX_TRANSPARENT_INDEX_VALUE = constant.Constant( 'GLX_TRANSPARENT_INDEX_VALUE', 36 )
GLX_TRANSPARENT_RED_VALUE = constant.Constant( 'GLX_TRANSPARENT_RED_VALUE', 37 )
GLX_TRANSPARENT_GREEN_VALUE = constant.Constant( 'GLX_TRANSPARENT_GREEN_VALUE', 38 )
GLX_TRANSPARENT_BLUE_VALUE = constant.Constant( 'GLX_TRANSPARENT_BLUE_VALUE', 39 )
GLX_TRANSPARENT_ALPHA_VALUE = constant.Constant( 'GLX_TRANSPARENT_ALPHA_VALUE', 40 )
GLX_WINDOW_BIT = constant.Constant( 'GLX_WINDOW_BIT', 1 )
GLX_PIXMAP_BIT = constant.Constant( 'GLX_PIXMAP_BIT', 2 )
GLX_PBUFFER_BIT = constant.Constant( 'GLX_PBUFFER_BIT', 4 )
GLX_AUX_BUFFERS_BIT = constant.Constant( 'GLX_AUX_BUFFERS_BIT', 16 )
GLX_FRONT_LEFT_BUFFER_BIT = constant.Constant( 'GLX_FRONT_LEFT_BUFFER_BIT', 1 )
GLX_FRONT_RIGHT_BUFFER_BIT = constant.Constant( 'GLX_FRONT_RIGHT_BUFFER_BIT', 2 )
GLX_BACK_LEFT_BUFFER_BIT = constant.Constant( 'GLX_BACK_LEFT_BUFFER_BIT', 4 )
GLX_BACK_RIGHT_BUFFER_BIT = constant.Constant( 'GLX_BACK_RIGHT_BUFFER_BIT', 8 )
GLX_DEPTH_BUFFER_BIT = constant.Constant( 'GLX_DEPTH_BUFFER_BIT', 32 )
GLX_STENCIL_BUFFER_BIT = constant.Constant( 'GLX_STENCIL_BUFFER_BIT', 64 )
GLX_ACCUM_BUFFER_BIT = constant.Constant( 'GLX_ACCUM_BUFFER_BIT', 128 )
GLX_NONE = constant.Constant( 'GLX_NONE', 32768 )
GLX_SLOW_CONFIG = constant.Constant( 'GLX_SLOW_CONFIG', 32769 )
GLX_TRUE_COLOR = constant.Constant( 'GLX_TRUE_COLOR', 32770 )
GLX_DIRECT_COLOR = constant.Constant( 'GLX_DIRECT_COLOR', 32771 )
GLX_PSEUDO_COLOR = constant.Constant( 'GLX_PSEUDO_COLOR', 32772 )
GLX_STATIC_COLOR = constant.Constant( 'GLX_STATIC_COLOR', 32773 )
GLX_GRAY_SCALE = constant.Constant( 'GLX_GRAY_SCALE', 32774 )
GLX_STATIC_GRAY = constant.Constant( 'GLX_STATIC_GRAY', 32775 )
GLX_TRANSPARENT_RGB = constant.Constant( 'GLX_TRANSPARENT_RGB', 32776 )
GLX_TRANSPARENT_INDEX = constant.Constant( 'GLX_TRANSPARENT_INDEX', 32777 )
GLX_VISUAL_ID = constant.Constant( 'GLX_VISUAL_ID', 32779 )
GLX_SCREEN = constant.Constant( 'GLX_SCREEN', 32780 )
GLX_NON_CONFORMANT_CONFIG = constant.Constant( 'GLX_NON_CONFORMANT_CONFIG', 32781 )
GLX_DRAWABLE_TYPE = constant.Constant( 'GLX_DRAWABLE_TYPE', 32784 )
GLX_RENDER_TYPE = constant.Constant( 'GLX_RENDER_TYPE', 32785 )
GLX_X_RENDERABLE = constant.Constant( 'GLX_X_RENDERABLE', 32786 )
GLX_FBCONFIG_ID = constant.Constant( 'GLX_FBCONFIG_ID', 32787 )
GLX_RGBA_TYPE = constant.Constant( 'GLX_RGBA_TYPE', 32788 )
GLX_COLOR_INDEX_TYPE = constant.Constant( 'GLX_COLOR_INDEX_TYPE', 32789 )
GLX_MAX_PBUFFER_WIDTH = constant.Constant( 'GLX_MAX_PBUFFER_WIDTH', 32790 )
GLX_MAX_PBUFFER_HEIGHT = constant.Constant( 'GLX_MAX_PBUFFER_HEIGHT', 32791 )
GLX_MAX_PBUFFER_PIXELS = constant.Constant( 'GLX_MAX_PBUFFER_PIXELS', 32792 )
GLX_PRESERVED_CONTENTS = constant.Constant( 'GLX_PRESERVED_CONTENTS', 32795 )
GLX_LARGEST_PBUFFER = constant.Constant( 'GLX_LARGEST_PBUFFER', 32796 )
GLX_WIDTH = constant.Constant( 'GLX_WIDTH', 32797 )
GLX_HEIGHT = constant.Constant( 'GLX_HEIGHT', 32798 )
GLX_EVENT_MASK = constant.Constant( 'GLX_EVENT_MASK', 32799 )
GLX_DAMAGED = constant.Constant( 'GLX_DAMAGED', 32800 )
GLX_SAVED = constant.Constant( 'GLX_SAVED', 32801 )
GLX_WINDOW = constant.Constant( 'GLX_WINDOW', 32802 )
GLX_PBUFFER = constant.Constant( 'GLX_PBUFFER', 32803 )
GLX_PBUFFER_HEIGHT = constant.Constant( 'GLX_PBUFFER_HEIGHT', 32832 )
GLX_PBUFFER_WIDTH = constant.Constant( 'GLX_PBUFFER_WIDTH', 32833 )
GLX_RGBA_BIT = constant.Constant( 'GLX_RGBA_BIT', 1 )
GLX_COLOR_INDEX_BIT = constant.Constant( 'GLX_COLOR_INDEX_BIT', 2 )
GLX_PBUFFER_CLOBBER_MASK = constant.Constant( 'GLX_PBUFFER_CLOBBER_MASK', 134217728 )
GLX_SAMPLE_BUFFERS = constant.Constant( 'GLX_SAMPLE_BUFFERS', 100000 )
GLX_SAMPLES = constant.Constant( 'GLX_SAMPLES', 100001 )
class struct___GLXcontextRec(Structure):
    __slots__ = [
    ]
struct___GLXcontextRec._fields_ = [
    ('_opaque_struct', c_int)
]

class struct___GLXcontextRec(Structure):
    __slots__ = [
    ]
struct___GLXcontextRec._fields_ = [
    ('_opaque_struct', c_int)
]

GLXContext = POINTER(struct___GLXcontextRec) 	# /usr/include/GL/glx.h:178
XID = c_ulong 	# /usr/include/X11/X.h:66
GLXPixmap = XID 	# /usr/include/GL/glx.h:179
GLXDrawable = XID 	# /usr/include/GL/glx.h:180
class struct___GLXFBConfigRec(Structure):
    __slots__ = [
    ]
struct___GLXFBConfigRec._fields_ = [
    ('_opaque_struct', c_int)
]

class struct___GLXFBConfigRec(Structure):
    __slots__ = [
    ]
struct___GLXFBConfigRec._fields_ = [
    ('_opaque_struct', c_int)
]

GLXFBConfig = POINTER(struct___GLXFBConfigRec) 	# /usr/include/GL/glx.h:182
GLXFBConfigID = XID 	# /usr/include/GL/glx.h:183
GLXContextID = XID 	# /usr/include/GL/glx.h:184
GLXWindow = XID 	# /usr/include/GL/glx.h:185
GLXPbuffer = XID 	# /usr/include/GL/glx.h:186
GLX_PbufferClobber = constant.Constant( 'GLX_PbufferClobber', 0 )
GLX_BufferSwapComplete = constant.Constant( 'GLX_BufferSwapComplete', 1 )
class struct_anon_103(Structure):
    __slots__ = [
        'visual',
        'visualid',
        'screen',
        'depth',
        'class',
        'red_mask',
        'green_mask',
        'blue_mask',
        'colormap_size',
        'bits_per_rgb',
    ]
class struct_anon_18(Structure):
    __slots__ = [
        'ext_data',
        'visualid',
        'class',
        'red_mask',
        'green_mask',
        'blue_mask',
        'bits_per_rgb',
        'map_entries',
    ]
class struct__XExtData(Structure):
    __slots__ = [
        'number',
        'next',
        'free_private',
        'private_data',
    ]
XPointer = c_char_p 	# /usr/include/X11/Xlib.h:84
struct__XExtData._fields_ = [
    ('number', c_int),
    ('next', POINTER(struct__XExtData)),
    ('free_private', POINTER(CFUNCTYPE(c_int, POINTER(struct__XExtData)))),
    ('private_data', XPointer),
]

XExtData = struct__XExtData 	# /usr/include/X11/Xlib.h:163
VisualID = c_ulong 	# /usr/include/X11/X.h:76
struct_anon_18._fields_ = [
    ('ext_data', POINTER(XExtData)),
    ('visualid', VisualID),
    ('class', c_int),
    ('red_mask', c_ulong),
    ('green_mask', c_ulong),
    ('blue_mask', c_ulong),
    ('bits_per_rgb', c_int),
    ('map_entries', c_int),
]

Visual = struct_anon_18 	# /usr/include/X11/Xlib.h:246
struct_anon_103._fields_ = [
    ('visual', POINTER(Visual)),
    ('visualid', VisualID),
    ('screen', c_int),
    ('depth', c_int),
    ('class', c_int),
    ('red_mask', c_ulong),
    ('green_mask', c_ulong),
    ('blue_mask', c_ulong),
    ('colormap_size', c_int),
    ('bits_per_rgb', c_int),
]

XVisualInfo = struct_anon_103 	# /usr/include/X11/Xutil.h:294
class struct__XDisplay(Structure):
    __slots__ = [
    ]
struct__XDisplay._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__XDisplay(Structure):
    __slots__ = [
    ]
struct__XDisplay._fields_ = [
    ('_opaque_struct', c_int)
]

Display = struct__XDisplay 	# /usr/include/X11/Xlib.h:495
glXChooseVisual = platform.createBaseFunction(
    'glXChooseVisual', dll=platform.GL, resultType=POINTER(XVisualInfo),
    argTypes=[POINTER(Display), c_int, POINTER(c_int)],
    doc='glXChooseVisual( POINTER(Display)(dpy), c_int(screen), POINTER(c_int)(attribList) ) -> POINTER(XVisualInfo)',
    argNames=['dpy', 'screen', 'attribList'],
)

glXCreateContext = platform.createBaseFunction(
    'glXCreateContext', dll=platform.GL, resultType=GLXContext,
    argTypes=[POINTER(Display), POINTER(XVisualInfo), GLXContext, c_int],
    doc='glXCreateContext( POINTER(Display)(dpy), POINTER(XVisualInfo)(vis), GLXContext(shareList), c_int(direct) ) -> GLXContext',
    argNames=['dpy', 'vis', 'shareList', 'direct'],
)

glXDestroyContext = platform.createBaseFunction(
    'glXDestroyContext', dll=platform.GL, resultType=None,
    argTypes=[POINTER(Display), GLXContext],
    doc='glXDestroyContext( POINTER(Display)(dpy), GLXContext(ctx) ) -> None',
    argNames=['dpy', 'ctx'],
)

glXMakeCurrent = platform.createBaseFunction(
    'glXMakeCurrent', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), GLXDrawable, GLXContext],
    doc='glXMakeCurrent( POINTER(Display)(dpy), GLXDrawable(drawable), GLXContext(ctx) ) -> c_int',
    argNames=['dpy', 'drawable', 'ctx'],
)

glXCopyContext = platform.createBaseFunction(
    'glXCopyContext', dll=platform.GL, resultType=None,
    argTypes=[POINTER(Display), GLXContext, GLXContext, c_ulong],
    doc='glXCopyContext( POINTER(Display)(dpy), GLXContext(src), GLXContext(dst), c_ulong(mask) ) -> None',
    argNames=['dpy', 'src', 'dst', 'mask'],
)

glXSwapBuffers = platform.createBaseFunction(
    'glXSwapBuffers', dll=platform.GL, resultType=None,
    argTypes=[POINTER(Display), GLXDrawable],
    doc='glXSwapBuffers( POINTER(Display)(dpy), GLXDrawable(drawable) ) -> None',
    argNames=['dpy', 'drawable'],
)

Pixmap = XID 	# /usr/include/X11/X.h:102
glXCreateGLXPixmap = platform.createBaseFunction(
    'glXCreateGLXPixmap', dll=platform.GL, resultType=GLXPixmap,
    argTypes=[POINTER(Display), POINTER(XVisualInfo), Pixmap],
    doc='glXCreateGLXPixmap( POINTER(Display)(dpy), POINTER(XVisualInfo)(visual), Pixmap(pixmap) ) -> GLXPixmap',
    argNames=['dpy', 'visual', 'pixmap'],
)

glXDestroyGLXPixmap = platform.createBaseFunction(
    'glXDestroyGLXPixmap', dll=platform.GL, resultType=None,
    argTypes=[POINTER(Display), GLXPixmap],
    doc='glXDestroyGLXPixmap( POINTER(Display)(dpy), GLXPixmap(pixmap) ) -> None',
    argNames=['dpy', 'pixmap'],
)

glXQueryExtension = platform.createBaseFunction(
    'glXQueryExtension', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), POINTER(c_int), POINTER(c_int)],
    doc='glXQueryExtension( POINTER(Display)(dpy), POINTER(c_int)(errorb), POINTER(c_int)(event) ) -> c_int',
    argNames=['dpy', 'errorb', 'event'],
)

glXQueryVersion = platform.createBaseFunction(
    'glXQueryVersion', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), POINTER(c_int), POINTER(c_int)],
    doc='glXQueryVersion( POINTER(Display)(dpy), POINTER(c_int)(maj), POINTER(c_int)(min) ) -> c_int',
    argNames=['dpy', 'maj', 'min'],
)

glXIsDirect = platform.createBaseFunction(
    'glXIsDirect', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), GLXContext],
    doc='glXIsDirect( POINTER(Display)(dpy), GLXContext(ctx) ) -> c_int',
    argNames=['dpy', 'ctx'],
)

glXGetConfig = platform.createBaseFunction(
    'glXGetConfig', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), POINTER(XVisualInfo), c_int, POINTER(c_int)],
    doc='glXGetConfig( POINTER(Display)(dpy), POINTER(XVisualInfo)(visual), c_int(attrib), POINTER(c_int)(value) ) -> c_int',
    argNames=['dpy', 'visual', 'attrib', 'value'],
)

glXGetCurrentContext = platform.createBaseFunction(
    'glXGetCurrentContext', dll=platform.GL, resultType=GLXContext,
    argTypes=[],
    doc='glXGetCurrentContext(  ) -> GLXContext',
    argNames=[],
)

glXGetCurrentDrawable = platform.createBaseFunction(
    'glXGetCurrentDrawable', dll=platform.GL, resultType=GLXDrawable,
    argTypes=[],
    doc='glXGetCurrentDrawable(  ) -> GLXDrawable',
    argNames=[],
)

glXWaitGL = platform.createBaseFunction(
    'glXWaitGL', dll=platform.GL, resultType=None,
    argTypes=[],
    doc='glXWaitGL(  ) -> None',
    argNames=[],
)

glXWaitX = platform.createBaseFunction(
    'glXWaitX', dll=platform.GL, resultType=None,
    argTypes=[],
    doc='glXWaitX(  ) -> None',
    argNames=[],
)

Font = XID 	# /usr/include/X11/X.h:100
glXUseXFont = platform.createBaseFunction(
    'glXUseXFont', dll=platform.GL, resultType=None,
    argTypes=[Font, c_int, c_int, c_int],
    doc='glXUseXFont( Font(font), c_int(first), c_int(count), c_int(list) ) -> None',
    argNames=['font', 'first', 'count', 'list'],
)

glXQueryExtensionsString = platform.createBaseFunction(
    'glXQueryExtensionsString', dll=platform.GL, resultType=c_char_p,
    argTypes=[POINTER(Display), c_int],
    doc='glXQueryExtensionsString( POINTER(Display)(dpy), c_int(screen) ) -> c_char_p',
    argNames=['dpy', 'screen'],
)

glXQueryServerString = platform.createBaseFunction(
    'glXQueryServerString', dll=platform.GL, resultType=c_char_p,
    argTypes=[POINTER(Display), c_int, c_int],
    doc='glXQueryServerString( POINTER(Display)(dpy), c_int(screen), c_int(name) ) -> c_char_p',
    argNames=['dpy', 'screen', 'name'],
)

glXGetClientString = platform.createBaseFunction(
    'glXGetClientString', dll=platform.GL, resultType=c_char_p,
    argTypes=[POINTER(Display), c_int],
    doc='glXGetClientString( POINTER(Display)(dpy), c_int(name) ) -> c_char_p',
    argNames=['dpy', 'name'],
)

glXGetCurrentDisplay = platform.createBaseFunction(
    'glXGetCurrentDisplay', dll=platform.GL, resultType=POINTER(Display),
    argTypes=[],
    doc='glXGetCurrentDisplay(  ) -> POINTER(Display)',
    argNames=[],
)

glXChooseFBConfig = platform.createBaseFunction(
    'glXChooseFBConfig', dll=platform.GL, resultType=POINTER(GLXFBConfig),
    argTypes=[POINTER(Display), c_int, POINTER(c_int), POINTER(c_int)],
    doc='glXChooseFBConfig( POINTER(Display)(dpy), c_int(screen), POINTER(c_int)(attribList), POINTER(c_int)(nitems) ) -> POINTER(GLXFBConfig)',
    argNames=['dpy', 'screen', 'attribList', 'nitems'],
)

glXGetFBConfigAttrib = platform.createBaseFunction(
    'glXGetFBConfigAttrib', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), GLXFBConfig, c_int, POINTER(c_int)],
    doc='glXGetFBConfigAttrib( POINTER(Display)(dpy), GLXFBConfig(config), c_int(attribute), POINTER(c_int)(value) ) -> c_int',
    argNames=['dpy', 'config', 'attribute', 'value'],
)

glXGetFBConfigs = platform.createBaseFunction(
    'glXGetFBConfigs', dll=platform.GL, resultType=POINTER(GLXFBConfig),
    argTypes=[POINTER(Display), c_int, POINTER(c_int)],
    doc='glXGetFBConfigs( POINTER(Display)(dpy), c_int(screen), POINTER(c_int)(nelements) ) -> POINTER(GLXFBConfig)',
    argNames=['dpy', 'screen', 'nelements'],
)

glXGetVisualFromFBConfig = platform.createBaseFunction(
    'glXGetVisualFromFBConfig', dll=platform.GL, resultType=POINTER(XVisualInfo),
    argTypes=[POINTER(Display), GLXFBConfig],
    doc='glXGetVisualFromFBConfig( POINTER(Display)(dpy), GLXFBConfig(config) ) -> POINTER(XVisualInfo)',
    argNames=['dpy', 'config'],
)

Window = XID 	# /usr/include/X11/X.h:96
glXCreateWindow = platform.createBaseFunction(
    'glXCreateWindow', dll=platform.GL, resultType=GLXWindow,
    argTypes=[POINTER(Display), GLXFBConfig, Window, POINTER(c_int)],
    doc='glXCreateWindow( POINTER(Display)(dpy), GLXFBConfig(config), Window(win), POINTER(c_int)(attribList) ) -> GLXWindow',
    argNames=['dpy', 'config', 'win', 'attribList'],
)

glXDestroyWindow = platform.createBaseFunction(
    'glXDestroyWindow', dll=platform.GL, resultType=None,
    argTypes=[POINTER(Display), GLXWindow],
    doc='glXDestroyWindow( POINTER(Display)(dpy), GLXWindow(window) ) -> None',
    argNames=['dpy', 'window'],
)

glXCreatePixmap = platform.createBaseFunction(
    'glXCreatePixmap', dll=platform.GL, resultType=GLXPixmap,
    argTypes=[POINTER(Display), GLXFBConfig, Pixmap, POINTER(c_int)],
    doc='glXCreatePixmap( POINTER(Display)(dpy), GLXFBConfig(config), Pixmap(pixmap), POINTER(c_int)(attribList) ) -> GLXPixmap',
    argNames=['dpy', 'config', 'pixmap', 'attribList'],
)

glXDestroyPixmap = platform.createBaseFunction(
    'glXDestroyPixmap', dll=platform.GL, resultType=None,
    argTypes=[POINTER(Display), GLXPixmap],
    doc='glXDestroyPixmap( POINTER(Display)(dpy), GLXPixmap(pixmap) ) -> None',
    argNames=['dpy', 'pixmap'],
)

glXCreatePbuffer = platform.createBaseFunction(
    'glXCreatePbuffer', dll=platform.GL, resultType=GLXPbuffer,
    argTypes=[POINTER(Display), GLXFBConfig, POINTER(c_int)],
    doc='glXCreatePbuffer( POINTER(Display)(dpy), GLXFBConfig(config), POINTER(c_int)(attribList) ) -> GLXPbuffer',
    argNames=['dpy', 'config', 'attribList'],
)

glXDestroyPbuffer = platform.createBaseFunction(
    'glXDestroyPbuffer', dll=platform.GL, resultType=None,
    argTypes=[POINTER(Display), GLXPbuffer],
    doc='glXDestroyPbuffer( POINTER(Display)(dpy), GLXPbuffer(pbuf) ) -> None',
    argNames=['dpy', 'pbuf'],
)

glXQueryDrawable = platform.createBaseFunction(
    'glXQueryDrawable', dll=platform.GL, resultType=None,
    argTypes=[POINTER(Display), GLXDrawable, c_int, POINTER(c_uint)],
    doc='glXQueryDrawable( POINTER(Display)(dpy), GLXDrawable(draw), c_int(attribute), POINTER(c_uint)(value) ) -> None',
    argNames=['dpy', 'draw', 'attribute', 'value'],
)

glXCreateNewContext = platform.createBaseFunction(
    'glXCreateNewContext', dll=platform.GL, resultType=GLXContext,
    argTypes=[POINTER(Display), GLXFBConfig, c_int, GLXContext, c_int],
    doc='glXCreateNewContext( POINTER(Display)(dpy), GLXFBConfig(config), c_int(renderType), GLXContext(shareList), c_int(direct) ) -> GLXContext',
    argNames=['dpy', 'config', 'renderType', 'shareList', 'direct'],
)

glXMakeContextCurrent = platform.createBaseFunction(
    'glXMakeContextCurrent', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), GLXDrawable, GLXDrawable, GLXContext],
    doc='glXMakeContextCurrent( POINTER(Display)(dpy), GLXDrawable(draw), GLXDrawable(read), GLXContext(ctx) ) -> c_int',
    argNames=['dpy', 'draw', 'read', 'ctx'],
)

glXGetCurrentReadDrawable = platform.createBaseFunction(
    'glXGetCurrentReadDrawable', dll=platform.GL, resultType=GLXDrawable,
    argTypes=[],
    doc='glXGetCurrentReadDrawable(  ) -> GLXDrawable',
    argNames=[],
)

glXQueryContext = platform.createBaseFunction(
    'glXQueryContext', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), GLXContext, c_int, POINTER(c_int)],
    doc='glXQueryContext( POINTER(Display)(dpy), GLXContext(ctx), c_int(attribute), POINTER(c_int)(value) ) -> c_int',
    argNames=['dpy', 'ctx', 'attribute', 'value'],
)

glXSelectEvent = platform.createBaseFunction(
    'glXSelectEvent', dll=platform.GL, resultType=None,
    argTypes=[POINTER(Display), GLXDrawable, c_ulong],
    doc='glXSelectEvent( POINTER(Display)(dpy), GLXDrawable(drawable), c_ulong(mask) ) -> None',
    argNames=['dpy', 'drawable', 'mask'],
)

glXGetSelectedEvent = platform.createBaseFunction(
    'glXGetSelectedEvent', dll=platform.GL, resultType=None,
    argTypes=[POINTER(Display), GLXDrawable, POINTER(c_ulong)],
    doc='glXGetSelectedEvent( POINTER(Display)(dpy), GLXDrawable(drawable), POINTER(c_ulong)(mask) ) -> None',
    argNames=['dpy', 'drawable', 'mask'],
)

# ARB_get_proc_address (/usr/include/GL/glx.h:327)
GLX_ARB_get_proc_address = constant.Constant( 'GLX_ARB_get_proc_address', 1 )
__GLXextFuncPtr = CFUNCTYPE(None) 	# /usr/include/GL/glx.h:330
GLubyte = c_ubyte 	# /usr/include/GL/gl.h:162
glXGetProcAddressARB = platform.createBaseFunction(
    'glXGetProcAddressARB', dll=platform.GL, resultType=__GLXextFuncPtr,
    argTypes=[POINTER(GLubyte)],
    doc='glXGetProcAddressARB( POINTER(GLubyte)() ) -> __GLXextFuncPtr',
    argNames=[''],
)

glXGetProcAddress = platform.createBaseFunction(
    'glXGetProcAddress', dll=platform.GL, resultType=POINTER(CFUNCTYPE(None)),
    argTypes=[POINTER(GLubyte)],
    doc='glXGetProcAddress( POINTER(GLubyte)(procname) ) -> POINTER(CFUNCTYPE(None))',
    argNames=['procname'],
)

# GLXEXT_LEGACY (/usr/include/GL/glx.h:344)
# VERSION_1_3 (/usr/include/GL/glxext.h:55)
# VERSION_1_4 (/usr/include/GL/glxext.h:114)
# ARB_get_proc_address (/usr/include/GL/glxext.h:119)
# ARB_multisample (/usr/include/GL/glxext.h:122)
# ARB_vertex_buffer_object (/usr/include/GL/glxext.h:127)
# ARB_fbconfig_float (/usr/include/GL/glxext.h:131)
# ARB_framebuffer_sRGB (/usr/include/GL/glxext.h:136)
# ARB_create_context (/usr/include/GL/glxext.h:140)
# ARB_create_context_profile (/usr/include/GL/glxext.h:148)
# ARB_create_context_robustness (/usr/include/GL/glxext.h:154)
# SGIS_multisample (/usr/include/GL/glxext.h:161)
# EXT_visual_info (/usr/include/GL/glxext.h:166)
# SGI_swap_control (/usr/include/GL/glxext.h:185)
# SGI_video_sync (/usr/include/GL/glxext.h:188)
# SGI_make_current_read (/usr/include/GL/glxext.h:191)
# SGIX_video_source (/usr/include/GL/glxext.h:194)
# EXT_visual_rating (/usr/include/GL/glxext.h:197)
# EXT_import_context (/usr/include/GL/glxext.h:204)
# SGIX_fbconfig (/usr/include/GL/glxext.h:210)
# SGIX_pbuffer (/usr/include/GL/glxext.h:224)
# SGI_cushion (/usr/include/GL/glxext.h:252)
# SGIX_video_resize (/usr/include/GL/glxext.h:255)
# SGIX_dmbuffer (/usr/include/GL/glxext.h:260)
# SGIX_swap_group (/usr/include/GL/glxext.h:264)
# SGIX_swap_barrier (/usr/include/GL/glxext.h:267)
# SGIS_blended_overlay (/usr/include/GL/glxext.h:270)
# SGIS_shared_multisample (/usr/include/GL/glxext.h:274)
# SUN_get_transparent_index (/usr/include/GL/glxext.h:279)
# 3DFX_multisample (/usr/include/GL/glxext.h:282)
# MESA_copy_sub_buffer (/usr/include/GL/glxext.h:287)
# MESA_pixmap_colormap (/usr/include/GL/glxext.h:290)
# MESA_release_buffers (/usr/include/GL/glxext.h:293)
# MESA_set_3dfx_mode (/usr/include/GL/glxext.h:296)
# SGIX_visual_select_group (/usr/include/GL/glxext.h:301)
# OML_swap_method (/usr/include/GL/glxext.h:305)
# OML_sync_control (/usr/include/GL/glxext.h:312)
# NV_float_buffer (/usr/include/GL/glxext.h:315)
# SGIX_hyperpipe (/usr/include/GL/glxext.h:319)
# MESA_agp_offset (/usr/include/GL/glxext.h:332)
# EXT_fbconfig_packed_float (/usr/include/GL/glxext.h:335)
# EXT_framebuffer_sRGB (/usr/include/GL/glxext.h:340)
# EXT_texture_from_pixmap (/usr/include/GL/glxext.h:344)
# NV_present_video (/usr/include/GL/glxext.h:380)
# NV_video_out (/usr/include/GL/glxext.h:384)
# NV_swap_group (/usr/include/GL/glxext.h:397)
# NV_video_capture (/usr/include/GL/glxext.h:400)
# EXT_swap_control (/usr/include/GL/glxext.h:406)
# NV_copy_image (/usr/include/GL/glxext.h:411)
# INTEL_swap_event (/usr/include/GL/glxext.h:414)
# NV_multisample_coverage (/usr/include/GL/glxext.h:421)
# AMD_gpu_association (/usr/include/GL/glxext.h:426)
# EXT_create_context_es2_profile (/usr/include/GL/glxext.h:439)
# ARB_get_proc_address (/usr/include/GL/glxext.h:446)
# SGIX_video_source (/usr/include/GL/glxext.h:450)
# SGIX_fbconfig (/usr/include/GL/glxext.h:454)
# SGIX_pbuffer (/usr/include/GL/glxext.h:459)
# NV_video_output (/usr/include/GL/glxext.h:476)
# NV_video_capture (/usr/include/GL/glxext.h:480)
# VERSION_1_3 (/usr/include/GL/glxext.h:521)
# VERSION_1_4 (/usr/include/GL/glxext.h:563)
# ARB_get_proc_address (/usr/include/GL/glxext.h:571)
# ARB_multisample (/usr/include/GL/glxext.h:579)
# ARB_fbconfig_float (/usr/include/GL/glxext.h:583)
# ARB_framebuffer_sRGB (/usr/include/GL/glxext.h:587)
# ARB_create_context (/usr/include/GL/glxext.h:591)
# ARB_create_context_profile (/usr/include/GL/glxext.h:599)
# ARB_create_context_robustness (/usr/include/GL/glxext.h:603)
# SGIS_multisample (/usr/include/GL/glxext.h:607)
# EXT_visual_info (/usr/include/GL/glxext.h:611)
# SGI_swap_control (/usr/include/GL/glxext.h:615)
# SGI_video_sync (/usr/include/GL/glxext.h:623)
# SGI_make_current_read (/usr/include/GL/glxext.h:633)
# SGIX_video_source (/usr/include/GL/glxext.h:643)
# EXT_visual_rating (/usr/include/GL/glxext.h:655)
# EXT_import_context (/usr/include/GL/glxext.h:659)
# SGIX_fbconfig (/usr/include/GL/glxext.h:675)
# SGIX_pbuffer (/usr/include/GL/glxext.h:693)
# SGI_cushion (/usr/include/GL/glxext.h:709)
# SGIX_video_resize (/usr/include/GL/glxext.h:717)
# SGIX_dmbuffer (/usr/include/GL/glxext.h:733)
# SGIX_swap_group (/usr/include/GL/glxext.h:743)
# SGIX_swap_barrier (/usr/include/GL/glxext.h:751)
# SUN_get_transparent_index (/usr/include/GL/glxext.h:761)
# MESA_copy_sub_buffer (/usr/include/GL/glxext.h:769)
# MESA_pixmap_colormap (/usr/include/GL/glxext.h:777)
# MESA_release_buffers (/usr/include/GL/glxext.h:785)
# MESA_set_3dfx_mode (/usr/include/GL/glxext.h:793)
# SGIX_visual_select_group (/usr/include/GL/glxext.h:801)
# OML_swap_method (/usr/include/GL/glxext.h:805)
# OML_sync_control (/usr/include/GL/glxext.h:809)
# NV_float_buffer (/usr/include/GL/glxext.h:825)
# SGIX_hyperpipe (/usr/include/GL/glxext.h:829)
# MESA_agp_offset (/usr/include/GL/glxext.h:876)
# EXT_fbconfig_packed_float (/usr/include/GL/glxext.h:884)
# EXT_framebuffer_sRGB (/usr/include/GL/glxext.h:888)
# EXT_texture_from_pixmap (/usr/include/GL/glxext.h:892)
# NV_present_video (/usr/include/GL/glxext.h:902)
# NV_video_output (/usr/include/GL/glxext.h:912)
# NV_swap_group (/usr/include/GL/glxext.h:930)
# NV_video_capture (/usr/include/GL/glxext.h:948)
# EXT_swap_control (/usr/include/GL/glxext.h:964)
# NV_copy_image (/usr/include/GL/glxext.h:972)
# INTEL_swap_event (/usr/include/GL/glxext.h:980)
# NV_multisample_coverage (/usr/include/GL/glxext.h:984)
# NV_vertex_array_range (/usr/include/GL/glx.h:359)
GLsizei = c_int 	# /usr/include/GL/gl.h:165
GLfloat = c_float 	# /usr/include/GL/gl.h:166
glXAllocateMemoryNV = platform.createBaseFunction(
    'glXAllocateMemoryNV', dll=platform.GL, resultType=POINTER(c_void),
    argTypes=[GLsizei, GLfloat, GLfloat, GLfloat],
    doc='glXAllocateMemoryNV( GLsizei(size), GLfloat(readfreq), GLfloat(writefreq), GLfloat(priority) ) -> POINTER(c_void)',
    argNames=['size', 'readfreq', 'writefreq', 'priority'],
)

GLvoid = None 	# /usr/include/GL/gl.h:158
glXFreeMemoryNV = platform.createBaseFunction(
    'glXFreeMemoryNV', dll=platform.GL, resultType=None,
    argTypes=[POINTER(GLvoid)],
    doc='glXFreeMemoryNV( POINTER(GLvoid)(pointer) ) -> None',
    argNames=['pointer'],
)

# ARB_render_texture (/usr/include/GL/glx.h:374)
GLX_ARB_render_texture = constant.Constant( 'GLX_ARB_render_texture', 1 )
glXBindTexImageARB = platform.createBaseFunction(
    'glXBindTexImageARB', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), GLXPbuffer, c_int],
    doc='glXBindTexImageARB( POINTER(Display)(dpy), GLXPbuffer(pbuffer), c_int(buffer) ) -> c_int',
    argNames=['dpy', 'pbuffer', 'buffer'],
)

glXReleaseTexImageARB = platform.createBaseFunction(
    'glXReleaseTexImageARB', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), GLXPbuffer, c_int],
    doc='glXReleaseTexImageARB( POINTER(Display)(dpy), GLXPbuffer(pbuffer), c_int(buffer) ) -> c_int',
    argNames=['dpy', 'pbuffer', 'buffer'],
)

glXDrawableAttribARB = platform.createBaseFunction(
    'glXDrawableAttribARB', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), GLXDrawable, POINTER(c_int)],
    doc='glXDrawableAttribARB( POINTER(Display)(dpy), GLXDrawable(draw), POINTER(c_int)(attribList) ) -> c_int',
    argNames=['dpy', 'draw', 'attribList'],
)

# NV_float_buffer (/usr/include/GL/glx.h:387)
# MESA_swap_frame_usage (/usr/include/GL/glx.h:399)
GLX_MESA_swap_frame_usage = constant.Constant( 'GLX_MESA_swap_frame_usage', 1 )
glXGetFrameUsageMESA = platform.createBaseFunction(
    'glXGetFrameUsageMESA', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), GLXDrawable, POINTER(c_float)],
    doc='glXGetFrameUsageMESA( POINTER(Display)(dpy), GLXDrawable(drawable), POINTER(c_float)(usage) ) -> c_int',
    argNames=['dpy', 'drawable', 'usage'],
)

glXBeginFrameTrackingMESA = platform.createBaseFunction(
    'glXBeginFrameTrackingMESA', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), GLXDrawable],
    doc='glXBeginFrameTrackingMESA( POINTER(Display)(dpy), GLXDrawable(drawable) ) -> c_int',
    argNames=['dpy', 'drawable'],
)

glXEndFrameTrackingMESA = platform.createBaseFunction(
    'glXEndFrameTrackingMESA', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), GLXDrawable],
    doc='glXEndFrameTrackingMESA( POINTER(Display)(dpy), GLXDrawable(drawable) ) -> c_int',
    argNames=['dpy', 'drawable'],
)

glXQueryFrameTrackingMESA = platform.createBaseFunction(
    'glXQueryFrameTrackingMESA', dll=platform.GL, resultType=c_int,
    argTypes=[POINTER(Display), GLXDrawable, POINTER(c_int64), POINTER(c_int64), POINTER(c_float)],
    doc='glXQueryFrameTrackingMESA( POINTER(Display)(dpy), GLXDrawable(drawable), POINTER(c_int64)(swapCount), POINTER(c_int64)(missedFrames), POINTER(c_float)(lastMissedUsage) ) -> c_int',
    argNames=['dpy', 'drawable', 'swapCount', 'missedFrames', 'lastMissedUsage'],
)

# MESA_swap_control (/usr/include/GL/glx.h:419)
GLX_MESA_swap_control = constant.Constant( 'GLX_MESA_swap_control', 1 )
glXSwapIntervalMESA = platform.createBaseFunction(
    'glXSwapIntervalMESA', dll=platform.GL, resultType=c_int,
    argTypes=[c_uint],
    doc='glXSwapIntervalMESA( c_uint(interval) ) -> c_int',
    argNames=['interval'],
)

glXGetSwapIntervalMESA = platform.createBaseFunction(
    'glXGetSwapIntervalMESA', dll=platform.GL, resultType=c_int,
    argTypes=[],
    doc='glXGetSwapIntervalMESA(  ) -> c_int',
    argNames=[],
)

# EXT_texture_from_pixmap (/usr/include/GL/glx.h:436)
class struct_anon_111(Structure):
    __slots__ = [
        'event_type',
        'draw_type',
        'serial',
        'send_event',
        'display',
        'drawable',
        'buffer_mask',
        'aux_buffer',
        'x',
        'y',
        'width',
        'height',
        'count',
    ]
struct_anon_111._fields_ = [
    ('event_type', c_int),
    ('draw_type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('drawable', GLXDrawable),
    ('buffer_mask', c_uint),
    ('aux_buffer', c_uint),
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
    ('count', c_int),
]

GLXPbufferClobberEvent = struct_anon_111 	# /usr/include/GL/glx.h:502
class struct_anon_112(Structure):
    __slots__ = [
        'type',
        'serial',
        'send_event',
        'display',
        'drawable',
        'event_type',
        'ust',
        'msc',
        'sbc',
    ]
struct_anon_112._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('drawable', GLXDrawable),
    ('event_type', c_int),
    ('ust', c_int64),
    ('msc', c_int64),
    ('sbc', c_int64),
]

GLXBufferSwapComplete = struct_anon_112 	# /usr/include/GL/glx.h:514
class struct___GLXEvent(Union):
    __slots__ = [
        'glxpbufferclobber',
        'glxbufferswapcomplete',
        'pad',
    ]
struct___GLXEvent._fields_ = [
    ('glxpbufferclobber', GLXPbufferClobberEvent),
    ('glxbufferswapcomplete', GLXBufferSwapComplete),
    ('pad', c_long * 24),
]

GLXEvent = struct___GLXEvent 	# /usr/include/GL/glx.h:520

__all__ = ['GLX_VERSION_1_1', 'GLX_VERSION_1_2', 'GLX_VERSION_1_3',
'GLX_VERSION_1_4', 'GLX_USE_GL', 'GLX_BUFFER_SIZE', 'GLX_LEVEL', 'GLX_RGBA',
'GLX_DOUBLEBUFFER', 'GLX_STEREO', 'GLX_AUX_BUFFERS', 'GLX_RED_SIZE',
'GLX_GREEN_SIZE', 'GLX_BLUE_SIZE', 'GLX_ALPHA_SIZE', 'GLX_DEPTH_SIZE',
'GLX_STENCIL_SIZE', 'GLX_ACCUM_RED_SIZE', 'GLX_ACCUM_GREEN_SIZE',
'GLX_ACCUM_BLUE_SIZE', 'GLX_ACCUM_ALPHA_SIZE', 'GLX_BAD_SCREEN',
'GLX_BAD_ATTRIBUTE', 'GLX_NO_EXTENSION', 'GLX_BAD_VISUAL', 'GLX_BAD_CONTEXT',
'GLX_BAD_VALUE', 'GLX_BAD_ENUM', 'GLX_VENDOR', 'GLX_VERSION',
'GLX_EXTENSIONS', 'GLX_CONFIG_CAVEAT', 'GLX_DONT_CARE', 'GLX_X_VISUAL_TYPE',
'GLX_TRANSPARENT_TYPE', 'GLX_TRANSPARENT_INDEX_VALUE',
'GLX_TRANSPARENT_RED_VALUE', 'GLX_TRANSPARENT_GREEN_VALUE',
'GLX_TRANSPARENT_BLUE_VALUE', 'GLX_TRANSPARENT_ALPHA_VALUE', 'GLX_WINDOW_BIT',
'GLX_PIXMAP_BIT', 'GLX_PBUFFER_BIT', 'GLX_AUX_BUFFERS_BIT',
'GLX_FRONT_LEFT_BUFFER_BIT', 'GLX_FRONT_RIGHT_BUFFER_BIT',
'GLX_BACK_LEFT_BUFFER_BIT', 'GLX_BACK_RIGHT_BUFFER_BIT',
'GLX_DEPTH_BUFFER_BIT', 'GLX_STENCIL_BUFFER_BIT', 'GLX_ACCUM_BUFFER_BIT',
'GLX_NONE', 'GLX_SLOW_CONFIG', 'GLX_TRUE_COLOR', 'GLX_DIRECT_COLOR',
'GLX_PSEUDO_COLOR', 'GLX_STATIC_COLOR', 'GLX_GRAY_SCALE', 'GLX_STATIC_GRAY',
'GLX_TRANSPARENT_RGB', 'GLX_TRANSPARENT_INDEX', 'GLX_VISUAL_ID', 'GLX_SCREEN',
'GLX_NON_CONFORMANT_CONFIG', 'GLX_DRAWABLE_TYPE', 'GLX_RENDER_TYPE',
'GLX_X_RENDERABLE', 'GLX_FBCONFIG_ID', 'GLX_RGBA_TYPE',
'GLX_COLOR_INDEX_TYPE', 'GLX_MAX_PBUFFER_WIDTH', 'GLX_MAX_PBUFFER_HEIGHT',
'GLX_MAX_PBUFFER_PIXELS', 'GLX_PRESERVED_CONTENTS', 'GLX_LARGEST_PBUFFER',
'GLX_WIDTH', 'GLX_HEIGHT', 'GLX_EVENT_MASK', 'GLX_DAMAGED', 'GLX_SAVED',
'GLX_WINDOW', 'GLX_PBUFFER', 'GLX_PBUFFER_HEIGHT', 'GLX_PBUFFER_WIDTH',
'GLX_RGBA_BIT', 'GLX_COLOR_INDEX_BIT', 'GLX_PBUFFER_CLOBBER_MASK',
'GLX_SAMPLE_BUFFERS', 'GLX_SAMPLES', 'GLXContext', 'GLXPixmap', 'GLXDrawable',
'GLXFBConfig', 'GLXFBConfigID', 'GLXContextID', 'GLXWindow', 'GLXPbuffer',
'GLX_PbufferClobber', 'GLX_BufferSwapComplete', 'glXChooseVisual',
'glXCreateContext', 'glXDestroyContext', 'glXMakeCurrent', 'glXCopyContext',
'glXSwapBuffers', 'glXCreateGLXPixmap', 'glXDestroyGLXPixmap',
'glXQueryExtension', 'glXQueryVersion', 'glXIsDirect', 'glXGetConfig',
'glXGetCurrentContext', 'glXGetCurrentDrawable', 'glXWaitGL', 'glXWaitX',
'glXUseXFont', 'glXQueryExtensionsString', 'glXQueryServerString',
'glXGetClientString', 'glXGetCurrentDisplay', 'glXChooseFBConfig',
'glXGetFBConfigAttrib', 'glXGetFBConfigs', 'glXGetVisualFromFBConfig',
'glXCreateWindow', 'glXDestroyWindow', 'glXCreatePixmap', 'glXDestroyPixmap',
'glXCreatePbuffer', 'glXDestroyPbuffer', 'glXQueryDrawable',
'glXCreateNewContext', 'glXMakeContextCurrent', 'glXGetCurrentReadDrawable',
'glXQueryContext', 'glXSelectEvent', 'glXGetSelectedEvent',
'GLX_ARB_get_proc_address', 'glXGetProcAddressARB', 'glXGetProcAddress',
'glXAllocateMemoryNV', 'glXFreeMemoryNV', 'GLX_ARB_render_texture',
'glXBindTexImageARB', 'glXReleaseTexImageARB', 'glXDrawableAttribARB',
'GLX_MESA_swap_frame_usage', 'glXGetFrameUsageMESA',
'glXBeginFrameTrackingMESA', 'glXEndFrameTrackingMESA',
'glXQueryFrameTrackingMESA', 'GLX_MESA_swap_control', 'glXSwapIntervalMESA',
'glXGetSwapIntervalMESA', 'GLXPbufferClobberEvent', 'GLXBufferSwapComplete',
'GLXEvent']
# END GENERATED CONTENT (do not edit above this line)
