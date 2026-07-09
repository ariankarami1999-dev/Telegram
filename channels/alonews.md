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
<img src="https://cdn4.telesco.pe/file/qRS-uAkzLeqVWn50OxhChxm-wHS6G6XWyB9bIZKZAHeLP03JKx-bm3B2CBBjCOuHv13uOO39Kya2DeGEy9QprTUHHTQ7ck2Wef4AK9Z-oGbL8u7k34kSuASUGNUhu1AQ-nWBuNjPhubPQRr-YhfVLPryQsZSCHXgxYT12kh9GA3X_Iuo0jJdWr_aGh_HcJbbBd67zhOPPttWi8d76HRNSWbtDREJy8-lXNYznHXAx6eZdkWUWApogTHg-5VyVZuiUBY502wrR1H8XWfrieFCKUDVqTtYjERZttBjiPFcWSUkfVqR936iI054xBuWmDdCRU_xve6Eob99BvFw13mjSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 924K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 22:35:41</div>
<hr>

<div class="tg-post" id="msg-132918">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری/رسانه عربی نایا: احتمالا حملات امشب کار کویت و بحرین بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/132918" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132917">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری / آکسیوس به نقل از یک مقام آمریکایی: ما در حال حاضر هیچ ارتباطی با هیچ حمله‌ای به ایران نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/132917" target="_blank">📅 22:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132916">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری / آکسیوس به نقل از یک مقام آمریکایی: ما در حال حاضر هیچ ارتباطی با هیچ حمله‌ای به ایران نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/132916" target="_blank">📅 22:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132915">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری/ العربیه: ایالات متحده در حملات امشب به ایران نقشی ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/132915" target="_blank">📅 22:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132914">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری/ العربیه: ایالات متحده در حملات امشب به ایران نقشی ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/132914" target="_blank">📅 22:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132913">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadbf3e793.mp4?token=hq-JFq1Z96aM-L_kA577PrinGqMDIjGdAOmLJ_G_vCevaizl2sVEsOmJyXw8vBzd9j70hkYKHHZZacslgJZ6kFWfgQ7EonT-rIsDlz6MUz3wxt69exbyil4jghhJ9MidVFuYOlVu4tRSeII0SiVgNl1rXvM4YF9nXezzxtef6kucLpzXUId1XkNkTuoTUTps1PYa9ATGubvdf0UPe3kML_3k4nOfmQXEbUBrH-DWo7mx2d2Ahz3S5KqvKwR1SqrMKLJ_YFWZ8poDoUdQcpXjA8slFVBTCYBuP83IxiTmMn5FZlJGvZdZZWq1r3xal7U5NfBDff7tWLETXtnd-h-diQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadbf3e793.mp4?token=hq-JFq1Z96aM-L_kA577PrinGqMDIjGdAOmLJ_G_vCevaizl2sVEsOmJyXw8vBzd9j70hkYKHHZZacslgJZ6kFWfgQ7EonT-rIsDlz6MUz3wxt69exbyil4jghhJ9MidVFuYOlVu4tRSeII0SiVgNl1rXvM4YF9nXezzxtef6kucLpzXUId1XkNkTuoTUTps1PYa9ATGubvdf0UPe3kML_3k4nOfmQXEbUBrH-DWo7mx2d2Ahz3S5KqvKwR1SqrMKLJ_YFWZ8poDoUdQcpXjA8slFVBTCYBuP83IxiTmMn5FZlJGvZdZZWq1r3xal7U5NfBDff7tWLETXtnd-h-diQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چغادک بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/132913" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132912">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
برخی منابع مدعی شدند حملات به ایران از خاک کویت انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/132912" target="_blank">📅 22:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132911">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb578e14f.mp4?token=nkKdrOklRon-zd-7B1N0KHioFPhM8CJkHMkJ5fPhSKtOrPKEaoXN09JRc9dm5w9W4KtC06QX6j2fzV2hN_XhHp7Jm0PPvwY_jba2wIXUnj7g-BRcloQrQY7GI6jMPFEVmNXdsyXvJQX4qbY4CooN1YYP1OcygDLXwSFd3_4BA7w5IyPRkSa2KDOMmE72gDNM5JirxZ4WrX5Q6crffpFDUvz3XxlhjILkcDSCf0Bi8V8P8FY8B4eDyfImora8qNwsDCDUQU7MBNlOJmT3q4wHiynuCRfURJmof4tyqtkOa5IDWgKOrn4_E1oKGthkQDS_hF5Qd246VAGbfxHd0RnO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb578e14f.mp4?token=nkKdrOklRon-zd-7B1N0KHioFPhM8CJkHMkJ5fPhSKtOrPKEaoXN09JRc9dm5w9W4KtC06QX6j2fzV2hN_XhHp7Jm0PPvwY_jba2wIXUnj7g-BRcloQrQY7GI6jMPFEVmNXdsyXvJQX4qbY4CooN1YYP1OcygDLXwSFd3_4BA7w5IyPRkSa2KDOMmE72gDNM5JirxZ4WrX5Q6crffpFDUvz3XxlhjILkcDSCf0Bi8V8P8FY8B4eDyfImora8qNwsDCDUQU7MBNlOJmT3q4wHiynuCRfURJmof4tyqtkOa5IDWgKOrn4_E1oKGthkQDS_hF5Qd246VAGbfxHd0RnO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی که گویا
منتسب
به چابهار هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/132911" target="_blank">📅 22:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132910">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
آتش‌نشانی اهواز : انفجار امشب، ناشی از نشت گاز شهری در یک ساختمان مسکونی دوطبقه در منطقه حصیرآباد اهواز هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/132910" target="_blank">📅 22:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132909">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
چند انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132909" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132908">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
مهر: تاکنون انفجاری در خارگ رخ نداده است
🔴
خبرهای منتشر شده در مورد صدای انفجار در خارگ صحت ندارد.
🔴
خبرهای منتشر شده در مورد صدای انفجار در خارگ تاکنون فاقد صحت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132908" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132907">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
چندین انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/132907" target="_blank">📅 21:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132906">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
گزارش ها انفجار در اسکله چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/132906" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132905">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
حزب‌الله لبنان اعلام کرد که ایران را در رویارویی با ایالات متحده تنها نخواهند گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/132905" target="_blank">📅 21:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132904">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
انفجار مجدد در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132904" target="_blank">📅 21:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132903">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9D6YNlDJ_Tx0tqS3lcgVfKaqre1Vh62ZKQGaAA0GFwdE_NmeOzdbfzRJsZlAQ11JQCSApoYMXBr5vDYRF6T8uopisnLNbYpCWz0reZN9NDb9edTz87eK0SmPalLUdcXfWqxbbQthhB8yN2XqVeX0vxQYXL6iYK3EYZfm5yI_ZTvXbmmgsgPeEm6NFQM_XhJ9WXrxP2EnBa8geUqKw4pewIBPdrsVc3b5BrIWaF0EjST9CNfLwiR1P8ibr8qxYC5JW-sPtoElZaoV5ABi8xKF8pRzvqgfTEfI_-5QFY4shMyVHwgOIAKAWs8046_Q5xrBBIH_bNK3RhEjq73QcpupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون فعالیت هواگرد های ارتش ایالات متحده در جنوب ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/132903" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132902">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
۴ بار صدای انفجار در اهواز شنیده شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132902" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132901">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
گزارش مردمی : 21:23  سه انفجار در چابهار شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132901" target="_blank">📅 21:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132900">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
گزارشات از انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/132900" target="_blank">📅 21:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132899">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
گزارش هایی از شنیده شدن صدای انفجار در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/132899" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132898">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نخست‌وزیر بلژیک: جنگ با ایران باید متوقف شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132898" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132897">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام آمریکایی:
ما به مرحله اجرای چارچوب مذاکرات لبنان و اسرائیل رسیده‌ایم.
🔴
کار برای نقشه برداری و شناسایی سایر مناطق آزمایشی در لبنان در حال انجام است.
🔴
اولین منطقه آزمایشی ظرف چند روز مشخص خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132897" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132896">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
هم اکنون فعالیت پدافند در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132896" target="_blank">📅 21:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132895">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02a761f84.mp4?token=Dw4sQ_EnqEq96OWngaxt_K2CZyo_fFxMQoPCVSaI7HlSRxcsAcdmfZQ0aQctXBi21iCvM91VnunU2ovfMYvM9yt9B-isBcJ1z18tbHqTRgIm3nBgMSRJpelm-YWr2thVchVYJZlQgRviEZEuhi5O6ma5I8uay-zcrBVvJZixoqWwaiC3CyzlX1tMnRVmnvQd_lb6r2ACZUimou_t9KT7G3sHURxYodjjmGQ-c_9Eeq9PpGLhmb6JNLxPsISQOY6aYRrOqjdMWGP8kmJor8yXbFohzt03jh-L98jxxs3VL6I8JnG819frd9seSt5yDCtQoMqEhsJ_8tjKWAbvytCYEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02a761f84.mp4?token=Dw4sQ_EnqEq96OWngaxt_K2CZyo_fFxMQoPCVSaI7HlSRxcsAcdmfZQ0aQctXBi21iCvM91VnunU2ovfMYvM9yt9B-isBcJ1z18tbHqTRgIm3nBgMSRJpelm-YWr2thVchVYJZlQgRviEZEuhi5O6ma5I8uay-zcrBVvJZixoqWwaiC3CyzlX1tMnRVmnvQd_lb6r2ACZUimou_t9KT7G3sHURxYodjjmGQ-c_9Eeq9PpGLhmb6JNLxPsISQOY6aYRrOqjdMWGP8kmJor8yXbFohzt03jh-L98jxxs3VL6I8JnG819frd9seSt5yDCtQoMqEhsJ_8tjKWAbvytCYEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شریعتمداری: باید یکی از خواسته‌هامون توی تفاهم‌نامه تحویل ترامپ باشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/132895" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132894">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / گزارش های اولیه از انفجار در چابهار!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/132894" target="_blank">📅 21:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132893">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt0VH0xgmLw4SVNZh9mYtBkuZPaZZSGS5doh5lOt1Hisdc7FHAtCUytjLYeHX8mnjQvPqVc3F9m1R2NZrY9y-VtlcNFy3fc0lHPkzVwVw4_bq4HTsGZRjMG0Xg_OJqkXK1PYnY9df7YwmmXzpE0ziKcuFaifgUIfRxgIcUHqZ94Yx_Y5Z5ejEN-9O0TOEFKEmnjAAX9OAWClhmHfod9rASzQ_v6jWe49ObAczO6J6v3TUqsn1myCDcL_h85xy43ikKyFqz4JkB6AdsiuH7A_uDHqD-P4xK_7a7iUiA53eQQoD1VidvXm3Tk4NugJBoGoKZH0CwUjwhdBFalBaZVy0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هدیه خاص اردوغان به سران کشورهای ناتو که در اجلاس آنکارا شرکت کرده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/132893" target="_blank">📅 21:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132892">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
اسکای نیوز عربی: اگر درگیری بین ترکیه و اسرائیل در سوریه، به عنوان مثال، رخ دهد، آیا این موضوع ماده ۵ [توافق‌نامه ناتو] را فعال می‌کند؟
🔴
مارک روته، نماینده ناتو: آقای اردوغان یک رئیس‌جمهور بسیار خردمند هستند. ایشان سال‌هاست که در این سمت حضور دارند و از قرار گرفتن در موقعیتی که از کنترل خارج شود، اجتناب خواهند کرد.
🔴
اسکای نیوز عربی: اگر آقای نتانیاهو شرایطی را ایجاد کنند که درگیری اجتناب‌ناپذیر شود، چه؟
🔴
مارک روته: بیایید در مورد آنچه ممکن است اتفاق بیفتد، حدس و گمان نزنیم، زیرا در نهایت نباید فراموش کنیم که در ۷ اکتبر ۲۰۲۳ چه اتفاقی افتاد. حمله وحشتناک حماس به اسرائیل. این حمله از طرف اسرائیل آغاز نشد...
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/132892" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132890">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558eba4f88.mp4?token=FqksGgxiIy0ZDLli4fulDtPGHFvQ67y83GI56FBiWax-f6o4JUvGIxWc2h78Cc-H7-SjnHB4VUOdcrdmZXWE4a67IJNPsd2QISqoFNUSWQntj5XiPeVCwMP7wnnhUvM6ES93HDIU_C9GbDmho88nCZB2l9FRKW8DMFuD30GkH5Zs8DVQ9k8KAbe5TsWNkUOsrucpqCwjic8oKvJq93G0yfYFvMq0KEVkPhfNt4ecTEWm7Rc3-SPGnUvM118YCSQ_GWdH8PZ2hAX03B5q7Fcj4ApVWBjeFJpW3pHJoeT4BL3N3_e9ZbZAspQNdz78BxJ2bZ9mcbnJ4TmYOC2Fq312rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558eba4f88.mp4?token=FqksGgxiIy0ZDLli4fulDtPGHFvQ67y83GI56FBiWax-f6o4JUvGIxWc2h78Cc-H7-SjnHB4VUOdcrdmZXWE4a67IJNPsd2QISqoFNUSWQntj5XiPeVCwMP7wnnhUvM6ES93HDIU_C9GbDmho88nCZB2l9FRKW8DMFuD30GkH5Zs8DVQ9k8KAbe5TsWNkUOsrucpqCwjic8oKvJq93G0yfYFvMq0KEVkPhfNt4ecTEWm7Rc3-SPGnUvM118YCSQ_GWdH8PZ2hAX03B5q7Fcj4ApVWBjeFJpW3pHJoeT4BL3N3_e9ZbZAspQNdz78BxJ2bZ9mcbnJ4TmYOC2Fq312rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آنیتا آناند، وزیر امور خارجه کانادا:
به نظر می‌رسید که آن حملات اولیه (توسط اسرائیل و ایالات متحده) به طور آشکار ناقض قوانین بین‌المللی بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/132890" target="_blank">📅 21:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132889">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای خارجه ایران و عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132889" target="_blank">📅 21:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132888">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
زمین لرزه‌ای به بزرگی ۳.۱ ریشتر ساعت ۲۰:۲۰ پنجشنبه ۱۸ تیرماه حوالی شهر استهبان از توابع استان فارس را لرزاند.
🔴
این زلزله در عمق ۱۰ کیلومتری زمین رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132888" target="_blank">📅 20:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132887">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
به گزارش کان مقامات ارشد اسرائیلی خواهان دریافت مجوز از دونالد ترامپ برای انجام حملات مستقل از سوی اسرائیل شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132887" target="_blank">📅 20:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132886">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
خبرنگار جروزالم‌پست به نقل از منابع دولتی اسرائیلی درباره احتمال درگیر شدن ارتش اسرائیلی در حملات علیه ایران خبر داده است
🔴
وی گفته که اسرائیل تنها در صورت حمله ایران به مواضع اسرائیلی یا درخواست آمریکا خواهد بود که اسرائیلی‌ها وارد درگیری خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132886" target="_blank">📅 20:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132885">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سی‌ان‌ان‌: میانگین قیمت بنزین پس از شروع دوباره حملات آمریکا علیه ایران، امروز ۵ سنت در هر گالن افزایش یافت و به حدود ۳ دلار و ۸۵ سنت‌ رسید
🔴
این افزایش، بزرگ‌ترین رشد یک روزه از ۱۶ اردیبهشت تاکنون بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132885" target="_blank">📅 20:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132884">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/708c587fac.mp4?token=rNs-YaxcIBAhph4lXR9bfIP-7_rl2EpYMOfzrtl-tRaOBZHYyI3ekK9MyecgtA7eRNtp0RP1zCnSdgfbvboWmNqCuRu2r0simvzduypZoU5IciZ1vKrZJYDL2YZ_D88oX92k6jHT7X81cs8UI7kfX8Tup7IVxeUPQj6617qqhou9jnnYo_HqEEB6wbENR0RgBCB_ElpGqHycNDHybmdor2MbJR2edqZVYr8KNVL7uSMMbC8A2Nbo34vepixDSxjB45BJL6ViQA0MPQT7K0-Ny49xHsRV7rlCe96-9rhDXzOh8oLw_gNDs-YraiEP8Qb0uHbN-dSKF7y0H35qlNAoqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/708c587fac.mp4?token=rNs-YaxcIBAhph4lXR9bfIP-7_rl2EpYMOfzrtl-tRaOBZHYyI3ekK9MyecgtA7eRNtp0RP1zCnSdgfbvboWmNqCuRu2r0simvzduypZoU5IciZ1vKrZJYDL2YZ_D88oX92k6jHT7X81cs8UI7kfX8Tup7IVxeUPQj6617qqhou9jnnYo_HqEEB6wbENR0RgBCB_ElpGqHycNDHybmdor2MbJR2edqZVYr8KNVL7uSMMbC8A2Nbo34vepixDSxjB45BJL6ViQA0MPQT7K0-Ny49xHsRV7rlCe96-9rhDXzOh8oLw_gNDs-YraiEP8Qb0uHbN-dSKF7y0H35qlNAoqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات مرز، صدراعظم آلمان: در حاشیه نشست ناتو در آنکارا، ما با دولت آمریکا به توافق رسیدیم که موشک‌های تاماهاوک آمریکایی توسط ما خریداری شده و در آلمان مستقر خواهند شد.
🔴
ما در حال پر کردن یک شکاف مهم استراتژیک در حوزه دفاعی خود هستیم، در حالی که همزمان برای توسعه سامانه‌های دفاعی اروپایی خود تلاش می‌کنیم و قصد داریم آن‌ها را در اروپا مستقر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132884" target="_blank">📅 20:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
فارس: برخی منابع خبری  مدعی شدند سوخت‌رسان‌های اماراتی در حملات بامداد چهارشنبه آمریکا به بنادر ایرانی کمک کرده‌اند/این هواپیماها توسط امارات متحده عربی اداره می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132883" target="_blank">📅 20:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
روسیه و چین در نشست شورای سازمان بین‌المللی دریانوردی، سند پیشنهادی امارات درباره تنگه هرمز را رد کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132882" target="_blank">📅 20:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132881">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری / حازم قاسم سخنگوی حماس در غزه ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132881" target="_blank">📅 20:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132880">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mA8EejL3zq_iVx2xwXW7Q2Gw2rZ0ZEdD5Kysi4f8y-2Ppx4SzWfwVuVwbPCv6h6YMedMeun4ZQdg4gMSdIIvUHLi1AP9GOKltcTQtEmLXhrn6UJeOJqJJwlEmVfTwD6B2XD1wy3W8qVfzUbWi1A4k_ZLcxTrGtsUdUFp7HVxpRRIkF4k70KTOcf_4_3KXIel2aVlZDUKpDCj5phKXfFeW0rB4KN5UmoHrwlYRZu7D8_dXyA2tJ7m0NATTR69930aR2M8thb4r3TbU_cgyQqvyeDSZONQmh6gaqdEdmjjWvyR8nlEtKEnzkaulY44If2gC2hZ9wzrI0cD5X1249Rvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون جنوب لبنان هدف حمله شدید قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/132880" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132879">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: ضمیمه محرمانه توافق اسرائیل و لبنان، به تل‌آویو اجازه آزادی عمل علیه تهدیدات در داخل «خط زرد» را می‌دهد
🔴
این ضمیمه بنا به درخواست دولت لبنان، محرمانه مانده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132879" target="_blank">📅 20:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132878">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / حازم قاسم سخنگوی حماس در غزه ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132878" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132877">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رویترز: گزینه‌های ترامپ در برابر ایران «محدود و بد» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132877" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132876">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، از مقامات ارشد بیش از 60 کشور دعوت کرده است تا هفته آینده در جلسه‌ای شرکت کنند که موضوع آن، به گفته دولت ترامپ، احیای تروریسم افراطی فرا ملی است. این موضوع، به ویژه، به گروه «آنتيفا» مربوط می‌شود، طبق گزارش واشنگتن پست.
🔴
این طرح، نگرانی‌هایی را در میان مقامات آمریکایی، متحدان اروپایی و کارشناسان تروریسم برانگیخته است. بسیاری از آن‌ها معتقدند که «آنتيفا» یک جنبش غیرمتمرکز است و نه یک سازمان تروریستی خارجی، و بنابراین، تهدید جدی بین‌المللی محسوب نمی‌شود.
🔴
سباستین گورکا، مشاور ضدتروریسم کاخ سفید، در مورد این موضوع بحث کرده است که آیا می‌توان از برچسب "سازمان تروریستی خارجی" برای هدف قرار دادن افرادی که ارتباطی با «آنتيفا» دارند، استفاده کرد. این اقدام، به گفته مقامات، می‌تواند ابزارهای تحقیقاتی بیشتری مانند نظارت را فراهم کند. برخی از مقامات دولت هشدار داده‌اند که ایجاد چنین رویه‌ای ممکن است در آینده توسط دولت‌های بعدی علیه فعالان محافظه‌کار مورد استفاده قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132876" target="_blank">📅 20:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132875">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
تکذیب انفجار در زنجان
🔴
منشأ دود آتش‌سوزی سوله بازیافت بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132875" target="_blank">📅 20:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132874">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
مدیرعامل راه‌آهن: با تلاش مهندسان شرکت راه‌آهن در کمتر از ۱۳ ساعت پس از حمله دشمن آمریکایی به خط راه‌آهن مشهد؛ یکی از خطوط بازسازی شد و به چرخه خدمات‌دهی بازگشت.
🔴
خط دوم نیز تا ساعاتی دیگر بازسازی خواهد شد.
🔴
هم‌اکنون تردد قطارها در خط بازسازی شده از سر گرفته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132874" target="_blank">📅 20:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
روسیه: رقیق‌سازی اورانیوم در خاک ایران یک گزینه کاملا عملی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132873" target="_blank">📅 19:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132872">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPr6qMAhi_YbFi9EIF_885lcfC0EZIOPKEeHD8san6wqpDThVyn5P0y67rKOeRBJbI7TmDKfU7O-sHIG0QenzkuAZmQ6pawfO9Xsp6lgbchJTtOxoX5aH-5AnBe9dKFJ95-O3g0fYSoISb0QjPI_cwK-8lhFoi0jvACv1qSrcDmQnsXVtGRA5-rqG0P9nUr8iXBgjBOBb6vuPLNxrA2QqvMxIAXvvN2K-UNQm27-odog0pl7ZF2YWGxjzHXq4idI_sVKSdVtgUXTASe5YiN0y3HJQ3mDARU2lr_UTsT-CZRtiXGfU6Db2InoVFdiZ8jRKOEH5j2_gEiCu-UFi0GXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: چگونه «سلاح طلایی» ایران در تنگه هرمز به اولویتی بزرگتر از برنامه هسته‌ای آن که مدت‌ها مورد مناقشه بوده تبدیل شد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132872" target="_blank">📅 19:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از منابع: قطر و پاکستان در تلاش هستند تا آمریکا و ایران را مجدداً به میز مذاکرات بازگردانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/132871" target="_blank">📅 19:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نتانیاهو: جنگ هنوز به پایان نرسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/132870" target="_blank">📅 19:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ندف ایال: منابع ارشد اسرائیلی معتقد هستند که جنگ دوباره در مقیاس کامل آغاز نخواهد شد، اما تنش کنونی ادامه پیدا می‌کند
🔴
آن‌ها هشدار می‌دهند که رفتار تهران بسیار غیر قابل پیش‌بینی شده
🔴
اسرائیلی‌ها می‌گفتند تفاهم‌نامه، مزیتی به ایران می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132869" target="_blank">📅 19:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568e3cc6bd.mp4?token=ObXbT6qX6-JHYoGI0fp9Ytd4aL00YRRDwqLEWXBjRn454IuV6DXCWn1W95rF1rpKf5fwOBgUvjs6MhXx6ooVHWW3BXYrlPlPJJcJfA80fzX6nPQkgEQAq4jaSDoV9oZwUFGWb8-m1eJ1dC0disMfocFEx4wSFHJkRnX5wNxGAUndDVkQz2RUddwDRgctQzW_WjbSmQN5E66Fi4T3n2-CdWUhW5lCH9gCe3tzuzNlvKVFSCto7ifIg5UD7BOBekt5noxXh_fjzXaIZPTeJrKiqXvFQwadR00CSY_oqwbP_rTLy1fmXegE_rj_jVks51F3daQB2x_8S--zKek34T8Y0LMKzlRdnpdxmfxyb3sPMVu7nWSNIVWik3uMg8x-DOubsjMbSdVxYOYSXY3c1ghzB0XTnEcdmQWWqRol9uvotBKgVefTRqbb-EKLzoNSZjST7unmY0asjz7t2aDBjvQ2vik4qtKhXxC46gyYtfWUmGByTkg3aMwGUidZUgv9FokLA9gTYVb3bf_fjap6BD8EK9RiDO0IpDKTn2I7lU5EHp9QOxNobOl3IC99QnSRgWYUz-nX2xRDnGVAmy1oVa1h1sMLrpcPstVo83BC2fiMZDj1JenpaQ7WeepFzPljcaoGmzeGtTvzW21DyRrGOmcU92QPkfl5xbv5yNGkxMTlcWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568e3cc6bd.mp4?token=ObXbT6qX6-JHYoGI0fp9Ytd4aL00YRRDwqLEWXBjRn454IuV6DXCWn1W95rF1rpKf5fwOBgUvjs6MhXx6ooVHWW3BXYrlPlPJJcJfA80fzX6nPQkgEQAq4jaSDoV9oZwUFGWb8-m1eJ1dC0disMfocFEx4wSFHJkRnX5wNxGAUndDVkQz2RUddwDRgctQzW_WjbSmQN5E66Fi4T3n2-CdWUhW5lCH9gCe3tzuzNlvKVFSCto7ifIg5UD7BOBekt5noxXh_fjzXaIZPTeJrKiqXvFQwadR00CSY_oqwbP_rTLy1fmXegE_rj_jVks51F3daQB2x_8S--zKek34T8Y0LMKzlRdnpdxmfxyb3sPMVu7nWSNIVWik3uMg8x-DOubsjMbSdVxYOYSXY3c1ghzB0XTnEcdmQWWqRol9uvotBKgVefTRqbb-EKLzoNSZjST7unmY0asjz7t2aDBjvQ2vik4qtKhXxC46gyYtfWUmGByTkg3aMwGUidZUgv9FokLA9gTYVb3bf_fjap6BD8EK9RiDO0IpDKTn2I7lU5EHp9QOxNobOl3IC99QnSRgWYUz-nX2xRDnGVAmy1oVa1h1sMLrpcPstVo83BC2fiMZDj1JenpaQ7WeepFzPljcaoGmzeGtTvzW21DyRrGOmcU92QPkfl5xbv5yNGkxMTlcWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: من تصمیم گرفته‌ام که در طول ده سال آینده، 350 میلیارد شکل به بودجه دفاعی اضافه کنم. بخش بزرگی از این مبلغ به نیروی هوایی اختصاص خواهد یافت.
🔴
در راستای این تلاش، ما همچنین یک صنعت گسترده تولید مهمات، با استفاده از فناوری‌های اسرائیلی، ایجاد خواهیم کرد. این سلاح‌ها متعلق به خود ما خواهند بود و وابستگی ما به خرید از خارج را کاهش خواهند داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132868" target="_blank">📅 19:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نتانیاهو: جنگ هنوز به پایان نرسیده است. در کنار چالش‌های قدیمی، چالش‌های جدیدی نیز در حال ظهور هستند. محورهای قدیمی در حال فروپاشی هستند و محورهای جدیدی در حال شکل‌گیری‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/132867" target="_blank">📅 19:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132866">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نتانیاهو: «حفظ برتری هوایی ما، یکی از ارکان اصلی امنیت ملی ما و کلیدی برای حفظ ثبات در خاورمیانه است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132866" target="_blank">📅 19:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132865">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
قیمت نفت و گاز در معاملات امروز کاهش یافت. نفت برنت با افت ۰.۹۴ درصدی به ۷۷.۲۹ دلار، نفت WTI با کاهش ۱.۱۳ درصدی به ۷۲.۶۹ دلار و گاز طبیعی نیز با افت ۳.۵۲ درصدی به ۳.۰۹۹ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/132865" target="_blank">📅 19:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132864">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
بلومبرگ با استناد به داده‌های کشتیرانی: ایران در ۲۴ ساعت گذشته برای تخلیه نفتکش‌های حامل ۱۱ میلیون بشکه نفت خام عجله داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132864" target="_blank">📅 19:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
شورای همکاری خلیج فارس: حملات ایران به کشتیرانی در تنگه هرمز، امنیت انرژی و تجارت جهانی را تهدید می‌کند
🔴
ما از شورای امنیت می‌خواهیم که موضع قاطعی برای تضمین آزادی دریانوردی در تنگه هرمز اتخاذ کند.
🔴
ما ایران را مسئول این حملات می‌دانیم و از آن می‌خواهیم که فوراً و بدون قید و شرط تمام اقدامات خصمانه خود را متوقف کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132863" target="_blank">📅 19:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نتانیاهو : برای هر سناریویی آماده‌ایم
🔴
یه چیز رو هم خوب می‌دونیم؛ اینکه باید همیشه آماده و قوی باشیم
🔴
قبل از هر چیز، خودمون رو تغییر دادیم  جسارت به خرج دادیم
🔴
پیش‌قدم شدیم و حمله کردیم، ثابت کردیم دست بلند نیروی هوایی اسرائیل به هر جایی می‌رسه
🔴
از یمن تا ایران، وقتی هم از دست بلند اسرائیل حرف می‌زنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/132862" target="_blank">📅 19:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132861">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کاتز: آماده‌ دور سوم درگیری با ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132861" target="_blank">📅 19:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132860">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
خبرگزاری تسنیم: بیشتر از ۱۰ میلیون نفر در مراسم تشییع در عراق شرکت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/132860" target="_blank">📅 19:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132859">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
منابع دولتی پاکستان به خبرگزاری آناتولی گفتند که پاکستان و قطر تماس‌های جدیدی با آمریکا و ایران برقرار کرده‌اند تا دو طرف حملات نظامی بیشتر را متوقف کرده و «طبق توافق» به مذاکرات بازگردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132859" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132858">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نتانیاهو: اگر ما اقدام نمی‌کردیم، ایران به سلاح هسته‌ای دست پیدا می‌کرد و جنگ هنوز تمام نشده است؛ چالش‌های جدیدی پیش روی ما در حال ظهور است.
🔴
ایران ضربه سختی خورده است و سیاست ما روشن است: ایران چه با توافق و چه بدون آن، سلاح هسته‌ای نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/132858" target="_blank">📅 18:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132857">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
اولیانوف: هیچ عوارضی برای عبور کشتی‌های روسیه از تنگه هرمز پرداخت نمی‌شود
🔴
میخائیل اولیانوف، نماینده دائم روسیه در سازمان‌های بین‌المللی مستقر در وین، گمانه‌زنی‌ها پیرامون پرداخت عوارض عبور از تنگه هرمز توسط کشتی‌های روسی را رد کرد.
🔴
اولیانوف تأکید کرد که هیچ‌گونه هزینه‌ای از سوی کشتی‌های روسیه برای تردد از تنگه هرمز به ایران پرداخت نمی‌شود.
🔴
وی در پاسخ به سؤالی درباره وضعیت کشتی‌هایی که با پرچم کشورهای دیگر از این مسیر عبور می‌کنند، اظهار داشت که ارزیابی دقیق درباره اینکه آیا ایران از آن‌ها عوارض دریافت می‌کند یا خیر، دشوار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132857" target="_blank">📅 18:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132856">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
عراقچی به فرمانده ارتش پاکستان: ایران قاطعانه مقابل هرگونه ماجراجویی آمریکا می‌ایستد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/132856" target="_blank">📅 18:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132855">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/718137081a.mp4?token=c8gqhEuQvwBttPR2QgILyO46NcWhyyyZpI5tT86i5jMyxCmmGBtJD4KjSco7YHC1oZadF_OvUJnW4JAS39BpiqBBRSXJHqlcZ8q7UefHaJHv1Uq2X6MZ3lAt2Ek1Yir1VvVFKKwOIeJ2W0FX2N4190oxIsL8ubXs2tJVB3IqdLRNdLxLnkP_SIGop5evY2TUC9mXTHFyRU3qlMZ7bHxoRE9kc3_tUi5BR_FpntBUS6PQf4fz9T_SI1J0VsRv-DElOwFmZRaGm6dInrWHNxmRs6TQhPYlpP69_9XnQg-UQqrfzf4cOqKCJKoslf6jkBvbnr9zZVO53BeJvA9FQkLl7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/718137081a.mp4?token=c8gqhEuQvwBttPR2QgILyO46NcWhyyyZpI5tT86i5jMyxCmmGBtJD4KjSco7YHC1oZadF_OvUJnW4JAS39BpiqBBRSXJHqlcZ8q7UefHaJHv1Uq2X6MZ3lAt2Ek1Yir1VvVFKKwOIeJ2W0FX2N4190oxIsL8ubXs2tJVB3IqdLRNdLxLnkP_SIGop5evY2TUC9mXTHFyRU3qlMZ7bHxoRE9kc3_tUi5BR_FpntBUS6PQf4fz9T_SI1J0VsRv-DElOwFmZRaGm6dInrWHNxmRs6TQhPYlpP69_9XnQg-UQqrfzf4cOqKCJKoslf6jkBvbnr9zZVO53BeJvA9FQkLl7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیرون کشیدن ۸۵ میلیون دلار حاصل از فساد عدنان الجميلی معاون پیشین وزیر نفت در امور پالایش عراق از زیر زمین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/132855" target="_blank">📅 18:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
مصر در آستانه هسته‌ای شدن
🔴
روس‌اتم اعلام کرد نخستین واحد نیروگاه هسته‌ای «الضبعه» مصر در ۲۰۲۸ وارد مدار می‌شود و سوخت اولیه نیز از ۲۰۲۷ تحویل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132854" target="_blank">📅 18:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
فرانسه، سوریه را به عنوان یک مسیر جایگزین احتمالی برای انتقال نفت خلیج فارس در نظر دارد، به گونه‌ای که این مسیر بتواند تنگه هرمز را دور بزند، این در حالی است که تنش‌های بین ایالات متحده و ایران در این آبراه دوباره افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/132853" target="_blank">📅 18:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132852">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMKJNG_i1jxQfdSSWsi72exG10xBKqp45g1hkyeYBxpWLepJR9eHAfdSQpa5tfaf91oWg6_E5WWEFMGTBSA3jye5eFyqH3dD0gjoYbanf2SKILie4OweB33COeIzRFVkD2u1OSt-7L5fZvzXEzH8yJ1ik6X8NR5dmoAKhIagSdsLKVOHLB-FqOwDoPFTfesHML88sy5Zgu7qnDF5PFxzia0nOvD3ujvh9S787eRoz7Bzfqm2fmDJxZz4EJViNaGiDWP9ZN0IOObRRlF9oyJV8IWUuFrM8B7RiP9jqBN9lI4toUg4UKiwgaiIykmTM02hrRsjetbqXoAfFBvLBf1gXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت
🔴
نفت تگزاس: ۷۲.۶۹ دلار
🔴
نفت برنت (معیار قیمت جهانی نفت): ۷۷.۲۹ دلار
🔴
نفت امارات: ۷۲.۴۰ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132852" target="_blank">📅 18:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132851">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu31kJTCOwkgSjO2EfmuiRHixKNZ8ntrXChihx61uUs0e-TAOKygHOMd86ATSIu5Zf58ASBihr92YPmAYnOFqb2h91lQrvhUDxl9Pd7tb_FFHz6IpZCBil50kUgLSpUNscnRvlI3SCPS9cGY72ildm9zOPh17fJNPLBaLD8-xSzeOGkUPvpPWqAvnr8Qrddm38XUjK7hmxlfbLS36LSDJQ0Ti7vjd0ad9vLQ2NGLVC8JTH6xpRfbdMs9Vs8wIDH1xRnJH2cywE8hpOMB4JHPWD70htr99BbE8QBQgoG3IYMnmbuuIz8vnqaE6ySnN1kgDKDzKaQv4Xn-CmVLC9zpxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضرغامی: در صورت تداوم تجاوزات، به کشورهای خلیج فارس اعلام کنید درب چاه‌های نفت خود را ببندند وگرنه آن‌ها را به آتش خواهید کشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132851" target="_blank">📅 18:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132850">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
بلومبرگ : قطر موقتاً برنامه‌های خود برای افزایش تولید گاز طبیعی مایع در مجتمع رأس لفان را متوقف کرده
🔴
این تصمیم پس از هدف قرار گرفتن یک کشتی حامل گاز ال‌ان‌جی قطر در تنگه هرمز اتخاذ شد
🔴
کاهش عملیات‌ها، تعداد نفتکش‌ها و کشتی‌های حامل گاز ورودی به این مجتمع
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132850" target="_blank">📅 18:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov1nx-OZMfaUjfZBsSBZdM6L-T8ov6l7mMw6VqkehjTa3eGQxgZfl27ZGvMYLb1uwM3XSZG5aVYPk0AckZKEXYg7Mdl18iz225jBuJ8Z7d71pdRXE1pEuQeUcELXDw_s4qbWJ0wZnEHYkOcLvrX2cgTrs2hPoooTpvZWIgn7nuNviJ0s_33HvODF4h3mWwPYMA7STJUGKzRVrusvwSnK5wh0eNkXrF-DpV7BSg2sYlrz6zca5pxIPjvxOnL9bmnXXfJrXK6NxpMzv6M0GQE89lehmVUdjxBDV13O32b0IkrRwxjqjOoS3kSwsBrFWt-JiQ8V1Rv0fNqkJ3NlRytf9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
در اقدامی عجیب و برگ‌ریزون؛ دولت مصر ورود لیونل مسی و خانواده‌اش رو به خاک این کشور ممنوع اعلام کرده
@AloSport</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/132849" target="_blank">📅 18:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
عمان: از اعمال عوارض برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند، حمایت نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/132848" target="_blank">📅 17:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132847">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
مقام‌های اسرائیلی به i24NEWS: برآورد فعلی این است که ایران تمایلی به کشاندن اسرائیل به این درگیری ندارد و به همین دلیل، احتمالاً حمله‌ای علیه ما انجام نخواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/132847" target="_blank">📅 17:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132846">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc73b26ab0.mp4?token=NM3v0A99wNq0cN52Zk8VWfWPNpUgLKBL4CjP-gtHN898JM40wx5oepakf_OeJf0bbgHuPwzKEoLYMcVC_P7DdzlKmFPEGKqql-gaPFQQVxJWiGo8aWFMr6PtRHVlNeQncS-8p3DuEDxrp7YWM7PwUr4PdGLuWYb90n8hL2pH2lck_sX_E5JNuehHtTbmG8LeO0xZ0FfGWL6fw06y_n4e3wM74U50ighx6kMY9ynrP5jWA0X92lcTLdsYMb97IK6ltAqEWyz7nMZImzgbtGzjxfrkpOqZMxnHW__5UwD5rWv97HKlCzNr9jKbb6A5QV_Ahv9wSbaQFkB-yjdpfhfoNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc73b26ab0.mp4?token=NM3v0A99wNq0cN52Zk8VWfWPNpUgLKBL4CjP-gtHN898JM40wx5oepakf_OeJf0bbgHuPwzKEoLYMcVC_P7DdzlKmFPEGKqql-gaPFQQVxJWiGo8aWFMr6PtRHVlNeQncS-8p3DuEDxrp7YWM7PwUr4PdGLuWYb90n8hL2pH2lck_sX_E5JNuehHtTbmG8LeO0xZ0FfGWL6fw06y_n4e3wM74U50ighx6kMY9ynrP5jWA0X92lcTLdsYMb97IK6ltAqEWyz7nMZImzgbtGzjxfrkpOqZMxnHW__5UwD5rWv97HKlCzNr9jKbb6A5QV_Ahv9wSbaQFkB-yjdpfhfoNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار «انتقام، انتقام» در مراسم تشییع، امروز در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/132846" target="_blank">📅 17:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132845">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920bba89e2.mp4?token=ul6ta06ql4J1KwlJvSx54OLxapWlaN-njs_dubu7RhlUOCJNWw1JYDHf-QBDPmrnWh34JMoOpN6ji9x5BHMXkCC1gq6azbpx58GBReysf6Jj3H52117a4hOSV_VgOOoAIZWLZWnHwix-LX5bGe9iUYQGSnmbrJBoEfIMN1NXFuS3mAEhRjU0kMdhF3iNxPyyrfP53yjyRmK3-MJfmn8e8r1oWSiUIchbfqFTVwBA-obpl7GwNJ4NoBr67ZYWTiVilWv5jycrAVoKbv7KwDEErDWmjgruTHU2iNRiVzxtbIbGZpd3Qjn9YgAgCuSav0S5mM4c3kIeS-LO-Y6cfdtt_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920bba89e2.mp4?token=ul6ta06ql4J1KwlJvSx54OLxapWlaN-njs_dubu7RhlUOCJNWw1JYDHf-QBDPmrnWh34JMoOpN6ji9x5BHMXkCC1gq6azbpx58GBReysf6Jj3H52117a4hOSV_VgOOoAIZWLZWnHwix-LX5bGe9iUYQGSnmbrJBoEfIMN1NXFuS3mAEhRjU0kMdhF3iNxPyyrfP53yjyRmK3-MJfmn8e8r1oWSiUIchbfqFTVwBA-obpl7GwNJ4NoBr67ZYWTiVilWv5jycrAVoKbv7KwDEErDWmjgruTHU2iNRiVzxtbIbGZpd3Qjn9YgAgCuSav0S5mM4c3kIeS-LO-Y6cfdtt_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیچوقت قدیمی نمیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/132845" target="_blank">📅 17:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132844">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
منابع دولتی پاکستان به خبرگزاری آناتولی گفتند که
پاکستان و قطر تماس‌های جدیدی با آمریکا و ایران برقرار کرده‌اند تا دو طرف حملات نظامی بیشتر را متوقف کرده و «طبق توافق» به مذاکرات بازگردند.
🔴
یکی از منابع نزدیک به روند میانجی‌گری گفت:
«پاکستان، همراه با قطر، با واشنگتن و تهران در تماس است تا دو طرف را متقاعد کند که خصومت‌ها را پایان دهند و طبق توافق به مذاکرات بازگردند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/132844" target="_blank">📅 17:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132843">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54633b65fd.mp4?token=BlskQsgaml5Kw7r9IQQmjxPw8XK_teoUhDpJ0eZEM1V7B8jn3--g1Eh6Zpr_qAZQK3awqQ8JJkzHK1eZjC8QKHmqih55VU6ZLPxo6zvvXUwITZEAombTo695JRvihhBUO61QTPd7WOW3TYHGj7mXgRaueuVVBVAcW6OtFFD_P-iIMkN2jMaLTt1Vxx-twUHulHwnRKuOd9Qd3JwvYO5gSD0o3ZDZqpL17JggvJsnlt6lP68mHvCGdsZh5tIw43J3k8kp8q-Zbk2FRYefRh1Tczbo3udq1v9vrLNhQV3uw7Gy8oOMkYX_iQgHaCXQw4sy9Ea8o52xr2wZGhyDoV_5tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54633b65fd.mp4?token=BlskQsgaml5Kw7r9IQQmjxPw8XK_teoUhDpJ0eZEM1V7B8jn3--g1Eh6Zpr_qAZQK3awqQ8JJkzHK1eZjC8QKHmqih55VU6ZLPxo6zvvXUwITZEAombTo695JRvihhBUO61QTPd7WOW3TYHGj7mXgRaueuVVBVAcW6OtFFD_P-iIMkN2jMaLTt1Vxx-twUHulHwnRKuOd9Qd3JwvYO5gSD0o3ZDZqpL17JggvJsnlt6lP68mHvCGdsZh5tIw43J3k8kp8q-Zbk2FRYefRh1Tczbo3udq1v9vrLNhQV3uw7Gy8oOMkYX_iQgHaCXQw4sy9Ea8o52xr2wZGhyDoV_5tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری گنده گوز شبکه سه:
به همه مقدسات قسم من اگه بتونم، خودم میرم ترامپ رو ترور میکنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/132843" target="_blank">📅 17:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132842">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
تانکر ترکرز گزارش داد:
احتمال از سرگیری محاصره دریایی ایران توسط ایالات متحده بسیار زیاد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/132842" target="_blank">📅 17:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132841">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
منابع پاکستانی:
میانجیگران برای جلوگیری از حملات بیشتر، تماس‌های جدیدی با آمریکا و ایران برقرار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/132841" target="_blank">📅 17:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132840">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3mjUQSaUj4OR61fFMZzhPQpCiE8F7VSVfuVmCxH8AmpZ39Kx0XhHyQCiAgqEqzMC2iNvoWehb2-49sP2FPEJgs7e_5xP1SkfuGjiegS5-fdpvzOGhRb9PNr0MGe129wZI041C2xt7Lh2PM1W9qDnqD93nGNuFQeW9YOe_37633i80DS8JcBDIarzqan8ZGAwusE6hZXgP096CAwfeQ7S5qGgxaqFWrg0D-IWBd2j4sdXtLzcJyKuqzru3HC_Hpi1bEIZbCndZTFvIdIHLyQA_dv0uPwazJX5GA-tjHO3Vo1yYjJKYs7Pa9Y8xppYIM6C4AlowsBw7eSwU5JdN7tIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار عبدالهی: بزودی قاتلان آقا یعنی ترامپ و نتانیاهو رو میکشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/132840" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132839">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سپاه پاسداران: مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن با ۱۰ فروند موشک بالستیک در هم کوبیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/132839" target="_blank">📅 16:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132838">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693aef909c.mp4?token=WsqOc9QAsSTBEq4yKNZXQkymMRGo9pZ7B814QuFs0_O3wcsHiete_x9dNl2Srjk_nxwFO1BdaV7areCOmdb19cO88L_Eey_SCLoF2fWn71oP2oL0bQNK359F_i8yTHKtBPntvguqAfQSS7YLZl9j5tRqC_7O7yTnp5nQiKwG2L7oq7f8gTLjeBw1VSbhHELjH6YCFTlExUfgY3MgbIGXdP07jWTtIfTKi_V_5DH6JksQJeDGyKPYjfFnadB117LmdDEzCgedP074ghZ73gxlxCwX81D2u7AD_j9buFcSwWdY7D4aiVCtg1POShDJRsc_y_c0DL3Foz_zI-EBB2f7Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693aef909c.mp4?token=WsqOc9QAsSTBEq4yKNZXQkymMRGo9pZ7B814QuFs0_O3wcsHiete_x9dNl2Srjk_nxwFO1BdaV7areCOmdb19cO88L_Eey_SCLoF2fWn71oP2oL0bQNK359F_i8yTHKtBPntvguqAfQSS7YLZl9j5tRqC_7O7yTnp5nQiKwG2L7oq7f8gTLjeBw1VSbhHELjH6YCFTlExUfgY3MgbIGXdP07jWTtIfTKi_V_5DH6JksQJeDGyKPYjfFnadB117LmdDEzCgedP074ghZ73gxlxCwX81D2u7AD_j9buFcSwWdY7D4aiVCtg1POShDJRsc_y_c0DL3Foz_zI-EBB2f7Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/132838" target="_blank">📅 16:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ابوالفظل بازگان: موشک‌های تاماهاک حدود ۲ساعت طول کشید تا به بیت برسن و چون ارتفاع پایین بود همه میدیدنش اما کسی بیسیم نزد که حداقل آقا رو ببریم زیر زمین
🔴
حتی ماهواره‌های روسیه هم دیدنش اما چیزی به ما نگفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/132837" target="_blank">📅 16:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=ZKkFlp0I-IhCQzvvxd8HiwZ6LTH8A2Ihn1IwmFxnyvrzBP7yXCYoI6N3K73mQ_mjmwL68B6Fs2diuvIhICynswdKbGkDOF833Cp3AJk1JG4cet2_pxBl0gcALEpweUgD0iiAEnjdQPnOXX2a4sMouWK3OVWZ0Svc1ZK0nRsV3iJ3ftw-RqjqOz8D9MBpQBUpxQwf9Ky_YO4BbmgZ9MSXC0YBEPywnFX6pYnxnXSA5HrPBM-H12UB8SVRPwFeq0J4vg6SGItAi1LA9m37akhiI-Xw_W3c-U0eNUTgXejUJieN_Fth6VQfyzzLJrQFznvSRRz3xpMzddXB0aSheyGRhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=ZKkFlp0I-IhCQzvvxd8HiwZ6LTH8A2Ihn1IwmFxnyvrzBP7yXCYoI6N3K73mQ_mjmwL68B6Fs2diuvIhICynswdKbGkDOF833Cp3AJk1JG4cet2_pxBl0gcALEpweUgD0iiAEnjdQPnOXX2a4sMouWK3OVWZ0Svc1ZK0nRsV3iJ3ftw-RqjqOz8D9MBpQBUpxQwf9Ky_YO4BbmgZ9MSXC0YBEPywnFX6pYnxnXSA5HrPBM-H12UB8SVRPwFeq0J4vg6SGItAi1LA9m37akhiI-Xw_W3c-U0eNUTgXejUJieN_Fth6VQfyzzLJrQFznvSRRz3xpMzddXB0aSheyGRhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
احمدی نژاد : بابا داره بهتون فحش میده،یه مرد بین شما پیدا نمیشه پاشه حداقل بگه خودتی؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/132836" target="_blank">📅 16:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132835">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKlkMHjP3t0cRES2jpyFcRTwCCD4v4ya0PAKCSgf1jUdYcVDBT4ratyQq26V162fc08g9c1D3z8gN1rpn86y81r2wnC-mhAHJp5YMP5Xa2qhTAaGNMeXGqqhWT6cm-IeSRwtoqmavd2Vhu7M4a9FAtOOxMtsKiExxfX5VnNq8pU878y5Gb7L58saz_4Ors48xs-EbvsXT5FWJqpFpT_Ra6Ecpk9-Emk2qH9RJZAHWKAnxdPBaxIf1R9ABtrkvRAMQVyuwde3op1nsfh7TSXCEkP0lyxZiVEdjGd5ZO4YiGSs8wJvK2qkLdxT6nmzW9Gm-KCIBWyO-NkuS6-WV4pOLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنایه سخنگوی فارسی‌ ارتش اسرائیل به ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/132835" target="_blank">📅 16:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132834">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22231a0a4.mp4?token=KDkktY6dysFyaFYdCkExAEyNoi08GwLh0AX7mxtlDmBUThIimBmCLeiHeuOIRIxogSCuI6tSxeaGxJWJ_hTCU3_P-e0S7ZxmAx0t0t4tI7D4Npq5OZ0a2tMnF2AwRKh2ZbAZ6yI51pyeAlw0ac_frYeoWzogOwzUPFzTWJn2YEmwvp1QkBAX9L8ffrco5Zj9iX2vOvDETY0UrMEjNca3rWEpfgD2lKLioZ7vGPstyPniIPr6zB4xEojQjzVSR2FzzLENsk_xq4-hEvfu_BGMtpWhi0nwPTB_6HU8XtsQs5YV30zx_Wln7bkz8e-iD1m3fTSbEooYkGVRhm_XNGc2xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22231a0a4.mp4?token=KDkktY6dysFyaFYdCkExAEyNoi08GwLh0AX7mxtlDmBUThIimBmCLeiHeuOIRIxogSCuI6tSxeaGxJWJ_hTCU3_P-e0S7ZxmAx0t0t4tI7D4Npq5OZ0a2tMnF2AwRKh2ZbAZ6yI51pyeAlw0ac_frYeoWzogOwzUPFzTWJn2YEmwvp1QkBAX9L8ffrco5Zj9iX2vOvDETY0UrMEjNca3rWEpfgD2lKLioZ7vGPstyPniIPr6zB4xEojQjzVSR2FzzLENsk_xq4-hEvfu_BGMtpWhi0nwPTB_6HU8XtsQs5YV30zx_Wln7bkz8e-iD1m3fTSbEooYkGVRhm_XNGc2xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قدرتنمایی
نیروی هوایی ارتش تو مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/132834" target="_blank">📅 16:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132833">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">روزی مردی مغرور، سنگی بزرگ را برداشت و کنار چاه آب ده ایستاد. مردم پرسیدند: «چه می‌کنی؟»
با خنده گفت: «می‌خواهم کاری کنم که همه از من یاد کنند.»
و سنگ را در چاه انداخت.
آب چاه بند آمد و زندگی مردم سخت شد. سال‌ها بعد، صدها مرد دانا آمدند؛ طناب آوردند، ابزار ساختند و هزار راه آزمودند، اما هیچ‌کس نتوانست سنگ را بیرون بکشد.
پیرمردی گفت:
«یک نادان، سنگ را در یک لحظه انداخت؛ هزار عاقل، که گرفتار بیرون آوردنش هستند.»
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/132833" target="_blank">📅 16:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132832">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423eb34be5.mp4?token=EQYunfjdL2q_KY4VtJsOImT1sgZgxfIQUEor8KpmfoV5ubEwhmx_qiLuRM1ryRYtu44Ceb6AZ8f3-g8jMycF12sCQmeYC2S6bBZSizwqqeu_TlGTWDiNofkiuonxKXh0VxKcvNVMPrSTwi4giFCSgYqlT8bOEQA_9b8sX32jo7SC6XPPiTmCBZODDWXR9-U60yYxmJTefrQK_gbjTw2z7Hyfbz2awbE0MEuuO2YvkwpR93MA726wdkXVfclhJp_22DgyII8ZVcYUhcegRG9Ix1AGhGRoDTEUZ4QKnfXuCP-p_bLIxP_Sck_gV5D9VxdV9cWuug0D_85lTkJNFKJleQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423eb34be5.mp4?token=EQYunfjdL2q_KY4VtJsOImT1sgZgxfIQUEor8KpmfoV5ubEwhmx_qiLuRM1ryRYtu44Ceb6AZ8f3-g8jMycF12sCQmeYC2S6bBZSizwqqeu_TlGTWDiNofkiuonxKXh0VxKcvNVMPrSTwi4giFCSgYqlT8bOEQA_9b8sX32jo7SC6XPPiTmCBZODDWXR9-U60yYxmJTefrQK_gbjTw2z7Hyfbz2awbE0MEuuO2YvkwpR93MA726wdkXVfclhJp_22DgyII8ZVcYUhcegRG9Ix1AGhGRoDTEUZ4QKnfXuCP-p_bLIxP_Sck_gV5D9VxdV9cWuug0D_85lTkJNFKJleQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: حمله به ایران مانند برداشتن سرطان از بدن شماست.
🔴
اگر سرطان را از بین نبرید، خواهید مرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/132832" target="_blank">📅 16:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132831">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
خلاصه وضعیت فعلی از علائم شوگون سالاری هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/132831" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132830">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a8caad7c68.mp4?token=Oq34XMwROHO_4ExJs1QS1Kh6FMSWibd265IO4aNuPmaE67NPckN7RO7NFlCwBK1xL6YIp84NknoSu_VOHk4c8OA550-XiknocPsctIRnRpP-4Sg9J6bXr5XEQROcNueIsqubwyEZlhntJpn9GnTmjLn10hqu6g8PsCqJZDFRs56ZlvECuGwj9EfmahuY8OQxav4GwH6h09Z3KhWqUgq60RGK1m6wtt8gtlmT9rzaWbtYbvPA9Ig9jxs45PLFDyeb2TQXdAzBNvNvVPfyAHVcxLkZLwuIL_1BN2Y5gMpM6FH-1o7di_8v5KAXmRQCngLZPoNcooe42JwpeZ7ip-uVcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a8caad7c68.mp4?token=Oq34XMwROHO_4ExJs1QS1Kh6FMSWibd265IO4aNuPmaE67NPckN7RO7NFlCwBK1xL6YIp84NknoSu_VOHk4c8OA550-XiknocPsctIRnRpP-4Sg9J6bXr5XEQROcNueIsqubwyEZlhntJpn9GnTmjLn10hqu6g8PsCqJZDFRs56ZlvECuGwj9EfmahuY8OQxav4GwH6h09Z3KhWqUgq60RGK1m6wtt8gtlmT9rzaWbtYbvPA9Ig9jxs45PLFDyeb2TQXdAzBNvNvVPfyAHVcxLkZLwuIL_1BN2Y5gMpM6FH-1o7di_8v5KAXmRQCngLZPoNcooe42JwpeZ7ip-uVcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی مطهری، نایب رئیس سابق مجلس شورای اسلامی ایران، ۲۴ مه ۲۰۲۲ (۴ اردیبهشت ۱۴۰۱):
🔴
وقتی که برای اولین بار وارد فعالیت‌های هسته‌ای شدیم، هدف ما ساخت بمب هسته‌ای بود.
🔴
اگر می‌توانستیم آن را مخفی نگه داریم و بمب را آزمایش کنیم، موضوع تمام می‌شد.
🔴
از آنجا که قبلاً شروع کرده بودیم، باید تا انتها پیش می‌رفتیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/132830" target="_blank">📅 16:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132829">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بمب اتم اگه بازدارندگی داشت که مسکو الان زیر موشک نبود! ۳۰سال پول مفت رفت تو صنعت اتمی و آخرش با دوتا بمب نابود شد و چند نسل هم سوخت و کشور وارد چرخه بحران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/132829" target="_blank">📅 16:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132828">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f696affe3.mp4?token=a-8GSqG814uPxCCq7zcIrntRYkuez0pE8HjYU6kOI1K5yEOFeS2eUawDRe-aSJbHR0FtCmoP_Zea3VZGtRPv1RhYa8-IRRzWyh2KX-lczIhuQUl9pPuBTZX8_SMMvfKVsAhWfGTaPuNtNgFUdCqdngzTL9rgpFnH7zJFfKvilHZfqNMwKuY2xxwyWqdCRij5tPDB5GJ3BiZ_jLUwo5IRWaW5dxRkbk1HSr-iz5qzJ_-Ep0aBPbBi_r0ApRonqop8eCFOO2DHJiYZyktKeZ-WHvRbs4TBcz-jr5WJQufQBELgBS_P13HZjvBitemJbC2DUV5lTDWUXJXfQoaCU2FfLQ8VzT-TiG_6xDMnPNQuHVZKh2nZ6YZZ1Xlwbs85RNc2DhL7B6sCflLQW1rGLSsa5_YuEuEJK-5lW66xla_dbfgHrvYHdMOJ2K3beuJNDv3MpzCylj_0nyu2wPuNYCRo91kVTqL_2FgtaBRjjvVTMkk4v2Ux3PooVVL7LkILiWJ1gyEUv7O1xLY9J_-mjh_R6CgU4P0OV8K48Z7wT6dnIKa2eGy1KwpV_3InywpInOjOa35SFeDWcSVFlJaNmn5Ai3uwEBfIe6XjOIWFNgQrsTpnLiwfHhefJW2k_rxWQEx8hJip7pQRhosfSw2FasIYFA0wM4hoxvv0X-nxoSP_gfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f696affe3.mp4?token=a-8GSqG814uPxCCq7zcIrntRYkuez0pE8HjYU6kOI1K5yEOFeS2eUawDRe-aSJbHR0FtCmoP_Zea3VZGtRPv1RhYa8-IRRzWyh2KX-lczIhuQUl9pPuBTZX8_SMMvfKVsAhWfGTaPuNtNgFUdCqdngzTL9rgpFnH7zJFfKvilHZfqNMwKuY2xxwyWqdCRij5tPDB5GJ3BiZ_jLUwo5IRWaW5dxRkbk1HSr-iz5qzJ_-Ep0aBPbBi_r0ApRonqop8eCFOO2DHJiYZyktKeZ-WHvRbs4TBcz-jr5WJQufQBELgBS_P13HZjvBitemJbC2DUV5lTDWUXJXfQoaCU2FfLQ8VzT-TiG_6xDMnPNQuHVZKh2nZ6YZZ1Xlwbs85RNc2DhL7B6sCflLQW1rGLSsa5_YuEuEJK-5lW66xla_dbfgHrvYHdMOJ2K3beuJNDv3MpzCylj_0nyu2wPuNYCRo91kVTqL_2FgtaBRjjvVTMkk4v2Ux3PooVVL7LkILiWJ1gyEUv7O1xLY9J_-mjh_R6CgU4P0OV8K48Z7wT6dnIKa2eGy1KwpV_3InywpInOjOa35SFeDWcSVFlJaNmn5Ai3uwEBfIe6XjOIWFNgQrsTpnLiwfHhefJW2k_rxWQEx8hJip7pQRhosfSw2FasIYFA0wM4hoxvv0X-nxoSP_gfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طاهری، مداح :
الان من شنیدم که ترامپ اومده ترکیه، همین بیخِ گوش ما، الان بهترین وقته؛
🔴
یه آدم با خایه و جیگر دار میخوایم که نماینده همه شیعیان بشه و  بره انتقام همه‌ی مارو بگیره از ترامپ بگیره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/132828" target="_blank">📅 16:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132827">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7b657271.mp4?token=XUXMIjzQ62jucQeSnZYsbSVECI6h9yg_Ha7LtoP11xVQc0-E94VCTxFq47EUaFKsdT5NViSmv_NfoD5NN-Zml9PW-KisJdlSHdZgdiQtEMwtoxsQDwQTrfp7f9C1vrUS3Lk_5fNMR9r__Uole-p9zzxBeZeYPZ8l33J30c1yeEPQ21hsb4JUUVIDmMDn-pM3npkcoPS8mcxT-AuHjaDUAmHWoyFKUtDmShE0cHmwCJZpgvtA3ltGz6zBXCitfXOMxCpIxyBpkLtpmsifDkpwvSaKKi9CotKCKGoFOeJOsnlAb4p0Cr5JyY0jiXvRKbsaDvmtNF3NBbIP8vf9eqbHaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7b657271.mp4?token=XUXMIjzQ62jucQeSnZYsbSVECI6h9yg_Ha7LtoP11xVQc0-E94VCTxFq47EUaFKsdT5NViSmv_NfoD5NN-Zml9PW-KisJdlSHdZgdiQtEMwtoxsQDwQTrfp7f9C1vrUS3Lk_5fNMR9r__Uole-p9zzxBeZeYPZ8l33J30c1yeEPQ21hsb4JUUVIDmMDn-pM3npkcoPS8mcxT-AuHjaDUAmHWoyFKUtDmShE0cHmwCJZpgvtA3ltGz6zBXCitfXOMxCpIxyBpkLtpmsifDkpwvSaKKi9CotKCKGoFOeJOsnlAb4p0Cr5JyY0jiXvRKbsaDvmtNF3NBbIP8vf9eqbHaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از مراسم تشییع در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/132827" target="_blank">📅 16:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132826">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
خبرنگار حوادث: تو تبریز دو تا پسر نوجوان ۱۴ ساله توی بازی کالاف دیوتی باهم رقابت میکردن که این بازی تبدیل به کل کل میشه و بیرون باهم قرار دعوا میزارن و اونجا یکیشون اون یکی رو با چاقو به قتل میرسونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/132826" target="_blank">📅 16:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132825">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
واشنگتن: چین در حال خرید دانه‌های سویا از آمریکا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/132825" target="_blank">📅 15:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132824">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e0d425be.mp4?token=HqikvjqLnm-DiTydoHGDx9fdGkxUlDYANcPLvfapAeg7JrLl2bFmpDgAjQQVBg2Bbt1ieOPq6VM9OIH-P6Sc4jnmSXGASNZyAwOMZNHYvcs_N3r9MreGQ0n7c1lHXtyT-dZi3hZeUwlpGSg8gKuQt8eTCnwfqdUrABcGYiE3AhJn4nlw8VlOjovntUFeHiZMHn4tUjKNI4ZibVRGXkw6laoqYysklZDbjckCzG1Spayjn9auadfCTq4HqxvT7m3M6gjjrzzlxF36EbtJbLycLya4N483V_TX7z-VFFh6HfzeAWlw6lcGUX4xffr3ISn9q4XFaI4DF5c4rwFXTqzuAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e0d425be.mp4?token=HqikvjqLnm-DiTydoHGDx9fdGkxUlDYANcPLvfapAeg7JrLl2bFmpDgAjQQVBg2Bbt1ieOPq6VM9OIH-P6Sc4jnmSXGASNZyAwOMZNHYvcs_N3r9MreGQ0n7c1lHXtyT-dZi3hZeUwlpGSg8gKuQt8eTCnwfqdUrABcGYiE3AhJn4nlw8VlOjovntUFeHiZMHn4tUjKNI4ZibVRGXkw6laoqYysklZDbjckCzG1Spayjn9auadfCTq4HqxvT7m3M6gjjrzzlxF36EbtJbLycLya4N483V_TX7z-VFFh6HfzeAWlw6lcGUX4xffr3ISn9q4XFaI4DF5c4rwFXTqzuAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
شما باید ائتلاف‌های جدیدی ایجاد کنید و روابط جدیدی را توسعه دهید، و من همین کار را در حال حاضر با هند انجام می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/132824" target="_blank">📅 15:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132823">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در پایگاه آمریکایی «ویکتوریا»
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/132823" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132822">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از فرماندهی مرکزی آمریکا (سنتکام): طی دو روز گذشته، بیش از ۱۷۰ هدف نظامی ایران را در جریان حملات هوایی مورد هدف قرار داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/132822" target="_blank">📅 15:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132821">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQG9S5vh9WUWRkyrLDZnRmZnX1l_s6VzRDGNY-tgOshGmmzvPo17tOhfNVrtR4dGn0xgpfd_klHbmgpwMqnOg2El1AFPSSdsF-ImdN5_6j-_avCgdTfViDssse5ApDIn01GKrv0_Rtn00SBxUtGr5JTO2dkQ_3QCcb1jEn7sSQd50or-QDPQ8CWwnQ3FV3vZl4DvK-j2iaALnuTlnzmsT0w__mU7TzaQWK-Usgh3o3MHe_3cjlYayIzVdWFWGTPcgNGj_us6pgfIFeehebSyd3j1lxHK2wS4c2YDaNtZI8BJS3rKbHTydgyfSpSx7dz-Gztz3T9452tdunKrKSL5Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
7 سوخت رسان آمریکایی بر فراز آب های ایرا
ن
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/132821" target="_blank">📅 15:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132820">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزیر امور خارجه بریتانیا: ایران باید از ادعای خود مبنی بر کنترل مسیرهای حمل‌ونقل دست بکشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/132820" target="_blank">📅 15:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132819">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فرودگاه اسرائیل بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/132819" target="_blank">📅 15:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132818">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNtmnD1jsVAYueuw2d5-K3-GuMwB1Cz6omRVb6-ZIortoP8TFP2MBzwuIG739T8FIK4A7odFg5M-QDqacIoKmJVXKTpcWB6Kj7prriwMW_t4ot9FPLZFV6IecqFqLJid75MSB8qxY9QdtnQ93yUA5URP4ooaxH3sruGD2eadfWMdIuE4W-2MFMqJJPxXJflKlm2ATRle6-44BeJXwAbgBIOK8m6TS63FBZ0OVvwRnviSCKq_dbn2l7DC24jufYdJbUZC4X4-ST6x5zGRHipcmb36qG8H-8_YVeXH-1D4_t8Du-CWH025ZHRJEk0-9hFFBQzAkWPJPbAWNuVni_Gapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به پهپاد شناسایی در آسمان زاهدان سيستان و بلوچستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/132818" target="_blank">📅 15:39 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
