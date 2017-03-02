# Genome_Browser
Group Project for BBK Biocomputing II 

Create a database tier:
Design a relational database in which you will store appropriate pieces of data from the Genbank file. What data are appropriate will be up to you to decide given the other requirements of the project.
Write a parser that can extract the relevant data from the Genbank file and convert the data to SQL that can be loaded into the database. Note that your parser will have to deal with identifying intron/exon boundaries and finding the coding sequence of the DNA (see notes below).
The database tier also needs to provide a 'data access tier' - Python wrappers to the SQL that return the data required by the middle tier - i.e. an abstraction of the database design that returns the data requested.
Create a middle layer / tier:
For practical reasons, you might choose that the person implementing the middle tier implements the data access tier, but if they do so then these must be wrapped in their own routines and not embedded within subroutines that manipulate the data (i.e. the 'logic tier'). In other words there must be a clear separation between the 'data tier' and the 'logic tier'.
The logic tier contains the "business rules" that take requests from the interface, extract data from the data tier, perform any needed processing of the data, including any calculations that need to be done. Note that the logic tier will not povide any information on how the results should be presented.
Web-based graphical user interface (front-end tier):
A (set of) web pages that allow the user to query the database - via the middle tier.
Supporting Python/CGI scripts that access the business logic layer of code when forms are submitted and generate new pages.
Requirements for the queries are listed below.
