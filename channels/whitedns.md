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
<img src="https://cdn4.telesco.pe/file/bzJoFY1eX3WGBNne907e8Zj6-mXRDI10Vk9UCPW0LUCkaWxxMlu233jjCurAXFB51iw3jI0sIgjfyv0T_0T_y63Xt4FsrXgZof-j9wmSmDCmySLEEJIcW7ueEVllar_vthAGCUYcBhWsKkmrzBZqSXuLA3G8WwaLqgF2mKI7OVj3XMRzLm8SRwLsYNYbbdpISQyIo0QBmKm53DAUIVaSkmj1VRRdsX7Wg6c1HpaY57zf3rsko94RSiPw53YZa9_DAlf69wFDYjnmj-OARZC7heSqPWBE-X17eHZa3kMaTlZR_vYrxiQG0WYqOJ_Dy5BMqk3_pLWbkwzLnexzbfLKxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 16:32:15</div>
<hr>

<div class="tg-post" id="msg-1359">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1359" target="_blank">📅 10:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1357">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LKAhsF2c2AEgNMPI78cfcKbP4y09K4s3xpcLVuI93W-hJ3j6RHC1UHs-Lqy382xK8lUMpMHQ7rEPoDXRUcjxmruZEE-_HIT5qfaOr6WFQMJefFDsfRBAlABYVr0Yxrj3rn0ZXeKIxjhLoV9pEQcHi4pdamB4p2NZ9a64CXxc6wYJgYWIKU0Mu0V8SZxUTuqmzIXS8COFSTw5sJ6zTIy-T_aFFsYisXxc5K8XtZzYEkwnF-wBV9bG7zlc1UyfgdopHQV1QSkqXJvkeecxqT_jJfrcuisw6nXKkE8iKOCsZmKR8FU1YCY7l7mTKAY6HudeTl8an0zr7Xhwf0Qs-czJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/whitedns/1357" target="_blank">📅 04:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1356">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">خب با کمک دوست عزیزم Mr Arrow مشکل سرورلس (فرگمنت) هم تو نسخه
48
برطرف شد.
https://github.com/patterniha/Serverless-for-Iran
* نیازمند:
Xray-core >= 26.6.27
(v2rayNG >= 2.2.6)
* برای آپدیت کانفیگها کافیست سابسکریپشن را آپدیت کنید.
* نکات استفاده را حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/whitedns/1356" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1355">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">3 سرور اهدای CottenDNS
لطفا تست کنید و نتیجه رو بهمون بگید ( کلیک کنید روش کپی میشه )
Server #1 thx to Araskhatare
♥️
Location: Germany
🇩🇪
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imdlcm1hbnkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI5ODQ0NDhjZDRkZTYxZjgiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
Server #2 thx to Araskhatare
♥️
Location: France
🇫🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imdlcm1hbnkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI5ODQ0NDhjZDRkZTYxZjgiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
Server #3 thx to Araskhatare
♥️
Location: Israel
🇮🇱
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HrvCfh7EgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiIyMjRiOWU4MjVlMzFkNWY0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
@whitedns</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1355" target="_blank">📅 18:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1354">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/whitedns/1354" target="_blank">📅 13:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1353">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/whitedns/1353" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1348">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/whitedns/1348" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/whitedns/1348" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1347">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMbQfQ3JyLSb3clENqt2_b8UYtwpLRyX1M2E9B1gIabSue7QzPYRa6iEMwp9O2RLqgXWyy1xTyy0fvlf94uvqW6Y5PFSTRIZyqZg8i-raQDlQ2MN-6hRohit0GTWfZ7ccQczwOvhapqQ3fHJmtFjILnWh7mQXYJGpIfSxO1BO4bBmaUhklYxAdXIjMvQ6gOK93VKFS5tkbwtvhdkel6k4_KEBITMmRPVgbnV86f91_PHddR_VO-NeUKumdgJ4PaKZq8jW29243YmhvkOH1cvgf3FFhwrE3EguPOVYMXXuHaC6Vhk8cFZnSBytiVDJhRdzi_IB2Qcf20_unnlFf_0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/whitedns/1347" target="_blank">📅 10:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1346">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🌎
دوستانی که با جزئیات فنی پروژه آشنا نیستند، به زبان ساده
CottenDNS نسخه‌ای کامل‌تر و پیشرفته‌تر از پروژه‌های MasterDNS و StormDNS
است.
تیم ما طی چند ماه گذشته، با استفاده از تجربه‌هایی که از قطعی و اختلال گسترده اینترنت به دست آوردیم، روی توسعه و بهبود این پروژه کار کرده است تا اتصال پایدارتر و سازگاری بیشتری با شرایط مختلف شبکه داشته باشد.
نسخه جدید اپلیکیشن
WhiteDNS
که تا ساعاتی دیگر منتشر می‌شود، از سرورهای CottenDNS پشتیبانی خواهد کرد.
هم‌زمان با انتشار نسخه جدید، یک سرور عمومی CottenDNS نیز در اختیار شما قرار می‌دهیم تا بتوانید بدون نیاز به راه‌اندازی سرور شخصی از آن استفاده کنید.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/whitedns/1346" target="_blank">📅 10:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1345">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
معرفی پروژه CottenDNS
https://github.com/WhiteDNS/CottenDNS
نسخه پایدار CottenDNS با تمرکز بر اتصال بهتر و پایدارتر در شبکه‌های دارای فیلترینگ، اختلال DNS، پکت‌لاس و تأخیر بالا منتشر شد.
در معماری جدید، سرور به‌صورت پویا با تنظیمات هر کاربر هماهنگ می‌شود. یعنی کاربران می‌توانند بدون تغییر کانفیگ سرور، روش انتقال داده، نوع رمزنگاری، MTU، فشرده‌سازی و قابلیت‌های بازیابی بسته‌های ازدست‌رفته را متناسب با کیفیت اینترنت خود انتخاب کنند.
مهم‌ترین قابلیت‌ها
🔹
سازگاری با شرایط مختلف شبکه
اتصال می‌تواند از طریق UDP و TCP روی پورت 53 و همچنین DoT و DoH انجام شود. اگر یک مسیر مسدود یا دچار اختلال شود، کلاینت می‌تواند از مسیر جایگزین استفاده کند.
🔹
مقاومت بیشتر در برابر پکت‌لاس
CottenDNS با استفاده از ارسال مجدد هوشمند بسته‌ها، Duplication و فناوری FEC تلاش می‌کند اطلاعات ازدست‌رفته را بازیابی کند. این قابلیت‌ها بر اساس وضعیت شبکه به‌صورت خودکار فعال یا غیرفعال می‌شوند تا سربار اضافی ایجاد نشود.
🔹
مدیریت هوشمند Resolverها
Resolverها از نظر سرعت، تأخیر، پکت‌لاس و سلامت بررسی می‌شوند. Resolverهای خراب به‌صورت خودکار کنار گذاشته شده و پس از بهبود دوباره وارد چرخه می‌شوند.
🔹
تنظیم خودکار MTU
کلاینت اندازه مناسب بسته‌ها را برای آپلود و دانلود پیدا می‌کند تا احتمال شکسته‌شدن یا ازدست‌رفتن بسته‌ها کاهش پیدا کند.
🔹
مقابله با DNS Poisoning
با استفاده از روش‌هایی مانند Transaction ID تصادفی، EDNS Cookie، تغییر شکل درخواست‌های DNS و ارسال از چند دامنه مختلف، مقاومت اتصال در برابر پاسخ‌های جعلی و دست‌کاری‌شده افزایش یافته است.
🔹
انتقال داده با فرمت‌های مختلف DNS
داده‌ها می‌توانند با رکوردهای TXT، CNAME، A، NULL و HTTPS/SVCB منتقل شوند. کلاینت می‌تواند بسته به محدودیت شبکه بین این روش‌ها جابه‌جا شود.
🔹
امنیت و رمزنگاری
روش‌های AES-GCM، ChaCha20، XOR و الگوریتم‌های قابل تنظیم پشتیبانی می‌شوند. نوع رمزنگاری هر کلاینت به‌صورت امن و مستقل شناسایی می‌شود.
🔹
سازگاری با نسخه‌های قبلی
کلاینت‌های جدید CottenDNS و کلاینت‌های قدیمی MasterDNS و StormDNS می‌توانند هم‌زمان به یک سرور متصل شوند. بنابراین کاربران قدیمی برای ادامه استفاده نیازی به تغییر فوری ندارند.
در مجموع، سرور CottenDNS امکانات مختلف را فراهم می‌کند و هر کلاینت بر اساس شرایط اینترنت خود، بهترین ترکیب اتصال را انتخاب می‌کند.
❤️
Thanks to
@masterdnsvpn
@WhiteDNS</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/whitedns/1345" target="_blank">📅 10:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1344">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/i0lTaG79vFSZmZCyRffeUXIRnpoJdJGoSaU18uZIcc_BaVhVi9-lVqjkQTUbtlYfMBt7X7tOIUOwG-z0cpoLagibFewNeSAytBaUHorgOLNd6MYtCOABLLLis5F7oZLJl46cfPzXVzLin5zqMrYw5Ltlwex10MXRG_-7Hmr9BHuMcGwHpL4bZYV6jY-IKpK8xzCA13AXdc_VHYnsh17-XVhDlnxjFAwCSYE5ZJ28Qnn1ghECbLLOteYDNRJvMdzEIn_5V2vNRvmFd84XV0pfbxc7N4SpEgbglEnKyDaTYeKu6T9nxhk-yrzeifvlY9rka0Ov7IEkTvtYYWrLS8RJAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضویت
در گروه whitedns
در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/whitedns/1344" target="_blank">📅 09:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1339">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1339" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/whitedns/1339" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1338">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGLwvLMH7liyApWV3Z-aEF85aB8zHWxSaMDBmscKvS-bzrs1uck6EXbq1nmExkcC1V8_IZWtopFt5gbEVp_ovm6z89ZLCzd_o-MPJgc4PBNnhkQWyHBWkV8qPtzXca6fuU6MMZdFCQgob9oLbOW-YwyShdkPxzxvexvuE8PNuvPd2vtU_DFO_5NduGy7cxS-dILuLjI6AjmyuFcXSf0AL5V1mWq4fjcHQMdPDX5iBU-1WvGCOIXDYEM9_gcoqXJQ1H9j0uT0immaRxHyHdYgDviSXtTIFD-Sb6xFeQ0F0xYhHjPwrze_r09N-RLm3V8iHEJAD_SAzIyPcAQelbaFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN 1.1.0 منتشر شد!
در این نسخه چند قابلیت کاربردی اضافه کردیم تا اتصال راحت‌تر، سریع‌تر و امن‌تر باشه:
🛡
اتصال همیشگی VPN
می‌تونید WhiteVPN رو طوری تنظیم کنید که همیشه فعال بمونه و در صورت قطع شدن، دوباره متصل بشه.
🔒
امکان Kill Switch
اگر VPN قطع بشه، اینترنت هم موقتاً متوقف می‌شه تا اطلاعات شما بدون محافظت منتقل نشه.
⚡️
قابلیت Real Delay Test
حالا می‌تونید تأخیر اتصال‌ها رو بررسی کنید، نتیجه‌ها رو ببینید و سریع‌ترین گزینه رو راحت‌تر انتخاب کنید.
✨
طراحی جدید صفحه اشتراک‌ها
صفحه اشتراک‌ها ساده‌تر، مرتب‌تر و خوش‌دست‌تر شده تا مدیریت و انتخاب اشتراک‌ها راحت‌تر باشه.
همین حالا WhiteVPN رو به نسخه 1.1.0 به‌روزرسانی کنید
🤍</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/whitedns/1338" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1337">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uuMSVZUDej860BvCQEC2JG5y9Vj25E58UwoLdqvSoy4bSEhD2rJxCxCxejPKtEX5PYD4Js77VIQqEXImYNGCTLCp_NJx7zRn0GG5OZhQWuZlL6SwZ-EHaDDAWTA4yf9YYxTBAVINzGB9OCP4g9BHr9wtiunDriA3BnZkrorbsWoIDQLHaz7PCuQYEqZNXMEn6Ns24QPcurOrwH4too4gZSClKIGqsEODys7-cZe8TtMDCHw0xJ-5EBBZtCVXr-PUQ9aEdpXcgRk_gmJOK8u3OiUyQKgDYmkd6khIYSGutb_1FouaGmyJ0XvCKFX6TYdX_utn_d6Q9hVQY7XsktFpmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
👋
:
حالا همیشه هم پست برنامه و توضیح نگذاریم، بعضی وقتها یکم حرف بزنیم با هم، اینجا همه با هم داریم کار را جلو می‌بریم
🤝
✨
برای اینکه یک پروژه درست بشه ساعت‌ها وقت و هزینه صرف میشه تا به دست تو برسه
💸
⏳
، وقت و هزینه‌ای که میشد گذاشته نشه، زمانی که میشد در کنار دوست و خانواده بود و یا اصلاً رفت عشق و حال کرد
😔
💔
. اغلب دولوپرهای این تیم کلاً نیازی به بودن اینجا ندارند، فقط احساس دین می‌کنند
🙏
.
شما میتونی با لایک
👍
و دیس‌لایک
👎
، پروژه را تایید کنید یا ردش کنی و یا با قلب
❤️
حمایت کنی و ....
خطاب به اون چند نفر :
اینکه تو اینقدر بی‌شخصیت هستی که آیکن
🤮
می‌گذاری این فقط یک چیز را می‌رسونه، تو لیاقت این را نداری که کوچکترین خدماتی حتی با دریافت هزینه بهت داده بشه
🚫
🛠️
. تو همون کسی که اصلاً برات مهم نیست چی به مردمت می‌گذره، برات هیچی مهم نیست
🤷‍♂️
.
متاسفانه تو جرات نداری بیای توی گروه‌ها خودت را نشون بدی و بحث فنی کنی
💻
🛑
، والا تکلیف مشخص میشه.
یک تعداد زیادی از شماها که همراه ما هستند یکی از یکی خوب‌تر و مایه انرژی ما و بقیه هستید
🔥
⭐
، دلیل اینکه ادامه می‌دیم شماها هستید، والا کار ما خیلی وقت هست که تمام شد
🏁
.
ارادتمند
👋
ویسپر
🎤
تیم whitedns
🛡️</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/whitedns/1337" target="_blank">📅 08:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1335">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rNUiQwGgqU-Dzi1zRpmjksyfUVdZMESPmJkSDteLom_TzWEOQVjQ-wt24_jbcBYxp1bU8-mU5LeOYCW-IuhYZwKzJxWxABm8Wc8JeuUOTpu_-ikSQc78TBfm3y_PTS1QVKE4jpxh9N_Aq53C5s68BRDgU4CMaYmLpHVAX1wYk8wHqs5ZoYaPmqCYsDaHqH20S60K14dEh17hkM_moNA7cf6s2noo1A6Ngz4iutAvvch9wXnl2Bre_RKd98gFesnLoLz3tOCcPE7brWUOT_VyPXq1FOFT__fB9cIGcgN-_8PqBwiHEEZOd9XySr3xDM2ftrk0zfRPadvw1GsAFviX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Aether Desktop اومد! — آزادی، با یک لمس
🔥
بالاخره نسخهٔ ویندوزی Aether رسید!
🎉
همون اپ محبوب اندرویدی، حالا روی ویندوز — با همون ظاهر، همون آیکون و همون هستهٔ قدرتمند. نسخهٔ 1.0.0 اولین انتشار دسکتاپه و هیچی از نسخهٔ اندروید کم نداره!
✨
چی داره؟
🔌
اتصال قدرتمند:
▫️
۴ پروتکل: Smart (انتخاب خودکار) · MASQUE · WireGuard · WARP×2
▫️
۵ حالت اسکن: از Turbo تا Ironclad
▫️
اتصال مجدد خودکار تا ۵ بار + انتخاب هوشمند پروتکل اگه یکی جواب نداد
▫️
پشتیبانی IPv4، IPv6 یا هر دو باهم
▫️
نمایش زندهٔ سرعت، پینگ، سرور و IP با پرچم کشور
🏳️
🎨
رابط کاربری خیره کننده و زیبا :
▫️
کاملاً دوزبانه (فارسی و انگلیسی) با پشتیبانی کامل راست‌به‌چپ
▫️
تم تیره با طراحی دقیقاً مثل موبایل، بهینه برای مانیتورهای بزرگ
▫️
نوار عنوان به سبک ویندوز ۱۱
⚙️
تنظیمات پیشرفته:
▫️
نویز (از سبک تا تهاجمی و GFW) · MTU دلخواه · Fragment · ECH
▫️
تونل تفکیکی (Split Tunneling) — انتخاب کن کدوم برنامه‌ها از تونل رد بشن
📡
اشتراک با بقیه دستگاه‌ها:
▫️
SOCKS5 روی پورت 10810 و HTTP روی 10811
▫️
هر دو پورت خودکار پروتکل رو تشخیص می‌دن — هر کدومو هرجا بزنی کار می‌کنه!
🛠
عیب‌یابی حرفه‌ای:
▫️
تست زندهٔ اتصال + بررسی ۶ موردی محیط سیستم
▫️
کنسول لاگ زنده و رنگی با دکمهٔ کپی
🪟
مخصوص ویندوز:
▫️
تونل واقعی سطح سیستم با درایور رسمی و امضاشدهٔ مایکروسافت (Wintun)
▫️
پروکسی سیستمی خودکار تنظیم می‌شه و موقع قطع، برمی‌گرده سر جاش
▫️
نیازی به Visual C++ نداره؛ WebView2 هم نبود، خودش نصبش می‌کنه
📦
دانلود:
▫️
نصب‌کنندهٔ گرافیکی برای ویندوز ۶۴ و ۳۲ بیتی
▫️
نسخهٔ پرتابل بدون نصب — هیچ ردی روی سیستم نمی‌ذاره!
👌
▫️
فایل SHA256 برای راستی‌آزمایی سلامت فایل‌ها
⚡️
ساخته‌شده با Rust + Tauri 2 — یعنی حجم نصب فقط چند مگابایته، نه ۱۰۰ مگ مثل اپ‌های Electron! کل بیلد و انتشار هم صددرصد خودکار با GitHub Actions انجام می‌شه، بدون هیچ دخالت دستی.
📋
پیش‌نیاز: ویندوز ۱۰ (نسخهٔ ۱۸۰۹ به بالا) + دسترسی Administrator برای ساخت آداپتور شبکه
📄
لایسنس: MIT — کاملاً متن‌باز و رایگان
💙
⬇️
همین الان از بخش Releases گیت‌هاب دانلود کن و آزادی رو با یک کلیک تجربه کن!
📥
دانلود مستقیم از گیت هاب
https://github.com/QW-AI-Code/Aether_Desktop/releases/
سلام دوستان عزیز
✋
یه یادآوری مهم که حتماً بخونیدش
👇
برای اینکه اپ (چه نسخه اندروید چه ویندوز) براتون وصل شه، این چند تا نکته رو رعایت کنید تا بهترین نتیجه رو بگیرید:
⏳
رو هر پروتکل ۱ تا ۳ دقیقه صبر کنید تا وصل شه. بسته به اپراتور و منطقه‌تون این زمان فرق می‌کنه، عجله نکنید.
🔄
پروتکل‌ها و تنظیمات مختلف رو تست کنید. چرا؟ چون DPI هر سیم‌کارت با سیم‌کارت دیگه، هر منطقه با منطقه دیگه و هر شهر با شهر دیگه فرق داره.
📱
اگه با موبایل وصل نشدید: چند بار گوشی رو ببرید رو حالت هواپیما و برگردونید تا رنج آی‌پی‌تون عوض شه، بعد دوباره پروتکل‌های مختلف رو تست کنید. خلاصه باید قلق DPI اپراتور و منطقه خودتون دستتون بیاد
😉
📶
اگه با وای‌فای هستید: مودم رو ۱ تا ۲ دقیقه خاموش کنید تا رنج آی‌پی عوض شه، بعد دوباره با پروتکل‌ها و تنظیمات مختلف امتحان کنید.
❌
اگه بازم وصل نشد، یعنی این وی‌پی‌ان با نت شما جواب نمی‌ده و باید برید سراغ وی‌پی‌انی که با نت شما سازگاره.
⚠️
و نکته آخر: بعضی از کاربرا میگن این اپ مشکل داره و واسشون کار نمیکنه.
اگه مشکل از خود اپ بود، نباید برای هیچ‌کس کار می‌کرد! همونطور که می‌دونید برای خیلی‌ها داره کار می‌کنه و هر کسی تجربه متفاوتی داره.
پس اگه برای شما وصل نمی‌شه، مشکل از Aether نیست؛ مشکل از DPIایه که رو اپراتور شماست و جلوی کار کردن اپ رو می‌گیره.
#VPN
#فیلترشکن
#Aether
#ویندوز
#متن_باز</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/whitedns/1335" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1334">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8d366d7.mp4?token=iSZylc-vikaJP5SZOgD1xHnvhVAFcyVqT_8oZeOXAasuKLANDQDMaQn-mSqkUgKCvpvvr8wanIO5UmDjZRNR7978NPdWsZaYzWHD-j6Vg5Rita2tZDoHHmECpuSe2M1LUDgDQQZ2MIhMhdIdHSEc2PpL5jAsK4X25JV7DivfwlROhaCoc3SPqq7DSEEaWiZnb5JqiT17SkBzGFkROJcvUmRsznxm5ehrE9dd688l7Z7tp4Z5Y0xlZgj9BzELMDhxgX4ACam5oOKa8L6oRAU_xncKtwVkhuxSSGT4xh6jJwrR_0hf8Q_MijwXrAiPfnWtsuOYiGmNh5GYv3eMSl3qeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8d366d7.mp4?token=iSZylc-vikaJP5SZOgD1xHnvhVAFcyVqT_8oZeOXAasuKLANDQDMaQn-mSqkUgKCvpvvr8wanIO5UmDjZRNR7978NPdWsZaYzWHD-j6Vg5Rita2tZDoHHmECpuSe2M1LUDgDQQZ2MIhMhdIdHSEc2PpL5jAsK4X25JV7DivfwlROhaCoc3SPqq7DSEEaWiZnb5JqiT17SkBzGFkROJcvUmRsznxm5ehrE9dd688l7Z7tp4Z5Y0xlZgj9BzELMDhxgX4ACam5oOKa8L6oRAU_xncKtwVkhuxSSGT4xh6jJwrR_0hf8Q_MijwXrAiPfnWtsuOYiGmNh5GYv3eMSl3qeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">UAC SNI Spoofer Desktop
نسخه 1.0.6
━━━━━━━━━━━━━━━━━━
تغییرات جدید نسخه 1.0.6
• قابلیت Mobile Gateway اضافه شد. دستگاه‌های متصل به شبکه وای‌فای مشترک می‌توانند بدون تغییر تنظیمات Proxy، IP یا DHCP از VPN کامپیوتر استفاده کنند.
• امکان پینگ‌گرفتن از کانفیگ‌های موجود در تب Configs و مرتب‌سازی آن‌ها براساس کمترین پینگ یا کشور اضافه شد.
• باگ‌های جزئی بخش SNI Config Maker برطرف شدند. اکنون کانفیگ‌های بیشتری از مخازن شناسایی، دریافت و پردازش می‌شوند.
• مشکل فعال‌نشدن دستی کانفیگ‌ها، به‌خصوص هنگام استفاده از Auto Mode، برطرف شد.
━━━━━━━━━━━━━━━━━━
لینک دریافت نسخه 1.0.6:
https://github.com/Floxu1/UAC-SNI-Spoofer-Windows/releases/tag/1.0.6
لینک گیت‌هاب پروژه:
https://github.com/Floxu1/UAC-SNI-Spoofer-Windows
t.me/UacSniSpoofer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1334" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1333">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌎
نسخه جدید WhiteVPN 1.1.0 منتشر شد!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1333" target="_blank">📅 17:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1328">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1328" target="_blank">📅 17:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1327">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv4vXDeV2SWrKpOnas-rrEic7AwLOvRfNDBRTJ52xJtkW2nxz6Liy0BhJzrTWTngjx5_kWsMrzgH_IDRe97xs8utLjkWmhIWyTCyGxaA9dPzQJ0OenKfT59OxnpZpFI8s3BYmG2836gmLt5U7cWVWZs9BdVdbbnpGiPa8oXoarIqlaiFoOBOWk6eun3Z-vRChgEaxf05fq5NRE-Ojr2kG5R6TIoZ0Lbz1Otnwq5yMRMk1_xWeTJ0OpJC2EWE0GbMcwBhQlSQtsPhzoEGcR-l6uA1ig7h_KX6AEU49mZEltCZs_2O11e_ZDjp-1M7XzUN4yyv19MxdFyiP5piXzc3bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN 1.1.0 منتشر شد!
در این نسخه چند قابلیت کاربردی اضافه کردیم تا اتصال راحت‌تر، سریع‌تر و امن‌تر باشه:
🛡
اتصال همیشگی VPN
می‌تونید WhiteVPN رو طوری تنظیم کنید که همیشه فعال بمونه و در صورت قطع شدن، دوباره متصل بشه.
🔒
امکان Kill Switch
اگر VPN قطع بشه، اینترنت هم موقتاً متوقف می‌شه تا اطلاعات شما بدون محافظت منتقل نشه.
⚡️
قابلیت Real Delay Test
حالا می‌تونید تأخیر اتصال‌ها رو بررسی کنید، نتیجه‌ها رو ببینید و سریع‌ترین گزینه رو راحت‌تر انتخاب کنید.
✨
طراحی جدید صفحه اشتراک‌ها
صفحه اشتراک‌ها ساده‌تر، مرتب‌تر و خوش‌دست‌تر شده تا مدیریت و انتخاب اشتراک‌ها راحت‌تر باشه.
همین حالا WhiteVPN رو به نسخه 1.1.0 به‌روزرسانی کنید
🤍</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/whitedns/1327" target="_blank">📅 17:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1326">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VdY-zu49xU9qdfpC8c5BFoYYWdLv3cqh3-lPUiK5U8pgFVNO5GczLWJ0yOHKvnfb1Ju8lebYeycJGYQA9iuNMtMUmue4vL52NzJp5QuHNB0oFG_-F8ZyEoXtb5Jt41GIPBMNhcXU2jHz4aiJ9WcBVMircpLqGm9Q8cu-2c8ZIFjtdyIT8U3Vbb9h_Pys-x3BE9e6sYW6ClrFohB1em-DowpTTpzgBDA7lD5r_-pDjalX0V2PtvQeuh-j-1wZ89HTfYlgJv81V3yhG_LtviWr0e--_mf6cq-2JEHtvuzXu_qqK1xgc8oZPkKpdBkM4GESQgCUFxN8QfGTcnjrdsBv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1326" target="_blank">📅 10:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1325">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-poll">
<h4>📊 از چه دستگاهی استفاده میکنید ؟</h4>
<ul>
<li>✓ اندروید</li>
<li>✓ اپل</li>
<li>✓ مک</li>
<li>✓ ویندوز</li>
<li>✓ لینوکس</li>
</ul>
</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1325" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1324">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kTtQFyTb5v_9Y5UlUkjM30O3JlXA7rixOpYYihlZrHOj_s3m3E657OKnRyqI7k6btPGoYhy6b87dqcOnlKLWOS521EeryCqgFbDzjkOpCfLDcK9_ptHSqXEE1VVWOhiezzKsmBZ3PfFu6XrHdz38zIqEK687hYaY3vupQwCRtjpAXI8NQ_Axw5u9OXdXR5uNEecMnDh1Xtjz6_OMdJ2x9gEZQhwJMGbGNH8rsFOKrsdPb0Lf6HnAGQgz7A_VUglSrpXly_wX8YiyCK0fiOjg7TlApKCh8EHOVqixNeyVD32_yk3hDkxv1XudmZrUz-cecpOKiapLav84BE6nVdMPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1324" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1323">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دوستان عزیز، اونایی که Aether واسشون وصل نمیشه، یه زحمت کوچیک بکشید:
📱
✈️
چند بار گوشی رو بگذارید روی حالت هواپیما و بردارید تا رنج IP‌تون عوض بشه.
🔄
اونایی هم که با وای‌فای و مودم متصلن، مودم رو ۱ تا ۲ دقیقه خاموش‌روشن کنن تا آی‌پیشون تغییر کنه.
🔌
⏳
اینم یادتون نره که ما تو ایرانیم؛ سیستم DPI و محدودیت‌ها روی هر سیم‌کارت با اون یکی فرق داره، چه برسه به منطقه به منطقه و شهر به شهر!
🇮🇷
🚫
اینجا خبری از اینترنت استیبلِ خارج نیست.
📉
اگه این کارا رو کردید و پروتکل‌های مختلف رو هم تست زدید و باز هم وصل نشد، یعنی اون کانفیگ کلاً روی خط و منطقه شما جواب نمیده.
🛑
یکی دو ساعت بعد دوباره امتحان کنید یا برید سراغ VPN‌های دیگه که با اپراتور و منطقه‌تون سازگارترن.
🚀
🌐</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1323" target="_blank">📅 12:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1322">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-poll">
<h4>📊 با این لینک موفق شدید عضو بشید ؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-text">عضویت در گروه whitedns  در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1322" target="_blank">📅 12:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1321">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1321" target="_blank">📅 11:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1320">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/p8fQxaUrCQKoV5D3VJ54gW6j9dwIzLfOlKgDC8xEWWSvucjJ9NXnmoMhO-b0Yy49kJ3l1DxnGr_WA3VinQui27301Dxv93lyd6Rd6uMu5c170MHLPTPj3PFg-7KadB9PYfklZOQNios6fe2BnWq9Zqpmz6KoLFPXx_P3XGJI5lAMVXH5rDPiFidRHWmHP_dD1dtvVzd3APyKqwqNaRUFr14S61mOrCSKaU5mG6p0r0htGV9tJPel51BPigJ9gOan68YCyVw9g7Bjpchk4lr2W49d15ypXO7WRr2dBg9XVTT_9-ZKyPD_RKkRDg_yIGk4Iw69E6eSL8f9MbNaEO0EgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضویت
در گروه whitedns
در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1320" target="_blank">📅 11:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1317">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/whitedns/1317" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Aether 1.2.2</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/whitedns/1317" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1316">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سلام دوستان عزیز.
راستش ما قبل از اینکه بخواهیم نسخهٔ جدید ۱.۲.۲ پروژه اِتر (Aether) را منتشر کنیم، ۱ روز گذشته را کاملاً درگیر تست، آزمون و خطا و چالش‌های فنی بودیم. خیلی از کاربران از ما خواسته بودند که قابلیت انتخاب کشور را اضافه کنیم و خودمان هم خیلی دوست داشتیم این کار را بکنیم؛ اما بعد از کلی کلنجار رفتن و تست‌های مختلف روی اپراتورهای مختلف، متوجه شدیم که با توجه به ماهیت فنی این کار، عملاً چنین چیزی نشدنی است.
برای همین تصمیم گرفتیم خیلی روراست و خودمانی با شما صحبت کنیم و بگوییم توی این مسیر آزمون و خطا به چه چیزهایی رسیدیم:
### ۱. چرا در پروژه اِتر (Aether) نمی‌شود کشور خاصی را انتخاب کرد؟
پروژه اِتر (Aether) سرور شخصی و اختصاصی ندارد و کارش این است که شما را به شبکهٔ عظیم WARP کلاودفلر (همان شبکهٔ معروف
1.1.1.1
) وصل کند.
بزرگ‌ترین مانع ما در تست‌ها یک مسئلهٔ فنی بود: آدرس‌های کلاودفلر از نوع Anycast هستند. انی‌کست یعنی چه؟ یعنی یک آدرس مشخص، هم‌زمان در صدها دیتاسنتر در سراسر دنیا فعال است.
یک مثال ساده بزنم؛ شمارهٔ ۱۲۵ آتش‌نشانی را در نظر بگیرید. شما هر جای ایران که باشید این شماره را بگیرید، به آتش‌نشانی شهر خودتان وصل می‌شوید، نه تهران یا یک شهر دیگر! حتی اگر عمداً بخواهید به آتش‌نشانی شیراز زنگ بزنید، باز هم شمارهٔ ۱۲۵ شما را به نزدیک‌ترین ایستگاهِ خودتان وصل می‌کند.
آدرس‌های WARP هم دقیقاً همین‌طور کار می‌کنند. پروژه اِتر (Aether) به هر آدرسی که وصل شود، در نهایت این سیستمِ مسیریابیِ اینترنتِ اپراتور شماست که تصمیم می‌گیرد ترافیک به کدام دیتاسنتر برود.
*   وقتی اوضاع اینترنت خوب باشد، معمولاً نزدیک‌ترین نقطه جواب می‌دهد.
*   وقتی مسیرهای بین‌المللی شلوغ یا خراب باشد، سیستم شما را می‌فرستد سمت آلمان (فرانکفورت)، آذربایجان (باکو)، ایتالیا (میلان) یا هر جای دیگر.
توی بررسی‌هایی که قبل از انتشار نسخهٔ جدید داشتیم، دیدیم وقتی مثلاً لوکیشن روی «اتریش» تنظیم می‌شد، پرچم اتریش نشان داده می‌شد، اما خروجی واقعی اینترنت کاربر یک کشور دیگر بود! در واقع آن منوی کشورها فقط یک برچسب تزیینی و قشنگ بود، نه یک انتخاب واقعی. ما هم چون دوست نداشتیم توی پروژه اِتر (Aether) ظاهرنمایی کنیم یا آمار دروغین به کاربر نشان بدهیم، کلاً حذفش کردیم تا همه‌چیز واقعی و شفاف باشد.
---
### ۲. چرا ویژگی «اتصال فقط به لوکیشن‌های غیر از ایران» را اضافه نکردیم؟
شاید باورتان نشود ولی ما این قابلیت را واقعاً کدنویسی کردیم و قبل از نهایی کردن نسخهٔ جدید، آن را زیر تست بردیم. اما خروجی کار روی اینترنت ایران اصلاً خوب نبود!
منطق کار این بود: پروژه اِتر (Aether) وصل شود، آی‌پی خروجی را چک کند، اگر ایران بود قطع کند و برود سراغ آدرس بعدی. اما مشکل بزرگ کجا بود؟
وقتی اپراتور شما مسیرهای خارجی را محدود یا فیلتر می‌کند، تقریباً تمام آدرس‌های کلاودفلر به دیتاسنترهای داخل ایران هدایت می‌شوند. در این حالت، پروژه اِتر (Aether) یکی‌یکی آدرس‌ها را تست می‌کرد، چون خروجی‌شان ایران بود قطع می‌کرد، سراغ بعدی می‌رفت و در نهایت بعد از کلی معطلی می‌گفت: «اتصال ناموفق». یعنی عملاً به‌جای یک اینترنتِ وصل‌شده (ولو با آی‌پی ایران)، شما کلاً قطع می‌شدید! درست مثل کسی که چون فقط سوار تاکسی سفید می‌شود، تا صبح گوشهٔ خیابان در سرما می‌ماند!
تازه یک مشکل دیگر هم هست؛ سرویس‌های تشخیص لوکیشنِ آی‌پی همیشه دقیق نیستند. خیلی وقت‌ها یک اتصال کاملاً سالم و خارجی را به اشتباه «ایران» تشخیص می‌دادند و پروژه بی‌دلیل آن را قطع می‌کرد. به همین خاطر در آزمون و خطاهای قبل از انتشار متوجه شدیم وجود این گزینه فقط باعث خرابی اتصال و اعصاب‌خردکنی کاربران می‌شود.
---
### ۳. پس الان پروژه اِتر (Aether) دقیقاً چه‌کار می‌کند؟
ما در این نسخه همه‌چیز را هوشمند کردیم. حالا هستهٔ پروژه اِتر (Aether) در چند ثانیه کل رنج‌های WARP را اسکن و پینگ می‌کند و به بهترین، سریع‌ترین و پایدارترین نقطه‌ای که در آن لحظه روی خط شما جواب بدهد وصل می‌شود؛ بدون قطع و وصلی‌های الکی.
البته اگر کاربر حرفه‌ای هستید و دوست دارید خودتان دستی همه‌چیز را تنظیم کنید، هنوز هم می‌توانید از بخش تنظیمات، اندپوینت دستی یا رنج آی‌پی دلخواه خودتان را وارد کنید.
یک نکتهٔ بسیار مهم برای آرامش خیال شما:
خیلی از کاربرها نگران هستند که اگر آی‌پی خروجی ایران باشد، امنیتشان به خطر می‌افتد. اصلاً این‌طور نیست! حتی وقتی نقطهٔ اتصال شما داخل ایران باشد، تمام ترافیک و داده‌های شما کاملاً رمزنگاری‌شده است. مقصد نهایی این ترافیک، شبکهٔ جهانی کلاودفلر است و هیچ‌کس در این مسیر نمی‌تواند اطلاعات شما را بخواند یا ببیند چه کار می‌کنید.
آن نقطهٔ ایران، فقط و فقط مثل یک «درِ ورودیِ» امن به اتوبانِ کلاودفلر است، نه جایی که اطلاعات شما در آن تخلیه شود. پس اصلاً نگران امنیت خود نباشید.
---
###
💡
حالا چطور آی‌پی خود را به خارج از ایران تغییر دهیم؟ (دو راهکار عملی)
اگر به هر دلیلی نیاز دارید که آی‌پی خروجی شما حتماً روی کشوری غیر از ایران قرار بگیرد، در حال حاضر دو تا راهکار کاملاً واقعی و تست‌شده برایتان داریم که می‌توانید از آن‌ها استفاده کنید:
*   راهکار اول (سوئیچ بین پروتکل‌ها): تنها راه طبیعی برای تغییر آی‌پی این است که داخل تنظیمات پروژه اِتر (Aether)، بین پروتکل‌های مختلف سوئیچ کنید. در این میان، پروتکل وارپ (WARP) بیشترین احتمال را دارد که شما را به یک سرور غیر از ایران متصل کند. این تغییر پروتکل باعث می‌شود روتینگ اینترنت شما عوض شده و در نهایت به یک دیتاسنتر خارجی هدایت شوید.
*   راهکار دوم (ترکیب با سایفون): شما می‌توانید از قابلیت «حالت پروکسی» (Proxy Mode) در پروژه اِتر (Aether) استفاده کنید و آن را با برنامه سایفون (Psiphon) زنجیره یا ترکیب کنید. با این روش، ترافیک شما از تونل پروژه اِتر (Aether) رد شده و در نهایت با آی‌پی خارجی سایفون خارج می‌شود که تضمین می‌کند آی‌پی شما به غیر از ایران تغییر خواهد کرد.
@whitedns</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/whitedns/1316" target="_blank">📅 10:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1315">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hGXS05I0SpkN7ElLxuV1dvlmuMBt7stW0usG4aJhNW3l9yyX-inf78Nu5v05jx3XAbB2g1bJgCPXa9vKoFlxcGgUPyLy6kQN4G_ZvY-AjYuynLfbZC2tgSIrZVjdMCK3FmoPrdKdxdszUz6NAQnmeEo8aqezV7oJmLPdBSQ5730CtOsg8ucayT5aiXAqDg8q6RlROrysLFvnEr-6Ys-F_i5jZnMuGD406oeF7DxtRHNyApxkn-Z5QfYiG4YwlUzkdqjh3DBPRoR5a418ZxeOZqTdm3uZy65Fa2H0g_etn6va7Ybf-uWimxg2duvcGlFcw8EP1kRBheQ_ehA-gGA_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
تازه‌های نسخهٔ ۱.۲.۲ کلاینت موبایل Aether
🚀
یک به‌روزرسانی بزرگ و بنیادین با تمرکز بر امنیت حداکثری، کاهش شدید مصرف منابع سخت‌افزاری و ثبات اتصال منتشر شد! در ادامه خلاصه تغییرات این نسخه را برای شما آماده کرده‌ایم:
🔄
۱. مدیریت خودکار و ارتقای هسته (Core)
ارتقا به نسخه پایدار ۱.۴: هسته تانل داخلی برنامه به آخرین نسخه پایدار ارتقا یافت.
خودکارسازی در CI/CD: فرآیند همگام‌سازی و اعمال پچ‌های اختصاصی اسکن رنج به صورت کاملاً خودکار و هوشمند در خط‌لوله بیلد گیت‌هاب پیاده‌سازی شد تا از بروز کوچک‌ترین ناسازگاری یا خرابی در فایل‌های نهایی جلوگیری شود.
🗑
۲. حذف کامل سیستم به‌روزرسانی درون‌برنامه‌ای (ارتقای امنیت)
افزایش شفافیت و امنیت: بخش دانلود خودکار درون‌برنامه‌ای به همراه دسترسی‌های پرخطری مانند REQUEST_INSTALL_PACKAGES کاملاً حذف شد.
دلیل فنی: برای اطمینان از اصالت کدها و عدم نصب ناخواسته فایل از منابع ناشناس، از این پس تمامی آپدیت‌ها صرفاً به صورت رسمی و امضاشده فقط از صفحه ریلیس گیت‌هاب پروژه قابل دریافت خواهند بود.
🌐
۳. حذف لوکیشن‌های فیک و واگذاری اتصال به هسته هوشمند
حذف منوی انتخاب کشور: از آنجا که شبکه WARP کلاودفلر از آدرس‌های Anycast استفاده می‌کند، انتخاب لوکیشن در کلاینت عملاً تزئینی بود.
اتصال هوشمند واقعی: در این نسخه منوی لوکیشن حذف شده و وظیفه اسکن رنج‌ها و انتخاب بهترین و نزدیک‌ترین لبه ارتباطی (با کمترین پینگ و پایدارترین حالت) به صورت پویا به خود هسته برنامه واگذار شده است.
⚡️
۴. کاهش مصرف رم، پردازنده و بهینه‌سازی رابط کاربری (UI)
کاهش مصرف CPU در حالت آماده‌باش (Idle): تغییر ساختار مانیتورینگ اتصال از حالت Polling به حالت Blocking روی پروسه هسته که باعث می‌شود پردازنده گوشی در زمان اتصال بدون ترافیک، به خواب عمیق برود.
حل نشت حافظه (Memory Leak): محدود شدن حجم لاگ‌های ارتباطی به یک بافر حلقوی ۸۰۰ خطی (حداکثر ۵۱۲ کیلوبایت) جهت جلوگیری از مصرف بی‌رویه رم در اتصال‌های طولانی.
رابط کاربری روان‌تر و سریع‌تر: حذف انیمیشن سنگین شفق قطبی (Aurora) در پس‌زمینه و جایگزینی با رنگ ساده ساکن که بار پردازش گرافیکی گوشی را به صفر می‌رساند. همچنین منوی تنظیمات پیشرفته اکنون بدون کوچک‌ترین لگی فوراً باز می‌شود.
🔌
۵. رفع تداخل با v2rayNG و حل مشکل نصب (Over-Install)
تغییر پورت‌های پیش‌فرض: پورت‌های اشتراک‌گذاری شبکه محلی Aether به 10810/10811 تغییر یافت تا با پورت‌های پیش‌فرض v2rayNG تداخل نداشته باشند. همچنین سیستم شناسایی هوشمند ابزارهای موازی اضافه شده است.
حل دائمی مشکل امضای دیجیتال: گواهی امضای اندروید در بخش بیلد تثبیت شد؛ کاربران نسخه ۱.۲.۱ می‌توانند بدون نیاز به حذف برنامه قبلی، نسخه جدید ۱.۲.۲ را مستقیماً روی گوشی خود نصب کنند و تمام تنظیماتشان حفظ خواهد شد.
🔒
۶. ممیزی امنیتی ۱۰۰ درصدی خط‌به‌خط
کد منبع برنامه تحت ممیزی سخت‌گیرانه قرار گرفت و از نظر مواردی همچون اطلاعات هاردکدشده، نشت DNS/IPv6، ذخیره‌سازی محلی ناامن و ترافیک رمزنگاری‌نشده کاملاً پاک‌سازی شد.
📥
هم‌اکنون نسخه ۱.۲.۲ را به صورت رسمی و امضاشده دانلود کنید:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/whitedns/1315" target="_blank">📅 10:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1314">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-railway.txt</div>
  <div class="tg-doc-extra">168 B</div>
