from pydantic import BaseModel, Field
from typing import Optional, Literal


class MaintenanceRequestForm(BaseModel):
    """
    Pydantic model representing a Maintenance Request Form.
    """

    # --- Top Section ---
    issue_type: Literal["breakdown", "abnormality", "pm"] = Field(..., description="Type of the issue.")
    pfc: Optional[str] = Field(None, description="PFC number.")
    m_c: Optional[str] = Field(None, alias="M/C", description="Machine Code.")
    shift: Optional[str] = Field(None, description="Work shift.")
    date: str = Field(..., description="Date of the request.") # Required field.  String format to handle the input.
    time: str = Field(..., description="Time of the request.") # Required, string to handle input.
    problem_description: str = Field(..., alias="Problem / inquiries decribtion", description="Description of the problem or inquiry.")  #required.
    created_by: str = Field(..., alias="Created By", description="Name of the person who created the request.") # Required
    received_by: Optional[str] = Field(None, alias="Received By", description="Name of the person who received the request.")
    
    # --- Middle Section ---
    root_cause: Optional[str] = Field(None, alias="Root cause / corrective actions / Spare parts", description="Description of root cause, corrective actions, and spare parts used.")

    # --- Preventive Action ---
    modification: bool = Field(..., alias="Modification", description="Indicates if a Modification is required.")
    poka_yoka: bool = Field(..., alias="POKA-YOKA", description="Indicates if Poka-Yoke is required.")
    pm_task: bool = Field(..., alias="PM Task", description="Indicates if a PM Task is required.")
    checklist: bool = Field(..., alias="Checklist", description="Indicates if a Checklist is required.")
    opl: bool = Field(..., alias="OPL", description="Indicates if OPL is required.")
    
    # --- Fix and Time Section ---
    fixed_by: str = Field(..., alias="Fixed by", description="Name of the person who fixed the issue.") # Required
    start_time: str = Field(..., alias="Start Time", description="Time the repair work started.") #required, str for input.
    end_time: str = Field(..., alias="End time", description="Time the repair work ended.") # required, str for input
    technician_signature: str = Field(..., alias="Technician Signature", description="Technician's signature.") # Required

    # --- Type Checkboxes ---
    mechanical: bool = Field(..., description="Indicates if the issue is Mechanical.")
    tool_room: bool = Field(..., description="Indicates if the issue is related to the Tool Room.")
    electrical: bool = Field(..., description="Indicates if the issue is Electrical.")
    utilities: bool = Field(..., description="Indicates if the issue is related to Utilities.")
    process: bool = Field(..., description="Indicates if the issue is related to Process.")

    # --- Handover Section ---
    handover_comment: Optional[str] = Field(None, alias="Handover comment", description="Comments for handover.")
    accepted: bool = Field(..., description="Indicates if the handover was accepted.")
    mc_is_clean: bool = Field(..., alias="Mc is clean", description="Indicates if the machine is clean.")
    all_tools_are_removed: bool = Field(..., alias="All tools are removed", description="Indicates if all tools were removed.")
    operator_signature: Optional[str] = Field(None, alias="Operator Signature", description="Operator's signature.")
    operator_date: Optional[str] = Field(None, description="Date of operator signature. String to handle input.")
    operator_time: Optional[str] = Field(None, description="Time of operator signature. String to handle input.")
    maintenance_manager: Optional[str] = Field(None, alias="Maintenance Manager", description="Maintenance Manager's signature.")