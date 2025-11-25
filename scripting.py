import streamlit as st

st.set_page_config(
    page_title="SCU Scripting",
    layout="wide"
)

# ---------- SIDEBAR CONTROLS ----------

scenario_option = st.sidebar.selectbox(
    "Select scenario",
    [
        "run and drives/ over 700/ with title",
        "runs and drives/ over 700/ without title",
        "runs and drives/ under 700/ with title",
        "runs and drives/ under 700/ without title",
        "No run and drive/ over 700/ with title",
        "no run and drive/ over 700/ without title",
        "no run and drive/ under 700/ with title",
        "no run and drive/ under 700/ without title",
    ],
    index=0
)

customer_accepts = st.sidebar.radio(
    "customer accepts offer?",
    ["Yes", "No"],
    index=0
)


# ---------- HELPER BLOCKS ----------

def yes_no_radio(prompt, key):
    return st.radio(prompt, ["Yes", "No"], key=key)


def damage_block(prefix: str, step_label: str, summary):
    st.markdown(f"{step_label} damage/missing parts notes")
    val = yes_no_radio(
        "Is there any major damage or missing parts inside or outside the vehicle? Yes/no",
        key=f"{prefix}_damage_missing",
    )
    summary.append(f"Is there any major damage or missing parts inside or outside the vehicle?: {val}")
    notes = st.text_area("damage/missing parts notes", key=f"{prefix}_damage_missing_notes")
    summary.append(f"damage/missing parts notes: {notes}")


def proof_of_ownership_radio(prefix: str, summary):
    val = st.radio(
        "What proof of ownership do you have (bill of sale, insurance, registration, non available)?",
        ["bill of sale", "insurance", "registration", "non available"],
        key=f"{prefix}_proof_ownership",
    )
    summary.append(f"What proof of ownership do you have: {val}")
    return val


def run_with_jump_radio(prefix: str, summary):
    val = yes_no_radio("Can it run with a jump?", key=f"{prefix}_run_with_jump")
    summary.append(f"Can it run with a jump?: {val}")
    return val


# ---------- SCENARIO RENDER FUNCTIONS ----------

