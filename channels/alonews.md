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
<img src="https://cdn4.telesco.pe/file/ve7ykfdS7NvybeltI7lv4yjtc794Gsr494m_8mcid5ktJrWZWr0aj96C02HVY6Qo62M6hVF-X_6V6Ip9bgsYI-MFdFhm24gdWIBXfW_2Tdemfv8tFJyd_EBmjP2k75rHwuT-ygIh_ohMLUNg48CdmaJW7Qnj6IrJyG5lff_ExUXnBK9pIJDO2dJzNEcyPTxNNEBO11udQ0cZOYw0MytBuFk1gx8cAgDw59U37E4CjtZaSIc4ZqLtkhlrMK1tQqd0_XJRB_qI36yfcuS-7ye3-qX-Hq6robHowKky_uj9h0OBRW0O2R5f-I_uO8o2F4sYlPQkdY3hzR_aM-UWkOvW-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 987K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 07:15:18</div>
<hr>

<div class="tg-post" id="msg-139763">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏
👈
منابع عربی:
چندین پهپاد انتحاری به سمت شرق و شمال کویت شلیک شده است و سامانه های پدافندی درحال مقابله هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/139763" target="_blank">📅 02:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139762">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
روزنامه روسی ایزوستیا:
آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/139762" target="_blank">📅 02:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل:
کانال‌های دیپلماتیک ایران عملاً از کار افتاده‌اند.
🔴
به گفته درور بالازاده، تحلیلگر کانال ۱۴، مجتبی خامنه‌ای،  رسماً اعتماد خود را از تیم‌های مذاکره‌کننده ایرانی و آمریکایی سلب کرده است. دکترین تندروانه و بدون امتیاز احمد وحیدی، فرمانده سپاه پاسداران، اکنون سیاست رسمی آنها است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/139761" target="_blank">📅 02:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af4929d98.mp4?token=Rgh2ksn4wBl3RA-q6D_nK5o5HphhkROS7YirgHsIVKSXZv28V22xA8LF6uX7aLOmMR-dho55FPBRJ4evziPyQaWv-uCx3sxcgWrU0PVtpXlKI9MJB15iXEOtC7WyqAdHes-qFMSMaYJtrRXGbYkFdQ_UKTbaP-MCzN3jfcpqqSnYndOpG9QEqIJulDQE3V1nfzlrM415dlBDXjYH3iryI2cl4H7aN9AljS8P8Xt2M1ai8Ss0l8-jDB0dgZjquJtlIZN_4dCASrNmLjO7WQ_x3R-Q2B1C53HssErlOyVf6n3cNL2eDUZ8vR8n_NVfn41ba_j614zhnIbINyRbGJza1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af4929d98.mp4?token=Rgh2ksn4wBl3RA-q6D_nK5o5HphhkROS7YirgHsIVKSXZv28V22xA8LF6uX7aLOmMR-dho55FPBRJ4evziPyQaWv-uCx3sxcgWrU0PVtpXlKI9MJB15iXEOtC7WyqAdHes-qFMSMaYJtrRXGbYkFdQ_UKTbaP-MCzN3jfcpqqSnYndOpG9QEqIJulDQE3V1nfzlrM415dlBDXjYH3iryI2cl4H7aN9AljS8P8Xt2M1ai8Ss0l8-jDB0dgZjquJtlIZN_4dCASrNmLjO7WQ_x3R-Q2B1C53HssErlOyVf6n3cNL2eDUZ8vR8n_NVfn41ba_j614zhnIbINyRbGJza1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از یه درگیری تو ایران، انقدر وایرال شده که حتی رسانه‌های خارجی هم منتشرش کردن!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/139760" target="_blank">📅 02:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139758">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjK6kV0JxKMuf0LRM16Xuo2kicM5iut7d9JaijlGOfmS83-GJT6XqdQ_7aBy7wzBw8r4W7ZTdVzL3krW4Q0MdQrF3mnxZDjWoAuc6EfCR-BQ9GaD1E77Fb_sxUQxXY8XGWqhXWUAcPqNmEio52MFGN-fV4MsVSrR730SazrAtm-MuM1Iif2qPsl3E8zuWcM96GzooeX2rIt2UAn-ALnjzLNsyAT389p6tzG0FEmL8GtK2tlW0k5bWyeTSeB5IuU2evmeByQo-p49ynqiPUyolD6TxMpZkidgVqSob1szPx9fmazH92KPMAsvgpEi6g7YEGxgeVeZoq8VQobFrYoAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXOr1HRQKmxxWHXl356Y25NoWNZvCXuokHWxJ07VZUUrTprqux0OOmWnfsX-hogfxIyk5KdoWjemSBXZBHO6-7jX_8HAOw7aT6NMCmyC5p8mfqlV7El7tFUFck_v5jbaeSuMWt1K-rgIJpjlPdssEC8hKSn2x2labL-EEMGL-yQpFqMNBey51Xh-XayZVee3nPBUWid1A6yOf47p6sxbncU2JEAbDrddoa5bxNmWnX-vhbnFq7e2xlUge6NQ65h6a_w6w9Nz4wNQFVTMijKt6gTMcmpLjFXF-aHUtUruIGt0aZXVdXQzUzHA_TjSi_qLzhz2H9JxmeFLoqaG05RAwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صحبت‌های فیلد مارشال، دو کشور دشمن(روسیه و اوکراین) رو در خندیدن به یک موضوع واحد نزدیک کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/139758" target="_blank">📅 02:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139757">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzznuW1TwBJyFKH_V8aIjRC2sJGAZhBvI5NVdiyacX_NK_wwkiqHJCaBX6eqbb0eMBZYENaJKlGR_H66SeTrAALw8_jkk6QttoNnCANIYyin4i6PMGmUBizh-5Kd_A9kONZRj3dFJvacg99KrEyDUHtq0__u2tkDflDfaEVFkSMay_tyBtDAehcceF-_jJz1TaLgS_W2lj81fGbJt2682QMPaifokEwZQ7KXdfZqLH22cO4Z-oH9mQO8CZ0hL1rD1nh6KD79VR7D_4eF9FZJ2LOxMSiaQwZT4J45v2Qr-vJzh86AxjUHw2z21QESyntkvoJaRSIMFtjTtbpaIhdcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نسناس:
پزشکیان باید رسماً استعفا بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/139757" target="_blank">📅 01:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139756">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfOuMzk8-UqDJvFA_uHfcyStV-XtryxxQtOQuQpHflz2RZogXDy-oUpiv64OEj_usO9KCfKV3iawmJIUd81wEX7vSJljyogFBr6zyVTIFjET8nCkphIsHP3cY6zE3uT-tMc7Sm5gRxl_UCJeywhw_z0bpzNnoAg-4eDHqZtZf0BPjqc6f2CUZWD-kIReaqXCzDaR8AlkuhgO5jI68yQ5_J9gy1nVIzu9r96ok2Wq1DqEsxgpAR_EmMN9xxvmqa2cbAtsb1X7uxx2IYbPuw6YgKsu8DqlBKbVkwfnY_EkugupLalK5pOtOjogfD7E60uJF9lguJm_LDsbWzzC0JvqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اربیل عراق هم اکنون هدف حمله پهپادی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139756" target="_blank">📅 01:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139755">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نیویورک پست: مسیر ترامپ برای بازگشایی تنگه هرمز ممکن است از طریق عمان بگذرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/139755" target="_blank">📅 01:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139754">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
انفجار در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/139754" target="_blank">📅 01:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139753">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مدنی‌زاده وزیر اقتصاد: دشمن آرزوی زمین زدن اقتصاد ایران را به گور خواهد برد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139753" target="_blank">📅 01:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139752">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
تعداد کُشته‌های زلزله تو ونزوئلا به ۶۱۲۵ نفر افزایش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/139752" target="_blank">📅 01:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139751">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhNjHltKSGvN5iR_4ai9IMkCGG3GJvrM9qhelKWkRnC-_iNnw39jodUM3SMPIezLSXMCvTetmN95OaPp4hAaVvjw2tapfhBtjCLaDRlA91kx2UXb7OqCbLc_6pVAUPVWlB46Xp4agqaExY-Ua5W4Z161JAgKMEEE8fMBhdtjhLJ08XSPxyWrEiCZLs3r1wneJn8UHTS9o_B6YfvsysM9-n6WavpP7xhN5lGCoxhnISXoaewx8SiWi7cBWoeleq_jb1JWeZpjUxcXr1LS6Glg8nr641s-6Zy463KIpwU1pi-rP8kpEOWFMX-jYcYiP8O3wpVT8zO8NBJnW2a8xQb6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکایی‌ها درحال حاضر ۱۹۳ هواپیمای سوخت‌رسان را در خاورمیانه و اروپا مستقر کرده‌اند!
🔴
این هواپیماها تانکر سوخت‌رسان، شامل ۱۶۵ فروند از مدل KC-۱۳۵ و ۲۸ فروند از مدل KC-۴۶ پگاسوس هستند و در پایگاه‌های مختلف مستقر شده‌اند.
🔴
بیشترین حجم این تانکر ها در اسرائیل مستقر‌اند و تخمین ها حدود ۱۱۰ تا ۱۳۵ فروند را نشان می‌دهد، که در فرودگاه های مختلف اسرائیل مستقر‌ و به‌طور مداوم درحال انجام مأموریت و تمرینات هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/139751" target="_blank">📅 01:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139750">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=Z7x3cK7Y9fdiXNSEWG2XcZXNn4H-ofUrmyHWs63jU6RMi239BuqRAIHMjjnziwVn_H9bdBe-A_ZGgmxvo8dpln34o9OLOBokQmFqAZyJSIBuYWLNinBbJEDp-8BpWJwdc4f8KVHbyv9giJ8blQMxh-Rj6INpiGJ8bJBCzaMhIygIwW38D_DVfioJ_cdweH_Dipfw-LN7w6QOIpFzjWt_l7sHmCiNUku6rJ2ALCRRW9CIrpv2-9UsEHoXMqSs2Gx-EZSoZpSRNBIYEDSKrzttZctJVU7ai0PSfzA0BX5R5UxsfrLL1tVarA82XZkdJnfqdGYoHpjKr5rz7Opq2IQ0Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=Z7x3cK7Y9fdiXNSEWG2XcZXNn4H-ofUrmyHWs63jU6RMi239BuqRAIHMjjnziwVn_H9bdBe-A_ZGgmxvo8dpln34o9OLOBokQmFqAZyJSIBuYWLNinBbJEDp-8BpWJwdc4f8KVHbyv9giJ8blQMxh-Rj6INpiGJ8bJBCzaMhIygIwW38D_DVfioJ_cdweH_Dipfw-LN7w6QOIpFzjWt_l7sHmCiNUku6rJ2ALCRRW9CIrpv2-9UsEHoXMqSs2Gx-EZSoZpSRNBIYEDSKrzttZctJVU7ai0PSfzA0BX5R5UxsfrLL1tVarA82XZkdJnfqdGYoHpjKr5rz7Opq2IQ0Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز گروهی از مردم پاکستان، تجمع ضد جنگ برگزار کردن؛ اما وسط مراسم یهو یه عده، یک حمله انتحاری انجام دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/139750" target="_blank">📅 00:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139748">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pGJ1COZKLuM0UlRXi9IBYKy0geD_wQUgujG2gxqm9nrRdlUNn_yAQgWBpiAWqzb-KwmhYp17jm0KqW-Fe_6biso0yY_2ea54J4Sx6Rf8RmfDMavVRYEdbwNCQoBk3NDaSz2okqiUIYRFpwA9hfjUGuJ-O5m_BTVl7iHfWD4P40qur8uwuMOkdMdLmwm07udtSWrL712pffC_S51x5Jta62ZtVx2vIcGOPwHnhjv3WjAYsCLp65E0P-Edd8CSpKBvPSDeNXtmWvlrKWZpeP0ylZF7-sB1Glq6J6ujpgQsXG5dmYnVjzM-RXYJbwXpzdBhK_Vl5niZhceXD8CVryrNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WXbZ-Lupy6Lqb0Y8USPvLgc-iX40b2g5G0Pcp-0dASzAq-B9dCkEOYFR9Poa1Y2R5GCTENsSd5Hn4ajgUgadfCSXN8N1Oog0Xvxlqqh8rQ7rqklwOzAwqzNXQ-el4gvmqemmBkNysY9T4H4ulUixZmoWAE4XoCugNc9ygSdvdyEzj9cuaFo9GCS__U6zXVumHcHCSFcvn9WvA1N-DUcT8UwP019NOgPPhp6A7Jtz98XxrPrtWGyLiJ2luGkX_RsuPK5TVT0mKhBoZlt6h1ebXORUDM9anUiNC5TW0GEvRFru9jOvsmX-6NG5E_gE9pFqSAI9FBZV9MBKl0yQcnR5UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مهدی روشنی، فردی که این عکس را گرفته بود به اعدام محکوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/139748" target="_blank">📅 00:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139747">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgnDsUiTyK5c631SCpvtVFJPt8UjOZ36z12IUT8FRwnEBwVhMxWsDr53mzCtpaoBfP7_akBxUdVseHL7YY74j1N57sR0K-kAqjcgY9rEDCd5HvhigkHVfja53KmtBh8azbqoSjoQ5UROZu3TQhB8VmS4WWCRlZo1CLOTDBL_DlOjnR29Fth6UnA2omTxpfedTqsS9JN3xlRzX8myXnuhHsrGv8Sh9_QyaTW00jTGOsZxJMCDB8H_6YDWMSe5bhrAZU9P90q0lH_ZBhQ_rZUMoD1tkoPBmlGZzAUmfwi3Vc_vqYs-UarNPZjL6NXMtr22jsyF4ktGxVhplOmZ512yoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: این‌ها کودکان گمشده هستند و ما هیچ کمکی از سوی شهرهای پناهگاه  (Sanctuary Cities) دریافت نمی‌کنیم
آن‌ها حتی تمام تلاششان را می‌کنند تا این کودکان همچنان گمشده باقی بمانند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/139747" target="_blank">📅 00:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139746">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/139746" target="_blank">📅 00:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139745">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سازمان ملل: از تلاش‌ها برای توقف درگیرها میان ایران و آمریکا استقبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/139745" target="_blank">📅 00:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139744">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
بیانیه قطر، مصر و ترکیه: از جامعه بین‌المللی می‌خواهیم که اسرائیل را برای پایبندی به توافق آتش‌بس در نوار غزه تحت فشار قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/139744" target="_blank">📅 00:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139743">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
الجزیره: ایران تعیین می‌کند چه کشتی‌هایی وارد خلیج فارس یا خارج از آن شوند
🔴
تهران همچنان کشتی‌هایی را که بدون اجازه‌اش حرکت می‌کنند، هدف قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/139743" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139742">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
صمصامی، عضو کمیسیون اقتصادی: با ادامه روند فعلی تا دو ماه آینده موج جدیدی از تورم در راه است !
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/139742" target="_blank">📅 23:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139741">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
مرندی:ایران هیچ قصدی برای مذاکره با ترامپ ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/139741" target="_blank">📅 23:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139740">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/of4n9IKeJUYvPhrmGozXluRBFd7mZs0kulKoqlssgO4ZeQj_q1iSAFxxKAnOrDlzOfGgFS5dTSfItCi3tOSuZYnqnKDs8XPXH09EZYkwOu35BzbtkLfAtZrsGHYr4M4U1cvoKCOa1zbPXWuy-tPm5Fpfndfj2fnsjl9VOjlJg7fn40idKVTKerLKwfHfLE3LAMWNAHwd0mMk-zVk0jrdXXmRwA2SwApnu5h3bORAG2E52bbh6rjOtSmUuCRKsdp6P7u9V3t8RtuVpZqZToNZM5IMqtJDBkWfib4GUFpK1T8qoxfTw9z5GvJwKZD-XrBWZcwUMbIb5IUSYU-h89Q2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی: اگر محاصره ادامه یابد، کشتی‌ها و نیروهای آمریکایی با خطرات و تلفات جدی روبرو خواهند شد. ایالات متحده باید رفتار خود را تغییر دهد - در غیر این صورت ما این را تحمل نخواهیم کرد. ما هرگز اجازه افتتاح یک کریدور دوم در تنگه هرمز را نخواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/139740" target="_blank">📅 23:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139739">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
الحدث: سفر عراقچی به اسلام‌آباد در آینده نزدیک انجام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/139739" target="_blank">📅 23:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139738">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a02fc078e.mp4?token=jcny5qpKeuRHJMku8KSeWAAn8onBom5XYRM7SeGePyis4-vhP_VdCYiQ6dKC2CsljY5WlN-LuhsLd1Nq0YErmvxK3G8h5adtWXs_ce-wdkF-aot_PW42BBcz7O8_gnkF-O7fmtHLXAMJG7h1AgYZ-7qnTBGVU3Gnv03zjdZm_oV_ytCXco0PLMul1w5Nlkxe1yHuvlw_PtRRTWKJVOoR3r8Z8mgNe3z0J6ITPExYTke9QiXlsb3K-mtouo8I8_env4FoxGHbj6-c2GWMpelxzcWDimzyy30FZ-uMdsR9TsEfVbOt9SVn6effpvoBMISjW5h6ENfb1iWxKeilsFKH9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a02fc078e.mp4?token=jcny5qpKeuRHJMku8KSeWAAn8onBom5XYRM7SeGePyis4-vhP_VdCYiQ6dKC2CsljY5WlN-LuhsLd1Nq0YErmvxK3G8h5adtWXs_ce-wdkF-aot_PW42BBcz7O8_gnkF-O7fmtHLXAMJG7h1AgYZ-7qnTBGVU3Gnv03zjdZm_oV_ytCXco0PLMul1w5Nlkxe1yHuvlw_PtRRTWKJVOoR3r8Z8mgNe3z0J6ITPExYTke9QiXlsb3K-mtouo8I8_env4FoxGHbj6-c2GWMpelxzcWDimzyy30FZ-uMdsR9TsEfVbOt9SVn6effpvoBMISjW5h6ENfb1iWxKeilsFKH9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رابرت اف. کندی جونیور، وزیر بهداشت ایالات متحده: من واقعاً هر چیزی را می‌خورم!
🔴
من هیچ واکنشی از نظر تهوع ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/139738" target="_blank">📅 23:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139737">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0ce171f4.mp4?token=lBQbH7M9ikkAf2hegyWD7e0FNa_MNJ6HFygjIH1x64R6F1W1xDzrG2RN50k18f96yJQjus67I4ZHwQH3373HFz_t678LzaZG2gWtE_c5B05OOBM94so-vIVjnd3tONP_4s9jGGoj_-HQy3uhKaKFXCAuvVPSYVV3nbFIXWG5ISdPlQD499K0xtLsF_pjNPtt8-KT5rYrO9NNzCxBrEARnXf_WEe38RmIaUR4RciDC7To1loM2x0aazSxvAtEvG5GkCeSIX6-cdFj8geL0vs8NOR5Yb31NPHK-o18h-e04P0MT7j-Hxg6zPyfHgmSQx-xOUsRex_tJvgKbeb1cXKKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0ce171f4.mp4?token=lBQbH7M9ikkAf2hegyWD7e0FNa_MNJ6HFygjIH1x64R6F1W1xDzrG2RN50k18f96yJQjus67I4ZHwQH3373HFz_t678LzaZG2gWtE_c5B05OOBM94so-vIVjnd3tONP_4s9jGGoj_-HQy3uhKaKFXCAuvVPSYVV3nbFIXWG5ISdPlQD499K0xtLsF_pjNPtt8-KT5rYrO9NNzCxBrEARnXf_WEe38RmIaUR4RciDC7To1loM2x0aazSxvAtEvG5GkCeSIX6-cdFj8geL0vs8NOR5Yb31NPHK-o18h-e04P0MT7j-Hxg6zPyfHgmSQx-xOUsRex_tJvgKbeb1cXKKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدتی پیش، یک پهپاد متعلق به نیروهای دفاعی اسرائیل، یک خودرو را در نزدیکی ساحل در غرب شهر غزه هدف قرار داد.
🔴
بر اساس گزارش‌های محلی، دو نفر در این حادثه کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/139737" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139735">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزیر اقتصاد: دشمن آرزوی زمین زدن اقتصاد ایران را به گور خواهد برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/139735" target="_blank">📅 23:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139734">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
یک منبع بلندپایه ایرانی به المیادین: ایران هیچ مذاکره‌ای با ایالات متحده انجام نداده است
‏
🔴
ایالات متحده همواره نیرویی تخریب‌گر و برهم‌زننده امنیت بوده است و نمی‌تواند خود را نجات‌دهنده منطقه معرفی کند.
‏
🔴
باز یا بسته شدن تنگه هرمز به وضعیت کلی منطقه بستگی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/139734" target="_blank">📅 23:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139733">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
منابع سعودی ادعا می‌کنند: خوش‌بینی محتاطانه در مورد پیشرفت در مذاکرات ایران و آمریکا.
🔴
میانجیگران قبل از اعلام آتش‌بس به کمی زمان نیاز دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/139733" target="_blank">📅 23:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139732">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
کانال 12 اسرائیل:
بانک اطلاعات اسراییل برای حذف سران نظام در حال تکمیل شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/139732" target="_blank">📅 23:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139731">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAr5X0utk0pymCHCCfyf4w0XHg9lXYHwgXIGGbAdgyvVkQUjYqsQ6ZTEp5CkgPiwv7RAyFfD9qAC_3dflDKqDGmUjbdP8uhiId81rBKWRM2UKRTeOdAhxmITt2OLENXJwE1ZsVNxeojVhIXYoJ4KA2vQgkGXFxdEJ3WVYd4I6nWxCPh1XQFSfV7remXVW2Bfava-usZV_KbHXwXsYVMTZYCUUOw32HCGES1yIqVkhBcptZBC8bGhPn6B9AnaYhGUW26vOUXYIS91BdmIGuM0b5HDU5p5IWBKkYUf5MXnnYkINv15T1TVLl-h6t1BQFcVLpcmPu99Ex_EzIeAf3iPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدیری ابیانه چهره نزدیک به جلیلی:
جوون هامون باید باهم ازدواج کنن نیاز نیست حتما وسایل نو بخرید میتونید با خرید وسایل دست دوم و خونه ۲۰ متری زندگی کنید. قدیم زوج ها توی یه اتاق زندگی می‌کردن نیازی به ماشینم نیست چون قدیم ما ماشین نداشتیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/139731" target="_blank">📅 23:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139730">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
محسن رضایی خطاب به امت معکوس:
شرایط کنونی ما شرایط گذر به قدرت چهارم جهانی است
🔴
وحدت‌مان را حفظ کنیم و اختلافات بین نیروهای انقلاب را پایان دهید
🔴
نباید نقد را به سمت تخریب و اهانت بکشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/139730" target="_blank">📅 23:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139729">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFco3xu7sCiWzP4oA7hiKSifte77y3O6ay19oaz9LRwtK_S8b3ZUoYgWjlfonAryzd2FBhEyEshyDvEeOOZfyutGpQz0XHt8tr3TLRQlLZnyose7QGHEujo3xOoV0btqFs9HqmfIRouiGYGmyvhm4Vwki2tCWaavpqEsOP2Uwfs_acDzX6JveS_g6sxCrG1OF722WkqgOYx0Q9qnKpf3IhVbksXBv_qvRrSZxjBtaJ7zME6PvmxgT-AplJ77H5YgZZjqsNY4ruB0FEufODViF7FbgOo1Pq2jmetefHzZgheQajRwTy-tHToFure6SY4d_UafYBKMXiBqJ1emzb3zrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گاردین: عاصم منیر با ونس، ویتکاف و عراقچی در تماس مستمر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/139729" target="_blank">📅 23:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139728">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
منبع ایرانی به المیادین:
مذاکرات ما با همسایه ابدی مان، سلطان نشین عمان در حال انجام است، به ویژه اینکه تنگه هرمز منحصراً در آب های سرزمینی دو کشور قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/139728" target="_blank">📅 22:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139727">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏
👈
محسن رضایی: اگه آمریکا حتی یه ناو هواپیمابر هم به منطقه غیر قانونی تنگه هرمز بیاره میزنیمش
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139727" target="_blank">📅 22:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139726">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc81f02b2a.mp4?token=P12c7MUDLKB7GS9_wuufoPFPcMNOwTZ-iqvqqVygrLOAiLaeZbNpbGdBpmFbUzFco6ZlQ8OQzuhXneosnsxFjl0azp3kKit_TFzBXO_-JYQv9f_4RUgRjHPFscUfTWN2d72MF12ycwTN_5dGjMTTgyD5f84xQTKF6weLOoRXzuoUOX3EkgmWmvlCqInYTHFIdeHgPQi96jDKylHRh9I1d_y0_qNhM31zVw3hJfTOhnc29GZF_cgLEa9dChy4h4DoGQItqLzGQoj_VlLcxm4AMSEnTcYRapj0H_uYcxAUl1L1cU2HD5F1PwOkh5Y5WaHyyXDROHVQ2lVbrm-81PrVoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc81f02b2a.mp4?token=P12c7MUDLKB7GS9_wuufoPFPcMNOwTZ-iqvqqVygrLOAiLaeZbNpbGdBpmFbUzFco6ZlQ8OQzuhXneosnsxFjl0azp3kKit_TFzBXO_-JYQv9f_4RUgRjHPFscUfTWN2d72MF12ycwTN_5dGjMTTgyD5f84xQTKF6weLOoRXzuoUOX3EkgmWmvlCqInYTHFIdeHgPQi96jDKylHRh9I1d_y0_qNhM31zVw3hJfTOhnc29GZF_cgLEa9dChy4h4DoGQItqLzGQoj_VlLcxm4AMSEnTcYRapj0H_uYcxAUl1L1cU2HD5F1PwOkh5Y5WaHyyXDROHVQ2lVbrm-81PrVoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محسن رضایی: آمریکا در طراحی چهارم خود علیه ایران تلاش دارد از داخل شورش‌هایی انجام دهند
🔴
کشورهای دیگر را هم می‌خواهند وارد جنگ با ایران کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/139726" target="_blank">📅 22:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139725">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/ژنرال ۲ستاره محسن رضایی اتمام حجت کرد : اکنون آتش‌بسی وجود ندارد .
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/139725" target="_blank">📅 22:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139724">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ادمیرال محسن رضایی: «اجازه نخواهیم داد هیچ مسیری غیر از مسیر ایران در تنگه هرمز باز شود. حتی اگر آمریکا یک ناو هواپیمابر را به مسیر غیرقانونی تنگه هرمز بیاورد، آن را هدف قرار خواهیم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/139724" target="_blank">📅 22:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139723">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039faea8ea.mp4?token=AyYAvwybG0CuN2On0mvUuwfhTk9gkOdWckX4RySjRoP8uBmCqSi7aG2zjmE0FtuaVfwjc0TIQiEN7GAMXcM4slaSzSRnQpGX5CriKfahxgFq4r63TJwzBRBptnRtnUxdLdcpuKl1dh0DpjtH43uilN-YqKYCKLvPYVvuazCjXBIuaM4deUh-cWk3CxP-AK3L2qhQUhRsTjXUQq_jpeYpV4yFVYkm_e33R68UYEm4CoOwPErXgPSED6CrmYhQ8TZ849ypIqTSFHZ6Ff2UOHiSdph-lZFleTs0kkzD22ZaYI7AuJbe3Efw6aKZeI-IecDTthy37FZ4nw0BWxxbnKKQ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039faea8ea.mp4?token=AyYAvwybG0CuN2On0mvUuwfhTk9gkOdWckX4RySjRoP8uBmCqSi7aG2zjmE0FtuaVfwjc0TIQiEN7GAMXcM4slaSzSRnQpGX5CriKfahxgFq4r63TJwzBRBptnRtnUxdLdcpuKl1dh0DpjtH43uilN-YqKYCKLvPYVvuazCjXBIuaM4deUh-cWk3CxP-AK3L2qhQUhRsTjXUQq_jpeYpV4yFVYkm_e33R68UYEm4CoOwPErXgPSED6CrmYhQ8TZ849ypIqTSFHZ6Ff2UOHiSdph-lZFleTs0kkzD22ZaYI7AuJbe3Efw6aKZeI-IecDTthy37FZ4nw0BWxxbnKKQ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرلشکر مارشال رضایی: آماده بودیم به ۳ منطقه از اوکراین حمله کنیم اما بعد از اینکه گفتند اشتباهی حمله کردیم، پاسخ را متوقف کردیم تا ادعای آن‌ها را بررسی کن
یم
🔴
آن‌ها در هر صورت باید مابه‌ازای حمله‌شان را بپردازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/139723" target="_blank">📅 22:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139722">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d49d0f727.mp4?token=Oh1UORb8ofZhHHKr3OuYUQSoD9Mss7Ow5vzbNshtWdUnYTaJLBSBAUYY2z_IV64gfHpZI5eOhsvlUJSocX_DzThSTsCzHF_ST79bHFndd_pjBGJPeDeX3lytxDC8-Q5AvmYOPl-CeM4kd5k5vzjuH2erlqSwM8jbHZOa3sok3SM6ac0KR99mlS32LAJHR1q_BNZG12zM2JEksb64BZrujEMUU5d9ob9UnrsDDsKQiTkaLBt4lQoJmnchzBV27BLq4BKPZnMt0FrvJQf2rBhivZnqljxjDx6r04cnbL-40lu1pUJ5sRZ-muNGRxjd6mLNmoUbBi7WNGlWBgGlmNeLfxW-7fHoto6nFLKHxz0T7vK5SNFfCVMSGgyBfJyPazDCZC_v007cbG11ugvF8YHG8EP9IZJYYfmSc8IaYF-BqeCc0ZGB6yVzkV2N3pfmEhLO02Nt7T5_2Ji_tEkyb-wEFZPln1kweJt-0z5bOY6WSEyB3Ak6MRRZU0kp8HARSJUv_Ps__a87kY6mF37vrlXcNAmvewjePLQ8aor9Gcsv5w2_MHxwZAKsL1bUqlBiXP8VKqiavBxqtmqtuRKFf8ytC2OGfAYRnvONy5TsuhoVAEX5u7eI_u0NQtfq7UynGM1hIT-yLXy2L9gsga1nOtVAwrgwc2-YPtsJPLQ9JsZsrrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d49d0f727.mp4?token=Oh1UORb8ofZhHHKr3OuYUQSoD9Mss7Ow5vzbNshtWdUnYTaJLBSBAUYY2z_IV64gfHpZI5eOhsvlUJSocX_DzThSTsCzHF_ST79bHFndd_pjBGJPeDeX3lytxDC8-Q5AvmYOPl-CeM4kd5k5vzjuH2erlqSwM8jbHZOa3sok3SM6ac0KR99mlS32LAJHR1q_BNZG12zM2JEksb64BZrujEMUU5d9ob9UnrsDDsKQiTkaLBt4lQoJmnchzBV27BLq4BKPZnMt0FrvJQf2rBhivZnqljxjDx6r04cnbL-40lu1pUJ5sRZ-muNGRxjd6mLNmoUbBi7WNGlWBgGlmNeLfxW-7fHoto6nFLKHxz0T7vK5SNFfCVMSGgyBfJyPazDCZC_v007cbG11ugvF8YHG8EP9IZJYYfmSc8IaYF-BqeCc0ZGB6yVzkV2N3pfmEhLO02Nt7T5_2Ji_tEkyb-wEFZPln1kweJt-0z5bOY6WSEyB3Ak6MRRZU0kp8HARSJUv_Ps__a87kY6mF37vrlXcNAmvewjePLQ8aor9Gcsv5w2_MHxwZAKsL1bUqlBiXP8VKqiavBxqtmqtuRKFf8ytC2OGfAYRnvONy5TsuhoVAEX5u7eI_u0NQtfq7UynGM1hIT-yLXy2L9gsga1nOtVAwrgwc2-YPtsJPLQ9JsZsrrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: با حملات ایران کویت به یک خرابه تبدیل شد
🔴
در اربیل بیش از پنجاه هواپیمای پهن پیکر نیروهای آمریکایی را تخلیه کرد
🔴
فرماندهی سنتکام از قطر، اول رفت اردن و بعد هم رفت اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/139722" target="_blank">📅 22:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139721">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06551d5d7.mp4?token=aKV7jFv3vxvA3EJRy-uK1dd08EyLeCmuyyJJEldcuV_c5za_ePmC6LhG6mL1uq0J5kDNmQ3gi1u2A0cb4Y3_DjOxldkwC-UAhmRw8eWChgcC4sPxXI-wLz5A6IaGfedl7N_lBZwbi_LTe5WrirdEyAC0xChOE-lJ65vBIzZQ--GRQDcEV-JoFxMSZb15rDsYb2sOZh1TMfwF1gWGO_sICt1BStV36I1uXF4N0wMmrQNinI2CUpboBkoZSYiHMUhO4Xpr7NLASxYsDuN1KTIdhssiusLNZAb9zlE9lKkIXIAfVpD-6QkzyIDgSoyFuVYMFjy2lLPClJ59Eo0mSCH_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06551d5d7.mp4?token=aKV7jFv3vxvA3EJRy-uK1dd08EyLeCmuyyJJEldcuV_c5za_ePmC6LhG6mL1uq0J5kDNmQ3gi1u2A0cb4Y3_DjOxldkwC-UAhmRw8eWChgcC4sPxXI-wLz5A6IaGfedl7N_lBZwbi_LTe5WrirdEyAC0xChOE-lJ65vBIzZQ--GRQDcEV-JoFxMSZb15rDsYb2sOZh1TMfwF1gWGO_sICt1BStV36I1uXF4N0wMmrQNinI2CUpboBkoZSYiHMUhO4Xpr7NLASxYsDuN1KTIdhssiusLNZAb9zlE9lKkIXIAfVpD-6QkzyIDgSoyFuVYMFjy2lLPClJ59Eo0mSCH_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زن بیژن مرتضوی مصاحبه کرده و تا تونسته مالیده
اولش گفت رضا پهلوی مقصره که به مردم گفت برن خیابون، و بعدش گفت کشتار دی ماه کار جاسوسای موساد بوده، آخرشم گفت کسایی که کشته شدن بخاطر بالا پایین شدن هورموناشون رفته بودن خیابون.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/139721" target="_blank">📅 22:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139720">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: آمریکا برای بازکردن تنگه هرمز بنا داشت حمله زمینی انجام دهد
🔴
حملات به جنوب کشور با هدف حمله زمینی آمریکا به کشور انجام می‌شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139720" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139719">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139719" target="_blank">📅 22:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139718">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/139718" target="_blank">📅 22:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139717">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ خواستار زندانی شدن عاملان افشای طرح حمله به ایران شد
🔴
دونالد ترامپ با «فاسد» خواندن کسانی که دست به افشای جزئیات طرح او برای حمله به ایران زده‌اند، تأکید کرد این افراد باید زندانی شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/139717" target="_blank">📅 22:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139716">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ:
آنها به پای ما افتادند و گفتند توروخدا حمله نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/139716" target="_blank">📅 22:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139715">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: فعلا سر جمهوری اسلامی رو قطع نمیکنم و فرصت میدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/139715" target="_blank">📅 22:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139714">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edad057e3.mp4?token=PHS43P1CUOLHvH-eX9P8w5EEjUzpHQkvBw7MTrXCjbq-yX6HYDsC-utxHpr_C6rIh_vLAyhffOiVPNZzK9F_LARc96nOAc56Z3XjTcJ7g9Scm3UUeEEdL_1AYQdXLmhazYe0FekddfBhQSU0L7bTZ82JmO75Q_DEMlgtlYR3U913sliF5cIxAFQVEZPA7fULZiWmVZJBUYg9yiN_Nu7-HsnwbtdfIQbJpIubndYBh94Eh8fJk7ERBfynVbPeQSgviKOuHKybUBV4palc_CZfAUd5RIwqXmnCKSYJK4o8GSR1d1L6XbE_wdjBNGGPL36T6w9-22uiDufTSYXvpBJnZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edad057e3.mp4?token=PHS43P1CUOLHvH-eX9P8w5EEjUzpHQkvBw7MTrXCjbq-yX6HYDsC-utxHpr_C6rIh_vLAyhffOiVPNZzK9F_LARc96nOAc56Z3XjTcJ7g9Scm3UUeEEdL_1AYQdXLmhazYe0FekddfBhQSU0L7bTZ82JmO75Q_DEMlgtlYR3U913sliF5cIxAFQVEZPA7fULZiWmVZJBUYg9yiN_Nu7-HsnwbtdfIQbJpIubndYBh94Eh8fJk7ERBfynVbPeQSgviKOuHKybUBV4palc_CZfAUd5RIwqXmnCKSYJK4o8GSR1d1L6XbE_wdjBNGGPL36T6w9-22uiDufTSYXvpBJnZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران تماس می‌گیرد و خواستار توافق می‌شود
🔴
دونالد ترامپ درباره ایران مدعی شد: «آن‌ها با من تماس می‌گیرند و می‌گویند: "لطفاً حمله نکنید، ما توافق خواهیم کرد."»
🔴
ترامپ افزود: «این حقیقت ماجراست و همه آن را می‌دانند.»
🔴
او در پایان گفت: «چه کسی در چنین شرایطی تماس نمی‌گرفت؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/139714" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139713">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ: پیش از اقدام قاطع، آخرین فرصت را به ایران می‌دهم
🔴
دونالد ترامپ درباره ایران گفت: «می‌خواهم پیش از اقدام قاطع، آخرین فرصت را به ایران بدهم.»
🔴
او افزود: «امیدوارم آن‌ها به خودشان بیایند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/139713" target="_blank">📅 22:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139712">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / یک کشتی باری ترکیه‌ای که به سمت روسیه در حرکت بود، در دریای سیاه مورد حمله یک پهپاد انتحاری قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/139712" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139711">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: من اروپا را بهتر از هر کسی می‌شناسم؛ حتی بهتر از کسانی که آن را اداره می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139711" target="_blank">📅 21:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139710">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: شرکت‌های نفتی سود بیش از حد به دست می‌آورند؛ باید بخشی از آن را به مردم بازگردانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/139710" target="_blank">📅 21:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139709">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: چمن مثل انسان‌هاست. آن هم زندگی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/139709" target="_blank">📅 21:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139708">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: در موضوع مهاجرت، اروپا با بحرانی جدی روبه‌رو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/139708" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139707">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ: آنها فردا اعلام خواهند کرد که تنگه هرمز باز است
🔴
ترامپ: تنگه هرمز به طور کامل در دست ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/139707" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139706">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: بریتانیا با بهره‌برداری از نفت دریای شمال می‌تواند دوباره ثروتمند شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/139706" target="_blank">📅 21:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139705">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ : من اروپا رو بهتر از هر کسی می‌شناسم؛ حتی بهتر از کسایی که خودشون دارن اداره‌ش می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/139705" target="_blank">📅 21:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139704">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ درباره عوارض‌ عبوری از تنگه هرمز: نمی‌گذارم ایران عوارض بگیرد. اگر قرار باشد کسی عوارض بگیرد، این ما هستیم که می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/139704" target="_blank">📅 21:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139703">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: ما دیروز میخواستیم بزرگترین عملیات تاریخ پس از جنگ جهانی دوم را آغاز کنیم ولی منصرفمان کردند، ما در حال حاضر، بنا به درخواست ایران، و با حمایت عربستان سعودی، امارات متحده عربی، قطر و بسیاری دیگر، در حال گفتگو هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/139703" target="_blank">📅 21:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139702">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fbe9e8fc4.mp4?token=SiN55L8Cj0EUSYjdrHkoBPmboHjs43sCRTZ8_vytS4AqJS9A0DOfQrEE6BbLTSqFgxOD-jc8XIsplzXPHFPepWLpVOlvJWU7AKM4hbs2pnctEC4nqrynPT-di7afrvRXlEdQAKKPX-2FNLd7TBdX4qzUL0uJh652x2RWRGj8_Vz4U_ZJ8KZOqoFV2qHBmkjl7w7OBIPTWmCrGjDnqh2dB1GhQiNkP1tLPxO1JXjs-by8WiemEfN3Z0wIF9heOGljF0KELbsdyfFS4dI5GTv3nCgWr0gVviIPaEtFKHXjbmsUjToeOfMQHf3RfBJ7Knsi7mn04-S0Z_G-EmP3V1CXoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fbe9e8fc4.mp4?token=SiN55L8Cj0EUSYjdrHkoBPmboHjs43sCRTZ8_vytS4AqJS9A0DOfQrEE6BbLTSqFgxOD-jc8XIsplzXPHFPepWLpVOlvJWU7AKM4hbs2pnctEC4nqrynPT-di7afrvRXlEdQAKKPX-2FNLd7TBdX4qzUL0uJh652x2RWRGj8_Vz4U_ZJ8KZOqoFV2qHBmkjl7w7OBIPTWmCrGjDnqh2dB1GhQiNkP1tLPxO1JXjs-by8WiemEfN3Z0wIF9heOGljF0KELbsdyfFS4dI5GTv3nCgWr0gVviIPaEtFKHXjbmsUjToeOfMQHf3RfBJ7Knsi7mn04-S0Z_G-EmP3V1CXoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمجید ترامپ از هگست
🔴
دونالد ترامپ خطاب به پیت هگست گفت: «کارت را فوق‌العاده انجام می‌دهی.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/139702" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139701">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3282f58089.mp4?token=RaW861BlERsiTnmQqXkxC_jbfqg6sXFVJWVAohjOoZHcU0Btkx72Ts_vCde737CuY1ilg8-FYK098uyi8ejofpXNXDLuayWqzWTCi30aIaj0UGlS1VlazivmIAI7_yVqXzJcBr-NjrjHUjNUi_7RQM6-XovLVmy8uDCghC30Ctiq-3s1zTjQcRuBC0gwV4drsAIL9_SOnVIfxKVUZpe4v8PuZJtsU9tvy65bk6TTaeeLc18Z_qZvCY_xuBfRMwEMmiDrqeP52oNtjItFIGpp_DZC7kxb9IW57ek-KnJQB75inV_bJ0_eRTuQtfKSxxuLLT6pMxkwZEmqyUbR9TRQUwBBUU9jE5aMlBUPv-BLZ05c8cn0T651u-xNwqj80u-Y3OaSXIbD0CZsNGMmpP6TfVQdqnBAH65VweAeB46RrM0T7wb7VhddTcDo2IIyZFGVskRR0-p3ObKThffsmUpnch1K3pGbsj6GIt0AgoRrpAd4RZGufQIQ29vd7upuTatTFl8WMJAmYMzNLFY7vgXuFLKmcB_kki9ew_TvVrSxRs5z_tqXqMyKrqc2cJo39ei17T5htYFdThJzuvXDrnV_NRQgHGo-XSqOcGs-uSLxG_xmFdw513yl7hMkOckOM3rVt5YB9O8XQlnkIIMomqFUOyoM1jHnVlf3ubz_zZtNcGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3282f58089.mp4?token=RaW861BlERsiTnmQqXkxC_jbfqg6sXFVJWVAohjOoZHcU0Btkx72Ts_vCde737CuY1ilg8-FYK098uyi8ejofpXNXDLuayWqzWTCi30aIaj0UGlS1VlazivmIAI7_yVqXzJcBr-NjrjHUjNUi_7RQM6-XovLVmy8uDCghC30Ctiq-3s1zTjQcRuBC0gwV4drsAIL9_SOnVIfxKVUZpe4v8PuZJtsU9tvy65bk6TTaeeLc18Z_qZvCY_xuBfRMwEMmiDrqeP52oNtjItFIGpp_DZC7kxb9IW57ek-KnJQB75inV_bJ0_eRTuQtfKSxxuLLT6pMxkwZEmqyUbR9TRQUwBBUU9jE5aMlBUPv-BLZ05c8cn0T651u-xNwqj80u-Y3OaSXIbD0CZsNGMmpP6TfVQdqnBAH65VweAeB46RrM0T7wb7VhddTcDo2IIyZFGVskRR0-p3ObKThffsmUpnch1K3pGbsj6GIt0AgoRrpAd4RZGufQIQ29vd7upuTatTFl8WMJAmYMzNLFY7vgXuFLKmcB_kki9ew_TvVrSxRs5z_tqXqMyKrqc2cJo39ei17T5htYFdThJzuvXDrnV_NRQgHGo-XSqOcGs-uSLxG_xmFdw513yl7hMkOckOM3rVt5YB9O8XQlnkIIMomqFUOyoM1jHnVlf3ubz_zZtNcGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد ایران:
مذاکرات در حال حاضر در جریان است. این یک اتفاق شگفت‌انگیز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/139701" target="_blank">📅 21:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139700">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری/ترامپ: امروز یا فردا متوجه خواهید شدند که مذاکرات در چه وضعیتی قرار دارند.
🔴
قرار است فردا تنگه هرمز را به طور کامل باز کنیم.
🔴
سپس درباره ظرفیت هسته‌ای ایران صحبت خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/139700" target="_blank">📅 21:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139699">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ برای بار هزارم: ما دیروز قرار بود آن‌ها را به شدت مورد ضرب و شتم قرار بدیم. با قدرت بسیار زیاد. قوی‌تر از هر حمله‌ای از زمان جنگ جهانی دوم، اما به درخواست ایران و ضمانت کشور های عربی این حمله را انجام ندادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139699" target="_blank">📅 21:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139698">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
خبرنگار: مذاکرات با ایران الان منتفی شده است
🔴
ترامپ: همین الان در جریان است. این موضوع شگفت‌انگیزی است.
🔴
آنها این بار آن را تکذیب نمی‌کنند.
🔴
اما به دلایلی، وقتی در حال مذاکره هستند، دوست ندارند بگویند که در حال مذاکره هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/139698" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139697">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ : با ونزوئلا اختلافاتی داشتیم که به‌خوبی حلش کردیم
🔴
با ایران هم اختلافاتی داریم و روندش به نفع ما پیش میره؛ اوضاع خیلی خوبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/139697" target="_blank">📅 21:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139696">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزارت امور خارجه:
در حال حاضر، هیچ آتش‌بسی بین ایران و ایالات متحده وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/139696" target="_blank">📅 21:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: نتانیاهو با حضور وزیر جنگ و رئیس ستاد ارتش، یک نشست امنیتی برگزار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/139694" target="_blank">📅 21:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139693">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
زلنسکی، سفیر اوکراین در آمریکا را برکنار کرد
🔴
طبق گزارش روزنامه آنلاین کی‌یف ایندیپندنت، این اقدام در بحبوحه تغییرات اساسی در دولت اوکراین انجام شده و انتظار می‌رود چرخش گسترده‌تری برای سفرای اوکراین صورت گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/139693" target="_blank">📅 21:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139692">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وزیر خارجه پاکستان در تماس تلفنی با وزیر خارجه ایران و رایزنی پیرامون آخرین تحولات منطقه‌ای، از سید عباس عراقچی برای سفر به اسلام‌آباد دعوت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/139692" target="_blank">📅 21:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139691">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: ترامپ دوباره در حال تلاش برای یافتن یک راه‌حل دیپلماتیک برای جلوگیری از تشدید تنش نظامی است. اما هیچ مسیر مشخصی، چه از نظر دیپلماتیک و چه از نظر نظامی، برای رساندن ترامپ به جایی که بتواند اعلام پیروزی کند، وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/139691" target="_blank">📅 20:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139690">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رویترز: رهبران ایران معتقدند تهدید های نظامی پرزیدنت ترامپ صرفا برای تقویت جایگاه او در مذاکرات است، نه به قصد گسترش جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139690" target="_blank">📅 20:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139689">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فرمانده نیروی زمینی سپاه:  درصورت هرگونه خطای گروهک‌های تروریستی این سرزمین را به گورستان عناصر مزدور بدل می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/139689" target="_blank">📅 20:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139687">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d504354916.mp4?token=OPO8KTLdyqtShpzQVy8mYRHMsyIvbOGDKbKQvajfjnAb3moVWg17WLvoTm9RlOUQRkEblN3ab-uzhe5Q3ShNoRxdZRdjqHTrtOCJCPSDUYU8FtGq7RaEMYVQS63DcoAm9RMmvRkkCkWgIpI20Y1_hZrrNIyzIome1_4Xj_vtNHhzYbMs0oWfTs7RqLoLFEIz8JNRMsQD0JQLiqR9w-pttGvvo3gHyyyACJ66DLBkNgOvw3CHzdoGgW1mZXCciSPOVEtKpmj50XdLkrfNZn79od6bzMhkwJWMcp-uxt8948BkMFVRzhvqMnL7iUzD2IFy_iyVCh6Mv7QZb51JXNwxtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d504354916.mp4?token=OPO8KTLdyqtShpzQVy8mYRHMsyIvbOGDKbKQvajfjnAb3moVWg17WLvoTm9RlOUQRkEblN3ab-uzhe5Q3ShNoRxdZRdjqHTrtOCJCPSDUYU8FtGq7RaEMYVQS63DcoAm9RMmvRkkCkWgIpI20Y1_hZrrNIyzIome1_4Xj_vtNHhzYbMs0oWfTs7RqLoLFEIz8JNRMsQD0JQLiqR9w-pttGvvo3gHyyyACJ66DLBkNgOvw3CHzdoGgW1mZXCciSPOVEtKpmj50XdLkrfNZn79od6bzMhkwJWMcp-uxt8948BkMFVRzhvqMnL7iUzD2IFy_iyVCh6Mv7QZb51JXNwxtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده F-16I سفا نیروی هوایی اسرائیل در حال رها کردن فلر (شراره منحرف کننده موشک) بر فراز جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/139687" target="_blank">📅 20:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139686">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJIivVg_C-Jd2XzavI6gQVS81J6o0gbu9Dq0NxjFZT4e3MQZ2XnzAv823RjA7dG39iy04lZW1wXMNWRv4i1XqJW_9CM4cz5pEV7C2YacGB1PabDaLSco1SgI0VvyaoqW0ueO7QzBScpY48XkyD9MRrqwayDnB7v4yuI7wJ_Bbhe3rqVmAaawHVPXWJU1Qb7aXtouRs4UNkIiED1ElClAZAJsf-5gfqtHJzmY_wVg5c6Mo2-qonZpdJcKLHGHs4uRKbn0q7oVWW8J_8GBVTdAYlPjzA88oYB6jjBWexjMN2g_nNggUtN88Jp1I-9iCllrWojDdSY0h_kiEg-b95bYJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/139686" target="_blank">📅 20:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139685">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
شبکه CBS : یک مقام آمریکایی اعلام کرد علی رغم ادعاهای ترامپ هیچگونه برنامه ریزی برای مذاکره با مقامات ایرانی وجود نداره
🔴
تماس ها صرفا از طریق واسطه ها جریان داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/139685" target="_blank">📅 20:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139684">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام): به اعمال شدید محاصره دریایی علیه ایران ادامه می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/139684" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139683">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc718d54a.mp4?token=VKmwM1cgEy9tn8I6LnFq_xz3F8pK6ba4il-X33FeQLorGxKAUdSWhB5hi4QPqwSiWyiUAFEHsI7zg3OQ4xZAPQZMXFCm-acuRIWfvYZWFQSREIX5YI_6EnMZ9woEXqXTSsp2VSwiuj8MBkWnfsrdtuiP2FYenkCuf_Pv-6GaTckDviDAtfTQdp8i9fMxOOb_Q1gbTCs1rgWB1ZrsLHbkj5sAJuEenOj24PwfSIuO4bXMl7Xx1NX82RmRpb6NcRgCotkfCz_pOshhotFYY_zb9-17rbQKNjd66sc1ePqrD9AtKe8ifVnkJfcbPaJ5rFu15dr1LduGW9-eNEBo7FK43Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc718d54a.mp4?token=VKmwM1cgEy9tn8I6LnFq_xz3F8pK6ba4il-X33FeQLorGxKAUdSWhB5hi4QPqwSiWyiUAFEHsI7zg3OQ4xZAPQZMXFCm-acuRIWfvYZWFQSREIX5YI_6EnMZ9woEXqXTSsp2VSwiuj8MBkWnfsrdtuiP2FYenkCuf_Pv-6GaTckDviDAtfTQdp8i9fMxOOb_Q1gbTCs1rgWB1ZrsLHbkj5sAJuEenOj24PwfSIuO4bXMl7Xx1NX82RmRpb6NcRgCotkfCz_pOshhotFYY_zb9-17rbQKNjd66sc1ePqrD9AtKe8ifVnkJfcbPaJ5rFu15dr1LduGW9-eNEBo7FK43Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام : ۴۴ کشتی تجاری رو تغییر مسیر دادیم
🔴
۲ کشتی رو از کار انداختیم
🔴
۲ کشتی رو برای بررسی و اطمینان از رعایت قوانین، سوار شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/139683" target="_blank">📅 20:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139682">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فارس: عاقبت مذاکره با آمریکای ترامپ بن‌بست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/139682" target="_blank">📅 20:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139681">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ae581f7d.mp4?token=m9zBWtMKByyoIJJortPmzoTbYce07T9ixbwmVGgQ-jNv86O4ClgKp4AZ3cPJs-lw3LU3zIeOF9l0gIjcMLhgfQjkJxtMNGtVl3CGjZD7yCxzIreZ1VdV8WyCHYBgN3GKAeFL4kh6vv4-f0NNAWEfUKU_iY8BojNtuzXXwE3h_VJp9wsIWfje3TDKpx-eoRvqbdtHUAMn8sACEK_kBWJzg-YvLGhpAE0jytBqgJkWaBBJlqpxh_xfPckGqf7ZOljc49Bn-QIcVvm64ncCTnw-xTZuNKthA-sGBF2_nI6Vp2RTuMiZyImYAVsPS6cTJarmGt54zD_f1K0WHCwocUml0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ae581f7d.mp4?token=m9zBWtMKByyoIJJortPmzoTbYce07T9ixbwmVGgQ-jNv86O4ClgKp4AZ3cPJs-lw3LU3zIeOF9l0gIjcMLhgfQjkJxtMNGtVl3CGjZD7yCxzIreZ1VdV8WyCHYBgN3GKAeFL4kh6vv4-f0NNAWEfUKU_iY8BojNtuzXXwE3h_VJp9wsIWfje3TDKpx-eoRvqbdtHUAMn8sACEK_kBWJzg-YvLGhpAE0jytBqgJkWaBBJlqpxh_xfPckGqf7ZOljc49Bn-QIcVvm64ncCTnw-xTZuNKthA-sGBF2_nI6Vp2RTuMiZyImYAVsPS6cTJarmGt54zD_f1K0WHCwocUml0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ف-۱۶ اوکراین یک پهپاد انتحاری روسی «گران-۲» رو با توپ خودش سرنگون کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/139681" target="_blank">📅 20:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139680">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
اسرائیل برنامه صلح غزه را رد کرده و همچنان به حملاتش علیه غزه ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/139680" target="_blank">📅 20:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139679">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17c460e34.mp4?token=IVqPNUSdAQ8UnPD_Od8OepRq5E0WuT1-puiVh271iNfJIEIN3fq_tdA1yxN8QSFLZj8qG9B2NYli2Kepy-9O4czlQb2pTN94qetifxR8r_XgPAcMeEDV3Ef65Dj_8G29MCtifiea7mI0EF49dH26EYXkqESTuBEIQMVfJTxc8ZtwLdi3fhGfIWDh_C9RpCBVjtBH2RcYcBD6S3SvfkhcJ0-eNxT1os_10MgD8fwdRUUsTBXFe78BLZu4ZuTXg2kMUcbLHUllWcxVTsAW3e6RwRxHxoZtXGjDX4LtVxYLxKK1u7ZOeKoq0bDJFnVC6Uun9H1HKk0nl9Fp_kypSD4Uvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17c460e34.mp4?token=IVqPNUSdAQ8UnPD_Od8OepRq5E0WuT1-puiVh271iNfJIEIN3fq_tdA1yxN8QSFLZj8qG9B2NYli2Kepy-9O4czlQb2pTN94qetifxR8r_XgPAcMeEDV3Ef65Dj_8G29MCtifiea7mI0EF49dH26EYXkqESTuBEIQMVfJTxc8ZtwLdi3fhGfIWDh_C9RpCBVjtBH2RcYcBD6S3SvfkhcJ0-eNxT1os_10MgD8fwdRUUsTBXFe78BLZu4ZuTXg2kMUcbLHUllWcxVTsAW3e6RwRxHxoZtXGjDX4LtVxYLxKK1u7ZOeKoq0bDJFnVC6Uun9H1HKk0nl9Fp_kypSD4Uvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل، بن گویر:
من از وزیر اسموتریچ به خاطر پس گرفتن حمایت خود از طرح ورود شورای صلح به غزه در کابینه تقدیر می‌کنم.
🔴
به نظر من امروز همه درک می‌کنند که نمی‌توان برای انجام کارهایمان به هیچ طرف بین‌المللی تکیه کرد.
🔴
این توافق نباید به عجله تصویب شود. این توافق باید به کنگره ارجاع داده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139679" target="_blank">📅 19:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139678">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: ایران هرگز سلاح هسته‌ای نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/139678" target="_blank">📅 19:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139677">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
👈
سید محمدباقر خرازی: رهبری گفتند اگر آقای پزشکیان یک بار دیگر استعفا کند، استعفایش را می‌پذیرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/139677" target="_blank">📅 19:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139676">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
رویترز: ذخایر نفت در آمریکا به پایین‌ترین سطح از سال ۱۹۸۳ رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/139676" target="_blank">📅 19:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139675">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ: ایران درخواست مذاکره می‌کند و سپس ادعاهای همیشگی خود مبنی بر کنترل اجباری تنگه هرمز را تکرار می‌کند
🔴
ترامپ رئیس‌جمهور آمریکا مدعی شد که رهبران ایران به طرز باورنکردی فریبکار هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139675" target="_blank">📅 19:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139674">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVy9vqrepPYnREBAn7d4OFmDlasCHPQk6Q2FYjlPwUR2Hv8-pshlHXQAF7XksDwwFklORVxLVIqcdi3DNV68HdWXj1y52Yb9fghf6JfY1W9J8JJf5X1DpZ-DG6twxXkZ6_QlbShnM-wpI932FB0oAyzSfktXaOGqDOlUFD3z6airWZoKv4rv-KOsqR6x6KXdDacFAW_MIWIo_T_jthMZgRgjZkjlIG2jeXIQQqeM5WP2I0EleEOBu2N3RpRvpfG14_tXe0JK8UJZnysiv1DNHqxcyd1tHkALD9wu4fep4KOhQaqXdgIMVx1l4Z7KlSVjRSSV-kGamLIBfc230qD9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: یا مرگ یا سرزمین مادری
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/139674" target="_blank">📅 19:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139673">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ: هیچ چیز به ایران نمی‌رسد مگر اینکه یک توافق حاصل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/139673" target="_blank">📅 19:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139672">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
العربيه: پاکستان به گزارش‌ها میزبان وزیر امور خارجه عباس عراقچی خواهد بود تا در مورد مذاکرات احتمالی با ایالات متحده گفتگو کند، پس از اینکه مقامات پاکستانی اعلام کردند که هنوز هیچ جلسه‌ای برنامه‌ریزی نشده است.
✅
@AloNewa</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139672" target="_blank">📅 19:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139671">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
العربيه: پاکستان به گزارش‌ها میزبان وزیر امور خارجه عباس عراقچی خواهد بود تا در مورد مذاکرات احتمالی با ایالات متحده گفتگو کند، پس از اینکه مقامات پاکستانی اعلام کردند که هنوز هیچ جلسه‌ای برنامه‌ریزی نشده است.
✅
@AloNewa</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/139671" target="_blank">📅 19:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139670">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqBMffw9NsGN5JtPxXaZxi2YVgZrVXhBghCAgKEbJIkfSNu2OMcxxulrvLrHmnifWEjCO4lIr5PdCIMeMw8R-bFej8sUkx1Hy0M5GM7Bc0n4E_2kbrKOX-5eWqC1QeGgi4iUcIUKZeyD4kjoiL37BYvU4AEuU4iuQD0FzWQB2lf6ezhTT3Wb_n_8-7J8pGuz9bzg0dRMfu3EaSxIh_S6yEZuKmE-taXMfKKNB-grBzdEzV-2srPle7m00AhJVIdpcnHh9LnWLo8txcX_zL1pF6Cm2xhukBlwT1C4rESoBZeWWGqS9rg0ODNaxqceLVfixiATaCEX0Y_AgjGIdLD95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای نظارتی E-3G Sentry متعلق به نیروی هوایی ایالات متحده در حال پرواز در نزدیکی تنگه هرمز بود و احتمالاً علاوه بر ردیابی کشتی‌های تجاری و کشتی‌های متعلق به نیروی دریایی سپاه پاسداران انقلاب اسلامی، به دنبال پرتاب احتمالی موشک‌های کروز ضدکشویی توسط نیروی دریایی سپاه پاسداران بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/139670" target="_blank">📅 19:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139669">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXQtQW9JF55Pq2ZZYzOeTeTIityFN1xDzqkNPaBjuhsmCbEy1sOqp-OEysv6QNo5AUp0A12b-naEcNcLinlnvj7NDEpD-skO7UFiLk9vski6Of7HazPfSckSfR6tHxi3YUNXYji6vRpj2xHKuHZM75I_1F_mohBNk549prpMWSR3xxzAsndX58XmV7W9gLk13x2bADSHx3w5U-tFaallko1EUTjPDt_jxWR_6xfDk7D9ry-z4NWtIg3w-AiEIQCJvb9rDNp3Fecl54R-2FLYoEgMwID9mdS41FHGMUzvjnfGWn8s_0yLKK33Kq2cY4keqKG-hIOsEFEmjXOXs_SU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیدینگ ریپورت : دانشمندا اعلام کردن تنها راه نجات کره زمین اینه که جمعیتش از ۸ میلیارد نفر نصف بشه و به ۴ میلیارد نفر کاهش پیدا کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/139669" target="_blank">📅 19:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139668">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8oNMfmWnMPxPvFVAbJQJXsrid-8B-kEgy1GwUqEgzpcxub9KHWkbD5dAuLSoXeEsyKmW182JSMWFA2J6vEnr2g0IguBvun1JP0pDICfRrOSLUJDdK5JnJIIeKLsIciHF8F_-vsEl9cQ5g448e6j0fbhhYjyIHJc4b8TMwKSDVPbPwiq611VDTIyh8zKqxCW59YXmz66Kaj2ZW_ywh3R1fVS4RtsIUA1DshuYTWF4zhS7ytEIlqHi49Zh2665Rpa-XcOTxvDOr79VhDNco2kVi4tMSYGU8Zc8HKUWef0aScKQECunVPGW7elvG1OnkSuGUkUodSDF42o1PfBCdiOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: رهبران ایران به طرز باورنکردنی‌ای دو رو و ریاکارن! از یه طرف درخواست جلسه می‌کنن، بعضیا حتی می‌گن «التماس» می‌کنن، مذاکرات شروع می‌شه و قرارهای بعدی هم برای همین روزهای نزدیک هماهنگ می‌شه؛ اما همزمان جلوی دوربین با افتخار می‌گن اصلاً هیچ مذاکره‌ای در کار نیست، هیچ صحبتی انجام نشده و فقط با «عمان» طرف هستن.
🔴
بعد هم طبق معمول شروع می‌کنن به حرف‌های تکراری و ادعا می‌کنن که تنگه هرمز با قدرت کامل دست خودشونه؛ در حالی که همین الان هم عملاً نیروی دریایی آمریکا کنترل کامل اونجا رو در اختیار داره و چیزی که ما بهش «محاصره» می‌گیم، یا به قول بعضیا «دیوار فولادی آمریکا»، برقرار شده.
🔴
هیچ چیزی بدون اجازه ما به ایران نمی‌رسه، مگر اینکه خودمون بخوایم؛ و از این به بعد هم هیچ چیزی رد نخواهد شد، مگر اینکه یا توافقی حاصل بشه یا ایران کاملاً تسلیم بشه.
🔴
ایران بخواد قبول کنه یا نه، واقعیت اینه که ما داریم برای حل مشکلی مذاکره می‌کنیم که خودش طی چند دهه به وجود آورده.
🔴
موضوع خیلی ساده‌ست:
ایران هیچ‌وقت به سلاح هسته‌ای دست پیدا نخواهد کرد!
🔴
از توجه شما به این موضوع سپاسگزارم پرزیدنت دونالد جی ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/139668" target="_blank">📅 19:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139667">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVbJcW24GfyF86tb8vkajwOx5JurGOmitD4iecILIebB899L0lSE8G-yGJ9PBHnrdFYPRHS9IuUNhKBkLl1549GdFf_UmuyyfMF8ZHJ8snOe9yKaD2gRl3qAhhOwZeftWVy48SfNgr7_R35CGjWxMxtpu-0i9DKnzwswyMCUFedGOs54GsBCymPuq-IyubVnEjrEflsTvEdpHofjMf6gNZAKV947vu453dEmGfmtXyCnkcSWLhYRAnV9VymG4SnVVQgJr3Cv1VcxJB-cQvVRXvbNNJMNa8lEhhP6x95Wr4J1IBR6mN2bJUEkYpt23UH9_w_kywqsBXeBrcQKUC9ySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام توییتی را منتشر کرد که در آن از اعزام لشگر هوابرد چترباز های آمریکایی به خاورمیانه و تصویری از تمرین این نیرو ها خبر می دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/139667" target="_blank">📅 18:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139666">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76554f0287.mp4?token=ULqGzdgc22V2cehI3Wo2L2-hYbtbAMzqGJylG3TMyWZPk51Ydj0-uqi7W3sNNXo6AtguCA5JQJwv3Wx5-oN7TKYiPbXbG4CWLogE4k_6ZpcGMJMwzrKjaEQtNm5eWGvETzSTXrZyatAV1fpa3Nik3zcvAnCEsFWFiUi9xry1hdvdTuHAl3ED7EZ0FRVIzDsYPXucYKex7Rym3ACFH2mP_PjycbXPIRYcBrtVbtOggYlpJpVcJgRON08Ayb8TMhtJA2hyqyfcq8WwZR2zMv-aRH8RfCX3kU6MEFEIDCaqjtwaIQv5TtjIe_f9DZFUg8jAZ09lzai1fw6NdI22oDSMMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76554f0287.mp4?token=ULqGzdgc22V2cehI3Wo2L2-hYbtbAMzqGJylG3TMyWZPk51Ydj0-uqi7W3sNNXo6AtguCA5JQJwv3Wx5-oN7TKYiPbXbG4CWLogE4k_6ZpcGMJMwzrKjaEQtNm5eWGvETzSTXrZyatAV1fpa3Nik3zcvAnCEsFWFiUi9xry1hdvdTuHAl3ED7EZ0FRVIzDsYPXucYKex7Rym3ACFH2mP_PjycbXPIRYcBrtVbtOggYlpJpVcJgRON08Ayb8TMhtJA2hyqyfcq8WwZR2zMv-aRH8RfCX3kU6MEFEIDCaqjtwaIQv5TtjIe_f9DZFUg8jAZ09lzai1fw6NdI22oDSMMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادعای نتانیاهو: اکثریت قاطع مردم ایران شیفتهٔ اسرائیل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/139666" target="_blank">📅 18:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139665">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd46c3368.mp4?token=vO1_gzlO_xpBKHBEHoMQpkAa7dA7Ew6RpjJmnkLSLLyu8WCUF57RPEOSGaHYz5KGC5FmTdyr5eKMSzxPEEcxTQ1_Hz7sCg1rS52PGavtVxM-YvMyBr0e72_uI83vhW_vpdugZHAjTgjKM-3tMQKa5GUhqxy3Ni4ma3JEGMlkdpdtw353Ki_a-HI5XsXX-qp_mAu3IOEROqZMhWuS-oMGw-ikM4EsTFZYMJd2_3berw8YtSbjFdpqrfLdkhitGexh2JcqSRTGsH4rE3zMurCZj9MFE5XLvaUvvpxyI5xCq-Klf95A3tAkK7UXTzE-KE_uh7Zr6E-Bs7W5Hxy4-BALtBIqUSU1AUL4XL1pBVEwWV5rysSjUNRjccEjXjAziWnC-mUpYimiHkW6ptwKcTfYiYpQT2cmGjEFSG_ALzqCKzb4dUq2fc_o6ZLz8NZpU0WwinoXSFrlTs_nJAjh4960QsZ8luTvZI6PxP3Ibbgj5WJf1Z7Fd33rqANsuzB546e0WMTSecZN_zWGp_8-kxgUR1UwepJrdY1Rzxu1RKZnllZfzm4a8-Q1d_fU8qi1XSvyC1XT0HaewU8IiaJzsNsOWeib5OjG3Vh5NKPBnn2-_Ee1rN893Fq5VPbF_R2U3JUcPOJxBVpjSqtwTyLdWnTc0CSU_ekTPj8zMLBcxefGajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd46c3368.mp4?token=vO1_gzlO_xpBKHBEHoMQpkAa7dA7Ew6RpjJmnkLSLLyu8WCUF57RPEOSGaHYz5KGC5FmTdyr5eKMSzxPEEcxTQ1_Hz7sCg1rS52PGavtVxM-YvMyBr0e72_uI83vhW_vpdugZHAjTgjKM-3tMQKa5GUhqxy3Ni4ma3JEGMlkdpdtw353Ki_a-HI5XsXX-qp_mAu3IOEROqZMhWuS-oMGw-ikM4EsTFZYMJd2_3berw8YtSbjFdpqrfLdkhitGexh2JcqSRTGsH4rE3zMurCZj9MFE5XLvaUvvpxyI5xCq-Klf95A3tAkK7UXTzE-KE_uh7Zr6E-Bs7W5Hxy4-BALtBIqUSU1AUL4XL1pBVEwWV5rysSjUNRjccEjXjAziWnC-mUpYimiHkW6ptwKcTfYiYpQT2cmGjEFSG_ALzqCKzb4dUq2fc_o6ZLz8NZpU0WwinoXSFrlTs_nJAjh4960QsZ8luTvZI6PxP3Ibbgj5WJf1Z7Fd33rqANsuzB546e0WMTSecZN_zWGp_8-kxgUR1UwepJrdY1Rzxu1RKZnllZfzm4a8-Q1d_fU8qi1XSvyC1XT0HaewU8IiaJzsNsOWeib5OjG3Vh5NKPBnn2-_Ee1rN893Fq5VPbF_R2U3JUcPOJxBVpjSqtwTyLdWnTc0CSU_ekTPj8zMLBcxefGajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: خاورمیانه دیگر همان خاورمیانه سابق نیست. ایران دیگر همان ایران سابق نیست. آن‌ها بسیار شدیداً تحت ضربت قرار گرفته‌اند.
🔴
آن‌ها هنوز توانایی‌هایی دارند، اما به ماه گذشته نگاه کنید؛ آن‌ها به ما شلیک نکرده‌اند.
🔴
چرا شلیک نکرده‌اند؟ زیرا می‌دانند که ما می‌توانیم آن‌ها را آن‌قدر شدید بزنیم که بازدارنده باشیم. اگر به ما حمله کنند، ضربه‌ای بسیار شدید را تحمل خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/139665" target="_blank">📅 18:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139664">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نتانیاهو: ایران به‌شدت آسیب دیده است؛ اگر حمله کند، ضربه‌ای بسیار سنگین دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/139664" target="_blank">📅 18:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139663">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نتانیاهو: یک کمپین سازماندهی شده با کمک مالی بزرگ وجود دارد تا اسرائیل را در شبکه های اجتماعی بی اعتبار کند.
ما باید با این کمپین مقابله کنیم و آن را شکست دهیم.
🔴
من فکر می کنم محاسبات ترامپ بر این اساس است که نمی خواهد اقتصاد جهانی فروبپاشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/139663" target="_blank">📅 18:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139662">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نتانیاهو: در دو جا نمی توان زندگی کرد: در کره شمالی و در غزه.
🔴
غزه اجازه خروج به شهروندانش را نمی دهد. من همیشه می پرسم چرا مردم غزه حقوق بقیه مردم دنیا را ندارند، حق مهاجرت.
🔴
اسرائیل دومین قدرت سایبری دنیاست.
ما در حال تبدیل شدن به دومین قدرت هوش مصنوعی در دنیا هم هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/139662" target="_blank">📅 18:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139661">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
نتانیاهو: من قصد دارم شرکای جدیدی داشته باشیم. برای همین هست که من به شدت در هند سرمایه گذاری کرده ام و نارندرا دوست خوب من است و ما در هند بسیار محبوبیت داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/139661" target="_blank">📅 18:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139660">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نتانیاهو: من دوست دارم نیروی هوایی خودمان را توسعه بدیم. فولادین ترین نیرو هوایی ممکن برای آینده. چون ما نمی دونیم کمک هایی که دریافت می کنیم قراره تا چقدر ادامه پیدا کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/139660" target="_blank">📅 18:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139659">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای خارجه ایران و عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/139659" target="_blank">📅 18:30 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
