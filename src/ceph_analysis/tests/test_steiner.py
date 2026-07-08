from src.ceph_analysis.steiner import run_steiner_analysis

def test_analysis():
    # Simple dummy coordinates
    points = {
        "S": (100, 100), "N": (100, 200), "A": (150, 200), "B": (140, 250),
        "U1A": (150, 180), "U1T": (150, 220), "L1A": (140, 230), "L1T": (140, 270)
    }
    results = run_steiner_analysis(points)
    assert "SNA" in results
    print("Test Passed: Steiner logic is functional.")

if __name__ == "__main__":
    test_analysis()
