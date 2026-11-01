from google.adk.agents import Agent

itinerary_agent = Agent(
    name="itinerary_agent",
    model="gemini-2.0-flash",
    description="Creates day-by-day travel itineraries.",
    instruction="""You are a travel itinerary planner. Build clear day-by-day itineraries considering rest and realistic travel movement.""",
)