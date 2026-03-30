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
ASSIGNMENT = {1: 3, 2: 3, 3: 2, 4: 3, 5: 3, 6: 3, 7: 2, 8: 2, 9: 3, 10: 2, 11: 3}  # subtask_id -> robot_id
PARALLEL_GROUPS = {1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 6: [6], 7: [7], 8: [8], 9: [9], 10: [10], 11: [11]}  # group_id -> [subtask_ids]
AGENT_COUNT = 3
SPAWN_POSITIONS = {1: (-1.25, 0.900999128818512, 2.0), 2: (0.75, 0.900999128818512, -1.25), 3: (-1.25, 0.900999128818512, -0.5)}  # LP에서 결정된 스폰 좌표

# --- Subtask Plans ---
SUBTASK_PLANS = {
    1: {
        'name': 'subtask_01_Move_the_Apple_to_the_appropriate_location',
        'robot_id': 3,
        'actions': ['gotoobject robot1 apple (1)', 'pickupobject robot1 apple countertop (1)', 'gotoobject robot1 bowl (1)', 'drophandobject robot1 apple bowl (1)'],
        'parallel_group': 1,
    },
    2: {
        'name': 'subtask_02_Move_the_ButterKnife_to_the_appropriate_location',
        'robot_id': 3,
        'actions': ['gotoobject robot1 butterknife (1)', 'pickupobject robot1 butterknife countertop (1)', 'gotoobject robot1 drawer1 (1)', 'openobject robot1 drawer1 (1)', 'drophandobject robot1 butterknife drawer1 (1)', 'closeobject robot1 drawer1 (1)'],
        'parallel_group': 2,
    },
    3: {
        'name': 'subtask_03_Move_the_Fork_to_the_appropriate_location',
        'robot_id': 2,
        'actions': ['gotoobject robot1 fork (1)', 'pickupobject robot1 fork countertop (1)', 'gotoobject robot1 drawer2 (1)', 'openobject robot1 drawer2 (1)', 'drophandobject robot1 fork drawer2 (1)', 'closeobject robot1 drawer2 (1)'],
        'parallel_group': 3,
    },
    4: {
        'name': 'subtask_04_Move_the_Lettuce_to_the_appropriate_location',
        'robot_id': 3,
        'actions': ['gotoobject robot1 lettuce (1)', 'pickupobject robot1 lettuce countertop (1)', 'gotoobject robot1 fridge (1)', 'openfridge robot1 fridge (1)', 'putobjectinfridge robot1 lettuce fridge (1)'],
        'parallel_group': 4,
    },
    5: {
        'name': 'subtask_05_Move_the_Mug_to_the_appropriate_location',
        'robot_id': 3,
        'actions': ['gotoobject robot1 mug (1)', 'pickupobject robot1 mug countertop (1)', 'gotoobject robot1 cabinet3 (1)', 'openobject robot1 cabinet3 (1)', 'drophandobject robot1 mug cabinet3 (1)', 'closeobject robot1 cabinet3 (1)'],
        'parallel_group': 5,
    },
    6: {
        'name': 'subtask_06_Move_the_PaperTowelRoll_to_the_appropriate_location',
        'robot_id': 3,
        'actions': ['gotoobject robot1 papertowelroll (1)', 'pickupobject robot1 papertowelroll countertop (1)', 'gotoobject robot1 cabinet4 (1)', 'openobject robot1 cabinet4 (1)', 'drophandobject robot1 papertowelroll cabinet4 (1)', 'closeobject robot1 cabinet4 (1)'],
        'parallel_group': 6,
    },
    7: {
        'name': 'subtask_07_Move_the_PepperShaker_to_the_appropriate_location',
        'robot_id': 2,
        'actions': ['gotoobject robot1 peppershaker (1)', 'pickupobject robot1 peppershaker countertop (1)', 'gotoobject robot1 cabinet5 (1)', 'openobject robot1 cabinet5 (1)', 'drophandobject robot1 peppershaker cabinet5 (1)', 'closeobject robot1 cabinet5 (1)'],
        'parallel_group': 7,
    },
    8: {
        'name': 'subtask_08_Move_the_SaltShaker_to_the_appropriate_location',
        'robot_id': 2,
        'actions': ['gotoobject robot1 saltshaker (1)', 'pickupobject robot1 saltshaker countertop (1)', 'gotoobject robot1 cabinet6 (1)', 'openobject robot1 cabinet6 (1)', 'drophandobject robot1 saltshaker cabinet6 (1)', 'closeobject robot1 cabinet6 (1)'],
        'parallel_group': 8,
    },
    9: {
        'name': 'subtask_09_Move_the_SoapBottle_to_the_appropriate_location',
        'robot_id': 3,
        'actions': ['gotoobject robot1 soapbottle (1)', 'pickupobject robot1 soapbottle countertop (1)', 'gotoobject robot1 sink (1)', 'drophandobject robot1 soapbottle sink (1)'],
        'parallel_group': 9,
    },
    10: {
        'name': 'subtask_10_Move_the_Spatula_to_the_appropriate_location',
        'robot_id': 2,
        'actions': ['gotoobject robot1 spatula (1)', 'pickupobject robot1 spatula countertop (1)', 'gotoobject robot1 drawer3 (1)', 'openobject robot1 drawer3 (1)', 'drophandobject robot1 spatula drawer3 (1)', 'closeobject robot1 drawer3 (1)'],
        'parallel_group': 10,
    },
    11: {
        'name': 'subtask_11_Move_the_Tomato_to_the_appropriate_location',
        'robot_id': 3,
        'actions': ['gotoobject robot1 tomato (1)', 'pickupobject robot1 tomato countertop (1)', 'gotoobject robot1 fridge (1)', 'openfridge robot1 fridge (1)', 'putobjectinfridge robot1 tomato fridge (1)'],
        'parallel_group': 11,
    },
}

TASK_DESCRIPTION = 'Clear the central countertop by placing items in their appropriate positions'


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