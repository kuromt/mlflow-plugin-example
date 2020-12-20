from mlflow.trackig.context.abstract_context import RunContextProvider
import mlflow

class LoggingExample(RunContextProvider):
    def in_context(self):
        return True

    def tags(self):
        return { 'mlflow.version': mlflow.__version__ }