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
<img src="https://cdn4.telesco.pe/file/cxef7cr3duD96_ysbTmHErvB6V0qWvQ47WmhPYTUTHLD5Es5a5fiufwTvv9EKmE8tSaa2BewRuEKqBqFnN7L78DZSQXdQb4JCfWOBESNoBX6dBVGA619_6jMMnrI-9yMKpvk3xtLZWwrdDiL3JuKARjKaVuBevsFC5ITM50xLXbJJ1AUwgVl1CA91nQaLfOY9QgrkYL9hT4ni3NsGYMyc27BWnvF0SYMvOXRCPqxGLWjhKilWsIvgnfSpqr5QiDbWvfV6V3gGOBvcjE-Uc5bIFJ6IG0HL8CIDDbuZbJj5Q7jFFuknznA793zB3PSpI0OVNsSAX7vFLH920zzL9rSJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 03:18:49</div>
<hr>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0rdWvRGjiDN2SnkBwEcXj8SbC0wWWZekvVKibebNMqUL0t0FCoSenR1HERP2egZamxdZaZOEtOu2x3k-WF_cKmcohdS7Uys9A1ZLQcmG4vuZdaRUiTVtzmpuaTRHFA-DDHiaww_LHyEC5aOS3NCRa56YKff4TeCrOwsB17BAP5r6oUdFRlQEFAM5L5UFLXAUWykgFTrdvzAjtpD2JL4194KopF3EQDByI3fkxyx-32F6E7c1bMx9idc2oCeQwMUfmfYAIx8FW4WPKENeE22OUeX-cgBBteqQbn8a9j1O6Le0Pc-1RcN7gpTNJxGnmPvNZGETBL3fE1rR5T9eH1HlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SolB7PBRxyYPePPAIqSmqAoOpnLRZyvDjg2YXQ-WuMmwD5rtZx15M5k-kwRq73ktQolZJPdMi_AIyu_aCHvGvtStD1gSvLX_sWCyKaZRugC5eiVn9eStNTt6pszZs1vTXlEGvWvcd4QJaroZc9yf8jVfVrO7UE2jq7RKxWpGykqTeRmlvtgQOJ1n_Ma-bIoLehAz1PKpwUrjtedaXd2Z0W6pLPAGt8thkP-uwOtK7jY9bQ_1rlf4QnWrbHW6w4KojW-JMQ01P_3bnYQStScW1PLWg023Nh5pyGYN42pl4OiPkAyFndZ7yGxnIdYZGikNIJscWlVmPC6UVvg1eYmXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=HHKm9WB22Fh99TQSqpn2UXio5FkJh5hasrGXn519FmlkXN8FI6u0ap5vR9kD9W7vuF31FkVM7oTD3Had_lHoNAYCXtOuLeCvTWy5Z-2IGo_br8GMo69tMcfoS2x-PRpfaC_TdGywBkxcPq73IctiC15nN-HZgW0d_jCzHsTn3Komj7XwRoNttP6wS_-hrcfGikfRngyrElhXNTpDP7txKexg8WRCqpNoLYDIQei3EAw6xyUhnvzuR_Zs6vgaOqPZ8IRzdGAFVdeEy5lD4DTgUS0rzWB0k3aFAyomT84T4GbWMK1Dt0uKEJGGzXaaDfggf23n02ZJ3OBcmzGAETdHsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=HHKm9WB22Fh99TQSqpn2UXio5FkJh5hasrGXn519FmlkXN8FI6u0ap5vR9kD9W7vuF31FkVM7oTD3Had_lHoNAYCXtOuLeCvTWy5Z-2IGo_br8GMo69tMcfoS2x-PRpfaC_TdGywBkxcPq73IctiC15nN-HZgW0d_jCzHsTn3Komj7XwRoNttP6wS_-hrcfGikfRngyrElhXNTpDP7txKexg8WRCqpNoLYDIQei3EAw6xyUhnvzuR_Zs6vgaOqPZ8IRzdGAFVdeEy5lD4DTgUS0rzWB0k3aFAyomT84T4GbWMK1Dt0uKEJGGzXaaDfggf23n02ZJ3OBcmzGAETdHsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjY-Qd4xVC_6hO9aUVQ3mTNQ2MzuQQguklsB9FqsSq5N2pZJmF3ACO8NAl9nkcoou-CMZKSkxZJMuUJpzGFEOVZ8b92EnRrYRT1ujIdd1OH2LlNZOgkLkPMBgYIC98zzt02FwOheFVr7St9a251Dbs32uMK2XrkuM0idHIFvq4LD_re4Z2UcAzmCRZ0UMB3GgCGGjx9LMrbQyYt8xsE6c_ACzIrw5yN3iI76MMo16sQ-SsdzvBZ8-LNEolYz5mzS3v9EVZF2wMYXl7aUsHvwhfzZsbSxGoJ3010pa4LWIfeR98fSLMFaUJz5qPfqZYk9CNn4U_7u2m37Xf92XEXVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارتش اسرائیل از ساکنان شهر صور
در جنوب  لبنان خواسته است تا
فوراً این شهر عمدتا شیعه‌نشین را تخلیه کنند؛
شهری با جمعیتی حدود ۱۷۵ هزار نفر.
🔺
این هشدار شامل محله مسیحی‌نشین
صور نیز شده است؛
محله‌ای با حدود ۷ هزار نفر جمعیت.
برخی رسانه‌های اسرائیلی می‌گویند
که شماری از اعضا و فرماندهان حزب‌الله در مناطق مسیحی‌نشین پناه گرفته‌اند.
🔺
در اطراف صور چند اردوگاه فلسطینی
نیز وجود دارد با جمعیت حدود ۶۰ هزار فلسطینی! آنها هم دستور تخلیه گرفته‌اند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWIA7vaW6eOWKyCwQaEt8rRn96sq6SsiWPsCYPkOtR4ENa24Ihg4vp5MXmqwJfoO7vxq353t9MqdpGYcevkeN28RxDQmdVvFF5Cd22K8tQY3qWFFy2aRykGX4v_46S3bVCBU1NRgF1en6xSfRDq0KTg_AK6dnYcYKp_FotiGj1nMq6ku2roMh4rO-cDTjB_841_XbOS_ER9fLHrg7RWcW_Cfb3f2wJLjKYVWnC1SZ9ddvYRbgDb0dxVBON_J1dZyOIgRWfuBq2EiKLMWpSMueFPqJYWAZVBuYFQEyeZDuBgEJpF48ec-vXHa8VqmFDmOq67tQwDdi0wrvWuC199grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=E0XQuEv2kYzHcX4HDdjJaiG04TWTuu3FLTR4wOJpJt0Kom_E_XerG4wmoHYCY5sal_NMr1pep6uHOE5EQ6Sas6ZVEZWDZgUaD0oqtA5RNLzkiKZJOfpjfp5pGGnqluOKZQbGUWP5SKOAz-8NFUJ0bUfcsF2hVXmcoLGeZ2L5GdjGfbwKKLdjuokgZB7txZaroRCiepXp5SSi8mwBxsQaHnSDeg6coVgqHWXQKg1vzEjoCPK8VncjZcSHzW3ldBpCTpiHi-XZgXdpH_Izz-5lwAcpYeEJ0rQbaBIMhYVtVa-Xd6cZKhwfJtcvsFyah0dvGihnHsm7aoLkXt4CTS8Bzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=E0XQuEv2kYzHcX4HDdjJaiG04TWTuu3FLTR4wOJpJt0Kom_E_XerG4wmoHYCY5sal_NMr1pep6uHOE5EQ6Sas6ZVEZWDZgUaD0oqtA5RNLzkiKZJOfpjfp5pGGnqluOKZQbGUWP5SKOAz-8NFUJ0bUfcsF2hVXmcoLGeZ2L5GdjGfbwKKLdjuokgZB7txZaroRCiepXp5SSi8mwBxsQaHnSDeg6coVgqHWXQKg1vzEjoCPK8VncjZcSHzW3ldBpCTpiHi-XZgXdpH_Izz-5lwAcpYeEJ0rQbaBIMhYVtVa-Xd6cZKhwfJtcvsFyah0dvGihnHsm7aoLkXt4CTS8Bzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nmaxx-dsW0yD5rsxPe8mtJsXiQA8ngv-N5qQMnCro6q9GyAQlnAJkzGestmUN4zRa4jycsxTvtMWMpgHt0fkgNavNEw2ysBdTrsT7l4GNMr_Ytuid2Xi1uB2NOB6T_GAF2sxyLupybv98S_K5pVbtAKTn92SCElP2cesEBKWQ7V9rmEHnhVM1w3-yUjK56cAgvyRKFrJ7iJziK8E8c5Bb5m2wwO1R9I4_h0syys0PzTBbJIRyT0so45pLLo-nesn78_I_Y6QxDlT7szIxioIchbjnnG4hbAsV_yTsMX5NSTKSCWMo4O48-28-VsytTSCxfSk7uTVS9iiWFzqCqCoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNM_OZ7ty6uOSu6HvfJpT8_pfg3ts3v8cEDr0geIFPDbPNZ46J41MA6bqcIcgRVRNLDOxIea7di5DQKg-GgAubiUewxJ8GNpndZwh4AEK2E-4JX4L_IdyK5XD1hwvebAxbvWOnMmTjjs7rffyaN5qGk9I7OB4YUadvae_UmNmOD5NsYGtpv0XmDzrNr6mghqR0P2ONn4pdSZQTIwUJYHOu8nk2-0X3qiuJTlR0GTUuPYYXrlVZwWJG-pT0o8Flry0HkdJO63hORiJ9s9q5-ZsRjxwGzeWxKsGlZE6V9g4l6dAmK6ZNJXuoUwLCXZiizBSrA74FCzWACSkJKHvyU9Bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=iEJ1792nZ0wwErbDdLKKwXvf3GGIt3bxnOcE9Ic07IqUny-cBSw_TOcFf8MY9KGPZPluO3FjxfdbnHpJ7c5fNV5oSEbO9dZDFUW0OTahpvD08BeT6Up8TfelECR8pb2OUun5nk1fMm8L8zqveY1YaSt_e7QE4BTceD93XishPydi2CWHCu7f88f8LzNyl6VAJRDI0hN_0QJGa5aGuICneM0be9HnspiC6yIZ8YZHwdaBdpNIGD4Vn5D0yZWbWw4E66w6FxED-2jfkcXBsCShtMm092Ey1WUaUBUhL5PORBKEHT59HYR305oiTwAYdQreBkgsYm4Av7MnqOOEu2EqaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=iEJ1792nZ0wwErbDdLKKwXvf3GGIt3bxnOcE9Ic07IqUny-cBSw_TOcFf8MY9KGPZPluO3FjxfdbnHpJ7c5fNV5oSEbO9dZDFUW0OTahpvD08BeT6Up8TfelECR8pb2OUun5nk1fMm8L8zqveY1YaSt_e7QE4BTceD93XishPydi2CWHCu7f88f8LzNyl6VAJRDI0hN_0QJGa5aGuICneM0be9HnspiC6yIZ8YZHwdaBdpNIGD4Vn5D0yZWbWw4E66w6FxED-2jfkcXBsCShtMm092Ey1WUaUBUhL5PORBKEHT59HYR305oiTwAYdQreBkgsYm4Av7MnqOOEu2EqaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شدید امروز اسرائیل
به شهر صور در جنوب لبنان،
اسرائیل همچنین امروز
ساختمان پلیس دریایی گروه
تروریستی حماس  در غزه را نابود کرد.
جمهوری اسلامی جنگ را به پایان رسانده بود
با این شرط که اسرائیل نه به بیروت
(ضاحیه) و نه به جنوب لبنان، حمله‌ای صورت ندهد!
ویدئو : حمله به پلیس دریایی حماس</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b3Mioj4XvEWutby4j0MYWIyMdspaROqB8gqxaUB3WpylH0ouarH-x_9idt8fsjn3T40xeQPZ7AgU8BGqkJZ-K-nrPeUhTt_OcAkqyRfZVEjtIb0j90D29_SgHkg-kJsMoXNkEszSiVcLbNWbAjPbmr7Epz9Ks-vq94Sxb2M9o2LdpQOAgyDMdRCVjlqdpbD2PtG9KebIz-dRQ8g1IGkiGc67Txm-2Ob1nszu2orVL9ODJ88Y7OEbaCSrOtiaLP-fcgQ82AkYpzepTQly2hWRJQcd7YO1V5xynv1jG70jFJk2ae9Omc0beP10QbzZJvRVEesqGORt1fjDVtxI1B7wVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3OdnPsakEFYS1xZXBdMCEhb3TzMEuwi84YI_E_Pgu7m0TkNuHq3XCe0jC_C4JRXWPksqDZ8NRCmRhOl69hGgj5sW0ba3eB6SJkAjOV7T_mdjoh2PtTT0XUjIiS4vlEAwd1NaLAjtChsKUwoECdmv_ADezAgzaVMgrCOT93rQZ3yi6ionYzZz9JhhRG3ImhpngS82HSKYXPnxEojnsWPJf_PawgNV2-n9MI9t9gzzaksuc0Uvk4Zew_08-f3luiEmvJPssndNNRuYuch5ckHU0CTOpCRKD8VGJdVgvHV_C9Fuo84L4gApDsKULoVLvUZ36vRWxsbsSsITlZKqXWQEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=r84DyzvmNnm9a576twT2MaI8gBJftQKHvxUe9UahZKiVrWH7yK-Eb9ggHVZE7vOQmQILpw_zwu642qMDYnIkY42E7lAzJMEe9lHN3nhmSnMsbXwJNBPI5r8q2CZPAjM4csfYOuPNzlfofO2zHAtezsbK-3nXRR3v1c8XHtI4blyb9oD258_1duWennLygfI6IPftYIFsAr3Hr4gBWkkkyHKNh8kN-Ax1b2Md85uBGm7e2XxNCN6wR7Jnw4Ej1zZmRnM6Rd5VxYWa5Cwcx2sSKtL7kqwGFvr9uszYgWqf16r1KLSh4jtw9KuJbm4NU-TRN0R834TYNpDKe5uKE9oAeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=r84DyzvmNnm9a576twT2MaI8gBJftQKHvxUe9UahZKiVrWH7yK-Eb9ggHVZE7vOQmQILpw_zwu642qMDYnIkY42E7lAzJMEe9lHN3nhmSnMsbXwJNBPI5r8q2CZPAjM4csfYOuPNzlfofO2zHAtezsbK-3nXRR3v1c8XHtI4blyb9oD258_1duWennLygfI6IPftYIFsAr3Hr4gBWkkkyHKNh8kN-Ax1b2Md85uBGm7e2XxNCN6wR7Jnw4Ej1zZmRnM6Rd5VxYWa5Cwcx2sSKtL7kqwGFvr9uszYgWqf16r1KLSh4jtw9KuJbm4NU-TRN0R834TYNpDKe5uKE9oAeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz1VkNRSa7x3tpNPOFgR1kS7Ak5A92xBz0ZmRuwQXuFSDlvJsLvqx8qf_yb3tCfgzD_Hl9GoO9g-cnoBzTSdHTw3SOIRkWY_poE467lEiyhOTRckn4VAnU8sAyAyDHAg3XrW06GEyC1OTy45qyaJUa51cWuE1fI2kWoBlhyy_ZUBZzFdSymHV_pND5yIu9bzt23OlVWnwmzD92snT3z2jrxeuM3PTEz_aB24Dv8ke3xIGGVCjY1NalZZSnVQlQ14RobDzpjNHuUkc3CGs2fIRrcRYtWrLYojmdRDp490LkDxm0zWihLX-wc3BeLjo5YCaPMTULOiCRwz3FBaCT28cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOyqxxY27ELeFV9VQdz1teaQLF7c8RAILLQyyC_P4YJlw8SoFUP_bjEjgz4H9OXRIkqofsnA7OfXjS3SNCWvkXokAc5w7AVYxwRemUzpBZXCatwqz2hMZXGM6delBMac0sR54aIhC6uByk7dlyMY5ZhItuz_Yv0S_J3kvd9RUry-QB8yONawTR4-GmMzBf4XFFXOi8uJDm_mnt1AjP6BwemB0LOSfVb1itszS4ItM0QsiMhltbkGnpW7ZIbEbsvGqP-42yhjbzFGXV9eSIXhL6P7gmRjVIcMH_qxkscJEcf0EoBVOc7jzbUkLVpVA7qls9Cj6iSO8Vv45c86qKdyOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY9RV32qaTw0exm9-DK194NbTlE-4E9YEDTZBelmKhAtJ_j5kG90do-ougJdaa0GsfzcC-K65VVfBQ6uKfsVCEHlflMykONaJpyyjow85ZhkwhgNz6YTKFfLyU3Cpl2A1Zt4TNM5jH-c9TG9ZlOAnIO-7O1KL1w38Ll36o2db7YhBBk6dcjXQ0tstSpjIpQ-ePQToQ_dN4yBeGaWTaGIAMC-ZmweDk0Xe5yZcpTshtlokHywcnmkUfI_d10godRXovQRB9cSggFfSQmAMAMp9cQs0FXyc2RA3-vw0al1owD-guBFKfZQq1-uvb2uVGpNBMZTLCJ7pr99NGetd-Hr5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ILjtLlrYpSuZ-OblXvcXqD20exnrFjTWvihCCah8lh21WMY31gvQfqqQsp6HeST_5KMj8EvfSFOAvOe_EAQqQtcD9M1e479yWWFi3whvy8xwg-B8aiQzU80LeoVRZ8ztCVr7VwxB_Fwi1CaTMLpP6bxrheJo7zL8mvrP6kh8o7vxFsFlScdl0UVRcnBNM59pkLYYs-hn08-XLMG5IgxU-J2h-fF8akqTYoW39Z418ec_dx51e-qMD6uERXsh2RfX7DEUEB-vBY_xkVICmLG2lalari0eVhdh_fwHgEOEHF6UEGhrhWPCj4sAnMfcZTZCSMn64MVoSs9aIxXQrMh11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EfncNQCt94Z7uNw1bT7oQlDr2VyFEZeY4lec_DUUD2a3yWe_ZEgOUUSLerhKXUvhbV0JV_ecgcun9FH7jwaCF0Tfe4_GzjFbekl4MknkwV37gEetFfLwI40h1ug8NkJojePRhWESyaZZbP9jvuCa3bZh9iy_xy6WYtAMV8ezi1IzS4G1vGc51kNCcD6AnI_TU6FkdkwSEvvhvI8PRfAPoB6SQcJIrHC04KRFtMW4ovmzsSpaF_FOg_5y48TYJusEdysBKlneFTM5bWYjMhqs_5oVSxE3QsFyL51pbUlx4K5GFTE8S5ByantBcrfu30_qxDC2LJfzB-KXiWB1Ky8v_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYyksYwMzyIqQqZ3YG5Krw11zaDeXa_VuAz-PFSq9pX7D0PqBlRaLqZSLPvk9LwllJV-leJJTA9-J5obb9UnslulbL1RcNczi0K48tk3xrUeSLS_ekrZamT1fpQZdHdzJl-EBBIeWOX1M7YYAKF8igZECPDvbBDB7ISxQcdHrsbkGGxFf4CGlwXGTYziQD7DEiaPhuz05nyWUzIbwsD6EjmLK6HnpADqsm-Yzyj24TsWRTT4mBK2144yKCPYFIGlXomDvZGsjVeCDoxGsyox_AnI-MYUCRzEib9AyGRU0gPh3ZCiJHoL61GMDiVjc-Nc8-pMpFfVGRBOnLYY3O_JAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4CnqP_H6sIJKEruoIMApotCOaNxwMF0dXcNjd_z69Jla3-Eq_sVzKjDmDnp0UgeGrKiRlKl9eVYRYaztTwwOqhqZxovNUXEDYb19P3j790pqy25ZjAbpu-Xf70yvt8J8cdMy5wAyBpl2Sq4ukHV_NVmWFJ4aX9u-iepMC4WvdgubWjJ0g43f_GRYsSHR0TOe5WnkKvNZmZdAX2Z0hbMWyaaENtYEeMCnZsy2apPBvLww5DTVwxb_s_fnoGSG8XljynuVWKoEsVGoF8vATCO9AZSSrNVjAsuBPwyhTlgjJESOivx0q-gr73K0DVqB4K-JJufQ2EfPxqs6G8O1zHCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICPdrQ0sD1_Dtb_QuX2kQRAbD4D0u8ZEooEUI1Od5nYA8lSRimv6CWa8Q35KkAdgSBzrI_hC6OB4n88IpxoI1fZebXVtd7W_T-zFXSJfX_f7uBu33TY3tM-Yen7mwMXyvFZAThQqgtL45e_YEXIcc9xZ3qppLH27AsfyikGTjkSPfe5GvmIjmXiwuHYVHycIYiHpHYAqi2VQHKsiwsR9ujGgcrwayq4HSjvmMlNCz6EggMm_sD4-rnCGcqEToGoyAADbFkMPq9dPKMzdmCjc0h0QBxFR4AJIIjTq5aPN_c1FYQVDzwQJcpuiSjBvkU78doENgAC5knwYsxCGtPLDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=UpPYQPyNj1h9Jl_-0qHcnSBc7WRvzVrqcow0ML2xIblzJlab1Hh4hokRN_9qv_5EFk5-A7R36ApxRTfgk5la6N0y7PsJ68qV_tK-bP5oxz6ldSjXPr2v2Z1wdcV7uOMkTEDAj5GRXFb2hbDS5-c-EePStjutIhleFoO0ZPXvPOF8elB_M0BgciPR9YZETjnU7sgUX4_F_X6EgKzuxpsUSC9kiKF7ur_lS4tlBH6hyW16WYTC8NoErxoTqcyBREmI3qICSlLhO90XiUuhAhO90cZsl1lhThby-awYRkdD4ElOtGNZW80HTeH91239UPCB067zvzRJLWw4IGzgMVgzOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=UpPYQPyNj1h9Jl_-0qHcnSBc7WRvzVrqcow0ML2xIblzJlab1Hh4hokRN_9qv_5EFk5-A7R36ApxRTfgk5la6N0y7PsJ68qV_tK-bP5oxz6ldSjXPr2v2Z1wdcV7uOMkTEDAj5GRXFb2hbDS5-c-EePStjutIhleFoO0ZPXvPOF8elB_M0BgciPR9YZETjnU7sgUX4_F_X6EgKzuxpsUSC9kiKF7ur_lS4tlBH6hyW16WYTC8NoErxoTqcyBREmI3qICSlLhO90XiUuhAhO90cZsl1lhThby-awYRkdD4ElOtGNZW80HTeH91239UPCB067zvzRJLWw4IGzgMVgzOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله سنگین دقایقی پیش اسرائیل
به جنوب لبنان،  بخشی از هدف این حملات
پیام اسرائیل به جمهوری اسلامی است
که قادر نیست با اسرائیل معادله‌ای تازه
در خصوص لبنان ایجاد کند.
جمهوری اسلامی با حملات دیشب و بیانیه پایانی امروز حملاتش، میخواست این معادله تازه را ایجاد کند که حمله به حز‌بالله لبنان مساوی است با حمله به اسرائیل.
اسرائیل این معادله را نمی‌پذیرد،
در برابر حمله به ج‌ا به اسرائیل به ج‌ا حمله می‌کند و در لبنان هم از ج‌ا حساب نمی‌برد.
گروه حزب‌الله چند روز پیش آتش‌بس حاصل شده میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9G1lSJWilJIls9HliTf1D651LT50RAQ0Dmc3m1at0i6ALkrq6UJ2li396ryJele2BCHlSfzqstNEfdrM6jwQu-mwMyTfZBP3H18nu9I1OgH8omWh4M0l2Gijt6DSpO4lgEoihMn4Xt0HvbNMzUgjQnq4TOvs9OuUECKwT6C2qD0A219sm1WTr4fn3uuhOx58ydL7NoXDDCMe0aSwORQk16cvfSY00ZHdQP1oicd3kk7p4Uou3HDyQj1cb03aUfTk-nICWg_3JsyhJlyvcB63WVuk8rCzKGnk_BAqjAFVTDmKEYmZRyY3UcbEcv4kwRWWKmdANpeqo8NZmEWTk3CyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=XBtGKgrlKs-fsI17NVSPph3yNUSalukXnCOAlAC9na-ZW-WoxwyeRw4pAAOxXNM9HTHKizE754BsQ09DdW9zyYp-DqY4V3d-oe2Uf8fM_bGPqtbOpNH5dK0aBR0-nZoBceEr_GKl7JW8UYOxQ-l1KdtSnjAIGk2PgZiRIRxIN8bOfDYTauWnoT9PlImEgw0PyEA1mNxQkFLsU-T1Y5m-xsD31ZkhfOo7GBvS6D1HP_GzCBLoObMBIFFhdp6secB35q1CR3Wq2fislQTQUpi19z61bsUWlBieaWUmTSN8_Of0yEdkZdAaBWS4-VJkS2aTvkvCu76E57TdatJT9tmQJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=XBtGKgrlKs-fsI17NVSPph3yNUSalukXnCOAlAC9na-ZW-WoxwyeRw4pAAOxXNM9HTHKizE754BsQ09DdW9zyYp-DqY4V3d-oe2Uf8fM_bGPqtbOpNH5dK0aBR0-nZoBceEr_GKl7JW8UYOxQ-l1KdtSnjAIGk2PgZiRIRxIN8bOfDYTauWnoT9PlImEgw0PyEA1mNxQkFLsU-T1Y5m-xsD31ZkhfOo7GBvS6D1HP_GzCBLoObMBIFFhdp6secB35q1CR3Wq2fislQTQUpi19z61bsUWlBieaWUmTSN8_Of0yEdkZdAaBWS4-VJkS2aTvkvCu76E57TdatJT9tmQJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=smd2RmUG7cw4V-bOoM1O0vMw5658U720osHQYJAWZstRNzXh3i0-DPzeAbQN0gXwDP410DEO_c1hQ71_crBQ2a0t26H8Mw8KUQR9ie5uYw5oM4LCJMFx6s6bWzUzWNE03P-nVDZ93QVIEsVU_p9QprbX7VXFoPHSzTZijZ70-cSdfe0sGNkS3TDzqH0jQ0oj5VMIdKAV6rsAn80K2Zt_NO0EAvg_w8rgk5IO84wI-PyKZpWkDTSffKKeUictuI1cxLEdZlLuIXtHN8BUFwP0OpCZK1OMul9GZ0zHGw_naWFYf6pYUMhayGfLLLv_WaTsckCf16ueDkWeMpVwonMjoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=smd2RmUG7cw4V-bOoM1O0vMw5658U720osHQYJAWZstRNzXh3i0-DPzeAbQN0gXwDP410DEO_c1hQ71_crBQ2a0t26H8Mw8KUQR9ie5uYw5oM4LCJMFx6s6bWzUzWNE03P-nVDZ93QVIEsVU_p9QprbX7VXFoPHSzTZijZ70-cSdfe0sGNkS3TDzqH0jQ0oj5VMIdKAV6rsAn80K2Zt_NO0EAvg_w8rgk5IO84wI-PyKZpWkDTSffKKeUictuI1cxLEdZlLuIXtHN8BUFwP0OpCZK1OMul9GZ0zHGw_naWFYf6pYUMhayGfLLLv_WaTsckCf16ueDkWeMpVwonMjoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=K05VvM4r7NpGiCVEtO5eTMe8VFKQcTiZ9ql2mrqtD1U5-JBw3Hb_JLA9lbYH3e8uveM6s6u-UsnHbBYzWd3a7xuPedCSjrGEmci968_xJ_2KNow4NEPp5xUxnkd1yOq71DF_CJ_C-wyR0XP_CduTpIqMKtoOJgW9i2nTk4L_bRXKub0LKXF87hFG2951ynMS2VbUtCjzMyOBvn6QUjFmbFfsvMYL2p1wnk5T0y3HmXF-dsWBJtVSRzlLPUhg6l5HlSL3JvOsLeL6vg-g9gK2Lrus62mvs2traulhxeagyNVFl0yyplxkBJOkw8jFdcgFl-YjbMdLUnBt9hR_5ngk0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=K05VvM4r7NpGiCVEtO5eTMe8VFKQcTiZ9ql2mrqtD1U5-JBw3Hb_JLA9lbYH3e8uveM6s6u-UsnHbBYzWd3a7xuPedCSjrGEmci968_xJ_2KNow4NEPp5xUxnkd1yOq71DF_CJ_C-wyR0XP_CduTpIqMKtoOJgW9i2nTk4L_bRXKub0LKXF87hFG2951ynMS2VbUtCjzMyOBvn6QUjFmbFfsvMYL2p1wnk5T0y3HmXF-dsWBJtVSRzlLPUhg6l5HlSL3JvOsLeL6vg-g9gK2Lrus62mvs2traulhxeagyNVFl0yyplxkBJOkw8jFdcgFl-YjbMdLUnBt9hR_5ngk0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIay86w-mCDAFhfbNfvUz6ZTv1dqx6kH5cN6GcybPNPag1i0jGO1kJEr0FOuDWRzi9ipBJol7TWaqyuGTYy9RMqsTmezHpYJC7nK5OuDMvqXvWrcxOi-zwhhmJPnzulxz7Ulu_EJpTsIjNsVXo-dXzPtGGirn2Roqy_ypgc54_h0tvSAY8cjnFiuMtNJjOum0KYBmlBt0wDIcOmHxjzEMXSQ_sY6lQbHcMbQdsG9I165xwmW9QTtMpPGdyL_jVIWN5SipA3Rj9u2OiXyYwbmty8vx4tG9JRpa20mu-svQKp9llkFoBSmJM0lU6tOKSHMifHOvM5NVTJ3pT07HnHbXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dL8msBMd7BM9OqXyUepLXw7Xqeo1w4-VlXo04Q8ekpELkj1nFylbEuMSXIglami2auwLaKOzKRQ-I26gJjLQRWoynMclL-qtP6--kboRVg9F1a8qYRpl9LzaC6NiZL7jp8rKY_dl5nfsisNiMaBJHsQXWQEjC_MquXtr4hxAGmXXSePlZfNxR5tggkluqAI1at7SyBbS_9VPpq1xBvRjAzvWipHqhBOXwk6P_HdDfHlASLgMLkiHSyRIFotiy3YYiTm7YQYwsx4OGNp2vLFiWW_Ts6biGr6FrwKSb5ZzWt8kFZVFfcTFhpV4PZryZ5KvU1zbrfpaPSecSr2731i2OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=Qkgc_xDMSXemQWg9TA6pC6lKQRtaXgISm0zMaTjdetEYrheKTNx-NkSLBNIgCFBBKMV-SyHI0pY9_sdL4BdbfT4upApX63UG0wWiHMb9WpaIOPp5Tobn90peGIpgMcSLlqr8m6NEylH3NBtfdHYAm88HLbX-61AUq63tQAMz0hwWNpx5t51XwOjHoHOUjawpgN4Rhb9DZirpHcYtUqFWzLUCEplFdalE4pEmwr_3sCOCpAlH-IdTLuNRrtb2cwAGolZHe3UH0FOA8D7TH1K8TC8H4qIumRWxjwJjgCfJq1lv4u7KeaRHtu5H08c-34OQQ7l584E_GI7-swuwwv5OvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=Qkgc_xDMSXemQWg9TA6pC6lKQRtaXgISm0zMaTjdetEYrheKTNx-NkSLBNIgCFBBKMV-SyHI0pY9_sdL4BdbfT4upApX63UG0wWiHMb9WpaIOPp5Tobn90peGIpgMcSLlqr8m6NEylH3NBtfdHYAm88HLbX-61AUq63tQAMz0hwWNpx5t51XwOjHoHOUjawpgN4Rhb9DZirpHcYtUqFWzLUCEplFdalE4pEmwr_3sCOCpAlH-IdTLuNRrtb2cwAGolZHe3UH0FOA8D7TH1K8TC8H4qIumRWxjwJjgCfJq1lv4u7KeaRHtu5H08c-34OQQ7l584E_GI7-swuwwv5OvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=oB-BWxJ7BLuDYD-e50EoXHRTCDG3kOq8yJtflX9xc8PLj4mI3JDacQcbLJYqHT8jtAo-Ts8lqLXJbbEPxgUlpDe-aC0tDVtj3E5cF1UpYmI1Ut4N3-tXgjG1nrNFvU349_636DFboVjUvk8RM5KBff0FmMdLzQcOqhTRsXZbiUq8bAe6kX6g97Pqk4JgVzPTeIrbK7oyTuHZpopw5zexf1Ak47Mt5_rHhaZLegsPikEuzKZPISw5L74qqwfzMTsoiXciVfnV15ieK8LvAiOygpZCAtu5W86ao5lqedVgWSzhaaZz_97uiplvCGJyC9SzQnqw1ydUcbbv9KDSAN8aKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=oB-BWxJ7BLuDYD-e50EoXHRTCDG3kOq8yJtflX9xc8PLj4mI3JDacQcbLJYqHT8jtAo-Ts8lqLXJbbEPxgUlpDe-aC0tDVtj3E5cF1UpYmI1Ut4N3-tXgjG1nrNFvU349_636DFboVjUvk8RM5KBff0FmMdLzQcOqhTRsXZbiUq8bAe6kX6g97Pqk4JgVzPTeIrbK7oyTuHZpopw5zexf1Ak47Mt5_rHhaZLegsPikEuzKZPISw5L74qqwfzMTsoiXciVfnV15ieK8LvAiOygpZCAtu5W86ao5lqedVgWSzhaaZz_97uiplvCGJyC9SzQnqw1ydUcbbv9KDSAN8aKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3kETrWrKcs9AjZXufszl4UU8a-NTw0HtORUr2C2T_bZRoa1npm-SJqREXcR0p3SnY1361JbWoAmgcmkaiAF1XPTrEtLVYNkU-OLH8jbfc5aeKy_XJJ0gvMbes49l4mty2tzsdZrCFPlkFnSb72ZnIJRBHY3QXegCywlT8sQtMSSU7nZvUt04zVd9Sif6vTSpWuIldssj04gRfcXLGs-yaBNxoze1CYLksAFYQWuZ78_tyLg7H4aOXgxCJc1piftC4ThtZTQWg0CPAjknNgY6lWWZsdGtWzykns0pqYDQKWg_qH1_WLfXXUDzi5-lfOyqoZRH83IvdfnAznhTY8dJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=ZlZ-DAugw2Bcl8SisfggNRYCTDsTp8VZ_ZdysUKS4BlmVAQuIq24lZk4F-5SZf7T06-cJoj4hLmAxb6P8kRuchup-YMrrV3ww3_X2BKtKBu6gsoneCSbR-qH1uYAbKGSjf7zSV1cAQ4jNXYO8yb0sLgWv_-y4EQ4b03bA13dW624Ah7pi7NbkjpH6rmhbr46bK-ZlevqMv7Mnqbd-jC_TQ1tfzwv3sQt9MXdhzGiAkHkI1P2ytMmqRIE-TerSFe4RMkvqxj3hV-lKRiZgzjmYq-aF0KcHXx9zZL-UpnKxOluP0uGkDnNAsZE_uUeGK51ZD7MpuQHCKZC8biBLhIs_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=ZlZ-DAugw2Bcl8SisfggNRYCTDsTp8VZ_ZdysUKS4BlmVAQuIq24lZk4F-5SZf7T06-cJoj4hLmAxb6P8kRuchup-YMrrV3ww3_X2BKtKBu6gsoneCSbR-qH1uYAbKGSjf7zSV1cAQ4jNXYO8yb0sLgWv_-y4EQ4b03bA13dW624Ah7pi7NbkjpH6rmhbr46bK-ZlevqMv7Mnqbd-jC_TQ1tfzwv3sQt9MXdhzGiAkHkI1P2ytMmqRIE-TerSFe4RMkvqxj3hV-lKRiZgzjmYq-aF0KcHXx9zZL-UpnKxOluP0uGkDnNAsZE_uUeGK51ZD7MpuQHCKZC8biBLhIs_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6tqVANZAItviI5unwhQAzIEqgfQWXOChvGlQ4XO4rg4NCKdo140Cm_W2oAT0pf5VqYYYvaQ_x-orqz6i9OqQxx9MgxH6IP-RSL4BlRV5ZsxsHiIrM8VtRxd_RHVck649etLbPS7ILFttJMKmXD-1RjtLQXVfcs1fybhCjVnOkGFvsYEJyPOGqbZrqxhpt2aLpvGgb0mrPB8swisxCNTItKq8I2o-e8PyE_YXsuOOwBhhBx8lPig1d8e28Gbai2b6YRtq2DKjX6W2sBhLDg1dT_gOkMpMq63hHaRa9bpJ9Pp0zgwAlwbGiv-rYp-iDwsfSQU2jtqbzOyXbz9BBMgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n56YHv2Kf9HZ4crZffXErYquhpjoI-DDuFm1z1Q1RUXGNHHSk46jOdxxSLG8tWsQaGg6mS9PMnqQNNlkX2ymgAgZ3Z5bj79Kvpu8VgbSkVqbnik4WkdBpWauiTbXWljMCkm3cvW5DU375KnjV7gcs9K3BtWG7bJm5C6e3NyNu_5V1zT0ttFUwgnIX0AflVkFx2Pl2SEV9UQZKtAQmfkh-llRdY7j96d-tbKrC9zfWpbvmlyHTq5rqPiUAbP3rk-3xtEN00eZSWtNhvyMPlQor3yMnq9_uUMvCCoUlzxM-W6dV3MdvgGLJE5skGF9_6F9Qvd71-8SLoKeUu-chfLOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.
دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین شاه ایران است،
امضا کنند
که :« جز تخم نیکی سپهد نکشت!»
متنی که در اون نوشته شده بود :
«نگوید سخن جز به داد و خطیر
نباشد به پیمان او بر، زحیر»
(هیچ فردی به خاطر فرمان‌ها و تصمیم‌های  او دچار آسیبی نمی‌شود!)
در واقع ضحاک به این بسنده نمیکنه که
خب زور دارم، پس سرکوب میکنم و حکومت،  بلکه احساس نیاز پیدا میکنه به فریب  افکار عمومی  و فریب ایرانیان!
برای همین دست به تهیه این «شهادت نامه» میزنه.
و از روی ترس، همه بزرگان ایرانی هم صف می‌کشند و گواهی میدن که او بهترینه! عادل‌ترینه!
که با این شهادت‌نامه، دشمنان ضحاک به عنوان دشمنان یک شاه ایران‌دوست و خیرخواه و عادل معرفی می‌شدند!
کاوه اما این بازی را بهم زد! یک تنه! تنها! طومار را پاره می‌کند و به ایرانیان نشان می‌دهد که رنج ایران از ضحاک است و آن دو ماری که بر دوش دارد!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN0few-qApru3Ei95J_2v9LbxwOl8QHtRz6Pw8JloGPrOBJHWe3zTmAakBQs6mApj_AO0iz-OHoo_YPVFr6C0X2oVwKCnSuC5BEO9r8dvGj_d5LjBU4MkSUo6LzFkG0h6SYI7EPYpW6px9-bKZhazJDnY7_BX05xrGdqd0fE1j-ZLi--x-7xmV51kncZVKl9eIb2VtQ6_YHHMTmHf5l7GgA8cyTrNF5dXOF1YkSWIiqbUTeMw_Pkr0c2dwAM2-QnIJ82DyC8Z1hV3Y9eMpCpQDvpLsmvoklsJeHpWP9-VkeMJ2NY1U5cAU5E_JFFuDLmlG2wWZc0YjyTNwAb6kRSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfTw4SuhH-oLTHUiwo3tMEMo0KvBd0n34NyWCn0m5pgP8HTb2VeDYB-6uMRmCxbn_P7FA7whK108_oZ8jR_fu2rD2JZCWh7kU1tMxP3Iw1LUJRlU53DPqbGUGObVUakcn9nCzRiezn1nGZpPQv_p_3_0wijaAL2FUsm6fsZZPiNAQRwRfvYX8aHLsQv3BYgZO8WuTQjbGioYFLxiuD60PUegv6NOmMjJTGs-_fX32zVDyxIIrhEhMZPTnUHvlyViV7I2utH7ExJq6AujqNp4OuxiJaCosUsolVorQ1j4_VT-KFhsWcuQN897PAxIfPm2pf7SQ2qO1BMIkFuNdWVhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی برای عمیق کردن دشمنی بین مردم ایران و اسرائیل این بحث «پوریم» رو به شدت تقویت کرد.
۱- پوریم اساسا افسانه است و داستان!
هیچ واقعیتی نداره!
۲- حتی اگه واقعیت داشته باشه :
یک وزیر ایرانی به نام هامون تصمیم گرفت یهودیان ساکن ایران رو قتل عام کنه،
ملکه ایران متوجه داستان شد، قضیه رو به شاه ایران گفت، شاه ایران هم با عاملان این طرح و با هامون برخورد کرد و سرکوبشون کرد!
حامیان جمهوری اسلامی حالا اومدن میگن : ما میخواستیم یهودیان
رو قتل عام کنیم، چرا ملکه رفته لو داده و چرا شاه ایران دستور برخورد  با عوامل طرح و هامون داده! عقلشون هیمنقدره!!
خب شکر خوردید خواستید قتل عام کنید که شکست خوردید!
کی دستور برخورد با هامون داد؟ شاه ایران!
۳- این داستان اساسا افسانه است !</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=ZXXwb3EwiGu0t9uwXjOscZSTgkBBZG5V1UTFSMskZoUAY3wD6dLtJ18ueWlrqs4unAiR_b0ss1Ajf4JsvEaNZ1ZC6z89rZeeeb1G_KXGMPzrTn2v_Z6_lamSV0YLywNrdCcT-BD6GVAdI921jcBDAyJgWtuGFgMeC3itZWcLoNPxlicMddvr0kfXjARPcwFS9teKX2v289iTiOFNyy9FQ7hN6plW6bjFavYw7ihCeW6VtfqIuygN-WyXn1Dphu-3gxamV_mexJyMeCPUbVLpIG-XZFNSncgUdxjsuallt9wYs_OJII4r5Fb7QQjsdXZumjeQ-He0xCaxaikMoS4SDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=ZXXwb3EwiGu0t9uwXjOscZSTgkBBZG5V1UTFSMskZoUAY3wD6dLtJ18ueWlrqs4unAiR_b0ss1Ajf4JsvEaNZ1ZC6z89rZeeeb1G_KXGMPzrTn2v_Z6_lamSV0YLywNrdCcT-BD6GVAdI921jcBDAyJgWtuGFgMeC3itZWcLoNPxlicMddvr0kfXjARPcwFS9teKX2v289iTiOFNyy9FQ7hN6plW6bjFavYw7ihCeW6VtfqIuygN-WyXn1Dphu-3gxamV_mexJyMeCPUbVLpIG-XZFNSncgUdxjsuallt9wYs_OJII4r5Fb7QQjsdXZumjeQ-He0xCaxaikMoS4SDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=HMcv5D_BM6zur4El4ee3ko8rneb0zEOwHy86ndrzkrBl2v5za3vZH9RXcXczk-LonSYDAJjhv0srZGkwzZoDszd-ffjSn2wOYYGgDFdPkClHo52yejlCe3RnK1Gj57l2EScCunaJZuq73YpItrQuuCM8kSujRMBfcxb4N1SQpX4ZFZF-B3V9z0LTciEf4at7ZvRDoHLjTIsC6_MRYQI3VDieCyofzG-mKNh8gK662gO7_Rzx0V_bcm4lV0lsL0S8RgOsIxdfCUs0fPnUzawRy0LcizgDQeovMxJfL-PVKoEc1iKVU-Ikw-4U5KuK3sQQJxgg19L7nVnFv65a4yAzpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=HMcv5D_BM6zur4El4ee3ko8rneb0zEOwHy86ndrzkrBl2v5za3vZH9RXcXczk-LonSYDAJjhv0srZGkwzZoDszd-ffjSn2wOYYGgDFdPkClHo52yejlCe3RnK1Gj57l2EScCunaJZuq73YpItrQuuCM8kSujRMBfcxb4N1SQpX4ZFZF-B3V9z0LTciEf4at7ZvRDoHLjTIsC6_MRYQI3VDieCyofzG-mKNh8gK662gO7_Rzx0V_bcm4lV0lsL0S8RgOsIxdfCUs0fPnUzawRy0LcizgDQeovMxJfL-PVKoEc1iKVU-Ikw-4U5KuK3sQQJxgg19L7nVnFv65a4yAzpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfSyvCf_GKRB1Zi7O3peZZriYucOj2eHHXwjbKwCyT-Km9BDTHNZbr2Azx4FtekMd_K64Y72QebK6Hn78e1Cj5QsD7uQjAy4B1ebO7cCwmdden45EOAx5JcaJtAhuglZf7haJyrJISb0aoolBZ9O1HNkOemVoXqdnAkxSSWzDjbRHrjScJTVKJvxxTkjW1jixvQv4mTXwNGUkvotwUcRW0UbeqzJjRYYrs3XTrcxPDC-g_cLRIk8NSRm7PyAf5tk_TzOstcEYRZ8EXkLAsEqUy75yRgdM1uR4skdfHbFpoPfnI4stc4jVzJOQhxm7EZNBDpLY81GNa8OJBsk1ZcOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
سپاه : اسرائیل شب گذشته به چند سایت راداری در سه نقطه کشور حمله کرده است.
🚨
سپاه : دقایقی پیش حمله به مراکز مهم‌اسرائیلی چون پایگاه هوایی نواتیم را آغاز کردیم.
چند توضیح :
🔺
سایت‌های راداری که اسرائیل به آنها حمله کرده کار شناسایی و مقابله با جنگنده‌های اسرائیلی را انجام می‌دهند که اسرائیل به آنها حمله کرده
🔺
سطح ضربه‌های دیشب اسرائیل به نظر میرسد کنترل شده بود. با توجه به مخالفت ترامپ با پاسخ دهی اسرائیل.
اما به نظر میرسد سطح درگیری و ضربات امروز افزایش یابد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLPnJlCtndujayub-ouinmXEzv3ZNntVqAKz9wcVBPlDdtQsDEAeERDAh3Wdq1K5FIeTh6ngJn_hnLHvmbBA_YNnG4ykD06FlUUU-Kwy4m1Ldjvo8_Yvk2-X8EfjbT93J7X2auXbnVti-ufAXNo65TQy0I2Dd0Nm4VJcj_YxGFP1zY1gZ6g2sAsqumM8aZE2rr1WCvkzHcfK31Kqf6zymFzJtXWMtSZjZWIA0IBjIeSEvgKo9o7_shxydZNE9fxhxMt2ukWAtCn9ZyCx-6iMGP-21fzF7V7Rz7WIL3PhGVlJI2_76FLzYCk6rS8QptWAPo0aFk26dZ6cAQie3ca5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1I_SU3y3uZrGatibeEzOotw5cmGrbFOMs_0IYtEtiNEXZGckpBhFUGKuv6rXC94kXkTpJTs6oeGY-7ES3OMozkGw1gV8JUXJAxXwG7NPYSWEXLjcQXgo0TT2K-HJzBn4D3V7iQrpJBiA2F06dL6vGqHzFmPJUa9OWc_WtKP3AYNvSY2Id6qM7KrhgaN6Wpgk2tiu_4QRPoJqO3RoPlwF91N5yPzHBFxTMBUOcKeqa-xRavQSUx_9Tj5-OJ6XorjSjRy8BvaNpnRp6uG9N9i_0HNi87ME_GgdcBH5uQpYqEoob6v5KEymAckj8Q26rgfG3ChKNoYeffZRKGooRy4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA3LcCp4K8H2lWwI7itpyu_POk2hn897NsKSDy7E-gsKOF6cFwCBsK22t_fEdn6Yu5AfKuEyY0dvNLds6_cwxR5Y7UgLyB9XL1ts9c0_3TAu49VvGcr9PFmWVnLgD55xuHi3esPJnBcyzYx8DZ1bcNlyoQVkWVKSR_03yJPumG6-mSDLpMe0_yL7q2scnXuXnNDhRaoDPygHlsxY3LOWeGudyP-9rV9IT5qUddJGeIUjkJasW8R2fyzjrH-T9DNQl1dvDAiQ7ofHKPSONs4Xk7sOjg4VkoBFhNl3hGovlHy5ocg953lkxhMJb1KlT4pxUT8A9OKCILmQYHMHZjprWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
اسرائیل : پاسخ حملات امشب جمهوری اسلامی را خواهیم داد!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5364" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApFjEe2jWsQPX8s_ZEavxIvBQSrnXElGwGAvBBhTZRV5FPtz9wATloQ0EyKZPWwmb6NgbMQDnzw_3e2Y03pBTO8wmQ2D93_oF6m44DQp_xEaDo3g00CspjtV8VX2I-A3F79H09JMRw7VFe16x14WesZjZlwLSX-qErHtkCrx4-ZjasZFA9f7MftfxDZHnqdY3PX97kkOW3mMKUBmk3rLCe4FqzZNp94cr0rj3C9-rn1FhFKpQ4LNS4ceJ8l-i8UFEh04LQzT9GnrWTXfj5fQXmCkYlYDda9lQeGzaH27BsP8D0JMsUWvftogzTo9Cms0QUB1XCUGhxvmD5ej1RE5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موج دوم و موج سوم حملات موشکی ج‌ا به سمت اسرائیل
توییت عراقچی</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5363" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
منابع اسرائیلی : ۴ موشک بالستیک به سمت اسرائیل شلیک شد!
دیشب نامه مشترک رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان رو تحویل گرفتند، که آخرین فرصت توافق و گفتگو است.
امشب جنگی تازه را شروع کردند، این بار برای حزب‌الله لبنان!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5362" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از حمله موشکی ج‌ا به اسرائیل.
🚨
هشدار حمله موشکی در شمال اسرائیل
🚨
قطر آسمان خود را بست.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5361" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amvsibmt_WwYit8WpGdzNWtfZR-d193kt954fwmqAe86Fotd1OIcYxSWr8pNwVzBJA_UZvq5Wkd6Zlz-L4xhsZITwthsEjBc0mQAO0-NUTdJ29MF3dNvRT_0_K4rp71Apv_5JDVR2hpY-jSHU0CDsoxsXOdWwf468CRBM33P1YmDcjhmmhd06SPuE81MfRTOcDmfHnDlzV02JXUwbufOA-oJn7T2cUcouV2UMtX5IWpZEMAnJGM3b2Au_aEjN3Rjgqve5Tz5syfHyOdqX3kgTR_MBbvHMsutFcew2yWqCj6NwUqJuwd0SKCNWrEC4Jl2cD1-X-DKdsLejYXSQqh7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTqkvohOV3W-9CKw35sqIO3bCCskXC2IT2p0pAsMyWgBNrLNZE-ZOCr_ONhcVPmbPGUntot0hBB0bZtFwBRX8CDnKKgG2_goUujZ1nUizfq__Cz-XigWYHjaK5bEp1VmvQJI5SoM5O5r8WnfYHLMoQc1zs2LA4UdjFWCZ4d0V9EF-BtSvNF51D2EVsQuk7YHjj-RaEOa2ZLUzYiI7tysMWilpzDt7Kgz3dLABElTvPmgjJ2V3jNm489xJiDi4HBwt4qWionTIiRfc-E9g5lyHAnVH17ymLkxA3Hc9mGOAvRz6w3WLEKujpgoPp_XsR_w584JCiizR_hWinXvxUz7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5nRYmImPCJPGy6iW9rNtk_lSKmLltE-NJwMKiJgFTemajcgSDPfO__wCdaOxpnD8yXXe7zkR3rJ1cZB9tiK90yIMSKCSGoUxvcbGRFFjfOQlilqbtMyEP8oAz3S6nOj8uog-p3_HIPilgdwr-pJVpBVvrJIqYy_N0cIrl1ChY84pHGQNcsmtGZfP6rRn14oDk3WjEoKqTkUz_TY7_wXE9-uFJPG2GXNSrn6QsVQ1aiMqBOO6vrWyRIJZxpxJWxhRSpmM_SX5oUnSf3MMbKK0mCT6Xj6BXbJ1N5OfLceYCIcEUmb9-MmHnXShFY31TAOW6JpYQj80FanZ2ulh0-7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpOTGcrHqXOdXKkBKpbwOLfG4TPDAHlRHN5nvZgxPqadvCnul57ROq-qnrMZ5GeHpQageyiNvpNLGgEl4nFfpIDVCy2tXzamkfxCqkUvsU-G9xTa36I7nZJ1SUnZBZZ3G04xN8X-eILrzCkaGX-Nas54eCwLIS_aKplWCU9Nt1y4qBb60iPPy9dWOu1VqsGw8BU-SP2khY3rspqivmYPvvaswF_e48cpyygPHlf4aRneS0XdvDxFas0z0wuk-3RktdpgpakVGyCP5uw6pSn-9CkHW82qSay0T-lUPbuFpzfRia-eN3PZPYwWeGcNeBgQSO0NOvHfu9fEqQwEm3YXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=cIiJEJJUQDzqNQuBUisj-rBpcTSoHWDRmBVt2PyvVFWsJB8rA8ounXU1E8v9X_EWGHDw0VWS9oimsnyv29C3_f30Sr-CJKzQ-HvvXSP_Q8x_3cf-vDvFAJK4FOQ8GQ9GsZnA-hQc5arHHr4hRlmyKHVMSzs9YVtE2L0miwTivPQ36bsOvXm4EZKYWHnRxoA2ys70T1GM_eiyJrCQ94Hg59sltxB41rpTNFqp30hPN7Y-PF1y8LnQO72WFrycV1PciG799EKardpHkwqb6V-Tba5L_0AzD45rBwrR12ZUGdXxusoQdF4-2QWl3Tmk7MnmuGNrFn5dW-W-ElD86p1M7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=cIiJEJJUQDzqNQuBUisj-rBpcTSoHWDRmBVt2PyvVFWsJB8rA8ounXU1E8v9X_EWGHDw0VWS9oimsnyv29C3_f30Sr-CJKzQ-HvvXSP_Q8x_3cf-vDvFAJK4FOQ8GQ9GsZnA-hQc5arHHr4hRlmyKHVMSzs9YVtE2L0miwTivPQ36bsOvXm4EZKYWHnRxoA2ys70T1GM_eiyJrCQ94Hg59sltxB41rpTNFqp30hPN7Y-PF1y8LnQO72WFrycV1PciG799EKardpHkwqb6V-Tba5L_0AzD45rBwrR12ZUGdXxusoQdF4-2QWl3Tmk7MnmuGNrFn5dW-W-ElD86p1M7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
