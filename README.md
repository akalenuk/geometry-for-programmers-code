# geometry-for-programmers-code
The source code for the [Geometry for Programmers](https://www.manning.com/books/geometry-for-programmers) book.

![The book looks like this](https://images.manning.com/172/216/resize/book/e/f5d0d43-f185-455c-b4b0-17be6fc05603/Kaleniuk-MEAP-HI.png)

All the code is in Python. There are no specific dependencies on modern Python features or obscure libraries, so any generic 3.x Python will do. 

The code samples only use:
1. SymPy;
2. NumPy;
3. Matplotlib.

In early chapters, the only working tool is SymPy. We will make it solve equations and write code for us. In later chapters, the code illustrates specific algorithms and as such relies on numeric computations and visualization. That's what we need NumPy and Matplotlib for.

In general, I encourage you to treat these samples as samples and implement the algorithms in your language of preference.


## 1. Getting started 
In this chapter, the reader will learn about applied geometry and its relation to mathematics, engineering, and computer science. The chapter showcases some of its modern applications in computer-aided design and game development.  There will also be a comforting list of knowledge and skills the reader is expected to have, of which the most exotic, namely computer algebra system SymPy, will be taught on spot with a brief but good enough to get started tutorial.

## 2. Terminology and jargon (no code)
In this chapter, the reader will learn the basic language of applied geometry. In the end, they should be comfortable operating with terms like “near-degenerate triangle”, “non-manifold mesh”, or “continuous transformation”.

## 3. Geometry of linear systems
This chapter will explain the linear systems to the reader as if they were systems of lines, planes, and hyperplanes. Which, of course, from the geometric point of view, they are. The chapter will show the conditions in which such systems have computable solutions. There will be practical guidance on choosing the best algorithm for the job, and for that, an iterative linear system solving algorithm, and a direct solving algorithm will be explained graphically. In the end, the reader will be able to evaluate a linear system and solve it programmatically using the best possible tool from any library or toolkit that provides one. 

## 4. Projective geometric transformations
From this chapter, the reader will learn how the most common geometric transformations such as rotation, scale, and translation, are all generalized and extended by the projective transformation. The reader will also learn the concept of homogeneous coordinates: how adding a single number to a vector allows us to combine all the possible projective transformations into a single operation which, in practice, makes understanding transformations a little harder, but programming – much simpler.

## 5. Geometry of calculus
From this chapter, the reader will learn how calculus is connected to the geometric properties of curves and surfaces. And how to use these properties to program curves and surfaces in practice. This chapter doesn’t require the reader to be familiar with calculus, its basic concepts will be explained briefly but sufficiently to make the rest of the book comprehensible.

## 6. Polynomials
In this chapter, the reader will learn how to use polynomials as some kind of digital clay – a building material for arbitrary functions with requested properties. There will also be an explanation of the polynomial modeling downsides along with the ways to mitigate these downsides.

## 7. Splines
In this chapter, the reader will learn how to craft custom curves and surfaces with splines. The chapter will explain the general idea of splines, propose a few well-known approaches such as Bezier splines and NURBS, but also will give all the necessary toolset so the user could design their own polynomial splines with the properties they want.

## 8. Non-projective geometric transformations
In this chapter, the reader will learn about signed distance functions, and why they are becoming more and more popular in modern computer-aided design. The chapter will explain what are the benefits of signed distance functions, what are the drawbacks, how to create one, and how to turn one into a contour or mesh.

## 9. Geometry of vector algebra
In this chapter, the basics of vector algebra will be presented from a geometric perspective. The reader will learn how do vector products work, how do they generalize, and how to use their geometric properties to solve real-world problems.

## 10. Modeling shapes with signed distance functions
In this chapter, the reader will learn about signed distance functions, and why they become more and more popular in the modern computer-aided design. What are the benefits, what are the drawbacks, how to create one, and how to turn one into a contour or mesh.

## 11. Modeling surfaces with boundary representations and triangle meshes
From this chapter, the reader will learn more classical ways to model surfaces and bodies. Meshes are mostly used in game development and 3D printing, while boundary representations are mostly popular in computer-aided design. Some of the hybrid applications are emerging on the market right now, so it becomes important to know how these models compare to each other, and this chapter addresses this too.

## 12. Modeling bodies with images and voxels
In this chapter, the reader will learn about modeling bodies with 3D images and voxels. 3D images came to the software industry from medical applications such as computer tomography, but they are now used more and more in mechanical engineering too. This chapter showcases a few image processing techniques and explains a simple vectorization algorithm that turns images into contours.
