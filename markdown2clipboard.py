import sublime, sublime_plugin
import markdown2clipboard.markdown2 as markdown2


class m2c(sublime_plugin.TextCommand):
    def run(self,edit):

                region = sublime.Region(0, self.view.size())
                originalBuffer = self.view.substr(region)                                
                message = u"selection converted and copied to clipboard"

                #contents = self.view.substr(sublime.Region(0, view.size()))
                message = u"converted and copied to clipboard"
                md = markdown2.markdown(originalBuffer,extras=['footnotes','wiki-tables'])
                sublime.set_clipboard(md)
                sublime.status_message(message)
