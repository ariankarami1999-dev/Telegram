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
<img src="https://cdn4.telesco.pe/file/vvfw7ntRoAepz1Vsp0rZHTiHO2Hjne4OkhFifluzDMaNAgETCZBIYjA_eMtHVBeR8szi-p746pPfCZ5K1n7jtix2L3MIsqv1PnsUI_ba3ioNvmdxNzT4iTgGfo9Le8YaLAYrTOghEnnl1pnqdy3m2dP7v4bG35nZ5ULL042ZPFPh5Z133V43WvB3COTIA1zddSbHwQv7782CpmsQZ7ANwbeVvqjtNdLQPvT7Wi_zZKfM6RpQoqJJB4dYA0EnG9p50avqlbA7Dyzfh34TAlLOIC087FJUERdVV7iL71g8U8DkFbgBfs0rnsv0nroqQQ85XOfChp2ZEgwBI-w7OGn96Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 73.7K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 19:20:19</div>
<hr>

<div class="tg-post" id="msg-652">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">WhiteDns-Windows-Setup.exe</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/652" target="_blank">📅 09:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">White DNS
pinned «
⚠️
اعلان مهم
📢
تمام تبلیغاتی
📰
که در این کانال قرار می‌گیرند، هیچ ارتباطی با ما ندارند
🚫
و ما هیچ‌گونه مسئولیتی در قبال محتوای آگهی‌ها، معاملات، خرید و فروش، یا هر نوع کلاهبرداری احتمالی
🎭
قبول نمی‌کنیم.  دلیلش ساده است: ما هیچ کنترلی روی تبلیغات ارسال‌شده…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/651" target="_blank">📅 07:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-650">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚠️
اعلان مهم
📢
تمام تبلیغاتی
📰
که در این کانال قرار می‌گیرند، هیچ ارتباطی با ما ندارند
🚫
و ما هیچ‌گونه مسئولیتی در قبال محتوای آگهی‌ها، معاملات، خرید و فروش، یا هر نوع کلاهبرداری احتمالی
🎭
قبول نمی‌کنیم.
دلیلش ساده است: ما هیچ کنترلی روی تبلیغات ارسال‌شده نداریم
🤷‍♂️
. این تبلیغات به صورت خودکار توسط خود تلگرام در کانال گذاشته می‌شوند
🤖
مسئولیت هرگونه تعامل، پرداخت یا ارتباط با آگهی‌دهنده، کاملاً بر عهده خود کاربران
👥
است
@whitedns</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/whitedns/650" target="_blank">📅 07:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-649">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.2 MB</div>
</div>
<a href="https://t.me/whitedns/649" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه 1.0.3
یک آپدیت متمرکز بر پایداری است. در این نسخه پایداری اتصال بهتر شده، مپ شدن تنظیمات Advanced اصلاح شده، تفاوت بین SOCKS5 و System Proxy شفاف‌تر شده، و احتمال حالتی که برنامه Connected باشد ولی سایت‌ها باز نشوند کمتر شده است.
WhiteDns Windows v1.0.3
- راهنمای سریع تست
لطفا برای تست اول این تنظیمات را استفاده کنید:
1. برنامه را باز کنید.
2. وارد بخش Connect شوید.
3. گزینه Proxy Mode را روی System proxy بگذارید.
4. وارد بخش Advanced شوید.
5. گزینه Transport preset را روی Balanced بگذارید.
6. این موارد را بررسی کنید:
- Compression = off
- Base64-encode data = Off
- DNS listener enabled = Off
- SOCKS5 authentication = Off
- Packet duplication = 0
7. در صورت نیاز ذخیره کنید و سپس Connect بزنید.
اگر سایت ها ناپایدار بودند یا باز نشدند:
- فقط همین یک مورد را تغییر دهید:
- Transport preset = Stable Iran
لطفا این موارد را گزارش کنید:
- آیا اتصال با موفقیت انجام شد؟
- آیا یوتیوب و سایت های عادی باز شدند؟
- از چه Proxy Mode استفاده کردید؟
- سرعت مرور مناسب بود یا نه؟
- آیا برنامه یا سایتی بود که با وجود Connected بودن کار نکند؟
@whitedns</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/whitedns/649" target="_blank">📅 07:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-648">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jXOPofesEsXBfLqRZI9zWVN2bjUhYMwsRMwTyljWiRNM9w2UMPbQB-CiiHuHCVbv4AAFMAxzNXW5n2bCgl1iegIYrISztoulnL4-FqMXbpb3OsI4-3FP-K3uaQ4gI60m4EYwFa1T-RKlSmWkTq1ANVUQ11Uzgweg356-8R37bMD2RE8TAZkSC5sSFwDyjepH1SEUqFWzFt7XdkXKLOzoTxgy4lLV-7nY_C9EWp-x4omYy2ICzfdt1QHTaDZnSNDCfoJR_6AgMq2lQOGzreP0S1dai4mv7HKGlJa1EHTnCVIaup3xmIWlwIjXE91glwLYBc7Gi5kMcbjFvv8ddRNROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/648" target="_blank">📅 07:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-647">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/whitedns/647" target="_blank">📅 04:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-646">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSOS Iran Connect</strong></div>
<div class="tg-text">🔶
خبرهای خوب:
۱. عبدالکریم، دوست بلوچ ما، تونست اپلیکیشن WhiteDNS را با کار تیمی دوستان راه بندازه
و وصل بشه
🎉
🗣
صدای خودشون، ۱۴۰۵.۰۲.۲۶، ۰۱:۵۲ ایران
۲. من داستان عبدالکریم روشندل را به Pedi جان در
@WhiteDNS
منتقل کردم، و دو درخواست مطرح کردم:
الف. داشتن رابط کاربری (user interface) پارسی در اپلیکیشن WhiteDNS.
ب. افزودن راهنمای پارسی به گیت‌هاب پروژه برای استفاده روشندلان با کمک ScreenReader.
ایشون از ایده‌ها استقبال کرد، ولی به زمان نیاز دارند.
⚪️
هدف دلی ما اینه که کاربرها خودکفا و مستقل باشند.
🫂
#همدلی
#ایران
💛
@WhiteDNS
🆔
@SOSIranConnect</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/whitedns/646" target="_blank">📅 03:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-645">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/whitedns/645" target="_blank">📅 01:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-643">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b77e656a8.mp4?token=kMYjByWhztJfFSAmUxi65TuLu69erhgsraAwncg-u-zVG3K25O2AW0JZz9vaduhQTbWhQFX2aBaVvUxM_W_5Lk9ldRvC1uFUTpbMmDctA0qH35o9sO2b799tMErUfY6oJXk7QdkrXIhGP0IKCX9ajm5zvt7tANz-LCSrdaO38nYpx7MZ3klDUjGkcccLRLtaxZiWDNJB5K32LMABvd-Izowl7_54mKkhWppS4dL5qbDSQiRkdpXWdOcE4mu4K9vpRqZFc5ut6KFUzJQjkJkX2KiteyhXnPB9Nt2jPna0b-uvDKbDf8gGrsxpmtkkypzdVyLY28CZrG_TlxojA7CKIHIq5LaLdAlVlOS-Ub62qdxN4NjRP0vWcByRsOf-LndZTz1zDkTX4l7tdf1pwqj7hsMhgwkRrIMdQ65iHgAcFlRrvEliOWogW400khNYcsYOEYF4lCPtPvEzudzXxriN-yiI5bFZTC0ny8uBX1frhhzxrjRETFUwHo2152EaGpF7r_jC8wbxLNuyGi3zv1f9Sapbr31XkLRuRugxi0gjDXvrBhHzoAdliG0GeMWLgZWVdrZ8l4bdOsi_BUAhJ22nHhy6yZpFX-axE6AXOQub6sSA4pQNOIsqAyUTGDuZNGCw8NykNVYacFeey_4udy9SE3zojHrPrgEhh2mu4a7cpL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b77e656a8.mp4?token=kMYjByWhztJfFSAmUxi65TuLu69erhgsraAwncg-u-zVG3K25O2AW0JZz9vaduhQTbWhQFX2aBaVvUxM_W_5Lk9ldRvC1uFUTpbMmDctA0qH35o9sO2b799tMErUfY6oJXk7QdkrXIhGP0IKCX9ajm5zvt7tANz-LCSrdaO38nYpx7MZ3klDUjGkcccLRLtaxZiWDNJB5K32LMABvd-Izowl7_54mKkhWppS4dL5qbDSQiRkdpXWdOcE4mu4K9vpRqZFc5ut6KFUzJQjkJkX2KiteyhXnPB9Nt2jPna0b-uvDKbDf8gGrsxpmtkkypzdVyLY28CZrG_TlxojA7CKIHIq5LaLdAlVlOS-Ub62qdxN4NjRP0vWcByRsOf-LndZTz1zDkTX4l7tdf1pwqj7hsMhgwkRrIMdQ65iHgAcFlRrvEliOWogW400khNYcsYOEYF4lCPtPvEzudzXxriN-yiI5bFZTC0ny8uBX1frhhzxrjRETFUwHo2152EaGpF7r_jC8wbxLNuyGi3zv1f9Sapbr31XkLRuRugxi0gjDXvrBhHzoAdliG0GeMWLgZWVdrZ8l4bdOsi_BUAhJ22nHhy6yZpFX-axE6AXOQub6sSA4pQNOIsqAyUTGDuZNGCw8NykNVYacFeey_4udy9SE3zojHrPrgEhh2mu4a7cpL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
دور زدن فیلترینگ با کانفیگ سرورلس با ترکیب nekobox و v2rayng
•
✅
لینک کانفیگ nekobox
•
https://pastebin.com/raw/rWeHKSt3
•
✅
لینک داخلی کانفیگ nekobox
•
https://seup.shop/t/exks1
•
✅
لینک کانفیگ V2rayNg
•
https://pastebin.com/raw/Yfymhyy5
•
✅
لینک داخلی کانفیگ‌ V2rayNg
•
https://seup.shop/t/k9mmj
❗️
هر دو کلاینت رو، رو حالتvpnبزارید .
📥
لینک داخلی ویدیوها
•
🎥
https://seup.shop/f/uns5
•
🎥
https://seup.shop/f/v4jx
•
𝕏 Irvictorious
kian
•
@ConfigWireguard
💎
•
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/643" target="_blank">📅 19:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-642">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">White DNS
pinned «
💥
💥
💥
💥
💥
💥
💥
برای تبادل نظر و همگرایی در گروه ما عوض شوید
🔄
👥
@whitedns_group
🌐
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/642" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-641">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">💥
💥
💥
💥
💥
💥
💥
برای تبادل نظر و همگرایی در گروه ما عوض شوید
🔄
👥
@whitedns_group
🌐</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/whitedns/641" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-639">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لیست ۱۰۰ ریزالور که طول ۲۴ ساعت گذشته به سرور های WhiteDNS وصل شدند
185.94.98.34
2.189.44.68
185.44.36.216
185.137.25.146
94.232.173.28
185.142.158.162
217.219.162.200
185.88.178.196
178.252.143.130
134.255.206.206
80.75.7.2
134.255.206.205
185.53.142.174
89.32.197.226
185.37.55.30
77.238.111.234
31.214.169.244
80.71.149.62
185.109.61.27
62.60.197.83
185.88.178.177
178.252.128.66
158.58.184.147
5.202.252.30
74.63.24.205
74.63.24.211
216.147.121.134
74.63.24.210
46.209.209.209
217.66.203.211
74.80.77.246
80.191.221.26
2.189.44.98
216.147.121.98
164.138.17.122
207.211.215.145
151.232.36.4
185.208.175.228
2.188.21.58
108.162.192.0
172.64.32.0
80.191.163.249
173.245.58.0
78.39.234.140
185.208.183.29
2.188.21.138
2.188.21.70
2.188.21.46
185.255.91.60
66.185.123.243
2.189.44.85
2.189.44.82
2.189.44.83
2.189.44.86
2.189.44.84
2.189.44.14
74.80.77.247
109.107.159.45
2.189.44.92
2.189.44.94
2.189.44.91
2.189.44.93
2.189.44.90
78.157.41.60
193.178.200.3
46.32.31.30
185.208.174.167
85.185.157.181
77.238.123.179
185.141.105.139
5.160.140.16
5.160.227.78
185.53.141.230
185.105.101.1
37.255.223.218
85.133.129.242
78.38.174.2
37.191.95.70
74.80.77.244
74.80.77.245
93.118.109.213
194.61.120.143
121.127.46.65
93.126.5.205
5.160.137.130
2.180.21.241
82.114.164.226
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/whitedns/639" target="_blank">📅 16:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-636">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سرور اهدایی از رسول عزیز از تیم وایت دی ان اس
Name: H3 (Germany)
Domain:
v.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Serbia
Domain:
v3.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Turkey
Domain:
v4.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: USA
Domain:
v5.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Switzerland
Domain:
v6.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: RMFT g1-7
Domain:
g1-7.rmft.tech
Encryption Key:
a337e9fa75161c44bebe7d717da36afc</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/whitedns/636" target="_blank">📅 12:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-635">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سرور اهدایی از چنل
@Masir_Sefid
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
Name:
@Masir_Sefid
🕊
(1)
Domain:
v1.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(2)
Domain:
v2.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(3)
Domain:
v3.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Name:
@Masir_Sefid
🕊
(4)
Domain:
v4.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(5)
Domain:
v5.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/whitedns/635" target="_blank">📅 12:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-633">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سرور اهدایی از چنل
@pythash
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
Domain:
v1.abolfazlshahi.cloud
Key:
a4c5649c628ac1103ad55c5208e0d74d
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
Domain:
v2.abolfazlshahi.cloud
Key:
965a568dccef58af7afb86e8ee55eea6
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/whitedns/633" target="_blank">📅 12:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-631">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AytMxCr0Kj1KI0SfGlS3XoL8nL_3G-8ix2aolfn2-Fy0SHBzEWvkPe8LLcWsS5kAGT6nfUlUzyHUzYYXh1fIyXxLdeZB7cQBRcE4PbPN0lFn-SAJA4fbI_EE71YkytuuPz11lMwp4pnWjYs7TGyAY7GX8HexvE5D__aJRNd5SYs9ggK8Gsojf4rTi45SwHoCTKplK2M1CEUKMLInK719IDcW_2fufeAE-9qRZ2H4MW_mb1e9UiT8DihXsybAmerSc0M13ANy8hRNGYYfOs2G02lOpl99tMx-Hp-9mz1nO7nrTzFDCOhwST-afSI0YzyGU7dUwfy9dphQzT8o45nopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q34zPYTTQ-Jcdn4_PxD2gNRbcQXzzyydK2zzFwTnyr4siSz26DPsmj0C3UQ2cUboSUpJINz1Tp87OLZ6cUgNWMm_zLbogEZkP1ij8NS2vlOtYGF2nib0De6_nnPlLnmwZhTCuC4HTn1MsDi-zbGb-NALAsooY4BSdewgRo3cq4UcW2s63ej2-KMHtVYDlmifP1rEiZdQj2j66EZB0f2hbeo9fllnWZy9Ejk-a7ogfBvUl0GrvkRqCohn60uvYt1sDDsbVXt2BfRALDkcns2NTavzbxtMTE6i4zMDEx7sIXWnZ2UEoHXBmh4MU2y_tZS_NQ4AGbl8TlRzHxMU_IItvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درحال حاضر نزدیک ۱۰۰۰ نفر فقط به سرور ما متصل هستند. سرور تا نزدیک ۲۴۰۰ نفر میتونه کاربر بدون افت کیفیت رو پشتیبانی کنه.
جدا از سرور های ما، سرور های اهدایی باقی چنل ها مثل مسیر سفید هم هست. ویدیو آموزش سرور اختصاصی هم پست های بالاتر گذاشتیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/whitedns/631" target="_blank">📅 11:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-630">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=a9y_EM8MjIzxCtEQEaTD1sdqNiaz3pBvZ6mTkh07wpdj_WSoxzkUDTNeuoLafx8iXe2G54ZPse5j6tc26mAY3nSVLhrpdzkdObUpc5CWO0cDp4RI51vuRkAPSWntH8XkjYyJDs13vHnawE5uaRJAvy9JD61UOEXVgp7UujTmBJ0MvzUasBFIKuolVOy42s16hJKdCVXzPjParILrdTHDtUVspjR-DxeSyQuwWMskrqCgGaK0X3eupA9nT8RSQHNLo9l1zcEOP8VZw25FH-toeqWzpKJdgUayqq3BbC9294etcQKUvb-1KkaP9KsC4-BKf-lUogf0EnSV4QWguHvKhA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=a9y_EM8MjIzxCtEQEaTD1sdqNiaz3pBvZ6mTkh07wpdj_WSoxzkUDTNeuoLafx8iXe2G54ZPse5j6tc26mAY3nSVLhrpdzkdObUpc5CWO0cDp4RI51vuRkAPSWntH8XkjYyJDs13vHnawE5uaRJAvy9JD61UOEXVgp7UujTmBJ0MvzUasBFIKuolVOy42s16hJKdCVXzPjParILrdTHDtUVspjR-DxeSyQuwWMskrqCgGaK0X3eupA9nT8RSQHNLo9l1zcEOP8VZw25FH-toeqWzpKJdgUayqq3BbC9294etcQKUvb-1KkaP9KsC4-BKf-lUogf0EnSV4QWguHvKhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.site
Encryption Key:
bad99364093861634030e96f11fe3132
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/whitedns/630" target="_blank">📅 11:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-625">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.3 MB</div>
</div>
<a href="https://t.me/whitedns/625" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان  نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
🤖
دانلود نسخه یونیورسال از سرور های داخلی
🔴
ویدیو آموزشی استفاده از اپلیکیشن…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/whitedns/625" target="_blank">📅 11:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-624">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEE0dlQRMt5d2qp64nEWdipBUSU_BhE5nP3vgV_DKJtEZ3wbDwGIOWpTVwkTEEMi5ma7kpG3t9bj2UR8eElwd7rkuq1e_W5dUHaSbEmAwrhEfMZnx6rmxi5sKs5VXmqIhSWC-B5Nh0PR7sxUlWZWNHzahS917DlCiVCRh6fu6Otk1AOUhJQqvD8f_X39qb5qdk2rx1Fsse4v5OYMuBf6eiNLORWzTvAT8eWolI-0sDmRX1qn8nDvrTiPw3mbNWDUNGgKd9WzkWiFQfgzNSVndTrGDucPNYgzeQmBQqemKifni_KbcS74mH7DgzQVLt3y6F3m6WXh4tbP0amYMSN8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
🤖
دانلود نسخه یونیورسال از سرور های داخلی
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
تمرکز اصلی این نسخه روی ساده‌تر شدن اتصال و پیدا کردن بهترین تنظیم برای هر کاربر بوده است. هدف این بود که WhiteDNS قبل از اتصال، چند کانفیگ مختلف را با Parallel Test بررسی کند، بهترین گزینه را از نظر سرعت و کیفیت انتخاب کند، و کاربران بدون نیاز به گشتن دنبال Resolver، با لیست پیش‌فرض ۴۵۰۰+ Resolver داخل اپ سریع‌تر اسکن کنند و راحت‌تر وصل شوند.
تغییرات این نسخه
:
✅
نسخه اپلیکیشن به 1.4.0 ارتقا پیدا کرده
✅
قابلیت Parallel Test برای تست هم‌زمان چند تنظیم مختلف قبل از اتصال اضافه شده
✅
حالا WhiteDNS می‌تواند قبل از اتصال، چند حالت اتصال را هم‌زمان بررسی کند
✅
اپ سرعت و Ping هر تنظیم را تست می‌کند و بهترین گزینه را برای همان اتصال انتخاب می‌کند
✅
قابلیت Parallel Test هم برای Proxy Mode و هم برای Full VPN قابل استفاده است
✅
در حالت Full VPN، اپ اول بهترین تنظیم را با Parallel Test پیدا می‌کند و بعد اتصال VPN نهایی را روشن می‌کند
✅
نتایج Parallel Test بعد از اتصال داخل صفحه اصلی نمایش داده می‌شود
✅
می‌توانید تنظیم موفق Parallel Test را با نام دلخواه ذخیره کنید
✅
چند تنظیم آماده WhiteDNS برای تست سریع اضافه شده
✅
می‌توانید پروفایل‌های تنظیمات پیشرفته خودتان را هم وارد Parallel Test کنید
✅
بیش از 4500 Resolver داخل اپ قرار گرفته تا برای اسکن و اتصال راحت‌تر استفاده شود
✅
لیست Resolver پیش‌فرض داخل اپ کامل‌تر شده
✅
پروفایل Default Resolver اضافه شده تا اپ همیشه یک لیست آماده Resolver داشته باشد
✅
امکان اسکن مستقیم لیست Resolver پیش‌فرض اضافه شده
✅
اسکن فایل‌های بزرگ Resolver سبک‌تر و بهتر انجام می‌شود
✅
ریزالورهای تکراری یا قبلاً پیدا‌شده بهتر کنار گذاشته می‌شوند
✅
شمارش Resolverهای سالم و ردشده در اسکن دقیق‌تر شده
✅
اگر پروفایل اسکن سرور یا کلید نداشته باشد، اپ واضح‌تر جلوی شروع اسکن را می‌گیرد
✅
ویرایش سرور، Resolver و تنظیمات از صفحه اصلی راحت‌تر شده
✅
امکان حذف پروفایل‌های اتصال تکراری اضافه شده
✅
پروفایل Default Resolver از حذف یا جابه‌جایی اشتباهی محافظت می‌شود
✅
هشدار باتری حالا قابل بستن است
✅
نمایش سرعت، مصرف اینترنت و آمار اتصال دقیق‌تر شده
✅
تنظیمات پیشرفته برای اتصال‌های کندتر و مسیرهای سنگین‌تر بهتر تنظیم شده
✅
وارد کردن و خروجی گرفتن فایل‌های TOML با گزینه‌های جدید کامل‌تر شده
✅
هسته داخلی StormDNS به‌روزرسانی شده
تنظیماتی که به صورت اتوماتیک انتخاب میشوند، تمرکز روی سرعت و کیفیت دارد. امکان افزایش مصرف اینترنت شما با کانفیگ انتخاب شده می‌باشد. اگر نگران این موضوع هستید تنظیمات را مرور کرده و مقدار  Upload Dup را کمتر کنید.
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/whitedns/624" target="_blank">📅 11:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-623">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu_Yq-gUjJTfDFVgdvlK_mnwJoSF5y5tdQmDLxfG7DQZwuB-T7c9BfEMO71iBfghO356Z8RRG6LSNfNTuvVi81DvUeFpxoP3YfNAgULYbl81tvQQW54NWySt8fHr0szrobHUJTSppGkZkNKsOcgBxv07bTX_PlqeP6M69nd3msCfEFPI3s6bwPcMgAnlB1a6QzjSfNo6oKalgaoO7rMK-PgTTVOWWT3bOvuO5dGVPG9S4UjWpC_Aqa-DdBLsQc6no9vXUHDttiqPSsRS-vBdVSfDqndoIlMubhxCJ-X3haCUFzHOOgdqR067t3cxyVUDSfb8t1L_EdLss1SVVzl49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن ۱.۴.۰ کلاینت اندروید WhiteDNS به‌زودی منتشر می‌شود. در این نسخه سعی کردیم کار شما را راحت‌تر کنیم و اتصال سریع‌تر و ساده‌تر انجام شود.
در این ورژن، اپ به‌صورت خودکار ۷ تنظیم مختلف را با قابلیت Parallel Test بررسی می‌کند و در نهایت بهترین کانفیگ را از نظر سرعت و کیفیت برای شما انتخاب می‌کند.
همچنین بیش از ۴۵۰۰ Resolver که قبلاً داخل بات و گروه منتشر شده بود، به‌عنوان لیست پیش‌فرض داخل اپ قرار گرفته است تا بدون نیاز به گشتن دنبال لیست، بتوانید مستقیم اسکن را شروع کنید و راحت‌تر وصل شوید.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/whitedns/623" target="_blank">📅 10:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-622">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9ZCDEaQ_sd_Dxg00zEl0ZIwQqEsIC4ujkSXsEdTgeaC5kensf6Y7CiH6u3EoeuhoPPpBhlXsk8cast5sZkYLhlQ-rIl-f_KHM5HwdmORI0iKzQjaY4DwjNypPodrxVgQYqs1Rr3h2p8xtJvcV_Nvb3fDiVmcY8ffSOtNCnkDvyKB5ZWkyxycUKKZgFZEpnxMEvNZqGmb076QGXGqfXu6q9-6cpCe6x3bqB8tZb5e2t3I3gUUMobe3Kdn55AiWlDhU4cZmOHrG7-PORE11TBLXVSEKJp2WWTUZEsiX1iDdeGg6aTvRcV2EmwFK_jui_aMY9A9zhdhjOkniT5WRY_Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.space
Encryption Key:
bad99364093861634030e96f11fe3132
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
این بزرگترین سرور ما هستش. ۱۲ هسته سی‌پی‌يو و ۲۴ گیگ رم.
✈️
هر مشکلی هست، از سمت اختلال شبکه، تنظیمات و ریزالور ها هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/whitedns/622" target="_blank">📅 07:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-620">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">StormDNS-Setup-Guide.mp4</div>
  <div class="tg-doc-extra">151.4 MB</div>
