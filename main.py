import asyncio
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig
from google.antigravity.utils.interactive import run_interactive_loop
from tools import save_report

async def run_study_buddy():
    # 1. Define our configuration object with strict constraints and NO default system capabilities
    config = LocalAgentConfig(
        system_instructions=(
            "You are a strict Multi-Agent Study Buddy. You must follow these steps in order:\n\n"
            "Step 1 (ProfessorAgent Mode): Look at the computer science topic the user provided and "
            "immediately print a short, challenging 3-question quiz. Do NOT attempt to check local files, "
            "do NOT try to list directory contents, and do NOT use any tools yet. Just output the quiz text and stop.\n\n"
            "Step 2 (GraderAgent Mode): Once the user replies with their answers, strictly evaluate them out of 100 "
            "and write clear feedback.\n\n"
            "Step 3 (Tool Execution): ONLY after printing the grade and feedback, execute the 'save_report' "
            "tool to save the results to disk. Do not attempt to use any other tools."
        ),
        tools=[save_report],
        capabilities=CapabilitiesConfig(interpreter=False) # Disables the agent's ability to run random background code
    )

    print("Launching your Capstone Project via Google Antigravity Engine...")
    print("Type 'exit' or press Ctrl+C to stop.\n" + "="*50)

    # 2. Pass the config directly into the interactive loop helper
    await run_interactive_loop(config)

if __name__ == "__main__":
    asyncio.run(run_study_buddy())