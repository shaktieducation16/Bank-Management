import streamlit as st
import random

st.set_page_config(page_title="ABC Bank of India", page_icon="🏦", layout="centered")

# Store account data in session state
if "data" not in st.session_state:
    st.session_state.data = {}

data = st.session_state.data

st.title("🏦 ABC BANK OF INDIA")
st.markdown("---")

menu = st.sidebar.selectbox(
    "Select Service",
    [
        "Create New Account",
        "Deposit Money",
        "Withdraw Money",
        "Update Account",
        "Check Balance",
        "Delete Account",
        "View All Accounts"
    ]
)

# ---------------- CREATE ACCOUNT ----------------
if menu == "Create New Account":
    st.header("Create New Account")

    with st.form("create_form"):
        name = st.text_input("Name")
        dob = st.date_input("Date of Birth")
        address = st.text_area("Address")
        aadhar = st.text_input("Aadhar Number")
        number = st.text_input("Mobile Number")
        amount = st.number_input(
            "Opening Balance",
            min_value=0,
            step=100
        )

        submit = st.form_submit_button("Create Account")

    if submit:

        if len(aadhar) != 12:
            st.error("Aadhar Number must be 12 digits.")

        elif len(number) != 10:
            st.error("Mobile Number must be 10 digits.")

        else:
            account_number = random.randint(1000, 9999)

            while account_number in data:
                account_number = random.randint(1000, 9999)

            data[account_number] = {
                "name": name,
                "dob": str(dob),
                "address": address,
                "aadhar": aadhar,
                "number": number,
                "amount": amount
            }

            st.success("Account Created Successfully!")
            st.info(f"Your Account Number is **{account_number}**")


# ---------------- DEPOSIT ----------------
elif menu == "Deposit Money":

    st.header("Deposit Money")

    account = st.number_input("Account Number", step=1)

    deposit_amount = st.number_input(
        "Deposit Amount",
        min_value=0,
        step=100
    )

    if st.button("Deposit"):

        account = int(account)

        if account in data:

            data[account]["amount"] += deposit_amount

            st.success("Money Deposited Successfully!")

            st.write("Current Balance:",
                     data[account]["amount"])

        else:
            st.error("Account Not Found")


# ---------------- WITHDRAW ----------------
elif menu == "Withdraw Money":

    st.header("Withdraw Money")

    account = st.number_input("Account Number", step=1)

    withdraw_amount = st.number_input(
        "Withdraw Amount",
        min_value=0,
        step=100
    )

    if st.button("Withdraw"):

        account = int(account)

        if account in data:

            if withdraw_amount <= data[account]["amount"]:

                data[account]["amount"] -= withdraw_amount

                st.success("Withdrawal Successful!")

                st.write("Remaining Balance:",
                         data[account]["amount"])

            else:
                st.error("Insufficient Balance")

        else:
            st.error("Account Not Found")


# ---------------- UPDATE ----------------
elif menu == "Update Account":

    st.header("Update Account")

    account = st.number_input("Account Number", step=1)

    option = st.radio(
        "Select Field",
        ["Name", "Mobile Number"]
    )

    if option == "Name":
        new_value = st.text_input("New Name")
    else:
        new_value = st.text_input("New Mobile Number")

    if st.button("Update"):

        account = int(account)

        if account in data:

            if option == "Name":
                data[account]["name"] = new_value

            else:

                if len(new_value) != 10:
                    st.error("Mobile Number must be 10 digits.")
                    st.stop()

                data[account]["number"] = new_value

            st.success("Information Updated Successfully!")

        else:
            st.error("Account Not Found")


# ---------------- BALANCE ----------------
elif menu == "Check Balance":

    st.header("Check Balance")

    account = st.number_input("Account Number", step=1)

    if st.button("Check"):

        account = int(account)

        if account in data:

            st.success(
                f"Current Balance: ₹{data[account]['amount']}"
            )

        else:
            st.error("Account Not Found")


# ---------------- DELETE ----------------
elif menu == "Delete Account":

    st.header("Delete Account")

    account = st.number_input("Account Number", step=1)

    if st.button("Delete"):

        account = int(account)

        if account in data:

            del data[account]

            st.success("Account Deleted Successfully")

        else:
            st.error("Account Not Found")


# ---------------- VIEW ----------------
elif menu == "View All Accounts":

    st.header("All Accounts")

    if data:

        for acc, details in data.items():

            st.expander(f"Account {acc}").write(details)

    else:
        st.info("No Accounts Available")