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
<img src="https://cdn4.telesco.pe/file/ArCWpLc91Hl_Y6tNgFlCiQcSMDgcHcQ37ryjI9063OdtYjwY22pyGssT6Z16orP7taEkXclLUX78dPVWBwBpDHsKc7z7-OXYneyFNN85MbnG-IA4xK7aj7tQ5uIEgxXxm0EZ1C7OzXOH7rWbKchewtEsOK2UincHD4aXE7oz2jCVkpMnY5QIrR7m1oHcZyxktmctQxmZ-7ffPphNWTp0dfvyJhMIf4geAVUbCytsrlVlS8It11vAwLFyxdCH2Gzea7RteTj-nmU8kOLF-Gcaaihcji5NdI9TdJu0jhpNEXcC0EdhOkJssH48aHmrkz6F7awpRhJ-YIzn-Wd6cwBJFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 114K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 19:17:59</div>
<hr>

<div class="tg-post" id="msg-70929">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=rOw8cxvxALulfDQlfmfmyOEFVloRXpCWKvpc-JtIWxwVjy4Q_vzT7SFnPHFtS-3nvzu5zrX01jbv77pkqEZqih3cFDs0D9BsPD-1HLJXzSIHP33FHbtPceF1hIWWC3piAZ50qCBfITnMGjXgUqM8dckIundY0kAjFNhPhJpnPc3f0J4bg3IeQvE8O3pWld4dWQwkP0SYtHuwkuQtwZIkbOCA3MKCPrlmZyhHV5DYKtcoyl2RcVrP0Oe0DoewH8i6-N34QY0aMX5gsDwvwNCrfRru1BdPfdaVKo_pCFgu1iBYSD3l_ml7-h0VH3SGlUuVguWPasoebE0po9iMQSkGDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=rOw8cxvxALulfDQlfmfmyOEFVloRXpCWKvpc-JtIWxwVjy4Q_vzT7SFnPHFtS-3nvzu5zrX01jbv77pkqEZqih3cFDs0D9BsPD-1HLJXzSIHP33FHbtPceF1hIWWC3piAZ50qCBfITnMGjXgUqM8dckIundY0kAjFNhPhJpnPc3f0J4bg3IeQvE8O3pWld4dWQwkP0SYtHuwkuQtwZIkbOCA3MKCPrlmZyhHV5DYKtcoyl2RcVrP0Oe0DoewH8i6-N34QY0aMX5gsDwvwNCrfRru1BdPfdaVKo_pCFgu1iBYSD3l_ml7-h0VH3SGlUuVguWPasoebE0po9iMQSkGDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇳
دیروز تو دیدار پزشکیان و نخست وزیر هند، مسئولین به پزشکیان میگن پروتکل رو رعایت کن؛
🇮🇷
پزشکیان میگه :
بابا ول کن این پروتلکو
@News_Hut</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/news_hut/70929" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70928">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=f0OT0XkkxcfKi5JyXyPZKXX2JQqfNj6seBysOZOTf2e0hwo5C6YgvLenipQ65GTGulWFD_NDdFUgK6h4Oi4Ephh94flRKJyEJY18Fbp6lD4Z7PfK8tmYYh6VReP7JWHI83K8YTB6vGGphqxtvaIl3c77NTwSr9prvl8n7saWG72u5HL24-GoV9t01lxW9gupx6a0rFjB9i-bUqojAzHrcyUEfa02_bR4psBxdQJj2k044YtuTNRVHFU__A_dw-ChSK1S46PW28Vhl8zSOecDl5Hc34bhp6jGuOGAINWmCMZJAyXVS1vj8p9x7Hd2f1Hjiwmmcvu6Gnc1ddLwAYc1T2FARj2YOp8_A78H1ZL1AWlW-5-48lHXBb6GM5L2wnLQysYzF4abKT2E90fI65zC2kEUydqLR5oENrK9r1dokQ9Cs6jLmOhkT3-83-JzRKqyU4Jv-hnVNaYYY8zY6esFSj1hPT1w083MXgY5QeQyTS765ddDxzWMAam3QWvt_N5BUMLHXwfrQEkp8eMErGVS0XQyvdQmD8q17WA3tRC-3zANrHXmmIqvIrXGNS_0RQkBZxiyLMycQZ0WyVj8vBSf2iANtPNu9f0OQkj3nydSb8KUQ66ojfsHNTRv4fma9M4d1Y8x1lo8MNgxv8WZEHnDZoBgrST_0VDyaDqQtEYRSQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=f0OT0XkkxcfKi5JyXyPZKXX2JQqfNj6seBysOZOTf2e0hwo5C6YgvLenipQ65GTGulWFD_NDdFUgK6h4Oi4Ephh94flRKJyEJY18Fbp6lD4Z7PfK8tmYYh6VReP7JWHI83K8YTB6vGGphqxtvaIl3c77NTwSr9prvl8n7saWG72u5HL24-GoV9t01lxW9gupx6a0rFjB9i-bUqojAzHrcyUEfa02_bR4psBxdQJj2k044YtuTNRVHFU__A_dw-ChSK1S46PW28Vhl8zSOecDl5Hc34bhp6jGuOGAINWmCMZJAyXVS1vj8p9x7Hd2f1Hjiwmmcvu6Gnc1ddLwAYc1T2FARj2YOp8_A78H1ZL1AWlW-5-48lHXBb6GM5L2wnLQysYzF4abKT2E90fI65zC2kEUydqLR5oENrK9r1dokQ9Cs6jLmOhkT3-83-JzRKqyU4Jv-hnVNaYYY8zY6esFSj1hPT1w083MXgY5QeQyTS765ddDxzWMAam3QWvt_N5BUMLHXwfrQEkp8eMErGVS0XQyvdQmD8q17WA3tRC-3zANrHXmmIqvIrXGNS_0RQkBZxiyLMycQZ0WyVj8vBSf2iANtPNu9f0OQkj3nydSb8KUQ66ojfsHNTRv4fma9M4d1Y8x1lo8MNgxv8WZEHnDZoBgrST_0VDyaDqQtEYRSQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
بسنت درباره ایران:
ما داریم سرِ مارِ ایران را زیر خاک می‌کنیم. این مار هنوز نمی‌داند که مرده است، اما وقتی خورشید غروب کند، دیگر تکان نخواهد خورد.
کارِ رژیم ایران تمام است.
و آن‌ها هم متوجه این موضوع خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/news_hut/70928" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70927">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgZKGK0UUay_iqeJge-QQTZyR2tO717UlxcHd_RNFS-ZWSd4k_-YbpFaEEEHYLCO17xQf8FzvC9JOjM1pfAseDitnym7uC1HR_2jUF4dijiWP_vc_wsNqrNQZ0nEpwjxNsV1Dz3PhVO12KGbT_RPZ5Wj3hE_4NQ1ABLAZCm89DI7fIaJYiBWSEMaSFz4i9RQe52XVEkeTnA-aLvYgpXTEHPNk1eq1tnrC9FjpFZnTJJIwYOf4_hetf8gB1tZbhhK3pKEhtGCh9QIRF87txRo-d22o5tSk7V_fNaPg_JFmWKSYIotf15ELIxXzdkV7jLo10Ye4Eq_3B-ejAYHRlbo0HcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgZKGK0UUay_iqeJge-QQTZyR2tO717UlxcHd_RNFS-ZWSd4k_-YbpFaEEEHYLCO17xQf8FzvC9JOjM1pfAseDitnym7uC1HR_2jUF4dijiWP_vc_wsNqrNQZ0nEpwjxNsV1Dz3PhVO12KGbT_RPZ5Wj3hE_4NQ1ABLAZCm89DI7fIaJYiBWSEMaSFz4i9RQe52XVEkeTnA-aLvYgpXTEHPNk1eq1tnrC9FjpFZnTJJIwYOf4_hetf8gB1tZbhhK3pKEhtGCh9QIRF87txRo-d22o5tSk7V_fNaPg_JFmWKSYIotf15ELIxXzdkV7jLo10Ye4Eq_3B-ejAYHRlbo0HcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت درباره ایران:
ترامپ می‌خواهد یک‌بار برای همیشه به این وضعیت پایان دهد.
مردم ایران ملتی بزرگ هستند و این فرصت را دارند که به نظام [بین‌الملل] بازگردند؛ آن‌ها تحت سرکوب قرار دارند.
نمی‌توان انتظار داشت که گروهی کوچک برای همیشه قدرت را در دست داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/news_hut/70927" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70926">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-q7ZYmTqp-6B-nrOz0cwDCS2V3W6S2mv9vRCrIdoRe55k2BJEnS7W3Z2cGq5IizYH1GxtRC3rP9IHzetv4OBnzCXkI94eUpY9AYqh8ZNs5w_JJa4e2skWcEvH88eAeSpPg_8o0FtwNfFfyY7gmrgchW3pLrCk83hQ8WAj6Sq3gvIkBkGk53GtPGDVs-gaOLkNLJjMSzk0XzIfP9hz_pp09QJVs6c6abcZ2oeCValTLCofzqlJb0kdntSsflFZhj3n2Z3iLfYCa1jg3CBfCnqZpjBXQJIQfqyYrJ2sxEM8pM6srbq_zx2AqThSvGs_ve7gCbLMDEk655uNhTbXYoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
از زمان تشدید محاصره بنادر ایران، نیروهای آمریکایی مسیر ۸۴ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/news_hut/70926" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70925">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70925" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/news_hut/70925" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70924">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6oN9hO8U575DLBmi6CfCWHIfVaVw91Q3OjQ5Ccvh45YuRamlt7npT-UKaXt7WRef5gV9gY9Q04N0mqc3UNJfkZuY5pgqxYFdAPk0NcENCn7D19RGpASlpBo_wyybh6o0S9X4cALZ2uYSqU5r86pkHkIZM3fqtoQXohNxalsz3nm_v81tC7TBZCSuHqvOXlMyroqM9lFcPiB0GGaskDmQF3Kof9kfUoRfSL5YJTctDmSBWef-CaNKGa6J6PfOh2_KqWb07Lsf3JlxRIOJkYiDO-NUZSKFN7oi71YMkyuHTzBs5bmgVyLHETUGr4l4LlNctDce5FUN2qvCqoNyIdogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/news_hut/70924" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70923">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=hkCGEbhKMCm9NlSagXm6ynVnHwEur2s0bDlL9Ycym_oDippXoRLg8ZxwPufo9YrWyst5YgmTkopA-7XuzSKGchlHJ0omb3thPScBWiCa4bivHeWAT8GzXMK89AbDvzVLUa51je8Jvfa5Z4IKJ0nNC9m1MhanKUr8baCQgA0hUDwBFmOAO8gWUgzg0HE1W4r75gf_iEaX6PeASD_PMhdbpi2ffvgi7T0t-01HEJL_onjtgm4fmzNMI7GjyIs6H_iNQygE3DFNpFd7LI0_I2lxBIdfDFJF9o8cHrFv2B4a_Qj7-B0tyodvt370UFTwpp8TP3fdchU9GkNE4tlLrRNtxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=hkCGEbhKMCm9NlSagXm6ynVnHwEur2s0bDlL9Ycym_oDippXoRLg8ZxwPufo9YrWyst5YgmTkopA-7XuzSKGchlHJ0omb3thPScBWiCa4bivHeWAT8GzXMK89AbDvzVLUa51je8Jvfa5Z4IKJ0nNC9m1MhanKUr8baCQgA0hUDwBFmOAO8gWUgzg0HE1W4r75gf_iEaX6PeASD_PMhdbpi2ffvgi7T0t-01HEJL_onjtgm4fmzNMI7GjyIs6H_iNQygE3DFNpFd7LI0_I2lxBIdfDFJF9o8cHrFv2B4a_Qj7-B0tyodvt370UFTwpp8TP3fdchU9GkNE4tlLrRNtxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت وزیر خزانه‌داری آمریکا:
می‌بینیم که — باورکردنی نیست — این رژیم در کشوری که احتمالاً سومین ذخایر بزرگ انرژی جهان را دارد... بنزین وارد می‌کند. بله، بنزین وارد می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/news_hut/70923" target="_blank">📅 18:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70922">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=LQ13m9fnISKtIQC-QqPkgL7wyIDAkuxNExfMwM5d6kMKeImIQaJ7Gqn4HeBRv0sGp3URdwV-w_d2NJy6Ac4m7E6LlSqXI2uOxHrNAGckF5gOOezU6QV4WontuxwMyqa2VtXDTanGUlGM-eD9eMXx6Oe-fu_5DvMv23V6aA6HCchqUMCk9JA-cdB1wrFQogvR5ItpJ4o0pNmgX1AIvWfZvsxbCsWpRd6pT4erEkDBfs1ZzwwnVwzq1AVvpH1TIdAoS1F5wQdZZEp_G6bWYk4Od1YqqZPY8U-xNAG9b0qCr-zP77czSC5PASY62pXmGPAyXqHdlfr36CMF7F1iyc_6eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=LQ13m9fnISKtIQC-QqPkgL7wyIDAkuxNExfMwM5d6kMKeImIQaJ7Gqn4HeBRv0sGp3URdwV-w_d2NJy6Ac4m7E6LlSqXI2uOxHrNAGckF5gOOezU6QV4WontuxwMyqa2VtXDTanGUlGM-eD9eMXx6Oe-fu_5DvMv23V6aA6HCchqUMCk9JA-cdB1wrFQogvR5ItpJ4o0pNmgX1AIvWfZvsxbCsWpRd6pT4erEkDBfs1ZzwwnVwzq1AVvpH1TIdAoS1F5wQdZZEp_G6bWYk4Od1YqqZPY8U-xNAG9b0qCr-zP77czSC5PASY62pXmGPAyXqHdlfr36CMF7F1iyc_6eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
متأسفانه شعبه‌ای از یک بانک مصری در دبی وجود داشت که بیش از ۱.۸ میلیارد دلار را به سوی رژیم سرازیر کرده بود.
ما از اختیارات قانونیِ «قانون میهن‌پرستی» (Patriot Act) — که پیش‌تر از آن استفاده نکرده بودیم — بهره بردیم و در حال تعطیل کردن فعالیت‌های آن شعبه هستیم.
ما آن‌ها را مستقیماً تحریم نکردیم، زیرا نمی‌خواستیم کار به بانک مادر در مصر کشیده شود؛ اما همه باید بدانند که ما هویت آن‌ها را می‌شناسیم و خودشان هم می‌دانند که چه کسانی هستند.
احتمالاً همین هفته تحریم‌هایی را علیه یک بانک اعلام خواهیم کرد و هفته بعد نیز تحریم دیگری را اعلام می‌کنیم.
ما با متحدانمان در اینجا در حال گفتگو هستیم؛ آن‌ها همگی پای کار آمده‌اند و شاهد حمایت‌های گسترده‌ای بوده‌ایم — چه از سوی اتحادیه اروپا، بانک مرکزی اروپا، بریتانیا، امارات متحده عربی و چه از جانب بحرین.
ما قصد داریم این رژیم را از نظر اقتصادی خفه کنیم.
و همان‌طور که رئیس‌جمهور ترامپ گفت، دلیل بی‌نتیجه ماندن آن تفاهم‌نامه (MoU) این بود که آن‌ها آمادگی دستیابی به توافق را نداشتند.
وظیفه من این است که اطمینان حاصل کنم آن‌ها خواهان توافق باشند؛ و قطعاً هم خواهان آن خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/news_hut/70922" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70921">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=mqaCmvsHZ8Ryvlz1Y3RHWoPxJhGH1snwUKMJkqEaiTcSz-COsw_dkuV_xsuPtQHCGm47VK3DMERZ67PSLnvuq8j_GdLEgci1eETw9xYS3EnD97nbDs_RegS10SSWNwYoU2_AUluG29rRB2NiaYiiVUMGG-wZoadIrqe5XexQGjwomoUQWKPi5uKTPAtTAOmvXBl3W6YDCZzk6KWQ2tFtJheAPp2b7RAnatUuhUMap7vYTRFtEUQeVwGv19v-ieDNyEY-jHnnuz5Gzre11B-1SqT-sx4Ptj-IkMovEpiUUSmSxIXan4P-CRvT-zkxlYURDRaIK5TUhENmX95OC8_j5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=mqaCmvsHZ8Ryvlz1Y3RHWoPxJhGH1snwUKMJkqEaiTcSz-COsw_dkuV_xsuPtQHCGm47VK3DMERZ67PSLnvuq8j_GdLEgci1eETw9xYS3EnD97nbDs_RegS10SSWNwYoU2_AUluG29rRB2NiaYiiVUMGG-wZoadIrqe5XexQGjwomoUQWKPi5uKTPAtTAOmvXBl3W6YDCZzk6KWQ2tFtJheAPp2b7RAnatUuhUMap7vYTRFtEUQeVwGv19v-ieDNyEY-jHnnuz5Gzre11B-1SqT-sx4Ptj-IkMovEpiUUSmSxIXan4P-CRvT-zkxlYURDRaIK5TUhENmX95OC8_j5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
آمریکا قصد دارد با نقض تفاهم‌نامه، از مسیر جنوبی تنگه هرمز عبور کند و ما اجازه چنین کاری را نخواهیم داد.
پیش از جنگ، روزانه دست‌کم ۱۲۰ کشتی از تنگه هرمز عبور می‌کردند.
حتی اگر اکنون یک یا دو کشتی موفق به عبور از تنگه شوند، این وضعیت به هیچ‌وجه با شرایط پیش از جنگ قابل مقایسه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/news_hut/70921" target="_blank">📅 17:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70920">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
ما در ۱۵ ماه گذشته، در حوزه نظامی به اندازه یک دهه پیشرفت داشته‌ایم.
در هر دوره از درگیری، عملکرد و نحوه نبرد ما نسبت به دوره‌های پیشین بهتر بوده است.
نیروهای مسلح در هر دو حوزه توانمندی‌های تهاجمی و تدافعی، به مؤثرترین شکل ممکن در حال بازسازی و تقویت هستند.
این اقدامات مرهون آن است که فناوری ما بومی است و جوانانمان این کار را انجام می‌دهند؛ از این رو، نیازی به روی آوردن به دشمن نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/news_hut/70920" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70919">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=Z7xa2qFzoNRhnujo14JvPL07iNyyTI-OTlA8omQOYvap2i_koyF9IzOPMbfkgJpEE5cT5YPzrpD3mEYthY88neRCw8hR5IrDsKIROpRT3_Wyq9kyoVeeWd7qztr51jOfQZqa8qSYUQ_tbiPgY0LFO_Fu4tNC9Ter3Bxn9-WItwSTSf1zuiLkAHk2DRe_KDRsceO4B55MGT12occw56iYHxlZbQYnNGyxSG0Brkd3vzG1gE3E-3a3jhXEMkTvxYb61UxNxO7dwLkJyS-P7Bhv-xxhrGXvM_9hYW13zktwQqiMUXzGtJKOkUd1lMclSX-i4W56Kvwi6hDeGTih5Btk_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=Z7xa2qFzoNRhnujo14JvPL07iNyyTI-OTlA8omQOYvap2i_koyF9IzOPMbfkgJpEE5cT5YPzrpD3mEYthY88neRCw8hR5IrDsKIROpRT3_Wyq9kyoVeeWd7qztr51jOfQZqa8qSYUQ_tbiPgY0LFO_Fu4tNC9Ter3Bxn9-WItwSTSf1zuiLkAHk2DRe_KDRsceO4B55MGT12occw56iYHxlZbQYnNGyxSG0Brkd3vzG1gE3E-3a3jhXEMkTvxYb61UxNxO7dwLkJyS-P7Bhv-xxhrGXvM_9hYW13zktwQqiMUXzGtJKOkUd1lMclSX-i4W56Kvwi6hDeGTih5Btk_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خانم بخاطر اینکه شوهرش دائم بهش اسپنک میزده، ماهیتابه می‌بنده دور باسنش تا این دفعه شوهرش ادب بشه!
اما همچین صحنه‌ای رقم میخوره و یه شاهکار خلق میشه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/news_hut/70919" target="_blank">📅 17:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70918">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020f47777b.mp4?token=f37x45YAuGTOvluxB4CN8tYnLyguV0kUbY8WXAHSQsA6HVxYMAjBVvv8APKw6jLZjWNaXqQKJgHZxEIV-Y_ak9WxkwA08MOAOdKOw3WJVbU3LKcKpVemX_hJS7jHMbkYopzJjj3ahOyP6HBKCl_mICuY64UI4mELe2tgkraK6MCGFAtWZA6GCRmzvnLnyZiv2JX6OzpqZhvelXhH8_wC-heyw9u58zoS5Wj2Tng0xlWBaT_S4zk3c8LBAjlfkr0nnEMWXsx6iajdrj5ntOiuh_9XypIVAPEgbU3nFUHvOYug4WbRDhIeG807TTjtzdT66ElGBzzudzGE5-oyouIGEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020f47777b.mp4?token=f37x45YAuGTOvluxB4CN8tYnLyguV0kUbY8WXAHSQsA6HVxYMAjBVvv8APKw6jLZjWNaXqQKJgHZxEIV-Y_ak9WxkwA08MOAOdKOw3WJVbU3LKcKpVemX_hJS7jHMbkYopzJjj3ahOyP6HBKCl_mICuY64UI4mELe2tgkraK6MCGFAtWZA6GCRmzvnLnyZiv2JX6OzpqZhvelXhH8_wC-heyw9u58zoS5Wj2Tng0xlWBaT_S4zk3c8LBAjlfkr0nnEMWXsx6iajdrj5ntOiuh_9XypIVAPEgbU3nFUHvOYug4WbRDhIeG807TTjtzdT66ElGBzzudzGE5-oyouIGEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره اندام های تناسلی  حضرت آدم و حوا:
حضرت آدم وقتی اومد به زمین دید لای پاش یه گوشت اضافه هست و میخواست اونو بِبُره
چون حس میکرد بدرد نخوره و فقط تکون میخوره
که یهو حضرت حوا از آسمون ظاهر میشه به آدم میگه نکنه میخوای مارو بدبخت بیچاره کنی؟
حضرت حوا بهش میگه جریانو و اون منصرف میشه
آخرشم میگه حضرت آدم وقتی حوا رو دید اون گوشت دراز مانند لای پاش دید یهو تکون میخوره که فهمید نه مثل اینکه بدرد بخوره و منصرف شد از بریدنش
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/70918" target="_blank">📅 16:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70917">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=QVtFf15SOYjx48fQ5xtX8SXHgdqF-XF5ZRpDDQvp7Ll2GMDGDEgwCILLjkTA2bedgVxdi7ydP0ExvtnE_twqQCf9ialHbNFUGuKq0BPfP6p72Rqzi5xHMAtGmJiwZLrT2NshN1TKU-x7ad0l8jq7GNrBuxyZhhhSU9rojwKIJtEcRM_S_kzMA_VLfyGoKQT9xWZ6zLcrExPm2gFGJok2gdysaPDl-tzHuTJ7QggR6USgPhGknp135J_TigAGoy6pkGvRBb5s1BuL5aHU1Xu9z0yWIOWAUgve2-ukCH9-28tsWEjq6xRpZ9GutkHrDmn_LQubHqWOz5i0bdMYsBK7ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=QVtFf15SOYjx48fQ5xtX8SXHgdqF-XF5ZRpDDQvp7Ll2GMDGDEgwCILLjkTA2bedgVxdi7ydP0ExvtnE_twqQCf9ialHbNFUGuKq0BPfP6p72Rqzi5xHMAtGmJiwZLrT2NshN1TKU-x7ad0l8jq7GNrBuxyZhhhSU9rojwKIJtEcRM_S_kzMA_VLfyGoKQT9xWZ6zLcrExPm2gFGJok2gdysaPDl-tzHuTJ7QggR6USgPhGknp135J_TigAGoy6pkGvRBb5s1BuL5aHU1Xu9z0yWIOWAUgve2-ukCH9-28tsWEjq6xRpZ9GutkHrDmn_LQubHqWOz5i0bdMYsBK7ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هر روز عجیب تر از دیروز
😳
جدیدا یه عده میرن به این شکلی که می‌بینید، یه مداد دستشون میگیرن، رو زمین میخوابن، میچرخن و نقاشی میکشن!
اسمشم گذاشتن " نقاشی با بدن..."
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/70917" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70916">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e0b60b73.mp4?token=gCg8peF9gT-NUpsXfKokWqyLWniFfg6Uq6hLofKw16Eh16egCgjS9OUmvNFJEeATO65qQy9R1Zq1Wjo32DgR_AizyLsaDGJoONieolSi47nnGu1nxMqo9vxyoonfz0m4xQYEryCbwwCHJ7ZJR0oNjCK1Ud234dLrMMLyB1YTK49eLL8gkDbsOFCXHT1vqI208jPjgMOKMyl8T0vY0qutPyHkFmPh4bWnumD_pan4BJZW4oqebeYw1Yy7T_V0XUo5T5ZPtVhdNHpgy8-SqsFOFPQLuCnqujwLXWzJQ4lJHe2Dwjx8YR3LzV9FuKwZVWigR-3Jibo-xUx5qEkmr1M6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e0b60b73.mp4?token=gCg8peF9gT-NUpsXfKokWqyLWniFfg6Uq6hLofKw16Eh16egCgjS9OUmvNFJEeATO65qQy9R1Zq1Wjo32DgR_AizyLsaDGJoONieolSi47nnGu1nxMqo9vxyoonfz0m4xQYEryCbwwCHJ7ZJR0oNjCK1Ud234dLrMMLyB1YTK49eLL8gkDbsOFCXHT1vqI208jPjgMOKMyl8T0vY0qutPyHkFmPh4bWnumD_pan4BJZW4oqebeYw1Yy7T_V0XUo5T5ZPtVhdNHpgy8-SqsFOFPQLuCnqujwLXWzJQ4lJHe2Dwjx8YR3LzV9FuKwZVWigR-3Jibo-xUx5qEkmr1M6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⏺
فرماندار ماکو:
آیا دولت مقصر گرونی هست؟؟؟ خیر ما مردم مقصریم باید به خودمون رحم بکنیم
قیمت ها خیابون به خیابون فرق میکنه تقصیر ملت هست که تو ذهن هاشون فکر بدی دارن
یه عده گوشی و قلم گرفتن بر علیه دولت مینویسن نه آقا ملت به خودش رحم نمیکنه و خودمون باعث گرونی هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/70916" target="_blank">📅 15:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70913">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gr-DqO097WPWjtqg5AYfTxqyOhcG1aLr41zwFdChibxPe8Lv5iLjCaMkqSetETZdNAy9uzADuN7pPphy_Bl8YUIIeQfEGfWlZtGch-cb6cW6QjT5o2k-4Riy1tU3p-vE-rcNzgZBteT2SwdQ0Y7LhE-y_1vwBnbSt2sC8OvqLr-ON53ACy-l4XXqJm-B6HIdRJYLtNs4yx6wqZ0QueFN1vAjJ3RAimTQwGwa-r1lw5jOevHUaMfLhQoi9ByMhk67hBnRo1YeHkdfYgZ61NfhSkfGlcHsMDX7yj__5o0L_0e-s4C_nemafxs1ToY6Kc4mJiy20Ed7dtEg12ZcxzsbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNtQOg8UyzXKc85u5cwO0hoEC6sruVY3iKFkXbMgydIiJ_e1nd0S6kXOnTJwKDBJI5HWW-gXHdh0LbDH_PB1ksZh-30ILf1d7v6YZWL3I46Y8GiwGrufOZRVnV9jpCfspLJDXGzQvsD0SmXIZJi2J1FUWGZRQ-mi1jCf2ApQP8WhZ0uWL4ZSnzwkqKJoZhT9OCNJELWInp-HgAkODz4qT4sZ8AqzQsSb9Ih1g6KTSzr_EDofnvHijnH_GgKDxLuacx1MJA8jg9P4Uvn5V2dHf8qFvPbA0zLhd6D_MSGV8pZVqBab7HyCt4ewbQIeePmbBOpWx1tG8gzipRGs5DfsaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f05211278.mp4?token=Ecol3IYLhrS3XYLLuA35L9eCNdJ6RNQsZSycm2B_j2PH4awLUZTNQOMKlHDgsy38lxaJvbAJkTzdvePS_2zN_6HWCB8zUc_UX7hqBSU7Plx3Z5gcA7-aaVMswemz-9nb1YslhahJs4_FxohmQchBTVy0opiDZGD1fEQXf8gR2h7Ccd4i9sfLA2YAeYNahybjQhamMp9Adz1IGTqU8KwL1KYxQ6Q790wEf39zvrI-rel7bZs2XkurW-wanwQ0K68qTFcarUI967z-b-uY9NKvcl4VOpCxQE5hle_PGEUrh4VCW5Rby-ie_1fjcY3tpSgYA5vGMJejYJJquyFM4qnpsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f05211278.mp4?token=Ecol3IYLhrS3XYLLuA35L9eCNdJ6RNQsZSycm2B_j2PH4awLUZTNQOMKlHDgsy38lxaJvbAJkTzdvePS_2zN_6HWCB8zUc_UX7hqBSU7Plx3Z5gcA7-aaVMswemz-9nb1YslhahJs4_FxohmQchBTVy0opiDZGD1fEQXf8gR2h7Ccd4i9sfLA2YAeYNahybjQhamMp9Adz1IGTqU8KwL1KYxQ6Q790wEf39zvrI-rel7bZs2XkurW-wanwQ0K68qTFcarUI967z-b-uY9NKvcl4VOpCxQE5hle_PGEUrh4VCW5Rby-ie_1fjcY3tpSgYA5vGMJejYJJquyFM4qnpsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ز غوغای جهان فارغ!
شمال تهران
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/70913" target="_blank">📅 15:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70912">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983da46010.mp4?token=qXo9vOC4XDOc76_LKpWwpuxkzuXZEjPKMVmZ_9LMv_L2r8sQxFAWZMMrpaBEVfYd3rv0kmI2wrG2Utu1fB9dmv7sgq2mLMwC3DS5IPSP9WVbHD2TVvahAxzvJbyEIbfuiwkdV_sEcFo5zOWuTXbrKj90PNoLoFDdVFGk6WTEGKxQDL4xjRkvadudQphRIJjvJETrl9dIPeV8cl-z5B_aUy5TaAYeuhWJRhya1ztk_LnwDhcU-B8bu3bWHc0eDB2lqrSIinBvFq6AUbNK0BGi7wzyRg59FZKsHC8JCkFpHcNwj5iCX2H4IsYPxicyOQkOYeU1zSTbNg7LcY7KhnI5YjifdcihJcy4pjPewPgacBpicd4_x_OhlKQPiQH_x5y5PXlP8dzN5EACZKuKqy9HfarEQu4xVY9gwEzpyzgoWHVoRufhFdWRpYQ42EftOxl57o1DMLHNFLuX8sB8em0283hWcWmOKOXxQex0H46wKI9ZdJZrIkZX766FuIEA13iO2MUO4-LK2yy-xZ135wuCPEjByAkJRafZ-WJlGQmh55zd4fNM88dY5bgwh0t4JM2NFHehT-5acykbOr2xqD-o4UhpPfl1ldkVI3L2cC8lLxE3ntzAraeKOadQbwS45gTzCGh7_OHYrIEXFkFsxX3qKOrhBVYmtxvYQBY88i5sR2c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983da46010.mp4?token=qXo9vOC4XDOc76_LKpWwpuxkzuXZEjPKMVmZ_9LMv_L2r8sQxFAWZMMrpaBEVfYd3rv0kmI2wrG2Utu1fB9dmv7sgq2mLMwC3DS5IPSP9WVbHD2TVvahAxzvJbyEIbfuiwkdV_sEcFo5zOWuTXbrKj90PNoLoFDdVFGk6WTEGKxQDL4xjRkvadudQphRIJjvJETrl9dIPeV8cl-z5B_aUy5TaAYeuhWJRhya1ztk_LnwDhcU-B8bu3bWHc0eDB2lqrSIinBvFq6AUbNK0BGi7wzyRg59FZKsHC8JCkFpHcNwj5iCX2H4IsYPxicyOQkOYeU1zSTbNg7LcY7KhnI5YjifdcihJcy4pjPewPgacBpicd4_x_OhlKQPiQH_x5y5PXlP8dzN5EACZKuKqy9HfarEQu4xVY9gwEzpyzgoWHVoRufhFdWRpYQ42EftOxl57o1DMLHNFLuX8sB8em0283hWcWmOKOXxQex0H46wKI9ZdJZrIkZX766FuIEA13iO2MUO4-LK2yy-xZ135wuCPEjByAkJRafZ-WJlGQmh55zd4fNM88dY5bgwh0t4JM2NFHehT-5acykbOr2xqD-o4UhpPfl1ldkVI3L2cC8lLxE3ntzAraeKOadQbwS45gTzCGh7_OHYrIEXFkFsxX3qKOrhBVYmtxvYQBY88i5sR2c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
اژه‌ای، رئیس قوه قضاییه:جمهوری اسلامی از هر وقت دیگه‌ای، بیشتر آماده‌ست!
کسایی که تو ایران هستن، همگی درمورد امنیت ایران یک‌صدا هستن.
اگه باز محاسبه غلطی بخوان بکنن که آشوبی یا اغتشاشی تو‌ ایران راه بندازن، مطمئن باشن که پاسخ نیروهای انتظامی، امنیتی، اطلاعاتی و قوه‌قضائیه از قبل هم قاطع‌تر خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/70912" target="_blank">📅 14:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70911">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqO_NiRXy8nOXVwbUrmwGtnbt9Op3KDMf3BNn2BoNoyeY3WGDf8wAYT9bQ4cN-GKm-mCyGAbKMX0O-Tpu4AMP8uYEI23KZN0HW5a5pP_NTPnEUopueYlZqn6e_qrXk55JyWFBc-g7QXupcgzgYPdcbKis-QoCdlE5lHaRZqEEJ5g8St7LI9j-uTtHAQcqL8shlXbY7yXUXVWhpYir9q9QR44zHB35UKrf6kQd9v8ELFJxzxWv4yss0WwLhOxI9N6hpmg7btT6L1hnconptUwKNUOrtsqs3b87UVQjJP1YU0DHJVhCFf5pIlKePE6KTwbW2i1C2NeMv8uopcUdQ3AFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
ترامپ یک مطلب از Breitbart News را در تروث سوشال بازنشر کرد.
⏺
تیتر مطلب؛
ترامپ پس از نخستین تبادل آتش با ایران طی هفته‌های اخیر، وعده داد که «سخت» پاسخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/70911" target="_blank">📅 13:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70910">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3ff78ba6.mp4?token=cBUz6MAIOikogrXXDDs5yz3Lh9te0DhGAh21nTFt6hhzwzLP5PMfsWpMsO7BTHezbTkbz8KFxB6eug8DkXbNm6x7MIRwJ46O5XsWFwbwgQgifWDQuTixPkpeUJnwr3Ad0CjYLDJhVsniHQyTKF4Bmif6DF4bbVxYkdy1c3dpaDvsgkErFcqZ0CEnT4V77zg9kI88DSjURdCEEVdmIa21O_G2047Krkfw4-tfjRc8xA8iORmS8BRJPoaDFd02vBLL-cMBW9rjg2rna9p6ZpI4Lbe5MCpRvXDKtVLNKCKMjwbeSO0gtAqDx_s3Vh0so-4M9zCn_VCLZSejt2qc5A6WQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3ff78ba6.mp4?token=cBUz6MAIOikogrXXDDs5yz3Lh9te0DhGAh21nTFt6hhzwzLP5PMfsWpMsO7BTHezbTkbz8KFxB6eug8DkXbNm6x7MIRwJ46O5XsWFwbwgQgifWDQuTixPkpeUJnwr3Ad0CjYLDJhVsniHQyTKF4Bmif6DF4bbVxYkdy1c3dpaDvsgkErFcqZ0CEnT4V77zg9kI88DSjURdCEEVdmIa21O_G2047Krkfw4-tfjRc8xA8iORmS8BRJPoaDFd02vBLL-cMBW9rjg2rna9p6ZpI4Lbe5MCpRvXDKtVLNKCKMjwbeSO0gtAqDx_s3Vh0so-4M9zCn_VCLZSejt2qc5A6WQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کسبه پاساژ پایتخت بورس کامپیوتر تهران می‌گویند مشتری نیست و سابقه نداشته که پاساژ تا این حد خلوت باشد. یکی از آنها صراحتا اشاره کرد، گرخیدیم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70910" target="_blank">📅 13:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70909">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78ca2ad56.mp4?token=iK3CRZ_cpkuR4yec4iEiE5N_dXQbW4XF4qhvd_Xhk5Cx86BBC4CuYlZgFCzbLldpunKWOLq2SAwPj0kfF8y8PF5mLoGedKyr5GW67AYt7ik3tZcu4P9Pc0inEv_bDOiG8_2Bbc054SNDZKxSzAZAoph2qgUy641fbYLnKMwGTCu9_Q91uwKWII0GNhisZRHuDAm3UxuRpEGYOPRPoZzH2eqFE-2qsn4AtAggPcDjFHsgEJp8Cu6MQMCx-kLrfsB_dLUKniL5SDVnIe8t0KTFf4LaoixO59MOTfEQuMUpw8ejOoYMCh8L96l-EtUhNkYJC9Qd8dvJpfipb8KHbbw1Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78ca2ad56.mp4?token=iK3CRZ_cpkuR4yec4iEiE5N_dXQbW4XF4qhvd_Xhk5Cx86BBC4CuYlZgFCzbLldpunKWOLq2SAwPj0kfF8y8PF5mLoGedKyr5GW67AYt7ik3tZcu4P9Pc0inEv_bDOiG8_2Bbc054SNDZKxSzAZAoph2qgUy641fbYLnKMwGTCu9_Q91uwKWII0GNhisZRHuDAm3UxuRpEGYOPRPoZzH2eqFE-2qsn4AtAggPcDjFHsgEJp8Cu6MQMCx-kLrfsB_dLUKniL5SDVnIe8t0KTFf4LaoixO59MOTfEQuMUpw8ejOoYMCh8L96l-EtUhNkYJC9Qd8dvJpfipb8KHbbw1Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از دندونپزشک‌ها میرن میپرسن کدوم کار زیبایی تو دندونپزشکی رو نمیذاری بچه خودت انجام بده؟
به طرز عجیبی تقریبا همشون میگن کامپوزیت و لمینیت!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/70909" target="_blank">📅 12:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=iKxt8JE7Di-kRcjfEeowoUbOBk8AKKnBvbAXiLCH4-zT4SyZjCZ73-Z9RlpRfLi-M6d63ea6ZwOXzuJFPaZGzlIsFCzuOIVTJf_Qa-O3KCL49pXFPJAYhbKy3XaXmOMonea_C7nUmoa7Lo_bKUwZbwG-WeGrbtddLwTlBO-EX_GhgKnUJvpdnfJTj6u9SnJPFtsI5JogCmgfJYtlott6gB6rQ5Fcc3IKa3WR48c_e3dBdfbwgMCCiMuXjEyT_uH_lwOLT4dh0Zr5Z-g7Myb2g4MxP0JC8uNUyNCzh7HHw8pM5-TOHAZUknH33srF4r74LVCHowCgJT8-7i0PXpi5qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=iKxt8JE7Di-kRcjfEeowoUbOBk8AKKnBvbAXiLCH4-zT4SyZjCZ73-Z9RlpRfLi-M6d63ea6ZwOXzuJFPaZGzlIsFCzuOIVTJf_Qa-O3KCL49pXFPJAYhbKy3XaXmOMonea_C7nUmoa7Lo_bKUwZbwG-WeGrbtddLwTlBO-EX_GhgKnUJvpdnfJTj6u9SnJPFtsI5JogCmgfJYtlott6gB6rQ5Fcc3IKa3WR48c_e3dBdfbwgMCCiMuXjEyT_uH_lwOLT4dh0Zr5Z-g7Myb2g4MxP0JC8uNUyNCzh7HHw8pM5-TOHAZUknH33srF4r74LVCHowCgJT8-7i0PXpi5qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
غیرحضوری شدن مدارس امسال شایعه است؛ برنامه دولت به حضوری بودن مدارس است مگر اینکه اتفاقی بیافتد
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70908" target="_blank">📅 12:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70907">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/70907" target="_blank">📅 12:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70906">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAQE_gC1yvCbDD5U0BbYLpjF-Z2qWruNuaJEcbE_yfOuu_dP237tu_uiB3yoOuvAozObddbBGAcYgEsA63HVx8EQ42Bs-jcfcAhUvHOBl0aw1y0igoZNoBI1NPHnIeHCVrkttyScsTbvGVJtAtdL8tqd0FsoT6R0CcMFyf1hj_i6FDPk7X-RNTKNxT3geF4GxA3aTwfiH9xONYTpCAs2CpQGgXEmLD3MmtXqEkErHR7eOH9O6lgNqoyOBkchj_EwE3qiWzfCaFa_-f4oOkw3iDyuZXetgrko-iAxdoXt5rhEqfdPbTkJyaoop4i36Lf8Q6lJ9n7jcRmMJ0wXPZTycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش بینی کنید.
مونزا
🆚
تورینو
دورتموند
🆚
هامبورگ
کرمونزه
🆚
پارما
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/70906" target="_blank">📅 12:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70905">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e393ac5d29.mp4?token=I4IBmlZZGJlm_thhNAVdSosPH2hzhngYpJ5bPUN_AUB1nz2gR6l2NQPeXnWUYJ_-INMDXojJQ4UZn6uq-OQ_Ue_Ytv7QGebpJRaL-O3H6wZLYekdB2Ce2ACqpgy_VaoI9NXFT0acKm9UltD_V4iQgtcxrxGG7eG-txhHrsTxUMaddePe15qul0Bna0MvPyf3ub_YrvK-G1hgCzKYsnohvoVHt6vf3Ty4OtXm0SyDNvu1ZbMLlBLpiGEdRcar6f_xrhsx_vIZcshOlgO9mJZBQJMNhh9H5VLS-GjkLg-2-CRt3z67DQpybSaxwax1phXThu_3q9bY1HB5trdwQ5egyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e393ac5d29.mp4?token=I4IBmlZZGJlm_thhNAVdSosPH2hzhngYpJ5bPUN_AUB1nz2gR6l2NQPeXnWUYJ_-INMDXojJQ4UZn6uq-OQ_Ue_Ytv7QGebpJRaL-O3H6wZLYekdB2Ce2ACqpgy_VaoI9NXFT0acKm9UltD_V4iQgtcxrxGG7eG-txhHrsTxUMaddePe15qul0Bna0MvPyf3ub_YrvK-G1hgCzKYsnohvoVHt6vf3Ty4OtXm0SyDNvu1ZbMLlBLpiGEdRcar6f_xrhsx_vIZcshOlgO9mJZBQJMNhh9H5VLS-GjkLg-2-CRt3z67DQpybSaxwax1phXThu_3q9bY1HB5trdwQ5egyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ترفند یه آقا برای فروش بیشتر:
برا اینکه فروشتون بیشتر بشه پای مشتری رو بخورید
😟
اگه پاشو نداد که بخوری بپرس ازش ببین کجا رو دوس داره بخور براش.
بازار خرابه مجبورش کنید اعتماد کنه بهتون.
بعد خوردن جنستو براش معرفی کن و اگه نخرید بازم براش بخورید.
بعد مشتری میگه هروقت بیام همیشه اینجوری سرویس میدی و اینجوریه که فروشتون میره بالا
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70905" target="_blank">📅 12:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70904">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=c9jMz_4Pqwj6YGX4K8YhHPs64eVnUprSXLPfgNYAd88-44SrP_cRJAenzfHTLQperHPLXKqIte9dpc18QPNxU1-g-2PV3Tm-38RlQ86XH7IiADFYQCiMmjKe3B3R93g8QwUvjroALYzxUNrHWXeijs6LUDBm3DmdPjtvyNznrM9CgJvRqnATCU0ORne0DGdOnSd7WU_Ixjr_eWWO33UKUF1MoXNVgiXFwhxz4NNVNio8QC69_45dZgSuVn8Ct-gZmcLqTmEI423KwyZWQRL_ptMj8CfEYOx7z6D6qhlXBWjboml7ugDZzSBRNAaPZAIPIzIS3Jz0kN5LzwjM6NG-iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=c9jMz_4Pqwj6YGX4K8YhHPs64eVnUprSXLPfgNYAd88-44SrP_cRJAenzfHTLQperHPLXKqIte9dpc18QPNxU1-g-2PV3Tm-38RlQ86XH7IiADFYQCiMmjKe3B3R93g8QwUvjroALYzxUNrHWXeijs6LUDBm3DmdPjtvyNznrM9CgJvRqnATCU0ORne0DGdOnSd7WU_Ixjr_eWWO33UKUF1MoXNVgiXFwhxz4NNVNio8QC69_45dZgSuVn8Ct-gZmcLqTmEI423KwyZWQRL_ptMj8CfEYOx7z6D6qhlXBWjboml7ugDZzSBRNAaPZAIPIzIS3Jz0kN5LzwjM6NG-iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بسنت، وزیر خزانه‌داری آمریکا:
تنها چیزی که برای رهبرانِ ایران مهمه اینه که سرشون به گردنشون چسبیده بمونه [ زنده بمونن ].
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70904" target="_blank">📅 11:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70903">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d67cce6282.mp4?token=LQ6u2InwIu-NY3IHhl2OPV07oUGrzgbgyBybSR1t0ja2sgmFBPLZJt5__gQu25gjZVyEBXGloJf8w4be6izBdTeA1Vi3nFPh5VSM7MNNlPUQzVx8tDPLhoqr7qbNTSh7X4GvOcJxb4ZIlvmJO0t02NeZt5kGKORUKSeau132Ynw7GqFMRdYdmb5VboLGhHwJFcCOd2U1YAD9uddpM0K4g29iSDBY6CtkU05Gnv6S-Qv1jBqD-cBP2Es06KA87w0vuMAwI4M5LZ4Hl-gg9_AuTkrUVFUcLlbo4C9hm_Ot13lpCn1PkoYJpSzQXp6-VOVXmGVeyAJUalBC4h54bR-Ixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d67cce6282.mp4?token=LQ6u2InwIu-NY3IHhl2OPV07oUGrzgbgyBybSR1t0ja2sgmFBPLZJt5__gQu25gjZVyEBXGloJf8w4be6izBdTeA1Vi3nFPh5VSM7MNNlPUQzVx8tDPLhoqr7qbNTSh7X4GvOcJxb4ZIlvmJO0t02NeZt5kGKORUKSeau132Ynw7GqFMRdYdmb5VboLGhHwJFcCOd2U1YAD9uddpM0K4g29iSDBY6CtkU05Gnv6S-Qv1jBqD-cBP2Es06KA87w0vuMAwI4M5LZ4Hl-gg9_AuTkrUVFUcLlbo4C9hm_Ot13lpCn1PkoYJpSzQXp6-VOVXmGVeyAJUalBC4h54bR-Ixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حمید رسایی:
هم‌راستایی من با اسرائیل در مسائل مهم کشور(جنگ و مذاکره) مثل داستان دویدن یوسف و زلیخا به سمت در است.
زلیخا برای گناه می‌دوید، یوسف برای دوری از گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70903" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a64b63295.mp4?token=QUsl_HM68wDoDmKOSVv0jutt_Z8nvezuSMcBvFNAXXDoVBLb_YIkOgE_u1xj0QnmNOTM6MeoNhlhfXbshPwhGG9ez8nDmh1r2BJnFamHkBzJCcO0PncwGIZ4QuqNTGv8_-2LswCEuSca2fBwOfxgwG6FDngKudW3frkghVB0rX5oNLyHiNhzZ82bbfSICLUuvtNHoNAm9bNfMoX_EvnP0J4R1Wo8MSClEzR1jXZrKq47HFcEz-46k_U-tEsKqvA_ereRZFQtOqiNqP7ZEH3ovpchx9KJZierkOH8t0SRHGRVOr0bCDx6ZeNEKnn9LjPk5u4YbxGAHfk_PYeflNRkuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a64b63295.mp4?token=QUsl_HM68wDoDmKOSVv0jutt_Z8nvezuSMcBvFNAXXDoVBLb_YIkOgE_u1xj0QnmNOTM6MeoNhlhfXbshPwhGG9ez8nDmh1r2BJnFamHkBzJCcO0PncwGIZ4QuqNTGv8_-2LswCEuSca2fBwOfxgwG6FDngKudW3frkghVB0rX5oNLyHiNhzZ82bbfSICLUuvtNHoNAm9bNfMoX_EvnP0J4R1Wo8MSClEzR1jXZrKq47HFcEz-46k_U-tEsKqvA_ereRZFQtOqiNqP7ZEH3ovpchx9KJZierkOH8t0SRHGRVOr0bCDx6ZeNEKnn9LjPk5u4YbxGAHfk_PYeflNRkuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مجددا در سراسر کشور، حجاب‌بان و گشت ارشاد راه اندازی شده، توی بازار تهران حجاب‌بان گذاشتن و هر کس بی‌حجاب باشه، بهش گیر میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70902" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f7c0f48e0.mp4?token=mBxlQTnPygzTyUNAVdZ4MOjW4pwpEbchSe1iU8w3BqY2vVVf2BXsVyK055XxWD7bSUXVf9cqzl6YBCP2dMec7hETYlhYcR1pLEWLspbMwQ_q4gp3h9dsHbeVrOIay0AOONWBXKiqAPWnm5jijp2Yfmz7EsKcv90oHpde3ZVu5CutIGPglxILTVHbaorHsxdLSaGD_R0P6DgumIZtTfjSpK6XwJmMagUTrQxtB23FJLolmKF-pzRDjqfQemBwX_d3knfMFH889OBfr9jPobxs9caGIH5vwFEZDjxWWd48lzj_Ho9ENzMXa1yx_2zD6ZgcfgJPXtnbfn13n59kW2QLLg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f7c0f48e0.mp4?token=mBxlQTnPygzTyUNAVdZ4MOjW4pwpEbchSe1iU8w3BqY2vVVf2BXsVyK055XxWD7bSUXVf9cqzl6YBCP2dMec7hETYlhYcR1pLEWLspbMwQ_q4gp3h9dsHbeVrOIay0AOONWBXKiqAPWnm5jijp2Yfmz7EsKcv90oHpde3ZVu5CutIGPglxILTVHbaorHsxdLSaGD_R0P6DgumIZtTfjSpK6XwJmMagUTrQxtB23FJLolmKF-pzRDjqfQemBwX_d3knfMFH889OBfr9jPobxs9caGIH5vwFEZDjxWWd48lzj_Ho9ENzMXa1yx_2zD6ZgcfgJPXtnbfn13n59kW2QLLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر ماشینش رو داده بود دست دوس دخترش و داشت بهش آموزش میداد که این شاهکار خلق شد:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70901" target="_blank">📅 10:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedadf0ba9.mp4?token=vOjk7WN8vGCM2CJhDMYh47lBZGom7masuSAmhHyPtlTJNw-wPjOAjNFnVSdWuQwwcbIXss_ruPQp2s5i7_B9xvIvl7cVz6Wx5WkV2V7hKj-uAVS6N7IxPpJkvg5XivPMgadM8q_-M2684AsGUXenm7v4wzPiLDD1bFb6NJvZvhdR6TVeCaKnhNJjb0RSRfyJpYDkz0okqBexr8N5-rBVQqfhm26lAyAfbwrPDV7ABciJZHgsuf-HUH6n4putnQtPp41Aw--5fRBXoJp43xWpXfoXrpMJ2u1dYeTqhKdeYDXdZ1ew4RxViiFxRvq8ZN87aGDc2_3tZsWC_UHywocsFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedadf0ba9.mp4?token=vOjk7WN8vGCM2CJhDMYh47lBZGom7masuSAmhHyPtlTJNw-wPjOAjNFnVSdWuQwwcbIXss_ruPQp2s5i7_B9xvIvl7cVz6Wx5WkV2V7hKj-uAVS6N7IxPpJkvg5XivPMgadM8q_-M2684AsGUXenm7v4wzPiLDD1bFb6NJvZvhdR6TVeCaKnhNJjb0RSRfyJpYDkz0okqBexr8N5-rBVQqfhm26lAyAfbwrPDV7ABciJZHgsuf-HUH6n4putnQtPp41Aw--5fRBXoJp43xWpXfoXrpMJ2u1dYeTqhKdeYDXdZ1ew4RxViiFxRvq8ZN87aGDc2_3tZsWC_UHywocsFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇳
خب، این آقا سانت رامپال، رهبر یه گروه تو هنده که پیروهاش اونو خدا می‌دونن
.
این آقا برای خودش یه اتاق شیشه‌ای مجهز به کولر درست کرده تا وقتی اعضای فرقه میان پیشش و پاش رو می‌بوسن، آقا گرمش نشه و عرق نکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70900" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d124e793.mp4?token=trkISie1YPVvdlf9XJ0HlzQV2THV6_l3aj8WexoXsOlgNYs0eiso5gHu2Ql-ki210enkDEe_2QONi1ycJIppIgUOpso05EhNDZ84_o3C6x6C3e1OtrbFSZGLxtxcrDEdyYjA7qj0_4cHbCkXzVpF1hGZ4X9SG67aTTBFO8g8TUD5-58I2zx619DIslkNomrXo40cd1-eBMjSIYZysFJJApJSb4tYyjnQw6dAAsg21WMiHooyEHarmSac0zYPJvALu8lcnAPw0yp0h0IT9o-MIvnDYg3GEHdmMlDkg4MtKTzDjKIglniq8CUo0j-gjXi7JUlCXmxR-7vq1UdaKuuccw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d124e793.mp4?token=trkISie1YPVvdlf9XJ0HlzQV2THV6_l3aj8WexoXsOlgNYs0eiso5gHu2Ql-ki210enkDEe_2QONi1ycJIppIgUOpso05EhNDZ84_o3C6x6C3e1OtrbFSZGLxtxcrDEdyYjA7qj0_4cHbCkXzVpF1hGZ4X9SG67aTTBFO8g8TUD5-58I2zx619DIslkNomrXo40cd1-eBMjSIYZysFJJApJSb4tYyjnQw6dAAsg21WMiHooyEHarmSac0zYPJvALu8lcnAPw0yp0h0IT9o-MIvnDYg3GEHdmMlDkg4MtKTzDjKIglniq8CUo0j-gjXi7JUlCXmxR-7vq1UdaKuuccw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی تبدیل به حکومتی شده که نه فقط مشکلات مردم رو که وظیفه یه حکومته حل نمی‌کنه، بلکه خودش تبدیل به یک کارخونه تولید مشکل برای مردم شده.
تقریباً اون ده پونزده وظیفه اصلی که حکومت‌ها انجام میدن در ایران انجام نمی‌شه.
و بر خلاف اونا حکومت جمهوری اسلامی تبدیل شده به یه جایی که روزانه برای مردم تولید مشکل می‌کنه. شده کارخونه مشکل‌سازی. شده حکومتی که مشکل‌ساز است نه مشکل‌گشا.
مهم‌ترین دلیلی هم که مردم ایران از این حکومت متنفرند و می‌خوان سریع‌تر سرنگونش کنن همینه
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70899" target="_blank">📅 09:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0W7PVA2YbL4Ug8Dko3mOUXtq9u5Cs4NXhA7ys7st2eRNpzBppFToPIaBPxNePinndyEa5lHYlvPAKyKEdBYbGQ8xxToJ98a3JH-AFJsc0DqBT6R6rS2wFHiY6aAcC_WMU-Y0M_-EON61v5I9FGpzAgB1EOGpxlBXAMZANKim7GyFDx-S7tHJWlHTn6iYc6Mhm4miUepRxn9VR2Wspj6KHSXSSG5IDWSiw7ROHjFYWRHSt4bNPt_n-UQeTo33MtqMxjke7Iu_W6cklRGTY9Ff97rA6PK-l_RkipY8RXVsA0kzkmnc1YkGFWFsZlCPFstIUZA_LtLOqktnT7DO9HuwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سه موشک از سیریک استان هرمزگان به سمت شناور ها در تنگه هرمز شلیک شد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70898" target="_blank">📅 08:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70896" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70896" target="_blank">📅 01:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70895">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJccSCigVhEyuYlJcsCsTF9I80Ss3jqBn7NHBTSPRi9HByE-rNoHfZc7dhd7Xa0IkUMyW-Z-jc6qQlKobC-iakz776M6qfpyVtT7zmH56zCvjei-IptKiofFh7Ef11O_w-fOqlwUKun0z411oZKODZ9oOlXZXr71mGBxnVnM4xyYl0ZLo2E6iCxbpJn_I3HKdYjRkuQl26-ii2hqmlsB8l6Ot0yaP790llsltgVNxEA31XvETi0rb12MP5Q5sIpDXF_WFQ3MxwaoyDoQB562sn8ahfOLSPCrRb2hER70P_eXCLNDR-GEJxnNkOeW0Xr9FIOmWpAjBLJRO51O5fL7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70895" target="_blank">📅 01:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70894">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سه موشک از سیریک استان هرمزگان به سمت شناور ها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70894" target="_blank">📅 00:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70893">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):  گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است. به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70893" target="_blank">📅 00:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej74DN8cP6aB2fiz6NmBzzXFPpgDh_ZQ2NMXcXTxpnS5BoJ3oDBLPCzHp5bv40SHV6tDs59WxbVyah73TeeAHrR9AUBgCQMbvhobwr415kY0WSpcK36RL6CJ0guMLRnn563QvG5KFkFzs3NKKhgsK6iBZ99e50xEK3atKHwo0EW7RgEkS9cT7U4QRgtoTxJ5xFJL6CAXuWBI4SOELfMnfopO1a_TrEzt-HdYKVAd5G_7KE0AksKJP1R5MAytqVe2dBw5200gutDQ3DSEPsOhlSkT0j1imaBchPKxsOpJekWc_4aZJMCBwbZUgBSLGweQo1DgnMGFj_zN1NHshNxGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)
:
گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است.
به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار باشند. مقامات ذی‌ربط در جریان موضوع قرار گرفته‌اند و تحقیقات در این خصوص ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70892" target="_blank">📅 00:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70891">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=ArB0VrhpI0NbPJgqwG5ZpVnD0Z2kXfVKHka1x6otFylFOzjfeI1bv7z4VOMgVGhQ4Kkv4QJaZlC92yZlYEsiYzpPz0iuU6bfGBGnRVv4mkzHDIXsXi0EskpwoFeJQSnDoH47CNDjcR7PCxtmcKx2bqgjl0Ls7zXvGFEdWOMikJLdhF1XVzi0D98eE1wfs8zkH5pVjhLgcjnKnOllATFoDmFF26FDtbIjA4eD_mlJylYMqWAZVNC_2PaeUbw9P8RnZD6HLQvyT8FqAGxwrNnNEYPB9bs5AqIF698VvoJHt1WNTArTGCWNb9Ja2NsEJ2irJR9BdHLi0dLYHeUFw7TyIxCqXq8A3H19RiWaA5iDrCDHpoAdAPlUq_WpssmfRmo8FuVXu81AttRjDkJUMoL-ysYAIV5xJfNAHznBjlzG99-kZvovqYK0ZBzX3o0UTza5AMKFNwpYCmX1oGTy_U_4zAJ_XZPiQge8wQNDstph_66zUQuDHwsVr0G1ypTM2dzqgZuB_5eVisGLH1Lr5Drk7-_JtX4K5Nyfr0A0iT_eY3pvDS2oOr-lP62umu8K1WfrBfA7G6VoLXK5VerxYKLZB5aUDIUH81dNtBcuG4y48krrOzlmEvvbcNvv61ssDQ7PjkZDp4hnyhQkwbc_6s80czgDm5KDxCd18VI15XHspM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=ArB0VrhpI0NbPJgqwG5ZpVnD0Z2kXfVKHka1x6otFylFOzjfeI1bv7z4VOMgVGhQ4Kkv4QJaZlC92yZlYEsiYzpPz0iuU6bfGBGnRVv4mkzHDIXsXi0EskpwoFeJQSnDoH47CNDjcR7PCxtmcKx2bqgjl0Ls7zXvGFEdWOMikJLdhF1XVzi0D98eE1wfs8zkH5pVjhLgcjnKnOllATFoDmFF26FDtbIjA4eD_mlJylYMqWAZVNC_2PaeUbw9P8RnZD6HLQvyT8FqAGxwrNnNEYPB9bs5AqIF698VvoJHt1WNTArTGCWNb9Ja2NsEJ2irJR9BdHLi0dLYHeUFw7TyIxCqXq8A3H19RiWaA5iDrCDHpoAdAPlUq_WpssmfRmo8FuVXu81AttRjDkJUMoL-ysYAIV5xJfNAHznBjlzG99-kZvovqYK0ZBzX3o0UTza5AMKFNwpYCmX1oGTy_U_4zAJ_XZPiQge8wQNDstph_66zUQuDHwsVr0G1ypTM2dzqgZuB_5eVisGLH1Lr5Drk7-_JtX4K5Nyfr0A0iT_eY3pvDS2oOr-lP62umu8K1WfrBfA7G6VoLXK5VerxYKLZB5aUDIUH81dNtBcuG4y48krrOzlmEvvbcNvv61ssDQ7PjkZDp4hnyhQkwbc_6s80czgDm5KDxCd18VI15XHspM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا استفاده از سلاح هسته‌ای علیه ایران را منتفی دانسته‌اید؟
🇺🇸
ترامپ:
من هرگز چنین حرفی نمی‌زنم، اما پاسخ «بله» است. هیچ دلیلی برای آن وجود ندارد. چه سوال احمقانه‌ای. آن‌ها از نظر نظامی کاملاً شکست خورده‌اند.
من آن‌ها را شکست داده‌ام، آن‌وقت باید علاوه بر آن از سلاح هسته‌ای هم استفاده کنم؟ چه سوال احمقانه‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70891" target="_blank">📅 23:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70890">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=N6eH-m2CU3Dcf81pAfaVeh5f7SsAQZcL6Fw21M8W1N3snpYhlV-EltiB_69ZIcN6toSCVjpAy_lTht2ZMgmW27bkkq8jzE96YJe2UlABa3kzcWYoNGgeiRhL3LfShicRJbNr23OdEYXs8Og0cQPApWAyfIYISq7uJ4Vh22-qQt3PXF2u6UoWzKlgweEqEkExllovBKRUhrVciiQQoxNHJAO6HimkgmoaA1TTl6csZB15B5j8xVsG541r_blU_P8LtcHqcLMN2IPWe3qEbX2-SXRCVzm_2W6MUbQHyk9kAT2rwZKs-r4s3yZrdLlkI068wOU3VzJFs5TpvMKajfSQtwusDr4rjqjMNFYqFT-DbCJAvOmiQnq7bAkJtfCXS127lCiopQ65pB9ctGYh4obIfYOoxfsXtP2zJ2-y1fFUjeksdUnx3Ye_R_sn7lqCe6ysxHb_tpHB2OXG0cv53RzLtghIs6Hbx2gpmDPblWHBIfoOtc-xZMHHoRtwiPEnPDUlkjfFHMQNQNaDPE0KVU5VYhH8j3gKy6r7OycrNZnC1prPqcMx-tLM6jSW4tJqMNDnnhxdrNquodPEzcevg8c9R4-AI0xijnykti6XdGFbmuSJVpxm8Nf0jdLogigXDNgZ5e_lVt0rovaInEO5VBFGw6buPpB7J65t4n6opB48lHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=N6eH-m2CU3Dcf81pAfaVeh5f7SsAQZcL6Fw21M8W1N3snpYhlV-EltiB_69ZIcN6toSCVjpAy_lTht2ZMgmW27bkkq8jzE96YJe2UlABa3kzcWYoNGgeiRhL3LfShicRJbNr23OdEYXs8Og0cQPApWAyfIYISq7uJ4Vh22-qQt3PXF2u6UoWzKlgweEqEkExllovBKRUhrVciiQQoxNHJAO6HimkgmoaA1TTl6csZB15B5j8xVsG541r_blU_P8LtcHqcLMN2IPWe3qEbX2-SXRCVzm_2W6MUbQHyk9kAT2rwZKs-r4s3yZrdLlkI068wOU3VzJFs5TpvMKajfSQtwusDr4rjqjMNFYqFT-DbCJAvOmiQnq7bAkJtfCXS127lCiopQ65pB9ctGYh4obIfYOoxfsXtP2zJ2-y1fFUjeksdUnx3Ye_R_sn7lqCe6ysxHb_tpHB2OXG0cv53RzLtghIs6Hbx2gpmDPblWHBIfoOtc-xZMHHoRtwiPEnPDUlkjfFHMQNQNaDPE0KVU5VYhH8j3gKy6r7OycrNZnC1prPqcMx-tLM6jSW4tJqMNDnnhxdrNquodPEzcevg8c9R4-AI0xijnykti6XdGFbmuSJVpxm8Nf0jdLogigXDNgZ5e_lVt0rovaInEO5VBFGw6buPpB7J65t4n6opB48lHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شرایط وحشتناک بازار با قیمت بالای دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70890" target="_blank">📅 23:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70888">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbctqFPA90lfWMHr6-2HjojuAFg-rzVsFWg2XX8TtPVWGYYiw_tEn4y9WmcOPXJ4RafFf7M99-8wUliWmNVZsxKdjin_kD4c6px4u056v3BxFCCL52Tk9f8309oKF5HV2Ll296Ctt3oWoqBeOC027M_hyS58YtmGh2vB274QxGRJraNJ6E9W8JC1MLub6stTlM6L4TO6wMYqO4NONxuNMOgD3MqMzUBfo-TUvtb-mft-5ljEVku6GYvcS5ynAGV6UI8SdvVh_Koqfw2M37wbN23TZM7B24Bt2t_4DxR3fUFtps1Ypt8Q1Fa6384qI2wOfjoUnpoQm2oQXILKPLZWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djjBQj5Qoeeau37Y5GRE3ntTcMf3SwByB3aQUll8pN0yo3KOH_VWmU0zbPOiNtL9mNgzoxCnl8IfABZUyRBL1ijM0BkpsmVIiuan8mfdhkEUe8BIFG_xMoXDQIdLMAuNLKXdCqdLLglZWNR3F6irKUx-mzdvxWn4kd1sL9q7wp7jRv55i1OAqcQoHnzq3PXwkEuoJRuGH_4JpvYlDKrXfML8Pxcm1KecU9PG7Mmk8iM1VcxUvnjsPHsykocMch0u4f_3rkdWr5dTS180vry5005iRk2uGxWYKN5M32SDjTm49cyfnE7eOP8qwBfM8WZHOFPpbKMcrRFgGLIWH-TNCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سلنا گومز و همسرش:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70888" target="_blank">📅 23:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70887">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=cDR3DszT55RI4Uls30biSH3gLDRislMRJo3-eoGzzr1JLiMTFnDAZHLDdcEdkgWZHhKcfzOlyV5kPMQ7G4NC_4ETfwYbDzl5CITUcIdm8g4V7vE9tuR5cct-529BhnQYCEyQWKBiM30SIN3HAAN0TNX0KClqZkBdAGxJnxqvsU9dOJ61uUnUS5pW3u5fnmi1bKcPj9zxYjQIrKkyUMv8pfOaX3jpYYsfyTdrpwabOqVb70e_qf5IiAV4dylMRskeRd79PENA2VV-k4-N5IMYadG5auqwvlFaZA6DmBfZkP9fTG21N5Kh3I12UiOA41p83qFgXYZqPj9wbus8NV0KsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=cDR3DszT55RI4Uls30biSH3gLDRislMRJo3-eoGzzr1JLiMTFnDAZHLDdcEdkgWZHhKcfzOlyV5kPMQ7G4NC_4ETfwYbDzl5CITUcIdm8g4V7vE9tuR5cct-529BhnQYCEyQWKBiM30SIN3HAAN0TNX0KClqZkBdAGxJnxqvsU9dOJ61uUnUS5pW3u5fnmi1bKcPj9zxYjQIrKkyUMv8pfOaX3jpYYsfyTdrpwabOqVb70e_qf5IiAV4dylMRskeRd79PENA2VV-k4-N5IMYadG5auqwvlFaZA6DmBfZkP9fTG21N5Kh3I12UiOA41p83qFgXYZqPj9wbus8NV0KsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنسرت محسن نامجو در پاریس، ۷ آذر ۱۳۹۱
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70887" target="_blank">📅 22:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70886">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=k76-rgWeocJ4XHy2coR1e2c-hDqXBGuKpHPwPyh-AOgExTIY-5_GNUJUg34EM9r8CVB019mXTQC48W6lMO-tj1mofocggqu809H0IvVo_RcTTWvClNchvJdOJwA4xLvV3qrkQJURwTTmcQpjvkvr1HLuut7l-JaQUxFjbb8sCoS5e6SSEIuLnwMhn8sD7N10jFtXmphlUVE4IctqsKMTKxJF9RN36Fovjkd-RjbnTp1oL7Lw15pMp24AgJm0RHiem6AUpyuknCIWs41Sut33A9Nc1EHv2-a6KZL5PuRuuTmlDVfGjkyzLF4CMZ_xoUPG33tlcNcdbF3_NlcVVHsLLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=k76-rgWeocJ4XHy2coR1e2c-hDqXBGuKpHPwPyh-AOgExTIY-5_GNUJUg34EM9r8CVB019mXTQC48W6lMO-tj1mofocggqu809H0IvVo_RcTTWvClNchvJdOJwA4xLvV3qrkQJURwTTmcQpjvkvr1HLuut7l-JaQUxFjbb8sCoS5e6SSEIuLnwMhn8sD7N10jFtXmphlUVE4IctqsKMTKxJF9RN36Fovjkd-RjbnTp1oL7Lw15pMp24AgJm0RHiem6AUpyuknCIWs41Sut33A9Nc1EHv2-a6KZL5PuRuuTmlDVfGjkyzLF4CMZ_xoUPG33tlcNcdbF3_NlcVVHsLLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای بدل ایرانی آنجلینا جولی:
تا حالا یک دفعه هیچکی دست رد رو به من نزده.
به هر مردی میگم با من ازدواج بکن نه نمیاره.
از هر جای دنیا باشه سریع خودشو میرسونه پیش من.
بعد دوستام میگن تو مهره مار داری دعانویست رو بده به ما.
علتی که اون هم قبول میکرد این بود که چون من شبیه آنجلینا جولی بودم، او میخواست این وجود رو در کنار خودش داشته باشه که مثلا مهمونی میره، پیش دوستاش میره پز بده.
من حتی بیماری‌های مشترک با خانم آنجلینا جولی دارم. هم قلشون هستم. ما ژنتیکمون مثل همه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70886" target="_blank">📅 21:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70885">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
📰
اکسیوس:
ترامپ طرحی را برای حملات محدود علیه ایران در نزدیکی تنگه هرمز بررسی کرد.
وزیر جنگ از طرح «حملات محدود» علیه ایران که ترامپ در حال بررسی آن است، حمایت می‌کند.
طرح «حملات محدود آمریکا» علیه ایران هنوز تصویب نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70885" target="_blank">📅 20:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70884">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⏺
🚀
فارس:انهدام یک فروند پهپاد MQ9 در شرق تنگه هرمز
دقایقی قبل، یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70884" target="_blank">📅 19:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70883">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f517057c.mp4?token=QKeHRap6JtMn-kiweVu4jLOomywfAsceA6te6VC3krkFHsl_yzNI-WVyN7t4oOkpqtnDISq072OHSBvNWkbxkw5T0dxYU_QBZXxIUsyjnVij7lH9DrTbGmyBv6_EU4NexHhctsC8oKzNkAgbhT-kszcRyixpXmPT0JIB_d-g3wq7jeF1xBdVKBpaJM7tPRJoJf-62Vx3yIt0etQM_jKhMBlUR5ydKzoWcE34f46RSF-sefVLuqWH60lWbQYRExI0edubnvJfhm_qV0Bs-FCy54NwF3W4E3TKhg08So5VHTHt2fN0HM80w6RYq4k7dZQ0C5fXfkHk5Q7sjRVqqgUQ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f517057c.mp4?token=QKeHRap6JtMn-kiweVu4jLOomywfAsceA6te6VC3krkFHsl_yzNI-WVyN7t4oOkpqtnDISq072OHSBvNWkbxkw5T0dxYU_QBZXxIUsyjnVij7lH9DrTbGmyBv6_EU4NexHhctsC8oKzNkAgbhT-kszcRyixpXmPT0JIB_d-g3wq7jeF1xBdVKBpaJM7tPRJoJf-62Vx3yIt0etQM_jKhMBlUR5ydKzoWcE34f46RSF-sefVLuqWH60lWbQYRExI0edubnvJfhm_qV0Bs-FCy54NwF3W4E3TKhg08So5VHTHt2fN0HM80w6RYq4k7dZQ0C5fXfkHk5Q7sjRVqqgUQ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
فرزانه صادق وزیر راه:
به علت از بین رفتن زیرساخت‌ها هواپیما بدون رادار هدایت می‌شوند و تعداد پروازها کمتر شده است
👌
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70883" target="_blank">📅 19:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70882">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇦🇷
پست جدید لئو مسی از خاطراتی که واسه تیم ملی آرژانتین ساخت
🩵
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70882" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70881">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70881" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
http://TrexBet.com</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70881" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70880">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKQQSiMryUnwS1S4ibQ-EnADi59kTky6QBts5axm4AuGxh5xTf0ybWseyYLuuUBMNzOKe-v3SOzxkTy0kvq8DICG-j7XQYzdR4WBY9EFlrz6Q2aF737Px9cBqnUljIXiVbfX2ToJhH-NUWp4VdzHIUD0BovLIA7fOTJwx0HyFCmnH85T5mRaV2hY6st4P3kIwnEU50gSccUr1WX8zjTYyVOZJSD7LWh5Qo-yMux4PV5k0C6dkEwFLU9CSoSfziekAZ5kESihyIbUR70EvvQE9r2Prm9hQZYbT0WubLv_t9bPUfWyQ-WSFGbZ3iTfYZWITYm80gUEpmWFan3Z62kXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
میکس پیشنهادی ضریب
〰️
برای بچه‌های
TrexBet
🦖
Code TrexBet:
SKCU6
آموزش استفاده از کد شرط در سایت بین المللی تیرکس بت</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70880" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70879">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URufQQJc4i96YRb5_LARXdcXEL7Fhf_afr4CX5OcJMQcs_b1KWnKUutcPZQlqYtJuaznjuzOYohKiiMcOzLMSMK1qocqyJKQ_3TV9xcS-Ko1tvgagRbtsGVQpOp1updv_xLaIxWKiS2m9sFAQr6aDc8BHMPXQqB7sp0klE7nQCXKDl4RoH4R8UxEE1xIQVO2w97e2af4hRIkACcz1bEUJKRkouUqAgKwhIxAkq4aJ-qEp7pCOhDLg-x9PeAOZ_xyupMsmM0IvrKHujq-4Ue3sjo-bgHpJJ87Xr_jQw5IgoSBSgT1EEad3i1A_PgG99wdT5sa_MnNKA03Dd60oadI3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💋
#فوری
؛لیونل مسی اسطوره فوتبال جهان از تیم ملی آرژانتین خداحافظی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70879" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70878">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=okvODqsC0LwrR7wIPwJIPoObZyEkPTk43_NN_VaDrGqMkb_NawvOgN9j2kA3SZePnawFchkUeeDG2-mgfq6CjuGxXA1nB7Nn6kWVtQawDvE4qjhTdSN7uYTuRcFD_1Gbo4Ey1rNDkeVB5-xFy3NJSSfayKPIq2e_OOnoRiVCHbjjWwtjhy6WAbvQSpOMPMEOv9NFotbDF-_HVgIauLsZik0RrrkF9x5aJ-2IFxNiZtTp68y3zea6_QPJvp1FaIFP1XRGOD-c0gHazpIFlOdU_oHo1aRYQLztCyz-1MTOXFN9Rtr0XM7R4dQoMGYKO72PiFGjbec22GIZaUFn744rSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=okvODqsC0LwrR7wIPwJIPoObZyEkPTk43_NN_VaDrGqMkb_NawvOgN9j2kA3SZePnawFchkUeeDG2-mgfq6CjuGxXA1nB7Nn6kWVtQawDvE4qjhTdSN7uYTuRcFD_1Gbo4Ey1rNDkeVB5-xFy3NJSSfayKPIq2e_OOnoRiVCHbjjWwtjhy6WAbvQSpOMPMEOv9NFotbDF-_HVgIauLsZik0RrrkF9x5aJ-2IFxNiZtTp68y3zea6_QPJvp1FaIFP1XRGOD-c0gHazpIFlOdU_oHo1aRYQLztCyz-1MTOXFN9Rtr0XM7R4dQoMGYKO72PiFGjbec22GIZaUFn744rSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدرضا نقدی:
ما انتظار پیروزی را داشتیم، زیرا به وعده و یاری خداوند یقین و اطمینان داشتیم.
اما انتظار نداشتیم که پیروزی به این آسانی به دست آید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70878" target="_blank">📅 18:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70877">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=R5aGnUpXFSp75E1WfxzFcdPIm39hzh9OFzeFew3TOLFRMagLkI2E_jiZgOQs78jlUU3YBlMum3-KxRAPs4O3p1ei6hyQS8XCHSSbtQLRbCbvifi65C8peeXoTPQub6lZIB5FJrIrQBxAKVGtj0ssgUjgSZVsRFQUsy5zy-ossZRG71lPXF_HnsWcstI66bYGkO_oiOTTfKfNqfO2b6zcvV4xHflN0BbUpu7NKnEDK9DWBWhz7i5ymnjJzkxzJGr6UV1tUAc8bR8Io0X5MSWainecMVZD6oyjnW9Pg5rbPsMW5KU7rfpAVQVxYLXyla7AbaVmz3xR0Qp-3S3OHU5nD1rJZjqpdTMpV9Dm-JwHoc8G6JCuqT_YmxONj_BgRZlgLQ0r9pVQQuOstkYrnPRtuj0Wh8h3Tl9utx_iVMelrg221crtLdUGFCj0Hv33891QIr92bLIbmRTQQGSm7fCR2m0vHA9NR6_Xy4TQIcpTwP1bEEll3WmFkCTARFS8YLcsmqeludGT_aXlPXygDb8Y_Y6XevGEmnnx5Stke8Y4bG05onNWXv4hGhgXLyTV-y_8iquz_x38QGj8smmk0rPm3YZW4thaPz-zFcfro850_TbIrHvh3i0_oTLa7nUA5g8N0UopETVk2FSrBddVGl1ZhowSYFP3NT2ifQaBpLUJzkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=R5aGnUpXFSp75E1WfxzFcdPIm39hzh9OFzeFew3TOLFRMagLkI2E_jiZgOQs78jlUU3YBlMum3-KxRAPs4O3p1ei6hyQS8XCHSSbtQLRbCbvifi65C8peeXoTPQub6lZIB5FJrIrQBxAKVGtj0ssgUjgSZVsRFQUsy5zy-ossZRG71lPXF_HnsWcstI66bYGkO_oiOTTfKfNqfO2b6zcvV4xHflN0BbUpu7NKnEDK9DWBWhz7i5ymnjJzkxzJGr6UV1tUAc8bR8Io0X5MSWainecMVZD6oyjnW9Pg5rbPsMW5KU7rfpAVQVxYLXyla7AbaVmz3xR0Qp-3S3OHU5nD1rJZjqpdTMpV9Dm-JwHoc8G6JCuqT_YmxONj_BgRZlgLQ0r9pVQQuOstkYrnPRtuj0Wh8h3Tl9utx_iVMelrg221crtLdUGFCj0Hv33891QIr92bLIbmRTQQGSm7fCR2m0vHA9NR6_Xy4TQIcpTwP1bEEll3WmFkCTARFS8YLcsmqeludGT_aXlPXygDb8Y_Y6XevGEmnnx5Stke8Y4bG05onNWXv4hGhgXLyTV-y_8iquz_x38QGj8smmk0rPm3YZW4thaPz-zFcfro850_TbIrHvh3i0_oTLa7nUA5g8N0UopETVk2FSrBddVGl1ZhowSYFP3NT2ifQaBpLUJzkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمدرضا نقدی:
همه فوتبالیست‌ها با توپی بازی می‌کنند که طبق استانداردهای یکسانی ساخته شده است، اما همه آن‌ها رونالدو نیستند.
گل زدن نیازمند فردی با انگیزه، هوش و توانایی است؛ کسی که بداند چگونه از آن ابزار استفاده کند.
آمریکایی‌ها صد برابر ما سلاح در اختیار دارند و از موشک‌ها و پهپادهای بهتری برخوردارند، اما نمی‌توانند به‌طور مؤثر از آن‌ها استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70877" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70876">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=Ah-K0S_E_wDcAcBVvWzePxYfNox3-R0SRPhPkNZB7i0i9C7RS3_XTOJZUHR_GIzXJ3tUxgqXQdbMS2WCV8wFFqahvROg3X8bZoWgtkRrBGXgk1MACpc0X0Y5PiOKd5NrVvlGklTqss2FRmXOWthsx2LGtiQcXklLLaJrnIDXkW7W3ztsM4RCDXklWAqXQOtICP1ch-I5X1Nho2J1jDutN0COBxa64C3g2M5UGFx9mtwzTz6xMe3uP42hXOJKz0rMA9lisEiAa07wBP5K0INhrbhXZqja_LenuFxqthyxQTIg57no7w01kSeqt4jZSis_VzEyl_ZQ1-9AZHB8cJ0g4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=Ah-K0S_E_wDcAcBVvWzePxYfNox3-R0SRPhPkNZB7i0i9C7RS3_XTOJZUHR_GIzXJ3tUxgqXQdbMS2WCV8wFFqahvROg3X8bZoWgtkRrBGXgk1MACpc0X0Y5PiOKd5NrVvlGklTqss2FRmXOWthsx2LGtiQcXklLLaJrnIDXkW7W3ztsM4RCDXklWAqXQOtICP1ch-I5X1Nho2J1jDutN0COBxa64C3g2M5UGFx9mtwzTz6xMe3uP42hXOJKz0rMA9lisEiAa07wBP5K0INhrbhXZqja_LenuFxqthyxQTIg57no7w01kSeqt4jZSis_VzEyl_ZQ1-9AZHB8cJ0g4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ماموران نیروی انتظامی روز دوشنبه ۹ شهریور ۱۴۰۵، به سمت کارگران معترض به استخدام‌های رانتی در پالایشگاه لیشتر گچساران تیراندازی کردند.
در این تیراندازی چند معترض زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70876" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70875">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2arwzXYNDdmyfRyo4OFY5Dko8lfnL2JMpsdblM4qzssqJC1niUaiHOhJr-bVr6StXo21v2CTplALFNPgMMYUyci4npXd2xTa3oG0j9DYqcJW4F05TNZecL9i1pmpwu5NdQKmrgGDg32XykhiU2z0QkRXa2QheKxL7jESenI2Y0hCapXNTJs6s1UyJ45yobRsyKNy1WL3OVY-yJLoD2XR_NpnZHAbvGVQ68BnHs37vxzMl0TCT425ck-FDijiH97J8duw57PGq_gUTy9ZnvYnDkFTwnTf4Zons5PlJZ2D1GOwPfQGTS1nb-92oPHEY87w63z-Cg0XRCMDMxV02kMcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضع خیلی قاراشمیش (یاغی)
وزارت نیرو اومده هشدار داده که مردم بنزین و گازوئیل غیرمجاز تو خونه، زیرزمین یا حیاط انبار نکنن، چون خطر آتش‌سوزی و انفجار داره و ممکنه با افزایش قیمت سوخت بیشتر بشه این کار.
گفته فقط اگه واقعاً لازم بود، مقدار خیلی کم و استاندارد با رعایت کامل ایمنی نگه دارین و موارد مشکوک رو به ۱۲۵ یا نیروهای انتظامی خبر بدین.
خلاصه مواظب جون و مال خودتون و همسایه‌ها باشین، این کارا خطرناکه و به نفع کسی نیست.
@Moris_news</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70875" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237073d371.mp4?token=RMR96QKgGruu5J4-YrexkxYZT3bGFuDuOLD9n-1Q2pmR0wVpxE5YEFAATsctnPMOb-99Lf8n--g2fczWrc5fD25M056SBGVssq-Owsk5GMZl3KRLZXtT4MJApY_GNxAh8J9WohQSxsgMjdg2yYXChncho0Q3CKMHTy_Akbh0A5NiA2B__3w0gdZz3ow3tm2vStDj2dBF5OUsD9S5CT6avre8G3_sDM7kax4zG7zBjFk5aU6PN4BtRGHDjbZSWDxZD7quLOmUsnVvEom_cKvZZZSraDIulYdjXTEhtPlnyEO4weXuM14uVBY8bhDdwx-Gat-r0zmsHdabxWhZZxaQdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237073d371.mp4?token=RMR96QKgGruu5J4-YrexkxYZT3bGFuDuOLD9n-1Q2pmR0wVpxE5YEFAATsctnPMOb-99Lf8n--g2fczWrc5fD25M056SBGVssq-Owsk5GMZl3KRLZXtT4MJApY_GNxAh8J9WohQSxsgMjdg2yYXChncho0Q3CKMHTy_Akbh0A5NiA2B__3w0gdZz3ow3tm2vStDj2dBF5OUsD9S5CT6avre8G3_sDM7kax4zG7zBjFk5aU6PN4BtRGHDjbZSWDxZD7quLOmUsnVvEom_cKvZZZSraDIulYdjXTEhtPlnyEO4weXuM14uVBY8bhDdwx-Gat-r0zmsHdabxWhZZxaQdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری دختر اکیپی قرار دعوا گذاشتن پسرا هم دوره کردن و تشویقشون میکنن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70874" target="_blank">📅 18:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f793f615.mp4?token=RWvZoxSSCI1suwK3Rs9hLpu9fZddwHNd72pfMPf7CR9II2f7m_qEkmOXaUtvdUqjvrNJ2O8Rki5yuEeKAGjxXcAZg-6qDgu-P5cabVLIhmTD7cUD_gfhQA9ZpLj4eICG92QCcAN7qJIfddeBPX5NW25IJX5LwI_pfZxCSqg-vI4lD6OxmCmyFujW_CqG0LGiUMh8xnVkNsHHvKGIhaNOfr5whDz45tgoJjofWSM3EhkFYaUS7F1sGHaLgJB-tHLM-9XXyk6RMaKmPe1eQl4xin-BCUG2O1Qzin0luzkWUE3AaAOLqUzV_i7ZZs_9mEF0NkmEvWrUze78g_HF0dDSPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f793f615.mp4?token=RWvZoxSSCI1suwK3Rs9hLpu9fZddwHNd72pfMPf7CR9II2f7m_qEkmOXaUtvdUqjvrNJ2O8Rki5yuEeKAGjxXcAZg-6qDgu-P5cabVLIhmTD7cUD_gfhQA9ZpLj4eICG92QCcAN7qJIfddeBPX5NW25IJX5LwI_pfZxCSqg-vI4lD6OxmCmyFujW_CqG0LGiUMh8xnVkNsHHvKGIhaNOfr5whDz45tgoJjofWSM3EhkFYaUS7F1sGHaLgJB-tHLM-9XXyk6RMaKmPe1eQl4xin-BCUG2O1Qzin0luzkWUE3AaAOLqUzV_i7ZZs_9mEF0NkmEvWrUze78g_HF0dDSPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت وزیر خزانه‌داری آمریکا:
می‌خواهم از اتحادیه اروپا و بانک مرکزی اروپا به خاطر بیانیه قوی‌شان در حمایت از اقدامات اقتصادی ما علیه رژیم ایران تشکر کنم.
و این گروه با هم، به این حکومت وحشتناک چهل‌وهفت‌ساله آن‌ها پایان خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70873" target="_blank">📅 17:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0baed51151.mp4?token=moDDRN32Qgh2B-gZ45N2glqU7V7aUuWP0mIUOhcsT_smz8pvsoxCZQgBGGFpGFI9nzlH69RPNtmkTtWehwteJ7ZpPaUcWnTW_lUNqH0-3gvK6vtqqiD1rN2wk98eR1X5aXUjPduQUoNuzyhT502xTilA1RfeyKAlP70UWBBl2nxpaC_EUonjN-r5vdxP2tOFTfTAkWbXhOcnxQFo7pIzup9n7_iSY6Owj-sH94gE4B0Ro5wrHnPpaogoVbkJjKC_6OjSGtv82PjCVrr6jLR2DbbOr6GgH8_eVyuX_QgI5it5YBHUpj4q_Z0AxhHzFbhFFKckP-XBv1vXoHWYdxxeSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0baed51151.mp4?token=moDDRN32Qgh2B-gZ45N2glqU7V7aUuWP0mIUOhcsT_smz8pvsoxCZQgBGGFpGFI9nzlH69RPNtmkTtWehwteJ7ZpPaUcWnTW_lUNqH0-3gvK6vtqqiD1rN2wk98eR1X5aXUjPduQUoNuzyhT502xTilA1RfeyKAlP70UWBBl2nxpaC_EUonjN-r5vdxP2tOFTfTAkWbXhOcnxQFo7pIzup9n7_iSY6Owj-sH94gE4B0Ro5wrHnPpaogoVbkJjKC_6OjSGtv82PjCVrr6jLR2DbbOr6GgH8_eVyuX_QgI5it5YBHUpj4q_Z0AxhHzFbhFFKckP-XBv1vXoHWYdxxeSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس‌نیوز به نقل از ترامپ:
همین الان با رئیس‌جمهور ترامپ صحبت کردم؛ او به فاکس‌نیوز گفت که ایالات متحده به حمله ایران به نیروهای آمریکایی در اردن — که دیشب رخ داد — پاسخ خواهد داد.
رئیس‌جمهور گفت: «ما ضربه سختی به آن‌ها خواهیم زد. پاسخی در کار خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70872" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csxw1XcxSQS7WyZgFYZIfgHTu22k4WtzFDPzNlPUR22feBie8dbTHHI5wmMmTaEmCNkcHYTnLk0bs69UzCTmCI_WwNyPynXLU8Z8QQJIor7NNiD_blU9iL-DkZFUcUHPR5EVkrbzYMWV8X2FngeGrKwic3LFqG5B2KULAqNxFx76IlEoMk257A0Etm7RY18jWFYt97dcctwhc3R3uXhty0I1o3InujVpy9qb-HAK94r9pmX2Q2FE9xy9zM9TUWszCzM-tVEJ-37rnt7IPZqCqGVG1SbeMtqMg63S0c-B3yiCs23kdH7XVSb6YAWu_a_q0UShN2kly7YZ9aHjCWcvKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:ایران رسماً یک کشور شکست‌خورده است. کارش تمام است!
آن‌ها نه نیروی دریایی دارند، نه نیروی هوایی و نه پول ملی؛ حقوق سربازان یا نیروهای پلیس خود را نمی‌پردازند، نرخ تورم به ۳۰۰ درصد رسیده و رهبری‌شان دچار آشفتگی کامل است و توانایی نمایندگی شایسته کشور را ندارد.
تنها چیزی که دارند «اخبار جعلی» (از سوی آمریکا)، تمایل به کشتار معترضانشان (که اکنون شمار کشته‌شدگان به بیش از ۱۰۰ هزار نفر رسیده است؛ آن‌ها باید به جرم جنایات جنگی علیه بشریت محاکمه شوند!) و البته ردیفی از «چرندیات» است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70871" target="_blank">📅 17:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا بدونید شما اگه عاشق ترین فرد دنیام باشی بعد از حدود دوسال هیجان رابطتتون میاد پایین بعد از رابطتتون تکلیف مشخص میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70870" target="_blank">📅 17:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841288ee9e.mp4?token=sSPBq8Mw8o2y4e-jd-PxWZ32HDybYmde4rGQ3X2enX7aBOLR4IspBm4BcCzdVAEoRbgocoECjhXnZo4Cz00pBitJloFJt8JnqfdW8jCffr_d10d06UrEkVmTGneKlnbgjudnzX2PBxVjqwM_8HPA4vRodl5ZzAbJ_kRhVHORGovJjlPUnKgSVMxGHJdXRloXbR51Hfdwn3s6007wIRkQK3inhDqHibPF7FdRPyyYIswu1qI_Y3Epy3HoxdTfrbJI0K6b4kPZ8aQ031z1WaaVqTnR9-0-OvrF-ofmACQdhPtyIZUW-Obz1xmqKclaPFpNtZoGF9Uy4-DHBAoRHdLfyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841288ee9e.mp4?token=sSPBq8Mw8o2y4e-jd-PxWZ32HDybYmde4rGQ3X2enX7aBOLR4IspBm4BcCzdVAEoRbgocoECjhXnZo4Cz00pBitJloFJt8JnqfdW8jCffr_d10d06UrEkVmTGneKlnbgjudnzX2PBxVjqwM_8HPA4vRodl5ZzAbJ_kRhVHORGovJjlPUnKgSVMxGHJdXRloXbR51Hfdwn3s6007wIRkQK3inhDqHibPF7FdRPyyYIswu1qI_Y3Epy3HoxdTfrbJI0K6b4kPZ8aQ031z1WaaVqTnR9-0-OvrF-ofmACQdhPtyIZUW-Obz1xmqKclaPFpNtZoGF9Uy4-DHBAoRHdLfyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کاظم غریب‌آبادی، معاون وزیر امور خارجه:
این اقدامات تجاوزکارانه با پاسخی مناسب مواجه خواهد شد.
حضور بیگانگان باید از این منطقه حذف شود و آن‌ها باید درس‌های جدی بیاموزند تا دیگر دست به تجاوز علیه کشور ما نزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70869" target="_blank">📅 16:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=c8_pK-VkbHVUlw21VJ_rkqDhULTK6mMhxQltNMmEngX32OvYeT0kTS_O4wwElbdhUlTmgzXQbVgMLfOoVxsRrPg2e0knZT9ng_z85wOhqzXZaDHU5Sy-BbFdDhnowd6j1vvYZdcvuE1YAf1-tRQK3KBzWH137dEQPr0T7y8AlLYEisf-eCz6U2xNGxxETo9seyeDl08PdI-mrdHJ68IRXiMblbUfzjaBXsCBn1xFB5vNX6nlP7YljVc4ZdHG3k3d8QKZCcxTUXt1rpeB2QwFoNXk2zSVgppcipzAVv-XfP-qNgENxxkb-vryTU14mDZMhvIhaLIx7sT6Nnt0qctW1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=c8_pK-VkbHVUlw21VJ_rkqDhULTK6mMhxQltNMmEngX32OvYeT0kTS_O4wwElbdhUlTmgzXQbVgMLfOoVxsRrPg2e0knZT9ng_z85wOhqzXZaDHU5Sy-BbFdDhnowd6j1vvYZdcvuE1YAf1-tRQK3KBzWH137dEQPr0T7y8AlLYEisf-eCz6U2xNGxxETo9seyeDl08PdI-mrdHJ68IRXiMblbUfzjaBXsCBn1xFB5vNX6nlP7YljVc4ZdHG3k3d8QKZCcxTUXt1rpeB2QwFoNXk2zSVgppcipzAVv-XfP-qNgENxxkb-vryTU14mDZMhvIhaLIx7sT6Nnt0qctW1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین شهر مراغه رفتن سر چاه فاضلاب میگن با یاد رهبر شهید پروژه رو افتتاح میکنیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70868" target="_blank">📅 16:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjPZv6ZKAJmMrBDpt2_BXlt2J6liSAnkX505JYguUqT6VJQPErHysCFUD-46pv4pk1Wb-MltX3czZ4jKBZXtOhxbBhfoc2fQ11ks5sz4OUo_u75FZx_EpGZ5XWaBsOySra9OG-pEA-upMPyG_ycxkfwfuvQa4KLmKDGBzqvmdWjQK7dn4UAZF3unj1tSdzkoZhue4mhuLc-a1e6lFRlWVrvc4lKNSVGP1n0aM5EZnMDg0mSQssxoZDEHvk25Q6NAK4m7JjZ5cjvn7J5I65KEYiKLjsSof_FnHUrRJpO4mNVoWBlO1wYc8t6-Mt5zf6riPxMrF_t871cvPgylyJYryA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی:
نتانیاهو به زبان عبری آشکارا می‌بالد که چگونه دولت آمریکا را فریب داده و به نفع اسرائیل، آن را به جنگ با ایران کشانده است.
او صراحتاً و با خنده از این می‌گوید که چگونه با اختصاص ۱۰۰۰ ساعت زمان پخش در شبکه‌های آمریکایی، بر آمریکا «تأثیر» گذاشته است.
اما به زبان انگلیسی، از رهبری رئیس‌جمهور آمریکا تمجید می‌کند.
مار خوش‌خط‌ و خال.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70867" target="_blank">📅 15:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0638c8610c.mp4?token=fzakFTyZbx1YQkocv8GKJLdbjVBRPsSYHAyymj9xN-fqg3LwB88LrrSoVIUqd8_WyOUddUscqcLq74wJSx3AIQD3bbfsD2UjLU-P9ursFwsmgJ6f7XjaSzvFrtLpbMg7zUT69P28fN0B2Md6Z3BZDQhTRNTbG26Zj_sTNJnpCL0_yiwp_9-ADN31z6jP9Wi6lOla-v6H4WevMg-pwXDmi-pwLEgTyAjKK4iTb_DL31bRrryiCe1p7HFRrnVvXM-PbvuYVU2dUxvZzJHQhHb4F1_xBdmx9H9Rq0omhSJvYIf6lx-JAZh0Ax-FClV2ZGFW1Dmd0NnbKMOPRikc9QALgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0638c8610c.mp4?token=fzakFTyZbx1YQkocv8GKJLdbjVBRPsSYHAyymj9xN-fqg3LwB88LrrSoVIUqd8_WyOUddUscqcLq74wJSx3AIQD3bbfsD2UjLU-P9ursFwsmgJ6f7XjaSzvFrtLpbMg7zUT69P28fN0B2Md6Z3BZDQhTRNTbG26Zj_sTNJnpCL0_yiwp_9-ADN31z6jP9Wi6lOla-v6H4WevMg-pwXDmi-pwLEgTyAjKK4iTb_DL31bRrryiCe1p7HFRrnVvXM-PbvuYVU2dUxvZzJHQhHb4F1_xBdmx9H9Rq0omhSJvYIf6lx-JAZh0Ax-FClV2ZGFW1Dmd0NnbKMOPRikc9QALgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه وایرال شده از صداوسیما:
یه نفرو آوردن برای مصاحبه؛ بعد خود مجریه فکر‌ میکنه صداش نمیره تو میکرفون؛ به اون میگه اینا رو بگو اونم همونا رو تکرار میکنه
😂
آخرشم میگه دم غیرتت گرم به‌به چه شیرزنی بود
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70866" target="_blank">📅 15:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70864">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1fde9913.mp4?token=u1u8FNjTBW4OzIrF-apRo4cp3cMcQrSDb49ACwJmebDElC_YewF3R7tp749237zfneKcdasOL3fwSRxZyJD6Y9vE4lx7ka9tFcwNJqU7GXDPdzHDNXgGgw7QxOw7RLEOvuilnlDQbPBmmiboCQL8hEhMTmvjA_qSh_pmlGk7yZTcFjctxA8z1B7562drg1Q_nXfMfs863RcwYS9tNAxlfKkMAOAKjFnUelmS4d6i-FfjKneU_P91nKCrwjhAYJS19OEmBMtBaNblYEmbLnb01CAKbT6ev2ea8vca20yXjLqus_aHRyitCC6MlTlkmzeuDZhmLz6BGjj1MR9Q2UrTlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1fde9913.mp4?token=u1u8FNjTBW4OzIrF-apRo4cp3cMcQrSDb49ACwJmebDElC_YewF3R7tp749237zfneKcdasOL3fwSRxZyJD6Y9vE4lx7ka9tFcwNJqU7GXDPdzHDNXgGgw7QxOw7RLEOvuilnlDQbPBmmiboCQL8hEhMTmvjA_qSh_pmlGk7yZTcFjctxA8z1B7562drg1Q_nXfMfs863RcwYS9tNAxlfKkMAOAKjFnUelmS4d6i-FfjKneU_P91nKCrwjhAYJS19OEmBMtBaNblYEmbLnb01CAKbT6ev2ea8vca20yXjLqus_aHRyitCC6MlTlkmzeuDZhmLz6BGjj1MR9Q2UrTlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حواستون به دوربین مخفی توی ویلاها و اقامتگاه‌های اجاره‌ای باشه!
موارد واقعی از جاسازی دوربین مخفی داخل وسایل معمولی مثل ساعت، شارژر، دتکتور دود و حتی گیرنده‌ها و وسایل کنار تلویزیون گزارش شده.
پس وقتی جایی رو اجاره می‌کنید، مخصوصاً اتاق خواب و فضاهای خصوصی، یه نگاه به وسایلی بندازید که مستقیم به سمتتون قرار گرفتن. سوراخ خیلی ریز یا لنز غیرعادی روی یه وسیله می‌تونه ارزش بررسی داشته باشه.
البته اینکه «جدیداً بعضی ویلا‌دارهای ایران داخل رسیور ماهواره دوربین می‌ذارن» رو نمی‌شه به‌عنوان یک اتفاق فراگیر و تأییدشده گفت؛ امکان و نمونه چنین کاری وجود داره، ولی تعمیمش درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70864" target="_blank">📅 14:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70863">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0345fee55.mp4?token=bz3FvU0r-RpHHdWUbr0ChPQWUmD-SPKqwa0OKpgR4EIbHFyL-C77sYFYWk5ekjen-MS_NI8vxGKnwKgBWp9hhp9W1gT1Ndpi28QtgND5dSm7gYn0XbufK-nCus9DDmlgJv31tGfEdguGUz9Agg0XgfrOEi1b0B1hRXjCLbjAtWL8IZWhF6WSdawUTWTbdWI-bJ9bYY_tmUafzuaFAdFA3S8wWhyJKXNFAlHkzO581SHph_qTdyLmy0x-fpMCRN_JBpQM-CZGq_3XYiaDWke6JflZru2msCNwyC97yjKWiXPzCxaGNQ_2p9Lfg6rEEJ5FeYCB0W4-n4fwULiLcIGXLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0345fee55.mp4?token=bz3FvU0r-RpHHdWUbr0ChPQWUmD-SPKqwa0OKpgR4EIbHFyL-C77sYFYWk5ekjen-MS_NI8vxGKnwKgBWp9hhp9W1gT1Ndpi28QtgND5dSm7gYn0XbufK-nCus9DDmlgJv31tGfEdguGUz9Agg0XgfrOEi1b0B1hRXjCLbjAtWL8IZWhF6WSdawUTWTbdWI-bJ9bYY_tmUafzuaFAdFA3S8wWhyJKXNFAlHkzO581SHph_qTdyLmy0x-fpMCRN_JBpQM-CZGq_3XYiaDWke6JflZru2msCNwyC97yjKWiXPzCxaGNQ_2p9Lfg6rEEJ5FeYCB0W4-n4fwULiLcIGXLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
پست جدید اسرائیل به فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70863" target="_blank">📅 13:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70862">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3zrkUqquprS9YZK6NmMWYRnrzh5oaHsG6eWLHaj55bkiwKuJ6a7_RmX5-qkKlTGrIpwDYLdkBdB0GS7MdSYr864MRfDVtgc1d_MMyBttK6XBWRk-Yb3lDjlO0bEhCN6s_PiHEvroaJBh44Ww1UiVh3aXGLBKRFdGi0RHMxGlJEK8Xyw4e-zfrGPbkgzVsvpW_EeBkgmPkTtZ8Vs2nWLSeT63SSa1ReNVN9odN76f3FuM42qwOQrRzIZJbLYWdzs1ATdKI7wagQscJgTJVW6KQ4zUkPGETZoB7-P6i2sv6r9X1Zl_8tMPoqvyYSleYK07pEsVnzlinXapEdfnSjzzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت، وزیر خزانه‌داری آمریکا، به خبرگزاری آسوشیتدپرس گفت که دولت ترامپ قصد دارد در راستای کارزار خود برای قطع دسترسی ایران به نظام مالی بین‌المللی، در هفته جاری یک بانک دیگر را تحریم کند.
بسنت اظهار داشت که واشنگتن به کشورهایی که همچنان با ایران مراودات تجاری دارند فشار خواهد آورد تا روابط مالی خود را قطع کنند، وگرنه با اقدامات تلافی‌جویانه آمریکا مواجه خواهند شد؛ او در این باره هشدار داد: «اگر ناچار شویم، این کار به مثابه خشونت مالی خواهد بود.»
انتظار می‌رود بسنت این موضوع را در جریان نشست‌های گروه ۲۰ در «اشویل» — از جمله در گفتگو با مقامات چینی — پیگیری کند. وی تأکید کرد که در خصوص اعمال تحریم علیه پکن به دلیل ادامه تعاملاتش با ایران، «همه گزینه‌ها روی میز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70862" target="_blank">📅 13:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d9350e95.mp4?token=TMDgy6u5TYxyze_dS7rRBrEMgFAtHVufpACWYB2g7a3bqYDgUi6eUfonQyz8teAoU2Lnwcrf_5SxehhSDFih9rT_apOnaBIwKINexbG-9tIg4kqiiBuU2CoEKtKMib-GjfRfwFEpFPwy_J8QwHFJQVOAJFpCoLfS26ifvbvOAR3gqkUbHEG3cLY1Vs38xdHq2o-S9VRVphQBOPnIJTeY6UQaoPUr344NhYLBuH9ZVoaQpvnqvQo39WSQISS8G--7QONX35Lnq3JINxDHDDcXm6e64ruwQpfuSVs3VO_-wMe90tBO_YiZ9z2SXZ-GBnYiLrmlyOFTVi9oF1NcUZZ68Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d9350e95.mp4?token=TMDgy6u5TYxyze_dS7rRBrEMgFAtHVufpACWYB2g7a3bqYDgUi6eUfonQyz8teAoU2Lnwcrf_5SxehhSDFih9rT_apOnaBIwKINexbG-9tIg4kqiiBuU2CoEKtKMib-GjfRfwFEpFPwy_J8QwHFJQVOAJFpCoLfS26ifvbvOAR3gqkUbHEG3cLY1Vs38xdHq2o-S9VRVphQBOPnIJTeY6UQaoPUr344NhYLBuH9ZVoaQpvnqvQo39WSQISS8G--7QONX35Lnq3JINxDHDDcXm6e64ruwQpfuSVs3VO_-wMe90tBO_YiZ9z2SXZ-GBnYiLrmlyOFTVi9oF1NcUZZ68Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇺🇸
ترامپ با هوش مصنوعی جزیره خارک رو نابود کرد.
جزیره خارگ دارد به تلی از خاکستر و آوار تبدیل می‌شود!!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70861" target="_blank">📅 12:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70859">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ae1b8230.mp4?token=pZU3vJOr6CcPx0XZxMyAJEa5P1aBxqoF9aAf3UEYeZT-EpCCmYRwdlfo6awgVJt5Zaap7rXjQK9Hd7isatwFEbGA-Rq2f_XlP3UbCoPZO3QihKdPxVNPgNpAB3Q3FjqtQ121vHaPrb4QEpemVF1N_3T_bVbU9tE_mYSeIzW2EdjcBrAFNfTSJidTHdv084UeBjIM14cIWdiuUvHGJtJMn23t3hrew3TjOV3HXJMej5PSLa924vjyaVfkc4oE5rDGssNEq6XKBcayp1jntAF492Zk-3SPY-yGQ1CcST5cl0r5XudpWShxR12MX_5ZiFJYQ-Uj-9GHappDX7yEnRfE5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ae1b8230.mp4?token=pZU3vJOr6CcPx0XZxMyAJEa5P1aBxqoF9aAf3UEYeZT-EpCCmYRwdlfo6awgVJt5Zaap7rXjQK9Hd7isatwFEbGA-Rq2f_XlP3UbCoPZO3QihKdPxVNPgNpAB3Q3FjqtQ121vHaPrb4QEpemVF1N_3T_bVbU9tE_mYSeIzW2EdjcBrAFNfTSJidTHdv084UeBjIM14cIWdiuUvHGJtJMn23t3hrew3TjOV3HXJMej5PSLa924vjyaVfkc4oE5rDGssNEq6XKBcayp1jntAF492Zk-3SPY-yGQ1CcST5cl0r5XudpWShxR12MX_5ZiFJYQ-Uj-9GHappDX7yEnRfE5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آزاده اخلاقی همسر محسن نامجو:
بی‌ناموس تو که چهارتا ورقه گرفتی دستت گفتی دارم میرم همین سرکوچه تو آمریکا پرینت بگیرم، تو فرودگاه امام چیکار میکنی؟ چرا چمدون من رو اصلا بردی؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70859" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70858">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70858" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70858" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70857">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiTU2UwaGVKtHsihZp0fDH68639VrZg45wVYtwDMVZncCQ5YkDkvWtDl8QIV1-UDFPOVSQvTG2kF_9wvOjoH5uh2WmYeAxCvBaXp2NV5OfkK1WGUVM9w40C8aa5RpuZA1YqwN5L4I9ziWAPl5tvFqkboN6jU99hEVLVnjETJ4Uv_B7n3qa2MRqtLDOQhrDXWU6SlX7zmrrv83uupCsHtzWJyTSIT03-vk0UBl-Pvmgw2koLFAy7xKcloMyAWwGQLFrzXch28kTxAkvK1X1iefEGhTz23EUGUpLTr8gEWIKeSERWzOeZY7lgkt4Pebls0IsLwL5lJBX9MA3VdJl0Y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آرسنال
🆚
استون ویلا
رایو وایکانو
🆚
لیدز یونایتد
رم
🆚
لچه
بولونیا
🆚
آتالانتا
ختافه
🆚
اوساسونا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70857" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70856">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/862d93bdfa.mp4?token=D9XsJ8_bpA8B8q6AVg-RMIhNyecdxs7ro0rpX7DIlQEyEvzju7IlNH1_ur5UHGeNDPlXoNPqFlrzG476v7TNM2q4Ys__fAnqdwksXCQlmomijl38zsBnQvXABQi4ZV_z0vHHEkOdqOR8wn7xCe79H0HzYYyO_-xWzTnpssw3U7SN-xXQEj-zlFr-Wh2CLh9qIclv3giUUIehhsZh3QW7qHTVp89MFzE4NutIrs5euMX-6VZQT7KGFSuP9102nq6bw-NgUXTrvOujlUubW9Tau8Ul9GArto_id7K7BxaqIBKKRd_nHBznA18Xy4rbQlCQukzfxNrgxdH4c2CbozwWNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/862d93bdfa.mp4?token=D9XsJ8_bpA8B8q6AVg-RMIhNyecdxs7ro0rpX7DIlQEyEvzju7IlNH1_ur5UHGeNDPlXoNPqFlrzG476v7TNM2q4Ys__fAnqdwksXCQlmomijl38zsBnQvXABQi4ZV_z0vHHEkOdqOR8wn7xCe79H0HzYYyO_-xWzTnpssw3U7SN-xXQEj-zlFr-Wh2CLh9qIclv3giUUIehhsZh3QW7qHTVp89MFzE4NutIrs5euMX-6VZQT7KGFSuP9102nq6bw-NgUXTrvOujlUubW9Tau8Ul9GArto_id7K7BxaqIBKKRd_nHBznA18Xy4rbQlCQukzfxNrgxdH4c2CbozwWNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای ایشون که داره وایرال میشه:
با این شرایطِ گرونی، هیچ دلیلی نداره که شما به دختر مردم غذای مفتی بدی.
اصلا به حرف کساییم که میگن مردایی که پول میگیرن پرنسسن و لَنگن گوش ندین.
خیلی از دخترا بخاطر اینکه حوصلشون سر میره با شما میان بیرون و یه غذا میخورن، پس دنگتونو بگیرین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70856" target="_blank">📅 11:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70855">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=vSbJR573veLp67Fjfz2FTNPSRu7nBDCYa-hhGSdHS4Ao2lNy3HsTIY5MYJDpb4iU-Rv6lmgiHUJImnqTzH7z0hIiTk55oSxqhrTTbg-GBf8VlbWe-V-G7rzmV03Wss5NqrHNtgH_2Z_2_a5ele9-qsyGvbCNLDPqOs9nGKKMmuO_O_V45Hc5wElxg4WX9S-_SO3BuXHYtyfPGDDnFDD7VLVocmU3ig2qaxzbKvYzrjNXt45KESRreghEvrb_MqCiGHm_Ei5NuZSHDD3vgHd6FtL-p3pkS36OLehkSNfd76BoSijyfsDSElZxPxi8YTths2ub59dfIyDlYJIkqwthlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=vSbJR573veLp67Fjfz2FTNPSRu7nBDCYa-hhGSdHS4Ao2lNy3HsTIY5MYJDpb4iU-Rv6lmgiHUJImnqTzH7z0hIiTk55oSxqhrTTbg-GBf8VlbWe-V-G7rzmV03Wss5NqrHNtgH_2Z_2_a5ele9-qsyGvbCNLDPqOs9nGKKMmuO_O_V45Hc5wElxg4WX9S-_SO3BuXHYtyfPGDDnFDD7VLVocmU3ig2qaxzbKvYzrjNXt45KESRreghEvrb_MqCiGHm_Ei5NuZSHDD3vgHd6FtL-p3pkS36OLehkSNfd76BoSijyfsDSElZxPxi8YTths2ub59dfIyDlYJIkqwthlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وایرال شده از طرفدار حکومت با پوششی جالب که میگه:
آقا فکر کنید شعب ابی طالب هستیم و محاصره مون کردن
این محاصره از شعب ابی طالب سخت تر نیست که
ما مذاکره نداریم و آمریکا هیچ غلطی نمیتونه بکنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70855" target="_blank">📅 11:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70854">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=NBMWMi0CpvQmz8_WTNp7nvXXhz3kXx_W-8kB69hef4H9bU_lCnsuyqp7Loha9C1kfUaWBMVJpLHl1GtB407UymRQNm-2xKYVFbCIadSGIhyAZguLmZyOWGkh7JuxfSSzMJwC_-NhOCDNbl3dpH2y7bIkYPMGTSm5FR6f3dLTuaKMac9JOwr24yQNyb96rG-WjmNProCTuKCrfglMM-wS0xvB2Ro8pkLBJk4Hsl5V6sC7t3hxaaTcyCMGrf6KFJY2dd7P5NYw-NOOTwNmTlRhECRu1Pfqx2bvJpFzjzauefLY16xieNnlvX7d386VZPb6McpUqIEW-rayB9BLnOg1bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=NBMWMi0CpvQmz8_WTNp7nvXXhz3kXx_W-8kB69hef4H9bU_lCnsuyqp7Loha9C1kfUaWBMVJpLHl1GtB407UymRQNm-2xKYVFbCIadSGIhyAZguLmZyOWGkh7JuxfSSzMJwC_-NhOCDNbl3dpH2y7bIkYPMGTSm5FR6f3dLTuaKMac9JOwr24yQNyb96rG-WjmNProCTuKCrfglMM-wS0xvB2Ro8pkLBJk4Hsl5V6sC7t3hxaaTcyCMGrf6KFJY2dd7P5NYw-NOOTwNmTlRhECRu1Pfqx2bvJpFzjzauefLY16xieNnlvX7d386VZPb6McpUqIEW-rayB9BLnOg1bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
رهبرانشان از میان رفته‌اند.
تمام... خب، تمام تجهیزات ضدهوایی‌شان، منظورم این است که همگی نابود شده‌اند.
آن‌ها آدم‌های سرسختی هستند؛ آدم‌های باهوشی هستند. اما... خب، بسیار شرورند.
تا سه ماه پیش، پنجاه و دو هزار معترض را کشتند و متأسفانه، شمار بسیار زیادی را هم به آن فهرست افزوده‌اند. حتی سراغ کسانی که معترض هم نیستند می‌روند؛ به خانه‌هایشان هجوم می‌برند، آن‌ها را با خود می‌برند و به ضرب گلوله می‌کشند.
خب، این‌ها آدم‌هایی بسیار خشن و شرور هستند و اگر سلاح هسته‌ای در اختیار داشتند، اسرائیل نابود می‌شد.
اگر من رئیس‌جمهور نبودم، اسرائیل از بین رفته بود. دیگر اسرائیلی وجود نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70854" target="_blank">📅 10:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foG6JtTb5ajYBE-7bF3kVGL5Gp720rgZ8lPMp1YbYurN9Q5hnLRTKWaQbw2Zw89d4fC0vRMCSG-Brktwi5A5qTMpinmKDHeJ7cOqfxbhtMufuuwa91FGNnKFsoT8syaE-cajY8xG5rzHuS41m-DGlt7agq1HPHQDh8WoF9DcQD9v3kQOaquYoZk76wGEEVz8HCrO9dLLoHqmU-JCOxpUZHSLiYgzPYTn4EmxiGkpzViemKgZRCXM0RIq1h8hvuGE-8Fe-dZodsmQ0_-_HbGqkfhz0zmYWaNAJ9NuRujOcxAJYRZ6zFv11Hc_GfUwo9jM64yioXbGZa0T0xXinyP3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
〰️
سنتکام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران در بیانیه‌ای اخیر مدعی شد که حملات نیروهای آمریکایی برای جلوگیری از مین‌گذاری سپاه در تنگه هرمز، «اقدامی تجاوزکارانه» بوده است. این ادعا کاملاً نادرست است.
✔️
واقعیت: نیروهای آمریکایی علیه یگان‌های مین‌گذار سپاه که در تنگه هرمز تهدیدی قریب‌الوقوع ایجاد کرده بودند، دست به اقدامی محدود و دقیق زدند. در واقع، ایران عامل ایجاد این تهدید بود و ارتش ایالات متحده برای حفاظت از دریانوردان غیرنظامی، کشتی‌های تجاری و جریان آزاد تجارت جهانی، آن تهدید را خنثی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70853" target="_blank">📅 10:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef58f7de4.mp4?token=k9xosCU73NxaGRiY85U2ueiUtfva5xWheMigo_oD7M9DFxO0KDlvs2v5MEoODMHtHnOKmukpENEnm3x9ttQv445Z9vYiTZ7qqE63mb0zgL6illVOBwP6yqXALRW-d838W0PeFddv2p4hSkyD-EvX3a1NeskspJkgXNOATL0ld5zSeOOj7NQUmevGvmaPE7NgBLB-cM97t4fHCOPJ9qYV6-JR88Zt4pBgJqydwfMc_zH68y36hoft7pOzKqS7LLRIhXY8J_ESHDxUL-BheA9WwGu6LOW5WZroQ9XLJqnW7h5-xJjwj592TKoTLdMbVi4umftJCF65G422ZXbExEr9XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef58f7de4.mp4?token=k9xosCU73NxaGRiY85U2ueiUtfva5xWheMigo_oD7M9DFxO0KDlvs2v5MEoODMHtHnOKmukpENEnm3x9ttQv445Z9vYiTZ7qqE63mb0zgL6illVOBwP6yqXALRW-d838W0PeFddv2p4hSkyD-EvX3a1NeskspJkgXNOATL0ld5zSeOOj7NQUmevGvmaPE7NgBLB-cM97t4fHCOPJ9qYV6-JR88Zt4pBgJqydwfMc_zH68y36hoft7pOzKqS7LLRIhXY8J_ESHDxUL-BheA9WwGu6LOW5WZroQ9XLJqnW7h5-xJjwj592TKoTLdMbVi4umftJCF65G422ZXbExEr9XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سرهنگ خلبان بهمن فرقانی، جانشین فرمانده پایگاه چهارم شکاری دزفول :
زمان جنگ، آخوند رسول منتجب‌نیا به پایگاه ما آمد و پیشنهاد داد برای بستن تنگه هرمز، فاصله عمان تا ساحل ایران را با قایق‌های موتوری با طناب به هم دیگه ببندیم تا عرض تنگه بسته بشه
به ریشش خندیدم و گفتم: «چرا مزخرف می‌گویی؟»
زیرآبم را زد و از نیروی هوایی اخراجم کرد!"
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70852" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70851">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8771a258e.mp4?token=a2wiwa5KS7ogN-mFS1Z2wdBM74HCOxnrg2wWfY9c91nM7N2GoS46k4g87O9VqCX92oiHM8c-stQxsTKjNXa-nqcTuinST3Hx1IwoWOOGXcSz-VXpRua_eTvsJuwX0xDhj7YsPzWvrZUi2PAA0nDnK8GQDiDTM8EEiE2j8v4d_C7WkkFhrvi4C6XWdNm0z7DO1_38WA7OcKNKqP5w3wNpLTiOVZjkD2ZbLANomGgZxLlfepJ71bb-VuF6dpi19qdM2kzLS_ZEw1HPk6XIyb7orTQey1rTjxwgBa8wDpI6TxmRU16b4oYaD2m1JcD45htjgDQYQNI05OViIzNDapyTVIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8771a258e.mp4?token=a2wiwa5KS7ogN-mFS1Z2wdBM74HCOxnrg2wWfY9c91nM7N2GoS46k4g87O9VqCX92oiHM8c-stQxsTKjNXa-nqcTuinST3Hx1IwoWOOGXcSz-VXpRua_eTvsJuwX0xDhj7YsPzWvrZUi2PAA0nDnK8GQDiDTM8EEiE2j8v4d_C7WkkFhrvi4C6XWdNm0z7DO1_38WA7OcKNKqP5w3wNpLTiOVZjkD2ZbLANomGgZxLlfepJ71bb-VuF6dpi19qdM2kzLS_ZEw1HPk6XIyb7orTQey1rTjxwgBa8wDpI6TxmRU16b4oYaD2m1JcD45htjgDQYQNI05OViIzNDapyTVIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یک سرهنگ فراجا:
متأسفانه مدتی عده‌ای از مراجعه کنندگان و یا به تعبیری ارباب رجوع به ما مراجعه می‌کنند و در خصوص گرانی‌ها معترض‌اند و هر بار که به ما مراجعه فکر می‌کنند، فکر می‌کنند که مسبب و اینکه ما از دست ما کاری بر می‌آید و نمی‌توانیم برایشان انجام بدهیم.
آقایون مسئول، عزیزان مسئول، به خدا گرانی بیداد می‌کند. آقای برادر تعزیرات، آقای بازرسی کننده، آقای بازرس اتحادیه، به خدا با کت و شلوار اتو شده و موهای ژل زده و عینک دودی نمی‌توان با فساد مبارزه کرد.
آقا یه جای کارو درست کنید که یه جای دیگر را بخواهید گوش‌نظر بدید. تو رو به خدا، تو رو به هر کسی که می‌پرستید وضعیت معیشت مردم را درست کنید.
فکر می‌کنند به عنوان پلیس ما از جای دیگه درآمد داریم، از جای دیگه خرید می‌کنیم. به خدا این چنین نیست. ما هم مثل همه شماها از همین فروشگاه‌ها خرید می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70851" target="_blank">📅 09:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70850">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78504efb49.mp4?token=akvtltBF3HtfC4yMKdZD_hI-D8ZZ8g9kevyCIiRhV31loGsYwIQZIrWmqD6rfZVqDiO5jqWYXAq1iZBkrjK2kBsT002rVkwI5Rdg7GkLPR73EHUMza0c9nPc0Dhe4_L4TRmDgrQdTzJQUzhUuNBaj9PsB71yBrvRs49yw-EPDMT9sw7fbpyWqDVWsw47KmKxezH9TVv99-LCarevYZKp3jDGub7BazopF7YqKMz9U6KsWBbgMYn6kkBWG3d79f6q4kK3QOcQd0o436iGQJbpL3seRHqIPi1ItmCnt6cGfqrmAWWLErpm0tNmJA6pSAQJV1RvgpdpjRsCMHsc_eUEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78504efb49.mp4?token=akvtltBF3HtfC4yMKdZD_hI-D8ZZ8g9kevyCIiRhV31loGsYwIQZIrWmqD6rfZVqDiO5jqWYXAq1iZBkrjK2kBsT002rVkwI5Rdg7GkLPR73EHUMza0c9nPc0Dhe4_L4TRmDgrQdTzJQUzhUuNBaj9PsB71yBrvRs49yw-EPDMT9sw7fbpyWqDVWsw47KmKxezH9TVv99-LCarevYZKp3jDGub7BazopF7YqKMz9U6KsWBbgMYn6kkBWG3d79f6q4kK3QOcQd0o436iGQJbpL3seRHqIPi1ItmCnt6cGfqrmAWWLErpm0tNmJA6pSAQJV1RvgpdpjRsCMHsc_eUEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل به فارسی:
جمهوری اسلامی و سپاه پاسداران سال‌هاست که ثروت و منابع ملی ایران را صرف تروریسم و جنگ‌افروزی می‌کنند، در حالی که سهم مردم از این ثروت، ایستادن در صف‌های طولانی و بحران کمبود بنزین است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70850" target="_blank">📅 09:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70849">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70849" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70848">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiOAkejgRvN9Sfqc1aKt2XnBO2mmItwlnVWdDg8-Yoz2bK5F4PIKbuGXS_5xVyXm4EY39swy2gQRiPBAf4jxMUhKnmEgiU8GaxVOPidb-GswZ4MIdyAGv4f0MSYyElaCVN9mGL-evtThGgFdyZac35S08soDPh5x_ssPupNALFCF-GOMfWkk-xbHwGtihbh9WeGJOvJABWm18Mr3d_02JAjbtZfh6dXEshmd9IsoETVd7pSiFzz_o7OftXGpbNAyPCxATnYCVFZmq5tDwX0vl9dL8Ms3i_iS2ZsgD7eNsiWHhJ1XDk7lB4Pq47qOe_YHL2WA-ltWwXgOlc8fs1OGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70848" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70847">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
نایا:حملات موشکی به قطر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70847" target="_blank">📅 01:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70846">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">یادآوری: علی خامنه‌ای، دیکتاتور و بزرگترین جلادِ وقتِ خاورمیانه در ساعت ۹:۳۰ دقیقه صبحِ ۹ اسفند ۱۴۰۴ توسط ارتش اسرائیل و آمریکا، تکه تکه و تجزیه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70846" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70845">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بچه ها بزارید منم این وسط یچیزیو یادآوری کنم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70845" target="_blank">📅 01:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70844">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr. NOBODY</strong></div>
<div class="tg-text">خواست پاتریوت رو با لهجله بیریتیش بگه اذیتش نکنین</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/70844" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70843">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɴᴀᴢɪ</strong></div>
<div class="tg-text">امیر پهن مغز پتریوت چیه؟</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/70843" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70842">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNhDqL7YU37HeAq0P44JWXMPbtpNPntxYKBXM6bUsO-31cY5ejDioBnk2LRpPmnOVuOExCK4XgAL9ZxkImZ9CUmPb6Wq1gPkau-qo2yrizbOjYyMaMUEcIdU2QAdL01cf69a3db_XfS5V0eBIdK7u6pyzN2ypG2XR-HEFXY8n-GqY_uWqtu6_yM3NUfyfZtzJd1i-JCSFYZiDR5Ug0g0YVmviWqTO-qGNxu-zGfPGucv0pe0Orze95yV7__zcMpGOO3k4xffku7iIx13-BVXOt9nnE3GDlJHKBA9Nq_FJgFb2WolK_esagNdqwFWekj1LeLF0Pli2Sllhxas9zDRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا برخورد موشکی صورت نگرفته، اکثرا رهگیری شدن #hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/70842" target="_blank">📅 01:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70841">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=CTKYyz01n-BxVESudtsOt-KX0CzXNffOQXIpOmQzBSao08K26IeO8GR691t3siwG-cBzQqOgS2sRXQ9d84vfZJ6njt9HKDV12BI0rX_rW7RPGCqgeLFNWTFcc2c2H32xtqyB3m0QAA_42avv3ucyTJ2J8vNgfqTlDvD_IoKgpb3hG0ZrXiOeutsW310OR-kW1RtRcRQkeJ0tgB8TMhhdkX2tKbGaCe0R_fD2sIoi6IDkhQe5w5r5vqzpxEZPT-mWbd45POXbqSu6kkzzNjAcSjM57tQ-9QYpnVt9z19QiW6V5NMn8es8lQ-WdClFrgzOMvhJETi0scpGOUChFfnRFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=CTKYyz01n-BxVESudtsOt-KX0CzXNffOQXIpOmQzBSao08K26IeO8GR691t3siwG-cBzQqOgS2sRXQ9d84vfZJ6njt9HKDV12BI0rX_rW7RPGCqgeLFNWTFcc2c2H32xtqyB3m0QAA_42avv3ucyTJ2J8vNgfqTlDvD_IoKgpb3hG0ZrXiOeutsW310OR-kW1RtRcRQkeJ0tgB8TMhhdkX2tKbGaCe0R_fD2sIoi6IDkhQe5w5r5vqzpxEZPT-mWbd45POXbqSu6kkzzNjAcSjM57tQ-9QYpnVt9z19QiW6V5NMn8es8lQ-WdClFrgzOMvhJETi0scpGOUChFfnRFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رهگیری دو موشک سپاه پاسداران بر فراز اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70841" target="_blank">📅 01:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70840">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
فعالیت پدافند در اردن  @News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/70840" target="_blank">📅 01:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70839">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:  از خرم‌آباد صدای انفجار شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70839" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70838">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از خرم‌آباد صدای انفجار شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/70838" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70837">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">صدای انفجار شدید تو خرم‌آباد شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70837" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70836">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44471a1938.mp4?token=uZb_Flrh84Zxag-D4xh2yV8dN11yV_i2edfDl9maK760Ao1ZVi8n2TBJ5oaXxRoT3nIZOFaZCHoDUxgLDeHpxWaREtXwciJFQmIoDWfRyXiEhUdDPQCW3PCxaJpfGP6TfNk-u2LKwG4Lc43S4JYPNJTvAdIiwYAaGe3VJ4g1DoaEqYQn9cq0chXkOSLsmtLuKJOc37kkpCwgU4mg60xDTP1R4rkvv4C_xyfhcVIxB8bA4wK5oQNhWjIX78FOELMsaKshCQzfGoyJZIbhs34LIhFNsl39cnWZ-Ocky74mqwjxzDP_fjgVR5V1GpUeVzzgpUixOJzGOvMDN7GkebaBwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44471a1938.mp4?token=uZb_Flrh84Zxag-D4xh2yV8dN11yV_i2edfDl9maK760Ao1ZVi8n2TBJ5oaXxRoT3nIZOFaZCHoDUxgLDeHpxWaREtXwciJFQmIoDWfRyXiEhUdDPQCW3PCxaJpfGP6TfNk-u2LKwG4Lc43S4JYPNJTvAdIiwYAaGe3VJ4g1DoaEqYQn9cq0chXkOSLsmtLuKJOc37kkpCwgU4mg60xDTP1R4rkvv4C_xyfhcVIxB8bA4wK5oQNhWjIX78FOELMsaKshCQzfGoyJZIbhs34LIhFNsl39cnWZ-Ocky74mqwjxzDP_fjgVR5V1GpUeVzzgpUixOJzGOvMDN7GkebaBwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت پدافند در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/70836" target="_blank">📅 01:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70835">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبر متوقف شدن پروازای فرودگاه مهرآباد هم فیکه #hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70835" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
منابع عربی:شنیده شدن صدای انفجار در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70834" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🔴
گزارش ها از شلیک موشک از نقاط مختلف کشور به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70833" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">همه‌ی خبرایی که رسانه‌ها بخاطر ویو گرفتن به ترامپ نسبت می‌دن فیکه، هیچی نگفته درمورد حملات امشب  تلگرام یه‌پا شده روبیکا... #hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70832" target="_blank">📅 01:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq4kiMAnHNTFfNas_4eQsUaEuLVT3gJ-hK2kE9NfAFj9PS8oPLkXhQ3xtj3SvFyHofzjen8JY52gf6mccKA65770w7QHG2peJcCXZaNTIv9WkVd6W1VmCyickxH1PoFQk9lgKtxFW1KOc4yJ9lZjOmfXVghtEDlffwGDAS5jzQwyok90dAaBNzdHU75lb_HY9jwsFxbaJBzwA3R1yZFMDBFVVvusiExOPyem3eUTFIKv1ZCWLR7iMtLTEU9rUh9EcSuxJFEPh_qTyuH2ynOn4EnhLjvNYQBik5EriB0XjDFgS1Eu6x8eGiWIZ__leiDlyNqd-Lk4v5wzTwsGFNghEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70831" target="_blank">📅 01:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=NEYSAcEMSMXWt_pKLxGvF59hYTEXw_9YdPX5o1Nwu57bmbM1QUwgYd_CyJKJkrB_qoEnL7k11FgPMLiFAvrjdPdwyZ6pL0XjWJBdmPx6MZTBNn_eUY6KbZ0O8PAXPVh3CShTPPp1ruRUTTkDYU311u-ZQ3NCPZaiI4hXBApt5cB8k0jLhYuMlwsPueY1fA8junq3VUaG6gwKwqY0d1mqWUrwjTlzFRcKWeD8UkfjP-oBHyJ2oT9-IIu1or5TApC2xPzArzAkvLajdLiB6vl36NrsCMTFWYVuJ2uLUSGZh_Ixrx42DtOqncYq99apZC768wOnthwsEbzOAvIa1kdRyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=NEYSAcEMSMXWt_pKLxGvF59hYTEXw_9YdPX5o1Nwu57bmbM1QUwgYd_CyJKJkrB_qoEnL7k11FgPMLiFAvrjdPdwyZ6pL0XjWJBdmPx6MZTBNn_eUY6KbZ0O8PAXPVh3CShTPPp1ruRUTTkDYU311u-ZQ3NCPZaiI4hXBApt5cB8k0jLhYuMlwsPueY1fA8junq3VUaG6gwKwqY0d1mqWUrwjTlzFRcKWeD8UkfjP-oBHyJ2oT9-IIu1or5TApC2xPzArzAkvLajdLiB6vl36NrsCMTFWYVuJ2uLUSGZh_Ixrx42DtOqncYq99apZC768wOnthwsEbzOAvIa1kdRyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش ها از شلیک موشک از سایت موشکی بیدگنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70830" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">همه‌ی خبرایی که رسانه‌ها بخاطر ویو گرفتن به ترامپ نسبت می‌دن فیکه، هیچی نگفته درمورد حملات امشب
تلگرام یه‌پا شده روبیکا...
#hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70829" target="_blank">📅 00:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70828">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4FHWQBh0XRtIDhlTXTt2Eui9rrS_cdSsV2X2EqE2s2Y8aCXbhoxje9cbw06T3x17wfUQxHRN5b_y7JhqDpUOF-QOb680TPqC23gg0Ajy0hKhsNF424oBHeuR9C_j72MCxnSMAlZMKQptwDnwKz8C4EmD5a4Excz9MuVLpfgLprGLjB4G5cdbPovNQdcbmRtQw-qTIK8unDvbKhmKtRk_zhw02wnOJ1rjT3A1OW7c1RjSaEAsgsSF1q9C00jsImYwEDXNFC1xgemQTSyINMqWxphIOrVzxHDCeVxYtSf8J1vjuG-j4HP3ZoXE1_1va1bLw_mexcbXLzs4yPX02ocWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
ابراهیم عزیزی:
یک بار دیگر اراده ما را بیازمایید و بهایی سنگین‌تر بپردازید.
انتقام در راه است؛
فقط فرار کنید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70828" target="_blank">📅 00:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70827">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06c56b11a.mp4?token=v2JYSKvdguiorddc_HNU6qzd7EWSR4V03PzB367ZqdMtKwqxOI5Z_3DEhErRgkMFF3pGUb1k8vbMgk8BrhHT9VDU4Z_CRGdSg-sUDRbhxV3d_rQH8lyopZ9qj57f6Bhc1nAVkerR1HZ1ZvViQBFpktyjwEp-v9t1Q_foEY6HrdWrBaPjBK36xvWlHoS6DYfRabL1aVCIihUiqAa7eVi6ZSA9_4kMSmtyXFGdBRiPahBGSnPYMwwEN4YMhgC86GJfxYozUv_ZLLF7ymPkgtyNAUad1xaECkJl9TkZ8g8buRPtyGuMGTJN0CQJzr7QuW4DaqZn3ydrHQKrbmtKguLDzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06c56b11a.mp4?token=v2JYSKvdguiorddc_HNU6qzd7EWSR4V03PzB367ZqdMtKwqxOI5Z_3DEhErRgkMFF3pGUb1k8vbMgk8BrhHT9VDU4Z_CRGdSg-sUDRbhxV3d_rQH8lyopZ9qj57f6Bhc1nAVkerR1HZ1ZvViQBFpktyjwEp-v9t1Q_foEY6HrdWrBaPjBK36xvWlHoS6DYfRabL1aVCIihUiqAa7eVi6ZSA9_4kMSmtyXFGdBRiPahBGSnPYMwwEN4YMhgC86GJfxYozUv_ZLLF7ymPkgtyNAUad1xaECkJl9TkZ8g8buRPtyGuMGTJN0CQJzr7QuW4DaqZn3ydrHQKrbmtKguLDzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:
من این رژیم را به زانو درخواهم آورد. به این امر متعهد هستم. این کار شدنی است.
آن‌ها بسیار ضعیف‌تر از گذشته شده‌اند و در موقعیتی متزلزل قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70827" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70826">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
آن‌ها از برنامه هسته‌ای دست نکشیده‌اند. ما آن را به عقب راندیم، اما آن‌ها کاملاً قصد دارند برنامه هسته‌ای خود را برای تولید بمب‌های اتمی از سر بگیرند.
بنابراین، این تهدید از بین نرفته است. ما این سرطان، این غده سرطانی را ریشه‌کن کردیم. می‌دانید که اگر سرطان را ریشه‌کن نکنید، می‌میرید. این همان کاری بود که ما انجام دادیم.
اما سرطان ممکن است دچار متاستاز (گسترش) شود و در صورت بروز متاستاز، می‌تواند دوباره به تهدیدی تازه و بسیار جدی تبدیل گردد.
ایران می‌خواهد برنامه هسته‌ای خود را از سر بگیرد.
من پیش‌تر یک بار مانع این کار آن‌ها شدم و تا زمانی که نخست‌وزیر باشم، مانع انجام آن خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70826" target="_blank">📅 00:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70825">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuD4qMV2MRHM4s4OZkVMBWd5urxaVchYD8XJ9VR9ZZkhJStr7_qqckH9RnAetPNQ5T4_Bgh2yaScLeLy_S1c2jnbLVZ5oqurEP4JV1wL5oM3BE05dmKSoEZAwA52WSaGZIhxdfJtKycJx9Ii93hDcPPNzlfVd6EOK_hkTPtOfEa-bfSZmPEcFyRotQ9Fcx2HUZdad9uT5wuCgQuA3ZH-eLQSZeTyXm_G-LhMzRfu2unnqu9ZiBbR5l3vaSmp7RRpGslhq88muA8FwJfITeZ-P92sgJS9NDWHY1_thNAqHIsTfYr3ysk611XvTrXsRKIlz2GiVncQ7tFir5yiw6b1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
سخنگوی سپاه پاسداران انقلاب اسلامی:
این اقدام، یک خطای راهبردی و مهلک از سوی دولت ترامپ در چارچوب جنگ اقتصادی است؛ اشتباهی که کفه ترازو را به زیان طراحان آن تغییر خواهد داد و هزینه‌های سنگینی در پی خواهد داشت.
دشمن پیامدهای این محاسبات نادرست را در هر دو عرصه اقتصادی و نظامی متحمل خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/70825" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70824">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
مجدد صدای انفجار در جزیره لارک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70824" target="_blank">📅 00:23 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
