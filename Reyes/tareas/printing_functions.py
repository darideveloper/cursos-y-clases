#Functions for importing(printing models)

def print_models(unprinted_designs:list[str], completed_models:list[str])->list:
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design.title())
        completed_models.append(current_design)
    
def show_completed_models(completed_models:list[str])->list:
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(f'\t*{completed_model.title()}')