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
PARALLEL_GROUPS = {0: [1, 2, 3, 4, 5, 6, 7, 8, 9]}  # group_id -> [subtask_ids]
AGENT_COUNT = 3
SPAWN_POSITIONS = {1: (0.75, 0.900999128818512, -1.5), 2: (2.0, 0.900999128818512, 1.75), 3: (-1.0, 0.900999128818512, 1.0)}  # LP에서 결정된 스폰 좌표

# --- Subtask Plans ---
SUBTASK_PLANS = {
    1: {
        'name': 'subtask_01_Open_Drawer1',
        'robot_id': 1,
        'actions': ['gotoobject robot1 drawer1 (1)', 'openobject robot1 drawer1 (1)'],
        'parallel_group': 0,
    },
    2: {
        'name': 'subtask_02_Open_Drawer2',
        'robot_id': 2,
        'actions': ['gotoobject robot1 drawer2 (1)', 'openobject robot1 drawer2 (1)'],
        'parallel_group': 0,
    },
    3: {
        'name': 'subtask_03_Open_Drawer3',
        'robot_id': 3,
        'actions': ['gotoobject robot1 drawer3 (1)', 'openobject robot1 drawer3 (1)'],
        'parallel_group': 0,
    },
    4: {
        'name': 'subtask_04_Open_Drawer4',
        'robot_id': 1,
        'actions': ['gotoobject robot1 drawer4 (1)', 'openobject robot1 drawer4 (1)'],
        'parallel_group': 0,
    },
    5: {
        'name': 'subtask_05_Open_Drawer5',
        'robot_id': 2,
        'actions': ['gotoobject robot1 drawer5 (1)', 'openobject robot1 drawer5 (1)'],
        'parallel_group': 0,
    },
    6: {
        'name': 'subtask_06_Open_Drawer6',
        'robot_id': 3,
        'actions': ['gotoobject robot1 drawer6 (1)', 'openobject robot1 drawer6 (1)'],
        'parallel_group': 0,
    },
    7: {
        'name': 'subtask_07_Open_Drawer7',
        'robot_id': 1,
        'actions': ['gotoobject robot1 drawer7 (1)', 'openobject robot1 drawer7 (1)'],
        'parallel_group': 0,
    },
    8: {
        'name': 'subtask_08_Open_Drawer8',
        'robot_id': 2,
        'actions': ['gotoobject robot1 drawer8 (1)', 'openobject robot1 drawer8 (1)'],
        'parallel_group': 0,
    },
    9: {
        'name': 'subtask_09_Open_Drawer9',
        'robot_id': 3,
        'actions': ['gotoobject robot1 drawer9 (1)', 'openobject robot1 drawer9 (1)'],
        'parallel_group': 0,
    },
}

TASK_DESCRIPTION = 'Open all the drawers'


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