import streamlit as st

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('select * from django_migrations;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.app} has {row.name}")
