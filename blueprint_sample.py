"""Implements upload of a single image into EstImage """
import logging
import azure.functions as func

blueprint_sample = func.Blueprint()

@blueprint_sample.service_bus_queue_trigger(
    arg_name="message",
    queue_name="samplequeue",
    connection="SERVICE_BUS_CONNECTION_STR")
async def servicebus_trigger_blueprint_sample(message: func.ServiceBusMessage):
    logging.info('Just a sample function to build and deploy to demonstrate Azure DevOps secret issue.')
