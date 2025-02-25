def create_organizational_units_ldif(filename, ou_list, base_dn):
    """Creates an LDIF file for multiple organizational units."""

    ldif_content = ""
    for ou_name in ou_list:
        ldif_content += f"""# Organisational unit for {ou_name} department
        dn: ou={ou_name},{base_dn}
        changetype: add
        objectClass: organizationalUnit
        ou: {ou_name}

        """
    
    try:
        with open(filename, "w") as f:
            f.write(ldif_content)
        print(f"LDIF file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")

# Example usage:
filename = "oueso1aragon.ldif"

