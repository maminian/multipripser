What is this?
---

This is a Python3 interface to [https://github.com/Ripser/ripser](Ripser), a fast software for 
for the computation of Vietoris–Rips persistence barcodes. This code is almost completely 
worthless unless you already have it installed.

How does it work?
---

Ripser takes in text files for input; preferably the lower triangle of a 
distance matrix in csv (comma seperated values) format. This code takes in a point 
cloud, uses numpy to compute the distance matrix, automatically generates the file, 
automatically calls ripser, parses the output and keeps the essentials. Already built-in 
are the options to save the input/output to ripser to text files if desired. By default, 
they're deleted up automatically.

Why do this?
---

Ripser is not multithreaded, as far as we can tell. For a particular project I'm working, 
many barcodes are needed. So, I'd like to easily parallelize it using the multiprocessing 
package.

Requirements
---
Python packages:
* numpy
* multiprocessing
* matplotlib

...and most importantly,
* The ripser executable.
