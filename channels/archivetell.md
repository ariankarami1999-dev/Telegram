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
<img src="https://cdn4.telesco.pe/file/Zb1t0waL7Gmv1PnfCFNynIp3lAo_-M77BeyyGZwmxu_CDA7mOkLHvPcHjxtt0H80dgwZoIwl7udsC82QEmYcZz4Efm3H5jRG0bcE5aZXy_aMhCR1I1R-pqMAiOKYSAJiMaLGgV62zpKPtdCASJYDqpNs18kX65ZwISP9DBGAoFvjWne__jmee-sPIhOdJ6EoAQXtORXdLwLJC7POhkasTCkiGDjBRntz5hzoK6W1IwdnctYxDTI38FfEcyqxRNl5TJ_2KbKYRvLzspygRqhFENPMTuyvF56WlXUwImAHmsczorGaLWs9udMOZfwSKJNoIedvgu26GJdKhoSzmv4fIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.57K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پروکسی‌های اختصاصی آرشیوتل
😎
⚡️
پروکسی ۱
🚀
پروکسی ۲
💥
پروکسی۳
💡
روی لینک بزنید و گزینه Connect را انتخاب کنید.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 101 · <a href="https://t.me/archivetell/6211" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqMsBg0pSILfErBsHqPOh8_zAj2xoC5zDaW80yxEvrj4mnc8z86FVuw62Q5_1nk-vvLlc6p0_pV6iOpSIn4X39kxUgU2eIVAZ8B3kFgFvP6hszfRf_ScvNRE6NCAwZeKC4G7fgkSGby14js9EfmiLD0GthOf7UlvD9Hb0nJO8yWf_oO2WmGXwShq6lFEg4tIBEBZ0YfKHsDfSlCrHV2-GQZStQzS0fxXc1yJbcGnYJ-b7EVXdDr6lS2ej_1zKgioJP30mcbZDRpGtAkx4rCQaWpjUW_EHG0UkpnEhfpecgESH0p8-5xoMBBjSNv8qiOXhfod03VQ9aplFE87xFONXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب یه روش مخصوص ایرانی‌ها اضافه کرده، رو همه اپراتورها عالی کانکت میشه:
Settings → Connection → Anti-Censorship
گزینه Protocol Tweaks رو روی Enable بذارید، بعد وارد Configuration بشید و یکی از دو گزینه آخر که ایران هست رو انتخاب کنید. گزینه Large TLS رو هم روشن کنید.
پروتکل های udp و tcp رو تست کنید
ایرانسل tcp 587 france
مخابرات همراه اول udp 80
با فیک میل اکانت بسازید
https://windscribe.com/signup
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 405 · <a href="https://t.me/archivetell/6210" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsYlHkwa80Kmsj9jB6nYfotLleDylvWsauAIL7JkN4D5oO2GxIrA3qBBy_MrBA9h10FJC40XOPNvKawzyf83jo8L8JSavcELrbrpaRS2BJw6bLZhK7Pr6p8vMYzGUyU_rmJaIgMpavP56K2jhewNkWqxU0XU5Z0EnyUR9GHRtPiF8B78R6Lbg5uLeMd7CvpboxwRey_weyrHg4plZYFJQc4-QHSEK88IPASPu_kDjp-GR9N1tf_oq0mMe7f3j2Nx3cylz-wdWjz12ON-CLbtcNjcwDHnrFy2QabTCcdn5C63L-CV_PQOUx14cjUhdt8XBpjIhu4vIjiKEhk9ycXD_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
Impeccable
‏این ابزار به عامل های هوش مصنوعی کمک می‌کند تا وب‌سایت‌های منحصربفرد و بدون الگوهای استاندارد ایجاد کند
🔥
‏
✨
قابلیت‌ها:
‏•
🔹
آموزش عامل‌های هوش مصنوعی برای ایجاد طراحی‌های منحصربفرد
‏•
⚡
کار به عنوان منتقد، توسعه‌دهنده front-end و نویسنده UX
‏•
📊
آزمایش ماکت‌ها، برطرف کردن خطاها و بهبود طراحی
‏
‏
🔗
لینک:
https://github.com/pbakaus/impeccable
‏
#هوش_مصنوعی
#طراحی
#OpenSource
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 730 · <a href="https://t.me/archivetell/6209" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKpoHgi3mz7G2XwNTRZppXQi99-K-gINzWr4uUEG1Qym00sYRG0JqlzoHS5JfPV8nAsd8hhBYU0hcfJaCc0Ikgbx46mDs7rJaltA-FCZFYB1YxCzMfmakJxtumQajWWtFOLWI3CRs1oQG9mCqEesJsqh8NNhgD9nVETpHP3E9jHot0QFbJnEyFcZKMsHVBvqOmfDa8UP8Po19ZUvtxJH_iSwdvyHmvONXJsbeLz0UOXIGkqO3S8INl9ayCsextf9C887Iqht6VRIWDcmSjtObTwPygJTsGYszkdcvUOQivSsbqwWjBwoMsKQXA6Foz32uETdRaA_jQdhznLUPAnsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXGKwDEgbVs7oIQGBDO-_4zccRY7_il77xejzwMxJF69LmW9DzhbSfXigjSKQSCXFsQXGAy6u04X8AcgWkA5OwjGeNgyqmmnozh5YRxu4zxSS-lJ_OkBfH8BORXMtD1Sk392HhD2d5-A0FuN0CCdQHkegNquoXoozx5Fb4o5NtCaj18-9-ZvidNIZ_GQJD4Re9zUTsMdGZZHi1Mlw_RvT3zUYfAIZaW81H4SehgEQz3d8QlRQxs6liwVW5iU-KPAvczVjm1DioGqh9RIett8KPhGzs1CXAlP6qWNA-_UTmi0ZGFWt3EwA1eNYtaCkPnpJctG4XMMIy-GnmisaqYZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpInkTRWOlFgOHhGz5Dz7bLQ9uq6rfCKoiMfoo2J-Z9A9dx5VJSitT44-vsHcTqa7LxNKr_w_etNKq1UukAw541jH4UibwTliQadjsWtbwKubVu1MPp70ZFiCiexuPFKdNbpbLDejjfjZctrM7cnz3HjkXnqq8UmtZ1SiS9IuUuivCXqnCicubF2RdPsKoP7bCYEohVopsKUEH1qzUx8w9UwoLhmk0rxBFHiKKHXyDAwC84Bq9GaDEhv5Em7FdsvFj1WPpejURkT4S3APt5sHSiKHr5v6uUts4m32h-3ELcsYlgm9Ax9y-1yO6_qtWU8LfT8rfu3O6XCAYH3Iq2LYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=IyG0a6CQvuiLf3NZo-53cjr_IDyAfUqBfImv5_-WteP7sPk1s0F7_fi69nd3auqGxst9nxILSr49Cu1oxhX8cDsSrXNPZODoRAXnlsKb2V7fUqyMcQ9yua_Rqn_YCdDvuDjue1AiaU_i7anf-cCNq0jvTkyTrTemwZiT9oGErHtuOiJQdPJ62tQEQnVnAFp_A3TfzzW91gIiceocMjOG1hOHoX_lwXAtrvHxLM9V4HHT7IPAHsEbKxetTgbHMf5ds18abdCMV3PZuCRZ0xDfmkeJV_RWhhMw2C7EoTyEb9WW_YN_Cr6bFRkjSkroV-VFg9b-c2-xJGIM431ErPvO-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=IyG0a6CQvuiLf3NZo-53cjr_IDyAfUqBfImv5_-WteP7sPk1s0F7_fi69nd3auqGxst9nxILSr49Cu1oxhX8cDsSrXNPZODoRAXnlsKb2V7fUqyMcQ9yua_Rqn_YCdDvuDjue1AiaU_i7anf-cCNq0jvTkyTrTemwZiT9oGErHtuOiJQdPJ62tQEQnVnAFp_A3TfzzW91gIiceocMjOG1hOHoX_lwXAtrvHxLM9V4HHT7IPAHsEbKxetTgbHMf5ds18abdCMV3PZuCRZ0xDfmkeJV_RWhhMw2C7EoTyEb9WW_YN_Cr6bFRkjSkroV-VFg9b-c2-xJGIM431ErPvO-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
هوش مصنوعی Siri یاد گرفته است که عکس‌ها را مانند Nano Banana Pro ویرایش کند.
✨
قابلیت‌ها:
‏•
🔹
«بازآفرینی فضایی» برای تغییر ترکیب، زاویه و پرسپکتیو عکس‌ها
‏•
📸
ویرایش پیشرفته برای ایجاد عکس‌های خلاقانه
#Apple
#Siri
#Ai
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/archivetell/6205" target="_blank">📅 12:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBdUlyQ_P0VI62VpLxO162j7zO5cuQLpN9vX3H3qTi9ed_GhbLxSfz4gLDmct1ElUvDlZ8poLq-dp6Jq8RXRwpgLrITuUz7-SPX7ILX83UbWM2PFYoE9-yWChkbiWEoF9uhec-ZOmx5wGITh_qmWzvYU3gfUJo0Z9St1gUWCITud5SU3FLcuf8UcaSYIcnDcpUMESuBc2N8dCGcvWK0hSK3owv_n8Wb5OtPMpkpPP5XGMYiHioZGGNwB3yurkvUyTaAYQ0gOImYd-8ZwmHIfQ0AV8EbNYFZfQFlUKPBtUYHfcqXk3cqfyIqEHTu1oofXLKBoTfVvN5BQXM8DmgEajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
.FrameCoach معرفی شد!
‏این ابزار هوشمند تنظیمات گرافیکی ایده‌آل را برای هر سخت‌افزاری انتخاب می‌کند و حداکثر FPS را استخراج می‌کند
🎮
‏
‏
✨
قابلیت‌ها:
‏•
🔹
انتخاب کارت گرافیک و پردازنده
‏•
⚡
انتخاب بازی از کاتالوگ
‏•
🛠️
دریافت تنظیمات بهینه برای حداکثر FPS یا بهترین گرافیک
‏•
📊
مشاهده تأثیر هر پارامتر بر عملکرد
‏•
📈
تست تنظیمات و پیش‌بینی فریم بر ثانیه
‏
‏
🔗
لینک:
https://theframecoach.com/
‏
#گیمینگ
#بهینه‌سازی
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/archivetell/6204" target="_blank">📅 12:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">با پلتفرم Cerebras به مدل‌های قدرتمند gpt-oss-120b و glm-4.7 با محدودیت بی‌نظیر ۱ میلیون توکن و ۲۴۰۰ درخواست در روز دسترسی پیدا کنید
🚀
شما می‌توانید کلید API خود را دریافت کرده و پروژه‌های هوش مصنوعی‌تان را با سرعت و دقتی فوق‌العاده پیاده‌سازی کنید
🛠️
. این یک موقعیت عالی برای استفاده از مدل‌های سنگین بدون پرداخت هزینه است
💸
، پس آن را از دست ندهید!
✨
cloud.cerebras.ai
🔗</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/archivetell/6203" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=eIdhtouwiZhiZc4M_t5lReecmhwpTT-MLLlpzN_HWTgCUCTwskPimVT2d_1FDvVL8fPJ7yAmPg9cp4NGsHo57IU5xk-FMDBcgbmQA7y7D0ExaahKitGiQoar8ZwMcPgLncRWLiDkQCPqDDqmHXkRiSoA5FD3tAbNLaY1-BoZ5nZLn0eL_DIWMnOi-GslnCqnQ6ChREL-758embeusgwFqDqa5MR2ZBKjtNbQ0P45ZMlSG9xpyF50m5b_TrUe5w6qcXZx3dc11v_o7dzRk24n5xSCRbTeWBug3TSRc7QDGFL9Waahn9MJQASy9DlChOx12yQ-LnCGp5qa4dsXkPmoCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=eIdhtouwiZhiZc4M_t5lReecmhwpTT-MLLlpzN_HWTgCUCTwskPimVT2d_1FDvVL8fPJ7yAmPg9cp4NGsHo57IU5xk-FMDBcgbmQA7y7D0ExaahKitGiQoar8ZwMcPgLncRWLiDkQCPqDDqmHXkRiSoA5FD3tAbNLaY1-BoZ5nZLn0eL_DIWMnOi-GslnCqnQ6ChREL-758embeusgwFqDqa5MR2ZBKjtNbQ0P45ZMlSG9xpyF50m5b_TrUe5w6qcXZx3dc11v_o7dzRk24n5xSCRbTeWBug3TSRc7QDGFL9Waahn9MJQASy9DlChOx12yQ-LnCGp5qa4dsXkPmoCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🤖
چینی‌ها یک هیولای هوش مصنوعی با ارتشی از عوامل عرضه کردند — Kimi Work می‌تواند تا صد دستیار را به طور همزمان روی یک دستگاه اجرا کند.
‏
‏
✨
قابلیت‌ها:
‏* تا ۳۰۰ عامل می‌توانند به طور موازی روی وظایف مختلف کار کنند
‏* مرورگر را تقریباً مانند یک انسان کنترل می‌کند
‏* دسترسی به داده‌های مالی را بدون پیچیدگی در تنظیم API فراهم می‌کند
‏* عادت‌ها، زمینه و اقدامات قبلی را به خاطر می‌سپارد
‏* با فایل‌ها و اسناد محلی کار می‌کند
‏* کد پایتون را اجرا می‌کند و فرآیندهای روتین را خودکار می‌کند
‏* کمک می‌کند برنامه‌ریزی کنید و وظایف بزرگ را تقسیم کنید
‏
🔗
https://www.kimi.com/products/kimi-work
#kimi
#ai
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/archivetell/6202" target="_blank">📅 11:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">78.2 MB</div>
</div>
<a href="https://t.me/archivetell/6201" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">12.8.0 (6913)
Directly downloadable from
telegram.org/android
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/archivetell/6201" target="_blank">📅 11:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjWIbx2-SJExEm9-fwNQgLOo1na_fyIfAlpI3086lWqs14JYjmccQQcxO9nzQ8uiORk3YPGOitkIXFMBe2Lu5bY7ZFNM1ULOyZPkMfXAcqE84QfvCR-XQv0MuV5aKfBT6FX0bc4gg6u583JSJNGN8ApryGRTMokK-IFthvWxL9sMknckonEumQcTYqezgDfgW5hZM8w-5rS_w2imHorSBfQGd_CwqWgNg-yllwIvqdIFQkuUwCZ1rxbwIzicSQuApGdArvAUXViOohnteEdEyCXFiw17qL7VZsdOn5O1BEWGRfv-kvDuUgZ5kNkRm465onLxma_VTQkhFQ8HMsj-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
گوگل NotebookLM را با قابلیت‌های جدید هوش مصنوعی ارتقا داد.
حالا این ابزار از مدل جدید Gemini استفاده می‌کند و می‌تواند فراتر از یادداشت‌برداری عمل کند.
🚀
✨
قابلیت‌ها:
•
🤖
پردازش و تحلیل بهتر اطلاعات با Gemini
•
📊
ساخت نمودار و تحلیل داده‌ها
•
💻
اجرای کد مستقیماً داخل نوت‌بوک
•
📝
تولید اسناد و گزارش‌های مختلف
•
☁️
محیط پردازش ابری اختصاصی برای هر پروژه
🎯
ابزار NotebookLM کم‌کم از یک ابزار یادداشت‌برداری به یک دستیار تحقیق و تحلیل کامل تبدیل می‌شود.
🔗
لینک:
https://notebooklm.google.com
#Google
#Gemini
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/6200" target="_blank">📅 10:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee5737315.mp4?token=YPL_M2CGH3ST7ZvQkBEWtqwydyJObn-g9ltWqbmCAOINIx8UY6buqnh7hbaWSr7EcYO1_MstoItb1EqoNJX3CW0C3iI51OvEVRgW2mAR-Bu1yUneIbA2BynYzhdckP1gizZ2lbe0ulzZcu7WgjEbKN7DcWhvfZTx4AcIw6nwGaERp-26nQyfXUR0e3Dh6njytFNa2OAUACEyoxAnNUKDnFnngh2sZs1Bw8rlvljLStxif4SUNOQqUtwJXn2LFmcLKVP8T4SBSbYAv_ArVfP_tMZmDUkAiVncCnxs4cF6nAIixq4LXsuzTRzlLXGePya3pwQqKCv2WEfJyjGMH1yYIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee5737315.mp4?token=YPL_M2CGH3ST7ZvQkBEWtqwydyJObn-g9ltWqbmCAOINIx8UY6buqnh7hbaWSr7EcYO1_MstoItb1EqoNJX3CW0C3iI51OvEVRgW2mAR-Bu1yUneIbA2BynYzhdckP1gizZ2lbe0ulzZcu7WgjEbKN7DcWhvfZTx4AcIw6nwGaERp-26nQyfXUR0e3Dh6njytFNa2OAUACEyoxAnNUKDnFnngh2sZs1Bw8rlvljLStxif4SUNOQqUtwJXn2LFmcLKVP8T4SBSbYAv_ArVfP_tMZmDUkAiVncCnxs4cF6nAIixq4LXsuzTRzlLXGePya3pwQqKCv2WEfJyjGMH1yYIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔤
پیدا کردن فونت هر سایتی در چند ثانیه
ابزار
Font Stealer
یک ابزار رایگان برای طراحان است که فونت‌های استفاده‌شده در هر وب‌سایت را شناسایی می‌کند.
✨
قابلیت‌ها:
• نمایش فونت‌های به‌کاررفته در صفحه
• دانلود فونت‌ها در فرمت‌های مختلف
• پیشنهاد جایگزین‌های رایگان از Google Fonts برای فونت‌های پولی
🎨
ابزاری کاربردی برای طراحان UI/UX و توسعه‌دهندگان وب.
#Design
#Fonts
#WebDesign
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6198" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌐
اختلال VPNها در روسیه وارد مرحله جدیدی شده است.
گزارش‌ها حاکی از آن است که فیلترینگ در روسیه نیز دیگر فقط بر اساس IP نیست و اکنون الگوی ترافیک و TLS Fingerprint نیز بررسی می‌شود. همین موضوع باعث ناپایداری VPNها، MTProto و پروتکل‌هایی مانند WireGuard و VLESS شده است.
#VPN
#Telegram
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/archivetell/6197" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
پروکسی محلی برای تلگرام دسکتاپ
TG WS Proxy یک ابزار متن‌باز است که ترافیک Telegram Desktop را از طریق WebSocket عبور می‌دهد تا اتصال پایدارتر و سریع‌تری داشته باشید؛ بدون نیاز به سرور واسط اختصاصی.
✨
قابلیت‌ها:
• اجرای MTProto Proxy به‌صورت محلی روی سیستم
• انتقال ترافیک از طریق WebSocket و TLS
• پشتیبانی از Windows، Linux و macOS
• رابط گرافیکی ساده برای مدیریت تنظیمات
• متن‌باز و رایگان
📥
دانلود و مشاهده سورس:
https://github.com/Flowseal/tg-ws-proxy
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6196" target="_blank">📅 03:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">Clearly, the iranians do not know how to speak english or behave themselves.</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6195" target="_blank">📅 02:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">😅
میگن با این مینی‌اپ میشه تا ۵ TON جایزه گرفت! (تایید شد الان)  اگر اهل تست کردن ایردراپ‌ها و مینی‌اپ‌های تلگرامی هستید، بد نیست یه نگاهی بندازید.
👀
📋
اول این لیست را اضافه کنید:  https://t.me/addlist/5VAtNN0PSuQwMzc0
🤖
بعد ربات را استارت بزنید:  @gramevents_bot…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6194" target="_blank">📅 02:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">😅
میگن با این مینی‌اپ میشه تا ۵ TON جایزه گرفت!
(تایید شد الان)
اگر اهل تست کردن ایردراپ‌ها و مینی‌اپ‌های تلگرامی هستید، بد نیست یه نگاهی بندازید.
👀
📋
اول این لیست را اضافه کنید:
https://t.me/addlist/5VAtNN0PSuQwMzc0
🤖
بعد ربات را استارت بزنید:
@gramevents_bot
⚠️
نکته:
• فیلترشکن باید روی حالت VPN باشد (پراکسی تلگرام کافی نیست)
• سیستم امتیازدهی بیشتر بر پایه دعوت دوستان (Referral) است</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6193" target="_blank">📅 01:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قابلیت جستجو در وب در ربات هوش مصنوعی وگا اضافه شد.
🔍
همین حالا بیاید و اون رو در پیویتون و گروهاتون تجربه  کنید.
😉
@T_Vegabot</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6190" target="_blank">📅 01:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">موتور جستجوی ربات
Vega
چگونه کار می‌کند؟
🤔
بخش جستجو در وب در Vega از مدل gpt-oss-120b پشتیبانی می‌کند که API آن توسط Groq ارائه شده است.
🌐
همچنین در این سایت انواع مدل‌ها وجود دارند که سرویس‌های جستجوی وب مختلفی را ارائه می‌دهند.
🛠
سایت برای دریافت کلید و تست انواع مدل‌ها
✨
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6188" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=EbKosgTSSgXPNoCFcK4_DTZGn0UbKiO7Y5Uk4qB7NhH1dO71Kp2KNm3I-SzGZSqPqamkly81PVAypcoDnYmFiEE7WzVhuzeYEx67irW52z0FcRv79c4oucYXdjUObCtwLAIDRuMkRt08o1TRnhoEn7gCqDTaR72fPSaNIbhCOmx2NGVYR0AJetOjIssyAGsw19WaufeFyMg0QXqYdIgO2y4s_kWiOHWPPaMREo0cql6345THLLz8irCBc0omW16VNt4HIDA_DvI5Vk56YOK6KH8gjwj7jkqo5CZuQQ4pwiXSbUMdGWy2hpK8Acg6ItY_ZGa8ksjTPltO10B0ssd9Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=EbKosgTSSgXPNoCFcK4_DTZGn0UbKiO7Y5Uk4qB7NhH1dO71Kp2KNm3I-SzGZSqPqamkly81PVAypcoDnYmFiEE7WzVhuzeYEx67irW52z0FcRv79c4oucYXdjUObCtwLAIDRuMkRt08o1TRnhoEn7gCqDTaR72fPSaNIbhCOmx2NGVYR0AJetOjIssyAGsw19WaufeFyMg0QXqYdIgO2y4s_kWiOHWPPaMREo0cql6345THLLz8irCBc0omW16VNt4HIDA_DvI5Vk56YOK6KH8gjwj7jkqo5CZuQQ4pwiXSbUMdGWy2hpK8Acg6ItY_ZGa8ksjTPltO10B0ssd9Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍎
Siri AI: تحولی در WWDC 2026!
در آخرین حضور تیم کوک، سیری با قدرت گرفتن از Google Gemini به یک چت‌بات هوشمند با اپلیکیشن مستقل و دسترسی کامل به اکوسیستم اپل تبدیل شد.
🤖
این دستیار حالا با دسترسی عمیق به ایمیل‌ها، عکس‌ها و تقویم، می‌تواند کارهای پیچیده و چندمرحله‌ای را به‌صورت کاملاً بومی مدیریت کند.
✨
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6187" target="_blank">📅 21:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=DOjItSo6yJ-kin7VdyieGWogprnDGwRdOPnjgRSoZjb1N3L_of2I1m4wmRNWW9EKywwvEn0N8M1rvBprD_7U7Tb0ceMBsRoCsAYnqEbIJ-lVCHCK-Ti4dlhPawEA8y3IvsvQMUfUUbjffGYrhYLvPHwsTGOxwDQZ6cbLGoYVUV4wwMfIe9v-v8EiLltgQWGL1rVUKHT7DFTFTq1UocBEwc2tEQemAaWItXNgoK3LB-JP0bpftZE58BcW_IEfBo39rj__3jlQuU4rVjy2mKpDjMLbCLSElyX9drKCXk24kEMG7DRsjkurzIIdU74ozi3XLEvkCr0slkO9y0wYo50ztw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=DOjItSo6yJ-kin7VdyieGWogprnDGwRdOPnjgRSoZjb1N3L_of2I1m4wmRNWW9EKywwvEn0N8M1rvBprD_7U7Tb0ceMBsRoCsAYnqEbIJ-lVCHCK-Ti4dlhPawEA8y3IvsvQMUfUUbjffGYrhYLvPHwsTGOxwDQZ6cbLGoYVUV4wwMfIe9v-v8EiLltgQWGL1rVUKHT7DFTFTq1UocBEwc2tEQemAaWItXNgoK3LB-JP0bpftZE58BcW_IEfBo39rj__3jlQuU4rVjy2mKpDjMLbCLSElyX9drKCXk24kEMG7DRsjkurzIIdU74ozi3XLEvkCr0slkO9y0wYo50ztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Apple
#WWDC26
has started
Watch live:
https://www.youtube.com/watch?v=hF8swzNR1-o
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6186" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M34qBj4JtODqN8b-td7K6jGBO51dGVVvNUPCvTxY-4Aeup2YlzpgPRwuxT0RwZWzQPIy4t73lLbZccbv-gDiMwIbzpcvaXd9kUC5vJqY8lYDWw5dy3EKKVNR9r29UvOD7ewlHYJxwdSEMUESUz6_FU7kvW0G9Huau5FXTonGIZMnaXuVMS3-T6Qk-bhphXAxLPi9eGtfSlYQhwJZljCVNV-75oVmLZYuV_gtxqNnfthdG3kKQbZwtOIEuTOBOjBOfDG8ZziJbhraHRwUPkhQQchKmXgX7gcTZamUuNgWOHHcY2SzkMYxR4-zCTsVJAASm_-um373tdK2BWx3OWwv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت ارائه APIهای هوش مصنوعی رایگان
🔥
از مدل‌های چندوجهی شامل متن، تصویر و ویدیو پشتیبانی می‌کند و یک راه‌حل توکن مقرون‌به‌صرفه برای توسعه‌دهندگان ارائه می‌دهد.
🔗
https://agnes-ai.com/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6185" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🤖
Kimi Work
دستیار هوش مصنوعی که کارها را خودش انجام می‌دهد
نسخه دسکتاپ Kimi Work منتشر شد؛ یک AI Agent محلی که می‌تواند بخشی از کارهای روزمره را به‌صورت خودکار انجام دهد.
✨
قابلیت‌ها:
• اجرای همزمان تا ۳۰۰ ایجنت هوش مصنوعی روی سیستم
• کنترل مرورگر برای جستجو، کلیک، تایپ و انجام وظایف مختلف
• دسترسی مستقیم به داده‌های مالی از Yahoo Finance و World Bank
• سیستم حافظه برای یادآوری ترجیحات و سابقه کارهای شما
💻
قابل استفاده روی Windows و macOS (Apple Silicon)
🔗
اطلاعات بیشتر
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6184" target="_blank">📅 19:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIKClPIf_JgScRG5EBLKGzeqTnCMqgnXrzImEimSbGERAi4ehGi5HZ1bCH7VfXvbF8bw117biBJo3uOPq7OL_0hP3F-zntThcmtovktKPphdTAtEuZm7zjylkvq49P1O6F6P7s2uCRSLKOQ3SckLnG8SfvuAJpL9ubtXwWYR-jzUj0NGW7wZC_UwuVBoNHFbHJKuPFu3s-Zpz2oB0deS7plrm3CWREVCz4vnENZ3OTN4DcYSqUFM36hxOz_qXqMkA807QewMyd9lDvNEFwpXawyz3Gg9_jTIoJspKWkZZWHz6Qqkvr_tq0cceaRvnhasAHLsD1iJLla-xw_vPjUDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
جعبه ابزار رایگان ویدئو
🔸
فشرده‌سازی ویدئو برای صرفه‌جویی در فضا.
🔸
برش سریع.
🔸
حذف کامل صدا.
🔸
ایجاد GIF از هر ویدئویی.
🔸
تبدیل بین فرمت‌های محبوب.
🔸
کنترل سرعت پخش.
🔸
افزودن واترمارک‌ها.
🔸
ادغام چندین ویدئو در یک فایل.
🔸
همه چیز به صورت محلی روی دستگاه شما انجام می‌شود.
https://www.zipvid.online/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6181" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
هکرها با سوءاستفاده از ابزار هوش مصنوعی متا، بیش از ۲۰ هزار حساب اینستاگرام را هک کردند
شرکت Meta اعلام کرد حدود
۲۰٬۲۲۵ حساب اینستاگرام
در جریان سوءاستفاده از ابزار هوش مصنوعی پشتیبانی این شرکت، در معرض تصاحب قرار گرفته‌اند. مهاجمان با فریب چت‌بات پشتیبانی مبتنی بر AI، موفق می‌شدند ایمیل حساب قربانی را تغییر داده و سپس رمز عبور را بازنشانی کنند.
🎯
در میان حساب‌های هدف قرارگرفته، نام حساب‌های مرتبط با
کاخ سفید دوران اوباما، برند Sephora و جان بنتیوگنا (Chief Master Sergeant نیروی فضایی آمریکا)
نیز دیده می‌شود.
🔒
متا می‌گوید این آسیب‌پذیری برطرف شده، لینک‌های بازنشانی رمز عبور نامعتبر شده‌اند و حساب‌های آسیب‌دیده تحت اقدامات امنیتی اضافی قرار گرفته‌اند. این حمله عمدتاً حساب‌هایی را هدف قرار می‌داد که
احراز هویت دومرحله‌ای (2FA)
نداشتند.
💡
این اتفاق بار دیگر نشان می‌دهد که واگذاری فرآیندهای حساس امنیتی به سیستم‌های هوش مصنوعی بدون کنترل‌های کافی می‌تواند پیامدهای جدی داشته باشد.
#Instagram
#Meta
#CyberSecurity
#AI
#Hacking
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6180" target="_blank">📅 18:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jewHxdnJYrpXtuCOmwOCGD4794n3WQw2IOWCL6q-j2Ph4lNOZ5tiJ1UQXSKj7blHP-ld6fEO4YyVaJZTEheXI0eRih0gws2QyMfOo4sFyOygnQkHiwgBjsHzDaywHz0rBa_8o83XQtr3GVBQFHu_5Ntzig-h3kNwyMxet-VXMsDl78ipABj1gZaj5JYG0r00gj6lThA0_rYDqKHB5PSAWpXHmEmi3jmRR2OOp2W8OolwnVNC2c_zL8-P9nfGMbnEofVcnoflN7_h7jpoLoTmiMLXTUI8K2YoPHbusfwVJL3cXrzsaDovHDDdGMD2NHx6BQMng_RYE_BDnCorXUIC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦾
شبکه‌های عصبی اکنون شبکه‌های عصبی دیگری می‌سازند — با عامل هوش مصنوعی خودکار ML Intern آشنا شوید.
⚡️
دیگر نیازی به یادگیری کد ندارید — عامل هوش مصنوعی مقالات علمی را می‌خواند و مدل را برای نیازهای شما می‌سازد
💎
مستندات Hugging Face را مطالعه می‌کند، مجموعه داده ها را جستجو می‌کند، کد می‌نویسد و آموزش را اجرا می‌کند
💥
خطاها را پیدا می‌کند، کد را اشکال‌زدایی می‌کند و شبکه عصبی آماده را مستقر می‌کند
🔗
https://github.com/huggingface/ml-intern
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6179" target="_blank">📅 18:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
کمپانی
OpenAI حالت Lockdown Mode را برای ChatGPT معرفی کرد
🔒
شرکت
OpenAI
قابلیت جدیدی با نام
Lockdown Mode
را برای ChatGPT معرفی کرده که با غیرفعال کردن دسترسی به اینترنت، Deep Research و Agent Mode، خطر نشت اطلاعات محرمانه از طریق حملات Prompt Injection را کاهش می‌دهد.
⚡
این حالت به‌طور کامل جلوی این حملات را نمی‌گیرد، اما آخرین مرحله استخراج داده‌ها را مسدود می‌کند و امنیت بیشتری هنگام کار با اطلاعات حساس فراهم می‌سازد.
💡
با وجود این قابلیت، OpenAI تأکید می‌کند که Prompt Injection همچنان یک چالش حل‌نشده در مدل‌های زبانی است و کاربران باید در استفاده از داده‌های محرمانه احتیاط کنند.
#OpenAI
#ChatGPT
#AI
#CyberSecurity
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6178" target="_blank">📅 17:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
ss://2022-blake3-aes-256-gcm:dxzSnG5le2y16bNqdyL2Hj2b9Qjptq2Ust7li7mLR6Q=%3AGZs23OkRjsO4i11hMhke9I48yENOx6VVuL23GKRXTi0=@37.32.8.201:8080#%D8%A2%D8%B1%D8%B4%DB%8C%D9%88%20%D8%AA%D9%84%20%D8%A7%D9%88%D8%B4%D8%A7%D8%AE%D9%84%D8%A7%D8%B1%DB%8C
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6177" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRrze3wackbvLjSJYbhgDkEZGsmPWPEhsoPv6DQeWiN4vOMGWXq9WY7Ia0LzdZU6VoYjFRLMpCttHDEIXzqKoHt0IPbR27O_Js0KcQpo5zQkyo8rcCMZ7fq2zypO25eFBExvtu85S8f0AC6KXhVIzLmOzugnryc8-l38pWrSAamV3t4G-rylERpIIO6SR5dwqfAPtrjrUHPkyJUdfk6Y9juXC-Cg7tQawocYVYqVRx6gS7j6JFxFTpVERc_09i6HausVRzb4L47kSroXSxRwrsqkxZSEMnqLth06WiOS7VaOLAbVx84c3Aq9N_IiSk88WuJkbE7dPseyefC7AmUWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار تازه و ناب
🔥
@ArchiveTellNews</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6175" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6173" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=AhQuy13Z-fHTCe4YOToMV10VcRArSxWvjL3MYYk0yiCAsx3lbBx5nAnFaTNdVaqO3PGLp0R89UkxuIZCwDb5VgrueBNOPkBlnZJNRoO9YaVhEh2m4m2V-cZ5sBYBiPNrTJ8msepmyCMx0ym-aDFH-aj0S-0HGiLqFOITQ2XY8k81Hce2wT1IPB7paaPT5UWd6SgYinW8_TG_uHPSCCBBNPCVLT4OslL72jLrYOMZUPyULDRRBb9jdbRwZWJCW1om-BAPETht_NvrjAoWBMQtt2zi_np1Fqqk2u7Mq5Dhl8Hwmw_ebevjp1LqHOoEGWqoF8a1CgrwvTNZ08GuR1fwkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=AhQuy13Z-fHTCe4YOToMV10VcRArSxWvjL3MYYk0yiCAsx3lbBx5nAnFaTNdVaqO3PGLp0R89UkxuIZCwDb5VgrueBNOPkBlnZJNRoO9YaVhEh2m4m2V-cZ5sBYBiPNrTJ8msepmyCMx0ym-aDFH-aj0S-0HGiLqFOITQ2XY8k81Hce2wT1IPB7paaPT5UWd6SgYinW8_TG_uHPSCCBBNPCVLT4OslL72jLrYOMZUPyULDRRBb9jdbRwZWJCW1om-BAPETht_NvrjAoWBMQtt2zi_np1Fqqk2u7Mq5Dhl8Hwmw_ebevjp1LqHOoEGWqoF8a1CgrwvTNZ08GuR1fwkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
AlicentAI — هوش مصنوعی برای ایجاد محتوای متنی
💎
این سرویس پست‌ها، توضیحات محصولات و مقالات را بر اساس درخواست‌های متنی تولید می‌کند.
⚡️
از طریق وب کار می‌کند که در آن می‌توانید بلافاصله نتیجه را برای نیازهای خود ویرایش کنید.
🔗
https://alicent.ai/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6172" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">برای مدت کوتاهی اخبار مهم رو منتشر می کنیم
🙏
❤️
کنسل شد نمی کنیم
😂</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6170" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
تهران پارکینگ‌های زیرزمینی را به پناهگاه تبدیل می‌کند
بر اساس اعلام شهرداری تهران، در پی افزایش تنش‌ها و حملات اخیر، پارکینگ‌های زیرزمینی در سطح شهر به‌تدریج برای استفاده عمومی به‌عنوان پناهگاه آماده‌سازی و تجهیز خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6169" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
ارتش اسرائیل: برای چند روز درگیری با ایران آماده می‌شویم  بر اساس گزارش رسانه‌های اسرائیلی، منابع ارتش این کشور اعلام کرده‌اند که خود را برای چند روز درگیری و عملیات نظامی علیه ایران آماده می‌کنند.
📌
به گفته این منابع، از نگاه ارتش اسرائیل، تحولات فعلی…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6168" target="_blank">📅 12:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
ارتش اسرائیل: برای چند روز درگیری با ایران آماده می‌شویم
بر اساس گزارش رسانه‌های اسرائیلی، منابع ارتش این کشور اعلام کرده‌اند که خود را برای چند روز درگیری و عملیات نظامی علیه ایران آماده می‌کنند.
📌
به گفته این منابع، از نگاه ارتش اسرائیل، تحولات فعلی یک عملیات جدید محسوب نمی‌شود، بلکه ادامه عملیات Operation Rising Lion (شیر خیزان) است.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6167" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نت رو قراره بزنن
ای‌ک</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6166" target="_blank">📅 12:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
منابع ارتش اسرائیل: آماده سناریوی حملات گسترده حزب‌الله هستیم
بر اساس گزارش رسانه‌های اسرائیلی، منابع نظامی این کشور اعلام کرده‌اند که هماهنگی کاملی با آمریکا برقرار است و هم‌زمان برای احتمال حملات موشکی یا پهپادی گسترده از سوی حزب‌الله به مناطق مختلف اسرائیل آماده می‌شوند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6165" target="_blank">📅 12:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی
💎
vless://1b5607ba-c295-43f8-923a-dc633a099276@82.47.63.98:8443?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=farsroid.com&mode=auto&path=%2Flokayb&pbk=US5uDp2cCip8cEuQUWEf4o7VbASXg45EeVia_Kz2QTI&security=reality&sid=fc0f43e6354ef57b&sni=www.qq.com&type=xhttp#%F0%9F%94%B5@ArchiveTell%20%7C%2050GB
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6164" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شرکت Wizz Air اعلام کرد تمامی پروازهای خود به اسرائیل را حداقل تا فردا لغو کرده است. برخی پروازها نیز در مسیر فرود به تل‌آویو به مقصدهای جایگزین مانند لارناکا هدایت شدند.
در همین حال، سازمان فرودگاه‌های اسرائیل اعلام کرد که فرودگاه بن‌گوریون همچنان به‌صورت عادی فعالیت می‌کند و پروازها طبق برنامه در حال انجام هستند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6163" target="_blank">📅 12:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📰
گزارش‌ها از حملات به مواضع امنیتی در ایران
بر اساس گزارش‌های منتشرشده از منابع ایرانی، چندین موضع و تأسیسات امنیتی در نقاط مختلف کشور، از جمله استان استان همدان، هدف حملات قرار گرفته‌اند.
همچنین برخی منابع وابسته به اپوزیسیون ایران مدعی شده‌اند که تعدادی از نیروهای بسیج برخی مواضع خود را به دلیل نگرانی از حملات احتمالی ترک کرده‌اند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6162" target="_blank">📅 12:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇩🇪سرعت فضایی.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/archivetell/6159" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حجم : ۲ ترا
💎
متصل رو همه اپراتور ها
✅
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6159" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4d671db5.mp4?token=a_Bx4RbhrxNyK74tdBN-48AkxrkLpMBYG8t2g2OlE8-MOfKRICMP-aaKl6s4cUXL99xPmlHdSfo9di4MgBq4M5IZsc2I_0U5JKtf_3r8q1KQeU1RuSq7BfXBLhmVCMwfBy1YIXSd3ZTJyNPo2QzqlGN_UrC9Xnb1vW_G-81lxmWyfpM_mQuxL6p-Wn5Uy_VXMgCGio2BGL_JVzZfKMdWdGU7bOWqGOODpYz6UOR88TdGHGYEXfY_sfPAUY0zudERbDI3vL2YIrACLmGqs2kBakV_h3IYUBJR6MF-v6OSdxNEw8aGBq35UrNOFhWQHIABUAPyzEs6pngcep_nJtlCAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4d671db5.mp4?token=a_Bx4RbhrxNyK74tdBN-48AkxrkLpMBYG8t2g2OlE8-MOfKRICMP-aaKl6s4cUXL99xPmlHdSfo9di4MgBq4M5IZsc2I_0U5JKtf_3r8q1KQeU1RuSq7BfXBLhmVCMwfBy1YIXSd3ZTJyNPo2QzqlGN_UrC9Xnb1vW_G-81lxmWyfpM_mQuxL6p-Wn5Uy_VXMgCGio2BGL_JVzZfKMdWdGU7bOWqGOODpYz6UOR88TdGHGYEXfY_sfPAUY0zudERbDI3vL2YIrACLmGqs2kBakV_h3IYUBJR6MF-v6OSdxNEw8aGBq35UrNOFhWQHIABUAPyzEs6pngcep_nJtlCAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📨
پیدا کردن اطلاعات از یک آدرس ایمیل - این سرویس ردپای دیجیتالی آدرس ایمیل شما را در منابع آزاد آشکار می‌کند.
🔥
حساب‌ها و پروفایل‌های عمومی مرتبط با آدرس ایمیل شما را جستجو می‌کند.
⚡️
منشن‌ها و سایر داده‌های عمومی که ممکن است به صورت آنلاین در دسترس باشند را نشان می‌دهد.
💥
به شما کمک می‌کند تا ارزیابی کنید که جمع‌آوری اطلاعات در مورد شما از یک آدرس ایمیل چقدر آسان است.
💎
فوق‌العاده ساده است: آدرس ایمیل خود را وارد کنید و نتایج را ببینید.
🔗
https://behindtheemail.com/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6157" target="_blank">📅 09:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVGaOi99hYRicgPao9udZ2GuQFD5HYFSf1fpt39NKcxHRBzKxDtQa67VTd74aXNTOfWJLDE4UWSEBrpLI2H0hESDzX-PbGkkkdJQxtQ-2y65euuKfM5BY9LmmJ8ki80flliyYiavPzf1u97l8zziNWB3VJKXX9ybPxcle-RkD6DMWyhHmfDt6Q0HoDpNEHM5ReQzmPMsyI6ORE7waOrVJOa6rVyiXdad_230Ifzyrm0tksvWwg036Zp16qkVdALXh6Hzoc5jZAF3dFcI2D4KQ0GA5znE3-OvY2hgRFrZ7ziRh6uyuKobJKz01w4Qs5B8qx8qIBpyi_fJqYVElg51qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جمع‌آوری داده‌ها از تلگرام به صورت خودکار - یک اسکریپت پایتون به طور خودکار پیام‌ها و رسانه‌ها را از کانال‌های مورد نیاز جمع‌آوری می‌کند.
⚡️
پست‌ها را از کانال‌های تلگرام در قالبی ساختاریافته ذخیره می‌کند.
💎
عکس‌ها، ویدیوها، اسناد و سایر پیوست‌ها را به طور خودکار دانلود می‌کند.
🛡
از نظارت مداوم و جمع‌آوری نشریات جدید پشتیبانی می‌کند.
📱
به شما امکان می‌دهد داده‌های جمع‌آوری‌شده را برای تجزیه و تحلیل و پردازش بیشتر صادر کنید.
💥
با پشتیبانی Telethon، یکی از محبوب‌ترین کتابخانه‌های تلگرام.
🔗
لینک پروژه:
https://github.com/DarkWebInformer/telegram-scraper
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6156" target="_blank">📅 08:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999b60eca7.mp4?token=TmUa5g1aoETJlVjcRaJXCp25FAzI44wKbhpQu8-mDismlCIZjHD0-7y5-3xFfeyp0_6UmHMEk19h_qGp6GMo8GxUOx-_en1EC37u_ITU-NOjxYdXArGI09b8dbQvHv9u8Zt9lAbodQ8X7i6hW7lFtEzhTL1MPNdEVFIt021eSUAnEmqN_ButnPRpihmwsUDptp10J1xfwA9TN4p9LnpY05jkpzUukKI_rH9oUQPgTSu7cSb6z8xcir64HAzn6e4saOfC_-JUz_4tHs2QbAm4_H-QcmwJDjWgqWuMmt8MsaLrsFndy0g226Ub7iVxpH_AZaTij4N5wBfBcHtlwjnvVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999b60eca7.mp4?token=TmUa5g1aoETJlVjcRaJXCp25FAzI44wKbhpQu8-mDismlCIZjHD0-7y5-3xFfeyp0_6UmHMEk19h_qGp6GMo8GxUOx-_en1EC37u_ITU-NOjxYdXArGI09b8dbQvHv9u8Zt9lAbodQ8X7i6hW7lFtEzhTL1MPNdEVFIt021eSUAnEmqN_ButnPRpihmwsUDptp10J1xfwA9TN4p9LnpY05jkpzUukKI_rH9oUQPgTSu7cSb6z8xcir64HAzn6e4saOfC_-JUz_4tHs2QbAm4_H-QcmwJDjWgqWuMmt8MsaLrsFndy0g226Ub7iVxpH_AZaTij4N5wBfBcHtlwjnvVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
🔥
جعبه‌ابزار حرفه‌ای برای ساخت AI Agentهای قدرتمند
برنده یکی از هکاتون‌های Anthropic مجموعه‌ای از ابزارها و تجربیات یک‌ساله خود را به‌صورت متن‌باز منتشر کرده است؛ یک پکیج کامل برای ارتقای Agentهای هوش مصنوعی.
🚀
✨
داخل این مجموعه:
•
🧠
بیش از 183 مهارت (Skills) آماده
•
🤖
بیش از 48 ساب‌ایجنت تخصصی
•
⚡
بیش از 69 دستور Slash برای خودکارسازی کارها
•
💻
قوانین و Best Practice برای 12 زبان برنامه‌نویسی
•
🛠
ده‌ها ابزار، Workflow و الگوی کاربردی
🎯
سازگار با:
Claude • Cursor • Codex CLI • OpenCode و سایر ابزارهای محبوب توسعه مبتنی بر AI
اگر روی Agentها، اتوماسیون، کدنویسی با هوش مصنوعی یا ساخت دستیارهای سفارشی کار می‌کنید، این پروژه ارزش بررسی دارد.
🔗
لینک پروژه:
https://github.com/affaan-m/ECC
#AI
#AIAgent
#Claude
#Cursor
#OpenSource
#GitHub
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6155" target="_blank">📅 08:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Always-OBITO.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/6154" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6154" target="_blank">📅 07:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6153">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-Yu-ZgWwltgZXjx94tPqvY1MdC2edkN4RZ0MRsvCZSTpPN2Mke2S7iKT6VzleJ_cZoorb_giREdtQBeTfql9nCEtQiQPlnUWdKVBYXFJs50UHos4Kp0SN_X8yqmz-aHxc-aQprrzzJvnbPQwIGVAhSAHjG1Mf3lKuI4g4z-E3RZS7LPuMyUNbLUgQUXYu-VEZmuU5dZsrsqbq0uA2AZ_wGmhD5ql6Oobh193ohR9NqqEn2lhCZ5cOJUcXaw0o-rtFro0wfF9eaFB563pKgChJjF4V1sQ3v5r1gJtDR92ig85Wlje5HNiolLIzszMuBzWdWe27Dde43DbmOi_CNG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی وایرگارد میخواد....؟!
@Sina_1090</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6153" target="_blank">📅 04:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه اینترنت ملیمون نشه؟
طرف آدم بدام*
کانفیگ فروشارو می گم</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6152" target="_blank">📅 03:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
60GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: 1 GB
⏰
مدت اعتبار: 3 روز
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6151" target="_blank">📅 01:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">vless://f5ed097b-b078-45fa-bf8b-a534f94206db@85.198.20.217:443?path=%2F&security=&encryption=none&host=play.google.com&type=ws#hetzner - heybaat  نامحدود تانل  وصل شدید دعا کنید</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6150" target="_blank">📅 01:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4DEYthOkg2dd-MX7hk9fzqvdKr896mi184oP8eSU8w6mFgxGHs0toI6X-Kb-WWaI5ieK3hsukoPl_C8K1X21RoCJIlngRLL88GSLO6teZSww3mpyufuqQq2xxOsrMUqh6L1Zi2reguiAUWXgtUUV8rCV2MgqmVNY6if83je1pK29M2RSV9y_yGQuvcQ0HD2iyHd5TSJUa-aKL2FfMXfR_Ifb8BMqFh-g_09OKakPqebbOIyUQkk2X4mlG6hf7TYi-x8WYmbq71xo1nhIzbfSmEdS6fMNb_lEhQ-2t4yGvmVOgek6IBAVt4w93AAlIAJdBALocBuNCANe2rUVvfaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم اطلاعات
قیمت هم 720
سرعت گاد
@Sina_1090</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6149" target="_blank">📅 01:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">vless://f5ed097b-b078-45fa-bf8b-a534f94206db@85.198.20.217:443?path=%2F&security=&encryption=none&host=play.google.com&type=ws#hetzner - heybaat
نامحدود تانل
وصل شدید دعا کنید</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6148" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نصب انواع تونل های DNS بر روی سرور شخصی:
curl -fsSL https://raw.githubusercontent.com/anonvector/slipgate/main/install.sh | sudo bash
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6146" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اگه نمیزنید ما بریم بخوابیم</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6145" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Fasten your seat-belts
Pack your Backpack
🗿
😂</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6144" target="_blank">📅 23:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">185.226.117.8.txt</div>
  <div class="tg-doc-extra">38.3 KB</div>
