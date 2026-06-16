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
<img src="https://cdn4.telesco.pe/file/ZST8GQZAuGoKIuxjVOLrbtnEh3uQLdxfuR56-qfImCCcl5kP7H3GM75I_bUzFX45dIVegsX43X38u2d2JKVKRcg9PsMgrhDv62q_X_yrgZfseSj-sJErCUdot1hhgdl8OLl7uFplRqAIE-0JE1mZJRQd7ssKNpVyLNghJv-KloKyDsSEbyndRQLbdGKDR1tGK_XTSU-kPk0xX9Iu-aoVtgWcWIfcvOVuFOBST6-7FWt9lQh2nepth3nZEFLIrZ6Y09LT-V6l82zQk5Y9GTMKO240WoMOxIi9OJYHeUQcFqc_-Lz74Denl17TwXLJiAexc2zS2a6paYGZOC24RAAerg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 301K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 21:43:22</div>
<hr>

<div class="tg-post" id="msg-23625">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6CALQ49RQhjnI_GxaP3_A0YJ5dr0rH3bL8hiRxtRMp8gga2XMUqxBYdSaMiNK8DolfhA3ntgB5lBhUeURet47jpjH4E46nnEnbGMTCrpzrP4ePkzPzMhfFYaW5gGyeJQMbF--zLfTVOI5L5fYSL69MiojM0uLJfv4l3-nUAxdyPL0Npk3ttprub7KsXaPoy9Dgg9RwUIPeLhrZV3IGOPoDzgUg9Fdaj4N8OeGQWXIyTbgpxciZuSsA9NFFN0XhkwMknKvBTXrGkF-kBKXjLMmqXyuwTLEYPeUOwtdvT-C7DAEzgH_hRZDsFUD-KmUMQGc7ptrRjgHawDrmiBgUOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/persiana_Soccer/23625" target="_blank">📅 21:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23623">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uPJXn4yB1BKOr3qVrxmdWPasl45wLrSj2Z8LMXW9Q0AhNPU702OKn5tsa5xKIn_a01Is7P92bWWlV-g7Np_Rt37rCcLO6anNKlRFlVN-Z5fvIGZtuVN2ONLc2Qt1eWQ8tr3HbXlooYG_CRMxy194eX8kGfQZLxkSzy9ipIxc7nMR2FQlCuO9imNTbNC5NR5-T_ZN--cYFCYA_9Qfwdh2ri1lRBejLtNIn5Bph2vmbLEbNcWkmrXHuH9KiZkh7vc6z7PqLP47TstPziCHbWYuw6u-S-kyZ6KUFTAT2nvM68hwBjdgjLNoIwYuzQZJXbDTVWsjVcj3fsBX07Mt4DVBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5YHMOFPLL_VgRGDgIQ-QJ63MyA2TyUdvh-s5L_oxmFw8yIg08_LdDG7j2wqNk9vxxf2pECfLEfXUfmrk6O7CM9gwbNT0xLGB30bU1Y0DlJnS5ZfhJw-MEbrH8Pd3NdLlO4twD7w3Bykdqp7QjVKFhH_ZaV5J_GoM0IVjfKek1zA2EuKlnTI9PCxoGkxsjgxJT_rbl-_ssrR6kseMUBvCTWPqsYWTVRnGimsfNeq4AkkRyekK-oM36Q-8wFi2ioQ8C-F_fgdssGjbrPDeLD8kHA8X9gJ6IZi88Kv_6tbVEENXrsmd2T4KmrbCFPYHbpkGo8zIvGkNv7WX6Ns15x-1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بازی جذاب امشب دو تیم فرانسه
🆚
سنگال رو عادل فردوسی پور در آپارات اسپرت گزارش میکنه. روی پست ریپلای شده اپلیکیشن آپارات اسپرت رو گذاشتیم اگه ندارین دانلودکنین کیفیت پخش عالیه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/persiana_Soccer/23623" target="_blank">📅 21:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23620">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwUcDN8jEVFXgueHPaPzvA64GAomCIPrjPJr1zbk8WIfKuxSoDgqWvQjcHqwpkXva_1lXLO5xiwYZgyij7x1I3CnfLyfxmpc17pOiqsPp45wlqjFa6QMq8VaWkIOa3QZhmk5vlR4QDRMvKGunt1_2LZaHd3Wv6j1Ytj_MEQ02I1KE-IaH7je5S8rhNvlyXZKpGVhrmc14MY_cUe22b81ulecnP0EMrW-GsUBUZbrm6hoyDN1tRlLmLfRwCzqOfVvAjFv8ucEcFcK2dmXa44_qGPWvVBIAUiL6U44pHCKoJv909zTFNqZWOW5nLa0bvTjt6czVD8ZsGBBBqMbdyVaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/23620" target="_blank">📅 21:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23619">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2rmGWA_L8nAOt4cHnCqDFoJVFhjZKKgnMGfXFiUcR3mAiyQeGkfHxAO3p2CjkIWjv9TaON2b5NVzCgkbwfaGdNwG87EBtTEUGn-XeAgpCZMl12YAC2AtzklRelGN1S8nT_8fv_FMOBMvDIxQuUvOUvB3kEKklut1WG8Nt19iqsaGwtYxyP2bjkaoH84GLN-JgYzGjkDAGAlctmdxLNqVnxRcQpC05sLcUUzuhZX-vp6fm6FuDUdi_gsjGa-U_XTL4vPDPtjva_net_tNUvTASZN7ngwVLLDHVDb1GLUoNWCEbTwTHlpALbuk2uI4Z1V08YoyAZHSW_i4180H-xMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بامخالفت تارتار سرمربی گل گهر؛ انتقال مهدی تیکدری به سپاهان در پنجره نیم فصل منتفی شد و این بازیکن تا پایان فصل در سیرجان خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/23619" target="_blank">📅 20:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23618">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335ba40687.mp4?token=axY_azJ1U4q3oGFEdh9y5xvD6dcB2IJCKeZgLMdZ8pMtEoKT7107b7dK-4jOCmb9V8pv6xw95LHxT8nTIyGGsbZBjwBfDGb8FadMuLF9j40fCbjVTLBM8KY4enrMj_uw3NS44VJSXhcM_z_54-oGuL5UYlizyJMnXWBGZty8AyvjHOakOTLLtvuW1bGCDC5BqmDEQE4iQhxdsjUIZPDOKokqBCjUePMAzCgfcbPi3TPGoRr5IQigXSr5L1tzOheOYYujWScbV3yn3nOXCQ7svUOETU3ktw6x1a8TAsNuEJOBWLhHGAWkuLIgMt2QtNk_cR7f9BXNNas_15w3P5TBkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335ba40687.mp4?token=axY_azJ1U4q3oGFEdh9y5xvD6dcB2IJCKeZgLMdZ8pMtEoKT7107b7dK-4jOCmb9V8pv6xw95LHxT8nTIyGGsbZBjwBfDGb8FadMuLF9j40fCbjVTLBM8KY4enrMj_uw3NS44VJSXhcM_z_54-oGuL5UYlizyJMnXWBGZty8AyvjHOakOTLLtvuW1bGCDC5BqmDEQE4iQhxdsjUIZPDOKokqBCjUePMAzCgfcbPi3TPGoRr5IQigXSr5L1tzOheOYYujWScbV3yn3nOXCQ7svUOETU3ktw6x1a8TAsNuEJOBWLhHGAWkuLIgMt2QtNk_cR7f9BXNNas_15w3P5TBkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
#تقویم
؛ 20 سال‌پیش‌درچنین‌روزی؛
لیونل مسی اولین بازی خود را با پیراهن تیم ملی آرژانتین درجام‌جهانی‌انجام‌داد. مسی 18 ساله در اولین بازی اش یک‌گل و یک‌پاس‌برای آلبی سلسته به‌ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/23618" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23617">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3B7H9xmk3kekKFAzrFRaeq_8jp1cx8CJBi2PuHQrmQPyUrYpQJibZF4WwRVrJXfl1IOPQFDKjgmS8B9QA0lrahlg1OPz7b_uNjrE7yeRgJCslKjGmswYF3l3d6eNMxZU3wGilcgm1D5VYgNedcsiI-g09DUs_-9Xbv0r4gJNxxvdBhs_ZPOwrE6DrWiTtnEsXooEmAWsYN78P0f1R-OK6s69w9xUs-_yPw7xBfgl9KBztFfFaACOiCi6Meh_eB08N8VEH9yOV0bbstM_FBoP3sWH9f7q7dtwB-9S-wCfItP78jxvveccKhVkf0e5eduDxtITZTRGEwqvNu4plZh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:  2014: تنها یک بردمقابل استرالیا و حذف در گروهی. 2018: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی. 2022: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی. 2026: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/23617" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23616">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPzmOas3jpESLGJqlYtgoP-K8yE3ldLacMIoepkC2pXWmGKdHHBzVrBiixVfXUl4X4FT5V4gAlNnRcdLEEgE4q6N3sHCiAgBRrE1x3IDqqDhAalg77AMurNrTd4tzhPCabdQ-WQ_zJPh2yUnj6l9ewp65nRqZY2Z92yNHbec_Q_NOXi3xzCTuH_bpKz7cBXQqbrwUh6XnyFfPoDarCamMpEE-3LR52vnIqrXr9m_tWj4WMP-pDDWHhnEft4dp33fgWNJGhTPK-3gWsYqj_AA-eNyI3hCR6N9ZV7LlMeJkn-hx6Ehradc9Q7TyG2OhgPul6OBcWKiCVaTFp06oo4qWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/23616" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23615">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G57ahAZhoEbroXyD0ofi8677z4sjNc2rhLWQVK4T_q8XVRlht5TKhIX6oOjGIFKHrgYv0guUvzjejznoUCO079ErG8arxjAGNoevaSc9ZZjKg0aH2z6PhyE7MJV_evdOfFhnGOW3E8XHLw4xA_q-PQZllNB2ZkeY98xheDjZI-bsRT8Y52mf9LwIge8yEQzFwTzF_HlZ5lGXh2K5aVX4K1EcnINhR3mtoO1t-IzwL9Qrw2lITZf_beeiUUwoPA-OOlhb8qoMqOH2ZACQ-hFzxa81wPplBzUfa-QUPL-83dQkWc-ym426Rf7YpOUCr9qzt8krQRBSNrksx7qDjH5JKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی های
#جام_جهانی
رو بدون استرس و کمترین ریسک ممکن پیش بینی کن.
⭕️
⚽
فرانسه
🟢
سنگال
⭕️
⚽
عراق
🟢
نروژ
💳
حسابتوبرای‌این.بازی در
#رومابت
با ارز دیجیتال شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
26
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/23615" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23614">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWigVdpuZzF79RSbJQ1o0FN7pr2tqKnEtdg3FtrXho4JRL6iyeoCTvZYBrULmMSClO22SU1s02beGXUt8tZcyAf3GExAPbbfrtzgqTSpGd41lQHAN6hzEYtfT0YfLvDWFyKYVFKo2qDSS_dMkcJQuUB_kZxjlHBMMLjBtsmr30jzAnHMvuu8AcgEAlEo596QCjpmiwbBaJPNyrV0Ct9rOzELCqJ4TD8AXYPXASv0AnM8dl6WTUYJ2-hjGrMTGFn_dBAUmGazOby3aixfHUcVAS5-SgRh7Szrv8wa31ivR9CKWxIXNxTEMWUma-W6kAf_ftgaZb5WNXXorejxMjQ1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/23614" target="_blank">📅 19:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23613">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw15cSoqqxvH73K5GyDCV4pzqdGBICPvZ8TwQG_EGgqAXRytHZUHk7YylibF_erOxA8P5DbtcPXVL08bxEXcLzcTzCM0irY_LFG7iE8VXAlwTMi7dstjDsWzATNHP7YQdL92psDAYBsU74v67MrHLyX83QXg2c7S7RqctqTMOIGRsNMz9iSAUE7ov9pK-9XEwAsX2HqNaQ30XZiJoPHzvr0u1UD7nwUNqeZURhKr0gtZtgJuvgd8nEL39gworHsXEgkssrbuIwFNfyf5Fjep80MjDxfmei1z4qnKXSQl3K3l3i3PnBqCJ4QM15jygy8F8bWTT6fYFtPZn0LA5Jssqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو: روبن آموریم باعقد قراردادی سه ساله رسما بعنوان سرمربی آث میلان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/23613" target="_blank">📅 19:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23612">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEgCiO7A8U-NYLa-7jrqnVM1PtJOD6rTPYLczF7ILllfAfRlxT6sp4GwSWINJWEAIWJN8VX-YrN-H6UdbIHe2AXNpntfmCFr0bEjVKkIDsDuHAoIqtUSn1yBES0Gq15EW43Q4eIrpArgc9E-4hUQ4BZeSlcWCic5xijyrhmZvTaCLpPdKy1fdgoYfVJAXpKtQfH9sUcCMMBtKNC0bLRsLYXXBAoX4Bu_oxj2-XOY_2RhG4xVydKzt2LKtH0vFHMcotuZK0g3X_5tD3Td7g-u4gsle8eA-v_2975ATDnjsO7mGq12JWip5DseC1fArL2nbuhGXTFJ7DwkCpSNtek-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
⚪️
طبق شنیده‌های رسانه پرشیانا؛
عارف علامی و آرمین سهرابیان دو مدافع میانی استقلال از فجر سپاسی و ملوان پیشنهاد دریافت کرده اند و به احتمال فراوان از جمع آبی پوشان جدا خواهند شد. سهرابیان از ابتدای مهر ماه سرباز خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/23612" target="_blank">📅 19:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23611">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328fe52870.mp4?token=vdQsivTdpI661RkZLkxqCew1d77_FLmiae1Wwl0axS9BG9bmlLKOM1NlHRemj34E1OKkaaxD6g7VAB5NISfynq5zaZkdfTR3-XETKUJDjffnJJh44YbowVkU-5pCRNtHSXQRVaOWQyWHNwJl17UwfQxkJzAB06wbHBRa9Q6qlHaJwi6AK3zJgSEXzG_mGdSrIIJSvQroWKen1tmG8E0IQs9lMeCabTHA2qnqKanSU4GS9lDtZGCT1EYfKrDhEHnWsiG6D5dpvStzuRpGyoxURkjJx-53mHvlt0YtXKjHtNKcAv0ps91AhAdI9FRdM_5KlAzPCm8ZrXawwtUFv1AYVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328fe52870.mp4?token=vdQsivTdpI661RkZLkxqCew1d77_FLmiae1Wwl0axS9BG9bmlLKOM1NlHRemj34E1OKkaaxD6g7VAB5NISfynq5zaZkdfTR3-XETKUJDjffnJJh44YbowVkU-5pCRNtHSXQRVaOWQyWHNwJl17UwfQxkJzAB06wbHBRa9Q6qlHaJwi6AK3zJgSEXzG_mGdSrIIJSvQroWKen1tmG8E0IQs9lMeCabTHA2qnqKanSU4GS9lDtZGCT1EYfKrDhEHnWsiG6D5dpvStzuRpGyoxURkjJx-53mHvlt0YtXKjHtNKcAv0ps91AhAdI9FRdM_5KlAzPCm8ZrXawwtUFv1AYVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
وقتی لیونل اسکالونی سرمربی تیم ملی آرژانتین رفیق سابقش رو در کنفرانس مطبوعاتی میبینه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23611" target="_blank">📅 18:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23610">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1q09hveSwxdW2LCEFtXUgcqXKE36aSYTiZAGsVkH_PxZ-SPBsoW03eHAApQi4uX2MPhETAvBuiASSZgm9YBf34HHFpWjtHhFiPQBJqrWFOQYbDRgPNtcQ5wJqGZVh44KQqrZi-f5BHWiBYF8HsjwGh-z8eAko_p_moKGZc1z2g9WyC8zxICmzzDwFdEJ4XFJvXBuTsCPkI8n5L_Z-g9AWO3FOTYhAFzZsKLlbnYC1qhuwhvsTiH9zGx4q1oT4ALMgvsVkbCcQ98rcNLNQ48bo7vCHwS6v72JCVHzjr-gxs2oCZkJqg_TeWjzavmx3Su45Vu6wy0sHExbENBPMIuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
آریا یوسفی در اردوی تیم ملی: فصل بعد یا لژیونر خواهم شد یا در پرسپولیس بازی خواهم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/23610" target="_blank">📅 18:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23609">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSBYZ38532vsf3p-Pruw_vzFdBSBH5t4xYirl1o1QvHldE-NCGKI10bNsKYz6WN7UX0i2UUwLM0IkSd_u3wYJvdwojW3UaT4IjFRi-S03sCLUqmAToYawc088rtH5H73hpGb6g2YxhiJ6G1ilI-Nq_VIkkViH2Aq741v_lNUdrT9YEAE4JufblXubS67GmGfIyG56Ty3F2IYjHyzBBTQ2m3UStToy2-4o8IePO4VsJGjlQ77_ZeofRFpCTWmIRBXkImO7gR-0D01Liq0BcL1xVqMZd6NOJN8HUtABrDx_4QeObe7vix3cjm36OG8dNjAGa5afRQrd6r4rnXHad8pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
مدیر ورزشی باشگاه بورسیا دورتموند: چه رئال مادرید چه هرباشگاه دیگه‌ای نیکو اشلوتربک رو میخواهد باید 60 میلیون یورو به ما پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23609" target="_blank">📅 18:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=GAHyk1jb0_uGBWyWf-2LHRyzPfHdA55ibyo3fFcG8HoUNib39t3IsHnqeJGJQDLStEtXrbQXVshngbNdJxzDgOa60H0vTsEUhW3-iR4SodQF7jwBw4xHpqaoYpqMMeXNM311BAIK1NolGkVpXebtgXmRRhUzEpVtpcAfKtp4Ci3bw63WaP8C0TNVT8i3e4Vu5lhN85YPzjM8J8PXyNy4TW7uOzro_ag8IoP7-zJfO7Q3zc_kMShgfZBjS_Scvbx6NbImrt0dNuZFubvqPqbkjKE2uXyImIRcvyuv35iEY-wtYlQjQI-6mgXCxU-dHzbYMy8V9JQNFNxSb0emJNzYk2sTJOV_o-iEkiai68-wu6pfnQJ-9Li9lORZf6L1xAgH8w-hkI1M_JeCZO0gwSrLhfpNjQVCQ_noIwAsB-HLQS89Bvj2WDkwTH5r_f52HBY5lOD3d5if8ntsn4QeFda-g7hWi2T1fHgssgjHEFdQS1l0Ob2LjovDi6q_DJJZhDJA0Lnevfv5u4VBQ3L3q5jUwfjV5O1EwU-LttaZQLd1vq6SR9GTbrHpQKhWX6qb_f6BS6YEpOjvtTWp0i99S10xVMw7ZOZdH_Sgxge5FpUc_FQrXR45KKG2Vm_FHzJibL5fxXcIFJXjJgvg0iry6WVEOfbnf-Z3gfxvxX0fF89mTU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=GAHyk1jb0_uGBWyWf-2LHRyzPfHdA55ibyo3fFcG8HoUNib39t3IsHnqeJGJQDLStEtXrbQXVshngbNdJxzDgOa60H0vTsEUhW3-iR4SodQF7jwBw4xHpqaoYpqMMeXNM311BAIK1NolGkVpXebtgXmRRhUzEpVtpcAfKtp4Ci3bw63WaP8C0TNVT8i3e4Vu5lhN85YPzjM8J8PXyNy4TW7uOzro_ag8IoP7-zJfO7Q3zc_kMShgfZBjS_Scvbx6NbImrt0dNuZFubvqPqbkjKE2uXyImIRcvyuv35iEY-wtYlQjQI-6mgXCxU-dHzbYMy8V9JQNFNxSb0emJNzYk2sTJOV_o-iEkiai68-wu6pfnQJ-9Li9lORZf6L1xAgH8w-hkI1M_JeCZO0gwSrLhfpNjQVCQ_noIwAsB-HLQS89Bvj2WDkwTH5r_f52HBY5lOD3d5if8ntsn4QeFda-g7hWi2T1fHgssgjHEFdQS1l0Ob2LjovDi6q_DJJZhDJA0Lnevfv5u4VBQ3L3q5jUwfjV5O1EwU-LttaZQLd1vq6SR9GTbrHpQKhWX6qb_f6BS6YEpOjvtTWp0i99S10xVMw7ZOZdH_Sgxge5FpUc_FQrXR45KKG2Vm_FHzJibL5fxXcIFJXjJgvg0iry6WVEOfbnf-Z3gfxvxX0fF89mTU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید.…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/23608" target="_blank">📅 18:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=Zbywe8YpUJIY-Sx2qp4-SVuNfNF9izApLN5HnDnoWB0ajFIopB7DDuXWMhaHGwQNdtIou4tlWbIStJKvxD2fhFeO4pIACk0ydej1JcUFXoaIZEWygq6C3fyQ6SbaXNygvbuGUq_ocHgc147wkDgzSXvUSr0XIjtP3WhPFjgwdCzsZRo8Q0nyu5_YULyinTAVB3QGhbSltsjV35ARP3wm5e35uaRUOHWO9OTogOpTAenW-lgkD0hOadsZkD4o2h1D50ZLcwvTVO1YNEVG-FplAZYslYP74s07h_tGSi443V9HgS6E_cwU-gYcdIpZL40E7bsKQRsAFkvLe-kZyTzWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=Zbywe8YpUJIY-Sx2qp4-SVuNfNF9izApLN5HnDnoWB0ajFIopB7DDuXWMhaHGwQNdtIou4tlWbIStJKvxD2fhFeO4pIACk0ydej1JcUFXoaIZEWygq6C3fyQ6SbaXNygvbuGUq_ocHgc147wkDgzSXvUSr0XIjtP3WhPFjgwdCzsZRo8Q0nyu5_YULyinTAVB3QGhbSltsjV35ARP3wm5e35uaRUOHWO9OTogOpTAenW-lgkD0hOadsZkD4o2h1D50ZLcwvTVO1YNEVG-FplAZYslYP74s07h_tGSi443V9HgS6E_cwU-gYcdIpZL40E7bsKQRsAFkvLe-kZyTzWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره‌خنده‌دار هاشم بیک زاده از حج؛ میگه بری حج نمیتونی با زنت... دست بزنی بغلش کنی
😂
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/23607" target="_blank">📅 17:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23606">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-dSBrAFOoUlYPpHv00YcWRVZQUfCj8AYAvEUWD4Nu2_O-EBUSjgPC0ShW_eGf01Kd175UYpq4OknBDPCtlLaz6z5f51vM_pHBf_BNglvGoJau5IBkxO6nNVGZXQKI4U0vcuaix9B3z06_a2mFXDnV8CfeosRbmhXCkEiCwXmo3-7C09_I7uCF60_4UXxJIhlaa8H7NBz__AzHqIsw6vifGLs5LsP_rHddoIFKUhASChnTBQvRXQn4qrgpsWQbjlfDrlzGo23Gen4ynkE-6b4WuWk2megVQevCgeAX6GUbu14cd-41rus9RFG8_f0_ukUn5cjKzXz4pvuBOlXlf9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید. 15 برابر جمعیت کشورش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/23606" target="_blank">📅 17:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23604">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clSeeqG35B79nIJQTTm4mSx52ncPYLZ1rLptWNK7D8bCwC7to-TRVcU8eG_pmPRnqt2mYRd9f-s-j-ivRfX5bns59y3oJRT4P-5x7UyZsJ10Z_WSaImzbXe8hTty6r8KHQmrPW03Bs_ktD7k6k5aSP65W1RBybm5jjNo6q8GX77GMNQpFJjdKrKne-i0c3_pZSgKYQEH1hdiWLJHT4G7VZbR-kuqANvqGVS7Hl04auLjiZKSg6B83v5RnUKJT-bVCiR9vLwWmmKhT0erfRmLnNQTvsRwAT7fbUtUqmA3NIhggVMYtgOwy3eXl8YpApAPelzenYkKhKkLBAM2CHIVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnTH7T12lq9yKzUR6Yj_f7du13UDtN7QqwqlwOxxbEzgNks886RsCbuAGdDQfGFXi4jbBxL6heymrQzydK9x0FOJxIQiKklx5AxvDcZl-JC4cnbppVkudxFpM2Vqc7OSsT5pLVnOodwgeUCjywfEq-TKoPX18OJMulxoXKS8qZhPLlnel4j-9G6VCc3AQKpsrwKvsNa6C8sHqYCqWYnxxcE82Rwg-JjvTHOWA8_d9y98Q8iRtnlyNhtUsTFmGo8EdKHiehNNDyvUBbzbJ3OdtXAvGG_qtbUovZGi8DSXTOxKeCVC5ebcC7ox0MZBu2XN_aSFHJeieXBZqVjFdUC3Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23604" target="_blank">📅 16:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23603">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzzitPFWJ2jZsv_f_s_HQ4Dr7V9bn1KHaMWOWVdBSJUOeW0ty9phcE3nRJ3LZO44mz7ady2newY9YEdzcq3yJrKiM-JVb2C3_6PnWIq68VBFNYzQQy8_3wOEHegPnDonC8tBRKFY-yDIx4syb2tgc_UNTXOI41xgdBleOpoHV-WXpTiYbie4bRpCa4MgIrpmrzeaX67VnJFUt_qj-i9HYBtY_PFrXXN305o1HXeUdKLosA7ZPC9Af5V4tDYfXBNJm89QvHdoK48M_AGDem2xu6IQeRELwCXScRdiZQV4vaKfgh3IIaGW2o0GMYvusonFpeIObjD6nrhlMcrM8eYgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23603" target="_blank">📅 16:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23602">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqX_hd88GHFrEnSADvNtlo5ytkAuwqJG7kP7UlHaYVSt4iMWj9oC3cgWEGpZZThgjGsegZfAiVThTF4ko7iIH_m90-cuN2OJAk0aH57qIM0bFRT76-E8B8CQnCUuEYrzKjpmQtC7CfMZzUbB77N2mqNFWxzgH1QAU640oib_JWOySwQgokLfDSnb0R6m0PIoZsw_HcG1GOBFk1EEb3rv4fOj6gERyq4S8fGmponRCnmK7wCJafVizZ7GpUe5ZsUGj9M5mcD1d1vPX_fyqFpM8iEa97GAmFd5l8TWIKaT72zA4kI5ypnCITr9xwEsW3U3R3USfQLi0EADWot8HuerVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23602" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23601">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=LiORZcSRDv03MpO3zrewi2Mt3OKTtKj1GV2wytCdaYCOffiwZRWVxLzUxYHYZrviP22U6Ryq0561fuG_IL-R6iE3hgiCSsAOjQo3_MzVtGI364xoOaApr3nwweCa6C2LlrQPIfWmW6A8Iz9ZUKMsmVEXXFMT8Ew0Lhag_-fr_FmojlLQo0c6J5lmj9BTG0MNzrbsb3sTNkAOZfY8LvCZ9i7BjqIQ_K0gqWrUXpxAVUa6J03-Bq1zFkapTIKMkOdngId8OC2SxOAoVOqGAcpuYGdaqgQfJOgM9PenVE4JbOYQiDHwKGTvw1xghPsr6MMc3HFFfencbf2Mv2XO_Fo5Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=LiORZcSRDv03MpO3zrewi2Mt3OKTtKj1GV2wytCdaYCOffiwZRWVxLzUxYHYZrviP22U6Ryq0561fuG_IL-R6iE3hgiCSsAOjQo3_MzVtGI364xoOaApr3nwweCa6C2LlrQPIfWmW6A8Iz9ZUKMsmVEXXFMT8Ew0Lhag_-fr_FmojlLQo0c6J5lmj9BTG0MNzrbsb3sTNkAOZfY8LvCZ9i7BjqIQ_K0gqWrUXpxAVUa6J03-Bq1zFkapTIKMkOdngId8OC2SxOAoVOqGAcpuYGdaqgQfJOgM9PenVE4JbOYQiDHwKGTvw1xghPsr6MMc3HFFfencbf2Mv2XO_Fo5Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جز‌ ترجمه‌های‌ماندگارتاریخ‌ ایران
؛ پیاتزا میگه به خلاقیت‌توحملات‌احتیاج داریم؛ حالا مترجم: سرویس خوب میزنیم تو دفاع باید عملکردمونو بهتر کنیم:)
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23601" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23600">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
#فوری؛ کسری‌طاهری امروز بین‌دوستانش گفته مذاکرات خیلی خوبی با باشگاه پرسپولیس داشته و بلافاصله بعدِ اینکه مدیریت این‌باشگاه‌رضایت‌نامه او رو از روبین کازان بگیره راهی این تیم خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23600" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23599">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDPjnkZNV2w8LNLiWNV5LCinz2RPa7qSDxbtYGWfueLM1VFU6C60Pj7mOUZNycNz-Z5e9cAjVsJW050U_gMoGBhGYO9hdS27kpzQFhsscxG2DK-FUPR7DU3ocwDFj4bRyiQ0C6Epqa6nKBojMbdNxJFt_wKIJ2aq824KEQ3aASr8_oWOZgdRikoofkgKzNQmM-IRMXAPH2i1kX8r7rVM5RZtnyjjD7VmC9DTtTJk_qfQz-2KimilVsCLEHPgIhafLb7Hq8kraYlpS3ysRCLxsz_HuTqKYoBrJGBD7HPrOCq6MLGqpOlp-nBM_9PrcAL9hORs7OcliqJO7VwA6C7OaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
تیم منتخب روز ششم جام جهانی با حضور رامین رضاییان و محمد محبی از نگاه سوفااسکور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23599" target="_blank">📅 15:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23598">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3yjOCZrxY_r3Yn8R3stn-vatjY8Em4STQzPzwCbHQFnwHIeJv8CIwvosKIvcK9RcIK89ZXTHfB11nnGWwNrIhXrQtNj8Xu9KuwHOcYJFP0__plpcUEZA7H0OEgRMXeA1u-Hi455hc_LbNpT69YALaOXojr815NyLldHSpaxf6M5W-5OvEgoK7dNHjRZj52Uh4y-ErvbmyXdZyGLk7bOsXctMQF0ZXkWYFVjRcvfenOFBg-zRY2gaxqopGtbTLEbFCHi8xAuT6EpmSPqsPHWelOU0H2sTvFSvwWcS1ivnniwzDweZ5_WrBi29Y_btkca55SYc76b5P9OmS6YV79o2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
روبن‌دیاز پس‌از ۱۸ ماه رابطه و زندگی در عمارتی مجلل از مایا جاما مجری‌معروف بریتانیایی جدا شد؛ بلافاصله پس از این جدایی، با حضور دانیلا ملچیور بازیگرپرتغالی فیلم‌های‌هالیوودی مثل‌جوخه انتحار و نگهبانان کهکشان ۳ درجایگاه‌ویژه‌بازی‌پرتغال و شیلی و تعاملات این دو در فضای مجازی، شایعات رابطه جدید دیاز دررسانه‌های‌بریتانیا و پرتغال بالا گرفته تا او علاوه بر فشار مسابقات، با حواشی سنگین زندگی شخصی‌اش هم دست‌وپنجه نرم کند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23598" target="_blank">📅 15:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23597">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=ZQfcDMBO3pK7K2eFwGWmift0HEfEqjys00KgKgzIUt3f642H4YY3MNIiqWWyfANJN0igvgalxU7tHwwlVMe_b-RNWQpNz6DjoDLTATG0wp80Evmp7IaMsSuipkWbcHITkOSnZ59xgRqY5UAfzVFxLhp_8RXFLZ2xAyy_Aq3xdV0qYh-8arRLBdaNWURX7tKAi5NSSA0U8SEzuzl3cycJQyPxvfmn9fZQdH7feM2S72XGefwnh-yJNamedqIDkoFYky9WT9kh9omlWBSRIcR-kn8nXKr5UY9Gigb59Jz--rV6_PUtqMfdh1z90weXMbwRsHQ7if9Y8ekocGzDaYsJXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=ZQfcDMBO3pK7K2eFwGWmift0HEfEqjys00KgKgzIUt3f642H4YY3MNIiqWWyfANJN0igvgalxU7tHwwlVMe_b-RNWQpNz6DjoDLTATG0wp80Evmp7IaMsSuipkWbcHITkOSnZ59xgRqY5UAfzVFxLhp_8RXFLZ2xAyy_Aq3xdV0qYh-8arRLBdaNWURX7tKAi5NSSA0U8SEzuzl3cycJQyPxvfmn9fZQdH7feM2S72XGefwnh-yJNamedqIDkoFYky9WT9kh9omlWBSRIcR-kn8nXKr5UY9Gigb59Jz--rV6_PUtqMfdh1z90weXMbwRsHQ7if9Y8ekocGzDaYsJXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
یه عینک بزنم تو برنامه زنده جذاب‌ تر بشم کسی زیاد توجه‌نمیکنه‌بهم؛ همون‌لحظه عادل فردوسی‌پور:
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23597" target="_blank">📅 15:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23596">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te_-dfq5AWmVM1w5VGYSzDuCkUl6-BiDRYmnbAJcwKkvCCXJB6jXcCQMJFDxgNjDXsos7iNIy8h6VUa7IqmmJ12RmAG4vaNpbQmK_g_k6WpvfZYfSSV8uZGwx8wtZb1YnZ080UTYJvsDILZdDh1n78vBgUjcbzwhhv37XbOx2Y2A5Dj9nOL2PAhZmZ0Ixg_GTv0bV4ikGamhwRQnjceixto0S4peQW9S18rYBTsauuY17eXbew3Mn2_S1EypAu-esBlG5gwCuZbIRajCTe3GWu8_BLPEq87XAUaZfzZCzDBBbVaY3ifu32iwrwcpyANc2J53bQ8SUHzsmuo2PUXriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌نشریه‌فرانسوی لکیپ:
دولت آمریکا ویزای مهدی طارمی و مهدی ترابی دوبازیکن ایران رو باطل کرد و نمیتونن تو بازی با بلژیک تیم رو همراهی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23596" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23595">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2AWj7iUGwUsF60AHg3OPD9JLqWpYpr5OFyUwleTuNXiRzMN_-SfM9C4AbnTZgxjsH0DAfHnL4UEmL51tsfosQepMRAAdysM2lziyavxObO8MZmFxDwRjCEJnSy8OWU-q4D4HnF6T8XrKT7igxwuGH_ldLPA7dJS9DBu2_oPg-Fxt4PsA3i1TnIy7Uy8l9Kg28pXAVQHviJAfBsFl6R4XgVaG-ROS0ptP9vKXor5xaAiuA0YzvJOGSPaeYc3H0NyZqrPL_VeX5pcHvcJjEyaEtO7sgnqeM2pHbmnmly0PdNdJv3b5kipOBZMhKleTmR6UMIoC2LjPlQdiI7FHMi0Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بااعلام‌استقلال؛ سهراب بختیاری‌زاده بعنوان سرمربی جدید آبی پوشان در فصل بعد انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23595" target="_blank">📅 14:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23594">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7FRQvmdlFjTldN5L22QsUNzqZgCBJ6A6EiFNNxGTgU4iP6Y58zvetYDgtZBXSfIuQMFaZIvn8lAeqizyDAzI_C0sThCzaneW5qovTN_XkQJZ5XXJT99I3-JqN7HCMwp8_jTb-ppZHjiYpV20vbFqzoIIUsD1Qcaf5h36I1WQUdI_GQS0_wyAiyc0jDlRFEHQRNMXKHuzZ5hjYJyrGeVV3wAOcWbNObf4UTVlFT1HC20cnpr5FaBsbto3dJJSobqk8b-X46NNLXPQ77YhVh2SI-sUk1aac_DrMnc5eB5co2n9r06ScF3j37i9qvA0I0s1CTqcv1N0ljfIte9WExbLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇳🇿
بازی که مساوی شد با اینکه نیوزیلند ضعیف‌ ترین تیم‌جام‌جهانیه؛ ولی کاش تو خارج از مستطیل سبز هم همه چیمون با نیوزیلند مساوی میبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23594" target="_blank">📅 14:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23593">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mV9oq79nALSO_-tr5isIwxqDjkrv08tB4AJM3KPjOWKfsgJyY_UrG-NoBiutfUbHmOs2zcYzVH6O0rNz80i-8ALG9fAOnaueqEv9MB7Syv-tbhisj92EUESaIjSH7SZ1oYA5ZOSHhfaVdURZ32UtEG61P4xFefXl3nWxi_P0XEIc7OiCVKMGk4N5KPIdK_gyiT84bdRJnD71KCEIcirkveU52WsTYvyRXttFZCItfmoSPd5PxwY0P7iW1B3TJozMTObAexZogk0C7_SXd85uiRP2-B8iTjtyhw_GByid0cN5Lc1ivKbAa1SWhSBcNumzIzPINyUlmMl92rhLnExFug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23593" target="_blank">📅 14:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23592">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHfoggr__XTKnCQpbM-uWr6zX1vuSivMtJkOcCAINkut9xzI7YvzXTn6Nf2SYv3pv5fSg3sYCjIn0Eo-nq0qfU7Bhlc4sAGnaPMWgCEbLNdtVKLXDqjvHjkMKvIQnxSC-FeaftxdahD70mbv6utnrGkzOwxE6roZ6qhk0rU6shgi4gj-ynJ05U9J7NfoT6XHbkIr5okykAyOz6a1SfxCmApjwEKltjWtjWEPEKmCwG7BeA0F_qS3PJ83vJ-zqeYCKAFxX7_0Y4PVgwJElRNy-3nsMabp74UTw0KgUamw96dFxkLPd-2qZE9CiMwatQzIX6s5Jb23N9F9FzAud-JoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23592" target="_blank">📅 14:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23591">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBTyapHCWSjB6GfaXJVsIwqMjcMStgZ8bQTjtGvjzeAZKW-g3oA82gtbEfPnjMUBGYD7uvtX3ikQzEerxynGrL32xbuVDDb2pkizkkdJq_ezBSs2RiHBjTRnPvQPcQoswuXzo44MekqekZWSmX4MFzpzQBrcOIjsJ5iXiijl37kOZvf-AbStPQY62eWyFy-RWn2uCvi4OHCy71HUdkipTZWExuBCDO-boENz2i92pj6I1FCsl4RQhDn97XhLWg48e_GhqlQqN9L0MmeTPjSsZqXGY61T5h88q4swBr6SA7u0EBf2I7EupE0liXg4v15UckmIlFDPU9YZXChVDyJ4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23591" target="_blank">📅 13:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23590">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=c09b-6T-lBzC6V0EnjvRXubPZF-yKLtXQeSP1C1-Ak319ToiHdq7iZwiwAwviXEzPqrhZ2nlIh2JssQqEbXaSzBE2eaLg7pLrPf_0-oioy5G0ooxFCGVzl8JkRcFX7E6Y1Em-tTKCPcQyRUzXgmLfqWyFpyyk4UL_RJvjsoIcT82h2x9gap12GN2vK0F5JBgFO0Xq9MvHAyU__i31ssPLhwS-5WRNGs6USYY1RFMRM6d8GY3_myc3YQ55VwxZJ2D7PIZFJJ6LgVNNyM-sLd6AchdlCf6ew9wg6sgYFtNcI_b11dEo6KAKu350XWb519SaeRfbFOgBlrhGwQ-tWgtcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=c09b-6T-lBzC6V0EnjvRXubPZF-yKLtXQeSP1C1-Ak319ToiHdq7iZwiwAwviXEzPqrhZ2nlIh2JssQqEbXaSzBE2eaLg7pLrPf_0-oioy5G0ooxFCGVzl8JkRcFX7E6Y1Em-tTKCPcQyRUzXgmLfqWyFpyyk4UL_RJvjsoIcT82h2x9gap12GN2vK0F5JBgFO0Xq9MvHAyU__i31ssPLhwS-5WRNGs6USYY1RFMRM6d8GY3_myc3YQ55VwxZJ2D7PIZFJJ6LgVNNyM-sLd6AchdlCf6ew9wg6sgYFtNcI_b11dEo6KAKu350XWb519SaeRfbFOgBlrhGwQ-tWgtcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23590" target="_blank">📅 13:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23589">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsrUFhlFvUiT-sZoOd6rvKdLdCgSmbc2gLSoxM5CCZKoxzs1juSN8Vx_t4Avbkkj20GGp0i_vVMWKdnmp0uqKxP8b0mJ7rJE-IeKxDNZSgxiuaQrjCeUT9MU_02aehXNlVej5U75SUExfydTQh3tAJB0kKH68Uf26XCCOSJxZYtBaOGRf9QYnRSf9pwhi1N8LJgTyn0pmSZlDJyHKjOPK55THJZ2HhDgt0AgMxULzsUPuCSmv3SPqMhwpJXznSko0m4iy8Gcdk9bSbfXVQin_QE8uhrC3TTIv-B3dymzlf9Gjj_PcLV4pJrRRdEI1xLXZNxU24gF_hvLt53Klh369A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23589" target="_blank">📅 13:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23588">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SscSBqA7jyOqo4AuxqmxMheNg1U17eIRQjp7TLiA_im54mkH7iu0j7LH_3HJC1FD_RjAOIOgC4g9wAJPr4C8IUtBJUZAuabShKMeKxkT8w1UyFk2skEf_1Uh_HQ7P4bAKR_af0wifKg6zyrbvsYWxDDfep11YNtYiRqUCh6w0TOtetbRsltJWhm79RwlZEUXqn5H1I_rg_hrzMBlV1G1JEj7ieC6pyFEWG94XkscjiKuhQPUi4wriVN7e1HuDjod-FDgOskN0YpHOp9As36m5NA0vPwg-hF-z580yE6PgkOTr3iWZpolf-z2ASwI8WGWOAXl5k9kxv8bHJ3kuNpdzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دهنت‌ سرویس پسر یه حرکتی زدی شدی سوژه همه؛ حالا تیری هانری اسطوره آرسنال دیگر کارشناس شبکه جام جهانیم درباره خوشحالی بعد گل محمد محبی گفته فکر نمی کنم منظور بدی داشته باشه. خودِ محمد محبیم گفته بخدا فقط یه خوشحالی ساده بود که اون لحظه به ذهنم رسید.…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23588" target="_blank">📅 12:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23587">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jcjs7R22rZ3ewRuoTP9fCGTt-lyqukOF-Ownbfu9FjC5AlnOb3g3nLEtrtRhJ4hHgXOwWdw2zZ1tYqMs7Km2dut1IdlA-CtL12Fc919pnRUJnL5yn45OIl8h73FXvNPXlzigVp_ybRZdyAr8P05KeUVAN0bGPu5Rfg5vL8Tp2x8kmo6CdZQzb6czvl4aFwdGSjl5_Blmh_pGpenfMXz4xgreQOCwjlTGrbDG9c4NcWflnreANAipQ3iw7pk1nV3zMHV84hCS34n2UgKXcTITwBtQdKFMXT5ka7KtlXT3ildd7dAGJwjlOlAu3j3f2ReUKHH2HK0V8SkawRjBtsIcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23587" target="_blank">📅 12:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23586">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uy2FPUGyYTp9aicWdQOV7562YG-Npj6domdXli8bts5s9RR3V_jCFaB2lhGk8lQbuckwUTrcS1JA2etFQena16nfIB7pqK-GV58eqUjxChSwg0OQGbVmFBBm0SNGMVk2cmX-I0uAmEU9lst8f914HVIqOWMPGhi4KNRvwDB1ZOjJ_g7kHBOig1X8JmwxQTIR5QMhFm5WA_ga_bRQtHQ4S3SAsuqZ0xuew8CiDoldFraZcEtcQQKZ9pidUg8MvkKVw98JC7M5kKs380jbTbq974cy3Eu8DN1KT2oaB1q9dkcELYXPI7lc-e1JaA5XCQdiFPNCxVljBp-4-SJBQMHVSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درباره وضعیت آریا یوسفی، محمد امین حزباوی و مهدی لیموچی که هرسه مدنظر باشگاه پرسپولیس است و مدیریت‌این‌باشگاه مذاکراتی‌نیز با مدیربرنامه آن‌ها داشته بزودی اخبار تکمیلی رو خواهم گفت.
‼️
آریا یوسفی جواب تماس‌های مدیران سپاهان رو نمیده و چند بار گفته یا لژیونر…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23586" target="_blank">📅 12:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23585">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9_-xe1NAdF6dCtjT-6bc7MMEXHqvDf3aHsp46fI4GfGGZ5wH--VxEdkplhe7L_7eDLEdVxyHNohIxKLABKC8b-0naTpOKg6nWpktm3l2jC4TcjXnFwG0Utyaffshb0SfbTtd_kzRctU26U6xqcmQILj6VUTGubvOupCS3P-H_FHjvyZNMPXzUArPjda3AGnFB3HRrZS3-ggHRW3Seavq3pTAKg1EL-I0_XPAlGrCriqyiZDmYqrvHMYcjUqeCXodwSho7YSf-rhT6pxyBIjGFbRPNiq0bQVENoyJchD5WJvwmW5A_q0nXTDqVu_PaFsUwGW3z2SMBwULKNJzumrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23585" target="_blank">📅 11:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23584">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICwavzjqACzbr3vyDvFF7d0x0jLaJfH889IcRns2UCsilMIOS8quDAIU98-Ai_omRsQ9j20mvSjeZpTYFmfWjHZ7IGFXUIRVh_wX4Bw0gjUWcEMERIVtTWniLeU36eJY5hdd7EK8ptYKR4OR9gJn63s7m0uufXDROeymP0Np4ZtCeH7H8EZXNKAEs3UDVwdEYqUcOw205z2ypLbvqlzF40zSKbr1LLrz5bBXdEaxEK_9lVskXjhaSE8C8CbqgyY3CCVgY9z7DQVaaHLNT0FsVGoXieeiZzHHrklQxGTbtHJy2NbM9TbKqi2zX2hJt8igGLQH60B2tj96v3bvb_FGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#نقل‌وانتقالات|رومانو: ژوزه موریینو شب گذشته درجلسه‌بامدیران رئال‌مادرید از علاقه خود به سبک‌بازی ماتئوس فرناندز ستاره پرتغالی وستهم خبر داد و درخواست جذب این بازیکن جوان رو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23584" target="_blank">📅 11:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23583">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚽️
خلاصه‌دیدار امروزصبح دو تیم ایران
🆚
نیوزیلند در هفته نخست رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23583" target="_blank">📅 11:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23582">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD9uPcm6xxu0Nik0ciy17PEXB_kuOu2UqzR7dDesnPILLPtpVLfJB7vIX3oGKG_voiA8O9qJ4TnMdSBzBSqDKDco47cNtfHSV4AFfG7o3tWuR8gLisvlBlfQgQO7uwh7ceKZKk9COteEDUBALNPqCGYwxAfjfYLBFu3SHRtP8I4wgJJWOCfba0YWMog_HttwP3fIfourkdhoeXPYdCI6Sl5DwhsL0LOjMGt2oz17iyVMBgP8I7OMNBNPGG37jd0TDUYr8L3avIUaUV3LJzjpAwngR39C4C61Bi7M2nxo0SrFL5VBdLmKJOLj7k0Nbt2Mj0k0vOpU7xSifbQ9NRQ01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23582" target="_blank">📅 11:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23581">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVLvd45ISE7mvNEjAzcDoyjPMwp7ZfH3KKRcGyt5arws6eE836PDt0-md0CHesbI47KRv6e5Wwq3uSErzRfZGVhMucvzzXz4s-WozEOhJJQwiot_Y9RAUzg4TgRqsZD_dmENty6pYUXhlc3yOjMsJ4j7tRldhQQvydysGXao2bL9HVdfKz9A2ddMfV6YAZlywqVCUZAdoDDhKoxhtI9tGL2yPH5hZtiDvHI5xREDC1zhm3-PvmqdGm5DGjMJ4j_ZfHeNchmeuAQ6J3HVm6UklsxfFPpetnJ2KbqOdCXQ-HNXl5prjrBI3ZnAt8oX3iCxPOwgbtgZmT143DPNZpBnzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امیرقلعه‌نویی‌سرمربی‌تیم‌ایران: میخواستیم دو شب قبل بازی بیایم آمریکا، گفتن نمی‌شه و فقط باید شب قبل‌بیاید. الان هم میخوایم برای ریکاوری بیشتر بمونیم لس‌ آنجلس ولی بازم گفتن باید همین امشب از آمریکا برید. ما مظلوم‌ترین تیم تاریخ جام جهانی هستیم. ساعتم هم…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23581" target="_blank">📅 11:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23580">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=VYN8ywNFpQi4h5m270PFzhHFxlgwKJI8htaF6Gk0t8pRJkO9y9Tx_KfTLoT4C3ATfUt5LFHG9CxVDDFrN5WHJS6NVBiv1DEVKDxGaIa40kCeJL_5L7mEb7iswjPtelju-ksjjJzpI5H7gpRoSg6LxziJoxE2KGVRTAti5XPOjxoTKsmKA8lT44lJ9SsjhobD-PSLf56QKR3GDohh6F3OQc73s6HF3JtXfu_ydU_Ml5rti2ORUJ2t4HB2LdVe15XLw8pedJYxgb490mWKnexqfEmLaA8Fuc0zwKlJofSrYd7h1tU1KH--tCmqfqYhLABPSZYfq5lNoxTqXYRFqdmDYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=VYN8ywNFpQi4h5m270PFzhHFxlgwKJI8htaF6Gk0t8pRJkO9y9Tx_KfTLoT4C3ATfUt5LFHG9CxVDDFrN5WHJS6NVBiv1DEVKDxGaIa40kCeJL_5L7mEb7iswjPtelju-ksjjJzpI5H7gpRoSg6LxziJoxE2KGVRTAti5XPOjxoTKsmKA8lT44lJ9SsjhobD-PSLf56QKR3GDohh6F3OQc73s6HF3JtXfu_ydU_Ml5rti2ORUJ2t4HB2LdVe15XLw8pedJYxgb490mWKnexqfEmLaA8Fuc0zwKlJofSrYd7h1tU1KH--tCmqfqYhLABPSZYfq5lNoxTqXYRFqdmDYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
امیر علی اکبری در ویژه برنامه شب گذشته جام جهانی به این شکل انتقام همه رو از ابوطالب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23580" target="_blank">📅 10:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23579">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPZvbnGzLSpbZQPo7QnYPuIrcIv9c2oOPlJdCM8Pelsyk4WrhVZKVlWwL62esX5m2OkC4jug6lY3kAfoVAIiYb8o4Vb4k0hGh8XRbPxH5GAYhpsJ3tI0ta53uRaprc-WBLT85xiPSZYoou-daK-nCEnIVoe6a3HNmKoJj17Mr6iAH1VXB-UsP-HwSR2Sw1E8BmyIzCM66vuWoVUdh24Wr1HOiKguWtG7nZEKjCXIyPBboGdrYgU1b-hVaW0P-hbS2FS_hgADWGJN71AU_gGzOCYSqiFQg1WnoOX2-5j1TPATlQC90w16Vr3Kfo3kD-T88TkS-Cok5s-KxinQqpEFJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23579" target="_blank">📅 10:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23578">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=hixq2tKl7gQgyw4Sxm10B8wJFoRLKRpapsny52lbEHZPIhs-332AzMuejJX8uRYmMx54WzoYOMzfHFn20QVpLtaSDoGPgWPof0wpVq2D37ukcf7bXKHJTIvy8TqVX0RYQVfpGyZwY9DNYNGGt5WBV9NJ1daM-2_gOSmMlTqBgqnL1sKvM6bPlnqYEx2RNf5SyR1liO6-xPk0iKHcK0J63qhebVQQhBryeU9dURk1ZBesfwIvFxPLp_17aWjyTejFXOucrHWmYP0wHwFDbHY09OXocCroYw8t7BoyQ6LBxvOe8OfEocpc9HUSTdgYAXMaG6pOFZUHhj9IGrDcAl6MrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=hixq2tKl7gQgyw4Sxm10B8wJFoRLKRpapsny52lbEHZPIhs-332AzMuejJX8uRYmMx54WzoYOMzfHFn20QVpLtaSDoGPgWPof0wpVq2D37ukcf7bXKHJTIvy8TqVX0RYQVfpGyZwY9DNYNGGt5WBV9NJ1daM-2_gOSmMlTqBgqnL1sKvM6bPlnqYEx2RNf5SyR1liO6-xPk0iKHcK0J63qhebVQQhBryeU9dURk1ZBesfwIvFxPLp_17aWjyTejFXOucrHWmYP0wHwFDbHY09OXocCroYw8t7BoyQ6LBxvOe8OfEocpc9HUSTdgYAXMaG6pOFZUHhj9IGrDcAl6MrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23578" target="_blank">📅 10:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23577">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foN-Heo2M07e-qGv5S-Qzg4hgbwZXqGSEjvkDsrDyngasogIw_Uh7e1DxPIBZNDKW3UX7MUjh4ws6Ldtndy5-FiYuwZMXqdi-A80doxrvzXMLtxJeBfiEn6d1WE0wodtbN2HAccOyucXA9eQtQ8wglevVFpopIL3jwGZG5V3WC6hACtx7sACYoDVGyo0c_5m9MP_dZPwlbZDucBREAZu02HS3KKKmfCIa2iO9KPPdSr4nwmCT0aj2-3CHPxIslW3zIFTZmlBJXvqdgQvE6mZY6CeEzHccNjv6K2K_FF-gGhld8P_mpdykwL3-0_FwwrFJD5wjVbLf_VL02WP3ntv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23577" target="_blank">📅 10:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23576">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhmAJG0OouQzTHsbzV6t-QI2Grl8NIYjIwsSzuyy9ZwxWcgDG94y_P4ITymq6uNdzrYtfrUXH7sgFQUm2tfv7mEczxJ9vviMyLpfEimZKTT_xbuyvA7n0FEdVgOVoLmuAQcFeQxPrU1rYb3qZ6eoSXzCOjriVnn_JJZRk2jXB2dahQNEBeuaSHkbUc93g5Bkk9hekvs1uqNhUJ0CnY3wBKSCsESumLxanXU7lGPEUHCXrJAJeVr7cJsvxFdwUe3VqaWhpentcKxX4q__nyM-PU1wamwKrQ1CbvRnbLCCMQsfiZqDdkL6ZS9ikxbN-Ew5ea59vY8NA2K2MfT1uT8NFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23576" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23575">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a244147c.mp4?token=R4MdREMx8sV3mON0oEBuIsQiq0nPA1xzgAn91cHXf1K__twMc7oxCxnNqulwHOpnAQivQIUgxMAbQ7Gg7I957QS4hg8bD7mUrHVeVFSFycN3M8hjPcNRT-81Jw1eJV5UCLaSd3Z3WeVYgUIufcVjhA_engfI8giCIBdG9mcf6DEVvs84NWWWTLx_lEJ5e8zkC_V6NeVwRN1brb1pcoGXJ4xRZ2G1ywjJtFxWIliAZJF7bZgzamwJyr9pmRzj7AAt53O0H2aHg0LjRl59cSI6mbKrZ4hNbgZZuLxoAIgbR-pyzW9yj3tCKiY15ZlooxHjHDFhJfbtnoGi8174gz6mrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a244147c.mp4?token=R4MdREMx8sV3mON0oEBuIsQiq0nPA1xzgAn91cHXf1K__twMc7oxCxnNqulwHOpnAQivQIUgxMAbQ7Gg7I957QS4hg8bD7mUrHVeVFSFycN3M8hjPcNRT-81Jw1eJV5UCLaSd3Z3WeVYgUIufcVjhA_engfI8giCIBdG9mcf6DEVvs84NWWWTLx_lEJ5e8zkC_V6NeVwRN1brb1pcoGXJ4xRZ2G1ywjJtFxWIliAZJF7bZgzamwJyr9pmRzj7AAt53O0H2aHg0LjRl59cSI6mbKrZ4hNbgZZuLxoAIgbR-pyzW9yj3tCKiY15ZlooxHjHDFhJfbtnoGi8174gz6mrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
سوپرگل‌دیدنی‌امام عاشور ستاره‌تیم‌ملی مصر در بازی روزگذشته مقابل بلژیک درهفته اول جام‌جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23575" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23574">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✈️
معرفی سایت و اپلیکیشن مل‌بت
🔄
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23574" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23573">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiIxvl3dM75tYZfgr57fBvUDkrdvuM9hVEqrokgnOCv3aoRhSAU6G5tIp0KvhYOx2YPezQTCU6nZG-PiIehi1aPvPZPsNm5XSHaMB17vI0i7dwqFI8sfjE0tzkxFn1MY2LCfiFJaMvw3B_u-f8rQ7hU5H5Ug0-hdeIb5ba_3YBoFcytWjRPGMhCQUJfZY-_4xw_zcE0H2mscnxBEFGVIQYI423IIlxwRzHpMK7iju7BCklUwDUiU9D0Hol0hA8rXH7rmQJ_plqf7XS0hhRJ1yYCA0OXsHlf_ttFEzqLpClSPnXiqLqJbe3oOqQILCFECWCgrLHkdET48xjHs8PSn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23573" target="_blank">📅 09:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23572">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7VtOHmGgLd7rqMmXDnmqx_9aMvNUxABvFuGNlFofRtb5Gh3H4EJCqnAll3vBcktyWIA1hO-Zg4y5zhur9ZEmoQEwnY1nUPvSrHefQcz_SdeWhCz2gxkYj7ONY3I-VGxbDExrbQcvXQ-8MesLfPXSAFoaxPZO7vHJOL2Xim3Y0vGuNUuZeYg8Z9_V90iHyKBtyM2DHvKC95mFJFWa9KpEb-041rtI_BpkgdeM_F-gcJvQJu_UWFtPYdIXqajB8cViMM-nhH401Ff19P5JRMq4PIbkZfuwZYJQJkwvYWFDe1FbZj9Qn44wN0IWnwNN2wM--fZgyYhM9BL24PjiZYrtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23572" target="_blank">📅 09:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23571">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607d3917ea.mp4?token=tZMABaGwZhf0zEC5vZvMNWYeOxbcFCubegW-S56M4Ya4-o71UPWZ9p2h-Na17OuA5RuUWDXGxje6f68cvRyOrXzvXr6A-OBgTQDLvi7XxjdDYWFjs_JXD9bXewDSjQDGMcqTM-skeqnePXwLwpBgcZAfExzpYxtHjF1Y_JsXjiDXp8pPvbVxY7ufzEN5tEU3AVDbObAYxXxLHlP9OmpGHmRwAfc9rVbSNIUjkmI51X43tIgGMSXJVVELRdhLteGLAPX-nPQ0N6zqfjct4q5AbbKxwOw5SWylsnxO-CxZZEwpQ1Bw2IDkLfcilMedZe03HIDxfJO7QuPa9-ycU0DBHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607d3917ea.mp4?token=tZMABaGwZhf0zEC5vZvMNWYeOxbcFCubegW-S56M4Ya4-o71UPWZ9p2h-Na17OuA5RuUWDXGxje6f68cvRyOrXzvXr6A-OBgTQDLvi7XxjdDYWFjs_JXD9bXewDSjQDGMcqTM-skeqnePXwLwpBgcZAfExzpYxtHjF1Y_JsXjiDXp8pPvbVxY7ufzEN5tEU3AVDbObAYxXxLHlP9OmpGHmRwAfc9rVbSNIUjkmI51X43tIgGMSXJVVELRdhLteGLAPX-nPQ0N6zqfjct4q5AbbKxwOw5SWylsnxO-CxZZEwpQ1Bw2IDkLfcilMedZe03HIDxfJO7QuPa9-ycU0DBHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ولاتی امیر حسین قیاسی خطاب به محمدحسین میثاقی مجری سازمان صداوسیما
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23571" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23570">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRkle1IlmrTAy61zhjTFWVAES0AMAQb_cO5iIPqU755KFR2i21OyHbFrJ2c0AX61tI4Zqlsm-SllDURdfNxWNFRnWkMZLzX0Shkj4-4nuFlF1u33dfyvzaT9p5_4JKEkFS4YDDU-Jt3bHgcPiW7y4hDfjcPDWVIilJCS5A81mdj-oM6oMnEYldlDJ65jvW3vjG1EUMy_I1zaM9zQKJnEWh-uL1IjfwxuDNlgsJgq-JLL0D6j-BxyzxF4BJvPgbrwtczTD32zFce94LV6SGJmz8sz4dXbbKPK-bSAVh1rzmy8PAljll2pC-ffR5FhYMZyLGyfe8usdeIxFXbBdvLnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇯🇵
موریاسو سرمربی با تجربه تیم ملی ژاپن با شنیدن سرودملی‌کشورش‌اشک ریخت. یکی از تاثیر گذارترین عکس های جام جهانی تا اینجای کار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23570" target="_blank">📅 09:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23569">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e9cf628c.mp4?token=RAStRjNMDdK-Ed6c9_xFBEiw40eWV95L_lXFFkVq_ndwlHvkb9GESgf8UT7R76PyR5RtMaEHlH6xI88rqSYWTGxC-k2u7b4vYsEdcWxVXo4FnwO0Ehh1hcH9QfRr6TakiK10jJQvldo2P8i892wIsUZUlF_2SMCFK8ls21Ja9QeaFEDKQdpNFBhF9_qRKsTlX9WLkRMh859NPmjD_Xh6jj7AnmDoXbK458PeVVopW85Jfeb5jXS7SpNiT8GUZxjd2DCXKSaz18MNCjbFTr4vQIu0-RC6L6fvNmfXyoGoxLLpXWDD2oRHczv7yovWgJELSNctGVYNaWICG8_4D4gwiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e9cf628c.mp4?token=RAStRjNMDdK-Ed6c9_xFBEiw40eWV95L_lXFFkVq_ndwlHvkb9GESgf8UT7R76PyR5RtMaEHlH6xI88rqSYWTGxC-k2u7b4vYsEdcWxVXo4FnwO0Ehh1hcH9QfRr6TakiK10jJQvldo2P8i892wIsUZUlF_2SMCFK8ls21Ja9QeaFEDKQdpNFBhF9_qRKsTlX9WLkRMh859NPmjD_Xh6jj7AnmDoXbK458PeVVopW85Jfeb5jXS7SpNiT8GUZxjd2DCXKSaz18MNCjbFTr4vQIu0-RC6L6fvNmfXyoGoxLLpXWDD2oRHczv7yovWgJELSNctGVYNaWICG8_4D4gwiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی در نشست خبری هم ولکن ساعت رولکسش نشد و به‌این‌شکل‌اون‌رو به نمایش گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23569" target="_blank">📅 08:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23568">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9HVROF3NvjZoIUjRf2sB7ApXHV5DpwdeKCNrfW2dauM6vnrFfLLrifxwU3Te0qQDiDvbxrOyDp8sbLrzZ0KTqaEaV9lGkhNUJ5knFX1a7jOX-Ll9eubeBzV8H3o8VLS7PJceBukS7YWFC8UFqgLaw-L-M1KAr9o7UB4vTOIyi5CAcmNJMbXP5FZeZf37NnmKkzG7dKBBvz7XnG0iOdyxKVnXscaV1qV4eHtBblpQmPiR0vBk5izCW34n8FKh6sfPVO3xeBYCxo5uG_F7DxbL4RFJdkt9k7brhWULlP1fn4Cpj0NeDDd0qFn-BCFDQ_DLhu8EcW5XobqaPza4aZr9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌ بنده‌خدا دیگه رو برد امشب بلژیک مقابل مصر 8.5 میلیون دلار شرط‌بسته‌بود که خیلی شیک باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23568" target="_blank">📅 08:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23566">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NOd_XVfRDdpRvmtOd60MM1dBjoPQJuqezlOcrx5rtamvCK3fJyW_HK335HWA5M9vX7tuQE-4aCpEzlqfLdeLcwDpTLNs1GkJp2ouabbwuLgr9DoALbaD0uFbkMpN8tZQ9qtJ3rGyXVc2HtjP52XAu_Q-1MZER0X4p5rePj7LNRS5c1fLbeosdGyUpPSMunKl5UacVNnOPeRdr5ta8AB2EXmCdHesgyd_QdRKYjnMzojXt9r8vUnwt9xPIlzAWwu1R8G5g_ztqBQj8fu5E_hrmjgCvYT7Sp7Q0P5ENWTFTJ0s3KW1o4k_Az4uIOMIcGwNDS4W1MeJyCdkSba6ZSepBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vqabn3cnuVEwls147Ub4L0l5MbV2dY-5LQ3Jsok8xEMfCP0t-vi_uRaL7XfHQp7Kaz7t-JeV0Uns9Mi8MXxb6-AFpq31fylZf-3Bj5KWOo9wZ3fJZKS_p8eUpdZE-tntgywzRutxYEvFnd5xHkbEhjTvur8FAE98iLQMAXAIlFy4glMcZEWBBVULeLs9tqQaWgHVobqtTcq1re2t1C8km6vdPZbciYYVkj9tX-NKZspvA5LbyVWuT6PfAgxuBKT43qEoJ5CWscVi-JWcZnMLr_1Cx_b0eVQvhO8NRKp2NPLYnwKC9qKsq0D8WbCAis9Mctih1l4qko5bNyOmO0Or-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
نیمار جونیور اعلام کرد که پارتنرش بارداره و قراره یه دختر خوشکل دیگه براش بیاره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23566" target="_blank">📅 08:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23565">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmNLaXXbtKD2BV8hP-D3iho7umlnVNYTjEqblm7wWcLH6LLKDQvIdsgsdxCNaEjSoWgz5uxi6LNG9edWqvOf3ChDUHBYExNbv4Ba1KaoKLYxDfWs66y3I57KYc6-_Tp_DwkC8NNO9VLOGU5aqe0Q6d27uYHR-81_dWhArHBSIuJBFxr333_3EPqHoI1-WvCQYWaRY9shSON74NamQ2jHUJoDTmcEnbOrY3D-UYDmWUwvPYLadBCjDlrYdVaEsQm4_zfoGgVRa9kWyt6gTidLIZIVa9LTHfUZz6JpMW6WqB00ySllDmFztpN3Sbd8nvbisk-QogcM16SuTUvvC4UHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23565" target="_blank">📅 07:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23564">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ae8867bbe.mp4?token=OmfqkGtV0ISU-W3LGi1BRSQkpjbiXEuMXc61chmLocVB28-o4HEC1drCD_chiUn5aJ0SsmLrTVQsXGWp7d0AORyYGXX8sBj9XlK_6I5wxayL8rT8mwBQdxZnp7EQCUNj8Uy_wcpaLEjeowDWJ3oUcqW9_3HL86pHjer7At25s1vRmayEPbhto54oQaMYBdef0Q-fCnJDuAzn1mqChCcWpf5hoFG3ZyNssOKYC6KrFvoHYas_QsImb4c6taZk8VebgrPRXPGPgbXGicTg-0PxvRJVTfAfEKesnuIP42McxVw4AIB-TrkYtdcu4uTGrGuuBBNQeCtOEhhmzXwb48cgBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ae8867bbe.mp4?token=OmfqkGtV0ISU-W3LGi1BRSQkpjbiXEuMXc61chmLocVB28-o4HEC1drCD_chiUn5aJ0SsmLrTVQsXGWp7d0AORyYGXX8sBj9XlK_6I5wxayL8rT8mwBQdxZnp7EQCUNj8Uy_wcpaLEjeowDWJ3oUcqW9_3HL86pHjer7At25s1vRmayEPbhto54oQaMYBdef0Q-fCnJDuAzn1mqChCcWpf5hoFG3ZyNssOKYC6KrFvoHYas_QsImb4c6taZk8VebgrPRXPGPgbXGicTg-0PxvRJVTfAfEKesnuIP42McxVw4AIB-TrkYtdcu4uTGrGuuBBNQeCtOEhhmzXwb48cgBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل‌های دیدار امروز صبح دو تیم ایران - نیوزیلند در گام نخست رقابت‌های جام جهانی؛ رامین رضاییان بعنوان بهترین بازیکن زمین مسابقه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23564" target="_blank">📅 07:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23563">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16918ae52.mp4?token=t-Cc2frPrSKQtReFP_NXbuaQI621IBtZ7O_tRxuXJ13O_grw2-Dy7QkLexYhWT-U2h9aTz86SjmfLtTC1imeOYAC8GoXI2E02wL11sBLCGvUNuhiMCY96-tnRtxxP4FCOSyzDIZjGzKHn2u7bOM8SGFfR514MZ3aAlllaj0FfcQuEXHtaQAESXYGsapTnsa2_9UfY8k-iSIDf9aujvNk_2BB9E3v0qpSSuAZ04SSJiRigtXcl3hFFqFx1LrtScadB1Dak7vkUKGqtNgyCUtzqB8MJX_h5L1WX50_qAjrsE41VsMna6YH_cYyyMOtMeOLIe8a_fPxPrWuPi1NqMtqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16918ae52.mp4?token=t-Cc2frPrSKQtReFP_NXbuaQI621IBtZ7O_tRxuXJ13O_grw2-Dy7QkLexYhWT-U2h9aTz86SjmfLtTC1imeOYAC8GoXI2E02wL11sBLCGvUNuhiMCY96-tnRtxxP4FCOSyzDIZjGzKHn2u7bOM8SGFfR514MZ3aAlllaj0FfcQuEXHtaQAESXYGsapTnsa2_9UfY8k-iSIDf9aujvNk_2BB9E3v0qpSSuAZ04SSJiRigtXcl3hFFqFx1LrtScadB1Dak7vkUKGqtNgyCUtzqB8MJX_h5L1WX50_qAjrsE41VsMna6YH_cYyyMOtMeOLIe8a_fPxPrWuPi1NqMtqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23563" target="_blank">📅 07:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23562">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23562" target="_blank">📅 07:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23561">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcvXiZ5gvF9bpKwxMadGXZgLAYY_x9Sp_MCe5f0FrheLjLKm2btHPQZMhyCsfjERwXO5e3PPuTv37-K_LXVMfdIl5JgoLSZfcXaVweQ2cVhakuEGjMPoQRE2XR5cegKMo4OUZ58NoCT9eMrJgAB-bORP_E2zJBENbk3u6I6CbWiaJPbljgEex1l5BNWqm8RquuCUXJdHOohE-F9r7lm6xRAXY1lMf1zZNo26k_VKZTnKJxZ9dbwy5Ito_0BatjauiACZDAfBlOPqLzEkfmkFn6tdXfUUXVXgE6AXZt4eFib-d8otS-87fQQ4nq2ptZmNkuyAx6j6XTiOiHYh8X7IBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از مصاف شاگردان قلعه‌ نویی با نیوزیلند تا اولین قضاوت علیرضا فغانی در تورنمنت در جدال حساس فرانسه و سنگال
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23561" target="_blank">📅 07:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23560">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMk-JBpZby3CElPgPiAMUEQWzkBxfHnHjfv5wUbIeKTlG1gIn_7IZKwbCutsRwqK0a752Jc2EvXxLmgVy5fZQCHFLqo9g6Nd-tYM2kX3dq3FIt6v_eO58E-fFdk9xxrEj1PlGM46xgAbgbegImpLoNYzEBkb-Vi6klaElOsEVEOyM5VyfGRZmq3AmEqpWZwlNbDOb1UJbC1DcP9USF9244B5wMm3OtjKTKyP8mYxFAaFN-Mk9iuQeybsm0S6RIyjJG_AhTAtJOA8jvArKl97LTvTjl83JplEYDsE2NU7shPNgs_0u2S0wjvXAlOX7W1Yi3TD81BG87tzMNsOkWPztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احتمالا فرداعصر ازتیم‌جدیدکسری‌طاهری ستاره 19 ساله فصل گذشته پیکان رونمایی خواهیم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/23560" target="_blank">📅 01:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23559">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCwdN5E-uFPL86sqAwKWJ9Wj4M4paGQcR4Q8T7NV2KCbxQr1jl9BDyz7aBK5AlRCuD9c59d2iHYhNfvg4SlsJDApGpgtIq8pgQCYhKHGVoZU4KZUdWT3KaXonRUXik7gYxM_ZgV4qc1RBW9aSfKt4lcRsaxEvJ7K_TefDLMZs1Ew6sHC4rSpPgrCcH7N_AADRZgQJA7kXGGMW3XSABkkOGsTM2Yb7vgzdNxlgQKNnmXxCm60Gu_6So-GXeoGDDdFXBwzA9GETXaWkBgtlLYEsO2nEFyfxdZ5jEc269aPIonXS5zsguENycKwssW83en264BUYn0hfvWkTTEBMAvSGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وزینیا دروازه‌بان 40 ساله تیم کیپ‌ورد، قبل از بازی اسپانیا و کیپ‌ورد فقط 50 هزار دنبال‌کننده در اینستاگرام داشت و بعد از درخشش در این دیدار و انتخاب بعنوان بهترین بازیکن زمین؛ تنها چند دقیقه پس از سوت‌پایان بازی، آمار دنبال‌کنندگان او سر به فلک‌کشیده و به…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/23559" target="_blank">📅 01:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23557">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFrMg0tkJxeufBal_iA8Q1tfLJRcpEeoLZ4zv-8Xvfbjw9tAUX8O1s_BFubXzZ8aUCblzX_gfLCP935YzA-OcMAuxwu6JzU5CaMxCKyVIdNO8g0DNlQFjI0UsqBEUS8ay8zYF2jAsAXw4ZTJmjjJhQxcJSsKEZt5pAW-jdIO3d04ijr-hiUC69zr31Mb1zP3WB0SNk2PF_6kSAQckXg6Do5yf8lDMfF7jYzW-zxmwxmY2qL-G_TbfNFUed5YHAi9_M9c9D1HRWsT4S3WTWghFHPHfJk7nnxDduJueeU1C1Akt1jNp6J1gBtbWJgTW1rIu_Mqp10Qkg0F-h8cae8Bcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف شاگردان قلعه‌ نویی با نیوزیلند تا اولین قضاوت علیرضا فغانی در تورنمنت در جدال حساس فرانسه و سنگال
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/23557" target="_blank">📅 01:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23556">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIcLC2ae0-aeuwVmIXxdGH2PHbaH3Z9KLAzSvsJTHQhvENSWeX2P32Uxh3RonbJ6GJZWKtj0_UO3hQdljc5vvIJkw_4jxjMWZijohFzQfQaFK8dguhK8dyE4x4davKTZol1GIsZKDrly_YrJYMfejQZ4DVGlrRWoGQ0yg7P3_ZX1hvHCHLkVO6cc4DrjSIbxYfMewCz5O2uTm2CuBVLpCav13AgSRDTbfaxG3GbY_nEHp8XsHiI-dBTxSA9ft8QvasT3l84TN_tYxQDqYOZWr-EFTeQCeqC8icHrDr3UguhuQo7oV9GGmINdEHPy9_tzhS3Lk3ujwAVEGJdfSOuLDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌‌ دیروز؛
از آتش‌ بازی سوئدی‌ ها بادرخشش ایساک و گیوکرش زوج خط حمله خود تا توقف‌غیرمنتظره‌اسپانیا و بلژیک مقابل حریفان خود
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23556" target="_blank">📅 01:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23555">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11adede3d.mp4?token=eFZcKcpkC40aoBspJYtWsnfo02PrgUqqsZtKAIolk7nfRlpR_xYRx5w6TsOmn_-g6eR03U8wYPbcGIo9EjG7OFC1S-bXhKAHaWnLEEUxfKQ2xdjSo-eF5WaJ97O3xDokyrl2RkNxsoVSuca1gQ4MhT5dM0jeeKgRLoFOQQ7A6WmeBhz_WNeuN7quZ1-UNEFPYCJNfSyaQxgZNpS2Is8EuDiM2wUoqlqDbCgd-M_iOo-2vn3jdhbdI8slemMvB0T3MOL_yhsvQjiAqS2ej5tZoKHvHawx9WXnz8K9CenY0LOlrcfYq7rqlr4vDO8ceIYouJ559qsNenVwbCVE037xOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11adede3d.mp4?token=eFZcKcpkC40aoBspJYtWsnfo02PrgUqqsZtKAIolk7nfRlpR_xYRx5w6TsOmn_-g6eR03U8wYPbcGIo9EjG7OFC1S-bXhKAHaWnLEEUxfKQ2xdjSo-eF5WaJ97O3xDokyrl2RkNxsoVSuca1gQ4MhT5dM0jeeKgRLoFOQQ7A6WmeBhz_WNeuN7quZ1-UNEFPYCJNfSyaQxgZNpS2Is8EuDiM2wUoqlqDbCgd-M_iOo-2vn3jdhbdI8slemMvB0T3MOL_yhsvQjiAqS2ej5tZoKHvHawx9WXnz8K9CenY0LOlrcfYq7rqlr4vDO8ceIYouJ559qsNenVwbCVE037xOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
نمایی‌ازاستادیوم‌سوفای‌درفاصله‌کمتر از ۴ ساعت تاشروع بازی دوتیم ایران
🆚
نیوزیلند در جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23555" target="_blank">📅 01:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23554">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a904e7169f.mp4?token=P8k9gkCIjV7oxAGXdE2DcrHxLI4CLM7d16l4lFj2N49kxIyuPPJgXW84sJek7dKCOlNNWvh7cJZ2jZDp8l42EaXvkadf3Pftnp39xZF7_K2PDAWY5a2qatzuhv8vlGlh07qDXPV3L401uosV2_mdzS1tWaaCCYABvkF_htfDvVwhH0VunvK-QJghhW-XXxY5kVp7NANdGfrLUMD9leAeYxB7gUlOroOM0fK3LpNABbZU_v-wuuLdXnLm8IdvCoHUYD3jbcSixUu7DsMa2Qy8uXfmJk_iZaG6OVlBroOBS1-fLzj79JBkvdM040iEQOEOZy17RDminRKEobf05qHaTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a904e7169f.mp4?token=P8k9gkCIjV7oxAGXdE2DcrHxLI4CLM7d16l4lFj2N49kxIyuPPJgXW84sJek7dKCOlNNWvh7cJZ2jZDp8l42EaXvkadf3Pftnp39xZF7_K2PDAWY5a2qatzuhv8vlGlh07qDXPV3L401uosV2_mdzS1tWaaCCYABvkF_htfDvVwhH0VunvK-QJghhW-XXxY5kVp7NANdGfrLUMD9leAeYxB7gUlOroOM0fK3LpNABbZU_v-wuuLdXnLm8IdvCoHUYD3jbcSixUu7DsMa2Qy8uXfmJk_iZaG6OVlBroOBS1-fLzj79JBkvdM040iEQOEOZy17RDminRKEobf05qHaTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
🇪🇸
دین هویسن دفاع اسپانیایی باشگاه رئال مادرید و همبازی‌سابق‌سردار آزمون درتیم رم: سردار همیشه به من می‌گفت باید بیام ایران و ایران کشور قشنگیه. مطمئنم ناراحته که در جام جهانی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23554" target="_blank">📅 00:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23553">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NR8FtQ20zqP_cS6mrHWNZmnzvGf791xiUXjtO6LKUqkCXvRba6I5_nRVB0-3Zx6VxcH4JN1CjCZKfxDXqFgZllfr2dqBjAiM1fr1T8KEHVT4bi1w9K_dsOjPL6R70wHltnDahPrj3Fr1dzTw0EEzow27bZPSRrwMEkfIG1XpZ80_YNPcVN6YhGbmAWSL2_n_svLAXdNIkzPlOk_Uk0lCswXKGMcdu-0fuBbYZkVlMVWXMxJQ0hHoQu0LkKAt0emCKnaoJnCNamkvSyJLt1jf2pMLKcwU2k_jVgIyH2Wy2rIDzzGJ0hZ4nR1ij72_jQYdhm5IsmupqxJet66X-5N5YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده‌خدایی امروز برای اینکه 85 هزار دلار ببره 1 میلیون دلار روی‌پیروزی‌اسپانیا مقابل کیپ‌ورد توی Polymarket شرط بست و الان همه‌ی پولشو باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23553" target="_blank">📅 00:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23552">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpx_7vZvPJuzu5MXVPyxqZLgUxiKcJ5bBfpkqSpfZwceLmkD1DlI2rdWyayQBISg6wyxhVOlC_VCkwMC2TLXPMZGJPJmHkZJ2BLgW7lGxIfpP_qriXwYdFk_tsBj22YdCly0ljB3Y_gvJ0wHIG1hK3Z1PkHJ7QE5-SojntG8-PeyqCwy61-x3Sd2LaYP9sqokZcP0TIoSYtMW_uzbTiQ9ZyekUHSmLL7UwYAuko9vuxdQs4_xiazhHcjKP15bUhKaVDwEDCzNZxr_S98mG2L6nlHhO4Rsg7qgzzl9-zi5aLFClCIg0M7k7OEG0zQ3JwmiDC7AJA8nPmzd07nLMxuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
🇧🇪
این‌هوادار تیم مصر پیش‌بینی کرده امشب مصر بانتیجه سه بر یک بلژیک رو میبره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23552" target="_blank">📅 00:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23551">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AImz6XGtmZ6ny-oCYe4VgxVmAMFazyaxpWPHIeRGZZkE5MOjruZphEG30X_EX9t8nIu7nUjm605La272FrTN-6LGnC8JOGpA9wmNXemqnko9eEY0Hnj2tGGT-LZvs00OCLW0IwuB72lNm_cuHBpTGBNwMyCYQns2fpPNenSVuB1BT4NcnldzIPDdP7j9qN72BUSUeS0l7GcZPE0g2NP3xQohIymlCbAhUmyF9O78Koiw2Us4JN6_NcmB_cz4BNhOE7_nIYvu5YCNrPxbGzWsGJ080eUFcNjhWpEBVtbm1KN4LO8hUF5OMI1-QaTtN0JOWzBzMgPaIpjtUCcoOAdmtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که دیشب هم گفتیم؛ نماینده کسری طاهری مهاجم 19 ساله روبین کازان امروز صبح با باشگاه پرسپولیس جلسه داشت...اما طبق‌‌ استعلامی که از مدیر برنامه این بازیکن جوان گرفتیم هیچ قراردادی بین‌طرفین امضا نشده است.
🔵
جلسه‌نماینده طاهری بامدیریت استقلال…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23551" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23550">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpxTqrH0FJhXXdHTOYAJgkNWev0k3cB2yGZkVnvHwiaGdX-G8rk1DpNdg0fsfICUyvDuI80U3jKxrvVIhkeSqp-_msPpn1AyrmZInMr4UdUP7KANJwzu-cvcJYjvaHs-ohvVAhEYECE1SSSqw42XSOjh7rrGIHRBR_GRfA8pLYS25IzgwAj0jERUaWAoKauq82wvZb4lv1HjqPZidjb1P-V7Au3YP4aud3wFXtgnYJtK3ehukf1B5_l48VoYVmGzTKtJi4BpUJRzutC3OZASHIcVC50nhlDVc7KiDL4W_pBTL5nSUbXFroTPUUUypaEt2oNQCHmbEfAUp5IveKzU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:
2014
: تنها یک بردمقابل استرالیا و حذف در گروهی.
2018
: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی.
2022
: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی.
2026
: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل عربستان و اروگوئه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23550" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23549">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZDBvzaJvaG9HyR6X2AInZV84qPErJowo0F2Fr_S2FGXVBR3s7hotGMARpOOe30TLzgj7xQE_7yYThWlCuJzqn0XjAk8lL0b2LovYnaVtIpp8Od48J4tDkRkPiYu7MBT-gToDDcZeQ5zr0GjLRevvsQxZLVkfQZ8MN6JEPumCVfDjT1C4pgRXLAJOXsdiN47sHLwaC1YLiFEMTnde78aFDNNBFcu5-NZdBNgvPeOsw3z2JL_blANLhXcpl6yXxs_49AyaiUvXuqmdqVRMNxT8QFubF7x6TKkXqtQwJEtyCMwi6fKAPCLPOAagW46M8UpW6kemiDy37r2wd_aIWU3QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های دیدار امشب دو تیم هلند
🆚
ژاپن در هفته اول رقابت های داغ و جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23549" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23547">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392bb7bb0d.mp4?token=elkLO2A1DLzaE_MjnYiqiXHHiQ0m9df0OuUop1QWVyZhIv9UJQx-ONOlS44vjCfQytkC-7_sTWIjM0gFmdxPneblR4nX-pjE_3ERqIWZIo9Rk4CcZaholh-xVE5ww0weY69Bh0gpb5iRsQM_keJGqrkeP5E9KSrFiumLRJxcdNkKk3rw5OQv9ta9MRZAvCNSm3zVm2m__L1XHZuBLKCkikkoQws9RLRcIMbUvdZPmIJpu51LsNG9NBYmcdN2Ip1OZXozmvbcvbOgzMhXnu9CC-dXIH8_L6Bdh2bgdugzxbtj629EiAQqbgFd675u4OXSpuM-W4Xdo4xsRCbd5kY3cDNuKH8hgMUbP9KjXkW8MExs6sYc8H6bPYNfkLN-WyHaF4X0aiqCdISaHh8uhA_brBsYcOfRlUTLlIndO_MaJxbPrwTB4yH-vFzJn846VaLCTwZq0fjLTC7J6rA6be26jKKXWBHDHqTk0vljVm7j87rmV_d-lTQP8wwlbPTCtJJM1MGWEcXmxLcUYQU1mibmrmn8QvdTGxk2356BlPZnBlmCT7Hm8YFXNKdbS0nBdvotHm-mMrvZFL8fE0p8YoSpxvkpJLVj_PxEcRybVr-3_h1YKpeeADPYFHtDoBlEIGaZ9WBkrgqshAUPxXdDUeG1tmzyB6vWQnCSheRw61nZpfo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392bb7bb0d.mp4?token=elkLO2A1DLzaE_MjnYiqiXHHiQ0m9df0OuUop1QWVyZhIv9UJQx-ONOlS44vjCfQytkC-7_sTWIjM0gFmdxPneblR4nX-pjE_3ERqIWZIo9Rk4CcZaholh-xVE5ww0weY69Bh0gpb5iRsQM_keJGqrkeP5E9KSrFiumLRJxcdNkKk3rw5OQv9ta9MRZAvCNSm3zVm2m__L1XHZuBLKCkikkoQws9RLRcIMbUvdZPmIJpu51LsNG9NBYmcdN2Ip1OZXozmvbcvbOgzMhXnu9CC-dXIH8_L6Bdh2bgdugzxbtj629EiAQqbgFd675u4OXSpuM-W4Xdo4xsRCbd5kY3cDNuKH8hgMUbP9KjXkW8MExs6sYc8H6bPYNfkLN-WyHaF4X0aiqCdISaHh8uhA_brBsYcOfRlUTLlIndO_MaJxbPrwTB4yH-vFzJn846VaLCTwZq0fjLTC7J6rA6be26jKKXWBHDHqTk0vljVm7j87rmV_d-lTQP8wwlbPTCtJJM1MGWEcXmxLcUYQU1mibmrmn8QvdTGxk2356BlPZnBlmCT7Hm8YFXNKdbS0nBdvotHm-mMrvZFL8fE0p8YoSpxvkpJLVj_PxEcRybVr-3_h1YKpeeADPYFHtDoBlEIGaZ9WBkrgqshAUPxXdDUeG1tmzyB6vWQnCSheRw61nZpfo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ماجرای شیر نگه داری علی اکبری قهرمان بوکس چهان در خونه از زبان خودش در گفتگو با ابوطالب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23547" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23546">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d02367735.mp4?token=R1UpOevAn4QYrA7HgIe0jYzLfOi4_n3f2QqctBlS9Btg_2N2ksgWU4s0CpxTdwG-t1iD8PuGlWvHu1GjHBKVE1q017vBcDxJXxE2mE8wrYY209djpyN1mimUaBkCliO_Z4xvmTshHlapGapXfMfZQBk_rnaf092qkCkfLSn3XGgPxFrN3Bvv6CxAhNU9G9gV-Cexcold0xQ_cxzDSTRRqi7ghJwWP33P7exx4BfNRyPD1p28YPtET2BjEMmGLCqHZkEsQd1m2DDITleLoE19lYOuZrGj11Yu7EafP5aZsQ1DiaCHhNDvlb_nGoI3l5xAPnDqFNBmiOomqCZkMijVhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d02367735.mp4?token=R1UpOevAn4QYrA7HgIe0jYzLfOi4_n3f2QqctBlS9Btg_2N2ksgWU4s0CpxTdwG-t1iD8PuGlWvHu1GjHBKVE1q017vBcDxJXxE2mE8wrYY209djpyN1mimUaBkCliO_Z4xvmTshHlapGapXfMfZQBk_rnaf092qkCkfLSn3XGgPxFrN3Bvv6CxAhNU9G9gV-Cexcold0xQ_cxzDSTRRqi7ghJwWP33P7exx4BfNRyPD1p28YPtET2BjEMmGLCqHZkEsQd1m2DDITleLoE19lYOuZrGj11Yu7EafP5aZsQ1DiaCHhNDvlb_nGoI3l5xAPnDqFNBmiOomqCZkMijVhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
وزینیا دروازه‌بان 40 ساله تیم کیپ‌ورد، قبل از بازی اسپانیا و کیپ‌ورد فقط 50 هزار دنبال‌کننده در اینستاگرام داشت و بعد از درخشش در این دیدار و انتخاب بعنوان بهترین بازیکن زمین؛ تنها چند دقیقه پس از سوت‌پایان بازی، آمار دنبال‌کنندگان او سر به فلک‌کشیده و به نزدیک دومیلیون نفر رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23546" target="_blank">📅 22:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23545">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9iHqcwqPxBaPMrdIcsZT0_OlRIsbAQmElz17_vSqn5daGvGwdEO1b5YlquzDOnNEe5gBtqaGgsLLnWBURyDGAQlPkSX3p2D9roI5MmChfiKrrD5-m7YABIXIUeJsOxU3YgyiDKZETLdx_Dd6zVIyC9-swy1_NRF1rdqBTl0zJD8CCFTEtqZR3zRofJKencE2MNmFQjW_InDjdllm1TH6k9fduZ59vuSqMDBQZM8pxeDJ6vn_sks2AC8Bgr0X3D2T6y9DfZi8qrGHPFiX5yY1B-WqIZoSbbYeYsnCkjVs9CztsRj-UJ1577RoaqPcYp_VTYeb9WpBHdkpGFXyu2JqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23545" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23544">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlvvF-9O7bba-ZhW0-SwF9piDmvjhIZLnroNL1Zb2yHzFH_B0VITmUHHEjbnWl03SgFRovbDZmEFVXf_FC9NhD_Z6r9EaCcDpPEmDOoP2ZBA8YCTXCRIF4uhis_iikr1cZ7oMIHn6w_i47KuD1xmnEYGG83JKE6JhX-1eGNi5BQFothEk9bSRBK_vXoDpbmhGJXsS8UBJIta29L-hmxT_gsv7ntXCRvHPgs7wnvD79LEQwlALrLxe8GpO3B_5VQjV9didmLrwhXe-dtguZQwzpwt4eu4mkuQSuebZJXyzTefv1AKo7sRkHZNJyTIKF3lGRyk83VkZWmQ0ZC3VNutlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
جلسه‌نماینده کسری طاهری با دوعضو هیات مدیره باشگاه پرسپولیس دقایقی‌قبل به پایان رسید؛ ایجنت طاهری به باشگاه پرسپولیس رقم مدنظر این بازیکن روبرای عقدقراردادی ‌چهار ساله اعلام کرده و منتظر پاسخ‌نهایی مدیران این تیمه. جلسه با تاجرنیا حدود دو ساعت دیگه درسعادت‌اباد…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23544" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23543">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMBjX9DJqKYJSgQ0i0btn6OYtPSkwUKJaF1BtZBOJbN7MKWGVGfNlxhvM8PlcS0zgay1UbrcwW-lzc-WmxqV9X6OG1_z5Y6MnJzx7khx0HOiLTqhiBh8C9fAcjYlVHaXCa35Dyu1hAg7I4uMDMvCl2hbnnEvRX9ihxHl5mOHF0tNhu70xWRmZsT5ylQRBZ5BWgvU6-WVs8XcMTg34gdX21IqpItK1FrY6cnh-BGvK-naeCp0Q-boQeR1J4ujZRHf8m42Vpu9kArLK5W3U0fNxrRng8K-PCCXq-15dhAk_sqaFvOIEGb-xr5KcVhzT24iaClVZSWXUbiPKt9oNI-ZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23543" target="_blank">📅 21:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_zQIx2Y776GvsESZ98FQFKMLbIQIZdD8W87qKPFJCcVeFUhF-PAEpjjr8Kt2FqYBz38RUT6otjiMhR83EJfEU_fDSRIeXbBMfnV8hqrD5IvAJcvsivTPmOhgtTMyEswCgM6shG7chCYrCoF56zSZy_sE67a6WgcGVJk2KMO6CG4CttNdFi4jFUH6MYyiRbKFXbDZKaDJ9ii_QrTMGahutUIZU0BqS2xQGVkgxc5OHAthtmDyrNV3GxPPieWjMUFYOp2aHOiR4aJnoSo91jZuXz0E8xaRKwLyzkK8IuugO-DnQJykdsk-3ttFAHrt9su_zcGhFU4RD2pkecDlKO2nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23542" target="_blank">📅 21:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23541">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsETyOy-720xWlC6hkf8N6pR6m6NME29uE1X44Q01j1M43LY98w-NiaTVF8vZ3MfUN_btELUZcO-HmfoPBju4RB8Ra1u4cWXUB46dsP-c1j8ij4tWHpwdCHkB5nvjPHzxvD_TUyLjVaz8J4MW50SZlPELUnhGgrb2t5SJtNEbHJH-UOjbzYlcxY_oVipi9pB9rBkrwMAg14dRWdoIdXfeFsSS4JM1GjrgwrQy0H1BkBPpdiWfjtrI0HNZyLLOaJb3Qz85lsrRAu4Na-OYJ7tSZlJiIiCRpL1o_LuOVGrnB230Y7ROFXfhcShz1MGjg4xRC0G1Tx5OJLiFLTOxM4qeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درو‌ازه‌بان کیپ ورد در نیمه‌اول دیدار با اسپانیا 7 سیو موفق داشت و مانع باز شدن دروازه‌ اش شد 40 سالشه و ارزشش تو مارکت تنها 50 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23541" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23540">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1PBg-jy52k1hcd5Bzfhw3sYQUDKJz_rZZ-YHJ5NyYg10dz0SXt4oiUJEkfxmszVqKAaswB1yajPt96aA3LzykSwDXyS-wx_m1b03RtePn6Y3SlpTBxI5p7RpJZl9DLyGxzShUArSRXJLs6499NijmGWY14O-9mqgiOsSL1zIuJ4v1L7ddUwEIyAtxjlTb14R7HL3r84zfSFkSs6MX3vUbYBSbM-nXHYPm2oBtLH6IMH3M_DmchWgE6VuCAauL_zQCGA8sAxIUUQ9kQJDd7Yfho3u7L6diuDWwwdqk8-rDQ3HNOXu5QE8snfB0Ujit9YmYqKnkvW9LTCluRez3QeqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای هفته‌دوم و سوم تیم ملی والیبال ایران در لیگ ملت‌های والیبال؛ هفته اول تموم شد که یک برد و سه باخت برای شاگردان پیاتزا حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23540" target="_blank">📅 21:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23539">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvU5mlJHi3z-OTuDRPvqAaXTsAPg6t8ttQV9i2GbJQIGH9gI0UoWq8QvXFWVFVR1Qp8_52tO3jzNGjXJgKvhoKqbMb4jeBzg22TnXVeEh-frF8Xo3hIE7pSOHHHCRfTsqbKwk6Qew3y0fKt3MrdXNrjaUjte0LfqZLkN_2P6WePqSFvBg3UnnpBnSpRsy-10TmgutL5eFZOZMx0F1J2Pkgg5aRCHvQOfMVXqfM6uVXjjo3Je_Ky2Gy5uZpd0JpcJSbDbkFknSLQd47fMJalghZvdm-kQPj7Ejs3V26CoMGX5kLIwCdCL4hdr98W6yVPJoziG_4TJLXUqv9XSRkP91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23539" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23537">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTeSAGRsMxHzSvXavu29efBM9K-5EUWH756nz24unT4l7-rR0TlNLqroI3ZLDlcqnGZ8-X2ypDKOtPwN7rydu5RUGr22s-oSCbvr2-cz-VnFsykxG0f_ovf1x7gfpFT_BNR8oxtJFwG8G_lEYChmRtFT1UI-I5THFeu-ZTZEqDIkX6IWsUVqcBBRaXMh3kBuBZ2-_9pyrfrMcIkrAKS_2MdURzfqstaS_FRrQLv-mfqK3Z_cU7EcVucxOHQA_yfPWEP58gkmmEJyaCQ74Rp9UobYXb0_uAGKSgVAfhbtNiLNarWNPA8ksvrB7fe94PqdwTQLDxvKQYEmf_WtzR4hvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛
فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23537" target="_blank">📅 20:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23536">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjvRm4c0ITb6502TNlUODtu7Yk27XTZSJQxqIHMLUWBeXKc095N8mjc-WUsQWlVKTKSJDgTxFGJwt15zxeN5tv7ut9tqNLFPQpiwDyPsZFeTXRuXGKOIvv1toessmytoibBbSWexDu3AWmJy92xSAHahQrX5euV1YY9F66SjzUZlNabzT57JlVVW2DKMGL8UxvP-heRksIBUnZuj7MFG3dnSurSZ4KXNjUEkZrp6-V-7yLTVR6adeeK5kkwsDWUE8t2fhIe42CeCb8LPRXAKQE9Ce0uQFDL9qUbxAo-Jf3wagMoZLYRVPNhUhg0Ucqsp4_XziJjD_NXxdPCYLNM2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23536" target="_blank">📅 20:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23535">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhVaIchFWmI7wJnrGM7qujBWxBZhQ4jmeHTmgDwl8LcPrJhqYojjOFppPJ_E4tB7IxzMoVS51baiajZqYTCZdfAQkmx8pavbq48IIGS4_FSq9TgCio9R47oMAd31rNW-pC8N529Yvc_5OFDW5JyPA_YaILTEIbUqIavr3fqce_cFGMUjGv6XPpVIgsHN0kpqsWPhagf9uFjGcCiSuLOj8C0w8aIscmamAv2MJ1X3VaGOMEafRO-zVj5V56BrdajqGk5-cK0ldwaadmnWejv7AysOwfb2okBGP5_8B0Ua1UDftdNNKWNrbi13o44yZLpbxcf9UwFSP5kqT7CM1E_byg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نتایج‌اولین‌دیدارهای ایران در ادوار مختلف جام جهانی به‌بهانه‌دیدار بامداد فردا با تیم ملی نیوزیلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23535" target="_blank">📅 20:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23534">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=SoyJKzP-J_V3XicpLSMLXY7SWjhPTNxFLOJam0dMp9ibVeN_SPpT8K2MCDoq4EJB-noNHwuh4_-R9QNPSglguJ9Gq-Jvg4oHdE6xyaJQPM6ScQQ0ekJeZsQoB94ahP5fI_XsI3rHJlcaoVw8ddHHvALdgzeE9X03-PPMuOKpeXTkK4ZtsqyxTBWeq0kbjPfsLurrYUfIENdhdhbyCAByv8cUt8wI2Pg_JA0UTJEJ0vXET2cZyZDO9CHQkH9XnwP2UT59_ccVAHm0yY9Y2OwozEC4EW0X_q2Ok8rVOKuiKpPDhJ4GMTkkujhEaLkqWB2NqMw7MGx38kxXLWilSEOcQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=SoyJKzP-J_V3XicpLSMLXY7SWjhPTNxFLOJam0dMp9ibVeN_SPpT8K2MCDoq4EJB-noNHwuh4_-R9QNPSglguJ9Gq-Jvg4oHdE6xyaJQPM6ScQQ0ekJeZsQoB94ahP5fI_XsI3rHJlcaoVw8ddHHvALdgzeE9X03-PPMuOKpeXTkK4ZtsqyxTBWeq0kbjPfsLurrYUfIENdhdhbyCAByv8cUt8wI2Pg_JA0UTJEJ0vXET2cZyZDO9CHQkH9XnwP2UT59_ccVAHm0yY9Y2OwozEC4EW0X_q2Ok8rVOKuiKpPDhJ4GMTkkujhEaLkqWB2NqMw7MGx38kxXLWilSEOcQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23534" target="_blank">📅 20:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23533">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eku5GweISnlvfy-BoCZN35zs4FVu7eQgFOrUF8jZ0m3TW6-QOyoYprlPBBX34fBorAknKTTeRQUPDFT69yleVM2BiQE0oARo8HRx1F2UFBSQs5UnKVkIGuIthUfkc1i6iUR-LWRmBJu6XtqVUjh1o6fB2FarjhfaIMEzhJiWhsK1BA3ZnX2Pvzf9GGcaB1ECNEiOkmKAa7ZEHGwLjVnpW-mfl4sHGQtRx6l5SiUDcEA4wAlkdXfjA9rzWwTN6ytm6GRil2R8BU6R1EsdnmoSqPzScGeXjFz629Q8AVdshB7aL_AnnAsxbFoBlXrnjl_6BtD2DhX-uY0HezGAdEB6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عادل فردوسی‌پور: مشکل‌پرداخت مطالبات یاسر آسانی توسط مدیریت باشگاه استقلال برطرف شده و طبق اطلاعات دریافتی ما این بازیکن فصل اینده‌نیز با پیراهن استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23533" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23532">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMRPD55i3Bc2yRctY1L6B270x3up3MvfFAYKDqL-xRhHXbgB0bLRS2N-yONM1Xb433__9SuAyFHZLXVQGg-_RDyKltdoFK8WHmM1MJF73aQFxNBQEo394yGcTd4DQB4Q3RWv_P1zl2iMFPpq-znTyOptADDuh_qKJHpfPY0YMY3b0fS-wnpoMGLC-nrkQqWjox7vqmRx5pdyM-RoO3GWagZLi7LY4jxLqpzwZRkfBmFDKH3Ybl8Wo3Cwp0LUSRr2LcPQKbQvpAioixuMoYUAYDLcrsI65JZ5O6HYculf4-coD7jMK6FjtHRqc2AgTm7OgPSGcgdC3Dva-TDHB8903w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقای‌گل‌لطفا تو این نظرسنجی که تو کانال دوم گذاشتیم شرکت کنید. اگرم دوست داشتید اونور هم داشته باشید محتوای جذابی خواهیم گذاشت.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23532" target="_blank">📅 19:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23531">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkjCyAGHayaVcChGJJLemnPaoE6u_bQH94cGFiRpupY3-yTs8p5SzbR_3mJWV6s5FFBGODNi8s1i0yRqYw6E9eXM2CgkrCrhHuJzdAVoTKJ0HMs4QBWDH-DIlkh4CgvQ69sMLabX4dPG6SUb9WDiR24CHICdHTaIFjJMyDu_V924v_kcfBM1f_-t37yWYQQjwT2aeR9aunQ-o5dZDHqIkS6VsHwgOOAdd5d6ijXaz0KLRU-9RgLs1YYNppMPH9ccIMMIvbBpiEYe17EPGS_5Hjwl88QbiFf998MEfYvgcB8blaxrk9XY7jJg-GMt-4Q8zeQSW8wvQdZf5Ui6D4W5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23531" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23530">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b2efb67a.mp4?token=biIng4PYayIZrULY1lK5CGkcIjo-fKsSkkbV-9Sz4Wec3KEvyLjdXUH1DKOcXGtMZVIT-nehW291DweEsg7d8ZQ9BqYXD1QMNvICB6l_aHfGvnXKCyrk-I06pchHNz18J-MehPtAKBp4g1I1WzlXm_7xR8V7C3usXPW8QLKbhgsqLIAOiLQbwe5FLaFqFxMrZ3t7X0Sa1GS3esa3v83X-Q9zwmhO9JEXqL5IruReP04RqDjoinZImdYfzY2GfjomxwnPT7UjNooz13qOG6Zkagurl2QScmlbrH7xBP17VJu36-wgiye33uhv5A-PkSJww2D2ujTnQIcGS54e3JOF8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b2efb67a.mp4?token=biIng4PYayIZrULY1lK5CGkcIjo-fKsSkkbV-9Sz4Wec3KEvyLjdXUH1DKOcXGtMZVIT-nehW291DweEsg7d8ZQ9BqYXD1QMNvICB6l_aHfGvnXKCyrk-I06pchHNz18J-MehPtAKBp4g1I1WzlXm_7xR8V7C3usXPW8QLKbhgsqLIAOiLQbwe5FLaFqFxMrZ3t7X0Sa1GS3esa3v83X-Q9zwmhO9JEXqL5IruReP04RqDjoinZImdYfzY2GfjomxwnPT7UjNooz13qOG6Zkagurl2QScmlbrH7xBP17VJu36-wgiye33uhv5A-PkSJww2D2ujTnQIcGS54e3JOF8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23530" target="_blank">📅 19:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23529">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvrHODZ3qUCd9M_HHV9ENYLPO9Lwq-YNxhgIeGhOOtQNv-x6jEKDuo1ZSgu2hAoNgT_M73ZGFtGnEwwf-jVUHlrm-zl5LeaiMhoUVwMnLAAaG-QA4Fb90a9yyuHvrP-ZFk8_1AyIUoPdTdDYfCTWBna-akZACeKIjl5A9AQXKmBhfEW-Nulnh9Hh_SDv4KbHrOnu356SFzsQetM8N0gRZne1WzKs777NgLT4m4TkslxmQtjM1ns7RkTN3HHCUlPxwMyOSjMF5q_CeUwvMEh15Z2S-3MPimYTczSYnIEQGWQXd_wI6aBtfE4pmZwwLYaEEHm-Al64PkDLfDvz2gMUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد...باتاخیر چندروزه باشگاه استقلال امروز صبح مطالبات معوقه یاسر آسانی رو پرداخت کرد تا مشکلی برای ادامه فعالیت ستاره آلبانیایی ها آبی پوشان پایتخت برای فصل آینده بوجود نیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23529" target="_blank">📅 19:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23528">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcADTew3E_FZc5fILI_dg63wo6PnmLRPlrdVQbxXgHDUdhLIzUsOuqW2M2yWEOJhcx9_QjZrBhowLGeXvQKkDVjH7ng8vzNFIQg_vM6DGhDKRe7EkhbwO3F7e-9XudKGhXCdYah6D4YMiDCRm7YiyBrHVW441N9u8mBYPgZ_ViSGxmxzCRdtDLatWefCGpBy-1VIP5Thj8U5ZYD-lpUp8RE_zjkInvhLMPyZOyodoNiNEj3jbKLwKCTMKGuAsd1USKAY3yq4CxOlsneUwH5XpVPkv3im60HIgf0Nd3FSIc736mEYJ_E7AxIHcmcl-Yr0cWmKGIAMcS-4n9A5hCGqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
بدن فوق العاده کریس رونالدو در سن 41 سالگی و آماده برای رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23528" target="_blank">📅 18:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23527">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kygVAWUKpD_hmSe3Ej7Eg1meqiE-XqHannekt1rlfNJrvI1iwntoEHQqpfmVJTvNqTI-AOeug_X_ZGdIybQsp1LCiNQCCUaliQXL-t0-MslKZdY2w2PndLIeY8ewphiNpRMY9vCpioCOuW4uS5VtkEffGPUvfmwcnJYtoIX3Faqftn4ZMs82KVAhiFToKaPpkldX7CB_lYnIyVU0QCPU5dEo5V4Zwrf2oz_R_wNfQX5aaJxkRoxMG1i61hmQv4HkPP7PpaOEG2tuRwzAwIotkt-8N52JjRTIJNTDF_qa3oXDZW9Z_otFM7UpMapB1eeKte0nBMReJ6iGUS0JcO5qOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#تکمیلی؛ال‌ناسیونال: یوشکو گواردیول مدافع کروات 24 ساله منچستر سیتی با رئال مادرید به‌توافق شخصی دست یافته و حالا توافق نهایی بین دو باشگاه رئال مادرید و سیتی باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23527" target="_blank">📅 18:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23526">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d57c883d.mp4?token=rDgO71aokdkI3iN9XzYcRvVNfXTeoAjcHzCc9ADMS4LdDF6N58IVwdr6g_kOmFdTQ1CfGT1euc5sPxHl5l0DHo-Gnul3wuUOAz5FC6H7aJQIRCNpjcjxp6UdBx8IYpVnPEHNQU-4eXfy7axkHBJqKSV19L-1EzxWED2wnyGLOWBdgOgSw2rdvuEe8K1nbCvAYHTv0014ITwHtqUaE2IKwKgkQYbDNO-bTyg7ACoa_8fW3segtaw7s7h6zBher_ERpEaw5BtutZ7cFErgNy4M2tNsIg0TP9G8-XpOiZ01egIPSMT3BIn7d7BpZDRgiIW4lHYy9-7WYqvBgqDWsi4lhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d57c883d.mp4?token=rDgO71aokdkI3iN9XzYcRvVNfXTeoAjcHzCc9ADMS4LdDF6N58IVwdr6g_kOmFdTQ1CfGT1euc5sPxHl5l0DHo-Gnul3wuUOAz5FC6H7aJQIRCNpjcjxp6UdBx8IYpVnPEHNQU-4eXfy7axkHBJqKSV19L-1EzxWED2wnyGLOWBdgOgSw2rdvuEe8K1nbCvAYHTv0014ITwHtqUaE2IKwKgkQYbDNO-bTyg7ACoa_8fW3segtaw7s7h6zBher_ERpEaw5BtutZ7cFErgNy4M2tNsIg0TP9G8-XpOiZ01egIPSMT3BIn7d7BpZDRgiIW4lHYy9-7WYqvBgqDWsi4lhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
برادر از 4 سال‌پیش‌تاالان‌داره مینویسه؛ سرمربی تیم‌ملی‌ژاپن با همون‌استایل خاصش همچنان میتازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23526" target="_blank">📅 18:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23525">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga25kIe3ilYAqOQZN4hpZwkbCckApJDcxYhKUiNEEQPsPIIQQ7C0yJT-R0hNcmoPiPT2lX1pw_YkfdJFRg1unC6vSmeDWr6lmVimtx0hLcirKd0dBwUTmKP2lYrPD8lnFFEEzC_BYlf5EEyQmuJBDCxs0biYMrLv4qpGi_XzlW9QS9ZXEnCWv0JfWtZtKh0tbSnPVNM4LYc0v6PkR-O0BhjZ4XnX86ppwCQXGOT-3Qmg2i7VCAQSSf1OvM5yVJASra6xKJG7EGfInLlaRIKUaHtFKV2Gip_1ZYPArVipJAQh3HmStvDGKGp95RqO6Y-gxV5aMjryemFzmYnVvAQdyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23525" target="_blank">📅 18:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23524">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bca14044.mp4?token=PxRn7GsDn-ue3Pl3WvmJnZOLUNJNvhZex66pnircFV9lEmKvSrLyb2Kyh6hbHa8lRQW2QniqtoU_B5WXKTLe-UIK23jgN0fDQc_amqWl9HVFLqvK9zomov3i1EOJrW18D8cj2d5STHyYnfBH2JAPPULlzjKJdHwhKbQD4s_HyFIudyu6wAqRPDtxjT3ixjoW10ywuYR8A8lqhH7hDK8QwPb4ZO5LJOPkeDio9PVoRzDEZZ_gPJWanMnNI26vEsnTkT8jPXtGCJt8IYSikeDWSNDWEcNW-HoIQoy2zCREeRL1AwJXf2MEKRwD-aRgpXOqZ3BM9fuHSsaBPSze17b2kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bca14044.mp4?token=PxRn7GsDn-ue3Pl3WvmJnZOLUNJNvhZex66pnircFV9lEmKvSrLyb2Kyh6hbHa8lRQW2QniqtoU_B5WXKTLe-UIK23jgN0fDQc_amqWl9HVFLqvK9zomov3i1EOJrW18D8cj2d5STHyYnfBH2JAPPULlzjKJdHwhKbQD4s_HyFIudyu6wAqRPDtxjT3ixjoW10ywuYR8A8lqhH7hDK8QwPb4ZO5LJOPkeDio9PVoRzDEZZ_gPJWanMnNI26vEsnTkT8jPXtGCJt8IYSikeDWSNDWEcNW-HoIQoy2zCREeRL1AwJXf2MEKRwD-aRgpXOqZ3BM9fuHSsaBPSze17b2kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇹🇷
آردا گولر ستاره تیم ملی ترکیه پیش از آغاز بازی با استرالیا خطاب‌به‌هم‌تیمی‌هاش: یالا ما ازشون قویتریم؛ بیاید این رو از دقیقه 1 بهشون ثابت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23524" target="_blank">📅 17:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23523">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3ye50dOqGyqeaFuzA9Q3vTeOZXZ3xtPUh0Fe8YOmXM6woMsAH-XCn-t6sRWdZ85F7tYMRxaTrwYIEJX511m1CDYsDoO_oGECJND5egOKfUCrgSOYI2afM4svSMDsIrp0LcvcxLbPRNfWSfaI3L0wI3u8oaWpBlDxrwnGybZwC0-etgYdwpKNJkXdC6BCXunxkxZCZzNy0buyqG1er2crF7H0zsb4N5kC2jrMVVniLVsemlzcFx1xNZmCFVSS2tt6uNIYoDYxRK6QUcuxi-Ren_gn4yhyybpwHwOai0zlPcb42VMF8vq8rq51C9gXIAWNQZan4akHP9miYmccDQNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23523" target="_blank">📅 17:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23522">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBkleuoTT9rcQPuPt90Yoq1W2vzYqm5xRYj7JFKtlOYrZLwyLVEO_lJGIsYCXiqDt-ZYwq8ZN7fyDrlnQ8n-Qs1s3LIYthTIBSxFq7egk7DVnfo5Hca1YXJddPlMbcBWaJghdskYOZf5zO83hRuryfACRte4FMNbGAglKXR17h3GCtykP_YzLFaPYPKre7YiYQfFfR05VG5kJKRr-FDtsxquptri84-XthNl3CRz3x42rMBoPqYgJ7qTa1P94RxhceA6OZbAthebmtHwRZYfn71grwR3NmKSDyArON-pl9bBwKINu2RnbCV72Djl-x5iJfXbGPz9YrKBlVEKBdCNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23522" target="_blank">📅 17:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23521">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXlWIpgwuLaKcZ-6vqA8c_lfyGT_JtyKivAju2p6C6RRwY7gY8eCqt5HS69BmwLPXqq8AsDKprNhsFIrDn6v3LeGZm9MSk5oxp9qO7mRdTX44mLZD5qWRv4l8f-uH8kBiveVpL-Ol5sqqHy9616gzZMv7Fa_cRRupCF1sYArBbpeNU92_hK0peTASiaLQs3386F4cbC4RgHlwjhjcYI8Sj7571TQart3T8bkSMdlx2N80nDk5LFNwZTxAbKQJTuCywQLLSP9GzoTgqMk69s5JtPQhomtx38lLh0A1OweQICxZDxGqlXNnfPU_QLeCfGcCH8Mww47BEp39uUfyK0giA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های دیدار جذاب امشب دو تیم ملی آلمان
🆚
کوراسائو در هفته نخست رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23521" target="_blank">📅 17:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23520">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7870ebb64.mp4?token=jxMp9I3kM-Ninm0E0mtPjhDiuKLY40L4NCA6p-YCVt-3Vx1LP1pHRA0S_zPb7a_iYjTutfZWI4xeOo06Dm1k0zneArU-_8EjkzWQjzrvaDA1h-kEXR0z-OFynpL_Klo7GsRdnusppbTiQppsfdWQzsEFWuaL3NtCd-DTxBHplDSrPwWwC6JwI-3iaTK9B1F9v6Plj9eJJ2ZnVUCSnQOgv5WEV_TQd1bPVMIrKh9_6yj4kgCz2DsgBWHVqY0ZQRP2L9L0oW04b5ZhdON9YfgpWy2iTLY6Yv-MKU7FPOyuhDYzyn11O_q6N6SLf_0WrkoU5fT6mJ-Xqc0UXXpPTMyCixmvT9MuBsScQhIIbh24IW_DGwJpGrcVYBznLxrLg4T2Bq7Ghp8KUo7ySZLxaXqv0cjtstckHZd1ovmCGDyyESAIPVaouCNuM7GF4LajOEZBEl5v7xWMfK2HJEGCS5HsZGL4I2BUFGPc1gnQRjkCYygHeguP3IH1hsVfHDHUhuyVgETJKnB_zfk1_OyKVv8rH3kb428N7PXunlsclBL8kyd2i5M-qihKUbG_iWZHaoZhSwJ3yu8Srx_29xdUIAOeQyCkulfTRID45PTG1xIueb-gbtmc1Po1JwaFeNNiNuWjvC_iOs8wKT8KgTIU0Y1JqemUYjaRRh1vXi8UYZQgNWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7870ebb64.mp4?token=jxMp9I3kM-Ninm0E0mtPjhDiuKLY40L4NCA6p-YCVt-3Vx1LP1pHRA0S_zPb7a_iYjTutfZWI4xeOo06Dm1k0zneArU-_8EjkzWQjzrvaDA1h-kEXR0z-OFynpL_Klo7GsRdnusppbTiQppsfdWQzsEFWuaL3NtCd-DTxBHplDSrPwWwC6JwI-3iaTK9B1F9v6Plj9eJJ2ZnVUCSnQOgv5WEV_TQd1bPVMIrKh9_6yj4kgCz2DsgBWHVqY0ZQRP2L9L0oW04b5ZhdON9YfgpWy2iTLY6Yv-MKU7FPOyuhDYzyn11O_q6N6SLf_0WrkoU5fT6mJ-Xqc0UXXpPTMyCixmvT9MuBsScQhIIbh24IW_DGwJpGrcVYBznLxrLg4T2Bq7Ghp8KUo7ySZLxaXqv0cjtstckHZd1ovmCGDyyESAIPVaouCNuM7GF4LajOEZBEl5v7xWMfK2HJEGCS5HsZGL4I2BUFGPc1gnQRjkCYygHeguP3IH1hsVfHDHUhuyVgETJKnB_zfk1_OyKVv8rH3kb428N7PXunlsclBL8kyd2i5M-qihKUbG_iWZHaoZhSwJ3yu8Srx_29xdUIAOeQyCkulfTRID45PTG1xIueb-gbtmc1Po1JwaFeNNiNuWjvC_iOs8wKT8KgTIU0Y1JqemUYjaRRh1vXi8UYZQgNWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
پیش بینی 4 بازی امروز و بامداد فردا رقابت‌های جام جهانی؛ ببینیم چند تاش درست از آب درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23520" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23519">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc271fde7.mp4?token=IgbCSnnQOq2vMOdTh9Fo--lUYmje7st9prOOe35jbwUokwlTOeJF079UxzK1UXj8VwLRSGyMYlq2eRjcVaNWyyMaCNaLeBEUBmM7QTW8JfP7uBMEgDQKJgPknr1mNdGWqOL1H6iOhBNgOC0vIDx6csvUt0WAoe4Ta16KrJeJSD1FIPSC7GmXAgASC7qHRr0HY8PHS7qfwksscQX9KV2D4tDYy-Jeq96nMMayLbzLQKLByvJfjy7Ov2q_M46u3elalZPA1TDuIvDLgSnzNyOpEbvilm0lX5b_mQ_quSvjw3rCEzoAzANYTKcoWJF8Qwt9ZLU8dpw4Fo_1yzJsjie3nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc271fde7.mp4?token=IgbCSnnQOq2vMOdTh9Fo--lUYmje7st9prOOe35jbwUokwlTOeJF079UxzK1UXj8VwLRSGyMYlq2eRjcVaNWyyMaCNaLeBEUBmM7QTW8JfP7uBMEgDQKJgPknr1mNdGWqOL1H6iOhBNgOC0vIDx6csvUt0WAoe4Ta16KrJeJSD1FIPSC7GmXAgASC7qHRr0HY8PHS7qfwksscQX9KV2D4tDYy-Jeq96nMMayLbzLQKLByvJfjy7Ov2q_M46u3elalZPA1TDuIvDLgSnzNyOpEbvilm0lX5b_mQ_quSvjw3rCEzoAzANYTKcoWJF8Qwt9ZLU8dpw4Fo_1yzJsjie3nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
تو نشست خبری شب گذشته ایران - نیوزیلند یه لحظه ارتباط مترجم با امیر قلعه نویی قطع میشه برگاش‌میریزه‌به‌مهدی‌طارمی میگه‌این داره چی میگه طارمی داره میمره از خنده‌فقط‌جلوخودش رو گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23519" target="_blank">📅 16:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23518">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9720dcdd27.mp4?token=Q6WJQwIDSs7dcdQtHiWK4wd4chcqCAxYXO1ajkBR69NoBhlQ_h1xL3fIIM6ZOlGgYUcW5iN7NM9nuWD7lcncLHlUhWSYBTW-UsednkaQzitUVHIWpsfS5hCulWZsNDFNn_P8WQvL0FVLzZbAmmP_33LXpPYyAfT4O8ShMVKyFPOUrzMpSZBwt8VJQBp0V6HmDZe5JD9rvB3ZUDmWBzinPfjlTRrYW3dgYZdzop9dzGJAJB6KQxt_bFPdXjIvZn35KqGk_Cnt6s4aj_Fs-6pKn12-z1ZIVDscK-xAKCcUM5gTtLGq_CHceoTKBP-lWoXeq9U1Mmm8FWOfT2tTp4_O9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9720dcdd27.mp4?token=Q6WJQwIDSs7dcdQtHiWK4wd4chcqCAxYXO1ajkBR69NoBhlQ_h1xL3fIIM6ZOlGgYUcW5iN7NM9nuWD7lcncLHlUhWSYBTW-UsednkaQzitUVHIWpsfS5hCulWZsNDFNn_P8WQvL0FVLzZbAmmP_33LXpPYyAfT4O8ShMVKyFPOUrzMpSZBwt8VJQBp0V6HmDZe5JD9rvB3ZUDmWBzinPfjlTRrYW3dgYZdzop9dzGJAJB6KQxt_bFPdXjIvZn35KqGk_Cnt6s4aj_Fs-6pKn12-z1ZIVDscK-xAKCcUM5gTtLGq_CHceoTKBP-lWoXeq9U1Mmm8FWOfT2tTp4_O9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت ژائو کانسلو ستاره32ساله تیم‌ملی پرتعال وباشگاه‌بارسلونا از تراژدی تلخ و سنگین زندگیش که در سال 2013 مادرش جونش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23518" target="_blank">📅 16:43 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
