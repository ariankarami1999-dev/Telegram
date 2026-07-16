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
<img src="https://cdn4.telesco.pe/file/NM4LKm_TT35KGAKay00z_65i18_5thHJYeslnpWmcOV0QDSmhzbKvs7NDT4NbPQf2TRV-upzo-YgQO1mFYqZ29_mDhiNt3OMOlvDXweqzpYUdS_PrY2Ljp1zbo45cm-h_G5p9pDtJwNzzKesQHzndi02XONcjn8s62mV7k6xAaKKE3l37NoWLZeu9trezyaGissO60fq2DXsXZnGpBn3A3DZAkdpBJ6NGIxAU88Ii1zNeEN3gDBDotNf56VKgYZgb_U_jfOvS5al3nuy3VeI9AGRu-WqRBnb-yaUdePUlQHrhnL1_6aFrkrLwkP5rXHY15xw2surgsnMfBGLwsSw9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 22:27:32</div>
<hr>

<div class="tg-post" id="msg-135969">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">#شفاف_سازی
🫦
📌
ببینید دوستان لطفا به مطالب جهت دهی شده توجهی نکنید این مطالب رو رفقای اقای زندی میدن بیرون که باشگاه رو تحت فشار بزارن، همونطور که چند روز پیش گفتم و امروز هم اشاره کردم باشگاه خوب نساجی نقدا پول رضایت نامه ایری و طاهری رو پرداخت کرده که بتونن…</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/135969" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135968">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">#شفاف_سازی
🫦
📌
ببینید دوستان لطفا به مطالب جهت دهی شده توجهی نکنید این مطالب رو رفقای اقای زندی میدن بیرون که باشگاه رو تحت فشار بزارن، همونطور که چند روز پیش گفتم و امروز هم اشاره کردم باشگاه خوب نساجی نقدا پول رضایت نامه ایری و طاهری رو پرداخت کرده که بتونن با دو سه برابر پرداختی شون به تیم های دیگه بفروشن این دوتا بازیکن رو…الان که باشگاه با علیپور تمدید کرده و زارع رو جذب کرده،مدیران نساجی الان زیرش زاییدن چون سپاهان سقف قراردادش ۴۵ میلیارد هست، استقلال بخره هم الان به کارش نمیاد، فولاد هم بودجش در حد سپاهانه… جز ما و استقلال کسی دنبال ایری و طاهری نبود که بخاد پول خوب بده الان به گوه خوردن افتادن مدیران شون ولی با این تفاوت که الان افتادن تو فضای مجازی و دارن کصشر تلاوت میکنن تا هجمه وارد کنن، بگن ما موز میدادیم کیلویی ۳۰۰ حدادی خیار خرید کیلویی ۲۰۰ اقایون جای این لاشی بازی ها بازیکن رو به قیمت بفروشید که اینجوری قهوه ای نشید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SorkhTimes/135968" target="_blank">📅 22:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135967">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
قرارداد علی علیپور تمدید شد
❌
قرارداد علی علیپور، مهاجم باسابقه و ملی‌پوش پرسپولیس، پس از توافق با دکتر پیمان حدادی، مدیرعامل باشگاه، به مدت یک فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/135967" target="_blank">📅 20:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135966">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKEF5gFyolum1JOP3Ub-2UoH6Htw6zUC97EpIOEVoJffuAC8SsYvcGHLn5HEzDjcsTAfE-kEBpjAfRnKSv3HTZexMQUjvUopMLty_cQGSRZgVW_dxtvTmE1ttzPirtW_VTfxGG1Ek43-BJ01N_OHd7szYxpfOv5BGp245TPu5N0kDyjfTgPZ5pOE5u7aOSj5SJ0j1DXj9NRpYIsONC5b0bVLoTMMgXjwDWGccFTxHCJJKSykgbazLqnlCMluhgFCr67PEIBhNxidzuIz0CPV7N9GZRxasJXc8Z7UBRLr7japEU2mdS_aAJfHk-v13K-UuPkNW8nvmKzoGuV9M7G5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه پاکستانی
😀
اکسپرس‌تریبیون:
❌
بعد از از بین رفتن تفاهم‌نامه بین آمریکا و ایران، پاکستان تلاش‌های خودشو برای کاهش تنش‌ها و ایجاد صلح بین این دو کشور متوقف کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/135966" target="_blank">📅 20:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135965">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/135965" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135964">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/135964" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135963">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcKQrcyjVumGYuT6JAvOoTK64STyVZ_20qIfPMG5IwQFdG-c0QRxOVn-UhXd4V5UHtWMeJKkzxRKQxGgKx4BlSetxJgfWh3b_FtW2IQ1UXNDwagjKrNaLQ38FlMEK__1erRCeJ2dXMKs7VxuX1RvEWaoUAPNk07IUtrd9p7s3ov_oy0hUWYDQoSoFdUZuGG1kfn1CDtmOiOD3XkD0-5u91BuVGoplMZizWb_f41lFqhNLRp3FuRznZPbB4IIzNw-HzCavKz_mPrkpMmH1YbOLJPA4B39fMxYhR7-8_Z-vY-TKBMEC2DKp6VOT3lRaBk37xdh3PWlpxCD8j2i1AzJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/135963" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135962">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyTHCf2mNOFsT3yxXTA7aavxZjcHtBJT_E91Wr3PicUwK3WQsyM4qRKaIryFzuMcXG8u4iWCYT0gjnVB4CENHNw7iQncZRAMXmg2EUM6s208QPYFxrZRz8Erv-U8zVuu5bvXBeq9DkLvZtXCvRx5AB2sapqULWVeCQPN4zmRV7uUggeOxGV1_JRiaEtD5kRF5NuBcFJc_BrSmzPPGjrgKTbYUn7b74RrnWn02rIgSs7VUCF_ZmVZNrNkDLox3YoqJGnDYmhoISkABEiLsnFJ-yiv8IIbCr-ohGinD5RFzjZrgFuuF4V4ZXFJETWs3yIB3roEgEoZqK7d4UR-xO5zwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیم ملی والیبال امروز تو یه بازی جذاب 3-2 مقابل آلمان پیروز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/135962" target="_blank">📅 20:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135961">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
❗️
فووووووووری
❌
فرهیختگان : اگر میلاد محمدی با باشگاه تمدید نکنه ، مدیران باشگاه از مدافع چپ جوونی که با اون به توافق نهایی رسیده‌اند ، رونمایی خواهند کرد
🔴
گفته می‌شود تمام اقدامات نهایی خرید جدید تیم انجام شده و این انتقال برای نهایی شدن تنها به یک امضا…</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/135961" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135960">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e071e1ff46.mp4?token=Ee5xQK4_RGRG9m0fGQa7XP1JWySW0Vgjx36HisGqcHJJ6vioJdF2WV3r2DudKxd0ETWcgJc9idVAUZkfMbOK8sHeOytosazl5xkwCgymxClhw3yhh4u7lVYhMkWaJ_6vXyhnWdrCUWEJ0gxIA4v0ewHA7kFUn6qprDDLctVfObdj30XyIf3ZUUf91anOhJ9inQy2wlK91tNQ5wwU8N9np2a9EPKy7Cs9ewEliKDKGPgrtBXqCeTxbwEqtiVk0MwNUHGMaCvVzC-JVQzMWdj6FYQ44f9aCzraYK94my2qlTxt68q0QQzlIUTLPyAvtbAmFVaicj2kLq7IAIIuw2sgp5pnO7A23veMb6DDBDOggzTuhUKewEso8dQ0-XAiunXUmfrRXSnseK8HwPcGl4MsRzhOYdUlLX14EBH2zGr5H9a3wlHiNaQlXkFEzdmkrmtmivINJYmW-JB-e8UZakc7J5Z-ZQU8XgXq1m042lU6yYxiCLn2BwdmxgmQ2XA_4vt5rwyruprJMi-kKq7w4Vdop16OWykIah4Fkz_WeX7gJVRStPchh5WQifBuU3uD16R2huhTH0GTYor73rxgMh4LJTrIlZPW5vPpiR2m28MIAktctoY3r7401KbG7Tl6WpFP6c3SVr3Fpd6KQPO-VdlqJxwB4I2A2VIeikfTOX0AX2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e071e1ff46.mp4?token=Ee5xQK4_RGRG9m0fGQa7XP1JWySW0Vgjx36HisGqcHJJ6vioJdF2WV3r2DudKxd0ETWcgJc9idVAUZkfMbOK8sHeOytosazl5xkwCgymxClhw3yhh4u7lVYhMkWaJ_6vXyhnWdrCUWEJ0gxIA4v0ewHA7kFUn6qprDDLctVfObdj30XyIf3ZUUf91anOhJ9inQy2wlK91tNQ5wwU8N9np2a9EPKy7Cs9ewEliKDKGPgrtBXqCeTxbwEqtiVk0MwNUHGMaCvVzC-JVQzMWdj6FYQ44f9aCzraYK94my2qlTxt68q0QQzlIUTLPyAvtbAmFVaicj2kLq7IAIIuw2sgp5pnO7A23veMb6DDBDOggzTuhUKewEso8dQ0-XAiunXUmfrRXSnseK8HwPcGl4MsRzhOYdUlLX14EBH2zGr5H9a3wlHiNaQlXkFEzdmkrmtmivINJYmW-JB-e8UZakc7J5Z-ZQU8XgXq1m042lU6yYxiCLn2BwdmxgmQ2XA_4vt5rwyruprJMi-kKq7w4Vdop16OWykIah4Fkz_WeX7gJVRStPchh5WQifBuU3uD16R2huhTH0GTYor73rxgMh4LJTrIlZPW5vPpiR2m28MIAktctoY3r7401KbG7Tl6WpFP6c3SVr3Fpd6KQPO-VdlqJxwB4I2A2VIeikfTOX0AX2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل چند ماه قبل پویا پورعلی به پرسپولیس با پیراهن گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/135960" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135959">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664e6b20c6.mp4?token=aie34GigIdFPuu-NDnzWy_1QRTMRrujx9Wk_qQsFcamSIcAT-dgWg1gCcPDBw65gFEGTtq9FHWJ5IwEpdvksnat7KK-KJ6C-KcWXOKFivzAJkonie1frTcTJu-qiixVcUOps5qqVan-e90h4LbCYVxYSldJu8ptXhWGOh7vIdoVotAkY-dWRORTiEarcgyc_B8rueIaJqHXzcDhprblk-1kHEN1uRpfPdG1XIg9B8Al0AiWcf8Nbsakva5C63ouDelaa4OjL-2kqg0y726f9udc8FnONTsdeXHs-idXkOXtVs01tSCf2tjY-Ne5R8CqjAy-CW2LqOZ5cye_ehT-Dsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664e6b20c6.mp4?token=aie34GigIdFPuu-NDnzWy_1QRTMRrujx9Wk_qQsFcamSIcAT-dgWg1gCcPDBw65gFEGTtq9FHWJ5IwEpdvksnat7KK-KJ6C-KcWXOKFivzAJkonie1frTcTJu-qiixVcUOps5qqVan-e90h4LbCYVxYSldJu8ptXhWGOh7vIdoVotAkY-dWRORTiEarcgyc_B8rueIaJqHXzcDhprblk-1kHEN1uRpfPdG1XIg9B8Al0AiWcf8Nbsakva5C63ouDelaa4OjL-2kqg0y726f9udc8FnONTsdeXHs-idXkOXtVs01tSCf2tjY-Ne5R8CqjAy-CW2LqOZ5cye_ehT-Dsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب علیرضا، پسر نابینای ایرانی اينجوری با گل آرژانتین ذوق کرد
❤️
🔴
گزارشگر اختصاصی هم داره که پدرشه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/135959" target="_blank">📅 19:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135958">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/135958" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135957">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
اردوی خارجی پرسپولیس در آستانه لغو
❗️
❗️
در حالی که تیم فوتبال پرسپولیس قصد دارد روز جمعه تهران را به مقصد ارزروم ترک کند تا یک اردوی دو هفته‌ای را در مسیر آماده‌سازی خود داشته باشد، هنوز شورای برونمرزی وزارت ورزش مجوزهای لازم برای برگزاری این اردو را صادر…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/135957" target="_blank">📅 18:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135956">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
ورزش سه: تارتار به وحید امیری پیشنهاد داده به عنوان دستیار و مربی به کادرفنی پرسپولیس اضافه بشه؛ اما امیری فعلا دلش میخواد بازی کنه و دیروزم داخل ترکیب پرسپولیس قرار گرفت تا خودشو به تارتار ثابت کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/135956" target="_blank">📅 18:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135955">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eda321934.mp4?token=buoiHGUQNbLJSgu2kKMDDm5_05vN4fldYMriVsiDFDQ-h0sMAkld7dzkH-2JHGhE7p_FujoQTiezIOoe3d_dsDT_kF3KUtQEbCVSW22msnepZoTCiC6n77LB-TN26sldR834MpXjN70q_59eZCcdpd-ljS_w3FrCt1kxgE3tCdEmIgNBNQO4HHrB-zbimOzL_ADihGHXHDX2llzThj18aNA_OCVEGzwG9Hsl7pUMTQOeq3P2HyxMaNRH35YCKy6UVITzI3I0rvkLsqaL_DZuQUSIx3uYiVa50Ax2eK5d0tkSRum7iID4JGuoGbbiCGCreZNLYDxX_AC-IlM_WYPMGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eda321934.mp4?token=buoiHGUQNbLJSgu2kKMDDm5_05vN4fldYMriVsiDFDQ-h0sMAkld7dzkH-2JHGhE7p_FujoQTiezIOoe3d_dsDT_kF3KUtQEbCVSW22msnepZoTCiC6n77LB-TN26sldR834MpXjN70q_59eZCcdpd-ljS_w3FrCt1kxgE3tCdEmIgNBNQO4HHrB-zbimOzL_ADihGHXHDX2llzThj18aNA_OCVEGzwG9Hsl7pUMTQOeq3P2HyxMaNRH35YCKy6UVITzI3I0rvkLsqaL_DZuQUSIx3uYiVa50Ax2eK5d0tkSRum7iID4JGuoGbbiCGCreZNLYDxX_AC-IlM_WYPMGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فوووووووری
:
🔴
ماشاریپوف و نازون از استقلال جدا شدن :)
🔴
پ.ن فقط از استقلال ی سهراب مونده همه رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/135955" target="_blank">📅 18:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135954">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
اورونوف چهارشنبه‌ وارد ایران خواهد شد.
🔴
پیشنهاد ۳/۵میلیون یورویی الشمال قطر صحت ندارد.پیشنهادی باشد هم با میلغ بسیار کمتری است و از قرارداد مالی او یک میلیون و ۴۰۰ هزار دلاری با پرسپولیس بیشتر نیست/قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/135954" target="_blank">📅 17:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135953">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
قدوسی در خبری فوری
❌
احمد نور میخواد برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/135953" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135952">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2powt3VISfbzCYWvxDKAaExuVXVkvyHRkEZDKMiHYiu0valsfrUrT3n7pCtAmRabXaNGljafd62bv9CV1a1d0WG101QllddMqtnLGwpxmGpmp2rQtNBBhMKE8dg9msdy6StwPSIFnGpU_jGvRrj_ajaG8XR01S5aQm-9y5Uk-NLuk68MHBaKDqFsT06s94AFQKzmwS4PRc2GBHETFcr-B0SKPZYux8or7P34-5NR-AlvFwgyo81EL4AKurpAN7jCEszZ_amfCbZ4aKXizgPbYPptIJdBaRAYqNSQmDh1Ck881RGsqYC_TKHxyl1LPQ8Z_a2RtCbUs7M8iP50IarRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ابوالفضل جلالی بعد از پیوستن به پرسپولیس یه میلیونی شد
🎉
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/135952" target="_blank">📅 17:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135951">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
باشگاه پرسپولیس مذاکرات فشرده ای رو برای جذب سامان قدوس استارت زده ..
🚨
اما نه با مدیریت حدادی  با مدیریت خود بانک شهر .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/135951" target="_blank">📅 17:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135950">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
شایعات؛ محمدحسین اسلامی در حال مذاکره با پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/135950" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135949">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/135949" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135948">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/135948" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135947">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135947" target="_blank">📅 16:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135946">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fz1ioEWRpmi5XlNm_lbX9IZO6guIuPyVN_M3cZGg8ha526yBEagczgFAZjv5oYZ0EXAlDizQNcnlVPcyn1ncNQczXeGEWpc7k9ZRMXvaXLzPFmoDjnRVUGXr2RP8z88Tc_KGrdHeYJPWYeaUzIDSNyCKS1uGdAIox7_8dL9q7AwatC-HWf4EhcZyp1qX3LRoEmwW_5enzk4oFOTvBQS8jIL3RjH0-Okg77aTuBWGZGtkQHgW6s5khl97kvi2XOmsSE4lSneUZ-9ufhCMHyJc8joTUWG7d0Xo_xSaU5yHogVfhQH829J5Y-5t-5PTbKzIoQYQ3kxsNYK1LuST8TX1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ایجنت مرتضی اومده مرتضی رو دوباره به لیست پرسپولیس اضافه کرده ؛ باشگاهم هنوز برای مرتضی پوستر خداحافظی نزده
😑
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135946" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135945">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
سامان قدوس؛ بمب بعدی پرسپولیس؟
🔴
🔴
ورزش سه: پرسپولیس برای جذب سامان قدوس هافبک ایرانی اتحاد کلباء امارات درخواست داده و این بازیکن در لیست خرید سرخپوشان قرار گرفته است.
🔴
🔴
قدوس که سابقه بازی در لیگ برتر انگلیس با برنتفورد و تیم ملی ایران را دارد، یکی از…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135945" target="_blank">📅 15:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135944">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlyL0fZuwzbkU5OSWGo9pRpp7vletPKJfroUnQcJZRhJ4hdo_Q1F68KvQtdMfMXntoh-odfsaSQwM0dJVVDIf2CDyk7JWS4dUeEECYLGfQ_j5aFQ5U6VN9Ok9n2BsnqvCFuQ8VlgjmW4rHl7E3wNSaTGJ1x61UQFVwXYT5naVvQ0BHvKOT8QObxCS4Hoh9FbPyQNnLc6rYfkFNTajFewLX2v4jBJ66xZKDZ4g2Auo7gXmR4Dsb6oU2lfoxTKArxS2fNoM4gyie2EtA_sHhptIOGJ-WiHODjJ8xDaeC4RXfdNQUTRJkHpIEYqSmPGDQT9OaO6hk2YS05YBhFlsTTqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سامان قدوس؛ بمب بعدی پرسپولیس؟
🔴
🔴
ورزش سه: پرسپولیس برای جذب سامان قدوس هافبک ایرانی اتحاد کلباء امارات درخواست داده و این بازیکن در لیست خرید سرخپوشان قرار گرفته است.
🔴
🔴
قدوس که سابقه بازی در لیگ برتر انگلیس با برنتفورد و تیم ملی ایران را دارد، یکی از گزینه‌های جذاب پرسپولیس برای تقویت خط میانی محسوب می‌شود.
🔴
❌
باید دید مذاکرات پرسپولیس با ستاره کلباء به کجا می‌رسد و آیا شاهد یک انتقال بزرگ دیگر به جمع سرخ‌ها خواهیم بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135944" target="_blank">📅 15:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135943">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
عملکرد پویا پورعلی هافبک دفاعی جدید 30 ساله پرسپولیس در فصل گذشته لیگ برتر :
🔆
21 بازی ، 1 گل / نمره متریکا : 7/03
🔴
سابقه حضور در گل گهر، تراکتور، ملوان، ذوب آهن، فجر سپاسی، خونه به خونه، بادران، شهرداری جویبار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/135943" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135941">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWYtwiN0b3KhqR5T0634ktOI4xgWujj5qpsBFflM5TtwdbvJE1ySvhc4O6o-b-14qTSUXS5i0huDe7RYuQXxSRf7JNv7s54e9Pk_dSTcHOqONRVh9rd2YqcI6g2m0zkEAjtBm6hT5AiJnXtwE71OM7bGJgQ7EoyqF_dU41ucLqP5_hlFypVdc411QJmdnEp2lB7l7EPmkKB43R1hHGY7Mwp60qCHbgrfyIg7Gftk0k_fTV4lIXfxgbrRxO-aYf5knhLNORC-mf96gngSgU0J3VAD-0WuAGVNk2LCd7i-7t-gDMz0ZqTEec6RBJkRwzoi5wbMdxOAx9ouyfsVMQAt7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
فیفا قضاوت دیدار فینال جام جهانی ۲۰۲۶ میان تیم‌های ملی اسپانیا و آرژانتین را به علیرضا فغانی سپرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135941" target="_blank">📅 15:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOBFoMmXOMNpDs4KD_EO3uov577IzDv47SURsnBvdWuETT64_QFAuvXzLruTyWiBmKVeHBt5q-lmo-U2Udl7zwZ2_Hm2jKldupRWmfDkt-U8DU12nhSLJiSlMOpokRUc4FdeD2hJfcDPkw750Xqm7aTq2kwF_ynuCPWVnCkfn19aFLVeIIB40lhnj3pqW53J-FcA-N54VCJa0FPs_8I81rQt-IY7Vt5e55Okvi70W5W8IeqPBIZcZx7fVmkMsfqYiwy2Hb8y_5QfC3j8xM3ZA5h4i6PJvkZhmPMC2rMJHl6fyjC-aH1Fb_Xpu0Gcu44py1CyhUxqfNfzIhKl3y88lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز:
مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135940" target="_blank">📅 15:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135939">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙷𝚊𝚓𝙼𝙰𝚑𝚍𝚒</strong></div>
<div class="tg-text">تو دور زمونه ای که فساد حرف اولو میزنه کسی که وظیفشو انجام میده باید قدردان خودشو پدر و مادرش بود...</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/135939" target="_blank">📅 15:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompourya</strong></div>
<div class="tg-text">دیگه نمیتونی زحمات یکی رو بگا بدی خیلیا به وضیفشون عمل نمیکنن</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/135938" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وظیفه اشه  دیگه دمت گرم نداره  مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/135937" target="_blank">📅 14:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135936">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidreza. Sadeghpour</strong></div>
<div class="tg-text">وظیفه اشه
دیگه دمت گرم نداره
مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/135936" target="_blank">📅 14:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135935">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دمت حدادی گرم که باج به شغال نمیدد</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135935" target="_blank">📅 14:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135934">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamed 65442</strong></div>
<div class="tg-text">دمت حدادی گرم که باج به شغال نمیدد</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/135934" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135933">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamed 65442</strong></div>
<div class="tg-text">دم بانک شهر گرم</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135933" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135932">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🚨
❤️
پوریا پورعلی با عقد قرارداد دو ساله به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135932" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135931">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
🚨
شنیده ها: امروز احتمالا ۲ رونمایی خواهیم داشت
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135931" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135930">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
بااعلام سایت ترانسفر مارکت؛ باشگاه پرسپولیس بابت رضایت‌نامه محمد مهدی زارع 800 هزار دلار به باشگاه اخمت گروژنی روسیه پرداخت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135930" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135929">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx0yiA2WjRFn7dzHGvfpxv05_cSEGwSR4n8Vi3wPnNzyDF1Sgp0UbPlB9it5xpRlVFRDOrg_DLjG_Tctk1P33MqKNtAGjJvFLBV6-u7pQvT-UN7KahKcJ30fZsgS7XUI-7Vnj1X9N-rcZs63C-NNxSLNnMAxtB_FiDtnpY0EDzYYkVWHbXC982elg64KJr3ekeeUSys7_rXdoFj_L357LqK_U9kftRM1cjWKBXxnE0p0tlCdH15EmzQWF1fkUfR610m6aFAwke5S2Ifjoy0oJcLSSlhQhlhj8usrPrVE73cRoG7Z_RttBC5AMeGjuK6hs2_CKPqrP_fP28sChS_IzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام سایت ترانسفر مارکت؛ باشگاه پرسپولیس بابت رضایت‌نامه محمد مهدی زارع 800 هزار دلار به باشگاه اخمت گروژنی روسیه پرداخت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135929" target="_blank">📅 14:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135928">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atQSu6XTdFmhu-Wfb4Fl2Ei6CAvKGmxbLi0O769ZJC7IThho9K3ntie_kngI283hcBP8eM6WZsIjVm3bd1bNoqBL9clrHkTKVFwvFogao-G1MeNPe_CTMejIBI7_5sP8iaRYc6GoloQQNDsNQS_5GXhe91U0LBFp104-sm8HxT3ajxbly5FbYGzs_Supq2yEg-9Xuh--laDueMveiclwcee6KY3-oDCDGm6JR5F-T7sMRDAnAvvVP3fn9zvBYagGw3BMpJrWPEiQD5IdjZ5SOzb56qkfhjKtZjMoVNlk6hmowRVMGXg95iW1qF05vmVS2LxRDIpPE9LyP5Ga5WBUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» مدیران باشگاه پرسپولیس با نظر مهدی تارتار با این چهار بازیکن وارد مذاکره شدند.
⬅️
مجید عیدی
⬅️
محمد قیرشی
⬅️
پوریا پورعلی
⬅️
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/135928" target="_blank">📅 14:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135925">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
فوری از فارس:
🔴
انتقال پوریا پورعلی هافبک گل‌گهر به پرسپولیس تا چند ساعت آینده امضا میشه و به زودی رونمایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/135925" target="_blank">📅 14:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135924">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
✅
شماره پیراهن خریدهای جدید پرسپولیس
🔴
مهدی تیکدری: شماره 11
🔴
مجید عیدی: شماره 20
🔴
ابوالفضل جلالی: شماره 33
🔴
پوریا شهرآبادی: شماره 21
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135924" target="_blank">📅 14:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135923">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/135923" target="_blank">📅 14:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135922">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">#تایمز_توئیت
⚠️
تو این مملکت دستت رو عسل بکنی بزاری دهن طرف دستت رو گاز میگیرن، همین زارع رو نمیگرفتن به خدای احد واحد خار مادر باشگاه رو یکی میکردید وسط فصل….
‼️
نساجی برای ایری ۱.۲ میلیون دلار و برای طاهری ۱.۳ میلیون دلار میخاست
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/135922" target="_blank">📅 14:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135921">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
❤️
رسمی؛ محمدمهدی زارع به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135921" target="_blank">📅 14:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135919">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veH7CoUcikUsjRg31RKE-wTtWzl9Q359YydH3pdGahlM-BsIxrbXpwpk9NajFhtG8WWUiIP9rWzCbTRr7QYIH8g9g-P8rqECuA08wCKGUVOU5Xo2fOzz9fqW0BMLD_v9iLz-PpeJjZM_Kmmh1LrEiSFSgDJrutoNd7GpQJ6fqGahjHlBkRFgET9_XZUSJG8cPaS4eC7ylSKk7mU3vGA02nB6-r1O6avM2Sl2BJ0pBN0t6M_KlDXapZK7yZ9TlJKWITHD9eiuqxvtt860c9xtVShaees4nIUMQwPjGqyy7YDPlDEZazJsQWv9Hp-dBdmv8USa-Y00nNLdpd7pOYlhzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
❤️
رسمی؛
محمدمهدی زارع به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135919" target="_blank">📅 14:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135918">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#تایمز_توئیت
⛔️
❌
با یه مشت دیونه زنجیری طرفیم، باشگاه هرکسی رو میخره یه عده هستن فقط بلندن گوه بخورن
‼️
قبلا میگفتن بانک شهر گداست پول نمیده الان رفتیم یکی از بهترین دفاع وسط های ایران رو خریدیم (زارع) یه عده دهنشون رو باز میکنن که با این پول میشد ایری و طاهری…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/135918" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135917">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#تایمز_توئیت
⛔️
❌
با یه مشت دیونه زنجیری طرفیم، باشگاه هرکسی رو میخره یه عده هستن فقط بلندن گوه بخورن
‼️
قبلا میگفتن بانک شهر گداست پول نمیده الان رفتیم یکی از بهترین دفاع وسط های ایران رو خریدیم (زارع) یه عده دهنشون رو باز میکنن که با این پول میشد ایری و طاهری رو خرید یکی نیست اخه کون گلابی اگر میشد مغز خر خوردن برن زارع رو بگیرن ؟! اصلا میشد تو بلدی بیا بکن یه عده فواره گوزو پر مدعا نشستن بیرون میگن لنگش کن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135917" target="_blank">📅 13:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135916">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
❗️
فرهیختگان : قرار بر این شده است که  باشگاه پرسپولیس قرارداد هافبک مورد علاقه تارتار پوریا پور علی را امشب نهایی کرده تا این بازیکن بتواند از فردا در کنار سرخپوشان تمرین کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135916" target="_blank">📅 13:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135915">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135915" target="_blank">📅 13:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135914">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
❗️
محمدمهدی زارع در آستانه پرسپولیسی شدن!
⌛
انتقال محمدمهدی زارع ۹۹ درصد نهایی شده و فقط واریز مبلغ باقی مانده است؛ پس از انجام پرداخت، از این خرید به‌صورت رسمی رونمایی خواهد شد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135914" target="_blank">📅 12:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135913">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
مهدی تارتار از مدیران پرسپولیس درخواست کرده با توجه به شانس کم پرسپولیس برای جذب ایری و زارع،اقدام به بازگرداندن مرتضی پورعلی‌گنجی به تمرینات تیم کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135913" target="_blank">📅 12:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135912">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
تارتار شخصاً با زارع تماس گرفته و خواهان اومدنش شده؛ باشگاه هم میخواد از اخمت‌گروژنی تخفیف بگیره/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135912" target="_blank">📅 12:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135911">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
❗️
فووووووووری
❌
فرهیختگان : اگر میلاد محمدی با باشگاه تمدید نکنه ، مدیران باشگاه از مدافع چپ جوونی که با اون به توافق نهایی رسیده‌اند ، رونمایی خواهند کرد
🔴
گفته می‌شود تمام اقدامات نهایی خرید جدید تیم انجام شده و این انتقال برای نهایی شدن تنها به یک امضا…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135911" target="_blank">📅 10:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135910">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
میلاد محمدی همچنان تمدید نکرده و اخبار قطعی شدنش کذبه اما توافق داشته/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135910" target="_blank">📅 10:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135909">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
تارتار شخصاً با زارع تماس گرفته و خواهان اومدنش شده؛ باشگاه هم میخواد از اخمت‌گروژنی تخفیف بگیره/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135909" target="_blank">📅 10:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135908">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
✅
#فوووووووری از طاهرخانی :
🔴
زارع در آستانه پرسپولیسی شدن..کار تمومه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135908" target="_blank">📅 10:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135907">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
✅
یه خبر نصف شبی فوری، شنیده ها:
🔴
برخی از کارشناسان حقوقی معتبر به باشگاه اطلاع دادن کسری طاهری میتونه برای پرسپولیس بازی کنه و باشگاه داره مجدد واسه جذبش تلاش میکنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135907" target="_blank">📅 09:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135906">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
احتمال گرفتن رضایت‌نامه قرضی زارع بیشتره
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135906" target="_blank">📅 09:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135905">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
حدادی : پول اسکوچیچ رو میدم بازیکن با کیفیت میگیرم
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135905" target="_blank">📅 09:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135904">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
استانداری خوزستان:
🔴
پس از تهاجم دشمن تروریستی آمریکا به شهر اهواز خساراتی به منازل مسکونی اطراف وارد شده و شیشه برخی منازل شکسته شده است.
🔴
تاکنون این حملات تلفات جانی در پی نداشته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135904" target="_blank">📅 09:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135903">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rp_bWFtIhNKeLJMKRxXtcfzd9jBNxmq-imTZ_nk2XhVXxI6Y2I5Je2FrGUdIK7-PyaZN2hMnJSRXgZJGfEhIZIxwyY3eViP4a9YGOOGJ3Zk2c2NU971_VVlekyPGvL5TsA6qhYtZc61qZwEdhZMwF538m9DuuNJ2nAztOgvLqZwgtlmXdWt036ovmCqdzFKE1wxgqixkwpHx2D6-Jrax_HyZk4BuUk4hoN4s_r_D418QkPPMBhlUiRkUVj25hAOHNTDm0vr1TFLoK1w7g-AUk0cF3Yx1KYwoI2BBaKneP5whW05SyGPn4wXSZwEs6qEezg5DQqRSFqDN7vEuHtzEnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبح بخیر ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135903" target="_blank">📅 08:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135902">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135902" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135902" target="_blank">📅 02:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135901">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juEnYP9j3l9t8PxkbGe_CwvMATPYvmnJEg793lK5p5nXgvc_j0mDrCDFVTHt6c-KnvZ3LxjY10IX5eQ0VXrf-K4wMBUtCgOZbQgQSJAdSVHN2GQBRWKiu1ythuLGxL6Nqg1SMzOkNxsZZuqnJWfnB6dpScEUTCujRgL3i2MpgEj-G-Dy7ji18IbU7QFR8ZTXrMmaTqRRIAlcialdf-_8P3TWYbBqor7sjKle7H55nyAKywImozgPTMvlPU1Bb_MDn79hd0dbBfsJmxvGmfUtbJu0H4NZbST_rFQn7RLYW3_r94-trO7Xkqo_CoX3RBP7FBuWxVUYqns-wO9Quv3ydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
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
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/135901" target="_blank">📅 02:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135900">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🔴
شهاب زندی مدیرعامل نساجی کسری طاهری رو گول زده و گفته پرسپولیس پولی برای خرید قطعی تو نداره بیا با ما امضا کن تا شرایط رو فراهم کنیم بری پرسپولیس و طاهری هم رفته تفاهم نامه سه جانبه امضا کرده و بعداً فهمیده چه اشتباهی کرده/ فرهیختگان
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/135900" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135899">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
وای چه گل هایی زد آرژانتین ..گل دوم هم زد ..و انگلیس داره می‌ره رده بندی و آرژانتین داره می‌ره فینال ....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/135899" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135898">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
بازی شد یک بر یک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/135898" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135897">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
انگلیس گل اول رو زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135897" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135896">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
صداوسیما: ساکنان اهواز شدت انفجارها بالاست؛ از خانه‌ها خارج نشوید و تو خونه بمونید.
🔴
+طبق گزارشات شما گفته میشه برخی مناطق رو دستور تخلیه دادن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/135896" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135895">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
❗️
طبق گزارشات مردمی، شدت حملات امشب به اهواز حتی از جنگ ۴۰ روزه هم بیشتر بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/135895" target="_blank">📅 23:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135894">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
نیمه اول چیز خاصی نداشت جز درگیری فقط و تو مخی بودن داور   صفر بر صفر تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135894" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135893">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
فوووووووووووری
❗️
جواد خیایانی: رامین رضاییان به لگانس اسپانیا پیوسته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135893" target="_blank">📅 23:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135892">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
قاب سنگین امشب
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135892" target="_blank">📅 23:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135891">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
⚽️
@Tipster_Mafiaa
@Tipster_Mafiaa
⚽️
@Tipster_Mafiaa
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/135891" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135890">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpRtDs-NPJTi9KKWX-ce9qV8iZ-UTkVA1uWuJdDsCjvUkozOO7VsoboHojkNwSeciasiIGYYYzb6s--oqnN_FxVuZvOdAVysYWBofMbpq8Vw_sHXr-cRcAqeso7HatCHlW3EwbQRlIUcTlRkUHBC37f17Q1oVES-GY5q9-oR-9nAoN_e7YMuwL0IY-mIOY0JeU2-KTLkapzyxxgmmfq6gn-3m7-_MJKCTcW8QMllx4F_T5PSQJ2uapSGckgnQizGkUmNHW58888KB5RcheqchzlC5OAkDtW7qPj0ut5A_rD3fwDx-u2OO8GYTSGzOUwOwkZ5mZEDQLe84QnLQeLIaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135890" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135889">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔹
🔹
آغاز بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/135889" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135888">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a436b0d04c.mp4?token=AEF6KcA1GA8EaDNXIBFHm3A1nEHLkYJV_Mw4jz3kyk62xft_kGF_Lbjb2zs0ybh62eqncu5aT9Ka8D0Ms1RQ50ArON1wtQnb5cmDfrvkPo02Iui6PZBvj6ZoqVslUmE65XU3zGLxijt-ldEnHRHdvQKk__vnpZ6oYZAwcAXEsTAFyZqvja08S_3wmcHZb_6R0mR-7g-dsX4p04M8mxNjLMZn4VUMydxMFnl2B5nYN-tp3NazvEMGi2X7oDQFrWtWYkFsk6do58Hto4uKOfiJQrk0DQpbd4hSumTLzopSVw25lsn252ci-iAUWBMXISWyKHKQWuk1JV-94nzu4WWaEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a436b0d04c.mp4?token=AEF6KcA1GA8EaDNXIBFHm3A1nEHLkYJV_Mw4jz3kyk62xft_kGF_Lbjb2zs0ybh62eqncu5aT9Ka8D0Ms1RQ50ArON1wtQnb5cmDfrvkPo02Iui6PZBvj6ZoqVslUmE65XU3zGLxijt-ldEnHRHdvQKk__vnpZ6oYZAwcAXEsTAFyZqvja08S_3wmcHZb_6R0mR-7g-dsX4p04M8mxNjLMZn4VUMydxMFnl2B5nYN-tp3NazvEMGi2X7oDQFrWtWYkFsk6do58Hto4uKOfiJQrk0DQpbd4hSumTLzopSVw25lsn252ci-iAUWBMXISWyKHKQWuk1JV-94nzu4WWaEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریم باقری: اگه جام جهانی رو 64 تیم میکنن ماهم به عنوان تیم پیشکسوتان تیم بدیم بریم
😂
😂
😂
🔴
+ خنده های علی دایی رو
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135888" target="_blank">📅 23:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135887">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
یاسین سلمانی ماندنی شد
🔴
با نظر مهدی تارتار، هافبک جوان پرسپولیس در جمع سرخ‌ها باقی خواهد ماند و فرصت دارد خودش را در فصل جدید ثابت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/135887" target="_blank">📅 23:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135886">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
#فوری | ترامپ به فاکس نیوز:
❗️
حملات علیه ایران هفته آینده گسترش خواهد یافت و خاورمیانه برای آنچه بعداً رخ خواهد داد آماده میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135886" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135883">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
کی میبره؟
🔹
آرژانتین
❤️
🔹
انگلیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135883" target="_blank">📅 22:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135882">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
#فوری | ترامپ به فاکس نیوز:
❗️
حملات علیه ایران هفته آینده گسترش خواهد یافت و خاورمیانه برای آنچه بعداً رخ خواهد داد آماده میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135882" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135881">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔹
🚨
خبرگزاری فارس: پرسپولیس علاقه ای به جذب آسانی نداره
🫤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135881" target="_blank">📅 22:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135880">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
مسئول باشگاه مذاکره‌ی پرسپولیس با یاسر آسانی رو تکذیب کرد/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135880" target="_blank">📅 22:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135879">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udJJ-RkMhIbcF_IaSoiftT9yisiIadMWMdwkRz1nQTNaAks1xGLxmgA5wegXQXHn7vQU9S72r3m0jel3jpdvHgwYen3xy3kYklQpm9qH9lDNWAr6jPQxfIN1xxlc5F3KwpYRamiFdLSoisxk-MG35T27QvUA-oUde1JyK83kh4P-PUTjGqKC2y8uDzCyHobCA2yytCPq-OOlG7X9tnLJJutOKpwDyPTsoNjj3IcS5Pw0MYSAFG11wmnTCNDQuyJUNxdqnpcclvENXZHVzkJiiZQFTdYYGLvvCWrfldWdn4IXG0X44y7fhyWbfs97ruPCm0LTwDl9_QXmg9LxT_k96Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کی میبره؟
🔹
آرژانتین
❤️
🔹
انگلیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135879" target="_blank">📅 22:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135878">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
🔹
تارتار هنوز درباره‌ی جهانبخش و قدوس نظری نداده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135878" target="_blank">📅 21:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135877">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
احتمال گرفتن رضایت‌نامه قرضی زارع بیشتره
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135877" target="_blank">📅 21:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135876">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
کریم باقری، کمکی که هر سرمربی آرزویش را دارد/ چرا او هیچ‌وقت سمت نفر اول بودن نرفت؟ پاسخ از زبان خود آقاکریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135876" target="_blank">📅 21:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135875">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
#فوری | ترامپ:
🔴
🔴
ایران مدتی پیش با ما تماس گرفت؛ آن‌ها می‌خواهند یک توافق انجام دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135875" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135874">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
علیرضا بابایی، مدیرعامل باشگاه چادرملو: متاسفانه طبق آخرین شنیده‌ها برخلاف پیش‌بینی‌های قبلی، کنفدراسیون فوتبال آسیا با درخواست فدراسیون ایران برای جابجایی نام چادرملو با گل گهر مخالفت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135874" target="_blank">📅 21:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135873">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
مخالفت AFC با درخواست فدراسیون فوتبال ایران؛ گل گهر نماینده ایران در آسیا شد!
🚨
🚨
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/135873" target="_blank">📅 21:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135872">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❗️
فووووووووووووری
‼️
مدیر طویله استقلال: ما برای جذب دانیال ایری با باشگاه نساجی تماس گرفتیم انها به ما کسری طاهری را پیشنهاد دادند و به ما ثابت کردند که قراردادش را با این تیم امضا کرده است! ما هم در نظر داریم هر دو این بازیکنان را در صورت باز شدن پنجره نقل و انتقالاتی خریداری کنیم در غیر این صورت آنها نیم فصل به جمع اصافه شوند!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135872" target="_blank">📅 21:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135871">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135871" target="_blank">📅 21:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135870">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/135870" target="_blank">📅 21:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135869">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228cd1f66e.mp4?token=my6eNnKZrqOrIrjEoT5ciqO6jVJFp4gHdH7mVvw3PMA7gbFbt38G8zjR3ANYKYEc-z_fFIkAfF64E9kv5KBsrhysU97DRN1bAjM0PEzz3IVVvreLMkW8YoSqre7fzmOnLl7XDp6btk5YfoalufwpjjzkoH-jO0AJ6WQkqj37F1EyNBTNBopVMpQ9Vz96yXo5SSXAXAoajkeKSE8ivO6QFBNb6JEXs8sK91TbWAD-ZvfVJGCUZjxX4A9JBOT2B5uYg3LfS97lOTwg2K_m40KzqbhSdBodK6rgq0J_UHzSan3FVuSHDQra6c0K92GJAH9IoXWVPNRpASoHd6ttEmsTYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228cd1f66e.mp4?token=my6eNnKZrqOrIrjEoT5ciqO6jVJFp4gHdH7mVvw3PMA7gbFbt38G8zjR3ANYKYEc-z_fFIkAfF64E9kv5KBsrhysU97DRN1bAjM0PEzz3IVVvreLMkW8YoSqre7fzmOnLl7XDp6btk5YfoalufwpjjzkoH-jO0AJ6WQkqj37F1EyNBTNBopVMpQ9Vz96yXo5SSXAXAoajkeKSE8ivO6QFBNb6JEXs8sK91TbWAD-ZvfVJGCUZjxX4A9JBOT2B5uYg3LfS97lOTwg2K_m40KzqbhSdBodK6rgq0J_UHzSan3FVuSHDQra6c0K92GJAH9IoXWVPNRpASoHd6ttEmsTYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔉
دانیال مرادی رئیس دپارتمان داوری فدراسیون فوتبال: تمام ورزشگاه‌هایی که در فصل جدید میزبان مسابقات خواهند بود به طور کامل به پوشش VAR مجهز خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135869" target="_blank">📅 21:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135868">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
کریم باقری، کمکی که هر سرمربی آرزویش را دارد/ چرا او هیچ‌وقت سمت نفر اول بودن نرفت؟ پاسخ از زبان خود آقاکریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135868" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135867">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjkbKlquhjO6P-QK1FFnhyoq8l2oIetai2xuNqtE5bN-SpWFNfx0Ab7dBSxEFBLyMz1mTy0SUPyP687jUZE9K-MJtu0UzB5W-qUzK-r2N8HAiP9RksVvSX1ta4PlOhZL-XUB1TSxr73ntZInrmrJMtR7pYNldkcwK_l4pcwl8wQNiG85x_PyGS0wxHgqvQqSr4BBYxdO22q7taqbvT4eV404q5N4IcHfZ85Hl6nGD5kBigFOpOc_a1yNK0WEAU-Vh0mtWmrRLcjT3idCZTWWpq5qX6kXJ-pq5DupHI8747m9i7Y9zXTqQtf6IJ6NgcP-e9W9PoqDkl1_oRZxWRElbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قاب سنگین امشب
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135867" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135866">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
🔴
ایجنت محمد مهدی زارع دقایقی پیش از باشگاه پرسپولیس خارج شد و گفت به زودی همه چیز مشخص خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135866" target="_blank">📅 20:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135865">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
❗️
با رضایت مهدی تارتار از عملکرد مارکو باکیچ، این هافبک در جمع سرخ‌پوشان ماندگار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135865" target="_blank">📅 19:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135864">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
✅
امیرحسین محمودی ستاره جوان پرسپولیس امروز ۲۰ ساله شد
❤️
🎉
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/135864" target="_blank">📅 19:21 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
