# ProactiveAI: Autonomous Agent Task-Planning & Execution Engine

ProactiveAI is a high-agency, state-machine-driven agent prototype engineered to operate as an autonomous systems administrator. Shifting away from traditional reactive, prompt-and-response chatbot interactions, this architecture is built to ingest abstract, long-form systemic objectives, decompose them into linear task dependency trees, and execute steps independently using tool dispatches.

## ⚙️ Core System Design & Phases
The engine processes objectives through a rigorous, linear phase-gating loop to ensure logical execution consistency:

1. **Decomposition Matrix (Phase 1):** Breaks down complex, high-level commands into distinct sequential sub-tasks with tracked operational states (`Pending`, `Processing`, `Completed`).
2. **Execution State (Phase 2):** Switches system processing modes to actively execute the lifecycle of each queued task object sequentially.
3. **Tool Context Ring (Phase 3):** Simulates autonomous workspace tool invocation, mimicking operations like disk storage queries, external network scans, data synthesizers, and direct file-system buffer writers.
4. **Artifact Compilation (Phase 4):** Finalizes operational pipelines by compiling short-term memory state structures into standalone functional markdown files written directly to disk storage.

## 💎 Key Features
* **High-Agency Autonomy Loop:** Runs entirely independent of mid-cycle human confirmation, terminating only when objective parameters are successfully satisfied.
* **State Dependency Tracking:** Complete visualization of agent state modifications (`Idle` -> `Planning` -> `Executing` -> `Finalizing` -> `Completed`) via a live interface.
* **Live Telemetry Streams:** A real-time terminal output interface rendering internal engine thought patterns and tool actions as operations occur.
* **Short-Term Memory Pool:** Maintains an ephemeral cache array tracking telemetry thoughts and execution states to guide step progression without human intervention loops.

## 🛠️ Tech Stack
* **Backend Architecture:** Python (Multithreaded Execution Management, Base HTTP Request Mapping, JSON State Infrastructure)
* **Frontend Controller:** HTML5, Tailwind CSS, Native JavaScript (Async UI Telemetry Polling & API Stream Handlers)
* https://github.com/paka2002/ProactiveAI/blob/ed91eff3b3b51f38667d84cc41b20158d0d6b880/Screenshot_20260522-034023.png