</div>
<a href="https://t.me/whitedns/620" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دوستان عزیز سلام
یک فیلم آموزشی آماده کردم برای نحوه راه‌اندازی سرور شخصی StormDNS/MasterDNS
دانلود سرور داخلی
https://guardts.ir/f/3c4216b2ea16
✍️
آموزش متنی
پیش‌نیاز:‌ تهیه سرور و دامنه خارج از ایران
1️⃣
آماده‌سازی DNS
ابتدا یک ساب‌دامین کوتاه بسازید و آن را به نیم‌سروری وصل کنید که به IP سرور شما اشاره می‌کند.
مثال:
ns.example.com  A   1.2.3.4
v.example.com   NS  ns.example.com
توضیح:
ns.example.com
باید به IP سرور شما وصل باشد.
v.example.com
باید به عنوان Subdomain Delegation به
ns.example.com
اشاره کند.
یعنی تمام درخواست‌های DNS مربوط به
v.example.com
به سرور شما ارسال می‌شود. اینترنت هم بالاخره یک جایی باید بفهمد با خودش چند چند است.
2️⃣
نصب سرور
روی سرور لینوکسی خود، دستور زیر را اجرا کنید:
bash <(curl -Ls https://raw.githubusercontent.com/nullroute1970/StormDNS/main/server_linux_install.sh)
بعد از نصب و اجرای سرور، برنامه به صورت خودکار کلید رمزنگاری فعال را نمایش می‌دهد.
همچنین این کلید داخل فایل زیر ذخیره می‌شود:
encrypt_key.txt
برای مشاهده کلید می‌توانید از دستور زیر استفاده کنید:
cat encrypt_key.txt
3️⃣
موارد موردنیاز برای اتصال کلاینت
بعد از راه‌اندازی، برای ساخت پروفایل یا اتصال کلاینت معمولاً به این اطلاعات نیاز دارید:
Domain: v.example.com
Encryption Key: مقدار داخل encrypt_key.txt
Server IP: 1.2.3.4
لینک داخلی:
https://guardts.ir/f/3c4216b2ea16
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/whitedns/620" target="_blank">📅 03:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-617">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nKxdZY10r6KW4AhHifyQV6P0_Oh3k9dYPTsfWetJRo2lL7hK4QGeJbBYfo3FcHu2_g7n3pw_Bei_3MN3KNm556u7PBRKm8-FZqgqEsNrJy9ONk6f2Nun21mhRIkve9GOPbekCC67PM68vkSv5Cr-fxQmIxcoqYqFFjI_LqAxTqAShSli3hzL4GwDsMpfChWOckMWMtS24zGwSWedTIwuMeh0cljSCPCNHZSTQ7zl8raj3Ft6lISOelsk4dirRIGb9Auoim4oPsUyYm1Tr8yA1AzICotW1s-sHD4YfoqzEkhU-F1srJTYKo63ycTQLspUZxTZjiKLAQJpoeI7nXo6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ql9if0Q1kxCjFYBsN-7O4kulHjXMJh-6iGBfkHlswL6ZquurHOgYRMWxehqVMsDdC4FhegS_fd9fAPFWj99tDk0wEwH0NN6n4HtHvfkA1VQpQ-sMwQxU08o-r1o5DiFsFIaIWtqRYv_aCA1Thg8v6gtXf_hEk7L1-4fnirQwoBSihy6wcjHnslCdYaOgeBdjRJLry9sa3y48Fs-7vygLn9AB4xZ4-NNQr1T5CNJ2JZdbIrGKZgds5IFkajRN9wHR7JN9axJ39U09Cl0ytZbYrC918nVD_ukA1xvQqC5CdQkZyIKNWxtZLk_Z6LlFXXtocnC7-Ig7LQowF59yQO7UVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داخل پروژه
TheFeed
که متعلق به
Sarto
عزیز هست یک فیچر برای ریزالورها وجود دارد. یک
جدول امتیازدهی برای ریزالورها
درست شده و بازخورد خوبی از سوی کاربران داشته بخاطر اینکه وضعیت ریزالورهای داخل جدول به طور واضح مشخص شده است.
همچنین خود برنامه به صورت رندوم از ریزالورهایی استفاده میکند که امتیاز بیشتری دارند تا کیفیت اتصال ریزالورها به
حداکثر
برسد.
متاسفانه اکانت گیتهاب
Sarto
ساسپند شده اما میتونید برای دریافت برنامه‌ی
TheFeed
به لینک زیر که پست کانال خود
Sarto
هست مراجعه کنید و ازش
حمایت
کنید:
لینک پست
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/whitedns/617" target="_blank">📅 00:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-616">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
آموزش خیلی مقدماتی و ساده برای استفاده از این نسخه
@whitedns</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/whitedns/616" target="_blank">📅 18:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-615">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">6.8 MB</div>
</div>
<a href="https://t.me/whitedns/615" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Whitedns windows v1.0.2</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/whitedns/615" target="_blank">📅 17:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-614">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/olslEINCovEF2NihU0cqUaL8SERmxQ4nmKTVahiyr2Ug3sJvj13jor5-TFqwXdRnkcU-binz20fg8oUD6lXxi0iQwFbNVFrxOz0xdMa_w8W7-cj7FRSCjkFGYEBCWFPIbjLYZeWUCylTo40dzRmdCdFMAj9WU3oz_ns2RdnoOijqXhg8iWS01lXf70qf_Fr_nQT57BwCCCdZ2mgQPNoHmMeOlGmy1yD3RG38XyEZNWAPJef-daduX6otb5d3bO3WhHYSIq6heZNbEEeQan8oB4wxuuYYLZX5BpvT63LgF2yQkzgM7Co68VC3u7fUYUU_5TR1bNA1lgJCBEgNGF0z0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
🔥
🔥
🔥
🔥
نسخه ۱.۰.۲ بر پایداری، قابلیت استفاده و تشخیص‌های بسیار قوی‌تر رزولور تمرکز دارد.
🛠
این بروزرسانی مشکل آکاردئون را در بخش تنظیمات پیشرفته اصلاح می‌کند تا بخش‌ها با قابلیت اطمینان بیشتری باز و بسته شوند و چیدمان تنظیمات رفتار سازگارتری داشته باشد. همچنین اسکنر رزولور را با یک حالت اسکن پیشرفته جدید بهبود می‌بخشد که رزولورها را به روشی واقع‌گرایانه‌تر و آگاه به تونل، با استفاده از دامنه فعال تونل آزمایش می‌کند، از جمله بررسی‌های DNS بدون کش، قابلیت EDNS0، یکپارچگی NXDOMAIN، مدیریت زیردامنه‌های تو در تو و جستجوهای پروب به شکل تونل.
🌐
تجربه نتایج اسکن نیز بهبود یافت. اکنون خروجی با اطمینان بیشتری کار می‌کند، مرتب‌سازی به درستی عمل می‌کند و نتایج صادر شده اکنون بهتر با آنچه در رابط کاربری نمایش داده می‌شود مطابقت دارند. جزئیات اضافی اسکن مانند امتیاز، دامنه پروب و قابلیت مشاهده بار EDNS اضافه شد تا رزولورهای قوی‌تر را با دقت بیشتری شناسایی کنید.
📊
✨
@whitedns</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/whitedns/614" target="_blank">📅 17:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-612">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/KLl3mEbYsH01I2QJbM2CGWrYy_WPxKtHoiKH7oyYqYKiknNmz-bWaLTjSAxDjUDCTJqHeZY7nqbBvciFJaVGPtR020LjnNUfJ4_Soe8ySulgzUe20iK7cAZ9WupiufvTfHA-lxVLqrFCdt53hfSn7PVbhFOZc-3IYXQnXk5JnaQV_5Ke_pGwXJ9QcfAv4ZSbw75aJPg6fS-4wHMe5RAbPmTBwRYSePn2qkplF4YX3WIhfmCu06vobTQGmgRL6YvoP8QBliGvydaPu96WKItBa8EhPwMeV_pHsfIxnU0Q3e7Tv4cUWfsYaMq5lfU5pvW8gG8Cyk1yqAc2kzRBSPUKLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/nEbgZ1YpuEwUVMU1exnMXuzxH-I-fsoO1Aj-NSw8U82DYxZdSlk8in5XliLRxXAhKquuSEvE2UCVS2hMO-QFS0trIJU2tZGPngQSiFiRpy5u6NmIHzt_T7Y0U54HlnoHfBGs2IF2Kg5MZ6TCZK-9pklDoGpuvsUPUq4R-KNjR2YLohqK4FSCBYjtAQAxkcmyq8umfCBlbxJmjZQVOGOLshljbWMA_kbdJ3GcUVTDZmIIkvCFAIMJ6YLlhz1F-tz4PsBi_rPGjpITa1eiYCr7ocZX9MM_TmtC0h_kk8Z6OoByzp_vDCyTY5N2t2oRZO3XsTkT1gzKt_21oWvd5sERUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">(موقت)
تنظیمات کلاینت Whitedns اندروید
همراه و رایتل و اپتل و مخابرات
یکی از اعضای عزیزی کانال "ارام " زحمت این کار کشیدید که از ایشون تشکر میکنیم
@whitedns</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/whitedns/612" target="_blank">📅 17:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-611">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/whitedns/611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛡
مهم: اگر این نسخه رو نصب کنید دیگه دردسر ستاپ کردن MITM و... ندارید!
این نسخه حدودا یک ساعت پیش توسط برنامه‌نویس شیر و خورشید آپدیت شد و به راحتی می‌تونید طبق این آموزش بهش وصل بشید:
1- وارد اپلیکیشن شیر و خورشید(آخرین نسخه که امروز منتشر شده) می‌شید
2- وارد بخش Options میشید از نوار بالا
3- روی More Options کلیک میکنید
4- گزینه‌ی  Connection Protocol رو قرار میدید روی CDN Fronting
5- میرید و عادی کانکت میشید و به راحتی وصل میشه!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/611" target="_blank">📅 16:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-610">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting-14.zip</div>
  <div class="tg-doc-extra">18.3 KB</div>
</div>
<a href="https://t.me/whitedns/610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">☠️
آموزش اتصال رایگان و نامحدود به اینترنت با متد ترکیبی MITM + Psiphon
⚡️
لینک‌های داخلی جهت دانلود: https://guardts.ir/f/db4006f1197c و https://uploadgirl.ir/d/1f4fb76a-c869-494a-b439-b11cb8d35947 (شامل فایلهای V2rayNG، کلاینت شیر و خورشید، ویدئو آموزشی،…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/whitedns/610" target="_blank">📅 16:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-608">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش اتصال رایگان و نامحدود به اینترنت با متد ترکیبی MITM + Psiphon
⚡️
لینک‌های داخلی جهت دانلود:
https://guardts.ir/f/db4006f1197c
و
https://uploadgirl.ir/d/1f4fb76a-c869-494a-b439-b11cb8d35947
(شامل فایلهای V2rayNG، کلاینت شیر و خورشید، ویدئو آموزشی، V2rayN و فایل Certificate Generator و خود فایل Json پترنیها)
لینک پروژه اصلی:
https://github.com/patterniha/MITM-DomainFronting
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از متد ترکیبی سایفون(کلاینت شیر و خورشید) + کانفیگ دامین فرانتینگ پترنیها، به اینترنت بین‌الملل وصل بشید!
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/608" target="_blank">📅 15:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-606">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXQ3lYnPhYi6aFmCMr9z4OcrS6CG5nJ2crktYABZpTyW2Q5mIIxS3COzMM7EWn9ZZdb3yLxafLJQZCSiMDhK9sqUQqhlZUuN0q8BYhldhg4XhTUbrRFC0B4Ngd97KxZH_oaa_aiLeNhvf_oL4nBUZ2Zts0YHZwfVMdZ_HJ2PQSAKMBBrgC-bVVHM53eKpuw4dWVpx0f4uCcBLEFFWHRu1g6oP3PGfz8WRM5HliQsooNAXhIqG5kFM6ISl7bHAX35NxE7kKWZ3Z5-bPrTMSdOyX9_QM2FAT_sWh6nWmB9r7CFySTdM3vWyskGK_hm3gS7fYCnUnYJQsdvEUZff2J9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.space
Encryption Key:
bad99364093861634030e96f11fe3132
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
این بزرگترین سرور ما هستش. ۱۲ هسته سی‌پی‌يو و ۲۴ گیگ رم.
✈️
هر مشکلی هست، از سمت اختلال شبکه، تنظیمات و ریزالور ها هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/whitedns/606" target="_blank">📅 09:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-602">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📢
اطلاعیه مهم برای کاربران WhiteDNS
دوستان عزیز،
برای بهبود کیفیت اتصال و افزایش پایداری سرویس، تمام سرورهای فعلی WhiteDNS به‌زودی پاک‌سازی و جایگزین خواهند شد.
✅
سرورهای جدید به‌زودی از طریق همین کانال در اختیار شما قرار می‌گیرند.
تا زمان انتشار سرورهای جدید، لطفاً فقط به سرورهایی متصل شوید کهآدرس آن‌ها
whitedns.shop
نیست.
یعنی فعلاً از اتصال به سرورهای دارای دامنه زیر خودداری کنید:
whitedns.shop
ممنون که همراه ما هستید
🤍
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/whitedns/602" target="_blank">📅 09:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-601">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mNEDUF6R-r0hUVopIyEJnvCvAd9bYOJ-UKoM8uL1JqnzVuQ-LqvyG4f55hcSI3VPG2EYKQkQGSG91JpmcWxB3z0OQYyhhtP7DUn25Ld6s38S5OkODX1ChqPQbzhzCibO_WBVqEk3j45deDtG14cAral9VY2BYj-PHHz2esasEM4r0s3CWxUhwkYYZwEz-7W3J9ypLGT2_GJWIg_eNTdOvRBPVxRCKzN2-gieRKrWJ2D5sK50hRJFUI_TEU36nw8FRzLJaR5suneVx0T0ZPzPkf9a_GklnLXCPBQ2sG0fbiyOF-_Tv5tMZF8SeL0tog0R3yC1WMAfMsJy-JhRWTlg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
به زودی.................
🔥
🔥
🔥
🔥
نسخه ۱.۰.۲ بر پایداری، قابلیت استفاده و تشخیص‌های بسیار قوی‌تر رزولور تمرکز دارد.
🛠
این بروزرسانی مشکل آکاردئون را در بخش تنظیمات پیشرفته اصلاح می‌کند تا بخش‌ها با قابلیت اطمینان بیشتری باز و بسته شوند و چیدمان تنظیمات رفتار سازگارتری داشته باشد. همچنین اسکنر رزولور را با یک حالت اسکن پیشرفته جدید بهبود می‌بخشد که رزولورها را به روشی واقع‌گرایانه‌تر و آگاه به تونل، با استفاده از دامنه فعال تونل آزمایش می‌کند، از جمله بررسی‌های DNS بدون کش، قابلیت EDNS0، یکپارچگی NXDOMAIN، مدیریت زیردامنه‌های تو در تو و جستجوهای پروب به شکل تونل.
🌐
تجربه نتایج اسکن نیز بهبود یافت. اکنون خروجی با اطمینان بیشتری کار می‌کند، مرتب‌سازی به درستی عمل می‌کند و نتایج صادر شده اکنون بهتر با آنچه در رابط کاربری نمایش داده می‌شود مطابقت دارند. جزئیات اضافی اسکن مانند امتیاز، دامنه پروب و قابلیت مشاهده بار EDNS اضافه شد تا رزولورهای قوی‌تر را با دقت بیشتری شناسایی کنید.
📊
✨
@whitedns</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/whitedns/601" target="_blank">📅 08:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-593">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.3.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.2 MB</div>
</div>
<a href="https://t.me/whitedns/593" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
تمرکز اصلی این نسخه روی اسکن Resolverها، مدیریت ساده‌تر پروفایل‌ها و پایدارتر شدن اتصال در خود WhiteDNS بوده است. هدف این بود که کاربران راحت‌تر Resolverهای سالم را پیدا کنند، نتیجه اسکن را ذخیره و دوباره استفاده کنند، و اتصال Proxy یا Full VPN در پس‌زمینه و بعد از قطع‌و‌وصل شدن مطمئن‌تر بماند. در کنار این موارد، امنیت خروجی‌ها، بکاپ و اشتراک‌گذاری فایل‌ها هم بهتر شده است.
✅
نسخه اپلیکیشن به 1.3.0 ارتقا پیدا کرده
✅
بخش جدید Scan برای بررسی و پیدا کردن Resolverهای سالم اضافه شده
✅
حالا می‌توانید فایل Resolver وارد کنید و اپ خودش Resolverهای سالم را جدا کند
✅
نتیجه اسکن به‌صورت خودکار داخل پروفایل‌های Resolver ذخیره می‌شود
✅
می‌توانید نتیجه اسکن را با نام دلخواه به عنوان Resolver Profile جدید ذخیره کنید
✅
Resolverهایی که قبلاً سالم شناخته شده‌اند دوباره بی‌دلیل اسکن نمی‌شوند
✅
امکان توقف اسکن و ادامه دادن آن از همان‌جایی که مانده اضافه شده
✅
سرعت اسکن قابل تنظیم شده تا بین سرعت بیشتر و مصرف باتری کمتر انتخاب کنید
✅
وضعیت اسکن با تعداد کل، سالم، ردشده و میزان پیشرفت واضح‌تر نمایش داده می‌شود
✅
می‌توانید برای اسکن، پروفایل سرور جداگانه انتخاب کنید
✅
اگر پروفایل اسکن سرور یا کلید نداشته باشد، اپ واضح‌تر هشدار می‌دهد
✅
حالت روشن، تاریک و خودکار برای ظاهر اپ اضافه شده
✅
مدیریت پروفایل‌های اتصال، Resolver و تنظیمات پیشرفته مرتب‌تر و راحت‌تر شده
✅
امکان وارد کردن تنظیمات پیشرفته از فایل یا متن TOML اضافه شده
✅
امکان خروجی گرفتن تنظیمات پیشرفته به فایل advanced_settings.toml اضافه شده
✅
خروجی گرفتن و اشتراک‌گذاری فایل‌ها امن‌تر و تمیزتر شده
https://dl.toolschi.com/view.php?f=e15bcec825298e4c.zip
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.3.0
از همراهی و حمایت شما ممنونیم
❤️</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/whitedns/593" target="_blank">📅 06:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-588">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بعد از اسکن بیش از
60,000
آی‌پی، تعداد
435
ریزالور سالم و قابل استفاده پیدا شد.
لیست این ریزالورها حالا از طریق ربات زیر در دسترسه:
@dns_resolvers_bot
برای دریافت لیست، وارد ربات شوید و دستور زیر را ارسال کنید:
/dns_master
بعد از ارسال دستور، می‌تونید لیست ریزالورها رو دریافت کنید یا فایل آماده رو دانلود کنید.
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
Source:
@WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/whitedns/588" target="_blank">📅 18:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-587">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سرور اهدایی از چنل
@pythash
از چنل اهدا کننده سرور حمایت کنید.
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
Domain:
v1.abolfazlshahi.cloud
Key:
a4c5649c628ac1103ad55c5208e0d74d
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
Domain:
v2.abolfazlshahi.cloud
Key:
965a568dccef58af7afb86e8ee55eea6
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/whitedns/587" target="_blank">📅 18:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-586">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های مخصوص وایت دی ان اس ورژن رسمی (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۳ اردیبهشت
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.2.0
⬅️
نحوه ی اضافه کردن پروفایل ها
⬅️
فیلم اموزش وایت دی ان اس
👍
تنظیمات مخصوص وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigxKSIsInNlcnZlciI6eyJkb21haW4iOiJ2MS5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigyKSIsInNlcnZlciI6eyJkb21haW4iOiJ2Mi5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigzKSIsInNlcnZlciI6eyJkb21haW4iOiJ2My5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig0KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NC5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig1KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NS5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/whitedns/586" target="_blank">📅 18:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-585">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UIvGINFOTXcvZivopplb6_OQHOHV5OFnbjayaYWIBn5N_QLi-f6u_cJIiqbyeS_G-xuYFGNPLadWici3Rr5LaIK2byZ3uWFP6_4Ds1BGF0NewFjL_8Bc7UIUF1OFEi1bcDmv4zRnj8gqRays7IJKiVTDCY84ZhzzLrSF04GMHiktzP3hav4IhsxUGgyn6Y4T8mrCMVNURnunHQlADvLbQU8HLh9vh0HnWc5_WwbncgukleXVBUwutjxKCTpUmrllkU8SbY1vMxpTXNrPsnM4KREiQWBtms61h61KoYuDMy20qMrcPf4s7vGpddSZlFBT3aJEjjpFwBSUXioR3FVrkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/whitedns/585" target="_blank">📅 16:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-584">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.1 MB</div>
</div>
<a href="https://t.me/whitedns/584" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
انتشار اولین نسخه ویندوز WhiteDNS
نسخه
WhiteDNS Windows V1.0.1
منتشر شد.
این اولین نسخه رسمی ویندوز WhiteDNS است؛ نسخه‌ای که برای شبکه‌های سخت، محدود و فیلترشده طراحی شده تا اتصال پایدارتر، سبک‌تر و قابل‌اعتمادتر فراهم کند.
در این نسخه تلاش کردیم هسته‌ی ارتباطی WhiteDNS را برای ویندوز آماده کنیم و امکانات اصلی را در اختیار کاربران قرار دهیم:
• انتقال ترافیک از طریق DNS Tunnel با سربار پایین و پایداری بهتر
• پشتیبانی از چند مسیر اتصال از طریق چند Resolver و Tunnel
• تشخیص سلامت Resolverها و غیرفعال‌سازی یا فعال‌سازی خودکار مسیرها
• مدیریت هوشمند MTU برای حفظ پایداری اتصال در شبکه‌های ضعیف
• بهینه‌سازی جریان اتصال برای SOCKS4 و SOCKS5
• سرویس DNS محلی و قابلیت کش DNS سمت کلاینت
• پشتیبانی از روش‌های رمزنگاری مختلف مثل AES، ChaCha20 و XOR
• استفاده از Wintun Adapter برای ساخت اتصال VPN در ویندوز
• مدیریت Route و DNS به‌صورت خودکار
• رابط کاربری دسکتاپ با امکان ساخت پروفایل، ذخیره‌سازی امن، Import/Export، ویرایش ساده و پیشرفته، نمودار زنده، لاگ‌ها و تنظیمات
این نسخه شروع مسیر WhiteDNS روی ویندوز است و مثل همیشه با کمک فیدبک‌های شما بهتر و پایدارتر خواهد شد.
اگر تست کردید، لطفاً نتیجه اتصال، لاگ‌ها و مشکلات احتمالی را با ما به اشتراک بگذارید تا نسخه‌های بعدی دقیق‌تر و قوی‌تر منتشر شوند.
لینک داخلی :
https://uplod.ir/8h2n22ficr8f/WhiteDns-Windows-Setup.exe.htm
Special thanks to
Masterdns
❤️
for their amazing work - without them non of this was possible
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/whitedns/584" target="_blank">📅 14:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-583">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/J_fPfIOVNw6e_5nEbUBCqMPKjEGAii469zOi8ydB0Ne3s7Vu9X3bsP881fmkK5IHlA2cSrrzdRmPgfSHez8cdqFRAlvYUfLIXVxCK0hN5aC6ghCUqLnAbTZIPiVC9NybkjN2CCvctBWHgh1In2CWfPDEDQsXJXcrvFcBSEom6QaKgemwuZs10s1dkfEAJrIBLEl7n1SJB8FTRvkO-LdVv71CUPyg5mJXF04ryXVkP63B92DagYoqWXClcW9hEFd4-oNl7F4Jn9GVvbFVaKrfcScC0HjldZnrWjDGiseQ3A4MdGq92yrcqCh1yskDosPlEtKr_q95plLotY4IJF9kJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/whitedns/583" target="_blank">📅 14:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-582">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSIBHAkIKn8BeCem_0wYbDpWQaYK6vsKH7lffXvxsnxSkG3X6CqLAYjhJdGGGL51Iqtg32nllYDD_JenyJLP2htghWDpznRhnkpdbpEr94RIbYd2B7TMqbQITxqOAG-ToAq69HX9FV1AokJufWlQGFyHVtw63ABR1vOHjteG2DfhJ1aKEsdOcs4PuxHUaLLWdTPYPo2ED6R-lcZkUrFoUre0Z9FvUNlFDvpkYSuSvCIUrUPIn6bfrnd-H7TzOUTqc33vj0zK4oTb7IT5H2KiGU_ukwby76wMwl05z5trhFjpuOoFlZ-PW16VIkCCmSpBCIu6hvgNM07gGP3uCs7xbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز،
یک نکته مهم را لازم دیدیم با شما به اشتراک بگذاریم.
بر اساس بررسی‌هایی که انجام دادیم، فیلترینگ دامنه‌های عمومی همیشه به‌صورت کامل و یکسان انجام نمی‌شود. در واقع این محدودیت‌ها معمولاً به‌شکل منطقه‌ای و بسته به اپراتور، مسیر شبکه و Resolverهایی که استفاده می‌شوند متفاوت است. اینترنت هم طبق معمول تصمیم گرفته مثل یک موجود عصبی رفتار کند.
برای مثال، اگر به وضعیت سرورهای WhiteDNS در تصویر دقت کنید، میزان لود شبکه یکی از سرورهای ما از حدود
4Mbps
به نزدیک
400Kbps
کاهش پیدا کرده است. این یعنی در بعضی مسیرها یا اپراتورها، دسترسی به برخی دامنه‌ها محدودتر شده یا کیفیت ارتباط افت کرده است.
به همین دلیل، ممکن است روی بعضی از سرورها تعداد Resolverهای کمتری دریافت کنید یا کیفیت Resolverها نسبت به قبل پایین‌تر باشد.
ما در حال بررسی راهکاری هستیم تا بتوانیم دامنه‌های سرورها را به‌صورت روزانه به‌روزرسانی کنیم و کیفیت اتصال را پایدارتر نگه داریم.
تا زمان آماده شدن این راهکار، می‌توانید از سرورهای کانال همکار ما،
@Masir_Sefid
، که در پست قبلی معرفی کردیم استفاده کنید.
تمام سرورهای ما و سرورهای کانال همکار، به‌صورت مداوم مانیتور می‌شوند تا در صورت افت کیفیت یا مشکل اتصال، سریع‌تر بتوانیم وضعیت را بررسی و اصلاح کنیم.
ممنون از همراهی و گزارش‌های دقیق شما
🤍
@WhiteDNS</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/whitedns/582" target="_blank">📅 10:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-580">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_xBGRdMmGdp2UNa_VU5OQnaCTgCE42e0bR7gN1_bw14DvqDz9VeaV9gSHuZnVebdGqB_b8ipmg8RbrAqtPRblWGB3RXOlIY-4yLh2cOdUxKkiLA2oMtvHp2LFHKNcs2PyCZrFgKPpy97Jjpjf2wiHnxInW0bhTa3hg-BGTT0rKcVnBveq-wAzpZuDTSp7vwy5GxPpijkdvmgb-JHTplJJEIu5UGZzafjmdFfOiKdo4k8TTXJlBqLdkUG0qS3_POUUZVSx92TQLpc9f5Jq11kDaLgH-wXPDr-rb4BLYk7Y8Oj2T9zXWa_8XvGLgOhzAxnUCzJc3jhemmDXY2Pn702w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات
@dns_resolvers_bot
اضافه شد
@WhiteDNS</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/whitedns/580" target="_blank">📅 05:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-579">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">به دلیل تعویض زیاد سرور ها توسط کاربران، تلگرام ممکنه بخاطر امنیت اکانت شما دستگاه شما رو از روی اکانت logout کنه و دیگه نتونید وارد اکانتتون بشید!
راه‌حل:
1. اکانت تلگرام خود را روی یک گوشی دیگر login کنید تا در صورت logout شدن شما بتونید دوباره به اکانت بازگردید.
2. رمز دو مرحله‌ای اکانت و ایمیل بازیابی را فعال کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/whitedns/579" target="_blank">📅 14:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-578">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olGVe3CUVV3-vXQWXAz7Ry2KbzHOsT_VX9RoVCVkHLt7hH2cyEp_UqTCQ__82jh1Wj9WtoirJUndL79ytQYFNzZGiXmflZRFh2uY9utcKhifHAY9EBwwlfrCxs4qnB9Y4hP2iGL754v85uaEph_H4IAnmlSHhXA_3PZpz986r2du5ge7DUMsiLaPiPwKuNpjUeUMAgyk02l-VhyS89ZYcipe0CV12_9QQHoC_dGhS2AtV0ibKWR_1-GyBXlWFJoor_uhKlrMYy3ZPPabVTYOzq_FhAif9W_Ae38hH_nW445uWT2VM9Ek7uYccGHz0M7zGnJhWPhRduQNeLim0a4bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
‏فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
‏ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام ⁧
#اینترنت_پرو
⁩ را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
‏ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
منبع
https://x.com/ircfspace/status/2054094958353678824?s=46</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/whitedns/578" target="_blank">📅 12:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-577">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-poll">
<h4>📊 آیا به اپ WhiteDNS تونستید وصل بشید؟</h4>
<ul>
<li>✓ آره</li>
<li>✓ نه</li>
</ul>
</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/whitedns/577" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-575">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt7J_mFffX_vD5_PjpTLMGkgRf71nHPlTXqSAj6dXRQEScAuuDF49aeVqVJuAR63aYw9CSMN93W_UkyqGJ-zXQ7hEOLpahMLj75hgxgyb6jmaB-JGPYRjPfq_LQ3ooQ89UDZPOUzD6bKITPkOJS0Bi6Iv-Jog78hs7mRDwy56aIfYwCNsKiVXomhJgIqBVdd0uBKOZfdeL-c59X2MpGTyx-rZYLgg7rALuoWSKehAtz0DYfINmxmiVYSioxhVdf77EqYDM5youEIsQx1fbQaCgJsi9X1CwgZCBWMpAH5XlvxG4X1-z5OB4FjPIWt4GHTwIpx3tCVR9hi6oALsYY_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای دریافت ریزالورهای MasterDNS / StormDNS در WhiteDNS
ربات WhiteDNS حالا امکان جدیدی برای دریافت ریزالورهای MasterDNS / StormDNS دارد.
برای دریافت لیست ریزالورها مراحل زیر را انجام دهید:
1️⃣
وارد ربات زیر شوید:
@dns_resolvers_bot
2️⃣
دستور زیر را برای ربات ارسال کنید:
/dns_master
3️⃣
بعد از نمایش لیست ریزالورها، برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید.
4️⃣
لیست کپی‌شده را داخل اپلیکیشن WhiteDNS وارد کنید و از آن برای اتصال استفاده کنید.
#آموزشی
@WhiteDNS</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/whitedns/575" target="_blank">📅 10:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-574">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚀
سرور اهدایی از چنل
@Masir_Sefid
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigxKSIsInNlcnZlciI6eyJkb21haW4iOiJzLm80cy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigyKSIsInNlcnZlciI6eyJkb21haW4iOiJzMi5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigzKSIsInNlcnZlciI6eyJkb21haW4iOiJzMy5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig0KSIsInNlcnZlciI6eyJkb21haW4iOiJzNC5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig1KSIsInNlcnZlciI6eyJkb21haW4iOiJzNS5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/whitedns/574" target="_blank">📅 09:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-573">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">White DNS
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/whitedns/573" target="_blank">📅 09:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-572">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9ad3f5766c.mp4?token=eRtqJZBqVZBJZxdrB0U1by4kyzXwO8BtmjH-FTFbrVLBTf2F8QuiYCoXoNoQCivp38a8aFEAz8ZLoQ6qmkYu1vr5RtyPP4c0tJlvIJ_7iRdhWp_-r8wVhTxH6Gtc0ezPixBvLfrWMIqLxdusoDF6wRiefbzF_-QDRaTGI3XOPbtlBbvTxm1mLei9fjpwUo4JeSrP2ia7Vl9RrhxUYwi9Zl5qM_r3DD0HEtdE_4s7TFH1FXI25QbMyQng-9Wd8C6l4pYRGyr9vETLr9uU-n_BKZTCc0gb3K9cbWd4zTvOxgPbIKoPxSAJdzAMNxuhmgEVA1oX9OYAmKqecUDarTK-gg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9ad3f5766c.mp4?token=eRtqJZBqVZBJZxdrB0U1by4kyzXwO8BtmjH-FTFbrVLBTf2F8QuiYCoXoNoQCivp38a8aFEAz8ZLoQ6qmkYu1vr5RtyPP4c0tJlvIJ_7iRdhWp_-r8wVhTxH6Gtc0ezPixBvLfrWMIqLxdusoDF6wRiefbzF_-QDRaTGI3XOPbtlBbvTxm1mLei9fjpwUo4JeSrP2ia7Vl9RrhxUYwi9Zl5qM_r3DD0HEtdE_4s7TFH1FXI25QbMyQng-9Wd8C6l4pYRGyr9vETLr9uU-n_BKZTCc0gb3K9cbWd4zTvOxgPbIKoPxSAJdzAMNxuhmgEVA1oX9OYAmKqecUDarTK-gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموژش نسخه جدید Whitedns
📲
✨
یکی از اعضای کانال آقا محسن زحمت کشیدند
👨‍💻
✅
نسخه اپلیکیشن به 1.2.0 ارتقا پیدا کرده
🚀
✅
حالت Full VPN کامل‌تر و پایدارتر شده
🔒
✅
حالا DNS هم داخل خود WhiteDNS مدیریت می‌شود
🌐
✅
دیگر برای باز شدن سایت‌ها و اپ‌ها نیازی به NekoBox، NVPN یا ترفندهای مشابه ندارید
🚫
✅
مشکل وصل بودن VPN ولی باز نشدن بعضی سایت‌ها و اپ‌ها برطرف شده
✅
✅
اتصال روی اینترنت‌های کند و Resolverهای دیرپاسخ بهتر کار می‌کند
⚡️
✅
صفحه اصلی ساده‌تر شده و انتخاب سرور، Resolver و نوع تنظیمات راحت‌تر انجام می‌شود
🎯
✅
اگر سرور یا Resolver درست تنظیم نشده باشد، اپ واضح‌تر نشان می‌دهد چه چیزی کم است
⚠️
✅
می‌توانید تنظیمات پیشرفته را با نام دلخواه ذخیره کنید
💾
✅
امکان ساخت چند پروفایل تنظیمات پیشرفته اضافه شده
📂
✅
می‌توانید هر زمان بین پروفایل‌های ذخیره‌شده تنظیمات پیشرفته جابه‌جا شوید
🔄
✅
امکان برگشت سریع به تنظیمات پیش‌فرض اضافه شده
↩️
✅
بعد از اتصال، نام پروفایل سرور، Resolver و تنظیمات فعال نمایش داده می‌شود
📋
✅
امکان خروجی گرفتن فایل client_config.toml از داخل اپ اضافه شده
📄
#آموزشی
@whitedns</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/whitedns/572" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/whitedns/567" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
تمرکز اصلی این نسخه روی بهبودهای داخلی VPN در خود WhiteDNS بوده است. هدف این بود که اتصال کامل‌تر، پایدارتر و مستقل‌تر شود تا کاربران برای باز شدن سایت‌ها و اپ‌ها دیگر نیازی به NekoBox، NVPN یا راه‌حل‌های مشابه نداشته باشند.
در این نسخه مسیر DNS و ترافیک داخل خود WhiteDNS بهتر مدیریت می‌شود، بنابراین تجربه اتصال ساده‌تر شده و کاربر می‌تواند مستقیماً از داخل اپ وصل شود.
✅
نسخه اپلیکیشن به 1.2.0 ارتقا پیدا کرده
✅
حالت Full VPN کامل‌تر و پایدارتر شده
✅
حالا DNS هم داخل خود WhiteDNS مدیریت می‌شود
✅
دیگر برای باز شدن سایت‌ها و اپ‌ها نیازی به NekoBox، NVPN یا ترفندهای مشابه ندارید
✅
مشکل وصل بودن VPN ولی باز نشدن بعضی سایت‌ها و اپ‌ها برطرف شده
✅
اتصال روی اینترنت‌های کند و Resolverهای دیرپاسخ بهتر کار می‌کند
✅
صفحه اصلی ساده‌تر شده و انتخاب سرور، Resolver و نوع تنظیمات راحت‌تر انجام می‌شود
✅
اگر سرور یا Resolver درست تنظیم نشده باشد، اپ واضح‌تر نشان می‌دهد چه چیزی کم است
✅
می‌توانید تنظیمات پیشرفته را با نام دلخواه ذخیره کنید
✅
امکان ساخت چند پروفایل تنظیمات پیشرفته اضافه شده
✅
می‌توانید هر زمان بین پروفایل‌های ذخیره‌شده تنظیمات پیشرفته جابه‌جا شوید
✅
امکان برگشت سریع به تنظیمات پیش‌فرض اضافه شده
✅
بعد از اتصال، نام پروفایل سرور، Resolver و تنظیمات فعال نمایش داده می‌شود
✅
امکان خروجی گرفتن فایل client_config.toml از داخل اپ اضافه شده
✅
ظاهر صفحه اتصال و دکمه Connect/Stop مرتب‌تر و جمع‌وجورتر شده
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.2.0
از همراهی و حمایت شما ممنونیم
❤️
1⃣
WhiteDNS</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/whitedns/567" target="_blank">📅 06:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-565">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همگی دوستان
🔴
11 سرور اختصاصی جدید و بهینه برای اپلیکیشن WhiteDNS
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidi53aGl0ZWRucy5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InYud2hpdGVkbnMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiYjA3ZGMzNTczNjBkNmU2ODk2NTA5MTM2ZDcwOTc4OTciLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEyLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEyLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjAwOWM1MTRiMmE2NDNlZDQwY2JkN2NjNjE5Mzg5YjBmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEwLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEwLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjFlY2Q1ZmRmZTM1MWE5MzEzY2VhMzlmZTFiOWM1OWRkIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjkud2hpdGVkbnMuc2hvcCIsInNlcnZlciI6eyJkb21haW4iOiJ2OS53aGl0ZWRucy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJhMmYzMzQ4YmZhMDIxNzA2Mzk5NzBmMmQ2M2YxMDNkYyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjExLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjExLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjRjMTY2OTMyNmNkYmU4OThjYWIwOTY1YWNlMzAxMGMwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEzLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEzLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImUyOTE4ODcwY2U4OGYwNTU0N2ZiZmJhOTlhZWU0ZWM1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE0LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE0LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjliODY3MmEzNTJkMDQwNDg5ZDk2YmU5ZGY5N2VkOTY2IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE1LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE1LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjlhYTY4ZTdlOWE3YzIyZDkxZDhmNDY2ZDY0YTM1ZGZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE2LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE2LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU5Mjg0NWNhMzhmMTk0NjEzODNkMDU3MzNjMzMyMTRjIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE3LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE3LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU3NjU1MDM1NGE3MzA5NTMwYjdmYTI1MTUyZGM2NzJmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE4LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE4LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImQwNTM4YTNkNTQ1YTc4MzBiOGJiMmViMGMzNzQ4ZTk1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
#Servers
@WhiteDNS</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/565" target="_blank">📅 14:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-564">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👇
👇
👇
👇
👇
👇
👇
👇
👇
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/whitedns/564" target="_blank">📅 12:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-562">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">امروز یک هفته از انتشار نسخه بتا۱ اپلیکیشن WhiteDNS می‌گذره
🎉
فکر می‌کنم برای شروع، اپلیکیشن مسیر خوبی رو طی کرده و این فقط با همراهی شما ممکن شده.
خواستم از همه دوستانی که در این مدت با دقت تست کردند، مشکل‌ها رو گزارش دادند و فیدبک درست و کاربردی به تیم ما دادند تشکر کنم. همین بازخوردها باعث شده هر روز بتونیم WhiteDNS رو بهتر، پایدارتر و کاربردی‌تر کنیم.
از اینجا به بعد، سرعت آپدیت‌های نسخه اندروید کمی کمتر میشه تا بتونیم تمرکز بیشتری روی توسعه نسخه ویندوز داشته باشیم.
از دوستان عزیزی که خارج از کشور هستند، همچنان درخواست داریم اگر امکانش رو دارند با دونیت سرور به پروژه کمک کنند. این کمک‌ها مستقیماً به بهتر شدن کیفیت سرویس برای همه کاربران کمک می‌کنه.
از دوستانی که داخل ایران هستند هم یک درخواست مهم داریم:
لطفاً فقط مصرف‌کننده ریزالورها نباشید. برای زنده نگه داشتن شبکه، باید مداوم اسکن انجام بدیم و ریزالورهای جدید پیدا کنیم.
WhiteDNS با کمک جامعه کاربری خودش قوی‌تر میشه؛ نه فقط با استفاده، بلکه با مشارکت همه ما.
ممنون از همراهی شما
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/whitedns/562" target="_blank">📅 10:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-561">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_Su21gEbXne_cxdWcpxeTMcViyvrnmNI1xIgK2_h6qKf2AUFTDS8kswQD19m7pFZz5YT3k1QOwXVgnHACA5BG_iHOeou4k0PQuWVmBS-mV5izQL4-1G0nFO4yvx8ZV5hc6D05YqoHAsUKk2xU-YcSwRfGjEg_dO9rbo8EAlk0mqWU__2lEbpyiseAkof7JZO48BGQL8P2benaqacsKoektLo7D_2ypDJNjemtQe_QeCIXaL0zNAFkk2Y1v9NIvllTTb1Xos8JIB4ImSmtbBiXdJpGfOxtTmYoIsDJUYNrICF_2T0Zct2h-HNpbtmK036d4DdxNtJwbKZLMlJwxrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
🙌
دکمه Donation به ورژن بتا۷ اضافه شده. هر کمکی  از سمت شما فقط هزینه ساخت سرور های جدید و بهبود اپ WhiteDNS خواهد شد.
هیچ اصراری برای کمک نیست و تیم WhiteDNS کاملا رایگان و تا اتمام قطعی اینترنت ایران ادامه خواهد داد.
ممنون بابت همراهی شما
🙏
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/561" target="_blank">📅 09:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-556">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.1.0-arm64-v8a-1778467437126.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/whitedns/556" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
هدف اصلی از انتشار نسخه ۱.۱.۰، رفع مشکل «وصل می‌شود و دیتا مصرف می‌کند، اما چیزی باز نمی‌شود» است.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
در این نسخه، اپلیکیشن بعد از اتصال وضعیت واقعی مسیر ارتباط را بررسی می‌کند و دیگر تلاش برای استفاده از Resolver یا تونل ضعیف و بدون پاسخ را بی‌پایان ادامه نمی‌دهد. اگر مسیر اتصال بعد از چند تلاش قابل استفاده نباشد، ارتباط‌های جدید رد می‌شوند و اتصال معیوب بسته می‌شود تا حجم بسته شما بی‌دلیل مصرف نشود.
همچنین هسته StormDNS در این نسخه تغییرات مهمی داشته و به همین دلیل اتصال بسیار سریع‌تر برقرار می‌شود. VPN/Proxy بعد از پیدا کردن حداقل Resolverهای سالم با MTU امن سریع‌تر فعال می‌شود و اسکن کامل Resolverها و MTU در پس‌زمینه ادامه پیدا می‌کند. علاوه بر این، اتصال‌های ناسالم زودتر تشخیص داده می‌شوند، مدیریت ارتباط‌های جدید پایدارتر شده و کتابخانه‌های native برای همه معماری‌های اندروید دوباره ساخته شده‌اند.
در این نسخه تمرکز اصلی روی پایداری بهتر اتصال، شروع سریع‌تر VPN/Proxy، مدیریت راحت‌تر پروفایل‌ها، اشتراک‌گذاری تنظیمات اتصال و عیب‌یابی امن‌تر بوده:
✅
نسخه اپلیکیشن به 1.1.0 ارتقا پیدا کرده
✅
مشکل گزارش‌شده‌ای که بعضی کاربران وصل می‌شدند و مصرف دیتا دیده می‌شد، اما سایت‌ها و اپ‌ها باز نمی‌شدند، برطرف شده
✅
حالا بعد از اتصال، مسیر ارتباط بررسی می‌شود و اگر تونل، Resolver یا مسیر خروجی پاسخ‌گو نباشد، اتصال‌های جدید به جای گیر کردن و مصرف بی‌فایده دیتا رد می‌شوند
✅
وضعیت سلامت اتصال داخل اپ نمایش داده می‌شود تا مشخص باشد اتصال واقعاً قابل استفاده است یا نیاز به بررسی دارد
✅
سرعت شروع اتصال بهتر شده؛ اپ بعد از پیدا کردن حداقل Resolverهای سالم با MTU امن، VPN/Proxy را سریع‌تر فعال می‌کند
✅
اسکن کامل Resolverها و MTU حالا در پس‌زمینه ادامه پیدا می‌کند و Resolverهای سالم بعداً به اتصال اضافه می‌شوند
✅
امکان روشن و خاموش کردن WhiteDNS از Quick Settings اندروید اضافه شده
✅
دکمه Disconnect به نوتیفیکیشن VPN و Proxy اضافه شده
✅
امکان Import پروفایل از لینک‌های stormdns:// اضافه شده
✅
هنگام Export پروفایل، QR Code نمایش داده می‌شود تا اشتراک‌گذاری راحت‌تر باشد
✅
ورود Resolverها ساده‌تر شده و حالا می‌توانید چند Resolver را با کاما، سمی‌کالن یا خط جدا وارد کنید
✅
پورت پیش‌فرض :53 به صورت خودکار مرتب و ساده‌سازی می‌شود
✅
اگر Resolver واردشده اشتباه باشد، اپ قبل از اتصال خطا را نشان می‌دهد
✅
تنظیمات پیش‌فرض MTU و پایداری اتصال بهینه‌تر شده‌اند
✅
مدیریت پروفایل‌ها هنگام اتصال بهتر شده و فقط در زمان Connecting محدود می‌شود
✅
بخش Split Tunnel و تنظیمات پیشرفته مرتب‌تر و جمع‌وجورتر شده‌اند
✅
بخش Logs به جای خروجی فایل، Diagnostics آماده و امن تولید می‌کند که اطلاعات حساس داخل آن مخفی می‌شود
✅
هسته StormDNS برای همه معماری‌های اندروید دوباره ساخته شده و پایداری اتصال بهتر شده است
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.1.0
از همراهی و حمایت شما ممنونیم
❤️
1️⃣
WhiteDNS</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/whitedns/556" target="_blank">📅 06:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-553">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfT1YED_KddBPEO_IN9POdw3qr-jZoMyncun73WNg_I8hRQdHXl2krA32WeBr2AxiwBrnoT7hfVJT9d6cN9qm2bVZwXpKTNNVsw-Z7KVwtF8gYiUDl7pq9UizXQktBVzO2bDdOFIAJHQb1fIHGcVPHLsdkgQdY8iqMDQp-S9xblnVtxn4WztnnlsIqFS4CB1nBOtIL30A_8saD9YkIOPXSB9CbM_95QQ7nKqDeerf44yuEWJ6fDSpztRv-wm5hxDOKYwe4Pk5I9P21QpTM452-bVAr4c7IvXeKRWE_w3sx-YGSBnJ-_nhXWaLv1BEVn5UObvWklrGkHDZrJNbz50CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام سرور هایی که داخل اپ بودن داخل تاپیک سرور این گروه هستند. لطفا عضو بشید و گفت و گو ها اصلی رو اونجا ادامه بدید.
1⃣
t.me/whitedns_group</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/whitedns/553" target="_blank">📅 15:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-552">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4sRd6jEm0WZO-vPi7J0RO9JoK7ZqIWcwGayQN39gCIC1grkGFMqcWjMYetP5w8ViQrQIFkHud9L1o9_Ob-ByGfjAMDjUDehqKib6rI2STakdikkd0mMwags5JkMrGCT7Zihl6jVFubxIabRg0G1S0xR9BXXIvpBM1oPSNWs7yK0SfgN3ncWVjExRokbwzqLuvKxDgFGTfBfv_sG8nPJHKAglCE0Ta-u4RKyy7ALqIEu0QIQuEmp9uklGPdwR5zhMIdPX_xkpiT9AnV2iCyxL9_5vayIqmLuUfuoFjDVVUfJpHx_OdwmepeWla5Kl2wuq0ZbrWKe6xhGgJ9Iv1c7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
🙌
دکمه Donation به ورژن بتا۷ اضافه شده. هر کمکی  از سمت شما فقط هزینه ساخت سرور های جدید و بهبود اپ WhiteDNS خواهد شد.
هیچ اصراری برای کمک نیست و تیم WhiteDNS کاملا رایگان و تا اتمام قطعی اینترنت ایران ادامه خواهد داد.
ممنون بابت همراهی شما
🙏
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/whitedns/552" target="_blank">📅 15:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-551">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/551" target="_blank">📅 14:01 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-544">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-x86_64-1778404214016.apk</div>
  <div class="tg-doc-extra">5.3 MB</div>
</div>
<a href="https://t.me/whitedns/544" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
انتشار رسمی WhiteDNS به صورت متن‌باز
دوستان عزیز،
پروژه WhiteDNS رسماً به صورت Open Source روی GitHub منتشر شد.
این نسخه، اولین ریلیز رسمی
1.0.0
بعد از ۷ نسخه بتا است و از این به بعد مسیر توسعه پروژه شفاف‌تر، عمومی‌تر و با مشارکت جامعه ادامه پیدا می‌کند.
در این نسخه، پروفایل‌های پیش‌فرض WhiteDNS از داخل اپ حذف شده‌اند
تا برنامه به شکل مستقل‌تر و عمومی‌تر قابل استفاده باشد.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
قبل از آپدیت به این ورژن ، تمام پروفایل های خودتون رو Export بگیرید. ورژن جدید دیگه سرور های WhiteDNS را در اپ ندارد.
ورژن جدید اپ Sign شده هستش و از لحاظ امنیتی بهبود یافته.
برای نصب، ورژن قبلی اپ باید به صورت کلی از روی دستگاه شما حذف شود.
از این ورژن به بعد، نیازی برای پاک کردن اپ در هر آپدیت نیست.
👆
👆
👆
👆
👆
👆
👆
👆
👆
👆
👆
👆
از این مرحله به بعد، توسعه‌دهندگان و کاربران می‌توانند پروژه را بررسی کنند، مشکل‌ها را گزارش دهند و در بهبود آن مشارکت داشته باشند.
🔗
GitHub:
https://github.com/iampedii/WhiteDNS
از همراهی و حمایت شما ممنونیم
❤️</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/whitedns/544" target="_blank">📅 12:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-538">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های مخصوص وایت دی ان اس ورژن جدید( 7 WhiteDNS)
👾
کلاینت :
WhiteDNS
1️⃣
|
WhiteDNS
2️⃣
⬅️
نحوه ی اضافه ی کردن پروفایل ها
⭕️
پست تنظیمات کلاینت
⭕️
پست تنظیمات بهینه تر
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oMSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoicy5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oMikiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczIubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oMykiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczMubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oNCkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczQubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oNSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczUubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
✉️
Channel |
@link_dakheli_app
| کانال
✉️</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/whitedns/538" target="_blank">📅 09:40 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-537">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سرور اهدایی از چنل
@pythash
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey
Domain:
v1.abolfazlshahi.cloud
Key:
a4c5649c628ac1103ad55c5208e0d74d
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/whitedns/537" target="_blank">📅 09:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-536">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سلام خدمت همگی دوستان
🔴
11 سرور اختصاصی جدید و بهینه برای اپلیکیشن WhiteDNS
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidi53aGl0ZWRucy5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InYud2hpdGVkbnMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiYjA3ZGMzNTczNjBkNmU2ODk2NTA5MTM2ZDcwOTc4OTciLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEyLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEyLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjAwOWM1MTRiMmE2NDNlZDQwY2JkN2NjNjE5Mzg5YjBmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEwLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEwLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjFlY2Q1ZmRmZTM1MWE5MzEzY2VhMzlmZTFiOWM1OWRkIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjkud2hpdGVkbnMuc2hvcCIsInNlcnZlciI6eyJkb21haW4iOiJ2OS53aGl0ZWRucy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJhMmYzMzQ4YmZhMDIxNzA2Mzk5NzBmMmQ2M2YxMDNkYyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjExLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjExLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjRjMTY2OTMyNmNkYmU4OThjYWIwOTY1YWNlMzAxMGMwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEzLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEzLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImUyOTE4ODcwY2U4OGYwNTU0N2ZiZmJhOTlhZWU0ZWM1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE0LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE0LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjliODY3MmEzNTJkMDQwNDg5ZDk2YmU5ZGY5N2VkOTY2IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE1LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE1LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjlhYTY4ZTdlOWE3YzIyZDkxZDhmNDY2ZDY0YTM1ZGZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE2LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE2LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU5Mjg0NWNhMzhmMTk0NjEzODNkMDU3MzNjMzMyMTRjIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE3LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE3LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU3NjU1MDM1NGE3MzA5NTMwYjdmYTI1MTUyZGM2NzJmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE4LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE4LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImQwNTM4YTNkNTQ1YTc4MzBiOGJiMmViMGMzNzQ4ZTk1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
#Servers
@WhiteDNS</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/whitedns/536" target="_blank">📅 07:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-535">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dE_s5gJXemLpbOkLf0_ch6nncvDzCbbjnqq3ZgXHyJcogq7i9K0l5ya4tj_Dxg9HolyMhhMsVUH8AdzQ-DFoJvKcpjrOQmgRluOT36ytceW-XU_GlfhjDe52xoVEW_SoxzD9SgaXY8bvbgfX64xNLodlMSR-bVMk6QmUCZgyE2Pfr1yUeoeGLPjgUq4Gn0IkokwmkhYhVCy48AIHt84S1oM59p_-nqOAOu4rqdXB7U6aZZDrPKsrzbefB_UvQO_1PuoUQS3_TAzn_ppuQsXGJssmqnBACobHpzo_aue5bnobJvUiyQHWBStws-ZolQD_5eRuEIorRn3Yq1FGS771Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه بعد از اسکن، DNS های سالم رو برای بعدا ذخیره کنیم؟
بعد از اتصال، زیر دکمه
Connect
یک عدد نمایش داده می‌شود.
اگر روی عدد بخش
Valid
بزنید، فقط لیست ریزالورهایی که با موفقیت تست شده‌اند نمایش داده می‌شود.
می‌توانید همان لیست را کپی کنید و با آن یک پروفایل ریزالور جدید بسازید. بعد از آن، هنگام اتصال، پروفایل جدید را انتخاب کنید.
با این کار هم اتصال سریع‌تر برقرار می‌شود و هم اپلیکیشن سبک‌تر اجرا می‌شود
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/whitedns/535" target="_blank">📅 05:18 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-533">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">White DNS
pinned «
سلام خدمت همه دوستان عزیز
🌿
برای اینکه مطالب، آموزش‌ها، فایل‌ها و بحث‌های مرتبط با WhiteDNS بهتر دسته‌بندی بشن و دسترسی بهشون راحت‌تر باشه، یک گروه جدید برای کانال ساختیم.   متأسفانه تلگرام این امکان رو به ما نمی‌ده که گروه فعلی رو به گروه دارای Topic تبدیل…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/533" target="_blank">📅 20:42 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-532">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سلام خدمت همه دوستان عزیز
🌿
برای اینکه مطالب، آموزش‌ها، فایل‌ها و بحث‌های مرتبط با WhiteDNS بهتر دسته‌بندی بشن و دسترسی بهشون راحت‌تر باشه،
یک گروه جدید برای کانال ساختیم
.
متأسفانه تلگرام این امکان رو به ما نمی‌ده که گروه فعلی رو به گروه دارای Topic تبدیل کنیم. برای همین، جهت حفظ بهتر مطالب و جلوگیری از گم شدن آموزش‌ها و اطلاعات مهم، لطفاً عضو گروه جدید ما بشید.
از این به بعد گفت و گو های اصلی تیم، آموزش‌ها، مطالب فنی و اطلاع‌رسانی‌های مهم داخل گروه جدید انجام می‌شه.
گروه فعلی فقط برای کامنت‌های مربوط به پست‌های کانال استفاده خواهد شد و فعالیت اصلی تیم در اون محدود می‌شه.
ممنون از همراهی همیشگی‌تون
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/whitedns/532" target="_blank">📅 20:38 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-531">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بازی ساده اس !ً مدت ها ذهن شما با قیمت vpn های هر گیگ 1 میلیون و یا 500 هزار و یا 200 هزار تومن عادت کرده بود
حالا وقتی vpn بشه هر گیگ 80 تا 100 کلی حس پیروزی و خوشحالی داری و مدتی لذت میبری ازش .
بعدش پیش خودت میگی خب میرم سیمکارت پرو میگیرم بشه هر گیگ 40 هزار تومن و اون لحظه اس که دیگه حسابی خوشحال خواهی بود چون با نصف قیمت VPN دیگه اینترنت داری  !
حالا اینکه روزی سه چهار گیگ میتونی در روز مصرف کنی و 11 برابر گرون تر از 3 ماه پیشه که اینترنت وصل بود دیگه اصلا به ذهنت نمیرسه چون مدت ها درگیر بازی قیمت توسط حکومت بودی
اینجوری چرخه بردگی تا ابد ادامه پیدا می‌کنه
حالا فهمیدید چرا ما با هر رانت دولتی مخالفیم ؟
@whitedns</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/whitedns/531" target="_blank">📅 19:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-530">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سوالات پرتکرار مربوط به برنامه‌ی WhiteDNS
این تلگراف به مرور تکمیل تر شده و سوال های بیشتری نیز داخل آن قرار خواهد گرفت.
@WhiteDNS</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/whitedns/530" target="_blank">📅 16:17 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-529">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/529" target="_blank">📅 16:15 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-527">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8Ml_CmafD3cP_OPPiHucQsddz_Pc2U2EEJcPId5hJDEh1O2A3KW05VevNv5BzIxHHmMZ5m8eTnAdLXlzFk2q_pR4u8ATFyLkpIU5CeP3kvgQdccy948JVvBHQUXZs8BkL3JdIByZQh__qRNb-HvhLbfLMh42mpJ9HNHKCQeVQrscKnhv1uQRtg38JCqc7rAiw63Adg7fNhsDiWEu-b7a_I-te9xfHmg0jWCAGn0qk6CUhpzHjt6cVCQqhYqpYy863VJTAhlaWefFd7V-3mDRI9QhmUFfKQBqbkWzxYp5dxhnZDm4I4NmBZKicRz_8nI2nGrRkouuRlOd0IdR7hBGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
🙌
دکمه Donation به ورژن بتا۷ اضافه شده. هر کمکی  از سمت شما فقط هزینه ساخت سرور های جدید و بهبود اپ WhiteDNS خواهد شد.
هیچ اصراری برای کمک نیست و تیم WhiteDNS کاملا رایگان و تا اتمام قطعی اینترنت ایران ادامه خواهد داد.
ممنون بابت همراهی شما
🙏
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/whitedns/527" target="_blank">📅 13:36 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-525">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsQqqBcM0hN1AAeKpdl1g-o2JQwuJCLOYIuGA8-QyszqafI0vTTdB0zAepWU8TLBrQNXqS7-mxfr9XVHL80kTexjPb8oL8WknvVpzJQKscHRaM1BRFWYh2Hq2nSUVV_nzglKq_II9C6qQYfmeVaABAXxhCLYIVFElsRGF_QvCLPC7mGX4StFVXxtfQDg1gtMaMfm7W0bri2PX4KHEEruhXzppoJn3BRSjfbPgxd_zOEZkIKZepD5fvF62D8waHEZBhIST07bvk8-vL-IJ6R4ZWhOzhGLnaAp6psiGToBLHhmhwWY11X2nbmMCdKe8PsyOx3U6wSM_d9PY7ptnBpAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ربات WhiteDNS حالا امکان جدید دارد برای دریافت ریزالور های MasterDNS / StormDNS
۱) وارد بات زیر شوید
@dns_resolvers_bot
۲) متن زیر را برای ربات ارسال کنید
/dns_master
۳) برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/525" target="_blank">📅 10:43 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-523">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/523" target="_blank">📅 10:15 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-521">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTcND5o1jKG7gOUKOt9bAGfa2lHTV37XZceKjC7aToaojON5R4EcdDzCW5WqFCfzPG0CGzWgmFtmr2vf_Zav2j-MVufp9eWfq3OJApoEdkvu-VmfB1ndoDoOGHu86ncVlHGVvhR_BoQWaoTaJhbWyoPE5Ve5L229PisC3wveKX1bcxxqeupAZBIcueG9QIB5evoiY1MnkfQMiUnMe51z0Tje2oniUJucH4WFRbaPDsL2L8mhB9n59lfkb-DiTl0FrXm9qX6IN6EG3yEvgAi8oTT-zYnaUPb0TluijgtraGpc4IgAU49oja1IcSoFS2YHStNPfofHSngfV197lkgo_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ سرور اهدایی از چنل همکار
@link_dakheli_app
برای ایمپورت ابتدا ورژن اپ رو به بتا۷ آپدیت کنید، سپس وارد بخش پروفایل بشید و بعد دکمه ایپمورت رو بزنید.
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidGUubGluay1kYWtoZWxpLWFwcC5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InRlLmxpbmstZGFraGVsaS1hcHAuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiZXUubGluay1kYWtoZWxpLWFwcC5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6ImV1LmxpbmstZGFraGVsaS1hcHAuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoic3IubGluay1kYWtoZWxpLWFwcC5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InNyLmxpbmstZGFraGVsaS1hcHAuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoicy5vNHMuc2hvcCIsInNlcnZlciI6eyJkb21haW4iOiJzLm80cy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbUNoYW5uZWxAbGlua19kYWtoZWxpX2FwcCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiczIubzVzLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczIubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
👾
لینک دانلود نسخه بتا ۷ از سرور داخلی
WhiteDNS
1⃣
|
WhiteDNS
2⃣
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/whitedns/521" target="_blank">📅 10:03 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-516">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta7-x86.apk</div>
  <div class="tg-doc-extra">22.8 MB</div>
