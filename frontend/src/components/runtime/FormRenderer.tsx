import { useState } from "react";

import type { RuntimeView } from "../../types/runtime";
import DynamicControl from "./DynamicControl";


interface Props {
  view: RuntimeView;
}


export default function FormRenderer({
  view,
}: Props) {

  const [values, setValues] = useState<
    Record<string, unknown>
  >({});


  function handleChange(
    fieldName: string,
    value: unknown
  ) {

    setValues((previous) => ({
      ...previous,
      [fieldName]: value,
    }));

  }


  return (
    <div>

      {view.title && (
        <h2>
          {view.title}
        </h2>
      )}


      <div>

        {view.components
          .filter(
            (component) =>
              component.is_visible
          )
          .sort(
            (a, b) =>
              a.display_order -
              b.display_order
          )
          .map((component) => (

            <div
              key={component.id}
            >

              <DynamicControl
                component={component}
                value={
                  values[
                    component.field_name ?? ""
                  ]
                }
                onChange={
                  (value) =>
                    handleChange(
                      component.field_name ?? "",
                      value
                    )
                }
              />

            </div>

          ))}

      </div>


      <pre>
        {JSON.stringify(
          values,
          null,
          2
        )}
      </pre>

    </div>
  );
}