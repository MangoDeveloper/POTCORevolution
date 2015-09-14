import os
import sys
import imp

panda3d_modules = {
    'core': ('libpandaexpress', 'libpanda'),
    'dtoolconfig': 'libp3dtoolconfig',
    'physics': 'libpandaphysics',
    'fx': 'libpandafx',
    'direct': 'libp3direct',
    'egg': 'libpandaegg',
    'ode': 'libpandaode',
    'vision': 'libp3vision',
    'physx': 'libpandaphysx',
    'ai': 'libpandaai',
    'awesomium': 'libp3awesomium' }

class panda3d_import_manager:
    os = os
    sys = sys
    imp = imp
    dll_suffix = ''
    dll_exts = ('.pyd', '.so')
    if sys.platform == 'win32':
        dll_exts = ('.pyd', '.dll')
        dll_suffix = getattr(sys, 'dll_suffix', None)
        if dll_suffix is None:
            dll_suffix = ''
            if sys.executable.endswith('_d.exe'):
                dll_suffix = '_d'
            
        
    
    if sys.platform == 'darwin':
        dll_exts = ('.pyd', '.so', '.dylib')
    
    prepared = False
    
    def __prepare(cls):
        if cls.prepared:
            return None
        
        cls.prepared = True
        target = None
        filename = 'libpandaexpress' + cls.dll_suffix
        for dir in cls.sys.path + [
            cls.sys.prefix]:
            lib = cls.os.path.join(dir, filename)
            for dll_ext in cls.dll_exts:
                if cls.os.path.exists(lib + dll_ext):
                    target = dir
                    break
                    continue
            
        
        if target == None:
            raise ImportError, 'Cannot find %s' % filename
        
        target = cls.os.path.abspath(target)
        if cls.sys.platform == 'win32':
            cls._panda3d_import_manager__prepend_to_path('PATH', target)
        else:
            cls._panda3d_import_manager__prepend_to_path('LD_LIBRARY_PATH', target)
        if cls.sys.platform == 'darwin':
            cls._panda3d_import_manager__prepend_to_path('DYLD_LIBRARY_PATH', target)
        

    _panda3d_import_manager__prepare = classmethod(__prepare)
    
    def __prepend_to_path(cls, varname, target):
        if varname in cls.os.environ:
            path = cls.os.environ[varname].strip(cls.os.pathsep)
        else:
            path = ''
        if len(path) == 0:
            cls.os.environ[varname] = target
        elif not path.startswith(target):
            cls.os.environ[varname] = target + cls.os.pathsep + path
        

    _panda3d_import_manager__prepend_to_path = classmethod(__prepend_to_path)
    
    def libimport(cls, name):
        if not cls.prepared:
            cls._panda3d_import_manager__prepare()
        
        
        try:
            return __import__(name)
        except ImportError:
            err = None
            if str(err) != 'No module named ' + name:
                raise 
            
        except:
            str(err) != 'No module named ' + name

        target = None
        filename = name + cls.dll_suffix
        for dir in cls.sys.path + [
            cls.sys.prefix]:
            lib = cls.os.path.join(dir, filename)
            for dll_ext in cls.dll_exts:
                if cls.os.path.exists(lib + dll_ext):
                    target = lib + dll_ext
                    break
                    continue
            
        
        if target == None:
            message = 'DLL loader cannot find %s.' % name
            raise ImportError, message
        
        target = cls.os.path.abspath(target)
        return cls.imp.load_dynamic(name, target)

    libimport = classmethod(libimport)


class panda3d_submodule(type(sys)):
    __manager__ = panda3d_import_manager
    
    def __init__(self, name, library):
        type(sys).__init__(self, 'panda3d.' + name)
        self.__library__ = library
        self.__libraries__ = [
            self.__library__]

    
    def __load__(self):
        self.__manager__.libimport(self.__library__)

    
    def __getattr__(self, name):
        mod = self.__manager__.libimport(self.__library__)
        if name == '__all__':
            everything = []
            for obj in dir(mod):
                if not obj.startswith('__'):
                    everything.append(obj)
                    continue
            
            return everything
        elif name == '__library__':
            return self.__library__
        elif name == '__libraries__':
            return self.__libraries__
        elif name in dir(mod):
            return mod.__dict__[name]
        
        raise AttributeError, "'module' object has no attribute '%s'" % name



class panda3d_multisubmodule(type(sys)):
    __manager__ = panda3d_import_manager
    
    def __init__(self, name, libraries):
        type(sys).__init__(self, 'panda3d.' + name)
        self.__libraries__ = libraries

    
    def __load__(self):
        for lib in self.__libraries__:
            self.__manager__.libimport(lib)
        

    
    def __getattr__(self, name):
        if name == '__all__':
            everything = []
            for lib in self.__libraries__:
                for obj in dir(self.__manager__.libimport(lib)):
                    if not obj.startswith('__'):
                        everything.append(obj)
                        continue
                
            
            return everything
        elif name == '__libraries__':
            return self.__libraries__
        
        for lib in self.__libraries__:
            mod = self.__manager__.libimport(lib)
            if name in dir(mod):
                return mod.__dict__[name]
                continue
        
        raise AttributeError, "'module' object has no attribute '%s'" % name



class panda3d_module(type(sys)):
    __file__ = __file__
    modules = panda3d_modules
    __manager__ = panda3d_import_manager
    
    def __load__(self):
        for module in self.modules:
            self.__manager__.sys.modules['panda3d.%s' % module].__load__()
        

    
    def __getattr__(self, name):
        if name == '__all__':
            return self.modules.keys()
        elif name == '__file__':
            return self.__file__
        elif name in self.modules:
            return self.__manager__.sys.modules['panda3d.%s' % name]
        
        raise AttributeError, "'module' object has no attribute '%s'" % name


this = panda3d_module('panda3d')
for (mod, lib) in panda3d_modules.items():
    if isinstance(lib, tuple):
        module = panda3d_multisubmodule(mod, lib)
    else:
        module = panda3d_submodule(mod, lib)
    sys.modules['panda3d.' + mod] = module
    this.__dict__[mod] = module

sys.modules['panda3d'] = this
