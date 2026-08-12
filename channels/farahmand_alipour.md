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
<img src="https://cdn4.telesco.pe/file/M_53fvqR4SmW02ZuVZ_Wtgy27VeNp9vJ-iKO1VXRqzKXvqQA8VaRljANNKvkGpB_OmdldKGVZuDmua94UcF3ij9h0HuqQAu0wnDHE9DEBaGBJ0tYVoRYJ7BWb_AF4vqhwNtKX97zy1UpraSyV9zGxIqFwoA-p0qBsWTzWiGjWjDyBQZgCCHeSBVjM1t1O-q2S5a1jS_wdNqh3r65i0kVT8bucG7jAjblEY3rQaFc160PLiJAo5iUrxzV2jFjRwKCosoO8lIVynbXiQhnmfU6aPsfg40z4HTX7-lT3e665FP92o5SBM5Hg08ReQ7yFDQ7XMuyXtAL2Cr9yaJvpX1g2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 10:20:44</div>
<hr>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFgTgBAaDE2Br7NXyrmnp5A7QvsRMXp2Ck7ehAh6P5elVRLqj4DKosPXIv5ny_gZodWWg5Vlp2w-2LdLpg6w8Ey9BOso-f_FOtcjTUS5LCCGQk12txvQ614Jvec3C1oK6_FJjC-JMMpFpqaOwzXq-j7MF8bvs4tqiztpIeR_i2ZGw78Gzgs-DSVzwgbNjCKM1kQOk_Q8twxYata4i2OS1XTBLxgfYLrGIn8PJWUA_vq_2FnvYdkIOqe942jVvaZJqta3eTKmdpUzVYwBDt_LCBn2nr-VsMuDAF4yQwpPthLwrxsBlB76FANGE3ai0AZPiF6hgVrNudc-oWl3gGYypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=laeL7yj7jOWnMQsKa6kk3qYtRQErfrgo8S99ShsIDqLxz3gULigGt32wat-oYLcB15sUTVZTjjMqipgsSUJW6zHwB98F2iA26yQbiIzFy8YbSL60saACkghpViKtOXsWt5FUmKQ80NiN_vmI5ZhuI0AJJ1jFWexLFkH5aXPCFASwWAod_f47kHr_mug63YPerOD4coRmDopnZk_40EZRAMuckwELtu1ntpjc6sNVuCLN1Vr3JS8LpVl8xcomm2xUncDB-4htjOMo1AsetPUjZfJvvaR2K97IZf7rvd72lzDRoZKoFu647oYwaswvzpLag0xRlyCtyZTSYvJuExbsvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=laeL7yj7jOWnMQsKa6kk3qYtRQErfrgo8S99ShsIDqLxz3gULigGt32wat-oYLcB15sUTVZTjjMqipgsSUJW6zHwB98F2iA26yQbiIzFy8YbSL60saACkghpViKtOXsWt5FUmKQ80NiN_vmI5ZhuI0AJJ1jFWexLFkH5aXPCFASwWAod_f47kHr_mug63YPerOD4coRmDopnZk_40EZRAMuckwELtu1ntpjc6sNVuCLN1Vr3JS8LpVl8xcomm2xUncDB-4htjOMo1AsetPUjZfJvvaR2K97IZf7rvd72lzDRoZKoFu647oYwaswvzpLag0xRlyCtyZTSYvJuExbsvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=Q93lqxIGa0ll8WR5Zm6SHnP-FgoqDDo5UY0BXlxNC99ABjPFFO9z8ux0ZzR2QO-b6kWK1isvX9wTIjUWjpVLx3Gd74a_SPiryxE45Gw4KhUHUed_LzmDV1H66rEWy_B2vE01IMQxnzvQEoYD3JZ2nFIXW_CHGVXQLsxkJBirtwjPi0NQhWWh-hjFqFgp5kEWEygJOvGu4g9NyzFjHVtxkuM-rs0G870b-ZxYFoeJ4--i9XmPQOfaOdTD8sCM0HXrvr15B1A-td5NSCgsAk-uGZBuGe2oXezqeomJhoVwZoRffKU327BX-6PV6dMLf4dUqQch6FAKPvoOQMjVe5YkSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=Q93lqxIGa0ll8WR5Zm6SHnP-FgoqDDo5UY0BXlxNC99ABjPFFO9z8ux0ZzR2QO-b6kWK1isvX9wTIjUWjpVLx3Gd74a_SPiryxE45Gw4KhUHUed_LzmDV1H66rEWy_B2vE01IMQxnzvQEoYD3JZ2nFIXW_CHGVXQLsxkJBirtwjPi0NQhWWh-hjFqFgp5kEWEygJOvGu4g9NyzFjHVtxkuM-rs0G870b-ZxYFoeJ4--i9XmPQOfaOdTD8sCM0HXrvr15B1A-td5NSCgsAk-uGZBuGe2oXezqeomJhoVwZoRffKU327BX-6PV6dMLf4dUqQch6FAKPvoOQMjVe5YkSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehRwrwTTfHTZEAAkuJ_fPFbkAduzwzO3PLrfBTEFOmt5BGOdngG8rBZIawftJ-uHzaXl7GFeHuKoijh_6O4IM8PYDEeGdR-li8aVgioYJtVRty9JWWYONpLs6vCiY4bCSkcKdX2mvQqp1jTUSHku-RIS24H46sJmIDySazYMPRFn0zgSasgib5KOJTAZ6xb6K3rtRzbGD3BHTGPZzdQuRHKctmL-vcZsWlW-ti7zrhI0eExQ1CwoQLT2nN6NMOUmSpo5Tt9Zzhj2w8Svl5AH5HMIfFPp5jQ43r5Qjs62h9eU3zAZAHlydCvYITWRaEJf9S-ekXkbgBRudTefZIkMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_RrAwsDMLyEYVlAP9O3cIHoqt1m6TKIwr2Vpb02KkW9oh8LmzojNCkuQwGHvp9eovnYJdvwq8BZPwwVkunlasHl2f49SMCXFYHFvPbADLSuE-5yEJZaGExpQGtrboXyfyKqB6xLwprqiXMFoB-Uf92VDhnaydsY2-HBlmEZWDlQMlG116xJnX6-KYtA4kJHQ3o_l3dKcR22aKyD32sXWJiSdTX-zkpzhDjKdFa-ZIIoP7sC0VfkW82JrvUkBcrO5BiKKLHdgRhvNarXGbyK1v7b-yBHqySLF3t3rDmWE0Yp2BnXcPQnPfiCJf6Tf9VmTyl5Z70tRZFQBivAK7ZwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InrP1RXG9c8B1iPcB8ieq-FQpv3bhh-T0ywnM1JIJWTowuSo0puOTjoq0QwhuhPQDosoNYk_A8-yW6cKldCyLl4hk6ABhTPmvRLEjvjOu11q_nqAvDTzHfq21JQn0Xz6Fyrxu1dFmrwSiFXlb1fD_ubP6l2OWWbPI-JG-qpv8ZTd-Ka__yiZz7gg9ImrcZEXIInnODMvlusFzHM3ppi9KrtUoWSeEr5owyOJUafHNrOv3-zRCQ4YZqBehION8EMwb6Pe5k6TPgHEhWDVIInr5ZbRdlFdk_bZs44SIH7JAQb67u18XUHuKJ-xzZIcP-Fhj2CLhjsrOQBYxCRjI0m1Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=QF1dmjFGCgtwiaXeDHuV5QYl4Bw85TS4jjHSPGOVJPh0bapvqb5iSYB9F1Anh12P4TtktW075_o5l7b3jXGmOZ3cmmMBoJn1CeoLIvlVMg3kvbMSDdixn4g_8XevurVwgvnHBwu_XHoD88a5fKL1tnaHhhLWyaRZbjeoFok6T7hyw0JMzhQxKKKQeYtjAt8GXYr1JHPR3QG48sG206zw81YKFxq0RgKVK7d0K1vmzaz1e8P7pnGP4BFFj5EMkFHA3vXQMdlTXwbi2hq6U7C5P7fJ5o7HZ-BGm4DCIozK4G-jaS-eMpFawqx9t8d0sVMu56WPufqfjAfOkU7WwtcEwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=QF1dmjFGCgtwiaXeDHuV5QYl4Bw85TS4jjHSPGOVJPh0bapvqb5iSYB9F1Anh12P4TtktW075_o5l7b3jXGmOZ3cmmMBoJn1CeoLIvlVMg3kvbMSDdixn4g_8XevurVwgvnHBwu_XHoD88a5fKL1tnaHhhLWyaRZbjeoFok6T7hyw0JMzhQxKKKQeYtjAt8GXYr1JHPR3QG48sG206zw81YKFxq0RgKVK7d0K1vmzaz1e8P7pnGP4BFFj5EMkFHA3vXQMdlTXwbi2hq6U7C5P7fJ5o7HZ-BGm4DCIozK4G-jaS-eMpFawqx9t8d0sVMu56WPufqfjAfOkU7WwtcEwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=Nt1CdbRESUL1m0PHIgfRcWVXVuQi-apn7edo7Bi2RHhx4LbUekcf4Fyby4m0y3klZxHbRAzDnBIVUFbOe4Poo8mdZCBozFX4qd9obVvHzILyeKpycjke1Pf9sVS_TYwpTnSEHt7NgwzR71yTB67BVd94f2SbJBSQAN07qVcO3JwRoKFvEqPlE_wvgrav1XXAjqoLP-pZe8lr03PzWACHvEDmLVcnQ2KEcrBaFGho2ku4zhdLwTa1gUUpdBbP9-wnPqgNi2FPhTHSeqYsGjHNHRnOO1FDCac5-JI_SDa9qT0g5u0OeSbb_OKj58emyn1kDzgGsqGxCzq_sSLv6XwKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=Nt1CdbRESUL1m0PHIgfRcWVXVuQi-apn7edo7Bi2RHhx4LbUekcf4Fyby4m0y3klZxHbRAzDnBIVUFbOe4Poo8mdZCBozFX4qd9obVvHzILyeKpycjke1Pf9sVS_TYwpTnSEHt7NgwzR71yTB67BVd94f2SbJBSQAN07qVcO3JwRoKFvEqPlE_wvgrav1XXAjqoLP-pZe8lr03PzWACHvEDmLVcnQ2KEcrBaFGho2ku4zhdLwTa1gUUpdBbP9-wnPqgNi2FPhTHSeqYsGjHNHRnOO1FDCac5-JI_SDa9qT0g5u0OeSbb_OKj58emyn1kDzgGsqGxCzq_sSLv6XwKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXLsFA0RZGt9PWdj5DmvVMw-8tZ2nRofxejMiyt273S4ChohX0t2ugsvhBHifwRurBkgA7OColWcxmCMyIUkwdZkvHUWYQ0U57RFE_vynVBTJHTWeCvpx5HTnrrT6X2H5hmKGSxjpckdU5SvKPWSzJtOqOxVG1w9IXV7m4PQG9qiF7AcDFTo2m5U22bGuwZB-9x2VagWKTN_oEkfTc9wUFnMK6OtIpcb1eLd_Y6npSscB1v9W98NJFXLZhEVm1kVRZdBCHipwdIxCVclcMuGkryjF67g3RUxLL5swIZ2lAachyAweJY6dqlM9Vbq6YOXpuu55cqGxvIaI3TitA2wFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5EP2OnyGlMij2rSYBkxRh08_WtJyA1bxfO72yfiEhVzWxDhyIvaXMCspIhd-Oae8OGmNDA1_vfRXvJElw3xpUhJ7BrGT161qgwByUl73c6nN_T9a_23XZMAz7-fdCzzp26fQurqE4hjqHEXJhNtkarX0aE9aPcIFLGO7C_GyeCVrUN1A5Aemx1Rz03dF4lCLyTgHGNW8dw-MRvciL15jfALavIR42O9q6ARy7EXD_lRX4MAi9XJ1LETCFBhk_xhkNecClQbmoSOCicKaEI08X_mwiNoDlAoESgTe6z7vfwZNz4bB_cVm8yfyI80Q94MTtvazHgtWYp0wWMg3PJnUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFpdXBRt1CSn6QUNwzz29hQPSXDZCxjS-8u8hPh-oU7il4qWleb8FfHBqZLpAKRP62ceb9aQMDYYo34vb7Syzj5Ue1cXUj3xEf95Pyn0l1ym4-3pUkEDY6AfJI3DLkKLfjKplbn_lQd3nwlwsIbxgYTJBCoJCh1V6bvSFcjaXerraRoXN699XK6YOqsJNBUHJCmLtvs4VOJb50F5_KMdVl18lFc9L_88dtYVE2tOYwyaj6tBDNrkqSt0B4ClpxmmAM_jb6JHKINt9pKJsMXRnv8-8r2QAxJVbeezzTxB9pUN-y-jqsfInXqb5dcBBCJfOr_c7XaajHfehGf-PQCWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsXETY9c2Os5uLbaTEYUMmg3VBs1qfWDuKWlQ4GzgqstuWHMGxTOGdOxzN8GN8hmmKCAVn_9NQ3PkSytg19P7l0A1A8zi5aao6mehRqPz7GzMfvaGwNhAA9L7Y_d2efvCQ1H5bZ6CYkvS5OsqiNOLJ7alq-2x95CG1jpiaIhJ1w4DH0BK4S1CclLtXJ-7uXf5OaocbybQhLigH9s_ICshRfUilNOPpWByxFCAcocyBLOmeKPBu2n5UDr-USnA_ABy3FT0XGD8dhJXycInTKJmL8meUXsA30ZYXSJx5f96AKA9AYeeg6fUvgVa91euHacDi6AJ3-YCd8mCKKKf6y7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FET_pPQe-gWQJ2qtcQPTnatZu6KA3FrrD7rc_y1QFMn-kk08pjegTUxBDQz39yy0xCXtEsg4nUE_bv6twrJzHbyqvRlh9E7MZ7ybXi0igoO5BRspVmiM-X1g-f81n71Nj85T93dCVTvWqSRotDFQiCkkd-7gtqpcZfIoNYlSpt7V5s1TcQDenNrRuoi9pWOAOVnzLMfMNZyrvTH0hS3f73uLDfCizXcmvmXHh6D_w_FrCODdwIX3kGQajqWn4_z_GXautOkn7mVhow5ZpGV-1OYdHHetDmC2nM9XrM-aBZrTvTHplpUoxYgFC_28yGNQRK3Llm5KHIQVZu14bqejGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfRfi3FOZ1GcyzYya9K5NgKAw65OXgnebnFsJ5cxk25ZSAwLIMw2WzAF7V2hole-QSrSMbHKWMMJX-4rP5I4aYDYEQ3btSskTZzHzXcwG8fbqyXSw5fTyF0WUc8HJKgsIAbxxhEUSgfAdJoQOkXD1G__XAdcYO2OHcYk6a1P3OAMEKhR5XhtwEutWgtJOfh9LuofCvo1XWSm9xgbDYB3_MmUQiLolsTxN3J1SSHFrs1J51fc2VsAmPFMDLlkeYzxZFUIpX-63fJllht3G2oEWzpFcZSLc0H6etDh3bLc3ZLSxJtcvHwtTfj9aZUxvk_1Ok_R0knT0vUsg2PgUAMBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMlRHsS1HBgRd_I3QocV5-QzFzZQhIDEtz1KEv5jkN0W0mz7rywAb8HzGVETcBv8pvnUC9w690Dw7wajcIkMn1CpqT7W6p3goSzb6j_y1F86wMbpy1VU98ZwDRnYVTxj2cB5uQaYoTCsOLk6Hd5-x9gQX2_sswz-DIe7WnfzRK9AzmXXQdTdQMIh_aI_fgshJMrUVDpPt-p8PkmURswkrhA8XX5PNa912uxVw2zAupGhPMbiil5F8VRxk3HnkU9bgbcS8M7HcCGElFr8xShkWVNrimVcp6TBuyJ_H3WOCzd2_uuQodp6Jc0JazQw56cEAcN4OF8_pfnaU8H7JkWJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UpG2BhioQqsKL6P2o8CTwHnuqeYgjsWt4TCMP0DF7mmSGkJBp61mh9bcKoehbb8zpbPjf0HKymrJZd8IknKN7-5kRYqO99T6WxFdh2ZzAy9KABZSi-EZlcTtSR0ge-o5UhQiUH4vTFpWyENHkpS-7EeMq2zwYsfY-qo9kWJC4qCw0umRrn3_vXUJpf0-497XZOCUM8Z2np9kbli9XSDO05nLMJYSA_pXbRUTUdEZcluP0oUJz428oJkRzS6I-UjJh22SmQmxCDDIyhbv9ZRvL4YkUx2kKqoJ1u_JMLIo62TX19T2TNPvEAmvhgi3DJc2UjCBRerbKI8lUmXrkJFH-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt9tw03ObZGd9moy8wBMvBI_9heHMNfqVlYj2I00UVHeTcMP2DjOktj8F7y7q4Up2B9NK80n9Wdzw1NkYlxrVIbZTJMC5F3DOjHLI4YR2LABqRX6v3kZVG6QY7lFKdgFSVQKSZGtXeMHz_SkFCtsrt9or5Kp4DdSudp8sgqqFE73CDNuFLtGw-4VaH0k8Dhk2F44AsPd69WeCRgZfGgLdJ11k7_SD7pclikhjwReWK7sWve7GC0N2aekBlL6ORusknu4AEddMak_PYoCOkROQPfJ_Zt3pIA4lzKmS3xDSp9BpJ7wivuZpdFrieq6oXP9AGPglq0JNrMzp3bbNgmawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=mDndXFZlArAxJeGO4cv5aHB73hneN5KOgtRj2bcCFHfFArceUxTTOVdRlc_uTlx3eoL63K8Svtqed7lwSqi9JKOb_A1NaBY1U7Epy_LLFhJf7Ci3abHxOofd6DgzaZjqZhK6nBl2Ss8z9xcZx4PxUoSvzn4Vyial995UMcYDnr39bb1y2xwPXxeAtfKwROdGccKbIPq7SJQzWv2UXCGp98l8qohgeKf9ZxIKySYVmv2WR1kJcijLzBQbSS2MQdzMOwo5_nD9pDs5F2mruouTYzwmVc6z7MSu_MhxItKapEIN_azoIxdmdgHkR4xa3IaLD9bUeOfR1bVCg11kowqGY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=mDndXFZlArAxJeGO4cv5aHB73hneN5KOgtRj2bcCFHfFArceUxTTOVdRlc_uTlx3eoL63K8Svtqed7lwSqi9JKOb_A1NaBY1U7Epy_LLFhJf7Ci3abHxOofd6DgzaZjqZhK6nBl2Ss8z9xcZx4PxUoSvzn4Vyial995UMcYDnr39bb1y2xwPXxeAtfKwROdGccKbIPq7SJQzWv2UXCGp98l8qohgeKf9ZxIKySYVmv2WR1kJcijLzBQbSS2MQdzMOwo5_nD9pDs5F2mruouTYzwmVc6z7MSu_MhxItKapEIN_azoIxdmdgHkR4xa3IaLD9bUeOfR1bVCg11kowqGY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftZ-UDIoLE-2kJ0mY5e-guYAFgEpdrwJJT5aw6tdHND722BH-L4_eIqvLOzjnswBrW3nPbcgruZ0UMHzr8fR__s8yraFOpLB46EMlP4wlFoF9znOvQN6BLoJsrRwKYL0qTtSom9dGTQOm9_SfyDxqtWOsFEkfo_KqTU7LciMtTtxMbBrDFFwdj6_GhuJfCzFJJkVibOIHeXnqcBSd1_lLteHhrYMYvz2T7MSzzBl6masulFHtQEEicZOOYEp7ggWj9GtC7DFNxCVkw_EIAYuQRMGzo35GsQCRRDSQJr6t6LoHwQ2Rg0FSQmNzq8t9Nd36ZK63rqZ33HDbYeLxpeEgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz7a1gcS3Myaw7221lu_9q0N75Ew304mGewobtghzM3-hYvfmaogY5XW8zaJpeqzMFhfUGiJDrwBd1T4D78iYbPibhaBSVHrPnjH0KVugfjXMB6zMqdM9hU0wyKG4O_KMgnNbu2D3ycMlA_v4qifXMiulID3ygbyyqRqIJYGfQDzq3T8bEhGx2HYF3LvIEEutaAbqGVGjIex134lVrliQsDKCkzEdWahLYZT5RC-evU1ltU2IqeptxchEN4EEj99V4hPz-LWY-AR_4A5scw3duz5-Du5MQzixDmicsa1jGOdrod378j2LjOCBBJSQYb74tF491lZUaLOvmhTbEUNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7WZmXsoxJzNNd0Ml4nVO7I16gSZgwNM_NZwTiucry421XTTsy2Bt2id5AAn9jox1rwzGuR2PG47KNVUdjluZgQKTDHYVtcqzTY6ZZZcnDvxk0QeMzyj7RMZdy4CzA3iqWiSTKwiNxjYp7ObsWR6Ti0KZPgfEFxRAfwJCrWLowBP6FzlXWcljMGG5YLvxOC0d15PigMeeAXKVHt-6sdVye3wj7fEusuZ27DVQK4pfmCDrgs0omaNEwJH3SahoOc9uZ62SdcIxLcJ_IUhvZ1ktv_C9HZQUjd_xusxnsltGHpQ_2Cml8tn36NCxLejcRZszXBkqhXJaO9paYFu8zgk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFLkK_lxeMtMPkFGmd5oPN-2kRf00GihfLIFJB1byEhnkmYoI1u75FzKjDgMF-SleEsCA7SDE36R9-exKBwCpeLhWY7AXyt-ayRw1zNHVAaZ2w5Vnb6zvViWS4BkFPH9jxqt5Glz79zgOK87LBNK6AO3FRApW29pMTxQemuQZxq6vN-_TtCUvkRszpPIDLaqCOqvrKXUcvlvhxH_L0IfqfrL-O7XZd9f38POHk6gQRJ8SEgHivH_Mujv4dlzOHmqv338ch-CINzNgejIfYwCUx1DP-iGnflitK8U1MEDskUMuXpPvIqNjuZQMXFJUdXTrQfUU61jKJhlvAR0i7uXCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plCTSMzAmP85eJYuNN-NCx4bJtwcKOmnV2fqraOgj3ED8LnfFxLjWlsyS4QauHd2ojR1e3miFXxoRdxf2VSrnTqM4seYp6kYMlmkgL3OwADADYhHxPc2Gi8VQ2P9VHNeLKXs1XOXficBm69DWD4bH6kwWtM-e9aK8bpV2oDAZ7sGuu7m15tNt4_7_wVt2jxMV9LrAIV-bNpGCCssH0dQey9h8Y-45jsI8OxIwIZs1uslkE1_1EJhN3EBzb4-4ENaNFTJAYDwrmtQSIFEpcGP1zH2BCNpoDNsSSWM6RAZXzckzhZNrdUvPKl4VJkos-RJEiXNbAT_DWixmGT8zsQIew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJArvSU3W6GlO6HCumXRaY_R77W3-p0viHx2FeSnPzDnTVrhuRBRCr8nryR6KmEX1O8jA6Z8-t457t8VcKWNj9aOEfvIp8HJDn5xGfjE-2_9WRniLXXdh1BuJsiGTm_9aH6lmqv50U4mXRE7BP8g9aeg1W4VDU_0t3xnlrwPKoTwK1ZeFQ356_53C92qSKyBRzlHrqFmECp5DCZ_mtt-4yMtcDvv9WgQFa7n3svRxMUWqlN8YGiYhO-S5YAtCIo7KN7d6lL949bAwYDY2-LEanu493hvFW7V38Rw7V6ELDAa2eHoMPqK4So4W4iQxfFSeqWa-GneguEuQGo9slFHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ljxzqUQICct2r7B3Q4qcASu__DeLVteHNaKEQjWYMowGaYbhWJGLBkUA5gWxYojIke2x21fzYwtCIuWoGxEdRvvcb8Ftt3Se9FyLNRxPV8yKQX2uXfAaXN9oIycdcJR195MjsQxrPooRCsFGLXw1GUrcoT4mvfivNeolgvXCc4p9lYhK4Mkd9YhaLURx8heBDf1CVv3_lswY04CcTZRrI04rcPqIJiIZ0lAQFC2cys0fA_hscoosgQbvasynDDoAbY-2iXskoSAIo1L68U2sEZIXAvQId8lT9wD4uEKyKlQM0qcljK8h35TS3jGCLBFf9u5J3vwEnWP15ncP5yT72w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=VScgMcWHFvyMnduBxeUH53pgz6qrDuV2ZqaIfPHWP25OT-6hiwxZZ5rrh2UysrUcS7ruUDX0O2j1iKGFQKRPqGY_83LkS73XH_CO96-qgTk1BVJkcwN1bRVWayyl23qqdUxliOnpv_R6ronZ-tR4jWQ027F7XMPBkkVDmi-tgyFAg5K_e1XcXK5X-uI34NJ8iUq2NoDqW9B8pQO36YS20ddGuKJuXp4Oo0SJTtZNjsIDIqJuKSDpL6g1mu9HmB-jVGWZtbUJOzIlZ9IYiCVEKOoMLcus-mBsL1qZz9ZIjlrltI3ZAkS0wbms9xzf0QoNdM9AuW4RbzTmZVxL-kEqJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=VScgMcWHFvyMnduBxeUH53pgz6qrDuV2ZqaIfPHWP25OT-6hiwxZZ5rrh2UysrUcS7ruUDX0O2j1iKGFQKRPqGY_83LkS73XH_CO96-qgTk1BVJkcwN1bRVWayyl23qqdUxliOnpv_R6ronZ-tR4jWQ027F7XMPBkkVDmi-tgyFAg5K_e1XcXK5X-uI34NJ8iUq2NoDqW9B8pQO36YS20ddGuKJuXp4Oo0SJTtZNjsIDIqJuKSDpL6g1mu9HmB-jVGWZtbUJOzIlZ9IYiCVEKOoMLcus-mBsL1qZz9ZIjlrltI3ZAkS0wbms9xzf0QoNdM9AuW4RbzTmZVxL-kEqJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=rRSNWBE1n_J-yTWU4il6Ry0izEhcJ7PbbFhM05o343Es5BU2qPOqUPySWDSgjmkpJ5zLQIEx1xhTAvl0Os-_vmZz0ttpht5L9O9udgwOgmV7PQDy87cC0_a58elWWtOLJuiY-BoZoygVgF-6KH96NMfdDgkd4Fi5TdnE5ZLL6HRRcxAcUW7Exibl6uu7oh2K6qFiW2l-aBvNBdWjB89q5Su0HeOrw7DYdqVOvxcxWaxRPVlSbbsLu2z28ElQlOavL9pElEOEcIweO4lRV4rbCpmsXal0pTo6nAAaTlu_Fn9yucXjo17gNz4MdP1KtnUC2slenfMoAgWj49LyzQ62Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=rRSNWBE1n_J-yTWU4il6Ry0izEhcJ7PbbFhM05o343Es5BU2qPOqUPySWDSgjmkpJ5zLQIEx1xhTAvl0Os-_vmZz0ttpht5L9O9udgwOgmV7PQDy87cC0_a58elWWtOLJuiY-BoZoygVgF-6KH96NMfdDgkd4Fi5TdnE5ZLL6HRRcxAcUW7Exibl6uu7oh2K6qFiW2l-aBvNBdWjB89q5Su0HeOrw7DYdqVOvxcxWaxRPVlSbbsLu2z28ElQlOavL9pElEOEcIweO4lRV4rbCpmsXal0pTo6nAAaTlu_Fn9yucXjo17gNz4MdP1KtnUC2slenfMoAgWj49LyzQ62Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP3GqzwUscMlL68Yg0rQA4kP-Leaa2lgytaQnx0tKtEhhLBfDlM88KYllXEX5H8Uf92POPjgoR0NfjGWUobYZcr_k31mclL0hMCJqdfxduZarhUQrQIH2-_AyR-ruO-r5K4BOTBgxJE-wf6FbhfxgXGXfZQ3t1dXGcCaiyRKKenslcQeF7wPlFi_LcWpuz69w2kWk-h3cNcJxHVtvr_XaWX02x2OJXD9BAcbHADx-213hIs7MeFRFxyHUPvyK3-S28qsXWHsowopblUVGZQA5vfesWrphWZ1VbP_jMBbn3vacaIM-8QLpqBu43P3AHH9FRAvsU8h6U4-yhVpdp1BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHTHxwoeBSyUl1eqHQ6RRjjtmBwLCuf5YKMo_SDnVVv0b-BmQzK5koSE6Ts0KqA6trz7E9pVUZ6eh9tS_eyKYU7zkrWHpnKjdr-lMiTC5Kd3nrql2GDqj5vTGMUB0hxNYJ9mOO24r5a30qBrCEognTMD4M8C0sd58S6GMHNJru8CKBXiE-hzr80tsffGFf7opMW-t2Wtm0IEWxmEfbp2CefdyhrF3wtMrVTy-gS0Qam-kRWl3uSMByrouB5ubETKoL5xfGVikiVlgU1NPhYURj7bL2_orvV4LbmXlOZnY8hMnjcPCLFlSmfUKbC0bP6hixBYNk86Nd5Dv1o4oT0HvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=bRngbvLXr8e7flLi64j8fO4iLCrYSHnuA4yJXLKNakGAv06T4-VKWOfJZvshn01I5UjU0MqDbfdUM9qvUy4hEbGrXGRisxYeCSm-x5X0HdtUzgAz_UUDjpXenUwcU16TXceWG32RzaF66eoPQHJec383-4fBy2O9cx8Ki9LPmGgR9jNyxNrt5xGG6d7RHVwAf_lAnLM4e7_OqRHvFqIemk17m4h6hsf3EBh7S-TnS5cmS7c0DzaPx5Xs6eOyhe9xLIQ9MP4lD49Ff7RcS1aTZCH8j4YzHLuMTLSc2NvEd886fwBFeRWG7Mtmx7CF3cKg1kWi16QOx6JLJHFN21sO0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=bRngbvLXr8e7flLi64j8fO4iLCrYSHnuA4yJXLKNakGAv06T4-VKWOfJZvshn01I5UjU0MqDbfdUM9qvUy4hEbGrXGRisxYeCSm-x5X0HdtUzgAz_UUDjpXenUwcU16TXceWG32RzaF66eoPQHJec383-4fBy2O9cx8Ki9LPmGgR9jNyxNrt5xGG6d7RHVwAf_lAnLM4e7_OqRHvFqIemk17m4h6hsf3EBh7S-TnS5cmS7c0DzaPx5Xs6eOyhe9xLIQ9MP4lD49Ff7RcS1aTZCH8j4YzHLuMTLSc2NvEd886fwBFeRWG7Mtmx7CF3cKg1kWi16QOx6JLJHFN21sO0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ_dr2fDqpEMgDs8V1I41on3wtARTM-iZArhT611eHnf8l0mcJyGdNnFYUlgXrB8CYySeooOHAP5xV4SNgTjW5OM4dg6rBGgLyozD4ayaS3quye4YFlSvM9FN5pxUH910NQ2hjsRWhsHaCIr6BLk-RFePIOYjAbMkudaMcbd4n0mYcaYjEVTKW5Mqb_75A6jfrtwQGs4aSBJLz5QsXMg9F7ZV5wvPZP5N93vMwUMAUv6vkFgTyo8EZO5Cu3c-Uz_Au5R84hy0rJdqfuTXBeuLXOQBu4gLzAgt_BhODDnJUZPdqswPgQ-eCqICt8OCnuf0tGauLbwfS2MK0xl8OtXhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCb_1vqru0DJ8HwT7coUyS1NQccLeksxQyGxY0tHDDnhP62BX8TxoVq-wpEZTh3DgzmNKlQUJA-GBoArV7cMjp2rQxtQxOXqXJ1ItqyLe8FfesczjygquO-qwe_gm8b-IYmluwaVdLLUSCKWG2nmlfP7MJHlcWRkln-BHAyVYtcDFQEo-ZCl7VuG2NNGsu3avBE9ify7-zlaeo43FVyL_Ajrkz5Yk_2lVvzrSEfsfTlFaw7fnLqrt28I3htkQSyc7mhGwJnY8qJytMGsJAPl_iMie47i4SJTMz9uaDNs4SynnDdO-I1qIVNz2uYIGlNCxWdnUURvv06EbbjURp3YNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=UfTf5OJH-xAhEau_vkU1KHV6vNwjRYwc58I5XA_QO-icTdHz-ysoOuWp6iyppL88mfH46F-htchvrMSGMm81krxstw8wnFImSK8XBAyD41hyCwhzzOHGIzuIH2B05czQcO4kK1u6bR29cWetGVY1lGZtac6cdjUSay_Irl6QxL7ujDVqlDAN0WG02-r1mQWe6_BEvMZcODyweqn_3TrkU-GFR2mFyhj2oS-ZG_9Uf1dwz-smIsgghS6HE2fxyo_dfhDuFtIfB0AfW9kV1XzG011n5Fl-dFiE-uU6rHvhQmyjuvsH0eeWlpdjm5wTy5gXG7LZQKEgAlwZLKnRBMvN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=UfTf5OJH-xAhEau_vkU1KHV6vNwjRYwc58I5XA_QO-icTdHz-ysoOuWp6iyppL88mfH46F-htchvrMSGMm81krxstw8wnFImSK8XBAyD41hyCwhzzOHGIzuIH2B05czQcO4kK1u6bR29cWetGVY1lGZtac6cdjUSay_Irl6QxL7ujDVqlDAN0WG02-r1mQWe6_BEvMZcODyweqn_3TrkU-GFR2mFyhj2oS-ZG_9Uf1dwz-smIsgghS6HE2fxyo_dfhDuFtIfB0AfW9kV1XzG011n5Fl-dFiE-uU6rHvhQmyjuvsH0eeWlpdjm5wTy5gXG7LZQKEgAlwZLKnRBMvN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=AxEuEmOSlH3xQyjeTeR0p5etFSwGuCNV8biRxRwtpAfRsskx6luysBWPbgP9pMPhBjNu-2ZQ33r-vnuNq75VKorsny-qnrVxQTwFRYcPMLrkiN4gUXehX6mVygAUBlxsOrwEzZYGGGEth4cvMKs8BlyM4t7Dwd0s7LONSG413_44L_bLo11izroJvL1d-U99kPmWFMVnyoNbVqAA_DD__C9PNGw49M_O09AzHb53ReXQ-LvCdOxhbumXHLElGSn-0XFI4OxexUHMzV82u030BJLd5djDNqFcvWeSVIRThUsIGCBzxzwIhWzuyyTyTk4y2nlJ8On3Sc-xOHILG1pxTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=AxEuEmOSlH3xQyjeTeR0p5etFSwGuCNV8biRxRwtpAfRsskx6luysBWPbgP9pMPhBjNu-2ZQ33r-vnuNq75VKorsny-qnrVxQTwFRYcPMLrkiN4gUXehX6mVygAUBlxsOrwEzZYGGGEth4cvMKs8BlyM4t7Dwd0s7LONSG413_44L_bLo11izroJvL1d-U99kPmWFMVnyoNbVqAA_DD__C9PNGw49M_O09AzHb53ReXQ-LvCdOxhbumXHLElGSn-0XFI4OxexUHMzV82u030BJLd5djDNqFcvWeSVIRThUsIGCBzxzwIhWzuyyTyTk4y2nlJ8On3Sc-xOHILG1pxTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=jv2XSf4FOSR7PL_ANjSxTXG-cGeJbK_VqQfIZZuDS2MJbjbVp1i2Ui2ysWZT2xOYRSDg6YNHiUP7olN4jJyQrmryjF3-9G7kNzwW6UXkiEWw34-T7ci3acyAlJhnHIXoxT0naAmDaEN12-Rd9NCR_nO6YYQ01wImZV2eHMRmvk3h_kpHcqCeCF9XGhdMdWyti1ZUa7QJQkvbaheTg3kjMkZ46fVFPdlzFc71vri4lg6DklbMNO3k5lKddY6qfZ7_awygaGeTP-vRnY_cx34SOiK1VoMYm4i75mor6yl8u2zs8tuIcxcjd6xQdlbZVjonQQCtoBLIARZSEYR0u9vXNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=jv2XSf4FOSR7PL_ANjSxTXG-cGeJbK_VqQfIZZuDS2MJbjbVp1i2Ui2ysWZT2xOYRSDg6YNHiUP7olN4jJyQrmryjF3-9G7kNzwW6UXkiEWw34-T7ci3acyAlJhnHIXoxT0naAmDaEN12-Rd9NCR_nO6YYQ01wImZV2eHMRmvk3h_kpHcqCeCF9XGhdMdWyti1ZUa7QJQkvbaheTg3kjMkZ46fVFPdlzFc71vri4lg6DklbMNO3k5lKddY6qfZ7_awygaGeTP-vRnY_cx34SOiK1VoMYm4i75mor6yl8u2zs8tuIcxcjd6xQdlbZVjonQQCtoBLIARZSEYR0u9vXNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWBjar101OWMEseRMuSUCMQ9bhMhPZ1Y69G0uHjW0o2BlIT_lJdQNw4jbseQRzKq1U8MQ_khH77ACoQXDJa8a183A0kxdhTZm2xF0PUTBz2sn8LVc1r8lKzRNCroFvyM8S-4rP_KkbHu2WU3fthxrIu8xhQJaJ0n55KRctf8_IbQwnh0lkkxW2VvEOAlN2SEMAnIPBrNDK2NJsBFHLeOFcs0zwJ20KMNLKxfQAXK7EdRi9QAymZOonKs0qfq3yV88BSjIccNu7zwVaYmT8OFf7d7MKRZTDorf2ofREouWZilXx-mgxN9r9VNu_8RqOE7hGQJAYxd3SykkreULyiTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucVDXWr0DgwfMeBBiv8z3kFlfbIrbTTFEc6BJRQLPq7S0QbXAsDONVLj8dhBHJd88yg2VSJcVoklUHSJYA5PlwHeyzw88eVXELu-qyZa9TE8By7I55LajWyfLTvgGM5dFzVN8cgKy7O49KP1BTna1eNp7cvoKwEXtdd4YGnAzpAk9sIglRABhkVI55JB7RZV0RUUQZ3SiKT79gtMf3wN8t6l69BKgcFLRLkyhs7xuWQkLsnQaT3SGKMrL7a7VTeurDEzEVr1hmyXpC5wmori7N5fBo6cwro7q53is4Euf-OxTfFZ120aOZKt4lEFlY5xf_LjplLyjEpnTNFJ907gQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXszWCze9CPkLRqKZ52p2cqzCP6BO2DlIWtoWiYzJy_nWpZOnk9g-SMJgs-MEnGSXddkaHFIft6jOH9vBraY7XZNUAEy1La7AKnYEsu9RVQx0OzH-tCTgSNkud2vAT4guUxVg3o8YiwlY8jYh-Mhm9tYVCC_q-tTMan7eYPe9I5Oturq-kvP3O1Kju9713O7B6yyH6IjU0N6DcTF-X4R-gJL5fN1oZgphDw2lmUtUhNc3Y8GlHCJTmFWyOASLlACJ7LbBSM-V7KYvWHSKDTSCVURLgZYxVr8k_jeIDvTtb3EPEP9WN9UvtXsdv4ZxDM3tQyFes4ewjnPszgQRlWeaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=t_f_FuQbQIXqUAboO-1_2D490zoy8Ljvg4spygqZHy5zyIX5tFDVGGRGYTnrJ0SMFvKrso19rBFft4yq53cvjsv2uwVM02PtCjvNLqShCaWlBXfEyM3uYCu3nddDJ41lAMcQhX1fX5DPiTXrvloZDRzLGe6VsInOiRzJnBToimHa1wN8pLIDfRoEe5q19S7l4wev_qqAP6lZbmJpz-B-0QZGMeFN-bwGoFG6tCcNUkw11oU-XPf-b5T6M6OAHKRvPaEmukPIhQpki1g2hK4wymPQT36eM-xCn6nZpX1N1WYXDU0fEaR0iZtZtCCbdhICwXNpIx2SlKGlbd5RDkH_fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=t_f_FuQbQIXqUAboO-1_2D490zoy8Ljvg4spygqZHy5zyIX5tFDVGGRGYTnrJ0SMFvKrso19rBFft4yq53cvjsv2uwVM02PtCjvNLqShCaWlBXfEyM3uYCu3nddDJ41lAMcQhX1fX5DPiTXrvloZDRzLGe6VsInOiRzJnBToimHa1wN8pLIDfRoEe5q19S7l4wev_qqAP6lZbmJpz-B-0QZGMeFN-bwGoFG6tCcNUkw11oU-XPf-b5T6M6OAHKRvPaEmukPIhQpki1g2hK4wymPQT36eM-xCn6nZpX1N1WYXDU0fEaR0iZtZtCCbdhICwXNpIx2SlKGlbd5RDkH_fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=AcdE2vJzOrqf2KjTALClf3I02oMziOyYmpOeS8G6k1CQJnrEseh48l4X97rN9e-huUKNod4lc9bgyB_zXi3nMmCPGhuCOL8vrqOWabfq8BAnV25cPYjN9xIF8lKbNHTf9C9m2kBBu_d-nsurnu5g__4aQqf1-s0WUpaYsgSNGAivWFgV_7JDwBLbIBUyio9R2Hj1J38TumCETlBZ1RW3324znNWy_UlY0j95fRCGH9JBIoWg26J4CvX9bnJyJE46g263-3VTxam5Bpmqk1q5SKJLyc-TpDguWCrNfh5bP_oXBowmvyKARmCFRIMKN7zYhzR1kt8_bf4Yw23Yb25s5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=AcdE2vJzOrqf2KjTALClf3I02oMziOyYmpOeS8G6k1CQJnrEseh48l4X97rN9e-huUKNod4lc9bgyB_zXi3nMmCPGhuCOL8vrqOWabfq8BAnV25cPYjN9xIF8lKbNHTf9C9m2kBBu_d-nsurnu5g__4aQqf1-s0WUpaYsgSNGAivWFgV_7JDwBLbIBUyio9R2Hj1J38TumCETlBZ1RW3324znNWy_UlY0j95fRCGH9JBIoWg26J4CvX9bnJyJE46g263-3VTxam5Bpmqk1q5SKJLyc-TpDguWCrNfh5bP_oXBowmvyKARmCFRIMKN7zYhzR1kt8_bf4Yw23Yb25s5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=d7dyZLQqVyp43WGiJv-rMJsztD3qaz-Wk_kAV9ssLldq2ieM2E89oaemB6r-iaP3VF2aDhvTHyqnryJ6BCFRe_0yiUu9eLoewLkhTqflckqTAKadOIsdbfau4E1IhFZd-SB70y9umWqUSt6ZKO2aRoOuUTkoUxbsi17m1L2e67wdd5Wwm1c6nrI6mFqFrhu1YpIKc7spt4-cFzAZO1p-krabQ1uwDmK4d5U9TAchaLn16Gn0GBWGlv_jE6RbLESlBnMi8mQvnJdZm6k5hbtPzWKhIT5s57Mx8NMPiQzFsNn9BBT8EShRL-nXyQ_bcy9ZnCIYDZlXs9L08B_pYaWsHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=d7dyZLQqVyp43WGiJv-rMJsztD3qaz-Wk_kAV9ssLldq2ieM2E89oaemB6r-iaP3VF2aDhvTHyqnryJ6BCFRe_0yiUu9eLoewLkhTqflckqTAKadOIsdbfau4E1IhFZd-SB70y9umWqUSt6ZKO2aRoOuUTkoUxbsi17m1L2e67wdd5Wwm1c6nrI6mFqFrhu1YpIKc7spt4-cFzAZO1p-krabQ1uwDmK4d5U9TAchaLn16Gn0GBWGlv_jE6RbLESlBnMi8mQvnJdZm6k5hbtPzWKhIT5s57Mx8NMPiQzFsNn9BBT8EShRL-nXyQ_bcy9ZnCIYDZlXs9L08B_pYaWsHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=qtWMmVR3jeOj26duWUWsC8R8kfCO6xLWQweI5e8OhPZJkHGvpgPRNOeqk8gksvaxuKdUd2_El6STGFl1Y_u1sgZOQURmbJlSZu7Z5AqYDEzcvmG9XRh2FmY4JlopNcDPjG5p_e7Yfmpvtg-KZCYo1irelmdVkA3lwRzByWxFemNqz9bsnEZlpWav7jo15gOYnHsFkIS_K_nezwfcH4SdbzO37QoYVLaQX6KPweknQWIE9LUGaD5BNoOziAK8Vf2wS7NcvVHzC-6L3gGzbu5B4UmqZAmAf9dWZdjOGBBVhXMRRwGzm5W7d9rA7pCOGSN5QpkHhnSyXG0cOgGZA08r0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=qtWMmVR3jeOj26duWUWsC8R8kfCO6xLWQweI5e8OhPZJkHGvpgPRNOeqk8gksvaxuKdUd2_El6STGFl1Y_u1sgZOQURmbJlSZu7Z5AqYDEzcvmG9XRh2FmY4JlopNcDPjG5p_e7Yfmpvtg-KZCYo1irelmdVkA3lwRzByWxFemNqz9bsnEZlpWav7jo15gOYnHsFkIS_K_nezwfcH4SdbzO37QoYVLaQX6KPweknQWIE9LUGaD5BNoOziAK8Vf2wS7NcvVHzC-6L3gGzbu5B4UmqZAmAf9dWZdjOGBBVhXMRRwGzm5W7d9rA7pCOGSN5QpkHhnSyXG0cOgGZA08r0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uks4fhYQZkeNW_gll_4NbdGLfwzDr6mvW9n0TjWxjcqWv2I7WGswuM0ELuIGXqzxFZBnbhdiG9YVEasAN5_rcB0vaJ0p8xs6pzT-rAdZhG1Ka1SW-ADAke79u8_tUI4luqSxL82KANocmZki-lNcKMVJqAJnGEEuJfuwzXTIKav9ZZIE_OApRP-mE_6XH8wBunjdNB24u61X-RwXkWvf-V19e1R1YT_f9dmAB2HJOz1ks9xk32EN3RXwb5t8emNkmpO_-1YZWyW7rL41f7_bdNs_z__WUkQdCKlLEYjy7H1TFxtJtPTBd0j_kL8UieNcJgB9TNfOjuALb40I01qz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5grHqwxh_ELNRgJ4F2zQNgmT9XVV8wgZQ-_yKE3Aq3b5Bl1um41lPhFpIwNHkajuvNi5WoDuMuPOgen0tqMzjXtwUuxSCr1d5yH90AUkF7nEqEKAT_t0QHPxBPCvHdGamqBjAcoZqOv2qUpkKjdx5qbjN5sDsUaZm6pENrXPuHqpeQOVDgRg7WluORVhZQ2tbmTp6zmGq-GCMjiU1iDRmiHs5izn-XK9FGUTGUvc2IOkV2gQQEBdr4y80YjO7mcbDV8AD76-DdTJqMeyJ7SIiUMBvy6Z8VUxg_zPrwc0B-hYnhkGA_ZjoUBAfzomAfxRZPnaSwuNJNPtG5U4yHPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnRfJl--cEoH9oDJv4iY6C7emCvB3aCXjoZtkwww3A-Hm-1Zzki9qFPA2oNz6OfFvzpSKPoN899STK_hqPb55O3fKt_BRxXBV0bragPnYrS3CkdvqAEbr7ZXo1-0nZGgCRuYC0_-XL8xM4ER58qJymA8IE7W7TfBlasuVPm583GnJD2RD9yPwOIlYSGbXKSxz4DNz99n_KteYl1KfyoVZmL8if9OlarnE3OQuchaFEKkkNRHzp84_oF6tLl6XZs926BS2ywBNuF2VWqsY7LPuk1TMvQK-iY0-qPgowq7sOWXpBww6Liu7fEQQOk9rimLOdBZAoGfcS2d-L6zYrLTZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKa8A8c-n4hvA-CsefM6WyxG0_eAaoMWcKpwpSg0iXFLGUnTnqO1QMB0fn8cMn7zHkg5Y9YZoETQxv-nmKVQp1eiNh76-PPwnO7hSIhxOLqErOo77k7bKM2G8R1MmyoOBvpvPNwMXnQN-vOJ0TcvmNOXz-dX3S6NrJZxPQCv5IRDMCrvewh_rTlepayCCX8Bistkp2HTTLDq1RT78Ot53TFSmjfLw50h0GKT8EWc77pWn3L1AoTHJslnLsEqnF-FNg1R553pnHv8uX4lNdlgVVmKpxIur4XzTlqMdByC0ZDVFzGCrrhI5om_RQO_uYGfunoTLrohkxIBNmhX_uI4Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9umKXrLG3f1dsaiI5aWBekVPsVH10sYPsjHw5nzOjGJ63-SWLg7WcnXbT--ExNLjSTx_GrAMf_1TpS1nuZPfcFobPY-3VQkbe3Y5N3QsY5AnbxHmLaNl9m--Uaz-ntYyLIA8mVA0yu3b_Qhh0UVcp9aSS2mWmbHseT2aFpe0A9jGqqo4_Ro8VWwT9aJux4gCk_2QDqx0G-qgwYo6uX0TKAAHjiExJ3GZdGwNFNJD2rnApROsGOdqimfkqncjMRRZYJyC6o8xVYNJXKwav853qUQMelwDO0zKd4BxTdg7ySC4CcJ9dHHuklSod_skyfjiwKeP5JgaZ0O8kgflcEmRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbUfrT1Er4sW7I2zcKa6NKPcJDyRLOpEqlk7QC6JDj6b6gnoW1AmkeMBXzpUqTpxXsXRXMGHIWCjt1eULzl8KQ9GfVbXh0wJo0M_RwWwaggw96Vxe2qoNHpGEHb7XlT0Y1kEgkbgO_WESP4rDrDY5yF3kppoNnxio056eEVtzEpwuh-FtWpoSSIGG4dVDcusTbk9klCRKTUyAoX2ztwXmIEbOBqdqw2UxYWklzWFSotsLV0w6iZieTmm6PSFrz3oOELPiNttFIefnA1oKUIp4DrDgcWis4oAaHQ7t47A_mCwvIc8FACigx0GeJu3ob_sm0ZweHfr567gpkhWzDgUMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVv2KFFHH0BwW7RtNB_1-C_hzje4Ja1FG7BbwKAw5TIseCqiYRK6NyAzRI2SIG4MGokK-r6wf02vZwGUJBuiPGiA4-NACYl6HlggXjrfJOqfWS3Wfj5k3rHzvRwYUkJb5TrEfmuA8HHsCpneV0WP5qTBqqyAm-BLW4JG3Zzqwf0xDdUAVDaf4W2opMvyyDngzweKoEI7dRJu4jqWAGH2bL8l5AQ656swoxEuhBnyCzbEBx1N-_PskfmPiaHkeobfM388JgJQ8ZhNT6w3ilgfwa9XNAw-Y0-PC7WOF8V0N-q9Xz9gEd-FT3aMavf_6AdtMMoIc1gPKc9GbYbp2zB6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4bJWtoF1TyEpYXRr4GArRU45nqT3X3Qsl_gNW-RMWWPhvJOtiY5l3TKSrmSPC5Kge2el5sm8dEKQgCtBUVi0HdGnKswRz0Wn1geix3-kW-koKuVl_G4jtUTaWNqRKd0gFpzmVved0MUkzn3MgZkFFSqApyZWEn5ji4sNOaMByfxtYaScu7yMw9fCDf5sA8OwGUY1uYSYjdHzwaaM6QSPBYhmRUxfCRglNt3einkLxWVX3ZeIu996L4-spvzXq6w5yb_y1qYDhGqDoKumm5agIaiiRRh8WWNRwjmNTCVbno8XH7Wp2ds91TbtNnWg8m3DaCaD5mZ6MFTJzJAHy1BvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geB9iHd1b_HAmYZ6BQj0Re7JPYia_uruQL4SJMTUvnp-yhvp2p65tKvYWL-Veekxa_vzoMfr1AkzOtwywCo82WzPNL1Ooml8g56TwGcMzqsf-AI2-T1yzbq9kZz88jOsVxbBVna3wQA6iAYLt45jNl7cW1q9U4_6dk-anrxdIhdW4IQy7DhqCSK-ML7DoqbffbE1OuRfyeTvwST7exm3_W2R7Oh0ZFO5sULt0mDQ1gZVUHizALO7iXg5uQ3ZLcHZ-lVgPrwMxBXpIO0BNWgZtj1TV_0Vxdk9SpuXMNPRJ0GYYiscQKaRESU-omoGA4NnR9Sz-TlYbty6-cv7Yci5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQoUt4knjCINJGJ7roJxBcSilrzIp3kLJuRjROWqZ8wTbI0ysn4mA88Va4srgEblqPnM_G8gTWt0YYt5FEcUGKow_LQhsq3lkz2KiA3ZsHZNoXvvAZtvog1hutoqMm9LnPpUK4agYZ4Fr0Bj2_hlmyNxdDA6wCxiaL1pfbHl3bCPOkX7vUP2E0wtOuoTtl5R6YBGogUoBy0pT8oJp5YCl6aJK9ug_sJ15491rVmirLKVY_c1uVw5xW0J3XiudcbVHKtCSVDB2Q5UquGhsUa5V4UquHtrslfdsCVVL5Wn4kSywe1d9YpqVK3RwalqkxZgkVlMd6_fR8Hz077zily7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkihzorJ5Qha745M-i0dGTP3iVoGSi-mCIt03mxkyWxoKeneFwCOiNVyJj_HS2o3SzsTH7qEQwXHXzz3SRm_irmekLC9dG6Fn80wlX1lLCSFpcjL79k7qYH3-q9_ydiJHNpu8UNCBPQ7BxKpDFa-QR59aX4yhk63-S8YlZuWz6R7__8UadbpNCVHwrtjJq2gcOThTbqGjUjW_NMOVOW_-Ly-JSeONAIkciuyPRZvNbR88oSnpIjfAAS8hGgxhX61UhniWOsRZxjowl7_gAnuzqc8DFxDM0SbUY36fnjdNREilXKUiJIn3ZujDOOQ8CRgCfvNEIk45zy8bRQR-fkSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsRTevkTcmUTqeNgu9QOVpAp_MyD4GJPk1bX5NVYO8IGDilsWADK9JBh_HtAayfTzHTMC91r3wxiyvg1KB8OQXKXH4jYaA4aajZ7f9lF6R5ZcxL_pwWk5nopfGGgpTIjsx5EdoXMm2pdO70iBzyLUiUpe_j0nK3GOHPB86bwn8Bd_H5wvAkHdWtXtv3qE7Jv_3ZH0dG3VHPkgOkFQliKIjrdl3cph02_43WFhJhD-IqrPrxdHZytgYnjSLwzpsLt9umB3mAMEkkhj-A1r49TpCCNRqlFPv3J8Ilg_l4JnBHktH44pN0Uj3Zv2AeTFagfyNNSf6eguVwrXosduxFjRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9JcV0NnLWTAReYlLTU42UEAzV-RyfD3kAini6CdZESzynmgwP6AL5XqwVUVk6SwZcSuycDBGGs_evEDwyvekrXlYV-i5BCukayP0HzNcjZgcdxTNfdmrYcBBGPIJb6J4kqLRVvRLwQdZbAtXrK-al8EevKrEo8wIci7UzxtabThxcatSPQtI_LOfPKxqe_fvC9JK_xyIzQGSopNmXr5cpZnn1TzcjXHts16s1pI7HrD-AfTY5Gb4qws0LtwxUQYGHpkFtQ6FM6YXQXwjf2JDsGH6qJ1Z8cW2JTvdQH19l3IXhFWQQEldtoY1oeNRAtxNRz2vx5hyfF8kskzWycUgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U609uU84-w-eKQFiud1wYkyotTRWfjcGH8nuYOFCq0Tr1tOlwgmQi0A3EIUT9z9GGrlZ8kB1tTuUh8QoOCGvug_KN2tzU9ozo2kPYftpnIeI3qNZbH_90NAg2qXTxlpAkc2iZwej6wjt_Iaqa_sLX0pHPLquDUwR-mmEGlPUjNWjcf5UKYuGpYFbTlkWVkSSbLdX3bOHJbJfQ-r03_ZrqdzU-tuhzxXtn0-T5NopCSJvVG7adGFC1H9shRX9wB2kJlU5JFVQBjcUVXyV9albu44VwGVXJa-YBwlwgbV2ZzSgo75lbQEmKRxt7dHqjeBZYdy5V4mui2R4HaF33lzTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=IHtDx3RBcdtxcq9fzVP45rr95Hc_z6DA30WfhsKlmhiJVqyBn8tvCGl3bvX7usYxEy7dE3nCextOlwIYLcBWN8NFwFz8tWSzr4m2NhDSoImPGsQfbm5tTuceuOCJeRxzzCXmtOEHlYYORndyLHGyDO1MR2DorBL5jUPZw7OJ3wulG6hN5oQnrlTqQ8Cp19vV3biO4LG_Le9cTGoJ7AohPdSGj0xZ3XjuWR0CaVTbzRt9TetfD_GYaaQh4wQaQd1R5QsLGeRLUO62oHE17oLmmjdzb75HCxOnYR80BMFB7naBwJKZaDsi09yAcJ9uiTj7bBmq5SsdqanSs14pQalN_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=IHtDx3RBcdtxcq9fzVP45rr95Hc_z6DA30WfhsKlmhiJVqyBn8tvCGl3bvX7usYxEy7dE3nCextOlwIYLcBWN8NFwFz8tWSzr4m2NhDSoImPGsQfbm5tTuceuOCJeRxzzCXmtOEHlYYORndyLHGyDO1MR2DorBL5jUPZw7OJ3wulG6hN5oQnrlTqQ8Cp19vV3biO4LG_Le9cTGoJ7AohPdSGj0xZ3XjuWR0CaVTbzRt9TetfD_GYaaQh4wQaQd1R5QsLGeRLUO62oHE17oLmmjdzb75HCxOnYR80BMFB7naBwJKZaDsi09yAcJ9uiTj7bBmq5SsdqanSs14pQalN_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCMKLVuAD43vUSZXzqrnBD38xhJBI4znS0TmcbuH7hfBzal4GR6zk7ealelMYChsmRZ81O375ALZOvuSXFD7NgEEdW_UfXtCNArZGmvJT5lpbaHqtAeYDZeaiPJlRbOrQ82LHeyyx1HZwUMtCElVTKKP9C7a2tmYjQkQVeeFjGz-7FNnAxNmj0tV98uxvoUldtJkzGf7p7oN27ffu8rFjqGopU3dr8NyJq1a04rc_vtUDQVl2gdlArE-mu6k_aS7x7JPJqfxIAvD1sEQoKAyY_1zIZ-zhbayBsWYTmZs3kCaLOTCT-5_10QjVEgKI629KzCOHLXPFiuVbYtDpKbfng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiuEDeHbrJ5pw5O_EmBoL8kp8bFXNEdMKuAHyqZ6SXqYW79SQN9nV7HMDsjQ5CCmVnRyUp4PpGt_gqEgD3LjfJxKHNenn0rA6C3q3Lh64O5H9h1fryHWpg6MeH1hTP5no7l1SZ7PwaP9TLnX16nRDo-CObII1T8RkffY2HkR7hFxYXNjc9s0syHsWEKq4yLF39DfELoyE708N1GOThma-GNEwxavXWkORx6_I2d01f2q1dyCnLOrgWNvy2CL-AIdmecDzrOZsJB9-ZasBOZ2CWkf100DQKXS98Vjq7UZ5MmjVqkArtPrhx2WutQWfbqtnLhTLm-TVxgO2hsCw7htGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FysBppDn8sJHGSepPcZsmHapfHbjiWpFRcDYUu0NnPXiKyBzaOBwbwbzZ0vssVzqvMW51U8JTngIK_aTDl34gAeowl3ybldG0gHymQiV3RpeHiYVCa-tvG1OYqHd86pv3yxbGwK-dFHHJLF9df5b-kCMGFap8ObiGJyDX_0Gyz632LdBWToDVDwr1pAinGo2mIgRzti8u3If74-_EVD50RPOZc7I9rLUYIbOX8Ps4EFXdmmAid4d6xGmsl5Jh1mjSmbduJV28MdrkYrnNTxYhY6mZXkpA2DzPWHBrFhQw7LBe1_9q-lDbwwYAOVlu1qqQ9Ihx4wUlRaMXXQtMluCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-bmdwrS0OYi3sB6Vj3tlBjvSwdJLnXc0e7c_jEIXMqrtKDYIg5VOX5jffef3lUHb5GPWB6bwdwm74lVDPrPM4UzgOjyaTUnTAliVUbug27EAYol17R0zhDMuLi6guxDxiukRwRnrog2FWiKtM-gYoGSCyO70t5nsKbob6as3oaXXaDWhUdIskA2o2cSPWLzML7ii1ZlG9DAPHwPhrzhmoKVZUP6ILcvoA8CFxA7ffOkwabMYdqGdCRcLP5UyXpfrPiqLwjmq_nplQMY_yKllI4KVXCUMoiL-TcojHIGchDJmQKLEIEY0AqfQtSoSm704AFbmDynbC38vT3RD9chww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDoeVTvlg_q4NZGobqML27Y08OJXOcC38TbHWIIuJO-980TmHNKvzLpk9fdQWibUFbD7rcYzUyYwveSVWRfDdu4VxfKEMMnKUK3MrmlGEuJyGR29BFV7F0Wj01MpIRklbKtG8yt_J28hNASaLPKbWpZAaYK54JBR7b8VaaToDJCAlVybcA5vzumKl_W4AfE_fCbs_UcAiSxgAxAjgSIGm2XjLlWos5CEsEbHRm_7iBrVYRbRGt50sjRMOh0Jo1N1Iw2XXOUTdihKdmf3A5OCRkfQfABNMHUI0TQtn_HNY4v5cGEig-JY08QLliu2yQMqVuB2ast138JxelAAjW5jcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZL54u99cW9jy4KMmmogwTNzO0x6rWrTqkCsua4CZ55GsPH2U0air7On-RNcjnQPl0ctCwWx46ng0KlrqY5DutyoXRok7jlyXCKrhGgm7WXcvFIaS_wNV2xDK7Z-qlO9mZpoNnL4eGpeBH7WFVEeOEPykL2YfJh8BvA6x2cfm_nDCZlGYeLhvjdwM2fUSt7-Xs36iiXNgu9piiDHnDit8ow5PNCAqrsCSvyqEM9KmtxjJHcqLtpMH9XokcPUUk4p2WHDXjeXcKv_UfObiiDyD3TkJGxV5IqsLFzm7mA00sYat93OMF9KlAFgEwu4wYX0_twaFTo2KPyDPEd-vE_bwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6Hum_To1QN0GYwL6z2TGD7M-s4PjxsbNiQ7H-ASO8fZm0gFTKn-80HRzFR1WGjykuCjPEoWmmHJdWtdvrSEVibi7Xj7mqMTc1Wg2Lw6fv-KQuB8tekmxti8ACrBAsV_5Qgs6R43yvn1X4yKzkr6jNUhzl23d2aTZBn1yMyu7rIBMmoe2yuE9Y_-lrYbCA8EH2DwVaUqO_WnLswU5-e6S8XPWMn8s6pGb897CFqFb6ZA3FIYFoWLVwySfbB-hHUZVOt8Mqe7hrgjrHcwEBd1Iw4AJ5-BzxQUEhfBBHHb3OYBDEgkUUm5_fp4F4fV9OAS3urqumRZi48QZXOSmbkAGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGMfrR1WBAXUZQWUPmzL2juXAkLrDV_JE1KLKhHc72cG_foWsMjhy_HAczJ5SiUkgqfqw5SBEP4SW4jAEHnmaGLNOMSEMVFwQ5ey44YYEkuwfPy8Pc_BJqlDiqH8fX2scp7yVmTiZL0GWeVC8HVE-IxyGJhkadzTB2xsxWaprVUx8tOpgkXzEnNn-f3oE1YVvmNeZhS8l8L3Py5Yy5iS9JAUk6zo7zgM57eXN5FZu-4XykG0LinikyQPN0nRjWXD3h0n7zbaSorkU64e9uvTjHmlEE0iev44KldqEeIdLn-uKFMTFWu1R58DEyGEIvGZUO3ZyF0Df_I0VA9pubZH0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=RHQebNoXiz4DReKYaMrzavyWijMOq4qd4NCwyWwo5pX01NfwRDcPUi7eejhWABHx-2CPk8oH7QHI_KeLOj2F6AnHYHiPmC2OtZbTNKu1uKtQTFXrEHDsb8oWwKEkhdXaNF_jgf_f6iw3SLyF_wzLUaPf5ubm4obF1IWE_xvtpkIT1fwv0irKgNpTAfubzuEBuaDiaSmWfVCWsCH2bEE1jnXpWataU6MlWDR2S4d9nT0nUYNxkeK2uvMtPdM3SZwzV_9ycrIg7Rwz5fepWgXj8deWHOEt5ix7EMwWyMs1W2FIC5h7v7Pr3tTlfllyoIgzEHzE65_eYbH9sHtfpm7vBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=RHQebNoXiz4DReKYaMrzavyWijMOq4qd4NCwyWwo5pX01NfwRDcPUi7eejhWABHx-2CPk8oH7QHI_KeLOj2F6AnHYHiPmC2OtZbTNKu1uKtQTFXrEHDsb8oWwKEkhdXaNF_jgf_f6iw3SLyF_wzLUaPf5ubm4obF1IWE_xvtpkIT1fwv0irKgNpTAfubzuEBuaDiaSmWfVCWsCH2bEE1jnXpWataU6MlWDR2S4d9nT0nUYNxkeK2uvMtPdM3SZwzV_9ycrIg7Rwz5fepWgXj8deWHOEt5ix7EMwWyMs1W2FIC5h7v7Pr3tTlfllyoIgzEHzE65_eYbH9sHtfpm7vBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuhcobGBZSt5r5DVU2TO__TP95rF9nHQKMwTon75u6nufd5ijtoT5B-grRrq8NWPIxbuj24Vp7WQojeBg0jU-scH4ZDZBP5VTW3mUVf1HlZeT4BRsT8thkkzIj5vy_id-nrKT_aFW_B8ucGtY1k7bl1vEQ0WKbvKgaqyHrr7fH9pTiRgq59Scnv0Q-apxciC31lEKlU9wFcPtBQkHMMfRXAzbsCj-BLNoOZuaN2J7p1yWmbJnUMHGxkjPWntDPz1rK50ppec6EcLFCUnhnVyUFbfNp67jZDi_lDmMay7wyB6uYX-GljcmmVUpQ-oachmk4rMQKoKYkA1CXLVZTqwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTrXQT76eq0vnKjZk2OXIE45WuNLd7IfuKL3v70n6F3VFOJkyll-84W0OfcjVgP63ldhxzlEPi4HC69kXM7rTaxsrpTMvm7IohX_Crx1qYaKlR_ECTZymN3LN-e5vjcZZHuLvvOOYeTG4IvLLcn8QyqsbKxPsO6SvK3Vgfo9VrCyW-OQfib6Fp3esMPr6p3avbsDgI_5VZoNFPm8kTQwW6Anyn5uQZpmsc9Suz3JMzFneuXE3hgXZASobP_BMasKobIAgREn0G6wNkgUmR7lVQbVhs7d0xQJkEQOvRNJctj-tSGO6PwhV89QNmc6YWZJEvXEVwQ89JTR3jXf4Jhxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLgEviUjzuworZL-jraj2iJfuby-08SHOrkgru1SHBwS3hNdButbfmmRAxKNBulbLpUipiY9VQKM7illrQ95k7BHqydbGkW33n7i7OOvtXLdPKfoPXrLnXCqX7VphPRjWyi7PokzFXAwwhYtRrBWnn4MM119BwfbYvcIHqcNAm-EU3NZUw-b809eYmbPZ9-XX_r9Z1D7cTjeMORYc57Q6BAPQlvNbXDW1DsSdX1UL8gLJHRqlwgrW9pRMIUU_YdI_aAsXL5wSWZUmlP87CZC5K3GNpHYlueZ_1ptUEcoWamlvBU6z1sUCG6MSggXK0jnQfkkyj7KxQRmuMqq8lw-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2amthJM3Ul5QUZjGr7KeLgrxDYI35oRhPZUebHPsy31TkZ93YQf9fxJ5VdGEsBs8NMPdbTLVIF2ENo_KiiNXvvm5T2ObPYOATm2f7Y-DPWrx5Hjqcg7SMAB5b1YSQb5pXIxQGsFxk-oRu9JuQR2Ti9zT-8A6VmFMaaJjof12Ml5_5Ab347j4j0scW5xL1w4v6A_Z1I8LG4NAJnUpc9bQw_Nw227vCvLGN9YmLWyaAEKyv7T64wJSlZFbRTKw19UITpSN1X2KHXH3EbqaN7W-Wq5CR2LV4crWqCQxfv-OXP0nsPcUSMFHkqte2E4F0qwKz7Jdx_0t5yMyq_GkRCO0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urHB7deXIKBqeC3YPe2Q-P3KII0Ju72x-jVPSlxRFQZu8mPrmj7wN14T5dF3i30dpOE4o0DH6INc9Yq8bP2lRMAXgCRq33lFf1ZPQkRi0l_BWDkuWJa-hVQgrULfZpUZqSXY7zscbpRhHP_3d3C7_PyQ1JrOVaDTMFWlDLBy80yiqyyuu3Hz4wXMYGvVYkCoeKzMKmWLjh6eNsAW1L818MmxHIUMXVqxeGPNuXoypljX-zGbPlmQO3q2irHUL2aA1G9J3KrgC14_DlGGSLR_AQPM_tXj-zx6hzzcoDaLDQFumH-5rk-q-uvJH7EYeE58EP3LblqLfpQNcWhxV24NiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXeJIi5tp1QXl8ym3YsXFsFcHG8orCqCMyFYcqFTLt8XEer1XAr03JRWus8PWy616QLRA3p2Bkv0g6BKVcKRzqKp6ehj2uB-DEyoRhLzY2NluJio8BoJaybQ8CfCjMQipm_K90GcpLT8qADrIZIQdpIyPw4Cb_WnJRcmrxk_DVF79ohp7YS1hpRy6eM7jzIfnEQ4GoMUQ8JC4H-jzP7H1Hh2ZiX4RBymK-b_IMBwwxRSWDVGeDk7Nc4i1UTIMipel_zCt8rOqQs9ZmZqk8uaCi9mkfBy9u_WdDwkOKTEdYu5qJ9go48c1-4h7I0U3311Ybtui5_c-Ql-TeGMMXLfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV1BvxNwX9mcbhrJ8gJ-3-3apI3jUNhqkjzZH8Vh4CweSwWbFGlrVj6eLOI96mgA5FMXQoFdfami2K-l9J7mgcM_dAp1bYL3ig_tz2XSyqcvyxh6HLUXUn25kuhvOZ8Vy1VCwqPFE_JsalUAwFXcDc-GwvTxN-HKQu-2Llm6RBcTQ4ooh5MZMaxfKg2SrogZ61JoQK7jQgYpXsE34EikPiM0pJ1J-xJpXt7p9Idvwgx6_O9u9MHj0UWFzqz_6KYO1XMPF64P5sseTnZeUR8bxkduSrZ9gPv0xxTHEpBljCzus8bp_02355DQ-3EYFa2yOniW__pwog3AmBQDbCpjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=NQQsNFG2NAQvbOipt1mDqDK9dFI_8DQjs5Z2l4Wjg1ObAkRtMYLCCsK9T3n1WXJnhYNyhXw5oGuZPP6jClPm6HYQpLYJTFGD-zuFzVkX7GyvH7PA8v8HZDJjJxGScCX8dFL5gWbbdv1DrvB8-IyQP0kzoiRuVYD61xtmroX3zncnCsrbFQFg8uYMbF-E7Ianeb0loAOacAc0ViGqXIw7UYNUYhG_FWwf6E1mJhyc5vSFLx-ar4L-byfN_ZABhGVXFh1baSre0vvXqPSat56Hz3Kb-CLdSFSJi4gEQzlNXev1Z8RPCmD2mWcrdvRhm6KRAbU6WV2ZUNTZcfAp5RnClG7-cLFsRetVfulPhdQftIrw2Hx565CswQclOM7iqmwv5vpr6HpZEtGqgwSlPoprUMP9PPoNb3dA7QuFxks0wxaLmgAa8YVnbm6bAE7Ldh1MBMLYPh33rmNIKKuss4iaaP9t1mSJ7vsoxJ8FL64YyesSR3alwqnB9uOfo-XML9qH0vfkA10IFOrEPJFEvJvwZ6EiSnAwpPibwGRc18uxHrHWXbvtAXYv5iibpzU9tH-uulAkp29zsIyiVp9dsngAai8sDJxISSj2xgntJ362x4Z08ptJsbppTircc2cSagRJajBaGLFxTdRr0FqgUfnQADCaECR5uLEgXxYxvJLqgVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=NQQsNFG2NAQvbOipt1mDqDK9dFI_8DQjs5Z2l4Wjg1ObAkRtMYLCCsK9T3n1WXJnhYNyhXw5oGuZPP6jClPm6HYQpLYJTFGD-zuFzVkX7GyvH7PA8v8HZDJjJxGScCX8dFL5gWbbdv1DrvB8-IyQP0kzoiRuVYD61xtmroX3zncnCsrbFQFg8uYMbF-E7Ianeb0loAOacAc0ViGqXIw7UYNUYhG_FWwf6E1mJhyc5vSFLx-ar4L-byfN_ZABhGVXFh1baSre0vvXqPSat56Hz3Kb-CLdSFSJi4gEQzlNXev1Z8RPCmD2mWcrdvRhm6KRAbU6WV2ZUNTZcfAp5RnClG7-cLFsRetVfulPhdQftIrw2Hx565CswQclOM7iqmwv5vpr6HpZEtGqgwSlPoprUMP9PPoNb3dA7QuFxks0wxaLmgAa8YVnbm6bAE7Ldh1MBMLYPh33rmNIKKuss4iaaP9t1mSJ7vsoxJ8FL64YyesSR3alwqnB9uOfo-XML9qH0vfkA10IFOrEPJFEvJvwZ6EiSnAwpPibwGRc18uxHrHWXbvtAXYv5iibpzU9tH-uulAkp29zsIyiVp9dsngAai8sDJxISSj2xgntJ362x4Z08ptJsbppTircc2cSagRJajBaGLFxTdRr0FqgUfnQADCaECR5uLEgXxYxvJLqgVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=j5vxj0v7eXp8-6NPfXRqsZNKguvAOdvCloZa0dorgJbIly-ldG4ipxiFr-VfgfaP2Ngzja-97Nn78QUIbupuLkKgU5dt0iGuV7WdfzVpgB3NAF1EhDAayOtS6pyW3zmE4ieV_j9KKnSlGTXOsMKftmrllohDvWZE8r7Jc6f2QFA114AunAs000gcptUUJJTPZ_k4QeFt1nIyeq3NU2uxZ9MrLogOkBCDebdacvhvHV--jqdDjTNlo9MuTX3r8Yh9fNEnUp2UthYhoqakM5OSWjv-VkgaHwtnU4RlYyWOcMcPzXJSlJyN2Pa7Fp2VF6Nygc9nzjfs9Nxvkie9ZX7YvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=j5vxj0v7eXp8-6NPfXRqsZNKguvAOdvCloZa0dorgJbIly-ldG4ipxiFr-VfgfaP2Ngzja-97Nn78QUIbupuLkKgU5dt0iGuV7WdfzVpgB3NAF1EhDAayOtS6pyW3zmE4ieV_j9KKnSlGTXOsMKftmrllohDvWZE8r7Jc6f2QFA114AunAs000gcptUUJJTPZ_k4QeFt1nIyeq3NU2uxZ9MrLogOkBCDebdacvhvHV--jqdDjTNlo9MuTX3r8Yh9fNEnUp2UthYhoqakM5OSWjv-VkgaHwtnU4RlYyWOcMcPzXJSlJyN2Pa7Fp2VF6Nygc9nzjfs9Nxvkie9ZX7YvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzFh2qKSrozEghpa1zPtO5UoaJJiJPq5kQdPRnUUglWQ6y29ZN-xYxguFQTyYoefsEipDtAjAIoxum058qgBEfN_oip34PT80q6IPb8FLtzUT_0SRy6ApZqBppNApd6eRYBDsvR6vaP2JxpO5FcvpdkaXO5sY0DcsFDozsPoandF6UZ4ZBPhCTqCKVRIis90oau4hJBrHaC7CqfvY3UXBgEEPfW72wCeX7lV5z2pTQoI6H3P4635yio-pXFGcVT_SRlDICozvh8DGNhpJPl_paKTf59IZSnwA1epoGNF2sk0_hlmDH6amWu9NWy0plnYPGPY34GqKecNYwe1N7Xx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki3JChpDcqt_Gz5TeIKORZPSbmWdO7EVPx7v-Jjnoi3Hnl1eARKdr_CI23tyHSmUhkrmADe8T7oj0e9_L5pEdBqxuL-wmm6u99yqaIbHZflM_jrfG9Gzh3bBdHwnM7irpUVvmViDv4XCHcW_BWljgzJRUDU7jsVZNs5ewqXsoLFsWk3WWOuOpcbslJ14z8yCp7QbSxE7qGmDhb-liYOuGCzY8yzmVuFt4evYCggH49rdHUqUhEdsh5ymyxqc8267X4dPxT8ZBOusXZYEitDQU3Nq_yNBUPwhzp-aMyMk103m3o-OwtPytrH5sShsIpJL4SPAlDul-IFJ7qY9JlRebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=tO4a9HCn25hFfsG3nyn8P4kZ8U6hjr9GrAVwBmBAUe_56vLQQAAQM-NWkVyZlXKNso8dZGNrBbIWG0nGXHTUwbIe_leielokMN6d4G4GKL44Iypkfj4gJWu-pTsqix6hwZsKjxB8yeHQoDMNs3cwSUC0q-A-VH_CteKqaXqGE6E-NcGbBCYzMSinlpwqSCQWJV_zucXfBYwRD_N6Zuie99swk7yzD_yJ_d1Qfwy3PtKCPn43pT5gq-WI6P12ZdhdDXNUsrbdI2Nnd6CgbdgLW9NjaUV09oTCMUy6zBKCIkcrnFfTJ8QpiP3FHf-13FGlCerv1cCF9ghzaRaIP-zUwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=tO4a9HCn25hFfsG3nyn8P4kZ8U6hjr9GrAVwBmBAUe_56vLQQAAQM-NWkVyZlXKNso8dZGNrBbIWG0nGXHTUwbIe_leielokMN6d4G4GKL44Iypkfj4gJWu-pTsqix6hwZsKjxB8yeHQoDMNs3cwSUC0q-A-VH_CteKqaXqGE6E-NcGbBCYzMSinlpwqSCQWJV_zucXfBYwRD_N6Zuie99swk7yzD_yJ_d1Qfwy3PtKCPn43pT5gq-WI6P12ZdhdDXNUsrbdI2Nnd6CgbdgLW9NjaUV09oTCMUy6zBKCIkcrnFfTJ8QpiP3FHf-13FGlCerv1cCF9ghzaRaIP-zUwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE9aLohXiVuJg5rK_1TBsXAvoDiokRdgoFA8MKkvRXomHJ0GJNoyh-xvu0CsRLusbekK6AaW1bySRXSDNLeebBOql3a5fvO8VuGHgsf0MdVTYC8S25aVXj6hXyxqUvHpYT3jUdQWkIXf4G8vHpxjPuSkDpDch9ysNCoo2PW90cofkf3iXNR0ygBsroC-xQ2Rk0A8u7fjqJzev7i1wUJ57JT3BRImjEFniKERXkIdPmtuX3gSeNgQO1GtKLfcAQd6tlYdAlii9XjdRdnHEg1c-zThn3qqfVQI3E3w4y2GFxAAax6L5u5yFH7E7uYzNSZqjDWYnTjCMRP3H7f3RiaaXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0HKp6mDRmHolVV0_c3mDSEQEfcaYUJNRUXpWKVruoZhdQDqf54CNS_rLqN8FTv5z-oFCCxuX5Z_xqL18E2JkQF9Ik9qD__dMIhuo0pxj32A2mw2Ep8ntXFVS7Q6gfyR-bd7R6EfN407Jp0JHxxwdC0MW1GG4ZV9BQ2NYYCw9lIUfTlhb6jxpFKJQAjRCMC2C-hA4wUvWEuc5C32CNqNTteIOgrU0T43XH7VaovGN8NXU7iopBSK9DpirFBz43G5ylqjguN2CB6QrpbkYhJpMOT-eNhIIIo_hDnmdwX3jfe5fzEMWzZ2vK2B0yNi5qNMPSMEdL03GBDRkC7-Rjpytg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riWI2syCOvyOHekeHayjokMCo7gFOYscfmPhz61rMOF8eouOG4JgtL85KinE9iI2ovkCEhrz83lS7ZAkglg1L6ir4CGAtrHYNVTnATi1eANA_dtZtHVqdS6W8z2EqCo6ZA7oMuRmyD6BLVxGkW1RSg9y1ngA1I5FmAe0KzMrpsEER-WilzpuL1khMLxqjEm2Q_AiOVb_1oNQgUE1qCqb59sgoub_ZYd-hZpsuX9ZcdNWMjeMELbzEF5qL_qJjzuJYn4hPaM4EgvDzZ9B1VGc45ea9Z_BVY6au-a9bhvKi4RX0SVhzC8MHGCRFggEY07U55lBIAFa1UaNYT47Dm2TTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEbSrKvpmBgGp85CDLDdP9AYs9MbgX5WBXsv6K9fWkB6ru4Qn7ZNZmd_0weWOYcA31coEDaZfN11Mw8cPpm0qPA_cvnqPFpM6HGO1qEZcWDlKP-OgbIDdDQ56MD1P5wg461A5GDkxsg4AqFj4zE197zgDRJdrfZGOqlPWoA0fyc8Y89hJWIErTvwAmxiTVg79atlHV3UaU9q9hKKgiU2gEf3lHcqOevSDLr-V-_br8qhngKR97lnAMddgU-6bCjQg4ANsXCNCKPFxxuKPApwuhT8g_lptmqCRBWe97NR84orjeBCZrhj9-egfY5X1bZvgugKLPvFk393Kq7bhytIPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxKE5DPlZYedy6iOcMy0Y_eXID2DLlCx53R-E1M4X2RbSYA7y1zdK_E3BKBWwGdR-YvmuFmqXMYrjl8GzbonALLOqZKibZyI08qUWhqZkSy_YBhSYVwCFioONNB11CSjkJ0Sm_Q7U0iyZDvtXSnm4fLSIpz8RGxCg2UptsFv9ktC07Zes2qKm3nc9wIPve7oYzPtCUqhGCigbxsgtXoeZ41E5TnpbdGpNw310JXo51-oGFx7LXa5kVmtvKSbMkT64S7cSF28YcizwBldQOv33S4uVoj9UMr49PoWzBCdU5gzV8PfQ643EPi-svtSNTStTs4DscakKTKIGdChEtS34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5QvYaCIV-tA4uGgmfTW21YmiiTpOF80vgUUYkGPwbypPMcyKE7FWessWB3fuSfLxg-ehtx0DcQ7WDw-OfNFrWp5X19WM4CmbuI-lMUnycxDnE8LbyIS606UeQkCUR-GRZgmiMuFhjveZUCHo8l9FObm_4_wt6LzSHEd3nm7PF2VVhmBidz0_kU6s62a0yKtb9leqnil92i7qAOTo3uTy_lAS59gt5qrmG-7PxdheTyN_oEc2jPY8FBoKOTAlZg9ecJWUCYjPc9DCJKp5PUq5nR1lSHJrkSjeLPMvqW9d3k5QX-oDzPMjmYX5asOvgzQsMhlZBYwEW4nWlx-ggmLawzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5QvYaCIV-tA4uGgmfTW21YmiiTpOF80vgUUYkGPwbypPMcyKE7FWessWB3fuSfLxg-ehtx0DcQ7WDw-OfNFrWp5X19WM4CmbuI-lMUnycxDnE8LbyIS606UeQkCUR-GRZgmiMuFhjveZUCHo8l9FObm_4_wt6LzSHEd3nm7PF2VVhmBidz0_kU6s62a0yKtb9leqnil92i7qAOTo3uTy_lAS59gt5qrmG-7PxdheTyN_oEc2jPY8FBoKOTAlZg9ecJWUCYjPc9DCJKp5PUq5nR1lSHJrkSjeLPMvqW9d3k5QX-oDzPMjmYX5asOvgzQsMhlZBYwEW4nWlx-ggmLawzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnDtSkyJso1CqxxKYIs1l30zxzzvfDLF97wy2XMzA5N_brT-tAkRx_8jtfDUkotuWHmM3fSvdZq8fK90XUK-CrlcUB9ehjKLMN6ArzUSDFheV3VnB1TUR4ii6gRSYxEcTBUanKL3ZWY28YX_lkt4hzyf49ICrPa6vGMXz247gnvZV-w-w4n38Y1--aUpULV1sVQN02oLkzzYrmUUsWu30HO6G8Gu7ZT9J-dt6HGHgT6ZvdELXjtdgYRxIevbzTS4JLTiGXGMcl0VB81JRAxyStGtxVUU-TYCVXAWRLRvjG_9osn1bA_F8KodjZ9yoFspcaTJ23dq9ujLrSS-QvUKmKTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnDtSkyJso1CqxxKYIs1l30zxzzvfDLF97wy2XMzA5N_brT-tAkRx_8jtfDUkotuWHmM3fSvdZq8fK90XUK-CrlcUB9ehjKLMN6ArzUSDFheV3VnB1TUR4ii6gRSYxEcTBUanKL3ZWY28YX_lkt4hzyf49ICrPa6vGMXz247gnvZV-w-w4n38Y1--aUpULV1sVQN02oLkzzYrmUUsWu30HO6G8Gu7ZT9J-dt6HGHgT6ZvdELXjtdgYRxIevbzTS4JLTiGXGMcl0VB81JRAxyStGtxVUU-TYCVXAWRLRvjG_9osn1bA_F8KodjZ9yoFspcaTJ23dq9ujLrSS-QvUKmKTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=E0XUU-HdCHunBWHoCX9TJNWF0esqksDEyph2LymR0g09i_9yb6J4oHtXQFLKUPw-c7XNMjjeQF9dVK4GDVcz4U6COJD0sJeMfVZwEp36XsmqwCnjbLLCCjsHnArIcZR2oWYhsNJ5K1Qp6O9q7mQhUIGjellimTerCfvLe1FAR8E_uFmqdkikEPTIr1j61x5Q68ccOSafKaV_zVacoH-fa161KGKRStgWS9bMkJsmLHTEbyOzaMPyjxPe3pdpxFc9eSKNOxwrHjPfa2NLptK5KtImwHgCyeqcOQikG5k3uljuJ8-8y85xIxSpFWzQQGceZsc7pjojSJGwwM7q1SEelw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=E0XUU-HdCHunBWHoCX9TJNWF0esqksDEyph2LymR0g09i_9yb6J4oHtXQFLKUPw-c7XNMjjeQF9dVK4GDVcz4U6COJD0sJeMfVZwEp36XsmqwCnjbLLCCjsHnArIcZR2oWYhsNJ5K1Qp6O9q7mQhUIGjellimTerCfvLe1FAR8E_uFmqdkikEPTIr1j61x5Q68ccOSafKaV_zVacoH-fa161KGKRStgWS9bMkJsmLHTEbyOzaMPyjxPe3pdpxFc9eSKNOxwrHjPfa2NLptK5KtImwHgCyeqcOQikG5k3uljuJ8-8y85xIxSpFWzQQGceZsc7pjojSJGwwM7q1SEelw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
