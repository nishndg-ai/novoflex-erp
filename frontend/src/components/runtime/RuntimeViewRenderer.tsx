import FormRenderer from "./FormRenderer";
import GridRenderer from "./GridRenderer";
import DashboardRenderer from "./DashboardRenderer";
import KanbanRenderer from "./KanbanRenderer";
import CalendarRenderer from "./CalendarRenderer";
import ChartRenderer from "./ChartRenderer";
import TimelineRenderer from "./TimelineRenderer";

import type { RuntimeView } from "../../types/runtime";



interface RuntimeViewRendererProps {


  view: RuntimeView;


  moduleCode: string;


  onCreate?: () => void;



  onEdit?: (

    record: Record<string, unknown>

  ) => void;


}





export default function RuntimeViewRenderer({

  view,

  moduleCode,

  onCreate,

  onEdit,

}: RuntimeViewRendererProps) {



  switch (view.view_type.toUpperCase()) {



    case "FORM":


      return (

        <FormRenderer

          view={view}

          moduleCode={moduleCode}

        />

      );





    case "GRID":


      return (

        <GridRenderer

          view={view}

          moduleCode={moduleCode}

          onCreate={onCreate}

          onEdit={onEdit}

        />

      );





    case "DASHBOARD":


      return (

        <DashboardRenderer

          view={view}

        />

      );





    case "KANBAN":


      return (

        <KanbanRenderer

          view={view}

        />

      );





    case "CALENDAR":


      return (

        <CalendarRenderer

          view={view}

        />

      );





    case "CHART":


      return (

        <ChartRenderer

          view={view}

        />

      );





    case "TIMELINE":


      return (

        <TimelineRenderer

          view={view}

        />

      );





    default:


      return (

        <div>

          Unsupported View Type: {view.view_type}

        </div>

      );


  }


}