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
<img src="https://cdn4.telesco.pe/file/pl606l-dFqBSNi9MW3lBwyErWKK3f1i9OEOFbv8lYWkV5EdlvLXFhkzuG791xogaOfPz4J_ztJiWlAkA3acD8gyYvxNZUhDeQPnuf4vlahGlzg0k4RormsRU6kyFlUiJjTV1WhVWSrzkDOLq3sI-v61puRaV4PIGd3mo9EXiuvQ_vWimJeykg2cTFmN3Ep7Hn6m5DCz4ZjBmI2DARYL82rYcrD91HkLL4Ln7qZhQAGSpxTmY3FIcnYfsUY_TY_EX_8n8DLXhJpDi5y5bzETue0VXzZwUqipeLFYOMdAJhMQ9Mf8rIHhx0XMxQ3udbn2GIbvrnIN_4XqGnQjO581fBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.9K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 10:00:44</div>
<hr>

<div class="tg-post" id="msg-9034">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njhRLUtXd8EH-foyFxbnqbXneqVDL1cXsEI1zFsFDHYhW2XDh1QMegsWJTDGN2Q5ayUyWrhmgaqT5yW7umoMo3oqzYK6eeitDkf_8v73Bl6XkUQ2fGhP69y5RwS8tmV13qWkV0mPz13VtkNis-qlgqPh3Ixj-2iNeII0wnoWksctiVWaiX2OcHTgYeIFR7e15SCQlt8dEXSwNSM7Hg6wFH6kgHaRZjpdLtU66EjkEQfbSpF3KZLh36skslCudpUz-ReLpGjpCZtUKDjykeIDXjXaL13_XvbANMpiJScUokCIHHturNtGz7HLIQ7prhsRr-kSD9of9gbRqka3GnCvRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot  جهت ثبت سفارش به ربات مراجعه…</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/IranProxyV2/9034" target="_blank">📅 22:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9033">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6wawdVzaObkPvymV12BBE028hHrApJrUKFbJqsVAw60ErfEjbrtYoMiHH340o0GaFK5qldp0_S-vNdyRfnvs7563PxmE-EuylEcPUAAH8LFouwdt9ykKSEt1e6QE3aNNulBG-IVAgckomcssIaGDkOVsQL4GA69vIklRnP0iBdJJ0Te-BhhewxAWtzM4jeSI2zOrc5DbDvDBaJM41Ptw6rYptw1CxwezPn24qTosgr3FvFAGWM5d75MyGxASoyOclNJjE7eBKA75B7YB6e_BLNVdgXsFh0N2k7kNcKsqqfWkkK-AZgPQu-qNR-JKsr2UVEgn2QNrslXb48XRwJEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/9033" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9032">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=178.105.226.182&port=443&secret=ee396219a1e9b2aebf6f245a1495777811706c61792e676f6f676c652e636f6d
https://t.me/proxy?server=orbit.proxyonline.online&port=443&secret=eea49899bfb9f5b061d6213e6f6480ea006f726269742e70726f78796f6e6c696e652e6f6e6c696e65
https://t.me/proxy?server=94.183.221.165&port=443&secret=a252e3eb41417da5e2332193f25bcf34
https://t.me/proxy?server=relay.proxyb.site&port=443&secret=eeee9dfed6b3721e5b2788f5100af2ff4272656c61792e70726f7879622e73697465
https://t.me/proxy?server=5.75.200.229&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/IranProxyV2/9032" target="_blank">📅 15:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9031">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
مث اینکه جنگ فعلا به پایان رسیده، هردرطرف از موضع خود کوتاه اومدن ولی البته یه نکته بهتون عرض کنم که این شرایط فقط تا پایان جام جهانی فک میکنم آتش بس برقرار باشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/9031" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9030">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:   نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/9030" target="_blank">📅 14:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9029">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/9029" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9027">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=fresh.nolags.pw&port=443&secret=dd691fa48fcc661b68fe4f5200c5b174f9
https://t.me/proxy?server=91.217.166.212&port=16&secret=dd1603010200010001fc030386e24c3add
https://t.me/proxy?server=fool.feel-fly.info&port=25565&secret=7hYDAQIAAQAB_AMDhuJMOt1iaXNjb3R0aS55ZWt0YW5ldC5jb20
https://t.me/proxy?server=91.217.166.22&port=20&secret=dd1603010200010001fc030386e24c3add
https://t.me/proxy?server=91.217.166.21&port=20&secret=dd1603010200010001fc030386e24c3add
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/9027" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9026">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/9026" target="_blank">📅 13:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9025">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
دوستان احتمال داره دوباره اینترنت بین‌الملل با محدودیت یا قطعی روبه‌رو بشه.
✅
از همین الان برنامه‌هاتون رو آپدیت کنید و این اپ‌ها رو نصب داشته باشید:
• Happ
• NPV Tunnel
• V2RayNG
• Psiphon
• ShiroKhorshid
• Http Injector
• NetMod
⚠️
قبل از هر محدودیتی، آماده باشید
💙
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/9025" target="_blank">📅 13:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9024">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcfwqZ3zJie_XSuY28-GF3uv6y6Y7V9kuBHD2T1vCEujCLd7QvkrSsLdzEos3_WcW7Fch2AyjEG4nhLV7pu--snHTFVSfxFc9HoVy3oYbAM6WlZ5hUvTwuCBuFaBuJgAyV2VtIWx40lhd-SIPbLmEwk156-dRP6S81p--lZwR-ZVtW45dUAFVpe2kcnAVXHBYqY8t8oZ7UvuwQzgx71qncCQMASr8JkANXqz86V-b2-CcGoR_6n4Z0vIQs8O_XYXtrYfKtRIuE1BIOtwlRJnP02NI-kLUq1d77r37t7hknSYbpZs6ROLLb3DkQaDmgDXw2qEVXJpgJ6li_WDk-LCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دوستانی که سرورا براشون متصله نمیشه، ۵ پورت و ۵ لوکیشن جدید اضافه کردیم، لینک سابتونو بردارین، حتما دامنه جدید رو از قسمتی که نوشته
info.russiaproxyy.shop
به این دامنه جدیدی که براتون قرار دادم
⬅️
doc.midnightfits.com
➡️
تغییر بدید و وارد ساب لینکتون بشید سرور جدید رو بردارین
🔹
نمونه ساب لینک جدید
https://doc.midnightfits.com:2096/reza/xxxxxxxxxxxxx
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/IranProxyV2/9024" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9023">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=s3.mowork.twc1.net&port=443&secret=ee90872f20ccc37e3aa2681602f51df71273332e6d6f776f726b2e747763312e6e6574
https://t.me/proxy?server=s4.mowork.twc1.net&port=443&secret=ee3e9cfe9af4494731b9a566075ee8c3bc73342e6d6f776f726b2e747763312e6e6574
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/9023" target="_blank">📅 13:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9022">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
vless://a78bf929-6883-48af-902d-7737793eeb17@hu02.sonicsonic.icu:443?security=reality&encryption=none&pbk=z-TKWOWgZLfzQ-wNdwXQqVwaUgCmbchM2Xtrk1NGynU&headerType=none&fp=qq&spx=%2F&type=tcp&flow=xtls-rprx-vision&sni=hu02.sonicsonic.icu#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/9022" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9020">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پروکسی مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=imtproxy.ir.imtproxy-ir.info..&port=443&secret=ee16550001232d00bb5190728b72644171706c61792e676f6f676c652e636f6d
https://t.me/proxy?server=65.108.154.5&port=443&secret=eecdf95381f978fb348f233a14b2251e6d7777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=91.107.148.135&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=5.75.206.125&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=91.107.167.170&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/9020" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9019">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پروکسی مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=91.107.156.186&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=153.80.241.214&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=51.254.130.47&port=8443&secret=a84102e409230c3b69dd4f68cef86baf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/9019" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9017">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
براتون پروکسی نت ملی و اوپن و... میزارم، حتما ذخیره کنید و برای دوستاتون بفرستید درصورت قطعی اینترنت استفاده کنید تا بتونید، حداقل کانکشن رو به تلگرام داشته باشین
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/9017" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9016">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری-آکسیوس به نقل از رادیو ارتش اسرائیل اعلام کرد که ارتش خود را برای چندین روز درگیری در ایران و احتمال بازگشت به یک نبرد طولانی‌مدت آماده می‌کند.
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/9016" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9015">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
دفتر نتانیاهو:
در پاسخ به شلیک موشک از سوی جمهوری اسلامی، اهدافی در داخل ایران رو هدف قرار دادیم. اسرائیل همچنین در بالاترین سطح آماده‌باش دفاعی و تهاجمی قرار داره.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/9015" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9014">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
فوری/نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد  بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
✅
با ما اخبار جنگی بروز باشید  @russiamilitery</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/IranProxyV2/9014" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9013">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پروکسی | فیلترشکن | کانفیگ v2:
🚨
فوری
⚠️
👑
نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد
بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
پروکسی نت ملی:
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/9013" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9010">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
ارتش اسرائیل:
در ۲۴ ساعت گذشته بیش از ۹۰ هدف متعلق به حزب‌الله، از جمله انبارهای تسلیحات، مراکز فرماندهی و سکوهای پرتاب موشک در لبنان رو هدف قرار دادیم. این حملات با هدف از بین بردن تهدیدات علیه شهروندان و نیروهای اسرائیلی انجام شده.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/9010" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9009">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
لشکر10 سیدالشهداء سپاه کرج مورد حمله اسرائیل قرار گرفت
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/9009" target="_blank">📅 12:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9008">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🆕
خبرگزاری فارس:
در صورت ادامه حملات به تاسیسات انرژی و زیرساخت های ما؛ کل زیرساخت های منطقه رو میزنیم.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/IranProxyV2/9008" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9007">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
مهر: شنیده شدن صدای انفجار در جنوب تهران
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/9007" target="_blank">📅 12:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9006">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
رفقا جنگ جنگه مراقب باشید از یک سری مراکز نظامی فاصله بگیرید ،امیدوارم تموم بشه این جنگ و همه مردم ایران سلامت باشن
❤️
💎
پروکسیارو ذخیره داشته باشید حتما
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/9006" target="_blank">📅 12:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9005">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smt8wAzjXAnJHOHWO56wXwu8ZevQS9WERfd3kGwas6_KFvZGaynlp9AH1LFOniMLDfhsHREmtge9ab5nV3EXG7KkfFNdRJ8IJkaxCBpxobybd8noRGRF6HJ8091p57glMnn6TPKP8lnah-pT6I27yMKvAyuYCNLSLuCoWL_w-_AzG2X9ArwM-90v6R5djKWXChOYYjCGcsUdApVJ18K5FQqLGbRXxO8ZyVaCeVyghyaSoz91nCjTHpK1rcumbTjX0vFwkJaIv4W3zffG_06HPW1mn_Je7imX2YNj9FqkUiKJuX7nz3sXcIA7vK0Y-iHEPAfzAxdfhUfkvinxYz3HGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون تهران
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/9005" target="_blank">📅 12:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9004">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKnjRwdRcA8d6gwMnDDS0nyMoSHTc8IePfpTdlSeRGg6LXsO8S9EeR1FB9cQCHPDJ_Gwy5Zoch9rbJc8amCtGy5I1pwrdGdr-VZ_HRDrJT5OJGnjLfZ0HP21xqKxqeJojJE-uzzqZW-7SxZTqihpwfBkmBA_hmZUGcfNVe2UCZozt2WinSyrFJIGjY6PztZ8bs7zTGwR88b6hU3axjXw1oCq5kfKNZEFj5E3FFN2FIzZIUyff_vqVkdxn3ZQ6r7_wtJCe8MXtIWJ_6KeQVIf-yWHvLOmqnrMBurQXXh8YIknBRsYsg219BK0yjrnVN4nSTVzeGH7rvhCnJE5ZR8X6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تهران، شمس آباد:
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/9004" target="_blank">📅 12:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9003">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
حمله اسرائیل به فرودگاه شیراز
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/9003" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9002">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
لشکر 8 زرهی اصفهان مورد حمله قرار گرفت
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/9002" target="_blank">📅 11:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9001">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
❗️
دانشگاه عاشورا هوافضای سپاه مورد هدف قرار گرفت.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/9001" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9000">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
❗️
وزیر جنگ اسرائیل: شروع کردیم.
Proxy
|
Proxy
|
Proxy
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/9000" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8999">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🆕
ایرنا : انفجار در استان همدان
پروکسی نت ملی:
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/IranProxyV2/8999" target="_blank">📅 11:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8998">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
تو اکثر نقاط تهران، پدافندا درگیرن.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/8998" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8997">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
تو اکثر نقاط تهران، پدافندا درگیرن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/IranProxyV2/8997" target="_blank">📅 11:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8996">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
بنا بر گزارشات دیتاسنتر آسیاتک قطع شده و به دیتاسنترها جهت قطعی اینترنت آماده‌باش دادند.
در صورت تبادل آتش بیشتر قطعی اینترنت بعید نیست.
اگر فایل یا اطلاعاتی به صورت آنلاین دارید بهتر است همین الان آن را دانلود کنید و تنظیمات حذف حساب‌های کاربری به حداکثر زمان تنظیم کنید. راهی برای وصل شدن خود حتماً داشته باشید.
چنل مارو حتما دنبال کنید، ما هر راهی که برای اتصال مجدد پیدا کنیم حتما حتما براتون قرار میدیم درسریعترین زمان ممکن
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/IranProxyV2/8996" target="_blank">📅 11:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8995">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری-صدای انفجار در اصفهان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8995" target="_blank">📅 11:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8994">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری-شنیده شدن صدای انفجار در اسلامشهر و ملارد و کهریزک و باقرشهر
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8994" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8993">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری-شنیده شدن صدای انفجار در غرب و جنوب تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/IranProxyV2/8993" target="_blank">📅 11:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8992">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G23v2YKfyeVRjtX1hMIk072PvLFjKFyIyadRoqU0MDfvvcpGbC4I0RlfnGLXNZ2zufzk-8xqKMjEg7IADgXWoMYBgRwKMt2soxaTATDETqM07XPWE8NJ8htGfkCxnnm_H-gJwq_nE6aoEnapPWztfoiUMiMr4GWlf09mr_AjjSLB7BhgLGlglduvc2nZ_2x6GrBydpNp_rc8AWW01T6eVo2kXsYkz5cj3ZR9dsYUsB6gKC9tHkcXHHEBOMcNSWG1wvwPFpH2-UcbXmVQU5tmMIjtCA-Nv-a1Rx1VedHtDZjRX4L-eYf-FBDtBr5VisxZwGTRJFk_3t20xL2Tb_ZYHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وضعیت آسمان اصفهان:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/8992" target="_blank">📅 11:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8990">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سپاه: حمله دشمن به صنایع پتروشیمی پاسخ داده شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8990" target="_blank">📅 11:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8989">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb9354396b.mp4?token=rajkyxDNLUQ7a8jRL_UVVoaQJsr9f11GSwhxnT3hPjMakFIm75k5WK2Vpt26vCPk6-EBSfJMvdvGeslvPFkZvwFHCEqWz42jEhODjkZnM6gvhkypVnKJxnT0AkPogFKCuTdqDSMPhU159jx21tBu07Zsj6e-5qrn5KizJln7OSkXMRBrc9wSVntnaX-cVYWDxLur3LMmWRNQkO7EDUfw_MwlY6oGxWhDILTR6_24ZNvrhfJ-wa1e7hMxBtdHm1WydNG6R7IED8W1VOMD5EkXXkY9PkIJw5dNuIKCEZEgmxdEmoyF5Fl82o12AegmV2-UUHUKdYIOGnSO_x-7eQUD9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb9354396b.mp4?token=rajkyxDNLUQ7a8jRL_UVVoaQJsr9f11GSwhxnT3hPjMakFIm75k5WK2Vpt26vCPk6-EBSfJMvdvGeslvPFkZvwFHCEqWz42jEhODjkZnM6gvhkypVnKJxnT0AkPogFKCuTdqDSMPhU159jx21tBu07Zsj6e-5qrn5KizJln7OSkXMRBrc9wSVntnaX-cVYWDxLur3LMmWRNQkO7EDUfw_MwlY6oGxWhDILTR6_24ZNvrhfJ-wa1e7hMxBtdHm1WydNG6R7IED8W1VOMD5EkXXkY9PkIJw5dNuIKCEZEgmxdEmoyF5Fl82o12AegmV2-UUHUKdYIOGnSO_x-7eQUD9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم‌های اضافی از موشک بالستیک ایرانی که در نزدیکی یک شهرک اسرائیلی در کرانه باختری اشغالی اصابت کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8989" target="_blank">📅 11:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8988">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88608e0e82.mp4?token=XWsy4xsTrI_IpvJ75HaE3XZ5fJi6WXXBa8U9xW_pr7Q8LLU_2q_bdh74y29xN8TK6gBn--SQ0s4ZOZOUvDrN0aADBsQoevIYJtToCBSirE4rJ6PPnfrbGqPOKKEG5b7Df7MVmXxL6BjKn25lB1RtpPzD0V4c3bYd4cIYKsr3Ef69fQALylA9BKsod0GSpQqBSBBmQeGEzlJPhHI0XNjOvF2_lKLFOstjQL7-eMoHvq4DzpQKVKbHtABtGwCApTT67cMh6vvOMPCqThn1uubutzjVv650esO4F9_OHzQfuJjJRr4NOM0z9PUDh1ginR51tM8qw4Abu-AX6xX2uq20ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88608e0e82.mp4?token=XWsy4xsTrI_IpvJ75HaE3XZ5fJi6WXXBa8U9xW_pr7Q8LLU_2q_bdh74y29xN8TK6gBn--SQ0s4ZOZOUvDrN0aADBsQoevIYJtToCBSirE4rJ6PPnfrbGqPOKKEG5b7Df7MVmXxL6BjKn25lB1RtpPzD0V4c3bYd4cIYKsr3Ef69fQALylA9BKsod0GSpQqBSBBmQeGEzlJPhHI0XNjOvF2_lKLFOstjQL7-eMoHvq4DzpQKVKbHtABtGwCApTT67cMh6vvOMPCqThn1uubutzjVv650esO4F9_OHzQfuJjJRr4NOM0z9PUDh1ginR51tM8qw4Abu-AX6xX2uq20ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از تأسیسات پتروشیمی هدف قرار گرفته در ماهشهر، جنوب ایران.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8988" target="_blank">📅 11:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8987">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
رسانه‌های اسرائیل:
پس از شلیک یک موج موشکی از ایران، صدای انفجار در منطقه مرکزی و تل آویو شنیده شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/IranProxyV2/8987" target="_blank">📅 10:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8986">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
اتحادیه اروپا: امروز تحریم‌هایی رو علیه جمهوری اسلامی به‌دلیل ایجاد اختلال در آزادی کشتیرانی اعمال خواهیم کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8986" target="_blank">📅 10:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8985">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
مدیرکل بحران آذربایجان شرقی:
در پی حمله ساعت ۵ صبح دوشنبه به یک مرکز نظامی در تبریز، هیچ‌گونه تلفات جانی گزارش نشده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8985" target="_blank">📅 10:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8984">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فعال شدن آژیرهای هشدار در اردن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8984" target="_blank">📅 10:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8983">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UihldFB6vZ6zqkryHqmoyUYLMWNCpEvv4_6J-eKzfScrr2l5qLC8m7HqlAULdDAggGPUDNtP_kVN67zT6DahfrX9eeSaXkYFoz96eTCWylvPw8zszofK7bYA9UnoGJiG3DJwQZJFDJxS-vGksEyivawmN14WVw3SfdWF54mM-qyRoDa8aUWo9QeMMplRHiu1Skj835qa_SE0V8lOxAFevRNhJ7n54FhL87OjICQokmgTNGmQYKt1R7A6qe_QPb6e5AhVc2nkMTku6pltGwFBX7WcRaG3mDzwnj4DvLZFs2rau8hb912oTCKkawslhLqeWYg5_idRV7kdmugB95ZB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت جالب ایلان ماسک: جالبه بدونین اسم تنگه هرمز از اهورامزدا، خدای آیین زرتشتی، گرفته شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/IranProxyV2/8983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8982">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
فوری؛ موج جدید حملات ایران به اسراییل هم‌اکنون
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/IranProxyV2/8982" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8981">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇾🇪
فوری؛ یمن تنگه باب المندب رو بست!!!!!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/8981" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8980">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇷
❤️
فوووووری؛ رادیو ارتش اسرائیل: تشکیلات امنیتی اسرائیل تخمین می‌زند که در آغاز یک رویارویی نظامی است که چندین روز ادامه خواهد داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/IranProxyV2/8980" target="_blank">📅 10:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8979">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
⭕️
🪖
به نقل از منابع عبری ارتش اسرائیل در حال حاضر در حال عملیات در خاک ایرانه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/IranProxyV2/8979" target="_blank">📅 10:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8978">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
سپاه : عملیات نصر شروع شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/IranProxyV2/8978" target="_blank">📅 09:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8977">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
انفجاررررر در کرمانشاه
گزارش منابع داخلی از فعالیت پدافند در کرمانشاه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/IranProxyV2/8977" target="_blank">📅 09:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8976">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
⚠️
سازمان منطقه ویژه پتروشیمی:  دستور خروج اضطراری کلیه کارکنان روزکار از این منطقه صادر شده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/IranProxyV2/8976" target="_blank">📅 09:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8975">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🆕
کانال ۱۲ اسرائیل: طی چندساعت اخیر به ۲۰ هدف تو ایران حمله کردیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/IranProxyV2/8975" target="_blank">📅 09:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8974">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
کانال ۱۴ درباره یک مسئول اسرائیلی:
تأکید می‌کنیم که یک تأسیسات پتروشیمی در ایران هدف قرار گرفته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/IranProxyV2/8974" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8973">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXe8uKbtaQQxm_lRXRsek2cLcBRCSa6LCxgv0MliAOBQT47-FPOWQNNxvHD1hW-loduJBwPQjY_PpuB4DwCMPypHbbvsXIjPPH9Ap0wzDUPesoYrJURLHtgWTC84hqbzpsUHi9LD61M3kokuXYDMXAcwQ1ViFcang9B2-EGaKlmfYsh1JxScE4dQEh3DGgw_m6et9297lKaLIbdSIWIXYsk6LSWbMDqF1j_QBBpRgSXVh8IKT9XagTyXom2KBbx8QPLhpHvsuvbyGllLOoo4-a8YXOGESCyhklwwdA6vzOzCTg-9098S3k8hFTGLAPsRWIoU9hWIXX9cmPz-7FIv0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور مورفی:
این جنگ برای آمریکا تحقیرآمیز بود؛
ترامپ دیشب گفت به نتانیاهو زنگ می‌زنم تا جلوی حمله تلافی‌جویانه‌ش رو بگیرم ولی اسرائیل ۲ ساعت بعد از این تماس جنگ رو از سر گرفت و ترامپ و آمریکا رو تحقیر کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/8973" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8972">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlY2lBv8BeWzfR43UfEBnrUA-Ebc0zLQyiV-tIgbID0Qcpkk1O8fgG52zKXt29Tzd2HrmsjNUy8hsqPTAM8zXY9VsTIwWX1D5wizFY5dmvJocqg_5SMJVz7FK-zGcoEBySJMfnQodYJgOMz3zTpuvX31JbaA8nqv5YWj8z8-ACi28qCL6KknRmZQ-f1Sj6MXhWh-VeLpj3kPKI4yWNIa46_taH8MB32KjHk2vKV0aNcfR23lJJQ9LzYnBRZrmJmqrlOE--pR93eoEYf3gcAwH86rLy3TRZNs52oiQyBqPy4R1QZ0CoHV-WYiJsbPe-DmEOpdvt7nTLBJTvjn482OPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم
:
سپاه موشک خیبر شکن و یک پهباد ناشناخته امروز استفاده کرده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8972" target="_blank">📅 08:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8968">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺⁴.ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8968" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ های جدید اختصاصی OpenVPN
با حجم و اعتبار نامحدود
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
بدون نیاز به یوزر پسورد
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8968" target="_blank">📅 08:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8967">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📶
این پروکسی های تلگرام رو داشته باشید متصلن:
https://t.me/proxy?server=www.alp-drtop.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b
https://t.me/proxy?server=167.233.66.2&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=188.245.196.78&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=87.248.129.107&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=178.105.225.211&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=91.107.246.35&port=443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=secure.bits-lab.info&port=443&secret=ee1603010200010001fc030386e24c3ad37765622e79656b74616e65742e636f6d
❗️
با اکثر اینترنت ها تست شده
پیشنهاد میشه کمی برای اتصال صبور باشید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8967" target="_blank">📅 08:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8966">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKzDGH303HhbqxfLHcI8U7sx2nWBK6lvAwFvxcYVKYjJVOEu68fRIatehKgUBHLkrFBRUD4SEDIyRcwQAjGzSw38_HdZiPkJPID9qCocdQF2rUFsq3QDjDgBOrsnZ7u179fJGqxpS-L4m0nmDoKS6d8im6dTZqF3N0vyk3AG6vxFOzGqQ_mRtAfsrAHMySCNGZV4WbKaCr6oJfaqbR9airx2WDPhMPqu-i4f7r-cIW9DgHPlBB2criWBSQdOD-94_aeMYIR2XDwz_UXfUaatPZ6A6zC23zWS72J4-UAn5WAArcj0L_mp3n6HgU8P1Go_3m2XyoNpbHrPtK2Gm1je1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه وزارت دفاع عربستان:
دارن بهمون حملات موشکی و پهپادی انجام میدن، دستم کم دو انفجار نزدیک شهر ریاض گزارش شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/IranProxyV2/8966" target="_blank">📅 08:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8965">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رادیو ارتش اسرائیل
موج جدیدی از حملات رو شناسایی کردیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/IranProxyV2/8965" target="_blank">📅 08:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8964">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
اصابت چند پرتابه به پتروشیمی کارون ماهشهر تایید شده و بخشی از پتروشیمی در جریان این حملات اسیب دیده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/IranProxyV2/8964" target="_blank">📅 08:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8963">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc73ebd9af.mp4?token=c2Yjrgb4JN0jFkD4RO5XAQnMV8EqRpfnDboPlvDNVkHJMAo7JFLzEAXfBC8tC0qtIvFiDyr5LeK9X_zCnOh4ayevNtjlnAkXLlFuHrWoZHj8bwNCux0GB8hbVqJ-zW704BWN9ZzGv3xXTIvXtKmz3icDnAdVKOSTytA50dg0RqM6Kb8zPXi3yC6ltoXhrSRHrd1y7-OGNui-rbqOmARe2cRGOGI_ylGb2LO1oL9fu5EVK1wuv4ulsVVXyTzyUbWsEOWbOPaH3sIKaN4aBSBijt-DpSOIcQq3tdUQ3i381anzlIj_THYEfp3EggUPqSAs4fHYqkd7PmfljGPwp4USEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc73ebd9af.mp4?token=c2Yjrgb4JN0jFkD4RO5XAQnMV8EqRpfnDboPlvDNVkHJMAo7JFLzEAXfBC8tC0qtIvFiDyr5LeK9X_zCnOh4ayevNtjlnAkXLlFuHrWoZHj8bwNCux0GB8hbVqJ-zW704BWN9ZzGv3xXTIvXtKmz3icDnAdVKOSTytA50dg0RqM6Kb8zPXi3yC6ltoXhrSRHrd1y7-OGNui-rbqOmARe2cRGOGI_ylGb2LO1oL9fu5EVK1wuv4ulsVVXyTzyUbWsEOWbOPaH3sIKaN4aBSBijt-DpSOIcQq3tdUQ3i381anzlIj_THYEfp3EggUPqSAs4fHYqkd7PmfljGPwp4USEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از موشک‌های ایرانی به یک مرکز نظامی اسرائیلی در نزدیکی نابلس اصابت کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8963" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8962">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQQoh1UK_nDemHNsjfdNQjDBLgRgtKPc8GrcSf_Wh5NtJWDV0R08Dla8K1ZjqnMyYIh-FgxQy2wxunU9HHVa6JKnYV5LVQ8Mnto2BpWGFkaYi2P2AZMqlcBG4GGgQQEgHAoj1rzSPNbhFAYi2IHtBDiNh8JRnlh6stewuveaYZecchWUI_4GLQHQ7e77Zmf6ftWb116LsKRmndabu16oUK0N1ygXchVmmjnSvddAc-PBhWwpgd5COCuSFGwa_rtoaDH8Gr_OQ5fmTrmHou6eho6dB5geWqjLZygPmsNv90wKCKnd9tAirMKvJYsd4YNBicuIWVS4ljgAHrStKF0hZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار اسرائیل:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/IranProxyV2/8962" target="_blank">📅 08:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8961">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
مثه اینکه موج جدیدی از حملات ایران شروع شده
از اصفهان ، ارومیه ، خرم آباد ، کرمانشاه ، ماهشهر و آبادان موشک پرتاب شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/IranProxyV2/8961" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8960">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8YmmaLRfb0AXViZUoK2tg-KVZWIsBhlN3lzDAcpVTAR_xR28yWNONLHFYEu0dbXSk-fmDNC5bwhRuEP0p-t2Xl3Z0qZlT5K6ACY99Tfwst65Oe7iDQ1vLSI1K9MGAXG-4-01c2Fk-sdyWDQkxrL2K7kyLJIKxJuWJES7zoXmtcodnnF7IsF6xgWP8pT5Pz9wH_ek0Lf2dtvf4aTMLVzm0F1--zU-fdJ3hgvDyssAidFr8yDEGLhz0BR6b108d_AYbJvyllZK7TbAI2d5Pu_YU0Upm4t2CaFI_lcFpsF0PlEaIi_8aYGCOOj_f6DTXjybGLIiqzH1VfawJVn7FMAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در پی به صدا آمدن آژیر خطر در اسرائیل، مقامات این کشور گفتند که یک موشک شلیک شده از یمن را به طور موفق رهگیری کردیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/IranProxyV2/8960" target="_blank">📅 08:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8959">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇸🇦
شنیده شدن انفجار در پایگاه شاهزاده سلطان، الخرج عربستان  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/IranProxyV2/8959" target="_blank">📅 08:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8958">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇸🇦
شنیده شدن انفجار در پایگاه شاهزاده سلطان، الخرج عربستان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/IranProxyV2/8958" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8957">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot  جهت ثبت سفارش به ربات مراجعه…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8957" target="_blank">📅 08:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8956">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
کاخ سفید:
این تنش های بین ایران و اسرائیل هیچ ربطی ما ندارند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8956" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8955">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شبکه «آی ۲۴نیوز» اسرائیل گزارش داد بر اساس گزارش‌های اولیه، اسرائیل تاکنون دست‌کم ۱۵ هدف را در نقاط مختلف ایران هدف قرار داده است. به گفته این شبکه، از جمله اهداف مورد حمله یک مرکز تولید پهپاد، فرودگاه بین‌المللی تهران و تاسیسات راهبردی نفتی بوده‌اند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8955" target="_blank">📅 08:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8954">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هرچی دارین سیو کنید احتمال داره باز قطع کنن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8954" target="_blank">📅 07:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8953">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏
🔴
وقوع دست‌کم سه انفجار در اصفهان  گزارش میشود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8953" target="_blank">📅 05:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8952">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
سپاه اعلام کرد به ایران حمله موشکی شده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8952" target="_blank">📅 05:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8951">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsiB_dHBT9f3EMBXCc8nRPlxJAl9Zog0KrtQzkAchYDKGh5CG5jsTJwNHGq7koj_YHf2DTYUQkaYQWkzl_pIlgHGf8EhWZYbjbAocLHroNPTdE1Lhi2Xs8Jj-ArFlRiQi4D0PE5L8yhDb5rw-4Pm_sLr3W88IqIejUIho6660X7iizbmg5isDlNE_Y9SqNRXk7EuTmAldSgLDM3x5g9bZH038ef5PuqZRqYB5SxFUhjNwx7uvROEoEal2_ETV-G3OxdK1Gz6EsEQMcsZwHh9dDiyH-GC6_2BY9u59DiLrSh6MxhvrSiAx6YCCGCzKvSizham9R5k162bRgX7Tk9TMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری-خبرهایی از انفجار در پایگاه موشکی اصفهان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8951" target="_blank">📅 05:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8950">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏
🔴
فوری
-
الجزیره: رسانه‌های اسرائیلی گزارش دادند حملات هوایی اخیر فرودگاه مهرآباد تهران و همچنین یک انبار نگهداری پهپادهای انتحاری را هدف قرار داده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8950" target="_blank">📅 05:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8949">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
تا کنون تعداد اهدافی که اسرائیل به آن‌ها حمله کرده 15 هدف بوده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/8949" target="_blank">📅 05:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8948">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
حملاتی محدود به چند سایت پدافندی و نظامی تو تهران، کرمانشاه، اصفهان، ارومیه، کرج و تبریز و چند نقطه دیگه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8948" target="_blank">📅 05:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8947">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری-کانال ۱۲ اسرائیل اعلام کرد که فرودگاه مهرآباد تهران مورد حمله قرار گرفته است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8947" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8946">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYo-u8VthET_I_Al5pwn1jx5tzoG3iDFvRqkezf5NxmpHqBdRpaOqbTl-_YwbW7ETdynbPq6c43z0mHvlqr6X0gdGqWhFhIPCeOac03TkkRgV8hT1WaFpqJR-w8TXrWzpsT9CYVEwhhjn0cUpFEVkUaHcbAZqcRstvXgnP1KHGIk2csC_W7-YeiR7dt1w4KUye3L-p0ZBp00nb4kwFVDj6p3OD0hUd21HDjs3G20BVUmdrb4zNBgrFE86ORyYV6Z5dyQuDbDnjzzcl-oEBMBuDXgNMlFUtO33YotwpgmTcneypf9ryqYCnwm99pQLVTxkJJKYbUCSWW9D-y_WpGIjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
حمله اسراییل به غرب ایران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8946" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8945">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
آغاز حملات سپاه پاسداران به مواضع اسرائیل به گفته برخی خبرگزاری های محلی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8945" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8944">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmGfRD8RdcOERJGeLm92dV6lii4yBlS3Qy4oZA-lLiCKGnq4oCw200QoqiZN75MbZjpK9-mQxonxo3_711-tEboiN_NZxBpZfao3VBYwtcU8f6p8e0d5Ac0ipExJ-KQ85ex8x0rY5uQsenFUPf5BDhKK9_9N9bvWxI3SjQzrmaCTEeslrMqiwERIjbZaVYnlG4ier4jSdng611W0Godrmqm71XPr1q1i-BPmYpf7zv7OOFuS0DAYqrSZTTfEliZdLO6lCY1ymH0BknouCeWJCu_ZZh5lh18PfxzuQ01TPoOOkIinZ7dW_J8ineFa4xVd17HMcf0YOCDlDYiLJU8Nqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به کرمانشاه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8944" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8943">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
کانال 14 اسرائیل:
نیروی هوایی اسراییل با استفاده از موشک های بالستیک هواپایه و موشک های کروز، از طرف دریای مدیترانه به ایران حمله کرده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/IranProxyV2/8943" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8942">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHOl0RE7Gtxv80excntaVAyqSx1ga2YRhqoOksBhVF2pYTdR47Nijrna3AaH4Toad1S2C45N1OBJJXQKuqDmfOXwItQ0ItmYBXzbYuHv7UC2GlQY0cAfh4LUPV27U9djw6MK3uCPdyjmAWT8e6SHEQ0Arr1131aifTRnH3vEFsAcBBRFpTcoL7Noi9LgQxAGHY2lZ4zIT44olEn-G_0WlDR4Qkj1ifgCjRPSDm_sh-eM9JtK5cl5yXjf4y0w0TfoByqtGCVUPeBATl3Wl87Fc5JjaRihaxJ0bc4qiActKPHrKVWJPuSnDsc6Oo3p1vSxX0yCfHY1kRnGxY8UmDmdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کرمانشاه رو هم زدن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8942" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8941">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOJEhBDVVPueB_1XeYZZvrwuWH_mBerfNLGHkuJzSUQwi-JZRZjk76a_dtM8aU3UxSxmj0-Z4zPj3NnPs96FAPNvmd-rGzddeiEbSxVUooiQkYcbC_niJtPaYivcLbuE6ccZ-RF-bZyBl2el2S1yraDoJzXcHZ9IKiyWNQee3EHzJWokjmdqZwdOi21fQFgKIpzsF6dQYtT-KYkLWOItC3y2P5H2VOJXXKzG43E5nm6wmQ4F8lsOfB-oKCalGfLatjpWWPM3iFpTXnUcnV8sX93j2_KFGdo3STO3lawdJRphVI0C3CBH_TKKgrLnyhH_7fpABKnUKLI7uQgVPa-vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه رسمی ارتش اسرائیل: «دقایقی پیش، نیروی هوایی اسرائیل اهداف نظامی متعلق به رژیم ایران را در مناطق مرکزی و غربی ایران هدف حمله قرار داد.»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/IranProxyV2/8941" target="_blank">📅 05:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8940">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuY5Gu8XLAaqNIAsbtc8uP6b7LyafBf1CHhOnY9rJ09MYdB-2G5N1qcNzPfZ9mjIJkPbN0igIKlL_sSFp-EscR1_xsxSj4fFT_V0xiCLL7vdCd7ajYmmfteLCArBEwtDekEh_3Ee1hPGr-cdqRn-TESkyhYqweeXf4C4dwZ5N0JGLOsfmu5q3a-Jd-t2ej5wPfvGM4hl3uKOfosTZxfy2W5LQS3LDakwp1CDWnDU5UiqMb-aJ2OFBpC_du4LQv33Nc0DsJTIMkG_1m01-6OoQJr4saLgqeKsXl3KIhlHStk5blQ_BL8DyMxZxmWEHo-pZV8_lH8K8T_EuUjatRaOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صدا و سیما حمله رو تایید کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/IranProxyV2/8940" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8939">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCd3lt6PYB60eoxNPaQaR2woYmOLfSuGFmDz3A7wyKw_bkcNVG0ThCZwZOot8IElW54Pm6I0gHogJjewH4dDUcGnhpCmxkC79z6xMiBtAjko2ux-gOYPxRDHleKu0ef4Kb3vWoV38uTzxWc7Bdxh6HW-1m1RMmi8NuDysK2HAbPqpxh9ZkrUI3TcbyEVqmkCzy36wU4u8J2z5cq_QGggtFgrLJp_5btsMTTI8ADr43XhvyYQ1kznRbepUAZ46reiEtyeT4b3yoaVB4ZqeIwxsp55xw39KsilAWjnkeyYvr9N78NzNM5p75lS88YkeF4rsWB3AYV7z779Va-7PYIzCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار تو تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/IranProxyV2/8939" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8938">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
انفجار در ارومیه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/IranProxyV2/8938" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8937">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8c9Xh3HsDk7027ACUb3U8vocJtb2rGb32k5E-7618Kk0a87BFA7FZYUJVY3haJYyPTh2v1jzygm1ldLASd-FD9iw7YAKcEUO2e0RpTOeHLSIK3hv5NBQAlc_kzKWf7H9nYWWyFGie_GJVJTrQakl54XRz03np-QIlVJG7CC7ckh0eJD11dyF2NQWxWWypleV2nVWxeJW6xrjicKrSZeux3Jt2k6_8mAXIJ_im65qpA7EdnCg1WDIIi8ixkwyG19qCasH2pnn8KhpXFrxXBXPZN0f-bEECy9BvncIMnt-VuTMtVW70ANp5gabFdZNxDF85TaZkC61yhtFYI4hZKDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شاهین شهر اصفهان،ساعاتی پیش
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/8937" target="_blank">📅 04:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8936">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
کانال ۱۴ اسراییل:
جنگنده ها دارن وارد آسمون ایران میشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/IranProxyV2/8936" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8935">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIcxUqueOMdImC9Q_mnIoOYZiKnRlw6x1s2b92osZ42wDoflshxUDpsJIwGKBPsVemQQUdTCvQmOWz5DUq2gEUBzdZdP8c9oTKtlO6RMFOrAlQTjpDUD_FPtfFLqEYsN6u3dmbYe2NVrQVTeXbMaKQcOuSNkXlqvRx50l6aU6Kb3mCKZw27XqlT6kj2oJRmU46A1B50884cpNrTc1rXzL-kIF-IIP6cDRUbh4sc5F1t8OysLMt4wSKGk6eqxArh0kuwOTCyXtnQfWVBmd4ipyZOTZurJ_YqHK2i4llDz1sUnKU_wd7WQKHhb6I_dPuPExOlXdTd-icUcXo2KxmPing.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یا خدا اصفهان رو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8935" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8934">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnoE9Ei8Lcj8UxGFrahxaGEIbkisUEEzbsfrzrF4krv8hPz-rW7sUmNuVOE7wYXicRxzQdVPmGt1vrjCRM8vjEBGoGYb7Kk_Uk9d0LUW-9hW5mMJ-q_L5XRMzPiHAhO8fy_QJg7ZBr3HWYvddiMhAoqIBTBy37rUN7A_zu6CeklQ_a3TKy8wqEwA1Dw9bXKUxjVuitdr0QQ7DvKdKISkJzUzoNteZr8gyp-qMpa-3F_H7gVoQ3l0AVm5DRajbiMoeI7_zqogvQw4Bb05PwICZxv42lgj1CDjq7W3JqbxxndB0zNZ-VjVULgtHkAEm3VmW7M-yv8GyS11TO0c9_fU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نجف آباد اصفهان هم اکنون
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/IranProxyV2/8934" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8933">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پدافندا راحت بخوابید مردم بیدارن
😂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/8933" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8932">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💥
شهر هایی که انفجار گزارش شده
تهران
تبریز
اصفهان
نجف آباد
شاهین شهر
کرج
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/IranProxyV2/8932" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8931">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
همزمان تهران و هم زدننننن تبریز و زدنننننن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8931" target="_blank">📅 04:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8930">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
اصفهان و زدنننننن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8930" target="_blank">📅 04:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8929">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏
🔴
فوری-سفارت آمریکا در اردن با صدور هشدار امنیتی اعلام کرد گزارش‌هایی از ورود موشک‌ها، پهپادها یا راکت‌ها به حریم هوایی اردن منتشر شده و از شهروندان خواست فوراً در پناهگاه‌ها مستقر شده و تا اطلاع بعدی در محل امن باقی بمانند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8929" target="_blank">📅 04:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8928">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تنها حمایتی که میتونید انجام بدین اینه که ری اکشن بزنید و فور کنید برای دوستاتون پست هارو عضو چنل بشن، ری اکشن قلب بزنید رو این پست ببینم چندنفرید
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8928" target="_blank">📅 02:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8927">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">+1 ترابایت دیگه برای شما دوستان فور کنید برای رفقاتون
🎁
❤️
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@deadvix.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%A9%F0%9F%87%A%20%D8%A2%D9%84%D9%85%D8%A7%D9%86
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@dep2g1.aswall.ir:43582?encryption=none&security=reality&type=tcp&headerType=none&flow=xtls-rprx-vision&sni=play.google.com&fp=chrome&pbk=95vLe0hBBerV1ch9WxJ9iPTi4u7V9NExNADg9-LpcwY&sid=025086f1385a838a#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@dep2g2.aswall.ir:11000?encryption=none&security=reality&type=tcp&headerType=none&sni=refersion.com&fp=chrome&pbk=YWfCdTnr4FAOMYTY2dLrMtQUokyxOGpPhYEEszPj20E#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8927" target="_blank">📅 02:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8925">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">1 ترابایت برای شما دوستان
❤️
🎁
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@VIP-Vanguard.userid:500?encryption=none&security=reality&type=tcp&headerType=none&sni=www.chess.com&fp=chrome&pbk=OfqZPHXqiwjyZEhZtVO1kk9PLxW2ueKdaOjVX_Br2Ek&sid=ce7d30ff97b02e63#%E2%98%98%EF%B8%8F%20980.71%20GB%20%7C%2030%20Days%20Left
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@50.7.5.85:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=dehone.tunnelltwo.ir&sni=dehone.tunnelltwo.ir&fp=chrome#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@50.7.5.85:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=deadvi.tunnelltwo.ir&sni=deadvi.tunnelltwo.ir&fp=chrome#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@94.140.0.0:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=nlox.nextigo.app&sni=nlox.nextigo.app&fp=chrome#%F0%9F%87%B3%F0%9F%87%B1%20%D9%87%D9%84%D9%86%D8%AF%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@94.140.0.0:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=usaop.nextigo.app&sni=usaop.nextigo.app&fp=chrome#%F0%9F%87%BA%F0%9F%87%B8%20%D8%A2%D9%85%D8%B1%DB%8C%DA%A9%D8%A7%20%E2%98%81%EF%B8%8F%20
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@45.130.125.60:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=decdnmtn.gozarino.com&sni=decdnmtn.gozarino.com&fp=chrome#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%A8%B3%20%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%D8%B3%D9%84%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@188.114.97.6:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=decdnmtn.gozarino.com&sni=decdnmtn.gozarino.com&fp=chrome#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%A8%B3%20%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%D8%B3%D9%84%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@deluxi.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%A8%B3%20%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%D8%B3%D9%84
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@devops.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%A8%B3%20%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%D8%B3%D9%84
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@usaoxp.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%BA%F0%9F%87%B8%20%D8%A2%D9%85%D8%B1%DB%8C%DA%A9%D8%A7
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@nloxv.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%B3%F0%9F%87%B1%20%D9%87%D9%84%D9%86%D8%AF
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8925" target="_blank">📅 01:58 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
