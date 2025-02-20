import streamlit as st
import json
from config import client, workers_name
from work_order import MaintenanceRequestForm



def process_maintenance_form(image):
    """Process the maintenance form image using Gemini API"""
    prompt = f"""
    You are a maintenance request form generator. Please provide the following information:
        - Issue type (breakdown, abnormality, pm)
        - PFC number (if applicable)
        - Machine Code (if applicable)
        - Work shift (if applicable)
        - Date of the request
        - Time of the request
        - Problem description
        - Created by
        - Received by (if applicable)

        - Root cause / corrective actions / spare parts (if applicable)

        - Modification required? (True/False)
        - Poka-Yoke required? (True/False)
        - PM Task required? (True/False)
        - Checklist required? (True/False)
        - OPL required? (True/False)

        - Fixed by
        - Start time 
        - End time
        - Technician signature

        - The issue is Mechanical (True/False)
        - The issue is related to the Tool Room (True/False)
        - The issue is Electrical (True/False)
        - The issue is related to Utilities (True/False)
        - The issue is related to Process (True/False)

        - Handover Comment
        - The handover was accepted (True/False)
        - The machine is clean (True/False)
        - All tools were removed (True/False)
        - Operator's signature
        - Date of operator signature
        - Time of operator signature
        - Maintenance Manager's signature
    
    IMPORTANT:
      - Select the Issue type according to which checkbox is marked breakdown, abnormality, or pm.
      
      - Extract names and signatures then see which name is similar to it from this worker name list and select it: {workers_name}.

    """.strip()

# - Problem description and Root cause MUST have meaning not just random words.

    try:
        response = client.models.generate_content(
            model="gemini-2.0-pro-exp-02-05",
            contents=[prompt, image],
            config={
                'response_mime_type': 'application/json',
                'response_schema': list[MaintenanceRequestForm]
            })
        return json.loads(response.text)
    except Exception as e:
        st.error(f"Error processing form: {str(e)}")
        return None