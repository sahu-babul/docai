import json
import pandas as pd
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from ai_ocr.azure.config import get_config


config = get_config()

document_analysis_client = DocumentAnalysisClient(
    endpoint=config["doc_intelligence_endpoint"],
    credential=AzureKeyCredential(config["doc_intelligence_key"]),
    headers={"x-ms-useragent": "DOCAI-1.0"}
)

def get_ocr_results(file_path: str, model_name: str = "prebuilt-layout"):
    with open(file_path, "rb") as f:
        poller = document_analysis_client.begin_analyze_document(
            model_id=model_name,
            document=f
        )

    result = poller.result()
    ocr_result = ""
    for page in result.pages:
        for line in page.lines:
            ocr_result += line.content + "\n"
    return ocr_result

