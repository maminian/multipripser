What is this?
---

This is a Python3 interface to [Ripser](https://github.com/Ripser/ripser), a fast software for 
for the computation of Vietoris–Rips persistence barcodes. This code is almost completely 
worthless unless you already have it installed.

How does it work?
---

Ripser takes in text files for input; preferably the lower triangle of a 
distance matrix in csv (comma seperated values) format. This code takes in a point 
cloud, uses numpy to compute the distance matrix, automatically generates the file, 
calls ripser, parses the output, and keeps the essentials. Already built-in 
are the options to save the input/output to ripser to text files if desired. By default, 
they're deleted automatically (you can save the results to a similar pickle file).

Why do this?
---

Ripser is not multithreaded, as far as I can tell. For a particular project I'm working, 
barcodes over many realizations of probability densities ae needed. 
So, I'd like to parallelize it using the multiprocessing package.

Requirements
---

Python packages:
* numpy
* multiprocessing
* matplotlib

...and most importantly,
* The ripser executable, which is a C++ program and requires its own compiling.
