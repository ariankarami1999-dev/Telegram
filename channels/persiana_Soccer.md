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
<img src="https://cdn4.telesco.pe/file/VTowa2YT4JSguY_UEIRY_83e8fAdAX4v44whZpun5wcs48GhKwWLWs2bR9q8LeaudBMKFlZu2VYzVqQBR8MerMGe3dSWBkq9HWG4M7DZwdV7MB2cEC-v1ztGIbVOvlJmyotDyY3bIa8DuSxYBIhVU5nBcwI4J95X15JndBzyeFKT8G8tPdChe-qsLFfVSEsXGYScBA1j5ahRiVPQLyIIr06ZwXdM7qEi0U8a__krAFk7biDnTvFm85x12ZGXRnKFogl94AfbOkS2iC8udDRPk6v44yohFRESkqupz5n0axXtbhpITh62dsUHjhHXk3FoUWWcRA73383e3qL4KNvrjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 449K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 20:53:33</div>
<hr>

<div class="tg-post" id="msg-30429">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opMDDiemdi0x0C3H7jd_MTTE_KzaSpNUoVtlclfwQAuLygSGJlI7gUChzM6pFins3ptYqdcn12OQZ8Ib6qf1pmy0Q4_Bq3LGHkdM0vCHvhRrnqwqm3OevjXCfTZBqshF92xr_1eTNV4GEn5e4ACUuZ0adZcn8yWTIFrVAH0Rjg2Go1D2jtpgmAZGq6-hts6YBOc2autw6dRIy55HnGYF4zVvjrT0aodrj353w9_YlBgcxs0prtIDy7rqXBZr6AbDobT0Zsl3EWyFr7VZ_9dCg56HxGH5z3ZjzrvD7PFVhAgvRqmIfWPGkCmj5z3cKfu4EfjAAKnDbxpjS1MazaefaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/persiana_Soccer/30429" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30428">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEJHaFtFd7S8gDkJgECdzn63PaL8ope9Hc8mJPLrFnxbzu9kmlTekIUQIpXmzAk3RHb1VRy17rW0jFYBBr6dVdUDZwrjqE3hOdfXRy_PSDGP-axP3ZmI0PAxwKSIgjs0sbGkrHkVzRPaEYvlCb2QxGd9tWYFmmLeuX7p77jJS__TyKk3w9bzDb32MjqnFMUbzr-ompiUajrWp2forLB3-qR3caPXvNg3O4cAUchlNjsn3ktqPxHE0iqZp5JiP6uzHZeGtevdOJablC7U3SOYE2PGMwz5rj0DSTWWpgnZrj25m_fLe9oeOJvGAnDXH3tCaj1iCoXmIk0HqhPqzjsTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/30428" target="_blank">📅 19:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30427">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-ROpXu-lf4aDNJD8Jojca7ZJJx-6ahO2Z-i0DLrDVbyswK8QHnarLw8wXdbNV92K7V9aP5Q8RJw8_zYs7-xuEArYv1Sk_OupfQnVuXbQZoFiUaJPDnosOLzB945fzvsWf8FL8UsGMAO0vVALp30hGUS-SSouFIGPWQR9I5k6xhkCEMjIcLP206vE9MzdfI-x9wHMhiSaOOXvvWwKEPfS5osovtxQQPfSWm3o55MgMosxLiiVI1ehxBoW-yq_dYsBPAkWeBHDtGACWkkV14KhefPG_dmN1wj9P5qEa4cdDW2xJhC7u4jo-8kqlWw04RN5UL_-wlwzCCurktBvV60qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/30427" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30426">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXwNEXBLlZe0j6mlpcRT1p5QDY1coFF0EiONaWiDv5lWeBeLaXs3Bisf8VNbzQmmXLnc-bz6Imi0k1y-3nJo5o6aq4Y21JT1IHDrVHJX7w4CeTYCfAqJ6ph8ynq9hLkOhMGPhNjx3PBvZsmoA1QMqhDhKXd8aq9-mUmweKovXCz4hm6p5R_AZlKPDWUaebMiuigLAnOfc-WXh76wV7sjDfrxE9v_NZQdj4fpVRSgSIuZlq3nzGICmcpORIQyN4TXLL0p2CicwjBv1fXmqui_5UvgM_CWIHp5GcwDvMtqNgGQbcbZAF3qRk-PJ7TC--SYFg90dHtXWQJIb8kZ09xCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ظاهر جدید وین رونی اسطوره باشگاه منچستر یونایتد با کم‌کردن 40 کیلو از وزنش در تنها دو سال. درکنار کاهش وزن رونی اخیرا یک عمل رینوپلاستی "عمل بینی" انجام داده که باعث شده همچون قبل خروپف نکنه و راحت کنار خانومش بخوابه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/30426" target="_blank">📅 18:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30425">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKeg_MXkMwX6eJwwtxV7B9ETOgleFCA1z6Kr4ma2ckLs--WUJg5A5FdYM_uvKxcKHZYhs7bMlyuqxWQ35QmWd_v61lB8xGAxImCXQiTHSO_MGjWmk9HhqNBKTfmwnkC0V4D-7F_-e4wfxuSmFyojCjB23aLm0pX0Du-raBfvXOhBN-izs3wO96NCgdf3pHPNyVHS1LQI-PQCyZIkSBAWZWzUoUhA98k1MVC9fePf-A-CP-oCFXiKNg9M2XYEnJFRuCYJAqG_NnO5u0AE8T8I8fxqBwVFVltUQFCJrjZ6Qu2CMcdL5iEFgjv9X8g8KkoyxEilZNlTIRTwI4aMWwQYbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
بعداز تمدید قرارداد اوستون اورونوف؛ باشگاه‌پرسپولیس قرارداد پیام نیازمند رو هم 3 ساله تمدیدخواهدکرد. تمام توافقات لازم انجام شده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/30425" target="_blank">📅 18:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30424">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d45DIiONNpjRBzjF9Beowy1KF2RjNi26JGWm4_oRjPQ_eU7_tBRf3BVhGYQ1y0XkJvyZXyV5GnaDjZiFrL5u6z9IZCK2n1VPWnQmboChQmcKPg65R5Hj1BKHXnU1-aFXqIZ9aC-CAPKdIvZz-Q-Qd0Ni6yV2DPMEPsfA7CaQ1yKn9eZPfGPA__G2xp0T4IQdWpt6DuH6GGZ_QwezqAFzrIoPwDGUfw8PzOINw0_FALD-K2T9-YrXkhk7pC9jBatNz4Zykz7ktr2aCNaF6yOiwkJ1gQ7obd_-bnK7egd4NU7hoH4aS9Azgy_FyCDojQPGCsfRJCV6utuQKWaKTKzzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛
آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/30424" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30423">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puylJMJfHy1seRcvDw-4YxUdaIS-iBD0weg3P-h_3KJrlJmym5m9p_gYbRX5esGmnK3NYG0s2JJFU3TUqrnH_o3wwRr8kQlbBVhr_-LCAFkSy71tvajT5nJawy51GcFTzMDga4DrgXZ6QvSRDqRwtM3338vmJ_xVvct3LHqyAHbMhKfTPWttOcRDvbKkJ6LoemmlvTmVSEaCR-3LG6hTacp5XMDeOe8kgUpF_KKtvnrD_jHUu0MRVbQrz2O7qC1pd4hjq1s1IzWu7_kgk9e7gbvKW7g3RGiS3I1uK68Wfom92V_Q_iFyBEzER_h_UaZeLNteRWMV-v52Q6NVmo3KBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه: امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/30423" target="_blank">📅 18:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30422">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFncDItagjVkmrVSTQCxCslKRlpP2OOYlLrlLM-YwWVCOijZ2FSs7AmvyDCifTPj2kRTxV5jEOXPUzq-DWWjAw9-mS9_eQ9Ui458B0CJ8skIxfGoKEFh_cslakE8M6XcYlEkWuwvBZyiyhNgzFZHLRf0Ng_BS-SATMVL8Oc_z-fwmewwuZkqCR_TiAPvvztxf_QnhPTgHu867284wf8FNOFQhYbEKR0ND5xZ99cuEG_j7rZEJywiAywdKcpwHub7I7I5G0MfbGYvH3ukTIihwqibZ07LHEHs5dLPTacmOp18HVmkUzgOS47TRAlNzl7S_uJ8z9Xhck2a5mTDaiEfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین: من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...! هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/30422" target="_blank">📅 17:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30421">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsGpL3E8iU7v14gslkFA8jQ-2pssZBp2PXdcqdJDnfOPrrjaUPd-VDB3tXdD3L3ISvF3zvLsbPdUQFivuPJVImFhsRreNQ_WQS-1wOQkQKQb_GSQj2pDLv4LSp7525_NaMAuIC2jUkm4u-4H_rHw3-ssItfiE3ho_RK7OxC-98HVGMtqeqRUcF4iaz6J3C4QQtKIgFDPj4lKmxLKTINpYronWhXRugw3GvtmjSjYvDx8c-XooyyTS3r1_2pEBv6Ez5mZINoBYb6483jh5M8OzOdGXawMEDAWpDHUgXA5O8JD5IooblonASnobdeyu0KE1zZlXCCkmd6L0DJGt7TauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین:
من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...!
هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از رقابت‌های لیگ باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/30421" target="_blank">📅 17:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30420">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wzy_uKJY09wq4mc6ZO5B4DpkFhd5a5F8MGXeCmaloQd_104r0UOUIJ0pSHhTCmUdsxede9jIyI60798aXPFZ4XTCNVm6Mgk1kE-QmsbZtaKFPKxCONWCxzySNibFCRBfJPEOHiKrEujNTMd9TsQysiZ_srR883tWqJEuNz09Mh1WH62dSdr09W7hJDPT3NHHDU0ZYUYkDZd57yZefR2qiJHM1pCqtOQ19nfHmeGYxtW_QNEfK0gaZTmnr1kxl4waQEXquzYdSAeTrYcFmX1IYZIz3An4bOBi5dAdxY7FXI1N7zmbJOZiteCgKiw7WmRIm95DP-t_9AhUy10PYL5GBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه:
امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/30420" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30419">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlT_kEJ5nr4h8r-4GsUncZ9vqEj4z7kQzHAtxulz6W1oimPN9_IIhflhyIQAt1H5G4c2yXSllPlSYODhqZeJsYpJGR1JQcXgzdfNhDUtyK5imcrfdXh_i52g3k6ss84ehKFEuHwW3YywSjgsa2p9eYo8ofYYgG8H6euNW01kEwJ6oiqvyDTX5APK1J8_vc320cLqySnqikC_-kpBIq13bPICm3vVWbRR_Bz_MQP1cFewD-yEj4zRizX2azWJXYP_x9Bws49U-WUsNO1uQFtEx1tTDycutS_e0--gyfL6QSGqNgGJvngWBahZ6UP4B8XWzdWD-awHFvG09TmIXLaiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاثیر نادر محمدی بر فوتبال روسیه؛ گل عجیب با پرتاب اوتِ آکروباتیک! الکساندر کوزمین، مهاجم بالتیکا، بایک‌پرتاب اوت همراه با پشتک حرکتی شبیه نادر محمدی انجام داد و توپ وارد دروازه روتور شد. دروازه‌بان روتور نیز بالمس‌توپ در ثبت این گل نقش داشت؛ اگر توپ بدون…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/30419" target="_blank">📅 17:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30418">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=mVchqkatbQbwqDXJ8zVKtaWsr_ju8WZqrAKSKc11zFVzencOIoQ581e8Ze-OAAZuUueBq2uCI2Cs5vS_I8QoxuDIM_0q4jvMzR7E4ZRehLIGXSEbAWpUOYyyIxOZZk2w-ixYVlRhwFoqDrPUFWl8k_gNKC9ouAQI7ob208K2Tbarrim7s0len0NVG1PPmXIRgJx1y-zOdPhWtEx2qrO85R-P59afFOd96N9irme5gcjcgCvBjPSulJ-dzM0PoO5CNqy9JIJIB_6WSPB_NE849bQNQcaDnpZ33UKjSWf-qQmTvzhVZ5klv07xdaALzJjscaHAPo6H3IBXCflydc-u3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=mVchqkatbQbwqDXJ8zVKtaWsr_ju8WZqrAKSKc11zFVzencOIoQ581e8Ze-OAAZuUueBq2uCI2Cs5vS_I8QoxuDIM_0q4jvMzR7E4ZRehLIGXSEbAWpUOYyyIxOZZk2w-ixYVlRhwFoqDrPUFWl8k_gNKC9ouAQI7ob208K2Tbarrim7s0len0NVG1PPmXIRgJx1y-zOdPhWtEx2qrO85R-P59afFOd96N9irme5gcjcgCvBjPSulJ-dzM0PoO5CNqy9JIJIB_6WSPB_NE849bQNQcaDnpZ33UKjSWf-qQmTvzhVZ5klv07xdaALzJjscaHAPo6H3IBXCflydc-u3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بعد درخشش نادر محمدی درلیگ روسیه با پرتاب اوت‌هاش؛ حالا تو تمرین‌ماخاچ‌قلعه کادر فنی یه توپ دست محمد جواد حسین نژاد دادن و میگن هرچقدر میتونی پرتابش کن به سبک نادر محمدی. انگار فکر میکنن همه ایرانی پرتاب دستشون زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/30418" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30417">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e769a610.mp4?token=cUSME8yactxxTEimJkkhWb7ZWkLChe1crAN33vyE0pgSjz4h20OhEQqMsOhQ17OdnNvFJLuXiMijqKL2sFzZDrKfVOQgcwzjQR665RHORxYDYBJakzB2NJntHBdYo7zmQ6iaS7ew6C1W_gTmIv_Iu_tOwUhVha_4nx4RPxwR6_anqU4rXjNUJvVf5XInv1zkaUNRQlfSp-f3-7U-fvZ4aNYtERXLt46YJrFxg2yYCpzE37P_aKZtPgD_Xf0fKEvF-BWYC7PHntMxCqh_DsfF0KxYjJB2hTkq3BY4y5icgRtoGmUBZleg9hsg57VB0X5RjGp4OcIz4YISjGZos3eCxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e769a610.mp4?token=cUSME8yactxxTEimJkkhWb7ZWkLChe1crAN33vyE0pgSjz4h20OhEQqMsOhQ17OdnNvFJLuXiMijqKL2sFzZDrKfVOQgcwzjQR665RHORxYDYBJakzB2NJntHBdYo7zmQ6iaS7ew6C1W_gTmIv_Iu_tOwUhVha_4nx4RPxwR6_anqU4rXjNUJvVf5XInv1zkaUNRQlfSp-f3-7U-fvZ4aNYtERXLt46YJrFxg2yYCpzE37P_aKZtPgD_Xf0fKEvF-BWYC7PHntMxCqh_DsfF0KxYjJB2hTkq3BY4y5icgRtoGmUBZleg9hsg57VB0X5RjGp4OcIz4YISjGZos3eCxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ساعت13:30 تیم‌ملی‌برزیلِ کارلو آنچلوتی با این ترکیب در دیداری دوستانه به مصاف استرالیا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/30417" target="_blank">📅 15:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30415">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzjMrSy2WPnlLzPEdMGX40iaaolu2IOs3CcrO_LZJWvcABLw2gDDCwpx2-9XfYbgHklQXbYLmOu3h_SJA2l8jaGBEC-6ekzBP3362_KUs1dZinr3w6vcKQhm3QeGzj1E5FXQ-_60uLIPn0NGWSURZCLgGUBEWBMhVay1jq4K8J3MKd3ZH0n-Ur_XIQN7dea-Wqu_bJYGocdM0KOXC47mLqowEN2NC42AqMpxBIxiNg__SSWyVPlYdWzU9koUI9m3SrRJGxq-Cp5vtvXg4ZSQkCuP-AEdNZ1MC1RgKUdvdbG3n2LSzJ8yQ7Gv9zuJBNLekRWDk1Fni9KQqrV11XdYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P6SWRgmdev0m83fg2VmCN05IKIvZEv1CEoTLdNeMONO3cZMaEjROz2ePVd5s_2tUkKjdL_WyaA0--K0VcJY1eXHbMet7kv9tQI41nlCgBBCxKD37Cox_32I62fh0KTxA3Wg-PZcLjBvgG5fjyngXSnE94LTkGh1se5sMBf05nNrpAmLjLt3l4Vrlz39ieGF8J06sSIqAqc3kt4LQCTYAZ3KPopsItYv34Yb9BXLTEAo7nbzV95PslwCMif7vHvBPF6gh59A1puapOskSjOdxq77CVP47y_JDzj1AYOZI9Qhb8SCXx11pnslz977XjgKvPx4iswd2Zkzeq3WOwDMBvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
انتقال سهمیه بنزین به کارت بانکی از فردا؛ نحو اتصال کارت سوخت به کارت بانکی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/30415" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30414">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9587608d.mp4?token=vXZ4S2vti_eg2uryoFKr1u48vd1lgRYKFfs3asTGbz0Odu7A7BBRj7kqiuzuh5dYDdueDVfOxRhLrp4lVZRDlGlCG_DSmNz9D8zEjoa2FEVsu_-9Xir7KjyvcO8kPvc_o54aN7XsX5hit05EjhtI-303wRvvA5W-BN13hRmrkHLJ7IcyjEx646B57z1dHPuSojCZLrQRN_DDomuQmXnTMENQGmoCetXPEhwPY5lctR-W9WCNCfAMmlQEgPY3xtGJyP47MiKcGjfif6QzW9DFz8-2ZKyp3xG0pSuWlC90mZ9dyAQvxmtwGPOU6s7RgEz8NvdlnG48qlVsIhg3b-0IeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9587608d.mp4?token=vXZ4S2vti_eg2uryoFKr1u48vd1lgRYKFfs3asTGbz0Odu7A7BBRj7kqiuzuh5dYDdueDVfOxRhLrp4lVZRDlGlCG_DSmNz9D8zEjoa2FEVsu_-9Xir7KjyvcO8kPvc_o54aN7XsX5hit05EjhtI-303wRvvA5W-BN13hRmrkHLJ7IcyjEx646B57z1dHPuSojCZLrQRN_DDomuQmXnTMENQGmoCetXPEhwPY5lctR-W9WCNCfAMmlQEgPY3xtGJyP47MiKcGjfif6QzW9DFz8-2ZKyp3xG0pSuWlC90mZ9dyAQvxmtwGPOU6s7RgEz8NvdlnG48qlVsIhg3b-0IeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/30414" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30413">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=FHVec2TEkVG6Ysa9PGubFX0NkA7ib5rVefQhWpZCNCb27rjoaI4B1DSogSFDjBcAmZY206gBiWLBL9JpTYApY_Vihl4yJGvM6DMQ6DxCHKRBDbZi2Xdsn8M7-n3U6j_uHaLz9khDJY7iClHBj6h-4zCZ1GsYBonE-vdgDTYuGq8Rb0q2UWEtnanWL3IQJBKHLj0HadrdVW9p9vxmLwM0NzDrolhOQA5yCaLk_lOSuQirNNzRcTvew_NT1LOYA7EGgtV7kCgLiHZNRWvfl3ZTV-QAajR48M7CQkyGiSDw9FHm2wCl4RPIvQemfYQNLStFvOriewWU1Ga0vaVSFWx1xDGsNJyZxMIFu9I27Xcg8vu1UqCbiZ8cDgBpqBi4DXw0Zdxta_JAqA_3XWTgjciXFgRfNL-VUrL8Uz61M2HLzUOHzltY4i9FdJ8w9RyT0O77o3Tdqc2NMev-jRBNtu9KHHdvrRtx-2U74xa_En-IDbj2Mq41uIOLKab_PpDMY7TMkhijhvdYW85m2vuB7E1I5g8JKxBLJXqNKk7tyr8gFdoLP0IXlmPrxCkqdWqFFkWQx5vVFDKYfBt0QbzuK2hoYXqhkDmANjNfyl-2AZZ77RtTy61eZoLHArMPtsvywalYK-nqOKwiWd_uTA8GO9SYHc8KYjo6zALoKT_9cPNLGHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=FHVec2TEkVG6Ysa9PGubFX0NkA7ib5rVefQhWpZCNCb27rjoaI4B1DSogSFDjBcAmZY206gBiWLBL9JpTYApY_Vihl4yJGvM6DMQ6DxCHKRBDbZi2Xdsn8M7-n3U6j_uHaLz9khDJY7iClHBj6h-4zCZ1GsYBonE-vdgDTYuGq8Rb0q2UWEtnanWL3IQJBKHLj0HadrdVW9p9vxmLwM0NzDrolhOQA5yCaLk_lOSuQirNNzRcTvew_NT1LOYA7EGgtV7kCgLiHZNRWvfl3ZTV-QAajR48M7CQkyGiSDw9FHm2wCl4RPIvQemfYQNLStFvOriewWU1Ga0vaVSFWx1xDGsNJyZxMIFu9I27Xcg8vu1UqCbiZ8cDgBpqBi4DXw0Zdxta_JAqA_3XWTgjciXFgRfNL-VUrL8Uz61M2HLzUOHzltY4i9FdJ8w9RyT0O77o3Tdqc2NMev-jRBNtu9KHHdvrRtx-2U74xa_En-IDbj2Mq41uIOLKab_PpDMY7TMkhijhvdYW85m2vuB7E1I5g8JKxBLJXqNKk7tyr8gFdoLP0IXlmPrxCkqdWqFFkWQx5vVFDKYfBt0QbzuK2hoYXqhkDmANjNfyl-2AZZ77RtTy61eZoLHArMPtsvywalYK-nqOKwiWd_uTA8GO9SYHc8KYjo6zALoKT_9cPNLGHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های پیمان یوسفی روی آنتن زنده درباره حواشی امیرقلعه‌نویی و دعوت نکردن مهدی قایدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/30413" target="_blank">📅 14:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30412">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqwhVniZK4Ce0b-2jkEF1JkWhKaNsjUOC0AZqqM8dE20MZf2EiSewqwOeVK3o3fDNvgt90dkmOAxexcp1wLsI5crCrTDZHN_8qFa0M_1UjVCjLpUnVOua7hTu_9H6M8qM7zFI7PHnG9n02Bzxk1PZuDBuOS3Ts7FrHhx03eBo646UuM_L5Q2TW6DQ7zmjIqdn9Rq1MGFtkFomq574yx_qv3lZNkMy7fIkrxOORmT1HqSzwocM38lRYrz5jbHmtFtQd9nOMRmfZ3S9_aJkKuJFbpeW6r4AzWqIt493I5I27MsP-ogF4pgfUHqrdfn8jzJdYS_MdH6ZHyQLPA9EXObxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/30412" target="_blank">📅 14:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30411">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlgxSV9UAuhnxzRuBEknW-ujqgIx40Sg4_-zGKVMYKqTRpvsUzudHcXAhYxMMi2mLu1p-CFzKOLClsNHifMdE4pMMiGFy4lYhdTA_S3pQ3Ukkyd8L7Lfjw7unEPpf2aS8dn1_eM6jGTaqppziivrO2rtxEaUF3WL6J5eH650DfduNrFyFwOSGGO9cuzI3iIOQkCU-1y3B1lG-rppjyRdTWR3K2vUwu5shqiB-C0qfK2n79yS6TTjgz1WiJVqf8eVxN61LFNqIG4feAsTc2rLYOqAa-Of1sOe0eA9hqIdU_IWzkPiFZnJzyq3EyOiadD_S25ay2mhHKE7tom1sLkbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه سپاهان قصد داره درصورت جدایی مارکو باکیچ از تیم پرسپولیس درنیم‌فصل او رو با قراردادی 1.5 ساله جذب‌کنه‌. مهدی تارتار علاقه‌ای به‌سبک بازی باکیچ نداره و بلافاصله بعداز فسخ‌قراردادش با سرخ ها با باشگاه سپاهان قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30411" target="_blank">📅 13:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30410">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVPXnbEyWXJukJkSUvnptTP1BmbdnsIkID2UHRWGqKYK562P5XCbMnw2uXdDegtbC5A5g5hl5szvtV9MuQIz63kMyrlCwT48Vi7j7Yt1PgG0sgWySzwZ8qDWCXxm5PJWR6aR-Sx8dFKCYTnE-oOHH3wrEcUrAjxyvIit3QCybzWTvLyajwxZjIsQQhFbPAyPG1cCHx4glvjVA3glhcg_1p2mIulOGCnMD29fRd8WYwbbFxmKMk0nBsamDcukNl3I4kbMTlKr3L9-AC6Zpnb9Brc9x44FEMg_HGVjSl9aWIROlvhfUh74p35r7Sj8K3ryXQu8ingSEKXSNbCvQUEFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج 4 دیدارمهم‌امشب هفته اول لیگ ملت‌های اروپا؛ از پیروزی خفیف پرتغال با گلزنی ژائو فلیکس تا توقف شاگردان ژاوی مقابل آلمانِ یورگن کلوپ و پیروزی شیرین نروژ با درخشش ارلینگ هالند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30410" target="_blank">📅 13:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30409">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyxrXvq08QWydoMzFTCpI4jdIfKQBpb8u7JSIHHQhS64VGKMY0lY7VUK8SzEQk4slM49L7X4BkPq3QVQ1iS4OOdWsC9oa_l8fmH2wvd57W3uLTHaCJ7p0oumedh5soQBGyfyvKC5XKuywmBwh4zHcs6AUA5L87ZvoRjHJdZEJmAq9aLSYluPNTtzUUxeIn6o8lg18JHWufn2kwyH5WlMIMjr-Hcl8sl8u0orqwORZia5RHGWtr0IVflrdHf6c1v_q_Rq0l12sJdnvBypzWKA7Ictd2IDDfQiIsA-7Ny0L7hh5H1V5aqOjl1pyItLs6_GSmIXu5aHyFapf8kXmFW9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30409" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30407">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLg2wivdnaP090j7ByZAi3BeRnU96sQIO73u8_7vsadZIJGVM-XfTlBCfguJLQu8sHC7eDTMJAmVtmuM8mtnjlP3T98XdBkcBh0Fq4brnl-X9Ke4assk8PqIE9rfqNg6sOjSRTgF2jeUuSYmlRbY1dg-cEaTHRms_N5SpM5FP8rPyFJ205HjpM9JxybI3vV9-YflMjkw7G1Wp_ADYNJUyRDxEMTh35rCMqcoiIdG_Simae906Bdj4Di4yaYy3JhE2Bl1x_3hkIqrnpObo90Ovis9q9gHuVC-rvbpgHUJKPqzuosj2I_JgYK-CxTYxX9WkQYqLEvX7d4BkyPyk92RPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30407" target="_blank">📅 12:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30406">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkjCTRHZybsmgHQ8WwhdPQhisLp7QqHEXPQYaAFrPWElzX18b9Sx0B-f3q6rnixqtMDsDBNuzghlDOMs-fJb8hpQZJMFWvHARRBfWJl8SA11486llGW-7957Gkc6Y4jcp_R4f7SH8keaSFNWAPAKRfhbdqGXQ8MHuQRNTgJUP8bPHOVp3rbQY4Sai2JECBQBEoRgRZ5dYnQmChfruV_T5CpBHGYI7untu7FmzcUVuS8L-_ewLhoa6Q5BE0tQVNRPQrOacIwvxY3Vu9QPuPBgss3IMJ-U-5SxZoX9ZEo4gWLGTQl6UFq5fInFJT_BopfaPo7mbh7uEyz2nAOgj_l52g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30406" target="_blank">📅 12:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30405">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLfLywaVBNsn6W2zMwUBi-gMtL927RvnUUjbucf-nBHL83BhTO9rm3ArryYNDMfA2PbM_ol68iqmwvpbDJoxi9p0g55C9PDiTPo8mMCqBSlXv8q8DnEUI9ituyuuXuafwY4tC0renCQUFVKiI0vgP6zrpObO9Gzkc1WzzWZmnr9MKXevEzoyrbIyGnerZr4cFeGjFliqW0xT69lHP1S0hZGA31Y4d2MXxq0-RNc2TUUx17qaknm462WyoSg9wPd3W8o7WQsbvzccz2yJvISsZnPvmaDW2gJ7hKuIAMmYWRJ_e9kli72if7oN1_6BMl1dEbEk3u-j9nmdjH65HowCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ دستمزدسالانه مامه تیام درسوپرلیگ ترکیه 750 هزار دلارامضاشده و دستمزد فابیو آبرئو آقای‌گل سوپرلیگ چین 950 هزار لار درسال ثبت‌شده. جفتشون‌هم 33 سالشونه. آبرئو در نیم فصل بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30405" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30404">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV8qDV9KK8sNdBaYRWRds_TRG0DRMykov_2MIfScYDtLb04UNrphOdzf_JqKGEgKT6ke3IaVMCIEsxFEba6rtMBpQpJjKL3dBhbDMR9Rfa84uSgJkYDO9fPNpiFgj9JjEyKHNZJUkN_KYk_OtpvPsEsDZA5AZZ0Jij3nzd0imQTY5-3OyYYEqwNvl8TmC62tZGsaMeFuspgVyGgCYc8JAZ7OAUB2GnxN5-Dtv003TzzFRqfwC7WGBdeRXuVk-0bPzNnuH8GCXBrwz0aXzeejpOrI5ZaSL3wtTyQem0gQVrob5HljYAFJ3Gv8OSLRKvA8_9DwNVlE2brh0WPCzRr8yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلیشا لمن ستاره‌تیم‌بانوان‌لسترسیتی: بارها گفتم بازم میگم نباید تفاوت زیادی بین دستمزد بازیکنان در لیگ مردان و زنان باشه. الان همونطور که لیونل مسی و کریس رونالدو در فوتبال آقایون میدرخشن من هم درفوتبال بانوان فوق العاده بازی میکنم بنابراین نباید حقوق ما…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30404" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30403">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNOcZpthxnUgOl0Gk6zqzV-BaxJo7wfnRNCGk6BThWuZV71Td06BCTRfWV9hE53xsKXghhzo_4F8ZOrPChq0TeYwFA0ySPaqCYYYCPgqxPeVULw5FdG3sYLmPmJ7V13GLBdfHCLOIMH0zQPVDazuHeFd6HCYL1CzYC6A770Fn6loXPZLxqZs1rnMw_gFH7138SOey-3qVWXqc2M63ZeN89sIc6xDdjhT3p2voVWi3EyUscVBVBAKi9jUvrb7gt6C000bS0m_zRnI3h5ne8ZoriRmhvXMWVwQyryyBLSfrlCRPFqe8fc5qzSWZVJPKOKyLTjU1yjAp9OI78cg4d5Aiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
جمعه‌های انفجاری در یک بت
💥
🔄
🤩
🤩
🤩
بانس کازینو مخصوص بازی‌های انفجاری در یک بت
💬
پشتیبانی آنلاین 24 ساعته
🔈
کاربران میتوانند در روز جمعه پس از هر بار شارژ حساب کاربری خود از پشتیبانی بانس
🤩
🤩
🤩
کازینو را تا سقف 30.000.000 ریال دریافت نمایند
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r3
🔗
https://t.me/+xNPVsLewpb4wMWNi</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30403" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30402">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciky19wKEdCsH4otU3zgKEqyxP5k4Y11tqWgSkRBP1YItwNq0PtJkpv1zXHf_MqIwrKb0nW5J5C5pCvOL-4gfprjQIGFljHKVBVNh6ctL1nf-a3NoHQaObcrB1fonxBSqLM0xjuu2BJnuO_re02jtSgfiFE9lPjyt9eojqwNHyU6pjmK1B2Avmwf7PJ87bF_Da2ndfO3NtKQU8Y49cXzUMUxdr9rnoO4N6GTUVwpcOPBbGCGrG2XLWZJt92jKgCrUcBuVb9e-JyZ8V3x6Onxk5O4xgKLQFyizCilHznlbcHLL38ByJSuayockq0Hr27WFHRqlW1imCct6k4PlOjEaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30402" target="_blank">📅 11:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30401">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638f1de447.mp4?token=nLWXan_CBOTnNxeOLBzJQ8QI8Adk1QchSmb2xzQitZDZBj5ZotzvM9HU0tSlNlTJudGtW2rh5jLq5KF4y_DA-L0rXufn0Hh7Bx1u0LFA__BonHr_DF3IcVRHMYLpW6VdJCrmoYXormMAoHQEzi85kDDLI1165GWNEJjBSa_67yYSXsyHdUaGQmWwsLVL6823uIpuqLoaF-GKRiusVyuMyOaZEYTRVqV9YrnpKO75jPZktz_cA8kDuOp90LKqS13Loik3t7Wt5sbRoSvF-0KOyu-RFid5lbgKIORTyF2NTawG0blnAjaJIABD1h9PymEy5ZWtTJe7Jqva14-mCPLuDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638f1de447.mp4?token=nLWXan_CBOTnNxeOLBzJQ8QI8Adk1QchSmb2xzQitZDZBj5ZotzvM9HU0tSlNlTJudGtW2rh5jLq5KF4y_DA-L0rXufn0Hh7Bx1u0LFA__BonHr_DF3IcVRHMYLpW6VdJCrmoYXormMAoHQEzi85kDDLI1165GWNEJjBSa_67yYSXsyHdUaGQmWwsLVL6823uIpuqLoaF-GKRiusVyuMyOaZEYTRVqV9YrnpKO75jPZktz_cA8kDuOp90LKqS13Loik3t7Wt5sbRoSvF-0KOyu-RFid5lbgKIORTyF2NTawG0blnAjaJIABD1h9PymEy5ZWtTJe7Jqva14-mCPLuDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا
؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30401" target="_blank">📅 11:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30400">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQKdr2cUGvOYM0Xpz-1QGmBWriRbcozwGyWbx0zaKTzVmXvTEjBnVOTVmp-xgjqJpwIo1gHZZYkPs4uOeUAettPDtEArz6srz2Ev2SV6EN1j0huH3VfncuSuJDUrtAw66WxEbYrz-wqFyIM0FmZT6YSO7RGNG8PW0jfORVi50tnBLH3EPdv6iQQvNafj6xd7fWrnseks9eVkCciXXek0aXJ5BDJilc13ihvsvNB1uixMBQ4IweGirbZTiNxyS1WwMZkF_ioEGRVSTYMyciBWxCBkCbZIDs8S37txZn3S6o295E2vzpf0OwOfqc5r4jXQGVTACN-pU8cT1KPWduIr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیویی‌کوتاه از تکنیک و مهارت‌های خیره کننده جیجی‌ گابریل 15 ساله‌که‌ بزدی یه راهی بارسا میشه یا رئال مادرید؛ هایلایت کامل عملکردش رو تو کانال دوم گذاشتیم. پسن ریپلای شده رو نگاه کنید.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30400" target="_blank">📅 11:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30399">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649db87b28.mp4?token=Q9jMIn-xgKGgGPAkHGw7sOMT68CaA-B5urGXnvaRQlsLKukRvpQEEMdHkkvFcUCc6t0aE8puM5GvjeLeNeQmDi3VfrD2fT4ThOGL4WaoZEjZFnChmOhXGVa335iuzmBU7hxJttad-gaEyxVX37_BX-QHvxvIxnFULlG3FFZBpxeG9i2era0pZlu8jnZTmR-UJ7ZwgSPXPojXW8POnpXb0Uoguv6GGWTJk9gOET_SoZyxVkMC-UTMZPDScDAgkc14NXJ-F7yslJ9eZ1bBKKloGvbho8oFA9EPzfdE2jXDn0GsKrktmSmaymG2Eq98Mf0cvtmCOQR0hbca1G39NmN7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649db87b28.mp4?token=Q9jMIn-xgKGgGPAkHGw7sOMT68CaA-B5urGXnvaRQlsLKukRvpQEEMdHkkvFcUCc6t0aE8puM5GvjeLeNeQmDi3VfrD2fT4ThOGL4WaoZEjZFnChmOhXGVa335iuzmBU7hxJttad-gaEyxVX37_BX-QHvxvIxnFULlG3FFZBpxeG9i2era0pZlu8jnZTmR-UJ7ZwgSPXPojXW8POnpXb0Uoguv6GGWTJk9gOET_SoZyxVkMC-UTMZPDScDAgkc14NXJ-F7yslJ9eZ1bBKKloGvbho8oFA9EPzfdE2jXDn0GsKrktmSmaymG2Eq98Mf0cvtmCOQR0hbca1G39NmN7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30399" target="_blank">📅 10:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30398">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHrP4UTV1oFeI1G9M7Q0tVUAVfXtZHmUHFwxmyjngb0BCMMvBeiDVGlrRkw74F8y2M7wqWLf51HBYI3mF8QO1k85jkvAhYr-tUp5C--CexjsW_QeXvDC95pSPnSEq8F9lEhpEOdsxdxObBxopHxytrAEH2dZXNm447mP-UJI-ufnl28SS1iiNklI_vmvQpyM3MZEcB85f2zEKBt3JjY34KUN-JIWupwZJvzi4FCOqXj0zkZPZuULgwZNv0H4eklQnpsi7s7r07k2BVhKEkpZ0zvtytTN8XkyIslluTeQ7bxRMF_vNzIaBicbjRiyIPU85JQdBOnL9F2i5rLEAYIFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30398" target="_blank">📅 10:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30397">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=bX3Bb0oNU9755YvU780kpDV39xAm9jdirLcI17UbDwhdij-W3mT_YvP9UeifHnHX6F1eqK43pEFOubWPOs-KnJAKLB74dZr1bkug5vA0ADRq2jvgIP3PXgx_zmYDekphxBaXHEXpp1pJt5NboT7mH8XdV_XDrkhNzqM9NhYVXv1Q9d-bQGB2ZiRjZtO1QTpYFnTZ6vQP-Iqxa6uErKBXms9xZggVQ1pxoh2EtUfB69pQ8pW5y9rhXlHfFFi1tk8TbOreG8c_ZwJ2qJvZD00nkOmSA_sdA8OUuPEKQZLYwcVOXjj6w-b0zEhUm3pu8aOGXy5x90QMKzIYqfzOzMb7oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=bX3Bb0oNU9755YvU780kpDV39xAm9jdirLcI17UbDwhdij-W3mT_YvP9UeifHnHX6F1eqK43pEFOubWPOs-KnJAKLB74dZr1bkug5vA0ADRq2jvgIP3PXgx_zmYDekphxBaXHEXpp1pJt5NboT7mH8XdV_XDrkhNzqM9NhYVXv1Q9d-bQGB2ZiRjZtO1QTpYFnTZ6vQP-Iqxa6uErKBXms9xZggVQ1pxoh2EtUfB69pQ8pW5y9rhXlHfFFi1tk8TbOreG8c_ZwJ2qJvZD00nkOmSA_sdA8OUuPEKQZLYwcVOXjj6w-b0zEhUm3pu8aOGXy5x90QMKzIYqfzOzMb7oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30397" target="_blank">📅 09:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30396">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSIbU27bvztaxytJz3x-1PVEBN8R9J1zEBO-WrrUpHodLLqtMhWl0SzsLBEfbKzVp5ZJU03wcMAoXyXGjiuFHhERDthnN8-ocQ78TWNkVB8KdmbSjzeJCegu5aTDwjatPpq1xCpxq9dCAalSCX--UiOZFgCcajK_uSG6AS-XGoUNlCxxxngpdofa7OsljIaaTo-KS8qxpvPAoinmOoufnZES5BIcjlanq_RIDdsi4iQ1aH4EU2iV3YfnuwYDnvC8AiFYzNVfvm0zakYCGnIpz-QOgle3BUZFJdNPRlBHNfoqiweKclejAyZqK570h1rbc61bmX-7JhqkGdiqUB_Mnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30396" target="_blank">📅 09:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30395">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpC4PwDRpG8TYR68QlSJZfG9PB3JPZqZ-bU1AKXsDoP-BV3VQ-rRvKwmaFYGARnhZPCQOOTbenBCN63gJuxOHh8X0QNqtyXZ6b33i8qSMKH-6EWny5OKwl3TBpIgkhdT-XzhFH7twQwgTeEuJ7jLfdaZ8QyXJeVG7VEaZ-JXbRgmSKngwA1CxCojbBxpbZq42HX6yfI5ZtFK6L9D2iC2Q-phWUFnmPB5xM96p9QqAcNQFkdh5yradtRLs5Ks8rwITaR3M_RWLRIQ-d3z9xLknZVEmD-bK7HbIlRKgSGlDZey0bviF6J94iaBEHCkr21BnOLlYRomtUUxKXHcX918_cAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpC4PwDRpG8TYR68QlSJZfG9PB3JPZqZ-bU1AKXsDoP-BV3VQ-rRvKwmaFYGARnhZPCQOOTbenBCN63gJuxOHh8X0QNqtyXZ6b33i8qSMKH-6EWny5OKwl3TBpIgkhdT-XzhFH7twQwgTeEuJ7jLfdaZ8QyXJeVG7VEaZ-JXbRgmSKngwA1CxCojbBxpbZq42HX6yfI5ZtFK6L9D2iC2Q-phWUFnmPB5xM96p9QqAcNQFkdh5yradtRLs5Ks8rwITaR3M_RWLRIQ-d3z9xLknZVEmD-bK7HbIlRKgSGlDZey0bviF6J94iaBEHCkr21BnOLlYRomtUUxKXHcX918_cAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30395" target="_blank">📅 09:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30394">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ortQnxrGsocpD-jfda11Q1p7_RjFLlNDVRx5ntPN9XaB3G7e__k-CikSpHRFgABVt4uy58_X0EMw9aXhg4xHlvucW_KkBeJrkoITsSjXQ79axsmkpq4AKzPu0xEr4wQuJH6sSToNWW5oY13BT1iRlV6pNbFPDzZRi2OUz03tM0A8N8zt_zjPQOTcGAzgNS1iKizMeG05mQHTP_ae7GkOglo4zlqkxihCmunzeJUeMtJwaNXsFVqzqtMnFvD5Mj6QEh0iKc1ZQPsGLsIB-Gcj9TqrESl13hrEhKPPqp-MhFob_qgo6fmgC3Dq_szsJNUVoh3qd33hqLeuDNhzcck_6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30394" target="_blank">📅 08:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30393">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VizWZjuVEykxDf9Ywq_hPUQL7c0C3FNH7rjWSG0hyspViIzmIFBP9l_f6dYCiAHNdPUKdefsHxfTUiH5vsJGaOlk5EJ-eeKVBm31h7_MVag1GNISxm1i_c62GCv_jzRq1fmSH9lPpHuTRrIDTqlrv_uBZ-mdl384gB-6e44iDlO4JPfcUmrSN6rRhzwymoaKjg9YmjCnDZIwSzeGQP8NHbkarFZGJrH-GGCZAlUf6zsoyWMJbcbD-53o8m5HV9HwfvX8WaWIRMNQS0muQmVPZQ2TtBdJy-gWTDXg5Fiv7gvD9GKNtT-4ZlqlMpoH4_6u_t_J-iFjK-jfZ18yunp9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه بدونید ازبکستان بعد از 6 بازی و 5 ماه بالاخره طعم پیروزی در یک مسابقه رو چشید. این‌بازی‌های‌دوستانه تاثیر زیادی رورنکینگ بندی فیفا داره. باتوجه به برد قاطع‌کره و ژاپن‌به‌احتمال فراوان در رنکینگ جدید چند پله سقوط خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30393" target="_blank">📅 01:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30392">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=KZ2muJm9Xrj7BqO7IO3O_qkNfOUMxzGnW8fkZd-a0LRb1evaCkjCIIx2LkzmAz2v0cyTMmRSHCIg_IGsjRFsc55s9rQo-iFxPxPeixMtedGZHm8Zbn1ox0wMUuLwANK_3eM9P2oeObRhqanxpn1e8RDmg0bhxP0wEhn5ZfI_EKORhRXUgpEXk7gP7GZ1hSimxtqjt0FRTgcHfpJTLF6dOyacvxodycPO3VLgPomf5IaRgDv2p_31u1vtbWS9DuTeRNIjQImpTNv1bJ8VjPqTynJZ44PjRPdTryxfsaZSuYl2oWLahPw7jljZQLKNMEs3Wsb58zQpbD-v0ibT1APmcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=KZ2muJm9Xrj7BqO7IO3O_qkNfOUMxzGnW8fkZd-a0LRb1evaCkjCIIx2LkzmAz2v0cyTMmRSHCIg_IGsjRFsc55s9rQo-iFxPxPeixMtedGZHm8Zbn1ox0wMUuLwANK_3eM9P2oeObRhqanxpn1e8RDmg0bhxP0wEhn5ZfI_EKORhRXUgpEXk7gP7GZ1hSimxtqjt0FRTgcHfpJTLF6dOyacvxodycPO3VLgPomf5IaRgDv2p_31u1vtbWS9DuTeRNIjQImpTNv1bJ8VjPqTynJZ44PjRPdTryxfsaZSuYl2oWLahPw7jljZQLKNMEs3Wsb58zQpbD-v0ibT1APmcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30392" target="_blank">📅 01:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30390">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okEQqRXujLZ1tDhPavX5sJ9WH5_y9x6NT52SerydPmMOeFwoDnKxqOSmYUB8EsFmZN2JZaUfFYxye-dQczvTqreeAl6Cv6XWPupbNzhRDVjjEmWZxeYERPReYjIMmrPxU_In-nJTy5_GEZunbUZwkUkeq_i_eXoKwNIRwDQ9QUddwi8-kx16jWT_bllIs2YYOhr4oUymkDGHKhN1Uk848bq9sVTrrPMu_GkIakqiN2EpEk0jaAt8tSbqN4ULk_NMQJC2wcVmlg4m7O4k0DaHKq7zPrPzMUyUlxg8CJTlmGBqiy2ApDbzCRyQ_t14zpn0J04d3Rq41DRrf7bwYTVpXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30390" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30389">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SatKL0TPJMMQBxlkH-5YSHdszQZfuhnIyOuKIGYJe8ddwVIGGYZ7GAs_PwH1vYTsQXNdQ0E_dxymtheStOwY7Z5nEIziy59-QwN_XcAiHmvgLMEw8uYnxLKIX90hoOQPtxyQHPHj_IKJSuyfhAe9bFtplD-r_0hYkj96FJ_sc2H67toHL-QFNF8ZaHpw79s2nq6FftlTwWya8aBmIf43O6HrJ1uCF3yg_gGaRIxFBRNwxlqCTDlBawfQE5cuuzVHi85bktNBIymJnZVnJjMPW0eOVspyYZNvba3yHcM23Yi0tY9f3NRFMsjKH3juz7UBHCMkjQZv88bWa6oZGxLd4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
ازتقسیم‌امتیازات در تقابل هلند و آلمان تا برد سه‌گله ژاپن و کره جنوبی در شب شکست سه‌گله شاگردان امیر قلعه‌نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30389" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30387">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTrC7xO1ebgYEoTgCa0yBYIyCgI3LMfv48cWYfsTnjXa9frvUrkO0IkaZeZDwtr9-eGvxkwGXPyYP0-GoXNph5L-GpSOhjfU2dI9hZiypCoIqDdABBq2smKbfk57ISOUqavr5eWKCgEQuQlo0mKXvtaHy9Kj-TeZ_ioy33Rh8bdMPkdouFu0CH4ndRuXvKLcwM5qCH7dygQFotuCW7P4R3vy9uZjTlvPgvo1SQuc66RBzBEtkt7IGMZZlxWBPw3EbueinX5hpMdmS-LzXzxDf-p8dRiPnrojCFPgzI51oRF82eflbMCAaB-Fvw0suJuci9OEbIgSJ8xbg8tQE4MrwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق‌شنیده‌های رسانه پرشیانا؛ دو ایجنت نزدیک به علی تاجرنیا رئیس هیات مدیره تیم استقلال از صبح امروز تماس‌های خود را با مامه تیام ستاره 33 ساله سابق آبی‌ها آغازکرده‌‌اند تا در صورت عدم موافقت فابیو آبرئو برای‌اومدن‌به‌ایران بلافاصله مامه تیام رو…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30387" target="_blank">📅 00:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30386">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYcO4TaQb_Ylrce7WehHBj4K5gItXfQ53zKxi_DIoJ08mvYr00P-afxaDVV--fT2D5YMPgAU6OrOnzh_3_8xUvzBQnfsEaiVMKysEWNsUBUoYymfBJO6cIOuVFJdxz_9RHZpEKo4VOl5RZbTxWM2_HTCtLxjt355KEvcFGmANkxxJvCDP_SiVZEIey9r0HgkXy2zrwR4mMDFSWUnS8M8JOD_-LPjnpx7Lxx7wi0g_3OQBLyYLyQKQ3KszxhrQGkK0JG0cZjH6eICU4PbPtzurcvwVwiW_uyEWoTd2bz3aynOO9XkVE-azZXPfK8Z4OIG1UZK4J9cPwr_itiUh9g3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30386" target="_blank">📅 00:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30385">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw4bOgGzKr4kGGIrBAXczg2l-118nU14GCi3tiJ1owlRPuWY5G7z-WqcoHSLrsw-KRTZxJk5Z3H9tD39vPDmNi_K87mdIELTnqdFIQl4G099ZLqcMZDEPiGdqys8sABwyZRfKGaedPRxvjcuWW8tVJuri99J2TaJYxuWvfzLkfNrVmQm-vXxgzDgl21sttOTcrA60qLB1AycNEbsUkFJo9k5rub57Qe_e3BeFr1QGXD7eqVNv_OIgR0sJZvKZiTV2rQ3TMGr3DHrlBkujhlDlDPFbCxZVO1ybJ5eyk3dX9f3Arys-pmOJmDSIr6JocsOUF_qgWgVqN3En5S63QRZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30385" target="_blank">📅 00:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30384">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzbR9VEli7tTDQxQ6SUIBQ6-0AKKWN3NPisrNYpS_TN5BjYtKPdWnb_S79qkoWIIEuV5OKC2-LIlk35nWstdUKF2mu43uytkibtaQ0t-lj96UuylFZUA9tIjkAZ5y9fHJTLE7hq93MCZda_LcLk4ld3lMzl2W-Bz-Vslq5V22-eAhW3Zh48nc_xVWw353UsadJVm3hQupPfY9ze_EbR8s9qjcOPnSXOjxKPFtH9hDptQ9OjUEO_HHQzBNljdLwVcncP2NeweM9233lfMpPm1_Ri0dQoD18LQBxkeC5uRHC1uFbmhy45eoPOLCt6qRZ9GWGn91ccO9M3y7zEPmf9g9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30384" target="_blank">📅 00:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30383">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbVxTrbCTyu6j3ZfvXoO_ZapQPQCgIhicA7jhb2crPuB89-ZmNFQBNTN5nGY4HLosI1XKeHKY9b5aPhfLg5WQwmVUgOUaAaBnXGL5MFcd50wN6XQydaRSMsBoyY0kw6VTui85kSvKxSqlGK-jQhIb0jCPfT0lw9vPSl7hqDaxOadgLe0C2KdwF9cgLEycftRJJT9pgat_f5_XSrP3Sf2_yIgXtTgAkTI1PIxE4A6sK_KohzoCBgIcpcaSH7gN3DIe4r6khwfsG1Dot2H8IkwOavHAfsvefvAmqBOzeFimjDZDQEoRObYy0-Bj8lo9nBXCq9bf4blsbx8yPx0vloYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30383" target="_blank">📅 23:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30381">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=anBEIgS_F_nnWwpKhVMoDBdbl9xmdXgk-FQ6fAkPi3fEWNH6m9xLD8vnfMT5u6DGFkG5nCCLxZLI3UcLCOazK_ariWgjeha47Pka6ecEuIYqCSxsyRNeCFgobaFBLNpxgVR3UHuEZx-QkSYYCYdr-JmsmGONuC6vpPJ4F1xWrLumeHDzkiXTJ7prFtkKiR0AmKzmqWhDOgJJkGGaF3E3t0_ShJf0hhMjrAH8JjgQSZnQ9YPoHjLetqMmZdlxr9yBIiQNmoh_-4_HnhYIrhOBCTp6ZFlmZeu76toxDnD85ldQz_3hhOCDSyMgslLitqzNs6z5uUIO7dPYLGrv3YKIgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=anBEIgS_F_nnWwpKhVMoDBdbl9xmdXgk-FQ6fAkPi3fEWNH6m9xLD8vnfMT5u6DGFkG5nCCLxZLI3UcLCOazK_ariWgjeha47Pka6ecEuIYqCSxsyRNeCFgobaFBLNpxgVR3UHuEZx-QkSYYCYdr-JmsmGONuC6vpPJ4F1xWrLumeHDzkiXTJ7prFtkKiR0AmKzmqWhDOgJJkGGaF3E3t0_ShJf0hhMjrAH8JjgQSZnQ9YPoHjLetqMmZdlxr9yBIiQNmoh_-4_HnhYIrhOBCTp6ZFlmZeu76toxDnD85ldQz_3hhOCDSyMgslLitqzNs6z5uUIO7dPYLGrv3YKIgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30381" target="_blank">📅 23:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30380">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViZKQuTY_GRrtVBXeUUfY3_I6uOQSmUqOXsqiVnAigbfhqe8IDcMZ_nDpUCdgVD84SaA6eF7pywepIiNAVX_w_m0R21q-_FQTgUyiTd6hd8ay_ZabzFFzMxitfnh-AMmcB6xBmVk-pCW6YcNjT7-f5FRQjSkuC89TgruPCQF24cA8t_idz1O9JaX0EJYRd68mQKIPs6v_auCl9rtw120RdGZY7iUG_YwajuNxLM4OjldLrg7xIKoBiZSbaIPki1DpPcROfyB3PVe3AHXJVKG5Bp4I72I7JMLtJ4LEvkuHeIDzBg-7WPs52KjuL6JrMI_s1bA_d724eAkPHDeQEAIbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع میانی رئال مادرید از ناحیه رباط زانوی دچار مصدومیت شده و ممکنه چند هفته روبه دلیل مصدومیت از دست بده. مدافعان تیم رئال مادرید در حال حاضر: هویسن، آسنسیو و رودیگر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30380" target="_blank">📅 23:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30379">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgAWGiPELbG5hS35PLtP94VwF7ogJmfxsXLzQbh7IkoEj3-wDdL73HSLeo-_30aHc8v0UxId5uOpC1prs6BRRmj4P0u4hSEg06bBcx-pS9Fd340s0p7_0q_qEZl450pXEBEpuavkA2s7ovpbY1rmRk0ix3PX_SCaosDkRvUn5c_bxXZ8BB-tK1VKSR62v-TSWiWnC-2ecuG7sytS7gb67RCN-Z7mDac5WLmXbE6G5WnXhUEo2GlYjtm3y01pFhdvMbrmOP4IHMEDxsO9ZeLGddwlneaW2nMIQ4HFjygY2f9w7rrr61iSnr2u-8LIY2gAx8aQacGiYNg_VTy0EoUviQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اختلاف برگ ریزون دستمزد مردان و زنان در مستطیل سبز؛ دستمزد کریس رونالدو در النصر 142 برابر بیشتر از گرانقیمت ترین بازیکن دز لیگ بانوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30379" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30378">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etaOtcDmzIbfyGxriAE_iA4uu17IxUvMegddki542UJGzLEXK7-5u6AopAKThUwhZyGn_We1uIyBKU7X-IDUYA4yNaX_8LCQSCL5LRi-E12DmVvGO7x2LtejsE8hOE2z7RfIFMwMmO8PqG0LiJk30pSf1bzW0UrrHJkaQR4M2Tuc3Im0gVoyRsvxatxKh0puiOPLToTHmgnf79aAdgTCFpn-E7LXCxfeAO1P4LiIDg3M5Q42qIxy6thGx9wLXe8qFmJSVD999pEOEM7UvWge9eEo4TrSjdAHsoD0RKYWwNvDidEC-6LxP8Gb_QGfrPJy-cM0Bv9Eexhebj52jPhAfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30378" target="_blank">📅 22:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30377">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=BLqY0Li1d_EnmwdkK5eF5-7dJAuivp8_KckoAcfWircmqBerkj22r9z7n0phCY8AHpdPuiGBtNC-LZwzQe3ZjJwg6XVYYdfPkWuiAZZ3zk7n5jWk-3fz-fJEe9yPX2Gb7-3TO8YrW06XiO0V2boMIlRyttBCfbOYoATNA67u4WiiJM44Fs2W68qPjY0lo55cLJzJOUAfFMb1Bv1r2xRbjkliyxJxOf_kMCKwYbulhOSorKt--Bad7OempRMUOoHq9yhJJz9mSVfADkv5Eu2ypF-UUI4VZGc_D_m-Y4ABG15Bm5qtUcOgn6G9wmehFbPxHlQ3p5twefL3eK6onw3rNByX8NSXYY7Lr3bDE96s_geVGv9p_rhNugq9ChaOBfoK-j-up7eAod83aIwam5RO1wBZmVDtI9uSy6nRpxclT4c-4EzNRVDxQl7Qt4V-NhRUoNcnEKsY_3TEG1CK4lkP2fAg4Y61TZW_1e1Q9bh6YDXav8nMB5o9N9lKq_kg8uFz2wERPfovsN4Y65HWa8P0wMZ88VxHY-_fl6d8am2JrylR9oGrUNcSe-TnSxSEilzP5Bi0rUZJQmipkV6oU254GkqJSBDo6YvUCbJxM6XsqSwX29pzHDKpDKI-0MVpdWhvhzPjILSJ1NmUigXxbM9TA0mVIfFAkj6zTCUZGW4uBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=BLqY0Li1d_EnmwdkK5eF5-7dJAuivp8_KckoAcfWircmqBerkj22r9z7n0phCY8AHpdPuiGBtNC-LZwzQe3ZjJwg6XVYYdfPkWuiAZZ3zk7n5jWk-3fz-fJEe9yPX2Gb7-3TO8YrW06XiO0V2boMIlRyttBCfbOYoATNA67u4WiiJM44Fs2W68qPjY0lo55cLJzJOUAfFMb1Bv1r2xRbjkliyxJxOf_kMCKwYbulhOSorKt--Bad7OempRMUOoHq9yhJJz9mSVfADkv5Eu2ypF-UUI4VZGc_D_m-Y4ABG15Bm5qtUcOgn6G9wmehFbPxHlQ3p5twefL3eK6onw3rNByX8NSXYY7Lr3bDE96s_geVGv9p_rhNugq9ChaOBfoK-j-up7eAod83aIwam5RO1wBZmVDtI9uSy6nRpxclT4c-4EzNRVDxQl7Qt4V-NhRUoNcnEKsY_3TEG1CK4lkP2fAg4Y61TZW_1e1Q9bh6YDXav8nMB5o9N9lKq_kg8uFz2wERPfovsN4Y65HWa8P0wMZ88VxHY-_fl6d8am2JrylR9oGrUNcSe-TnSxSEilzP5Bi0rUZJQmipkV6oU254GkqJSBDo6YvUCbJxM6XsqSwX29pzHDKpDKI-0MVpdWhvhzPjILSJ1NmUigXxbM9TA0mVIfFAkj6zTCUZGW4uBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30377" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30375">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhA2wmUEXdNwz4YnbIJywg5ovVpCcHYPyQECmRSdw9qWz244AlfT14Z8Cw5cWUbLP4xA-3X2y6RHReOnYk1kwD_-2JqiAS68CuYKZ26HGQTCA86jOvB2wlZDQYhkz19LckF3qjOpZat5Yg-PmElzVzRjFMrYbLs6ZyGIJXWjFnKH-_rDKLy1CRfNHYameOWATPgTBh3CMIh8zHyGt7yf0nhm93DouFhRtAGPPfRedQ6pLdah5yxOf42BoSyZN2UCvneLGww2_Y3YWtWzh4K0f0Gr4hCAYiMUIBFlveKD-m2t4jV_zT4H7X2cmJDn7y_I49iw70PcCbsLjF_za1Qh2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgg3zuoWWkjn76YDt7Ng31TCQYi526jCbvnnJj09Faw55lKFAVP7EUqpKahdmph2s0woAzZB5ihgpA5_3ZjV_OnKCzC5vjaVy7q87ld0RUkRbVLvTyZf9aRoVGzLcq9Xo0TSc7yNHj4Zsc_OU-GNdbPBoQXUyBwOX1UFB18If69DUkkIYsLmjLYMZhxwUCSueTxi4qGq6mx90YRXF3xvoIXDlXv6uQltsdrY-nWby5oBnnV1JYQ3VnSuKYmi758QqyckejxEZk5PrOKyKBpwFnCnHJWEQg4VctaqmPVd-m_4rzzDS6-qdQNEXiktiS0T-sLGtTpds84j7mw0DSVkkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30375" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30374">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQnP7z1nQD4v6ZLDmUNIsVWZyTRYo36J4W3AYPP3k9RRxYrds5jy704YVZDxurV32pJvFSTwMe5bG79UWn30ugra7Cu6TzPinmLAmQl9VViLakYEi4tEax_9xcWmjrHWR9sbtz0Mzu5gYsclrkT4bMXrYzvh1WlXfZa1e1IBFeuHko0bGatrTvDUxfVnZwb7JvSo-ZN-aedkn9kcrtoeSWnioeKl6E--ezwBC3P7oIbB233IqEexfL0utvegAedtm23OmH2-YaBUkYLit-N0TrpY-Bq-TksY7a7XbswKiDRS75plC12WAV7aEsYjvWm4es627j1FWHxaC9EW0UPxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ گزینه اول باشگاه استقلال برای تقویت خط‌حمله‌آبی‌ها فابیو آبرئو33ساله است اما درصورت عدم‌موافقت فابیوبرای‌اومدن به ایران در این شرایط خاص؛ گزینه‌مدیریت‌مامه تیام است که‌رابطه نزدیکی با حمید مریخ ایجنت یاسر آسانی نیز داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30374" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30373">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6c6bFunPDo5aaQ2G2ugYXqtl6b7mB5XcSYPqV3Nhk4Qj08Dtypn-7YoLSn_WfmLiahMJnTEuRjkilH4UkscaQ_kHeQ3A4BJT6VLLk2vrba51GaEVwygS3S0QlrjaKFxP2NsYbLtgA5VS9EoBf1UM12Ss994Ft6h3QygFHV57yFxfOoGZZ_UnTQll5E6hLpiTzduTFcSkmxhh7v4d4fMHlzmbv_aqYWAcjNVEC2VndZlAytDBvlrtNB759iGGsRgok5HtSTSytrlwN53gcOHYhDwjUAVGlFZGUOII6B0gn1RzaQVv_qoqBBx_7w0CUzVR8sHvV8Uovj-kYJ67_BdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جذاب‌ترین‌مسابقات‌ملی دراین فیفادی؛ به هیچ عنوان این هشت مسابقه دیدنی رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30373" target="_blank">📅 21:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30372">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏀
پرتاب‌های دیدنی مژده نظری ستاره تیم بستکبال بانوان ایران؛ با دوستاش شرط بست 200 دلار برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30372" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30371">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30371" target="_blank">📅 21:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
گل‌های تیم ملی ازبکستان در بازی امشب مقابل تیم‌ایران به این شکل زده شد؛
گل اول روی پاس گل دیدنی احسان‌ حاج‌صفی37ساله، گل‌دوم پنالتی دادن بیرانوند34ساله، گل سوم فضای خالی شجاع خلیل زاده 37 ساله به بازیکنان تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30370" target="_blank">📅 20:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30369">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaPeDFwX-qqxB71mMWKwsgKF3ViD3dA2tE13ieP6lbYE71nSkaD94-68MvPBdcES6r5EMWHBpmJkoryewrneXeKiwa9rAuNw0CYQTizhi69F5xgdOIRkF2kmltXFilUjGkMVoh2mY1aypT4kSzC9gSaxGDKZ6EYgaF4OHjTHfHn7CQF64qDwm1_LQh7idX0T0vmdcFicpTy8b5IWmolcaWWCKGNJbbX5ZV6IwcKuSiwY6cew7JcoAVw9z26ptiSkLjIYdJNwILpQwte6taswWLg_RlNHk0QtIq3k4w2nrc-_Tl9sXkkXvjymEiU9Jamr0nVOnRXiqVQakPaIh513JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در روز پیروزی ژاپن و کره مقابل حریفان خود؛ شاگردان قلعه سه تا از ازبکستان خوردند. این نتایج بازی‌های دوستانه تاثیر زیادی رو رنکینگ بندی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30369" target="_blank">📅 20:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30368">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30368" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30367">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0dbmYVsz6-zqOzry1punpwJfM8gF5z0vHdrldfIDyZbNe9dqKeRsqvXeNSl-Sw2ZY5ZG9smmvhTbLRvmM68UHs2PMdnMctTIQf-p4GGiJ494qOR36Pj43iJujpsTOqHYA-LB7FXtLC4etO--XJqfzXGhe1kWshwsDlRfnPZR7REcEIWcWAFtXYGZIgjJxomJ9QV5O-O6KcBx0st339TRp0WGohE-eiLO4uqRwpIdiuNUwYCorMa3XMlnKFwm6NZ3gl-EfSw0TpjXFQA-kKlgJEABY85DVOKRYa30-ufJNZQXNwcBrThu4VKSknhnr8s_9PXn_Av1higf1EgnJE4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30367" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30366">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhmibuHwi2PwQUTHKzn6QoYx6ye31gl3n8d2K5TqDebg3ZO8_Ht3gfTrcHWR1flveFT9QNbBLrK231ZUj6_0lwsV7CmpAZy_tmzoguQGEpKgiu9D_bTa7bFMYhiw7A2_c0goZlLXpduU5GKJobYw4tailbUMV-g8Cq95ZXM8NpIu1okU3K4epJCBIArmM_Eydu5ShujB4k-C7DeD2GQbmHGHl1T5a7U8dyf-LRkaVTY3D9lDHCPplRR3TJ9KU-Rl227H1TnJ71Gt8up_q4vWpZ3wSH8u4qSZNgiaMhzlVK1IP-dCDCSr9vUUE-T39jFvZlfjfxeCiUlQ0ZxNdwromA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30366" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30364">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9JNaELevL-D9fftjlWe187I0WCUmczxeCX8nfugacD7BZDzK-M_ufvqqsvKTMFhQx81W8vsHhL7imqYt5LCME3Se_pU-5uVS9131LllgsdUh_hcuXXEDmRP6dka7v_E7acfJ-Gmr_yjTIYb6b5Ptuk4JDs3CLbjDZoFc4SF1ZrLBT-5-JpHEH8wsqieiGDpV55XM-PUhn_eCpL2igcPCh2JCbaxvp38em61rnobCZzXUtzWzyQAXXfnTYxgFzaVkU3_2DN9UamByWp-rhtcClXLLs1Y4oVq5S73e3N45v_WrkevqOK37LbLiPdf77ZcWUMgt5w9ztfqVaQx9fkFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
حسرت ژنرال در پیروزی برابر ازبک‌ها؛ گل سوم ازبکستان به ایران توسط نورچائف در دقیقه 95
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30364" target="_blank">📅 19:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30363">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=S5SiHCBAcRl-hWmoVe4khtLDgxYjPsWKe8Qr3PrmMyvKTMoUb5WDr4eJ_pqyR1gKxte0-savPYwashNnydC-knmEPhdhXJnrLYpAA5VEdsOu6hQwLDugWG_3dME9uZAi0c0WqqYcY4Kc8Yy-GLCVJBGcULsMx55ZAeshmtIPPvMvrWBY6Hv0rFWrcUDKojSRrdgzA4Kj15Pyq06ZX2ThsoiFdBWNPe1U0ivO9lrCNtRUyVP000X5syQc2dDwnjmQKCVvnELUWhCanZRgC1ymyKvz95vRPDAk8RIekCec766iVmcumTSOrB2LrWbSUdmOnFPJGjAKlk6q20a5jTA0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=S5SiHCBAcRl-hWmoVe4khtLDgxYjPsWKe8Qr3PrmMyvKTMoUb5WDr4eJ_pqyR1gKxte0-savPYwashNnydC-knmEPhdhXJnrLYpAA5VEdsOu6hQwLDugWG_3dME9uZAi0c0WqqYcY4Kc8Yy-GLCVJBGcULsMx55ZAeshmtIPPvMvrWBY6Hv0rFWrcUDKojSRrdgzA4Kj15Pyq06ZX2ThsoiFdBWNPe1U0ivO9lrCNtRUyVP000X5syQc2dDwnjmQKCVvnELUWhCanZRgC1ymyKvz95vRPDAk8RIekCec766iVmcumTSOrB2LrWbSUdmOnFPJGjAKlk6q20a5jTA0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
🇺🇿
شاگردان قلعه نویی دومی رو خوردند؛ گل دوم ایران به ازبکستان شومورودوف در دقیقه 58
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30363" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30362">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6tWpRtqyYAVKLT9_pGADbVe2s6w70-HUM4QwlC2VPfZimIbBtG5AOlEViMhfoV5wWB1cOQvHGH8zm7L1M4F_90sPuB_NXyinm352AjjTo86uwWgXKPq2vx7T14lefKnb5QqVribr06fgsjvtareZojTjURUBFVAv4oGo7iCxnOPs-bDRO3rEdXsqr6pX2zlYtqbBPg1jfPMcZXpWuB07_j2feLsZwmvQ7sRObuUSxgDi3Ca9hts-jb5_z1YFVvqwZuYH-JBWKraI_eFYvErsAl8N1Q7qNMOHgJ6PQX03_a4wJdqRUB2hKhBvLtMMJ5UXYk5vM79CWobiw7n5QE9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30362" target="_blank">📅 19:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30361">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401621b710.mp4?token=EPsaigI4Buf_lI7EnU2BdwbVJ1MHlUjxNFbgmyDQGpIXafJ1FmzbX15fS_XrX6ulAlMzp24Me4EgH959z41vj5YKuyeG7bppW1-XoWahICTlZ0F8NAvHbJAKw6IvyUZK1ibUT6JOthqcVK5_jjDI9jL2iJHCOxJhQ9eBCl7hR4ce0jspeqsqS3ZQkKKHUWoY90KoFreJJ1RnbdSk0s-KYjFYn3zbo7R23WTzOIkMQmAyNClPv2vCV7sq7DR7woQx-lx8tKHLpmNFN-MFQsnVQxvXCSelaIGAmiiHsli0weUwfANdSFsYbg00ghZItPRhKQ-qbkWaWIzG8PTThYVyGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401621b710.mp4?token=EPsaigI4Buf_lI7EnU2BdwbVJ1MHlUjxNFbgmyDQGpIXafJ1FmzbX15fS_XrX6ulAlMzp24Me4EgH959z41vj5YKuyeG7bppW1-XoWahICTlZ0F8NAvHbJAKw6IvyUZK1ibUT6JOthqcVK5_jjDI9jL2iJHCOxJhQ9eBCl7hR4ce0jspeqsqS3ZQkKKHUWoY90KoFreJJ1RnbdSk0s-KYjFYn3zbo7R23WTzOIkMQmAyNClPv2vCV7sq7DR7woQx-lx8tKHLpmNFN-MFQsnVQxvXCSelaIGAmiiHsli0weUwfANdSFsYbg00ghZItPRhKQ-qbkWaWIzG8PTThYVyGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
کاشته دیدنی ستاره 36 ساله ایران؛ گل اول تیم ملی ایران به ازبکستان توسط رامین رضاییان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30361" target="_blank">📅 18:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30360">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=BJZY4Y7uVoLFrDh3BR5btPBaMM9Vy0kh5Vh94wOZqWTSv5e5nFn8H5aQ3lKvKpz4K59Aq2fDSGFzrIJ9rnGZAEcswon8PgQ3unQEbhKMmUjPrI9bYZ4QNNwf9m_nhoFjiH-O3cC8yk5XN8HmUHWFeAB-eL4K4yqwCYx9rXPMsPUI_YvLH-zMJxhSYTH2CJGibvBAbnrH3r5_eXdvKBVetQRTetAeFvniOclLj3AGTthRBjNVi0o7-WkTD2HBdxfiqvy12JTdqIW3yL0CYV7X_gFn9H3j3gS889EGbcc1Diu6wtcFYuCZT7MtrXrQu32FS81s5qd6O3PZOTaFpMvGQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=BJZY4Y7uVoLFrDh3BR5btPBaMM9Vy0kh5Vh94wOZqWTSv5e5nFn8H5aQ3lKvKpz4K59Aq2fDSGFzrIJ9rnGZAEcswon8PgQ3unQEbhKMmUjPrI9bYZ4QNNwf9m_nhoFjiH-O3cC8yk5XN8HmUHWFeAB-eL4K4yqwCYx9rXPMsPUI_YvLH-zMJxhSYTH2CJGibvBAbnrH3r5_eXdvKBVetQRTetAeFvniOclLj3AGTthRBjNVi0o7-WkTD2HBdxfiqvy12JTdqIW3yL0CYV7X_gFn9H3j3gS889EGbcc1Diu6wtcFYuCZT7MtrXrQu32FS81s5qd6O3PZOTaFpMvGQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30360" target="_blank">📅 18:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30359">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nwh01RgfY8P-LDgFq6F30cvZKbZiPjid1keltvjf7nwpYXWYbqZEjtl2I8jzUMRZ-cL2oEG-DbETzu1OnUZc6B5rofWKFXiW1RGLCA1rum2ScM9C1_m3ZG1EgDLHtEe0JTsDq2zlSSfRmKtXfCECG5QkPhX4cfpzJgeIjEjWezvSQ5199dj1YEJt5GRlrXH7eIv48yc7AGiQc1ZPciudHZT_6XWA6ex86om--s35SFvuHtrhCNYXJPdGofNiPX9AzT51_5Uh1mspIil7anxHUsZr9XE7jYjuAydiD9WSroQeU5vJtQfVnfLfdv5Dbd_9es_zHQQqW59Og3Y8hxmQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30359" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30358">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=dwLT6-w_JDdP09joBzgHXqQwqNCPmymlCWmXAS5KMedZfCSphBttXK5d88wuVLqgs59U43zmD-Kr4N3PVG96enKWIaexx6NXaXt9geH4zSA5GphdbF6DlOlyix9emQMxFqQ6dAS34tpg6YujhEK796qoVLHpHGCaPml4tpT0B6XfSNullpFOEt2q9dHfxuM2JLq4rdLo9fHYUnFSY49udcgWLT-ISHhUn3Dk7ycty9_Hk674YSyEQQVr2em5GkwhBMQ32PjTZAzQz0eUfBtakzCC1wX8DqK6QE1iyeK-hHaGbc32MmpKn39TWvU_5ZkzVzsc4kha64Aciyu6sCZrfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=dwLT6-w_JDdP09joBzgHXqQwqNCPmymlCWmXAS5KMedZfCSphBttXK5d88wuVLqgs59U43zmD-Kr4N3PVG96enKWIaexx6NXaXt9geH4zSA5GphdbF6DlOlyix9emQMxFqQ6dAS34tpg6YujhEK796qoVLHpHGCaPml4tpT0B6XfSNullpFOEt2q9dHfxuM2JLq4rdLo9fHYUnFSY49udcgWLT-ISHhUn3Dk7ycty9_Hk674YSyEQQVr2em5GkwhBMQ32PjTZAzQz0eUfBtakzCC1wX8DqK6QE1iyeK-hHaGbc32MmpKn39TWvU_5ZkzVzsc4kha64Aciyu6sCZrfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30358" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30357">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=OD4C19jTtNJ2Jdvyi-1GB72PLJi3WdUAeIADCtX7KekBE9oYRHvSk5b9e4DBcZfDGteoFMxz4nEcVzAxQXPoQQl98V8eHdxvGNhsIZ0VdlMJOjtiuHZP_tukm2MfjpTSBcWnyv8Npz_g00PcGeO3w2Z4wEZUHs-RddNBDPNPfmo6NeZ7qUebWc1BbXJrF8P_aowXuAAR96ePfZxcXmxjQAKUm_nNKk2hcIm50KTAtpIP8m5kQTTy4NdagrI8UxKevpYo5xEM603Le-lO7FPLDAybMECb5DqCHE2-EK8IAWNjJNwydSP8-4Xo4jfZY_0c_ZEQVzug4IxJIXuJX1RAMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=OD4C19jTtNJ2Jdvyi-1GB72PLJi3WdUAeIADCtX7KekBE9oYRHvSk5b9e4DBcZfDGteoFMxz4nEcVzAxQXPoQQl98V8eHdxvGNhsIZ0VdlMJOjtiuHZP_tukm2MfjpTSBcWnyv8Npz_g00PcGeO3w2Z4wEZUHs-RddNBDPNPfmo6NeZ7qUebWc1BbXJrF8P_aowXuAAR96ePfZxcXmxjQAKUm_nNKk2hcIm50KTAtpIP8m5kQTTy4NdagrI8UxKevpYo5xEM603Le-lO7FPLDAybMECb5DqCHE2-EK8IAWNjJNwydSP8-4Xo4jfZY_0c_ZEQVzug4IxJIXuJX1RAMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های‌ بامزه عادل‌ فردوسی‌پور با لهجه های مختلف اللهیارصیادمنش‌فوق‌ستاره‌ایرانی لخ پوزنان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30357" target="_blank">📅 16:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30356">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UukOgcdS8_X6xPLgdtsTBmNvjkB4_ygn-5l088kCdOQme527btsELmGPuLRMsVIqzHGs9FP5nJnyTWzloDHwhgiJewTQtp89W5ZY1TNXDG-B2jVClrO5_6K_RURgCxP9spmcfDuxr6K2KEGM-xrPTHbv1jgiuyFomUMw5vwchevlzs0l_lH_Ft9ugIGba2iawTIqJH_wEZybrIaMx9rWH-KdNuh-Hui28Z5qY3yRRyQk-2dOxaiDitEEd8XYLz3GXCFremx3syA5xydIuEeQlF6HARzK_nhizbs3EeTDL7yjGv4j642pgpZLypM__jGci4hivAVxuIWTQmUwaukUZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال قصدداره که برای پایان دادن به حواشی پیوستن بیرانوند به‌این‌تیم؛ قرارداد حبیب فرعباسی گلر28ساله خود را در نیم فصل به مدت دو فصل دیگرتمدیدکند. محمد خلیفه دیگر دروازه‌بان 22 ساله نیم فصل به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30356" target="_blank">📅 16:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30355">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcTMvTYw653RMz3wwbwNnqjY3ZTPxI2EfNht9uNL3aF2mnPZtuROQ1n0aZmnBWrNLNtlMiQX6e5Dk_E57kArLqy9TheTQY7EZy-2O0fNtHtjaz6HvkBEYWOv2BRSd9yD6zo96gnt7LrVYR9N_tWxIDuo8oOTlm6uFDaL9laZe66-tzahQpyymdpC6Ztlv16m5NICh6ruBb4LuKbRvq6h4L6SAUE-AZxH_Ujm1XjcAD0F5wvFGp2ZSjqFKTN4OAIBOXtn66u2oL3YcYaRbZJVqQHTmqPgmb_QnF60k8OWF88KKCVKW4ERmurZGUm0xzozZwHjjMBK3B_3MELN-5ehBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30355" target="_blank">📅 16:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30354">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=n4_-EYgFTZdJ2fDyzBPyoNysow6rkmSfiymeOq4D6JQ5bx2COibHKm1GUUae3E7iIRK_ObaSnIBEcZZ92Qz2C2G9-EpPgmd6TzNDpV1gNyVl4z0w0eMSIs0hi9LeMWvU-GnRmQ-I2sHVS-fPYUVP-5YfBeCEqSnW2rN9p16faReC1hE0lfNlku7Kn8pxw_q96HEG-SuZ2xX46W_caNIKxUezdXyhgLs8TVSNOD4H8pSKvH9Q4EnzvtKfkBMlVTMTBp67cuqf9bOV1kUl85q6vvbZ-Xbh9WFvGr7rTiuOK2WKk4j4dN2CBMCA-BcNCUA9ayMZcqE_Rbq97wL5QGhCWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=n4_-EYgFTZdJ2fDyzBPyoNysow6rkmSfiymeOq4D6JQ5bx2COibHKm1GUUae3E7iIRK_ObaSnIBEcZZ92Qz2C2G9-EpPgmd6TzNDpV1gNyVl4z0w0eMSIs0hi9LeMWvU-GnRmQ-I2sHVS-fPYUVP-5YfBeCEqSnW2rN9p16faReC1hE0lfNlku7Kn8pxw_q96HEG-SuZ2xX46W_caNIKxUezdXyhgLs8TVSNOD4H8pSKvH9Q4EnzvtKfkBMlVTMTBp67cuqf9bOV1kUl85q6vvbZ-Xbh9WFvGr7rTiuOK2WKk4j4dN2CBMCA-BcNCUA9ayMZcqE_Rbq97wL5QGhCWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛ خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30354" target="_blank">📅 16:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30353">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30353" target="_blank">📅 16:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30352">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHL9xgap1qIXGSXYK-yybbLkYIvAORzF834KmDJ2gJNIHw-9LYmMqgvD81iTqAFpKpTQ1KWJRZGE0JlBE_nEb_v8zaP8W4wvd22WC-LzW6kOUPkrc1iBoJTihxiEIUEQAKbbG7KTPGcfSuXsmrCJ7dz44BJKrJ-B5IuLPNbaWv_cQxlFix0riWlZt53c8oFa7wOR2WWEvYTxSXF0Hdeilaqsx6P0WUgtdzKYESBQO75d9wZXI5TRSdMgO2rU98teuYFGyazPw5cGMSdhkKlRGrknSrR3ZiOJnHeHwFEPy4iW-OCMeiLuGnYSF1OU7pYA1yWtzQ0MiQUSCpULnJ51MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30352" target="_blank">📅 16:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30351">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtbCOyQDR0ST0RqnRdbpojxdftOtnak9qcoCIfJ-mcX_U1WgTUqZvgP66X_IT1Cgtg5cYRVk6xHhd1LSV0i-COcTRw_UJ1VoGvIHDE_GlCft68xHEbwgLZif283K6t8kAeDVDwKuz7VDDwNM93coP-Ltxr6H8fTNopvA3w3X4KMFsZB2PT0LWCOuYaPj35ecgHHK3MrPf5ZI7SHNSY1OP5vuBBxva_APZ0tuMZnJW2vVNWnd9U5kDRADtjq_zFfDPckNoIP1BH7z4BZPws0-SnOZynzNGgIWSP7vPkvTTPbqEHhofRqqJuzwlP_30oz9OAoXMBqHQEIkAw2Pw71Sbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره:
من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم منطقی به نظر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30351" target="_blank">📅 15:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30350">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cbciy6ijpBJVcYv73-hk2htm36Utxu93EoZn8ulS5xTsYKBFG6wdNgoeVl2s_8L5KlaP6Qoqe16N7RYCeD9BznSWpQzjLw8yMJcMVcpe39pNAB7sAOv6-HgHcqGCFZgXSYk5n1VK1p5mlsSVxbxqZ6Ebguh_7yJIoqomSy5h7qR4BzwpQv05sN-ZslzW64JLZH4ewNaou_L0_dQX9UffyIrAaNPX6mxOpo-xL5KVKq0k_ckKNYDUe489NjvfavF8LJ_knLMDJNld_MGnrMeuA2y0KOIzaGtnWCcIZjcqNg6JsmRZDt_YmkfyVldQfQmqdfKzNQvFq0VBkwyDHFZc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گروه‌بندی‌ فصل‌ جدید لیگ ملت‌های اروپا که از امشب استارت خواهدشد. این فیفادی با فیفادی های قبلی خیلی‌فرق‌میکنه. تقابل‌های جذاب یورگن کلوپ، زین زیدان، توماس توخل در پیش خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30350" target="_blank">📅 15:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30349">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFCTlFaiO0pS59iPT8RWPQpI9nBk17wJ0CYaFymxLPPZmcgElhvG1we8_bhhGqletYjJ_TqGr8lV0wI-hJhnOYy7YdI0_NEaTxSrpCN5uaa8jCWzkdrf0I0J5ltTVWPSt373ULrK1sLkp99tBh7GRKEmQ3myEsUu5MzmR_1mGcDatkbqq5zghfat6JdujVmcXHQZsASmQe7yXhxt7st6kLaep_hxLkHkseQm6o1NGncMw4E4QNg3Qr4ADIU8huEjKrIj-9zYqCwbhvSn1Oy0i0Z7g60L-HBR1H2UfyvFKxaRFMWbWDhzWBN-rmWFTQom1n0RT7ObtHRulNRr06AVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30349" target="_blank">📅 15:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MERT7Gd6lIqw451VtbiK1DDYvX0Igv8vhujckzsXNrIYNudejeFBokSSZ51ph1namIIf4DUXk5uisLUrsgsrR0xnpYI2onaUH5bYA1BPgFJ6aFLe39sQHjTBqjLKs9NCPjJyIrrMDyYaeEeLyaD3kF3B0bZ2Jhw0ZcWVg1REE8Ajy1AB8ixzIK-xQXqYzy41GSYMOIcMpxhpZ1IkIVjRo1DbMtklF-iMJfcKXzP8wK-Yj2IftmRMEzIcf3-404GstEM0rhLEr-a93Hh5yjEmdXhv6ygFOvukeintuyTvE-PR0HZcfF3Oev0kNqGnhoQUngKVhVZYESiN_xfvajZTrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30348" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30346">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmkQt-knSkQR7e6aJXzcmbnEj9lZHYvMVqSOlR_aQcUMuE91tvKrmMgisyzhFEiqY1ARljyCatO1lPbXPwOQWWUtcsn-vHIUZj6Spf6o6qChBQrVEKJsbNiv3NqyD9Wf2joAWXWvLH_bM0ZrtUL1dvNG_zTrYl451ZYfI0SsuyNVBbXsw8Mpy4b9RQE8Qixg9YFCjVEnooLB8ipN911dg6yXkyFBbjnizHenpl7waIYCOOMa-L1HxspsD2TTnr1Z7ylNKqo8va02w7WMzn6Hcf03nYzHNqSNHox_3t9JLbO-F9qTn-6dcHr03HCUoVCdraZiw-afO2DF2YI57WuN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره‌کننده‌وفوق‌العاده کریس رونالدو در سن 32 سالگی‌مقابل‌تیم‌های‌اروپایی در چمپیوکزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30346" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30345">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJZ4qnzaRhaKPvi2aF-6GWZkt952tDHuIfTrSmIZmNTmZ-eXbjTLadBXrOU0JZyhKrbUCWEoru_96bzLbGXR0RZ0VTsBYcwk6UBpAK9UjkDsoUa22FX75sMYqmlxaIC3exHrCskQc8vlkO5GuyIe-KWxhphKDkpN4uqn-qQXxkOmWs6J_kuOc45RfJOZ-854xdn6yv3olE1z-HnIJKcsrLmpbtdYCzFvoU0WnueowMuHKEE4eMP1-Jti0Uci1UbhtkKqi76fvx4q2tA3-fgkpUXtMxoVqQ_IHFn7d8JVD9Kim_43q7OlzdH2ldk0pnuZHmuvj7A2O_107BvEwrwI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعود بنیادیفر بعنوان داور وسط با کمک بهمن عبداللهی و فرهاد مروجی نماینده‌های ایران در جام ملت‌های آسیا 2027 هستن. علیرضا فغانی هم به عنوان نماینده کشور استرالیا حضور داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30345" target="_blank">📅 14:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30344">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-nyasgWYWBSwQV8KdO1hUTSk4miK0JTMPYVhZoz7i-zbkMMJFS_xiwTwIrAvRB9lesFMjWDgMg-3-Fr-dQuUWE7Cc8ZTDr084Zkbz5hyMRgVVey1SZMcJ5KkWv4iJV2Lp0917U79MINr7NCJqk6TnbD2WzxnXaPvpua1t169MHUY-5u2PF0Qr_kFy7z9K10Ww8BbV9L5pCTejipCy6CCGafLShj_qzdun5alt3lZO8AXUXUuC5pd6b1ty2PvO0gioubrX1Nu41DdxvDHaEs8gxfxl1jtWS8S7F_KCEzHzUz6n1t-cO4gwkuAoW_17b5JcssV3EEGvRKehjKlY76jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدیه اندونگ برای‌عقدقرارداد 2 ساله با باشگاه تراکتور درخواست دستمزد سالانه یک میلیون دلار کرده و اعلام کرده هیچ مشکلی برای بازگشت به ایران ندارد و حاضر است با تراکتور قرارداد ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30344" target="_blank">📅 13:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30343">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izlp8sYh3QSvF3RqU2wEIeBm1j5zIjIXZJcCQ1qr8C47XfAP_3h_AHWO2yNOsQyn6n7Jz_LQSSEduE-xtlSuoMIznxga9JKyZ5VsbVfrQR_oD2Smvsr-1U1YoUyzqCe0cjJbsOhiv9lCO4wfuh39TXx2b-8lfOGLkBKEP75dR27i4uyC1YXhtwPJlZ4ZaSIoy43U0IK8gZPb-aMOSKC0TF9IqQK0WM_of9X10SR-CJUlWsKLGriNyao6CkuMtCAxsLjNKcV60DJm21T3c-wqff73AXnh6k8E5uTbv4o24OgNhhOgUumbugSBXIAC1OsqqfJPy5X4GP__JEsr2U5Zvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
تیپ و استایل متفاوت بازیکنان تیم ملی فرانسه برای اومدن به‌اردوی‌تیم‌ملی این کشور برای فیفادی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30343" target="_blank">📅 13:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30342">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ar9D-6Tt2H5hwpgV9ET58MCBcytGDj78ajF7eBn8u3WMwMVPxHSwPYh-i6dZflWRJpTyNwHsYwIgXKAVUQ37zWyZoyiD658H3agqzuNF1R5vOCafU5fg0Q7Xx4wLN-BcgjPP8YtASB-zateSK5PRZWo8frzdHLMhDj0i08fnUK70_m0IbmbUPmwh-Dj6mnBehHyPJytDtkc8PleNHU_HSw4itEsAZmyqcdFRsjyBzg-t5LpzpnFJHOn9eM7zV7FUqdK5cI560lqU1Ih9QhNS-qYPbn2VjR8K68MnauGnvU0XU0aYPH66xNUfs_DSylxnrigzfGnsODYpiyyGoKq71w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30342" target="_blank">📅 12:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30341">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvxJk5ZvXfng4tx9KCMScgO5onSzPabJTitSffapsX0ncjizzCbQajGrGozrlnymfxAmRKAXs87UyIMEUeztugB6vQ5eExbYsDeTuBPTmSx2HF6sAM56lJ_sOfuHjTeGrOVMwmFBoexeRHPCKJlPzT0H1ixs857wuXkF31jv6wBx6DbOW9VU48zNVskmniDP1U3aojzpK6xmuOa0sAMjPFutUGFT9Zm11tEdLwyxk_kMv1XX9d-GQTHU1ABt0PA3J4Zr7pBr_A0K0JxabyFEMG8iNU4GBYmzZEXS33_fhdoFp2_qVK2IkyhtRU2QtV-g4xkG73nHyLLW_6XbahcJ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئالیا:
چهارتا مربی عوض کردیم این همه بازیکن جذب کردیم پس‌مشکل تیم چیه چرا نتیجه نمیگیره. مشکل تیم از نگاه کارشناسان و پیشکسوتان رئال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30341" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30339">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHgvTC4yaexHh_g5iFM_XvwQeC7aWEjjsZpTSgloPrZmd1If5qaI04sGkFoSY2fA3qc9ePgw0b7UwclObuvOoK8u3siveBtxFBi0Y7jBSgpVTB964gJikLGrcF2ovriApUmZdkRne_e8bY9nYHBLFd-eO9c0k9a8gKsrtGqegmlJsoFl9IbTzq3aV5gd7Pt9_HUaBXRe1PrDHGnXibZH2Ik8Lk-cCrbPI_PSKwCc8bElW199hZGl0WbKKIrLz0rIxIoK62CXl9TeAJhynwfaHeHmEy60HKMKNsmsimJqxFH4CVVRdbG_lJw0tjQUrpEdgc1T0jQVWxfkdCWK0awkFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛ تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30339" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30338">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuOtIgX19D4UkmaQwG-zl7uhSG9AW-y7mojKRnFX0Hk-yvHL8hLpJ_7nakQ5wQpdWtk31NVW1SZQBUwEvtlN0oo5uAuK5hHg0GkOYhdwfi2kbE1GnIsTGq24syvmQDdzJ4PAdARxpdOjsXZzdfzpp66hZou5DpH1xpmggEHQ53DeG60EHHJoDAcB9kW-DhoOnPM7pz86hiDGJnI4C1mPXQjf2h7YDB3R0SmUe5LIFG8obQ5PNQJnOjrqbeCYmWaa7W-4YoLJr1ARYU-55aHgYbCBSoJY3-hBQBVB4oXgnI78GqxtVYN2OwJwB24e7Pdnqd4iMQQsgyYjHeEwFmRPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛
تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30338" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT4GY8jViNtZgG5M65sb_QlEMOKJf07o0J4ebwhhawC0GMx1neXh0Eh8YEL4ZI2CKOnaf73954cV5QdofNfHmGlGCRWdJFXTCj5PAmWVeXogPk_rUM0IV9XIjH-6T80fxkCYHdEoW3LAmc13b5il9W4OpkpTzCRn2poN8rzbM1qY8l-iiHTPMY9Ud-SpLEFCiAwzOReoikELw-T9d_bBEJCbui_05eqEsg8mp-Rbd_QQiAmGgA9_HxgxfvpmLMzqrEMQDv5bKiVD6MuAESVQimlOM4XKnbFfoj-87rg-fx1BqIwK630MJyxxY-H9UB-gr8irzPB-gVtWSkMwv_K0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رونالدو 101 بازی بعنوان کاپیتان تیم رئال بازی‌کرد که رئال هیچکدوم ازون بازیا رو نباخت‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30337" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30335">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPuwj79NWsZHcOvCzUgic26bkgql5KALUczhTBdiQlhR9ocfdNEY0fd1OrXlW2HLD-4mpIuLu_MRFgjaZuZEzU2OG77LAWkgil2WbbSsy8icA2fv5BsJV5jdbI3Uxx7p3gJHUsNRxJo3ePPu0fEJh0mVjGeT10O0sNUHFNULr3Z6vTErYudOEfpwNHWj0URFYcuO-I9rJomb7eXXJfNLOQknBZaimVFjumCrxl39efwsazG7t34ky2K-HT1eWJZEesjT5Z-bdrmdnwmgL8XEGCo_-ThEvP5yIEU96uGtA1QFai1QuWbUE5qehwwtxgUt2seHDx9uZc05BFemt_duPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سابق سپهر حیدری: من زیاد اهل فوتبال دنبال کردن نیستم اما در حال حاضر بهترین بازیکن ایران چه ازنظرفنی چه شخصیتی رامین رضاییانه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30335" target="_blank">📅 11:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30334">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4VZdLF8J3XnAgMLBKSyus1R1RLkC-iLh_dLrKdJrHkcvlJ5dfrwgOp0Si-hCG9TjcepTvB3N3IUJAQJRYl31DQJN1sef9rH-chcmE0bCqeNVOm7NrrD4p11mJsfYgK7oa_Uw2yOmKML9a_hG6m6WR2NRfxyoCb6yjZuklPBhydUL6H_vMh1XOIvwdoddfL23T7Y2-H4L7uOOBMHGuHcLUEXCz_kNTdz3VR5xtb5xWxTiKQ3LfthgcNcyDym5xMZ8-dY71L2NGzR7_4gOHBA0VDGmGQiv2kBHRPU_WsuF0HXSUoa47I5iM4Npb1RcjRKGlp4jPpdAxhIIhfAQ042YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعد از عدم علاقه مدیریت باشگاه استقلال به برگردوندن دیدیه اندونگ به جمع آبی‌ها بخاطر مدیر برنامه پر حاشیه اش؛ حالا از تبریز خبر میرسه که ایجنت اندونگ این بازیکن 32 ساله رو به مدیریت و کادر فنی باشگاه تراکتور پیشنهاد داده تا درصورت توافق با این باشگاه…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30334" target="_blank">📅 11:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30333">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=njvJmi8XVLFDQ0iH8WTMTeGNVsI-gthPqHWHVLpDHhJymhEjwkZTPE8x-vLVK1wXLMKepIbtkXBEIe3hntP-r1tg0iOrVQCkbQkhVwq8F-3QqlSSAeQte1uWdKoMdJw_igfxGQXYDThD2Lcr7V5tQDlphhTe0QVvNeYyWdf6F0rpejSMfOCWxW_dYw7XoWtQYESCJPAnh4y9j_EYCtgslEVqUnf3fu7XqEIc9pVFIMOaf6GQPi_UmEw-TRzrU1BQOxPWYtBHOrbiUjmFKwmFI1Od0rYJmXobymEKdekq1bG6o0S-Hg5HrFSW8owOpXIS_s8BKgysR5-7mWLs6FUue4bm9md-Dtl1y2ilWMsIfKXFD1RNpbRzqU2-UKv42YaKde4ZiwRKpygQS-Q6stpi5qeVAlZEqLObPyTA0jpQITpwU49z0v-AozikaAFcVnrW1jH4G-tMEN6PV-hXJehBl2maI6uY6wjcthDKgaZAMe5SbS6dG-FkFRcBzvLFpI2242Q9wVDVAJJWqY0PJvWgh5fWcJRFh_owYqMyvWvwYhmqabsnuK4kfq-1qy-f2D6WBrkf1HWoE85cSSRqTIpI3yQ_j_VKH4t3LdTlBXulfLqOA3ZDTEccp7-8phOWa5o8OkfKumKCcFl0k2FWgGKHzaHDOZSJVEj_pp-BaGHVC1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=njvJmi8XVLFDQ0iH8WTMTeGNVsI-gthPqHWHVLpDHhJymhEjwkZTPE8x-vLVK1wXLMKepIbtkXBEIe3hntP-r1tg0iOrVQCkbQkhVwq8F-3QqlSSAeQte1uWdKoMdJw_igfxGQXYDThD2Lcr7V5tQDlphhTe0QVvNeYyWdf6F0rpejSMfOCWxW_dYw7XoWtQYESCJPAnh4y9j_EYCtgslEVqUnf3fu7XqEIc9pVFIMOaf6GQPi_UmEw-TRzrU1BQOxPWYtBHOrbiUjmFKwmFI1Od0rYJmXobymEKdekq1bG6o0S-Hg5HrFSW8owOpXIS_s8BKgysR5-7mWLs6FUue4bm9md-Dtl1y2ilWMsIfKXFD1RNpbRzqU2-UKv42YaKde4ZiwRKpygQS-Q6stpi5qeVAlZEqLObPyTA0jpQITpwU49z0v-AozikaAFcVnrW1jH4G-tMEN6PV-hXJehBl2maI6uY6wjcthDKgaZAMe5SbS6dG-FkFRcBzvLFpI2242Q9wVDVAJJWqY0PJvWgh5fWcJRFh_owYqMyvWvwYhmqabsnuK4kfq-1qy-f2D6WBrkf1HWoE85cSSRqTIpI3yQ_j_VKH4t3LdTlBXulfLqOA3ZDTEccp7-8phOWa5o8OkfKumKCcFl0k2FWgGKHzaHDOZSJVEj_pp-BaGHVC1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری درخصوص دعوت‌نشدن برخی از ستار‌ه های ایرانی به اردوی تیم‌ملی توسط امیر قلعه نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30333" target="_blank">📅 10:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30332">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f00468324.mp4?token=D9B883QBZTC0AWLtdBVat6zKf6NMgifT2-uLvOmJLezU2PK-2r2TMUi-X7g5Kn-nsnuCM0RizTedIQAPHfPadjrSKT3LbtdvpxaXxRKPpEsqlsscwsebWuv7js0UBnZi4XBUF9IVl1R0rwvSGlmLn6AkU2AYarLoCHG7ya9kBVcQ1awRiuEuWoMm6MV_Dl9iYgU97S3y7z5IMhfD4zEC05sK5xqdOICrwmMHCYpnZpMFdwIeA0irHKX8R17fBE2NojV6bOvwm57BzTkJ2W1GaxMzTC9U8uU8BgchqFgGi48IFIXcoCc3pIqBH_MuRwmPeB-0sAvPrwkllJKI3bjZUyXj-GPrXN45gpYUd2qZaHSdh2hDgVWhsC5g0ZemO7uCcweklv3keJj63PEiu89oi1zjaoGYAdzBEnBPpF-fhc7Sfqt57ubDD6f0xLx719LCq7iAaWkNXCmPuzvURJNOg8Mba7GakMTEOx65Jh_BAh3O7i5Y1iKZzkwaXLRGsqICgAjmjqZXasJTzJUa4bdroWfXqNEap3Egmdxf57KVc61witmk-SrPoVNeeX8jQ_GeiNVlCKZ81z0aXPPK9OQ8SQ_2a8aVnvejOolNHbwXNhVI2n-ziUXn9AkPGU1qsVdu6GVcpXw8ofE9X9DRksudWfUMyKvE_a4wuqoayJuzlhU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f00468324.mp4?token=D9B883QBZTC0AWLtdBVat6zKf6NMgifT2-uLvOmJLezU2PK-2r2TMUi-X7g5Kn-nsnuCM0RizTedIQAPHfPadjrSKT3LbtdvpxaXxRKPpEsqlsscwsebWuv7js0UBnZi4XBUF9IVl1R0rwvSGlmLn6AkU2AYarLoCHG7ya9kBVcQ1awRiuEuWoMm6MV_Dl9iYgU97S3y7z5IMhfD4zEC05sK5xqdOICrwmMHCYpnZpMFdwIeA0irHKX8R17fBE2NojV6bOvwm57BzTkJ2W1GaxMzTC9U8uU8BgchqFgGi48IFIXcoCc3pIqBH_MuRwmPeB-0sAvPrwkllJKI3bjZUyXj-GPrXN45gpYUd2qZaHSdh2hDgVWhsC5g0ZemO7uCcweklv3keJj63PEiu89oi1zjaoGYAdzBEnBPpF-fhc7Sfqt57ubDD6f0xLx719LCq7iAaWkNXCmPuzvURJNOg8Mba7GakMTEOx65Jh_BAh3O7i5Y1iKZzkwaXLRGsqICgAjmjqZXasJTzJUa4bdroWfXqNEap3Egmdxf57KVc61witmk-SrPoVNeeX8jQ_GeiNVlCKZ81z0aXPPK9OQ8SQ_2a8aVnvejOolNHbwXNhVI2n-ziUXn9AkPGU1qsVdu6GVcpXw8ofE9X9DRksudWfUMyKvE_a4wuqoayJuzlhU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های محمد احمدزاده سرمربی‌سابق ملوان درباره سختی‌های عجیبی که در زندگی‌اش کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30332" target="_blank">📅 10:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30330">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGNFrMDhIzssxUola_goYX62zyK9kUz8tMQKcPT6uibkaVUGpWv_mva_wqmZOT5zhYYWK8N8xgtqIQS0L2K2CBrot1H3KpXsNxBXv_7AuFWeJifzfUoc8WZAxhonqn_ROaqnCQV-MizCwwOH-Tsy3Qptkc63Own1xyMdyBewr1QuMp6dY_wE-RTXXc1MKqOmQ3X9fivA_2BjWGNrqsju3QFU6svxFBSjBzIWhRC2PjHK03_v-L9JoMytzCNoOrKyvHLwCasnOe4ajWcFZGl3s9qxY_jf-lPSFAouBDfMDSVSEAs4ltghzzl0_RHfw96_ruWqCaMCh1nl9xOeagRXew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BA8JuV1RUK6FwW71piXNSQH5RGZkR4aI393Uz6KdFW2w9lv_WwVLXmzmax3wAtMIX5cUL109ZBZ8AGvtUIOhx2uPoRt2ELhF1tmwKblJpY_ywaIaIQxX6uo-vbF6FIFqz8RUC2oL8_b-UY-ZyrWgQdzFjkSERCBqeitWL7RgUfAMY6wtqJVTE-R4W_pcsV2d7b3wPUfbuwRPCM0F8lxD5xeIfn_F6lrBi7LGrSN54MtBsiVXi0BHK6y_RciskEVtGKJdNOVl10IoSYN-p8CyBIgB17_tMWS1qrGdEFkTJBVjCgN4yhhJSnNU2GveiWEQY_F6ELu6S7_SOiS-ODgEaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
فلش بک به سال 2012 زمانی که:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد 85 گل به ثمر رسوند.
🔵
پی اس جی 86 گل به ثمر رسوند.
🔵
چلسی 87 گل به ثمر رسوند.
🟡
دورتموند 88 گل به ثمر رسوند.
🇦🇷
مسی به تنهایی 91 گل به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30330" target="_blank">📅 09:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30329">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79121e6f5.mp4?token=GaFZs4XwCzeYzM3ewLCbYk3j5bNyXhEpOAhYGQYX9lJVhE56kapreAt15v0w-UEPU71rH7ObPqsUKodsfZHvJVL4QcHTXUBgibo4rcrVqbtq2GrwR-sAbdtwjn3ymC6jaCrZzNo4pX-HeVDhBZCTlxSzabMCvaiitF1UhWmBkjbQOITY8_uV6jBQBskB63UqsF9wsqO5CSOS2_VkRogNKEVbTICeYHZXnpMrUFievmuaUaiJ969hWoraxbZMmTJUclAqmE56oCKmvnZdzi562ps86hy_eA5N5nZvuEvesldakySJXDiZuwjvuFbzoFPOCwt-SDLqmX_HFTWes-k85Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79121e6f5.mp4?token=GaFZs4XwCzeYzM3ewLCbYk3j5bNyXhEpOAhYGQYX9lJVhE56kapreAt15v0w-UEPU71rH7ObPqsUKodsfZHvJVL4QcHTXUBgibo4rcrVqbtq2GrwR-sAbdtwjn3ymC6jaCrZzNo4pX-HeVDhBZCTlxSzabMCvaiitF1UhWmBkjbQOITY8_uV6jBQBskB63UqsF9wsqO5CSOS2_VkRogNKEVbTICeYHZXnpMrUFievmuaUaiJ969hWoraxbZMmTJUclAqmE56oCKmvnZdzi562ps86hy_eA5N5nZvuEvesldakySJXDiZuwjvuFbzoFPOCwt-SDLqmX_HFTWes-k85Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30329" target="_blank">📅 09:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30328">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIZQXy5JzyHz74ijCQ6KkiedmfhGwjqeVJfZVlPM0vRJ2BCbvdfdYTyvC3X4a1-karYGFeDSB63-qvQIGCqPLbCL2t_wwY7LMmggxCc65FpQwk0WUQpzNm4bbm5vVNuCZ_GxgeWT1btqLNT4QYN-v4KK4PrGjh7RtHGi2LeaCaMIOmQ_1h9xR6BfBp1hNqNZauks7xpGDk92eh-98jP7lc1du3OeXYwRVqJnjprY6tJqGLv5XBNzunNKj92ipAN_He2uJ3_zM1HY5OccxwUSFKM_UxZtI0symVwlo_lpgmcizhvAd27b9_OCa-kEBN_rreK1BjkDxinS7szXoTStNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب ستاره‌هایی که علی رغم درخشش خیره کننده در دوران حرفه ای خود توپ طلا نبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30328" target="_blank">📅 09:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30327">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0wyUMP8MzhNs4LDduhtMw5Uqhlv9HaEQ50uGzpYnB6ia5Y_Q1Or6bjj6V1QXLMny8lNQ1NoR_L6m4RZgDY_eSbLH2e5LNNeQyBhKMLake6HDQ_SkvUfg6ZhQlBZ2VpLNshcDUuwE5U8C-3Ffpkw1lLR6QnMCET6vc4STIPFdsQdGKP2zW4WHJOuv17U7NAVLbokUKhM-bLT4DACyIP3yYoLj05RjrCF_rqlanHpJH7vFdP3a0iP2Yl-acuEwInv31G6wClVQvQV_oDzCIVETQbOJRQbqUbHXqUgj8CQMm0QH5C8kpvGmoyqMChha_pARScdC3NGv8wW5W-sYir0cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30327" target="_blank">📅 01:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30325">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFb1q19kCkYW_8mIeNmRdbVJZSIN3uVgWVtZkN5rYrYOdK6GktQjpIJvlDoGYxGsTEqZDsVZ57FpDfTsMpm5uqnLJ87tcttLhMAzhoErCSGYp-6-jCjL574HLWz3J2uhnYHlD86Rs8JTe386IA3zF-hdRNw0StCU_oFg8opfg5qOhyaXkFispqAOeRPfPMfqBAQnwX0xr4_Si-jIzzVJGVnsrtXqMe-Ev0LNZTAR13PnUdDDYgU_4HpSp-xfyT2X9a2dl1kZ-o0YUH3xcrQzYnUqlHK75h7dW25IiipIPuwBn90lNerQtbxI36Bx2OWML1qkax8o325LCgQFvbVKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTCtW0uOUlOV8HNH71B03aeH2XxZtpj8UydyJ5-7l06YgS_cB7u1Mf6zD_r76mOvMATQMPmtn57s8k23UHodIy3bM8PUTAaeTiSLxNN79Yg2Gh_5BgL0poyg9FoVzx2Ggbsjm9xSHUf5BxfJwiMkYVe1BM8ebC38mtiSxHpuHLTODyKP0CgXqrapDWDIn9HFDetkYytBoKUfT2hQlKX73OzMvrVczs3UHzi2kR8CsN5DnaLqJE3UczXjoETrffmeYvWEuSED7VVi58qIXZnYWD5Hjue_NfuIY_PKWsp9sc5MGWSpxflts-1C2oUCbJV-LX62lpXCglhq0HZxmF8jlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آخرین رنکینگ بندی تیم‌ های ملی پیش از شروع مسابقات‌فیفادی؛ اسپانیا بر دنیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30325" target="_blank">📅 01:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30324">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=U1O07gQ7oziZwuSv_JRaqeZg7GFByChTziVCtB14MAaZD9LboH0r06-WslgGrqnWFfCGpXuXNCwrcZZ0xVcLy0m_ostFj5FYunhKD9UXL_JNkHJDpnu1PTAWtnL3RzUComMXrukiIeh2Tdnpj6im3KYSwFgO46waV7wXHpmWUH8ugSUQEKLbNO5ZOV1l8TKJ-sbXGV2PNVFht-jFwDAANalEIb9qFIY-P4XXaqrRiDB_90e3hy_wb9VO6S8M3TQcts5D3ZNA8IQJo_XylS9ZEDWdX9seuTX9j8ldOfxeMf-VfT3JJS-MEcVGofxipYTeROtJo9KW9lkvpazsTrKFuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=U1O07gQ7oziZwuSv_JRaqeZg7GFByChTziVCtB14MAaZD9LboH0r06-WslgGrqnWFfCGpXuXNCwrcZZ0xVcLy0m_ostFj5FYunhKD9UXL_JNkHJDpnu1PTAWtnL3RzUComMXrukiIeh2Tdnpj6im3KYSwFgO46waV7wXHpmWUH8ugSUQEKLbNO5ZOV1l8TKJ-sbXGV2PNVFht-jFwDAANalEIb9qFIY-P4XXaqrRiDB_90e3hy_wb9VO6S8M3TQcts5D3ZNA8IQJo_XylS9ZEDWdX9seuTX9j8ldOfxeMf-VfT3JJS-MEcVGofxipYTeROtJo9KW9lkvpazsTrKFuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل فردوسی درباره زندگی سخت یان دیومانده ستاره 19 ساله رئال مادرید در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30324" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30323">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=NXnxT41VygTcAO1oA__250DI-l5A5QRMmIaQ9OtqpsWxRlpHQhYoRB_XH-PH5CK7OVDE8IPg6mC3nEkE2uD5_6r97NgrDmpLy3pJcoobo6MVAWhnixh1trTvLXRQmQtUH6gRHNBpMyNcgEvdxkm03SDE2Ml7K-vsPd7I1LpaUJ9j4i2HBDIlNmAmt38LcNZcOehC8i1WdyYflaX-Uvp62vfX0W2cnz2MTUueqHEmuLC1kXWNPYhg8fySuy6cK6fIFDcN3hCXnrhGv3dYw3J50MYq_bkSuE1E_P0gE4dtAr8yG2rNSvxAVyb6A3OAyskMxql_m8Whal9ODogRSp-Ugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=NXnxT41VygTcAO1oA__250DI-l5A5QRMmIaQ9OtqpsWxRlpHQhYoRB_XH-PH5CK7OVDE8IPg6mC3nEkE2uD5_6r97NgrDmpLy3pJcoobo6MVAWhnixh1trTvLXRQmQtUH6gRHNBpMyNcgEvdxkm03SDE2Ml7K-vsPd7I1LpaUJ9j4i2HBDIlNmAmt38LcNZcOehC8i1WdyYflaX-Uvp62vfX0W2cnz2MTUueqHEmuLC1kXWNPYhg8fySuy6cK6fIFDcN3hCXnrhGv3dYw3J50MYq_bkSuE1E_P0gE4dtAr8yG2rNSvxAVyb6A3OAyskMxql_m8Whal9ODogRSp-Ugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چالش‌عجیب‌وغریب‌امیرحسین‌قیاسی در قسمت دوم برنامه جدیدش با خوردن آبلیمو با غلظت بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30323" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30321">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psgZzoj9i1JsJsxY8kk1PNHHpSdFalEqJTrpU7P47xcsh6myhIp0uxDxNoDllk2nuuZ9mcvpu1ok1Bx--XeEvnZlskJpZ3F2xEon8fgLPCDLFb-lO5PfqC0MembHEZUGckujqpZfYOht2RhuTMfi5kul6MS7uqJLb6RdvaD7X1zAZJq9HoTadldm_XQ_0DPO9aIqbRRcnx_WJJA_PMtp2bVcL8bx4h_qcdJhBAsXbGdUg5O9VP-KdrZACmWyok9CYMYRafFLQhTAhBz25rt522LDfVj2wGAAntxXCVu0fQBoqiMBtGPR2fQq8ZXOwx8ftu4ysdeAdqudhE8S5f1qkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30321" target="_blank">📅 00:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30319">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urZl5UqdbOUG5bxyHmKQf9m2w40vJlpC7-sd_EH0w4nieS8UYzbNykL5zgWBQkv8xNdJmoTsjh2ewcJMq_ErSYXwaVy3UcrKKSgfnz3DKzzylyszT2fBuSlX522TRb8vcBVYopX-2g-4GDZBDE6bD3P483zUN0m7Zkd6RvAF-PVzTx7YbMQQcuv6UsVcqySoVji6hPfnhLePuKDBUnpF7aBzlP4k54gRkgAFRjU5a2Vtc4NgKucXa8JJ88xRaS4y5R8PN-d416dxRARdLhUHQ8sEoFjIRS0T1p0GiB6ZSKq-Px6zhzwYlXefC9BKZio5No1wEN79wwtm4mkLWbnvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30319" target="_blank">📅 00:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30318">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvTAE_aIEsS3BFXT8fOEKIFOy45s8H38s54tMl18py0W8mubwbIKbf4kSpuGl4aUQw1plIKHRUXTs3nU8skhoPZfB2HWeg2UCo2gFjd5ZRTbVlDbvOpuzGSiXtEIoqackOWvEg0ZkpeS4Ule7vZ9Z99rpZx2fcpEsE3W_KZu3qkRzV3W6j969FqqcDMQYxKk-dR2QZMnkM2Jr3CoXybOC_a_au-22goWThirArphcYFozk_4WCozitkoDEP8NFnzPEDmI-GgfFl9On6Yi8d4H9Pz721HqMUWJWs3ZXwrM7EhhidCvCQvZfozG41w8xUks3SsBBpvH_g-xDvMe9_t9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌‌‌‌‌‌تنهادیداردیروز؛
شکست‌مفتضحانه تیم امید مقابل کره و حذف درمرحله‌گروهی بازی‌های آسیایی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30318" target="_blank">📅 00:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30317">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqNLoOES_6P_db-EVCD0FaNITt-awC_BPdQKlNud10MoavSbYwOHZ9_xKYQX5cc6yGZmBY9jSvCrG7guQQWUAw7CllK48qjsUGDeZUcgLVGRzvMfnMY4Xy02aQjJjvTGymw_U8oYlaRWaQuXJpFZl3HctyqZJOfbcRXAzun9Zi6AQhRf41G26cfGzmsYcdJyFLXFLGlNEzZC7U02WqThS5vvnpXdN-bx-NNP75tKKBOXS-M_jk5qrsaS75onSr8QYqSR-iiyrj4_l3QFWQZY9FM7kO-2KUPKyElQR7lfBtKXVfGKE8hHD-FpwW7OAZrbyVUR-3nyTJp0tiWMk0MNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
گل تماشایی ابوالفضل کوهی در بازی امشب نساجی مقابل استقلال خوزستان روی حرکت انفرادی خود؛ کوهی درآستانه پیوستن به سپاهان قرار داشت اما در نهایت شاگرد مجتبی حسینی در نساجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30317" target="_blank">📅 00:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30316">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=ZMT7f0f30uz0416cpuYtx2SF8XNzgMpwMOOT5mOLpjYjSJrlZ9mD4cHXrdecog6hEeFNtWG5FoztrancF0wurAZPwDYqERsxmXoWxCzvh7BTbhVK944SSM8itik-UmK1rCnMO4oxSNWJML9KzCW-BTAPWbwHfltysZMD3MsrpUn4Z4CabmP1u__r_rB63yvt_kHzN6b8Gp85UBvM160SijCA6m6A-a5x-W2sDZGWSFGe1FxfNF3f_R0RTGPmYPHlL1sOzzIiCVlyrFVPaqB5EeEJmxssONtDbbFim5C-SN2Ydeu8RiMIKHvvl51sjlY9aDkBTZXZeZdqUhoFK9dX4JBUscqpSAyX7nM0wz-s79Xn-zeofgC0uJisIazolxElMNxC66nUUI0OF_yYDLxLDDLNpjMckhr1tNJuDLhylkOx8ME90kh9bZSuqmUzL-um1294dwUHXBekAtKUQ2irysx9D8zX2MQqyTwkQXDR2v15gmncMAuLykMeZcOi7lzg45Xu0n2vm0CZ3p8tZhtZDAODXN0KokknDUeXMVfXvbp-Qxcmo--yZZxIXHRFjiCH2Qms2P_leML5yFyuWL9_UQcyqjXiXrhwOpT6kzYHXwS8EowlbaDV6rAho9xo9J1QDN-6OgC-rRH6PlsmwlYops3eKKVshOZ3mccs6dqySnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=ZMT7f0f30uz0416cpuYtx2SF8XNzgMpwMOOT5mOLpjYjSJrlZ9mD4cHXrdecog6hEeFNtWG5FoztrancF0wurAZPwDYqERsxmXoWxCzvh7BTbhVK944SSM8itik-UmK1rCnMO4oxSNWJML9KzCW-BTAPWbwHfltysZMD3MsrpUn4Z4CabmP1u__r_rB63yvt_kHzN6b8Gp85UBvM160SijCA6m6A-a5x-W2sDZGWSFGe1FxfNF3f_R0RTGPmYPHlL1sOzzIiCVlyrFVPaqB5EeEJmxssONtDbbFim5C-SN2Ydeu8RiMIKHvvl51sjlY9aDkBTZXZeZdqUhoFK9dX4JBUscqpSAyX7nM0wz-s79Xn-zeofgC0uJisIazolxElMNxC66nUUI0OF_yYDLxLDDLNpjMckhr1tNJuDLhylkOx8ME90kh9bZSuqmUzL-um1294dwUHXBekAtKUQ2irysx9D8zX2MQqyTwkQXDR2v15gmncMAuLykMeZcOi7lzg45Xu0n2vm0CZ3p8tZhtZDAODXN0KokknDUeXMVfXvbp-Qxcmo--yZZxIXHRFjiCH2Qms2P_leML5yFyuWL9_UQcyqjXiXrhwOpT6kzYHXwS8EowlbaDV6rAho9xo9J1QDN-6OgC-rRH6PlsmwlYops3eKKVshOZ3mccs6dqySnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برای اولین بار در 47 سال اخیر، یک ژیمناستیک‌ کار زن ایرانی درمسابقات‌آسیایی شرکت کرد. هنگامه هادیانی؛ ایشون درمسابقات رتبه خوب 13 ام گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30316" target="_blank">📅 23:48 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
