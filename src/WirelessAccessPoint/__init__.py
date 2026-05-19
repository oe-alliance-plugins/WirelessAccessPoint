from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from gettext import bindtextdomain, dgettext, gettext


PluginLanguageDomain = "WirelessAccessPoint"


def locale_init():
	bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, "SystemPlugins/WirelessAccessPoint/locale"))


def _(txt):
	t = dgettext(PluginLanguageDomain, txt)
	if t == txt:
		t = gettext(txt)
	return t


locale_init()
language.addCallback(locale_init)

__version__ = "1.0"