</div>
<a href="https://t.me/whitedns/516" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید تستی WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
در این نسخه تمرکز اصلی روی مدیریت راحت‌تر پروفایل‌ها، اشتراک‌گذاری تنظیمات اتصال و پایداری بهتر بوده:
✅
نسخه اپلیکیشن به 1.0.0-beta7 ارتقا پیدا کرده
✅
امکان Import و Export پروفایل‌های اتصال StormDNS اضافه شده
✅
حالا می‌توانید تنظیمات سرور شخصی را به شکل لینک stormdns:// خروجی بگیرید و برای دیگران بفرستید
✅
امکان وارد کردن چند لینک پروفایل به صورت هم‌زمان اضافه شده
✅
دکمه‌های Copy و Share برای لینک پروفایل اضافه شده‌اند
✅
امکان Export All اضافه شده تا بتوانید همه اتصال‌های سفارشی را یکجا خروجی بگیرید
✅
پروفایل‌های اتصال حالا با کشیدن و رها کردن قابل مرتب‌سازی هستند
✅
Resolver Profileها هم حالا قابل مرتب‌سازی شده‌اند
✅
ظاهر بخش Profiles مرتب‌تر شده و دکمه‌های ویرایش، حذف و خروجی گرفتن واضح‌تر شده‌اند
✅
وضعیت پروفایل انتخاب‌شده و پروفایل فعال واضح‌تر نمایش داده می‌شود
✅
قابلیت Traffic Warmup اضافه شده تا بعد از اتصال، مسیر ارتباط سریع‌تر آماده شود
✅
قابلیت Keepalive اضافه شده تا با ارسال ترافیک سبک دوره‌ای، اتصال پایدارتر بماند
✅
Traffic Warmup و Keepalive هم در Proxy Mode و هم در Full VPN فعال هستند
✅
از تنظیمات پیشرفته می‌توانید Traffic Warmup را روشن یا خاموش کنید و مقدار آن را تغییر دهید
✅
نمایش لاگ‌ها و وضعیت اتصال سبک‌تر و مرتب‌تر شده تا صفحه هنگام دریافت پیام‌های زیاد روان‌تر بماند
✅
دکمه Donate اضافه شده و امکان کپی کردن آدرس‌های حمایت مالی داخل اپ وجود دارد
پیشنهاد ما این است که اگر فقط به تنظیم پروکسی نیاز دارید، همچنان از Proxy Mode استفاده کنید. حالت Full VPN برای تست وجود دارد و بهتر شده، اما چون کل ترافیک دستگاه را از تونل عبور می‌دهد ممکن است روی بعضی دستگاه‌ها یا شبکه‌ها سرعت و پایداری متفاوتی داشته باشد.
اگر سرور StormDNS شخصی دارید، حالا می‌توانید پروفایل اتصال خود را راحت‌تر با لینک stormdns:// ذخیره یا برای دیگران ارسال کنید. همچنین استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند فشار روی سرورهای عمومی WhiteDNS کمتر شود.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
#WhiteDNS
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/whitedns/516" target="_blank">📅 09:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-515">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pBq4A6rcG4ocBYBkgB4xwzhTGah9mChipFTEtYitTz9fboeLk_yurT_0S3_uFg2kILqgxhNtl-OvIuMKgRP5CuTfFEZjP7xqUcJ68LTT_mXTPiBB2gysSOBl479dAf_ozGHxraNO-VcCHZjF8ipWtBMMCfhLJ-aeOJp0oDG8JtIs67gGJn-qO3upCtgGXbUGjgXTFFaxo8mMB2lO1ezKQskBnD4xXS1PyeVNKaQ4-H3U2s9BAeHOtzNwqM37sxvxwACIAh3UFfrcX7ihlOn4XJxP5SM1mKCfogTzVL8I543OZNpRSoHlHuwz9vWQQesv2y12m82CBJxTXzprXY8cwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/515" target="_blank">📅 06:59 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-513">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❤️
سرور اختصاصی whitedns برای Slipnet
❤️
آموزش کامل :
https://t.me/whitedns/294
دانلود کلاینت :
https://github.com/anonvector/SlipNet/releases/tag/v2.5.3
User:
whitedns
Password:
whitedns
[dnstt-socks] Public Key: 1b23cc151ab07274a4f2623a94b7172d61803956fa068f5074e38ec5eb800516
[dnstt-socks]
slipnet://MjJ8ZG5zdHR8ZG5zdHQtc29ja3N8dC5pcmFubW90b3IuYml6fDguOC44Ljg6NTM6MHwwfDUwMDB8YmJyfDEwODB8MTI3LjAuMC4xfDB8MWIyM2NjMTUxYWIwNzI3NGE0ZjI2MjNhOTRiNzE3MmQ2MTgwMzk1NmZhMDY4ZjUwNzRlMzhlYzVlYjgwMDUxNnx3aGl0ZWRuc3x3aGl0ZWRuc3wwfHx8MjJ8MHwxODUuMjMwLjIxOS4xNjd8MHx8dWRwfHBhc3N3b3JkfHx8fDB8NDQzfHx8MHx8MHwwfHwwfHwwfDB8MTA4MHwwfHR4dHwxMDF8MHwwfDB8MHwwfDB8MHx8fDgwODB8fDB8L3wxfHw=
[noizdns-socks]
slipnet://MjJ8c2F5ZWRuc3xub2l6ZG5zLXNvY2tzfHQuaXJhbm1vdG9yLmJpenw4LjguOC44OjUzOjB8MHw1MDAwfGJicnwxMDgwfDEyNy4wLjAuMXwwfDFiMjNjYzE1MWFiMDcyNzRhNGYyNjIzYTk0YjcxNzJkNjE4MDM5NTZmYTA2OGY1MDc0ZTM4ZWM1ZWI4MDA1MTZ8d2hpdGVkbnN8d2hpdGVkbnN8MHx8fDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[dnstt-ssh] Public Key: 1b23cc151ab07274a4f2623a94b7172d61803956fa068f5074e38ec5eb800516
[dnstt-ssh]
slipnet://MjJ8ZG5zdHRfc3NofGRuc3R0LXNzaHx0cy5pcmFubW90b3IuYml6fDguOC44Ljg6NTM6MHwwfDUwMDB8YmJyfDEwODB8MTI3LjAuMC4xfDB8MWIyM2NjMTUxYWIwNzI3NGE0ZjI2MjNhOTRiNzE3MmQ2MTgwMzk1NmZhMDY4ZjUwNzRlMzhlYzVlYjgwMDUxNnx3aGl0ZWRuc3x3aGl0ZWRuc3wxfHdoaXRlZG5zfHdoaXRlZG5zfDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[noizdns-ssh]
slipnet://MjJ8c2F5ZWRuc19zc2h8bm9pemRucy1zc2h8dHMuaXJhbm1vdG9yLmJpenw4LjguOC44OjUzOjB8MHw1MDAwfGJicnwxMDgwfDEyNy4wLjAuMXwwfDFiMjNjYzE1MWFiMDcyNzRhNGYyNjIzYTk0YjcxNzJkNjE4MDM5NTZmYTA2OGY1MDc0ZTM4ZWM1ZWI4MDA1MTZ8d2hpdGVkbnN8d2hpdGVkbnN8MXx3aGl0ZWRuc3x3aGl0ZWRuc3wyMnwwfDE4NS4yMzAuMjE5LjE2N3wwfHx1ZHB8cGFzc3dvcmR8fHx8MHw0NDN8fHwwfHwwfDB8fDB8fDB8MHwxMDgwfDB8dHh0fDEwMXwwfDB8MHwwfDB8MHwwfHx8ODA4MHx8MHwvfDF8fA==
[slipstream-socks]
slipnet://MjJ8c3N8c2xpcHN0cmVhbS1zb2Nrc3xzLmlyYW5tb3Rvci5iaXp8OC44LjguODo1MzowfDB8NTAwMHxiYnJ8MTA4MHwxMjcuMC4wLjF8MHx8d2hpdGVkbnN8d2hpdGVkbnN8MHx8fDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[slipstream-ssh]
slipnet://MjJ8c2xpcHN0cmVhbV9zc2h8c2xpcHN0cmVhbS1zc2h8c3MuaXJhbm1vdG9yLmJpenw4LjguOC44OjUzOjB8MHw1MDAwfGJicnwxMDgwfDEyNy4wLjAuMXwwfHx3aGl0ZWRuc3x3aGl0ZWRuc3wxfHdoaXRlZG5zfHdoaXRlZG5zfDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[vaydns-socks] Public Key: ecef7073cd119405e62f1347daa949794193ccd618f0f879fa7c10da37a7f53e
[vaydns-socks]
slipnet://MjJ8dmF5ZG5zfHZheWRucy1zb2Nrc3x2LmlyYW5tb3Rvci5iaXp8OC44LjguODo1MzowfDB8NTAwMHxiYnJ8MTA4MHwxMjcuMC4wLjF8MHxlY2VmNzA3M2NkMTE5NDA1ZTYyZjEzNDdkYWE5NDk3OTQxOTNjY2Q2MThmMGY4NzlmYTdjMTBkYTM3YTdmNTNlfHdoaXRlZG5zfHdoaXRlZG5zfDB8fHwyMnwwfDE4NS4yMzAuMjE5LjE2N3wwfHx1ZHB8cGFzc3dvcmR8fHx8MHw0NDN8fHwwfHwwfDB8fDB8fDB8MHwxMDgwfDB8dHh0fDEwMXwwfDB8MHwwfDB8MnwwfHx8ODA4MHx8MHwvfDF8fA==
[vaydns-ssh] Public Key: ecef7073cd119405e62f1347daa949794193ccd618f0f879fa7c10da37a7f53e
[vaydns-ssh]
slipnet://MjJ8dmF5ZG5zX3NzaHx2YXlkbnMtc3NofHZzLmlyYW5tb3Rvci5iaXp8OC44LjguODo1MzowfDB8NTAwMHxiYnJ8MTA4MHwxMjcuMC4wLjF8MHxlY2VmNzA3M2NkMTE5NDA1ZTYyZjEzNDdkYWE5NDk3OTQxOTNjY2Q2MThmMGY4NzlmYTdjMTBkYTM3YTdmNTNlfHdoaXRlZG5zfHdoaXRlZG5zfDF8d2hpdGVkbnN8d2hpdGVkbnN8MjJ8MHwxODUuMjMwLjIxOS4xNjd8MHx8dWRwfHBhc3N3b3JkfHx8fDB8NDQzfHx8MHx8MHwwfHwwfHwwfDB8MTA4MHwwfHR4dHwxMDF8MHwwfDB8MHwwfDJ8MHx8fDgwODB8fDB8L3wxfHw=
@whitedns</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/whitedns/513" target="_blank">📅 05:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-510">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎁
۷ سرور اهدایی
با تشکر از رسول عزیز، یکی از اعضای خوب WhiteDNS
❤️
#Servers
🌐
Domain:
g1.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g2.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g3.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g4.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g5.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g6.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g7.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
@WhiteDNS</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/whitedns/510" target="_blank">📅 05:14 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-507">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانفیگ تمام سرور های WhiteDNS و اهدایی آپدیت شد
🚀</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/whitedns/507" target="_blank">📅 03:39 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-506">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دانلود WhiteDNS Beta6 از سرور های داخلی
📶
WhiteDNS Beta 6
1⃣
📶
WhiteDNS Beta 6
2⃣
منبع
@link_dakheli_app</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/whitedns/506" target="_blank">📅 18:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-505">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">White DNS
pinned «
سلام خدمت همه دوستان  ما تا امروز حدود ۳۰ سرور مختلف داخل کانال منتشر کردیم. بعضی از این سرورها داخل اپلیکیشن اضافه شده‌اند و بعضی دیگر از پست‌های فوروارد شده یا منابع مختلف بوده‌اند.  برای اینکه همه چیز یکجا و مرتب باشد، لیست کامل سرورها را اینجا قرار می‌دهیم.…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/505" target="_blank">📅 18:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-504">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سلام خدمت همه دوستان
ما تا امروز حدود ۳۰ سرور مختلف داخل کانال منتشر کردیم. بعضی از این سرورها داخل اپلیکیشن اضافه شده‌اند و بعضی دیگر از پست‌های فوروارد شده یا منابع مختلف بوده‌اند.
برای اینکه همه چیز یکجا و مرتب باشد، لیست کامل سرورها را اینجا قرار می‌دهیم. ممکن است کیفیت و پایداری بعضی سرورها در زمان‌های مختلف تغییر کند، پس اگر یک سرور کار نکرد، سرورهای دیگر را هم تست کنید.
ادامه داشتن این پروژه و وصل ماندن کاربران، مستقیم به حمایت شما بستگی دارد. اگر دانش فنی دارید و می‌توانید ماهانه حدود ۵۰ دلار هزینه کنید، با دونیت کردن ۵ سرور می‌توانید به وصل شدن تعداد زیادی از کاربران کمک کنید.
domain:
t1.prs612.us
Encryption Key:
3e80a0eb3e1fba2bf17e0e0eb5783dc5
domain:
t2.prs612.us
Encryption Key:
afc1bd5e98cd98cde7515adb7295122b
domain:
t3.prs612.us
Encryption Key:
8786a860148e2d4d55403ae3c80ba854
domain:
t4.prs612.us
Encryption Key:
943664f15fd1763e242ce12ba993d9c9
domain:
t5.prs612.us
Encryption Key:
6a9ab24a8bd3937378efbfb3c23e1358
domain:
t6.prs612.us
Encryption Key:
71201fedadfbc0b62189c08961bce651
domain:
t7.prs612.us
Encryption Key:
c4ff91174a79e9e03a4d6727878ada17
domain:
t8.prs612.us
Encryption Key:
ae5db6f03e485214e1fcc9d26a4c0a2f
domain:
t9.prs612.us
Encryption Key:
a01c03a340a3e684a2815961e086eb27
domain:
t10.prs612.us
Encryption Key:
f3a3c5d02bb7ce04f6a4f144fc35e9cb
domain:
t11.prs612.us
Encryption Key:
e7f2db07e778563d31ed1fc80d5fe612
domain:
te.link-dakheli-app.shop
Encryption Key:
TelegramChannel@link_dakheli_app
domain:
s.o4s.shop
Encryption Key:
TelegramChannel@link_dakheli_app
domain:
s2.o5s.shop
Encryption Key:
TelegramChannel@link_dakheli_app
domain:
v.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v3.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v4.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v5.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v6.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v.whitedns1.shop
Encryption Key:
c8328f9d541860df1637b9b3ed7b990e
domain:
v.whitedns2.shop
Encryption Key:
7ecd7b6271c47e348f6ab177517ee8fa
domain:
v.whitedns3.shop
Encryption Key:
9d7aedcaf1f94e784a24fdfc1348a337
domain:
v.whitedns4.shop
Encryption Key:
0ce14ab71acebbd46b8129e25593155a
domain:
v.whitedns5.shop
Encryption Key:
2dffd162cb02b278c1ab57ee17fe07ae
domain:
v.whitedns6.shop
Encryption Key:
e32afdaa30ca36ead696cd90d84ced15
domain:
v.whitedns7.shop
Encryption Key:
6394eec942238533798ec7524eb7ea66
domain:
v.whitedns8.shop
Encryption Key:
1c167e9850936655c480e4938b2c5c35
domain:
ob.networks.icu
Encryption Key:
3947d5ac68015a09a53a0b361bd82999
domain:
ts.networks.icu
Encryption Key:
e0e71e667e5dcfe3b18e3bce659773d2
domain:
zw.networks.icu
Encryption Key:
0798c0e8aa05080125e6c65282fd792b
domain:
v.0x0.guru
Encryption Key:
33815e1bcb88873f2199c735828ea745
domain:
v.iranmn.best
Encryption Key:
aaed913b8367fce3e20910472d9e3e2d
domain:
v.kmjhfilterchi.shop
Encryption Key:
4f3d0262ba2bd7cc20b596bdbc77f761
@WhiteDNS</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/whitedns/504" target="_blank">📅 18:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-503">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRVOWJwrtsbFcHYNl-exk_Udzd1P9KcrfP3tUHWcHuWsh2YJNTPtXDbbnBUEzGCbrrjdxCzGqTwQxmorf10up12AX12-Y9EQGAIvomTnjAmgpxjGDbFZ3qpF_Rru3MwQjrBG6H0jR-HwL_llUCXQvQNbxtxPA_OzBgOT-7_0SCdsDtzg_tzY8VG_2ra6LKPH5Vbc43pcLETV00qY8a0ECccDKPUcfnjMKMuo-Yd84neGmYKymHapzVF1jv3xjZqXXP4b36kcOJF3iH0uV_n4rSbE-bqqqu4QpUqxFu-8IaAyqDpmfDG70nqBcq5T--_blldChfNXkicdLq71S5SyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد
Advanced Settings
شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup: 1
🔸
Download Dup: 4
🔸
Upload Compress: OFF
🔸
Download Compress: LZ4
📊
این کانفیگ به‌صورت حدسی انتخاب نشده.
ما لاگ‌های سرور در ۷۲ ساعت گذشته را پردازش و بررسی کردیم و بر اساس پروفایل‌های موفق‌تر، MTUهای پایدارتر و مسیرهایی که سرعت بهتری داده‌اند، این تنظیمات را پیشنهاد دادیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/503" target="_blank">📅 16:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-502">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gfzwvtnIobn_rdGTYEdsb1bdbp8w0naofPWx-O0OymL-SdA4zXkY3CwiWVewmBmvHFIcnut4nF0zAIhNJlQIWe6QgKNMObAkENOtjCzWjeU1cM2hsKUggQ9n7Zgegi-xfR6qVmp74Ipde9-duCkOJcWDVAeKmGf7YBD3co614dURK5YmmGEGf1AI_TH162U94PIe9zXg3asUk_MyLAaF3dnYdX4wbwb6wJjSpFQOxJUAlv7HReqU8bV8Py_vBs0PpI4oRDduvLW-t-WZTeOstURLc1T0xuUWZkq1ZjxaxNQko6Ru4JUPWHyjhcNd-7mbQmQ9xokaCy7wdHOOfv7qkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به هر دلیلی میخواهید از حالت پراکسی در whitedns استفاده کنید بهترین کار استفاده از اپ نکوباکس هست   https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/tag/1.4.2  #Nekobox #Proxy #WhiteDNS  @whitedns</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/whitedns/502" target="_blank">📅 12:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-501">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/JCWFSE1n__XWrXiL2Y24JitenCwmRjmzImSzZJstaZn1XFQwRxpPJEHVsXNTafaNut1CjzMjwBafJxViF4R8F57zCaONEzmjHOxs35DOLanPI4dyVkcVnqs3Gl6IWVqaMtPm__yiCGB4HVP9WeP4WliuZvf5T1qNQUgxeTGVi_KFPjfe_aG9klvmTuEwbe_Ru1hcXTu2xFnSgPAlPOlGdB7q_tBcXrU8Yhaeb9Kk9DW8uzKAtrFp1a1Oe-2WvEIszodKmKAsFvCt8Hs11_J-nDCg1C_YgUUNbSZ03dXlH78aW4BmYjNHq0LA34mG2m_zlYPlRnGOAnDEH1ggQpzgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/501" target="_blank">📅 11:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-495">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromConfig plus</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rdPlPfmRhINzpkhjvzNioPE2VJK01dAurbN2wx6EC8xyjg2-pcGOJ29HvEE9bsKuHyW0IQO5EQ-bkSsv6zRDZBj1gWFVElwn2-TdvAG95ziammlTX4IrXrbYo75playf-CImRjoC7TzBGugTQtH3BE7lQ2SdZVm2bUA92s4RcHw1j-ZaqrhL_fRGezhOwxyoJNq1H8KGMR6yEGMil_xBSmr9eCrA0nmf7YHdIzGpx0RBeNwGakVK-X97_0daD7RRLq6Kf20tx_P4YuLh-rOZ8-AbGs8SIEfYOCFzX3VQ_1BiJfgCnYV28ceMp3mH7sjpr0QrtQTOi26Y-2Gt3-bqQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHxgfxAXzR0ZAtsOzQQ0_1jEN3qULg9Ml3iLO2WEadrosW5mvO3WFJPsSptQXmx3wSK2BV0cqFs4ZfP_j_MVNFPn3X7dxTYvqsCNJhTYOjah3dNaRV4kqqE99XsBA-t5JHQOMqyq94O0TER234IhWnfsINZL2nJpTNCFfvQJ3V471PyWwJnZahG7m_wjPgf2YLNW060QVE9Jm5MmB42CwTGjdxNe6p_dWOaAK9N9Lww8D8CA5w81mbAJSaNww2QnsHQ2fCVXkfLKUQP4xCfQxDJE3xpdElEPs_s2a5sXFqQlPi_LZPbO_0eD7d8LVxd-_YoJR0KT98OcpX6NmmuGRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYiwT345vGCItk54CNzqISX80_6gkRk5Xxxt3h25uA0u0OLhYTp4nlssNWRxrJGol81z-cK-8Z74DJjEBF12QQ18A4wX6cUgoKyH3thVroeDkGjS6fUZGqZdzglAkd-cjaNU1qwonkp_UUxTxfeGwNab8io5jnAgyLeZbmtfcastF5Fvsec1JU6gbX9s1bH_lGwUQPmRgDLqhEqI1dRFw4oatWHnegi89HsZuZPTZwm-tOShUF7kW6pnV1pPLimiZo7ou-GYSYLu2n5z6WkUlvsbI6VuUQXzZ3Bs59Zf5y4rUG7fLqq5XkUYTvYGS0BlSI-LKG39zEuG9QkNGJBGoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SEULwpxHEoeazcfQOjUoiyiaALRKZ1T9oaceNUvjoa2USvsx03XBKnqsJnBuEA-LqDSa8V7MC9NKyAmKNQmHn_bQ0Zp01HFnWgJvNVdhnSA9ukbdrHHSkIxRyAN333DUC3pBZgny8P-d25E_p2VQW-lOPvrPlhz45A86WD7-oRNOKGGu3wh0eFhkRWpIv_bghrNJrcvpFtjWoKlh4oQ4k_pj0m147AHy6DB8Ownn_xkzerwPxRPDT4J7vVKgAxMulrQV34Y5xsc18hFx5DA3WJ1Znl6sp9PEGVD1tNjHeztX9U4hCejLobmekwsGvxBeItG_bXjZosbXVpGfv-eRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYZSSEDieOyNPV98Y6Kk0VLbdMX2Gog5zwjz9pmmxHy_5YDx2Jn6sk68hq7Wr5mdVJYuPgaQCbN9vI6xonOY26kJlg3h3R8Dln9ygzzOBAYWwnUyHa7E3wVk--zP-Vlzsijz6_J16EPBxQ2wfY_H0EIO8ABE84FndfpA0M-gSqyqFVlROLAxB9o1TLGg6lF-AEg9WtPZ0g1KkqshEM9KsEWWjNJtJL8lnKursgcCpvzuUOmyCUXudmWi5ppnYm3ENbbjpQWmTGtU9_X1356tbE74zKNDuKMOx9V68zYhGLkILR-tqsfHz1fvB9OEJFKNtGnXO3SzlavX29JesDy_Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcE5oc5iRw1vlIWSA_gdkQntcLCFA8IIjqwY0nZK5wdFK30ZgTkjF5ItYsT-EeUq4hyCYENT3QrnZvD84SkRCKrrnoTiBD5xOz7Zon6fqP3Pfl0Cj79j7gAQKNDGTGlQVHGKfO2g_gLBPDdMKwx8_vm1Xp7EVccIT3F2t3KxRq9HuS2DsZsJfM6tt--qbhJNL3L5u53qAkoBu97zM9BmVR6TbDafzj9O8L10mozV9iyduGTTJRdETQ0gSRdlefQ2cnEc1b52FhdeTSmMDhuP-OR1ZuXzgtQd2rEfEkB7cr5lSUyP4adxspOwEkaylb1AG0sDqFQI_4jIWNBuyBcn0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔺
آموزش اتصال به برنامه whiteDNS در اندروید
1.ابتدا اول برنامه رو دانلود کنید از طریق لینک داخلی :
https://guardnet.ir/f/8f0ef50b3049
رمز فایل موقع استخراج:
3666
مطابق تصاویر بالا کانفیگ ها و ریزالوز ها را وارد نرم افزار کرده و تست کنید.
کانفیگ ها :
1- دامنه :
ob.networks.icu
🔐
کلید رمزنگاری :
3947d5ac68015a09a53a0b361bd82999
2- دامنه :
ts.networks.icu
🔐
کلید رمزنگاری :
e0e71e667e5dcfe3b18e3bce659773d2
3- دامنه :
zw.networks.icu
🔐
کلید رمزنگاری :
0798c0e8aa05080125e6c65282fd792b
اتصال برای تلگرام با پروکسی از طریق پورت 10886 و لوکال‌ هاست
127.0.0.1
به پروکسی زیر متصل شده و وارد تلگرام شوید و حدود 3 الی 5 دقیقه منتظر بمانید تا تلگرام آپدیت بخوره
https://t.me/socks?server=127.0.0.1&port=10886
این روش و برنامه برای تلگرام تست شده ولی خیلی خوبه ، برای اینکه سرعت بهتری داشته باشد در تایم شب بهتر عملکرد دارد و سرعت بالاتری دارد. اما در طی روز هم برای تلگرام برنامه جواب میده.
هر گونه سوال بود داخل دایرکت هستم :
t.me/Config0plus?direct
🟢
Join:
https://t.me/Config0plus
جهت حمایت از ما ری اکشن فراموش نشه</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/whitedns/495" target="_blank">📅 09:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-494">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سرورهای WhiteDNS تا امروز نزدیک به ۶ ترابایت دیتا جابه‌جا کرده‌اند.
این آمار فقط مربوط به سرورهای اصلی WhiteDNS است و دیتای سرورهای اهدایی داخل این عدد حساب نشده.
حالا بیایید خیلی ساده حساب کنیم:
اگر هر گیگ کانفیگ فیلترشکن را حدود ۲۰۰ هزار تومان در نظر بگیریم:
۶ ترابایت = ۶۱۴۴ گیگابایت
۶۱۴۴ × ۲۰۰,۰۰۰ تومان = ۱,۲۲۸,۸۰۰,۰۰۰ تومان
یعنی با کمک هم، تا امروز چیزی حدود ۱.۲ میلیارد تومان هزینه خرید کانفیگ را کمتر کرده‌ایم.
برای مقایسه، هزینه سرورهای ما نهایتا حدود ۳۰۰ دلار بوده.
اما اگر همین حجم دیتا را می‌خواستیم از فروشنده‌های فیلترشکن بخریم، با دلار حدود \`۱۸۰ هزار تومان\`، هزینه‌اش تقریبا می‌شد:
\`۶,۸۰۰ دلار\`
این یعنی با یک هزینه خیلی کمتر، چندین برابر ارزش واقعی سرویس به کاربران رسیده.
دم همه کسانی که تست کردند، گزارش دادند، سرور اهدا کردند و کمک کردند این مسیر ادامه پیدا کند گرم.
WhiteDNS رایگان ساخته شده، رایگان می‌ماند، و هدفش این است که دسترسی آزادتر برای همه راحت‌تر شود.
ممنون از سازنده های اصلی پروژه هایی مثل MasterDNS و فورک StormDNS
🙏
این اعداد فقط برای سرور های ما هست و نه سرور های اهدایی. اعداد واقعی خیلی بیشتر از این چیزا هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/whitedns/494" target="_blank">📅 09:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-493">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCVkdmD2igcvK8CKI6Oi-zmTWOFIinHrnxaht1vaqwJBE7a4VhAUbl3ICgY1dgYHYwRsmli2adzQE2Qv8xO_fYqcyNdxZDJo9hPdT1qSB14AkVvsMBFVoklNRhnSvJDwTx0M7zZwWMiots79yH8PgiQzzLdI4E6COYfNafJ4FhL5TPXvD4ICh9JWfXUuhW87Gf4L9brm1eoi8oeFcykPN2Ym8BzueHBL4ASrT26jICU2Ul14uEWcaa4lte72y-ms3w5oQ5fPM6t6OoihxayvSHqlWOjsl5lzW5YuyhdotL62gfJyNm0kDewJvnMCl5MWPzy9JmxQSeJxPiaWpKueiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ربات WhiteDNS حالا امکان جدید دارد برای دریافت ریزالور های MasterDNS / StormDNS
۱) وارد بات زیر شوید
@dns_resolvers_bot
۲) متن زیر را برای ربات ارسال کنید
/dns_master
۳) برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/whitedns/493" target="_blank">📅 09:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-491">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">server_config.toml</div>
  <div class="tg-doc-extra">11.1 KB</div>
</div>
<a href="https://t.me/whitedns/491" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
StormDNS Server Tuning برای لود بالا
پست مخصوص دوستانی که سرور شخصی دارند
!
ما برای سرورهای StormDNS یک اسکریپت تیونینگ آماده کردیم که هدفش پایداری بهتر زیر
فشار و کاهش قطعی کاربران است.
این اسکریپت چه کار می‌کند؟
👇
✅
قبل از هر تغییر، از فایل‌های مهم بکاپ می‌گیرد
✅
تنظیمات server_config.toml را برای لود بالا بهینه می‌کند
✅
تعداد UDP reader و DNS worker را بیشتر می‌کند
✅
صف پردازش درخواست‌ها را بزرگ‌تر می‌کند
✅
بافر UDP/socket را افزایش می‌دهد
✅
محدودیت فایل‌ها و پردازش‌ها را در systemd بالا می‌برد
✅
تنظیمات kernel/sysctl مخصوص UDP و شبکه را اعمال می‌کند
✅
پورت‌های DNS یعنی 53/udp و 53/tcp را در فایروال باز می‌کند
✅
لاگ را روی WARN می‌گذارد تا زیر لود، سرور با لاگ زیاد کند نشود
✅
تایم‌اوت اتصال SOCKS را روی 5s می‌گذارد تا مقصدهای خراب یا unreachable کاربرها را
مدت طولانی معطل نکنند
✅
در پایان سرویس stormdns را ری‌استارت می‌کند تا تنظیمات اعمال شوند
⚠️
نکته مهم: ری‌استارت باعث قطع شدن sessionهای فعلی می‌شود، پس بهتر است روی هر سرور در زمان مناسب اجرا شود
اگر نمی‌خواهید همان لحظه ری‌استارت کند:
sudo bash /root/stormdns_tune_all_servers.sh --no-restart
اجرای عادی:
sudo bash /root/stormdns_tune_all_servers.sh
📌
این تیونینگ جادو نمی‌کند؛ اگر مشکل از resolver، DNS delegation، مسیر اینترنت
کاربر، یا destinationهای خارجی باشد، فقط با افزایش منابع حل نمی‌شود.
ولی برای سرورهای پرلود، باعث بهتر شدن queue، socket buffer، limitها و رفتار اتصال
می‌شود.
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/whitedns/491" target="_blank">📅 08:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-490">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروح جنگلی👻</strong></div>
<div class="tg-text">اخرین اپدیت سرور های روح جنگلی از ۵ سرور ۳ عدد به استورم اپدیت شدن
سرور فنلاند
v.0x0.guru
Key:
33815e1bcb88873f2199c735828ea745
سرور فنلاند
v.iranmn.best
Key:
aaed913b8367fce3e20910472d9e3e2d
سرور آلمان
v.kmjhfilterchi.shop
Key:
4f3d0262ba2bd7cc20b596bdbc77f761
روح جنگلی
WhiteDNS</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/whitedns/490" target="_blank">📅 08:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-489">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nol1aQzO3124OM1JQSBsq_ZLVfI6ZGYuYnuYRZ3pnHS3CjPzBsBaV1-6gMDVUTi0msr1e1qZD-9ydCP4jdrV-UXOuWG8uyLlNdZq8Tkj7aKjjbNZVBENkoWyWayJlmgJkwTQcTKvMDB2Sqthnnf-5mXqdid2y4tmKShBxrgeSRoqgnGgzFv93JHbUl7KEhP8rq-gQhO6mCsmRoujc4kqE8-C-7QKBSsIO2ynfuu3SJbnPLxI9KLq0Ws3qC0Mpgmg3461i3yDa9FSA9X2rXrIiiKIYJnnilUCTANGgv3CjYakIEEYR7hC8IiWrAn0TjjklA1yTNeLWYiNxAEk5WKq3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همه دوستان
🌐
برای دریافت آخرین آپدیت‌ها، آموزش‌ها و اطلاعیه‌های مهم خارج از تلگرام، حتماً اکانت جدید ما در X رو دنبال کنید:
🔗
https://x.com/WhiteDNS_Team
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/whitedns/489" target="_blank">📅 07:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-488">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد Advanced Settings شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup:…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/488" target="_blank">📅 05:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-487">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/487" target="_blank">📅 05:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-486">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M35hoDjYmAgCbuXyAo-GLAtFsg-KCMRRuKTRnkYk7FycNRotU72OGF5mP_-c10V1Kcb5zlO8nmE7WSXAymv-HJ7h8Stow82MF22YRPZO1D0tDbzAeQrDHf5gREmp4NM6Jh36vjLAKlke8Ig8uAaphCBxCH1Iu_KwdVncZpMzvhUva1SDVF3_pQVukrQsRThIaMRkCegL2ueBpS9BGgBbkPU3mS1lCGzOpc0qEwnYqbNQ1crZv-CCyqHs8Rafrla6D8-oZaioC93UHyWf3eDBtFH_-p4MPGnyCPLOcA0nOv81cUhJZt-KhaYXwYHfaVNE78gQnn963b-ofEkaugyMFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد
Advanced Settings
شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup: 1
🔸
Download Dup: 4
🔸
Upload Compress: OFF
🔸
Download Compress: LZ4
📊
این کانفیگ به‌صورت حدسی انتخاب نشده.
ما لاگ‌های سرور در ۷۲ ساعت گذشته را پردازش و بررسی کردیم و بر اساس پروفایل‌های موفق‌تر، MTUهای پایدارتر و مسیرهایی که سرعت بهتری داده‌اند، این تنظیمات را پیشنهاد دادیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/whitedns/486" target="_blank">📅 04:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-485">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS_Resolvers.txt</div>
  <div class="tg-doc-extra">8.5 KB</div>
</div>
<a href="https://t.me/whitedns/485" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">۵۱۲ ریزالور جدید تست شده تیم  WhiteDNS
مخصوص اتصال StormDNS/MasterDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/whitedns/485" target="_blank">📅 02:44 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-478">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخدماتی حامد📱📶</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ejMJUMHzLDGywdruwTtkx15JNWirf0kIJrQhCzyHnXMCuQd5CyHEXpXCSKqKNG4n2GRh-v2HSS_3MA-bsnKs1tEOpTXIWQDUvIdvtro99Lq0pfSX8T00iymRtpGnV3JP3sxEIwsfmpxc6p4Ulm_GhLAXNovkHhHQhFVFIUq2jxqapNWyhBZwtC0FYBNKCcl9jBpVw77vF2EOfj7c-c7WSHaj44xvNR0_TiOPXKw4VYwaC8LK3u5hBIJrzqFBqG2vI52kyE30X13bapKkpJn80wSUmoXCLPsglJafSLphFum2FyNZoGdrpT9hFMP6PYg2KmzEg4JQrmTPdOQAz4lyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtZrEoP6lRxOsW7Kk85S43t9ESWpxIucJS42sbQEqzeCq94etl73_neM9odrIozPwh0JyngjKdOrlQxoTOkqnssm4MaDlnchU3IGKRfpcuso1v0FEU_gTXgfctTMIvf-GF_4EtVWvLUf7s71Yp2lYpBYgYaUtZ5BfBj0yheomz7x19VarXkAS8livWhlKOhsI088EAKud-f79Dts9CUvWo90HdH7ObVLC-e7KDLoWtYBKvMMcX_zLJQrWpVPEaLd5hfbfAi41itv1j5LoNptNtaAbk-QtB_fkKMaUSA5zS6x0AMoNyBX5AS3UjpUv-gExsmvmKw7-5OY7s7ATIGPOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpKPCWL1gIeT7hfJWvNRFwgUu0JGgJqCDo3CV7x2KXV0kjZkm1QqTxCUB1U2wWM9cJiwzQ7wbn_4_vFsDcgWu6Sr1TVOaN2ICH0N6pAIlj8KaxvPfo5N8lVEPfUE55kVgHaFTdcyS4CKTYzERd1lwmQTrvC6_Ttc6m6DdJjLb2sSVARFgqXJGvkS-i6VbTpuI7XQYrAeDwSQYOVIPprmXrEhSpF8hYoJNuK8IwfyrQWCGFVbS83FWuFYCKKexWOm3A1bMcUSty8YKnC02jvS7dmMHMjA7Wv1nwyZF2GglY4twMLnxI78iaQRV_ZW3uea_JBKJkDnSycxO1VOq43Obg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbvKjiyH9kPwBNASSGURdq-5XTrQ1pOEOLodlLHeNV_iW1n-PMong7pBe7aTJYw8BRSFjU7J3ae0pwNAVmPy0JkhN3piBHjFObZiCOZv3BUEj0wnrbq3zwSo5RUocJpuHTXe4lLHAaNZPhlmUUPH0oZ3-L7yKyrmojY1GtQ29ZUpVR8VcmmTHajCXHOIAtYwGw3UXqpRvKjZRnMYT7aqTZ-9fOjHjwUfJEycVB1Hp_YMVnuXHjBjfhvTNZJI0ihfb9H7hnQ7ePZ1Yk-ISjyaVCz0lL2ac_L5QN7LWzQVTcUy6vaVQNO9eBfpM0cYdrvxUCqHy2FAPYDTPD2pzjiQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCloRAxx9uNPsx3wN2_soD6yIuq-D-09CMKiMCdRCUJbR_APZta0K-qlIxEyhdvAfOR7OGgHLdcEa9yiqp_X-v1NpfKwfEyLoALiVmlqxXep3Yy5jXbulQmK61es5j8RoPLRElF7wgbj0qOtp_lOfDGAsL-G64BVaSAeK31d-lvKPtjkJ7s8ycdmPb7XI4z7ALfc4J75JEr7UgU3yTtbJV4bIJpSLTJlXlYVKLQlbL_Ru3TRm6-OzdZz-hHn7VNPGuBqQ7UxkAhHfkqGtYBmwt5hBAaidyli6GajUHI2jnN0PpF0qEK7cwErlBhB_NBkFF4cqGGt4RRhCb3BwQzHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8oPINLiEt2hHkKdAob9kbaBcm8wdxSP347f8jeENLTf7T5M8_DvLMZ0BeLPjdJvAPyoN3MUxQqaYRIqUdOAHKp3dX2a6OL-Je7qRKbHK2QrbiDAD7uqvGchX_F6cp8q2P79484FkYvVCPGrEUEfEkgl786bZatDhAB8EECQCNuHFhcvvJIOTEHv7ApYUew3JDlgi4NP5wqibMocEUvrMO8Tk0QEZKxDNHwOSJbU1N7MhvJttoNy1u5ugWpeaUNJ4rCPUVNG7mjtVgEcPAOY7VGgoQuERZh6mH6hTsJsiXeJZXTpdRn-_zxOVaWwbb01vxQlvipqrzAZ_L69m_JwuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش اتصال وایت dns در اندروید
1- نرم افزار را از آدرس های زیر یا پیام بعدی دانلود و نصب کنید. (White DNS)
لینک شبکه داخلی (بدون نیاز به فیلتر شکن)
https://dl.toolschi.com/view.php?f=48c485b41de6bf08.zip
https://guardnet.ir/f/Universal
رمز فایل : 3666
2- مطابق تصاویر بالا کانفیگ ها و ریزالوز ها را وارد نرم افزار کرده و تست کنید.
کانفیگ ها :
1-
🌐
دامنه :
ob.networks.icu
🔑
کلید رمزنگاری :
3947d5ac68015a09a53a0b361bd82999
2-
🌐
دامنه :
ts.networks.icu
🔑
کلید رمزنگاری :
e0e71e667e5dcfe3b18e3bce659773d2
3-
🌐
دامنه :
zw.networks.icu
🔑
کلید رمزنگاری :
0798c0e8aa05080125e6c65282fd792b
برای دریافت ریزالوزها از ربات زیر استفاده کنید :
@dns_resolvers_bot
اتصال این نرم افزار در اندروید روی پورت 10886 و لوکال هاست (
127.0.0.1
) است.
پروکسی تلگرام :
tg://socks?server=127.0.0.1&port=10886
‌‌
@hamedvpns
☑️
لایک   |   Like
👍
❤️
اشتراک بزارین   |   Share
⭐</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/whitedns/478" target="_blank">📅 02:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-477">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/whitedns/477" target="_blank">📅 13:21 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-476">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HwRxKP2QR4Z8awV3mm6HPbfYrDWHCQz8IP6xZkzo3iMPC_NArdl59GKK9kCTVJgeN1ym1memuXIJt_WHWA7HNS06Vfoxkep48esw912cTkfGQyhDF9fn3PDIyD-KWu_vF_fvv0VUGVaZEmuqUkW4u5soTQPA0nBytNYJ2eNzjXntzYX5bdp-w-2Hv-D2r0YEtEAe8o85ZB-3ZoEiD6jVgTT7GMEj0XMKnwRlunIm0Kzo74glDEDjtqncgDoRdgU-9KSeOmWt52TU8G93ZyJwuP4b1ZEAA6fgpODYwB0UPse_Bg1-_q1dhavMfu-sXjG8ArCMZrxv2hVtPbFPeXqimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/whitedns/476" target="_blank">📅 13:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-474">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pt3cX5DavzZBr_EmpllgRUyQyqw_9_TyjIF1Ldl_M0vIYN20NRxuOlqr6Ct2-YUc9KottJxooes1yxsznx7JgmZqiCusiVdd_MQZXdhWaDNHEQLzDQL18eIOaUG9hSWVu6wgcTiAFZcpusm817yp28cMBzU63lPFgnR3pgIGcT1tuq2aDMR3u1ob1Pv7WKpN2RnK7DSP19RJYRT4qjn5Xx4EIM9A66jhHYBzJ4DO4W3lCT44TajcxdDqOCq8cwiZRrLM7zWK-pActowARBazmrUqwRAr3aDiVnieJvjmPAg4cwzKc3WaMRIjKI2G0de0AbeqzMWBNgrvNqHo3Wllng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JieaT8qxp2E9JSbVzyrcDiGTrDXeC_U9m3EXAnkMc7kO5WLTd8_3Q4-hpIm8IzIGio31u02ahQqfO0-EJyI8iHSUjkAobgLENTkAWINz5YXVMKHWiDxwo9yc-q4uCm67s3yKuvfAyoKVViPvIQ0SKgKhLA4o3viCJFmCXuw_ivsS97RN09Mz7PYEtxswBfIK94XyVCXTKIQEEiwkXxKj5WwzlvA3aGzZonJdo85y6DGT8BvEPkrnoYR7q_NlMOpFStKzR2seI4iN-HR5CZzc1IbSDkdeHNUi9fFHy29Kx31-nz1PvGJrpaZfkxF_50heQzbqNImgqVRZ8yxvWLvxCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">╭────────────────────────────╮
⚡️
WhiteDNS Configs For StormDNS
⚡️
🔐
۱۰ کانفیگ‌های اختصاصی و پرسرعت ╰────────────────────────────╯  01.
🌐
Domain: t1.prs612.us
🔑
Encryption Key: 3e80a0eb3e1fba2bf17e0e0eb5783dc5 ━━━━━━━━━━━━━━━━━━ 02.
🌐
Domain: t2.prs612.us…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/whitedns/474" target="_blank">📅 12:31 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-473">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">╭────────────────────────────╮
⚡️
WhiteDNS Configs For StormDNS
⚡️
🔐
۱۰ کانفیگ‌های اختصاصی و پرسرعت
╰────────────────────────────╯
01.
🌐
Domain:
t1.prs612.us
🔑
Encryption Key:
3e80a0eb3e1fba2bf17e0e0eb5783dc5
━━━━━━━━━━━━━━━━━━
02.
🌐
Domain:
t2.prs612.us
🔑
Encryption Key:
afc1bd5e98cd98cde7515adb7295122b
━━━━━━━━━━━━━━━━━━
03.
🌐
Domain:
t3.prs612.us
🔑
Encryption Key:
8786a860148e2d4d55403ae3c80ba854
━━━━━━━━━━━━━━━━━━
04.
🌐
Domain:
t4.prs612.us
🔑
Encryption Key:
943664f15fd1763e242ce12ba993d9c9
━━━━━━━━━━━━━━━━━━
05.
🌐
Domain:
t5.prs612.us
🔑
Encryption Key:
6a9ab24a8bd3937378efbfb3c23e1358
━━━━━━━━━━━━━━━━━━
06.
🌐
Domain:
t6.prs612.us
🔑
Encryption Key:
71201fedadfbc0b62189c08961bce651
━━━━━━━━━━━━━━━━━━
07.
🌐
Domain:
t7.prs612.us
🔑
Encryption Key:
c4ff91174a79e9e03a4d6727878ada17
━━━━━━━━━━━━━━━━━━
08.
🌐
Domain:
t8.prs612.us
🔑
Encryption Key:
ae5db6f03e485214e1fcc9d26a4c0a2f
━━━━━━━━━━━━━━━━━━
09.
🌐
Domain:
t9.prs612.us
🔑
Encryption Key:
a01c03a340a3e684a2815961e086eb27
━━━━━━━━━━━━━━━━━━
10.
🌐
Domain:
t10.prs612.us
🔑
Encryption Key:
f3a3c5d02bb7ce04f6a4f144fc35e9cb
━━━━━━━━━━━━━━━━━━
11.
🌐
Domain:
t11.prs612.us
🔑
Encryption Key:
e7f2db07e778563d31ed1fc80d5fe612
╭────────────────────────────╮
🚀
Powered By StormDNS + WhiteDNS
📡
Stable • Fast • Secure
Configs by
@PersiaTMChannel
@WhiteDNS
#Servers
╰────────────────────────────╯</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/whitedns/473" target="_blank">📅 12:20 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-472">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGLYmBTsQGCpJoCJYsUGT4J8taHOKLlPUFIJq7ARpAD46_FYW-pwdiRYUjfrdPuLVT-UvN7DHQmFQb0cCs6HxTwqjQb-KsKAwgKvhpoym2DjYa_1RfjcrOTJp7GHTEjSzwSpNYNPtCJMixpTQRX-Gib1BnnX3wfflk2HGcQBEpnpHB2TOijHwkC49ieGcKZEWLPquZGa5ygNKxHNc4S3c4AQ3NwPHrOE8kyn0mX54KFexy7zjwtLnCDyGlcTOJePdmNg6kKnOMY-7MRsDfeS2QAMlGDBSWsm_3C9nSybMoro-4XfI_90ikPagG1bhAzcjSeBLSkxa08NZ9aqwpy4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteDNS روی گوشی مثل «کلاینت» کار می‌کند و به سرور StormDNS/MasterDNS وصل می‌شود. چون این روش ترافیک را داخل درخواست‌های DNS می‌فرستد، برای اینکه روی اینترنت ضعیف یا پر از قطعی پایدارتر باشد، بعضی پیام‌ها را چند بار می‌فرستد.
Upload Dup = 3 یعنی وقتی گوشی می‌خواهد داده‌ای به سمت اینترنت بفرستد، همان داده در مسیر DNS تقریباً ۳ بار ارسال می‌شود. سرور معمولاً نسخه‌های تکراری را تشخیص می‌دهد و فقط یک بار به مقصد واقعی می‌فرستد، اما حجم اینترنت گوشی قبلاً مصرف شده است.
Download Dup = 7 کمی اسم گمراه‌کننده‌ای دارد. یعنی خود فایل دانلودی لزوماً ۷ بار دانلود نمی‌شود، بلکه پیام‌های کوچک تأیید دریافت دانلود چند بار فرستاده می‌شوند. ولی چون هر پیام DNS جواب هم می‌گیرد، این هم می‌تواند مصرف اضافه ایجاد کند.
نتیجه: این تنظیمات می‌تواند مصرف اینترنت را خیلی بالا نشان بدهد. مخصوصاً با مقدارهای فعلی مثل Upload Dup = 3 و Download Dup = 7 و اندازه بسته‌های خیلی کوچک، داده به قطعات زیاد تقسیم می‌شود و روی هر قطعه هم هزینه اضافی DNS، رمزنگاری و تکرار اضافه حساب می‌آید.
برای مصرف کمتر، معمولاً بهتر است تست کنید با:
Upload Dup = 1
Download Dup = 2 یا 3
اگر پایداری هنوز خوب بود، همین مقادیر مصرف اینترنت را خیلی منطقی‌تر می‌کنند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/whitedns/472" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-467">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">22.2 MB</div>
</div>
<a href="https://t.me/whitedns/467" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه WhiteDNS Beta6 آماده دانلود است.
ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
لینک دانلود (Universal) :
https://guardnet.ir/f/8f0ef50b3049
رمز فایل:
3666
در این نسخه تمرکز اصلی روی پایداری اتصال و رفع چند مشکل گزارش‌شده بوده:
✅
نسخه اپلیکیشن به 1.0.0-beta6 ارتقا پیدا کرده
✅
قابلیت HTTP Proxy اضافه شده
✅
حالا علاوه بر SOCKS Proxy، می‌توانید از HTTP Proxy هم استفاده کنید
✅
صفحه اتصال حالا درصد پیشرفت را هنگام وصل شدن نشان می‌دهد
✅
هنگام اتصال، وضعیت بررسی Resolverها واضح‌تر نمایش داده می‌شود
✅
بعد از وصل شدن، تعداد Resolverهای فعال و سالم نمایش داده می‌شود
✅
امکان دیدن و کپی کردن Resolverهای فعال اضافه شده
✅
وارد کردن Resolverها بهتر و دقیق‌تر شده
✅
حالا اگر Resolver اشتباه وارد شود، اپلیکیشن بهتر آن را تشخیص می‌دهد
✅
امکان Import کردن لیست Resolver از فایل اضافه شده
✅
5 سرور عمومی جدید به مسیرهای داخلی اضافه شده‌اند
✅
پایداری جابه‌جایی بین Proxy Mode و Full VPN بهتر شده
✅
اگر اپ را ببندید و دوباره باز کنید، وضعیت اتصال فعال بهتر تشخیص داده می‌شود
✅
نوتیفیکیشن اتصال بهتر شده و وضعیت مصرف دیتا را واضح‌تر نشان می‌دهد
✅
هشدار Full VPN حالا قابل بستن است
✅
آیکون اپلیکیشن به‌روزرسانی شده
پیشنهاد ما این است که اگر فقط به تنظیم پروکسی نیاز دارید، همچنان از Proxy Mode استفاده کنید. حالت Full VPN بهتر شده، اما ممکن است روی بعضی دستگاه‌ها یا بعضی شبکه‌ها رفتار متفاوتی داشته باشد.
همچنین اگر سرور StormDNS شخصی دارید، بهتر است از سرورهای خودتان استفاده کنید. فشار زیادی روی سرورهای عمومی WhiteDNS وجود دارد و استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند سرویس عمومی برای بقیه کاربران بهتر کار کند.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
#WhiteDNS
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/whitedns/467" target="_blank">📅 11:22 · 17 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