</div>
<a href="https://t.me/archivetell/6142" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ریزالور</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/6142" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-universal.apk</div>
  <div class="tg-doc-extra">16.9 MB</div>
</div>
<a href="https://t.me/archivetell/6141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/6141" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ریزالور
95.80.164.6
84.241.3.33
185.179.170.127
188.136.174.86
46.143.244.4
46.100.46.8
46.32.4.164
62.60.167.216
185.128.138.250
185.128.138.249
188.121.129.238
93.115.151.185
10.233.249.52
217.170.242.11
185.57.135.72
2.180.21.144
213.176.4.6
93.118.162.116
5.160.162.44
77.238.123.238
216.147.121.66
176.59.222.24
216.147.121.152
95.217.210.65
176.59.31.187
178.252.180.62
176.59.31.198
176.59.222.28
176.59.31.195
176.59.31.197
81.168.119.130
216.147.121.105
176.59.222.30
176.59.222.31
176.59.31.191
176.59.31.192
176.59.222.27
176.59.31.194
176.59.222.25
176.59.31.189
176.59.222.29
176.59.31.186
176.59.31.188
176.59.31.184
176.59.31.196
176.59.222.26
176.59.31.193
176.59.62.14
176.59.31.190
176.59.31.199
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/6140" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ربات تست ۱۰۰ مگ فقط با ۴۰۰ تا رفرال بزن رو لینک</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6139" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279755f66a.mp4?token=vlV0pz4swXaq5vWCWanAxV3HC_zuKO8hsfD_iJXvSSoeco9uM_nBVMDzP3aj-0TDiGqkAzHtYLPQYv1nzY0xaEdW8cFIqQgDGuJzxxhChJ4gCgCWxLYh97BdxXGYgfoxxHFaMQoVvTVvSgVAhwQUyOvGqUpQEb3Cx_G19H7NnuLANCZpFB7NjqhsU-Ll-_C3lYVQ6mgZny3CNWnwRjDT1x09KaECVic85GSHk_bfwSTFdn0Ecm43B1TBgsegcvNFABA98nW34cAi19zPvkwasmRE4IyR0nQAkS2IzlnFA5L-GnEs_IAAJWlwcJSYHyJ9r6lCYLcSBkVQhiA7MPCzhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279755f66a.mp4?token=vlV0pz4swXaq5vWCWanAxV3HC_zuKO8hsfD_iJXvSSoeco9uM_nBVMDzP3aj-0TDiGqkAzHtYLPQYv1nzY0xaEdW8cFIqQgDGuJzxxhChJ4gCgCWxLYh97BdxXGYgfoxxHFaMQoVvTVvSgVAhwQUyOvGqUpQEb3Cx_G19H7NnuLANCZpFB7NjqhsU-Ll-_C3lYVQ6mgZny3CNWnwRjDT1x09KaECVic85GSHk_bfwSTFdn0Ecm43B1TBgsegcvNFABA98nW34cAi19zPvkwasmRE4IyR0nQAkS2IzlnFA5L-GnEs_IAAJWlwcJSYHyJ9r6lCYLcSBkVQhiA7MPCzhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6137" target="_blank">📅 22:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی
🔥
vless://8879af15-f3de-4ff8-a4dd-e9ee7f33477f@v2speed.solarmg.ir:8443?type=ws&encryption=none&path=%2Fdownload.php&host=v2speed.solarmg.ir&security=tls&fp=chrome&alpn=h2%2Chttp%2F1.1&sni=v2speed.solarmg.ir#ARCHIV%20TEL%E2%9D%A4%EF%B8%8F%E2%80%8D%F0%9F%94%A5
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6136" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خب دیگه دوران صد گیگ هدیه به پایان رسید
از الان یک گیگ هم غنیمته</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6135" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df24a7408.mp4?token=VO-m-tETe9M-q0RP1W91Np9AtfOcXrQqyHSv1EGYtuOhbUOM7Za2gLMYwsjBsSgduBAEHSi3GCBjiAD8ep-GiRrX-9SNtiZJlW-X0eIqp3gjsNrIiesuWA2UfPVUKxHUA1kuYlB4bQhDnrodpqHPfCF9Y5Z8KlHNFH-xfowR_AxexB1qAVCIP6fFJqu01uUOgrgQcdyyJgoNTonYn9iRmeb09oxUVZ4oPNwwjCc3avz8Bwzr-1K5YLjkVvGpkIFeV5bRfSW2X4vfeX8Cd6D-eTiUizpKliBW_zLEWTJrWn32l3eyPQVmies-vMQD5-Kq8TFoOoQ77zClcvUM7fay4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df24a7408.mp4?token=VO-m-tETe9M-q0RP1W91Np9AtfOcXrQqyHSv1EGYtuOhbUOM7Za2gLMYwsjBsSgduBAEHSi3GCBjiAD8ep-GiRrX-9SNtiZJlW-X0eIqp3gjsNrIiesuWA2UfPVUKxHUA1kuYlB4bQhDnrodpqHPfCF9Y5Z8KlHNFH-xfowR_AxexB1qAVCIP6fFJqu01uUOgrgQcdyyJgoNTonYn9iRmeb09oxUVZ4oPNwwjCc3avz8Bwzr-1K5YLjkVvGpkIFeV5bRfSW2X4vfeX8Cd6D-eTiUizpKliBW_zLEWTJrWn32l3eyPQVmies-vMQD5-Kq8TFoOoQ77zClcvUM7fay4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6134" target="_blank">📅 22:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/043de26847.mp4?token=E8446tMyIFqecnqy2vDEHdnOWWOWJKOXbTKVkP8UGeaeoKK7DxtdSNahvgjuoEv5QN4M35_qkx4mCuID47SmzVbA7V8msXL-mr9Y5Q3wqEkL1fIctSCAVpLmU-NdARGoU9ZFmFDYaz5BW9FZHDLXf8tDFqDbMtTVLZ1oUCkgHtBcFgzumg7Rpm4GAuIFQFnFR2gA0ucnVYDxSWuIIM6TXpQn5HpA1tIgKUUXWxkpytrs33WNaRTDbV5fJkWagU7Q3Rfh1shdk4S_G-yKOJ5KLf1wUNe-bUlvCnGfqRxmA4UJcJCZRXiMRXrCop9hYp2sr5wtYOSR-QWBgIntVDgN5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/043de26847.mp4?token=E8446tMyIFqecnqy2vDEHdnOWWOWJKOXbTKVkP8UGeaeoKK7DxtdSNahvgjuoEv5QN4M35_qkx4mCuID47SmzVbA7V8msXL-mr9Y5Q3wqEkL1fIctSCAVpLmU-NdARGoU9ZFmFDYaz5BW9FZHDLXf8tDFqDbMtTVLZ1oUCkgHtBcFgzumg7Rpm4GAuIFQFnFR2gA0ucnVYDxSWuIIM6TXpQn5HpA1tIgKUUXWxkpytrs33WNaRTDbV5fJkWagU7Q3Rfh1shdk4S_G-yKOJ5KLf1wUNe-bUlvCnGfqRxmA4UJcJCZRXiMRXrCop9hYp2sr5wtYOSR-QWBgIntVDgN5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6133" target="_blank">📅 22:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6132" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">از اونجایی که بو درگیری میاد نصب کنید
😂</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6131" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حال کردید
😂
😂
😂</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6130" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">از اونجایی که بو درگیری میاد نصب کنید
😂</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6128" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/archivetell/6120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6120" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تا کمپین اوکی بشه این ۱۰۰ گیگ رو فعلا داشته باشید
پر سرعت
🔥
🔥
vless://58e82e36-32e4-4368-8742-f51446c3fd28@45.130.125.66:443?mode=auto&path=%2F476T682e67a4f84a3c838ca94R86273&security=tls&alpn=h2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%2210-50%22%2C%22xPaddingHeader%22%3A%22apinode%22%2C%22xPaddingKey%22%3A%22domow%22%2C%22xPaddingObfsMode%22%3Atrue%7D&insecure=0&host=ticket.fibernet1.qzz.io&fp=chrome&type=xhttp&allowInsecure=0#%40ArchiveTell%20100.00GB%F0%9F%93%8A%E2%8F%B3
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6118" target="_blank">📅 22:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان ببخشید کمپین جدید مشکل داره از سمت ربات
اوکی شد میذاریم
سرعتش عالیه شرمنده
❤️‍🔥
تا ی ساعت دیگ اوکیه</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6117" target="_blank">📅 21:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کانفیگ مخصوص کلاینت happ
زمان : 60 روز
حجم : ۱ ترابات
لینک دانلود
Google play :
https://play.google.com/store/apps/details?id=com.happproxy
Github :
https://github.com/Happ-proxy/happ-android/releases/tag/3.22.1
happ://crypt4/vfb1onL0njkmd47DHXNPUKKEEPQNrpfahCf5vmgczvqBX6IcP0JkObKmWDw+hAZ2VwZ21pi6REi4WyyLXGQxIbppw+LrTNA2hI/+0Mv4HBgFZV3AEzeh1kgwD0yr9nppZJsSGofePhJLN2CcRV095i4udLU52HxgvaCcMSlW+MxM5BQyQycn0iznnAt+/d3fjhtJbMsGGPwC3VAK25ERXDg4IQVlPdk1K7QOfMqddVfnbPKHx6cYrLbYlh0jQS1ya2pgxEDHAHnKBapy6ldkGRojSL5NkZ0hDNhagnbvlB6EG+7WXfXLGBG4HTDv18z8kKwMcd8SqxlQs7xoZnsmUaMDLdiy7WLZ1feY8Z0upkOTj72B1Iwj1TIShiG1ZNyvKn9pPLCrNhntsChX3ckLrAMCI8U3iIRjoTgfW3WftxxTLfTN45xFAYGkektT1C1z/v1Bs+E5FZujJdzi/rCA+RoFpO8p7CvIbbCizV+dYY5deDml/Y0aBtTcy5J/Haukal2Wsx3Rrhcb8V1+L9FM6PfN0aKuZyzZ6cEZ2BCJTSEG4CAv0PSOwqQHts5lpfRLDdE6M5em9jkYuS5sdwxU2PULK4QDUn2a4LmkW5NMWQq/QOYuNTaiPsN1QqLKsTi0eXaGC9sJNHRLFOXahzwCgnKKr+ios8lIK98MoQ0KoUU=
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6115" target="_blank">📅 21:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T34Lcsx8dQ1Gb-JbSXnYT2xsZvV_P9Ax6O7re1A_94dCemJE6w49QkHWMB6YXsJY3brpH7iF-tHXRpnHvkJtkYnwBCSHm2Fj6OPD86tYdgGpvuchXbwRYOvceWLZjROKRXFqgAb-BIrrLW2s3LZ9gSQd_tgao6C7gYMJ1JQvsbk_gIl8RmPnKcQWDdarhuNGQ3PJNCxWez4s58VP8mHZ9efIwJ8NRa12AfxNyWyfsZVV-4LRVcBAYp0teCGr2fe38ADhO17h-tkCI1QBkK54lyPRuIVDJcNevBQRFDyyFnLaBDI1jCrHBBfgftfhhaSdBlmn2Ht4KYnULvq0YiCNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
✨
دریافت 10,000 اعتبار رایگان Figma AI
اگر از Figma استفاده می‌کنید، با این روش می‌توانید 10 هزار Credit رایگان برای ابزارهای هوش مصنوعی Figma Make دریافت کنید.
🚀
💡
کافی است وارد لینک زیر شوید و Team موردنظر خود را انتخاب کنید:
🔗
https://figma.bot/4o7EDMQ
🎯
مناسب برای:
ساخت رابط کاربری با AI
• تولید Prototype
• طراحی سریع صفحات
• استفاده از Figma Make
#Figma
#AI
#Design
#UIUX
#Freebie
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
کپی پیست آزاد برای چنل عصر نوین فقط
😐
😂
🙋‍♀</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6113" target="_blank">📅 20:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🤔
آیا گوگل هنوز برگ برنده‌هایش را رو نکرده؟
با نگاه به رقابت اخیر هوش مصنوعی، به نظر می‌رسد گوگل همیشه چند قدم جلوتر آماده ایستاده است. هر بار که یک مدل جدید سر و صدا می‌کند، مدت کوتاهی بعد گوگل نسخه‌ای قدرتمندتر یا فناوری جدیدی معرفی می‌کند.
📸
از Nano Banana گرفته تا Veo و Gemini، بارها دیده‌ایم که گوگل بعد از اوج گرفتن رقبا، مدل‌های جدیدی عرضه کرده که توجه‌ها را دوباره به سمت خود برگردانده‌اند.
💡
نکته مهم اینجاست که کیفیت خروجی فقط به مدل بستگی ندارد؛ مهارت در نوشتن پرامپت هم نقش بزرگی دارد. بسیاری از کاربران از قابلیت‌های واقعی مدل‌ها استفاده نمی‌کنند و بعد عملکرد آن‌ها را ضعیف می‌دانند.
🆚
ChatGPT یا Gemini?
• هوش مصنوعیChatGPT در شخصی‌سازی گفتگو و درک سبک صحبت کاربر بسیار قوی است.
• هوش مصنوعی Gemini معمولاً در برخی وظایف فنی و استدلالی عملکرد پایدارتری دارد و کمتر دچار خطا یا «هالوسینیشن» می‌شود.
• هر دو مدل نقاط قوت و ضعف خود را دارند و انتخاب بهترین گزینه به نوع استفاده شما بستگی دارد.
🚀
چیزی که مشخص است، رقابت بین OpenAI، Google، Anthropic و سایر شرکت‌ها با سرعت زیادی ادامه دارد و کاربران در نهایت برنده اصلی این رقابت هستند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6112" target="_blank">📅 19:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba62c4ab7.mp4?token=ric_0OFm_0KtTty-zg720UnCD4U7JpuXQGengifbCHtm6qZn-Npmr1qA3cMl7Jjl5iv3AdVtOPBHNWdOloU9UNZkA5YdDeqLcIyJzPDxKH1GHMaW0ZZSP70-rRfdvOsa1fg7q-86LqFrcaeqJ4bDcM1SeMVP8xljaB3-oIuI3NI_d8q48jeBy3jm4g8b7hDGlTynNwj-XL8G9BBJtgZsKeJ622VkI-w1d5Txp_fDVE-Nh46G26zVDWZYEhNVOAbijXL2zIcyBzCphDcRTtqK0ui_HcbDWAvONIBd4RqRUuCDyJYTuwpiHiMpLZQDtMd8DUUeP1SBN0peGxg1wY7Lng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba62c4ab7.mp4?token=ric_0OFm_0KtTty-zg720UnCD4U7JpuXQGengifbCHtm6qZn-Npmr1qA3cMl7Jjl5iv3AdVtOPBHNWdOloU9UNZkA5YdDeqLcIyJzPDxKH1GHMaW0ZZSP70-rRfdvOsa1fg7q-86LqFrcaeqJ4bDcM1SeMVP8xljaB3-oIuI3NI_d8q48jeBy3jm4g8b7hDGlTynNwj-XL8G9BBJtgZsKeJ622VkI-w1d5Txp_fDVE-Nh46G26zVDWZYEhNVOAbijXL2zIcyBzCphDcRTtqK0ui_HcbDWAvONIBd4RqRUuCDyJYTuwpiHiMpLZQDtMd8DUUeP1SBN0peGxg1wY7Lng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧩
یک نوار بی‌پایان از معماها به جای تیک‌تاک
یه اپلیکیشن جدید اومده که جایگزین اسکرول شبکه‌های اجتماعی با حل معماها میشه. تو این نوار، بازی‌هایی مانند وردل، شطرنج، تتریس، سودوکو، پاسینس و بیش از ۱۵ ژانر دیگر وجود داره که به صورت تصادفی ترکیب میشن و ترکیب‌های منحصربه‌فردی ایجاد میکنن.
میتونید از جریان خبری به چیزی مفید برای مغز تغییر وضعیت دهید.
🔗
https://puzzle.express/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6111" target="_blank">📅 19:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=XYi8BRCQw35iLmtKVjpW5ZiANxGLzSl2hTiHYHVY3cnWSzbqm2EjrVnwgYvs2Ga4p_K-bTcmVHOk2WTXYaGHi2FY7sk7jDBkVfSTRsIAjKvs8wjkKlYulQ2_d6YvRhbE2-QW3VQuA8pZy4jZcMd0jqLbq-v0XdwSgy8XcW80CWmpMF1PGhd2gZizHOrLuA9oKRfcW4sCT2ZENP7CsvGUg8HMpbNn6NUvlh2JiZxbCVkXq9OPizBy7RlgbX3Y50CfaLBkR2TQRucoVNRUuWL3RZLVrBt6KPA4e8xAYViHVJmd6OakuXXqqTeKWJVn9fnfeH0bpB3GPQMkiL-Ilk1cNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=XYi8BRCQw35iLmtKVjpW5ZiANxGLzSl2hTiHYHVY3cnWSzbqm2EjrVnwgYvs2Ga4p_K-bTcmVHOk2WTXYaGHi2FY7sk7jDBkVfSTRsIAjKvs8wjkKlYulQ2_d6YvRhbE2-QW3VQuA8pZy4jZcMd0jqLbq-v0XdwSgy8XcW80CWmpMF1PGhd2gZizHOrLuA9oKRfcW4sCT2ZENP7CsvGUg8HMpbNn6NUvlh2JiZxbCVkXq9OPizBy7RlgbX3Y50CfaLBkR2TQRucoVNRUuWL3RZLVrBt6KPA4e8xAYViHVJmd6OakuXXqqTeKWJVn9fnfeH0bpB3GPQMkiL-Ilk1cNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6110" target="_blank">📅 19:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔐
دریافت SSL رایگان ۱۵ ساله برای پنل ثنایی با Cloudflare
اگر از پنل ثنایی استفاده می‌کنید، می‌توانید بدون نیاز به Let's Encrypt و تمدیدهای دوره‌ای، یک SSL معتبر ۱۵ ساله برای تمام ساب‌دامین‌های خود دریافت کنید.
⚡️
✨
مزایا:
•
پشتیبانی
از تمام ساب‌دامین‌ها (*.
domain.com
)
• اعتبار ۱۵ ساله
• بدون نیاز به SSH و دستورات لینوکس
• قابل استفاده مستقیم داخل تنظیمات TLS پنل
• سازگار با Cloudflare Full (Strict)
﻿
🛠
مراحل کلی:
1️⃣
در Cloudflare وارد بخش SSL/TLS → Origin Server شوید.
2️⃣
روی Create Certificate بزنید و اعتبار را روی 15 Years قرار دهید.
3️⃣
دو مورد Origin Certificate و Private Key را دریافت کنید.
4️⃣
در تنظیمات TLS اینباند ثنایی، محتوای Certificate و Key را مستقیماً Paste کنید.
5️⃣
در Cloudflare حالت SSL را روی Full (Strict) قرار دهید.
💡
نکته:
این گواهی فقط زمانی کار می‌کند که رکورد DNS شما در Cloudflare روی حالت Proxied (ابر نارنجی) باشد.
🔥
با این روش یک‌بار SSL را تنظیم می‌کنید و تمام ساب‌دامین‌های آینده نیز به‌صورت خودکار تحت پوشش قرار می‌گیرند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6109" target="_blank">📅 17:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC_-niCj_c2Xf2AnBrgSQutYH7V3ouJxftZ3Yaux4kyexxAEfjXCtPlsdxXZyHqUC1AqTbEJg87X8oOp6YDIAOlytsk_2-PV1feUBcjPr_JWAtTZmnJauK8fKbkQb26e6bxiDbJK5utmSS5uFrkRCLrCrlEFuX6sPhB19q5e6xl9j_FTMp0A61trcO1D_NIRI0yJsFKpkNE45GaA-a7SWGXwgJztfji9QKxWdQknJ2TWcGBwDp-wJwnAOpc_hrvESz07L0pt4CRctL5wP438OyYIQ1o3sLnHGPV-zOau2_Rn5a2xajngwRQ-3eCPlbGOt6RWeNzYYcsbR9-vz3yR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان برای پنل ثنایی و ....
قابل ثبت در cloudflare
بدون نیاز به احراز هویت و کارت و ...
فق یک ایمیل و یک حساب github لازمه
https://domain.digitalplat.org
https://www.gname.com/tld-eu-cc.html
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6107" target="_blank">📅 17:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6106" target="_blank">📅 17:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6105" target="_blank">📅 16:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انقار میگن نقز شده این سری     .</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6103" target="_blank">📅 16:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انقار میگن نقز شده این سری
.</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6102" target="_blank">📅 16:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2541bf82.mp4?token=HiiWyRPGnrTkh02sZqKVaCS24BZCBc0fHGltkfVQDtJONoBFSN0GFeszInEhl5c3oCH01-afANwRDguftxygRp7J4OxI9Eh66nGeMgUiUjPpmhdbklH11XYo2XhD2zjG2xNbJaERmgm-smvHvv0x5Uz5gd8kmZarGKEHuIYnvPwYhnZ8yb17Hzt1PypfXNFV3IkfNxtvyDC5FanItFYi2V_zhFZ78FDwB5QOkP_c67fLX6LOMnqi6RluOo8V_g7t5rOVzD3FWiH3doGbuFyV-aO6m7sBpQEqNT5h1VecZRshPXE8PxY3iOY-Ot4kJXcRqazkkWpVo2NzBzkckHkgSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2541bf82.mp4?token=HiiWyRPGnrTkh02sZqKVaCS24BZCBc0fHGltkfVQDtJONoBFSN0GFeszInEhl5c3oCH01-afANwRDguftxygRp7J4OxI9Eh66nGeMgUiUjPpmhdbklH11XYo2XhD2zjG2xNbJaERmgm-smvHvv0x5Uz5gd8kmZarGKEHuIYnvPwYhnZ8yb17Hzt1PypfXNFV3IkfNxtvyDC5FanItFYi2V_zhFZ78FDwB5QOkP_c67fLX6LOMnqi6RluOo8V_g7t5rOVzD3FWiH3doGbuFyV-aO6m7sBpQEqNT5h1VecZRshPXE8PxY3iOY-Ot4kJXcRqazkkWpVo2NzBzkckHkgSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک جایگزین رایگان برای CapCut — توسعه‌دهندگان نرم‌افزاری منتشر کرده‌اند که تمام ویژگی‌های این ویرایشگر ویدئوی معروف را به‌طور کامل شبیه‌سازی می‌کند.
عملکرد: تقریباً از تمام ابزارهای CapCut، به‌جز برخی از ابزارهای هوش مصنوعی، تقلید می‌کند.
سرعت: بسیار سریع‌تر، روان‌تر و پایدارتر عمل می‌کند.
طراحی: رابط کاربری مینیمالیستی و شهودی.
دسترسی: در همه پلتفرم‌ها موجود است.
Clypra
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6101" target="_blank">📅 15:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یوتیوب و اینستا شماهم روی همراه اول و رایتل باز شده؟</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6100" target="_blank">📅 14:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">💼
🤖
AI Job Search
هوش مصنوعی که برایت دنبال کار می‌گردد!
اگر از فرستادن رزومه‌های تکراری و نوشتن کاورلترهای خسته‌کننده خسته شده‌اید، این ابزار می‌تواند بخش زیادی از کار را به Claude بسپارد.
⚡️
✨
قابلیت‌ها:
🔴
تحلیل آگهی‌های شغلی و بررسی میزان تطابق شما با موقعیت
🔴
شخصی‌سازی رزومه برای هر فرصت شغلی
🔴
تولید خودکار Cover Letter حرفه‌ای
🔴
بررسی و بهینه‌سازی مدارک قبل از ارسال
🔴
مدیریت ساده‌تر فرآیند اپلای برای ده‌ها موقعیت مختلف
﻿
🎯
مناسب برای برنامه‌نویس‌ها، فریلنسرها، دانشجوها و هر کسی که به دنبال فرصت شغلی جدید است.
🔗
GitHub
#AI
#Claude
#Career
#JobSearch
#OpenSource
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6099" target="_blank">📅 14:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj9CyElKc_qSdIvipuPgPHZtBpFcrbj9PUuI5NRSKqGepxXkuX_WJHgElOJKFDivMILs9vlhKpMDwvcL48sU-GU9oXC2p_Iav6bIEk0rQvQV1-NwGgHrYTuvD9TKwz3oZMeSctmpaDeeJGRwp1oTsuZ_XpriafQxsY5YcGP2Bud5h3y3tL_OQqESu8gD5-Ivv0pJYRwk4T7T1SZq0Avm_0gbvxuSyjcwSVuBkYtX0kyGoqWJwN2N_sc9lOK7GMTo57BtqAdJ4zZSSf3ZBfFv3zWup46BGgj3wlZa9e9ujL8ONj_5HPUd5_RfaSjgPO5n1rAur30ZPChyE1RtcS_M9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
🔥
گیم GTA 6 بازار بازی‌ها را به‌هم ریخته!
با نزدیک شدن به انتشار GTA 6 در
۱۹ نوامبر ۲۰۲۶
، بسیاری از ناشران و استودیوها ترجیح داده‌اند بازی‌های بزرگ خود را در ماه‌های دیگر منتشر کنند تا با غول جدید راک‌استار رقابت نکنند.
📅
نتیجه؟
نوامبر امسال تقریباً خالی از عرضه‌های بزرگ شده و بیشتر شرکت‌ها بازی‌هایشان را به سپتامبر، اکتبر یا حتی سال ۲۰۲۷ منتقل کرده‌اند.
🏆
بازی GTA 6 فقط یک بازی نیست؛ بسیاری آن را بزرگ‌ترین لانچ تاریخ صنعت گیم می‌دانند و انتظار می‌رود توجه میلیون‌ها گیمر را به خود جلب کند.
💬
شما هم فکر می‌کنید GTA 6 رکوردهای GTA V را جابه‌جا می‌کند؟
#GTA6
#RockstarGames
#Gaming
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6097" target="_blank">📅 14:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نامحدود
🔥
vless://991898b1-426b-4108-9d11-188339714c53@168.100.8.115:443?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=168.100.8.115&mode=auto&path=%2Flokayb&pbk=ZqgdfgPqBr3zZuk4yw6Rtw5u1ar3pPBYooFil3IKzUw&security=reality&sid=4dc2accf4ae6&sni=www.samsung.com&type=xhttp#@ArchiveTell
https://168.100.8.115:2096/sub/4spf8icnqa5e6si8
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6096" target="_blank">📅 13:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">50gb-@lxhosein-@archivetell.npvt</div>
  <div class="tg-doc-extra">1.7 KB</div>
