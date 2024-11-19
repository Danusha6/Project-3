import csv
from binary_search_tree import Node, BinarySearchTree

class PatientRecord:
    def __init__(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        # Initializes the patient record with various attributes
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature

    def __repr__(self):
        # Returns a string representation of the patient record for display
        return (f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, "
                f"Diagnosis: {self.diagnosis}, BP: {self.blood_pressure}, Pulse: {self.pulse}, "
                f"Temp: {self.body_temperature}")

class PatientRecordManagementSystem:
    def __init__(self):
        # Initializes the BST for storing patient records
        self.bst = BinarySearchTree()

    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        """Adds a new patient record to the BST."""
        # Creates a new patient record and inserts it into the BST
        record = PatientRecord(patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature)
        self.bst.insert(Node(patient_id, record))

    def search_patient_record(self, patient_id):
        """Searches for a patient record in the BST by patient ID."""
        # Searches for a patient record by its unique ID and returns the record if found
        node = self.bst.search(patient_id)
        return node.value if node else None

    def delete_patient_record(self, patient_id):
        """Deletes a patient record from the BST by patient ID."""
        # Removes the patient record associated with the given patient ID
        self.bst.remove(patient_id)

    def display_all_records(self):
        """Displays all patient records using an inorder traversal."""
        # Returns a list of all patient records in the BST by performing an inorder traversal
        return self.bst.inorder_traversal(self.bst.root)

    def build_tree_from_csv(self, file_path):
        """Builds the BST from a CSV file containing patient records."""
        # Reads patient records from a CSV file and adds them to the BST
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Adds each record from the CSV file to the BST
                self.add_patient_record(
                    int(row['PatientID']),
                    row['Name'],
                    int(row['Age']),
                    row['Diagnosis'],
                    row['BloodPressure'],
                    int(row['Pulse']),
                    float(row['BodyTemperature'])
                )

    def visualize_tree(self):
        """Visualizes the BST using Graphviz and returns the Graphviz object."""
        # Generates a visual representation of the BST using Graphviz
        from graphviz import Digraph
        dot = Digraph()
        self._add_nodes(dot, self.bst.root)  # Helper method to recursively add nodes
        return dot

    def _add_nodes(self, dot, node):
        """A helper method for adding nodes and edges to the Graphviz object."""
        # Recursively adds nodes and edges to the Graphviz object to represent the BST structure
        if node:
            # Add the current node to the Graphviz object
            dot.node(str(node.key), f"{node.value.name}")
            if node.left:
                # Add an edge for the left child node
                dot.edge(str(node.key), str(node.left.key))
                self._add_nodes(dot, node.left)  # Recursively process the left child
            if node.right:
                # Add an edge for the right child node
                dot.edge(str(node.key), str(node.right.key))
                self._add_nodes(dot, node.right)  # Recursively process the right child
