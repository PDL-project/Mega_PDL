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
ASSIGNMENT = {1: 1, 2: 2}  # subtask_id -> robot_id
PARALLEL_GROUPS = {0: [1, 2]}  # group_id -> [subtask_ids]
AGENT_COUNT = 3
SPAWN_POSITIONS = {1: (-1.25, 0.900999128818512, -0.5), 2: (0.5, 0.900999128818512, -1.75), 3: (2.0, 0.900999128818512, 0.5)}  # LP에서 결정된 스폰 좌표

# --- Subtask Plans ---
SUBTASK_PLANS = {
    1: {
        'name': 'subtask_01_Put_Vase1_on_CounterTop1',
        'robot_id': 1,
        'actions': ['gotoobject robot1 vase1 (1)', 'pickupobject robot1 vase1 shelf1 (1)', 'gotoobject robot1 countertop1 (1)', 'drophandobject robot1 vase1 countertop1 (1)'],
        'parallel_group': 0,
    },
    2: {
        'name': 'subtask_02_Put_Vase2_on_CounterTop2',
        'robot_id': 2,
        'actions': ['gotoobject robot1 vase2 (1)', 'pickupobject robot1 vase2 shelf2 (1)', 'gotoobject robot1 countertop2 (1)', 'drophandobject robot1 vase2 countertop2 (1)'],
        'parallel_group': 0,
    },
}

TASK_DESCRIPTION = 'Put all the vases on the countertop'


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