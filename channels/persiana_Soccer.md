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
<img src="https://cdn4.telesco.pe/file/Sj_AD5fqWsUfV7kg6KEA1B7cVyu8TYJ1u2kzHAU9h8ok4dRLkLTBW05a0r5ogGRzP_aZpEpDGK74TpFvjoHxrUHwUulemIxpci3uQ-b7uIX_1VerRCoaeCw1C-m0FSby-sld5P8ugtBMSRygfovWr8oqNGcx2DGL66u_P0rUSUxN2CrK3Hu9OcYxocAeXVNXQiwpEP0b060Ri6RGLCDXFyKy-FZAufaGhygqcaJA7cbOGEjYFxzx3uJveC40SuqLctIiCsepB7CqKHOdPykp_-4ebG3QV6kaxr4PFQ0bKdj8DsWvpjF3IA5N1DW-2CRd5bKkyKQZ-q6OrIXKkdhEJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 520K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 17:28:51</div>
<hr>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=lT0YDGn_xlfO1OZ36EUffmxWyZrlKpomz0m_Uk_sodQURdsShFfEhyGeQ42SX3j6d9QFdCW0MwOPknPQMBCwfoONKJ_jqZSSc046cZ8HmKWbFxFuBn5DeQ6lQEx0Y01M1_I4gYrioDfHHPGL3TSwPjxVN1KT5X7pbbmAWX5jpNBRcJPj_n9ZUFLfxHEPqAK9dPMX8tVL6Nl_z3z2DXzuMRiHUPt7s60l5ltCzHiOPGpJl2Hd-TLP8ZMM9tEFludgxWV7QWO9mCHjYF_R-5c6RSPy33NhkXXVjH9lOLrnnXY4pq9Ad_iY7ui4yCNdi4crSu6C18VPE2DXaokuQ0ai5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=lT0YDGn_xlfO1OZ36EUffmxWyZrlKpomz0m_Uk_sodQURdsShFfEhyGeQ42SX3j6d9QFdCW0MwOPknPQMBCwfoONKJ_jqZSSc046cZ8HmKWbFxFuBn5DeQ6lQEx0Y01M1_I4gYrioDfHHPGL3TSwPjxVN1KT5X7pbbmAWX5jpNBRcJPj_n9ZUFLfxHEPqAK9dPMX8tVL6Nl_z3z2DXzuMRiHUPt7s60l5ltCzHiOPGpJl2Hd-TLP8ZMM9tEFludgxWV7QWO9mCHjYF_R-5c6RSPy33NhkXXVjH9lOLrnnXY4pq9Ad_iY7ui4yCNdi4crSu6C18VPE2DXaokuQ0ai5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saNzXnbGmNQ1_FYjqjtJ0BqrujAO9h0E9P6obtW7Tuxmr9Y_93oJBqjBYIZqi5NYs4hukGzCVXDG7xyYXpBfJRvABknDaazsm7_FIdTc0vee6NMhPIZecGHC_Zhv_hZaGBb_wn-801WYfujSWoyn_JJ2gKRLtUSogXra0iPWbM5cJIifrIhJO1NYw4rnEty8m9FkBcHVCgVAP9tcnZuGZglsNCI7Ja_riVYR1UxxVDIkUISTpxzMLVD9CwBKxw8z-AxG6DX8r_ksKkAtLg9Qwb8g3qNDKTei-VnsKSmWLY8C0Iksx0RMb0bsXuiQkahdw3KJXKIDNyogcbHF6cIltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=GgYX328VjNcyNHlso10Jrh2K5p_vNcqLHr9rQZkM2KpvKx1taGF8xouLHa7Q1vY3fU4urfL4inDhXdniVkO98EQysSmQzumvHf469RdwEmtJmVzFMB_yLf2ReeuuaQrj-q598mxyGcuj5wUtWzMUGND2qa1COA-HAtnlzCU8OiW_fj9bJD7Ra8VELIeHx0DvR3hPL64GNlqojdhG9UC_89xEMoMIGO-NtR3BL2h7jQJw0ER9QHDMoSVlBHNU9a0G3qCJ_Ano6P3MwbvT90Xex0KoELueO1q_J9ZCzltDIVWMkEZcraxvhd2gDzmR9YR7a25Ldt3yudIV12gjzJ833Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=GgYX328VjNcyNHlso10Jrh2K5p_vNcqLHr9rQZkM2KpvKx1taGF8xouLHa7Q1vY3fU4urfL4inDhXdniVkO98EQysSmQzumvHf469RdwEmtJmVzFMB_yLf2ReeuuaQrj-q598mxyGcuj5wUtWzMUGND2qa1COA-HAtnlzCU8OiW_fj9bJD7Ra8VELIeHx0DvR3hPL64GNlqojdhG9UC_89xEMoMIGO-NtR3BL2h7jQJw0ER9QHDMoSVlBHNU9a0G3qCJ_Ano6P3MwbvT90Xex0KoELueO1q_J9ZCzltDIVWMkEZcraxvhd2gDzmR9YR7a25Ldt3yudIV12gjzJ833Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه دنیای فوتبال را رقم زده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbXs2GOh2ibErFv4_YS6Gykk5srqRZ9JMbdhVh-0Oh6l84R5Z3n-F7R2hfsUhsNnd418scIaSAAt4JWZZq4am2V13-ygX-fzBnF6XauTlPbcyEyCXRHcFf60vOJRjeYYP_YuKwETVfHovpXEPeLYswuoG0nUX9iDBvPLJpsF6CFsCJBcFAhLYuBijzQykF3rlisXBKxHxUogMA9w3UoyMyZlePgfcnKXTkZ6O-_dz8dL7rMHpJmD99Ar7zLP5sI5VDlkZ19niet1AWjX-jsYB378gQ7lwd0hDGAsc7bTBt3XfOSToathMAayzY8m56wczDD3eNc6sygu1EeDmY8lqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26061">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBPVkw31S_J18a8Caj4jal6VRc_krjCjDby2HLeQHiUgY16RvBdwM8iSmY_Gg2farZ3KH6irP69mbQOmcFs3pauzkrfUmr9oPpL_VRCa7RrlblJdYtsUwUkbx8CcbxNWirWrSpob-1SB7NrCr-ev7KqCx3d4mbUdHI4Y_2bcOnZo93hcIOfHAzKrSG0JKe1anfuL9T409a5QBcZhiX8xAT7VcHAHSw2JDOJXEWV35iCU-1vbMXXGnGUud3hH7jRW--2fI8kx_F7FgSgqjoxeni67AfabhWXhJwhxOLDxVrp5Cea9f-qk3IZSV82cnxyP_CnwblHX-CEoOTq3W1TzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق‌ اخبار دریافتی رسانه پرشیانا؛
به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/26061" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26060">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVad5Z_WeYnMQaLn4zvEE13xYJt8pFaTUBOPQw6CEIMSfK9PArRyYjGdCjISHAou9lfF7HlVXfpubt6xxaRljMUbrVUC12CcXfFDkhQ2zNxoo-jO95ZCCXL7b-TFo9O_dkB3O4c--n_qZXCQFji1-FBj19sWC4wGjkT9PkKqB17AQXrYB4CAGYvp7Fvls7PEHL7E3ZxC1pMYgiDt4KrR3AWIhi0Z6wqyv6ew61p5HzqTsZDIx5XzTvsBS7F0L8Y54vFteWRcS6_7MfX0NpY1yiRWhdTzHNqzqo_BnwjnV_kgGSLrdRQUfbQoFTd9uF0SXg-ZeKcYzPdAwoSmXI1ujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/26060" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=KsnVmmlDN7pefmXoO_DZUOIclmRKzIm0MvJMh9O4Wb-kRx9Co8o6ZFL_hpRV5fbb3DWRBVEh9In1PkwlMJh2TxJfIj0tzi8lckNV9ivTcQssYnBNpvfr1HBJBg5J1J2haPkNw-yBh_KLWOgKSHywi7qbIuKhI_utfAjbHzIi9VMuAEreKBxtC6jDZiXWWSLcuX3hD7T6FtdljYh8DVnLJ6X8npTfRcTU3w54zMpRFQwXMM6-bfy_2w9nygX5GdvCpdl2Gvi9Oz-3GJHTYHRnOnpS0dxOYbK23ZeAm68VJbneQGm0fYFACpgagHzhLNn5Jx99wpBUaF8HFL9tn96BVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=KsnVmmlDN7pefmXoO_DZUOIclmRKzIm0MvJMh9O4Wb-kRx9Co8o6ZFL_hpRV5fbb3DWRBVEh9In1PkwlMJh2TxJfIj0tzi8lckNV9ivTcQssYnBNpvfr1HBJBg5J1J2haPkNw-yBh_KLWOgKSHywi7qbIuKhI_utfAjbHzIi9VMuAEreKBxtC6jDZiXWWSLcuX3hD7T6FtdljYh8DVnLJ6X8npTfRcTU3w54zMpRFQwXMM6-bfy_2w9nygX5GdvCpdl2Gvi9Oz-3GJHTYHRnOnpS0dxOYbK23ZeAm68VJbneQGm0fYFACpgagHzhLNn5Jx99wpBUaF8HFL9tn96BVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsg4vBLwJ5e6BSn_QnbOQVUXyyvFSzsuEde9fMWhVvishV0AE7fSUpY0NGBBLH__uXVfKDSvQJ5rnYoQlZk-w0r2euyFNucx4fqdQ4l3hlvbpHnyOP05yG9cOvYOtI4u5F8JAFWvOeTRAXL8A1iSDE9zSJF43riJaAhRYO0WlQ3VRdH9irULGin_teD9SofD47iQWPiT9dtdhK6QAGiZ4jZRijEsc7vA-lS7qCLG4xOJEBiwV_yuL-WCKgBSNTs9DA45kIsjBcaOTyEx2AlRMsNuMGOope6xCE6KXPLuici7QpN1ynQyjEdFmuaXI6UYnCeHS7nx0XVBfzXMu_NuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ99USyvGhOYA53cANt1qJDNkOFRmNL2Ot-xEQiFVlnzuUXeSZvH5MJlOwU2-zTZFvUgldlznWJ2nbMldCizAzvuOuucaLVe8RBc5KmOOHi34jdK1vXKiWu27pdLeQ-LLeN6lEp2irA6IMQZ4utzqT7DvV8G1jXMTaM8pWbTGLbjs8eV_-NbeE7KP-wKwGac0aZC2eDXiSKyDgQBKPsyjrwWEVdqpUMNlQw0uDNEUlKPa1w_r3oThUmsxFtShR2qX06WynxsHSS9He8ubtPitcjAutPtE7hDiByeEzTYwupH7jUVcxJrN9Fz3dXU_0Kui0KMwK7Nf6z7lIFU8Tf3fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=BqRGnoqGZSi6Ie1mqy_t5dp3BV2HfaYlDo8vg9pNzGKEFTrKsUq2Cw2ppXYXXMxx6u2_2qGFK6uMSZwiyKFSDRJPholbc_V4J0IS7n5tLzJuvz3TS04F6d40d7K8hsLXATb7ldM5e6Ow0m_FOZlgNjg7gKzL7nNO1VOMHmLkfqfbAY8ENNxGSOe4OeCKk4bvFN9R4yzHrIIJvW1nyMxD17SpMmw-fmQU1nMp-TDw1ub30C-uKP7bp1ZnVFoPs-GgNojAWhyGvgZ6xlxiNCL6xjrEqUftsrpUWV9cHKhJLvdhuC--i0aeAoHvaQhsKrWnNwfLAbOXcHG5f2or8odcrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=BqRGnoqGZSi6Ie1mqy_t5dp3BV2HfaYlDo8vg9pNzGKEFTrKsUq2Cw2ppXYXXMxx6u2_2qGFK6uMSZwiyKFSDRJPholbc_V4J0IS7n5tLzJuvz3TS04F6d40d7K8hsLXATb7ldM5e6Ow0m_FOZlgNjg7gKzL7nNO1VOMHmLkfqfbAY8ENNxGSOe4OeCKk4bvFN9R4yzHrIIJvW1nyMxD17SpMmw-fmQU1nMp-TDw1ub30C-uKP7bp1ZnVFoPs-GgNojAWhyGvgZ6xlxiNCL6xjrEqUftsrpUWV9cHKhJLvdhuC--i0aeAoHvaQhsKrWnNwfLAbOXcHG5f2or8odcrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26055">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=RVC7KAltG8p05jvopIuBwXUZAUfMqxPGbnhgfQw8UTiTwkZ_bKsJ4BW_F5mOcqUFy0LvO2mmaeu1_xNqX3LBP6hrOoW1X2yyf71gjveVOSVPWSE37P8K7D-MP5J5DabeBBToDJeWoee0gBgweYHOeMj_FXVloBNNKrMx8zJhpQzlAelJgklmfK3qpN_Gm5dOqzP-fVHzypv06_yfa9r9pR6_cD4FqFPJ6wIh6-VtnPvughDdyQDYsUHpdEemsUxoeGrepUKXVToZ6kLkwG58Z_QQMAnz1LJ_JWC4Fgw5Sr1XvhkTSA9fwJuOx2_bqLYP4V0tsYOtzcyfJWCImeQFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=RVC7KAltG8p05jvopIuBwXUZAUfMqxPGbnhgfQw8UTiTwkZ_bKsJ4BW_F5mOcqUFy0LvO2mmaeu1_xNqX3LBP6hrOoW1X2yyf71gjveVOSVPWSE37P8K7D-MP5J5DabeBBToDJeWoee0gBgweYHOeMj_FXVloBNNKrMx8zJhpQzlAelJgklmfK3qpN_Gm5dOqzP-fVHzypv06_yfa9r9pR6_cD4FqFPJ6wIh6-VtnPvughDdyQDYsUHpdEemsUxoeGrepUKXVToZ6kLkwG58Z_QQMAnz1LJ_JWC4Fgw5Sr1XvhkTSA9fwJuOx2_bqLYP4V0tsYOtzcyfJWCImeQFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پله همیشه می‌گفت زیباترین گل زندگیش رو در ۲ اوت ۱۹۵۹ مقابل تیم‌یوونتوس زده! اما از اون مسابقه هیچ گونه فیلمی وجود نداشت. حالا گوگل با همکاری خانواده پله و با استفاده از Google DeepMind، فیلم این گل رو ساخته. این ویدئو، فیلم واقعی اون گل‌نیست؛ بلکه‌بازسازی‌مبتنی برAI و اسناد تاریخیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/26055" target="_blank">📅 14:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKJxFdbnyJ6dupTscX09lgsmAFZEkA1_uD-_Z9x9jjQEdC7b_kZmSYz4eH4-3e7mcdxsfuBAeQKEzzxtk0SwULlZVOpX0K82IPwlrL1hkCZn45CaKp0Iofb12-xdLUjKGekom3KVSlI90c9DK065Mzcqxn6ze2ecE-Wctg4SFmV-9kMEJBFkzvxFbYbmqkpMajhoVfcWQNBAhErB011nRHzPcjP2uQP7H6VT_IW8C-D9-XDHf_xvOOS5029jawh7nsxvcrC82h7iITZ0Nw0n9b1fzqgMljt1H-DIS4-_d9dS5-ccAFDN-rEeWCAoBZfWThgSig0HiMDBTpKWh1elfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKSvU9_f7j-XSaEso_a6Lw2QIu1ksAm4AIIc3E13AEQ3QUWMA7sIavj_NvwYZPm9AnwlZ5yavOhjrL3FEVoacRCtGnnb6Ib-ikXzlP-EIOeXCnhpVn__fcgFWfU8pqBWskiembmExN4V98a4zm9nqvbcZwQCpqURgeWbPsuYCWtc_H_0suLIhCHPcCcdlRa3TcDAnaiv-aW6blESvKU6Usw6InwNSL0Koeoiy2mVz7T94xJOV8k-kND1LwU32Vd7ZZvlhVZQxx-nqSTR0xwu-yuChx-YvmHP_tlQlGMuQOL5eiA7T4xNbMvq7lnOMpfpEqHAn6yw0DrIB_4S4DUDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26052">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vq38ZDOVgkN3f8VwVkE8rOZX01pajxaN53NJ0tNwkwY3EMKu7eQPpSXQDNyMfHLCc8PtFK2WeiJhMBJMh5LrsjwhwMRtCJDGEimyQTqamNTGVvf7XLuQoAHw4yKjuGxhIveAg_i3qUwsQmBvmfznKc74f38iKyoeQwZT60X5YjEZZk6IFtJAhYrYEXIBSRX9_nLfVlicL-QLvaJnXQYWaZ641K2MIXa4s4kOWfrc3LyN8CUhEImRkJPG_z1VAyjrXtR3OaujuyGxsShCjCCQovQPrO1JomNyT3HhVOGJXzGzY8JOYEhL1zZlXgqnYTn8y0ivadxnYVYedwhuUCdknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/26052" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26051">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpNbmGRMPp9tbNVKh8MpMqJqKs0Rk1VE30SaHFIx_FqjpCrVQ_rYbI-gZG3WOjqKff7CUYKuxRSCRZ3-D9TyimMzULDBPVsPApxhRjFLxNt7a0yC1dMgMfiUqCq7PcqiVkuTaUiJ6ZF1EhAH4TcNmoVOkFUjT8LwVMHVIE1jetLemMuyGt9u2okDkU3WQN6qZaHp6vb77foKD_HUp99cu6mU8bus8MYQsr8ReXG5GKXMFlrWs3w2xUTso3-MAax3XybtTxmoYGv6O4w7fV7JnRYRpKdARpveL2X5_IEvBRI2SQuWdXJ3qu1_qYqf30049eg_VqiiVhMJ4dv5kTfDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26051" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26050">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwB29TmiLX5uvyVLK-QwKSpLlNdnaBbu1VI8I4HTI7zUCu8yw8w5Vqm3nyLzuibja99by4ZyUcaXDevhyEqPqfiMOIF5YGd5Sl8_BT0Dnn65qEZH6nToOmvX7mji0qFEFPDe7FwjyBkqmrltJXR86e5Dr2RGdVW0c2un7i-CHUbseXhIm6AZ4qET5MBx8yb4-ET9wT-P0M_EuUDys98bRQJ1xY8UizMacj6mfQ40Pbda2ghd6BXdhgZdwtJGcjiRUkS5FBW2ZZHaBmS4otttZUZpPdL9jiYoqzAC5Ev-SDkqqwosWZkMpv4WLaWs6JeMR4WtXjhZbR3NrWSoeuQHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26050" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26049">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2h1Tzb1kgSK72MLoVWFIpLMQ81uPwLRWsyx7lCUu3ka2urr8WCmoOH8dWVtlFFSTcyUdriwisLZT5wxY5Dyo1smPPteUGqmrJdGqiYQjp1FKYAdfbGAuFjYV_WV2zkPmUvPsQrCYOHE0OOBDIA3pMYmO3LYjcs2r5gopZas_VocuZgblwFW7Br2EdMTazRr5ncjbEH2fIQNEiiSAcm5Jh6Az-WleKOMNavxa7s0q1a2mytlgHMDMifjluJ5_MBB0OyZgoGg_Byt0SZ31eULY5shuN1PWRuMgaGbbl0N8brj_PHFLQtemilPFk4WL0FEA3yVbMUIomm-qOD5nOoKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کلارنس سیدورف اسطوره‌باشگاه‌آث‌میلان و رئال مادرید درکنار همسر ایرانی خود؛ سیدورف فصل قبل بعنوان مشاورمدیرعامل آبی‌ها 250 هزار دلار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26049" target="_blank">📅 11:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26048">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrUmBL0OI08C6JYdLdjE1p2ZTzItOdFZ68CHa0glmIuRsh0EewschSOAhk5Miv0aKTX9ZLlIt32ojsmpmzBgthXZygXzAQweeoFcSeeN3K-51FhP6IZd6TwngBT-UNHVtHhuEvO9vi3EYrS93hxBdOv7REConUjZZqOOt0voSqI4dr_Ba6zm8eUEbj_knWZVzRlvIgjMrR4g507vTlMv_SwwT4wKCYpVQgpWA--H9xEKtlY9Gxmj80MReg7lyyGCAZmlnv5ceIsX6S9q9XPJ0_7ozwmkNPPgvTPCRoGIqWBMLFvGMrm8koxl4RUvRYT2xafNcta2aT6FoAwLBIBusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26048" target="_blank">📅 11:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26047">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nApOFO_sYBbSFk_Pva2Q4q7gwvAAYI9OyV0x3qbYPJqgT8Ps6wT1lNSTQYg45fCXUSCz21s6MTYF80hPHEaA5f8vEMRUdqhwngRynlP8N0l9mn9UqI1jrdwsTG9zafDbQXhzhtEzaWTyoqfxJgjrNvwCr0MeV3kBXf89BJXjX8K76v0UOvONPOfGi-kdmKBKn_05jhuRU26p3zh_pxEoA8TM1hLQCPYzltZezoPrqoIyxNPgSgbWPNlSogriC7JoRXodoFi0bq4i3GUSlgsj-2DHMyicKlQE7dcsIpWUR6RFPwTVTMo4_WdgKRBwZQcuHy2lYZVuynQg5B2qPJhcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26047" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26046">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYNoVGU2_YBIlp7PBA8RLt8p1lE26kXSsLAcywSRjA0luwxfprcjuWNM_-oCkqHN5LHiIvFMYLHyPjuA_uuHYTL6NCYQXZ_B7WTTjX_m7TIDcrBDW2bgUfFaPpyg5rDN_JZEeb_E1UMzhbyKyWDh4rDMIIno2VTEM971aOpDf4fdC8VWGhbivZbZEFmltNtjMabfoWSXF_3vaRc6HYL-CFRLxqVRw5wbQd0jvE83LD_rcidsXytUFV0zamTarnPq9Gh6PXYZ7E2uF3RZPekS6NN7KFYBXX-4RbbZUH5sZH5lf5pcUbnwKYCK98FEF15yVemaBrWXt-z9O1MzcO9MkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26046" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26045">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgFaoQX9ImNhn9TSi1O-GFrLWQK5hSqwSbOjps3a_J5aVUIE4tyq9SMrWQtHFDKUOA8E-L7NNAf75AA2TMNRcJZtrEL5KJIiFot8zS8LUQnoHzLlMrC0E5B2ei8A_obUpsce-kbdzXpkzgoR2jehYyIpcivKMYjSkRRpGOijoufasTxZXn27w21oQdigqDQMKy1WyhRmJ0mtP20of1wXWwB_PFTt52cfAi57i0X6OtlU_2Me4JOCelWl16ip87-7aM0LQmLpTgtR6MxhZ9nRhMOO5fcBB-dpTOGAIaNyWHX2Bq7atXw2xNVT_EOPcsg8n0tStSWNpWi5EaeOJlB89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/26045" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26044">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">📹
ویدیوجدیدوبرگ‌ریزون‌میلادکرمی بلاگر معروف و محبوب ایلامی و ببینید. رفته رو پل B1 کرج!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26044" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26043">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2k6inj52MHQE0E4qqpkQyDFXLTIMtc4Nb3AfM6YA2q1ztjgeLRQRcJ454zA7un74k_jAMULHpwDun6x-xmyVJg_4tMRl7EtWICnLF1vQxmmWwyAF7rESatGVIhI4vHBt5IX8Vu0uqKa2xX11faQSjbiAdxB_nCdoy2w8_0q-S7m0m8UXuLs8vwfQzOQjRogOJPI2ImILH61ni6Sx7Pr_A8pzZigaYdgRQHRzaP-eQt7OuUR5rRvd1omKp_iZ1Kjjb6ReowN9cgEul6k9gcP3DFy9gxRU0_NWruY7YlDb9lX7JcWkYIQUa47OnfjsKu91-ty1a5nw6ggKOLRAWs5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
برای اولین بار در ایران ، فری بت
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎁
💰
سوپر بونوس
وینرو
، پیشبینی بازی فینال جام جهانی با بیمه ی
200
درصدی
☄️
⚽️
اسپانیا
🇪🇸
✖️
🇦🇷
آرژانیتن
⏰
امشب ساعت 22:30
🚨
ورزشگاه مت لایف
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr28
📩
@winro_io</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26043" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26042">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26042" target="_blank">📅 09:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26041">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=IgC5NHGSeHMOUQ-Eco8tg2D-YKvAWus2NaZWdudhcvvp931Z_ZeruWpAfbyw5nfzgxfSeq8Z1nALAJUncUpTSz8WWNnoQH85WRvqU3Tk3yNffFsX75tKieYzeum8PYOJwQyyD2upEjFhZ2_XWZ8LrgwVyXiyc7e24keqR_bC61Hl-TPA1Vgrqv7HzWwLylKHt6ih6Qzo94hmpJFsY0DkY69iHHJeOLmXNd4PNPRUowWyKNT64UdHC8IeeaWspIjtUgwzN5FoRO0uo25cfUFwFONuOBMwkqaJ9-fiNbudoCjoQZa8XSyxgpkmp2rEeRE4HqyCaEtNHTEelMRAhDTJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=IgC5NHGSeHMOUQ-Eco8tg2D-YKvAWus2NaZWdudhcvvp931Z_ZeruWpAfbyw5nfzgxfSeq8Z1nALAJUncUpTSz8WWNnoQH85WRvqU3Tk3yNffFsX75tKieYzeum8PYOJwQyyD2upEjFhZ2_XWZ8LrgwVyXiyc7e24keqR_bC61Hl-TPA1Vgrqv7HzWwLylKHt6ih6Qzo94hmpJFsY0DkY69iHHJeOLmXNd4PNPRUowWyKNT64UdHC8IeeaWspIjtUgwzN5FoRO0uo25cfUFwFONuOBMwkqaJ9-fiNbudoCjoQZa8XSyxgpkmp2rEeRE4HqyCaEtNHTEelMRAhDTJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین و پی‌درپی عادل فردوسی پور به امیر قلعه‌نویی سرمربی ایران در برنامه شب گذشته
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26041" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26040">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده و مهیج شب گذشته دو تیم انگلیس - فرانسه در رده‌بندی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26040" target="_blank">📅 08:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26038">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVxzpmbEY6mITACJAKa9qjIk_hVZVBmbbDMuxOTgVyugreOb8Fzrx6-wGQ7IrtwpR_kENLRbdg40JcNCLh6-tNyLtVgDUozGdVzKmHebP7wQ-HP3AtUcsT7QXDSO0l7lxpZuzns5Ilh6HhZSs67lZSakB9Jv_BUUuNJb1B-WIuAAzz8SZuCGiqa5iFu0gL3FShKHur7frnFPdHW34SLajFccUUO10jEv9l4wqhVvLdgwRxvIH2Ri3FuP5r_eAqFuFpCL1KlrRXne11tgiTkjVCOV7YHZHbcmtLdccIbkR1iyi8Ye3jAHkOk4CiTV2NKUGroVLDsm5U1_YtDSpcRDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNdrBDbm0Myt2ESeMUowGqqf6X92OFz1FUvAyLpot6yHthRC-qYjnaFx5qMcQgDkpbLByELA-wtFHUwdPhBTJ2ug_2TmjEN7KTj_JbMXIhCKtnTsKIYcMWeIHsTmiDwXzzxMdmSWAIoMXUOA_SONcEcyt9yiIJ_1qVmv_M2i4z4aVoR9w5cDZv0HZgAmcOlKpQL_lSJgN5y6iGd-QkEpJ4vg5Tc7VdKlmvNGt89WVxti1kdDpDPMrnB3IfG7TcSHJCBvxKtGgUUKDUNBl8yMD_ogDzbD3dBGaVH4oQ4axg2N_K4TkCZHuHJVfoLwHU5Ant5_Tvx9dMzUHAliS52nsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم‌ملی‌انگلیس شب گذشته در دیدار فوق العاده تماشایی بانتیجه6بر4 از سد تیم ملی فرانسه گذشت و رتبه سوم رقابت‌های جام رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26038" target="_blank">📅 08:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26037">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgJyzOhJPCcEm1IAbpWjEHATO4MNqJNHx8iuQxF3xNnVPeRiR2zKXXE_3ykwHVXBdcZkxJZOPed9HahITDYDVLCOdMri4LzZsVLNRxOMZUO6nIrRRjNM_4tpYUn5w39pB6tso_l7iQvczspig3AnCJvLwnX6ADDsjfBKkLF0PkV3kBsM3241Mzdq66ABu6RwlYNxF4x1QTj7y4m4OE2DwB1risllgzOMkfN0mp87ad2qUPd_eL1-D_Ts4xzLjWUOEuh5INHWeofAc0xJAp4EU8jLdSOhQWi2eqk9rjyNpvyRwAZc91oCgifUiuLmSpLCIZDJ9M5ABEnarBpOGtFhiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26037" target="_blank">📅 07:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=YMhxq76v-KjlhNv4YlAZ83075_S9p16IPKbxOnvHzGhDSb5P0iL4_Xyyot2BjRcKa8rj1MJ5pAgyhimXqLL3AwYiDsA24tCaOLXoXmVbQqWcK0C9zw0oPqWRfnAjKs3pMtEYOrlfC70b2-tnnlAihO9L5BTA25yaKpyYQEPYBESsW2aHXb1yY_UFm17-jITOlszcUBE0prC2S4BVkfRNgzYdAKo7Hu9xCY7SB-0A-ysfSMotOjM7KAqgal12DqJehjEkNden9LeElsGqF_Ab1jtjcwhMAuUCVwRDz4dYCWeWPbrZ24nzdkea-g7epMPv2GYszy3szgOKYiXRR5MgZz5PclUl-tKdP6QHfih_-IIM340ZmzqaD-7Ccr6S32CwFUmtNE3LfFKE_CQXUH-iopVib7z3PXLI6PYb7jB-HFJIESbtbRd-WjYLvURDfmnPMiHvt8bWu0Nysi7_mK_B--BZBl4ykF--T8QIs4QCzWbuzY3dtssSliXJBUeoTJJnc5nr20J4bJ5oB70Ax4XYm7Pq7sVES6z1ie6jyNDPbI2WcCuRdfKdb6i2XoeP9yeLySdzT9UNdQ4lR7t0GvaIuFXD12rZ2hbP2ZS5eVd33Mn4lwRvZLG8_vHyEJ6mlFPr9Jigu8BVe3UqxXy0bKXz2pDuvTT2AAfL_MUtlzXxhJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=YMhxq76v-KjlhNv4YlAZ83075_S9p16IPKbxOnvHzGhDSb5P0iL4_Xyyot2BjRcKa8rj1MJ5pAgyhimXqLL3AwYiDsA24tCaOLXoXmVbQqWcK0C9zw0oPqWRfnAjKs3pMtEYOrlfC70b2-tnnlAihO9L5BTA25yaKpyYQEPYBESsW2aHXb1yY_UFm17-jITOlszcUBE0prC2S4BVkfRNgzYdAKo7Hu9xCY7SB-0A-ysfSMotOjM7KAqgal12DqJehjEkNden9LeElsGqF_Ab1jtjcwhMAuUCVwRDz4dYCWeWPbrZ24nzdkea-g7epMPv2GYszy3szgOKYiXRR5MgZz5PclUl-tKdP6QHfih_-IIM340ZmzqaD-7Ccr6S32CwFUmtNE3LfFKE_CQXUH-iopVib7z3PXLI6PYb7jB-HFJIESbtbRd-WjYLvURDfmnPMiHvt8bWu0Nysi7_mK_B--BZBl4ykF--T8QIs4QCzWbuzY3dtssSliXJBUeoTJJnc5nr20J4bJ5oB70Ax4XYm7Pq7sVES6z1ie6jyNDPbI2WcCuRdfKdb6i2XoeP9yeLySdzT9UNdQ4lR7t0GvaIuFXD12rZ2hbP2ZS5eVd33Mn4lwRvZLG8_vHyEJ6mlFPr9Jigu8BVe3UqxXy0bKXz2pDuvTT2AAfL_MUtlzXxhJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب‌وغریب میلاد کردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=kAUaC5ltK8cG4FWsgNdg0n36tBQGwuCMMdDMo-126kcPpad4drQD7JJTrL41tOW1YxDZe2AIJHKybN6OTMw9szJFQSWV-x8wYnOfqKZxTsfPdTYgG5m_TY7yRxgxCtwE6mcv3QpJruuu-N5ZM0q7A1j9el_ckia7rxDRRPF0EMm0yKngYFCK5CVLEzwhd9QmSyd5ua2hV7xomcrXN9c5V_m618QM7Y1d7l8GL2PhKyONDhWssk0pER9HJjfqHZme0DzqK32FyX7BY8Tt5bFru0SOD3P-tPE6bWwb7ia0UyiQtRZsMpHTANCpe6E_JaGuKtiNmThX_dnDQJu5zuaeSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=kAUaC5ltK8cG4FWsgNdg0n36tBQGwuCMMdDMo-126kcPpad4drQD7JJTrL41tOW1YxDZe2AIJHKybN6OTMw9szJFQSWV-x8wYnOfqKZxTsfPdTYgG5m_TY7yRxgxCtwE6mcv3QpJruuu-N5ZM0q7A1j9el_ckia7rxDRRPF0EMm0yKngYFCK5CVLEzwhd9QmSyd5ua2hV7xomcrXN9c5V_m618QM7Y1d7l8GL2PhKyONDhWssk0pER9HJjfqHZme0DzqK32FyX7BY8Tt5bFru0SOD3P-tPE6bWwb7ia0UyiQtRZsMpHTANCpe6E_JaGuKtiNmThX_dnDQJu5zuaeSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26033">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛
سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد اما گاوی در کمال تعجب قبول نکرد و گفت تنها عشق فعلی من بازی فوتباله!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26031">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkEz_RBwS8HEWxR-jTHMAG6Bopwh-DntNvwDydwlXLWVpXu4lA8WzIpuNs5fPRB_f1M0C51o6qU4VJwoP2R_ADqUIl9SgN5Jy2gmovt4izaiN4HmCX_U2mSvjVJkx_BEveOISFQfeZtq_oU0uit2WT7aAO9LWtJ_gm7IYD8bQtjiQZin0CsqzpQjQ3oHr5fAd9MwRyjJ6hPZvERlYSjhLCSQ-KRAE04yirAe2SHM_DMgTrLHkxfrAC8oSWYgX7Mfi9qtNdS0z9siiY9qW3SgsE4bnOxdU6bqSQc9hDE-ah3EqUQoyozv8PHwbAhl6nE6K1ADNUg_1Bv2L8NMZo7RWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26031" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26029">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=FLEBMTKiBoFnDFLR5_dQv_lXvL6ZdR05Lu_zbPEgKQhDELLxjFxwma89B3t4E_Go95k71a4rRZQsePNXZXfLB3_OA2n70agHdnqDWqcuVjF8F7KUbwQJk85mFFjbDyFi6qWfJ_T6cdjjB3wD8XsQkjvB6ctSYRPL1CW5_PcQR7v91xF4ak2TUNhD4F2UgCnQw2MOjWMl9-ZfVs8Gx_fk9sve66yp2GFKBJSJ5gyvc91Rmzf-IUfAKMTdslHHai3oHp4UTU0U38nhPmLPHbxIKlQpR93AXtv1ksimt0WbAZhN_10muCfUurTTZnPcGH7Awovawvt6cLRWT_yv2V6URQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=FLEBMTKiBoFnDFLR5_dQv_lXvL6ZdR05Lu_zbPEgKQhDELLxjFxwma89B3t4E_Go95k71a4rRZQsePNXZXfLB3_OA2n70agHdnqDWqcuVjF8F7KUbwQJk85mFFjbDyFi6qWfJ_T6cdjjB3wD8XsQkjvB6ctSYRPL1CW5_PcQR7v91xF4ak2TUNhD4F2UgCnQw2MOjWMl9-ZfVs8Gx_fk9sve66yp2GFKBJSJ5gyvc91Rmzf-IUfAKMTdslHHai3oHp4UTU0U38nhPmLPHbxIKlQpR93AXtv1ksimt0WbAZhN_10muCfUurTTZnPcGH7Awovawvt6cLRWT_yv2V6URQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26029" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26028">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCLvKdbfZwUKDusPr7KabTaG7FCufB0HQAA1_PlEri4c6JmoiUJzN4i5756N8lAc5WfWsS1L27kTiL304mfa70cj08eqPyl2pAjCPL-jQPyl8Vbsb83UpDlrsEjsZJeTFtjr1bGG1KyoEo0ZkP9wYRQeqhxFYS6N_LYT0ECgbpqlHOf7vfd28pc9I1obh7jZCAOb6zYJPRRkMS9wmxsjC0ZE-IzgC5UN_WYhrsjIwBD70j1M7y6JFl0-9LCJ2rI4obf2Ly_iTp8iyDmjCMG2JBYkJm4rj_G4RAB1jaGpx4o_hHB9vmMwwKl7U3_IjR3b-7fKHRgfvLXdogcE7ic8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌دیدارهای‌امروز؛
کمتر از 22 ساعت تا نبرد تمام‌ عیار آرژانیتن
🆚
اسپانیا در فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26028" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26026">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGMxINoW77Udq6Ma3Gpa0lG-NNYDTIQyqn6QD1NCi2_KrR-9i2nWRO4G4XxEh5r4Uv7XpTAGDrOfaDf-IeelfoFnih-ZpzEhnTAq2VXg5vRPQQU9hvy0fpih_Xe98gCCMsXScEGKV8SwoOCEe7kNVqYFWtKU7BSTGVKYA9iWNbLTQ4HMnzgUHcSiC-FtN0yHXeHAlgHwb2LdXZhQUvf_62xoTfdK5PrLIREVdgat3E8uMVAaFVnUJB6zWAoP0iahY-13BGnAbb3UVP-4Ptrya4Y8Uhp_fCBg1uLyzAUXMHI0OYBuHJ1yz0AsUTQ2Ny4_ajODDNZMTfXuvONHIv97pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26026" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26025">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdibSXzCcL6I1HC-Zp69InIEkyt98oERSddhKn7Kbgf55GSOIJg-mMF-g1_kBAdSQ06Ot6lmM9RGLiqpdopJomsahTwxbOVExZdDj3yL4pElc2a8UtymblQGI4_-iT6SE_abJdHKpqg9YTD5hN6drNdRPsQrH3KjfBQAM0cRYoF9ja_ymrAQjsvRZp1rr1_R7bPdpm3dcqi8wOTLPVMfRL79Gz6rnWYquFaNq_GQvf_po9Kvra1slVqsK_0Pxu9grGR5PvgfhrojgO2vummGXJKslX4yGXXgwb9mWLo6IlSrB3hpLBnOmYnfUgkn2y8LTYJunVWsBcDZX-xOtfRwZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26025" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26024">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=g8uSttg4XVs4q-ZnpHYByzm7SLR5MCZuh9tBCGOW7DzbqUBnw1yUKAwuqRlnJMpraSg8fXZbR2lICZ2V58ff5TSAS2c9az_yEPKWMAgmLBpm1ZId7JlhIMUuppzWwUEc-iAC9-x7s90NMzEQGgSnIjDSN1HaJUqTqZRt4H9oXdjkgJlG4OyVHnZ0B_W42ikOqK0SfpK5Zyy55R0RTHNNEEJ1XDp4DqZxflN-n_Rtp2d-SyAd8yt5osx56wCZbOq5qodUauXwmMdCjBfXH1zPF0dWWnAZpW35YcF8jDvjtfVIyAdeZ5bNmkmEcgOzR7jl9GTStFHeqaKeieGBG8P8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=g8uSttg4XVs4q-ZnpHYByzm7SLR5MCZuh9tBCGOW7DzbqUBnw1yUKAwuqRlnJMpraSg8fXZbR2lICZ2V58ff5TSAS2c9az_yEPKWMAgmLBpm1ZId7JlhIMUuppzWwUEc-iAC9-x7s90NMzEQGgSnIjDSN1HaJUqTqZRt4H9oXdjkgJlG4OyVHnZ0B_W42ikOqK0SfpK5Zyy55R0RTHNNEEJ1XDp4DqZxflN-n_Rtp2d-SyAd8yt5osx56wCZbOq5qodUauXwmMdCjBfXH1zPF0dWWnAZpW35YcF8jDvjtfVIyAdeZ5bNmkmEcgOzR7jl9GTStFHeqaKeieGBG8P8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26024" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26023">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=GIYFlm2vtqcqhqSOp9tFPpiNk4tDg-vcStjHdX1mZUsWffDFUBf8R6_ZXUqJKVaf8uLII5qKKN-ghCJQhNK9g_xUIeN4vmoocOa3DPpbRsH0E5OWHQ-ACTLQmHGiemp1KTnRd4A4iWwbqU9SJ3os2MukuGFJ2D1-g55TaSswZL0iozJOGODU46zIc75UVaRybzHmwtacCgoCSOOg_ofB5Ny6p1lvVwZSCQCg3l_I_yg5EIbphYugdCPD-s6moXmvilC9kfM9FlQXjg3ERuzmq3NwUjJpgbk05ZcGvToQjnyns_lMd10pyDuO22yBD08sKGx8TjcJDrFqG6Lxo5XB_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=GIYFlm2vtqcqhqSOp9tFPpiNk4tDg-vcStjHdX1mZUsWffDFUBf8R6_ZXUqJKVaf8uLII5qKKN-ghCJQhNK9g_xUIeN4vmoocOa3DPpbRsH0E5OWHQ-ACTLQmHGiemp1KTnRd4A4iWwbqU9SJ3os2MukuGFJ2D1-g55TaSswZL0iozJOGODU46zIc75UVaRybzHmwtacCgoCSOOg_ofB5Ny6p1lvVwZSCQCg3l_I_yg5EIbphYugdCPD-s6moXmvilC9kfM9FlQXjg3ERuzmq3NwUjJpgbk05ZcGvToQjnyns_lMd10pyDuO22yBD08sKGx8TjcJDrFqG6Lxo5XB_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب‌شروع‌شد؛ جواد کاظمیان با انتشار این استوری و تگ کردن مونیکا بلوچی تولد او رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26023" target="_blank">📅 23:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26022">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBvQZHhpIs4uCpV0NG1aaYXoj34h1Oa2uR7odFjXJr6cbBAxMuXCP42hulwvwseEq1ONhaHYm66fOiJTiBylXmhbjbjmyXf9uOvbEQ50LuB43oIAId7cxumvNZpsazVuD28DP8439Q-2CoSXXSVllPb3weW4iz6ED2VfY5qxkkptpKeKqeKZs79xN4BWudPYrTCr2Ku4WVS1UBqd8bHGDXePwXTDkYaTZJslHblb-Ivg71fClno7lz6KynV9oSNACLnxK_1uqArR1oTp3CPqg3_I-QlnIn7nbajh29fb3_74rx2d-dHWft7TEBBzlMqGqal5kJnAOdYez-lUPK7gsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26022" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26020">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqkYfx2XvMyTvH-mlGCdE2uURLfY_qItgnI3HLtlHmAQ3eDoH8x5cZbuk1v5a1CRi32cT0zHd_ss1yR1mrpoTaTuwqfhOLb2fn4MgJ2o34MSRGoZo0sJzVqXoZHgWUyJpHxnOE8uzPl7aiyIP7llnFpldjBg4kQNy5B8LLTatnl9wAqnntbUPHSp6tYXPyDZee7FOdTmElh-PlbokXn3zUO4YgU_3K5XiIqRvbiT9ZQPjx6wa1C9JQTFSk9IVQsvf-rmyeP6Ce9gFh86tv2tpAA85ycoMgaXSjXuvmRgdgCwQewGWaVMckjfs0GeSn5DUJ6hEQwKfKX9NDO30naRSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RV_e8rReFXLbMb7hOV2kl5aRofaNHR24wLavy5bGTJa8dYN4xhVhoMul6DD9LvjR94NcgS9QMNWRaDyY2lp9IYVB5ogik2zEmzjNwMEyLIfmKeqTnoUEJZcTpMzWa0oNFzN27NhNfSwhsvFFyo1ycLbXijswcE4nSKxiXq_CPvnh3N0ehfa7a5FRAwwfNzBeYWnxkGphjX3wdmwhvx4lKXgNrdvzptDo4rN7ITIdzlhbDul24mB6ruWdS9lePeIP3GHQ4F-F-kcNPkSCh57D519u_gC7B7PQSkfv7i1ChYeMTcIjk30mc8Fx2LWLH0WByqQ1qP2Hw_bZHr4SZkxHcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26020" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26019">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beuj4OstEaM5RaqMzrARun1jxv9_WZF27jKZfLXZLotBaWn0XFUJMXbFsTn3VnZmbZjHmYUxI6zhq81IFo3TTsWH4Os3K0lS08e1ZbGoZTAwNaxJtNKPaIAp7NfSwbgAlf5MlYAVfOjiOIgfE7Gfuod3z5KcBtYOqt2jkYt7tznjFlZ8JZiiIoD_jFOCt3UBaa9CI14nsGNpj2SApXYPdU-j_2gYkdFrRUK0lTGM-oedOZDKdC3GrwUcUGUWF_7bptTPTzomPnDRSBetJJ8J5OZjvUUoL_BjUpjIqx-3Se3y41RS-WGqHKLsHUO05ESis7FvwZlpKb93evPM7L_xxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26019" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26018">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr_d2IcRUPQbPO1YfoE707iAPqxqj6uHHc6EXZmvwUWxgqTrka_19l5UD9-7c64qy4Ugr2DYSgVa24XnK5dx2c002Suk3kxBpt4i9BCeGhTytktJS1Kv67vgRLiw3MJWX1qLUXQyQlHbPR1v-l1rsvB60i5XAOJsyA-bQlsG2CTpLthzmyjze_CC1XYy92dq0PXZy2N-2GtYwVw2OPGbPF4JuV8ACwMLfvOWG0qJkJX-8G5MLs4eJIBwRNrw8lkPKxn2LDP68TMgPGiMriyKE4CZ3ntnQbfwZSGr4bYwmWkpr1x9hY9AMHh6NcDscVcU2n4KeSsLauDvrDL0nhIANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26018" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26016">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇪🇸
🔴
هایلایتی‌از عمکرد آلن‌هلیلوویچ ستاره سابق بارسلونا که در آستانه عقد قرار داد با پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26016" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26015">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrVQzqE7EDtcYn1bv6T7pepU9wMB93FCYJRg3dNHdIKhu-WB_D6pWebeNWMCuD6kQkVSsGmP1V4ipxHWa7QrrKN1ni4NPQe9a4IkgBfyBmByuqZuUBsmAt_9vTsh841btseQNwKfYQ_UyPjJZoyzZf4kamWulAqtno1HMMEAebKyHeiwRU4uvweYkgWhcCP7YhAZosmFH5BZBPw_dK8jUzybwtURbKlv8FeeCeHQnXQp5enBMeyMhfQIkrCKIZO8tfeVwEX25ankRDi5ZZZ5GvYOPvrD1I-sqccXqCLaJscExfXBAWnFua61355iKJE6RVzOiWLSQWzKqLDKrIp74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه‌پرسپولیس به‌درخواست شخص مهدی تارتار با یک‌مهاجم‌کرواسی که سابقه بازی در تیم‌های ملی پایه این کشور درکارنامه‌خود داره وارد مذاکره شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26015" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26014">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boZ6uFV8INrqZVFjW2xAYSuUed2dSGEnhH19YjBxGd_6QKQ677vmWzapDl82HKeVyrVB1x4cV1HfzYiqBzIMTeXhUpDw7L4YD5Gq8rupdEYYU22q2HLVnzQT9qXvyV3hFVgJHc8bwHUATWXKUEx2CKg7az6eo1zdqzL2oouwMSHoUtuAG8vpogUhBU7i_7wsxR4Hr1jshcBjVNi-5I0IebsZSg7ZEHkD952Nt-yAo6eYgabxjtmb_F_9iskxspw_RMlV69BICpwojL7lTsqavp4F1EiSoK3CEGhHBX8z-dfnBAa7j82c18b9pSlk35j2SfcoowYbexsRVUKSPnmj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری اسطوره باشگاه چلسی انگلیس:
این سوال رو از من می‌پرسن که چطور می‌شه مسی رو متوقف‌کرد؟جوابش‌اینه:هیچجوره نمی‌شه! حتی اگه بخوای با بازی فیزیکی جلوش رو بگیری، فقط باعث بهتر شدن اون می‌شی. مسی فوق‌العاده قدرتمنده، از جنگیدن لذت می‌بره و واقعاً هر چی که فکرشو کنید داره. به نظر من که اون بهترین بازیکن تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26014" target="_blank">📅 22:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26013">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26013" target="_blank">📅 22:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26012">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNa-DZyhdu0zjaloaIhJVHNEkXK089UATrl5XA7xTLejZeLdB2lvpN6EH--EMB5_0sk4FVzLS1Qh2pUZfsUzlyEYe9yQrYiwpMWvcxXjyFLM4GxwtMOmkBY3YpE5D0limTeUYWQyQ7g3icPYJ-24CmRq4BhDyx3DIa11fy_C1S1n_1fvHtEOkZ638SnNvVScPjeDDvg88xL6H-zcP1WoRKdX8oOTsxcGz4TuYDFgwNf2M7alF59XRMz0Z2xTDcreMwS1qGviw1r_efgPaQVp7bkXjavT5gUp-6aZNSDhgbPV_xvLc-Bxj-usoEfO7WIT-P49yOA_TSYAQOLCesww3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26012" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26011">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSYWGSOQEl8ra_o8Ds6XyKM6IMpH97NYz6FQgdLuYnJ3lc6RdA3_OeP5jzE6I7N-fypPzjVZDlzfV25n03y9oOezcLP2ND7SoIh-qJb1UY8_plNvxgtJJBcFWcaf6W7NBLw39z9M_CobXnVjSRoSz-LfBNyxv4p0vKZKuaUShZ4s21SsQT6xbB7qaDQE9je-UeGUqRxF0Fu1EE6FFn6HQQo_Dsq4Z_ocN68zntjBAuAdmlGTmtSZb7PaCgpjZpoacvSM-3dEUN0ymuCURQOkQC3epYhOwpFIh7WKOuYptGzq-m9r6p3tzqflX3Kw-0Jpb8XDjWzmwYA_Je8uCn_NPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26011" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26010">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEaCMzRU3QhPYavFHLtsZ_AqpG1N9mkwzCOVILfq0Cz6r7pC4gRleihVXCASSrN5cHJADEprNdwfGiv3kxkRyjCk1Up7TarVSwAFPPJjEEQYTjQgjb0fSBZ_xVzdUagKYEUbhWWJZpankldrAVCBQ3qI8qUG-OqN7Qj_MJahhgKC8am26EdhLNbzVuJblEm1E85dJfLqA2H8XDjmprtezAi2Rn1h4xnJr7dbU_ca8zjHZDr9ayttf69N7G-RV0lMvlkFCK2a01YVu8J7j1_6kDUEGC0CsLK_9sEWeDUuSqsk10phOV8RtjAqNR6Xt5umvggmBQz6EY1Oa53KT2fL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتاین: آرسنال هایجک خورد؛ تیم چلسی با ارائه پیشنهادی 137 میلیون یورویی به آستون ویلا درآستانه عقدقرارداد پنج ساله با مورگان راجرز ستاره ملی پوش این باشگاه قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26010" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26009">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgWTJ90kPkJVPbmm8-zPgDLO-S5iyyKebxQRmWQvmfNab7GTAIaS0UvP_sBYSDVK0s0CZmPf24oSXABvSB1YraJMJu2XODHAqW55Q58r3hPsCFjMLMlSnavTThIcI96DVEBpKL0DShGdqZTKMBN5FE1PUmSdZl4LRzLS20MT-PwQhNdBs7DANcLkMzBjBMEZ2Ch7iYt3GSWQZFmvr6zTb5SdVR7T0bvLrnjC8LFnuTc3z5KPK7zHTpSr5BE7uAMp6ukHD8dDDEVX7OCkikf9M86Ebtc4AQgbF9MfD3JXhv20VqqxTX-yg7_BCRZYI-4AJPoJFr_dmcdA86SP8oDlPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26009" target="_blank">📅 21:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26008">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=nuFIf8QsmjePisUFiPJ0f5o8nyF2SRxhVc8jqSi33vTDJsNZ3-vGF5KNjmF8BoWXGEuzpHL38ud8OiLEf5zsMGp9r3Ve3GLEVXa5TrKtoFKMD4xXixX2qmmSftiIkfnFCQlyQH4vaiJDMihPcvhnCyFbF2xXHT9EXrcTGbqbByyprNXm3YKa6nEq5enBQorx6k0OiGxwSGiji3B6ge3kiZ2rg1S7dCSz_-F670SIzWs-j45Cg8ZVFdlcpYtMyZ7GLgWm6DOmW_ApuTUfJNNvvD96YRv2nlWEjEQRnr2wGc1rhvu1dGBeYEtG6_rhhCYyQFYAgydUxkNgNQGNPlHx_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=nuFIf8QsmjePisUFiPJ0f5o8nyF2SRxhVc8jqSi33vTDJsNZ3-vGF5KNjmF8BoWXGEuzpHL38ud8OiLEf5zsMGp9r3Ve3GLEVXa5TrKtoFKMD4xXixX2qmmSftiIkfnFCQlyQH4vaiJDMihPcvhnCyFbF2xXHT9EXrcTGbqbByyprNXm3YKa6nEq5enBQorx6k0OiGxwSGiji3B6ge3kiZ2rg1S7dCSz_-F670SIzWs-j45Cg8ZVFdlcpYtMyZ7GLgWm6DOmW_ApuTUfJNNvvD96YRv2nlWEjEQRnr2wGc1rhvu1dGBeYEtG6_rhhCYyQFYAgydUxkNgNQGNPlHx_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تو زندگی همه باید مثل علیرضا فغانی باشیم که حتی اگه داور فینال جام جهانی هم نشدیم از تلاش کردن تو زندگی ناامید نشیم. امید کلید پیروزیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26008" target="_blank">📅 20:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26007">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7t6rMms0Ku_llgXyps5ueX_dSjJW6QKfWlw1E_XwZ9Nxvly85W35YiiQBayzJ0Bfi-Ot1wH7-zGsMzBIGnL8i3kSctITxX34mHNLVxe-jUaXszjqWQafcURhxSACwRXsMfqavmhDXs3RwoBekxor4cA5Xvvhgo88_Aw854K6280ARDJqL-vZkZcqgwHIRHU9fG1qXiP9Iy11EB4cXvOmwNfWt0h6IgudhCTHTw4APgv07SPDm1284yT0I0QI5zwqkbaQPCfl-waM74fhpT39au0szm6Ua-fTB7S9cRZk9x9V_70Wc8-sFzww2y5mv7L7va2n9W6GD_XLqQgY6S4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26007" target="_blank">📅 20:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26006">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9_mzXcSlXpg2eocSrnLztTHkbsQzCwNCNyyzs54jMPxVO616auUx7Kq53QRdIV3l9zoA3vvYGSrB6kWaEPegeBBN9Ip-dID6SOCqR2tqvOGqeGzqM2oH8isDwwdz6hjHPIZBv27zhK9HUzbGQldWX0EjWXJg55wPtpOOtfdskzwxr0LYWGva_kVRK9czoI5lHiZ6AYR2rhvKX2K3wfA0nYEoYRGuop9HKxCd2_L789bdsasFj6dhYKPMK5TBX6fcq_Em_JwlIKTcI0MTy1XKfKY1YVPFoc2b3tmqIwj6QvpjTlgVgp_0m_KCshnn8PD_RDrY0g0ul8aVG5NbtO3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راجب خبر حسین نژاد هم‌پرسیدیم گفتن تا شب بهتون خبر میدیم که توافق استقلال با روسا صحت داره یا که خیر. وضعیت جلسه باشگاه پرسپولیس با نساجی برای جذب ایری و طاهری هم مشخص بشه قطعا تو کانال میزنیم. خبر رو بی سر و ته نمیزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26006" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26005">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3YAZrsSQfKtfyQqeXW-d6Aa-JeU0PHpwUw8j_oxUvqxt-qNPSUMRYxZuS-z9uxH6GNTBdMWmtwCVOz3FMU7pv9L9ZDM4w_Kg4s7lN_XZ3FGLeEcaMKg3U6v7hmkhBAZfH6Sy5x7esfyBjOT6mEXooVDzBpAt0DnZ5F-IZ9UICMbFyLfencZCb_BoUk5R1O-RnTraIIulWzrWhjhTWkGKDrKmUd9x8gnJbCV6XXPL00MufHY8VjbkHxZNpX6Gihh2wUKtcnSjP6WFplkdtkG-viYOy6peB9IymdxyuumoylKcE21wG7L-1NZPuxAADa41_Lofk_fU7NbtA4uaU6RYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وزارت‌ارتباطات‌شایعه‌قطع‌اینترنت پس از جام جهانی را تکذیب کرد.
علیرضا عبداللهی‌نژاد»، رئیس مرکز روابط‌عمومی و اطلاع‌رسانی وزارت ارتباطات و فناوری اطلاعات، شایعات مطرح شده در شبکه‌های اجتماعی مبنی بر قطع اینترنت پس از مسابقات جام جهانی را کاملاًبی‌اساس‌دانست. واقعا اونایی همچین شایعاتی پخش میکنن مریضن. سه ماه مردم ما نت نداشتن بسه دیگه کم دهن مردم رو سرویس کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26005" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26003">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izvfAnLWKtzcmGpOcrWar_4r67Gf5OU7gLg3t6NxMTrlq8C4EydzQXNTtuI-4AhnDG2zdkZJjMduhLIogZFieJ12qrn0GhSBOUKw2Ky3-yn9ktMbxAv-Syw7boSbtOMUc3oJ3meDEsVAFoq5xcB5ResBRfFnHkjhFufG04Jw68xa7_2nmMIgte7Cpu9TOJUX2HKWm9_z4njFPnXA6kAx0z0edTjfCzTk-17HjI1anhHHlauF4DNrd9C-VaRZ3LTJ6DyNr8qtuo7jYFUTmdsA9tOckWy57-2FoYfFgu2fZ5yJWRbgK8hOZkLnDXcFlbcCeAFo_We5vJQ6JyTQd9AbHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
آدیداس‌ازاستوک‌های مسی برای فینال جام جهانی رونمایی کرد که روش‌عبارت "آخرین رقص" حک شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26003" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26002">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=Wkws90sxOQ2jnzC4V_UTLxesmmocudsFDNErYgfJg7akQ0VNag2A1SaG6WrDoh5vYFkrGRkg7Yk2ascbqY8u9rk6IxeGWjYo3WeQHXA7cLFiW9O8i0LENXjibYJA6lX5z6-2e6DDQQGwPxaknV7mZLh9LzI1cbzUAGcx8qJzW4pD-MDk7VU_csK8pEpYsDLXhcm3KJmJRBj1VqIrHNMA3Az0ip7pqBIpi3Mbj2K2uRg0RglvkeB3DyxhXJ1_IoGrRrqq1kfFPpmmKPRN0xAk4t4aYwAS49IQ0Wmqnxxah77N2nHmPvqwv2DK5nSlxejyMQd1eaomHpqDaldOV8dOig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=Wkws90sxOQ2jnzC4V_UTLxesmmocudsFDNErYgfJg7akQ0VNag2A1SaG6WrDoh5vYFkrGRkg7Yk2ascbqY8u9rk6IxeGWjYo3WeQHXA7cLFiW9O8i0LENXjibYJA6lX5z6-2e6DDQQGwPxaknV7mZLh9LzI1cbzUAGcx8qJzW4pD-MDk7VU_csK8pEpYsDLXhcm3KJmJRBj1VqIrHNMA3Az0ip7pqBIpi3Mbj2K2uRg0RglvkeB3DyxhXJ1_IoGrRrqq1kfFPpmmKPRN0xAk4t4aYwAS49IQ0Wmqnxxah77N2nHmPvqwv2DK5nSlxejyMQd1eaomHpqDaldOV8dOig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ درباره مسی: من‌از ورزش‌سر درمیارم، یه چیزایی هم از فوتبال می‌دونم. داشتم بازی مسی رو نگاه می‌کردم، دیدم مدافع‌ها حسابی چسبیده بودن بهش. ولی یهو دیدم غیبش زد و سر از سمت راست زمین درآورد. میفهمید‌ من چی میگم؟ همین خودش توجهم رو جلب کرد. هیچ‌کس هم درباره‌اش حرف نزد، ولی من خودم متوجهش شدم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26002" target="_blank">📅 18:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26001">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4lw6vMtp0FsHcne1dhR6oZpN35GZRSVlAA--_gBjP35OhQRlllP0Ka3riVX8N-7WldlBOAavX3e4rMQTRfR8BwNr6KUv_wT55BbrkXeiNb-vIQAqFna14DG5ADacvgqbSlG5MKfzAfmPmT708tNiVV1C8gvSNf9mdtM45M2FVg_Ffg6nQRTLhbcsALS9qU2TJIq5yUKccv1M7KDKoeW7RRntEIt1wzPaX1nwa9Crwh6mZks-GOmDED2CV8EmjeyXg-Koec5XUM8lbAZmf3VKjQsTK-JJEFt6m1aaLg2eSH99-R7deE6FlJt5Vbv8HG__r-sAJpUitZdyGC_X6gfog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوان‌کاپدویلا دفاع‌سابق‌اسپانیا باسابقه قهرمانی جهان دست‌زن و بچه رو گرفته و بره آمریکا فینال رو تماشا کنه بهش ویزا ندادند. حالا چرا؟ چون 10 سال پیش برای بازی خیریه به ایران سفر کرده بود .
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26001" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26000">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2PP1nGcLg5W834DxmaRRO6yowCJ-uFk7ALrmz_OIi_Tx6th4zrO9XZiQZjK5G-Bo-kqX9i30N-PBJR4BD-dmpvYBWbPtv3RlJYOs4KqBy_SeAt-vhGi5kJjX_uRpcqxTzhiXJSY2z1BFIKrivqDqXIQ4GZOeZndZIAVsIq5cvPpPFhnws4ZT5D1D3G9XCz3oaNRFpGAUO-yRYSFVavl9d28a1hK8iy1tNCRgsY2i-D5RMA0afMhVVtgcxPsp9Sb1YaaQaWd4ABPL8BOyUgdU55-5BkR51m52h35fFzRzSYBOhOEyMm0UsLoU8-Cqe65MC-VJReq_w0j2JiyYJG8tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26000" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25998">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K76ITIPye2q7Zd2O3zdTKd8-lXKjBaEEy7jKT3kxn162JPHvy13snh-os-4eoDv3vUXyJ71soY2FkqWhJZjmuGFqW5lY1agvxMp4DblpCWYzFPruoefe5Q11ap0puxZ46UUDe93XGR8jgmArDmnJnwh9BtlPOgYKjadMT6C3sPmpN0CDHYTp_pYaHXO4O9yWtskhIs158coVy6WOMgXmhzAMANSnGigPQ8BrGxh1eVT-KaT_yS8gVvpXnqAMiRjyloTzpiByyds3CZvqQLYs_L3pkcYYZyLvOK3RKRm-t6KvYnSLa4Li6IcqjPmzcy4UifW0QbbarAwzOt0qxsOpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم اومده با استفاده از تکنولوژی آفساید درجام‌جهانی2026 باسنشو مورد بررسی قرار داده؛ افساید مهدی طارمی هم تقریبا همچین چیزی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25998" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25997">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQQwEkJlv71g1BV-WSIfFaGABErZ17w0RJnSYkqM3HzLf8FNmlNLipSRHRRPrlUr3p6gl75Gdpkm6R8ShYpBaHM9_1QJ1a3DhdGZQpuQbLBKgFtZEYJ3_JaECUgOGH1I96sYTdtRxYUM-GXmYKHePfjx2_yh8BFciYWRGIgZSNjZ5VsrbQOfY4qgLI_YL82FE7ye1PfxK71_22kg6x4k3EYn5L8h04b1zIGDwUyARkG3qc9RQfzAgAJ6pYdesoPElh-MQlqcD-WkhCO3Uip7xHdiKHKl1xGUzy1dTIm5K8yDFRxEG_uVI3Lj_NgbSSyB7v60rLnHuZ4IK-bCHy9uAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25997" target="_blank">📅 18:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25996">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkoehyD3TITr_6_OcugNc7lo31bvoBD5RyhYoMIg_JqkTDWS5YRkATGwSNgL2beZ_hsW9Zr3eLVHX7K8fx5QepztPEMDyE07XPmfvxursdKPuqxDP4eVhrQ8exzHNL1zc_kRhfJemi2grnUQZnUUDjiNBvT5CAy2dTQssUdI1LgXVewDuFau7FyWk7VQNX0MZ0DcD0iehYIHx5eZx8nsSNYDIoh5Tzv5KKyzuNrdL9ADoqntMarNf8i-aA3khzArfNL7VOFOszXjCb54uxNrM4tPSkaa1OOeM3vW-lE-0Or2YxDFgNVRivjAS8oKtNaTNQ6FI6V09_HU5ci0YC8oJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25996" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25995">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHtyWSDV2Bxcycg46ZXFuwN-PATAuHiPXIJzxRgWq3X48xgy5D6yl0l-pmLLtEqrFEo7u7AerWkhfVLmT53Rk3CZ1z1cD4p1S6EGtO1Ac9-kwaCwIAH-R1WomO76d9xzz8anhkqDdj2HAKFLr9n4-9YLHPTRHT0Fq_Lz5LbQ9bQh1O4_tHZV9iGCNjxoDX_T2dy5xL6d_zfIxgVBxf3gtuMS2sU0xv4bonMFq9jrdlc4SBoNqebEycdrV9ZZ96NsyRtvvZ-lLbw51I71nNijJzdHFWyGLq2Co-pXERD7ugjb0JY6BMO6KItZ4h2NqbxooC3H5AlULRvfL3eMWN5f4ygU4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHtyWSDV2Bxcycg46ZXFuwN-PATAuHiPXIJzxRgWq3X48xgy5D6yl0l-pmLLtEqrFEo7u7AerWkhfVLmT53Rk3CZ1z1cD4p1S6EGtO1Ac9-kwaCwIAH-R1WomO76d9xzz8anhkqDdj2HAKFLr9n4-9YLHPTRHT0Fq_Lz5LbQ9bQh1O4_tHZV9iGCNjxoDX_T2dy5xL6d_zfIxgVBxf3gtuMS2sU0xv4bonMFq9jrdlc4SBoNqebEycdrV9ZZ96NsyRtvvZ-lLbw51I71nNijJzdHFWyGLq2Co-pXERD7ugjb0JY6BMO6KItZ4h2NqbxooC3H5AlULRvfL3eMWN5f4ygU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیو ساخته‌شده با هوش‌مصنوعیه که خود کریس هم لایکش کرده، انقدر قشنگ ساخته شده که قطعاًاحساسی‌ترین‌ویدیوییه‌که میتونید امروز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25995" target="_blank">📅 17:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25994">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=bIqMzclrYJQtbFHp0EL8nIabDKtMs6yO8LS7xAtpRjhxEwU-sp1bFFOCQAq2VJryQUttwz3FCBLj1SwfATFR6Ldcgpc8J4GV_8cK3MPihyA0yzhAKEPyCA_PxSltJqj8bKRI0HzgNDUb559IE99sP_92DYUvEdt5VJzBdffxlWpZjgmb1K5EG-wtzHymFF8bmXrOChDd8V-Dw5hLTBiAdFyMOw5W7Cqjw_0Rde9ewNNDTDsmjC5WVxdRYvzNOh0pt9xoLwjZYiICiSAA3y3F8dA8nN4I6TFsbVQvUaQUlqqWiFNm_BorCmC-c_cAowPbNcHYMlzDsXk3oEHd1IY0aYl8KQYS_8-gasbJrLQc1k9kfSyON2SnuaeaY9upBi93Yw5wvr-9MAHVM38IbHtJG5j809YmDh7gGPLU16toERPt3WpWtyyeC4cUQOoCg9KA3sh5kw-xbWr6OUB5cyRaYqp9Gy04ZmE1_1vvTk9moRAO5mg23YLB1HjhMnBJW-nPa7tYmWYV9IKXqyTiUa5um4uxVAbLewQYKsTjMRNUphlmCk0KGu4m_8StVI_t3Bi-_Vsg3vaKY4OMs2DfjeA4m_kvgc2OsZ1sWyqdDCXXQKHw957O-ibvoFfRS3SXvcZKOOKreJg62aGNO7EeNJ_b7gYtL2qw5XN1Tmztza9ei-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=bIqMzclrYJQtbFHp0EL8nIabDKtMs6yO8LS7xAtpRjhxEwU-sp1bFFOCQAq2VJryQUttwz3FCBLj1SwfATFR6Ldcgpc8J4GV_8cK3MPihyA0yzhAKEPyCA_PxSltJqj8bKRI0HzgNDUb559IE99sP_92DYUvEdt5VJzBdffxlWpZjgmb1K5EG-wtzHymFF8bmXrOChDd8V-Dw5hLTBiAdFyMOw5W7Cqjw_0Rde9ewNNDTDsmjC5WVxdRYvzNOh0pt9xoLwjZYiICiSAA3y3F8dA8nN4I6TFsbVQvUaQUlqqWiFNm_BorCmC-c_cAowPbNcHYMlzDsXk3oEHd1IY0aYl8KQYS_8-gasbJrLQc1k9kfSyON2SnuaeaY9upBi93Yw5wvr-9MAHVM38IbHtJG5j809YmDh7gGPLU16toERPt3WpWtyyeC4cUQOoCg9KA3sh5kw-xbWr6OUB5cyRaYqp9Gy04ZmE1_1vvTk9moRAO5mg23YLB1HjhMnBJW-nPa7tYmWYV9IKXqyTiUa5um4uxVAbLewQYKsTjMRNUphlmCk0KGu4m_8StVI_t3Bi-_Vsg3vaKY4OMs2DfjeA4m_kvgc2OsZ1sWyqdDCXXQKHw957O-ibvoFfRS3SXvcZKOOKreJg62aGNO7EeNJ_b7gYtL2qw5XN1Tmztza9ei-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌بدونید فدراسیون‌فوتبال‌اسپانیا به سر آشپز ایرانیه یک میلیون‌دلار داده که در آستانه دیدار فینال جام‌جهانی‌بهترین غذاها رو برای بازیکنان درست کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25994" target="_blank">📅 17:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25993">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5oiEHScTqnbtwmGwkg-jXXpcT7TkDBApeaxDU8O5qU2xtb5A4o0uaQaC7asNDL3AU9gCdCE5h0ZvlvH4BsCPPEa8vyNC4ruetVLC_Dw-5xF23GAEZ5PsKOGDqx8eqaKE4WgX8ZWw6zy3bWSab5kSA2fDXRntKuBlins3Ew9BMDhrf6TT4TNvqhDZcbVogKUvSRgTNfVJj6jK__a-eVT6oQEcLfnWTSXN2ZC7IHm0LCmeDzu1yDTq-rsPpSjUILSqdN8PGUq1WYI1WOTNn-qBi_d7A74rYt9JMtJPEJQQuDbeoofrKQ2P-9nOFAhETGx2aMx3_D39sq_LIgDYTr7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز محمدامین کاظمیان؛ یاسین سلمانی وینگرجوان پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و از پرسپولیس جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25993" target="_blank">📅 16:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25992">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzQY_Lt3PgfISNb6JvKP1pqMy7sWRT_4K3KC4wFVO9exkXMSEMTsgNf5HXgP_pMH3Ut4NNcia2L02R6FGTfTTfcMtAifFSnfZvPRpINcTR079JbZ7JrcedpTkhjOymhZZcjhfOEgwZNC3c-6Du7yhAsx5hbmhC7GuejRZvMXg6oQc14eeyJOf2hG7471JiVQZ9ud1Qy78USX6X7G0Rm52eR-8CAklQATxHFRulIVdKjn13cY-zbRYYfR7QQARKjpnDCgIQ_opnHHA15Wpl_oJlH7sQwy_9D0VdGAhGtmhOPx8Y0RENxdtUqtlOeOmwTcBjBu3S1rUyi-u5a6HfTtzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25992" target="_blank">📅 16:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25991">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7vPKY8B1zPD_hlDOKaQ_79bJoy_FaowsNZVPomdjVjrW-gPl6f9BxpEAv1WxVmmzf9XzeIOFS5tRdocqZfk0atr9r8-TUjjZsYEZW41RIJOgbtv6xna8XrZBneQ1EfiqW8B-sknNjL_U_zQ09l1kIuK0qY2XF_zYsHtQtBp_uPMgMQBgOCyebojYLo7FmzzTSEsHWn2RYT61tvCfvP5kn52FuY2maxTzqT-GzWKMQXt6zVKejzYS0BqTU1uixjQFhGIjjwx93tPV271hXMKX41N6dymtZVF7_F4UxPjKFYnV0NvJA2DHQvHLvJ8rqxe1XodcwNDLpenRX5-Xb899Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ از طریق نزدیکان خودِ محمد جواد حسین نژاد درحال‌پیگیری‌هستیم‌که ببینیم طبق گفته علی‌تاجرنیا باشگاه‌استقلال‌باباشگاه ماخاچ قلعه برای گرفتن‌رضایت‌نامه به توافق کامل رسیده یا که خیر!
🔵
تااینجاش روخبرداریم‌که استقلال با حسین نژاد به توافق شخصی رسیده…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25991" target="_blank">📅 16:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25990">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBxbAa7rmw2RV3fzPPg7O4oQoXFhBVUy1po8BWSCAg1BiOPGeoktdj4nk0K31v2PnOEAGA9andlRq7aqyibdCefe1Ei_0TC8y0oEaACfteiCrAXGsyKIYjFwDD2IlwjhabEKeSfh6WnEnDHw6Cb39s1sk24AAAP4JSEQBiRnEB3YxwNT0mzyeyN32sRS1z9zv-7QNJtwoqvsUscDspxk1MjDzYR6mA77RYqq1oi7popsIcmhEIY5rJu2ilzrDWtMQYeEwnvbjIgJvPEtlRpdqUnEdd0ht89ny7ClB25VsWAOBPa6QxVlNMtxZ8cCNxUYA-zwDWl6lwxm0xwTBO2ohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25990" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25989">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grH4tI_0mB1YzX3VKkH46CAB_ovSQbbZBGg1bNeBHjSZDI-meftDzJ21eDU15FVl-teFn2pWtiL2H1g7pEoMfzViZ4ETUlMDBw5X6_y5oja7uBchQYPrENeIYNPCAP1LotAByLRyJxOffc03jUtrFyHVOS1O-K-XPdNe8Nou-o_Qkqi_rpwkrTzgVIVX2BqJqlbRhsmNVKJEqD2-93xClVVwHlBteAWcw_Ma9iHqY88ly9Dc8EyHWQNYtiQaXHC2Pd8TFpoXGtVfghsHznOaQGWY0qxansYwjyDfJjGKKV2hlvVtd2VTXKE5xwp7E19H3lJv0Mj2pt79tW7CM2R4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25989" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25988">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsrUI869N4ysTodwK2aWYP9fXZin8NB3stkWL1kcqN-mtTEpLnvhmzMinM4xH0Y18OEzrQpNOI8-IrjU5FHpLamzQQODSy0e3wImE1LJzXT6ISzO0eHFCiY3cKeQanrIlqL2UmyHrXcRQY2Jzv0vUmpHmuK8V3D9KVaWBOKyGymWfzJU3FajBmAQUQRdP2tsDr_wRz15dZ9UT3mppVjRg0f8Y1BTAirI1-AJm_fOTTBhpSN7wMm45zPs1foUWVCqbmnfVnBGZk03qY_WWaX0C1v4snz9JuLokTAMkgpCNWD7_LSmxowldW-XgnnkN2Of1AJ3PQpP4CPcosI3W9ajTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ یاسر آسانی برای فصل آینده حضور در استقلال 1.5 میلیون دلار خواسته و ازطریق‌مدیربرنامه‌خود به باشگاه استقلال گفته درصورتیکه بادرخواستش موافقت کنند حاضره قراردادش رو باآبی‌ها به‌مدت‌سه فصل تمدید کند اما در غیر این صورت ظرف 24…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25988" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25987">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJI6xk39aiCg8_XKTDqF_UgZE0XvITPvRNBSwxkUIZm__6Jl9GIwlIt7RM_X4yXm_bNKZ5jrmAbOQvn30VGFqa7fk9INFqD50m1rQtbLdIU6oTCOBWR2vR5cX9GfZ13KUuV6fn3kCXNpnbPlyLZ9Q6gQ_wsICFthiGJAlwCRqb1Ck1wwGMLorBIy-7IDdEciEQzctuCwLNQsIv_KlnzhXqlM-EhzsT2Ps72B3TcB31XP8K-_C-mHV76Igs_chqguDo1ZadWJeY_QaaDCfJyTkj_t5uAJiZPjuBz6QndkOk-fT5R5HcsnCpvPAdQicw0ZtBtKe6xTj6x_r1xrpfVEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق جدید ترین شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ظرف همین‌هفته‌از تمدیدی‌های خود یعنی روزبه چشمی، علیرضا کوشکی و محمد حسین اسلامی رونمایی‌خواهدکرد. همانطور پیش‌ترنیز خبر دادیم تمام توافقات با این 3 نفر انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25987" target="_blank">📅 15:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25986">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O27bbGoda02RrYF57SjQlsxsQ5eMRHesvWMNqujwWb6kKu9TBODYka0HCR9tdEgiZG9gaoMEYZPNxLaTv1-TCEynI4s-dBEOXfIlorhcJfjZt9Z-lk-xNW4eXUDqYNKJ7H4tJvv-2y4SdbBXlvt5sZZc-gwxUwZy4MukOni2QaSiFFHX37LFR4dsTWIjknkUifBPljk-Gbfp2wei31Kt2l7vLGekkGOaRjNNfln3Wj-kq5H-x99p5_6dVG08e7zT5QFe9CkRDiRv135Q-psiqAn1JbWIvJMT_D8pdVU9yobs_vAB_wa2Nd9dKAtBVZuq90aSLuzw4Dx-hyC2GXqZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی؛ امروز حوالی ساعت پنج عصر جلسه مهم‌سرنوشت‌سازی‌بین‌مدیران دوتیم نساجی و پرسپولیس‌برای‌انتقال دانیال ایری و کسری طاهری به این تیم دارند. طبق شنیده‌های پرشیانا احتمال اینکه این دو انتقال انجام شود بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/25986" target="_blank">📅 14:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25985">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSABpmJNxk9ECEMO3jaE00bjrQs3dmWumoxYugCRvt_atWxeRmoi_1nIM0s4hYD2e4-bkq0W6YnwlN843lwy8q6JldVsXy8bv_REwpUmikRTdCvbDHBOVnc-nJXaIRuSz_sNXhVE063nKQvkwYsR2oN0WvdZow3wfOz4JQfjmojU4okO78rBMVdTERjJMfL_lNDcve6AqmWASOhIvF_okB7y-w-kuV2QGkuON93OiJre5s2bARM_Bmja-kTb6umrJD_jhe0PvF5t0_IlCLO9KaouXu2IuF_RnwhPZ9kwrYBxydsUy7cSnpLtj3TQTuj_c8_uiC7T03kXvA0sHIF8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/persiana_Soccer/25985" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25984">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5wVx-RkQOmTone288AqMdQMj4b5Iczt3nAWIHaW6brps5HwnS4uwQ6UPqRgM0alTorvI22XM_z4muipwgZ9cK2GLT1wyOEC-N31Mu9urk2zEmdGEMc9tRaeIi3RbqU2f1y_t7V05y6WtY_ImHdHvbO49yV4O-KicyhEUmJXFZjKa_r0kGYue_9QtX6JaQDXz9O67obIYRc1HhOj2W9cDa5sVnkOzvSo6osgY1CuSsOKffT-AaD8twMGq9-8H_oadtYU-QZ2KjgNYrIs9AoMr3C0U-C5bZFYYoyI_RGfbGXlxKjjDWHQD-SKs1FDx1M5j6YM1Wt7naX_8OCvEniGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
👤
طبق اخبار دریافتی پرسپولیس؛ کسری طاهری از مدیران‌تیم‌نساجی‌خواسته‌ که کمک کنند در همین پنجره‌باقراردادی‌قرضی همراه بابند خرید دائمی به پرسپولیس بپیوندد. زندی مدیرعامل نساجی قول داده که همکاری کند این انتقال بزودی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/persiana_Soccer/25984" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25983">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkFGW61J3w0a7agxJaldkaEb14EiBccemlU6Nw4l-nEAfFgBia6dNuO0XhIL7GoxF6dDTDNSD77BmwViQbD44NfrMZwg0z7XcltwAgXEhhKMIuk6p6vNEEC8i18DOJV2HHXR5I7wP9CHPvGNDlouKo85EI96kywxAUaNpa2SlSUALfcwXhihVDGPQE-aAGaHcrDkrlWEBry6os_0huQOAzKPWi2zIjkbT54QftvuZtiJNYfjkrFWG4-ozZEWRSHtlqYRR7CM-A_4w8zj-dIN_D_6z_-0xBfsFb8RMIZSJXJiH-2uylwajiA5FFBmaoLxrAOXYrtmODp1zhxF5pZn9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/25983" target="_blank">📅 13:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25982">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dngYoY207v4FSUZv6xyyNvHB49hH21IX33E5rR9frdkiGGMo7Q_WdtZL9c602nIDo2JkMgDH_9oQDYhJfxOVocVchagr2HO57kIGIQUByCiZrMYljlNraIMuFtcuWI_dO04h5I7MYN5Vja2mYX1eH13TKPJO818LQzDBgbZh00dIjtsjGxeR7W-600MBPNJ7fdFkxJNcHuvebyvdv2QRoKJ1bD4IfkbMGIP0CjvmYV5XfkwxQi225y-2Dtid6Fi2JfW_wjbB5qxlTdaSug84jtYD7hLBfRWZXrckcG_6sypCNLs72tnOtGQfAmoOT3YI5ED4_28ojVswHhkgEzmufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ تاجرنیا رئیس‌هیات‌مدیره استقلال: مابامحمدجواد حسین نژاد و باشگاه ماخاچ قلعه برای جذب این‌بازیکن به توافق کامل رسیده‌ایم و بزودی با حسین نژاد قراردادی چهار ساله امضا خواهیم کرد.
🔵
علی تاجرنیا نیز اعلام کرد که تکلیف نهایی پنجره نقل‌وانتقالاتی دوشنبه‌رسمامشخص…</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/persiana_Soccer/25982" target="_blank">📅 13:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25981">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKCA4FHG-IcDF4gcCPBLtfJDDSqGFFE9LnJPOOsGd-5IutU42bwXAWDUMz82LkMnMp1C0wEsMThxjLKZQtAqH2Itw0fyldtpe6VfO5_gKOr85rOANWwmMC5y91uN6FClp7tCD-JO7Q_cS2NIHwzJm1qMZRKHpHMy-_1tSEuXiKWhNN-S9oTu-F9igS9hhKu3sHFyJDvyXMZdC1sMsT7SAfYJ_fIKKZm_zxLbbqFQMI5jdB1rfHHC5PJmq-J69aMjguG2QBewlW6QeE5JdAaPJdfRllelJA9a7M2tbVGLNcxmgRRF8rsR2gLF93rs9AQUHe6xlJff3eaTmgw1l7e1EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/persiana_Soccer/25981" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25980">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouWKZhQYU8JXsEMhyuUnsuIJQ_I4G4HqWySyqMd66FMjuzqkalmAoBSD5KWemI-1B5Tm-P9pddUe1LFxKT5kCODn_3GHyDSGXd5Zm7JSL8OGElSKrMq2mqq4n7ulIFH0pzv6HZ7veJYJe0vFQiUHgwmXEq-dNmKSZkgoJT92yxj_hG-PsolkLU0esRNyJJEI_yhof7NvOnQm4CDnhyyADycgok2FthvW19cSZCBhExF5F5auVNz51BhbiAyclkcySNkT6v_qmWgkvrYpFiLA4BxhoJa9HkTOpKMRmTVIYzn_f_PxBP8rNlphlAnHSfQ-Zv2ES9M5GyBC_MEY1o1Bqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/persiana_Soccer/25980" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25979">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p09cjMVTTzjxPF6r551G2v8JyZLUJdryUyU4d1P7MNiPKb0AfvIj4E8nzA2kWTHR2SwHyhCP3sNol6IkCr60y4-uTkoqKw-2Sn-2kI2MuhVEzZNekpBPdqSTap7kbWPYtS8cg66EgaRwqMSn0hWuFT3YwyTs5nRqOC0XuBCwuBOLV7A8BsWoH5fhRwYvakBbJ-Mhq2JTKw2xHlMaKLAxsIHkE-gEFvdHAfUpjPw3QsPW_712IRr_O6sfKEWQXlNkfdTeK2zw2uyqvEVqdr1hcKKHbKGhDk_NG8E4191hX3i9F_mxCjzpr52k8oLisQuII-wAdUvJvJv-RGp7tYHK8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه تراکتور امروز پیشنهاد تمدید قرارداد سه ساله به مهدی هاشم نژاد ستاره جوان این‌تیم داده که رقم بسیار بالایی هم به او پیشنهادشده‌است. حالا دیگه‌باید صبر کرد و دید هاشم نژاد تمایل به ماندن دارد یا رفتن از تبریز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/persiana_Soccer/25979" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25978">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5wDL8DTohWHLhvQJSf-o0I0zhCAMNY8hXLtjLX26nVK_26E3o1fK4P_h8RiZAgZRJMX7DJI66qoW5SK2QuHuFzg4glgJELTgS6wecIAVSjhROe0e7lunDkl9BSxVIoIzS-J0Yk-Y81BXrYdpZsVs6kfNHWdYErrhFFUTiDRGQ3KjpcQYnYUqBMSn6i9-xqotmgPaNTgMZcQ-h_vJG0aTVbA2OkpTWQwKDKO7YyEziRZXWb3KwfC3vPoU7VAcV6KO1LZlhUGa3M1MSzmVqhpwOZQOQYlqXgb-blDW2vQ3gyGugtFt8rg-93OO8ci3LQFV31S4PC0axl0Svgo8VkEJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#اختصاصی‌_پرشیانا #فوری؛ مدیریت اتحاد کلبا ساعتی قبل پاسخ‌ نامه باشگاه پرسپولیس روداد. این باشگاه‌اماراتی طی ایمیلی به سرخپوشان رقم‌ رضایت‌ نامه سامان قدوس هافبک‌ بازی ساز 32 ساله خود را تنها 500 هزار دلار تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/persiana_Soccer/25978" target="_blank">📅 12:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25977">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5Ma3RLdjf_UdgxfL5A9iDiJbyJ9P2Y3oM28JPZ4yC7Gbmla2Y-P-1OweE3WprnMOiqMrmp-236gaR3dZzxtY0btL5IMzDpEFeYRBODUTPAHHo6tJqhzyypqJc1kwKIejX1MktxMcqPgYODQ0eWgZW8mHXoT6tqs60Uc7A7Ezs5SVulPOS8yjty1-ffLIMBmPf26TQnkuaZ9KJijSXdc_Gy7JFdG7IpEp4zAtPx3w52Q5ZU4j0UaL3wFuMB8COOiSj9-dZ_-KD91VexzTZfWfU2KKSGBDoD6Fg5S47GHLWU-rbTZ9qag0UtkMNkYs-JaxQTYwBBjUs9q0F0RFhz9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های…</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/persiana_Soccer/25977" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25976">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epc-RYWo1jXBl-7ZNq_dG6SVErbFviQZQkLiG9PkU_fCYQ0f4MkkyR_Czwb1eZpuC9SQNSAlTDQk81CxyaQhR11oLV77P4Gi-O9MWZFeEEpeoCrwLV_882jKuv-DRHL_Xiw268nOmXqw2GuftJ14Xjo7YH754OGMtHDdC2AVQmy6A0R3CC6ANxwV2VK1ytciIq1w7CSWvLLDpMZb7rz8-ixzvPybHBWRt__RSj0HXCSnp5Z2qVgtDXrHpu_J7el7ZJk9kyDfcY5kCULD6aIMCIwmuoJ_ix9MkpxryToo0KeLmFLkKFaxCjcay2rHLHw-sVVOnOHFMIr4-6duHAAfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیربرنامه‌های یاسر آسانی ستاره فصل قبل استقلال برای جلسه با علی تاجرنیا دقایقی قبل وارد باشگاه استقلال شد. هلدینگ خلیج فارس به مدیران استقلال اعلام‌کرده‌اندکه به هر شکلی که شده آسانی رو برای فصل بعد نگه دارند. ایجنت آسانی نیز اعلام کرده آسانی هنوز نامه…</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/persiana_Soccer/25976" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25975">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPs5Sm81D0HUN6BGIbXOVgr-t0iB3pQGcU0BtMNW2VzezbXrqDtSVZ3nH29HbmeC4eq8PKWTW00kTa9esd6Wt2HUYWwAULJuwjHe-mVT_v-P2ChWdyV1Z-6wrvEHYLp7Yz8Rz6YHRXZiifFjTKGWb-t3OrI84SLQe2gtZZ5QyUO-kiv7jobjA1TOk-icSXGPQticYKC0wwrOwGdB6kuhi1Y4NFbIYyhm5zN0J3rUKv9qu2q9KNXWem_H0lRhWNr1wiKxdhko1vptTXrnNN_ptwPVTKW4jf3w_q9mouZFd7Nx_6-JzbwZWktbFhSBEgC40URSHmuq3qjdPwlmxIgLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/25975" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25974">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YW5_SBfbyWFdIaUqUUDL1q81_YMQot6z2TY7V61SRAgkvNXbsfEAyCAxlDygm20kkRiccF3KV2kgJhjsaYat5cTx7VQPqGjNeoFaadeTp2GUsvl0l1u0x4k0H48jndDWjKcxuhUiXTHOy708rAuBFgaxsQH8cgeVPgJQCc1NKzY2TeAk6XqkVMgX2o4eR5fxs0RiDSy0FLteZEMBOECmGi466ITtCn-Gf8PpOPrt5_jqVOp0EyibQXmXgWDNPnIIQzNkMYgyzSBUDaBGXx2E_zyDF72cqLHQw4OSiFxcgJBAkYktGxQDu1TNAVF2aFVsQgdLKncfWKhv_5QQRGKlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ آفر مالی‌سران‌پرسپولیس به آسانی برای فصل اول1.5میلیون‌دلار بوده و برای فصل دوم 1.8 میلیون دلار بوده. آسانی فعلا هییییچ پاسخ سر راستی به مدیران باشگاه پرسپولیس نداده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/25974" target="_blank">📅 11:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25973">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=TkgFwrqY1_jq67CRv8BNvjbW42TgyTCg31SuxMhiYMUC999zPw6zSOuSuKxLPa3wkvOC4D-22WN02IXNeHbQIRIEDe5YrLdEwXjprrfLm41WWMEHNj51fA-A-JCfJcbx7OAxhq-UVBJS4YhkNNlWX-Rf8ZS2hotISsyWY1106kDFxkyfqFUa9bqlZCUkw-R1EmqD2Xog7Ux2maamJ2Ws4Fivp-B0zhOh5ObK5Pp_ZQUuy9BgqurpDftIJ-X0fuPiTpqkiTU_Y5lPI6V8-iw5ksM3d3ORrjI7wnfCdSQssG0bj3WzLp6gkaAIRsjl6MgUxQ4dUrjf3GyN2shKIzHpqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=TkgFwrqY1_jq67CRv8BNvjbW42TgyTCg31SuxMhiYMUC999zPw6zSOuSuKxLPa3wkvOC4D-22WN02IXNeHbQIRIEDe5YrLdEwXjprrfLm41WWMEHNj51fA-A-JCfJcbx7OAxhq-UVBJS4YhkNNlWX-Rf8ZS2hotISsyWY1106kDFxkyfqFUa9bqlZCUkw-R1EmqD2Xog7Ux2maamJ2Ws4Fivp-B0zhOh5ObK5Pp_ZQUuy9BgqurpDftIJ-X0fuPiTpqkiTU_Y5lPI6V8-iw5ksM3d3ORrjI7wnfCdSQssG0bj3WzLp6gkaAIRsjl6MgUxQ4dUrjf3GyN2shKIzHpqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین:
بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25973" target="_blank">📅 11:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25971">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHds2RBXNRJg-dWD_4BFLhEmCrkVGIPox3KTjCRKrRmsesjlvnReTehqmCzL5wsAAOTGNYqotEHec3ibhYd7WBzP_I9i88v1eGTcm3EKzkoKGaVe0g7SY4e2w9bPOcR9k2UAATs7TwR4qt1vhfUa7Q9IV6FLfZW8OsLHCvn36cNm1s1yMD4_4chwuE1NLViEru8D3Ejgf2lMQI5cZ2_P-YkneRe-IzCxfYWQHSi89VMVfoxklkJwV6BYr42lXhsb4aIW0Xc-WASeGgiDS4eV_pRgiGa64u6qGZfNds3uEcSXaFnmMvFhqxpyhjemCW_EaNh_sz7v4WuF4NtTzRh0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0A19Lx7dxpobNkWnjAU_1ivNjB-MPJWXS9VJ6Kd4BeHPNS2S2w-R0Uho4aAHNSjD78Ojl7mW4sstTkY2vyJnFa_oDcNVKNv_nD9msa9YWBShJDt3t_zljajDx_aL1LHkdaWGKBwq3KhNf_C7py27veCdH677u44gGsWHtQ2nFoXQxmLYU7Og2bJxAdd37918RBvEUTiNJhvfYyK9B0mz4hDsS9xDPf97KfzVktPA6i-vB9L9ad4kpYTUMmfWeKcQeSs1BCA_9_tD72J6wDuZqcu3O9GWf9TeV5pL6D93hKE3yY5ZLlQ_WmhW41P0dqRX9QK4VCDnZlBo5moQv7SDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پیش‌بینی جدید پارتنر لامین یامال از نتیجه بازی نیمه‌نهایی: اسپانیا بانتیجه 3 بر 2 فرانسه رو شکست خواهدداد و راهی‌فینال‌جام‌جهانی 2026 خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25971" target="_blank">📅 11:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25970">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HglMZhNlJs07G6hmUT5cFeEnpUAK0L3BkvNeiYX2aSc-e2hqJoGDaPGBMStEdqZpHUAt3KBKqTkwqE-upvsz-QQo76HdB0cZsoSCzC0gv8LEk_ys8Cpgxb5TFEHk-KTKv3aQod_2x8p3vyhLbpH1eHin94nX39OnWTkV9hRgVhiUAKkJnpE9ZPfpvaWMETNrk9etmVeOxabGU74qLyndUdTIzGrnmpmG8k_z7dN_gUD7SuB3zSwuvBIYbaTW2fCAS6ynSJF-gQ0P1Mi3gOSajqhOW01L7h6IMhF6zcNc421P4xmPa6EO2GZcCDAnQXRgjrhdYX0vwJ5vl6x2q_49Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/25970" target="_blank">📅 11:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25969">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxuW56-0i5FNExM7LBYejz3vfgT6OCK6DjrcPATX8VSSyMI4J8_cNE1ERpI98Ar899UR5YSZf0ZIPDcZp151kXSfvEciYL0CN5-6cH_v9Em55VbDcjYj-An1UXXx8MDxcCAEVdFGDMBXjEMcemHbsm2M8cF8HTjVo3L7Wi5ICg5dgAYTYvi-v87VXBSveWs5cUIVf1nyCGt25V8wHqpVfjlPmfCQUQFeETr5nn0inxfjX2FBKZe1PHxcVGsZv4lgPiGq7CJ5NvK3tJdET8ks8Vd5RYK8jevWMc9aDtGNoW1hGsuJEXQRaen6UxcF0vB9WLjXqkDvikK-cqc94SzuZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25969" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25968">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDsrjf3vFl3hosW64SUjreJlyf8OSR9g8nOPb3SE05LW4p7MrCTaXj0eo5KkPbj0W65GMr1zucRnWBWF2TPI9kEzM8TvF4xD1mIeSpvm2THqeXLFCnWn3FUWyz_eCbBUXwNj8T8LFKCU_vRZpIZrcX1MZcFn72AVcjB2AoWrTr5l_swsZ31avGmWLc7sxfHV8zAobOzliGXaeN4z0SBgF8QMrdXRbvTWEic8n0axPE9ed-FI0Hr-jlCRgpw_lMprkkLQ1VK9-H7a4xd5K_8aZyRqvsjObwbMbsxJBMJjDMkPJlF0sx6eW-bTbSIDwmOqvWZxjs5T2MYLW4vDWQTDFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25968" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25967">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=DwiiCCcUaL1UxNTaTVlFzqt1bVfWi_S5jY9CIrWdF-9xae3CLaNx7IYIj7BV5Hy6F37VQE9kKdkU9eKBKtvlbiwSXDFEOIUCpyusTDEBIgHsEoHjFY2vZwXxtsoTjoEnM3l_3EW7DTo_hPYgpuL91y7cdqFaX11hiY5CVU3ePNXgKz36GaOluCKreY2yuZJQXGXGLegJR33VdmIDEsHSvdx30yB1FFaOKNQAYDiE4Xo9b5LMNAW4cBWF0O_HP8bA8Fil2jMcorIzOs2rRI_15-F7AvdX9pzYb_OfR7EJYEYlg1Pda_yidVis95Sq-GwfLdHiCcau9-3k_DK5NdxLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=DwiiCCcUaL1UxNTaTVlFzqt1bVfWi_S5jY9CIrWdF-9xae3CLaNx7IYIj7BV5Hy6F37VQE9kKdkU9eKBKtvlbiwSXDFEOIUCpyusTDEBIgHsEoHjFY2vZwXxtsoTjoEnM3l_3EW7DTo_hPYgpuL91y7cdqFaX11hiY5CVU3ePNXgKz36GaOluCKreY2yuZJQXGXGLegJR33VdmIDEsHSvdx30yB1FFaOKNQAYDiE4Xo9b5LMNAW4cBWF0O_HP8bA8Fil2jMcorIzOs2rRI_15-F7AvdX9pzYb_OfR7EJYEYlg1Pda_yidVis95Sq-GwfLdHiCcau9-3k_DK5NdxLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25967" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25965">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgfnhFJAR2uM_iCpWFG6AcBhQ_JHcFMxSi0CEasfn9vSAFULgs4zV6ilFlWKm2fCRY2l162-JnZBTPTM7HgyHnfIoq40Iu__roOKadS3WG9dMzaXCLQR5Akf-6SGzB1w7zqiOJTfJSPlkuuVmuwU3Jp4PdSaf4F80xxVagomEkuNeYVvUjfI5wYSGeyuvuzTJ1QBs04mRWVlAR1LUWDHj-ZhgthpBbMyX1l-9VqqWL2KQV-auzThJirdPxOCzrqlXoJdDCyjyAj31xkxzwxzeM5uJ7fkaL43GB8rdx1LNG_WHRkzXptpLVPFn7W3VbEVa8RySuIkVRi1ZKA-tptKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25965" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25964">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nrvc1LLiNkJxGCAAAnAXNuHMMzF1hwmEROTQXDFTOdhvsmGls-9TBuUhzcIyrbyCydPV9Awr7TomXI71Cdri_gLn1lxJlYq1qPBOJKB0Wr4uhkQ1lb_-ohvuORw0mNySvjWri5H-q9Jekkh8fmpV1MdwtWQjYnQsh_Fhw0fEJLCn7EiipZuR1MkV6sPmRKUsYKzirpSKhUp6fIKk9X0tQj9hJv9ASzpqwbHQUqJ9RhgNELtc7XjhYvb11KvOvuvAMpGeOp7agAuDdS4UW9tsWHTjNZPmfkPmy16Hk7eWb6bIXCrtAmqngje8o8lHjvMF3xKmyJWUGnC98EMXNDu3KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظات کل‌کل پریشب وینیسیوس و اوتامندی و به رخ کشیدن قهرمانی جهان توسط مدافع آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25964" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25963">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=CEdBi6ps_ehFeMb8sg0JlH27Zh7mVMdZw60qV15JzM0J65L-q4HIi20TX4IkZPyDA3-GECXdQicDn5Ra_m0_S8ypVpOu8pbaQMzCMDb8czqhZaMGkV_AIsnIiVjIZFYbFICtQBz6y9gj22Y6C-UzI_sckr-K7wm_B2ZgHrITwj9E98G_QiQAtJPJBCMRLl0sKoWEiXN8h67dOtySmGWC0hvMfXL6_j5CkKy0Nr08V2Ol68mb7kA5sX_Rt2Q75aKgLz6izPUzSTuzgOUukwRGLgGAirzvc3WIzL__OAtIng1z5SXlGxoRr7t1F-mkzPcltAlNRW_y_0DHTT9a3GfCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=CEdBi6ps_ehFeMb8sg0JlH27Zh7mVMdZw60qV15JzM0J65L-q4HIi20TX4IkZPyDA3-GECXdQicDn5Ra_m0_S8ypVpOu8pbaQMzCMDb8czqhZaMGkV_AIsnIiVjIZFYbFICtQBz6y9gj22Y6C-UzI_sckr-K7wm_B2ZgHrITwj9E98G_QiQAtJPJBCMRLl0sKoWEiXN8h67dOtySmGWC0hvMfXL6_j5CkKy0Nr08V2Ol68mb7kA5sX_Rt2Q75aKgLz6izPUzSTuzgOUukwRGLgGAirzvc3WIzL__OAtIng1z5SXlGxoRr7t1F-mkzPcltAlNRW_y_0DHTT9a3GfCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25963" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25962">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oxx64azoJ9TGs7x02ztp0I9gn2HwdvPr9urp9zEZfbxUIURix7_Q10z4CYoJKlud8Bj8VNxH2w6K9npu8o8Q-vZKha74EPsLnx8rHTNw_q_X2811ZscMnLsnpX0rKAhNqB84pLj0oT6dD3VpC5FSradxwVVMk29U1UDdGBIkHjCYZC6JIhEWOLE1bLQkRwLOrRkzBm8uVIVU5es7Zt6jKoJFRRCD1EFP6yW-0ipeBAfLpRVEQgd6kE_G_K2R4yDhMDsA1-79LtXWF6bfWWji9OExamn9LNxOz7ZRSXLipEcFUgc2oxvYHTS4Rv8D3mDONV_pZ6CIbM4PwiUknpEISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ همانطور که در روزهای اخیر خبر داده بودیم؛ محمد جواد کاظمیان وینگر پرسپولیس در لیست مازاد سرخپوشان پایتخت قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25962" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25961">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj9Ftd6AGQBnGnM9kZ8IOKWkZ0LYHZgeurzffAZ9P_q85msgz8uIZfe57-mzntswE5tJL_Hciyw0tyvXhpd-22TUhf2s3ObdFt-6Ek1CGiJU3WefQPO0SZN1OT64Ce1_5eiZKGuWukZRRYrA7qPVM8UTgOuC5KzT-elo0QVuMwjrRV_tjyYqxsW9dgXG0Qa0ioMXWn1hUUIiN3kMflGP9FfuPOdQp6tfkWa38Qdgt_WMRnNfMtE1S5_Orrg4cxO9dh7CI_yIZbU7QDiZRbbho8U9Rdx_Wjf_wDe0gfytymDfTWHxZOBuxqUTk6fMomyIa6umWwJ79lqTXsTRC9PV0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
با اعلام مدیرعامل باشگاه نساجی؛ باشگاه پرسپولیس درصورتیکه رقم‌مدنظر باشگاه نساجی رو پرداخت کنه این باشگاه دانیال ایری و کسری طاهری رو به سرخپوشان خواهدفروخت. زندی اعلام کرد که طاهری میتونه با قراردادی قرضی همراه با بند خرید دائمی راهی پرسپولیس شود. تنها…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25961" target="_blank">📅 09:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25959">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MD--kGZKbshHlsK4rRSOF23POeBYyIUQsxzSOzuw905tLhEsbS4cKjoSvfbZdHEz49li_6L6lAQlqwqnWaFayFlxct6lS2TDNTwG0oNSQi2hYcF8sov27Yuw9HoqTg0jQlp2eGu4aNt19RvPqZqDybA1HAEjD4hXB_gJJA6nkRuEe5vtL1DzWLGrxHNTw9tRLyDLU2GhIvJxXaYBG-otOjOGDLJzd4iLXz-6lN9CdIxz5MbIKfLjaC1D_qZrOgK4KuYW9hzvfaf3olM90-WpDuvoAevokEM3hwZikg8Bl-C3kqd3fzrg7LPSq2rsnwpprjp67Ul-79Z-C3FinEMMHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها مسابقه مهم بامداد فردا؛
رقابت فرانسه و انگلیس برای کسب مقام سومی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25959" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25958">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRFWQDE_dUk35a5cNmICijbceF504bYe_gKAnfnfcxSQUAIB6__U_KNEzkm33DtgJxy0V9vxjkRp5AGqb_4twRPxlhxK9vxG2lbYOAbTrPKA6LEf-FpVDYD68ZhQ_6P7ESrXO4n9bstPYqNhQjede2gEDm0B4FqaPKz_Q8A70b9zob2NoLEgcL7ptwS5MMKA1sUq8hj-JDAMjitMcq2vzYFhBgyzUQpIXZtH8_xPS40ccpjodZouDL0NFtocfKpj8Qf9Jx9xIb93Pw1CLsXpqvFCW5ZxS2DAhzXgIgaJgWwbvWarh39_YYv3TF-pG49F1pKx0sxRsSqtJgiBZl1sIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغذیه بدنسازی‌ویژه قبل و بعدِتمرین؛ چهار گزینه پیشنهادی عضله‌سازی عالی برای قبل و بعد از تمرین
‼️
بهترین‌تایم تغذیه قبلِ‌تمرین‌بین ۳۰ الی ۶۰ دقیقه قبل از شروع تمرین؛ بهترین تایم تغذیه بعد از تمرین بین ۲۰ تا ۱۲۰ دقیقه بعد از اتمام تمرین
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25958" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25957">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=lQHCpGO6bqdOttO5HQ58T3I6dvzSXnEkIg4XEZ3GTXLzdZL4qA5oHGA9zXnsAy5Kvpn8blVU2v31uv4Zg-hFX89IAaNM1lUUVzb8_vC4-JVy3thx390QKlaMNgnlS4dz2a1tTZGnOKLIamHJPnnpvoIG5agiVubRFbY_IPQ5mPoP_A4LDqT-bGeBHpHeGRaLaiZCd7ZPDHPYUJtUoTKegI6MZk42gEUhGny5JX_v-q4OZdrD6raDO1lnG1d22WEus8o_EMtjQL3R4fHM2CjEGga6ipoQj2LOTxDy_m0rDINQ4pX4-8DyBygNPMUNSMdqPbEZ-9QVSpAvI5mqRZ28OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=lQHCpGO6bqdOttO5HQ58T3I6dvzSXnEkIg4XEZ3GTXLzdZL4qA5oHGA9zXnsAy5Kvpn8blVU2v31uv4Zg-hFX89IAaNM1lUUVzb8_vC4-JVy3thx390QKlaMNgnlS4dz2a1tTZGnOKLIamHJPnnpvoIG5agiVubRFbY_IPQ5mPoP_A4LDqT-bGeBHpHeGRaLaiZCd7ZPDHPYUJtUoTKegI6MZk42gEUhGny5JX_v-q4OZdrD6raDO1lnG1d22WEus8o_EMtjQL3R4fHM2CjEGga6ipoQj2LOTxDy_m0rDINQ4pX4-8DyBygNPMUNSMdqPbEZ-9QVSpAvI5mqRZ28OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌علیرضافغانی از علی آقا دایی: طبق قانون سه بارپنالتی علی آقا دایی رو تکرار دادم چون ابراهیم‌شکوری زودتر میومد تو محوطه جریمه من‌هم‌مجبورمیشدم تکرار بدم. علی اومد گفت بجون داداش تا صبم تکرار میدادی من باز گلش میکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25957" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25956">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCVWo8WLEf3D-D7Ydb9a9YNM4xpxjefijpqO2dzrXMVjLnXm7P26z541wC05jQ83M2tSfUcvA7lXDi1ZTl6F-41c8hi0WHIO4pn1BKaPRqA4I3WTJ4yd9Gl8HoFli-68kvyw1BMJgGVP2pOGq0pmCPSU_KHdBmz6Z_f5HnYdnp7FYGucpDUek90HEpURuIBou0X4rGniT-P-cbfVvgS2ZrX19hEcEdzjaDcD2_aGWZHdb0do-Cu93G4zy9VMEeDO7JIpUp8cVTo97pMJRlB117eQyh6wUo1-gfbldXZBg34d5Ed816ikWRO4J1jIia9GxSb-LCxjeDKgb5-943OSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25956" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25955">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5YkOOKsyCNrscR7dRntMQF3szlPGnz7RYhUU_rWN5rLcbMtjU2fKVBh6hZsFIypdZmhiKpSIN1yA8HOtbN-eIlqkK648pJUiZYs8GVc0Si-RBhgmqoeVXD8rDtJ8iun727OeSYopMemXE9xWey82EwqpiQLcDNo3FSEQ1yBK-hBoMI1dqa8e0l_Wd-k4mR9ojLCq1uuq1bNnX1aFbbMrIfFkYnsbPrJYy_s-DhRXbw_rEz43QTlL6kv6oFYUinqIDxAmMaZzcQKUv2loeNWbkNpmcFCOOFlf2NpLHb9VSRMx7bf_Tw00vi-WtpDlL5C7ZMsL_DXjHOz9faSIwE4jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
👤
علی آقا دایی اسطوره بی بدلیل و تاریخی نه فوتبال ایران بلکه‌فوتبال‌دنیاست. اعتباری که علی آقا نزد مدیران‌ باشگاه‌های‌ بزرگ‌ اروپایی‌ نظیر بایرن داره بازیکنان پرادعای‌این دوره‌فوتبال‌ایران حتی از نزدیک هم استادیوم بایرن‌مونیخ رو به چشم ندیدند. زیاد به اون…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25955" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25954">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7RgXmrK3TiCsXJOZVmO8P9Kvt9Fwav_C5WCmiqlZFCkux-L3sX1ck9LgSEtLLb9QLO6iqIbhR7LZuDgms9_L3kARmQUqEFkAZEMgyd1VaEVEwz-SikQXZPXD0QkjC3F9Vvg4pAkL2bPIY9NXWjKmQh3juTU8MCi0y0LBDEWee5-XtLxZQUHfPBDC3jA1oDPoFppEmVrvUbPYwKlNefhNLoP24l7wT0Kx8HJu4lT_0dSiG28QpwtTbAr_wg4J8IQ_tTeTsuX1gPxSqDbTV-5SzPYFSwT8QYLHShafnVa2kanGq5Sh-gviHgXqUdP-l-S40iNbRbod-3M4WA45G28zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25954" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
