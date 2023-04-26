import os
import sys
from typing import Any, Dict, List, Optional, Tuple, TypedDict

import govuk_frontend_jinja
import requests
import yaml

from govuk_frontend_django import components

if not len(sys.argv) > 1:
    raise Exception("Please provide a GOV>UK Frontend version e.g. v4.6.0")

GOVUK_FRONTEND_VERSION = sys.argv[1]

jinja_path = govuk_frontend_jinja.__path__[0]
govuk_frontend_path = components.__path__[0]

# Code to generate GOV.UK Design System components

python_imports = """
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List

from govuk_frontend_django.components import base as govuk_frontend_base
from govuk_frontend_django.components import error_message as govuk_frontend_error_message
from govuk_frontend_django.components import fieldset as govuk_frontend_fieldset
from govuk_frontend_django.components import hint as govuk_frontend_hint
from govuk_frontend_django.components import label as govuk_frontend_label
from govuk_frontend_django.components import tag as govuk_frontend_tag

"""

subdataclass_python = """
@dataclass(kw_only=True)
class {subcomponent_class_name}:
    {subcomponent_types}
"""

base_component_dataclass_python = '''
@dataclass(kw_only=True)
class {COMPONENT_DATACLASS_PREFIX}{component_class_name}(govuk_frontend_base.GovUKComponent):
    """GOV.UK {component_name}

    See: {gds_url}
    """

    {component_types}

    _jinja2_template = "govuk_frontend_jinja/components/{component_hyphenated}/macro.html"
    _macro_name = "govuk{component_class_name}"


COMPONENT = {COMPONENT_DATACLASS_PREFIX}{component_class_name}
'''

COMPONENT_DATACLASS_PREFIX = "GovUK"

IGNORE = "_IGNORE_"

TYPE_MAPPING = {
    "string": "str",
    "integer": "int",
    "boolean": "bool",
    "html": "str",
}
NAME_TYPE_MAPPING = {
    "formGroup": "govuk_frontend_base.FormGroup",
    "errorMessage": "govuk_frontend_error_message.GovUKErrorMessage",
    "hint": "govuk_frontend_hint.GovUKHint",
    "fieldset": "govuk_frontend_fieldset.GovUKFieldset",
    "attributes": "govuk_frontend_base.Attributes",
    "label": "govuk_frontend_label.GovUKLabel",
}

DATACLASS_TYPE_MAPPING: Dict[str, Dict[str, Tuple[str, bool]]] = {
    "Fieldset": {
        "legend": ("govuk_frontend_base.FieldsetLegend", False),
    },
    "Accordion": {
        "items": ("List[govuk_frontend_base.AccordionItem]", False),
    },
    "SummaryList": {
        "rows": ("govuk_frontend_base.SummaryListRows", False),
    },
    "Checkboxes": {
        "values": ("List[str]", False),
    },
    "CheckboxesItems": {
        "conditional": ("govuk_frontend_base.CheckboxesConditional", False),
        "conditional.html": (IGNORE, False),
    },
    "Details": {
        "summaryText": ("Optional[str] = None", False),
        "summaryHtml": ("Optional[str] = None", False),
    },
    "ErrorSummary": {
        "titleText": ("Optional[str] = None", False),
        "titleHtml": ("Optional[str] = None", False),
    },
    "Panel": {
        "titleText": ("Optional[str] = None", False),
        "titleHtml": ("Optional[str] = None", False),
    },
    "Table": {
        "rows": ("arrayofarrays", True),
    },
    "TabsItems": {
        "panel": ("govuk_frontend_base.TextAndHtml", False),
    },
    "PhaseBanner": {
        "tag": ("govuk_frontend_tag.GovUKTag", False),
    },
}


class ComponentParams(TypedDict):
    name: str
    type: str
    required: bool
    YAML: dict


