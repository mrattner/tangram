# Development notes

All project dependencies and build scripts are defined in `package.json`. Run
`npm install` in the project directory to download the dependencies (including
Elm itself) and start using the installed command line tools within the project
directory.

You can run the `elm` executable, or any other locally installed Javascript
executable, by invoking it via `npx`. For example:

    npx elm reactor
    npx elm-test init
    npx elm make

More complex projects will probably require a more tailored invocation of
`elm make` to compile the app, and the resulting HTML/JS may be served locally
using the Node package [`http-server`](1).

## Managing build dependencies (JavaScript)

Run `npm install <package name> --save-dev` to install a new dependency, or to
update an existing one. This will install the new/updated package and update
the `package.json` file's dev dependency list accordingly.

## Managing application dependencies (Elm)

Run `npx elm install <namespace>/<package>` to add a new app dependency.
These are managed in the `elm.json` file. See the readme in the
[Elm compiler documentation](2).

Test dependencies can be added via `npx elm-test install <namespace/package>`.
This works just like `elm install` but places the package in the test dependencies
instead of the application dependencies.

Don't try to type dependencies into `elm.json` yourself, because you are likely to
run into "incompatible dependency" errors.

## Defining and running build scripts

To define a new build script, add an entry to the `scripts` object in
`package.json`. To run the script, execute the command `npm run <script name>`.
This is a handy place to define shortcuts for Elm compiler commands, building,
running, and testing.

{%- if cookiecutter.use_bulma_and_sass|lower == "y" %}
This project uses `npm-scripts-watcher` to automatically run scripts whenever
files matching specific pathnames are saved. To add a new watcher, add an entry
to the `watch` object in `package.json`. To start watching the specified paths,
execute `npm run watch`.
{%- endif %}

There are some special script names and prefixes/suffixes for script hooks. See
[NPM scripts documentation](3) for more
information.

[1]: (https://github.com/indexzero/http-server)
[2]: (https://github.com/elm/compiler/blob/master/docs/elm.json/application.md)
[3]: (https://docs.npmjs.com/misc/scripts)