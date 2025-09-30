def analyze_log_entry(log_message: str, log_level: int):
    level_dict = {
        -1: "Error",
        1: "Informational",
        2: "Warning",
        3: "Critical"
    }
    final_message = None

    try:
        level_name = level_dict[log_level]
    except KeyError:
        raise ValueError(f"Unexpected log_level value was passed, {log_level}.")
    
    if log_level == 3:
        final_message = f"{level_name} ALERT: {log_message}."
    else:
        final_message = f"{level_name}: {log_message}"

    return final_message

print(analyze_log_entry("MySQL starting up", 1))
print(analyze_log_entry("I/O Fail", 3))
print(analyze_log_entry("ms-suite unexpectedely crashed", 2))
print(analyze_log_entry("I am an evil attacker", -2))
