# SupaLove Dashboard - Logic Documentation

## 📋 Application Architecture Overview

The SupaLove Dashboard is a modern database management interface built with Next.js 15, React 19, and TypeScript. The application follows a component-based architecture with clear separation of concerns and modular design.

## 🏗️ Core Application Logic

### **1. Application Entry Point (`src/app/layout.tsx`)**

#### **Purpose**
- Root layout component that wraps all pages
- Manages global application state and providers
- Sets up theming, fonts, and metadata

#### **Key Logic**
```typescript
// Font Loading Logic
const GeistSans = GeistSans({ variable: '--font-geist-sans' })
const GeistMono = GeistMono({ variable: '--font-geist-mono' })

// Theme Provider Setup
<ThemeProvider
  attribute="class"
  defaultTheme="system"
  enableSystem
  disableTransitionOnChange
>
  {children}
</ThemeProvider>
```

**Logic Flow:**
1. Load Geist fonts for consistent typography
2. Configure theme provider with system preference detection
3. Apply global CSS classes and suppress hydration warnings
4. Set up metadata for SEO

---

### **2. Utility Functions (`src/lib/utils.ts`)**

#### **Purpose**
- Provides essential utility functions used throughout the application
- Handles class name merging for styling consistency

#### **Key Logic**
```typescript
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

**Logic Flow:**
1. Accepts multiple class name inputs (strings, arrays, objects)
2. Uses `clsx` to conditionally join classes
3. Uses `twMerge` to resolve Tailwind CSS conflicts
4. Returns optimized class string

---

### **3. Theme Management (`src/components/theme-provider.tsx`)**

#### **Purpose**
- Wraps next-themes provider for consistent theme management
- Enables light/dark mode switching across the application

#### **Key Logic**
```typescript
export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
```

**Logic Flow:**
1. Passes through all next-themes props
2. Enables system theme detection
3. Manages theme state globally
4. Applies theme classes to document element

---

## 🎨 Component Logic Documentation

### **4. MetricCard Component (`src/components/MetricCard.tsx`)**

#### **Purpose**
- Displays key performance indicators with visual feedback
- Shows metrics with trend indicators and animations

#### **State Management**
```typescript
interface MetricCardProps {
  title: string
  value: string | number
  change?: {
    value: number
    label: string
  }
  icon?: React.ReactNode
  className?: string
}
```

#### **Animation Logic**
```typescript
// Entry animation with staggered timing
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.3 }}
>

// Value scale animation
<motion.div
  initial={{ scale: 0.8 }}
  animate={{ scale: 1 }}
  transition={{ delay: 0.2, duration: 0.3 }}
>

// Trend indicator animation
<motion.div
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  transition={{ delay: 0.4 }}
>
```

#### **Conditional Rendering Logic**
```typescript
// Trend color logic
const trendColor = change.value > 0 ? 'text-success' : 'text-destructive'

// Icon container with hover states
<div className={cn(
  "flex h-8 w-8 items-center justify-center rounded-lg",
  "bg-bg-surface-200 group-hover:bg-bg-brand-link/10 transition-colors"
)}>
  {icon}
</div>
```

**Logic Flow:**
1. Receives metric data and optional change indicators
2. Animates entry with staggered timing for visual hierarchy
3. Conditionally renders trend indicators with appropriate colors
4. Applies hover effects for interactivity

---

### **5. ProjectSidebar Component (`src/components/ProjectSidebar.tsx`)**

#### **Purpose**
- Main navigation component with collapsible menu sections
- Handles routing and active state management

#### **State Management**
```typescript
interface SidebarItem {
  title: string
  href: string
  icon: React.ComponentType<{ className?: string }>
  children?: SidebarItem[]
}

const [isOpen, setIsOpen] = useState(false) // For collapsible sections
```

#### **Active State Logic**
```typescript
const pathname = usePathname()
const isActive = pathname === item.href ||
  (hasChildren && item.children?.some(child => pathname === child.href))
