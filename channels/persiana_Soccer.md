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
<p>@persiana_Soccer • 👥 202K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 01:38:29</div>
<hr>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqqQ_ouYSkKg2MXRo0bFyy6Momh5OKP6n-9Yy_fOJU6YZU1SZ5IJXQ6MYblEmCEGIBmK5jGiEQr2eZpwoZQYVP_aygYbsjywaf917JpJDNLIFuZa6jJ39benD4ibInAyHrWEJ9h9ajjnJ_D1Kzs1J5iNgHoukJbn6DfwBxX31x20VdWsCEt8A5564n819BhElVsjWjbAAsowzdpG5ohYCfg3PqesKU3MD98emwIGYKkFBsD5hB12hcDv74wY_H8S6fb5N4CBRb9FVbhxT75YA-3D9rjyhWB2Z7yv5TJiWkeN9PAfNGjBmNj2Y-tYI8OEyS9m5NV70-fzZYlazyhiBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsJ9ZhBpJiV4G5f3rlk4MbYvUl60ITqt7J1RAFAsTMDpeGpy7isF0QF-QIcyx_jX7-_Jk8MTgHZ-uk75NGa-HBRidZNBivuS-fxTM7FReaslZJialScVuflWAefzfrEDI-5ZMLYuiX8XbervNAqO7S7ApbwgFs4YwGse2sXnb2CrFncUawWP52E3A7D8NFaqWEIUQzN5qdQbsjNImm3gjV5rYehKav-ZoRlN7-g0bMzyRj3usWO0bUtl_GFJPdJqfGPyM2tQjAc2gj4lAG4H5ypnyZURsKpSM242dZqWbHhzPPJBRwIr9AiGhHlIiiKnmBQyIXjc_SydmXHTXxR5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHRxCcWGezD6nf0KR6pKAC3ScpkpcJkgIBdhK5ZJPdM99kp8coOd21NLMLLCzt5mkbGFTEKokuw6GbWehPaFBf62bnSh6rqM2zDBhlKJ7d00zyv7WOk3RubsdDJ9QBsWOXRlIKfIjl9oWgjNwrTP6RSDcp-x4FxuTbhJBepnivgwsTCOT8VGnqLM0iiyLFiot39FGXqjTw9f36w99kN_SgQ27DkqU-R3DsrZJUZ5rxx6EHtxiuQETyam-Q4upkParSpOZJ4u91I28SyVIzFgOOumzillUEn4GNLpf_S30kiFE_glRukaksamAafMOmOdwW4FxlZ7DzvidoL8hnvQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJOqj5SfJwQNcqYMr6OnT4cezIl4cGikU6ntyyC6nYb5BgZ2csDdxbVa77-0M6crmMWYx43zmwnMFfEohjATBNhUoY8Xyy0OutCLnAWtMyJG2c3w7VRXxRzByR70IptS3UtSFM4UtYQ_d_rOfFRJkvGaP63rwsT62HLRLCuLBmqb3oRCX9_kio2EijI2s2f76pmKigiX8wRxXX_clx31xtlZ-_CvjYNcmo1cxdTT1Zk8QTnSPyHCIGr-_R7C8Ay_w_f_Q1PcmNUNnCUXE9V8H6ClZXWkrSAuPV976MY0-g_vE4UhnngRc0dTjbLOREGvwMkGhpfhfhcA03yOJiowDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22203">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/persiana_Soccer/22203" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdxLx5hzevnX_wfbzRu6ztRUiqtOm6OvD4WYr4Xx378sJJi3ecjzeIi3_OxjJ6bM0beQRvsxuYRuijZaJu-J0ydz1bKDxN2oEChhMqXy46EHw_qVxH1as8ye8VqfLQATsW0dSBMxB6Ly8VPqlDxU_2Oq-SqYefjU8hnGKD3g1SNIyLIsf0TNZfYPGzEN8FbqADUFKNuzw9RtE5V3xh4bRiFD-rbNCrs1_Oy89jwAyZ2zdt_vPBBIolvCy8f-gGdiEAzxQXFzPO8hp0RLaPKYofzJ0IFSRPPfv8EnJVHlWV6ChQIGtuqsys-Y3c8dqEvOkynJASUtG7JhNKqIHYZvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lP0yx0hhl1ztyHrt9ERWKOumwuin6RVET6YKmxscGey6ZBgGyhuk_9TsiImH5VVt7b9bUmmFOpSTSuppPdmptY4nRydDyop2xnKyPLCUJwZrFgpeh2Gpx_SESoRdokALd7RAzKu7WOchzRle5tPBEQgcksLIKmFD-uw9EDYpAk_Zjm6_w8smaCjUhKu6Ou91ck0lxZKqnjPgfGqJxwHpoX4JiHhZzCbLADEWRYuw4abRRllZvO_NqOpVwTUvw4RqCe-xR6YTO21rsNcRgBsxea2BogV05m_LBgxEozVIQneHJCIznOO0jSzCmJ8aQrCJ7yiIcKaPgWFICVapC236Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgtw0tmeZ50w_RNkj9yBzKYmRTYgoRtSvP2Dp0WPmwxhVXmYIf3Xg1BMDbhQgLb1sgi6kljkb8Qjo5JZNH_ThV9ZYr0J9mlgQhDa_i8_rriSTHuad6XJQd6yJwzu0nJk1oDf8p03Fpa94j-r4jpqzpqakISuD_m2MVZueyEayWflHFVZzAKsMvrUhXDTpnNoElqVu82w_8PginJTwpW6KwI19DfDlw-FphdOuwPl3-beq6_WbBsaxkROWcOI7sMlvyaaKkq8vldPvZopYZwoYc-uwZHV0YoFLuEzYMHfem4gznz5MwlcRn9kXJhDN8H8Y4YlBQXSaW2-a79ra6acJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceoGJv0ojutbhZ_2zF0TVaYus1enO-qRE8nJTmBQZnevPOj7WcjJPKaaMjySA-xxGvZcDfsDh5Eg3AfIKXHNyWRsa6Z5zgg4mkSP2tjH_AYnay-teksMdmuf7N2Onne3Vdv2eCCTIR0hCyyLw2kxzdWMgpIF7SUaSwyvdew3rXj8hB9w6jfgQ4ycus_kLpM3JOxJX1NOdXuL7nIEetzUV125AB37k177R3W5Gj5Q1mQhT8NMde0ltrcSkEL1re7q9e4YWcDuD2UU7aV7ZzgmRd2-V-RP7IGklSg6V-BnYh_Jp3mw3HnYQ2faLVHglWFAR-SentGgx1SXanhcU3Lkew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwqx5rh0Ongyjaa_IrDuVrgcGoKx_Dki9WXI1OnoV_jwVX76LEPbv8afKzeqdsGhlTQ1oeDKq7j5YpPkKWAV8kUu8O5KzqKJImxb-OJedd8MKubWYj4vFcnaVfhwBwEjCymxM7cPEfkf20G_JJJbNOocYWcq6OO244Y4uwU_l9EEw-Yfjp061-yRveiqu238i1cOUuGv6rX5PgrrNDdL7COdg61w4nKOezgmQBJn8AMMr0TOOYaplBqcFoX9zU2dWcjTq46wHz7M5JImKniHZI_h5rKmA63ldAznEHJKEjn7AcP2fPvAXM1VGmc1QYAwJEZ4bveYGmBzgv37-gIHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZuOYyx_uNxkqSImfVZzEzQEssr8M2bgz3C8Z9PrClRpGzudHSOyBOTgfdgPV4_kY4d5ofqMRIV_obSEZDhu6ua-XhBruxpXcnoo9mB1XlZ2Mc23nDiNeo0lYou_g8g-_sylE91xqUlZLJxLCwbAN_OWQltmIVTYuqZPusLaJ2exxePX3-Ss2Lf69frlCl0L5YQwbpWdH-22Iv68cg2aK0jVJozE5liG7BpW_hkFpu8h4ktEQXR-Ei-frWYrKm9uMIKqQYAEwubpr_YaFAOLv5Cz4qUqQxGtvkKMyIvHTN9zdwdgx_0K2v5tZn9wTaY_LVUNOHhfBuTccVKp2XPCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_pLfTPtv7hX0PVo4PP0E5l-het7O5Y_uyUCAE_Tm5Bopf2uadgqEMrYCQ-GBcp-dlv2C57JBrPKAz6q2JfELD7nFq1cz7yef6oHFx_X_2HJxhpWlXf3d8q65hJkx3u0bcHWgevsMsqVjlAYrEfy6INsem1n78-OCtvQyA3W3BnC-9scZZPd7Vcw0p7iQUa3YgBx_cw0y-4keoX8oI7VHFt9h2-srfO0k_sq8MGF1Db2hGwgRcEJwxE0X9c8WQmWUqTnfJec1aWOrRmoC-M5EeBEC9OLfmp1dDyAWQafTam6jFXLtJxx-p__YIiLyqTsJf9AxEtTRY8TItFZ4CNCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntWT2jgziyTQ4d_66k0Stj6XP0MwzOVPMkrAmfAivp09NhiRQoBqBy9N6lc6Y9KRD8qhWvRIhpy-bSkD5ZkRZW5q1ifLfihwTTWi5OLqXWvGCyVKYU2suA4cT6NSMkVuF_DVCsaHM2zgXf8j-I30_1VK6VaxHZX6pAY23KQXc3b-kqXW-P-8ZVKVi8UQraXRw_RPuLKc4xCHFDLHw-3cadrE-4mNN54Op-cIiXzWxaZr1-N169JqmwnMPSG4p8F3tiums-fwmUXgZw4eSJsvYYw8DSqK7EYMIpe7HlEKacvgewUMMxcnZJ0dlqFByhfWwDDn3oRs2a_p4V1lM5q8Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAMuFcyOace0VG3FdSseQLZyN82S8ukvkWo-SSG7nelNrjrnjIvTQPzKtJpnSIvADr4wW-X0kn5Port5rvrnJRT7oNnRSnLcZiTMC35HGlUL8xxUYy_E9aF-2sTu_zApqP-iPmw0F9vfHIXLn_kn6BOickjAc1r308C4xMhIaY9ZWfHEMUBYFqScOmiuXo46kyuRmDD1KqOmw5Do_OYJbPaL8Y_oZS0Iah5fhf4b3hlsfK3cqliRqfuV1kG-ew-R7Dvk-pfwph9fQlDecFfcqC0QXwbaWbEhuNmaeEFr1B7yemXMk198f8FQV0cx4CEMRC7_iUYV7FF6MASFmNtSxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_PkDSHOW9zeRMw4ewPj7wQ4gN_sXS6VDyrI0EuwI-t8Bbe1M-iZCxlyZy6nSnC28LruWxIWVMfDdAY9EyZ_njic8CxufOh3KuG_S0ESCyne2dxQdAPCfa_xPE1Yhq-grs-szrD6myEaAInI-G_0Sy890onK6sEkMtetVGDN_6aSia3I28jQies9O2gSkMFgLq6tZAYWkvwR_qFpWriFO6WXz6w1MvrZd7WgCZr8HR5W3X3usyxQOsQIHHi8eaxUfoQ5afe_K_beKit_76HFXyheE97hS2qqkf3JddZoQxVneOm8HpGwVXvM4rEbp0TsPIWmyjrWp5CUEN9gY4I7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwux93A2rCIMYoWLeMZ25KE657UFBLVXn_euMBGwOCqQKCghS9CTNtinsbzpwNfsNUUagtiXUljvy7WvsiJhL4u2mq4cIff7Yd9kWB3rOmNJkbRsUZqne0ja92spsRSmEhI0yQLTUu-ivek_qL6wELEFY8Z9athPjJrKk45YNIGnHKiUJmyFap6MJ-BINcvBry5SIHzmSbH-jxUHrLf7HC7mAnAi_08cdMcV3Nfg3t8J0CZTsxVscbiktfOXSFMFTXL0yGuNWxm_gO5BtmHd5IDAq0y1LEcb8_PlzzLdMH2KLFYlo06pkrt2PRHN6ThThSAqVHG09_E1-QT3uCtoSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7hBI9NWoFKIB3XyPuUU-LQ3RRwBTIeQOjJ_z8-wjW0pMtUY7XbM2KRhEp2Efip8WD-ghxKCvhN75zQ5ZZLVbXJ6D5VdQt9BDXfpVSKSRbeksASMbUwqoU4rK5Pwe33oFcMFgrIi52hY3fwOSEQ02WWTI0PC9_wQ0zGhwsc7cWYjx26c_3q2hr12Xch9rB_Ebyud4d1POjSe1QTLcv5uM-fbQlVqwnnVu-9_1Gt6A__86biO9vuv9m1f8TBmqhQO50xyJjjaJ_kUNE-j_AvFo2Xdylzfl2jLTMntnMAgJAYZPbcpAzNWbWFf-TNp36SzUUSHE0dIhLMgIOtQTpaLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6ofVvfNyj-aWA4j9haelPesDryqX_Fc1pTbuINNzIujxK6gCyWXWwBTJ_tNHNhLIUxa76FjvxtfFzz_jIGouZul_d_kMpubywbcuE4_CU7fiqpEr3FF3ZWpRLkREpqNycGMIfHEffqe58v_xdoT6vxoMpmq5Mvgh68IvXmqOyT47J128dm4ZAD-lRzTIafjOwxe1ZpXpfiuFJfBF18egL-GSRe1yHm7JWhlW_LWdjp4dv2GquErVxT4ITZhgp7LabVW2LQBUjozhI3qbwJQjOvXBZ9Swn4HuEK8CfJeHiiEut2IErZyUUdkTGhVFKDNHy4plp8cEMl4UmZKaRr-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgJWnisfCNaCVdujDf9cy28xWwbz3Oq-GGYDB0sZxAIkjl0lgVK93JVVNWN4P4d4K6IojEoCFiyN-8zjcF5IMqgVT9uGxsYYCUxa-oIqkztVgJSBjE84kW6zpnFWmH3r5G_skryoRLhDwiskTN4kOT1WvmqPZdDVkOFLfjJtKws8MBvbp2nLqh0wKO4ycn8Jl0tvW1uxkJT6JAzL9G8eElsScYvZD5OFotHrVijNM7TZ7d4qKCypBuwEaECAYewa3U1S_s5v--_0jjD77UMTHfluOcZXV2nq0CS0Ab1SZj9yCuBIRH3kMy3E8zz8o42aMMk8_24Gr6cTPcCVM5Qykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=SMSgThEq20KoBrzp8Suut3uYEP-LUQism5ePmrtiJWyHXr9zWU76iLHwcpYInkXk3JDPNcZIJ-ZnLb1T4-3gZMsrZeYtjg0EOKvYTcoPRXZLYJ38lkb_g-pm9VdCVmcQayimT5-pU_TMElwSN_tpSYvvi86Atcca-o-cp_PUnBY1wFmFuRmJKQZpQYX7xNXXP1IU7EWgK96XzIQBqSo7Gg-KwL7qk95dxeB7QrzjN-71htvWEBvCXIOLlNu3nIzXJSZ_40t-ePUdsNzZ26EoOEw8XMd1Z3h1d78B91LendgydjpId9i_w9rTYH_nPqz6hag5MNM6YmAj8EZEWx0_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=SMSgThEq20KoBrzp8Suut3uYEP-LUQism5ePmrtiJWyHXr9zWU76iLHwcpYInkXk3JDPNcZIJ-ZnLb1T4-3gZMsrZeYtjg0EOKvYTcoPRXZLYJ38lkb_g-pm9VdCVmcQayimT5-pU_TMElwSN_tpSYvvi86Atcca-o-cp_PUnBY1wFmFuRmJKQZpQYX7xNXXP1IU7EWgK96XzIQBqSo7Gg-KwL7qk95dxeB7QrzjN-71htvWEBvCXIOLlNu3nIzXJSZ_40t-ePUdsNzZ26EoOEw8XMd1Z3h1d78B91LendgydjpId9i_w9rTYH_nPqz6hag5MNM6YmAj8EZEWx0_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuoFetV71KluTeoswC1gAqnqBoG0558HjBOkLrEQaBFwBs1BvTTiNjjkvAihZyZiUxR5YiDBexVeBf-JkJwDvtD2PSpvEJYCC8Dv-xz4cIm0KsKx2dHgPF5R718465leRUL52IZwRV5wK1qSeN987wrJGaoaucA72WuPYmZ4oYfJpF4MWnOQSKonTSBf9vByHHonpY4hutozQRvhE5-PycZiRAswVqWEv-1utwhTGqhp-JY9ReUDDMCeRvQ1s27Z9p6LMZfKbpirA8SuziPQySpHo3MvqKfFPgYw0v_pLLAXdCm4rdjfUfpCq9mpq9yknBtifaFO7nUjky6c7iHweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlaoRJc4M0spKsIl2TrEyOkATYPDUXG5kQOUnHk6o7dutgKaC_i69Re83sosrwI53PzhFYIzfFRsCARxM09QEf5guOKDlJfLOZ_z2A25vPYrtp5KGQNOu27LZ9XdrCJDb3jmpSUMl8OAiboBau5IjjiQQ2TR6KehTbbkEy88lOANESQPmJ-haoBzc7eGxGYL2f6x4IHzLxh9OFmkaaSs7LQRw9q8Juy5sIxhW5idKsWVO1Ae_zDCZ-1rHGzdSz0Say25hPTGaRNBYNTaM1H6M886XzJ6Pk0MXJ9YMlukkolnF7v75evDl_OpeZvOEkbDfEpq1FFuzFQsU8IR2thWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1bjdSIguSVIMnSNZboAZeBHmJ7Um-ecddZI-Ce9tNDtX-h1qVTmpIBYUwnEr8Hi-3dilI8sKolpsmm6JjbGExmDsdjJkwshIZEmYE3W9pD-C50hZBcDQftsiB1GixoEZ4yvhtOrOPxNiKUElgNktHcSwDTQdDER-YYAE_UJqzWdfUJyybeRkc5zBxqQPccylnVwdTbh21a2UtFWMdr6-pnXI-HkWmu9zyGioemITSDTbPcqurzRtf0HM3XAiYNax1LwQGvqNbHztbQO-njZWK5sORaBBvLYxmbxSHuXKknnmweF4lf6ka6kjhmKG7acpL3hWsohFFbXrtddEebpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJhgnMeQqeZ_WcR_kt9lfmhfaLQLmQUgO2ZxFelSIL0xau1ARcWPgkKZTI5XiQOJFLVzaqn30jhaKFPHmV8bhsx8oVEzLlXJ5yv8AX3zPuvT7LB0yFEGoOVio24ibWD64FfhoB-LCMwPh8_xgOCrkbK1-r0h0x0k7p0DUuuEh1VEgjMSHlqtgLrDURSgYee3yam_A_9VDt2wlVXG8l57V5jzqeUGSlQOSyWiYAoju0iLTonA7NQ5mjXklwER4Ksn3wvqf3X0zZR4DKhXTmSJnAAknfOByo7wrqndXJOa2zECzVzvYQimqKMPIfrKUIIXCjAklmv3Yxttbw7BI2j6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TszEaqRVx4kUT0z41L6JdotFuzkLTdPOCCZTl_SVE4jTC7DEPLT1M44ugYKd-6waMHZK0beROFMxFwQ3HUpzqOTrbBvct1SDYaEKB8L5XIxxF8ZyyvAcarXhgGHOLszRDdR2eL9jLK5VlDdc6HTE9O8WoRakXr4GhQHKuPris1cI4Fm0B9qOcQaynpsUkqlsK7-wI75h5QDTsLB2HPc4Xf3HNrO455xBJcDxmdy0RWysJJHhlxvXvKleTwQ9wGSdy529NOuZ18X1uGgGJuHRRGLvOI_3vxRcxvS9B_rhqRRbbdjznbFYjY8sDg0xG9XQwP8qdNdP7XSESlcPPc9gDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZ_mD-_u6zIPYuRJqvfXSfLpP-Jaa-RXo81WXmxwTrhFy5jc2OTpgsb5Ih6o4fECbYiTdDWp-Mdq0ExMMVPMy1eam9D4LVEF6v1td8NVlsax3qD8YCzRD6NWtCjvsbTAK2EwP2nqtp3AF-mDA96GggUxSMMjvDRON9364AgJ6sLqyXo9gnSgASbq8enPsfcQuJgdI9NulPqNb1yYi8TmVcQS_iIuUdhAhoQeucF-AcMJAYu-6r3pHCP-7mFNB_Z3t3oUusTp6_yktMP2PfFr3WNvlrwIcEP0w55zN0eJmeF5LDbKJbps2L8WC2XlIaCMsSG_NCP7p49aJIrYTpx1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGQfON1oBeGi3z53RglWn1GkQ4XksgTnvE66UkcNGVzFD5TaJSsxz6qi9XrwCVKcGyQ5xp5ty21NRHAOQcN_yn_CoRv8ZHVcb78jHza4PMaaF80-tzPwTXYWp3aHrk_VKiemI5LCASgTJNF40pJgIfh_NbdxDX3iyHUozJuChTVioYCAhFB5Mc9naK88UrJWrZUcht1tG04UMy-WgGFFhqMKVHV7L4a_hzKIXrsHBfNpITY_8WuwVxbE_F5xbLSiA3THAqQ13906hPYE8zrjbhfdeRXHx2v8iSMJ1R8s82Fw22csGRgA0JTSHvzT1DFHRLdP3Vsf2TCj9UiNUo2EGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrA7X00SKPFI2m3OEAKOAFMOkS3OIVMl99op8w5RHzGyxwvpBabGhAA7Mua7SUg6netXDH1xT2h3GpxQqpfc2iDs8huxzW7u9TRbuYpVhdx7iS0Z7UEU6WMwUTa3jvOpX1VV-3cI3k6k7qIreWBtgNNC4JYCGU5ELq8qvnP07pBAakKS_xc61jgJ7sL-8nYncnUTvSCnY_CpsXd6LSIDMmhSUBE91kejsaykydyvxHI450QeReYcFqjmfnQPG9qm2ZhC2yEJj1A52emwXKBwPMUAofmiGQVkqdqCb2RSCaR7PZbViUC4QUrjqi5OtAkLSINk3j3u779fy_wtIz1vpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YylBHrUJih8UOLX_Xbh3udx1h8HuvvvDREFqpnE1BaaGg72LVm_10-w_8O0964HEFOOcsMoDmRo_C_Bk4NinDVDKyB2HqLq3WmQBHpQMhBFg0J8-2Z-btv1JA1q8YfbSv50nvJscuST5NOVbMee5hqSee_j23-BNK40JN2EXpPGRGTAi2LlFVsBZgk46YRXRuVGXQ6FYzPmnTVxM0zVou0u28fyyjsi6U5I_pGFGK4imQB0yXYzOKJORcmH3Tkv8xJWPRt_B7lg3s40-vu2SKNqAwOYXP7YyEsmLkoCQCPJdbFQ7tBW42ItKGZAe2JZlWUoH8rvysqMHcCw0iqfG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZZ9ufDq12GAUUWJ0gpqrI0Lg2hivlFv5VVmu6TCwmuSK8B2Ao85jCgd-ffFRcsXGkRivc525JvhYFjdRQABhf7tiFSNC8IJywulYrpqleeoN-rahPvt5wCxRd5Ko1ffZa2fwrO8g9hYyspbkpfGk2DM3xWxkdKfxuxGRHHw4moxi6jqQQtfxOZXGM0Y-QpGBWl9Bf9qXvyMqnDDJ5FaTLzr6ebK2o-SlOOSF6Ir2416EbwXCpDX3yWE82KbUjD93FslVL10LxFnByXanPS0mNCqr3QNVg8ruU-gz-rq2KyRsx42MSv1Ag8X4hO_UGCB2_4dEwqHceNzYJYiyncUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO_HxD_GBUAfyE84bIxOMYl2j_rduFXRcv1k5w7fkV7o4A9GlxlaCEGpShae8i3XECEdbD9awAxDnfrc8kWFAju-wfgMl3ULflS4SmxmCoQS_l3mVThHpbk0L2Kxw2pNfugYO9GK8c1gqDy_iTHZBiJGCctxFOj4yZTjFlVlA10Q51-qEjc94s-MF8JYWLuFWn7xja5XFutL6EPDq-p35-V9zaKsySjQ31IUPNGR6Ln9KG4LIBkTw9wHtUVkXYtgdogUYj3PDWbhl5Ie-srZJoNhnJuhJAdu1kTqX1vJqmGrmGsab-NnKNHFvWoG3ehF8VedGeIrNYwUVfEnrMGkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD1qhKF16ssiQrEzLJPDMjbRelJVEEgcnidN6LqDordHYMuAWf7abi6bM7iI-xcd9mymS_h6idPnpwzcJjiI8f739fvH-hFyNk4dU4gnOtJ-uxWRzqbBQHE1efTbidUzQ6KNCr1QJYud0z43N0Ht7kGfB3cbj50szozGO3CiXi2U1FzCWpNgJ-f5Vnx-imr7ayV0qjNCSbZv4o-Kx1yRwn38g3BA6CfDTRy52ZGbXCC9rqWmHzmuICjCixN8Ec941v6BwdOK2fDDXcwcxw0alO5Kg1vsLckC762b-LQhb3317ITlnaOn-GNZCoQ0XBcNmfUdXQ_FLFt4DQT2hCbvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaghYcHuir-XlloynDE9gvFwLUrC_lrp6PWSGXcjapMJvHOdjV2fXaEBIeamjBoeYqXy_LigzjPp7GYIN14CaK34ThZN-ADKcU_pebWJy7vGmto1PnTcfHvjEdto9Ga3H6tHVCcrBkUUPCkkDrdsAaQt4gwsdwP5Ju473jmn3Dgr5l4abR16qdUXYkDUNdlDNdEzPu9stL-qkCV38vXeIE2eb3kTt_NNoPYNHmGwOxTspb0yDsBhiDoyYcCvxJmb8J8o0mgwz7zH7fDn-CNjd1iz5Q0EXYIaM_uLFhJ-niBRMiDjEoaj1XkkQXb6qNsrL_zg5_8Z7I8mRUMHtH4hag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NefyyB9F7p__K3BsZpt3sQ4FXCJ_K4PFtOoY0N7FeyCXrzauAK42GxftBjTt64yaApCvD3PXJOrKaggo-Hn_QQgkpcd8gj4SD63_rvM7rRLR2cMfGZibjjRlV5QS4VT25E3f6ZH5paM7K91xH_JS2fp3UOJAc_2B_ab4Ag_gqvyOoKUBL0V4mn7PDMbc3c9elPVdon_QBOdY5t9GSP3Bf2ssBgju8Pl3WoXdOcKUyKRWg_cmEeWDfzb7AzqW_DZdk3824LYj2g28UUhvQpl4sNdKN3oieziZ4q0JTY2A5JoXt2SZFifQDXFfVvbpF-JAQZvuE4NpHbGSKQ_U1ILthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY0cdDJeUMHm6W-d91ChDzgJrQbWOYGLBSNixOZUxR6mamb7W9ojnoLPRZYO780FWh30bghWWVWJwkK5XFXRpkrozVTP7IPJFJU0qZTlu7QavHP-8c8-Kwr1Q0bYXlxZVuKR7Qx5aDjKZjPJaHnnxTnPsQznBUF_PtuAhF6ZwHliPY9esHJOWO0ekyY2GeZ55s4-28hZ7vhPLbBbaNM9orDfk3jHWfBJ59TsYc0t_mp3j-Vy-254Vev_LPG7uzBktp9FYi8piZeH0h_BELKsJsasdCcV-6aPaZhOumbG1mNbC813naZcQxNv8lOBIZ1_LhZmNAWu1SxS6QfUw9aG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGugVd5f8akBJd5ndNc8VBbVNuYiukCbwI9OimYRUdVg0jIa4jn-pK8S2vNExPrcKgd7OxsaxMoo4CpCr1Zyviy6pdfBV-xAyxSGg6ThbRTaZrnUBxKyX70eZktEg0TTO-uaUfqi8CMkZduRG9P8jwtYnEhmoISDDLPpvwQDO9zMZ88MlYoHPb1kvj_1ABUOGH3yqeLXNtN_5jgE5RF11oMrslrb3tpVLdwFFKES96HRkfvSB0HSgeHdPq7GMikGaDCXf38P7ZnzGQEmONTGDIPCAhzI1HzAG0-VZp1J5tSE4oXGedJgVt61Q-iTSjmk1hmEpakiGYptMu8cgODwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt3lb6hpYrrxT9_TEbeQ4STdw4qOdQmDNrk1bzKLDip1jwSEHXrc1LuHUK25_qeDBUbWDyy_OHSGzx2TRwkHLcrXqpIV81mziBeLBEfLQH4lgwSzyBM3iYD67otYWDPEBFKKgPN7-NkVzHOzCKg0A89KupcL-p6qayfANGQ67VrX6eXibYyVZ08PMsVIey36DYCwkkdxBe0cDA2P0eoj0njRU7htlZ8wlUOMl1EFoR-Lv2TrtOLZNpGI1zrsdaYi8XS8gq-SCIPrHfTDqnoItCVn9hEZMOHv_-kgclvxHq_gIkg4caW4FrfrBaEX0aC1svOMUvlljKRHRXAtp7tBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5v4Zj_dxrgp6aUJPuH6RobZ8LoNyuT9ipQ8T9a7924sjUJVoCDjyxdrOn7s1rGN1NfUCSZlRzKRwIBrw0u8BkzMhDdqNaRPbW1UPS5_iKK4outDlfx4ZG4zDxDxfaCxXMjQqCF_XHmAv2k5bEmH5kO8vsaFB9pbX7Bv6FCfxePUWf7kn2yHzB2e-Ufvah8BQkHQcO8gOrcons5LwXA2z2iEbijg6Q2Y8VvypBCp9mWgx-jDldAhRXpujryqJmc6uFM-YsMFASeD2Pu6yOES5b_VORXp696wuSX4sCCbXwCN60dKXccfU4T_x4t5YsBepH-YHbmnHs5tRoFJfmgORQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qbgx7IEk_RfJpK-ED5TvWTiU3h9WUIYCHFEcOoxAi0N3nc4VSP7AB3AVU8ylIi43eflH0cYTIGKZp_O3vIlxR15q1U_qt2L19uxcYm3q86orfrwFNjOGfC7Su8wB2m8Brtl3Falg9YZ3dcb8FfieIgJ17tEc5VjFcC1QUhFfeZsRtpSulOOARdG-fO9oyeqn9xIBHeHHPATBFqGgO0BRkWFbhrMMKtqqpk0Cie4dWiucIlszjhGM-oFuWeOZtyjSrBJWbfGRchCTi5sXABkaXDqr0Kb-DhlHEo0WoO6lTIVW87Dg6AsXhnstBSW0fgiZ5NrSxzgjBWO8nqg2THhQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6rarq4lNAFqv4gdnh5-Knsa-lJnRV1kxW89fd5VID0QNCM9ZIfdTjTeclhkQ9HTy9NAWg8OiEbT0Nou5eY7fE5hWMcArm77utj2x_93v9NdtiVb2JttanF-1WPfb_ZkuupdWXk48RhQv3ZwoD34RAuE4NpMFJ3XCLQ2XcAn0Iy-GYAZliG7lqd8Z65pjKAa1Zccpf5mjMWWyFp14nfdkLZ9psVJm1twodqek_bvkIR34YnzbYTbJgimCjtguUp-Myvex846YnWd67IbxL_ZP0AbSePOr0HwJXeh31fo_i0JUD-AGFGzjwpEWvFp-T4UhdOcFSs3epqJ4mQReZK9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcDZRfuXsa_9J3LZBzfm69yEuHvZ5e4lj5G62gLIjNmTKIMwCqUb9cw1wuM4DiTvVX7CJHxW35X9PuMn244fFl3EfcHcBnjd8Yg_NvjG4EIttTkX5IiMVOh5fGnehAWI40S1a-0msw-x0g76SdXRycKPJkCeG5p7xOKshet_IyZjiA_0DUPUhVFw8R2s5Raen2YBAuYhsEZ9AOdWvGWG0dpgBQ3sHMP6HMzBN-2wiBNDKi2gj_jtdArlywlcq98IqohY_rqX54P-5bZj3dcnBrof0TWucmZ1GPHScYyjJKxSCSumlFsQ1xaOUpQoNa40-PBN_agpkrLzPGvxkXMZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGBJm5qmD1aXIUKNX5bABFTPE4O0H95Qz16veTlwul0yP9eizH7KDBVTnih8Y4aT2pKAmFczgE7zYvkGbbWznwCDi3M2NczRVlzdj0XINhRMpJwqP7oxpGWzB1vPzCYNeFRTJZEOvyL5PIS94Hvra70Q8D_6nSJNQ3_oNECOzG1LW6-Psk0gXCMArE23C30tT_ZnOdFM-njpDZo_S6vvGkFR335DXjO5hVqh7gmEiT3S0SDcHzf1Nzs6UIZIqkQgYbpGK9gqA2Odfu1vQCI-PJ0QbmfKpg7R7kFyOEy7Q6xpaIRMHdm4DCW-TgeartY7Q4kRZbqxBrNX9j9J5OlJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfKiLWUp7eNdLw7rkxe__g-nYJXmO_gqdZIuwVWyYOKe20JZTW5Elh_HZ9LkqhsLqTBFN1xIKXjtQ0jMInVeXhDZQU0liE57v0oTkJ8L90UB-MByON8KTJl_5wC0eHBMixhRvNGNKlj913uNCg0j9apSQkXCDlPeWOExWk3hfMAvHaZoGnXiC1XgkyE_CzH8byLS5iyWbBhI7VdxdsdZ2tS2D77t7PAIbGy7HkbP6h2556QdWl2J_Ys0JtDMryUhBMj2VAc8n84ndF80r5OQrZT1bYkC0fxnoEf7ySjHggGtCVzKSOycOolsNs98ixhQj4k1GzrXMv8tGGfsP-Dvcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edls0FVHt_3r9dhGchd4b4DrqMHIhAPwD0-o4_GJXXHUs6dTXdl_IxjnCpuL9C4G-_3qMcd9Ce5hvKFzb5zhBZ97vRLENE5S1se3VEvvBp5W70UpU-THv03sKj28dUVecTNQ9XX-OmNM5qChLT_1vqvzv3vfKg3D4SnTGTBzcFb4t-oZBZ0m-KCFnFhC9juROM4pv0XeuOY63Dhps8Q8N8C7C3LeGHBfUpbfKeHgxCv5VIarrGM9VjXjdIGuhHT8xiH5-77ysFbkCm_B9OsC1qpeyRiaPbHYyZd6VzgLNU9JIwXmLrasqbjaN2TMcXqZhBAuKpNhXKQ4om6MR9Arrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYHiVXRiUyE4OeG5Gz5d4B3UMAyzBe12xlxgM7IrA2XEm5GBYHKEekk4h5wT65DX77eTYLj8kfYk9-_Wgv02g3mTpkvuAeSSInidmsAubVk14tWr_RfVQCGxf1vB33ERRrKQSHfjHnT9pDiXXSp8Cukx1aegSOXI_cEePyznQcYHPA6ltQ6OBRN-GnC17q4FK9aPxhTVCufG8L_gDzvwb41QWN4vhYtFEmHAsxP87jAUD5f7GMTlUKV23DPrVkXDHgywXizb94oJr5ps3jRVDqe1SnEC71wou6XrYVVPZqLZmwIV_eBL9jLFU0Fiw976hIhDXLZXJ7JTc-i9hQizUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euDNv7FAAHRgqXG2fkHdR9VgCBpxonmshzpbtRSKphq3nBmYcpDaBPTd0GhFAYd782_OJEbY5X6nLD1cJO9PQHS3JzuoGTDyTy0Gl7gADaNBQ8gRro-sXLMgJK4vDGzYvnDlwx7XcuCOC7s0YvP-68WoDYs1VUbNJWU4RwP6n6bnCLhvNNFz20NaQYnoIarFwJ76d-6uoMMRUCjWyjKbSdK8uR1A15BtKTn_yxc8XT0RE7-7qttokqut34wSFMz8D_NVeEFzbWvdWkmGUVvhweR69_RvfQfPgCVo_fHxllomlVo0KoMq8Wtrr5yiBenUf3s7upfN2ppM4izqthixww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyAgGuAT0u3rnoFTt9QMuF-3CuyyYls2g5AoDbWWo897qAJEz0vREWS51gHyT4U7f-Yb3Jm6OWqs5al_5hA_QdibvCA_bQYMfs2TmDmfLI03jAGGzfG-u1HOo4wQWP2j_uA6VuGQ-q-7H5ziJe0Cvr39wbPcr1gAY_5dnkK4G9t3_o6uKbt9avEN5uEUIQzLW6OJ9i97QNuznuIXSfPeK128QN7lC_pvXvwCYCOcm7W8prIPhWR9UbbxZiLwymBRfcgGpczXPx6nc91QbF_hdKNLhSIiXgK6J9-fQiXrAjfpry0EM5mj9HMYyE7aHZDtHVPE47ZSmyuVfO_MQ-E2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drbRZ6ev0Lgyn4F-XtMBHi0R4bFLVYHr3EchRRY5UklyKecuGxrZyfiXm_0SKe0Zc_1StSStuF_eF_OPXrtr_sLXKRiBLKFQVltwcF-WxU8ZUGHCRYzVaFPhzjw3N7TZhtFbWTBnY4RDX7hNaE7H1k9gdm1jxYvGTm_1PWhzZOreuWkHn-Va_EDiAIlhvYm0UfiuAhqDk4a7UyUMBfJToF_LzZYxt9DodVOLMImI9nvqb7tQu2gKe4lC-zJ-eKSC-KjNUGfG1grnYQlrFCS9d2ImgwpadA65LYu1PQ7lYvZ-oegUpRrUjuLvj79h_gESzJpzDqQb_BD0CTB5wSzWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9qVs2WnPJEweEWZG8O8z52pgNe8r1W5etFGl_LW6t19Nvk_qJ15tzVx57wA2N7pBM6ycDTMuDSUXrorGpChCkkk8euwjni3ygnAV4Dtu71R2esuNvbdqZN8xeFRBf7A-yZPDq5ZTh4CKBCImXoI8zUN4uVZ0ho6b2Sox3Tzo-qkMcazLjwRyLjbBgfx_AXEEiXo4IklYyfJaY58Z87PDZwKXSHJYh9zPwpcrBF1SR_AKTIJID6-HQQxBGxNRLD0bTOT6-9mKCDSPgBwCDFOHDhyo5j8oR7yQVQz6pXCvmcJSNMSbbUrJZr9_RIqGXQLXo_QuoTdesWAoY3nIyMsiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bq_aapA9bMmkwfdGlz_VDpt2EFrS2ri9woH3jxW5CRouXTwmO23VQIzKB7ZijP72AeiYTLj29UWeEhX7hAOUzpwWGni9qPqAAQweZ4kbltLhbhSDbXI1YOBgBKVJ-w05rEC0qjR3M8_OzUrp1XYYiwz7zEqgqkk9iUn1e1zvGHK6gsGDmHdbRHgMUNA4ujUfuoPYa_C4Tdhbhz832eQQC1YuQKVtHjlPpQyNb2I9ShqPIbdl4RAO45LcOQSJtVCbBou0Xfv8ESEo-Q5mh4ZEF_NEuhBSlbpjJsTaVYl14Yhta8dgX_DZl_fsC4-Vn_vtUw60fHdfHcvHjgqgnHOEOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0oQ9bIiPCFhmtfUwzOrlj640sinw4hzAaIAHx89-fbj76x1B6p_6PVJ_M8coeIYABLEPDmsbIsmJitf3bDcBWRvpOZrHhUoIXXvpUXRAbqrYMnh8NJL42ZBWGSlcdaHKsG0rPfqD-kOLInFGMkGFBLKoNFhIaL1qqECflq5vt--Simh_VK42izC_HNLa4qKKGgvGoW5g59uz1H1AjPfCrAIRVv_gGeXhdnxh1F8Pkj08CPUhfsFFfznyOkcvVpsvO-vwGTWtj9mS8xXOP-qtbAUjMSiNNvu8jNoBsOYSIjYHxo6olqLxZlR2_Ay0kvps9cnRoNzKyz8jJuTMKESPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVxxboC5thqVyPC_MqouB9Dl503QXLmEytgFNtRzRfB-8waSm5spcLZgaw5lqTbB60dPT3-sdNZPKQZYSsNU4OC-vSenU3WIba9zX2AkKJdwPSydhvBpwbtWXkL4PnUyaPz8R-B5NJfgCz8ODvKnLhija06AOBW2TAlphVuyL4l3M6nZ7Imlp-3xbN-fH_rywQ0qrELQvJ7trSnbntc7d_tjejU_3uvehANz9rFKKbSg_hStOmLi33V813uSriRVDxa33O4VeDOG47zvegKBOYUFsX56y3fBZhor5HvbUgAzXH5IerNjp8Lhy_8q6PfSei_UkthcYncuqyPVXAviQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_g0mA6-hYSePq-jLMISQSWiTpDXtEcCB9IBScdZ-3e0rWiEiM9Vi7Y1CUh6r2ltVFjye4iCio4BrX9tQqlYcvPE1Ou4d7WYW0qCJW0kHKM_7vgPZS5mJ-Z48-xi7zn7ptIPTbXQxvzBvr7dGbC_nrhF_RIVLxOHu0PvD73ilxjW2U9ApU-iCTHpa_b_9Ub3fLseD_XN2CBXR0f2NqHS_W7VICv2EajgKBgHVkcNvHyHxLB703_kH-nJ5icCvFVjZDNIX0mk_HJDb6XNLdwjQ_hi_4spNhefeBD2l6vuWkeww7RGD_W1zax-igQkc5EGZOVhQIlukPeaUPIK6qZEbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-poiUDin0vCbSN6D6INPhc7o5ptM_sgQ_IqazofhNZYeLc949fnmtRY0GMqr4U7vjg_jdEQPpYucUZIzIWmjimK1Dc2k8gH9XzV0oklwfR-PE5DgSEHueAj8OkyaAx0Qz6jv5RTSWy-XT2fAe6Qw8l2wEvZsLtreoAhxMeCQLrcYDeBNPgjFZQFi10LCZl8cZE5aefIzjz8Bv6FqCOVu2qXwUxDlHORC2jjEycRoaDIc3_xUgK7LQtSYmMkAMUIBOR5DixKf5eIisOP3cDAuTDwZimcPNhbgjYEXox0KAXwQFFfudEQyQoXvsO__gyLufStnAC63vroE0x8bQio4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UufPF2H_bhoq4pkTsv71bs0v2ytzNsorgq1UAnpsa9VLnpPswXlPBJG2m4qJOyqkRt43psZ-i0rbOKX9TYxbI-X9OrZ63kN695DRmL-I9bn5LYUn9at1yc4fhapBiy6PZggGz9XJ-IU_qTMm3vTzbkaK6d6HFjnIDK5mUj2rHwFLkAV89LytlAH02btxusdRNiAXP2sUJlaWhvhSm98fmVbx4956L8r8FcHb_h50hIiI-6UlA0Nx35UBcmJ2Xt0orLmPqjqRr1xjXKNz8Hr4ngvJVrC7_f7G1TLIVntVxel8w2KZftu8APN8TLYG4RRjKdlwtFEqV6SZN2p5EAIOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln4dEOJoTTOPc5PiHettlKuiX2gX7t_Gi8W9vQU41KtH5fIsY_PFJZJIy8lB7g1qT8Mp-Rdg-c8e-U64KGllX-zB9btHkAsX8ul1zv4bghK8Cuz5_jGnLwGfbXw_EtnIsGrmARlEXcqNSe9i2zN-l8dSUl7im0p5jg9QZzL3RGvphKSuX812vXzMI78TU6yVnId144LlT9ItPen_k0n7kMIuJQvOzCpt_JIkHYuJm4eXGFh0PtWp0YS-aCIxlcVYV0gflftzUaMQ3r9ML0kYT_z-saQ7pnUnQ8XRKmnVH4m6uG_ktJp3qi0i1llods4-WmA0d_zWYjSVAaqqWogr8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6Urcd6Qt29hK7Lg08XFQCrFUCtK2oMs1ujC5x_m6dAp2nt7BkQaJc4fpA22qQkTvt3O227X8XJ1NufiOT-On4wqt1do0M0WlZVp8whGc2QPkPFZCbAwStK7Gk2FLj3sxBlGQqCP0Loem0q0S-6_QEcaq4gR4Ch3ueLJVPh1Qt72wJe74Ag91UXyEGaSgw4rA9niZjYZhIe-0OOtWWvxi7iF2Ss_AUlwVaA3qcqmS9qyF3bVOjs5TyikqQb6J_PW3-mzL4KfjqqDSh-hPCTKDVIf65UJV7Q3-g6ZrDatsopVUV5W2HHeCYkUX-Y21Voi8UNKm-BoBYrqv-SkFAyP2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=LlnJ6vXOMe4lOkYZnw0MpIrBdM_VxviLJMyKYsxrs7fBF62AjXI-MRw_7-Uf7kS_KnHhpi0McCOkG3Taky17HARTtCjaUcG-orVktAGydILXPQ4_3HGEG2cz4qB8QfM0hRJjGSuvrK6n9UISFF-OIHaay1RdINdyidKYwsXgTZDgZAxaxxSoUOQhlaG9vEE4tY3uyA8OUAxubHY0WvWET5adTUKivUf0TYpF1nBtDpoxjIF7_76LQG4-kT9yUi_OM6F55hq9hv3cB3OcoGQL_q_BSGxsnOv80_ZrxCmyAgBT0RvPfIbpIQnuUEjWd-aFRhTXK6cbZs-g3fB2ufFE1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=LlnJ6vXOMe4lOkYZnw0MpIrBdM_VxviLJMyKYsxrs7fBF62AjXI-MRw_7-Uf7kS_KnHhpi0McCOkG3Taky17HARTtCjaUcG-orVktAGydILXPQ4_3HGEG2cz4qB8QfM0hRJjGSuvrK6n9UISFF-OIHaay1RdINdyidKYwsXgTZDgZAxaxxSoUOQhlaG9vEE4tY3uyA8OUAxubHY0WvWET5adTUKivUf0TYpF1nBtDpoxjIF7_76LQG4-kT9yUi_OM6F55hq9hv3cB3OcoGQL_q_BSGxsnOv80_ZrxCmyAgBT0RvPfIbpIQnuUEjWd-aFRhTXK6cbZs-g3fB2ufFE1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5P-khG291jvRnBFcIlKluAH8KsUCLyrwVhCfNRocUuvWGbJbAbZ6H07FeqJ135Igh15N3iq5cdp8mPHF9jximzW7bDNT-Pw0epXMYjTQ-oczCY088RojXAqa4_2iMiBD7J9A0zW0TDYqUzbLXHChs0eftyrKENUg5KzgsdmxnKhQSrqGvNIsrVz6N0wxiZtFFQlZoWBkzcttxPbW6dtdL2JO1C26shea9Y8MVFdPELTy3GsDJQf8M86D5TesuyR0dEs_kqK2EOm4lsMzz-lIt1rl7PpfYgGlbr7Nzv5wlwG8z9HBsqAhSqcBo_cBt9DvIqmI36SoMXdK_PuQJYZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbQQstUaLDc01pSJGu20C2uMFEBGouck8fEXlN-9eCbn7Ks2oco3hU9uWEwaNr_4oFXVV_otLri7wMOrRGMGoJ4slv55BEf4PMYUdVn3VrgPvvemJV6_exdNAou3ewGj-se0ZDWGcFhhn0R6ekl63hiSX3RJ0jw6zvWfybkZ2yXMNzkv6e7l3SyKDld8vLoEas6jpT1djpfNsbG-eDFremNH4aEgXLB3LIgQMbOzlN8T0wrJEX3o8pAq4ARY3q0hGkUNVRUi73WUSRkrdZYguXB3_7oqrbdnrBtM7weYsm_qXzmNTDaP8hZ9lBdwICqzNmfgcNsXlU8ahatWPBjI7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOs4G4aHU05A4zhuA_0UFwa_R57iwlsrwYFcmfWU6KIimc92E8TULivYLjaPDZa9kU0zwHjwIzFnI2He7CVd-98AV8EoyFBQzoD-AERy7POnygXN2bpRFhxpgZbZnbnrW7N8M8y5eTbQHDuUMtnLMcncg9ufY6feL7YrPmzk701SAOsmTaZqE1bnCBpWB6Af034Yk6vcTxSkPxiR6mNhPj7wBlnXJqFf6nC847utHWrpjDQSYH8Rkpg1Za70-Eh2Jp35haZ4HFsANMqI5j1gle4wXlXbsvOLGSSTbOZMMs1rb5Sl7lEElGjrislf4U-b0sYJXaC0toc67Ert-jC5Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK4WCWOBDJ2FtWfE7lw3YQCdB2S-jQZ8NLuHme--H5ztm9d7aK1QhwafdDcUSgzFRI9AaupwkA3QEsUVvA41pxTfnEg7a5VlEFedO6ueMiQ9nNKi1gMQpHAtHFDOfnAOO7AlH-C-uvLJweRXPkWDEOspPKsskyO57SN_J1ut7RBPiYgiqUnbP8v2Uqq_ulWfLVsnCtcN7kHInKLpOO6ve45HkPRl6tVMPOXUH-tbSNcTFJntJJf6cDXK2q3B0TlbsvVsxpl36wJmdM4R17_uPszt5EQmTFft9Jqm8TvSH4k5gqYz9w-uRA0fQAI5Z6pdecedNn-c2HQxPbRrXCfq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzF0QFKw1XET1ZioBz8wjFwjBHD3pxfJXMNehN-yQNibe1z3vUelpXFHOG2kX5dvJIu_7XMJYMaLnv5SLOWkPU641hRA8N5HXsK3xwT8MXaU3WS6eV67Z36oKvY3HLXPhwmataQd68EcJJuWkqeVsr047yFOvBQbc-vGPFG-27e8TZRDsjohR1JScc6e6PJqf3b5KSccgYq6M47JTaE5fE6wYoz0F7wlZ8jVrnvlprBk5L7n-4FRZHOBKnwXsDORAQu5_Jt-hPASyXurt-ViHbpmJ5HKA0WctvTrzlstVgqSNE6gG4IyF-baMk2S3nK2dbce-yrPLbz8ZrEGRgMyqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5YBQ7rDWDpXhlyke3CALIOzsOVaOywkKuAM2cwgeVEh-N7Nfh753Zrn5Isf4QOBiuzd9kcx6bzfJWMxv2H0WlFe8ExFHTG4JQj56hGWl6mNxO8z8ocbcb0BS6nxz5I6v3tw6Un49kRbsft_Ex2y2VbmWZDeh0HQJllosoKTT-V4aHzaZQCIzpFnihhnWG844wb54rHmXxnGx7TOgppURocdoTJYCGcYq908RCrtxY_xglNwZsG8Tfw51auGghRIRevlexBaqBsOXv9xE2WogYOSEXLWrY6f_85lLVuNK65vAtNeihqmo7Pu_hUz_fzjxy6ot-H3PmBl1Q1Ly-2Gxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQgzYDubyAYFx5dKOVrbNhxuVqlof4-djQDfC0yLUIYw2z8ePfmE4loye0doXJGrVeirrWb1gxievKNd8zRYUqPmmMtdAoRIuBo6VvaAZEjz0A8slW5MTk4tH_QXknCxUsl7fkk77Ey7UQTOj0btxcm_M4SAzETi82nKDBg5YyNstYB403q9a_8hBOQOA1AqB4P3CO69bHFDYgGRWxshmbi4p-pMgb-A6A87AAoMSA67ncAMqHgE1LpMIoTrbdU23JJ4DzzwNdx1_JSo1zY1VD1l3cNW4jeAfpPm9ZNiiz9sluSUy0k6pWmzo-kAGcIuKl7LWzcS0iJylzYkVyLTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=i-OJ5NZ2_KVqbqREDKx0zfdU6vgccNQ3Kg08k8qJE3tI1M3Ctb4_yYugJ4T1lEfZpn5W136dRxExCHWt-BTxZItzHvouj4c6E1uH4pzHJZlAuEg_PTjgVnFpDec0Bzov6k1gJXX0fHqH_mgMdX0S4dA4uol7SnDVpjYjvjYoShLsjG3v_G3nNCh7ViQCGf3XVbUXClD54J6qTDwrK607vZ8iLEQOtI5qm_57MQJIc_9X5NnoZG8Pt6wksQ3S2WmmkOL_5V-D9G9Co_Fh3SowxHqBBpxO_pY_TUgtTdW-jJjCWeqnlmLJIsZpgKF29SdPG1D818Q7MZXZ97isyDdjqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=i-OJ5NZ2_KVqbqREDKx0zfdU6vgccNQ3Kg08k8qJE3tI1M3Ctb4_yYugJ4T1lEfZpn5W136dRxExCHWt-BTxZItzHvouj4c6E1uH4pzHJZlAuEg_PTjgVnFpDec0Bzov6k1gJXX0fHqH_mgMdX0S4dA4uol7SnDVpjYjvjYoShLsjG3v_G3nNCh7ViQCGf3XVbUXClD54J6qTDwrK607vZ8iLEQOtI5qm_57MQJIc_9X5NnoZG8Pt6wksQ3S2WmmkOL_5V-D9G9Co_Fh3SowxHqBBpxO_pY_TUgtTdW-jJjCWeqnlmLJIsZpgKF29SdPG1D818Q7MZXZ97isyDdjqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtOY1ltaujS8GSThrLkabsDnU8rA7NmvGiT28cmhTqq3sjovjaqGJBzCAqNaW2YSAePmfVlOoHYKySmwMTCm5OZEFCD4FqPfmyDI1-H52G8p73cZUevTQ-AUsw55R5iHs8kFto6aovSwXBTFDS0xiKQO5gmKKGuuhE02petibHvB1kzFuQ86YIevpfAEkfRXgsatt_iqssR5tUevmF9AvNtcl7we0X-nPUNCillLDYvY06lULq0A6vnr-pwFzhbQ41yJVW-FwqfGreMm1E8NkoXs0LaRolCwDi9RGyyv-MnlIzBteKE16Yb7aVvOPsj5qlwyW22KwxGSpG36ApJ7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC9uAnW7pyCjpfRIfh1cEq5S1cRUuBvqikZN-o-L-fsUDNW0jEllzxbKieXl_YxQeYiKpKkeRTI0YyElre3qmOuda2krMLXs_bcSubHiGX05isiLhi1fCLQBjsziKGVBxVO7AJe0uEWfcadYemh5Va7HLyx0mAfnxk8cG7x0cQjjw4JEfnMRTshkNF1OufbR1wh4k3GhG45v49bF3FGA4ptiD1EEC64h-16jsh5A94BtfGf_am3IbI2eKfAEtvWTk7IjmHNg7VaxUoj8cH8NdzgkAQ8aR6gfHYvjQ6ERWXL9rM5EpQjIUQLB44yK6VRJSLLmtZJ3GLNKzvUa3gNIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=HeOLhdG7nZtbICz7dt7Qa_of5or5t7gX6TFiiKqwU5yCGzjw0c0z1NgCRY_vGM1PYLedi6EdDSh7JYq_OLpqFHKQscntHU2SuC66ZenibPD-0qA0KHm14TV_uwpv5Z-gsweX-P05JkeouK_2n0jg8oLwFpPPQi4ZXqO8Sq1RCyJ-vKULkKZ-qddNXzJXRo_Q31Wj3Noj3bzQZg86iNfATVgIsKqGTkDwp2sNHnxU7mkwyoaSYgb9R4-lzyMOsDqnn5TvdUTQnZmN0mqc8AdFhqboqH_r3toGxv4ncoCqaGj-XgLZudzV2LaOv16qLONULlIJI-d7saXqSm1Auc_1zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=HeOLhdG7nZtbICz7dt7Qa_of5or5t7gX6TFiiKqwU5yCGzjw0c0z1NgCRY_vGM1PYLedi6EdDSh7JYq_OLpqFHKQscntHU2SuC66ZenibPD-0qA0KHm14TV_uwpv5Z-gsweX-P05JkeouK_2n0jg8oLwFpPPQi4ZXqO8Sq1RCyJ-vKULkKZ-qddNXzJXRo_Q31Wj3Noj3bzQZg86iNfATVgIsKqGTkDwp2sNHnxU7mkwyoaSYgb9R4-lzyMOsDqnn5TvdUTQnZmN0mqc8AdFhqboqH_r3toGxv4ncoCqaGj-XgLZudzV2LaOv16qLONULlIJI-d7saXqSm1Auc_1zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIPnGyInK-d3uQ5GktZu6KsmiOOzxjS5mQq9wUXLG5lAURBcJRU438l9LPQFKlg4DNtKonhQGnWve2TpichiW-XGDgthfL9reCkSz_4zMUn9Inl7bOq9f32jYxHgXhGJd-OtVIDfM5kGUSRRKQSIC5gbJ9hqqxlyR6CNYy1Vhqx1s8VJrjtzbrVwU_Z-qNezwTQ3euRqxBJq5VhlH45-tE242tRKllgt9-Q2Z3WCVcw21QaoozazJI0kDhiCBEMvWy_ffWn0UX7UjOW5w5GgX29RPVKb8E400v6GSEhMNbTF14ZYWq9UPXZqbWzWEfuErG-vpxTGEQ6IWl0YHxZxKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Des0z--rYCQAH2D0KS5x4tkbUhqG3YkbKWFnt3PZo5T5AgUZQe8Ba8qxdHvy4IAM8K9wZrVHUKtHhLQYxjZCIzKuLZpk8zeffEWYwsUENHi_NAwDzMleeGBLM8GycubLCdJloHuxc7uxVLmdJHny1dqV13r5UAzJn0swtd2m68vZuEwFVzxmTzHD7ZPYHfwnzcHMVeser5vvrxPl5BAws4AS88hR-xXo6yE4iZH35a06ikkMDml51Kdkl48pFrTJgnDfGoYRoj8nd_sUunFNTgt05XkdsUb078Cx7aG28KYENRNNQHalbMFQSd6rqAZ3oVsMSTWSk2Q63-qkbxM8bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIwpBxSQn-Jg5vxGty2MiAqVQ9iUPDe6GbjyceCsfWn0-44rqRROHYkkxKkbC3NL_d1-M24NjTsrDdU06IgiTaYgzxetJViwuNDfE2IO0-ReIxTwzaQZg0QZmaEOCknG0Prxb3c11LcueDtLMXTza_1yFbieLDZnDoQ1vOtr_t3sB9jLaZc3mGs9EuGX7lVojomScofoxX0M4Q0HTWjUftRaeZf5R1UOYtPePCxsIHdgcbv0oIpk-7o389XrAkpJxGmdkubaMJ1iOKI5WdX5QTbSO2Mp0sVvrPwX4KYi2kXYCrtngCpi9AmeWswR9Cp-Fn6hCalIhKDyh4aQPqZpwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARM4JtBvJaz6WplrPoDeyfF0i43ZiuuiOoks71wePVOd0aosGgMSbv8U78MFXN6e-L13r0k37vWK1EDofBZQvDItNODwO--TSSJEBr8SWAm2rQ2Onp-jk3sCinWn_75VsjrRlCa6zxb2N7Hg0jcxfJe861AYKkp8T0yBtCuQZQav0ngEt9ETZ1WufvZ6DkcPpb-A_kfGkHNHd1Zv9Szx3F46vGdTryE9bNPKcSgz-k-gCWdgZQniHi39vcmFtgJDKF21GdfkOCWsf7-nf2m52PfXly1suNOj8kVYtPHe2sPoG_UlrpQVaslykptjg6UK9sn1RKaz6nl8nzIYHL4LaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz-kwOmeycEFM8a5vw_mdN1dld3P0ZsTavCRmC0yTDIjCOBwPD1w-euFxfT3uPwTPoQEH-_ZRA5P26zsockVcMoidJnDlUGXy3EYrZj54So4_TgRyb_MZQTx_0bO7swYZXFcgb8RvvVgdHo67yoHJcGv0BktHHWF91UIhwuw6NWDXzHmR0ssWWDyxGHUzu81J4ADDa92yYQ97DGjiBePRddTxjPqCzsgo-mrrEKQJjz5pTUKyp5HgrvsM_wobebUp3TLzIHjqR8bvCFPA1136eJQt83MSCXnyoZ7OHywQ538cmkkMU8yVirpCXGV3mk75fqb8U_Ikvb1h5u8um68qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4q9d63_9vmlMOKR9tFxG2bh8yKePgiq8gPXZvDNzedrCDvM58hvHHiNK1bQTeMjblLKIXMZuTBi0OrQeeyIRZSErn3h4ia6zZL9EA5zHxC9CHN880U1CNuf5whp6LlgZlDjfb8qaefihC2s4N6EElmN-2eas7SEAOiZ0iaH3PIlOz6mYUfPgn_eSWU-rZEYBR5y62wwRY9rvQbxt5qB_aSvHf3UYH_kdbaaPF5iFOdZjs_D7lpCuVG15NdniXfPBy1CUa2qX1OSD1TcN3ayqSTl0IgaKYmfchuC0WSip1rCo2MLyIV5T4Y6K1B7nhViy6nWF40rVTWbhB_pzhwWdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjnF7O2p4ekjCW6LUX5NOpUM4_pqSe1boImDC1vmBOoW48obgBQVwSsMxYcfYTv8rPP7CrIpMbrwuuWyYD1B-dNUmVMer_hceXA9uUnoQinFXzMa5CI5UYKOL8PjDLZqCUvIndjqdl8__BARxzmIeiNZlVeC6e6euyJKmHoczcYBo82NhcPlQCKaz0rk7rUZ6j4FVvt8SZGfIcNDjDGGQ-yJLR6qkYZTMyD-y3iWGugwF4C8E7qiq1ihbOzJpbxeZoTZvYgfYQ1FVOxeqVWK1HLSeImI25DUwuWFdpR-h-wSu8lHz_06C2pX1ZMlwfnkY9ulfliIRFsmHF7lMB66EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwdY6zW9-IxJpTAVGaiCjlkDLkAs73IEIwEwLttBay4kEqD_aOaKq7jCExy_ez1Tshtiw-GuOjOCR9pOMLD6rABROyYCb6VrMtJsWAbSnaWKGcR5Ifaa4UxMZUZWDaW3OkU2b5QUj_Tybjc_04Ex1txIexuIVAPSdLWxVOAa-FAswheyw6EuGqehz0oNJc2JOQgnCq5TnBvkT3FGyrRtZAED8CODcS68Ty3cImosb1yKpBt6lX24S5Wx4mM85sF-8duM84-RDcv3LW8uvuAFv7WJX1NQpWkVYzk2y9qrX19S62aTvdzXOKnn3HYWzp0WwmYC2O5__hKb4UI7xjzCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWKBMR4PgkPw_SAzToCWRwolNJdj-wSAdwYYMbigw9yzfSKEylnPzh8LuKIFZfrs8xaPt6CyZZXCH5KOH5ky5YNgQDXy2_sGP3wVJ7uQ72wfilnaL5MKAJOz_5hAD_JO54a2h6n3tnOWCP2bA6p5ofvb_pYoUS1ypFfTkzbsg7i2Cbbt2q7DHaI2OqJpL4ibkPHlpupOINiodGjyfI2o5r8S9Cv8uq0CQJ49uCeb8wLn-AnhvMhzXyCSrlJAUUXPuODdLM21FHmJRaYkbD60nv9ijfjl4_jVWCvEnlR3R3foPKE3YbdLOod8qXd_GKufImc0zRkQnsFYx2Yabzd8Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCYt2w9WbQIhLQU5-opT2gb2pT6kv6uoQw0tnryQmMqVIZdtwb_eAOA8dnn35eG888D3xEiLIiFbigadr0FJZow699NqBIHYdeKHfHzarhca0vLAzZAdGIWeQddQKQXY1KL_bEadW_rcl9gl3eOYNLs7VvCmzq8XtuXIP7mv0p3lOhGV0cx8zcMKOG-4cInvVVel2SrxpIcT9ZycIxSxMhQHKjJY9MddPbWHHGc8MWSbJKlJu9DirWInYvQYkXhZlnE3qh03OX418P3S4gQbhy94MkkaXCO8ssbyQU_1yCfrAmDwnP4d7PVF4NujmOUfm_X4WM9D5UsjNqtR7UXt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2oL6jwpdY7gozV-63_z4zfuQu5sWeW5boeUCLe3e7pBDBTZeW73mJ0o2yh4Cm89DwkJOVSkepmt03P24-Z-KML9GXFj7Y905FcItvUq4Y2cLS9KpseYJCc9AQ-GjxmxEmtsyMOvgpYj62H9TRofWG7bTmnMgpwm_s4Uit44DUYtlPCRoDFBvsi9ajuqqlWriNXinT0yMJB6lu-pFrlsoA0OP_ik3mjKNtl45ZmZLrluZBH1V9hDegM-d-N9ck8GMeCFmvG-LKnHg2rKe-rBv_X5jJeohL46_pLRAb4gWZ5uImLuuqvcktSX2v9mKme42OM9xiF-QBcA1XloQaTomQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOfLYez76EEbb7vRcZF9MMCK6r1zmfCoUBsNXyYunfjeCPR7jSHRgzx7DCkpizsMoonVIMT29C4_0FDxkQl3UcGFFkS7nJiTc3fAY5J4GTyNaedNM6Mkfu7L0lmfpYLzezkLL9HOi8abGFMzD6zU-e4tIF8JVe55td4rMqKUez0MPiZ-tSNsHqZ-S6JFOUDMhHgYGSDtrigC-Tu_s9oqK2uT3yck_80REiIrcH9zgMWGPq1mjNRHBJDDhxbErsn5XJgkij33OjdkC_485FtnDNncXEl_AKL5yevUxmvJQX_ORLWFuRq17BJCzzxP8G96xMH_wEqk4Q6TgbTSqZIKYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1Pgt1mYD6e3-25GTHsCnf2dMAmvVMkvIOofqA9v-Fm0QZbCmij-e1bIrSKWZSDBadqut-IOzvQDULJPr-FuFhRcgEwnwiRS5orvX6b39WL57lhxNMv4EltV2bVbzYzsL6Yhnbu6CWZGq6ZZwyQ43niUMqo-EgtxK69-1taEOypmzhGueLpiyglVvYK5k_ZAJ1rQdpGp0TPAsf42tjjoPMdZfKrcCD2n_NnaJkMQjnaFQsUprKolp26x8dIy5aTKvSWlkJkhcSiCU70IhVAYIAr_WJI9sIYh1ux2YPesEP0tKhfxviyfeeGt8oLsLS6u91P8qHljsM--ft-17br6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iERsdN6MzG73mEBW7BmtHHnfCqlGCDlSsRMVwqUfQSWkybElehDN0mGsJ36rYAhNknrgEFPESdKQn1dP0j99Skbm8hIdpJDa8kiOzaFaxOr5jDKJWq_gSrioeOHtTdbe17WhL-Ib3Tep9hepLJ0A7hcPpdzWB8iEr_mvnBvT0m_u0ebbFOkNhxQLizJ88nCGHs7oZx4T5urAHRxPPPb8HW2vfLarN69KcsbgfWXO_cMCq8vK6Vb_r9LOTvNWGNAfiRpblco0cI3nIdnBm2rsgf5EytTmql-VmvuizPRHqQc5nYkZMGDSAYEHyppm7rtqsOSzX0mgb1xiUtBaXE7ndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=ogALyshSNV-UZoLpo_wPIEQhMHfAWTrkoYoU0DyMU9-S0fAo7anfOq50zbXqbAU5Bt6Q8WvCGF4E1HlfgeZdcn6erp0Vce-tWpC352CCUtv0oV5xW96et_hbrbtncAx5gBRweaEmcNoRRO54XDIBdDgMmjE8CENPXDE5VMZBAOPZOehjzWxFNv4L0yNJj7iZmE-NMdpoMqw8U97xrNYqw0s4Gif5lhE24OsSBRg1GWVgRK9UewZQjEbF-q8dqGl75Yk5vgRzoQB_K1z31-nFSAqbw6bn7SFNOcHOBR6anEE19y-bIbk-nfmO8q6VpK3lvmWljRVXV9CXDlUvCLa_Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=ogALyshSNV-UZoLpo_wPIEQhMHfAWTrkoYoU0DyMU9-S0fAo7anfOq50zbXqbAU5Bt6Q8WvCGF4E1HlfgeZdcn6erp0Vce-tWpC352CCUtv0oV5xW96et_hbrbtncAx5gBRweaEmcNoRRO54XDIBdDgMmjE8CENPXDE5VMZBAOPZOehjzWxFNv4L0yNJj7iZmE-NMdpoMqw8U97xrNYqw0s4Gif5lhE24OsSBRg1GWVgRK9UewZQjEbF-q8dqGl75Yk5vgRzoQB_K1z31-nFSAqbw6bn7SFNOcHOBR6anEE19y-bIbk-nfmO8q6VpK3lvmWljRVXV9CXDlUvCLa_Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImeIFul3O-RZUh5Th4WcgR85SWvABth_dYlJ8a4fflSUBJz3_H1uqWem50bT1gB3e-EVptCo2mp-8-zAHy_DSTZgCDOnftJ3ekAY7ji2xFAn_H07r4D1s2MRd5ITJ_b3_lTQY23jJREtMgbiBJrn2Y09Et6Hh9Ufpfffyt_TgPjSJJ8NGCILcs4C6Rw6-ZBz-DpwoswA03T2Ate6kqV9GWyQ9hZ-wgx5pimCAnBbFePQi5ECUqAeJiCbcZu5XiJQO4BIOLF7ZNpSQizakGww0etIWGRfS86Ru7W1XtVkz7GFpOT1DByfYI81PUa0yOKvyHj66NnnJXbnaJFkokVxgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSqLTjLrwuu_bMeYaIqiW9hXeaqB0J9TDseGTgA8emWG3G9uBvItg9eUdIRCONiOm3UktZxNhACFnuyUApE2Gjhz-HAqEd8VgY1r2amAC0E54P5-h1XHyYjjaO8puQjE5goRtzGVaIiBcQSNfe81We-uDHh3DXnBK6_OyxfURkpi123LLapclMds8-Wa9CT-NQ2sSC4wxQq0-MUVeQUOC6napJOXzGjnmiqAV7d5bvPjZnMEvVNZ50kGL8noFnasqDbPxbff8iT0Trc498b5xp0aIMgSps9UrInXiPgjWl5VhWfVE9SxgiJHw7rPZmyr44NwZmrbnMiiovRRXbBnog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCiSFFuwbnOsKDAiE-DZqz8MARd_hfH_7RbVPpoFeimNQljU2LHPRhOQ6trnTX9DFlr8Sw_ZBAiQnZXJHDdQBkvAhP7Y8-vPSWXgen0qNIZLuUFchM9aQYjgDLPN1vWpHOUh6mfkuZDmisrZJ4_0F0zQ9tNAH1Al3FXvdLrvZDmNWHFIzUiJI7a8lS6nJGit1rH4b_VMMpDlT9MoLLTlEoW89FJcaLZZLH-KWzHfDkGdIZd9UX-Em5mbhV8znN6bpyz5z5HWPiuHskXv1J3NV2g9sFaZGu5Z3hdZrQFjGZj-pELrHknGPxqUuYrlZGar-g2VFAIlgq8WyOdasbNdgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoPP9Fw1HQAZog-BUzHczOdRfqO0nCQd_7EZ67GsUk5_lzIGgx26DQjBh4lSaeQc6kJsWjlbK65ekITd0I1zTXBxe2CcYDz1GJSjfjCbgq0ZwQkHGaHAtsoFJP_P25hkuTFLbcbG-cF74v33nFcPj7tOe2rojt0ATSmLre_PDU-T1EAyJJCMvEuuJQoRuyxbLHhqin_p6B-Xv-hs6W_tOC4a4PItiqjRus8_bnB616oM04KxnZVj8rRj7LD-ibjW0VUf2Hkb_aKS-VkJjuEd5KmoNqn0HhMGHoondobEZ4YMX0DglfU3hOBehg-XOcNk61p6X_PbHNC6HyPlKg8zxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdJPVMEnSAU1W8TCzqjHcBiohMQSrX2VucGi2rgsYjweKQQAp77-EUHBtWfv6yBU4YUht6f850bSKr6QNpW07kCKBlGFaUVMOZpwNX1yl-giirieejhSSDSZiyCmBgi5ZLKgf_R5hPGYXP3tvtJfrhG0LWjbGhDCZ53IpA0ynqNVrkzv6H7xuQk1db3QyQ0cIjcI1IY55taaCSFJbVPBdnn4RZrlUzzU8AvBgKif-FgzpCZLNz2PuO2uBcFPgy1IW5rHmyq2JXS5BMwx-TUTHJZrMIFsCxGKnsCrOyn20FVvSqsfSDR1wZ_-JukAACvWifgwkkQwhtN2KuFCwh_zVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHC8GyVZlEwD2HY5jlRs4lGQccoYxN0SYhbqi1-JEINzFQXffqsNal6kR9eqO85817faofB7pxHq6-n9RkjxbkyKTduBuodiumiciCXnK3NYfH51OL_R2s6Pgdb5EzqUT54o5XHRaBEqF42paF7l1NpPbQPsK6sSZH9HGZhy43DZ_tzZsLt5xH1eA5TG88zmoPYoe30BxytkohcE8KLC0Q4HbK8heklMya6_Vz4W5E9hDxluQ_1rhfxCqZWI1HqFbYW2gGG41HqEl6SsezmvNofiHnc4eaKYg6b8U4hmuR9HDB1w3TrcaIWL3t3pRIkX1iwqZpmOR_iJkK39iEbO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP7T1m51dm93MV7HcEx_dDDwP8gitMeqqBbHXpp3OJ46_qZ9BiTE9QJca8oo8t--51fndaxzI4aCmK3Wgygyxm-PYs6AFkxPkGgDiJCJQOTEAo8fuY026kf-ug2LZ8CL4MsSq182uPulKMMzQJ_fLuI0XixAePxov8z4Ik2IJAey7_ghss_j922H5dtmSV6OQUtQkqmRD_ihkJ2ak-Z3qw_2Nz8Dq-sVBiLstO9UhIRERAeSrrCKaNXb_cuxVUR5vM-E9fI-DNaT6UNc2bwNATyOu-k3_rFbcDglc1SpcMzHUV3J7dif4dbOSafaU-S4c3GX-4da5xBUYNPw-4izLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKjTJjN_6MoxF7nN2MWI2tKbStU4TFAFnpB11KfUze-w0ng6GbSTBn1slkPEYJYbKN5Dl4rPSxql66bnQw2kA6EWLDHfL3aYaMTM4K_px03pW4dzSDvKFcnggFDHCywTcq_UF_AsZLPFDUdQsuxFZl48hJMX6qrOBdv4QHEE_JyKJnfWsutbXinj6dPIxEz8vq2VK2-lVzXd_ySU_1SSHNX6cZVVi8cryqDpbSTQt-EcOsEVqe66aWFmbrar6t6ql2TdJ0rSIB9R5bTy7O3ITaTGUwYGVuMC2DIBi8W5EugsYJ7BDZqYtz7qJ-FOYh5bIJfZ5d2tUSk0Ii34dKzCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2-XtvhIT2dXg3T8ZDSzGpr5Ri1LlWIGbqlZMx6Cn2sakqEDVPHSB9gNTWZ3WXAxp4V3pxL_wtICfGGuNsj4ySCe-LkwmVAGdSJVBYJ1jHIPaTTRHYXqvkl4UkfGNn64HiOdaX6qLOO_9wEau3RFiGbPl5EkL2SlGD66n8ShP4OD3_F_bHvjKW-3ofeWvqsF78D2e3ODj_9BHjDSFM_8mZiSJ18ofYcwllOlt0oWGtNzkO0XJhmpfrfKvTom23fhwf9SZd77yYPUpS_Fdws3s65e8ZxJW98--1VXMQWNtFQATIqWP41rKrd3MTt-fYgncjyoiYs5Z_1JkQBXhYkGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
