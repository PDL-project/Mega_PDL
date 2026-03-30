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
ASSIGNMENT = {1: 1, 2: 2, 3: 3, 4: 1, 5: 2, 6: 3, 7: 1, 8: 2, 9: 3}  # subtask_id -> robot_id
PARALLEL_GROUPS = {1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 6: [6], 7: [7], 8: [8], 9: [9]}  # group_id -> [subtask_ids]
AGENT_COUNT = 3
SPAWN_POSITIONS = {1: (1.5, 0.900999128818512, 2.0), 2: (0.0, 0.900999128818512, -1.75), 3: (-1.0, 0.900999128818512, 0.75)}  # LP에서 결정된 스폰 좌표

# --- Subtask Plans ---
SUBTASK_PLANS = {
    1: {
        'name': 'subtask_01_Close_Cabinet1',
        'robot_id': 1,
        'actions': ['gotoobject robot1 cabinet1 (1)', 'closeobject robot1 cabinet1 (1)'],
        'parallel_group': 1,
    },
    2: {
        'name': 'subtask_02_Close_Cabinet2',
        'robot_id': 2,
        'actions': ['gotoobject robot1 cabinet2 (1)', 'closeobject robot1 cabinet2 (1)'],
        'parallel_group': 2,
    },
    3: {
        'name': 'subtask_03_Close_Cabinet3',
        'robot_id': 3,
        'actions': ['gotoobject robot1 cabinet3 (1)', 'closeobject robot1 cabinet3 (1)'],
        'parallel_group': 3,
    },
    4: {
        'name': 'subtask_04_Close_Cabinet7',
        'robot_id': 1,
        'actions': ['gotoobject robot1 cabinet7 (1)', 'closeobject robot1 cabinet7 (1)'],
        'parallel_group': 4,
    },
    5: {
        'name': 'subtask_05_Close_Cabinet4',
        'robot_id': 2,
        'actions': ['gotoobject robot1 cabinet4 (1)', 'closeobject robot1 cabinet4 (1)'],
        'parallel_group': 5,
    },
    6: {
        'name': 'subtask_06_Close_Cabinet5',
        'robot_id': 3,
        'actions': ['gotoobject robot1 cabinet5 (1)', 'closeobject robot1 cabinet5 (1)'],
        'parallel_group': 6,
    },
    7: {
        'name': 'subtask_07_Close_Cabinet6',
        'robot_id': 1,
        'actions': ['gotoobject robot1 cabinet6 (1)', 'closeobject robot1 cabinet6 (1)'],
        'parallel_group': 7,
    },
    8: {
        'name': 'subtask_08_Close_Cabinet8',
        'robot_id': 2,
        'actions': ['gotoobject robot1 cabinet8 (1)', 'closeobject robot1 cabinet8 (1)'],
        'parallel_group': 8,
    },
    9: {
        'name': 'subtask_09_Close_Cabinet9',
        'robot_id': 3,
        'actions': ['gotoobject robot1 cabinet9 (1)', 'closeobject robot1 cabinet9 (1)'],
        'parallel_group': 9,
    },
}

TASK_DESCRIPTION = 'Close all the cabinets'


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