import streamlit as st
import PIL.Image
import pandas as pd

from llm import process_maintenance_form


def main():
    st.set_page_config(page_title="Maintenance Request Form Processor", layout="centered")
    
    # Application title and description
    st.title("Maintenance Request Form Processor")
    st.write("Upload a maintenance request form image to process and analyze it.")
    
    # Initialize session state if not exists
    if 'processing_complete' not in st.session_state:
        st.session_state.processing_complete = False
    if 'results' not in st.session_state:
        st.session_state.results = None

    # File uploader
    uploaded_file = st.file_uploader("Choose a maintenance form image", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        image = PIL.Image.open(uploaded_file)
        
        # Only show the image if processing is not complete
        if not st.session_state.processing_complete:
            st.subheader("Uploaded Image")
            st.image(image, use_container_width=True)
        
        # Process button
        if not st.session_state.processing_complete and st.button("Process Form", use_container_width=True):
            with st.spinner("Processing form..."):
                # Process the image
                results = process_maintenance_form(image)
                
                if results:
                    st.session_state.processing_complete = True
                    st.session_state.results = results
                    st.rerun()  # Rerun to update the UI
                
        if st.session_state.processing_complete and st.session_state.results:
            st.subheader("Extracted Information")
            
            # Convert results to DataFrame for better display
            df = pd.DataFrame(st.session_state.results)
            
            col_1, col_2 = st.columns(2)
            with col_1:
                # Display key information
                st.write("### Basic Information")
                st.write(f"Issue Type: {df['issue_type'][0]}")
                st.write(f"PFC: {df['pfc'][0]}")
                st.write(f"M/C: {df['M/C'][0]}")
                st.write(f"Work shift: {df['shift'][0]}")
                st.write(f"Date: {df['date'][0]}")
                st.write(f"Time: {df['time'][0]}")
            
            with col_2:
              st.image(image, use_container_width=True)
            
            
            # Problem Description
            st.text_area("Problem / inquiries decribtion", df['Problem / inquiries decribtion'][0], height=100, disabled=True)
            
            col_1, col_2 = st.columns(2)
            with col_1:
              st.write(f"Created By: {df['Created By'][0]}")
            with col_2:
              st.write(f"Received By: {df['Received By'][0]}")
            
            st.divider()
            
            # Root Cause
            st.text_area("Root cause / corrective actions / Spare parts", df['Root cause / corrective actions / Spare parts'][0], height=100, disabled=True)
            
            st.divider()
            
            # Preventive Action
            st.write("### Preventive Action")
            action_cols = st.columns(5)
            action_cols[0].metric("Modification", "Yes" if df['Modification'][0] else "No", border=True)
            action_cols[1].metric("POKA-YOKA", "Yes" if df['POKA-YOKA'][0] else "No", border=True)
            action_cols[2].metric("PM Task", "Yes" if df['PM Task'][0] else "No", border=True)
            action_cols[3].metric("Checklist", "Yes" if df['Checklist'][0] else "No", border=True)
            action_cols[4].metric("OPL", "Yes" if df['OPL'][0] else "No", border=True)
            
            st.divider()
            
            st.write(f"Fixed by: {df['Fixed by'][0]}")
            fix_col = st.columns(2)
            fix_col[0].write(f"Start Time: {df['Start Time'][0]}")
            fix_col[1].write(f"End time: {df['End time'][0]}")
            fix_col[1].write(f"Technician Signature: {df['Technician Signature'][0]}")
            
            st.divider()
            
            # Technical Details
            st.write("### Technical Details")
            tech_cols = st.columns(5)
            tech_cols[0].metric("Mechanical", "Yes" if df['mechanical'][0] else "No", border=True)
            tech_cols[1].metric("Electrical", "Yes" if df['electrical'][0] else "No", border=True)
            tech_cols[2].metric("Process", "Yes" if df['process'][0] else "No", border=True)
            tech_cols[3].metric("Tool Room", "Yes" if df['tool_room'][0] else "No", border=True)
            tech_cols[4].metric("Utilities", "Yes" if df['utilities'][0] else "No", border=True)
            
            st.divider()
            
            # Handover Section
            st.write("### Handover Section")
            st.metric("Accepted", "Yes" if df['accepted'][0] else "No")
            st.text_area("Handover comment", df['Handover comment'][0], height=100, disabled=True)
            handover_col = st.columns(2)
            handover_col[0].metric("Mc is clean", "Yes" if df['Mc is clean'][0] else "No")
            handover_col[0].metric("All tools are removed", "Yes" if df['All tools are removed'][0] else "No")
            handover_col[1].write(f"Operator Signature: {df['Operator Signature'][0]}")
            handover_col[1].write(f"Date: {df['operator_date'][0]}")
            handover_col[1].write(f"Time: {df['operator_time'][0]}")
            handover_col[1].write(f"Maintenance Manager: {df['Maintenance Manager'][0]}")
            
            # # Download button for full results
            # st.download_button(
            #     label="Download Full Results (JSON)",
            #     data=json.dumps(results, indent=2),
            #     file_name="maintenance_form_results.json",
            #     mime="application/json"
            # )

if __name__ == "__main__":
    main()