# Heuristics for the Travelling Salesman Prorblem

<b>Course Name:</b> Introduction to Algorithms and Data Structures
<br><b>Coursework Name:</b> Heuristics for the Travelling Salesman Problem
<br><b>Programming Language:</b> Python3.
<br><b>Final Mark:</b> 97%

## Description of the coursework

The purpose of this project is to try several known heuristics to solve the Travelling Salesman Problem modelled as a graph. For this project, we will use a weight function between nodes which will correspond to the Euclidean distance as long as those files are under the <em>euclidean-tests</em> directory. 

On the other hand, if we are considering non-euclidean tests, the distance will be provided in the files themselves.

There are some tests provided already, but it is really easy to create your own or to get some real city from the internet and try the heuristics on it. Anyways, considering the files provided (cities25, cities50 and cities75 for the Euclidean case whilst sixnodes is for the non-Euclidean case).

Given a set of nodes, try to find the optimal order so that the cost of a tour is minimal.
There are several files (cities25, cities50, cities75 & sixnodes) which are used
as input and from which a graph will be created. The graph for the first three files
is created using the euclidean distance whilst that is not the case for the last one.

From there, in graph.py there are several functions which try several approaches
to the problem and output the value of the tour. 

I have uploaded a document which analyses how these functions compare to each other
and the possible imporvements which could be done.

## Files
<ul>
  <li> <a href="./coursework-document.pdf">coursework-document.pdf</a> --> This pdf file contains the description followed to complete the project.</li>
  <li> <a href="./Report-TSP.pdf">heatmap</a> --> This .pdf file contains the report explaining my solution to the given coursework.</li>
  <li> <a href="./python-files">heatmap</a> --> This directory contains the files which contain the written code.</li>
  <li> <a href="./tests">heatmap</a> --> This directory contains the whole files which can be used to test the code and, consequently, the heuristics implemented to the TSP.</li>
</ul>
  
## Getting Started

These subsections will help you get a copy of the project and understand how to run it on your local machine for development and testing purposes.
I will discuss how to clone this repository and set it up in any IDE of your choice. Furthermore, instructions on how to run the server will be given as well as how to build & run the project from the terminal.

### How to Install

The first thing you should do is clone this repository into your local machine. You can do this with the following command:
```
git clone https://github.com/Paramiru/Heatmap
```
Once you have cloned the repository, you should check your current version of Java. I used Java 11 (LTS) for the project. You can check the version you are currently using running this command in the terminal.
```
java --version
```
It is worth mentioning that you do not have to worry about the dependencies since they are in the file pom.xml, which you can find inside the heatmap directory. Maven will take care of downloading anything you do not currently have so that you can run the project.

If you have a previous version of Java 11, you can download it from Oracle's website.

Once you have cloned the repository, you can import the Maven project to your preferred IDE. I used Eclipse, but feel free to use whichever you are most comfortable with. 
You can check the Java version you are using for the project. In order to do that, find "JRE System Library" in the Package Explorer and select "Properties". Change "Execution environment" to be "JavaSE-11".

## Running the Project 

Having built the project, you will see a runnable file inside the heatmap/target folder <b>heatmap-0.0.1-SNAPSHOT.jar</b>
Run the .jar file using:
```
java -jar heatmap-0.0.1-SNAPSHOT.jar ../predictions.txt
```
where ../predictions.txt correspond to the text file which sould be in the heatmap directory.

## Screenshots

<p align="center">
  <img width="460" src="">
  <br>
  Rendered heatmap from given predictions in coursework document
</p>

## Authors

* **Pablo Miró** - [Paramiru](https://github.com/Paramiru)
