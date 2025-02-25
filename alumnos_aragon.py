def create_students_ldif(filename, class_name, num_students, base_dn):
    """Generates an LDIF file with student records for a given class and number of students."""
    
    ldif_content = ""
    
    for i in range(1, num_students + 1):
        student_id = f"{class_name}_{i:03d}"  # Student ID, e.g., "1ESOC_001"
        student_name = f"Alumno{i}"  # You can adjust the name format as needed
        student_dn = f"uid={student_id},ou={class_name},{base_dn}"
        
        ldif_content += f"""# Student {student_name} in class {class_name}
dn: {student_dn}
changetype: add
objectClass: inetOrgPerson
uid: {student_id}
cn: {student_name}
sn: {student_name}
ou: {class_name}
mail: {student_id}@example.com

"""

    try:
        with open(filename, "w") as f:
            f.write(ldif_content)
        print(f"LDIF file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# Example usage:
filename = "alumnos_vuestro_apellido.ldif"  # Name of the LDIF file
class_name = "1ESOC"  # The class to assign students to
num_students = 20  # Number of students to generate
base_dn = "dc=vuestroapellido,dc=org"  # Your base DN

print(f"Generating LDIF file for {class_name} with {num_students} students...")
create_students_ldif(filename, class_name, num_students, base_dn)
print("Process completed.")