</div>
<a href="https://t.me/whitedns/1314" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک‌های استفاده شده در ویدئوی بالا</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/whitedns/1314" target="_blank">📅 04:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SduE9RBgOUoIUyTcrulDYIbn4sjNRD_2FAcNnM_gu21qDc7OnS3BFgSyfvA25fVYBL-CZsRQ-Hxj1rELV-waiuBZZKSFrQKSFdIaoo5A966i1mrFH_zqHkLuIvbHgOsL5n_488BrRX1ohza-f3uqQn7ObRs-dj0xcoe5Uv5gGpRY3qIRK3v-igPWyfW3wtb0Ri0fJ1d89NV4atY81BLE4SasFrJ0xR4CBU0g-Ata9mZ9U-vBqScgeAA9RQYdOEXWI4z2ZR5e7hCaG6GgzScJOIxQBYNSBbQ4hNliH1Gtwxrg1nNo2J5y1gdszTqakV2pyYUaGX0ySSxMLl4iDWEZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
هرمس رو با گوشی موبایل روی VPS رایگان و تلگرام اجرا کن! + آموزش بکاپ کامل از Hermes
⚡️
دستورات نصب استفاده شده در این ویدئو:
https://t.me/MatinSenPaii/4683
⭐️
توی این ویدئو:
1- بهتون یاد میدم چه شکلی با گوشی آیفون/اندروید/لپ‌تاپ، هم Hermes و هم 9Router رو به رایگان روی سرورهای Railway بالا بیارید.
2- وصلش می‌کنیم به تلگرام و از مدل Mimo رایگان روی OpenCode استفاده می‌کنیم و API 9Router رو ست می‌کنیم.
3- به طور کامل بهتون یاد میدم که چه شکلی می‌تونید از اکانت گیتهابتون استفاده کنید تا Hermes رو بهش وصل کنید و به راحتی، هر چند ساعت یک بار از تمام داده‌هاش برای شما بکاپ بگیره.
4- به علاوه روش ایرانیزه شده‌ی استفاده نامحدود از کردیت رایگان 5 دلاری Railway
😂
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api و سرور رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/whitedns/1313" target="_blank">📅 04:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1312">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سرور های اهدایی و فعال WhiteDNS پارت ۲ داشته باشید برای زمان قطعی (کلیک کنید روش کپی میشه)
Server #11 thx to Araskhatare
♥️
Location: Germany
🇩🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6nwn4eqIDIgICB0aHggdG8gQXJhc2toYXRhcmUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiZGUuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI0OWUzNDlhNDc2NjQyYTg4ZTQ2NDVmYTJiZjgwZjhjIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #12 thx to Araskhatare
♥️
Location: Israel
🇮🇱
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh67wn4exICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI2MmIyNjQ0NzU5MjU4OWE0NmQ1MzdlY2M5NDc3MzY2NiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
آموزش استفاده از برنامه اندروید
👇
https://www.youtube.com/watch?v=tz8cj7HzHVI
آموزش استفاده از برنامه ios
👇
https://www.youtube.com/watch?v=filwdiPKN90
آموزش استفاده از برنامه ویندوز
👇
https://youtu.be/Mc--GlKw2wg
@whitedns</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1312" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1311">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">10 سرور اهدایی و فعال WhiteDNS داشته باشید برای زمان قطعی (کلیک کنید روش کپی میشه)
Server #1 thx to Coreforge
♥️
Location: Turkey
🇹🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7nwn4e3ICAgdGh4IHRvIENvcmVmb3JnZSIsInNlcnZlciI6eyJkb21haW4iOiJ2LmFub255bW91cy5vYnNlcnZlciIsImVuY3J5cHRpb25fa2V5IjoiYjI3NTAzOTE5OWIxYzhjOSIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #2 thx to Araskhatare
♥️
Location: Germany
🇩🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6nwn4eqICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXJhc2toYXRhcmUxLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI5ZGIxNjYwMmM4Yzc3NjcxOWJhZDE3ZWZjOWQxM2E0NCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #3 thx to Araskhatare
♥️
Location: USA
🇺🇸
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7rwn4e4ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6ImVkMGNlZjE2YjcxNTNiOGQ4MzVhMzI3ODYxNTk3YzY0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #4 thx to Araskhatare
♥️
Location: France
🇫🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6vwn4e3ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImIuYXJhc2toYXRhcmUxLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiIyZjAyZTNiN2NiNTg3ZjM4M2U0MWM0MmU4ZWYzYWY2MSIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #5 thx to Araskhatare
♥️
Location: UK
🇬🇧
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6zwn4enICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYXJhc2toYXRhcmUxLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiJkYmYwMmYyYWVmZmQzM2QyNDY0M2ViODM4OGY2N2Y0ZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #6 thx to Araskhatare
♥️
Location: Ireland
🇮🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh67wn4eqICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjY0MTVlYjhmOTBmMWQ0NjY1N2JjZTljYjc5MTg2NDY2IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #7 thx to Araskhatare
♥️
Location: Sweden
🇸🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7jwn4eqICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InEuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjFkYjFiMWIyNGM2N2IxNzYwOTAzMmNjNDdhZmRhMzZlIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #8 thx to Araskhatare
♥️
Location: Spain
🇪🇸
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6rwn4e4ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Im4uYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjU4MTcyOTA4ZGFhNTAxZTk0MjUzNWU2NTY3NzkwM2ZkIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #9 thx to Araskhatare
♥️
Location: Italy
🇮🇹
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh67wn4e5ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imx5LmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiJkMzM4NmM1MzkxZmRmOTJjMmNkODM3YmFkZTBhNGVjYyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #10 thx to Araskhatare
♥️
Location: Brazil
🇧🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6fwn4e3ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlsLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiJmNzk4MDAyYzlkMTkxMTg4M2MzOTE2YTQ4ZTkzNTVkMiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
آموزش استفاده از برنامه اندروید
👇
https://www.youtube.com/watch?v=tz8cj7HzHVI
آموزش استفاده از برنامه ios
👇
https://www.youtube.com/watch?v=filwdiPKN90
آموزش استفاده از برنامه ویندوز
👇
https://youtu.be/Mc--GlKw2wg
@whitedns</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1311" target="_blank">📅 22:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162866f874.mp4?token=kFs7wVIJR9l9Ru9f8kJZmfdi8NDuCnxZJgutGBsD9efLA1fRfOUKkeUWLd06VBEIaAcGG0W_Pg9fC7AiDlr7J_U6TVsEW_Qpuav2PrE7nABETRHKx4iUPh46hm0VfJv-9RrGLjF8AajMfUW5dz3oQmBVsP00R-b8XK5ZZkVBEDnd6jEjXOud7DBta2DBDxF2n_Xc_mtxXnO-3iLASiLE3Hhq15CHuml7IazcPG8qfGKe7W0fuUheia96f5Mx3n5fdEYlOiXB0k869BcenhXgFO6aUUkC8FVxecExq4MAgz4WsKCeKk8UUblogMDnEacWWCMkZzgKwjHX-gWykfZXYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162866f874.mp4?token=kFs7wVIJR9l9Ru9f8kJZmfdi8NDuCnxZJgutGBsD9efLA1fRfOUKkeUWLd06VBEIaAcGG0W_Pg9fC7AiDlr7J_U6TVsEW_Qpuav2PrE7nABETRHKx4iUPh46hm0VfJv-9RrGLjF8AajMfUW5dz3oQmBVsP00R-b8XK5ZZkVBEDnd6jEjXOud7DBta2DBDxF2n_Xc_mtxXnO-3iLASiLE3Hhq15CHuml7IazcPG8qfGKe7W0fuUheia96f5Mx3n5fdEYlOiXB0k869BcenhXgFO6aUUkC8FVxecExq4MAgz4WsKCeKk8UUblogMDnEacWWCMkZzgKwjHX-gWykfZXYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
آموزش وصل شدن به این روش شیر و خورشید در Mahsang دوستانی که بلد نیستند.
1-اول به داخل mahsang برید
2-سه خط سمت چپ رو بزنید
3-قسمت تنظیمات سایفون رو پیدا کنید
4-پروتوکل روی cdn fronting قرار بدید(دکمه ذخیره یا سیو رو بزنید حتما)
5-برگرید صفحه اصلی گزینه F رو بزنید
6-حالت فقط سایفون/only pisphon رو بزنید و دکمه کانکت و تمام
حالا شما رایگان و با سرعت بدون نیاز به پیدا کردن ip به اینترنت آزاد متصل میشید
🔛
لینک دانلود نسخه جدید
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1307" target="_blank">📅 07:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1304">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xr6mjHg7s4OZs4U0X_2FaVwsD-ihZPFIf7YpywHg335MxkvB0GRK20_VHtQVyteJaDgQn7C8MsXrKrcWv6NfIVs1Wng3VKSm0kFt6V_5yUGHirkKJKY25iDVSTnpb29TvbkbonMYa1tHwH_ArPQ_cxiUnlzfAWkGqkUCm2wv9CWKSs7qh-KWwj40DHaFiNL6dCem8qpR0xACpXqzaag0t9udEumZ066fGVtGX7rBijKHKOBJEiCMfwFEYFU2olt4ws51n_infWfYO9lhq02xitYyxjLN12uLzOubfOkOdHm4aBDwvUu0ns2cfSnBmmRYS2o9UZCmWzOAmXExr1NCQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!
هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده.
منم یه مشارکت کوچولویی روی خود هسته داشتم.
تغییرات اصلی این آپدیت:
1-
امنیت در پروتکل MASQUE:
قبلاً وقتی وصل می‌شدید، کلاینت هیچ تاییدیه‌ای از سرور نمی‌گرفت و اگر کسی وسط راه سعی می‌کرد با یه سرتیفیکیت فیک گولتون بزنه، برنامه متوجه نمی‌شد. اما الان اتصالات MASQUE سرتیفیکیت سرورهای کلادفلر رو به صورت دقیق (از طریق هش‌های SPKI) بررسی می‌کنن تا دیگه کسی نتونه ترافیک رو شنود کنه.
2-
پایداری WireGuard و Gool:
قبلاً بعضی وقتا برنامه بهتون می‌گفت متصل شدید، در حالی که دیتا اصلاً ردوبدل نمی‌شد و فقط روی یه پروکسی SOCKS5 گیر کرده بود. اما الان یه سیستم بررسی سلامت (Health Check) مداوم داره که اگر دیتایی از سمت سرور برنگرده، خودش به صورت اتوماتیک اتصال رو قطع و دوباره وصل می‌کنه.
3-
اتصال مجدد خودکار در Gool:
تو نسخه‌های قبل اگه تونل بیرونی Gool قطع می‌شد، کل فرآیند کِرَش می‌کرد و خارج می‌شد. الان Gool هم مثل بقیه پروتکل‌ها خودش هوشمندانه دوباره ریکانکت می‌کنه.
4-
فیکس شدن نشت مموری (Memory Leak):
یه باگ رو اعصاب بود که وقتی اتصالتون زیاد قطع و وصل می‌شد، تسک‌های قدیمی تو بک‌گراند باز می‌موندن و آروم‌آروم رمِ سیستم پر می‌شد. این مشکل تو تمام پروتکل‌ها کامل برطرف شد.
5-
هوشمندی در مصرف منابع:
از این به بعد Aether همون اول کار، تعداد هسته‌های CPU و مقدار رم سیستمتون رو می‌خونه و میزان اسکن همزمان (Concurrency)، بافرهای شبکه و صف‌های داخلیش رو بر همون اساس تنظیم می‌کنه. این قابلیت برای کسایی که می‌خوان ابزار رو روی روترها و بردهای ضعیف‌تر بالا بیارن فوق‌العاده‌ست.
لینک گیت‌هاب برای دانلود(نسخه‌های مک، لینوکس و ویندوز):
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.6.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/whitedns/1304" target="_blank">📅 05:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1299">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📱
آموزش کامل اپلیکیشن WhiteDNS منتشر شد
سلام به همه دوستان عزیز
یک ویدیوی آموزشی کامل برای استفاده از اپلیکیشن WhiteDNS آماده کرده‌ایم. در این ویدیو، تمام مراحل از نصب و راه‌اندازی اولیه تا اتصال و استفاده صحیح از برنامه، قدم‌به‌قدم توضیح داده شده است.
در این آموزش با موارد زیر آشنا می‌شوید:
• نصب و راه‌اندازی اولیه WhiteDNS
• اضافه‌کردن و مدیریت Resolverها
• اسکن و پیدا کردن Resolverهای معتبر
• تفاوت حالت پروکسی با VPN کامل
• نحوه اتصال از طریق DNS Tunnel
• مشاهده وضعیت اتصال و میزان مصرف ترافیک
• مدیریت پروفایل‌ها و تنظیمات برنامه
• نکات مهم برای داشتن اتصال پایدارتر
https://www.youtube.com/watch?v=tz8cj7HzHVI</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/whitedns/1299" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1298">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Mz96p07K6JBVAVEH1aTBEiqnnpZ9ufKmagVEX-I0HszsqLLpUGXegxHzu2hz_PUlmqiSCF25rxoNezMD1xSEWRPBrejWviJD8_O1gTFNAlPHNm0FVmn4Wj2fHFWOeBPi-EzuJyJ0MJPRM0YqC3k8vRj3fX_Y2YlYf8u3dYDg82sgF4zNmZ_gWePbRLkIf8foa-JNPU0aSDaVeHgCfvRCFf4cUEahWQoDL9RS7qphP5w9N8LKoop0-J5DZZwOzzqDhaosGlGI3VDDX3XiAUUVJSPOKb_-Q5JfdkHUOs0jQUGW-SAk_hKZwdU4sJyUOt0F4-VUu5wB9YJ4dpX3c7JTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1298" target="_blank">📅 18:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1297">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OYg0BwqCmDTN1B1i4SOVwIHz7G559cHkK4yv5-GtByKUiQ1oLgXychvNxIA5K_4L1Qx3oS7H4nnCDFcWsuawwZEsSr5w98ZeFix6P2HGAYUYpNLaAQz1BtzyiERWnB6lr8gjbtKLBtlgzOCnCe55rMjcXuayQ4_Kv1PbmDVNgtUWsDJlziY9YO1_Og49lVd1knsCn99oeMqUM_sFOrXukVUhVDd91Mlgqoa84vTlbzBWeeNX0rCYCGMkRr53r1zSKJph-bUjg229A5v3E6Q8XRZiHSYKl95qjZlFfq7pm5GNTzvf6pYLIthHoW0p-eDdrsl-VnfYYuFhcG1LH9LyaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1297" target="_blank">📅 18:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1294">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/whitedns/1294" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخهٔ جدید Aether منتشر شد! (v1.2.1)
نسخه قبلی رو حذف کنید بعد نسخه جدید نصب کنید
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/1294" target="_blank">📅 16:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1293">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cxOXrF54NT3RTYvt-JkC_dPE0oI7UNqr5OQK-GNuBLO4cGy-wyARVZBwuTALR5-ORXPkIAiIcSAVKymtcsYgY6LRS7r4hLA8wRWZIIT4BTvTukmAdgQarObFe1DeGn-1_ZndeYM253Fzm7XrGUMnNjfhegdvrHumowwaYM3-0ysyr11xD9arppFtWG0rQpBnKkLHAdcBuqUQ-9waXO8O_WmCDUIDM8haCUf91zGJEbupHabT7Uup2iUV1KGZBmX4j9zFrJp956sGTXoRHwzOtY6kkzvlX3NQHUe6JoRYCCH1aMurqw1ztMhVQQRB5DfNX0b0qvmoRC3Y1YyEFo-gMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخهٔ جدید Aether منتشر شد! (v1.2.1)
🎉
اگر به دنبال یک اتصال واقعاً پایدار، فوق‌العاده سریع و بدون نیاز به برنامه‌های جانبی (مثل v2rayNG) هستید، نسخهٔ جدید اِتِر موبایل با قابلیت‌های شگفت‌انگیز برای عبور از سخت‌ترین فیلترینگ‌ها آماده شده است!
🔥
تازه‌های بی‌نظیر در نسخهٔ ۱.۲.۱:
⚡️
موتور هوشمند واقعی (Smart Auto):
برنامه مانند یک مهندس شبکهٔ حرفه‌ای، ابتدا DPI شبکه و وضعیت اختلال‌ها (مانند فیلترینگ SNI یا خفه‌کردن UDP) را تحلیل می‌کند و سپس بهترین چیدمانِ اولویت‌بندی شده از پروتکل‌ها، سطح مبهم‌سازی (Noize)، فرگمنت و رنج‌های آی‌پی را برای اتصال گام‌به‌گام و کاملاً پایدار اعمال می‌کند.
🟢
«متصل» یعنی اتصال واقعی!
دیگر خبری از کلمهٔ «متصل» فیک که هیچ سایتی را باز نمی‌کند نیست! برنامه تا زمان دریافت هر ۴ تیک سبز سلامت (پورت، هندشیک، اینترنت و آی‌پی) در وضعیت بررسی می‌ماند تا از اینترنت واقعی مطمئن شود.
🛰
نمایش آنی آی‌پی و پرچم:
با موازی‌سازی سرویس‌های تست سلامت و تشخیص IP، این فرآیند با سرعت بسیار بیشتری انجام شده و بلافاصله وضعیت موقعیت جدید شما نمایش داده می‌شود.
🔄
آپدیت آسان و مستقیم (مشابه تلگرام - آزمایشی):
از این پس برای دریافت آپدیت‌ها نیازی به سر زدن به گیت‌هاب ندارید؛ نسخهٔ جدید مستقیماً درون برنامه به شما اطلاع داده شده و با یک کلیک دانلود و نصب می‌شود.
🛠
رفع ریشه‌ای تداخل‌های متنی زبان فارسی:
به‌هم‌ریختگی ظاهری و راست‌به‌چپ اعداد در فیلدهای حساسی مانند ip:port و اندپوینت‌های دستی کاملاً برطرف شده است.
🔒
امنیت بسیار سخت‌گیرانه‌تر:
تأیید نام هاست در اتصال‌های TLS (بستن راه حملات MitM)، حذف لاگ‌های موتور در نسخهٔ نهایی و مسدودسازی ترافیک ناامن HTTP برای محافظت حداکثری از اطلاعات شما.
🧹
دکمهٔ بازنشانی سریع تنظیمات:
با تنها یک لمس، تمام تنظیمات پیشرفته را به مقادیر پیش‌فرض بازگردانید.
لینک ریپو :
🔥
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1293" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1291">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqwaISm-ezIqp4_OFN9eMV-hIKTpBWGZzO4APM9CS7FP3WMGU7Cbl2Vy0-NbCxgK-IC2f9d5ppdXkVdt1VZndGsVwVWIsCtW6vYFAWGzQv1phz2ufIu-s-oBkQ_Souuq8sm2h_rSjrGSOheKLmAmQfRXW4-0C1KVOog1m98mIQD59mWxxspUq9kzDbMWSrIKmN1rqQGidytZzGgiN9Y4aJAirHwMo7lv84yHGgtpMRHG9JCB8vr4MAC5QA-Fy1q3b-HRzYk3N-ZXVkH4xjnaVpryOAcL6exLD7i_j0PFBZgPeG0hd22Ed7dk2ugG0dWybdSV_Kaci2ohuZLOSocmFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/whitedns/1291" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنوا | Nova</strong></div>
<div class="tg-text">🤖
ساخت پنل نوا پروکسی فقط با ربات تلگرام!
دیگه لازم نیست مراحل نصب رو دستی انجام بدین.
😎
فقط وارد ربات نوا پروکسی بشین، اکانت Cloudflare بسازین، توکن رو دریافت کنین و چند ثانیه بعد پنل اختصاصی خودتون آماده‌ست.
🚀
بعد از ورود به پنل هم فقط کافیه رمز ادمین رو تنظیم کنین، کانفیگ رو داخل کلاینت Import کنین و از اینترنت آزاد استفاده کنین.
📺
آموزش کامل مراحل داخل ویدیو گفته شده.
💬
اگر سوالی داشتین، داخل کامنت‌ها بپرسین.
🔹
ربات تلگرام:
@IRNovaProxy_Bot
🔹
وب‌سایت:
https://novaproxy.online</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1289" target="_blank">📅 09:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1288">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard  https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1288" target="_blank">📅 04:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1287">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1287" target="_blank">📅 04:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1285">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8dnum1jZodaCTvSa7edzGYYurUAok9So7hkjWR6x0Nk5AIgQDo5VzXOiZkdrt2VBEgWOshq776Ist4Yh6MBOLq_7TRiMd61XkMOiKNc7XgwvhP6zjGFUIKy6lTyty51fF9zsXL9P1MyHvp1wNriAFhk3wZi4RWsYVFFbNa3yUz1mA2_0TVNALSgxTkLJcqkfxOTAkd5IC2nPA1Zj1pUoOfQ3SCBiskb961Zkrt4bUK3HG0XBz809szqsn8i1P28dWt1NMT2upSfoZx6RPQ4t239PXZmM4oEVaB49WreMlaD__DbQurAVmIelcK9MPag_znxyVffDSyjUeP2JV905A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/whitedns/1285" target="_blank">📅 15:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1283">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک ظرفیت جدید برای تست فلایت داریم که میتونید از لینک زیر استفاده کنید
🚀
📱
اپ  CoreForge  یک فیلترشکن ساده و قدرتمند برای iOS / آیفون که مخصوص استفاده در شرایط سخت، اختلال شدید اینترنت، اینترنت ملی و حتی دوران قطعی کامل طراحی شده.
https://testflight.apple.com/join/3htm1Whc
آموزش
🎥
📹
:
https://www.youtube.com/watch?v=filwdiPKN90
@whitedns
📢
🔗</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1283" target="_blank">📅 12:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1282">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jKRni-1tP3l_1POqf3GUMLx75_GtEmy2RallmEvj_tTlgbVm4FrYW0T0BQx7pTBBIheD3PJ8FfslVCJAoDLdDdhZKm_5GZFm62CCixcBQtTt84Bll_J-l5dMjvXsQfEsz47OthAN-1MG2EhVlIBXVbl6_x6MuJK65QyjAAIVvY08aas1ihnaeIMDJzTolt_SlLShaOVFaTzuGQ-WJluyVC2XZrBZKuh5X4jLPFa9HQTSomhwbcwcTX-tImWsA7-v7VDub-RYg-zwFiJk85qcwdlD_UICjEmjjih-bs3kA1Fe-hJlF07-yrxHG6u6jM6-pWfJLMTJG4NJ6X7eyhwpjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1282" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1281">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/JtbbW2vDTgyy9SmGxvntCiF0W32NMIQBGb22uoJvYOQzNQcCPOIiKkZgQ2MaERQw-kon_wxXrr4dMS760F8Q7Re2VoZ5jOH8gm9ohSNdzb0PCDW9bYXzrb02g1mle62wQULPQrnKGgVYF5MfJmgWSaKJYEdrWwaR3Q6Edzjk8nzU04gSMN3DpB7M6kh5bKRQMNcgbm6h2xn7l78ssa-TDLBuMe0PU3voCshOO6E1G351rL7Y2fOf1ngi5rRs2ltHSWysg9bsjwgAUdabN489On0VXTVkTiEKMJt7_v5m4aYjcDj6IXfrUyPYpjqpEOug-rgzR6ZYeSpMfPGqz4HalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در whitedns android</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/whitedns/1281" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1280">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Dv1D66voFueP6clwqLh19nVvcAEC0vdwsbeE5PKn8yHt8mGDKuDeJv7eDKP1gTXsdpXvthwzcEf0AVIjMBb6Ughs_cH_zU8vZz32jgVTnK9xHu5-cCAD_LxjKPDAvXhlCvGJUBTcNVT0rIvlOzdkNIQkVK-5Ttn_9tANu7qG51bR8s1LIzeBuF_xq3kOXoTIkrIY3wwg59iWMax2iKWD9-UZUvY5LW-7R5RLGY2XFbyprwqByOVntNvLoO6NQ0tFe1y0z3vc2y5D_rSTVQ4I8Gfic96pSr2Nl78iMJvVEe9GHZRvJVjUDuH8UY6UMHVFiGY-nGweOZ8saH1OJTMl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در Whitedns windows</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/whitedns/1280" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1278">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Android.zip</div>
  <div class="tg-doc-extra">2.5 KB</div>
