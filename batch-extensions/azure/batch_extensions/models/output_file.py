# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class OutputFile(Model):
    """A specification for uploading files from an Azure Batch node to another
    location after the Batch service has finished executing the task process.

    :param file_pattern: A pattern indicating which file(s) to upload. Both
     relative and absolute paths are supported. Relative paths are relative to
     the task working directory. For wildcards, use * to match any character
     and ** to match any directory. For example, **\\*.txt matches any file
     ending in .txt in the task working directory or any subdirectory. Note
     that \\ and / are treated interchangeably and mapped to the correct
     directory separator on the compute node operating system.
    :type file_pattern: str
    :param destination: The destination for the output file(s).
    :type destination: :class:`ExtendedOutputFileDestination
     <azure.batch_extensions.models.ExtendedOutputFileDestination>`
    :param upload_options: Additional options for the upload operation,
     including under what conditions to perform the upload.
    :type upload_options: :class:`OutputFileUploadOptions
     <azure.batch.models.OutputFileUploadOptions>`
    """

    _validation = {
        'file_pattern': {'required': True},
        'destination': {'required': True},
        'upload_options': {'required': True},
    }

    _attribute_map = {
        'file_pattern': {'key': 'filePattern', 'type': 'str'},
        'destination': {'key': 'destination', 'type': 'ExtendedOutputFileDestination'},
        'upload_options': {'key': 'uploadOptions', 'type': 'OutputFileUploadOptions'},
    }

    def __init__(self, file_pattern, destination, upload_options):
        self.file_pattern = file_pattern
        self.destination = destination
        self.upload_options = upload_options
