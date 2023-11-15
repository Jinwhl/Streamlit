import streamlit as st
import matplotlib.pyplot as plt
import math

def Y_calculator(rho, u, l, mu, y_plus):
    Re = rho * u * l / mu
    C_f = (2 * math.log10(Re) - 0.56) ** (-2.3)
    tau_w = C_f * 0.5 * rho * u ** 2
    u_star = math.sqrt(tau_w / rho)
    y = y_plus * mu / (rho * u_star)
    delta_lam = 5 * l / math.sqrt(Re)
    delta_turb = 0.37 * l / (Re ** (1 / 5))

    return y, delta_lam, delta_turb

def y_plus_calculator_page():
    st.title("Y+ Calculator")

    density, velocity, length, dynamic_viscosity, y_plus = (
        st.number_input("공기 밀도 (kg/m³):", value=1.225, format="%.3f"),
        st.number_input("유체의 속도 (m/s):", value=10.0),
        st.number_input("물체의 길이 (m):", value=1.0),
        st.number_input("공기의 동적 점성 (m^2/s):", value=1.79e-5),
        st.number_input("Y+:", value=20)
    )

    # Y 계산
    value_y, value_lam, value_turb = Y_calculator(density, velocity, length, dynamic_viscosity, y_plus)

    st.write(f"Desired first layer thickness [m]: {value_y}")
    st.write(f"Laminar boundary layer thickness at L [m]: {value_lam}")
    st.write(f"Turbulent boundary layer thickness at L [m]: {value_turb}")

    # 시각화
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 0])  # 예시 그래프
    st.pyplot(fig)

if __name__ == "__main__":
    y_plus_calculator_page()
