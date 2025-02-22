from test_unstructured.partition.test_constants import EXPECTED_TABLE, EXPECTED_TEXT
from unstructured.cleaners.core import clean_extra_whitespace
from unstructured.documents.elements import Table
from unstructured.partition.tsv import partition_tsv

EXPECTED_FILETYPE = "text/tsv"


def test_partition_tsv_from_filename(filename="example-docs/stanley-cups.tsv"):
    elements = partition_tsv(filename=filename)

    assert clean_extra_whitespace(elements[0].text) == EXPECTED_TEXT
    assert elements[0].metadata.text_as_html == EXPECTED_TABLE
    assert elements[0].metadata.filetype == EXPECTED_FILETYPE


def test_partition_tsv_from_file(filename="example-docs/stanley-cups.tsv"):
    with open(filename, "rb") as f:
        elements = partition_tsv(file=f)

    assert clean_extra_whitespace(elements[0].text) == EXPECTED_TEXT
    assert isinstance(elements[0], Table)
    assert elements[0].metadata.text_as_html == EXPECTED_TABLE
    assert elements[0].metadata.filetype == EXPECTED_FILETYPE


def test_partition_tsv_can_exclude_metadata(filename="example-docs/stanley-cups.tsv"):
    elements = partition_tsv(filename=filename, include_metadata=False)

    assert clean_extra_whitespace(elements[0].text) == EXPECTED_TEXT
    assert isinstance(elements[0], Table)
    assert elements[0].metadata.text_as_html is None
    assert elements[0].metadata.filetype is None
