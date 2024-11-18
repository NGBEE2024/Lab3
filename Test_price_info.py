#Test_price_info.py
import price_info as PI
def test_cost_of_fruits():
    # Test for specific fruits with known quantities
    assert PI.cost_of_fruits('apple', 10) == 12.0, "Test for apple failed"
    #assert PI.cost_of_fruits('unknown_fruit', 5) == 0, "Test for unknown fruit failed"

def test_total_cost_shopping():
    # Verify the total shopping cost
    expected_total = (1.20 * 5) + (1.40 * 5) + (6.50 * 1) + (2.70 * 2) + \
                     (0.90 * 10) + (2.95 * 1) + (4.95 * 2)
    assert PI.total_cost_shopping() == expected_total, "Total cost calculation failed"