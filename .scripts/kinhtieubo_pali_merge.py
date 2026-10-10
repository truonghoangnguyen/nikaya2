#!/usr/bin/env python3
"""
Merge các file kinh tiểu bộ từ 3 số thành 2 số.
Ví dụ: mil-3-1-1-mahavagga.md, mil-3-1-2-mahavagga.md -> mil-3-1-mahavagga.md",
"""

import os
import re
from collections import defaultdict

# ===== CẤU HÌNH =====
input_files = [
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-1-1-arambhakatha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-2-bahirakatha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-1-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-2-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-3-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-4-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-5-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-6-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-7-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-8-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-9-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-10-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-11-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-12-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-13-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-14-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-15-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-1-16-mahavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-2-1-addhanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-2-2-addhanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-2-3-addhanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-2-4-addhanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-2-5-addhanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-2-6-addhanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-2-7-addhanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-2-8-addhanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-2-9-addhanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-1-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-2-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-3-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-4-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-5-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-6-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-7-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-8-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-9-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-10-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-11-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-12-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-13-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-3-14-vicaravagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-4-1-nibbanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-4-2-nibbanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-4-3-nibbanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-4-4-nibbanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-4-5-nibbanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-4-6-nibbanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-4-7-nibbanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-4-8-nibbanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-4-9-nibbanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-4-10-nibbanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-5-1-buddhavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-5-2-buddhavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-5-3-buddhavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-5-4-buddhavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-5-5-buddhavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-5-6-buddhavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-5-7-buddhavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-5-8-buddhavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-5-9-buddhavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-5-10-buddhavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-6-1-sativagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-6-2-sativagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-6-3-sativagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-6-4-sativagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-6-5-sativagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-6-6-sativagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-6-7-sativagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-6-8-sativagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-6-9-sativagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-6-10-sativagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-6-11-sativagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-1-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-2-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-3-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-4-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-5-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-6-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-7-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-8-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-9-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-10-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-11-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-12-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-13-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-14-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-15-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-7-16-arupadhammavavatthanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-3-8-8-milindapanhapucchavisajjana.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-4-1-mendakapanharambhakatha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-4-2-mendakapanharambhakatha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-4-3-mendakapanharambhakatha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-4-4-mendakapanharambhakatha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-4-5-mendakapanharambhakatha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-4-6-mendakapanharambhakatha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-1-1-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-1-2-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-1-3-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-1-4-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-1-5-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-1-6-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-1-7-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-1-8-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-1-9-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-1-10-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-2-1-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-2-2-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-2-3-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-2-4-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-2-5-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-2-6-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-2-7-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-2-8-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-3-1-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-3-2-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-3-3-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-3-4-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-3-5-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-3-6-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-3-7-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-3-8-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-3-9-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-3-10-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-3-11-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-3-12-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-4-1-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-4-2-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-4-3-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-4-4-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-4-5-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-4-6-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-4-7-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-4-8-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-4-9-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-4-10-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-5-1-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-5-2-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-5-3-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-5-4-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-5-5-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-5-6-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-5-7-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-5-8-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-5-9-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-5-10-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-5-5-11-mendakapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-1-1-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-1-2-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-1-3-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-1-4-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-1-5-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-1-6-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-1-7-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-1-8-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-1-9-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-2-1-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-2-2-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-2-3-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-2-4-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-2-5-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-2-6-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-2-7-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-2-8-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-2-9-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-2-10-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-3-1-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-3-2-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-3-3-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-3-4-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-3-5-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-3-6-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-3-7-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-3-8-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-3-9-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-3-10-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-3-11-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-3-12-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-4-1-anumanavagga.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-6-4-2-anumanapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-1-7-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-2-1-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-2-2-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-2-3-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-2-4-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-2-5-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-2-6-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-2-7-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-2-8-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-2-9-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-2-10-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-3-1-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-3-2-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-3-3-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-3-4-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-3-5-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-3-6-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-3-7-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-3-8-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-3-9-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-3-10-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-4-1-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-4-2-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-4-3-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-4-4-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-4-5-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-4-6-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-4-7-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-4-8-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-4-9-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-4-10-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-5-1-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-5-2-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-5-3-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-5-4-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-5-5-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-5-6-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-5-7-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-5-8-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-5-9-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-5-10-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-6-1-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-6-2-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-6-3-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-6-4-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-6-5-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-6-6-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-6-7-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-6-8-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-6-9-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-6-10-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-7-1-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-7-2-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-7-3-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-7-4-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-7-5-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-7-6-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-7-7-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-7-8-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-7-9-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-7-10-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-8-1-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-8-2-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-8-3-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-8-4-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-8-5-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-8-6-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-7-8-7-opammakathapanha.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/mil-8-nigamana.md",
    # ... thêm các file khác vào đây
]

