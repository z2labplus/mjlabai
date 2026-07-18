from __future__ import annotations

from dataclasses import FrozenInstanceError, asdict, replace
import inspect
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.synthetic_policy_table_update_smoke as table_module  # noqa: E402
from mjlabai.rl import (  # noqa: E402
    SYNTHETIC_LOCAL_SOURCE_KIND,
    SYNTHETIC_POLICY_TABLE_UPDATE_SMOKE_VERSION,
    SyntheticPolicyTableEntry,
    SyntheticPolicyTableUpdateResult,
    SyntheticPolicyTableUpdateSmokeError,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateTraceSmokeError,
    apply_synthetic_policy_table_update_smoke,
)


def _record(**overrides: object) -> SyntheticPolicyUpdateInput:
    values: dict[str, object] = {
        "record_id": "p8-table-record:0001",
        "source_kind": SYNTHETIC_LOCAL_SOURCE_KIND,
        "state_id": "synthetic-state:a",
        "action_id": "discard-1m",
        "current_action_value": 2.0,
        "reward": 1.0,
        "next_max_action_value": 4.0,
        "terminal": False,
        "project_authored": True,
        "synthetic": True,
        "local_only": True,
        "uses_real_data": False,
        "uses_external_log": False,
        "uses_platform_data": False,
        "uses_model_output": False,
        "uses_self_play": False,
    }
    values.update(overrides)
    return SyntheticPolicyUpdateInput(**values)  # type: ignore[arg-type]


def _trace() -> tuple[
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
]:
    return (
        _record(),
        _record(
            record_id="p8-table-record:0002",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=10.0,
            reward=2.0,
            next_max_action_value=6.0,
        ),
        _record(
            record_id="p8-table-record:0003",
            current_action_value=3.0,
            reward=5.0,
            next_max_action_value=None,
            terminal=True,
        ),
        _record(
            record_id="p8-table-record:0004",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=8.25,
            reward=4.25,
            next_max_action_value=None,
            terminal=True,
        ),
    )


def _entries() -> tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry]:
    return (
        SyntheticPolicyTableEntry("synthetic-state:a", "discard-1m", 2.0),
        SyntheticPolicyTableEntry("synthetic-state:b", "discard-2p", 10.0),
    )


