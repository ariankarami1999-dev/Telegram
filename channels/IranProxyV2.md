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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 18:24:47</div>
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
<div class="tg-footer">👁️ 950 · <a href="https://t.me/IranProxyV2/9033" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/IranProxyV2/9032" target="_blank">📅 15:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9031">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
مث اینکه جنگ فعلا به پایان رسیده، هردرطرف از موضع خود کوتاه اومدن ولی البته یه نکته بهتون عرض کنم که این شرایط فقط تا پایان جام جهانی فک میکنم آتش بس برقرار باشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/IranProxyV2/9031" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9030">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:   نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/9030" target="_blank">📅 14:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9029">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/9029" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/9027" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/9026" target="_blank">📅 13:31 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/9025" target="_blank">📅 13:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/IranProxyV2/9024" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9023">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=s3.mowork.twc1.net&port=443&secret=ee90872f20ccc37e3aa2681602f51df71273332e6d6f776f726b2e747763312e6e6574
https://t.me/proxy?server=s4.mowork.twc1.net&port=443&secret=ee3e9cfe9af4494731b9a566075ee8c3bc73342e6d6f776f726b2e747763312e6e6574
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/IranProxyV2/9023" target="_blank">📅 13:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9022">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
vless://a78bf929-6883-48af-902d-7737793eeb17@hu02.sonicsonic.icu:443?security=reality&encryption=none&pbk=z-TKWOWgZLfzQ-wNdwXQqVwaUgCmbchM2Xtrk1NGynU&headerType=none&fp=qq&spx=%2F&type=tcp&flow=xtls-rprx-vision&sni=hu02.sonicsonic.icu#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/IranProxyV2/9022" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/IranProxyV2/9020" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/9019" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9017">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
براتون پروکسی نت ملی و اوپن و... میزارم، حتما ذخیره کنید و برای دوستاتون بفرستید درصورت قطعی اینترنت استفاده کنید تا بتونید، حداقل کانکشن رو به تلگرام داشته باشین
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/9017" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/9016" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/9015" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9014">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
فوری/نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد  بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
✅
با ما اخبار جنگی بروز باشید  @russiamilitery</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/9014" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/9013" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/9010" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/9009" target="_blank">📅 12:16 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/9008" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/9007" target="_blank">📅 12:07 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/9006" target="_blank">📅 12:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9005">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAGGcxZ_KMWq-2Xv8ZB3bhYM8u1d0Zl7S0qVIMeFa4XCJaNGIsQiIIPtjz3jaC23UKGYMbiCamFjvQKHdlcv7Q6usX5G9v0QoInT42Fi6WKj_46MppQJISGi9QpiiyYjCvTd1M2U7_8frf2bjYb55a6X8BQT2EBP6ZDlm-joDXvdnGAhO7C1FtrxjVtzFYMoXSKKO8YKMjndxYQMHS5APNN8xiK2AjPCabL37mT6sgtOPn_HEJh54Cs7WhCG7oEctk4UJ48DwdZqPmILPbLmQa9USdkf8CqWFR1U8Yv5HOaN7E1B4Rduny29PIyY-nMVpj6IOnzm9AichLf8g_0UVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون تهران
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/9005" target="_blank">📅 12:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9004">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alZsNAjoFRFqKWVqTZweh_9CKKRYt6qAVjrUrrvN1UjucCcpM8TQA00a6HWNbJDQLiXkDp_3cvFspdkjdp9FV1QIr4N07k8mSREjEUMeuDcWRe9zGIRoVeBBNHMhQQ9KEHPPQYnWyg12jnLF6nXxqu1sDOrUU-4TefUJXHvz3ckKoMcrck8N9pL_RwgxkZG2pjoDwh22BPRLGf-UiQapJt4xBUPnDFl92eyhQiV4gnQhQ84Dwmy_xKEljm2JQIbDVXZTrXZ3t1Ge40ST1p2gU2Ry7vzJzW9Jfqa7vsNDviOgrx8jC9_tKWg1RBmtDOx7rEZZTjR5RcvYThimu4_mBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تهران، شمس آباد:
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/9004" target="_blank">📅 12:02 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/9003" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/9002" target="_blank">📅 11:59 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/9001" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/9000" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8999" target="_blank">📅 11:54 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8998" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8997">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
تو اکثر نقاط تهران، پدافندا درگیرن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8997" target="_blank">📅 11:49 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/IranProxyV2/8996" target="_blank">📅 11:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8995">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری-صدای انفجار در اصفهان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8995" target="_blank">📅 11:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8994">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری-شنیده شدن صدای انفجار در اسلامشهر و ملارد و کهریزک و باقرشهر
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/IranProxyV2/8994" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8993">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری-شنیده شدن صدای انفجار در غرب و جنوب تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8993" target="_blank">📅 11:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8992">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oayWtRgUBLvNMWwtzPn3wE4ZD4cugKvU7bsC67ZCTw7KJpR7BL62rr35DQKRpNldBX_6YZFFgiVzuu15-6LdKRlz0Tn8rdfAfVnfdO4YU43Xivfu5BGi-D7QnP3DulQI2XzhZ0aUmekwU7M_-pOFnYZDGJ_N49e7EYuZZwpLEIWrJadRgRG6WwmmR1ErykOHrwjlPk7kd1asVlEtZ6h_NCj2-VvmhwdYIX2RQfCoupkcLpeh1xw85weW1FkbgN57SPnm4QMre1Ix5P1PcZhOtp-ED0H1PVpfs0RlQXXzWjpwuJi0t-Qa9moq5Sc-xZ0Ji09cIPvhW3gGXDmc0fCziQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وضعیت آسمان اصفهان:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8992" target="_blank">📅 11:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8990">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سپاه: حمله دشمن به صنایع پتروشیمی پاسخ داده شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8990" target="_blank">📅 11:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8989">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb9354396b.mp4?token=aZWHevlZkiUH-976ya_YgFvqc8VbWU0X8zVyKBZhiHHjQK5gAyvu5pCneog4EzYIOfsmiX5AXBie5rVs5TUciG6by3qKGVNgTeP4fYKpqFPPeuaa0_3wvVe2QWu4hi0K30aBYVy72D_Bypn6hOzPHGJLyLKc5lP7QRJjBmfZjaIzYmhMInC83eeMMyfOaOjBERXsew40HFTZwL6rc4ZIu2P09KinK9ngJFa5tW6DBwt0A4XcWJ_ssXU0sJYVXo6bS-QwIBOOrJJvPqlB1YC8pxWbQ16q3UzUZRwTB3tJo67rfKbW-VVrNWOha4X_5m8I8MoJ7_BJ7qHoKczE5Lvwpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb9354396b.mp4?token=aZWHevlZkiUH-976ya_YgFvqc8VbWU0X8zVyKBZhiHHjQK5gAyvu5pCneog4EzYIOfsmiX5AXBie5rVs5TUciG6by3qKGVNgTeP4fYKpqFPPeuaa0_3wvVe2QWu4hi0K30aBYVy72D_Bypn6hOzPHGJLyLKc5lP7QRJjBmfZjaIzYmhMInC83eeMMyfOaOjBERXsew40HFTZwL6rc4ZIu2P09KinK9ngJFa5tW6DBwt0A4XcWJ_ssXU0sJYVXo6bS-QwIBOOrJJvPqlB1YC8pxWbQ16q3UzUZRwTB3tJo67rfKbW-VVrNWOha4X_5m8I8MoJ7_BJ7qHoKczE5Lvwpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم‌های اضافی از موشک بالستیک ایرانی که در نزدیکی یک شهرک اسرائیلی در کرانه باختری اشغالی اصابت کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8989" target="_blank">📅 11:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8988">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88608e0e82.mp4?token=WSmuaJsV_GbeuzuWe3_tSEt9JKv36mBF2gqtFSpPiR7w5-XaYZhoS1FUA4oa-JdjQGXDi484ufH6Oo2QzKOrzEJWVf2ra7m6bU0cN2Wbgmj1bySNARcWnWjNj9Uy5NgmYSUvA6qm4-Q_D1MmI0k36jGrvjtXrR9iCL1hQXil-Hv0MPMWusL1nxJ320HfVi-S-dXeMvQ7M4DquoCgpSq17YOjj_RP5K1qAc3knkdNyEzN9tiHKEboGK7W6Gnn4aPLJafGqSi_monpsgPzWeDCY4SbowGvxnx81wk5h2FFbrIyqTtNHbjgxfo1gSyZOxU3D1_zfH2SysfS8Ct73iCQ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88608e0e82.mp4?token=WSmuaJsV_GbeuzuWe3_tSEt9JKv36mBF2gqtFSpPiR7w5-XaYZhoS1FUA4oa-JdjQGXDi484ufH6Oo2QzKOrzEJWVf2ra7m6bU0cN2Wbgmj1bySNARcWnWjNj9Uy5NgmYSUvA6qm4-Q_D1MmI0k36jGrvjtXrR9iCL1hQXil-Hv0MPMWusL1nxJ320HfVi-S-dXeMvQ7M4DquoCgpSq17YOjj_RP5K1qAc3knkdNyEzN9tiHKEboGK7W6Gnn4aPLJafGqSi_monpsgPzWeDCY4SbowGvxnx81wk5h2FFbrIyqTtNHbjgxfo1gSyZOxU3D1_zfH2SysfS8Ct73iCQ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از تأسیسات پتروشیمی هدف قرار گرفته در ماهشهر، جنوب ایران.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8988" target="_blank">📅 11:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
رسانه‌های اسرائیل:
پس از شلیک یک موج موشکی از ایران، صدای انفجار در منطقه مرکزی و تل آویو شنیده شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8987" target="_blank">📅 10:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
اتحادیه اروپا: امروز تحریم‌هایی رو علیه جمهوری اسلامی به‌دلیل ایجاد اختلال در آزادی کشتیرانی اعمال خواهیم کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8986" target="_blank">📅 10:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8985">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
مدیرکل بحران آذربایجان شرقی:
در پی حمله ساعت ۵ صبح دوشنبه به یک مرکز نظامی در تبریز، هیچ‌گونه تلفات جانی گزارش نشده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8985" target="_blank">📅 10:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8984">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فعال شدن آژیرهای هشدار در اردن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8984" target="_blank">📅 10:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8983">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrdFHqGx2NoxssSg4A1EnXfKeHEIqI1ettyGJtlGn22eu0m5B27VnfYVeDo48Mjg2MT4FuOpAiF8WceomGoh5EpThg14-JWwf8ox3vBzxnV2sDhcuOI_EkwZJw5igOzo60KJU8kRWA8Sq186rCQ3H_bA1EAJcsIVls3k1n4GQF9p56s-yoo_VVbna_pxY-7AIjpBjZmCLheepgDrqj-2SXPA6J2VUQ1YCHHxJGgfmtY1CNf_trTHfz2A7-f43nAC0G8uDle4SUTi6NBo8T0Tw7ohfJvcW_wMUbaSYTWwvVuVyaZ9gsjxElu-x_oRqi2Q5eW-Kxty1tZjl-ngNIuSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت جالب ایلان ماسک: جالبه بدونین اسم تنگه هرمز از اهورامزدا، خدای آیین زرتشتی، گرفته شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/IranProxyV2/8983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8982">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
فوری؛ موج جدید حملات ایران به اسراییل هم‌اکنون
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/IranProxyV2/8982" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8981">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇾🇪
فوری؛ یمن تنگه باب المندب رو بست!!!!!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/8981" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8980">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇷
❤️
فوووووری؛ رادیو ارتش اسرائیل: تشکیلات امنیتی اسرائیل تخمین می‌زند که در آغاز یک رویارویی نظامی است که چندین روز ادامه خواهد داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/8980" target="_blank">📅 10:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8979">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
⭕️
🪖
به نقل از منابع عبری ارتش اسرائیل در حال حاضر در حال عملیات در خاک ایرانه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8979" target="_blank">📅 10:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8978">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
سپاه : عملیات نصر شروع شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/IranProxyV2/8978" target="_blank">📅 09:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8977">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
انفجاررررر در کرمانشاه
گزارش منابع داخلی از فعالیت پدافند در کرمانشاه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/IranProxyV2/8977" target="_blank">📅 09:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8976">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
⚠️
سازمان منطقه ویژه پتروشیمی:  دستور خروج اضطراری کلیه کارکنان روزکار از این منطقه صادر شده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/IranProxyV2/8976" target="_blank">📅 09:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8975">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🆕
کانال ۱۲ اسرائیل: طی چندساعت اخیر به ۲۰ هدف تو ایران حمله کردیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8975" target="_blank">📅 09:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8974">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
کانال ۱۴ درباره یک مسئول اسرائیلی:
تأکید می‌کنیم که یک تأسیسات پتروشیمی در ایران هدف قرار گرفته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/IranProxyV2/8974" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8973">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0Gt5btLjEw6oDrW9bd8Vtsh2bf7G0BD6ybZpn0VxRTNeaob6G3Rw33ZX-YsI8BJohfkRocmDWOvhAhaPuoIV-JKWRSvYqPlrmVTdtv6roqjkmP8H0fT6NV4HMbWNG8m2JM8jN3TmRGsGQd_8M-bCiMueiiCVOEsrRNqoOO54HPpVZ882rjss8oO-DgTFqV2qMHjeSI40MDqYI660AIjcuRIKjTLL9__jKnkaYuzymZ5rN-ddLfoK15Z_volugPaondYer1qPV7cAlrRuuGjeMNyMa76CAzRtNjmy5BI32WOlaTwIqIX4xihObxjcVrInbgwmipLAuhYMmew_CIGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور مورفی:
این جنگ برای آمریکا تحقیرآمیز بود؛
ترامپ دیشب گفت به نتانیاهو زنگ می‌زنم تا جلوی حمله تلافی‌جویانه‌ش رو بگیرم ولی اسرائیل ۲ ساعت بعد از این تماس جنگ رو از سر گرفت و ترامپ و آمریکا رو تحقیر کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8973" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8972">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw0z0wVTCTnf3C47ZfcSEsTY6pZOG57I7TcD4FZHvqsKdcImqxv8rfBVOYs9vc5wV_t3ywjmQv3ZODj_Knq0U5TIr7y-r6ZKpDE3_lZs4A5Iw82CoGINigVi8xcu2WWrTbvMDeQCvx1yRcgjCCSJNXYdniSn_K7dXPj482iEVZ5pBK4etsr9yo2NAponpf4ooGHStsCT71DuCiiBb8phvv2HN5oDzEVi4-wAmIH7Nrxa27kHjFea04RBKLWrpFb2afuGtRDfrkjFqCpEWK8aecblkF8GhIDecfXNk4gXoLcmegzxw0n7QTs8tdyrMHAG2Ijch0rf5IC7xcoDH0cMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم
:
سپاه موشک خیبر شکن و یک پهباد ناشناخته امروز استفاده کرده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8972" target="_blank">📅 08:28 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8968" target="_blank">📅 08:25 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8967" target="_blank">📅 08:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8966">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_TczatfpELjYM1-WZLyp1usIS3M5vqbY7su77L8F_DwSXdHL5YOu3BRyDQgsfU0y1WbAzkaI4c2ESLhY3TQZVtLK94KDD37Q8YIfyZTxQUkkv9ITBd-za4IdPg7kRRrfF62h4dlyqRPQPEUmRZd0Vv61k5cfSdRavHOEFKHaMGpJveFYjp-Dz9I3yCfB1VdA-Hd54hzPpvJIx7uuB0yqXqSy4IoXHgyauGAXlZ4x55ocqj0-DTRgIG8rEEFRSo6R2wOf2lFmf_X1_nulThVCaAyKqbXQHED7IEuUgr9zJzH_v8NPGDhLis2W3i0u2cWMO4Djz8LuF899nJaPrwgeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه وزارت دفاع عربستان:
دارن بهمون حملات موشکی و پهپادی انجام میدن، دستم کم دو انفجار نزدیک شهر ریاض گزارش شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8966" target="_blank">📅 08:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8965">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رادیو ارتش اسرائیل
موج جدیدی از حملات رو شناسایی کردیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/IranProxyV2/8965" target="_blank">📅 08:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8964">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
اصابت چند پرتابه به پتروشیمی کارون ماهشهر تایید شده و بخشی از پتروشیمی در جریان این حملات اسیب دیده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/IranProxyV2/8964" target="_blank">📅 08:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8963">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc73ebd9af.mp4?token=drKNBlXGcLwMJy3ZFLDDZs4ikNjnCNVRCWkpeFQE2Hi5H7gjMafYFE_YTSm-dVxRpzHmQp7t0rHZ_83-ctsWH1p--_GWWiz99RXBDAhDD-z-IBbUx2wdX0Zdobwz96bFkjkte_0Zviny6kk24zibQIP0MeNOSoQaJB5P1e_yhcbp33pJwKvOuxenZ56J0qQG-vGvjUgn3Z6ix4_KpP1RWGMgOeluj55iWVYzbykWLBDaA-jpG_J15zsuHLfFNDF2QHDpbX-5PQi7fjhiQR8vS8D9hjaAEbbWVTIVuOnrLY6UQYsBS2ez7LRiOvqf8Yx3oTlalmBwkLgkgpYfgkgmuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc73ebd9af.mp4?token=drKNBlXGcLwMJy3ZFLDDZs4ikNjnCNVRCWkpeFQE2Hi5H7gjMafYFE_YTSm-dVxRpzHmQp7t0rHZ_83-ctsWH1p--_GWWiz99RXBDAhDD-z-IBbUx2wdX0Zdobwz96bFkjkte_0Zviny6kk24zibQIP0MeNOSoQaJB5P1e_yhcbp33pJwKvOuxenZ56J0qQG-vGvjUgn3Z6ix4_KpP1RWGMgOeluj55iWVYzbykWLBDaA-jpG_J15zsuHLfFNDF2QHDpbX-5PQi7fjhiQR8vS8D9hjaAEbbWVTIVuOnrLY6UQYsBS2ez7LRiOvqf8Yx3oTlalmBwkLgkgpYfgkgmuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از موشک‌های ایرانی به یک مرکز نظامی اسرائیلی در نزدیکی نابلس اصابت کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/IranProxyV2/8963" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8962">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWoTvKPkS9smNgx-HshZW5mp9jVJZ_U6_b0pMXesN5xc9zkrnG-_m3FywldKp8w9ZqOuYZ1EwYTzN8YFbKpyHMqohwvsJ5U4FZvAsKYrL5at2MC8z6s3QEgSZa5fFBCwi5TqYc22E_9NwJP-VXS8yFQp9aUTdLTrHTrik-4bt2K3ie5UE0qEeyn0uoms8RiVqyHs3sWxC7BmiMiOlvAUSnNx2FGeSVKmWbWw9znTKcc9CxtyeUN_LNOmAZqFRYe5wNQ0Gq4M8qgWNWHoq9rIYgK4x4NKq3X_RPoP6yIsbaVpC649zEUd-ebx1IFHBl-jAMSlh4B4KaRWzwG2uNI2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار اسرائیل:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/IranProxyV2/8962" target="_blank">📅 08:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8961">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
مثه اینکه موج جدیدی از حملات ایران شروع شده
از اصفهان ، ارومیه ، خرم آباد ، کرمانشاه ، ماهشهر و آبادان موشک پرتاب شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/IranProxyV2/8961" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8960">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6KTiNn67b_4SBk5vXWpZbg5yJSp7pzK4glKp_iyDa_fqFlkWN15aprdiqO-SelaYEZNBf8rriKglSzlEpVweQ2vMxf4itSXxG1XiSXkzExqU7bEVC8dC4HwYvZQ80UTQj5fo1F4Vt4I5vJODbIf6A29_FJTpcEUOliJTHuRMjFjcz2_5R-Uufsgy2jd-pUn0775i7-QapbcAtOuu6fTs5Pd9kW9-1WR0RdRCNH5cOaq1W_bhRXSe_oJ1e1NLr9qUws7GSpghTIVK6uxDbx47KMyhoGgRAqUFTiCLaCJoBF62AfWUbOGobnKf-SOzkBUbWcCRxj0P6XdwqvrfO_2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در پی به صدا آمدن آژیر خطر در اسرائیل، مقامات این کشور گفتند که یک موشک شلیک شده از یمن را به طور موفق رهگیری کردیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8960" target="_blank">📅 08:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8959">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇸🇦
شنیده شدن انفجار در پایگاه شاهزاده سلطان، الخرج عربستان  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/IranProxyV2/8959" target="_blank">📅 08:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8958">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇸🇦
شنیده شدن انفجار در پایگاه شاهزاده سلطان، الخرج عربستان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/IranProxyV2/8958" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8957" target="_blank">📅 08:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8956">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
کاخ سفید:
این تنش های بین ایران و اسرائیل هیچ ربطی ما ندارند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8956" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8955">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شبکه «آی ۲۴نیوز» اسرائیل گزارش داد بر اساس گزارش‌های اولیه، اسرائیل تاکنون دست‌کم ۱۵ هدف را در نقاط مختلف ایران هدف قرار داده است. به گفته این شبکه، از جمله اهداف مورد حمله یک مرکز تولید پهپاد، فرودگاه بین‌المللی تهران و تاسیسات راهبردی نفتی بوده‌اند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8955" target="_blank">📅 08:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8954">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هرچی دارین سیو کنید احتمال داره باز قطع کنن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8954" target="_blank">📅 07:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8953">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
🔴
وقوع دست‌کم سه انفجار در اصفهان  گزارش میشود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8953" target="_blank">📅 05:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8952">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
سپاه اعلام کرد به ایران حمله موشکی شده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8952" target="_blank">📅 05:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8951">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olrm42Wt72Xd1dzep_s8noN2l6yecH2KWzyoA7Mm6HlVB_dhdGYvw_-vlywftFD5yJpTfZ6LSOZy7-VUdz1G9NVo0DeQSV5t7uEUVrrX-VcRfvRrfgfdUGxptnyEhUxVM-Fng7BUPjcEaGF-zWeWJSL_lpcKimwRixDgj4VV85-e1uzv-WKfLNOSeBIERKmjBZgK0nxVvWi6la6zQkqQdb_sdWRM30qqM6GbaUZ9sTcABYobnqqu4OudQCE9OF1lccfXTHVlSnCSqFoNKla2qNwefMn1rqyP53jqJdRyas0EEYPQNAB_8HMFM_id9LjtPUU7vQzxKJPUbNbYRHXLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری-خبرهایی از انفجار در پایگاه موشکی اصفهان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/8951" target="_blank">📅 05:26 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8950" target="_blank">📅 05:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8949">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
تا کنون تعداد اهدافی که اسرائیل به آن‌ها حمله کرده 15 هدف بوده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8949" target="_blank">📅 05:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8948">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
حملاتی محدود به چند سایت پدافندی و نظامی تو تهران، کرمانشاه، اصفهان، ارومیه، کرج و تبریز و چند نقطه دیگه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8948" target="_blank">📅 05:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8947">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری-کانال ۱۲ اسرائیل اعلام کرد که فرودگاه مهرآباد تهران مورد حمله قرار گرفته است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8947" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8946">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz6o7J8vuUgNIl7p3ZbjtaRTNgIv4gXvpUeoQefOZJCB_snhlTDfM3R8_r9zppudz6m4SppGFX25H8AnA2JSSbV_DCpHKcKesaP8cjkAiq-GQMoY6jwT2Z3DB6kmahcd3TFLxuAmVSoYh76z5wiu-9YAOULPLM95BPT7rt9Gm-69n57lYkoqIk9VqTwd6EF3iSedBZpVIRh3a-vjrzjqqzh_4XJhIycAUtCYIP3LnEDsid9tClS7I2DzHs7ibGFKuGQj2D7-LQXbfd5Mv35iZKZpzNawyGJZJdVZFY0hEqU6MfLRGObzmB24d67IbfQ3KTH9DyhN6f-pYeXKe8tnNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
حمله اسراییل به غرب ایران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8946" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8945">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
آغاز حملات سپاه پاسداران به مواضع اسرائیل به گفته برخی خبرگزاری های محلی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8945" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8944">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzcGJrD84jHN4V5AmP99N6EyxdvS8BcODHXSZMfvvF423bPlrU4KmvXXZp3Vts9CAA_4IEt9gG-MnP7Yh0_X4WtbkulOBoqQWqhqDRQuHa-Y0vIRtzvmuOZUKEkaTv2IukWzUWnaILrQ5t2rDZy9C8QAJsNoP9JBxKy03YDiXbsgiLugTEEhgt6RLIcOOLJKhnv6TKFVnYKqD_Y-I8jTVAyG9aSZbf7-IeCW6y7sJ6aD5T5udXkNZpdhifbINssmrkzixcrRsUDKMYw-pCOAsmfnL4vNjVx_lxj929vuEGSj9rnywRbtfOYwxfmI5Pm0Vmd5pDu1co3ObpZu0nlWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به کرمانشاه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8944" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8943">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
کانال 14 اسرائیل:
نیروی هوایی اسراییل با استفاده از موشک های بالستیک هواپایه و موشک های کروز، از طرف دریای مدیترانه به ایران حمله کرده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8943" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8942">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTaZFIFvvtlqadlj7z5GdmN-q_NcwX5eFF7OtPaNWAoOQsXQR-nG84AgtFFMRZqd6bbxKajy1ybyw3Rn3nGjGN8-bc40V5I07eGIeFouZT9-tYU__wqIig5uZY1I-43WTUHGfN4dGsK-ju6xq6FrISsU5SnOJM7wEvW8rqoJ-k23-bLqyVjagneF-bjJ17CAGkTZrnupYssiWvCvWhqH9-i_oohb3Fz_i5x0EAtaTjEN1uQDIhdRgbVXATFwTYYyj6QRtE5Q6ZLp1S1wqbvlcVRb7ThNCMSxf9Z4gnf60TpE7S7Ic6jZEEhaaly4Po_TLXol-ZSSFXO3e1VGgsW8VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کرمانشاه رو هم زدن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8942" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8941">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSlSetPfiRoM2ngz9Ov8tMkL0CBTBA4RIZqu9zcQbyWoxMX8N97domnoWn2l78U4hYrs2UwPUW0rtpnuVeYkwjiiNWc3dRY9RwtaVuudI7wScTNcYB2HlBSs9VVbT889rgNqT2JE4FlC-zwPyrpgPc6mkCBKRbLxa_8Do_JrgJ4JbLQTlzIEqWh3y_HI4lqnaCl-Z3R_BiWlpgEASfogIFcNTxUttDJRKaJ_GrRPnQIO3DjbgkFtX2bQC0aGFsRDFFy9cwLDZH0Y1aHHNQ97Rqs6V_nV8cHfOmMXrMLcU6D43BEnqkKcNdqDqHSRmLwxdjTfXyf0_8re4fRKqsUaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه رسمی ارتش اسرائیل: «دقایقی پیش، نیروی هوایی اسرائیل اهداف نظامی متعلق به رژیم ایران را در مناطق مرکزی و غربی ایران هدف حمله قرار داد.»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/8941" target="_blank">📅 05:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8940">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPh_LeKMzaFgt0DtCY-I7cu3mRPMtpZG8o8cLkwKIQbB1TM-aTmKW47heBK9v96GxIWdnvBbWRSxLk98qIIBIg7qvU5d8zpHgLWhtMojOWvfhjcgm4u9LGPnJ6HqfB7r6WHQR3qwuhJx-1q7vDxhdSkdqyG6h7nfYNB3V2uCq4o4YHDh9VNogvP5ml211juc-vGNLkovC3X3pmgYSahKQftJJ-zjLVOCxaDf0gnp7O_T31kJvDLyhrRCxERT-GwIRU0yrEBR3-T37S-i760hC1nEBsO807tssDY7HKpuBIS0ylmjQ2u4dPM68rOFk8pvaJQ1ITVgVCLQGU685jL5GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صدا و سیما حمله رو تایید کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/IranProxyV2/8940" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8939">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ohu3dHQEhfgG_EdbRJ1FxAoMDogERvGIn9smtPKw34fjGM9Uzrjc5EBqhXlEOIYOC1cZTKziMPW3_ip4ytRv_yYRWSwfJ3zRXFmtyY7y8DojUDux1oqR_StkS3t552zCsBJM_FCdOJ40P9e75Dy8mGmgzLN97yukxsSlhXZp-EwCaN6Z1sS17N_tocunzad4EhEZwDR57A9cXiB_rqSN1PragGc2E7CArywz3w5GLgDucs2T_4s-5nBILZtTQaI6OT0pHYhpLt4Ot2ftZmgJEmpgMVwBfiLeLT4L89qEzCq2HAGxrqGe8NfW0Gh4M9STZg6k1JLL3jgdnuuK_ifh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار تو تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/IranProxyV2/8939" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8938">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
انفجار در ارومیه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/IranProxyV2/8938" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8937">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciV0AlbFxroNuTT_IUkeMIriWPjObELzOuA8r2m1_gjahwenvou8pZ4UobuKBQIDQBZ76RMrmAGIvCMUHOx6DadOK-KXsBbgi4-5CWqzpP2KZ7TDRCC54TF7iWxwMcSpW6_0wDV7Ssbkt-TUy2MGSiTnVYGGHujPI7HwsD5fkM89NbUtccJeuAN1tUtquA6NOCpa4DM2jhnk7psdINqK3rkoCKA8LJi2vqmwpRrw0dXA65v1EJItN39Okc825o-DpTtz7h4sE_58chxslLZE9GLPHPlz-A-2p_LFORqB92NP_NbSG--9beSvcASjr042wwE4U-rif-efdGjhu3TOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شاهین شهر اصفهان،ساعاتی پیش
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/IranProxyV2/8937" target="_blank">📅 04:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8936">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
کانال ۱۴ اسراییل:
جنگنده ها دارن وارد آسمون ایران میشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/IranProxyV2/8936" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8935">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OY4Dm8Lwih1_5Q3mswXcZpQE_1yycRDdci7BgIMnVw4NrbxcAOTgKotXKimkHAgeYEDO-kGsJfQWpIVQPEWAK3Q9PiKS_8XgnH1KlWS8c3hnNK71dmqOtl3PImBMrvzUfO_4TKqPjLq_abYjH3D52DHYtbEtCUQXQxualnLO6nvUTaIjUwkyA2aPVG6pzYjqmTShfTN-Tt-yvO9EQPvsOXlXoWJEnI3OzpLTeffkIaCtKfuA2FL34w3U8Qjdd4hIMDeZHzU8tGrW7oSgHS8gUjjxgG71tYndzAR39BoCUIReSPtLJNuFtmD5b04IMUgQd5mddg8bcQ7Re1D9hTpRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یا خدا اصفهان رو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/IranProxyV2/8935" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8934">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KICY_HfxRlRP1z0oBWKvCh9l1V4R1sDRYKLimYGnsIy-00lyLhNODqE7qC9YL_VmVhbEZYzhYNaz1STo_ExDKOXX14Km2w48ur41yYZ6-tnxxvXuTzRVRYkxGERb1Cw3TnDisZRZVPemBrimGiwlXfT6qKGXymywO7iad7hL6AZH92c9BV_45PE_A3otNLHp6Xpq9UQGqEghQElYs_ZsWMePAKkY2ajywLd2ClXkH5jsCMBP8On4KBkVTn2sxAZ9dR8tPlbtkrnhOq33GafZ89gyIn5ktkWBjvI61nquZ5ldhlg4Z2aw9Z9_0kleMaI9Da_tjZPtHgkQ3FYnX7DHgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نجف آباد اصفهان هم اکنون
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8934" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8933">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پدافندا راحت بخوابید مردم بیدارن
😂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8933" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/IranProxyV2/8932" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8931">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
همزمان تهران و هم زدننننن تبریز و زدنننننن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8931" target="_blank">📅 04:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8930">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
اصفهان و زدنننننن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/IranProxyV2/8930" target="_blank">📅 04:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8929">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏
🔴
فوری-سفارت آمریکا در اردن با صدور هشدار امنیتی اعلام کرد گزارش‌هایی از ورود موشک‌ها، پهپادها یا راکت‌ها به حریم هوایی اردن منتشر شده و از شهروندان خواست فوراً در پناهگاه‌ها مستقر شده و تا اطلاع بعدی در محل امن باقی بمانند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8929" target="_blank">📅 04:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8928">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تنها حمایتی که میتونید انجام بدین اینه که ری اکشن بزنید و فور کنید برای دوستاتون پست هارو عضو چنل بشن، ری اکشن قلب بزنید رو این پست ببینم چندنفرید
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8928" target="_blank">📅 02:03 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8927" target="_blank">📅 02:01 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8925" target="_blank">📅 01:58 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8924" target="_blank">📅 01:56 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
