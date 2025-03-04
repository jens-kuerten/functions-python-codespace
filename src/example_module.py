import logging

from csfunctions.events import DocumentReleaseCheckEvent
from csfunctions.metadata import MetaData
from csfunctions.service import Service
from csfunctions.actions import AbortAndShowErrorAction


def example_doc_release_check(metadata: MetaData, event: DocumentReleaseCheckEvent, service: Service):
    """
    Example Function. 
    Checks if the document is a Test document and if so, it aborts the release and shows an error message.
    """
    # We can use the logging module to log messages that will be visible in the logs.
    logging.info("Triggered by %s", metadata.app_user)

    # The event data contains a list of documents that are about to be released.
    for document in event.data.documents:
        logging.info("Processing document %s", document.titel)

        # If we find a document with the title "Test", we return an abort action.
        if document.titel == "Test":
            return AbortAndShowErrorAction(
                message="You are not allowed to release Test documents!"
            )
        