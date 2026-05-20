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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 23:33:35</div>
<hr>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHRxCcWGezD6nf0KR6pKAC3ScpkpcJkgIBdhK5ZJPdM99kp8coOd21NLMLLCzt5mkbGFTEKokuw6GbWehPaFBf62bnSh6rqM2zDBhlKJ7d00zyv7WOk3RubsdDJ9QBsWOXRlIKfIjl9oWgjNwrTP6RSDcp-x4FxuTbhJBepnivgwsTCOT8VGnqLM0iiyLFiot39FGXqjTw9f36w99kN_SgQ27DkqU-R3DsrZJUZ5rxx6EHtxiuQETyam-Q4upkParSpOZJ4u91I28SyVIzFgOOumzillUEn4GNLpf_S30kiFE_glRukaksamAafMOmOdwW4FxlZ7DzvidoL8hnvQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJOqj5SfJwQNcqYMr6OnT4cezIl4cGikU6ntyyC6nYb5BgZ2csDdxbVa77-0M6crmMWYx43zmwnMFfEohjATBNhUoY8Xyy0OutCLnAWtMyJG2c3w7VRXxRzByR70IptS3UtSFM4UtYQ_d_rOfFRJkvGaP63rwsT62HLRLCuLBmqb3oRCX9_kio2EijI2s2f76pmKigiX8wRxXX_clx31xtlZ-_CvjYNcmo1cxdTT1Zk8QTnSPyHCIGr-_R7C8Ay_w_f_Q1PcmNUNnCUXE9V8H6ClZXWkrSAuPV976MY0-g_vE4UhnngRc0dTjbLOREGvwMkGhpfhfhcA03yOJiowDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22203">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYwoNAkZmSlOv-mjQ0sKZiEIGBPPM9aQRL2kNCoElekUpIA3YPT_Ktx4DQHi_8zdiwNmysd8Egrw6XXbgLdnga04ds3hEaYzST9oaIRHFkbnJ0A8dIF95I9IOXXmM4jbjQUHLPvuGuFi0i1pl8DMhnw_kJlHKvKA-UbzOF-XEd47qSLWjn5t6S4qLVLAR9eyMfdgiR9QnaSBiAJMDF7QVgd8mTTSUd1mV6zwF9c5mQTHmEY8vu-joX_Sl8h7z2XfkPaBfgUGPY945VcXgSu8M7TC-Dd5gk5nwoBuJJZk5YvlAk4lSpELyw2oqH5_oRofIW7y5w9hA6rIW580DVEB6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چنل ما برای اوناییه که فوتبالو نفس میکشن
📹
خبرای لحظه‌ای تحلیل، حاشیه، نقل‌وانتقالات
🟨
مهم‌ترین اتفاقای ورزشی پوشش داده می‌شه
🥅
یه منبع‌کامل و قابل‌اعتماد دقیقا همین‌جاست
▫️
https://t.me/+XdSZ8OmU62QwYTU0</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/persiana_Soccer/22203" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdxLx5hzevnX_wfbzRu6ztRUiqtOm6OvD4WYr4Xx378sJJi3ecjzeIi3_OxjJ6bM0beQRvsxuYRuijZaJu-J0ydz1bKDxN2oEChhMqXy46EHw_qVxH1as8ye8VqfLQATsW0dSBMxB6Ly8VPqlDxU_2Oq-SqYefjU8hnGKD3g1SNIyLIsf0TNZfYPGzEN8FbqADUFKNuzw9RtE5V3xh4bRiFD-rbNCrs1_Oy89jwAyZ2zdt_vPBBIolvCy8f-gGdiEAzxQXFzPO8hp0RLaPKYofzJ0IFSRPPfv8EnJVHlWV6ChQIGtuqsys-Y3c8dqEvOkynJASUtG7JhNKqIHYZvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lP0yx0hhl1ztyHrt9ERWKOumwuin6RVET6YKmxscGey6ZBgGyhuk_9TsiImH5VVt7b9bUmmFOpSTSuppPdmptY4nRydDyop2xnKyPLCUJwZrFgpeh2Gpx_SESoRdokALd7RAzKu7WOchzRle5tPBEQgcksLIKmFD-uw9EDYpAk_Zjm6_w8smaCjUhKu6Ou91ck0lxZKqnjPgfGqJxwHpoX4JiHhZzCbLADEWRYuw4abRRllZvO_NqOpVwTUvw4RqCe-xR6YTO21rsNcRgBsxea2BogV05m_LBgxEozVIQneHJCIznOO0jSzCmJ8aQrCJ7yiIcKaPgWFICVapC236Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgtw0tmeZ50w_RNkj9yBzKYmRTYgoRtSvP2Dp0WPmwxhVXmYIf3Xg1BMDbhQgLb1sgi6kljkb8Qjo5JZNH_ThV9ZYr0J9mlgQhDa_i8_rriSTHuad6XJQd6yJwzu0nJk1oDf8p03Fpa94j-r4jpqzpqakISuD_m2MVZueyEayWflHFVZzAKsMvrUhXDTpnNoElqVu82w_8PginJTwpW6KwI19DfDlw-FphdOuwPl3-beq6_WbBsaxkROWcOI7sMlvyaaKkq8vldPvZopYZwoYc-uwZHV0YoFLuEzYMHfem4gznz5MwlcRn9kXJhDN8H8Y4YlBQXSaW2-a79ra6acJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceoGJv0ojutbhZ_2zF0TVaYus1enO-qRE8nJTmBQZnevPOj7WcjJPKaaMjySA-xxGvZcDfsDh5Eg3AfIKXHNyWRsa6Z5zgg4mkSP2tjH_AYnay-teksMdmuf7N2Onne3Vdv2eCCTIR0hCyyLw2kxzdWMgpIF7SUaSwyvdew3rXj8hB9w6jfgQ4ycus_kLpM3JOxJX1NOdXuL7nIEetzUV125AB37k177R3W5Gj5Q1mQhT8NMde0ltrcSkEL1re7q9e4YWcDuD2UU7aV7ZzgmRd2-V-RP7IGklSg6V-BnYh_Jp3mw3HnYQ2faLVHglWFAR-SentGgx1SXanhcU3Lkew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwqx5rh0Ongyjaa_IrDuVrgcGoKx_Dki9WXI1OnoV_jwVX76LEPbv8afKzeqdsGhlTQ1oeDKq7j5YpPkKWAV8kUu8O5KzqKJImxb-OJedd8MKubWYj4vFcnaVfhwBwEjCymxM7cPEfkf20G_JJJbNOocYWcq6OO244Y4uwU_l9EEw-Yfjp061-yRveiqu238i1cOUuGv6rX5PgrrNDdL7COdg61w4nKOezgmQBJn8AMMr0TOOYaplBqcFoX9zU2dWcjTq46wHz7M5JImKniHZI_h5rKmA63ldAznEHJKEjn7AcP2fPvAXM1VGmc1QYAwJEZ4bveYGmBzgv37-gIHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZuOYyx_uNxkqSImfVZzEzQEssr8M2bgz3C8Z9PrClRpGzudHSOyBOTgfdgPV4_kY4d5ofqMRIV_obSEZDhu6ua-XhBruxpXcnoo9mB1XlZ2Mc23nDiNeo0lYou_g8g-_sylE91xqUlZLJxLCwbAN_OWQltmIVTYuqZPusLaJ2exxePX3-Ss2Lf69frlCl0L5YQwbpWdH-22Iv68cg2aK0jVJozE5liG7BpW_hkFpu8h4ktEQXR-Ei-frWYrKm9uMIKqQYAEwubpr_YaFAOLv5Cz4qUqQxGtvkKMyIvHTN9zdwdgx_0K2v5tZn9wTaY_LVUNOHhfBuTccVKp2XPCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_pLfTPtv7hX0PVo4PP0E5l-het7O5Y_uyUCAE_Tm5Bopf2uadgqEMrYCQ-GBcp-dlv2C57JBrPKAz6q2JfELD7nFq1cz7yef6oHFx_X_2HJxhpWlXf3d8q65hJkx3u0bcHWgevsMsqVjlAYrEfy6INsem1n78-OCtvQyA3W3BnC-9scZZPd7Vcw0p7iQUa3YgBx_cw0y-4keoX8oI7VHFt9h2-srfO0k_sq8MGF1Db2hGwgRcEJwxE0X9c8WQmWUqTnfJec1aWOrRmoC-M5EeBEC9OLfmp1dDyAWQafTam6jFXLtJxx-p__YIiLyqTsJf9AxEtTRY8TItFZ4CNCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdtxRLVFMpp2LgI1210AbRrOQx5ds2nrLne__PyOjheXSZ0JmpkCAuc-jfflwz1rjw7XdIKxgP2aJgqFfgSVQimNxVjwWgPeXkZ4KVw1f-JINMhxMwgRGU6bMIyMWnZPx4brMBplCox0hTN1axjkI2Xa2okEZDWcrW9U317KDXVv8oXwmv7HRWeaNJPUzP82X1rs643QLD27EEnQj_sLSAJhq8cYksULlNGMnKNqSO5dTz0SBlN_y-d4MbCpTVD6ejj7kL5ol5ldRhxPPIvU0Y_hK5MFRVXxfnlpceDEmY5W5_mNblh-UIigVmohsPpIGO_YX9KPG__qOk0DKQiUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIaJuF4sdJkVUO1yoieUQmnVkE-yCYbJAjQZVgshYLmT3Jiy32VJS1dgB2G2YeO88CZdT4zsof6xYq5IyZwyxtcWVN7X87uZeSZstNi5TtWyVHvCaekW0DXEOZf4_mgMeafd6-wsVh-dKFWP6Bf8S_G2gqzzAKWmw8aRrN8BYHZFbnuJqiFILiyh9389dzt-rLjrAss-GfahMON2gBRQNrWd2J5N1FQ9DSM8Kzj5b_7uLsQ3ejnXWEB5V2kxBy9NExRaohd_Oka6AydJs-2jxFj46cOgDbeu-XVeLsaxy7azIvirhpQeCCf3uJP1RwOncO3VYsqjZucnaJxTzYnwSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me0Tkz5ooEnqVKZFCA-p5NVfKiU1w-rReJnKeJ_d5Bc3HsguUZlryRCaQwbExBCztSiMvPkuAWrQDuKTDIOd4y5rksxQegY0gFCetCFVTp9NSWpPXr_bjFNlNNi_szAk1pdwVjS5WDzGGcze5NnSwAVYd8TBWBhi5BBVDoenfzmQ5UW5HAj2o2eK0eulv2HxQ21i36-bfb08lWKowTBUk9RTCrUMyrSzqrKn7Rf1-6qgvNdM-cm8uyn6gLACby5F8Ew5xbL3SUKPfq2l1VRgnyextKiqYBqC_KY32rp_fzKeqRqIJnCAYyK-nVh65LwdnwTBjeLDk6l3BRpiDfWJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwux93A2rCIMYoWLeMZ25KE657UFBLVXn_euMBGwOCqQKCghS9CTNtinsbzpwNfsNUUagtiXUljvy7WvsiJhL4u2mq4cIff7Yd9kWB3rOmNJkbRsUZqne0ja92spsRSmEhI0yQLTUu-ivek_qL6wELEFY8Z9athPjJrKk45YNIGnHKiUJmyFap6MJ-BINcvBry5SIHzmSbH-jxUHrLf7HC7mAnAi_08cdMcV3Nfg3t8J0CZTsxVscbiktfOXSFMFTXL0yGuNWxm_gO5BtmHd5IDAq0y1LEcb8_PlzzLdMH2KLFYlo06pkrt2PRHN6ThThSAqVHG09_E1-QT3uCtoSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7hBI9NWoFKIB3XyPuUU-LQ3RRwBTIeQOjJ_z8-wjW0pMtUY7XbM2KRhEp2Efip8WD-ghxKCvhN75zQ5ZZLVbXJ6D5VdQt9BDXfpVSKSRbeksASMbUwqoU4rK5Pwe33oFcMFgrIi52hY3fwOSEQ02WWTI0PC9_wQ0zGhwsc7cWYjx26c_3q2hr12Xch9rB_Ebyud4d1POjSe1QTLcv5uM-fbQlVqwnnVu-9_1Gt6A__86biO9vuv9m1f8TBmqhQO50xyJjjaJ_kUNE-j_AvFo2Xdylzfl2jLTMntnMAgJAYZPbcpAzNWbWFf-TNp36SzUUSHE0dIhLMgIOtQTpaLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6ofVvfNyj-aWA4j9haelPesDryqX_Fc1pTbuINNzIujxK6gCyWXWwBTJ_tNHNhLIUxa76FjvxtfFzz_jIGouZul_d_kMpubywbcuE4_CU7fiqpEr3FF3ZWpRLkREpqNycGMIfHEffqe58v_xdoT6vxoMpmq5Mvgh68IvXmqOyT47J128dm4ZAD-lRzTIafjOwxe1ZpXpfiuFJfBF18egL-GSRe1yHm7JWhlW_LWdjp4dv2GquErVxT4ITZhgp7LabVW2LQBUjozhI3qbwJQjOvXBZ9Swn4HuEK8CfJeHiiEut2IErZyUUdkTGhVFKDNHy4plp8cEMl4UmZKaRr-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgJWnisfCNaCVdujDf9cy28xWwbz3Oq-GGYDB0sZxAIkjl0lgVK93JVVNWN4P4d4K6IojEoCFiyN-8zjcF5IMqgVT9uGxsYYCUxa-oIqkztVgJSBjE84kW6zpnFWmH3r5G_skryoRLhDwiskTN4kOT1WvmqPZdDVkOFLfjJtKws8MBvbp2nLqh0wKO4ycn8Jl0tvW1uxkJT6JAzL9G8eElsScYvZD5OFotHrVijNM7TZ7d4qKCypBuwEaECAYewa3U1S_s5v--_0jjD77UMTHfluOcZXV2nq0CS0Ab1SZj9yCuBIRH3kMy3E8zz8o42aMMk8_24Gr6cTPcCVM5Qykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=SMSgThEq20KoBrzp8Suut3uYEP-LUQism5ePmrtiJWyHXr9zWU76iLHwcpYInkXk3JDPNcZIJ-ZnLb1T4-3gZMsrZeYtjg0EOKvYTcoPRXZLYJ38lkb_g-pm9VdCVmcQayimT5-pU_TMElwSN_tpSYvvi86Atcca-o-cp_PUnBY1wFmFuRmJKQZpQYX7xNXXP1IU7EWgK96XzIQBqSo7Gg-KwL7qk95dxeB7QrzjN-71htvWEBvCXIOLlNu3nIzXJSZ_40t-ePUdsNzZ26EoOEw8XMd1Z3h1d78B91LendgydjpId9i_w9rTYH_nPqz6hag5MNM6YmAj8EZEWx0_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=SMSgThEq20KoBrzp8Suut3uYEP-LUQism5ePmrtiJWyHXr9zWU76iLHwcpYInkXk3JDPNcZIJ-ZnLb1T4-3gZMsrZeYtjg0EOKvYTcoPRXZLYJ38lkb_g-pm9VdCVmcQayimT5-pU_TMElwSN_tpSYvvi86Atcca-o-cp_PUnBY1wFmFuRmJKQZpQYX7xNXXP1IU7EWgK96XzIQBqSo7Gg-KwL7qk95dxeB7QrzjN-71htvWEBvCXIOLlNu3nIzXJSZ_40t-ePUdsNzZ26EoOEw8XMd1Z3h1d78B91LendgydjpId9i_w9rTYH_nPqz6hag5MNM6YmAj8EZEWx0_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuoFetV71KluTeoswC1gAqnqBoG0558HjBOkLrEQaBFwBs1BvTTiNjjkvAihZyZiUxR5YiDBexVeBf-JkJwDvtD2PSpvEJYCC8Dv-xz4cIm0KsKx2dHgPF5R718465leRUL52IZwRV5wK1qSeN987wrJGaoaucA72WuPYmZ4oYfJpF4MWnOQSKonTSBf9vByHHonpY4hutozQRvhE5-PycZiRAswVqWEv-1utwhTGqhp-JY9ReUDDMCeRvQ1s27Z9p6LMZfKbpirA8SuziPQySpHo3MvqKfFPgYw0v_pLLAXdCm4rdjfUfpCq9mpq9yknBtifaFO7nUjky6c7iHweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJdltt_4g1ii4pqVrC7O4Zwy3K5nUFZQO0Dr8l9Ju0b3o30_6-Ljc97rwylZ6BsOGucUQl5taMMmVca8Fpml0M8ubF5dh2RINTuYk_HJ7Epd2oD9cUOMUV7B9Ybjq4QKj1OCaUAjFxPF28HtRf4dXMKCVLwd4N2lhcDHfxQ0hG5AFTEIvWhHSjY7tM7H-a8UCICn_IXNNUQqE7YmH8ktzcAph5RZSB7KUL7A1blSRb5sGH68o4LF5nvkER7LHmfXBWZL2WxEbHPFlJFKvnN6DJ_v3eXecaJLqQs2B74CaDFrLKD3TIyiEbmxbKVEE6Nx5mG75cbX-TrU3is8HsQQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ4WmTDtq_LXhgtjXy1IFKRgzdQRcdlYn_bbMS_S-EBKEpOI3tMMBZyPcDM3T8K3-XtELdvtDgrDhREB5cr9ncvYuRnrC1209pioHxn6SGTIetLM4NZWbefbU_458BcecpBLVkezshbOwDNFzEsW5wI4Ff8U-mt6WGowJshLLNZqLbzUfC28d3-5SrfvUeAp960LdJazKAj83vAA2uaEqAXwOQE_NF7JM9joNvhT6pP0sxEakzslzNDCQ48yHHJywy2C6YUsJ-l1OnQ9LbgyzOT8Goy3kV5qPU1ee1JuiDao3Pao89LKDUj2A2JHLK8dxH3xywNzePu29vQFFx7E6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfJEWFFqT1NWUJhZqD142UK2H8LkNoMmQTEmP99cjfiNktQPZexOc9DG3v01lktlbkPdYV2XGADdaUlaKog97RWXXbnfo4YdpqMTGNNTn9B0TUTHaPrSMSas4LZH1oeygsnUC9sQoPVIqHe8L3R6UW3Rg7qL_vXjwtuwAXwQHrn5SI7Z88sKXVJi3K_oDz4V3r4nCKRz0PxXU5qNV5h19O2jUI9dSNvIvRPXFM9QOZNCPwtrYKFW5rxfc4qDWkxiRB7yuK3T9j5yV6DcnWK2GxKQgn7NGd1s4lE_SihRYciQkYHq7ifPzpjqD2rhdCFE-PfMgEMVU842999-G7gCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZ_mD-_u6zIPYuRJqvfXSfLpP-Jaa-RXo81WXmxwTrhFy5jc2OTpgsb5Ih6o4fECbYiTdDWp-Mdq0ExMMVPMy1eam9D4LVEF6v1td8NVlsax3qD8YCzRD6NWtCjvsbTAK2EwP2nqtp3AF-mDA96GggUxSMMjvDRON9364AgJ6sLqyXo9gnSgASbq8enPsfcQuJgdI9NulPqNb1yYi8TmVcQS_iIuUdhAhoQeucF-AcMJAYu-6r3pHCP-7mFNB_Z3t3oUusTp6_yktMP2PfFr3WNvlrwIcEP0w55zN0eJmeF5LDbKJbps2L8WC2XlIaCMsSG_NCP7p49aJIrYTpx1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGQfON1oBeGi3z53RglWn1GkQ4XksgTnvE66UkcNGVzFD5TaJSsxz6qi9XrwCVKcGyQ5xp5ty21NRHAOQcN_yn_CoRv8ZHVcb78jHza4PMaaF80-tzPwTXYWp3aHrk_VKiemI5LCASgTJNF40pJgIfh_NbdxDX3iyHUozJuChTVioYCAhFB5Mc9naK88UrJWrZUcht1tG04UMy-WgGFFhqMKVHV7L4a_hzKIXrsHBfNpITY_8WuwVxbE_F5xbLSiA3THAqQ13906hPYE8zrjbhfdeRXHx2v8iSMJ1R8s82Fw22csGRgA0JTSHvzT1DFHRLdP3Vsf2TCj9UiNUo2EGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrA7X00SKPFI2m3OEAKOAFMOkS3OIVMl99op8w5RHzGyxwvpBabGhAA7Mua7SUg6netXDH1xT2h3GpxQqpfc2iDs8huxzW7u9TRbuYpVhdx7iS0Z7UEU6WMwUTa3jvOpX1VV-3cI3k6k7qIreWBtgNNC4JYCGU5ELq8qvnP07pBAakKS_xc61jgJ7sL-8nYncnUTvSCnY_CpsXd6LSIDMmhSUBE91kejsaykydyvxHI450QeReYcFqjmfnQPG9qm2ZhC2yEJj1A52emwXKBwPMUAofmiGQVkqdqCb2RSCaR7PZbViUC4QUrjqi5OtAkLSINk3j3u779fy_wtIz1vpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YylBHrUJih8UOLX_Xbh3udx1h8HuvvvDREFqpnE1BaaGg72LVm_10-w_8O0964HEFOOcsMoDmRo_C_Bk4NinDVDKyB2HqLq3WmQBHpQMhBFg0J8-2Z-btv1JA1q8YfbSv50nvJscuST5NOVbMee5hqSee_j23-BNK40JN2EXpPGRGTAi2LlFVsBZgk46YRXRuVGXQ6FYzPmnTVxM0zVou0u28fyyjsi6U5I_pGFGK4imQB0yXYzOKJORcmH3Tkv8xJWPRt_B7lg3s40-vu2SKNqAwOYXP7YyEsmLkoCQCPJdbFQ7tBW42ItKGZAe2JZlWUoH8rvysqMHcCw0iqfG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZZ9ufDq12GAUUWJ0gpqrI0Lg2hivlFv5VVmu6TCwmuSK8B2Ao85jCgd-ffFRcsXGkRivc525JvhYFjdRQABhf7tiFSNC8IJywulYrpqleeoN-rahPvt5wCxRd5Ko1ffZa2fwrO8g9hYyspbkpfGk2DM3xWxkdKfxuxGRHHw4moxi6jqQQtfxOZXGM0Y-QpGBWl9Bf9qXvyMqnDDJ5FaTLzr6ebK2o-SlOOSF6Ir2416EbwXCpDX3yWE82KbUjD93FslVL10LxFnByXanPS0mNCqr3QNVg8ruU-gz-rq2KyRsx42MSv1Ag8X4hO_UGCB2_4dEwqHceNzYJYiyncUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=jIO6LNMvNNkhNDcJ70GE5PVbIygkrimp9AyrJpeaYvTa1920noUoD7WRvDU5c6L3jt7D_s6lSHYYh0Xcj3Df8S66GqE5jEaHl5vOdHYb_xPqahRxsPCAiTMjvPPa3KA1Br-PJoZNOcPt6oEp3_qo1-SOCvhCYfYDzxPP9ONzCi6d1tIMiB7ZZmVhdyZPMxj7ZihyrUgCNqj50hLiROt_gw2BS4V__yP44ZaZaMfarsobOle7ngv0ROoPaBb2j_FMHkBkGCidJhXnU4jsZ8mEKvvnOfxlwCvCZa8dJRBtq9qn8E-IZLxdE86fHaz2-ohW2qkSn8LQNyLXz91gCvydFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=jIO6LNMvNNkhNDcJ70GE5PVbIygkrimp9AyrJpeaYvTa1920noUoD7WRvDU5c6L3jt7D_s6lSHYYh0Xcj3Df8S66GqE5jEaHl5vOdHYb_xPqahRxsPCAiTMjvPPa3KA1Br-PJoZNOcPt6oEp3_qo1-SOCvhCYfYDzxPP9ONzCi6d1tIMiB7ZZmVhdyZPMxj7ZihyrUgCNqj50hLiROt_gw2BS4V__yP44ZaZaMfarsobOle7ngv0ROoPaBb2j_FMHkBkGCidJhXnU4jsZ8mEKvvnOfxlwCvCZa8dJRBtq9qn8E-IZLxdE86fHaz2-ohW2qkSn8LQNyLXz91gCvydFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=I3NHp1jHRaUs0OqP4aFQbvQ4BajdPgCOlTOhXXPxgRa4N2tNsjzJLYxcaJXzs4tqWnuKbmqckozUzxlNSWYuM04QbyyvOs2y-1-zwJ7N0Y5rMOAxboiP0rAVAaEMWDYTqSokTI76DluaNIbefq-wuFU2Lsoq0_97SMZxxB7UvzGnHNS6GuHls2dCKSr7XkDreDvyqqsYIBLSagbnVJXh-9JzinP63DsGV-0Ds3G2G0o-_gnTZ0VdmyYCAL9PiGgJmnLLEep06f4Ji2_V522RVzYdVCmucLXogG7RPl4jeNtAjUrb8_kRe0sCuG3nbw1WsKOwYEfxp-3HuMEB-0hgiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=I3NHp1jHRaUs0OqP4aFQbvQ4BajdPgCOlTOhXXPxgRa4N2tNsjzJLYxcaJXzs4tqWnuKbmqckozUzxlNSWYuM04QbyyvOs2y-1-zwJ7N0Y5rMOAxboiP0rAVAaEMWDYTqSokTI76DluaNIbefq-wuFU2Lsoq0_97SMZxxB7UvzGnHNS6GuHls2dCKSr7XkDreDvyqqsYIBLSagbnVJXh-9JzinP63DsGV-0Ds3G2G0o-_gnTZ0VdmyYCAL9PiGgJmnLLEep06f4Ji2_V522RVzYdVCmucLXogG7RPl4jeNtAjUrb8_kRe0sCuG3nbw1WsKOwYEfxp-3HuMEB-0hgiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO_HxD_GBUAfyE84bIxOMYl2j_rduFXRcv1k5w7fkV7o4A9GlxlaCEGpShae8i3XECEdbD9awAxDnfrc8kWFAju-wfgMl3ULflS4SmxmCoQS_l3mVThHpbk0L2Kxw2pNfugYO9GK8c1gqDy_iTHZBiJGCctxFOj4yZTjFlVlA10Q51-qEjc94s-MF8JYWLuFWn7xja5XFutL6EPDq-p35-V9zaKsySjQ31IUPNGR6Ln9KG4LIBkTw9wHtUVkXYtgdogUYj3PDWbhl5Ie-srZJoNhnJuhJAdu1kTqX1vJqmGrmGsab-NnKNHFvWoG3ehF8VedGeIrNYwUVfEnrMGkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD1qhKF16ssiQrEzLJPDMjbRelJVEEgcnidN6LqDordHYMuAWf7abi6bM7iI-xcd9mymS_h6idPnpwzcJjiI8f739fvH-hFyNk4dU4gnOtJ-uxWRzqbBQHE1efTbidUzQ6KNCr1QJYud0z43N0Ht7kGfB3cbj50szozGO3CiXi2U1FzCWpNgJ-f5Vnx-imr7ayV0qjNCSbZv4o-Kx1yRwn38g3BA6CfDTRy52ZGbXCC9rqWmHzmuICjCixN8Ec941v6BwdOK2fDDXcwcxw0alO5Kg1vsLckC762b-LQhb3317ITlnaOn-GNZCoQ0XBcNmfUdXQ_FLFt4DQT2hCbvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaghYcHuir-XlloynDE9gvFwLUrC_lrp6PWSGXcjapMJvHOdjV2fXaEBIeamjBoeYqXy_LigzjPp7GYIN14CaK34ThZN-ADKcU_pebWJy7vGmto1PnTcfHvjEdto9Ga3H6tHVCcrBkUUPCkkDrdsAaQt4gwsdwP5Ju473jmn3Dgr5l4abR16qdUXYkDUNdlDNdEzPu9stL-qkCV38vXeIE2eb3kTt_NNoPYNHmGwOxTspb0yDsBhiDoyYcCvxJmb8J8o0mgwz7zH7fDn-CNjd1iz5Q0EXYIaM_uLFhJ-niBRMiDjEoaj1XkkQXb6qNsrL_zg5_8Z7I8mRUMHtH4hag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NefyyB9F7p__K3BsZpt3sQ4FXCJ_K4PFtOoY0N7FeyCXrzauAK42GxftBjTt64yaApCvD3PXJOrKaggo-Hn_QQgkpcd8gj4SD63_rvM7rRLR2cMfGZibjjRlV5QS4VT25E3f6ZH5paM7K91xH_JS2fp3UOJAc_2B_ab4Ag_gqvyOoKUBL0V4mn7PDMbc3c9elPVdon_QBOdY5t9GSP3Bf2ssBgju8Pl3WoXdOcKUyKRWg_cmEeWDfzb7AzqW_DZdk3824LYj2g28UUhvQpl4sNdKN3oieziZ4q0JTY2A5JoXt2SZFifQDXFfVvbpF-JAQZvuE4NpHbGSKQ_U1ILthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff2he3lRJLVrMMD_t61_dR05Qk2dEBLD74frz2uscWFLoAFFlK-xWqIBWhuZI0c1LNesrYZU6f9BEXSigfOsZ4Q-WE-g24nek6l9aZ5ys3r8o4znb2o31wRanHGVcpsvuhBIfTZ0TGLgbT81PClfO-HQJfRaBs1Y706cC6oVBCUNQO4iyop5_rcDXrdZU5YTa11vNamRNPoJDcCCqVMSAdPVAj7yWIBdmrDHNaKgjXQ0rZOQjKHEr1uyd6M3yG33cL-DSimG1L9Fp1EuDoMnD1HlLPn5KA1iQnOPfqD_AzaLdVWyt7q6RWhmdJvpApjdNME-aYMZuNWFgM2y8TdGQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crlZcjW4OQd6-aREJC6KyZYNupmv3-ZU4sMMd9Qq51zQw4DddhcGEP23vKR6UxBQlDASsfV_9s2oLtekHAPAbDenQSWV4S7-DBD-mefD4KPuq-KhT4KKOujXDi2EeMWLIBNCZJAdg-8OWygAPsIwS5Z4EZlbsaq4GYf336L5n-EQN2QT9gy0BOytRw9w1-wqZJUvdtRKPp1nnP6hCd7yKcH18aNYJ-TM0Vvf-wp0MCAF8kKvsFJwcuv0qXs48ugCIpixKHRKh23Xg2GJWE_asFPFhjaZesCgkl0jRfRY4xpPxofKL044DFjoXOtMzAXqk84ZFVCmAlV5yznpgn7MTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wy6MQpjjTmf70O77rQIcnjnm0gM5QE-sKLh9CGgyZ9Yu5ICoorGwvbe2rLsIAY6wwMnfhwZ-1hnqrRKcxEOVoTnaRy8mb_xquI14202wCLS1jJuk9W3KkM7zyO0sKcUYia3ZNvmoFUhqcqidOTDj2uAWPJeJNQgANKfKZcDl6KDmT9A1zKg_iqFhPZI3PWC4V0LG60xWXgdq6Yr5LZjiEAoTO12Ln5AD8rnTPco6tyIxxngWr_o-mlpLHlYqSHwGHykEvE4DxukPjKHEJz-S4ezm6xwW2Jkw2ge__u4MuZmHSGBnpssTmVq0TIX7SR9aGG7Rpi-p_K8PJTC83RvMVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXhNJz_YLL-yCZQMN8xwwx8_upy3hsQMyErNGmGxsLRcsg-hxUICccYjlc3fs2OFZX9yUan7ltQkdQVzevltfaqCd8OwDx3w_MjUfJLYTqVYK_505oCOsCie-lvRMSxS7sMVKORMJIorvN9TRHDsh0OLQrwnt76m6BRip1eyNSKOSPrXl2TRYKDx_CGjPcNzyT0YBn08X3qnATRx8yUKgDhZXS0lFxpSn0eqqBF2-E-MxnbEYH7OO7NLh67EhZSNHpZeV3WcaHx0p9DF32bQZ2Vf__0r9C8akV5ODKE59SbC14d466FQAPXHrQmisgiHzGZt42cX_gIG4fAOATf_oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qbgx7IEk_RfJpK-ED5TvWTiU3h9WUIYCHFEcOoxAi0N3nc4VSP7AB3AVU8ylIi43eflH0cYTIGKZp_O3vIlxR15q1U_qt2L19uxcYm3q86orfrwFNjOGfC7Su8wB2m8Brtl3Falg9YZ3dcb8FfieIgJ17tEc5VjFcC1QUhFfeZsRtpSulOOARdG-fO9oyeqn9xIBHeHHPATBFqGgO0BRkWFbhrMMKtqqpk0Cie4dWiucIlszjhGM-oFuWeOZtyjSrBJWbfGRchCTi5sXABkaXDqr0Kb-DhlHEo0WoO6lTIVW87Dg6AsXhnstBSW0fgiZ5NrSxzgjBWO8nqg2THhQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IedZj_1-HbNbMZRsCjj1o-2ZfXLZ8wkSZuCROBhYx8KF4gRmj6V5qODd4YtjC1V-AubQXY4JriNibz_bNhNnYNuMU22A94vAX1W10OeBxgDN-0rOUPnO-zf00mYrBsIJ7xLx4tdZVMm2SgYW8Q0gl2QgkssjhBfKHFYAgrRpQIJUR3Ayz9bJILhxJ3F6h1dsf9KQMgN3Cw6zgrzQL93-S5xESWDr_iP6TQh4i1hJ3fY72vGuu4JLkLZy3EXxPFbxvx69aVMkuus-vcvAMeHNptlfBcAEv_ZNAZs6lBRc4Sh7z6G8hrCxIlDNMIDIyO07uW3IAceNVMHKBekUiY8xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLMo9h4r-96Fz33adnUVavPpKScmgIyAp3960WWTWPuNKki-yiiT5c-HxdBFXEu4Pu9C6PIRpoRbwUG72q-tpRW9QmVBvaHDUH4KccOZgj6_iDWm9zDchesoXZFSKgWVzE8II7-Lv1iM0gvNk9yQVfVVIl19dhaRIzeBDt24wbORXMNER8bKXsSC6COD-6wcozdKC5Mnq1NIBbZfAVmCd9IrZBkhYRrMfJhOnLg_6_9X6wGUW8u3pknrAMD-MncAhwB-zd85WETlEot8oVEDgYblbyKfc6EkV0ZYahg0DFtJjfFOYHhD-3NjBS0KbLlc9ho_q5tj2ZG5e2RjBQrUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGBJm5qmD1aXIUKNX5bABFTPE4O0H95Qz16veTlwul0yP9eizH7KDBVTnih8Y4aT2pKAmFczgE7zYvkGbbWznwCDi3M2NczRVlzdj0XINhRMpJwqP7oxpGWzB1vPzCYNeFRTJZEOvyL5PIS94Hvra70Q8D_6nSJNQ3_oNECOzG1LW6-Psk0gXCMArE23C30tT_ZnOdFM-njpDZo_S6vvGkFR335DXjO5hVqh7gmEiT3S0SDcHzf1Nzs6UIZIqkQgYbpGK9gqA2Odfu1vQCI-PJ0QbmfKpg7R7kFyOEy7Q6xpaIRMHdm4DCW-TgeartY7Q4kRZbqxBrNX9j9J5OlJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1COD_fFwJYkJQ6AeDLO69AglonoNpioxlUxMKA1J-5EjVyynoSPc4hqQwcmCFBxsKNmjeTMXFl-mINUQFSjGkYyAr422dE7CZ9tp9AxuS3WMGWTl5zWJxkHvwZKoaUKwMI-wrV9wJtjKJgZ55t-pR2pYB66UeZiZfBD_LZVyH1i3zTBl2hPwqeH9iod1W6_dgeRYqhcpJKRNRU8Bb-zkQRQLItJwYl2p0lqnJTOR8vr9ZV6grvzqASe-hGh6C0cipJ9lfBGrGTYBv6ybtE5SoLqjAAG2wQ5RmonaDLR6HuYxDfj40RHhad3UYmjWXSON6R3KSgfPUQTYuJtOXGDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7klR4leujbIYVe25HryjHULvw3zT8vWLS6YJ8ypz0A8PEBbKt_QG6kWGmnQG9u5rT6TcfmkfaLJG6afzYfX3yIaX6SCAI99nxdaNGMf5Nmu2GTa6b6MzyPTUTJ1_Q86oOrLAzOqhfZBHlqasWl3z7o86fxaPEnZ0zzN1V1YBocCYez1ugDcLrtgmDLYuKQ8eZgi38LId1D4YETDX14ed8YaOBg6hnojIbJNGzSkgWV8eRQ6bF1T35RunQ_n5T1Z4UA5bVUrctttLK8Qxali8xsLWDjUbCEYi4pqaLUrXLlBljCk-d-fO0MKw5Y15Ol7_njbGpI3Bo_cjurVI1ZJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrRLCIENYDKbchfuASoa9WYiFtwbgmh-eOYrWwudly5UQhLfjZYumIk4N2_vM-n4nd006jB784XvyuuABGQwrilKpQaRWZXjR1walXxpHj1YBmapyaIryC28XjCST6Cexp63-eKtkEQoV9MYzD9ZcSMq5YjHsOZt9REjln_zl55OltdGr3fM-VbXVWEWvas0aAN84v2hwz6KtmAIU9s-3PqN07X9XtEyTyyiqlISCMYZmV9GsNAfny2B6xdyRkpnqcBLgAk7WMmTVldwWgKUNys6-FoN7Vc5EM_ZLkmTHZ-bxX1jm3J7J8Y4zMnNrOUIK-DPSMi838ZBoOu1zjMkbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdDF_pz94Zr73XlBt1-Uc7rleYdV7bP_PsQOS2i9fGJFXHHhGGvp7ZXaelyRxPsnP93l3TIWNdL5GWstN6bmgWAzcNhzBsZh0lHTm9EiYBdJI6WsjdacAWOTb7LVDC6MC3WVpWGII7eyGGBz65ea6cBsZ0Tz8ptwMmxwVskRXGhJemLi2UGHi0--wc1899xz1bXwcsw7sNJVWSuANrpFR2EOqJfufxQKv_zzfU748gy_TMp-d1apeecjqZPJ1FV-JarIbFCRckW6qxiIpdyoADNXK63-c3Ud-yFuAt3yMIlMiEGaGD7efQuF_HSGTD__0qEeEuUiuIOKdfHgHvYO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhAqzTjVE2PaZESz4ccOzezQxpi4j-S2Msg4jsEpDGHCmDB9SdCSi0DODItXCbZ20-4D-ONiZb6OvThOTYJcIXbnKMTwV6YDDkvw2ONBrijKYh-RvoFN7bBnrNx1_cAERvRfbyBILy0VLQShd3LZMKuGiuctlAVc6Yz2BXmc7XXhhH1Q4E84POqG3n5ZaVB1Y6S7bQtgjhfgePAVWGru3CC0IOigIJu1TFfYbR_y2RN-wc_ze8eQMP2iHOv1WAhbDjYti4JX1MTZqv5KYYEscOdz1mod7tQHhbQpa6Is-u69LDJQk4xcU1J9lV6GA-zvFvmmbxdAsPSQ79q-QPnJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drbRZ6ev0Lgyn4F-XtMBHi0R4bFLVYHr3EchRRY5UklyKecuGxrZyfiXm_0SKe0Zc_1StSStuF_eF_OPXrtr_sLXKRiBLKFQVltwcF-WxU8ZUGHCRYzVaFPhzjw3N7TZhtFbWTBnY4RDX7hNaE7H1k9gdm1jxYvGTm_1PWhzZOreuWkHn-Va_EDiAIlhvYm0UfiuAhqDk4a7UyUMBfJToF_LzZYxt9DodVOLMImI9nvqb7tQu2gKe4lC-zJ-eKSC-KjNUGfG1grnYQlrFCS9d2ImgwpadA65LYu1PQ7lYvZ-oegUpRrUjuLvj79h_gESzJpzDqQb_BD0CTB5wSzWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIqkgJ0IWw8rhXLm5MuNFFgAswfd9iYI8lxMXXkBeNwEkINW9pOeeftzJowA1GxFCOTJbuhlHKn6aRkJINmG7ZvXQWsQvUJzpeanYbcFOiKF1BpNn4T2KqWaaz7uETB13zb036zJ9GcFp4NWtjFDjn282kWFkzmqVheNuTJQtC11tZHRGL8ra-i5DQZK0QLE9zdMchhcshjlIhb-W86vhTv7thXJCVm_cH_PVPNOvldpXJau_GEg4Bfb0kF-ZU5JkDQF3Y3ZYYrII6zWUgF-bOytRmZW83XGk9MNUbN-SUUMvovOUjX4d9XP2HF6EZ5gwwcUS1a_V68UozcJI5RW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZLAXazP1w0uQfd-XEGT08uSkhE5H4peWCG2-t-aKzcX-OL1jaBqBcOAVCnm-sxnwW3WFpkt3gfxPun710gf02lDMRz0U5anMQl-tCZrkfDt3vuXyCV6sMOcrscj4_dE8X-Ybd-mpdbZIng182ek_mamu5Ms-ircM0LnqrjxfWVZ22RH_ewTU7IpIlWT3HPjwi_nGuIePEkQ0bBl6HQ_kYptgF41eltCGnI0dRjo7EYVkn8J5fs5zgprUf5vX2HmrdZkva9b9uJqAQNDepf5X76ywIpQpXSBBrSEkZXTQYs74fD4MOZ0N0RwdgobfP04abJtq5oYIWa79Se31oUuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oe8eg6Tz1IUvdijOZRq4r8TM_y8hSLZ7MR0dhx43H2djtzcv_kAjUmTUZjYVPLz03JqVl0tizubwaYp46uY600CdQgXvRxvGXCv_orCpigju115sQQyLL9qCV0lO3ICayRRluOf9vuhzNj7Ci-OSztUYSPLTGnEDPRwBzEGxLhuPlx5pxesyV4bBnwTPPURGQjnT2pvNN-gfP9nMu5hgC1NVGoJIO3Sp_l152qTbBcLxVxI2xp-t0Zd-KfGwxg53n8PTYJxgJs_guf1nn5rBGtEaWRogYTg2Jr3aRBeLbvZ5VKGY57rl6SYQj5ogSsGV5XYpyiYvx1T1HD-0pJ5UIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_svR8F3LhUQsv3N5W-V-v_uIIY1FZ0MsQVN88BA_GQVQiOK2_8jyLT94oe7IB20chux1-l8GH_d5DVHgKR9LXgaph1Eb95Rc6ZHyhtONlSwocCtBF9EgiK7ou7u2e9T8Mbjpbw-7fJjR-L_Ku6IWb66J7AvAWjQY3Ob1ZQDA6oBM9YTS2iVhhC3Tcy8HwmzroMRWbyiCrO-f82zJm6h1_Af9ma2yNrYWUwlNDIJvXqL7_lsFfVSRnou2EP4rcsakDeWIf6bORi1PFq_vdGEgxRNxHHL0g_1AbwOK5RejxqEgEh95NnjiUmE8CF3DwbQ1_ul146iVF1h6cApNaKfFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6UqqXbhpecHuVjZxFlwzM6L3iGKGuCcRkMlU_FDv-xmPpiaOFhEMoljg6oEyzDdyoYbukojBSTIs9EU3cVBjIkpNmq65oRwRjapMFb91tf1HHdSHt9lMmdySL-H04cfV-i1gF8OCjR_AAZd1Qk8njJ3U_z4FqBsKWzkaPxFpLrgPnzQeOnKg8Wd2kHgVVtjUhl0hRztOAm1x8X_RvFmRW2oE4e5qymlq2s2gEBpz3BwK6YSe6PHVHGm10RY9enLJSYD0pm5OnJtsErGnMQdWcMl1WNT9vIfNE93lMWCRvR28GgmyhHIfK-OKyFC2x3CkOYBxObBU2-jnZTESP4Q9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSlN7T3qtB-VtpVrfz1gUlloF_99trZQxb7Pbi3iMDVDJXFvUn13QLrSqMTQz3Wy211N1GzY41YJ3wR00hv2EO4lqF6WOPqx9J_YH4O6F_BjBIuwRju2ZZz-p866tKNOeKYkNDxPg8w01lJiULbngk4eNGXYGftDhBaIfqi4p7J1WrmQixFDyGieylBD7jqJ0EiiqjpYOn1fh09DfwFcZQgkZ1XIKc9NKklQ7fiXPekvnaez98hhC4gmvnOZmbAd1ssoyLejI2fseEKPifSB-Lav7-IZiWpTuIucQIEoKJYQqJGJjln3qKRGEkSW1vtChaAG42IqJwjKRPX4519Eug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UufPF2H_bhoq4pkTsv71bs0v2ytzNsorgq1UAnpsa9VLnpPswXlPBJG2m4qJOyqkRt43psZ-i0rbOKX9TYxbI-X9OrZ63kN695DRmL-I9bn5LYUn9at1yc4fhapBiy6PZggGz9XJ-IU_qTMm3vTzbkaK6d6HFjnIDK5mUj2rHwFLkAV89LytlAH02btxusdRNiAXP2sUJlaWhvhSm98fmVbx4956L8r8FcHb_h50hIiI-6UlA0Nx35UBcmJ2Xt0orLmPqjqRr1xjXKNz8Hr4ngvJVrC7_f7G1TLIVntVxel8w2KZftu8APN8TLYG4RRjKdlwtFEqV6SZN2p5EAIOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbN64qXc7hOwdOwZZVByiMHJ9ja51A0ZZOEw8fw7iY8MwWNjDrsLQ7Is2WS-yJGpu74i4JMBMF--Hzuz-M44O65nq_rrj8if9UekXMyOMVM4OGGvxkUfExE73rJMSiN4yQcBxQtgn2nSI16sL1xT_-UnTG8RSHzWKYVnS_jyOqudt5vb6cvnKhgAc-0hqKsQhHeDgJlgSqMwoqmP3Nw5_93kjFXsSSa7JQ0Ty7sFjBTNo5mNJ8oAh9joEoIAmYiR98mKRKdHf4Vtza4IE2XqqDKPXxl5pHWOV2hiBhTvvEB_0yP6DVYnoTVJ7Sn2Nub-hnEuXnY589JX0CR9RfncjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGYwzO2ObM-Aoxaam0hZYDpzpIuFTL-bCBtJEpnbGbqSTf58w24RbPVyzN1U_Hq5QDKGPu579gyRY-0067_hcWkXcx7uzcBA2m1A4Bz7MI4y3JvpPqWg7axuF-_bkrUhvnSAV4ycwES0b3jhr876zE0pwqf9sYY3WEDg-EEQMs0cnJ8Dix8yLEvUAOV69MnGn-vb_djZ9vnxEIVId0FL-aHUa2zCZyRb8f4eEH_oJHndwvI_CWwudoU6yQ04vRfhlkT6T7C3UnY-zX-k00FQstSyaC81jXf1kJYta0tD4dPoZyIDnU0NAW3fZFrnQfmaUyeMyIAZ3l8E2rIks841Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=dnjb7pzsRZTCHmB3ggYHC4Dus19C8RSmpYNgoayklK1hmn1SKIFNoxZ3qlVp-wID93q4ZtirITK9DHxJmJd_aR5dYrGdOhdhSXH2HrOpWCEQcdcouJn0HnJ75cYs5rWl0ikd6PzwavZAcCEqK-Gzk81g8UNjfiwRZRFVWSZEwGjpFqVDq9NBvqamIL9B3Adc92NKasgGqowU84qGM7DfIdQQwzdPSE64nf3PRNUgKy-SmTBMM_0NaFKCHPomoGX0oR97CxcqnguVV0ZiWuhyWoPOGe9IlDN_3Ia8ODcLYGSfU_CsPtoLpmjXm7Waj1qgqPQxUTdkYdBi1lFSg3QHYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=dnjb7pzsRZTCHmB3ggYHC4Dus19C8RSmpYNgoayklK1hmn1SKIFNoxZ3qlVp-wID93q4ZtirITK9DHxJmJd_aR5dYrGdOhdhSXH2HrOpWCEQcdcouJn0HnJ75cYs5rWl0ikd6PzwavZAcCEqK-Gzk81g8UNjfiwRZRFVWSZEwGjpFqVDq9NBvqamIL9B3Adc92NKasgGqowU84qGM7DfIdQQwzdPSE64nf3PRNUgKy-SmTBMM_0NaFKCHPomoGX0oR97CxcqnguVV0ZiWuhyWoPOGe9IlDN_3Ia8ODcLYGSfU_CsPtoLpmjXm7Waj1qgqPQxUTdkYdBi1lFSg3QHYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU8ueSTHksMvkucDD_EV6uGwLHVPXqGl9EobMlNf3joO_4hjNnibID-6_FidKB5MxU1eZQ_R3yaWoWMMZj_jsQyBixqUw29GaTxAKbzBZIuHdcUGrIIT-dfCwjcIQZnHfOLrN7lpc2EPRGbUDXSPBH98ZqoWkLNQQyY7xbAg1LvYzCA2_uE5sLFFncj25lD9h4LtBKHhQqIw3O2WGGT6T9S_ar-i3Lb1Kpq4dsmFSpLvizmSozb90qZvLvyuJZFgQbJx3r9R1joqcQNe86hzMa_0E4JdmakUapUbU0LbFB8tyBGS3kZ-YWWpg2RqAQOwzzhUslWFknb_X6GzDhyAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbQQstUaLDc01pSJGu20C2uMFEBGouck8fEXlN-9eCbn7Ks2oco3hU9uWEwaNr_4oFXVV_otLri7wMOrRGMGoJ4slv55BEf4PMYUdVn3VrgPvvemJV6_exdNAou3ewGj-se0ZDWGcFhhn0R6ekl63hiSX3RJ0jw6zvWfybkZ2yXMNzkv6e7l3SyKDld8vLoEas6jpT1djpfNsbG-eDFremNH4aEgXLB3LIgQMbOzlN8T0wrJEX3o8pAq4ARY3q0hGkUNVRUi73WUSRkrdZYguXB3_7oqrbdnrBtM7weYsm_qXzmNTDaP8hZ9lBdwICqzNmfgcNsXlU8ahatWPBjI7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSN3ONV15aQDwhkypKGDYTJaF7ZGScwi7Ec_ztfLp6RFPd5aRkzwYXdmDqPzdhOlsmn9fDT0MLE6VSHlzSZlSTnGRF45sR6HCXMvkM5bOZYRpyCgKhXj3emmYml2FHO4jIJoWRI-5rNa6Yd-TuodGKLrjjX0Wvt6mudvozykozNdB7KaGnok-EZamKzVawTZglhC0KJ9OnFfVoJXvhUnQ67d_JtHoS70wyotKL2pTM9sLp5bUlDTWcHmdlVQGeO6ybInbF_fO0rL39aABN8N57bM9-yS0dKWv7Sdv3mEIzAYNZZUWHgBtRMrL9ItZzp-ZJwTPTusIC_Nu1lhzX4QJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOs4G4aHU05A4zhuA_0UFwa_R57iwlsrwYFcmfWU6KIimc92E8TULivYLjaPDZa9kU0zwHjwIzFnI2He7CVd-98AV8EoyFBQzoD-AERy7POnygXN2bpRFhxpgZbZnbnrW7N8M8y5eTbQHDuUMtnLMcncg9ufY6feL7YrPmzk701SAOsmTaZqE1bnCBpWB6Af034Yk6vcTxSkPxiR6mNhPj7wBlnXJqFf6nC847utHWrpjDQSYH8Rkpg1Za70-Eh2Jp35haZ4HFsANMqI5j1gle4wXlXbsvOLGSSTbOZMMs1rb5Sl7lEElGjrislf4U-b0sYJXaC0toc67Ert-jC5Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGTFAGc-TFw2D2L3piywH-oWarCCjgQQin6A3iwLleY2QD_UuuwPO9DrgoKke81S68lv6KHyaSyHMgvLdEd8vcBVIX5HrJuq5U74C0EVAXGC3nyfsjvpEmDEF1Gf-w7-VSCmi3xz3egLEtA_8jeOHw0c3WiQjLV82j_qLfsIDfRwzPHsnsQun3vOvonU25-bPxHD8xX0PaUtp-9Wyf6d9Myc-jWYeupOQ-jdTk0NpSQmw3EM0i-NlOSCxR7O-eBFGkoj_jgGX4HuTAjhQhb1nYu9rs7XPy6fha0ZSqSw-ZRJlrDVo0LHAwvmO1aTZwJZx7t1BA2a9nu_y7JA7TfG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpxftMlpEcC-Epr8QthapFuj98q6HBuMu9KLEnW0jU4ni3rYQgxdunbV3v1Sodl_mXMtmVpoKv-m-mjhXC0ySfktz_77uENoKL5lJowLUPtOKgTXA42LPlSuElrKmyRfBs9X_7Vf4X0B6jqnMnLyPNNpncrfupbJS1c_RBzbOE-pxKZ1YoruXxnDYGi5rToUKUA07tyyD6sYY72KApfA3S-h7PS05BJFj_gBwYfd_KHbfhOLkNt9DlPBjjoBnSeW6ZZtb9tkQ9gFu1pwtj2Kgcxb5kjYmAyWJ-68V_ZZL2ut2OHJoIzxgJD5kRJygEIEZrw4EtfuWiaEE_8sPId9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXWnyZdmMteqBFpne1y0aESAitGjEvjZqGpTBtuJqBlpSEz5WLrLu__A-1anlwSjCfIjR3wvA61ZOcFSKBZsWOxK_ayV4r30nSAwo5VJn3iXOGuFnyQQZmtOUkQkRFl_YNXdJW_7mFB6_vpwvXtnnpB-T3USHBNvGYSw0mOhidJ6cruCnlvup9xeCwxaT0NgWKBNcABxBuBcepq1vAlJBxzUFVzwCsqcxOvnD46BbtlANt86m6iptAcTKPO18aNpGDvpPEvuYO2VtDQZajzUaEaioFf_xsCuJAqE5lXL77JZBsZq2I8_53QWTX2Tx-1uiVVUxPOc5WTy9xW625E_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svIabWA50bz5i6i8FJNvc0OjtTFXvBDloErahrAGfcht-eSZORCNZ5xleqM0FRwDOPoyQiLgi2_-fbAuqxtNWYk1sAaj0De2Cl-WCKdjiQFw0fSkQhFkh6GvNWaoEn99DwS1rHjg7ZpK_aA3rDvLQXxluluL03yeK_UXYiVB1khTiWcvMz1VDIsZB8nUOdpKnwfDrZRqUueRge99znFBb6FhvSpy5QOPEB1TY6pJnBDbPHAMDy5C6D5TeYSZLIFmJGtXqVMo_YW1NkATq6gsHH6M1n8Du363pLTW4CZC2nuplRvAWy-cKkDxi5Wg08jRjrNroiTXTI19AAS6Nwdtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=knVLgWI3p5wqgRYaIN4nskMr8hir22hI_yMensUj420CQuaSYgC8hSGlsYweYhV2NeL9Ym8kW_EYcTtiOt5v8zRjEWN1plYM9P0l1RxvMv77FL9NH4ERJGVWpiJ6Tx7_ql4Dw8LjsPic4U1mkXtj0w7AUslIONP3i9fe7AznPc6nMPw7Wz6cxdaUlOMYB1tHLUsW8WnT4P1N-DDQ6IES4tF9jByNdxZ3FxqduWS-WTplrOPkdVTkuFILfQsJBQxS6kLgr1ESGztzxIOsrnCvWcvgtUWml2Qw7advNw5GANNmU7WhkSImkE--TlDc6hL6okcGipDtSkmWySfmRqkA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=knVLgWI3p5wqgRYaIN4nskMr8hir22hI_yMensUj420CQuaSYgC8hSGlsYweYhV2NeL9Ym8kW_EYcTtiOt5v8zRjEWN1plYM9P0l1RxvMv77FL9NH4ERJGVWpiJ6Tx7_ql4Dw8LjsPic4U1mkXtj0w7AUslIONP3i9fe7AznPc6nMPw7Wz6cxdaUlOMYB1tHLUsW8WnT4P1N-DDQ6IES4tF9jByNdxZ3FxqduWS-WTplrOPkdVTkuFILfQsJBQxS6kLgr1ESGztzxIOsrnCvWcvgtUWml2Qw7advNw5GANNmU7WhkSImkE--TlDc6hL6okcGipDtSkmWySfmRqkA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Urf4ya51PAAqihPEtWUPu-Dxh0qOvXN7nBzylu1T4BZjdbWGrFMSQkuZ69ST27ts9vVxpG8SHEpZ3fz0PYKj3kBQhAcm27K3QBH1KeOFvnkWezcEP8IN08t9-iLNqXDYvZxN2ugn7G_1CIVKvQOHJ9P9zIvPNvk6p86arBH4i8qSuLp6-ooTFSGl3fPXvVCetwnDjbC_XZu1rJO6ynfIAmdjp9IbpYoJ9ypfdo-zCIipvTKOdASJFS5lgqkLMhIQWBFSxHlUUPTVgbLR30HANXfLStkev2d38FNGM3ZOK7phFkklMphL7Yil0ooLyanvIW6wJdGAx1tDHW8EYm76SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC9uAnW7pyCjpfRIfh1cEq5S1cRUuBvqikZN-o-L-fsUDNW0jEllzxbKieXl_YxQeYiKpKkeRTI0YyElre3qmOuda2krMLXs_bcSubHiGX05isiLhi1fCLQBjsziKGVBxVO7AJe0uEWfcadYemh5Va7HLyx0mAfnxk8cG7x0cQjjw4JEfnMRTshkNF1OufbR1wh4k3GhG45v49bF3FGA4ptiD1EEC64h-16jsh5A94BtfGf_am3IbI2eKfAEtvWTk7IjmHNg7VaxUoj8cH8NdzgkAQ8aR6gfHYvjQ6ERWXL9rM5EpQjIUQLB44yK6VRJSLLmtZJ3GLNKzvUa3gNIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=sFGjiYZ-a-ywtaZW-xoLTG_8iXuNNxiwKC4XIpGYxT4luHsrfHCUbySZGLs6_RP3rdLLwJMze0vu2geTgFM4WahrdPhMXXOQbH35igj-kDIVxcNUjMCCzOGi3I8xyVHpBxI6QIqFr3FQ0CM9sWkPlOpv5Ik-VLY9Y0bNdJLQaMiyWx3MBHWklJuB344ba5X-sa7quWklKUaF8byFC5fCmczhj7LEaXAH8rXnIlmDqxp59e_SojeYi7u5BOZQeCCf1dNSdiBMgi2IIhDNl21Pcbxz-CJ0Ti3vsMsBgkUft_vb-u8YTDGdUZ9KQcknpoApkyJ74n3ddLBn79IeCu397w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=sFGjiYZ-a-ywtaZW-xoLTG_8iXuNNxiwKC4XIpGYxT4luHsrfHCUbySZGLs6_RP3rdLLwJMze0vu2geTgFM4WahrdPhMXXOQbH35igj-kDIVxcNUjMCCzOGi3I8xyVHpBxI6QIqFr3FQ0CM9sWkPlOpv5Ik-VLY9Y0bNdJLQaMiyWx3MBHWklJuB344ba5X-sa7quWklKUaF8byFC5fCmczhj7LEaXAH8rXnIlmDqxp59e_SojeYi7u5BOZQeCCf1dNSdiBMgi2IIhDNl21Pcbxz-CJ0Ti3vsMsBgkUft_vb-u8YTDGdUZ9KQcknpoApkyJ74n3ddLBn79IeCu397w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIPnGyInK-d3uQ5GktZu6KsmiOOzxjS5mQq9wUXLG5lAURBcJRU438l9LPQFKlg4DNtKonhQGnWve2TpichiW-XGDgthfL9reCkSz_4zMUn9Inl7bOq9f32jYxHgXhGJd-OtVIDfM5kGUSRRKQSIC5gbJ9hqqxlyR6CNYy1Vhqx1s8VJrjtzbrVwU_Z-qNezwTQ3euRqxBJq5VhlH45-tE242tRKllgt9-Q2Z3WCVcw21QaoozazJI0kDhiCBEMvWy_ffWn0UX7UjOW5w5GgX29RPVKb8E400v6GSEhMNbTF14ZYWq9UPXZqbWzWEfuErG-vpxTGEQ6IWl0YHxZxKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mBg8Lb1Tx1OfU-iY8mYomowtfQHDjRMRu2bcoz1Oglm1VGyjIp8JU_7i1avXAao975JTK31xYjf7GNAx8x357XLMivvPEi9FfyK2xd7O85xZeOQVz1MsztQ0PoFfwzqAas4vZR51UT_Atv_AVZDv7GYMwgiBQI4PpQ14XdsrYN3o71U30UZO2Q9vQO7q9bFo0vRlL1IPTjJ-JDOwhmkdy_MRQhLTMKk8FyNbb9_DBEHDPdME-nTT3fwvCyxKtj90IXNvdsYlzE8mzXswi2_q2mT5hC9MpKQ90Ktq7jthvKlmZkCV38RVtbCEnd1JthGT3dJb6P2ec7efkdW7tENvRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thX6C9y8mjLplCmpQrGGlY0dGrxM1noaUoDzJ3T3H0ilDrXqVcieTlXUWpLoALhGsPjLFd26F-qDCCWfBxbMr6gHYVa0BZXO1r7ruOjVQUkp41F90RkHJsvwlq-yazwLW8VLV3p5sTCvjde2WigKqeW3i4jsNKG9kqZyTLjZ0euzgjbx41-sXJ8ROCYTiir7zN-lOZ--HPgZmfN3dKeGhchAf__LLC3c-w8Y48eZ8-JY0p8T7U_uAfMcszSCAP7VIIbUYVhYobLfeSUk8Pxb9pwM76QRpBxGNuuxFzLpABVVMKhdQJVTN8_aoNJqYRc3c71saXNKETC0uNLP-xQoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARM4JtBvJaz6WplrPoDeyfF0i43ZiuuiOoks71wePVOd0aosGgMSbv8U78MFXN6e-L13r0k37vWK1EDofBZQvDItNODwO--TSSJEBr8SWAm2rQ2Onp-jk3sCinWn_75VsjrRlCa6zxb2N7Hg0jcxfJe861AYKkp8T0yBtCuQZQav0ngEt9ETZ1WufvZ6DkcPpb-A_kfGkHNHd1Zv9Szx3F46vGdTryE9bNPKcSgz-k-gCWdgZQniHi39vcmFtgJDKF21GdfkOCWsf7-nf2m52PfXly1suNOj8kVYtPHe2sPoG_UlrpQVaslykptjg6UK9sn1RKaz6nl8nzIYHL4LaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz-kwOmeycEFM8a5vw_mdN1dld3P0ZsTavCRmC0yTDIjCOBwPD1w-euFxfT3uPwTPoQEH-_ZRA5P26zsockVcMoidJnDlUGXy3EYrZj54So4_TgRyb_MZQTx_0bO7swYZXFcgb8RvvVgdHo67yoHJcGv0BktHHWF91UIhwuw6NWDXzHmR0ssWWDyxGHUzu81J4ADDa92yYQ97DGjiBePRddTxjPqCzsgo-mrrEKQJjz5pTUKyp5HgrvsM_wobebUp3TLzIHjqR8bvCFPA1136eJQt83MSCXnyoZ7OHywQ538cmkkMU8yVirpCXGV3mk75fqb8U_Ikvb1h5u8um68qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu54vk3h9dzIg3JephlmEe-1fll3dQAKtAmCNQeaJcjYDtZ70nntUy_H63vuHes1w8weirg-oy-Va_WtABRK-gtakfZosDiQPBzEMpaOF8P1EH8NTEdZcYcd7EdbZwtZ29jjJpB90dMQvtDTvoKpmXhk7TBzMLHLDrRV-iFSDmKXbZv1bVttnne6NDoTZFyTPkLi6wHygIgBr8A33QANuCq1n_u-YIfeHVKmHwHlQhh30Ac2U5tTmrKyJb5do5zode5I02ESde7Fkxpprl82LkHljJXEWjPn0QGsUS5Z-woh1l4vgiZh_t9OIEF_0dSY1vsuah_hHZJ_fFncaxWtQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjnF7O2p4ekjCW6LUX5NOpUM4_pqSe1boImDC1vmBOoW48obgBQVwSsMxYcfYTv8rPP7CrIpMbrwuuWyYD1B-dNUmVMer_hceXA9uUnoQinFXzMa5CI5UYKOL8PjDLZqCUvIndjqdl8__BARxzmIeiNZlVeC6e6euyJKmHoczcYBo82NhcPlQCKaz0rk7rUZ6j4FVvt8SZGfIcNDjDGGQ-yJLR6qkYZTMyD-y3iWGugwF4C8E7qiq1ihbOzJpbxeZoTZvYgfYQ1FVOxeqVWK1HLSeImI25DUwuWFdpR-h-wSu8lHz_06C2pX1ZMlwfnkY9ulfliIRFsmHF7lMB66EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwdY6zW9-IxJpTAVGaiCjlkDLkAs73IEIwEwLttBay4kEqD_aOaKq7jCExy_ez1Tshtiw-GuOjOCR9pOMLD6rABROyYCb6VrMtJsWAbSnaWKGcR5Ifaa4UxMZUZWDaW3OkU2b5QUj_Tybjc_04Ex1txIexuIVAPSdLWxVOAa-FAswheyw6EuGqehz0oNJc2JOQgnCq5TnBvkT3FGyrRtZAED8CODcS68Ty3cImosb1yKpBt6lX24S5Wx4mM85sF-8duM84-RDcv3LW8uvuAFv7WJX1NQpWkVYzk2y9qrX19S62aTvdzXOKnn3HYWzp0WwmYC2O5__hKb4UI7xjzCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hemco1HtMyVUdC7BklKvfaWjtr5eQmdyMSRsDk_4OVjpJStLs-DbjigpAwlLqGbD0Z-Uyjo5wzYeAK-t8hjXzEaSb7sT4-pyUZrk8iIVQCSkbt2Utz0Ph02TcTCtB4WYtivNvRTuCp600u8rHuaTnATWUm5KxmiUoG4IJgz5KdHlQiN312Ft_azX0b0j2368mHkDuMVIiZXXLp_elwsX4GzQtiHq1aIDRE5f6nsQNfRBJRrGJcGoR6xtLs-qX2AVcA90mII__JaMmQ0XYiL7YXsT9NsOx3wozhI67pr0YH9o9MCWhLN42Mhpq0JqDVFJk7vGv268gsvzSzCBpNcvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPz1Vwpayoad-WZzWrJ6Zu_2_PSmfK-kV1uHSbRHykfIR8G2RoPE7OIRMutjnzDVqjWv90j_Knud9lBJZdLAagbFhxvbAF_2A54CHPttGcgl8847hjsJVt2CxT1DGHua5uwxEON01SFWV-5QEA9TSJOlWgas8uRC_uKg3BLB5nLbicvrj0CgM25k9j-yV9pbH_4M_xNtgJNAKWUo1r35fNli81yydaKfLErw7txZyrAXQP9gFSO5VlbEuWdbqzcP3LMKgJmgQO3tR1EKfF2K-IQ1YpqWNvkPIJ9NYMJDZYFZmiw6NfLPF_XUA25JF_HcOsqtyV7Y_R1qjnI2U8V0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/add-oh-Peu74DKBzji60APTNCoKd3pOraJVOxOAXD6_wXfV4f7suyB25i4w2xVZNduuz4vMDSr_IpEjpGZLfj-XhzCt-KtLlhcHrFzl4xsp9Uc1yCTJMeoNfgCD7z5UZwNnD3dvkZ4rv1YFN2KGaL3WIJ8dWR-Tt62UORRWzDwzRyGarp6wWY9y66O3LE-pwMgY9pp3zWGBhruMwBN93eoF8cR26gWr01X5T_VMtzChQjk08Cmw4czzgLOvGp-i5A7UmzQ5W275Xur6DjZMzc82eq-hRK_46xX2o-42kinf9NpfUEMeHdsnbG6Y7LVym0Vh8Izh2ecFYaKDpdE-mUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A76cNNbAxe4X1hmP0CBBHJxvK3_FT_J89cc8iICJWOPhBzJYWeT1Pry16mv9Sd9NDa2aMeBsYJqeaKp_sno5UYd-F-D0Xum5VKE3HmYcE-dnSYTqfhxXtsgeqDqYHnqwxOJVkCiTsU1tGeTWykP1pDj1tORhVx0IYNAVO5Po4ob6aOfC6aWyP3wcDVDOBPE7sR-6MJDreyFlrKYUuJgwvzhYvAV-4kuhMyfNqxzgJU_ZQeeMqbBjMG34ZU6sXfp3sx45opiaF8jon53wwF5GPgJsQYzqFab13mF3-Zk5jGGIaqRVILRfxCzfKCgwhcFByvxknZhXiqQn6JQpMhsSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwGvcGrQ5Uju4rDqxj8Q1GnoxzMhJGW-s8kVfskr0bOXeWaRI7kFvvdjmcpfT7WItgmjE33gi7KTXPKAcImYPUe-nO_4gsJddElR95S0Aw3D1Qa5XMfcNODHqgEjvGRAB3Afj_i-tgRaqJLGsY09tku_I5DqYvYAA7ctmjaFjhHieOLK_rhloQWGJon6Frm_t_nVE86srfdqXwUjk0AzADyRWRNSFgNf8pHV7p2duWGx074WhUKMdS7O1JrdksigJCEGZkrxBLdwWwY_sPjAmDmXQWBHzX1a0levoa6AFtnH0Y5Oxt5goM11U2sgH54iybNCD-FP1jjysdep48SrIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDRpV26X7bdg3QDvT_QK9C6UuGiKI0I1QheTkVBD0RwI7UxdewuW4Hs9-VqZ8dbFA8jh0fipkj5BSynA2XdH3SRmPRBiYwv9adCtLAm152eodqPBe1viqfU_w8BzjF_00GrqzXQefgzVeIIysMwVzAQKXGNivPFw-1KPwz-Mwd4GvfV0pwdtn8695xhLkZJ5THycpP3VN4AH4G44i-TPrmu_mZrhr3dU9HD_ubuvDG4pNXxiVEB1nj1MSke_6h0nNWUI0hGI58tHL19pyFRqdFiRHwKpbpKLK0eY-jqnlu5qwymjqdD5cUHtYQ-dMy4-lnOsnUBb0weEEP2yMPANMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=je4HP7I-3n8GVOWrEnXltw3TbtTwVBAhEiSAUMf0Kqz1v1zM5KF2C4Pxe_C2T-uz_sPchK5r9zxmRJgh_qthoUiAf0482kiPjNkqLJHtL9IprVAKV27983DRh8Ybg73aFr5Znz_DlM_LZZMz8CqMgh3D_IAq6KQm3Z5fbWq13yxOgXcyFQ-Ps2bDi2YoLESELmosG84sjXnUu392yHRlv8s6J3PQ7vV7vTKMGLWMB2qlkb-YpGEUdpgj6VBsrkC4JEQBUX_TQ4GOupkPaRZlEGY370M72COVuqdDmTOTU4DHY0sb3lNSn4q-vxxraXGqOVTToWemLHYImOWjlQBy1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=je4HP7I-3n8GVOWrEnXltw3TbtTwVBAhEiSAUMf0Kqz1v1zM5KF2C4Pxe_C2T-uz_sPchK5r9zxmRJgh_qthoUiAf0482kiPjNkqLJHtL9IprVAKV27983DRh8Ybg73aFr5Znz_DlM_LZZMz8CqMgh3D_IAq6KQm3Z5fbWq13yxOgXcyFQ-Ps2bDi2YoLESELmosG84sjXnUu392yHRlv8s6J3PQ7vV7vTKMGLWMB2qlkb-YpGEUdpgj6VBsrkC4JEQBUX_TQ4GOupkPaRZlEGY370M72COVuqdDmTOTU4DHY0sb3lNSn4q-vxxraXGqOVTToWemLHYImOWjlQBy1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TG6ld6Y0i6b5zRjZp5CZreiAKb1j14wYauf77LCSFY3CbPWSvrjFDiBeX5mXsG3mnJ3K-ynZDgdC3okeMUHh2uldekJck399v0yQH8ZYvgGgt8SwbX1QXCUtSrQo9k1i4r0Cqna3icjv4hd2v1Xndx5MqSo-2Ra3UuFATc7YMLWiYO_kxTX3glMxR-NIzvqYqU1LThftclvvrwVvI9RyZBXMQIUnzZkKl8abFNd63lLB2Hhs3RBpmdkUV8Hini8fTPJB7pUqeYYs4lJBAxyHM22VOest3tS-sSy8gWd1RYP01sH64ATdJF8XcGTAUV6Pk5DOXP5yLF6_NVpaBIeI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6KcdyZ5Y89wJdwX5H7tcm8NZfHoT08TTNIuG4NTxuaTmZuEZ5optqLHlenlILUxigGz0YrWVNiEHP3bqZkZ5VsFdlDBmByULSAE-xSv4bw-PVIay1ugCuGewWkYL5T-Y0DT3Mez_5Wx627pIc15cZ7SLkWPYJSfqcxcstK82Od0TiEa_mIwChxH8FI1whsA6UawaEuF6mKyuonPsVPEnsOWE2NQRVDNcOTZB5X3T0Tq3jyz6ikXPGLiL4gGMzBFWScJpdAazDKLbHE5GZJDXCJKOrEp1zfYPz_Y3B_3SPheeQ365GmttU3HN1o2F0gI1ANVmANSV-YXXgK35jPGDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOByLpq_GI-n8gIptLeFaZF1sxWerMGn-syaGMNxE-6aGmqFfi3kSYSA0rYT3JxW5yU0788PLOqAdZ8iKvSzF3Lo7bkBKbuvDdjSbIsoz74gbUobC0wEh0wWMfogTfOm3Q6aE8Y2GSJT2rwKodKgrXRGHcT_nQb0-12TFViuhujDm7HTt99sYcnY51u4Pev7ssAXUP3iP1kY2kuIibcOjmP52isyHaYoQ4LR_tJz1xQIG6vx7HtD9uIwEStirqn-QnN21tl9lP6vyWFoLyWD3D0Ec5MBBUQsT49wCb1zGItZqfFNPnekYbYT1RFIyEggxWSXwXKZi02uuurM9QzaYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuKSFrsRzaOTKOu1K7FgxF7dTeHZOf0n8rHg9yvjueP0AC2IBD6NRoBH9WTBEogzXHLXGscUIltdr2jBTHROiiKxmy4pScb67QpFssF5Y6LSPlvk4Ncr4GiWlyFQfadaAqujPo0F0PstF4_K5_SJJQa4Yr6mbFSLYwx7yUzjee_oSzEP3-6rkM5ES5euC3buAs5MLIZiBH5iHwFPXEH5quH6WIiJvTeH-vajLFKn6YUmBRnCftAaJ03bWXixgA9Ycqn1Lm0nnpfGt34f_ae7P995rOvpXvA_3vkjrINX1hVNK9-d4ghBfIeQ11hY1ItNaVzEcMq3iiUA_BAIkpeJbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoPP9Fw1HQAZog-BUzHczOdRfqO0nCQd_7EZ67GsUk5_lzIGgx26DQjBh4lSaeQc6kJsWjlbK65ekITd0I1zTXBxe2CcYDz1GJSjfjCbgq0ZwQkHGaHAtsoFJP_P25hkuTFLbcbG-cF74v33nFcPj7tOe2rojt0ATSmLre_PDU-T1EAyJJCMvEuuJQoRuyxbLHhqin_p6B-Xv-hs6W_tOC4a4PItiqjRus8_bnB616oM04KxnZVj8rRj7LD-ibjW0VUf2Hkb_aKS-VkJjuEd5KmoNqn0HhMGHoondobEZ4YMX0DglfU3hOBehg-XOcNk61p6X_PbHNC6HyPlKg8zxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdJPVMEnSAU1W8TCzqjHcBiohMQSrX2VucGi2rgsYjweKQQAp77-EUHBtWfv6yBU4YUht6f850bSKr6QNpW07kCKBlGFaUVMOZpwNX1yl-giirieejhSSDSZiyCmBgi5ZLKgf_R5hPGYXP3tvtJfrhG0LWjbGhDCZ53IpA0ynqNVrkzv6H7xuQk1db3QyQ0cIjcI1IY55taaCSFJbVPBdnn4RZrlUzzU8AvBgKif-FgzpCZLNz2PuO2uBcFPgy1IW5rHmyq2JXS5BMwx-TUTHJZrMIFsCxGKnsCrOyn20FVvSqsfSDR1wZ_-JukAACvWifgwkkQwhtN2KuFCwh_zVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLrjnijs_oWRIyiFa6_XWxI1d8SSoFZvQwG_ts6PFn1OzAEQVyQgLa92PqbqCnU3wk4aPG-li0vIut2BrD7X2OIQKZhZgdx3flGInPBcY3ckDiRY_mYnnplc907PsRUU1KPBcu9YODn6CS1knyhs-XQbSCxUPJL3eKOhC5ZFb5L6cAVqzVnjL3ADxd3p7Cd2S1A0eJd7jTecATI8pChpS9POkHb4ZNOz5jpXHpvut05fbY37C3k99KgKOqH2TBoldm4Rekwn83CSCLcyFWyGG6XvR9RyEC3pckeRzqTVpclJuYHUUVOIBhfhOoveOiQo6YyHNG5KrUqbWRJsSTVCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzgJetNvseMYqyMTDXz8VpMiJtJDvCE8_aPs1WHqZtwSMjKHm_BH5C7Age3qhW2akh14Xc9G2PcQsKkQZKkl-NneTLBF_GePuqYCUXw82mbVWXH79yqw5hRSTvO4Zc2DiZv1PGwBzJxL-M8TWNxvWvi9zaT8DbUd51pyE2w1_T02t2UNMwnAinkOMaTSpNR2NfjZYf7MtyLcaZKcJHDqAIvWVhWm6isYelzhJMm3iYuLvTp-3K8Sa56N0qaLXLDz7k9xVzHb5MxCtbR2hx7loRYnRqp-2czx5bMvzXghPXNrJspqET_H1HboFAWgyLSY0bOhhnmu1kUGfPnUxJ_Wkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVXL2bUlZapVHtCEUmRMP02IDSoho9k6m7wV3fZn767FDPAcdy5oUi44owe2SiVjp3G6WvuMqPTZ67sTr2-GnAXfQPByle7DF7XR091IE8QLKhMehIDti3WywifpDtVojoijkjoKc3O47y3V-DqLXq5N3qFGGtL6nZwbIeraqVkE1owJSJjzbgWJMXntikKnek6l_KBJ_5I7Pus5qRiw0bejHpofOsn8JJdr90gh-Fjo7kPjOZfzwM6zRw3FV-yBOp0nP2TRdiPtcUq65ZxkuQoU9TJSODImQWs1Xxy-FRIRZK5lx-Lpisy2slktHB4ZnCbxb30MwfAE21vYZ697TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2-XtvhIT2dXg3T8ZDSzGpr5Ri1LlWIGbqlZMx6Cn2sakqEDVPHSB9gNTWZ3WXAxp4V3pxL_wtICfGGuNsj4ySCe-LkwmVAGdSJVBYJ1jHIPaTTRHYXqvkl4UkfGNn64HiOdaX6qLOO_9wEau3RFiGbPl5EkL2SlGD66n8ShP4OD3_F_bHvjKW-3ofeWvqsF78D2e3ODj_9BHjDSFM_8mZiSJ18ofYcwllOlt0oWGtNzkO0XJhmpfrfKvTom23fhwf9SZd77yYPUpS_Fdws3s65e8ZxJW98--1VXMQWNtFQATIqWP41rKrd3MTt-fYgncjyoiYs5Z_1JkQBXhYkGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZCG_NUaggCgVSqV2JxWyr-PeWUafL5UqTA5isK_Hb1gX_bXMTR7lj2b1vGcr0spUNIWUW_59-0CWk2H_H70ouS_sF2kuHv5ryKJSkZ3faoaXKxMlsClqQHSBE-Nw2XE8_rkKPRObRDCxsRm3Bre3cV-ZUsjJ7s_wIyoDLjDvsk8-GEqqaLd295-ACcAH9t2b3OAvXCIlxNFAI5ME8XpXGenXh9BBzmyxq_1smY6sx1bdc_T8iDeD_pqDZA_90BFg1Y2H6iKbrirf0oMZKQqmgHi_u1H_XrBQSVuDY74un3Mc4flLjL2toXcRL2neqsCwjYSqIBITh606NI0WbgbXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuwiNEdgQoMu4ir_RMKua310Ci2EF-vsstprFYhuG6sz4mQ7YTQWsc2V0L9ftAElK460Yv1p-Mocdbr-AJ7ctnneFmwUT7FSqPPV7OkjatUtCRQxjjE0GvbE7QEs3sSfovNvDbyhcyJ2BDeOrf-xOdlXkHWY3Pt1uQSijzq1EPdFMOwO5KaxHZxgoEaWqgp-Khi5Ey-JFB6f7I0wglX4BzHVeZm5C0egMCiWgfoAiQi-3JOo0g2VtgEdqEMVMLBQ4laBVHUBKOWQuNWB_gaTJKn8Kpn23aGLTZX7gXqHaeuXBkoARezp6qsmE1DZS0Io0S9Ew1ye_1asIUWswAIF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
