from assemblyai import TranscriptionConfig
from assemblyai import Transcriber
from assemblyai import Transcript

from mistralai import Mistral
from mistralai.models import *


def createSimpleAgent(model, name, description, client : Mistral) -> Agent:
    simple_agent = client.beta.agents.create(model=model, name=name, description=description)    
    return simple_agent

def createAssemblyAIConfig(speech_models : list[str], language_detection : bool) -> TranscriptionConfig:
    config = TranscriptionConfig(speech_models=speech_models, language_detection=language_detection)
    return config

def createAssemblyAITranscriber(config : TranscriptionConfig) -> Transcriber:
    transcriber = Transcriber(config=config)
    return transcriber

def GET(inputs : ConversationInputs, client: Mistral, agent : Agent) -> ConversationResponse:
    response = client.beta.conversations.start(agent_id=agent.id, inputs=inputs)
    return response





