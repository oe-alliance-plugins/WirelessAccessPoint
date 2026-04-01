from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.WirelessAccessPoint'
setup(name='enigma2-plugin-systemplugins-wirelessaccesspoint',
       version='3.0',
       description='Using a Wireless module as AP.',
       package_dir={pkg: 'WirelessAccessPoint'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
