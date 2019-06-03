"""
File: test_graphjinj.py
Author: Sam Nolan
Email: sam.nolan@rmit.edu.au
Github: https://github.com/Hazelfire
Description: Tests the overall functionality of graphjinj
"""

from importlib.resources import read_text
from unittest.mock import Mock
import requests
import graphjinj

def test_graphjinj():
    """ Tests whether graphjinj works correctly """
    session = requests.Session()
    mock_response = Mock()
    mock_response.json = lambda: {
        "data": {
            "allTasks": {
                "edges": [
                    {
                        "node": {
                            "name": "task1"
                            }
                        },
                    {
                        "node": {
                            "name": "task2"
                            }
                        }
                    ]
                }
            }
        }
    session.post = Mock(return_value=mock_response)
    result = graphjinj.run(
        "endpoint",
        read_text("test.examples", "getTasks.gjinj"),
        session=session
    )
    assert "task1" in result
    assert "task2" in result
