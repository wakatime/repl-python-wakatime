# Install & Uninstall

## [AUR](https://aur.archlinux.org/packages/python-repl-python-wakatime)

Install:

```sh
yay -S python-repl-python-wakatime
```

uninstall:

```sh
sudo pacman -R python-repl-python-wakatime
```

## [NUR](https://nur.nix-community.org/repos/freed-wu)

```nix
{ config, pkgs, ... }:
{
  nixpkgs.config.packageOverrides = pkgs: {
    nur = import
      (
        builtins.fetchTarball
          "https://github.com/nix-community/NUR/archive/master.tar.gz"
      )
      {
        inherit pkgs;
      };
  };
  environment.systemPackages = with pkgs;
      (
        python3.withPackages (
          p: with p; [
            nur.repos.Freed-Wu.repl-python-wakatime
          ]
        )
      )
}
```

## [Nix](https://nixos.org)

```sh
nix shell github:wakatime/repl-python-wakatime
```

Run without installation:

```sh
nix run github:wakatime/repl-python-wakatime -- --help
```

## [PYPI](https://pypi.org/project/repl-python-wakatime)

Install:

```sh
pip install repl-python-wakatime
```

Uninstall:

```sh
pip uninstall repl-python-wakatime
```
