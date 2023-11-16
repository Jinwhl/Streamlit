import streamlit as st
import plotly.graph_objects as go
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

def calculate_layers(layer, G_r, value_y, value_lam, value_turb, y_desired):
    layer_thickness = []
    layer_index = []
    total_thickness = []
    total = 0

    for i in range(0, layer):
        growth_rate = G_r ** i
        layer_thickness.append(value_y * growth_rate)
        total += value_y * growth_rate
        layer_index.append(i)
        total_thickness.append(total)

    check_lam = [total_thickness[j] - value_lam for j in range(layer)]
    check_turb = [total_thickness[k] - value_turb for k in range(layer)]

    desired_layer_thickness = []
    desired_total_thickness = []
    desired_total = 0

    for q in range(0, layer):
        desired_layer = G_r**q * y_desired
        desired_total += desired_layer
        desired_layer_thickness.append(desired_layer)
        desired_total_thickness.append(desired_total)

    desired_check_lam = [desired_total_thickness[w] - value_lam for w in range(layer)]
    desired_check_turb = [desired_total_thickness[v] - value_turb for v in range(layer)]

    return layer_index, layer_thickness, total_thickness, check_lam, check_turb, desired_layer_thickness, desired_total_thickness, desired_check_lam, desired_check_turb

def visualize_layers(layer_index, layer_thickness, total_thickness, check_lam, check_turb, desired_layer_thickness, desired_total_thickness, desired_check_lam, desired_check_turb):
    fig_layer = go.Figure()
    fig_layer.add_trace(go.Scatter(x=layer_index, y=layer_thickness, mode='lines', name='Layer'))
    fig_layer.add_trace(go.Scatter(x=layer_index, y=total_thickness, mode='lines', name='Total'))
    st.plotly_chart(fig_layer)

    fig_check_re = go.Figure()
    fig_check_re.add_trace(go.Scatter(x=layer_index, y=check_lam, mode='lines', name='Lam'))
    fig_check_re.add_trace(go.Scatter(x=layer_index, y=check_turb, mode='lines', name='Turb'))
    st.plotly_chart(fig_check_re)

    fig_desired_layer = go.Figure()
    fig_desired_layer.add_trace(go.Scatter(x=layer_index, y=desired_layer_thickness, mode='lines', name='Desired layer'))
    fig_desired_layer.add_trace(go.Scatter(x=layer_index, y=desired_total_thickness, mode='lines', name='Desired total'))
    st.plotly_chart(fig_desired_layer)

    fig_desired_check = go.Figure()
    fig_desired_check.add_trace(go.Scatter(x=layer_index, y=desired_check_lam, mode='lines', name='Desired_check_lam'))
    fig_desired_check.add_trace(go.Scatter(x=layer_index, y=desired_check_turb, mode='lines', name='Desired_check_turb'))
    st.plotly_chart(fig_desired_check)

def y_plus_calculator_page():
    st.title("Y+ Calculator")

    density, velocity, length, dynamic_viscosity, y_plus = (
        st.number_input("Density of Air [kg/m³]:", value=1.225, format="%.3f"),
        st.number_input("Velocity of Fluid [m/s]:", value=10.0),
        st.number_input("Length of Object [m]:", value=1.0),
        st.number_input("Dynamic Viscosity of Air [m²/s]:", value=1.79e-5, format="%.8f"),
        st.number_input("Y+:", value=20)
    )

    formatted_dynamic_viscosity = round(dynamic_viscosity, 8)

    # Y 계산
    value_y, value_lam, value_turb = Y_calculator(density, velocity, length, formatted_dynamic_viscosity, y_plus)

    st.write(f"Desired first layer thickness [m]: {value_y}")
    st.write(f"Laminar boundary layer thickness at L [m]: {value_lam}")
    st.write(f"Turbulent boundary layer thickness at L [m]: {value_turb}")

    layer = st.slider("Select the number of layers", 1, 100, 47)
    G_r = st.slider("Select the grid growth rate", 1.01, 2.0, 1.2)

    y_desired = st.number_input("Enter desired layer thickness [m]:", value=0.000001)

    layer_index, layer_thickness, total_thickness, check_lam, check_turb, desired_layer_thickness, desired_total_thickness, desired_check_lam, desired_check_turb = calculate_layers(
        layer, G_r, value_y, value_lam, value_turb, y_desired)

    visualize_layers(layer_index, layer_thickness, total_thickness, check_lam, check_turb, desired_layer_thickness,
                     desired_total_thickness, desired_check_lam, desired_check_turb)

if __name__ == "__main__":
    y_plus_calculator_page()
