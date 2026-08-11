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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 18:20:19</div>
<hr>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=q6Ibrx6FbfcipZQxKAryguafCwGUrYQ9oAtMVVctdK70e-GoAhwsjPvy2id56sGX3q5Hu0ILbCczyGMNi3RvscvUHjLgcjVJXlRe-DTbb_vchDjkKJ7L3Ux-ZQh94TKbhNykftvaI5BXLXW0I7q3he_NRcS5YVk-PSwAuK07yyKMYAalmjzzRLPU1tdOfraV-p6kUILV7srR12CdIj8fKOFC8YHixXSTMLV8Ilo4knH46KKP2ONXp7hrKTFhUqMmunWnN7X_cCj-kt6I_tghcynDAUntnOv4OvjXaBo3bemkQc9jfMi3FfsWJzzttLiDAthK1Ae7rVZNiSHSjErO6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=q6Ibrx6FbfcipZQxKAryguafCwGUrYQ9oAtMVVctdK70e-GoAhwsjPvy2id56sGX3q5Hu0ILbCczyGMNi3RvscvUHjLgcjVJXlRe-DTbb_vchDjkKJ7L3Ux-ZQh94TKbhNykftvaI5BXLXW0I7q3he_NRcS5YVk-PSwAuK07yyKMYAalmjzzRLPU1tdOfraV-p6kUILV7srR12CdIj8fKOFC8YHixXSTMLV8Ilo4knH46KKP2ONXp7hrKTFhUqMmunWnN7X_cCj-kt6I_tghcynDAUntnOv4OvjXaBo3bemkQc9jfMi3FfsWJzzttLiDAthK1Ae7rVZNiSHSjErO6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8LKtiFhKKepSC3KrLV9niniGXrZAMov0Hc4FdQlcOETjTzOgIBadTdMM6OxgDYMfZhMPwsszMIv90or4efwwU16IQkJYxhbzqOQ2c5fGswCcQwCaHbfCULwVJQSJVHFe3A_5SKwLPBu6KOGoha_NJSjdQnA_EUt9VDFYlB1o0_Jjrvryh7rhuEzNLFLH-4lA1YCsu-UnpCJLOW20fBcepmb89lb4mm2RNpbNUh0afUXhfbtqN1i56M6PNTJ-HSYFGpJ2q62uePzsZzChKE2udi0RD7KhJBBHVNUT1wHws6ZlKi91ukM2JCqGICiuLWUx61QolM864kyB-8CoaQOLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYB9sOyKsiatHYvbp4gbC9ZCr3hilz0RMS17ucE4_mk1e6twh1Tq6lm-iSY9iaklaRuWNQLTRnJvReebYeaEqecOsfNZPL0q1isjV4BdFhFkvza_WnnROS1z9bugh51XKefzuG2IWaE717uG2YRu1K-7bb8ftyIBLJBMWQvO3AtPO1JczGJV0CFVX7eWXxzVWQ9HPefqB1ltxPhbVGaTo44Uk-E8sOgAdmzCbP9If9_2KdZgCzoYoQCbpXvhvhzutycDcWZlfWmaaipZxa3hK8ktOggE94r8D5CA3IOfXdzflQF5TZNo2KVJJQFmRC-n6-vr0N2xYczm1UELGy18Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InrP1RXG9c8B1iPcB8ieq-FQpv3bhh-T0ywnM1JIJWTowuSo0puOTjoq0QwhuhPQDosoNYk_A8-yW6cKldCyLl4hk6ABhTPmvRLEjvjOu11q_nqAvDTzHfq21JQn0Xz6Fyrxu1dFmrwSiFXlb1fD_ubP6l2OWWbPI-JG-qpv8ZTd-Ka__yiZz7gg9ImrcZEXIInnODMvlusFzHM3ppi9KrtUoWSeEr5owyOJUafHNrOv3-zRCQ4YZqBehION8EMwb6Pe5k6TPgHEhWDVIInr5ZbRdlFdk_bZs44SIH7JAQb67u18XUHuKJ-xzZIcP-Fhj2CLhjsrOQBYxCRjI0m1Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=NtJ0OltJTRbMBkHknwMqNljS-qqpfAHR-_hkc8p-_bTzV3pV_CPFUPbsfzZm7j1c8iLhIbDsSf7LgOSJQrdodc7en8TgiaGuVGW-bDAyThvs9jwLbo_v47DFDsaP03oP5c9yztj_OuKpI5dVhtaDkwpW1EvwoHIYPfVEGhyEhQv3Jld4cLI4SQV74Kpu0j7t71U4sC4m-TaoXK1MdSFOxE4olglemYvZVDWt9_0f9GihrdsLC2CGcgV4p0nCiPHabeX2ZfEfTzfg0c1WbtsZKSDUiZsJOSEpKpfCbm5e4oB7_VePK1nl5Ux58jzUuTGgEHn7j3CJjKdLUCo059EGvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=NtJ0OltJTRbMBkHknwMqNljS-qqpfAHR-_hkc8p-_bTzV3pV_CPFUPbsfzZm7j1c8iLhIbDsSf7LgOSJQrdodc7en8TgiaGuVGW-bDAyThvs9jwLbo_v47DFDsaP03oP5c9yztj_OuKpI5dVhtaDkwpW1EvwoHIYPfVEGhyEhQv3Jld4cLI4SQV74Kpu0j7t71U4sC4m-TaoXK1MdSFOxE4olglemYvZVDWt9_0f9GihrdsLC2CGcgV4p0nCiPHabeX2ZfEfTzfg0c1WbtsZKSDUiZsJOSEpKpfCbm5e4oB7_VePK1nl5Ux58jzUuTGgEHn7j3CJjKdLUCo059EGvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXLsFA0RZGt9PWdj5DmvVMw-8tZ2nRofxejMiyt273S4ChohX0t2ugsvhBHifwRurBkgA7OColWcxmCMyIUkwdZkvHUWYQ0U57RFE_vynVBTJHTWeCvpx5HTnrrT6X2H5hmKGSxjpckdU5SvKPWSzJtOqOxVG1w9IXV7m4PQG9qiF7AcDFTo2m5U22bGuwZB-9x2VagWKTN_oEkfTc9wUFnMK6OtIpcb1eLd_Y6npSscB1v9W98NJFXLZhEVm1kVRZdBCHipwdIxCVclcMuGkryjF67g3RUxLL5swIZ2lAachyAweJY6dqlM9Vbq6YOXpuu55cqGxvIaI3TitA2wFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5EP2OnyGlMij2rSYBkxRh08_WtJyA1bxfO72yfiEhVzWxDhyIvaXMCspIhd-Oae8OGmNDA1_vfRXvJElw3xpUhJ7BrGT161qgwByUl73c6nN_T9a_23XZMAz7-fdCzzp26fQurqE4hjqHEXJhNtkarX0aE9aPcIFLGO7C_GyeCVrUN1A5Aemx1Rz03dF4lCLyTgHGNW8dw-MRvciL15jfALavIR42O9q6ARy7EXD_lRX4MAi9XJ1LETCFBhk_xhkNecClQbmoSOCicKaEI08X_mwiNoDlAoESgTe6z7vfwZNz4bB_cVm8yfyI80Q94MTtvazHgtWYp0wWMg3PJnUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFpdXBRt1CSn6QUNwzz29hQPSXDZCxjS-8u8hPh-oU7il4qWleb8FfHBqZLpAKRP62ceb9aQMDYYo34vb7Syzj5Ue1cXUj3xEf95Pyn0l1ym4-3pUkEDY6AfJI3DLkKLfjKplbn_lQd3nwlwsIbxgYTJBCoJCh1V6bvSFcjaXerraRoXN699XK6YOqsJNBUHJCmLtvs4VOJb50F5_KMdVl18lFc9L_88dtYVE2tOYwyaj6tBDNrkqSt0B4ClpxmmAM_jb6JHKINt9pKJsMXRnv8-8r2QAxJVbeezzTxB9pUN-y-jqsfInXqb5dcBBCJfOr_c7XaajHfehGf-PQCWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsXETY9c2Os5uLbaTEYUMmg3VBs1qfWDuKWlQ4GzgqstuWHMGxTOGdOxzN8GN8hmmKCAVn_9NQ3PkSytg19P7l0A1A8zi5aao6mehRqPz7GzMfvaGwNhAA9L7Y_d2efvCQ1H5bZ6CYkvS5OsqiNOLJ7alq-2x95CG1jpiaIhJ1w4DH0BK4S1CclLtXJ-7uXf5OaocbybQhLigH9s_ICshRfUilNOPpWByxFCAcocyBLOmeKPBu2n5UDr-USnA_ABy3FT0XGD8dhJXycInTKJmL8meUXsA30ZYXSJx5f96AKA9AYeeg6fUvgVa91euHacDi6AJ3-YCd8mCKKKf6y7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FET_pPQe-gWQJ2qtcQPTnatZu6KA3FrrD7rc_y1QFMn-kk08pjegTUxBDQz39yy0xCXtEsg4nUE_bv6twrJzHbyqvRlh9E7MZ7ybXi0igoO5BRspVmiM-X1g-f81n71Nj85T93dCVTvWqSRotDFQiCkkd-7gtqpcZfIoNYlSpt7V5s1TcQDenNrRuoi9pWOAOVnzLMfMNZyrvTH0hS3f73uLDfCizXcmvmXHh6D_w_FrCODdwIX3kGQajqWn4_z_GXautOkn7mVhow5ZpGV-1OYdHHetDmC2nM9XrM-aBZrTvTHplpUoxYgFC_28yGNQRK3Llm5KHIQVZu14bqejGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfRfi3FOZ1GcyzYya9K5NgKAw65OXgnebnFsJ5cxk25ZSAwLIMw2WzAF7V2hole-QSrSMbHKWMMJX-4rP5I4aYDYEQ3btSskTZzHzXcwG8fbqyXSw5fTyF0WUc8HJKgsIAbxxhEUSgfAdJoQOkXD1G__XAdcYO2OHcYk6a1P3OAMEKhR5XhtwEutWgtJOfh9LuofCvo1XWSm9xgbDYB3_MmUQiLolsTxN3J1SSHFrs1J51fc2VsAmPFMDLlkeYzxZFUIpX-63fJllht3G2oEWzpFcZSLc0H6etDh3bLc3ZLSxJtcvHwtTfj9aZUxvk_1Ok_R0knT0vUsg2PgUAMBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMlRHsS1HBgRd_I3QocV5-QzFzZQhIDEtz1KEv5jkN0W0mz7rywAb8HzGVETcBv8pvnUC9w690Dw7wajcIkMn1CpqT7W6p3goSzb6j_y1F86wMbpy1VU98ZwDRnYVTxj2cB5uQaYoTCsOLk6Hd5-x9gQX2_sswz-DIe7WnfzRK9AzmXXQdTdQMIh_aI_fgshJMrUVDpPt-p8PkmURswkrhA8XX5PNa912uxVw2zAupGhPMbiil5F8VRxk3HnkU9bgbcS8M7HcCGElFr8xShkWVNrimVcp6TBuyJ_H3WOCzd2_uuQodp6Jc0JazQw56cEAcN4OF8_pfnaU8H7JkWJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UpG2BhioQqsKL6P2o8CTwHnuqeYgjsWt4TCMP0DF7mmSGkJBp61mh9bcKoehbb8zpbPjf0HKymrJZd8IknKN7-5kRYqO99T6WxFdh2ZzAy9KABZSi-EZlcTtSR0ge-o5UhQiUH4vTFpWyENHkpS-7EeMq2zwYsfY-qo9kWJC4qCw0umRrn3_vXUJpf0-497XZOCUM8Z2np9kbli9XSDO05nLMJYSA_pXbRUTUdEZcluP0oUJz428oJkRzS6I-UjJh22SmQmxCDDIyhbv9ZRvL4YkUx2kKqoJ1u_JMLIo62TX19T2TNPvEAmvhgi3DJc2UjCBRerbKI8lUmXrkJFH-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt9tw03ObZGd9moy8wBMvBI_9heHMNfqVlYj2I00UVHeTcMP2DjOktj8F7y7q4Up2B9NK80n9Wdzw1NkYlxrVIbZTJMC5F3DOjHLI4YR2LABqRX6v3kZVG6QY7lFKdgFSVQKSZGtXeMHz_SkFCtsrt9or5Kp4DdSudp8sgqqFE73CDNuFLtGw-4VaH0k8Dhk2F44AsPd69WeCRgZfGgLdJ11k7_SD7pclikhjwReWK7sWve7GC0N2aekBlL6ORusknu4AEddMak_PYoCOkROQPfJ_Zt3pIA4lzKmS3xDSp9BpJ7wivuZpdFrieq6oXP9AGPglq0JNrMzp3bbNgmawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vq-KzUdscpB8pQTR5JrRGKl96dr97Ngk1huouZ1ozqzbreErrY4czqbBFltr4d_YZr3Z4hB5YcEbS0zz4WCjta4h_OFycx8Tb0d0B06OibVSm-JbnwUqxRLUR4ppOXwQhCFFAT28xbV8WYmqsLP5W--L0iZq2pUQB3T_0Nqk49MHVBroJ7UdJBVHPI0X_mCxtNnP6jUsDS5pP7-TX-iFXTTdshk2tlz-ticXY64ZPDkB069BJ5GPD5lV7pcRllK4ZzVwea4iwHXTztZf7wlXWSDf3-psqIQXnmme2Xuulj3PIcd7oZ0smK0JCd07AqDNxzugkB99jeGlxxyxFHK0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIBnuyGeyQSKHS5Vpjvci2SuFzV-M_Oc5G733B980-CBo756bF1XlXW7KjUyJaxhGlo8LOqrDWYApqBb5X41ULlAyxJtSmGBF99GtZFaXcbWtBnnoh_3rm_qwmJisXqo_zG_yG-finxFqNckKZ6VbQPvp_Rr7xEbEdBZcApsW6ca5CC6vv6bJK81voOPm6l_14KV4Nny_jXbsA8yR0KBpnxWYk0eEtav7XkOS_iFkjjwNnAKbZyvUBdzctKuHngdNqH1uUKwhwn4z8K0Xb9ioYqVdG4VgNkGTYJVNe7VfFaRkWSAbpDc1cmQMajMGDU7nD0zj7O5d8V7_3VpfOBQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7WZmXsoxJzNNd0Ml4nVO7I16gSZgwNM_NZwTiucry421XTTsy2Bt2id5AAn9jox1rwzGuR2PG47KNVUdjluZgQKTDHYVtcqzTY6ZZZcnDvxk0QeMzyj7RMZdy4CzA3iqWiSTKwiNxjYp7ObsWR6Ti0KZPgfEFxRAfwJCrWLowBP6FzlXWcljMGG5YLvxOC0d15PigMeeAXKVHt-6sdVye3wj7fEusuZ27DVQK4pfmCDrgs0omaNEwJH3SahoOc9uZ62SdcIxLcJ_IUhvZ1ktv_C9HZQUjd_xusxnsltGHpQ_2Cml8tn36NCxLejcRZszXBkqhXJaO9paYFu8zgk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0S4ZAGQncSRKfMrE8CS8bCNkI-iILmfqNsd2souUT5wVuOh_HPK8JVG2emxOZa9ZaX3EgCBpXC9NdI8lmYXWWM07RNxzW2zWNrUMTQt4fnwC27qBTry-QKQJwUMv1A5QMTEI_kao_qgzKsGmSbkZvrIWZmbLyIN6OcyTyLb1tL195kwTF46TapOl2pVJf6f2b62F5329d9bz8an482HjwmgnymB4PuzwhlpfNITIGEs1jBYREJPMIuFQeiUnF9HfRRuDejqqEPdHqLRlhGMB4tHBlxhUb5h23jUIDRvaMYwyMAgeLK-KPQGF8DA7_6V8yboq2e9iGWdrbkWktGgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwVDUbfEZhTiACuAV1rEk8bUgk4EBm-qCUEH0vCWH1-aoZutSkvjq2A5EgcLstpaDnJALfORKmm_Y0HmXfizCKMrTUKwaJatc1vfJXZIa5DlSujGbTlmWkTdTWWZi0fxFu1oH5_aLslTh1fS_YEHs0gryclWDrDVAmjuup8UbJZWXjKSsbkItua8-veNoF1wFBu-77Kwe6gnfre6Ga-0NXvPZw76lF54O7TQDSfoqnXerd3Y8zAxYjpULAi-O7c8UFXp-5N6Reqm2m2Z-CaIy4S7d0j-_zcBIlgr0_xEVl5ozzUvlc8_x0MYU7XAipnar1CXZIUBHLpDylfSH1fQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dR-zIBD_Hmyu818pCkBP5-MmYXy31PBoXmjbmWgl69Fw9S_-0JA2IDXO4GWDz9s6NR5hi-__ZL3e3d-Z3N3wTxBoZJEYLy2fsfcXfOjE9K_dz3zqXs9NZnNBL1WQCVueAJ9OTHtRW8xR04XY17r5Q5ckq1xCoJb-74-UKVVGtPU1kONFNrM-FBha79u94IiknL1xrGvgkRHF9Ongr0okSD2ZPDFCad2GzN5XvHQvTXSUrL6eoYo_H_mGXcbobjDtfLqhWWnKju175ayQLp4SOPnrx65oW0qXOJ-fSdktv_dAb_kss-7iUtko_QoCgCVZcNY_kBxRNTzMbmKKvwVJPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fyXVjS9OceTCEDCZuLFBV5gZgnEktdVq5MPT7FV_sf0StvmV2_IOuFpqEcxQzAaJ4jJX5SMlAuVIR1teey6Z1jRAS0-6Vz6Ttm570TfoFV2HlM9j64jCwAtuWcF29umUbEtIkERU_l3AOoOvVxPJQdgfbuhZ2Ea3CmsJaqi3hlbEqPORAVA-M993NHr4ZKMV0hAupmqJSIK1dgmwmzH01-a-Xb9CqQ821bVc_HCzkX0zB4hX4ogFzKFvIRI2Prf5WvLwKyeGoY5cnTsF4Kze9ImKr5Dxjb6CDWJn_fTfuCVLk5VWuU5JH60tMFFmNa13nj_cGzH0n8H9d9uGJriFEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV8DVizBbiAT3K_oKo5DoWaxhywmIB3S0jfJKr_XIkL-7REZISWzIOeHU0WHrcgu3hdjd-i-drlSRrQ68s9QlWgmIhBUtrskAAsG7iZlP42JoCN50ogKiqZ0gmvMA9jKtXCoUfjwG09ngWBYhC0D_BGmpDmgeMK6wPZgRl9Vu_V3UfRBqne1sAiVtWHlXXa-FWOQz2Ye9FmqUn-3viP-W-o3QDnoHfJiqocMAVwixIIS6gVBmg9BKRpD1oO7zcyQ80OrY2qYt8j4GkkzaVzPhqZQFfmpAvn7IY11EBU6gC3PKjxZ5zgJNvR8U4xv5AbbzfhTUe5NGyRxV8cB5vZFSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQkVXAVBbydwlmiifCXW9KG_tAkL05wcH3ifsuTQooqmgrjKRYGp4SvTtRITUiGU_Yihy5nysCJRbq4z05vXoUNyb0E-5sBIwvcZyEDil8xvRn42TSYHSn37Dg9stcbNayqzS4Z6R2OmkUO9YyIPuRPK3QMzpdJW6Kj0n5mtj5gISS5SB7zedG00YGcaRsc7RLk8j7-tnq9NZSx9muK0oBFvW4W1szVZicAItNGnnN6US5ev8gVOypNRDWAIEmHpUKWl6nUiht4Vh3p0sp-Tj1KPD7CRajiLKQ9EgxBgawjlQ7V0xxPspJuEwwzSNWR1DPv0TseyAWnhMvc8Bw4fbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moJ-wLWhjzsyp3ZmSDTdT02Rh7bCDSnEWDa1yorpE0iu-fQ25WImAlY7fIFmfPbGMAAUlXbkd6Ij4m8Nr3vpwt0u1WIdvOolEX-pptvR3FWBDDpgSBEk_4WT-rH2ycJKdWQAwzcVTsM0c9v6TTODOqTB1bmvDI1k26pjxwfm3GgJFO5hkOwC6pp3d_sfmbaoDRP0E03RWQEVUICIkqV1Lr-qBs1egzKTsCAknP8xLUBPn25QJgBbJiL8xqe5E1lc5iJ9nA_rHewmoEcjE_SH4MtLyOC2lj0gvtJQbmlNbbOp3Em4s4fVMUM7LqBipSj-eVAwSWaJqeuLef4rHfPTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFYM62WMvcblCAsz1C27wt8pubOw-PI5JULzNJAiTx3Xm5tkNytmR5lzer7b157pdhduiMKFKO_tjrmD_ERmnoWuSKMrpg_nG_Mqass62_WSnpv0_oXKA9paw3HUaE9x5J1UhAeSD3sSSYsbdaRICZ8TcwVB20bu7Lt9UzdiIx-GmXYGZvz31Ft5CEj6zuZBya2IXwhMGfXRQDek1uUFZq6ZVhHS6bJLA-eyinHov6W-Oo4ssPTtEktTqJwwIwQA1llmn4i8wWVrRPE3ogkJLds0iyYOl9NvpAoYY4n8tMFOF_gfLt7VvzXftHvGq9G_-X2NNJCXsuHcZomxjqp7wQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=AxEuEmOSlH3xQyjeTeR0p5etFSwGuCNV8biRxRwtpAfRsskx6luysBWPbgP9pMPhBjNu-2ZQ33r-vnuNq75VKorsny-qnrVxQTwFRYcPMLrkiN4gUXehX6mVygAUBlxsOrwEzZYGGGEth4cvMKs8BlyM4t7Dwd0s7LONSG413_44L_bLo11izroJvL1d-U99kPmWFMVnyoNbVqAA_DD__C9PNGw49M_O09AzHb53ReXQ-LvCdOxhbumXHLElGSn-0XFI4OxexUHMzV82u030BJLd5djDNqFcvWeSVIRThUsIGCBzxzwIhWzuyyTyTk4y2nlJ8On3Sc-xOHILG1pxTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=AxEuEmOSlH3xQyjeTeR0p5etFSwGuCNV8biRxRwtpAfRsskx6luysBWPbgP9pMPhBjNu-2ZQ33r-vnuNq75VKorsny-qnrVxQTwFRYcPMLrkiN4gUXehX6mVygAUBlxsOrwEzZYGGGEth4cvMKs8BlyM4t7Dwd0s7LONSG413_44L_bLo11izroJvL1d-U99kPmWFMVnyoNbVqAA_DD__C9PNGw49M_O09AzHb53ReXQ-LvCdOxhbumXHLElGSn-0XFI4OxexUHMzV82u030BJLd5djDNqFcvWeSVIRThUsIGCBzxzwIhWzuyyTyTk4y2nlJ8On3Sc-xOHILG1pxTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=jLN6XB6_9cEz0KJ08GlEcitJx_bSuHK5YpSUMU3D7Mob5OYbQjI6YswASaR-9IMZtjPdEjA5hRlfpaDqYuZ7iUCsI5nMAi_wyXcvAXK-yWTHQISKl5019icX6y1k8sQ5oTwUqo4x4Jgc24X17sDIS6LI0_dHkaMCfwiqTfWA43u3O2K1XyhXXfukCbUbaXXPaNkchmibtSAinihmGnQQ2icrt4pGyDHNf47rUr5rYasy4HtiF1DOf4Rp5TSbyMxBeFUcfXDXhzLTd5-FSv_WIizQNOG-qX2KhsAhF8u0HUHdQ2MDUziR_itz9x10XAQX-2fJIu1SGyaSirvhLqrX0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=jLN6XB6_9cEz0KJ08GlEcitJx_bSuHK5YpSUMU3D7Mob5OYbQjI6YswASaR-9IMZtjPdEjA5hRlfpaDqYuZ7iUCsI5nMAi_wyXcvAXK-yWTHQISKl5019icX6y1k8sQ5oTwUqo4x4Jgc24X17sDIS6LI0_dHkaMCfwiqTfWA43u3O2K1XyhXXfukCbUbaXXPaNkchmibtSAinihmGnQQ2icrt4pGyDHNf47rUr5rYasy4HtiF1DOf4Rp5TSbyMxBeFUcfXDXhzLTd5-FSv_WIizQNOG-qX2KhsAhF8u0HUHdQ2MDUziR_itz9x10XAQX-2fJIu1SGyaSirvhLqrX0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZuVmsmTCC81eFQ63zYSQ5WHOdZuE32TbzgIKgBycrWjZC50gc_Pq8rQTL28EfoIkUKrZhR0G10kjLVJO-aTjHDCDO_FzNsFqU0TmyymkDsR_5c2SwEBuVZjHxrItyeEWCXMVEN1vRGhtqHChixs7GQYtWRrVzKPCpXXvM0yaCd_wa-TPqp5RhBW4E5Ce1iR1RzO9BwZMqpe1vE64LMXJDFEODlBPEuPLxYtcN5l0NktXfim2bpZzPcz2FyVq4kz6zyrqag9pTtXcWVcYq9MgZ9MLGrNuGf1Jd0SyIewgM-NwmscQbzAH2dfth12pWSU1xm6wFTcLlJQ0NfaQwIFbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIK41dNslqb2-6EtpXTh8KRezE-hJPfz-mejFk3DoAjLCdmZhd4EKIWvS7tLtgwDv2ltUbxbQ0fj9mu51c2JwT3tSwclNX5DDeFpdo4brDtNvIbQ32V1HnmxRCbI6TfrgAQuFIvc3KpNRE3QTXLDHtvoRGRJwIeR-9tP1bAuqUq9xxLr_aJ67gBvoi3p-NqLRwiLSTetO1_4yiCBuH_lkdjeUiV_ELDRF0ryP2U42fEaO2YPe0v38gTiz1V8sxwzhx-k7oI9gBDm_FLwVBbwv0QKVheTPQ1kUCcA0X21hpKtUPMx9WMJ1_znO9kwC0ncsi7Xvl8JFXbIiLRKT3L5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chP1YHIZlbNyfq_7UlpANIuvaSfGuEv7Ot_ToYtX4MnXgPmUy96VJVpleCHdJQjOy6bvFbpjsUjz8kWKa4MlOWeSKjVEsSAV5eBIyDcoNUE6VQKg7uqT60awtRFFk-AQumIvVCfVhkJqo72tOO9rD3AarRKblRYm7nqmnI1fV9Wr8REeEvHGA4zuA_L9zM9cuNImg6BYt4zPwkealsVQYy8u8eBj-c0KKiTnYqKioVuyVe0PG2ErlMNNZBQtHO1b1dMSjTmkP22Jyov0rjDOou0zoPN-c7NstgBBDvN906YYIW2168BSB8IyT18kDH1VHyApl5_hypwBSKypAQmgdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=QN41aeD8gFLBgPiSgQLPfKuxQwcoHW8VT33UTeEmw80k1UaDOiGfN4HXL9HO53RDYOiios3zVl5ez6_Kq09_19wIIt1UFaG3VLJoDOsqdC3LHL6s4kLvuGOCsg3dttHqkIZD7wKUhTOwYs8lJgq9clY4hYb4ONOT4pTLLJ2UQCr8XIqAx4XErnfqrZnOFjsrO-cDNxWU6uEgnyJ_EeFnVwRcXF43Pcn1ulxRI9h0P8IkoaVT8MB0rHTxZWbi8RTrVsvWCEPVUXWeAhalScDMqjvy5y88Ky7aLuXcWidkLjFY7_xUjNf_rG9zWFqEHDUdHHHpZ3rX4uu3ch52BIqIyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=QN41aeD8gFLBgPiSgQLPfKuxQwcoHW8VT33UTeEmw80k1UaDOiGfN4HXL9HO53RDYOiios3zVl5ez6_Kq09_19wIIt1UFaG3VLJoDOsqdC3LHL6s4kLvuGOCsg3dttHqkIZD7wKUhTOwYs8lJgq9clY4hYb4ONOT4pTLLJ2UQCr8XIqAx4XErnfqrZnOFjsrO-cDNxWU6uEgnyJ_EeFnVwRcXF43Pcn1ulxRI9h0P8IkoaVT8MB0rHTxZWbi8RTrVsvWCEPVUXWeAhalScDMqjvy5y88Ky7aLuXcWidkLjFY7_xUjNf_rG9zWFqEHDUdHHHpZ3rX4uu3ch52BIqIyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=Y0lpyG-j-HBfiPnvf_JjSbfJXCl9zAfZlWQsIWSP6KwcG3rPJLpGizHKKi2SFdYqpvJFHRSH1cgwVjKw_RRKw1jHBiSE2RtsGfuOl-EQU6TjXBGVWsJc5ecfDREWN1KdTCxaTi0llGEP9oG2bOK5NC8WBquhigSdvjjfPIsjTfhfPXEz-As9rKhrS6BUni2z4niNDQWN5Q4KCSjFpUMqdbxhF8EcxQPVoGnoMrBIz4ip1ybfDYW-ApnuO_6ZgHx8SGKUuFIatcg5Op5FCtxO2DBxCr7u4F1mMEUzPrRCZ5U7UHENui4stFQNoJFLLHVntLCO8R8O6onJESardQyT6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=Y0lpyG-j-HBfiPnvf_JjSbfJXCl9zAfZlWQsIWSP6KwcG3rPJLpGizHKKi2SFdYqpvJFHRSH1cgwVjKw_RRKw1jHBiSE2RtsGfuOl-EQU6TjXBGVWsJc5ecfDREWN1KdTCxaTi0llGEP9oG2bOK5NC8WBquhigSdvjjfPIsjTfhfPXEz-As9rKhrS6BUni2z4niNDQWN5Q4KCSjFpUMqdbxhF8EcxQPVoGnoMrBIz4ip1ybfDYW-ApnuO_6ZgHx8SGKUuFIatcg5Op5FCtxO2DBxCr7u4F1mMEUzPrRCZ5U7UHENui4stFQNoJFLLHVntLCO8R8O6onJESardQyT6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=o9cz460tns9MVAhQan17cMdgrRbtIv1uAomn7jTZPnyKHdshXZ04wrfq9f38BjEuXa8ADaNXybw6vo6pQFbOUBeF6HwxnlHiMJ93G8G_x1-9QR1ADonDewJmiYzM26P594QoGnwPs8oa8gPHi7ldS9b0WBPFZ9A8VeXcCIiMV1nwg4yMUWTZHGn3XcuTaJEQDW-RqKDFDXAWwGWUp6iJt-iuRAcnKeuykmXHhqQeO0zbxEdF9YJgGnTS0CeOszwI4PB5_8HVwvTnjy4RjxW_sl4yyrCOnLk9icCeJbSZlKeNNwIMZdo2KqdSrPy_D0-1YGzhysrc5W6JnWP01TW9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=o9cz460tns9MVAhQan17cMdgrRbtIv1uAomn7jTZPnyKHdshXZ04wrfq9f38BjEuXa8ADaNXybw6vo6pQFbOUBeF6HwxnlHiMJ93G8G_x1-9QR1ADonDewJmiYzM26P594QoGnwPs8oa8gPHi7ldS9b0WBPFZ9A8VeXcCIiMV1nwg4yMUWTZHGn3XcuTaJEQDW-RqKDFDXAWwGWUp6iJt-iuRAcnKeuykmXHhqQeO0zbxEdF9YJgGnTS0CeOszwI4PB5_8HVwvTnjy4RjxW_sl4yyrCOnLk9icCeJbSZlKeNNwIMZdo2KqdSrPy_D0-1YGzhysrc5W6JnWP01TW9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=qtWMmVR3jeOj26duWUWsC8R8kfCO6xLWQweI5e8OhPZJkHGvpgPRNOeqk8gksvaxuKdUd2_El6STGFl1Y_u1sgZOQURmbJlSZu7Z5AqYDEzcvmG9XRh2FmY4JlopNcDPjG5p_e7Yfmpvtg-KZCYo1irelmdVkA3lwRzByWxFemNqz9bsnEZlpWav7jo15gOYnHsFkIS_K_nezwfcH4SdbzO37QoYVLaQX6KPweknQWIE9LUGaD5BNoOziAK8Vf2wS7NcvVHzC-6L3gGzbu5B4UmqZAmAf9dWZdjOGBBVhXMRRwGzm5W7d9rA7pCOGSN5QpkHhnSyXG0cOgGZA08r0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=qtWMmVR3jeOj26duWUWsC8R8kfCO6xLWQweI5e8OhPZJkHGvpgPRNOeqk8gksvaxuKdUd2_El6STGFl1Y_u1sgZOQURmbJlSZu7Z5AqYDEzcvmG9XRh2FmY4JlopNcDPjG5p_e7Yfmpvtg-KZCYo1irelmdVkA3lwRzByWxFemNqz9bsnEZlpWav7jo15gOYnHsFkIS_K_nezwfcH4SdbzO37QoYVLaQX6KPweknQWIE9LUGaD5BNoOziAK8Vf2wS7NcvVHzC-6L3gGzbu5B4UmqZAmAf9dWZdjOGBBVhXMRRwGzm5W7d9rA7pCOGSN5QpkHhnSyXG0cOgGZA08r0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XA2cm2iS0OJIGWWkFXI4baSerJqvnsq1lWJNNGoTZuijeHfLwfaF0n8ppW37sTEiuu56lQFOfNcWqR8XIjIf5It0nugAxgouAB9iD940tx-hyaa6w3ZfxhniaLU52EM4Ce-CUAjFkPvI5lMfClTm8zXRK2ipU4lk0RDAIrDWFXRYah3Vf6dTO50HS5PLH6jJfETq55SyQ6-aM1wmc9SBejZIKhfzL9evnz0O0xbcKHnrSiRwxgc7sLgJXotBbDxsuCEPmxhQASiimQDesS0uPdKRSjHpXAbxGOKOo91F8B1hq60VY1GkHXWRV7rLdWOEZQMv5j8FAXmHfBi0lJsVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5grHqwxh_ELNRgJ4F2zQNgmT9XVV8wgZQ-_yKE3Aq3b5Bl1um41lPhFpIwNHkajuvNi5WoDuMuPOgen0tqMzjXtwUuxSCr1d5yH90AUkF7nEqEKAT_t0QHPxBPCvHdGamqBjAcoZqOv2qUpkKjdx5qbjN5sDsUaZm6pENrXPuHqpeQOVDgRg7WluORVhZQ2tbmTp6zmGq-GCMjiU1iDRmiHs5izn-XK9FGUTGUvc2IOkV2gQQEBdr4y80YjO7mcbDV8AD76-DdTJqMeyJ7SIiUMBvy6Z8VUxg_zPrwc0B-hYnhkGA_ZjoUBAfzomAfxRZPnaSwuNJNPtG5U4yHPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTgF5i3LBFsvLw7dw7kfqiEmWqnO_9D9P4TSlCYq8v4EnczmaVHvfd-GpKsc2RkshFhpNbukAwHB8f9KTCAybOHcqWt3bCBiJFA6Sqtget16-XjMqTgGg2mDuVq97iDgEdiYW1GIWTwBGV_-GfxsMhq94ZV3a7QCbMt3l7VzPAmhZTiwdmy92nYKrRn9d6up0z8hPC7CQp-98KvjUop_UVj8TdRBvtUe5KN31KhXaEiiAwubA1MqdUN7eaoS7CHzounSvy_17RDsymJAdKtREujh1qo_0ZamdKqkPEeFEh28moifr3ViAhMKui2grK9qequLN6x2O0SWQT7GpWbNzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bEtRhqCrOZXr34TI7B8uIOhkPjjuCaRz303qKeDKBOzMnZdANJAaZ_z9Tv_KwyCBxkALKnREsRftgCGZSWrRp62dTgucK3w5msvXTuDHQWx1TJF1H5QlluW-zg7BSDyfXuL5JAE1_KPB7e5jDYrO14K7KVajOtkinbIbZOO0neYyI-PsEAIvnYOhndU2YA-FLnBJe20mBO4IJKEFBIZiI1uBEK2EN8WWFBVIPH3xhpeMhv3XmM76K_2xjzcJNQ6Gbj0yMu6rOzB5DcTsgYadfoDHjMW25sTXXgSdh_AQAsu8GjawqXJg5KHUIEFPMOiRPY5cK19eTn3YqK7Re_jpeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gvv-Q1osMjFS3h6ZDKVnPmf5PekF9NhPOayritRxoVZ46P3N5eyCA6Pro5KCmLUSdw8Wx3_AZTtSYIcPgSs1akDvOBOh42qDIbKZDkdvKhkh8SFhNYIazW1jCoDon8h49fy0tpCfbOK0uFvOFQP-dn8V31anXv6aF6VlprSyu_fan8kIgcd-QbIn7aHjF-eahgxBCl5d7sTwTKieFJnktMhi8Y-pBuKtL35xnzg5VqqlfPQTzlf6lx7j1T3qMWdTyglAhTAFGoO5HECIThLSIxDkKe1TwzHYOSa0Uxzc-B_7n65S4TBQJB4xy7FrTN1IXCTFPWRoIy9ZONu8dUq6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOIkOeuBohcUBWu6-97qGx02DXfkzCJYuXCheLICN3KVJMnt0CrEl7ga0QpaXU10qVKrXNLK55Z6Ypip9JN5mBrcekNa7Mx64xwHWaq3AnqiRTm9ZR4D_47rV0M4ou0FZ2F8fKpjPb6hD71UM65esVhUfKiiE4Og7jsJ0aD7Q1XHbcxP1tR8zlzq8nSmxQki3U90jyBYIYSDOF0llX_mNdTS2aa9igoLVyv8w9TbBW-7ceCWnu62djVwxuMug8uQgt2WTg2isbvKrcbaKjEi6bNCVsTztsEqlhmExPncbS_fJ8txfNkMZzZmrvz-2VZk9iCnMU43nhQ8G47066uMqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqTbP0iG6BsYmsjLG-xL2UiTZ9Hh3do3A0Y17sL8gUkQ6fl535_pgGw09yW0B23VT3FW91H7bx57NULrLl7jUVYB0-whcTOSI-wNacehTdyKhHRZ67muf-f60W7BYVzRAxl3AUcBozJUM-ilzojlAVXV9_O043he5Xqeh1NFty8jjq4ArsoUumVL6jH-ENXAo4xbXN29p7iG_6VUlkBQPl_dlPDvsiNHEa7F9w5GY1K2ztxa01Ja__lfq4bbBtANhY3M1B5UyF7_iJsrQcCtzdqzkidKSgcC1OVjDI4qxHjyy7sC40YssxB7qqj3HGZNsfGXBrE24oq4TwhuTYxVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obrPNmqZCFyKV32zmh-C7XG-3s5AHGzBAOiXoykM65VaQYP7dhHTky860RFAY7YjNpXUMf684W9rqF0Pob0tySu-rpgLHSsP_Xkru6JhHCR8wavMLHT5IEx7spXqQc4RmgLwky1B5Y2BDWs0caWaSWMuTVNcVUVAi_QdMmUEFVeJ8Kgs7hfBUQQQFb_vgicVEFF5U84rUB2bW2j8bnIMFcJPqUHUpk0SLkQcWUNsCwGn6mbr5ZSPcGorwH44SAAItqc2KDAcm8Tc_P9mrlcmZPE2HbztQH_48DtPBHzU7dgQfcQPllcarJXRCL9lqb8Jd87nUouZ_5b0zvJFDlJQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTTmNTz5vTuMoPgbX8JP33a3lsrdZlbH-Q33-XUBZtMfyBAcc_YLycuZV8JhbWDxKqiTHiGIk0bO_MdjqZ0FE8Jp2dtttOiR1D9HsZgR_vGv69chhU55Z0D5ToiuzWs5rVZ7-bRtJ9Pj4JbVzIPOBndfGmmqzU-fNvPz4MM1S9co28tKCAJ5pP-KfPC_KFwsbv_Saw3UsWYW-0qTBhX3MvvmPoG6r0Acl9DWz5JH4ZtVD9bveBVXgbomrfBRoCcDwTKlMvnhnTO_4hIxlYf_3lIlZrWp3UB1UXZI8jHJlSxz9TqAZjCTePNqdCWu9PnVsZV770Zq1lmTJWlEnlxUsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTiIGM8COmQJdaAY7Q9cqMzEwgM6hW9b8Jqr7NXszGOIvPUqwex-E9331NvMO2HP4IaE5mTMqHmRWp6gkOnLe0Xc1hZ2ODBiZ-8vnxSVx85-379mFwHidODxIoX08srRGE8onJWf-wcoJ6frItYxuj57BQj3h8JA8fAlGgHq6JCz6N_Avx7qd0btv6NR3K14DQ-Dk__v6z2j58TKnoEbI6V437q5mMD3Nt0cMBo6B6RiyVF-epwi6n7A8-1xmSuYjqdGwVjj0E08bfC-HXNsVHB7VkarBUS72AUXAZjBUnd_5CWHRYmfkqL1jovDQeIqdfYbcXnmoQrjgZxAe5b4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9xpiRCM4yBcoiI6MobBTMYfd0FX43fSgJkeH1KBsVFh5Kt9D2puzjtIUuiWbLTIk6Jemc73_0Oeh7zLDOfB1QyVFuCgn3CE5N5Cr6urK4h19H0T7HU9n9AW0nt0sCCCMIygpbqdrSiGxD7_Z5ibfi6xcbnZC2xsxMyPmcxRGzAvd9CYE-n68uoyh7ooc7lDlUbnZnlTPc5Qrg2hi94mJjvrjsx2IfnX4M0pltrcrQznwT9MHrqLD9sRyPqnm816Mt0n-4EuLz5T3V1ZHwnbjwSKX0e1OZ8G6v-Ig-y44a1Nxw_BTVh1kqbyCFFacf5-NJV3wf043Cp4UVCnjRfH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciW8m0PXXyd8basWo8uc2KHlRA_TtbgGHtC7k6owkbMqeeyCex-a5YTKh_2bOrjLs6D-ReGs5tcF4mnAFG2QnZQF1txVmlIUAAOrONodl4C1PHj9xo0obgQEu-xKbIjoiDFDd07J-S9o6C1FbqpfcLZtKu-DzQSIEdmmy0fvuOxnEXV7efm6U4NGQsmPO3s7csexcybHjR4Hu3tWVmSOalwfE2N20j3bykAOp_RmNFrZzYqiTZA-hOw_8WcHfUgmvqWx9UOa7sVtMvyaPLe1XK0R3h77IjG7-AbLeqgzs_nw81sEUtW8mJHNLLOECm82mwpSVUHleiyWlCzO37pt-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBwOUXNkOH6R_y7W6qhX5ddbBhWoVM7mGcbfMZtwQKjaKBwp47I3JGaMfC32qINwjgxJNRGnqAqB28kLIB8Ei4aRP1H0tH1QP1WwFx-7vqen2nYOjPx1tsIb128MhFn0R-4SwEZMq-wtfb07sI-6nLs7aMo9yOr_U7mU04RLnIM5eU7pPfaDk3ekg5BDWMUhyyuXXVKo4khZQHuwS60juJpNG7lzKoUOK2tZUPfe_YVZtrejBUC5cErDl43fcaoi0LDaLYechMndNZ35uRWEHZv-RVTljfus16dhtEjYR-kUbRz2BoTrZ5M2IhGcn8OnePhRIDgBWMb4w8aWX8Mvlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT_7qtXrQThVTqM_AkjvBIIdFVs0EXcTDW3K_o2BaMJgDmhQ4Fl_U467NCPxJUtYVUYGi4zE1TcxX1t6Umt8wxyhFr1Yub_m8Vc_lV5PdLLzML7_oaLXKQVFTdIW2NKbskydpxLyBiwctZq3jQbponuR-AbAEbIl5veujXDV9kOEBB31-06S3Jrqu3Xu8cazlCnYYbyPEb69cHqLS786RwO9Cqo69kPY1A2CZOUo7il9HhrRm-v7nJvoeACqz-VR_90vAc48EavZ9VNwX8Ah0Hh8iipPzwBCXwWV6kRAUv5qzGJgOtP-nJADv4jYpNg8GMg6U8aUjmcn__8CQV0zRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=NEDHW010rR2gM51j4ar0eFaoFM6EaYHd4satV48Y93Khta5f7QpPJdSz7AzJmFgzpDQ9zVc-uEKXyOu_6qWI_pk7qPZI2k3sqb0BOpKdikrMtFNRIhWdLzuzM7FWIvpb8pDKOXZzaj5q1RtJaKs3_T5rK59GzK0Cgcsg-n-_Agkwx48XnRh_h-ZrhVTSiok8u4j-iinNVRaAwB9h2xByptH4qmZpuPS6es2IfxtqoMhW30_QMY31C1BWzzbVBm8QgcSO1f-fl0QCXSJFcKmFHtGgeji8TiSX9Aohkj3DRSNVuTsI7KZB3kNR1TpI6gqFiHyJhMPpvAX9iMAaKpwhIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=NEDHW010rR2gM51j4ar0eFaoFM6EaYHd4satV48Y93Khta5f7QpPJdSz7AzJmFgzpDQ9zVc-uEKXyOu_6qWI_pk7qPZI2k3sqb0BOpKdikrMtFNRIhWdLzuzM7FWIvpb8pDKOXZzaj5q1RtJaKs3_T5rK59GzK0Cgcsg-n-_Agkwx48XnRh_h-ZrhVTSiok8u4j-iinNVRaAwB9h2xByptH4qmZpuPS6es2IfxtqoMhW30_QMY31C1BWzzbVBm8QgcSO1f-fl0QCXSJFcKmFHtGgeji8TiSX9Aohkj3DRSNVuTsI7KZB3kNR1TpI6gqFiHyJhMPpvAX9iMAaKpwhIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvRSJebpfS3ASJasqph2lMqIkVZlMnzFauIj3QzBrdgDv54iH3gwuEb6NA03CifzBa7GDBByYzS0ujyM-CMv3sBaIxqA4SgK3fNzIXy6txMLMzwqEmzuMZNAZui2a8LVooZiF18CrXQvkMSuxv9ZKxD06FU7hAGYtxxErmkI7qaps2ab2E9b6bYAKNHRNlegehzbmGKzr4ov9oPYTsDoUVCsISZ8hUqtyRDcMwbnno8E-WSbg9hNfJwEcQKjiosgCqE5x2zgq2sxdkYXvmmoJ_9BwcnMszNmV2s_YIU0ydiueBxvsVuuYai3_aERTGla_ubKwyhILM6T4vu5AyRl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiuEDeHbrJ5pw5O_EmBoL8kp8bFXNEdMKuAHyqZ6SXqYW79SQN9nV7HMDsjQ5CCmVnRyUp4PpGt_gqEgD3LjfJxKHNenn0rA6C3q3Lh64O5H9h1fryHWpg6MeH1hTP5no7l1SZ7PwaP9TLnX16nRDo-CObII1T8RkffY2HkR7hFxYXNjc9s0syHsWEKq4yLF39DfELoyE708N1GOThma-GNEwxavXWkORx6_I2d01f2q1dyCnLOrgWNvy2CL-AIdmecDzrOZsJB9-ZasBOZ2CWkf100DQKXS98Vjq7UZ5MmjVqkArtPrhx2WutQWfbqtnLhTLm-TVxgO2hsCw7htGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzEnH0LA14zvz13Nts1SMbVXwxKVH8c3lPXU09cD8ie-88o283WWJbwEBMpxBG4F2U2HmfanYcNQH30IM19Kp4iGFtLRzbgnrV977sq-ucHlko1hhZjZQvz0gmWH2yORBlbqjXzvCQFFZmKipy-ziNTZYuGRcZonU1dcyFBk1npne1ggyPpI1oQTxtzJ929vWZ6F48EoA7lawdztCw-YobAe6DVMXTYiy1uWHLEUmU5VCEG6ZdzxaiE2PKNvH-FA8UaCxYbMduDT1S2GyTF6mkXkb7xXha43dWo-LvtDlEj6m4-OixaMuPbohjgLKQeizWacMUWwiDYLCKu9Hv0-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR0iNbxh4lsf_OTGuMHx5efSpK_UYp-dMH5yfdiBSkxXXL3fL6muZsHPRjmfm1K8jIORGSgFKcYnhuU1rqOnkSeVT-sqzLDNZMW3Kzj9FmsEuXtmE4ZTfN7glc03d143socCpS8GSvjf_SGhYZUK5DK-9vY2OPEbfLPJwHiVMfvGwCcMab7TgLx_I1fTCfw_ewd43BYP9XAjykl1fyCKR87x7rTPx_PWnseXJ2jmFl2hKftqX2JjExxotu4Oeu3zCSid8wf5k1rdxXTQVMVkdh2xSjnaixdR87wyD7yNvGR0G8oudYkqPSCy9ECVZpGW_ppXCyrIqd-KS2ByfAs6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppcpzpCsDEB0XIuwpO6SQUTigz8O1ofYEgBoAtft_YhA6_qPupKNl7pKtFkxq3Cq4BVa6RCSkbg2jCgyEQXHXPxEfjMlm9WWJl7UH3FayTyYiVtCgyv9NgUzeuBBz-98fFqOo5MSXqZYNdOTQtQ6gKU8RdTY64G3LNRJhCmbjyRVTOuCNo6j6HeWSMugMLPl-AaImt2Yw-myLNeuA7thBX4khnpNHeUPSkIzlMKlCULyyWx1HSHD4tiEieYU-JYjLcekaaPPVyQOlYjSzwfXcWtFnPVri1hsiQg_knHk-dFk26TOyxTkKkD3u7UVznQBcVZjfZlkQjhm7G3NAUH_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWK9fjn_nL2T1pW86-5bCeIJ4f_Z0NWJFeOuie5Rbi1dk1D95jh7Xrj2iVxkx4q_A0pqS_9ePoiW_zEnus0BUTw9cQ3ntFbei38wwGV6sU4-Ro1T1tLdG1yc5hQWPP9GnaEfBsFketPMsGbAjF5KP0tSsSuyWY9eW4MWfH7CuxH4r-6Mwt7FT9PpAfIPL0n23rLCCzoBCyViw2dNf5OtI_ruEcnTQ-e_cqmTrlgKNsXhuh1iSKsCOtLV6NZBIJ6-dURu6PqKNIicLugoRtPl8RPQuRwLdktagGGiSJ4AVTd1Fbo8x82E9mp0wnpJ00pS4wlBkRm1JcqIlHos-FJxCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EntJDgITS5mA12A8ATk5a1VwWpZiMfLEBtXC61DwkzFy9Im0AHYpk_-ZICsjCxtnqpXpzD1Uimbnq2iSD8PNmSWatjv7OK_JdBkdiqk_x81lezHO1JmdQ62ju1Yk3pQU1YSnQl7Os74lKedSuYyhuzqHbpSFH381Aq2bGycVZq4s2yWMBd2lPzf2S2UjrBuw2OpzSbxa5OymCnMM46BM-pLxZaOop1RCl6NVOWgbW21ECDO53ExcGQUwWroXhw_yvpdGKp-LZkogYY6gp4yBPCJ5axTDL9PnHHwwwXS0yem3XzuwlbkoDMF6zc2RaannHCiHK1ThRtbrtSPgfgNXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odYmCANXSjnC3TqBKrK9VbqAQ3p6GUPg8v8NHmsgUEt2F241MFl91szvu_r8EQ63-HJNhEFYIksUaoR1N21kCXNluJ0kZom3TZWzdHMv3vSWk3HPGjSiZoym_vl-xk6kxK6ctd8i6rH8B_JTcbyWIDEdmBQY-3-X80kMHA9u_N9dVrby5f5FCAPqVj16WrT8lvda4aW6lQ-eRoHmDzEaW-gYEi5U0lM2auGtZ69og4nA-QODdkvwUSvYw9kdJLqFTgCUqAbbnNIWQE2WPQFkp6gKJymvmmk3T6s_7Mm-BWcZ5DeFcHJHiPhiYB62Z4k5DyC0QDkN1W_Cg74X8OXPQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=L-ti-1R-Qu6TmahmGLcIgqOOnx3NZvujF5x2W1SbIlP0ROAyerI0bM-_cWT2UQ3No-gE42yPRna5MXn2WtYvvglnSKa7D26D9FiBT2mmM0qA5FEtp7VyFspnPmA9ss6oXlyO64cdtXR60D0nsyCzUUugbinF8tifHOdAmQrnr06g01gjMk2_VYSQcWzT4m6-gN-4Jylz2t4WZ2ioLuUKDvJbdsFTgw3ravxq8MdQlN4BNr2sdan0YSC6u4LY0ifN1H1DYYMV8TYa3_DGUT5tF0QPStW4rTkITWXVJs7GA0828ueJo2ZD0MLTaGAIb7mfqOb6m_mJUM4kfqh7ivRznw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=L-ti-1R-Qu6TmahmGLcIgqOOnx3NZvujF5x2W1SbIlP0ROAyerI0bM-_cWT2UQ3No-gE42yPRna5MXn2WtYvvglnSKa7D26D9FiBT2mmM0qA5FEtp7VyFspnPmA9ss6oXlyO64cdtXR60D0nsyCzUUugbinF8tifHOdAmQrnr06g01gjMk2_VYSQcWzT4m6-gN-4Jylz2t4WZ2ioLuUKDvJbdsFTgw3ravxq8MdQlN4BNr2sdan0YSC6u4LY0ifN1H1DYYMV8TYa3_DGUT5tF0QPStW4rTkITWXVJs7GA0828ueJo2ZD0MLTaGAIb7mfqOb6m_mJUM4kfqh7ivRznw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPbSYdgWnldMM9KPTelXw_O0DbCBHeJg8lhufbMoFDpiPacGY1u9eCoL_k1Eo-f1GNL8NXhImsL3EcNo95ppmNl--k3wu31KRNNSz1So0xrpVUp8cvf59JKU8BWebkKhgH_0LrHEeZIzaFA-QvCdqtYTu8lCEVqzGFocakLqL3Pkn96V9oLGnIsuQdfiHw1OEDNuWhXWrMz9L1RO-8csGhvysgbu2H0sfPLYcW_RAmUXJEKJZbZu_YTkNO5mnUI0d_MZvl2Fmd4OWeQ-DxeeXS8ba4TuZHcMSl5S6KsOcDCdIduG4RxJvL4J7lgAipqJ5ndw0675ARYeHEQBPgMm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X154E_c3Che4oJFsqF7-8oVePO6eqtcqHaI_kLx4A6qm5znitdfG_JYsxeLVttBqF-qcZwotltCDgl771hCalBRhnXiZh7lRIsjN6hVLha67LWOmF6-FCT-yR2rwTVPp-MPTh4uAC5DJZCCCeSUh9q-mYWeb1i5NNPg1ot7Un2hkoc1vvMyYfDQqVFWZ4EJ5I9wIYxSLpi0wB0ZZzNA07Q3ngY6iFmEzX1p4XDHI3vob_sv8cKZNANpybe2Dx5qzrAeUkeRsJWvEGXg4pm6cI4AaMW16tF2ncGod98kNwx_qgefTZITuggU-Vek3KPmUH794M429ZdRT_hP3VhGxXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLWLKVsd01r0igpQM2iSHyrpHsGpKRYNT2kjVHdarK-Jpk-BB5RU6U-CW3bXqjlD_gMKsWI-qh-Oj8IGBxiBSXIZ4V1cwrUanDFKlWf7ucXFQH9zjP1l2MJuZS8oScMh3BptTThS7Eoi0iK-VMUa0iAHg_Tlc98MdSpwJge_OLtBpChpZBgcWj8udulgw0uet9H6ukEOGfvptZ6LCjGnpQFNs3F7bWaR4-YO96ooU-KJjzGaBuKiQNHIAcApHNsQk7de61foZPGmkY2s0mlMtRdFOmI4_tWrZW61tcgVwgMFuWcryDRmPyy28FC4Ixm1ItNdZ27whaRzwvVdvRP0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkB1L4dugPK3rw87oVTqom7sw2Ns-PU0wOw0lg-y2Gxv7oa_3N-jLdG5zRqLpVJnci2ywaZKhIVi86LQIcU3ISLvvefUyTSPulmLvrNzZbM5m7fhqmd_JaxNbHSOOWghJJXxX9YwHOY5G8FmVK_hv239FBy1O_ajfdCn9mWqDFcqw8QZhquyhzJNqwdD9zxhnQsaAs4JqBWxugRQPCtuopPFx5pCHN2M8UbwJFGobw-__QcTlcxuMeDUJnrLdkpxjP1dsHWXmfCbL9nxhLN2l3FqmJNM8nV0dUZOhPfxDifcLY3fXKwuOjhLhJMOdGgFsGsCPa4NBQ1ZYjzx3uDKFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFE5_gR-WW4-7NPIHH8taALcOcOtTG_mxoU0I074dQA8Lr6ucMeWIZSb2chvz_slKhELgHqXhbKZjzEOq9xFX85pexo1k3IVBKm6naDr-PSEAFum0wQMw6mwMulvBtBAdZgF0AHGQvtMOXl6CxukpvuVC-xo1zDGVI9_kRqxAqm4HfI4zWxwvgZ3VDiHwZ7Hw1r104gvItJbEGrghpzAxLpseSOXOL3HQTip1ojtzu9B9DQhQItMeQlrQM3QoWyeOFfMpjOVLbd2HI9r7eL8wJsRWnO0FT02xqUDMkA5cyMW7H9-x2_WdqLPZTvuSIEgPjb7wtPPpA1vB54rTyfDbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXeJIi5tp1QXl8ym3YsXFsFcHG8orCqCMyFYcqFTLt8XEer1XAr03JRWus8PWy616QLRA3p2Bkv0g6BKVcKRzqKp6ehj2uB-DEyoRhLzY2NluJio8BoJaybQ8CfCjMQipm_K90GcpLT8qADrIZIQdpIyPw4Cb_WnJRcmrxk_DVF79ohp7YS1hpRy6eM7jzIfnEQ4GoMUQ8JC4H-jzP7H1Hh2ZiX4RBymK-b_IMBwwxRSWDVGeDk7Nc4i1UTIMipel_zCt8rOqQs9ZmZqk8uaCi9mkfBy9u_WdDwkOKTEdYu5qJ9go48c1-4h7I0U3311Ybtui5_c-Ql-TeGMMXLfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loOx18Yrc3Ob82GaSl8IGSaZuwH0Tz9FCoDxWQdSxUMw0-8KzoUBFCqgGAebvLVOQqxrF5rOo_cshp-IOts7MipPHSbYd83Hu-_7lIYkJvMRZnkaZN9xC2k4lCLgkQFpE7tQWOETz6cuEIrkXkKSOvwG1v_ijPYA2_CUTpYMojAS603PwaXT1_g7W2BfhTSbiChoXiM75oQGAOVYlFUNIKu2Jg9VZ-ATuBf8_V-78LZFPvGVnv7mt0TcnfrAf0tn5Cgdgm440FlhEbKDEsrvEHq0aOAPCCJUPRwbMPhVwS6uASg9JIvh7XQMRPTbu8Sb_C0oSzvS-etaPDEcjEjT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=VOdN61tjPdxNBpTbPALkZDF4OFl2V65AoeilRGEza3ZL_oHq90e_k_byR1RXVs4lxcpI0k1d6Ps6p-sW6TtwbkFfs-ujUBvoiYsV31UdSzk-LZH1nAGj-4W1zjy4jxatui3D8U50jjoC9KIEJwXs-VGggv-jvpKai4TRLkyG5-htto8TRIMk1U2NMIlWf7VBKrX4GgeWwu0XX4N7TRtxwRBm-FWwg-aZUDzy5xNa105ZoribWBYMRg4LfYJRyoVUnqwV0MabwSSdF2wlir4DOGxX2DfGrVUxFiMzu3EZ3h-1yq2WQkfIjYg83Aifhl3j53my_BBR6XQVIJhthNCF3E4A79SkNRVqPtIKbc7EI0xk1SaOZsCQpg5UcRGgoVF7SXVs8QNJC_D-W0EtnE9EXytjLpT34u_wHQ5Jk9fAPYOMRq2XiWJZZFK_-f11OrgCVrIBUzjnBwEcEUm1PthEzWZKvtYT__5QH1P1hasztMZX8QtvrkHxL7BoiARzeJn5hmIuqlM_yJiBc2SWiii4ny_kIFQzlmxwKNEUc9Lkh7ShgW6vxk5ZNKoZVD8Ac4IRnipJTn3iXEJvIcar0CsYyRJpd1CJqor4nK5c3qfhsswMI0M2C4ZXQVAgK6sWHDT3HCg7GBcElLXIrMGN9zTPqwcAjGktPc-nMuia7QBnPQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=VOdN61tjPdxNBpTbPALkZDF4OFl2V65AoeilRGEza3ZL_oHq90e_k_byR1RXVs4lxcpI0k1d6Ps6p-sW6TtwbkFfs-ujUBvoiYsV31UdSzk-LZH1nAGj-4W1zjy4jxatui3D8U50jjoC9KIEJwXs-VGggv-jvpKai4TRLkyG5-htto8TRIMk1U2NMIlWf7VBKrX4GgeWwu0XX4N7TRtxwRBm-FWwg-aZUDzy5xNa105ZoribWBYMRg4LfYJRyoVUnqwV0MabwSSdF2wlir4DOGxX2DfGrVUxFiMzu3EZ3h-1yq2WQkfIjYg83Aifhl3j53my_BBR6XQVIJhthNCF3E4A79SkNRVqPtIKbc7EI0xk1SaOZsCQpg5UcRGgoVF7SXVs8QNJC_D-W0EtnE9EXytjLpT34u_wHQ5Jk9fAPYOMRq2XiWJZZFK_-f11OrgCVrIBUzjnBwEcEUm1PthEzWZKvtYT__5QH1P1hasztMZX8QtvrkHxL7BoiARzeJn5hmIuqlM_yJiBc2SWiii4ny_kIFQzlmxwKNEUc9Lkh7ShgW6vxk5ZNKoZVD8Ac4IRnipJTn3iXEJvIcar0CsYyRJpd1CJqor4nK5c3qfhsswMI0M2C4ZXQVAgK6sWHDT3HCg7GBcElLXIrMGN9zTPqwcAjGktPc-nMuia7QBnPQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=j0xQdmIlYh5nyrBEqipiFgxYXlx4lSwy4eS_jKD65fFdnHAM61svC4__9vVFDW9b2_YczkXdfNrkcbG_-pXejZd53to6JDxYwRk-BJH_vMdgdd_dKOhaVaGNxSQIwObI-wSKWoAistqVGLA8k2DQgqiXTvVyBeXpkc_OnnBFQjyesJeiNqrccMtabTypWKBDFOwm4qgZFw95ZMt_yVmAsqw0Wkltd2h7a8R2PrcuUpMCtZYBfkLJBTsG0nTKG6Mi7LzniB3oY-L2NcCmyW8JAy0sUaaYFccODDl0-wwZ-mSyjKlsH03ssF5FRKxFb5eukUEXNp2JMRQRezENyTaDGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=j0xQdmIlYh5nyrBEqipiFgxYXlx4lSwy4eS_jKD65fFdnHAM61svC4__9vVFDW9b2_YczkXdfNrkcbG_-pXejZd53to6JDxYwRk-BJH_vMdgdd_dKOhaVaGNxSQIwObI-wSKWoAistqVGLA8k2DQgqiXTvVyBeXpkc_OnnBFQjyesJeiNqrccMtabTypWKBDFOwm4qgZFw95ZMt_yVmAsqw0Wkltd2h7a8R2PrcuUpMCtZYBfkLJBTsG0nTKG6Mi7LzniB3oY-L2NcCmyW8JAy0sUaaYFccODDl0-wwZ-mSyjKlsH03ssF5FRKxFb5eukUEXNp2JMRQRezENyTaDGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBid_fV6f_Gbo6UW7r1rO94ajLi8Hm-8auY5DTi-WG1eVmGVTTCJxaIuwU6ZFYLf_Imb1hk0eUkAF9sQifRdgnMGrPqfT-207Bxq6h4DLWJRa7Gs9UiToSl_CwRDyXs5nL4KlqkGYAk1D66pKtN9gu5KhTXcAp8OzNU-5x60ISrESkFnQA8k8DoXRLHoZ93IN95_obanuNSEHc-heBNTOifGVF7XBajyMRHnnlArB0oijDpN1DBcwYttUjdJOzIxeDbXFOBQhhcyEkaOKLdfJeW1q_z33_dBWp1a0EOufcvbRqzI9y_zTsHFNJkCPVAM1t0M2Yipdd8ltZHoKz1xjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQcF_Y_IVO01khdW9uf8-91RWGB8Hks1c5YTbGij_kcToT6PCAU2V2JAOgavIpirVwyXl6yABBsCCr4e8uSG-BoDQnjrQ3qk83XctC4IOts6yuY6Bj2C0hhrvEF8XzGDAeMlNysrbidOYqXxoa9zUKjDX1bBLtnyO5wqVRYoe91M-NtEw_JRGwpJQ7X4a0H8UAsNhs0cZLGMKucd8xNpot1MbydjLcCZA4qksBo1_RRPIU6CxPJj42mypwQ3Hpw-Wc72Q0xtMYaPvDKvBNVlBM4VoNin_I14m6itaoVt-KOxp0uAW5_BsH7jtouyif_mT4hDWzNh_ECH-tZfRwWuZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=Aq06y5-AS5yWjU19l3uxI6FdOCQ7CUNAkwFyz-rX1eG4kvHSMWCOtP4GF9T8E2phIM32TgDwjMWcxs6iKp0Wv1B3sxdIXnTNdJ4VUcwVDz0po2OQ80k8NN9Exlsy5XyGCX3BRxMtR5m8DBi4LLLCuGqPeVdB_cY3N4ZQopERyTW5yQFLZL5VqEJPpxc-sEHjebDNQD30HbkrCF6MjWefPqB-jv6TBRZCyvExuLhVSZXjfZ0wku0oNa54r_LopNXcTYmMjV64VehtFKugrShiM1NFbCK2fFpXioLVNcdnJBdCuQW_b89W0bsq54bQvpfDRvG5o51wPa94ptVSDqpRRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=Aq06y5-AS5yWjU19l3uxI6FdOCQ7CUNAkwFyz-rX1eG4kvHSMWCOtP4GF9T8E2phIM32TgDwjMWcxs6iKp0Wv1B3sxdIXnTNdJ4VUcwVDz0po2OQ80k8NN9Exlsy5XyGCX3BRxMtR5m8DBi4LLLCuGqPeVdB_cY3N4ZQopERyTW5yQFLZL5VqEJPpxc-sEHjebDNQD30HbkrCF6MjWefPqB-jv6TBRZCyvExuLhVSZXjfZ0wku0oNa54r_LopNXcTYmMjV64VehtFKugrShiM1NFbCK2fFpXioLVNcdnJBdCuQW_b89W0bsq54bQvpfDRvG5o51wPa94ptVSDqpRRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrKBnfq7EHz3rcvZR7yl0vj-8ccMddNY6-6bxRFopG9vscgQzgVChDcqNYn3X9Ap62sUoXYZR0NAIbFzDLZZE2pa-S3SNO5uws2evcstHsVQraPgaJV8ZN25Be_QC0Ns7Bs-YAyPwIYJrrivuQrr4xuop5zFpB2YAIpyMYbeQAjx0miEqVVYCr5uYTWsHfmNTin_HsKSj7IQsiwzyjs9ZwbOo2zaA25DCRsh9DM6QDIpTYgKB9AUXMPljOpW7Ex79x23zhTaZoVlvohjXhSkUXaVeDR2gGWLfRq54jO9NmmmBXo-mSpIJYilAb_KbkR248HBHQ-Gpkn_KjSWIT2gDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACfhOSmbQAKe4o1ItDndz0L5Q6Z-cvD21crjrXZUiGW163SkeY5pE4Aqkmi6OaJ8bCsVIgi5VBkdxOLgTjlXiEiPnUxBXUvYeRHSnnU3PQAYj567bEqLU1WRy4BJjS5M7rvCFTJpabu4ooaKmvUEqQc2UuQHu8RyBUDs2OeLJHJsuZFN_Qa7Os_RU7nyfsCsV6S31IDGN69yVHbC7Lb1se3szYOJ2xnwOEJ4sE-9AGT4TEarPTitaXqZSLZ2hGhWUpnPCdjjUiRs4tzbmzN1Y_4_5nCClms6ry-E6Smzghl0dr7BG46iKnNrnne8JDueDWAzZ5wTJNGKpfMIlmmJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3QS_lOLP4gEV4OJQ4hkKMoA1Er0by3vuXBP_3daRTQ4JsC3RQsNXjCJOa4Kzr-iHYU7kRCtV08IK7k3bRwG9eoThCpEfwUo6jgpLwB3wervrObU88XjU59fFa7KFDPqKejqbwqkbKqUSC-XIN6AYsLCbbBwKCx3Z_2qLBbpzzbACPugOL_E3aWBwKN1ni43Li8em9TYmZedI77hQIudEipvwD4xCJt1j5Dzz_1BTYw-SWQjKVMnvKcKeFicyAcsStKvnb8KSjJ-I4nByyD4vWyi1ZUm5SD9P0zgE1RgalabAu0bCD2KNblYoneUjMWqpSOQG7tHcpRA4SJHzRkrKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCc4RlTe9tBrThx4umV70NGRg52T8FGfvgdTL3M99WkN4KPevKyK2ECGZKG0xO31lqyjJnggHJMLHrLoMa86gse2BeAu8N2rOcW_lOv9frVc9ZX_I8h7mn4mN-lsoDpLuhL088TNIMa9_fqZCRr-4daJf9k_efOZeUBHiMJGtvJiJNgx-4vSj_yjUm0k72pWzCEpbI8EKbfCh3qCQN7ttCmJRd-Hrbko_Y_AwR8oP__cSl2hVlNeJ35DGcUpZFFudp_ShWYVMNXsJtqMNBuWOfFSC0GWRbVRFojHRkiL-DmdBLxeuwY0zflwiZHpekGFDnFFDbv8AY6N0grF-2GvNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUbFJp_uMrgi5fX9ixwjU2v00MH4K4lN5WA7T6h-j9h3bYdqZhwBx_JJlYMP6QkjQxLj4Z0iLWCb2B1MEkgwGNfALHJkjl0u9vjYtKdi3WvjjN92HeGbX1CEJkRSWQJDwKbm_19Tq2f-Z9Rr5WDcSykL62mSOfMRMjtPz0Wvd8Pd5JxbInJ2UZVZzdE2GIs8ykinb-2BVtjn2dYdlolZMIqR0OlPTzu1aV3xBLjPr37CKSgJypqnAdkGAdZNvdcnvcouy5H9aQwRALGo5wVhq_dvsCEv_MHU3VLWdHHXbiyLwHGJ4lDsFBViPduoKbdYUQN43JWJZq6dO1gq1n9VXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5SSrf3G8Mofu38CJU7gLw8U5mRsSWRHCBG0-_9bhs0IE6fFNcAQXP54pWo2NI5AUEzvEPBaUbi0lx7h-PmU1PRDQyW-zosgQZdi96B0FHl7CTyNaOAPMm9LR-LdZCkQbwhnzZ9BPH4y0-jMOTYKVIiRoCFHo1C8PQMacFyBouG3Yr2o6uceyMjbawk6qVpQnlrOrZbnriKdfwx_SvNsKvkgPDJSHMIOOxIBXpbpTag8Cyl8hCxSH59Nh15p0OXM4QAs3PFe7FCxSIMMp8s9c59odxPId7ujK9K6NFg9fQ1fK7osp_hOq1MhHOYvNFykNoYE1BJoz5B5QssX5mjfzG00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5SSrf3G8Mofu38CJU7gLw8U5mRsSWRHCBG0-_9bhs0IE6fFNcAQXP54pWo2NI5AUEzvEPBaUbi0lx7h-PmU1PRDQyW-zosgQZdi96B0FHl7CTyNaOAPMm9LR-LdZCkQbwhnzZ9BPH4y0-jMOTYKVIiRoCFHo1C8PQMacFyBouG3Yr2o6uceyMjbawk6qVpQnlrOrZbnriKdfwx_SvNsKvkgPDJSHMIOOxIBXpbpTag8Cyl8hCxSH59Nh15p0OXM4QAs3PFe7FCxSIMMp8s9c59odxPId7ujK9K6NFg9fQ1fK7osp_hOq1MhHOYvNFykNoYE1BJoz5B5QssX5mjfzG00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnDtSkyJso1CqxxKYIs1l30zxzzvfDLF97wy2XMzA5N_brT-tAkRx_8jtfDUkotuWHmM3fSvdZq8fK90XUK-CrlcUB9ehjKLMN6ArzUSDFheV3VnB1TUR4ii6gRSYxEcTBUanKL3ZWY28YX_lkt4hzyf49ICrPa6vGMXz247gnvZV-w-w4n38Y1--aUpULV1sVQN02oLkzzYrmUUsWu30HO6G8Gu7ZT9J-dt6HGHgT6ZvdELXjtdgYRxIevbzTS4JLTiGXGMcl0VB81JRAxyStGtxVUU-TYCVXAWRLRvjG_9osn1bA_F8KodjZ9yoFspcaTJ23dq9ujLrSS-QvUKmKTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnDtSkyJso1CqxxKYIs1l30zxzzvfDLF97wy2XMzA5N_brT-tAkRx_8jtfDUkotuWHmM3fSvdZq8fK90XUK-CrlcUB9ehjKLMN6ArzUSDFheV3VnB1TUR4ii6gRSYxEcTBUanKL3ZWY28YX_lkt4hzyf49ICrPa6vGMXz247gnvZV-w-w4n38Y1--aUpULV1sVQN02oLkzzYrmUUsWu30HO6G8Gu7ZT9J-dt6HGHgT6ZvdELXjtdgYRxIevbzTS4JLTiGXGMcl0VB81JRAxyStGtxVUU-TYCVXAWRLRvjG_9osn1bA_F8KodjZ9yoFspcaTJ23dq9ujLrSS-QvUKmKTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=R8N3J4cMTeUrHgTFXFmNEQkaIDeEFpJ2Gz0JU-vp1u3UfYuK4SPTWiP3M4pYfmPhjbRsx2NusYel3g8zIc6zbl7BrI-kxvBInQOAuHbIXfwworA89Kaqr3khuxqmQZYcNEZgIt1EW2v8ZsbVy-NvFjqD2B7JMExP4pSxZDn7Z_LE4vzTzyUzTZiiSPQ5eVe6pkweeIwKjU1kX8ZyWUJ_ePm1sb8mPNXsbkvN444tsxcNYl35JmuGoUit_-uCSnvLZfl_YJ-BrUvtrnW916EEtEwKfz5WcYQSbwrGGrIQXe2eGsAixwbKk8c-ddylGvbdI_2TN3uIdJ5CnBlA0YZKAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=R8N3J4cMTeUrHgTFXFmNEQkaIDeEFpJ2Gz0JU-vp1u3UfYuK4SPTWiP3M4pYfmPhjbRsx2NusYel3g8zIc6zbl7BrI-kxvBInQOAuHbIXfwworA89Kaqr3khuxqmQZYcNEZgIt1EW2v8ZsbVy-NvFjqD2B7JMExP4pSxZDn7Z_LE4vzTzyUzTZiiSPQ5eVe6pkweeIwKjU1kX8ZyWUJ_ePm1sb8mPNXsbkvN444tsxcNYl35JmuGoUit_-uCSnvLZfl_YJ-BrUvtrnW916EEtEwKfz5WcYQSbwrGGrIQXe2eGsAixwbKk8c-ddylGvbdI_2TN3uIdJ5CnBlA0YZKAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Heoppu-pSVXw0mI_UjWNFFRNYM1DyJq6sEVY8xgr6Q_MCkXkurTIs6It4qaOcZYsPvQiudGa9bRqCtxJG00bCOhapz-59hkSGhI7rw4oAHHU0V3g0jTwO_fTJ5JA6fN_jhdr3U1P7K8Fi-ATEGqCB3JG13bXyWiZKWBOYV0E6OdtmoHh8hUlVuVmI_gatkmmX4pLO-mKfXpX17VDsZGcHZnciIJ7c-H2CYsH0GtwLhLlIATBYTVQLjEal2eZS8TEwIrTrxDVMVJmWdf_bMCpcnbQBSumchoLNRo6D59sZvwKtgd1_B1652cgrxDkz_LJVnOKQ71aHbAdB5dDRbhl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVzL1V_zNL49Jg0NRHgChIA9NIHb-APfCI6tV1O-pGOyqEXOpZ-b9TmLHh2LagtfUya0_9r8PFJBhuGbR7JNxHsQzW4C9u69pS9-HJPlr1ibpMXkSGZQkyfmkyYKL9fLuPSF3XqJobj6LWNbDYA0dtaVMPGjPz6ys9jq1ocIDZWxN9t0vV4P5sYOsnVZFyHDP25ER-QH6EjIiOG1t31kw2FpIFQAkIckD0YpUXAqjRWaIs53KbHUniyLlkhHZ78kqdHErtmQ1xP_aLQKlLWxi6-WoEhH5JMB2CRJkvTk02z5YeJdbbXCpQHD3Xs1UvesZYWkkqsA05l8mz2-Muajeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