def build_dataclasses_from_component_yaml(
    component_hyphenated: str, version: Optional[str] = None
) -> dict:
    branch_or_tag = version or "main"
    govuk_frontend_component_yml_url = f"https://raw.githubusercontent.com/alphagov/govuk-frontend/{branch_or_tag}/src/govuk/components/{component_hyphenated}/{component_hyphenated}.yaml"
    # Grab the YAML file
    r = requests.get(govuk_frontend_component_yml_url)
    r.raise_for_status()
    component_yaml = yaml.safe_load(r.text)

    def convert_yaml_params_to_component_params(
        yaml_params: List[Dict[Any, Any]]
    ) -> List[ComponentParams]:
        components_params: List[ComponentParams] = [
            {
                "name": param["name"],
                "type": param["type"],
                "required": param["required"],
                "YAML": param,
            }
            for param in yaml_params
        ]
        return components_params

    component_params = convert_yaml_params_to_component_params(
        yaml_params=component_yaml["params"],
    )

    dataclasses = {}
    dataclass_name = "".join(
        [word.capitalize() for word in component_hyphenated.split("-")]
    )

    def build_dataclass(
        dataclass_name: str,
        component_params: List[ComponentParams],
        is_base: bool = False,
    ):
        dataclasses[dataclass_name] = {}

        param_list = [param["name"] for param in component_params]

        has_text_and_html: bool = "text" in param_list and "html" in param_list

        for component_param in component_params:
            dataclass_field = False
            dataclass_type = ""
            dataclass_value = ""

            if component_param["type"] == "nunjucks-block":
                continue
            if component_param["name"] in ["attributes", "classes"] and is_base:
                continue
            if component_param["name"] in ["text", "html"] and has_text_and_html:
                component_param["required"] = False
            if component_param["name"] == "for":
                dataclass_field = True

            if not component_param["required"]:
                dataclass_value = "None"
                dataclass_type += "Optional["

            HAS_BEEN_MAPPED = False

            mapped_type = TYPE_MAPPING.get(component_param["type"], "Any")
            if mapped_type == "Any":
                print(f'No mapping for: {dataclass_name} {component_param["type"]}')
            else:
                HAS_BEEN_MAPPED = True

            # Fix text and html typing as only one is required, not both.
            if component_param["name"] in ["text", "html"] and has_text_and_html:
                HAS_BEEN_MAPPED = True
                mapped_type = "str"

            # Override types with the defined name mappings.
            name_type_mapping = NAME_TYPE_MAPPING.get(component_param["name"])
            if name_type_mapping:
                HAS_BEEN_MAPPED = True
                mapped_type = name_type_mapping

            # Up to this point, if the type has been mapped, we don't need to
            # generate it's sub dataclass.
            GENERATE_SUB_DATACLASS = not HAS_BEEN_MAPPED

            # Override types with the defined dataclass mappings.
            dataclass_type_mapping = DATACLASS_TYPE_MAPPING.get(dataclass_name)
            if dataclass_type_mapping:
                if component_param["name"] in dataclass_type_mapping:
                    GENERATE_SUB_DATACLASS = dataclass_type_mapping[
                        component_param["name"]
                    ][1]
                    mapped_type = dataclass_type_mapping[component_param["name"]][0]

            if mapped_type == IGNORE:
                continue

            sub_params = component_param["YAML"].get("params", [])
            if sub_params and GENERATE_SUB_DATACLASS:
                sub_dataclass_name = (
                    dataclass_name + component_param["name"].capitalize()
                )
                subcomponent_params = convert_yaml_params_to_component_params(
                    yaml_params=sub_params,
                )
                if subcomponent_params:
                    build_dataclass(
                        dataclass_name=sub_dataclass_name,
                        component_params=subcomponent_params,
                    )
                    if mapped_type == "arrayofarrays":
                        dataclass_type += f"List[List[{sub_dataclass_name}]]"
                    elif component_param["type"] == "array":
                        dataclass_type += f"List[{sub_dataclass_name}]"
                    else:
                        dataclass_type += sub_dataclass_name
            else:
                dataclass_type += mapped_type

            if not component_param["required"]:
                dataclass_type += "]"

            if dataclass_field:
                old_name = component_param["name"]
                component_param["name"] = "_" + old_name
                dataclass_value = (
                    'field(default=None, metadata={"name": "' + old_name + '"})'
                )

            type_and_value = dataclass_type
            if dataclass_value:
                type_and_value += f" = {dataclass_value}"

            dataclasses[dataclass_name][component_param["name"]] = type_and_value

    build_dataclass(
        dataclass_name=dataclass_name,
        component_params=component_params,
        is_base=True,
    )

    return dataclasses


def build_component(component_hyphenated: str, version: Optional[str] = None):
    """Generate Python code for each component

    e.g. "govuk_frontend_jinja/components/accordion/macro.html" -> "govuk_frontend_django/components/accordion.py"
    """

    component_underscored = component_hyphenated.replace("-", "_")
    filename = govuk_frontend_path + f"/{component_underscored}.py"

    # Check if file already exists. If it does, don't overwrite it.
    if os.path.exists(filename):
        print(f"Skipping {filename} as it already exists")
        return None

    component_name = " ".join(
        [word.capitalize() for word in component_hyphenated.split("-")]
    )
    component_class_name = "".join(
        [word.capitalize() for word in component_hyphenated.split("-")]
    )

    print(
        f"Generating {component_class_name} {component_hyphenated} {component_underscored}"
    )

    gds_url = f"https://design-system.service.gov.uk/components/{component_hyphenated}/"

    dataclasses = build_dataclasses_from_component_yaml(
        component_hyphenated=component_hyphenated,
        version=version,
    )

    with open(filename, "w") as f:
        f.write(python_imports)

        # Reverse the order of dataclasses to fix typing order
        dataclasses_reversed = reversed(list(dataclasses.items()))

        for dataclass_name, dataclass_params in dataclasses_reversed:
            if dataclass_name == component_class_name:
                continue
            f.write(
                subdataclass_python.format(
                    subcomponent_class_name=dataclass_name,
                    subcomponent_types="\n    ".join(
                        [
                            f"{param_name}: {param_type}"
                            for param_name, param_type in dataclass_params.items()
                        ]
                    ),
                )
            )

        f.write(
            base_component_dataclass_python.format(
                COMPONENT_DATACLASS_PREFIX=COMPONENT_DATACLASS_PREFIX,
                component_name=component_name,
                component_class_name=component_class_name,
                component_hyphenated=component_hyphenated,
                gds_url=gds_url,
                component_types="\n    ".join(
                    [
                        f"{param_name}: {param_type}"
                        for param_name, param_type in dataclasses[
                            component_class_name
                        ].items()
                    ]
                ),
            )
        )


# Loop over directories in "govuk_frontend_jinja/components/" where "govuk_frontend_jinja" is a python package
# and generate Python code for each component


for component_hyphenated in os.listdir(jinja_path + "/templates/components"):
    build_component(component_hyphenated, version=GOVUK_FRONTEND_VERSION)
