"""
File: main.py
Author: Sam Nolan
Email: sam.nolan@rmit.edu.au
Github: https://github.com/Hazelfire
Description:
    A description and parser of a document that sends
    a graphql request and then formats it using jinja
"""

import json
from jinja2 import Template
import requests
from docsep import parse

def graphql(url, query, session, variables):
    """ Sends a graphql request to the backend """
    return session.post(
        url,
        data={
            "query": query,
            "variables": json.dumps(variables),
        },
    ).json()

def run(endpoint, document, variables=None, session=requests.Session()):
    """ Runs the query and returns it formatted """

    if not variables:
        variables = {}

    documents = parse(document)
    queries = [doc for doc in documents if doc.name == "query"]
    displays = [doc for doc in documents if doc.name == "display"]
    return Template(displays[0].body.strip()).render(
        **graphql(endpoint, queries[0].body, session, variables)
    )
