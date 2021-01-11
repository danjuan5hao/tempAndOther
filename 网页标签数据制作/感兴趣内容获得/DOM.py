# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

class W2TDom(BeautifulSoup):
    """build DOM for Web2Text.
    output dom blocks segmented from DOM,
    content, text, tag

    PREPROCESS:
    1. empty nodes should be removed
    2. nodes have no content to extract such as <img> <br> <img> should be removed
    3. nodes have only one child should be merged with their respective child
    
    SEGMENTATION:
    DOM should be segmentated by leaves into DOM blocks

    FEATURE ENGINE
    features should be extracted from DOM blocks"""
    def __init__(self, html_text):
        super(W2TDom, self).__init__(html_text)
        

    def __repr__(self):
        return "111" 

