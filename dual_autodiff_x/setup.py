from setuptools import setup, Extension
from Cython.Build import cythonize

# Define the extensions (Cython modules)
extensions = [
    Extension("sub_dual_autodiff_x.dual", ["src/sub_dual_autodiff_x/dual.pyx"]),
    Extension("sub_dual_autodiff_x.version", ["src/sub_dual_autodiff_x/version.pyx"]),
    Extension("sub_dual_autodiff_x.corel", ["src/sub_dual_autodiff_x/core.pyx"])
]

# Call setup with cythonized extensions
setup(
    ext_modules=cythonize(extensions,
    compiler_directives={'language_level': "3"}),
    package_dir={"": "src"},
    packages=["sub_dual_autodiff_x"],

    # # Include only .so/.pyd files (compiled extensions), exclude source files
    package_data={"sub_dual_autodiff_x": ["*.so", "*.pyd"]},
    exclude_package_data={"sub_dual_autodiff_x": ["*.pyx", "*.py"]},
    # Ensure that wheels can be built
    zip_safe=False,
)