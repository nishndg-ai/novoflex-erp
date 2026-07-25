import {
  createContext,
  useContext,
  useEffect,
  useState,
  type ReactNode,
} from "react";

import type { RuntimeMetadata } from "../types/runtime";
import { loadRuntime } from "../services/runtimeService";

interface RuntimeContextType {
  runtime: RuntimeMetadata | null;
  loading: boolean;
  error: string | null;
  reload: () => Promise<void>;
}

const RuntimeContext = createContext<RuntimeContextType | undefined>(
  undefined
);

interface RuntimeProviderProps {
  moduleCode: string;
  children: ReactNode;
}

export function RuntimeProvider({
  moduleCode,
  children,
}: RuntimeProviderProps) {
  const [runtime, setRuntime] = useState<RuntimeMetadata | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  async function reload() {
    try {
      setLoading(true);
      setError(null);

      const metadata = await loadRuntime(moduleCode);

      setRuntime(metadata);
    } catch (err) {
      console.error(err);
      setError("Unable to load runtime metadata.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    reload();
  }, [moduleCode]);

  return (
    <RuntimeContext.Provider
      value={{
        runtime,
        loading,
        error,
        reload,
      }}
    >
      {children}
    </RuntimeContext.Provider>
  );
}

export function useRuntime() {
  const context = useContext(RuntimeContext);

  if (!context) {
    throw new Error(
      "useRuntime must be used inside RuntimeProvider."
    );
  }

  return context;
}