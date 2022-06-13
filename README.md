# Barnes-Hut Algorithm
A Python implementation of the Barnes Hut algorithm with a [simulation](https://github.com/alessialin/BarnesHut/tree/main/output) of collision of two point clouds. [^1]

The Barnes-hut Algorithm is an approximation algorithm solving the [N-Body Problem](https://en.wikipedia.org/wiki/N-body_problem). <br />
It is notable for having order **O(n log n)** compared to a direct sum - Brute Force - algorithm which would be O(n^2). The crucial idea is that it groups nearby bodies and approximates them as a single body. If the cluster is sufficiently far away, we can approximate its gravitational effect using the center its _center of mass_.

## Files Structure
```
├── evaluation
│   └── BH_evaluation.py
|   └── BruteForce.py
│   └── comparison.py
├── output
│   └── benchmark
|   │   └── BarnesHut_time.png
|   │   └── BruteForce_time.png
|   │   └── Comparison_time.png
│   └── BH_GalaxyCollision_800_v[x].mp4
│   └── BH_GalaxySimulation_800_v[x].mp4
│   └── BH_Quad.png
├── src
│   └── quadtree.py
|   └── BarnesHut.py
|   └── body.py
│   └── node.py
│   └── quadtree_example.py
│   └── utils.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Simulation


https://user-images.githubusercontent.com/81080301/173432857-0ac0e527-560d-4181-bd28-10c911697dd6.mp4


## Resources
Barnes, J., & Hut, P. (1986). A hierarchical O (N log N) force-calculation algorithm. nature, 324(6096), 446-449. <br />
[Wikipedia](https://en.wikipedia.org/wiki/Barnes%E2%80%93Hut_simulation) <br />
[Galaxy Simulator](beltoforion.de/en/barnes-hut-galaxy-simulator/) <br />
[Princeton CS126](cs.princeton.edu/courses/archive/fall03/cs126/assignments/barnes-hut.html)<br />
[The Barnes-Hut Approximation](https://jheer.github.io/barnes-hut/)


[^1]: The purpose of this repository is solely for the final submission of the course of [20602 COMPUTER SCIENCE (ALGORITHMS)](https://didattica.unibocconi.it/ts/tsn_anteprima.php?cod_ins=20602&anno=2022&ordin=IR&IdPag=6625) at Bocconi University. 
