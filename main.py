import streamlit as st
import config
import time
from simulation.world import World
from simulation.trip_manager import TripManager
from entities.rider import Rider
from entities.driver import Driver
from entities.vehicle import Vehicle
from strategies.routing.eco_friendly import EcoFriendlyRoute

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="EcoRide Dispatcher", layout="wide")

def main():
    st.title("🚖 EcoRide: Optimal Fleet Dispatch Simulation")
    st.sidebar.header("Simulation Controls")

    # Initialize Backend Logic (Caching prevents re-running every click)
    @st.cache_resource
    def init_simulation():
        world = World()
        routing_strategy = EcoFriendlyRoute()
        trip_manager = TripManager(world.quadtree, world.graph, routing_strategy)
        
        # Build Grid (Same logic as your Pygame code)
        world.graph.adj_list.clear()
        step = 80
        for x in range(0, config.SCREEN_WIDTH, step):
            for y in range(0, config.SCREEN_HEIGHT, step):
                if x + step < config.SCREEN_WIDTH:
                    world.graph.add_edge((x, y), (x + step, y), step)
                if y + step < config.SCREEN_HEIGHT:
                    world.graph.add_edge((x, y), (x, y + step), step)
        return world, trip_manager

    world, trip_manager = init_simulation()

    # 2. UI INPUTS (Replacing Mouse Clicks)
    with st.sidebar:
        st.write("### Add a Driver")
        d_x = st.slider("Driver X Position", 0, config.SCREEN_WIDTH, 100)
        d_y = st.slider("Driver Y Position", 0, config.SCREEN_HEIGHT, 100)
        if st.button("Add Driver"):
            new_driver = Driver(d_x, d_y, Vehicle(1.0, 100))
            new_driver.id = f"D-{len(world.drivers) + 1}"
            world.drivers.append(new_driver)
            st.success(f"Added {new_driver.id}")

        st.divider()
        if st.button("🗑️ Reset Map"):
            world.drivers.clear()
            st.rerun()

    # 3. DISPATCH LOGIC
    st.write("### Dispatch a Rider")
    col1, col2 = st.columns(2)
    with col1:
        r_x = st.number_input("Rider X", 0, config.SCREEN_WIDTH, 400)
    with col2:
        r_y = st.number_input("Rider Y", 0, config.SCREEN_HEIGHT, 400)

    if st.button("Find Optimal Driver"):
        if not world.drivers:
            st.error("Please add at least one driver from the sidebar first!")
        else:
            active_rider = Rider(r_x, r_y, 0, 0)
            
            # This triggers your algorithm!
            with st.spinner("Calculating eco-friendly route..."):
                trip_manager.request_fleet_dispatch(world.drivers, active_rider)
                st.success("Dispatch Algorithm Complete!")
                
                # Show results in a table for the recruiter
                st.write("#### Fleet Status")
                driver_data = [{"ID": d.id, "Pos": (d.x, d.y)} for d in world.drivers]
                st.table(driver_data)

    st.info("Note: This web version focuses on the backend dispatching logic for your portfolio.")

if __name__ == "__main__":
    main()
