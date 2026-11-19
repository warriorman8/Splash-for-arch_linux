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
depends=( 'vim' 'grace' 'gmsh' 'shellcheck' 'cloc' 'gedit-plugins' 'xorg-server' 'xorg-apps' 'qt6-base' 'gnome'  )
makedepends=('git' 'pypy3' 'cmake')
checkdepends=()
optdepends=('paraview' 'freecad')
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
	# creating the git link dictionary for foundation openfoam versions
	declare -A flinks=(
		['of8'] = 'https://github.com/OpenFOAM/OpenFOAM-8.git'
		['of9'] = 'https://github.com/OpenFOAM/OpenFOAM-9.git'
		['of10'] = 'https://github.com/OpenFOAM/OpenFOAM-10.git'
		['of11'] = 'https://github.com/OpenFOAM/OpenFOAM-11.git'
		['of12'] = 'https://github.com/OpenFOAM/OpenFOAM-12.git'
		
	)
    # creating shell alias dictionary to be put in bashrc
	declare -A shells=(
		['of8']='openfoam8/etc/bashrc'
		['of9']='openfoam9/etc/bashrc'
		['of10']='openfoam10/etc/bashrc'
		['of11']='openfoam11/etc/bashrc'
		['of12']='openfoam12/etc/bashrc'
		['of2206']='OpenFOAM-v2206/etc/bashrc'
		['of2212']='OpenFOAM-v2212/etc/bashrc'
		['of2306']='OpenFOAM-v2306/etc/bashrc'
		['of2312']='OpenFOAM-v2312/etc/bashrc'
		['of2406']='OpenFOAM-v2406/etc/bashrc'
	)
	rm -rf openfoam
	mkdir openfoam
	cd openfoam
	for key in "${!flinks[@]}"; do
		mkdir $key
		cd $key
		echo "alias $key='source $PWD/${fshells[$key]}'" >> ~/.bashrc

		git clone ${flinks[$key]}
		cd ..
	done
	# creating the git link dictionary for ESI openfoam versions	
	declare -A ESIlinks=(
    	['of2206'] = 'https://sourceforge.net/projects/openfoam/files/v2206/OpenFOAM-v2206.tgz'
		['of2212'] = 'https://sourceforge.net/projects/openfoam/files/v2212/OpenFOAM-v2212.tgz'
		['of2306'] = 'https://sourceforge.net/projects/openfoam/files/v2306/OpenFOAM-v2306.tgz'
		['of2312'] = 'https://sourceforge.net/projects/openfoam/files/v2312/OpenFOAM-v2312.tgz'
		['of2406'] = 'https://sourceforge.net/projects/openfoam/files/v2406/OpenFOAM-v2406.tgz'
		
	)
    # creating ESI shell alias dictionary to be put in bashrc
	for key in "${!ESIlinks[@]}"; do
		mkdir $key
		cd $key
		echo "alias $key='source $PWD/${shells[$key]}'" >> ~/.bashrc
		wget ${ESIlinks[$key]}
		tar -zxvf *.tgz
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
	chmod +x source/splash.py
	pypy3 desktop_apply.py
	mv "$pkgname-$pkgver"/splash-flow.desktop /usr/share/applications/splash-flow.desktop
}
