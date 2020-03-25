import os

from design_patterns.factory.creators.transport_creators import TransportationCreator, TruckCreator

def consumer(creator: TransportationCreator):
    """Consumer Transportation client
    """    
    transport = creator.create_transport()
    print(f"This is how my package will be delivered: {transport.delivery()}")

if __name__ == "__main__":
    try:
        consumer(TruckCreator())
    except ModuleNotFoundError as module:
        print(module)
    except ImportError as import_e:
        print(import_e)

    finally:
        os.path