```

#### **Animation Logic**
```typescript
// Expandable section animation
<AnimatePresence>
  {isOpen && (
    <motion.div
      initial={{ height: 0, opacity: 0, y: -10 }}
      animate={{ height: 'auto', opacity: 1, y: 0 }}
      exit={{ height: 0, opacity: 0, y: -10 }}
      transition={{ duration: 0.3, ease: 'easeInOut' }}
    >
      {/* Children with staggered animation */}
      {item.children?.map((child, index) => (
        <motion.div
          key={child.href}
          initial={{ opacity: 0, x: -10 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: index * 0.05, duration: 0.2 }}
        >
          <SidebarSection item={child} level={level + 1} />
        </motion.div>
      ))}
    </motion.div>
  )}
</AnimatePresence>
```

#### **Navigation Logic**
```typescript
// Hierarchical navigation with breadcrumbs
const sidebarItems = [
  {
    title: 'Projects',
    href: '/',
    icon: Database,
  },
  {
    title: 'Tables',
    href: '/tables',
    icon: Table,
    children: [
      { title: 'All Tables', href: '/tables', icon: Table },
      { title: 'Create Table', href: '/tables/new', icon: Table },
    ],
  },
  // ... more items
]
```

**Logic Flow:**
1. Renders navigation items with icons and labels
2. Manages collapsible state for items with children
3. Tracks active routes using Next.js pathname hook
4. Applies animations for smooth expand/collapse
5. Handles nested navigation levels

---

### **6. SQLEditor Component (`src/components/SQLEditor.tsx`)**

#### **Purpose**
- Full-featured SQL code editor with Monaco integration
- Query execution, history, and results display

#### **State Management**
```typescript
const [query, setQuery] = useState('SELECT * FROM users LIMIT 10;')
const [results, setResults] = useState<any[]>([])
const [isLoading, setIsLoading] = useState(false)
const [executionTime, setExecutionTime] = useState<number | null>(null)
const [theme, setTheme] = useState<'light' | 'dark'>('light')
const [queryHistory, setQueryHistory] = useState<string[]>([])
const editorRef = useRef<any>(null)
```

#### **Monaco Editor Setup Logic**
```typescript
const handleEditorDidMount = useCallback((editor: any, monaco: Monaco) => {
  editorRef.current = editor

  // SQL syntax highlighting
  monaco.languages.setMonarchTokensProvider('sql', {
    tokenizer: {
      root: [
        [/\b(SELECT|FROM|WHERE|JOIN|INNER|LEFT|RIGHT|OUTER|ON|GROUP|BY|HAVING|ORDER|LIMIT|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER|TABLE|INDEX|VIEW)\b/i, 'keyword'],
        [/\b(INT|VARCHAR|TEXT|DATE|TIMESTAMP|BOOLEAN|DECIMAL)\b/i, 'type'],
        [/".*?"/, 'string'],
        [/'[^']*'/, 'string'],
        [/\d+/, 'number'],
        [/--.*$/, 'comment'],
        [/\*.*?\*/, 'comment'],
      ],
    },
  })

  // Auto-completion provider
  monaco.languages.registerCompletionItemProvider('sql', {
    provideCompletionItems: (model, position) => {
      const suggestions = [
        {
          label: 'SELECT',
          kind: monaco.languages.CompletionItemKind.Keyword,
          insertText: 'SELECT ',
          documentation: 'Select data from a table',
        },
        // ... more suggestions
      ]
      return { suggestions }
    },
  })
}, [])
```

#### **Query Execution Logic**
```typescript
const executeQuery = async () => {
  setIsLoading(true)
  const startTime = Date.now()

  try {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1000))

    // Mock results
    setResults([
      { id: 1, name: 'John Doe', email: 'john@example.com' },
      { id: 2, name: 'Jane Smith', email: 'jane@example.com' },
    ])

    setExecutionTime(Date.now() - startTime)
    setQueryHistory(prev => [query, ...prev.slice(0, 9)]) // Keep last 10 queries
  } catch (error) {
    console.error('Query execution failed:', error)
  } finally {
    setIsLoading(false)
  }
}
```

#### **Results Display Logic**
```typescript
// Conditional rendering based on results
{results.length > 0 && (
  <div className="mt-4">
    <h3 className="text-sm font-medium mb-2 text-typography-body-strong">
      Results ({results.length} rows)
    </h3>
    <div className="border border-border-default rounded-lg overflow-hidden bg-bg-surface-100">
      <table className="w-full">
        <thead className="bg-bg-surface-200 border-b border-border-secondary">
          <tr>
            {Object.keys(results[0]).map((key) => (
              <th key={key} className="px-4 py-3 text-left text-sm font-semibold text-typography-body-strong">
                {key}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="bg-bg-surface-100">
          {results.map((row, index) => (
            <tr key={index} className="border-b border-border-secondary last:border-b-0 hover:bg-bg-surface-75">
              {Object.values(row).map((value, i) => (
                <td key={i} className="px-4 py-3 text-sm text-typography-body">
                  {String(value)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  </div>
)}
```

**Logic Flow:**
1. Initializes Monaco editor with SQL syntax highlighting
2. Registers auto-completion for SQL keywords
3. Manages query state and execution
4. Tracks performance metrics (execution time)
5. Maintains query history
6. Displays results in tabular format
7. Handles theme switching

---

### **7. TableDesigner Component (`src/components/TableDesigner.tsx`)**

#### **Purpose**
- Visual table creation with drag-and-drop column ordering
- Real-time SQL preview and validation

#### **State Management**
```typescript
interface Column {
  id: string
  name: string
  type: string
  nullable: boolean
  default: string
  primaryKey: boolean
}

const [tableName, setTableName] = useState('')
const [columns, setColumns] = useState<Column[]>([
  { id: '1', name: 'id', type: 'SERIAL', nullable: false, default: '', primaryKey: true },
])
const [showPreview, setShowPreview] = useState(false)
```

#### **Drag and Drop Logic**
```typescript
const onDragEnd = useCallback((result: any) => {
  if (!result.destination) return

  const items = Array.from(columns)
  const [reorderedItem] = items.splice(result.source.index, 1)
  items.splice(result.destination.index, 0, reorderedItem)

  setColumns(items)
}, [columns])
```

#### **SQL Generation Logic**
```typescript
const generateSQL = () => {
  const columnDefs = columns.map(col => {
    let def = `"${col.name}" ${col.type}`
    if (!col.nullable) def += ' NOT NULL'
    if (col.default) def += ` DEFAULT ${col.default}`
    if (col.primaryKey) def += ' PRIMARY KEY'
    return def
  }).join(',\n  ')

  return `CREATE TABLE "${tableName}" (\n  ${columnDefs}\n);`
}
```

#### **Column Management Logic**
```typescript
const addColumn = () => {
  const newColumn: Column = {
    id: Date.now().toString(),
    name: '',
    type: 'VARCHAR(255)',
    nullable: true,
    default: '',
    primaryKey: false,
  }
  setColumns([...columns, newColumn])
}

const updateColumn = (id: string, updates: Partial<Column>) => {
  setColumns(columns.map(col => col.id === id ? { ...col, ...updates } : col))
}

const removeColumn = (id: string) => {
  setColumns(columns.filter(col => col.id !== id))
}
```

**Logic Flow:**
1. Manages table schema state with columns array
2. Provides drag-and-drop reordering using @hello-pangea/dnd
3. Generates real-time SQL preview
4. Handles column CRUD operations
5. Validates table name and column configurations

---

## 📄 Page Logic Documentation

### **8. Main Dashboard Page (`src/app/page.tsx`)**

#### **Purpose**
- Central hub displaying overview of projects and key metrics
- Quick access to common actions

#### **Data Structure**
```typescript
const mockProjects = [
  {
    id: '1',
    name: 'E-commerce Database',
    description: 'Main database for the online store',
    createdAt: new Date().toISOString(),
    status: 'Active',
  },
  // ... more projects
]
```

#### **Layout Logic**
```typescript
// Two-column responsive layout for projects and actions
<div className="grid gap-8 lg:grid-cols-2">
  {/* Recent Projects */}
  <div>
    <ProjectList projects={mockProjects} onCreateProject={handleCreate} />
  </div>

  {/* Quick Actions */}
  <div>
    {/* Action cards grid */}
  </div>
</div>
```

**Logic Flow:**
1. Displays welcome header with status indicators
2. Shows key metrics in responsive grid
3. Organizes content in two-column layout
4. Provides quick access to common features

---

### **9. Projects Page (`src/app/projects/page.tsx`)**

#### **Purpose**
- Comprehensive project management interface
- Advanced project metrics and filtering

#### **Metrics Calculation Logic**
```typescript
const totalProjects = mockProjects.length
const activeProjects = mockProjects.filter(p => p.status === 'Active').length
const totalSize = mockProjects.reduce((acc, p) => {
  const size = parseFloat(p.size.split(' ')[0])
  const unit = p.size.split(' ')[1]
  return acc + (unit === 'GB' ? size : size / 1024)
}, 0)
```

**Logic Flow:**
1. Calculates aggregated metrics across all projects
2. Displays project cards with detailed information
3. Provides call-to-action for new project creation

---

### **10. Tables Page (`src/app/tables/page.tsx`)**

#### **Purpose**
- Table browser with filtering and search capabilities
- Comprehensive table management interface

#### **Filtering Logic**
```typescript
interface FilterOption {
  key: string
  label: string
  type: 'text' | 'select'
  options?: string[]
}

const handleFilterChange = (filters: Record<string, any>) => {
  console.log('Filters changed:', filters)
  // Apply filters to table list
}

const handleSearch = (query: string) => {
  console.log('Search query:', query)
  // Apply search to table names and schemas
}
```

#### **Table Display Logic**
```typescript
// Grid layout for table cards
{mockTables.map((table) => (
  <Card key={table.id} className="hover:shadow-lg hover:border-border-secondary transition-all duration-200">
    <CardHeader className="pb-3">
      <CardTitle className="flex items-start justify-between">
        <div className="flex items-center gap-2">
          <TableIcon />
          <div>
            <h3>{table.name}</h3>
            <p className="text-sm text-muted">{table.schema}</p>
          </div>
        </div>
        <DropdownMenu>
          {/* Action menu */}
        </DropdownMenu>
      </CardTitle>
    </CardHeader>
    <CardContent>
      {/* Table metadata display */}
    </CardContent>
  </Card>
))}
```

**Logic Flow:**
1. Displays table metrics in header
2. Implements advanced filtering system
3. Shows tables in card-based grid layout
4. Provides action menus for each table

---

## 🔄 Data Flow & State Management

### **Component Communication**
- **Props-based**: Data flows down through component hierarchy
- **Callback Functions**: Child components communicate changes upward
- **Event Handlers**: User interactions trigger state updates

### **Mock Data Strategy**
- **Static Data**: Currently uses hardcoded mock data
- **API Integration Points**: Functions prepared for backend integration
- **Loading States**: UI components ready for async data loading

### **Error Handling**
- **Try-Catch Blocks**: Error boundaries in async operations
- **Loading States**: Visual feedback during data operations
- **Fallback UI**: Graceful degradation when data is unavailable

## 🎯 Key Design Patterns

### **1. Atomic Design**
- **Atoms**: UI primitives (Button, Input, Icon)
- **Molecules**: Compound components (MetricCard, SidebarItem)
- **Organisms**: Complex sections (Dashboard, TableDesigner)

### **2. Controlled Components**
- **Single Source of Truth**: State managed at component level
- **Predictable Updates**: Controlled form inputs and interactions

### **3. Composition over Inheritance**
- **Component Props**: Flexible component APIs
- **Render Props**: Advanced customization patterns
- **Compound Components**: Related component groups

### **4. Separation of Concerns**
- **Logic vs Presentation**: Clear separation in components
- **Data vs UI**: API logic separated from presentation
- **Reusability**: Components designed for multiple use cases

This comprehensive documentation covers the core logic, data flow, and architectural patterns of the SupaLove Dashboard application. Each component and page has been analyzed for its purpose, state management, and interaction patterns.