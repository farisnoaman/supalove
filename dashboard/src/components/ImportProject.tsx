import { useState } from 'react';
import { Button } from './ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Upload, AlertTriangle, CheckCircle, Loader2, Database } from 'lucide-react';
import { toast } from 'sonner';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';

interface ImportProjectProps {
    projectId: string;
    onSuccess?: () => void;
}

export function ImportProject({ projectId, onSuccess }: ImportProjectProps) {
    const [file, setFile] = useState<File | null>(null);
    const [isUploading, setIsUploading] = useState(false);
    const [result, setResult] = useState<{ status: 'success' | 'warning' | 'error'; message: string; details?: string[] } | null>(null);

    const [migrationFile, setMigrationFile] = useState<File | null>(null);
    const [isMigrationUploading, setIsMigrationUploading] = useState(false);
    const [migrationResult, setMigrationResult] = useState<{ status: 'success' | 'warning' | 'error'; message: string; details?: string[] } | null>(null);

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            setFile(e.target.files[0]);
            setResult(null);
        }
    };

    const handleMigrationFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            setMigrationFile(e.target.files[0]);
            setMigrationResult(null);
        }
    };

    const handleUpload = async () => {
        if (!file) return;

        setIsUploading(true);
        setResult(null);

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/v1/projects/${projectId}/import`, {
                method: 'POST',
                headers: {
                    "Authorization": `Bearer ${localStorage.getItem("token")}`
                },
                body: formData,
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || 'Import failed');
            }

            setResult({
                status: data.status === 'success' ? 'success' : 'warning',
                message: data.message,
                details: data.details
            });

            if (data.status === 'success') {
                toast.success(data.message);
                if (onSuccess) onSuccess();
            } else {
                toast.warning(data.message);
            }

        } catch (error: any) {
            setResult({
                status: 'error',
                message: error.message || "An unexpected error occurred",
            });
            toast.error(error.message);
        } finally {
            setIsUploading(false);
        }
    };

    const handleMigrationUpload = async () => {
        if (!migrationFile) return;

        setIsMigrationUploading(true);
        setMigrationResult(null);

        const formData = new FormData();
        formData.append('file', migrationFile);

        try {
            const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/v1/projects/${projectId}/import-from-migrations`, {
                method: 'POST',
                headers: {
                    "Authorization": `Bearer ${localStorage.getItem("token")}`
                },
                body: formData,
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || 'Migration extraction failed');
            }

            setMigrationResult({
                status: data.status === 'success' ? 'success' : 'warning',
                message: data.message,
                details: data.details
            });

            if (data.status === 'success') {
                toast.success(data.message);
                if (onSuccess) onSuccess();
            } else {
                toast.warning(data.message);
            }

        } catch (error: any) {
            setMigrationResult({
                status: 'error',
                message: error.message || "An unexpected error occurred",
            });
            toast.error(error.message);
        } finally {
            setIsMigrationUploading(false);
        }
    };

    return (
        <div className="space-y-6">
            {/* Standard Import */}
            <Card className="border-dashed border-2">
                <CardHeader>
                    <CardTitle className="flex items-center gap-2">
                        <Upload className="h-5 w-5" />
                        Import Database Backup
                    </CardTitle>
                    <CardDescription>
                        Restore your project from a Supabase backup (.pg, .gz, or .sql).
                        <br />
                        <span className="text-yellow-600 font-semibold">Warning: This will overwrite your current database.</span>
                    </CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                    <div className="grid w-full max-w-sm items-center gap-1.5">
                        <input
                            type="file"
                            accept=".pg,.gz,.sql"
                            onChange={handleFileChange}
                            className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                        />
                    </div>

                    <Button
                        onClick={handleUpload}
                        disabled={!file || isUploading}
                        variant={file ? "default" : "secondary"}
                    >
                        {isUploading ? (
                            <>
                                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                                Restoring...
                            </>
                        ) : (
                            "Start Import"
                        )}
                    </Button>

                    {result && (
                        <Alert variant={result.status === 'error' ? "destructive" : result.status === 'warning' ? "default" : "default"} className={result.status === 'success' ? "border-green-500 bg-green-50 text-green-900" : ""}>
                            {result.status === 'error' && <AlertTriangle className="h-4 w-4" />}
                            {result.status === 'warning' && <AlertTriangle className="h-4 w-4 text-yellow-600" />}
                            {result.status === 'success' && <CheckCircle className="h-4 w-4 text-green-600" />}

                            <AlertTitle>
                                {result.status === 'success' ? "Success" : result.status === 'warning' ? "Completed with Warnings" : "Error"}
                            </AlertTitle>
                            <AlertDescription>
                                {result.message}
                                {result.details && (
                                    <ul className="list-disc pl-4 mt-2 text-xs">
                                        {result.details.map((d, i) => (
                                            <li key={i}>{d}</li>
                                        ))}
                                    </ul>
                                )}
                            </AlertDescription>
                        </Alert>
                    )}
                </CardContent>
            </Card>

            {/* Migration Extraction Import */}
            <Card className="border-dashed border-2 border-blue-300">
                <CardHeader>
                    <CardTitle className="flex items-center gap-2">
                        <Database className="h-5 w-5 text-blue-600" />
                        Import from Inactive Supabase Project
                    </CardTitle>
                    <CardDescription>
                        Extract and import data from migration-based backups (for inactive/deleted Supabase projects).
                        <br />
                        <span className="text-blue-600 font-semibold">Use this if your backup contains migration data instead of plain SQL.</span>
                    </CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                    <div className="grid w-full max-w-sm items-center gap-1.5">
                        <input
                            type="file"
                            accept=".pg,.gz,.sql"
                            onChange={handleMigrationFileChange}
                            className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                        />
                    </div>

                    <Button
                        onClick={handleMigrationUpload}
                        disabled={!migrationFile || isMigrationUploading}
                        variant={migrationFile ? "default" : "secondary"}
                        className="bg-blue-600 hover:bg-blue-700"
                    >
                        {isMigrationUploading ? (
                            <>
                                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                                Extracting Migrations...
                            </>
                        ) : (
                            "Extract & Import Migrations"
                        )}
                    </Button>

                    {migrationResult && (
                        <Alert variant={migrationResult.status === 'error' ? "destructive" : migrationResult.status === 'warning' ? "default" : "default"} className={migrationResult.status === 'success' ? "border-green-500 bg-green-50 text-green-900" : ""}>
                            {migrationResult.status === 'error' && <AlertTriangle className="h-4 w-4" />}
                            {migrationResult.status === 'warning' && <AlertTriangle className="h-4 w-4 text-yellow-600" />}
                            {migrationResult.status === 'success' && <CheckCircle className="h-4 w-4 text-green-600" />}

                            <AlertTitle>
                                {migrationResult.status === 'success' ? "Success" : migrationResult.status === 'warning' ? "Completed with Warnings" : "Error"}
                            </AlertTitle>
                            <AlertDescription>
                                {migrationResult.message}
                                {migrationResult.details && (
                                    <ul className="list-disc pl-4 mt-2 text-xs">
                                        {migrationResult.details.map((d, i) => (
                                            <li key={i}>{d}</li>
                                        ))}
                                    </ul>
                                )}
                            </AlertDescription>
                        </Alert>
                    )}
                </CardContent>
            </Card>
        </div>
    );
}