# Scenario 1: Running And Driving | Over $700 | With Title.
def render_scenario_1(customer_accepts: str):
    st.markdown("### Scenario 1: Running And Driving | Over $700 | With Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario: Running And Driving | Over $700 | With Title")
        summary.append("customer accepts offer?: Yes")

        st.markdown("customer accepts offer? Yes")
        st.markdown("1. sounds great! Let’s confirm some info and get you scheduled")

        # 2. title/mileage notes
        st.markdown("2. title/mileage notes")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s1_acc_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s1_acc_liens")
        v3 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s1_acc_miles")
        notes = st.text_area("title/mileage notes", key="s1_acc_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Just to confirm the car has xxx miles?: {v3}")
        summary.append(f"title/mileage notes: {notes}")

        # 3. driving notes
        st.markdown("3. driving notes")
        drive_quality = st.radio("How does your car drive? Good/bad", ["Good", "Bad"], key="s1_acc_drive_quality")
        daily_use = yes_no_radio("Is it good for daily use? Yes/no", key="s1_acc_daily_use")
        move_5ft = yes_no_radio("Can it move forward and backward at least 5ft? yes/no", key="s1_acc_move_5ft")
        engine_noise = yes_no_radio("Does the car have any engine noise? Yes/no", key="s1_acc_engine_noise")
        drive_notes = st.text_area("driving notes", key="s1_acc_driving_notes")

        summary.append(f"How does your car drive?: {drive_quality}")
        summary.append(f"Is it good for daily use?: {daily_use}")
        summary.append(f"Can it move forward and backward at least 5ft?: {move_5ft}")
        summary.append(f"Does the car have any engine noise?: {engine_noise}")
        summary.append(f"driving notes: {drive_notes}")

        # 4. damage/missing parts notes
        damage_block(prefix="s1_acc", step_label="4.", summary=summary)

        # Is vehicle as described?
        vehicle_described = st.radio(
            "Is vehicle as described? Yes/No",
            ["Yes", "No"],
            key="s1_acc_vehicle_described"
        )
        summary.append(f"Is vehicle as described?: {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get address for pickup")
            st.markdown("Get Pics of Title front & back")
            st.markdown("Get pics of dash with engine running")
            st.markdown("Ask for video of engine running (Not Required if not BB offer)")
            summary.append("Next steps: Get address for pickup; Get Pics of Title front & back; "
                           "Get pics of dash with engine running; Ask for video of engine running (Not Required if not BB offer)")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            did_offer_change = st.radio(
                "Did offer change? Yes/No",
                ["Yes", "No"],
                key="s1_acc_offer_change"
            )
            summary.append(f"Did offer change?: {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get address for pickup")
                st.markdown("Get Pics of Title front & back")
                st.markdown("Get pics of dash with engine running")
                st.markdown("Ask for video of engine running (Not Required if not BB offer)")
                summary.append("Next steps: Get address for pickup; Get Pics of Title front & back; "
                               "Get pics of dash with engine running; Ask for video of engine running (Not Required if not BB offer)")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario: Running And Driving | Over $700 | With Title")
        summary.append("customer accepts offer?: No")

        st.markdown("customer accepts offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. title/mileage notes
        st.markdown("1. title/mileage notes")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s1_rej_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s1_rej_liens")
        v3 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s1_rej_miles")
        notes = st.text_area("title/mileage notes", key="s1_rej_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Just to confirm the car has xxx miles?: {v3}")
        summary.append(f"title/mileage notes: {notes}")

        # 2. driving notes
        st.markdown("2. driving notes")
        drive_quality = st.radio("How does your car drive? Good/bad", ["Good", "Bad"], key="s1_rej_drive_quality")
        daily_use = yes_no_radio("Is it good for daily use? Yes/no", key="s1_rej_daily_use")
        move_5ft = yes_no_radio("Can it move forward and backward at least 5ft? yes/no", key="s1_rej_move_5ft")
        engine_noise = yes_no_radio("Does the car have any engine noise? Yes/no", key="s1_rej_engine_noise")
        drive_notes = st.text_area("driving notes", key="s1_rej_driving_notes")

        summary.append(f"How does your car drive?: {drive_quality}")
        summary.append(f"Is it good for daily use?: {daily_use}")
        summary.append(f"Can it move forward and backward at least 5ft?: {move_5ft}")
        summary.append(f"Does the car have any engine noise?: {engine_noise}")
        summary.append(f"driving notes: {drive_notes}")

        # 3. damage/missing parts notes
        damage_block(prefix="s1_rej", step_label="3.", summary=summary)

        # 4. pics & vin
        st.markdown("4. pics & vin")
        st.markdown(
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle, "
            "dash with the engine turned on. VIN and 10 Sec video of the engine running? "
            "(See if customer will send it while on the phone.)"
        )
        pics_vin = st.text_area("pics & vin", key="s1_rej_pics_vin")
        summary.append(f"pics & vin notes: {pics_vin}")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 2: Running And Driving | Over $700 | Without Title.
def render_scenario_2(customer_accepts: str):
    st.markdown("### Scenario 2: Running And Driving | Over $700 | Without Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario: Running And Driving | Over $700 | Without Title")
        summary.append("customer accepts offer?: Yes")

        st.markdown("customer accepts offer? Yes")
        st.markdown("1. sounds great! Let’s confirm some info and get you scheduled")

        # 2. title/mileage notes
        st.markdown("2. title/mileage notes")
        st.markdown("I see there is no title, may I ask what happened with it?")
        summary.append("Customer statement: I see there is no title, may I ask what happened with it?")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s2_acc_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s2_acc_liens")
        v3 = yes_no_radio("Is it possible to get the title? Yes/no", key="s2_acc_possible_title")
        po = proof_of_ownership_radio("s2_acc", summary)
        v4 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s2_acc_miles")
        notes = st.text_area("title/mileage notes", key="s2_acc_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Is it possible to get the title?: {v3}")
        summary.append(f"Just to confirm the car has xxx miles?: {v4}")
        summary.append(f"title/mileage notes: {notes}")

        # 3. driving notes
        st.markdown("3. driving notes")
        drive_quality = st.radio("How does your car drive? Good/bad", ["Good", "Bad"], key="s2_acc_drive_quality")
        daily_use = yes_no_radio("Is it good for daily use? Yes/no", key="s2_acc_daily_use")
        move_5ft = yes_no_radio("Can it move forward and backward at least 5ft? yes/no", key="s2_acc_move_5ft")
        engine_noise = yes_no_radio("Does the car have any engine noise? Yes/no", key="s2_acc_engine_noise")
        drive_notes = st.text_area("driving notes", key="s2_acc_driving_notes")

        summary.append(f"How does your car drive?: {drive_quality}")
        summary.append(f"Is it good for daily use?: {daily_use}")
        summary.append(f"Can it move forward and backward at least 5ft?: {move_5ft}")
        summary.append(f"Does the car have any engine noise?: {engine_noise}")
        summary.append(f"driving notes: {drive_notes}")

        # 4. damage/missing parts notes
        damage_block(prefix="s2_acc", step_label="4.", summary=summary)

        # Is vehicle as described?
        vehicle_described = st.radio(
            "Is vehicle as described? Yes/No",
            ["Yes", "No"],
            key="s2_acc_vehicle_described"
        )
        summary.append(f"Is vehicle as described?: {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get address for pickup")
            st.markdown("Get Pics of ID front & back")
            st.markdown("Get pics of Proof of Ownership")
            st.markdown("Get pics of dash with engine running")
            st.markdown("Ask for video of engine running (Not Required if not BB offer)")
            st.markdown("Send to manager for review")
            summary.append("Next steps: Get address for pickup; Get Pics of ID front & back; "
                           "Get pics of Proof of Ownership; Get pics of dash with engine running; "
                           "Ask for video of engine running (Not Required if not BB offer); "
                           "Send to manager for review")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            did_offer_change = st.radio(
                "Did offer change? Yes/No",
                ["Yes", "No"],
                key="s2_acc_offer_change"
            )
            summary.append(f"Did offer change?: {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get address for pickup")
                st.markdown("Get Pics of ID front & back")
                st.markdown("Get pics of Proof of Ownership")
                st.markdown("Get pics of dash with engine running")
                st.markdown("Ask for video of engine running (Not Required if not BB offer)")
                st.markdown("Send to manager for review")
                summary.append("Next steps: Get address for pickup; Get Pics of ID front & back; "
                               "Get pics of Proof of Ownership; Get pics of dash with engine running; "
                               "Ask for video of engine running (Not Required if not BB offer); "
                               "Send to manager for review")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario: Running And Driving | Over $700 | Without Title")
        summary.append("customer accepts offer?: No")

        st.markdown("customer accepts offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. title/mileage notes
        st.markdown("1. title/mileage notes: I see there is no title, may I ask what happened with it?")
        st.markdown("I see there is no title, may I ask what happened with it?")
        summary.append("Customer statement: I see there is no title, may I ask what happened with it?")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s2_rej_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s2_rej_liens")
        po = proof_of_ownership_radio("s2_rej", summary)
        v3 = yes_no_radio("Is it possible to get the title? Yes/no", key="s2_rej_possible_title")
        v4 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s2_rej_miles")
        notes = st.text_area("title/mileage notes", key="s2_rej_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Is it possible to get the title?: {v3}")
        summary.append(f"Just to confirm the car has xxx miles?: {v4}")
        summary.append(f"title/mileage notes: {notes}")

        # 2. driving notes
        st.markdown("2. driving notes")
        drive_quality = st.radio("How does your car drive? Good/bad", ["Good", "Bad"], key="s2_rej_drive_quality")
        daily_use = yes_no_radio("Is it good for daily use? Yes/no", key="s2_rej_daily_use")
        move_5ft = yes_no_radio("Can it move forward and backward at least 5ft? yes/no", key="s2_rej_move_5ft")
        engine_noise = yes_no_radio("Does the car have any engine noise? Yes/no", key="s2_rej_engine_noise")
        drive_notes = st.text_area("driving notes", key="s2_rej_driving_notes")

        summary.append(f"How does your car drive?: {drive_quality}")
        summary.append(f"Is it good for daily use?: {daily_use}")
        summary.append(f"Can it move forward and backward at least 5ft?: {move_5ft}")
        summary.append(f"Does the car have any engine noise?: {engine_noise}")
        summary.append(f"driving notes: {drive_notes}")

        # 3. damage/missing parts notes
        damage_block(prefix="s2_rej", step_label="3.", summary=summary)

        # 4. pics & vin
        st.markdown("4. pics & vin")
        st.markdown(
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle, "
            "dash with the engine turned on. VIN and 10 Sec video of the engine running? "
            "(See if customer will send it while on the phone.)"
        )
        pics_vin = st.text_area("pics & vin", key="s2_rej_pics_vin")
        summary.append(f"pics & vin notes: {pics_vin}")
        summary.append("Action: Send to manager for review.")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 3: Running And Driving | under $700 | With Title.
def render_scenario_3(customer_accepts: str):
    st.markdown("### Scenario 3: Running And Driving | under $700 | With Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario: Running And Driving | under $700 | With Title")
        summary.append("customer accepts offer?: Yes")

        st.markdown("customer accepts offer? Yes")
        st.markdown("1. sounds great! Let’s confirm some info and get you scheduled")

        # 2. title/mileage notes
        st.markdown("2. title/mileage notes")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s3_acc_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s3_acc_liens")
        v3 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s3_acc_miles")
        notes = st.text_area("title/mileage notes", key="s3_acc_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Just to confirm the car has xxx miles?: {v3}")
        summary.append(f"title/mileage notes: {notes}")

        # 3. driving notes
        st.markdown("3. driving notes")
        drive_quality = st.radio("How does your car drive? Good/bad", ["Good", "Bad"], key="s3_acc_drive_quality")
        daily_use = yes_no_radio("Is it good for daily use? Yes/no", key="s3_acc_daily_use")
        move_5ft = yes_no_radio("Can it move forward and backward at least 5ft? yes/no", key="s3_acc_move_5ft")
        engine_noise = yes_no_radio("Does the car have any engine noise? Yes/no", key="s3_acc_engine_noise")
        drive_notes = st.text_area("driving notes", key="s3_acc_driving_notes")

        summary.append(f"How does your car drive?: {drive_quality}")
        summary.append(f"Is it good for daily use?: {daily_use}")
        summary.append(f"Can it move forward and backward at least 5ft?: {move_5ft}")
        summary.append(f"Does the car have any engine noise?: {engine_noise}")
        summary.append(f"driving notes: {drive_notes}")

        # 4. damage/missing parts notes
        damage_block(prefix="s3_acc", step_label="4.", summary=summary)

        # Is vehicle as described?
        vehicle_described = st.radio(
            "Is vehicle as described? Yes/No",
            ["Yes", "No"],
            key="s3_acc_vehicle_described"
        )
        summary.append(f"Is vehicle as described?: {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get address for pickup")
            st.markdown("Get Pics of Title front & back")
            st.markdown("Get pics of dash with engine running")
            st.markdown("Ask for video of engine running (Not Required if not BB offer)")
            summary.append("Next steps: Get address for pickup; Get Pics of Title front & back; "
                           "Get pics of dash with engine running; Ask for video of engine running (Not Required if not BB offer)")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            did_offer_change = st.radio(
                "Did offer change? Yes/No",
                ["Yes", "No"],
                key="s3_acc_offer_change"
            )
            summary.append(f"Did offer change?: {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get address for pickup")
                st.markdown("Get Pics of Title front & back")
                st.markdown("Get pics of dash with engine running")
                st.markdown("Ask for video of engine running (Not Required if not BB offer)")
                summary.append("Next steps: Get address for pickup; Get Pics of Title front & back; "
                               "Get pics of dash with engine running; Ask for video of engine running (Not Required if not BB offer)")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario: Running And Driving | under $700 | With Title")
        summary.append("customer accepts offer?: No")

        st.markdown("customer accepts offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. title/mileage notes
        st.markdown("1. title/mileage notes")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s3_rej_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s3_rej_liens")
        v3 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s3_rej_miles")
        notes = st.text_area("title/mileage notes", key="s3_rej_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Just to confirm the car has xxx miles?: {v3}")
        summary.append(f"title/mileage notes: {notes}")

        # 2. driving notes
        st.markdown("2. driving notes")
        drive_quality = st.radio("How does your car drive? Good/bad", ["Good", "Bad"], key="s3_rej_drive_quality")
        daily_use = yes_no_radio("Is it good for daily use? Yes/no", key="s3_rej_daily_use")
        move_5ft = yes_no_radio("Can it move forward and backward at least 5ft? yes/no", key="s3_rej_move_5ft")
        engine_noise = yes_no_radio("Does the car have any engine noise? Yes/no", key="s3_rej_engine_noise")
        drive_notes = st.text_area("driving notes", key="s3_rej_driving_notes")

        summary.append(f"How does your car drive?: {drive_quality}")
        summary.append(f"Is it good for daily use?: {daily_use}")
        summary.append(f"Can it move forward and backward at least 5ft?: {move_5ft}")
        summary.append(f"Does the car have any engine noise?: {engine_noise}")
        summary.append(f"driving notes: {drive_notes}")

        # 3. damage/missing parts notes
        damage_block(prefix="s3_rej", step_label="3.", summary=summary)

        # 4. pics & vin
        st.markdown("4. pics & vin")
        st.markdown(
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle, "
            "dash with the engine turned on. VIN and 10 Sec video of the engine running? "
            "(See if customer will send it while on the phone.)"
        )
        pics_vin = st.text_area("pics & vin", key="s3_rej_pics_vin")
        summary.append(f"pics & vin notes: {pics_vin}")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 4: Running And Driving | under $700 | Without Title.
def render_scenario_4(customer_accepts: str):
    st.markdown("### Scenario 4: Running And Driving | under $700 | Without Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario: Running And Driving | under $700 | Without Title")
        summary.append("customer accepts offer?: Yes")

        st.markdown("customer accepts offer? Yes")
        st.markdown("1. sounds great! Let’s confirm some info and get you scheduled")

        # 2. title/mileage notes
        st.markdown("2. title/mileage notes: I see there is no title, may I ask what happened with it?")
        st.markdown("I see there is no title, may I ask what happened with it?")
        summary.append("Customer statement: I see there is no title, may I ask what happened with it?")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s4_acc_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s4_acc_liens")
        v3 = yes_no_radio("Is it possible to get the title? Yes/no", key="s4_acc_possible_title")
        po = proof_of_ownership_radio("s4_acc", summary)
        v4 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s4_acc_miles")
        notes = st.text_area("title/mileage notes", key="s4_acc_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Is it possible to get the title?: {v3}")
        summary.append(f"Just to confirm the car has xxx miles?: {v4}")
        summary.append(f"title/mileage notes: {notes}")

        # 3. driving notes
        st.markdown("3. driving notes")
        drive_quality = st.radio("How does your car drive? Good/bad", ["Good", "Bad"], key="s4_acc_drive_quality")
        daily_use = yes_no_radio("Is it good for daily use? Yes/no", key="s4_acc_daily_use")
        move_5ft = yes_no_radio("Can it move forward and backward at least 5ft? yes/no", key="s4_acc_move_5ft")
        engine_noise = yes_no_radio("Does the car have any engine noise? Yes/no", key="s4_acc_engine_noise")
        drive_notes = st.text_area("driving notes", key="s4_acc_driving_notes")

        summary.append(f"How does your car drive?: {drive_quality}")
        summary.append(f"Is it good for daily use?: {daily_use}")
        summary.append(f"Can it move forward and backward at least 5ft?: {move_5ft}")
        summary.append(f"Does the car have any engine noise?: {engine_noise}")
        summary.append(f"driving notes: {drive_notes}")

        # 4. damage/missing parts notes
        damage_block(prefix="s4_acc", step_label="4.", summary=summary)

        # Is vehicle as described?
        vehicle_described = st.radio(
            "Is vehicle as described? Yes/No",
            ["Yes", "No"],
            key="s4_acc_vehicle_described"
        )
        summary.append(f"Is vehicle as described?: {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get address for pickup")
            st.markdown("Get Pics of ID front and back")
            st.markdown("Get Pics of proof of ownership")
            st.markdown("Change status, (if DV Offer send straight to offer accepted)")
            summary.append("Next steps: Get address for pickup; Get Pics of ID front and back; "
                           "Get Pics of proof of ownership; Change status (if DV Offer send straight to offer accepted)")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            did_offer_change = st.radio(
                "Did offer change? Yes/No",
                ["Yes", "No"],
                key="s4_acc_offer_change"
            )
            summary.append(f"Did offer change?: {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get address for pickup")
                st.markdown("Get Pics of ID front and back")
                st.markdown("Get Pics of proof of ownership")
                st.markdown("Change status, (if DV Offer send straight to offer accepted)")
                summary.append("Next steps: Get address for pickup; Get Pics of ID front and back; "
                               "Get Pics of proof of ownership; Change status (if DV Offer send straight to offer accepted)")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario: Running And Driving | under $700 | Without Title")
        summary.append("customer accepts offer?: No")

        st.markdown("customer accepts offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. title/mileage notes
        st.markdown("1. title/mileage notes: I see there is no title, may I ask what happened with it?")
        st.markdown("I see there is no title, may I ask what happened with it?")
        summary.append("Customer statement: I see there is no title, may I ask what happened with it?")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s4_rej_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s4_rej_liens")
        v3 = yes_no_radio("Is it possible to get the title? Yes/no", key="s4_rej_possible_title")
        po = proof_of_ownership_radio("s4_rej", summary)
        v4 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s4_rej_miles")
        notes = st.text_area("title/mileage notes", key="s4_rej_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Is it possible to get the title?: {v3}")
        summary.append(f"Just to confirm the car has xxx miles?: {v4}")
        summary.append(f"title/mileage notes: {notes}")

        # 2. driving notes
        st.markdown("2. driving notes")
        drive_quality = st.radio("How does your car drive? Good/bad", ["Good", "Bad"], key="s4_rej_drive_quality")
        daily_use = yes_no_radio("Is it good for daily use? Yes/no", key="s4_rej_daily_use")
        move_5ft = yes_no_radio("Can it move forward and backward at least 5ft? yes/no", key="s4_rej_move_5ft")
        engine_noise = yes_no_radio("Does the car have any engine noise? Yes/no", key="s4_rej_engine_noise")
        drive_notes = st.text_area("driving notes", key="s4_rej_driving_notes")

        summary.append(f"How does your car drive?: {drive_quality}")
        summary.append(f"Is it good for daily use?: {daily_use}")
        summary.append(f"Can it move forward and backward at least 5ft?: {move_5ft}")
        summary.append(f"Does the car have any engine noise?: {engine_noise}")
        summary.append(f"driving notes: {drive_notes}")

        # 3. damage/missing parts notes
        damage_block(prefix="s4_rej", step_label="3.", summary=summary)

        # 4. pics & vin
        st.markdown("4. pics & vin")
        st.markdown(
            "What’s the easiest way for you to send: Pictures of your id front and back and proof of ownership?\n"
            "(see if customer will send it while on the phone)\n"
            "May I get the VIN to give you the most accurate offer)"
        )
        pics_vin = st.text_area("pics & vin", key="s4_rej_pics_vin")
        summary.append(f"pics & vin notes: {pics_vin}")
        summary.append("Action: Change Status. (if DV offer send straight to offer accepted)")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 5: No Run And Drive | Over $700 | With Title.
def render_scenario_5(customer_accepts: str):
    st.markdown("### Scenario 5: No Run And Drive | Over $700 | With Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario: No Run And Drive | Over $700 | With Title")
        summary.append("customer accepts offer?: Yes")

        st.markdown("customer accepts offer? Yes")
        st.markdown("1. sounds great! Let’s confirm some info and get you scheduled")

        # 2. title/mileage notes
        st.markdown("2. title/mileage notes")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s5_acc_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s5_acc_liens")
        v3 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s5_acc_miles")
        notes = st.text_area("title/mileage notes", key="s5_acc_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Just to confirm the car has xxx miles?: {v3}")
        summary.append(f"title/mileage notes: {notes}")

        # 3. driving notes
        st.markdown("3. driving notes")
        why_not = st.text_input("Do you know why it wont run?", key="s5_acc_why_not_run")
        run_with_jump_radio("s5_acc", summary)
        drive_notes = st.text_area("driving notes", key="s5_acc_driving_notes")

        summary.append(f"Do you know why it wont run?: {why_not}")
        summary.append(f"driving notes: {drive_notes}")

        # 4. damage/missing parts notes
        damage_block(prefix="s5_acc", step_label="4.", summary=summary)

        # Is vehicle as described?
        vehicle_described = st.radio(
            "Is vehicle as described? Yes/No",
            ["Yes", "No"],
            key="s5_acc_vehicle_described"
        )
        summary.append(f"Is vehicle as described?: {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get address for pickup")
            st.markdown("Get Pics of Title front & back")
            st.markdown("Get pics of the vehicle")
            summary.append("Next steps: Get address for pickup; Get Pics of Title front & back; Get pics of the vehicle")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            did_offer_change = st.radio(
                "Did offer change? Yes/No",
                ["Yes", "No"],
                key="s5_acc_offer_change"
            )
            summary.append(f"Did offer change?: {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get address for pickup")
                st.markdown("Get Pics of Title front & back")
                st.markdown("Get pics of the vehicle")
                summary.append("Next steps: Get address for pickup; Get Pics of Title front & back; Get pics of the vehicle")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario: No Run And Drive | Over $700 | With Title")
        summary.append("customer accepts offer?: No")

        st.markdown("customer accepts offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. title/mileage notes
        st.markdown("1. title/mileage notes")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s5_rej_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s5_rej_liens")
        v3 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s5_rej_miles")
        notes = st.text_area("title/mileage notes", key="s5_rej_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Just to confirm the car has xxx miles?: {v3}")
        summary.append(f"title/mileage notes: {notes}")

        # 2. driving notes
        st.markdown("2. driving notes")
        why_not = st.text_input("Do you know why it won’t run?", key="s5_rej_why_not_run")
        run_with_jump_radio("s5_rej", summary)
        drive_notes = st.text_area("driving notes", key="s5_rej_driving_notes")

        summary.append(f"Do you know why it won’t run?: {why_not}")
        summary.append(f"driving notes: {drive_notes}")

        # 3. damage/missing parts notes
        damage_block(prefix="s5_rej", step_label="3.", summary=summary)

        # 4. pics & vin
        st.markdown("4. pics & vin")
        st.markdown(
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle and VIN "
            "(See if customer will send it while on the phone.)"
        )
        pics_vin = st.text_area("pics & vin", key="s5_rej_pics_vin")
        summary.append(f"pics & vin notes: {pics_vin}")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 6: No Run And Drive | Over $700 | Without Title.
def render_scenario_6(customer_accepts: str):
    st.markdown("### Scenario 6: No Run And Drive | Over $700 | Without Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario: No Run And Drive | Over $700 | Without Title")
        summary.append("customer accepts offer?: Yes")

        st.markdown("customer accepts offer? Yes")
        st.markdown("1. sounds great! Let’s confirm some info and get you scheduled")

        # 2. title/mileage notes
        st.markdown("2. title/mileage notes: I see there is no title, may I ask what happened with it?")
        st.markdown("I see there is no title, may I ask what happened with it?")
        summary.append("Customer statement: I see there is no title, may I ask what happened with it?")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s6_acc_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s6_acc_liens")
        v3 = yes_no_radio("Is it possible to get the title? Yes/no", key="s6_acc_possible_title")
        po = proof_of_ownership_radio("s6_acc", summary)
        v4 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s6_acc_miles")
        notes = st.text_area("title/mileage notes", key="s6_acc_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Is it possible to get the title?: {v3}")
        summary.append(f"Just to confirm the car has xxx miles?: {v4}")
        summary.append(f"title/mileage notes: {notes}")

        # 3. driving notes
        st.markdown("3. driving notes")
        why_not = st.text_input("Do you know why it won’t start?", key="s6_acc_why_not_start")
        run_with_jump_radio("s6_acc", summary)
        drive_notes = st.text_area("driving notes", key="s6_acc_driving_notes")

        summary.append(f"Do you know why it won’t start?: {why_not}")
        summary.append(f"driving notes: {drive_notes}")

        # 4. damage/missing parts notes
        damage_block(prefix="s6_acc", step_label="4.", summary=summary)

        # Is vehicle as described?
        vehicle_described = st.radio(
            "Is vehicle as described? Yes/No",
            ["Yes", "No"],
            key="s6_acc_vehicle_described"
        )
        summary.append(f"Is vehicle as described?: {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get address for pickup")
            st.markdown("Get Pics of Title front & back")
            st.markdown("Get pics of the vehicle")
            summary.append("Next steps: Get address for pickup; Get Pics of Title front & back; Get pics of the vehicle")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            did_offer_change = st.radio(
                "Did offer change? Yes/No",
                ["Yes", "No"],
                key="s6_acc_offer_change"
            )
            summary.append(f"Did offer change?: {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get address for pickup")
                st.markdown("Get Pics of Title front & back")
                st.markdown("Get pics of the vehicle")
                summary.append("Next steps: Get address for pickup; Get Pics of Title front & back; Get pics of the vehicle")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario: No Run And Drive | Over $700 | Without Title")
        summary.append("customer accepts offer?: No")

        st.markdown("customer accepts offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. title/mileage notes
        st.markdown("1. title/mileage notes")
        st.markdown("I see there is no title, may I ask what happened with it?")
        summary.append("Customer statement: I see there is no title, may I ask what happened with it?")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s6_rej_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s6_rej_liens")
        v3 = yes_no_radio("Is it possible to get the title? Yes/no", key="s6_rej_possible_title")
        po = proof_of_ownership_radio("s6_rej", summary)
        v4 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s6_rej_miles")
        notes = st.text_area("title/mileage notes", key="s6_rej_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Is it possible to get the title?: {v3}")
        summary.append(f"Just to confirm the car has xxx miles?: {v4}")
        summary.append(f"title/mileage notes: {notes}")

        # 2. driving notes
        st.markdown("2. driving notes")
        why_not = st.text_input("Do you know why it won’t start?", key="s6_rej_why_not_start")
        run_with_jump_radio("s6_rej", summary)
        drive_notes = st.text_area("driving notes", key="s6_rej_driving_notes")

        summary.append(f"Do you know why it won’t start?: {why_not}")
        summary.append(f"driving notes: {drive_notes}")

        # 3. damage/missing parts notes
        damage_block(prefix="s6_rej", step_label="3.", summary=summary)

        # 4. pics & vin
        st.markdown("4. pics & vin")
        st.markdown(
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle and VIN "
            "(See if customer will send it while on the phone.)"
        )
        pics_vin = st.text_area("pics & vin", key="s6_rej_pics_vin")
        summary.append(f"pics & vin notes: {pics_vin}")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 7: No Run And Drive | Under $700 | With Title.
def render_scenario_7(customer_accepts: str):
    st.markdown("### Scenario 7: No Run And Drive | Under $700 | With Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario: No Run And Drive | Under $700 | With Title")
        summary.append("customer accepts offer?: Yes")

        st.markdown("customer accepts offer? Yes")
        st.markdown("1. sounds great! Let’s confirm some info and get you scheduled")

        # 2. title/mileage notes
        st.markdown("2. title/mileage notes")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s7_acc_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s7_acc_liens")
        v3 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s7_acc_miles")
        notes = st.text_area("title/mileage notes", key="s7_acc_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Just to confirm the car has xxx miles?: {v3}")
        summary.append(f"title/mileage notes: {notes}")

        # 3. driving notes
        st.markdown("3. driving notes")
        why_not = st.text_input("Do you know why it won’t run?", key="s7_acc_why_not_run")
        run_with_jump_radio("s7_acc", summary)
        drive_notes = st.text_area("driving notes", key="s7_acc_driving_notes")

        summary.append(f"Do you know why it won’t run?: {why_not}")
        summary.append(f"driving notes: {drive_notes}")

        # 4. damage/missing parts notes
        damage_block(prefix="s7_acc", step_label="4.", summary=summary)

        # Is vehicle as described?
        vehicle_described = st.radio(
            "Is vehicle as described? Yes/No",
            ["Yes", "No"],
            key="s7_acc_vehicle_described"
        )
        summary.append(f"Is vehicle as described?: {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get address for pickup")
            st.markdown("Get Pics of ID front & back")
            st.markdown("Get pics of proof of ownership")
            st.markdown("Change status (if DV offer send straight to offer accepted)")
            summary.append("Next steps: Get address for pickup; Get Pics of ID front & back; "
                           "Get pics of proof of ownership; Change status (if DV offer send straight to offer accepted)")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            did_offer_change = st.radio(
                "Did offer change? Yes/No",
                ["Yes", "No"],
                key="s7_acc_offer_change"
            )
            summary.append(f"Did offer change?: {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get address for pickup")
                st.markdown("Get Pics of ID front & back")
                st.markdown("Get pics of proof of ownership")
                summary.append("Next steps: Get address for pickup; Get Pics of ID front & back; Get pics of proof of ownership")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario: No Run And Drive | Under $700 | With Title")
        summary.append("customer accepts offer?: No")

        st.markdown("customer accepts offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. title/mileage notes
        st.markdown("1. title/mileage notes")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s7_rej_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s7_rej_liens")
        v3 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s7_rej_miles")
        notes = st.text_area("title/mileage notes", key="s7_rej_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Just to confirm the car has xxx miles?: {v3}")
        summary.append(f"title/mileage notes: {notes}")

        # 2. driving notes
        st.markdown("2. driving notes")
        why_not = st.text_input("Do you know why it won’t run?", key="s7_rej_why_not_run")
        run_with_jump_radio("s7_rej", summary)
        drive_notes = st.text_area("driving notes", key="s7_rej_driving_notes")

        summary.append(f"Do you know why it won’t run?: {why_not}")
        summary.append(f"driving notes: {drive_notes}")

        # 3. damage/missing parts notes
        damage_block(prefix="s7_rej", step_label="3.", summary=summary)

        # 4. pics & vin
        st.markdown("4. pics & vin")
        st.markdown(
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle and VIN? "
            "(See if customer will send it while on the phone.)"
        )
        pics_vin = st.text_area("pics & vin", key="s7_rej_pics_vin")
        summary.append(f"pics & vin notes: {pics_vin}")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 8: No Run And Drive | Under $700 | Without Title.
def render_scenario_8(customer_accepts: str):
    st.markdown("### Scenario 8: No Run And Drive | Under $700 | Without Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario: No Run And Drive | Under $700 | Without Title")
        summary.append("customer accepts offer?: Yes")

        st.markdown("customer accepts offer? Yes")
        st.markdown("1. sounds great! Let’s confirm some info and get you scheduled")

        # 2. title/mileage notes
        st.markdown("2. title/mileage notes: I see there is not title, may I ask what happened with it?")
        st.markdown("I see there is not title, may I ask what happened with it?")
        summary.append("Customer statement: I see there is not title, may I ask what happened with it?")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s8_acc_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s8_acc_liens")
        po = proof_of_ownership_radio("s8_acc", summary)
        v3 = yes_no_radio("Is it possible to get the title? Yes/no", key="s8_acc_possible_title")
        v4 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s8_acc_miles")
        notes = st.text_area("title/mileage notes", key="s8_acc_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Is it possible to get the title?: {v3}")
        summary.append(f"Just to confirm the car has xxx miles?: {v4}")
        summary.append(f"title/mileage notes: {notes}")

        # 3. driving notes
        st.markdown("3. driving notes")
        why_not = st.text_input("Do you know why it won’t run?", key="s8_acc_why_not_run")
        run_with_jump_radio("s8_acc", summary)
        drive_notes = st.text_area("driving notes", key="s8_acc_driving_notes")

        summary.append(f"Do you know why it won’t run?: {why_not}")
        summary.append(f"driving notes: {drive_notes}")

        # 4. damage/missing parts notes
        damage_block(prefix="s8_acc", step_label="4.", summary=summary)

        # Is vehicle as described?
        vehicle_described = st.radio(
            "Is vehicle as described? Yes/No",
            ["Yes", "No"],
            key="s8_acc_vehicle_described"
        )
        summary.append(f"Is vehicle as described?: {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get address for pickup")
            st.markdown("Get Pics of ID front & back")
            st.markdown("Get pics of proof of ownership")
            st.markdown("Change status. (if DV offer send straight to offer accepted)")
            summary.append("Next steps: Get address for pickup; Get Pics of ID front & back; "
                           "Get pics of proof of ownership; Change status (if DV offer send straight to offer accepted)")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            did_offer_change = st.radio(
                "Did offer change? Yes/No",
                ["Yes", "No"],
                key="s8_acc_offer_change"
            )
            summary.append(f"Did offer change?: {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get address for pickup")
                st.markdown("Get Pics of ID front & back")
                st.markdown("Get pics of proof of ownership")
                st.markdown("Change status. (if DV offer send straight to offer accepted)")
                summary.append("Next steps: Get address for pickup; Get Pics of ID front & back; "
                               "Get pics of proof of ownership; Change status (if DV offer send straight to offer accepted)")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario: No Run And Drive | Under $700 | Without Title")
        summary.append("customer accepts offer?: No")

        st.markdown("customer accepts offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. title/mileage notes
        st.markdown("1. title/mileage notes: I see there is not title, may I ask what happened with it?")
        st.markdown("I see there is not title, may I ask what happened with it?")
        summary.append("Customer statement: I see there is not title, may I ask what happened with it?")
        v1 = yes_no_radio("Is title in your name? yes/no", key="s8_rej_title_in_name")
        v2 = yes_no_radio("Are there any liens on the title? Yes/no", key="s8_rej_liens")
        po = proof_of_ownership_radio("s8_rej", summary)
        v3 = yes_no_radio("Is it possible to get the title? Yes/no", key="s8_rej_possible_title")
        v4 = yes_no_radio("Just to confirm the car has xxx miles? Yes/no", key="s8_rej_miles")
        notes = st.text_area("title/mileage notes", key="s8_rej_title_mileage_notes")

        summary.append(f"Is title in your name?: {v1}")
        summary.append(f"Are there any liens on the title?: {v2}")
        summary.append(f"Is it possible to get the title?: {v3}")
        summary.append(f"Just to confirm the car has xxx miles?: {v4}")
        summary.append(f"title/mileage notes: {notes}")

        # 2. driving notes
        st.markdown("2. driving notes")
        why_not = st.text_input("Do you know why it won’t run?", key="s8_rej_why_not_run")
        run_with_jump_radio("s8_rej", summary)
        drive_notes = st.text_area("driving notes", key="s8_rej_driving_notes")

        summary.append(f"Do you know why it won’t run?: {why_not}")
        summary.append(f"driving notes: {drive_notes}")

        # 3. damage/missing parts notes
        damage_block(prefix="s8_rej", step_label="3.", summary=summary)

        # 4. pics & vin
        st.markdown("4. pics & vin")
        st.markdown(
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle and VIN? "
            "(See if customer will send it while on the phone.)"
        )
        pics_vin = st.text_area("pics & vin", key="s8_rej_pics_vin")
        summary.append(f"pics & vin notes: {pics_vin}")
        summary.append("Action: Change status. (if DV offer send straight to offer accepted)")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# ---------- ROUTER ----------

if scenario_option == "run and drives/ over 700/ with title":
    render_scenario_1(customer_accepts)
elif scenario_option == "runs and drives/ over 700/ without title":
    render_scenario_2(customer_accepts)
elif scenario_option == "runs and drives/ under 700/ with title":
    render_scenario_3(customer_accepts)
elif scenario_option == "runs and drives/ under 700/ without title":
    render_scenario_4(customer_accepts)
elif scenario_option == "No run and drive/ over 700/ with title":
    render_scenario_5(customer_accepts)
elif scenario_option == "no run and drive/ over 700/ without title":
    render_scenario_6(customer_accepts)
elif scenario_option == "no run and drive/ under 700/ with title":
    render_scenario_7(customer_accepts)
elif scenario_option == "no run and drive/ under 700/ without title":
    render_scenario_8(customer_accepts)
