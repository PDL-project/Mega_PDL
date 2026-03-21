"""
Checker for 5_tidy_up_livingroom task.

Task: Tidy up the living room by placing all items in their appropriate positions.

Appropriate positions:
    Small items (KeyChain, Pen, Pencil, Watch, RemoteControl, Newspaper) -> Drawer
    Book, Laptop -> DiningTable
    Pillow -> Sofa

Objects per FloorPlan:
    FloorPlan201: KeyChain, Pen, Book, Pencil, Laptop
    FloorPlan202: KeyChain, Watch, Book, RemoteControl, Laptop
    FloorPlan203: RemoteControl, Watch, Book, Pencil, KeyChain
    FloorPlan209: KeyChain, RemoteControl, Newspaper, Book, Watch, Pen, Laptop
    FloorPlan212: Pillow, RemoteControl, Pencil, KeyChain, Pen
"""

from AI2Thor.baselines.utils.checker import BaseChecker


class Checker(BaseChecker):
    def __init__(self) -> None:
        # Small items -> Drawer
        _drawer_items = ['KeyChain', 'Pen', 'Pencil', 'Watch', 'RemoteControl', 'Newspaper']
        # Larger items -> DiningTable
        _table_items = ['Book', 'Laptop']

        independent_subtasks = []
        for item in _drawer_items + _table_items + ['Pillow']:
            independent_subtasks += [
                f'NavigateTo({item})',
                f'PickUpObject({item})',
            ]

        conditional_subtasks = []
        for item in _drawer_items:
            conditional_subtasks += [
                f'NavigateTo(Drawer, {item})',
                f'OpenObject(Drawer, {item})',
                f'PutObject(Drawer, {item})',
            ]
        for item in _table_items:
            conditional_subtasks += [
                f'NavigateTo(DiningTable, {item})',
                f'PutObject(DiningTable, {item})',
            ]
        # Pillow -> Sofa
        conditional_subtasks += [
            'NavigateTo(Sofa, Pillow)',
            'PutObject(Sofa, Pillow)',
        ]

        subtasks = independent_subtasks + conditional_subtasks

        coverage = _drawer_items + _table_items + ['Pillow', 'Drawer', 'DiningTable', 'Sofa']
        interact_objects = _drawer_items + _table_items + ['Pillow']
        interact_receptacles = ['Drawer', 'DiningTable', 'Sofa']

        super().__init__(
            subtasks,
            conditional_subtasks,
            independent_subtasks,
            coverage,
            interact_objects,
            interact_receptacles,
        )
