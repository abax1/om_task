# Python Assessment Task
## Problem Definition
Problem definition
Given a set of edges on a regularly spaced grid find the path requiring the least time to be travelled for any 2 given points.

The edges information are provided as follows:
(vertex1, vertex2, timestep)=time

Vertices are in the excel format (e.g. A0, J9, AAZ121...), timesteps are from 0 to 9 in hours and time is also in hours but can be less than or more than 1 hour.
For timesteps: 0 means that the time needed between 00:00 and 01:00 (HH:MM format) is considered constant. 
If the last timestep (9) is surpassed (after 10:00) then the same value for timestep 9 must be used for all subsequent timesteps.

It's possible to specify a range in which the travelling can start (e.g. from 00:00 to 01:00).
The distance between 2 adjacent rows or 2 adjacent columns is 10 nautical miles. 

The grid is continuous both vertically and horizontally (e.g. passing the eastward boundary goes back to the first column on the same row).

Explain how the solution provided would work efficiently also for larger grids. Better if examples are provided.
## Solution
### Firstly, let's visualise the problem

### Assumptions
1. Edges are bi-directional