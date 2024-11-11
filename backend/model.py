import json
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_model(class_name, fields):
    class_definition = f"class {class_name}(Base):\n"
    class_definition += f"    __tablename__ = '{class_name.lower()}'\n\n"
    class_definition += (
        f"    id = Column(Integer, primary_key=True, autoincrement=True)\n"
    )

    for field, data_type in fields.items():
        class_definition += f"    {field} = Column({data_type.capitalize()})\n"

    return class_definition


def add_function_to_crud(function_name: str, function_body: str, crud_file: str = CRUD_FILE):
    # Split the function body by lines, strip whitespace, and indent each line
    formatted_body = "\n".join(f"        {line.strip()}" for line in function_body.splitlines() if line.strip())

    # Construct the new function string without any additional escape sequences
    new_function = f"""
    async def {function_name}(self):
{formatted_body}
    """

    # Read the existing CRUD file
    with open(crud_file, "r") as file:
        crud_content = file.readlines()

    # Check if the function already exists
    if any(f"async def {function_name}(" in line for line in crud_content):
        print(f"Function {function_name} already exists in {crud_file}")
        return

    # Find the position to insert the new function
    insert_position = None
    for i, line in enumerate(crud_content):
        if "self.session = session" in line:
            insert_position = i + 1
            break

    # Insert the new function at the identified position
    if insert_position is not None:
        crud_content.insert(insert_position, "\n")  # Add a blank line before the new function
        crud_content.insert(insert_position + 1, new_function.strip() + "\n")
    else:
        crud_content.append("\n" + new_function.strip() + "\n")

    # Write the modified content back to the CRUD file
    with open(crud_file, "w") as file:
        file.writelines(crud_content)

    print(f"Function {function_name} added to {crud_file}")


def main():
    with open("tableformat.json", "r") as f:
        json_data = json.load(f)

    fields = json_data.get("fields", {})
    class_name = json_data.get("class_name", "MyModel")

    model_definition = create_model(class_name, fields)

    with open("generated_model.py", "w") as f:
        f.write("from sqlalchemy import Column, Integer, String\n")
        f.write("from sqlalchemy.ext.declarative import declarative_base\n\n")
        f.write("Base = declarative_base()\n\n")
        f.write(model_definition)


if __name__ == "__main__":
    main()
