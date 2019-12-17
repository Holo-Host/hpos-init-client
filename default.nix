{ pkgs ? import ./pkgs.nix {} }:

with pkgs;

{
  hpos-seed = with python37Packages; buildPythonApplication {
    name = "hpos-seed";
    src = lib.cleanSource ./.;

    nativeBuildInputs = [ qt5.wrapQtAppsHook ];
    propagatedBuildInputs = [ magic-wormhole pyqt5 ];

    meta.platforms = lib.platforms.all;
  };
}
