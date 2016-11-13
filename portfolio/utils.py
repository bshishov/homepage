import subprocess
import os
from django.conf import settings


def url_to_pdf(url):
    output_path = os.path.join(settings.MEDIA_ROOT, 'pdf.pdf')
    subprocess.run([settings.WKHTML2PDF_CMD, url, output_path])
    return open(output_path, 'rb').read()
