import sys
import os

def extract_logs(log_file, target_date):
    """Extract logs for a given date from a large log file efficiently."""
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    with open(log_file, "r", encoding="utf-8") as file, open(output_file, "w", encoding="utf-8") as output:
        for line in file:
            if line.startswith(target_date):  # Fast comparison
                output.write(line)

    print(f"Logs for {target_date} saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python src/extract_logs.py <log_file> <YYYY-MM-DD>")
        sys.exit(1)

    log_file = sys.argv[1]
    target_date = sys.argv[2]

    extract_logs(log_file, target_date)