</div>
<a href="https://t.me/archivetell/6095" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حجم : ۵۰ گیگ
زمان : نامحدود
متصل رو همه اپراتور ها
✅
پسورد :
@lxhosein</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6095" target="_blank">📅 13:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🤖
مدل جدید Huihui بر پایه Gemma 4 منتشر شد
یک مدل 12 میلیارد پارامتری که برای اجرای محلی بهینه شده و روی سیستم‌های معمولی هم قابل اجراست.
⚡️
✨
ویژگی‌ها:
• مبتنی بر Gemma 4 12B
• اجرای محلی بدون نیاز به سرویس ابری
• نیازمند حدود 16 گیگابایت VRAM
• مناسب برای چت، تولید محتوا و کارهای روزمره
• قابل دانلود و استفاده رایگان
📥
دانلود از Hugging Face:
https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-it-abliterated
💡
اگر دنبال یک مدل سبک برای اجرای آفلاین روی کامپیوتر شخصی هستید، ارزش امتحان کردن را دارد.
#AI
#LLM
#Gemma
#OpenSource
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6094" target="_blank">📅 12:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekbh7bAE0-EOq36_5LPL_GmxDQjuYsUow58AV2MkW7Y58oq26w8Rf9NOOmAAHjt0rVvY1MdaApLXuvX-gw9qFXw_-UUkGSI4qOLHcxRx2u5pUI7tXm_wlapqTnr0AHIegdaZKM0nAFzWt7v0ka0FFKKfkjI8G8CFzRLucPuss5jYVl7PCSMZ6qD5-Sh6xlXZiBBNEpORsl0Qlv89uEXGyHPvjP71IvytKvp1_2y6TzmD-qqeQx8zznZ_eGiLG0bIbNxQHqBcIiCk_Kih1wpuSDc8AgmYLWysoGCWRXT9jIcTRNrRQ4ry-2DBKgj9xoGk2OOJb_3j7c4nJgc5-qRXlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
خلاصه کردن ویدئوها و صفحات وب در چند ثانیه
دیگه لازم نیست برای فهمیدن محتوای یک ویدئوی طولانی یا مقاله چند هزار کلمه‌ای وقت زیادی صرف کنید.
⏳
✨
افزونه
Summarize.sh
محتوای صفحات وب، ویدئوهای یوتیوب و حتی پادکست‌ها را به‌صورت خلاصه و قابل‌فهم نمایش می‌دهد.
🔹
خلاصه‌سازی ویدئوهای YouTube
🔹
استخراج نکات کلیدی مقالات
🔹
نمایش خلاصه در پنل کناری مرورگر
🔹
صرفه‌جویی در زمان مطالعه و تماشا
🔹
مناسب برای دانشجوها، پژوهشگران و تولیدکنندگان محتوا
🌐
لینک:
https://summarize.sh/
🚀
ابزاری کاربردی برای زمانی که فقط می‌خواهید اصل مطلب را بدانید.
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6093" target="_blank">📅 12:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLNEalwYF0vcU9rMzV7gIsXdeTTRwmy7YDbh_K9ckKTszP6FUnVxbuDXoE_zm5537T7ev4j0E8OXUhGY_rSqGYe7bpwye9BmTT9gRQdeQLL36LnhadaeQPH4RTJhTkxg-tMU2ZV2_TAn0DHoZjXKLJMRg4iT-NwKrku9O_ZcoAW_ht2221VWpj3FedPimm_-hZNgZ3BdYWe2ipHcaIP_DiD2yVLBbHJlfNOE1rC1jk2h4Zg19teno8DsHt3SVyS2szo0GSu2zh7VBJWQNNk3T38wyfPj4BIjK9nvc4xkXWhF1veX_DHKRWtHUK0Dqd_QoXIH24U8h9W3WECBGZMkvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
مقالات پولی اکنون رایگان هستند - دیگر لازم نیست برای اشتراک در سایت‌های محدود شده هزینه‌ای بپردازید.
1️⃣
آدرس مقاله محدود شده را کپی کنید و
http://r.jina.ai
را به ابتدای آن اضافه کنید.
2️⃣
تجزیه‌کننده هوش مصنوعی
Reader
تمام متن پنهان را استخراج کرده و آن را به Markdown تبدیل می‌کند.
گیت هاب پروژه :
https://github.com/jina-ai/reader
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6092" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📚
BooksBunch Bot — کتابخانه‌ای بزرگ داخل تلگرام
اگر دنبال کتاب هستید، این ربات می‌تواند به یک کتابخانه دیجیتال همیشه‌همراه تبدیل شود.
👇
✨
امکانات:
🔎
جستجوی سریع کتاب‌ها
📂
دسته‌بندی بر اساس موضوع و ژانر
❤️
ذخیره کتاب‌های موردعلاقه
🔥
مشاهده کتاب‌های ترند و محبوب
🎲
پیشنهاد تصادفی کتاب برای کشف آثار جدید
📖
رابط کاربری ساده و شبیه اپلیکیشن، بدون نیاز به نصب برنامه اضافی.
🤖
ربات:
@BooksBunchbot
⚠️
قبل از دانلود یا اشتراک‌گذاری کتاب‌ها، قوانین کپی‌رایت و حقوق ناشران را در نظر داشته باشید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6091" target="_blank">📅 23:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
200GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6088" target="_blank">📅 22:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
آپدیت بزرگ UAC Spoofer Android منتشر شد!  نسخه 1.0.5 با امکانات جدید برای عبور بهتر از DPI و فیلترینگ:
✨
حالت‌های جدید:
⚡
Fast
⚖️
Balanced
🥷
Stealth
🛠
Custom
🔹
سیستم پیشرفته Fake SNI Probe
🔹
تنظیمات حرفه‌ای Fragmentation و TLS
🔹
ذخیره خودکار بهترین Strategy…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6087" target="_blank">📅 21:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 100 گیگابایت
🥳
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 85 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6086" target="_blank">📅 21:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100 گیگابایت
🥳
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 85 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6085" target="_blank">📅 21:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚀
آپدیت بزرگ UAC Spoofer Android منتشر شد!
نسخه 1.0.5 با امکانات جدید برای عبور بهتر از DPI و فیلترینگ:
✨
حالت‌های جدید:
⚡
Fast
⚖️
Balanced
🥷
Stealth
🛠
Custom
🔹
سیستم پیشرفته Fake SNI Probe
🔹
تنظیمات حرفه‌ای Fragmentation و TLS
🔹
ذخیره خودکار بهترین Strategy برای هر مسیر
🔹
امکان وارد کردن کانفیگ‌های شخصی (Manual Mode)
🔹
منوی فارسی
🇮🇷
و English
🇬🇧
🔹
افزودن Certificate داخلی
🔹
بیلد و انتشار خودکار توسط GitHub Actions
🔹
لاگ‌های پیشرفته برای عیب‌یابی
این پروژه از کانفیگ‌های VLESS و Trojan پشتیبانی می‌کند و با استفاده از Xray داخلی، VPN محلی و تکنیک‌های مختلف SNI Spoofing برای دور زدن محدودیت‌های شبکه طراحی شده است.
⭐
اگر پروژه براتون مفید بود، حتماً داخل گیت‌هاب بهش Star بدین.
🔗
GitHub:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6084" target="_blank">📅 21:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">😎
پروکسی‌های اختصاصی آرشیوتل
⚡️
پروکسی ۱
🚀
پروکسی ۲
💡
روی لینک بزنید و گزینه Connect را انتخاب کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6083" target="_blank">📅 19:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-6OJ6RpyVCxjLeBD1__1FUZxuegOxaNg7-s3mmeatss-Pe_ZmS5N_JXiPrSUBpX2GTRdNJBzhEy0EsHr4SQeLKQFICfsCipZbcRjNflTmTA5HSc2ar-wXkb3MltMYUTPvXSX_9SMGYvJHmWaj44ucgSPcQtAMOIH79v3vbZm8cUl6Xy4R2-rywE5pzfZryLsJTXHeL3NOMVuPk97xLcTtp-5s-YqMI4f1xaHpYTZB3kGwNBVPo2xYSdXz4ISXiZ82mFyHqbOIrRIl4ZUVBmnVHn8hgaVq4n9nj6WxfRMFSVzeZR-nxVbxBQXDLN0dXk4MkkyoQ-6t7lGTYEiaheRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📄
✨
آپدیت جدید UPDF منتشر شد!
اگر زیاد با فایل‌های PDF سروکار دارید، نسخه جدید UPDF چند قابلیت جذاب مبتنی بر هوش مصنوعی دریافت کرده که می‌تواند حسابی در زمانتان صرفه‌جویی کند.
🚀
🆕
امکانات جدید:
🤖
AI Copilot
تبدیل، فشرده‌سازی، محافظت و مدیریت PDF فقط با نوشتن یک دستور ساده.
🔍
جستجوی معنایی هوشمند
فقط دنبال کلمات نمی‌گردد؛ مفهوم موردنظر شما را در اسناد پیدا می‌کند.
📑
AI Bookmark Agent
ساخت خودکار بوکمارک و فهرست برای فایل‌های PDF طولانی و چندصدصفحه‌ای.
✍️
AI Editor Toolkit
بازنویسی، خلاصه‌سازی، گسترش متن و اصلاح محتوا مستقیماً داخل PDF.
🎨
AI Creative Studio
ساخت استیکر، مهر، واترمارک و پس‌زمینه‌های اختصاصی با هوش مصنوعی.
📋
AI Page Management
شناسایی خودکار صفحات خالی، چرخیده یا دارای مشکل تنها با یک کلیک
⚡️
برنامه UPDF کم‌کم در حال تبدیل شدن از یک PDF Reader ساده به یک دستیار کامل مبتنی بر هوش مصنوعی برای مدیریت اسناد است.
updf.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6082" target="_blank">📅 19:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc7ad03ba.mp4?token=r5tp2D9NTxr7f2EzSqOPno6OT8CXYkZUKPe0EqGabWaIHKkOA6WiWL1qS1mM-9U1ESyPHuCQFL4dm4HHdhEKnWXgNhJy3zGn51je9Mcqb6_q3qrHOS_-xhzJJ8yEO_WxJndT4AM0v3X9SJzywL-KMB3v1ZNGNrGL2D_BImD4XWvbZmryybvgjJxdHuLD-HrErNL8Av6wsq1aJqeTJydHkC_D22gWN8-TV-1jvFE8eHvz7NGLL1z-rwwvb91tcf0dyQoCHfaKvPv033BT3mpz01BhucsXHqdIiRfMf28HJUbosJEMe7bP52OrJy-mHP9lpgTFtIhRd4l8f0KJuQUSlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc7ad03ba.mp4?token=r5tp2D9NTxr7f2EzSqOPno6OT8CXYkZUKPe0EqGabWaIHKkOA6WiWL1qS1mM-9U1ESyPHuCQFL4dm4HHdhEKnWXgNhJy3zGn51je9Mcqb6_q3qrHOS_-xhzJJ8yEO_WxJndT4AM0v3X9SJzywL-KMB3v1ZNGNrGL2D_BImD4XWvbZmryybvgjJxdHuLD-HrErNL8Av6wsq1aJqeTJydHkC_D22gWN8-TV-1jvFE8eHvz7NGLL1z-rwwvb91tcf0dyQoCHfaKvPv033BT3mpz01BhucsXHqdIiRfMf28HJUbosJEMe7bP52OrJy-mHP9lpgTFtIhRd4l8f0KJuQUSlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎵
🤖
گوگل یک مدل رایگان برای ساخت موسیقی منتشر کرد!
Magenta RealTime 2 (MRT2)
ابزاری جدید از گوگل است که می‌تواند کامپیوتر شما را به یک ساز موسیقی هوشمند تبدیل کند.
🎹
⚡️
✨
قابلیت‌ها:
🎼
پشتیبانی از ده‌ها سبک و ژانر موسیقی
🎹
اجرای زنده با پیانوی مجازی
⌨️
کنترل و تولید موسیقی با دستورات متنی
🖱️
واکنش به حرکات و تعاملات کاربر
🎷
شبیه‌سازی انواع سازها و صداها
⚡
تولید موسیقی در لحظه (Real-Time)
🎯
مناسب برای آهنگسازان، تولیدکنندگان محتوا، بازی‌سازها و هرکسی که می‌خواهد بدون دانش تخصصی موسیقی ایده‌هایش را به صدا تبدیل کند.
🔗
امتحان کنید:
https://magenta.withgoogle.com/mrt2
🎶
آینده ساخت موسیقی هر روز بیشتر به هوش مصنوعی گره می‌خورد.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6078" target="_blank">📅 18:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFRGD9mg1GAjsOpE-WvAWMwBoCMxo7-DxCtodI4eNBfjJv6TrISjRKnObFYl8wY9uOT9-sVBFuX3leq_VT6ORdHYCxm7aFiLjnTwbK_naFonsSSz_eDWNZ1rNA7JAJHuFzpoAfhQDjo3Bx0rvt-TU1btHIm77_NMY1wi5B_6TIbbWC3LTJUq17_W24iRbszKmuuKMixrOzpZhAylPuiNJrJ0XFJbbvZP-u3aGIWtZOvWfIP0rO3-OCwrC5KVsvX31rZhmiWiaknAi5quAwb9SUvC_3y3-25MqmLXcRAjQ40kxuJFr-hY0XSiXW94J0zUODDZD5WcKnvkhTGnf77g-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه اندازی پلتفرمی توسط OpenAI با نمونه‌های کاربردی ChatGPT
🔥
در این پلتفرم حرفه‌ای‌ها از حوزه‌های مختلف تجربیات خود در کار با ChatGPT را به اشتراک می‌گذارند. آنها توضیح می‌دهند که چگونه شبکه‌های عصبی کارهایشان را ساده‌تر کرده‌اند و دقیقاً در چه زمینه‌هایی کمک کرده‌اند
⚡️
🔗
https://chatgptpro.substack.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6077" target="_blank">📅 18:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">زمان : نامحدود
حجم : ۱۰۰ گیگ
متصل رو همه اپراتور ها
✅
اتمام حجم
❌
vless://d601f422-a626-4533-a3d9-8fddf16517b5@171.22.136.84:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#100gb</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6076" target="_blank">📅 16:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
80GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 80 / 80
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6075" target="_blank">📅 14:55 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
