"""
Pytest autograder for Unit 2 Lab - Student Report Card Analyzer
Tests Bronze, Silver, and Gold tiers (10 tests each)
"""

import pytest
import importlib
import os
import glob


# --- Dynamic Import ---
# Find the student's submission file based on tier naming convention

def _import_student_module():
    """Import the student's lab file (unit2_lab_gold.py, unit2_lab_silver.py, or unit2_lab_bronze.py)."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for tier in ["gold", "silver", "bronze"]:
        filepath = os.path.join(base_dir, f"unit2_lab_{tier}.py")
        if os.path.exists(filepath):
            spec = importlib.util.spec_from_file_location(f"unit2_lab_{tier}", filepath)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod, tier
    pytest.skip("No student submission file found (unit2_lab_bronze/silver/gold.py)")


module, tier = _import_student_module()


# ===================== BRONZE TESTS (analyze_name) =====================

class TestBronze:
    """Tests for analyze_name() - 10 test cases."""

    def test_basic_name(self):
        result = module.analyze_name("Sherlock Holmes")
        assert result == ("Sherlock Holmes", 2, 4, "SH")

    def test_leading_trailing_whitespace(self):
        result = module.analyze_name("   Sherlock Holmes   ")
        assert result == ("Sherlock Holmes", 2, 4, "SH")

    def test_single_word_name(self):
        result = module.analyze_name("Madonna")
        assert result == ("Madonna", 1, 3, "M")

    def test_three_word_name(self):
        result = module.analyze_name("Mary Jane Watson")
        assert result == ("Mary Jane Watson", 3, 5, "MJW")

    def test_all_lowercase(self):
        clean, wc, vc, initials = module.analyze_name("john doe")
        assert clean == "john doe"
        assert wc == 2
        assert vc == 3
        assert initials == "JD"

    def test_all_uppercase(self):
        clean, wc, vc, initials = module.analyze_name("ALICE BOB")
        assert clean == "ALICE BOB"
        assert wc == 2
        assert vc == 4
        assert initials == "AB"

    def test_no_vowels(self):
        clean, wc, vc, initials = module.analyze_name("Gym Myth")
        assert clean == "Gym Myth"
        assert wc == 2
        assert vc == 0
        assert initials == "GM"

    def test_all_vowels_name(self):
        clean, wc, vc, initials = module.analyze_name("Aoi Ue")
        assert clean == "Aoi Ue"
        assert wc == 2
        assert vc == 5
        assert initials == "AU"

    def test_extra_internal_spaces_stripped(self):
        """Leading/trailing whitespace stripped; internal spacing preserved by split/join."""
        result = module.analyze_name("  Ada Lovelace  ")
        assert result[0] == "Ada Lovelace"
        assert result[1] == 2
        assert result[3] == "AL"

    def test_four_word_name(self):
        clean, wc, vc, initials = module.analyze_name("Sir Arthur Conan Doyle")
        assert clean == "Sir Arthur Conan Doyle"
        assert wc == 4
        assert vc == 7
        assert initials == "SACD"


# ===================== SILVER TESTS (build_seating_chart) =====================

class TestSilver:
    """Tests for build_seating_chart() - 10 test cases."""

    @pytest.fixture(autouse=True)
    def _check_tier(self):
        if tier == "bronze":
            pytest.skip("Silver tests skipped for bronze submission")

    def test_returns_tuple(self):
        result = module.build_seating_chart(3, 3)
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_correct_dimensions(self):
        original, _ = module.build_seating_chart(3, 3)
        assert len(original) == 3
        assert all(len(row) == 3 for row in original)

    def test_alice_placement(self):
        original, _ = module.build_seating_chart(3, 3)
        assert original[0][0] == "Alice"

    def test_bob_placement(self):
        original, _ = module.build_seating_chart(3, 3)
        assert original[1][2] == "Bob"

    def test_charlie_in_original(self):
        original, _ = module.build_seating_chart(3, 3)
        assert original[2][1] == "Charlie"

    def test_charlie_not_in_backup(self):
        """Backup should NOT contain Charlie — tests deep copy."""
        _, backup = module.build_seating_chart(3, 3)
        assert backup[2][1] == "empty"

    def test_backup_has_alice(self):
        _, backup = module.build_seating_chart(3, 3)
        assert backup[0][0] == "Alice"

    def test_backup_has_bob(self):
        _, backup = module.build_seating_chart(3, 3)
        assert backup[1][2] == "Bob"

    def test_rows_are_independent(self):
        """Each row should be a separate list (no aliasing bug)."""
        original, _ = module.build_seating_chart(3, 3)
        # If rows are aliased, Alice would appear in all rows
        assert original[1][0] != "Alice"
        assert original[2][0] != "Alice"

    def test_original_and_backup_independent(self):
        """Modifying original after return should not affect backup."""
        original, backup = module.build_seating_chart(3, 3)
        original[0][1] = "TestChange"
        assert backup[0][1] == "empty"


# ===================== GOLD TESTS (calculate_grade_report) =====================

class TestGold:
    """Tests for calculate_grade_report() - 10 test cases."""

    @pytest.fixture(autouse=True)
    def _check_tier(self):
        if tier in ("bronze", "silver"):
            pytest.skip("Gold tests skipped for bronze/silver submission")

    SAMPLE_GRADES = {
        "Alice": [85, 92, 78, 90],
        "Bob": [72, 68, 81, 75],
        "Charlie": [95, 98, 100, 92],
        "Diana": [60, 55, 70, 65],
    }

    def test_returns_tuple_of_three(self):
        result = module.calculate_grade_report(self.SAMPLE_GRADES)
        assert isinstance(result, tuple)
        assert len(result) == 3

    def test_report_contains_all_students(self):
        report, _, _ = module.calculate_grade_report(self.SAMPLE_GRADES)
        assert set(report.keys()) == {"Alice", "Bob", "Charlie", "Diana"}

    def test_alice_average(self):
        report, _, _ = module.calculate_grade_report(self.SAMPLE_GRADES)
        assert report["Alice"][0] == pytest.approx(86.25)

    def test_alice_high_low(self):
        report, _, _ = module.calculate_grade_report(self.SAMPLE_GRADES)
        assert report["Alice"][1] == 92
        assert report["Alice"][2] == 78

    def test_bob_stats(self):
        report, _, _ = module.calculate_grade_report(self.SAMPLE_GRADES)
        assert report["Bob"][0] == pytest.approx(74.0)
        assert report["Bob"][1] == 81
        assert report["Bob"][2] == 68

    def test_charlie_stats(self):
        report, _, _ = module.calculate_grade_report(self.SAMPLE_GRADES)
        assert report["Charlie"][0] == pytest.approx(96.25)
        assert report["Charlie"][1] == 100
        assert report["Charlie"][2] == 92

    def test_top_student(self):
        _, top, _ = module.calculate_grade_report(self.SAMPLE_GRADES)
        assert top == "Charlie"

    def test_lowest_student(self):
        _, _, lowest = module.calculate_grade_report(self.SAMPLE_GRADES)
        assert lowest == "Diana"

    def test_single_student(self):
        grades = {"Solo": [88, 92, 76]}
        report, top, lowest = module.calculate_grade_report(grades)
        assert report["Solo"][0] == pytest.approx(85.333, rel=1e-2)
        assert report["Solo"][1] == 92
        assert report["Solo"][2] == 76
        assert top == "Solo"
        assert lowest == "Solo"

    def test_tied_averages(self):
        grades = {
            "X": [80, 80],
            "Y": [70, 90],
        }
        report, top, lowest = module.calculate_grade_report(grades)
        assert report["X"][0] == pytest.approx(80.0)
        assert report["Y"][0] == pytest.approx(80.0)
        # Both have same average — either is acceptable as top/lowest
        assert top in ("X", "Y")
        assert lowest in ("X", "Y")
