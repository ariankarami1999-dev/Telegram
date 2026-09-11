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
<img src="https://cdn4.telesco.pe/file/F4jCF1Cm2B3UF3Rz1yfhetGH6jaF4tswcKSQ0dOy90Aa7b0o2lFQD3pj4jPddHWAFhvHm8O1xNtEi6QxO3keeogNiZtn5z6skfvG0HbIxxRUUZmDYO06vovUiJtkVF04f_YkwkNKir_yZ-Dmiaju3ekI1ydnKOa_3JcZlKZ3qNDFARd_OV7Medg4czOxAa0IJgkpZcy00LeT_elI9BbYDfzKwwV7hj-GT1DafnjYx_jZgiV2sK97dEtHbyUEolvvHicOILommkxvFk61uIcqWflp3G15ZdZUM9F5PDJWQ_ZDpdiWkMCje_ooWytUa7g9WkMJII6V4-qI3knec3UYSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 04:46:05</div>
<hr>

<div class="tg-post" id="msg-139880">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZvCnySbFA1wV2e4bqAdw0-2fXdjZBYJqP9GCoqO_jl7WWIOT0Vm-P5QduJ9O_JgS2laml-7ggjrSGFiO9P7zDrpOzUCkik23EqAA-XXwLcQiffAIKKTsVcjffB4REBG2qFURgB7qnvT8nNbwfj-cL7uRHO451--fhBom-8GEbBxve94rwScIPxdHV4iGZfVLWYpzI3_LCvSCD-Ca0tqDQTeX8dqpL6DXBjIwZNwFAcMjwG6lS_wkaHHurJYy4KmU5MKEc5T0_AO1FXlFgTESbUKJ3unEwqv1JM63Q6huwrlylImujtWAyYLtdA_W0d-sh90p9zXBagtfu26VtZ4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سابالانکا مقابل پگولا؛ قدرت سابالانکا برابر بازی حساب‌شده پگولا. ریباکینا در تقابل با گاف؛ نبرد سرویس‌های سنگین با سرعت و دفاع. دوئل‌هایی نزدیک که تمرکز در امتیازهای حساس تعیین‌کننده است.
🎾
Sabalenka -
🎾
Pegula
🎾
Coco Gauff -
🎾
Rybakina
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژ خودتو انجام بده و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/139880" target="_blank">📅 01:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139879">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
روحیه بازیکنا که عالیه امیدوارم در نهایت بازی با خیبر برگزار بشه بهترین فرصت برای گرفتن سه امتیاز و رفتن به صدر جدول
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/139879" target="_blank">📅 00:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139878">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7d8a9c3c.mp4?token=i1d8K2fH-hmtP1pczBJtN5cPWzAfuiX3ylRdJGYDxttf0_08waG6L5UhXj-0LEcvRu9GEjmuhEaAz-ORvB5CHsa08I8ADM9Rm9f0eYE6o0J0T6SAErz8KPIt8ya_v6MPUGOV14ddcrX3dS9RnMUWvdW-4LCXXnsAjvlUDqh0HMo1VT-0Bz1gJFaIxzexP7RfPOxWAIptXaJ5ErdlPsSr7svqWjF23_n34nzd4yb865qTiM8w-DyHydG8F8qV5pwhvduLX7tK_ZG8ctc3AODOJHQBAa57jEoCzPtGiBhMs1G4lHwNO7KPlpD7pXbdlrTGsUZ8tqYruNCfBSQIthnCioi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7d8a9c3c.mp4?token=i1d8K2fH-hmtP1pczBJtN5cPWzAfuiX3ylRdJGYDxttf0_08waG6L5UhXj-0LEcvRu9GEjmuhEaAz-ORvB5CHsa08I8ADM9Rm9f0eYE6o0J0T6SAErz8KPIt8ya_v6MPUGOV14ddcrX3dS9RnMUWvdW-4LCXXnsAjvlUDqh0HMo1VT-0Bz1gJFaIxzexP7RfPOxWAIptXaJ5ErdlPsSr7svqWjF23_n34nzd4yb865qTiM8w-DyHydG8F8qV5pwhvduLX7tK_ZG8ctc3AODOJHQBAa57jEoCzPtGiBhMs1G4lHwNO7KPlpD7pXbdlrTGsUZ8tqYruNCfBSQIthnCioi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
دقیقه 95 بازی استقلال و پیکان، یاسر آسانی به یکباره بعد از سوت پایان بازی مصدوم شد تا شایعاتی مبنی بر مصدومیت تعمدی برای عدم بازی در لیگ نخبگان به اوج خود برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/139878" target="_blank">📅 00:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139877">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
✔️
اتهام بزرگ خداداد: فدراسیون پول آپدیت VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/139877" target="_blank">📅 00:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139876">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UC8b-X_o6rWaUnKm3CKpHOKey3gvs61343OY6qBNA42vveyXTo2V4Ivy1e75zZd_6F2ZHaZ7SJjCprRXLZVE5cCQVaIqZYNOL_IAIkcU4EzmLXRk_FQEILoP4evwLbZfEPH227TQb_Z3VO7VVdq8F5rkitOUYO9-FK4BjSytQyV0_VQ2USK6dycODDKzzYx7LH99aDIpA35BkT4FZb9Iz_51xOomy1MPaUNIgObs17gDZ0tnR49aiAAqixChNoRyJi1kJ-baQBu__B4YdEleU_aIq88XUb5bsr5R4HNP77mPq6g9R10RjitiRQqc7rbLyLow1PLx3kHHoUQnn-Dpmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
جدول لیگ بعد از بازیهای امروز
پرسپولیس با برد خیبر می‌تونست به صدر بره ولی آقایان رنگی تصمیم گرفتن خودسر بازیها رو به تعویق بندازن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/139876" target="_blank">📅 00:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139875">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🗣
🗣
ورزش سه: یاسر آسانی به علت مصدومیت دیدار برابر السد قطر رو از دست داد
‼️
السد قبلا اعلام کرده بود آسانی بازی کنه می‌ره شکایت می‌کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/139875" target="_blank">📅 23:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139874">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
پرسپولیس با مدارک جدید دوباره پرونده آسانی رو پیگیری کرده و معتقده حضور این بازیکن در استقلال غیرقانونیه. سرخ‌ها میگن مدارک جدیدشون کامل‌تر از شکایت‌های قبلیه و امیدوارن این بار نتیجه پرونده تغییر کنه.
🚨
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/139874" target="_blank">📅 23:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139873">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
#منهای_پرسپولیس
✔️
✔️
استقلال ۴ روز دیگه با السد بازی داره و السد تو پنج بازی اخیرش دو بار حریفش رو شیش تایی کرده به بار چهارتایی و یه بار سه تایی فقط خدا به دادت برسه استقلال :)
✔️
✔️
شما فقط مراقب باش دوباره خاطرات العین و الوصل رو تکرار نکنی قهرمانی…</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/139873" target="_blank">📅 23:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139872">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
یا الله بسم الله اسماعیل کارتال ...
🔥
❌
پ.ن چه تیمی داره حاج اسماعیل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/139872" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139871">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TplSzabvnIv3ftJI-WSjqOWL3WYgSBHDgOioPwIs_NDeR9yWxoYdZoXa0qOut__r9o_46Bir6P3Vfmhh33IT3sakdxMyvlECYSQhjPoTkMGffUj_jpNuRwxSiC28JZG2Nfu0D643nYjgoGkIbZMq2FbldhUpfjhJY8cWHnbc-QX3imEID1lUhDHTXd5nWWZkC1pDzpTmWDc2nHr874IhwmZxINsNq59bjWo1qTeIe9ZqEoW2tyCo3-zrnqGdEjbjGZ6L2-mnRCnPQbsEBOlCLJ9tNXdZnpkxTRPkYbpAf2iguEb8RaOo52HgDR-Rjaeqt1rRkfInXi_o6pgTgd214g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پس میگفتید که استقلال خوزستان ضعیف بود که ما چهارتا زدیم؟
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/139871" target="_blank">📅 23:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139870">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
✔️
اتهام بزرگ خداداد: فدراسیون پول آپدیت VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/139870" target="_blank">📅 23:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139869">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
خداداد طلبکار هم شد
❌
❌
بعد از فحاشی ناموسی و اظهارات بی شرمانه به امید عالیشاه، سرپرست تراکتور:
❌
❌
دارم میرم مشهد به یک زمین چمن سر بزنم؛ فردا از باشگاه گل‌گهر کسی ویس منو ضبط کرد در جریان باشید/ پسر بده فوتبال ایران هستم؛ شما خوبید  «سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/139869" target="_blank">📅 23:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139868">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
بازگشا :
❌
سازمان لیگ بهمون گفت بازی بخاطر یک ملی پوش خیبر لغو شده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/139868" target="_blank">📅 23:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139867">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
سهیمه پنالتی کیسه واریز شد...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/139867" target="_blank">📅 23:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139866">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfSCeg7tgaejxBx8aMYPuygzxKNuUq_k8weafow4s0SV1jaKGr88vFbFvk1WUDkt_6MJjsHjTVrcAmMaDDlHFTNcVgs4fwwZJ-PPxVIPggjhBlfMAMXp2f4GRt8Nc4A0kifmxXxUkpJLq_KXXHHOJPVGfrAZRYPzexJLTHC-BhdV18HODaWohEr5Kx_Es2XnPhYAoGBf89FWll-Da2LJ6CcSkkXu1_lKp3BGZxvZaou4IksOWoVL_h6rN4kawPtTE4KqzNmHpOzzsaPkwIGnEImq5STTmplOSOgpw3MIJCvHSJ6yZ28jf9Rz1aNT2jQpztW1zC0NQwYxXdmRNYh-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
روحیه بازیکنا که عالیه امیدوارم در نهایت بازی با خیبر برگزار بشه بهترین فرصت برای گرفتن سه امتیاز و رفتن به صدر جدول
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/139866" target="_blank">📅 23:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139865">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: تصمیم لغو بازی از طرف خود سازمان لیگ گرفته شد و برای ما عجیب است که چرا دیدار تیمی که فقط یک بازیکن در اردوی امید دارد، لغو شده است.
✔️
✔️
تمرینات و برنامه‌ریزی پرسپولیس همچنان بر اساس برگزاری بازی با خیبر ادامه دارد.  «سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/139865" target="_blank">📅 23:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139864">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
⚪️
⚪️
⚪️
⚪️
❌
⚪️
⚪️
⚪️
⚪️
⚪️
⚪️
لعنت به بی برقی ...برق نداشتیم شرمنده نبودم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/139864" target="_blank">📅 23:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139863">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tflixpyCW-Hz3sS6xGZP7Oz4eZRT7PcIH0NEgnVRNRKUpYansf3jwDvMtW0TmIQh-q29BdNRziLv_xg43jcov5eOM_klOjf6v1e3I-t7mGCagWCDNKFqSfd1SvP3VU1tdsJNKcVjS3Y-r0Wva-AnKtrr2CzukZzJJXzM9hPICQmbxahZgjkwMsyzTmmAiHealNFpxsx1xC9Cg8UR-Ij1nWus-0XqAvYha6lmyv7mNXQ0_PdhXeP0olg076s6Oo6K76EDarY6d3VmNiYPnuxErHLN3sPo_16QP2-vzjET85kWb9TfSZ-zo1ERDGlNwYmgaJlMeDEqAKdVe1EnD3CRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Bayern -
🟡
Bodo Glimt
⏰
Tonight 22:30
🏟
Allianz Arena
🔵
بایرن در برابر بودوگلیمت؛ بایرن برای جبران لغزش‌های اخیر به دنبال یک نمایش مقتدرانه است، بودوگلیمت اما با فوتبال جسورانه می‌تواند دقایقی دردسرساز شود. با این حال، اگر بایرن از همان ابتدا ریتم همیشگی‌اش را تحمیل کند، مقاومت نروژی‌ها خیلی سخت دوام می‌آورد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/139863" target="_blank">📅 21:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139862">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
سهیمه پنالتی کیسه واریز شد...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139862" target="_blank">📅 20:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139861">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
سهیمه پنالتی کیسه واریز شد...
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/139861" target="_blank">📅 20:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139860">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
تارتار:سازمان لیگ بیجا کرده بازی مارو لغو کرده...ما هیچ درخواستی برای تعویق بازی نداریم و میخوایم بازی کنیم...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139860" target="_blank">📅 18:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139859">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139859" target="_blank">📅 17:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139858">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139858" target="_blank">📅 17:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139857">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139857" target="_blank">📅 17:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139856">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139856" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139855">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139855" target="_blank">📅 16:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139854">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139854" target="_blank">📅 16:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139853">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139853" target="_blank">📅 15:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139852">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/139852" target="_blank">📅 15:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139851">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
تارتار: ما از تصمیم سازمان لیگ شوکه شدیم و درخواستی برای لغو بازی با خیبر نداشتیم؛ ما منتظریم تا بازیمونو سر وقت اعلام شده انجام بدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139851" target="_blank">📅 14:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139850">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
تارتار: ما از تصمیم سازمان لیگ شوکه شدیم و درخواستی برای لغو بازی با خیبر نداشتیم؛ ما منتظریم تا بازیمونو سر وقت اعلام شده انجام بدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139850" target="_blank">📅 14:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139849">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
با اعلام سازمان لیگ، ۴ دیدار از هفته هفتم لیگ لغو و زمان جدید برگزاری آنها متعاقباً اعلام خواهد شد.
✔️
ذوب‌آهن - سپاهان
✔️
خیبر - پرسپولیس
✔️
ملوان - فولاد
✔️
فجر سپاسی - آلومینیوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139849" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139848">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔔
🔔
فووووووووری
🚨
مهدی تارتار با لغو بازی با خیبر مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139848" target="_blank">📅 14:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139847">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6BUMCqRVZ56P4LyerUZMdBA5MoZRikRcswNrfhsuy4yGMELSJl7jeQ3ZA74wAXcLthFTSHoHN7eAoUOY1j-WdADADWolA8drmmQx6u4bnsYrLjORjWgkew1PCEBU0Rx0rJt_f5skrIVoDCuJTiJG_5OyC00yho4rS48H6H9faXGDZrpWF3gavgi49GBznfDUPsyp9gm1yZ26YkoAdf3dTtEQqaSE2Oq56h4hepviiKIiyGf9HIskwDHV3qXquRdmwBKZtvcXfH7C3HJRDP1qIFTGuHklfQiMMb7LM8xsbr5sto81_2o3HV4ctX0q8jXVHOXTh7u3nCoAlxDLVOkCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد مونیخ؛ بایرن آماده‌ی شکار بودوگلیمیت!
⚽️
بایرن با مالکیت و فشار هجومی بالا، شانس اول این دیدار است؛ اما بودوگلیمیت نشان داده مقابل تیم‌های بزرگ با جسارت بازی می‌کند.
انتظار می‌رود بایرن از همان ابتدا برای گل زودهنگام فشار بیاورد و برتری کیفی‌اش را به نتیجه تبدیل کند.
[
بایرن‌مونیخ
⚽️
🆚
🇳🇴
بودوگلمیت
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139847" target="_blank">📅 12:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139846">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
پرسپولیس-خیبر فعلاً طبق برنامه
🔺
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر ارائه نکرده، با توجه به شرایط موجود، این دیدار طبق برنامه قرار است یکشنبه برگزار شود، مگر اینکه در ادامه تصمیم جدیدی در این خصوص اتخاذ شود  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139846" target="_blank">📅 12:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139845">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
یحیی گل‌محمدی: فکر نمی‌کردم لوکادیا روزی در جام جهانی مقابل آلمان بازی کند/ او یک بازیکن حرفه‌ای بود/ از روزی که در تمرینات حاضر شد مربیان از نوع تمرینات‌ش راضی بودند/انگیزه زیادی از خودش نشان داد/ لوکادیا یک مهاجم شش‌دانگ در محوطه جریمه بود
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139845" target="_blank">📅 12:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139844">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔵
رسمی؛ رضا شکاری به پیکان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139844" target="_blank">📅 12:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139843">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139843" target="_blank">📅 11:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139842">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❤️
علی علیپور:
🇮🇷
🇮🇷
واقعاً افتخار بزرگیه که اسمم کنار علی آقا پروین، اسطوره بزرگ پرسپولیس قرار بگیره. خوشحالم که با کمک همه هم‌تیمی‌هام تو این سال‌ها تونستم تعداد گل‌هام رو به 96 برسونم  ﻿
🔴
ولی حتماً از قول من بنویسید که میراث، رکوردها و افتخارات علی آقا…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139842" target="_blank">📅 11:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139841">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139841" target="_blank">📅 11:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139840">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
عبدالله ویسی بعد از باخت مقابل پرسپولیس، از سرمربیگری ذوب‌آهن استعفا داد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139840" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139839">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
سازمان لیگ به باشگاه اطلاع داده اگه میخواین میتونید طبق قانون بازی تون مقابل خیبر لغو کنید و بازی نکنید حالا قراره تارتار امروز تصمیم نهایشو بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139839" target="_blank">📅 09:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139838">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139838" target="_blank">📅 09:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139837">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139837" target="_blank">📅 09:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139836">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf9VKkcsJXBnrN-7UVEtl6ChDC5OM9l8XwJk_-TtqhNBp5Nk8E3Ow830oqZVCpm6DeNadkKInnkObx3qVrq4ChunlgiJEa2ittP6DvRmiSRU3nmOSMq-nCxOBuVH3FWu2_sgbhsMkHQFdfy44Hybaik1rH5mVp1TNoS4uXPexqkKvnuL9jB2KrphsnJLMTmEVBMqgdW7GJTs2EJIAS0bKvj5yf8RSk2ptmvlsmCbWl_btcEvqKiYTlMWdwoQsMMQXV4y-8_9SAcJxquZHlA6XPMPtE7xXgS6oz_w1gest9lJJGeWDwHpgaiprmONF8HZu1ZxRgg9e-XvtOTd3x6Zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139836" target="_blank">📅 09:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139835">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU_Nh_pnLFe4EF1JbQRFJ_FPN2addHfsywwcMc4TSA26iiNfqKCoNFupeQKcIAGBC140U93ZwDcZrCpL1JmfLaUOvxItdXr68S4D0S_vNIbzKJiERrXhuaXkQmQQCUopkwVn71_A1W2a3BVz50EHtt_1OBuy-VObj9HxESx9MfcNZUjB2gxNgtxKt9EomwjS-EGZF3VuKxhHi3a_WqQGtjc81wqdF9cmUTSlN0V5XMVEl5KRnDh0voOl4GE2fH2AxbmAPlcXecxkasMfQPhT09fX4-BRn6gJRYAou14vj39ISILmcxSup8G_ZQQw3yE6nJvyjYkSeCvmIFP6JhEFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
جدال قدرت با جاه‌طلبی در یواس اوپن
[
الکساندر زورف
🆚
بوتیک فان دِ زاندشولپ
]
⏰
بامداد پنجشنبه ساعت
۰۳:۰۰
🎾
زورف با اتکا به سرویس قدرتمند و عمق ضربات از انتهای زمین، دست بالاتر را دارد؛ مخصوصاً اگر بتواند رالی‌ها را کنترل کند.
زندشولپ اما با سرویس و بازی مستقیم می‌تواند ست‌های نزدیک و تای‌بریک بسازد و زورف را تحت فشار بگذارد. با توجه به فرم اخیر زورف در US Open، کفه ترازو به سمت زورف است.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139835" target="_blank">📅 01:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139834">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139834" target="_blank">📅 00:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139833">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
احتمال لغو چند دیدار از هفته هفتم لیگ برتر
✔️
برخی باشگاه‌ها از جمله سپاهان سه بازیکن در اختیار تیم ملی امید قرار داده‌اند و به‌این‌ترتیب احتمال دارد برخی از مسابقات هفته هفتم در روزهای شنبه و یکشنبه لغو شود.
✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139833" target="_blank">📅 00:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139832">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139832" target="_blank">📅 00:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139831">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381bd5fd51.mp4?token=hF5maZ3dSHNlObeZ5IZlt6T9u0uOUotaP2MqmDESLQ8AWg6unk4MQjeZfwoa2q3mmYZKmbflwWPbbAzyYcZavSowkwt5yAAaJZZmZkHRGenRr7b1GE5horN32C4awZCrptFb6dg7_DYX8PL_I8ozCS81K8dcTcqhQsik3axPtJqnZvVsQ1cIkcCszrwdCi7d3pWSBqYUB7z5yLedVBKl20BuCdsk7xnlStFwGKU8CaVmbPHtDMzIzMyfUDienMYI8RZjeUdrJQ3xsfX4LK5aShn4ji06zAd2mwHJzsBj8fgbrSnKF4YBcZOjv_ewfRV_cSQBYkUQIEJ5hDUucJ9MxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381bd5fd51.mp4?token=hF5maZ3dSHNlObeZ5IZlt6T9u0uOUotaP2MqmDESLQ8AWg6unk4MQjeZfwoa2q3mmYZKmbflwWPbbAzyYcZavSowkwt5yAAaJZZmZkHRGenRr7b1GE5horN32C4awZCrptFb6dg7_DYX8PL_I8ozCS81K8dcTcqhQsik3axPtJqnZvVsQ1cIkcCszrwdCi7d3pWSBqYUB7z5yLedVBKl20BuCdsk7xnlStFwGKU8CaVmbPHtDMzIzMyfUDienMYI8RZjeUdrJQ3xsfX4LK5aShn4ji06zAd2mwHJzsBj8fgbrSnKF4YBcZOjv_ewfRV_cSQBYkUQIEJ5hDUucJ9MxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ ویدئویی منتشر کرده که تو پایانش بخشی از سخنرانیش تو زمان شروع حملات مشترک آمریکا و اسرائیل به ایران آورده شده: «خطاب به مردم بزرگ و سرافراز ایران، امشب می‌گویم که ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از آنِ شما خواهد بود.»
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139831" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139830">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95197e80eb.mp4?token=iY1G_Rsp5pkTEsBpghu-A1dbTXMkCiPejmWd-l4PYii_KKsbtl4shRa_kCHIuuT8krXW-BlDA_3nBB_tXIX_9n8jVJdLc9hNGLDMDFtd4KWt1LDp-DjVdkPvz4yUSqfcfUWXfFQz5cPLZpLYXusFRh9k93aRgfV_kcDpm9OU0nqE6OEIH7cSrRbjiRaFrglLCFRHlEDE9EyW7mWfCY-DrxgC4ZKQhE_yq6dZsg5RhrDYTZl2dWbsCmrGWCFuF6dqg3KW99rcZmU6_fM0PbKfBu-vgfR02FdXbFwfrvplKoQDq_6cWo9YDqPyxekbe4XB1ze_LTDseLC5e-wYVF7vCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95197e80eb.mp4?token=iY1G_Rsp5pkTEsBpghu-A1dbTXMkCiPejmWd-l4PYii_KKsbtl4shRa_kCHIuuT8krXW-BlDA_3nBB_tXIX_9n8jVJdLc9hNGLDMDFtd4KWt1LDp-DjVdkPvz4yUSqfcfUWXfFQz5cPLZpLYXusFRh9k93aRgfV_kcDpm9OU0nqE6OEIH7cSrRbjiRaFrglLCFRHlEDE9EyW7mWfCY-DrxgC4ZKQhE_yq6dZsg5RhrDYTZl2dWbsCmrGWCFuF6dqg3KW99rcZmU6_fM0PbKfBu-vgfR02FdXbFwfrvplKoQDq_6cWo9YDqPyxekbe4XB1ze_LTDseLC5e-wYVF7vCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139830" target="_blank">📅 00:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139829">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
پزشکیان پیگیر حل مشکل آزمون برای همراهی تیم ملی
🚨
مسعود پزشکیان، شخصا پی‌گیر رفع موانع بازگشت سردار آزمون به تیم‌ ملی شده و به احتمال فراوان مشکل آزمون برای همراهی تیم‌ملی در جام‌ملت‌های آسیا حل خواهد شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139829" target="_blank">📅 00:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139828">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
نیویورک‌تایمز: آمریکا و اسرائیل احتمالا هفتهٔ آینده به ایران حمله می‌کنن و تو جنگ سوم تأسیسات هسته ای ایران به شدت هدف قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139828" target="_blank">📅 23:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139827">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139827" target="_blank">📅 22:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139826">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
برانکو: هر روز به بازیکنان می‌گفتم پرسپولیس بزرگ است و نباید معمولی باشید
❌
❌
به شاگردانم که مربیان بزرگی شده‌اند افتخار می‌کنم
❌
بدترین روز زندگی‌ام، روز از دست دادن جام مقابل استقلال خوزستان بود
❌
❌
اگر به عقب برگردم باز هم پرسپولیس را انتخاب می‌کنم
❌
می…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139826" target="_blank">📅 22:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139825">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری
❌
با اعلام کفاشیان، جام فصل قبل به کیسه‌کشا داده نمیشه و باید برگردون تو غار  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139825" target="_blank">📅 22:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139824">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
تسنیم: پرسپولیس بیش از حد به بیفوما وابسته شده؛ بدون او سرخ‌ها توانایی خلق موقعیت ندارند!
✔️
نظر شما چیه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139824" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139823">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
✔️
هفت ورزشی: فدراسیون با اعلام استقلال به عنوان قهرمان فصل گذشته موافقت کرد
🙁
🙁
🙁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139823" target="_blank">📅 22:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139822">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdivZe3Hh8G_kPJpaGhOVzR8x-AVRLOacmFf2Ky1dn236JQYK4A2zVzysZ43cKFn2WiTxyeKUcksxMw2TgdxvYfMhbi-XclZ1UIeVudAKcI68DrlgXRuWw72uX8qaz6Br_0g-RfVOnEEQ3MpIC8nDAOwvFu5ZuBouSq5OrIaMx8hBCNHIrnXzcusRDw2TEMC8c6cL5eotDZcMksl7OJ6oMkGLJbRuev7Eozg9iJ8h-quDPmaWuD2ZDePKAp-r0YerZ15CHz3FnFsSzi5XzJNwAOR0clI1NztT1QhJUrSdGClH7qxalzJTQVp8yMwPVxGEw1r32fEpM_LVDZV1puDqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یه جام از منیریه پرت کنید جلوی این کصخل تا خودشو نگاییده
😂
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139822" target="_blank">📅 21:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139821">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGT_dhf9tOLg3aecHHl5x53J4ZoDQ5aTAnfHEfnidWQt0FQPQpSB1O2NsM0KKE914LnGgzpfku0EbpvN4n2JMNiQYfJcuWzxPybEF7C3AOjrooy-86JKS6orF3S_Sn8QlNYFBbIJPENc3n_DNIIwCJ8r9KBT79A8yex5izGJgAUkxqLT4SP1fNedQYvQkdbMn973B6piq28rzfqKgZpltalT_a0COJ7DUeC1b-QL_l2Tcfa5OCMYN3An41UgM9ib3Qb-47_qNwSYXHRJ0F2f3A1LSKhzaQj06XLdBdxcy4PoQUv-LnB-oeyiCAe5Apwk7ucyb4zSnWL9Fbw5fk3iUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دوئل سنگین امشب؛ لیورپول در برابر اتلتیکوی سرسخت!
⚽️
تقابل فوتبال هجومی قرمزها با ساختار دفاعی و ضدحملات خطرناک اتلتیکو، نوید یک نبرد نزدیک و پُرتنش را می‌دهد.
[
لیورپول
🔴
🆚
🔴
اتلتیکومادرید
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139821" target="_blank">📅 21:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139820">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⚡️
⚡️
ترامپ:
⚡️
از نحوه مذاکره آن‌ها راضی نیستم من هنوز درباره ایران تصمیمی نگرفته‌ام، آنها نمیتوانند سلاح هسته ای داشته باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139820" target="_blank">📅 20:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139819">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXVtWbq8YyJdwh4pEsZgd47fM2JmztoHuw5agACYb1bIRznTco99OctuhnYwYRNdBi4Xxf643rwDJoc-TXODlqq5JMYN3qofcUOUZjdUA11jFwEpF4JL0x-3ztFhf9ZjpO_CK_aZYY4wegPvKykq9joOdh3VPSwFcInjcWfrvAn-Cv5RVK22HKTzUYZ6bqbLunvn_kJio1qiFij0fBF0z78XDaEjdkHWJdkGwo6wmq8R6T039ZIXNiIL7eMwt5bIVUa2Cbfte-7hnsTypnkzNOVBzpEAJOgRYJQw5bty5QZ450VoJ1kUiFacE74sBFqDSTETTljpmuty8yTcXL-vJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس مدل دهه شصت
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139819" target="_blank">📅 20:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139817">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139817" target="_blank">📅 20:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139816">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139816" target="_blank">📅 20:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139814">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
✔️
✔️
✔️
✔️
فرهیختگان: دنیل گرا طی ۶ هفته که حتی یک ثانیه بازی نکرده ۳۳ میلیارد تومان پول گرفته!
😐
عجیب اما واقعی: دنیل گرا بدون یک دقیقه بازی برای پرسپولیس در این فصل، ۵۲۷۸۰۶ ریال قطر، حدود ۱۴۵ هزار دلار و یعنی ۳۳ میلیارد تومان پول گرفته است!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139814" target="_blank">📅 20:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139813">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4qv_p77gBUPHg3ipIBsl0BrX-mryrwKpRVo__DwpzKcEqF7j4fpgq5C18OTkB3hcaMJCBVdi5wiQcvzlAP2yZlFZMwgUnGWPQmcgjBLgQf8eMRQiXZT4sxsUyB_euKOx3o9KNhGPUKqWdS2qRJ7AaUYRU1syoMOjftIEwQl27VIdz4rIQnLJBpHmEPZbYpeqacndb3tmc5JDWIHIokTBsgxElZb6lXvT3pp9fwmqy_mvyUfTs3gsRWEWa1pKiB5Ux01CW9eeSNpslPYUwunoXUI9LXqg7sIIL1gMxMvTk9Hr3JeF8hZCODoTholDm9ZbAsJFiAPPXj927vz5I9JZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رسمی باشگاه پرسپولیس؛ اردوبادی کناره‌گیری کرد، صابری معرفی شد
‌
❌
سیدعلیرضا اردوبادی، رئیس پیشین هیأت‌مدیره باشگاه پرسپولیس، از عضویت در هیأت‌مدیره این باشگاه کناره‌گیری کرد.
❌
در پی این تغییر، حسین صابری به‌عنوان عضو جدید معرفی و با انتخاب اعضا، رئیس هیأت‌مدیره باشگاه پرسپولیس شد. مراسم معارفه وی نیز در نشست هیأت‌مدیره برگزار شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‌</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139813" target="_blank">📅 19:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139812">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🗣
🗣
شهرآبادی، ایری و لطیفی‌فر به دلیل حضور در اردوی تیم ملی امید، بازی با خیبر را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139812" target="_blank">📅 17:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139811">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
سهراب بختیاری‌زاده در آستانه برکناری از سرمربیگری استقلال
❌
[ قدوسی - قرمزآنلاین ]  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139811" target="_blank">📅 17:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139810">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
سهراب بختیاری‌زاده در آستانه برکناری از سرمربیگری استقلال
❌
[ قدوسی - قرمزآنلاین ]  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139810" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139809">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
سهراب بختیاری‌زاده در آستانه برکناری از سرمربیگری استقلال
❌
[ قدوسی - قرمزآنلاین ]
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139809" target="_blank">📅 17:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139808">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
عضو پنجم هیئت مدیره پرسپولیس مشخص شد.
✔️
به نظر می‌رسد روند انتخاب عضو پنجم هیئت مدیره باشگاه پرسپولیس به مراحل پایانی رسیده و حسین صابری خورگو به عنوان عضو جدید این هیئت معرفی خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139808" target="_blank">📅 16:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139807">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
فوری؛ سردار آزمون پس از یک دوره غیبت به تیم ملی بازگشت و اسمش در لیست اولیه جدید تیم ملی قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139807" target="_blank">📅 16:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139806">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
❌
اسامی داوران هفته‌اول پریمیرلیگ ایران
😀
استقلال - مس‌شهربابک/موعود بنیادی‌فر
😀
سپاهان - چادرملو اردکان/امیر عرب‌براقی
🔴
پرسپولیس - شمس‌آذر/بیژن حیدری
😀
تراکتور - پیکان/کوپال ناظمی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139806" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139805">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139805" target="_blank">📅 14:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139804">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
برانکو ایوانکوویچ سرمربی سابق تیم پرسپولیس بعنوان‌مشاورفنی زلاتکو دالیچ به کادر فنی‌اش در تیم ملی امارات اضافه شد و قراردادش رو امضا کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139804" target="_blank">📅 14:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139803">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
عالیشاه وکیل گرفت
❌
❌
شکایت عالیشاه از خداداد عزیزی به زودی در مراجع قضایی ثبت خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139803" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139802">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139802" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139801">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
رکورد تاریخی پرسپولیس
✔️
پرسپولیس با تفاضل گل +۹ بعد از ۶ هفته، بهترین شروع تاریخش رو ثبت کرده؛ آماری که فقط یک‌بار در لیگ سوم بازهم توسط پرسپولیس و یک‌بار هم توسط سپاهان در لیگ دوم تکرار شده بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139801" target="_blank">📅 14:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139800">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
✔️
آمار جذاب پرسپولیس تارتار
✔️
گل‌های زده پرسپولیس تا هفته ششم در ۹ فصل اخیر بی سابقه‌ست که نشون دهنده هجومی بودن پرسپولیس در این فصل هست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139800" target="_blank">📅 14:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139799">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPqEXyWxvrQrQZtH8mnJyfZSSscJvO6xoZA8n88FLa00IEyFB3xnmD9j8Mj6gADPFi2_xw4j88hXZd6IBR7Mvnlr58I1yjqpmveEVmmTrQqbVq6Ro3_oqbBSjcPRYBTPQ_BSqoWqCqwhrhQugC5B3xRoslsZuxtEbCQKFvTTZcOsjea9EE59mX4Dc-R_BciJgiPllmSbcNFc-RGRsne7U__2fZYZOVdiyBbt3oTW-G2rKDyWHUU0memzPPSeZdqdPqnRHnQ3O7fb_xJIyUm5SIKe4gLf5XOuZzbn-YQteAkCjlAZq8xYpui8moegsA1qxJoZVjvYUrZpvxEYdAB57A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دومین شبِ جنون اروپایی
چمپیونزلیگ دوباره با نبردهای بزرگ برمی‌گردد!
⚽️
شب دوم لیگ قهرمانان با چند تقابل جذاب دنبال می‌شود؛ بارسلونا در خانه به دنبال شروعی مقتدرانه مقابل فاینورد است، در حالی که پاری‌سن‌ژرمن با توجه به برتری کیفی ترکیبش شانس بالایی برای کسب برد دارد. در حساس‌ترین بازی‌ها، ناپولی و آرسنال می‌توانند یک نبرد تاکتیکی و نزدیک داشته باشند و لیورپول مقابل اتلتیکو مادرید احتمالاً با بازی فیزیکی و کم‌فضایی روبه‌رو خواهد شد. اسپورتینگ و گالاتاسرای هم می‌توانند یکی از بازی‌های پرتحرک شب را رقم بزنند؛ در مجموع انتظار می‌رود چند دیدار امشب تا دقایق پایانی کاملاً باز و غیرقابل پیش‌بینی باقی بمانند.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139799" target="_blank">📅 14:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139798">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeCbEhZEtdAChbfm4qk8lD9erqpldRGxniRowl0MqYhpMU8NQQKLARVdgYiuL0JpnOWDUmgcFGZJ3-pN7gXjMxv6kkoM3Efz3BSnXx3wXNbnD0SyyLNhjpBTSVervyPOlXXU3PabxcIG8NvBHyrLaev8vaElDzjfzneQpEbdjAaXvBoZcZWrV61yUyYb4iIHWjD3QLayZoYEb4fnFCqxDdFyl2fApR4KLjZSOyN2NL5BFXOtIACWK_1yi9c_z3BDWtbBRl4hhj0Dl9xsDxgZSBShg6GpmYkV9rkmREbLZP1t2bktkdwooeCoNIZu6avaOkR7Vdu9u03QSbIiCTDdhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
فوووری از یاشار سلطانی
🔄
🔄
در پرونده فساد فوتبال برای تعدادی از مدیران ارشد و چهره های فدراسیون کیفر خواست صادر شده
🗣
🗣
مهدی تاج ، محمد مهدی نبی ، احسان اصولی ، تهمورث حیدی و خداداد افشاریان افراد مطرحی که کیفر خواست علیه آنان صادر شده و طبق قانون از حضور و فعالیت در فدراسیون و کار به طور موقت محروم می‌شوند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139798" target="_blank">📅 12:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139797">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxWENDLQ3ZP5seVA-9ICojexzR-eKmrBboPmWjZoheYeE_1744ob_kvw5YqttSQ4XRQAa1WPtpzM95pd5tv03iusMRBeXTbnX1gSVLe8UIhciTOtKz2iS0cT_YyJ-dx1FufGjvm0ntodVbIz7nszn7-o9gNhy6DgQXT6MdRZkkOOCD_2QTybvpGIJTvVGecEmS-conyflmRvh2HOFHNSClKsQRDHpN9yZKTEI-4zVkSzBbV7i-enN6rqpXj9O7gp0UVFjw588Ox50DFbhsqKpKXy2jjO9m9XIDuCwQ7bQd1cN8amm7s3IsLkcu7KMEprJg9aBlcY7iu1dZrYoCajrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گفته می‌شود که باشگاه پرسپولیس تمایل دارد قرارداد علی علیپور و حسین کنعانی دو کاپیتان تیم را برای یک فصل دیگر تمدید کند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139797" target="_blank">📅 10:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139796">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
🇮🇷
پوریا شهرآبادی جوان ضمانت کننده آینده خط حمله پرسپولیس؛ یک خرید بسیار هوشمندانه از گل‌گهر که با استایل مناسب و دوندگی بالا در همین ۶ هفته ابتدایی که به عنوان بازیکن تعویضی به زمین اومده، نمایش قابل توجهی رو‌ رقم زده. امیدواریم با مدیریت درست کادرفنی و…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139796" target="_blank">📅 10:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139795">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❤️
❤️
تارتار از امیر حسین محمودی خیلی راضیه و احتمالا مقابل خیبر زمان بیشتری بازی کنه//ورزش سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139795" target="_blank">📅 10:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139794">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
دکتر حقیقت: ما کارمونو بلدیم نگران نباشید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139794" target="_blank">📅 09:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139793">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6dd97ad3.mp4?token=TbRkSA3kPDSUQaq-LwdwlXbPEqR-V_yeT2OxjDjMYvTEEwTkyvGr67h1dKupNDV5CBK5sepZSJG3omdCCjQY51WL5ICUrG5ZS5m_-Qom6WzpcteIP1JFBlLy0z83JEiYmqMlCIB2gSccRJ68tbLNXQ3zVSieZuuqTIiH13dfH1uInJ6fdILEW6kHqfCZxUF38VmW07AGi-oVFEi0-bkhWxbsMz-CyR79fLXcQbLq2BPBLs-LsIc3MfpfQhGRDKGGsyWc_3p1VWyocIUSAeT4vx8ThDKK4FWZZS0nwMVzcSIdsLcjxNSmAo3TB7DSr0klomN-O35SSaQ1OVeKXU0Zww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6dd97ad3.mp4?token=TbRkSA3kPDSUQaq-LwdwlXbPEqR-V_yeT2OxjDjMYvTEEwTkyvGr67h1dKupNDV5CBK5sepZSJG3omdCCjQY51WL5ICUrG5ZS5m_-Qom6WzpcteIP1JFBlLy0z83JEiYmqMlCIB2gSccRJ68tbLNXQ3zVSieZuuqTIiH13dfH1uInJ6fdILEW6kHqfCZxUF38VmW07AGi-oVFEi0-bkhWxbsMz-CyR79fLXcQbLq2BPBLs-LsIc3MfpfQhGRDKGGsyWc_3p1VWyocIUSAeT4vx8ThDKK4FWZZS0nwMVzcSIdsLcjxNSmAo3TB7DSr0klomN-O35SSaQ1OVeKXU0Zww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🔴
دو گل پارس جنوبی به پرسپولیس در دیدار تدارکاتی دیروز.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139793" target="_blank">📅 09:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139792">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139792" target="_blank">📅 09:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139791">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV_FyASy0zncFhs7XUVJBX8EPwBToWR3mx8rTNDfFZWCcTnkmgg7GGZD90ifj5vemR6qVSQPoAfOa_hz2LXeF3ir6WVuYtMIlFS_vLIAGuCqWAGN-M09ldv4tXKdWaZo2I17XgotS_LMv0IFNs1z4sdlntqpv4g52OM43Di2GWCDsO9vRubV_v0ZmBAaoKevA-CLXnPPkwCutvrLmsw8NuFAzAL7WMBUvvzubFXW6i0W3MgGzzUmteAH2RtOLaE7eSL5bEd9ZSnXh_7CwUgmRiHYhzL4wGTSwuhNIHc2XdeX5J343I1KYog1-ii-vOnWNppYLEzVbnu1beI5UIjE_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نبرد قدرت و تکنیک؛ در یواس اوپن
🎾
Ben Shelton -
🎾
Alcaraz
🎾
آلکاراز از نظر کیفیت رالی، تنوع ضربات و توانایی تغییر ریتم برتری محسوسی دارد؛ در مقابل، شلتون با سرویس‌های قدرتمند و بازی تهاجمی می‌تواند فشار زیادی ایجاد کند. اگر آلکاراز روی سرویس شلتون موقعیت بریک بسازد و وارد رالی‌های طولانی شود، کنترل بازی بیشتر در اختیار او خواهد بود.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و با ۱۰٪ بونوس اولین واریز پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/139791" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139790">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
زارع: جلوی خیبر نیستم ولی تلاش می‌کنم بازی بعدی باشم  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/139790" target="_blank">📅 00:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139789">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
زارع : حالم خوبه به زودی برمیگردم،  نفهمیدم چیشد پام به شیار های حموم گیر کرد و بغل پام پاره شد و بخیه خورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139789" target="_blank">📅 00:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139788">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف پارس جنوبی جم رفت و در پایان ۲-۱ شکست خورد.
✔️
سرخپوشان در این بازی با ترکیبی از بازیکنانی که در بازی شب گذشته مقابل ذوب‌آهن حضور نداشتند و بازیکنان تیم جوانان خود این بازی را آغاز کرد و در ادامه به دلیل…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/139788" target="_blank">📅 00:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139787">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
✔️
✔️
✔️
✔️
فرهیختگان: دنیل گرا طی ۶ هفته که حتی یک ثانیه بازی نکرده ۳۳ میلیارد تومان پول گرفته!
😐
عجیب اما واقعی: دنیل گرا بدون یک دقیقه بازی برای پرسپولیس در این فصل، ۵۲۷۸۰۶ ریال قطر، حدود ۱۴۵ هزار دلار و یعنی ۳۳ میلیارد تومان پول گرفته است!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/139787" target="_blank">📅 23:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139786">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
شرط سنگین گرا برای جدایی از پرسپولیس
✔️
✔️
شنیده‌ها حاکی از آن است که تارتار نگاه مثبتی به استفاده از این بازیکن در ترکیب تیمش ندارد و همین مسئله بار دیگر بحث جدایی گرا از پرسپولیس را مطرح کرده است.
✔️
✔️
دراین‌بین گرا برای جدایی از پرسپولیس خواهان دریافت…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/139786" target="_blank">📅 23:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139785">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
بازی رئال مادرید و اینتر هم شروع شده که رئال  دو گل زده تو سی دقیقه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139785" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139784">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
اگه اینترنت‌تون امروز بیش از حد ضعیف شده؛
✔️
طبق اعلام مدیرعامل شرکت ارتباطات، دلیلش اینه که فیبرنوری تو ارمنستان
🇦🇲
قطع شده و دارن فعلا پیگیری میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139784" target="_blank">📅 22:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139783">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIQAth2CCpkVctEVg52FDkJVyje_tT5_nECp8lEwbhalHOoj8qKOQ2dmbA9jtVdwgojEqvZ7mPSwgTVKotXP5Te-T_9vYF1U3d0I2t1fxwjCcNAC8Cqft1yxOQWWReBSiTOoIWPNrniax4EKjTSw70RjZI26v-thoexG4eQby6rCL0kQ2WRbJ1_m6VZNGewmVV1t5wHberLlh6vIKOvMKY9nrc5TsOlcqfdi9xCoFwnu7aUYfdoDDFsyx32aUqA2o7Oa_tGPyxHQdbl3ALjMF9QUsMkCD0hSNl0Bxxw3vLl4v1JGO2PGeFkQX_Lm9m0AYW0GgK8kr8gsPrDu-rPeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اگه اینترنت‌تون امروز بیش از حد ضعیف شده؛
✔️
طبق اعلام مدیرعامل شرکت ارتباطات، دلیلش اینه که فیبرنوری تو ارمنستان
🇦🇲
قطع شده و دارن فعلا پیگیری میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139783" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139782">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD_BKZhY3Q0VZnaRR6Sofn0FBnh90XsqFFNFbdko7pqYLYowliVSkIOEwqk_CWlsKi4_FjIg8vOGE7ZnqWp4heMZRyabfKlTKo01XpTzdcKoumzliEYHxLCOZ-zvW5DuvHHe69BMuSc1P0nA-vSZJcfxJ2tXBr3xZX3vO8rsmpMZwcYKceBeVR-Tlye81k5nNdpz9OONXwDkE9miRQZ50FuRE6jnKV_cfwVZ_yMivwO6KUaBNd5PGLBxvmuTyAqidUlmp_wTaQgQjgg6Ebz-vtpkFYZkYU8nz4W6Z_onRjsjm6IbHs-k4K7MpxCxcrYNLCWbK4OEXUk7oZtRIdTmhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
تیم ملی امید راهی ناگویا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139782" target="_blank">📅 22:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139781">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
فووووووری
🔄
با اعلام سازمان لیگ؛ فصل گذشته هیچ  قهرمانی نداشت و یه موز به استقلال رسید
😅
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139781" target="_blank">📅 22:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139780">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
دکتر حقیقت: پارگی نسبت بزرگ بود اما سعی میکنیم به بازی خیبر برسد حالش هم عالی بود تقریبا بیست دقیقه پیش مرخص شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139780" target="_blank">📅 22:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139779">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139779" target="_blank">📅 21:59 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
