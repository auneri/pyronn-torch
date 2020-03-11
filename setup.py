import sys
from glob import glob
from os.path import dirname, join

from pkg_resources import VersionConflict, require
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

try:
    require('setuptools>=38.3')
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)


if __name__ == "__main__":

    object_cache = dirname(__file__)
    module_name = 'pyronn_torch_cpp'

    cuda_sources = glob(join(dirname(__file__), 'generated_files', '*.cu'))

    generated_file = join('generated_files', 'pyronn_torch.cpp')

    setup(use_pyscaffold=True,
          ext_modules=[
              CUDAExtension(module_name,
                            [generated_file] + cuda_sources,
                            extra_compile_args={'cxx': ['--std=c++14'],
                                                'nvcc': ['-arch=sm_35']})
          ],
          cmdclass={
              'build_ext': BuildExtension
          })
