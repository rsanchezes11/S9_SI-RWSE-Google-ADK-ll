from google.adk.agents import Agent
from travel_assistant.tools.budget_tools import estimate_trip_budget

budget_agent = Agent(
    name="budget_agent",
    model="gemini-2.0-flash",
    description="Estimates basic travel budgets.",
    instruction="""You are a travel budget advisor. Estimate basic travel budgets using the available tool.""",
    tools=[estimate_trip_budget],
)