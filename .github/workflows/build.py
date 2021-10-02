import subprocess, os, platform, shutil

current_dir = os.path.abspath(os.path.dirname(__file__))
main_dir = os.path.join(current_dir, '..', '..')
build_dir = os.path.join(main_dir, 'build') 
bin_dir = os.path.join(main_dir, 'bin') 

try: 
    os.mkdir(build_dir)
    os.mkdir(bin_dir)
except: pass

if platform.system() == 'Windows': #Multi-config generators, like Visual Studio
    subprocess.check_call(['cmake', '-A', 'x64', '-D', 'CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE='+bin_dir, main_dir], cwd=build_dir)
    subprocess.check_call(['cmake', '--build', '.', '--config', 'Release'], cwd=build_dir)
else: #Single-config generators
    subprocess.check_call(['cmake', '-D', 'CMAKE_RUNTIME_OUTPUT_DIRECTORY='+bin_dir, main_dir], cwd=build_dir)
    subprocess.check_call(['cmake', '--build', '.', '-Wno-error'], cwd=build_dir)

shutil.make_archive(os.path.join('mcpp'), 'zip', bin_dir, '.')

