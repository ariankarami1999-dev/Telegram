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
<img src="https://cdn4.telesco.pe/file/SsG_OQltecCAEmvZDhhlhhQWvM4D5lOciii9HaNkJHZ0jAUShxM6At604Kt5C8ezAocvFjWxFu8DnKpyOIs7uLLKaZ0Hd6_zVqfIcmQLOnNPokQ2UgFV3Es7HVkUd7D1_h9nH1shIpSi-BvqFmgzlsraJFlzomxVgKgUhcle7vNJ5w_biAEcVxJY9nSuaT9g2zoUbqhoJ_TCBD4CShgy-nICgh-x7-LSkl1tisu4womUOb55-pB3UIHAakY0R50z9CXp5hknr3YYCQ_yD6PZrrfhejbuoQ4-wty0lUByEBV3tdTPC7OpKQuVkNZu9jB7I5aVq5ExNLFjOXUJFsbXvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 15:23:01</div>
<hr>

<div class="tg-post" id="msg-77611">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3K7E2MCN35a5wKAbofWvr7Dc2Sc0AzslMrxh544joD7QI-Zv1rLQF9mYqZPUbCFRuRQq8R39vUczAV1zy4atR_LqOoW3TNFmkFwlL7laMNNgnlCM2JjOcqIbPlNOEYEM-pVrm4qpXaOir7rJCgey_6tWYVrps5p20nVnNm16FgRpeYi7vvHnrfHZKjAGe2hYaIMSxm4EsYNRzYURTMw7Nj6XgKOxvNu4hm4KFj2vwSFgQJP6aNOtFnxLKQJ9x-0HucsjxRC1lhUGVC5-k9rQ7AkOfzclgwapfKUYaFa3bsyUoqZkD2qym5yAXSbFLfFwEAKeWRAmJGr61DQHbbzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/funhiphop/77611" target="_blank">📅 14:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77610">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YczWgA2KZYSNilyGNB_6TZ0CBXSTv6-dZmxRnHX-yUnTsE11sRluPB_JbqDeQoQrKLmSoki5btzizewoyH5UXemDsRPl9bZPog9UMkdUxd6wt5mnOK1x7bMvBQnd7Rl4paymFspZpz4dg49P69Pq_CflGAHyZajKvhXGWLcubDC5Huw4NnJobeAKhHIKWSEnSZYEaTLdcaD7dJOTkq7epvssjSnPxC4mKli4MfW5InR23Xr3K9DmTHpthgpVQStUkuqdIC7pC2USt3g9BFok9wUbMFIT_BqQQhBmUY1gI7laRW5u5MdF0xOtiGdWRyIM4g6Kvo5rLwVtXmI3SKcb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب داشتم این صحنه رو کابوس میدیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/funhiphop/77610" target="_blank">📅 13:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77609">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE7lMP4FDj83iWEtOWzOjBPHbKcnCha5Z9ODup5weG74TUQSRaR3H23zzBnaPMoXgP02matzDb3zIzRkwopEJae6WYqVfiixpuham0xH--nmhcAD2n7ifB82B1S2qTz7eRWHMz0synDDUyvj3h1N__KIgNHGIgDrh6kajzUhDu5udguIntP027NuZ4YfukUZ2_jMyAhmkMndLxHWuzI5EJK8t7Q73ycEB6VBzAfYUTvBl2NCeZtNkQan3dPYw9gOKnIBLqMq8ucS701hiAUZLTq7rn4BL_6u9-OEKw5A5dtkDEDSu1Mki5PiCgSA7U9nYua38qwBr-pgCsBqXSl8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 گیگ فقط گیگی 2/800 تومان
💥
💥
💥
100 گیگ فقط گیگی 2/990 تومان
💥
💥
💥
50 گیگ فقط گیگی 3/600 تومان
💥
💥
💥
به مدت محدود، ارزان ترین قیمت
❤️
☄️
10 گیگ = 60/000 تومان
💵
20 گیگ = 99/000 تومان
💵
50 گیگ = 180/000 تومان
💵
100 گیگ = 299/000 تومان
💵
200 گیگ = 560/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/funhiphop/77609" target="_blank">📅 13:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77608">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک خبرنگار آمریکایی:
ترامپ از تبدیل رژیم در حال بررسی سوییچ سیاسی به تغییر رژیم کامل است او معتقد است جمهوری اسلامی هیچگاه ممکن است حکومتی اهلی و عاقل نشود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/funhiphop/77608" target="_blank">📅 11:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77607">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نقض نقض نقض، تا روز آخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/funhiphop/77607" target="_blank">📅 11:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77605">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دریانوردی هند : سه ملوان هندی دیروز در حمله ارتش آمریکا به یک نفتکش نزدیک تنگه هرمز کشته شدند.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/funhiphop/77605" target="_blank">📅 10:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77604">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHy8ZMN6K8hY-Bx1yjcEGDpdFfPcMYS3T231Hn4VmwoEBfcaRbsIW9M8itNcR1bUmUWcv-F64XtCiCYNM_EYCpm3sPOFLN1snFLD_4ZaH03ayhVKI2PYzu1-8C85C19tUxYI70-xbzsrNbnnKNwejM2R21PYtEGBkZlMePajXVXyylKdogFnv0ymrO6ZZFVrn1qnHwG3nn5fmCm4OEPQ_Jpq58kmOpWGuNySQGjR1u0gZGnlqWjmBuZ6Jj-MfniD235HqGNu7yjMBM1zugGFEvRmTyJDCzL0sEeeeeQDZD0_m_g7H-NaZwdQQRZVxIwIs_Sa48_inz_I0H_JDRazLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت یاس از ترک جدید تتلو :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77604" target="_blank">📅 10:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77603">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77603" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/77603" target="_blank">📅 10:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77602">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC_iEakhMKaK8uKr5s7JGkxMWrPqMJtSduxtyVGWFvT652SH4-pYG1hr2WH9PxlUxeCkufhRLCkpdNNODRWliNEspskKRikqvnNv5cC6TetSaV_OBhUGar7cyFQYvJn6_bX-NvtiJXqeLFElRe378CzU23WO4HwhuYW6ztAN9BWDg9yuw1cTSXVbHU1DXGPlC6VV_fKGgMpXfm2Sh_0mWIx8qiucoaCci_rcjmgStl0xSEWPVwPe-HFOwHccQ312JAAg-1imYFMkBu5m1QXgwNT5VCI2-JCK3WaX0fiD7at5t_zN9aj9Hs9Ga--tnYTkdPkc-OxNKpyrNlAOqmpS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r21
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/77602" target="_blank">📅 10:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77601">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57acb15649.mp4?token=ksDzE-CLvg1KrG7ip4Vb_f54c8G-IzvmScrsW-6izI02oIX4pNPafwils2U74Sgx4u34QskHV6tKXA7bcn1LnPKYsZrBBJC6EijUDgwcm2L0dO6uKqAP60H3GiAK8oyu7tR5p9NfK3mkchr8-MrQnDAGylayJTLLcuKkqwkcdAe18CswalyH2HcjCEhCCZK_bZ6l2oIb5xDQa2kzEqktGqCymW420q_TA7Y-YDBXJwVm9C8tA5a769AT-as460I3UFw383WQVHcEQ8xtf06RVKhi_9S5CjyOay888dpmsSAPS12zD-_sdqVN1KzMg4SQUWsGQIvEx95xJ9CKttcdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57acb15649.mp4?token=ksDzE-CLvg1KrG7ip4Vb_f54c8G-IzvmScrsW-6izI02oIX4pNPafwils2U74Sgx4u34QskHV6tKXA7bcn1LnPKYsZrBBJC6EijUDgwcm2L0dO6uKqAP60H3GiAK8oyu7tR5p9NfK3mkchr8-MrQnDAGylayJTLLcuKkqwkcdAe18CswalyH2HcjCEhCCZK_bZ6l2oIb5xDQa2kzEqktGqCymW420q_TA7Y-YDBXJwVm9C8tA5a769AT-as460I3UFw383WQVHcEQ8xtf06RVKhi_9S5CjyOay888dpmsSAPS12zD-_sdqVN1KzMg4SQUWsGQIvEx95xJ9CKttcdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/funhiphop/77601" target="_blank">📅 09:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77600">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی: در جواب حملات وحشیانه رژیم جعلی و آدم‌خوار آمریکا و به دنبال افتخار آفرینی های سحرگاه رزمندگان اسلام در سرکوب دشمن متجاوز آمریکایی با توکل به خدای متعال، با ۱۲ فروفند موشک محل استقرار جنگنده های F35، F15، F16 آمریکایی و همچنین…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77600" target="_blank">📅 07:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77599">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم امشب تغییر رفتاری از سمت ایران رخ دهد.
اگر این باعث نشود آنها پای میز مذاکره بیایند، باید استراتژی خود را تغییر دهید. تمام توان خود را به کار ببرید. آنها را از پا درآورید.
بگذارید مردم ایران به مرور زمان کشورشان را پس بگیرند.
اگر آنها همین الان توافق نکنند، باید اسرائیل را در مسئله ایران آزاد بگذاریم و خودمان هم از نیروی نظامی‌مان استفاده کنیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77599" target="_blank">📅 07:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77598">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75edca7aa.mp4?token=bEzygzKIJJCCGJ4lvUyR9mI9Vvj4ib_AZujmyO0S0xiZdzUI3KSjiCfUg1OUfRH2weWg9z9cLXM7Id3kF2vJtqYgY9iRY6jtvHv7TMtSNi-t15dVJ2QYTJ9PPpArdzRzNF0QJXMqvBHyMH1H34j5l7cB8vmh50woscA2HsMg-l_mYvPldtxMf9hX-OXVlRqpjHJQcVDHpCgKHh74_zpb5lKJly3Ksf9c6P22KG5pZ9N7X2UBWp_Xl3red2eWM7xNEW-o4lvqOb9D-nnS6xITlyAfYvMNI6A7bem-Or8rNn7Xf3SgiOhTtTfXcnTGvayK-yNMsbTeIhEJrddnVNbi2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75edca7aa.mp4?token=bEzygzKIJJCCGJ4lvUyR9mI9Vvj4ib_AZujmyO0S0xiZdzUI3KSjiCfUg1OUfRH2weWg9z9cLXM7Id3kF2vJtqYgY9iRY6jtvHv7TMtSNi-t15dVJ2QYTJ9PPpArdzRzNF0QJXMqvBHyMH1H34j5l7cB8vmh50woscA2HsMg-l_mYvPldtxMf9hX-OXVlRqpjHJQcVDHpCgKHh74_zpb5lKJly3Ksf9c6P22KG5pZ9N7X2UBWp_Xl3red2eWM7xNEW-o4lvqOb9D-nnS6xITlyAfYvMNI6A7bem-Or8rNn7Xf3SgiOhTtTfXcnTGvayK-yNMsbTeIhEJrddnVNbi2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
در جواب حملات وحشیانه رژیم جعلی و آدم‌خوار آمریکا و به دنبال افتخار آفرینی های سحرگاه رزمندگان اسلام در سرکوب دشمن متجاوز آمریکایی با توکل به خدای متعال، با
۱۲ فروفند موشک
محل استقرار
جنگنده های F35، F15، F16 آمریکایی
و همچنین تاسیسات مهم ارتش تروریستی آمریکا را هدف قرار دادیم و آن تاسیسات و مقدار زیادی از
جنگنده‌ها را منهدم کردیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77598" target="_blank">📅 06:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77597">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU6WqQgnd8NoiKqCeiwmeLRhYAa9fVckHxlS_ExsvvF77mc_wTADDRa1LhdsCfazKHlD7QySt82nu-uf1QhyOQS51dYLR5n6G2hRQtTuNLK5oe2qY30Es9Xd_vV37EyY5t_WMTLakLStuRFwAVL53mJgjSXrq4KRn3Iw4ZsCerqeER1x1UxCNfj0gsFpKrOrgtiP3jykglsOVxykAtgEdmP8RpTocBMDGhHGwo5Cg0yFtVYgd_5yz8w0CzNAk4GTfIy7pjyp1Y34IUrpNKQ0Dt1YUnNtiqAmQIWUo4-Nmct0xsTxmGouwC1UN9SvR-pBMkPIUtOqjr1jaoC56YwXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل نگارش کپشن
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77597" target="_blank">📅 05:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77596">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">برزیل ۲ ۱ از ایران جلو افتاد تو والیبال   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77596" target="_blank">📅 04:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77594">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8c4cfc6c.mp4?token=mY9bONupRNNbMzDxRwWdMgsJhh1h7a3OPkfFQlaFoDL45uI8qzD8TEFqOTjZK_vdUI8pFfNJYeGtsob8-64fj9vS9Qm4MjVLP3UddWkJOiSc1ECPLHKyVQFQrJI6C0rHRM5Uo6uXmUSOftKG4mZA8nnfdc6MXdEXbvXcPzDfFF2i3AdeZpGnhhhAg1K4RHHfUeTpjLM_uO9z1775Dax5NPxnZ5C0OsUD6EGkO24T9oQ8Pqv4FuTHjggCdtU1Tr-8WSNECrDzfNLXDEkOUrKuJKgqc1whUQY4fZ8Txgrb6Kx8eZYciq6xI0uJztRgf40LY0TiTVdIr0hxqDsS_8tPqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8c4cfc6c.mp4?token=mY9bONupRNNbMzDxRwWdMgsJhh1h7a3OPkfFQlaFoDL45uI8qzD8TEFqOTjZK_vdUI8pFfNJYeGtsob8-64fj9vS9Qm4MjVLP3UddWkJOiSc1ECPLHKyVQFQrJI6C0rHRM5Uo6uXmUSOftKG4mZA8nnfdc6MXdEXbvXcPzDfFF2i3AdeZpGnhhhAg1K4RHHfUeTpjLM_uO9z1775Dax5NPxnZ5C0OsUD6EGkO24T9oQ8Pqv4FuTHjggCdtU1Tr-8WSNECrDzfNLXDEkOUrKuJKgqc1whUQY4fZ8Txgrb6Kx8eZYciq6xI0uJztRgf40LY0TiTVdIr0hxqDsS_8tPqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام الان با انتشار این فیلم مثل دیشب اعلام کرد که فعلا حملات «دفاعیش» تکمیل و تموم شده تا ببینیم چه پیش خواهد آمد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77594" target="_blank">📅 04:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77592">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">احتمالا الان آمریکا داره خود زنی می‌کنه که حملات سپاه به کرج فراموش شه ولی نه ما نمی‌ذاریم.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77592" target="_blank">📅 04:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77591">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قزوین و مناطق مختلف جنوب کشور باز صدای توقف حملات اومده.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77591" target="_blank">📅 04:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77590">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UF9M0465eBOa_3Ei9bCbi6UBjMOH2E3CFP7V5ldZwfwWr0G-_5VoatU9dOsobtTceZgMk1-VDzJtagSX2NIHLcdHB0tStb5rVYB5Lm6c6pJSFsuVRTZHm3aTMbtAAkkgoMmep4x0E61kyg-89rc5RCGfrYKUPDPkGIIt9M6_7zm2AXQqAnpQ5CZ4OMmE2VxIX-id-qKLknX6lDOUE-Vrz90uZG-iwt6xUEjubeK2uT92Jp8XkbB51koKbYbs8jfXh5P7Cwn84eqrS1apm4aE1nY_sOFTX7-FxlD6zsZ096kX8UgwoGkkfFEU5Y8pKLd--LutQFYnAPcablFBhaPFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید مجید بالاخره بیدار شد:
تنگه مقدس هرمز را ناامن می‌کنید؟ از سراسر ایران منطقه را برای شما جهنم خواهیم کرد.
این پاسخ به جسارت آمریکایی‌ها در منطقه است، ان‌شاءالله.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77590" target="_blank">📅 04:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77589">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ: بمباران به زودی متوقف می‌شود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77589" target="_blank">📅 04:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77588">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">برزیل ۲ ۱ از ایران جلو افتاد تو والیبال
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77588" target="_blank">📅 04:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77586">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اوه اوه  هشدارها و درگیری پدافند در بحرین.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77586" target="_blank">📅 04:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77585">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اوه اوه
هشدارها و درگیری پدافند در بحرین.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77585" target="_blank">📅 04:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77584">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">صدای دو انفجار ناشی از حمله‌ی مقتدرانه‌ی سپاه در بندر سیریک در استان هرمزگان.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77584" target="_blank">📅 03:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77583">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">صدای دو انفجار ناشی از حمله‌ی مقتدرانه‌ی سپاه در بندر سیریک در استان هرمزگان.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/77583" target="_blank">📅 03:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77582">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">صدا سیما به نقل از سپاه پاسداران انقلاب اسلامی: مهر نیوز راست می‌گه، سپاه پایگاه آمریکا تو بحرین رو با پهپاد زده ولی بازی رسانه‌ای دشمن کاری کرد شما نفهمیدید.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/77582" target="_blank">📅 03:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77581">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946d468c47.mp4?token=m8H0u2pEqkggsKe3O0WPVOW8_Bb7K9MDva0Oxxkm7mg6glDgDt928AqDBJ2wh7KFBlbYX09XD0QxISDLVE-CfJaKv0TDkqOKa3NuHXmAdJHrK-R-1FoVckY-RtltJ013Y2uSWTp9K2eI1YrkIgxeBvAWwIVCuHb8AC3293GCcaUqxxxFrF5OHwj5h1vao0KQMPek9rBqEgE4xHpTuqL6kJJaAhF9RBxjEkOxSVxYAFmxLbi8mWU1fxaxMd0pKQq4dQOlihHZyM8m9OkPvxYgc9mk7AR09VaT1fv2a9QG1ugozo2roc6kWbnEn6H7GWj6-jLZ2V4qTWYDEM-rKITg6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946d468c47.mp4?token=m8H0u2pEqkggsKe3O0WPVOW8_Bb7K9MDva0Oxxkm7mg6glDgDt928AqDBJ2wh7KFBlbYX09XD0QxISDLVE-CfJaKv0TDkqOKa3NuHXmAdJHrK-R-1FoVckY-RtltJ013Y2uSWTp9K2eI1YrkIgxeBvAWwIVCuHb8AC3293GCcaUqxxxFrF5OHwj5h1vao0KQMPek9rBqEgE4xHpTuqL6kJJaAhF9RBxjEkOxSVxYAFmxLbi8mWU1fxaxMd0pKQq4dQOlihHZyM8m9OkPvxYgc9mk7AR09VaT1fv2a9QG1ugozo2roc6kWbnEn6H7GWj6-jLZ2V4qTWYDEM-rKITg6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر: سپاه امشب هم اون وسط مسطا پاسخ‌هاش رو داده موشک‌هاش رو زده باز شما عقب مونده‌ها داغ بودید نفهمیدید: مرحله اول عملیات های تهاجمی موشکی و پهپادی هوافضای سپاه انجام شد.  پراکندگی مبدا شلیک ها و فراگیری بانک اهداف، جزو مهمترین ابداعات عملیاتی سپاه…</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/funhiphop/77581" target="_blank">📅 03:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77580">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ممبرا می‌گن کرج رو ۶ بار بد زدن.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/funhiphop/77580" target="_blank">📅 03:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77579">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ممبرا می‌گن کرج رو ۶ بار بد زدن.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/funhiphop/77579" target="_blank">📅 03:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77578">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کرج زدن؟</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/funhiphop/77578" target="_blank">📅 03:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77577">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا می‌گه ما پاسخمون دادیم تموم شده رفته شما داغ بودید نفهمیدید: در پاسخ به تجاوز ارتش تروریست آمریکا در مناطقی از جنوب کشور به بهانه واهی سقوط بالگرد خود، برخی از پایگاه های آمریکا که در منطقه که نام نمی‌بریم هدف هجوم قدرتمند ارتش قهرمان…</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/funhiphop/77577" target="_blank">📅 03:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77576">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ: اگر ایران توافق نکند، فردا شب دوباره آنها را به شدت بمباران خواهیم کرد
(I will bomb the shit out of Iran)
.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/funhiphop/77576" target="_blank">📅 03:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77575">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zlftju7s01rh-30dWZ6FJKk0XqwU7mtJBIsaF2_PXzLS3dSZ_LfpOWMdYKZ6L4K5pU0a9yptPEVhXwE9RafxYlKw0tAjDtICPjS5whazo5EQsLwX_EWwdlcBmKw3_4hh0xHLwPZvd6z80hxDPc3WgE3nawKPfTjfLXVnirb1bodsGL8lpf0kpUnNiG0qwxfZUj5A2EImh6BD6kIuaNqKCxNbo00rGCeS7hSlDUeEuld7JZUnpni3rU6FDr_eQ01QFLz4RAdjHgzTKjfUgC7Za49Mb-mPPuPD-lm6U02eVWzs2kilr0_sGP5ewrbv-PzSHY2_Q1dITidsXdqwb_b4LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه خاتم‌الانبیا اعلام کرد از الان به بعد تنگه رو کامل می‌بنده و به هر کشتی‌ای که با هر ملیتی بخواد رد شه شلیک می‌کنه.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/funhiphop/77575" target="_blank">📅 03:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77574">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ به فاکس نیوز:
این بزرگترین نقض آتش‌بس در تاریخ جهان بود.
(ولی هنوز آتش‌بس سر جاشه حرومز؟)
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/funhiphop/77574" target="_blank">📅 03:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77573">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ: من مستقیما با مقامات ایرانی صحبت کردم و آنها از من خواستند که بمباران را متوقف کنم.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/funhiphop/77573" target="_blank">📅 03:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77572">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ: اسرائیلی‌ها در این بمباران مشارکت ندارند. من درها را برای بمباران بیشتر باز می‌گذارم اگر ایرانی‌ها درست رفتار نکنند.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/77572" target="_blank">📅 02:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77571">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ: من مستقیما با مقامات ایرانی صحبت کردم و آنها از من خواستند که بمباران را متوقف کنم.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/funhiphop/77571" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77570">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ: بمباران به زودی متوقف می‌شود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/funhiphop/77570" target="_blank">📅 02:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77569">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ:
بمباران به زودی متوقف می‌شود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/funhiphop/77569" target="_blank">📅 02:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77568">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یدیعوت آحارونوت: احتمال آسیب به یک ناو نیروی دریایی ایالات متحده پس از درگیری‌های امشب با سپاه در تنگه هرمز وجود دارد.  گزارش‌ها هنوز بسیار تأیید نشده‌ و احتمالی هستند.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/funhiphop/77568" target="_blank">📅 02:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77567">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یک مقام آمریکایی به فاکس نیوز:
حملات نظامی آمریکا به ایران همچنان ادامه دارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77567" target="_blank">📅 02:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77566">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پاکستان: به آمریکا اعلام کردیم که دست از میانجی‌گری برمیداریم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77566" target="_blank">📅 02:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77565">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا اعلام کرد از الان به بعد تنگه رو کامل می‌بنده و به هر کشتی‌ای که با هر ملیتی بخواد رد شه شلیک می‌کنه.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77565" target="_blank">📅 02:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77564">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اینو منبعم زیاد معتبر نیست بذارید کامل تایید بشه که فاکس نیوز اینو گفته.
فاکس نیوز: ترامپ گفته است موج بعدی حملات بر روی پل‌ها و نیروگاه‌های برق متمرکز خواهد بود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77564" target="_blank">📅 02:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77563">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا اعلام کرد از الان به بعد تنگه رو کامل می‌بنده و به هر کشتی‌ای که با هر ملیتی بخواد رد شه شلیک می‌کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/funhiphop/77563" target="_blank">📅 02:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77562">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">روابط عمومی سپاه: درپی تجاوز جنگنده f16 به حریم هوایی خلیج فارس و شلیک موشک سامانه پدافند هوایی سپاه به سمت آن، جنگنده متجاوز متواری گشت.
🔥
🔥
🔥
🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77562" target="_blank">📅 02:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77560">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اینو منبعم زیاد معتبر نیست بذارید کامل تایید بشه که فاکس نیوز اینو گفته.
فاکس نیوز: ترامپ گفته است موج بعدی حملات بر روی پل‌ها و نیروگاه‌های برق متمرکز خواهد بود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77560" target="_blank">📅 02:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77559">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اینو منبعم زیاد معتبر نیست بذارید کامل تایید بشه که فاکس نیوز اینو گفته.
فاکس نیوز: ترامپ گفته است موج بعدی حملات بر روی پل‌ها و نیروگاه‌های برق متمرکز خواهد بود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77559" target="_blank">📅 02:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77558">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اینو منبعم زیاد معتبر نیست بذارید کامل تایید بشه که فاکس نیوز اینو گفته.
فاکس نیوز:
ترامپ گفته است موج بعدی حملات بر روی پل‌ها و نیروگاه‌های برق متمرکز خواهد بود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77558" target="_blank">📅 01:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77557">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">موج جدید حمله‌ی آمریکا و فعالیت پدافند در بندر عباس.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77557" target="_blank">📅 01:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77556">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال ۱۱ اسرائیل:
اسرائیل در این مرحله در حملات به ایران دخالتی ندارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77556" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77555">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیویورک تایمز:
امیدها برای یک پیشرفت دیپلماتیک پس از آنکه تیم ملی میانجی‌گری قطر روز چهارشنبه بدون پیشرفت در مذاکرات تهران را ترک کرد، کمرنگ شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77555" target="_blank">📅 01:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77554">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یدیعوت آحارونوت:
احتمال آسیب به یک ناو نیروی دریایی ایالات متحده پس از درگیری‌های امشب با سپاه در تنگه هرمز وجود دارد.
گزارش‌ها هنوز بسیار تأیید نشده‌ و احتمالی هستند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77554" target="_blank">📅 01:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77553">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام آمریکایی: امشب چند موج حمله دیگر نیز وجود دارد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77553" target="_blank">📅 01:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77552">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">با اعلام منابع دولتی، کارخونه پتروشیمی متعلق به مجتمع گاز پارس جنوبی تو عسلویه بمباران شده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77552" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77551">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایرنا: فرودگاه بندر عباس ایز دد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77551" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77550">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">با اعلام منابع دولتی، کارخونه پتروشیمی متعلق به مجتمع گاز پارس جنوبی تو عسلویه بمباران شده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77550" target="_blank">📅 01:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77549">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک سری گزارش تایید نشده از ترور علی لاریجانی داره منتشر میشه!!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77549" target="_blank">📅 01:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77547">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رشد شدید سهام فلافل پس از حملات آمریکا به جنوب.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77547" target="_blank">📅 01:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77546">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آکسیوس:
تمام اهدافی که مورد حمله قرار گرفته‌اند در جنوب ایران واقع شده‌اند.
این اهداف شامل سامانه‌های پدافند هوایی، رادارها و واحدهای فرماندهی و کنترل پهپادها می‌شوند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77546" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77545">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شلیک موشک های سپاه به سمت بیکینی باتم!!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77545" target="_blank">📅 01:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77544">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الجزیره: اسرائیل هم امشب به ایران حمله کرده و تو عملیات حضور داره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77544" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77543">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رفتن سراغ زیرساخت زدن.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77543" target="_blank">📅 01:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77542">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مقامات آمریکایی به کانال ۱۲:
ما انتظار داریم پاسخ ایرانی ها مثل شب گذشته باشه و پاسخ خاص یا بزرگی رو شاهد نباشیم تا آتش‌بس فرو نپاشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77542" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77541">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">من که میدونم امشب هم آتش بس نقض نمیشه ولی نمیتونم ثابت کنم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77541" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77540">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رفتن سراغ زیرساخت زدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77540" target="_blank">📅 01:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77539">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بعد نیم ساعت صداسیما انفجار های جنوب کشور رو تایید کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77539" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77538">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گزارش‌های تایید نشده از وقوع انفجار در کارخانه پتروشیمی عسلویه
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77538" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77537">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">من که میدونم امشب هم آتش بس نقض نمیشه ولی نمیتونم ثابت کنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77537" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77536">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHwROSNeXETrmX1dZAPpdMuIdhZIoF-hutpR1EJeMcJ-d3csQhwnYl-PfctllYKr6Y4UC1xT7c3T8m7xIz9skHwyLUCv5kjo5PeaW2b-A81M5DQ6aKz7F63m53ShDM_R5ythzJRl6037bVmEsUytFuJzbDeJPJsopxi3nHj6i2VOs3sPIbjAkWxqujCwsla_eYNfCEO9xJTaG9XQW-MOvDwDn9hxIcP2jeDhg-gtOOfAJxmmDl-tTbMaHq2hxT2wFclmu2aU78DFF29R6MFB4n8r9SW1LUM39c7QrF5-Fhdwgj7BO6dBqpB-wt5VwcS6-AJk9TMRts_RRZAlkfmqDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
حملات به ایران را از ۲۰ دقیقه پیش آغاز کردیم.
این حملات در پاسخ به تجاوزات بی‌دلیل و مداوم ایران است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77536" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77535">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سه انفجار در قشم گزارش شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77535" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77534">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دو انفجار در بندر عباس چند لحظه پیش.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77534" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77533">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">باراک راوید:
ایالات متحده حملات خود را به ایران آغاز کرده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77533" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77532">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فعال شدن پدافند ها در عسلویه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77532" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77531">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تایید نشده:
لانچ موشک از سمت تبریز
احتمالا به سمت اسرائیل
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77531" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77530">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجار در میناب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77530" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77528">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال ۱۲ اسرائیل رسماً شروع حملات آمریکا رو اعلام کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77528" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77527">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
ارتش اسرائیل سطح آماده‌باش خود را افزایش داده است تا برای احتمال ازسرگیری درگیری با ایران آماده باشد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77527" target="_blank">📅 00:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77526">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فرید جان سیریک صدای انفجار بد اومد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77526" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77525">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تهران صدا انفجار شنیدید؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77525" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77524">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرگزاری مهر: فعال شدن پدافند در غرب تهران.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77524" target="_blank">📅 00:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77523">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حدود ۱۵ سوخترسان آمریکایی در آسمان منطقه درحال پروازن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77523" target="_blank">📅 00:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77522">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فعالیت پدافند تو قشم گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77522" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77521">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صدای انفجار تو کیش گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77521" target="_blank">📅 00:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77520">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سری قبلی قرار بود ساعت ۲ بامداد حمله به زیرساخت هارو شروع کنن و آتش بس شد
پس این سری جنگ از ساعت ۲ شروع میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77520" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77518">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: یه ساعت دیگه بالا باشید خیر نیس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77518" target="_blank">📅 00:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77517">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر جنگ آمریکا در ادامه:  سنتکام امشب شدیدا مشغول خواهد بود. ایالات متحده تأسیسات کلیدی در ایران را بمباران خواهد کرد. حملاتی که امشب رخ خواهد داد قوی و صریح خواهند بود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77517" target="_blank">📅 00:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77516">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا:  همانطور که ترامپ امروز گفت جمهوری اسلامی معامله نخواهند کرد، پس ما به شدت به آنها ضربه خواهیم زد. سنتکام این کار رو بسیار خوب انجام میده، بهتر از هر کس دیگری در جهان  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77516" target="_blank">📅 00:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77515">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا:
همانطور که ترامپ امروز گفت جمهوری اسلامی معامله نخواهند کرد، پس ما به شدت به آنها ضربه خواهیم زد. سنتکام این کار رو بسیار خوب انجام میده، بهتر از هر کس دیگری در جهان
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77515" target="_blank">📅 23:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77512">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/3f262c09ee.mp4?token=jeZcEktXIMp2UheKWSPLsPXmPMmJCV61PUTR86K6l3GxQZ61Odew9a_ZGbYIICJ4bG8rXb09ZIhJWZ1XcIIEyHLqoFMWhsA2FJkiwjkNaAv2-njNaRzGAg4rMdlYay-cDoe4X8qJWdRH9iMYGtDAvaim8-7GIKaUTqvNH31E-R1CuTK6KsEm-alYs8Zui5z3FlqUM0whfguElBeDDfBv-zWmqZl0G4wQtBwn7JUH3prl7ivwO3jpecmVZUNlPKx-ydnoziDME1Is48U1kYwfISHGeK4Xa_b_XOH8q1Evf7DwTSulAomIQqVCosMf7VEXZRxsac-jxKK2WoZq9s9p9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/3f262c09ee.mp4?token=jeZcEktXIMp2UheKWSPLsPXmPMmJCV61PUTR86K6l3GxQZ61Odew9a_ZGbYIICJ4bG8rXb09ZIhJWZ1XcIIEyHLqoFMWhsA2FJkiwjkNaAv2-njNaRzGAg4rMdlYay-cDoe4X8qJWdRH9iMYGtDAvaim8-7GIKaUTqvNH31E-R1CuTK6KsEm-alYs8Zui5z3FlqUM0whfguElBeDDfBv-zWmqZl0G4wQtBwn7JUH3prl7ivwO3jpecmVZUNlPKx-ydnoziDME1Is48U1kYwfISHGeK4Xa_b_XOH8q1Evf7DwTSulAomIQqVCosMf7VEXZRxsac-jxKK2WoZq9s9p9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمام تصویر لو رفته از عاصم منیر همین الان:
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77512" target="_blank">📅 23:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77511">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یک بمب‌افکن هسته‌ای «B-52H» نیروی هوایی آمریکا که از ایتالیا حرکت کرده است، در حال حاضر بر فراز عربستان سعودی است و قرار است دقیقاً ظرف ۱ ساعت به منطقه عملیاتی ایران برسد.
🙏
🌹
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77511" target="_blank">📅 23:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77510">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">معاون سیاسی امنیتی استاندار قم:در ساعات گذشته هیچ‌گونه فعالیت مرتبط با پدافند در استان قم انجام نشده و اخبار منتشرشده در این زمینه صحت ندارد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77510" target="_blank">📅 23:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77509">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سرور نامحدود واقعی!
⭐️
👑
پهنای باند ۱۰۰٪ نامحدود
👑
پینگ عالی، آپ‌تایم ۹۹.۹۹٪
👑
پشتیبانی ۲۴/۷  فقط ۲۹۹  هزار تومان ماهانه
🙂
💬
خرید
✈️
کانال مشتریان</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77509" target="_blank">📅 23:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77507">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ttnZwasDjbmmcXJpT5lSP8ALQV7dwgY2zhhtxZfOjgfFmaSuzxGi7OlRXlBT0VElVpEjlPNVarwAaVBlZhHNqLIaRwEle4ZwSgZhG_q7I3s_RZ2h0ueUxudBr5CyYu1RoXxhSUxL7IoWBs5H5z_4agiMnpcY1MoRC_RfNJoPaKKf4gZqGEyJRFAqw2zqLJgdPtcrOANHJC-08tj4vvuCdFgC2Oins90DdTv8fOes7wr_YaxKt7oYlZnrsiTpGtIeM8tWsy_Y2DeNOwUVWNyha24SWV708JmitT7LU7Vt-N7JPjikodwS-pXNVVcxGpvral36GcRjKffhpNAgGnVsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرور نامحدود واقعی!
⭐️
👑
پهنای باند ۱۰۰٪ نامحدود
👑
پینگ عالی، آپ‌تایم ۹۹.۹۹٪
👑
پشتیبانی ۲۴/۷
فقط ۲۹۹
هزار تومان ماهانه
🙂
💬
خرید
✈️
کانال مشتریان</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77507" target="_blank">📅 22:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77506">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EL-Gf6_Kx830egns1Xp0e6q0EgfvwLyN5XGoca_P-KYw5x3tHj0At3ffz-k9M5gcYq9qQdYMr4x2bcvGLHwqLBTdPTBmNHqiRdwqH1TSi9EB0Wd2BNJMDsQgx6UOXcbZXm2TyLsYUg6KiHIe8ZomJ2ggFg8TBRvat_W_sv44hjYBBUGQFCszJ9A8pUD7n8U28x_nrMOmVAX-uaPXXmlFnq-IxFmHlw0WEAOfAcWD62A90_DZ5Qqd5WoXUhljpJ1ckBFXAGlLKGb6Cd3MqPSA-7DBp8WM5XuVzHRFOqrDJUMs9zS3c1yhibFrEjA6x8L-PjlAa-CYmH1F8uc4cRJcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس رو نجات بده خواهشا:
در جنگ ۴۰ روزه، وسعت آب‌های سرزمینی ایران افزایش یافت؛ در جنگ بعدی، شاید وسعت خاک ایران افزایش یابد...
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77506" target="_blank">📅 22:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77505">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آکسیوس: مذاکره کننده‌های ایران به ترامپ قول داده بودن طی چند روز بهش جواب بدن ولی الان دو هفته‌ست که دارن زیادی طبق کتاب هنر مذاکره جلو می‌رن و برا همینه که ترامپ زده به سیم آخر.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77505" target="_blank">📅 22:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77504">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آکسیوس:
مذاکره کننده‌های ایران به ترامپ قول داده بودن طی چند روز بهش جواب بدن ولی الان دو هفته‌ست که دارن زیادی طبق کتاب هنر مذاکره جلو می‌رن و برا همینه که ترامپ زده به سیم آخر.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77504" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77501">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqPiUVeMLKgPcF0MGomkoPabttxNaIItnAB6j_1GgibImKfsSzS28r2l_G3XQ3yyR9Tf3V9XiGpPbrQp0tYVtjq3i790IZaFIuCorNIMy8ns5KpeXDDdrsK04mYqZt4sYvPGleqGvOghPkDtFQ2TCM0ZMviB58npmuWw1hRp7p4I6hIJIUPi-vZALtFWX6SPkMNdlDezy5M22U511hgM86SzLfgR_bNApRsqcmRVYvIGCet5Swxh-leh_ZMH87hwKAJpQzfOvOEWs8-qM_sg7H3nF1vM4CdlPkErlgAb3MioWGNJDZhS9Mwvx-wzlu8ReRkkbt2H5JXC7YYnNqyyNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام وحید جان
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77501" target="_blank">📅 22:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77500">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جواد خیابانی بالاخره ول کرد و بازنشسته شد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77500" target="_blank">📅 21:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77499">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک بمب‌افکن هسته‌ای «B-52H» نیروی هوایی آمریکا که از ایتالیا حرکت کرده است، در حال حاضر بر فراز عربستان سعودی است و قرار است دقیقاً ظرف ۱ ساعت به منطقه عملیاتی ایران برسد.
🙏
🌹
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77499" target="_blank">📅 21:46 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
