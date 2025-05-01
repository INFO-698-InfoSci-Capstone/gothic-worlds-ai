#!/usr/bin/env bash
set -a
source .env
set +a

#
# start.sh
#
# 1) Kills any processes on ports 5000 & $FRONTEND_PORT
# 2) Removes the .next folder (if any) in frontend/
# 3) Starts the backend (listening on port 5000)
# 4) Waits 2 seconds
# 5) Starts the frontend (listening on port $FRONTEND_PORT)
# 6) Waits for user input
# 7) Gracefully kills the two Node processes it started
#
# Usage:
#   chmod +x start.sh   # make it executable
#   ./start.sh

###################################
# 1) Kill processes on port 5000 & $FRONTEND_PORT (Optional)
###################################
echo "Killing processes on port $BACKEND_PORT..."
PIDS_5000=$(lsof -ti :$BACKEND_PORT 2>/dev/null)  # Mac/Linux command to find PIDs on port 5000
if [ -n "$PIDS_5000" ]; then
  kill -9 $PIDS_5000
  echo "Killed processes on port $BACKEND_PORT."
else
  echo "No processes running on port $BACKEND_PORT."
fi

echo "Killing processes on port $FRONTEND_PORT..."
PIDS_3000=$(lsof -ti :$FRONTEND_PORT 2>/dev/null)
if [ -n "$PIDS_3000" ]; then
  kill -9 $PIDS_3000
  echo "Killed processes on port $FRONTEND_PORT."
else
  echo "No processes running on port $FRONTEND_PORT."
fi

###################################
# 2) Delete the .next folder
###################################
if [ -d "./frontend/.next" ]; then
  echo "Deleting .next folder..."
  rm -rf "./frontend/.next"
  echo ".next folder deleted successfully."
else
  echo ".next folder does not exist; skipping deletion."
fi

###################################
# 3) Start backend in the background
###################################
echo "Starting Narrator AI backend server..."
(
  cd backend || exit 1
  npm run dev
) &
BACKEND_PID=$!

###################################
# 4) Wait briefly before starting frontend
###################################
sleep 2

###################################
# 5) Start frontend in the background
###################################
echo "Starting Narrator AI frontend..."
(
  cd frontend || exit 1
  npm run dev
) &
FRONTEND_PID=$!

###################################
# 6) Output info & wait for user
###################################
echo "========================================="
echo "Narrator AI is running!"
echo "Backend:  $BACKEND_HOST:$BACKEND_PORT"
echo "Frontend: $FRONTEND_HOST:$FRONTEND_PORT"
echo "========================================="
echo "Press [ENTER] to stop all servers..."
read -r

###################################
# 7) Gracefully kill the two PIDs
###################################
echo "Stopping Narrator AI..."

# Send SIGTERM (default) to each process
kill "$BACKEND_PID" "$FRONTEND_PID"

# Wait for them to exiti
wait "$BACKEND_PID" "$FRONTEND_PID" 2>/dev/null

echo "All servers stopped gracefully."