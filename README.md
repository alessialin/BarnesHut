# Barnes-Hut Algorithm

The Barnes-Hut Algorithm[^1] is an approximation algorithm solving the [N-Body Problem](https://en.wikipedia.org/wiki/N-body_problem).


It is notable for having order **O(N log N)** compared to a direct sum - Brute Force - algorithm which would be O(N^2). The crucial idea is that it groups nearby bodies and approximates them as a single body. If the cluster is sufficiently far away, we can approximate its gravitational effect using its _center of mass_.

## Quickstart 
In order to run this in your local machine:
```
> git clone https://github.com/alessialin/BarnesHut-py.git
> cd BarnesHut
> pip install -r requirements.txt
```

NB. I'd suggest setting up a virtual environment beforehand to avoid polluting your machine's modules system.

To run the Barnes-Hut simulation:
```
> python3 ./src/BarnesHut.py
```

## Files Structure
```
├── evaluation
│   └── BarnesHut_evaluation.py
|   └── BruteForce_evaluation.py
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
|   └── BarnesHut.py
|   └── body.py
│   └── node.py
│   └── quadtree_example.py
│   └── quadtree.py
│   └── utils.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Simulation


https://user-images.githubusercontent.com/81080301/173457020-c3ca8967-6f28-4167-ab73-b338d87f2bed.mp4


## Resources
Barnes, J., & Hut, P. (1986). _A hierarchical O (N log N) force-calculation algorithm_. Nature, 324(6096), 446-449. <br />
[Wikipedia](https://en.wikipedia.org/wiki/Barnes%E2%80%93Hut_simulation) <br />
[Galaxy Simulator](https://www.beltoforion.de/en/barnes-hut-galaxy-simulator/) <br />
[Princeton CS126](https://www.cs.princeton.edu/courses/archive/fall03/cs126/assignments/barnes-hut.html)<br />
[The Barnes-Hut Approximation](https://jheer.github.io/barnes-hut/)


[^1]: The purpose of this repository is for the final submission of the course of [20602 COMPUTER SCIENCE (ALGORITHMS)](https://didattica.unibocconi.it/ts/tsn_anteprima.php?cod_ins=20602&anno=2022&ordin=IR&IdPag=6625) at Bocconi University. 
