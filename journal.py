import streamlit as st
import datetime
import json
import io
import base64

def main():
    # ------------------- STYLES -------------------
    st.markdown("""
        <style>
        body {
            background: linear-gradient(to bottom right, #e4d9f7, #d6e9f9) !important;
        }
        .big-title {
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            color: #8A6FD1;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #A89CD4;
        }
        .nav-button {
            display: inline-block;
            padding: 5px 15px;
            background-color: #8A6FD1;
            color: white;
            border-radius: 20px;
            text-decoration: none;
            font-size: 0.9em;
            margin: 10px 0;
            transition: all 0.3s ease;
        }
        .nav-button:hover {
            background-color: #7860c1;
            transform: translateY(-2px);
        }
        .journal-card {
            background-color: rgba(255, 255, 255, 0.7);
            border-radius: 15px;
            padding: 25px;
            margin: 15px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #8A6FD1;
        }
        .entry-date {
            font-size: 1.2em;
            font-weight: bold;
            color: #6a5acd;
        }
        </style>
    """, unsafe_allow_html=True)

    # ------------------ NAVIGATION -----------------
    st.markdown("""
        <a href="?page=home" target="_self" class="nav-button">← Back to Home</a>
    """, unsafe_allow_html=True)

    # ------------------ UI HEADER ------------------
    st.markdown("<div class='big-title'>Serenity Journal</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Your private space for reflection and growth</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Initialize session state for journal entries if not already present
    if 'journal_entries' not in st.session_state:
        st.session_state.journal_entries = {}
        
    # -------------------- TABS ---------------------
    tab1, tab2, tab3 = st.tabs(["Write Entry", "Past Entries", "Import/Export"])
    
    with tab1:
        # Journal entry form
        st.header("New Journal Entry")
        
        # Date selector defaulting to today
        today = datetime.date.today()
        date = st.date_input("Date", today)
        
        # Mood selector
        mood = st.selectbox("How are you feeling today?", [
            "Happy", "Calm", "Grateful", "Motivated", "Neutral", 
            "Tired", "Anxious", "Stressed", "Overwhelmed", "Sad"
        ])
        
        # Journal prompts
        prompts = [
            "What's on your mind today?",
            "What are you grateful for today?",
            "What emotion was most present for you today? Why do you think that is?",
            "What's something you're looking forward to tomorrow?",
            "What was challenging today, and how did you overcome it?",
            "What's something that made you smile today?",
            "What's a lesson you learned today?",
            "If you could change one thing about today, what would it be?",
        ]
        
        selected_prompt = st.selectbox("Journal Prompt (optional)", ["No prompt"] + prompts)
        prompt_text = "" if selected_prompt == "No prompt" else selected_prompt
        
        # Journal entry
        st.write("Your Journal Entry:")
        entry = st.text_area("", height=300, placeholder="Start writing here..." if not prompt_text else prompt_text)
        
        # Gratitude list
        st.write("Gratitude List (optional):")
        gratitude_cols = st.columns(3)
        gratitude_items = []
        
        for i in range(3):
            with gratitude_cols[i]:
                item = st.text_input(f"I'm grateful for...", key=f"gratitude_{i}")
                if item:
                    gratitude_items.append(item)
        
        # Save button
        if st.button("Save Entry", type="primary"):
            if entry:
                # Create journal entry object
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                journal_entry = {
                    "date": date.strftime("%Y-%m-%d"),
                    "mood": mood,
                    "prompt": prompt_text,
                    "entry": entry,
                    "gratitude": gratitude_items,
                    "timestamp": timestamp
                }
                
                # Generate a unique key for this entry
                entry_key = f"journal_entry_{date.strftime('%Y%m%d')}_{datetime.datetime.now().strftime('%H%M%S')}"
                
                # Save to session state
                st.session_state.journal_entries[entry_key] = journal_entry
                
                st.success("Journal entry saved successfully!")
                # Clear the form
                st.rerun()  # Changed from experimental_rerun() to rerun()
            else:
                st.warning("Please write something in your journal entry before saving.")
        
    with tab2:
        # Past entries section
        st.header("Your Past Entries")
        
        entries = list(st.session_state.journal_entries.keys())
        
        if not entries:
            st.info("You haven't created any journal entries yet. Start writing to see them here!")
        else:
            # Sort entries by date (newest first)
            entries.sort(reverse=True)
            
            # Create a dropdown to select an entry with improved formatting
            def format_entry_key(key):
                # Extract date and time from the key
                parts = key.replace("journal_entry_", "").split("_")
                if len(parts) == 2:
                    date_str, time_str = parts
                    # Format date as YYYY-MM-DD
                    formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
                    # Format time as HH:MM
                    formatted_time = f"{time_str[:2]}:{time_str[2:4]}"
                    return f"{formatted_date} at {formatted_time}"
                return key
            
            selected_entry_key = st.selectbox(
                "Select an entry to view:", 
                entries, 
                format_func=format_entry_key
            )
            
            if selected_entry_key:
                entry = st.session_state.journal_entries[selected_entry_key]
                
                # Process the entry text to replace newlines with HTML breaks
                entry_text = entry['entry'].replace('\n', '<br>')
                
                # Create gratitude list HTML if it exists
                gratitude_section = ""
                if entry['gratitude']:
                    gratitude_items = "".join([f"<li>{item}</li>" for item in entry['gratitude']])
                    gratitude_section = f"<h4>Gratitude List:</h4><ul>{gratitude_items}</ul>"
                
                # Display the entry with proper HTML rendering
                st.markdown(
                    f"""
                    <div class='journal-card'>
                        <div class='entry-date'>{entry['date']} - {entry['mood']}</div>
                        <p><em>Prompt: {entry['prompt'] if entry['prompt'] else 'No prompt used'}</em></p>
                        <p>{entry_text}</p>
                        {gratitude_section if entry['gratitude'] else ""}
                        <p><small>Written on {entry['timestamp']}</small></p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                
                # Add delete button
                if st.button("Delete this entry", key="delete_entry"):
                    # Remove entry from session state
                    del st.session_state.journal_entries[selected_entry_key]
                    st.success("Entry deleted successfully!")
                    st.rerun()  # Changed from experimental_rerun() to rerun()
    
    with tab3:
        st.header("Save and Restore Your Journal")
        
        # Export functionality
        st.subheader("Export Journal")
        if st.session_state.journal_entries:
            # Convert the journal entries dictionary to JSON
            json_str = json.dumps(st.session_state.journal_entries, indent=4)
            
            # Create a download link
            b64 = base64.b64encode(json_str.encode()).decode()
            today_str = datetime.date.today().strftime("%Y%m%d")
            file_name = f"serenity_journal_{today_str}.json"
            href = f'<a href="data:file/json;base64,{b64}" download="{file_name}">Download Journal Entries</a>'
            st.markdown(href, unsafe_allow_html=True)
            
            st.info("💡 Download your journal periodically to ensure you don't lose your entries.")
        else:
            st.warning("No journal entries to export yet. Write some entries first!")
        
        # Import functionality
        st.subheader("Import Journal")
        uploaded_file = st.file_uploader("Upload a previously exported journal file", type="json")
        
        if uploaded_file is not None:
            try:
                # Read the JSON file
                journal_data = json.load(uploaded_file)
                
                # Confirm import
                if st.button("Import These Entries"):
                    # Merge with existing entries (new entries will overwrite if keys match)
                    st.session_state.journal_entries.update(journal_data)
                    st.success(f"Successfully imported {len(journal_data)} journal entries!")
                    st.rerun()  # Changed from experimental_rerun() to rerun()
            except Exception as e:
                st.error(f"Error importing journal file: {e}")

    # ------------------- FOOTER ----------------------
    st.markdown("""
        <hr style='border: 0.5px solid #ccc;'>
        <div style='text-align: center; color: gray;'>
            🌿 Your thoughts matter. Your journey matters. 🌿
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(page_title="Serenity - Journal", page_icon="📔", layout="centered")
    main()
