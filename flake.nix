{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    treefmt-nix.url = "github:numtide/treefmt-nix";
  };

  outputs =
    inputs:
    inputs.flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
        "aarch64-darwin"
      ];

      imports = [
        inputs.treefmt-nix.flakeModule
      ];

      perSystem =
        {
          pkgs,
          lib,
          ...
        }:
        let
          python = pkgs.python314;
          poetry = pkgs.poetry.withPlugins (ps: [ ps.poetry-plugin-export ]);
        in
        {
          devShells.default = pkgs.mkShell {
            packages = [
              python
              poetry
              pkgs.gcc
              pkgs.gnumake
            ];
            shellHook = lib.optionalString pkgs.stdenv.hostPlatform.isLinux ''
              export LD_LIBRARY_PATH="${
                lib.makeLibraryPath [ pkgs.stdenv.cc.cc.lib ]
              }''${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
            '';
          };

          treefmt = {
            projectRootFile = "flake.nix";
            programs.nixfmt.enable = true;
            programs.ruff-check.enable = true;
            programs.ruff-format.enable = true;
          };
        };
    };
}
