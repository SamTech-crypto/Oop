import os
import shutil

def process_file():
    try:
        # Ask the user for the input file name
        input_filename = input("📂 Enter the input filename (e.g., input.txt): ").strip()

        # Check if the input file exists
        if not os.path.isfile(input_filename):
            print(f"❌ Error: File '{input_filename}' does not exist.")
            return

        # Ask the user for the output file name
        output_filename = input("💾 Enter the output filename (e.g., output.txt): ").strip()

        # Backup the output file if it already exists
        if os.path.exists(output_filename):
            backup_name = output_filename + ".bak"
            shutil.copy(output_filename, backup_name)
            print(f"🔁 Existing '{output_filename}' backed up as '{backup_name}'")

        # Read the content of the input file
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Process the content
        upper_content = content.upper()
        word_count = len(content.split())
        line_count = len(content.splitlines())

        # Prepare the result
        summary = (
            f"\n\n--- Summary ---\n"
            f"Original File: {input_filename}\n"
            f"Word Count: {word_count}\n"
            f"Line Count: {line_count}\n"
        )
        final_output = upper_content + summary

        # Write the processed content to the output file
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(final_output)

        print(f"✅ Success! Processed content written to '{output_filename}'")

    except PermissionError:
        print("🔒 Error: Permission denied. Check your file permissions.")
    except UnicodeDecodeError:
        print("⚠️ Error: Unable to read the file due to encoding issues.")
    except Exception as e:
        print(f"🚨 Unexpected error: {e}")

# Run the advanced file processor
process_file()
