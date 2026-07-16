<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/mLC_630DHN-JocXJqz1ABc6zCtaZVenjDtMtdD8No_duszCrQ1FMpQcbwZHvt951qpOdzPfDVIJLak0WdZaMER7cYnFsWWoWFzaIp0xQ3wrTMc0Yxhh3GgBWil3JjEGHr-rbo3v5luwUA8eEItZVw4eakrotX9QwKRsL_TcbxyMlnH7ahu2XZJ2G7Pkn_Hb_mX6UzGpIuRXoiuVtVuL9SkeUkAuodHHMByn0ZwgBEg_cLqUutH0HNnHIdSkEGnRKbZ783KuKcnrKf5c7nC8toblqC22xdILQ4d0B53TThOH2VcsK3kcdaNGsymckNICf6Mj8cbuD0jb6xW3_b2qRVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.81K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 18:00:25</div>
<hr>

<div class="tg-post" id="msg-7028">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOi75oA2xZ0aauK6_uXX-wINurwcCDtIroERhpM_NoqThIukmSc6DlGunuVLSbm00NyyofUsm7_VlB-RJ5_dPlcDbue_T_lCBpmlBTIzSzDwLV_M12CD_vXx3okFO3yobUfYXXVTYFgBuZulp-PclMNiMaAwBUdhxF0i9hcdRdJbH1rUV2712PCSeP7TFDYD5YkX64rh6hecF--_rfkFKY4YNPGfccxcn_uq1c1a9DYBR6VsJAyCqF46ONI9zrQHIgMI7uGPh1WwXyiCuK_Y9OF9zBvjrUl-ycYZa0v5Q9vZYILH43neXTopkbp0Q6uWicKwbJ5YWBPw9Tc7ka0EfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFZYh1JWMtA6nIf3Megw9yA1oPgrj4f1z8YTQlrrYHCWFw2IbUqkY9m-uVahSTD61f-tI92C_6SDYNUHGuDsFy7cb46dz09IzXmhIVRc2E9JvxGCJNWDiRfhzwPMf8gEMS2OaBNPLwsT-EpogV7JZGBctQYfP8lt0bTwSbgH56ocKmDPjBLSxqMuBWDROlrhiuf_9Sm8z-s0uZm3_ATHHRCFY19u7MKw9NSWSrr92fgfofD8gBo4ei5br8FsBPKuC6FHbQrliRYAjtx1ScAQZHzCdGzRzujr6Dxr9801xXFNN7YCxLXog3ypHcyjuMRo9GvSDiiMbM6CR6nW_zNOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYDawdA801nKmSzApIN3bQI4OoNxeGm2sOR5f_LbHJKg-STaLwzWQ5RPrOK1Pu4ChtM4lXskEil6kYnfLpxPA0VKE2ytVvH-8nuQmgCOe6JlpFTFY_kYA8fLj3o0nQbrgAGhfYKZkk5fOjyr3fwmlUi_6yV5_NqcmbTRtWTArD8BAOgtWGI8cIliWaVb-A0heQGPTD0OUnsaxkuwsRC0_G_cbwyAfeGham67pv5oB-rUkXYigdVuEdXLMnS6TSqfV1v9CB-ra8_QLPO6zBhN10aO0QHmf-LMoapfIsyVfwd4zifS7qhqiQ3-LK4xGPsHL6D7ihEsvjbMIhE-TEmsnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
مجموعه‌ای از پرامپت‌های متنی، تصویری و ویدیویی رایگان و قابل کپی برای مدل‌های هوش مصنوعی مانند ChatGPT، Claude، Gemini، Nano Banana و Veo که امکان فیلتر کردن بر اساس نوع، مدل، دسته‌بندی و امتیاز وجود داره.
🌐
https://freeprompts.io/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 397 · <a href="https://t.me/ArchiveTell/7028" target="_blank">📅 17:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7027">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McBmPTcM3utv7xc1XU8EIJPm3aN39DCED9HKsiyaPwoxN_-5WWO1RKps5w0SMiJrkp3pxEVO6LixAYsC9gPzP8oZJlfgAsodPMmNgDDvHfoAzv8tjxn74aoVkuFYoS0Y19lEz1bZpv1k3BvnBVOIgdXiVJGAyOAn6EuJdow6f6FjXrdlTsXJU4ho6GnF4wWuwGUWlJMfkCeXhnRmDPGqT_fIWnTGyroDqOrvELVEUb9lW0wFUjW0H1NMKdZQY98jRBBThJttBBSngUBL13C9qcU32ry4ZY4YJy0NCwQI-EATG09-ch5sLfsK7-yknkEJJsaU1H29MwmRmhhJ-y5ICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛠
استفاده از Claude Code با مدل‌های رایگان و لوکال
محیط Claude Code عالیست اما استفاده از API آن پرهزینه‌ست. ابزار
Free Claude Code
یک پروکسی هوشمند است که اجازه می‌دهد این محیط ترمینالی را به هر مدل دلخواهی متصل کنید.
✨
ویژگی‌های اصلی:
🔸
پشتیبانی وسیع:
اتصال بی‌دردسر به API سرویس‌هایی مثل DeepSeek، Gemini و OpenRouter.
🔸
اجرای آفلاین:
پشتیبانی از Ollama و LM Studio برای کدنویسی کاملاً رایگان با مدل‌های لوکال.
🔸
پنل مدیریت (Admin UI):
رابط کاربری تحت وب ساده برای تنظیم سریع کلیدهای API و تغییر مدل‌ها.
🔸
مسیریابی هوشمند:
امکان تخصیص مدل‌های سبک برای وظایف ساده و مدل‌های قدرتمند برای پردازش‌های پیچیده.
این ابزار روی ویندوز، مک و لینوکس به‌راحتی نصب می‌شود.
📥
سورس‌کد و آموزش نصب در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 487 · <a href="https://t.me/ArchiveTell/7027" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7026">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHfZgKNuh1TaXI-Zj14uOJXFbDucqDjdQPfa3T28jUEd3w8MenFDCXCsZRqHWVpr82T1EsluC2KXVXCI6KiWkp6uzAOmw_hy9C3s4saDSJsf2v0Xy3P9VP664XtaeQ1IHQhO26505rzvtv4Smu4ITc-zv33JFV5o2XW1WwN78xixdQknCLd3JizeEYFlgLtdV5zVmk7yAapqzQzxD7_zG8AB_w_iwMu8ANnoVtRh54ZWlvxgc4MOSwoxr0mtRX2XDDmCxwWLFDf1nXwR9h0BQxJX89veMNkIqYI6RIkfWDl0gubjpqHhTQvOvEe875IP4KdUuv_g2n7UnItav6yGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
معرفی و آموزش راه‌اندازی UAC SNI Spoofer برای ویندوز
یه کلاینت متن‌باز، سبک و دو زبانه (فارسی/انگلیسی) که با متد SNI Spoofing و هسته Xray کار می‌کنه. تو آپدیت جدید فایل‌های پروژه،
آموزش ساده و قدم‌به‌قدم راه‌اندازی
هم قرار گرفته تا خیلی راحت‌تر بتونید وصل بشید.
✨
ویژگی‌های کلیدی تو چند خط:
🔸
پروفایل اختصاصی اپراتورها:
تنظیمات کاملاً مجزا و بهینه‌شده برای همراه اول و ایرانسل (بدون تداخل با هم).
🔸
اسکنر هوشمند:
تست زنده و پیدا کردن خودکار سریع‌ترین SNI و مسیر.
🔸
مدیریت بی‌دردسر پروکسی:
ست کردن خودکار پروکسی ویندوز و بازگردانی امن اون بعد از بستن برنامه.
🔸
بهینه‌ساز یوتیوب:
استارت سریع‌تر و روان‌تر ویدیوها با قابلیت گرم‌سازی مسیر.
🔸
نسخه پرتابل:
اجرای مستقیم بدون نیاز به نصب پایتون (فقط کافیه فایل ZIP رو دانلود و اکسترکت کنید).
📥
دانلود نسخه پرتابل و مشاهده آموزش راه‌اندازی
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/ArchiveTell/7026" target="_blank">📅 15:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7025">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBreak The Barriers</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3X-UI-MANUAL.fa.pdf</div>
  <div class="tg-doc-extra">3.8 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7025" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دفترچه راهنمای کاربری پنل 3X-UI ثنایی به زبان فارسی
