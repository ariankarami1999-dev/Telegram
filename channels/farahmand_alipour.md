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
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 23:56:59</div>
<hr>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0rdWvRGjiDN2SnkBwEcXj8SbC0wWWZekvVKibebNMqUL0t0FCoSenR1HERP2egZamxdZaZOEtOu2x3k-WF_cKmcohdS7Uys9A1ZLQcmG4vuZdaRUiTVtzmpuaTRHFA-DDHiaww_LHyEC5aOS3NCRa56YKff4TeCrOwsB17BAP5r6oUdFRlQEFAM5L5UFLXAUWykgFTrdvzAjtpD2JL4194KopF3EQDByI3fkxyx-32F6E7c1bMx9idc2oCeQwMUfmfYAIx8FW4WPKENeE22OUeX-cgBBteqQbn8a9j1O6Le0Pc-1RcN7gpTNJxGnmPvNZGETBL3fE1rR5T9eH1HlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SolB7PBRxyYPePPAIqSmqAoOpnLRZyvDjg2YXQ-WuMmwD5rtZx15M5k-kwRq73ktQolZJPdMi_AIyu_aCHvGvtStD1gSvLX_sWCyKaZRugC5eiVn9eStNTt6pszZs1vTXlEGvWvcd4QJaroZc9yf8jVfVrO7UE2jq7RKxWpGykqTeRmlvtgQOJ1n_Ma-bIoLehAz1PKpwUrjtedaXd2Z0W6pLPAGt8thkP-uwOtK7jY9bQ_1rlf4QnWrbHW6w4KojW-JMQ01P_3bnYQStScW1PLWg023Nh5pyGYN42pl4OiPkAyFndZ7yGxnIdYZGikNIJscWlVmPC6UVvg1eYmXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=HHKm9WB22Fh99TQSqpn2UXio5FkJh5hasrGXn519FmlkXN8FI6u0ap5vR9kD9W7vuF31FkVM7oTD3Had_lHoNAYCXtOuLeCvTWy5Z-2IGo_br8GMo69tMcfoS2x-PRpfaC_TdGywBkxcPq73IctiC15nN-HZgW0d_jCzHsTn3Komj7XwRoNttP6wS_-hrcfGikfRngyrElhXNTpDP7txKexg8WRCqpNoLYDIQei3EAw6xyUhnvzuR_Zs6vgaOqPZ8IRzdGAFVdeEy5lD4DTgUS0rzWB0k3aFAyomT84T4GbWMK1Dt0uKEJGGzXaaDfggf23n02ZJ3OBcmzGAETdHsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=HHKm9WB22Fh99TQSqpn2UXio5FkJh5hasrGXn519FmlkXN8FI6u0ap5vR9kD9W7vuF31FkVM7oTD3Had_lHoNAYCXtOuLeCvTWy5Z-2IGo_br8GMo69tMcfoS2x-PRpfaC_TdGywBkxcPq73IctiC15nN-HZgW0d_jCzHsTn3Komj7XwRoNttP6wS_-hrcfGikfRngyrElhXNTpDP7txKexg8WRCqpNoLYDIQei3EAw6xyUhnvzuR_Zs6vgaOqPZ8IRzdGAFVdeEy5lD4DTgUS0rzWB0k3aFAyomT84T4GbWMK1Dt0uKEJGGzXaaDfggf23n02ZJ3OBcmzGAETdHsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWIA7vaW6eOWKyCwQaEt8rRn96sq6SsiWPsCYPkOtR4ENa24Ihg4vp5MXmqwJfoO7vxq353t9MqdpGYcevkeN28RxDQmdVvFF5Cd22K8tQY3qWFFy2aRykGX4v_46S3bVCBU1NRgF1en6xSfRDq0KTg_AK6dnYcYKp_FotiGj1nMq6ku2roMh4rO-cDTjB_841_XbOS_ER9fLHrg7RWcW_Cfb3f2wJLjKYVWnC1SZ9ddvYRbgDb0dxVBON_J1dZyOIgRWfuBq2EiKLMWpSMueFPqJYWAZVBuYFQEyeZDuBgEJpF48ec-vXHa8VqmFDmOq67tQwDdi0wrvWuC199grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz1VkNRSa7x3tpNPOFgR1kS7Ak5A92xBz0ZmRuwQXuFSDlvJsLvqx8qf_yb3tCfgzD_Hl9GoO9g-cnoBzTSdHTw3SOIRkWY_poE467lEiyhOTRckn4VAnU8sAyAyDHAg3XrW06GEyC1OTy45qyaJUa51cWuE1fI2kWoBlhyy_ZUBZzFdSymHV_pND5yIu9bzt23OlVWnwmzD92snT3z2jrxeuM3PTEz_aB24Dv8ke3xIGGVCjY1NalZZSnVQlQ14RobDzpjNHuUkc3CGs2fIRrcRYtWrLYojmdRDp490LkDxm0zWihLX-wc3BeLjo5YCaPMTULOiCRwz3FBaCT28cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExVubsK3fvGcuFVmsj5_6iBfHtb7ExpIhjh_AdSnKLj-ZFdBg8wAhbnm0TRZRaK2pztUJ_-BF6fu2nDeBTIC8AMk1gvI7iyv5ewOoYrFvxyE9r_obO3Y_RD9YtIguKw6yWwhlJIaR1sdZjgmhdo6wjt89A1WlIMxaTlh56m8s1lQrVFysr3-QtM5H4g_I86bFI5jhYseBqfif0Gv0NHbYB-veewpSJVAHG31UJ9KikKy3l10D0Jsy7Vu_P3AFHAYUFO9gNaz7vkxdRdWLaqlEc8BpZt3LajAK8p5AUBjeKtqu3sBj3TXw5QJFi9xzWIpvh3HIwl8RXDIMI7x04HaXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY9RV32qaTw0exm9-DK194NbTlE-4E9YEDTZBelmKhAtJ_j5kG90do-ougJdaa0GsfzcC-K65VVfBQ6uKfsVCEHlflMykONaJpyyjow85ZhkwhgNz6YTKFfLyU3Cpl2A1Zt4TNM5jH-c9TG9ZlOAnIO-7O1KL1w38Ll36o2db7YhBBk6dcjXQ0tstSpjIpQ-ePQToQ_dN4yBeGaWTaGIAMC-ZmweDk0Xe5yZcpTshtlokHywcnmkUfI_d10godRXovQRB9cSggFfSQmAMAMp9cQs0FXyc2RA3-vw0al1owD-guBFKfZQq1-uvb2uVGpNBMZTLCJ7pr99NGetd-Hr5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmCovfr1jIHaN26Ww7ap3w3_pLMhuhpueMBbIGT0U8sim4gXlENxIQperECPRHjBdglq43A-K39f52xVXkBuOsHUevZXPVWnfGLI8IzUKBzGoeNkpqUzYH3cGl6Ul2dDP1EcjhcSD-9zkZgr5lks36WlGz3pvYIKpPKeizjvzHJfIGexynisDcnN7W1nGxvCGfnFmv5wQQaI2Tt33nrtclY8QCmZBd2SflGJ4i6tfU0-sPtreFiTMDPI3yH488siaP0T5B8GoDLP87J0_4P8tZvskPsu72opfTVG_ogbFawpZl-IgWOVb2ybdnMNpitQaBBW8Uvh3X2AgtaOO-Y_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRtx5aHr2IUlU-iyFgpQUGKDhfcgiwZturWW_nxOwpun3_IsBSqS6bUYBlcpM5J5ilOyK9UQF9pgDo0UZhoXy4-Bm0NwMZl7H47gHInL8Bhykzb95PnHc7BWrXrwwM4cqQq0Ynh_rbpFD_anYoktAgBHauTwhhBeypNcafF9OPSr64j3mMQCV8vBQPkFqW3WNmGPmneyeid1Q6Fy4jaaz-B0kLRKYGqW3k3_29GO_56AAozJcuC_ft1rrWfusaYsnsVmq75rgiOPMnNkrmpSvAU5wfHnIihl1EWbtxTHYfmaDwFkZw_gOl69SqhF8-t6_O5h9XaRcod8gbxfUf_HSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L15qRdHoCjfVdQVgVVw5IrGYQUttoI4QN62RiN2MXuEeW-bR3gkIg1sk6gz5BLKNQeLjP4Hwr3dtPSAIoqG-s8WWfasW7gfZqsbPQaJrQNsUafQEVCIXsW7Sx3mh4xwjnw2te6_5YQrcpjkCToJlFJDeRccGjTfasiKCAp-foDWrCzdPug2Z6josr_6RZg0tQDcX65s1lZTs8F42ufccJ2mbPKlJbNhtLwQtQF80K3J94LDs6U1n4apZl1fkxGOHm7gW_Yr4R0tEpV4--8cWm-661v6mNaeJcV7INjDPAlsFVh9IX8FzUdmT7HLShAJP6oh2zMX_F8ZENAsMX5pL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4vihMYrB-NRadMHCtw4_NnNtQuyaVJkNaR78uoheBKHhuJaywIn-ZGbiRwzphBazNNBWii2hERxZLBMws5ZiuijYO4A9kHB-8QCz5g67GO_3WhNJv-i9jWTkshEYs2JZ2flPT9btqpBt5gy3ZiyUsZb1qR6Un_L24885TYuPZAHkOOhJ8J08ue0WFtEPxUuGnyBdMc1-KJRE0_JK6Dh5itwc7IyWYBUmdjMse_V9NB__HMf26kkNaZfdPiPr7Vq8x7BbdyDEcRlm4Nk1SNIA-dNbj8btX158B7H4ToKcnX4-Y0E8PAsrW9-Ae7oYsrbMfSeGcmytNXqbN_13nCoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSzMhDbS5My3csK8FJ4TzJsJNXIdaeMu7sYAyDNk4Gj3LhnZFncGKS2HQ_bWIRbishrU8rbG1x0ZINnoKsfrS6IqJNXZC-wAK0YLCcYUq50o3wd42eSZhs4HZwUvuk-QtCIQmWrzsqiyY62YTV-FmvQBmHeb3wucyHWF2FMLx45Sws2szvricHYcAcs5H78owFPw2swJXTXcGPFJPpqY8Pi3pSSs9681s-BX380F0wBYnKytmVlJsG-fiyje4ONOotG39MkaC2aK1qKeGY97gvPG9qMEzOfgn9NmSVhCpVFaAUEmkQWFBQN_9mXxPSwyjeERWDb9MjoQSbLmViwwaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=FZ6hrmhxLvtOq2nCHgHKxy_qHi1CySVyO9M8m9P4VgQgbrtz4eiKdPaxIuIFEoV-aha6vFEGFV8qvR7FTXu2MxmtC7AaRLe6_GHPH_ZBab6yVwhjCF7GtkBuhiq0ze1luaq2IA0NR6k3IOp-oEi5uZgeKGCQqghO4ydxRxbH2qA4mEIkrxMwyLIA1AZRJ7BNRKGEEySkWcF_6aUBO4j9xKe_yH6Kt_8I4tPC2ath2P4wOIr0tJTxgMnxu_ynx0-oM9G5NLRILuSRDwMP2-0rInYKqJbaQkwrJNeYyOdWP5sbBfmJ9Vq-Rcmgxr4ZgVfgfJzViS0GB3p4hm8vKhKEFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=FZ6hrmhxLvtOq2nCHgHKxy_qHi1CySVyO9M8m9P4VgQgbrtz4eiKdPaxIuIFEoV-aha6vFEGFV8qvR7FTXu2MxmtC7AaRLe6_GHPH_ZBab6yVwhjCF7GtkBuhiq0ze1luaq2IA0NR6k3IOp-oEi5uZgeKGCQqghO4ydxRxbH2qA4mEIkrxMwyLIA1AZRJ7BNRKGEEySkWcF_6aUBO4j9xKe_yH6Kt_8I4tPC2ath2P4wOIr0tJTxgMnxu_ynx0-oM9G5NLRILuSRDwMP2-0rInYKqJbaQkwrJNeYyOdWP5sbBfmJ9Vq-Rcmgxr4ZgVfgfJzViS0GB3p4hm8vKhKEFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFhAKHdWyJ6E6JEpwObX444gBuKNexDAdZekX0r800Tbcwy11AztIWFFHk3T9XSDYyy1Z2-BaKgcwfT4TiVA_-OTqBBv_TyiB2vxkwHfMg7AYpBdPNqHVfb1Q5zIMfWnvvYAF-EC3riQ-Ng73N2gdyrzDCahOVRBygb46bnHUuhtzAvgR0yYJnZQGCn1WY2_cJCjzCkTxYJNrqO1ZSXobBUEiEQ2ITaJ6038_ZvymfQIBKHKu9GaPxywIn4cNOaGHL1pAmxFe0OdsHuul5wV3An3zsYoPopNWt-A5_zwbpkXaD4t4Lb3aUBMXu410aLxTRcD5CEPSnYA1awbCJrxSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=L29qOfACqlwinkcpcwFXjTf2qn-eSDyRY1JRgnTsUKfAKz_P8g3pu33z060VZ5U1G7ewR26hedQNbVe09jyPlPMcXFTELIjcfylrPkmeH7rqkFa68q8zVovjREezde8lyH16rP4Px6EuIK-TAHD_IcgydD6iSsK6EacmFhgM_DFSpiPfzXzxT57q7eMS4cfs_iycnH-s-2t7irrc1HeWgQWMsQl_cYzn7ge2W3SB8VLkNViNo_VNZ5S_Expa74EU8nrnl-I8JfZ_O3-jV8JKkBoh5CvYP2-xMVKzlj_-fbQr2JWZpG2J8XeONZrc2pMqM1tzDpg9nzTHodKy56iDfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=L29qOfACqlwinkcpcwFXjTf2qn-eSDyRY1JRgnTsUKfAKz_P8g3pu33z060VZ5U1G7ewR26hedQNbVe09jyPlPMcXFTELIjcfylrPkmeH7rqkFa68q8zVovjREezde8lyH16rP4Px6EuIK-TAHD_IcgydD6iSsK6EacmFhgM_DFSpiPfzXzxT57q7eMS4cfs_iycnH-s-2t7irrc1HeWgQWMsQl_cYzn7ge2W3SB8VLkNViNo_VNZ5S_Expa74EU8nrnl-I8JfZ_O3-jV8JKkBoh5CvYP2-xMVKzlj_-fbQr2JWZpG2J8XeONZrc2pMqM1tzDpg9nzTHodKy56iDfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=SLgKJ3J3cQiYCZ6BCk8Earh-g3ARu-SW1MAcArlKZdNZb9jsnvta-IxV0Ec6l5gvaYfEzZEYst2oZzZJRjwbMA4pidqULhmCHfJCNAXfxOPsMtCYwR-RVQH8x9jhJYybHqbJFtgPO3SeD0t1gNEI73ieec229Sr3TFSiKkjM9jxGq7hweZEBpByuOxAouA_lvpmN0N5SGqLER3ip9jyPGeeoB-3QDCylnVjkCpmpnKpVXpikW5DsOeyErAkMvItJyVMeWPBQ11ky4RbDKfEDDWnOSinzS4kNNWp7WzPx2TYyriRHbQqbWVcnZkfmeLsmMpyHsZSjOekazkAyH6wCkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=SLgKJ3J3cQiYCZ6BCk8Earh-g3ARu-SW1MAcArlKZdNZb9jsnvta-IxV0Ec6l5gvaYfEzZEYst2oZzZJRjwbMA4pidqULhmCHfJCNAXfxOPsMtCYwR-RVQH8x9jhJYybHqbJFtgPO3SeD0t1gNEI73ieec229Sr3TFSiKkjM9jxGq7hweZEBpByuOxAouA_lvpmN0N5SGqLER3ip9jyPGeeoB-3QDCylnVjkCpmpnKpVXpikW5DsOeyErAkMvItJyVMeWPBQ11ky4RbDKfEDDWnOSinzS4kNNWp7WzPx2TYyriRHbQqbWVcnZkfmeLsmMpyHsZSjOekazkAyH6wCkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=K46Pjg1LhdC1j1PS5ZGO_UU_YIWF4-cPwr_L_DbD1JekBntyd3rjhrPd0VIbdvB9Qd1cCX4VbeFLW2BE9JBXTKbxyn5M4ePE67Weelpw7HqJ_j_J_saxpcRZ8Goojn5ZTkiU7eaxmhZOAGYR3LTmlLhubcyGNnDdkAlylWI68nyG9QQ5yFIm9x-CjNgbPzBOhXIPtVmNC5g8ey5MqaRZVSOAJRdxfHK0Lx8aQvwkmScEpI41OB5jb60dgryL4Y7sWbSdezkk84aM8Co_amktM4wBbpKVs1SLijcWoMR9R6nYaNMIeQRlVNSW6ek9GqgjQPssqF1A9fF6XX8nnOkjfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=K46Pjg1LhdC1j1PS5ZGO_UU_YIWF4-cPwr_L_DbD1JekBntyd3rjhrPd0VIbdvB9Qd1cCX4VbeFLW2BE9JBXTKbxyn5M4ePE67Weelpw7HqJ_j_J_saxpcRZ8Goojn5ZTkiU7eaxmhZOAGYR3LTmlLhubcyGNnDdkAlylWI68nyG9QQ5yFIm9x-CjNgbPzBOhXIPtVmNC5g8ey5MqaRZVSOAJRdxfHK0Lx8aQvwkmScEpI41OB5jb60dgryL4Y7sWbSdezkk84aM8Co_amktM4wBbpKVs1SLijcWoMR9R6nYaNMIeQRlVNSW6ek9GqgjQPssqF1A9fF6XX8nnOkjfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCMx8cqG4hO7cLXgnHx9DI6SqDKC1lXkyiOAMlmipIjBve_iWtiIW0COTvc7MiD_1bsvzfGobjQcHTC35ymd2VnaRxW9dDPaagW6DIkZwIR5aznSPUM2Om1r2lzpDeV_6RaLT-teaYXb9lljTLfUmy-YpwXsO0aKY_hAYv7WeJ0dhB-bebJ7JX2zmjkVOD2HzDLaHPgPqd7vooGt8f98LZWiHOe7imeqKKO6JSuCUnVDGj3qhsw2ZqbH9Uz5oc2nlkTsl5FkXvyPiMrxL4jpkuLxzH9V17Y0iwn8ulnijapF53c8t0B3uh4xnx3GxwtXFJMPzg5HiHRFXze9qxsl5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jtZL9DmVjmsJ__tWH-AccVhqAZRc_jcpAuJVDSFWx-533gFcn0fwJRMpkVftU_2Jjtv_othqbwh2r7j84cqM_7ek3NWFsM6DTmdxtQfF2sBGLrYTVH2sP-C46dIpJI0Gj9NubyLTF5jF_QYEfIT5cmvZDcHWjbuBXffm1jm6QO4rSifJ4PYsh7siqhnifipRNtnvwvXGtc8QT84MIGGlUa_yXZLAnM_GE38EJJx1y9UeJagtixTKjkgAGzLpisktCj6R9RUhsVf3CoiminEQO8nHQ5s9iegWhPtrMiqyZ6jhOftwywuKoc5TOhd_YIiq_SX4XkHKnBZZiOioNd2I1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=a-WkQiqy9Kur_-oZBT3t_ZYu_XnDvPZDx2H673_I9Tnk-mWhyEhy5NnTJUlokbcWafb7HLkyKOZj_H0MtHsW-QT_xRWlY9qtHVRXMs7S5_d8eHyr2TuOiq5UVJggF6RoreWIKcwRlDPpH556w27kSD9vyzQpttx0-kBsvGDF64nb42PW0DAP4stN99ItitiXKaYHglFFOoDtEyhlrF0ADZyZOejsVHKh5EiQmc3Sx9DedLBYxhMVw4LBi8bFh1upKf0QNpHJ6m7S5r-lqA0pudvtw0p_oH_-Ibdh7JUEg7luUZ2RhwChTZJzy1N0tHll383RSvitKx977Mzj7-h8Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=a-WkQiqy9Kur_-oZBT3t_ZYu_XnDvPZDx2H673_I9Tnk-mWhyEhy5NnTJUlokbcWafb7HLkyKOZj_H0MtHsW-QT_xRWlY9qtHVRXMs7S5_d8eHyr2TuOiq5UVJggF6RoreWIKcwRlDPpH556w27kSD9vyzQpttx0-kBsvGDF64nb42PW0DAP4stN99ItitiXKaYHglFFOoDtEyhlrF0ADZyZOejsVHKh5EiQmc3Sx9DedLBYxhMVw4LBi8bFh1upKf0QNpHJ6m7S5r-lqA0pudvtw0p_oH_-Ibdh7JUEg7luUZ2RhwChTZJzy1N0tHll383RSvitKx977Mzj7-h8Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=IQJKbFUemHWHqJ-6EvWmerJ_P1Y4jS_rkYxH0_h07rNbE6Gn4LPWzYrx1B6Exf5HS9Z8cQ_JwGddxTAmm7jyOv_iKSAiE70YWpU2HiXl9KctSgwyipKofLp2qWPd1CbSl13OO-MdsdcgWGBV5QePXUdUrTIXFR2ZYkjuXvx-37rx2oNpLpXwtrwAA7ffQZyixd8yhH4ZTOlsdJzlO-apqPzjZ-ERSrpu9aZd2AqX4boh30YY-Z7MNkf4ObUZBINr8Go-if5nInve3sXrFKHdpaPzqj_HqzIZmvoXjA3G3SIpDPveN1AWOjW8O2u8yP63mIkO9bV9CEfYqaGw6WPZyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=IQJKbFUemHWHqJ-6EvWmerJ_P1Y4jS_rkYxH0_h07rNbE6Gn4LPWzYrx1B6Exf5HS9Z8cQ_JwGddxTAmm7jyOv_iKSAiE70YWpU2HiXl9KctSgwyipKofLp2qWPd1CbSl13OO-MdsdcgWGBV5QePXUdUrTIXFR2ZYkjuXvx-37rx2oNpLpXwtrwAA7ffQZyixd8yhH4ZTOlsdJzlO-apqPzjZ-ERSrpu9aZd2AqX4boh30YY-Z7MNkf4ObUZBINr8Go-if5nInve3sXrFKHdpaPzqj_HqzIZmvoXjA3G3SIpDPveN1AWOjW8O2u8yP63mIkO9bV9CEfYqaGw6WPZyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhpeT9Xajrjsd8HyVD5jGWQTXzN3YUH6KO4ejk1i-R83zhmcBkyYtJDyw9l7ZjfCCPp3mEYeWU67BmIpo6PSow0ekg9rIfel42ra59AlmCFmt2j-mCUPmrOLj_9RMLUcYpPW9F4KdUcN380tlyCZ0FfZA7yQpuiJM8c5rPqCIejrlQaeTikSv6yFu82Mq2ZTe0aPuhbMikLHhopAkQApc1eT4LlnnM1tj-wH5ew3DSQVBOSem9zoiHs-bi6RxD3HX4hHnOeCCU41xas2gTVXWl4Velf32KelVvwfeNBGkz-IpY--RYGlPvGErMKpPtLXno9HAdXfosbNThye9kvEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=YC0EN8mXwakJO4LXgVxbvv1dvbY7sYmUhtxEeJXoTsyvmYjg1yWsoPRduBEcoebPAASldjZBRaZjpXJwFn-2_NXwpo8-nE1Y_-bXixFi8d9TWR8C2ij_fZvow3bx2Q5KlaIMtGoL4WDJ32HS1cqMXijKxwN7YtnbvhbHSzsBzt1lFkLyYQN9y-0cX1mG_sUtOprkjz-h-YUPfRE82-pi0TlHUx8JoYgtXVp88BZY226RpKWFy7S6qfcUmOh8Ez9wAcTxu2d8L3hUerk-VJUG-5ZUEpwcusQos2lURYx3q8CpJaM7zRfOmpkrzAOnT_XPOXIMA0HvHUFz3tloBoOQrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=YC0EN8mXwakJO4LXgVxbvv1dvbY7sYmUhtxEeJXoTsyvmYjg1yWsoPRduBEcoebPAASldjZBRaZjpXJwFn-2_NXwpo8-nE1Y_-bXixFi8d9TWR8C2ij_fZvow3bx2Q5KlaIMtGoL4WDJ32HS1cqMXijKxwN7YtnbvhbHSzsBzt1lFkLyYQN9y-0cX1mG_sUtOprkjz-h-YUPfRE82-pi0TlHUx8JoYgtXVp88BZY226RpKWFy7S6qfcUmOh8Ez9wAcTxu2d8L3hUerk-VJUG-5ZUEpwcusQos2lURYx3q8CpJaM7zRfOmpkrzAOnT_XPOXIMA0HvHUFz3tloBoOQrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGcjBDMwSCovfmDk3yYmcTecjIj-ykQ6eMhPUZ65QmT2e4bBBjRfhtrZlelj0HS3QHmT5swChxhCbtpbYFzPmbRTG8XAFMtG4EOwylN602MhLguxEoIaSBaj8zNOtOgF-wJ8A5kB07Ofu604MjPx4H7DiKW1QDK5-_wg2p0UrrRzm2OnJWZQLrFzy0OfZ3kntITKIg0WOC75OHeVuyDH0NAAqQgPmw0R4OlN2oBvgupv3MDUoDuPPVS1uR8CCKQZBQ0kVVUmJiXT4U1oH-y4JE6P1KaQ873RRDs30xanflvjCw1O7SIbUjhtekt59hqsH-lCWahz-Lrs7r6k5PLVSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og7I3n6QKQiGr-FTo7cQRAAOWzi972EX_dU2qKkkR6zqfKaL1lj_UcevV2l3zSZKGstPjFSGibFRYUB24-jx7DDiQjI3ytFSY_VEYfEYF5U7l9MX7r6j4vHsPJTzVvoTgwp-z4kbmuhrzkFs_7drXREx7X3Itd1Y224pdxva9-chj_-FN-0iO7fVYq-F9W2_eLUW0WPcPCZLXg87TqxFJr_x7iMfBUUU9kvoanrNQtsfL_10x98YbHWitEsGXXrZ-SHHUmRtXa6eb6fsdVn46JDzgKMDq9OyUZ5VGybEfuEYSYqYBz2HW2D4mWlye2G4lhhkHX2_0MZ0bzj1ztxVnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXRfkhqOdPy1bjrYPJp__MN22KPych-rPrp-lwEr2YCpq3Esvoeo1St3yN8CwcRqvuvSn3FCinv-XuHbcrVw7CYEJrsxSfmh6QvXuEGyQqTf1sXvJepMlD8YHZeauLeJRljRjt4gIW9ceSO6Vvvnu_o0B_b_c8TGoGmN_wRmoCaCab3Q7QPrJQEX7_gaTtCCifbkjVwy0PsPtwevJr7STArH0wtPe8g5eAEa_XdX6nMO7d3whDr3M-hs1H-IO-pv4la4TqY9s_f1JYN5wtWlGYdT7YeInk6ou7fw-DjVgMPGT4T08np57gm7UeUh3n8Bo7uAvhSr43WnXODBg0OeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuzTtR3LMUWixOm2RQHBliBgNmiD2mt3_n9jMa5TYC_Y0xjtqE2IAI8a_ieoObOnRCVF4NMdn9JYB-RPq7g3Kz3-aW3963BmtUdungyWzFKpEnR1RCgjb6VuGfvV_AZpDmIjGwMb6Ztw67Z0unkLiN2epncxffHsscRJTNURz8jklKoLam3rgwVQM1Yrp7BRRY5FvFb5tBmsIkBHfiRl8OwoYcab41FNTVJ5owFrlCiAQQjWPYk7C6txB-zzGoL1p6h03t54q5k1NDnVLDGkZnMR4PIU8RIKAt3qORI1lkU2KESABSjVLq0fiI1PlsF3iIgTTAoxuHV_zusBscB21w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=rJaB2gLtZJ3ucJz0zGmx0-9ELQm6iiSdkaQd7cdvGgsPeJ1FnMaCkoERunBZKdPRX0mwZMU5YyFIm5NyzTAwoqw5s5w5FzToHipiQ-qRGiglE5g4btewH0eq-hz19p3uGtoOA_VRgAQQMyc_MrWvD6k11Bm41T972d9a1q3VFn062tp7GpXTd1c9Q8dYW5Cz_lFH1pFQki2xkAnQl6AdDDXgc-wqy7fY99anPc_NJgV7P6NfI11RtBw1aV6JT7VK5WTaU1nFaWF0oQmR-ig9hFhmEXwHWaPFRx3Y5ArRnHX9OZk8wa_9BorBXUe191DkQvNOB9KuJ0UK_fRP69BEcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=rJaB2gLtZJ3ucJz0zGmx0-9ELQm6iiSdkaQd7cdvGgsPeJ1FnMaCkoERunBZKdPRX0mwZMU5YyFIm5NyzTAwoqw5s5w5FzToHipiQ-qRGiglE5g4btewH0eq-hz19p3uGtoOA_VRgAQQMyc_MrWvD6k11Bm41T972d9a1q3VFn062tp7GpXTd1c9Q8dYW5Cz_lFH1pFQki2xkAnQl6AdDDXgc-wqy7fY99anPc_NJgV7P6NfI11RtBw1aV6JT7VK5WTaU1nFaWF0oQmR-ig9hFhmEXwHWaPFRx3Y5ArRnHX9OZk8wa_9BorBXUe191DkQvNOB9KuJ0UK_fRP69BEcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=AP9ulm7V6ERV-D4gjP4SxiqPMIKtw8SiE4A8gmkazNEpt_j5h2WuLY4ZG3xgFEV9v8o8sdYb6BQXDQFcTnfaqvWRYR9h2w-3pNxOrcpbxrSJPJusPCskjVHXmzknRFf-5mVaVSFEvnqJVknyG35Esc5aLZqR7vbMsKPAinbU_7zoY9pWb8ch1Suqkoe3DW8XvuL-WOP0F3yYLYF_gD7vejYQB0VnSEUzQTBGbqEEUoGNOCG1LTmPDY0r0xJ1PuBIx-ezyNeAnWIH0cKWz1SMYrrYIr_7lEyxG3GZxt--VU8h4drCr5LG3tSkTqd3FALTXuyPaQJdgcWB5XuaYnOvgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=AP9ulm7V6ERV-D4gjP4SxiqPMIKtw8SiE4A8gmkazNEpt_j5h2WuLY4ZG3xgFEV9v8o8sdYb6BQXDQFcTnfaqvWRYR9h2w-3pNxOrcpbxrSJPJusPCskjVHXmzknRFf-5mVaVSFEvnqJVknyG35Esc5aLZqR7vbMsKPAinbU_7zoY9pWb8ch1Suqkoe3DW8XvuL-WOP0F3yYLYF_gD7vejYQB0VnSEUzQTBGbqEEUoGNOCG1LTmPDY0r0xJ1PuBIx-ezyNeAnWIH0cKWz1SMYrrYIr_7lEyxG3GZxt--VU8h4drCr5LG3tSkTqd3FALTXuyPaQJdgcWB5XuaYnOvgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSaB9ZTrFGnYZvEWTFzvySnHiE9Ye-J8oR8gGqUZ225jJjuivLdIHpqkflbMra-uTvBEc05Ixg8GWX4J5JDWwwpZWNHXKRHEZt1zNG5LyU5-DYOQEDlPDxxhtrh7N3df-cz27XQs2tCq6E1n2oXgLIt4KY0u9bQF3uoV2tA92ffewIyhgGf9CAEoNqPO5C4wf8aqIQOStx6tgRkIwfZL3-cWNKF24RAZyIvwSBw0to5lNxMYQaPue4dfHmstB7uHJ0LHVlZH14g_7CrZnDkw-vo-F7NzSymcSmCSwgmVBgVghLZj15WpNFR7AZBTKRs_vshu-jWKHKzFtuZ3wKwCiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vxgs56fH7UpHizjYRNwr5J9peazQHBm_Ro1i-tfhYrjtACOCl2pA8xP8RFhyQV1WwrxwWv7CV2-tDtsorvPInUxgCObC-2iFvSw7zrVbk9RfzcCo6-PT3Oz1mDEcO35cyJQHAOM8sSxRyq7g70bAMxucCMhZGLftl7jfL2Mpl7bSWlKtecIulCNLKVFm66F3Yk0vFnreu2gGNodnM9ipCQUPxvtQDNdA2ub7FNZc-ZMr3SlgwcTDffivfUQJhX5nSyuthdfX3LMbBwbbn0EYdb-2-d22SinVtScwR419dC-PshalbLGcvcIgj7kXpMA3QV8XvSfcZLYUyrnH-oVeTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5DFD87GM3HLPTqLEO3ovEJykEh-loANLv2kRdKjACx-bwVV1Bo6WCKGQUbFcjEQDFkdI5yrDDpqrrGlefLmwq-KXmj1uSbeqCrdYxVrPMvPUgMEjxRP0Lp9qsB5Ue6bzsk1F_1N1nKXA2jOWjq5g-KGjbN1Tj-PE-svWUEQhQTHQgrLEHtsbbJQSuIeg_rUXpn_zVdcR79FtgjJNUZZO0E6ePFZQqgYSgrcvEOLi0Z-hndxN6yJ9HC4y4uqIMe4AdBKKvEsuy5rKTpFP7GW3DVyuFpAZyk7z_NecpeS7wuk8OrL6fYIh27xdMcaQsrEmR3Lf_Uq7gT44fRjgSFgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPU8NtE-LvY3JZZp6owS3J5e3aeKG2Un52RHsdGUO5RQzDJ0Wk35WJofNAeRGTRF2J3XNLRYhkNdLlVVuxixfcAj-1VOZkG9KzhoMGLqM9JO9gaXdz1qQf5YVwG6PuG0d0v16CRCzOtxgQctj6rR0ORLxxitQFVx8ndqihwhffkI3FBThPj22Gw2xClooyGSMp0oDIvhhEnteSqgYLvxz3AjKcILdeBDKtDMUcJwYFYDKgC9zGTC-NWPmm7il95JvW06D__nI5sjDD8dqX-8DZxyiKbZoi6K8yGmkaFoGbl2ELh5thiwZeBkam_vyELK0TGO5Ho9XYyKEE6B_lX65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
اسرائیل : پاسخ حملات امشب جمهوری اسلامی را خواهیم داد!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5364" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnram3TwDOTBTUtltAoTWlvIMuUxf8nsHrNwcOIaTBhVUBDVA0CPl6exqsorwRWNlE-iOd4lP6cnsW60BgCUJ6fkSkEIm9or9NPZRnS3VCAZRZbmCJReQiZpxutw82xvi61V-IsGX12aZCnVeTqovDyoyatg5KRmFw1AlepQOZ67868iZDg4dMhSs0uyQlkQa1eVTEp_kw8o0_Xw1KmpMpmvMyuivGcAC-Hd9mAOAi74qt-nhDcAjVQyY2A3cvAO1BdD-6EeetaGPE6luwdg2P8UfTVuGRPOyZwPhUIgz9FZD9iFTRhfuRcfTWdrFzkMcFBgP8Ua658B9G9uMncShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موج دوم و موج سوم حملات موشکی ج‌ا به سمت اسرائیل
توییت عراقچی</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5363" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
منابع اسرائیلی : ۴ موشک بالستیک به سمت اسرائیل شلیک شد!
دیشب نامه مشترک رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان رو تحویل گرفتند، که آخرین فرصت توافق و گفتگو است.
امشب جنگی تازه را شروع کردند، این بار برای حزب‌الله لبنان!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5362" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl7oRB59gSOmEWhQcs7gWHSy0rcfy70QxGtWytzBAfeQncO2wFMx-KYMJwT5oF7-dgdJlbzAsqtXjXJxNjeReTz8w8t3PusFmwT-m2zXWDLRgs1GJRthVEBcGJ2V5jruHW56ElR4EonYjlPzGiitFGaTwYKIg-_zbJlukdaAJeIRo6XjbzvuhjXfaO1_rq4CoTJOCAoPhkD9foqf9a0oos3aL1-iBA1CjwEQQOHm8hnVAfNlFD-HfLfRlyzzncDMjXwlVUTyMx6O_ol9M9-pV9R83m0BRJMPS83Ej50dp1OQc-PFz6yvDuN3nwybOveVr8uHTzYUAoscx8Njv2yj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feRZnsCkDn4Vb5cloQyxKGdxHbP8d5lGfPxX8T045DHz9v9iOaJuv05S4HGV51uxHmdVsLgIYj6YUq7J468LbalxdVmtnRbsG5WUZloFFHewBL6omZS0oUXGbkT4KsmPEAMfqhuCwKgqeIVQxSlIscywlxWcmk2B35mS9UbXfCL2OnzGqjVI29nZtm4Z6CfJmKmPtaEbsDN2PalQrk0dsoPqxKS0Si1im5IpuXayDweJFKuABe_NGo_-lhbsmKti7Rces51Pu9631oek8PQhwAJpfdLQeGJgj8FK6ByzjK7WitVmuYNGgGZSpFqcgWllcqZFxlVl1G1mSMjv7BptcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dvd3Ego77pvRn0iPJ0haR_bdjOI-OF-TJGTqc6cOGrFXUarNDya4TBsxTVj3Qy32XH4mKH0wP_kkdLpn3ApnfSm4qYhbm-pExvQSe55STJTaLjE9lZfhKhRkfSh84u5q_A0rgr_aQyCLeFPr7AwLh1wLj2xCqA_ieOX79d_hczteIfwzLdjzpE9JbGy4V0G_QR5R1UhOJ33Ou1QwxBJzRYWE5trtPlHqYT2yuLduDtfuM3yIu7DZEuxnlfbdYewe6GfTtI_RjRTPCH18z6QDEnBizdYLeC1vHMSXxMlJQNy3r8hdgJ_lnw0F5AuHRrN2r7gvIYayQLAOKJwe0c_rcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfKccuUbFXnGMmfoeZ_XicmrFF1_p9ll1KXCDryfOKrpIEisKJpKQNdbvm5cqOOgRTzmZHH3HPZ5VPl2va_NbGwfuh8kyxKVToWLL44IS_TbKgRo-jolHm56sjKVLGTvRwE5Cl3ptHyrejzxKo9YVL3Wf37N8j6QdeKWLAhrpJqtUK77qty3cHNAMK9Sn6nyDssUENQ3zwDSzgS30jYti53XO2AtqnDay06DeIBNdiMJ0vHrODF5rye6NmVoOW6lLX0gmSx5T82EJT2Khws2Mhotgprb9R2n2XTGq2jCNexnW9lhxkIwqGpKTGYvaG30_fq4Av2S3savnzMQIxByzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=Y8BAgIADNrURXVRDz_DvqbomYbM7ZM6jL4ilI0Bvb5nfQ9g04kmvdhTgDQFtHA2Lli2kKQq6uLNj9mqGTwrq6ZRVBvxgDZo4C0_DI-R1-dZdeIc-PmkI1L0pI3rpvrmtabCIbzT__c_j3J3U0JIV40xe7wDWmrYGeth1xgVOjWztxuJfAzx8ykd8mFXvmVPSmWGWJfzr_B-ZbpWnzQcKGDcu-TnClyzRsEUG_RPZoA3FhsFG7RgbmsSgF77HBea_3NUKbjap2_HKRtrdSUwL6Nwnq67epQ3G_n4vmtAw9cn5AO_tGGCzFx-inQw9seDbQYrI-22xjCwXPSch5AJOHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=Y8BAgIADNrURXVRDz_DvqbomYbM7ZM6jL4ilI0Bvb5nfQ9g04kmvdhTgDQFtHA2Lli2kKQq6uLNj9mqGTwrq6ZRVBvxgDZo4C0_DI-R1-dZdeIc-PmkI1L0pI3rpvrmtabCIbzT__c_j3J3U0JIV40xe7wDWmrYGeth1xgVOjWztxuJfAzx8ykd8mFXvmVPSmWGWJfzr_B-ZbpWnzQcKGDcu-TnClyzRsEUG_RPZoA3FhsFG7RgbmsSgF77HBea_3NUKbjap2_HKRtrdSUwL6Nwnq67epQ3G_n4vmtAw9cn5AO_tGGCzFx-inQw9seDbQYrI-22xjCwXPSch5AJOHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=GfgAd-fhzbgudPMTyJE1rQhAiZcVf_hMDIhQ08M5aYDAF8-nW3saPp_LQnhuO03Rm9TAoKuTbmSruTvyQrRljwfYfK7CS8iH04ZvRyFz4MwL9OeDlK6Y3qP6YNH9tccmrOKfeTHPXydO3A9b7xznUDGOTY-ZqRIi1tdgage3TAfjbvz-ouV_sgVLSv98vO7sGq6V8TVkvSl4c-nK2dKnmqRLVejpcGfXqsh7WiEWBg0rbMOW9U-Vn9mkbkqXkeDKP_tnANXrfFo2ZVOqj8xgWnfXBqpVNlkIvqz8bSmBIwAfcnQlkHw4tfg8yCgcviPYK5Sgz8LUsLKsDie_YLtPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=GfgAd-fhzbgudPMTyJE1rQhAiZcVf_hMDIhQ08M5aYDAF8-nW3saPp_LQnhuO03Rm9TAoKuTbmSruTvyQrRljwfYfK7CS8iH04ZvRyFz4MwL9OeDlK6Y3qP6YNH9tccmrOKfeTHPXydO3A9b7xznUDGOTY-ZqRIi1tdgage3TAfjbvz-ouV_sgVLSv98vO7sGq6V8TVkvSl4c-nK2dKnmqRLVejpcGfXqsh7WiEWBg0rbMOW9U-Vn9mkbkqXkeDKP_tnANXrfFo2ZVOqj8xgWnfXBqpVNlkIvqz8bSmBIwAfcnQlkHw4tfg8yCgcviPYK5Sgz8LUsLKsDie_YLtPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،
عراقچی ۴ روز پیش به شبکه المیادین
(شبکه لبنانی با پول ایران) :
اگر اسرائیل به بیروت حمله کند
اصلا تحمل نخواهیم کرد
و این یعنی شکست آتش بس
(بین ایران و آمریکا)
و نیروهای مسلح ما پاسخ خواهند داد.
به کشورهای دیگه هم‌ گفتیم که در اثر اقدام اسرائیل جنگ‌ دوباره آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=HrUHT--ALaodzxJCy7fUOdjV9d0BgdrolLNAk5jZzcBNDrxGTk_KWr2bas6hlN9p7loxiM4AqxoyKMN6Zg63EWmzHfQkjWVP1hVRndapEfixj8bjPQ0OKBDkRm8JkDg1WpN0041JdSn_XlJYeCehgKNOgKmAY6DFHQFnOh1YZCkl7gBKwMIMEzChvHj3OnLeDeHMzgRkBeO3He5tvp9Oxg-riAIxRzuoiZ3s4k1hjI4RvFYVP06uYi1R5tJvq9Vx02VNQ_RwBVi5JiD1akRW9a1F7rmY9sMTfVC942RpGPZr4WxzmmXdrO6k1d4tpF0beTq6oOsRcHKfH_7zaEQofYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=HrUHT--ALaodzxJCy7fUOdjV9d0BgdrolLNAk5jZzcBNDrxGTk_KWr2bas6hlN9p7loxiM4AqxoyKMN6Zg63EWmzHfQkjWVP1hVRndapEfixj8bjPQ0OKBDkRm8JkDg1WpN0041JdSn_XlJYeCehgKNOgKmAY6DFHQFnOh1YZCkl7gBKwMIMEzChvHj3OnLeDeHMzgRkBeO3He5tvp9Oxg-riAIxRzuoiZ3s4k1hjI4RvFYVP06uYi1R5tJvq9Vx02VNQ_RwBVi5JiD1akRW9a1F7rmY9sMTfVC942RpGPZr4WxzmmXdrO6k1d4tpF0beTq6oOsRcHKfH_7zaEQofYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو‌ رستم تهمتنی،
«چرا دیگه نمیزنی»؟؟
بله جنگ طلبها دیاسپورای ایرانی بودن!
نه اینها که ۴۷ ساله سیاست‌های
خصمانه و جنگ طلبانه دارن!
در دیماه وقتی مردم ایران رو قتل عام میکردن «حیدر حیدر» میگفتن، یک ماه بعدش شد «رستم رستم» !</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
