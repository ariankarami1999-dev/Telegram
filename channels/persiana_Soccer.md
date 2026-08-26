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
<img src="https://cdn4.telesco.pe/file/MdqPU3XFyX9jjG284dRWlYyXGE9sszFMwzGfrpeGEXtW1eoGQFf-QlW7F5EMTivSaAjwozohsTgdaaNqMD8606iyouqbkjCwWzRLaCxTk1id6ZjSWBkWvhDetE2dd_lNlPRwKtT5KkxhxYCny0dMeEXfmufUUF3_t6Bttkbm8WPAlPtN0ChUpTTbAR72m5ttvC8tNTAZQH9_ayp7qtknbFFm7HOelLXM0XX1o3A3ofVS1AZhBsw9QommC9LiHmIkfOcDcrue_gRrKJYGnunrtY3Y9IF-QXbP2OphANsWRgQQFsU-IUgav6gw9bGyevQE7oKOXJ4su-owlKTWrU9_iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 624K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 08:00:33</div>
<hr>

<div class="tg-post" id="msg-28501">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKtXz-E7OO4jmIpxw8wdk8-IbAyRDUYe5yEn2bk_QrII-X-HFZbGwFGiyNaz8wavQ1wVKrQipjvmx0ay3WvgfoXiHxuZJoK8L7il-e1HRaFDxNu8hWYZDNG0RMKqZPlM78zdFhY2b0BfCgdVGRVjg-1ZouQdwncyVNyT8CWyY1rMlMcUW9PKNv-7Jdsed0u3psYuHk95XB0NSyYVVG-7Eb7Oqycl_AjKZUygLdKVRIXVfbHRuT-0I2h4KK3RK8nDLZHkCvjVKK2TsNX-67FuObWIaJZ-UOpyQetpZsiukaNqap82H-Hy2391_xaP4x-2zM-t_CbJun5SkxalV9G45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
مارکو رویس در گفتگو با رسانه‌های آمریکایی اعلام کرده به احتمال زیاد در پایان قراردادش "خرداد ماه" از باشگاه لس‌آنجلس‌گلگسی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/28501" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28500">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMisVKv_4w9X3Xt9Hh0hwEd366lZHZ1G8jHGEyKD_g9wMJTgexlilFX8t7XWDYpXDIlqMK0Q_VVZyU1-hVhnEhZGKzXKJVWl1tzupanTew_CKiqYN8ixll1FGTOZdnQvCrBslPMR6hGEdj4QWp_Xu9NPlvZWtjGavlm-CEVbko_ti0fHDAJWQuqpNlVERcnfENTMQObzINS8KkqOMCC6W0LfEp_xq5kvp1D_iSgbJ937jBy46zZH4Gt_VO0ZwkARHt_dCbX7ekkIBYah4zNEnfiVrePIHSCTogZ4XMxsi-zFIiZMuCwyVnaEqsOsTv6hVk6V7rpBRemjF1YqNAJmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
دومین آزمون مورینیو با نبرد کهکشانی‌ها برابر سوسیداد در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/28500" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28499">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibgdhKmwveuv3E31Za5MjmJtJ792hObZ2n11mgiSpXx0PBY9thjiRD3fcoUES-WVE79ZM28dM1HgSxy09pcq_tsx5-hQzkm2TlNX2L5_0wV0wUy3tZ_UFjPa6P_m1ghBhi0FRHoHV6N2c4XR9IwufNM6LZGNpIfMbVCFCi747UqavnjS2RR2DdcFC5hUPjFPrSAcnFI6EyMfeCj8Aqg17EYX0DzZ_XxYDd3W_J_aoAPG8OOWDIMCiYIgMBml1uzlGyVy72-mmNKutz-tinjJ9-rfjlHIOgqROCAQx5PfRPDjNyHJh1MvxqlsVmO1cxxax1Hwni-MTaeBzp4Z643iTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
بازگشت‌دراماتیک شاگردان پوستکوگلو با درخشش ژائو فلیکس و سادیو مانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/28499" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn4tS1rvej2Y55C8ZFgO4_3GEeNQJFW0EUvy6bJnBBKQLCXcz5axWYA3OMKvhEcQyrOeHH75C-EsQJTDfARJlJlG0XhgtsiL-abkkAJ7r6skYPFi4aKWEfo-IPmZ46n5AMnwlzb0EOc2VomDWEqQwri6hh_1tVwNd2IbEyutoa1knvt-APUf7XzXJ093BcbEnx8zwyI1z_1yorWOEokTQcOWBEbV5-s0Atm2lxUuMljhheZOvVvBao4EPtqgdSe2hgbkJwz5peuY0bww67Gm5thyr0eKY-LOc3W8fRWTO4K8m8anlOYebaugdOPKse8i-4GuMtBX5sLaA14Dg31MqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/28498" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaTNy5N2yow_1J1mA46XluLJjGQP544eZ_NBvIqi7rECJbVDppbv77Kj_b4d4pelZ0qfBsMWd8xTJA_08wOk8_I4IwXFZy09KJVx2CCMYPG8AD2WciPQMPCc7ZFs5f4mNUr3v3HaBGMGsLrLjf64pH4qz-jE4T5O283WLvsFDACm1lRrZCVMadB5LzZvd-dZLPqGNUT1NU2d7WsCaLOYfW7HvLaRUrlsZX2_dkKDUDluNB9340EjgxN2hxNzwu1y9esJMiTowIt4avYSEmCpIjM2F_BcYg0fgh5wNguRWHC8gNvSO2zuNerzuQjHrtLTipy_VSaI2u6LHrp2dZvFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛ باشگاه آستون ویلان پیشنهاد 45 میلیون یورویی الهلال برای‌جذب اولی واتکینز ستاره خط حمله این تیم روکرده و قصد داره با 70 میلیون یورو این بازیکن رو به عربستانی‌ها بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/28497" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28496">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=LlVyYQN8MrbbUyue9_tuTtOTESS8TfmekWudma9eSu3w84vHCVBWT_3IWFfubCSBXm274p_VFbgPLNymWUZEIxz8MVWjB3WDjHzzDJ4mwlK35VeI0oRe3Gf51UxIRtnRQHY4LrxSHE25hRlcX5B1EUNU8vHXdj7voYGdr5Fm_ZlXsx6mioHZyrDoHAghqJaHxsMDEZ5qWBxj7Bw8gwFI20viB5vI-4engDi6XDscdnTmeIsPxuPw_ppeaDfniaU6uFekN9OCPx5VUQrs2w9sKXPZhdxka223-BzcFPCKttUVpxxo2AoiBoFpQ-aLNCE7gWIpyj8kzNZK9YtDEt3jJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=LlVyYQN8MrbbUyue9_tuTtOTESS8TfmekWudma9eSu3w84vHCVBWT_3IWFfubCSBXm274p_VFbgPLNymWUZEIxz8MVWjB3WDjHzzDJ4mwlK35VeI0oRe3Gf51UxIRtnRQHY4LrxSHE25hRlcX5B1EUNU8vHXdj7voYGdr5Fm_ZlXsx6mioHZyrDoHAghqJaHxsMDEZ5qWBxj7Bw8gwFI20viB5vI-4engDi6XDscdnTmeIsPxuPw_ppeaDfniaU6uFekN9OCPx5VUQrs2w9sKXPZhdxka223-BzcFPCKttUVpxxo2AoiBoFpQ-aLNCE7gWIpyj8kzNZK9YtDEt3jJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/28496" target="_blank">📅 00:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28495">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=XQ0FCQyHtnoNsFaYSZ3oDv2drd8WAEr5NN6kxQrFnin5kjyYuqg0J12c1B-e7fNlXVkLwAxH99XAbLs5tRxJVpokozXcpSVAxADkEnBVeckHFDdNm5hhR4bqi3JY2XFEejSPbInNCFEwoGDTMHX-ORE7hvsDE3cuQT04Y7y26NFo9RDZRh9AVIpYoV7WboND0vX5mFHqqXqs2Uo_pquF6tTXmvDPTpL1bu7Ijk2GK_DMR-G7u78pBcmC8dYhBR4Y-S7tWOC5xt8nAYiJiYjo4IXQDF6l3otS-IW4m4pjtGu4gvQQy8b8M9dMHm9By1K6JvFrxmZGrqUgeF5nSZX1qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=XQ0FCQyHtnoNsFaYSZ3oDv2drd8WAEr5NN6kxQrFnin5kjyYuqg0J12c1B-e7fNlXVkLwAxH99XAbLs5tRxJVpokozXcpSVAxADkEnBVeckHFDdNm5hhR4bqi3JY2XFEejSPbInNCFEwoGDTMHX-ORE7hvsDE3cuQT04Y7y26NFo9RDZRh9AVIpYoV7WboND0vX5mFHqqXqs2Uo_pquF6tTXmvDPTpL1bu7Ijk2GK_DMR-G7u78pBcmC8dYhBR4Y-S7tWOC5xt8nAYiJiYjo4IXQDF6l3otS-IW4m4pjtGu4gvQQy8b8M9dMHm9By1K6JvFrxmZGrqUgeF5nSZX1qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز اولین‌تیزر سریال «مرد سه‌هزار چهره» به کارگردانی و بازی مهران مدیری منتشر شد؛ مجموعه‌ ای که ادامه‌ماجراهای «مسعودشصت‌چی» را روایت می‌کند و قرار است از اوایل شهریور ۱۴۰۵، به‌صورت هفتگی از شبکه سه سیما روی آنتن برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/28495" target="_blank">📅 00:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28494">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQUpB5ed7j5r-TKWcdTppiX1AM-Q67x3h3N2fsh4UD-0b8GCC808DA_aGhd5Egicwv313BW-7JXu8gGTj_69ACnvb3MAXQHPaxltkcCUP6dFLgChb4dwnHbcvy3kKJgOpfls4QBwl2_xD-falPiVhu2b_vpMIaj0tcMQ0tMXeuy9odU7NRgVIek49ZKJdALvSjTUxQm0sE7PUZQPGNL_mmDARTs0HBM0QTR6GXXIrQ3MHcl3iIjSVvJN0pLlioqEOV-OCmJ2qNy-7daJUpIwCXr_egpC4sHGm47sscfUJnHTG04MJ5KLuUK_KWxDASLZmrTHjwAOfL-wMUNb7OLIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/28494" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ig9FGP_uulgRNUe5GbDtu1uUJLqb-TV1ohwXyi0p0KUaHRB3Rkzb_U4BZlO1ePO5D1MoU9PMM6v_AaVFitQyR1JxYIBxh1G15eHYG8DYq0kYtKbGE5ayVvR4Rjm8BrVZHuAsGJ5_vmsIJVeJ5V-xDTTyZ3VIXwcvJWwifbzjnPYom2kQbgQcvTaNIWwCse-EdPlsyEA0E6pIkI1JCvAHMs-fheRxYWvOgUTUIx3H4rZ9dYqZT91AKQ9BlvOFbenMBb__7WBt5wEV-HJ-I1TtFZzgQN0C538Q4tGpMoJcE7_-L14WyohVqboXJ_TYbssbcjRB6Mfgy9-fk0jXRsHFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1xkUmXMgVDCPzZhcUxl5_ZfMlExxNkxtZjJwZndWarCkZ5oozALgeocA6AJJ7djDaD8XVT5uv__cwuo-jk8lAEYk7gDgSIw4ziKhA8PGFUT7xByUYNBb-5JIXaNRUu7v2Hl2F51HDpqX1d7VhUCG0k4i2HVO6yjZ9rWDS9oCQzSsrBM5PkvLyIyUSU4NhGtflb3yzkZVeWMWbhCcq3yKfgBAHOqT-lCmabP0tK1k13wHVUQkbeZSw9kP9SCUPoqArYuhvRwhCmMAeee-48s-V4fK89RwXm1qYWVdubBc8PIga5G-qMeqvaZDf8ICSu5vagY0hH0HoFh8YeVjikNFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/28492" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tN-RNdENhNNThLc1wLkdl-VZ44uA_z2MdkB1sNa9PmM3qh5_ur3RGLSDsEghnfigMCJai2698iLPYVeP8H9--TMkbsNPV07QFxSUI0yAerMEIBApTsjezXdSSJWqEJlN7lTwcC8pW7gX216kTcy_rnzNFVBD0ePfYPkOg8gf_xnzzGBZVXrXFFon64ZSo5kPxDKho20AwCRrz4Mbjbi30rXDeda90qUo2oow50xatTcsTEgUUVjBMHY_kQZaYgh1ceAvs6GZ4v4vnKrL2YFKq53YeyEIZwiF-ii1tEClHXlHxtMC8NcJFzYbMzvlKeH5Ky1ii-6AMZ-U2pgPILjSPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مصدومیت اوستون اورونوف از ناحیه‌قدیمی همسترینگ بوده که بارها در این ناحیه مصدوم شده. فردا از او MRI گرفته خواهد شد و میزان دوری از او از میادین مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/28491" target="_blank">📅 23:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d926debd47.mp4?token=UtL7WNNWGDWuNfvuVFoYMdEx5YRVRxbnA5ZP2AyU-Pk6Axncp0Kyt4QfBeoVT-FkwKhAL4YmffVeRdFAhPF9ZjLsaocoKw1d9Yc7yY-Wb94dW4SOvAcA5FExfHnCmg4V7yLJQHcQgzOQQkpoedLZ-5U-1D1TwMoCFpGcwkLs1GLe1TqkKKeCBC6Kx43tu3Ay7NQKkGXr6vSkAIX788f_M4O-mia9kfAxJgyTmViX0Sro-Y4wQLd5QoLyFZvUWGJFrA8BSssxjXCVTYs5o7JYT8rCwpfTt9lSNgUrQ42ke_-C4fBC_DpJqh8bVHeErXZ9nCR9m7eJfc591oPWeEkvYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d926debd47.mp4?token=UtL7WNNWGDWuNfvuVFoYMdEx5YRVRxbnA5ZP2AyU-Pk6Axncp0Kyt4QfBeoVT-FkwKhAL4YmffVeRdFAhPF9ZjLsaocoKw1d9Yc7yY-Wb94dW4SOvAcA5FExfHnCmg4V7yLJQHcQgzOQQkpoedLZ-5U-1D1TwMoCFpGcwkLs1GLe1TqkKKeCBC6Kx43tu3Ay7NQKkGXr6vSkAIX788f_M4O-mia9kfAxJgyTmViX0Sro-Y4wQLd5QoLyFZvUWGJFrA8BSssxjXCVTYs5o7JYT8rCwpfTt9lSNgUrQ42ke_-C4fBC_DpJqh8bVHeErXZ9nCR9m7eJfc591oPWeEkvYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ژاوی هرناندز سرمربی‌سابق بارسلونا با عقد قرار دادی تا پایان جام جهانی 2030 سرمربی هلند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/28490" target="_blank">📅 23:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/28489" target="_blank">📅 23:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28488">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmOXA7URvTn-y_3mIYQwGfCe-J-jB8Ie7BCYB628XAAzwoLG_QzJn5aLf4sQ3wwmGOwqDOhrb-bow9xLWwcDrv-Twi19NVhPvXX9CSeqIHRW0OsRxxUnOS5SRs7tBzV2uEd5VNjI-6rV6yQpdbyPpq8nqxi31v1EbHvmy0uIqGBKYjnzPIWVJQN8Vc0tn3e59p52PfTOpJofi2tmqUk2JnTl_9ItK0ePCdXaqynKQz7HY5v49QSIwmWGsu-aegtNpIHylt0r66kNlOIvbYNFOQNUgNS8oQj-A14QESHQXlQQ-HuNMBEBojMOvdRDk29Ma5O5RyGd2_l8zIFQBGDAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇵🇹
برونو فرناندز ستاره پرتغالی منچستریونایتد بعنوان‌بهترین‌بازیکن‌فصل گذشته لیگ جزیره انتخاب شد و جایزه ارزشمند خود را نیز دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/28488" target="_blank">📅 23:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28487">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlhHJjHBJy2OYJGjdbUKLBWID44Prxh34dt6HhxhmRysqJoTXgOR-M1MAXV4ax7X8e6vKTz4vfuF0GAbUUhwWkeb2rem08Nd5vlQUTX7E90FjVeEPQA7nu_zmc8zd2U1lf_MlG8GlsZ220Lzl3-59f4Dt_G3zmdMQFc_x4pgQepfdWk7hgoZxSwn2j6xvxfnPg1Vsk91k0EOvldbTik57xYPZlx4VRkNJ7CUxbJqcrUSwJOhiGkHFSddGLU2T3-Jg5aQoDsTY_DmDBWqq4wuGNuOzrYBYGgldGwfiYsy5dybNteEzqB_hqF2U12MuWz2qRZjVjVYzFbug63rgsuM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ترکیب‌تیم‌منتخب فوق‌ستاره‌هایی که فوتبالشون رو ازباشگاه‌پرتغالی‌اسپورتینگ لیسبون آغاز کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/28487" target="_blank">📅 22:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f05b52e15.mp4?token=lBRKWWXY3dzUq0pDE166vFThlqqA6FSYMT8jsHD1YFsxA1Uk6NfiFtPEs9As2TWxJg1--BZ3oxlWl2aEI6PixHoaJN05YO9YFj10dtAj2Ve9TZ88XSpM-7cgOyq4FTTb5fOal52Z4F0alMPAdOAyI0q0yqovoEab27kV8SqeMVahbq5pAyPLd9_IqKpYsxvAXm0PozsuV9dGoEmkKBOUHQCAmISONR_tqZm7Xq8E_JkusU9_v_tyDmbCEJcqvuj2NkkiVGyWfYMjLLh9NepM13o5E5dQG-0Sp-n5IGP-tFtOVvE01N9PZNMbmSLUuyD32W2Hna5-QdlJKN6dpLwsfKKyTEPGrPFT2fxFONk4mnMxLDqYi2DGo0ROnSL8eTzXCIgxY-c3sYOxu0dVhYF7UETxEm_pPK8JZ2KOATeQsrTe4_mOZjHuV2oq4lgb0cOXeA2VV8rN3tl7uErqhJolR1oPUzAjSFJNG_8X9wEhwptZz66E6VmtHt3Z8z6uJ7LEXNl-pDTTo2kSpnDdqPPSwrsXM5JOhJm2vZgr8pBEfaQvh1fEVPvJjiXGCjYdxsweG4Cx3rQA1Yi15_5TCZbLQ2hewj1xT8TDh0sZAsAkZMkqTgqVqr0R0tAOzsTItakxRCQ1e_XwL3BgIP3MJIZ_Sfd0PNEk4uv7rj0u7mI4Rf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f05b52e15.mp4?token=lBRKWWXY3dzUq0pDE166vFThlqqA6FSYMT8jsHD1YFsxA1Uk6NfiFtPEs9As2TWxJg1--BZ3oxlWl2aEI6PixHoaJN05YO9YFj10dtAj2Ve9TZ88XSpM-7cgOyq4FTTb5fOal52Z4F0alMPAdOAyI0q0yqovoEab27kV8SqeMVahbq5pAyPLd9_IqKpYsxvAXm0PozsuV9dGoEmkKBOUHQCAmISONR_tqZm7Xq8E_JkusU9_v_tyDmbCEJcqvuj2NkkiVGyWfYMjLLh9NepM13o5E5dQG-0Sp-n5IGP-tFtOVvE01N9PZNMbmSLUuyD32W2Hna5-QdlJKN6dpLwsfKKyTEPGrPFT2fxFONk4mnMxLDqYi2DGo0ROnSL8eTzXCIgxY-c3sYOxu0dVhYF7UETxEm_pPK8JZ2KOATeQsrTe4_mOZjHuV2oq4lgb0cOXeA2VV8rN3tl7uErqhJolR1oPUzAjSFJNG_8X9wEhwptZz66E6VmtHt3Z8z6uJ7LEXNl-pDTTo2kSpnDdqPPSwrsXM5JOhJm2vZgr8pBEfaQvh1fEVPvJjiXGCjYdxsweG4Cx3rQA1Yi15_5TCZbLQ2hewj1xT8TDh0sZAsAkZMkqTgqVqr0R0tAOzsTItakxRCQ1e_XwL3BgIP3MJIZ_Sfd0PNEk4uv7rj0u7mI4Rf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تومیسلاواشترکالی
؛مردبازی‌های‌بزرگ؛ اشترکالی مهاجم 30 ساله‌تراکتور که شب گذشته در دقیقه 80 بعنوان‌یارتعویضی‌به‌زمین بازی اومده و در دقیقه 90 گل‌برتری‌تراکتور روبه‌پرسپولیس زد. سال گذشته نیز دردقایق پایانی‌بازی‌برای‌تراکتور به میدان اومد و در دقیقه 90 گل‌پیروزی‌بخش‌پرشورها رو بثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/28486" target="_blank">📅 22:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28485">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oalY2yiZ_T28g1V5NkUbM4xX7tpo6ZMqMsoaZ1bNJNv1Z8RD6C1zI84W4E9fzaNoi-XLQvu8Zn4sKfO31NtPMvvcGwwv3Wyy8Z8k_LeAaOF6BVlI8bXOsLr-FCcbxKtxrvS_8Fd3xqz1-Mx9XZ6UYA86cHh5kavusMaOFV3ETIl41feOsTPBdzKqHpJdkAAbwKbuwasXZcTYWMOnXVTfNSGHWoslZW7_J6dOhJcfzjz0Ezz9bXwvBNhHLIPKsu3sqFTL6GSSqhtm5IdOLFgHPVkBjjTFBa_wo8T5tfZ0tCjVfWd5orO1ciJmtRn8QV8BYsZV2ONlQM4lEDw-BTEP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ انزو فرناندز ستاره25ساله باشگاه چلسی در یکقدمی پیوستن به منچسترسیتی فاصله داره. آلونسو گفته دل انزو باموندن درچلسی نیست پس بفروشید و 140 میلیون‌یورو درآمدزایی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28485" target="_blank">📅 21:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28484">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4bE4ynxWLdahbq6VKG28aXeve_8HpJqNl02ZYybEEQPwxTqz1IzIkDb_xkq87JAXdIvfZXJ-VSrYIHb0tdbOikKW1vEgVXLJBi9-Issq6sm7MO1yXK8aSovCjpCBcqsqhZPSrVSA65ljNurLZeC--6KFe05oKt0fyr0PyZH1K5hqt9mWocQ_TAm-1qciFA80cJU04A9Cg75PTUYyWO9YquJA3ag1HX5Y2OU4fTZ1VTW219z4lvHR8tVw8c5GULnspeChvODuA_VNVxEJ3IV0-1GGRWxfGTYn9XSKH9yY8ptlVLzcrkLU4BgeQT6VyPia7Pc0_zXUHWn5qjb3WwghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌میلان باموافقت‌روبن‌آموریم؛
کریستوفر انکونکو ستاره‌فرانسوی‌خود رو با قراردادی قرضی تا پایان‌فصل به لایپزیگ‌آلمان داد. انکونکو از ستاره‌های فصل‌گذشته روسونری بود که روبن‌آموریم نخواست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28484" target="_blank">📅 21:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28483">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPzFg1Ty2bOGJvH5zotmPhyyOmg-QcbJjgimZxeM9lt6aoSevGHR-1Tj8yIUbXdosbfXGK2BwAsNcxRqcFaGrcnyfpnKsN7VpAUzm5C0fOrI8JH-1ixLvz8gPN6cGOAien94puOTyNluVYnB6UuC2KsMiDXTyJcoKqHNCJw4Rp33f1wajLsz3Xp4puBCVWia_C2O_BO8Nu4wS_LpVbsalcW_L0-DmUOtsozpDDZ7qBP3nI68tA0t89SvlqSmmAf_CTmOQeGy47Sm925_WBBlPQdQBOnbR61y3vCV0nkA7dFj0dMqGlOYmSCu5Avw8z6M_5mbXU_rQw3mrbXtCPhI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28483" target="_blank">📅 21:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28482">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-bowVKWIPBnIl1qla4AiWN8fDtfoS8CYNg2aWA4WlUakHUwQMQOMI8ez20kQsdRPK07l-PmA0hypKUwgoJENeg5P7QCg8YAJAuqvHWekl1oxDhk2wC-uAsI6QYMzhYLgK6vHKiXK3luLTwhZLJVmjPPzjmxY-VOwMzfYveAilEq9-ljW0IPsQlbCKKtT0i8C-Dh_SnzzzejzDM_yy4zTGPzdAi-gxYFMKCJHhKwPLO1j0ETl_ZB79bFnFvh6IkgdviFkVjSq4RQACYFpcnGKacxkL_GZ8K9hU1RWrsiCxXbSHTA_NSJqGohLyXXCK3GEfsSwDIv4Wej8_3pen8DaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛
با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28482" target="_blank">📅 20:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28481">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXESDcOudHuE9pooAbbHip66A5GIA_7Na3x-RVNXqp86cpT8cYrMxh10i48ds6whiFy7lzPK8F1lmE8lewrSx5VzCnEFVnePytkZMbGLP0twKCOLfVCvp5VnGXnb-o8JY9rUgyP3idSdes91V-DJBXVhFfPrk2lxR3ZNUCUd6e3B_Xjg_5Evot2ckMwhItlHxCJ78PktlcZjm930I-CzwscDYZNqaEgItRbezSavrwALipGOQM2PWlaFcrpnA78_gaO7_J3ctBNg7QovveVQOUu_-Mwiji7Vpz2ml-1z28cgf7-E2oPsPrKpE2vTWdKrwBHhG2585TsGgdzKNw5IlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28481" target="_blank">📅 20:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28479">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EROs0A8UwPJlnb2ya27NoMjzRsJOCuvl41g-8e_d6loX8ZCRGW1QWMXbo2ZKMUrQnUItL76Fio7_oFPE6j-8ShWjtb94cmRRWjXu_wRvgl8JbQ9I7ABff7hD_a5ALrtfsgvyGPRal18K_DKsEPaCVe7PwKKOgugA1RasbQ5LidZ4OSxTYwMcKE7JZfH4u8fj8l4b_5oRCJ21R-CwF_5xq7xyV6ZUm3WxawmwAfJ33C9JAffvsgtzENJk2x7Aji0qhvB1gNcy9ADLhdSKRBU26Ah3_w5ocfm-WulAEE7XNlisnsjuUkVwfxYq6P0d--SDt6L1hc731zHlnU5y9W4CCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIh0GzWuNMcNOsvYuQ8_DKdDH9vEPnSzXJz4n09_EKNkOiPcmIbkJqNcZshemPNsHXtMTO0glepl59ao35KLdHRBN27-VAMDm4Xrhrc2wjH4OEEg0CE3rXkwQKdWXszkd1uLz0ABOmMdxdvmtPl4RS0aICxIIT9E3AHfZOMvg9mBiDyu1Ah41K5ty9sXzqtUAJ5wsuijBN_xSvYye_Ej62s8BMnn3JPeo4dvwDet1I5x_BHtv234hRSziP-ocHDFdYUKdPxuKpBl2JaTj7pYwNgjhU1L1raqEwyXEUy9ly0Nk-muoSQ9KWUWwFQjsBvoq9qBNfy6tWCh606Rq7SjMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28479" target="_blank">📅 19:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28478">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMoeBotTtzolcxW4c--lMONVjGkL1h_At9yJQEYn5rma6UAHu6TAlGuOqSInQQmGcxjA3pjoz5kdZM20gQQUwh4UfIdPly42AimEnkW64hFE83XTCCN0pufecVm2eC57H6AMrpILNHKcT04pIoHerB2IXTS-ccGIl5U9WmYujozl2ztYpSsYrm8Y2kD5cIrgcZh3bLfV9cIMhv1MTIlAImi8pSfcl3iqEbQAtuc-n-uyN7ajDLFQeP73LqhppfQhX7wQ2YdK0MRoGQ-TX75qChxocsSZeWhODdfbbYKxLEqxf35NBsJyhERkSZ2Wt5KrXHEGZ5k3UwQYwbkWldt3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ هفت روز تا پایان نقل و انتقالات باقی مانده و هنوزسرنوشت بازیکنانی مثل بارکولا، آلوارز، انزو، مینته، امبایه، گاکپو و پست مهاجم نوک برای بارسلونا و وینگر برای لیورپول مشخص نشده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28478" target="_blank">📅 19:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28477">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxetivueDNaQbFRbSJR113pOhzmEq2nwB7qU5ME9LpTM33JZ9879mRKCfd3I-TIo9s5q2Bzb6jQtP_ELaMpJCztUTWr0iL4RH6tisZ65NB5Sb_3wxOgIW_iNUQMDQ4ZhaVBoSxiRuNQg7eb9eRC5I2wauXo9nw9LlcyGbUzCoRYVjhXSLknb06hKdk1wPypfiOhJqj89pgf3_Ny6slRhnMLT8PJ2ksy6hWGCiu56rhw58tLXa8yxofOMAfs3TOF9e03gBFIQUl0hSv9scVSYCvgrXce9gW4qdv4k8gu8FHfMZtLNAx-I0tD_Dlc4i992gOT56fzE5L-De9INVYDz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28477" target="_blank">📅 19:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28476">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ5Rd0uQAV4rN5caG86jqR_dbj2vb9YR_3cY1BBQZN8BrPxrPJ9b8SCTXCUotBYg0a8osyN-dJ7KlEWXPP4uEuSw2SUuIqZAEx05RSom2VlE20X6uy5YNdgaa3e8DhxqzTOdPiGHDnz_tT-Xf7A645jRRAXTP_Gcnr9GYhmTmTRSQgp6oMUvoznqGp69ZjOFk1EsF31ZZqXhenDHIg5o4O5PBuo58PuR1KnMnsHf2NcAIMUGBgA-HdGohokjMnDnQpLyKIkoirgbguv_6_2UDBb9BoIbme3eVDRodbI6KVrXSPOdIm162PMc2pM-v_2oJoSUuKpU_jAjOXjIraiLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حرکت دور از انتظار عارف حاجی عیدی هافبک سپاهان خطاب به هواداران باشگاه استقلال در پایان بازی امشب؛ حاجی‌عیدی در دوران حضور نکونام در استقلال تلاش کرد به این تیم بیاد که نخواستنش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28476" target="_blank">📅 18:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28475">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
قیمت‌موادخوراکی‌درتنها 5 سال‌اخیر رو مقایسه میکنی آدم‌کرک‌وپرش‌میریزه. کسی ندونه فکر میکنه 50 سال‌گذشته و این‌قیمتا تغییرکرده. قیمت خودرو هم که بماند همین امروز روهرماشینی 50 رفت بالا.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28475" target="_blank">📅 18:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28474">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnk3B3JYyWlrfrG6V3nBHO5MZ7i0TNC0K817PpQ_VmB1nJI3MbYsJdr1ZZvT9zPfDMXiHrMHc8j_oYQSv17ln8ry2nr2RHTB56WLQF8g2vTRRR0OK2g7n8D0veFGwARWcqy1nWf1-nC8ln_SqgEuVa9yTEDPahxlWsh4W7dK1ICq9TVzkVDthDT8e6wV58W54tD6hV7gQWK3oLtNWNoqzX5wmf8-nLq_diGP5K7PzV89VIKRWp97Ivn_8cRJz8UIVB7tS0uW9BoXOuICzokGTdOFdOyoPiYau9gi7tBFa_YkhBCiZfd7kTqOHHvL-OKmlFY2fm_J8GYUd8FmnlH6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ سال 2017 در چنین روزی؛
بارسا باپرداخت 145M€ به بورسیا دورتموند عثمان دمبله ستاره جوان‌فرانسوی این‌باشگاه رو به خدمت گرفت.
عملکرد دمبله دربارسا
: 185 بازی، 40 گلزده، 6 پاس گل، 141 بازی رو به دلیل مصدومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28474" target="_blank">📅 17:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28473">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORzI6ODo7zsBOI1LWi_43hp29CQBbrN5V7f-Z3Ls1ehA_lc41sa8ZyhquACEFtnZvGOFJW9AjroBR0cNXsh3SBQ3LmVxa9OCv5tpNWd1tl-LaFGsyGesb90U8fYS36qKtZdCMrwSdp88WF3EbVt_QUEbOIFREP_rAKvWGsfM4t4lBNteyAB9qMvh-yjLH5B0G6OzOjQbhIfDHL6bSRGy3i2mnohSZ05Apa551hc_9UclEqdAWi0KA0hHaet2PRc3ZOYU_VEk8kmsVEcvegGVyZKbMDwfw9ed6N_5VYZPp8aDAXlbNWjDy9dDANGIyC_-CbysXSg32lL9hvCx3z0hVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تاتنهام‌امروز100 میلیون یورو به باشگاه‌منچسترسیتی‌پرداخت‌کرد و از ساوینیو ستاره 26 ساله برزیلی جدید خود رونمایی کرد؛ سیتیزن ها دراین پنجره 12 بازیکن خود رو فروختند که بیش از 400 میلیون‌یورو سودخالص کردند. الان هم میخواد حدود 140 میلیون به…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28473" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28472">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hdo300fC2Ds3zh3P6s_a6KfT6X3pqInc-ULELC_eT3Sv2mXbpflgovez2K4SnVOPlqUcyOeEglbZaEOm_9rp7R-AwFYJvdMPNx0ELfF3UxIlz_ufuOPYkyEA6s81BEph3RDlXFbB3gK5o9IFMKLUmohcYC0wkNpIvqX3DYDX6VczAT7MiaE72twI3vuIMR9a2URqK-HWAVvx5XzKDE7qU6Qj8nNFF7C4147NMxwWGIAfsbded0__FBzmtcDDke7VZ7xRsHUjSRfmQqo_ZHcceLzvqQYheb3CXIWKWhH9x9kHfc4q9A7-j311T2j8vWlKBuGK3p3BR6SebWbqmofFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
ترکیب‌احتمالی تیم‌اینترمیامی درفصل جاری درصورت پیوستن‌پل‌پوگبا و آنخل دیماریا به‌این تیم؛ دیویدبکهام‌مذاکرات‌خودرا بااین دوستاره‌فرانسوی و آرژانتینی‌آغازکرده تا درصورت توافق‌نهایی باهاشون قراردادی دو ساله تا سال 2028 امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28472" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28471">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2YKDUUeYf2VdgUxExKUuFSOE9VelRJtUwhnp2u8fXpE2JQGvbBTAZRXBipqEzIlEWGT-6AMFpf0vyrc9lNPeWQs3XszP4KnloV83f3Uy7vPd4hux4Y_e5TyYkFpSHHnhG2pQ5HxDzjBSRzA3rmyCBK734OtiM-BHokKlppgXLcFlLFwY82Mbq1P10b5wsjK7lsRnvrWu1S9StRtGWaX24fNJ6uNQgF4dB_8lAD7gyEDKTKQPdBTlhKg8j2uDii2GBl8JN2NK42f4XsA9VclmGvDiwKro8dAAf2rGhtqf0rUCXzeM_ErnE_bclnrUauN0MDwbRX-VbRLwOObD0vmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام اتحادیه انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ناتینگهام فارست
🆚
لیدز یونایتد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۲۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28471" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28470">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRMWX9QZZs6fMBfdKWdIZLZ4U_tbP-iYqI4jcAvcGll9CWQC7tLjF4raHAYrThGrUbhiS_F0Gx2RIBbyy52nXHr4PA7IB_RGZNX8HaYGT9A5z5I1-mWzg9lzQ54yIiHMbXWObldY2-QXnFzMwwB4zl3ALRwRm4FKVI3AEjwtYtaFCSeWLYEQz7iuR5z97tRE0PVHb96uqvGs0JWZGeCsz_OCdqo7A5Mb-LZtNuGCsYG1KA6gcwOqMEYCfyXao3kKzBVw7NBQ-eixQKYE5AyBfSqEk2xKAvlR7bWFzOG-RPVeRwuxmUpMD3pIw52KL3kddhL_xjehoIRa3GBJbd-DZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28470" target="_blank">📅 16:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28468">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=dB-m3g_Qay3tbyPlgaD9XaAMLv0wYmkEZ7LwH_pNJX7BYf6jQx8fyvA1KihqZndm53iJsuYIzTLtSPnn5-bx0ZBiDAJJMFlJ-Nu8Zzf5Zdva_VXzJxtUTlrZ4mEL9INizJ2yAkKQ9w0Ap_EQxFvQkRj_EGB1mqzBi2e5-GtCBRZNEUt4RDE0QSJcNfL5lCwi8CO1ngNJRVpyWjqcBNb_XNFkxEFTYmEBX6CnVN2hLL6tRwg9TAfHq87KBLk6oLuMXdMlnZ7bLtpmOLaA1t5HDNkCSrX2i8EsmbQx8ZNi7krsWvSKqxMGwaHPTwkIhl62oeWg6NEo301Dc8ljPPp22Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=dB-m3g_Qay3tbyPlgaD9XaAMLv0wYmkEZ7LwH_pNJX7BYf6jQx8fyvA1KihqZndm53iJsuYIzTLtSPnn5-bx0ZBiDAJJMFlJ-Nu8Zzf5Zdva_VXzJxtUTlrZ4mEL9INizJ2yAkKQ9w0Ap_EQxFvQkRj_EGB1mqzBi2e5-GtCBRZNEUt4RDE0QSJcNfL5lCwi8CO1ngNJRVpyWjqcBNb_XNFkxEFTYmEBX6CnVN2hLL6tRwg9TAfHq87KBLk6oLuMXdMlnZ7bLtpmOLaA1t5HDNkCSrX2i8EsmbQx8ZNi7krsWvSKqxMGwaHPTwkIhl62oeWg6NEo301Dc8ljPPp22Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28468" target="_blank">📅 16:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28467">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI50NP7sMVrF-bzrAsPk2D02kpd--gcw1In6IBoIMp_ybszL2ld93IU7lwTCHjSsTJQkVvG_kLcWYjz-opE-UGL3sLXgc86-9Yo-2n7PCOOec2x1hSjahZJ_bjRS_8jaPBWdspxBeIsKmlBGZ-Ixc0gRP7egvVcFHWg9fNWrOlgTNAmvQnuebkZyxgZ2qFlX5KZLP82b_YL2f83R55CS4BnPOCgSO4evbqgkYR4tlz8GkFu99x6OPGx6CwfW7w7437dzIagpchbGdp2JlBFKWBkiW-lPUL5KNJRR6c8Qm0k6VnAuEvOLJWcIGCjHTqtlmeOyFr6i9oSfTorWIoeNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قانون 90 به 10 در دربی بالاخره اجرا خواهد شد؟! بااعلام‌رسمی‌سخنگوی‌سازمان لیگ، طبق قانون باتوجه به میزبانی‌استقلال در دربی 107ام 90 درصد ظرفیت ورزشگاه در اختیار هواداران این باشگاهه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28467" target="_blank">📅 16:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28466">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfAcRzbl2DVVJ6rQRhwOKC29dLqzQbWTM-CLxRLDCqekXS9AwuyrgjFIypJ0auLz0e1z3cmEaTVP12JGyB1E9c0G6r0mBzJnncZ4tVqDE7Bslygt6vYRVCduREZ9_8RhBcHOKhNbjl5Qnj4DU0ADEznEFl9zy_Dk3cMx9yyxHWb-yAFxNFDQ7CBxZTK2BCH0AhafZsnfyIYrcILbv5-Hoy-xZAYrXU3DvEUVk2EvQy5pBg7VyjxAuRl6XN4WXMETv2XLt8mQXMshbSec2pNc2EeCG5hnjsvPq9U83yIvkINjFcdR2OxC86RDkqnEHsy9Ubhemdk-6uXedld6KTI28w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عارف‌غلامی مدافع‌میانی‌استقلال با قراردادی یه ساله به ارزش 8 میلیارد تومان به چادرملو پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28466" target="_blank">📅 14:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28465">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PizQENhH452hQfkPXcZYvnWqNpzkC-bgG8xsSf58ghowP6vOREAdBLKc8QH2JLRK44X3NvHuuKVADvddmq49aGqx1ZO1tFkOHz--F4znyqFaO4owGiNAf0SVHgA9WvweeTvJ5Kle-7imZNJ2QnSFpOnkwPQuIlq3-ytavkzE2HLOO9eRX0yxC7Kr30oxayqjf0V0vZMklAQeeGM9mwTOtzPGeJSA46BkgsHUzpIh3d1sxhoa5MXmpMj-flgRshc-bOFgyOs7cOwUFinjU5zu7SD7H1reEH0HO-tMJL_vddqp8fp1JEFby00iw5CQFUaatGYQwT9O0YpmCgrrrkjoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28465" target="_blank">📅 14:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28464">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEbXo1d101R1PRAbOtdxioSzRoLKlJ41e6YV_QL6XUfKqLn-M3hJ10qLCjh4zsnBuell2Ud5poBlfsuQMB6ze5f64J8S0ocEyHF36zCYrWi4cdgqLJfQYcVdDYjKRKWDzM_V2HrJnGnT2zIXlA1RWRipy_bu4vl9mbsuMj3MtwWVNiaEg0qAveiYhAfR-F7g7_zxE8E72PFym69oldcYF61RrZSAbgdTEeRrzU0rWz5q_I_Nnkun72moiS0LEfh14HA2PEUPbssZ4YKrAnMadiVwNWGFtzrdz-hkHw96INfPnKuPxYk4cKIPl4FqtTbw9nrxUw4Q8_5xWqlmKJZw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هایلایتی‌ازعملکردفوق‌العاده دومینیک لیواکویچ دروازه‌بان تیم ملی کرواسی و جدید تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28464" target="_blank">📅 13:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28463">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsksxQHVakV_XVL0tSbEdXnpBuUrtiSYkQvE8zZkZ3I7CKxdqkjWrbI6Rp3Vf9H7iRHrajJsq8iGbNRjScEq1uhwl6Q8qn5pOtpOuHKJmXe64v5cHH-ZeVSSC8RTuG_N9r8F-D7OmOO36K4QJAFDng4u3TyQBcOOdyJKOTvvHYq400TZ8on7KoNBtYSToBZKybgy4w2IAS2l6gEoIK0qkV1TSNkTUOiBUp8QnnYrlCXUl9GErA39ED_T7TSbYCR_uSTDxdQLo7wuqh_gaZxUrjH9gFtoOKGCSyTxg_qWEEgHQoezIsemMd-KqtlFq9RzCDPl8fVebTTcv0M52Ka9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توورژن‌آمریکایی‌فصل‌جدید عشق ابدی یک دختر ایرانی رو دعوت کردن که همه پسرها عاشقش شدن؛ اینم رفت همشون رو به ترتیب بغل و بوس کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28463" target="_blank">📅 13:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28462">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=PAdv1a6O92dQfcOpUF6NDm2qKD9BfV4cWzytaiRrN1SCdZR1CDaMMSe1DRbN_LxnfNvld4JX01CN_769WmYl-DZgOsJd4e3HkyVv5ZHGwtiklvjHnuuY6qXNuLJJTqr7o1VO0LIHil9pB-aZ3n3tViFXoGM2W_5WCf17BdQZikiJ5OBkp_7eqWVhpTx9m0k8QrUljeQwAea9atff7VAO5A2fS81js_-r-2zXPrWKziBNM6JR6GiLETMO6aLWxgly4blmEPJuIwQKrIMxjqBJIV5en_0lWU3pJhe8GoeEhPRWKP4AmVAD19g2XJ0RzDSI-t3OwHUMvjfVsliMYXnzsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=PAdv1a6O92dQfcOpUF6NDm2qKD9BfV4cWzytaiRrN1SCdZR1CDaMMSe1DRbN_LxnfNvld4JX01CN_769WmYl-DZgOsJd4e3HkyVv5ZHGwtiklvjHnuuY6qXNuLJJTqr7o1VO0LIHil9pB-aZ3n3tViFXoGM2W_5WCf17BdQZikiJ5OBkp_7eqWVhpTx9m0k8QrUljeQwAea9atff7VAO5A2fS81js_-r-2zXPrWKziBNM6JR6GiLETMO6aLWxgly4blmEPJuIwQKrIMxjqBJIV5en_0lWU3pJhe8GoeEhPRWKP4AmVAD19g2XJ0RzDSI-t3OwHUMvjfVsliMYXnzsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28462" target="_blank">📅 13:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28461">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNNEv6oJ97StG1uhRg7UnwTPgST9YQ1guS_g2I3AOh0oX11XzWc0hJsVTlDLyV7upx6QGhGOVsuDEUBjL2dAxn4NcCBlvVhh6p6Vp06lHYxjT1Vg6skSC_2oPy3n6KlzUcLza3B5vfpW0dc6x8PSA-OiotBJq_G9dkFBiDqFz5DOxc9EGFjl56TbdT0ri2RQF4z-WM_tBAvEjfdTgb8FZodqJVuTByaiDOj8QcGnunH_V83SLNO845wMeUFU3HLf2xAalwYP-1prztNBCHAf5ztG9pR-e0Y_GvI0GH68U_3_quq3H0bN86SjgHT6DpVpfaP6lAjvdcZhZAPtV1m0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🔵
درامد باشگاه منچسترسیتی در این پنجره با فروش ستاره‌های این تیم: بیش از ۴۰۰ میلیون یورو!
‼️
ساوینیو ۹۵میلیون‌یورو؛تیجانی ریندرز ۶۱ میلیون یورو؛ رودری ۶۰میلیون‌یورو؛ عمر مرموش: ۵۸ میلیون یورو؛نیکوگونزالس۵۵ میلیون‌یورو؛ جیمز ترفورد ۴۶.۷ میلیون یورو؛ آکانجی…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28461" target="_blank">📅 13:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28459">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XoNBUZG_1oR_ww5O4xDx5P2mON7HppJPMZLUpUURlSjg-CJW01EhOfgw_W8P6cRNrz2dGsHWwpyruogB2virin0RLpPYsnqrDQiMvCKDMbtK2NMUtfE-yO_D1rntVDLdBWIKQjn2_-OfCZISxLfdY-c0tZnZw5oFEt721hDWsYNwTKnv2ejZ3uqdJbpCJwMbZ84MwAj955EzWOU8EKn_fIuGluBI8edgGTZzYiw69jfkYeabeB7TGtcKYJMr6zGQAPTR_x9kahig3qkZjpgKFyQVnBeIafhQzTvlWq9v1L3J4jwXcAeg6_fFiAwZVaDKG6L8AHJx5Ar7U9y1-lXE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDVNxOmais9WAwzUjdbhAYo0ehD5bavmTfBcngmvieIAQ_iCREWltKXvPxquIcDPhgS_fOd9deNmFq-hkT6LrKvh_--pKoXGzmjvdfjJXibMSefOsQaURnhNp2jDLrPD2hSX27ke-2a91Qxu6fylnDTw_8FEngiGZ4ICckqKC748usJF6OPPR6t3iAsoauWe99toHk04_CDXlEvOkXMT_X0W-j2EylzqTtg7r-dtEZ4My_OpHhEbgTGuQ2kvdwAKchi3dEEroenPspBl9b0ZNso-Wuc49UP_-swP3zKORubICEf04maZ_LnpFnubLR2CjqVxBWxHU97rnd53yG56eA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
از مربیان آکادمی لاماسیا؛
که حسابی به بازیکنان این آکادمی رسیدگی میکنند تا ستاره هایی بزرگ به تیم بزرگسالان تحویل بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28459" target="_blank">📅 12:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28458">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=uBp9iUEuXlDE-5dZXljoELBtvNmTDpTfHCSz8rhPpu8tbz7AQX_B8O9fsSo9hRRDFPZjHKqf1NjaHiKgpt7hYwC75LitAXEAoFbxaLRWbtQs19Y_3AKI1SxSXIbyfTJA3N0sZgelgUm7X3IggaUJcU190YO9YWuqT1bWVM0_Rl0VZrF7eYptSFo4oehETxnk9vbuell6uMQ6BCslPHWpNgnhp09_U6NpBXmqWkui_yurlZmXFNec2cWGT0AU-WXo1c-FHSKalnm9VLZVg1PgzSAHXVIzCklWw1mDq1Rz211GpojKjxrL3GW2cdtWNKNcUqTTnPUkRd6QKx45hxLSuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=uBp9iUEuXlDE-5dZXljoELBtvNmTDpTfHCSz8rhPpu8tbz7AQX_B8O9fsSo9hRRDFPZjHKqf1NjaHiKgpt7hYwC75LitAXEAoFbxaLRWbtQs19Y_3AKI1SxSXIbyfTJA3N0sZgelgUm7X3IggaUJcU190YO9YWuqT1bWVM0_Rl0VZrF7eYptSFo4oehETxnk9vbuell6uMQ6BCslPHWpNgnhp09_U6NpBXmqWkui_yurlZmXFNec2cWGT0AU-WXo1c-FHSKalnm9VLZVg1PgzSAHXVIzCklWw1mDq1Rz211GpojKjxrL3GW2cdtWNKNcUqTTnPUkRd6QKx45hxLSuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال:
باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28458" target="_blank">📅 12:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28457">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWOWbbHB33OvQOjA5rdwI-ISUZXZQXdWnax1e4qubmMkl97PxPj7j3E-yCblDmdkJsi76X5m_VxeCdqxL2QHrLEklfk43V29p97_NxGIw2TuMBZet7aRHlGZ84QVAbo-RIsR_ILMxylMwZJJBMosxOTKRx2soZrZsAXQWv04xMswIAHQRQa1uiPT5OS2rsbzGfCQLrXCWyme55DY4qRFXQS4-7hM4jsCsz4vvk-Y7GNegpNPZVzvtmZlHLn7itaadwPePZ2czaoB6Dr-9cqiHGYyBwNdaqo5P1FD6sUJnyr-KYB9pHTVsxlk0OcDjx54E8-VgvAbb9-nSQOaUiqSYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام خوزه فلیکس دیاز خبرنگار نزدیک به پرز؛
اوسکار ناسی مدافع میانی 21 ساله گرانادا با عقد قراردادی پنج ساله به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28457" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28456">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpomTTvueBhPm6U3XrKXYb2czQsD_NawdyJXTNJc9iBgBfh_39PzVWrySiqtNtRyEsb3QYrsW1Et-3gamTvnV28Jk1x11f_EN4GBjncP2ydhTST2pC50ThUj7ilNGBlTP1c2NHaHoyWe7XZT_zLejaUKXzlKzNtuoOKpCnPicFUYaceT6weShFxnbwXwFWtxdu1N-E0JGVmlh2eXSPTPPZcc4BCOcE10mXsPdIuy2j8xPBxMshxpcKTQEEKDo5BD9UIUJgZv4Wp36Ij6DenygvAiV4bmHMh2Gi0QjPsWDBuKpNOMGemtraCPIGweXUT8eS3dRtr1QZnUskl-WzqRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی‌از حرکات‌خفن‌و‌فوق‌العاده برای در آوردن سیکس پک‌های شکم درکناریک‌رژیم درست؛ تو‌ کانال دوم تمرینات‌بیشتری گذاشتیم اونجا هم جوین شید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28456" target="_blank">📅 11:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28455">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDXBIolXkROjA9yAK81s6qD_esp2vM42r4AV2NgGfgz2ww-9QC6OHzJvyot6YLXBx4Y2ff1IZegKkNKa6qbScjHN8XPROEnEZO0DLKcRtugfHXc6WZ7AgojtSaMe3BZsw9bN25yIMR-APhegG0OZHj3YgdWHfP1cN4ZXXF4MXC2ShqZXhzLo_5XRfpeN9vGjhiUXTL1bYO1GgqhhiCNB1_Ex4CPD5oAfPhGQTQ4Zkf-iMQ8xkKb_9L-fX5o4C-yPK5UgJJ0csQ766eAF6ySJbmWFHsXo7PNCG7la4FhVr8KgFRa0W0EKBV92y2ALnf3pZJPFtPUIMSOoluZqmEktSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمیدرضاگرشاسبی‌مدیرعامل تیم فولاد: باشگاه استقلال یوسف مزرعه رو میخواست و مذاکراتی هم بین دو باشگاه انجام‌شد اما کوتاهی باشگاه تهرانی در پرداخت رضایت‌نامه و تاکید آقای حمید مطهری برای ماندن مزرعه باعث شد که این انتقال انجام نشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28455" target="_blank">📅 11:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28454">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSSwp97oSVxYQfOWAyxstR8ZOMLp1oWEJdEJIz1Ntb9ubyTKl66wqfmGhQ031PZ5d0tFJ1_Y0blauNTikdVJ-8xQh5ePNo8gbqBmbX4dN3YiwFHTKC6LkwaPXobE94cjfkSSHT-3ILAsd88fgQxWsvkHwSfRBfwpmADD62uSmK6i_-dhI-tX5XaCZ6HQn8YE2m87xSzf5QGzG1Tl_olxp9hMUX1yolPS0n1Ai_G2pxLogF24_ABA35zflyY3esI-8SVFvkTrBIxb-3bU7uD_GWSpoS4piuhqDBBGsiSXCZla6PjwfWqQkXp56lxz-1tL7tX9xhDRWLomekv2HxqbRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28454" target="_blank">📅 11:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28453">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fd6zkvxXo31WBVRpe4VJfhFrWbM_Q3xCP6y_Lmd3t6bmM6w0h07TfajGmkt5iSR75We0SCiQmDtqZ9lugRP2CAy3OjF1GfMXmyMc04Hy3F5o5mjHI7mgA3n50kY8aAauB12s7peQVlAFF9YbEp_Kzi7xyaHaBt04iE0gjMYuikppTNgZzMaELPLRrrVT2lhykrZeNh6z84G1UMZJ4FEZVALPuvgeiW4a4Wvo0TCKnddLT3tdP6LApdNo3mqCu4NRTidRMGJ2OTOWjR4GlmhRfNoFPytsIzUepjRCnV7X9Kl6KqiATn8O6H8SYBl9-d5JzDrXfjF-tE8wpYVyx2DsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛‌سران‌منچسترسیتی‌بیخیال انزو فرناندز ستاره آرژانتینی چلسی نشده‌اند و مقصد دارند به هر شکلی که شده او رو به خدمت بگیرند. انزو در بازی اخیر چلسی از سوی هواداران بشدت هو شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28453" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28452">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VofwhdwGw2r8OEWeeW9YmvgK-JcnlBV1qvPLfKsEXdJlvyEbXUT_CghHszMfgOK4sFsmuGzm6icmbtpL0ZkFAk8-90TT6e2Y1ujk7iKdRWDgGcGq93hr79wmN52vMZha9LWHLIegCWHM8cpCJUOG4juZXQkOdPH6D40sFAzbXIS0AC2MukjA5KtHkNKD5wclRH0onuM49VlSi0AeJCSCBNwSURr6H-ajiP-v6iaBDdjTJubke8gk75S1-QOPKDw8lxZ9_gHpOxIs6PE5SCk67vBRoZKlcPDebBHNI1U6M0L-tT18yhC7TbD-ccbY4aklAtBLAAD_8EITUrMMSNuqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی‌تارتار سرمربی‌پرسپولیس گفته ترکیب تیم‌من تشکیل‌شده از بازیکنان 22 23 ساله. براساس امار رسانه‌ها میانگین سنی تیم پرسپولیس در بازی امروز مقابل تراکتورِ نکونام 28.5 بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28452" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28451">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEHI71h6L6kjTa1XcJXvT1Rv0OQ2Auma5szL-ZE8Vkw74F-vqDJPUo8jxfTI2mPmKJ-OpTYsLSplB4RTl-G2f1K-3JSaaoujk7HdJUuT5hzCCXsFO6kpVH8m9QoGVABr9qrR2CcbYOxMSzsoOI4u13GCWMc7_bd3COH9033HSmsB-Za-YYhzpdlDl1AXNiU7ajCgR8add2oK52aQGjEfqNCy8DgrFxFrqmoY8nYbNWtB59_vlg9g9QpcO_4TDgbryW-FWcRcvL8I_79qsPmwZ4vFemBZUL187svYKbW3sq1kFaVn_jUMmDgl3Gk8wyK5N-gs5g0TqhMaYbuTuwxsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بدنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
؛
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://t.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28451" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28450">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Y09ffZwL_d7BL0nNbJ9Hs0wQmOWj-Myb5NtpucqJzHanxNCuBPu6Dxyl77RZwG5dowa6Htjlx-LWf2xiGb5Enfk-S97iZBURACYJSkGuV5u7XabFtH6tefq7tvDLMN8MpBvlvexKVeM3Yl-3w_mKO9Z4I9f5sM0aYg-4xWzeeEIMAFvES2DcpNr9APKf06bFFUt5Kw3BJItNMmNCSNZmauZ-Pc5AOp5PPCKWagqnD1dQtCUtrirnoCMYD6tZC4Byc-kpEsFu1nlcpafXQct9BSNyYHOKRTTC6GZB5_trR_ZqCKPtEt9lf_gPBpTnA1uL_uIHgq083RjUrbzRZ2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28450" target="_blank">📅 10:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28449">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=fQId0qJ3J9A1kmch8MkPspv1PKlwfFv1Vs97WoHRH4Mc7Zn_eo3jEMC0SzamRJulMCOMRLeHx9cZhVEdzB2B3aHC8kWrPO4z6SXQmh-ZQmO7kiK5BwL8w09bjSg3-8OHALvxpUfiq3OWw9h-0jdUji0no2M30lp4Gix0yzhQIxVNc-3QStHpyPEzYkYe4J4m1Kh4HGZgw-X1J9nESkOcoRbiZ24xkZmleQXvkIIM7x6J2-g5PfLglISW2Q0rcUcWsMibAcRhCpJhgfjnpGo8j12mxSjvZBrRsEfanIsbS5eQxQc1dobERB49dZ3Evw5Gx3hpZymlIliFhETfS6CaAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=fQId0qJ3J9A1kmch8MkPspv1PKlwfFv1Vs97WoHRH4Mc7Zn_eo3jEMC0SzamRJulMCOMRLeHx9cZhVEdzB2B3aHC8kWrPO4z6SXQmh-ZQmO7kiK5BwL8w09bjSg3-8OHALvxpUfiq3OWw9h-0jdUji0no2M30lp4Gix0yzhQIxVNc-3QStHpyPEzYkYe4J4m1Kh4HGZgw-X1J9nESkOcoRbiZ24xkZmleQXvkIIM7x6J2-g5PfLglISW2Q0rcUcWsMibAcRhCpJhgfjnpGo8j12mxSjvZBrRsEfanIsbS5eQxQc1dobERB49dZ3Evw5Gx3hpZymlIliFhETfS6CaAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
مجری‌شبکه پرشیانااسپورت:
جدا از شوخی سبک‌فوتبال استقلالِ سهراب‌بختیاری زاده یه شباهت هایی به‌سبک‌بازی منچسترسیتیِ پپ گواردیولا داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28449" target="_blank">📅 10:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28448">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCq_fe9vVhZC7DONZ8OQL30KQslaFZbe9DjR2PWFgIjIw5BdQkLRWX2y9_s8FKAsivkbDn_GNCFK5btynoX_y-oG24Fn2rmWsjZmg7KyL9Ub4SIRrr9pOMGoXBGqInxMVl0p4whx12vJwyX61YIPs9-pf4oc1GtarAtZzATRfoiHWuSQO_YnWcq_R2W1JJeWqtrXGArEwL5tE6FNtNJNqJ9mZLn95b5w6hpapmefcqpUudVi6IwCUVf1WV1AFAViA7W9FDdzcb5QBr9IaHXDo5xmzsMvpuEpI1e6UtxGG2IvcEpSQHrW8--BZzxwzXvL8p2BVJOptlNOyAiKqLe-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه سپاهان به‌نماینده محمد حسین صادقی وینگر جوان تیم پرسپولیس اعلام‌کرده درصورتی که بتواند رضایت‌نامه‌اش رو از باشگاه پرسمولیس دریافت کند حاضرند که قراردادی‌چهارساله با صادقی امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28448" target="_blank">📅 10:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28446">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBx22JSs2W8WBMOCEnifWfdOVQdVnfdHExf6F5Zz2-GWzx0TNUYQYP46d0KeLXJhF2eFjwH2m1W9qz2cjY1Df_dpFy8QdyLTOIi1yGT3ovjfIbkjZt_lH6ZbxKMloIK6AfRzFeEVQK3qhBSLoCuemLoO-CSbKzwophL5zKLpq3aalSBG-ZhU0pzYR_8PwITaH6EIbXpHp5fsVNJ07Fkuxvl33DXtOzEL4-Tcq0wrn5dA-RUpxjwsmTui_R_qxIdJ51TPiChrrIrmLENuU121WZnA59VMoHG6__78mfjF70Wy3IWIlFMOL4mt1Iap1ZzuzD4kZqPGb2FhABdlDkpzlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uR_XJCqcsk1K3HaepMNF6C_X4YZM5sAzZ1MBe0QBp_Hc7aF1v3ZrzfsEQdBahbzZ4qR27Dl729K06OsyjORTJOqUcDJ9xElb77P4_98w5nz04xLneYYryeRJ41CCz9KiMNFgU3onZvRZgezxlhJL4O8lZAmyjivJ43FyC-s0clFx4a0yOBsw_rgnoHdzu6gtjMT-FwBXmH4sqTmsIOOSPP9p8LQANVGzjOF6XhMyv3pg11qGpmit9GgKUEapj_WQLC3Aj4ms4tD6GBbQYkG9Rwd3JCOMiv3Z-RDG9JYlL1_CNQHXkaGCUscayFe_ndrUtEG9Yini6qMToxFuxXAIiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
برنامه‌وزمان‌دقیق برگزاری دیدارهای تراکتور و استقلال در لیگ‌ نخبگان‌ آسیا؛ این پست رو یه جایی سیو کنید و برای دوستانتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28446" target="_blank">📅 09:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28445">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrK0nfNHHqlBKFRqtKFpwdHUmUQ4g1aKpu-1XL7Lab9w4JzpkvoESHnglUV9wFwgW8u4FUlxhuInTSqB5SvvW_8je2buQZ40IMWQBk3H-BrQ-NC6UZCE7jbIKDtfdWq7HHKN7FouFls-Qaw6lOfM6oLQV-19bxnjaTS38mWa799188ynMXEtsja8iwg_0bVSyIrVtSWRXPEK-fVSQOm-l7cczLSkr111UkqE8bmvRR3jwz7ntJhpn_mAE5DtZWaKxdwh9NrnmIT4of8612ubTtSSKv2GZN7aDb5G6E2ENmRBWCAz-swDafDoObntuwk4o5hGdM6eHDupA21mcs6k1ngRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrK0nfNHHqlBKFRqtKFpwdHUmUQ4g1aKpu-1XL7Lab9w4JzpkvoESHnglUV9wFwgW8u4FUlxhuInTSqB5SvvW_8je2buQZ40IMWQBk3H-BrQ-NC6UZCE7jbIKDtfdWq7HHKN7FouFls-Qaw6lOfM6oLQV-19bxnjaTS38mWa799188ynMXEtsja8iwg_0bVSyIrVtSWRXPEK-fVSQOm-l7cczLSkr111UkqE8bmvRR3jwz7ntJhpn_mAE5DtZWaKxdwh9NrnmIT4of8612ubTtSSKv2GZN7aDb5G6E2ENmRBWCAz-swDafDoObntuwk4o5hGdM6eHDupA21mcs6k1ngRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
موقعیت صدرصدی که دیروز شهرآبادی در دقیقه 90+6 برابر تیم‌تراکتور خراب کرد اوستون اورونوف فصل‌گذشته دقیقا اون موقعیت رو تبدبل به گل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28445" target="_blank">📅 09:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28444">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0ewS3ANE1EkBq-hT1QyoxRuwpOO7SA6E2cjC6dduQ_hxDLtTS3PBrlFm_7uujTnMQf2diTtXyFSI1zWuD5Zuj-ayaA0c4yXDQWEvBBwhkpnNmcjOyttELbL_PQ735Ph9Q3sBhRoKHj-93RUw-bAgQNweWujDPYGEh-ggASNzhGGL53fio7hdCxuZUTiShrAzTaH3PvGPCVAXGP8tw69mHEWNPep9XKLH4Lp_FdcBofmGCvR04yh2lwv9p2WVaO5DPX2kprutmsm90zmufau8ig7vUDITG_6-BiwjNIVS1D_bj6ccQ18fm2IBBxh5rkUCG6hXijVKIIF7be3InFl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی:
کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28444" target="_blank">📅 09:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28443">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RipannZaAjtIbmjWbR1I6GTaU603g2j6DJfh22CVMK4ALcwFlbivD6vY3LY6fiGr0UzvLzHBP3F5x40NtaB9b4rz0Ka1q34NJNgX-eUvLTRJmaMQvazZy05WmQvyDyMJqXVm8uZ8Wn9OgzReo2vpcJzte9CV77OlgR6pv7sgMslIKoOCCnL3zfuV79SKo5HLe5_OJfm9UQqDL05rTRlLXaNxekNEI4vbzUawjxVRkr3ytdcmLsQXddRPPpOjOlzyKreP3h5IDnzzl26Q-a9mqQYR8kDLj8WeBrJvMWZTU6HpWvKqtTdnKNBYN6pI4of90d35ys6YIyd0TB9aJthbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28443" target="_blank">📅 01:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28442">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1b5debf9.mp4?token=A3_W8PGQ5re2UG-ElQ7HvbriB4P4WTzsuwshkUAv2DJ51pb26n1f2BCruQCnHFOkkR5w0r-Ke9yGVHOdPlEgkDtDvlhwpXqG2UCtR8ugkrNm7jCW682cAd_KsjA-U9vo9Q2JJv3O0xJOzWriL4uXyTf4gcL0tPiCBQf-qmyc4U27U12Bg7VRi9HgjBJZX90PYlSZt6qMK2Sw1ScYuVtOd2D9-kmMu7mqK6vsuxLZkXjw0i7H4JxKnOZacvOgrw1aJBpo3G4HT8yfO4fVjajDFyD9z6DJ1cLxRPhJm3BhHjkyjnbtHhm_gCMbksTdHpjud_dJLfSS_bQjGEmZE5gmeBr1pvhx4zLDrTP5cAOSwmA-kekg1xQljxCOw46cQPtEN4olMHpV8nbeRDi0QHgf-TdFyeQUrn9r5EnfTcYIlV0RIMJsaUxI_vPp728ysStak-OpS0XU5JwQqGcP-wWgN0fRGHkEiKLn1rWzbpZ_eWeZ39RIC5OgR2hpof_wA8Hho0Xe0gIYyf3dIhRjZPpyUL4_eErzD_GJ8Ljpbjd6wh3jZVb4SywgrXXCN1GayGacY6udL0zqw222NIQerbasTsdaOfCDQizjvA5Z4AcvAaKl83EIPpzzMQxv_vG6ol1MXISta8_ouX6SkK_7MQ0x7Op0HkYuKmdkXIwzFG66eyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1b5debf9.mp4?token=A3_W8PGQ5re2UG-ElQ7HvbriB4P4WTzsuwshkUAv2DJ51pb26n1f2BCruQCnHFOkkR5w0r-Ke9yGVHOdPlEgkDtDvlhwpXqG2UCtR8ugkrNm7jCW682cAd_KsjA-U9vo9Q2JJv3O0xJOzWriL4uXyTf4gcL0tPiCBQf-qmyc4U27U12Bg7VRi9HgjBJZX90PYlSZt6qMK2Sw1ScYuVtOd2D9-kmMu7mqK6vsuxLZkXjw0i7H4JxKnOZacvOgrw1aJBpo3G4HT8yfO4fVjajDFyD9z6DJ1cLxRPhJm3BhHjkyjnbtHhm_gCMbksTdHpjud_dJLfSS_bQjGEmZE5gmeBr1pvhx4zLDrTP5cAOSwmA-kekg1xQljxCOw46cQPtEN4olMHpV8nbeRDi0QHgf-TdFyeQUrn9r5EnfTcYIlV0RIMJsaUxI_vPp728ysStak-OpS0XU5JwQqGcP-wWgN0fRGHkEiKLn1rWzbpZ_eWeZ39RIC5OgR2hpof_wA8Hho0Xe0gIYyf3dIhRjZPpyUL4_eErzD_GJ8Ljpbjd6wh3jZVb4SywgrXXCN1GayGacY6udL0zqw222NIQerbasTsdaOfCDQizjvA5Z4AcvAaKl83EIPpzzMQxv_vG6ol1MXISta8_ouX6SkK_7MQ0x7Op0HkYuKmdkXIwzFG66eyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛ پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28442" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28440">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YB746rqL_1gBtfuuKBAHAp3rUYYM9GyfUKv8VW4Ahw3JnrLRlx2XG-f8Y_he5h0Q4yHwl0gYSyavQonLCvmc853HNj1V_As7A4fKQ8xzs8sPwclhJrZmbyyM00Qgna3lRZxMTp0Q2Um45EAMNUoBwdnoJ8x8sFIO_MsZxR2M02Dj2T5mOizzLal9pr5tjbCCpDVwaL613RBaEmCF4NbHG6IAS1Xk7BpAcLsFS8qGJVdtMfJ9rxtSbARVpjiCiKqHDqCyWRHxSILGjvKlMwHw4G0RNn_hyttmzWvVIPEv_9eilgTVTJ6bb_yvlnq_rJb6RTQvNU76toXtPrul3VTTcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
فرصت صدرنشینی یاران کریس رونالدو با جدال مقابل الاتفاق در هفته سوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28440" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28439">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpqHPbyJsmQCqoQAX8FzR9qb-Q-4c5s-AM2T_Wti_TDXP0x9OxaKeG7aFgCcJLFTo1BpD7gMGBaPkJkR1lQzSohatfTtbsyrmP8ByyZHU_zRRGHgJRZGBCW7ZIgPWlNhKUB_HPjqQRn9LvPxzCymGDxelvDBj9PGm6xE2qo5OUpOqKhfm8-LKfTZPDrp1t6e2T2cUtyvHp5zhS35xN3UipTou4JpfYzKJsYXnAjKl-qAn6_Z4Y94-cdRCxA-B6MOyx5xP-Xbuw7UxkWWb2KlR96k4cTLuRnxW2Z9CAmvtog4bqQVnGrRJjyOUKAs4xuR2UiBAWoTAx_Gl21qBjIOrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌‌دیروز؛
شکست پرسپولیس مقابل تراکتوروبرد ژابی‌دراولین‌تجربه‌مربیگری درپریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28439" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28436">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d9ec1535.mp4?token=dMTTn5ga9bCdvWAeqLl-AFit50GMwpEFQEieAXBxgkfPZYaVB06id6YfPm6buQqF9SBnSMXRCDx4TfTTdKb3rKm_aOA-DXGhDm3xUv2W-R9oQv4twIERwrAl2wKEE8u0gfWNlFT3JR7rwKKy1Ka-rTMdYydM11X02vlIdZkHp35U0oORxcCsKiNGCdnlTb3-eG-ZgC64rZsP8j3RFnpq0Na261QJnO-62d6ikS9AT1mSl_8WI3szBWS8RGZP6zYAAwYmW281gg_gN4m7RKeGuU57_9PTQKaL05x0vq6yVCsVJ5atHvuFCeXzFLA3Exn6V4LG1Nj3TSpA75jGShhzwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d9ec1535.mp4?token=dMTTn5ga9bCdvWAeqLl-AFit50GMwpEFQEieAXBxgkfPZYaVB06id6YfPm6buQqF9SBnSMXRCDx4TfTTdKb3rKm_aOA-DXGhDm3xUv2W-R9oQv4twIERwrAl2wKEE8u0gfWNlFT3JR7rwKKy1Ka-rTMdYydM11X02vlIdZkHp35U0oORxcCsKiNGCdnlTb3-eG-ZgC64rZsP8j3RFnpq0Na261QJnO-62d6ikS9AT1mSl_8WI3szBWS8RGZP6zYAAwYmW281gg_gN4m7RKeGuU57_9PTQKaL05x0vq6yVCsVJ5atHvuFCeXzFLA3Exn6V4LG1Nj3TSpA75jGShhzwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🇮🇷
رامین رضاییان در اولین بازی‌اش برای فولاد به این شکل پاس گل داد و فولاد به گل دوم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28436" target="_blank">📅 00:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28434">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cATBTAUI3sMtMVTIT0vBPjBkTTnB444eJB8DginZvg00fP_whz-yeDC3JpuAQcUiOqY6rbMFLHpe-3F4r_yXpUzM4KLEAFpxxVA-Kc_afna9a8gFNvOwuzrFZd3fyKlDkrmV0-XFgVYAUUTWZ_aV1VceYdPv3XEu63JXvPlhiqDNE1ASyOPs0eEJaU3VnrmAEqYt_gko_umv-NGNgGrQv2hvLi1ID0CUNkAJItFtzOoq8m24zwdEmoIANZdr5GXwSQDYWkSwO9pZud_aghWsBkjfF6CbzmRhOBzVS1skndOxrG5HF-qv-hG1F6xhSBGzvFr76XiOdOWqYg0vBG3EUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHgctHBaIwUgBdk37pi2Mhb8yWB6J5pnwEl_wNJSdjnj-6nVG6bjxTUV1yVqFLMfrMmmN2UMkNVFXhNY6BLlIwwmMf2TYz-ftTG5a3AhKBQywPgcgLzaoRvk5aQC5gSCXh0bdOfXMKmCEyEgk0e_hIZo8ifQS6soY8d2yp1KrvNOdmHQ4oqDZNm0df3ia_Qq6LBkHvlzhGiTa5hYJKabDh-tnSmQV_e4_iqjjvL0XK6f4PDeAl9CjwwYF2TnJkDbKt-b_Pv-Afnbt6PiH0QLno38UDKo_weqNEkb_rK3ZZ3kcgWQ49qGnkID7wMXq8AphAJ8FtStk_Hly61dcTqEow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛
پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28434" target="_blank">📅 00:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28433">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIBsWPRzAGF4RjKr5YvPnsXOSUmICdHxRUWgXTa8N2IrgvZZvihXoAatYAf7QRNf2Yv1znajOOeE4nWkSYG7SuDdCe-NYAhzbk-_EQbWSA1gY8VKl4x67anLBOmXa33gKC5VzgCG68EW2T5lp1ZDd1Wd81XdsY-qYEMaHl-Od910QaETmWQK6snIoOtM5WadY9wTi1E4x73IDU4r7wSmgPSoaLie0dD-tDD833qMLNgjcUgkSc4RuIFootrbtUKQBoTbHRxsl8ggp4UOIIYmRzwWWxQ8TCustutdY0Xgs8gi58xq1KdN3EpY8jBmpOkr2nVgQZ3fwUTioCjsUagD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28433" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28432">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPT1WLTrN1HaAIt-rt5Eh2l7olx2qrnNSnZeWBLh7jRNV8AzxqWTinGta2yQPqqRzKqG1648Y585J5K7YaCuBjlnOsbtt5SSdYffUsRg1PlpbJfrEjDipJyaZ0PWRgVATVsVyPSkGZbMAYTcA722TE-DwFy_36NgNrc7xSkiSF45HhN_G6wp_fEngL6ZWid8uMY92DkSmNejlsWjpcUDHk3anRWcSQnEzXCo_J6fXSnoQ4PUYqZ3NCA2MgO_Cr-wuwToXNRmuVZtJartTFmjLM23gI4lTEQGqOBlp1xASCHcZjTZtNcpquf6VbcapKlqVuA04JdK5ELfgl7ddzHCJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مدیریت‌باشگاه‌پرسپولیس حمایت‌کامل خود را از مهدی‌تارتار سرمربی‌سرخ‌ها بعداز شگست مقابل تراکتور اعلام‌کرد؛ حدادی مدیرعامل تیم پرسپولیس اعلام کرد که کادرفنی تحت حمایت کامل اوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28432" target="_blank">📅 00:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28431">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVUkqS1OCkTY--2sNBaHt-jpP6gOR1ICJ3TuqEPS__ub8oeqfRZAOuW-U9MqCr_uzGLpxHcmYjeyXzh-90hXeTuDrceivR90KTLNer1WN1lrQYxNkNT0dRV5T9xp126c6asmGQat78w_CPesf7Yvl5xAQSVk2YMpIKC4_ZbIqA265r98pPKbMCec1KUACwtNrL_x-yjq4Hj6V0zCptgxzpdmwXfJDJZyZcjlg4APcgemNmqys7_xGhBGJhEDprTPZjyHARTLYGv3WL2jPqTLjoCGw3CpQzZvNtbndfJUz99ue5fY-RAQu0qvJCqnyF5GC9p4AGQ8UsyTwGsQiuh-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28431" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28430">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206c65214b.mp4?token=OoaDhd54GesUnALItWsdvTeZ0xcjrpfpUE3yuiBH8hsTIu4yRBgLJ6t9SB3Et9hjmvIMShcZeZkMr2-t4Xr0ALhRPz5_eDHcX0HpMhTrdl1j-WbEwCxD6H2pyVULVRSVh_hp3AZRlue9UYX62wFpgeJMjOhea3LCop9BR9leTAUw9S2-d4lvDihCQdY3MPFmNQnVI9h0Ax8gLDxk3DS94BKCdGQ80nsf0DpapbL0P4uSPxnYBgUzqo6CndyvGkgnv67ia8DwHgZUhN-drPrrnjf3NX96AcdXzcS9V3gwIH122Fcdvv3ikN2wn4YP70IQONCTuPsmD6RcdzwveD7yuTEghxBamC_-T_h6pB8J1c3DxyzfRt67dacY2yD1rqHn3QryJMFLcQDVeZzm_AMhcl1TR27OP875iggFMxO3ydziZurlXSuIrH63d_wqs495bzHbnFgFaQQHCRhF1kIZYMBt4QoXGwSnaem8I7CH0AuAsllQX2Ms9IyBZnJnH643kKNM2QCj74qMhT0NAe4CH-XRvOSP2cJQUm2q5bByCvbA0jrktWJItLRFGa-Ti5iT7V7htzqGhs_wfjhvEBybPjuVjUzhYE7aKstBKC57lF5Tq3Q2013GG4vSdSJJzJ7qMD5Jac0SFiO73hxqkoMFxi5d7Rm2UE_GL_QML-VT38I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206c65214b.mp4?token=OoaDhd54GesUnALItWsdvTeZ0xcjrpfpUE3yuiBH8hsTIu4yRBgLJ6t9SB3Et9hjmvIMShcZeZkMr2-t4Xr0ALhRPz5_eDHcX0HpMhTrdl1j-WbEwCxD6H2pyVULVRSVh_hp3AZRlue9UYX62wFpgeJMjOhea3LCop9BR9leTAUw9S2-d4lvDihCQdY3MPFmNQnVI9h0Ax8gLDxk3DS94BKCdGQ80nsf0DpapbL0P4uSPxnYBgUzqo6CndyvGkgnv67ia8DwHgZUhN-drPrrnjf3NX96AcdXzcS9V3gwIH122Fcdvv3ikN2wn4YP70IQONCTuPsmD6RcdzwveD7yuTEghxBamC_-T_h6pB8J1c3DxyzfRt67dacY2yD1rqHn3QryJMFLcQDVeZzm_AMhcl1TR27OP875iggFMxO3ydziZurlXSuIrH63d_wqs495bzHbnFgFaQQHCRhF1kIZYMBt4QoXGwSnaem8I7CH0AuAsllQX2Ms9IyBZnJnH643kKNM2QCj74qMhT0NAe4CH-XRvOSP2cJQUm2q5bByCvbA0jrktWJItLRFGa-Ti5iT7V7htzqGhs_wfjhvEBybPjuVjUzhYE7aKstBKC57lF5Tq3Q2013GG4vSdSJJzJ7qMD5Jac0SFiO73hxqkoMFxi5d7Rm2UE_GL_QML-VT38I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ سردار زاهدی معاون‌نظام وظیفه عمومی: علیرضا بیرانوند ازمهرماه سال 1405 سرباز خواهد بود، و باید ازیک‌مهرماه‌به خدمت سربازی بره؛ زیرا مهلت معافیت تحصیلی این بازیکن هم آخراشهه و بزودی به پایان میرسه./ حالا اگه یهو زدند معافیت تحصیلی بیرانوند دو ساله…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/28430" target="_blank">📅 23:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28429">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9CUzLSmwRlEo_E2BsrVP22PcriTbknPVwS63YiDH2eJBJli1z52llZyVHd_WFNnM-ofrlMIX0uTHu0xrv3Z5KdAk-rt3qRFERTe54iktAeV0fuyp45Lm0_ouCHv1vEFjo7B9B1omRUm_sC7YlFZ8wi0YnwNLXJNAFdZ3cyfQbOJj1p-3H27NuEoIE4FUhkFleqEuj6XVEA98Itwell_uNzscdLPX28c3Go7xi1F5Cnc9mj2WmV6c8pjllMe4pSGzmmN2VhDOdlW_05g3ipU8GP-LeVnTljkVkTOEsywl5iSBVf-Z6YWaRvayj7Od5MEkkcx4WkL45wM3JH1B_PGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخی‌ازرسانه‌های پرسپولیسی خواستار استعفای مهدی تارتار ازهدایت‌پرسپولیس شده‌اند و مقصر این شکست در حساس‌ترین بازی فصل رو او میدانند.
‼️
ترکیب‌پرسپولیس‌بعداز اومدن مهدی تارتار در این سه هفته هیچگاه لو نرفته که گویا به بعضیا برخورده و منتظر اولین شکست بودند…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28429" target="_blank">📅 23:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28428">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbf8bXBFPp098vBTDqnVexWUCxowbPP3G6uXbjHUpef0scN0bsrTc_lJ8JGCb_9AQ2O2n5eL29aeoClMzDzowTtH_lZbtfla-dYoI4f-XcVz1jbv6ntQYp7PwXCxOMJJNPN2khTuROlX9jIGr1Sjxk4YpWdPKnjBrb_A_SFFKzbpeBmv9kIV5eWe5Emhsjp29nLdqX7o9Mygbv2Q-Jp0Ki98jCqdgGgkRzxYEIDIbgOtO6DUuqff7MD_hWY2KnmT19th19b1u-F9_a0KORwAdd1Ou94AY3cWLIUt55Xjaa8qFl7Ccfr_oK7AnN-DqrZyrl_pVZ07dJqk6SWvna2k9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل مارتینلی ستاره‌برزیلی‌آرسنال که همسرش گفته بود رویایش‌پیوستن‌گابریل به رئال مادریده حالا درآستانه‌عقدقرارداد 3 ساله با رقمی نجومی با الهلال قرار گرفته است و موافقت خود را برای پیوستن به الهلال نیز اعلام کرده و تنها توافق بین دو باشگاه بر سر رقم فروش…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28428" target="_blank">📅 23:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28427">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGOMXczx8-8H2SFdBvaZY9juU3j__Z28OCVyLnjnwQATJyW5FDAfuHRp7DdLQP8RluACSTgjaIMovu6tgFqk8YXRStiR1mGF6J2RhicxRcSAJDUA9kXn_8WU8e4iDiIhHkY5mKLYKn192nTXpE8W46x8NEycdmjiHEIYCIJgblJJ7CsQXfSD-9sy1QnsTom_Ma1pYvxjJ3Fi-MHmSbXSwO56X8LOMSolTBg-W5TzqbPko_xm84zA4UB8zvRW_9rfsFfXsj1xog64htxtmd_B7nKeA4U7aqqRm6ogw4a7kiGQbQO8cemqza3ubSzfNDRPsqReOG5abSCYVOourkWX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی و نتایج‌کامل دیدارهای هفته سوم رقابت‌های لیگ‌برتر؛ آبی‌ها درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28427" target="_blank">📅 22:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28425">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jxsscrs9ve490SOSBp1OCaQHSvZ3xMc59Sit9zPz6U_eWOE4HqZ_CwQSTEUOZO5Zg4ecgxCKdd-SK3FDMgei8bRmbCznz6JwKnXoc3BjQBRhp41jpIgdkZTzQnIMQrah6kYETRLzPHKnvs9DGYPrGVBMw49xg5Baauh4Bz6Q118wPQRO-bQsF1PAA9TuMuuToBxthSqK4Kua2Gfi8-fCFBuAgwmOq5xy2aYfTKCErhggoVPFOeUxOWFIVt9j-84RRDe0Kgd1hFiRJ46kvJlz_2pZHDnQ3LxkoIKpKsQQZpCcokQioByBCAUVKxynlurQIcCMNr2MwJ8xXWj46PaTcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GsJa54g-mwo9ljAKyeazwP2bNDsLmbs4ocGQh0ac5Be50j5YSaTNxUE2LaP9Vz4nmPdXSkC2mXIxmf67ibmdZOzh-e4xCA7gINykmy1EMFlAKj9CSKdqbJ8GliojZyEMf2R41noRdVhAVUlnL_KUdhppJlQ0wxqCLU14UmuyYXaDMI5YFkSlM_wziU0uwReAz10GlED0dynqyK6vgKODhj35tWj6Jp0TBHKXh1hFnEtEsFVONgTnlIWRc--dOFb9TRKanjw0HY5TqnfrxIMfCwG671764NLSV2EiHYp5H3ZmbX9jSlX7NozEoYtqXlQxHPh3OnFcEOH93s9s0NpPjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌رده‌بندی و نتایج‌کامل دیدارهای هفته سوم رقابت‌های لیگ‌برتر؛ آبی‌ها درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28425" target="_blank">📅 22:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28424">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7lErCq3fFp1lswAaCVyjS_WiElNDNHcFXxIO3T5HdlkKrFB-hs4JqxoCSyCiOvsZSv4BappS_-824M9lfwZ3pFZRcfZjVzJ_YexJSocJZPI0js9CXhzKft3WLR8VyIxteQ5IaJNN7WFwbYcQdJTGzUug8EfO05uxc-dv7K2NwloZlQSgtnYrxJ2_SiF5Iaj_bErVwKQpmWt91IluZwyOqePhRbxNmZVlV4zUlOMINlFWDGf5Bqbhpjb8NuO6AfpS4pe3cpqRJxIWuLH8nSnMhmcqtRM-Hv-wThhDisyYYVBjvvASoX2ovqRfBhRIo6rP2TYAR0ILcdafUIiWsLPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندم خدمت سربازی در تیم نظامی وجود نداره. علی رضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28424" target="_blank">📅 22:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28423">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFOXXWAPdDnsKm6xJEeTeDnPOo2-r2jMjqFwYsFTgfgHmpMweRXz-SCA3o6Y-aYfKV9mvTa7BJ0CWtFaAMzNnC3YiRizCRsxTN-EQFNogD10N7DqKhgxVsm1ry9AeKJ8JpB8pLgbmzHZEaIIRHZDDkH-c_MQhl8a6AqHsd7jG2OZB9-P-9vExnweMWVGR_w1wJg0oS5zUrRgPJiZDqiATRsytAVxzddbuoZyD1GeHXLpnJGEcvKWjfnyfthb_aEeWohIZ50eP65X7qxX9c4sDL2hbz5rhszkEBSDfaG5TVdzzGjzoXCQMvLjb6ZP3UDgDbGHDMEK7DgLToZP0Rrw0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28423" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28422">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9gxmaR__9jrETN8uPPeSYSTg3V60n1p8Nx4qsNExSvObz1MR455bhMExgnj7R4XImqM3a0Z88TgbLTJjrqB-i3CbPhWN5Tg_o876TAK4-RaDiPdfcm13hJCc8GaqzdfKfQYsS9H73fb5jucmYs55yadIQ-YbK-6J9CUAspS_VYULK7AsgbeRBLMDyqYXAwQ4b7SFpSMfoGOmNoi2NCy1VBherfwHpb0Zn8J2XoU0UafsPKPWMZtWS2cQC6vSB5IQo_MH1rIFnCJCHg4R_IYmtcSsNzyEeOPu8WQGoVV617cQ6cs6KT5kgXnUmOOy7BO_w3a185B_7nQErdGShep5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگاره از تارتار پرسید و گفت چرا اورونوف و سرگیف بازی‌نکردند؟ تارتار برگشت‌گفت به دلایل فنی بوده و حتما یچیزی‌ میدونستم‌که بهشون بازی ندادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28422" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28420">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9248dbd6b.mp4?token=fjo2UUTBa18MT39gYg_P9svemHg1Fr19t_vRqt2NzsbzIjT4I6bSciHecqh8T8dNeHeAe6eeAvc1rxdc7Ev7V_fUvl6QO7YJuqqX_7RT6lfRH1pw7HE79kRP6bi5i1zyC0aDfEWL0RcQbGS33JIHsjmdywccH2Xa2Hiv5Gb356-7jhRXui-IAQNl5lQNwIEm_dPSeqNihsExE2Nb4-fjP6ATcoj7ARli30gcRCvVKFQTCTTveuhQ914cbaXRasNnWHXmfgy2aGZc0FPvuTE40q_FAq9km7zMst2GoRZ93GfTrhw9k_EDlZmJxEyAhSk0q3L8AfE3PYLfaL3H7JJZmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9248dbd6b.mp4?token=fjo2UUTBa18MT39gYg_P9svemHg1Fr19t_vRqt2NzsbzIjT4I6bSciHecqh8T8dNeHeAe6eeAvc1rxdc7Ev7V_fUvl6QO7YJuqqX_7RT6lfRH1pw7HE79kRP6bi5i1zyC0aDfEWL0RcQbGS33JIHsjmdywccH2Xa2Hiv5Gb356-7jhRXui-IAQNl5lQNwIEm_dPSeqNihsExE2Nb4-fjP6ATcoj7ARli30gcRCvVKFQTCTTveuhQ914cbaXRasNnWHXmfgy2aGZc0FPvuTE40q_FAq9km7zMst2GoRZ93GfTrhw9k_EDlZmJxEyAhSk0q3L8AfE3PYLfaL3H7JJZmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🟢
گل‌های‌دیدارامشب‌خیبر خرم‌آباد - مس؛ بازی یک یک شد؛ مسعود محبی بایک‌ضربه سر دیدنی برای خیبر گلزنی کرد و نیک نفس هم با شوت دیدنی اش روی حرکت انفرادی‌اش گل مساوی رو به خیبر زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28420" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28419">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb30f0066.mp4?token=ESxXY76zWvgHMtyHfMFt8aoKTYrLWGQJT32miTFG3mvWxeCwQgWRqAuQsqR7krl0va4qTaFLvBmQ7XuSeDCXpE8og3lViZvsVDruNazpaI19niEpLA6XH6TnYmooHPykp-YlCB9EE4pA-V_wmxM4Tosurh61dP-ZreBOkkxoK-2fjAjOulNBHV1EGekA3F5uLYyumqbBliOeYSDCvDsYIaS5VSBLZLTlywcn5MDd-hxeBLFjxkZHVdOl2gZJJuoTgQ6K8c3vdMqoo3ZzZs4GyhVID4PG81_TWXKhtOZub5QaVPw1_Jx_prPyRe8V2ZaOodE3jhIW9WjsP9ZdDPijWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb30f0066.mp4?token=ESxXY76zWvgHMtyHfMFt8aoKTYrLWGQJT32miTFG3mvWxeCwQgWRqAuQsqR7krl0va4qTaFLvBmQ7XuSeDCXpE8og3lViZvsVDruNazpaI19niEpLA6XH6TnYmooHPykp-YlCB9EE4pA-V_wmxM4Tosurh61dP-ZreBOkkxoK-2fjAjOulNBHV1EGekA3F5uLYyumqbBliOeYSDCvDsYIaS5VSBLZLTlywcn5MDd-hxeBLFjxkZHVdOl2gZJJuoTgQ6K8c3vdMqoo3ZzZs4GyhVID4PG81_TWXKhtOZub5QaVPw1_Jx_prPyRe8V2ZaOodE3jhIW9WjsP9ZdDPijWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهدی گودرزی ستاره جدید گل‌گهر: مذاکراتی با باشگاه استقلال داشتم اما به دلیل بسته بودن پنجره باشگاه استقلال نمیتونستم با این تیم قرارداد ببندم. آقا سید همیشه به من لطف دارند بله با من تماس گرفتند و درخواست کردن که به گل گهر بروم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28419" target="_blank">📅 21:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28418">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e283ffe059.mp4?token=jsVvvC3eWtJLk_00KZ-G1nhdje14bfSfwgcGz57s2C3Os6aS9RjAv4FOeRtOUc8aYNP6VK571iFIVKtyJnMawr3ohR2gSf4XjTs5gGPAZOpM38xQ3I111-aMHk2WyL7TK5vhypN-cry5p_s2wSY339SJjCuR7H5SSSOPuIhrbbFd7RGA05m5wOLfHjLcvaqE1Y_K8vucDfzcL6Ch8dE98phAUCs-IEaCS27UtT1Ge29caaH9mrnkiNk7Y0FKtHPmH5uxsNtonY8_dcBDEwe30h-dIUpAzeB8dQBJHiGtnhUXPF6zJZDCr00oib-_o6A-mFlDhkSYOKL7T6372yH2vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e283ffe059.mp4?token=jsVvvC3eWtJLk_00KZ-G1nhdje14bfSfwgcGz57s2C3Os6aS9RjAv4FOeRtOUc8aYNP6VK571iFIVKtyJnMawr3ohR2gSf4XjTs5gGPAZOpM38xQ3I111-aMHk2WyL7TK5vhypN-cry5p_s2wSY339SJjCuR7H5SSSOPuIhrbbFd7RGA05m5wOLfHjLcvaqE1Y_K8vucDfzcL6Ch8dE98phAUCs-IEaCS27UtT1Ge29caaH9mrnkiNk7Y0FKtHPmH5uxsNtonY8_dcBDEwe30h-dIUpAzeB8dQBJHiGtnhUXPF6zJZDCr00oib-_o6A-mFlDhkSYOKL7T6372yH2vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسینی فر مدافع ذوب آهن در بازی امشب مقابل مس شهر بابک به این شکل تماشایی دروازه خودی رو باز کرد؛ جدول آنلاین هم پست ریپلای شده ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28418" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28417">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuSXxM9uaLjLHynNnW5yxyN61wZ4O58cLe8aTmdbib_PTcSpk5Damk01G8iDduGvE1_flu20DShoZ1jo39F_27orS9O8iFLb26IOaFL4A2PmJNMoglJsUWsq-ivjG7sFejI-ylh8MuFYO5zQbRB5Hs6Se8p1Jlful97lwVzq1QHSrLRnnid4JUOVz-vM14AkXHv4ctmc6UGcI_KvhcOZPTEBVuIqnDx33x7YoeTCxQNF-5Qn4ZpQSQ7XYn8Te32NLpygMLgJI0rgkDoNyx4BtRml7pJncgm0ZhUqWiO-nIgl6G-wcA3gCWN5rC_mLsQjtNp4R-QkdnEqDj6VUaQa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخی‌ازرسانه‌های پرسپولیسی خواستار استعفای مهدی تارتار ازهدایت‌پرسپولیس شده‌اند و مقصر این شکست در حساس‌ترین بازی فصل رو او میدانند.
‼️
ترکیب‌پرسپولیس‌بعداز اومدن مهدی تارتار در این سه هفته هیچگاه لو نرفته که گویا به بعضیا برخورده و منتظر اولین شکست بودند…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/28417" target="_blank">📅 21:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28416">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87affc8d0d.mp4?token=uPiYzcbEN0SOdxuahE1699e5yTWOxR4PoVDZtFQqM45qyAZtzJB9--Btt_HIdeHCr43p6Zih3V1RIZBRWLtvzJhMb2gsrYitfD-8vHXihan3n1Y8q_QS6dpbEKm1pGcz6lwwgqirS0TImDf2WI3BBWEXeIWQdW6cCT6MNXaBZ7VcxfnwSihbttvpJz6bQ76X_pwqV8gAig4e9O7ubADY-vKCZ0B05Fiwk-N1W9J4wbCUOtFMsbUag0J3veTJlINQUILF_mC_43RTnE8h6Y1vjudpj9-T7TZ0mdxalRppKohuIlaOXqL1bCvdhinWsDC4yAB-pFJiwbQtp6Gf8kCrog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87affc8d0d.mp4?token=uPiYzcbEN0SOdxuahE1699e5yTWOxR4PoVDZtFQqM45qyAZtzJB9--Btt_HIdeHCr43p6Zih3V1RIZBRWLtvzJhMb2gsrYitfD-8vHXihan3n1Y8q_QS6dpbEKm1pGcz6lwwgqirS0TImDf2WI3BBWEXeIWQdW6cCT6MNXaBZ7VcxfnwSihbttvpJz6bQ76X_pwqV8gAig4e9O7ubADY-vKCZ0B05Fiwk-N1W9J4wbCUOtFMsbUag0J3veTJlINQUILF_mC_43RTnE8h6Y1vjudpj9-T7TZ0mdxalRppKohuIlaOXqL1bCvdhinWsDC4yAB-pFJiwbQtp6Gf8kCrog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول آنلاین رقابت‌های لیگ برتر بعد از پیروزی تراکتور مقابل پرسپولیس در هفته سوم لیگ برتر.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28416" target="_blank">📅 21:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28415">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2UU-DAeywqv2pUvSFJZTNLQm5Y4ZkXV6EthYJsqDPPapP_ncXH1vm5tN16zwxNoIxcx4UeXTb2VHuFjwv5VlopKw4S0SqiNooiKPtzN2c_ZvjCNtENSDsQq1QHibYIMq1ahVUnggciszTXJPMeYzutqlnvQz_bJPxPZEgP6E3qGp1RTeB4LDoFooJ1NhOTu0phjwse8YkvCSa9N8RpaNBsPtUM_4CWkmZ6XxXopMq-pUBEvNN5nhYAmo7JDZFHXBWlZ63cXMH7DiMFZr_T9cWWTP_6yA1xY8pqv3Fo-EFf7FwDm1S7_G7NTrWbbf_yTJBnZZcqq0zgttRH7ZCfCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/28415" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28414">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgyPPPJZywqFs406RRU2geptC3KjQqAt75drCHvZ1h3OUuTGlKGL5y6GeYnWUhOLzvN48kyXEuFrdvjd4tGDOEfKXhcUh1RYweNmcjOUQT115LgVo0jhVr8JOHl4bam-g_zzegw42lXLk1knMj9SISLRw_9K7wiUeb7XxqmwEJRkJD-_xBo4hPFQFPqhutkAPiqvZeAk3fWlpvUfuyXl5fdcftfq1S2OBADqR-0bNAzQC9NaaK3ZvwGrF9oz6bw6VHomvSUtPw8DEtEh-JoM5HVAm-gfFkzkY_TFP6KgX70blVmYEdHQSbzcZHWQBg-bPulFwvnI7sgffV87jgLXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28414" target="_blank">📅 20:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28413">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U67Q_42TRipINzcC0aP78O8RhJf9kAyE6AVcmw9cbgMAuWeNDzCvZ70mw3OrdCCmJym0gMF-qNYwwn6nU2zEdu3DEMdRsVWsw1gq3XlO6gO0tolf2NXs0pNs6xOQF1wFH0bIVUB93nslemKl0o8UqE1hS1HxmxXJichWHAMja-8xPtrPKwwcjnYijtlCpEPWfBRGUoOD2oNLACdMD9P2N03fzfkZXEIK3WIX32ICO-HYh_O-HIPS1ivEZhFrB0sEB8lq7ivsrw_wE6x5RjNJpLpdyMmMvjteDAGW1A_2M4x6BJw_V05RVIhbjsscdmHLFTQ5dz9FjeYVbZDcVKa1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28413" target="_blank">📅 20:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28412">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGAMCo5wsh9AFpWO-JpSk4skTqS1Vu_YRtvctPSp37dmm23Eyj10zvrb5oyOdOK_bSBlbhJi466A5HZTlB9G7jm2_Hy_4mHub1wxtUoyv_w7tD2NqMloO9r47PweDy8dbXwD6vzgzJaNSdAteEWimDGU_JDL_C_PncwGEkWd55ctI3YaeKhG1h9fVEzPDEXzSVkMId2Pbd1B_5GCnuMBzgONPoJ5m1G7ojLnFROqSl5jaPfJHWtJygE_R1FK_GXpSU8-mCn0eBHhcLF4PdLj9-3DtxqsyABASsxPLAhMWQqKsVPSI149sBx1DgIY_7eSGPAMx2VRkkmbwDKd2Y_M7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28412" target="_blank">📅 20:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28411">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8596f7941.mp4?token=nmibJtm7vUq-m3Nq1qzyrZM1JJw5iYUMf1pv8fferYcBMyYa49z5ZiNBxRo1vyVm9d25d1ELVLl0Zm90lakf6rZgPb4CmZSioy6oEgDh3nDeijK_JWx_cp6sC-CMF-RnGltQMIDxVm3fFsBEQpDhoCCeZc-SVABJOH70haLQth5Su_20CwjmdMEb6sASweb-wpbHW4BglCEHatDrVHLK7Dfcj8CfDlxLCb3YVcgXmi19qFz_thCyDnrzx_l85qZxq4lzH8aonZ-fAO8zFyIfTZpAuqpE3OmmZtfipW6FnNhlxwp1IQ8IKTaWjXySuOJ-7eipUtZ0aFVOpuwwCmvWow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8596f7941.mp4?token=nmibJtm7vUq-m3Nq1qzyrZM1JJw5iYUMf1pv8fferYcBMyYa49z5ZiNBxRo1vyVm9d25d1ELVLl0Zm90lakf6rZgPb4CmZSioy6oEgDh3nDeijK_JWx_cp6sC-CMF-RnGltQMIDxVm3fFsBEQpDhoCCeZc-SVABJOH70haLQth5Su_20CwjmdMEb6sASweb-wpbHW4BglCEHatDrVHLK7Dfcj8CfDlxLCb3YVcgXmi19qFz_thCyDnrzx_l85qZxq4lzH8aonZ-fAO8zFyIfTZpAuqpE3OmmZtfipW6FnNhlxwp1IQ8IKTaWjXySuOJ-7eipUtZ0aFVOpuwwCmvWow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28411" target="_blank">📅 20:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28410">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130f6f7f0d.mp4?token=RruOgiadTFKWr1UNl988_HPGzf1JM5jhJazEntVWcNepRSyE5enaC6ZIidBLFWGJO3VotIngVq26jT5rJhGzOZS-Av6CrJBKc2n34cu8xjgfYQOkk1NOFrGnIFLZuQuZ-RX62zTtyv-_t30nr7jDSoNU2zdeouApxHmg50e2PyB9QCwlskSlS_87x8JDKzT5whyDBXGoREiYowUehuSAouloKarm2sAw2I5MjQHZBdDKrwk8yZmCGvHWhtAo-D-bCUl7G3mBvj1Dl3O3J1FXrXvHi4TZSrmwn3GN1tgKlPll2UB8NLzVA8klvE8L0oZOT8rwGo7hQsyHxo9JV47BGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130f6f7f0d.mp4?token=RruOgiadTFKWr1UNl988_HPGzf1JM5jhJazEntVWcNepRSyE5enaC6ZIidBLFWGJO3VotIngVq26jT5rJhGzOZS-Av6CrJBKc2n34cu8xjgfYQOkk1NOFrGnIFLZuQuZ-RX62zTtyv-_t30nr7jDSoNU2zdeouApxHmg50e2PyB9QCwlskSlS_87x8JDKzT5whyDBXGoREiYowUehuSAouloKarm2sAw2I5MjQHZBdDKrwk8yZmCGvHWhtAo-D-bCUl7G3mBvj1Dl3O3J1FXrXvHi4TZSrmwn3GN1tgKlPll2UB8NLzVA8klvE8L0oZOT8rwGo7hQsyHxo9JV47BGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این صحبت های جواد خیابانی روی انتن زنده صداوسیما که سال گذشته به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28410" target="_blank">📅 20:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28409">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bd5f94c2.mp4?token=i8VijJGOOdBKQNYfuaX2JKoPO0bNhIZ7cEaiCXKVYGfV5XrTnkJGD7gR-e7I-UkFSN0Mu575UZPqX0_Mg6fl1v0vrm1o1l7KaweJccBBGA8MaaIRDFdcfmP9FejEVR7JtpU2GfVShcWpiCNyaubjetBf--icHIl6XV86dKfDSJhvXkRy7q5Lnpcx49s88hWgjZPZ85DhjVw4Cf2ZM2K81TOsljhtbz_SKEnAqBwtADUPgnWoL_Cb0VfC1NddTje2QrPxmqisbLAB9iOqOg4Wp4aVGGuRGxOgrMHj6s5rLMlf00eSoiw8imI7QWvTc04DvCWMPYSm02DB2BlCrukYRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bd5f94c2.mp4?token=i8VijJGOOdBKQNYfuaX2JKoPO0bNhIZ7cEaiCXKVYGfV5XrTnkJGD7gR-e7I-UkFSN0Mu575UZPqX0_Mg6fl1v0vrm1o1l7KaweJccBBGA8MaaIRDFdcfmP9FejEVR7JtpU2GfVShcWpiCNyaubjetBf--icHIl6XV86dKfDSJhvXkRy7q5Lnpcx49s88hWgjZPZ85DhjVw4Cf2ZM2K81TOsljhtbz_SKEnAqBwtADUPgnWoL_Cb0VfC1NddTje2QrPxmqisbLAB9iOqOg4Wp4aVGGuRGxOgrMHj6s5rLMlf00eSoiw8imI7QWvTc04DvCWMPYSm02DB2BlCrukYRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28409" target="_blank">📅 19:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28408">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7JSeH3fJ-1oU8_UGj1PCCmxvqiog_snftRNtRXHibZulcXSkl0bECEB-ck-jroYqWMz1mNiBTY_xMZc-K8dpP3SvWo34oNs9TuT0-0tu46NywhjmKGKm1C3zlR2eZwaI-G6V07Rg9kMaUDibeOoHvG6LF0xi7S0_BuF8Kxf-ToKNVwVgEDRKPC3lqtWqryBbj-X9GhZWIPMlu5XxrrTN7Xs6WHSA4T19C_AFjztMUANqHWL_9mJ7oF6gq-tDeTKqBcWkySzqGwzjafyqxtzV6WVVHyPWueNis3ND5bZLRvmBLi-aYQn7jKtUXzonEhubC5WBYk-ac-AwLRqiLYDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🔵
درامد باشگاه منچسترسیتی در این پنجره با فروش ستاره‌های این تیم: بیش از ۴۰۰ میلیون یورو!
‼️
ساوینیو ۹۵میلیون‌یورو؛تیجانی ریندرز ۶۱ میلیون یورو؛ رودری ۶۰میلیون‌یورو؛ عمر مرموش: ۵۸ میلیون یورو؛نیکوگونزالس۵۵ میلیون‌یورو؛ جیمز ترفورد ۴۶.۷ میلیون یورو؛ آکانجی ۱۵ میلیون یورو؛ آکه ۸ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28408" target="_blank">📅 19:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28407">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfErJMAmDTYKoFWaOgTqr8UJRl7DizriKcbsFdspIPW5dD71OPcFbsJ_FttddvL1S9bZblgxSC-MJea5y-wnkFVI-bYVG2J_TOWkS8mKt7CkE9wo4FmZeoPf5ITx7_jPzWI3E1OW5JdXoPhF0VF4KsEL-bN8VRQyowiQ6g5d4STKUxN_oC_YTBEYCQ8uj7YRc9gs2ptnxr-wets_cIf4PFaa9BtKmVN5yWcfpzLD_1HsJtrw0yAIqpxXS-3Hp3R3lA9uDax01gAxbouBS-j8jBVNK-no4EC1o1MTL5FAZc9MJUKeHqJJ1jhpoP3y0GAtT8LU3plH_RRGfHWmwHdwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔴
🔴
شماتیک‌ ترکیب دو تیم پرسپولیس و تراکتور برای دیدار حساس امروز؛ ساعت 18:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28407" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28406">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtYRBrB5T6pf8zEL659FkIEaObNOLz0IkWUn-G5oUmD5q2lO5llF4ITid_GV3asnb3BQcyvnliDWuNNuVn9kiJSMtwSyjtTHcEF7g_U2EURrTtyAX9KXYulOEd5-LK-JxG59Ldwmq8L4O5XjtOFJvajxtEJ6BUiPkS4lLIWxixMwowa5UfYaw4fLRhVMpbtkBBHIix5rtZgCUIoAV329YSB2li1WwdS-O1RsbI6zGeJxNQ9f5oRSfvn5bL2X0YHuGKlOF-xUReRN3-A8Xcz-695EPYDefu5sd9FUaYbln3GdwR_IdzyF-YQldEADrtXRcSfnYk46bF8WG62EIY9ajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال طی روزهای آینده 70 میلیارد تومان به باشگاه ملوان انزلی پرداخت خواهد کرد و مدیریت این باشگاه هم رضایت نامه بهشتی رو برای آبی‌ها صادر خواهد کرد. تمام توافقات لازم بین طرفین انجام شده. بهشتی تا نیم فصد قرضی در باشگاه…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28406" target="_blank">📅 18:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28405">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7DMy1edn5B1_Tyu2WlC200nFNBhHRI2a1z9boatLktGmrjS-x_ScHw5ac0nfLHPJkK_FUlMrw_sjxrsab-y9kH9NQJRv1ajhEwFORQcYvSjqBQXyH8-lpyAsIgubOBn1bJW69T8BIASeWygqJaZyBw-S5zv1JlZagEIOpSY5Y7XKBmeZZ-SNn_xCACF7cpLUdWLXKYsKmX1_LXxqkDn_9grYVdpGgwMBUts5OrSvC7UXKsi9x9r2Lyxw1Tl-MqFa-IsLqEZONMAP2glGZCRUWca2q6Oi2hy3LyNJ0KCH6it0ZJ7_5lP197IeqJsDnM8BXMocFTQOqFH1ow4-EGjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیاناتوسط سازمان لیگ
🔵
بااعلام‌رسمی‌سخنگوی سازمان لیگ؛ یاسر آسانی یک قرارداد دوساله تو سازمان لیگ داره و الانم داره سال دومش روسپری‌میکنه و قرارداد جدیدی منعقد نشده بنابراین هیچ مشکلی در این باره وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28405" target="_blank">📅 18:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28404">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOtD342LEC0N-lAiKfy99ugldUCKyrMI2_4CyiE0Ir6Ww65hlfN7XTVsZUi_YTBdx9tg9Tthrt1hZHIJQka7eEMzN0PP6iaqqdF7KrhbweTMXqBkHhisqsr2m5qTj5ZIeHUrluE34P4muGUnX4dNzjXI9LH3V8NF4HB1jl6gYYxpkEnxZ20HRxLxsH2Dz69_XtFeMNvNj2d-aXd3PvEUVWMXAczhZ0slO2b7jIjqbklzakKcbZEWc7hYjoVUv_QYae3LgnzMhKuZnfXozWkCkPC4HkgZSekx2aKTL22ajL1MiB0SVRu_iL-yCOnnrOwv6MwUum19NMD31ErVPIK3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
آمارتارتارسرمربی‌پرسپولیس درتقابل‌هایش با تراکتور: 25 مسابقه، 13 شکست، 10 مساوی، 2 برد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28404" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28403">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP-wsz8qtszs4fSfmPZUl1-Rdl_2YuUz72D5ybzAOgDO6TUzmKt-3YZdiPp9KwKtno3cghDsWG5nPoiSP22IV4M1pFA4sJwAE7gu5uBRgPCqtZFXM435D9FuGgNzZSChtiOkHBJPEvwylB-LZ8RW7sZMvt8tNQsnXk9x067vsFO3Nb9FHzp4vZYP1ndJ57WWmqovyGgVPZVoCX2qzef-aADqdkJXXd_LbBFIYtROP_yk92wnPzeijh5cqLk6O0KxI38uciPAIC6q4hKfRD7uqjCIKAqT7S6GArvd10gUxr3sc-3MeKjf3Cnmb8qMnpHtRptaPEircBkNsBacu-zl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشریه اسپورت: باشگاه اتلتیکو مادرید آمادست که خولیان آلوارز رو با دریافت 150 میلیون یورو به تیم‌آرسنال‌بده و توپچی‌هاهم برای پرداخت این رقم اعلام آمادگی کرده‌اند و حالافقط‌رضایت الوارز باقی مونده. سران اتلتیکومادرید به آلوارز گفته اند تو رو به هر تیمی که…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28403" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28400">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mNcu81hfZU_ZgImh7-yVsE0_pJ_IzfUFuKISx_lIXCce5rKqm4t4FLiByZxwkT2NOGYIYeMvxU_ANa3cnE6tJvWQir9R8te7vpsYZZrlr7i_pgPRoG_yB5eGmcIKU-kzuR-VK7ADM3lo299vMq9-PAL75lJLgOTQvebiRxdOYJBW0JoL7Go1kvW0lncn0waEoTJ4xKDwI1YJN0jr5Xu1JBOB_0Hc-cDQ0L-zpHRUhH8bBcwt7YVhlnRSWYQSVLFEAJ62Aa9x9eZIs11AvA4ByRImcGixljN3vp1OXR2qzIsVYPfaboD8Z2izWk9kv2bObEvQyZKOAALklExlLqJavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bH9NT88PZMIWcWtzl1NZ2rh2flAdLxORlj7_ufZjlyiAeqbSERqtMs-WBZ9d5uVHEi-RhipsOnANaUBJzix6Q8_x0G2KEz6o-G9S94s8_ylsA2kpueJMO3oCyCfHvqbqYh2xlu6WXTuSok8gi4GbgVgOaLGP5SYm4Kq-Kec9f_fy-kZc6IdZ6LvR-GrevD3_YkE7iJN2nR8ha0_QZziKNbGCdXvRmtAhSBqawTOVHMvcbZYh6lVQKj7B7LZQ6gusIBZkUlDz1pFZ5wAgoJV4fU4CCXgadGg04rSsbRUBJcIz-CvEjSxzYkmHNANv8wSXQpIS3AEollh-mDVb0IJD1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته سوم لیگ برتر؛ ترکیب رسمی تراکتور برای دیدار حساس امشب مقابل پرسپولیسِ مهدی تارتار!
🔴
علیرضابیرانوند،شجاع‌خلیل‌زاده، محمد دانشگر، مهدی شیری، دانیال اسماعیلی‌فر، محمد نادری، سید مهدی حسینی، اودیل‌جان خامروبکوف، امیرحسین حسین‌زاده، مسعود زائر کاظمینی و…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28400" target="_blank">📅 17:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28399">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dof_vlxENRZuPE3I8-ZXZ5ko7LVGp-iF5V-IvvCitxeiBNoaK7bOdPv6vMEHzQ_dBPkI7u92SOHuO8qn92EGEnxxG3F_hziKSzScJ97_FOYYhxS5hweox0XEHnKMvp2nr-LPxhPBmy1CnWHriV_SSGeTWlElLLVKBnGNdF7uMVYY7MBTBbjv7c_nOHXmWTG0BZsfqDWyGXVYzj8rpB1uJFPjht2lTimZfWeNW4UAashGRPop5ulQ0HWiqcehR0CF0L_-pMrOtph_KhEy66nN0Fgu6a4s2ElslGRQnvOWVO9i4FOXZa3r1HbNwjuWic8vv4r-EeUpghlw4CnNNQXjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28399" target="_blank">📅 17:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28398">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqs7T9nnmq2dExHainy4cGlbNsKpahwxiShxftCxqcaq92nCzF2w3ktE25eXghg6f7nrgFIOw9TihLYY32EM_82dzDQUWCTo1frQ-T_QbqGZAG8T1KBePg2cVaF3pxOSsj200IcxQXCUVeq-PJdTU-yD406YJkEVgi-QnQ4W3DAIUQ_234QlNH1VXTH5Ya2V2eKA4INqTAQmzBMANC2Mt4XUMwPEtZ1ZgeSbm-XLUCwRL4YVlOJDgBJu7LmDumtvow13JgNu9ZRMrz-a0e6GKctgWaeOO3HUofmlAYLU0z1RfKzZGyKAuMvPau7Hj_Oa0Icz5V9-0SunsaXr6cB4oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر؛ ترکیب‌رسمی تیم پرسپولیس برای دیدار حساس مقابل تراکتور؛ ساعت 18:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28398" target="_blank">📅 17:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28397">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJiqDo2cB3o2RnVZjiQ1P12dcCDtkrrsrtZUq8YJPFqKpVuLg1SPR8i0y256L4af0zZRISCxqtLCJ34jsEMCXARYCmF1JcrrM-rEDFW2_LJ52wwhzbqnOwuUrOovoc2c3iNTC1b5Zg3xM0uHXSxYIn59GCAgut-f3aWz0ErKgHAweO0tKg3hLd6mjKhHrofBqW_TqIkKKhhFmVQUvpbl356xLG3wZjUw4u2779kYS3KRNiTwNsBUsAOHr0RhixQ_2_yKBWFMpwjHME7zaz6HzEbFiQJlm0F-Rkf10EHTH86aZw1oHFvmEGG48MMux9gjyqJpkRHZkVSBGU8ho3sSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لیگ برتر؛ ترکیب رسمی تراکتور برای دیدار حساس امشب مقابل پرسپولیسِ مهدی تارتار!
🔴
علیرضابیرانوند،شجاع‌خلیل‌زاده، محمد دانشگر، مهدی شیری، دانیال اسماعیلی‌فر، محمد نادری، سید مهدی حسینی، اودیل‌جان خامروبکوف، امیرحسین حسین‌زاده، مسعود زائر کاظمینی و…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28397" target="_blank">📅 17:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28396">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTm2600wOY8rWgE70ifZQL7C6Y4Qt3CfM70getlvCtJ59Mm6wi98_EkOv3IxckuU2ZClCKp6mztDw9Jd2-O0q1dDzEW2kYb5a8TQS9EFhEjU02Csg-bBpUVqopOxH288vlMLLl8wNITkq5UA5xeuOrCSSvaYxhXFGa-bI0sOgaMF-Mi9WjNWTRspEQskb0KP7jKWEklk3GwGvguFsuhr_9NF7Oim-Qe5rul473f2-MLyaIUxGA3LrRAxG7ixMBeZ_1vwt0Op2XKYRmnmbpf25yp_2BJBGcmif3mysNTJ-gxsiJhq7WR8QhVOWUPUcN6dLFEHknEtGDK4yrp-QS1NHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌هااز تبریز؛ تیم جوادنکونام فردا با این ترکیب بمصاف پرسپولیس مهدی تارتار خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28396" target="_blank">📅 17:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28395">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebi-EYwt4SigHBNY9Ex6bX33S48qD0wGtks9bE5DoBnjpDrIAGwZSk1rxjDoHOXwDXbi-esrMyE4Yc9dnxqeg9nxVXKib2wOt9EBbX1NRIhocv4z2pQADZqAJCudpAOb0MgFgRw4uYV4YI3RFh3gPs9kqpHD2qOsjfYRVkVcu27lu7rT0QrDgN3-7Mh9iVzLHvmY0bSiYBOafz11X4jhbwvNYRFfS6_8Z0zvP4SnVTux2qLZ8oSy8TUKc9UKe6Put6-_CmTRvJt5WX4ApHtreKGdsBOsH3_4wQTQdmmjJQIknZ0JgnGrmXA36fi9MKbdKCsohLOUTcBQBpFzVtaHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28395" target="_blank">📅 16:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28394">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiUuKyCyxK99AYRdm14JgmcGK00cmudhlUPxfXsEv0EDSVgPRf2VkAomrMiFM-GI6GEqf8kfHWvg0Ll9SsfOZZHGXh0VPIaLolpkpooGEazHKgUkGfm9FFBVY7b6JxULRUyPaxBlebIL_sAgfRMKN6NK75Fh8WhtECERmsoWSuOTpIzmI2Y9iG8tjStSHCCSi-oaYcD0KSIZ77aB_iyyItuiFwFKEwvXWNXSsm20geZ2bZK8poUYo8sxV2lbBrlaPsqpI6f03bIVBKjIAkZZbPsjL8PrwDchyHe-VMoKV8w-2icSJN2n2Y8FLC861nCjeNwF65I0WXduHbMycgXvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28394" target="_blank">📅 16:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28392">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8AjevGJlvsvRdl5niNZ5HaHoNcmHpna84zv36zTsrHjHawbJYqLmtTBjja-Ee0FHRBcVLWc0g6VtArnCIZYo7KY5HGxcAO3N-SZpLkN2b7CgvzHxzOXNHjs1wb2ba1iaGp-nJrluHw8Pqw2V8LbaBrzeWJ-XZJV1rc-WtjtTH_IyXobqTVtWqbEib3Ncl1tQCrHGgh8GMrBcEDsIT-vmj-DBVjiclEtFfio4Nc1K3Ve6Yn8D6RRABEHLJnE03AxLcE-scA4iAEp12XwGZ8L0nQ00Usr5AkM1x4sV_bpdkl8UKdfe4PlLah736Lx2XQV26hwv9PeNVhrztN7FX6hPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
به مناسبت دیدار حساس امشب؛ تمام تقابل‌های جوادنکونام باپرسپولیس درتمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28392" target="_blank">📅 16:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28391">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISnhCXQqnaolV7FK6JzHFgpci4JwJmWYJS1gaud7YkKnLDGqKU1oNjEztoPtxFCMP8AyuF8Ck3gEp22Qn3fU5uFVudhUn95aWCRPlv1LcB8HlG5yWsuwg6GgYXJQOZx6_aahB60mav-yrWPXVTj8jqdGVeVJ4DM1dfR-tqVo09dWvxnD2ZmyY9EWZWfzNqMK0Varor4UYhP1nh5jNLiMFg42LwxZn-OWjLuv6a3Wiyzhu98hkWeP0EY12kzcgJSMclFVkLvOGKUL_1ws221U4VEOA8X55k09M2HOrWVzcZB-G5ZeXab-oBZC7AM432dKyiriI3IwsP40tUVmTWkVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌تراکتور به همراه نساجی، فولاد و استقلال‌مجموعا ۱۲ بارمقابل پرسپولیس قرار گرفته و آمار دو برد، چهار تساوی و ۶ باخت را دارد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28391" target="_blank">📅 16:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28390">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6PVgpQycKFGV6g3w_OWp6jjm7hJFjwb8S8iytJygnPUU6Ub-Kt7WV2UlBhodOKySflEZQCRALLVTLA89GDyxMSxfFpxFYK05bJtn-6_8A--GNJ7rY049LLGlSrVdpCMmSvM2Qp82l8LCJvbmUhfmWG-uvJycWGHcCVefrYjsds55Y59Z1wIEfZ_-E8Gut6fuED2B0vfnBuwIETP8da7bz5K1Bq_Ec_6MRO7fOEaxUBkFC8wRWRctBdnXjD_uC7kO-izfHjqxr9X4sIwaVDFV-Dx8FQso7TeQuGyrV9xLVjqLrKlaraOtbsRPg7YEQ4Us7pXnTfh5xnmdRLoDqCklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|اسپورت: فلیک به شدت علاقمند به‌جذب سرهو گیراسی مهاجم29ساله تیم دورتمونده. سران بارسا قصد دارند که در ژانویه مذاکرات خود را با مدیران دورتموند آغاز کنند. گیراسی بند فسخ 50 میلیون یورویی در قراردادش گنجانده شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28390" target="_blank">📅 15:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28389">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfc5_rJMx1AisLmVaVBVlAR5LMNEok33ZZ8izDIn8ZU433Sda066m0d1hZXsI5jh9hmU9JjO6o6GtLfKKrXt6AoyD0p_V13sV4dO_BLSnhovCizOpMNMzwVQn4B8rry5ZqK2nzxJ_lhUQfnQ-XarAtsiPWNF9HzpbrJs0N5GE5nI8cxAE-w94683jjbYXaV3ALY9qyqtJAYmo_r7lV2BymaW1qHe-Ec8_bm5iRcQa8nqaMzLwF0eLUGNSnmztzVwYFJzrngkJ-ynKd6WG03qcfOhsI0OInUJmuI-PvFRkTsUYDr0-mk9yWuXnwufVGrUZh6Iw5qN1Mj7onNvz2YvwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
رستم‌آشورماتف مدافع29ساله‌استقلال که در بازی شب‌گذشته‌مقابل‌سپاهان دچار مصدومیت جزئی شد بااعلام‌پزشکان‌این‌باشگاه هیچ مشکلی برای دیدار روز جمعه با فولاد در خوزستان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28389" target="_blank">📅 15:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28388">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRscp30qL63R2Ht2UZViv9ut_bO-QYFOzenlAigXqjooHuaCJSd0ITjfE8cHN-xcHB9BUOZDO8MAGSkOLi5_lC1lxCZ3Pz6fw-CRsmahqcgB-R6AHHA8Iu4jg8QBCNCumAxIZ0XFeGDy91Ya3uE31Lc86sE2chEpGiQP2n3txnwFHxtGi0KZsxj-rWldELeThO548_T_7AC8JZXZvUfpfu2zSly40p9u6NHTmesjQN7ABw9diqWm6VYvR7e2HRX0AUADmuqDtWUdKLd25mjBcSdDuNlgfuT01qIidH91CRc5Gw8VXe31tOHgDwsm2I7xYut6t1329Gj-RHl9MQcpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایشون خبرنگار باشگاه الوصل هستند که از این به بعد در پایان هر بازی این تیم در لیگ با مهدی طارمی ستاره قناری‌ها مصاحبه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28388" target="_blank">📅 14:26 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
