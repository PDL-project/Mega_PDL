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
ASSIGNMENT = {1: 3, 2: 1, 3: 2, 4: 3, 5: 1}  # subtask_id -> robot_id
PARALLEL_GROUPS = {0: [1, 2, 3], 1: [4], 2: [5]}  # group_id -> [subtask_ids]
AGENT_COUNT = 3
SPAWN_POSITIONS = {1: (0.5, 0.9009992480278015, -0.75), 2: (-2.75, 0.9009992480278015, 2.75), 3: (-0.75, 0.9009992480278015, 0.5)}  # LP에서 결정된 스폰 좌표

# --- Subtask Plans ---
SUBTASK_PLANS = {
    1: {
        'name': 'subtask_01_Slice_the_Lettuce',
        'robot_id': 3,
        'actions': ['gotoobject robot1 fridge (1)', 'openfridge robot1 fridge (1)', 'gotoobject robot1 lettuce (1)', 'sliceobject robot1 lettuce fridge (1)', 'pickupobject robot1 lettuce fridge (1)', 'gotoobject robot1 countertop (1)', 'drophandobject robot1 lettuce countertop (1)'],
        'parallel_group': 0,
    },
    2: {
        'name': 'subtask_02_Slice_the_Tomato',
        'robot_id': 1,
        'actions': ['gotoobject robot1 tomato (1)', 'sliceobject robot1 tomato countertop (1)'],
        'parallel_group': 0,
    },
    3: {
        'name': 'subtask_03_Slice_the_Bread',
        'robot_id': 2,
        'actions': ['gotoobject robot1 bread (1)', 'sliceobject robot1 bread countertop (1)'],
        'parallel_group': 0,
    },
    4: {
        'name': 'subtask_04_Place_Sliced_Vegetables_on_Plate',
        'robot_id': 3,
        'actions': ['gotoobject robot1 lettuce (1)', 'pickupobject robot1 lettuce countertop (1)', 'gotoobject robot1 tomato (1)', 'pickupobject robot1 tomato countertop (1)', 'gotoobject robot1 plate (1)', 'drophandobject robot1 tomato plate (1)', 'drophandobject robot1 lettuce plate (1)'],
        'parallel_group': 1,
    },
    5: {
        'name': 'subtask_05_Store_the_Plate_with_Sliced_Vegetables_in_the_Fridge',
        'robot_id': 1,
        'actions': ['gotoobject robot1 plate (1)', 'pickupobject robot1 plate countertop (1)', 'gotoobject robot1 fridge (1)', 'openfridge robot1 fridge (1)', 'putobjectinfridge robot1 plate fridge (1)', 'closeobject robot1 fridge (1)'],
        'parallel_group': 2,
    },
}

TASK_DESCRIPTION = 'I want to eat a sandwich tomorrow. Please prepare and process the vegetables needed for making the sandwich, place them on a plate, and then store them in the refrigerator for use tomorrow.'


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