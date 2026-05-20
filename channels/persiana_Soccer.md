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
<img src="https://cdn4.telesco.pe/file/D6VfaKvZWakrQtR8I5XWjl5jUbfrBFJnSsBM5Ubs2ZSc-wECV5nJX7LMPZYvmlSS_CBq5MnSAwvzaVWA6Cem7tzvSNKt9IunllwgAZmEVP7qoYqhpHHrODauVbNFjnaZivgCL6T3rAziZsBhP9InQr8tmNY_xZi_bT3SHi7UIQByO4dFa29Nf2Jgnb-H3xREMeSgUtDhbZBKX4_Aaw3-Qz3Nk_68Fyntp8c_eGmXWtbpEemEub4REC9dGpVKYhMktNh2uzTPIAbMxaD7kpDEYJ16xOZhUSd2kEx0aTOw-dKHP-gGpYJ2lYZuR9ebMLVLQRwm7B-oMegqmq9CQ3lJiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 203K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 17:31:58</div>
<hr>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lP0yx0hhl1ztyHrt9ERWKOumwuin6RVET6YKmxscGey6ZBgGyhuk_9TsiImH5VVt7b9bUmmFOpSTSuppPdmptY4nRydDyop2xnKyPLCUJwZrFgpeh2Gpx_SESoRdokALd7RAzKu7WOchzRle5tPBEQgcksLIKmFD-uw9EDYpAk_Zjm6_w8smaCjUhKu6Ou91ck0lxZKqnjPgfGqJxwHpoX4JiHhZzCbLADEWRYuw4abRRllZvO_NqOpVwTUvw4RqCe-xR6YTO21rsNcRgBsxea2BogV05m_LBgxEozVIQneHJCIznOO0jSzCmJ8aQrCJ7yiIcKaPgWFICVapC236Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgtw0tmeZ50w_RNkj9yBzKYmRTYgoRtSvP2Dp0WPmwxhVXmYIf3Xg1BMDbhQgLb1sgi6kljkb8Qjo5JZNH_ThV9ZYr0J9mlgQhDa_i8_rriSTHuad6XJQd6yJwzu0nJk1oDf8p03Fpa94j-r4jpqzpqakISuD_m2MVZueyEayWflHFVZzAKsMvrUhXDTpnNoElqVu82w_8PginJTwpW6KwI19DfDlw-FphdOuwPl3-beq6_WbBsaxkROWcOI7sMlvyaaKkq8vldPvZopYZwoYc-uwZHV0YoFLuEzYMHfem4gznz5MwlcRn9kXJhDN8H8Y4YlBQXSaW2-a79ra6acJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=fVnvWR5NX39hpUOehW6WEAVe20KTPjWjXMFiWtDI54JnSlX1bmGiPofiU2QXAyQLV9w7qmgJOdJUHxF3Uxwjr0LVdOfyJW4qnaQqddWRRCrSk-ZB3_z059mf2r5mnseEJv8hqZDsLcHcHJH7tYWGGY9BtdFMFvKDA9k0xbEDpBPXkyb9ZwLjDWBBgdvxN3cUEaXO6wuUMoHpuCKYNQZwNE1UsHnhV-3Fy-xkhAm_bIXm3wkyYVDv-wRu7s2cgkgFr87uZPpNXcI_IoaKvyZy1UuGiSlAHPMVESrqaIwD8bblPebyJbAspVH3g0veMZguq884rJpY6EjK7fV9vX2Erw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=fVnvWR5NX39hpUOehW6WEAVe20KTPjWjXMFiWtDI54JnSlX1bmGiPofiU2QXAyQLV9w7qmgJOdJUHxF3Uxwjr0LVdOfyJW4qnaQqddWRRCrSk-ZB3_z059mf2r5mnseEJv8hqZDsLcHcHJH7tYWGGY9BtdFMFvKDA9k0xbEDpBPXkyb9ZwLjDWBBgdvxN3cUEaXO6wuUMoHpuCKYNQZwNE1UsHnhV-3Fy-xkhAm_bIXm3wkyYVDv-wRu7s2cgkgFr87uZPpNXcI_IoaKvyZy1UuGiSlAHPMVESrqaIwD8bblPebyJbAspVH3g0veMZguq884rJpY6EjK7fV9vX2Erw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceoGJv0ojutbhZ_2zF0TVaYus1enO-qRE8nJTmBQZnevPOj7WcjJPKaaMjySA-xxGvZcDfsDh5Eg3AfIKXHNyWRsa6Z5zgg4mkSP2tjH_AYnay-teksMdmuf7N2Onne3Vdv2eCCTIR0hCyyLw2kxzdWMgpIF7SUaSwyvdew3rXj8hB9w6jfgQ4ycus_kLpM3JOxJX1NOdXuL7nIEetzUV125AB37k177R3W5Gj5Q1mQhT8NMde0ltrcSkEL1re7q9e4YWcDuD2UU7aV7ZzgmRd2-V-RP7IGklSg6V-BnYh_Jp3mw3HnYQ2faLVHglWFAR-SentGgx1SXanhcU3Lkew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwqx5rh0Ongyjaa_IrDuVrgcGoKx_Dki9WXI1OnoV_jwVX76LEPbv8afKzeqdsGhlTQ1oeDKq7j5YpPkKWAV8kUu8O5KzqKJImxb-OJedd8MKubWYj4vFcnaVfhwBwEjCymxM7cPEfkf20G_JJJbNOocYWcq6OO244Y4uwU_l9EEw-Yfjp061-yRveiqu238i1cOUuGv6rX5PgrrNDdL7COdg61w4nKOezgmQBJn8AMMr0TOOYaplBqcFoX9zU2dWcjTq46wHz7M5JImKniHZI_h5rKmA63ldAznEHJKEjn7AcP2fPvAXM1VGmc1QYAwJEZ4bveYGmBzgv37-gIHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZuOYyx_uNxkqSImfVZzEzQEssr8M2bgz3C8Z9PrClRpGzudHSOyBOTgfdgPV4_kY4d5ofqMRIV_obSEZDhu6ua-XhBruxpXcnoo9mB1XlZ2Mc23nDiNeo0lYou_g8g-_sylE91xqUlZLJxLCwbAN_OWQltmIVTYuqZPusLaJ2exxePX3-Ss2Lf69frlCl0L5YQwbpWdH-22Iv68cg2aK0jVJozE5liG7BpW_hkFpu8h4ktEQXR-Ei-frWYrKm9uMIKqQYAEwubpr_YaFAOLv5Cz4qUqQxGtvkKMyIvHTN9zdwdgx_0K2v5tZn9wTaY_LVUNOHhfBuTccVKp2XPCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_pLfTPtv7hX0PVo4PP0E5l-het7O5Y_uyUCAE_Tm5Bopf2uadgqEMrYCQ-GBcp-dlv2C57JBrPKAz6q2JfELD7nFq1cz7yef6oHFx_X_2HJxhpWlXf3d8q65hJkx3u0bcHWgevsMsqVjlAYrEfy6INsem1n78-OCtvQyA3W3BnC-9scZZPd7Vcw0p7iQUa3YgBx_cw0y-4keoX8oI7VHFt9h2-srfO0k_sq8MGF1Db2hGwgRcEJwxE0X9c8WQmWUqTnfJec1aWOrRmoC-M5EeBEC9OLfmp1dDyAWQafTam6jFXLtJxx-p__YIiLyqTsJf9AxEtTRY8TItFZ4CNCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdtxRLVFMpp2LgI1210AbRrOQx5ds2nrLne__PyOjheXSZ0JmpkCAuc-jfflwz1rjw7XdIKxgP2aJgqFfgSVQimNxVjwWgPeXkZ4KVw1f-JINMhxMwgRGU6bMIyMWnZPx4brMBplCox0hTN1axjkI2Xa2okEZDWcrW9U317KDXVv8oXwmv7HRWeaNJPUzP82X1rs643QLD27EEnQj_sLSAJhq8cYksULlNGMnKNqSO5dTz0SBlN_y-d4MbCpTVD6ejj7kL5ol5ldRhxPPIvU0Y_hK5MFRVXxfnlpceDEmY5W5_mNblh-UIigVmohsPpIGO_YX9KPG__qOk0DKQiUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIaJuF4sdJkVUO1yoieUQmnVkE-yCYbJAjQZVgshYLmT3Jiy32VJS1dgB2G2YeO88CZdT4zsof6xYq5IyZwyxtcWVN7X87uZeSZstNi5TtWyVHvCaekW0DXEOZf4_mgMeafd6-wsVh-dKFWP6Bf8S_G2gqzzAKWmw8aRrN8BYHZFbnuJqiFILiyh9389dzt-rLjrAss-GfahMON2gBRQNrWd2J5N1FQ9DSM8Kzj5b_7uLsQ3ejnXWEB5V2kxBy9NExRaohd_Oka6AydJs-2jxFj46cOgDbeu-XVeLsaxy7azIvirhpQeCCf3uJP1RwOncO3VYsqjZucnaJxTzYnwSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me0Tkz5ooEnqVKZFCA-p5NVfKiU1w-rReJnKeJ_d5Bc3HsguUZlryRCaQwbExBCztSiMvPkuAWrQDuKTDIOd4y5rksxQegY0gFCetCFVTp9NSWpPXr_bjFNlNNi_szAk1pdwVjS5WDzGGcze5NnSwAVYd8TBWBhi5BBVDoenfzmQ5UW5HAj2o2eK0eulv2HxQ21i36-bfb08lWKowTBUk9RTCrUMyrSzqrKn7Rf1-6qgvNdM-cm8uyn6gLACby5F8Ew5xbL3SUKPfq2l1VRgnyextKiqYBqC_KY32rp_fzKeqRqIJnCAYyK-nVh65LwdnwTBjeLDk6l3BRpiDfWJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwux93A2rCIMYoWLeMZ25KE657UFBLVXn_euMBGwOCqQKCghS9CTNtinsbzpwNfsNUUagtiXUljvy7WvsiJhL4u2mq4cIff7Yd9kWB3rOmNJkbRsUZqne0ja92spsRSmEhI0yQLTUu-ivek_qL6wELEFY8Z9athPjJrKk45YNIGnHKiUJmyFap6MJ-BINcvBry5SIHzmSbH-jxUHrLf7HC7mAnAi_08cdMcV3Nfg3t8J0CZTsxVscbiktfOXSFMFTXL0yGuNWxm_gO5BtmHd5IDAq0y1LEcb8_PlzzLdMH2KLFYlo06pkrt2PRHN6ThThSAqVHG09_E1-QT3uCtoSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7hBI9NWoFKIB3XyPuUU-LQ3RRwBTIeQOjJ_z8-wjW0pMtUY7XbM2KRhEp2Efip8WD-ghxKCvhN75zQ5ZZLVbXJ6D5VdQt9BDXfpVSKSRbeksASMbUwqoU4rK5Pwe33oFcMFgrIi52hY3fwOSEQ02WWTI0PC9_wQ0zGhwsc7cWYjx26c_3q2hr12Xch9rB_Ebyud4d1POjSe1QTLcv5uM-fbQlVqwnnVu-9_1Gt6A__86biO9vuv9m1f8TBmqhQO50xyJjjaJ_kUNE-j_AvFo2Xdylzfl2jLTMntnMAgJAYZPbcpAzNWbWFf-TNp36SzUUSHE0dIhLMgIOtQTpaLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6ofVvfNyj-aWA4j9haelPesDryqX_Fc1pTbuINNzIujxK6gCyWXWwBTJ_tNHNhLIUxa76FjvxtfFzz_jIGouZul_d_kMpubywbcuE4_CU7fiqpEr3FF3ZWpRLkREpqNycGMIfHEffqe58v_xdoT6vxoMpmq5Mvgh68IvXmqOyT47J128dm4ZAD-lRzTIafjOwxe1ZpXpfiuFJfBF18egL-GSRe1yHm7JWhlW_LWdjp4dv2GquErVxT4ITZhgp7LabVW2LQBUjozhI3qbwJQjOvXBZ9Swn4HuEK8CfJeHiiEut2IErZyUUdkTGhVFKDNHy4plp8cEMl4UmZKaRr-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgJWnisfCNaCVdujDf9cy28xWwbz3Oq-GGYDB0sZxAIkjl0lgVK93JVVNWN4P4d4K6IojEoCFiyN-8zjcF5IMqgVT9uGxsYYCUxa-oIqkztVgJSBjE84kW6zpnFWmH3r5G_skryoRLhDwiskTN4kOT1WvmqPZdDVkOFLfjJtKws8MBvbp2nLqh0wKO4ycn8Jl0tvW1uxkJT6JAzL9G8eElsScYvZD5OFotHrVijNM7TZ7d4qKCypBuwEaECAYewa3U1S_s5v--_0jjD77UMTHfluOcZXV2nq0CS0Ab1SZj9yCuBIRH3kMy3E8zz8o42aMMk8_24Gr6cTPcCVM5Qykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=SMSgThEq20KoBrzp8Suut3uYEP-LUQism5ePmrtiJWyHXr9zWU76iLHwcpYInkXk3JDPNcZIJ-ZnLb1T4-3gZMsrZeYtjg0EOKvYTcoPRXZLYJ38lkb_g-pm9VdCVmcQayimT5-pU_TMElwSN_tpSYvvi86Atcca-o-cp_PUnBY1wFmFuRmJKQZpQYX7xNXXP1IU7EWgK96XzIQBqSo7Gg-KwL7qk95dxeB7QrzjN-71htvWEBvCXIOLlNu3nIzXJSZ_40t-ePUdsNzZ26EoOEw8XMd1Z3h1d78B91LendgydjpId9i_w9rTYH_nPqz6hag5MNM6YmAj8EZEWx0_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=SMSgThEq20KoBrzp8Suut3uYEP-LUQism5ePmrtiJWyHXr9zWU76iLHwcpYInkXk3JDPNcZIJ-ZnLb1T4-3gZMsrZeYtjg0EOKvYTcoPRXZLYJ38lkb_g-pm9VdCVmcQayimT5-pU_TMElwSN_tpSYvvi86Atcca-o-cp_PUnBY1wFmFuRmJKQZpQYX7xNXXP1IU7EWgK96XzIQBqSo7Gg-KwL7qk95dxeB7QrzjN-71htvWEBvCXIOLlNu3nIzXJSZ_40t-ePUdsNzZ26EoOEw8XMd1Z3h1d78B91LendgydjpId9i_w9rTYH_nPqz6hag5MNM6YmAj8EZEWx0_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuoFetV71KluTeoswC1gAqnqBoG0558HjBOkLrEQaBFwBs1BvTTiNjjkvAihZyZiUxR5YiDBexVeBf-JkJwDvtD2PSpvEJYCC8Dv-xz4cIm0KsKx2dHgPF5R718465leRUL52IZwRV5wK1qSeN987wrJGaoaucA72WuPYmZ4oYfJpF4MWnOQSKonTSBf9vByHHonpY4hutozQRvhE5-PycZiRAswVqWEv-1utwhTGqhp-JY9ReUDDMCeRvQ1s27Z9p6LMZfKbpirA8SuziPQySpHo3MvqKfFPgYw0v_pLLAXdCm4rdjfUfpCq9mpq9yknBtifaFO7nUjky6c7iHweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJdltt_4g1ii4pqVrC7O4Zwy3K5nUFZQO0Dr8l9Ju0b3o30_6-Ljc97rwylZ6BsOGucUQl5taMMmVca8Fpml0M8ubF5dh2RINTuYk_HJ7Epd2oD9cUOMUV7B9Ybjq4QKj1OCaUAjFxPF28HtRf4dXMKCVLwd4N2lhcDHfxQ0hG5AFTEIvWhHSjY7tM7H-a8UCICn_IXNNUQqE7YmH8ktzcAph5RZSB7KUL7A1blSRb5sGH68o4LF5nvkER7LHmfXBWZL2WxEbHPFlJFKvnN6DJ_v3eXecaJLqQs2B74CaDFrLKD3TIyiEbmxbKVEE6Nx5mG75cbX-TrU3is8HsQQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ4WmTDtq_LXhgtjXy1IFKRgzdQRcdlYn_bbMS_S-EBKEpOI3tMMBZyPcDM3T8K3-XtELdvtDgrDhREB5cr9ncvYuRnrC1209pioHxn6SGTIetLM4NZWbefbU_458BcecpBLVkezshbOwDNFzEsW5wI4Ff8U-mt6WGowJshLLNZqLbzUfC28d3-5SrfvUeAp960LdJazKAj83vAA2uaEqAXwOQE_NF7JM9joNvhT6pP0sxEakzslzNDCQ48yHHJywy2C6YUsJ-l1OnQ9LbgyzOT8Goy3kV5qPU1ee1JuiDao3Pao89LKDUj2A2JHLK8dxH3xywNzePu29vQFFx7E6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfJEWFFqT1NWUJhZqD142UK2H8LkNoMmQTEmP99cjfiNktQPZexOc9DG3v01lktlbkPdYV2XGADdaUlaKog97RWXXbnfo4YdpqMTGNNTn9B0TUTHaPrSMSas4LZH1oeygsnUC9sQoPVIqHe8L3R6UW3Rg7qL_vXjwtuwAXwQHrn5SI7Z88sKXVJi3K_oDz4V3r4nCKRz0PxXU5qNV5h19O2jUI9dSNvIvRPXFM9QOZNCPwtrYKFW5rxfc4qDWkxiRB7yuK3T9j5yV6DcnWK2GxKQgn7NGd1s4lE_SihRYciQkYHq7ifPzpjqD2rhdCFE-PfMgEMVU842999-G7gCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I37bbwMQGWs_8PHy-ih6i4ItCZnZugJxK0JefEGioUPtopFUn_SZDRRdSRNrd0j7UuvqkrfUKzA-QkMAnYS83eZvGmibF5sBztx6d3AwMIGdHj86fWMR4SV7po_BmGb2eQdKc5vnFIuAfP-7EdgsEOSQAzTCxo3cRBigq009NQGvjW80dRxSlD7_oPWDfvJY_83q9MEoUuNfzeFkLkRrD3RbSq9zcI_AzKAJr34T1VfwCwIiqaDcrOdehkvFfcYKKzVfuvyeOgLCqQ5zZuFc1Wrh04DS6SxO5ySPAxo0CbyPGYCc2a92S_3X6YE50eiyPhcq6cwRAsd2E6VWI2IWWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورودی کانال VIP بتمونو رایگان کردم
؛
خواستم یحالی بهتون بدم هر کی جوین شه تا ابد میمونه
💯
https://t.me/+--L2Hz5HpiY1YWZk
💎
#تبلیغ‌نیست
💎
👀
کانال وی ای پی رایگان برای همه
👀</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5HATnomEAI4jlW-sixKvX585aXSFSLYL8-dsj1DdbncDRyNFATpp6BJPGwviUDRzZq33S2GlXLnnxUjs1ZphOONs8ZYcT-lmI7WXrS3Je5-FNUwrUL1hQd6jDjv10_R_xVgZ9-RjmwZm5oGbkxniMitjS82vwoIY12pVn0ZvkDux86x9y9GaelVrGR7o-KB7j7wgVBIoUXKCWsKtCDh6chF-wRlJQ-19oWPh5aEDpCbpuqLhJKPnClnF-rcK24vsBjUePewKtaQPY3wUFa5hPJI6i3lBZqCsuBLRaSarYNYShGInIwo5npGWVwvpk7Nbu1sB4xlYC3A5jd5B2jr2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrGPAeS8mqIweQD29brmOd-a8dy50NXHvXAZADPvLeBQL0Qhis4GO5fCVI3uls_X2I856s4zWS-z0plWvlp6L-8Z8AF0DQ2pQjem3-0mIQO9qPK0hOCuBCIcp1kk1yp7MFarnV55EIFXRMzji6pzcf5fAhyrxRw4ulwpJ_qrSmRNApuJ3L8MzaGgf-FKb30YQAHE94Oxle6O36pKjNY3_9iVGD5T-yNiHHvM5l1ZrHdDuu7z9L3H0ZZvpu3ZOhL5SH0xMJ_1cNOGSifNUMb4_fHpgTnZ-rmxesUxzupxp8rSbOodJs94BFNHJ1S9cOSN7r8BM1Rm9rN7XizBUyW2ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APu0jznb1uE2XQ70wFhB9_tpK3wGv8402n7zZ3cZ16E1kiWnd0J5GRfXNXMukCi8edXeVnlpnBPY8npydPtfEpMwXZJkhUrg1VJSuCP8zRyo838hn-bx_pF8NOTAd2rYC5VO2E8VgkzLoLSFnzEiHL5Cu75hLYM9e2J7YhwkHIAeHaCWgtWmdGnwmhA8QUUQEuW6RYa8Xs_8CV4CGmvRTIxXBrV5t_8qXBs3aTkk0uaTryS-ebEkPFgV7WZBkS7pnUcDu5-2sW1b7a5qKdZENrsw4eLhHwE1dBwMGO6US3xLTFyw50is3lVjdLqqyiDw2QGhunewf43hwp7USF_tjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ru-egjwRMRZkRntLHT5V0J3aclqXfgktbutz7I9quCnAJCkcf5sHgRjz2UZisieuWvZyN43M68laCG4zmP6opyHk2Euc0nkcfYLT8uvbxF59zcBIZ3O04LjXTnBTuaeY_X6sV20wMWNLKfHNO97V0dEwE7AOIyTg3pCLj7Dl8ejP3CQ_s9FcuK8KxFla7YQCPueH5SCGs8mggwrm0h06XarBgBLrkGzFYBInFY9vez9gJI7ERYddApN5m3wo60EoUPMW1YDCDnQLKEE-zc_mK_zkYe4BywwYXoC3xQYX3Z7K5hdA6iZtfMKGbdFS4gb5-BFr5hT2GEzZgdq8hOuwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZZ9ufDq12GAUUWJ0gpqrI0Lg2hivlFv5VVmu6TCwmuSK8B2Ao85jCgd-ffFRcsXGkRivc525JvhYFjdRQABhf7tiFSNC8IJywulYrpqleeoN-rahPvt5wCxRd5Ko1ffZa2fwrO8g9hYyspbkpfGk2DM3xWxkdKfxuxGRHHw4moxi6jqQQtfxOZXGM0Y-QpGBWl9Bf9qXvyMqnDDJ5FaTLzr6ebK2o-SlOOSF6Ir2416EbwXCpDX3yWE82KbUjD93FslVL10LxFnByXanPS0mNCqr3QNVg8ruU-gz-rq2KyRsx42MSv1Ag8X4hO_UGCB2_4dEwqHceNzYJYiyncUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=FIy3wb7n2l2KhniKxN3J7AnL6dU0X6CdjkTzRsjF5hS9GD7SVFaU25woN7e4bITz9TOWeJMC41qO2Xh2gSvA1K6P08GZl9hEDJ59wNH6-T-K5VGT_T6JlJJbAJ-VnvdyMxWE0V95Vjb_otV2Ub2E0cCCuwnBxqAWP8mBYjqN1nBdH8nP07TUzdZDhi8UbNYCTJurMfheJubHzFcg6gIo12-wIDCslw3i7jvlC2AT82cLq4C1iaSzaumoIyQdJAlgUUPqF826w3DRhuneJWZ8QksTD6-nSYtCWIfTgcca5ieRrPCZ0ouO2aHmtcqVOevMWW52bZLJSJGuq6g0B9wWDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=FIy3wb7n2l2KhniKxN3J7AnL6dU0X6CdjkTzRsjF5hS9GD7SVFaU25woN7e4bITz9TOWeJMC41qO2Xh2gSvA1K6P08GZl9hEDJ59wNH6-T-K5VGT_T6JlJJbAJ-VnvdyMxWE0V95Vjb_otV2Ub2E0cCCuwnBxqAWP8mBYjqN1nBdH8nP07TUzdZDhi8UbNYCTJurMfheJubHzFcg6gIo12-wIDCslw3i7jvlC2AT82cLq4C1iaSzaumoIyQdJAlgUUPqF826w3DRhuneJWZ8QksTD6-nSYtCWIfTgcca5ieRrPCZ0ouO2aHmtcqVOevMWW52bZLJSJGuq6g0B9wWDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=O9qWfThPutHodD5tgUBEJGR2XIztVAOUPzQgBKmr4DNwjxXHfAysz1MeMt2hlKAu5k47HOo5KBg6cz-DXGz6-akHGn6X58pOsfFOLVwL4yWjN59hAUNPxAXvGMYqUplAY4ktey9Xd-ea_dRGV7Z5K-7u3zGFdDGSTMOi3MD2YIPllRUJ0GPLQAN5y5J6BwPfq6VWweNP-lTN9TUg8djsjo2-p7bt-ci32r98-qAgJUEYtZJkpO5eG4uWf5YWtyFsK4ATTELXJE9uROA6Q0Qm3TV2Hg3xkT9MKdmbD55lfj1V-5lWrzoo99HcOh8A2psvHOC-Ez58WF38rPqSnAvVdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=O9qWfThPutHodD5tgUBEJGR2XIztVAOUPzQgBKmr4DNwjxXHfAysz1MeMt2hlKAu5k47HOo5KBg6cz-DXGz6-akHGn6X58pOsfFOLVwL4yWjN59hAUNPxAXvGMYqUplAY4ktey9Xd-ea_dRGV7Z5K-7u3zGFdDGSTMOi3MD2YIPllRUJ0GPLQAN5y5J6BwPfq6VWweNP-lTN9TUg8djsjo2-p7bt-ci32r98-qAgJUEYtZJkpO5eG4uWf5YWtyFsK4ATTELXJE9uROA6Q0Qm3TV2Hg3xkT9MKdmbD55lfj1V-5lWrzoo99HcOh8A2psvHOC-Ez58WF38rPqSnAvVdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cif1e5ayQaZ_c_1xogOyszWNcm9yfwKN0bIxTkX7Xk_W9up5d_K_OiW2AYoj8gvvjunQEMOe_f2fE9s78xcOfXWxUyibKUtY9t3IES9MaWaLxBup8TU5wm4PJbwCRsYSAg0Qv0ZXjd7LpUHtDjkvy4rN8DrlkGn6s1c2rtZ5e3vaFyJUECbB7KarWmRPHl_tf597m38FI8msvfhCbHhMvCV83GBLGg8FMAMkfmvkTXYApH5vJeZ8MxZflB_StAd-3eplqU0iNhZcP6jqTsnPRxyY9To1f8CDCkSO-TGyasyiTKDgiUXKMlCoR6I-snRBP-WPhaGCRbMwwuyszrIA0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD1qhKF16ssiQrEzLJPDMjbRelJVEEgcnidN6LqDordHYMuAWf7abi6bM7iI-xcd9mymS_h6idPnpwzcJjiI8f739fvH-hFyNk4dU4gnOtJ-uxWRzqbBQHE1efTbidUzQ6KNCr1QJYud0z43N0Ht7kGfB3cbj50szozGO3CiXi2U1FzCWpNgJ-f5Vnx-imr7ayV0qjNCSbZv4o-Kx1yRwn38g3BA6CfDTRy52ZGbXCC9rqWmHzmuICjCixN8Ec941v6BwdOK2fDDXcwcxw0alO5Kg1vsLckC762b-LQhb3317ITlnaOn-GNZCoQ0XBcNmfUdXQ_FLFt4DQT2hCbvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaghYcHuir-XlloynDE9gvFwLUrC_lrp6PWSGXcjapMJvHOdjV2fXaEBIeamjBoeYqXy_LigzjPp7GYIN14CaK34ThZN-ADKcU_pebWJy7vGmto1PnTcfHvjEdto9Ga3H6tHVCcrBkUUPCkkDrdsAaQt4gwsdwP5Ju473jmn3Dgr5l4abR16qdUXYkDUNdlDNdEzPu9stL-qkCV38vXeIE2eb3kTt_NNoPYNHmGwOxTspb0yDsBhiDoyYcCvxJmb8J8o0mgwz7zH7fDn-CNjd1iz5Q0EXYIaM_uLFhJ-niBRMiDjEoaj1XkkQXb6qNsrL_zg5_8Z7I8mRUMHtH4hag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_bnW-LHoA9dG-msnLnkKK7bCZEWyosU5xvnDikpGklXQUQqFBzpvAxs6Olw5T0svBomRr2JJcwYur8uoTOA3ibZwk5NQmHGqHhFfVhc6EYK6PVB5BKv4nw3-t_k7zanjPaguMjWBiiVuL7PRkWJL5Uy22Zan6pfkbh46wx55xpqMnSQprIFwYJNoUYAiW47wqPRaIfk3PsGDAzXW18D9Jl4_5gSHLpXs0dtIWh_SJmoCZrzBAn0Pru19a7iZHM4VE-eRHAclR-vfyYBd4b47_BcqwE9dOS6wLJ6nnK1fYuy4jYhpgPb6NEPadTI6qboS5AeTgtg5fukVTsyDjws-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff2he3lRJLVrMMD_t61_dR05Qk2dEBLD74frz2uscWFLoAFFlK-xWqIBWhuZI0c1LNesrYZU6f9BEXSigfOsZ4Q-WE-g24nek6l9aZ5ys3r8o4znb2o31wRanHGVcpsvuhBIfTZ0TGLgbT81PClfO-HQJfRaBs1Y706cC6oVBCUNQO4iyop5_rcDXrdZU5YTa11vNamRNPoJDcCCqVMSAdPVAj7yWIBdmrDHNaKgjXQ0rZOQjKHEr1uyd6M3yG33cL-DSimG1L9Fp1EuDoMnD1HlLPn5KA1iQnOPfqD_AzaLdVWyt7q6RWhmdJvpApjdNME-aYMZuNWFgM2y8TdGQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crlZcjW4OQd6-aREJC6KyZYNupmv3-ZU4sMMd9Qq51zQw4DddhcGEP23vKR6UxBQlDASsfV_9s2oLtekHAPAbDenQSWV4S7-DBD-mefD4KPuq-KhT4KKOujXDi2EeMWLIBNCZJAdg-8OWygAPsIwS5Z4EZlbsaq4GYf336L5n-EQN2QT9gy0BOytRw9w1-wqZJUvdtRKPp1nnP6hCd7yKcH18aNYJ-TM0Vvf-wp0MCAF8kKvsFJwcuv0qXs48ugCIpixKHRKh23Xg2GJWE_asFPFhjaZesCgkl0jRfRY4xpPxofKL044DFjoXOtMzAXqk84ZFVCmAlV5yznpgn7MTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsoHXWupH7zSQ7NpnhkBptA9Zv_vF9G_lpL1hxkFH9zypHFsw9H-tALrxFbZbh2bdabe-Q5sMuxxB8bp7XC99H3-yTOhlfH5_w_5zKJXl46VJt6q248s9xBLhNDbDE2zi3bpkW4mCIqYS1kagPAwmh1B23bOEMbLE1GU5UU6OKoMm272VwAaopasC_YJXLU3P5_L2YPRXVlz79sLE5TfrMK0w9JAEcr6sc_7LyUVfAZnT9tufCP0LMmFIavn1i3FK4c36ILxB_0jAjb3WyF8nIulhVWlR_oFTbJ3qeO0UklJey_HNSqYZwwLOSMR5y7NPxDfDVm0sm1Fl3IAdYG74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8HlXUPe1LIga7z2uF58G-YJoZInFGwx9RVQb_vTYgxP_M9os911j4gaQKiKhPcyoSfUQxmOnhhtylDANje-xStX9K7ADU8d7fh_8qZJTmrKWlcIrMhe_l84eBHRV1Nb6MvnsogfFLMsKdfDjKtyK2PG8Yy8y8AA0fzzegGJpaMc1qAz4xMtaSVW01Q7AQmueiJNSAwEQZmh2apuKQHu2fSCtJacO4KJulaZPBFnrZawFciGOboFJT2gzxBtE1EPgOtjyZIOjXcYUec8m9NH_BS2s8rOXRe5GG5i7QeX2_ay72FOziJQ4eELoQamCyr695WNrHi-N1FGZEqVOZPVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pggfy__2kgJ9KShdIhGE9IuWL8xrEF7N2HuYYv_ll5b7rmPxrxi6OdM_UyHYc066Q5AiiX6GndiRkYlvhB71gzfFOL4w5lZvnflMr-MfTUPZVYakEJqZ0QDZpwvxVmpnaxEIZ6SVVT8UwSpjyvIUIX7f6Y7G-UYnKNeMYy19GbE5eInLNgV78Bi599zSAM8ZTzAzLtB0wtWiXMdkpOVMv4zyHEr9tVwV6iDtmZ8qbUEfYTG2pzU1due_FwCWQ9Bby7mw4ZVdAhqJg94xpcIfrPTHNT2Kx3RBW_vIPRJOownx7_2VR_UImuOe_xaquGejNUuLG1l3n8zAtE1dkQMJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpwNIesaeDJEMAHJltWsie-G97KOh0b6-KpQCIIpoHEqjhHmJNN4WQJwJH6SzPfVx4yVimc35IkPIQ5v4yTNmM4fJC85ouZwuW2V6pXR8dPAFeo-1H7kwBSHjs2r83VDhZLNcXs1KXvqMC4SpeChT_qFgF8N9Qu0HoRVDdCUa_SoZ5pMKpQfRhMfTFSyEMPXh4zR09aZBCz7O4jKEwefObWmrcfdhs3OP3v_9uoYJpH_Zs1CSptq5oi5QKlIBMKQLwThQyvix27ambCpDfG0ClNa4xBY7KAtH8Cp6qJYQR7pitNAfJtPUQ7b8t06_zC-V_CcxhyKA3RH1Ui7atEHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqJsq0NmGUuEQZiEnXpxHCLnVZrRS19WqNRpGpW6hv3jy7hSD6TU-F3uhBhDxWV1QcMnTfrvtVlMkVQywg07gM3H30AcFZu-6WJlvHdZZnRs5o5MtQ1m3RT1x9Hx8HdRvaFvksbVD2jNz_DRL_QBa42aYDqlglVHC4tFfzOWntU2PJzZMmQSpgE1M8tCbQrQttW-vWa72g-0TQIl4-VVSJkAxCIvb6-nB9CqKOZUjnFfMOoNPCI6WJ1FanhIHnnXnnOnRyNPpQpaZteowwvlK6SZ9WyAnaDKOyZKIl7GxsYkbtAobVT_BsAeZ3XbCYcoBNt3fEkaJX5IRg-FiBY2Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWkYlSqLPBn5CfEGz0It_F_4NlZrk8_1QAQOUGSx18midm1d0wDX398LFMBuWPU2PWJUABqfnsrK0tz6hH7f4gnal_RiY8zU-fGWcgpVeHuiDYopg64IvXUtqwdEmlfKy5G8YmfzS7tu0aGKLUG5dHlFoK13nIkq-QAuXCSSAUL0CKOS2rBYLlJkA-yO-MueXMjghLy6aA_YnksoCAThr_-4cO2tPLGrHj700j7LapLbDWED92usEn6Dw559ol0gNDiPIvakI08-dnKxTogeREqRYtgJ8YgNQ3Er1g_PGz7uKFMPAWACXLGS_5hycMze34rLfr-dq-jaFvdzsrdZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aybc46zsPmbtvMcIbw9mtFIjiUDERr-ES1vcGoCdQ2rlXApBRC2r1rtky29qDwNyybKv9yfIfORWplnR-lFvvHIzkS6t-pQB20igLYgo0BmdV0Mk4JJO_n75MnHGNXRhEeGtB4QFacJZWtboN6xoq5GWUS-PXO5noMBYNNfssblgoc5GKERRd4Uhh-bye_KAjEtbb6Qt0cu3FYVXMjwbKIB3jz4BPYVYJf6ZLz7SRlnJ_m8wcLVC_vK3cdEcZzouW5_69kLOW9pzNKWde0cLuW4mNBPPOFJQhuDB9udhN6G5D4t60bkwqxsfVp1UfKos7bLv82lRjqS5k1BqhU7I3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGcR8TuXiMya5nNLqsYLemttUvet4KBpeOsqGiH-72j8nNSzsNrPkaGjkG7wsLc2G0QpiAHMtG5p21WtQnZulEOdOuzSOuefHiwoGf3o9FH2Aso2ss9WDGqPuKOGWRMW1AgJO6TADrxmgkPXQmn18Pjjwn5tUfoyfBI3qa2ahRG-HmW88j-OWhj4m6MWw_DuSz92Bbocf2vONJeCZF7Zc_u7O5GtpMx1TUznITQrRw_BGhHTFjOiSN2pUt-uc0H-0oXnNOrgiQ56UOXYaGvhkfsQf-Dxfn-E5LoPKDOvhTOY0f844vMZpPS7h6Vbp9vLppeWaVFllUc-B-ijnWbUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZfigSB_NpnHiphZYBnt14vVmH9xykJVB3jw_fHBDgauOMt_V6F0QAh9FZpj5ZqwNwnMhT6u6t7PAoczH-90GjbGuHtLq4nUnic-7Vp4qeLjUgcJG6fkRWsdkbuYdY6cwX-IpvkXV5Azui7VKAMD7b63ugZjdm-wRZk1h3Gvmf9eW39mbYD2cVl0JX1eQkAF0inU8diev4VXAE13An04ka-EJwDyT8zFgiVoXo-tDPwxQQJNV1pPMf453VdxPFcuY7t0CbCGrpP195lf_ncjYrd9ycC-ILfERZhV_3xM6iDPPFTn_qwF2QLbEt1S4Dp5Tckiy14-liE5Lvnwkn9x1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsJIDncg6hZjfuRYlcpnW6N8SL3vlzNRG87KGWym4TKnoOYMhckHbUC6GW082Tk_voTa26ZdF40DIhVdS0nWncb2uUwc5PjVW-ubL8z5QKVh0r8fVTAhWQGJrEuHI6Ky1knIASv9i0cRh3EFJ4fEQRgjUIbxZ-P-0vxOWF8g9PcQuXbPNsV-hmuTzGI9k3XxbYE4u58LcojKLdGvSbbM-PopvV50oc0PEjay8LEnjIT2fE0UlE3z1iDdVECxTJD9Rmat-hxoMdfK4drg8ijtjW7rhq8ae67fS9gt5CJzxiuNAKE1aSrHQJPCaTb8S-TzQPSqj12DeSf6BGQm9-qtJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qzlm2hFIDB71fr0NT4MRSqwN75zoSE0igqZjzE5FIqW7WWzqi8CBIV6hbVw4ujHe2C6Dc0PA2L1WTuvw7in1ZmyAAmVWwwJmo8ybrR5MyvQy6kV69sEBujCdYtm7J7Zi1HHo4BlfW_hMAE79BdHL8I4J1nAF3K3LrAKe7p067xN52E-DuXmHYqzfTXtysI9P7fgfbJWFjk5VsnHeDbbgFYm5zTpxNb1wiyYa44YMqGarl-Kpb225igE5PjYS1MihHq5jRqarU_5TrtglqlSVarlPLd6hsH-GINioJ1ddIG4whnAB7kBq1jW5GFW1HKXgTF5P3-ZlhNZHevpMt7geOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drbRZ6ev0Lgyn4F-XtMBHi0R4bFLVYHr3EchRRY5UklyKecuGxrZyfiXm_0SKe0Zc_1StSStuF_eF_OPXrtr_sLXKRiBLKFQVltwcF-WxU8ZUGHCRYzVaFPhzjw3N7TZhtFbWTBnY4RDX7hNaE7H1k9gdm1jxYvGTm_1PWhzZOreuWkHn-Va_EDiAIlhvYm0UfiuAhqDk4a7UyUMBfJToF_LzZYxt9DodVOLMImI9nvqb7tQu2gKe4lC-zJ-eKSC-KjNUGfG1grnYQlrFCS9d2ImgwpadA65LYu1PQ7lYvZ-oegUpRrUjuLvj79h_gESzJpzDqQb_BD0CTB5wSzWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEInVbEpq91XpOFQ3KyI7nDan5RK8RyFrf5cFGee4AihN5kWviWlRnWheZKTHiUbU8eb6sowUnE8WQ2AyyDyATOkOocmuY4kj7Q_rbcizH6yE8ja5eyrvwm_pTfjss5zLURO_P7Q0POQjBgrdZxTO9K6WN-sAyiJukB6RMb1jWXQQUiylLQvrUP2lJSN1KlUm0F0sG95ndjnsnTmtSz_YaKhQwFIjFtbZFhxqaisZ4DCedlJd3xHUiopvCJDRzDeRnEbofuhYYpq3WrgGkhTumgF_lv9ylhCTLHbbLxRAJRhVdDMXJueqwWDAK-OOI4XSXOIWqjtq4ycFPWAqGLdkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZYEtqQm0UgOUH8aH7K-YiBGRqFDwhL0qQKhvzB6kB7YVYl7lrlALsnfvQSh2t_Yo4EPWXtMGhNBoWCjruW-0m6gqMadhLjekKfu30Oo1G_zDlpBba5UelIBkBihQbNvcJsYFPUvE7xhZnt4ukoy0k70M1f08O8ovk38HI9CxljAu-pERU7eA779SAbhtW90Vtl0OBBEdBrxbvPRfgmBSfdteSVawTLGAUy8FzVN84B4INPfft1bWWWJAxAkan9y18i8ANh-pOCueJto-VGtzfXm3Ioi-pgdLZ_F01luvNwmyo9iv8hPJIsAOndnPpE0tiaO51Vna7q2H_0UvhaShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUV9RcShRX1mwYl1kimK54le4yNuL9xH86SvuWKBYzwc89K2hi7npbH7vugO6mK5Ddtn8_6pbrDv_mAbD03-dJrRkkilUr3jfIfSy2bT9LjElWLMSWRhTd0VxZliuUDfnJXMF8uxVWnNqb8xM-DWngdxNiUu4PViyAZ2xQInbCRlWDnSRHtjIXR37l0mD0aQibyDtX--e0QJbvgm-ktxrhYsQl8mzlltAs8s8uorSUdSk1YNwlJ1TNmkLOCoQAjVKqUkar-3-IFGRr_wddkqQUj0HzysxNHb8GUk86kv-MepmmiOV0JfnTQ_FcFyhxnaKkIqxmn55jIBO8IDtvycdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مانوئل نویر، گلر ۴۰ سالۀ تیم بایرن‌ مونیخ قرار دادش را برای یک فصل دیگر با این تیم تمدید کرد.
📊
آمار:
✅
۵۹۷ بازی برای بایرن
✅
۱۳ قهرمانی بوندس‌لیگا
✅
۵ قهرمانی جام حذفی
✅
دو قهرمانی لیگ قهرمانان
✅
دو قهرمانی جام جهانی باشگاه‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkDBCqlIiRvxtwF0F3maxrRvcGoxmSCCqh6mXMQhjX9W8n86NRxtPqwp_YZPy5IC0XxUxaLU7ZkVLy0U1XWyuR8RKh_4DMdoB9H0QhTn5VrIT2D1NuH_vffAU1c9zJQogfVzSX1GJfDMgYbFBNU5trenhRkwPHPadh23BSd74CQr8lYAHdKi6Jjm-FH7M1fWVAEHNbmmH18Cv4f1z7sroK2_zHgxr8opG6p714bwPeLYA6y_C13_DvoAOfzPfKFpCoIQUXcSmogf0jhf65Hvvo6M9H0ws4iCO63K9608d4KQNWD-YivtAqnrEB8qiZuiQP69xRO2uxF2QfyquT1big.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfILJv7HGWhfyfxrl78rUJbzZAd80FxXbg7PIlDQSF2sK6xk9ikRu-sPAj8DJz_wDxph8UJqoQUQeG-ADX7b7es14OPn_iNSWI6dLuwlcWDMlCRhK8BIY3JMLn7SubO1ZUeE1VP-x91A2_sKnFc7azz7cctc_tVTiyvBC5tHuxeca-4j4SQAj7bifUnnXlvYxlGybBi3bZV3FNY59aFYDF5TVPVDeYn_Aqc-vZWBLxxxVxbqXf5XnYf9OE28qur46BJSeHQdEkzE-_Wf48JlFgnVRQyg5fYLMMGzIY21t1OQYFB0W8TSO62Ys20-RJDruhWeVvjsPAQtrBeLttoO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB-OKaaFqosXCh_1TFBwKIm9dia0aGnwjyUM4o6scl_TMWWRWDaXxbJB9V0DAwmPdxNOf5Iv8gEuROQcD4oXi_eZLYdAVDpVt8kY5L0PqdTJtDqbAq0UY9SD2bZVfM9rXaiJ4TIRl8ePrzthHBRGBtayJO8DNYBPSNh9h29sHbVnE7cPmd8wuLVtgmIj_M3erzrT0KPsaf57niDe7gjVsuS-JDxaORrQmZXArld82LtohNy5lv8jVHOEyDQ_DdbaI_1EtKUT60C5OvSxDRFDvn900VF2mn4I7-5yh-_pXf9ltk-SN0vpOwBKLMM28WZkdB415JvaVr9LKzqseueCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAFP9-zaHL_VQX6zRIYkPy1xP3piupoHnYdswLkRk9-dbOTfWNOq0rPHYtLXEj-yUESdLgfhAQS1Lm5V-P--b7krMK-j-By1Bh-1Nh1u25_rGU_FeEJVDkxeIH2Q0gAuyz5lv_bGuKqrsPKgF5qcqflaVoFA6bLHJqPP-Hj7jQSJ9w8EvdO-41-7gdrBZsT0a6-3s_KyZPMqdyGcoF0Q-qYrkm-XNShLLyZtwGF4MPQNwSknB7NPDhCDQZQqqOPz16cufnMCiM851Tts6jJ8UbUix2FS2xUH_uJUZ7p1GvOgirLbY0fJHeNS4Ib_M97T1_BvS7ptJHVAwrECG0I88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmr_VDOiYyxm-zWdl8Vn-Bxxu8jQ274ipfkl0ewg8cJPG7x17S7ckfqrzQLnDwl3Mz_fmxsL61XSTy1ICpGWczci4dISJQy41NSSGd-zQH0vl8OdyznnLYeeskFfB0GW1NYimAhvwVfbWTPMUQmqM7het_oaHzZNFaqu7Cq3fvpj-sCPzQ1oGJJaTQzMCoXH7HTSC2w36W27meLuqUsIIgxT0rVkCadIsJ4KgLjchMGdY1EO8TXyGIPJBJ9bZMiLdiX_-y1EQWZkkJ70czF3RvWEkCU842DxYv0gBqTdaIX1ZrdkZBywRCwJiRyqB5y4fPl7jDvhG6gKARNhkV9_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuZupVwCVtqGV61I1O5lHiTpUBDgAO9H_ta0hK8UL4IH1B-kKXaG90QgnPyPSxgjQu5Nd3z9fXK6JoKXL1rrkPEF_UzRNuxG9u3-6CnYbVTXjf5zzrlh6YLIJFRiPlvORbw0LlRsGZcXXe0azChgVbGSAZxyGN10BbfHVD8NCIQYUP6yLtEt4NK3yS1z9N-2RTV9jboc5mS5o2RdX0Tfga9xgT1lOqW_wrHN1E14H1n4zx2rD33TtUkOA9fMKnLkZCHOb6zuKT4vwhuZm6OcZl_VVvQC7dT297rWPePQtLvcSQ5Nn3DspAN1a5XKXpxKunypwc0BrDC1lv-RRR098w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc3zB-bsCwav9GL59UlelM9vmXx4ToWSu5_JRpIBSUPwcV-YkVRJR7FZMFkBUsRaKz1F6w1m2V2WN7airHyIciY1wo31s99peBk0X0Azj6wc8ESls4qGP4XZ7LARijAd4dCzfPkfzSrN4OTsGlrRsU4ZZIq1guks6FoxaXm4kz9dRqHKlFjA8Jrmz8YzSxacAwJle5Ksen-rTuNI49k0ByC5ye8KiTfGMGy0F9r5_I55YAqmPgYTDVcYN3FSedcK2cZzpzxOs0Xc2p7lzgfvmmHFI19HS_3VjbXJ16jZSr-bhfDIKFAZqtZtJ9NloGjqVfTxBpqdZpLltHDcT3hUEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=d1GHjWZMm_BPAeYwThVAGXZZb6m0VoIMwNmFA78oveVEhCeLnTlg4aJtqo6afLQ1eT-Y6GfCtRqC6H9Uojsa3wkEgkakNPaif4iBglDqhhd0-VIJ3xRGPUin2cX27098ogcbtjwg9XRfwHNJYw36I0DfTv-8espdJYn1JNZyzOp19as74w2EwGuReA1e-TkI_MprezlvWWwX1A_KONIkvNDvhfOB7zZU-mG9CfzYgMt8wpHtKgPVndg0TeyHKoXcZBjf5vr6QO05fmPISqWFf2j2md5N1RZwTiSeOhfjiy0xyLC2VPDxlS7LaAHA_-hqwvNPSWPFidFm4XJ8HqmE3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=d1GHjWZMm_BPAeYwThVAGXZZb6m0VoIMwNmFA78oveVEhCeLnTlg4aJtqo6afLQ1eT-Y6GfCtRqC6H9Uojsa3wkEgkakNPaif4iBglDqhhd0-VIJ3xRGPUin2cX27098ogcbtjwg9XRfwHNJYw36I0DfTv-8espdJYn1JNZyzOp19as74w2EwGuReA1e-TkI_MprezlvWWwX1A_KONIkvNDvhfOB7zZU-mG9CfzYgMt8wpHtKgPVndg0TeyHKoXcZBjf5vr6QO05fmPISqWFf2j2md5N1RZwTiSeOhfjiy0xyLC2VPDxlS7LaAHA_-hqwvNPSWPFidFm4XJ8HqmE3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4ZWg2cNq9nL2GGr69GXjmJny14RiMO72sApr5ger1HRo2p0og_VqNtZ69Mahnqx6zzX2K-FAVJb4Cu7LmWM1zigzWpxNiUdB97BpNzFNXWlxVGHXsvK9WyxMFX9r5jgojSScQMiLCVo3YNx62pRQYzBWR0cDIi2_ApZqJkRhZt4GFskm6GTTuEWB6zjg7ifn8p_zbjtaWp3zxNYx0txALtrK69ZcpfTyYVHnnDkbmu9bXkl7obtPgx3Jjj1yVKSEeZ8do2YR17yHNMqg9mcV31fT1NVJtMbvcmNJyEQ-NkxpNuqb7LV-sZSddzcMTFh0ihijVrca_pgNTjp2ICg2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdlYuLLM0Te9MoMNJr_xjJ3gJ6rjlNTFBNHAhaVasAXehbPslzW7GQiau2xPXCQnGSllYLSd5hXAH__KfIWdpBbOeXepo3FCX4YpY61_AZ2TsDt0aeZGYDP13p3xFy_FxRIeQtxKKlp9_SBUzhuomw-0kXl8waLdVBYF1JBka-8PS7L1JaI8nR7A7tvdyBfObZsem7sP_Px8Q9nkANrMQQckcoFIMo4NFufuEKjBGzj5gUdblO--jhizLJSIeanY8MTqikmF1d5YPUgCSjvp8Nycml4ACpAJSnu5RWUFRaDrr0arzP-BHfZgiaiTGHuOZaQ0kpErOnS7qUa5xES12w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzySVEunBfwNTkv9c-Pd40FwIBIjd7_4i_xiWq3_uoqZ8T2Sx47OK3yrrbKSPhPEs0-MNwkFC2m_If1sQpNLEsgY_3abBWG8aQDnyJT84gi0-pAvoilTNez6yK2YhtCkrV7ykBbD8qTzbTLGpNd8P1OHISIh6GjFTorrgrEhO6Lu0q3suNnREmAC_CsTnKxDQibEDUQXOV46-DExdJuglh3puQ3fGxQtYyHY_aTXloJ31-uFB0j7cD5sQNAdu-t4p3uP8QP0P6XmS8CpPhs3U99QZmvH7Ziiy2OdDA3RUZOoQzOy45X3PPWIBL_mY4guMrf8jD-jPB9j08sNHq_O6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8HIPIZFAGO9ZWwIFo3DvlXSQX19Nlf42Ega0nKnz8m7kJRRQw1Qw1Ppg3JqXHZEHnXs2bOUlOGSLJ-4oNCdeY6tMEBvTiyr8OMYSxqHBkxa1zxHh6lyKluFm16y-asyDAa9SUCGjTykKDlXa0LMcd5eKSDk0l41GYs2HMKlCgCK3QhgNu1TJwwU0Tlcb9kxdVY6AenuH0P5_Pnquhmlj6zJJNnEAQO4N4jcqK-RptZhwYgkHR0YDzvWclzwSh0WYiYuyzF1e5eD9eRo38vn2RgNW4yhrPeSYcPEpEOi5ZtWRqnQ1nDOVxtA_aqqaHN1YiHeOiQinVSglPvyYD7fPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAVtErqzrTqvmPO7LsrFZLlGufm6UUs-DA8ezccKmxzdt1KaevzAkVEvRyR7mvPiJqWkoPu4M3jhwi2AR-Px5JeHPqwag0TDkgdHGEEaGmAhGLhVsV6DP6AMNQbJsTIZ-XkGAlejtKWWIx-3UTTUbUuihyoAX90IugrXexKxSgUeQg4C0rfsTn0Nrk1kQmqqPyuozqcCfcVMmSpSPd6-V5PCVgLNIpAkgECmInrdOl-NjmZv26RNi4FtTMAR-3vpP9vVkXf3WYQycCyPqmal9C8xi8Cp5QsZBxydnsoER6muT3XfTK5nUk0QekkUcAqVCH2a961IAummBVyK3L5RMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbOpHM8zsbjP_5sDQ1A1GMXEB3-6sxJdvzZ73mZ6FeYVi7QIBu3SVnSt7yI0epDXpUO1ukNtgDpzrE0A4o0J-qa8x9pBkbQKHhIMdgKxP1BOn-OLdxdTzqVOlg-wg3RERpgpxSKLgQS8pn73gIjl5kOjMLv2jWPmSVb01ls2E55CVjtEPM417qqcY0iH6y5Zam43TNBZySCGRUcnX66KouqBxCkBULsG3GxDBoJQyFHDsM-fxJD_Q72qa86g2uFxf9zD_JMaUJaKVMeL1h9t7SuAUqIZxwJWyxJ7M-NjRWPUyBYSI3gaOWBzdHYVh4IW0Sx1nKSnrYNeWCx1L3SSGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VykoDbD1D6PmnXPY-0SJWYpO_WLoywDa2G64QfK3oMzEk5QwgcMfrke6qESYDBKRhH7qYxOcv_h9OStZdriS6uQ3a8NGyr-Q5YgOtcHo6roKpP8NZmRlvxyETkUFBpEdBGNMdrNyF_HuDEnZdG3JwWnk4mPi2mMbtbbuOsdsdoFYG5F3hMOg4YyfzlnQ4mIOlQ1eZ1DyNk_UX2I4reNnrKrmL5JTCaX38gPsax_oTB0M8UzH18nRbMOzI8hr_Ugv1PRUOSPxhtWGko025t4jaz2T6iuEx5oXEiljcaqd0i1TluicCjAQdHwruYUXt7pKs4YgH_Afqxu6BfpCmc378Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG277TeG9RGPak3NK4Ll3jqExxgrrWGkPRBrH0W38xC-a_GqOlgDhwn5FEfpb_OxVz6_g42uUrd9ElRdfxVZ3AKMpFyI4t9CSKAxEo2iFAXuA36gvs7r2vGk7xMMsJn022pecw5Qw4Ha5keXdS71zJnKQMXzxZMUYHWUBmFTNRSt0RmWPIIaW_In_Mw8ZsEhX8gJnIOEtg65ElEKvWoM4JHNjxDcGo0QpK-V65F5RlkGAFyIRC-qFiuKc_XX-PkqX7MVIOdfYQCzMIPy0k9jkdpC-AznVqZhH1o26rwnuWn4tjj3SmtKeXTyCbc66HM8SdwBeN6P_qha_y3fMnJ4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=Qm8I0iRClrNukST8vAtjpYa69vSNKVUm1ky980s0kJBXd4d9LXFRy3LDfw61oTH6CATb7cX4XsP36rBCbuyzLpJG9SkljaJl8-m6h5a0zKREeBZBbatTYrI8whHwA2n-BmaeHzcDIblwuk0h4MmY6K3DNBQ-CHNcGhXq2DcXH6GqkfKhOsPZp83DaHVKE58M0CHA1UlvuLjGfsKrR8BNyAxQX6kgnHYcFY7ygJxoRh_azhLn6jHcVy4yDeQlbhbp92IjespgcBtgwYztvBlY4xAowIXb_Ua1jmcfk0UJQIM0qve0YV6b7iaMPoYx70YuoLWfT3fRWLLy2xoSmSHrQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=Qm8I0iRClrNukST8vAtjpYa69vSNKVUm1ky980s0kJBXd4d9LXFRy3LDfw61oTH6CATb7cX4XsP36rBCbuyzLpJG9SkljaJl8-m6h5a0zKREeBZBbatTYrI8whHwA2n-BmaeHzcDIblwuk0h4MmY6K3DNBQ-CHNcGhXq2DcXH6GqkfKhOsPZp83DaHVKE58M0CHA1UlvuLjGfsKrR8BNyAxQX6kgnHYcFY7ygJxoRh_azhLn6jHcVy4yDeQlbhbp92IjespgcBtgwYztvBlY4xAowIXb_Ua1jmcfk0UJQIM0qve0YV6b7iaMPoYx70YuoLWfT3fRWLLy2xoSmSHrQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJ37LBlum0_ierWzhInwKacEX_YfG6YB051ejeavaljBtPEzDbxMFBTj6k7fxjYq1-86vhPjsK9iIu4-fiZDv8bYDgldvQxVnhByr3LPpQO-GfoCh01MddWZUKCUU0C1ay1GdIEKhVR5-1Ts_yBLD1GiLuViy3qhI4XiLXsGwg4YKxiUO6v7yAadyNq0MwVc7kZytm6pYC2N6WfyERIHYeNPTG7HrX-nK8_Gn5KRbHYXk07DlSxbcgcJsr10gXAcH5_kLMIdZevjG1V7dQc-Lcq1JJl5Y91bveTBiYivVEi46oZxd4-1KIk4kIMIT0pTerbGr-YnUK455WOK80g47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyrNlfOO3sWqxOp7Sdw8H9ShVC_lM-xOyKUJTPXTljRigXmuy904pUUCIn6u7vF0tOdN6B-8vX4lduWUDNbaAVXPu0BE9oeEQ7cAKoOJBTTpXLSgNgfmCZRqH4wSWNdHkYVOS73TlltBLh8qxvBRryW5WuAQg2YBVDeFOAjlxQ8ZHQQ6AiwlhHvU114iAQfWVQlJjLuvXt0XllrDS9cHboO4IHtO8yARmzbq3eRVRBw5dUA57U3SsFbV6SXnhi5HmM2hpo68H-6TQx6b3yvPwQ-FGn9_uLNHbOiSfST2UPcpI-9uRctiL_2Kjmhch640bgjP6tnJRKn5qNuPY2HbWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=vqjvp1VxRM0Q1iy9rhAuBPig54Zn65_x7epzmsCMXiIGuryPdOqb9EGMPcMeYjsIdSEFq2zS3qAqOcLhiGDIso6FuPfxbgM8YuoE2lAz6SKNYkyAZHOzrGwmwyP805l-6FiHAa26ycg_J0RIVioYYNtSt32ZksEQuA5kB9jjJT9OdWPHp37mj5hUe82KGWYMeOHAnfHwN_5IJbEwGqSjOkm0QfkwPGvHEx1EPL966eDu8-gMQtfIezwkHrN61rgChqr9OR3grZIOdKXKvr-iqGzlEoVxVtKomsoZXjA-0gbE3KqaCrVS-1HYz5USnTE267MZEJ_Acw68wXl5HA66Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=vqjvp1VxRM0Q1iy9rhAuBPig54Zn65_x7epzmsCMXiIGuryPdOqb9EGMPcMeYjsIdSEFq2zS3qAqOcLhiGDIso6FuPfxbgM8YuoE2lAz6SKNYkyAZHOzrGwmwyP805l-6FiHAa26ycg_J0RIVioYYNtSt32ZksEQuA5kB9jjJT9OdWPHp37mj5hUe82KGWYMeOHAnfHwN_5IJbEwGqSjOkm0QfkwPGvHEx1EPL966eDu8-gMQtfIezwkHrN61rgChqr9OR3grZIOdKXKvr-iqGzlEoVxVtKomsoZXjA-0gbE3KqaCrVS-1HYz5USnTE267MZEJ_Acw68wXl5HA66Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3LWp2M5o7uEN8VXK0McbssT9Z3aIX5G8AtRkDBiVM_0D1Lz-Sh13u9LibleeAcGEnchk3u0phqdjbgcx2-9F6atmBc6tp7OEFromS8NL3Fz_YWfN0lDBEBmszF_meBeTEdqGv998o7ZxupvpWpMalqtvCMdUIQHBrJBm2ecIoJ4C1qMcyJ4cJCjgLS2CO2DaYE_9KGOtJ6mSiwI-MgTSmWTKAb6eItJi864zrTZiAKIyxkpWnXTvaq_vb-4QZ5K1fJlVccLJnirgcRw6FF-Tunx2wEmmK_rWajiZd-E66zC_s6caZ-n6KYmbLXuTmug04v4wPy1mI1BEP64CQXY1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/o1C9V2kR3T1x70gTwQahdBuQlaJKwaXKmIRioRL5MOVbV7ZcZMtG5V1V_xZzUqkwxB4p50-eWyKNYZUWytkjI0RyfNVPmrmLUNn2uCBrme_iJnibEHSpuHcNf-EjNY9-JbBXuQ89PGpEA-NvuwfzlaKdeNvCGiaAgQQ6a0dYPM_2wCWKEiWY6ymQjstFfUJSFSRABhCOeXlEbTtyV-H7sQ8xGNOmYOj0pIeZXfSoUdEhW90iVwuwQXxqGFaGF_Fwaem4ID8VhXEnbs0fMPhyfYNKMZH1AhkGJ8oWpyOqcQPjJ4gLlRv2Dw8_jIfXtm6-DAvcYhyUd2jXdVLuU9U6Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdSi4b6X4DI0UfUuf3d_d0SxcQQn_6uKKA8IQ--8isikmAZ3fJTfZ5y0QAJzgJgxPbqdPww_dyUCtu3WXXDzEoQTtwiME1_C9pE4hYyW7t6XYB0pwycuso3GJRPIh0mAWLR-YmIPTz9t-jL7bQQGy1rvI8Er2SAJOsOgFBaq_FQf3dQK4Xz8szEnComTajGLtrO-6HUHn-vSFG_0d4mgrRmWUWbMvMspwY8jOg0QjZTQ1WzoSFZ1RUioeu6k5GzLPv59dO_dsyEbbvGdrbyNrD9DNmwDrinoKCN0RIFbceFrtZ24cdnpW5_to9Dhoizl2x4Meu-4Sdo2t92eBhvWTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIVrPdwnihJVbCxq5c976KrD3klpl254xu5Wfrt9SpSABpK8l4gzqrQmodsRg_8UZwrmOf-J1vgEP9ErnGlQMPKHZbj6G22xn0xk6GsteKwHgaF5H_PU1Excl06vn3z_pAYzccjUFGOlkSjVWOWS8PPg2TizOBseiJTGlEORMKQDn9Hr3IWZNi0rTMCF9ybtFFNdbReWWI3Ifio8sMTxdRyb8zIW41iRfU7mW1NIcIRnXz62u3gEoiDeMuQQsH4KqPTgnCrxrakAu_6Wt2z6_PWz6g8mWhTWS-LkVcW4ImqgjEbqOF_KPjbH0U9oWWMpRGFFmQDAIEeLoKVPyrvpmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8903ycTeUWiT6uEItoNSNFHajArLNw0NowATJtYHwgoiwBvLrd9vmAOlMIjxZTG1gq1_26sgacCrtB2UjT4XuaLG9c6HeZ8At5bWVnCj52swk7OwGo5lfW6SWphOOE7ZKTJ3-XmcryJvRVI6rRHFwo8GD-AjNd1sq_5NldbmRmA6ML3zdwJUHxuY6TXUp8zXokTWl0yeZmEEqSlvXQmr_YJagzAJAtf6n_4slNjHzsclRN015WdhxwO9XsLqckCeVSnvTTjGxi-5v1NavoLB86jk1UCOaF2k2zuYAPiTau65rJTFv3RMUMKCG59PudNrQCu87905FzyvLadasrUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF8a2Prpt0DXy-f0S8lBg-QTQxVNM6pWpVLnsmbFu_HMAe22RTkqNHupqgZ5dnLaJayBOrRELdS_sl-Zy1o1kbnTkFkqYFl1m8j6OFblFFknGZ3VVAkL6WW7b66RGu9Fqv7EZJ_N2NFYelSakj_pfNDxStZLsOHOY-fOEag1t7FD9LEMO6eucHQxrjYPYxjNBGoMx8PTnHMVCPp1H4Yee1_tn8kjnLp0rdT6XjYzWmjx4poa61YTNmw2tMOk2TCYTfg3_FYRhIUCU2Ww5FfKCrZ8PBlWc3GrvL7I7bPKWgv6ALBkAVJ0r0tnYIqPk39hvki_L-OfU_qbAym2OJH6zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6c3ZoJtvmsP_M879v6vWuK5ml-hC15EXaBoe1a6eXg91O5tGfvnGm4ZXbhCtqMSipbVZnfW2s4Iqy2ql8HOmD5NV77ywMFbU8idW9iXpZn_QG3b_9IJkV6ah2skqQ_NqOsAVc39ExMoIxpgZ_A_OsfhggJVwBxwm5STNoAS0_JE9w16_seCbzzOF4tYU4JjHMRftgna9JY45oRN7PgCk28avRTxGpmGOsB_Cte_Zecf-NfGhUGLhr2bkZCW4yQQ7K9fdVPM1mIn5J85jWgdEJvVnM7oMu76mSvlK7twOZL7PhfKxcw-3Y_1hA162rVqr3gYYC6tbv7_OMX8O28exA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5tgE4eP1SB6d1LIX9gQOL35z0-JWlG0ne2mKplf97uxPVBJw3u9whxUY-uNcTovmPf0hY9XvtQrAsUTqLzuRNEfp5kIAEf6RDVxifxZuy4U8Oxx8my1ZAbpJXr5rg33Jl-gO8roSst-vRWFSSJIqBf0rYXbv5kQig_wQl0yNo8kBUMiQK9bvonHTnmRRsxVjSRZsnqk8DUFKq8RlZsUpQgQoV35YZSLOyfASHmoNPTWsguu-Atjz-mejV539Q70XKZK4W1Q5Xhs-s1F6EtHHeVZZRnXzssRbPwrY8E83ipxqEmAEzFmVyYgi5lSbrHUk24UHwabcuySIF7a_LJxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMrgJgXaXdWGcxPuUK017H6-w9-YYE9W3Ju1y3uLebi23zVYVw-AQQYO0UtuphMscY87holI-3nVaumCuiXOOCMn8DLXJOXvzzny0fQJ-gMVF7qUyPIQZUcXUbQnF5X2vAayhRB6gc2qr18suwxXRNTlyJyTJETONI63eZbK3Famcbv261RGm6ilWK3DSX1Mtjmabzn7D2DnhT56U1lWsKey2-WCFtAuih6dwE9tdYUlpDSlfrnEfQY1qmuBjezs_sr5HmHJjiumGRxmvyUfgCBBjAheectrTH37x4HZLpfoKJQJj37aZpz8EG42lZOzOyWCFTdv3ZFeQc6fevIeIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3uf-fMGesMeBX7tJc3uJ2AXiW5x2NJ3u8hzaF4Dc6_Z_lCMCRilhtE11bopfcYokWRc9f5co5L-lo_OGUVQREG1RYHiHduqNkhMzcexX-79TXn-QkUERSSE8M8YEH2HAOFCLHWTgZ7yS16-rSIp3Orz01CmawSWNxtIMt7X6XW8GrPblaxRJifwMBBFLIXW3Qjq8ZXXT8oi1hsCUiKeTDuPYj4VWebITwCHaWhpDAgZCRoroNuUvWXgGCZIeVF5xA86iWGEbZKzdRE6S44v6IMm4whN2Nt8nciYCpeaCKE2kpfbqVsEtySU_19z0oc1M30yrSLijF3OGfcHUm3Ryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WB-x-aHKic_0kDu1S-DQmkdeTYUu2gqe0CAC0qhjqPs0pzJF1JSi19PJB34UtSm2gf4hs6kM6KZpj0Bn_Vu-OIWN2c58HQYAxljq-XeFwqOpNLmJe38qbtpWpKzaFD-OgUmZ1n5lzHVtJ3hXDqTaCMMYy-tXyiKPjQqj0RgOEFcPJ49yGHZxdBwVye2830vOAAZFqOctWfj6kMMZllfc6nNLt86Tadv3mLPUtUO4x5PsvfLBwZ8dlC61iEJWIiKfsX_A2i6eO4z7DSM722wm03hXGLjL8DSa4-jtGHBHlUY5va1bgzsYCUGis7h3SwF0Eb20bBpdTKGKzNE5BCLb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcfQsjB7xoa6578Gg69BIQxaWsssW991K0SbLKacdq1wdIfghYKZW9v6koV-fAvkko4v96SAamejX0mmbaQ9UaajONnppnmu2ZndoHDD-CexFGIVTrQVQuMQ5oA7Dcc5SSobkljGLaY5lhE3CCZVwOMKGRltAx7OKF9jiK1yquD2ANaiLYK6gER7VBoBn6TI2Wlwah49hlx-mb4F7hDwkvTTLDwgyRh4TafsrUAHG4QVmp2Kbmsn8y42y1oqgZYLIPCLNFZ9527YWaOlRSS37ONyryFFH5jxs4Q0pG65vbThPqNuiswSq7WkNApwB19T3qMMqxPaPlN2sf8-h-acyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv0h2rggEHbZdFl7hwbLtxVrYwVyQMfAoiaQEp3eFFUrngUtlD8PuU6FjXqRiDdAT_ccwgM7AKwsFRDG_0ypHgUTHYIe6dEnQuEjECf5AH9sL2uOAn6kZ0mvcNWwGKvJsxa5-B7CS9tHpCexMJCkrGPlxBTTYKJv-sDBMdc2zPxX7bMRvtRM4vHGD1COnTSCGqAPISa8MUUJzyiq9z2xLq-dslgXu2Dz3FpEeX93PmVUGou1ZXccKbQNW__M9Wtfxva442W2crPbIBYn8GlwJLsEKXmNMd5jkRvMOmMO12iSZlSXEqhozWmOudHGKoX5abhAhcVUy4QU_KfvAoWs8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_ZmKSSUdRZw3tmTSf1pZqpdooU9xYjpm0fBrhIU9qg3AWj2rssigsod2Bsw03i2ushyJCx7BBFQU0J7nzXPMJ0DtBs5EZcG31pAjQabaExT0jxGE6FFk6k_QLOZbhy2R524AeCohFZvG_ZXDWOMtnI5t_SDwUJTSccjXVY9D4Bgh_2hvWqbFKKek3_dLclFc_fNtqqkpi3stMYypNq70tiYK8QmGZGOdG73kP5bpDcKCQVRFC8euOBl3tWhh50fCdaPv77E7rKVNqZmjJF2NzXtHTjEJobvooGnzEjzEfX70uOPgkwNx02IvWkzm0Fx6iNR4UsYMqHo-3OuZ-MP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=hXWOlmZ_jwRIDbMwQDWGmDoRfdu_ZZwQuFX78xc8sJs3mu8UbhPPIWOLLEWsJOXMviPglMw-ktIciDa9KJDlgqmbhGu01qfPV-rvpX-zpKafZNXYL9apf7UzMFY0jksm93MtGcDtr8ZHA6yoJAnw16lbEfeErV5q01wyjAp51JQpYyq5DK0h-_l-cj1FK8oPum8dv1aC0MaNvPktqTCFWWfrEEt-8J7NY4_f8TXqfeBom-wFlKBQdZ74Fo9-n6Y2-TRhf03p4b6iX1zTQLxGuTen4dtpp0nF5yQPE5XVv3Q_O6x8uEXJAyarvEpO0IyTm7H55jzAjztzMyMZji2IgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=hXWOlmZ_jwRIDbMwQDWGmDoRfdu_ZZwQuFX78xc8sJs3mu8UbhPPIWOLLEWsJOXMviPglMw-ktIciDa9KJDlgqmbhGu01qfPV-rvpX-zpKafZNXYL9apf7UzMFY0jksm93MtGcDtr8ZHA6yoJAnw16lbEfeErV5q01wyjAp51JQpYyq5DK0h-_l-cj1FK8oPum8dv1aC0MaNvPktqTCFWWfrEEt-8J7NY4_f8TXqfeBom-wFlKBQdZ74Fo9-n6Y2-TRhf03p4b6iX1zTQLxGuTen4dtpp0nF5yQPE5XVv3Q_O6x8uEXJAyarvEpO0IyTm7H55jzAjztzMyMZji2IgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR_jjOR0xlCYWr5oFWmkpisaNgEzoJafhZDqNoa2lsGB4-CZp9hn7o_q4DErn-qK6jJbfZvHmFij8BFQcvLwTy03Q0kwNSeuWTTmFFd40QootPLBIPJfXcF_0i6SjvvGUSIyafJU7NcETvmLzHhfjxLYLQsPJ5l8yhMDpfbrEoOFumPeyY64tNCEJDVv-hZn_w1DU7L7YI5In26QeFrzVZGppq6YQc0Xh-kNocekDrLM-l4LUvZtIpxNB0QdT9bZ24zISJBdkvuc0NvjCYhGCl70EU_oCkk2KRK4zgX-Wasg-1_gD58pk51XdlPpF2BfmsBA-tJTwTZxl9eIO2C_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clTElHvPJQQD4Y0fteb_Qk1GmvJgrxzl3xQy0FN9_5dmQ3s4TZnN7P2jiY0VxdA_bmEvwCxDYRU-tkVZjs6EX2oL_meWfzZPPqMcqdqDndZsUM3vJRlW2GcIAAIpxH0zYkcYND_2kPIYW2wMXceP0VtEvhhKQLaMqpTJ6_X5HO2AERj_Z49YwaDWuRtalPD_IbWa9WzbViRYOtdEcepfDhbfAceMxl0nbbRX0y-eS05rCzIQljSKmayOwQMvQuwsH9CNq2Wm5YuvNJ73pAfUSdUwUtSbGtnSqFm9jTtBA84anasqZVfJMedy-a-a2qcoyV3eCHAm0YqobJTUrYEHJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUIpX0Z3rXD02oeLSPAxS6H2kjtX5UBsTSiL7RhUAZeCbGehfILPt39lV0THGqnyI5xUDUq1kkmSHSZVvbETLYX2lb4peajZDE3DEQfhLch26-OmsyziKNyYk6Gb_dakDqIFAgeJfI2Kyi-jHRS84xMGJ07yOYbRkKturO3q4z147SMlp9ExMW7EWQUpIsRYpL688lOCTFyPpvXjkXp59XXx_13SuX9NJBBM3o9UYldyDcgjmjCHBJBA_bfXTho_BqFv33PjdaHF87tquv1mJGgph46SZML8sXeq2GTDz1UIiiUMz0Pv0myK53RqzyDSQr-9J5FpvXkfCdiNhBMyqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMEryo310paAQDz_QFDsZ_zyQPc4WmFtqwKREjkRSuuBbHBOHmJyLGp5yWO0v_cmuC5fuvUSsFADKwfvL4FZC5IUXfGh1sk8qCtVjp-OQbnqhViTYA0gPpeBEHANQ8JN2d2IcXRQ9ijhhiiIvbOqaky6RTIdKxnAx9KaJ6fNkMjsmC72YZzIuEUdcUaFsmhFBhO6mLlTb6sCEuAz2I-O60NRk2dJ6T-8-_tlBXoRrdP7lPzJrWqt444VromM9kN_LMuezWDnWXHx47i-tbFbq5okGkSdlj2pYi2jpgf4f52l_mBT3Dzo-8qchoBZEKGJvXsk-Uhy7JuFcCo_agujvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwYF-gOkZGqdt3rJ0utVC0czCYZaLc5wdQF0EA6_IhD8rWcM7ovXPyXAxhVZTlZ1LZptY3x3OI0SBSeI-msS-dEDa3LB4GYPMpQ2o4Fh_P9X9412qc7xHwo0WGqN_0E7B6sjW0_5VnlAPhaT2XcVuTasi2pCVTvIRsQvvuCsnC-MXvumyoKw295Iwtt4Q-q_UAyGnhWE01HRJlDlxGT26bHKf0bAoFPSu_yHz4nvCSqoVB6KgU3cx6lIN4qfglJSPjbOawFdrE1eRYdTzFlSFkM_jByBEbZE68owkcjTQ5wWIW3YSph25-MX8IvEaKc8-Mt-lvCVtpILYbZ7Av6jyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1tTIPki_aed2S2S7-rfcJ_EN5nKtppecbYu_CvQda2kWef-zoDy5hC9wq49tgFBAOpXoni4aqDBw8jyq8I976NVKijc8PB28UrO6cFxpdtCChdHYP91miy2XMRRQW7TSyYqLqXm__xsn7CBz8JaNTGrUBAA4U7LF_kglA-3tynzR1HDAmVDlVUkfjnts9VRdGmy79UYgb3VUFfQH1HI3v46XsZr3IZ9Pu0WJunmqlXDxLNUBofqQD6rQ5u6_nw6Gty5HXyujgsw9I0mAlr5tfvoK3jhtrIN6IeyH5XpGaV_C7U6LhFccjxeRsqv4viDKGNz8NuoQBku-juM86r-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYxL1GAYc8zOHLPS0r4pBWHyuQCdY-xmkW0DdCrzamjaia3-Vl1oKqDRwqh21TLgvkfVAi61P0F1zRYmh5Yvng4hJjC84VErDdBnoygOn1pgXTQ8uxymJ0mNKToOYfdx41qxKdBO1ZEbpjW7py8-TMOqQwG_SZwy88JufzyUK2kTS9fAVckM0iBAvbDiSizALySNPsimkbv1hlZAR9lxE94i5uWjJxswaLsuej_lMXu2NIVL9m0Wrjoti_D7es_qTdPRRGMSZj1pE8ZI0dZXNlxnQtjjTqcNz_4bx6evueLqC6wDeur8nDXmZBbtqoHi2IXu-YPXsUYMzUqyw7RqwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kv6I996854UApuc7wBsFzMCBdkYumU9U-yQ6okd7c3GCGhwkzwFrtgPiqBfIwvQn1-E_uSYIuJtgif-Qu6R_zHvk9PYni6CLdhnOeePrMQ_jkrL679eWIs2xGJNvnaqTrU6zThTtc-qAHI2Fw3M6iTngEj47DdV-0KkJ-L0maIq9qFKbldfC-mq2dQzBYwDP4STUGsQjZaOTOfm9CTqyYFuEoMW2U1mS47Bm1KM6bBou19fs-Ap8ChfQhmqE4_xI9Sz3Bldf2aZ3L5a_Qk2GsHQDrhFcXGz3qUQ6SYeMJhIwFejYuHjB-uVIlkczUodXfitwVqDqdc3jgcj-yrAjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwIWq6Q6Xya1Wx-m5qbOApNKdIb4OcXKW1wl_SeA2cvkmF6j4y3HiDuOsuyAs87WFCMtVZ4PLErZQa7miM_Wvmva3OiSuMI_YMenU7AQc4eMj1m9McEbMJ_oKeK952JqiPjuPh8OwVwutzv9lbEC_pBG5rURkup8DdV6IB9LEZBVDs4JCOnAElzxewnnM-JHyUUFeAHMEs7KU4-AthBmqewJmS8WuuBBlkug7RV0p6o8-lWIV9KuHZ8ZfqEdpSaxVIupyhZqiKbWH14Q5gntj08IM2gfZ_Qiorgj2onkMcu-HLOmeYkd1KI6t6-P-ymWoD51wWifDhqrWfadMk0ksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtbfffTqK7GuAxyNRBdCfTIi_RLLMLY2P_SYs2HDGQicQJh-IvnxxVd66l130haKQG2MmdfzZjnDd9MWdYzlFqXB-IY5z4gotKvTQV3O1bgK05oxFTSVzuLIdPjS1wd4l9qUz0OkLhnSGBMi54bXXDer-R98ZBNcUW6txNc1wfBNfv92wqjv_oolpNy_mqr3w25c6_PcVFY0dVkKGS51XhYeIImEcNwzVpFT0GNiV_Az2Un7Ez6Rce8enDHzEZ-ajIjEK8MGauvGbm6iW-NO1zb41yD7Y26rmLH5cgwZmvkptDpHLIuPA8yyEAuPbmyRDQNElAcd6nHx_iAjcjYVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paDBKmogP1yUF-LLqVSMRO1P5-TG4bYo4ok0SFGWHmZsGhHKT7dXqB5tkGe5ruenh7m0cuV8WTete_puOl74YaHEIeOYo4uHYiNPc7LaHW3-C0nsBBIYRAS_EP0YrSfduVZqDKeanLA8Wwb1kTjDMVA3HkhQT_unexUa4nUP3Ph_UIGjKWNSQzLzFsZlol5eB14zWfHe2ig1kPyuUhPshp4zYXTLwEpgaVyWMDs1EKw7MELXQl7A3Xti_uK58IbBlismL00Y9DpS0wP02KxUaq57C-KDnyloVXiQNShKdNu7KyR_LQdlk-RzCzjPAu1Z7FoDSCHSRvx4wDDR6u5AZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG777zZQFmRuUmM5z8lPf7snKPChPiQ2X-NjgDA7SyISnokReymGLFMvpnI6rSj4rY0I4OL20KFAPNvZd4dUCznrDiAQ3WOW6PwvPD3CuXHTSFzUVcAc-Fn9fSWHbsy6QtIxt8mw8deowKVN5m9X8QqkOwaNZDpaZl4LXy26BiM67d4Ts7xbaqKUrxuK5UR0cQIVbc5jJa_Vx0U0xhzZlGw3CxuJ92TLBxRG2Defd94u-_TXCKHU5iRWaLTNhKwPX1Nv4Xoc_DU3NMTAa2-mH-QAGTMpj09wKB8FxH92enmMuThMx1wHNA0wXhnYTpbZCga4hgTf6MeEGGngu3Fmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWnfvRf3j5Du5_bVW42tQJU56WZtdycJEnAJxzBIjm_OfFVMgUqzvZH_JXfBceTZIRTG7RgHhgdbwFS9zI-os9td2SPNpq7QkFB3_QZ8Rx3UCONQhetUvhNQnTWTVdMmK9YResQ70c2BzcXXmIJHg4iPDjk4C5xdx878UpArnWcn2lnWMq5sJJ35hwF3wft9Nh0wjUrEO2_gNUFDrlKl2XHpzkXtg3DuXnR3XCPoZFUPWQ4Fvsd_8tDDyXvvWZWK6lolx0GAxDiKp66rS8XZZ1jB0AC0LMGXfl5ViH6wfWlrpRo5qBO5WtFURit2HiL1RCyI4bbpVuJHkpyNSfopTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG-zCH68bJJvgOj8Qg2Pq3ZmUkrARiy0He9uiBZgclPW53AIkWhPggWYa6vwnMIYWkZ3IKXlZLmSk1aF3_J-up2iHO8koJ0pYs9JGFvlEsDg1Z04isBgRuaPMxqbPUD6SMdqsC1avyrODrudQ4DDIYKoIxOOBBKp50HwKlMW1NNBgFVVQfLmqrgye3RAckyTpwAl6SAfyqWlwK-Cu_vHXFs3VvRLnjaIrPTP2CDgOffExNkngVJWt5UgUjWrjBnY9-34rYYjPAt-z8SJsMYxWey0c6ClWchWxFfIlO3pOiz_ts5lQOs51aghvHMFDkrUkvP_z3MbAyZ0MvHdpxf2_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J901wCVWMBpVZ9mvIuysPEXFJe0Be78-PV2nNz2kByPnv7mcrtSsd6fVDtzAcbPvFiN9710wsSkUgReT_4w_EHsLn4hs4RQKE8hnl5JE3xB67KEfMVmjq66LOHIBvPZB6IdqgQvOx-LTe1wghQ1Lhz6DcnXCJwi5maZupZr8cfAf6kNVzAQeoP_YIPnObE87ZdHyMYpruyvUhwk5y1mQ90ZXhLmaPNoz4W1cuOSdpQ-PbbiQf1KeAbRdNuVtJyXd8QYlyaWO9hdUzts-ibhp9Kua0DDO_MQjDIYUW6_9IDj1QFrDSi8gdijPeHoWOtJo4wr2EtVeWz4lknI9RdXf2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCmkr6uF595gGNQJNP3ujN6NCQ_7zeDA9PiZDKzqXBj3SOIBaWPw_4Fwsb7WxZrQwhrTECZz--h2xZaa1ofp_NZTJnqG6vsz8ncK3TbLmrZ8rTZHg5Ds--WCtNqK_GR5SHb5nA8C7thL3Dk9dw6p_vFfmNspGa4Gyu5iJtvCq2fiRL9KaOYiIVr9LE0PAnmqOw48NErbQxzXyhruoKo4LbkozJH3aA7eSjvlGQpcEw8hHDSYbBjtVnGcIta7JJUtlqkdpLPYlFclffa-GIlGLCA3iMC8sGnhToPEy8BIGN1GRQFn3Bxj99PEhXy-6fcVHMoolWf5zmWDNwPgwKA_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
