from enum import Enum


# Создаем Enum с сокращенными именами
class LabelsEnum(Enum):
    U1_QUALITY = "quality"
    U2_ACCESSIBILITY = "accessibility"
    U3_COMPLETENESS = "completeness"
    U4_FAULT_TOLERANCE = "fault tolerance"
    U5_RECOVERABILITY = "recoverability"
    U6_HOPE_ERRORS = "hope errors"
    U7_SYSTEM_FAILURES = "system failures"
    U8_COMPLETENESS_ERRORS = "completeness errors"
    U9_OPERATION_FAILURES = "operation failures"
    U10_OPERATION_SOI_FAILURES = "operation SOI failures"
    U11_DATA_RECOVERY_REQUIREMENTS_ABSENCE = "absence of data recovery requirements"
    U12_HARDWARE_FAILURE_RECOVERY_ERROR = "hardware failure recovery error"
    U13_SOFTWARE_RESTART_RECOVERY_ERROR = "software restart recovery error"
    U14_DATA_CORRUPTION_RECOVERY_ERROR = "data corruption recovery error"
    U15_STANDARDS_NONCOMPLIANCE = "standards noncompliance"
    U16_ERROR_HANDLING_INCOMPLETENESS = "error handling incompleteness"
    U17_DATA_CONSISTENCY_CHECK_INCOMPLETENESS = "data consistency check incompleteness"
    U18_CONTROL_DIAGNOSIS_DEFICIENCY = "control diagnosis deficiency"
    U19_NO_DIAGNOSTIC_MESSAGE = "no diagnostic message"
    U20_DATA_CONSISTENCY_CONTROL_INCOMPLETENESS = "data consistency control incompleteness"


def get_enum_values():
    return [label.value for label in LabelsEnum]
