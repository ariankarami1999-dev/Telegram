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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 01:38:00</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/IranProxyV2/9034" target="_blank">📅 22:09 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/9033" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/9032" target="_blank">📅 15:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9031">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
مث اینکه جنگ فعلا به پایان رسیده، هردرطرف از موضع خود کوتاه اومدن ولی البته یه نکته بهتون عرض کنم که این شرایط فقط تا پایان جام جهانی فک میکنم آتش بس برقرار باشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/9031" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9030">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:   نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/9030" target="_blank">📅 14:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9029">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/9029" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/IranProxyV2/9027" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/9026" target="_blank">📅 13:31 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/9025" target="_blank">📅 13:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/IranProxyV2/9024" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9023">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=s3.mowork.twc1.net&port=443&secret=ee90872f20ccc37e3aa2681602f51df71273332e6d6f776f726b2e747763312e6e6574
https://t.me/proxy?server=s4.mowork.twc1.net&port=443&secret=ee3e9cfe9af4494731b9a566075ee8c3bc73342e6d6f776f726b2e747763312e6e6574
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/9023" target="_blank">📅 13:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9022">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
vless://a78bf929-6883-48af-902d-7737793eeb17@hu02.sonicsonic.icu:443?security=reality&encryption=none&pbk=z-TKWOWgZLfzQ-wNdwXQqVwaUgCmbchM2Xtrk1NGynU&headerType=none&fp=qq&spx=%2F&type=tcp&flow=xtls-rprx-vision&sni=hu02.sonicsonic.icu#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/9022" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/9020" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/9019" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9017">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
براتون پروکسی نت ملی و اوپن و... میزارم، حتما ذخیره کنید و برای دوستاتون بفرستید درصورت قطعی اینترنت استفاده کنید تا بتونید، حداقل کانکشن رو به تلگرام داشته باشین
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/9017" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/9016" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/9015" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9014">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
فوری/نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد  بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
✅
با ما اخبار جنگی بروز باشید  @russiamilitery</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/9014" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/9013" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/IranProxyV2/9010" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/9009" target="_blank">📅 12:16 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/9008" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/9007" target="_blank">📅 12:07 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/IranProxyV2/9006" target="_blank">📅 12:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9005">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUSluSswYh9rWdGWaFO1xWra5tufGdXoZimHD7sZkAiBd-beYZXMAUgub2qT8qoW5koUpEdFcqxgCbuSsxqz4zWBoZA57eZSkNI-1n-jH3mS7PvrGDEHVLdN9fbZ2ATXFi0weFbH_JZYvQrLSyPdfxZkCN2YMj22114iix8_80Cg02SD5DDH7FGsxJbwvM6lUlJG-Afrg3pnrL_jrgyEpWH4vTHDAM35WuOxC7626GVXNnolJepZwWFtbhdJBi7S8umHfNvqq9BZSS_VV0-oGjTJjE7Jsit90RO0GWv8ZhI5rwpP6Il4Wd0GTA42_SVbZztgBRPB_bOSdHoLZnz2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون تهران
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/9005" target="_blank">📅 12:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9004">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhexqMjbtjv28n_FYAQdhCXeAGPG20FRALhmD1PhtaZEF6fgTc2wbei__GrUedJmuwuJJjRTFs_weYQI2lwdLtgECDf5IXXytXvWYnBgio3CAR0Fpl9UqWoqKQfzk8t1iGwotgt0v3fZEAVsB4P4zDEaqvQbgre36pDu_UHKF_ouNiQw1q5xkz4Qi_sYWFGoE_t6JQ91fv5PyQKcgVP9GF5bhUfz36uPVll49_uVig2ajS3DFsInJ8gqjTHPgzwc_u8grZL5ULu6z4wD87AXSv1gKCWjawdlXbemmzpiavZPKSyuiNzuEFC7EKBx0pNnrzTQTiolLYMjBVIv1vPTSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تهران، شمس آباد:
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/9004" target="_blank">📅 12:02 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/9003" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/9002" target="_blank">📅 11:59 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/9001" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/9000" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/8999" target="_blank">📅 11:54 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/8998" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8997">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
تو اکثر نقاط تهران، پدافندا درگیرن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/8997" target="_blank">📅 11:49 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/IranProxyV2/8996" target="_blank">📅 11:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8995">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری-صدای انفجار در اصفهان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8995" target="_blank">📅 11:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8994">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری-شنیده شدن صدای انفجار در اسلامشهر و ملارد و کهریزک و باقرشهر
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8994" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8993">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری-شنیده شدن صدای انفجار در غرب و جنوب تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8993" target="_blank">📅 11:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8992">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB8H3d6Qoiite3VffpQIk3MLjA13cCtvwgxCdIThDS661UUQXtGus4RqU1-yfuA9gLGKNoCcskWvu8fK0YjVlYFtlKO7Oxe51lZ3fXr3tya0fuokzsLwLU0qqquNUNtGoPRNR2N25_K-aRFRRU77Y8TuPAH3ODM0wpnTmokC8rl0MsUrchHHlnfuvkqFvB6fPltlEHkgWbT94MHdvd-MHc4mg9kdWQQDcBuj1Rhhx9raI1_svJ_RXMz0yJteYIvhN5mjPz4UqVD3rSAqhhJLh_BFtKhpDXmA0JMF-0CnNKeo6hBbgrmDzIpd9fkOY4OtChgXsSg_VSGmUvdenDrXDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وضعیت آسمان اصفهان:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/8992" target="_blank">📅 11:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8990">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سپاه: حمله دشمن به صنایع پتروشیمی پاسخ داده شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8990" target="_blank">📅 11:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8989">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb9354396b.mp4?token=Q_uf9sqMBLfEv8fo48tiOCCClMnuRtDArDB_DzD-555khtzCENLfZaPbFNOqoCp1NP8xfP2fc1HIH_-uItnpACHld82P46jzAkdsD4Xr9Q5tN8BbR5O8BXgBD0SpEhKzTfcpox6MZCDL3OdLfWEvDMC_jqkvT0PRJKBlW6wpn56Tmt28aP23KXqaT6ugqtLEGPCES5POuy8RGOdPk0yjrjSGWBjbUX3qihkujP5ARtGja3IseEAuwun3sy__vBDo7h38IpaXOHOjVRay3Cm7Cq_KlxeTloD1klg7Ysb5_2h8kzdxA4GuDD7-17UTPhPHYiBjR5JC7OFjaXT-9jGZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb9354396b.mp4?token=Q_uf9sqMBLfEv8fo48tiOCCClMnuRtDArDB_DzD-555khtzCENLfZaPbFNOqoCp1NP8xfP2fc1HIH_-uItnpACHld82P46jzAkdsD4Xr9Q5tN8BbR5O8BXgBD0SpEhKzTfcpox6MZCDL3OdLfWEvDMC_jqkvT0PRJKBlW6wpn56Tmt28aP23KXqaT6ugqtLEGPCES5POuy8RGOdPk0yjrjSGWBjbUX3qihkujP5ARtGja3IseEAuwun3sy__vBDo7h38IpaXOHOjVRay3Cm7Cq_KlxeTloD1klg7Ysb5_2h8kzdxA4GuDD7-17UTPhPHYiBjR5JC7OFjaXT-9jGZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم‌های اضافی از موشک بالستیک ایرانی که در نزدیکی یک شهرک اسرائیلی در کرانه باختری اشغالی اصابت کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/8989" target="_blank">📅 11:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8988">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88608e0e82.mp4?token=ZhpnHO-DpOEgU4N235b-njrmAOawHRxmn0GbIqjVyyyoFWJXUj6K2JS-sJFKjRSsDWjlBb6OIYyMLraNSfy-JqGHsGn-93JotR8ERiv84rcwjqbRb6hrH29BkzXlMJyJ12t6u3cYoPcW4GmWIKQlBIiDZitvK4XkCkuhHfuol7IpXFVdzAKPIqgnbyj_QbvEduBiciguwCT0VOdDvxZAJhBg-BZqzTVJENQmYN511DA5REvLZATNeNALKHLzb1bgZ4qLHf2n86AjtA_RYbfTubJN7EFDGGV1ZumVjZbIernC2K4dfMf7473N0QcoJhscOiJBpVuKbk5UxEFPTWslzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88608e0e82.mp4?token=ZhpnHO-DpOEgU4N235b-njrmAOawHRxmn0GbIqjVyyyoFWJXUj6K2JS-sJFKjRSsDWjlBb6OIYyMLraNSfy-JqGHsGn-93JotR8ERiv84rcwjqbRb6hrH29BkzXlMJyJ12t6u3cYoPcW4GmWIKQlBIiDZitvK4XkCkuhHfuol7IpXFVdzAKPIqgnbyj_QbvEduBiciguwCT0VOdDvxZAJhBg-BZqzTVJENQmYN511DA5REvLZATNeNALKHLzb1bgZ4qLHf2n86AjtA_RYbfTubJN7EFDGGV1ZumVjZbIernC2K4dfMf7473N0QcoJhscOiJBpVuKbk5UxEFPTWslzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از تأسیسات پتروشیمی هدف قرار گرفته در ماهشهر، جنوب ایران.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8988" target="_blank">📅 11:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8987">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
رسانه‌های اسرائیل:
پس از شلیک یک موج موشکی از ایران، صدای انفجار در منطقه مرکزی و تل آویو شنیده شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8987" target="_blank">📅 10:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8986">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
اتحادیه اروپا: امروز تحریم‌هایی رو علیه جمهوری اسلامی به‌دلیل ایجاد اختلال در آزادی کشتیرانی اعمال خواهیم کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/8986" target="_blank">📅 10:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8985">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
مدیرکل بحران آذربایجان شرقی:
در پی حمله ساعت ۵ صبح دوشنبه به یک مرکز نظامی در تبریز، هیچ‌گونه تلفات جانی گزارش نشده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/IranProxyV2/8985" target="_blank">📅 10:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8984">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فعال شدن آژیرهای هشدار در اردن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8984" target="_blank">📅 10:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8983">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf8i0MzrdgFh3pee3scXyVp9uEc7K1FfRGnc0ZU6b58khECRIfVYcezhqm4svtW-f-Hy_Dzp8YwyaoFroDD1WdkSleSrZbfBdEQjJubtnBFUsvjOELjjZC5etDxd33AH0TNwlSYaAiZCTMXCBGLrneh7QB8efoq0DgQxcGc9V5lSWZQUtC_4B3GkmiDM83yY0SgqvcSdesifOwJcss0DOPZdUbYZbmQ-GWt6mV-MxASBUP_Vnnxy92PII8eOd8CoKvMJ6UfEV1zIWP3UKRD_OP-aQ_sD9EyAqhjneasKc4LZT6-obulHZjCrMl8fhZz9f8UeSXdk74P0E7c2vO9xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت جالب ایلان ماسک: جالبه بدونین اسم تنگه هرمز از اهورامزدا، خدای آیین زرتشتی، گرفته شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/IranProxyV2/8983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8982">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
فوری؛ موج جدید حملات ایران به اسراییل هم‌اکنون
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8982" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8981">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇾🇪
فوری؛ یمن تنگه باب المندب رو بست!!!!!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8981" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8980">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇷
❤️
فوووووری؛ رادیو ارتش اسرائیل: تشکیلات امنیتی اسرائیل تخمین می‌زند که در آغاز یک رویارویی نظامی است که چندین روز ادامه خواهد داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/IranProxyV2/8980" target="_blank">📅 10:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8979">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
⭕️
🪖
به نقل از منابع عبری ارتش اسرائیل در حال حاضر در حال عملیات در خاک ایرانه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/IranProxyV2/8979" target="_blank">📅 10:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8978">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
سپاه : عملیات نصر شروع شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/8978" target="_blank">📅 09:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8977">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
انفجاررررر در کرمانشاه
گزارش منابع داخلی از فعالیت پدافند در کرمانشاه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/IranProxyV2/8977" target="_blank">📅 09:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8976">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
⚠️
سازمان منطقه ویژه پتروشیمی:  دستور خروج اضطراری کلیه کارکنان روزکار از این منطقه صادر شده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/IranProxyV2/8976" target="_blank">📅 09:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8975">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🆕
کانال ۱۲ اسرائیل: طی چندساعت اخیر به ۲۰ هدف تو ایران حمله کردیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/IranProxyV2/8975" target="_blank">📅 09:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8974">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
کانال ۱۴ درباره یک مسئول اسرائیلی:
تأکید می‌کنیم که یک تأسیسات پتروشیمی در ایران هدف قرار گرفته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/IranProxyV2/8974" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8973">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXZqC8C3R28cNaKNnY-blCcJojEvvYMFyCsuXvCC0JoImgiQ3LHj36Bu6OJ3h4qpHhdMo3tg-NOznBzFpSX0GZ2RmcsXR7Z9MXmGrd1sfEUHJhA0FRNMuvOlBiLDUND1fU6p2L2JviVpgKxtw83enCsP4mdx357HO6rBErcnVb0pKFcOUxgFD-T0mj6vmAdmA2mT7ewHUVpd_9VL3pBzjFrZDSDlolFhqrxBOlvmNNEASoEM7DBusvJyIJ-ozNVKwMktefeXOUyKbSFrB6fUBU9lG9gQSu6LnyHlbAQiUFM5N_hbIl2W9d-Z7QU3RpBbAeoTpZnu8MDzRmqx5-UpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور مورفی:
این جنگ برای آمریکا تحقیرآمیز بود؛
ترامپ دیشب گفت به نتانیاهو زنگ می‌زنم تا جلوی حمله تلافی‌جویانه‌ش رو بگیرم ولی اسرائیل ۲ ساعت بعد از این تماس جنگ رو از سر گرفت و ترامپ و آمریکا رو تحقیر کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/8973" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8972">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V56EN5fUQxIQwBERSEZHRIpz0_HT1k3R23XMc5TdkbYOw4lmyzT_Kwk_xHtVzV15l6C0WOHxSgwfTOGSjtWRHjPtn8L5dKGwNTD-ci5AOr2gSWkbAg0VJGmWN8oIFpzDFNKW9bS23RFjEldiqNOiQVxbSu-SUTFl7iFcgWcEW9w0xFWjliBQfRPh5DskXxKLucU5fMaCrAUxCaH-hu3EyOV9vOQ53IW3e61qEPaD6IQGYjhrrcigPT3k7ZNhnhBKH3OANvv25ZemBBtvXXJnfSESv9tCYMG2AAJZGpt96N92Z8nIUq47ljoNyZP7_lxpEAC231NiA2KPK2mjyiVbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم
:
سپاه موشک خیبر شکن و یک پهباد ناشناخته امروز استفاده کرده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8972" target="_blank">📅 08:28 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/8968" target="_blank">📅 08:25 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8967" target="_blank">📅 08:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8966">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcqWleFjGTC1n2j8oUi9v2y8izxVEabYDsf394h6jvOqxIcdG7vBIiTkBOsVCtl7uOsKNUg4TjoZZf3EtgaIDoWoCvLTCy9Oabwws1JM-DjsGj0Q7pQACpXa8zPcl-nA6C0o_U4eHVJ-T0FsNx-yM6E15qDkNzswSH27hXzYi9YypnezAhCvBaH59gf3HSFE1jB3iP22Ut27tmmr4Dc6j5-WmDzMWI5xXnxtOowsZRJl2X0EMecyU4l7UQOolrRP1SJrc18_66Nc8u-ZJWuEHYeqgXW9PZY-85gSutGMwfnWzqGzd4F3gH5lTS4AHssSqCNvHOdqkpk9WIlGyKqbSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه وزارت دفاع عربستان:
دارن بهمون حملات موشکی و پهپادی انجام میدن، دستم کم دو انفجار نزدیک شهر ریاض گزارش شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/IranProxyV2/8966" target="_blank">📅 08:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8965">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رادیو ارتش اسرائیل
موج جدیدی از حملات رو شناسایی کردیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/IranProxyV2/8965" target="_blank">📅 08:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8964">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
اصابت چند پرتابه به پتروشیمی کارون ماهشهر تایید شده و بخشی از پتروشیمی در جریان این حملات اسیب دیده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8964" target="_blank">📅 08:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8963">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc73ebd9af.mp4?token=BvW8h4AJfhCgKbY9fXT1u51pHEADVwAb-VId_90DDtqk8yT3kbwhOBtDSlNEU6eEzgwuLbhELzWahSe0ii00qP_sEaqrUnB112urUbUD_Yi4aIjBw5fC8OX1i8P95OZFKPOqoj_m6MJ9cDpgJOVntVOiX8W9w32LjAZDDBQNpQsfIAALltd3dj3jlNXQt7ZAP5mXj1Q4Crf86A5I05JIM6fvCWb0A53vIhigjhGuNyScLbD60wEhNW5wnriHUh_swRhvxotoKQgMZyDIjZPm_yp6-68RMY8YwQXdvPw-7zNOoXXuFNPL_VZqfm9ZukqfxfzJku-ZT07LV7P7q4PnOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc73ebd9af.mp4?token=BvW8h4AJfhCgKbY9fXT1u51pHEADVwAb-VId_90DDtqk8yT3kbwhOBtDSlNEU6eEzgwuLbhELzWahSe0ii00qP_sEaqrUnB112urUbUD_Yi4aIjBw5fC8OX1i8P95OZFKPOqoj_m6MJ9cDpgJOVntVOiX8W9w32LjAZDDBQNpQsfIAALltd3dj3jlNXQt7ZAP5mXj1Q4Crf86A5I05JIM6fvCWb0A53vIhigjhGuNyScLbD60wEhNW5wnriHUh_swRhvxotoKQgMZyDIjZPm_yp6-68RMY8YwQXdvPw-7zNOoXXuFNPL_VZqfm9ZukqfxfzJku-ZT07LV7P7q4PnOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از موشک‌های ایرانی به یک مرکز نظامی اسرائیلی در نزدیکی نابلس اصابت کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8963" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8962">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqRdYK5RDWaPej7vM8a1xDBto8ME48UcyMNcZrEBML7r2hsK9oLYkHOBwJalK5jG6DVeOJONFVfYPLxC1cv4mdyOyFPYBrv_vxlueMHplY71gKHSECEU3BNU3JBFSuInFtwQUkE-5TRG-YGIKXCh2jB1Vd_aUXCoX512217sefcozIIa9T-hhS3OYuWpbwtI97jiiJqncOQv3QnEgVafOmlHtA_oCqdpP9HMDWb3wjl0IG1P-Jf7Yix7ick2GEAIFOd2tjLiwGhuMx9KVkC_z741g84Y2Vqw-Tpa8O1qY8ns4S6HTrK4UGIbP5LzkQUZJHkfYb3qwSB0GT1sN2ibVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار اسرائیل:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/IranProxyV2/8962" target="_blank">📅 08:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8961">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
مثه اینکه موج جدیدی از حملات ایران شروع شده
از اصفهان ، ارومیه ، خرم آباد ، کرمانشاه ، ماهشهر و آبادان موشک پرتاب شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8961" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8960">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDqePdAC5Ricsg0bUkFiFXzKGpS1QiUvBE9fyH7S7o9cAKBWz65lOzACEyFlebdUYUPeRqPJWoFChKcee-pMKxv5NevjajP4sMCQqjsjiX0QvSgbMMn5vPnGNmTobXghD_qZ8-Ba0iAyNX8E0odwxcrl9MZ0mfbRZp4E_satJ4YPC9aANq4DGK0xR99tgfnGnzHfzIBNEFVcslBU7D1GIymoJZgeaeUIBOQNnkzyU0NNa6PZWI2XdOx5RSJTDR4TaOeHWjbKujZ_eIhKGjMBgrXZaT1EudfblilEHlFcVsmEsKg8lNh-n-ioNtdiH1cvBTTEvrM1-M0kHp2Vg76YyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در پی به صدا آمدن آژیر خطر در اسرائیل، مقامات این کشور گفتند که یک موشک شلیک شده از یمن را به طور موفق رهگیری کردیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/IranProxyV2/8960" target="_blank">📅 08:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8959">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇸🇦
شنیده شدن انفجار در پایگاه شاهزاده سلطان، الخرج عربستان  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/IranProxyV2/8959" target="_blank">📅 08:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8958">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇸🇦
شنیده شدن انفجار در پایگاه شاهزاده سلطان، الخرج عربستان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/IranProxyV2/8958" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8957" target="_blank">📅 08:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8956">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
کاخ سفید:
این تنش های بین ایران و اسرائیل هیچ ربطی ما ندارند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8956" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8955">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شبکه «آی ۲۴نیوز» اسرائیل گزارش داد بر اساس گزارش‌های اولیه، اسرائیل تاکنون دست‌کم ۱۵ هدف را در نقاط مختلف ایران هدف قرار داده است. به گفته این شبکه، از جمله اهداف مورد حمله یک مرکز تولید پهپاد، فرودگاه بین‌المللی تهران و تاسیسات راهبردی نفتی بوده‌اند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8955" target="_blank">📅 08:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8954">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هرچی دارین سیو کنید احتمال داره باز قطع کنن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8954" target="_blank">📅 07:36 · 18 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYvdRecNLxrqDOtxmo7zMmD4Oa5uFkYwxVvRVAimdvFGm0h_HdG7MwClk9840HbzxMb8K9hPDI7BYmA9A65FUL-AjuhwKJcjPXLT_xSmdkSQ5F-g_Sb0LTTUkBy-KXkeWqIBFewgvAKK67WjDuKZS4UKJ4ntKFtN_NMR5t00U2mUw7cYww4u-IQdcaW4EXjP3vRe3-T802qP22KFVhwOoxc203o4XBuBDcs0oc2bpkQEoWpCDpxCXlVYYCVPip7Vedy8fzdZVKNIx2h2hS2Sj_LYEvt6Lzm8W1SIJ126H60NOROgf8WW5rziB47sqf8qDBUcjAx1WHV0L0bBscbLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری-خبرهایی از انفجار در پایگاه موشکی اصفهان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8951" target="_blank">📅 05:26 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8950" target="_blank">📅 05:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8949">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
تا کنون تعداد اهدافی که اسرائیل به آن‌ها حمله کرده 15 هدف بوده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8949" target="_blank">📅 05:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8948">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
حملاتی محدود به چند سایت پدافندی و نظامی تو تهران، کرمانشاه، اصفهان، ارومیه، کرج و تبریز و چند نقطه دیگه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/8948" target="_blank">📅 05:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8947">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری-کانال ۱۲ اسرائیل اعلام کرد که فرودگاه مهرآباد تهران مورد حمله قرار گرفته است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8947" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8946">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvPbgflmfBtIJZjg7uNXsmp9_x7boXuqhosniUd5qyH8X79WsEFvZLZRPiielnjReXI4K3WUrZb4zEiJylhhXt-_K4iuYUuBqJzXmEMq3y-A0BJ5ZVT6mQrfz61UQhuwAcXjgZifqx28NBHc5aXuzImDkQYW-67P5o666HCnJDItraEbylguK77VK3tYFytTIagi74Wvw1XhiYkMZE9fz5Zr9D6P1OCP0jiWou5bKEaCI7klzLICK3g5IXH1Gd8toe77ypbGh4ZwPhVTNEpbF8AHvfTbEv_1wWJ887vpP18ywYtcMRy2SM-D-B4wydIk3Eb1JmjCfhgJBfWAIZtCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
حمله اسراییل به غرب ایران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/8946" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8945">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
آغاز حملات سپاه پاسداران به مواضع اسرائیل به گفته برخی خبرگزاری های محلی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8945" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8944">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOF4Dax3ewn04w27Dx1LC0oVfhuwdFNnMWtwtE_Rsxz7jEZcbnBSdsnHJOfI8a5MwAXSDBr8M36mFqBrZV9O03LW1bioW8RfGSn1azMMamACsGaet-csCKEaui8jyUfE-NjUfJ8AleDqKSqGvXMy4V0gjgcmWBMDcJtsDdwMuU-ZyAk8_fY5qA22-sRZRtxf72hsutP-IxIHWFKiuc6lmfDeynsGas6_h5LwVW0PJr5rhm_UEm-gfksbdjZo3yITN6hQJyl0oAVu_KYr49K-fe2dP8WRpXT5LoyuwMzvFLoN7foK2iftPZWshrgCprZykKJZ0UV50gMZ0SAofNs36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به کرمانشاه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8944" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8943">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
کانال 14 اسرائیل:
نیروی هوایی اسراییل با استفاده از موشک های بالستیک هواپایه و موشک های کروز، از طرف دریای مدیترانه به ایران حمله کرده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/IranProxyV2/8943" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8942">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVWIxAAd0Zo3N0v0etEqNzXUhfB2uvGLhaKBek2hcwQzOQDHPoHxQubSSy7PxB53I7vy0txE68nw0Uz4PrG4Y4vULJ9NOG2tKw3P5St-vetI_nBera5IU2y2D3UZZh4ezEeGf1iV78ScVXn5apZ5qOerRaDhHcEnkff0tG7kvTlW88I_CGIqJq2B2DW5LhYvHPowO3bPrhONqO647pwNd-QFnsfPEF2SnI2_jH9Nh9eWhBVc6Q7RyYk6jUFLxtLs3WU9NSBarSRjW7VrHOnVUcXDn3gAFE07YKkamqahoMw-sJ6cSVYWHlPap4rUtHhAEeHJlDfnUmf-D9LMfgljMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کرمانشاه رو هم زدن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8942" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8941">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7ikv_rnF7FFeITl4u8e5kL59FeDFQR18bfdlxPf-x79FklJZz89RoHZRSd364zh6FXCfMvQGnmv8oEgS9f9UZ17itcqejn87Y6-33hfUhSOd_ZYIgEqhMa7uBSrLofwWpPAlrnq9xaTHRgXw20NmPRq0H3OzznR-5MESlElr2QYP6NGPodWksj7EF1FUJP_MZLEH64FfzRnJqgdhjYsbTvu1Y7gAvZh_KazPWeEXmpPmAJNq6F80apX2G96mouFa3MvuMzKel2jAKaliI4XH_T475VHcCiTzrpBfqY0-gau8R39MtfOXi_AQWV9wrO5vcaCdeih_t5Nls4MuifO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه رسمی ارتش اسرائیل: «دقایقی پیش، نیروی هوایی اسرائیل اهداف نظامی متعلق به رژیم ایران را در مناطق مرکزی و غربی ایران هدف حمله قرار داد.»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/IranProxyV2/8941" target="_blank">📅 05:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8940">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKmk4uTUiQzIOV8qAG_apW9gXOVlo95Ru7poty4D6Wqpui7TD3ALaq9oHnvMjqHWFMw4lCSBb8CRohe9U_H1J06UQcV2lHUUesXl0Qrg4xDT5WBM6UqZFBPRx_G8rkYLRGwgz4yY8LeQqhMml4kvMqHbOwRrojRGNkezzLk6DGyK_PQJTa7cC-lhX_AJZSDYua2wJ4CMnmdx2Mtkmoo-f8Zo7xq96Ymx3PLFJvY3ZAk4wR-7jVsVbCAledVoNQ1S6F9rHAvYvRKG3GYMeOd5z9Uo8JqJUIJURB-M50PGZmLIcc09D56QNz4dUuMAZNKvh0sQDGvmFZNYOup5NyjEUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صدا و سیما حمله رو تایید کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/IranProxyV2/8940" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8939">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTf1L6GJU5kCXD8cQokjsO6O_fs3F6n2vDv0Vbtw9n6Qey7KjlGU_M0fQmrBiuCBaPuCfWS2HKJZwmTu2R-LUrKS0-gMmsf1BdUTaZKeXVS7r1FXoyFjmJ45Ogso8b81rikKOsBrIG4z08fsH3UzTBlHzdbTvBp0vUZ9JRx2SCIX2YKZJq83t5frW4uVDLqlcsbxGZPBQibDqDJ2ZapugXX4WXVfrHjucBJSykHv4Vz101I2K8CFbbmLa2JQSOP5XB__deUzhEnfnkijPWtrlYWV4kJSW8BxcTJ_Z822viYOuxj_1_Bi5sq9a1XWcGRJbF1KToGiKWcmk4stQN_5Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار تو تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/IranProxyV2/8939" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8938">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
انفجار در ارومیه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8938" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8937">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0F_qTs1_du3A8Rss_uJZoX2zY7X-vEo_ajxh2gIhHolFv5ycFdGTcwhqNRDEXBoe-QE5RnUxEcxEzWrMVppckGs_WkDTQ7OSz1RH5HuTVxiaODwuLWm_q9ji2ar6fnpuMZG8A3ZfWL4bxM1j7VoLFFscf2abvWBIOXANjovB9Juj_VokwrolWXylHBG2nmt1Mv1ZoiUXnh1eUOMmVaOGLlo8E_q5tst_qf32iYly1NZl8xIvsuwomLp21451mhtV2-2In17ycF6kHGSNTITYTa8NnQbt8862MAFw4v6KoN5EiE6W4qWBjZzwYNG47WXomyxC_5HtC3usjeCzPSS3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شاهین شهر اصفهان،ساعاتی پیش
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/IranProxyV2/8937" target="_blank">📅 04:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8936">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
کانال ۱۴ اسراییل:
جنگنده ها دارن وارد آسمون ایران میشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/IranProxyV2/8936" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8935">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgIrTwMpZDbsItJig0d7TYwGhS3-z0zm2BSLvVr-KLioFFc7mgL6B_bGJSL5ljSgvSGfLmsNRqJeytolBgslx_HF_25_tjOmHfyJ9dYJqpv0QlxuyL0bQm_G5SsVQ0ywQ3AyO-7jvIcX352N7GUl__LDHkIvZ0ZuyWKh5doEIurNTurmGZ9FLOGmoO4gAH1uCh_BSlaVhT7HAqQMgRoFj9ipDDrePZ2EVc9oFvVzcHzmmysldW91-xP3SVHPjXiEX1oLk8bLpAJzCagCxhduqVOnB25zvj6IfAS21GPHgpLZ7Hoz2v4HVuZ0wDSofFp1MJG1uhWXtbhChXLgiAAJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یا خدا اصفهان رو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/IranProxyV2/8935" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8934">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeQB4CoYBcZ7vygneAvjkFBF6q46-A32kcxluw_WsHCE_Z6S0XP722Nl7Qlqz2vQ-v5b1pdNhCgKvuK6k4KN_YQ1vzPjkfjUVIev6TMtEzAsDfUY5w9t6bQ7kTznbbFSlzEZH5HUDPYHyGt5PpfZW1e3CzeiKmAca5Jgi9Sd-Co_v-UC7e_Immt-x1p6SW26-jO4bCgfLdKBbAVXZDUXclndmpPeZG4WU8Je0x5frDNVg6osQHHOOyFQQzFdPJL4fKSge_cQ4sORhqP2PtnuG4WJbzu4nVg3QMc5jRd7jyDKK-WUAF-QOrwzqgtxaUi1M5xH1ZLyytHht6Xmyg8pVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نجف آباد اصفهان هم اکنون
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/IranProxyV2/8934" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8933">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پدافندا راحت بخوابید مردم بیدارن
😂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/IranProxyV2/8933" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/IranProxyV2/8932" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8931">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
همزمان تهران و هم زدننننن تبریز و زدنننننن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8931" target="_blank">📅 04:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8930">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
اصفهان و زدنننننن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8930" target="_blank">📅 04:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8929">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏
🔴
فوری-سفارت آمریکا در اردن با صدور هشدار امنیتی اعلام کرد گزارش‌هایی از ورود موشک‌ها، پهپادها یا راکت‌ها به حریم هوایی اردن منتشر شده و از شهروندان خواست فوراً در پناهگاه‌ها مستقر شده و تا اطلاع بعدی در محل امن باقی بمانند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8929" target="_blank">📅 04:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8928">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تنها حمایتی که میتونید انجام بدین اینه که ری اکشن بزنید و فور کنید برای دوستاتون پست هارو عضو چنل بشن، ری اکشن قلب بزنید رو این پست ببینم چندنفرید
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8928" target="_blank">📅 02:03 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8925" target="_blank">📅 01:58 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