</div>
<a href="https://t.me/whitedns/1278" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1278" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1277">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PyWU5Z4s0jgeSU4UUVAECuo-XqZ3mUpjgD-ntskYvrDhrrXM45ctYfNZ7Wm3nmRbRRQ2weSbD9qozIOQ67NqkIr2shM-49RQjDOBCzfqMWgmf6F6NVU4u-ja-ox8JCLMcLaP9NntyRukTa_3SUqp18J7MiR4P3YV5b_C-mdisMgp0kQ0xp1uNHlj-FzRdFBpBUbw5Dyi9M8yNmoIxO6y1R-dkKsnjIXzqWoE4K7p-0A1GBjpxAV_G6EDwc5CK8Xn8k53eitufjw_8lEFJy9d4UubKzkPMoqDvwL4wbQlyL6CiRsV0Tg9qoFi4QtxnqeY3lxfYCxrhgUtSS4hilUhwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
افزایش سرعت اتصال WhiteDNS
تنظیمات اختصاصی whitedns
یکی از مشکلاتی که بسیاری از کاربران با اون مواجه هستن، اتصال موفق
WhiteDNS
با سرعت پایین یا ناپایداره.
✅
یکی از مؤثرترین راه‌ها برای افزایش سرعت و پایداری اتصال، استفاده از تنظیمات بهینه میباشد (البته استفاده از سرور و کانفیگ اختصاصی هم تأثیر قابل توجهی روی کیفیت اتصال داره).
📦
به همین منظور، ۳ تنظیمات پرسرعت برای
اندروید
و
ویندوز
آماده کردیم که می‌تونید از اون‌ها استفاده کنید.
🍏
کاربران آیفون:
اپلیکیشن
CoreForge
به‌صورت پیش‌فرض تنظیمات بسیار مناسبی داره و در اکثر مواقع نیازی به استفاده از تنظیمات اضافی نخواهید داشت.
📥
نحوه استفاده:
• فایل تنظیمات رو مستقیماً داخل اپلیکیشن
Import
کنید.
• یا فایل رو باز کرده و محتوای اون رو
Copy/Paste
کنید.
⚠️
توجه
:
این تنظیمات فقط
مخصوص اپلیکیشن WhiteDNS
(مناسب اینترنت ملی) هستن و به درد استفاده در
WhiteDNS VPN
نمیخورن ؛ لطفاً این دو مورد رو با هم اشتباه نگیرید.
💡
نکته مهم
:
ممکنه این تنظیمات باعث افزایش مصرف اینترنت بشن. بنابراین بعد از اضافه کردنشون ، مقادیر Download Dup و Upload Dup رو متناسب با نیاز خودتون تنظیم کنید:
🔹
مقادیر
بالاتر
👈
مصرف اینترنت بیشتر
✅
اتصال پایدارتر
🔹
مقادیر
پایین‌تر
👈
مصرف اینترنت کمتر
✅
اتصال حساس‌تر و شکننده‌تر
❤️
امیدواریم این تنظیمات تجربه‌ای سریع‌تر و پایدارتر از WhiteDNS براتون فراهم کنه.
@whitedns</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1277" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1276">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📌
چند نکته مهم برای عملکرد درست برنامه‌:
1️⃣
حتماً فایل PDF راهنما رو بخونید
تا برنامه بدون مشکل براتون کار کنه.
2️⃣
وقتی متصل میشید، صبور باشید تا
آی‌پی و پرچم کشور
روی صفحه ظاهر بشه.
3️⃣
دوستانی که میگن آی‌پی ایران می‌گیرن و سایت‌های هوش مصنوعی باز نمیشه:
• یا چند بار قطع و وصل کنید تا آی‌پی غیرایران بیفته؛
• یا از قابلیت جدید
حالت پروکسی (Proxy Mode)
استفاده کنید و اون رو با سایفون ترکیب کنید. این‌طوری هم سرعتتون عالی میشه و هم مشکل هوش مصنوعی کلاً حل میشه.
💡
*نکته:* ترجیحاً نسخه
مودشده سایفون
رو نصب کنید تا محدودیت سرعت نداشته باشید.
https://t.me/whitedns/1261</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1276" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1275">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdKbC2Euf7V2gCoCGPNaEkBc-u0R3MYh2xB3U4vU4zuM80TDvq_ymvT4F2uN2SR2WJrY8sooH4sem2NgAnldSi3DOrT0CWpGtMe_WedYL3L9YI3Q4kTYffW_fauLF90golwmWGODVz-SFOlqgtwnMrc4RBkpJj6zn8GNjU1vVtMoqq56fxLyNNNmxjJZMSgHXUhxn3cqG45SwW8XsaQ9xY7t9JsGin3gnsTdNAn1kYUNxxuqeeptK3AzZnZUNwDk0R1hW3_5irOAra9qXeRWEEckDicG8tMHZASPOwOKRReWebm-JGziCTmnDYXa0Hts-EnU9WeJgYk495wGov1tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/whitedns/1275" target="_blank">📅 06:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1274">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/whitedns/1274" target="_blank">📅 05:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1273">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1273" target="_blank">📅 05:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1268">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/whitedns/1268" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/whitedns/1268" target="_blank">📅 05:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1267">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La0UccfEoVYz8zDFALxpxVf7alr9YYp8cwoxIpWwgx5TGg2i4Anvtf_VEDfQ1AC8Jfpf6UdOYB182KREb8af8kNoOOVTz6uLQoUR0QBwB05hABWdKrKXRMhsAUKa11DIFMHrga23D8O620i995bSptZsVyYO1NkNJXSDHUgzjX2OPu3iuHc6jifNOHJibmgyCItQJQ8zYkIKQN8kJnLSsL_ZoQY81sjWLUbA8N4u6aEXCJemc8eHOJeUhwnLyA-LJ1pPxtQ44-zC0G50Gb8CGEJyePhoLkprn0okZy_DXGu0NlkOzIlLLInoaIXniPA9VBMeovjKoR6wsSr_xsi6JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/whitedns/1267" target="_blank">📅 05:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1266">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اگر توی نصب مشکل دارید نسخه قبل را پاک کنید و این نسخه را نصب کنید</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/whitedns/1266" target="_blank">📅 05:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1262">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/whitedns/1262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/1262" target="_blank">📅 05:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1261">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uDhFZ6mN0OiBW-AP8wdmh91p5goIJQrkLZPtx0SBAI6YcLmyQ5NtL4Xzz0rWKOknToUG8oiaAqcEnjp3Vl5asQlSjLWoxPTA8gLgd9VN5Rg5oCkE9NDa1xMIcPEGsN8O6QGTeUopWlzivCZvCK2BTWDAt3qFl5TvKrKtaq7h-eNasjJpN3HePBu2JvmYl46J9xxptwJJSNIzqEi7LYYw6Cq-sIge7TnLrsvg5lYTArqzrCmIqx8EVlijgDbtpYYs9kpsh2PUbbkVxbeEnLad6cuHfID1VLGTnAfbFjZCISOgxc5KdOgo3Zuq0g0rfD3W-uVlEJa4UClr2YGmLtBWpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Aether
1.2.0
🌐
✨
(فقط برای اندروید )
آتر یک ابزار ساده برای اتصال امن و عبور از محدودیت‌های اینترنت است. برنامه به‌صورت خودکار سرورهای سالم WARP را پیدا کرده و یک اتصال رمزنگاری‌شده ایجاد می‌کند؛ بدون نیاز به خرید یا واردکردن کانفیگ.
🔒
🚀
📱
روش استفاده:
1️⃣
اینترنت را روشن و برنامه را باز کنید.
2️⃣
تنظیمات را روی حالت خودکار بگذارید.
⚙️
3️⃣
دکمه بزرگ وسط صفحه را بزنید و درخواست VPN را تأیید کنید.
📲
✅
تمام! بعد از نمایش
Connected
می‌توانید از اینترنت استفاده کنید.
🌍
🎉
مهم :
⚠️
برنامه روی حالت اتوماتیک اول اسکن میکنه و ممکن هست بسته به وضعیت اپراتور شما و فیلترینگ حتی تا چند دقیقه طول بکشه. پس صبور باشید و به برنامه وقت بدید.
⏳
💤
یک فایل PDF با توضیحات دقیق در مورد کارکرد و نحوه راه اندازی براتون گذاشتیم . کامل بخونید لطفا
⚠️
https://t.me/whitedns/1265
کد پروژه :
https://github.com/QW-AI-Code/Aether/
@whitedns</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1261" target="_blank">📅 05:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1259">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTv_UJyei-YSsNHdqESyahhIOau39_B0WuvtzWLl8_n5HjfO0SPkDMAUO3L22D7Vnbj-7ZYJ5ZuIDW4giHp6mgJ6NTTUG43wR-TQ6Lt-rP1Z2KdSttJ6b6dFh1cd38nG07-O-19umu_jAqyOhyrU0NK1QcqYYnWNGeY5afNcN_mEBMUjYJlSDhvE9IsyNVdBpx6ZfmBEbePJ2TiRu-z_ADO_UIdA2BALSkco2gOngMCpwIBgS87RjC4MPidra-GWaebpXxd9lzdsTDsrL5lbHFLvVK8LTqCj2EzntrJUyJen6_6ivkbaqTkhdAO4FSHwx_xRtvQgbaxUJsWDtn1FLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای  ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/whitedns/1259" target="_blank">📅 01:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1258">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/whitedns/1258" target="_blank">📅 15:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1257">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👆
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1257" target="_blank">📅 14:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1252">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/whitedns/1252" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/whitedns/1252" target="_blank">📅 14:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1251">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXksbfd8IVjO-T4nUksTrJufWh1qpad_nQmcpaZ8V7Tdp67IBmDALCXrQZIQpeBkz2LyDw9tfgcSCCQ81AvdcgiT97s9qpzmrZ74wmT4T__XYaBTCVNV3anhq3X4mN5MLlFq33IQUj2SjDJk6dY3ZQ5moPuN0wTNuA518zWTq7Vti4ZwCETcm3sqLqZkhGJedNYr8yFcCUEgCPp0eX7fxt7uwO_p5QpAx0uieL40acQTvBTjBpHGndtKBfwkfpsaGZr9-5VjCglCTUz49O5ttyJmIB3I7KVCqtTmb6lBXY7dQ1QmpK3M3-VB3TQqjY8QPYj5biFGX0nstHukyC-Vww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/whitedns/1251" target="_blank">📅 14:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1250">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آموزش آماده شد اما تا ادیت میکنیم، ورژن جدید WhiteVPN رو ریلیز کنیم چون آموزش رو با کمک اون ساختیم.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1250" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1249">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همراه با فیلم آموزشی، درحال آپدیت کردن هسته WhiteVPN و اضافه کردن بهترین پشتیبانی ممکن از آپدیت جدید BPB  هستیم تا اتصال شما ساده تر و پایدار تر بشه.
نامگذازی اپ هامون هم داره کم کم تغییر میکنه تا کمتر گیج کننده باشه براتون
به مرور زمان همه اپ ها تغییر میکنند به نام های زیر:
WhiteDNS
WhiteVPN
WhiteScanner
WhiteBPB</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1249" target="_blank">📅 08:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1246">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">White DNS
pinned «
جلسه پرسش و پاسخ توی همین تلگرام به صورت انلاین بگذاریم  ؟
🔥
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1246" target="_blank">📅 16:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1245">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-poll">
<h4>📊 جلسه پرسش و پاسخ توی همین تلگرام به صورت انلاین بگذاریم  ؟🔥</h4>
<ul>
<li>✓ بله❤️</li>
<li>✓ خیر🫤</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1245" target="_blank">📅 16:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1244">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bU4gDKL2tRAb_J26p_L9z8HoEKZjyKUaecJbiV2WJke5EqJcgWgrw4hY2RjYwvKmgM5jhjZiUwFha0h53usw1bZBIhhcshL0W3UIIzNhSp0tar6yxpVatraeBsO_fYLbTz1WimqRuPsSDDp4_ThAwJhfy_Ll8DDqXTmg0cPyfzCjQh-VjJWRLPGOPWhb50Oklv6fFjajErhlh5AzEx4WaiI58H_NYZ4cSWW5sjBrqJctMVHoWV0DHnsxv6nYl54R6G-Q4sTe3grIPLV2RNm03qMgjRLUcQas8z4JQ6ga5CjYTkEw5lqB9ibHOX7CZ57Whbo7o4Dk2vy3DJhrImgJ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده است.
✨
مهم‌ترین ویژگی‌ها و تغییرات این نسخه:
🔹
نصب سریع با One-Click Wizard:
دیپلوی پنل حالا فقط از طریق ویزارد آنلاین و اختصاصی انجام می‌شود و پس از نصب، یک لینک کاملاً پرایوت به شما می‌دهد (روش‌های نصب دستی روی این نسخه کار نمی‌کنند).
🔹
داشبورد مدیریت داخلی (Admin Dashboard):
امکان آپدیت پنل به نسخه‌های جدید، حذف کامل پنل، و ریست پسورد مستقیماً از داخل خود پنل اضافه شده است.
🔹
راه‌اندازی ربات تلگرام:
مدیریت کانفیگ‌های تکی، دریافت لینک‌های سابسکریپشن و مانیتورینگ مصرف (همراه با هشدار مصرف بالای ۸۰٪) از طریق ربات تلگرام.
🔹
حذف کامل Environment Variableها:
تمام متغیرهای ثابت (مثل VLESS UUID، Trojan Pass، Proxy IPs و...) از داشبورد کلودفلر حذف شده و مستقیماً داخل پنل قابل آپدیت و مدیریت هستند.
🔹
ارتقای چشمگیر امنیت:
لاگین به پنل حالا نیازمند ایمیل کلودفلر شماست.
مسیر ورود به پنل به یک آدرس تصادفی و امن (Secure Path) تغییر یافته (دیگر با زدن
/panel
وارد نخواهید شد).
🔹
تنظیم سریع Custom Domain:
دامنه‌های سفارشی خود را می‌توانید مستقیماً از بخش Common settings وارد کنید تا کانفیگ‌های مربوطه با تگ
D
به سابسکریپشن شما اضافه شوند.
🔹
قابلیت‌های جدید شبکه و پروکسی:
پشتیبانی از Xhttp و VLESS Encryption برای Chain Proxy در هسته‌های Xray و Clash.
🔹
انتقال آسان تنظیمات:
اضافه شدن قابلیت جذاب به‌روزرسانی و همگام‌سازی تنظیمات از یک پنل ریموت BPB دیگر.
⚠️
نکات بسیار مهم برای اتصال کلاینت‌ها:
حتماً کلاینت‌های خود را به آخرین نسخه آپدیت کنید (حداقل Sing-box نسخه 1.12.0 و v2rayNG نسخه 2.2.3 به بالا).
برای اتصال پایدار در v2rayNG، حتماً گزینه
Hev TUN
را فعال کنید.
در صورت مشکل با فرگمنت در برخی ISPها، حالت
Packet
را روی
1-1
تنظیم کنید.
لینک ریپو :
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
لینک ویزارد :
https://wizard.bpb-panel.workers.dev/
@whitedns</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/whitedns/1244" target="_blank">📅 12:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1239">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/whitedns/1239" target="_blank">📅 12:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1238">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nmm9tMtSaJHT6bHh_toScQJJhfFFXxQ4sa9KYjaD0SPgH-6UyVUBzDIdK12XvtU5Nf1dqswTg7CpqBQU5YTTZiavBH8MgsBMgByQeLnBlqypBlKgFHhWgWuWUkIdnjlOIjUcg36mPqaYUSXfXmEy7qtFJt6gBhIgqh8SSAkXHbcaJ59aOn7KZulUC485-dOC1aJZ4aCX5px1Jk0oVoWIlSSkKJ-ot9YwG6YNaXiJe97-_NHVAapO4bfpw6-hIFU_TLJWGGIfetCCZfDSW1hvj35fnR_E3wCwtghWLqQjika75H3qTScvvO0Ae6OUjIP9dvbhx5UnIQuzFLOshIgXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/whitedns/1238" target="_blank">📅 12:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1235">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.2 MB</div>
</div>
<a href="https://t.me/whitedns/1235" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تازه‌های نسخه ۱.۱.۰
🆕
اِتِر (Aether)
تایل تنظیمات سریع (Quick Settings)
— روشن/خاموش کردن VPN مستقیم از منوی بالای گوشی، بدون باز کردن برنامه. یک بار اضافه‌اش کنید: منو را پایین بکشید ← دکمه مداد/ویرایش ← تایل
اِتِر
را بکشید داخل.
اشتراک‌گذاری VPN با لپ‌تاپ یا گوشی دیگر
📱
💻
— از منوی کناری ←
اشتراک‌گذاری VPN
. گوشی شما یک پراکسی
HTTP (پورت 8118)
و یک پراکسی
SOCKS5 (پورت 1080)
روی وای‌فای/هات‌اسپات باز می‌کند. آدرس دقیق
ip:port
قابل کپی است و کافی‌است در تنظیمات پراکسی سیستم دستگاه دیگر وارد شود.
تنظیمات پیشرفته در صفحه اصلی
⚙️
— دکمه جدید بالا–راست صفحه، پروتکل، حالت اسکن، نسخه IP و بقیه تنظیمات را در یک پنل پایینی باز می‌کند.
آپدیت بدون حذف برنامه از این به بعد
🔄
— همه بیلدها از این نسخه با یک کلید ثابت امضا می‌شوند، پس نسخه‌های بعدی مستقیم روی نسخه قبلی نصب می‌شوند. نکته: برای آپدیت
از نسخه 1.0.0
فقط یک بار باید برنامه قبلی حذف شود، چون آن نسخه با کلید موقت امضا شده بود.
رفع اشکال:
پنل اشتراک‌گذاری VPN حالا بلافاصله بعد از روشن کردن سوییچ، آدرس
ip:port
قابل کپی را نشان می‌دهد.
✅
عنوان ریلیزها تمیزتر شد (دیگر پسوند "(build N)" ندارد).
📝
Downloads
📥
https://github.com/QW-AI-Code/Aether/releases/tag/v1.1.0-build.2</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1235" target="_blank">📅 11:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1234">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚡️
اِتِر (Aether) — آزادی، با یک لمس!
⚡️
نسخه اندروید   درویدِ قدرتمند و رایگانِ اِتِر؛ اینترنت بدون محدودیت، بدون ثبت‌نام، بدون سرور شخصی!
🚀
🔥
چرا اِتِر؟
🖱
اتصال با یک لمس — VPN کامل سیستمی؛ همه اپ‌ها و مرورگرها بدون هیچ تنظیمی از تونل عبور می‌کنند
🛡
موتور…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1234" target="_blank">📅 11:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1233">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ny3NfoELW9U1ek3iKpJOl7VS0IAveFrqbZLVhrGjtVwUKyYqkkMHfS2I3TJBVt-J8X-Qdd_z8wtT2j-4Z8Rapp-FeGv8GjOs3pXGZy2nr8dxWN1yZb9yS6WwTeAl7wTjZs24BmHaLaiuQnnSDlNCIftirgCGQ4UJLvJOU_deft1IJ3BDXeFGv8TC_FNlPpRSa_eah2XUjSfBmQpbUyElrFmWyJ-4Jbq2JegacwmHjjODC_SQP1-4a7UCiGzAyLQjiHH11rsb31DBmMEpiOsFA1lr22vrRmyGHBA-pn527d4uKMEddLNm5DLl0LCUKAFoP8vvv84SiAtvXNrgyrgIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1233" target="_blank">📅 05:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1232">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⚡️
اِتِر (Aether) — آزادی، با یک لمس!
⚡️
نسخه اندروید
درویدِ قدرتمند و رایگانِ اِتِر؛ اینترنت بدون محدودیت، بدون ثبت‌نام، بدون سرور شخصی!
🚀
🔥
چرا اِتِر؟
🖱
اتصال با یک لمس — VPN کامل سیستمی؛ همه اپ‌ها و مرورگرها بدون هیچ تنظیمی از تونل عبور می‌کنند
🛡
موتور پیشرفت
ه WARP با تکنیک‌های ضدفیلترروز:
✅
پروتکل MASQUE (HTTP/3 و HTTP/2)
✅
تونل تو در تو WAR P-in-WARP (حالت gool) برای سخت‌ترین شرایط
✅
قطعه‌قطعه‌سازی ClientHello و مبهم‌سازی ترافیک
✅
اسکن هوشمند و خودکار بهترین endpoint
⚙️
۴ حالت اسکن برای هر شرایطی: Turbo
⚡️
/ Balanced
⚖️
/ Stealth
🥷
/ Thorough
🔍
📊
نمایش زنده ترافیک — سرعت لحظه‌ای و مجموع دانلود و آپلود، درست مثل VPNهای حرفه‌ای
🌍
نمایش IP سرور با پرچم کشور + تایمر مدت اتصال
🧪
تست خودکار سلامت اتصال — بعد از هر اتصال، خودش بررسی می‌کند ترافیک واقعاً جریان دارد یا نه و دقیقاً می‌گوید مشکل کجاست.
🔁
اتصال مجدد خودکار — اگر ارتباط قطع شود، خودش دوباره وصل می‌شود
🔒
امنیت کامل، بدون نشت:
✅
بدون نشت IPv6 و DNS
✅
بدون بکاپ اطلاعات حساس
🎨
رابط کاربری زیبای Material 3 — دوزبانه فارسی و انگلیسی، با منوی مرتب و مینیمال
📱
سبک و بهینه — نسخه مجزا برای هر معماری (arm64 و arm32)
📥
دانلود مستقیم از گیت‌هاب:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1232" target="_blank">📅 03:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1231">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سلام دوستان عزیز
👋
🌸
اپ CoreForge یک قابلیت جدید برای کاربران iOS اضافه کرده
📱
✨
این اپ شبیه WhiteDNS است که برای iOS و شرایط قطعی اینترنت طراحی شده
🚀
🌐
🔗
لینک:
https://testflight.apple.com/join/3htm1Whc
🎥
آموزش استفاده:
🔗
https://youtu.be/filwdiPKN90?si=O-hvgeNw43t4BUmR
📲
کانال تلگرام:
@WhiteDNS</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1231" target="_blank">📅 17:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1230">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامیرپارسا گودمن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6b89a933.mp4?token=fVxFcaFaamXWRteLLyrQmBc6GCff9hphOoeXGZ4uj9zUmM35M8WMxpWYW4ciwdy6duT3Ie1p-HDvvJ5f96_UzioSpvwhMa-_6gIEOLx31KYnrADruOz8vIjX1kIPN__e3j6HmvoIPZgI9rQo8OD50h7ygyNcZWwFDKt3uGUV4dXCsV2X3xs4lGV00MXIL5GeUL0Wm5MjaY0IOsNFLYqeILeAne7SYMr19DZZoOzBowUJiaTRGz76ees0rGS04awVd14jNVrFIC4D48fFC_VxSr4udrYY8rmY0x8WnLS-0BCtqfuIjsBq64yx-1S3VNLaWrcEzbHV45PLnFlqiAMhbh50dzfFVPFkv0CNS2ut2SH8QUh6n7d5UrZVclIW1DgC_Mqq4I7RVyE4VlAPrRPPykGwy9ae9_IQMHwZk0CDQjguURUp_i70pIMGzGd9XotwIt7G2JLnK3XmZmd5DpuQHkFI6OKwJEhFIfvWQH0PmxsjZedip_PDRBnpsvD-hgbPkLC5WEPDZ1pqkkIHRNuF4zZCoHS3tMLQUF6nsehS5mS3fUzY2cMMkewZmaKPWkc9tP-pcRjXqzC9eoU4TaovMrRGqnGSGX5fMaAKr-0eIEVum4-dFrTe_MlXynVV0kXTd8x1IYeydOKkoWr3bka4PUgXtazduZ_kj_AVp_Vc8cc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6b89a933.mp4?token=fVxFcaFaamXWRteLLyrQmBc6GCff9hphOoeXGZ4uj9zUmM35M8WMxpWYW4ciwdy6duT3Ie1p-HDvvJ5f96_UzioSpvwhMa-_6gIEOLx31KYnrADruOz8vIjX1kIPN__e3j6HmvoIPZgI9rQo8OD50h7ygyNcZWwFDKt3uGUV4dXCsV2X3xs4lGV00MXIL5GeUL0Wm5MjaY0IOsNFLYqeILeAne7SYMr19DZZoOzBowUJiaTRGz76ees0rGS04awVd14jNVrFIC4D48fFC_VxSr4udrYY8rmY0x8WnLS-0BCtqfuIjsBq64yx-1S3VNLaWrcEzbHV45PLnFlqiAMhbh50dzfFVPFkv0CNS2ut2SH8QUh6n7d5UrZVclIW1DgC_Mqq4I7RVyE4VlAPrRPPykGwy9ae9_IQMHwZk0CDQjguURUp_i70pIMGzGd9XotwIt7G2JLnK3XmZmd5DpuQHkFI6OKwJEhFIfvWQH0PmxsjZedip_PDRBnpsvD-hgbPkLC5WEPDZ1pqkkIHRNuF4zZCoHS3tMLQUF6nsehS5mS3fUzY2cMMkewZmaKPWkc9tP-pcRjXqzC9eoU4TaovMrRGqnGSGX5fMaAKr-0eIEVum4-dFrTe_MlXynVV0kXTd8x1IYeydOKkoWr3bka4PUgXtazduZ_kj_AVp_Vc8cc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">https://t.me/xsfilterrnet/3623</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1230" target="_blank">📅 00:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1229">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kQZy5vWDnOLREeShVYZGgdbALgCwwtJ3Aw7KAktlyY1Xpz_CpBmkS0n0RbXxAZWKrKoec9T-7lVnnbKIBN7bmxVF45QUmVTPk9zR2ew1L3TgotfXOGJoJOLjkzHl1WLkhJGt1A0QwV6LaXWT0h-glb2iDbiwnq0t9pgQB9XNL6e2HDBOv82_ZR-PTsQBTydoIgAd0t5uRaBRUKNnnnjd56TI-W0NqjuQ9bytvBcyTW1im1Nl36I-fwKpAv5OHsFLkBXVYwXkPdMS6BnZadE-TIgCJBVAA1jQyQrFWOR1A3BW9Exll2aOthw3FzBUZ-89izb_xr9dFcEUFItdDTzYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1229" target="_blank">📅 17:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1228">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1228" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1227">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1227" target="_blank">📅 12:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1226">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1226" target="_blank">📅 12:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1225">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KfwbqLY9vQo2etRc6DksWR3oV-zCCiJ3onOXBDVaCVvyGj50W2zHEDRCQjbsluhSR2Nkd4GI6jpuR41ofpQKLM7ketse0PYTNjLJubOXOGvmBTmZNqHN19vD3E_WKVJCkLJ6D0fGuuCN-jJPwESLzF27NoHzX0Lcw1kuwc3UfNal-6BFRM1NgJ9Hv5icD5ocWprIP1w3j1Nl9zfR1f-tNZH8kcBLiNtpUoGLxiEuwEm0QtrTs_WXoHoND2aoOi3SX7Pw4CNZ1aXfmL0uc5DtUwzM0oudCD0ikaJqnPlBBv7APmj5cEsYdiCRBaHyJLvHQfibxNhDBdPrOeUHo6D3UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/whitedns/1225" target="_blank">📅 06:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1224">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EgJ7jvYGtK6Nbmct6zbX8Z8PvYMA2NqNDA0gLwEeeRpEMiIYw1MA1p0r4g0Inl8Dg3rkQJStQ2DCQRBQQqMEgUbyo8MF4TXue-w7d_HwU54SHlqdQsbw9_Bv4oDXHqMcqQ1pY8_Ofyjo986uZ_HYQwx2d53LlMV9YHQsm0xlq60QF1v6IGMGg_eyuG5DZigtZHwHwcRsaYI1Zbz32lZvmsSUQkynH8_Kg7XeG5Wr4VBUjuNHZrycjQk732QIgW0c2L1NGfHY1Yn4e9b4RKsQmhfZUJ8Fn8eumhzT5qKJEfoSaX-eu-UJ-DDbRwqfjdshOJxAS101jsaLWgdDZOwOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/whitedns/1224" target="_blank">📅 20:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1219">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1219" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1219" target="_blank">📅 17:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1218">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQgXExU2Hu5gBoQcHvuadP0TIurAqzeUwqS2TwNF8o6Yz5Wz-kbm1150gvUdfhKMZZqTdM6S5qV10ZDql7UoGg4Zj_6N2x7Xdu1l17WUVC3UiRUJiA01LtFz1WJowyrzEDaasRrBqowoknLCjP0h16Gbn6udklSPJ-gfmUa77CIg0LiS4tcUi6xIdKVnboPqw0hI7rzN7JCP6tygJTh_Qz7GTBE15pkn8Oh94MUXZM3f1rQe5YSYtqnc04UVVeQbL_q0pC7sgqONYGPjGdbXyrHQTRk2PJG4P3qo0QoJBA8pd3XSMBBfTCJ86wVfG3x1tmjm7aUla6cyERm8F6XOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/whitedns/1218" target="_blank">📅 17:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1217">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/1217" target="_blank">📅 17:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1216">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1216" target="_blank">📅 14:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1215">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">White DNS
pinned «
دوستان برای همه اینها اموزش هم گذاشتیم که الان لینک را اضافه کردیم .  لطفا بدون دیدن این اموزش ها سوال نکنید
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1215" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1214">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1214" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1213">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1213" target="_blank">📅 12:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1211">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fh6BvWJj9Z9vJ0jw_eZxyyJqNeXjSF0gNRS0hRRBCQCCEc9iKyUyOOJ2zC0vXb8Ms4tNCeYmy28O2aF3D4WHjnkj2N6xW5t-8u7Op1SblfY93ZnH3wJwZKXJ4mmADUvOlfDrsvfOGMCxonzbKmavFvfXYLvmIdc1njviu5X-hJjpn1U0pvwV7-j9S7H6ELHEo1zZqY7caypXiOf8PVA3S5qZgMdbIRGft_TmIts5QBINX1EJxK61OpBi2qyW_iLR-RGEzJ7U48ORUBi6pDuPN8HuKJl9ULq_Py8_twJLad-plBhiQ9RtOOs_foT1R3w8fA9dYJTOKfb6x01DPPRCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/whitedns/1211" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1210">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VYEJNl9NFSGfLHZK9dLRi-_UGZ99ofeP9RJKbrlBN_rQaLQ3RqKkBaI3WGYm_-HNHGww_VbkzxJV9nNWi9QotiXNtufLJO-myv3YZz-eHfAGPVpzrEuu2A-cF7mLR4ysKoSmFjwZeg4hMJK4JevDaB4Ssth9ahO394LNnM_yWOOcGR_3MlPmheYztMofzO6mgt0G6NfJjJzbN4aJTr16wbwPHUqAv2o-XmaRh-XNdZygdwY457l0ROeIyonQxQrZHLvLhIDTus4ondtGl6nW5KyfbYUNtM85p7OaW9PVxeyKFIThNcSPu5btme8xKNNPcOLwA86LZx8lb5_txLmEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در whitedns android</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/whitedns/1210" target="_blank">📅 12:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1208">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IaWN1HSfHOrei4Mej-wc_dkcc4YbIyh5hYQTzgwU4UKJmKZCygWMn5a2YnB6uX8b-CRlSs-2jCwo1jaCl_RBVIyl9KTgYI7CbCjFnNIjuihoscMBKs9RTIZwqQU2FIIh4-FF7Js667M7skTOCJ09mGflV8kl-kz2weMg6wmKHBModrRPLQQ9I0bCexbp8Bql1-vfVIyxVnpf5tZyckyLlcHtFMa-iwt18Z-BUIgLq_XnTqiS0EuwgK2XmS_uPEBreuPE8ojYUkbIam-17KtdZxYSuZVTzOvPEhT4RlwRSmaciPdhVs9lQcxxeniofA5lNxPOt7gFrvRwexrVnIVS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در Whitedns windows</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/whitedns/1208" target="_blank">📅 12:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1206">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Android.zip</div>
  <div class="tg-doc-extra">2.5 KB</div>
