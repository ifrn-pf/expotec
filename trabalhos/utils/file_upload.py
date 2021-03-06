# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core.exceptions import ValidationError


def humanbytes(B):
    'Return the given bytes as a human friendly KB, MB, GB, or TB string'
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2)  # 1,048,576
    GB = float(KB ** 3)  # 1,073,741,824
    TB = float(KB ** 4)  # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B, 'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)


class UploadMaxSizeMixin(object):
    def clean_arquivo(self):
        arquivo = self.cleaned_data['arquivo']
        if arquivo.size > settings.FILE_UPLOAD_MAX_SIZE:
            raise ValidationError(
                'O arquivo deve ter no máximo %s' %
                humanbytes(settings.FILE_UPLOAD_MAX_SIZE))
        return arquivo
