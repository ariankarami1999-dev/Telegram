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
<img src="https://cdn4.telesco.pe/file/FkoP_aIeIL4_-_inYPZro2KkX3opEAg21gfjMIaaHHMqWBonI0wH0NP7B1zMp9_tXARGNQLpQBLhpn8-vBOAwLZ1aGwwmFjStYdT7Ojt1pJias0tSQmw3qUZHuM6ax2iPaGj01C9cAX-3EdnCWYbkSH3AAoyKdgWRKdxJca61ijaFJtRyCvS83xET_e0hk0Jt_s4HmLIW99JH6RzpIrlJoF5KQM6TdfnzHjoUX5u7GqxpP8_E_ifu9k_w-Zv66zlX49xblAQJnVD_BxIABhHXMaUAvSxqSs77j0CHIjzii52kUIcOBZvE002_HJgdbEh8RIlT-NkM6M5WcmYOWfjEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 217K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 20:51:17</div>
<hr>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Jf71KIbGugXtlVk2Y6YKtb5HiveMEM9H7lR_ADYwwW4TIRFbe0V6jZOmhWw4Hb5zbxJH3pXKk-M8TnQ0EZIwUauYka3EmYCJIUfFfZBDYmv_Tv3CJ6Oo35OdoaKOy7ZiYpGHOWJDcUXhJVh4nGR-S_l27QVRlv9fhscPd5K-5aqdzO5CqPVSf_pPqO7yZF-cEr0zqHC6o0WK_Yw9-YFYPOR4uTn31BlzBSVxPSwQaqxUgdnpwmninipI-9-ER26cR2NNOa4S3GtJRSSSZRgKe7X0-nTWWsFwr2hK-S1D0XWy6X1hpYaHomtfFJ12aq3KjZEJxiiYJwVzpT6ZeLlZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Jf71KIbGugXtlVk2Y6YKtb5HiveMEM9H7lR_ADYwwW4TIRFbe0V6jZOmhWw4Hb5zbxJH3pXKk-M8TnQ0EZIwUauYka3EmYCJIUfFfZBDYmv_Tv3CJ6Oo35OdoaKOy7ZiYpGHOWJDcUXhJVh4nGR-S_l27QVRlv9fhscPd5K-5aqdzO5CqPVSf_pPqO7yZF-cEr0zqHC6o0WK_Yw9-YFYPOR4uTn31BlzBSVxPSwQaqxUgdnpwmninipI-9-ER26cR2NNOa4S3GtJRSSSZRgKe7X0-nTWWsFwr2hK-S1D0XWy6X1hpYaHomtfFJ12aq3KjZEJxiiYJwVzpT6ZeLlZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=OHDGa1HQv6JcSYxWgOuLpI9xGy0FvC4kEOj_xf-lpa2V-IIjbHK1OoEFoV7HSY09IAWYD0rZg3Xk9zdY89RY5b-EiOfEA7nFquSu11DsHcFvF4RWqYUd2MaB4-RAkbGGREjnsizbtysMiA-ntecEQ8Sgd-51TJqgVlCpyCt15W9gO49U0Wj3XLsdameYLsHDvjq3uuqkFZi8Dlza4XXdJjXmCZuZZW7osvRMIxJVM3UTgrbkZ1HZJlpuJJ_JA6Q7hXgJXBoC560Rc6PA1r74UY409ZJXp2k6Mcm11dwXMi22pK5miMYpLq0Y2iCS_KdHWziHG6HzpmqP6rMKQO6uSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=OHDGa1HQv6JcSYxWgOuLpI9xGy0FvC4kEOj_xf-lpa2V-IIjbHK1OoEFoV7HSY09IAWYD0rZg3Xk9zdY89RY5b-EiOfEA7nFquSu11DsHcFvF4RWqYUd2MaB4-RAkbGGREjnsizbtysMiA-ntecEQ8Sgd-51TJqgVlCpyCt15W9gO49U0Wj3XLsdameYLsHDvjq3uuqkFZi8Dlza4XXdJjXmCZuZZW7osvRMIxJVM3UTgrbkZ1HZJlpuJJ_JA6Q7hXgJXBoC560Rc6PA1r74UY409ZJXp2k6Mcm11dwXMi22pK5miMYpLq0Y2iCS_KdHWziHG6HzpmqP6rMKQO6uSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaoHAWLGnm-SsJHyNFl1K0_Jqc1hb3oHqoJvYY8wF7SmxWVca1Oy9Rayl43kp8q90pJJ0vhJ5C0Uzub6b7-Vy-LlrSONLHf7qWjCWvDkkfwjNlrKdtofdVT9P7Cv2bDaC1F8qJbtt1-RQsk8kiLEYAO6s3C9CNN8AGbhVqA9koxnOFU0MpSAPnTLeMUm07v3kpq3VHTTVhw7se-AEDpc0QK8AqTR8Q1boD6TPbqlhIOzYOEaFB-iFWxrd-I4i-WRoWxt6k_i7CGnsxzisVppDYKcp-7b5klSKGqIfkOcvGPAoC5NJYeaHau3hQWumEpHT4t4zXTWV4dvNuz7i1XPPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfG9YDIHFfvl-S_btL325FsNuwgg-TWsCjRt1pjTPW8BqZ_wkhMHgvq6Ga8MkchVsjZGJOM86UK3V5S37ts5wrt5ToRdvuDIyqiwe22MH9R4NhRJ9PekzC10Yg83YO4bv5w2uKb7RhUvggFB2X4xoaDPDx2prqSqhcVAo6AWn0plkxDGnUK6vz2AGP-oLWoT4aRKo4t625QgIUcEkohLjp0FwkhZIYPkrqkx9nNfFfgzts0hOrfEu9-Jj3ZcnbbwRv2gpWiCLiwrN_zthAPCUAKVrX0MTmmozx1NZk070MwMTfgW_tKiliqc16rY7Vzf1i-UmqYeEspgxbb6GYlf-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=mMVbJz35GVTuJbx2T3Jj-dPsg3MEwz5fmBpX_Yfms5GoTOE-Z2oABNV2jrH98UiexHHrihBlnxp7TMKihniUOjg9CG3TMCmz5lpsB2deoHA0S2EOwpbh_Opv4l_z5vZ6gEHvi3v4oT2BTe7i9yACoOulaMKeJZoyxKsqJ0PmAF28NpT49xzdJKvO_Vc98ICCFGIKQPr9fMpuotFaVevKL8sgTU0P-AFUAdBtbdXm54Er1syOHXVKuKsdHuOVIEpDfcnZhmQk_HbV-HkPQy7D5BPXaqynsJS4oGt8LMKRnC8ZzcmI2TacOlxodekyiJJXy4E7myNQHRF84eLQdE7O3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=mMVbJz35GVTuJbx2T3Jj-dPsg3MEwz5fmBpX_Yfms5GoTOE-Z2oABNV2jrH98UiexHHrihBlnxp7TMKihniUOjg9CG3TMCmz5lpsB2deoHA0S2EOwpbh_Opv4l_z5vZ6gEHvi3v4oT2BTe7i9yACoOulaMKeJZoyxKsqJ0PmAF28NpT49xzdJKvO_Vc98ICCFGIKQPr9fMpuotFaVevKL8sgTU0P-AFUAdBtbdXm54Er1syOHXVKuKsdHuOVIEpDfcnZhmQk_HbV-HkPQy7D5BPXaqynsJS4oGt8LMKRnC8ZzcmI2TacOlxodekyiJJXy4E7myNQHRF84eLQdE7O3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=PEK4GQjUPIcAIxLOhC4kjjCDRkw4GV8H8HuQLWn5s91bA3sRAG5jMgPG0GzFIL6sYilfc5XAdbAH0ytRlNCLkPN7fhAqbXT5B8qG-VWCbPieWdQJqjf8LNqp_fdwApRDK1ZNzfuMykoqcxxgKNi_0c6vPTxvGuU-9wr0dj4KYhpiQoFbF4pkMY-BWpGdClPgoCGMNOgCl-taCZZUIX5KjhXNBDw9mMZ3UTEPK2SMYk-6rQ54Pf5VXOxk_FoN5zwRPUU993SGHhV9IBmUIVQardapJO2M3iOfknSKmYX9QZ7PBZS6-ksUArUhrPH3PLB6_ByjnkFg3hbB8IMYVmndoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=PEK4GQjUPIcAIxLOhC4kjjCDRkw4GV8H8HuQLWn5s91bA3sRAG5jMgPG0GzFIL6sYilfc5XAdbAH0ytRlNCLkPN7fhAqbXT5B8qG-VWCbPieWdQJqjf8LNqp_fdwApRDK1ZNzfuMykoqcxxgKNi_0c6vPTxvGuU-9wr0dj4KYhpiQoFbF4pkMY-BWpGdClPgoCGMNOgCl-taCZZUIX5KjhXNBDw9mMZ3UTEPK2SMYk-6rQ54Pf5VXOxk_FoN5zwRPUU993SGHhV9IBmUIVQardapJO2M3iOfknSKmYX9QZ7PBZS6-ksUArUhrPH3PLB6_ByjnkFg3hbB8IMYVmndoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=D8a5GLdpUfOkdMG_3FRp7W92p_JRPV7vE23uGUnXcRBazmJzVvEInpitTIm5GFENIRiwBc8FHWEf6-SZnpU7KdqPypscIdqDcQLVudSQzeVrUA5slanDv4rTVyKS_6UVne60cXz_1xMS6iCglUTTGMze_SHeh-fTgGfOAqThpsijvglCh8UPXcwqRi3l5RtADQSrT7watIon-pD9CY39_L7-ClrK4l_RVBpsKTOsBivLy9dnkzL-rwSLHXQ5iDhOzq72hQBPbv0GBs_FcPsZL_AFH7serlPKMkTyWuDws8L5-p2Fa8CMeSQQHw7X6dK5ziWKDNYEPpr5KRRGdg0vOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=D8a5GLdpUfOkdMG_3FRp7W92p_JRPV7vE23uGUnXcRBazmJzVvEInpitTIm5GFENIRiwBc8FHWEf6-SZnpU7KdqPypscIdqDcQLVudSQzeVrUA5slanDv4rTVyKS_6UVne60cXz_1xMS6iCglUTTGMze_SHeh-fTgGfOAqThpsijvglCh8UPXcwqRi3l5RtADQSrT7watIon-pD9CY39_L7-ClrK4l_RVBpsKTOsBivLy9dnkzL-rwSLHXQ5iDhOzq72hQBPbv0GBs_FcPsZL_AFH7serlPKMkTyWuDws8L5-p2Fa8CMeSQQHw7X6dK5ziWKDNYEPpr5KRRGdg0vOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=q3m84EgSAQOWHjzxNyGotj8wmkPoIZoaDCgJiP6xa8G48j-urCUIx2njk7pf7FTG1IR--PN8GI4QJy_8PUIlKtEsYI4AH_pzkUzayrLz51D3vhYRnC8JIxGPNRhq4JqEM0q9kSQhx-dRE1XSg6431gyhjTTKckvpMRsNxeAMzsZHZkcmB6zX7GExr6Sp9qPdDw-pSYMKgPI0bdZuAH8pJPsttlDoXZ7caTVfwBb0pHN3oqMsL5ASgsmUAAnD-Q1cAh5rVur0mlk61zfJp55cI3diFfh0YFsaJk0q8cKPdiivG2e9-3ta85OQ-1d30QAgjpDGT09ucQ9ftdlDschKQbcJjTOV_pkhjLPH4uq23erXoRfPK0IgQvfLrxlHFkMxYydxEcEOXwNxUFPR5nOo63_Foy1ZvorcZd6mbnLNe-hEomDbQirjr5wKNuP_mwsmyBO9zsoLXtLohoz5DzKBxNgEueQqGpUfi7n0zu9MeduFELjARiamdhBVFqGr-O3QNNXS6yo5d5G0X7IuX7HH1hTj6MSfSQt5pDDkqSB0fmf_vYJXwofnEKmXUf7szC1Es6gF1IqLD-cTjqp_PYjJEDteW-9dz6OnsTT9uHpeYfBHgaFBDGZUEp9Jgg8qf-G8Rc6KaY-O1fAmi3sKfjQTi5E2MJ4-gVEGVbGZcwiTtbM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=q3m84EgSAQOWHjzxNyGotj8wmkPoIZoaDCgJiP6xa8G48j-urCUIx2njk7pf7FTG1IR--PN8GI4QJy_8PUIlKtEsYI4AH_pzkUzayrLz51D3vhYRnC8JIxGPNRhq4JqEM0q9kSQhx-dRE1XSg6431gyhjTTKckvpMRsNxeAMzsZHZkcmB6zX7GExr6Sp9qPdDw-pSYMKgPI0bdZuAH8pJPsttlDoXZ7caTVfwBb0pHN3oqMsL5ASgsmUAAnD-Q1cAh5rVur0mlk61zfJp55cI3diFfh0YFsaJk0q8cKPdiivG2e9-3ta85OQ-1d30QAgjpDGT09ucQ9ftdlDschKQbcJjTOV_pkhjLPH4uq23erXoRfPK0IgQvfLrxlHFkMxYydxEcEOXwNxUFPR5nOo63_Foy1ZvorcZd6mbnLNe-hEomDbQirjr5wKNuP_mwsmyBO9zsoLXtLohoz5DzKBxNgEueQqGpUfi7n0zu9MeduFELjARiamdhBVFqGr-O3QNNXS6yo5d5G0X7IuX7HH1hTj6MSfSQt5pDDkqSB0fmf_vYJXwofnEKmXUf7szC1Es6gF1IqLD-cTjqp_PYjJEDteW-9dz6OnsTT9uHpeYfBHgaFBDGZUEp9Jgg8qf-G8Rc6KaY-O1fAmi3sKfjQTi5E2MJ4-gVEGVbGZcwiTtbM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=ip_FjGyw30ZZ6dZifOfteYW2x0V3JHSxccnuDy8OXS6SYDMIL1YQw-O71lRipJrzjPLIyEwUD2b6heQNYIRvmaPltKClRDl_8SvIgMDCD8qfxsrLt2fAVGbEJsM5LP5dWt9LTTFMllMWSqe3qI5xVbXORCgZ_gZFMh_OlXnInlzzd_6lQnV6eQ8o5akSRUCQg3fhe8w7rOti3TZHi2BAz_3_8BapWPRA268uQIv9UQtXf_7yNRCvdrn-ULYXWo_AkeYsqIvldTwo3PY4AsK6yLL5LMPsb7VmPqD09Y7RzijCL4y7A8GJPUP5jko24pdiCIiSU6x7AjC6vrVjd2sLQyUnF_GYYc_1DA0awiO9KMdpNqfmGrpNDg7w25Zg29LNl7CqSTJLyB7tS2Ch1FXmMiC4htYKXAqC2reOK5ZiCHc_6MCGmm3bWkfg5Z0H6mEg7jLM3kQMiqN7BqRJrY_dYpGO8t0sd1e9XsWbX_5bSwqQ85buPcN0y9iflmKGDRr5iGI5lcCYmk2CH6gQi-ImftE-bs7MsTPU4P6Ua5PBO1jj4hVWP3o4Ls8cUUyJ6UMnrXIhUs_VVUGIGsMywyqU5aC3hATYbcCtw54fi-_JxRYOJq-V16-9FZ1NhmTaP3wugPTo3DMEdSnx_e7NrU18FTVDrd1yOMGwaw8NSwnoaBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=ip_FjGyw30ZZ6dZifOfteYW2x0V3JHSxccnuDy8OXS6SYDMIL1YQw-O71lRipJrzjPLIyEwUD2b6heQNYIRvmaPltKClRDl_8SvIgMDCD8qfxsrLt2fAVGbEJsM5LP5dWt9LTTFMllMWSqe3qI5xVbXORCgZ_gZFMh_OlXnInlzzd_6lQnV6eQ8o5akSRUCQg3fhe8w7rOti3TZHi2BAz_3_8BapWPRA268uQIv9UQtXf_7yNRCvdrn-ULYXWo_AkeYsqIvldTwo3PY4AsK6yLL5LMPsb7VmPqD09Y7RzijCL4y7A8GJPUP5jko24pdiCIiSU6x7AjC6vrVjd2sLQyUnF_GYYc_1DA0awiO9KMdpNqfmGrpNDg7w25Zg29LNl7CqSTJLyB7tS2Ch1FXmMiC4htYKXAqC2reOK5ZiCHc_6MCGmm3bWkfg5Z0H6mEg7jLM3kQMiqN7BqRJrY_dYpGO8t0sd1e9XsWbX_5bSwqQ85buPcN0y9iflmKGDRr5iGI5lcCYmk2CH6gQi-ImftE-bs7MsTPU4P6Ua5PBO1jj4hVWP3o4Ls8cUUyJ6UMnrXIhUs_VVUGIGsMywyqU5aC3hATYbcCtw54fi-_JxRYOJq-V16-9FZ1NhmTaP3wugPTo3DMEdSnx_e7NrU18FTVDrd1yOMGwaw8NSwnoaBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=Rdbh5jp9WuVybQaKnTOF5dODVUpCntUjztyFQSemHyYcmk39uFcZ5AFDeOmMgrkIdpY1-09g20AtAJvc4o4czFhJvOI1YFoQlQyugCHxSS6pWkDRz9YSLy7nbxNDcs1jOkMsI1Wv3TI94lpZngcfmaGh63CK0hYxbWkRX_6HKDo9z3qMmxo1bh8Eo7iYpeywnJGNyXBg8szvajZjS2UlS9aGsI1xdfIrQAl1DoRR6E3cpCDc_m06t0XCMjqAC6lXQMwcXvIKSVRO1L5s7O1nEytT0WxKyKEC1qIB4sKP8p7ObB3bpoXq1Eq4Mu0s4qYumza0oeYI9J940ngI6DrJeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=Rdbh5jp9WuVybQaKnTOF5dODVUpCntUjztyFQSemHyYcmk39uFcZ5AFDeOmMgrkIdpY1-09g20AtAJvc4o4czFhJvOI1YFoQlQyugCHxSS6pWkDRz9YSLy7nbxNDcs1jOkMsI1Wv3TI94lpZngcfmaGh63CK0hYxbWkRX_6HKDo9z3qMmxo1bh8Eo7iYpeywnJGNyXBg8szvajZjS2UlS9aGsI1xdfIrQAl1DoRR6E3cpCDc_m06t0XCMjqAC6lXQMwcXvIKSVRO1L5s7O1nEytT0WxKyKEC1qIB4sKP8p7ObB3bpoXq1Eq4Mu0s4qYumza0oeYI9J940ngI6DrJeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dahKW0wXjoBzb7IUGSl6dho8B8EINbXZ5cqTiluKu-RgEMCJgh4OtjX7EZnpfCjLPZVCrZkXjtbu6stT9hk70iQ-tLP07ME7ddplPCgkjCgekGydbLUSNzW2yv-rtRZ5LHPK13z9FwZVVT4XxVolhzWJ7pDct8Vx9IDSFuTiWDFM-e-JKYT1BxuYz0TL10vLyyGsWx76yedFUsmMV8i_IAxDjmykqGRzFUtvaDy_-vabsa6aj-4T0tQpL1pjhdPUo2Tu4cgtloCVDxyPboFHxc1Q7sBq0iyKV3fm-TtMgkZ1DfR0xFsMBofnlvI_e0fg10GcswhJxPg0zm_SZkmhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhdfZn1vh58UHrLm8lfZkD-_V63xgH9zFbwZcNC0IT3WwiMAY-AIJyX2Y1XjhYJiroY0hzg_ntpHK1FTJtZ91F4TlAV8ZGtTJEfeWRtuEbMKVa3LD_-TUgNWR3ZWb92l583-5eyQiCGxzAgLxhFbXhOD5Eg691yQBOd7PmA1Y0l-iUXJB4UPPVEon3AH83c5Ow9-bejISwD2ksN5yOTc1Y5TLtzt-pbm-xKeZlSm0mucpaAvVC9TuZNeCoyubLxQsEmqCEQqnyGLprpwq1bd_VEINLAhBBqfHL0gcG46ldTmNlkYn4OiptaqRUJ0QuYl-Mk3OBVoJ8x3uu59RG9Uew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=JDAf80GfVsqBGPCHQvvkoBPMrsQM2vVANTTcl5anBnyar9EW40HPCdd59eg6j7K4QTC3AQ5n5P2RsivFEgr0H5umkNy6TRLekCPfo1N69iB5tTxbwLNCa75W9AD4L__1Lws5_3UBzfnwQlFRJmH4Sx94k_RskQt2uC2709HyKRyEtHQwwRNA0rIas0eiWo9VcSukTP7awb7rnZY2CYWbT9iB8i55lf0YAI6HAOQ4xOKMzkjNECnwjgheQUiLWH-mxm78cftV5px0xCMllBZAOtAlWqKSkf6MYyLMZxt33f0BJhEu-f-8t21zsIE8IaCuqNcPxZ4z9UBdCkQn4TVt1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=JDAf80GfVsqBGPCHQvvkoBPMrsQM2vVANTTcl5anBnyar9EW40HPCdd59eg6j7K4QTC3AQ5n5P2RsivFEgr0H5umkNy6TRLekCPfo1N69iB5tTxbwLNCa75W9AD4L__1Lws5_3UBzfnwQlFRJmH4Sx94k_RskQt2uC2709HyKRyEtHQwwRNA0rIas0eiWo9VcSukTP7awb7rnZY2CYWbT9iB8i55lf0YAI6HAOQ4xOKMzkjNECnwjgheQUiLWH-mxm78cftV5px0xCMllBZAOtAlWqKSkf6MYyLMZxt33f0BJhEu-f-8t21zsIE8IaCuqNcPxZ4z9UBdCkQn4TVt1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0ogAm1VWZYxX8epuOvnSY3NOWIypcelOK-NJmhP_u0O7bEl7Wm1U5UWx5SnXR18g0jKUJMUu5NakQH8_sX2rVC26crNb3YjCUoqjRPz1QucG0bBSjFBtd5LBQhXUCcxcTTS6Dmt11vUAXY8x9vw9Yon6428QHN7GWsMRfPF8daBseiogJNJ7Q2zet8wReyLNin1-1DIvlayfTlcfZfAGq7ajW6Linn2SoCzPz4EVCTxx8qpBk4hMZbgTClTBJUTrGga3kjKwndpNj8mpFyI7AJbdc3UPjV2vWf1lBLIWYNT1IXVfz8O8rnQcKNGrCeSu8lNt0HqMSzDeTGZ94q-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGjz_08JDImxL9NPtQQFdK44ksvR0v-G8W8I86TsP9zqZvNpJ3jYnm9ywi6MyeQQ3wftUjrBwnEaplhHDjDkepmS-SkFDIM8iB0-dZ8lvsVRjH4WNHLLrYWVUVwCwPzQG5A-tNX_UpBv1j76fZ6r2RWiSsG18_X5517l5NQYvDnc7fx9vp2aDgYl6n-Ya94w5BAZA9s68jshdrETwLCU58jAeyxsbL1WwPG67d2URLD-yrw19vM6Ax1jrlXmFoG9JBp4FdCGMKmWGnox1CZDGj7xhT4wFJvrpVfOWDCL2-XEZjNUzkqcN0ufQnCKcuZkge21QyyJz89WkE6vtZfMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfPZl_UIVpAaQwEYJwNw6-LzNC7GQT0JpRXMbRyEZl9d0Ivfwvo-iZrT06Cf26w-2eD0Fo1eZJKin2n31DO0jVyGZ3jRf8tk5Y-3d1nG6vy1V7r2udzCEUX_MUDfZoP8tX9Wz0oExpylTN4iB8H2UTNT_lTeFyMOvVQm3LFXmGlksTHyEIzdkFIOA8WRZBFdKaxjJmQm7yBgN6Ej6Ps0I_usympFlihZkS6Hx5UwTQ-U14NgCsygdIhQd83lPUNjalrZdl_fgDgtowD3do-FkKRYvMdcu-CbBsOjj1h2rgSYGguuT1Pxx2qn3dF8PeaP5sJ1QmQ0xRvK9tgPekTrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQ33eMYPhGn7V2fuWMMMiNHHEi2Mvf17pCsqmpS-JrVq3YhhP_FnjvMdKncYXdR_79Zh3GMbKxlRbLoDxPuSDsnRQ1ZtNby0gmRQyWNmujc8aOZhZRLWvFrzUkR1IgeKmDKZIIMRIn-mawufUAT-jPsDYIKLkuqfiEqAyX4YSWxKb5--4vihMcCwndeRO84dkfC5oZwatpapIZRmjqHPMgHAnExdJRoGzIN1zzwxTYqi4dQeyG72GTGwtr7KhsvKTlTI7xbOVCYTA7Nf-ewjiEazOTvl4FhvEGXkTfRa2UzFnfZJV0tPDt5G-cAhBaw69Co5tTDu2gGUMs8Hs2hicw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EQOova1yluilZtP9JY-O4NIQ72SJek6f4QopdbXFLcHKl7vTeCNo5R_yKWQHytgGDEPjhnWj3MYlBPcZgyB-J0z6Oto5Yl4IKa0kEnONUkebDfJiPpX1_wipnf_ytad3Swo8RZTAG-NM36QI8NbS1lRu7mNIRPSiA-zw_IJrM8JwAW0UT01BSoaiUMaCt3BMW1fXnhuf25ApzJg5s69yXJsLVlnBUKmRY2Zv69ubnV626UoxCgcO6mL580T5TStS8Egk4CurMnTuW-08vJmIy5HyJh24v3VC-0lt8sHTM-pIeF8u7aY-a9Eph_9Kc3yLluzy6qmWQpUPSKAxcjqzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXykCPw51hgwYEx2VgnxXUjbBS2fMflF1QSsFLmVNh9IQmrAGg_zed9V__jc3gjM36Aor1QtTmzjt0qnpquEzR8faujxxiXQJHQoideh8DJz269Lolwp6VOBJJnsoQVf1NM3K_otZ2eDE2wJVr_AVBff_apqWf8aRwxtqTM205IRjmqswTs5KbHFEiMnSTMXeElXOytND4MGKr_Zpn1LIOfNau_Lidr9BDL9UiJ12sc4vNsm5DmZs9mOIUfp96qqZIQPZZdQ4_ogzRpyaeN_HyLFrOUyo1whMENkgjGIOtNoafX08mRbSBkXUd9ara1B2y2TymGCmKQ5wattIkOp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0HQrAbwDfbyD21KiQYDd7w7bn1u2SOYBG8zn5l8Ab0rzvphwq7KotuUh4_7B9tmb92jwzU9FH1qqZzwHop0XK9H339_vh7y3gqa4rILvDBcNl3r0WQAixontiSGHKGfsjFfdb3TNgRnuWgkxaChr37qubACVXJRJ3OmvlLLXKW0iPH5O-A_dThPwH-f6GKOZdGrf_9es-pYsyQlaEtLv46w19drbVIurspRmcbtk6l4RzHU9EwFIIcxoeXfueedR3desj_tATisHMizK2BbfBMPrnnlYzIFmBFDjl7Sp_C4HKkCLTPJubHFkevVO1gjnMDwsSg_a2DzNhvfpPlRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vn-WrzCThJpSoy48tzRMz6QfEnCqlR_pY-nL3mTCcfX2XG0GjBdkczlb1SLXbGqsqgbwelHtSG5M-IF_whH73T1WdOyt_JWt4RnQ77PXBdvAMVIdFs9VT-9l68mjswUtctQbtb1SRLpbOQHhUgtTvsZWZ2mtd6mU5axxKrswy0z_uWOvDCMvqprr_bq1ziABQGsHmHJShxMD478tMknQvEL1F3bBAlhQ1RdyjVtnYngHrlBHm1tCmEZhtPkFsoCD1FqZSFXkF1KpUbXbxyXsp0cfuYAEzNIoqDcNCBgzWeSIw0d28YpV50FdQbpPpoclB1DkfRsjEv4GiRlusDBY1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1fN7PMP1F76UoQaWt1OOAylOLL34ynKmK6iod7uXOkFTKgKQr_jVovj2_6yQ22PGIvfmt1lNo46EklsmuEBdDDvYXVJAtAaP22FlBAkUUcEbS4aZ9KUGFtIoHR5i8ekkSxtRM86PH0ccBw0ixhcta7e5-2y56_YXalB-BS_VtwzL7Rw7rt799v3marFWMaZisLNGFkx29yDz3hlClyyA2aefUKb3zyr0H5HmY6Zoo4YmyiCng3BADfTOlAqJN_WqR5s3TDkQEblNweMKH-Kh5Ef6WCfp2gbyDRmrMjM4_H8ZJwIvgcHonrt2B3S9Rxt0jjRHj6r-ElSJV_eqfN5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlA78MST5c9l5PTHu9hSuGgwEy4VMs4rxH9nCNd1y6Z3SBfFrGC2l1X1UiBp0aC8-fMZy8R3AeNNA33ZOC6EyzIabloJi1NgQV0LFZD_Hb2ahLSlCAGDuF0QwCHoUMvN3fcpC7G3KFB1J03iHmavT52Cf1y2ombMb4VsMCOYnFHhaimO2U8QQljuapQCblqZRmNy2vJ-KfTlYEvtyiyQPmUj0rpSDu_AToe55VWMVRkxhtwrne-wrc9zuCwFvVmD_nkhrDeKw6jGh0-1C8RulEBDecT5zNG045jcidsNsYu4edu8O5yeeCJTrIqG0z7Vj8bQqydrhBDwDHUD6G21FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKEeUeKQwp2KZq2DLgDlXjO3xOuQnOPn6Ya8bB8Fs52RumF4JTF8dci4yJ1XdFOjCyeUFdK2QK-Bm4ziaBlTaQy-5j8kJj-5xVB6ekBYz8AxPCX1s1XmCXd__92qk5ksV58miUApYkuFeXRJ7rviLsTtemH6Lm_VtpqsG_oZfQx1tAZedqpAjSu1wnRZTOTEYxIfLNZXn01kdHxHSJK2GUOJcx_bmHG1NQMO90OfYwYETnfiuBuGn0yl0nVABJh5qDFFeCVzSUjrKqpYI0XFp2Z1T_RX28VEGIaubsozOVuMJIMF1BimTM00rOpIakTFoGOmKxcad6zCNYMUYL_Kig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=pg3oUEOq9uHhIwb1sylsDwz8e4bYvNakmNQbQN2kbcYzVquGx-ZebWlSJVsvXI4unloMRQbnulklDhscnkhq6NvQCuoxCmtFZl_ufhF3qP2WPHPQIOnHjNYWwDWDSS2dxg1fJCEf3nkYPsGxER8AQIEFMIb-DO-tawoNVM0Ep6geEYH0xrZ9tEbvFGX1Eo1To3r6zn5Nhx0ItIbcmXllLl1A77QIfnyT8oNuBMNBEXLg18vQZowhB9n90HiuI5Fn9Ab0r2hvd6qaA1Ey5Rs8n8MtwbS7tq50xJUDV7Z5KOOb1GPKsMv2acbOYMJJpbUlKdQsdQ9T9_FTxB5o5RDgvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=pg3oUEOq9uHhIwb1sylsDwz8e4bYvNakmNQbQN2kbcYzVquGx-ZebWlSJVsvXI4unloMRQbnulklDhscnkhq6NvQCuoxCmtFZl_ufhF3qP2WPHPQIOnHjNYWwDWDSS2dxg1fJCEf3nkYPsGxER8AQIEFMIb-DO-tawoNVM0Ep6geEYH0xrZ9tEbvFGX1Eo1To3r6zn5Nhx0ItIbcmXllLl1A77QIfnyT8oNuBMNBEXLg18vQZowhB9n90HiuI5Fn9Ab0r2hvd6qaA1Ey5Rs8n8MtwbS7tq50xJUDV7Z5KOOb1GPKsMv2acbOYMJJpbUlKdQsdQ9T9_FTxB5o5RDgvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=urVxZorgIXkaWHrI5zVG1jL9B4TUOObxju-5dyxzT6DrdAtNNU28J4tzmkAlvdpT103NKMNgBtNsIDY0MkoV9kBdFHucFoTay3buU7Uq38Cxk3I2AfJGDMjWubXDXYEhJOClEJ5GiLuGYgPvVBHzaqxSaS7_-zhSTxXD8hXbQb0aEyFk_HTHLsNKH6albSJRBWyZopaEn7lHUCwXpzOfEVv1nKYWziQ0vjJZK9r-jyWqLv0nC5Rg4oLD9t3L3wa6lcrP_T9hRynp5aqa56maqFYzkHaqAiKEDePNlrNAZtjk_8yCOJwiR0AXbQG7cqE5lnNronsLg9qf_k-wy0faAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=urVxZorgIXkaWHrI5zVG1jL9B4TUOObxju-5dyxzT6DrdAtNNU28J4tzmkAlvdpT103NKMNgBtNsIDY0MkoV9kBdFHucFoTay3buU7Uq38Cxk3I2AfJGDMjWubXDXYEhJOClEJ5GiLuGYgPvVBHzaqxSaS7_-zhSTxXD8hXbQb0aEyFk_HTHLsNKH6albSJRBWyZopaEn7lHUCwXpzOfEVv1nKYWziQ0vjJZK9r-jyWqLv0nC5Rg4oLD9t3L3wa6lcrP_T9hRynp5aqa56maqFYzkHaqAiKEDePNlrNAZtjk_8yCOJwiR0AXbQG7cqE5lnNronsLg9qf_k-wy0faAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=h0bjuF19DH0j5ZVZmv6bGzbhTMQbD-bJzm_Ti5HTiH4MUI8pxXNJMPduVXc0og1QIWMGqq0912KS2lzyh7xCrY2f1SYa-DXKFFt75pjBH7Zxbpzh2p4vhNUPn0Sma09k3nog84JsWs08RzdxJ5gZe7BVlwDUR_EUriyJbshTDJ2xerLsRtudsKICizb9fnVssat-V8UKCB8IBOUucywrrC6HW2KafhPxFnPoE-u_9KW9OEsufBAB81fXqwyoHnTcHB84cP0UfdmZILyp1WLECiDxXMPYWVS1bSN0GHtuCI_52cl1OoS0Jnze_yEVVexOcw1R9p5QxQ_I4cCG1KQoDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=h0bjuF19DH0j5ZVZmv6bGzbhTMQbD-bJzm_Ti5HTiH4MUI8pxXNJMPduVXc0og1QIWMGqq0912KS2lzyh7xCrY2f1SYa-DXKFFt75pjBH7Zxbpzh2p4vhNUPn0Sma09k3nog84JsWs08RzdxJ5gZe7BVlwDUR_EUriyJbshTDJ2xerLsRtudsKICizb9fnVssat-V8UKCB8IBOUucywrrC6HW2KafhPxFnPoE-u_9KW9OEsufBAB81fXqwyoHnTcHB84cP0UfdmZILyp1WLECiDxXMPYWVS1bSN0GHtuCI_52cl1OoS0Jnze_yEVVexOcw1R9p5QxQ_I4cCG1KQoDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=U4BfC6a3-Si0IZYU6jNEUn0UkKiERpVVth-8FuyRkaAJmJrbMzW95YhPNw_DhnMoU3Cfh2ReZjIFvHGbemfmIxclKhlVrymyH_lUUmIJgvE1atvQjBRj6PF5VnIzO1LMhPJXFODqf8pQH55WW-vyMvQY67R0rrK4zck-ZHcS5aA6HavbvQ6F9La5xsSRbdWujgk_tW33eWb30OVNfkOrFauGXP1SAyb8mV7Aas-Zu92BaQYUD7d1pOWQWsKeGKRf7glY-dbQ-9d-aeHBhodBWKvp-Ry3mMQUgfg_Y__09nJ7HwCr0FOYtaV_ygaHdnO_5LTgT-QDeZetdG4a68CX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=U4BfC6a3-Si0IZYU6jNEUn0UkKiERpVVth-8FuyRkaAJmJrbMzW95YhPNw_DhnMoU3Cfh2ReZjIFvHGbemfmIxclKhlVrymyH_lUUmIJgvE1atvQjBRj6PF5VnIzO1LMhPJXFODqf8pQH55WW-vyMvQY67R0rrK4zck-ZHcS5aA6HavbvQ6F9La5xsSRbdWujgk_tW33eWb30OVNfkOrFauGXP1SAyb8mV7Aas-Zu92BaQYUD7d1pOWQWsKeGKRf7glY-dbQ-9d-aeHBhodBWKvp-Ry3mMQUgfg_Y__09nJ7HwCr0FOYtaV_ygaHdnO_5LTgT-QDeZetdG4a68CX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k-2iaXC_epFCM3o3hGZRGq79SvuZkeNnRr90_8-L2ashGR8qY8nO32SEbCdJ6g3A_xR0FFkYxPkuppEeSE2PiOpQBa9dQf6TjOww7vVXB_zQIe3IoAgyZUI7xPnqHrm4AMwmCgtXoX61A-2zEvIibX9Mjdip0RaWn29gJM02GrLQXKI-APhAyZt-rG8Hr46s_D11uKsPW6tIy0JNtGMdRN_3DJzNQe0EnsF09gcOFoy7xwd-rlQGrc9LPHGCTpytcS-wqWjt4TlKfbBQjFXWtT3Esm6xgWJOeWw4kpljHUHlM2s8_zOrh2nFrevNRhU4oIFHjSzD3EwTYT8IW0nVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpCy8kmUHNZEzljhex0yRIT8Fva85pclxC8CSqINCnTeEs8ropRDOU8epEu012jywOGylRHrrtnr21ic0YU6QpSX7jCM3O4_0PpQqH_dzENVk7dP_rbMtXeieABkCrXo187Cq0ofcKJu2acmn7iN8lRnaPmda0KNnxc6T79UTRQW0YdoWLy-gdWaO-CSONJ6uVUB1Y6e9EWVnuJ-wi9OUz97VX8Bq0FNBGY-shNsHykZtI2c5oTnPvindNcf0Lqb0smT4m1MWCYe9wx66bSOyB8p0HJP7dPtj_oK06UDY3t_nZLfoz4XvWV8RzZ9vI6g6XC7UpqBAi1M7hO1fi0bkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJflZhSVUKdT4Ezou04XFycWVUFDjcI-mz4xlp5rIq59MYjuCba6FiSVQ7jUcSswO9bgSSlU_mvjXwfTh0GbadrVMWwGEeObH3vCGQx3cWKdzXZ4abZEgqe9QqeJY7oBlYVG3_hhqBdYfstmYqfk6FXm50PhHHS7VHmMuFYwMrOSJvjCopETXbMMfI0Ch9DMSljvtPE_4pvq4d1iFukSGjLdFw4DqRZXmYKF6cIMJWxhhWUbNzNM-XG-xQYwWrc8-KrlLrXEFvosizWghZi99FILI7deIsZ1cQIl13KUBSPmGGhLHHVGsBjtWneipDv9rb710QnJwl_TkaBMqmC99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=FXhn0qocL8UuTQR-H74SmGaeExiYhdRyuR3lYJncGVNtqJatRxPswT3swJFcQrEcOXotazDULmcQIF-urrrIe4dTnaJAIJ1KWkxN0TfUcGS33BnoOSPr0LQA0dMaqM1YM6bVJTAENBvAA9C0vbvRqPH0tk0d4fIcBK9iDaW5aQGYKjij0zsw5KpKT-kl3FSZVIOJj72_P3wFKpX0Wu6RVFb_7kULBPFcbmvTLt-_JERo6qrD74FqV4the8TXMcqaChserVLu13dLcKzWXIJJEPOFezLiVQjh74P7RieEwfLrQgoDLZjcK2WqwQ-sCXHkefqQTMCc-ARf06J-HgXRBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=FXhn0qocL8UuTQR-H74SmGaeExiYhdRyuR3lYJncGVNtqJatRxPswT3swJFcQrEcOXotazDULmcQIF-urrrIe4dTnaJAIJ1KWkxN0TfUcGS33BnoOSPr0LQA0dMaqM1YM6bVJTAENBvAA9C0vbvRqPH0tk0d4fIcBK9iDaW5aQGYKjij0zsw5KpKT-kl3FSZVIOJj72_P3wFKpX0Wu6RVFb_7kULBPFcbmvTLt-_JERo6qrD74FqV4the8TXMcqaChserVLu13dLcKzWXIJJEPOFezLiVQjh74P7RieEwfLrQgoDLZjcK2WqwQ-sCXHkefqQTMCc-ARf06J-HgXRBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKNkbZZyXe1o4Y2hO-bPHr44F31WATb2jLOJj-iNUeExBhkhERlGH_53CCOcbE3LrK4VlF_QU83qA1IFlGq51tBRS_k53pvsOODAKXn8Bzz-od1g-GoqFLhn4Bs8LxsAZiho-LXO1VQCoYmVTm3oyDE1rLF9-9SZpXOT21RBTVgedQ1sdogumGYRsAW9VVYtH0TDalmB2QfXPWzHnhA00j8rlgePYZCPRCES-wmXErtZTPW2BZcSLGZu8E1RhHz_a3k3BrKAshqbntM-MLQDm5EVdcT2Hr71_7rDdvrRIA0oOZCzI_uW9ERJ6A0Ey5bN-b4hWmi0RxtxFHP6gkj96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=nEiyWabWBWNoCnfnxOiduoQYLm4QvSKxezl0Z-zprWySm29vLaQsLmIOojplI3MTBFDjIE-3sYiNB4KApXMye2BsCUXPBVeA0osBDyhl2JFbp9u-xl5wbi0hCB8mcZPkc9eyv03yH9M9XnNDl9X7iPUzvdudFX74DDNhrQTmBRq9-_P5ul8p2EhMZBXS_rlNfWJDoDCaPnk-YlloZlmzK2hyQi0kJ3uUUNkSPOel04VCW3_axMdH7qbpvOYh37BKlmEE4--Jq_roxwgKtG38d9XbSjGYDyz1yWlG9X-7WRaTNuNaNpE3Vadyc6Pq8DYhaDUVVkSm3Uumu7iUY7zwTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=nEiyWabWBWNoCnfnxOiduoQYLm4QvSKxezl0Z-zprWySm29vLaQsLmIOojplI3MTBFDjIE-3sYiNB4KApXMye2BsCUXPBVeA0osBDyhl2JFbp9u-xl5wbi0hCB8mcZPkc9eyv03yH9M9XnNDl9X7iPUzvdudFX74DDNhrQTmBRq9-_P5ul8p2EhMZBXS_rlNfWJDoDCaPnk-YlloZlmzK2hyQi0kJ3uUUNkSPOel04VCW3_axMdH7qbpvOYh37BKlmEE4--Jq_roxwgKtG38d9XbSjGYDyz1yWlG9X-7WRaTNuNaNpE3Vadyc6Pq8DYhaDUVVkSm3Uumu7iUY7zwTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=JioNunTOH4JT2HmXpVGBHXcg1iZw1Q4lm8t2ZYslJzPSp44ZUtyKSDRDtHbTM5vj5zTBG3XJHvoDBXfxgXEuMljG19cZdHyzQYCxnwdZJ0gBRgXpfbRsNMYAx7s0ZioqeqeLNMBVFzeKNLvkjkz1bpI7pkGCHKySoQrR1ww4GbrIagx3O7fNA3drl3vOXFEZk5hW_dhITEPsdz0_KGMb5e0DfknQX0QEG1BgSprQD2C0QCfsO8-SSPMGOZyOf9SIaa8kybUwzVUfdj4inW18AC19y6M6qG5-lsi2f-ZdU5eVRnrPQ50d0jUvMJGSybQBrsbbmBYADpx5cuSk7FE5bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=JioNunTOH4JT2HmXpVGBHXcg1iZw1Q4lm8t2ZYslJzPSp44ZUtyKSDRDtHbTM5vj5zTBG3XJHvoDBXfxgXEuMljG19cZdHyzQYCxnwdZJ0gBRgXpfbRsNMYAx7s0ZioqeqeLNMBVFzeKNLvkjkz1bpI7pkGCHKySoQrR1ww4GbrIagx3O7fNA3drl3vOXFEZk5hW_dhITEPsdz0_KGMb5e0DfknQX0QEG1BgSprQD2C0QCfsO8-SSPMGOZyOf9SIaa8kybUwzVUfdj4inW18AC19y6M6qG5-lsi2f-ZdU5eVRnrPQ50d0jUvMJGSybQBrsbbmBYADpx5cuSk7FE5bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=VapV53XTOg1L6CBJrGbcFFKsDEPL5MFMdFjKtVocqOApU2ODE7Wf6fMRrfNHbvwmJ6Vgeqwpl2ylXpSzNiw_gkzTe4_a1Vr7i4mYSFbw1EtFzkEh3wY27M4KIq8nsWKMh5WpMNw_JRfT06mWOF5-SQyGhGX0BkEFNKpv5VtiI_4bSl-3InhHtXNcP-i1fkVqFroAxdywtmVz9Qasids7dZhmQkeKWfRb8MfekGFY5yawDAOZzVp1oKmvMJxsI68z461K-RQ2qdoVsKKyh9Ol4fxQxh7XwaSLYb92qAUFLRGUqESVGEe3D56EvPxlRG79XoAzeZbYJZ5hUqpljicZfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=VapV53XTOg1L6CBJrGbcFFKsDEPL5MFMdFjKtVocqOApU2ODE7Wf6fMRrfNHbvwmJ6Vgeqwpl2ylXpSzNiw_gkzTe4_a1Vr7i4mYSFbw1EtFzkEh3wY27M4KIq8nsWKMh5WpMNw_JRfT06mWOF5-SQyGhGX0BkEFNKpv5VtiI_4bSl-3InhHtXNcP-i1fkVqFroAxdywtmVz9Qasids7dZhmQkeKWfRb8MfekGFY5yawDAOZzVp1oKmvMJxsI68z461K-RQ2qdoVsKKyh9Ol4fxQxh7XwaSLYb92qAUFLRGUqESVGEe3D56EvPxlRG79XoAzeZbYJZ5hUqpljicZfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_O-qowJismsChDUnxNgi3wN6TAsyExY__TBWl-MIi7uuc5iy6W4HB1pgHu6jC5fOdRBfXB3WTgWnjlfwzRYhToWNxg8-ifufGi4CgFcKKWqvFqS_1X3DZ1vyv__JHTBFJaZVfmuTRKb0CVlsWzlehjuIXySifQORV2CW10Q_uOqanGOXQRLxUH9ZXtr9eLD8LHEGysUQZm6T8lTP9zHxiozz8X5ht9uqfH_76R1GABjgF1fh6_FUNdiMTqv1ic2dz14zHz8eP9PoJ2ve54ba0fsKIOQO1pX4OjLStjION8EjwOT-wX-PgU0wCb73PbArjqEb7FHngZMd2nA1hpU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=adet6CYKKcflPm6BaLiDGt8S5ObyGUgsdUl8cPw9LW5Hx3Ezfcio2Tafwj9DAgghLKcyBGeoyqPpZ5ZANE-eXj1Z8j2D8DCyKIJ4tBh3pSL1LcPMp22-teFC-8wDFrWxi32L03sK-rN3vmbP_E5noltbiy_ciph9koTSwfqs0LaW4SaRJL36ss9L2iQ9sqGTrma6JiM4-SzrrMGv5Hgq2OqcwSrtoMbHIISicdPwUQP5JQDMLtmIWU6PvaNXOH6J1GrBYolzUrSaKowxSZ9oxPJNggN4uqIcReHADMAnI9IUWwAhvlYGGfFLx-YEtiVJUePf5yLcPOV6nSZF4I8Fmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=adet6CYKKcflPm6BaLiDGt8S5ObyGUgsdUl8cPw9LW5Hx3Ezfcio2Tafwj9DAgghLKcyBGeoyqPpZ5ZANE-eXj1Z8j2D8DCyKIJ4tBh3pSL1LcPMp22-teFC-8wDFrWxi32L03sK-rN3vmbP_E5noltbiy_ciph9koTSwfqs0LaW4SaRJL36ss9L2iQ9sqGTrma6JiM4-SzrrMGv5Hgq2OqcwSrtoMbHIISicdPwUQP5JQDMLtmIWU6PvaNXOH6J1GrBYolzUrSaKowxSZ9oxPJNggN4uqIcReHADMAnI9IUWwAhvlYGGfFLx-YEtiVJUePf5yLcPOV6nSZF4I8Fmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNSUhkITuIPfWSAPH9MljOw265s4PTNSOjHpftjD0yuReShm-E_7f9IV8zjt1g9u2nFQbsoaiWSVKUouXCWBPnZxPLwrmEpOXkZtKDJ0NCTCKdhDD8tHKBtHqWY7escMpU8siyFgvn_GqUyuw1EK_0Aq9Yx1DNruO6xBCT9w_jdObLBR5Y8rlsXure8LlvJe1li2uFlDB6S6uBS4d5qJtR-cK-E3pADRwu27MCIz9bF6RNWPXpYWoTerXABcC3rH_8y1nJNygVYuFbTELralJRskiAIzRcgm8vRjuQQQpoULqe8d4EnhDP_B-brjCtaobawEVpu68TlWUerUw2eRqGNj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNSUhkITuIPfWSAPH9MljOw265s4PTNSOjHpftjD0yuReShm-E_7f9IV8zjt1g9u2nFQbsoaiWSVKUouXCWBPnZxPLwrmEpOXkZtKDJ0NCTCKdhDD8tHKBtHqWY7escMpU8siyFgvn_GqUyuw1EK_0Aq9Yx1DNruO6xBCT9w_jdObLBR5Y8rlsXure8LlvJe1li2uFlDB6S6uBS4d5qJtR-cK-E3pADRwu27MCIz9bF6RNWPXpYWoTerXABcC3rH_8y1nJNygVYuFbTELralJRskiAIzRcgm8vRjuQQQpoULqe8d4EnhDP_B-brjCtaobawEVpu68TlWUerUw2eRqGNj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-nnEj3b0_9e2n3fxTDcLNzwkBJ5VYHgqEXY3xIxsSXbPdQs9kqSfNOeGvyDJ_LVl3kpHiUBB0or3PWiKX1b1lNrwQpYUxKJaHysZIECqfHkIrdfHi9R9axnlPNZeBZjpQ_GgGRBz5_XYLW8jnk6jRX4wzh5jTf_CqY__nk2OAPzIBAB0neKqnw60vzkaw18AxGaHfUSsskDQe3KqWl-vKuVzRtPHN1Ad9mz7hznugsSmyUut5-diDAGpEouy07ZsTrSYbs00qzItBwyX8Hur2bybDm3aDYDoSGnj4kBMjusDNe1MZjEeP1gMGhDWD1ALYYqQQyXZ61tpBlBXK45ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=vGMbz-W_5xh8EdBVnC8PZaHMLab-4QgQ9eHQyZYjIvkR-Py6KRmVvah1HCW1sgw_Farv3K1YL1BWqQtS5UXjsl_a8_-jVwnI31g7WsZ1o3pRddwcG_TBYu2_qBkU9vwLMD90xfUozUzuHYTA9iRj6sXllX36ylJ3-nA9iPFrN-HCKn2C6sd6-JUt-MGB5QlsDUnsOX5MldTmVG4NN68EJKj2sgbi-n-1ipIntcH-ql96OcT927qngdQ8mmyoNU7HaqvuLVVkvMn3EIvn6w3UYNr3TyRxfHn0CIWiDs-QOBvkJIjMD3WuxhVmZ305rOWvTmrfxXPutO-nAINJue7rMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=vGMbz-W_5xh8EdBVnC8PZaHMLab-4QgQ9eHQyZYjIvkR-Py6KRmVvah1HCW1sgw_Farv3K1YL1BWqQtS5UXjsl_a8_-jVwnI31g7WsZ1o3pRddwcG_TBYu2_qBkU9vwLMD90xfUozUzuHYTA9iRj6sXllX36ylJ3-nA9iPFrN-HCKn2C6sd6-JUt-MGB5QlsDUnsOX5MldTmVG4NN68EJKj2sgbi-n-1ipIntcH-ql96OcT927qngdQ8mmyoNU7HaqvuLVVkvMn3EIvn6w3UYNr3TyRxfHn0CIWiDs-QOBvkJIjMD3WuxhVmZ305rOWvTmrfxXPutO-nAINJue7rMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqLuUtYOgXhlKsF5O3_919MYJA4QzHcPGo0oBd8bNhPUbcS0wMhSfp5n3KAuNWXLuazg0vOSUd4n9yGnSZkuEKstieV2p18ZM9oR1VIVBQnqcvSekyN8OY6wkNQd-Z5Tp6LEHIJcHR96DNQezrAchU28JKSdAyneKggcqLJogM6nQJ-oWWt7a7LiTKDuCgo-Sk_B3N7c03MfG567XZqJ4TlvfupoSUx2pPVE6PdXo0Q7KNipEVIULnY7CZ8AZEpOVw3N98FcGCNgc20I0ZQaZ8P-eQPSCGcrIXpGO3lmtw37sKeSa_g2HkxQRCoiANnqOupTYlbgFaA178yluRi6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=heFEP7YqSuUgkMJExj0VTRxd7Tzd5sEEpsi74h6JmQqly5ve_r62UQkMebnlTpDDUy_pddg6jF2JV6fo5v9ajAKO0Tiwrw4AHzQtZcksj9v6rA3-7J9hNa9Lyk0-ETGBmnv7Fp09uLI02vVtmUg1B2dEAILM4_e7Zu0YE0IGOftlfXSe5k3HiCaUTUWu6u1Bb50q-BiE4BtCDQzhkNsV5npFshOmzagh5HeoK_FI6LeZDD21zr4AShU939ddSrsHoyah4HEB8gVyhYmMeUGXObIHB78vBVZsLHAchfO5g9-Bh1RtylcWzqLaz3nnh25QUle6nTwtXOZ6-ZIFF9tDoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=heFEP7YqSuUgkMJExj0VTRxd7Tzd5sEEpsi74h6JmQqly5ve_r62UQkMebnlTpDDUy_pddg6jF2JV6fo5v9ajAKO0Tiwrw4AHzQtZcksj9v6rA3-7J9hNa9Lyk0-ETGBmnv7Fp09uLI02vVtmUg1B2dEAILM4_e7Zu0YE0IGOftlfXSe5k3HiCaUTUWu6u1Bb50q-BiE4BtCDQzhkNsV5npFshOmzagh5HeoK_FI6LeZDD21zr4AShU939ddSrsHoyah4HEB8gVyhYmMeUGXObIHB78vBVZsLHAchfO5g9-Bh1RtylcWzqLaz3nnh25QUle6nTwtXOZ6-ZIFF9tDoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=UiJEJrMxrxj9ev7nK35e9XIPYgUm7xWsn61eltvBCa6xawWPcARH8oaqihACWN6e3s3qs6wVNvTLcHiayGACp1EnJ3tDWYajoh5EaVay-FOTX5zOVMaAAwTVuEhYP8A1I7Adzvy5Igkt2VOkn7BbtEPyd-wssqUC1L-_-Q02hGK7itBfpg9HVDCEUpyEWjHBSfVmMMNIJUgarmuiGh98_-DXqYrWkqitQs52M-bnCft3ee8JR53BnFzo75RZrXilhZ-9ACML6HmESCENIsEsbAX1gZn2bYdxfqJ91wN7j0RWwPOeBxq2kupn_ICJK2k7f2nPEUq9LeFnw3_MJxtKng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=UiJEJrMxrxj9ev7nK35e9XIPYgUm7xWsn61eltvBCa6xawWPcARH8oaqihACWN6e3s3qs6wVNvTLcHiayGACp1EnJ3tDWYajoh5EaVay-FOTX5zOVMaAAwTVuEhYP8A1I7Adzvy5Igkt2VOkn7BbtEPyd-wssqUC1L-_-Q02hGK7itBfpg9HVDCEUpyEWjHBSfVmMMNIJUgarmuiGh98_-DXqYrWkqitQs52M-bnCft3ee8JR53BnFzo75RZrXilhZ-9ACML6HmESCENIsEsbAX1gZn2bYdxfqJ91wN7j0RWwPOeBxq2kupn_ICJK2k7f2nPEUq9LeFnw3_MJxtKng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=QiTvxAezJmXIOnNAXPPrrDZxPL7fGJxVvDeFsx5toWV2EfFSDUwCPFU0wWLzM55CdHxahBBG0csOfN4eg9KFAbAAPlU5-BKzYm7JMiTvHQ_8nk0tFQCicbinRVYkmmGIQ0q5fjDSyTsWlJThmwj0DNCk1C4N9bQ5k9GpbXjjSFh-nw1SMofLp6iLnxQ5Ziwv-xLF81k2_wzBtoqZd-_ekUKGXFrMBh2rB4d5qntMxBRuIpAL_NKtXPeRNI5CmB7eyYGMnboSi8l5hlATFryOb6SsF32BK6ce2rq3AFaC3rOpB3wmYxvYtgj8_-TExJA1iVT1PTkuf3ocLGfp_cTTBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=QiTvxAezJmXIOnNAXPPrrDZxPL7fGJxVvDeFsx5toWV2EfFSDUwCPFU0wWLzM55CdHxahBBG0csOfN4eg9KFAbAAPlU5-BKzYm7JMiTvHQ_8nk0tFQCicbinRVYkmmGIQ0q5fjDSyTsWlJThmwj0DNCk1C4N9bQ5k9GpbXjjSFh-nw1SMofLp6iLnxQ5Ziwv-xLF81k2_wzBtoqZd-_ekUKGXFrMBh2rB4d5qntMxBRuIpAL_NKtXPeRNI5CmB7eyYGMnboSi8l5hlATFryOb6SsF32BK6ce2rq3AFaC3rOpB3wmYxvYtgj8_-TExJA1iVT1PTkuf3ocLGfp_cTTBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=RaYLfP-WODzv9sGRHNvXEvhKFddV6Ses-XjTY0sh75kHzfgeGDVOltASxLQOvttg9I6J-_itlW56i0GxGh3w91MqXaTYeWVp-G1NQY00nTZGOMmL8vTmA7FW7urmsI_Ct65LovHD02GWfVOu_85CtjnZlwg0W0SDTbQCUR_gc5VKf_gCXfrvx3j4FGS3pWYB7qQUgBRfuMPM1HtBN8mTD8XYsNETnGqDd8GsxuO4Q4pUz5fOr_n3HdCvtVl3PqpvjmlhWbhmh_9bP37jEPLKqM79KCTuenmtzjdpeRdyRGy50D9k31YZcpkGBs_mtE3qLdStUs0z3gO8xVQQ1g6ioQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=RaYLfP-WODzv9sGRHNvXEvhKFddV6Ses-XjTY0sh75kHzfgeGDVOltASxLQOvttg9I6J-_itlW56i0GxGh3w91MqXaTYeWVp-G1NQY00nTZGOMmL8vTmA7FW7urmsI_Ct65LovHD02GWfVOu_85CtjnZlwg0W0SDTbQCUR_gc5VKf_gCXfrvx3j4FGS3pWYB7qQUgBRfuMPM1HtBN8mTD8XYsNETnGqDd8GsxuO4Q4pUz5fOr_n3HdCvtVl3PqpvjmlhWbhmh_9bP37jEPLKqM79KCTuenmtzjdpeRdyRGy50D9k31YZcpkGBs_mtE3qLdStUs0z3gO8xVQQ1g6ioQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=JFib_qITq2EafsQEmoXSuu8YRxlxjOQ-6ObJetG0-TmPbbsgxR-hyJXSghCjFUzWGKVQAEBwCVBb7yAxkAFn6KRZPjhZE_ImijtB4m4Ee3BWv1reXChmBfi_lGFzzzZawalzWZlDDDj8AgQVI4VUOHgZsgHVYxnhXwiq0vjF5ugkCWvpUOYexi_zIpE7mdtlUUyBNkQedXRjg8s8FE7wfyGmz5mfEepg2m4fmDX8lupBx39Yw5HEpoXrW2Dku0EwHgVhq86_hc75S5bAvdMuq-JnkjyhgNtVZnowGqWDwte5zPvLrBiV_tVLvhNbm_Moh7GMAtZeeZMti4_oZUU2tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=JFib_qITq2EafsQEmoXSuu8YRxlxjOQ-6ObJetG0-TmPbbsgxR-hyJXSghCjFUzWGKVQAEBwCVBb7yAxkAFn6KRZPjhZE_ImijtB4m4Ee3BWv1reXChmBfi_lGFzzzZawalzWZlDDDj8AgQVI4VUOHgZsgHVYxnhXwiq0vjF5ugkCWvpUOYexi_zIpE7mdtlUUyBNkQedXRjg8s8FE7wfyGmz5mfEepg2m4fmDX8lupBx39Yw5HEpoXrW2Dku0EwHgVhq86_hc75S5bAvdMuq-JnkjyhgNtVZnowGqWDwte5zPvLrBiV_tVLvhNbm_Moh7GMAtZeeZMti4_oZUU2tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=ERXDJ8Qz1Pf5T6uTZ3SiZzdqCt5arUXYV3lW8TX2RxgLBKAx7inYYc-BBuYMOgMxiBRShP3dRfcUlxsSRugir8S384XULChTHXeUb886T8gds06BhWF2zzHj6NpcQ953QrHJhcQkLbwbqkHcPP9PnmIJXMVXW02sFKFbldRXGEKNOTCoNl6WLxeP5zyB4HPvLGMgaUtwITPly6PNBxk5DPrTJpPAE-EY9yLkYPvyeXejeqEkdSMCqbQSIILuzEBcLnduMkAmG59v4WY-gyZNkpikxxCkHW5t9hQIO0mcUjZDAWPqaCDS_HZ7WPysgSqLao7yr5QF652XIAwMF1eShA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=ERXDJ8Qz1Pf5T6uTZ3SiZzdqCt5arUXYV3lW8TX2RxgLBKAx7inYYc-BBuYMOgMxiBRShP3dRfcUlxsSRugir8S384XULChTHXeUb886T8gds06BhWF2zzHj6NpcQ953QrHJhcQkLbwbqkHcPP9PnmIJXMVXW02sFKFbldRXGEKNOTCoNl6WLxeP5zyB4HPvLGMgaUtwITPly6PNBxk5DPrTJpPAE-EY9yLkYPvyeXejeqEkdSMCqbQSIILuzEBcLnduMkAmG59v4WY-gyZNkpikxxCkHW5t9hQIO0mcUjZDAWPqaCDS_HZ7WPysgSqLao7yr5QF652XIAwMF1eShA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=ZYnfl44gOM7cU7Z9QILFRuySQLhB-kZo-hgjf_0IOA2LD2MNsbDjHHrjAu4o0f7GK4-JPP0H-9D0HkwOcNqN-MBpZfmjI8mLoSYzLa0FN4WH9WU1zIfkbxOvxfRvzqksYHXgVU78a5zqOjnt2GC4bKeDPL6YtKUdsynnU22fKd_8gblPJnnXRXmy8AW4245l-8ibxh5y2aDfE8CGLioEC75wnkxm4z36tScPLle6j47HC8bCXDZTxVd2gn1kEmDQYEkH714kLCa8Xwst1nNDzj_yaJsrNMM-E5_7rH4LZUDWPAFkvBTP4g7nL3hQwtAvfo5EIJ9ZsbRtZHEQH2QGQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=ZYnfl44gOM7cU7Z9QILFRuySQLhB-kZo-hgjf_0IOA2LD2MNsbDjHHrjAu4o0f7GK4-JPP0H-9D0HkwOcNqN-MBpZfmjI8mLoSYzLa0FN4WH9WU1zIfkbxOvxfRvzqksYHXgVU78a5zqOjnt2GC4bKeDPL6YtKUdsynnU22fKd_8gblPJnnXRXmy8AW4245l-8ibxh5y2aDfE8CGLioEC75wnkxm4z36tScPLle6j47HC8bCXDZTxVd2gn1kEmDQYEkH714kLCa8Xwst1nNDzj_yaJsrNMM-E5_7rH4LZUDWPAFkvBTP4g7nL3hQwtAvfo5EIJ9ZsbRtZHEQH2QGQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxtQBOY9-hNx3q6lG8Gna-6M_ah3AEiJClGgEujsuEx76II6NAKSW-TcXMhje1E6W4MIDbW79eqMzpaR2XLfGlmzaH4JRenp3A_QENRkqmGOBJzrNrVlk--1iYkD_yxPqNEDm_Ff_fb1emmnJWCPDpCNxpQmbqGfLb_LorPDD73zsEOiTfjrVsDwqv0tLdwif-pvQDbIfmXI0SuoFuGIY7_xb3DpNiRp3ne_3_kmpmnBgmEqi75QjZZPJR5yM6ZPuV0f1EJmd8nO31RACO2P2RdSC_5otvX-GG-hS245zy_QwSfm1frIt6Af-Q_8afv-CqubU8YK5Br9u1KxqRR6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9Rpb82JVaZLgoKLPzIZsPhqnxjoaYETEWyayFXE_h0nRJL5zn_q9BZThGqvw9LS9FVOLV5du_pczPl8bT4cW0agDS9bjpX1LhfRJPAOc2c4Sdmhx2KoUc5y1w8FKmjGSidDxf8OsZMLk4fKHytT11McibbE3aL4vmNB9wZf28CfjGUwCaWSyXurrSV37Jo54UycfvsnetaEF1WBB7w6SLTbzbQ2jau3PnlyU3IcCLMo0esp7MYiuO4cf_mkgRjvz89z7AXecFb-jOJQScSAdIts3_scWpQH6PuIuwndfAk2en3BtdRP3kTwZlcQba_YdKbi_beK-xY_iTG7FR8RPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igcfwOGphzkEesahQG-VnYz7g1TUAhwmYCf9rHWL_WvGaalROOIqQf6tK96DiYM6rIOioH7cKLAKjucSgJQxquUXMh9hAdYSnqBJ8A7v8_2uLTk3BIfawXaHPHVdFKmvr6D2QF2tkUsaXXttmwRp29ZPWn0AkM7mIFx0nUBUBEw_KsmY5bXdb4dsDuHg2-ZzRPG89OQMivT2cq_ekxo22vnBxBZjvjP8g-Gh253eizwSdt8o66iYp1WWgDRIhaj2X1KKl3j3eFYnE6Wl58WCox0ijIo7_R1DXv51932_GW1QV-4i__RizjpS36AzyDe8vEuekmDfrVCxRL7iovsbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=mu2G4jEw2wCa8JkPxg6f8JtdzAAGDwXmpubgXrdlhXL-L522w--3xR8SnHSb45FhLpsmO0xpaIHYdlu5DiYPiRQBERNl_Kd2TYD1i6IC283pnBVmRNLkL-ru2reYGkaM6JzOdfoexzs4kcjC4tH-DN1hvlYjwlpr88cjPTznVC8fvnxeEYY4DDflb7DujXBDY1ftU-zKokH_5MzJBO5ul-Xy2eg0y6W2OsX3kPwJfY1QRn2rdYokaIJ1NfmwPqYH5nanUy28KQZMTHNWCfqorOs5xqD8tII4yvJpWFN_pMAY8au81DuOw1gsmcEMNDgo-IfFSesvo0X8q7pg51yN8nax8wI4fywJzIcYdLnj_1IjwufamHiC9etyQwTVWAALfqavIpOdvjZRX7laYgbadQO_SFcqOrMR-VjtyiwEn_aG6ANfDYUxaHMYGhu1FnYtyLoq8u75Imh70kzVN7vRafPn2J-_y4jib7nXEBKkYVAT5i_S6zJ2cRCDTeUr3NcSJBJ2GT1nu759C8J5CT8cyM1enLRIu7eShbQGu6kWK-vw4sPF0rF30VbppTb1RofK5AKU5vBokfJe9wnYLOiAdCWHWqu3QkLlPHIHsV4yf6eAhFMJFK-6QCHTii-SuOuZWrxW0Zc_TLeU4FC5HI0H12GgqXoWu6iILLkYeI6mmJY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=mu2G4jEw2wCa8JkPxg6f8JtdzAAGDwXmpubgXrdlhXL-L522w--3xR8SnHSb45FhLpsmO0xpaIHYdlu5DiYPiRQBERNl_Kd2TYD1i6IC283pnBVmRNLkL-ru2reYGkaM6JzOdfoexzs4kcjC4tH-DN1hvlYjwlpr88cjPTznVC8fvnxeEYY4DDflb7DujXBDY1ftU-zKokH_5MzJBO5ul-Xy2eg0y6W2OsX3kPwJfY1QRn2rdYokaIJ1NfmwPqYH5nanUy28KQZMTHNWCfqorOs5xqD8tII4yvJpWFN_pMAY8au81DuOw1gsmcEMNDgo-IfFSesvo0X8q7pg51yN8nax8wI4fywJzIcYdLnj_1IjwufamHiC9etyQwTVWAALfqavIpOdvjZRX7laYgbadQO_SFcqOrMR-VjtyiwEn_aG6ANfDYUxaHMYGhu1FnYtyLoq8u75Imh70kzVN7vRafPn2J-_y4jib7nXEBKkYVAT5i_S6zJ2cRCDTeUr3NcSJBJ2GT1nu759C8J5CT8cyM1enLRIu7eShbQGu6kWK-vw4sPF0rF30VbppTb1RofK5AKU5vBokfJe9wnYLOiAdCWHWqu3QkLlPHIHsV4yf6eAhFMJFK-6QCHTii-SuOuZWrxW0Zc_TLeU4FC5HI0H12GgqXoWu6iILLkYeI6mmJY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsD7E0P-S4hlLGQohuEJ9qVS4ecYlgu7Guj3L1Inq1MbzmdHnrIVD1JrZwjB1HofTXjyeAawXozQBlsSeBGUvugqpIX8JH_LeXLMHnDoCr9b57AfJJTPjOrDw9zOvUrGjk8HKsuAyv1k8aPi8tur16gXrXOM4HTr6ziQdjUFnG15jnM6r-sBhpBA8QW70j5XNRXqfRTrLROllRLj16-QdLrgOtnbju0X5lQxqtnHrrW2oM8h1Y6Uc3X-D63pyD7yRzNDTU7Xv92yXmgSz0ZxV1PGFYDo8RStUWRRdSihAde-3KWJ5tYmdhomyTZ0tWhG73cr0PpufJMbjFVn3tfkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=WRty5bqbZ3UT9JITnYMsboDMalfWzqFcYs3TGe4jd1pm1p3fjVgIC9CiEU7VNIZKmj2f68X05eNLHR4DoWnhQrE2r-Na-6bMafAS0_0tlgRey1o7jALbo9D6GyiWA67rEXBiY7L944lsftCwbIC5g72IyHhGimQKgrtA7VJBgbp0i2BfZdg00gjaQUziOpzC50C9QNOSCF_u80_W0v3zKQdmC7gpWaTlB8zy2YLvsnV9hDM3RHQI5YY0l843xsaUGuuElRrE_GQDOgehprJefd5IAyU5vPB9qsc-10e34Iy76HtNi98Spk1NFysoYF3j4KYq-9_ZD9MAjKI0iNc_1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=WRty5bqbZ3UT9JITnYMsboDMalfWzqFcYs3TGe4jd1pm1p3fjVgIC9CiEU7VNIZKmj2f68X05eNLHR4DoWnhQrE2r-Na-6bMafAS0_0tlgRey1o7jALbo9D6GyiWA67rEXBiY7L944lsftCwbIC5g72IyHhGimQKgrtA7VJBgbp0i2BfZdg00gjaQUziOpzC50C9QNOSCF_u80_W0v3zKQdmC7gpWaTlB8zy2YLvsnV9hDM3RHQI5YY0l843xsaUGuuElRrE_GQDOgehprJefd5IAyU5vPB9qsc-10e34Iy76HtNi98Spk1NFysoYF3j4KYq-9_ZD9MAjKI0iNc_1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=miAdcHnSVDFPm1uh83KVZvAqe4QI5Q3AxrEXhQvQ1zdwZvZnJNogkF2NCE1j-U2KnAS07ccP1wd7_dVaIPj9pwTAWvWmM6LLBxYv5AFoiEkP-SSMY7MAqcQoZG6J0ylZV59gpTV0EFsJFx1N83DRdmcestAn0TWpjBp6VigWBt1GcrtWYMtrGv196DZ_Za5YIZWX1vrhvBIDHKlNnKab30a0SrEN4XtEXzSv6zJRJTJhnZBz9Cc_LHIQb3l3mGqOpx7ath1Ar1e6mLPHqOHF5TupjBbQhxnw1wy-qc2mFIpCzJDz_MskLUBELYLe95VY35kh9_PaG111d2gLvZROPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=miAdcHnSVDFPm1uh83KVZvAqe4QI5Q3AxrEXhQvQ1zdwZvZnJNogkF2NCE1j-U2KnAS07ccP1wd7_dVaIPj9pwTAWvWmM6LLBxYv5AFoiEkP-SSMY7MAqcQoZG6J0ylZV59gpTV0EFsJFx1N83DRdmcestAn0TWpjBp6VigWBt1GcrtWYMtrGv196DZ_Za5YIZWX1vrhvBIDHKlNnKab30a0SrEN4XtEXzSv6zJRJTJhnZBz9Cc_LHIQb3l3mGqOpx7ath1Ar1e6mLPHqOHF5TupjBbQhxnw1wy-qc2mFIpCzJDz_MskLUBELYLe95VY35kh9_PaG111d2gLvZROPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=CYBFeTTFmpF_qJ1DbKFiCSVdhqqLEUpF3d5JPe4SAUTlDfud3vi5liz7hQb9MXMpCTcMmkuXFTFXPgdIwvlYugxl2a0_d0BXBIOntQ7LxM_0vQE3yEytgAHFtURE2GhaSHwDN0sWQRwv1nrOYbySDqqW0b-os5Tq_6XYaFrdJHfd0GCkO9n8WmVnpE4G-r1GDZ5lSOLUhvQfPcBtYnnlQWlDn6XHzk4tEAGHbJVkPYUWxrBgZqMGdtwD6uwyREUBHHoai8BWTNXiWvhG7efBaLn0qUGxD8RtKyhoQPSmlWmXe5NN9xcETMJ1XnuFhC2q8tGFTB2fv3T_rhZS8r_gjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=CYBFeTTFmpF_qJ1DbKFiCSVdhqqLEUpF3d5JPe4SAUTlDfud3vi5liz7hQb9MXMpCTcMmkuXFTFXPgdIwvlYugxl2a0_d0BXBIOntQ7LxM_0vQE3yEytgAHFtURE2GhaSHwDN0sWQRwv1nrOYbySDqqW0b-os5Tq_6XYaFrdJHfd0GCkO9n8WmVnpE4G-r1GDZ5lSOLUhvQfPcBtYnnlQWlDn6XHzk4tEAGHbJVkPYUWxrBgZqMGdtwD6uwyREUBHHoai8BWTNXiWvhG7efBaLn0qUGxD8RtKyhoQPSmlWmXe5NN9xcETMJ1XnuFhC2q8tGFTB2fv3T_rhZS8r_gjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=hUzj8LiY8m6o0yvEOOS5tYrbYEItQmIgJTyURd4XeaparyJWHT3JjAwvNthtQydOYxs1zj7ZxNhSSe-v5sgtXuQuyZneAoKLI2Tsko3EgJYvc8L_FCOEvN_Rp8yDyf2Xy35DZND4UKQDXJweLNNenY79qaRvL9PsVZDO_wvjZHmXBNgdUpIbXwqmKTnB8IDJgUaBv1Gas4qzm82xd0YZpSe7vo3TY4OjT5jioBwjcqPDW08zPS2HyYLQkOnAh4irO6nWmjVE2HyxgCZJTdZK-gvDV9YSuIB3Ia5yJv4I66k7UYA67hW1F8wxqPSwl1nwHwqYfq7PthIhaUacq0tgfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=hUzj8LiY8m6o0yvEOOS5tYrbYEItQmIgJTyURd4XeaparyJWHT3JjAwvNthtQydOYxs1zj7ZxNhSSe-v5sgtXuQuyZneAoKLI2Tsko3EgJYvc8L_FCOEvN_Rp8yDyf2Xy35DZND4UKQDXJweLNNenY79qaRvL9PsVZDO_wvjZHmXBNgdUpIbXwqmKTnB8IDJgUaBv1Gas4qzm82xd0YZpSe7vo3TY4OjT5jioBwjcqPDW08zPS2HyYLQkOnAh4irO6nWmjVE2HyxgCZJTdZK-gvDV9YSuIB3Ia5yJv4I66k7UYA67hW1F8wxqPSwl1nwHwqYfq7PthIhaUacq0tgfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc8wl-cULTHSo2OKGAi4lK20SWh9iMfMVEXR8olagQKHwKLIHAbr1AEgRE0gKb3KQacm1RQUEft44o9OHOY8VEcc2jMxU6tfA2etNfGPi22diDvzgEvGeTrMmlavmw5Fc9eFGgJy8oXQ9-kg4fdKCayNKRN3Qhz2NlN0Ce0zDCl-tra9AP5SLkXeUTYTzHSJYQRNZWIv50Y-abhk9hI3OgfPFex-QOak9MYbVUTs8ww6iddpXaozrDXIQM6OkrkyVVc3ru8UZkny9MnMXldZtT7tYCnAj8ArQZylXeEExNYSsl8no9vQQnIq8hLgToSveqxn2unKHKhXqNguzo4Zng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v56eoogur1ipo6GcmYNwak_RAUG7DmFhkI8PQk0buk64yjhZdgz-AiUC_nD4p3fjthiuaK1XyviHGWmQSnPh_68tu_4vyFmPHal54ZbweI_DpDzohETwlfe-gkjbZWFHgju8xCOW_JaOaMV31XF4yHjqLJHI9Ziwr4-YLlBGQgVnsxgktPSZhP840gajG-oqQN0r_TbyKwpz_jYXePdEph-IcOuoTtqhnLaeDO4okwsDqJ-BXlqkkFxnIqipWjWRSAzJ0E-uUDTxC8hSKm_zvtNOdvvTEJ61TtPR19ETxBASSACbRYOBtX6qR-l2eHciRwZ62pVBiMMQabKNT4UYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=H7jsTTJzHC_81SHbWCGB-TtkKSBmM4mVMCQs4LsJ4zAwvUF2B6RcH1cOxQWEUpnhtm6krRZofUeYcowQpj3N6T6as5cxZUXuivgbfu8J2te68sqB0LMKskytNxEpPM8dQbWcUFYcnioC69b0W9VhgeIwz5lxL-7wVOexW1AUINt3FVxxH_7qBneDp_DWwzbTtkc57a5fOUlfFmlSzxUGojIEo--fMXD_96XqEhGNNMb0aD0BC6mTIO7Sh404q9akk3EUaeJgI8Wuoh1vG9ksdsuL6HiHmG8K5LhJJg5k69xmd-dTdQQoQrc2IhAObFsoqCmQZGegaGTaPMjHQgqTDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=H7jsTTJzHC_81SHbWCGB-TtkKSBmM4mVMCQs4LsJ4zAwvUF2B6RcH1cOxQWEUpnhtm6krRZofUeYcowQpj3N6T6as5cxZUXuivgbfu8J2te68sqB0LMKskytNxEpPM8dQbWcUFYcnioC69b0W9VhgeIwz5lxL-7wVOexW1AUINt3FVxxH_7qBneDp_DWwzbTtkc57a5fOUlfFmlSzxUGojIEo--fMXD_96XqEhGNNMb0aD0BC6mTIO7Sh404q9akk3EUaeJgI8Wuoh1vG9ksdsuL6HiHmG8K5LhJJg5k69xmd-dTdQQoQrc2IhAObFsoqCmQZGegaGTaPMjHQgqTDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=iF8GhmljwsXA-_z96aJP1Qt8vFthECp9lsSUf8G7cQtdN5PeK9MLKnI-d2BzqH8E0OBUKpyQG-vULUPggX96h0jXszvQbb5I3Ts3T4Z_M8YPQvBg9Pqc5aTWoASICdq3kdlXClWSsd08uQvEpJBw3nNS2ndqbA-D2DlMfn15pOGBkLReSa9izM67-leJUi0vMIDtCJk8_16ynwy0QqD-AWkmKnBJxZdIe1jpLmk2fywJeyK2ZtoKGA3CP0UAXioktNK-1GR_LbCIMCguThHmyfhKTEYj3aWCqNSZUkwPEGKcqqp0dVLwBIGlkJzQ3hnZ39nSu49VzyJJf6kQq4P4Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=iF8GhmljwsXA-_z96aJP1Qt8vFthECp9lsSUf8G7cQtdN5PeK9MLKnI-d2BzqH8E0OBUKpyQG-vULUPggX96h0jXszvQbb5I3Ts3T4Z_M8YPQvBg9Pqc5aTWoASICdq3kdlXClWSsd08uQvEpJBw3nNS2ndqbA-D2DlMfn15pOGBkLReSa9izM67-leJUi0vMIDtCJk8_16ynwy0QqD-AWkmKnBJxZdIe1jpLmk2fywJeyK2ZtoKGA3CP0UAXioktNK-1GR_LbCIMCguThHmyfhKTEYj3aWCqNSZUkwPEGKcqqp0dVLwBIGlkJzQ3hnZ39nSu49VzyJJf6kQq4P4Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzU3U4rKVf8YpdDprOftXpO5LymeErYzjm1EfmUm9uhbfn1ISVqpEbgWvaZt05NItFM5NGMLdREAydg3EJ1QPBtSu3GZNXCrHCwknhQ7mDclphdU4nbKmb4uhUnVVkhdIWS-GEpAO41JfE8fxBDpD90NkMgRduh27mPhZ5NnFF2XnLiKT1xf_9QAHw0Z6ai681fKYJNEe46_m7LmRRnP75CMRySKFbs0fqR4f-irShUMmg7QGt6iSMNwGfVtqPpe5ekO8SJ09hXvphdg0B9xT3LvzyHC1kyCBNe0CnPsRX7rMJ7otM3PlOUsLsi01wnpErKS40tprnXJvfVtrwSL2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=uEp-Oi43mfkpcJLJub1ktDU4dTLXTLsIRGt4GHljD6IhTxmlRUWZbj1Rw_q3igkWN5vMINwhvhOHj-o0kPSnrKwUYhKoPwSro3r23UANqAJQmxSv_Yo1CCYz7F_Wggq5kPRkthY2OrsY4LvDV3JdOUcCCfZWK3mq1DoNcOlQq-3OS-HThtiMyVglJy0zuShXojBSHBqJMJ9lBncxX1PX2-vC8M_Ji4kAIL1XxxbKhk5AxqTl_GRO0RBo8Wi1Ul5cXu9wui8cshKf22YPuZKKWObP34_WTeEdCmREwrZi5gGPPjYYHlU6Yc4I2ZCGQUpB9q-uv2zsQS-iwjuAmn8DUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=uEp-Oi43mfkpcJLJub1ktDU4dTLXTLsIRGt4GHljD6IhTxmlRUWZbj1Rw_q3igkWN5vMINwhvhOHj-o0kPSnrKwUYhKoPwSro3r23UANqAJQmxSv_Yo1CCYz7F_Wggq5kPRkthY2OrsY4LvDV3JdOUcCCfZWK3mq1DoNcOlQq-3OS-HThtiMyVglJy0zuShXojBSHBqJMJ9lBncxX1PX2-vC8M_Ji4kAIL1XxxbKhk5AxqTl_GRO0RBo8Wi1Ul5cXu9wui8cshKf22YPuZKKWObP34_WTeEdCmREwrZi5gGPPjYYHlU6Yc4I2ZCGQUpB9q-uv2zsQS-iwjuAmn8DUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=rt4zw6cD8yI109g9xjnQc_LOLrzSafDJFEocRGwg-Nz2pntZg2UuTIxVNMdFXJhqIBwr8YVaS3tjp_mdPx68mY69ftN5dk2Ohg3B6yTqWHNjZDAYqnaFSmFMKrZVVe7XFnfFqibdR0g9yOGvfr-ICqpGypEl-4MDKEuf-FinbQzgzoVcBdPg6LmQ3nFMPAx3k1FiIbq_cn7yqWbjBLAZ4rSdRGJWBsM69Hfs2SShHtDvOD6jpURaM3MuAW1c0QzgceGjMfjGf4muXLriTFUyfzOxMpxc7AhIeraVSR4_HlJO-uApA2B8d05V7w3H7q58aYKDiKVwNXk3AhXGY2fi1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=rt4zw6cD8yI109g9xjnQc_LOLrzSafDJFEocRGwg-Nz2pntZg2UuTIxVNMdFXJhqIBwr8YVaS3tjp_mdPx68mY69ftN5dk2Ohg3B6yTqWHNjZDAYqnaFSmFMKrZVVe7XFnfFqibdR0g9yOGvfr-ICqpGypEl-4MDKEuf-FinbQzgzoVcBdPg6LmQ3nFMPAx3k1FiIbq_cn7yqWbjBLAZ4rSdRGJWBsM69Hfs2SShHtDvOD6jpURaM3MuAW1c0QzgceGjMfjGf4muXLriTFUyfzOxMpxc7AhIeraVSR4_HlJO-uApA2B8d05V7w3H7q58aYKDiKVwNXk3AhXGY2fi1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKLPD5JGMROKFPu3iolgKQc_HyogAFc3vpcRGmhR5ZciztRdapM8rZxtK2-CmVy7kmTOp0QsUL3kGnjDz0Pz8i47d5PHwjQaQMTcuT5JRW1mJNUfNVVmrTGq0kWXE2XDArsnW2XniMeieQ2J97uqj3gF6q4zaH1Skt1bBj_ftDeY7tQ8yvNRKihOQPfShwUpcsDz7vrK76EwzM3LSMikf2i8HF71nNzoVpQfWW3QFaIk7zzGCInJPahFvA6w7Sn5Lw8E5vXPZoV4UwVioLeNA3SG_UmeHog8Y5-kuBH7mdM-kl7o8z7rar6lDhffDh2lNKX0DQMq4VwbkWwx9o3WcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8gO2fuxFsx1tU70xWHbN8zFAosdu7feUd9dUoYcJOVUx4_PPnV3dac5BDoVe2l6M7B-rAIx8Ib7utr4Lcra3OZDl4d0HlUGtxRfJAicRJfdbp4VX_pPXOvEEe3Yy2asOOpV_NYQLaeFBxtR3FSPicId6EYgceZJe5s0NGm9vCU9jvcRnmjEDqgs0c7nRWZLtPtYPw4CvPbmJZyPKUKCTi4nELCjG904cpPLE1BQ4xWpTk0TPjjF8el0Ga1JKdzPIN_7rFn-eDjc4GKoWidDyto_kJgVyYKXgRFyOmrLWwDXUiFxAoevVIu4fiMCfHX-pGGdl-2Dhsp375muPtJJTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v2k1DLWwgJ3EWBUMqqDA3gTg2nkRQCAmozA4qxvLoSuwWQNnP3oPSTWkQWq7VQEcW4xjygEVq-gNtmlFX_fPn62f5kr3Jmayy7zmgrg_KZzBm4t-VLJD8mG5_WefVfZxqVz3EE0DM97Sm_gJ075ascrUBd78oeQxHG9KuMfWwLlu-bDcVZea642nNF8Wp0vvocXC2V37QtMT0xatsA7hKz3tG5Be2yRSo3MclvL_kLi_iuPheBLzQC_XxpLH1_pyNVFeUFpJgOjxX-MSnjuxKx8mN3Dd_QlYk8NwxI2n-OSrhhkUZ7_7miGwSUo4HOJ5tJ7Yw9KH5h7ZZAhLOKvWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=AaefmArgrT1dn3l51T53FpudmoeUbV3EbN-Z271g32P4TamhJnkj5jijF7gVFGPVvwoMDgmlFLTmi8cM715GZ34xa2lm5DHkVZl9_skesb829EL3rW-SnZJXSRcQbr4QAKq4gfnbqxa_Bu9waE_-B9axMNlq8RL_P6oU3kpzPIGuQaHFV32d3y29IWyZwsl41IVBM26rBd8NzOSL3hg1ueL1i2BD2qJnwuiRmEuK_8muMkA4QVrTTj3Abc12r9W_EDwKdutjJ1lt9frvhc22LepgMuVOKjnRkZIfBFjBXw0u8EebSdazIUibYG9gsj7W4xsHVxEcnZWUug74f4ORgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=AaefmArgrT1dn3l51T53FpudmoeUbV3EbN-Z271g32P4TamhJnkj5jijF7gVFGPVvwoMDgmlFLTmi8cM715GZ34xa2lm5DHkVZl9_skesb829EL3rW-SnZJXSRcQbr4QAKq4gfnbqxa_Bu9waE_-B9axMNlq8RL_P6oU3kpzPIGuQaHFV32d3y29IWyZwsl41IVBM26rBd8NzOSL3hg1ueL1i2BD2qJnwuiRmEuK_8muMkA4QVrTTj3Abc12r9W_EDwKdutjJ1lt9frvhc22LepgMuVOKjnRkZIfBFjBXw0u8EebSdazIUibYG9gsj7W4xsHVxEcnZWUug74f4ORgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imZHU9C1ikL2uXWXWd4-tkT8AUs35sShf3eYpkxBbaDkxqzM6b1_eTOW-gKrV-CGE9c4NBOtvfaCLkB9hCFaeqIehOiFjddddTjDMD4w1viz29IoTqwoVNADdd-6cjnKe7BH_qP1S7ztmtwSxBj94evt-19x1yelZhbpLteef24JCL2lBGYGNysYrv3ULyyMIeRmHt0evPqWNJBwO4ZHn2MHgR8gWXCbfq6gBlFlgDbLXPkiDBeS7fF6P893e7xujKNk22hgxvSlH6YVIF-MOO_YngvrrETcmO07GuI1b3mZNqTBxQS1M2dl6gOlz2JYU_gBFYS1oOrg9D42-8sKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAoh-oA-4fzTnlrPE3T3Uf_GTLxd9GRm3b2ySqbBmSUTpU3NhLEIjp__YWCAbqjiTrh5HdNXyV6aLuAgzV-qIpWIiALBZSDk2b2eOZJsMUm8zoyHTq0pdKY2DOAP7F3EcTu1DOI6VIdUNobN_A0iAJ2MnCCmqTkZze56NM7RSEwcBJ8HxpNggrmqGe8GY-teCOJstbAaGWULcAFHZBm3NRIgjSluierMSGtzoskCZTx4Fooy3HIJvRXxUDY2IAkD8OjBUpyLZ2TAslnMD_69U-wTB745aKEwbKhM7P_ww2fW6OM_bGhJRTccLVIAiypcdSczZuEj9BHEW0JX8Hdxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=dPe-63OKkbQJ3wgOUIcjoLfVvs-6dw7o_YV30KnchZpg5xFiboSIc886CetSUwmj_lUXN9WcECJ_Os_rdh2PAkagycF6DQw8c5ENTUdEe6V8CyCceNIm9yEZkELeAlbeNQCRGa6BxkXyehcTtoJE5iVgCFtg1VAcuHdwpClcXk1b3xtKx7nnEURjz-D_pehC1RTbU5iR1om-eQa4OTlqO_c25OSJwNJo-9GI0zKp9GmwdRgKRWksnbrP2GguMcLofnMDn5kaHv7aNzrEnRHoMO7yy1Zw2_q10sycOcp9IwQPx8o-nm2opEFaZJAEhJeTqphgQtRRA7sVkyvne-Z2ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=dPe-63OKkbQJ3wgOUIcjoLfVvs-6dw7o_YV30KnchZpg5xFiboSIc886CetSUwmj_lUXN9WcECJ_Os_rdh2PAkagycF6DQw8c5ENTUdEe6V8CyCceNIm9yEZkELeAlbeNQCRGa6BxkXyehcTtoJE5iVgCFtg1VAcuHdwpClcXk1b3xtKx7nnEURjz-D_pehC1RTbU5iR1om-eQa4OTlqO_c25OSJwNJo-9GI0zKp9GmwdRgKRWksnbrP2GguMcLofnMDn5kaHv7aNzrEnRHoMO7yy1Zw2_q10sycOcp9IwQPx8o-nm2opEFaZJAEhJeTqphgQtRRA7sVkyvne-Z2ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=tzEKAlMDdtZtcEEPrE0FAvkpQNYXtd8ji4rGYiXkeYb0deYeU_tU7QyJE9tlokYzqMZVURAfqGJ_XBPAvu9UKrmKs7qm1o5zVrcoI5-7uc9L5qHHnyBLL0OIBwcu-l2C9sC477t8avLZXvE4ZU-g6tS213hNEBEXdbnDhg-BhZmmEow0aq7NH7jYWEaQwsiteFUbK6KrRgsoO4k5qfIH3X7ofskw8Wzmppu33fErmAXNoSJAoOrzOTQ4zjCEhbqk-2v7Py-Pym7p7FD6ss5c-GS2x13nZDVZI4z9WIacoH9B2f2rhIUo2Xxn0HJmuKeruQOF-U9jxWdTubXgj2Nkig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=tzEKAlMDdtZtcEEPrE0FAvkpQNYXtd8ji4rGYiXkeYb0deYeU_tU7QyJE9tlokYzqMZVURAfqGJ_XBPAvu9UKrmKs7qm1o5zVrcoI5-7uc9L5qHHnyBLL0OIBwcu-l2C9sC477t8avLZXvE4ZU-g6tS213hNEBEXdbnDhg-BhZmmEow0aq7NH7jYWEaQwsiteFUbK6KrRgsoO4k5qfIH3X7ofskw8Wzmppu33fErmAXNoSJAoOrzOTQ4zjCEhbqk-2v7Py-Pym7p7FD6ss5c-GS2x13nZDVZI4z9WIacoH9B2f2rhIUo2Xxn0HJmuKeruQOF-U9jxWdTubXgj2Nkig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=XwGQcPMCDzGSSRH6cJ4q6NZsy3FqNV7dc57mzLgQ2ea2X8i4TGlI7dmqhN6IR3tDYEVDGNcfhh51TJ0Rph3qHZIJm91aug71U5ykN6sccU1Io-jf6qhR2Nucf6p_w6pYNOeuPdqIvzN29133CjBzb5hM6_G42CiU75Pe5TL8E3Ag-LX6NWmmYKajD1F8SiBH5qrNL7KDAJytZCVoFql6-S6p4wb_PKbzcDwuWqm0B0rER8V1vhVMei8mV8poFUu9KcB6uKbzCC3q-ubJcj0i_X6us1B5VuoLX8wVkiU4O2C_37q2o9KpsY3L6XHS5wLDEDoJJBRWMCGneqd2OOcEWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=XwGQcPMCDzGSSRH6cJ4q6NZsy3FqNV7dc57mzLgQ2ea2X8i4TGlI7dmqhN6IR3tDYEVDGNcfhh51TJ0Rph3qHZIJm91aug71U5ykN6sccU1Io-jf6qhR2Nucf6p_w6pYNOeuPdqIvzN29133CjBzb5hM6_G42CiU75Pe5TL8E3Ag-LX6NWmmYKajD1F8SiBH5qrNL7KDAJytZCVoFql6-S6p4wb_PKbzcDwuWqm0B0rER8V1vhVMei8mV8poFUu9KcB6uKbzCC3q-ubJcj0i_X6us1B5VuoLX8wVkiU4O2C_37q2o9KpsY3L6XHS5wLDEDoJJBRWMCGneqd2OOcEWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=uJ5FD7_XxPv9b5LxlFsY4alh2ThRRAxegbx-1DTZsY-q2MBoZQcTMY3e2ucdB-BZ-STD53sXlkK7u67kadD_n04c-Bz_TJtj_0FI4rCQe3oAKlDhqdjNt8Vd-fJ26gd-rXeE3sUPLF05V3m6CQEBXYVTR9lz3H8M5nKolze_ZXeWaxJqALGxp4toRdRb8f79xGAezUicO5YvoLNn7JKPDz2Rzqa8jB_VmX-0gkHXzyzq5v5zobyVqJNoYkufOq9Iyd8q_ZcJbupFFqUX-vvsbYzNAGra2XLAWAxcKlSJhvU_M6p1lopYSqiAdg7sqxDovgwv45T_NcvLgE08qYRoWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=uJ5FD7_XxPv9b5LxlFsY4alh2ThRRAxegbx-1DTZsY-q2MBoZQcTMY3e2ucdB-BZ-STD53sXlkK7u67kadD_n04c-Bz_TJtj_0FI4rCQe3oAKlDhqdjNt8Vd-fJ26gd-rXeE3sUPLF05V3m6CQEBXYVTR9lz3H8M5nKolze_ZXeWaxJqALGxp4toRdRb8f79xGAezUicO5YvoLNn7JKPDz2Rzqa8jB_VmX-0gkHXzyzq5v5zobyVqJNoYkufOq9Iyd8q_ZcJbupFFqUX-vvsbYzNAGra2XLAWAxcKlSJhvU_M6p1lopYSqiAdg7sqxDovgwv45T_NcvLgE08qYRoWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8t_kECFq-WmQ90_MSLLCv0uZyYDwgANqT5O_MDp4_hRMpJ-enPdFqTTQPKwa3aTF3o8NjKGXqUv4Hwm2EmI4GB81WvpQZ19xsGRiQRDrhZrwYyvKtt3ZajufFnjbbppj7tqcnmFrC9R8uW6SMyM9nnH9UPSc-50mUrwXTQM71v3YLfU6BieFSDEBWMlRgHiM_CmeD1_z52b0i4IZi2vqMKR044Cz5vP3NnXQH1qSp3AXn0ZVt-aPXtnyFygdmkHv1GbpawjnwrYbkANSdioo3_dcTr7FxdflEPchW9M8W7-elUgM0tO-elZzUf4omXb7zymNsVzy4fFfKd4wX8YcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=p1LBDqT4AO_3Fn_cETGlsOeVkWg_OlCtbyUJxLOgF9vodM8SXBn9-Zz5QQiS9kLUlrfpslvh213-Qvv5DpCPa0Jsk_XPrcAwNP5I7rrtGAuczbCrgAyhy4uyVoyylTp_xgb-kqtki4VAzGbTJyuJl32a7O33grih4GPO-CTC7moIFTLkONhidLQgI1ptAHpl_U9vqZtBckjXXDkTwksS5ZIfsRqh0HJmf1alIV-TBkyM4toM96BOe5KxjjZbcb6MVHtaIW2tt5QF52ktmQQBJ085QudAPD2vjhfSZa9NEwXryAOQENaKywKoCZHp7tinXMbRlLJfnXTNorbAGk6XzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=p1LBDqT4AO_3Fn_cETGlsOeVkWg_OlCtbyUJxLOgF9vodM8SXBn9-Zz5QQiS9kLUlrfpslvh213-Qvv5DpCPa0Jsk_XPrcAwNP5I7rrtGAuczbCrgAyhy4uyVoyylTp_xgb-kqtki4VAzGbTJyuJl32a7O33grih4GPO-CTC7moIFTLkONhidLQgI1ptAHpl_U9vqZtBckjXXDkTwksS5ZIfsRqh0HJmf1alIV-TBkyM4toM96BOe5KxjjZbcb6MVHtaIW2tt5QF52ktmQQBJ085QudAPD2vjhfSZa9NEwXryAOQENaKywKoCZHp7tinXMbRlLJfnXTNorbAGk6XzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=Wwg43LH6XzHWz7z3J-c9l6SJSUIZyokPJimpQroWrqdQ6N004sRHQo2_id_HdJnp8t4TNRb7njebY8NcT42t-UuyGBtgoODG0jjRDcjwuyLCTFshXfPhPga8BmB0czIg9HJqTeMvo13MUg7Vj2gHO7ZNqGfhcqH0ccdA52yTxzAZCtutnXQ_c4za8P3BAzxSmqb4gqehVf8RONajgezHz6wneblj49nRQOLMiy2f4lDI_w0qiTbIk_VdT2zPc3HqZWOHhvKuRR3TTETDKf8MAXjYuO-4PXJWuDOHuKkyV5riHe0cwT93GwtAKDJl30FhYJmLLsHjc_MgXzteB6xwyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=Wwg43LH6XzHWz7z3J-c9l6SJSUIZyokPJimpQroWrqdQ6N004sRHQo2_id_HdJnp8t4TNRb7njebY8NcT42t-UuyGBtgoODG0jjRDcjwuyLCTFshXfPhPga8BmB0czIg9HJqTeMvo13MUg7Vj2gHO7ZNqGfhcqH0ccdA52yTxzAZCtutnXQ_c4za8P3BAzxSmqb4gqehVf8RONajgezHz6wneblj49nRQOLMiy2f4lDI_w0qiTbIk_VdT2zPc3HqZWOHhvKuRR3TTETDKf8MAXjYuO-4PXJWuDOHuKkyV5riHe0cwT93GwtAKDJl30FhYJmLLsHjc_MgXzteB6xwyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlhR7rJ2VW1s3Oqqz_l5g-FMISvOpJuy9o76Qd_F8CPiLelPTus3QCHXa9kStM-sPWsbWOLYkbp_kzVJmqev5xUAjK9v3c3hkeQpTwrl0kivjfmLobcfPPitmEapRtoQdGdyxluElfQLNHugIFt5B_OKhmyPyrtIbldPvWHYJm25FKoCuHnIV0VrpZHBd4MWaNWAnKt8w3jm-U4PBc5AzJeAOnsZ6FdaPYR68TKTQBcDHXzK3CpbWac6GQg_zXZvxn1lmrYr5wt-uwxaTwl3U_E7N0p6BwEKvhnFHNlfDENykpbvto9wnkl2jeviplpuaOFgv4UBjL01bzqiyVkDTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUA53EEtvnVcE5vFfrfQ7TP7nocax9UXhcGwhzPDTK5kSgvxDLMUP6ufU-2OQr8urRhX0XHHJboY9M11g218gqWpA5oPpzcn3Yyj05FpQOfmJbSHt1iqYaKxxMoLSzGXlqFkHCqmh6mRu_Z3jWX3_surMhKfX1Sv0865jSca6OmqIyuyQKPiTy-VqbDE2FjKsavl082WQqO1kvzBjlRd_krkD5TxFxUVMYdtfMYRvhf6K4-TXcisg2w5ii36HnQ7xCeI-BVziFYbNq3nfqp8m58PhmAgy9pwHM56rr3YMYQrqoLDVQUmVpGyb2Y2NKVEDn2gKH7tLHexoXDCmmM04A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOeW1h9eECN2k1YGAU282v9LrwvYTuUvwFW4vk47AE5MUArggspYnlvF90Z2DpvsbJGBYjKOHayYrrz_d4sI-mKbh5b-Aj8sbBtj__VmPX9QgRKDb2UvcNRopfL1GsFKJJVizgvjvbW_DCJGbpPG_86B00Nvk7zGsahJIU-BLNCq3gefYYavbwWpsX3LWVXH6QiTFyNcMSzZ4VrM-KHqj3INVzPcyRGZEewfIJP-HdyX_haE4SQlUuuCBrBGdrNpBrRpeewBRjiztPlO2hWG5ZciecCJJLbhE7MAJphJ8SJDt7EEXXlFdzwkYsz5Tqr16iAO1ZOcF6p5Y75pzrt5fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=qbpZ65cZODt9CzCxqpYGHovZaSc1rkUylzCrCJuTXJjLTo1NX5CIXpPsb5ITPxCRXOR0tScHgsqika6epuUUfa-dzYwaHGq_4NQQZBn5njo5o1h8HYOAQAU0bspLZDojgv7u0XE0xF9l2re5Gw9oIkKbvpO4OgPDL3drrNmQIa3NerMBNhdAN52TRvqEuXVGG0BPQMnwo9zKzB0ZYlxrs7rXJ7hXXValrGfEsgBvNlL-3nyT_PNZOcOod4YhLqa7KlCdH1slh2Za2dpABbgcSJ-f_J6yIOvD8ZRAbWabfNc6bp9QwKoQdzCyn9IzAHAPzPJa2fd859e5_cU8w-vtVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=qbpZ65cZODt9CzCxqpYGHovZaSc1rkUylzCrCJuTXJjLTo1NX5CIXpPsb5ITPxCRXOR0tScHgsqika6epuUUfa-dzYwaHGq_4NQQZBn5njo5o1h8HYOAQAU0bspLZDojgv7u0XE0xF9l2re5Gw9oIkKbvpO4OgPDL3drrNmQIa3NerMBNhdAN52TRvqEuXVGG0BPQMnwo9zKzB0ZYlxrs7rXJ7hXXValrGfEsgBvNlL-3nyT_PNZOcOod4YhLqa7KlCdH1slh2Za2dpABbgcSJ-f_J6yIOvD8ZRAbWabfNc6bp9QwKoQdzCyn9IzAHAPzPJa2fd859e5_cU8w-vtVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIT9ligT44nNZCF3HL7UZAvvGvycFsPpI6ehTi8vUKkPdkARpOjFjcDrZZTDaJ6w2rt9mGDBsRPQ3gQM90BpQMJsHdPWUbpQXR3JsQxbNoxB_ajEasgBNdmPVtznn19XlCR02wS1Tplht5hPG0nnONqdsCIbJvT782dzAkUeaEx_99PJE6XIwMD7RNirGs-RR4d2APmfQv-FusxHV9qcbb5098SKpKu1xMwuXN6dqwD6Db-_hu3o_Qj9eMO94b8R8OG8XJ0VMlwIJkcfCo2t904I7sc0KhI5FAMLIcXzXxfcOFfMRvqWDierJcLFuDGCHZXxZMRSucCehebnlSu0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c331047.mp4?token=QQZr-r0LPJ1tLymsv6N4SiWtXLrzUgUqIF7vldMU62LvqDcljihkRCQiLlLCzWchl3WMjRFkVZHBMT9qJCy9z8XM0fqzNv4jeAKojp-gWDwSvnJFhtg4eCBixhs77hxKhMf2U6C4ORJLoz4jrrfQuq7K3SDgaqsM_phh7vy7s-VXMkGY3l7Yt6VAZ8lxFTtgYOSZGmkY8r74mO1aGlO-01nTofRiSMoMlz6FCuPC53F3NeGhE8J_31OkmOeaVe5TmFYkUI_vB38iKuYz6znXVuXU8gXU7Is16kHUXvVMgzGM7u-WC9ML0U6DmPsUJNOoeM3nkU8L5CwR04tWnbQPbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c331047.mp4?token=QQZr-r0LPJ1tLymsv6N4SiWtXLrzUgUqIF7vldMU62LvqDcljihkRCQiLlLCzWchl3WMjRFkVZHBMT9qJCy9z8XM0fqzNv4jeAKojp-gWDwSvnJFhtg4eCBixhs77hxKhMf2U6C4ORJLoz4jrrfQuq7K3SDgaqsM_phh7vy7s-VXMkGY3l7Yt6VAZ8lxFTtgYOSZGmkY8r74mO1aGlO-01nTofRiSMoMlz6FCuPC53F3NeGhE8J_31OkmOeaVe5TmFYkUI_vB38iKuYz6znXVuXU8gXU7Is16kHUXvVMgzGM7u-WC9ML0U6DmPsUJNOoeM3nkU8L5CwR04tWnbQPbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=WHz17y4Ps3DNjbBnjubHSfo5SVJT9ld4LtSNYV0v45FrIwhPHIojpPSGAjzEL_5RjppI5f8xSN7h21Y4PcuvTnbisT_2bveG62dDQVOpdPab3Gfem6w-Qdf1GpF96kRGHKAoC2AsQQM_vfivvSn5M-5zT5Q-e0qUDwT61gt-PAY47sV2CGH_nvtXDceQc9yXZ3SpUMumJGgZGj9DJTtxZr789xBh7WVBEA_LplwJW5PbNC_h2hreKw459DZlBnyOKep1gMiyVHeokEdNgibB6B_z4hhtCR5eib1V2cwLwnRMr5FkJwqHIcyiKBtX8rBmtn41cpnkPQhWU7UoUlv6JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=WHz17y4Ps3DNjbBnjubHSfo5SVJT9ld4LtSNYV0v45FrIwhPHIojpPSGAjzEL_5RjppI5f8xSN7h21Y4PcuvTnbisT_2bveG62dDQVOpdPab3Gfem6w-Qdf1GpF96kRGHKAoC2AsQQM_vfivvSn5M-5zT5Q-e0qUDwT61gt-PAY47sV2CGH_nvtXDceQc9yXZ3SpUMumJGgZGj9DJTtxZr789xBh7WVBEA_LplwJW5PbNC_h2hreKw459DZlBnyOKep1gMiyVHeokEdNgibB6B_z4hhtCR5eib1V2cwLwnRMr5FkJwqHIcyiKBtX8rBmtn41cpnkPQhWU7UoUlv6JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی دیشب:
ایران با این احتمالات قطعا صعود میکنه اگه هر ۳ تا بازی طوری رقم بخوره که ایران حذف بشه؛
فقط معنیش اینه که خدا خواسته این تیمو بزنه و تنبیه کنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=pxDigVkpiwfm1Vo1vRG-uPiq4dtD65tVabgZCQuYul0vvLmaOd_eQ5ezemmxXPnMRswwnry3qUvyknnV10AnjLzfwfmErFPozl8AGCkI6tYkwZ-LmUQ1Fk1P9A3o38izjQtymypZ22YmvTEObhWz93AYC1VVSMl6FFOEjoCVkejixeSnkcANYA8H2XEVSUDPoqC0thcKagPiPuI3iISdDvCKXf_fFxoY6zBu1q7-saoAs8DqUveBRCi6YH96gorF6gjprX_vuw0kx3fiNt89MgtUtEfBxEcgPS-SPjUjpnuCyLuGV32XA7BKqRFXqi5yzY4sucTFKrw0QLYik11dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=pxDigVkpiwfm1Vo1vRG-uPiq4dtD65tVabgZCQuYul0vvLmaOd_eQ5ezemmxXPnMRswwnry3qUvyknnV10AnjLzfwfmErFPozl8AGCkI6tYkwZ-LmUQ1Fk1P9A3o38izjQtymypZ22YmvTEObhWz93AYC1VVSMl6FFOEjoCVkejixeSnkcANYA8H2XEVSUDPoqC0thcKagPiPuI3iISdDvCKXf_fFxoY6zBu1q7-saoAs8DqUveBRCi6YH96gorF6gjprX_vuw0kx3fiNt89MgtUtEfBxEcgPS-SPjUjpnuCyLuGV32XA7BKqRFXqi5yzY4sucTFKrw0QLYik11dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=G-wgfsV-LujrcDy57YTEhD161ltu6MJlqdUQFW5C6DOxoCH94H37axKpWZ3nzWr3pJaiqWVuFPgOxiQbsNbtMUiQiAjKamkLhOdrjgNMbUSnTGEJiILRcfYgywG6ZkdMI5jmBaR7KTXg7AM_2fq6rKREAhCctIThpIATQpWgRrp6cYvx7jTUwU260iRPX9rEPphbFx1SN5pnZawvNmU7IlNVlRaO-ZOUsfw4RVXd8nozK1scle6O9Bg8B7vXfxnjEKszLqFQyW9IOm1SwOY343Ymi6WsPk7Sdd3c6IPTMc57XFfImiZgLVmpOmkP54Cfr4pF2N5fjxoATOXrFkyujw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=G-wgfsV-LujrcDy57YTEhD161ltu6MJlqdUQFW5C6DOxoCH94H37axKpWZ3nzWr3pJaiqWVuFPgOxiQbsNbtMUiQiAjKamkLhOdrjgNMbUSnTGEJiILRcfYgywG6ZkdMI5jmBaR7KTXg7AM_2fq6rKREAhCctIThpIATQpWgRrp6cYvx7jTUwU260iRPX9rEPphbFx1SN5pnZawvNmU7IlNVlRaO-ZOUsfw4RVXd8nozK1scle6O9Bg8B7vXfxnjEKszLqFQyW9IOm1SwOY343Ymi6WsPk7Sdd3c6IPTMc57XFfImiZgLVmpOmkP54Cfr4pF2N5fjxoATOXrFkyujw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
