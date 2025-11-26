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
        "no run and drive/ over 700/ with title",
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
    st.markdown(f"{step_label} Damage/missing parts notes")
    prompt_damage = "Is there any major damage or missing parts inside or outside the vehicle? Yes/No"
    val = yes_no_radio(
        prompt_damage,
        key=f"{prefix}_damage_missing",
    )
    summary.append(f"{prompt_damage} {val}")
    notes = st.text_area("Damage/missing parts notes", key=f"{prefix}_damage_missing_notes")
    summary.append(f"Damage/missing parts notes: {notes}")


def proof_of_ownership_radio(prefix: str, summary, prompt_suffix="What proof of ownership do you have (bill of sale, insurance, registration)?"):
    val = st.radio(
        prompt_suffix,
        ["bill of sale", "insurance", "registration"],
        key=f"{prefix}_proof_ownership",
    )
    summary.append(f"{prompt_suffix} {val}")
    return val


def run_with_jump_radio(prefix: str, summary):
    prompt = "Can it run with a jump?"
    val = yes_no_radio(prompt, key=f"{prefix}_run_with_jump")
    summary.append(f"{prompt} {val}")
    return val


# ---------- SCENARIO RENDER FUNCTIONS ----------

# Scenario 1: Running And Driving | Over $700 | With Title.
def render_scenario_1(customer_accepts: str):
    st.markdown("### Scenario 1: Running And Driving | Over $700 | With Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give the offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario 1: Running And Driving | Over $700 | With Title")
        summary.append("Did the customer accept the offer?: Yes")

        st.markdown("Did the Customer accept the offer? Yes")
        st.markdown("1. Sounds great! Let’s confirm some information and get you scheduled for pickup and payment.")

        # 2. title/mileage notes
        st.markdown("2. Title/mileage notes")
        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s1_acc_title_in_name")
        v2 = yes_no_radio(p2, key="s1_acc_liens")
        v3 = yes_no_radio(p3, key="s1_acc_miles")
        notes = st.text_area("Title/mileage notes", key="s1_acc_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"Title/mileage notes: {notes}")

        # 3. Driving notes
        st.markdown("3. Driving notes")
        p_drive_quality = "How does your car drive? Good/Bad"
        drive_quality = st.radio(p_drive_quality, ["Good", "Bad"], key="s1_acc_drive_quality")
        p_daily = "Is it good for daily use? Yes/No"
        p_move = "Can it move forward and backward at least 5ft? Yes/No"
        p_noise = "Does the car have any engine noise? Yes/No"

        daily_use = yes_no_radio(p_daily, key="s1_acc_daily_use")
        move_5ft = yes_no_radio(p_move, key="s1_acc_move_5ft")
        engine_noise = yes_no_radio(p_noise, key="s1_acc_engine_noise")
        drive_notes = st.text_area("Driving notes", key="s1_acc_driving_notes")

        summary.append(f"{p_drive_quality} {drive_quality}")
        summary.append(f"{p_daily} {daily_use}")
        summary.append(f"{p_move} {move_5ft}")
        summary.append(f"{p_noise} {engine_noise}")
        summary.append(f"Driving notes: {drive_notes}")

        # 4. Damage/missing parts notes
        damage_block(prefix="s1_acc", step_label="4.", summary=summary)

        # Is the vehicle as described?
        p_described = "Is the vehicle as described? Yes/No"
        vehicle_described = st.radio(
            p_described,
            ["Yes", "No"],
            key="s1_acc_vehicle_described"
        )
        summary.append(f"{p_described} {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get the pickup address")
            st.markdown("Get pictures of the title front & back")
            st.markdown("Get pics of the dash with the engine running")
            st.markdown("Ask for a video of the engine running (Not required if not BB offer)")
            summary.append("Next steps: Get the pickup address; Get pictures of the title front & back; "
                           "Get pics of the dash with the engine running; Ask for a video of the engine running (Not required if not BB offer)")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            p_change = "Did the offer change? Yes/No"
            did_offer_change = st.radio(
                p_change,
                ["Yes", "No"],
                key="s1_acc_offer_change"
            )
            summary.append(f"{p_change} {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if the offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if the offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get the address for pickup")
                st.markdown("Get pictures of the title front & back")
                st.markdown("Get pics of the dash with the engine running")
                st.markdown("Ask for a video of the engine running (Not required if not BB offer)")
                summary.append("Next steps: Get the address for pickup; Get pictures of the title front & back; "
                               "Get pics of the dash with the engine running; Ask for a video of the engine running (Not required if not BB offer)")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario 1: Running And Driving | Over $700 | With Title")
        summary.append("Customer accepts the offer?: No")

        st.markdown("Customer accepts the offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. Title/mileage notes
        st.markdown("1. Title/mileage notes")
        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s1_rej_title_in_name")
        v2 = yes_no_radio(p2, key="s1_rej_liens")
        v3 = yes_no_radio(p3, key="s1_rej_miles")
        notes = st.text_area("Title/mileage notes", key="s1_rej_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"Title/mileage notes: {notes}")

        # 2. Driving notes
        st.markdown("2. Driving notes")
        p_drive_quality = "How does your car drive? Good/Bad"
        drive_quality = st.radio(p_drive_quality, ["Good", "Bad"], key="s1_rej_drive_quality")
        p_daily = "Is it good for daily use? Yes/No"
        p_move = "Can it move forward and backward at least 5ft? Yes/No"
        p_noise = "Does the car have any engine noise? Yes/No"

        daily_use = yes_no_radio(p_daily, key="s1_rej_daily_use")
        move_5ft = yes_no_radio(p_move, key="s1_rej_move_5ft")
        engine_noise = yes_no_radio(p_noise, key="s1_rej_engine_noise")
        drive_notes = st.text_area("Driving notes", key="s1_rej_driving_notes")

        summary.append(f"{p_drive_quality} {drive_quality}")
        summary.append(f"{p_daily} {daily_use}")
        summary.append(f"{p_move} {move_5ft}")
        summary.append(f"{p_noise} {engine_noise}")
        summary.append(f"Driving notes: {drive_notes}")

        # 3. Damage/missing parts notes
        damage_block(prefix="s1_rej", step_label="3.", summary=summary)

        # 4. Pictures & vin
        st.markdown("4. Pictures & vin")
        pics_prompt = (
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle, "
            "dash pictures with the engine turned on. VIN and a 10-second video of the engine running? "
            "(See if the customer will send it while on the phone.)"
        )
        st.markdown(pics_prompt)
        pics_vin = st.text_area("Pictures & vin notes", key="s1_rej_pics_vin")
        summary.append(f"Pictures & vin notes: {pics_vin}")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 2: Running And Driving | Over $700 | Without Title.
def render_scenario_2(customer_accepts: str):
    st.markdown("### Scenario 2: Running And Driving | Over $700 | Without Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give the offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario 2: Running And Driving | Over $700 | Without Title")
        summary.append("Did the customer accept the offer?: Yes")

        st.markdown("Did the customer accept the offer? Yes")
        st.markdown("1. Sounds great! Let’s confirm some information and get you scheduled for pickup and payment")

        # 2. Title/mileage notes
        st.markdown("2. Title/mileage notes")
        st.markdown("I see there is no title. May I ask what happened with it?")
        summary.append("Statement: I see there is no title. May I ask what happened with it?")

        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Is it possible to get the title? Yes/No"
        p4 = "What proof of ownership do you have (bill of sale, insurance, registration)?"
        p5 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s2_acc_title_in_name")
        v2 = yes_no_radio(p2, key="s2_acc_liens")
        v3 = yes_no_radio(p3, key="s2_acc_possible_title")
        po = proof_of_ownership_radio("s2_acc", summary, prompt_suffix=p4)
        v5 = yes_no_radio(p5, key="s2_acc_miles")
        notes = st.text_area("Title/mileage notes", key="s2_acc_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"{p5} {v5}")
        summary.append(f"Title/mileage notes: {notes}")

        # 3. Driving notes
        st.markdown("3. Driving notes")
        p_drive_quality = "How does your car drive? Good/Bad"
        drive_quality = st.radio(p_drive_quality, ["Good", "Bad"], key="s2_acc_drive_quality")
        p_daily = "Is it good for daily use? Yes/No"
        p_move = "Can it move forward and backward at least 5ft? Yes/No"
        p_noise = "Does the car have any engine noise? Yes/No"

        daily_use = yes_no_radio(p_daily, key="s2_acc_daily_use")
        move_5ft = yes_no_radio(p_move, key="s2_acc_move_5ft")
        engine_noise = yes_no_radio(p_noise, key="s2_acc_engine_noise")
        drive_notes = st.text_area("Driving notes", key="s2_acc_driving_notes")

        summary.append(f"{p_drive_quality} {drive_quality}")
        summary.append(f"{p_daily} {daily_use}")
        summary.append(f"{p_move} {move_5ft}")
        summary.append(f"{p_noise} {engine_noise}")
        summary.append(f"Driving notes: {drive_notes}")

        # 4. Damage/missing parts notes
        damage_block(prefix="s2_acc", step_label="4.", summary=summary)

        # Is the vehicle as described?
        p_described = "Is the vehicle as described? Yes/No"
        vehicle_described = st.radio(
            p_described,
            ["Yes", "No"],
            key="s2_acc_vehicle_described"
        )
        summary.append(f"{p_described} {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get the address for pickup")
            st.markdown("Get pictures of ID front & back")
            st.markdown("Get pictures of proof of ownership")
            st.markdown("Get pictures of the dash with the engine running")
            st.markdown("Ask for a video of the engine running (Not required if not BB offer)")
            st.markdown("Send to manager for review")
            summary.append("Next steps: Get the address for pickup; Get pictures of ID front & back; "
                           "Get pictures of proof of ownership; Get pictures of the dash with the engine running; "
                           "Ask for a video of the engine running (Not required if not BB offer); Send to manager for review")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            p_change = "Did the offer change? Yes/No"
            did_offer_change = st.radio(
                p_change,
                ["Yes", "No"],
                key="s2_acc_offer_change"
            )
            summary.append(f"{p_change} {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if the offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if the offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get the address for pickup")
                st.markdown("Get pictures of ID front & back")
                st.markdown("Get pictures of proof of ownership")
                st.markdown("Get pictures of the dash with the engine running")
                st.markdown("Ask for a video of the engine running (Not required if not BB offer)")
                st.markdown("Send to the manager for review")
                summary.append("Next steps: Get the address for pickup; Get pictures of ID front & back; "
                               "Get pictures of proof of ownership; Get pictures of the dash with the engine running; "
                               "Ask for a video of the engine running (Not required if not BB offer); Send to the manager for review")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario 2: Running And Driving | Over $700 | Without Title")
        summary.append("Customer accepts the offer?: No")

        st.markdown("Customer accepts the offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. Title/mileage notes
        st.markdown("1. Title/mileage notes: I see there is no title. May I ask what happened with it?")
        st.markdown("I see there is no title. May I ask what happened with it?")
        summary.append("Statement: I see there is no title. May I ask what happened with it?")

        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p4 = "What proof of ownership do you have? (bill of sale, registration, insurance)?"
        p3 = "Is it possible to get the title? Yes/No"
        p5 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s2_rej_title_in_name")
        v2 = yes_no_radio(p2, key="s2_rej_liens")
        po = proof_of_ownership_radio("s2_rej", summary, prompt_suffix=p4)
        v3 = yes_no_radio(p3, key="s2_rej_possible_title")
        v5 = yes_no_radio(p5, key="s2_rej_miles")
        notes = st.text_area("Title/mileage notes", key="s2_rej_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"{p5} {v5}")
        summary.append(f"Title/mileage notes: {notes}")

        # 2. Driving notes
        st.markdown("2. Driving notes")
        p_drive_quality = "How does your car drive? Good/Bad"
        drive_quality = st.radio(p_drive_quality, ["Good", "Bad"], key="s2_rej_drive_quality")
        p_daily = "Is it good for daily use? Yes/No"
        p_move = "Can it move forward and backward at least 5ft? Yes/No"
        p_noise = "Does the car have any engine noise? Yes/No"

        daily_use = yes_no_radio(p_daily, key="s2_rej_daily_use")
        move_5ft = yes_no_radio(p_move, key="s2_rej_move_5ft")
        engine_noise = yes_no_radio(p_noise, key="s2_rej_engine_noise")
        drive_notes = st.text_area("Driving notes", key="s2_rej_driving_notes")

        summary.append(f"{p_drive_quality} {drive_quality}")
        summary.append(f"{p_daily} {daily_use}")
        summary.append(f"{p_move} {move_5ft}")
        summary.append(f"{p_noise} {engine_noise}")
        summary.append(f"Driving notes: {drive_notes}")

        # 3. Damage/missing parts notes
        damage_block(prefix="s2_rej", step_label="3.", summary=summary)

        # 4. Pics & vin
        st.markdown("4. Pics & vin")
        pics_prompt = (
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle, "
            "pictures of the dash with the engine turned on. VIN and a 10-second video of the engine running? "
            "(See if the customer will send it while on the phone.)"
        )
        st.markdown(pics_prompt)
        pics_vin = st.text_area("Pics & vin notes", key="s2_rej_pics_vin")
        summary.append(f"Pics & vin notes: {pics_vin}")
        summary.append("Action: Send to the manager for review.")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 3: Running And Driving | under $700 | With Title.
def render_scenario_3(customer_accepts: str):
    st.markdown("### Scenario 3: Running And Driving | under $700 | With Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give the offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario 3: Running And Driving | under $700 | With Title")
        summary.append("Customer accepts offer?: Yes")

        st.markdown("customer accepts offer? Yes")
        st.markdown("1. Sounds great! Let’s confirm some info and get you scheduled")

        # 2. Title/mileage notes
        st.markdown("2. Title/mileage notes")
        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s3_acc_title_in_name")
        v2 = yes_no_radio(p2, key="s3_acc_liens")
        v3 = yes_no_radio(p3, key="s3_acc_miles")
        notes = st.text_area("Title/mileage notes", key="s3_acc_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"Title/mileage notes: {notes}")

        # 3. Driving notes
        st.markdown("3. Driving notes")
        p_drive_quality = "How does your car drive? Good/Bad"
        drive_quality = st.radio(p_drive_quality, ["Good", "Bad"], key="s3_acc_drive_quality")
        p_daily = "Is it good for daily use? Yes/No"
        p_move = "Can it move forward and backward at least 5ft? Yes/No"
        p_noise = "Does the car have any engine noise? Yes/No"

        daily_use = yes_no_radio(p_daily, key="s3_acc_daily_use")
        move_5ft = yes_no_radio(p_move, key="s3_acc_move_5ft")
        engine_noise = yes_no_radio(p_noise, key="s3_acc_engine_noise")
        drive_notes = st.text_area("Driving notes", key="s3_acc_driving_notes")

        summary.append(f"{p_drive_quality} {drive_quality}")
        summary.append(f"{p_daily} {daily_use}")
        summary.append(f"{p_move} {move_5ft}")
        summary.append(f"{p_noise} {engine_noise}")
        summary.append(f"Driving notes: {drive_notes}")

        # 4. Damage/missing parts notes
        damage_block(prefix="s3_acc", step_label="4.", summary=summary)

        # Is the vehicle as described?
        p_described = "Is the vehicle as described? Yes/No"
        vehicle_described = st.radio(
            p_described,
            ["Yes", "No"],
            key="s3_acc_vehicle_described"
        )
        summary.append(f"{p_described} {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get the address for pickup")
            st.markdown("Get Pics of the title front & back")
            st.markdown("Get pics of the dash with the engine running")
            st.markdown("Ask for a video of the engine running (Not required if not BB offer)")
            summary.append("Next steps: Get the address for pickup; Get Pics of the title front & back; "
                           "Get pics of the dash with the engine running; Ask for a video of the engine running (Not required if not BB offer)")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            p_change = "Did the offer change? Yes/No"
            did_offer_change = st.radio(
                p_change,
                ["Yes", "No"],
                key="s3_acc_offer_change"
            )
            summary.append(f"{p_change} {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if the offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if the offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get the address for pickup")
                st.markdown("Get Pics of the Title front & back")
                st.markdown("Get pics of the dash with the engine running")
                st.markdown("Ask for a video of the engine running (Not required if not BB offer)")
                summary.append("Next steps: Get the address for pickup; Get Pics of the Title front & back; "
                               "Get pics of the dash with the engine running; Ask for a video of the engine running (Not required if not BB offer)")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario 3: Running And Driving | under $700 | With Title")
        summary.append("customer accepts offer?: No")

        st.markdown("customer accepts offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. Title/mileage notes
        st.markdown("1. Title/mileage notes")
        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s3_rej_title_in_name")
        v2 = yes_no_radio(p2, key="s3_rej_liens")
        v3 = yes_no_radio(p3, key="s3_rej_miles")
        notes = st.text_area("Title/mileage notes", key="s3_rej_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"Title/mileage notes: {notes}")

        # 2. Driving notes
        st.markdown("2. Driving notes")
        p_drive_quality = "How does your car drive? Good/Bad"
        drive_quality = st.radio(p_drive_quality, ["Good", "Bad"], key="s3_rej_drive_quality")
        p_daily = "Is it good for daily use? Yes/No"
        p_move = "Can it move forward and backward at least 5ft? Yes/No"
        p_noise = "Does the car have any engine noise? Yes/No"

        daily_use = yes_no_radio(p_daily, key="s3_rej_daily_use")
        move_5ft = yes_no_radio(p_move, key="s3_rej_move_5ft")
        engine_noise = yes_no_radio(p_noise, key="s3_rej_engine_noise")
        drive_notes = st.text_area("Driving notes", key="s3_rej_driving_notes")

        summary.append(f"{p_drive_quality} {drive_quality}")
        summary.append(f"{p_daily} {daily_use}")
        summary.append(f"{p_move} {move_5ft}")
        summary.append(f"{p_noise} {engine_noise}")
        summary.append(f"Driving notes: {drive_notes}")

        # 3. Damage/missing parts notes
        damage_block(prefix="s3_rej", step_label="3.", summary=summary)

        # 4. Pics & vin
        st.markdown("4. Pics & vin")
        pics_prompt = (
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle, "
            "dash pictures with the engine turned on. VIN and a 10-second video of the engine running? "
            "(See if customer will send it while on the phone.)"
        )
        st.markdown(pics_prompt)
        pics_vin = st.text_area("Pics & vin notes", key="s3_rej_pics_vin")
        summary.append(f"Pics & vin notes: {pics_vin}")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 4: Running And Driving | under $700 | Without Title.
def render_scenario_4(customer_accepts: str):
    st.markdown("### Scenario 4: Running And Driving | under $700 | Without Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give an offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario 4: Running And Driving | under $700 | Without Title")
        summary.append("customer accepts offer?: Yes")

        st.markdown("customer accepts offer? Yes")
        st.markdown("1. sounds great! Let’s confirm some info and get you scheduled")

        # 2. Title/mileage notes
        st.markdown("2. Title/mileage notes: I see there is no title. May I ask what happened with it?")
        st.markdown("I see there is no title. May I ask what happened with it?")
        summary.append("Statement: I see there is no title. May I ask what happened with it?")

        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Is it possible to get the title? Yes/No"
        p4 = "What proof of ownership do you have (bill of sale, insurance, registration)?"
        p5 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s4_acc_title_in_name")
        v2 = yes_no_radio(p2, key="s4_acc_liens")
        v3 = yes_no_radio(p3, key="s4_acc_possible_title")
        po = proof_of_ownership_radio("s4_acc", summary, prompt_suffix=p4)
        v5 = yes_no_radio(p5, key="s4_acc_miles")
        notes = st.text_area("Title/mileage notes", key="s4_acc_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"{p5} {v5}")
        summary.append(f"Title/mileage notes: {notes}")

        # 3. Driving notes
        st.markdown("3. Driving notes")
        p_drive_quality = "How does your car drive? Good/Bad"
        drive_quality = st.radio(p_drive_quality, ["Good", "Bad"], key="s4_acc_drive_quality")
        p_daily = "Is it good for daily use? Yes/No"
        p_move = "Can it move forward and backward at least 5ft? Yes/No"
        p_noise = "Does the car have any engine noise? Yes/No"

        daily_use = yes_no_radio(p_daily, key="s4_acc_daily_use")
        move_5ft = yes_no_radio(p_move, key="s4_acc_move_5ft")
        engine_noise = yes_no_radio(p_noise, key="s4_acc_engine_noise")
        drive_notes = st.text_area("Driving notes", key="s4_acc_driving_notes")

        summary.append(f"{p_drive_quality} {drive_quality}")
        summary.append(f"{p_daily} {daily_use}")
        summary.append(f"{p_move} {move_5ft}")
        summary.append(f"{p_noise} {engine_noise}")
        summary.append(f"Driving notes: {drive_notes}")

        # 4. Damage/missing parts notes
        damage_block(prefix="s4_acc", step_label="4.", summary=summary)

        # Is the car/vehicle as described?
        p_described = "Is the car as described? Yes/No"
        vehicle_described = st.radio(
            p_described,
            ["Yes", "No"],
            key="s4_acc_vehicle_described"
        )
        summary.append(f"{p_described} {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get the address for pickup")
            st.markdown("Get Pics of ID front and back")
            st.markdown("Get Pics of proof of ownership")
            st.markdown("Change status (if DV Offer send straight to offer accepted)")
            summary.append("Next steps: Get the address for pickup; Get Pics of ID front and back; "
                           "Get Pics of proof of ownership; Change status (if DV Offer send straight to offer accepted)")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            p_change = "Did the offer change? Yes/No"
            did_offer_change = st.radio(
                p_change,
                ["Yes", "No"],
                key="s4_acc_offer_change"
            )
            summary.append(f"{p_change} {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if the offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if the offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get the address for pickup")
                st.markdown("Get pictures of the ID front and back")
                st.markdown("Get pictures of proof of ownership")
                st.markdown("Change status, (if DV Offer send straight to offer accepted)")
                summary.append("Next steps: Get the address for pickup; Get pictures of the ID front and back; "
                               "Get pictures of proof of ownership; Change status, (if DV Offer send straight to offer accepted)")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario 4: Running And Driving | under $700 | Without Title")
        summary.append("customer accepts offer?: No")

        st.markdown("customer accepts offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. Title/mileage notes
        st.markdown("1. Title/mileage notes: I see there is no title. May I ask what happened with it?")
        st.markdown("I see there is no title. May I ask what happened with it?")
        summary.append("Statement: I see there is no title. May I ask what happened with it?")

        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Is it possible to get the title? Yes/No"
        p4 = "What proof of ownership do you have (bill of sale, insurance, registration)?"
        p5 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s4_rej_title_in_name")
        v2 = yes_no_radio(p2, key="s4_rej_liens")
        v3 = yes_no_radio(p3, key="s4_rej_possible_title")
        po = proof_of_ownership_radio("s4_rej", summary, prompt_suffix=p4)
        v5 = yes_no_radio(p5, key="s4_rej_miles")
        notes = st.text_area("Title/mileage notes", key="s4_rej_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"{p5} {v5}")
        summary.append(f"Title/mileage notes: {notes}")

        # 2. Driving notes
        st.markdown("2. Driving notes")
        p_drive_quality = "How does your car drive? Good/Bad"
        drive_quality = st.radio(p_drive_quality, ["Good", "Bad"], key="s4_rej_drive_quality")
        p_daily = "Is it good for daily use? Yes/No"
        p_move = "Can it move forward and backward at least 5ft? Yes/No"
        p_noise = "Does the car have any engine noise? Yes/No"

        daily_use = yes_no_radio(p_daily, key="s4_rej_daily_use")
        move_5ft = yes_no_radio(p_move, key="s4_rej_move_5ft")
        engine_noise = yes_no_radio(p_noise, key="s4_rej_engine_noise")
        drive_notes = st.text_area("Driving notes", key="s4_rej_driving_notes")

        summary.append(f"{p_drive_quality} {drive_quality}")
        summary.append(f"{p_daily} {daily_use}")
        summary.append(f"{p_move} {move_5ft}")
        summary.append(f"{p_noise} {engine_noise}")
        summary.append(f"Driving notes: {drive_notes}")

        # 3. Damage/missing parts notes
        damage_block(prefix="s4_rej", step_label="3.", summary=summary)

        # 4. Pics & vin
        st.markdown("4. Pics & vin")
        pics_prompt = (
            "What’s the easiest way for you to send: Pictures of your ID front and back, and proof of ownership?\n"
            "(See if the customer will send it while on the phone)\n"
            "May I get the VIN to give you the most accurate offer?"
        )
        st.markdown(pics_prompt)
        pics_vin = st.text_area("Pics & vin notes", key="s4_rej_pics_vin")
        summary.append(f"Pics & vin notes: {pics_vin}")
        summary.append("Action: Change Status. (if DV offer send straight to offer accepted)")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 5: No Run And Drive | Over $700 | With Title.
def render_scenario_5(customer_accepts: str):
    st.markdown("### Scenario 5: No Run And Drive | Over $700 | With Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give an offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario 5: No Run And Drive | Over $700 | With Title")
        summary.append("Customer accepts the offer?: Yes")

        st.markdown("Customer accepts the offer? Yes")
        st.markdown("1. Sounds great! Let’s confirm some info and get you scheduled")

        # 2. Title/mileage notes
        st.markdown("2. Title/mileage notes")
        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s5_acc_title_in_name")
        v2 = yes_no_radio(p2, key="s5_acc_liens")
        v3 = yes_no_radio(p3, key="s5_acc_miles")
        notes = st.text_area("Title/mileage notes", key="s5_acc_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"Title/mileage notes: {notes}")

        # 3. Driving notes
        st.markdown("3. Driving notes")
        why_not = st.text_input("Do you know why it won't run? text", key="s5_acc_why_not_run")
        run_with_jump_radio("s5_acc", summary)
        drive_notes = st.text_area("Driving notes", key="s5_acc_driving_notes")

        summary.append(f"Do you know why it won't run?: {why_not}")
        summary.append(f"Driving notes: {drive_notes}")

        # 4. Damage/missing parts notes
        damage_block(prefix="s5_acc", step_label="4.", summary=summary)

        # Is the vehicle as described?
        p_described = "Is the vehicle as described? Yes/No"
        vehicle_described = st.radio(
            p_described,
            ["Yes", "No"],
            key="s5_acc_vehicle_described"
        )
        summary.append(f"{p_described} {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get the address for pickup")
            st.markdown("Get pictures of the title front & back")
            st.markdown("Get pictures of the vehicle")
            summary.append("Next steps: Get the address for pickup; Get pictures of the title front & back; Get pictures of the vehicle")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            p_change = "Did the offer change? Yes/No"
            did_offer_change = st.radio(
                p_change,
                ["Yes", "No"],
                key="s5_acc_offer_change"
            )
            summary.append(f"{p_change} {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if the offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if the offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get the address for pickup")
                st.markdown("Get Pics of the title front & back")
                st.markdown("Get pics of the vehicle")
                summary.append("Next steps: Get the address for pickup; Get Pics of the title front & back; Get pics of the vehicle")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario 5: No Run And Drive | Over $700 | With Title")
        summary.append("Customer accepts the offer?: No")

        st.markdown("Customer accepts the offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. Title/mileage notes
        st.markdown("1. Title/mileage notes")
        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s5_rej_title_in_name")
        v2 = yes_no_radio(p2, key="s5_rej_liens")
        v3 = yes_no_radio(p3, key="s5_rej_miles")
        notes = st.text_area("Title/mileage notes", key="s5_rej_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"Title/mileage notes: {notes}")

        # 2. Driving notes
        st.markdown("2. Driving notes")
        why_not = st.text_input("Do you know why it won’t run? text", key="s5_rej_why_not_run")
        run_with_jump_radio("s5_rej", summary)
        drive_notes = st.text_area("Driving notes", key="s5_rej_driving_notes")

        summary.append(f"Do you know why it won’t run?: {why_not}")
        summary.append(f"Driving notes: {drive_notes}")

        # 3. Damage/missing parts notes
        damage_block(prefix="s5_rej", step_label="3.", summary=summary)

        # 4. Pictures & vin
        st.markdown("4. Pictures & vin")
        pics_prompt = (
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle, "
            "and VIN (See if the customer will send it while on the phone.)"
        )
        st.markdown(pics_prompt)
        pics_vin = st.text_area("Pictures & vin notes", key="s5_rej_pics_vin")
        summary.append(f"Pictures & vin notes: {pics_vin}")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 6: No Run And Drive | Over $700 | Without Title.
def render_scenario_6(customer_accepts: str):
    st.markdown("### Scenario 6: No Run And Drive | Over $700 | Without Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give the offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario 6: No Run And Drive | Over $700 | Without Title")
        summary.append("Customer accepts the offer?: Yes")

        st.markdown("Customer accepts the offer? Yes")
        st.markdown("1. Sounds great! Let’s confirm some info and get you scheduled")

        # 2. Title/mileage notes
        st.markdown("2. Title/mileage notes: I see there is no title. May I ask what happened with it?")
        st.markdown("I see there is no title. May I ask what happened with it?")
        summary.append("Statement: I see there is no title. May I ask what happened with it?")

        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Is it possible to get the title? Yes/No"
        p4 = "What proof of ownership do you have (bill of sale, registration, insurance)?"
        p5 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s6_acc_title_in_name")
        v2 = yes_no_radio(p2, key="s6_acc_liens")
        v3 = yes_no_radio(p3, key="s6_acc_possible_title")
        po = proof_of_ownership_radio("s6_acc", summary, prompt_suffix=p4)
        v5 = yes_no_radio(p5, key="s6_acc_miles")
        notes = st.text_area("Title/mileage notes", key="s6_acc_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"{p5} {v5}")
        summary.append(f"Title/mileage notes: {notes}")

        # 3. Driving notes
        st.markdown("3. Driving notes")
        why_not = st.text_input("Do you know why it won’t start? Text", key="s6_acc_why_not_start")
        run_with_jump_radio("s6_acc", summary)
        drive_notes = st.text_area("Driving notes", key="s6_acc_driving_notes")

        summary.append(f"Do you know why it won’t start?: {why_not}")
        summary.append(f"Driving notes: {drive_notes}")

        # 4. Damage/missing parts notes
        damage_block(prefix="s6_acc", step_label="4.", summary=summary)

        # Is the car/vehicle as described?
        p_described = "Is the car as described? Yes/No"
        vehicle_described = st.radio(
            p_described,
            ["Yes", "No"],
            key="s6_acc_vehicle_described"
        )
        summary.append(f"{p_described} {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get the address for pickup")
            st.markdown("Get pictures of the title front & back")
            st.markdown("Get pics of the vehicle")
            summary.append("Next steps: Get the address for pickup; Get pictures of the title front & back; Get pics of the vehicle")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            p_change = "Did the offer change? Yes/No"
            did_offer_change = st.radio(
                p_change,
                ["Yes", "No"],
                key="s6_acc_offer_change"
            )
            summary.append(f"{p_change} {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if the offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if the offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get the address for pickup")
                st.markdown("Get Pics of the title front & back")
                st.markdown("Get pics of the vehicle")
                summary.append("Next steps: Get the address for pickup; Get Pics of the title front & back; Get pics of the vehicle")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario 6: No Run And Drive | Over $700 | Without Title")
        summary.append("Customer accepts the offer?: No")

        st.markdown("Customer accepts the offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. Title/mileage notes
        st.markdown("1. Title/mileage notes")
        st.markdown("I see there is no title. May I ask what happened with it?")
        summary.append("Statement: I see there is no title. May I ask what happened with it?")

        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Is it possible to get the title? Yes/No"
        p4 = "What proof of ownership do you have (bill of sale, registration, insurance)?"
        p5 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s6_rej_title_in_name")
        v2 = yes_no_radio(p2, key="s6_rej_liens")
        v3 = yes_no_radio(p3, key="s6_rej_possible_title")
        po = proof_of_ownership_radio("s6_rej", summary, prompt_suffix=p4)
        v5 = yes_no_radio(p5, key="s6_rej_miles")
        notes = st.text_area("Title/mileage notes", key="s6_rej_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"{p5} {v5}")
        summary.append(f"Title/mileage notes: {notes}")

        # 2. Driving notes
        st.markdown("2. Driving notes")
        why_not = st.text_input("Do you know why it won’t start? Text", key="s6_rej_why_not_start")
        run_with_jump_radio("s6_rej", summary)
        drive_notes = st.text_area("Driving notes", key="s6_rej_driving_notes")

        summary.append(f"Do you know why it won’t start?: {why_not}")
        summary.append(f"Driving notes: {drive_notes}")

        # 3. Damage/missing parts notes
        damage_block(prefix="s6_rej", step_label="3.", summary=summary)

        # 4. Pictures & vin
        st.markdown("4. Pictures & vin")
        pics_prompt = (
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle, "
            "and VIN (See if the customer will send it while on the phone.)"
        )
        st.markdown(pics_prompt)
        pics_vin = st.text_area("Pictures & vin notes", key="s6_rej_pics_vin")
        summary.append(f"Pictures & vin notes: {pics_vin}")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 7: No Run And Drive | Under $700 | With Title.
def render_scenario_7(customer_accepts: str):
    st.markdown("### Scenario 7: No Run And Drive | Under $700 | With Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give an offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario 7: No Run And Drive | Under $700 | With Title")
        summary.append("customer accepts offer?: Yes")

        st.markdown("customer accepts offer? Yes")
        st.markdown("1. sounds great! Let’s confirm some info and get you scheduled")

        # 2. Title/mileage notes
        st.markdown("2. Title/mileage notes")
        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s7_acc_title_in_name")
        v2 = yes_no_radio(p2, key="s7_acc_liens")
        v3 = yes_no_radio(p3, key="s7_acc_miles")
        notes = st.text_area("Title/mileage notes", key="s7_acc_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"Title/mileage notes: {notes}")

        # 3. Driving notes
        st.markdown("3. Driving notes")
        why_not = st.text_input("Do you know why it won’t run?", key="s7_acc_why_not_run")
        run_with_jump_radio("s7_acc", summary)
        drive_notes = st.text_area("Driving notes", key="s7_acc_driving_notes")

        summary.append(f"Do you know why it won’t run?: {why_not}")
        summary.append(f"Driving notes: {drive_notes}")

        # 4. Damage/missing parts notes
        damage_block(prefix="s7_acc", step_label="4.", summary=summary)

        # Is the vehicle as described?
        p_described = "Is the vehicle as described? Yes/No"
        vehicle_described = st.radio(
            p_described,
            ["Yes", "No"],
            key="s7_acc_vehicle_described"
        )
        summary.append(f"{p_described} {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get the address for pickup")
            st.markdown("Get Pics of ID front & back")
            st.markdown("Get pics of proof of ownership")
            st.markdown("Change status (if DV offer send straight to offer accepted)")
            summary.append("Next steps: Get the address for pickup; Get Pics of ID front & back; "
                           "Get pics of proof of ownership; Change status (if DV offer send straight to offer accepted)")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            p_change = "Did the offer change? Yes/No"
            did_offer_change = st.radio(
                p_change,
                ["Yes", "No"],
                key="s7_acc_offer_change"
            )
            summary.append(f"{p_change} {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if the offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if the offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get the address for pickup")
                st.markdown("Get pictures of ID front & back")
                st.markdown("Get pictures of proof of ownership")
                summary.append("Next steps: Get the address for pickup; Get pictures of ID front & back; Get pictures of proof of ownership")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario 7: No Run And Drive | Under $700 | With Title")
        summary.append("Customer accepts the offer?: No")

        st.markdown("Customer accepts the offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. Title/mileage notes
        st.markdown("1. Title/mileage notes")
        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p3 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s7_rej_title_in_name")
        v2 = yes_no_radio(p2, key="s7_rej_liens")
        v3 = yes_no_radio(p3, key="s7_rej_miles")
        notes = st.text_area("Title/mileage notes", key="s7_rej_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"Title/mileage notes: {notes}")

        # 2. Driving notes
        st.markdown("2. Driving notes")
        why_not = st.text_input("Do you know why it won’t run?", key="s7_rej_why_not_run")
        run_with_jump_radio("s7_rej", summary)
        drive_notes = st.text_area("Driving notes", key="s7_rej_driving_notes")

        summary.append(f"Do you know why it won’t run?: {why_not}")
        summary.append(f"Driving notes: {drive_notes}")

        # 3. Damage/missing parts notes
        damage_block(prefix="s7_rej", step_label="3.", summary=summary)

        # 4. pics & vin
        st.markdown("4. pics & vin")
        pics_prompt = (
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle and VIN? "
            "(See if the customer will send it while on the phone.)"
        )
        st.markdown(pics_prompt)
        pics_vin = st.text_area("pics & vin notes", key="s7_rej_pics_vin")
        summary.append(f"pics & vin notes: {pics_vin}")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))


# Scenario 8: No Run And Drive | Under $700 | Without Title.
def render_scenario_8(customer_accepts: str):
    st.markdown("### Scenario 8: No Run And Drive | Under $700 | Without Title.")
    st.markdown("**Initial call:**")
    st.markdown("Give the offer with confidence!")

    if customer_accepts == "Yes":
        summary = []
        summary.append("Scenario 8: No Run And Drive | Under $700 | Without Title")
        summary.append("customer accepts offer?: Yes")

        st.markdown("customer accepts offer? Yes")
        st.markdown("1. sounds great! Let’s confirm some info and get you scheduled")

        # 2. Title/mileage notes
        st.markdown("2. Title/mileage notes: I see there is no title. May I ask what happened with it?")
        st.markdown("I see there is no title. May I ask what happened with it?")
        summary.append("Statement: I see there is no title. May I ask what happened with it?")

        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p4 = "What proof of ownership do you have (bill of sale, registration, insurance)?"
        p3 = "Is it possible to get the title? Yes/No"
        p5 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s8_acc_title_in_name")
        v2 = yes_no_radio(p2, key="s8_acc_liens")
        po = proof_of_ownership_radio("s8_acc", summary, prompt_suffix=p4)
        v3 = yes_no_radio(p3, key="s8_acc_possible_title")
        v5 = yes_no_radio(p5, key="s8_acc_miles")
        notes = st.text_area("Title/mileage notes", key="s8_acc_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"{p5} {v5}")
        summary.append(f"Title/mileage notes: {notes}")

        # 3. Driving notes
        st.markdown("3. Driving notes")
        why_not = st.text_input("Do you know why it won’t run?", key="s8_acc_why_not_run")
        run_with_jump_radio("s8_acc", summary)
        drive_notes = st.text_area("Driving notes", key="s8_acc_driving_notes")

        summary.append(f"Do you know why it won’t run?: {why_not}")
        summary.append(f"Driving notes: {drive_notes}")

        # 4. Damage/missing parts notes
        damage_block(prefix="s8_acc", step_label="4.", summary=summary)

        # Is the vehicle as described?
        p_described = "Is the vehicle as described? Yes/No"
        vehicle_described = st.radio(
            p_described,
            ["Yes", "No"],
            key="s8_acc_vehicle_described"
        )
        summary.append(f"{p_described} {vehicle_described}")

        if vehicle_described == "Yes":
            st.markdown("Get the address for pickup")
            st.markdown("Get pictures of ID front & back")
            st.markdown("Get pictures of proof of ownership")
            st.markdown("Change status. (If DV offer send straight to offer accepted)")
            summary.append("Next steps: Get the address for pickup; Get pictures of ID front & back; "
                           "Get pictures of proof of ownership; Change status. (If DV offer send straight to offer accepted)")
        else:
            st.markdown("Update new information, regenerate offer")
            summary.append("Action: Update new information, regenerate offer")
            p_change = "Did the offer change? Yes/No"
            did_offer_change = st.radio(
                p_change,
                ["Yes", "No"],
                key="s8_acc_offer_change"
            )
            summary.append(f"{p_change} {did_offer_change}")

            if did_offer_change == "Yes":
                st.markdown("Contact management to see if the offer is good")
                st.markdown("And start the loop at the question ‘customer accepts offer?’")
                summary.append("Contact management to see if the offer is good; restart at 'customer accepts offer?'")
            else:
                st.markdown("Get the address for pickup")
                st.markdown("Get pictures of ID front & back")
                st.markdown("Get pictures of proof of ownership")
                st.markdown("Change status. (if DV offer send straight to offer accepted)")
                summary.append("Next steps: Get the address for pickup; Get pictures of ID front & back; "
                               "Get pictures of proof of ownership; Change status. (if DV offer send straight to offer accepted)")

        st.markdown("### Copy summary")
        st.code("\n".join(summary))

    else:
        summary = []
        summary.append("Scenario 8: No Run And Drive | Under $700 | Without Title")
        summary.append("Customer accepts the offer?: No")

        st.markdown("Customer accepts the offer? No")
        st.markdown("No problem! We can usually pay more with a few more details confirmed.")

        # 1. Title/mileage notes
        st.markdown("1. Title/mileage notes: I see there is no title. May I ask what happened with it?")
        st.markdown("I see there is no title. May I ask what happened with it?")
        summary.append("Statement: I see there is no title. May I ask what happened with it?")

        p1 = "Is the title in your name? Yes/No"
        p2 = "Are there any liens on the title? Yes/No"
        p4 = "What proof of ownership do you have (bill of sale, registration, insurance)?"
        p3 = "Is it possible to get the title? Yes/No"
        p5 = "Just to confirm, the car has xxx miles? Yes/No"

        v1 = yes_no_radio(p1, key="s8_rej_title_in_name")
        v2 = yes_no_radio(p2, key="s8_rej_liens")
        po = proof_of_ownership_radio("s8_rej", summary, prompt_suffix=p4)
        v3 = yes_no_radio(p3, key="s8_rej_possible_title")
        v5 = yes_no_radio(p5, key="s8_rej_miles")
        notes = st.text_area("Title/mileage notes", key="s8_rej_title_mileage_notes")

        summary.append(f"{p1} {v1}")
        summary.append(f"{p2} {v2}")
        summary.append(f"{p3} {v3}")
        summary.append(f"{p5} {v5}")
        summary.append(f"Title/mileage notes: {notes}")

        # 2. Driving notes
        st.markdown("2. Driving notes")
        why_not = st.text_input("Do you know why it won’t run?", key="s8_rej_why_not_run")
        run_with_jump_radio("s8_rej", summary)
        drive_notes = st.text_area("Driving notes", key="s8_rej_driving_notes")

        summary.append(f"Do you know why it won’t run?: {why_not}")
        summary.append(f"Driving notes: {drive_notes}")

        # 3. Damage/missing parts notes
        damage_block(prefix="s8_rej", step_label="3.", summary=summary)

        # 4. Pics & vin
        st.markdown("4. Pics & vin")
        pics_prompt = (
            "What’s the easiest way for you to send: Pictures of the inside and outside of the vehicle and VIN? "
            "(See if the customer will send it while on the phone.)"
        )
        st.markdown(pics_prompt)
        pics_vin = st.text_area("Pics & vin notes", key="s8_rej_pics_vin")
        summary.append(f"Pics & vin notes: {pics_vin}")
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
elif scenario_option == "no run and drive/ over 700/ with title":
    render_scenario_5(customer_accepts)
elif scenario_option == "no run and drive/ over 700/ without title":
    render_scenario_6(customer_accepts)
elif scenario_option == "no run and drive/ under 700/ with title":
    render_scenario_7(customer_accepts)
elif scenario_option == "no run and drive/ under 700/ without title":
    render_scenario_8(customer_accepts)
