// app/admin/page.tsx
import { db } from "@/lib/db";
import { site_settings } from "@/lib/db/src/schema/site";
import { eq } from "drizzle-orm";

export default async function AdminPanel() {
  // Veriyi veritabanından çek
  const settings = await db.query.site_settings.findFirst();

  // Veriyi güncelleyen Server Action
  async function saveSettings(formData: FormData) {
    "use server";
    const title = formData.get("title") as string;
    await db.update(site_settings).set({ site_title: title }).where(eq(site_settings.id, 1));
  }

  return (
    <div className="p-8">
      <h1>Siber Asistan Yönetim Paneli</h1>
      <form action={saveSettings}>
        <input name="title" defaultValue={settings?.site_title} className="border" />
        <button type="submit">Güncelle</button>
      </form>
    </div>
  );
}
