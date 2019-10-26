#!c:\users\gbobt\github\poemnews\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'google-images-download==2.8.0','console_scripts','googleimagesdownload'
__requires__ = 'google-images-download==2.8.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('google-images-download==2.8.0', 'console_scripts', 'googleimagesdownload')()
    )
