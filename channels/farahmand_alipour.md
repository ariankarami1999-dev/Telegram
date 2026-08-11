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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 01:06:10</div>
<hr>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=PmHKt-Ni0bPcSEdASlC1ddbnaR69dDPoRN3V2FxvO1iG04DclmE4wvuHIDJcDPnDfJ5V1D-LWnFSExeAlGAGZSd7aK8a5d0vEa23DMTg09nxfGTuP1Zqw-jmX-ziKMUKsP8GLJCw4Je9f4QhGGOb3oDxuDPc5Zf6XriorYZ0SqyjuN_Nj7bBgcz0sKi1wuqcvUgxt2t0CKF5qZjFw_s5ozbVZzxmpttZ6C1l27h9ewuqw-NX4EBHb1OaoVf0jPD8F_1tsB0phPhWwsKl0DnmBDvajK7-VMgwNOVk0jx3FtG0_tvMoVkDmyY86DPIeY8oh6CWGDi5ZxIXUCt819kgfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=PmHKt-Ni0bPcSEdASlC1ddbnaR69dDPoRN3V2FxvO1iG04DclmE4wvuHIDJcDPnDfJ5V1D-LWnFSExeAlGAGZSd7aK8a5d0vEa23DMTg09nxfGTuP1Zqw-jmX-ziKMUKsP8GLJCw4Je9f4QhGGOb3oDxuDPc5Zf6XriorYZ0SqyjuN_Nj7bBgcz0sKi1wuqcvUgxt2t0CKF5qZjFw_s5ozbVZzxmpttZ6C1l27h9ewuqw-NX4EBHb1OaoVf0jPD8F_1tsB0phPhWwsKl0DnmBDvajK7-VMgwNOVk0jx3FtG0_tvMoVkDmyY86DPIeY8oh6CWGDi5ZxIXUCt819kgfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=q6Ibrx6FbfcipZQxKAryguafCwGUrYQ9oAtMVVctdK70e-GoAhwsjPvy2id56sGX3q5Hu0ILbCczyGMNi3RvscvUHjLgcjVJXlRe-DTbb_vchDjkKJ7L3Ux-ZQh94TKbhNykftvaI5BXLXW0I7q3he_NRcS5YVk-PSwAuK07yyKMYAalmjzzRLPU1tdOfraV-p6kUILV7srR12CdIj8fKOFC8YHixXSTMLV8Ilo4knH46KKP2ONXp7hrKTFhUqMmunWnN7X_cCj-kt6I_tghcynDAUntnOv4OvjXaBo3bemkQc9jfMi3FfsWJzzttLiDAthK1Ae7rVZNiSHSjErO6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=q6Ibrx6FbfcipZQxKAryguafCwGUrYQ9oAtMVVctdK70e-GoAhwsjPvy2id56sGX3q5Hu0ILbCczyGMNi3RvscvUHjLgcjVJXlRe-DTbb_vchDjkKJ7L3Ux-ZQh94TKbhNykftvaI5BXLXW0I7q3he_NRcS5YVk-PSwAuK07yyKMYAalmjzzRLPU1tdOfraV-p6kUILV7srR12CdIj8fKOFC8YHixXSTMLV8Ilo4knH46KKP2ONXp7hrKTFhUqMmunWnN7X_cCj-kt6I_tghcynDAUntnOv4OvjXaBo3bemkQc9jfMi3FfsWJzzttLiDAthK1Ae7rVZNiSHSjErO6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehRwrwTTfHTZEAAkuJ_fPFbkAduzwzO3PLrfBTEFOmt5BGOdngG8rBZIawftJ-uHzaXl7GFeHuKoijh_6O4IM8PYDEeGdR-li8aVgioYJtVRty9JWWYONpLs6vCiY4bCSkcKdX2mvQqp1jTUSHku-RIS24H46sJmIDySazYMPRFn0zgSasgib5KOJTAZ6xb6K3rtRzbGD3BHTGPZzdQuRHKctmL-vcZsWlW-ti7zrhI0eExQ1CwoQLT2nN6NMOUmSpo5Tt9Zzhj2w8Svl5AH5HMIfFPp5jQ43r5Qjs62h9eU3zAZAHlydCvYITWRaEJf9S-ekXkbgBRudTefZIkMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_RrAwsDMLyEYVlAP9O3cIHoqt1m6TKIwr2Vpb02KkW9oh8LmzojNCkuQwGHvp9eovnYJdvwq8BZPwwVkunlasHl2f49SMCXFYHFvPbADLSuE-5yEJZaGExpQGtrboXyfyKqB6xLwprqiXMFoB-Uf92VDhnaydsY2-HBlmEZWDlQMlG116xJnX6-KYtA4kJHQ3o_l3dKcR22aKyD32sXWJiSdTX-zkpzhDjKdFa-ZIIoP7sC0VfkW82JrvUkBcrO5BiKKLHdgRhvNarXGbyK1v7b-yBHqySLF3t3rDmWE0Yp2BnXcPQnPfiCJf6Tf9VmTyl5Z70tRZFQBivAK7ZwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InrP1RXG9c8B1iPcB8ieq-FQpv3bhh-T0ywnM1JIJWTowuSo0puOTjoq0QwhuhPQDosoNYk_A8-yW6cKldCyLl4hk6ABhTPmvRLEjvjOu11q_nqAvDTzHfq21JQn0Xz6Fyrxu1dFmrwSiFXlb1fD_ubP6l2OWWbPI-JG-qpv8ZTd-Ka__yiZz7gg9ImrcZEXIInnODMvlusFzHM3ppi9KrtUoWSeEr5owyOJUafHNrOv3-zRCQ4YZqBehION8EMwb6Pe5k6TPgHEhWDVIInr5ZbRdlFdk_bZs44SIH7JAQb67u18XUHuKJ-xzZIcP-Fhj2CLhjsrOQBYxCRjI0m1Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=MEDfO5kAbwx1yTHrVsttoZPC8aHZJdrPKbkv9B1pXmfQyF-LISVfbFVp53odcdYKg7J_PDO2o2UvGpPUIf8ENetooU2leVulxAx_ji9KFDaraKMyjvV4Lm__4FU84S6As2_S3VIP-M0G7O3Vyajs3UEKdJhzUypAqcHKi0kRNHvfCa9U_Ai800U7hPPPu4iOsXV4gETJNF5L9jzvToi6qJxMIR9r0WGBwQkbRppUSQHM7d9lXoqmHc04Ift_KBIyDnPwz_lbbN6DqMIUVwpiSMkNFKErx6asQrJce6FzHBUrRCj1_E-iTr8EJrb7JPTXWaPQoI43pyoa0jxgWGA2JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=MEDfO5kAbwx1yTHrVsttoZPC8aHZJdrPKbkv9B1pXmfQyF-LISVfbFVp53odcdYKg7J_PDO2o2UvGpPUIf8ENetooU2leVulxAx_ji9KFDaraKMyjvV4Lm__4FU84S6As2_S3VIP-M0G7O3Vyajs3UEKdJhzUypAqcHKi0kRNHvfCa9U_Ai800U7hPPPu4iOsXV4gETJNF5L9jzvToi6qJxMIR9r0WGBwQkbRppUSQHM7d9lXoqmHc04Ift_KBIyDnPwz_lbbN6DqMIUVwpiSMkNFKErx6asQrJce6FzHBUrRCj1_E-iTr8EJrb7JPTXWaPQoI43pyoa0jxgWGA2JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=NtJ0OltJTRbMBkHknwMqNljS-qqpfAHR-_hkc8p-_bTzV3pV_CPFUPbsfzZm7j1c8iLhIbDsSf7LgOSJQrdodc7en8TgiaGuVGW-bDAyThvs9jwLbo_v47DFDsaP03oP5c9yztj_OuKpI5dVhtaDkwpW1EvwoHIYPfVEGhyEhQv3Jld4cLI4SQV74Kpu0j7t71U4sC4m-TaoXK1MdSFOxE4olglemYvZVDWt9_0f9GihrdsLC2CGcgV4p0nCiPHabeX2ZfEfTzfg0c1WbtsZKSDUiZsJOSEpKpfCbm5e4oB7_VePK1nl5Ux58jzUuTGgEHn7j3CJjKdLUCo059EGvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=NtJ0OltJTRbMBkHknwMqNljS-qqpfAHR-_hkc8p-_bTzV3pV_CPFUPbsfzZm7j1c8iLhIbDsSf7LgOSJQrdodc7en8TgiaGuVGW-bDAyThvs9jwLbo_v47DFDsaP03oP5c9yztj_OuKpI5dVhtaDkwpW1EvwoHIYPfVEGhyEhQv3Jld4cLI4SQV74Kpu0j7t71U4sC4m-TaoXK1MdSFOxE4olglemYvZVDWt9_0f9GihrdsLC2CGcgV4p0nCiPHabeX2ZfEfTzfg0c1WbtsZKSDUiZsJOSEpKpfCbm5e4oB7_VePK1nl5Ux58jzUuTGgEHn7j3CJjKdLUCo059EGvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXLsFA0RZGt9PWdj5DmvVMw-8tZ2nRofxejMiyt273S4ChohX0t2ugsvhBHifwRurBkgA7OColWcxmCMyIUkwdZkvHUWYQ0U57RFE_vynVBTJHTWeCvpx5HTnrrT6X2H5hmKGSxjpckdU5SvKPWSzJtOqOxVG1w9IXV7m4PQG9qiF7AcDFTo2m5U22bGuwZB-9x2VagWKTN_oEkfTc9wUFnMK6OtIpcb1eLd_Y6npSscB1v9W98NJFXLZhEVm1kVRZdBCHipwdIxCVclcMuGkryjF67g3RUxLL5swIZ2lAachyAweJY6dqlM9Vbq6YOXpuu55cqGxvIaI3TitA2wFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5EP2OnyGlMij2rSYBkxRh08_WtJyA1bxfO72yfiEhVzWxDhyIvaXMCspIhd-Oae8OGmNDA1_vfRXvJElw3xpUhJ7BrGT161qgwByUl73c6nN_T9a_23XZMAz7-fdCzzp26fQurqE4hjqHEXJhNtkarX0aE9aPcIFLGO7C_GyeCVrUN1A5Aemx1Rz03dF4lCLyTgHGNW8dw-MRvciL15jfALavIR42O9q6ARy7EXD_lRX4MAi9XJ1LETCFBhk_xhkNecClQbmoSOCicKaEI08X_mwiNoDlAoESgTe6z7vfwZNz4bB_cVm8yfyI80Q94MTtvazHgtWYp0wWMg3PJnUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFpdXBRt1CSn6QUNwzz29hQPSXDZCxjS-8u8hPh-oU7il4qWleb8FfHBqZLpAKRP62ceb9aQMDYYo34vb7Syzj5Ue1cXUj3xEf95Pyn0l1ym4-3pUkEDY6AfJI3DLkKLfjKplbn_lQd3nwlwsIbxgYTJBCoJCh1V6bvSFcjaXerraRoXN699XK6YOqsJNBUHJCmLtvs4VOJb50F5_KMdVl18lFc9L_88dtYVE2tOYwyaj6tBDNrkqSt0B4ClpxmmAM_jb6JHKINt9pKJsMXRnv8-8r2QAxJVbeezzTxB9pUN-y-jqsfInXqb5dcBBCJfOr_c7XaajHfehGf-PQCWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsXETY9c2Os5uLbaTEYUMmg3VBs1qfWDuKWlQ4GzgqstuWHMGxTOGdOxzN8GN8hmmKCAVn_9NQ3PkSytg19P7l0A1A8zi5aao6mehRqPz7GzMfvaGwNhAA9L7Y_d2efvCQ1H5bZ6CYkvS5OsqiNOLJ7alq-2x95CG1jpiaIhJ1w4DH0BK4S1CclLtXJ-7uXf5OaocbybQhLigH9s_ICshRfUilNOPpWByxFCAcocyBLOmeKPBu2n5UDr-USnA_ABy3FT0XGD8dhJXycInTKJmL8meUXsA30ZYXSJx5f96AKA9AYeeg6fUvgVa91euHacDi6AJ3-YCd8mCKKKf6y7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FET_pPQe-gWQJ2qtcQPTnatZu6KA3FrrD7rc_y1QFMn-kk08pjegTUxBDQz39yy0xCXtEsg4nUE_bv6twrJzHbyqvRlh9E7MZ7ybXi0igoO5BRspVmiM-X1g-f81n71Nj85T93dCVTvWqSRotDFQiCkkd-7gtqpcZfIoNYlSpt7V5s1TcQDenNrRuoi9pWOAOVnzLMfMNZyrvTH0hS3f73uLDfCizXcmvmXHh6D_w_FrCODdwIX3kGQajqWn4_z_GXautOkn7mVhow5ZpGV-1OYdHHetDmC2nM9XrM-aBZrTvTHplpUoxYgFC_28yGNQRK3Llm5KHIQVZu14bqejGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfRfi3FOZ1GcyzYya9K5NgKAw65OXgnebnFsJ5cxk25ZSAwLIMw2WzAF7V2hole-QSrSMbHKWMMJX-4rP5I4aYDYEQ3btSskTZzHzXcwG8fbqyXSw5fTyF0WUc8HJKgsIAbxxhEUSgfAdJoQOkXD1G__XAdcYO2OHcYk6a1P3OAMEKhR5XhtwEutWgtJOfh9LuofCvo1XWSm9xgbDYB3_MmUQiLolsTxN3J1SSHFrs1J51fc2VsAmPFMDLlkeYzxZFUIpX-63fJllht3G2oEWzpFcZSLc0H6etDh3bLc3ZLSxJtcvHwtTfj9aZUxvk_1Ok_R0knT0vUsg2PgUAMBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMlRHsS1HBgRd_I3QocV5-QzFzZQhIDEtz1KEv5jkN0W0mz7rywAb8HzGVETcBv8pvnUC9w690Dw7wajcIkMn1CpqT7W6p3goSzb6j_y1F86wMbpy1VU98ZwDRnYVTxj2cB5uQaYoTCsOLk6Hd5-x9gQX2_sswz-DIe7WnfzRK9AzmXXQdTdQMIh_aI_fgshJMrUVDpPt-p8PkmURswkrhA8XX5PNa912uxVw2zAupGhPMbiil5F8VRxk3HnkU9bgbcS8M7HcCGElFr8xShkWVNrimVcp6TBuyJ_H3WOCzd2_uuQodp6Jc0JazQw56cEAcN4OF8_pfnaU8H7JkWJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UpG2BhioQqsKL6P2o8CTwHnuqeYgjsWt4TCMP0DF7mmSGkJBp61mh9bcKoehbb8zpbPjf0HKymrJZd8IknKN7-5kRYqO99T6WxFdh2ZzAy9KABZSi-EZlcTtSR0ge-o5UhQiUH4vTFpWyENHkpS-7EeMq2zwYsfY-qo9kWJC4qCw0umRrn3_vXUJpf0-497XZOCUM8Z2np9kbli9XSDO05nLMJYSA_pXbRUTUdEZcluP0oUJz428oJkRzS6I-UjJh22SmQmxCDDIyhbv9ZRvL4YkUx2kKqoJ1u_JMLIo62TX19T2TNPvEAmvhgi3DJc2UjCBRerbKI8lUmXrkJFH-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt9tw03ObZGd9moy8wBMvBI_9heHMNfqVlYj2I00UVHeTcMP2DjOktj8F7y7q4Up2B9NK80n9Wdzw1NkYlxrVIbZTJMC5F3DOjHLI4YR2LABqRX6v3kZVG6QY7lFKdgFSVQKSZGtXeMHz_SkFCtsrt9or5Kp4DdSudp8sgqqFE73CDNuFLtGw-4VaH0k8Dhk2F44AsPd69WeCRgZfGgLdJ11k7_SD7pclikhjwReWK7sWve7GC0N2aekBlL6ORusknu4AEddMak_PYoCOkROQPfJ_Zt3pIA4lzKmS3xDSp9BpJ7wivuZpdFrieq6oXP9AGPglq0JNrMzp3bbNgmawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK-qkphGXyGirMfymb2EIvUU3KHqGya0-sVvbt4Rl39gFxsEe4jEIEpXSrrCQVbgq49ZbeI1qEyMyDNKsr56mC3Qwe6zrPZEl_lDrYOBij2pRgEDeUB_NPHQ929J2_SKoiRTPTyqSG41uEj4qQOlHVioGtHB8IR3VJBrRjzbXO71Jjj8JIX_vQn_oTFl23faQMXfoTzLWlDuPM90uIt2DZk_veyoe5ZwjsjuMUZS24CEudSHTf4nz2avFXKnxuZgYzsBXZL5kWVLm1r8MmHDoav0TKtBfInO73VM6N3mjvatJ_8vAx1nO8xwXCA1Kudu9guCmM857pmF4MegY7dwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2xgKBd5nLr76I3doTZWcPJsDMbVC5gxzuUsmCaUpM8Uv4WmJk5ZfNKit270MSP4mcXf6zEXiEa03i1b3gYbAd0GpEtA0vdN5Rqu-PuiOfwnt8zgIN4ynlV-ra1tLdwfqjMbx8NOKf0rfnk417OrEidLp3NtDCEDRCJ_k-BCE47w2321UKbvB89C7HEbKmcRPKxzT16mTKOqmMJTOGlqEWcsyBIVuarl9lcv0TqzB0r_iR15kdj2TOuUpraPP1cjsS0ARcQYBR4tvyyAKyGMGzGp5iQwUJwACQznpWd9miEZJrXx4_Qr8e69eF8gqmR6H6dibHemL3lfFWG0PjGtTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7WZmXsoxJzNNd0Ml4nVO7I16gSZgwNM_NZwTiucry421XTTsy2Bt2id5AAn9jox1rwzGuR2PG47KNVUdjluZgQKTDHYVtcqzTY6ZZZcnDvxk0QeMzyj7RMZdy4CzA3iqWiSTKwiNxjYp7ObsWR6Ti0KZPgfEFxRAfwJCrWLowBP6FzlXWcljMGG5YLvxOC0d15PigMeeAXKVHt-6sdVye3wj7fEusuZ27DVQK4pfmCDrgs0omaNEwJH3SahoOc9uZ62SdcIxLcJ_IUhvZ1ktv_C9HZQUjd_xusxnsltGHpQ_2Cml8tn36NCxLejcRZszXBkqhXJaO9paYFu8zgk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI3dVdUHaE-FByZjADnXE0UtvFh3S4LyAbjrMOqtFIN18Qagsw0MVYd2Wxl6ZEwKXedBIoDICX_Bk810g_XGrIucrgFI7XUc_gqufPsdjxTuhIFnQF50UJ8MecpUVON8kEnKkg8vfhNgsCgtIfe7o5wjYCKyrtR0DnaA0aRqLcvpN0R1vJSgL_Jzx31mnehYGULnX4jcvctXX5vdFoizMAEOJ7y1n0TObbiUEacbCEkwu351f_OgNi14mFnO1EjDipr3C5Po98Mp87RKS9dR_GXWFO-ycZV__j1Rx1sLaOSxCp1-3CtJlF0zXU-UHu6sOQLBfncHvR12yu2vfFMYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plCTSMzAmP85eJYuNN-NCx4bJtwcKOmnV2fqraOgj3ED8LnfFxLjWlsyS4QauHd2ojR1e3miFXxoRdxf2VSrnTqM4seYp6kYMlmkgL3OwADADYhHxPc2Gi8VQ2P9VHNeLKXs1XOXficBm69DWD4bH6kwWtM-e9aK8bpV2oDAZ7sGuu7m15tNt4_7_wVt2jxMV9LrAIV-bNpGCCssH0dQey9h8Y-45jsI8OxIwIZs1uslkE1_1EJhN3EBzb4-4ENaNFTJAYDwrmtQSIFEpcGP1zH2BCNpoDNsSSWM6RAZXzckzhZNrdUvPKl4VJkos-RJEiXNbAT_DWixmGT8zsQIew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppGK4vIg0F4bFw_T5QlsV3Aq5KMskSX3qkvSOcMnabibyvKR8Ntm2P7MkYzGI--L5E1bgE1sjjrPegJnDCyzAoLZGxCdW3BKmq-rhl8SiUMh_K7iKjYWqLMQHRwnHXUPkxtI22Ho1poRrmnhq8NAIpJH6dEQ33kYuBsNZgt78pu4Jm6aEAFQC3Zw_j9bUN0MOnRO-cAclP_dzoluQCn5pdDh92WlT9eefpAJ4xlBjTvZ2J0CVKK_S3ltVxTJLPilrZb5k7D9owya2evdbDCxb_Zy27B8hi1y5d3UN_jx94tnDzRF4dgsKlkrXp12kXLdw0h72aNnLOzIq-xcz0ybaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgHA3aqmt9UBnQyvC2U5rqVlJ016kGw6Hw38e8ovz7SNg-ka7mVKOtsxqSl97LDND4J4R2kq5Edpb8qE_ITslW0vk4F8HPNFRlqIMSTKcMAf-t7nUyp0QHaP2-E-6w_FYHsWZAdz7bL_tibdafWeRy1ctJWGEYQwP8ajHCNbH-1Pao0nhXAc_mmlJaOG8qWlpqJjZXPgyVkHD_iBd7efMvRneN9dBUEueVAZT9GgVIFZ1hTcpCmotijP0y8zCvGNxFpnwWptbrY5-f3yp_AYkyGl5ZZbCA8F9wRmrLlGFL-AEX8kQACADDFV4ZOKZwwbqjpNfIREie1EnbL2KYubIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP3GqzwUscMlL68Yg0rQA4kP-Leaa2lgytaQnx0tKtEhhLBfDlM88KYllXEX5H8Uf92POPjgoR0NfjGWUobYZcr_k31mclL0hMCJqdfxduZarhUQrQIH2-_AyR-ruO-r5K4BOTBgxJE-wf6FbhfxgXGXfZQ3t1dXGcCaiyRKKenslcQeF7wPlFi_LcWpuz69w2kWk-h3cNcJxHVtvr_XaWX02x2OJXD9BAcbHADx-213hIs7MeFRFxyHUPvyK3-S28qsXWHsowopblUVGZQA5vfesWrphWZ1VbP_jMBbn3vacaIM-8QLpqBu43P3AHH9FRAvsU8h6U4-yhVpdp1BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHTHxwoeBSyUl1eqHQ6RRjjtmBwLCuf5YKMo_SDnVVv0b-BmQzK5koSE6Ts0KqA6trz7E9pVUZ6eh9tS_eyKYU7zkrWHpnKjdr-lMiTC5Kd3nrql2GDqj5vTGMUB0hxNYJ9mOO24r5a30qBrCEognTMD4M8C0sd58S6GMHNJru8CKBXiE-hzr80tsffGFf7opMW-t2Wtm0IEWxmEfbp2CefdyhrF3wtMrVTy-gS0Qam-kRWl3uSMByrouB5ubETKoL5xfGVikiVlgU1NPhYURj7bL2_orvV4LbmXlOZnY8hMnjcPCLFlSmfUKbC0bP6hixBYNk86Nd5Dv1o4oT0HvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ_dr2fDqpEMgDs8V1I41on3wtARTM-iZArhT611eHnf8l0mcJyGdNnFYUlgXrB8CYySeooOHAP5xV4SNgTjW5OM4dg6rBGgLyozD4ayaS3quye4YFlSvM9FN5pxUH910NQ2hjsRWhsHaCIr6BLk-RFePIOYjAbMkudaMcbd4n0mYcaYjEVTKW5Mqb_75A6jfrtwQGs4aSBJLz5QsXMg9F7ZV5wvPZP5N93vMwUMAUv6vkFgTyo8EZO5Cu3c-Uz_Au5R84hy0rJdqfuTXBeuLXOQBu4gLzAgt_BhODDnJUZPdqswPgQ-eCqICt8OCnuf0tGauLbwfS2MK0xl8OtXhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOWPlpV1LR-pQBwJOWVlfQC2CEHBt6tR5sDMJUlGr-qKVzluB54UWjaq_ndwPsoqLngOtlUlo25j7LsMg8qHZ-_PEz7ANS8SDqLmT-5oDJnNLGzQq6VAwleFWTWjFeH6HbnV65NshQ4gyHON_yg_ASBz2JhMuF0qLYe2E6nfB0Byuy2fkj69A0sUuccDCQ0OOqQ6294K54btqZAuRlDe-NeE1taMIOhqzPuoZPZ63UTk0BuqcXpp-pZ0AbyfSgipGxX9OVZHnEpVzBtjyy8Gc1I6v1DoFgU9tevIbHD8FxHKRBghtzYisbihZVdc26NLH3Gwgmsm6mkxCaIlXNn_-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=e2_beF_HlUGwl8wm78XRpXwDo1JomPl4YT41_QPUsdvo_awyALrbWgHBAhHoETJLtWYwV5ah2S_BbdRytvPprilDXxHBC31v3fFTmPAB87TADn_OpC8CEDggHtOL6YBVy7LRiQPyH3H-miac1DoEyrkXP5hj2bbSP65tEhkC6pa1EbECmwvEW-Qf9gqTjRx6_4u5M8nnI1OqZCDjAQjBtLp9p3gv0JJC3kP5IH8uiq_rXmv_sDz6SrEfFMryAobMeddRlDGKmb4VgjWB0dXS7PoBWQ3lujuBYnhTo47vNg3HEpYKgNSUIM9PErGdjBznhTACHniU7VCb840bcbg_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=e2_beF_HlUGwl8wm78XRpXwDo1JomPl4YT41_QPUsdvo_awyALrbWgHBAhHoETJLtWYwV5ah2S_BbdRytvPprilDXxHBC31v3fFTmPAB87TADn_OpC8CEDggHtOL6YBVy7LRiQPyH3H-miac1DoEyrkXP5hj2bbSP65tEhkC6pa1EbECmwvEW-Qf9gqTjRx6_4u5M8nnI1OqZCDjAQjBtLp9p3gv0JJC3kP5IH8uiq_rXmv_sDz6SrEfFMryAobMeddRlDGKmb4VgjWB0dXS7PoBWQ3lujuBYnhTo47vNg3HEpYKgNSUIM9PErGdjBznhTACHniU7VCb840bcbg_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWBjar101OWMEseRMuSUCMQ9bhMhPZ1Y69G0uHjW0o2BlIT_lJdQNw4jbseQRzKq1U8MQ_khH77ACoQXDJa8a183A0kxdhTZm2xF0PUTBz2sn8LVc1r8lKzRNCroFvyM8S-4rP_KkbHu2WU3fthxrIu8xhQJaJ0n55KRctf8_IbQwnh0lkkxW2VvEOAlN2SEMAnIPBrNDK2NJsBFHLeOFcs0zwJ20KMNLKxfQAXK7EdRi9QAymZOonKs0qfq3yV88BSjIccNu7zwVaYmT8OFf7d7MKRZTDorf2ofREouWZilXx-mgxN9r9VNu_8RqOE7hGQJAYxd3SykkreULyiTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXxgLvpn8EhzQnzUifydd7vxB3f7JNx-dT3S-aPMZlz_iJ8AK-cqtBdDRuLgOl5SD1GlACfFVllH7riGk1-2C7Fl5qNTw6YW6DUfkcuWeQxjFk3B7G0b--97_AhLfvtzfGNGq3InOyPND7mPJxPU0Od4F8ctldDDlTZK5s2SoBHgOlrAW3KJMKm1QRRyv4m4XsFki-NHHn8K1OWhHdovEOmnfkye8N9XefsC3tXcRWDyFSMWxxx9_rvRV-CpFodrK7Tr9gNWTFkfxGrplq25X6hiotGUZP9DlRsVpl2yzbnLoD28OAtZjzRejXOujexo4-5czZTrwTYTR4W8Z0bB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzmDbwz5QYHei4HI45dPm2h1h-W1GWicpd8DfLYubZnOiH6zxCkq9mqMhI9_bB_Bn5qLCKZqNpMdpwhYhnM-uOOoR_gmwJztG47-H8dOOnief4FqkAuw-U0ia0NAsV2PcIIvhlih90t3Ob9k0P3QU6L0LrnOiFccoQELc7PhjsrJJssAwLvAAlTgNoXJryWhOFgQOW1bqEl0DUQn3lmRAfVBhyia2oimU5ekVimACeO2uuJ3yAPA6K33QmvjZI1qUiQSJ5Cde5nsKrVMYnwUdguH2lL3-Exani-qvfgVQgh5pJDsG9s1LTbDp7ar0EX3NXYmUiHzWsJDzY0RoZ4peA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=D-hbtnN5OX49Vhuagbqkyd_aNABIYoMopfhajVIu6z7Pr6OEQTZyXbxGNz6P07HDXwl7CyKtRpeOAunbNB_LMAcgc8_2h8_esrYYaYh1LEcCWydZah20KKj7Yw_4D-sKRh3FyRale50UCHKHIqZie-JqDsMP74LQ_8T7SvF-i4wnVjgrS0R9wZ0eZTsX04yFJrLtAtYH7Ws2sfdl0_FElZRBXUYCx00O20Zf5hsgqGLck23aFGV6dRIDOrzu5hxodwcKXJwX482D9j4vBC1L5DWQU_MpUSvgXFCRn2orM_vDmhh5g3Pe7w7RBhmZY05lU_r683WfuOCg3HpW6059GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=D-hbtnN5OX49Vhuagbqkyd_aNABIYoMopfhajVIu6z7Pr6OEQTZyXbxGNz6P07HDXwl7CyKtRpeOAunbNB_LMAcgc8_2h8_esrYYaYh1LEcCWydZah20KKj7Yw_4D-sKRh3FyRale50UCHKHIqZie-JqDsMP74LQ_8T7SvF-i4wnVjgrS0R9wZ0eZTsX04yFJrLtAtYH7Ws2sfdl0_FElZRBXUYCx00O20Zf5hsgqGLck23aFGV6dRIDOrzu5hxodwcKXJwX482D9j4vBC1L5DWQU_MpUSvgXFCRn2orM_vDmhh5g3Pe7w7RBhmZY05lU_r683WfuOCg3HpW6059GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=GrKnAdBoe0NiT8PIyVql6e7XQ4fkVY57FZU-RC6c4Dj4fBwySu65A_H54_ZBW5fm2gY4AP833Oj42_P_10nPJ-WsbJtpYUrM2UDhN2rn5PpyBCt-yRGp0lc2yGQMA5KuP8MGbD8kXxz-NlI1zImWrsXpsCEp3_QSL1fhE0AEbTdGhiYVxFdoII1Zik8K1DxvyUbhgItxUO-NZRT_N7ZEhnoh_-Wshx6YshLDz_xxzbcDQZmvQ9V81ULF2irpNb-zyLTVvi4etXUu1WIoZfFRwKQw_PrJs5sCEQ8P2UCgwNpA0-igjeL95ukg7Zyb61J0hhkjgFnL5mTKeUkM0sfNaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=GrKnAdBoe0NiT8PIyVql6e7XQ4fkVY57FZU-RC6c4Dj4fBwySu65A_H54_ZBW5fm2gY4AP833Oj42_P_10nPJ-WsbJtpYUrM2UDhN2rn5PpyBCt-yRGp0lc2yGQMA5KuP8MGbD8kXxz-NlI1zImWrsXpsCEp3_QSL1fhE0AEbTdGhiYVxFdoII1Zik8K1DxvyUbhgItxUO-NZRT_N7ZEhnoh_-Wshx6YshLDz_xxzbcDQZmvQ9V81ULF2irpNb-zyLTVvi4etXUu1WIoZfFRwKQw_PrJs5sCEQ8P2UCgwNpA0-igjeL95ukg7Zyb61J0hhkjgFnL5mTKeUkM0sfNaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlwO-to6Mj1OC1WBp3DI6Y3ecOGUnPcoJw-DW9PZktkr5vGQyOuiUPPhdznwGiUq2d24t1rakceDHMVagQrdABmPfhfZEAW3lb7hvjIjIsOCtyQqXWGTac5mcFIiezBah5PR4gy7bIWGDX81raX65Cp82opuw875gJieb0DqZfL19p9AftZke1x3tM_fhF2P5pU38dO80sEAQV-q8ais9_cNsf4Mqsw2Q5xiKokiJrpr3Mk5jov9tKsaTQZSA4ukHOUgqVXqXkkzQ0qk1j9IDqMQ2gpSj5yk8-Rmm6b8NPPmWzVvet5eqtTIYrOoKpVLO3TMfXG1Efse0Uff8tiKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5grHqwxh_ELNRgJ4F2zQNgmT9XVV8wgZQ-_yKE3Aq3b5Bl1um41lPhFpIwNHkajuvNi5WoDuMuPOgen0tqMzjXtwUuxSCr1d5yH90AUkF7nEqEKAT_t0QHPxBPCvHdGamqBjAcoZqOv2qUpkKjdx5qbjN5sDsUaZm6pENrXPuHqpeQOVDgRg7WluORVhZQ2tbmTp6zmGq-GCMjiU1iDRmiHs5izn-XK9FGUTGUvc2IOkV2gQQEBdr4y80YjO7mcbDV8AD76-DdTJqMeyJ7SIiUMBvy6Z8VUxg_zPrwc0B-hYnhkGA_ZjoUBAfzomAfxRZPnaSwuNJNPtG5U4yHPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egG1kyj4w7PnL6ASkaQYf-umUfJPx3LUq8SOX29tjk3_uYCY4weh7TDYbdjV2vCtZxx38VbVLH_T2WYKOHr19nOzVk6QsCxzShd9n86_6aDpSfLtR1bOECLHWjvOyrl-qSSLEtQP6hKaoQP_iv4uT805egTJLgNaCRe4C7ocwBpBL0SRbzAw-iKZ6wZlF4KK7fqSuOVrpOXa6tUX4fAugHcdcfPRsehdF5cHw_fjWh7Te_dPDHar4c3kD5cjitS1eqpHyw-ayiiKaZ6PDpBjG7Z68DiUEAgDpgzMJmqRfAFPNgTpC62XAhIsV6Rs2s-yzg1n0AA8-yf4yrVAmjuKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKa8A8c-n4hvA-CsefM6WyxG0_eAaoMWcKpwpSg0iXFLGUnTnqO1QMB0fn8cMn7zHkg5Y9YZoETQxv-nmKVQp1eiNh76-PPwnO7hSIhxOLqErOo77k7bKM2G8R1MmyoOBvpvPNwMXnQN-vOJ0TcvmNOXz-dX3S6NrJZxPQCv5IRDMCrvewh_rTlepayCCX8Bistkp2HTTLDq1RT78Ot53TFSmjfLw50h0GKT8EWc77pWn3L1AoTHJslnLsEqnF-FNg1R553pnHv8uX4lNdlgVVmKpxIur4XzTlqMdByC0ZDVFzGCrrhI5om_RQO_uYGfunoTLrohkxIBNmhX_uI4Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9umKXrLG3f1dsaiI5aWBekVPsVH10sYPsjHw5nzOjGJ63-SWLg7WcnXbT--ExNLjSTx_GrAMf_1TpS1nuZPfcFobPY-3VQkbe3Y5N3QsY5AnbxHmLaNl9m--Uaz-ntYyLIA8mVA0yu3b_Qhh0UVcp9aSS2mWmbHseT2aFpe0A9jGqqo4_Ro8VWwT9aJux4gCk_2QDqx0G-qgwYo6uX0TKAAHjiExJ3GZdGwNFNJD2rnApROsGOdqimfkqncjMRRZYJyC6o8xVYNJXKwav853qUQMelwDO0zKd4BxTdg7ySC4CcJ9dHHuklSod_skyfjiwKeP5JgaZ0O8kgflcEmRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdotSL-2MD-ALLEBKiysKy5ocRTP525IirObVpJCmjoPDSD-TyTx1_g-jKb4Qw5_yG4o4ooXMFR809-rF939aljzCmTUmKQdnuCh9sUOK697A1ebnT67Q9UCwxTEmusNvvQLvmsHxN6qoPHoyBD2_EieOAleC-Vxyv4KEJ0YWa7MfnfjZj0n5JOMRw4QiAyc9sKh65b9Al4uvrfUrpeeWkdnyFgsrd9mzzbcFhHMpsqxPHku3dyqWy2B1uOUChc2MbbLj-2iY_Nz4XNBZPm2MXN9P5VTW3xX3JytUUhXu6k4Es89iNXrvZXP4EudeHNtWGv0ml6uTDr66qciGf7OcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jogi1NTD24TC7oMUTF5OTbbgCZBIrO1qUY_nMGdilZ9kFdhkuu0Vke9Iu2Sx60gojjQV0v51H363T6ULRYedtD4lbFE0OVA7T_TZdMQpu6G1O2iSAnMjNGfrqywyZHq1iAsmr9L01QjwltrNHzeNHaLMWMokC_YoCRE2GV-96SuEIexuk2gzFqUWT6sieoNEloMn7vK2owP5zQF-OWLO5f_6i-M88-MCD5Cyhz07QmG1K0EB9mqoOp1ntEgI9_izvyVJzHf2yPaM5gXdam9JtTNnzQOh4sW7xC64KqdX8AXXi3jTRsXHEFZXm26NOWdwkPhCx_N3wpU1tzdqAAOhaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADnc_zfC7Q9BnI2bmp0OGsenkfGWajZgX8NI0OnN_JqEY6XC8QqJgBcik7YuNf4ioCOExTACMiDO4gcfCxjqBiYI7e_s0c9o6W87hJ7h7kE9SvKvR1YweXVvqQm1qvR4Zss7eFVYz_AUspHV4Q1fjzto-9FGGWlkuwvK6ERnRNVVy9r2jYYbNHBol5yK20SIVfbvkz5VWPgGMOckYIYOOrA94lKqGN31ESpta66FkrRM67uvXrAv5pV1Sjl43dutOAnL3tU7oRbWIH6eSrzmFPSXIEChJUqKzfNFFAlfn2pwM8fs7ogRDD4_wSnx6SgELdZJlwwwa1CGcohY9ofwdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v30s6N42IWIvk64zlQN_cFDtjJ8BWUESMsO5JtSLUg7e6f4fGdGWySQC-XvvA6kUBqQWnWvWJMQuhnerl8qeGbxZiOhpd_wKSAqMSyMqv6GclmIyKBDpNLbaErL4PR-xO5wNdyTp_xnuEWYimgrUtIowZQ47mqOkli-NkZCS6CpFh3qpj4wynTlpkZbjR2SufKCoxlmFBwqDNil5GzZaixGc-jC-3IjBiKG4Q0xxA6BpxhDJcskwfylb9on7tS3CzQJndkKojvo_9-TVRkX_Dbf4ZmG01j2NMGBOIGdpfdPsk9AIn_O8CpMohEw-0mBeWWSeCzW_GcTuoPk38K_hkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doJzAs9lF4QT6L4yqPjyzFjrzY7jSjEdPAd8j7HvDr_zCLrseHiIxPh0d7GqUHTjVSBagEO5ZmLUd7yXqOxCva2VVH1_Vt4iL_mUMucRsYHnt1fuDolXgfZRiuc0wnvFX2Rk_STu4mjmiU171yRq85tAFGLzgGRElnCVwwDLALhpqybMex399RruUZ6iBkIRAH4QdTR3gnDfBu9x8XWBm2XU_dJFc50tGN6Nb_RhiIBik7b54bj38mkO3NzmZYATr80IEqR0QW8e-j-v7SGTyRq_dvByhnmSDyKM2IVB-PE6XP1cAm1JbRo37VoDMbl3Onq8kuKP65bqRRQ3G19Ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqtpivC9shhskyUHPCVl4h9s9meW5bdw-ts8SMSAfmXjBz9T0kDAQVXzOsPHYnmC_pVyiajTR_s9IQFnoBhTdDdoIdJH5_CVOMNa-JSZsaLDZYuc89Rv1OujKwJX6epowoqcPmgj5FKyVY3KsxmAZOclaxozv55PByluhjbc0UHYUj7m3g8Vae26VhBdiqC7R2_5apHvaBzM-04bTzXVhPlGDEmKF4mNHgkxcDF3ChJAZP05mrMZd9OPcvDTF0Jf0NNkDdHtPmke651I44zVJeCW9VsNMc7XQ6pB2UCkTDk0VMpTrbnGkGyz00InwPcv3udlSFy07k-TY6lNgdOIOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV39td9tqHhndPpZHl0WIKlD_fYglt2D-zqCTdCefVVspNr0YPwYEtKKwsmCFPyJV7znqT8h8KxeFk21Us9WOpE1IZGEfZp0wtVY_s6yni8jjp6vtwEvVh3H4CNpea2d_a8K_-D7xuOuf-5JLL_6kYMKVVzT4_lMatbMvl3H1Ln-k7CSBafJeTTA8TbXibjOt3kGc1HNIG4_-xpkwPTxQEHhlGQLMMMn86PHx1KOD7ZTrh8uhYlwpOSIW0lLulVr8Cuo9yn6j_mf5By6qdlGSttNXYgXWSVbkMjprAG143UeGBAzo082TiMbZv3QQBrijSswp3jBlyjfMhlcCs7k3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOZYXWQyUHAWRyuSBEswAbYL7f8c8L9ud1B7ErIY3b8VBDiDQSDxH7bDwstHxAhUE2HTMfqSreUiHhkzFCEkTQ_1vRLrucfIVjDUiamNsYvuO_pMvBpW1_Nlpn_G1WaBTNJE8ntc-yeZ0ZjuIVQMB-Vm-AibZTpaxA1uDWnXOie0KrqXKmdDkxYc5VZCVNs3yWWOhi0nj-7tbINPI8vAYBHNds-XK4ZLx8U8Xh4l6_GbuCRclrIWyIH-dqIEmJFz6t75D_Vccb_e-Lckgdktl8VOdG8bkpzCthYUf-QqXhy3kCZ43b1CXGTFENhQObuY8GN8jh8l4Vxx887qj8Z_Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6X1wYpGdBNpLc-lKZDmqVVXNgGIFaSPhOkfRUYF79iFxNCyqZrZBBx78DDNcveWHi5ztsNK91HqyF7m-a-WpPNJ_NWa80SDXjEMldzrM_9d1hxmJP-l_WB9tPQxIluTfU2a7UQ58Lv_YiAZ0q8xRIjCvhsF8jJc_Ychd-_nV5QGAla9Tdq9GD9I3zrbx3YzsZb15GgYt7g4LMVJl21h3pxmDUpJWYGp7_gamJYar55f8s-DZYoJ3oxiL26GG4GbZT7NsyRtEfaMkfA5fEMUyNoqZrn10yQuW1lKo_SGnWwth9-bTi0irtFvsdvrYq6ubOn7E3Owtu1VnEwml03YpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=CPtoUubWgEgWAHnbfZxVCgFxqo0kZiuqzbElX-UqCc-k-ng7-vbuctBf5KVcIgHoHs2HCz3wZuR7oTyNNSNWY57au2dhflA8lPR51tITtulMw4jtZHR93CX2AyMvv6T3uZDy2kLP2qfzIF_WrmHc-6rvC64wZMnZd-WddtPpF2jwgg3m655J4mKEVwPt9ZdhQaEARLWEYfNKfJXsFsz5Ki30EU4-kCrIaJUla0Ho-9YUwh6TUe5PgqpjYQRK3KYZVEvVP1uShvrrGjYJUCqIR8CULSVPobLeZOzBoeh1YDwYVURudm6n2mojGXVDbf_GNwrc8iKatGDAwedN5xKRHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=CPtoUubWgEgWAHnbfZxVCgFxqo0kZiuqzbElX-UqCc-k-ng7-vbuctBf5KVcIgHoHs2HCz3wZuR7oTyNNSNWY57au2dhflA8lPR51tITtulMw4jtZHR93CX2AyMvv6T3uZDy2kLP2qfzIF_WrmHc-6rvC64wZMnZd-WddtPpF2jwgg3m655J4mKEVwPt9ZdhQaEARLWEYfNKfJXsFsz5Ki30EU4-kCrIaJUla0Ho-9YUwh6TUe5PgqpjYQRK3KYZVEvVP1uShvrrGjYJUCqIR8CULSVPobLeZOzBoeh1YDwYVURudm6n2mojGXVDbf_GNwrc8iKatGDAwedN5xKRHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCMKLVuAD43vUSZXzqrnBD38xhJBI4znS0TmcbuH7hfBzal4GR6zk7ealelMYChsmRZ81O375ALZOvuSXFD7NgEEdW_UfXtCNArZGmvJT5lpbaHqtAeYDZeaiPJlRbOrQ82LHeyyx1HZwUMtCElVTKKP9C7a2tmYjQkQVeeFjGz-7FNnAxNmj0tV98uxvoUldtJkzGf7p7oN27ffu8rFjqGopU3dr8NyJq1a04rc_vtUDQVl2gdlArE-mu6k_aS7x7JPJqfxIAvD1sEQoKAyY_1zIZ-zhbayBsWYTmZs3kCaLOTCT-5_10QjVEgKI629KzCOHLXPFiuVbYtDpKbfng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiuEDeHbrJ5pw5O_EmBoL8kp8bFXNEdMKuAHyqZ6SXqYW79SQN9nV7HMDsjQ5CCmVnRyUp4PpGt_gqEgD3LjfJxKHNenn0rA6C3q3Lh64O5H9h1fryHWpg6MeH1hTP5no7l1SZ7PwaP9TLnX16nRDo-CObII1T8RkffY2HkR7hFxYXNjc9s0syHsWEKq4yLF39DfELoyE708N1GOThma-GNEwxavXWkORx6_I2d01f2q1dyCnLOrgWNvy2CL-AIdmecDzrOZsJB9-ZasBOZ2CWkf100DQKXS98Vjq7UZ5MmjVqkArtPrhx2WutQWfbqtnLhTLm-TVxgO2hsCw7htGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FysBppDn8sJHGSepPcZsmHapfHbjiWpFRcDYUu0NnPXiKyBzaOBwbwbzZ0vssVzqvMW51U8JTngIK_aTDl34gAeowl3ybldG0gHymQiV3RpeHiYVCa-tvG1OYqHd86pv3yxbGwK-dFHHJLF9df5b-kCMGFap8ObiGJyDX_0Gyz632LdBWToDVDwr1pAinGo2mIgRzti8u3If74-_EVD50RPOZc7I9rLUYIbOX8Ps4EFXdmmAid4d6xGmsl5Jh1mjSmbduJV28MdrkYrnNTxYhY6mZXkpA2DzPWHBrFhQw7LBe1_9q-lDbwwYAOVlu1qqQ9Ihx4wUlRaMXXQtMluCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-bmdwrS0OYi3sB6Vj3tlBjvSwdJLnXc0e7c_jEIXMqrtKDYIg5VOX5jffef3lUHb5GPWB6bwdwm74lVDPrPM4UzgOjyaTUnTAliVUbug27EAYol17R0zhDMuLi6guxDxiukRwRnrog2FWiKtM-gYoGSCyO70t5nsKbob6as3oaXXaDWhUdIskA2o2cSPWLzML7ii1ZlG9DAPHwPhrzhmoKVZUP6ILcvoA8CFxA7ffOkwabMYdqGdCRcLP5UyXpfrPiqLwjmq_nplQMY_yKllI4KVXCUMoiL-TcojHIGchDJmQKLEIEY0AqfQtSoSm704AFbmDynbC38vT3RD9chww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbcRf3h44JPeSeTYso9gdimZAhZ77Sdvp1NfycPCwI5YXMe92MqVOBr8tMHD-8J8AoHiZZYSVpKG4m8_g-u3mDWNJF2steTqYRJte7M66__RS-u8VdP_cPOsQi5POvIdB7VGiAy3j_QrlPSCdtEPK_-TJewvY8AwC72Z6AF-GSR0dTBjkbeD4s8kkfi5Vo9suh1aYsupFeow5YHo_WJhYBt1T9-EHoWhiXJ01jpBnhTbZDBteNPnIHiZPSLHk0CHmz7YP0sX8DFCM24YVqtU_LR3PMY40EyaKbQqFvTcq6NL0M6lV9Qfo3C2o4nkQEGqTNsEIl5Ssbo6GNvH4AYBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZL54u99cW9jy4KMmmogwTNzO0x6rWrTqkCsua4CZ55GsPH2U0air7On-RNcjnQPl0ctCwWx46ng0KlrqY5DutyoXRok7jlyXCKrhGgm7WXcvFIaS_wNV2xDK7Z-qlO9mZpoNnL4eGpeBH7WFVEeOEPykL2YfJh8BvA6x2cfm_nDCZlGYeLhvjdwM2fUSt7-Xs36iiXNgu9piiDHnDit8ow5PNCAqrsCSvyqEM9KmtxjJHcqLtpMH9XokcPUUk4p2WHDXjeXcKv_UfObiiDyD3TkJGxV5IqsLFzm7mA00sYat93OMF9KlAFgEwu4wYX0_twaFTo2KPyDPEd-vE_bwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6Hum_To1QN0GYwL6z2TGD7M-s4PjxsbNiQ7H-ASO8fZm0gFTKn-80HRzFR1WGjykuCjPEoWmmHJdWtdvrSEVibi7Xj7mqMTc1Wg2Lw6fv-KQuB8tekmxti8ACrBAsV_5Qgs6R43yvn1X4yKzkr6jNUhzl23d2aTZBn1yMyu7rIBMmoe2yuE9Y_-lrYbCA8EH2DwVaUqO_WnLswU5-e6S8XPWMn8s6pGb897CFqFb6ZA3FIYFoWLVwySfbB-hHUZVOt8Mqe7hrgjrHcwEBd1Iw4AJ5-BzxQUEhfBBHHb3OYBDEgkUUm5_fp4F4fV9OAS3urqumRZi48QZXOSmbkAGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QI2sfycFCrAyzuGrYCdHf3J1xEiFSdZ2E3tL59adBG9p3K_WDNBnRWkwRG3mLaRZBCf9BAonCmC19N0LS5eyUlIIqDt5Cei7QCXhGp42UM6qHP6ommpbpbkp-HhFopFDitXDrognkDiYyQeVxtBqkyAgDzoYY8wXZemqKHOLgaVIYRftFP-XPT8TAFsg2kNZ4TlHqkwLSMAkPBBqDa__jMdQOKs1edNsyTG2f1vYabWadWluEsixSdYKN56okQYmm6Qul0d1ny4Ozzm70aA8dN73KQLzC2fwJb04JFnDVarVHDO7kznbbT1sipttpilud73J-6cGRfz9-6qy8J6sBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=gSyTXvpGcmyNLqxSRldBekLpQqOCp1ki7DYyc2lA91FeicBxObDA0rjscoA26wOoTnq-WOS193vc72ZYd6CawU6UG1-jjfgFVCb08vqMy5r0fdf42NCE7rAcQTYS6kKNTo71Mm7cI-vtxhxA73wYGksNADsU1Er7EUVBhpsoxdMdlMsaP3273Jt8-4Cd71zUfCGaFDhezPIUv9g0TUBRk5lHqReGarbvq7UAeCQelXTtebpnLo3ou1plYk3OXKPmzCp1p-vv7M1Q4YcWFfJow9Dp6XEe6JuTSD_gZQJHojVS6GY4Lt-LUhg7JTB_siDdvCJf4t_2o9MkycADGJhDUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=gSyTXvpGcmyNLqxSRldBekLpQqOCp1ki7DYyc2lA91FeicBxObDA0rjscoA26wOoTnq-WOS193vc72ZYd6CawU6UG1-jjfgFVCb08vqMy5r0fdf42NCE7rAcQTYS6kKNTo71Mm7cI-vtxhxA73wYGksNADsU1Er7EUVBhpsoxdMdlMsaP3273Jt8-4Cd71zUfCGaFDhezPIUv9g0TUBRk5lHqReGarbvq7UAeCQelXTtebpnLo3ou1plYk3OXKPmzCp1p-vv7M1Q4YcWFfJow9Dp6XEe6JuTSD_gZQJHojVS6GY4Lt-LUhg7JTB_siDdvCJf4t_2o9MkycADGJhDUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmC9Kk5xgaS4NPd3N3iiiEBExlGUT7eZKd1rfp-wvFJvIPhsgshLbswcPyOGVY64vYlNsbCbFhXmHXcCk0kgIrbwISJ7Vc4PKN9iJY_m08j4lH2bup7ALBnsPIVsu7-ue_MeOIXPHsw5OdHdGEv7BhdZzzMRa5Xpem51SOzrocdw3bh3OaFU5sc62rEuuqUE-T2JZeqo1LkH5e7QTaOhuKu4dRaubomF0a31d9CQYB57jIp2Nufq04gBgReoKWrWUuCz-p7FApSIiPv5r96VJbh4_ipp2uZlOQhbhzagUVmyueiBDkC40xCfxG9NijGz0tEsjJaopblDxkElKBRm7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHKQfTYMp3PuarLX6si-gl8O3Bl3trJYmK_AcDdOMdyi3U5wzzCuSncl7x9YjP6KNDxbOvnt-kuNdPcriEMYVtjcrlF-Omxdzg10qm25qQ6XM5WMLSrKvzW6Es0zbsMkOAR8uZjVQkR6tTNO7LWSb3koYUw-9oc4LuXZ5TDwZJKyRVb-gYo7KyzPyeq1IJ2QbzYZNuATJLG-P_qvFqK5A5CRtoA7HCgQQPQxfWrIMv6AhpD2t8OpRT--KsBuMcCniFh8yOVR9dxKwPriWkPMs00xHwQbnH8Y0SJNB-1lR27NDAxvHubbRn6ciKL0vYvgJ95dG4WbUiFuhJyU1tmJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLgEviUjzuworZL-jraj2iJfuby-08SHOrkgru1SHBwS3hNdButbfmmRAxKNBulbLpUipiY9VQKM7illrQ95k7BHqydbGkW33n7i7OOvtXLdPKfoPXrLnXCqX7VphPRjWyi7PokzFXAwwhYtRrBWnn4MM119BwfbYvcIHqcNAm-EU3NZUw-b809eYmbPZ9-XX_r9Z1D7cTjeMORYc57Q6BAPQlvNbXDW1DsSdX1UL8gLJHRqlwgrW9pRMIUU_YdI_aAsXL5wSWZUmlP87CZC5K3GNpHYlueZ_1ptUEcoWamlvBU6z1sUCG6MSggXK0jnQfkkyj7KxQRmuMqq8lw-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOqBVv60nm12rviCC7vud5Xmg_7L0EFaappZfJm4db-g0zTG5QB2CRXj-kMBVf4OMdIKysWK-bsZwpqFL7MbPLjiRBAZ3kMMs4K_nTsvsJZbAFc12weIfurjnuIuKy-rMGy7CdKPiES0mHlROjAeRPIVH8k7qZ5AWiZDrNtCmoDy5jloewJ5D-Hsm3c_NnQNwGBZ3kpn2j8rBFZZwWEl3qIOgJW57CfEl-QtQKsBZDnIj8-dqRx5kthKSZCXWaZwAL4caFM6J4jxJjRJjO7DlcJ2R55Wva3P5AfsrgAEl8zzwe8DnCTY2EkVIRrOvWeDfOxWRrIp_2NX7D2Hj1KcxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4a64R4AHbMP2x6OQ8R3Mtockh3IINeV2zmMUJWGN2WcgbVbCYnQmNl6gbwJVTFM9dIdvqiOshfuxQQbYQ-09is0VRDrJpSrJzHDFGTTa6B6AesIwNn2ZbPU2IAK8yEJl-gtdWf_v-BHasboVKraPSa4AL_5eF2kAXJ1LpjJq99dkflxTxM9dqeXF_gMIu4wAHx1VjR9fsbf4cuy-rQJDt9mPBgED4JKYwGNsbXA5OlhUWOd4eurt5XouKJk6GJqXIWcbhRH-4j0J7D2RQMyRYJZh_bqLDQ2YjOfiD98gN6mdkmA08WYSiYRfGYkiTAQC7Hpxul9dF0uL8gu8dsehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXeJIi5tp1QXl8ym3YsXFsFcHG8orCqCMyFYcqFTLt8XEer1XAr03JRWus8PWy616QLRA3p2Bkv0g6BKVcKRzqKp6ehj2uB-DEyoRhLzY2NluJio8BoJaybQ8CfCjMQipm_K90GcpLT8qADrIZIQdpIyPw4Cb_WnJRcmrxk_DVF79ohp7YS1hpRy6eM7jzIfnEQ4GoMUQ8JC4H-jzP7H1Hh2ZiX4RBymK-b_IMBwwxRSWDVGeDk7Nc4i1UTIMipel_zCt8rOqQs9ZmZqk8uaCi9mkfBy9u_WdDwkOKTEdYu5qJ9go48c1-4h7I0U3311Ybtui5_c-Ql-TeGMMXLfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2CztOhrHAUf6QP_iFu2GG1HZnzArAODoa-oy0DwQwmeFAHNFcqaYwNhcy9FPAy1YWahp_JvhIFd4eHFIZHQpVy-QQWfAPdXHJOioTQmGDOigQB_ngYVdKPh8sfxXR3_wt9Mga_nMdFCo7d1s4-gftjQJsy-TiOK7LB0inlyfcns8LZO2lg3yjk3lam-VKML1qA4KszLCwB1PtbcptoqzrGZIGt-pxqsFRATBWmKgFff-47prERvLRU4H0no3nbJoJIz6jmiQbi2xiaH8JHTrXKAaost4u3AgdHv-cisCvq6OxulXHuTBtBQG9TexaRGBkg0rBvzLXaCgrseTjkVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=gDJ5D0ke44tTrpmD2YGq7u4oO1pWseK5aZNGSpLrlVTvjPovP6LfxQttkbfRKHIqq5rGfZTBVT1INSg5pxEym30uyFOF6oFuFm_VjS-FGAmfZFy5DO1d_fkQ8b9bORPaNsBrYH0AU1ehDXCxp1NZE8EkgICuBXlh_CdC1NAK9dL-0UfI8ZSn-dPCAV2WhxXoT-BMGiz-knWnLHbWSswo8uilQNNjjvcAkwdvMHQxiEhGPCvziQxw30GJREinvazsHZwq5DTkZHK2teF2ofb4sNFmfiWiojvPnXeAfdJ2gLCkYCQO510QCGWbPHB7H31WRt_Mo4f6mOH1FJYCmLpXT5ep3-4JsBlPlpdT1lMAjxgxSbHx6LTCiHf-ZfitP5hq7YFblThafm1BIV0ys3yA-2lcdzG9bpmOx94jnyCYLCj1Y187a3807PIuJzV75iK-ZntEVFpiVvGIM5WNAfB1HXj4vdIho7CfrSrDDbAjfJO9sS3CNHyS7EpikYzx2lQwMnUW0mjyPseBfkRXdVVOdaeyZljmSgZbyfOSKzEuxz7Z_-2brK3hT9R2-DglTpharEXQYBa44165JvrzTUs1URgTVtNtmDcJKE017kmxxjYCYGwYmV9T2yISbwyYgGoCw9wgCGzgE19M5M_GvL4IugwILC_OmtTG0KI8K0ztUe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=gDJ5D0ke44tTrpmD2YGq7u4oO1pWseK5aZNGSpLrlVTvjPovP6LfxQttkbfRKHIqq5rGfZTBVT1INSg5pxEym30uyFOF6oFuFm_VjS-FGAmfZFy5DO1d_fkQ8b9bORPaNsBrYH0AU1ehDXCxp1NZE8EkgICuBXlh_CdC1NAK9dL-0UfI8ZSn-dPCAV2WhxXoT-BMGiz-knWnLHbWSswo8uilQNNjjvcAkwdvMHQxiEhGPCvziQxw30GJREinvazsHZwq5DTkZHK2teF2ofb4sNFmfiWiojvPnXeAfdJ2gLCkYCQO510QCGWbPHB7H31WRt_Mo4f6mOH1FJYCmLpXT5ep3-4JsBlPlpdT1lMAjxgxSbHx6LTCiHf-ZfitP5hq7YFblThafm1BIV0ys3yA-2lcdzG9bpmOx94jnyCYLCj1Y187a3807PIuJzV75iK-ZntEVFpiVvGIM5WNAfB1HXj4vdIho7CfrSrDDbAjfJO9sS3CNHyS7EpikYzx2lQwMnUW0mjyPseBfkRXdVVOdaeyZljmSgZbyfOSKzEuxz7Z_-2brK3hT9R2-DglTpharEXQYBa44165JvrzTUs1URgTVtNtmDcJKE017kmxxjYCYGwYmV9T2yISbwyYgGoCw9wgCGzgE19M5M_GvL4IugwILC_OmtTG0KI8K0ztUe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=DAioSTqzhVkQI9FzJSL1PrmqBUZ5yz-lR3aWsNVFS7oh3bERO6Qk_4C33IpEwEp52NpW7qdLg_9QzKfJ4780GuvijSY3oL0RgHLKSpWtSBwuHyA7mpDT6qX167N_yTWR_y6pPhAUsVm45_9K9h-m6wERKkgnQzEx2xUxs0wrUeW2gWuSQon5PDYh0FNQxcPPSaBSwgaBfT3HzR1Q2E6LXEzs2D0L9MNvtrWsd6a9sKzQ6sOcZQ5cNmkpZlLDB2MfdZhEOfOW2ai0KLRIV1pf1bAuQgZz-mW_mryK_dvqS0nNZxihAVkESdyK0JhSGKosxTAWL77Z6RP6ueTAOYmGWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=DAioSTqzhVkQI9FzJSL1PrmqBUZ5yz-lR3aWsNVFS7oh3bERO6Qk_4C33IpEwEp52NpW7qdLg_9QzKfJ4780GuvijSY3oL0RgHLKSpWtSBwuHyA7mpDT6qX167N_yTWR_y6pPhAUsVm45_9K9h-m6wERKkgnQzEx2xUxs0wrUeW2gWuSQon5PDYh0FNQxcPPSaBSwgaBfT3HzR1Q2E6LXEzs2D0L9MNvtrWsd6a9sKzQ6sOcZQ5cNmkpZlLDB2MfdZhEOfOW2ai0KLRIV1pf1bAuQgZz-mW_mryK_dvqS0nNZxihAVkESdyK0JhSGKosxTAWL77Z6RP6ueTAOYmGWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lceK1aQcHisPFxxO9k_7q65tv36cRaaFTsuxXJ-06YA_nHKcpMVoVs3cYZMk-P4VyrXSOyIN9TMrOlSg8atfWtgbjWavU2Vspd4pFADno1uiGUiWz18z9tSWvWK6sfLnRzVXdVnHTHZRYH0CZO31x8_t4PCbKtPaphcA_zCrvV505ULiMGAM0Hm_uLgQp5m_DZ-W05WkHjNsECJBSsr7opcu4pUvujK_9OdTFbM-TJe80QQrBMkBqqFrl_Yr6-oY36wQ8_2pDli42ffdVpzv8z-XJJzbGWr_f9c7E69NmtLto-xE9i_lwCJa4EYnHEBhDcNe4533IWNdS6YDnYnSEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMEVBRR_MClz12Z0sadnQMDIFS2vhz7WR2_nNcesNN-1GKd-gyE6LTdXlJBrCLCQkEwVHzov2xpYjxuZW5-oRDjAP7ofzvZaGY93FpJWZQmf8Ms5exBT74kwM4EaNA_rx1mj9ZS_sRlxt6UcA1y2W-Zv8vK5Ix6Le3uiH0rPWdH4efhaNNfq5c7QQGgyU4POOgq0ic2k_6UbKsUPQlH_AVDqYdiuTK8wGaSOJ9CYYOHxHBB8haNCVDx3jpoOhxFflXK-L_slHvNT754f-WO2nEy3cTB0nHygw9k8I5tiRDdQ_9MCDs_nT71IyvMnj99VO3eZOKND7hUqzKpXEB6vQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl3I_kXOgcMZXYnxx9MTX6B9aYz5-zQYoh94TQ8deWQTiTAHYzBFMKhJz67MjQWdtJNiG0V5gLrnWPLyohVFdQxpX-g0gnq9YFwfdKUzFumY4353CdAl4URY-5wCip669_dUZTPjqGUH_OkBL71j9e6tQIXK6El0UIXCv3HHfzwuX_eaSVVmdKX3XjEBmGWJ24ijp42Yke_wl7ssEjcA_gDPFMjlog1rukSrk7Pt99ZEjyWTMR3UWzeK72h-4e--i_dcvU_56dXV9lRZXXVBX1FVVLtOrHMZ9Meb4zJxf9A1-LmxRrWz3tUGRq9p1JxjGE77DWLOuRLfm_PFMFyBiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0_6J3tSJ9pT5x_OirgIajfsBLc7stKyhbFYfeKRR0v-sk52j6Vx54MWaaKcuI5N03ZFixxR7hiGOZ6IZ-nfvDqHVMF-cysXHv6BNM2SoLmEesppR6cqquwn50wH666ZA5XCcW9oAnnNXswJYGQqjU4Jxks6iqbWp1Ti-cKHvEJ3mA9jgzqhxSVnqYyjfqV6qCqMsKzQb2XuqKFZMi5XC-otaXbdBI1kgmaNw2JjgLDir7dXTDEChHnaMraPY7a-aXhBXqPN0lhT1Qx3mJthtkBScqLtNAe1cZwh4CK3zXYxRRBMiQMHQgzukvBr3hNPABTuwIKLcoCfXvZCrj9lbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5aseQAVf1DmqkO3WBpdgy_5nE1qHz18hKMPfDpYxnPdRMGToq54dHnDbJTRUSsBOV3PX9pVbAg2F9KCeM7QsPzJOr473FmxoSYTS0JPynFfcLNYK1swvDX8W1384hm98clSEf-xWWM97jHYr2EBmdjvuQrthxfEwttVVlsrnLbUDkObAAy9w_6kBzh4cpoTs1SWWYYeR2dy1JRs-7ygdvAGqZIAza7V-t_5fEPTxdpn2JPEBNWF98OYAbQJuLvt_Wsd4Bp-lKAj9gHNB-__YSxmQUkg-M3XZWQMrPX7LhdGH8_wFy5Kza_wG8P-rJccQAkyJ6b0xCNxz0ne7bbybJg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5aseQAVf1DmqkO3WBpdgy_5nE1qHz18hKMPfDpYxnPdRMGToq54dHnDbJTRUSsBOV3PX9pVbAg2F9KCeM7QsPzJOr473FmxoSYTS0JPynFfcLNYK1swvDX8W1384hm98clSEf-xWWM97jHYr2EBmdjvuQrthxfEwttVVlsrnLbUDkObAAy9w_6kBzh4cpoTs1SWWYYeR2dy1JRs-7ygdvAGqZIAza7V-t_5fEPTxdpn2JPEBNWF98OYAbQJuLvt_Wsd4Bp-lKAj9gHNB-__YSxmQUkg-M3XZWQMrPX7LhdGH8_wFy5Kza_wG8P-rJccQAkyJ6b0xCNxz0ne7bbybJg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8oFi67TjmG_aG4f8nu9Oq_7NYwUORwy8QggSpGOCO3z3XyY4-F0_Nn365wBRJa0qvlD7FFdUj_6DHR2lV6u6O0Gq-RdMoDWrM4cGfo2Ihv3un6iRb5sqhDwlRUgBy7jRwB3bP6tZwzA9a7E1PrMuwf1ATD2tgL2YkobXqztT6qaPgHR9VWnOf4M5jrsxA22iMmaJEhAhBk6RwuzP7yQCQHTsBUUx8S8F0PsFai8G2AevjvRXEHJfY4EuXYXRHBS1UQu-ohev5pthzZUNf0BenqRY0RHyUftj6dEPMhIVbCNFWwEaP9epXZebONosrpjGac-8ipj0TeKN8auw6a_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