</div>
<a href="https://t.me/whitedns/1206" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/whitedns/1206" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1205">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/v23iZ-Rt4TOBZDPofj_HJTYGRSLLh0UXk-ow2Oqgw8B13jxlBUgdTOhVQt2XTGKCYuBb5vOm5BCQkmNBZR667az6izl9SRWKhaXccU_aqLp-abUe6-M6XAcyxOovH5IyghS6sxN0-6tAWUaMYHXeLqzSN2aDKAIoFJWETnP_XylWW9E_bdGO55umpBsjVMSW88PK-OrccRm9n16PZMSHIh1d4swhKabsWe60mK-BxMIMeWNnGks_xbPvMYLwXqi22NSrN8S6NjMI14dMqDOvY5fnvPCQZTjiQnC_m3HFFOWBnomryFI7OijjSbYVvB2diN34Y6PO4t2GpYHAoFfOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
افزایش سرعت اتصال WhiteDNS
تنظیمات اختصاصی whitedns
یکی از مشکلاتی که بسیاری از کاربران با اون مواجه هستن، اتصال موفق
WhiteDNS
با سرعت پایین یا ناپایداره.
✅
یکی از مؤثرترین راه‌ها برای افزایش سرعت و پایداری اتصال، استفاده از تنظیمات بهینه میباشد (البته استفاده از سرور و کانفیگ اختصاصی هم تأثیر قابل توجهی روی کیفیت اتصال داره).
📦
به همین منظور، ۳ تنظیمات پرسرعت برای
اندروید
و
ویندوز
آماده کردیم که می‌تونید از اون‌ها استفاده کنید.
🍏
کاربران آیفون:
اپلیکیشن
CoreForge
به‌صورت پیش‌فرض تنظیمات بسیار مناسبی داره و در اکثر مواقع نیازی به استفاده از تنظیمات اضافی نخواهید داشت.
📥
نحوه استفاده:
• فایل تنظیمات رو مستقیماً داخل اپلیکیشن
Import
کنید.
• یا فایل رو باز کرده و محتوای اون رو
Copy/Paste
کنید.
⚠️
توجه
:
این تنظیمات فقط
مخصوص اپلیکیشن WhiteDNS
(مناسب اینترنت ملی) هستن و به درد استفاده در
WhiteDNS VPN
نمیخورن ؛ لطفاً این دو مورد رو با هم اشتباه نگیرید.
💡
نکته مهم
:
ممکنه این تنظیمات باعث افزایش مصرف اینترنت بشن. بنابراین بعد از اضافه کردنشون ، مقادیر Download Dup و Upload Dup رو متناسب با نیاز خودتون تنظیم کنید:
🔹
مقادیر
بالاتر
👈
مصرف اینترنت بیشتر
✅
اتصال پایدارتر
🔹
مقادیر
پایین‌تر
👈
مصرف اینترنت کمتر
✅
اتصال حساس‌تر و شکننده‌تر
❤️
امیدواریم این تنظیمات تجربه‌ای سریع‌تر و پایدارتر از WhiteDNS براتون فراهم کنه.
@whitedns</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/whitedns/1205" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1204">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1204" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1199">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1199" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/whitedns/1199" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1198">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_uo3dOkwhEuyMZypd_DB9mddnpZOQ_ZweWIfNYsMKWdsliF1o4OOmLkaa0hFwTT65G6VBucYQt9HX6yBPTKAWOMfpN66yFGIpOT_5jC7SSetvmYsHtutg3SnHY8s63XtW8Bdgv8YnH8DtypvJGW4ERqgoxVgO8Nr0lN95cp3xAXowF-Sy0Y5ePt2TDxbW5BlX6KxooKla1FdRJ-OfzZWXcPn2HUwtBdQX3whdKqiS_1u63jiXNml3eGJcQn1ryjqhiEX6fEJTy5kqW_DjrICFueR7V-NiwjtPfDVHn8jTjUULAlYfHJRL2nEKZSYcKgg5q940TNmKRbaG2JnEytmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/whitedns/1198" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1196">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AHxx1f_gyQckK5xOvwzxWKgKeorIodLC6pNk35cP40JZzILaf3oCgH8kyRlCyW_NuEC7QmM8f6OCKekfpJp2TxxyUOF1crNIgKD7bzeifRGoqv9g_DDWNhZ56mxI6Oe1J3jhnliz6mCpp36d4Jx1d00Supu_qaOZfBfybknTBV6_u1NGhSiYfU2Q2IH-LTkt06EeTCsRPczE80aM1bx8HDUgJ9h3_tRNHrKO033Pvce5fo0hdxJG4JcfnJaS-Cpnwoh09g9zLbXp9t89HJmam8rn5FNbAb0sqwGyatF7PWf9oia2oOoYubKPxvSGAxlWREpCt7EfxavlrA12xLyYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h4quCstAHIkdbTSgDEkxw2bvGW5w9BAfaEk0CdyxShJm8QKE0yKhuhjza6HynhJ0CL3OejHnCy1SaAvoXfk8lTVRq3yFDLbOEpgMtORLjMLdBYKHTPZgO7Y2rRJd5JC3UYuZu6XVlPQ7Aik2-XlYD3-gvfIcD2ztxvoDTs92bdpcLHQpZKI-1tkQ_d5LL97kHLHUXK1jm-6AQq83kUTxebJ3qSqua9NcPwv942eepaCsIHboFiT94GvzcLgAu3tT_2vZWQWk8-P8IF0FwloP11ljhKNGaS6HNrOzTVu3rfnNISEmufaZT-ostY3HzK-1REdTtrxeTOajDPQNIpT1xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI (نسخه 0.4.0) با هسته‌ی جدید!
نسخه‌ی جدید برنامه آماده‌ست. توی این آپدیت، هسته‌ی اصلی (Aether Core) به ورژن
1.2.0
ارتقا پیدا کرده و قابلیت‌های زیر به GUI اضافه شده:
🔵
رفع مشکل وضعیت Connected فیک:
قبل از این، بخش Validation ابزار با پینگ کردن
1.1.1.1
(که داخل شبکه‌ی خود کلودفلر هست) وضعیت رو متصل نشون می‌داد؛ در حالی که ممکن بود ترافیک واقعی اینترنت قطع باشه و لود نشه. حالا ابزار یک ریزالور خارجی رو هدف قرار میده و باید ۲ بار پشت هم موفق بشه. یعنی وقتی می‌نویسه Connected، واقعاً متصله.
🔵
اضافه شدن انتخاب ترنسپورت برای MASQUE:
توی بخش Advanced الان می‌تونید نوع پروتکل ارتباطی MASQUE رو تغییر بدید:
HTTP/3 (QUIC):
حالت پیش‌فرض؛ سریع‌ترین هاندشیک و بهترین کارایی (اگر شبکه شما با UDP مشکلی نداشته باشه).
HTTP/2 (TCP):
کاملاً شبیه به ترافیک عادی HTTPS؛ مناسب برای زمان‌هایی که شبکه شما UDP/QUIC رو اختلال می‌اندازه یا مسدود می‌کنه.
تنظیمات انتخابی شما به‌طور خودکار ذخیره و در استارت‌آپ بعدی اعمال میشه. (این سوییچ فقط روی پروتکل MASQUE تاثیر داره و برای WireGuard/gool غیرفعاله).
🔵
به درخواست دوستان فرانت کار لوگو هم از دیفالت عوض شد
🤠
دانلود نسخه 0.4.0:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1196" target="_blank">📅 04:29 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
