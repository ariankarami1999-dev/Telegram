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
<img src="https://cdn4.telesco.pe/file/bpf-9HqA-ahH0zBxFS_BKY3lVoFjpBNifcmsaU64Quqj_PfgfdSFbNSPtdJkfMemxx3ma-beubfXvtutG0WKNj32wIUzrjYe1F-AtnYLb2Rjuy0nZksuXn7Ite76rvEC_u9zYAXy7UkN2_3_6YdxJ5MhHN6-DBIHJLrx_T8e-7TiyykvuCV4WVOavEwI1fKRN83QNxIP3goJ3EhKZSxc1BiR82mUrMOYKOmvL07SywQvngfm0CXkJKKMbwojVihf-8EwJHSCZ1ZSy_0voba31PSGpfpBDzaU52hIZeYrCYAMiElwG7BkLGeloDvIT_jUJ4b0iszuBiWpxxbXSxY_jQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.9K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-9033">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/IranProxyV2/9033" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9032">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=178.105.226.182&port=443&secret=ee396219a1e9b2aebf6f245a1495777811706c61792e676f6f676c652e636f6d
https://t.me/proxy?server=orbit.proxyonline.online&port=443&secret=eea49899bfb9f5b061d6213e6f6480ea006f726269742e70726f78796f6e6c696e652e6f6e6c696e65
https://t.me/proxy?server=94.183.221.165&port=443&secret=a252e3eb41417da5e2332193f25bcf34
https://t.me/proxy?server=relay.proxyb.site&port=443&secret=eeee9dfed6b3721e5b2788f5100af2ff4272656c61792e70726f7879622e73697465
https://t.me/proxy?server=5.75.200.229&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/9032" target="_blank">📅 15:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9031">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
مث اینکه جنگ فعلا به پایان رسیده، هردرطرف از موضع خود کوتاه اومدن ولی البته یه نکته بهتون عرض کنم که این شرایط فقط تا پایان جام جهانی فک میکنم آتش بس برقرار باشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/IranProxyV2/9031" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9030">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:   نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/9030" target="_blank">📅 14:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9029">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/9029" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9027">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=fresh.nolags.pw&port=443&secret=dd691fa48fcc661b68fe4f5200c5b174f9
https://t.me/proxy?server=91.217.166.212&port=16&secret=dd1603010200010001fc030386e24c3add
https://t.me/proxy?server=fool.feel-fly.info&port=25565&secret=7hYDAQIAAQAB_AMDhuJMOt1iaXNjb3R0aS55ZWt0YW5ldC5jb20
https://t.me/proxy?server=91.217.166.22&port=20&secret=dd1603010200010001fc030386e24c3add
https://t.me/proxy?server=91.217.166.21&port=20&secret=dd1603010200010001fc030386e24c3add
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/9027" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9026">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/9026" target="_blank">📅 13:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9025">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/9025" target="_blank">📅 13:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9024">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/IranProxyV2/9024" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9023">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=s3.mowork.twc1.net&port=443&secret=ee90872f20ccc37e3aa2681602f51df71273332e6d6f776f726b2e747763312e6e6574
https://t.me/proxy?server=s4.mowork.twc1.net&port=443&secret=ee3e9cfe9af4494731b9a566075ee8c3bc73342e6d6f776f726b2e747763312e6e6574
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/IranProxyV2/9023" target="_blank">📅 13:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9022">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
vless://a78bf929-6883-48af-902d-7737793eeb17@hu02.sonicsonic.icu:443?security=reality&encryption=none&pbk=z-TKWOWgZLfzQ-wNdwXQqVwaUgCmbchM2Xtrk1NGynU&headerType=none&fp=qq&spx=%2F&type=tcp&flow=xtls-rprx-vision&sni=hu02.sonicsonic.icu#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/IranProxyV2/9022" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9020">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پروکسی مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=imtproxy.ir.imtproxy-ir.info..&port=443&secret=ee16550001232d00bb5190728b72644171706c61792e676f6f676c652e636f6d
https://t.me/proxy?server=65.108.154.5&port=443&secret=eecdf95381f978fb348f233a14b2251e6d7777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=91.107.148.135&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=5.75.206.125&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=91.107.167.170&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/9020" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9019">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پروکسی مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=91.107.156.186&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=153.80.241.214&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=51.254.130.47&port=8443&secret=a84102e409230c3b69dd4f68cef86baf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/IranProxyV2/9019" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9017">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
براتون پروکسی نت ملی و اوپن و... میزارم، حتما ذخیره کنید و برای دوستاتون بفرستید درصورت قطعی اینترنت استفاده کنید تا بتونید، حداقل کانکشن رو به تلگرام داشته باشین
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/IranProxyV2/9017" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9016">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری-آکسیوس به نقل از رادیو ارتش اسرائیل اعلام کرد که ارتش خود را برای چندین روز درگیری در ایران و احتمال بازگشت به یک نبرد طولانی‌مدت آماده می‌کند.
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/9016" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9015">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/9015" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9014">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
فوری/نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد  بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
✅
با ما اخبار جنگی بروز باشید  @russiamilitery</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/9014" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9013">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/IranProxyV2/9013" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9010">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/IranProxyV2/9010" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9009">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
لشکر10 سیدالشهداء سپاه کرج مورد حمله اسرائیل قرار گرفت
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/9009" target="_blank">📅 12:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9008">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/9008" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9007">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
مهر: شنیده شدن صدای انفجار در جنوب تهران
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/9007" target="_blank">📅 12:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9006">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
رفقا جنگ جنگه مراقب باشید از یک سری مراکز نظامی فاصله بگیرید ،امیدوارم تموم بشه این جنگ و همه مردم ایران سلامت باشن
❤️
💎
پروکسیارو ذخیره داشته باشید حتما
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/9006" target="_blank">📅 12:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9005">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGZ2Pb3GOq2Y7q54Eto-OcAI7Q4_k3WGHsCzhFLAMdrCeCoONxWd2W05yWyE_X__isyA_ktS9s_7EYZJ9O36w-2OjH1rILo7vQSWKMElz6_MAq3-j_0IG5g2i9v_SfRv0h3XfCuxBZXouJUsi1yNNlTH23lA08IH4RBt_38ESGyR1sxEUClz4yrhs9N_2T2cr01lI7Is6TgxSve9jo4IX90q7NTL7RwzkNhi4qZcbMkPd-PYJOITotw1cnrw0o2oiI6GeBhEftaq2li4ThaklziMjUEa03GUn9lxV0_R7Cz_zZXcwobdWo3x3leEyIiT3VYyZkOXj5C-twiYHQrBlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون تهران
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/9005" target="_blank">📅 12:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9004">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_3LxcljAbxZJ3j_DuDL9xAQQmfbGy5G0VnB2RS-zQjaMBHwVy3Hnz7nSabxO8reDiTS-4Siv_FxhHTbB7_mwoeZVvOWZOaQ076C6RYym0iNwaJ6DltLiIzh5GOJLeJaVQ2_lVRum0Sc0vscopGS7c_hljPQKJE80O0uxGhTpXHZ961VlB57lwelqvdFKRNSykzjWxwLkc7ARWWwsM9rqc2x-7dTFRFbK1ddpKRsWdtwoow3Se7hKNWG1Kn8CcveyhMFVv3pI5PfWLUrrbKnmeIGEUJX8aMGdPuRVhmui4BQrszOlcKXRZd0qYNiUKV5Ml9P98-iV98_5VRyxg9iSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تهران، شمس آباد:
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/9004" target="_blank">📅 12:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9003">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
حمله اسرائیل به فرودگاه شیراز
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/9003" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9002">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
لشکر 8 زرهی اصفهان مورد حمله قرار گرفت
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/9002" target="_blank">📅 11:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9001">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/9001" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9000">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/9000" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8999">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8999" target="_blank">📅 11:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8998">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
تو اکثر نقاط تهران، پدافندا درگیرن.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8998" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8997">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
تو اکثر نقاط تهران، پدافندا درگیرن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8997" target="_blank">📅 11:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8996">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
بنا بر گزارشات دیتاسنتر آسیاتک قطع شده و به دیتاسنترها جهت قطعی اینترنت آماده‌باش دادند.
در صورت تبادل آتش بیشتر قطعی اینترنت بعید نیست.
اگر فایل یا اطلاعاتی به صورت آنلاین دارید بهتر است همین الان آن را دانلود کنید و تنظیمات حذف حساب‌های کاربری به حداکثر زمان تنظیم کنید. راهی برای وصل شدن خود حتماً داشته باشید.
چنل مارو حتما دنبال کنید، ما هر راهی که برای اتصال مجدد پیدا کنیم حتما حتما براتون قرار میدیم درسریعترین زمان ممکن
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/8996" target="_blank">📅 11:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8995">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری-صدای انفجار در اصفهان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/IranProxyV2/8995" target="_blank">📅 11:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8994">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری-شنیده شدن صدای انفجار در اسلامشهر و ملارد و کهریزک و باقرشهر
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8994" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8993">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری-شنیده شدن صدای انفجار در غرب و جنوب تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/IranProxyV2/8993" target="_blank">📅 11:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8992">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnM2NQMlX9CqrYhbM5Z15KCQeiqyWcjdORZwgw3-KO9PVnc_MBWVzzho5KmR7iK63CIqmdcJrLyZUZxImJ3pFFn9Gu7Pr7wBb59Znc933LQPrYD06aWE3qKdlSjJMBfrJYvl4W5gMGOzR18K6UyuBnjmtpy8y_QOvsvnpzMS2GhR7m3Yn74LfA_1dfPhQbyZlXuVr2ej_u2pBGN2rnfqRQtGnCo6Zbb86kC-2uMIbA3HufWFe2IQxTt84J0XiltGXKrraCBq5sWbSM5I-7hxhNXVnYpfwc67_RsfLiIqxWgv_fYKZxTz_UUbwrLcMeZcgGxi9L4MgwUZn7kdHHZP4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وضعیت آسمان اصفهان:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/8992" target="_blank">📅 11:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8990">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سپاه: حمله دشمن به صنایع پتروشیمی پاسخ داده شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/IranProxyV2/8990" target="_blank">📅 11:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8989">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb9354396b.mp4?token=BR5TKwgAHUlr0RxqnqevNglYBPn0ZOyu6iQXYc2qCiCAD1nLbRDuNlPrut8f7Vd1ff3IyVjn8Gxk_4BiJOiFcPPVhyxOfruIHbShuv0OXUHRY75-Gg5pdeThP-JTGLDG0IpzC81KjDv4EmZk0J6u1WedNRIO2uNGce9f219OPeMQ2roV0an3nZjchAwX90WYrOVDGt1zNw_OG9BtE8ZFxg8JM1DfZjBKxbJvkmnXnYYXWQOgvzxIN-43aF5WTa4Q6I01NWrYWTDmi4lORRClU4zhwXah_qxp1fr_eBbQBEL43wMVsYjA8SDMwMCu64-sqf0iHtCljBDYSRGd4-alrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb9354396b.mp4?token=BR5TKwgAHUlr0RxqnqevNglYBPn0ZOyu6iQXYc2qCiCAD1nLbRDuNlPrut8f7Vd1ff3IyVjn8Gxk_4BiJOiFcPPVhyxOfruIHbShuv0OXUHRY75-Gg5pdeThP-JTGLDG0IpzC81KjDv4EmZk0J6u1WedNRIO2uNGce9f219OPeMQ2roV0an3nZjchAwX90WYrOVDGt1zNw_OG9BtE8ZFxg8JM1DfZjBKxbJvkmnXnYYXWQOgvzxIN-43aF5WTa4Q6I01NWrYWTDmi4lORRClU4zhwXah_qxp1fr_eBbQBEL43wMVsYjA8SDMwMCu64-sqf0iHtCljBDYSRGd4-alrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم‌های اضافی از موشک بالستیک ایرانی که در نزدیکی یک شهرک اسرائیلی در کرانه باختری اشغالی اصابت کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8989" target="_blank">📅 11:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8988">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88608e0e82.mp4?token=svIBsz3iM32kpvuctgRHrH7Ik0doz7opbjsdJA1RyFrIr_s6UhijNULTHAI3LL1K5pIaweuzYhYg6WJn3AKt_jBUEEDrlbQO_ekKDagQiZwieCw_jSUxB5wFq3b0I18vIC_7thgiq2Mawwdvt_5ZrvEwvNHGeNnZf5EbMNnyLSaF6K9K75-QjbIDNZgwQnyl_YbTcdLH2WqmA6eEGwo3UZcUeYyCQXdkJuvNNa20Ntfg77WQfAyivwYJ2Ejv2Tcc3OcHtsUvooaFfGQw0NJsGKd8eTaTslU-ukmHJZAPvf01AutE72cqXGUmg46hVhWC_Pg8s3CBaE-mizz0NlndKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88608e0e82.mp4?token=svIBsz3iM32kpvuctgRHrH7Ik0doz7opbjsdJA1RyFrIr_s6UhijNULTHAI3LL1K5pIaweuzYhYg6WJn3AKt_jBUEEDrlbQO_ekKDagQiZwieCw_jSUxB5wFq3b0I18vIC_7thgiq2Mawwdvt_5ZrvEwvNHGeNnZf5EbMNnyLSaF6K9K75-QjbIDNZgwQnyl_YbTcdLH2WqmA6eEGwo3UZcUeYyCQXdkJuvNNa20Ntfg77WQfAyivwYJ2Ejv2Tcc3OcHtsUvooaFfGQw0NJsGKd8eTaTslU-ukmHJZAPvf01AutE72cqXGUmg46hVhWC_Pg8s3CBaE-mizz0NlndKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از تأسیسات پتروشیمی هدف قرار گرفته در ماهشهر، جنوب ایران.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8988" target="_blank">📅 11:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
رسانه‌های اسرائیل:
پس از شلیک یک موج موشکی از ایران، صدای انفجار در منطقه مرکزی و تل آویو شنیده شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8987" target="_blank">📅 10:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
اتحادیه اروپا: امروز تحریم‌هایی رو علیه جمهوری اسلامی به‌دلیل ایجاد اختلال در آزادی کشتیرانی اعمال خواهیم کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8986" target="_blank">📅 10:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8985">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
مدیرکل بحران آذربایجان شرقی:
در پی حمله ساعت ۵ صبح دوشنبه به یک مرکز نظامی در تبریز، هیچ‌گونه تلفات جانی گزارش نشده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/8985" target="_blank">📅 10:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8984">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فعال شدن آژیرهای هشدار در اردن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8984" target="_blank">📅 10:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8983">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uu-5ayZAPx6ONiYCCwY8N92UfeXeX0B1HndmA4294pg2Mzc7S2u5fjDykI8VG1HFhX803g1M15eVKfzRzK_C5gtwso288YMLMbmfmPR7hRnKxdR8FDa7eFnm47yuDlmLuGTXaKKYOHQ44Lzt-JuXMWWVLNpL-DhMW7NW9Y1-R_aNUWhlypluv_xALrzlzxTy1mqLE_DwkSzwcAYW7lW9gQwMv1d-U3SXABSZAd97jGnzg_E1PNrf4wOaVlWT8h3evvEYszi7uNC0e87a4CrO95N9Am2k91eGcyG_ErAjSpFT_v1n5hhlxFWSJdJnsCUmTjcMtCN6WHqcbCIYzqlnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت جالب ایلان ماسک: جالبه بدونین اسم تنگه هرمز از اهورامزدا، خدای آیین زرتشتی، گرفته شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/IranProxyV2/8983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8982">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
فوری؛ موج جدید حملات ایران به اسراییل هم‌اکنون
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/8982" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8981">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇾🇪
فوری؛ یمن تنگه باب المندب رو بست!!!!!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/8981" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8980">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇷
❤️
فوووووری؛ رادیو ارتش اسرائیل: تشکیلات امنیتی اسرائیل تخمین می‌زند که در آغاز یک رویارویی نظامی است که چندین روز ادامه خواهد داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/IranProxyV2/8980" target="_blank">📅 10:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8979">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
⭕️
🪖
به نقل از منابع عبری ارتش اسرائیل در حال حاضر در حال عملیات در خاک ایرانه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/8979" target="_blank">📅 10:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8978">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
سپاه : عملیات نصر شروع شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/IranProxyV2/8978" target="_blank">📅 09:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8977">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
انفجاررررر در کرمانشاه
گزارش منابع داخلی از فعالیت پدافند در کرمانشاه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/IranProxyV2/8977" target="_blank">📅 09:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8976">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
⚠️
سازمان منطقه ویژه پتروشیمی:  دستور خروج اضطراری کلیه کارکنان روزکار از این منطقه صادر شده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/IranProxyV2/8976" target="_blank">📅 09:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8975">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🆕
کانال ۱۲ اسرائیل: طی چندساعت اخیر به ۲۰ هدف تو ایران حمله کردیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/8975" target="_blank">📅 09:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8974">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
کانال ۱۴ درباره یک مسئول اسرائیلی:
تأکید می‌کنیم که یک تأسیسات پتروشیمی در ایران هدف قرار گرفته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/IranProxyV2/8974" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8973">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5X3g1CoryUWGIXKVdfWWk-_52UJTZzOcP3ld3sTpausSgdC4j4_2v6OmDjH2U62ty0LthWXwO5Fq39d_v59KNh0z6v41sqH4SoqQcGSzfpqA5TgpSNzxdPi87DrMwtwXdkxThoJh4hd6R9spY3SDYZIb0JTvgnUSJpdh9nS1Y_9Fd3RqucmW5HmfuOfc_GoJVwEsMXmwQrfpmPQPSgQdwhSN4Ae_R-HE2luZ5egazcAxElD3xfNvuR38C1UPnH8WJny13OiN5ek1y1OgNCBm7tzijg6Sa26lzjzuH3bmyIUtaLhg_DMdry4VxpQYBdTssfxKDxG0LdStOJtO6Fzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور مورفی:
این جنگ برای آمریکا تحقیرآمیز بود؛
ترامپ دیشب گفت به نتانیاهو زنگ می‌زنم تا جلوی حمله تلافی‌جویانه‌ش رو بگیرم ولی اسرائیل ۲ ساعت بعد از این تماس جنگ رو از سر گرفت و ترامپ و آمریکا رو تحقیر کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/IranProxyV2/8973" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8972">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u29boIWz-c9EkxPXKItNWGnQoCNcaCwOQS2qjxJ-pE7h0hmeklc_j-k1SlmZuQv1irKj3I0O0wq9A-GPivtO1EdZXcuOyMYvnxR1xjwd2TPl6911wbTI1gTJLmUrPO1v2YZ7uTybTl9ic8VqyFRwB49iy9Y_3lB7al16Qvuf1bpUOi3fxplEpSSFjmFR-lT9Gh-Uu9e8BbCDvWo4YuFHn_ffPcIPuaTBLDmJW5KL4Xk1cOCc5nuEZrmsRtDyrDMbrlz8OMtWB4IdaH0ogSS7kwWinDawELjy_IiHGowxv9fnPqmrjK4xQWc5a-jgQ0ODeA9MXC-Ub6-L-hrF1-WZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم
:
سپاه موشک خیبر شکن و یک پهباد ناشناخته امروز استفاده کرده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8972" target="_blank">📅 08:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8968">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8968" target="_blank">📅 08:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8967">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8967" target="_blank">📅 08:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8966">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYDtGQu3TJ5h_UgoaOPl7XqJyiQiQvjHZxpHKe8xBXlJvl1TLgtASaTEgxntinEWrJx1gfPk78BdujLycD2eLFDSyfubZw9WoNbe7s1a6ivXwtUuZThFv3vK8bkrSnW5hTYTmyb29Em_48DoVj10JaViFuF6tbAgp8Qjg25VfcToVOIPXN9ijCliykuoZXrE12fhwfnLXuqXiKuGuIQYi5rtsiQt8Ey2AnpF-lebu8ZIkabNTDOVcisv0uS9WagVERjk_7-07nkigU_yu64bTqs8FkNW1tGWV9B3g9mfu3UXQtI8olAxuL5v-k015qEusEqkZxffHlv4Jhx_tb8VwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه وزارت دفاع عربستان:
دارن بهمون حملات موشکی و پهپادی انجام میدن، دستم کم دو انفجار نزدیک شهر ریاض گزارش شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/IranProxyV2/8966" target="_blank">📅 08:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8965">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رادیو ارتش اسرائیل
موج جدیدی از حملات رو شناسایی کردیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/IranProxyV2/8965" target="_blank">📅 08:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8964">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
اصابت چند پرتابه به پتروشیمی کارون ماهشهر تایید شده و بخشی از پتروشیمی در جریان این حملات اسیب دیده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/IranProxyV2/8964" target="_blank">📅 08:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8963">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc73ebd9af.mp4?token=B4aw451iVULoNDaGAD7lp2u1Neod61LN4AITCv49q0r_oIlE1TLo-nHA6RFh7GZMXMgCRivC8id6tHtE_csyN9o1UaMvO-qDQlioxwlzGMF2R1cobl_VSTWLWk9GUYwoWyp4QSEDQi6BQBaxijIGk3F5XBYuXeD1U1alxi4OgSNYYu3lOYm-p0EyhyUbAAH8cObCbGh_9aoucne-8j-4C3MnuLCYtAlZLPIko82zq5AjKLUrrW7t5cMRozqXoV4CEeqofAU0dmEc5pmVuh71nu4ecaLjDX4oXE5GkXoeWMcT_0QbNoFgpJp0IWUqrvNRjEXaAMMCJ84422NsGwUFOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc73ebd9af.mp4?token=B4aw451iVULoNDaGAD7lp2u1Neod61LN4AITCv49q0r_oIlE1TLo-nHA6RFh7GZMXMgCRivC8id6tHtE_csyN9o1UaMvO-qDQlioxwlzGMF2R1cobl_VSTWLWk9GUYwoWyp4QSEDQi6BQBaxijIGk3F5XBYuXeD1U1alxi4OgSNYYu3lOYm-p0EyhyUbAAH8cObCbGh_9aoucne-8j-4C3MnuLCYtAlZLPIko82zq5AjKLUrrW7t5cMRozqXoV4CEeqofAU0dmEc5pmVuh71nu4ecaLjDX4oXE5GkXoeWMcT_0QbNoFgpJp0IWUqrvNRjEXaAMMCJ84422NsGwUFOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از موشک‌های ایرانی به یک مرکز نظامی اسرائیلی در نزدیکی نابلس اصابت کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/IranProxyV2/8963" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8962">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldiD94e4FEKRCK5S7tePwWeGgn9-aj5AnnKGIzvWPySHokaxKFQNz3J7n7btecF8BGDhk_-8fwakD8wf8_CMKRD6-S4zNP3-AV6rPr6So2rzQqCGNdLLiS4DYIxDjsIMnJtzLmty2AKZjy1NeMUFfwQjoz2_-WQoQ2G8Op3-4gB9HKmUM-4kWwaqAC79xrGjVLooXoQ8lm2N7SgTZzQeMD5D_JJrf5xNQTPFZrHd_7bJ-9yPMp5aTit9FkqzfZ0xxOaRmCSII_MF6IPG-vKF-cLgaanmLN8rXHqB0tC8iAhDerXMXyE7gV_ralkAsriqReefOpepscmBPKuZVLD_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار اسرائیل:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/IranProxyV2/8962" target="_blank">📅 08:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8961">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
مثه اینکه موج جدیدی از حملات ایران شروع شده
از اصفهان ، ارومیه ، خرم آباد ، کرمانشاه ، ماهشهر و آبادان موشک پرتاب شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/IranProxyV2/8961" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8960">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvcSKLosqaUj4YMXZ-Sa0nCeDs7e-wCIf8HxVvDGz_bwEj_Lz5IkiskNkrA8wW7PH0pHvQMz9m98pmCBkDKN-RYU3h07oJ4j7N858Z_ig-YL5vxLxYyg_uxByFbOnHiBCr5TsiEwMqtKVvRuUkry5mTlur3kjWtel7j7zren4-W50NVPUmcpuLrgSwT_HtgrutcOzEHEIJ9S7oFsMv9CrayBfSGBVMeG13ry0c4UQ71pE_zcqpzVO_7b1Bz6bADcE7ZbFOSY-avSw6yyb4rbb1sd2yZ9QlywIQuP8bZQU3BXsohxx8Gd19tKKDh4vXmNwvCvxpd0cJXc0QTCc2atdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در پی به صدا آمدن آژیر خطر در اسرائیل، مقامات این کشور گفتند که یک موشک شلیک شده از یمن را به طور موفق رهگیری کردیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/IranProxyV2/8960" target="_blank">📅 08:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8959">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇸🇦
شنیده شدن انفجار در پایگاه شاهزاده سلطان، الخرج عربستان  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/IranProxyV2/8959" target="_blank">📅 08:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8958">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇸🇦
شنیده شدن انفجار در پایگاه شاهزاده سلطان، الخرج عربستان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/IranProxyV2/8958" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8957">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8957" target="_blank">📅 08:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8956">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
کاخ سفید:
این تنش های بین ایران و اسرائیل هیچ ربطی ما ندارند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8956" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8955">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شبکه «آی ۲۴نیوز» اسرائیل گزارش داد بر اساس گزارش‌های اولیه، اسرائیل تاکنون دست‌کم ۱۵ هدف را در نقاط مختلف ایران هدف قرار داده است. به گفته این شبکه، از جمله اهداف مورد حمله یک مرکز تولید پهپاد، فرودگاه بین‌المللی تهران و تاسیسات راهبردی نفتی بوده‌اند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8955" target="_blank">📅 08:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8954">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هرچی دارین سیو کنید احتمال داره باز قطع کنن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8954" target="_blank">📅 07:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8953">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
🔴
وقوع دست‌کم سه انفجار در اصفهان  گزارش میشود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8953" target="_blank">📅 05:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8952">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
سپاه اعلام کرد به ایران حمله موشکی شده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8952" target="_blank">📅 05:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8951">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3Um0rgMYO6ieJYK3xrgp1DNjS--BjafYlK5JDTkx95ZYrn5TcTByOpLyBL1VWchUm3BlGMKdTIPwKafReCdSIv-LMZOAiFnhPmZV04EcOU_8dR9-GasT5zT2KU3_GJvzLdROB4DlCUnsWJoCwDB91zLbCuXml77IJPECnkKKL4YeW4DJti_ZORGn_yjkN1iIwe5Dz3fjvgI34Ui2Vwx0bYuf_dqJDvaqVjO7InES58edC6qB7u5o3RvG33MxLGqg65LChtrZ0QTJYm50ogL28_10Fyy1y-QCZeJnNYOcp3wiKXEsfYjwN9H0iCcNtHLdlwQzuVu3yfNIYfA8efWvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری-خبرهایی از انفجار در پایگاه موشکی اصفهان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/8951" target="_blank">📅 05:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8950">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
🔴
فوری
-
الجزیره: رسانه‌های اسرائیلی گزارش دادند حملات هوایی اخیر فرودگاه مهرآباد تهران و همچنین یک انبار نگهداری پهپادهای انتحاری را هدف قرار داده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8950" target="_blank">📅 05:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8949">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
تا کنون تعداد اهدافی که اسرائیل به آن‌ها حمله کرده 15 هدف بوده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8949" target="_blank">📅 05:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8948">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
حملاتی محدود به چند سایت پدافندی و نظامی تو تهران، کرمانشاه، اصفهان، ارومیه، کرج و تبریز و چند نقطه دیگه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8948" target="_blank">📅 05:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8947">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری-کانال ۱۲ اسرائیل اعلام کرد که فرودگاه مهرآباد تهران مورد حمله قرار گرفته است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8947" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8946">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ulr6mo4tJ-Ptsk5KJDl6RmcAWoEbRM1kmr6rgi1MDze-fjXCUXlym77jpaipV38bx0eu2NLltwxSdnXGnEYbde30M6ec5h2ugzNC1wZw5gBkYbMNCeAX7cr5gHfu6DtlgNjpH6FD9OgOrO8E3CLSPhtnvD5ry9TN-HeerQ6VzJaa3XlZmoISi6wcVZS1VZNmNmKPkkQBgyVZbGotZ8SjEE27VhDzL7sKyA9f8cqqB00qS5fTx8zJKUlgLTHXuuH09iHkwJ-ODY1TME9f8Py7j00XzojRjdjoiTjfXsDYjPNa66FMzegnKO8Tqn10HIjkMCNSmOfh3PJBgZ2edhTlUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
حمله اسراییل به غرب ایران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/8946" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8945">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
آغاز حملات سپاه پاسداران به مواضع اسرائیل به گفته برخی خبرگزاری های محلی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8945" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8944">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIvDBMJPCRkcznEpNw-9z04sKjjb1_mR2dSkzjilSAaMudgL77_JWU41ueU7SrWbL6LoRdtY5x4Uwbdc2eZnPmepoesgmeL6myR6rLZZUGHyCKahf403SlFaXR5Oxx9IU9gR7wryemivQFS12KdQsrsor_P4zG0rCAbaa51346xZjvZa7nuxxHKKC3mMnLPE7UZl6iwiQXjKxaA_USI6y4SBPszT-2J-VorSdCBOqk-W0xXhgWa307zv_wsAxnO7LM8_eM4kK6D2AgEBM3RPtLxpwW9EhaC83tVrHtHRTHjYIt9G7O7O-rQ5FLOgUc_KlPbKl1rH2KCIfZ4gX1EdSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به کرمانشاه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8944" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8943">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
کانال 14 اسرائیل:
نیروی هوایی اسراییل با استفاده از موشک های بالستیک هواپایه و موشک های کروز، از طرف دریای مدیترانه به ایران حمله کرده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8943" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8942">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tata1BOrYFj97Ikxr7NesoT5NzhYLg5cq8he32T9QbQaa0j88vkuxr271bkTOD5WA-ZWlMaNbQaEg4IGL_H1nEq1MS8dv0H7BnbHHI84N718xwVRj4zncH3lrQuJySDM0BbewZfJFccBO9QpXH7TuhQPGfyJhMns01GieqqCJkJpDxQDySJOhgVRXClBcqvkwbDOAaA7H0aDw4TSqpI2mMWEE3M1AydQY5K0GjKiLD_zKZBlD7yy9HPLXq1ukZTaYv51-tKruuAifotzqXdDDQMKdlNdr3Skx08HZs-ba3U9FcdKUXn806Ifql4p3GaYgvti-FjWOkEi_qrw2auXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کرمانشاه رو هم زدن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8942" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8941">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liQduyYlL2FpNvXpkeIlV2jm1gQaJRgb5tKI_t0bP4bmBlNn5Q6k82FITgEZGkbl1iKYNr5TCotL72wWwbq3dDZ05EU3TDeD8olyvDYcGluHbtb42YsBWIwZCU4mm1QSA-QRp3o1NNz8rdlRJRHF2kQtRQufQSku1pqPseUuDAxGTa8iJjCgLHnV1IC7R4CJqgsl3PVUkTAPWqCNme-7U9BK4f6MfTHqBVdMcjZ8tr_DL6HLdReH-UHlnwUOZo1fxlKzUdveuE_NgEP20rZowMr3caK4kH7-glca-nIoqSdT8yOLwQKcCSFUGSQ7sMLdsY6Xm66MIJj7NP6l4TRTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه رسمی ارتش اسرائیل: «دقایقی پیش، نیروی هوایی اسرائیل اهداف نظامی متعلق به رژیم ایران را در مناطق مرکزی و غربی ایران هدف حمله قرار داد.»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8941" target="_blank">📅 05:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8940">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuFCicNivqHTNmwTlrx2_JtNOrwRzMEND1EsO4DHq42N4CzwTeb6mjIDGiCpa7aW5Ux-mgrPfPK1zIpOJ2GwBUJ1lJh-jx7HYA0pG2ui25QxV837F5RLoA6dJujIsIC2iD4LnhqNjmYHHanGzvasAFz1Sk3j2ZFWn_-V9gPsDwfEAp6m6KNrPrvu2rL8e_0qRvoVG0yuqHhketCGfO5wDq6_gzWrGuV_PjQXWOhYlJo89qK0YBeXqN7J-mrT-vl-9yvlbXYNKZ2YuHMCkWxlSAmEDbQylgHURSrKB287P9Rcql2pto1ItvSFVnTONGJuO_JiFL8VVH5xu1Xk1YVDNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صدا و سیما حمله رو تایید کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/8940" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8939">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTADhbQJbvpQQPIeeYCMyy3XUqKbzh38bF4bkmasrnfPsH20uGjT9CxK3CowDO7CF8SHUR6Diiadj1bD-BiEwGQ2lJfpKfMVZ8TsaDD2SR7NWs18cl0ldkPwgMjW9K1oLa1z5YC7b1YjSbD_bKe9G_hAxgevuXXZ507d_Y1D66-p_zCsDB1nDeVfNwCozs51l0mQ5CZx-jbAxeS_kTqjO_nQXWRXR1wZ66E9EkoyAvpDKA4p1c2ug1V_P3XgwRn1KhjqFW2kABIN-gIlcwfOJrwtOTttz_1JG7pJ1PCkJZvtvB9rvy8wXEspwgwPYy2lYXhzJzV12dza4y6_hoXUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار تو تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/IranProxyV2/8939" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8938">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
انفجار در ارومیه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/IranProxyV2/8938" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8937">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrf9SYCej993UI9o4NUiVP-0aEvAmGjo5h07P5jjUN6vJlVCmaUbFX5Hvi5SUf7S1gruT5y-KbupNBBry5oB7bqjuVv8I50YMeyDXqFbalaQQq-UNBC-hJE4S5biSSf_Vpl-PGJMJUfiIRZDZHnmgjTSyvbseqfFp-hD2NoArWZwVbUaK94rlPceSBydKcCVpFqrcEpYuDiW2gtFSNZP76EPz3b7iM7j_a1EvE_tos-K-WXMjc2lsQtUrsa7rlBoMBPE2KozhrRlOrS_eJVrAA6HP3TOlG0SEpgajbuqQe233a4A9y2Fdsgi11yHu1WvMEhB-goZatG_lh_f3Jh5fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شاهین شهر اصفهان،ساعاتی پیش
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/IranProxyV2/8937" target="_blank">📅 04:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8936">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
کانال ۱۴ اسراییل:
جنگنده ها دارن وارد آسمون ایران میشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/IranProxyV2/8936" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8935">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQvEg1He-_JefMdfA8VVTL1zemucPXFeoXIj5-fMSn1UuWoC4pBfWqMX-fT_91C05SrFqc_Q7xCQm6sthLOa0f04DNkW0OqXxMTsOuWYG2KgridxflbU_srJh28OAfdk8SYSazmoJZr12GKSxi9ax0d9lfRy7JtTjK6PIIjdJunCg7Nb1XfNga621R82rh3xc_aFMI92YSuMy5quLrMSJM--C1_uFRKuw8bsAcihVrNxX5fYxlAjOANiGYadM69I2p59lHXg-29wXBlH_1zfifgkE2fKYYAFgwgOqVYDHydAIRhnDglLf4edVBIskTCqM8qdRxSlv2BPXfuqTreoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یا خدا اصفهان رو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/IranProxyV2/8935" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8934">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zk4ym8TSq0cn6KNs8mH41_tJ93NDq04Airj_l_FYLoyVk_xdjkusDNtrXrVeGnXiKBKElrexh8M1LK_uaxVWaG8-1_wmER4EPOxtsxY2f244OsKlFCAxuvDhqjzrMTqauhhfBCks_hhLInlT_Iq5PHjyzQr2UJbwlQjwjzUQqzOSQAhzUn5wtRSYBUoqNUVtQxuk5ZIL1ftpIeTI7PZOfiPIBJ9NVTWs9kiBm55lV-WAMB4jeDfncklFalSQ5KwP1GpnZwlhM4CwFDa53gW-rfPiHmqWtKgUEvtb5E8NZj6s12Lp1G_-dQYsDDOVVqKoISShYM8Sfr9lsGXfxOgYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نجف آباد اصفهان هم اکنون
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/IranProxyV2/8934" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8933">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پدافندا راحت بخوابید مردم بیدارن
😂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/IranProxyV2/8933" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8932">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/IranProxyV2/8932" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8931">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
همزمان تهران و هم زدننننن تبریز و زدنننننن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8931" target="_blank">📅 04:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8930">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
اصفهان و زدنننننن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8930" target="_blank">📅 04:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8929">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏
🔴
فوری-سفارت آمریکا در اردن با صدور هشدار امنیتی اعلام کرد گزارش‌هایی از ورود موشک‌ها، پهپادها یا راکت‌ها به حریم هوایی اردن منتشر شده و از شهروندان خواست فوراً در پناهگاه‌ها مستقر شده و تا اطلاع بعدی در محل امن باقی بمانند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/IranProxyV2/8929" target="_blank">📅 04:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8928">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تنها حمایتی که میتونید انجام بدین اینه که ری اکشن بزنید و فور کنید برای دوستاتون پست هارو عضو چنل بشن، ری اکشن قلب بزنید رو این پست ببینم چندنفرید
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8928" target="_blank">📅 02:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8927">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">+1 ترابایت دیگه برای شما دوستان فور کنید برای رفقاتون
🎁
❤️
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@deadvix.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%A9%F0%9F%87%A%20%D8%A2%D9%84%D9%85%D8%A7%D9%86
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@dep2g1.aswall.ir:43582?encryption=none&security=reality&type=tcp&headerType=none&flow=xtls-rprx-vision&sni=play.google.com&fp=chrome&pbk=95vLe0hBBerV1ch9WxJ9iPTi4u7V9NExNADg9-LpcwY&sid=025086f1385a838a#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@dep2g2.aswall.ir:11000?encryption=none&security=reality&type=tcp&headerType=none&sni=refersion.com&fp=chrome&pbk=YWfCdTnr4FAOMYTY2dLrMtQUokyxOGpPhYEEszPj20E#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8927" target="_blank">📅 02:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8925">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8925" target="_blank">📅 01:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8924">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
ترامپ: اگر توافق به دلیل بندهاش فرو بپاشه، ما گزینه انجام یک حمله کماندویی به ایران رو بررسی خواهیم کرد.
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8924" target="_blank">📅 01:56 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
