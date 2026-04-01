// layouts/MobileLayout.tsx
import { ReactNode } from 'react';

interface MobileLayoutProps {
  children: ReactNode;
}

// voici le layout tout simple du mobile
export default function MobileLayout({ children }: MobileLayoutProps) {
  return (
    <div className="flex flex-col gap-3 p-2 overflow-hidden min-h-screen">
      {children}
    </div>
  );
}