"""Main script for SQL query analysis and validation."""
from pathlib import Path

from src.scripts.database import DatabaseConfig, DatabaseManager
from src.scripts.analyzer import QueryAnalyzer
from src.scripts.validator import QueryValidator
from src.scripts.constants import (
    DEFAULT_QUERIES_PATH, RESULTS_FILE,
    EXPECTED_RESULTS_DIR, REPORT_HEADER, REPORT_SEPARATOR
)


def main():
    """Main execution function."""
    config = DatabaseConfig()
    db_manager = DatabaseManager(config)
    validator = QueryValidator()
    
    try:
        db_manager.connect()
        analyzer = QueryAnalyzer(db_manager.cursor)
        
        queries = validator.read_queries(DEFAULT_QUERIES_PATH)
        report = [REPORT_HEADER]

        for i, query in enumerate(queries, start=1):
            try:
                columns, result = db_manager.execute_query(query)
                result_formatted = [" | ".join(columns)] + [" | ".join(row) for row in result]

                expected_file = f"{EXPECTED_RESULTS_DIR}/query_{i}.out"
                expected = validator.read_expected_result(expected_file)

                report.append(validator.compare_results(i, result_formatted, expected))
                report.append(analyzer.analyze(query))
                report.append(REPORT_SEPARATOR)

            except Exception as e:
                report.append(f"## ❌ Query {i}: Error\n- **Descripción**: {str(e)}\n\n")

        Path(RESULTS_FILE).write_text("\n".join(report))

    finally:
        db_manager.disconnect()


if __name__ == "__main__":
    main()
