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
ASSIGNMENT = {1: 2, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 1}  # subtask_id -> robot_id
PARALLEL_GROUPS = {0: [1, 2, 3, 4, 5, 6, 7, 8, 9]}  # group_id -> [subtask_ids]
AGENT_COUNT = 3
SPAWN_POSITIONS = {1: (0.25, 0.900999128818512, 2.0), 2: (-1.5, 0.900999128818512, 1.75), 3: (0.0, 0.900999128818512, -1.25)}  # LP에서 결정된 스폰 좌표

# --- Subtask Plans ---
SUBTASK_PLANS = {
    1: {
        'name': 'subtask_01_Move_the_Apple_to_the_CounterTop',
        'robot_id': 2,
        'actions': ['gotoobject robot1 apple (1)', 'pickupobject robot1 apple countertop (1)', 'gotoobject robot1 countertop2 (1)', 'drophandobject robot1 apple countertop2 (1)'],
        'parallel_group': 0,
    },
    2: {
        'name': 'subtask_02_Move_the_Bread_to_the_Sink',
        'robot_id': 3,
        'actions': ['gotoobject robot1 bread (1)', 'pickupobject robot1 bread countertop (1)', 'gotoobject robot1 sink (1)', 'drophandobject robot1 bread sink (1)'],
        'parallel_group': 0,
    },
    3: {
        'name': 'subtask_03_Move_the_ButterKnife_to_the_CounterTop',
        'robot_id': 3,
        'actions': ['gotoobject robot1 butterknife (1)', 'pickupobject robot1 butterknife countertop (1)', 'gotoobject robot1 countertop2 (1)', 'drophandobject robot1 butterknife countertop2 (1)'],
        'parallel_group': 0,
    },
    4: {
        'name': 'subtask_04_Move_the_Fork_to_the_CounterTop',
        'robot_id': 3,
        'actions': ['gotoobject robot1 fork (1)', 'pickupobject robot1 fork countertop (1)', 'gotoobject robot1 countertop2 (1)', 'drophandobject robot1 fork countertop2 (1)'],
        'parallel_group': 0,
    },
    5: {
        'name': 'subtask_05_Move_the_Lettuce_to_the_CounterTop',
        'robot_id': 3,
        'actions': ['gotoobject robot1 lettuce (1)', 'pickupobject robot1 lettuce countertop (1)', 'gotoobject robot1 countertop2 (1)', 'drophandobject robot1 lettuce countertop2 (1)'],
        'parallel_group': 0,
    },
    6: {
        'name': 'subtask_06_Move_the_Mug_to_the_CounterTop',
        'robot_id': 3,
        'actions': ['gotoobject robot1 mug (1)', 'pickupobject robot1 mug countertop (1)', 'gotoobject robot1 countertop2 (1)', 'drophandobject robot1 mug countertop2 (1)'],
        'parallel_group': 0,
    },
    7: {
        'name': 'subtask_07_Move_the_Potato_to_the_CounterTop',
        'robot_id': 3,
        'actions': ['gotoobject robot1 potato (1)', 'pickupobject robot1 potato countertop (1)', 'gotoobject robot1 countertop2 (1)', 'drophandobject robot1 potato countertop2 (1)'],
        'parallel_group': 0,
    },
    8: {
        'name': 'subtask_08_Move_the_SoapBottle_to_the_CounterTop',
        'robot_id': 3,
        'actions': ['gotoobject robot1 soapbottle (1)', 'pickupobject robot1 soapbottle countertop (1)', 'gotoobject robot1 countertop2 (1)', 'drophandobject robot1 soapbottle countertop2 (1)'],
        'parallel_group': 0,
    },
    9: {
        'name': 'subtask_09_Move_the_Spatula_to_the_CounterTop',
        'robot_id': 3,
        'actions': ['gotoobject robot1 spatula (1)', 'pickupobject robot1 spatula countertop (1)', 'gotoobject robot1 countertop2 (1)', 'drophandobject robot1 spatula countertop2 (1)'],
        'parallel_group': 0,
    },
    10: {
        'name': 'subtask_10_Move_the_Tomato_to_the_CounterTop',
        'robot_id': 1,
        'actions': [],
        'parallel_group': 0,
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