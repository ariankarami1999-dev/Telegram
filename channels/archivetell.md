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
<img src="https://cdn4.telesco.pe/file/l6CZm4Ux9hx7PQIFTr-k2AyYKQ-vbWgpfswCUHUKmBymnYgbgpefuSvmRuLLFqED-BcxU94hZMGqNn8kUyV48Cu_k0nKlV-MjvU_P4DCmr4_8ZAJ7GIuKNlzVuO6vwuoFsxZr5wM5On1JKV4iVD6fEMH3YzsvD0AJN8JmZytsgI3r9uNTetJ3CDMC0oGGVMXOYV48oW_xWWRsMTFW0zXQPY8xlhmdWiMj3fnLvFbp_vP1I6GqP41jMqlbKH47tvUNWWiplfQh0Yr1rsap6E8lnXKUYe0hCaeYA06P9lGZ8CP-BfuoBQLf4JcLx_k-d3n--it_Ui3lJQIgA_HgV9wPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 14:01:41</div>
<hr>

<div class="tg-post" id="msg-7759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/qrSgyzUKla6Go8DkdwrUMAi_ZFFJbmMc1b3XhtmyMRn-BkKLx10weOVJrP7Z2f7N-RDceLn2_jgkb-Wv9KJ07CdVR24ulp4lrTLkDKYTbJ6uXVo-pJc3S0nS6pZOBbZw4lR0OwMqFQidcmXRtCP6OZjCIerovPVkfstZX8VA_pAB58TA_6EKPfBs5txffrg6Iy6-5QaB6qUdgdsuBkDN4RfNy8VU6QxkQzQObh4G9GXWqixRQQnU8Jm_lF5HMPCDK9s4rLggw3-1d3ilmYs4eHmdlowWoXnmf5Ky9Q4Kk6DOvOXkrO3i03oGhESe6eMnXZ2oP26dDrTuJUbv1UiPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/jyozIDaN_TyqXdEPChu4iQ_Z-zDufPYMHiV6OJimJCPONxBFIeQgUBv0ua6tfr9MWb21Pk2xmzAMI0TitEApDqTuDVKl3soVZOBkEuZwMtjrnghB1KFF4NVArZJpmKsbms0O0138NL6cBHgN5gvUsLpbAVNpLIU3IDqAetef6lToAVQB5Zpzg8x_cnHvilXwaoIQ4F3Pgjmhk2HRnbgzEcEx11KWk7AxDhpcbbLhuMzDHdjqss4dtSZZ64kLGlsWLrtmPmCitYgzhGq8z1tYbULka2_NLBh4kQT2afXRgMLd2i16u1B7TsdtcIKdxU02RZqbJXaSKKMIZLCMOHNh3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔥
کلونر اتوماتیک و خفن تلگرام روی کلودفلر!
‏بچه‌ها، این ابزار Serverless روی ‌Cloudflare Workers⁩ بالا میاد و خوراکِ کپی کردن و همگام‌سازی کانال‌هاست؛ بدون نیاز به سرور و کاملاً رایگان.
‏
امکانات اصلی:
‏•
🚀
دیپلوی تک‌کلیکی:
بدون دردسر و سریع روی زیرساخت کلودفلر بالا میاد.
‏•
⚙️
فیلترهای پیشرفته:
می‌تونید فایل‌ها رو بر اساس نوع (ویدیو، عکس، سند) یا سایز دلخواه فیلتر کنید.
‏•
🤖
چند بات همزمان:
هر تعداد بات که خواستید اضافه کنید و تسک‌ها رو بدون محدودیت مدیریت کنید.
‏•
⏱️
همگام‌سازی لحظه‌ای:
هم بکلایت تاریخچه رو انجام میده و هم پست‌های جدید رو هر دقیقه سینک می‌کنه.
‏می‌تونید سورس کاملشو از گیت‌هاب (‌
iamLiquidX/telegram-clone-worker⁩
) بگیرید و با یه استار حمایتش کنید.
⭐
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/ArchiveTell/7759" target="_blank">📅 12:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7753">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/QEMs3wGNt05mH8nMKRmsgSiK2D9Qk0P-S7dezSY_54OJMF-3Qh8o7H5wTGh4epYqeutDlw76i0BiuTOy0uf-o_wioiVzBTVO-lVuDaP3Kq7E5Sh2Rdd8tNlCgiyd-McKgG-veWVpcNHjRKBzkBS38T4TyhMg-ZGZuokEEkgtZmV1AiYxzo0Uu1r4taYV4fT64__aprsqAYJCvlVwx-aObXcTlxBDgSZTQJGMaBWVaiAhJRNbjQgSa9tgzp92spK0Mjak9t6DcUvslxI4gPXnYPn7a25d_uwMTbjnCVFx00kEwPZ_TU9XMSb9XZuefAZomGzU-yxRczukI9HtSeps7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/XLP6DW9UkuWBVOFW8Q9aWPHRytDEk49TOilvW7BlAfcaVQMWnOCMsxxlAvgJXbgXdY9nhsmWrCFtbkhjz1VdCKtHHjvq9z80uy6uAO4dVr6orN2_KvpoZsfky3ZFOAyGNlt8J--bgctMEiDvZ4iiCfZBJ_uPe12N3EgfyXI3Jnqqzc8snBdU_Bncz55quO-ZEXIHI3DumcnQwQeEwytUMcpSlqgPdOhGPrWxafZ9LZp3c2FBRaZceeww9TaT6FiZ4HWmPxjP2p_B7otOU-Bpr1GHHNj_qYOEr28xp1bsFNKFaJufv7LTcjU563sENblE9svmY_OV9sYxHmgiMNgVbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/qvt8O5Ruj4GAJwbswMC2Xem5dQ9hv2ktUjYKPt5zRNJcW9PDGt2HmJF1wdlCNLO3ALg0_sOdIYswkVgp4ahcBgx_vUFC6DhcEgsVHeOnWZbuRBnp5LptLRiYbp5WXCjJ0wwKjy6aB6rISpGyOx4ArMBlk5zelQXkpblypup4egymuHXK3S9t-VButEmqY1pqczSE_Sdo-rRAtlZtpzfkjXrr-QfHvupKEWLIZaqMjdx7184xL4dqGlUS4wajPoRRoFWIKmydoVJTLO45-OTqnUIOlA3kfzgHfxqyLSgd_03yGIpJoCCpxnvMz-vzySPNGLJi6mLxK80n2EVvFx4HXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/NvNWnm7jBFeEBCr0bBuYWAvtG6z685YhGUgAU0KFFmjLTMpnuszYSrsIF4fWL324uP_Ph8i1U--he0OsmRMDCd18PzJ8Tr31nHSN-ni1wWD7tsX2PKoxqZrOVhccAIawA0FFFICO7WGTCzooIp0WfcskkmoQw-Xe1pgqmHxXrwy_D-YvX_am8uGxLV6nbXQW5Dl-aamNe5b_J1w3nLHi_k2EmKG5-CDBlFasoZlV_FDkFNHbVC7toY7buIpxi7xCS7dtyAy99ge1pstSy_fHf3XAYsyY_FspLjvnTbOnLpRAPETgFde1PzZ5nP32ZJsBHF6UwdaTrEYaEZT2-2vvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/JJatWEnFm2pl-xVIOwYLcS2crj9jJHciUr4pDFhRH1EAnQPHj-Pmf4uEmfGeT6MCpHjZwNXqjVgDt2h65eU7O1MmWqMVsxkR06zMmsZkZjiTpP8Wv3sor3q06tYL2YrhWrsb_hfMfCRoYYaMmDQ7I8jpbrFWGkCjJ1mU37JYkrWxgN33pKRgCOvKRZl5MFdni5xNIAZoM-ZHp6eXX4mMCKpLdrsvxNQzb8N4ehd71s71Ctg0K0LejRsw_R1vcsjfE_yWw6DKpCy5gZHmcYbKFvUVtvrCOJP1M2OVoJjrMXAF2Ig0gTBG23geW1a6euyyZf7RYaQsa463JLBhASeqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/uCOWmx4ZWqI3aZv3wcL8qD1Sq4AGoRZvBHXVo1KxsPb6oPlKXHYr3jmISBl915sD_FRa_HPBTbbcJXzbxATDxVd7P9Lh4Xp7RBFaRlDzYMNSdqb1vuJEFly7xD8KzIgi0rfDokfBiDdHR39Vksj1ZYxoPETc8VDC41oZ5goJVBHDRoKp8kpH2TnMfI3xiWGFzWv7xEsovA8nESHYo9uHBY8DTFe2qcs8mN2HZzE-dMuBsR6E0Z3vd2pNc1JuJyP67PmMpe5SUhklPUXBVxl0cjP2H8x9uAXsrfrAzSJfoueEhBgllmvD8iUzltT7B12Wwrqme_N18xz85fLJFCiFuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.
یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار بیشتری به دست آورید. نیازی به کارت اعتباری نیست.
1min.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/ArchiveTell/7753" target="_blank">📅 10:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7752">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⌨️
؛ DeepSeek V4.1 Flash، Muse Spark 1.3 و GLM-5.3 Flash به صورت رایگان در Cline Desktop
​تیم Cline یک برنامه دسکتاپ جداگانه با تمام قابلیت‌های یک عامل مستقل را راه‌اندازی کرده است.
​
📌
امکانات برنامه:
🤔
استفاده از ClinePass یا کلیدهای API شخصی
🤔
انتقال یکپارچه وظایف از Codex، Claude Code و سایر عوامل
🤔
برنامه‌ریز برای اجرای پس‌زمینه عامل
🤔
مدیریت سرورهای MCP، پلاگین‌ها و مهارت‌ها
🤔
مرورگر وب داخلی و ورودی صوتی
​
📌
مدل‌های رایگان موجود:
🤔
DeepSeek V4.1 Flash
🤔
Muse Spark 1.3
🤔
GLM-5.3 Flash
​
📌
نحوه شروع کار:
1⃣
دانلود برنامه:
https://cline.bot/desktop
2⃣
نصب و اجرای Cline Desktop
3⃣
ورود از طریق حساب Cline یا اتصال کلید API خود
4⃣
باز کردن پوشه کاری پروژه
5⃣
انتخاب یکی از مدل‌های رایگان از لیست
6⃣
ایجاد یک جلسه و اختصاص وظیفه به عامل
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7752" target="_blank">📅 01:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7751">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmwsB4sPTx9EVC7Naz7jsgLoO08T4YBgL1pZ2OUpsGHRnlnjFFkeuR6nE5mYxS0z3jdw1nGqfDybw6bW9uunG6aKasConmMErIaZ1m6ekpQuH3CNxNw6lcD9vBZe4meiNtEuH_h5CAl9vTTma21yxZJ-Q8f4LHRYJb6N-gCCQo8d4Py8jeBMLC2n-Tx-MeUYWQjhR8she2EF34I6JfyIyxM1C7Xg-9WtWETsOcs6-TCVfoLW8eFYDtb5DU_0v6vH_j5paIqq00KLEx-CiPV1VVIoCP6Zwm2IfepsVQ-vYRwdNYDak_FJTx0WCG_HalBRH_rOPSHsWvtqlo7Kez8lzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
؛ LIGHTVELA - یک هوش مصنوعی رایگان که 24 ساعته در دسترس است.
4500 اعتبار و 100 میلیون توکن
مزایای طرح رایگان:
🤖
1 هوش مصنوعی
💳
4500 اعتبار در ماه
🖥
2 پردازنده مجازی + 4 گیگابایت رم (محیط تست)
💾
50 گیگابایت فضای ذخیره‌سازی
🌐
دسترسی 24 ساعته
📱
ادغام با تلگرام و سایر پلتفرم‌ها
نحوه دریافت:
به
lightvela.ai
مراجعه کنید.
یک حساب کاربری ایجاد کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7751" target="_blank">📅 22:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7750">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کانفیگ مخصوص چنل -
سرعت خداا
vless://e4b11ac9-46f7-4cc0-92ed-bb9dfaaf3600@94.237.92.65:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=lkMM9FR-o7Z6NwmmQVK8rLhCQR1mbJTgjY_0upeS2SY&security=reality&sid=0436301fb0178b&sni=google.com&spx=%2F442987454d44398&type=tcp#@ArchiveTell
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7750" target="_blank">📅 11:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7748">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BAUjytIBLEg27Olf4-Nkjr-cJXuA4fQunPGLAn-YrHjb_tUiEpSSd2eoiI-iYJ8K67aghglTmaagc8GtMCXMG7yqMEDUMWPBYvdvRvz4dlHvZ_K1I6EzUga9EIDa4jWZeJVliE8K46uhJqjy4l4EroSpEGHeshb1BJCaTd2cImwmMSPULDsSxY5aDRmAUdH03Q9hGD5FreomOCQcV58UDekRqSwoQq5IUvyzB4aiOC0N6p6wxWEh9zeKv_m3vzDmeGFOxGpjf4PZzQgYVba6_ytl1_GgTDO0CTNwmFLyEOU-z7WNxHLMh4LWiHffFD4RnAtEqvJvjKpzJC87Gmf4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
از تاریخ ۱۴ تا ۱۶ سپتامبر، با ورود به
Z.ai
؛ ۶۰۰ میلیون توکن GLM-5.3 به شما تعلق می‌گیرد، بدون نیاز به اشتراک.
🔗
https://autoclaw.z.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7748" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7747">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZqwunYsRmE7pDltaTy_cum0zywF-CVjTyGJ3AofPCHe-zN6xyhXlI43CnF8Jiu5XfLRbRZqMn129BoYVmi6R5EWlzSWubiI48EQy7apUEj95H3UJwetKgyAciwyxPvJWVveaOstMjNNZmwlsyZmCy1oYwaeGvbQQgBX4Pn8p_-zpPCnjmNNBF1CqvYzp9dqxkQ1mQDJFvGcyW-FnnAaST8eRXiQBA7piuaPAyAlCA0VxXNu1qVeG4qDyeS0iB_O_5h7CdyIQKwGWZU5xVlHLWa8bwKspyiKG3X-0xV6Q0lwuWtVBjicisEqTpLRSL6yVeRqPdgbEZjrf5cNtAz363g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔓
رفع فوری خطای ریجن و تحریم Antigravity
اگر موقع کار با هوش مصنوعی Antigravity گوگل با خطای تحریم ریجن یا گیر کردن روی Eligibility Check روبرو شدید، ابزار متن‌باز
Open AG Patcher
در چند ثانیه این مشکل رو حل می‌کنه:
▫️
رفع محدودیت ریجن:
بدون نیاز به دستکاری یا تغییر کشور اکانت گوگل
▫️
پشتیبانی کامل:
از Antigravity 2 و Antigravity IDE و ترمینال (CLI)
▫️
امن و خودکار:
اجرای پچ با یک کلیک + بکاپ خودکار برای بازگشت به حالت اول
💡
نحوه استفاده:
ابزار رو اجرا کنید و شماره نسخه مورد نظرتون رو بزنید تا پچ در چند ثانیه اعمال بشه (سازگار با ویندوز، مک و لینوکس).
🌐
دریافت ابزار از گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7747" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7746">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m82_Env1Xx3vBnMvXQ7KYMDJ_K1Dfus2n_lY0Nv18SMTwCp9_OXmp-yaFGPCvGX84eRMS46tdi0SooStwptOYzqOj7MVLXBvNCeEEopvokCIJBjw6rUUC3pW_p3zqVYgKePzcNSOh7tqZ0ipIYmXeNtPN5utPhWHz4eMr8FBaLh9qB26vnPRkN0QqdmCyCIdpzPw8AnkAp38n3J4uFgTQTUVSXBFk-Y7JS7rqJ9NHv6RhmIUuIbsyyL6foAl1CkGTPprtVX4lrVl1B0gBQDGVSgh6e-J1P4A34di9Jcg_YTIJGNdDojr818xoFjWjxr7wZshVZ-L93Iu9GFH6mQ9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نحوه استفاده از Claude Opus 5 و GPT 5.6 Sol
به صورت رایگان
📣
حساب‌های جدید در
Verdent.com
، یک دوره آزمایشی 7 روزه با 100 اعتبار رایگان دریافت می‌کنند
💯
🆓
🎉
✍️
آنچه دریافت می‌کنید:
👀
🔍
☑️
Claude Opus 5 / Sonnet 5
✅
GPT-5.6
☑️
Gemini 3.1 Pro
✅
GLM-5.2
☑️
Kimi K3
📌
نحوه دریافت:
🔥
⚡️
☑️
به
➡️
🔗
https://verdent.ai/
مراجعه کنید.
✔️
برنامه دسکتاپ یا افزونه VS Code را نصب کنید.
☑️
یک حساب کاربری جدید ایجاد کنید
✉️
✅
مدل مورد نظر خود را انتخاب کنید.
☑️
از اعتبارها برای شروع استفاده کنید
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7746" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔥
KiraAI
روزانه ۵۰ میلیون توکن رایگان
🤖
مدل‌های موجود قابل استفاده :
⚡️
kira-3.5-pro
⚡️
kira-3.5-flash
⚡️
kira-3.0-image
🔗
kiraai.vn
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7743">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔎
scite.ai
— موتور جست‌وجوی استنادی برای تحقیق جدی
۷ روز اشتراک رایگان (تریال رسمی سایت)
📑
Smart Citations
نشان می‌دهد هر مقاله توسط مقالات دیگر تأیید شده، رد شده یا فقط اشاره شده — نه فقط تعداد استناد
🧠
Assistant
پرسش پژوهشی‌ات را می‌پرسی و پاسخ با استناد واقعی و لینک به منبع می‌دهد، نه حدس
🤖
دسترسی به مدل‌های تحقیقاتی:
Claude Sonnet 5 | Claude Opus 4.6 | GPT 5.2
🎛
Personalized Feed
فیلتر و شخصی‌سازی حوزهٔ تحقیق ، فقط موضوعات مرتبط با کارت را ببین
🔗
Custom Dashboards
داشبورد اختصاصی برای کلیدواژه، نویسنده یا ژورنال خاص + هشدار مقالهٔ جدید
📊
Analyses & Topic Classification
دسته‌بندی موضوعی، شناسایی روندها و گپ‌های پژوهشی
آموزش فعالسازی
🔗
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBBaJanCbFvTXwn0BwnhltxIAuejvH5b7BeuqOuffY0UbAKtnWj378i_NbQfwLDZOp2rrLXo_7QGWxwJePm0t_ZQoCbs48QOXAdj2Brk_hyueK0Vj4SP2Ra7XwANfQ4geEBgEh-AHDjrEUGfufhe6M2OMoWCbn6c9I4VG8FdXd54BTwXPBH9mpAQhhTtvfvLD595Um6Ig1flhODRop56pCYrR-XRv88wSSozFaIa6ONhosDM05bfynfMTVLL8LTYDEBdDp29XSxTJErAajvbJxxtNiAu2VrIBVTcJiCv7AKLtToOuZVyWsRXooZ0h81JqD9pO8l8fMPupX4Dy80xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">keys.txt</div>
  <div class="tg-doc-extra">2.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان  claude-fable-5 | claude-sonnet-5 |  deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید  @kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url: https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz-5TWDl1u1bBo8DjDtnvzJh57BsEH6mrey_xkuY8pcFzqQHZ92DrZFWEPYP__i0bwW70T9qEqno8si72LdA1L6RatEwxRW8PWbw8oLYBVPj0FXMXGfaC87AbDMjuTDAGQB9dn1gE_2lNTW1C2fOhUHB5iTK2T3xkbUBNBFTnx3RcGn_RBVXPEVwHraY5GoGOnKlCzKyM_PnfXltv9lMYYQBXMQ_CBc_W7hXUo5JHFEo1_F6JIRXM2lPmvUiK-48QibcucanGDLqmayHnt2AeVUmkWVGQaEYtktW0iFW-c0ayWLjrlKArHyJ-nXZ57JrfeCYhUCuJrcL7cAnyyP4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
