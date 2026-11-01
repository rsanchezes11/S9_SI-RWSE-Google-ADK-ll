from google.adk.agents import Agent
from travel_assistant.tools.risk_tools import assess_basic_travel_risks

risk_reviewer_agent = Agent(
    name="risk_reviewer_agent",
    model="gemini-2.0-flash",
    description="Reviews travel risks and practical recommendations.",
    instruction="""You are a travel risk reviewer. Identify practical travel risks using the available tool.""",
    tools=[assess_basic_travel_risks],
)