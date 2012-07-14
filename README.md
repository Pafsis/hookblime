# Hookblime

Hookblime lets you easily add hooks to execute your own scripts on file events.

Hook scripts are executed by the user's default shell\*, giving you the
possibity of using shell-scripting oneliners.

## Supported events

These are the currently supported events:

* on_new: Executed when a new file tab created.
* on_load: Executed when an existing file is opened.
* on_close: Executed when a tab is closed.
* on_pre_save: Executed before a file is saved.
* on_post_save: Executed after a file is saved.

## Configuration

Hookblime can be configured at any level of the
[Sublime's settings hierachy](http://www.sublimetext.com/docs/2/settings.html),
both in global and scoped ways.

All configuration must be set in an entry called "hookblime", containing a dict
for each global hook and scope. Each scope must contain its desired hooks.

Each hook dict must have a "cmd" string value with the script to execute, and
can have an optional boolean entry called "replace_filename" which if true,
makes the plugin replace the string "%(file_name)" with the current file's path.
Note that on_new and on_close hooks can be triggered by non-saved files, in
which cases an empty path will appended.

If both global and scoped hooks are matched, only the later would be executed.

Sample configuration:

    "hookblime" : {
        "source.python" : {
            "on_post_save" : {
                "cmd": "python_saved %(file_name)",
                "replace_filename": true
            }
        },
        "on_new" : {
            "cmd": "global_hook_new_tab"
        }
    }

\* The working directory of the scripts is always the user's home.
