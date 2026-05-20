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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 21:07:19</div>
<hr>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdxLx5hzevnX_wfbzRu6ztRUiqtOm6OvD4WYr4Xx378sJJi3ecjzeIi3_OxjJ6bM0beQRvsxuYRuijZaJu-J0ydz1bKDxN2oEChhMqXy46EHw_qVxH1as8ye8VqfLQATsW0dSBMxB6Ly8VPqlDxU_2Oq-SqYefjU8hnGKD3g1SNIyLIsf0TNZfYPGzEN8FbqADUFKNuzw9RtE5V3xh4bRiFD-rbNCrs1_Oy89jwAyZ2zdt_vPBBIolvCy8f-gGdiEAzxQXFzPO8hp0RLaPKYofzJ0IFSRPPfv8EnJVHlWV6ChQIGtuqsys-Y3c8dqEvOkynJASUtG7JhNKqIHYZvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lP0yx0hhl1ztyHrt9ERWKOumwuin6RVET6YKmxscGey6ZBgGyhuk_9TsiImH5VVt7b9bUmmFOpSTSuppPdmptY4nRydDyop2xnKyPLCUJwZrFgpeh2Gpx_SESoRdokALd7RAzKu7WOchzRle5tPBEQgcksLIKmFD-uw9EDYpAk_Zjm6_w8smaCjUhKu6Ou91ck0lxZKqnjPgfGqJxwHpoX4JiHhZzCbLADEWRYuw4abRRllZvO_NqOpVwTUvw4RqCe-xR6YTO21rsNcRgBsxea2BogV05m_LBgxEozVIQneHJCIznOO0jSzCmJ8aQrCJ7yiIcKaPgWFICVapC236Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgtw0tmeZ50w_RNkj9yBzKYmRTYgoRtSvP2Dp0WPmwxhVXmYIf3Xg1BMDbhQgLb1sgi6kljkb8Qjo5JZNH_ThV9ZYr0J9mlgQhDa_i8_rriSTHuad6XJQd6yJwzu0nJk1oDf8p03Fpa94j-r4jpqzpqakISuD_m2MVZueyEayWflHFVZzAKsMvrUhXDTpnNoElqVu82w_8PginJTwpW6KwI19DfDlw-FphdOuwPl3-beq6_WbBsaxkROWcOI7sMlvyaaKkq8vldPvZopYZwoYc-uwZHV0YoFLuEzYMHfem4gznz5MwlcRn9kXJhDN8H8Y4YlBQXSaW2-a79ra6acJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceoGJv0ojutbhZ_2zF0TVaYus1enO-qRE8nJTmBQZnevPOj7WcjJPKaaMjySA-xxGvZcDfsDh5Eg3AfIKXHNyWRsa6Z5zgg4mkSP2tjH_AYnay-teksMdmuf7N2Onne3Vdv2eCCTIR0hCyyLw2kxzdWMgpIF7SUaSwyvdew3rXj8hB9w6jfgQ4ycus_kLpM3JOxJX1NOdXuL7nIEetzUV125AB37k177R3W5Gj5Q1mQhT8NMde0ltrcSkEL1re7q9e4YWcDuD2UU7aV7ZzgmRd2-V-RP7IGklSg6V-BnYh_Jp3mw3HnYQ2faLVHglWFAR-SentGgx1SXanhcU3Lkew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwqx5rh0Ongyjaa_IrDuVrgcGoKx_Dki9WXI1OnoV_jwVX76LEPbv8afKzeqdsGhlTQ1oeDKq7j5YpPkKWAV8kUu8O5KzqKJImxb-OJedd8MKubWYj4vFcnaVfhwBwEjCymxM7cPEfkf20G_JJJbNOocYWcq6OO244Y4uwU_l9EEw-Yfjp061-yRveiqu238i1cOUuGv6rX5PgrrNDdL7COdg61w4nKOezgmQBJn8AMMr0TOOYaplBqcFoX9zU2dWcjTq46wHz7M5JImKniHZI_h5rKmA63ldAznEHJKEjn7AcP2fPvAXM1VGmc1QYAwJEZ4bveYGmBzgv37-gIHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZuOYyx_uNxkqSImfVZzEzQEssr8M2bgz3C8Z9PrClRpGzudHSOyBOTgfdgPV4_kY4d5ofqMRIV_obSEZDhu6ua-XhBruxpXcnoo9mB1XlZ2Mc23nDiNeo0lYou_g8g-_sylE91xqUlZLJxLCwbAN_OWQltmIVTYuqZPusLaJ2exxePX3-Ss2Lf69frlCl0L5YQwbpWdH-22Iv68cg2aK0jVJozE5liG7BpW_hkFpu8h4ktEQXR-Ei-frWYrKm9uMIKqQYAEwubpr_YaFAOLv5Cz4qUqQxGtvkKMyIvHTN9zdwdgx_0K2v5tZn9wTaY_LVUNOHhfBuTccVKp2XPCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_pLfTPtv7hX0PVo4PP0E5l-het7O5Y_uyUCAE_Tm5Bopf2uadgqEMrYCQ-GBcp-dlv2C57JBrPKAz6q2JfELD7nFq1cz7yef6oHFx_X_2HJxhpWlXf3d8q65hJkx3u0bcHWgevsMsqVjlAYrEfy6INsem1n78-OCtvQyA3W3BnC-9scZZPd7Vcw0p7iQUa3YgBx_cw0y-4keoX8oI7VHFt9h2-srfO0k_sq8MGF1Db2hGwgRcEJwxE0X9c8WQmWUqTnfJec1aWOrRmoC-M5EeBEC9OLfmp1dDyAWQafTam6jFXLtJxx-p__YIiLyqTsJf9AxEtTRY8TItFZ4CNCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdtxRLVFMpp2LgI1210AbRrOQx5ds2nrLne__PyOjheXSZ0JmpkCAuc-jfflwz1rjw7XdIKxgP2aJgqFfgSVQimNxVjwWgPeXkZ4KVw1f-JINMhxMwgRGU6bMIyMWnZPx4brMBplCox0hTN1axjkI2Xa2okEZDWcrW9U317KDXVv8oXwmv7HRWeaNJPUzP82X1rs643QLD27EEnQj_sLSAJhq8cYksULlNGMnKNqSO5dTz0SBlN_y-d4MbCpTVD6ejj7kL5ol5ldRhxPPIvU0Y_hK5MFRVXxfnlpceDEmY5W5_mNblh-UIigVmohsPpIGO_YX9KPG__qOk0DKQiUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIaJuF4sdJkVUO1yoieUQmnVkE-yCYbJAjQZVgshYLmT3Jiy32VJS1dgB2G2YeO88CZdT4zsof6xYq5IyZwyxtcWVN7X87uZeSZstNi5TtWyVHvCaekW0DXEOZf4_mgMeafd6-wsVh-dKFWP6Bf8S_G2gqzzAKWmw8aRrN8BYHZFbnuJqiFILiyh9389dzt-rLjrAss-GfahMON2gBRQNrWd2J5N1FQ9DSM8Kzj5b_7uLsQ3ejnXWEB5V2kxBy9NExRaohd_Oka6AydJs-2jxFj46cOgDbeu-XVeLsaxy7azIvirhpQeCCf3uJP1RwOncO3VYsqjZucnaJxTzYnwSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me0Tkz5ooEnqVKZFCA-p5NVfKiU1w-rReJnKeJ_d5Bc3HsguUZlryRCaQwbExBCztSiMvPkuAWrQDuKTDIOd4y5rksxQegY0gFCetCFVTp9NSWpPXr_bjFNlNNi_szAk1pdwVjS5WDzGGcze5NnSwAVYd8TBWBhi5BBVDoenfzmQ5UW5HAj2o2eK0eulv2HxQ21i36-bfb08lWKowTBUk9RTCrUMyrSzqrKn7Rf1-6qgvNdM-cm8uyn6gLACby5F8Ew5xbL3SUKPfq2l1VRgnyextKiqYBqC_KY32rp_fzKeqRqIJnCAYyK-nVh65LwdnwTBjeLDk6l3BRpiDfWJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwux93A2rCIMYoWLeMZ25KE657UFBLVXn_euMBGwOCqQKCghS9CTNtinsbzpwNfsNUUagtiXUljvy7WvsiJhL4u2mq4cIff7Yd9kWB3rOmNJkbRsUZqne0ja92spsRSmEhI0yQLTUu-ivek_qL6wELEFY8Z9athPjJrKk45YNIGnHKiUJmyFap6MJ-BINcvBry5SIHzmSbH-jxUHrLf7HC7mAnAi_08cdMcV3Nfg3t8J0CZTsxVscbiktfOXSFMFTXL0yGuNWxm_gO5BtmHd5IDAq0y1LEcb8_PlzzLdMH2KLFYlo06pkrt2PRHN6ThThSAqVHG09_E1-QT3uCtoSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7hBI9NWoFKIB3XyPuUU-LQ3RRwBTIeQOjJ_z8-wjW0pMtUY7XbM2KRhEp2Efip8WD-ghxKCvhN75zQ5ZZLVbXJ6D5VdQt9BDXfpVSKSRbeksASMbUwqoU4rK5Pwe33oFcMFgrIi52hY3fwOSEQ02WWTI0PC9_wQ0zGhwsc7cWYjx26c_3q2hr12Xch9rB_Ebyud4d1POjSe1QTLcv5uM-fbQlVqwnnVu-9_1Gt6A__86biO9vuv9m1f8TBmqhQO50xyJjjaJ_kUNE-j_AvFo2Xdylzfl2jLTMntnMAgJAYZPbcpAzNWbWFf-TNp36SzUUSHE0dIhLMgIOtQTpaLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6ofVvfNyj-aWA4j9haelPesDryqX_Fc1pTbuINNzIujxK6gCyWXWwBTJ_tNHNhLIUxa76FjvxtfFzz_jIGouZul_d_kMpubywbcuE4_CU7fiqpEr3FF3ZWpRLkREpqNycGMIfHEffqe58v_xdoT6vxoMpmq5Mvgh68IvXmqOyT47J128dm4ZAD-lRzTIafjOwxe1ZpXpfiuFJfBF18egL-GSRe1yHm7JWhlW_LWdjp4dv2GquErVxT4ITZhgp7LabVW2LQBUjozhI3qbwJQjOvXBZ9Swn4HuEK8CfJeHiiEut2IErZyUUdkTGhVFKDNHy4plp8cEMl4UmZKaRr-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgJWnisfCNaCVdujDf9cy28xWwbz3Oq-GGYDB0sZxAIkjl0lgVK93JVVNWN4P4d4K6IojEoCFiyN-8zjcF5IMqgVT9uGxsYYCUxa-oIqkztVgJSBjE84kW6zpnFWmH3r5G_skryoRLhDwiskTN4kOT1WvmqPZdDVkOFLfjJtKws8MBvbp2nLqh0wKO4ycn8Jl0tvW1uxkJT6JAzL9G8eElsScYvZD5OFotHrVijNM7TZ7d4qKCypBuwEaECAYewa3U1S_s5v--_0jjD77UMTHfluOcZXV2nq0CS0Ab1SZj9yCuBIRH3kMy3E8zz8o42aMMk8_24Gr6cTPcCVM5Qykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=SMSgThEq20KoBrzp8Suut3uYEP-LUQism5ePmrtiJWyHXr9zWU76iLHwcpYInkXk3JDPNcZIJ-ZnLb1T4-3gZMsrZeYtjg0EOKvYTcoPRXZLYJ38lkb_g-pm9VdCVmcQayimT5-pU_TMElwSN_tpSYvvi86Atcca-o-cp_PUnBY1wFmFuRmJKQZpQYX7xNXXP1IU7EWgK96XzIQBqSo7Gg-KwL7qk95dxeB7QrzjN-71htvWEBvCXIOLlNu3nIzXJSZ_40t-ePUdsNzZ26EoOEw8XMd1Z3h1d78B91LendgydjpId9i_w9rTYH_nPqz6hag5MNM6YmAj8EZEWx0_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=SMSgThEq20KoBrzp8Suut3uYEP-LUQism5ePmrtiJWyHXr9zWU76iLHwcpYInkXk3JDPNcZIJ-ZnLb1T4-3gZMsrZeYtjg0EOKvYTcoPRXZLYJ38lkb_g-pm9VdCVmcQayimT5-pU_TMElwSN_tpSYvvi86Atcca-o-cp_PUnBY1wFmFuRmJKQZpQYX7xNXXP1IU7EWgK96XzIQBqSo7Gg-KwL7qk95dxeB7QrzjN-71htvWEBvCXIOLlNu3nIzXJSZ_40t-ePUdsNzZ26EoOEw8XMd1Z3h1d78B91LendgydjpId9i_w9rTYH_nPqz6hag5MNM6YmAj8EZEWx0_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuoFetV71KluTeoswC1gAqnqBoG0558HjBOkLrEQaBFwBs1BvTTiNjjkvAihZyZiUxR5YiDBexVeBf-JkJwDvtD2PSpvEJYCC8Dv-xz4cIm0KsKx2dHgPF5R718465leRUL52IZwRV5wK1qSeN987wrJGaoaucA72WuPYmZ4oYfJpF4MWnOQSKonTSBf9vByHHonpY4hutozQRvhE5-PycZiRAswVqWEv-1utwhTGqhp-JY9ReUDDMCeRvQ1s27Z9p6LMZfKbpirA8SuziPQySpHo3MvqKfFPgYw0v_pLLAXdCm4rdjfUfpCq9mpq9yknBtifaFO7nUjky6c7iHweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJdltt_4g1ii4pqVrC7O4Zwy3K5nUFZQO0Dr8l9Ju0b3o30_6-Ljc97rwylZ6BsOGucUQl5taMMmVca8Fpml0M8ubF5dh2RINTuYk_HJ7Epd2oD9cUOMUV7B9Ybjq4QKj1OCaUAjFxPF28HtRf4dXMKCVLwd4N2lhcDHfxQ0hG5AFTEIvWhHSjY7tM7H-a8UCICn_IXNNUQqE7YmH8ktzcAph5RZSB7KUL7A1blSRb5sGH68o4LF5nvkER7LHmfXBWZL2WxEbHPFlJFKvnN6DJ_v3eXecaJLqQs2B74CaDFrLKD3TIyiEbmxbKVEE6Nx5mG75cbX-TrU3is8HsQQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ4WmTDtq_LXhgtjXy1IFKRgzdQRcdlYn_bbMS_S-EBKEpOI3tMMBZyPcDM3T8K3-XtELdvtDgrDhREB5cr9ncvYuRnrC1209pioHxn6SGTIetLM4NZWbefbU_458BcecpBLVkezshbOwDNFzEsW5wI4Ff8U-mt6WGowJshLLNZqLbzUfC28d3-5SrfvUeAp960LdJazKAj83vAA2uaEqAXwOQE_NF7JM9joNvhT6pP0sxEakzslzNDCQ48yHHJywy2C6YUsJ-l1OnQ9LbgyzOT8Goy3kV5qPU1ee1JuiDao3Pao89LKDUj2A2JHLK8dxH3xywNzePu29vQFFx7E6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfJEWFFqT1NWUJhZqD142UK2H8LkNoMmQTEmP99cjfiNktQPZexOc9DG3v01lktlbkPdYV2XGADdaUlaKog97RWXXbnfo4YdpqMTGNNTn9B0TUTHaPrSMSas4LZH1oeygsnUC9sQoPVIqHe8L3R6UW3Rg7qL_vXjwtuwAXwQHrn5SI7Z88sKXVJi3K_oDz4V3r4nCKRz0PxXU5qNV5h19O2jUI9dSNvIvRPXFM9QOZNCPwtrYKFW5rxfc4qDWkxiRB7yuK3T9j5yV6DcnWK2GxKQgn7NGd1s4lE_SihRYciQkYHq7ifPzpjqD2rhdCFE-PfMgEMVU842999-G7gCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZ_mD-_u6zIPYuRJqvfXSfLpP-Jaa-RXo81WXmxwTrhFy5jc2OTpgsb5Ih6o4fECbYiTdDWp-Mdq0ExMMVPMy1eam9D4LVEF6v1td8NVlsax3qD8YCzRD6NWtCjvsbTAK2EwP2nqtp3AF-mDA96GggUxSMMjvDRON9364AgJ6sLqyXo9gnSgASbq8enPsfcQuJgdI9NulPqNb1yYi8TmVcQS_iIuUdhAhoQeucF-AcMJAYu-6r3pHCP-7mFNB_Z3t3oUusTp6_yktMP2PfFr3WNvlrwIcEP0w55zN0eJmeF5LDbKJbps2L8WC2XlIaCMsSG_NCP7p49aJIrYTpx1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKr3ry-G_LHls2EgdM9vaY6ysu8sIxc9GSTIvcEEtBzy2GBmIFtviXY9nkgOnN6bL5ARhHwUYVkqInIFtb3LFfffaJkULJEOhz654nWEaUzNkgXM9aKgN08xMgtCsEDz5-0ljL3Q7oCSLZnGreki4PEykRumtYb6OjgrjNMVCkFyhvNd_L9GnIq6IXRQe_jO1Xu9Qx55qzLq94qtp2z_M8BMkmP6zPTM_PiJR-9r1RcPftnxM5llaQRsOviHA6Vo6A3wVV_ptkKBiWOqBwk2NtiWqy7e44e5O41zl8Rrxic6AKPUNbNZRzMVC42_sQBIOVx6OQ_ujTBSc7uss0VRdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB-lCl8uJAWfM3E53x2_a9VW5UFRTnq3zBTwQehg2-mf3gYDh-naHDvgJoCZXM1BMQHq_TUoyK9QydQLYD_vZAotzYbEYZ3LHij3nsmElk_O3HSR-ekmmhVp7FrYhFSUiKjcQou5y1IU-63bTq7fiGrFEDV5B1juL008TbB4aeGonRZr2GCmksg8uD5k_lyf7Z_EMjL5BiAYc4pyqUccChToy6rZxmXZj0kA1zXGuZZworOZH-HHmv4DBh3vCExNwrebQ8E0BwvTiLQDkoOTfpH5miYe86F6Gj1Q8oPwzPtY67n_hegdR9SH5OY7fvwOIXyyxQIkxo90GRCEOB4h5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YylBHrUJih8UOLX_Xbh3udx1h8HuvvvDREFqpnE1BaaGg72LVm_10-w_8O0964HEFOOcsMoDmRo_C_Bk4NinDVDKyB2HqLq3WmQBHpQMhBFg0J8-2Z-btv1JA1q8YfbSv50nvJscuST5NOVbMee5hqSee_j23-BNK40JN2EXpPGRGTAi2LlFVsBZgk46YRXRuVGXQ6FYzPmnTVxM0zVou0u28fyyjsi6U5I_pGFGK4imQB0yXYzOKJORcmH3Tkv8xJWPRt_B7lg3s40-vu2SKNqAwOYXP7YyEsmLkoCQCPJdbFQ7tBW42ItKGZAe2JZlWUoH8rvysqMHcCw0iqfG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZZ9ufDq12GAUUWJ0gpqrI0Lg2hivlFv5VVmu6TCwmuSK8B2Ao85jCgd-ffFRcsXGkRivc525JvhYFjdRQABhf7tiFSNC8IJywulYrpqleeoN-rahPvt5wCxRd5Ko1ffZa2fwrO8g9hYyspbkpfGk2DM3xWxkdKfxuxGRHHw4moxi6jqQQtfxOZXGM0Y-QpGBWl9Bf9qXvyMqnDDJ5FaTLzr6ebK2o-SlOOSF6Ir2416EbwXCpDX3yWE82KbUjD93FslVL10LxFnByXanPS0mNCqr3QNVg8ruU-gz-rq2KyRsx42MSv1Ag8X4hO_UGCB2_4dEwqHceNzYJYiyncUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=oRIHuJGIEQTNH1k-PUbVEb9E0CB5Caq_aMIjCoCce9y1HCOz6td12TO9wB__2Vc6O5M1toXliD7E6GZQsz8_9zxHZKpYf3UZsnSMS85Id_YT-Puv2gA5YvGPDeSWTWJ4ZbhDxcUZHu6o4HLD_4ApR_r2wA6howu31uk9Eq3spuiXXMF5pi4GOCB_N69Y6olqvb4aNwvQt84AVVuomD5SwhgjVYlFJVItmQRrfwUkXwABKYExqMrvdxGpWxu_ph9pKhhGqMZhVV1x4sq1YBdU6g8IKnyi48eCUcOx14JMDZcTwGGvLUAiFDmHUkBIi9IodVyRefDKcFA6r2cdD9MR3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=oRIHuJGIEQTNH1k-PUbVEb9E0CB5Caq_aMIjCoCce9y1HCOz6td12TO9wB__2Vc6O5M1toXliD7E6GZQsz8_9zxHZKpYf3UZsnSMS85Id_YT-Puv2gA5YvGPDeSWTWJ4ZbhDxcUZHu6o4HLD_4ApR_r2wA6howu31uk9Eq3spuiXXMF5pi4GOCB_N69Y6olqvb4aNwvQt84AVVuomD5SwhgjVYlFJVItmQRrfwUkXwABKYExqMrvdxGpWxu_ph9pKhhGqMZhVV1x4sq1YBdU6g8IKnyi48eCUcOx14JMDZcTwGGvLUAiFDmHUkBIi9IodVyRefDKcFA6r2cdD9MR3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=fAUo0SxVlx-qH0J2B4w9zEaQDvQIyxo4u1TaPAUoZf-ZmxzTwzDhEq0tmZr6XBRDwPNsqnV_sCNf5z70GA6BmI5sqSw_s21HdsYQBHkcKnrWmmKEwdB8XgpJYLFBFuqucDJYvZD3b5c10eoni5lgkHDX_eReFlWoEiGcJ0nMvUTny22OXyihCz9y7DgRdosBcaUgoh5y2xJEzUNcmAdB7VPuXdn9g9iJ17jUyfiDU2s1kjBVGfXk_8gi9CceZr1ZrTJhWJQqGx_cGBsyK0Q96BKk_GbSinlpo-ulxKCyzNheQRCcD1vYr87Lyjxke-bT09AuaMlQbIjtwLVgFK3WAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=fAUo0SxVlx-qH0J2B4w9zEaQDvQIyxo4u1TaPAUoZf-ZmxzTwzDhEq0tmZr6XBRDwPNsqnV_sCNf5z70GA6BmI5sqSw_s21HdsYQBHkcKnrWmmKEwdB8XgpJYLFBFuqucDJYvZD3b5c10eoni5lgkHDX_eReFlWoEiGcJ0nMvUTny22OXyihCz9y7DgRdosBcaUgoh5y2xJEzUNcmAdB7VPuXdn9g9iJ17jUyfiDU2s1kjBVGfXk_8gi9CceZr1ZrTJhWJQqGx_cGBsyK0Q96BKk_GbSinlpo-ulxKCyzNheQRCcD1vYr87Lyjxke-bT09AuaMlQbIjtwLVgFK3WAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3m2XjBfs8NfwGA5tlG-zvTvHQ4i6E_IToAsIokR-9MFnLveFtrMXiY5mzaclgfMYRUQENpobFSOcdwpVB0kcK2-FpwkltE7hMQ6Mm_Hx9jz5UCb80SUQ4YdBFaDx5I50ODAcyxa7cMf1kM5tJDnT9UAbVngj0Vh2qM-Y8Kb9smeVHJcDQOgnv8ckM-B3S4WrGX7DUyOiev5r5ocdmfZeWJbtWUjlo4jQ-Ko4eg0LqPv-rLR3-K8-7hmijzRxfjX0NzXMVR33NTdKu26sPBhu5o6TX9zjjGO-8MB3ZZrmuddL5twOBPobFK6NFbsUlnhI2RdfvwSUBFLdy1duL3SXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD1qhKF16ssiQrEzLJPDMjbRelJVEEgcnidN6LqDordHYMuAWf7abi6bM7iI-xcd9mymS_h6idPnpwzcJjiI8f739fvH-hFyNk4dU4gnOtJ-uxWRzqbBQHE1efTbidUzQ6KNCr1QJYud0z43N0Ht7kGfB3cbj50szozGO3CiXi2U1FzCWpNgJ-f5Vnx-imr7ayV0qjNCSbZv4o-Kx1yRwn38g3BA6CfDTRy52ZGbXCC9rqWmHzmuICjCixN8Ec941v6BwdOK2fDDXcwcxw0alO5Kg1vsLckC762b-LQhb3317ITlnaOn-GNZCoQ0XBcNmfUdXQ_FLFt4DQT2hCbvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaghYcHuir-XlloynDE9gvFwLUrC_lrp6PWSGXcjapMJvHOdjV2fXaEBIeamjBoeYqXy_LigzjPp7GYIN14CaK34ThZN-ADKcU_pebWJy7vGmto1PnTcfHvjEdto9Ga3H6tHVCcrBkUUPCkkDrdsAaQt4gwsdwP5Ju473jmn3Dgr5l4abR16qdUXYkDUNdlDNdEzPu9stL-qkCV38vXeIE2eb3kTt_NNoPYNHmGwOxTspb0yDsBhiDoyYcCvxJmb8J8o0mgwz7zH7fDn-CNjd1iz5Q0EXYIaM_uLFhJ-niBRMiDjEoaj1XkkQXb6qNsrL_zg5_8Z7I8mRUMHtH4hag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzX_3Ep3WtnESWtrbpeBgFZJy6YBATzsrDCCWhd21m0nLGAAvYERRLZmTLBvKirouMFMPCapK5LKFCJuhtfZ-ca54HWxUphzlq9WY-5pk4t4pX6roc2C1KInVbpR-iWeo126ucBeVXe23WCfz09hahKoxc3w6WuInfurpOwhghoYr9gsw5sYTFL1ZWIuMC56AOZRcHI8L0qrBfxTLrx1pBVAKvyeMZqVLYDO5otFA2MaR8BzeZRI80aW4ZauxkZCW89ZSNrORtQnuhNctOb24aO2vFigFCtNBJixP30UYPLkVezPbEHHj7291DZTZaNrIBcy0OUOH6ZXogGLyKD3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff2he3lRJLVrMMD_t61_dR05Qk2dEBLD74frz2uscWFLoAFFlK-xWqIBWhuZI0c1LNesrYZU6f9BEXSigfOsZ4Q-WE-g24nek6l9aZ5ys3r8o4znb2o31wRanHGVcpsvuhBIfTZ0TGLgbT81PClfO-HQJfRaBs1Y706cC6oVBCUNQO4iyop5_rcDXrdZU5YTa11vNamRNPoJDcCCqVMSAdPVAj7yWIBdmrDHNaKgjXQ0rZOQjKHEr1uyd6M3yG33cL-DSimG1L9Fp1EuDoMnD1HlLPn5KA1iQnOPfqD_AzaLdVWyt7q6RWhmdJvpApjdNME-aYMZuNWFgM2y8TdGQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crlZcjW4OQd6-aREJC6KyZYNupmv3-ZU4sMMd9Qq51zQw4DddhcGEP23vKR6UxBQlDASsfV_9s2oLtekHAPAbDenQSWV4S7-DBD-mefD4KPuq-KhT4KKOujXDi2EeMWLIBNCZJAdg-8OWygAPsIwS5Z4EZlbsaq4GYf336L5n-EQN2QT9gy0BOytRw9w1-wqZJUvdtRKPp1nnP6hCd7yKcH18aNYJ-TM0Vvf-wp0MCAF8kKvsFJwcuv0qXs48ugCIpixKHRKh23Xg2GJWE_asFPFhjaZesCgkl0jRfRY4xpPxofKL044DFjoXOtMzAXqk84ZFVCmAlV5yznpgn7MTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOjVIHRlsItm_XRKbxvLPvDurb132QdcKBSlrctWiZ64fl4hCSxNk8axotYuNQuK9neA5sM_mbcE1U7W4oSakDIXDcQMw1mCOEz_ki8mNOI81K0ZNX10VswfVuVM2Ons38GzpkK4ldxHk3te7kGk14C4qkQLXfqslzGwk3YHgj2JlO8Y7o4hF7G19IgqfDbD0cFmnA1TrHtwy0m6Y-va4qmOqq-v2hu_I4dkZBDZmLjazDg5MQGDSYoOSlj_ndgEnu1SXFvaGlazaO1dwPy9WWK6a3GvRWodcuh4Pz5IfIAQprmg2jJ9FaYS0Nk2cMCesnv-5qDG4_3iP5kpA965Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8HlXUPe1LIga7z2uF58G-YJoZInFGwx9RVQb_vTYgxP_M9os911j4gaQKiKhPcyoSfUQxmOnhhtylDANje-xStX9K7ADU8d7fh_8qZJTmrKWlcIrMhe_l84eBHRV1Nb6MvnsogfFLMsKdfDjKtyK2PG8Yy8y8AA0fzzegGJpaMc1qAz4xMtaSVW01Q7AQmueiJNSAwEQZmh2apuKQHu2fSCtJacO4KJulaZPBFnrZawFciGOboFJT2gzxBtE1EPgOtjyZIOjXcYUec8m9NH_BS2s8rOXRe5GG5i7QeX2_ay72FOziJQ4eELoQamCyr695WNrHi-N1FGZEqVOZPVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pggfy__2kgJ9KShdIhGE9IuWL8xrEF7N2HuYYv_ll5b7rmPxrxi6OdM_UyHYc066Q5AiiX6GndiRkYlvhB71gzfFOL4w5lZvnflMr-MfTUPZVYakEJqZ0QDZpwvxVmpnaxEIZ6SVVT8UwSpjyvIUIX7f6Y7G-UYnKNeMYy19GbE5eInLNgV78Bi599zSAM8ZTzAzLtB0wtWiXMdkpOVMv4zyHEr9tVwV6iDtmZ8qbUEfYTG2pzU1due_FwCWQ9Bby7mw4ZVdAhqJg94xpcIfrPTHNT2Kx3RBW_vIPRJOownx7_2VR_UImuOe_xaquGejNUuLG1l3n8zAtE1dkQMJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9YwdeAWcnwMOthweVIjI8eUAL-fCo6Cyun1ctqpLxzwP30M67OrwQS-8k3vSznH7TmztTgKuwKpwqmCYh5QCK8SsHdubk-eIr6rovv33owtZnAh9pHz2w9Z_AmEO2ul7G2bFzVub-zc_rsuid6wKBk3ffH_mN4Cn1is5uKgeb5Pph5oPZeSoUOVS-wltSNN9hB-HQCxzR55-R-mcNyw27Vr4MDnkM8hR3PJ3VZ69lHR7pbgPTn7cJ192MUwxwE0vxpQFmOFgc1UaofwiesaHbWqMVrmt9Xh7opcDF3NihcEWxiAubaqVg5frDPr7x76bPxKzaEyqV_5lwxLr58Xtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSWWjoDCHb99N6QEumZC9pPG5tf3tJ_T2ww4mv5On5GI-gNMQixhirs8sFb_aX-lb1Os0JXadaeyG5uJaggBaO_CAKlyxx_o4UFRZPPHWvLA9-tOOCUPQnEmKn-LapaaiaYoPnITOxClfuKkgxaOeupnYDs8zZeiWXLOgk_QRs0AyB99ruUqw3h-CtATjZXpSw5uEubl5LHO9rcaMOq90M1kjmicJ6EPaNAdYnaD5HlTbnOsCmdB4RdiVvrcraPf02AMf2nkxlyk9mT5kL318AFkbD1v9uKP8WVpawHFaMFf_X_6MFi5p43IxjFfKT30fJykPpYAc_Dja1ngp7CGmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGBJm5qmD1aXIUKNX5bABFTPE4O0H95Qz16veTlwul0yP9eizH7KDBVTnih8Y4aT2pKAmFczgE7zYvkGbbWznwCDi3M2NczRVlzdj0XINhRMpJwqP7oxpGWzB1vPzCYNeFRTJZEOvyL5PIS94Hvra70Q8D_6nSJNQ3_oNECOzG1LW6-Psk0gXCMArE23C30tT_ZnOdFM-njpDZo_S6vvGkFR335DXjO5hVqh7gmEiT3S0SDcHzf1Nzs6UIZIqkQgYbpGK9gqA2Odfu1vQCI-PJ0QbmfKpg7R7kFyOEy7Q6xpaIRMHdm4DCW-TgeartY7Q4kRZbqxBrNX9j9J5OlJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8AqyHVf8FbBAnJFNKh_wV3cLBXasCsP-WDdjoudeOjWgYdD8B4at261MzDe2ynUeAiGi5kbT-8Cj_QJ_RY-frlHM89QpPZM6kOc7ZS4S-B9U9VjFw_JVF_oES-DEGo4opkW0ofuQVFWjxv0J9JCkZnwdnoLyh_Egakt889Jdd8cC8Q30buSDaS7jj7Aajdkl3xn-0pwol4nfbO-pvcMPZSWVGeHPTH5vZf3-Ze2U3mFWIqkENhMOcyOU4V2hMW1IhINDkM4ATBnau-Mt8RwKxcFvn-LGszm6KfiZ3usVQSd8oruK9XhqUZNIl01hsMGpSOyZcyGUrrGFrCZrKrnnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxgMKjkYGk4RtW3ZtWwllVU8tm_0K-G1dTU6CQk56W9nHTmkMiF_OWIJE9ZYdqJag0alaRceQ80xHAkdx3Qbnb67cBbWPeX8eY-U20_U51twKSdAUmF8ovqyUejcrKbHHAZsNpZJhF-V3pPqf01ycuxOEhIlGhHFD_RuQs832IXLT1DTUbYbVNRmmHkPEIqbhImjD9EvCGPn0f5xEfbwYH0ASwqMpTwinINojjS7tvLJHtyH_vpeyabs7v2Fd0ANzMZMyUFamg_Y2TChhmnr4rm2_5ZCoabmIY_91zhr1t1c1ghAH269sRJK1j3yicmmCEBTNmMBo5IeVpwzcAEKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNfPOtQNkZDJZ2VEI9XsS0A2OvFjYPPj2MmC902QF56rxws9Al4vxWJjcZxAv_RmnnE64wCWMQ_h7MsLQrMa7gsfjBVfyXUbGB6iD0Jvt6hKkB6NGRo6TpXdNGSJ1B3iNAE2hmuQ3Um2zH9x2tY3kKIaNT1deVovWKnENp06MX8AQ1_ibZidotaQtSEvUpvjGiYtWI0U73f5eMszWo0WZxEOe7jdYNVe_dUMe5nyCNcc4dxHxDBfX-ChQBNU-Fsw0m3tI-e62j9_BMcH04K08v5Oki38PoFs-2rh24W53_R4h0imoo_DFkO_Rf15Bu7OCLnwO6RtZTJABZmM3gF3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0Q4Jgg4sVEBqY4SKxbJaOCO2pf-akoPSRCSlDe3PoHSDagT-GGZbSJj1d2C9goQFNhxNkVj2c0Wrxp8S1b2PBZzRlnBWDtjJMU5dPb9E6_IDn5Ob9EdnV1ZSraL6vvrqef0TRdLIb8A3fmXmN2cVzbcPagBmFsTIirWVNviitjBFxOqGJyKqXycrD0OvVAAtw1QaatBWnhSBEkKA-6gUxdQw9Hmxk6-2fKETGmpth3NuN9yB3Dki_vCj3vF2S9tfBEHIAbwq6b5WX8q0FzzD5o0yaO5Ngye5Dxg27ShOw_v3-KgoNUH7cyD1mp-GlN0QRSzG-AQedaYCiVmWR1HPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui2uSarwvOwls9uiUgtyo9vWMpO8WRri8zuUCVnTBqj9Y_RTzbGOxaylGO04ICEfFUd-h14oZ1NzZZRbOr0dBCYXlWi6cvgJWNRl6HMXNugs8QEWiP4jAIt4iiqmYW6sHkGeNrLx1LoLZTzLXx7oiw_bpOa_TUGFb_OaJL1GW--xqh7vSRDq6Io31YDe9FPGwU2q738_M951C2C6fUQnebkzIRfzol8IOXJYWyBT3HKCl7QSU5lB7RjCKXNag54zwi-9pXoAwYGgHSIEdIkqPuv-mvAQDtPfuun3IrXaS82iSXstvsCBY1Tl1wxAGKuI01-S2rc8z9R8OQfAgEizXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drbRZ6ev0Lgyn4F-XtMBHi0R4bFLVYHr3EchRRY5UklyKecuGxrZyfiXm_0SKe0Zc_1StSStuF_eF_OPXrtr_sLXKRiBLKFQVltwcF-WxU8ZUGHCRYzVaFPhzjw3N7TZhtFbWTBnY4RDX7hNaE7H1k9gdm1jxYvGTm_1PWhzZOreuWkHn-Va_EDiAIlhvYm0UfiuAhqDk4a7UyUMBfJToF_LzZYxt9DodVOLMImI9nvqb7tQu2gKe4lC-zJ-eKSC-KjNUGfG1grnYQlrFCS9d2ImgwpadA65LYu1PQ7lYvZ-oegUpRrUjuLvj79h_gESzJpzDqQb_BD0CTB5wSzWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUXxL1ZtSzvY_sl-g0ZMstITw8Hkuf1T5U2_Iem30nneFKp5k7LuyfRWU5nVc6O8Yh20t6JGJ2LlfUQpCA8U4B4mFWBJ2f_Lg1sFNpAe4KduV2KJIgPRxdNbA09QP9e5AZYUYzoaLlR1uxQMRgqpjb9Yk1xYMXZyogg6eIEA1QvxsHT6eREt04NeFbH_Eg0jX2aq3DFoxZZ7pOIPhxYmq71QQwFBwmGrNSGVyypUgjpEHFXLakdX7vVOghmxbSxR9Adv7eHRiQY9AaukuZUP0qh8BWJqnW221xxhOimzIgVziiKD5fe8arE6UEURtwe-crau8EENLvZgi1C-l_ylMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il0rmRvrJMQnmaQ9bLiwpkD5OJypw2d5PILRJ4pYWoB3YydeWsIItaBN1O8WWRAJnGP9tgQJHlUNSVM2PYtzAokDmaaZ-6e-pobmmwfuDlAlSQung7myEZASSDNkBHdD4bXLUry9-h7OR6VxEKT65cW_4dCqE45dM4R22BeCbBM_Pqh0NKzrGHBhKzSTxLFNBaXX5GL8xKF7B-QG6aCdl_7tOqJErg6qBWkvQo2a96txS-4nS_krPXLv73Rp4PQyOEmQCPWRZqTDmuYFRllFNwwmCOY7kTRQX3I33cHn8QkUT8tVU6TfbhW23TfHR76-aschYt9kFhu3grDJ60CQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iV3lHzIj3jLWSmobFR-l_28x-TXIvoc2D1BYfYPKlUELVIqIe0MQdbjPZCHBSxljzTIkjvT_YLuUE5x4e22Uep_zoP9CVxFVZg-bXqLC4KI48OzZnQ_9-qPFLIv6XMVNC1jwo90xOMa5Zuou4konbcZnGQoEUfNWHdjPTvhEdyKMgHOi_RCGa4PGbWooATEYpVKM5WKqhvFtG1buAVKgqpsMSNQcsi8ABfzkr1lAfe1z3WlUY6eXna3rn86I9CRgwz5OrwZQ4rcppyRHvPpjkgGxGuvJCVyaCMlO7IoXzaG1XE5NKItomElXoAnvwDSZ6aMijA87mP_a6TImWHDhkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBzM2CZVtdIYGd0bhPbmTd3L9X8hT4PVDWKEYZRa2GkNBElyb8jMXFUQkXv_zhqBFrqJZw70B-rN4v8SsCk744O8HR0rspaH6ALSEznurc3VIbHNR20SDmtDMVPEtiMs9DfR96XN-Y5-7ISJj4booM36oyXj7Gp3VWNehsvEEwNTVD_O1Co-8oE6Gb94q1So7-zVszu2GWC_Qn0Sq1ts-xstyIdKyTeHMHUs0aPcXgyWCnQAMmqNz1FjjMORbIsLZ1aJym-mCRP41Y6DMfuCl-10ctO06Mcpd_ugjt2RvEzy5A8aIo8_Yw_EM2mUoJisNhOjPhZO62ku2eEYch1ETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpT3im5IiD0TdtOfkpVc4EsY8nCr4RuQpVGGF6nLLpwUc67i4BPth8gxqY5qE36wG7WWV7Oupbh0-HHMTR5S56vJkqpEzpO0r0QkmxjHLy8AGUYzdcwcy1RM7eYVdlEtUbCqjqPODozEml5V-Qqt2vE8x8-P5yLzBfPcsQXimho26YQg8-WHalXFCQsRaq2_sjugjwFQ5ukIziVObz5ysNcJaPwTpkkQ__Rw_fdbzLEgdyk7GRBs7kXhb-XapEwHIZxPwg4wMsgXWHVai-RsHGo5vBeawE2NHo6EAZLSNk3WdcA4nrjnN4iQg9LJjYYNK4wJZClMko1PX4KsMJi6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InHHpdsI3ItWhUfQZqWeoVEpNDWCs6zpX4R5-UypgukfLp9Avi55NVH9dzXQGVLFU8u16khze1KOnGXLddH1rUe29dEh5cv1pyIc630XHh5k1y0M49m7_H3OovC8FlW7hfzzTSx96-gQW4XyDVAxvn5rZG5HW9mYufoI6R1zN---6uMt4h5uA6ROaa7-2SqARTGBvOVnp2T0UNyqaY8vp6O0LaIxNZ5rv1MrYpQydCKLqIfMhLiPbniiKEF-S_t5l8hVDPNaGXJphkArlGx2O7VJrpNlDW2mI807ItOtPGKXnHALFHhq4LC3Y_7QVJUQbdTeu-UHm67lB28F7du25A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQl7k6It3TiOY6t5nlUiTGj4xFDekTHljMpH2MiVKXA0xX5zKN_ryzjaWSqIvWHNk8Oj5Hi1CX8baWwKOz1n0XLi0SJZJHXxEOz1FyB6hT7INijFQ1LWHZGaD-4qvimz_okwgPx3xzogcFORwXd_y38pSbQXYp56LFETK7ghoirw2IbS6nvSBudcztLhpltk-C8u4mepV2PmDSoaockNVeXCQH8tSe8GDnqIyARpysDxs_OjWdDl0pgrJQ2grUGoavO7ilWcZRF1qDFkoKMQWey5_BWYDtKAUuIeuTb_6fduh_aXJ4GDp21b8OQZL9X2_5AGkZSIb44THusrSnkIFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmr_VDOiYyxm-zWdl8Vn-Bxxu8jQ274ipfkl0ewg8cJPG7x17S7ckfqrzQLnDwl3Mz_fmxsL61XSTy1ICpGWczci4dISJQy41NSSGd-zQH0vl8OdyznnLYeeskFfB0GW1NYimAhvwVfbWTPMUQmqM7het_oaHzZNFaqu7Cq3fvpj-sCPzQ1oGJJaTQzMCoXH7HTSC2w36W27meLuqUsIIgxT0rVkCadIsJ4KgLjchMGdY1EO8TXyGIPJBJ9bZMiLdiX_-y1EQWZkkJ70czF3RvWEkCU842DxYv0gBqTdaIX1ZrdkZBywRCwJiRyqB5y4fPl7jDvhG6gKARNhkV9_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKV46vDkOiPIQZST8IkGt72HB8Pu8a6OdSoUz7jR0EUQOBOPcOoQtiGfjGmGP909jXDKTM30og89yktWXxegW3zsbfnF47JuPRfPJjm2WRbxG0H0kPjrJO179msk6ZyoXpeEyG_qhcw7FJQABwYTbUXIxppeKuc3ExYfxdsokDpPBQOAPmwRCgr78tIMXg_hX7R2ddMREVfFk3r_XgMG8zos3EY6cTzFM1mgajpXi1-ql41HbXWr7E09lPjAuyjD02sKK4q2bW5Gd6W8CGPoG9g8Ndiq_vWYLdP5K_Vq-2uw_aKZGZKhG_z0LufIl61uJqPMjcrmcfjpCLTZ7y9GUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNJbs6En4DJvUOLlhQCmJhOb8u9B_UD78O4ySUQPo7WFXJYg0lm_tCrknZP5JLYqVOuCO-dQEoE0G8hJINmrYjeO45jbfVjBVKpYQk8ab4OXqWAUcnh_rdPCrsHJFujHClswj5_kCIpNSTgMDvrwix1vmJq7o42HfZmBpWSF2gGcHFqF0MZ3t6EDwdqZIv9kZP0YumQLR3i2MjWCMBesHpSnBoEIoASpDlx9GeoguXt5qSd8OYXNOTmJSkHtAGkANeWznAqCvftaoD1OmfFjCtsEv0i21n_xInikCYu9vIMaJBnh0Ozwj2o5eX14eEfP3tds8xcvq_-KcIazMcmP7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=CS_FvFDFyTmXs54Wn1X0jyZClBbnUaGsvPYfBPBy6k1Tri2sRYFU9bLdpO34IJgC_zYseywCdOJrVzRSpetvBl2mmgS_rhc5GV3IkvvXZG8tvTXFT40rsAeeQZm-KLS-YuysRz8GNGWIfZgut6VHxMhgW5uchX2wPktkbhdqSeOby-oqt6lrqVaDpPxmKvq0jhc7rCNOBN5vh2ACiPsK_W_x_JDVFdTrcs9wcEm-jvdrifmkm_b-zJaobXKek9o4psRd5AUR1yxMuzfKeQXfYmH3D6jizmtDZdNbv5mZ9jqBG8diHC4UdWYmzySZEP6iNnYqT0VGXuuL75Gln31w9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=CS_FvFDFyTmXs54Wn1X0jyZClBbnUaGsvPYfBPBy6k1Tri2sRYFU9bLdpO34IJgC_zYseywCdOJrVzRSpetvBl2mmgS_rhc5GV3IkvvXZG8tvTXFT40rsAeeQZm-KLS-YuysRz8GNGWIfZgut6VHxMhgW5uchX2wPktkbhdqSeOby-oqt6lrqVaDpPxmKvq0jhc7rCNOBN5vh2ACiPsK_W_x_JDVFdTrcs9wcEm-jvdrifmkm_b-zJaobXKek9o4psRd5AUR1yxMuzfKeQXfYmH3D6jizmtDZdNbv5mZ9jqBG8diHC4UdWYmzySZEP6iNnYqT0VGXuuL75Gln31w9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJrzTsaNoF-6sxJbuiwmsrW8GYiRQmRxa2t47AmiI7u5zHtEtKPAEZqQHBTDkpIcksRNU-ANH1S7lFEWCUpgpj_wVHFLtdgIRAyILQUsozJSTAhpm6KC04s5DB8BYUvSd7BEf2oQ3TjNrYbj8cTNS4LecRpjdKh5OIcn1k5Frzo3Inz5rN1a6J0V69ywrI0fZrywg4VxEK1BzRFwC1M4yqEgsRQopXoHA-ObLqPTotRffmktGoMuwPUGkpBGNamEUvQ_VLNd7N5MPlQiaFSAprYLNV_Tfyo5kYpcB1WXcQSv7Pej5eiCA6D5MlOAa0pUzMsrNWdUlt9QbLGpUk22jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukgshSVWxhfd3px7wLLa5NvYCCDYCkKESm27rgraR157jlsGTQ0OjNCTEDxDo_7YTxFgAkfXGhMWUVod3IsdFx7NTxvPfRfyLXESOR9EIDkTQjqECZyRjYwJPyK_1fkUY96p9Fzoz2Tl3gd4isudP4A-PFOKPaCcONcbsLYTT0zoR9-KXoSc9L6bAzFS-KgVoIhCWvFICIcG0N5fRcRB84xBPwhYDp4PJUqWP_wBCP6cYtdhUhYRe0_FBqKhVW29a_5hr6bpH13VKF0jU7zJYUNHEdLLikA_Rp8iW-S6N4fQBmfSjzHjubwABa7EDSlGpwiTi-01NxjW_CoT-mK51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKFDh5cnXU7JXpdbj0hO_Yk55YzDMGaYoXRVfv5leitcQ2aQokHqD9qL_tmUFOtO9Avk1cdsEljndl85xrazvqSH8eE5Ixdv1WGhc94BbjhXhk9oeHQcELezEqVKYFA6gSWYq46hE2n4MH1_ddp2Zqz0bbV25jGvCO7NBo6HbjoUlEKf_WG-EBiDHYO7EuGDIt8anbK0_WuCwhJdJMXU_DqH1jpumrkHH9wlQE6HJPYE7bQrc20S9yws00Q-BTnMb3UF9wWmLhaxJtIx1quwKK0hCDKgnfIKzN-2iPuUR1HDMPiaYUQph1TgofRLtaXXsxeNQ5Ay7yeIe3td6tj5-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-1TDSDKEvqAAOVqKyRxJIlNfKKS_7XZM-GNFv8ISoA2jldA2JAq9IDKwSaUGdTFV6HY8fVa7wI8AZpPf_c0PXTGPwe1eJ_uvYWXwe80pwNfYDk_-nw1ANtKzghha2adSKfJ-CVFRP8GpurY7BX3F0kygqggWB-0qh828FuUHraK-goP3Ey_THYGqM6SaWB898OutiZ41bANPvwFj0LUnO_D7Spdqoj864DLDAZs-Fo4yg1fU1LbFsczQJ34v-z2SN0jSP0HfjWGlHmHDTPrk4bgjOjoYtEL3SXg2yuybKBGI1JLTQSSN01oIdzl1FzimoeJjpUXZHcFVR9qX30d2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVqxrZ3eTmETA5vMxUeMGGEkEDg-YssMOqv5Vkm2ydhcW5T7cGitezvq6lRNGrX8Hi0dTbOLTQV0_gK3pLwExc_OwQAiY5jN_eGQ4xqpsHGjTEwJRBCQBNgwIJnDMVHK_LmjK54UA9eYYUaBdeRgJRx88JHSBipSlLl4KhZ-X-ohB5S3hf-vUfaY_ckDmZJmVXzB_58P9zVd4nuwszsvgdSRyqHOKE6x6f_4CeaAnE4QtarfGZHvvGlolz--Ngd2RvzvUXEqjA8c8L7PRU8zLj6ZRD0mWxSy21JveYveEhXcLT932cSIJPib2QV6TKkbmadiHcl-MVeVB7SI15UjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWU3jnuLJioKRE2HvSKeNj8X5_0AppLiN5HrAojhp7kbSJF45o6stNIl9K98DjNQDqNV9t0m1SOI6Oy6m8Ne6HfWT4DS5JlPGeGqznulQ96VUTVjV7B_VO2D4Xa_uTC28Al0Kvpo1w5tUPw0MI6aB0Y0yjgBbcftxrjEm-DJPr-oJrmCbAfKAvftKg4vkyk-83DJqUzJJavQcrtxsZ-T7snPZRU7dV_pwmN0XySepyFuOak4qTnzzqAq5odTvvvLqzxMPAqnt6Q4wqMY9ryM9lhigNMhf3FLcJjUIpMvJG46iNbNDlIKVVl1e-L4siAC1Kf42nTvk2541RS9brdZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnTH6cQvdoet5PoBGsnaOiAxBm0aN_2Kh5w9QisfIMEeC-GhMTrmPcnLuFM7mHJ-Uqg1BrhOM6kzotgPj4_5STwNfso1O3ipvzUyC4KPJpVHg6O8XbXg2gZIlCLzXqozp_eOfW-yCpAEleXGuh5yudFdLLGBH8b-J6VrOMsGwtGhQma6VmdX2u1M9X5M6pDGitWX-2SYmGwSj0a0L_KaJuw4AwYsxnA_j1CoQXoPStNQanQDpyDcyyAsaZFDJmOL15A4OtKrdHLeWPYWgqv_Z1DZsZyr2pbv0PFGSfMJmMpqXBFOEabNkty45qtr3Yg1WxcVbz--KZvqt_F8YOcSzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJn47Iwo9W4IF6GD3M-NqNVcSSaHix0Eo2rVpjx6buYUJ5eGJHTvvEb-biF4LJQiWBSiSlXyKvqrggDIusQeXn1V1BtaXscSk_rbFHSbmd20_LEIaq7b7Np0ULclF7KgIvrL_utpeS5WwAyErJtixEKXFwooX-HuyUp0L6OIeQoXwdrDEzXNix4g1a1Xz5JYivIfT45vttOemGVGOPhqk65Apkgfh2pSIQ8OgvXvZa9ybUYzlM2yTw7sN4R1AubYcZrAQDSMxZHLLqmB2btgUqpVrAR0DNv9HRRlsfDV9Br7whJFgsSW6s-U4GlPrV0dvmEAsVSH3ubTY570qGKI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=LRmJ76ol8zOUgxOIe3GUroRGmDZEmvgU6a-07aYveZ-2_Zan19svVHyDFcxan72DvyRD2UteC0cMRs6YsGt4qpQWPsM9c5gbIn-3s9I73eS2a0XAmdneTUxjANTBHsvoscBy-Ww3UnrXSfO9uZ_IT59GF46tvKVQ0c9xhIG-fQ7D8QMg8C4sASSxZUPjx5-qf9oqpklYlrmYKjEJWbW-z9gKo_J-SFhQwNFGLF72Da5lNK_yALWZa66nDSqg0DKusbtj1hCyOzQNOTsU8kkqyxyDhrZbKnryPabsIhTMlACRv30MIQKLUGrzpd-7oVtzdGkLGC3h7vlzRWC_P1oz9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=LRmJ76ol8zOUgxOIe3GUroRGmDZEmvgU6a-07aYveZ-2_Zan19svVHyDFcxan72DvyRD2UteC0cMRs6YsGt4qpQWPsM9c5gbIn-3s9I73eS2a0XAmdneTUxjANTBHsvoscBy-Ww3UnrXSfO9uZ_IT59GF46tvKVQ0c9xhIG-fQ7D8QMg8C4sASSxZUPjx5-qf9oqpklYlrmYKjEJWbW-z9gKo_J-SFhQwNFGLF72Da5lNK_yALWZa66nDSqg0DKusbtj1hCyOzQNOTsU8kkqyxyDhrZbKnryPabsIhTMlACRv30MIQKLUGrzpd-7oVtzdGkLGC3h7vlzRWC_P1oz9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nxmg3i9l-jsqtXws998WNIumzTmYBsn3j_1gkf7Z2i2Bux5UVSpoIdlB97QkZFPEGpug2XpMDAo_mIO0hJD3W4Ha5KpkyZwVphIFPWDnC3T9mTfu7UYF0T7H_pSnBtO-DzjRIBNQsT1c8DLMhqnP11tG4hMEyClp0onpcCMtAJUvdN4yxiq52ACC1NU688Z9GDYB9Z3Qkqn7ZaOAdI3zrDsNLBzESvNIPrzmnr8NjA316hpt1fLFdOKLEkBrxOJE1ChWUf_o_UN27kOQBWrKo_f5ZOPY96hIP9W2oJSY0KMqk83xXYoMUcm0VleY0AYpoNDBwpKwnpBaa3xmAJCIbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK7PqRnK8T9hVTWbWItd9qDEKVIvv05a9U62TRhu6QUfDbZw5dUSJOCUEyJWgng9up1Og-2KpTKM-JvAa9_jKngRM2JKl2-ghbitlxyUt5Ka8g0qutCjbvOWMiGIpAO_-7Zt17ClpXNHw-F8eKX0w03cgCivH7ZvrnPd6GfbaUcJHz3WxlZtUbgEciN932Y5fPC5QBYwaycLCno0_M-58MHuVNuhL_WHG26mItyGTmhNpEoabNnNZ7vd-qgqx7AWRMA-7VJ3332pggG2UUXS4JjN-Zdk2aBedl4wvubGLDR40ywvPZPFXrA9AOgQFNKwpAyXphc7RxKP1yM39Du9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=hyl_Dd2Aq0gz07IURj5qwZJO_pguAgkBLy-LriQ_SjVC9lx4492BCsF8_k3fw2IWa4SdYtncyjk2DR-VwpnO5WfHYeb-O7SPknAMBzeE3UTd6zbZ_2a6ndP4Co7tAxyIw9D2Qe1w7U2d5L-8qhjVyWCvz3Zj-8D4CExngdtCaZN3trHVIaN2thX12goA2X2bzQRcZ8JaCashynoW5h8uTyfAUucDqnAY1MO57OITabYVFDROE6BNCaPOB75GYGz6Wmw2MJh435h78XwM4WtFKXE8vRbevR09Bi2qbA-aKBZngzs3AjzGOHy5rQ04EeygFcZOF2duBG7MWpy4LuphgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=hyl_Dd2Aq0gz07IURj5qwZJO_pguAgkBLy-LriQ_SjVC9lx4492BCsF8_k3fw2IWa4SdYtncyjk2DR-VwpnO5WfHYeb-O7SPknAMBzeE3UTd6zbZ_2a6ndP4Co7tAxyIw9D2Qe1w7U2d5L-8qhjVyWCvz3Zj-8D4CExngdtCaZN3trHVIaN2thX12goA2X2bzQRcZ8JaCashynoW5h8uTyfAUucDqnAY1MO57OITabYVFDROE6BNCaPOB75GYGz6Wmw2MJh435h78XwM4WtFKXE8vRbevR09Bi2qbA-aKBZngzs3AjzGOHy5rQ04EeygFcZOF2duBG7MWpy4LuphgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQTZpMjV14hUCMS90cOYq8FYDDZCQg1MrhAeJD2Nu3WgvX30DPtbknkdiRQ7hcokl0U_MJQxGLXT47zNyUlGl-VYZa3rh9M1Buy7m4pmSoIw16OOaihCSoxwO5IxMIOGECBo_ankNkRx_SldK5roerqPeNeZ5zZ3Pt2MwrljdlZWqcg3yC-sWMDmkrKWxB7Ge6guwfZBzdLAQdXXC-SXB12oGmAadO0RPaWihgWKYwIn15Q5hF5cRauwzioOewZkoxbKV7Po8MQWmIGuRwehNlcx_JjSQigbttpccFy_YMIqKeKP_Ih1sw4SIJjoW4aPa5laMVCMG3XK6aJV2aZ53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SeaMq2nZ1gSf5w4MAdtIf1wtfT_X-_bqpwDJryo2lR-jTVbXMIFi1rE6IVsLqc7oeW0yp-2kNujrZg-FmwlXETTXzut416eRjjFUkskpzAmQjxG33nFEn3Lt74kqhq7Ek88uO5uL6o3EUt586aTC01Hy2yBkpWZDk6Pfgvl-vu353c0psa6SpOadgI_li2ZsjM5H-3-apgA6LLIFGxXwdg_MM1OAXdPc8-IqUX7dzc3q7MN1Tx6EboHnIX9b62mk8wRr5nJDWgmtgCNosng087p0DzsrxR00-wUZsdW42n634CaKLbWxUgI3HQLzT2Ow7CWofP1n0m8RnUIRiIRJ1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seCEngfwHLcId7N_Hmj_OJzHDdH7TYIHpSPuqeP-oBGm3F3nul6LaNjda8TUwXjP7dLAHLnwIMMJxX112Q6M0MNtjWvql9_EmBops06xrMjvS7kQJko3gKBCC39wVPofMLWh0_Teapx0kYY5_1D8qFD_lm-MyggBqKvzbyUYgKMlaMpJ5SXL6dDlIiGPfrXmDVR6m9sCRfnN8nSsh_oAPFxyLqI63bokJERbZ5PEmRrZdFRzbuf0QohPU-IAH1u01dCZYRc7ImFaUnACD2ZgX7pLyZE14FnQGlb7vMdFpnWFP3rrHJE1bEvvW5pVuvvFoYtQuB6YCkyqV2S8-KVFdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls5oXi02B1JSY107c-TryVfvwTxSSLRQlv6yoQFL8ddOeVKSdNZ5yWfzNKczgzOe-vA5sUJEvSxduFDXJ6wZuE4CHzqdXZTv2KwkODgMpQRlEvugy50Z-YydTcBlT8OR3a4gPfuudvKZgqjaC8jyBdf2EVrD6LQhmWdlt5ltX6y1XuG8eodHTFvd2czoP6B4xolgD3OJqiJky524kX-8OGIdsRnAhfCoyjBP99DmFFVZXTc0EUCOpAWcMlcCa_SIoYd6ue0kBg24XOoD6Srei_cqYhllFPmUoAHjw9GsrpZzH8xILpD-R43TC4Tldf32jLYHqgRHf-eSpkHST7GL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vmn5YURIXLPHYFrOFw69vbzjVNYjXJ-YJWwshQ25t3PMQDaQofYL8NKTxleTnYe_99CY0aM35o23IeGwawbLJu7uVpzSv5aKS9p1D8i17uRYfXe2-0Y31871lgX_3fW2aZNpkun06EYFp4t9CwHs6RKZP39FVQG7QgeOCxbiccGKsiNpLXKzX9gO0TBSqLF5WfvHDuOlVwqP1fOSb_SA6kSGV6yIFstHiX5sviMHmxUWHlnVP9froWFwjsoosb9JKFvzWLD1uuK9ona5Zg8hppdr6fZ0QEck7w5Dp61E5l7dWhfYGW7X7TgCsTPWtB0QY0TLa3bwVBRuoTqpfIc96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkIGuqeGStt7PA9eVeCBfDsqASgS_1ptXQZ3vc1wVPamc7a_b0kZwkD4WjY_d1OFs_oawlrfdhLg0IOePziaHXy8QapiUnJxCro9P2N2v4toEhF6YydVM6B6tS_TIPSlWWPD6xeg2AhbJ1kw6JahJNsBy61A_SdPK9EAoDMFx629yA1ylFcTVdNLURvVPKe2nJAQ86cL1JeoKHq5UB7ckn6aDck5By1fvuG_VsgyucWmQE_dYZUQZTDLVzXhE-A_gn7xn9PnLWULnj28xh90srfZe-N0Q-QQN8Q0MascGUopr-7DS7kgKk30hJKZqCat_jHy7q-vTKh88RHAXfg_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veIfAUwkZGB-vNIpmSGr3bPMMK1tfdiaKiX9VhNKfDASx1w0U5yx0TztkITnig22zxmcdc2TXcHBe5UUcZCB4gd4lMOlnz1drc_zqQmoSzKJqxwvogTQ1KqE1oA-LOdbWiACXtSg3jluQnPtQ_-lO2_YDHb-l931UrKQJOJfaoJsNjB0of8tG6zGk2jBSUGiKE2V9nxMVtv_uckoUbGRR6xIfDfyuOV917rIAS0ko0U0I3P9PcuEnYmObsffgdNcrLLOHxFuMCv8dShZ2__wTMQt0oW6JW47h7ilNgKgeHaXRUazyPN7jwOCyvaSedzFXjmnaJ_DWjHJSV1UfQ5_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixpl_5nOmMT0xo1DDIZOdMU_lCALgbnvOPdfeQZHcpweUsr4jEGB5jH74OMJUtTGtwMJsfD55b8Xo54H8w0G4TBOC6Iu6NPKkUYdzK_izHXgJNUT-qIQo-Rg8Vs9Jc4ianvHIO-OGOMHjtTulql5OnrDlALj5PLi-8mV8g3kPTZEwEgj7SH-DTS2AAr6du6ZmUveNvAtGzRglTO0l5vt21aypRFzdYvn7DOeU5Wxfitm9-uUYN7HLBGKVbat1OC0b0Plf6KMOYXxUY1si4JftvRC0cl_WpQYn9os2GYLGbYbtYuiM_GVWHucyNzcySPs-icGofuRd0VDprQq0ajYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxljF3GwuL9t2I3Oa2yd0087Qnzbprd6TlQvNpv7f6WrU0uAUGwlMgEQ9e1IZffhlpa4FcKBO8tzJ07KyvM000NtpDT4AFovq9saUrE7Wp6tiZCzIDHwSjAzgSVvj8IY-G_RNNg0IrUyT6CqT_v2qP5DgnRX5Go51c7jp9zeasWcVGZekILUYkk4eOuxLBI4DZDOIXTosdz3BYsPOlwvbd3KWJfU68bqpF7g9MYHV499TZ2EdBf8047cbfcO8hzVeo7bAlcqsI7_4CWrruhU3IPQTd8JxpUqExkqEwNyVjB-eSjT3KYCVwB-2H3ZpqPfbCC6Ym8x7xxSqSYJrVhzfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCofudJGYKV4_xfebIAYMAgO1RCIQ9-9_o3V56_bhn1rINNb6fVGyF-1H1z9JlbpM3IlnQl_JQeK5X8JGDFiFKmzaxJshlM_6ubuVf8wvmXpug1B-OshToUnG4hOZuDmkRtQJhNN8fkcUOidtGjlEflQG-FdmvBl2Me288UqRvbCfs55tE9U1t0_b0bFkd7vlP0vQ58a-6lERU2YpLlP4SxlNah-6-vo1AXk6PdlelEXYqa7EsBXhfY5GkBSgmMRemT7mP-WKz8Ci_74hUZdS5L4T8nLZO88LEEMXQB21M8Jk3LEQEOGNHT4EG45RjGkmxtfvcJPtarxwCX6mqrw2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUM57494H-iUSb6nb9F5QHRwhSQo2vucKhMvAAi0yl1_XoPhbH9Gs9BoFSVfUA9zQgsUOvXw1R1hNjt0gyBl3TnqjhQ6FtpfNAGFYG8dydX1ibT7wvg8b37gzj7oMVDJoZ4oK9JJRvRZJ0hq_69OIv1r8hTs0XKeIZTraAVnNA_c7s3IuL2IfgehR1lQuOKVI-Mbn71MZXEU2XKHzRQd0dlJ6BEbeBLdD1xI6CB_UR4rFhrs5Jg6r5QyvWnywafZdEzIWkXQOGDQzTgJJEeeqTrtv9KDIILwV24qoWCevafXwg-D887VXljn__og-mUijeIuVMINpB_aE-0DSL4biw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwJyuLeAP43k9wUgolx9S2FPJAUgV3BnXCKof1qguDhczfcIpjmoc2q3eFFwlV3C5bOpAGvIi32hkhlGje73VwKORGJGVMJx96DdrEiMVLIONKgSbNFToKZA2dGEGCQS7zukKlM0GPn0nP4i3YvLJVWeRFXPrMO9eOSb_RBZS6aZMKOSzn2J0JLfEsnjvjGPd1bmpThLNjkH6i-r1FRJ6pUBB40bFzasv8kEdbj9NtNVP5O57rxay1lHlTOuzQElJ42me2--izyvVAOmlVD8SkY1PhsqT1KbTPXruWT1nDM3_U7HFAbn16x3wMwgew68H85TKOHETebgNgTp0SYszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHK9ExSRnrxSSbYhBwor8aIbd8gtJ9F8ymLcTE69oNZHHeH2NIQam5oFvWYQLS6vipEhSP-o0neMnkx6igMFBZCRibxqJ_-Ubrh08d9rEaJLqDcATA4O6eyT7m-PBZ8cbZO0WwtR3n8wnPrkObdT3h4cfBgKXV56aWSNgBlgYZPRGhMys6kn3opLD3yHkpPvZHeJC9j4u0eilKPOb4Yq2rtB_me6Q41G7bk-6aNfiNfAdQrhjiuVM2tWvRKup0aUxaU94hz9a29iWYtQr4vka4ANgHLOzG53azJVLt8F-uoq0p-1g5ryuLKwV8nT4C_blT73rPbc1JbLkvnHSWgbiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLLK21-NOh63ZI2G_5SQXsl9k2JZ4za7x9yGreMde-JTQ7aq1ntykEEkWSQxVn_BHnwdVRZ9Np1xiu2bi81CTvXmJ68sMOZRppjsKYcfImtpB8YfSZXfbK9A-R4PJMY54e0Py140HSUkXDSnqEqj45L2aYHRl492ECg39lnj20aBH6drDb4_OOyXb-kfHI7ey4SPuKTBiRLLZp1ZId-Dodwd9SwPMZtj_87jZXAQ4X1dMtyuU9rty6W-BQ2YI2yWmZgrgPbVmYuJXTwDo3GHvRyUDrFM0QpKBn_NhaufPDv-DlqI5GiZrbM263lxu9NuZ2jiRS0HHL8H6ro4cM5ZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=JiYzCwCOY0TAM3uAiElYfHlHKNhAG8IPXfDZ8RKOeivtWSCqebsrE4s85Mr7JFj25a2HkplWipZdz4hresBtFoJfqFSe4U94VO4tJ_GE8YmnhDINjOLaw5m04ocRtx_bBr4SNSOgvnzFdT7uBDsfrDMJFV9hGf--rnlSw4oF5AFm2INkADscHlmBNR1yeQEbeiWtHYOJmKgrtOmkHaxOvvw5XSt6FaHqO8YNHol_qd3JaSuP1bwrrM6-05kY3r5oIym0sl0c7pq7RhlmfHEGFQpcpv7NkMpebgQRFjdF-jpbZunCeI4e5Reze-HrS1XcpxksgpFCHlSBeZ4ifo7ySg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=JiYzCwCOY0TAM3uAiElYfHlHKNhAG8IPXfDZ8RKOeivtWSCqebsrE4s85Mr7JFj25a2HkplWipZdz4hresBtFoJfqFSe4U94VO4tJ_GE8YmnhDINjOLaw5m04ocRtx_bBr4SNSOgvnzFdT7uBDsfrDMJFV9hGf--rnlSw4oF5AFm2INkADscHlmBNR1yeQEbeiWtHYOJmKgrtOmkHaxOvvw5XSt6FaHqO8YNHol_qd3JaSuP1bwrrM6-05kY3r5oIym0sl0c7pq7RhlmfHEGFQpcpv7NkMpebgQRFjdF-jpbZunCeI4e5Reze-HrS1XcpxksgpFCHlSBeZ4ifo7ySg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYWraFlqBvIbCVEBGu_zWZF7LgO7q3gIXxzqPIvfbrx8FL4Jnq5dGxrvCgy4AC6VR_x4gIlk06u83ZbbIviNQ_zysBN9lUwNh3twtONzrr8Xkn310Qy8TvuxZacWF09WZYOZF6dmvlvjhOG13hvpALz9S3RDznVlVY2z4dqAyxpdqAmDX3M__i_zNrWfVU0Ih66MghQcqEp4t_SeK4ehcaS-3P2_6A28Ko1U520ac0AiAxNp6KFO1_WxIX-lnHK6DrzlTcyyyvEXfWBaG_gqtZq3DuF_hoYHwGID7W9cIChZswg7ty1V149_o4VLBXPe_0SRws7t61zStiWbO_gDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7TVgN6OfHvxgmvcHAO6qL5_4PNWMN0ZGm68uN6m1O2-SB6BL4pTuebV9dngtjWJT7eo2YOPZMCF5jQefxoXRz4QLtjVw5haRNpgD6e_p6I0As6OpDDyhffyKkE3jExMfvMLotJsB09XwJC6i6niM9aWsvybE5yNSCNxCu27cGqOSeGNHXqo5yzim8DSMfccMg6CoYIoiwmVVRkzA42rFzPzJGYxni9t4BdzKLz0dgB6e4GvQd9hxnrs2XQ5Vf_dHQj3ED4U61vTo6ZDGdRuPIwblXFZJTeH_v0dP4NuVyWMTSC5R27NAcg-FO2A7JypEI_1fH7BlFQ9uGq0GMuztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Atvnjy2sniRL6_BnOi3WY8yd-gtXq5KGWOKCvye_3HXDxqii4IQex8ANuUDwcWsscy9KtaHcYefgJsO5l_Y9oF47fK_97cIYoENpuASF1N2L8kFBoClMoi0dV70FmU-TBz8s3FLsL391vR9z82lNG4eq7OOaobkJzAEnWM8h5iSnxkk6UwpSbrjvobDwsFXeB2l6GYuSRWRLQbVCF3CV6jlQ7swzVsyPrYUqtuP7g7s5jddYe33el7t6tKjYgqeqQ43RvYhcYvbUlvZLQsRsFlqKxeFhlrH4ImltVHJkhl2FGLLsX9S-yKTCnHyQrqmDH3c82zYA6onENeqCrjJKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5vT_bxOlfD3QWl2txxvp7UoOYTkRc6ijIjukc5YAPKF-wOVUEEdhjJhoaHW7FpjSm-HPPPptRozO4E15f4E4GOFP0DdxtOw3K88IRrjbGT0fSkdkil_ijP6GFK7FJcpUWkN5oE_hbyTXL9xVI5cBjJVN0IAwgE0R4g-9ovtBsdS-I8kBePvAuMIseBrMiT46BiS4un9x-RR4glRMEZl4ivbkknCDPW1I7Te8sBk4WHAGV3k5tCmVCi9OT6mkjr-a0zLNIn6GIXseak0GF-1qqnyuzZE6hX4dpjxN1Yl_Lno7XTwLcwSXdeUyFA6U1wNFPFZA1XsSajbF6Spu4ToYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNbgskR8O55sqQaLaIVZbPUCH2oVyebssLoG1eZCV36o3vne6uy_KPpTVWET2PTsh1mMk9wAWbGhxB65Eh0Xi1d988juCWpDTWMFVxkA_GSH3PCz4txvGNmHLNufcRjPKVivqYGqys45Qxmi7kuz9Uub-dljWI_HCMolgrRbZJZC9cwuJcj0LKuzG-n3uTC0qAOpjF6WQAdH1L22UbQUl2QVWw5PdJq7ao3-1UgVYCNl6E3nnkjWtJWnHwfCoTmMDi_JIKabeQqtX1Fr9DKVf7c_o3VyQL69H62nqbX2qsChoZikwUH3ocqyFNKyA48lK_InlSOgBXzEstxN0-m-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1hlLLo6CIrMQ8aCDEMCTBN9Yudia0ZQtKouC_t16CeUyVARF52S5nl1qaIhu-1bnfGMGT1dN_tsXiUioQB5eFc9FD0EnKUnx4rqnotx1HFnPt8bh_KSuidTbrruW1CaM0EYs9t-n3Y8r9E3PfiT-4Rlsd5aqO8ae9Kcwhwz7WRoGeWf3x5JNu1oqrEOQP-FX-ie7BCyOOCSjvFccaBUNH_fBp10aZo7KmUVhULfmp_DjWZdeeWp5S0yQmdxfFLZWqbRPWrnwVQI9NBYaHlOmPjJ4-67zgdMo0s5__M4E32SUS4mQcy0o5Z0m2Iu9GXP0MlF3JjdYTRR-9QkWz3o-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAte_Bk1wZysrHuxFqdUY4aD0FW-QfFLO8i4HZvera_m5gu4Tuq2RO8l4-Nc5NhgmVa3xeLR7zcnS9UBNaBjiFxp8uCwjR3PsGsXEl9r9n21CTEvcQcLa7s4qun5in61swvBKOBVpLBOgRQH-HmjeksMk6oSryvP-tJDrdC1I9zT7UWY05DmNuHIoovZfzv-BW4oaQ833k4JEHESfSS1ZssOHRHpnt1G6lqE325bU0QDnRWLvvTSLZyIdf4ZPkOIwB0oWjlVKTjgVdXgyZZGcGX1utF6cUxw0kdpgAzM97T_fDpfjC-7ZhAwQEpstQ2FKW4h0svZa1SRMl1mFlTKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGHcAzcvC044aTPdJYaopepohfAx0DTRtEsKRmCfwn0mywSiK-DAzCmlSTXHE2sYUN40OriPviYBiDLBiTQyNAKIYMYPFPYaEcu3YQ93jTECL1M0T6Mf2dyAJm0a-6I1WVy0Lr5e3_2iwvNS93QX5-v7f9q5cFRlLrViLV5hzw8DwpGhbOwKjKjBx1_lqfufnKsGCIbhFrC9v9iWOMfjoh6L_h4sVbWnR4CnKF-lGrTBNkQ8HWXAVu1L_P_hXWFbpiFxrXX-6kBPmBGV0201JVZZ9xKSOU2Olfuo6nAaZNE9xGHahKnz-JLLJNqtda9HyMQAAh-wcBJt-MnKn-BkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4mejzHtTwODpEev0_mwRTUhZd1FQLNnhg4FYwnpswQbz99Gj1zCoNo15I93HtHUb8nx24nKy9preV50O9rT6w4tdc3oluHhHItG0_HNqfiVN1jcf9SMWJYnFshMxFyImYpH-N7O_vbBg4YPzbZtnEcEzlQC5mxQhbV81q5aZ5sR9tbHnIDDDLpTgg_2fdzAJX6dzi6DfbqIn68KD5ZqNqy9C6Jj3KBxm3BsSTeEw392AxBbwOMRunhqKxCeeYcKcoymyyNE8wDfjYf-ZYrJ4zBnm7Prak52uq2hUg_O7KLp0KAflLiL2fyau4DNUu_ufPrUvshkjfZ5DTXd-72wyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xmz2ctWaiEKS1yJ3zjsR7eHnmiIgqGZ4QTdI6rxatq2nu1Gd_CjyFpMw7mbfzIWAem_4eA_Ue2rQ9Ek6HKgTtcC93GO9F1AV8CbiijawxKtghiF6X4QYNvO0DxAH1RB8AdoTbGkkm_b7RKUBcCOoCJGvkQRSUS3UkTeg0zJBp8wUfuZfdeoYNpG6aadYw6og7kaJBG6uxkj6TZiKGVQ1nw_UukvhJ6GHx45t5VziXWDXGKfaBsudGujlvaP42cLMmUMfSMmEsMtnxhIFmO4VmC8V-3h2jvGcoK-Web89hf_dHaowsWm3wvOGpWjrH6_AGkgPaOt9d8Cv08Crx7voLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miXq64Mz-8q6cyBrx_6koKwi3pp0VBJwGV5F5UawYoVxQAfltRFJApOeI6ni19l5gSD9z76ZUGap1Bfgd7egE_MWDRdWGAiGud1zJRwv3ESxN2TJm_pTFs9A4qxaRw9aEhHOJRSVKVPWxcpwJKn70XiFVK-zeP1VxVTR06ILjjErsdxJmh5BE0AQVC1avW2hyiHGVNi6frF2kBdyul0OIa36WTdYj8zNlCUP41i8Ojcy30UkbBnZDFM2LenB0EXE4UaSn0KC1leZTdrWTMy1uF686uDH26ZED8HRjmbJKz_YSfpHSbDPKX5qxydp8GwritIUPW996TRsu5hg4zPOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3hXecZXwjBzxjq8niAnMl46pSy-KdZQN-JNAq63THLPYjN6AXzE_PgN-J-VNtsgeV7FQqGyjUL0hZr3kP2ZRSyUwbg-dP1TFDQqD9wRu9ooRJ_6xK4DRtDbHfJcgnPWRHiXQ5eETPamAGFR1SX1pSWMZMlwIDjxw0Vt_E2CgoUt6OHOalPjUrmimKCA0Olod2rGHD3tLxZmxx6C3Mh-JpAFs4M7iiD3BB2ya2S2oRQdd7bmQaWXedDMvopmDpEJvPZ7ubwiLAsRqQHCms6e0j3yej_kd0rMDoEPyHWG9yHYPnfp9rpDMVmWRU0qs44D1lGrnjNiVw_972Mkj3-3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqeu4q87UZqDWPmBU9PUGrfxsw2cQw8TRzWfuDYffFrTbDemQvW3udB4Ka0S7paYJVBVO4XFfA_9JX75DVGePW7uB0-63nMDVRqs10zrO8gffMfYbU86julwTpBr7eX45WZ5qPvF-6pD4zbJMwCpDPyQgMlmzMjudYfkDFm2SjeXfxa7r0khDuXMy-wh2KB_73YS20tQJuOiFyAIb-f067angHphL-SoqTagBz0x7snEVTCRtsRvFiiL4NnSYnulPKBXQIdQlZogIhzYZuxlAc2QWEkWIf3wpsngnFf-eDSCRVlL-73uAnAYlUs72T4EAaZQfl0ktw005z6CnMDFLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCC2pA2PUKWvX7vj9uNXMZ7VgdT1IbyJh8UQUtgaH8OV-tPNFxP8Pi_lWdQy_Xu1KTWmOYnw717HqnmwMVNWlEMvLHR_eTgNrAPEEmqPvabLxaqw_MMnh7Sfm3C0egX9EtI7m7vFb8VGn2WcJ8h4W8hAQrgtt60EgENcC_xPQlEOSWmooopAgFzIEBskm1OqwTnRnQq81duAJE1SN17Q4ZiXiFkCcTWmpEzvUs-rZ6auLJQyDsZ2lq4wJ1-3UtcRFUu17P-PtjIKcak9StAQIMey-M-FXsDhV85INhMDBpHHNLWhvGK37eKy-b2AD4ylPlXfG170kPtRlbvShmLM8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4W0hPlKX22DWsSh7juLmf0tVRWrDZK7vpwWDVjGX7TmLQABTnalt1aVIRFEhE_9xQ0xxmn5tK98DmzB1cZ2hubaao0yb_k5uSlo-q-hBe-u2po5zlwl0E_FzC-G85IRfZGR8uwkdxtHepWNE-IMGDBAg1jMtp9I9xJtoMKM8NMXHqYQDjnyyFV7VAS14EiZArmPaPtdpwNdSNYztKsorKTIRhyz6P8i_r-ZVU3fTmkebvSpBiGXqSkll2NE7Fz9hT32FPhPgVNcUxB6FbR_-NaF86NEfH6yxg2YRpTSLk3UyjYyoX6yc8HsrhKeNrKeBjIiXnoIr1dWLgENTy6BEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
