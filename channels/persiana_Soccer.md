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
<img src="https://cdn4.telesco.pe/file/EU5c2yAGjUBlWox8KcvH719BvL-vjFYZQNAhIakn7AAq5HIIESIQ14X3JtrDHabn5MUrZmFP2Ih4jn_OnIUWroAlIA944hM19StBUUC16xcCq83NS9uz3_WV7XJyu-h6_4-I_OSZe1kr0f1H807Rfvo0kyDYGkK_RGEjYDBX14Jj2BM2P1x2dL67EIvzeTQGkeQ-_8ecNBSsISO0HWR3fWAygNbUzppnlKHMqwgKUqihvNsxLUrTeVJwMSyt-mecCY-BsVXdRO9BILqPmEfiGeTvbJSoq5LI_EACeEbdwrCESit2_AUK8B7k05npJKTkPvigpGnytCF7AWsyBdbpGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 318K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 09:53:06</div>
<hr>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWCPrDrMzlnNd1J7RXDliW_M7dZik636rgxceQ4-6oIipsIHY_mce3g_xYAdiCpb5oN03FmXFAzGSyG_b1smCSSi-Qa42Z2AHCnbv8_kMd0k5q1UvBEpOKlgMxTJaZEdvV3sxM1GH3-huC_SqjXe74pqEs2_J6jx1rxq2zffONTZrKsxSwPOpxU8mFzMweHpa_ETUYTpQds0VCIbNh0pepE0wFRbztzQ6W53rdIHDKwiXmsxNAtLvHroG3i3jCiiCKsqFgbvpu1E8gvsuw7gWsOxdtq3hb8u9-gFvndLb_WMm3qqInps4nRpd_rtqRa4twijk-LMBB51-wbfImgwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=U6z5saCjFHR6glbEuXFmN_o4hi_PjqeDgSDdgQSHPW1lrx20LYoWOqqCWwzdcDQymL0yPjr5WW__Q_6reGHDouCkfZKSxna9cbaIQFRUHDQm9rEuUZFkGKdvwgi3F9xJI8AWSzUa9Z62Ot3vY9QxzxWfieSULoroKnd9TOLxwa5nlh9GJRtAva1KOH9tqhwHSj-f5UPLgbfdrj8F1vjy-GrdooSkhFWKIYcTyfk7-zhaUlTgBGXMNRJP_UOjhKMoC3_Gn7C5M_mP6jK6WkGCRP5ZFx7OQrwe9Wp2OnwGAySBXMxIdz7mo_DtBf40n0nQHYU87oPrwGnbkKUjSGCcVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=U6z5saCjFHR6glbEuXFmN_o4hi_PjqeDgSDdgQSHPW1lrx20LYoWOqqCWwzdcDQymL0yPjr5WW__Q_6reGHDouCkfZKSxna9cbaIQFRUHDQm9rEuUZFkGKdvwgi3F9xJI8AWSzUa9Z62Ot3vY9QxzxWfieSULoroKnd9TOLxwa5nlh9GJRtAva1KOH9tqhwHSj-f5UPLgbfdrj8F1vjy-GrdooSkhFWKIYcTyfk7-zhaUlTgBGXMNRJP_UOjhKMoC3_Gn7C5M_mP6jK6WkGCRP5ZFx7OQrwe9Wp2OnwGAySBXMxIdz7mo_DtBf40n0nQHYU87oPrwGnbkKUjSGCcVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبع سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxXGRvLH8Snbgjd5mgOJVwonQH-f6_harj3PiecHDUsD9UjLLN5yThw3qkuTo9ZSYMKfma8tDPQOGM5YYMlMae4p92A-7mY2O1SSuOcPydKL0X-rl6K1zdM0yzZZY7aRSskwnTkOgNZ6KppQxqf46PuGVVD_4onzv6WHV-gu4Mp25RX6XoiNa4GDObUs258kDVsAP7AF0RXza55OfkNAIF8Ly8pzwrBRCmsngITqlAvE0VjmCF-YjwBrvsemM77cgejGvLZR7OUjMcufdbXhlsf8hw0InPWrvm8mRjsx1vyK1LR6L4fG4weVa2Fep6Ff4-lGC5ggoL7ZRn-8m8jSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXb_BbRGDBn4rTzXVb4XhwKGbe3TqhFfteOl781iitFy8lqLh6Mv06ezOu4KHFQ_tJdiF-1FlVVuwTTkd5MLAe-e9p8hOpOGgo_sNvwmfdirXuXF15t-toTQzG6N_obYkV25QrP4TrHI35Y4CYoaaCSQppkmRcrI2DEIvN55wMs0m-p7ZOzw_dasTcn7Df3sRcsXdgch6d_XIHb73wH12t_rLdUxp9m2CfZvbrqtD7F-gUD_JhdSCHPCNJSiQu3FLz6wzFtPgpNXwpm6f6seDf34CEeUaQY476T3jgCbaRL1iSXJ_ax19Jpp5wQzPw59DXDPF_NdkXi5nz-wY51sNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJJH6goyXjy6R9jZ3yBDy_xo8msXxmaqdexRl7xg3rICQQnCDGiohZblZFIPeN6mYbZ10rqra9Sxrk7RobvZgKbxk4J0xJKg4SxMdy4d27tWTmjmp1Omvcsaf84Vtm5I12c0bJhq1qdlsZ611AShhk3iYIaLJ73q5TRBUfeuXrFbcRwjJntnR8FsGjIF3FynMqyaHOTj0FtDRjJfm7cLMcMONp5HwzreHUe596-YrzZMnjVpTCny1x2yYec-Rlv3bEjtbsMw8JiYrp-5UGVHMb8OXnV4x14Cs4jkWoHwiUPx8xH9LZFM0vMIeYgNvWicTXHe7hB3e7lsJXE7txuBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzbT6Tk2ayTABkq_Wz2sGXnKdTdVY_87WOfL20Ojlqotz6Ar0oaVPqjuIdfNFXVnu6jDfMMkh8bXGTfun0_0xE1dDzq6i9OIDWoaitQWYN2yO7fg_sk06SeHoZ8bj2LSrqx9fJ27L0w1yGa4fVwhM4LK0clv36Fu2yETylR_p1WkdoozNLgOZOz7cQEzwfPSr-rEE4y9JirtMxMzS719Hju4z8L33sS3awE1QHLBvc3yxf8sILuH_S1Va9aMa5Okva-dQcbUUwxSJ_pnbsnSYSjqdCBMhS1FSMuEpeBCri02Rb3J42vxyO-aKW3U_y-vK4qVuORuiHBA0rVIC9D3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeElx7aN0rc5SloSe0hFJlGMVJuSTZmT59GoeUx6THAhJSY7BA_13RXwAi5glW5_YV-Dd-rKvf9xZGrwGcXe-LXofJkp62xtELnSl3L0VYIz2RiBbqPIluCByCwNy7EpWPp4d1DuaU9CSd1ILATJLAl5QyyfdJ7-bNlknMwKUsIMYS-e8zWO4NQVm3CPJ5tPcgu3VNxULHapNkGSeviJmbeUVul2SxB2I6NULIezzBPBZYPZU03PN8pxG4Orsw0kUcyk78q-XIn_2MzqEsjhP0DOsN-uIH24Dl2AqMA1oRjHKifvH6WiNP59ZPPVQo_oYJ0w8zvWFpaFY3pOaV2wAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwTVhMiKYofUrKnlTNb98vPqlSkxNDal1bvrw7u9AUsoWDAzd83MZMIw1VVApbSLyO-o9henudaRbXHeNN0CsYbXxbIpfQMPAALpk9gsCdsQXxc--upwP1ABMB5NL4vmNg7yYmuswFIOrHzK3m03MwmmMxudNYvHLwarwDVEfCopVYhPEZrnpjavLELW8uYDVEGGzkxfefdR-HaxJwd4_qhsV5xV0XdIgqxx0EIMVia_4VaTorvTDHV5lKp44d9L4mBmMa6wgFxKT4s7b3OdPyLxfJTarEs5PR_m7R2sFioyBmyM0ssYLdpeCqRGcNnUg0SFpZMBi9b66hiBU1s_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVjTH4lAS_MZm1ghiMkdw8DKjiWiJVXQ-RnAWYEZ3fn4D0O78WfFUhFHk4A-DEVua70gdD7La9hEhaRV8drZmHjN9U8FoU8zmg36dSL4ToAl6WmjrmSR-zoRFJbJxGUfwuR4SoHXiklBMDkrKOdknJDTJgProBS25jTpkgJV7vrTNH9ZuxZGO8qgyJiOX4LeWciYskw_fI3j_5pcBYENIwsNCGrUH2qnNDLj6rwG8u2WEfXyc7nSjYnvySAi_96KuUQsWh6vSWrdlRxQyjSru2ZqUUta-c3BZ0y5EhEhuYuimdy7xrQEfleFQyz7-x3LFrKdvkFx6dsF7Lo52dSlAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1uJw8l4yODDIVpYehAUbLN1YWhVnj42aSVZLBIdsUkXqDzBLwMTOcxjTpTmfKM3Q3W4CL3Nv9iD1_0033dji1e2u3Y_Jh3K_G-X-YvpG3Njb4ryaGF6xIVyzkLgawNbic2c6YeuPg-nfLc3KLDMrUi2HFphWqg-8Ftc412BVrnrwrCQiLrHgL86gPab9zs2F1doRi1MkHrL7i3AeIlg7Uj1djesKydumdxJxAwjvoVk85wyP2Rt-47h9Zh4vgw2Be7Q1qu_-5MI4TvKj1Nvni9sB39Ny-QQ4P7-TvNkbHg0Zxf4U-ZJUlK982OdVivHqMjRiqO3uyKPQaYeirw1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RelPq8vYmQ4NTzaQvBninuixSa0yX9VcNmpn_mxuQdMITFQa9n8oYhidNx_2xLIw02NPXjfEGlCVcvtFcveqLj1FUTyP83QoMiwZdNmWGUpTnbSCscySzEQthfCZ1XoSBz-mOL3NH82szLsf9cJv6I8458qKlr5QI8YmHuSpoXCTvnpqU-sP3ar2uH7P3JKYI5wL0p3B8g6yMRemMTCRJSwI2lAUUQtkcXG7Vja2CBI46KmZx2xe1GmwTb77AhM6jyxWWrisP4AT2y-WAbjXSedZYukJvMRPLPhQg5nFRgi9Op0dQhUxd36WMg9CVQbXW9ik0hZUYpR8yHZ0TLemoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4HVPo3d4IfL61UK2ZeR1l6suOQfc3FVaJi56hjo4jEvDJ21ovvUuK-zpDKSUk69SOiUoHjgELHGzVxofax8L0qFK4jf03c8YPDQsLI_Z7ZZsbmbzNASSEQ4QObu67Zwm_RP2ouGLDyHhoUV7aeV2gfk-KWPrY27ew66_SPOpvrTsvA7cDE0ENPwmn0j0KEzQ4wH_BApNNM7jGV89ttphdHAcHJgKEKgALPWWcA96tsAGKolXNLstyXcW9n50fJjm7EFGSdjCGasnHmFRDJ1QWiCBS11kAGsoKYUUhZyKgt1zwm8ehzgK0BJUTiqXzIr_4MwJXXMWB6DQTapKtyVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌‌های‌رسانه‌پرشیانا
؛ ابوالفضل جلالی از دو باشگاه اماراتی الشارجه و الوحده پیشنهاد دریافت کرده و درصورتی که مدیریت باشگاه استقلال برای تمدید قرارداد اقدام نکنند لژیونر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/24425" target="_blank">📅 04:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEd8Ff4eC6XcCrFX1_oTzfdkdPSYvqpbA8kviTYfhLsrK5oGSXsIhPxfjbg_oEgzQ5r0wub1FpqwdY6ev6EXAH9GQC8UGVtaWyqNkTyQmf_mdV_Ubhh-jZyXA7com58ih-4QyP3N-hk2ZFt9jBddRKgUO3NP-DjDE5X_4ZH6QNe9JOdiSaUMrHJCKxcnUmh9T0N5DeqMLsPjpdW1i0vCYwTLbuwgbqcNHMoIfQFHq8SCZ55vSSKDNoclWh45Xjp6cFK6jMXOcoZIQIO_8djw7dCOJTN6v10j0JOjhVNozFjvkEyx0kGc2azRZFaX38sD18ALvALyTDh8IKxzmoMdkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/24424" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=L9b_biLFgo1tBln0nnlYA-jQYfMTiTfer1AS0W9tNgbR5q9jVIG3PNGsvYqhmPTeauAvKqFciw0aD7O2n_3tvJHLzFbr6w7tXwjMo2UIjGVl5HZhpIxCsOzk4Hyl0CEc66cIs094rvB_mFh488dCn4frCVW1BzjiUFGMh4RGY8h4GgFshySKoNXC1GU9IRrZqjau5S9PqDzVw98p3n3mDzWq_UcBrJ1gK0hWBxpZ2fBO8fwUIUr0WQKhOr3hPpsuAxW_GWigk-MMZxYxx6M7iKZpYgRl9eGfsMry2emLILkTTH2tTms98VVlcBGdxS4q46Irv8bMxh1QQQM7hZXj1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=L9b_biLFgo1tBln0nnlYA-jQYfMTiTfer1AS0W9tNgbR5q9jVIG3PNGsvYqhmPTeauAvKqFciw0aD7O2n_3tvJHLzFbr6w7tXwjMo2UIjGVl5HZhpIxCsOzk4Hyl0CEc66cIs094rvB_mFh488dCn4frCVW1BzjiUFGMh4RGY8h4GgFshySKoNXC1GU9IRrZqjau5S9PqDzVw98p3n3mDzWq_UcBrJ1gK0hWBxpZ2fBO8fwUIUr0WQKhOr3hPpsuAxW_GWigk-MMZxYxx6M7iKZpYgRl9eGfsMry2emLILkTTH2tTms98VVlcBGdxS4q46Irv8bMxh1QQQM7hZXj1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
عارف غلامی بازیکن استقلال به این شکل جواب صحبت‌های مجری‌صداوسیما رو داد: آدم صندلی دزد از مفت بر هم مفت‌بر تره. اشاره به همون شعر شایع.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24423" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUNMOVAjKJFPpz9CLPzspDZE2TidhB729TLGLqwvsywXuRL0cjcsZ7ybOC7zp2M8W3Dkrp6CMDG9sjtwOBfg-jrqZWhdTX8rlCwjdNRsqZkkByK06bcMS3Q0HDXeeGWdSf-6WNjqO1wUkpjPDA9-E4276-ckSnjiVQKOrQ-EcIU3Q_FN9qoDD626prLxzEr00we2QeLEHAWYVcaDMInofkTCyjv368QImCj9QVhHaSUALwIfzyme-Rk-ySiSh8oUmKs5D0bGJl-ICsGxzJFF2HtKaZNtfoX0S92MR2bRbLoSsTxHLhFINVeug3okZY0kuVTayg1HXSUTbAS64qXG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ایران - مصر | نبرد صعود
دو تمدن بزرگ، دو تاریخ کهن، یک میدان سرنوشت‌ساز…
این فقط یک بازی فوتبال نیست؛ جنگی برای بقا، افتخار و رسیدن به مرحله بعد است.
ایران اگر این بازی را ببرد، صعودش قطعی می‌شود؛ یعنی ۹۰ دقیقه تا یک جشن بزرگ ملی
🇮🇷
🎁
شرط رایگان ورزشی
💰
۲۶ میلیون تومان بونوس
🌍
فعالیت در ۴۹ کشور
📡
رسانه بین‌المللی
📺
پخش زنده بدون سانسور بازی داخل کانال تلگرام
📅
ششم تیر
⏰
ساعت ۶:۳۰ صبح
⚽
ایران vs مصر
صبح زود بیدار می‌شیم، چون بعضی بازی‌ها ارزش نخوابیدن دارن.
ایران برای صعود، ایران برای افتخار، ایران برای تاریخ
❤️
🇮🇷
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/24422" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzjtjrlQmDnNjls3-e6K0oc8ViJwjouX-s333Yl_ClDjrICLDIP_UT3SW1JNGSKjlLY-0jz4_YKmvwBeTTZ5UF-rvN7XrHZVtO0NsOmJPjiMvvnGMfPzmOngLuayQPM7MCL8QLUm4Vbhknuwdj9HoXb61siGlbhy4mLDHpApOqub57I5WRdqTYMfGp_mvxVDVbOCBfNbi9zd04FQ_pUsazuN3-p3HmCtefWdyIUXPYpkF3lEVR0V3V3HAq82i-oR9CVOfYHOpsur8G1xzMKgFfAQmHuR5Gzco1zSXnM_hl7m-AoZB3WjNYYC44GvI1P3k7PyjBR-AvtMyU1_MJILMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=W1ped5xMLaa5kyAh7nsGUL_Ihv6lFpJRFIiZZKAhSp_hLRSsHwFwexaiLNXtAanugpx3a373d8Tqezek4Y-Z1-E3ashKDGo8wp0nKYR_1jaE9iTxmfubaAnLt5LyVcgwxBkEfVkryagFUaOi_EQkQVPy-y8e2f4BDPlGVgUlAcGKuX8GQF8LiboZU2K88OQcvzclutCO6_KXeOLSw0saPWQ3kFGxUUKWLYXvTiS_Y6PHYPlGHZ3TOE9o8wkonA6_y0pfOakyRaKOMoQ64sDZX1b-vjU631fETJxG3j2RZKxstD56mtpV0vd0DLc-g74y_6tg2k0XOcPhXoY89GCrJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=W1ped5xMLaa5kyAh7nsGUL_Ihv6lFpJRFIiZZKAhSp_hLRSsHwFwexaiLNXtAanugpx3a373d8Tqezek4Y-Z1-E3ashKDGo8wp0nKYR_1jaE9iTxmfubaAnLt5LyVcgwxBkEfVkryagFUaOi_EQkQVPy-y8e2f4BDPlGVgUlAcGKuX8GQF8LiboZU2K88OQcvzclutCO6_KXeOLSw0saPWQ3kFGxUUKWLYXvTiS_Y6PHYPlGHZ3TOE9o8wkonA6_y0pfOakyRaKOMoQ64sDZX1b-vjU631fETJxG3j2RZKxstD56mtpV0vd0DLc-g74y_6tg2k0XOcPhXoY89GCrJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NncNFZuVim-nahPDTR-YkMwJ3iBThoMTA6eagEZl05lDFKGd2DrA6gdARgJWB0IoUyeUOVis6OSNUBA0fKS6VAkHWDVOUWul8m4fViakcxE8YIYGY0NCPd3LXO7O_g0qdCNjyDVrLFOcwLixr9b9K7YpLcZGdBmjhFbs1s7BrXLILEOjMEeQ8TFuczOQ4hYvErNQK3SmYLscDWGFJsQFMDkld8R1o-8_nWFJWkbhB4fMHPY4W-ylslMeSvw-HvVhZySxG5ccQ2Yw8IPDolm8wHN8Lh_SgNWzAsYzzrZQSjGBkki-RhzGUrmPMx0IBd1e5xasu_jWnVL_e-Nqlosw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد چهار بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1DnXo8_ROvbYaLUsrXO9HcFtFhyNJvFfYAip7TYj4ISG-_N6FdF1Mp3Mw-9yNr_7ThxX_9dPd2CvWEbP2eCiPGTAXCMdfOH8ORJCeEEEhwV2eZz2i9erkipxPoi-B_ia71zHJONZVEdJs_wZP6-s8b1VvLgCA4z9Ai0nab7SNtwRf7dkIC2YcAc0ZKNu6YSzTgjYowxNgOb8purfnvRjaKuYwbNPMivJQajBXaxX6LS4VT59mhhv_FV3pdZ-VXa9EakPIEG2iVzdGJZpt6nDVHPlqqRfICB7rx2HrgILjcku20lbRf-wF4RttTPTwaKYXpgB3V1Ava7qhiCfTd82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaimqWgzoEWszjoi3c83Wqk8Ai-8FculBEA60tzDEqS84tUS-xY6GV3u8TEcxF8UjURMeZ5su_1NoYRI2t8b7QxPSDoQnt7iXdAPr6RGvmP4QFLEkvOc3cE7o3WWuN2SHQTwj2o2LfRq6mWK8JLZEzTCaQq0IeWCJRf5kqzcixROadxJjGYcJC6wDZiHXSo49WE3b5HCGHV4sQua1qc2PzTkP0-xFmSi6lsnl3PqVyKcevrF-B5VKkj9fS_lZzpofM96SXNAT8yTNXLKR0WR581jnHMqeoGH_sz0Hee0v1BSQCyT0Tg3_WQz133P1ZIK71Hb3_J1Gpi_o1MMSi4ETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPldQeY7imV9BLF4qFclFd53CPbQFTmDWuJ3YLZpYi_CFoZji2U1G25w3_XO-qLh0N7WFL1-FAuQgpxy4DjCa9-scNNSdrZvwNJUftC4oq_ZNwNUc2TCi4CEMIBWUhPLPuYrLwdgfGTHFKmim76m_8jHHkGXWNs7TVFM-B2FT1l8t6Sn9R9CJU2kDvjptrXmDSqDcDzlPJAg7KYYkHz2ImYEWGDAayBTCws7vOmMYJcQgIHHOB-0TA6YBkOO82M08g1zmLmSHu-xRafsihiDWCvxPWjEdHDj-Ed-UrcQSLVT-XIdvh7U1FbkJ6mBOIcRtFC3pTg3OM2RScoiyX455g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3TtugJiI4DRn1b2w2vrTGqmHxAF3qA65CK9XGWKrWKqh-V28bcwsYKNmQ67uYBhSLi96aqcorUrX8VMfitkecUoRB0drR10_55HC9bmIkq79pGyXwDmNcl-N-J9pvjAXuc8q03YNwkLiIJ8z3QPZ4W9UfkMu-4VZKv_fyJJHV4P8K6FH2FeltBgPJ68eICg-0HkzgTtoG-O1QoVjPAomfdGqwDuxHBcbU2wwR9LU6E9jJ3ywLeFFtGou8R3ToaS8XMCtOTEaLXbWTCp-3C046RorLuZ3VNYEINkRNFnlWDYKmGlwdNJEO3_Z2ZL1tDIhRaC9LGI8CC2_iNhYMNDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
علی‌تاجرنیا رئیس‌هیات‌مدیره آبی‌ها: وکلای ایتالیایی بهم قول دادند تاآخرهفته پنجره باز میشود. انشالله تو هفته آینده خبرهای خوبی خواهید شنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/24413" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDd1Y7vs8bTLfoO6MiUg_0iB8ywqJyj6k-p-as7GWN9yI_h84MFYzmY75CcISRgclAhcRXRsiT4rh2fUuOEQMdHtQ_410lqebZqUBtOilbXZKASJqEbyDS7VhVJc-LW_t04e1kL_w3ohGJMIr5BJPtqR-3l1xcfrPNrvguRhs7vrtz4DTJsN7_gtnpGUpHOIbPlWnzJRTHKCdTzhpJ09pLmIDbX-R71ofa4TP6ycWQaTd5f8WsZ7IIxawCuBVtlpzUBMSvoA3CBmeQCV5ZDcV6YgQHX8swGkthKU1wpSdjzYjUPvn2p61Z6BsTE55tk2IOnlFD8bj-G7BOP8rG9SQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله‌حذفی‌ رقابت‌های‌جام‌جهانی؛ داره کم‌کم جذاب‌وجذاب‌تر میشه این دوره از رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/24412" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khKSJC-hVW53aWxtw0_QsQEoxonrPXJA1Fyw_S4pVy_HEy8138r4wTYMfgHsujvNuw1_JTozYrVNAmNmXTTaBPgefTQA4IIebDm4xvsFi8IM-mZ71Xh0SSrJQC04tW6Di2k3BQPrhj1uZ_U3h0ew9Y7PTAmOJJcCBbIU_djPaFIxpHOkpHlfmaKLYcUVgCxzyB71N_tLluuX01VTUjBy1U1e8IkwoIlTa7Vm9S1Aw6bUbeFa7OBLG2k4qDWRmOvaeTS1p_kSIajLO7q5vVU8MKs0O0yjhWs92oPK5wEOrLWRZg5-HUJ2tOwCFaa0Xo9IdIRczK0PahgYOw_8ey8kdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24410" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24409">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR19KrBS0voWMfhLFJMoHUtrDuwxSGQsRdyy4eCLUYjurSwLwKk60yd2gUnoICFXVEYGgEFOKGyzHZNVUj-lqttWk1CSI5JjAdDIIURPFrUDBAQ5uLvKWQwiAEivMo0MRqN6xF-74Nh-kYeLxIYMH4U9w4wgFMZout9GGC-uHWms4JVBW_f-JNcmNF0ArN3G8LrpB4NWycpjQhMRM3So2U3BUasKaENi8FeQCk75fkggCyc9HqsD-jQJPaS1BO55v3eB1AKKeWRHIQbKbgYQNSp5nmtBNBIlESdwyLbLtPovOOICM8vZDJVe4CYOMKjUSpMrVINGJoZBGwWaRNb0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد چهار بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24409" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24408">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_RZXn0mSUSfvmtCbGKLuuxjLsN7M32UO2Xu5RTWyAYzTm6pCO9z7073b4KcAlOM6H0lqHEXshoL-gzddFmM78MNxbCWGOgQ7l9hLW6TlaZTWBIBwlJHDh3fELQaSUDoro6QIaNwXQ44F4ymJcz-8QAKcOWbd6B2F0BTbNBtyzHJ_XDl9hZg09xMdB91K3UUR8te90Ha6RFG-xuWI5QnOrf98WJcvLz35FfH4JX1E-XAr3cGox2ASF9ZnmtKlYzEwmGUb_c4eeGY5y7y61tuNvhyFLD_4IVAZEcWRhbSvH55dpmJ6ciha_raYf8Pv39ur-_UIbZzSMzRy8i9HzMgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24408" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di0cX_GKYFHbfytoa1IU28KDNzdCoV4v7DJL7J5Gj4RVIDYj81UTKreO4MKnCj4FZCPX9UnewaPpQuqHH5xJyLLst_wwz6199V-ApEjQKaNj-u6JGr7aWXqQLtfJhQU9j8Vi5sJ6cd0ZCT3MqKBTbizxSTNP2HdX5YI5jVrYTFJ6uPuQlTtAGTr5w5r2PKCIumFBhBrkQjT3MJc-_QDxY3JimVDo1WXjWhS3s23UQM3CWnejlEEqbzItikyNatkRZwTOwuu4jEZuzbV4HU7MpCwHNyuqHnsFAOw6d6RaurMLIEhwqSgx3VOwHw_h0CbIXN3ALDKL9vgz4F3M3l05Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24407" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrghxVjyyvcvDzgUUJRGcoPegUObdojViEYJCuQmhY36QfWe9hf9uAQZidM4fFW-2qplk9Q0IgLWPs4kORwh1-Tm7vTPFt4mqrPwM5jsrAWh4toCeRTcjBzkuZntG56iUDMbv4ZTo4heufmDC25B4455w_8F16HiIqfad22jzx7MT7v8-j5kUZmhBdZ4AfiGFa1R-X-i0oKT92w0HRcve5NuLMS6kuKSskTGGxQ7YvCzHIMwTkI82WrnhgXYWsozzZuNuCAxc0cWEYjvUR3l2ERBRYHW9HAQWX9rwxf861CZD5-ciJdAYAORULAnZ5YJqXYfj21IizufgNgVKVjmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24406" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=IbjEG-lHZ_K19t0NzU3mIbKGda7LoZDxXz5nzY7Pe2BNWh0HGwSB4ylDW_aL8ldMUXT5XxP277JYFHC_GszD6Q0B0KjB1SeCaMkssV3lzhUHIZbEpbi5hLEuPF7Xr8UO4JRHwzo8PcEdqoy2TWlpjpseOrwYeIlJplDPhJCVjMA_ia9Rg1a60CUy39RSaqynr8OuupCwuIhWOYgFfAuQIxMi4uGHk9QmGuLMhTmGdUMs0DLNtWREYP1XpLVWI8QpxsONx-WZvwnH5izPAmEoMj6AKwfYT4xRsFs07kG5t3Fm_xb5oTIrwhIWqQtJCdYIl2FYSleAgoS0PMDkKQVZ5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=IbjEG-lHZ_K19t0NzU3mIbKGda7LoZDxXz5nzY7Pe2BNWh0HGwSB4ylDW_aL8ldMUXT5XxP277JYFHC_GszD6Q0B0KjB1SeCaMkssV3lzhUHIZbEpbi5hLEuPF7Xr8UO4JRHwzo8PcEdqoy2TWlpjpseOrwYeIlJplDPhJCVjMA_ia9Rg1a60CUy39RSaqynr8OuupCwuIhWOYgFfAuQIxMi4uGHk9QmGuLMhTmGdUMs0DLNtWREYP1XpLVWI8QpxsONx-WZvwnH5izPAmEoMj6AKwfYT4xRsFs07kG5t3Fm_xb5oTIrwhIWqQtJCdYIl2FYSleAgoS0PMDkKQVZ5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24405" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUhS1uiNfqUzW5QiYvZMpAOx_8ZQEVBNrF2ZTU-3jW-1wph4DAkeeLmJrpO95ArZodSVTRmuhHvh3FYDMYdSooecR0u-7PNv7Z4muatlTkkPmmng8s1zFEs_tF9jECEUudSYMmJ0FV9qneXzoqKo5PK2FkWXC5kB7QhPESPO3xeT-yx3bhITrbgp058vGtCPfq4n6yfe8DZ4lskSiwlgLIvPEiTwKuhIa-qEnmNn9uEvVKMyXhkzTsG2yTBW_EGWYdOJ8x0LSBwIYQXT0Th-Ne55MV5XdcviL75kJ9Lh2ch4-yaQmtA5oKlGxU_51giQK1PeHiLkyqp2bLI9yWmLlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل اول چادرملو به پرسپولیس توسط سیروس صادقیان در دقیقه 57؛ بازی حالا یک بر یک شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24404" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=hapZ6bzzmb-EH6SlShrPt3R00MrElc_6HOfs-bNVPp4-JJhnvkQOHEqQ66kDQbY0nSgutwIaWpnu7N-S0wwFcERP1WD8FwziCfDW4jvGbFCDHiu7IB7bh7ZmUAWcftAldFSxEQjY4kOJ7y7N_B4xSGOnf-LLSItFdI4SfAG21E1hRvfnCfy4kpyBd9yIjUiSiKLwnRwnuSDpoFWdt1lOSdjIa43WXb5y5vq3Tv4JPDPDvN1Op_O2dPP51JPSttxvnpmtqkdVNRQceWO_yFoLrT8xitRuLM5p-nZ0t5munBDp6KbIowwmsgLUEFF8jTE3ERRPuvRVJ3TjjZMa-3UcZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=hapZ6bzzmb-EH6SlShrPt3R00MrElc_6HOfs-bNVPp4-JJhnvkQOHEqQ66kDQbY0nSgutwIaWpnu7N-S0wwFcERP1WD8FwziCfDW4jvGbFCDHiu7IB7bh7ZmUAWcftAldFSxEQjY4kOJ7y7N_B4xSGOnf-LLSItFdI4SfAG21E1hRvfnCfy4kpyBd9yIjUiSiKLwnRwnuSDpoFWdt1lOSdjIa43WXb5y5vq3Tv4JPDPDvN1Op_O2dPP51JPSttxvnpmtqkdVNRQceWO_yFoLrT8xitRuLM5p-nZ0t5munBDp6KbIowwmsgLUEFF8jTE3ERRPuvRVJ3TjjZMa-3UcZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌جهانی ۲۰۲۶ رسماًبه‌پُر‌تماشاگرترین‌دوره تاریخ جام جهانی تبدیل‌شد. مجموع‌تماشاگران بازی‌های جام جهانی‌فقط در ۱۵ روز از ۳.۶ میلیون نفر عبور کرد. این عدد رکورد قبلی مربوط به جام جهانی ۱۹۹۴ آمریکا حدود ۳.۵ میلیون نفر رو شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24403" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=blXg5vFqqZTX9vOeFhjqS1xW0bS3uV9HMVvRWBNHh7-HltDguWg-z6er5-h-ePOyuuE8SV_ZEtazuAeNPu4cyRb881gUXtqrLJkYvFQQvpb8TARzshPLugF0u-ULSijzqbe32Y3gUeR3-ziEw27rayMOVH8_-pvx441ucoB_2KnyRTIAIqptKga__I_SBv5QfIJphcW7eRR2CtRKj-rzauihvnrfh_YvggQDD3uIY0bLcVqjim6YrFv_cekHLbgyTE8rAptcGj5GaD_jIW2DDUsCEPAsfeY9jgT3VrPQVRX0Yq3FDV6DdXoEAcyLrpHl9IhOFA58PvxwQbo0CTzW5T1oy2_i0-JaEFj20x_NMljRLaDlk4Uu2rGRfvuXT1IY3PdJWa6V5gVjVq5UK8CNxS8-jB1DHKi-XM8j61AzEDaD9pFkTJDXxRSuleLBn05JVGAHgyOjBc9BEVai6mUxYETj_6bwnYPbwGLJh4IxpcKHNX_vpRJX62gZSrzpr_oWifAdxENDFC58SoPmiMSTRB0ySV4q9gM0aO-ATka1o5KhYs5jX4KRxH9Uzydd0ot3Eek_r9PMeXox3FQavxPfcdXMZ231DYggUaYgx4p13pfy05Rp8A3QaeDYM1eGLVDEIC6hgsK4MJIg1ZpOHRaZZjzXswjUfmP43RghRix1vDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=blXg5vFqqZTX9vOeFhjqS1xW0bS3uV9HMVvRWBNHh7-HltDguWg-z6er5-h-ePOyuuE8SV_ZEtazuAeNPu4cyRb881gUXtqrLJkYvFQQvpb8TARzshPLugF0u-ULSijzqbe32Y3gUeR3-ziEw27rayMOVH8_-pvx441ucoB_2KnyRTIAIqptKga__I_SBv5QfIJphcW7eRR2CtRKj-rzauihvnrfh_YvggQDD3uIY0bLcVqjim6YrFv_cekHLbgyTE8rAptcGj5GaD_jIW2DDUsCEPAsfeY9jgT3VrPQVRX0Yq3FDV6DdXoEAcyLrpHl9IhOFA58PvxwQbo0CTzW5T1oy2_i0-JaEFj20x_NMljRLaDlk4Uu2rGRfvuXT1IY3PdJWa6V5gVjVq5UK8CNxS8-jB1DHKi-XM8j61AzEDaD9pFkTJDXxRSuleLBn05JVGAHgyOjBc9BEVai6mUxYETj_6bwnYPbwGLJh4IxpcKHNX_vpRJX62gZSrzpr_oWifAdxENDFC58SoPmiMSTRB0ySV4q9gM0aO-ATka1o5KhYs5jX4KRxH9Uzydd0ot3Eek_r9PMeXox3FQavxPfcdXMZ231DYggUaYgx4p13pfy05Rp8A3QaeDYM1eGLVDEIC6hgsK4MJIg1ZpOHRaZZjzXswjUfmP43RghRix1vDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
#نقل‌وانتقالات|رسانه‌‌های عربستانی: عبدالرزاق حمدالله مهاجم کهنه‌کار مراکشی قصد داره در ژانویه قراردادش رو باالشباب‌فسخ‌کنه و از این تیم جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24402" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=IN96IahReHze1qHEOSEeNMAXZjRsv4ooISoyeE9SBj8satJKSQ4w0CtDE-GsGYapL7Hjmlot3f8nSgvbXwzb7tp4T8VT-UZAtUE2_fWFUUiWHFQaDL2M3hZGI5Zf0dcwvXamT4p-LhN80io2DfEN0lu-P5LYOEM0-VXRyE9y7bAfIVbXwQcDCbkjwjsKPDLm5RWoJOKnmdYu4PljN9rv5knDzRU6jBNpgFMAYwJuZagG9ccZ2W8q0svmKNAqO-bW4UQHGDSzCsrJTS_SE3X5BbC2Ud7HxzaLecY8UfyytUTfWNKWWG5yKQdE8zl_965eV8_TwXrsgAddX0KA0-k1tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=IN96IahReHze1qHEOSEeNMAXZjRsv4ooISoyeE9SBj8satJKSQ4w0CtDE-GsGYapL7Hjmlot3f8nSgvbXwzb7tp4T8VT-UZAtUE2_fWFUUiWHFQaDL2M3hZGI5Zf0dcwvXamT4p-LhN80io2DfEN0lu-P5LYOEM0-VXRyE9y7bAfIVbXwQcDCbkjwjsKPDLm5RWoJOKnmdYu4PljN9rv5knDzRU6jBNpgFMAYwJuZagG9ccZ2W8q0svmKNAqO-bW4UQHGDSzCsrJTS_SE3X5BbC2Ud7HxzaLecY8UfyytUTfWNKWWG5yKQdE8zl_965eV8_TwXrsgAddX0KA0-k1tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24399" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3569629639.mp4?token=gmKn3uu3-C8mn9j_0PS-yrXntfSWV4TWlMeDbEJN2t0V_fz4kNN_lxmwslwia1Mn2dZqRWZ1Cv6BQ6Zdh_m7Ke7ix66uN4d6gORhNRnALLcWe99ZcGad4rroVlKP9NULkFb6QJo_957PvbBdRjpJwXSM1zaz7gpjftyngEqzHvlbhkANVnBgNTYZsDmut-wqfgGTqwPFgSSsAeoI7YNLGyARNhRBuaNl2Oou1kqMvliHlauspDTPdS_2g9KYO2rMlKWJWJalOpbYfnz-N0cvzgTby2610Vnd8RoFepkJn0oDgNZYS7AKOjWGvZNBqOVJjJ_WexyeZfk2Rx5-Zkus3kYk_AlUIICdgCALZsUpIyOu7NDthSxaGYJzsxLkCdjbqo6A8lEXp0kY3O8UqpMUxr9H_AbGaIkXLB4N3OXcBKEhY2xnj_iGISQObzZ14c1Mbx6--ZcsiBzL0ouu3ZEnhDLO_2b7pJ5LK3UF3xZ7SEtdcgymAWh64sZp1OoxKl2djuTtfq71hZafMghgyrFSk84zvss6wCpjYhaGYFmzC1TosymfVeIddiOdqN_W__6by_N1p3ao9kYai6-aRsx1dYomieIi9KxgGRsvADZBXzWA4jO--Y_Fg2LO-4wrLiAcNaCYAEzjkkNGh6lc4Sa6oRrFCBSHodJxj6o0FNgXzlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3569629639.mp4?token=gmKn3uu3-C8mn9j_0PS-yrXntfSWV4TWlMeDbEJN2t0V_fz4kNN_lxmwslwia1Mn2dZqRWZ1Cv6BQ6Zdh_m7Ke7ix66uN4d6gORhNRnALLcWe99ZcGad4rroVlKP9NULkFb6QJo_957PvbBdRjpJwXSM1zaz7gpjftyngEqzHvlbhkANVnBgNTYZsDmut-wqfgGTqwPFgSSsAeoI7YNLGyARNhRBuaNl2Oou1kqMvliHlauspDTPdS_2g9KYO2rMlKWJWJalOpbYfnz-N0cvzgTby2610Vnd8RoFepkJn0oDgNZYS7AKOjWGvZNBqOVJjJ_WexyeZfk2Rx5-Zkus3kYk_AlUIICdgCALZsUpIyOu7NDthSxaGYJzsxLkCdjbqo6A8lEXp0kY3O8UqpMUxr9H_AbGaIkXLB4N3OXcBKEhY2xnj_iGISQObzZ14c1Mbx6--ZcsiBzL0ouu3ZEnhDLO_2b7pJ5LK3UF3xZ7SEtdcgymAWh64sZp1OoxKl2djuTtfq71hZafMghgyrFSk84zvss6wCpjYhaGYFmzC1TosymfVeIddiOdqN_W__6by_N1p3ao9kYai6-aRsx1dYomieIi9KxgGRsvADZBXzWA4jO--Y_Fg2LO-4wrLiAcNaCYAEzjkkNGh6lc4Sa6oRrFCBSHodJxj6o0FNgXzlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24398" target="_blank">📅 21:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGiLeKPwkzWQ9uUOPlEg5MKUzlxGR5N7QI2jsUvsp4bvdAT6SB3Ryw0sSJ9AR3yvOiYl9wDXyM8Wsqs9KxLgDg3yyB1YEpNYdHJsFjWTQYinVeWMxn--tYW7rU8Z1tiFKsOsJic44pc67gUPYKiu4M_bX771IymwtisuYgYK8g07KAZfcl8W5dyCCM299cRSd9I-9UYJhZPyif12j5tVeZ9LvgwUwTomefpq8avVKZTlGJW9TGoUQCgRie2c5RMRmd3g5_reprLNqinSFWUgxxwaD6Lmj7MjzyPdcZHCuFGirTd4n75PVPR8vjvBHuMfX3bErJUWnKLNH5OSMlrfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24397" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=WOWPbRYypYMThxrr4UYT7lzLb1Bqr82VgvASXXVC_yExpfT4VtXnci9TF304w_nK2F1tx7KZiXHmDGn4wgYbRJ4X7C109-jRYCd6DZ80qYubHkhChRbR5Pl8lbF7LyRVdlacax8-ZiiKP9oXzKOC28Xj5svJ1J88R9sbY6Z3BLyvoED0SHBGdmx0LqLpKzchUZc3gaqBCR4d1naw5Yfr3RaZWbIkUyGcSZxVoOv3cponPz3Jp3g5xW9PosxhrsMJ5gTAYnInFn_rvm0o5OwaSidSlJsybzLpup3GAB2RluH5udlfBPagmOOMmS07fYrhs4y9M3F5yh1g9d3tbYmP1yCx7MNSrrj8kCPzd___IjgQ52IQheDIsVBmDGbRww-ofk2yo-U5Y9yBRt1XwF3B-keaekeiMmqiNmVoGjCCY27Q4iZMILNvlAyN782NwtZ87MXpcBxT9d2gbXJkOsEeiEGv-vI5favMfKgdkWMouCwvDFvAkapQV5NESjk03fvDZA1mUhCUSzUyX3X1OpAeNw7uI9kPE1BLOeooUuTixKmhchkihrfAAw8R7AJcdxX9kZBd3wJrthhQzm2KqXyZrTWbS2xqywX2bhotiyefBe2bFvL_jR_Ps253MmAPzfTY63TZkMV4xW4SYI34SB594vMy8GyXZ1BLWSQYTZ68hY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=WOWPbRYypYMThxrr4UYT7lzLb1Bqr82VgvASXXVC_yExpfT4VtXnci9TF304w_nK2F1tx7KZiXHmDGn4wgYbRJ4X7C109-jRYCd6DZ80qYubHkhChRbR5Pl8lbF7LyRVdlacax8-ZiiKP9oXzKOC28Xj5svJ1J88R9sbY6Z3BLyvoED0SHBGdmx0LqLpKzchUZc3gaqBCR4d1naw5Yfr3RaZWbIkUyGcSZxVoOv3cponPz3Jp3g5xW9PosxhrsMJ5gTAYnInFn_rvm0o5OwaSidSlJsybzLpup3GAB2RluH5udlfBPagmOOMmS07fYrhs4y9M3F5yh1g9d3tbYmP1yCx7MNSrrj8kCPzd___IjgQ52IQheDIsVBmDGbRww-ofk2yo-U5Y9yBRt1XwF3B-keaekeiMmqiNmVoGjCCY27Q4iZMILNvlAyN782NwtZ87MXpcBxT9d2gbXJkOsEeiEGv-vI5favMfKgdkWMouCwvDFvAkapQV5NESjk03fvDZA1mUhCUSzUyX3X1OpAeNw7uI9kPE1BLOeooUuTixKmhchkihrfAAw8R7AJcdxX9kZBd3wJrthhQzm2KqXyZrTWbS2xqywX2bhotiyefBe2bFvL_jR_Ps253MmAPzfTY63TZkMV4xW4SYI34SB594vMy8GyXZ1BLWSQYTZ68hY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به چادرملو توسط کاظمیان در دقیقه 28 در تورنمنت سه جانیه سطح دو آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24396" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uan5GjPljwxSWYxX0BY2zGElv1zsf5YEhCN5SGwSlNcwAOj8AQHCkv8wz20Gx5NiQsVsshdj48HQfpeSaiN1UuOfNZsUALo5QRNPAVAl_rNcao5vF5yekR0wS98PRtlsfOTH_dEi__4kKbemB3xomjLVH-e8z3Na8kWHgy_EFJBVzp0EBeVCS-iUOFsVRtV6liRgYG5oCKb0xHx6jmJy2nfMzrIQNyXolS_qlpkCJdIkIPbjylYYVAJVEN84iutWBVOHkh9_aXJ2wwit6SF40VVxTMs18FHkgguJYG5Gf3y6xvXGmlKIFRBQBafe5jTu0XIlzWmQbD2gTNRpbNvVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات
|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24395" target="_blank">📅 20:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24394">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-RUDcoXnH8pzKil41zqn3N5qvdUdrK2TMZTc0RRlPe37bK_lvSoD8J9_AYj1aBvuR7Wrw6vI6vjcQO6kR2CirdrzaUh1O94xr6hFsDjc__KmmRv9riHWX6YB1uzBpAKg6k8P99Xy_VPuXJqdBH26JKhNq-QbRs5nWqewsv_BzFjZShaD9g6b0G5EPoS4q03jVmYaJiu31UjgyL_jl1yJxbCpUf5eiMQdKDUP4VSl3cBpAtLcY4gAAWynYX7Bre2lWH5hh1X__ZvizAhZZKEbHniFSbm2hllrNQu9857LkD4h9294gA-V5jBd0lWhP5TOWSrbF3EZp4jkXWZOtYfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24394" target="_blank">📅 20:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOdKetYj2uDmGoh9sdtsRHIH9vupsCyipiLmmmpzKv1qESVUdnwnv5WLK-ji248mtb3WZoiHUI5rUNP3cnC8hVpIo8OJhRxa0gJneq7gBUlogRnPzoC2ypXKDiGGkcBmSqyPdwHYU0T4cHVodRocA2-cqI1q_Y2OadlC6Zy2nj5GyWd3Pv2odN3rA-NdRu7NDTWfnzNJJX_KuDzzNor7OWYCK615-8SJWPt7sARXCEEYy4TUaQ5mN6vGwiGiDXCcG3_KIdfeyp2tI1sKO6BWgecQmUEDj1svQ_FwFG0A1UgXYxtlTJGkCNiQdKtcaUwN5GAzpR9d1MEVWDGgJmFVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2wV3ULVbhYfJ0bBYM-jK_DoxO5dc-NwBnEEky_YNzNacZMjGQkODF8I5ubkIp1wUd4g407I5ouZcYazemhXe9dqfQ9trwRulZzCBj4ePUWh-Q3IjAUBYXQf-bgYlFBD5fd4SslOTBrvHcbaVGo3Vsrqw4hdzZXJLoW3fFTnIwOOo5oXi2STAV4XoDUjqQLR5nV-pWJ8d6erFvyNkeg0fia2MNJPINl-J9mTnoRcmuKN9L2l6Ux8nsYwCe6QnYgD0EpYS5_v8oLYniAmByCQDiYdGCVw5hL8Caky9IsqhF-97XPzXDG0iu_KV3htRI1uCITbR3v09F6-m061zkPEnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ناتالیا شادل مدل استرالیایی دوس‌دختر کنان ییلدیز بازیکن یوونتوس. این دو حدود سال ۲۰۲۵ با هم آشنا شدن و رابطه‌شون رو خیلی خصوصی و دور از رسانه نگه داشتند. ناتالیا مدل قدبلند با حدود ۱۸۲ سانتی‌متر هستش و قبلاً شایعه‌هایی درباره رابطه‌هاش با زنان وجود داشته‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24392" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co2FPdErwdQZ7v8eF7v13oyjGrxq_JWINsII2X3YoRMIucQOsiAlIm5VsnRQ-cL5kZqVFLXQb-5jKNCRbmpvM0uEGf0lZdsM-AFtL__XEeGj3MgH4-GesS65ubKGFzsOX0F9yojXohXYTYEP4U7uigRTBY8S5f0vaXZvnWJz3XIY8_qpflJAwOdlPuGWACwBYBOgOz7JaBvee0M9L_lEiMEbYdpihghm_wjIPj5x1nfh14RcmmSC71E9wkiDBeO2VZXJzfMv-0mE3Ol7t61edzbXvcDZbt0PIVmcdOTIG5-exNc0dsEQwGgay2iF1v161zDvnZXL7NPE4QidK-IWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24391" target="_blank">📅 19:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI57yRFHscgzso6SFLAZRfPWox73FwUaETer9I3Zgco9XIBgpJgQMddy-ionHP90p5j6Cg3v-gHrUOUKKobLyDaCOUCml-9L0U_hoQb9NX63HpxoLHZel7_3L1DU0LGkxfN4ym07iqc8Rugb729KspgcubPxAUxfgSjzCGjucBFb_AfM8lJXjcZ8uKfjzGWYu6jkAgi485u4yb6FL9uure7Z5wF9GhjP73VnSBbF05ND7M_6d5UZ9fioq0gRfYe2u-VuafNIqQQtoiV-yrFUC5oePMHGfqJIDdpgMhzV-7eoCsjFLDehpIkAUOzGY32LeazilsPCHw47_ONDE11juQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24390" target="_blank">📅 19:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBsxD5Zz9oGlQISOztox5woh2J2dD9xzUF5wQIaTVUXsI2FCaXApDqZbCNf5NcddPm8L-5cLUOj81Kovy21VbIW6uXbbivTK5eDOByphAiMUl5QjbmYaOV0J_0vR9I-NZmcqrIw-pSGYpwtA9OKs1vmrlAtdc1wnagpQqPiwWk9D1RXDRsoJ0MzkxzUlHcqFmtcRx5FfcNvAcJmHG51Z3ha2WPVHuI_Rdxayle8b6p78j00pPB5YyUifVTEMbgq3blkHwo0Z3W9IJ03GpxCVGH59R1-GByMRoqjvgBXgscnyP1-OW8cZjJ6Dy0HkKaGDChvvRa4_5rucul55pZb5qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24389" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozmlir2C_oivWllC8C3_DpdC9ybi91MqhiiXp1pHPz6IZd2e0g5jdzFakQRIY1LUNWeuNEI84o95VHWQfinEivhD_u-FG-rlOH4Q-UD4sujPkfYFp7kt5-o5N-5RYSBAUBmFSgay1v2y6bB4i9ootfqz3NAsKiMVvP2TFVzqQD2cqZS1pcfILBYrvGq1JcSgyJR9fWX2RAkQR49Xi8Lj0G4SlOPb_Iz4D9bzo2PT37edkh4nFnoMIOZuyq5nOw1DVAuwugoQwPUYMdyn8RL4I6Hj9hjkmnt1ZYkgCCep6_LFh6XNEJjINNGswiJaO33gfDTyazkfeMop5ComI8i2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24388" target="_blank">📅 19:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXKjyizHn8tCVLAkA2ka9VqcvbyLEWP846EMDnz1yLsWzjU0icziHIFfT2D0AHcxTWy4ZbBjb9JzOEA1hW32EascSNi7oRrRiMAp0PEi1hKDQZg1ql1UJ_vT6z6AViIHqBGleOmB_QOIlYKN1phAuoMC16UQOfYedO3sjuJc7YIv3Ihmt68QDQ6s57-RyjjcCiJkt-6eFiKPSUG8B2LBYIX11sw7zjLcipJuLuXiHngASoBaznGcN1e3_VRKHGDc5-4HBdSyJCkKlE-iSuCb_T8sOXhuTyGvp2LVYQXYqTl-qhbBvqM93Ogj1TAJ5nz3ejp-LI83zX1N0Mqi-dowmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24387" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohIyVwV1s2ScsdzGQ9B5tpG4V-itc3qpu88rgaz30qfWMX9phesYX-yqsOydYVMrY6ikmyoqX2eiY6pnnz65h30ZGe_qgQrAC_0q_FFJ31fo9jy1-IVmuGtfD2aMFcxTlzaVb9V9ZZOkzmJAEz2wx1g34qQbXy_EBH4pxLMSEC459E0ifU658EjMub9NC-HCMuoOGt9l1zoUUQ08emXtIa4joOtSU7CPLkJNUq50Kuz-nUKSb3UUIUGSeplzBDzdSBUCk5EzePMzP7uwkFg8rO3h4rybvZePzU-D_7b-y9oUUdqxUUSv9bDcLATfGL8iNqPepDxj-0aXBjEW0_xN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24386" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24385">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Iia6EI6fZV6cmQ2ptU1Wx3lfPYZaYOT3ZopJ-9AAF2IKVe4RPluS0OWcuQxhyZvX7rfILl5x1ISeSk-lebO8yO6iQZIKr3XEMlNagdR8jW74IKChOxY9VA9ypGpt2fpkX5qskIb9F0MWUCrD1EhCgT1xP7ml9ACX5KafBpoCulhyAYtjWYpu4GhlZzrCd0xvj4yxj-6mtHAPk23Eei-pWOK4yNF3UL1IBTweX2zAb0ugRGT_5pIlPI4XUiNZOR-qH8f-GicHjqmsn7xhoS0uj3EK7UF4WPFwEKK6jejAo4tb0PfDN1iKzROaubjjSNq7ZUqKopLS7eBQH_tigWFXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
جذابیت‌پیشبینی‌مسابقات‌جام‌جهانی را با بونوس های لنز بت تجربه کن
🔄
☄️
بونوس خوش آمدگویی
🔤
0️⃣
0️⃣
2️⃣
💯
بونوس روزانه ورزشی
🔣
0️⃣
0️⃣
1️⃣
💯
بونوس کازینو
🔤
0️⃣
0️⃣
1️⃣
🔒
کد هدیه چرخش رایگان بعد از اولین واریز
📣
بونوسهای‌باورنکردنی‌لویالتی‌امتیاز وفاداری برای کاربران فعال سایت
💱
کش بک هفتگی
🔤
0️⃣
3️⃣
💳
کارت به کارت آنلاین و تمامی ارزهای دیجیتال
💬
🪙
واریز و برداشت آنی جوایز  5
👛
📱
@
lenzbet_official
🌐
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24385" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stxqfAWEuU4eao3usK4uLriyDfvGdeNzeggeD-NqPb6CIM07uzJEHE0MgF-sFOPqCDG92mVPf9a9MY9pVABXZPjfILcwkMwY6I4rF2jCbN93ES1UxFUIcC3DalpYW2IpwPwbMipNKcyU2LEnKxzaQY5e4KZUVe_0rxIUYi0ig_8HA4ciK0MRwCpfrDBd_LyhDmjuJheBcTiqEBLUH9aKxj6A_WniYsC6_ngzrgbydG1l3bvHiiV4DIFL347tpptr66cqc62EZxbDxSC-rl5rPNcyXBU5ZyuZkhVdHrzo53wQAy4QOlXV1wAdQEPOlPy4zByUy9uP2_TdCi3_heKvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_nk4IVaMnbW6EtV3BI4LCmEzjoYUrqAfnj5ueXZPXRdHl7SEaQhtmHuZSmXLpMKcoNdFroViZ8W3OItKozRADsijT3rvFhWwwqeRVIAoVq5C7lWZrGVerL2bY5ZmcACnY3k4pfcZoFUtab6_YdCq9xs2hMP6Vj175BBB7XzRI3qmYnUP1tzK8afuRt6JwGHlc4tmSuCVSBl_vOveJEb1VyTt9xrbDHUhP7vSJ8K8tqjR9G2NMD2jRvPuqCUgBFpoQPSIwbrHZ-GK-I52rRp5473tVo5ekGrhLgozZu6iDbaLRmU1G7fkVsJ_UXccgbVd3UOFBIyonwkGRhe6BDOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO-2-SV4F7oaNnDtKaaAfHRO3pwdlh_Pa_gKcHgNEv6K3wnkWMH4KweNzU-nuCCvCohhaLtlwPQF5S6sn0yDLmSm73jS-Wnk3k0KX-BpPFfJjqhEM81DIBM5YKwTVAyl-MkjjNLO6gVg35TM4hVSB5OR0Bx8iavr75UkjpDOPtROOZSimxvGFcJmkgBEJc43BiK8U3MVJQkKCuRlK7czdgZAquL0zlO1bwr0YJ8UoqYFSeJBlXz50Cwn5OzyzK2buldrYJNyRUh-GuP3URofWkgMHFhXHm6dXRGjRcvtEm1S3tsYk4yT6vfwOrt4I46YSVyooV0WW8gGdim6q5HFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24382" target="_blank">📅 17:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5c2TC56R9nHRzkvwjJCL6I84MZWWXQqNM4T732JkDj-8UCOK9g9k5SuakxHwCrEyDnJfpvurF-SaMm6k5fDFpQ9O1Y2RLRj_2dXyTTB7a2gWoSKKFNpeehHaxbIc37cOzx4ZS0IJHL4S4SZCIO33eZ5wZzVecq4dh7p8LMNtpzQtEmrb0aXGc57F4-bhL2EMM38fCOVFbDHNDXvLM7SPs4Qh78AmsTCnyFB0nAQP96HNnNXx8miQx6j_4tt2z4aUlcNK1nLlJlpRyJWtMhBB2pevRcF9BvxB3Vd77yIhkm8WWLiuMBznhbFEQMV_HAbXXioHGc8loz3Fqep_eQ5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرچم‌حمایت‌ازهمجنسگراهابین‌پرچم‌ایران و مصر قرارگرفت؛ فرداصب قراره ورزشگاه رو از پر از پرچم های رنگین‌کمانی ببینیم. فیفا گفته هرکی از قوانین ما پیروی نکنه بین 250 تا یک میلیون دلار جریمه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24381" target="_blank">📅 17:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xqn1oxOsjgIxCGwxZYv8wQypbE_Y2G7I4xnRC0GTY26yxkfIWEEyDhBFxnjH7-crRoxjRewXVbTa85F1D2zzdUsza7j11bQzHuIwa-yHv-TZmlN08dyNWD8n_7MpqDe89Icfgk6WhcM8oLQFYT886V4ody0a2rCujn_qFpy3xHPEvrIf1itAWT0IAbZ2Vfu38ivPz27JEbmEI2huVDMmxweOt3h92LG0glY6re7f1Sqet4lUxb4UDzVLVFKvM_GHW150qpjEUrBslho4T7bYPe-XgkZZU0zGUnGSsYNn-nXHH433OGGg35rBTE-gUhRTK7LoGjzXSD7jWa-WJ0Ok1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24380" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tiw4opFzpfKXu4cy9d6v3CISmcVGjx_yZaOpuRT-tWbnfl2OlEKv4vgF0Y4rAGV8A9zMz2krg8Mewo5getZ21ThqGHRIoNMS9MUNFV81uws6SaSp2yDpePMVJSPPQ407kChSfMbRoDA01hoVcd1GRj4q6GL-KTdXI3n_F10-VhPq5upuxHi2IzEre0Z3MXG2z9CSl7jeDZ3s6XjIlHT553LIglCeZTSakgutQQVvOIqp7UWbfXAihwcLXDE_qpZVh0RdBetnZgn02FIPzJdB3dF6Men4OdfuT2BEqgRw3v2K3323KtUW-FhiT4oXGiiURgSS9aerqqGCPB4yBX8XdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ داکنز نازون مهاجم 31 ساله تیم استقلال دربازی بامداد امروز مقابل تیم ملی مراکش این‌شلیک وحشتناک‌رو روانه دروازه مراکشی ها کرد که‌با سوپر واکنش استثنایی یاسین بونو مواجه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24379" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=WJiTXjaCSjDdSBmbwQ1d5m6NxuE0ohfwnv0tTDzIl-NT_o5aes-T7ERaahyj_-Zcqt37_qFp14VkdHOHvsqvdLDt8CqDOw4v8dCR9WE2y6qMuhklsroa6chpiYnHEqmyhTNEbJ9DA-0UK2lICWrMQgnCR3e_mOsCx_mfWRsANMpoxx2Ab1qqMTvhfDnLlZMG2aGxHvKvnbPdpmDxT2BoZENrASoZnJLJmJ4yX7PdSc0ZDgn7hwMgazj4EMRFVib9ch-OW69DG5FNQ-yiUtSXUCW8uGM1n_XS-U_SwBPKwxK93DQb26qhcJaIpmEm2wmQCbUIknVKQACtzZoPfz0QzzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=WJiTXjaCSjDdSBmbwQ1d5m6NxuE0ohfwnv0tTDzIl-NT_o5aes-T7ERaahyj_-Zcqt37_qFp14VkdHOHvsqvdLDt8CqDOw4v8dCR9WE2y6qMuhklsroa6chpiYnHEqmyhTNEbJ9DA-0UK2lICWrMQgnCR3e_mOsCx_mfWRsANMpoxx2Ab1qqMTvhfDnLlZMG2aGxHvKvnbPdpmDxT2BoZENrASoZnJLJmJ4yX7PdSc0ZDgn7hwMgazj4EMRFVib9ch-OW69DG5FNQ-yiUtSXUCW8uGM1n_XS-U_SwBPKwxK93DQb26qhcJaIpmEm2wmQCbUIknVKQACtzZoPfz0QzzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
توصیه جالب جواد خیابانی به محمد جواد حسین نژاد ستاره باشگاه‌ماخاچ‌قلعه: هیجوقت تنها نمون. همیشه مادرت رو همراه خودت داشته باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24378" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSHhHlM2abe_SlPgVy6aCyX2kxtEd269nm4OcEgMfaV4nWqJmNPnA552NqQzYmB5kTyq6SJsW65Nd_BWZ1TSrJ4Tkn_-jl5BgQGInihJ7NycSFKRWqYPmVPw-ugu7NBTZxswqPfKnE_MRgrDyBQAs5DqYsqzenju_tL8ZAPkmd0DUWHoNVQJKhqo_rWkvY3RPClr1DVGEKWUEdIsLt11_XcsLhlKXyVZZsWcOLDoa0ODox0dg4LQUT1V2czSyZhPXlRxKR4itWCR8YLhsSS8bgTqLfkpOCSiR8jMbKAhVcang_t0323SeCAnrpY6SZErb4DqKpt0ACgAa2BjeNjCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
🔥
باجمع‌کردن‌امتیازاین بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
فرصت‌رو از دست‌نده‌والان‌پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24377" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj8Alekt2KKP8KWCtoz_3pWcTVJKxWQb_jwy2A2EFMdL05lQTsuPOOhLJ84ciUtwmwopmhGNJRRQuwOcyHKAVpjj5knJkXTji0h13NbKZyiBYV86koAKatBhPQxpkembhRyQESNkMp-NdeHoNN54VwY9vTHrEZEQUsk7HcbaEjD_soTriZbyWoti5PU7U0xPNaP8OnIDE6DxnXfY3K4-JYbM-oB0K28T3et3kgcDOijs-tsFhnshrs3wRRre_4IFcABWdTUw9aAfrjyBI6p4ObLbDW3LzasfR2MAiS6bYFAV3eTfQvG6W3EH1frw19szKtMpmJOB3TOel9UsheEF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی
؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛
باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24376" target="_blank">📅 15:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnQM-4qxifVSKuh7gO__yG2Q5qsiJgYN7jYmYKRAXtjFGMTEhgRV7B4GEN1zoa--ULowQo3wTGM4VTrau-i0ARf4qUT3OmaSvv28pJ8yI7gY3Ax3fhkj12pk6-9wABz2TfhDgKKyyU3uDRdyvHF_K3x27ugVRpTWQBvLy7cw-fYCeRWPJ7AfBbD4hAk0e7d76FohVrkEKn0_RkTia3EE8zx9zdIPX4LcxLWEY_snq2EhlYhHdi0WcrQOKPauoCsPIRqxd9bNSjWYw5eh82OnjiXHn4L7_8OOCFTpsI9fzQrgpnY33g9qZUKnFRWYsRm4cRwmZJ8U4aEnczAL6yPeww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk09l7zOtu0gkcW_bGuDeCJ1sevU9VaPjzINmElAQQgF-3B_Nr7B8j2VLgibc6WrlDV_x5vnWJYl-CooqYIuUAaM47e2FA7_eK5OHG043oCP-OzHtTRXhJ1sg_A4mjhpbhrqDTxhD0z3AQ5IFl75Lf8pO_uPPcHVTPoJW_quDBWQwVZJacz0Lg3DINlsKlcj4JUOZCEjh_VT1T9lNqp9LR_GCldhfer0OgKjxOK4EoKPZQlDKfFYu2dkPju7VtDPfT-Y3joK6ghF_Qu5dkuKkfJbx4L-_dWFPghnhopqgCeYfYEmaTI_8pyH3eQdkxYQJMBEoWilnFzITbNpME1M7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=VA1oJX5q_dsZaLm1vqAaPUa8MvF6NbjAPwiPJvKWJks4jOTdmoi5OirFhoqMjwXBFgFUGyMlg3Hiy3bWl32qJdpNS9sLgL0fqB_E7UNWISyM8wAeNnDdc3V_Yp_ShNGyTHI9R51jb0EufgXXAvbN3r8FDJT7mFDV1P7FytXkn2A6GWsySzYY2oYutRujbfONJiCJPaG8sq7LYW-lClMmcmYGmNSemgiu8N76XpakG-XRhIu_-1OLzbPsm2GL4S6uS51KwYaQ0DUR8qLk4GHM6aAbYaad7wCcpTNl70akyfNHv_aRL5rndZtfiYDKZCxszwRTVwyBwoKNbUQ_V_w2Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=VA1oJX5q_dsZaLm1vqAaPUa8MvF6NbjAPwiPJvKWJks4jOTdmoi5OirFhoqMjwXBFgFUGyMlg3Hiy3bWl32qJdpNS9sLgL0fqB_E7UNWISyM8wAeNnDdc3V_Yp_ShNGyTHI9R51jb0EufgXXAvbN3r8FDJT7mFDV1P7FytXkn2A6GWsySzYY2oYutRujbfONJiCJPaG8sq7LYW-lClMmcmYGmNSemgiu8N76XpakG-XRhIu_-1OLzbPsm2GL4S6uS51KwYaQ0DUR8qLk4GHM6aAbYaad7wCcpTNl70akyfNHv_aRL5rndZtfiYDKZCxszwRTVwyBwoKNbUQ_V_w2Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=jWxpnb24mBSy_wlIItMz0D3SYWbhgB_FAB9KrnDCAnmR52DzvLWCm5ycFnOpFAh_iAiPUVv_zQXpl-W4PdLhKoaZ_kPEOURiocLaFfXX9P7m9VcroUZLjGpY2ezfvsIqDYYfTJbQ54Hoa_KYLilrLTiQOm76K7elk9b4r78EcqlIPkhLAxh3YZhgS5sK-GaSvuM1dsNS_oibpOeweKa54Nr5HNV5Lo2SQqvMrCe0ZkIGQWSWsSyQzWWmHypIbPxbkvVmuy84dwTWgLqOVB--rPo9eHs-dXqAmbj7kA2dlWCWKug3DUKszhYQrNWf1063rgznIPHE2r1sucLQDIRpaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=jWxpnb24mBSy_wlIItMz0D3SYWbhgB_FAB9KrnDCAnmR52DzvLWCm5ycFnOpFAh_iAiPUVv_zQXpl-W4PdLhKoaZ_kPEOURiocLaFfXX9P7m9VcroUZLjGpY2ezfvsIqDYYfTJbQ54Hoa_KYLilrLTiQOm76K7elk9b4r78EcqlIPkhLAxh3YZhgS5sK-GaSvuM1dsNS_oibpOeweKa54Nr5HNV5Lo2SQqvMrCe0ZkIGQWSWsSyQzWWmHypIbPxbkvVmuy84dwTWgLqOVB--rPo9eHs-dXqAmbj7kA2dlWCWKug3DUKszhYQrNWf1063rgznIPHE2r1sucLQDIRpaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
بیدارموندن‌ساعت 3:30 صبح برای درس خوندن
🆚
بیدار موندن ساعت3:30برای بازیای جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24372" target="_blank">📅 15:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lh5r_HA_IQmuaKegxU7360wzb49dtYsfOnWxWQNN2LjbXCmpFfwUtutTxNIe0TtSXxyCM6mKc-NGhqe_VE7mJQZFdHtIjdP02IAsfNk1aHpBXXSFFUj14yiMmXuAfL2zWWmyeeEf9LVRtPbDtosT87KlELDwEB_Fjaik2wF0FfCkqvRs1hOtAdW9HCgJKtMMq_kTORpqONGLfGe3IVZc0gkEcLnsdAADLcfxZ9KIZcCqU824cKGiyFOUJZedJD5ckmFEL1xctQvLB-egqwxQKxA53PQ_9VoWQSIBbjk87J4b1I2seMfEam9T0P2XjH7TJQtZiXZZeCHfx26TokD8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwlTT5wr0D2Mu_FhVH7tQQ2NRztFwSt2a42Sso1bF0GxdgNA3AGb1xJyBYEF6gRkBFiZZLAIbNbF-Nuw9sqThOmdFzVEpOH4OxA9PPvVNqds-w4B0Y7ejZf9IOHR5538FY_CHx__pYPYTEjP1NHI3qh43nEm-AJEaf9B1D3MUT3H1HL4VTHf7AQOHDZY7FjdkZXGpXeg4gIhHDRNB8dNX1TB55eaISJXoVKFq5yBX2tUUpaYpl_qRXep4nP5jAA7lMJIS2Tu9sMr0eQ_Ve6HDSWs91Br27l_JRh33JWFyGWQi_43ArMhSC0i1RHUYC8jZ33eiD-GcwkO2KfGAA7Dhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24370" target="_blank">📅 15:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWIujCFNNI3qoCjo9nGWt8U1FQnRqCpXXzKGGx-ex9r2DOzg56uPQ-BW3h2ePD2dcz1oDSVvZlUrTqDuVH9bKxf2atmhw8cFqE45pinEjPB4fZzCTou_O4yb1vWWqY-ec-gDrs2wIMet_0vkuiWnfYJ1oyKw_S1A80WgBOcTbZhWR2OqzgpObnoM_e5lKqXs7t-mvDXe8B78yft3E2y9hMJkknsKFO_AFONNQ8P14JMtmeqAQEqwMS6jNlo9r6Nlka7ufJI5UDOLpJs42Ri0_3Bat-OcfUqtF7Wy4wJodu9o8arsP8Bv5pIGW_ctPaZ4_Cfw2n5I_Rq0Hw_yCs_faQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال ۲۰۱۶ سمیر نصری که‌بصورت‌قرضی‌تو سویا بازی می‌کرد، برای درمان‌سرماخوردگی به یه کلینیک تولس‌آنجلس رفت و بهش سرم ویتامین وصل کردن. بعد از اینکه کلینیک عکسش رو برای تبلیغات منتشر کرد از اکانت توییترنصری چند توییت عجیب منتشر شد که ادعا می‌کرد علاوه بر سرم، «خدمات جنسی» هم بهش ارائه شده! توییت‌ها خیلی زود پاک شدن و نصری گفت‌اکانتش‌هک‌شده.بعضیا هم حدس می‌زدن کار دوست‌دخترش بوده؛ نصری امروز 39 ساله شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24369" target="_blank">📅 14:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=gIp1bQOSpJ8XYTLT6R7ZOyeFHaU4qrwuNYXosRxCeCiSVuqIUo4NOimVYtknNb5Zwyv-5MbcBZ2-ezsPB6lP1lKqYXsxE9eMK8RH2w9nhXozkL1a33cYXqHNZAkdfpNI2RkQ9HoD8K0W3d6lRMix5202GtXt-2DACvk0iq_0oSlluQykKCe5d84xgBanhmvEVS57dWeTbVKGElj7GR5808RuTrNQix8V-izR2KAmdK2Ig7eHjpTA8vg4Tp2Ryo4Xd4LPnTN9Cy9_p486p40GGF17Z1XM_s8La3mzGUPRejNYBK1YDFPW5DW5vwIKskqqnCmQTzeCL_bqDcbvLaYhBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=gIp1bQOSpJ8XYTLT6R7ZOyeFHaU4qrwuNYXosRxCeCiSVuqIUo4NOimVYtknNb5Zwyv-5MbcBZ2-ezsPB6lP1lKqYXsxE9eMK8RH2w9nhXozkL1a33cYXqHNZAkdfpNI2RkQ9HoD8K0W3d6lRMix5202GtXt-2DACvk0iq_0oSlluQykKCe5d84xgBanhmvEVS57dWeTbVKGElj7GR5808RuTrNQix8V-izR2KAmdK2Ig7eHjpTA8vg4Tp2Ryo4Xd4LPnTN9Cy9_p486p40GGF17Z1XM_s8La3mzGUPRejNYBK1YDFPW5DW5vwIKskqqnCmQTzeCL_bqDcbvLaYhBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌های ملی ژاپن و برزیل بعد از اینکه از مرحله گروهی خود صعود کردن به همدیگه خوردند و این مصاف جذاب رو رقم بزنند مصافی که قبل ها در کارتون‌محبوب فوتبالیست‌ها پیش‌بینی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24368" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=bfSqf4f-M8d27b1FCWHh4qQadU4VJf5Lu79YiOwWTKRb_L-9uH9dHc_qQYqKKWtf831O0eKlNo895Gv7xMJKhDJKwXWRZb5dva2bH7b7F7MEK2ba5UuM5bderjYRuu5XcFKXsr7j7fEvr-RzaIcfOJM_5tPG6dTxEe84tkD5e_1UUi7lqieDsV6ddyDMWeCkQtBbwgwjW5sjyXXiKvZbeTdZ_ayIp4UOpgwzg5eDn49eooWBqQpja_vN9nNoL5vmA8g-bY4e_zo1N55Rtu6VSryuULaSehAwwM7yQmxl0KXZaZDUn9D8TfOxXLLYOS6AfSFt2oI3z6oTTTpABRe2ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=bfSqf4f-M8d27b1FCWHh4qQadU4VJf5Lu79YiOwWTKRb_L-9uH9dHc_qQYqKKWtf831O0eKlNo895Gv7xMJKhDJKwXWRZb5dva2bH7b7F7MEK2ba5UuM5bderjYRuu5XcFKXsr7j7fEvr-RzaIcfOJM_5tPG6dTxEe84tkD5e_1UUi7lqieDsV6ddyDMWeCkQtBbwgwjW5sjyXXiKvZbeTdZ_ayIp4UOpgwzg5eDn49eooWBqQpja_vN9nNoL5vmA8g-bY4e_zo1N55Rtu6VSryuULaSehAwwM7yQmxl0KXZaZDUn9D8TfOxXLLYOS6AfSFt2oI3z6oTTTpABRe2ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌ کمانی‌وبرگزاری‌مراسم‌حمایت از جامعه LGBTQ در ورزشگاه سیاتل گفت: مااینجابرای فوتبال هستیم نه مسائل دیگر. تمرکزمابرروی مسابقه‌وکسب موفقیت است. درخصوص موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24367" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6tCAIgUXfz1x7rtwrLsOooq6FUqBQNC-aGspcKgSy5BQT27zku08YWwNac_nvuKm1jr_sDCJFEq-DmCUN_VXVj-I63Ivg07_hmykGNqNJ8m0uT-HY7qnpFJI1llmkKLYyua-fuWHWcpYI4NVsckxyyRHPRD_p_YUHqZMZzi_GXQS1Vt4z1lIVMMV4rRR3cBUp8Eo_1vgWartWOHqtin-K4tLO0dE8FQCe_mKjgkJaM1NZHdiW7gvz4yp3K9jryozDQEaD4w3CN6KA9gY3NPDm8YatEsPNAkpiHj2_zB0-U3zFNPt4zlGxWFV0O1TeliOlipxD5n5QQ5hjguhDYWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
دو پست کریس رونالدو و لئو مسی در ایستاگرام رکورد داران بیشترین لایک در جام جهانی شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24366" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9-xKVjkwlGN2pJdc9bFIxCvbXe7RcQwFMzb417WKP5qUStExw8-W9n1fPjFQ6YKcwT6tnGgEXqJo9PkMGyhLzwr7MlXKRS7iEe6lSTMw3wOxk_jrl--ChqgAWJNvJiGZrRyQo39XSAEKVoF0CIW_pzxMlb3aCEIyQU61c0bcAntogsNeBVV93zInBb6kSG4q3Dz6_jR7LYN--ZKkalQ03OJa5SDzbH7r-qST4to8l62jAjuT-hZ7Bm1ALJwUvu-uoeIEPJh6Lk_PMByoGvRrqO_nKNaCmKutiHpvL0dZYxppLw-z1zDN6makfVeLL6ryLV9WljizLTd_eT3v5qpRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر:
ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24365" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxdUpYH4cLb5qnrTvR1Th6PcPjFBokIS5SJ6H60Q-64yi2PZJ9ZcJa_ZCMWT3epabFxj0pTU1sqlWiOOHaQ0oRRQ-oFJizA5U0UFhXCysiE2yEEgO0A3OlQGeEuupMjuuXHVhfo3cHdSIOujybEVaI-iTdEHE_4FiyC36PhgWbPLg2FXCVUnaKyRp2FiixeAl-yfpGkndWj2q78pjFM_vvAZo36lS8vE8Ajg213gGxl5vDPy9hjedheQDTCq0bV4pwq8xNeW3i7t0nvhEhIaNWvp_yDO2MZNdYZlP5tRUTxhuYIBHLx04mgTMWgqfRwmLunSxYo2Yoqx_1WZ9ht4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24364" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M02dNoio7gZ4rDmNBEpBcvvAU8CuS765slsZ2dMBeVUw7QMMEHlXyPAa2zKg-MysB4m0Cexx-M4yNlueU6BiNW3rrn4f6r0keOGVni399_3MQjvG4IDIHXWCt-VQ5lygCNSsNPfpmq8DQEpCMC1HvTnDXv-EDEa8Iz3vHdgWHw2M8EYuamy_WqGATpT1nvsUAj8oSX3tIIN0FRxaFckey0Kk8m1txJlle7yEE_0zuDGAkThvTGjd19TSZxpnsE_Q812aERqshpzRF8obtXYRrRKL2FVcDcRsVR52nJvBB-lHFNj2TIb2FnBzgOb7PvkjQnhoCSVzmK4HL5jjsZbsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24363" target="_blank">📅 12:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXmuk5-xIWbQBISOccJJMwkCDSAY3hQMH7jnF9fX8McS9VNlV3pRfGLhjCXox03pJgzoHsC9wKFwjhq0jetfsfCH5tQpfJWwtzZCFmA_4xfD3VHSxQIIbFovLF90GHqsPgRmdqywAsB46ijhCAA4sHP4JAg8OFUPZDkjMFv6CA293w-fKC1bGu3bMBOBCZLExTZO6InLTJxU6x--4rcEsFkaoT4WGp0Q0G-lM6pcqmHsdx6ZwvsIlGNAXYXolkQLNNz5Vg8Wxl-pO8SHtmV1bnz_XQt15gi_v35QUWX68rbkBLQaVK0R5uLPbCe3PfrydJSwJCI1_Ozc7Ou7f6bthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24362" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBJeuLegTMumSfPlDm9zq22ueW40h4sB67q7CyE3El88NjFhNe9q_rRb2osp0XmDmUTWUwrhk-LBiQ17jSb5QObr-MBnibhL9fQPEggYkYc7MqbMVC2IgaTmCyQWkrD_Z0PAcpfgRbDi5e2NFjIeeTbaAcnN61CEQWfXzelV4TQdDW3ivxcaJwbLMsI88NxM-8PytAIyihhfIqiKWIbLZF54lprM7Pxl41m3cgV0tcI5zR41NcRLMPBCB4iCLHp3P6uHMUP7htUyIDLJMX05ejsfnGyP9ZGsMHiv_OU-dFpt8f_spZFa1UMBIhe8uGGpi5he0Tw7KloJwEBTy5suXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون درآستانه‌دیدار فرداصب با مصر بیانیه داده و گفته‌رژه‌همجنسگراها قبل بازی رنگ پرچم کرنر و پرچم‌های بین تماشاگرا و هرچیزی که مختص این موضوعه به ما ربطی نداره و به اجبار فیفاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24361" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=PSt8RL-SX4h-sAA_uW-nb6-vixa3HX1h10_sDf9aMF07-fPE8csALm_tC82EG1Db8GrbamyAUjbQKaB9tXuPCwmyNp_pUCj3aR2iVhutgODUpnnsiCDIrFtYiHl6cXutOadNxCqhkivDjgM-UPxy2L0nM0Xe3AScurwTbg-6zQZQSwWIjvP-_csFjXf_Nr0KTZUgIpaelSzjcYp1zbi6SawUfhOehuln522lw3cm-wZjGFbdt46ZRLMFg1Sh9dyJAb7_xuC2RWtqT6ezfTb20u0J0ESXv0QnqzaCNoZr45pxXxahHL8uV2vZzOhty9SUxdhDlckJk9nF9xGVODXnnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=PSt8RL-SX4h-sAA_uW-nb6-vixa3HX1h10_sDf9aMF07-fPE8csALm_tC82EG1Db8GrbamyAUjbQKaB9tXuPCwmyNp_pUCj3aR2iVhutgODUpnnsiCDIrFtYiHl6cXutOadNxCqhkivDjgM-UPxy2L0nM0Xe3AScurwTbg-6zQZQSwWIjvP-_csFjXf_Nr0KTZUgIpaelSzjcYp1zbi6SawUfhOehuln522lw3cm-wZjGFbdt46ZRLMFg1Sh9dyJAb7_xuC2RWtqT6ezfTb20u0J0ESXv0QnqzaCNoZr45pxXxahHL8uV2vZzOhty9SUxdhDlckJk9nF9xGVODXnnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌هایی‌که‌کمترین‌درصدمالکیت رو درتمام تاریخ جام‌جهانی داشتن رو ببینید باحضور افتخاری ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24360" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24359">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq_MbqZUTERRkyfOL57XiyXpj4DJKqxhMoB1Tq1bT2t7_QDGeRr8ySb-ktp5uY56gnwMRRAZ096K6NHZv-6227-2gCAzfPYEZVuMyU4KsCSQtwDCRV-lq8IQOuYqeF4Au8X1YeSonMC2v3ldqNXCWXSf_rVqUoOvqEe_P9DlM0UMsFLeWE59_umIQsktVoY2yo9hOtjM-QUuiCvopEP3jrNDlwuoSsPnbAw9-2H_3NE3qr0kcfOh8zF-v-ov-pgbJ8gt3KCTuelNClXFXTu7T3eLMOOzzaqjiFKYApHuljkZMVgulANzgQ-0pw-8W7Mhua71wWmT4eTOmZuIrbIf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار مثبت 18 و جذاب جام جهانی رو در پرشیانا آنلاین میزاریم. اونایی که جنبش رو دارند اونجا هم جوین‌باشند. ادمیناپست‌های خوبی میزنن.
🫦
🫦
🔘
@Persiana_Pluss
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24359" target="_blank">📅 12:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24358">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzhUnvS5-N80Z8IBY-mBZ_Aa46rDgKZ9_sdamxyLX1GJqMTPz9H2-q6N8yP6UhVVuiMrJuvpVFgI-z0O48A-CbUhfVHz_EYBZbVvgPm4bMCM92RL8qYwBilwaPD-H4OEwzNqz5gnYV7uq10hPVz_ulzubMaM9GJ6_cWqeRZFcOuWW2LQqsOIep8dY4qBgoIHbzlEgLGBDWquctcp2NGmG2Hv8HGOEmpmJnz_AVrEhlZ7Oxtr99DBEyAmEOCJB2WnwKCHv3eYL7lfFhonqi_fBPCNTjNCQArALe_i7eTIARqTassBk7lvo77uD9rAC2F-uNmUhJ89rUmmH6jmNlkc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس: دراوج‌فوتبالم و درسن 34 سالگی خداحافظی کردم تامردم روزهای درخشانم رو از یاد نبرند. موندن نویر درفوتبال درسن40 سالگی نه تنها هیچ کمکی به تیمش نخواهد کرد بلکه باعث خواهد شد که مردم روزهای درخشانش رو از یاد ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24358" target="_blank">📅 11:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24357">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwfwLB_NMAInpdbjN4_-HIQuDi5ddLnXIfvQbMmUxEaJmc_K8fHYirEwPUbJoCze8NDB59Lk5UXHUQ9gaIKaBgZ1Y0GGyyC3z7JjQcyvGpZW5G5TTb8hOefTeUlc7Kl4XYT6I9pCJbmm2XGMqD0Ji34vxsLIVdvnNbFbEkzuWpIZZ6rSyCpuvdi4gPs5_gNs6ysMQ63uOnkAtghHdh8ENrb04TPy_47_fkZMNpKkcZwYwuxXSqbusdId-00ilgS2QfEyBmGxja57UKxP3YwHU8TkUSJSLZpqajqjVJmfLbessD0CQd-trb1W-qku5Ho41-5ZEjAPtZc6Uo_2rTaghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الانگا بعدازمساوی‌سوئد باژاپن خیلی‌ناراحت بود و فکر میکرد صعود نمیکنن. بعد از بازی رفتن باهاش صحبت کردن گفتن آروم باش، صعود می‌کنیم. پاترم توکنفرانس گفت بهش گفته بودیم مساوی هم کافیه ولی یادش نبوده. بهرحال‌الان می‌دونه و خوشحاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24357" target="_blank">📅 11:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24356">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlegJVrpt3Gc5yR7DqZWVazXv1i7uVsGlo2868-smaOn_ld3Tuseau3OEXNTfKBJhVVYCFkyIDmfN625CfKj9Au-N8BxDsgo3FaGErPPQHvZOnr6aA5CiI2-0Vcgh0arEqTI46j-Lu4USZbWKA12_foQ3RWropx2G4S7HLRWd14m5kA8f_Wy4vKgb1rCtRIvAFQUYZwXyuz8X6Xm7W0tQMQWrlo-lO9Q6zVuJOtdc8lTBHXIzRrclD-yV_DEJehRYibHy2z0ERXJ2olLxeaOMstkhe1xDtuyF1qiNxYluyz3la2P_hQAqdeiHGtOkmA2iykYJcTbvE2WZESxUTyfxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
ستارگان رئال مادرید؛ وینیسیوس، امباپه و بلینگهام در این جام‌جهانی در اوج آمادگی بوده اند و ۶ مورد از ۷ جایزه بهترین بازیکن زمین را برده اند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24356" target="_blank">📅 11:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24355">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0i8d1sbCzmYeMp9fAi5gUuG49iEr7gjM9Um3UZz_7qoLLRNPJ5qUBSfdvVwd9BkeyxltiaqxoqdHJ9X-3iv0zAwZ4-V6mYN6DTGt9jU0CVZNMHFxcGdYyRHnx9_wKe3wT4R-7BfGvoeilKvcpz2xbM6S-CpFHFUFM1CeMPQVWLEdm1VPxybO2rFvKJl2SPeGtUnhAq4VXGXNx2J-dQdV0PJgo6kj3hVcgLeWJGxNB9W3MUHKLcTn-oxL8gtvNHOjUewXsiqyN1IUJ30GKHPLZn79PM6voaBxCWx8kEEytwcjRJeDEskz3pV2JUNu1aTYEQdqhceNmJsitUDhcE9xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مبین دهقان هافبک میانی الوحده امارات از وضعیتش در این تیم رضایت ندارد و به‌دنبال بازگشت به لیگ برتره. دهقان فصل گذشته قبل از عقد قرارداد با الوحده در آستانه پیوستن‌به تیم پرسپولیس قرار داشت اما عدم توافق مالی دوباشگاه‌مانع…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24355" target="_blank">📅 10:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24354">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=dDOZ0Ho7RoDBYNlgPAAuuNcBKVFD-S9FGb4I1fZOjeCcw0fwI_mD_-6S_yIVNsLJpOLUDZDdvEPlCDlXAI5I---zFBE9kj9fVqvM8PvOsopn1lri3ANI-RlBn0X7fhyAJoPPJxfmsNCRo4lz8QpKauAuT6RDRaKKxZy0w7UzgtTZNv5Dmy3Pumz2FgJwUSAMWqh_pZVnkLKu7ktN8cW8niXPGwEDhKvHTqVQcTrfaJc-Na-InZXfD21zv6hIiw_4iwv38hXXBi8i2QsEHsyrXT88jb-wJhoRSXDMEg5L0xQeS_hfj3ZYFbr1qLk1z4c3V7X4ixs7c4igZxUQwCqTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=dDOZ0Ho7RoDBYNlgPAAuuNcBKVFD-S9FGb4I1fZOjeCcw0fwI_mD_-6S_yIVNsLJpOLUDZDdvEPlCDlXAI5I---zFBE9kj9fVqvM8PvOsopn1lri3ANI-RlBn0X7fhyAJoPPJxfmsNCRo4lz8QpKauAuT6RDRaKKxZy0w7UzgtTZNv5Dmy3Pumz2FgJwUSAMWqh_pZVnkLKu7ktN8cW8niXPGwEDhKvHTqVQcTrfaJc-Na-InZXfD21zv6hIiw_4iwv38hXXBi8i2QsEHsyrXT88jb-wJhoRSXDMEg5L0xQeS_hfj3ZYFbr1qLk1z4c3V7X4ixs7c4igZxUQwCqTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇪🇸
ژوزه‌مورینیو:
من دوست دارم بازیکنای رئال مادرید درجام‌جهانی ببازن و برگردن به تمرینات تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24354" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24353">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇵🇹
🇵🇹
سوپرگل دیدنی نونو مندس ستاره تیم ملی پرتغال دربازی‌مقابل ازبکستان رو از نگاهی متفاوت ببینید؛ همشون فکر کردن که رونالدو میخواد بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24353" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24352">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NdW0p3IE-oSBJWYqzB8KR5leQH1LbXz7PgoRqMr_LNeEfOj23xNhOusTVHraptP3LHVmIRBe02JLm6_HcyFSHx40WHiEAXoV42xZjSpQTVHyYPCUOljNm-1PqbbNctk5zwerIyUYNI3xKiMoDgXc5qlJ-sNdvseKPmCx484cf9pZwcXqqERiAmwfY_wwqSRIBIiGwX1IY8X85iA-0QnemZ5w5entm1UKSvTBMwTCDgnwm5MWYoJJ4deMkRpCFl1GWZQDyvMlcK-uBcDJaGeSL3w2-do-PVlHczzgkTq3LjF-JXydfSqm3B_HY8PSOJmA7Wk7Lk0iUTx0K3JUvgyYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوق حسااااس
فرانسه
و
نروژ
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود به‌سایت‌فیلترشکن‌خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24352" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24351">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFNNyiBWOZQMrPg7ioOHenODFZo4beKboLfSiDjaQlqr_mtve7zKGO0-TeA9g_dxfSYibmoXD9plpkXdN8bamISMeyEMTFkPEh9bHDfQFjXVfW3RovQVLGVf4Cgb8v3dSbkQ9tPqIVG-fwlxYwzcDi7dxIJCPHJd8PMAn2SP6AKP23C-2nZnJAXrR44yJtUf5yMgNjpDR_Fy5s10H7vRaLJRXVIFGIyIyAQ3GGYjQqlI5KlJcoMGmFYrEtdmvKfCDnPuuPdzuakfTjuUv96boelEc_vN_ZkMMj4Bei0tJKoK78_8tsOZJ7mpRNEp1uTmV5qFWI74PICWFxWjwep-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24351" target="_blank">📅 09:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24350">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFQ7ooTQ-EJxxHkspO5wgTD-DZVegC9i_CRA_qPUr13WZHnbqtq4he8Amih6G_qP1CJ1ABcB2J-cjxjbdsTmM8WPKJ9hFa80ddShUhPnC28GZ6Aivj55qAGCm1FoRQKqHzMnemQOSiD0K0U4E1Zs5vhSRupqL4zWmlIJKa7LLSgsGNY7kbrr0WBHFl3OE4KpnFplmPx_B9eFyEtKdqh2jKOm-N2712bipIRUigz9TqPjKy7zHI_CJdnb_ngw2ZFiDbAlCkwxH7jqL9L3x-cDfkbBQ2lL_-_Op3faKsZMaB3Js7wGd5bIY3QjWzuxFlUgXtpDx1gpCIurNqtRcAm3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ برزیل در مرحله بعدی به ژاپن خورد. هلند به مراکش.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24350" target="_blank">📅 09:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24349">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=XwUYjm_YQxkF5wzCMLucBtB07JIPVJ7f0nvwDeGDrrr50yarHO1J0G3WPxhKUtYRSdQGcfYPG2mfxYu9p2NPSGjcenM9pHtEZ0i5kECiWQMdUddqIlT1QSmYJtVkwPh8AScFYH5JbIQJagQ4n14eSwWG-7lxB_15YeDshZ4B5fgMzGx546lkv9m7Oqau85lWrCqXwM3Thit1-Eoill-PfPPFz5efxOQMNrFhWLkwFoRJLyfILGTS1SKculQkTwv0h1vhMNCRGWnam0IzD4yyZpITHwusygktqtlPds3WaWyOly3e643AZSmEdkkVkV6o6ptN70zUpqzHQqOxNKlDJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=XwUYjm_YQxkF5wzCMLucBtB07JIPVJ7f0nvwDeGDrrr50yarHO1J0G3WPxhKUtYRSdQGcfYPG2mfxYu9p2NPSGjcenM9pHtEZ0i5kECiWQMdUddqIlT1QSmYJtVkwPh8AScFYH5JbIQJagQ4n14eSwWG-7lxB_15YeDshZ4B5fgMzGx546lkv9m7Oqau85lWrCqXwM3Thit1-Eoill-PfPPFz5efxOQMNrFhWLkwFoRJLyfILGTS1SKculQkTwv0h1vhMNCRGWnam0IzD4yyZpITHwusygktqtlPds3WaWyOly3e643AZSmEdkkVkV6o6ptN70zUpqzHQqOxNKlDJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24349" target="_blank">📅 08:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24348">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1MOCrg0WVSNJ-qCDV_u_SAwUeYMX_V5gSQTK0mEsxt23HGL97g0MjC3Rcdv7sMC2cVtkZ_V05-Sf-P1cxnAfwzm6io_6t3O6IzZboy1apnf5iotvrALULCKWlznMmkFiQ8XqcCUE2NdZDhaFNi8TgRWtrIcRZMQHqeLOm63PXDoWV_nqpAzNUzbfEgYgnnBkYInWd3RhfOMP8V5NcH5MhlXX06xaXMyWuq6pIliMLhRL_rcPZt3ZFT66hhMrbZ8z5a3gJQDknkpqDiqe9VFfX077FzZZzdT3hsSr7OOUto-4x6z8ITXwmTrSVX-IvsiU4qPtPevG8JCeyMNU0GsiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ ۱۲ سال پیش در چنین روزی؛
آخرین حضور جانلوئیجی بوفون درجام‌جهانی؛ آتزوری فقط یک تساوی میخواست، اما ضربهٔ سر گودین در دقیقهٔ ۸۱ همه چیز را تمام کرد. کسی‌آن لحظه نمیدانست آن اشک‌ها اشک وداع همیشگی‌بابزرگترین‌صحنهٔ فوتباله. پنج جام جهانی، یک قهرمانی، و یک خداحافظی تلخ که هنوز از یاد نرفته. پایان یک اسطوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24348" target="_blank">📅 08:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24345">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOQ_fczshr5ttSTHHVXxV4qtEbi1tFL_IqWjyPF0bqPRV14Obe8x7L_3u_nnfVGaQmC2gxR6RUJi4K-z14GctAK2ZQqiQZUjnptnUm5MXM-uGVtz0bmCXcvRevvwUYw9sTBVRt8DDM3m-qeQ-o3PX3G5xFjuLs9rG246HAcKAJtGKVmW-rzwfvIiv8G7Mr4AkozBLfm8pc4NJTP-1gy6X1I-OTnspuuqd2mPis0WtneOyUGci8x7LRo3zEP0Hz-UkJFUDIloBg9GdnU-bmY2AYEJS9TMVJcLXJco9bpLIZ3Qrr7ddIGbfBs8yfAFks5CHH-S-uNsa4gUTRhbBQS41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F و D رقابت‌های جام جهانی در پایان مرحله‌گروهی؛ترکیه‌بادرخشش آردا گولر سه بر دو آمریکا روشکست‌داد؛ پاراگوئه با استرالیا بدون گل شد؛ هلند سه بر یک از سد تونس گذشت. ژاپن هم با سوئد مساوی کرد ولی جفتشون رفتن بالا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24345" target="_blank">📅 08:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24344">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJeCo6Hqs2y-4hi1NDU_UAX1W4JFmM1aYaYU6A8v2DZA9UUjFthEeOdmvRNt0_-QX9GNx7IlOj9lXFrQ4vmfOPX7RDA-Ib-Xi0ZTcbsMqFRPcAqkoGPFrq1NehuRm3GZW4u5lWldv-CYVpYcocEcA2NVQqlW9gJI8sy2nl4n1-DE7W2yaai5sYAOUfi183KEWGv_8673RtGzdaMw_E1oRq8s5OBNXLyo-hL2hvftq8WhaUWEkhKqDkcOSkqASdIS_FoYWPBP3yyHP4cU6pSooRcflZ_gUaPM1UI9ZDIdvrsK7bm6P7ibPCX4zC-XGY0GN9WwsPdG3ApltsSS5oooOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛ از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24344" target="_blank">📅 08:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24343">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVzUsQv_UvTlHbJd9b7UmWC3sbZOywL02oMG0iQ-EXQW1m67hsihKSXWYUYsGFzv-E5O5hGIYr9YtfV1R6qlAvOrQVxgYof9MxL4VX956_wKXteWhHaThbOxZaNbX81GAnflJ1JobsGKzTfB6VP8OeesuQsVZcbmJ7N48xO51-hcANyMzNdRhVBPeRw3SRdmvNwls3ab6KKDx8otnh59A2rmGTBMhdqhDBt2HHy4WPNOFaSbYX_wHbrpbbMzo2R_QEz4nrxEZQA5G1mV9lHcpwNMlDdjbpg6zBAa2gyQ5M6yvNnT727Zj-tox4WFUK10ZHBpsEMHpH2zDMx07GJ8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24343" target="_blank">📅 02:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24341">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqLI6ACfqMNfvx-vmmr0SaXwsY9qioLnCJf0DOIHyws7TFqkHfaoCU0u6_ebRB1EB9aj4R_1d9U1xHRCeP5oAJoXJcHvic__ojszdqgEQvosT3v8-3_JBxmhNvyObDvF5_0P8NV9HZjLoP5eDxP4yCrQlnXaVGPFp_h4aLDNMuohnMTUOwCaf3PE6RsPkyplHXPGJBxX6XAGl3DYgDNEdQB2CsvR-3NFqoeJbUvcsowngaZ1GrMHBLEnSvsyEMmx_-gxv5TheMdCiSqWp26oaLui5ZxxIUIt2OHiNpDiV0fWSqTzMQ_wSnXGezoBFobhGo0Jcr354fOuPW5KA-Df0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛
از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24341" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24340">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwnVNqErVeerJyA7QuA8keLiOVttCdL9G2b_Vm841sO8Qq_aAleXCvOwvMXc5n2pAnLhP3mDScIox6Y8U87xr_hTIUrPRdKHZBYiWrDbKTFLsjIUhJzyFy9XG_B9qHN__BECeVL2Y-IhVxRBos35lcWmR3-ShmDngiOEHkRiNjOghvPsVwiJcFGRvhI_l7ATSTiLDOgYdA91DSw_2HpBOMybMh0JK6mrQjMgN_r1O6C2j0wALPT9fKLzCw0Cswml1B68WKPYYLpJFtST60Uso_0Od05uutfjISnGtHWx_TjbrVBNvvxHrS2r1Izlh5g0NAElK-ftTe1yz_fV89h1CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌ دیروز؛
از نمایش خوب شاگردان آنجلوتی بادرخشش‌وینی تا برد دراماتیک اکوادوری‌ها مقابل مانشافت و جواز حضور در مرحله حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24340" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24337">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24337" target="_blank">📅 01:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24336">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGUZJvEIvzMIvtdcrkWDz-EZENWpPDl2VRmhz6tOtrdmyk2oRagu6qwy0iWHx6JXory7HMVqR6-tYz6gB6ZhcWmMU_Cjk-wi-nVSQD7Awz71Y_dUgz1gYkmP6Fq9mNMCn97SVfiI01zxf7OQA14eqRoWUM8kT1zE5m7iuubISYGSY4hoUdHJpUnKYXhJ4dyeT2nZHnoG9xpidXpRNLkN7R5kDc0yPw7L9fvWjsUslcSbuW9tZw_WIUsS2ibLWp3UUJT1ASEm4JLIJmOPw5Xd41ULAxQbd1aypTJ4nIEXhLyWiSDssIX_Fbuu6y73kZgeWnnf5PrgErBW2XAp7_VmPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24336" target="_blank">📅 01:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24335">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGXTftSn_633YLiyc1DTixyv7XteeHWAnLtBjbC0gbY2bwGkhpQXeJN_2OT5-aBbZ4E7pWbrqvEOffwfDknfJwijoreVIsV-k5StK-vGSMX3NjorWc25vdUIEFnwsgkr-6btJLYH9UL1NdVS8VLhdfRrWG8BOZXqIXU8OgGIKjbUJ5FHEZ_hB8zvTsmf1LUJY7M_cOMU3DDxemilA98e9JLKtu1T9BMoqPJQ6qNIYTmsCWg7utsnD7eTf8UqY9ctsKsVTM5CvKVf1LjiyN0kRub931UNprWvxGhZpCbr7doIgJRYOI53IURqqmE7pa-3NVJ042cCoKl7o8-uO9uVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24335" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24334">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=LKxOOqwvfLB2BDm_bNdAlYHOV2OQyXINfc1HTIrB_qJ_J09TQxdh0yNBBWbhN1u5RCQLgU94plGdvStIeWEaM9bmK-FCFbKq2Dvv9ymb31YS__W2UzU_MttMcScrFLsGCjsckC5t8mySQoaUthCANm_U4SMF23TkcSZU3Y3zDpjXQuhUF2lQm5fsXs7pUhqAt0WsTMN7H-jiqtsl0p3DmoD2kmkD0BGBrUfq2xmjoPD9uUmF4HicJU-GVpVVXvN3WQsrUcohORXVvWnWzzYeAZKzXpUPFvF2ZFq8JA6WIElosOb-bjQkgalzpMBLlhpIMosRnLjDnXptHEAP0jc60w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=LKxOOqwvfLB2BDm_bNdAlYHOV2OQyXINfc1HTIrB_qJ_J09TQxdh0yNBBWbhN1u5RCQLgU94plGdvStIeWEaM9bmK-FCFbKq2Dvv9ymb31YS__W2UzU_MttMcScrFLsGCjsckC5t8mySQoaUthCANm_U4SMF23TkcSZU3Y3zDpjXQuhUF2lQm5fsXs7pUhqAt0WsTMN7H-jiqtsl0p3DmoD2kmkD0BGBrUfq2xmjoPD9uUmF4HicJU-GVpVVXvN3WQsrUcohORXVvWnWzzYeAZKzXpUPFvF2ZFq8JA6WIElosOb-bjQkgalzpMBLlhpIMosRnLjDnXptHEAP0jc60w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هوادار تیم ملی عراق که تو صفحه‌اش گفته دوتا از بازیکنان جوان اسپانیا بهش‌پیشنهاد رابطه داده‌اند‌. اسمشون رو نگفته ولی گفته جفتشون تو بارساست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24334" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24332">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMYR83cZ01LNJx8n3RAwt2xwgJXZpA3UJv5So3iTJf-CukwYaUBsx5YFDU-j3-IOo_2W1rfuuO8Wb6PrvCvQaBqW4ynzRp4_FhmvqkC406VoUZwbQXyzSjyccTBcKAnSaiel4pSgd7ClNzo5QQ5Q3G28oLFfZ2JsEVXpGoyKurNkjKuIl0yocwv9yLF1n9ueIOGFzkuNUfuZJ2clouP0e3Y-z7cnwJ5MY-1zTppq7Zxub_a2sBQolxoXBUUr2SpeZSPyUJB-XM_XesvjhS9ad7uVjrSrYkkBCDTqlXCV_c1-ph2UaFvsJfxT9hKttlsGN1Saggxy2oxZJY7IKzROhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24332" target="_blank">📅 00:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24331">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXEsNHUQVoAHi97Ey8kr7wQiWAtFJCD_VoioGevXj4jZUipssSZTnk5i9Hkqiueyevii4pNLr5AqeE-sXpW_HXnyCZzbZb1qY7kdTEw5LKGWEZqkIoXdN96OObAW_dRS29ZTXJKxT6xAw7AAer2VWu1rz0RrMw5AZlIVN-DUCMULsmjCka9d_yQnX0CkcVk6CmF78Q0djNngl82sjpRXnUjDhKyHV3iqVMHuROaBJ6NqzyTr3UQNfPplEHLaGTlNKl1K8sYxOsGo5sNzL82H5s2Wm2vtGl4agXZAEj-CMiaYgZ-GGGmreX4PHWe0h-tnKqdSQTModslleU7pdzumMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24331" target="_blank">📅 00:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24330">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZQLy8gju72TlyhMMQ_j_mg7JxUbckDZ-7pEF3AsHSIEai4oa9g9YDMMYy1uFMEbipd1daPysn3Uoi_tdfa7xq3cCRwp8im6MrONCye77733P2OgGP6B3W5mIB9puDT693xpRxod59kcLnTRdtZmNxzlYwczR0EidElT56mQrxCIgw52ZWi4wE4WBbY_kxk5u8i5CmKTWLRVHAbO7WN7Db07b9msAgO7QjwtwhkUrRBtYWroCXjb4YFgIBHmVqtLt_oJPfxctlPbMlc0CBIwseBLFWPPiRXVv9YaXf8YIF6s7j17bUqYDzl-6Q7a2E5QPD6TSp4aNKhx6_Mxa0WSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24330" target="_blank">📅 00:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24329">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P--hee6YjBQKRDgootr86EBdCmHjOGMAKhvbyGy_Jo-fGWd8Ldz4Tfel8E6ISKipsVayo3K1xFkAYo3Ff5xwUQdXjHz22c_a5JBRXtJi8VxrT6F1J6x-pZyG1oTpIKbCgOUDlYU-WcgRbRuWVjViplG6Xsk5JCe-pu5Tz7SUDTNVKaExSMxAxtfS2doijfQsSR0hECAG7m57co3qb8Idr4Rvzch9-DIm_AE4zOavx5RG2FkJ26r218l4RpieETN20SZHn6JJw_5369fXz3KVSXsGUsqjg9pU6R4yjpQvrv_oCJBlJZfGeSHV4QbkUL8sL9WLsiqtPAf4kwVplpM7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط ۱۲ تیم‌از ۴۸ تیم‌حاضر درجام جهانی بازیکن سیاهپوست‌توترکیبشون‌ندارند‌.حضور فرانسه بعنوان تیم اروپایی با ۲۰ بازیکن سیاهپوست از نکات جالبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24329" target="_blank">📅 00:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24327">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=CMyRvLr3HG39oEuv_1qFp0nKopt6bncmWcftRDcNW-XF2WuB5u_Cjz32pyah1vUtKW8LdC17j2s5Z5HJPOT9vA0KNVuuE6UGAtyDQwKzSv5xAUamG0yGYr9xBi3QpEEqi34dpsLoXz3qomVM7VJDOVKixF2694bGrwMJgCCwjam2flN0oCR2e20z4tOMAY84-5M8UNu0hgJ4dXeS3V64_kLP3_298OO5fw6MpdXhwOk75pgyDe-8Vx2OyAM9K9sufw7PnurDhhCinPR2m8YY9FynVZzHwI4-71he0bfzixRTCQdg1VdsPKl54cmP84N9C6aXHEf19ZM3Z_vUr4KU6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=CMyRvLr3HG39oEuv_1qFp0nKopt6bncmWcftRDcNW-XF2WuB5u_Cjz32pyah1vUtKW8LdC17j2s5Z5HJPOT9vA0KNVuuE6UGAtyDQwKzSv5xAUamG0yGYr9xBi3QpEEqi34dpsLoXz3qomVM7VJDOVKixF2694bGrwMJgCCwjam2flN0oCR2e20z4tOMAY84-5M8UNu0hgJ4dXeS3V64_kLP3_298OO5fw6MpdXhwOk75pgyDe-8Vx2OyAM9K9sufw7PnurDhhCinPR2m8YY9FynVZzHwI4-71he0bfzixRTCQdg1VdsPKl54cmP84N9C6aXHEf19ZM3Z_vUr4KU6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24327" target="_blank">📅 23:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24326">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I30BhZvUu-xE9Qb920nTwa3pRRue1OKgh3FSaIaAAy5M1NYwRJSu3xhmM4l6hmCLMoFjVKCenfd5Gr9O4dEFBI4HNvJKNVAnzJerxm2_b8BxSS7C6MScWvaAxmSSX-b2Xnti9ezPbB-aYqiW5TamdL388uZu8s0JiqSGnb2bB6eMVbpLCo6vJ9VGmsdvGyTYnWA7xtC5MuXCUG03Tt2traSyQqVVLT-ceWwoNCh3CwIsvQppjybrVFFyg2mSt3fJXfsipOxXLAfttvuUr5lFU2PXu-m-iKoKsBOuicrB1y-OiBQ5qFDSs24ohjgVtqAKaCIb04n8cpyxgC2dBNW5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24326" target="_blank">📅 23:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24325">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxYAt97RL7ilM0I4oZ6RFkV3REJKYMrX9yMzjVaelejXxeVi6HIXWdAR1seYJCsirsW4lwbaa7SWO4PkzPX1tjKz6X7sXr6WwUY5kuAjALBoXAG94zyCBNn3z2TtdkJYeEjHuxP-fQvcQhhpjvfT-YvkRWawzy-4lt6rpOZahuwcmy1ucTGcXavqrXI5j9m9WxmfNNWSYIZ_Z6Rts4QN1lnvllFpmngpB8jLAYyyKdDrLQ-sYM0Bw01rzOXEs2YzsVN_4VZcgmaCnTwBn6zcsmFkeSUwHRXu7yfEvUik4KXrvvEiBZ3tDPWDPkZilv1pGgHw87ZnCHpSTFR3FGfnhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دوست‌دختر ژائو نوس ستاره تیم ملی پرتغال هم امشب از نزدیکی شاهد درخشش CR7 بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24325" target="_blank">📅 23:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24324">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
🇧🇷
خوشحالی‌منشوری و برگ‌ریزن هواداران تیم ملی برزیل حین گلزنی وینیسیوس در بازی دیشب.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24324" target="_blank">📅 23:28 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
