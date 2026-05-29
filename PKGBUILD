# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: warriorman8 <suhaibyasin1998@gmail.com>
pkgname='splash-flow'
pkgver=1.0.0
pkgrel=1
# epoch=
pkgdesc="An openfoam GUI wrapper that helps you set up sophisticated CFD simulations and on the cloud"
arch=(x86_64)
url="cfddose.com"
license=('GPL')
groups=()
depends=('paraview' 'freecad' 'vim' 'grace' 'gmsh' 'shellcheck' 'cloc' 'gedit-plugins' 'xorg-server' 'xorg-apps' 'qt6-base' 'gnome' 'apptainer' 'openfoam-org' 'zenity' 'vtk' )
makedepends=('git' 'pypy3')
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
# install= remove application executable and uninstall pypy3 modules
changelog=
source=(git::https://github.com/warriorman8/Splash-for-arch_linux.git)
noextract=()
sha256sums=('SKIP')
validpgpkeys=()

prepare() {
	cd "$pkgname-$pkgver"
	pypy3 -m ensurepip --user
	pypy3 -m pip install --user --upgrade pip
    pypy3 -m pip install --user --upgrade pip
	pypy3 -m pip install --user customtkinter
	pypy3 -m pip install --user pyinstaller
	pypy3 -m pip install --user Pillow
	pypy3 -m pip install --user matplotlib
	pypy3 -m pip install --user numpy
	pypy3 -m pip install --user numpy-stl
#   vtk needs to be installed here
	
	
}



package() {
	cd "$pkgname-$pkgver"
	pypy3 desktop_apply.py
	
}
