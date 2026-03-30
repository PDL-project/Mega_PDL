#!/usr/bin/env python3
"""
Auto-generated multi-robot execution code.
Run with: python <this_file> --floor-plan <N>
"""

import argparse
import sys
import os

import sys
from pathlib import Path
PDL_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PDL_ROOT))
sys.path.insert(0, str(PDL_ROOT / "scripts"))
sys.path.insert(0, str(PDL_ROOT / "resources"))
# Add scripts folder to path
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
scripts_path = os.path.join(base_path, 'scripts')
if scripts_path not in sys.path:
    sys.path.insert(0, scripts_path)

from MultiRobotExecutor import MultiRobotExecutor, SubtaskPlan

# --- Robot Assignment ---
ASSIGNMENT = {1: 2, 2: 3, 3: 1, 4: 3}  # subtask_id -> robot_id
PARALLEL_GROUPS = {1: [1], 2: [2], 3: [3], 4: [4]}  # group_id -> [subtask_ids]
AGENT_COUNT = 3
SPAWN_POSITIONS = {1: (-2.0, 0.9009992480278015, 3.25), 2: (0.75, 0.9009992480278015, 1.5), 3: (-1.0, 0.9009992480278015, 0.5)}  # LP에서 결정된 스폰 좌표

# --- Subtask Plans ---
SUBTASK_PLANS = {
    1: {
        'name': 'subtask_01_Put_the_ButterKnife_in_Drawer1',
        'robot_id': 2,
        'actions': ['gotoobject robot1 drawer (1)', 'openobject robot1 drawer (1)', 'gotoobject robot1 butterknife (1)', 'pickupobject robot1 butterknife drawer (1)', 'gotoobject robot1 drawer1 (1)', 'openobject robot1 drawer1 (1)', 'drophandobject robot1 butterknife drawer1 (1)', 'closeobject robot1 drawer1 (1)'],
        'parallel_group': 1,
    },
    2: {
        'name': 'subtask_02_Put_the_Fork_in_Drawer2',
        'robot_id': 3,
        'actions': ['gotoobject robot1 fork (1)', 'pickupobject robot1 fork countertop (1)', 'gotoobject robot1 drawer2 (1)', 'openobject robot1 drawer2 (1)', 'drophandobject robot1 fork drawer2 (1)', 'closeobject robot1 drawer2 (1)'],
        'parallel_group': 2,
    },
    3: {
        'name': 'subtask_03_Put_the_Spoon_in_Drawer3',
        'robot_id': 1,
        'actions': ['gotoobject robot1 spoon (1)', 'pickupobject robot1 spoon countertop (1)', 'gotoobject robot1 drawer3 (1)', 'openobject robot1 drawer3 (1)', 'drophandobject robot1 spoon drawer3 (1)', 'closeobject robot1 drawer3 (1)'],
        'parallel_group': 3,
    },
    4: {
        'name': 'subtask_04_Put_the_Knife_in_Drawer4',
        'robot_id': 3,
        'actions': ['gotoobject robot1 knife (1)', 'pickupobject robot1 knife countertop (1)', 'gotoobject robot1 drawer4 (1)', 'openobject robot1 drawer4 (1)', 'drophandobject robot1 knife drawer4 (1)', 'closeobject robot1 drawer4 (1)'],
        'parallel_group': 4,
    },
}

TASK_DESCRIPTION = 'Put appropriate utensils in storage'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--floor-plan', type=int, default=1)
    args = parser.parse_args()
    
    executor = MultiRobotExecutor(base_path)
    executor.assignment = ASSIGNMENT
    executor.parallel_groups = PARALLEL_GROUPS
    
    # Reconstruct subtask_plans
    for sid, data in SUBTASK_PLANS.items():
        executor.subtask_plans[sid] = SubtaskPlan(
            subtask_id=sid,
            subtask_name=data['name'],
            robot_id=data['robot_id'],
            actions=data['actions'],
            parallel_group=data['parallel_group'],
        )
    
    # Execute in AI2-THOR
    executor.execute_in_ai2thor(
        floor_plan=args.floor_plan,
        task_description=TASK_DESCRIPTION if 'TASK_DESCRIPTION' in globals() else None,
        agent_count=AGENT_COUNT,
        spawn_positions=SPAWN_POSITIONS,
    )


if __name__ == '__main__':
    main()