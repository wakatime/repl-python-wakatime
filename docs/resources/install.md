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

## [Nix](https://nixos.org)

For NixOS, add the following code to `/etc/nixos/configuration.nix`:

```nix
{ config, pkgs, ... }:
{
  nix.settings.experimental-features = [ "flakes" ];
  environment.systemPackages =
    let
      repl-python-wakatime = (
        builtins.getFlake "github:wakatime/repl-python-wakatime"
      ).packages.${builtins.currentSystem}.default;
    in
    [
      repl-python-wakatime
    ];
}
```

For nix,

```sh
nix shell github:wakatime/repl-python-wakatime
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