دامنه رایگان همیشگی بدون کارت اعتباری!
‏بچه‌ها این
پروژه گیت‌هاب
با نزدیک ۲۰۰ هزار استار، دامنه‌های رایگان دائمی میده که واسه پروژه‌های تستی و سایدپراجکت‌ها کاملاً خوراکتونه.
🚀
‏•
دامنه‌های متنوع:
پسوندهایی مثل
.us.kg
و
.qzz.io
بدون هزینه فعال می‌شن
‏•
کنترل کامل:
دسترسی کامل به
Custom Nameservers
و تنظیمات
Cloudflare
دارید
‏
💬
نحوه استفاده:
کافیه برید به سایت پروژه، اکانت بسازید، دامنه دلخواهتون رو ثبت کنید و نیم‌سِروِرهای کلادفلر رو ست کنید.
‏
🔗
سایت پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⌨️
ترجمه سریع و هوشمند، بدون دردسر!
اگه دنبال یک مترجم ساده و کاربردی هستید که فقط به یک سرویس محدود نباشه، پروژه Translator می‌تونه انتخاب خوبی باشه. این پروژه با پشتیبانی از سرویس‌ها و مدل‌های مختلف ترجمه، امکان ترجمه متن، استفاده از قابلیت‌های صوتی و مدیریت تاریخچه ترجمه‌ها رو در یک محیط مدرن و ساده فراهم می‌کنه.
🤖
قابلیت چت با هوش مصنوعی؛
با استفاده از API Key با مدل‌های هوش مصنوعی گفتگو کنید و پاسخ‌های هوشمند دریافت کنید.
🔑
همچنین امکان استفاده از API Key و ترجمه با سرویس‌های هوش مصنوعی مختلف رو داره.
🌐
نسخه آنلاین:
https://codewave4.github.io/Translator/
🔗
سورس پروژه:
https://github.com/codewave4/Translator
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=mv7X7sF7G6I_u6ekerOYEoCYlaqnEr9RSYjkQoPbt5IL_z7QxXILA84OFliMjP7qBiSjYc0Zxg_mYm51nQn6W3DlZVznqvL9BVS8WsREgCJQAuMrFT731egJgxG1u0K0GoEapMFB-977-sLwMInIsiv-pXdfvDNnctxYrO9svhOaQeba8WZt9rH2HWa9TsyLm81CNgG9I1_MrxtnROXwVQloqfawn4L_ymxKtNhTgfmwbmKgiSYALJ0irw4P01Obd-0HYGnIjvSJ11GalceHmhze_zMyEKJ5WYyPDGswDnOXecbTTu5mIZeK6LNYGxlEYMSt9a5OG7szo_cWCnkx_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=mv7X7sF7G6I_u6ekerOYEoCYlaqnEr9RSYjkQoPbt5IL_z7QxXILA84OFliMjP7qBiSjYc0Zxg_mYm51nQn6W3DlZVznqvL9BVS8WsREgCJQAuMrFT731egJgxG1u0K0GoEapMFB-977-sLwMInIsiv-pXdfvDNnctxYrO9svhOaQeba8WZt9rH2HWa9TsyLm81CNgG9I1_MrxtnROXwVQloqfawn4L_ymxKtNhTgfmwbmKgiSYALJ0irw4P01Obd-0HYGnIjvSJ11GalceHmhze_zMyEKJ5WYyPDGswDnOXecbTTu5mIZeK6LNYGxlEYMSt9a5OG7szo_cWCnkx_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🎬
ساخت موشن‌گرافیک حرفه‌ای با یه پرامپت!
‏این ابزار هوش مصنوعی کل فرآیند ساخت تیزر تبلیغاتی، از استوری‌بورد تا تدوین صدا و انیمیشن رو خودش انجام میده و خروجی رو با بیت موزیک سینک می‌کنه. خوراک بچه‌هاییه‌ که سریع میخوان خروجی باکیفیت بگیرن.
🔥
‏
⚡️
دسترسی به منابع غنی:
۱۵۷ مدل سناریو، ۲۱۴ استایل بصری و کلی الگوریتم انیمیشن آماده
‏
⚡️
شروع سریع:
کلی تمپلیت آماده‌به‌کار داره که کار رو برای پروژه‌های فوری جلو میندازه
‏
⚡️
عملکرد هوشمند:
کافیه ایده‌تون رو متنی بدید تا در لحظه ویدیو تحویل بده
😎
برای دانلود ابزار تولید ویدیو
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzatEhjp6IAeT7jQlxGw_AvscsQAqQcU61Ty1vwfhRv-Ao7LX0kenpcGYlC3Rhv9IDYNbMdK33fcjiAWNzvV8rqIkh-_42xzR7Hy-QpWFaCxFaOb-0_Co9zb4ErB7FrhY1RAfpItYAC_oZDxw_kLMTREOzWXi4nNMyA9mUEO0JIblNgSFHPvVfsOBIeUsSyGs7fiPHkfpYD-AizaCXCOqEAIawv8X5HwghFt09V-3Zqb6RdWHhDIEW8qAmNqVa7VSCtt7nRlaj93UpHMflqXqFOavDTJiRIgVzVkyXDzgjls83VNd3Vy0rBDXulE6NMwGcySmlWTyZndEBV2CFE3uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
مرجع خفن اسکیل‌های ‌Claude Code⁩ و ‌Codex⁩!
‏سایت ‌SkillsMP⁩ یه کاتالوگ تر و تمیز با بیش از ۳۳ هزار اسکیل آماده‌ست که تو کار با هوش مصنوعی کلی جلوتون میندازه.
🤖
‏•
دسته‌بندی جامع:
از برنامه‌نویسی و ماشین‌لرنینگ تا امنیت و کار با ‌API⁩
🔍
‏•
دسترسی سریع:
لینک مستقیم به گیت‌هاب برای هر اسکیل
📂
‏•
کیفیت‌سنجی:
دارای ایندیکاتورهای کیفیت برای انتخاب بهترین ابزارها
⚡️
‏خوراک بچه‌های وایبکودره که بخوان پرقدرت‌تر پروژه‌ها رو ببرن جلو.
🚀
🔗
skillsmp.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🛡
دیگه ایمیل و پسورد اصلیت رو به هیچ سایتی نده!
حتماً براتون پیش اومده که برای ثبت‌نام در یک سایت مجبور شدید ایمیلتون رو بدید، اما بعد از یه مدت صندوق ایمیلتون پر از پیام‌های تبلیغاتی مزاحم شده یا اون سایت هک شده و رمزهاتون لو رفته!
ابزار جالب
AliasVault
دقیقاً برای حل همین مشکل ساخته شده:
💎
این ابزار براتون چیکار می‌کنه؟
⚡️
ساخت بی‌نهایت ایمیل دائمی:
برخلاف ایمیل‌های موقت که بعد از ۱۰ دقیقه می‌پرن، این ایمیل‌ها
کاملاً دائمی و همیشگی
هستن و برای هر اکانت می‌تونید هر تعداد ایمیل دلخواه که خواستید بسازید!
⚡️
دریافت کد ثبت‌نام داخل خود برنامه:
نیازی نیست برید یه ایمیل دیگه باز کنید؛ ایمیل‌های تایید و کدهای ورود مستقیماً داخل همین برنامه براتون میاد!
⚡️
مچ‌گیری از سایت‌های متخلف:
اگر یه سایت ایمیل شما رو به تبلیغاتچی‌ها بفروشه، دقیقاً می‌فهمید کار کی بوده چون برای هر جا یک ایمیل اختصاصی ساختید.
⚡️
نصب روی گوشی و کامپیوتر:
هم اپلیکیشن برای موبایل داره و هم افزونه برای مرورگر، و خودش پسوردها رو سر جای درست پر می‌کنه.
💬
چرا این ابزار فوق‌العاده‌ست؟
•
ایمیل‌ها هرگز منقضی نمی‌شن:
هر زمان در آینده بخواید وارد سایت بشید یا رمزتون رو بازیابی کنید، پیام‌ها باز هم به همین ایمیل دائمی میاد.
•
سقف تعداد ندارید:
برای ۱۰۰ تا سایت هم می‌تونید ۱۰۰ تا ایمیل مستعار و رمز مجزا بسازید.
•
کاملاً رایگان و امن:
بدون هیچ هزینه‌ای، امنیت و آرامش صندوق ایمیلتون رو تضمین می‌کنه.
🌐
ورود به وب‌سایت AliasVault
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njsQ52xMS5HM0gJCl4_jUTz4g6YlnOjoMvqAd19wMfOfbV8zZXVKd_mgOwTiTABdovJwHG3B6cn_qihDiPizhALj5fhO7K4ORYAFXu9cr_JrTKXT2hm2EcTxmbFGQywSEhQBZaUtx7HD2jZWtztondTToKYSLb0uNXl1TFveFPV03RuuQvBFpQZp8o_k6pnEpiVNlorLxayoUv4o_ECi1FOEmcc-u-9pMeKK7G8-p96rxtAuDiDuMtJ2xywaesaDoV4lmdK5MkucYfi9qvpIV5JKOBl2RnjthrjpbAhCrxCtkR8uDjXcCs45wIhHFbBdpf-ISFpz3Q3itrIWHa0BtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سایت، ده‌ها مدل و ابزار با اعتبار رایگان روزانه
🎁
💬
Multi AI Chat
GPT، Claude، Gemini، DeepSeek، Grok، Qwen ، Llama
همه در یک چت، با امکان مقایسه جواب‌ها
🎨
تولید و ادیت عکس
تولید تصویر از متن (Flux، Stable Diffusion، Ideogram…)
حذف/تغییر پس‌زمینه، حذف اشیاء و متن از عکس
Face Swap، Upscaler، تبدیل اسکچ به تصویر
ویرایش عکس با دستور متنی + تولید تصویر سه‌بعدی
🎬
ویدیو
تولید ویدیو از متن و از عکس
Face Swap روی ویدیو
خلاصه‌سازی، زیرنویس و ترجمه ویدیوهای یوتیوب
🎵
صوت و موسیقی
ساخت آهنگ (Suno، MusicGen…)، Text-to-Speech با صداهای طبیعی
شبیه‌سازی صدا (Voice Clone)، تبدیل ویس به متن، حذف نویز
✍️
نوشتن و تولید محتوا
تولید محتوا، بازنویسی، خلاصه‌سازی، ترجمه، گرامر
تحقیق کلمه کلیدی و تشخیص محتوای AI
🌐
لینک سایت :
app.1min.ai
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان
claude-fable-5 | claude-sonnet-5 |
deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید
@kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url:
https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🆓
هوش مصنوعی رایگان  — بدون ثبت‌نام
Kimi K2.6 | GPT 5 mini | DeepSeek V3.2
📌
امکانات:
⚡️
چت هوش مصنوعی نامحدود
⚡️
تولید متن و محتوا
⚡️
بدون ایمیل، بدون رمز عبور، بدون کارت بانکی
📌
نحوه استفاده:
🔗
وارد
این سایت
بشید مدل موردنظر را انتخاب کنید و شروع کنید.
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QipGrfPOEZnXSn_UsOu-ZozO9sBJxuJBe-wHN9vaOGzaGCW0Rpi8-X79ahPeivxxzJrlziHG2eVJdxf0j0MaOOE6_BbMhg-OzDcvMSXLkhKkl5dKyL8hoaTQPzT6tcIj_sx-h_v1DJK_B-GcT0s6i2Zlbz6-PAPPxSmyDUN3P6-ZLqUnw2RrOC3fp4Fle0TRS15JrT_eILpaTtPNNaRd4DLzlBVOmAftAPAh4pUFoIeczVBqg2SWLPJTT2AprGGQOYvUrrjWGNx3Y91CPdn6QZqBOdLtuZ0c6bam5kFr3RwQ4lf1OpK4IdDZtuOOWsXeJIf_yeDtPVWw0LlgKyOPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
۵۰۰ مگابایت پروکسی رزیدنتیال رایگان (
proxyma1.io
)
یک سرویس پروکسی رزیدنتیال که با ثبت‌نام از طریق تلگرام ۵۰۰ مگابایت ترافیک رایگان می‌دهد و API هم دارد.
📌
نحوه دریافت:
1️⃣
وارد سایت
proxyma1.io
شوید و ثبت‌نام کنید
2️⃣
پس از ثبت‌نام، یک پیام برای استارت ربات تلگرام نمایش داده می‌شود که داخل آن یک کد هدیه قرار دارد
3️⃣
ربات را استارت بزنید و کد را برای ربات ارسال کنید
4️⃣
۵۰۰ مگابایت به حسابتان اضافه می‌شود
🚀
📌
ویژگی‌ها:
☑️
پروکسی رزیدنتیال (Residential)
☑️
۵۰۰ مگابایت ترافیک رایگان
☑️
پشتیبانی از API
☑️
ثبت‌نام آسان با تلگرام
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqb8iiPqZlCKg0Sm2qzp0s40mP3axXouLs_3aWXVDl2cXG34ZCRxilG8Jbwr5PiLYXixpgEu-_OyNzRHc0JliLa1jbV6sbtp5U5SRCG6vMT_0flfQ34s6n8EQrl9fWEcnYxbFDJVvVmHJobR87S4yeVnxwclUWwSmsAby6tUXxb63zhQfXV8dEpYmtwrJEr6LKzT5fyV_PxzvNOT9OsnAtJp8f5z6Ppu_BXi9LHPt6v4EZGe1dprSs-JBMMgoqIbhOQ8ou6EGjdCZ5ePt_IT2kH_bvix_8rGuBaaq10GVw_gj4EAv0VkYSuyBAHxKiqYoYmNsXO2XR9x9cQnRmhAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
۵۰۰۰ اعتبار رایگان برای مدل‌های برتر هوش مصنوعی
پلتفرم جدید در شروع کار ۵۰۰۰ اعتبار به شما هدیه می‌دهد تا با قدرتمندترین شبکه‌های عصبی کار کنید: تولید متن، عکس و ویدیو در یک جا.
📌
امکانات در دسترس:
☑️
چت چندمدلی
☑️
تولید تصویر
☑️
تولید ویدیو
☑️
موجودی اولیه: ۵۰۰۰ اعتبار رایگان
🪙
📌
روش دریافت:
1️⃣
ورود به
getunikey.ai
2️⃣
ثبت‌نام یک حساب کاربری جدید
3️⃣
ایجاد کلید API در تنظیمات پنل
4️⃣
استفاده در رابط چت یا ابزار های واسط
base url:
https://getunikey.ai/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔍
Hidden File Hunter — شکارچی فایل‌های مخفی ویندوز
دنبال فایل‌های مخفی و سیستمی توی ویندوز می‌گردی ولی پیدا کردنشون واقعاً دردسره؟ این ابزار دقیقاً برای همین ساخته شده
👇
؛ Hidden File Hunter یک برنامهٔ دسکتاپ ویندوزیه که تمام فایل‌های مخفی و سیستمی درایوهات رو پیدا می‌کنه و توی یه جدول مرتب و قابل مرور نشونت میده.
✨
امکانات:
✔️
پیدا کردن تمام فایل‌های مخفی و سیستمی در همهٔ درایوها
✔️
نمایش نتایج در یک جدول مرتب و خوانا
✔️
خروجی گرفتن از فهرست کامل مسیرها در قالب فایل TXT
✔️
کپی کردن خود فایل‌ها با حفظ ساختار پوشه‌ها در مقصد دلخواهت
✔️
فقط می‌خونه و کپی می‌کنه — هیچ فایلی رو تغییر نمیده، حذف نمی‌کنه و بهش دست نمی‌زنه
✔️
ساخته‌شده با Python و PySide6
✔️
تم تیره و روشن
✔️
رابط دوزبانهٔ فارسی و انگلیسی
یه ابزار ساده، سریع و امن برای وقتی که می‌خوای بدونی توی سیستمت چه چیزهایی از چشم‌ها پنهان مونده.
🔗
لینک گیت‌هاب:
github
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚀
اپلیکیشن Bifrost (بایفراست)؛ پل ارتباطی فوق‌سبک تلگرام بر بستر ورکر کلادفلر منتشر شد.
بایفراست یک بریج لوکال (Local SOCKS5) مدرن و بهینه برای اندروید است که ترافیک تلگرام رسمی را از طریق پروتکل TWP به ورکر رایگان کلادفلر متصل می‌کند؛ با پینگ پایین، بدون قطعی و با سرعت دانلود فوق‌العاده بالا.
🔒
بدون نیاز به VPN، بدون روت و با مصرف باتری نزدیک به صفر:
این پروژه کاملاً متن‌باز (Open-Source) است و برخلاف فیلترشکن‌ها از VpnService استفاده نمی‌کند (هیچ علامت کلیدی بالای صفحه نمایش داده نمی‌شود و اینترنت سایر برنامه‌ها کاملاً دست‌نخورده و بدون تغییر باقی می‌ماند). مصرف پردازنده در زمان عدم استفاده دقیقاً ۰.۰٪ است و امنیت و رمزنگاری پیش‌فرض تلگرام (MTProto) نیز کاملاً حفظ می‌شود.
📥
دانلود و نصب برنامه (از گیت‌هاب):
https://github.com/Qorvhex/Bifrost/releases
⚡️
کانفیگ تستی برای شروع (بعد از نصب، کپی کنید و داخل برنامه Paste کنید):
twp://telp.qorvhe-x.workers.dev?clean_ip=1music.cc#Bifrost-Test
🛠
سورس‌کد اسکریپت ورکر (TWP):
https://github.com/Qorvhex/TWP
📁
لینک پروژه و سورس‌کد در گیت‌هاب:
https://github.com/Qorvhex/Bifrost
لطفاً تستش کنید و سرعت و عملکردش رو بهم بگید!
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🖥
مرورگر ضد ردیابی Private Browser Pro؛ هویت جعلی و دور زدن بن شدن اکانت‌ها!
​بچه‌ها اگه نیاز دارید روی یک سایت چند اکانت مجزا بسازید بدون اینکه سیستم‌های امنیتی بفهمن همه‌شون مال یک نفره، یا می‌خواید ردپای دیجیتالی‌تون رو کامل مخفی کنید، این مرورگر اوپن‌سورس ویندوزی دقیقاً همون چیزیه که دنبالشید. این ابزار بر پایه نسخه فوق‌امن Ungoogled Chromium و Electron ساخته شده و از زبان فارسی هم پشتیبانی می‌کنه.
​
🎭
جعل مشخصات سیستم (فینگرپرینت):
شبیه‌سازی کارت‌های گرافیک قدرتمند (مثل RTX 4090، سری RX 7900 و تراشه‌های اپل)، اضافه کردن نویز به Canvas و AudioContext و هماهنگ‌سازی هدرها برای عبور آسان از سد کپچاهای Cloudflare Turnstile، hCaptcha و reCAPTCHA
​
📁
مدیریت و تفکیک کامل پروفایل‌ها:
امکان ساخت محیط‌های دائمی (Persistent) برای ذخیره دیتای هر اکانت در پوشه جداگانه، یا حالت موقت و یک‌بارمصرف (Ephemeral) که با بستن پنجره کل ردپا پاک میشه + دکمه پاک‌سازی آنی
​
✅
پروکسی پیشرفته و ضد نشت اطلاعات:
پشتیبانی از پروکسی‌های SOCKS5 و HTTP (با یوزرنیم و پسورد)، حل آدرس‌ها از داخل پروکسی جهت جلوگیری از DNS Leak و غیرفعال‌سازی WebRTC برای مخفی ماندن کامل IP واقعی
​
✨
محیط کاربری تمیز و دو زبانه:
کرومیوم دست‌نخورده بدون واترمارک‌های تستی، تم دارک با کلیدهای میانبر سریع و پشتیبانی کامل از منوی فارسی و انگلیسی
​
💡
بهترین سناریوی استفاده:
ایده‌آل برای مدیریت چند اکانت در شبکه‌های اجتماعی و پلتفرم‌های حساس، تست وب، ریسرچ‌های OSINT و حفظ حریم خصوصی بدون نیاز به خرید اشتراک‌های گران‌قیمت مرورگرهای ضد ردیابی.
​
🔗
گیت‌هاب
​
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📥
تبدیل فایل‌های تلگرام به لینک مستقیم نیم‌بها با ربات Leecher!
بچه‌ها اگه کندی دانلود از تلگرام یا قطعی فیلترشکن موقع دریافت فایل‌های حجیم کلافتون کرده، یا می‌خواید تورنت و ویدیوهای یوتیوب رو مستقیم به فایل تلگرامی تبدیل کنید، این ربات لیچر ایرانی حسابی به کارتون میاد.
🇮🇷
لینک مستقیم با ترافیک نیم‌بها:
تبدیل آنی فایل‌های تلگرام به لینک دانلود پرسرعت تحت وب (سازگار با دانلود منیجرها) با محاسبه مصرف اینترنت به‌صورت نیم‌بها
🌐
دانلودر همه‌کاره (لینک به فایل):
پشتیبانی از دانلود مستقیم لینک‌های یوتیوب، اینستاگرام، وب‌سایت‌ها و حتی فایل‌های تورنت و تحویل فایل داخل چت
☁️
اتصال ابری به گوگل درایو:
امکان لینک کردن اکانت شخصی Google Drive برای ذخیره و آپلود مستقیم فایل‌ها در فضای ابری بدون مصرف حجم گوشی
🎁
شارژ رایگان روزانه:
۱ گیگابایت حجم رایگان در هر ۲۴ ساعت بدون نیاز به پرداخت هزینه یا خرید اشتراک
💡
نکته کاربردی:
لینک‌های ایجادشده بین ۶ تا ۸ ساعت معتبر هستند؛ کافیه فایل رو به ربات بفرستید، لینک مستقیم سرور ایران رو داخل IDM کپی کنید و با حداکثر پهنای باند خط‌تون دانلود کنید.
🔗
استارت ربات
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AReojpR8Y66GCM_42iMthsRBVicKE4MMSY-j1-JMx6jkoKXTVao7XEKSUecizwy8Z33-q7web7K_OXh9ned-TrGaXBqWatcIZOu32QjmCxp_A5llNYU2pg6TQ6r_4s3lUADQENAUfhvOSzky5Yywxcl0_c2EB62yy1WMmx0rn8RqCGGHKIIeDIGkK-gKTIl1mOong62ityZrIYGfLZuIUwKfk69zerdIKESFPKE2dRuG1-wYfhCfWVSltWO6H99zFdxqFHk3eEQHAUdENSdBpsFj6GmXXz6eEt03V9jyVECo9Pcn4fTL8szMBFLumYwv3WZLFg3S9KFcxbDqHXdJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید (1.8.0) برنامه MSN-GUARD منتشر شد :
💢
BOOM
💢
تغییرات :
1- اضافه شدن متد اختصاصی SHARD برای اولین بار
-_-_-_-_-_-_-_-
2- دسترس‌پذیری کامل و پشتیبانی 100% از صفحه‌خوان TalkBack برای عزیزان نابینا و کم‌بینا برای اولین بار
-_-_-_-_-_-_-_-
3- آپدیت هسته
-_-_-_-_-_-_-_-
4- اضافه کردن قابلیت Backup و Restore و Reset Factory از تنظیمات برنامه
-_-_-_-_-_-_-_-
5- برطرف شدن مشکل دکمه Reconnect در نوتیفیکیشن
-_-_-_-_-_-_-_-
6- اضافه شدن Theme کاملا روشن برای استفاده زیر آفتاب
-_-_-_-_-_-_-_-
7- برطرف شدن باگ اتصال خودکار پس از قطعی اینترنت و چند باگ دیگر
-_-_-_-_-_-_-_-
6 روش دسترسی به اینترنت آزاد:
1: متد Masque
2- متد Wireguard
3- متد Warp On Warp
4- متد Psiphon (اختصاصی و اولین)
💯
5- متد Tor (اختصاصی و اولین)
💯
6- متد SHARD (اختصاصی و اولین)
💯
💻
ریپازیتوری گیت‌هاب (متن‌باز):
https://github.com/mbm110/MSN-GUARD
📌
لینک مستقیم دانلود :
برای گوشی های 64 بیت
برای گوشی های  32 بیت
برای تمامی گوشی ها
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✉️
؛ Turbo Mail ایمیل موقت، سریع و بدون دردسر
اگه برای ثبت‌نام یا دریافت کد تأیید به یه ایمیل موقت نیاز دارید، Turbo Mail یه گزینه ساده و سریع برای شماست.
⚡️
ساخت فوری ایمیل موقت
👌
بدون نیاز به لاگین و ثبت‌نام
⏳
اعتبار ۲۴ ساعته
🔒
مناسب برای دریافت ایمیل و کدهای تأیید
🚀
ساده، سریع و بدون مراحل اضافی
کافیه وارد سایت بشید، ایمیل موقتتون رو بسازید و استفاده کنید.
🔗
https://mail.turbocenter.shop
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎧
دستیار هوشمند و همه‌کاره موزیک‌بازها؛ دانلود با کیفیت FLAC با ربات MelodyAddict!
بچه‌ها اگه عشق موسیقی هستید و از دانلود تک‌به‌تک آهنگ‌ها، افت کیفیت یا پیدا نکردن موزیک پس‌زمینه کلیپ‌ها کلافه شدید، این ربات فوق‌العاده با پشتیبانی کامل از زبان فارسی دقیقاً خوراکتونه. همه‌چیز از شزم اختصاصی گرفته تا رصد خودکار پلی‌لیست‌ها رو براتون یکجا جمع کرده.
🔄
سینک خودکار پلی‌لیست‌ها:
زیر نظر گرفتن لایک‌ها و پلی‌لیست‌های Spotify، SoundCloud، YouTube Music و Apple Music و ارسال خودکار ترک‌های جدید با امکان زمان‌بندی ارسال (۳ ساعته، روزانه یا هفتگی با دستور /digest)
🔍
شناسایی جادویی آهنگ:
پیدا کردن نام و فایل موزیک فقط با فرستادن یک وویس کوتاه، زمزمه، فایل ویدیویی یا لینک ریلز اینستاگرام، تیک‌تاک، یوتیوب و توییتر
💎
کیفیت استودیویی FLAC و Lossless:
قابلیت تنظیم کیفیت پیش‌فرض خروجی برای گوش دادن به بالاترین بیت‌ریت ممکن، با سرعت عالی و کاملاً بدون تبلیغات
📂
مدیریت پلی‌لیست‌های ابری:
امکان دسته‌بندی، ساخت و اشتراک‌گذاری مستقیم پلی‌لیست‌های شخصی داخل تلگرام
💡
نحوه استفاده:
ربات رو استارت کنید، زبون رو روی فارسی بذارید و برای شروع کافیه وویس یک آهنگ یا لینک پلی‌لیست موردعلاقتون از اسپاتیفای یا ساندکلاد رو براش بفرستید تا بقیه کارها رو خودش اتوماتیک انجام بده.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jSCBZFcPbnhPFqaprZSpGbQwdHPypFJvbK0IdPOQvACSuQdTEdOdBRlCohTd9iqdZU7bNaGI1Vh3UQqC1yuSEccbst89q1R5YSW9KT4qwwrD1eHMiycKLAB8zCjPDTWF1QlyM6-WKo-gHa0ixXbPD0fR9o80Ad6mgdSMCFKeaPQxZpjhI3Kx5KT6HdR7w13bSSxffOmi3IDwmiRHwFxhdIgbFJPsWSB1o_S7na2RFJcXnED013TPXRqxj468PVHbkhM-3bwghtjPP3azcnNjVmzof61Y9rag9yEYZgUQ0oYP6ZzbcDTAFXsas8xYuASwtDiHmY4sHQQZAI5LRJCOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید ArasClient منتشر شد!
نسخه جدید با اضافه شدن بخش Free منتشر شد و از این به بعد این بخش به‌صورت مرتب آپدیت میشه.
📱
؛ ArasClient یک کلاینت سبک و کاربردی برای مدیریت و استفاده از کانفیگ‌هاست که تمرکزش روی سرعت، سادگی و اتصال راحت‌تره.
🆕
اضافه شدن بخش Free
⚡️
آپدیت منظم کانفیگ‌ها
📊
تست و مرتب‌سازی هوشمند سرورها
🔄
انتخاب سریع‌تر سرورهای مناسب
📦
پشتیبانی از نسخه‌های مختلف اندروید
🔗
دانلود نسخه جدید:
https://github.com/ArasTey/ArasClient/releases/download/v1.6.8/ArasClient_1.6.8_arm64-v8a.apk
🔗
سورس پروژه:
https://github.com/ArasTey/ArasClient
💬
نظر، انتقاد یا پیشنهادتون رو کامنت کنید.
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xpn_nL4F2_JnZ7sO9wegojn8M0WuIRjEO0FSOkb5OJ-RKtBFAmpKZKoAVf5tQdNLmhiB4_wkbn6bAeFFCcQhCs6sR_kjQHbzaXa5XUiE0jxNM9lwtCsQaRB5v5l85wjIin9VnxGm966SH1uxCRswgx8GzFoebh615JiKJVQqtYVGHpgmKfBIEG3sXVX7_WYQH0T7u4gjjRSpySZy359GikfrIqteT-r4TZ4XAQPfMcW0wV2AXzS8o1fpfBKn10n-7fuYth1ynAKNUEl7AgYBPAL0H7Foh4JeZ-aEL6T8l-J_wz-WSJULqdhlyav7JXu0ITH9LIMbGNSDGO4Ycx3BHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
اگر می‌خوای شبکه‌های کامپیوتری رو از پایه تا سطح حرفه‌ای یاد بگیری، نت‌داد دقیقاً برای تو ساخته شده.
از مفاهیم بنیادی مثل آدرس‌دهی IP، سوییچینگ، مسیریابی و امنیت گرفته تا شبکه‌های مدرن، همه چیز با پروژه‌های عملی و مثال‌های کاربردی آموزش داده می‌شه.
✔️
۱۰۰٪ پروژه‌محور
✔️
۵۳ درس تخصصی
✔️
۱۴ بخش آموزشی
شروع یادگیری از اینجا:
🔗
https://netdad.vercel.app
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVid4Z_z_9b88pCZXchKsL_1Zg-PGN3zQj_q5oxlYnCRdnoCz7sMx0AyybBy7wwRapwqMlmK_F9LWbL8dfXfBWDTINs83J_ndmIlNQ_BE1OZS6L7ae17z4sfbcw6II_2U_EopHPxxiIvQwKbsEzFTxdlCejQAq-K4Jq_mDQ_mtL_GpAV8o23BCcJNQjoSVa6isUnphhqurLQTaDqFfn9O1L0w4g6ZxU8of-YplwShTOEZ_lDccafo0bZNszkDvSrU8B2kWapmp21UgPRUM3tCD6rfCM1tSvjlfwW2J4e5iD9qyYas_cH8N8qvU0HP49LVlYcnowCZbMJ7z0wTukwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lxq92TKefXJ3dkrQo0TWTIZ4tyevvRbt2Oh_ESFw4CqGdLFAgxVaw7l9neIPb3slWLdNzGsmjPrQO4tMXw8WcoVi27XRzV1cSxL3iQ5bKX1GckZbDrWu4OlQB174BLZ1owSuv2F7rVaycfYGiOzb6vYHkIn92YdFAWTo7nKc0MY2s6IpK3DLtD1V6eZI6DGoYt3caoPkiBG37_bcuwnTPDCZLOrL771tb3ltE6ECIPHWUGVPHslnrN7OyY9s6uRlOwLv6kKovX0RQM2VkN87SOBwsWeZwQLFUCszYZJJkcK_8oPKdMBUeu-OK4B0v64FzHRDhxv6GULJKPIJbuzkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥁
کیبورد لپ‌تاپت رو به یه درامز حرفه‌ای تبدیل کن
پروژه خفن KeyBeat یه استودیوی درامز تحت وب هست که بدون نیاز به هیچ نصبی، مرورگرت رو به یه ساز واقعی تبدیل می‌کنه
🔥
یه پروژه اوپن‌سورس عالی برای برنامه‌نویس‌ها، آهنگسازها و عشقِ موزیکا
🔗
لینک سورس کد و اجرای مستقیم:
https://github.com/faithsaly5-stack/Keybeat
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H63BBJOjm1GPu-KAhh6C3ZzQ4wmJxSqRJ09S1O2YRuZ_l61xc7Wdxh-33rtYP_pxDUmTIEMjSpOQlCxKmfegTuF9dSIwhF8_gR-mpOJmt3MlN5Hjo8AmvnZGePVKKt-evYngD52n7b5f--iMyO2LqDNyzZE_ow7jWLQc3JI7Qb4mBC1i5pUQozKCRb8m2a74jSXuEFUf4JDLGvYzckabZPaKpF7e5wkhjHGkS1jVi-jSZS1oXBViaxe31EMIYYN2L85V6qto7EQjV1pzk1SnMjyqmY3s83ZfiMEuc6AFNKuMKDH0HoQ0LUbn1qVp1GPGkBGOG4qB82sVbtMriu8l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دریافت آیپی رزیندنتال رایگان
💎
با گوگلتون سایت زیر بشید و روی claim offer کلیک کنید.
بعدش برید بخش proxy generator و پرش کنید و بزنین براتون 300 مگ آیپی رزیدنتال میده
🆓
http://rainproxy.io
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKFCJcBcFjfgfi2yb57p7FGSSXjB-a9eWkzO30sYguUDSAsi3O2KecGWseSep-xawdU-5DnyRuN08QFV5l4RuZJDupIKu3x3YaJ2z1BB8kD3f92eSffNNocT3lhP3BpfUX1_NWxOMVz9CXWXz65cAqUSX7nmf8-Uov-Rem_OI2B-V5rr1eto6DydVhNM31qpV9Ut22qcrGhRI18_RNQm-dReUtqxJKzAET88GTXMtU-9FplOfQdsNXjnjF6vHrQbIN3oP0cCCEwMoeqiPP-L6UvD1-I_9xK3Gwypf9QT33TpRSuKztmq8_OXnlzdCbhal0aSQ2e2KilrGLypoYvrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
15 دلار اعتبار رایگان برای دسترسی به بهترین مدل‌های هوش مصنوعی
استفاده از مرورگر به شما 15 دلار اعتبار می‌دهد تا مدل‌هایی مانند موارد زیر را امتحان کنید:
• GPT-6 Astra
• DeepSeek V4.1 Flash
• GPT-5.6 Luna
• Claude Opus 5
• Grok 4.5
برای دریافت:
🔗
browser-use.com
با استفاده از حساب گوگل خود ثبت نام کنید و شروع به استفاده کنید.
برای دریافت اعتبار بیشتر، از چندین حساب استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🧰
جعبه‌ابزار همه‌کاره و فوق‌سریع تلگرام؛ معرفی آپدیت بزرگ بات Amir Tools!
بچه‌ها اگه کلافه شدید از اینکه برای هر کار کوچیک (هوش مصنوعی، استعلام قیمت ارز، دانلود یوتیوب و تبدیل فایل) یک ربات جداگانه استارت کنید، این بات همه‌کاره دقیقاً خوراکتونه. در آپدیت جدیدش کلی ابزار مدرن با رابط شیشه‌ای اضافه شده تا از ده‌ها بات متفرقه بی‌نیاز بشید.
🧠
هوش مصنوعی با حافظه اختصاصی:
مکالمه پیوسته بدون فراموشی کانتکست چت، سوئیچ خودکار روی مدل‌های پشتیبان و امکان ریست سشن
📥
فایل به لینک مستقیم و دانلودر یوتیوب:
تبدیل آنی انواع فایل، ویدیو، آهنگ و ویس به لینک مستقیم پرسرعت + دانلود مدیا از یوتیوب با بالاترین کیفیت
📈
نرخ لحظه‌ای و چارت زنده بازار:
استعلام آنی قیمت دلار، تتر و ارزهای دیجیتال (BTC, ETH, TON و...) همراه با نمودار اختصاصی و باکس High & Low
🤫
پیام ناشناس امن و دوطرفه:
ساخت لینک اختصاصی با آیدی تصادفی برای دریافت متن، ویس و عکس ناشناس با قابلیت پاسخ‌گویی مستقیم
🎁
سیستم قرعه‌کشی خودکار کانال:
ساخت مسابقات و چالش‌های گروهی با دکمه شیشه‌ای و قرعه‌کشی کاملاً خودکار و عادلانه بین اعضا
🛠
میکروابزارهای روزمره:
ساخت بارکد تصویری (QR Code)، پسوردساز غیرقابل‌نفوذ، مبدل ارز به تومان، هواشناسی و مینی‌گیم‌های کوئیز
💡
نحوه استفاده:
وارد ربات بشید، دکمه شیشه‌ای منو رو لمس کنید و بدون نیاز به رجیستر یا مراحل طولانی، به تمامی ابزارها به‌صورت یکپارچه و رایگان دسترسی پیدا کنید.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTCzP97LmoSTGR3qrw0rqJpiXwsy73VxJKFiDxQMaLJ5AmEEGJL5gSi-YFmfxzO2jtUP7fET7_2CzSqD2yc7OV8x1B1VlOnu2aw9cDwGq-kAcG0Ywafyks9G0fyxAezbgGbMS8zMXCr34wMXR5cO59PAqoHlYObbnIjWeFyEKhpBdm2V5Kfk8zPdxd4212aGetJY5AKmw9UzH1o4zgQKpFlG2dr_infzZBOURHDoae0H_70rOxsv4NNSsR9URxfsr_wR8Jp9JT1meiBH38IBua07CT_2AtukfRdCbFjJFYf7phQIMsfKzGj2PxUwD9M4-B_GhrgQAez7T_Q03BGhHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل:
① به
https://arena.ai/
مراجعه کنید.
② حالت
Direct Mode
را انتخاب کنید.
③ در لیست مدل‌ها،
GPT-Image-2.5 Sunburst
را پیدا کنید.
④ به مدت
72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود
.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXuA3MJWk2wHkF5-NDEbqY6_hXChWdta5ORdY006E_I7iK6yVCEuqzli51yoMPneALbUOPy3_53nIQfZD2bU3eWMiK_u0YNUGbBBzyzZJANwTALsOLG-tlU1H0SBZepqH2ZLmZ4QAhw_-Ahyf-YOweR56Q9J03UQCEwO_ZeRt18r38iHRVE_p8l27aAD5SueerYZmE5CBVn5egRzZFNLzqa0XMiZsdSPQccI2NeLvUI8FtgzV8NbmBTPROHfyUNJRzWLypGlxpvQcgltT3qTwPHhlr2qg8JsnXF7mrN1QMrTn7a1T0zidpwepPp6oCn-wcCu_ITMzhoyOC2Ynpt7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4.1 Flash به صورت رایگان
💥
🆓
این نسخه ۲ روز پیش منتشر شده است. دارای ۱ میلیون توکن متن، قابلیت‌های بصری پیشرفته و کیفیت مناسب برای استفاده در سیستم‌های هوشمند است.
🚀
🔺
رایگان به صورت روزانه
🔺
پنجره متن با ظرفیت ۱ میلیون توکن
🔺
سهم استفاده روزانه هر روز ریست می‌شود.
هنوز مشخص نیست که این سرویس چه مدت به صورت رایگان باقی خواهد ماند.
‼️
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvcNw4piof5UBksuAfg3S5bp5YwUG1xSEDtnLnoqWDUEtSk3ilvpU5J966WU4mwQFYRmjiHar3zRHg4kB_H53xF97osIXzeF4nZ9NK_PkYNiAKxw7HV-DDvuFTC2wLpw9z-3zOOEQBbslwxlQLVPqIw2WPwCkNtYI73xRvTr81vXjgbmUJC4B9AU0MAPTGIQ9vomoFYlHGUiG4tP3DePK4UKPyKck-9muQ6G-UJpUczVEPGDLlYRrgwu-r-lxygT4hxq1GX6txBXYcXHmh2UNV0hJcXsvxHI3-y91e8tfqWCYjCLfl10D4dqN7dpmEm_lAibntx_QZ6SjHtF1CYJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
📌
Base URL: https://tokenharbor.ai/v1  با جیمیل…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5NdlYfSRKmvB7pfoPBno5mYNE7theaCkzc4ncAowe7l0XNMnv0LoSSekHSwcUCwq-VOCDOXDJVeQfc1UptqTCgH3RIG3i8kBd8nmM5j1Ado81Doc3yCN8D8u9gp4MW-rBaqN9RvDCn4wfQlkmdeefjROUC086300bUOzV26AmVk0tRTMp9gEANxahXv6xGAPSdLDxbqFvql9EB1qn2_JFPMq8jPiPd2vuERNLCVbs2hWatBSrU0Tg2U2Wi9f1GCEg3BfdQX6CjuPr0MVIFXnvBwA-4lcFGVykmudugkl68pos6LCSsH7Nh_oq4b5uhOqMuzsdPZJQvjmgTDzxcx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKUNQm4MzrhKZJHUwdsOzxPqOuHG3UehaLru1lPUHroo7-9G6lOc1HvwT8iUV7kccD0HME0pqg4PriS130WJCaUkN-K2FbqQWcUpTRwFifD21Gq62aosx3uOlqCwJ8lJ93tsULsEn_D8DLfSfGyrr-bzCfwLn_can3iTXmUdfgL37lCMSO6dIOPIxUPhDCusWu36KXijlnoXU9DmRavIez7LAar7lG5D1kHQlo6P4Hir-6IQpylYvUxcVnV6P7FNutxxIfszDjACT2JqRpH6DNYLf0ZwGkt_hg5m7ossmjD2icDw4TMqR5BGmCS8l6ae-IMAxqykpGHuAaErbmOvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">150 میلیون توکن رایگان برای مدل های زیر
💥
🆓
GLM 5.3 Flash | Qwen 3.8 Flash | Mimo 2.5 | GLM 5.3 | Hy 3 | Qwen3.8 27b
✅
وارد سایت زیر بشید با جیمیل ثبت نام کنید سپس از طریق منو 50 میلیون توکن امروز هم دریافت کنید
✅
‼️
نکته :
از مدل های با پسوند Free استفاده کنید و احتمالا این دسترسی شامل محدودیت تعداد ریکوئست در دقیقه باشه ، همچنین ممکن هست هر لحظه اشتراک رایگان بپره
📌
Base URL :
https://kiraai.vn/api/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🧠
پروژه OXYGPT — یه ربات تلگرامی که هوش مصنوعی رو حسابی جدی گرفته!
بچه‌ها این صرفاً یه ربات چت نیست، یه اکوسیستم کامل AI روی تلگرامه: چند مدل هوش مصنوعی، مربی‌های حرفه‌ای تریدینگ، sandbox واقعی لینوکس، اخبار فارکس زنده و داشبورد مدیریتی. خوراک کسایی که می‌خوان یه بات production-grade بسازن نه یه دمو دو ساعته
🔥
↔
مسیریابی چند-مدلی AI
: استخر کلید Gemini + سرویس‌های سازگار با OpenAI، round-robin می‌چرخن و روی خطای 429/503 خودشون فالبک می‌زنن
🪟
پنجره‌های مکالمه مجزا
: هر کاربر تا ۵ چت جدا با تاریخچه و state خودش می‌تونه باز نگه‌داره
🧙‍♂️
مربی‌های تریدینگ (Persona)
: چهار شخصیت آماده (ICT، Quarterly Theory، Matrix/369، Price Action) با یه دستور سریع صدا زده می‌شن
📓
ژورنال معاملات
: ثبت و پیگیری ترید‌ها با قالب‌های اختصاصی، مستقیم داخل تلگرام
📰
اخبار فارکس زنده
: رویدادهای پرتأثیر Forex Factory رو با تحلیل کوتاه AI نشون میده
🖥️
قابلیت Sandbox واقعی لینوکس (E2B)
: مدل می‌تونه کد اجرا کنه، پکیج نصب کنه، ریپو کلون کنه و فایل بفرسته/بگیره
🔑
قابلیت BYOK
: کلید API خودتو وصل کن، از محدودیت پیام و quota عمومی بی‌نیاز شو
👁
مانیتورینگ کانال با AI
: کانال‌های تلگرام رو زیر نظر می‌گیره و پست‌های مهم رو تحلیل و تحویل میده
💡
دیپلوی با یه دستور روی Docker/Railway انجام میشه، و هر ۵ ساعت یه بک‌آپ خودکار از کل دیتابیس‌ها زیپ و برات تو تلگرام ارسال میشه — دیگه نگران از دست رفتن دیتا نباش.
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU55I00uwqF3AMFABwtg6NrIMRr-yVx_RpUAKlYRx2TGBxcrMBLyfqtynb9z1O0wTURv-GnoA8ZBCgOFTW-k4d4MpF7KX8VS8Au0dAyDLXxQcfCdTlT3j5O9Pa_ajxD1H8XD3TTdNAfTTcfe6mT1aS01ogAJvNifZvXDFG4U3-q4uD929mAT732AIMX9o5u_q8yLpBzIpzf7wkmCtHWHF7Cs6MYomShPhwZxldGcBNsHoNWVLiU6bI6IdG7M_zPTllcHJP4j2T451MmWKUlfP8O0ab9KvswCySHqTx22vuV319PqNV7rsFc75GV75MiWoIy2ni-V6-IW5UBs8GJaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB1WQJVRWvJNRKFBBvBYle4fgO2r3DYexFRUxjK4v402WuOxxZ5JCAVQyW43phGuDcZ427sF_3prilS0yVtRcUXiJDEswnQoAeeZdLkik3qRc0kxX1oqlmdHRdafWI-3pa5bPEBIODJc3FH3P7E0qSvIYDHVvVIFiUq8DiVUxBJvri5HLdc_PZgSFR6uNX1riIotzOh0na3wYL5emZRWIKJAOqKZApwc-ZyrKhWu1AnqmTV4E3LKnFYs_96yLF3RhKZ7FxfYoqcobqy1fM50FT4amhGS-3PMg0m_SG73bxduw6Hy26F0Bdt8jPTPRkIpTu2zdgFdUVTOof3WFOQ9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه 1 میلیون توکن رایگان برای مدل‌های زیر
💥
🆓
Gemini 3.8 flash | Muse Spark 1.3 |GLM 5.3 Flash | Deepseek V4 Flash | Deepseek V4 Pro | GPT 5.6 Luna | Gemini 3.1 pro
✅
وارد سایت زیر بشید و ثبت نام کنید و یک کلید دریافت کنید
✅
‼️
نکته :
با هر آیپی ۱ بار میشه ثبت نام کرد اگه میخواید چند اکانت بسازید هربار آیپی هارو تعویض کنید
📌
Base URL :
https://apinex.bond/v1
🔗
لینک سایت
🔗
گرفتن کلید
🔗
دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bL6ScoQrglZOYaub_1QzfKuhpKN8YJGnZjmlwA90pHPMyMFebqhozeKxYV65c_nfJd9VdYQxeKOzmGsxQSmvaKyxDFGgDP_OY3GYGMtmola8p80A1aTwCzWfvjZjSV-hA3iWQJneAfUD-x6rrkQ7GFuactXT1kmfHFLC7AEdxlk20hj3LXUpBKdsF6qvV1RIEvYF0uMKIni4_1Zynuj4FNXyFwXvFDr0mSISKknZ0B--9hMZMrBaGzSdY8rkcBgD-_YCvBtV2AZMbJynySsLj-mcxndgv7l4OqEAfWnEevog9dWdAnrgDKFQWbg-dnfyK0_s4INpjvp_-u1aZ6U3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 میلیون توکن رایگان 1 ساله
💥
🆓
Fable 5 | Opus 5 | GPT 5.6 Sol | Grok 4.6 | GLM 5.3 | Qwen 3.8 max | Kimi K3 | Deepseek V4 Pro 0813
✅
برید داخل
این سایت
ثبت نام کنید
حالا برید داخل
این بخش
پلن سالانه رو انتخاب کنید و این کد تخفیف رو بزنید :
DEVWEEK
بعد اینکه تخفیف اعمال شد تایید کنید و تمام ، یک api بگیرید و استفاده کنید
✅
📌
Base URL :
https://codecraftapi.com/v1
اکثر مدل های جهان رو داره میتونید از Playground چک کنید ، چون سایت شلوغی هست طول میکشه تا ریکوئست ها جواب بدن
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obKmWgNECqrl-VarbbIIXGMvmAqeO6WPpSuATSt2OAT88pUZMkXerQYh-U5h4HChuQXUFtEbon8bg_iaoKsZnAZdhZ1UuZaKXayJqqMY5tun3YECxZbontT0jDLceH4Kthdxed1DMxguFI3rDZ41EMu_xA3F6SJuHsSt3-2a6IDIiDG1UQREofsRMjt3BFHaNIdKO10msfJLgvmq5FdqVQa0NlPLjayG8cePB-HhdMBraZL1b5J9VP_ICgz3m6c2_dD3FPX2Z-vI5x0OsMzrYDIRnu3Lffw3_ryZZuPUJIYG47eds2N7oMuI3RSmrMzjf5E1PQGrg2ol2b2OmnR91A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
با فیلتر شکن کشور مقصد یکم برین تو گوگل بچرخین،
بعد به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید.
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود و ایمیلش میاد
✅
بعدش میتونین به راحتی از antigravity و سرویس های دیگه گوگل استفاده کنین.
از توجهتان ممنونم
🙏
✈️
@ArchiveTell
|
#method</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">📌
Model :
gpt-6-astra
📌
Base URL :
https://api.eirouter.ai/openai/v1
sk-e76d452dff7eccef0a1b6bde4f8262c7f628f4f2991676cf3188d0cb68023b3f
sk-778bbaffd07397311260074542e405ab11833bf458e0250363ac1afd7db02297
sk-b028d3f23d96d0b0fc96a24985164437fcaf272276caf33548a664a0df424dc1
sk-1f153c31ccd2448b30c2f56287d5dc8fcc8ddafa579d12a797450321d86e9d29
sk-3334618935b09f67a70938d3379971e3ad350fec1154008d3abbaa07565c00b3
sk-242582ef9fc5e53351eb2fd67178b83033a450a61d048cf66be6aacf98a9e2bc
sk-db726cb7cc5b14160f9d8900455fcd34fd56cbb94f3afac65494a5161eee35b6
sk-7e85fc089be2d58f76c236c8ae1efc6062f68a459bdc9f87bcbe896c2d7307e2
sk-cca857a86f2c62b5d704f2234ed5632f8ef4dfbfcc0da509fe0e021516a0406d
sk-3c3eb497a104328775de0ddb333c7c8d596c20a89e25bbe7e204318f35e2b050
موجودی هر کلید هست 5 دلار ولی نکته اینجاست توی سایت قیمت هر یک میلیون توکن این مدل هست 1 دلار
😁
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=g9bHD5zQ_4WM1rWbdVXkNc-aluAgYAYc6f85jZrIcYlO7IDvML9InpZeBITG5OCeq7HXzpabQsqZF-22WgfHxhH8x24Z_g1k_O91rv8fFdZExsZYj6oEbAZdbA33p7xyzRjvXIEJMPdP4FRAB7gD8FzLfKB2oXIQo8x6KHYvSLqCvHfbisx2h8Iziz2iQAB1VEQHcq1d2VP-nDwYMuncEOwLYDZrLBoma8r4KvjyawqS_t5qm1nh5buA11tEYiPeqADCk8XKXX4RodW4BO3lIBKWvuIE8KJ49CA2Kx39GAdSdtdFxrKfRvyCuzNz-VFCTzmf34hpec8KuZCq7h9yH0NmbBY0LpSAb-1TtUTAu_ogmueJ05JWHHXXTpXR0v910XhhgMBzq-ZNj__AOp0BE3ZXUpiE42br2nWQbKsY9RmDW00WBRrUug1Uh0JhS-B8EsKG6bT6lWhN9hMBP5EbPbcSfq1e05eCDbFD0YLfyGop3qhCCepqaRT2rmEEjKrvL51kfRui4KmlSJ5W1-eZDWGMxeV4pLERP4pLryLR5DNa_McZtZbsb4L7tSqE9NugxHJU_jSeIt3Dz3ZoyZ4jHYFXEV1cvZ4liTfdV7naqSjjRb_2FTJhrWXrn4Zo3RH6Arl6LYDBmc0BNm3WKHwUJRp7yC9zb-wWrrMZ5GGyePI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=g9bHD5zQ_4WM1rWbdVXkNc-aluAgYAYc6f85jZrIcYlO7IDvML9InpZeBITG5OCeq7HXzpabQsqZF-22WgfHxhH8x24Z_g1k_O91rv8fFdZExsZYj6oEbAZdbA33p7xyzRjvXIEJMPdP4FRAB7gD8FzLfKB2oXIQo8x6KHYvSLqCvHfbisx2h8Iziz2iQAB1VEQHcq1d2VP-nDwYMuncEOwLYDZrLBoma8r4KvjyawqS_t5qm1nh5buA11tEYiPeqADCk8XKXX4RodW4BO3lIBKWvuIE8KJ49CA2Kx39GAdSdtdFxrKfRvyCuzNz-VFCTzmf34hpec8KuZCq7h9yH0NmbBY0LpSAb-1TtUTAu_ogmueJ05JWHHXXTpXR0v910XhhgMBzq-ZNj__AOp0BE3ZXUpiE42br2nWQbKsY9RmDW00WBRrUug1Uh0JhS-B8EsKG6bT6lWhN9hMBP5EbPbcSfq1e05eCDbFD0YLfyGop3qhCCepqaRT2rmEEjKrvL51kfRui4KmlSJ5W1-eZDWGMxeV4pLERP4pLryLR5DNa_McZtZbsb4L7tSqE9NugxHJU_jSeIt3Dz3ZoyZ4jHYFXEV1cvZ4liTfdV7naqSjjRb_2FTJhrWXrn4Zo3RH6Arl6LYDBmc0BNm3WKHwUJRp7yC9zb-wWrrMZ5GGyePI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده:
جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch:
کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی خودش اونو به آرت نهایی تبدیل کنه
🎯
ادیت موضعی دقیق:
امکان هایلایت و تغییر دادن فقط یک نقطه خاص از عکس، بدون دست‌خوردن بقیه جزئیات تصویر
💡
نکته دسترسی:
تعدادی تمپلیت آماده هم برای تسریع کار اضافه شده و این مدل در حال حاضر به‌صورت عمومی داره برای تمام کاربران فعال میشه؛ حتماً حسابتون رو چک کنید.
🔗
ورود و تست در وب‌سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⭐️
۶ پلتفرم برای تست رایگان GPT-6 Astra
دسترسی مستقیم و استفاده از API مدل‌های پرچمدار و سنگینی مثل GPT-6 Astra معمولاً هزینه بالایی داره و اگه حواستون نباشه خیلی سریع اعتبارتون رو صفر می‌کنه!
💸
با این حال، یه سری پلتفرم کاربردی وجود دارند که اعتبار (Credit) اولیه یا سهمیه تست رایگان می‌دن تا بدون نیاز به پرداخت، بتونید قدرت این مدل رو توی چت، کدنویسی، پردازش تصویر یا ساخت ایجنت بسنجید:
1⃣
پلتفرم Vercel AI Gateway
یکی از مطمئن‌ترین گزینه‌ها به‌خصوص برای دولوپرها. این سرویس هر ۳۰ روز حدود
۵ دلار کردیت AI رایگان
به کاربرانی که حساب فعال دارند میده. محیط Playground، پشتیبانی از ایجنت‌ها و سازگاری کامل با فرمت OpenAI API داره و برای ادغام با پروژه‌های شخصی عالیه.
2⃣
پلتفرم Brainbase
اگر دنبال کدنویسی پیشرفته، تحلیل ریپوزیتوری و ایجنت‌های خودکار هستید، اینجا فوق‌العاده‌ست. بعد از ثبت‌نام اولیه،
۲۵ دلار کردیت رایگان بدون نیاز به کارت اعتباری
دریافت می‌کنید تا بتونید تسک‌های سنگین برنامه‌نویسی و اتوماسیون رو با مدل پیش ببرید.
3⃣
ابزار Roboflow Playground
بهترین جا برای محک زدن قابلیت‌های بینایی ماشین و پردازش تصویر (Vision). توی این محیط می‌تونید اسکرین‌شات‌ها، نمودارها و تصاویر پیچیده رو بدون نیاز به کلید API آپلود کنید و دقت تحلیل مدل رو با بقیه ابزارها مقایسه کنید.
4⃣
سرویس CometAPI
اگه مدل رو برای اتصال به ربات تلگرام، افزونه یا اپلیکیشن خودتون می‌خواید، این سرویس کار رو راحت کرده. بعد از ثبت‌نام کردیت رایگان میده و چون ساختارش دقیقاً مشابه API استاندارد اوپن‌ای‌آی هست، بدون تغییرات عجیب غریب توی زیرساخت کارتون راه می‌افته.
5⃣
پلتفرم Imaginode
یک فضای همه‌فن‌حریف با محیط تعاملی Canvas، چت، API و ادغام با پروتکل‌های MCP. بدون کارت بانکی کردیت اولیه میده و هر پیام با این مدل حدود ۱۲ کردیت مصرف می‌کنه؛ بنابراین برای ساخت سناریوهای متصل‌کننده متن، تصویر و اتوماسیون حسابی جوابه.
6⃣
سایت Vibany
ساده‌ترین و دم‌دستی‌ترین راه برای تست تفریحی و سریع. در بدو ورود حدود ۳۰۰ کردیت رایگان می‌گیرید و هر بار اجرای مدل حدود ۱۰۰ کردیت کم می‌کنه. یعنی حداقل ۳ الی ۴ تا پرامپت عمیق و جدی می‌تونید بهش بدید تا خروجی رو با مدل‌های قبلی مقایسه کنید.
✈️
@ArchiveTell
|
#AI
#API</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🧠
شیائومی وارد میدان ایجنت‌ها شد؛ معرفی دستیار همه‌کاره MiMo Desktop!
بچه‌ها شیائومی رسماً وارد قلمرو ایجنت‌های سیستمی شده و یه دستیار دسکتاپی معرفی کرده که مثل ترکیب Codex و قابلیت‌های کنترل کامپیوتر Claude عمل می‌کنه؛ این ابزار خوراک خودکارسازی کارهای روزمره شماست.
🖥
کنترل کامل دسکتاپ و وب:
اجرای خودکار تسک‌ها، کلیک، تایپ، کار با فایل‌ها، پر کردن فرم‌ها و امکان ضبط و اجرای مجدد فعالیت‌ها (Record & Replay)
⚡️
پیش‌نمایش تعاملی و ادیت موضعی:
رندر زنده سایت‌ها، گیم‌ها و داشبوردها با قابلیت هایلایت کردن یک بخش و بازنویسیِ انحصاری همان قسمت
🧠
دسترسی رایگان به مدل‌های نسل بعد:
بهره‌مندی تسترها از دو مدل معرفی‌نشده و پرچم‌دار MiMo-X-Pro-Preview و MiMo-X-Flash-Preview
💾
کشینگ فوق‌سریع تا ۹۹٪:
فناوری بهینه‌سازی توکن برای تغییرات مداوم پروژه‌ها جهت جلوگیری از هزینه‌های اضافی
💡
نحوه ثبت‌نام در نسخه بتا:
ظرفیت بتا کاملاً محدوده و اولویت با کاربران فعال اکوسیستم MiMo Open Platform خواهد بود؛ فرم درخواست رو پر کنید تا لینک دسترسی و مدل‌های جدید زودتر براتون فعال بشه.
🔗
فرم ثبت‌نام در نسخه بتا
🔗
صفحه رسمی معرفی
🔗
صفحه رسمی قابلیت ها
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=e-4GPJwqE91N8X3Aswzi_80yeylUzy85XwbvLPFo8ldOp1_jlqj8C51dwigwsUtEgqgTj-VAwJmb2RJaVI0ClBuc9QgjY-n0JhcHqePy8Be6hUZEC0m4cqjxaOIDIxxRC1vROXIkhvAtC7MQSLqVN6SgA4YfV8pvMOacM56cSeQ_DkfodRslrM5AH3omLiSzzrMybsajeqaPxjhrRZMrxm4UJiAtlg75FsXk1wFhxwHaVZrjY200BZOL0O353ocdXJmpSrGvh1kjfsYcO-V2wJu56zab-grf0OzNPDEngeNpV3O5QLpaWKf7Mz4N9Bi5yx6B3JqnSpVQKFa7REz1x122gGXA3dj1eaBpl6vAdwTQR14qw7T6d7j2UOuIewZHF5xHkpqdfNRY2qEa3z555EfSd2gaMaIPdn1eXf3JRTGokKKIK_WBS0hPGAAw-jAuwRptai2zU-GRaJfvWw6CAvUDXKfb87WgIMFjwg4Z3ScP2ycgJIeTTnCWG4sFeKILnsRpgHzJPqi1BTpwoqRyLsumkOj5DO7WbzyCIMP86RtWg5QfYIJ6Gi1SpBH7zQD-Q0TPYSji_vZqrFtCnVBLHd7v6pRQCOX3yNLi-oewkUkewYj67B8XrCjguWVG5kVrAw8rZfpCM3JwX0UDgqeV1xnz_rsZKUH8IUoVpAytfus" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=e-4GPJwqE91N8X3Aswzi_80yeylUzy85XwbvLPFo8ldOp1_jlqj8C51dwigwsUtEgqgTj-VAwJmb2RJaVI0ClBuc9QgjY-n0JhcHqePy8Be6hUZEC0m4cqjxaOIDIxxRC1vROXIkhvAtC7MQSLqVN6SgA4YfV8pvMOacM56cSeQ_DkfodRslrM5AH3omLiSzzrMybsajeqaPxjhrRZMrxm4UJiAtlg75FsXk1wFhxwHaVZrjY200BZOL0O353ocdXJmpSrGvh1kjfsYcO-V2wJu56zab-grf0OzNPDEngeNpV3O5QLpaWKf7Mz4N9Bi5yx6B3JqnSpVQKFa7REz1x122gGXA3dj1eaBpl6vAdwTQR14qw7T6d7j2UOuIewZHF5xHkpqdfNRY2qEa3z555EfSd2gaMaIPdn1eXf3JRTGokKKIK_WBS0hPGAAw-jAuwRptai2zU-GRaJfvWw6CAvUDXKfb87WgIMFjwg4Z3ScP2ycgJIeTTnCWG4sFeKILnsRpgHzJPqi1BTpwoqRyLsumkOj5DO7WbzyCIMP86RtWg5QfYIJ6Gi1SpBH7zQD-Q0TPYSji_vZqrFtCnVBLHd7v6pRQCOX3yNLi-oewkUkewYj67B8XrCjguWVG5kVrAw8rZfpCM3JwX0UDgqeV1xnz_rsZKUH8IUoVpAytfus" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آرشیو ۱۵۰ پرامپت آماده برای خلق ویدیوهای سینمایی با AI!
بچه‌ها اگه با هوش مصنوعی ویدیو می‌سازید ولی خروجی‌ها تخت و مصنوعی میشن، این کالکشن خفن خوراکتونه. یه دیتابیس آماده از ۱۵۰ پرامپت تست‌شده که دقیقاً دستور زبان کارگردانی و سینمایی رو به مدل تزریق می‌کنه.
🎥
کنترل دقیق نور و دوربین:
پرامپت‌های تخصصی برای مدیریت لنز، زوایای حرکت دوربین، نورپردازی و دکوپاژ
🎞
همراه با نمونه ویدیویی:
هر دستور شامل پیش‌نمایش رندر واقعی است تا قبل از خرج توکن، خروجی کار رو ببینید
🎭
تنوع ژانر و اتمسفر:
پوشش کامل انواع سبک‌ها، سناریوها، اکت کاراکترها و فضاسازی‌های سینمایی
💡
نکته استفاده:
تمام پرامپت‌ها آماده Copy/Paste هستند؛ فقط کافیه کپی‌شون کنید داخل ابزارهایی مثل Runway ،Kling یا Luma و المان‌ها یا کاراکتر مدنظرتون رو با کلمات کلیدی دلخواه جایگزین کنید.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIfdqvDQXIM5exAhi86aBIglYT_55XyAu3QuJpdgIE_tqQ-biwBB2__BBY9eD9x91wJnBAFnKJX76_5htEcJQDo19rMxLibEhTRz_pFPWLL5UfcKygr0EjmaYJfC7ZaPW9TebLrqvE3mUPACc9gOHzpvzxQNc8kdCgfFMTskHnFGFzQJzlC_Q_rCZDV2xOdKJ6TXZ7MUq9uNlgXj5z18iaUfh-Rkavozg_vO9shlea4Or7o4fi2G-0BGdFy_9aXG0qjRNNvlHOCbQmeBzkdJexYQKPSxTc2OIrQpD6AehXlGcTY2NsKRcFptL9hX6zia16f2QgjKv4L7kQrLEIiIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مایکروسافت آفیس رسماً مرخص شد؛ معرفی غول اوپن‌سورس GenOffice!
بچه‌ها اگه از خرید لایسنس آفیس یا برنامه‌های سنگین خسته شدید، این پروژه جدید خوراکتونه. یک جایگزین کاملاً رایگان و متن‌باز برای مایکروسافت آفیس که ایجنت‌های هوش مصنوعی رو مستقیماً آورده داخل اسناد، جداول و ارائه‌هاتون.
📝
پکیج کامل و همه‌کاره:
مدیریت بی‌دردسر داکیومنت‌ها، شیت‌های آماری، ساخت اسلاید و کار با PDF بدون نیاز به ابزارهای متفرقه
🤖
ایجنت‌های تحلیل‌گر:
اتصال مستقیم به مدل‌های قدرتمندی مثل DeepSeek ،Claude و Kimi برای تحلیل داده، نگارش متن و تولید محتوا
💻
آزاد و مولتی‌پلتفرم:
پشتیبانی رسمی و نیتیو از مک، ویندوز و لینوکس بدون نیاز به پرداخت حتی یک ریال
💡
نکته جالب توسعه:
جالبه بدونید نسخه اولیه این پروژه رو فقط یک مهندس، توی مدت یک هفته و با سوزوندن ۱۰ هزار دلار توکن هوش مصنوعی جمع کرده! ریپو تازه پابلیک شده و سرعت استقبال ازش وحشتناک بالاست.
🔗
گیت‌هاب GenOffice
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=E10902THLBLdobIpq6aIBuMAHJqzb_32_CtB0zArXMqXVk510KLEwQtCSraizpthJc2cCxVjdjktDQpd29T6AbF4IKwnor4DOF_cAfPGx36C_YtXghWRyTEK1FV4SQJSU_0C0rZuATX473QLhUEZ4s0GjXGOKjRyHJd92AASh_f65CSqLcGWw5ZFPeVTbXBcVV0FHQCF85Oj1YhkEYH4jQoWtja922mjgus6eGcVtReuDtOxGYSrYik_EZxpxz69M_zWeeF3MjwAOgZdXBVwUo6Y-45A-IlPb3EN-dqMbkUcbUf16tkPXWpkenoHGtnwcFP5odJVVTBeT13CBFiB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=E10902THLBLdobIpq6aIBuMAHJqzb_32_CtB0zArXMqXVk510KLEwQtCSraizpthJc2cCxVjdjktDQpd29T6AbF4IKwnor4DOF_cAfPGx36C_YtXghWRyTEK1FV4SQJSU_0C0rZuATX473QLhUEZ4s0GjXGOKjRyHJd92AASh_f65CSqLcGWw5ZFPeVTbXBcVV0FHQCF85Oj1YhkEYH4jQoWtja922mjgus6eGcVtReuDtOxGYSrYik_EZxpxz69M_zWeeF3MjwAOgZdXBVwUo6Y-45A-IlPb3EN-dqMbkUcbUf16tkPXWpkenoHGtnwcFP5odJVVTBeT13CBFiB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خفن: تبدیل هوش مصنوعی Astra به یک بات بازی‌ساز حرفه‌ای!
🎮
🔥
داستان از این قراره که یه دولوپر، Astra رو طوری شخصی‌سازی کرده که عملاً تبدیل شده به یه ماشین بازی‌سازی. اصلاً هم شوخی یا بازی‌های دوبعدی و پیکسلی دم‌دستی نیست؛ کیفیت کار در حدیه که باورتون نمیشه کل این دموی سه‌بعدی خفن فقط توی
یک ساعت
جمع شده!
👀
⏱
سازوکارش چطوریه؟
🛠
همه‌چیز با یه اسکیل (Skill) جلو میره:
* اول Astra باهاتون گپ می‌زنه و از بین ایده‌هاتون، کانسپت اون بازی رویایی که تو ذهنتونه رو درمیاره.
* بعد طبق همون پلن، توی ده‌ها دور آزمون و خطا پروژه رو قدم‌به‌قدم کدنویسی می‌کنه و می‌سازه.
پرامپت استفاده‌شده برای ساخت این دمو:
📝
Prompt (high effort): /dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
🔗
دموی بازی توی مرورگر
🔗
خود اسکیل Astra
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5377Y76rMQgsbAxqMlPLRqs_Noho98YxQJTbiDRXYxegFSlTVcoRZyCLoaJAdoTbkIKuoYkrtqwj1Z75Nv6CY6qbLkkLOUenG4j18pNskzn_gQCewSjQf3WfNxrHZ5nsMApP_fobmIQGjIOPNeJgesCV_N1Wl0U_JuoVXsJTBXQ2hxuOZqw7---qIwFDa6gp5HzJqil7Qk_AfQ0ONkApCxLWM7FgJX8ElgOqaoA0tx7VkJcqcY0ILa7ztzkTPdQbn5DeQgYUflATMt7PnMQ2guDtjN0rHxJJDALLuRPg2uXPqIKRfy77PfopAebL9UA84UlWRlKVSYtD-UhJpaZPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
باز کردن بی‌دردسر فایل‌های آفیس روی اندروید با OpenDocument!
بچه‌ها اگه فایل‌های متنی یا اداری دارید و دوست ندارید برای باز کردنشون تو سرورهای ابری آپلود بشن، این اپ خوراکتونه. تمام اسناد OpenOffice و LibreOffice رو کاملاً آفلاین، سریع و بدون نیاز به اکانت باز می‌کنه.
📁
پشتیبانی کامل از فرمت‌ها:
خواندن بی‌نقص ODT ،ODS ،ODP در کنار فایل‌های رایج DOCX ،XLSX ،PPTX و حتی PDF
🔒
حریم خصوصی واقعی:
پردازش کاملاً لوکال، بدون اتصال به اینترنت، بدون ترکرهای تبلیغاتی و بدون نیاز به ثبت‌نام
⚡️
سبک، امن و باسابقه:
یکی از قدیمی‌ترین و پایدارترین پروژه‌های متن‌باز اندروید (فعال از سال ۲۰۱۰)
💡
نکته کاربردی:
بهترین گزینه برای کسایی که با فایل‌های کاری و اسناد حساس سر و کار دارند؛ با خیال راحت می‌تونید حتی در حالت Airplane Mode به تمام داکیومنت‌هاتون دسترسی داشته باشید.
🔗
گیت‌هاب پروژه
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=id5lwWsOj4KLDFw1FniOjp5nRsC3OwElJ7GRKPe-qG7YqS3I6CAp_AlQ6Y9RKgtVEWnAJb_Z82SwENA15qV1fosKizsJ56RwxCAL6JN-wbBqpG5vEidvDT0ObTv9VM2M8_Dv5m_Ah2aSrdm36LnWySUNqXh4z4lfU-zP1QrpnmWWfBozy2xhy8Cm9eRYXoqsrfPkbEQABCcuPw1OIJE0SS4kidxaWyf1QW9IH33vBK3kkAwwglJ-3HX52ls3_4ASXZAYlPh39N2fwaAuQjnXMLImxwfdskMbIBdSBSHxp34XgOALZYQxGmjpCxJJmIN7CkxDK2Wo4yYZzDpH4UMWBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=id5lwWsOj4KLDFw1FniOjp5nRsC3OwElJ7GRKPe-qG7YqS3I6CAp_AlQ6Y9RKgtVEWnAJb_Z82SwENA15qV1fosKizsJ56RwxCAL6JN-wbBqpG5vEidvDT0ObTv9VM2M8_Dv5m_Ah2aSrdm36LnWySUNqXh4z4lfU-zP1QrpnmWWfBozy2xhy8Cm9eRYXoqsrfPkbEQABCcuPw1OIJE0SS4kidxaWyf1QW9IH33vBK3kkAwwglJ-3HX52ls3_4ASXZAYlPh39N2fwaAuQjnXMLImxwfdskMbIBdSBSHxp34XgOALZYQxGmjpCxJJmIN7CkxDK2Wo4yYZzDpH4UMWBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📍
با GeoSpy لوکیشن دقیق هر عکسی رو دربیار!
بچه‌ها اگه دنبال لوکیشن یه عکس رندومید یا اهل چالش‌های OSINT و ژئوگسرید، این هوش مصنوعی خوراکتونه. حتی اگه متادیتا (EXIF) پاک شده باشه، از روی خط‌کشی خیابون، گیاهان، معماری و تیر چراغ‌برق مختصات رو براتون پیدا می‌کنه.
🌎
جست‌وجوی جهانی (Global):
پیدا کردن چند تا از محتمل‌ترین کشورهای دنیا حتی از روی اسکرین‌شات یا عکس کراپ‌شده
🏙
مود شهری (City Search):
اگه شهر مشخص باشه، با عکس‌های خیابانی مچ می‌کنه و آدرس دقیق پلاک و خیابون رو میده
📸
تحلیل چند زاویه‌ای:
امکان آپلود تا ۴ عکس از یک لوکیشن برای بالا بردن نجومیِ دقتِ حدس
💡
نکته طلایی:
کیفیت عکس اصلاً مهم نیست؛ این ابزار حتی فرم شاخه درختا یا مدل آسفالت رو می‌فهمه! موقع ثبت‌نام اولیه هم یه سهمیه سرچ رایگان بهتون میده تا تستش کنید.
🔗
وب‌سایت ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArIgURoAV-RFDYL-V-d9QoFeY5h2cTXyFSugknRIOrFvhTKseCJIaCOAkqUeoKpuswZ-vQPIUcAycPtYi8qjVVEfT5FbGSvJGFzFjiAjdQajTTkYi0dfN1CSI8RmTSk1H0lLwjZXDacwodD2NGF4kNgnjEQaWJCiJ6XgQL4nCDJL4QwtWi0wsVhHhZMKlAYSVv23tYEczcgtZOLwUTYWnSa9Uv0xI9eEs6A9JrAOIl8a7jKkZcmkarGpqpLeJyN7FTJA5ICE4oQa8PBpRzR0eKAJILNAoemybzVESqkovIy9NAgMEmm1hpM6F8QIgaH1K5FYIOKQCaJVGcYqnYcBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕸
با SpiderFoot ردپای دیجیتال هر چیزی رو توی اینترنت بیرون بکش!
بچه‌ها اگه تو حوزه امنیت، تست نفوذ یا اوسیانت (OSINT) کار می‌کنید، این ابزار دقیقاً خوراکتونه. اسپایدرفوت یه ابزار متن‌باز و بی‌رحمه که کل سطح وب رو شخم می‌زنه تا تمام ردپاهای دیجیتال و آسیب‌پذیری‌های یک هدف رو دربیاره.
🎯
تارگت‌های همه‌جانبه:
جست‌وجو بر اساس شماره تلفن، ایمیل، آیدی توییتر و تلگرام، نام، IP و دامنه‌ها
🤖
اسکن تمام‌خودکار:
جمع‌آوری آنی داده‌ها از بیش از ۱۰۰ منبع اطلاعاتی بدون نیاز به سرچ دستی
📊
نقشه ارتباطات بصری:
تحلیل داده‌ها و نمایش گراف‌های دیداری از اطلاعات لو رفته و پیوندهای مخفی
💡
نکته و اجرای سریع:
راحت‌ترین راه اجرا با داکره؛ کافیه دستور docker run -p 5001:5001 spiderfoot رو بزنید و پنل تحت وب رو باز کنید. (یادتون نره، فقط تست امنیتی قانونی و اهداف آموزشی!)
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EswP_6cIQk9Eld2VNcbxWp8Nfm0oJaKWQp0VE3yv20S-N7Get31CzszU0lpCrq9LeovzOCf9gTXs-fldJRRAUtRWE2r5Ap86wt3ic6kQdnZMzyLBmMdDzh69RCAyl6OUhVGKumHo012DyRHvJJFxq4qg0Ng-VL5BbdKeAZ5tsZMbMkjeG19GVYMpjJTuKn21C-DaI2FrUA_BZLzRF6r0tO6lUnUBJsskZAEsezEC3TJ--pPV5Xpr7T21UCtjHJX5v8ODMzjL8iXXAz0zh00xksLvDaz1os_hXaGNVQExPTk-FFeo4ZzAsdNBHaFQBzrxqrxZUvyrqX0ZEpxjxf21VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توکن‌های نامحدود برای Claude Code با شاهکار مهندسان اسپاتیفای!
🚀
🧠
پلتفرم
Portal
مثل یک مدیر هوشمند عمل می‌کنه و با واگذاری وظایف ساده به مدل‌های ارزان‌تر، تا ۹۰٪ در مصرف منابع و توکن‌های هوش مصنوعی شما صرفه‌جویی می‌کنه!
🔥
🔺
تندخوانی با Gemini (bulk-reader):
فایل‌های حجیم و چند هزار خطی توسط Gemini 2.5 Flash آنالیز شده و فقط یه خلاصه مفید به Claude تحویل داده میشه.
🔺
کدنویس روتین (code-writer):
تولید کدهای استاندارد، تست‌ها و تنظیمات خسته‌کننده به مدل‌های کم‌هزینه سپرده میشه.
🔺
تمرکز روی کارهای حیاتی:
با این روش، Claude فقط درگیر کارهای پیچیده و استدلالی (مثل رفع باگ و طراحی معماری) میشه.
💡
در
نتیجه:
یک ترکیب هوشمندانه از چند مدل AI که باعث میشه هزینه‌های شما ۹۰ درصد کاهش پیدا کنه و خیالتون از بابت محدودیت توکن‌ها راحت باشه!
🔗
لینک دسترسی و پروژه
✈️
@ArchiveTell
|
#TOOLS
#AI</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syS07tqLvalkwoOFGNeh3xDwvHTWcHozXPuJIQphfQmgoFbMXV117dCcBBjYNM7ZstmZJiwW0nVC0lRuHf9bUOZ2gGlpE84fTnB1j3ELEHCLhspeuNFZ_soEgNhDflxIAJ8lFRRXbRuFhO-I_OIW6WVPF4IQ8jPKYXYpdEuJSZ67rPXXg5wa_S-BJ6tkrM3ng5gg8qYIDavZaujM6ni1G_kM88ghF8Dafo3XIpYpQOgarMt-ylVH4N8IdTZTbY4NWL3r_MZEPF1kuPFrjXKItDvcjMQ_0QgmXlZi-2zpch2FA8wu8kWdGyyBrQ91i9efB7hEKzu77SQa1NELWslKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esmDyrgQDHEq4ZWwsHyybRoNm1lC4cSzzIFeSvrlAXmVkzwMEHsihaS_NzFTWhU-WI5zesVhd5sah3FDoKuJVO2mHz2NX-0YYotBl67YgEd1Inh5s50Rs4iYoSeASa-mqLtu2Z7Lm1Z-q4Yr2Ikc5iPm3zet8Xyg_YRk50cnM2I9RgEDtvKhIlm4GDzRjjeLHjnECQqXmYY57pt1WOJ608FdMcyWP52xlRQn0r6EyxWOQ7tgBKDEqLyNE4MnMCHr7xsTzVje0cAAykAQMt0DqX4I_k-dBTNoyTrc0BhugxmQ2PaWR0YGx0G0WXD5SJpM1lYQHJLiuF_4HCO6ppqf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iefKqhYaYTNU_KtCVXzfVS7QZxViqk9IXIRGRT4ijGxJl9-apRzE-JtmeQkBTm5IMshP8-MOBdJgrU1LjzJR2DMOYWRpopVrHKLq2CwkkjWzPgrP-HqjXY85KhZkqplq6HV73wGdPf_L1ysxTIpm_R36sZDZqbp_TkexECUjRY0ZI7BTWDhn79E3dgW8mj2JjZVPHnQRx9f8jdl9h3G7kOVTV7W7m7CfykgFZP2Xlf9-X9ibdVpYGg9A7P3tat3c_-_igqG91hkLoviD-MyqJiD8714-2pMJA2r7iw6rH25AeBDzDwB5mPmjuYNbSuk2JX5Dw5uqVHEK4LN1-sheNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📌
مدل GPT-6 Astra بازم یه حرکت دیگه ثبت کرد؛
بازی Portal رو تو 23 ساعت و 43 دقیقه تموم کرد!
مدل به طور خودکار شخصیت رو کنترل می‌کرد به طوریکه هوش مصنوعی یه تصمیم می‌گرفت، بازی متوقف می‌شد. GPT-6 Astra با استفاده از تصاویر، موقعیت شخصیت و زاویه دید دوربین، تصمیم می‌گرفت که چه اقدامی انجام بده. بعضی وقتا هم تصمیم گیری هاش تا چند دقیقه هم طول می‌کشید، اما در هر صورت تونست بازی رو به پایان برسونه.
🔥
این کارو آقای "cozyblaze" با کمک اشتراک ۲۰۰ دلاری Codex Pro انجام داد.
🔗
سورس پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPfMlXjCuCO2-lFHPnQgIlmmlLLXVwJsPekFvjN9DUPus7sgtHmlNarZ48lFJRp9hm_Ujg9uW8IATPTGt3FWm-Lens6Oxuu1M6-m9yydsHKmqBT5YGDxiwdaVpzs_mCdZ-fhBXWDTeYe7Ni7zVEwxfMvgBXtem-BqpRUDzIGH49U2UZqKA-FCWRSXdXcvqePHWqxY2td6UhTdVyaMVFdTKLC0WCNIjWkjDjqpjMSRAMC9ujVPTzbkAm6_4f_Nl6pjZxNtJXp2VN_Numw2dGCWD8WpA3IOIdodpR2q5cE9yMR1bu8tqVHnxSJjU8mmHQOIAm2IW978nX8pTwIP6_YAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعبه‌ابزار همه‌کاره برای برنامه‌نویس‌ها با DevToys
💼
اگه خسته شدید از بس برای کارهای روزمره (مثل تبدیل JSON به YAML، تست RegEx یا دکود کردن JWT) مجبور شدید سایت‌های مختلف رو باز کنید،
DevToys
دقیقاً چاقوی سوئیسی شماست!
👍
🔧
بیش از ۳۰ ابزار کاربردی:
انواع کانورترها، انکودر/دکودرها (JWT، Base64، QR)، فرمترهای کد، هش‌ساز و فشرده‌ساز عکس.
📄
تشخیص هوشمند کلیپ‌بورد:
به محض کپی کردن متن، خودش می‌فهمه چیه و ابزار مناسبش رو پیشنهاد میده!
🛡
کاملاً آفلاین و امن:
تمام کارها روی سیستم خودتون انجام میشه و دیتای حساسی سمت سایت‌های ناشناس نمیره.
➕
پشتیبانی از اکستنشن:
میتونید ابزارهای دلخواهتون رو هم بهش اضافه کنید.
📌
لینک مخزن گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=VHNPbJqO_QrV2Fa9FewfH6TVipj-3A9jLs1z8L5F6cRy4hK6KvBaOPKc1fqmtIOF7mUBO7q1Mo76j5gafdE6UWydHyk2CALc6C1SAXOUFARDnA1ERpeTL7QUifeDNJ5a_7fMV7OQnXT5GxUaNZKLQTVe0wn0ewM2XTyLqsn8lwg1E3fcODsIg_Ha1xMGjd7R52Fe_mtl4pPqoSyCkWOEa-oN5kkJEBg49vYX2X_XYB6FcqYLDsD4g52CvvZgV4jMcTVhvcXcrkPruXNFJT09P0IdZ8PN8nXOoRBopqnvb_pl5vZXOYDv0T_J7y3NFfoFCiTSnCBiwKXz-CcvmPU5Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=VHNPbJqO_QrV2Fa9FewfH6TVipj-3A9jLs1z8L5F6cRy4hK6KvBaOPKc1fqmtIOF7mUBO7q1Mo76j5gafdE6UWydHyk2CALc6C1SAXOUFARDnA1ERpeTL7QUifeDNJ5a_7fMV7OQnXT5GxUaNZKLQTVe0wn0ewM2XTyLqsn8lwg1E3fcODsIg_Ha1xMGjd7R52Fe_mtl4pPqoSyCkWOEa-oN5kkJEBg49vYX2X_XYB6FcqYLDsD4g52CvvZgV4jMcTVhvcXcrkPruXNFJT09P0IdZ8PN8nXOoRBopqnvb_pl5vZXOYDv0T_J7y3NFfoFCiTSnCBiwKXz-CcvmPU5Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم 7 برنده خوش شانسمون
🎉
:
1.
@reza1629
2.
@mhti9
3.
@KIING_ZOG
4.
@Gogogrugo
5.
ＮＯＢＯＤＹ
( 6641463426 )
6.
@an_Y008
7.
@AshenOne2077
برای دریافت جایزه به دایرکت مراجعه کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🥇
رکوردشکنی دوباره از GPT 6 Astra
خبر رسیده که GPT-6 Astra تونسته تمام ۴۸ مرحله بازی «I'm Not A Robot» سایت
Neal.fun
رو بدون غلط رد کنه ، خیلیا جوری جو دادن که انگار آخرالزمان امنیت سایبری رسیده!
😂
طبق معمول، ته این هایپ‌های رسانه‌ای خبری نیست. کپچاهای تصویری سال‌هاست که عملاً مرخص هستن و حتی مدل‌های پارسال هم با یه پردازش تصویر ساده دورشون می‌زدن.
سیستم‌های امنیتی واقعی وب الان با تحلیل رفتار موس، کوکی‌ها و الگوی کلیک کار می‌کنن، نه با ۴ تا عکس چراغ راهنمایی و خط‌کشی خیابون
😁
تست کن ببین رباتی یا نه ؟!
🧐
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn-BB87mW_O0pNhUbZWI3AdBfaeKA7iIMo18PCspC6qIhpiiLa2rP3781gCD6BLWiMcnjp05AiU1OlOWC2JRiTNnzkZbbKs4zDQoNUl7FAkAwHIu1fTgW5_kn4f-fM8dLgP9fLfTGKlL35EowattxLOpAqelm7B2qczXcd9XtBwvbvb31jWhl5MOndypn0qI6pFrieqhVY4cOOywa-Tkd99m6ClICAergaJaSlQ-FzNVH8sj4IV7Dt170QxttBBX6cIX7nDP6TGAl6EaPUZ5dWfTyxpOhof9rr4G3SHGdZv2lhLI0R5x7ttaTQfOrqSn722uv_ophe_xJm91tXPQwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جداسازی صدای خواننده از موزیک با هوش مصنوعی؛ تمیز و بدون دردسر!
🎤
🎧
بچه‌ها اگه دنبال ساختن نسخه کارائوکه هستید یا می‌خواید صدای خواننده رو برای ریمیکس بردارید، ابزار آنلاین
AI Vocal Remover
دقیقاً همون چیزیه که لازم دارید! با استفاده از مدل‌های صوتی AI، وکال و ساز رو در چند ثانیه مثل آب خوردن از هم سوا می‌کنه.
✅
🔺
پشتیبانی از انواع فرمت‌ها:
هم فایل صوتی (MP3، WAV، FLAC، M4A و...) و هم فایل‌های ویدیویی (MP4، WebM) رو به راحتی قبول می‌کنه.
🔺
بدون نیاز به ثبت‌نام و کاملاً رایگان:
پردازش تماماً در کلاود انجام میشه، قبل دانلود می‌تونید آنلاین پیش‌نمایش رو گوش بدید و تا یک ساعت خروجی MP3 یا WAV بگیرید.
🔺
کیفیت و دقت بالا:
تفکیک دقیق لایه‌های صدا بدون نویز و افت کیفیت محسوس سازها.
💡
نکته:
برای آهنگسازها، تدوین‌گرهای ویدیو و یوتیوبرها برای برداشتن کپی‌رایت یا ساخت بیت‌های بی‌کلام، این ابزار سریع‌ترین میانبر بدون نصب نرم‌افزارهای سنگینه!
🔗
آدرس ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiZMwbrPDyjLLMY8IYyPRJ4j8K1VlhaEO3uv2NlbnX2Ld-6S3RWlnOe9kTSaulryz-lId9yVtVA_mcEFU1tE853XiAG7bCHgoQ9AodgdGwsHr5mV7R4Rq6hWLIiNRVhJyq2vIKN9nw2AwaFzg160WADwc_mCURU3Se5hp9ZdufAw4QucL0nQ-hNrF0cj7-lJrrInCPjd3dkRzWf_JvGAlzr-RiqiFRzNYAbsg9E75AysRc_BNBmlz4wmRGNNugHOe1Nw-aofhkSDEEuZP4ZKitGBusZx-s603K1e0XpHiZDkisE-Zaw6rclsMx0ebFdP5sLvkb9gQa1yEEAGmhPamg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل گوشی اندرویدی به یک کامپیوتر دسکتاپ کامل با Android DEX!
🖥
📱
اگه از قابلیت محدود سامسونگ دکس خسته شدید یا گوشیتون اصلاً DeX نداره، این ابزار خوراکتونه! نرم‌افزار
Android DEX
با ترکیب جادویی ADB و موتور قدرتمند scrcpy، گوشی اندرویدی شما رو به یک سیستم‌عامل دسکتاپ واقعی با پنجره‌های شناور و کنترل کامل تبدیل می‌کنه.
🚀
🔺
تجربه دسکتاپ چندپنجره‌ای:
اجرای اپلیکیشن‌های اندروید در پنجره‌های تغییر سایزپذیر روی ویندوز، مک و لینوکس با اتصال باسیم یا بی‌سیم (Wi-Fi).
🔺
خوراک گیمرهای موبایل:
کی‌مپینگ حرفه‌ای کیبورد و ماوس، شبیه‌ساز جوی‌استیک WASD، قفل دید ۳۶۰ درجه شوتر (FPS Mouse Lock) و حتی شبیه‌سازی ژیروسکوپ!
🔺
دور زدن شناسایی امولاتور (No Ban):
چون بازی‌ها مستقیماً روی سخت‌افزار واقعی گوشی اجرا میشن، آنتی‌چیت بازی‌ها شما رو شبیه‌ساز تشخیص نمیده و بن نمی‌شید.
🔺
امکانات یکپارچه سیستم:
مدیریت اعلان‌ها، پخش صدا، انتقال فایل با درگ‌اند‌دراپ، رکورد صفحه و تعریف پروفایل‌های اختصاصی برای هر بازی.
💡
نحوه راه‌اندازی:
فقط کافیه گزینه USB Debugging (یا Wireless Debugging) رو توی Developer Options گوشیتون روشن کنید و برنامه رو اجرا کنید؛ بدون نیاز به روت!
🔗
گیت‌هاب پروژه
🔗
سایت پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYPPD2gGTNDpWUf3Q_fDQ2q_KoBviBNGiqtqqEvCjCYwifLW3u9ftSbVktGcJ-I9LvsqZcfxLo8figU76p3bMlHzzwygu74NXut2-XlWHpIhfurTC7DegKbuBNa8g3fpA8ClR5lkh-NIMf-uYFZanRuhTBdY8kCZFNSm15zOeqvaNFyU8w4nhND67vgUxy8yhcyQ2mQ2S0JEVyP_T4Tn53UoG6d3sleN1MjWkB5BZR7DCgZfB5IznmimECAV604BlmAmgSxUPtgsMgNYBjQXb0-HY8YD7CCCgK3Yfwj9u27sTZPfGdmCKeaddBGqVwOvmKnmDFgjxz5a06HtkdNxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معدن مقالات و دیتای آکادمیک اروپا؛ گنجینه‌ای که کمتر کسی می‌شناسه!
🎓
بچه‌ها اگه دنبال مقاله‌های خاص، دیتاست‌های خفن یا پژوهش‌های پروژه‌های اروپایی هستید که جای دیگه پیدا نمیشن، پلتفرم
OpenAIRE Explore
دقیقاً خوراکتونه! یه پایگاه عظیم با بیش از ۱۳۰ میلیون دیتای علمی دسته‌بندی‌شده و رایگان.
✨
🆓
🔺
آرشیو عظیم ۱۳۰ میلیونی:
دسترسی مستقیم به مقالات اوپن‌اکسس، دیتاست‌ها و حتی سورس‌کدهای پژوهشی پروژه‌های اروپایی.
🔺
بدون لاگین و کاملاً رایگان:
بدون دردسر ثبت‌نام، پی‌وال یا محدودیت دانلود، مستقیم به منابع معتبر دسترسی دارید.
🔺
ردیابی شبکه‌ای پژوهش‌ها:
می‌تونید خروجی‌های مختلف یک پروژه (مثلاً مقاله + دیتای خام + کد نرم‌افزاری) رو به‌صورت متصل به هم پیدا کنید.
💡
نکته طلایی:
برای پژوهشگرها، متخصصان هوش مصنوعی که دنبال دیتاست‌های تمیز و رسمی اروپا هستن، یا کسایی که دارن روی مقالات بین‌رشته‌ای کار می‌کنن، این ابزار مثل یک میانبر تمام‌عیار عمل می‌کنه!
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds0bRdc_aHDFsz7crrp-r4dixo4Bfy46Fv0lrfUgClvPcJ43MiWfUxFEAKCMnZohK5H4PDsLi8SJkPQ48Lgbf36NCbmJTUOery_s53T1J2ULSzilNxvFMOOxTm9t_qY3safRNARz_fVPvHbhckZJs-0QSNMNq4dgcvC3c6FG0pkDBNMZU3kfYbH4gvZklbXB6a5lZQ3dpC0Nn3Beil_pgyBSQN0eid2_tQEdRO-zjP2pYZ64Sutf8eBlkkDS5fQru0Ks_qRyw3jbmu8-7kCiBJMJRpy2zIbhGSEPzzrBN6DPdx2Q4hXTXCMeeeii7iVnsPwODNVkuFjefPUeCNLgKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیبورد «شریک جرم»؛ قبل از ارسال پیام حواست به جریمه و حَبسش باشه!
🚨
بچه‌ها براتون یه پروژه به شدت سمی و دارک آوردم! این کیبورد اندرویدی اسمش «Соучастник» (هم‌دست / شریک جرم) هست و کارش اینه که موقع تایپ، متنتون رو آنالیز می‌کنه و آنلاین بهتون می‌گه ممکنه بابت این پیام چقدر جریمه بشید یا چند سال برید آب‌خنک بخورید!
😁
🔺
کاملاً لوکال و آفلاین:
نیازی به اینترنت نداره و داده‌ها از گوشی خارج نمیشن؛ با llama.cpp مدل جمع‌وجور Qwen3.5-0.8B رو آفلاین روی گوشی اجرا می‌کنه.
🔺
سیستم دوسطحی سریع:
اول با یه دیکشنری سریع کلمات حساس رو بررسی می‌کنه و بعد مدل هوش مصنوعی جرم یا تخلف بودن متن رو می‌سنجه.
🔺
پروژه کاملاً اوپن‌سورس:
کد و نحوه کارکردش روی گیت‌هاب قرار گرفته و برای گیک‌هایی که می‌خوان اجرای مدل سبک LLM داخل اپلیکیشن‌های اندرویدی رو یاد بگیرن عالیه.
💡
نکته:
هرچند قوانینش بر اساس مواد قانونی روسیه تنظیم شده، ولی معماری استفاده از مدل‌های فوق‌سبک لوکال برای پردازش آنی متن موقع تایپ، ایده به شدت خفن و قابل شخصی‌سازیه!
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZXPmpV5v1AGhYb8lxyEgXFriq0REX5aZW8NnfqBiCyQ7QOoUOHxijYZgGwG1wpAkFt1CrpmBqx77JYkXYBqkbpduMhDDkdncK1EYVyL46i45Co1Ia3Jq7kEQCpYCe0gyOnOIEr6ni7ZBuBPQFiTh_y33yVjWs5OvRcQshRQcR0AUWhOniezW-H5qutfVvbUOGXX0IILFAeO71z5KJX9rjVR-r_7bXppmwF4IK3YduPcTZmtPRCB3BRphZk9GpTSCY3-3AmkWJvPdZN_c5C2MnFwquuCM3eqPNMeHgM5rfIZi4q-KF0R2tYxhXw9REZ6i7EDcBoe3gbDTIqM10ZJ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طراحی و ساخت اپلیکیشن با M3E Canvas
🛠
📱
پلتفرم
M3E Canvas
یه پلتفرم اوپن‌سورس و جدیده که بهتون اجازه می‌ده با درگ‌اند‌دراپ و کمک هوش مصنوعی، برای اندروید و وب رابط کاربری بسازید.
🔺
طراحی سریع:
المان‌های آماده رو می‌چینید، رنگ و فونت رو شخصی‌سازی می‌کنید و همونجا تو مرورگر تست می‌گیرید.
🔺
تولید پرامپت جادویی:
جذاب‌ترین ویژگیش اینه که در نهایت از طراحی شما، یه پرامپت دقیق می‌سازه که می‌تونید مستقیم بدید به ابزارهایی مثل Claude Code یا Codex تا براتون تمیز و بی‌نقص کدنویسیش کنن!
📌
لینک دانلود / گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه
ArchiveTel
رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد
این ربات
رو استارت کنید
2️⃣
در چنل ربات جوین بشید
3️⃣
با آیپی خوب ترجیحا آمریکا وارد دکمه بشید تا سایت باز بشه و دکمه وریفای رو بزنید
‼️
نکته :
در هر گوشی فقط 1 بار میشه اگه میخواید با یک گوشی تعداد بیشتری بزنید باید هربار کلون های تلگرام رو نصب کنید  ، هر 5 رفرال برابر با 1 اکانت هست ، تمامی کریدیت های جمع شده تبدیل به اکانت میشه و قرعه کشی میشه و لینک فعال‌سازی به شما داده میشه
‼️
شرایط : حتما باید در چنل آرشیوتل عضو باشید
تاریخ برگزاری ، فردا دوشنبه ساعت 20
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHnh5KQcXtdBO7PpanN_p9fQp00iPf_2jVTmylmamblg7VszkLBjLgUOmcDdm6qmIe1R-4loKxkABb4XPriHoshKuSc_pqHzIRRkdOG6VLwpmMMnhvA9cBN2Iqw0zJQlXJ56XSDuo8GhgtnMx2o1AF2vzp24FBcF7ZA0VpZO6mdfIuP8SOooNjeYxeTX1dMl6jMxBlHJI-M_6tcSm3H4NrlVV7DkqtmjqE1dBTzzQmWjDsA4sI5VRdtC2qZLpxiKszIenSISmjMHhlGe_ufY3UQ-P1Q7XA5j_5pgp02sZ56dsUss6kTIETEhQzVrkZHUU25bTNJY1YN8pWibEBE4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی ها
💥
🆓
DeepSeek-V4-Flash-Vision-Exp | DeepSeek-V4-Flash-0731 | Qwen3.8-Flash-Next
✅
این سایت ثبت نامش کمی آزاردهنده هست بخاطر UI بدی که داره ، باید با گیتهاب لاگین کنید بعدش میره تو داشبورد و به ایمیلتون کد میفرسته و اون کد رو توی مراحل وریفای وارد کنید ( شماره تلفن لازم نیست ) حالا بگردید عقب و از سایت API دریافت کنید
✅
هر روز این سایت 1 PTS بهتون میده که معادل 10 دلار هست و خیلی زیاده برای این مدل ها
🚀
محدودیت هم هست 20 درخواست در دقیقه
‼️
📌
Base URL :
https://developer.amd.com.cn/radeon/api/v1
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBsMkaKOf2SCLjD83CEHGGfB84f2OiUMaG13hpzxUXCrnRBjibKm086X_JnrEzK-lv7oq_0Bb9CLa37t5u-NnECCYaWaS11PkihS3D5qhue3xdK2Vy3292EQrZvB3UlBoQsFflkfSl_izrOUvvnj7XzyVBHsWPKkA62s0tBRN7a5v0usrLHQJip_oxVPFVIUjQZ0k6CMV_m17z-Yiz18-_UbuHR8-gahOx8L3S4ZRnxQ03lwHqU1UWJ2lAp4Nq7wd1cDsCMSFXi4nO00TYs8Y_xvFmzJCQUxjH2PMo71VbwcMgov6Vn-lrt6kGDOoYt8A2lLhk3NAJxjCL_B8T8cwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به هوش منصوعی های محبوب
💥
🆓
Opus 5 | GLM 5.3 Flash | Deepseek V4 Flash | GLM 5.3 Flash
✅
4 میلیون توکن میده که میتونید استفاده کنید از API هر روز هم ۱ میلیون توکن میده برای opus 5 ( حد مصرف روزانه هر مدل ۱ میلیون توکن هست )
📌
Base URL :
https://helyxai.space/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-7XbyJQA0vO-mkHkcmYhPuU13b8Y9Fh_c9Byge3BYACN5BGkIUlYGvpjFFtRtGkdVvh-iz2dWl3PiFB9NBO3FPTKdNeVMi4LeIKg37hzOyRWyh-wc7H6qQS5r_MWn84tjtFrq-5aXJkfk5vUYq0bwCj1fJG1d1d7TXIXwfBqoCaiIeN60oKWVnbaohOlMKg90_y5-jM7UCACXQfVBhyuhQz5NmO1cst8eJpWTNYWhr2yR3JS80k3PX8ungpbPQUbV4NSlr6_4z2i4HL4mP0uLYKAkdXKuU5wg7wocp0RumXNA5WziHOeH-CMy3Abe2ZdG86WRWGkKJ-Nc0f2QUCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏
اینم لیست مزایایی که داره:
‏• جمنای: ۱ سال رایگان
‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه
‏• جت‌برینز: ۵ سال استفاده از تمام ‌IDE⁩ها
‏• گیت‌هاب: پکیج کامل توسعه‌دهندگان
‏• آفیس ۳۶۵: نسخه کامل ورد، اکسل، پاورپوینت و تیمز
‏• فیگما: نسخه حرفه‌ای مادام‌العمر
‏• نوشن: اکانت پرمیوم مادام‌العمر
‏
برای دیدن آموزش کلیک کن
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL2ea-rc7AiXfBYpax_Uj_THIGPvhmUPWs8oszA6WD_KdkrTZqxwSLkGObE33Tp4HVED5c4nEngGQMLMeysWhzAgviRm3sfKqi5lEaTWgMZjPpMktZdyyvidgct5oMAwT_sxDFyavLCX6swA896M9G_Fc3v8uxLLNVPCKLthO6mw7KZf6J2gYm7IDj-xUBiYMS8VfDJWiH7BHRBK923gfkykcYPfq1Ay7ocx-OPhKe0moN3ucdjLGcHsGZV7Z4hNPI5h7YaNqugQmp4KZgEj3VuadrIojPS6Ky3J1249wmydfYXQyCmimMEzd5zbjL4XwSvyEafUh_gGw1HQzrk9jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
داستان GPT-6 چیه؟ انقلاب هوش مصنوعی یا فقط شوآف تبلیغاتی؟
🤔
این روزها همه جا پر شده از اخبار رکوردشکنی GPT-6 Astra و نمره عجیب ۹۹.۹٪ در بنچمارک ARC-AGI-3.
طبق بررسی‌هایی که کردم، این نتیجه تو شرایط کاملاً ایزوله و خاص ثبت شده و توسط منابع مستقل تایید نشده.
قیمت‌گذاریش هم به شدت نجومیه؛ هر یک میلیون توکن ورودی ۱۰ دلار، و خروجی ۵۰ دلارِ ناقابل
😁
(مقایسه کنین با جمینای ۳.۸ که ۳.۷۵ دلاره)
در ازای این هزینه سرسام‌آور، وقتی در کل حساب کنید، برتری خاصی نسبت به رقبای خودش مثل Fable 5 نداره.
یکی از معدود بنچمارک‌هایی که هنوز اشباع نشده و به نظرم بهترین معیار برای ارزیابی مدل‌هاست، بنچمارک Humanity's Last Exam عه
تو این تست، عسترا نمره ۵۷٪ رو ثبت کرده؛ در حالی که Fable 5 با قیمتی مشابه و حتی پایین تر، نمره‌ش نزدیک به ۵۸٪ عه
🔥
با دیدن همین آمار میشه گفت OpenAI با این Gimmick های تبلیغاتی، رسماً داره به شعور کاربراش توهین می‌کنه
😐
من حتی کاربرشم نیستم ولی باز به شعورم توهین شد
#طهلیل_ai
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8GY81u86iHlDun6Bj_qfvLXu2HfVk9T1hQA-Ev7HG1U_eu9dQgT3IKxZDQNRmZnG5p7fJwWGdAkrQ1WNt1S2cjYwbQ26ZWP15JInbEomODOn78-gX3QB-DxR31hRVf0nJKUVcRj-Y5U7b1bqAZO54hXpbY5kcFsKp_RtNNX9xZaWqPIt40TnzTZ5Y0MQJssu5dS3sWdayg0gz7mq-xnb4ImaJ6oOUA1bOFeezd01taTkIUTyrE0DRf2cwGqLVSFcM7vZlRrG2MTJQ-l4ts92dMDiRWrCj84d-I-nmzf4m6kpccj0WHkr837760YpLs5KXn69UGnSLcLqFl9ZpKHyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Free 2k$ model GPT
💵
📌
Base URL:
https://vip.9aws.net/v1
📌
API KEY: sk-g926rIr0SG7pfoD4WextkZwRRAgFOwYZDsG5hnDr8mL2ZH9d
📌
Models:
gpt-5.5
gpt-5.6-sol
gpt-6-astra
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrfHBirvO8xMecTbKQHr7UmxYkIJbwXWHFJDk6JcOi9k9yasAG7W35nYpBx-CUKbVHLLECoW_9H4hoQutamrLxKckBdv1zgYn8b3ODaYhFY3nKZ-mTFVb860yzyOKFgMjGwNmZpf95ySljOWq2ibet4o_yolFFcPXvq2Sv3wozPOli6tV9YlRULtmFy4spRiRMNYEbUn9n4-GKi1ZRC6mZgnFh2wZUg40xmpPwQPWK9wCfwIqnsyYLZVwm-c48U1iHEu5ZYGEVeoaKavO-hzPcRLXn-Lw74nYbVVJkE_Nzso-FL6UMhAnJGZCSWt1HtZri0z4Gi4KuVYXN0PgXESbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی آزمایشی رایگان به مدل‌های پیشرفته هوش مصنوعی
💥
🆓
Opus 5 | GPT 6 Astra
✅
سایت ClickUp فقط یک ابزار مدیریت پروژه نیست؛ ClickUp Brain حالا امکان استفاده از مدل‌های مختلف هوش مصنوعی را در محیط کاری ClickUp فراهم می‌کند. طبق مستندات رسمی، مدل‌های OpenAI، Claude و Gemini در Brain قابل انتخاب هستند و می‌توان بین مدل‌ها حتی در یک گفت‌وگو جابه‌جا شد.
🚀
🎁
سهمیه رایگان
در پلن Free Forever، نسخه آزمایشی Brain شامل ۲۵ استفاده برای هر Workspace تا ۱۰ نفر است. در Workspace های بیش از ۱۰ نفر، این مقدار ۵۰ استفاده است.
✨
⚠️
این سهمیه ریست نمی‌شود و پس از مصرف، برای استفاده گسترده‌تر باید پلن/افزونه پولی تهیه شود.
🤖
حالت Agent هم دارد؟ بله!
دارای دو نوع Agent است:
• Super Agents برای انجام کارهای چندمرحله‌ای، تحقیق، کار با اطلاعات
Workspace و اجرای workflow ها
• Autopilot Agents برای انجام خودکار اقدامات بر اساس trigger و شرایط مشخص
💡
علاوه بر چت معمولی، Brain می‌تواند روی فایل‌ها و اطلاعات Workspace کار کند، جست‌وجو و تحقیق انجام دهد و حتی Task، Doc، گزارش، اسلاید و موارد دیگر ایجاد کند.
🔗
لینک وب سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qecZgV1AlNwZbBoYodMItyB7Sb3nh_eYiHvqq8aYSJO3ct4Rk5c3SPIbZUn-DpsghvFEYOQflvg7KG2Fymr54prwAQlq3HD4vNf7cC2IRdUSLoN5XRavoSiKdlrL6HgxG1WRkC15ad2eHt-ADbWlDazSUWQu3D6E2_lbHy3CYRoH06PkcbwVNOWIlwyy8C_K8TisGBi53bxq3gPATxP_YKYC0bsXKhXyMzKe3frJADLTl0n_i4xYWcCcQD4u9rTbtftsVYmTHlUn_0Rm2DRFmkJ3GaLAzCnnqskoptPzyk5v1CTvUSeE5NiDNrRPSZByPqeSHsykDzMVcVi4UjYZFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی
🚀
🆓
Opus 5 | Grok 4.6 | Deepseek V4 Flash
✅
برید تو سایت زیر ثبت نام کنید و موقع گرفتن api باید گروه Free رو انتخاب کنید از این گروه این سه مدل بالا رو تست کردم جواب دادن ، بقیه چیزای خوبش کار نکردن این مدل ها رایگان هستن و کریدیت نمی‌خوان
✅
📌
Base URL :
https://kiosapi.com/v1
اینم کلید خودمه اگه دوست داشتید میتونید تست کنید ریت لیمیتش رو نمیدونم
📌
Keys :
sk-ZoCd9hc91if9INutCoTC6zA0wJ2pbrd9a75GQJTyj5V4gIup
🔗
https://kiosapi.com
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXkaDRFHosmoquirQHs5aGV94pWca2r_mfL87EmeVHgrzRe0iem7CWaN4FVJNeIMnT67pgyyofyoWEDpV6suOnkXuGOsCyaEocq99beozJ2BZr8UVn-5BfzrugYtRAQl3T5mUsd8QycHUgGyTcX5UowMtQ_TKnKdquLNgECD4mfKb6KC63vvEB_fEyK2eXmbvov5OPy8CgzpBbJeaVx9eMWDIsDsWFJkeqZcereWTNYtwdWRIkqXQIYG-J-D6I3yCP8U0GO5F6NoAr838EIKNM_t0HJy6j-Ds9hoPLr4MZ9CW9n3YRPSdAVGNMonHuGZYubkh1x7W03twez3uKg_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5000
دلار
😎
📌
Base URL :
https://vip.9aws.net/v1
📌
Keys : sk-faNuu4uK9WqIYAiXjdmYxeX6PI1Z5wNLzCsIXKbKVQ67W1rG
📌
Model ID : claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRizqnRI9mABQi4bO2GfcezMtG0J7clC2vIteeNMdWnlO2bGCnHHQ0W9yxiulD-oBhRLfNZB0Ac3s0gpIzsSptPLKr8JkuuKa8XJVm50AX73cScusimNbFBooaNEORSa8QTCaGBkWA1oZVIz-9KwQztsLY8m64DITD8q6qr6Fb2DF5a6MS6BbsWyOBSRB7r0zJPLrjhgc5xqS8_KZ3l_jR3nu5wNj3RWzYjq-25ujXuX6QdpBYeQGwf3VRT55nJD1Lh0SLTUtx4KUdp26D7tUFUFmZVAWwGjnDPyqUqD_UF6E4PQ0t48GY1ILRVedG7zs1mqkyV6xp4ZYR7Qe09r-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت وبسایت ۱۰۰٪ رایگان، فقط با یک کلیک!
​سایت شخصی یا پورتفولیو می‌خوای اما حوصله خرید هاست و دردسر کانفیگ رو نداری؟ این پلتفرم اوپن‌سورس رو دقیقاً برای همین ساختم.
​
🔥
چرا ZeroWeb؟
​
💰
بدون هزینه هاست: کاملاً رایگان و مادام‌العمر روی سرورهای کلودفلر.
​
🤖
مدیریت با تلگرام: پیام‌های فرم تماس سایت مستقیم میاد تو تلگرامت و همونجا جواب میدی میاد تو سایت.
​
⚡️
نصب با یک کلیک: فقط روی deploy.bat دابل‌کلیک کن، تو ۱ دقیقه سایتت بالاست.
​کدها و آموزش کاملش رو تو گیت‌هاب گذاشتم. همین الان دانلود کن و سایتت رو بساز
👇
​
🔗
https://github.com/faithsaly5-stack/ZeroWeb
​
⭐️
خوشتون اومد استار بدین
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPKuo3bdM2ogjuU9i7xgGOwJyzCXMpWtrwoLhaTjUdDn-hiO3QlOEfuaVp8_zX0em_u_8EuDLH3V-LXfwm0kyaPpMP4omifIVZLAxnmU3COhPcoQOGfOGfjzYhr4KBqHPkQUKizPmv0AyGJS4SQVJy2uvaXeAwNT6HFPt5z-Nl6oEBJ744PZeaGXXjPehihik9i4manz2Xz3cGS4S7ocFK_9RK_ZWbjT87FS9jim7sy3R7Sk5_8P1-w-5Vk2WvnKfwLi7ihJxecNMF_vEeiwiOFpd1Y7Qe5ewwo7tk9oGH9oNlvx21BrD11F-B0jQWDDBZboMtAW04XoMJQ4KQCdAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت z.ai کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه: ۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan: هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIVqPvxotkD_r43PRQLXQqvWOX3_0f2yCdAwUOJyjfQcWzUzCjYqOrx_kLOYwRB8kvxXS8LATkdg_CgvmKbWQ9ZHypQ02Ml8wziW8ePLsEC3FoxIJzgTS8gpYK1RUWGCJJAWjzx2oyTZukVlYFHpGWu5QlwwKTJhKNJDhN03_T945be2h-ifE_ggJ6enXDhGjo0n0-oSXjWH-lrPyRBvgL94O65yp-tnmnpllFP-LW78EA-FERpUl-Uwv5Gxwe3-lRxJVS41Eo0ZlSExdeU3pwK1KZ64WhXYiuV4OoDThbzhZ1U9FSDU8jMTMnZlQbFls6rfD9VTzqieRfVmU9pSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1,000 دلار
😎
💵
📌
Keys :
sk-ByTi6xCfB7Pt1N8Hp9z7VdsRwGIMM5pdnh4CsorUfflysvbq
📌
Base URL :
https://tabitoken.com/v1
📌
Model ID :
claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_nnyWjWt1MjBdG80TjR94343qedGz2tI8iOmrIlSZkcLd2-8sl0Eh4jqg7RtC6EvAiqlzK7ijnbzMc77nJLiuCW-jzRQBCA89O6rSuGaS_mUXUMO91ciCzy4FU8Ghvn14hxNmjN9VN8mFsvXNE0K7zkoU3Vdk7PpMKS2S-sXQ41EcoJFp4j9ooeNd8ByUBCfaRbhu4kJczXOsw1t3376aYP84t-8IGKIttDaE3IaCn0rEWEovDbzRLjhGjgtr0pwJVBd_uKX46CdygJoyNWOqtCjuLghaKuyeFsCPg7jse7l5gHOfYZBxGgZzM_9E3zPSxDk5rfmQJNsvDl6OcSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY9iRMn9HJnScTAB-l-3xlj_eQ6iHtGsB1L0NA3J7iAbZDHYSUJJF-n-_zTJVRauoj5ozegTLpMGbafz-vccv582Ws7_T3cglH3rnZsD_6ttKQCWrd3jrnS4ubSwzv45X9qjFbhiUcQXYDud7Q5hK4DN4pkGH-yfD5Q4AYwE5q8bJqyNmktcQuU_ihgwZnhqIXPmjKT691owZjJ6zOS3IVIEfaGk_2QuNZA0ktQJZNSBNpIZnaT8zn0r1gshFzOcR6DHL5-zaLEjqtH2zPw7ZkPSUjakM_LIXF2lsW1TRnfvYKgZNb9i8YhMZ4M-_TkkpmqrgXxN50A79L7JYJglFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم به دلایل نامعلومی میاد API مدل های Fable 5.1 و GPT 6 Astra رو میده ایشالا که خیره
📌
Base URL :
https://api.experientiallabs.ai/v1
ماهانه 5 دلار میده و همچنین فکرکنم Fable و Astra کلا رایگانه
تست کردم اوکی بود
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhhR0hlh-hwrrn9nIsPFz7Y28wJ0jTghZ_XbZWqMwNYgWoo5jhaaL5LnkJGR_ExsF5EdDR_MwHUwW92lw5VJKhrshM21bXrrW4Bbeg8WE5c1yEYmtKrbMLWgO65El8zPXswjNvS4SJoyoybweCoFeSZjqcvsabmLwG42RVB_eo3Tzk-37s0ZCHiOJXw1KZdTHS7QWbfjj-JM1WxE37bKA7khkZkQlK_XG6YiCj5BDVxwBWCtDkB4c2e-SHsiZNL8hyuLNibWYEvt4oU3e0fiMFcHg_qNc7cPK3uLLBUYeHrYUZs_8WcUPUkZBpUiAmHCsu16U_8PFprzUVqCfTFGZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=XneapucYZUWOKu5fG9gyn05BEgw4pZButeePCgFfA_vKcOb3N5jT7eVSVngMetGb1yz3VFYWG1D7YE1qC7kkVUXbXGBOeyob96lUWPlD_EqV7IdJaPSLf81HjjTHYHfb95Kq5lQ9dJRQZegRMDxBzm1jT58qlzdvjslbxhl_eJxQz3PwbY2yGeDUatA_gbrDh_Hn3svI0ACjzzH_1Wc8STlqEEY5KiBwgAL5b8PN4Jme-u9VQhyizsm3PVJoaPDtjRJu3h3XOatGonl5JJZiuVkcVKGUbCUc1gVOPvqWZQ9crDxGEbLpqpw54WmqKJSu0tGFuic4FR5bAFNKA6-oRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=XneapucYZUWOKu5fG9gyn05BEgw4pZButeePCgFfA_vKcOb3N5jT7eVSVngMetGb1yz3VFYWG1D7YE1qC7kkVUXbXGBOeyob96lUWPlD_EqV7IdJaPSLf81HjjTHYHfb95Kq5lQ9dJRQZegRMDxBzm1jT58qlzdvjslbxhl_eJxQz3PwbY2yGeDUatA_gbrDh_Hn3svI0ACjzzH_1Wc8STlqEEY5KiBwgAL5b8PN4Jme-u9VQhyizsm3PVJoaPDtjRJu3h3XOatGonl5JJZiuVkcVKGUbCUc1gVOPvqWZQ9crDxGEbLpqpw54WmqKJSu0tGFuic4FR5bAFNKA6-oRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی حالا می‌تونه با YouTube کار کنه!
یک قابلیت جدید به نام youtube-skills به ایجنت‌های هوش مصنوعی اجازه می‌ده فراتر از باز کردن ساده‌ی ویدیوها، مستقیماً با محتوای YouTube کار کنن.
🤖
🚀
قابلیت‌های اصلی:
🔺
استخراج ترنسکریپت کامل ویدیو همراه با تایم‌کدهای دقیق
🔺
جست‌وجوی ویدیو بر اساس موضوع و پیمایش کانال‌ها
🔺
دسترسی به ویدیوهای جدید و محتوای پلی‌لیست‌ها
🔺
دانلود زیرنویس‌ها
🔺
پردازش گسترده‌ی محتوا؛ از جمع‌آوری ترنسکریپت‌های یک کانال یا پلی‌لیست گرفته تا تحلیل چندین ویدیو
🔺
امکان انجام تحقیقات عمیق با بررسی هم‌زمان چند ویدیو درباره یک موضوع
📊
یعنی ایجنت می‌تونه ویدیوهای مختلف رو جمع‌آوری کنه، متن اون‌ها رو استخراج کنه و برای تحقیق و تحلیل از محتوای YouTube استفاده کنه.
⚡️
مناسب برای ساخت AI Agent، تحقیق، جمع‌آوری اطلاعات و تحلیل خودکار محتوای YouTube.
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6ahAH90Uiqi8VriMymEm5SMcCFUNH6H9kIcInTbRml0q02jXn0UHEjnU3of7n7-C4SCpa72eu8HRrwJmT2vi79BQIo8hU4XfsnqN75B3_BZpigICCfGsDO1VKBGnhkyw2s8fr-kyUGM1ZybBJ16Wlc0Y2hNetmKqv4ZhZECoF0VGSEa-in16be107GJuyoC7EKdioUpYHI_gziRRqq3aXln-M-v748WsQI8G3q-V1kEhtHb8Y3JMSFgrIWfGouNKpR7ys0VEZ2Qm1bCafzkdxkImrTJe5uHaMdjXe32GHtMoT8GbaP4-SyQgRW0Dy57tfn-z8emy30s0lXzYbPuew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 دلار برای دسترسی به مدل‌های هوش مصنوعی محبوب
💥
🆓
Kimi K3 | Deepseek V4 Pro | Deepseek V4 Flash | Sonnet 4.6 | Haiku 4.5 | GPT OSS 120B
✅
کافیه با جیمیل ثبت نام کنید و یک کلید API دریافت کنید تا 100 دلار دریافت کنید
✅
📌
Base URL :
https://api.you.com/v1
📌
Example Model ID :
kimi-k3
حالا برید بخش تکمیل پروفایل و یک ایمیل با دامنه ناشناخته وارد کنید
مثلا تمپ میل
سپس 100 دلار اضافه دریافت کنید
😎
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎯
چالشی بزرگ برای وایب کدر ها به همراه جایزه
اون لحظه‌ای که به یه دایره چرخان خیره شدی و منتظر جواب هوش مصنوعی موندی؟ Commons میگه این وضعیت روزانه
۳۰ میلیون ساعت
از وقت آدم‌ها رو می‌بلعه و حالا با پول جدی می‌خواد حلش کنه.
😎
💵
🎮
چالش چیه؟
به‌جای یه پروژه‌ی کلی «چیزی با AI بساز»، این‌بار هدف مشخصه: زمان انتظار برای پاسخ هوش مصنوعی رو به یه تجربه‌ی سرگرم‌کننده تبدیل کن. یه بازی کوچیک، یه تجسم تعاملی، یا هر ایده‌ی تازه‌ای که به ذهنت می‌رسه.
🚀
⚖️
داوری روی زیبایی کد نیست؛ روی کیفیت خود تجربه‌ی انتظار، اصالت ایده، ارتباطش با AI، قابلیت استفاده‌ی دوباره و کیفیت اجرا تمرکز داره.
💰
جوایز:
🥇
نفر اول → 20000$
🥈
نفر دوم → 8000$
🥉
نفر سوم → 4000$
🏅
رتبه‌های ۴ تا ۱۹ → هرکدوم 500$
🔐
+ 20000$ جدا برای بخش ویژه
📌
مراحل شرکت:
ثبت‌نام تو
commonsmade.com
← بخش Hackathons ← Join the hackathon ← ساخت پروژه تو بخش Code ← وقتی آماده شد Publish کن و تو Hackathons ارسالش کن
✅
🗓
مهلت: ۱۷ سپتامبر | کاملا رایگان
اگه مدت‌هاست دنبال بهونه‌ای برای یه پروژه‌ی وایب کدینگ بودی، این هم خلاصه‌ی مشخص داره، هم جای خالی تو نمونه‌کارت رو پر می‌کنه، هم یه جایزه‌ی جدیه
✨
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
