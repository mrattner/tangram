# {{ cookiecutter.project_name }}

I don't do a whole lot yet.

# Using npm

All project dependencies and build scripts are defined in `package.json`.

## Dependencies

Run `npm install <package name> --save-dev` to install a new dependency, or to
update an existing one. This will install the new/updated package and update
the package JSON file's dev dependency list accordingly.

## Build scripts

To define a new build script, add an entry to the `scripts` object in
`package.json`. To run the script, execute the command `npm run <script name>`.

{%- if cookiecutter.use_bulma_and_sass|lower == "y" %}
This project uses `npm-scripts-watcher` to automatically run scripts whenever
files matching specific pathnames are saved. To add a new watcher, add an entry
to the `watch` object in `package.json`. To start watching the specified paths,
execute `npm run watch`.
{%- endif %}

There are some special script names and prefixes/suffixes for script hooks. See
[NPM scripts documentation](https://docs.npmjs.com/misc/scripts) for more
information.