✔️
راهنمای جامع پنل 3X-UI ثنایی که برای نسخه‌ی 3.5.0 نوشته شده است.
منبع:
https://github.com/yukh975/3X-UI-Manual
@break_the_barriers
💎</div>
<div class="tg-footer">👁️ 727 · <a href="https://t.me/ArchiveTell/7025" target="_blank">📅 15:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7024">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Doz8FEKpnFVaqxrc4L0Gna40HF-Rynz8MDsXyHihuRw6J2lq4e2WXohRbF2Q2Dkz-AlpWC4AbYv-2YdYYObL4GTj_gn-QSkTHoa5Y0scDxIQmPsZGMMBXui-19--M4mgKXvMJrCTeKoentMuXbKckvYDhSwsHAhwpM0Ff_q-cHRZkNEgOuUEkXq3_43DyFjA1VO6GXlYtmEswr732fNYRBlG5VRTQOD8uf-ofEoYajiAUiENa07zOCWCqGYHpp6RZMIjf4F3e00BYbaHaH8un8YYJJC-l2SAYKrLvvqM2jIdeGJ_V717ZbtZ-ajPT2mqWaG7TSPhwt8iUpbFcSfabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
؛OpenAI قابلیت جستجو در ChatGPT رو اضافه کرد که به طور همزمان در چت‌ها، پروژه‌ها، تصاویر و اسناد جستجو میکنه.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/ArchiveTell/7024" target="_blank">📅 14:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7023">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📱
معرفی Hermex؛ کنترل کامل هوش مصنوعی اختصاصی از روی آیفون  اگر با پروژه متن‌باز hermes-webui یک دستیار هوشمند اختصاصی روی سرور خودتون راه‌اندازی کردید، حالا می‌تونید با اپلیکیشن بومی Hermex، کنترل کامل اون رو روی گوشی آیفون خودتون در دست بگیرید. این برنامه…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/7023" target="_blank">📅 13:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7022">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📱
معرفی Hermex؛ کنترل کامل هوش مصنوعی اختصاصی از روی آیفون
اگر با پروژه متن‌باز hermes-webui یک دستیار هوشمند اختصاصی روی سرور خودتون راه‌اندازی کردید، حالا می‌تونید با اپلیکیشن بومی
Hermex
، کنترل کامل اون رو روی گوشی آیفون خودتون در دست بگیرید.
این برنامه کاملاً رایگان است و هیچ اطلاعاتی رو برای سرورهای واسطه ارسال نمی‌کنه؛ یعنی گوشی شما فقط نقش یک «ریموت کنترل» رو بازی می‌کنه و تمام داده‌ها و پردازش‌ها روی سرور امن خودتون باقی می‌مونه.
✨
ویژگی‌های کلیدی اپلیکیشن:
🔸
رابط کاربری بومی (Native):
ساخته‌شده با SwiftUI (مخصوص iOS 18 به بالا) با طراحی بسیار روان، بدون نیاز به واسطه‌های وب.
🔸
چت زنده و هوشمند:
ارتباط در لحظه با دستیار هوشمند، امکان ارسال فایل و عکس، و مشاهده روند استدلال و تفکر مدل.
🔸
مدیریت همه‌جانبه:
قابلیت مدیریت تسک‌ها (Cron jobs)، مشاهده مهارت‌های نصب‌شده (Skills)، ابزارهای آنالیز و بررسی حافظه مدل.
🔸
شخصی‌سازی کانکشن:
امکان اتصال به سرور از طریق HTTPS، پراکسی معکوس (Reverse Proxy) یا شبکه‌های امنی مثل Tailscale.
🔸
بدون هزینه پنهان:
فاقد هرگونه تبلیغات، سیستم ردیابی (Tracking) یا پرداخت درون‌برنامه‌ای.
📥
دانلود و اطلاعات بیشتر:
لینک نصب از App Store
(یا جستجوی Hermex)
🔗
سورس کد پروژه در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/7022" target="_blank">📅 13:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7021">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjrmkLJ8pqkzPMzQqu2LhMwwuK1J8GdMbmW_GoASdXwWWZIcKQMCW8ASpuXzp4-GeUEgI7z_9-icYXt68lgcs71Wnh-RZplLCXjHAZpZDNT6xg3DgVgJTnjQ9peqAitIhy3ipWOcc5LEfUbyouoarD_ga8jvPpQHdmvS38e_S_7-wBNMubA2yICFafAd2g-xg3wwEpp7hH7AXiZeWUiVgHhG7DsKd9OzrwSEwiXcBRPFq1UaT_0T1Rw9ubN0aeHkmCVl2akC4q1IcTchPxmw-nQdj6Koj3a8lDnbohjlpCJ05rSq2fiqloUkxBYbPotITs4DE1FdVdRzrlxDgSDJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 977 · <a href="https://t.me/ArchiveTell/7021" target="_blank">📅 13:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7019">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqxfqi-L6iUiMJG6xnXou321S92Jkjuo7thgQzJuAmryxD3nDj1lbb1T6fbvWrVeAbEFOxq_3DQwtkkM1sy96FAcUVofQpGKjqxvltNgtqEuciL2AkDXoOA7xCqLWMEcdRvq549x0_L1gtDT8PZFp9Pdeg3yESexi6nn_azfZbn96C_mS4e-nfS2imslYuwqUoHUFrnx9r7jqPAklU6_7ifwKPfQcKJg_kfMjZ4UOzmNmBpYzhgeJaaaX9uxaechttyhfQZZKRjpTx_fUj0KhHVaOhoTPTXa2VC5qGXvqQJyPs5JjyMiP4Yja4Ro8IA55Y5i2DmwY81CWIAwHmAI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RohanKar Launcher
🎮
یک لانچر دسکتاپ برای اجرای مجموعه‌ای از بازی‌های کلاسیک
PC
که روی
Archive.org
منتشر شده‌اند. با این ابزار می‌توانید بازی‌ها را از طریق یک رابط کاربری یکپارچه مرور، دانلود، نصب و اجرا کنید؛ بدون اینکه نیازی به ساخت حساب کاربری داشته باشید
👤
مناسب برای علاقه‌مندان به بازی‌های کلاسیک که به دنبال دسترسی ساده و سریع به آرشیو بزرگی از عناوین قدیمی هستند
🎮
Github
🐱
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7019" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7018">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNkzUHIgAcM6kTV_xkOF5s-NkjKJoI7ddXveJe7dW778s2Hh_RpGV8_wgl_4Vc4NiUDcoa55nbyHF3ri9uxglsALk1bAUIfPmjgyGZqy3iD0tFxtY_B5itYdoL4WIjrJbf3Pb7uG1i4QOeH8S0SQtTZOUZvctmTwQ6FjpgfHSJ364hj-nd5rvGtnAlqBlxsjmGhqSceGH3HCTveUgeNNgafbg37kSmR6DxMsa3jFDgGLv7Cm6PBtVRmlqhOIEb3IkVPnA3R-GVTn3pUM945OENUSShEGgoc2etzERVMABOREY_zrDJUyIQjEJqZqIyT9QNy0_OU7rVgUPkH4AY8V3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
هوش مصنوعی برنامه‌نویس Grok Build متن‌باز شد!
شرکت SpaceXAI دستیار قدرتمند
Grok Build
رو در گیت‌هاب منتشر کرد. این ایجنت (Agent) هوشمند مستقیماً تو محیط ترمینال اجرا می‌شه و مثل یک برنامه‌نویس کنارتون کار می‌کنه.
✨
ویژگی‌های کلیدی تو چند خط:
🔸
همه‌فن‌حریف:
درک عمیق سورس‌کدها، ویرایش خودکار فایل‌ها، اجرای دستورات (Shell) و سرچ در وب.
🔸
انعطاف‌پذیر:
دارای رابط کاربری تمام‌صفحه ترمینالی (TUI)، قابل اجرا در اسکریپت‌ها (Headless) و اتصال به ادیتورها.
🔸
سبک و سریع:
نوشته‌شده با زبان قدرتمند Rust (دارای نسخه آماده برای ویندوز، مک و لینوکس).
🔸
متن‌بازِ یک‌طرفه:
کدها کاملاً در دسترس هستن (لایسنس Apache 2.0)، اما فعلاً مشارکت و ارسال کد (Pull Request) از سمت برنامه‌نویس‌های خارجی پذیرفته نمی‌شه.
📥
سورس‌کد و دستورات نصب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7018" target="_blank">📅 11:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7017">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8Hv9EJGoNfSyzf_2Hy8CI-068CYSMjtfHk1TgJVjpv19FNRHyTY-J4uIVHOhdcJdqz6OjvRiswwv3xRAoVs3PSeE5Sa7U9lO2pf9NDp3TDmuw33i7VPIHsSFfgssSlfbeVExc7Wb0N6KKu1Te8qCiUfFWIAGcUYgCR7RUXOyRt-Sy5zKTVPvsO73Bd0T1IBQGpgkBVm2arQVI7YFBlMyNKmy65f1BKzFC5S5mTOH7tehBD4B-kG8MWOoMnau4TBjM_ccf_91D1vfkF9d8qGcy4sFWyglOODr30BeO3Z5OL6ykTQZLV91iN3o8qHHBaX7ZGN0-cTA2aJLvpQMOCERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛ OpenCut جایگزین رایگان CapCut که متن‌بازه و مستقیم در مرورگر کار میکنه
🔥
🔹
این پروژه هنوز در مراحل اولیه توسعه قرار داره، توسعه‌دهندگان وعده دادند که امکان دسترسی به ویژگی‌هایی که در CapCut فقط برای مشترکین پولی هست رو فراهم کنند.
🔹
در حال حاضر تمام عملکردهای اصلی ویرایش، تولید زیرنویس، تنظیمات خروجی و .. در دسترسه.
🔹
به زودی یه کتابخانه از جلوه‌ها و انتقال‌ها و همچنین یک سرور MCP برای کار با هوش مصنوعی به این نرم‌افزار اضافه میشه.
🌐
https://opencut.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/ArchiveTell/7017" target="_blank">📅 11:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7016">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMMg7w-j3Fiah_OqTxhhnn2qf6nICDhoG8NTMxQdAlOjC3adfKERp6S5n_ADKMd1jdyP9KeF2_a4edA3REfob_lZKexa4LyLqu5QWskli1CAGzZtOVmQOegMG63btwr4EKc8_n8haKjWhM10-FBSP9SQzVNlmLv85eRkEPy9m4zTdlif2-xlgSmZUhh3k-RabvCQqUOQJnMjzqxD_rgccVd4JwFFuWe_iuCTA2iwOoKa3ljqcnnsYqNNoSuWiLxnT82GGIYfbRbg5uJdHrb_79WEktLaSWwJxdOvzR6IxtXtAJNsc_rAwxA1ETRGCdKHdejrubdCa4Ya7K1FXAK0kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
یه کتابخانه عظیم از دوره‌های آنلاین رایگان
با CourseCorrect میتونی هر مهارتی رو یاد بگیری
🔎
فقط بنویس چی میخوای یاد بگیری؛
سیستم خودش دوره‌های مناسب از منابعی مثل Coursera، edX، یوتیوب و… رو پیدا میکنه.
✨
اطلاعات هر دوره:
🔹
زمان تقریبی یادگیری
🔹
سطح موردنیاز برای شروع
🔹
چت با هوش مصنوعی برای بررسی اینکه این دوره مناسب تو هست یا نه
🌐
https://coursecorrect.fyi/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7016" target="_blank">📅 10:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7015">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9TZJAq3jRKMPWX3EMFHVpPZXnSAfhapM5zYovT7eCjc3AtmG7G6Q-DFS9YR_-XzglmhdDAeTfIzRWrnrZOR6PIvJ_gAHjxLnHwPlGzAEW_axqKO-0T4yOIvbagSQRjSk7abpY9FH10U0Q9rr_Jgj3AbRj0HpvGFoAXpRTugkWHDDaLtXBddR1RqTHY7S2qmv-0IoZHWH60dsMZ5rfSwCNaG8DsplY7mWwJcfm8X0C650lB6ImDX7SQptxmDWe0R8i4Tq2QhXH7INkVyB3vajC8fJJ8zvUH5_PzH7m1w5epUazl-xBOre0TdX3gI4ZFT5HLXq1eaPaNA4eZirSP7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔓
دور زدن محدودیت‌های پولی مقالات با یک کلیک!
این افزونه مرورگر به شما کمک می‌کنه تا بدون نیاز به خرید اشتراک (Paywall)، به متن کامل مقالات در سایت‌های پولی دسترسی پیدا کنید.
✨
این ابزار چطور کار می‌کنه؟
🔸
فریب سایت‌ها:
افزونه خودش رو جای ربات‌های موتور جستجو جا می‌زنه؛ در نتیجه سایت‌ها تصور می‌کنن با یه ربات طرفن و کل محتوا رو رایگان نمایش می‌دن!
🔸
استفاده از نسخه آرشیو:
در صورتی که سایت خیلی سخت‌گیر باشه، افزونه به‌طور خودکار می‌گرده و نسخه ذخیره‌شده (Cached) همون مقاله رو براتون پیدا می‌کنه.
🔗
لینک دریافت افزونه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/7015" target="_blank">📅 09:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7013">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6514ad748.mp4?token=dIH9XuoME75L6oLQ_Seyu_aeZoGEC40xk8UvdJcZtjI1cA-acxeQv4-sazTmAuUGOl2L5mvgwwD4WsS0etj4Kc0Ry1c7VyDf7IXjP43MHfWKrTIL_FKruLh2BRkus6ITwl-77E8y2OBxNDQbfMjgjVb44aNbKby2M6oMWz06poMz0kd5FXYZifzLyG_OS8632KLWMz_Ck8ddnUG8cy6Jj5PYucSr54qtxEoo36wEkY5iEOdmbRmrIfmtgOjbx6a-QHDBf8RmrLHpyLqZOG6mfPJKBHaQj8pc6eLtBp8DOA2z2lu0TvbKzuUScs24C60naXWoeCY1Oni-k1Jbx6ByYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6514ad748.mp4?token=dIH9XuoME75L6oLQ_Seyu_aeZoGEC40xk8UvdJcZtjI1cA-acxeQv4-sazTmAuUGOl2L5mvgwwD4WsS0etj4Kc0Ry1c7VyDf7IXjP43MHfWKrTIL_FKruLh2BRkus6ITwl-77E8y2OBxNDQbfMjgjVb44aNbKby2M6oMWz06poMz0kd5FXYZifzLyG_OS8632KLWMz_Ck8ddnUG8cy6Jj5PYucSr54qtxEoo36wEkY5iEOdmbRmrIfmtgOjbx6a-QHDBf8RmrLHpyLqZOG6mfPJKBHaQj8pc6eLtBp8DOA2z2lu0TvbKzuUScs24C60naXWoeCY1Oni-k1Jbx6ByYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
انتقال فایل بین تمام دستگاه‌ها با PairDrop (بدون نیاز به نصب)
ابزار متن‌باز و تحت وب
PairDrop
سریع‌ترین راه برای جابه‌جایی فایل بین ویندوز، مک، لینوکس، اندروید و iOS است.
✨
ویژگی‌های کلیدی:
🔸
انتقال محلی:
شناسایی خودکار دستگاه‌ها در یک شبکه Wi-Fi.
🔸
انتقال از راه دور:
اتصال دستگاه‌ها در شبکه‌های مختلف فقط با یک کد ۶ رقمی.
🔸
امن و مستقیم (P2P):
ارسال فایل‌ها بین دو دستگاه بدون ذخیره در هیچ سرور واسطه‌ای.
🌐
اجرای مستقیم:
pairdrop.net
🔗
سورس در گیت‌هاب:
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7013" target="_blank">📅 08:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7012">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brCDitUlFnWbI48o64G9tmmOUuiTaKFCxQUq1ePUSD-PNRoa5ApmB8Zg82ZL3R-EjdF3Y8E3UKMEmyBAYx6CXsZR9u62FHKzV7ziW-5lHsbKqj_yYM68QoaPF23etdjAtZlTNwW_OltG-g-cLVkPBsHZ9PRSB5l7_6gCz7WNtMZWuCjjiREVH0xkctzSJB01T2MxQcPhKHywYqPARSm90hbOyX1lHV6AI_-HxmeavC6YnxbhKh7Lnwvg4o0pIWKvXmWe39Cve9KJTakp564ZtUxY4o_erf4c9yGd6mkkjLxfGe8bPMKSilr5otkldy5TzUx4zQhgFTyw-UX0oXv9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دریافت اکانت ۳ ماهه رایگان Avira VPN (نسخه Prime) (
تست نشده)
یه فرصت عالی برای دریافت اشتراک ۹۰ روزه و کاملاً رایگان فیلترشکن قدرتمند آویرا، بدون دردسر و خیلی سریع!
✨
مراحل دریافت اشتراک:
🔸
مرحله اول: وارد لینک کمپین آویرا بشید و با یه ایمیل (واقعی یا موقت/فیک) ثبت‌نام کنید.
🔸
مرحله دوم: ایمیلتون رو تایید (Verify) کنید و یه پسورد برای اکانتتون بسازید.
🔸
مرحله سوم: وارد داشبورد بشید؛ تو بخش وضعیت اشتراک (Subscription Status) می‌بینید که اکانت ۳ ماهه شما آماده استفاده‌ست!
📥
لینک دانلود اپلیکیشن از گوگل‌پلی
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7012" target="_blank">📅 02:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7011">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ai2lahxcxs41Be8b49etOupwstm9bo9v6KnboB5Fl2nNUMHiev504QnwkPqznfhwOAzVXprBjxnzwgvxKnCCm-RI9rFgj_2d8vp-IdrtjMizm9PAiUO182weEYHZKii2UPuwnwLKbPWBh83DhodXBmzRhsYabItHwXsZPkvigccAGRylnzYKiXqK6DGgEaD-ey3T0wsbtoq0zwhcg-3lgN55_oWtD4TViUMqhc51V4O79nQTihUlH_nd-NTWI5uNDH8SZLK1iIlG-pWT1AWx0cg_PCqu0fvZi8FP6aIeDYXfa-w3poteFsWfR2CTJ4FAUN2_DoKdivI5jq2v9Ugeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار از زندان DeepSeek
👇
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7011" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7010">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🛡
آموزش ساخت کانفیگ Bepass (متد یوسف قبادی) روی Nekobox  این روش کاملاً با پنل‌هایی مثل نهان یا BPB متفاوت است و با استفاده از Worker کلودفلر و پلاگین اختصاصی Bepass روی نکوباکس کار می‌کند تا نتیجه متفاوتی برای دور زدن فیلترینگ به شما بدهد.
🛠
مراحل راه‌اندازی…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7010" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7009">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🖥
نسخه گرافیکی ویندوز فیلترشکن Aether منتشر شد (آپدیت v0.3.0)  اگه یادتون باشه قبلاً ابزار خفن Aether رو معرفی کردیم که بدون نیاز به خرید سرور، فیلترینگ رو دور می‌زد اما محیطش متنی (ترمینالی) بود. حالا ابزار Aether-GUI اومده تا همون قدرت رو با یک رابط کاربری…</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7009" target="_blank">📅 01:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7008">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🖥
نسخه گرافیکی ویندوز فیلترشکن Aether منتشر شد (آپدیت v0.3.0)
اگه یادتون باشه قبلاً ابزار خفن Aether رو معرفی کردیم که بدون نیاز به خرید سرور، فیلترینگ رو دور می‌زد اما محیطش متنی (ترمینالی) بود. حالا ابزار
Aether-GUI
اومده تا همون قدرت رو با یک رابط کاربری تر و تمیز و فقط با یک کلیک در اختیارتون بذاره!
✨
امکانات برنامه و تغییرات این آپدیت:
🔸
خداحافظی با ترمینال:
دیگه نیازی به دستور زدن نیست؛ یه دکمه Connect می‌زنید و تمام تنظیمات و اسکن‌ها تو پس‌زمینه خودکار انجام می‌شه.
🔸
ارتقا به هسته جدید (v1.1.1):
مشکل اتصال فیک کاملاً حل شده؛ پروکسی SOCKS5 فقط زمانی فعال می‌شه که تونل واقعاً تست شده و ترافیک رو عبور بده.
🔸
ریکانکت هوشمند و اتصال سریع:
برنامه آخرین مسیر سالم رو یادش می‌مونه تا دفعه بعد بدون اسکنِ کامل، درجا وصل بشید. اگه اتصال هم قطع بشه، خودش خودکار ریکانکت می‌کنه.
🔸
فوق‌العاده سبک:
مشکل مصرف پردازنده برطرف شده و مصرف CPU برنامه وقتی مینیمایز (تو بک‌گراند) باشه تقریباً صفره!
🔸
پنل پیشرفته:
می‌تونید پروتکل‌ها (مثل MASQUE یا gool) و نوع اسکنر رو خیلی راحت با رابط گرافیکی تغییر بدید.
این نسخه در حال حاضر برای
ویندوز
(فایل‌های نصبی exe. و msi.) آماده شده است.
📥
دانلود فایل نصبی (از بخش Releases)
🔗
صفحه اصلی پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7008" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7007">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHmnhidmHkr-qz5wAizJQYSGKiqZoxr9IF-_kCDN8quo16-zH0Jpxv09TN19omPi1iJcWAozr-NSKAGBuxfGIQEMMgnLsEDMDQCyapQyq4Z68Vq3KHRIu7jCDnaOxTy9tyRzZ2h4Z2CHkd-sZUN4HFHodNrqv_K6Wy-364pOUQUA21zyWjcg9-7Z0yzYn8DWsgB0j0ugTOSzYeMJtpQCIWBk7yM_0NRRQDpIp5s0pep7zuJPpUKtaKg2swF984AaVvLWuMnAFoivO1gkidX9EhLZpMQ_OmIes9AMGRRg1XHWrcP9QK-BcGLWWGs7bb3buuLBnnJP8Mq_57fj0cVQhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید و خفن Aether (نسخه 1.1.1) منتشر شد!  تو این نسخه کلی از باگ‌ها برطرف شده و امکانات جدیدی اضافه شده که اتصال رو خیلی پایدارتر و راحت‌تر می‌کنه.
✨
تغییرات مهم این آپدیت در یک نگاه:
🔸
خداحافظی با اتصال فیک: مشکل وصل شدن ظاهری برطرف شد. پروکسی SOCKS5…</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7007" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7006">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه  پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز…</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/7006" target="_blank">📅 23:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7004">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🛡
آموزش ساخت کانفیگ Bepass (متد یوسف قبادی) روی Nekobox
این روش کاملاً با پنل‌هایی مثل نهان یا BPB متفاوت است و با استفاده از Worker کلودفلر و پلاگین اختصاصی Bepass روی نکوباکس کار می‌کند تا نتیجه متفاوتی برای دور زدن فیلترینگ به شما بدهد.
🛠
مراحل راه‌اندازی در چند قدم ساده:
🔸
۱. نصب پلاگین: ابتدا پلاگین Bepass را دانلود کرده و داخل برنامه Nekobox (نسخه ۱.۳.۴ به بالا) فعال کنید.
🔸
۲. ساخت ورکر: فایل Worker را دانلود کرده و یک ورکر جدید در Cloudflare بسازید و کدها را داخلش آپلود کنید.
🔸
۳. تنظیم آدرس: به انتهای لینک ورکری که ساختید، عبارت /dns-query را اضافه کنید.
(مثال: https://name.workers.dev/dns-query)
🔸
۴. ساخت کانفیگ نهایی: لینک به‌دست‌آمده را داخل «فایل خام» که در این لینک (Rentry) قرار دارد، جایگذاری کنید.
🎁
راهکار سریع‌تر (کانفیگ آماده):
اگر زمان یا حوصله ساخت کانفیگ را ندارید، می‌توانید مستقیماً از کانفیگ‌های آماده‌ای که در همان لینک Rentry
قرار داده شده استفاده کنید (فقط فراموش نکنید که حتماً باید پلاگین را روی نکوباکس نصب داشته باشید).
با تشکر از یوسف قبادی عزیز
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7004" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7002">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAJQQaVp_MDZQkzD4iw2PBVtEWl3xgyqMwyxSi91z77jNRni3ZFt-LC1qIVlVYDlj9GY1_eDx9g9b0NR4wi9KGF8ty276xhGntvnkU7uRiZVoqKpVBAqPrQ8FHuXMqklGo5zwAthp_55YGXiZfaSOVYu3gw0hTm9sKWI7NkwMcfNMG7HoyEbTuiOFvGkLSytjrSc4y0uPsv2ApHFVROfLkEdt1J5HsG8nf82QC51NrVhSWqUj_XX6SoR6Ld8ILQIQSx8vasgLaLgmrC4eWwioT2pxcrjyaur_l8M1a5cKvfg0HPgxwVr3Rv6bfAjh6H_9TrNlNjhRMOTI_Bz8wmWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
معرفی Consensus؛ موتور جستجوی هوش مصنوعی برای تحقیقات علمی!
اگر دانشجو، پژوهشگر یا حتی یک فرد کنجکاو هستید، Consensus یک موتور جستجوی مبتنی بر هوش مصنوعی است که پاسخ سوالات شما را مستقیماً از دل مقالات و منابع معتبر علمی پیدا می‌کند.
✨
ویژگی‌های این ابزار در یک نگاه:
🔸
دسترسی به پایگاه داده عظیم:
جستجوی هوشمند در بین بیش از ۲۰۰ میلیون مقاله و سند علمی معتبر.
🔸
پاسخ‌های مستند و واقعی:
ارائه جواب‌های کاملاً مبتنی بر فکت و شواهد علمی (به دور از اطلاعات زرد و نامعتبر اینترنتی).
🔸
استخراج هوشمندانه:
پیدا کردن مرتبط‌ترین تحقیقات و استخراج نکات کلیدی آن‌ها در چند ثانیه.
🔸
کاربرد همه‌جانبه:
یک دستیار عالی برای نوشتن پایان‌نامه، مقاله‌نویسی، یافتن جدیدترین دستاوردهای پزشکی و تحقیقات شخصی.
🔗
آدرس سایت:
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7002" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7000">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHjfhUEmp0fj_3XfDjDPYb6PluKMYCAEhvZ6VZ0mWZeJspsUnWCCxbHK077oenR0q2oEy0u4tsYOW4S0P3T0e68GgjaWLk2Z649xtLlMmIrLrhqTie-yGqVUHvNmZflVZQCC8vfz42lBIvx6SDY-OFNj1lyyYlQxDlha5Smgq6Ip_pmycVJMEF2uTZfip1zZXCBDfGeVweGoxxFfwaJOYylSjf5JO7eRnsOdjoNuMR441fR-JLfXacs9wmIAq8s2ZSGZpXwN9ATDydz8A96Pj5mqT2r96Rwpv5Z3vAcIu_yy6twhI_54RqpcXpoougNtnvrr0Y13oHGfXQPRBu38kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📦
Universal Installer؛ همه‌کاره‌ترین نصاب برنامه‌های اندروید!
اگر زیاد برنامه‌ها را خارج از گوگل‌پلی دانلود می‌کنید یا با فایل‌های چندتکه سروکار دارید، این ابزار متن‌باز جایگزین بی‌نظیری برای نصاب پیش‌فرض گوشی شماست.
✨
ویژگی‌های اصلی در یک نگاه:
🔸
نصب هر نوع فرمتی:
پشتیبانی کامل از APK, APKS, XAPK (همراه با OBB) و APKM.
🔸
نصب خاموش و گروهی:
نصب و حذف بدون نیاز به تایید مکرر (نیازمند Root یا Shizuku).
🔸
جعل هویت (Spoofing):
گول زدن سیستم برای اینکه فکر کند برنامه از گوگل‌پلی نصب شده است.
🔸
شخصی‌سازی نصب:
امکان داون‌گرید کردن نسخه‌ها و دور زدن محدودیت‌های SDK.
🔸
سد امنیتی:
اسکن خودکار فایل‌های نصبی توسط VirusTotal.
🔸
انتقال محلی (LAN Sync):
اشتراک‌گذاری و نصب راحت فایل‌ها بین دستگاه‌ها از طریق Wi-Fi.
🔸
طراحی و پشتیبانی:
رابط کاربری مدرن (Material 3)، بدون تبلیغات + نسخه مخصوص Android TV.
📥
سایت رسمی جهت دانلود (گیت‌هاب، گوگل‌پلی و F-Droid)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7000" target="_blank">📅 20:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6997">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuiHGaq9y9bThU7EjYl9l2Zg3CIwAolc09v24qHUEf6jKn5Ano0JM0kqUQWg_lAvVW7e8FHIhCcrjUlwIEXnMqZpOllmu_-3LPLtxm98DGsWdEDu1fNyGoZ5XV6SUIl3jYfMxBvWfxMCpmf7L3UF1sLcPWAWZUaemGNb7wmtVDCiSTL5FKypfhvMWjXNQblGuh_s0hDPjoVBNR9v0fvzG-fju45FhdHNKgjLrpMpy5vhWdBrv4o9tTV4Z_fFwlcXWBB81fp0nAVFhnIhyl0zaLwrTjqkGVVZE--KTo4gNDPeL3iv45-jEuyx7R628uCrkR0lrUX29zn4CD-jXSIbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fP07lb43hJ_NiZujOgOv_Pl0FzF-Dj1ZS5pdmaYcUgFzI9mpZOqCur8cEOMZOKHF6cYMra7CMmB2LBah5_TIBsRbgvOicflSareRafeV53HRc9ExGUzK4dQHyD4NlLB13uhMNP6haIQ73zIbcc3j91gU0etsbdGvvvvNFG0F0kILcsoPXsLUhEyV9kNDuXMuvzQJFn08JUY6O1YKpD968P0bxYQyVUjCcr8IAfrEeZYY9is5zEuhT2ds3jlw_V0BkdP84j8yJjGZl6OkxbVvvxO3bTEhMynEF-jPygyBPap3IogsyMBFg36bLTgNlTvkpqZM9GUZfUfI9tzRlhunrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
گوگل برای ۲۵ سالگی Google Images سورپرایزهای بزرگی
معرفی
کرد.
🔹
تولید تصویر با مدل Nano Banana 2 Lite داخل Google Images
🔹
طراحی جدید و مدرن صفحه اصلی
🔹
گالری شخصی‌سازی‌شده شبیه Pinterest که با توجه به سلیقه کاربر تغییر می‌کند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6997" target="_blank">📅 18:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6996">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhmJ8S_vPws9oVrEonbEFXKowt3A7DQrpApZAZzzWuqNKFMizNPT_shhS8AuDSdcKPq9W6s3071UUCBUIvAJyL0xG48Azdho5ab-rubYv4tYPHxggM7TzFJLOWOIoSNvZrBSJDF9rdmeDZcMtrG_Evjvx7HosgT3ry117vQfQqJPK13tEAVE4insEsgdM8mmuhBx8zfzS3NP_a66xqcdA0wVRb92P4lT4ZEbwt0n-6D08hZrJ-cxLivIejZa_GP0-N0rT3zeQTwbfmVrgztdy8KQeyiuMxoBCODhwYFsZNqXQmPamqm2bHP0rAvyiQOsPErJL41hxS42ig-zG14MQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثه آب خوردن  کلا ۱۰ ثانیه هم طول نکشید
😐
ولی وصل نشد رو ایرانسل برام
😐
😂
😂</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6996" target="_blank">📅 17:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6995">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxjPmlJIrFSPgrMyzxHXZhcSk4t8uzuIaM-KR0XwAL_5IAzgJ9RSW0m__jsaCmFDG9Dmcz9mdqOurdEp0lzWmU3QVpLSmPJbWmfWMn22HhHQjE9tsN-yiXuoOZfM_Vxx587xCWSQ3sqiOIYf44C4r3jRZ8INel9VKZyujCrXE7NgtWjzeGcikM6sGNW7oUFtQxM-ZBF7cjk_9aBeY83aJFSTYe8EAdoc2HZxAuUsHMw6kAbkE2q4XUj8kIcpcRGjQo2Yk2GbgRP3ux0DINZOucNR4-4JqWJxLqv4mANctjYOLA5xupbKfA56dK1i31Aj6Hz09ulZOUe_4XG8gMzAqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه  پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز…</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6995" target="_blank">📅 17:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6994">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه
پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز می‌کند.
✨
ویژگی‌های کلیدی:
🔸
بدون نیاز به سرور شخصی:
سیستم به صورت خودکار سرورها و مسیرهای سالم (Endpoints) را پیدا کرده و متصل می‌شود.
🔸
پنهان‌سازی ترافیک (MASQUE):
ترافیک شما در بستر HTTP/3 و HTTP/2 کپسوله می‌شود تا کاملاً شبیه به وب‌گردی عادی (HTTPS) به نظر برسد و مسدود نشود.
🔸
امنیت مضاعف (gool):
علاوه بر پروتکل WireGuard، از حالت وایرگارد تودرتو (Nested) برای ایجاد یک لایه رمزنگاری اضافه پشتیبانی می‌کند.
🔸
کراس‌پلتفرم:
دارای نسخه‌های آماده برای ویندوز، مک، لینوکس و اندروید.
📱
نصب سریع در اندروید (از طریق Termux):
برای نصب خودکار، کد زیر را در محیط Termux کپی و اجرا کنید:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
پس از اتمام نصب، کلمه
aether
را تایپ کنید تا برنامه اجرا شود.
ابزار پس از اتصال، یک پروکسی SOCKS5 (به عنوان مثال روی لوکال‌هاست و پورت
1819
) در اختیار شما قرار می‌دهد که می‌توانید آن را در تلگرام، V2ray، Nekobox یا تنظیمات سیستم وارد کنید.
📥
لینک گیت‌هاب (جهت دانلود نسخه ویندوز، لینوکس و مک)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6994" target="_blank">📅 17:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6992">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvN--yDGoWlSSTY2K-otupjsZCiom4j-ULXvjANOOG7Xaf0q6AqCGhId4MHdhFHwuNWuTZ6vSI2D4G9GquLsk0VJrbHtFiamWvokc8X7DWF0CWFaMMiqUQYiYtajyjXDR2-yJNSeZRfOUN5GXzCB81xVN6rN-enB5Ugpj2e8NZCBAweygb383jwzUS9fWtO8L2Y5oqcyr_CC-2p6uFokvDBP6v-mT_6P_g8oBpARFf7esnPEx06HH3SUv5CA42WB-V13NXDv6pu1DKDrweu32LvaH7tueC9rhs3Y8Z67XcOwmcrW9oggCIAxOC3W8DpeK_4-tWQwBvMpjG8LlA2x4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
اشتراک یک‌ساله و رایگان MultCloud (ارزش ۴۰ دلار)  مولت‌کلود (MultCloud) ابزاری بی‌نظیر برای مدیریت یکپارچه تمام فضاهای ابری (گوگل درایو، وان‌درایو، تلگرام، دراپ‌باکس و ۳۰ سرویس دیگر) در یک پنل است. با این ابزار می‌توانید فایل‌ها را بدون نیاز به دانلود و…</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/6992" target="_blank">📅 16:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6991">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4TNBVHf113cAMOXomugv3uqGvsv8yX4lo5aTiPE7qCSv3qWyQOiSDi2-g72cxMWRLAPQs-Dhnsh1jNtB0GKVUtFhqK4qraDlUUMAZMHY0nTEIpDJ8ENMImz19bFYB0PNL6QZ-DQQBXU-4W65_rXFCTyr4VO8YCejgvTsuezHFZHx2-VbkOwZr_FH-IvhldsPJqvS9-30o83muS9Sb_V4sZc4bQA9s8iGtat9HFGbH7gQb5PX7Q9u59KqKazjwwJW7XqPdLuYYaiI2OuZqzMIvIueOR1En4AJtCSvKes0VBy_j_u459WBRVqxHTt-6HDCjaiXRVPOWnUyGRFy9YTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
اشتراک یک‌ساله و رایگان MultCloud (ارزش ۴۰ دلار)
مولت‌کلود (MultCloud) ابزاری بی‌نظیر برای مدیریت یکپارچه تمام فضاهای ابری (گوگل درایو، وان‌درایو، تلگرام، دراپ‌باکس و ۳۰ سرویس دیگر) در یک پنل است. با این ابزار می‌توانید فایل‌ها را
بدون نیاز به دانلود و مصرف حجم اینترنت
، مستقیماً بین فضاهای ابری مختلف منتقل، سینک یا بکاپ‌گیری کنید!
🎁
نحوه دریافت اکانت پرمیوم ۱ ساله:
🔸
وارد لینک زیر شوید و یک حساب جدید بسازید.
🔸
در پنل کاربری، از منوی بالا روی آیکون کلید (
🔑
) کلیک کنید.
🔸
کد پروموی زیر را برای فعال‌سازی وارد کنید:
BAAYK667N5K3K0N6
🔗
ورود به سایت
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/6991" target="_blank">📅 16:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6990">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5760952ca.mp4?token=FZRrj57bREf0K7E3AytGMVPClALg_AncYHCwWmObaoKj8qUdDK0xTWhDxBU4hdPU8nc9-5Aofyy0Z244d8SG-0-foKY7-b4H7OJo2jLNOCu-zhzfZuTpM1TOqZ4xlB3AyZkRogRpeNFBRmIOYFBfScISG-MTJZIru2_-xO6wHOB2Nhw39Kma_BvKbII5NwqCqIUhy2B4TzHMJJHR-Kvuks8JJ4AGqAIOk9Y7BcN6n1P__nFR3g1MjCRA_sEZtDher4kaqwXxzJO0tbnGZnB4ACJTkU1vBDrEz_OPmUIJHgvDW4dLK6LR2_M84vwW2Fc25X6_0ZS7NTZXh34WcOvbVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5760952ca.mp4?token=FZRrj57bREf0K7E3AytGMVPClALg_AncYHCwWmObaoKj8qUdDK0xTWhDxBU4hdPU8nc9-5Aofyy0Z244d8SG-0-foKY7-b4H7OJo2jLNOCu-zhzfZuTpM1TOqZ4xlB3AyZkRogRpeNFBRmIOYFBfScISG-MTJZIru2_-xO6wHOB2Nhw39Kma_BvKbII5NwqCqIUhy2B4TzHMJJHR-Kvuks8JJ4AGqAIOk9Y7BcN6n1P__nFR3g1MjCRA_sEZtDher4kaqwXxzJO0tbnGZnB4ACJTkU1vBDrEz_OPmUIJHgvDW4dLK6LR2_M84vwW2Fc25X6_0ZS7NTZXh34WcOvbVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
نتفلیکس شخصیت رو تو چند دقیقه بساز!
با Reiverr همه فیلم‌ها و سریال‌هات رو یکجا و مرتب داشته باش:
✨
امکانات:
🔸
جست‌وجوی هوشمند با پوستر، تریلر، امتیاز و توضیحات
🔸
ادامه تماشا از همون ‌جایی که متوقف شدی
🔸
پیشنهادهای شخصی برای وقتی نمیدونی چی ببینی
🔸
رابط کاربری مناسب برای تلویزیون
🔸
اتصال به تورنت‌ها و سایر منابع دانلود
🔸
نصب روی کامپیوتر یا سرور شخصی تنها با یک دستور
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6990" target="_blank">📅 12:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6988">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👱‍♂️
پروژه Ponytail
برنامه‌نویس ارشد تنبل برای هوش مصنوعی شما!
✨
ویژگی‌ها:
🔹
جلوگیری از پیچیده‌نویسی (Over-engineering) توسط هوش مصنوعی
🔹
کاهش حجم کدها تا ۹۴٪ و صرفه‌جویی ۲۰٪ در هزینه‌ها
🔹
افزایش ۲۷٪ سرعت انجام وظایف، همراه با حفظ امنیت کد
🔹
اولویت دادن به کدهای موجود و کتابخانه‌های بومی، به‌جای تولید کدهای اضافی
🔹
سازگار با بیش از ۲۰ دستیار هوش مصنوعی، از جمله Cursor، Copilot و Claude Code
📥
گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6988" target="_blank">📅 12:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6986">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏
🤖
پروژه Hermes Agent (نسخه اندروید)
🔥
پیشرفته‌ترین ایجنت هوش مصنوعی خودآموز (Self-improving)!
✨
امکانات:
🔸
پشتیبانی از انواع مدل‌ها (OpenAI، OpenRouter و مدل‌های Local)
🔸
اتصال مستقیم و مدیریت از طریق تلگرام، دیسکورد، واتس‌اپ و اسلک
🔸
حافظه بلندمدت، یادگیری…</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6986" target="_blank">📅 10:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6985">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcOHyi88AjOGcGA1wqP64lTEK59eD-KG1Q1dn06pB_-Aelt-h8SPGQgUW-iL2vdx8KFjD88L4U1oiyaTuCxoDTT6XkTJasbg4N7taWSIffLc8k1P_yfYgQyackXUZOtz21h_ps0LyEEjbtopowllMKTAYqfXTFnzGqRRdU6s-3VTS-StPfbC5N-VLJAaHtRUecrHQ90_CiSedwCoe4rOgnY_srEadf629TO7ny3mLAKP1qhNa0H_Ih4caeX9scwnD9FnG3qny_RGTNEk8T7J2dxgDvyeNXL7ca3o7B4L-KNfpQ3DNbzdPaPZmVGcnGgQ2Cthr-D1INQ-x9YFf07hJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤖
پروژه Hermes Agent
(نسخه اندروید)
🔥
پیشرفته‌ترین ایجنت هوش مصنوعی خودآموز (Self-improving)!
✨
امکانات:
🔸
پشتیبانی از انواع مدل‌ها (OpenAI، OpenRouter و مدل‌های Local)
🔸
اتصال مستقیم و مدیریت از طریق تلگرام، دیسکورد، واتس‌اپ و اسلک
🔸
حافظه بلندمدت، یادگیری خودکار و ساخت مهارت‌های جدید
🔸
اتوماسیون و زمان‌بندی وظایف (Cron) فقط با زبان طبیعی
🔸
دارای اپلیکیشن بومی اندروید برای اجرای مدل‌های آفلاین (Gemma و Qwen)
📥
دسترسی و نصب:
GitHub
,
F-Droid
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6985" target="_blank">📅 10:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6984">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0EYpgsjMC0InTSAYddwd1Ftt_dOZvOhgj2DNVkcUrxDqPRcksNTxvti16b3TuTmKH9z2Q7ZRGynAkG9q4P0sxMCHiSP2yeEVMZ3F_mD5TgLfThv1X2PlI4kFOAaxm_nKcW0GBJWKKTlsH2ynOMHIoiARFIvPqLeGIumzKHIn9smCtz9BrUWT3KLKvFYQr9tZutxkfQYX3V-NWdRp85-GIYa7iSprCqfSsc7jDCpO1p2pVPwRS8u0lNd8qCl6qHFtdI83eilLf66UUDkA_GUI3kbMWhRQ3SucDzUqZaJXl3yYyMUy7CDKJvB64GXTsv9WKpMqGR0E153cgPAdEsViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💎
Google Gemini API
دریافت رایگان توکن‌های هوش مصنوعی گوگل!
✨
امکانات:
🔸
دسترسی به مدل‌های Gemini 2.5 Flash، Flash-Lite و Pro
🔸
بدون نیاز به کارت اعتباری یا اشتراک
🔸
ساخت کلید API رایگان در چند دقیقه
🔸
توسعه اپلیکیشن با جدیدترین مدل‌های گوگل
📥
دریافت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6984" target="_blank">📅 10:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6983">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX2wICleWUBjFTUldMVMKsz3jDsRMv7wVhZTOiCyBppX2xn_N6l3Jp7HI1zJkyKM8tuyAJoLsv2aoVnm5SNDqYWZRqfipT_8yzxJREcFJS76x05dOMBVbiUxPINpeeeURJgHxY9_M2eizfudgjgxxOm2CzKaD4kf-NkRaoW4lk8kpWy3StAI_JAe016Umqyfbmm1WX2eB5Any8m9tc9J18erg1oEoBh7Zu2_c5yGgKfILZXKNoW53NxbNhsjNPaVfPrEcpqozTkClliyxAwNWSamUZTiFotj9lQom15ErgsyAqKv0Edn78m7XDOBELceyYo0I8Sn389Ol2rjy-cAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
هفته توسعه OpenAI
شرکت در رویداد و دریافت ۱۰۰ دلار اعتبار رایگان Codex!
❓
نحوه دریافت و جزئیات:
🔸
ثبت‌نام و ارسال درخواست شرکت در رویداد از طریق پلتفرم Devpost
🔸
مراجعه به تب منابع (Resources) در صفحه رویداد
🔸
کلیک روی گزینه "درخواست 100 دلار اعتبار Codex" و ثبت آن
🔸
مهلت ثبت‌نام:
تا ۱۸ جولای ۲۰۲۶
🔗
ثبت‌نام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6983" target="_blank">📅 08:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6981">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏
🛡
مرورگر Cromite (کرومایت)؛ جانشین قدرتمند Bromite  (جایگزین کروم)  اگر از طرفداران مرورگر محبوب اما متوقف‌شده‌ی Bromite بودید، Cromite دقیقاً همان چیزی است که نیاز دارید! این مرورگر یک نسخه سفارشی (فورک) از کرومیوم و بر پایه برومایت است که با تمرکز شدید…</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6981" target="_blank">📅 02:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6980">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏
🛡
مرورگر Cromite (کرومایت)؛ جانشین قدرتمند Bromite
(جایگزین کروم)
اگر از طرفداران مرورگر محبوب اما متوقف‌شده‌ی Bromite بودید،
Cromite
دقیقاً همان چیزی است که نیاز دارید! این مرورگر یک نسخه سفارشی (فورک) از کرومیوم و بر پایه برومایت است که با تمرکز شدید روی
حریم خصوصی
و
حذف تبلیغات مزاحم
توسعه داده شده است.
✨
ویژگی‌های برجسته کرومایت:
*
🔸
ضدتبلیغ داخلی (Ad-blocker):
مسدودسازی خودکار تبلیغات و ردیاب‌ها بدون نیاز به نصب هیچ افزونه اضافی.
*
🔸
پشتیبانی از افزونه‌ها:
امکان نصب و اجرای اکستنشن‌ها (Extensions) در حالت توسعه‌دهنده (Developer Mode).
*
🔸
حریم خصوصی حداکثری:
محدود کردن و غیرفعال‌سازی ویژگی‌هایی از کرومیوم که برای ردیابی عادات وب‌گردی کاربران استفاده می‌شوند (قطع ارتباطات اضافه با گوگل).
*
🔸
مقابله با انگشت‌نگاری (Anti-Fingerprinting):
جلوگیری از شناسایی و ردیابی دستگاه شما توسط سایت‌های مختلف.
*
🔸
آپدیت خودکار:
دارای سیستم آپدیت داخلی در اندروید (همچنین پشتیبانی از مخزن رسمی F-Droid).
*
🔸
پشتیبانی گسترده:
قابل نصب روی اندروید (نسخه ۱۰ به بالا)، ویندوز و لینوکس (۶۴ بیتی).
🧪
نکته امنیتی:
این مرورگر برای استفاده روزمره و وب‌گردیِ امن و بدون ردیابی عالی است؛ اما خود توسعه‌دهنده صادقانه تاکید کرده که برای خبرنگاران یا افراد تحت محدودیت‌ها و سانسورهای شدید، همچنان استفاده از نسخه دسکتاپ
Tor Browser
پیشنهاد می‌شود.
🔗
[سورس پروژه و دانلود در گیت‌هاب]
🔗
[لینک مخزن F-Droid]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6980" target="_blank">📅 02:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6979">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">net.yukh.xui_81000@ArchiveTell.apk</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6979" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‏
📱
3X-UI Manager  مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع (فقط نسخه +3.3.0)
📥
دانلود: F-Droid و GitHub و Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6979" target="_blank">📅 02:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6978">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏
⚡️
پنل نهان (Nahan Panel)
ساخت و مدیریت فوق‌حرفه‌ای پروکسی (VLESS/Trojan) روی کلودفلر!
بدون نیاز به خرید سرور و درگیری با ترمینال، یک شبکه کامل و ضدفیلتر بسازید.
✨
امکانات برجسته سیستم:
🔸
نصب تک‌کلیکی:
راه‌اندازی خودکار Worker و دیتابیس D1 فقط با دادن یک API Token.
🔸
مدیریت آی‌پی و شبکه:
اسکنر داخلی برای آی‌پی تمیز (Clean IP)، آی‌پی پشتیبان (Relay) و مبدل پیشرفته NAT64.
🔸
مسیریابی هوشمند:
جداسازی ترافیک سایت‌های داخلی (GeoIP/GeoSite) برای اتصال بدون مشکل.
🔸
ضدفیلترینگ پیشرفته:
جعل اثرانگشت ترافیک (TLS Signature Chrome) و تنظیم دی‌ان‌اس اختصاصی (DoH).
🔸
ساب حرفه‌ای:
دامنه اختصاصی لینک ساب، مخفی‌سازی با تغییر User-Agent و نمایش حجم/تاریخ انقضای فیک برای گمراه کردن فیلترینگ.
🔸
امنیت بالا:
دکمه توقف اضطراری (Kill Switch)، مسیر ورود مخفی به پنل و استفاده از پورت‌های امن.
🔸
مدیریت همه‌جانبه:
اتصال به ربات تلگرام اختصاصی (فقط برای آیدی ادمین) و مدیریت همزمان چند پنل (Master/Slave) از طریق API.
🔸
نگهداری آسان:
آپدیت خودکار مستقیم از مخزن گیت‌هاب و بکاپ‌گیری/بازگردانی سریع با فایل JSON.
✅
تا به حال مسدودی روی این پنل گزارش نشده است.
🔗
اجرای مستقیم نصب‌کننده (وب)
🔗
سورس پروژه و پروکسی در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6978" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6975">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nw2zX5M2e8tVmDjppqJdXaMt9W41ZYDcljaybR9OxSaXGv65c2EfKPkA6WwRQv-uK3UGhNVjE5IrHrXlAS4jIDSagdM3X8PNgyqliV2rWsfdHLsZxlDnYMpnxAFAurQkZGxjjKSapypYXp8gNC5LQ_Vexr2NqfpvLOtGgqHercJC7E7NvlWJA7B4kwO7o0tzfA_PfoKFc4uPiOLN1RUkfilgqKLenxijK1QYGISVUPBvtYjXSKfxy18_M83UOsjx7KmwEvdIg35BaymxKTlDSadWvNac6cHzZ--MtHpulJ-FaOSWaF_Ln0wPCm4oTOYUfrVAoQQPThc-djTxzZGOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
تلگرام دیگر برای اجرای ربات به سرور نیاز ندارد
❗️
با قابلیت جدید و فوق‌العاده
Serverless Bots
، از این پس می‌توانید کدهای ربات خود را مستقیماً روی زیرساخت خود تلگرام اجرا کنید.
✨
ویژگی‌های این قابلیت:
🔥
پشتیبانی از JavaScript:
کدنویسی مستقیم و سریع.
🔥
دیتابیس SQLite:
مدیریت داده‌ها درون خود اکوسیستم تلگرام.
🔥
میزبانی بومی:
اجرا مستقیماً توسط سرورهای تلگرام.
🔥
کاملاً رایگان (فعلاً):
صفر شدن هزینه‌های هاستینگ.
🧪
نکته: این یعنی ساخت و اجرای ربات‌های کوچک و متوسط، از این به بعد بدون هیچ‌گونه دردسرِ خرید و مدیریت سرور امکان‌پذیر است
🟠
⛓
منبع
👉
🔤
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6975" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6974">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
📱
3X-UI Manager  مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع (فقط نسخه +3.3.0)
📥
دانلود: F-Droid و GitHub و Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6974" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6972">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3Bw64-TC8HlOlZ9tY6k4No3eCnj8tQTANZ9qlkbMEvzlmRMi6lmrWo1dbsbZ-y8qytrPkVm_iEUbb5Bd3NaxpzSMGxSc6lEHYaX4OMuRuzFBTM6-MATkO_Hp_DqZloFVD0ZTlvTlF_hS6qFqrVRAcVuAR0oYktzV7-BDB_yR5xfxYFRLIO83MKHJZGL7Y50mJVruHQp3PnVFah2b02gC9F4DTkFkSA8tcemVjzRVF5nzuQ8wTMQKSAN6Bh3PJAkhSvdGPggQGlp66u99ci5jt__-qS-8ECaETqHlUFKnoSPbPcu4LvTZUQJcGEmVLO7SRKxWmvegxlyOUr0WXp4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
3X-UI Manager
مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع
(فقط نسخه +3.3.0)
📥
دانلود:
F-Droid
و
GitHub
و
Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/ArchiveTell/6972" target="_blank">📅 22:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6971">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_cdLnJ0n2tYcxifHz4UHNBsx3MVLz4KOglOG1UXjqbiWYm92J414uEQZAXsGODHIIsN199fIAS5QC1qcMSfQ1hOtZCi0lvSgtHjKCEt1HFvypiNPpUvJt-f-29bAuiiQnL4aOtfjtUXO-yyl5TWNaxg1drNfqZJ_FgwvaLUwEvuB8BWVpPHsw-u8Lzt8g586AVpFdw3KO0hgNcqBVUuUCgQPwQpGjBZuk-t1gA8OhZC5Umvk2ZDVAPG8dDOawCWcLwq24JVczpCXTt_dMtJvUBYjkCFMTybwOLNtYc80mmrzTebfWPGSVB_xyUpRLihfz5Mgg_Ks2FfIJMfEgPSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
Droid-ify
یک کلاینت (رابط کاربری) مدرن، روان و فوق‌العاده زیبا برای مخزن بزرگ F-Droid!
اگر از سرعت پایین و ظاهر قدیمی کلاینت رسمی خسته شده‌اید، این اپلیکیشن جایگزین متن‌باز (Open-Source) دقیقاً همان چیزی است که نیاز دارید.
✨
ویژگی‌ها:
⚡️
سرعت بی‌نظیر:
همگام‌سازی (Sync) و لود شدن لیست برنامه‌ها در عرض چند ثانیه (بسیار سریع‌تر از نسخه رسمی).
🎨
طراحی مدرن:
رابط کاربری چشم‌نواز، روان و منطبق بر زبان طراحی Material You.
⚙️
نصب و آپدیت خودکار (بی‌صدا):
پشتیبانی کامل از ابزار Shizuku، دسترسی روت و Session برای آپدیت برنامه‌ها در پس‌زمینه بدون نیاز به تایید دستی.
📦
مدیریت آسان مخازن:
قابلیت اضافه کردن و فعال‌سازی مخازن جانبی محبوب (مثل IzzyOnDroid) تنها با روشن کردن یک سوییچ.
🧪
نکته:
این برنامه در واقع یک پوسته سریع‌تر و بهینه‌تر روی همان دیتابیس امن F-Droid است و امنیت شما را به هیچ‌وجه به خطر نمی‌اندازد. اگر از برنامه‌های اوپن‌سورس استفاده می‌کنید، نصب Droid-ify یکی از واجبات است!
📥
دانلود از GitHub
و F-Droid
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6971" target="_blank">📅 21:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6967">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyZVGCeX4tMxZxfFBTHhc8bYICsxYzk14qDjuDRlM5g3dWDt5lenwkGmqDBlUc6vKnvUkxOYNW1JWvYIxzg1d3IZh8DzmzWG03Fa-di1uh3duBhj0-amUgnti9WuSAVlp2G3XuG0bIQ381Mc-_emaA1e6s-cbbWFxAjVN6xr0AxYlkVz8_ojuYV-2vCcPgmtXYr-5BJRZ074HGzn5cHvMvGfxi2cCBWu2mwKco-A4bp2woIIc7Xn1VimBTm7SwMHrwxzcb7br7Z9GjZ437uAPp5JWx81czC0jqNW7QhAork_Yudlwc1-ZH7oQBk6F1toTVHLJlyTbL2UweDu-v_JUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bknwjtejq5SOliHTKeIJXw58eEi4U27qRYufATgeQv5lKRDIqdE644qR00hnBOOm-a-pD2Vw46gxMU5zqWC2xTlZw1JhLeBJ6KDf7XejeJOe3t_aEvMJUGHrPbNBhFZZjFvnaiQZ_icGbdbNl7ysXhs27j1V0bNkrHMGQVuXOzx_RC1Lb0wVzW32KA_00TQdDHBjOM9S1xplhYg_nZ9v8EOA03F-g19-6FNHfQ02GRvkCREhKSXGwOsshYiYxOTC2Ob-KsmkvN4ADrBjgtCkhzy0GdePJfEX6IxnkOlUPX_3YyeHEFLpmOewl0XiqSJ_i22WQd77whv-kMnAhfDbrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xkry-9_75Nb0N39al2ULIhqIGBJevx2sbpKJHgxnihqb_9SAoVkGbZE9ziRpW2wOZVjdVJSB3xBGXKBHDmx0VChYTHEavMrOHh9JZ5ho5qkYocyMl_MJYnuF_7RlPgjBzq2ImMavtnBIWlqwe_MzAv1ZWAGJryCXP6Sz_BccmaZaCA4oPAcg8keyvkCilM90oz-4y0CCcWLenBV_4DbqmGyvcB5lCsU5LnqZ6Y6PV_1IQ-hHmQdgVHIwYFN5SDxTUGeIf5Xu0PTPL1RBthN2rixLjg7u4JEKOMLha0wpvnn1B9Q3eS2-yDhE7pPUlm8NdJVSeUXDB4yGfXuk0titOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XaUte3tpdpVvv_i7EvlsqF2MnnSH21rxShHBtwq-042kgRiqQXC1QRuaMvgcTbbccslYtEGt6AqqVqe7WcxJjGKuA1S7AC3KPfJSwlE6Hxc_VRt7V3_m2s-Zz1knFO36Oq1YpCuGrNL57LHgVsAvnk_WFOPrZz6FTH1PaBmjafKYmcXOczn2mXnFQONjBBvcr-o7YsHUH5go7kKsc-kvkCqyzLpJjKUsICWpp_ILaloi0gEBfXIuLHT2nJ7uSd5W6XWeJlbyxiCHC0p2LyceuubQ8Ck4Q7JA3HOO2pxET94wKtAr8rKP5CxhGHSi96OhgbO8x6PSIO0srJJsQkZSHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚀
آپدیت بزرگ تلگرام با ویژگی‌های بی‌نظیر منتشر شد!
تلگرام به‌تازگی یک به‌روزرسانی عظیم دریافت کرده که قابلیت‌های کاملاً جدیدی را به این پیام‌رسان اضافه می‌کند.
✨
ویژگی‌های این آپدیت:
🌐
بخش «انجمن‌ها» (Communities):
فضایی جدید و یکپارچه برای تجمیع کانال‌ها، چت‌ها و ربات‌ها در یک مکان واحد.
📝
ویرایشگر پیشرفته پیام‌ها:
ادیتور متن تلگرام دگرگون شده و اکنون از ابزارهایی مانند
جداول
،
چک‌لیست‌ها
و
عنوان‌بندی (Headings)
پشتیبانی می‌کند.
🤖
تولید محتوا با هوش مصنوعی:
از این پس هوش مصنوعی می‌تواند مستقیماً بر اساس درخواست شما، پست‌های آماده و کامل ایجاد کند.
🕵️‍♂️
پیام‌های خصوصی مخفی:
ربات‌ها قابلیتی پیدا کرده‌اند که می‌توانند پیام‌های خصوصی ارسال کنند؛ به‌طوری که این پیام‌ها حتی از دید مدیران چت نیز کاملاً پنهان می‌ماند.
🧪
نکته:
این به‌روزرسانی به‌صورت تدریجی در حال انتشار است، بنابراین ممکن است این ویژگی‌های جدید هنوز برای همه کاربران فعال نشده باشد و دسترسی به آن‌ها کمی زمان ببرد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6967" target="_blank">📅 19:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6966">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiKsem5x8TM6HWhMnX8NepYSBIryOwNEn1X1GJxX-TJ4cvkIIu4u-TA8MSsQ-T4mNUbO3FFe6jrV3_pjjtfU5qtPuAMxn12s9qZ29tuPHtrQUGaAERZzPODIzpT6NTX-s0czRxYB7M0ZGbg8IPenyy81uGH0jhlKqFqymQWd1jQ0rfRpBxg9DGuKti26NVZQINsgWxCvmqIv3aq4L7zSruqdOeuCgeFwlBQ5yWbe_WWYEC400EP0BOSSFrwUHStHGprg0-rEdjy9srlJU0negAPlIb6irH3Z4sY_UD8pCqLu8jJ35J9Q6pjdGVmoiw6_tKRkWhw20kg1SRpHOAMtLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
Acode
یک IDE تمام‌عیار و ویرایشگر کد بسیار پیشرفته (Open-Source) برای اندروید! با این اپلیکیشن می‌توانید پروژه‌های برنامه‌نویسی خود را با امکاناتی در سطح دسکتاپ، مستقیماً روی موبایل یا تبلت مدیریت و توسعه دهید.
✨
ویژگی‌ها:
🎨
پشتیبانی وسیع:
رنگ‌بندی سینتکس برای
+۱۰۰ زبان
و پیش‌نمایش زنده (Live Preview) وب.
🛠
ابزارهای حرفه‌ای:
اتصال مستقیم به
GitHub
، مدیریت سرور با
FTP/SFTP
و کنسول داخلی JS.
⚡️
قدرت و سرعت:
اجرای روان فایل‌های سنگین (بیش از ۵۰,۰۰۰ خط کد!) و پشتیبانی از کلیدهای میانبر کیبورد.
🧩
شخصی‌سازی عالی:
سیستم پلاگین‌پذیر (دارای افزونه‌های هوش‌مصنوعی)، سازگاری کامل با تبلت و
منوی فارسی
.
🧪
نکته:
این برنامه با مجوز MIT منتشر شده و دارای قابلیت بازیابی فایل‌ها (File Recovery) برای جلوگیری از پاک شدن ناگهانی اطلاعات است. (اجرای آخرین نسخه نیازمند اندروید ۸.۰ به بالا می‌باشد).
📥
دانلود از Google Play ،
F-Droid
و GitHub
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
⭐️
Cyru55</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6966" target="_blank">📅 17:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6965">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQvNJsWx7yixvTEjHFMnJuNMBWYaFBXIkGptxsDR_0xBwcAQk-pCsN0x82PyqCFZZU-n22ifDtnKw1XgXdCXr-dhJ3GUiKLvHdDxo4mJuG-xf2Kd2-vO5yHLeVNCc1mraxVAnuwOjqRcNqx5BPsLKCesulbh67gFsb3Ocy5affsqTYbhfBu-y47s7HA9y9M7R9aHrRS1iPf_BxmBP3OaKWolZc9L41datCbJum9agYt2l-TZk6eS2rQ8m9x4KzF7alTHJ2Lk6dE29EHw1XkMF0tmrzYLK0vzPoMh31o-6khhivHMEvl3Bpu0mXNNVZTtI7kYHTpHeB_bifM1bneZ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
وقتی هوش مصنوعی علیه هوش مصنوعی رقابت می‌کند!
در یکی از آزمایش‌های جالب روی مدل‌های
Sol
و
Terra
، رفتارهای غیرمنتظره‌ای مشاهده شد.
🔹
کارتل قیمتی
مدل
Terra
پیشنهاد داد قیمت‌ها را با هماهنگی افزایش دهند، اما
Sol
پس از پذیرفتن پیشنهاد، آن را گزارش کرد و حتی خواستار حذف Terra شد.
🔹
اتهام به رقیب
مدل
Terra
در مرحله‌ای دیگر، برای حذف
Sol
او را به تقلب متهم کرد.
🔹
رقابت بر سر درآمد
مدل
Terra
با کاهش جزئی قیمت‌ها نسبت به
Sol
، مشتریان بیشتری جذب کرد و درآمد بالاتری به دست آورد.
📌
این آزمایش نشان می‌دهد که مدل‌های هوش مصنوعی در سناریوهای رقابتی، گاهی رفتارهایی شبیه رقابت‌های دنیای واقعی از خود نشان می‌دهند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6965" target="_blank">📅 17:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6964">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚀
مدل بی‌نظیر GLM 5.2 به نرم‌افزار Trae اضافه شده؛ کاملاً رایگان و نامحدود!
اگر اهل کدنویسی و دنیای هوش مصنوعی هستید، احتمالاً با
Trae
آشنایی دارید؛ یه ابزار و دستیار فوق‌العاده هوشمند (Coding Agent) که کارش راحت کردن زندگی برنامه‌نویس‌هاست. حالا خبر جدید و جذاب اینه که مدل پرقدرت
GLM 5.2
به این پلتفرم اضافه شده و می‌تونید کاملاً رایگان و بدون محدودیت ازش استفاده کنید.
🤓
من خودم هنوز این مدل جدید رو فرصت نکردم تست کنم ولی Trae کلاً سیاستش اینه که مدل‌های خوب رو رایگان ارائه میده، اما قبلاً یه
صف انتظار طولانی و رو‌مخی
داشت که آدم رو کلافه می‌کرد. نمیدونم واسه این مدل جدید هم همون بساط صف برقرار باشه یا نه!
🌐
لینک سایتش:
🔗
https://work.trae.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6964" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6963">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏
🎙
Voicetypr
ابزار متن‌باز و قدرتمند برای تبدیل گفتار به متن به کمک هوش مصنوعی. جایگزینی عالی برای تایپ صوتی که در پس‌زمینه سیستم‌عامل اجرا شده و همه‌جا در دسترس شماست!
✨
ویژگی‌ها:
*
🔸
تایپ سراسری (System-wide):
با فشردن یک کلید میانبر، در هر نرم‌افزاری (ادیتور کد، تلگرام، مرورگر و...) صحبت کنید تا متن بلافاصله همان‌جا تایپ شود.
*
🔸
آفلاین و امن:
پردازش کامل صدا روی سیستم خودتان (Local) به کمک مدل‌های Whisper بدون نیاز به اینترنت (پشتیبانی از +۹۹ زبان از جمله فارسی).
*
🔸
سبک و فوق‌سریع:
توسعه‌یافته با زبان Rust و فریم‌ورک Tauri با پشتیبانی کامل از پردازشگر گرافیکی (GPU در ویندوز و Metal در مک).
*
🔸
ویرایش هوشمند متن:
قابلیت اتصال به API مدل‌هایی مثل Groq یا Gemini برای اصلاح لحن، یا تبدیل صحبت‌های پراکنده به ایمیل رسمی و کامیت.
🧪
نکته:
این برنامه برای ویندوز و مک در دسترس است. در اولین اجرا، به حدود ۳ تا ۴ گیگابایت فضای خالی برای دانلود مدل پردازش محلی نیاز دارید و پس از آن کاملاً مستقل کار می‌کند (برای لغو سریع فرآیند ضبط، کافیست دوبار کلید
Esc
را بزنید).
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6963" target="_blank">📅 16:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6962">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmEbI0M2B4qUorBGrfIYnRlj59fc5wyuU3Z8IDW_ERoaTNQTx48xW6aw0q7WlVtMHlbn-YQsDX_SLA64QAM1IruG111GiQOjHwK02F_xeLO8f65IEeDJNSm24JUWLSNcxwPPyo2TO8V3J_Lr9CMjcgbC3DPfg4VWMp4-J3bfrKlL5CVKvCcRHvMKPaOiAq2a1UnNC7BcVv4wopLPcJsPTjiiB50ybJgvEjNhF1qTY3m_1DPmRD3q9YfOCTHteVj2h0qlPiwoGa5GNsCQVng3ROg2RqWE0Xv_qtDoYo-ZjbfXXGqiBaXbvAY4tyhts1mPfoCw9GvupmhIxvdeGUzQOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
TelegramOS
پلتفرمی یکپارچه که تلگرام را به یک سیستم‌عامل کامل برای کسب‌وکار شما تبدیل می‌کند؛ تمام ابزارهای مدیریت، پشتیبانی و توسعه در یک داشبورد جامع!
✨
ویژگی‌ها:
🔸
مدیریت متمرکز تیمی:
کنترل همزمان چند اکانت، صندوق پیام مشترک (Shared Inbox) و مدیریت سطح دسترسی اعضا.
🔸
اتوماسیون و CRM:
ساخت سناریوهای کاری (Workflows)، سیستم پاسخگویی خودکار و مدیریت پیشرفته ارتباط با مشتریان.
🔸
آنالیتیکس و مارکتینگ:
ارائه گزارش‌های دقیق از عملکرد، تحلیل کمپین‌ها و دسترسی به مارکت‌پلیس داخلی.
🧪
نکته:
این پلتفرم بهترین گزینه برای تیم‌های پشتیبانی، فروش و بازاریابی است که می‌خواهند تلگرام را به قطب اصلی و خودکار فعالیت‌های تجاری خود تبدیل کنند.
🔗
وب‌سایت رسمی TelegramOS
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6962" target="_blank">📅 16:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6961">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0feee0c240.mp4?token=bfK09raVVkIIznVUAJp0ZPCNUyITg_-HpdWOpMAtTRMBrV8VmeFe6chiGgPMBnRIFtu1HpQjwLQ4jWsqg3eXXsPzxyy9SNLtej1BYbkvZqxUPNeb62Gbgtdvm8tenraNY8B8j6FLUOvKMQbmrwKSd5lB8s9pZJVVwtAboaB_p96kHm4ICiXi5Ogsp3SQbS0kKPjBLcmkxudzygAMkHXBRD5sNMTnsnE4XfpxkA5V2uaFLf9XadNESpEFIzUuT3FkGQlo5626ns6aG7nZ11vvKt1YeE-CiX1NvpV2NZkFOvo52SzBpvr6FopoS9Oq9FosUGhKyxPsaOJKGDYbJY2YsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0feee0c240.mp4?token=bfK09raVVkIIznVUAJp0ZPCNUyITg_-HpdWOpMAtTRMBrV8VmeFe6chiGgPMBnRIFtu1HpQjwLQ4jWsqg3eXXsPzxyy9SNLtej1BYbkvZqxUPNeb62Gbgtdvm8tenraNY8B8j6FLUOvKMQbmrwKSd5lB8s9pZJVVwtAboaB_p96kHm4ICiXi5Ogsp3SQbS0kKPjBLcmkxudzygAMkHXBRD5sNMTnsnE4XfpxkA5V2uaFLf9XadNESpEFIzUuT3FkGQlo5626ns6aG7nZ11vvKt1YeE-CiX1NvpV2NZkFOvo52SzBpvr6FopoS9Oq9FosUGhKyxPsaOJKGDYbJY2YsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
با یک کلیک، طراحی هر وب‌سایتی را کپی کنید!
یک ابزار فوق‌العاده به نام Ditto می‌تواند در چند ثانیه، سیستم طراحی هر وب‌سایت را استخراج کند.
✨
امکانات Ditto:
🔍
فقط کافی است لینک سایت را وارد کنید؛ Ditto آن را تحلیل کرده و نسخه‌ای بسیار دقیق از سبک طراحی‌اش را آماده می‌کند.
🎨
تمام توکن‌های طراحی را به‌صورت خودکار استخراج می‌کند؛ از جمله رنگ‌ها، فونت‌ها، اندازه‌ها، فاصله‌ها، سایه‌ها، گریدها و سایر جزئیات بصری.
📄
یک فایل
DESIGN.md
تولید می‌کند که می‌توانید مستقیماً در Claude، ChatGPT، Cursor، v0 و سایر ابزارهای هوش مصنوعی استفاده کنید.
✨
بدون نیاز به کار دستی، ساختار و سبک طراحی سایت را بازسازی می‌کند.
🔄
حتی می‌توانید سبک چند سایت را با هم ترکیب کنید؛ مثلاً رنگ‌بندی و انیمیشن‌های یک سایت را با تایپوگرافی سایت دیگری ادغام کنید.
👀
نتیجه را بلافاصله پس از تولید مشاهده و در صورت نیاز ویرایش کنید.
📦
امکان خروجی گرفتن برای Figma، کامپوننت‌های React، تنظیمات Tailwind، Storybook، WordPress/Elementor و متغیرهای CSS را نیز دارد.
https://www.ditto.site/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6961" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6960">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">موتور جستجوی مبتنی بر شبکه DHT بیت‌تورنت، که امکان جستجو و یافتن منابع تورنت و لینک‌های مگنتی رو فراهم میکنه
☠
http://cilimo.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6960" target="_blank">📅 14:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6959">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA_nkfy380GcP_L2zddr8Thux_YQCIBBKtfvn_V18P8Jp3gKSKWp5mcK1XCh6Dr2E0b3nAJTVqHfvFEnGmRflzU60bFmGEUVG5nj9Rqn4nHLVAl3Fqj4PIN1cmF8TmdG_9UyCrvNwPmd1nQiVvnMT2cfnso3uRcs5s6dj3jYVe5iYYjtkQODycLFGTrKYBXMZ5bBQ3I6rVXNr1CrXyS7jaovUp6fBzSLT8jONA0gU4dEiekCvr-hTbaOPk663oJ3C3-qdkZcwPNkX9mCokrZPZ17NGdglS0xEbMoeHgX4st38ZGlBfZnsSqthSqN_ZKKbwynRE4k5BA7dhJzktrAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌐
Magnitude Browser Agent
دستیار هوش مصنوعی قدرتمندی که با استفاده از بینایی ماشین (Vision AI) به شما اجازه می‌دهد مرورگر وب را فقط با دستورات متنی ساده کنترل و اتوماتیک کنید!
✨
ویژگی‌ها:
*
👁
معماری بینایی‌محور: برخلاف ابزارهای قدیمی که به کدهای سایت (DOM) وابسته‌اند، این ابزار صفحه وب را مثل یک انسان می‌بیند و با مختصات پیکسلی کار می‌کند.
*
🖱
تعامل و اتوماسیون کامل: کلیک، تایپ، و جابه‌جایی المان‌ها (Drag & Drop) در پیچیده‌ترین سایت‌ها.
*
📊
استخراج هوشمند دیتا: توانایی خواندن و استخراج داده‌های ساختاریافته (بر اساس Zod Schema) مستقیماً از روی ظاهر سایت.
*
✅
تست‌رانر داخلی: ابزاری فوق‌العاده برای تست خودکار وب‌اپلیکیشن‌ها با بررسی و تأییدیه بصری (Visual Assertions).
🧪
نکته: این پروژه در بنچمارک WebVoyager امتیاز خیره‌کننده ۹۴٪ را کسب کرده است. برای بهترین عملکرد، به یک مدل بینایی قدرتمند مثل Claude 3.5 Sonnet یا Qwen-2.5VL 72B نیاز دارید. نصب اولیه به سادگی با دستور npx create-magnitude-app در ترمینال انجام می‌شود.
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6959" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6958">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyZM_0LbpnoZlnzzzjmxa_bCFNwZH5Gvqs-fsZGioF482FmIscVO-MElgj5b3HxCMBgVrA4FRRYb4isGXAjpmeIEN-FaOzDbXqZyLdT5fzubiAAKVVpq_daAu0e9O8rPxnl7yPj-0B47Bqd-XR2DTHgV1DrZJAkqDUWKcN2kMfExD5IpTFNY4HOkBcSWF-8ajYCGKDoJ7ItCDA16okAP8kB0lW4JjoWhM390_mUEoKfZ435jRg3_RMGt2ONIrvvxG-dlmfhfOl4f_OLMirAIgBzKON9tADQw6-N4lX7TH21Yt6oMN92cff4_ev04hrxXIpq7rLz9gRIXbMeGLSnG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار چندمنظوره رایگان برای ویرایش صدا، عکس و ویدیو
سرویس
Magic Hour
مجموعه‌ای از ابزارها و فناوری‌های هوش مصنوعی کاربردی را برای انجام هر نوع وظیفه‌ای گرد هم آورده است:
🔹
تولید تصاویر، حذف پس‌زمینه و افزایش کیفیت تصاویر؛
🔹
ویرایشگر دیپ‌فیک با قابلیت
جایگزینی افراد در ویدیو
؛
🔹
بازسازی عکس‌های سیاه و سفید + جایگزینی افراد در تصویر؛
🔹
مجموعه‌ای از ابزارها برای کار با موسیقی و فایل‌های صوتی؛
🔹
تولیدکننده زیرنویس.
🌐
magichour.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6958" target="_blank">📅 11:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6957">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">۱۰۰ گیگ کانفیگ اهدایی
🔥
vless://63dc39fe-3bc3-4267-8bf1-4069b47baa18@194.110.172.150:443?encryption=none&fp=chrome&pbk=3sRLbKljY5s7LCik-w9MqgenayhgHgLV0v9lmFGQ9TQ&security=reality&sid=3094219d2cfd2b3d&sni=www.samsung.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/6957" target="_blank">📅 11:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6956">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏
🤖
3xui-telegram-bot
ربات قدرتمند و متن‌باز تلگرام برای فروش خودکار سرویس VPN، با اتصال مستقیم به پنل 3X-UI. با این ابزار تمام فرآیندهای فروش، تمدید و مدیریت اکانت‌ها بدون نیاز به دخالت دستی ادمین انجام می‌شود!
✨
ویژگی‌ها:
🛍
فروش خودکار سرویس با حجم دلخواه، شارژ کیف پول (کارت‌به‌کارت) و پشتیبانی از چند سرور (Inbound)
🎁
مجهز به سیستم ساخت کد تخفیف، ارائه تست رایگان و زیرمجموعه‌گیری (Referral)
💻
دارای ابزار اختصاصی خط‌فرمان (vpn-bot) برای نصب سریع یک‌خطی، بکاپ‌گیری و آپدیت
🔐
اتصال کاملاً امن به پنل صرفاً از طریق API Token (بدون نیاز به یوزرنیم و پسورد پنل)
🧪
نکته:
مدیریت کامل ربات اعم از تغییر قیمت‌ها، تایید یا رد پرداخت‌ها، و مشاهده آمار، مستقیماً از طریق دستورات داخل تلگرام توسط ادمین انجام می‌شود. همچنین برای سرورهای ایران، امکان تنظیم پروکسی SOCKS5 نیز تعبیه شده است.
📥
دانلود و آموزش نصب در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6956" target="_blank">📅 11:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6954">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEBiZwTjE4eVREzKtsibDimLcx8LSzao56upKVu2HXMnJLl6iL8YItXE7f-JI1fFlGcyyjFZ9jC2YNcgfaNmQ6XM3QqMzJjgzHJAUVrSlORhrFYzDRGUp3UMfW_OyLLIdl4UiMaxxo-5JqjzCjS255yDURdD_m_kENIjRqU9ffMGA7GCGMow-LKCET4-nBsGfH8zjTkcW3-0Q6POl4pYKuPH1lGM_FBX_LodROhVonqTggxBHXJWYEh8KYTgGCbe5xtib4_uO2sTIO-m2_KOX0RjjBL-oaD8PZeeL7pNSBxIQUEYjonJBx6rsSEWy8yhL5p9Fiivjawy9qcU12nqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌐
BrowserOS & BrowserClaw
دو مرورگر متن‌باز؛ یکی برای شما، یکی برای هوش مصنوعی!
✨
ویژگی‌ها:
‏
🤖
BrowserClaw:
اتصال کلاینت‌های AI (مثل Cursor) برای انجام خودکار کارها روی اکانت‌های واقعی شما.
‏
🧑‍💻
BrowserOS:
مرورگر امن با دستیار AI داخلی و پشتیبانی از مدل‌های لوکال (Ollama).
🎥
ضبط ویدیویی تمام اقدامات هوش مصنوعی برای بازبینی.
🧪
نکته:
هوش مصنوعی در تب‌های کاملاً ایزوله کار می‌کند و هیچ تداخلی با وب‌گردی شما ندارد.
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6954" target="_blank">📅 10:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6953">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏
🚨
حذف ناگهانی دامنه
t.me
از DNS جهانی!
دامنه
t.me
(هسته اصلی زیرساخت لینک‌های تلگرام) به طور ناگهانی از سیستم DNS جهانی ناپدید شد! رجیستریِ پسوند
.me
وضعیت این دامنه را روی
serverHold
قرار داده که باعث شده هیچ‌کدام از لینک‌های تلگرامی در سراسر جهان در مرورگرها باز نشوند.
✨
جزئیات ماجرا:
*
📱
اپلیکیشن‌های موبایل و دسکتاپ تلگرام همچنان بدون مشکل کار می‌کنند و این قطعی صرفاً مربوط به لینک‌های وب (آدرس کانال‌ها، گروه‌ها و ربات‌ها) است.
*
💎
ضربه سنگین به اکوسیستم کریپتویی تلگرام و مختل شدن دسترسی کاربران به کیف‌پول داخلی (Wallet) و مینی‌اپ‌های مرتبط با شبکه TON.
*
🌐
دامنه موازی
telegram.me
همچنان فعال است؛ این یعنی محدودیت منحصراً روی آدرس کوتاه
t.me
اعمال شده و کل زون دامنه‌ها مشکلی ندارد.
🧪
نکته:
با اینکه اعتبار این دامنه تا سال ۲۰۳۵ تمدید شده، اما رجیستری کشور مونته‌نگرو (صاحب دامنه‌های .me) بدون هیچ اخطار قبلی آن را از دسترس خارج کرده است (پاول دورف در پلتفرم X مستقیماً از آن‌ها خواسته مشکل را حل کنند). این اتفاق زنگ خطری جدی برای شرکت‌هایی است که زیرساخت حیاتی خدماتشان را روی دامنه‌های ملی بنا کرده‌اند!
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6953" target="_blank">📅 10:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6952">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1Nl56he7b4VUWefnAnb-6GjBgp5H3LZpwdvsRsLnbC70w2qBPYCEF1KRhXZBC1FGfH6p3XMNXHCEA0PwbU3IQg-z_cKd-rAaJxHGjI-RJJ7HESZ2fkzjwn6Qrrz8IJydLCzfp2q3xuXdxbbuv-2fk3BWyqNiNwKr-tsjmluDyZzG2JHpG6xjsTLOG52dQpby3b5ZWnfSIzojga9VS9Noa1EZNsB9i1ctKk3xjB-nv0kMBgbRs76-3AUOnM4auuIkUe0AqhpEzlwwpUhHEcFYvV57NON0fsOXXLsxbzqfhfCiUsYMzLzocD50aIIdzcdkz6n6Oy4rTvWesz_BxLzCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛ Google AI Studio حالا به GitHub وصل
میشه
🔥
با قابلیت جدید Import from GitHub میتونید ریپازیتوری‌های خودتون رو مستقیم وارد Google AI Studio کنید و با کمک Gemini روی کدهای موجود کار کنید.
✨
امکانات جدید:
•
📂
وارد کردن پروژه از GitHub
•
🤖
سازگارسازی خودکار کد برای اجرا
•
✏️
ویرایش و ادامه توسعه پروژه
•
👀
پیش‌نمایش و Deploy سریع‌تر
⚠️
فعلاً اتصال یک‌طرفه است و تغییرات به GitHub برنمی‌گرده؛ اما همگام‌سازی کامل در حال توسعه است.
https://aistudio.google.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6952" target="_blank">📅 09:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6951">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfkCb5wT2TT0JaZlf9mk9Cmwt8h-6YwLKpFjMxAf6BxJCr-kkgXcAA51ZDuDadd6kiLX0SMaeOpaWMfUeroIurvGuBrJcB6uUxfztTKxYflaYPOsicKL_DtlICg6hxe5SS3ZpuJY1sj4z3zgpZvXXyKPxWzBtDQydz-LbvhXGZoRPND0wM9rkbN6-4l6nr7NzZyawkFTN7WJkNEILqYfT0EXCSUXiTtGqPAAo3cgA4SBVmPsL5y2uPpvQgnfRy9DIiHcTphamSDdOW_50doEaqCmgSF7_rtub-BWTHRNCMdfS4EjNcdnM7q_tB1DBoTGuV-xN0x30sjaMI8irys77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
بیش از ۳۹۰۰ پرامپت آماده در ۱۶ دسته‌بندی مختلف، از جمله:
• تولید محتوا و نویسندگی
• برنامه‌نویسی
• بازاریابی
• طراحی و تولید تصویر
• آموزش، کسب‌وکار و...
https://xueprompt.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6951" target="_blank">📅 08:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6950">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184a52dda.mp4?token=uIBoPMsfzjm3UK5g4CZsMCgsTote1hIWPRO-Fhr2Obbq5OKGdgcI1m0eD9Nh9kh34YOs1Erxn6p9fUL0iCd7H_Z3GfEEi4CEsDcu_TwUQ48Trxb-3BjNeDbr2DF5GeJdV3J1XAW6bagbJQXrlH236cNeMb-_QZq-zP_p-vEvAPR2Fhf0FUhbqX6nkhFzL0H2uwP4Nflp2hZ6BWDubYjwD53di3__EuJzGwP9NOX4lXEnrYWpGx62HR1WSgv2YiI-YcotQWe-TSVxBnAKgKGDaGbRKOYHECfxAbN88r5qc_hS5Ylk7fWx-aW0rzhrsqiMVjzbekO0M_H7IK7Zy990CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184a52dda.mp4?token=uIBoPMsfzjm3UK5g4CZsMCgsTote1hIWPRO-Fhr2Obbq5OKGdgcI1m0eD9Nh9kh34YOs1Erxn6p9fUL0iCd7H_Z3GfEEi4CEsDcu_TwUQ48Trxb-3BjNeDbr2DF5GeJdV3J1XAW6bagbJQXrlH236cNeMb-_QZq-zP_p-vEvAPR2Fhf0FUhbqX6nkhFzL0H2uwP4Nflp2hZ6BWDubYjwD53di3__EuJzGwP9NOX4lXEnrYWpGx62HR1WSgv2YiI-YcotQWe-TSVxBnAKgKGDaGbRKOYHECfxAbN88r5qc_hS5Ylk7fWx-aW0rzhrsqiMVjzbekO0M_H7IK7Zy990CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧰
۳۰۰+ ابزار رایگان، فقط در یک سایت!
📄
ویرایش، ادغام و فشرده‌سازی PDF
🎬
برش و ادغام ویدئو
✍️
ابزارهای متن و نگارش
💻
ابزارهای کاربردی برنامه‌نویسی
🔑
ساخت QR Code، رمز عبور و داده‌های تصادفی
💰
ابزارهای مالی و محاسباتی
https://footrue.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6950" target="_blank">📅 08:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6949">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📶
دسترسی به لیست سرورهای عمومی VPN
مجموعه‌ای از کانفیگ‌های
V2Ray
،
Trojan
و
Outline
VPN
که سرورهای جدید و سالم به‌صورت مداوم به لیست آن اضافه می‌شوند
🤔
🔗
نیازی به کپی تک‌تک سرورها نیست؛ فقط
Subscription Link
مشخص‌شده را کپی کرده و مستقیم داخل کلاینت خود وارد کنید.
V2Nodes
🌟
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6949" target="_blank">📅 01:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6947">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">برای احتیاط ام شده برنامه های ضروری رو آپدیت کنین که خیره
🌑
Slipnet
📂
WhiteDns
📂
Resolver
📂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6947" target="_blank">📅 01:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6946">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRseyFGHRXuUL2-QA4uLFwmofP0uoNSsYWwGscmUGjgiBCpRehXBpHbxJ_ZGUTDMELyrap91xI9dzxy72KoVgT1fgSjQqLxsAREvIUFJSOrvUk-_KC1oiry6a9J4KC0y3kcfoHzOJ2y11sDAgAHQHgN5omrxtUVAtxLB64UwR04Y5XqG8eNP6tjmvqB_jJbHpzsAI8AxXjYicXX65h52l7Iv0eoLjdxJqlWicUY79quBBu84gW1Ln7N01MMADzy0uC0ph8eykT_ye2LogyHDQOPlxJWsTA1lUt7tB0MpnXIcyXDfRQSnnp6T_gaOqNFUBHW7gPylZ_WGbfLJ2o_sJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🖼
Image-to-Text OCR
ابزار تحت وب و متن‌باز ساده و کاربردی برای استخراج سریع متن از داخل تصاویر به کمک تکنولوژی OCR (ایده‌آل برای تبدیل عکسِ اسناد و نوشته‌ها به متن دیجیتال قابل ویرایش).
✨
ویژگی‌ها:
🔸
استخراج دقیق و سریع متن از هر نوع تصویر
🔸
توسعه‌یافته بر پایه تکنولوژی‌های مدرن Vue و Nuxt3 و TypeScript
🔸
رابط کاربری تحت وب، بسیار سبک و بدون نیاز به نصب نرم‌افزارهای سنگین
🔸
کاملاً متن‌باز (Open-Source) با لایسنس AGPL-3.0
🧪
نکته:
برای راه‌اندازی این پروژه روی سیستم خودتان (لوکال)، پس از کلون کردن ریپازیتوری کافیست دستور pnpm dev را اجرا کنید تا برنامه روی پورت 3000 در دسترس قرار گیرد (بیلد نهایی نیز با pnpm build در پوشه dist ساخته می‌شود).
📥
دانلود سورس‌کد از گیت‌هاب
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6946" target="_blank">📅 23:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6945">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏
🤖
آموزش کامل و به‌روز راه‌اندازی NipoVPN
این ابزار با پنهان‌سازی ترافیک واقعی داخل درخواست‌های جعلی (Decoy/Fake HTTP requests)، به‌راحتی از سد فیلترینگ پیشرفته عبور می‌کند.
⚙️
۱. نصب روی سرور (VPS)
به سرور اوبونتو یا لینوکسی خود متصل شده و نسخه جدید را نصب کنید:
Bash
wget https://github.com/MortezaBashsiz/nipovpn/releases/latest/download/nipovpn.deb
sudo apt install ./nipovpn.deb
📂
۲. ایجاد مسیر لاگ‌ها
Bash
sudo mkdir -p /var/log/nipovpn/
sudo touch /var/log/nipovpn/nipovpn.log
📝
۳. ویرایش فایل کانفیگ
فایل
/etc/nipovpn/config.yaml
را با ویرایشگر باز کرده و مقادیر زیر را به دقت تنظیم کنید:
tlsEnable:
برای امنیت حداکثری این گزینه را روی
true
نگه دارید و پورت را
443
تنظیم کنید. (امکان استفاده از پورت 80 و HTTP معمولی هم وجود دارد).
fakeUrls:
چند سایت معتبر و بدون فیلتر (مثل
google.com
) اضافه کنید.
token:
یک رمز امن و طولانی (حداقل ۳۲ کاراکتر) برای ارتباط کلاینت و سرور بسازید.
🚀
۴. تنظیم فایروال و استارت سرویس
ابتدا پورت انتخابی (مثلاً 443) را در فایروال باز کنید:
Bash
sudo ufw allow 443/tcp
سپس سرویس را فعال و ری‌استارت کنید (بعد از هر تغییر در کانفیگ، ری‌استارت الزامی است):
Bash
sudo systemctl enable nipovpn-server.service
sudo systemctl restart nipovpn-server.service
جهت بررسی لحظه‌ای لاگ‌ها و اطمینان از اجرای بدون خطا:
Bash
tail -f /var/log/nipovpn/nipovpn.log
📱
۵. تنظیمات کلاینت (گوشی)
کلاینت رسمی
NipoVPN Android
(در گیت‌هاب) یا اپلیکیشن
سیمرغ (SIMORGH)
را نصب کرده و اطلاعات آی‌پی سرور، پورت (443)، توکن و آدرس جعلی (Fake URL) را دقیقاً مطابق سرور وارد کنید. کلاینت اندروید بسیار بهینه است.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6945" target="_blank">📅 22:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6943">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏
🚀
SulgX Panel
پنل مدیریت اشتراک VLESS فوق‌سبک و شخصی، ساخته شده تماماً با پایتون (FastAPI و SQLite).
✨
ویژگی‌ها:
🛡
مدیریت کامل کانفیگ‌های VLESS (WS+TLS) با پشتیبانی از Fragment و SNI اختصاصی
📊
مانیتورینگ زنده مصرف ترافیک، محدودیت حجم و زمان انقضا برای هر کاربر
☁️
بهینه‌سازی شده برای استقرار (Deploy) رایگان و ساده روی پلتفرم‌هایی مثل Render و Railway
🤖
دارای ربات تلگرام هوشمند دو زبانه و سیستم ضد-خواب (Anti-Sleep) سرور
🧪
نکته:
این پنل کاملاً رایگان و اوپن‌سورس است و به راحتی از طریق فورک گیت‌هاب و Dockerfile قابل راه‌اندازی است.
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6943" target="_blank">📅 18:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6942">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">archive-scanner_v1.0.4.apk</div>
  <div class="tg-doc-extra">10.4 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6942" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر آیپی تمیز کلودفلر آخرین اپدیت
دوستانی که نسخه قبلی رو داشتن هم میتونن از تو برنامه آپدیت کنن هم با این فایل
سرعت اسکن خیلی بالایی داره، دقتش بالاست و ui کاملا ساده و سریعی داره
🔎
Findings:
❌
Detection: 0
⚠️
Suspicion: 0
✅
Not detected: 67
• File name:
archive-scanner_v1.0.4.apk
• File format:
Android
• File size:
10.43 MB
•
VirusTotal link
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6942" target="_blank">📅 17:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6939">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMaHaQ1TES0Q_060zEK5CzNWLsoj8-TFuBkM4l1XXGTK1K-GXamTDsogh4CRKUKd0HZJL4B3RzzeYmTGIihilM1Hj4nNvzrQxk9WA0sWB4Y1Ux2NHUHQkfckcVkvv9VpOfmOaGHDlt2ZM58SxOs6GL-cXJWqSDhva6-ZATBGS4gRMl5X3Mbn0iJz9WduwOSJDSY7OKiX9N3dgdDhW8Fp-BBqnu4AL9hXS7_ZD8mWwpBwGJUrAWhBDnlqhitZbknAFJJEHfn3qVkGgHIKQvmXelauhmTvghYQSwCp1EDxBX8ScAXKa-i9rKOElu7-9xk6aVupFYaKfmqBJCOgKc6txg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thOXRrmQd09W8Pk9zFeWYk5r5511Wy9RKi_J5FYlHl4_gf6R1BssRbB8eWIMARgFUc8ap5xlzhP7vdLgTKwISzrmPDaVD93g7BVkfhfDPuB-VSkwE57Lgj1qIYi_dJ8GDMwQM-8SWA84LTgUBglhOq_NNvVoB7S9BNP2ROBVhPYYuT6R-KgXg3jepjuI09rH7FzlCxkNO9bf9gvbAoCoqtQfofj9x6LrDRHQYOL00H6pEK5HKW34cmgnQZyejCpAXZGL1TqlRV6iy0tr55Q9Pt3uv8HTPJ4tx0i6PjJqTZuij8Y4Wo6SGPEyG1ZtcVNfYoYcA9NbWq2PW8k8HcAtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MX8IlhWs1JsqVnMTPifkPg2uTsH65W6O2RoimaSZMAw4Uaqee_PC4CnjB9zYGP0czCJBH-4ZlArZA2IuRnOcL6JDqCj4ulibLNe29oG11msH6vI5tHkhQqe-Tl7s9FdY98VE0XIdOF6uIrlpbcya4Dp0NBsbwQJKhn7CM4n61tG63OpPgRmTJvdLA4DlE4wxko1xHn9lYod19we_9EiCR5h_RIkRl-CyydsZ-uDdGK_Rv9BqLiTWj4KSx8vzfQ1vl_gI2dsOd6wP6Nf-GQ3v2yx99r7NsPLP3RU0gHV2moVXbtQANXX8k1SduVxT0Vs5pQ0-s1E-nAaIeK0E0T4Hmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
؛Archive Scanner v1.0.3 منتشر شد!  جدیدترین نسخه‌ی Archive Scanner با بهبودهای مهم در دقت، سرعت و امکانات منتشر شده است.
✨
تغییرات مهم:
⚡️
اصلاح کامل تست سرعت دانلود (اندازه‌گیری دقیق‌تر و عبور از فیلترینگ SNI)
📤
اضافه شدن تست سرعت آپلود برای هر IP
🤖
ساخت…</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6939" target="_blank">📅 17:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6938">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">📱
؛NipoVPN Android کلاینت رسمی اندروید برای پروژه NipoVPN؛ یک ابزار پروکسی و ضدسانسور قدرتمند که ترافیک واقعی HTTP/S شما را در دلِ درخواست‌های جعلی (Fake HTTP Requests) پنهان می‌کند.
✨
امکانات:
🧩
توسعه مدرن: برنامه‌نویسی شده به‌صورت کامل با زبان Kotlin و…</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6938" target="_blank">📅 16:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6936">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نت من ترکید
ی اعلام وضعیت کنین</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6936" target="_blank">📅 15:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6935">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
🔥
ChatGPT Work
اوپن‌آی با معرفی قابلیت انقلابی Work، آینده هوش مصنوعی را تغییر داد. این سیستم دیگر فقط یک چت‌بات ساده نیست، بلکه یک دستیار هوشمند (Agent) است که کارهای پیچیده و چندمرحله‌ای شما را از صفر تا صد، به‌صورت خودکار انجام می‌دهد.
✨
ویژگی‌ها:
🧠
تکیه بر موتور GPT-5.6 و Codex:
ترکیبی بی‌نظیر برای اجرای کارهای سنگین تحلیلی، برنامه‌نویسی و چیدن خروجی‌ها.
📄
خروجی‌های زنده و واقعی:
ساخت مستقیم ابزارهای کاربردی مانند شیت‌های اکسل، اسلایدهای آماده ارائه، اسناد و حتی وب‌سایت‌های تعاملی.
⏰
اتوماسیون و زمان‌بندی:
هندل کردن خودکار وظایف تکراری در زمان‌های مشخص (مثل چک کردن روزانه قیمت‌ها یا خلاصه‌سازی پیام‌های تیم).
🖥
کنترل مستقیم دسکتاپ (Computer Use):
قابلیت تعامل با سیستم دقیقاً مثل یک انسان؛ کلیک کردن، تایپ و جابه‌جایی فایل‌ها برای انجام کارهای پیچیده.
🧪
نکته:
امنیت این سیستم کاملاً تحت کنترل شماست. دسترسی‌ها را خودتان تنظیم می‌کنید و برای اقدامات حساس، سیستم حتماً از شما تاییدیه (Approval) می‌گیرد.
🔗
وب‌سایت رسمی OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6935" target="_blank">📅 14:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6934">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPDHFFIxaVTIWGGOLes1Z8el7bRo-YBCrF6bXkvdgDJggEXxDBi_dqn-gARchYoCNXkt7pg7wZa6R21Et5Sqc3x1vP2_U0F4rSF-7lZxHOQx07S_nd5eyf5fRw9_cFbs1K-tIZufyUaV3ccRSLKX7shpxPatxKbYKxmNsiIieJEIazFXD8owvNhwpFrjcfjWPH4dMURXeL6T2-_5i8SJawf8SMekjZVkWkp8j_VbfEWxboXrx1YdUOLMlDAMSwHyXvfT7nF0Qx4mBk3NUZ2JOzTXN_cA91BQ-2WBX5r_YUQObGTNB5jbY92q67nJ2RG4_RJD2bcPXYDEBvitvjdPeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🕵️
3D Investigation Board
یک برد کارآگاهیِ تعاملی و سه‌بعدی (مبتنی بر GPT-5.6 و Fable 5) که به شما اجازه می‌دهد اطلاعات و سرنخ‌ها را دقیقاً مثل فیلم‌های پلیسی روی یک بورد مجازی مدیریت و تحلیل کنید.
✨
ویژگی‌ها:
📸
امکان اضافه‌کردن انواع شواهد، اسناد، یادداشت‌ها و عکس‌ها روی برد
🧵
اتصال بصری سرنخ‌ها به یکدیگر با نخ‌های سه‌بعدی و فیزیک واقع‌گرایانه
🧠
کشف هوشمند ارتباطات پنهان بین داده‌ها به کمک تحلیلگر هوش مصنوعی
🧪
کاربردها:
این ابزار خلاقانه، نه‌تنها برای حل پرونده‌ها و معماها، بلکه برای داستان‌نویسی، ایده‌پردازی و برنامه‌ریزی پروژه‌های پیچیده فوق‌العاده کاربردی است.
🔗
مشاهده ویدیو و آموزش کامل در X
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6934" target="_blank">📅 13:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6933">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTvy8tZm1l4_AJkallzKkyoU_I2jdNoT8VsncBEHtIbiGZW3K9AKB8v4nzOpDhnvks4ax_dcSiVc1D0TFgY8sVxUf6mFuSPFr7gbyrOw6ckpE9m7O6ICkKJzPPHlmhTREK9_ETjjoRUnB6TCeWFQm6tIpDt741e40fPTWBSABnyd8NhzT05ksBiTjMQrmvDuxip3khv00ohyqbeDTxzB67j4RmlToSDmW3ao1VnYNW7nXBhl9hKPXgoRdZRdfV0BiFC5kZWV8_MxVeqj-aD1uEcPbpaybLMTQlXip4-mXXYJ_evKAogMdJYEgK--wxYSbZwccFiEd6Jjv4-R8JB2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤖
OMG-Agent
کلاینت دسکتاپ متن‌بازی که به هوش مصنوعی اجازه می‌دهد گوشی اندرویدی شما را فقط با دستور متنی کنترل کند! (مثلاً: «تلگرام را باز کن و به
⚡
Bachelor پیام بده»).
✨
ویژگی‌ها:
🧠
پشتیبانی از مدل‌های هوش مصنوعی موبایل (مثل AutoGLM) و APIهای OpenAI
📱
اجرای خودکار دستورات با تحلیل لحظه‌ای صفحه گوشی (از طریق ADB)
💻
سازگار با گوشی‌های فیزیکی اندروید و شبیه‌سازها (Emulators)
🧪
نکته:
پیش‌نیاز این ابزار، نصب ADB، کیبورد ADB و فعال‌سازی USB Debugging روی گوشی است.
📥
دانلود و راه‌اندازی از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6933" target="_blank">📅 13:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6932">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏
🚀
۴۰۰۰ دلار کردیت رایگان API
هدیه‌ای ویژه برای برنامه‌نویس‌ها! دسترسی سریع به قدرتمندترین مدل‌های هوش مصنوعی دنیا برای پیشبرد پروژه‌های کدنویسی شما.
✨
ویژگی‌ها:
🧠
پشتیبانی از مدل‌های برتر جهان (GLM 5.2 ،Qwen 3.7 ،Deepseek 4 Pro ،Minimax M3 و Kimi k2.6)
📧
ثبت‌نام سریع و کاملاً بی‌دردسر با هر نوع ایمیل
💻
سازگاری کامل با انواع کلاینت‌ها
🧪
نکته:
مصرف کردیت در این سرویس‌ها با ضرایب بالایی محاسبه می‌شود؛ پس حتماً در استفاده از توکن‌هایتان دقت و مدیریت لازم را داشته باشید.
🔗
لینک ثبت‌نام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6932" target="_blank">📅 13:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6931">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g43AyXlRFjujRpat9xRkhAkY6jNxsE77vi0-dMmkhMuo7b4qag1pFVxOF4OHA9GKQGEsug8ga2hg001zhCpNBDAtSkXMQFTD-xo-YaA6Aze4E-c0n_EGWlfrn1P2IpNAiPc8ce9rTDUSAQQPvm_JN5jfdHFdOcWKmRyb2GeLXodZh01Dwl_dkCSABeA6GwiwMudEXF2U56i2uZk1QjVmHd0zgWGyk5Dv__--ZwiO9A8iatSzXV1E5LDh8YiPhhJOvzmN5dLR11N5SOmrxlZEMVxKVTsTLt6_U8P5Hu-juRBOKQT9Z5tA0OlaeaDGKhnkzlCXaEzjbA6DIHSA7Wu4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⭕️
Colibri
پروژه قدرتمند و متن‌بازی که با C خالص نوشته شده و اجازه می‌دهد مدل‌های عظیم هوش مصنوعی را تنها با اختصاص ۳٪ از حجم کل مدل به رم (RAM) اجرا کنید!
✨
ویژگی‌ها:
🔸
اجرای کامل تنها با یک فایل C (حاوی ۲۴۰۰ خط کد)
🔸
کاملاً مستقل از پایتون، کتابخانه‌های جانبی و کارت گرافیک (GPU)
🔸
ساخت API لوکال سازگار با OpenAI (تنها با دستور coli serve)
🔸
اجرای مدل سنگین 744B (که در حالت عادی ۷۳۰ گیگابایت رم می‌خواهد) تنها با ۲۵ گیگابایت رم!
🧪
نکته:
برای کاربران ویندوز، استفاده از WSL2 پیشنهاد می‌شود. به عنوان مثال، لود یک مدل ۳۷۰ گیگابایتی تنها ۳۰ ثانیه زمان و ۹.۹ گیگابایت رم نیاز دارد (البته به دلیل عدم استفاده از گرافیک، سرعت پردازش حدود ۱ توکن بر ثانیه خواهد بود).
📥
دانلود از گیت‌هاب
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6931" target="_blank">📅 12:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6930">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">📈
؛
Vibe-Trading
دستیار هوش مصنوعی شخصی و متن‌باز برای ترید و تحلیل بازار. کافیست ایده‌هایتان را به زبان ساده بنویسید تا خودش برایتان استراتژی معاملاتی بنویسد و بک‌تست بگیرد!
✨
ویژگی‌ها:
🧠
تبدیل مستقیم پرامپت‌های متنی به کد استراتژی، تحلیل بازار و دریافت بک‌تست‌های دقیق
🐝
تشکیل تیم‌های مجازی هوش مصنوعی (ایجنت‌های ریسک، کریپتو و کوانت) برای مشورت و بررسی همه‌جانبه ایده‌های شما
👥
سیستم جالب Shadow Account: ژورنال معاملاتتان را آپلود کنید تا هوش مصنوعی خطاهای احساسی و رفتاری شما را در ترید پیدا کند
📊
پشتیبانی یکپارچه از بازارهای جهانی (کریپتو، سهام و فارکس) با دریافت خودکار دیتا
🧪
نکته:
این ابزار با پایتون توسعه داده شده و به‌راحتی به API مدل‌های مختلف (از جمله Groq ،DeepSeek و OpenAI) متصل می‌شود. برای دیپلوی روی سرور شخصی یا اجرای لوکال فوق‌العاده است.
📥
دانلود و نصب از گیت‌هاب (PyPI / Docker)
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6930" target="_blank">📅 12:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6929">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
🐋
Orca
محیط توسعه و هماهنگ‌کننده (Orchestrator) فوق‌العاده قدرتمند برای مدیریت همزمان چندین ایجنت هوش مصنوعی برنامه‌نویس. یک دستیار همه‌چیزتمام برای توسعه‌دهندگان!
✨
ویژگی‌ها:
🤖
اجرای همزمان ایجنت‌های مختلف (مثل Claude، Codex و Grok) روی یک پرامپت و مقایسه خروجی‌ها
📱
دارای اپلیکیشن موبایل (iOS و اندروید) برای کنترل و هدایت ایجنت‌ها از راه دور
🎨
مرورگر توکار (Design Mode) برای انتخاب المان‌های سایت و ارسال مستقیم HTML/CSS آن به هوش مصنوعی
🔗
اتصال بی‌نقص به گیت‌هاب، پشتیبانی از محیط‌های ریموت (SSH) و ترمینال‌های قدرتمند داخلی
🧪
نکته:
این نرم‌افزار متن‌باز است و تقریباً از هر ایجنت مبتنی بر CLI (مثل Cursor ،Copilot و OpenCode) پشتیبانی می‌کند. کلاینت دسکتاپ آن برای ویندوز، مک و لینوکس کاملاً رایگان در دسترس است.
📥
دانلود از گیت‌هاب (بخش Releases) یا سایت رسمی (onOrca.dev)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6929" target="_blank">📅 11:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6928">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN88JB2kEvg7rYLo8nNLp83kZ0vW_wbuZKrM7yKK71xG9jA_d7sgLnkVQuC-9IKuz3Yzofu8R5GuXb6RDgJH_vZiJZRHr1OgUcq_ITbO-luiJTi8gDUi2wuEZP61xPDoiwAssbL9TWeAoqrraWikcJdeUotk_xKTSmfY0JLYReUbc8tX56epzLX9H9R6EHV5nOPmfskJMhRB9LSLih1qj9MLOFIJ8kqLMlVE_jr3ZxWaBAkUOkv3s1LpS7r05lKoKQMssgxGaSzYT6geSQHGymrmN7DyoKhsHwx_IEIKstjMdbe1C3W1NtfN6P1jgRA3EMYtvphzwU7y6QCWJMf3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هر عکسی رو به پرامپت تبدیل کن!
؛Convly AI Image-to-Prompt تصویرت رو تحلیل می‌کنه و در چند ثانیه یک پرامپت کامل و قابل ویرایش تحویلت میده.
✨
مناسب برای:
• پیدا کردن پرامپت یک AI Art
• بازسازی استایل عکس‌ها
• استفاده در Midjourney، Stable Diffusion و سایر مدل‌های تولید تصویر
✅
بدون ثبت‌نام
✅
بدون واترمارک
🪙
رایگان
https://convly.ai/image-to-prompt/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6928" target="_blank">📅 11:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6927">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pC16-Wk_M2IUgqfSoiS-zHZxWVUokB6UfPGdvpdZtW_lpcyT1k9o44YKElH9QP1l1Ua3e9BqsuajxVDaZra4BcIPTJLnus9osJ25GmAyS6DSnuRgQcP8TOODB-k1fXycBJLw94In68lvBm7yZkQqc7jWvOnqcpWWWdIFyisj7wzanYtognFzUjH7xsmdEkwHVqexTlh9Ew0YaK5EwfJS7isomFNw_XJkNszm0SOo0oGAKct9e8GONVHilNst6ncJ27-X5wpfaTttxuTwP15S3pLHhTGTr-rZo3kcWfJTATX2gmX-T6Xx2QRmt5vRgsRCisozZ8R0sFrZxhXCkZbriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
بازی خودت را با هوش مصنوعی، در چند دقیقه بساز!
فقط ایده‌ات را بنویس؛ هوش مصنوعی بقیه کارها را انجام می‌دهد.
✨
بدون کدنویسی
🌐
اجرا مستقیم در مرورگر
🎯
آماده برای بازی و اشتراک‌گذاری با دوستان
https://codewisp.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/6927" target="_blank">📅 09:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6925">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFjOsNL4eZF1jFAM82mMMAcER4Bht0S0sC0QbYyWItQ5UIE5PVZzoUnEUguMnFmCKGH7coOTjedofNfGJNpJzIuk362X2LGxYd0Yr8sXTX5LqqpixeH12uKYD0dp1hTWKRuV4F4pCv3xTmvTMLkhyn0Z_YLlkYhshmULOmjZsInwIqgDGSKYc00evzUF7DLb9OuFE-en10SfIq8i4Cmgwc-ZMZVlB_hcxtv2hBNhW2twW4V3GxK7fdcSSGekC9wHWxYFdB94-L0J8I4DRCmVTNnvlA1mINejb4fMPzVdDyhoykWN_-sFDIfXAonZ6RRxKLcjAIBHiihGBoAyUTBV_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧩
؛
Hermes Browser Extension
افزونه‌ای حرفه‌ای برای مرورگرهای مبتنی بر کرومیوم که وب‌گردی شما را با رعایت سخت‌گیرانه حریم خصوصی، مستقیماً به محیط هوش مصنوعی Hermes Agent متصل می‌کند.
✨
ویژگی‌ها:
🧠
اتصال یکپارچه به هسته Hermes (محیط لوکال، کلاد یا ریموت)
📄
استخراج هوشمند و ایمن متن صفحات و تب‌های باز برای هوش مصنوعی
🎙
پشتیبانی از دستورات صوتی و رندر حرفه‌ای Markdown
🛡
امنیت حداکثری بدون نیاز به دسترسیِ تاریخچه و کوکی‌ها
🧪
نکته:
افزونه در فاز آلفا است؛ برای استفاده باید فایل‌های نسخه ریلیز را دانلود و به‌صورت دستی (Unpacked) در مرورگر لود کنید. پیش‌نیاز اصلی، نصب بودن خود Hermes Agent است.
📥
دانلود از گیت‌هاب (بخش Releases)
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6925" target="_blank">📅 08:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6924">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌐
؛
Omni Browser
مرورگر اندرویدی امن و فوق‌حرفه‌ای (مبتنی بر موتور فایرفاکس) با تمرکز شدید بر حریم خصوصی.
✨
ویژگی‌ها:
🛡
مسدودساز تبلیغات (uBlock) و گاوصندوق بیومتریک فایل‌ها
🧩
پشتیبانی مستقیم از نصب افزونه‌های فایرفاکس
🎬
شکارچی خودکار لینک‌های ویدیو + پلیر اختصاصی
🛠
مترجم ۱۰۰٪ آفلاین و ابزارهای حرفه‌ای دولوپرها (کنسول زنده JS)
🧪
نکته:
برنامه در فاز آزمایشی است؛ فعلاً به عنوان مرورگر اصلی استفاده نکنید و از اطلاعات مهم بکاپ بگیرید.
📥
دانلود از گیت‌هاب (بخش Releases)
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6924" target="_blank">📅 08:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6923">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/se1i5IgiTthqB2B2OwemsAWLZYCRhjvPQAmul0hO8EahLhM94fu6ngoAdUUHENN-QXawNM956omCGLyTP1dIjzNdXYr079IUbXaRX7UQSJP_MIJ42Ps1GZC-QUXG45bLTFo-iJXL9BhR7TfJzVv-PLzWTSe3zMie6kE-C3qcdc16bhfh0OPYwpSUiVHhxbczqeLGnq-o3LPW0Dz65-11XkD4PHnJEYYMcDZ0-oJn3Hyr7KZj281yLtoVVvL-uZ8B5dzPZ3iVYlBjHV0TjXuOQJiUEheXAT_2M03H4OGsyTdiKnQQlQN5xM6MjwBL1o0U_Dvz6xjpbn_-Wq1lxfzokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6923" target="_blank">📅 08:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6922">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">Telegram-X-0.28.10.1791-armeabi-v7a.apk</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6922" target="_blank">📅 01:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6920">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTelegram X APKs & Build Info</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram-X-0.28.10.1791-arm64-v8a.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6920" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Version
:
0.28.10.1791-arm64-v8a
Changes from 1785
:
4ac597ca...5c907d8b
#arm64
#beta
#apk
(
MD5
,
SHA-1
,
SHA-256
)</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6920" target="_blank">📅 01:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6919">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚀
آپدیت بزرگ بات منتشر شد: هوشمندتر و سریع‌تر
تغییرات کلیدی برای مدیریت یکپارچه کانفیگ‌ها و عبور از محدودیت‌های دسترسی:
✨
ویژگی‌های جدید:
•
📱
مینی‌اپ اختصاصی:
دسترسی سریع و رابط کاربری مدرن برای مدیریت آسان‌تر.
•
🔗
بخش ترکیب (Merger):
ادغام تمامی کانفیگ‌های Render و Railway در یک ساب‌اسکریپشن واحد (نیازمند توکن Cloudflare).
•
📡
بخش رله (Relay):
اتصال دامنه Render به Cloudflare Workers جهت رفع فیلترینگ بدون نیاز به خرید دامنه پولی.
🛡
نکته فنی (مصرف Cloudflare):
این روش بهینه‌ترین حالت ممکن است؛ با سقف ۱۰۰ هزار درخواست رایگان روزانه، نگران محدودیت نباشید. مصرف فقط در زمان اتصال/قطع صورت می‌گیرد.
⚠️
توجه:
به دلیل ترافیک بالای انتشار، ممکن است در ساعات اولیه با کندی جزئی مواجه شوید که به مرور برطرف خواهد شد.
🤖
شروع استفاده:
@REN_WZA_BOT
@REN_WZA2_BOT
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6919" target="_blank">📅 00:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6918">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJvkagnkqDEDP4IOMxZ9w9sCP60-xntJDnqz-ADNHp2sNEF78gOfmBk4zvlk6aMyjm4ppBTqzQ-XZ5AkAaYKWrXWNl2F_2qET5j1JxL8EUKHWzkaAVZcJxeJfOR4FdXsqF6FofpGr9vFZEMre8DYjuWSZ7tY4KuR5_YVmcJIGIXsi9qe4WvX2hrykx-QExN7-FnC_jWq7YXPzJ5H1wI_QdLboEwoBq26TxVVUTx2E0O4xvrHdAJsguXq-YagZ7eXkcd_fVcLcS_IH18MHcyVPLO90exSlZcUVcoRs4BI6S0Aa3X2aEPNeRs0RfffNqSPjKr09cmkTw8EAW6i9WkqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به Claude Fable 5 دوباره تمدید شد، شرکت Anthropic این مدل را تا 19 جولای در اشتراک معمولی در دسترس قرار می‌دهد.
محدودیت‌ها همانند قبل هستند: 50 درصد از میزان استفاده هفتگی. پس از یک هفته، Fable 5 به سیستم پرداخت بر اساس توکن از طریق API منتقل خواهد شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6918" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6916">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qf_aE5ViDK4OVlFpXVKQv5N_SvWmnjBRrWmSl8QmAd8CRbhVpQV2naEFm-VusOjriMzUIHZcj_Ejv-KkA4-7hSnRvm_A-5A7lSq_FTG6Qaxlic3SJ7QRMenSoLvlhoN-Fd_FgEBhQBcW9bGpZUCKW2uMJlY2KPwoTlpkCh2bkJo16LvzwoXiweYlhQECdXY8MbhD9EqvivDa_4ECsSK8ifcW4OJH_vhJ5nk4ZSG7dm98AsUaqNbWOPRXcn-sehEl24vI2oLgGekGx1n2IpAWZLi68BIdl3PzF1OivNLfOESu0AgxBJ2WDawmTQGOPXuZ5JHfDOhk6Nmsoc6wlraPAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTs4gx3yNI82innc9y86AdW_plkrWWsmGXRVlU4qkKjFzUnyWXdjEZNOlLvdc01vIH3aqIH8lV7IfpeTsl0IXvtr70XAZpPer22JzVDavmRydxHWxksSENW_5TMZ-lmkgCU4xh3VDfvIh0-YE9Tqtim2sjoCBpVIsyfAZvG0wNgEtQyZZgnc6DAeWLy3lEY1DbfUbmnIiVUQsX6JhOjpD2sQY1biMSVoHABy22z0TGwBxsLRrIwblxkpvuF6m2lhAVWdY5EkFBEUcZwBSrNhET0I6PDvUAYC3NB7NcryvioMIw-CAPQAqCIIcbBHQMysUOR488939VpY4Z4wAAWjUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">؛PCLink راهکاری سریع و سبک برای دسترسی از راه دور به رایانه، بدون تنظیمات پیچیده
🖥
• دسترسی کامل به فایل‌ها، اپلیکیشن‌ها، کیبورد و ماوس
• خاموش، روشن و ری‌استارت کردن سیستم از طریق گوشی
• اتصال آنی با اسکن QR Code
• پشتیبانی از Windows و Linux
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6916" target="_blank">📅 21:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6915">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اپلیکیشن اندروید NipoVPN توی گوگل‌پلی   https://play.google.com/store/apps/details?id=net.sudoer.nipo</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6915" target="_blank">📅 20:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6914">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMorteza Bashsiz مرتضی باشسیز</strong></div>
<div class="tg-text">اپلیکیشن اندروید NipoVPN توی گوگل‌پلی
https://play.google.com/store/apps/details?id=net.sudoer.nipo</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6914" target="_blank">📅 20:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6913">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@ArchiveTell.json</div>
  <div class="tg-doc-extra">2.4 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6913" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ warp
فقط سامانتل
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6913" target="_blank">📅 19:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6912">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پروکسی تلگرام
🔥
https://proxybolt.link/
| سایت
@mtpro_xyz_bot
| ربات
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6912" target="_blank">📅 19:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6911">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⏱
؛
tg-username-clock
یک اسکریپت ساده و جذاب برای شخصی‌سازی پروفایل تلگرام که نام خانوادگی (Last Name) حساب کاربری شما را به‌صورت خودکار و هر یک دقیقه، با زمانِ دقیقِ فعلی به‌روزرسانی می‌کند.
✨
امکانات:
*
⏱
نمایش زنده زمان: تبدیل نام کاربری شما به یک ساعتِ زنده برای مخاطبان.
*
⚙️
به‌روزرسانی خودکار: اجرای اسکریپت در پس‌زمینه و آپدیتِ اتوماتیکِ هر دقیقه‌ای.
*
🚀
سبک و کاربردی: پیاده‌سازی سریع بدون درگیری‌های پیچیده نرم‌افزاری.
📥
دریافت اسکریپت و دسترسی به منبع پروژه.
⚠️
احتیاط یادتون نره!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6911" target="_blank">📅 18:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6910">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔐
؛
OfflinePW
یک پسورد منیجر اندرویدیِ فوق‌امن، سبک و کاملاً آفلاین است که از یک دولوپر ایرانی (Cyru55
❤️
) که با الگوریتم‌های نظامی و معماری «دانش صفر» توسعه یافته است.
✨
امکانات:
🚫
آفلاینِ مطلق:
بدون نیاز به هیچ‌گونه دسترسی (Permission) در سیستم‌عامل.
🪚
امنیت TwoFish-256:
قدرتمندتر و ایمن‌تر از استانداردهای رایج AES.
⛏️
ضد Brute-force:
خنثی‌سازی حملات با استفاده از PBKDF2.
📸
حریم خصوصی:
مسدودسازی خودکار اسکرین‌شات و ضبط از صفحه.
⚡️
حجم مینی‌مال:
تنها ۴ مگابایت با رابط کاربری ساده و پوشه‌بندی شده.
🔪
پشتیبانی وسیع:
سازگاری کامل از اندروید ۴.۰ تا نسخه‌های جدید.
🔒
مدل Trust No One (به هیچ‌کس اعتماد نکن)
هیچ‌کدام از پسوردها یا کلیدهای رمزنگاری شما در سیستم ذخیره نمی‌شوند. تنها کلیدِ دسترسی به داده‌ها، رمزی است که منحصراً در ذهن شما قرار دارد.
📥
دانلود فایل نصب (APK) از بخش Releases گیت‌هاب.
⭐️
در صورت رضایت، با Star دادن از پروژه حمایت کنید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6910" target="_blank">📅 17:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6909">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkWkmFnwlChH4ORhIzvCCsKZgSMxQbpqQ0mbqjYKbde2IXOpZqHzmZ3f92R2kAQUMF4jFmnMawJlniPDiL0FjgN_vcFiE5eXqAVXXrw12MogyI5ZBoyxStKjhEkAt4_wRQuHElc3XY6NMYt6TEQkghPSHBHCy1X3F2O_q0Ok7GCVx7S_qGJw-paW7H4ph9U04YCrZbsrgsxWQSMoNSemeZIMXIqh_DlnmGW0hDyydD1xmKcmIeIInY5iEEAFueRlHfDcgFWdt9uYlPfu7bw6WckeVcnkSHGfN8fAXkuvD_lcyEFi1d1TUFnWDQNDbbyUbyvQHmTbDyCWsS6xX8BKhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌍
؛
OSINT Intelligence Dashboard
داشبورد متن‌باز و کاملاً رایگان برای رصد بلادرنگ رویدادهای امنیتی جهان؛ یک تحلیل‌گر شخصی و جایگزینی قدرتمند برای پلتفرم‌های گران‌قیمتی مثل بلومبرگ ترمینال.
✨
امکانات:
*
📡
رصد جامع:
مانیتورینگ ۲۷ فید اطلاعاتی (پروازهای نظامی، تشعشعات و درگیری‌ها) روی کره سه‌بعدی.
*
🤖
تحلیل هوشمند:
اتصال به مدل‌هایی مثل GPT و Claude برای دریافت لحظه‌ای گزارش‌های امنیتی.
*
📱
مدیریت آسان:
کنترل کامل و دریافت هشدارهای چندسطحی (FLASH تا ROUTINE) از طریق بات تلگرام و دیسکورد.
🔒
اجرای ۱۰۰٪ لوکال
این سیستم کاملاً آفلاین و فاقد هرگونه تله‌متری (Telemetry) است و تمام پردازش‌ها منحصراً روی سیستم شما انجام می‌شود.
📥
دریافت سورس‌کد (با بیش از ۱۰ هزار Star) از گیت‌هاب.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6909" target="_blank">📅 16:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6907">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🗑
حذف کامل برنامه‌ها و فایل‌های اضافی مک با Uninstally
وقتی برنامه‌ای رو در macOS به سطل زباله منتقل می‌کنید، کلی فایل کش، لاگ و تنظیمات پنهان روی سیستم باقی می‌مونه. این ابزار بومی (Native) و اوپن‌سورس تمام این ردپاها رو برای همیشه پاک می‌کنه.
🔥
ویژگی‌های مهم:
🖱
ادغام با Finder:
امکان حذف سریع برنامه‌ها فقط با یک کلیک‌راست (بدون نیاز به باز کردن خود ابزار).
📦
پشتیبانی از Homebrew:
شناسایی، مدیریت و حذف پکیج‌ها (Casks و Formulae).
🧹
اسکنر فایل‌های یتیم:
پیدا کردن و پاک کردن فایل‌های جا مانده از برنامه‌هایی که قبلاً به صورت دستی پاک کردید.
🔒
کاملاً آفلاین:
بدون جمع‌آوری دیتا (Analytics) و بدون نیاز به ساخت اکانت.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/6907" target="_blank">📅 16:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6906">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌍
سناریوی جدید AI 2040: Plan A
تیم پژوهشی گزارش معروف AI 2027، سناریوی آینده‌پژوهانه جدیدی را منتشر کرده که مسیر توسعه هوش مصنوعی را در صورت همکاری قدرت‌های جهانی (آمریکا و چین) بررسی می‌کند. بر اساس این سناریو، تا سال ۲۰۳۵ حدود ۸۵٪ کارهای اقتصادی به AI واگذار خواهد شد.
🔥
مهم‌ترین نکات این سناریو:
🤝
توقف رقابت AGI:
توافق آمریکا و چین بر سر کاهش سرعت توسعه، افزایش شفافیت و نظارت‌های سخت‌گیرانه بین‌المللی.
🛡
تمرکز روی ایمنی:
متوقف شدن توسعه مدل‌های پیشرفته، صرفاً تا زمان انجام ارزیابی‌های جامع امنیتی.
💰
درآمد پایه همگانی (UBI):
رشد اقتصادی بی‌سابقه از ۲۰۳۲ و پرداخت یارانه‌های سالانه به شهروندان جهت جبران بیکاری ناشی از اتوماسیون.
🚀
شتاب علمی چشمگیر:
رسیدن AI به سطح برترین متخصصان تا ۲۰۳۵ و افزایش ۱۰ تا ۱۰۰۰ برابری سرعت پیشرفت علمی از ۲۰۳۷.
⚠️
نکته:
این گزارش صرفاً یک سناریوی تحلیلی و آینده‌پژوهانه است و پیش‌بینی قطعی محسوب نمی‌شود.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/6906" target="_blank">📅 16:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6905">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بنازم
🔥
🔥
🎁
گیووی اکانت‌های مادام‌العمر Proton VPN!  اکانت رسمی پروتون اعلام کرده که اگر امروز تیم ملی سوئیس بازی رو ببره، اشتراک‌های بسیار نایاب و رایگان مادام‌العمر (Lifetime) هدیه میده!
🔥
جزئیات:  *
🇨🇭
شرط قرعه‌کشی: پیروزی سوئیس در مسابقه امروز مقابل آرژانتین.…</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6905" target="_blank">📅 16:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6904">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بنازم
🔥
🔥
🎁
گیووی اکانت‌های مادام‌العمر Proton VPN!
اکانت رسمی پروتون اعلام کرده که اگر امروز تیم ملی سوئیس بازی رو ببره، اشتراک‌های بسیار نایاب و رایگان مادام‌العمر (Lifetime) هدیه میده!
🔥
جزئیات:
*
🇨🇭
شرط قرعه‌کشی: پیروزی سوئیس در مسابقه امروز مقابل آرژانتین.
*
💎
جایزه: پلن Lifetime پروتون (اشتراکی که در حالت عادی اصلاً فروخته نمیشه و ارزش بسیار بالایی داره).
🔗
[لینک توییت رسمی پروتون]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6904" target="_blank">📅 16:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6903">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nclOfivHY3H3xrRuM0J2nzYJym6crWhGTBPg0Ia8ux0XTOj1_kfoLrPLH7taqevDcpB4LIaqRuuoAs585HW428a0hNUuJ35QfjmgZ8nteoyHHSeS9bTxu_b_JKPSkTcD2O2mMb_rsAjC0dOCFSeHl1YAUH_a7D6nzscEvZizTdJoy70_LDEYUDdx6lHL0hFXAYguHS8nH9DZgu0YmZySsLXSVLL1QZxkb03Ce_CnNqa7VQQruJMofe0lY9z3Qc6vAIzs91_w8YD0yp6mBrIn1ZWZR4dN9T4qcEC_iG0-p941vDqKalW-ImGIUuzsV2uEcQqoWTUCE3XsT7P7xvT5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
AIText Detection for X
⁩تشخیص متن تولید شده توسط هوش مصنوعی!
🔍
✨
‏‌این افزونه با هدف شناسایی و تحلیل محتوای تولید شده توسط هوش مصنوعی در توییتر طراحی شده که با یکپارچه‌سازی آسان با فید توییتر، امکان تحلیل توییت‌هایی که کاربران میخونن رو فراهم میکنه.
https://www.tweetdetective.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6903" target="_blank">📅 15:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6902">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVKGgAsffHV56B5bb0KYLZJWeLNsXOu1CyjCc5uE3mFSUyfOUWeh_tLAwDZU-Jr1OREqjUfDK61mY3pUFBwLeC3lou8T11F9csHgVUQ3yoV9WMnD3uXFvOu8xdBz0A4vJrIpKzNPAtxhM4BBagi1uyYtd0jE5w5Y9Z3n2x7WqMFve_-1oXk8Vt-l7ze24p5ZXucGQdUqOLndWczzUdubYkOhjKmw9nCfIJo1XdbpLDMqs4Hj7zMXHd9yTi6o2G6qfZ4D8nBQeXTyobbiBeBdDlNiDBGxXCarAJm9ZteH38OfLV_X3trTW4fOHxBitG3_Ql-M5GbZcSsXBwBbBLhqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
معرفی ‌Gitea⁩؛ جایگزینِ سبک و قدرتمندِ ‌GitHub⁩ برای میزبانیِ شخصی!
🛠
‏با ‌Gitea⁩ می‌توانید در عرض چند دقیقه، سرویسِ گیتِ اختصاصی خودتان را راه‌اندازی کنید. این پلتفرم با وجودِ سادگی، بسیار منعطف است و اجازه می‌دهد به راحتی پروژه‌هایتان را از ‌GitHub⁩ یا ‌Bitbucket⁩ به محیطِ امنِ خودتان منتقل کنید.
‏
✨
ویژگی‌ها:
‏‌
🔹
فوق‌العاده سبک: یک باینریِ واحد که حتی روی سخت‌افزارهای محدود هم کار می‌کند.
‏‌
🔹
سازگاری کامل: پشتیبانی از ‌GitHub Actions⁩ برای اتوماسیونِ حرفه‌ای.
‏‌
🔹
نصبِ سریع: راه‌اندازیِ بی‌دردسر از طریق ‌Docker⁩ و پشتیبانی از دیتابیس‌های مختلف.
🔹
همه‌کاره: شاملِ مدیریتِ تسک‌ها، ویکی، رجیستریِ پکیج و ابزارهای ‌CI/CD⁩.
لینک گیت هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6902" target="_blank">📅 14:09 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