class SyntheticPolicyTableUpdateSmokeTests(unittest.TestCase):
    def test_exact_initial_and_final_table_values(self) -> None:
        result = apply_synthetic_policy_table_update_smoke(
            _entries(),
            _trace(),
            learning_rate=0.5,
            discount_factor=0.75,
        )

        self.assertIsInstance(result, SyntheticPolicyTableUpdateResult)
        self.assertEqual(
            tuple(entry.action_value for entry in result.initial_entries),
            (2.0, 10.0),
        )
        self.assertEqual(
            tuple(entry.action_value for entry in result.final_entries),
            (4.0, 6.25),
        )
        self.assertEqual(result.trace_result.final_action_values, (4.0, 6.25))

    def test_requires_exact_tuple_shapes_for_both_inputs(self) -> None:
        entries = _entries()
        records = _trace()

        class TupleSubclass(tuple):
            pass

        bad_entry_inputs = (
            list(entries),
            {"entries": entries},
            (entry for entry in entries),
            "two-entries",
            b"two-entries",
            bytearray(b"two-entries"),
            TupleSubclass(entries),
            entries[:1],
            entries + (entries[-1],),
        )
        for value in bad_entry_inputs:
            with self.subTest(entry_input_type=type(value).__name__):
                with self.assertRaises(SyntheticPolicyTableUpdateSmokeError):
                    apply_synthetic_policy_table_update_smoke(  # type: ignore[arg-type]
                        value,
                        records,
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

        bad_trace_inputs = (
            list(records),
            {"records": records},
            (record for record in records),
            "four-records",
            b"four-records",
            bytearray(b"four-records"),
            TupleSubclass(records),
            records[:3],
            records + (records[-1],),
        )
        for value in bad_trace_inputs:
            with self.subTest(trace_input_type=type(value).__name__):
                with self.assertRaises(SyntheticPolicyTableUpdateSmokeError):
                    apply_synthetic_policy_table_update_smoke(  # type: ignore[arg-type]
                        entries,
                        value,
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_requires_exact_entry_type_and_field_types(self) -> None:
        entries = _entries()

        class EntrySubclass(SyntheticPolicyTableEntry):
            pass

        class StrSubclass(str):
            pass

        invalid_entries = (
            (object(), entries[1]),
            (EntrySubclass("synthetic-state:a", "discard-1m", 2.0), entries[1]),
            (replace(entries[0], state_id=StrSubclass("synthetic-state:a")), entries[1]),
            (replace(entries[0], action_id=StrSubclass("discard-1m")), entries[1]),
            (replace(entries[0], action_value=2), entries[1]),
            (replace(entries[0], action_value=True), entries[1]),
            (replace(entries[0], action_value=float("nan")), entries[1]),
            (replace(entries[0], action_value=float("inf")), entries[1]),
        )
        for bad_entries in invalid_entries:
            with self.subTest(bad_type=type(bad_entries[0]).__name__):
                with self.assertRaises(SyntheticPolicyTableUpdateSmokeError):
                    apply_synthetic_policy_table_update_smoke(  # type: ignore[arg-type]
                        bad_entries,
                        _trace(),
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_requires_exact_ab_key_order(self) -> None:
        first, second = _entries()
        cases = (
            (second, first),
            (replace(first, state_id="synthetic-state:c"), second),
            (first, replace(second, action_id="discard-3s")),
            (first, replace(second, state_id=first.state_id, action_id=first.action_id)),
        )
        for bad_entries in cases:
            with self.subTest(bad_entries=bad_entries):
                with self.assertRaisesRegex(
                    SyntheticPolicyTableUpdateSmokeError,
                    "must match trace key",
                ):
                    apply_synthetic_policy_table_update_smoke(
                        bad_entries,
                        _trace(),
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_requires_exact_initial_values_for_both_entries(self) -> None:
        first, second = _entries()
        cases = (
            (replace(first, action_value=2.0000000000000004), second),
            (first, replace(second, action_value=10.000000000000002)),
        )
        for entry_index, bad_entries in enumerate(cases, start=1):
            with self.subTest(entry_index=entry_index):
                with self.assertRaisesRegex(
                    SyntheticPolicyTableUpdateSmokeError,
                    f"entry {entry_index} action_value",
                ):
                    apply_synthetic_policy_table_update_smoke(
                        bad_entries,
                        _trace(),
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_trace_helper_is_reused_once_without_duplicate_formula(self) -> None:
        with patch.object(
            table_module,
            "apply_synthetic_policy_update_trace_smoke",
            wraps=table_module.apply_synthetic_policy_update_trace_smoke,
        ) as trace_helper:
            apply_synthetic_policy_table_update_smoke(
                _entries(),
                _trace(),
                learning_rate=0.5,
                discount_factor=0.75,
            )
        self.assertEqual(trace_helper.call_count, 1)
        source = inspect.getsource(table_module)
        for duplicated_formula in (
            "target_value =",
            "td_error =",
            "updated_action_value =",
        ):
            self.assertNotIn(duplicated_formula, source)

    def test_trace_errors_are_wrapped_with_chained_cause(self) -> None:
        records = _trace()
        bad_records = (replace(records[0], uses_real_data=True),) + records[1:]

        with self.assertRaisesRegex(
            SyntheticPolicyTableUpdateSmokeError,
            "trace update failed",
        ) as context:
            apply_synthetic_policy_table_update_smoke(
                _entries(),
                bad_records,
                learning_rate=0.5,
                discount_factor=0.75,
            )
        self.assertIsInstance(
            context.exception.__cause__,
            SyntheticPolicyUpdateTraceSmokeError,
        )

    def test_repeated_output_is_equal_and_inputs_are_immutable(self) -> None:
        entries = _entries()
        records = _trace()
        before_entries = tuple(asdict(entry) for entry in entries)
        before_records = tuple(asdict(record) for record in records)

        first = apply_synthetic_policy_table_update_smoke(
            entries, records, learning_rate=0.5, discount_factor=0.75
        )
        second = apply_synthetic_policy_table_update_smoke(
            entries, records, learning_rate=0.5, discount_factor=0.75
        )

        self.assertEqual(first, second)
        self.assertEqual(tuple(asdict(entry) for entry in entries), before_entries)
        self.assertEqual(tuple(asdict(record) for record in records), before_records)
        self.assertIsNot(first.initial_entries[0], entries[0])
        with self.assertRaises(FrozenInstanceError):
            entries[0].action_value = 9.0  # type: ignore[misc]

    def test_result_is_frozen_and_has_exact_safe_fields(self) -> None:
        result = apply_synthetic_policy_table_update_smoke(
            _entries(), _trace(), learning_rate=0.5, discount_factor=0.75
        )

        self.assertEqual(
            set(asdict(result)),
            {
                "table_update_version",
                "entry_count",
                "initial_entries",
                "final_entries",
                "trace_result",
                "update_applied",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(
            result.table_update_version,
            SYNTHETIC_POLICY_TABLE_UPDATE_SMOKE_VERSION,
        )
        self.assertEqual(result.entry_count, 2)
        self.assertEqual(len(result.initial_entries), 2)
        self.assertEqual(len(result.final_entries), 2)
        self.assertEqual(
            result.evidence_grade,
            "P8 synthetic/local fixed two-key policy-value table update smoke "
            "evidence only",
        )
        self.assertTrue(result.update_applied)
        self.assertTrue(result.safety_guardrails_all_satisfied)
        warning_text = " ".join(result.warnings).lower()
        for phrase in (
            "synthetic/local fixed two-key policy-value table update smoke only",
            "not a persistent policy, model or checkpoint",
            "not an environment, episode or replay buffer",
            "not self-play",
            "not a variable batch, epoch or production training loop",
            "not model-strength evidence",
            "not stable-dan or luckyj comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)
        with self.assertRaises(FrozenInstanceError):
            result.entry_count = 3  # type: ignore[misc]

    def test_public_imports_are_available_from_rl_package(self) -> None:
        self.assertIs(
            apply_synthetic_policy_table_update_smoke,
            table_module.apply_synthetic_policy_table_update_smoke,
        )
        self.assertIs(
            SyntheticPolicyTableUpdateResult,
            table_module.SyntheticPolicyTableUpdateResult,
        )

    def test_public_surface_is_narrow(self) -> None:
        self.assertEqual(
            set(table_module.__all__),
            {
                "SYNTHETIC_POLICY_TABLE_UPDATE_SMOKE_VERSION",
                "SyntheticPolicyTableEntry",
                "SyntheticPolicyTableUpdateResult",
                "SyntheticPolicyTableUpdateSmokeError",
                "apply_synthetic_policy_table_update_smoke",
            },
        )
        self.assertEqual(
            tuple(
                inspect.signature(
                    apply_synthetic_policy_table_update_smoke
                ).parameters
            ),
            (
                "initial_entries",
                "input_records",
                "learning_rate",
                "discount_factor",
            ),
        )
        public_text = " ".join(table_module.__all__).lower()
        for forbidden in (
            "path",
            "fixture",
            "persistence",
            "environment",
            "episode",
            "replay",
            "self_play",
            "model",
            "optimizer",
            "trainer",
            "training",
        ):
            self.assertNotIn(forbidden, public_text)


if __name__ == "__main__":
    unittest.main()
