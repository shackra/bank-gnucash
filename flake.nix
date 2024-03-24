# This flake was initially generated by fh, the CLI for FlakeHub (version 0.1.9)
{

  # Flake inputs
  inputs = {
    pre-commit-hooks.url = "github:cachix/pre-commit-hooks.nix";
    flake-schemas.url =
      "https://flakehub.com/f/DeterminateSystems/flake-schemas/*.tar.gz";

    nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0.2311.*.tar.gz";
  };

  # Flake outputs that other flakes can use
  outputs = { self, flake-schemas, nixpkgs, pre-commit-hooks }:
    let
      # Helpers for producing system-specific outputs
      supportedSystems =
        [ "x86_64-linux" "aarch64-darwin" "x86_64-darwin" "aarch64-linux" ];
      forEachSupportedSystem = f:
        nixpkgs.lib.genAttrs supportedSystems (system:
          f {
            pkgs = import nixpkgs { inherit system; };
            inherit system;
          });
    in {
      # Schemas tell Nix about the structure of your flake's outputs
      schemas = flake-schemas.schemas;

      checks = forEachSupportedSystem ({ system, ... }: {
        pre-commit-check = pre-commit-hooks.lib.${system}.run {
          src = ./.;
          hooks = {
            # nix
            nixpkgs-fmt.enable = true;
            # python
            black.enable = true;
            isort.enable = true;
            mypy.enable = true;
            flake8.enable = true;
            # shell
            shfmt.enable = true;
            shellcheck.enable = true;
          };
        };
      });
      # Development environments
      devShells = forEachSupportedSystem ({ pkgs, ... }: {
        default = pkgs.mkShell {
          # Pinned packages available in the environment
          packages = with pkgs; [
            git
            nixpkgs-fmt

            # ⚠ PySide y Shiboken son instalados por Nix, no por poetry
            (python311.withPackages (ps:
              with ps; [
                # interprete
                python

                # pyside
                pyside6
                shiboken6
                pyside2-tools

                # desarrollo
                black
                flake8
                pytest
                python-lsp-server
                pyls-flake8
                pyls-isort
                pylsp-mypy
                python-lsp-black
              ]))
          ];

          shellHook = ''
            poetry shell
          '';
        };
      });
    };
}
