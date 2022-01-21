import sys
import subprocess

def main():
    # NOTE Use universal_newlines=True to force Popen to return str over bytes to avoid working out which decode to use
    p = subprocess.Popen("git ls-files --others --exclude-standard", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    out, err = p.communicate()

    migrations = []
    for unchecked_rp in out.split('\n'):
        if "migrations" in unchecked_rp and unchecked_rp.lower().endswith(".py"):
            # Look for a Migration class just to be sure?
            with open(unchecked_rp) as maybe_migration_fh:
                for line in maybe_migration_fh:
                    if "class Migration" in line:
                        migrations.append(unchecked_rp)
                        break

    if len(migrations) > 0:
        sys.stderr.write("Unchecked migrations detected: \n")
        for migration_name in migrations:
            sys.stderr.write(f"  * {migration_name}\n")
        sys.stderr.write("Commit all these files to permit a commit.\n")
        return 1

    return 0

if __name__ == '__main__':
    sys.exit( main() )
