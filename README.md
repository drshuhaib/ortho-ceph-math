# ortho-ceph-math

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)

A modular, unit-tested Python library for automated Steiner cephalometric analysis. Designed for clinical R&D, dental software integration, and AI vision pipelines.

## Overview
This library provides a clean, dependency-free mathematical engine to calculate skeletal and dental relationships from cephalometric landmarks. It is engineered for modularity, allowing dental engineers to drop this logic into CAD modules, 3D Slicer plugins, or web-based diagnostic agents.

## Core Features
*   **Steiner Analysis Core:** Calculates SNA, SNB, ANB, and incisor inclinations.
*   **Modular Architecture:** Separates geometric math from UI logic for easy integration.
*   **Unit-Tested:** Built with clinical accuracy in mind.

## Integration
This math core is designed to be imported into larger clinical workflows:
```python
from ceph_analysis.steiner import run_steiner_analysis

# Dictionary of (x, y) coordinates for 8 standard landmarks
landmarks = {"S": (100, 100), "N": (100, 200), ...} 

results = run_steiner_analysis(landmarks)
print(f"Diagnosis: {results['Diagnosis']}")