out = "/Users/ng/projects/nikaya2/docs/kinhtieubo/pali/mil/1merge"   # thư mục output
# ====================


def parse_filename(filepath):
    """
    Phân tích tên file, trả về (numbers, suffix).
    numbers: list các số (dạng string) nằm giữa 'mil' và suffix.
    suffix: phần tên phía sau (ví dụ: mahavagga, arambhakatha).
    Trả về None nếu không khớp mẫu.
    """
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    parts = name.split('-')
    if len(parts) < 3 or parts[0] != 'mil':
        return None
    suffix = parts[-1]
    numbers = parts[1:-1]
    return numbers, suffix


def transform_content(content, file_numbers):
    """
    Chuyển đổi nội dung file:
    - Bỏ dòng H1 (bắt đầu bằng '# ')
    - Thay dòng H2 đầu tiên: '## <số>. <tiêu đề>' thành '## <file_numbers>. <tiêu đề>'
    - Loại bỏ các dòng trống ở đầu.
    """
    lines = content.splitlines()
    new_lines = []
    h1_removed = False
    for line in lines:
        if not h1_removed and line.startswith("# "):
            h1_removed = True
            continue
        new_lines.append(line)

    # Tìm và sửa dòng H2 đầu tiên
    for i, line in enumerate(new_lines):
        if line.startswith("## "):
            m = re.match(r"^##\s+\d+\.\s+(.*)$", line)
            if m:
                title = m.group(1)
                new_lines[i] = f"## {file_numbers}. {title}"
            break

    # Xóa các dòng trống ở đầu
    while new_lines and new_lines[0].strip() == "":
        new_lines.pop(0)

    return "\n".join(new_lines) + "\n"


def main():
    # Tạo thư mục output nếu chưa tồn tại
    os.makedirs(out, exist_ok=True)

    groups = defaultdict(list)

    for fp in input_files:
        if not os.path.exists(fp):
            print(f"Cảnh báo: Không tìm thấy file {fp}")
            continue

        parsed = parse_filename(fp)
        if parsed is None:
            print(f"Bỏ qua {fp} (không đúng định dạng)")
            continue

        numbers, suffix = parsed
        if len(numbers) == 3:
            key = (numbers[0], numbers[1], suffix)
            groups[key].append((fp, numbers))
        elif len(numbers) == 2:
            print(f"Bỏ qua {fp} (đã có 2 số)")
        else:
            print(f"Bỏ qua {fp} (không phải 3 số)")

    for key, items in groups.items():
        num1, num2, suffix = key
        # Sắp xếp theo số thứ 3 (chuyển sang int để so sánh)
        items.sort(key=lambda x: int(x[1][2]))

        output_filename = f"mil-{num1}-{num2}-{suffix}.md"
        output_path = os.path.join(out, output_filename)

        transformed_contents = []
        for fp, nums in items:
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            file_numbers = ".".join(nums)  # ví dụ: "3.1.1"
            transformed = transform_content(content, file_numbers)
            transformed_contents.append(transformed)

        # Ghép nội dung, giữa các phần có một dòng trống
        merged = "\n\n".join(tc.strip() for tc in transformed_contents) + "\n"

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(merged)

        print(f"Đã merge {len(items)} file thành {output_path}")


if __name__ == "__main__":
    main()