# Tangram
A template for creating projects in the [Elm][1] language, made using
[cookiecutter][2].

## Prerequisites
### Cookiecutter
Install the [cookiecutter][3] application to be able to use the template.
Requires Python.

### NodeJS
You must have a working installation of NodeJS on your computer. If you are on
a Linux system, the easiest way to install Node is via [n-install][4], which
installs the `n` version manager for Node without requiring a previous
installation of Node. The package repositories for Node in APM, etc. tend to be
very out of date, so using `n` is far preferable to installing Node via your
Linux distribution.

If the command `node` results in the error *"The program 'nodejs' is currently
not installed,"* you need to add a symbolic link from the command `nodejs` to
the version of Node that `n` has installed:

    $ sudo ln -s ~/n/bin/node /usr/bin/nodejs

To allow NPM, the Node Package Manager, to check for updates when you run it,
run the suggested command to allow read access to the update config store:

    $ sudo chown -R $USER:$(id -gn $USER) ~/.config

## Using the template
Provide the URL to the Git repository to create a templated project in the
current directory:

    $ cookiecutter gh:mrattner/tangram

Follow the prompts, or press ENTER to accept the default values. Install the
JavaScript dependencies by running `npm install` in the project directory.

[1]: http://elm-lang.org/
[2]: http://cookiecutter.readthedocs.io/en/latest/usage.html
[3]: http://cookiecutter.readthedocs.io/en/latest/installation.html
[4]: https://github.com/mklement0/n-install