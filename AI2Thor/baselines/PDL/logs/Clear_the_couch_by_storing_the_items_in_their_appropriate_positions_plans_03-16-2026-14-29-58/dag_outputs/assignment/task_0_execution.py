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
ASSIGNMENT = {1: 4, 2: 3, 3: 1, 4: 2}  # subtask_id -> robot_id
PARALLEL_GROUPS = {0: [1], 1: [2], 2: [3]}  # group_id -> [subtask_ids]
AGENT_COUNT = 5
SPAWN_POSITIONS = {1: (-0.75, 0.9026566743850708, 1.5), 2: (-3.5, 0.9026566743850708, 5.75), 3: (-3.5, 0.9026566743850708, 0.5), 4: (-0.75, 0.9026566743850708, 3.25), 5: (-3.25, 0.9026566743850708, 4.25)}  # LP에서 결정된 스폰 좌표

# --- Subtask Plans ---
SUBTASK_PLANS = {
    1: {
        'name': 'subtask_01_Move_the_KeyChain_to_its_appropriate_position',
        'robot_id': 4,
        'actions': ['gotoobject robot1 keychain (1)', 'pickupobject robot1 keychain sofa (1)', 'gotoobject robot1 sidetable (1)', 'openobject robot1 sidetable (1)', 'drophandobject robot1 keychain sidetable (1)', 'closeobject robot1 sidetable (1)'],
        'parallel_group': 0,
    },
    2: {
        'name': 'subtask_02_Move_the_Pen_to_its_appropriate_position',
        'robot_id': 3,
        'actions': ['gotoobject robot1 pen (1)', 'pickupobject robot1 pen sofa (1)', 'gotoobject robot1 sidetable (1)', 'openobject robot1 sidetable (1)', 'drophandobject robot1 pen sidetable (1)', 'closeobject robot1 sidetable (1)'],
        'parallel_group': 1,
    },
    3: {
        'name': 'subtask_03_Move_the_Pencil_to_its_appropriate_position',
        'robot_id': 1,
        'actions': ['gotoobject robot1 pencil (1)', 'pickupobject robot1 pencil sofa (1)', 'gotoobject robot1 sidetable (1)', 'drophandobject robot1 pencil sidetable (1)'],
        'parallel_group': 2,
    },
    4: {
        'name': 'subtask_04_Move_the_Pillow_to_its_appropriate_position',
        'robot_id': 2,
        'actions': [],
        'parallel_group': 0,
    },
}

TASK_DESCRIPTION = 'Clear the couch by storing the items in their appropriate positions'


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