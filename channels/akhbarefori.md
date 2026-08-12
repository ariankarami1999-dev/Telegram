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
<img src="https://cdn4.telesco.pe/file/ijZjUCWOaUGUBrkIKEiBM-LB4InkCqHDMKWELpCmjfsxy8JxFwUGFngdG57_LyIojg-36d2Yw8HLDSX-KUJGfui_uvvgfNtXP_VBQmtISnAj81pi6z7Qozoiyw94bibFykJCTKqqJkHu65CJaXYFNoKgXd6cI_pPbvCLfPCO7_DjjUbla6uEe9qf-1006_dBPf7LCYzCSBXa70oB4rymLwaBjQqNNcSl3-aDmeNwJg-3aIOMAs96Un5AgIZUxgh3Zo1TGDxLERCTJI7_TYhKnmxqooRba0HBh5I_xXJFFtKH6coKxR_OOsSDYztMuWob3J1IfDWg_mLTnUCV30Ew-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.21M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 19:54:24</div>
<hr>

<div class="tg-post" id="msg-680660">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTLC92rI3Ligwqk5Va0r0MfUufnO0G7y6uFOTkt97CwY8IIHl4SxpYqHGD6oJEz0Ivyt7QfuiyARz-s30KBUmdFBD78x7iN9Lq0W0miZcrGojSCadT1tESkYIIiFkLhmM-3f7EGpnO-bwm7OmQtlZmnPB81W-c2B_8yAJXJNj__13mQbHrCEBzMH9iQ8eBiO5UGbiKNeZ9yuF_M9CYkVt1eztIpHqiJCCFeBvvm51GJVqtKeMj9ChqsBkKDZVlWk3KoW7buQ6aZdUfRP8M3QycHwcb2rqa_Ria8g-KrI92FdK93IUU8dhKpbqpGanW7q3SZdchMi_ocjEuINXrRfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفت‌وگوی عراقچی با وزیر کشور پاکستان در فرودگاه مشهد
🔹
عباس عراقچی، روز چهارشنبه پس از ورود به مشهد در فرودگاه شهید هاشمی‌نژاد با وزیر کشور پاکستان دیدار و گفت‌وگو کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/akhbarefori/680660" target="_blank">📅 19:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680659">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
گزارش رویترز از عملیات «مخفیانه» بارگیری نفت عربستان در بندر ینبع
🔹
خبرگزاری رویترز به نقل از داده‌های شرکت «فورتکسا» گزارش داد که تمامی عملیات بارگیری نفت خام عربستان در بندر «ینبع» طی هفته گذشته به صورت مخفیانه و بدون اعلام رسمی مقصد یا هویت کامل محموله‌ها انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/akhbarefori/680659" target="_blank">📅 19:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایران را با ماشین‌حساب نمی‌شود فهمید!
🔹
شاید مسئله آمریکا، قدرت ایران نباشد؛ مسئله، اشتباه در فهم ایران باشد.
🔹
سال‌هاست واشنگتن با یک فرمول ساده به جهان نگاه می‌کند؛ فشار را بیشتر کن، هزینه مقاومت را بالا ببر، و سرانجام طرف مقابل را پای میز تسلیم بنشان.
🔹
اما ایران را نمی‌شود فقط با ماشین‌حساب سنجید.
🔹
اینجا، در کنار اقتصاد و منفعت، مفاهیمی زندگی می‌کنند که گاهی از سود و زیان مادی مهم‌ترند؛ عزت، استقلال، حافظه تاریخی و اعتبار ملی.
🔹
برای ایرانی، عقب‌نشینی زیر فشار خارجی همیشه فقط یک تصمیم سیاسی نیست. گاهی می‌تواند زخمی بر غرور جمعی تلقی شود و درست همین‌جاست که محاسبات تغییر می‌کند.
🔹
فشار بیشتر، الزاماً به تسلیم بیشتر منجر نمی‌شود.
🔹
گاهی فشار، چیزی را در جامعه بیدار می‌کند که از جنس عدد و نمودار نیست؛ حس ایستادگی.
🔹
تاریخ این سرزمین کم شاهد روزهایی نبوده که تهدید بیرونی، مردم را با همه اختلاف‌هایشان به یک نقطه نزدیک‌تر کرده باشد.
🔹
وقتی احساس شود موجودیت، استقلال یا عزت کشور هدف قرار گرفته، شکاف‌های داخلی می‌توانند رنگ ببازند و صدای دفاع از وطن بلندتر از صدای اختلاف شنیده شود.
🔹
این همان جایی است که شاید محاسبات واشنگتن به خطا می‌رود.
🔹
آن‌ها ممکن است تصور کنند هر فشار، یک ترک تازه در دیوار ایران ایجاد می‌کند؛ اما گاهی فشار، آجرهای دیوار را به هم نزدیک‌تر می‌کند.
🔹
ایران را نمی‌توان فقط با هزینه‌هایی که می‌پردازد سنجید؛ باید دید برای چه چیزی حاضر است هزینه بدهد.
🔹
شاید قدرت واقعی یک ملت، فقط در توانایی پیروزی نباشد؛ در توانایی تحمل، ایستادگی و حفظ عزت در سخت‌ترین لحظه‌ها باشد.
🔹
و اگر کسی بخواهد ایران را وادار به عقب‌نشینی کند، پیش از هر چیز باید این حقیقت ساده را بفهمد:
🔹
این سرزمین را نمی‌شود با فرمولی که برای دیگران نوشته شده، تحلیل کرد.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/680657" target="_blank">📅 19:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjDuz_vK7YTLQ0WKSYUFbvZb9Xus5sVYJ36KTzdpKDs3oliOGZNIz7DgK-5HEex7nGHJvClGxDxiDObXjvBeT1xnM25kXxUcMqQE8qN7CdoqW-Hexl7OuSxLkFw9In1SI8uMyMBy7MbIFVRC_5hBJz8C7pcSV_SZ_BXSX1ZryBLom9VQ_UC84n7NMFS5rH0dBnQek6a2sKidjliK3k_3MIYOM1W2j_f6gLQmFI5X748x2efYAjLDhiSWLFiLmdrha-pt4ailNxLlA0aUt5Tm6zwRhpHCizPRQraryNqSXa2_zqY1K33IqtXCK-wSLP0duNRoZcB_q-DTEPTZaQC8tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بارزانی: ایران آماده کمک به عراق است
رئیس اقلیم کردستان عراق:
🔹
مقامات ایرانی در جریان سفر اخیرم به تهران، آمادگی خود را برای کمک به نخست‌وزیر عراق در زمینه «تمرکز سلاح تحتِ کنترل دولت» به من ابراز داشتند.
🔹
مسئولان ایرانی مرتبط با پرونده عراق، تأکید کردند که اگر هدف کمک به یک کشور همسایه باشد، آماده همکاری هستند چرا که ثبات عراق به نفع ایران نیز خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/akhbarefori/680656" target="_blank">📅 19:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce5db6d5d3.mp4?token=v01cDCAOEWGRl4JIaEJB0nI6e-mwS2hohAwuxlGFaz2Zz6lVQnPQRWpebglFTnxq1qW2lUnI1WiLMDj26hpMpnp1X5tKJ-bMtXbve3I57T1MQLYgdsX32ubAvLp2KWQcFHhWtMUmDWY3yGPyC24O3H9ISNKw9_u4w6gPg2xndrT4ic7Kn3lARW5xoZDDxhypYW2inIT40-641tShYRR8Nt6LMKd5fEBPuKwlERZ1Hv7dujo92gKDLAsaCxAMd3VeW0TrY6VMHkHsagXH07WGNlLh56dA9XU3oQxzXMBbSO99JKQYsKI_bzJAwd_6ZA0vsNh25eLamlgDqmGPMHJYUj9qxZtqMFhYEv9iIZ1W8hb2uH7KXGIKM33OxjWdLeP18hI3uxNnsK_2poGC_Mk00RRA-E8Di1dcFN4cDuznXJSP-R9h4Nxe_ocYXX5jXuZ6Ac2xt1Dk8o9G-tfWCwEYZO2YI6iUi4ONV9FYMl-nsB69nPm8bU9C_DPmbVRKDtr8aKPoEG--0R3DiBIPYJTAu4FC1spLtJgArjRy1dXv1btwWmlWiMqvZ9QhiZk-4r1y4MSBKBeaVtNvKebG1CPD-gCXKVqP9n0k69BUoU5Ec3Bz_9SK-lxeAyv3iQFyEjaYgLYoHuKxZMkKNvVNCR7tRL6-vN-kjm9us1XWvh78u4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce5db6d5d3.mp4?token=v01cDCAOEWGRl4JIaEJB0nI6e-mwS2hohAwuxlGFaz2Zz6lVQnPQRWpebglFTnxq1qW2lUnI1WiLMDj26hpMpnp1X5tKJ-bMtXbve3I57T1MQLYgdsX32ubAvLp2KWQcFHhWtMUmDWY3yGPyC24O3H9ISNKw9_u4w6gPg2xndrT4ic7Kn3lARW5xoZDDxhypYW2inIT40-641tShYRR8Nt6LMKd5fEBPuKwlERZ1Hv7dujo92gKDLAsaCxAMd3VeW0TrY6VMHkHsagXH07WGNlLh56dA9XU3oQxzXMBbSO99JKQYsKI_bzJAwd_6ZA0vsNh25eLamlgDqmGPMHJYUj9qxZtqMFhYEv9iIZ1W8hb2uH7KXGIKM33OxjWdLeP18hI3uxNnsK_2poGC_Mk00RRA-E8Di1dcFN4cDuznXJSP-R9h4Nxe_ocYXX5jXuZ6Ac2xt1Dk8o9G-tfWCwEYZO2YI6iUi4ONV9FYMl-nsB69nPm8bU9C_DPmbVRKDtr8aKPoEG--0R3DiBIPYJTAu4FC1spLtJgArjRy1dXv1btwWmlWiMqvZ9QhiZk-4r1y4MSBKBeaVtNvKebG1CPD-gCXKVqP9n0k69BUoU5Ec3Bz_9SK-lxeAyv3iQFyEjaYgLYoHuKxZMkKNvVNCR7tRL6-vN-kjm9us1XWvh78u4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظ پهلوان آواز ایران
🥀
ایرج خواجه امیری ۱۳۱۱ - ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/akhbarefori/680655" target="_blank">📅 19:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680654">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تاریخ خروج نهایی اشغالگران آمریکایی از عراق قطعی شد
🔹
شورای وزارتی امنیت ملی عراق با صدور بیانیه‌ای رسمی اعلام کرد که مأموریت ائتلاف بین‌المللی در این کشور در تاریخ ۳۰ سپتامبر به پایان می‌رسد و این زمان، ضرب‌الاجلی نهایی و غیرقابل‌تغییر است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/680654" target="_blank">📅 19:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680653">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8852f0078.mp4?token=HCfxrQDueX7EwXbGLmbrV8pZ0zjFvMt3gi6dW_lKI4HjqCqvClax3_ABPnjUjLLsM62irLw_z8cAz_TGz9sFekrvrftKi97ImE2gHZPSR5m3ZkBeF3jZNk_Jt1FBhyU8gG4c7BxqyTWe4gzpxZuJfs61RlaWmBBqL6n2wO6l2QbKmW_QKVJ12w4xbcsG63HTDXp6G7NTh7-u0UN5ezhXQz2c8AqWM3Lcxd1TsJLvWCzvqpRpYMgA4mgVQmk0gvVWqMQfGP1PSnhHK_TCWOwOuLbwLEp80fUANzVWVkRbPX-8x1w8vAjp99fpW4TUSYO1pS_aViFL0fAsxfLCDj0v5Xkuv3yJ8u6x3wMAvqUqeldC5LPZiGwRh5R_82q4ccHAEI75S4SiLAqo68KGsVcP_yEIV-iOgGybjuOuf9HDJJLWNc99u7LUjpVHFXc5fun-952jxUZJqwd37q1lhXSm--dMg1HEwttmaxBkr1znPhv7Zhr9ftJxhh68nr1cUbv9REgc6l6WiZBYP7rnuqjWgmjzr9_RhSJYXsNE6sy6Q_CW7ezOfYnRQT9K6nH4q_HOqV9Elw4y4aKf3_7HBIc9vFt0sJLU9DWhe_SHStHAi8c1FvWOWvJOAZTh7kkHerMH9M6TRjYuvcwtPS8uib48UOA0zcYW7vVJYLREb-maClU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8852f0078.mp4?token=HCfxrQDueX7EwXbGLmbrV8pZ0zjFvMt3gi6dW_lKI4HjqCqvClax3_ABPnjUjLLsM62irLw_z8cAz_TGz9sFekrvrftKi97ImE2gHZPSR5m3ZkBeF3jZNk_Jt1FBhyU8gG4c7BxqyTWe4gzpxZuJfs61RlaWmBBqL6n2wO6l2QbKmW_QKVJ12w4xbcsG63HTDXp6G7NTh7-u0UN5ezhXQz2c8AqWM3Lcxd1TsJLvWCzvqpRpYMgA4mgVQmk0gvVWqMQfGP1PSnhHK_TCWOwOuLbwLEp80fUANzVWVkRbPX-8x1w8vAjp99fpW4TUSYO1pS_aViFL0fAsxfLCDj0v5Xkuv3yJ8u6x3wMAvqUqeldC5LPZiGwRh5R_82q4ccHAEI75S4SiLAqo68KGsVcP_yEIV-iOgGybjuOuf9HDJJLWNc99u7LUjpVHFXc5fun-952jxUZJqwd37q1lhXSm--dMg1HEwttmaxBkr1znPhv7Zhr9ftJxhh68nr1cUbv9REgc6l6WiZBYP7rnuqjWgmjzr9_RhSJYXsNE6sy6Q_CW7ezOfYnRQT9K6nH4q_HOqV9Elw4y4aKf3_7HBIc9vFt0sJLU9DWhe_SHStHAi8c1FvWOWvJOAZTh7kkHerMH9M6TRjYuvcwtPS8uib48UOA0zcYW7vVJYLREb-maClU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏
ایرانی ساکن کانادا که شغلش قصابی است از تفاوت ذبح حلال و حرام می‌گوید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/680653" target="_blank">📅 19:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
تولید جهانی نفت کاهش می‌یابد
آژانس بین‌‌المللی انرژی:
🔹
تولید نفت جهان در سال جاری میلادی بطور متوسط چهار میلیون و ۳۰۰ هزار بشکه کاهش خواهد یافت.
🔹
سطح عرضه همچنان ۶ میلیون و ۳۰۰ هزار بشکه کمتر از مدت مشابه سال گذشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/680651" target="_blank">📅 19:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
منبع مطلع به العربیه: میانجی پاکستانی در تلاش است آتش‌بس ۶۰ روزه را تمدید کند
🔹
پاکستان تلاش می‌کند با تمدید آتش‌بس ۶۰ روزه، مسیر دیپلماتیک را باز نگه دارد.
🔹
میانجی‌ها برای رسیدگی به پرونده‌ها و مسائل حل‌نشده میان آمریکا و ایران، به زمان بیشتری نیاز دارند.
🔹
میانجی پاکستانی نسبت به تمدید دوره ۶۰ روزه آتش‌بس ابراز خوش‌بینی کرده است./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/680650" target="_blank">📅 19:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ya1nx465RKe7ARnamdBhngIZXQfhTv0IXPyQ4Wki6C0Zd1sTepgmwgC5T0Yhome1tlXoTuZjxrJcNVeF88pXrPMGEylbmXmIL4zECzO0pNQ0z5JEJciPi1i0StebLfoyzIMHK3J2Y_w053q46W83xYfAZbrkHL4lwln7vynNYKk3bqCKtpAEPb4d3ipin8rci9rD8V6WnAsodN-WqYgxNBxnSyRz0oGx8U2Th19cc27Hc9kFym6CB231s893aPmi-OhyZ4zizOkhAjqxDt_P6LQ5cVS3M-OrdXxbpFZzysjDReycbMNpLy4J6VU_-t2SX4gg70-poT9fn77nrV00oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gi5tduV4RF2tTK3eX2jDGtI8BT99BsPucx1yR_HyrUaBnew_mZ1ctjLFt5VP1G4sHyIbVWo51G8yZXOPF83cJFmRxff0wpFnmCh3aDsWVdgI6ir5p57nyWXLxpdBQozPaG-vkd7wYbI2ouBZ_f2DDKP6NndHYwKP8618am0s0XKnNUeXCJ2fTsjG46OZ9So_0UpoPPr0G6h-KkRA3q4I-0FunHt_IUrztjHKICu9Uht2QlZVu1CV3JUTyFiKeM95t4C8n01yzhW5CnelnWdOVe5kE2TeW7RF1rcWMuN1pgs-KutlH7pj7vxuW0HeuhVBTZPdnYORCfKIQNiOUGpTiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بزرگ‌ترین ناوگان و زیرساخت خودروهای گازسوز جهان
🔹
چین با ۶.۸ میلیون خودرو و ۹۰۰۰ جایگاه CNG در رتبه نخست جهان قرار دارد، اما ایران با ۴.۵ میلیون خودرو و ۸۰۰۰ جایگاه در رتبه دوم ایستاده است.
🔹
نکته قابل توجه سهم خودروهای گازسوز از کل ناوگان کشورهاست؛ ۳۱.۹ درصد از کل خودروهای ایران گازسوز هستند که بالاترین سهم را در میان تمام کشورهای جهان به خود اختصاص داده است.
🔹
کشورهای هند، پاکستان، آرژانتین، برزیل و ایتالیا نیز در رتبه‌های بعدی بزرگ‌ترین دارندگان خودروها و جایگاه‌های سوخت‌گیری CNG قرار دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/680648" target="_blank">📅 19:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSWmH0wdU7pgBfV0ysk711rvpJASTBnYUuYjnBK6l5kl2qQnTr1s2jzWIENyMlEm6uVi7P_Ohk52En-Xppp0gjcfe24Id-2IpgnKkrEOflmqnE9b9yslZD9x_PHAfV2-LhKJJkc6I_TPewwTw34wgwLE98NnDw1ou_g4Gazdn0HQ2J0jq6iBFM9UVb-_UYXBGnLGuU4jQPMTLKCTI4HICoB9Si2ylM8M47kIg8XHt1r51wMtSXwWcfcor1jRRQbXQCd2D6pzn3d4OXwrhZMMeFCFa4erXIj1rjCO_kwfm6JYUJ_whZXOkbJ1nqTmfCf9DqnGCBV2EqDEfwM51puaJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار نقدی: اگر روزی ایران هیچ موشکی نداشته باشد، خطرناک‌تر خواهد شد
مشاور فرمانده کل سپاه در گفتگو با شبکه پی‌بی‌اس‌ آمریکا:
🔹
ایران طی دهه‌ها فشار آمریکا ایستادگی و تمامیت ارضی خود را حفظ کرده است.
🔹
در جنگ اخیر، ضعف ارتش آمریکا را بیشتر از تصور خود دیدیم.
🔹
ملت ایران با مردم آمریکا دشمنی ندارد؛ اختلاف با حاکمیت آمریکاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/680647" target="_blank">📅 19:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdNhCa2XNmKRDgnMKBh8SoWcItozHZuo23JrGEEy_rURtbPgpqeI_LbwA7C5G1noo_WnUIaRnvQQ4R1ZhNEPrTy_UbVPrIkbnclTN3hzZqcvje0WeItxhDvtCrh2G03x7ygA7k0yus3YwSwXini_Mo6uJrC4YAydS6TSg7SKombeqhFCFB6FEUlx9wMweqcEvTXfmsb_uFKPG5FcIG5Dn9aXdHXOIvL8lSqYiI4RbLXqyxJCULsUollk2oKQ7V1ZSljS0y61o9vZDlIR6QsfZhumz3SKc-nXXA-KBVd5c4mJ-LgbRfog6-cmsGjf1tryf9JXWsEtLyZk2TbvxFFxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال تایمز: «جی‌دی ونس» معاون رئیس‌جمهوری آمریکا، شخصاً از کی‌یف خواسته است حملات به زیرساخت‌های مرتبط با کنسرسیوم خط لوله خزر را متوقف کند
🔹
کی‌یف با درخواست دولت ترامپ موافقت کرد، زیرا در تلاش بود از آمریکا مجوز تولید موشک‌های رهگیر پاتریوت را دریافت کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/680646" target="_blank">📅 19:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp8q9_sXgHKON83iuFVB7hxzQKDGVZC19W38ohC5h2A8bIlYm7NC8GUruE-6aVPoMEp3bUoHrjjevgCYB2dI-wwPV76QqvlC-2yuqgwYUYvN1BH5N74StEJUWIwZ2ERnca7KlbvcF3o9Sh1smgHPJfu2MkF4SzfHLXZTEQHcGxLsdJe9J3kC3E55Rn21LDJlK-TmYq7dvKAN9Uj-4RuLFc1WG5aF3UOPhrqJzVk4cd_tILPykmlnr-B_42JEyY4w_dt_FlLFqPhxv9pVz9PHoviD45TMgKN6ftkbdFnmOoPuL39otDIIHDlUANg55Vy8qJkEPpdOd817XVup88149A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
این روزها اسم آمپول‌های لاغری ( مثل مونجارو ) زیاد به گوشمون می‌خوره؛ اما این روش درمانی برای همه مناسب نیست و میتونه عوارض خطرناکی داشته باشه !
پرسشنامه زیر
توسط جمعی از پزشکان متخصص غدد و تغذیه تهیه شده تا شما با پاسخ به چند
سؤال کوتاه در کمتر از یک دقیقه متوجه بشین آیا تزریق آمپول لاغری برای شما توصیه می‌شه یا نه.
🟢
شروع ارزیابی</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/680645" target="_blank">📅 19:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
روسیه یک کشتی و نفتکش مرتبط با اوکراین را در بندر اودسا هدف گرفت.
🔹
حکومت طالبان اعلام کرد طی پنج سال گذشته حدود ۸ میلیون مهاجر به افغانستان بازگشته‌اند.
🔹
انصارالله: فقط مراکز نظامی سعودی را هدف قرار می‌دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/680644" target="_blank">📅 18:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98dea1296.mp4?token=Syc05uMZK80xSeYKWFSIOTfH8rIDpUd4CrMKj1__o87HOXwxPOnCRb3JsvZYvxHQaAfbbQdbs7Zprpj5Xa0_NwAHsViaWy7DenFHB4hnrRw3BQt7rLDqkDzK4zd-gdMXnTTHh0I4hs5P-N6SP7wZFlZYy0eELELTAyLU9uneFdXaM_cudCHf__z-RptesiqMf7BmCqd9oS-34-u59O1Bdhz8ua892iphTA39t9RJDMAvw0zh38Yd36YaroVGTqvxb9MTWyxP3RLJwXYJ8cv79F2t-ktPB5cdTcl3w-2ktriNN1WM1lH-uyoddvE7H4GvOHftNLR62LUXKsLJ9ntcVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98dea1296.mp4?token=Syc05uMZK80xSeYKWFSIOTfH8rIDpUd4CrMKj1__o87HOXwxPOnCRb3JsvZYvxHQaAfbbQdbs7Zprpj5Xa0_NwAHsViaWy7DenFHB4hnrRw3BQt7rLDqkDzK4zd-gdMXnTTHh0I4hs5P-N6SP7wZFlZYy0eELELTAyLU9uneFdXaM_cudCHf__z-RptesiqMf7BmCqd9oS-34-u59O1Bdhz8ua892iphTA39t9RJDMAvw0zh38Yd36YaroVGTqvxb9MTWyxP3RLJwXYJ8cv79F2t-ktPB5cdTcl3w-2ktriNN1WM1lH-uyoddvE7H4GvOHftNLR62LUXKsLJ9ntcVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای ماندگار موسیقی ایران خاموش شد/ ایرج درگذشت
🔹
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در سن ۹۴ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/680643" target="_blank">📅 18:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
توهمات ترامپ ادامه دارد   رئیس‌جمهور آمریکا:
🔹
ایران نیروی دریایی یا هوایی ندارد، سربازان باقی‌مانده‌اش حقوق نمی‌گیرند و نیروهای سپاه پاسداران نابود شده‌اند. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/680642" target="_blank">📅 18:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680641">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxXHtS-cJBGLwkJxZtRyCBohSnpP8wZMpSuCna1-h6X7p2OI-Wplo3YMEQbGCoRpewq2D5mxrlZ065nMbqUh6M64_gYN9ZhbA6hBPhLTfj7xgYlLwcgrdUFumEtjOaot40nTRKchArXh5aV-o-dioLNUi9Qqd2BTw3JJc-_zDof1l9i3R2xuocDEGGRiLt21VMUmHI-Z1LFTrDt6Ng94_GaycLQYc3IjY8WGmI54e-mwzbNHrUArwpDrsMAz-9DuxIAMTEREVxM9pYNkJpJPA6_Xh6I18s5ONmG0G0-dFp-ZA7HlGXSkufF5bB6GgLzZAl-NCCODsh6KAJ_beapPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب حجت‌الاسلام ‌والمسلمین حسین طائب به سِمت رئیس سازمان بسیج مستضعفین سپاه پاسداران
💬
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی حجت‌الاسلام ‌والمسلمین حسین طائب را به سِمت…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/680641" target="_blank">📅 18:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8bhXz52j-e-_Uy8L3vcOdu41pKwGQWe8mO6jykrPqpqmi13_3xObQ7xMXHAheuPVM3s9W5gU6UnAyonJMoCZW3D9IgZiX_osKqB3ybqR-5tPYKoSoz5uCOZVHltsbF_MDDA58kkscjvi4ITEkVMeYckxsj5Y-OoJoAD3LQb9fb3Jrmr0Jxa2EkGZSTNAOxCC6Q88t_H0e5UrJ5Zw1ITYLgpcZkz9MGdyqArofYrOM2Y_R9DJl42hlFdnjI3RlE1ocMZy_aLm-39YRvVjvbaFC5Qqhpz1-lduooZh7tk5Dwa8bczlKfHzSlRjguw_APQ_BWJZfjHURs5pD8v8KOzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت کاربر خارجی: مردی که ادعا می‌شد در تونلی پنهان شده ، در دفتر کارش به شهادت رسید، در حالی که کسی که به ناوهای جنگی و جنگنده‌‌هایش می‌بالید، با کامیون حمل اشغال مواد غذایی از ترکیه گریخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/680640" target="_blank">📅 18:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn75YOUcrvorS-O2ogc36zT82J2iis1fknDy1jnKzun26_myv-b27V4Mr0rOrzNt4lGGw7RKCe3dEH9D7NzDYNDX6Lr2Bj-YJ3bOdPTdYDDCULzw0o1f7QQhdZ0Q6n5cXz6pWVm9MH6gILP106ORnNjmVSv85EotHVDNVuCFeZ2Xk0sR72sPFgwuyz-qcAkGdkhE84zeshgcbCQ_8zFF0Q_JRe8Gl0U6kFTf__P-2qg96WQmKOUFuVGjmWq8dWXcwJgsE_4DSDX8hnmo4hhmp7fnt8IumEb3P_Or4_6o2SihmSebtPVtJDjarsUqDpbf6NNW_1eepNUjhcz7WLEfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده مهلت سه هفته‌ای پنتاگون به شرکت‌ها برای ساخت سلاح/ آمریکا برای جنگ با ایران باید کدام سلاح‌های خود را احیاء کند؟
🔹
بر اساس سند محرمانه‌ ای که به امضای معاون وزیر دفاع آمریکا رسیده، به شرکت‌ ها اعلام شده که «چرخه‌ های بازگشت چندساله‌» برای جبران خسارت‌ های جنگی قابل‌قبول نیست. اگرچه سخنگوی پنتاگون مستقیماً این اقدام را به جنگ با ایران مرتبط ندانسته، اما کارشناسان نظامی اجماع نظر دارند که این فراخوان اضطراری، پاسخی آشکار به تهدید جدی موجودی تسلیحات آمریکا پس از چند ماه درگیری مستقیم با ایران است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3236935</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/680639" target="_blank">📅 18:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680638">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صدای ماندگار موسیقی ایران خاموش شد/ ایرج درگذشت
🔹
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در سن ۹۴ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/680638" target="_blank">📅 18:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYRhSDth7CYRfieuGl87jqO_oGlxE_iSXAnFcxcjN3cZ218P_wYmW60CmkJf43b3hy0GD6IRC768mCa5CTivM6A8DNMa7uNiBCM3NWSGyQXDkFRrJlpCE-NTvZEJtuktGc0NgEau1VnGFdjb69-GOwIPxYi8VthNhrrUgai696LiA_nZ4GoK43SK68WFA_c-BarDoaR_52tEzZuZY6IFeR8UCzMaFNFPhnibqmtwQT2XN-2B5JaakwxF585nGkL-u91AgtMk-k0orUS0LEuzoS2iBhhGmucFPWP0zHBJvBq5aCJAp2EuTxfthxhOirG9aNbCVnlkWA3ALvnrBNrsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ متوهم در ادامه خیال‌پردازی خود درباره ایران: ایران هیچ کاری از دستش برنمی‌آید در برابر محاصره دریایی ما، و همه آن را «دیوار فولادی» توصیف می‌کنند #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/680637" target="_blank">📅 18:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680636">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377783ba7b.mp4?token=J1LVqeA-EqhmV9hP5KiN-NDD4T-Yxs0gAZMfLxkmgk768K1N_VIjGhdhlOUicSdRIjXdpwvSxx2NHo_pqdIG7npGbVksfnvSWPskLjezJHxO-3YQoYXk4TOUrwhQ55Tx9Sua6id4nV-bqgxjW-IKznoBAfp84ejDklR1nlXpCNGiwJ7rKJWNK1wvrcdbyGZ2XIJzb_87p4M9SxjJbgUlQCI4TzKLZ-AsYM93qhuuCMFM4PmSuaMaHh-D1bzjVCfdpA3PhXw_e2rWu-pPAq5UyAbghMM3EK96crKUUoOYqrK2j6xydtn6kqsW37otGgXq971-TbgGAQtNbnIWajdQTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377783ba7b.mp4?token=J1LVqeA-EqhmV9hP5KiN-NDD4T-Yxs0gAZMfLxkmgk768K1N_VIjGhdhlOUicSdRIjXdpwvSxx2NHo_pqdIG7npGbVksfnvSWPskLjezJHxO-3YQoYXk4TOUrwhQ55Tx9Sua6id4nV-bqgxjW-IKznoBAfp84ejDklR1nlXpCNGiwJ7rKJWNK1wvrcdbyGZ2XIJzb_87p4M9SxjJbgUlQCI4TzKLZ-AsYM93qhuuCMFM4PmSuaMaHh-D1bzjVCfdpA3PhXw_e2rWu-pPAq5UyAbghMM3EK96crKUUoOYqrK2j6xydtn6kqsW37otGgXq971-TbgGAQtNbnIWajdQTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوگل از پیکسل ۱۱ رونمایی کرد
🔹
پیکسل ۱۱ با نمایشگر ۶.۳ اینچی Actua، تراشه Tensor G6، رم ۱۲ گیگابایتی و حافظه پایه ۲۵۶ گیگابایتی معرفی شد.
🔹
این گوشی به دوربین‌های ۴۸، ۱۳ و ۱۰.۸ مگاپیکسلی، شارژ بی‌سیم ۲۵ واتی Qi2.2 و اندروید ۱۷ مجهز است و قیمت آن از ۸۹۹ دلار آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/680636" target="_blank">📅 18:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680635">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: واشنگتن کنترل کامل تنگه هرمز را در اختیار دارد و قصد دارد این وضعیت را حفظ کند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/680635" target="_blank">📅 18:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680634">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: واشنگتن کنترل کامل تنگه هرمز را در اختیار دارد و قصد دارد این وضعیت را حفظ کند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/680634" target="_blank">📅 18:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680633">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
طلای دوضرب دختر وزنه‌بردار ایران در تاشکند
🔹
هستی صدیقی در دسته ۶۹ کیلوگرم جوانان آسیا با ثبت رکورد ۱۲۶ کیلوگرم در دوضرب به مدال طلا رسید.
🔹
هانیه شریفی نیز با مهار ۹۱ کیلوگرم در یک‌ضرب، در جایگاه هفتم قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/680633" target="_blank">📅 17:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680632">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSqHnw_BbAiwAIXBsAxpKWyD05lJsZeuV6fjXJsypg9SdQfCx1K7Ms3NNsqch_CtjSx09gLoaJu-Jp70wN10-XQnvDGTpk4i5aRnaJxCmtKUeK8BIG1kpz1n5OSntStFn70KmpG1ZSjWhXe_gZSkVE_2d0fjz5UFODETD5VG_O2v_ZS05R-BR9CMRlXsy8W_tugCVqjhv7MPYsazgKC4dJAOf-D9hX1Z72qUi0sqqNprgsP8Y9236yKwAZWBrlV-EIOam8iu0NPGoS7g5Bx16ozV7SiU17ytCKYbTo6nTGS8IWvoWqLnZITeDmX7gq2SkyzYMtaiBwELzdKMTDNB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/680632" target="_blank">📅 17:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897df1ea58.mp4?token=h4dJPWS5714wSHJycbhEUst-SWshIUfGiKGp1uSvHhVGtwvTA2XX361TwqmWzHTB2VCvosLzvz3gvRPk6kiS3zd0xGrT2jbouHncx_rB2mzayqVTxvRrHnOg4Vuw-5slu95w_l6GpWZcWeCFlcRZtzMcCgBTYWtT4XOTJbuRsEmSL-mI8dtebBCfoIzWa0jVRTNuvD0BaEmm01h1uWAHngZk-8R1tHIEqKFzIlDwqGqhRRuOfJeVMaIRW4mei6gb2_j9eFbu0iD285rRtdY9oZDBXWEl3IcHO43ul66T8x3kIWFIv5FzYJlQwtE9dQjRxnTinWY2v1-CMJ2sNRKFvjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897df1ea58.mp4?token=h4dJPWS5714wSHJycbhEUst-SWshIUfGiKGp1uSvHhVGtwvTA2XX361TwqmWzHTB2VCvosLzvz3gvRPk6kiS3zd0xGrT2jbouHncx_rB2mzayqVTxvRrHnOg4Vuw-5slu95w_l6GpWZcWeCFlcRZtzMcCgBTYWtT4XOTJbuRsEmSL-mI8dtebBCfoIzWa0jVRTNuvD0BaEmm01h1uWAHngZk-8R1tHIEqKFzIlDwqGqhRRuOfJeVMaIRW4mei6gb2_j9eFbu0iD285rRtdY9oZDBXWEl3IcHO43ul66T8x3kIWFIv5FzYJlQwtE9dQjRxnTinWY2v1-CMJ2sNRKFvjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
پیر و جوان، کوچک و بزرگ؛ همه زائرند…
◾️
حال و هوای موکب هیئت قرار در مسیر پیاده‌رویی زائران امام رضا(ع) به سمت مشهد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/680631" target="_blank">📅 17:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680630">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تولید نفت ایران افزایش یافت
اوپک:
🔹
تولید نفت ایران در ژوئیه، به میزان ۲۶ هزار بشکه در روز افزایش یافت و به ۲.۴۷۸ میلیون بشکه در روز رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/680630" target="_blank">📅 17:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680629">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
آینده مبهم سفارت‌های آمریکا در منطقه
سی‌ان‌ان:
🔹
واشنگتن از سفارت‌های آمریکا در خاورمیانه خواسته برای فعالیت با کارکنان کمتر برنامه‌ریزی کنند؛ اقدامی که به گفته دیپلمات‌های سابق می‌تواند توان آمریکا برای پیشبرد اولویت‌هایش در منطقه را کاهش دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/680629" target="_blank">📅 17:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680628">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f13359cdd.mp4?token=s_2VesNMjTWJ59TktRrUbVMxI42A7sl8JfPVaqNLMEsVAc5eURzltL8248hM5VpikYev0hurKa7H-V8oMEosbZ4hx1TDw-CNt0I4MLJPuVpvSZeli72c-PW6hrgZyj-IyetKfICRdkgREvB6sFrvKqwxxKbbfsw_3IAgLA41CTZj06-joI1cDIy9RxdoFLlPxRbMRAA53H8pHzXw5OYj_YKa3N3DTs0nUdAisMerexxv8sGo4cWNXkpwbaptrxwPKUFF0UGcJdMHssuvXfRWHS-2Lklgik1E-Kk99TigcIDHovMN7EA3RQohcamRNHkMbsM1U5Kz8v84u99UqIh0Slgg_pIP1BOAkl4jcQeAkxYRI64UEW0qSWI1K7r50xlmlroTeHaCpw26m_hdQxS8AI5XOLBcJLgWXCPiH0Rkhzthhmyt6nt6O0aHhW7jy4SCFDrEuim3QMFEOKAkzM6NhWdDhISLsAfpmSHQJwE-iUv7A8dfH7LTfczrCB0RbDy3rY6yeuTYAfLZ44vLwZsmnSUarvVkc6rIDFJrds8IXs58Dlbxodr9pktca3Ymk3wjmwH0rqaormJdlnpMEt-EXWbontJfu6HcgDX3U14UJ6oHZqfu7jlhMDzdbWyPLypYcl62Yduk3HCfjH4V8JBem5G4-TzzgmBwaYf0mVrI9dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f13359cdd.mp4?token=s_2VesNMjTWJ59TktRrUbVMxI42A7sl8JfPVaqNLMEsVAc5eURzltL8248hM5VpikYev0hurKa7H-V8oMEosbZ4hx1TDw-CNt0I4MLJPuVpvSZeli72c-PW6hrgZyj-IyetKfICRdkgREvB6sFrvKqwxxKbbfsw_3IAgLA41CTZj06-joI1cDIy9RxdoFLlPxRbMRAA53H8pHzXw5OYj_YKa3N3DTs0nUdAisMerexxv8sGo4cWNXkpwbaptrxwPKUFF0UGcJdMHssuvXfRWHS-2Lklgik1E-Kk99TigcIDHovMN7EA3RQohcamRNHkMbsM1U5Kz8v84u99UqIh0Slgg_pIP1BOAkl4jcQeAkxYRI64UEW0qSWI1K7r50xlmlroTeHaCpw26m_hdQxS8AI5XOLBcJLgWXCPiH0Rkhzthhmyt6nt6O0aHhW7jy4SCFDrEuim3QMFEOKAkzM6NhWdDhISLsAfpmSHQJwE-iUv7A8dfH7LTfczrCB0RbDy3rY6yeuTYAfLZ44vLwZsmnSUarvVkc6rIDFJrds8IXs58Dlbxodr9pktca3Ymk3wjmwH0rqaormJdlnpMEt-EXWbontJfu6HcgDX3U14UJ6oHZqfu7jlhMDzdbWyPLypYcl62Yduk3HCfjH4V8JBem5G4-TzzgmBwaYf0mVrI9dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقش‌های شهاب حسینی در گذر زمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/680628" target="_blank">📅 17:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680627">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
جزئیات آتش‌سوزی در مجتمع خلیج فارس قشم
🔹
آتش‌سوزی در یک فروشگاه تشک به‌دلیل وجود مواد سریع‌الاشتعال، پیش از اعلام حادثه گسترش زیادی پیدا کرده بود.
🔹
۱۲ نفر به‌دلیل تنگی نفس از محل خارج شدند و حریق به‌طور کامل مهار شد.
🔹
بررسی کارشناسی برای علت حادثه ادامه دارد و شواهد اولیه، رعایت نشدن برخی الزامات ایمنی را در وقوع و گسترش آتش مؤثر می‌داند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/680627" target="_blank">📅 17:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfSESJC9SA1-nwZwlr7NZTU0KGpw2p_E5OYimB5xeEhgCTdk8ndqjWC4eBh2Ybez04J20qZcnvvwnSpYtUXvpXtmLPKNej2XSeruZ04pHRyi_X5pPeMPttBgkhUxfZD6G4sNFnutFh6Ns2bj9XhMFO_jD6vDOtFcV4emQdWh2fC0X6XZrWKfuvhdcqfXhterfQLCeP6ywmI7afBEpDQAvvE3M9p5l75ZDLrNwIvdGEyGoKnGQ0EkBJrbMZnKHKyN0ZdI09b3XoZMl_HAuI7APg0Hol4mANfaXeHSIGG5tjgX_X9QD24Kq2R0vRgaEyQyrT4ikV_V-LPwKlTqDv57fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک قدم تا درآمد
🔹
#چرخ_زندگی
یک پویش برای پیدا کردن راه‌های ساده و کم‌هزینه درآمدزایی از خونه است.
🔹
قرارِ هر هفته یک کسب‌وکار خانگی رو از صفر بررسی کنیم؛ از اینکه با چه سرمایه‌ای میشه شروع کرد تا تولید، هزینه‌ها و اولین فروش.
🔹
اینجا قرار نیست فقط ایده بدیم؛ می‌خوایم ببینیم با امکاناتی که همین الان داریم، از کجا میشه شروع کرد.
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/680626" target="_blank">📅 17:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680625">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coa9qhyWPYT4UVt64AfVQEnUfAd5As2Y3uDzAs1TP25GtTUPOYdXQvrLk-ZL__mcshULkjq_pd3jhQJz4iRoFkazoAENjdkNcCeypG2F-rjLmEsGcnG5r7LEgkmprQmf8tb76M1a39zj5cz_j_AIQ18vWTVtltQOIak7W5gwhmRGaqXmjQ7j1fm8ylrGUD4BF8unxaxrj3gT9wCLXwGpf7fu3h2Ufwzb2xtVRjbP-SFCjyYzujdWmRKEOqWJqkvKG9rxyKGsU4Hp_jfmZa74_iF6ZVXrgWF1vbLFjCbznNc17I8gnWMLqo1ZBxN8cyNNUi7gz3_OJpHsNAlxTEJE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«خورخه مسی»، پدر لیونل مسی درگذشت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/680625" target="_blank">📅 17:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680624">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
کویت مدعی خنثی‌سازی طرح تروریستی علیه تأسیسات حیاتی شد  وزارت کشور کویت:
🔹
دستگاه امنیت این کشور توانسته است یک طرح تروریستی برای هدف قرار دادن یکی از «تأسیسات حیاتی» را خنثی کند.
🔹
بر اساس این ادعا، فرد بازداشت‌شده آموزش‌هایی در زمینه ساخت مواد منفجره و…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/680624" target="_blank">📅 17:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
کویت مدعی خنثی‌سازی طرح تروریستی علیه تأسیسات حیاتی شد
وزارت کشور کویت:
🔹
دستگاه امنیت این کشور توانسته است یک طرح تروریستی برای هدف قرار دادن یکی از «تأسیسات حیاتی» را خنثی کند.
🔹
بر اساس این ادعا، فرد بازداشت‌شده آموزش‌هایی در زمینه ساخت مواد منفجره و پهپادها برای اجرای این طرح دریافت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680623" target="_blank">📅 17:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680617">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyuxoCOse6v6qSrsjIJdHpTJzTg00UYYU5gSm4uwAbc1v2SADixzjKHlRNtgkZx6M2Ave2l93YDJ3LhBQ1CmY5fLWxxRpRS2sRKHvnijSk5c98yhzKN_kaf_Q-0SmJzj0IAzNV3hREk_bPPzmg3u3up4MeMai1o3b_GsEKkjUUnYNaLyFFq4ZXDjdnFiuTFwj8P0wcsk9_s8nHM3_ORPkOovXLsAgX2Rz10233W0iCkj5nUCI-zKvUxKvk-wbMsw4y4iWbd6QGwUUhTabrfAU5vPxAvElIovphvT2_1TUZZBj6G26bh2mWhHFMkFgkq_c6BhKR0SJmXbwOAJQN-NUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvbT4hkhpjQWswOXJ3LB9yVNbeaOuoSWa9Ft8iURatIgMf7LsNebOl1V93VONrSpNog37rjbponCEUfeDuwpuFO7DDTaWXHKjpKVrcZE9NTc_t_w4Odb55K63k9ZxzVLHGrU73vBmstnn9-mSS8UXSqZAm1cLjxoi20zrJKWWOCRF7zg6pkiyuajMrI3KlACgAr4e6AoscYYsElwG0O4nkSWSaU-zb1X82xzu1jVTPN_o_p53c8OY5dZVGJ7qo4A0mQalKv1b0rUBjjPhGLXr32X7efkCYGKLgBCvYO4xlxu9f-6XZmrNjiMR4UK22nia7qKP7COR0YfsFegN_JKHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyFk_jGY6uv5WLYSFn8z-G3hD63l5T-PH_Xh9gFIlsK5rZZv0HMR9RCdsNO5xayX9flJZrf3zKyBqKkqW91aJp1OuD57I8rVHIpALp6qqfeS3kDOXLrP6ndG9Ufrt3SsNsRqdIxoiYa4xTWCNH2eyEZzYyFYBsq7Np8ZBT1et-peU49rgfrazMOncOf6_oxYRC4qQ4Mn5FIDY4XtNgAuWIc-nL8Kxed8hX3kled76B4voyRQMEGySOTGW0f9NVhXzHCzh2gvAgbbVXgfn8z2ojR5AVUJdOVhywevp5jqR4fEIHASlv5WqypAU2U7jRkRspDBWiCLXHzUJNaN7SGmUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OI82z7qOye6GZw75YoyQmFiIZSbTbOXgLVRd4rEWJmSIhOkfJY7_Y-WWB3RIQkxAT7ZzY_jZQ6Zbrx1rFmpIttf1LnyDqAY7i60hCM3JbP10yuqGqDcYVnelrvPRQax1Nq8JQHOo-BqaLiVFu9WEFz0vwAvYQAvOUtASz0AJMNqrBApls_rLgy8Xzwp0TJsz8xw4SP6wLOXL2iGxm7NuunsBZWAP3fK5p2_ay3_HsNgs2qQ01exN-45rc2oDWwPtd2W8l9reimHHbqlGdK7ceyqyXsbBNd6l4_K5sQLJaaPoXdWyGA_ej7BGU5T3N1_A2CDuEv-7ELfQJMyOJpskJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4AniMJh88UNv7G4rWX4kUZCJTyLvtlES6dWMIs2ZybogK3eNX2V_n8ZWGJ1kB_4jo0EAz3VTZrQwVxjysQcVVgELbJqzmpuTX6mVKpKLkAeM3YiI2UVGMfyoVkG335W1LG1MCqSizxIbSxlhhe7r3cS3E8u_bQFawe56Q52719C4ckZFyX_8VCXJrUcxNnEOAWB8JIgq56k2vXq9yZKXEU0yBC4oHAa8D7I0Jvzf6CRZmXRve8OgGkNRUdlOx2TLbI69ZC4O5qxaFZMzSb0u32oPIcq33qCjVY5D8FVWoaPTk59PZX9BdjB2U02LmvriSzJ_YYpAgB27hhd7qlNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHhLJgA66L8reFhx3Dq9UB_uQXrxRq_sWNXaMMuUmHQgQKLvKJ-8QCld-x9j-iWAPRuswKs3KvVGiUFlr1zxs7fBqNslCzcpVQhZpnexcNGpYDhu-y4chvw2wEfDcpTmcOTv6ObuxtN81nIhhiGZFq3Q1N9BHi_Mn-J0ys2QW_ubWYwbPc_9R7Y7vRPcLP7lKxRmg0hMrT3lBuLtXcOx_ZdhJuUQ6jcPiN4SPlrO4guSs8JQpt35YyeznLSLZxJfRWhNDIH4obMFZOEaxmRAvk009wbGtzVEJm8FJ8-I2XN3E6fmmnjScfXb4Je7vI2hz8cG8ypjezd1uGHmSjpVeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حال و هوای حرم امیر مومنین(ع) در نجف اشرف در سالروز رحلت پیامبر اعظم(ص) و شهادت امام حسن مجتبی(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/680617" target="_blank">📅 16:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680616">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
تمسخر فرار ترامپ با ماشین حمل آشغال غذا توسط جیمی فلن
🔹
فلن با کنایه این فرار ترامپ را به عنوان «طرح خروج ترامپ از جنگ با ایران» معرفی کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/680616" target="_blank">📅 16:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680615">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1faddfb66.mp4?token=FAmqYKlknD9wl74_YHiTUWT9p4mnUS2mNsVUBTTDLcYpd-FUvtmhyzJ-zuvAU9_6ZsVBBeUdN58ruc9l_ctTFV8n90Q-zVJUSnl2Gl_FWm5U2aZ701dybTezmi-bSYsCfi8WuYSHrCFT2Lgk4wJKMj3QZuRu1Gl-Yeaykmv-lkHhZkT72PXTnTcVy0yqEHCVWgOMqMcUhhoQttsgMQ6mxexw3Rted5FDnP12JsM4nS2qysiJXjJOCsAKR6RDPsB4c16rE8c8Vz7mzlrA8kiPYlco3jCbw-vBGq0Jk5SPsQZN_rDFdyVogYboc6zMOUhHaT8uXrFxU7RKfBkOOEwdUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1faddfb66.mp4?token=FAmqYKlknD9wl74_YHiTUWT9p4mnUS2mNsVUBTTDLcYpd-FUvtmhyzJ-zuvAU9_6ZsVBBeUdN58ruc9l_ctTFV8n90Q-zVJUSnl2Gl_FWm5U2aZ701dybTezmi-bSYsCfi8WuYSHrCFT2Lgk4wJKMj3QZuRu1Gl-Yeaykmv-lkHhZkT72PXTnTcVy0yqEHCVWgOMqMcUhhoQttsgMQ6mxexw3Rted5FDnP12JsM4nS2qysiJXjJOCsAKR6RDPsB4c16rE8c8Vz7mzlrA8kiPYlco3jCbw-vBGq0Jk5SPsQZN_rDFdyVogYboc6zMOUhHaT8uXrFxU7RKfBkOOEwdUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی مرگبار کشتی مسافربری نزدیک جزیره بالی در اندونزی
🔹
یک کشتی مسافربری امروز در آب‌های نزدیک جزیره بالی اندونزی دچار آتش‌سوزی شد که در پی آن یک زن ۱۹ ساله جان باخت و ۱۷۲ نفر نجات یافتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/680615" target="_blank">📅 16:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680609">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70b1c63e05.mp4?token=KKpiRvdbExxzPjOKVCQAkGvcf-xGgHpO5O0-UwS5mTuZAdEoOvPxILwkcHZP_TWaA2bwR7NX7sCatH7A_nBCh0x3mS1TVxJfguspJBv_Q1BN9NQmaKxmC13wkRFKfpon4oZH7Cvg0Wz2biVFVUFmRP72mvijMS6H0vWq1CVbfieFKHAXllSXpANmgVCTGtrRQ11grQ9hhpjm2bjtwaM8V9hiCFdDLQQUuIStMt4IcUDuueptkWqJ3LWIo684yLRMdeApInoczc1PDQ-K305X1LA54k-hSNasYesR0WgUh7uzdsvU7iTDFi45q5ef8RoP-hu_XD25JrMkrSZfdxHh7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70b1c63e05.mp4?token=KKpiRvdbExxzPjOKVCQAkGvcf-xGgHpO5O0-UwS5mTuZAdEoOvPxILwkcHZP_TWaA2bwR7NX7sCatH7A_nBCh0x3mS1TVxJfguspJBv_Q1BN9NQmaKxmC13wkRFKfpon4oZH7Cvg0Wz2biVFVUFmRP72mvijMS6H0vWq1CVbfieFKHAXllSXpANmgVCTGtrRQ11grQ9hhpjm2bjtwaM8V9hiCFdDLQQUuIStMt4IcUDuueptkWqJ3LWIo684yLRMdeApInoczc1PDQ-K305X1LA54k-hSNasYesR0WgUh7uzdsvU7iTDFi45q5ef8RoP-hu_XD25JrMkrSZfdxHh7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شهادت پیامبر اکرم (ص) و شهادت امام حسن مجتبی (ع)
🥀
در حرم رو به پنجره فولاد
گفته ام بارها حسین حسین
اربعین در طریق کرببلا
گفته ام بارها امام رضا
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/680609" target="_blank">📅 16:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680608">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
زمان دربی پایتخت مشخص شد
🔹
بر اساس اعلام امیرحسین روشنک مسئول کمیته مسابقات سازمان لیگ، داربی پایتخت از هفته پنجم لیگ برتر فوتبال ایران، ۱۱ و یا ۱۲ شهریور برگزار خواهد شد. البته هنوز ورزشگاه میزبان داربی مشخص نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/680608" target="_blank">📅 16:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680607">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca137496a5.mp4?token=Vsb7Khi-fyL1rJytlP9A49A0T7TlgmtKSzI3-Owa40kRAB2ahxiwn9RnNlZEpdTHdHYsr4nX7AS-wNn9VnNoZ-oMl1jNkeaonxLOKwfL9PQ1uN-42SYOQa73wWhm2XiPWOSwz8uU9VFsMx9XdYZEbwyY7DsBOc1PGj2akW58WsrCB04jZfTVSAxZEXl3-JjN9T4vIgUf0nm1qcizvU_AejSO9P2qPY287YKiEK9XzHseFJZRcl-yWC0kqXjqlAYue7gYFLjU8_gfKyyz9n7trwJRjNWNeTK9ukTIJ1nXZf0rggKl8YC3eh4WPju-tdx9eTwxytFnOcgrFFsNQgiIvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca137496a5.mp4?token=Vsb7Khi-fyL1rJytlP9A49A0T7TlgmtKSzI3-Owa40kRAB2ahxiwn9RnNlZEpdTHdHYsr4nX7AS-wNn9VnNoZ-oMl1jNkeaonxLOKwfL9PQ1uN-42SYOQa73wWhm2XiPWOSwz8uU9VFsMx9XdYZEbwyY7DsBOc1PGj2akW58WsrCB04jZfTVSAxZEXl3-JjN9T4vIgUf0nm1qcizvU_AejSO9P2qPY287YKiEK9XzHseFJZRcl-yWC0kqXjqlAYue7gYFLjU8_gfKyyz9n7trwJRjNWNeTK9ukTIJ1nXZf0rggKl8YC3eh4WPju-tdx9eTwxytFnOcgrFFsNQgiIvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط جنگنده F-۱۶ نیروی هوایی ترکیه
🔹
این سانحه در جریان یک پرواز آموزشی در استان یالووا در شمال‌غرب این کشور رخ داد.
🔹
طبق گزارش‌ها، خلبان این جنگنده جان سالم به در برده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/680607" target="_blank">📅 16:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680606">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKrAlLnWrcI9YUq2EWVo4GdYdvFtwQP0vKanbIuYVVcrAviM7jK6s3AxBPA62pD1NZQxKXX15RxZBZjiY1fEvRv4bl5sVt_Co4r7VS5IsUmrVu0s2neVjXk1D49-CVektDSyi-j5rPS2sZ0AJYqf77ubAKO_cOMiD3O0mpSXK6dp90_zU11kPqrczSqJsB1n6oICfS8cI7PVH7WkBvFNPig5F9LfXe3sSbHJbFEM3h5T9aqzQGTBXpG8aB4haow4JUb_QsyDkYCtRenGBzo7x5Ynm3eVhoBOsWA9S5cqc7bU1gbWFCf0RscPxj8WY7QyunqlVMiTnReY10Lpl-JyvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: ایران و پاکستان عقبه راهبردی یکدیگر هستند
محسن رضایی در دیدار با وزیر کشور پاکستان:
🔹
ما دولت، ارتش و ملت پاکستان را از سرمایه‌های بزرگ جهان اسلام می‌دانیم و خرسندیم که در تحولات منطقه‌ای، بیش از گذشته شاهد مشارکت و تحرکات نخست‌وزیر و فرمانده ارتش پاکستان هستیم.
🔹
ایران، پاکستان، ترکیه، عربستان، مصر و اندونزی، به‌عنوان کشورهای بزرگ جهان اسلام، وظیفه دارند در مسیر تحقق وحدت جهان اسلام گام بردارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/680606" target="_blank">📅 16:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680605">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">صدای ماندگار موسیقی ایران خاموش شد/ ایرج درگذشت
🔹
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در سن ۹۴ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/680605" target="_blank">📅 16:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680604">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjedzcZ5lAyGVM17upUA5xbfMVNqlg8iqRY6JClHBZWe_UXadnWfwHlIlOscQRrGvRBAkupgrTEPmY4GQwt22hXxI0vRcDSZcXl9L8ubBnn1V-cttnvkHBa7g2FZ96vJve9CBR_hInYn0CmOlNDOmz0IDtvXkl8NjQY01H87COEFlVsyN3DMWnsMs7sHNFsvrzGH5iNi_A0wFb11r_o1NOXAjVbwlyEyEkeTwz-cEG_gtajRuuf39xMNGoHkpFiJsHmw1ES0QGI9fZnNZoWFx96n09EhUhI3N6uZhfoSIHZuorN1-bSixOgi5EajXcwjaANRtMg1G4F0qi8jtGVWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چنگیز وثوقی، بازیگر و برادر بهروز وثوقی در بیمارستان بستری شده است  فرح‌بخش کارگردان سینما:
🔹
بیش از یک هفته است که چنگیز وثوقی به دلیل بیماری‌های قلبی و کمی عفونت و همچنین مشکلات ناشی از کهولت سن در بیمارستان است و مشغول مداوا است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/680604" target="_blank">📅 16:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680603">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
دادستان اردبیل: افرادی که در انظار عمومی وضع پوشیدن لباس و آرایش‌شان خلاف شرع و یا موجب هتک عفت عمومی یا موجب ترویج فساد باشد، شناسایی خواهند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/680603" target="_blank">📅 16:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680601">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFMjP6IILqWo2gsczM2tT72r1IKY7p2ZhRALm8wCmeo82PRkJTH0NNdJKWT3GgYqTplN7QzTasIFQuxD8KqllmopIXuOmoal_6cGCtgfyZz3-Fmm1KLaESZT40Vukeu4FBsOEmbhZiJluTDw6nMZGg8IbALSW_ZBkOYzoHJa1m_QS3Btpo0W7bLi_goZxqvAWPRVcfE7ilm1fHKjPfh_0Wwy1hzSzAb6TH1dzsxmrM54yhByxw9jf8nojf6uoH7WD8pQa-FLqsC32yJ5AW93SFSdGUHjsmdVACpOjIcdnZDRLTAqDPan15Fr5GCj3X_DOKM38heHRl0eT_OVxlGqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6ed03846.mp4?token=QgwxU3y65Xii8BRmnOmZ3uwh_xBK-AUchnEzJx-2g2KqT8HXI0t2QVsqC81TN_zQTHaOz9eBxQ6wnkY2K40AchcH6aagNePYhfEboCmSKVS6xetq-RGdYjYhdhWmOVOLo2wAenPj_VWIR5VlcGkp4YPLEhm2CRheBR3glKa3dj1w8_Lu1FCW8KWRZy1DvvRE6mvUEWvndI6pRe5499YWLlC3O295H0psTwkSvdBHIxR0l18543vnGKnlXjniDSagntk6sOwH3pv9uOqmapC5Xnt-4awUu54kJAnVXJtroC-zdzXRIW7_YqAK-u_2w_VpKpz3hRIFXaJgWztYKg6lmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6ed03846.mp4?token=QgwxU3y65Xii8BRmnOmZ3uwh_xBK-AUchnEzJx-2g2KqT8HXI0t2QVsqC81TN_zQTHaOz9eBxQ6wnkY2K40AchcH6aagNePYhfEboCmSKVS6xetq-RGdYjYhdhWmOVOLo2wAenPj_VWIR5VlcGkp4YPLEhm2CRheBR3glKa3dj1w8_Lu1FCW8KWRZy1DvvRE6mvUEWvndI6pRe5499YWLlC3O295H0psTwkSvdBHIxR0l18543vnGKnlXjniDSagntk6sOwH3pv9uOqmapC5Xnt-4awUu54kJAnVXJtroC-zdzXRIW7_YqAK-u_2w_VpKpz3hRIFXaJgWztYKg6lmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مبارزه عجیب سنگاپور با تب دنگی با کمک هوش مصنوعی
🔹
سنگاپور برای مقابله با تب دنگی، هر هفته بیش از ۱۰ میلیون پشه نر حامل باکتری Wolbachia را در شهر رها می‌کند. این پشه‌ها با ماده‌های وحشی جفت‌گیری می‌کنند، اما تخم‌های حاصل به پشه تبدیل نمی‌شوند و نسل پشه‌ها کاهش می‌یابد.
🔹
در این طرح، دوربین‌های مجهز به هوش مصنوعی میلیون‌ها پشه را اسکن و نرها را از ماده‌ها جدا می‌کنند. پشه‌های ماده‌ای که احتمالاً از سیستم عبور کنند نیز با دوز کم اشعه ایکس عقیم می‌شوند.
🔹
در نهایت پشه‌های نر با خودروهای مخصوص در مناطق مختلف رها می‌شوند تا با نرهای وحشی برای جفت‌گیری رقابت کنند؛ روشی که با هدف کاهش جمعیت پشه‌های ناقل بیماری به کار گرفته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/680601" target="_blank">📅 16:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680600">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef213bb96.mp4?token=VFlfEo757WwJbuAYe2yKsGtxY0pk2fqZCGMnhcUTqD93aF9tzNHUK3Y5_Ff6PZtTCwaaoeHn5XTCVvygombq4j-yVIBnRdu93zpyywmWhxcEss4-8mLZ7geTDVzBfX93heV9_MOB7tYzMcBJCqiOcNcZLWK8EsYPmU3v0_YScV1X4vmMlBKNeLHzH0HMLBFqkuPT3gyo_WGgupNcUN-cNdotsBQcig8B4DPZkZlC7z_WH1xNC7-gdfkfTxmpidTReh0vV1pPVrSO0Pnw6huEVjpMlc9F9nwOB2P0gDhaGwH79m_jlWJRuSGSshs0acWJWIduJ9I4vdgCWMNxXTKilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef213bb96.mp4?token=VFlfEo757WwJbuAYe2yKsGtxY0pk2fqZCGMnhcUTqD93aF9tzNHUK3Y5_Ff6PZtTCwaaoeHn5XTCVvygombq4j-yVIBnRdu93zpyywmWhxcEss4-8mLZ7geTDVzBfX93heV9_MOB7tYzMcBJCqiOcNcZLWK8EsYPmU3v0_YScV1X4vmMlBKNeLHzH0HMLBFqkuPT3gyo_WGgupNcUN-cNdotsBQcig8B4DPZkZlC7z_WH1xNC7-gdfkfTxmpidTReh0vV1pPVrSO0Pnw6huEVjpMlc9F9nwOB2P0gDhaGwH79m_jlWJRuSGSshs0acWJWIduJ9I4vdgCWMNxXTKilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛑
مغازه‌دارا و فروشنده‌های پوشاک، مشتریات منتظرن...
✨
مدل‌های ترند و پرفروش
💰
قیمت عمده واقعی
🚛
ارسال سریع به سراسر کشور
📦
خرید مستقیم و بدون واسطه
اگه دنبال سود بیشتر و جنس پرفروش هستی،
همین الان وارد کانال شو و لیست مدل هارو ببین
👇
🔥
تولید و پخش نیکلین (منگو سابق)
https://t.me/nikleinn
https://t.me/nikleinn
https://t.me/nikleinn
https://t.me/nikleinn</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/680600" target="_blank">📅 16:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680599">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgUSL3WhHCvli6PiGURQBMrvQZu8IzRBEI4DM1lGRnmaobA_P60mWiDqfi5pOcuh_7WH4AeYP_HWruCaXdFKKmQ6srElj9v_kZVAh71E197FIWhUpplL8MOQQwhJsBsD9Yoc1tLC9uFrgLpBU2wDAn9xdk3V_1ywp9ewOV9iar7yeRTNsW7SLtrkNfvMeOib7ibM0Bylc4NI6i4ZFwOkxJn5gafazOLV7n2xyXqEXvlhhOE11wIJT5c9bx_h3t_NVp5Uf9SDfZkDz3NLQPTalVEIRcjIDiolXkm4IFzOWoM4YVAtejOdgA0lbwHg1F3id6_MPVacqs3UWxgdIRUSDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای ماندگار موسیقی ایران خاموش شد/ ایرج درگذشت
🔹
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در سن ۹۴ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/680599" target="_blank">📅 16:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680598">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
یک هیات امنیتی بلندپایه عراقی فردا برای گفت‌وگو در مورد تعدادی از مسائل امنیتی به عربستان سعودی سفر خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/680598" target="_blank">📅 16:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680597">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lez96oPAAQ-xZQPJUewFoDMaI7Hz2n8hePyO9ToUuLikFN9cA7LA6t1QIMgg35LPngLt8IkwGxxEVqciihVFCX_PNcgnEWwHLJP79PJSwZMsNX96AGPP8pcvrFiCh7nptj3lGx9urv_gBJm6WBLE9l-gbhVhduPb3qRZoRJoEXSM225PudZlD8B_zHL8fBdMISkoh60vkWlIyyujpwL-3BHh-h00ay2lbuVx3pd6UsnnrCHfskOeyjilBw1RC_llmaqW69ZsrlcP9qkpEwc37nbXb5w1VHR6HozNrrMTxKIYJdXpRbEo1_upfM4nmU5UyGmAzee1iKAdIsz3yF50bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین اقتصادهای جهان بر پایه سهم از تولید ناخالص داخلی
🔸
مقایسه آمار سال‌های ۱۹۹۵ و ۲۰۲۶ نشان می‌دهد ایالات متحده همچنان با سهم حدود ۲۵ درصدی، رتبه اول اقتصاد جهان را حفظ کرده است.
🔸
بزرگ‌ترین جهش متعلق به چین است که سهم خود را از ۲.۳۶ درصد در سال ۱۹۹۵ به ۱۶.۵ درصد در ۲۰۲۶ رسانده و به رتبه دوم صعود کرده است.
🔸
در مقابل، کشورهایی مثل ژاپن و آلمان با افت سهم در اقتصاد جهانی مواجه شده‌اند و هند نیز توانسته خود را به جمع ۶ اقتصاد برتر جهان برساند.
@amarfact</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/680597" target="_blank">📅 16:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680596">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrLaVF4xUneRzj1UTQex83qK32q4_c_RO7DQYkGc60Yqmg6rsCHNcpK5HZmWT6f5DnXkG6PGSG2ZYtyp13uq7VCPrL6RJFCyi44_EJR54-5nQsBKjqO9Rbac6fpSn-NxUalJkm75BUmTlqw0E3i_SRKe7HLUaj9Y5aB_IkwgzN3VuAMGTCu7qzO2HG0ROCmXw5SoThWj5kVYsOZbbBZuM4XiX_FJ8PvZOdYGGXAzJa8rZi61tRIXPZq0YBmNDuX46mE3Cgn3rCYw_yJEU9Ec7xJp6yZzcPd1XVbSKl6cB2E_Wrlo-csPhGVTWGBJNY8u5D9oCEKstHXpdfGSGrj8LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر فرار ترامپ با ماشین حمل آشغال غذا توسط جیمی فلن
🔹
فلن با کنایه این فرار ترامپ را به عنوان «طرح خروج ترامپ از جنگ با ایران» معرفی کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/680596" target="_blank">📅 15:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680595">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
آماده‌باش سفارتخانه‌های آمریکا در خاورمیانه از ترس درگیری علیه ایران
🔹
شبکه خبری «سی‌ان‌ان» گزارش داد که وزارت امور خارجه آمریکا با صدور دستوری فوری، از تمامی سفارتخانه‌های خود در خاورمیانه خواسته است برنامه‌هایی را برای فعالیت با حداقل پرسنل (کادر محدود) تدوین کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/680595" target="_blank">📅 15:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680594">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tby6oJhuEpQKJaGNWT_e1SCDKchXV8YNyT35yNxAUOLR0-gXcuvOn1hqVsXAGTMaNLCFXOoaQbwowjPfmuoIIMn3ePKCjRkYj71TgkK1zjIMYLRJoHQ45HakS0uq2gmEVK_66dbAB3QqKp5AkUVpght-p2loJs6I35qszTpE-aBK_pRWA_P4tUwyljAnzUVzpyTX31ol_AjZuyS_f13oUEveR_SXdgbLiRJWT5cj2HH6hw5f3ZKcKYwodUwCtVaUgDSOSebd9wUeoziNmkDomJ7KZzlfOUyNxxDOpjIImqnKHD-mH2B3VlIjdapnl7XYWHX64hiuUOqbqfJI0nNvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مک‌گرگور مشاور ارشد سابق وزیر دفاع آمریکا و پنتاگون: ترامپ بر هنر شکست مسلط شده است
🔹
این بحران در پاییز ضربه بسیار سختی به ما خواهد زد... ۴۰ درصد گوگرد جهان از تنگه هرمز خارج می‌شود و در حال حاضر هیچ‌کدام از آن خارج نمی‌شود.
🔹
او باید بنشیند و کتابی با عنوان هنر شکست بنویسد، چون در همین کار مهارت پیدا کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/680594" target="_blank">📅 15:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680593">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad6950c610.mp4?token=YaFniB05CV7LQFuIybsAH66DDWcGIhmztujk6FtzBRgEL3h_yzVAwQA9G3cg7aXnqaOZLbie70b91cCJmstXM1qun0e9C90p5xkrgwgsbYzXoYnvsMICP_xqq8lATkv5KzzLSTXAK89rzih4EdfFU2WlgY_mgVsG-0kJ0d8F5LWMZ_9LwS3vWIDwJ4UgdmdJhugmfJ1zEnkmcrJe2onT_kKSJno-OGOWpZ4wuOuFM2LP4ReyT1eNNhZ2RS7MwR_537iuyX964nkrU4h6AUZ2QNjnmCkC0D-ZzQv23gBP89tYS6tFfC4JEaJ4zdi_kzQqVF8_TY-lN6oWcNdAGgLEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad6950c610.mp4?token=YaFniB05CV7LQFuIybsAH66DDWcGIhmztujk6FtzBRgEL3h_yzVAwQA9G3cg7aXnqaOZLbie70b91cCJmstXM1qun0e9C90p5xkrgwgsbYzXoYnvsMICP_xqq8lATkv5KzzLSTXAK89rzih4EdfFU2WlgY_mgVsG-0kJ0d8F5LWMZ_9LwS3vWIDwJ4UgdmdJhugmfJ1zEnkmcrJe2onT_kKSJno-OGOWpZ4wuOuFM2LP4ReyT1eNNhZ2RS7MwR_537iuyX964nkrU4h6AUZ2QNjnmCkC0D-ZzQv23gBP89tYS6tFfC4JEaJ4zdi_kzQqVF8_TY-lN6oWcNdAGgLEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرور قمه‌کش تهرانی دستگیر شد
🔹
شروری که با قمه‌کشی، ضرب‌وشتم شهروندان و عربده‌کشی در خیابان‌های تهران اقدام به ایجاد رعب و وحشت می‌کرد و تصاویر اقداماتش را در فضای مجازی منتشر می‌کرد، دستگیر شده و در اختیار مرجع قضایی قرار گرفت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/680593" target="_blank">📅 15:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680592">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b594ce2abb.mp4?token=NhpNKf3GhXWiw5bChN1Dn5DjXTQgmGMYVV1LPT3_720h3JLjaM3Md9WBYRx1ASKDiX6Boi_lbHf2i-hB9RB4Tzp5kxupV-5JHqliyETK3QfZLN_khdkKozSBdeMKoHV5g-TB2Wq9EjxQ2WAg0zrikZBMXaZ7zMeUJpcUSjr3m-eE-pngWIC4nnLl_M0_5xmHRSv15X8hMuQd62xSS6MLyfruOJtfzhobKA_5CWlYySoWnuQi-aRrx8t0WmVVtY6Wh4OT_KIX4ev9-6vaMbt0tdy7Os5iP4Sz1YrU2Rie-sbdQpXGDKGe_M8_cRgA8zJOZ7IMvRsf5bO-Urn8Jg9fEHceYyO0NvRda0Upbme13Ah6pgoPWj3dtNqh9RIfx_sNNhMGLp1-WyK17Mec3Xh_y4VWUiS8P0ZS9uYiWY4hZq4m1tKP0g4xc7Zu8beZgT6udhC2Cfmb86h7qhTyDay5AmDzyoItjKw-o6C3chckMq9_hUkKy-bOiWShNyf3jzk5dpAYisTRbVLjAufYTzoV_lgCJSaFaSJF4MdGEPr0Rt3L5-n6rQG6sLp6xO-rGUH23vMM_yq9-awBcN2uum6YwDDV69y6WA9oQN4KovWrnol1LcVSyfm4nJDNJH7qgmg-NOEmrskteqNWzt4GK5wyJ0kGcZ5u5znj9Y0ivjXzZKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b594ce2abb.mp4?token=NhpNKf3GhXWiw5bChN1Dn5DjXTQgmGMYVV1LPT3_720h3JLjaM3Md9WBYRx1ASKDiX6Boi_lbHf2i-hB9RB4Tzp5kxupV-5JHqliyETK3QfZLN_khdkKozSBdeMKoHV5g-TB2Wq9EjxQ2WAg0zrikZBMXaZ7zMeUJpcUSjr3m-eE-pngWIC4nnLl_M0_5xmHRSv15X8hMuQd62xSS6MLyfruOJtfzhobKA_5CWlYySoWnuQi-aRrx8t0WmVVtY6Wh4OT_KIX4ev9-6vaMbt0tdy7Os5iP4Sz1YrU2Rie-sbdQpXGDKGe_M8_cRgA8zJOZ7IMvRsf5bO-Urn8Jg9fEHceYyO0NvRda0Upbme13Ah6pgoPWj3dtNqh9RIfx_sNNhMGLp1-WyK17Mec3Xh_y4VWUiS8P0ZS9uYiWY4hZq4m1tKP0g4xc7Zu8beZgT6udhC2Cfmb86h7qhTyDay5AmDzyoItjKw-o6C3chckMq9_hUkKy-bOiWShNyf3jzk5dpAYisTRbVLjAufYTzoV_lgCJSaFaSJF4MdGEPr0Rt3L5-n6rQG6sLp6xO-rGUH23vMM_yq9-awBcN2uum6YwDDV69y6WA9oQN4KovWrnol1LcVSyfm4nJDNJH7qgmg-NOEmrskteqNWzt4GK5wyJ0kGcZ5u5znj9Y0ivjXzZKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای همسری امام زمان(عج) در سریال شبکه سه
مه‌لقا باقری در قسمت یازدهم سریال «رویای نیمه شب» ادعای همسری امام زمان(عج) می‌کند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/680592" target="_blank">📅 15:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680591">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0CrSGtY_43B3kvQBm_rIWMsjI_14e238hynkvqvwQfRwDaWusZYSJ9FP3KCBhSKH7EeUADAZKhhE0kSavSpSGn_y8_z5zIM1Evc6u0rHYD9gIgHDm_fFY2IPHeROyNSTeIVB1DJ3ibmuGs0nJgVPN_JMH-s5eQcK3sryYXZhi2u4bYUF8NoXbJDj4umehRkK1tbKa2QErSclxpK5ZLp9YTcFjS4SladRDwwOGwyhC1zwFRpds7cQHwR2Gq19NN4wxUs7JPZ4rulHjgrHHKBgGaHe7zBhndI7xuGRuCIjQLghn42YQKsfEHQgUekz27OcKLjW-QsWYHpWdm6jFG3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش موارد خودکشی در صفوف ارتش صهیونیستی
🔹
یک نماینده کنست از افزایش خودکشی در ارتش اسرائیل خبر داد؛ به گفته او، ۲ نظامی در همین هفته خودکشی کرده‌اند.
🔹
هاآرتص نیز از ثبت دست‌کم ۶۸ خودکشی از زمان طوفان‌الاقصی و ۱۸ مورد از ابتدای سال جاری میلادی خبر داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/680591" target="_blank">📅 15:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680589">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIClQToYv1vwEZ5EJ68kpQjCf2JQhhfJRib-zbc66IgZUt4e-VMk7eqmoaDUYL-KWZYLXcClHODJKl-rRqFnEwzqaU-qsJcWZE5ctrHzLvTtQRXrnZD40btVf9Gc2BZKiZykyNU4CZvPo0LM11qG8l8fMwp4kXL3HgKdDqDfHDCEmY7QXrZxA8-71U7uYyuyEAnql64bSm743aQSfQRa0TyXgGVmguYuqju_VLQ2htTaC4DqzqcwR-cyUuLmyjTbSHKOdQfpv97BMxHoEeVpUY-QN7roErePQldc5VO2nC7omkLtfYY58mOjN_kCHBJ1i0xq4nFLjbc_un9VMyaY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnezMOd6ykYaiGxO_MCZgJgVVWbbaTUM66bi2Lp5-EviYA2Vah33fC_-RaVGNg3s129XoPX2JBhAO3H3KBc-CwFeLsuH3o1kHorQ6jPffVpyVbwfCedQcmzInkpwjc0Tfkmt5HcILng_VTGu9u4Bg4pHTX5Dl0SZMjA7rCuQXsGeVKbvL-xLDE4ld1flctIXoSUISRAsAgCrCBzJ6WJHlpEW-XiPEmAb1tOm95oXu6tO1nRCIG4y84Z41Ic2ufAuGmg07ZpIcyMr5eC5-iLvRsgrv5QdPcP8tzmFDmcAUHx0vvNBfuLc6lV5YX2mSwoV5HJpybNXadn5ICHd5d9O6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چیزهایی که به اعضای بدن شما آسیب میزنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/680589" target="_blank">📅 15:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680588">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93bd8e5d8.mp4?token=Zfg0d30MjVMq2sLPuKVaMYIBC-mSic43lZSBLmBiENKnEjpNjFNmn_IBijSDV3vIqyD6-JvpwmYuOZqNIRxvbR4cYYyV6azlS8Uh4Nb5Eu9OJGPOD1GO2S0yeXr0SBZP1QMWD1n03wuOhMZoA6CtMLzHa9uZ1-ks99mbdn31Pgnc9zFD-wql1u3UpUjwbGi9TiadUihX2oDWx-hqNkUHRvlHPo_MA8g6INPzHQscbhOnV9CgDRPuBeVV4XJQos2QidA0jOFDsn13Ext1tCuZ7p0zAKkWWPsxk5i5_km2w4ySaB-fYzs68mvc_RkZZJQ8rTGlMOpDh5XHfiem2ZrrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93bd8e5d8.mp4?token=Zfg0d30MjVMq2sLPuKVaMYIBC-mSic43lZSBLmBiENKnEjpNjFNmn_IBijSDV3vIqyD6-JvpwmYuOZqNIRxvbR4cYYyV6azlS8Uh4Nb5Eu9OJGPOD1GO2S0yeXr0SBZP1QMWD1n03wuOhMZoA6CtMLzHa9uZ1-ks99mbdn31Pgnc9zFD-wql1u3UpUjwbGi9TiadUihX2oDWx-hqNkUHRvlHPo_MA8g6INPzHQscbhOnV9CgDRPuBeVV4XJQos2QidA0jOFDsn13Ext1tCuZ7p0zAKkWWPsxk5i5_km2w4ySaB-fYzs68mvc_RkZZJQ8rTGlMOpDh5XHfiem2ZrrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت لعیا زنگنه از پشت‌پرده «در پناه تو»؛ سریالی که در زمان پخش با ممیزی‌های مختلفی روبه‌رو شد
🔹
صداوسیما می‌گفت پارسا پیروزفر زیادی خوش تیپ است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/680588" target="_blank">📅 15:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680587">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1c75d976.mp4?token=bZUAVuI8NMqqgxyi8G1ZXNcOV_oOMgq_HMGhMYryfg1LKVXYGIHQdwvkj26CHP2u4pA-UVpAWq_L5NdIYeHIz-KXRFGQEmCURZx4bCNkvUxR3eT7CwtHwPZQlANPR2U1wJTsP1QmwjrBy-lgHuamyc4U_UfI2q410Ic9Q574MuCmqFMHeYLzAPZdXkWuHL4h9qjqIcfZDoaaMQDwCZS0TSCT73L0p2PetS_76uRTnHNa6EJEXjyzr91JNyEFNNdeN14FZd4Nf7OiH4DOduxVleo-vujklYbVokDvrjOOG84bRRrJxohaToU_LPDDCHwya2oMILDpUyWv72pf4p_sZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1c75d976.mp4?token=bZUAVuI8NMqqgxyi8G1ZXNcOV_oOMgq_HMGhMYryfg1LKVXYGIHQdwvkj26CHP2u4pA-UVpAWq_L5NdIYeHIz-KXRFGQEmCURZx4bCNkvUxR3eT7CwtHwPZQlANPR2U1wJTsP1QmwjrBy-lgHuamyc4U_UfI2q410Ic9Q574MuCmqFMHeYLzAPZdXkWuHL4h9qjqIcfZDoaaMQDwCZS0TSCT73L0p2PetS_76uRTnHNa6EJEXjyzr91JNyEFNNdeN14FZd4Nf7OiH4DOduxVleo-vujklYbVokDvrjOOG84bRRrJxohaToU_LPDDCHwya2oMILDpUyWv72pf4p_sZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده باش؛ به زودی به سراغت می‌آیند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/680587" target="_blank">📅 15:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680584">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">روز بود روز روشن</div>
  <div class="tg-doc-extra">حاج محمود کریمی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/680584" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🖤
پک
#مداحی
ویژه  شهادت پیامبر اکرم (ص) و شهادت امام حسن مجتبی (ع)
🥀
مزارت سجده‌گاه آفتاب است
ولی افسوس ويران و خراب است...
شهادت
#پیامبر
(ص)
شهادت
#امام_حسن
(ع)
@gharar_madahi</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/680584" target="_blank">📅 15:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680583">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af49a37116.mp4?token=GY1hBzcKznnwnUEVEy0Dx06OzU-jh0NFt4qPQXD-6dgMFKoP1eF-zZtaAavzikqpIhTM22IMXiD0UvnzPZ_mgfc0KAGLqpZgA6WcaRctj0A5wuTz2OLhyHyjzNWoHOAwq0sys9OxaDK5oSXbEfjGdnZVDR3uqGnwChiSxIhpECR-8UAz7SUCcMY2QIjo8G89UP-N8SeDCN2Kwcu4U___5TmwpX6temLr4biuglShRCrQ3WWbMLmShL3l4X3T6yUAPx6bbbA3qjSPISHsYh_ZomYzfyeWakbu5g9biVVvKOKuYUGDHyEFREQDhd-lBoj_7HVb-KWVZrWe9HPMvxd7DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af49a37116.mp4?token=GY1hBzcKznnwnUEVEy0Dx06OzU-jh0NFt4qPQXD-6dgMFKoP1eF-zZtaAavzikqpIhTM22IMXiD0UvnzPZ_mgfc0KAGLqpZgA6WcaRctj0A5wuTz2OLhyHyjzNWoHOAwq0sys9OxaDK5oSXbEfjGdnZVDR3uqGnwChiSxIhpECR-8UAz7SUCcMY2QIjo8G89UP-N8SeDCN2Kwcu4U___5TmwpX6temLr4biuglShRCrQ3WWbMLmShL3l4X3T6yUAPx6bbbA3qjSPISHsYh_ZomYzfyeWakbu5g9biVVvKOKuYUGDHyEFREQDhd-lBoj_7HVb-KWVZrWe9HPMvxd7DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اختلافات در موساد
🔹
رئیس سازمان جاسوسی رژیم صهیونیستی تغییرات گسترده ای در ساختار ارشد این سازمان ایجاد کرده و شماری از مدیران را به دلیل شکست اطلاعاتی رژیم صهیونیستی در تغییر ساختار سیاسی ایران کنار گذاشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/680583" target="_blank">📅 15:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680582">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای آناتولی: ایران و آمریکا با تمدید مهلت ۶۰ روزه تفاهم‌نامه موافقت کرده‌اند
🔹
خبرگزاری آناتولی به نقل از منابع پاکستانی مدعی شد ایران و آمریکا با تمدید مهلت ۶۰ روزه مندرج در تفاهم‌نامه اسلام‌آباد موافقت کرده‌اند./ فارس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/680582" target="_blank">📅 15:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680581">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69dda9395.mp4?token=tAu4kqQ-py2ewnTzrybgjO--sMrpdBs1wzz4rnPZN9E5zdekK_xm4SWGulB-Kpr1QFTAmgsxGyhm_Ozk5cc-6SrrTfcIHLt0uhuhbRwOxmXAvlvRp3pS1oEvrL_mq4YnQ8r-U2kGfY2SJe440LQrBz48WuJOv7CS8EGCgDpPRd_uJIrJapDEw_B6hivPWohfe3vUwYIB1NagPg8Ui4q3C8QYcLVIEqf5DMzhFCwghKLU4FsVsdl2IqdaLX4J2-4py7kFJlgWC0abwtQQ6d-gMOauMJhbvONJgLue_HKyE2SUyvzQ1nw0gsubnZXY_UxgtsaZdCvkSVtQO84tkodnuU4oOWdFpvSm3cZZC0aVdrPECuRJE1ZnxGcgNx_HIiAqRppVDMQAmoiMsa6g807IUr78wWmd8LfBPpujMD7-ZvCaVQJGDtjbW3lSa-HzzuHfkO0BBzMyIUygM5oJPcT9IXF2TSCj18dkemo9FxMKTvOYB7Wa8F33wT9GPPUZkC7g_L5CtgSgMla-pl0PwLruOj9bxODuAr1yLx_4em-x6HzuU0tjYdKOMLE2Z717MqYRFK0MpkghAPIWFK_0Aw-w7izuZ9ihJXLGIsNVW6V3djxTxEydFK6fmbGfzRMtcV7ywua3m3YGAwzYYh71oNcElFyx99d1vdFxzCu9LfRWgwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69dda9395.mp4?token=tAu4kqQ-py2ewnTzrybgjO--sMrpdBs1wzz4rnPZN9E5zdekK_xm4SWGulB-Kpr1QFTAmgsxGyhm_Ozk5cc-6SrrTfcIHLt0uhuhbRwOxmXAvlvRp3pS1oEvrL_mq4YnQ8r-U2kGfY2SJe440LQrBz48WuJOv7CS8EGCgDpPRd_uJIrJapDEw_B6hivPWohfe3vUwYIB1NagPg8Ui4q3C8QYcLVIEqf5DMzhFCwghKLU4FsVsdl2IqdaLX4J2-4py7kFJlgWC0abwtQQ6d-gMOauMJhbvONJgLue_HKyE2SUyvzQ1nw0gsubnZXY_UxgtsaZdCvkSVtQO84tkodnuU4oOWdFpvSm3cZZC0aVdrPECuRJE1ZnxGcgNx_HIiAqRppVDMQAmoiMsa6g807IUr78wWmd8LfBPpujMD7-ZvCaVQJGDtjbW3lSa-HzzuHfkO0BBzMyIUygM5oJPcT9IXF2TSCj18dkemo9FxMKTvOYB7Wa8F33wT9GPPUZkC7g_L5CtgSgMla-pl0PwLruOj9bxODuAr1yLx_4em-x6HzuU0tjYdKOMLE2Z717MqYRFK0MpkghAPIWFK_0Aw-w7izuZ9ihJXLGIsNVW6V3djxTxEydFK6fmbGfzRMtcV7ywua3m3YGAwzYYh71oNcElFyx99d1vdFxzCu9LfRWgwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی از نبش قبر نیما یوشیج برای انتقال پیکر او به زادگاهش، یوش
🔹
نیما وصیت کرده بود که پیکرش را در یوش دفن کنند اما برخلاف وصیتش او را در امام‌زاده عبدالله در شهر ری به خاک سپردند. از جمله دلایل عمل نکردن به وصیت نیما در زمان مرگش، آب‌وهوای بسیار سرد و دشواری رفتن به یوش در دی‌ماه بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/680581" target="_blank">📅 14:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680580">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293c0a782c.mp4?token=sRr7N7CycdP_QN1Js4LWxJyoR9E8xTVZLB7r6nd9ufwMPcWSPdoMsOv2gqTqVm9IaB-BDx42YPZJDLQjzsTwb7VOKljtWoG1uTAEk2F3LtEF1mwDuC9_SbFH16MFxK4ECpyg6LrlE9PN4A2AfJofXUnCYTan40d_8B2vTo9NNAiS9ZzgGNlLfr_tqW96jHB3t29KKGK2p8IOQ8mwuJuO1oU33397OTCMOQ5qf8RWhO-to5bDIb4cCpe1xi8JD6Lrgdm4yvMFmxg-knybHu3dLVDs0CtXq2XDSlLintsUDpQbrg8zMVUs8iTXxQ75AXeyG4DZfSSu2Cs7Gp_SKcg5UaG8iVC8FjWkyJYws3fJfBdo2AYqdBC_4GEXKRtwnHMVqNCqOB7MiyMngSt-dCsC41umpj0g-KjG15jfA-MuBq7rIOBcvGTMf8Ik35StTJWqTWLIBwROqlBf_9QU0E9pZzYL4PTeUQZcenHe4SOFXt0nnlmcvmxE8XMDDpo3KORUckwZfWt82XV5w8rZiz89rlBAY3DB0PSJ7W3fbVL4Q87IHUe0lsZjH9I2LuCmKfBf9VX2p8S38z4F__B_wxRm7gwDOfi47tWGFNV2GOaaJQ7Kp6COGkgEMKMo8T29pQzrrc05GHhYZmWnGbt-7xAhe8TE9ErYChGcbeP9XpREHCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293c0a782c.mp4?token=sRr7N7CycdP_QN1Js4LWxJyoR9E8xTVZLB7r6nd9ufwMPcWSPdoMsOv2gqTqVm9IaB-BDx42YPZJDLQjzsTwb7VOKljtWoG1uTAEk2F3LtEF1mwDuC9_SbFH16MFxK4ECpyg6LrlE9PN4A2AfJofXUnCYTan40d_8B2vTo9NNAiS9ZzgGNlLfr_tqW96jHB3t29KKGK2p8IOQ8mwuJuO1oU33397OTCMOQ5qf8RWhO-to5bDIb4cCpe1xi8JD6Lrgdm4yvMFmxg-knybHu3dLVDs0CtXq2XDSlLintsUDpQbrg8zMVUs8iTXxQ75AXeyG4DZfSSu2Cs7Gp_SKcg5UaG8iVC8FjWkyJYws3fJfBdo2AYqdBC_4GEXKRtwnHMVqNCqOB7MiyMngSt-dCsC41umpj0g-KjG15jfA-MuBq7rIOBcvGTMf8Ik35StTJWqTWLIBwROqlBf_9QU0E9pZzYL4PTeUQZcenHe4SOFXt0nnlmcvmxE8XMDDpo3KORUckwZfWt82XV5w8rZiz89rlBAY3DB0PSJ7W3fbVL4Q87IHUe0lsZjH9I2LuCmKfBf9VX2p8S38z4F__B_wxRm7gwDOfi47tWGFNV2GOaaJQ7Kp6COGkgEMKMo8T29pQzrrc05GHhYZmWnGbt-7xAhe8TE9ErYChGcbeP9XpREHCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال و هوای چند روز خدمت به زائران پیاده امام رضا(ع) در موکب قرار و کانون سلام/توزیع ۸۰هزار غذا بین زائران امام مهربانی
از سر جاده راه افتاده
پای پیاده، یه دهاتی
با همون لباس ساده
داره میاد برسه پنجره فولاد
بشینه روبرو گنبد
گوشه‌ی صحن گوهر شاد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/680580" target="_blank">📅 14:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680579">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
کپلر: این هفته تنها ۸۴ کشتی از تنگه هرمز عبور کرد
🔹
بر اساس داده‌های مؤسسه تحلیل و ردیابی داده‌های دریایی «کپلر»، میزان عبور و مرور شناورها از تنگه هرمز به شکل چشمگیری کاهش یافته و طی هفته جاری در مجموع تنها ۸۴ فروند کشتی از این آبراه راهبردی عبور کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/680579" target="_blank">📅 14:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680578">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
تویوتا فراخوان جهانی داد
🔹
تویوتا موتورز به دلیل نقص نمایشگر که ممکن است باعث از کار افتادن چراغ‌های راهنما و چراغ‌های خطر شود، ۶۵۵ هزار دستگاه تویوتا کمری را در سطح جهان فراخوان کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/680578" target="_blank">📅 14:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680575">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJJgrn4NdVa23KhfCQuNDKI5kL02ScSt8PsB7_xzsCxF155f9ScQ4ImtHtSVqRqJAt42qj3fthQ6teWzY-BorWUW68Y5YW3GE61l__oswiejBtL5l9o9kNFWzPSao1Kc9atCvTF-foi8potr8kTfFd80bKQWDupAScq8BUL1p45hjpamJEvu9MzqxrsnyljLWaK4drLpEGBZDo0IH9ameH0TgPmxhBiIcnXs_ZVH4c-Wafitwa97xuTKuslDMbbLGU3jhrWWa54_F4laOOgd4A8-E06gZYjD_I_zbHir6TmVAnPHI8oFu-wzzXRsvtY3bdvWOXT-zXd8UCyi0IxGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زاکانی، شهردار تهران: موشک مستقیم به طبقه آقا مجتبی خورد؛ همسرشان، شهید و خود ایشان مجروح شدند
🔹
موشک به طبقه‌ای اصابت کرد که ایشان و همسرشان در آن حضور داشتند؛ حمله‌ای که به شهادت همسر رهبری و مجروح شدن ایشان انجامید.
🔹
پس از حمله، اطرافیان قصد انجام اقدامات درمانی و بخیه جراحت را داشتند، اما رهبری در همان شرایط نیز دغدغه اقامه نماز داشتند و یکی از حاضران از آرامش، مهربانی و توکل بالای ایشان در لحظات پس از حمله سخن گفته است./ دانشجو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/680575" target="_blank">📅 14:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680574">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
وزارت امور خارجه پاکستان: پرونده میانجیگری بین واشنگتن و تهران را نبسته‌ایم و مدت ۶۰ روز مندرج در یادداشت تفاهم قابل تمدید است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/680574" target="_blank">📅 14:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680571">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
پنچرگیری هم لاکچری شد/ هر لاستیک نیم میلیون تومان!
🔹
هزینه‌های نگهداری خودرو در حالی هر روز سنگین‌تر می‌شود که حتی یک اتفاق ساده مانند پنچر شدن لاستیک نیز می‌تواند صدها هزار تومان روی دست مالک خودرو بگذارد.
🔹
بر اساس نرخ‌های اعلام‌شده، اجرت پنچرگیری هر حلقه لاستیک سدان بین ۲۰۰ تا ۵۰۰ هزار تومان و برای شاسی‌بلند تا ۸۰۰ هزار تومان اعلام شده است؛ رقمی معادل ۵ درصد حقوق پایه ۱۶ میلیونی یک کارگر.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/680571" target="_blank">📅 14:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680570">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uzo0RA4sseRZUjLBLj9E3RbmlZm9vYNC8tNeDPBq8t0Cpm9jynlr8660wLFwZuo2osgdACkWbTQrWByIlL6SGIEXTbFH2wDAhhEtjmbVZcIHfiU8GkT0TihKSi23uBizWitARCQY4xrrygmVMAoJPsrp1x_I6BAFA1VQpWMkLpoOkRuUYWWMeIFnmCls5nmkQCULJhPILDvin2BDLYyZBhN6Mm681w82O1TzT7vr7cJ3J5U_ePMBwQ5p1fZhD122QsgOdPAOg44at0IWFP9IKEe3N_pMcFda0whOtZHE6jLlU4fr0VazEsi3S5Vg_BzTZbyhwjMCKakwfv-lzd1xMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده جدال بر سر دریای خزر/ ایران هوشیار باشد
🔹
مسئولان باید در نظر داشته باشند که مساله مالکیت دریای خزر بیش از اینکه یک مساله سیاسی یا اقتصادی باشد، یک مساله ژئوپلیتیک حیاتی است و می تواند امنیت ما را تحت تاثیر قرار دهد.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3237180</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/680570" target="_blank">📅 14:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680569">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
پزشکیان: ایران به هیچ وجه خارج از قوانین بین‌المللی عمل نکرده است
رئیس جمهور در گفت‌وگوی تلفنی با نخست‌وزیر ژاپن:
🔹
ایران به هیچ وجه دنبال ناآرامی در منطقه نبوده است.
🔹
آمریکا و رژیم صهیونیستی با تجاوز  به ایران و ترور رهبرانقلاب و شهادت جمع کثیری از غیر نظامیان از جمله دانش آموزان میناب و تخریب زیرساختهای غیر نظامی موجب بر هم زدن صلح و ثبات در منطقه شده اند.
🔹
امیدوارم تلاش‌های دیپلماتیک ژاپن برای برقراری صلح و ثبات در منطقه ثمر بخش باشد
سانائه تاکایچی:
🔹
توکیو از روشهای دیپلماتیک برای پایان جنگ حمایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/680569" target="_blank">📅 14:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680568">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVFsmsLOouKclHkASfk4o1-_bxTVpWmLGLInbTrlIe_VKKJXweOOR892fJ-LuDPSalbOatxghNP91vt2HYjGZm4fkiv7IVL4RBaG5T36MKHpJfr-cE8jmBII4wWT6PoGyLr13FefmDfNggfhlxVzMH6aEMipfT2XwGV9xTqCr_BOYl3ooajKsKm5PD2fSrlrD5FXdtqsvH27PW7YdO0IElEpNM3KHRzTVA_RE6vUd4y02wX_T3RAHWf-gzOTbUwM1XyIBxL2lHrBmYVdR9u4eObMQN79FtvRQB6FvI2mE7n2t9YAiqazUmTK0g5z_zp7QySRoFAIV15wUZCHb62maw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قوی‌ترین پاسپورت‌های جهان
🔹
سنگاپور، کره‌جنوبی و ژاپن دارای قوی‌ترین پاسپورت‌ها
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/680568" target="_blank">📅 14:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680567">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd389e9e9.mp4?token=lQNx0K4uYQz51j29czRlRQkS1Cm4BJepnWSHfa8JbszbUuQQ3HBHAv82mYhca_lod-JM87VAvj4iyXaoh7ZpgHP286sOI_RvJVy5L9Bxj7fWgj8yNGSDiVTn1pjT2qBhxJ9aRqumtWsfYz7z4mDmHGM9f9NMA6GxJIyMXL8UuTFwkkJrJvezfoNd-In3iWWCIDABBH4jH7u_ifzaXGlzWBknwK3D7MQav19yw68Wpf3aKL4SxD3bgUuB41dzQob_YPT1qXurK7unLH5OscKEQhbKRf0kPggxOys1B4iAPsQ79mNWVfwa_S9opeAuUMsQDU3z25WTHcyjYR5KmtlCwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd389e9e9.mp4?token=lQNx0K4uYQz51j29czRlRQkS1Cm4BJepnWSHfa8JbszbUuQQ3HBHAv82mYhca_lod-JM87VAvj4iyXaoh7ZpgHP286sOI_RvJVy5L9Bxj7fWgj8yNGSDiVTn1pjT2qBhxJ9aRqumtWsfYz7z4mDmHGM9f9NMA6GxJIyMXL8UuTFwkkJrJvezfoNd-In3iWWCIDABBH4jH7u_ifzaXGlzWBknwK3D7MQav19yw68Wpf3aKL4SxD3bgUuB41dzQob_YPT1qXurK7unLH5OscKEQhbKRf0kPggxOys1B4iAPsQ79mNWVfwa_S9opeAuUMsQDU3z25WTHcyjYR5KmtlCwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجموعه میم‌های وایرال شده کاربران خارجی از پنهان شدن ترامپ در خودروی آشغال غذا
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/680567" target="_blank">📅 14:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680566">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ونهم از فصل پنجم
🔹
در این قسمت دومین تجربه‌ نزدیک به مرگ آقای سید محمد موسوی که هم زمان با جدایی روح از تن مادر در حین عمل جراحی، روح ایشان نیز بخاطر ناراحتی قلبی جدا شده و تجربه مشترکی با مادر در عبور از رودخانه‌ای طغیانگر را درک می‌کند و بخاطر نگاه به نامحرم و دروغ، خود را در طبقه‌ای از جهنم که شادمانی شیطان بزرگ‌ترین عذاب بوده است، می‌بیند اما بخاطر آبروداری فردی گناهکار در دنیا از این طبقه رهایی می‌یابد را در این قسمت و ادامه ماجرا را در قسمت بعدی نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید امید متقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/680566" target="_blank">📅 14:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680565">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
یک مسئول: هیچ آلودگی ای در مسیر آبی تاسیسات و آب‌شیرین‌کن‌ها وجود ندارد
مدیرعامل شرکت آب، برق و تاسیسات قشم:
🔹
در مسیر آبی تاسیسات و آب‌شیرین‌کن‌های شرکت آب، برق و تاسیسات قشم هیچ آلودگی وجود ندارد.
🔹
فرآیند تصفیه و تولید آب شرب قشم در شرایط کامل سلامت انجام می‌شود.
🔹
مردم جزیره قشم از بابت سلامت و کیفیت آب شرب هیچ نگرانی نداشته باشند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/680565" target="_blank">📅 14:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680563">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdbw_mViNRC0ZR2AbwyhkpDMBPuLFdO2pDGF5u2134di-chqF5qZLVbbLQWg2RngwLb76RrP1TWR614-FJ3BJhhvyybc8MX1mp95hMTnbXFPBqpd5iuiJbQR7rvS5Azsc6JaHfqSShRq0uStMxDS_KnafD6VhFv3YPe5Snv6pZ3_cBM7MrLICsrsDkTEAs9DzWF92PEgeZCZEgU1r9nfLAaQm8ytP6QGV9fow7WJoCI2tohJ5ZHz0MIixYVa6fbWL8IMMOOSafErvETll-6cNGAbX9DeVbPOunZVA8PjtSaHgAh6YopHHUXxMhyu244eCI15je-IRDHWeiAyi8Guzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بر اساس مجله اکونومیست، محبوبیت ترامپ به پایین ترین حالت خود رسیده. حتی از کم ترین محبوبیت دوره اول خودش و حتی بایدن، کم تر شده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/680563" target="_blank">📅 14:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680562">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
علی‌اف: کریدور زنگه‌زور و اتصال ریلی به ایران در اولویت باکو است.
🔹
بلومبرگ: امارات در صادرات نفت از طریق تنگه هرمز به عراق کمک می‌کند.
🔹
مسیر شمال به جنوب جاده چالوس تا اطلاع بعدی مسدود است.
🔹
آتلانتیک: ترامپ به گزینه اقتصادی روی آورده اما تاب‌آوری ایران را دست‌کم گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/680562" target="_blank">📅 14:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680561">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuqxxQDFdHkLlxY1EKYvfPeZO4t6xW2lBNeB_Zdo4jLUBAC7L-wm6xCbgbzAu6QmI3L2XhtT3xJfcACyTYg2sYCh3bMTWoZ_m_SJEhAhjrdYzzDJ3i3jyhESEabr6EGfBZ4RluV87l6-Ws0Zkj5MurW3-igkM44S97NEJyllu6IT_LezpdqfTvcM9FoRsXVfSevwlVMEX6cw9WCD4WGUtP3geR7DCUgamZyOwAb5CzOJl2oFm_6BWZmKYYJPvqRlIesNwYH_v8SIuMJpOdWBt_pFKE1wonsZTdLJnblc8BdlAx49r63ANFnmoXZ1HaIJTMIUrWNH-fZxCK0QeE9D-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال حوزه جنگ اوکراین: ترامپ در حال بررسی تغییر نام وزارت جنگ به وزارت تسلیم است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/680561" target="_blank">📅 14:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680560">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3Fz5gp9EJluFhrxOiOlmo4qwNN4OqHuME8qcWOrpAkFFZTIGtOLfAZGcpRwWjTEm-NkpSNwkNNjXUsg224DQJvZWoydP8Gw9C_5lltdbYRwwRsg7czmJr6Pxr9ch8LPmbZrE3YDYbhRCjsuuNk3_f5VRoMatabfZszIdMra50406crSU3uO_jaXR2qdZGzKqMIQLv92eHtfg_3_c26ps53W8CxPz9EZRc7LKx8gV5j1NCc8oeu_kET2R3HY2M3nCSeo161ozOZPbZaVxkNDeR6As6L1PwoVljCtudD8QBnmYy1fjWKa9p7RXc3mM8HPslMO65q1wsRZVbS5BNzChw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ هگست را با خود برد، اما روبیو را گذاشت تا هدف موشک‌های احتمالی ایران باشد!
🔹
یک کاربر شبکه‌های اجتماعی با کنایه به روبیو: «مارکو داداش، اگر جای تو بودم، از این به بعد حواسم به پشت سرم بود.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/680560" target="_blank">📅 14:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680559">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNr5FcStelTtg7SyM8TgPe3F4mZHoy01HBkeUfPbbpwiazX40mu2YqBwIXwzcQEPn47kPNiE3X4lbIYeNUPLVGHIV4iY2wcwNDw7JhLExpxPGff8G0xuJ1vsZAooWqs3uPwbg8SWEM1QEtXkE8mjcD6UoV_0s1tISDDBEkWmo4Q58VECa1Sgsu8JJbH-huSYXt-s8PaaNY_jtLv6m0v97lmuCOZSA7wuIrzkpx1Hi_iyP65Yel-sOCkcdQ0JfeCTyrB0phNpKaZkbcfX04vyrY2CjUIH7lhKRLTV5RZ6Dv8ZwMRh7p8I-s0UC9-26_cFHi5XN87RlKiOm8ngcZiQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییر مواضع مارکو روبیو درباره توان موشکی ایران
مارکو روبیو، وزیر خارجه آمریکا، در اظهاراتی طی ماه‌های اخیر مواضع متفاوتی درباره توان ایران مطرح کرده است:
🔹
ابتدا: «ما ظرف ۲ روز ایران را له خواهیم کرد.»
🔹
چند روز پیش: «این نبرد در آخرین لحظه است؛ آنها دیگر موشکی ندارند.»
🔹
اکنون: «ما ایران را دست‌کم گرفته‌ایم.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/680559" target="_blank">📅 13:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680558">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9YRHwablTf6_wxDcnFnA8zB5KXRcsmlfqro_MvmVfthQ8jZykVluQ8L1VpRLRYkF7zoajyU41z_3pLIXIBCBqQMKViy__GhDXtErFHywzlwroIPm7EutK1HOv-gNIjd1nQuncWOQRTbAYXTnZMJRFZPBdyVnZAC9T7rpPIxYYQgmruQB-Yj-nDlXqo0grV-BKdjAWEueLfwVWb-DrYeiYVD-Zo8YUVQu49I54vW7MNsYW1JaBkQeh74_YK4DW0LDLDojcyqSbKhb0PLvIVpxVYM69btSuTdGK81l4opWZLcufyvRet5ZpZJdx-X1KWbxEEzPPxnMBVp44qJfcaJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانیل دیویس، افسر سابق و تحلیلگر نظامی و سیاست خارجی آمریکا: این هشدار را نادیده نگیرید، ما مدت‌هاست ایران را دست‌کم گرفته‌ایم و در همین جنگ هم چندین بار تاوانش را داده‌ایم
🔹
وقتی ایران چنین تهدیدهایی می‌کند،  واقعاً به آنها عمل می‌کند. بهترین کاری که رئیس جمهور ترامپ می‌تواند انجام دهد این است که از این جنگ کنار بکشد.
🔹
ترامپ در «اعلام پیروزی» و بزک کردن نیز مهارت دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/680558" target="_blank">📅 13:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680557">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HB2D2X4p0zWE02mXf0v3gYjRla5aHn3y8MxCeSA2EIWcDaNUxQZLnZ5S7eJ-lIK2EwcDe5-AjgIFRYDTqrUF8Kwc4JDwddUwckBv-l7EqtHnR1tZ5D2t9sWwr-m-xZw7zXH63jkfh3MCYa_2CiAAmQhenRl7HO2Q8jBzoLvoC9MPu0cn8lhBsFQYqmiBTRHe70oY4PuPc7Ej1oIluPsE449JJeA-GABypYV1i80rLfJfFGlR0CNv_bTWyaOmM7XJWlg_DpfvzEXuU3wiipQV7SrCzFOH-p3ThV_DV7nZa1h_qEooleszlhJub1MQ5eugLAPXQ_vy5s22q-IQxyKViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وندی شرمن، معاون پیشین وزیر امور خارجه آمریکا: در آینده قابل پیش‌بینی و شاید برای همیشه، ایران کنترل تنگه هرمز را در دست خواهد داشت
🔹
بعید است اعمال فشار اقتصادی بیشتر از سوی ترامپ، باعث شود رهبران ایران تسلیم شوند یا از مواضع خود عقب‌نشینی کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/680557" target="_blank">📅 13:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680556">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ضرب‌وشتم مدیر برق عسلویه هنگام جمع‌آوری ماینرهای غیرمجاز
مدیرعامل شرکت برق بوشهر:
🔹
مدیر برق عسلویه و همکارانش حین جمع‌آوری ماینرهای غیرمجاز با هماهنگی قضایی، از سوی یکی از استخراج‌کنندگان مورد ضرب‌وشتم قرار گرفتند.
🔹
مدیر برق عسلویه به‌دلیل آسیب جدی به بیمارستان منتقل شد.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/680556" target="_blank">📅 13:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680555">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo0DSuiO8R3i1KeTk9D6Ie-ga3McZZgYNRblLREAgo_cGx8VzEuqL-N4WKMwfqprAXLrvfknneqQG9iqhovV_IdUsmdKGv5Bk5EaH0Yqo1PlUTQ5NsRgTyxcCpiu7dMRMDU7FPC97RQpl2Q-KwGFlR0Gqp3UQb4Ona0nBi3vXA_I2JgnxCTtetXFCLoIP8JEw9rd-UDFC3ahU-XQwcUwITypn16QPRP-MugjWrwDuoTE0Wo1DeyawFvUnRbklj3A91Qyl4Rk3cyUnSyIKUElnw0rGiGI_xskvaAIAK9a0z99QTql2eHRPfegmj7NG1_7AUaoJG-IOPM4rMAIQ5Uwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طولانی‌ترین برج کبوترخانه ایران؛ چهل‌برج کلیسان
🔹
چهل‌برج کلیسان در روستای کلیسانِ فلاورجان اصفهان، از نمونه‌های کم‌نظیر کبوترخانه‌های چندقلوست.
🔹
این بنای دوره قاجار از ۳۲ استوانه تشکیل شده و حدود ۱۳۲ متر طول، ۸ متر ارتفاع و ۵ متر عرض دارد. نام «چهل‌برج» نیز به تقدس عدد چهل در میان مردم نسبت داده شده است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/680555" target="_blank">📅 13:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680553">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbcf87c51.mp4?token=fBLgqKfKwyeLq2DO-rgKDFEfQnf3uxiRbhZWiDSN1zQEt8sL0ZF6ntZfkoBLvma_bkdF9iExltLulH9N-TmARJMpvQp7-QW225jkx_j6dX0ltrO_zVIg0E_StLoqiWgk5SilAtyxF6XsYD7Zjffv_XO1KMArlaJyfMKgTvF3Slv1NeZ-v9ICxw9UR4Qafr5WxRw0QtTMjASmZf9xq9oCRKNV_zH3LdsZhNCMxT_lBtSzsh2Yjuh_FabL5gGy3taZKjFRDyWeMzsHxShdpyXRmqt_Bj7Oa25vZ-6bzJKMRRKQGM9hZZgJuMUZn68Hf7xtZM3CvcD-KcSd9HnfauGAiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbcf87c51.mp4?token=fBLgqKfKwyeLq2DO-rgKDFEfQnf3uxiRbhZWiDSN1zQEt8sL0ZF6ntZfkoBLvma_bkdF9iExltLulH9N-TmARJMpvQp7-QW225jkx_j6dX0ltrO_zVIg0E_StLoqiWgk5SilAtyxF6XsYD7Zjffv_XO1KMArlaJyfMKgTvF3Slv1NeZ-v9ICxw9UR4Qafr5WxRw0QtTMjASmZf9xq9oCRKNV_zH3LdsZhNCMxT_lBtSzsh2Yjuh_FabL5gGy3taZKjFRDyWeMzsHxShdpyXRmqt_Bj7Oa25vZ-6bzJKMRRKQGM9hZZgJuMUZn68Hf7xtZM3CvcD-KcSd9HnfauGAiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: بریکس باید از گفت‌وگو به اقدام عملی برسد
🔹
بریکس می‌تواند سهمی مؤثرتر در شکل‌دهی به معماری مالی بین‌المللی فراگیرتر، متوازن‌تر و مقاوم‌تر ایفا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/680553" target="_blank">📅 13:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680552">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzvsqcU4m_sj0aAGD88hyShT9RXLGcn5Ol8K0L7aCRBQoIOpm5Pzh-mmvn2Ut4QnOdwcCIvlq_7DGaGNc28sA7hFuXScF_B5mCgKRvah_hCNAI2RqStnRsGbeD6EqklVQIyu1xAGTwmHAp6OJQfhgLsv47zNqX_GD6KP7KguRIHYquAu_GqK94RRf4zZbCzIcYe948NwUydp-xYBSj3o14Tum0UIQDq9A5vxvuVX_Zo-w-MWplt1JnkhFOf2g4xDCrx2TnrnaZ1wfpTJWFxiSSg_JKqaiVaP5OXjs-TpjKnOsVJu85mxXfUPKE2mYiRSUs97FbSexraPgx7s-PndVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه رویداد نجومی همزمان در آسمان
🔹
امروز خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی همزمان رخ می‌دهند؛ یک شب متفاوت برای رصد آسمان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/680552" target="_blank">📅 13:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680548">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d72c32eb9.mp4?token=abJhs_g9kB9OmGclWTnBX_aXvPOm8sqZmPpji17e0GGsuZEmLYhRzH4sKgt38Oc5ihHYHfYMRolgGIb0idDWS-1Dw4EzH66EN5yKM40wAO2issLGJK3c2GZ2cIOVBOIONu3scH3Igxgdpf4mQWsLo1kjhBpi5CvdkMkBNJ6VZY-KQC_5j8kM-dELzL8BE--_3H_4WXwKc-1tJsvIf0NfNyc_PpVHFpLagXa_vGDzBWA0IhUAVxC2-WsTIShuYzfWWJEG6jQ_z128Uo3Sm3Z7K3Tz6bMxrzQTxFpHesZi35kA70T7bUDJ9WyuD4jrqWtmUOJaO57P0WD_F6dJ9nV0_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d72c32eb9.mp4?token=abJhs_g9kB9OmGclWTnBX_aXvPOm8sqZmPpji17e0GGsuZEmLYhRzH4sKgt38Oc5ihHYHfYMRolgGIb0idDWS-1Dw4EzH66EN5yKM40wAO2issLGJK3c2GZ2cIOVBOIONu3scH3Igxgdpf4mQWsLo1kjhBpi5CvdkMkBNJ6VZY-KQC_5j8kM-dELzL8BE--_3H_4WXwKc-1tJsvIf0NfNyc_PpVHFpLagXa_vGDzBWA0IhUAVxC2-WsTIShuYzfWWJEG6jQ_z128Uo3Sm3Z7K3Tz6bMxrzQTxFpHesZi35kA70T7bUDJ9WyuD4jrqWtmUOJaO57P0WD_F6dJ9nV0_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طلوع خورشید بر فراز تخت فریدون دماوند
🇮🇷
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/680548" target="_blank">📅 12:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680547">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCGJ8Yh2jML18aXTHuszp1gfJoJFyOJC6Qex4tesSwJ0POuEtHL2uZoOb0dFiuCUBJcKYCwlWwrGH12rFhapVgIDNcaAlvpCcFDomb0nZ8ECPpB2ZzEAkxPWxQarlK3V97wdlLcDtq4rNCuJHWMYm7ONkJkBFdJ3IuJIdTbcD3HPjRhnO8j5aLE2CvdKGrkqCAZR9s_0X3K3CUWGR_ZhCVhk92asK3C9e2FUdr4BQaxFKgxKe3mqtGx9YfF9_3m9KPVC5DZZu3CIcpi-8k0eq_tvGh3abXEtB2gh4RZiR-_Dc9WQdEyPViXwdNvUKz6H2jwDGO1nTPu1H1PcFJleHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرویس دهی و خدمات رسانی متروی مشهد در ایستگاه بسیج خط ۳ برقرار است/ اتصال خط یک و سه در ایستگاه تبادلی
#شهرداری_مشهد
#جهان_شهر_برکت_و_کرامت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/680547" target="_blank">📅 12:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680545">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261223a0ae.mp4?token=JXy6R1alL4fX1gvcSpXasD3qvYpz62nxcSVT6mPt_4zAyJDNHTbU05g2RAQ-Pw9FEaKM7t7sPTKoUdykt7d3iviGFOBAgDNtn0s4-at7UWaepElj9VWLknta2NRbzJkOW9vAZ7XFegd8alxxrtHGkbugcAOUvIi1RAFsAeh9biOu6SH_DCtT9_akN7LaxD2M-fjL-3qWFywN6CifRmzKS88G07jJC7B6Te5twnC_V9iRBCupjA2JmRg854NQZtyHed6Jih3jdtJI47Q1pliv2b2zjBzxrsqmvCR3VwZRgRKlzwyHgU5H9_zN9-erenLTl9bA-8aLym9_Iog0yPipgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261223a0ae.mp4?token=JXy6R1alL4fX1gvcSpXasD3qvYpz62nxcSVT6mPt_4zAyJDNHTbU05g2RAQ-Pw9FEaKM7t7sPTKoUdykt7d3iviGFOBAgDNtn0s4-at7UWaepElj9VWLknta2NRbzJkOW9vAZ7XFegd8alxxrtHGkbugcAOUvIi1RAFsAeh9biOu6SH_DCtT9_akN7LaxD2M-fjL-3qWFywN6CifRmzKS88G07jJC7B6Te5twnC_V9iRBCupjA2JmRg854NQZtyHed6Jih3jdtJI47Q1pliv2b2zjBzxrsqmvCR3VwZRgRKlzwyHgU5H9_zN9-erenLTl9bA-8aLym9_Iog0yPipgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع سیلاب در تویه رودبار دامغان
#اخبار_سمنان
در فضای مجازی
👇
@akhbar_semnan</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/680545" target="_blank">📅 12:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680543">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
کشف پیکر مطهر یک شهید دوران دفاع مقدس
🔹
همزمان با شب شهادت پیامبر اعظم(ص)، گروه‌های تفحص شهدا موفق به کشف پیکر مطهر یک شهید دوران دفاع مقدس در منطقه عین منصور، شهرستان موسیان استان ایلام شدند.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/680543" target="_blank">📅 12:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680541">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjYypX6ZmORjKqgug6_tOMNuLwKVr9MkZYE6AJvGOHRwOi4sxuWOVJ4AE0sVHlHbexmJenIonzGlsQepTOfU_UJ92UN08wcGD17WXcLZOqUllVip9PceyT1gqmcxdAHfUSwYaCEs8GcWHRopVJ3RwgldJ5TpULVxutQDc7OCv9gFcsNwNGmqT9eMYDuPuw9OOTGsaVHfC0L89re7_n5mAFM9O-juy3SksbHZqILRzSRb2jE1famSeSJ9im3fcuAlPrceG01oFJ_QGsx6Av-DZ-yGHhpVDE5TdTNBlDb-xCljpl44taPoQJu1lKYGlHpA4R_93K0eMvQi-wlldn6yYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقاشی منتسب به آدولف هیتلر ۱۹۱۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/680541" target="_blank">📅 12:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680540">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
هزینۀ اجارۀ نفتکش در تنگه هرمز ۲۰ برابر شد
🔹
کرایه نفتکش‌های غول‌پیکر مسیر خاورمیانه به چین به ۵۰۰ هزار دلار در روز رسیده؛ در حالی که ابتدای سال ۲۵ تا ۳۰ هزار دلار بود؛ افزایش ریسک تردد از تنگه هرمز و کاهش نفتکش‌های در دسترس، عامل این جهش اعلام شده است.
🔹
یک نفتکش ۲ میلیون بشکه‌ای با محموله ۲۰۰ میلیون دلاری، برای سفر ۳۰ روزه حدود ۷.۵ درصد ارزش محموله را کرایه می‌دهد؛ یعنی یک بشکه از هر ۱۳ بشکه.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/680540" target="_blank">📅 12:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680539">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBT3tn2kPwhFZne2pGEXJK1txWlGd9FR2s5MNs4YuXVlYSzBM_6RVqzxw2f2iEk567-gA3cX3Dee1Ht1Itu8dpjnN4YNq72cCGsWg2_r_8KbHAJm4-yw0_gC6ZdvWdRCQ--jT-qJ-IFoJl0Jhe5vLV1ODSS1AZWG3S6aVUSnbsH41apWwRQcfjTWgBMzhR0_NeC2NXjcPC8L5fxg-Dihdn6slcpimm0omO7_-35fXuzQ_ClA-2iNSpUSr5oQW3oroOz7AhvVnxrTVGcCJ-eJZaMK79aL-QN1EU25sqQNEoOTgMbfFUpALmiD_Vc9sZsxe49JSwAJFxEnrM-UMR90iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلون میزراحی، تحلیلگر سیاسی و فعال رسانه‌ای اسرائیلی-آمریکایی: تمام جهان غرب به یک فاحشه‌خانه انحصاریِ صهیونیستی تبدیل شده و اگر ایران نبود، بشریت هیچ امیدی به آینده نداشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/680539" target="_blank">📅 12:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680537">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
سردار جاویدان: ادعای حمله زمینی به ایران توهم‌آمیز است/ مرزهای ایران امن و استوار است
فرمانده مرزبانی فراجا:
🔹
ادعاهای مطرح‌شده درباره احتمال حمله زمینی به ایران توهم‌آمیز بوده و تحرکات دشمنان هرگز نمی‌تواند اقتدار و امنیت کشور را خدشه‌دار کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/680537" target="_blank">📅 11:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680531">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyExXOoCgyyWKX69md1imvE7nGmnqldbDOQXN7Rg1j0o3tZxpyVDbEbdnq4Sz6i9ET3k-Ze8o9Mazd77kG64qZi_I2K18dLQXw98dA3m2dhyIOcCg99-RlbUnDM9P7SEz-nbJKV7Tf5WBCKQSurPfqB1Ih3EEfa0m53buFl2hXImiJhqFNAb3RtEa4sAxARs3eu-5pDHSCRLlDI1YvumFV61zFQq33no55UHJgVz1sHAxzGNmUMWNpwf9rpwQENoop0dLlso-Romlt28ElZLhAIZmtD98GcMo9oUbEv_XFEs7LEXyUFmnvJzFr1jAHWBU-8sc_i7HECoFQ1GQyzBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5OVI_J00l-r_p1YFTB06wt0yi5PafDRAy9FGNF6lTEA84ciBlS1rIcDmJgICSq4FOJ6uOhWQ3-2NZ-ntsRC_Kf_9Q5qk0AJ0eJYlB5G03iPBLB_9FyoWi6_A7zX_tEXgBhf0B-995iJulopxAI538rf5Qr7QsuiTy1Vm53-jl7ekWeTdyfbWdcgc7KKTvAlsK6Uqi0SHn6TiSQXX0-iQ3S4qA0GoX8qLOaFTMb1AaGE8gTH3kkh-5mkLxcB1hnrYQjk9H-BUa_XxWljQ1LOhket2MAr2pqPsRFu87j8v2CC8jIH6eOrYrxOTiFYH14Vi_r63xyOsd2u_2DfOrQ0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIVfWfv_TsayUyqdsvFBmE_RQ0psEQTApZFOE24d_YzCuWhuShmd_aXtcKSq7tS2V0Ija8FiuUPaH2J8XymFudNkH8N77ga6S7mcdocsonEEeCqYvRg_52F3WWyFXdS77LQ745Ezy6NzWjNfW27D_hht8bRMGhXIayeGxBsK9uiMTenNNDWaI0_dC050jj0rR8pt1xoWnRv64P2UOH-STfFgy02Set22-jc5dbOU01B7pzY5wiBh7qZi7Y06qpKnXPZQ_r3AzRKtRRXLgvojF5AeB4ihV3reYfDumFLWqJLUNVksHukwlCdb-YqhZ0ea6CnMgT8bjZBRGI6ucHOlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5eIQqJqX9Bxcd3Whq7R5XbbKPWaISI-943IYm11IRzjF5rICfsXc2C2DtDtH1kImoauObMhTOU8BTezqxxE6X22LLq2w4aOqWQDri7S2u5eizLqYCANC6cIeu-hW3k9clgRy1XOrTj3TT9xkQnms9hWIajxUzLbieKN8jBMTWSFfwqtaQf1HWwRwhh9-Tl3p3zQAzPeY5MSfyPINFyl6nXcXQHjG3ao7MxTasiCYmd1lWL6hN6_zogAOLlbojLZr7Kg_3PziOUHMAEuc5x_36c_lZ8wv0xDxlZ7Cfp0KihzobgB23BOBUOb0vfFtuyl113u_tfBGY9sb4q56OI2ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTy3huq-c0aVM6-Qf6mFRQEXItOTNe3XQF1jBY6QXUsWErthdnCdHo5q-r9QeBepAR1LoU3ifjjyJSCYh51xhHLKruey-KnL0X3qrRc1ES5z1Ao2spQH2O7QKfseAeVdkDasYW9IGiyCS4aV-W_yvK5rDHpN5f7TZarQ_y9l1AYUqy9TXbGOqhRsBuL_6O6YUFA17F2AAtsBpjxl6oX2LBxj2i0FIH4cQVPesNl108nSIMHv898j4_8xjXMxmyX9SoB9ut6-GXvnIHevodysZ-ee5PoPuxhMP_aafdgQnrhxkZ7AYbo18yU_RXAFiy2qGW9S1XBSQXJcUujjGK2Odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvabj3dCO9NfpzsfWYP4RohUCl1aL4Cz5IX3qL8MtaFCcgKbavS2Y6fblQC2Lqd0vUHGFA41nxPUaY3Uq7no33gJM1Wh9lPujpQk7wAGkWwW2IvLKivqOza4CYDHcs5oD0nXUKtnrFvoCaCJs_qVmejYMW5O27Bk0Q-7F1yrA-EzGaAZRUg9baEBI25jZhq42eZcqPuxl_WOCrq2fWWFRlhY-_RWCM1QlW_94b8PF_ZCfRXvnAgZfAeb1fWX46yVuRNWhNzf0tZjsKKp1ZGmvICLS_estOE1if6Xv681nhn8VE7wDNEswkxInP8uuyCJ2kr9Y9zt7AoVmCOZDoQFKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تهیه و پخش بیش از ۸هزار ساندویج در بین زائران پیاده امام رضا(ع) در موکب هیئت قرار و کانون سلام
@Heyate_gharar</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/680531" target="_blank">📅 11:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680530">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
وزارت امور خارجه پاکستان: پرونده میانجیگری بین واشنگتن و تهران را نبسته‌ایم و مدت ۶۰ روز مندرج در یادداشت تفاهم قابل تمدید است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/680530" target="_blank">📅 11:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680528">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZgswgjwAp0zZ7zXLGYsXINO1IngGz0s9S7XlyfLgqGFGFXUsg7jnnmgxOFuG5eRuDt1dyI__wYXlNJIuuRG5kJn3HGcwvpsdBG-hGodYr0Z7Ii7PbNRCAAdAmlfCOEh7sEI7FHGS2paPbwelbUeuxt38GuqQ9Z54Y2RmbhTQj7Y6wVFwRqnomnHuXF_4v-dSOED0QiouJdhwC29xtPlv_X-E6xami8q136WwWatHtgDRyDZgcOXB7dt-KEiBlzlAZhqu3SUI5534lApMhKPeqOTHC-lv3NeaG8D8z6efG6Yphnx29R1NeL4_FKEDY-slF_JO3Fd1qAxjao0ZGo91Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3BH-JAldyCa-k60ePC2Sl3GbrzMnMsy4Wk0eu-GU-LqerkTL1NvzRbWA6cSc6t3KVfWkfqxQpIhEoWBzH96tf5o-ikgUVIgO8JapNCCaQGIkPdFKjcBYbysR2Xqk9TRQUZyygHy42sKF7qxtPxoRYM5s0tdMdxlzBJ9ncoAmaVG-sW5ZYPTBnY9xfJ1W_3GR5Ea4imVF2KvFYDonyvn_5ZIT5xmoVIBOmqBFVRnIB62uk3eDnA8XocW21i593GRZsZ_GR7u_Lvisb_ByzOcCIzdD742nXnk2cSbyO83ABdTLaSrJVsnXjZEypIKqHfEGvpXmvHDgE35QH7JVx7hSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این یک دیک‌دیک نر (Dik Dik) در پارک ملی اِتوشا در نامیبیا است؛ حیوانی با ظاهری عجیب و بامزه که واقعاً شبیه شخصیت‌های انیمیشن به نظر می‌رسد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/680528" target="_blank">📅 11:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680522">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqFQol-Ymy8-bu88HnshFpdybL0W0qV7qvoyL6_8ZjEvWCwUi7f3oaJtOV6l70pckK22CwQwOQtZ9Prc4iNaB68JpDkpShdXAovcr4OQ8MftTo9tVHaCe3LqzOUByF_GlZSa1WgZjxxxPY2KHxXFFahPggjCxB7msOwY33Z5nHFlUZkFJ0X5IWbxgJGKxHtC67PDoqkt9KBSrFhw37IpeEZ3ISvXMI7-gj8Bboab5BfaCJhSZ411dhHYrt1xCandNiRl6S2tUAIdmJol_f9kvkMYXRFlM-SDH3jHAb-M9p49hczusoutscZuUHG2Fqu6PogYoizUWrxz3hDnB1r5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af677bab1b.mp4?token=kO-983VCMM_LhDAFsHCb2C2EkbJUwLhutiZLwKMFOEpB9wAGCZ_drRggu4c6idLltjwsL0XnqbxAaJmXMrcxTLiv9J5XShH4hsmfnyWHaZUrMXuPnMaoXqxs6L9V8By4Hpymv8igK7eMt9Em7UBe2FmWvnfVndRZkBbbB3uRudlBTZQsCUrj91c7QB6bZny0fGyJHpDRgEn3Zti-hHREoFPNvKVjFhKx1ejLCCVKqfMb50TU4OtJriiSVHfM3KdKjk3IsYKGq6g_I7FhPnZ9Zl4vWFC6eQ6UW9uFffjN-G-JCTP9WcyYdgDWeqbdeXrz0dNUguGAc1_yqLjt0kagWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af677bab1b.mp4?token=kO-983VCMM_LhDAFsHCb2C2EkbJUwLhutiZLwKMFOEpB9wAGCZ_drRggu4c6idLltjwsL0XnqbxAaJmXMrcxTLiv9J5XShH4hsmfnyWHaZUrMXuPnMaoXqxs6L9V8By4Hpymv8igK7eMt9Em7UBe2FmWvnfVndRZkBbbB3uRudlBTZQsCUrj91c7QB6bZny0fGyJHpDRgEn3Zti-hHREoFPNvKVjFhKx1ejLCCVKqfMb50TU4OtJriiSVHfM3KdKjk3IsYKGq6g_I7FhPnZ9Zl4vWFC6eQ6UW9uFffjN-G-JCTP9WcyYdgDWeqbdeXrz0dNUguGAc1_yqLjt0kagWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شهادت پیامبر اکرم (ص) و شهادت امام حسن مجتبی (ع)
🥀
خلقت چه لایق است که صاحب عزا شود
عالم عزا گرفته و صاحب عزا خدا ست
@Heyate_gharar</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/680522" target="_blank">📅 11:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680521">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
وزارت امور خارجه پاکستان: پرونده میانجیگری بین واشنگتن و تهران را نبسته‌ایم و مدت ۶۰ روز مندرج در یادداشت تفاهم قابل تمدید است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/680521" target="_blank">📅 11:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680518">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCMJgwoqg-ONbDE1lDcPZM0KPHIBDorDfhR5SxYsGuzX7lTbpNrV6uYcneMJD5JsZLKmtDu3SoURfZu4kF87TeEHcjfv_jq9kFPP6X9__SXHfyBZdhbn85X7X2Db53Q0nWLf7fz3IMN0chyTkF_ACkh6yAiTe_i2erZs2zwU2qTD6A5e4LTGdEe7E4eLMb6x-OnIY3yFaduGv25voLaEtDjY0yh5uaGGdMowfS-j_m6uVpaN_Y4w9yArng93bzdWWpTTjPkWIOQwf9ucPnS-BYJhnUTH_xTktXy8iHy-Mb9x3gMkLejc8F30S2a3bQTZqBIbISYb-khOv8bltUh5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید انقلاب به روایت خودش: من بیست‌و‌هشتم ماه صفر به دنیا آمدم
🔹
من در شهر مشهد، مرکز استان خراسان، در جوار آستان امام هشتم، علی بن موسی الرضا علیه‌السلام، در یک خانواده روحانی به دنیا آمدم. زادروز من، بیست و هشتم ماه صفر سال ۱۳۵۸ هجری قمری است.
🔹
امروز ۲۸ صفر مصادف با میلاد رهبر شهید انقلاب است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/680518" target="_blank">📅 11:16 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
