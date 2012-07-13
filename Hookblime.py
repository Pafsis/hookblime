import sublime_plugin
import subprocess


class Hookblime(sublime_plugin.EventListener):
    """Excecutes user set hooks on file events"""

    def _get_hook(self, view, hook_name):
        """Gets the hook string from the settings, returing the scoped one if
        exists, the global one otherwise, or None in case both are missing."""
        settings = view.settings().get("hookblime", None)
        if settings is None:
            return None

        scope = (view.syntax_name(view.sel()[0].b)).split().pop()
        scope_settings = settings.get(scope, {})
        hook = scope_settings.get(hook_name, None)
        return hook or settings.get(hook_name, None)

    def _call_hook(self, view, hook_name):
        """Calls the corresponding hook based on the view's scope and the
        hook_name. If the hook has 'append_filename' set to true, the view's
        path is passed as the hook last argument."""
        hook = self._get_hook(view, hook_name)
        if hook:
            file_name = view.file_name() or ""
            call_args = hook["cmd"].split()
            if hook.get("append_filename", False):
                call_args.append(file_name)
            subprocess.call(call_args, shell=True)

    def on_new(self, view):
        self._call_hook(view, "on_new")

    def on_load(self, view):
        self._call_hook(view, "on_load")

    def on_close(self, view):
        self._call_hook(view, "on_close")

    def on_pre_save(self, view):
        self._call_hook(view, "on_pre_save")

    def on_post_save(self, view):
        self._call_hook(view, "on_post_save")
