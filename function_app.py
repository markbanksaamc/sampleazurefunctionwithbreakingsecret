import azure.functions as func

# Import the service blueprints
from blueprint_sample import blueprint_sample

app = func.FunctionApp()

# Register the blueprints
app.register_functions(blueprint_sample)
