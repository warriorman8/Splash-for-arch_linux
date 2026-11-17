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
url="https://github.com/warriorman8/Splash-for-arch_linux"
license=('GPL')
groups=()
depends=('paraview' 'freecad' 'vim' 'grace' 'gmsh' 'shellcheck' 'cloc' 'gedit-plugins' 'xorg-server' 'xorg-apps' 'qt6-base' 'gnome' 'apptainer' 'openfoam-org' 'zenity' 'vtk' )
makedepends=('git' 'pypy3' 'cmake')
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
	git clone https://gitlab.kitware.com/vtk/vtk.git
	# creating the git link dictionary for openfoam versions
	declare -A links=(
		
	)
    # creating shell alias dictionary to be put in bashrc
	declare -A shells=(

	)
	rm -rf openfoam
	mkdir openfoam
	cd openfoam
	for key in "${!links[@]}"; do
		echo "alias $key='${shells[$key]}'" >> ~/.bashrc
		mkdir $key
		cd $key
		git clone ${links[$key]}
		cd ..
	done
	cd ..
	
	
}
build() {
    cd "$pkgname-$pkgver"/resources
	cd vtk
    mkdir build && cd build
    cmake ..
    cmake --build . -j$(nproc)
	cd ..
}



package() {
	cd "$pkgname-$pkgver"
	pypy3 desktop_apply.py
	mv "$pkgname-$pkgver"/splash-flow.desktop /usr/share/applications/splash-flow.desktop
}
