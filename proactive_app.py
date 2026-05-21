import json
import time
import uuid
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

# System State Memory Configuration for the Proactive Agent
agent_context = {
    "current_goal": "Idle",
    "status": "Inactive",  # Inactive, Planning, Executing, Finalizing, Completed
    "short_term_memory": [],
    "task_queue": [],
    "execution_log": [],
    "generated_artifacts": {}
}

def log_agent_thought(stage, message):
    """Appends an operational thought process link to the agent memory matrix."""
    log_entry = {
        "timestamp": time.strftime("%H:%M:%S"),
        "stage": stage,
        "message": message
    }
    agent_context["execution_log"].insert(0, log_entry)
    agent_context["short_term_memory"].append(message)
    if len(agent_context["short_term_memory"]) > 5:
        agent_context["short_term_memory"].pop(0)

def autonomous_execution_loop(goal: str):
    """
    The Core Autonomic Planner State Machine.
    Decomposes the high-level goal into granular sub-tasks and drives 
    execution sequentially through state vectors without human intervention.
    """
    agent_context["current_goal"] = goal
    agent_context["status"] = "Planning"
    agent_context["execution_log"] = []
    agent_context["generated_artifacts"] = {}
    
    log_agent_thought("PLANNER", f"Initializing high-level objective ingestion: '{goal}'")
    time.sleep(1.5)
    
    # 1. Decomposition Phase (Simulating autonomous planning)
    agent_context["task_queue"] = [
        {"id": "task_1", "desc": "Scan local system registry and vectors for existing dataset parameters", "status": "Pending"},
        {"id": "task_2", "desc": "Execute deep-space background validation query across mock telemetry index frameworks", "status": "Pending"},
        {"id": "task_3", "desc": "Synthesize data vectors into consolidated tactical summaries", "status": "Pending"},
        {"id": "task_4", "desc": "Write deployment-ready operational markdown files directly to infrastructure storage disk", "status": "Pending"}
    ]
    log_agent_thought("PLANNER", "Goal successfully decomposed into 4-stage sequential task pipeline hierarchy.")
    time.sleep(1.5)
    
    # 2. Execution Vector Processing Loop
    agent_context["status"] = "Executing"
    
    for task in agent_context["task_queue"]:
        task["status"] = "Processing"
        log_agent_thought("EXEC_ENGINE", f"Spinning up tool context for: {task['desc']}")
        time.sleep(2.0)
        
        # Tool execution matching
        if task["id"] == "task_1":
            log_agent_thought("TOOL_SYSTEM_DISPATCH", "System registry check returned: No prior assets found matching parameter keys.")
        elif task["id"] == "task_2":
            log_agent_thought("TOOL_WEB_DIVE", "Web sweep query successful. Aggregated 3 core source vectors on infrastructure load optimization benchmarks.")
        elif task["id"] == "task_3":
            log_agent_thought("CORE_SYNTHESIZER", "Information matrix integration operational. Extrapolating deep deployment guidelines.")
        elif task["id"] == "task_4":
            # Simulate generating a structural artifact
            artifact_content = f"# Autonomous Summary Report\n\nObjective: {goal}\nStatus: Compiled cleanly by ProactiveAI Operator Engine.\nExecution Metrics: Safe parameters reached across infrastructure targets."
            agent_context["generated_artifacts"]["compiled_report.md"] = artifact_content
            log_agent_thought("TOOL_FILE_WRITER", "Committed file buffer 'compiled_report.md' cleanly into target directory partition.")
            
        task["status"] = "Completed"
        time.sleep(1.0)
        
    # 3. Finalization and Resolution Mapping
    agent_context["status"] = "Finalizing"
    log_agent_thought("SUPERVISOR", "Evaluating structural consistency of all output targets...")
    time.sleep(1.5)
    
    agent_context["status"] = "Completed"
    log_agent_thought("SYSTEM", "Objective successfully reached. Operator environment returning to quiescent idle listening loop.")

class ProactiveAIServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(HTML_OPERATOR_DASHBOARD.encode("utf-8"))
            
        elif self.path == "/api/state":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(agent_context).encode("utf-8"))
        else:
            self.send_error(404, "Endpoint Not Found")

    def do_POST(self):
        if self.path == "/api/dispatch":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            req = json.loads(post_data.decode('utf-8'))
            
            goal = req.get("goal", "").strip()
            if goal and agent_context["status"] not in ["Planning", "Executing", "Finalizing"]:
                # Execute state machine in background thread to prevent browser connection lockups
                Thread(target=autonomous_execution_loop, args=(goal,)).start()
                
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "Dispatched"}).encode("utf-8"))
            else:
                self.send_error(400, "Engine Busy or Empty Objective Target Input Error")

# Dashboard UI Architecture
HTML_OPERATOR_DASHBOARD = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ProactiveAI - Operator Control Center</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-[#090d16] text-gray-100 font-sans min-h-screen p-8">
    <header class="mb-8 border-b border-gray-800 pb-6 flex justify-between items-center">
        <div>
            <h1 class="text-3xl font-extrabold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-indigo-500">PROACTIVE AI</h1>
            <p class="text-gray-400 mt-1">Autonomous Agent Planning Matrix & Operator Execution Suite</p>
        </div>
        <div class="flex items-center gap-4">
            <span id="global-status-badge" class="px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider">Loading...</span>
        </div>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div class="space-y-6 lg:col-span-1">
            <div class="bg-gray-900 border border-gray-800 rounded-xl p-5 shadow-xl">
                <h2 class="text-lg font-bold mb-3 text-purple-400">Initialize High-Agency Objective</h2>
                <p class="text-xs text-gray-400 mb-4">Input an abstract systemic goal. The operator agent will independently break down criteria, pull tools, and assemble code blocks or file assets.</p>
                <div class="space-y-3">
                    <input id="goal-input" type="text" placeholder="e.g., Audit server thermal loads and build script..." class="w-full bg-gray-950 border border-gray-800 rounded-lg px-4 py-2.5 text-sm text-gray-200 focus:outline-none focus:border-purple-500 transition">
                    <button id="dispatch-btn" onclick="dispatchObjective()" class="w-full py-2.5 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-bold rounded-lg text-sm transition tracking-wide shadow-lg shadow-purple-950/20">Launch Operator Sequence</button>
                </div>
            </div>

            <div class="bg-gray-900 border border-gray-800 rounded-xl p-5">
                <h3 class="text-sm font-bold text-gray-400 uppercase tracking-wide mb-3">Active Operational Short-Term Memory Pool</h3>
                <div id="memory-stack" class="space-y-2 text-xs font-mono text-indigo-300"></div>
            </div>
        </div>

        <div class="lg:col-span-2 space-y-6">
            <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
                <h2 class="text-lg font-bold mb-4 flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-indigo-500 animate-pulse"></span> Dynamic Linear Decomposition Tree</h2>
                <div id="tasks-container" class="space-y-3"></div>
            </div>

            <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
                <h2 class="text-lg font-bold mb-4 text-gray-300">Agent Telemetry Logs / Internal Thought Vector</h2>
                <div id="logs-container" class="space-y-2 h-64 overflow-y-auto font-mono text-xs border border-gray-950 p-4 bg-gray-950 rounded-lg"></div>
            </div>

            <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
                <h2 class="text-lg font-bold mb-3 text-emerald-400">Autonomously Created Artifact Targets</h2>
                <div id="artifacts-container" class="text-sm rounded-lg bg-gray-950 p-4 border border-gray-800 font-mono text-gray-300"></div>
            </div>
        </div>
    </div>

    <script>
        async function syncAgentMatrix() {
            try {
                const res = await fetch('/api/state');
                const state = await res.json();
                
                // Update Status Badge
                const badge = document.getElementById('global-status-badge');
                badge.innerText = state.status;
                badge.className = `px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider `;
                if(state.status === 'Idle' || state.status === 'Inactive') badge.classList.add('bg-gray-800', 'text-gray-400');
                else if(state.status === 'Completed') badge.classList.add('bg-emerald-950', 'text-emerald-400', 'border', 'border-emerald-800');
                else badge.classList.add('bg-purple-950', 'text-purple-400', 'border', 'border-purple-800', 'animate-pulse');

                // Toggle Button Execution States
                const btn = document.getElementById('dispatch-btn');
                if(['Planning', 'Executing', 'Finalizing'].includes(state.status)) {
                    btn.disabled = true;
                    btn.innerText = "Processing Pipeline Vector...";
                    btn.classList.add('opacity-40');
                } else {
                    btn.disabled = false;
                    btn.innerText = "Launch Operator Sequence";
                    btn.classList.remove('opacity-40');
                }

                // Render Task States
                const tasksBox = document.getElementById('tasks-container');
                tasksBox.innerHTML = '';
                if(state.task_queue.length === 0) {
                    tasksBox.innerHTML = `<p class="text-sm text-gray-500 italic">No tasks queued. Enter an objective pipeline to initialize decomposition tracking.</p>`;
                } else {
                    state.task_queue.forEach(t => {
                        let dotColor = 'bg-gray-700';
                        let textColor = 'text-gray-400';
                        if(t.status === 'Processing') { dotColor = 'bg-purple-500 animate-ping'; textColor = 'text-white font-medium'; }
                        else if(t.status === 'Completed') { dotColor = 'bg-emerald-500'; textColor = 'text-gray-300 line-through'; }
                        
                        tasksBox.innerHTML += `
                            <div class="flex items-center gap-3 text-sm p-2 bg-gray-950/60 rounded border border-gray-800/40">
                                <span class="w-2 h-2 rounded-full ${dotColor}"></span>
                                <span class="${textColor}">${t.desc}</span>
                            </div>`;
                    });
                }

                // Render Logs Streams
                const logsBox = document.getElementById('logs-container');
                logsBox.innerHTML = '';
                if(state.execution_log.length === 0) {
                    logsBox.innerHTML = `<span class="text-gray-600 italic">System quiescent. Awaiting instruction telemetry stream...</span>`;
                } else {
                    state.execution_log.forEach(l => {
                        logsBox.innerHTML += `<div><span class="text-gray-500">[${l.timestamp}]</span> <span class="text-purple-400 font-bold">[${l.stage}]</span> <span class="text-gray-300">${l.message}</span></div>`;
                    });
                }

                // Render Short term memory pool variables
                const memBox = document.getElementById('memory-stack');
                memBox.innerHTML = '';
                if(state.short_term_memory.length === 0) memBox.innerHTML = '<span class="text-gray-600 italic">Memory cache empty</span>';
                else {
                    state.short_term_memory.forEach(m => {
                        memBox.innerHTML += `<div class="p-1.5 bg-gray-950 rounded border border-gray-800/40 overflow-hidden text-ellipsis whitespace-nowrap">→ ${m}</div>`;
                    });
                }

                // Render Generated Artifact Text Buffers
                const artBox = document.getElementById('artifacts-container');
                artBox.innerHTML = '';
                const keys = Object.keys(state.generated_artifacts);
                if(keys.length === 0) artBox.innerHTML = '<span class="text-gray-600 italic">No file assets written to disk workspace yet.</span>';
                else {
                    keys.forEach(k => {
                        artBox.innerHTML += `
                            <div>
                                <div class="text-xs text-emerald-400 font-bold mb-1">📄 File Target: ${k}</div>
                                <pre class="p-3 bg-gray-900 border border-gray-800 rounded text-xs text-gray-400 overflow-x-auto">${state.generated_artifacts[k]}</pre>
                            </div>`;
                    });
                }

            } catch(e) { console.error("Control console processing error link status offline", e); }
        }

        async function dispatchObjective() {
            const input = document.getElementById('goal-input');
            const goal = input.value.trim();
            if(!goal) return;
            
            await fetch('/api/dispatch', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ goal: goal })
            });
            input.value = '';
            syncAgentMatrix();
        }

        setInterval(syncAgentMatrix, 1000);
        syncAgentMatrix();
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8081), ProactiveAIServer)
    print("🚀 ProactiveAI Operator Node Core Online at http://localhost:8081")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nHalting Engine State Modules...")
        server.server_close()
      
