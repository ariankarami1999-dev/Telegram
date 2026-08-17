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
<img src="https://cdn4.telesco.pe/file/UV_utVoWBCLzS2W0ogb2Zzcush8XpBP1MROzFaM9bbMPtTmPSwVFvEP3O_Jol_ov_5MB_qybM-tNAUvRoqtlcxXFAUX9iEfl_GYJYMpym9qoE9o5W61UMRO9jFrGxxFsNU50tqhZM7RJ5uUSYKxM0kPXg1ZZeabjVGMuvvyBwWCq5lqlL3zzzLdIdEn2Er1Frd_DHitvdyW69LPlI0PBglWkduCIoOIicraFbDBsXM-TbfeXERPgDQkbp_Ai4EktXkxmtRmiF7zQe9UFoFRZ01vZapNi997Im_3y6byhX2FM9Xec69P4xSCgmuxr9wmKMBiysydoR7ZLkcyFj_jBlg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 02:17:08</div>
<hr>

<div class="tg-post" id="msg-138440">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnx9Os0CU66NdubOp6YrGspapfzwkU7goRYSIpJMxR_hbrx2fyX2m7dL8Bsf1975h2blJFkbh4imB2Zxy9-hjPSWjSAM-iG3PDpvpElUhpUbGLO8iDBs8DlRUP2kExtno5H-34dnEuOMFU1UvZQfjXoehxns7rmIGvw4wZ-OdXWHFdT4OkkA9yT4VtiasHEZ1nYlG1LvyjjVPtFYl_TmuIsOM1g6XWmDdyPk0kz2s4HGVMFazQa9gdnITR2hfEadaIFTDyuhA99tC7E65IwCuCJg6G1HxNC-4JDY2PUcIcl1Wod77HeF_mxElVuOAQHNiwjXApk60A-EW5iAjantSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
رقابت‌های پرهیجان فردا فوتبال؛ از لیگ برتر تا نبردهای اروپایی!
🔥
⚡️
استقلال، سپاهان و تراکتور برای ادامه شروع قدرتمند به میدان می‌روند، و در سوی دیگر، فنرباغچه با لیون و دیناموزاگرب با وایکینگ می‌توانند جذاب‌ترین تقابل‌های فردا باشند.
چند بازی نزدیک و غیرقابل‌ پیش‌بینی هم فردا در پیش داریم؛ شبی که فرم، فشار و جزئیات کوچک می‌توانند سرنوشت بازی‌ها را عوض کنند.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فردا همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 372 · <a href="https://t.me/SorkhTimes/138440" target="_blank">📅 02:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138439">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOVOH6B526BofsOZVUuYF6aeGxkNi9e2092VCF8XrHJL_mAzyNCfdXiU7wqdqekecZvo-rA5mbDNhE3j2eYvIlZ2rT1du43zb6Kp8j5fsBLhBsRPgOFn7rnI12fB7Wib0I9MiT0fG0-ueaAjgaQtwg8x3Q9opXqMmyTtgq1BAPNCher39rNg6OksjMscbUX0LLk3CaqXnAHE_Zz208WDNe94QAr1GrHHabeou3qUovzUY16-j_gpeDEo_mngv7IkQaeqbvSTJNhW5Rxy0zdbCF6wa7m43jXNZ4AmQf3Xcw49OzSj1-ezGiv5YrurZSaB-WYKUZif3Dks7Lr1uZe8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
دردسر شیرین تارتار؛ ۴ مدافع برای ۲ جایگاه
‼️
⬇
⬇
⬇
با اضافه شدن دانیال ایری، تارتار حالا کنعانی، زارع، ابرقویی و ایری را برای قلب دفاع در اختیار دارد. زوج کنعانی و زارع در هفته اول خوب ظاهر شدند، اما حالا رقابت برای ترکیب اصلی جدی‌تر می‌شود؛ مخصوصاً با توجه به هزینه‌ای که پرسپولیس برای جذب ایری کرده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/SorkhTimes/138439" target="_blank">📅 01:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138438">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
محرومیت علیرضا بیرانوند در دو دیدار ابتدایی لیگ نخبگان آسیا
🔄
🔄
علیرضا بیرانوند در دو بازی لیگ نخبگان محروم خواهد بود/ تراکتور در لیگ نخبگان آسیا کار خود را با پارسا جعفری شروع می‌کند
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/138438" target="_blank">📅 01:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138437">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
قرعه‌کشی فصل‌آینده لیگ‌نخبگان آسیا فردا ساعت ۱۱ صبح برگزار خواهد شد
✅
پ.ن استقلال و تراکتور بخورن به الهلال و النصر بخندیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SorkhTimes/138437" target="_blank">📅 01:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138436">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
✔️
کوروش اژدهاکش با قراردادی قرضی و یک‌ساله به نساجی پیوست؛
🔴
این بازیکن از عصر امروز در تمرینات نساجی حاضر میشه. / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SorkhTimes/138436" target="_blank">📅 00:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138435">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiu_-0HdoZ9C2jwpJmCu7QB_4wSGmn0xOTb8yVmiVXnizUo7RD755thyFadp5bOyPlB4DXuwXLj5LGSPUS-mnTZIDX8P3x0gIjpWSpjbab4bW8hnMENEr_j2zIQSylbgjuwV8Y7ARJh86jAgPOzPQLj7BrdP52hzkzr9g18KyldbA66RL51EtA5xxq9rZzZK2TJnwOam1UUqPysDD0xNvb37WJVbwi11ikcvTjZMhcjpiaz6t2dSlAxrDYGoWkAHyz6qM01aVoKSGJ2paB6P4UAo10lIic5UY70B3U8b5iAgsISxb0k4zoJXJW9UgB_fO6-VOxba5_nhIjju3sFwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
سپهر خرمی: پرسپولیس امروز آخرین رایزنی رو برای جذب محمد قربانی از الوحده خواهد داشت
⏺
آخرین تلاش برای جذب بمب نقل و انتقالات که میتونه تیم رو تکمیل کنه.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/138435" target="_blank">📅 00:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
معاون وزارت ارتباطات : با اشاره به تجربه قطع اینترنت در جریان جنگ اخیر کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهاب شدید نیز میتواند بدون قطع اینترنت مدیریت شود و دیگر شاهد قطع اینترنت نخواهیم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/138433" target="_blank">📅 23:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
❌
لیست بازیکنان آزاد ایرانی با حضور محمد محبی ؛ علیرضا جهانبخش؛ رضا اسدی ؛ مهدی مهدی پور ؛ مرتضی پورعلی گنجی و رامین رضاییان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/138432" target="_blank">📅 23:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
کنفدراسیون فوتبال آسیا حق انتخاب کشور میزبانی رو از استقلال گرفت، مدت زمان معرفی استادیوم دارای شرایط AFC توسط استقلال به پایان رسید و دیگر استقلالی نقشی در میزبانی خود ندارد!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/138431" target="_blank">📅 23:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/138430" target="_blank">📅 23:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/138429" target="_blank">📅 23:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138428">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ad56d37c.mp4?token=kKkdd8e02a6bX-BFrAJw1v-nk-Lk_axcOj6LNn1_fpjskie3q9Flr0zuYibQFg0by__kFIC2UpFH22gE2H2tq1T0BaFCNfXc8Xp7Rx18Bpig2uypRSYT2ng-y_K5SfDad74cyLlucyJNpEhAjUweMjUJ0HVjY5_l43JzxMjr5a6OcAIEgGX3j1rDnVuQI7F9fDV0Fsvkhp9sq7JQe8GpMnkGW5XZ0Eij8knjNnIzIXXXL8aPrVt8gLwQZgw1V7xyQR5R_yi8cmNjT4z5zM9g5ZsEMqp-o-0toBO9ikg4S05lDyQ4GwWq8sflbxmPxnuoirSOPnbQvKgK6uyFd3_jyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ad56d37c.mp4?token=kKkdd8e02a6bX-BFrAJw1v-nk-Lk_axcOj6LNn1_fpjskie3q9Flr0zuYibQFg0by__kFIC2UpFH22gE2H2tq1T0BaFCNfXc8Xp7Rx18Bpig2uypRSYT2ng-y_K5SfDad74cyLlucyJNpEhAjUweMjUJ0HVjY5_l43JzxMjr5a6OcAIEgGX3j1rDnVuQI7F9fDV0Fsvkhp9sq7JQe8GpMnkGW5XZ0Eij8knjNnIzIXXXL8aPrVt8gLwQZgw1V7xyQR5R_yi8cmNjT4z5zM9g5ZsEMqp-o-0toBO9ikg4S05lDyQ4GwWq8sflbxmPxnuoirSOPnbQvKgK6uyFd3_jyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚽️
🧡
رامین رضاییان میان تشویق شدید هواداران فولاد با شعار « رامین، رامین، رامین ما دوست داریم » وارد خوزستان شد؛ فقط کلاه رامین رو ببینید
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/138428" target="_blank">📅 23:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138427">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
✅
خبرنگار: چرا کسری و دانیال رو خریدی!؟
🔴
شهاب زندی: من وظیفمه برای این هوادارا بجنگم. باید بهترین بازیکنا رو بخرم و باشگاه رو به سمت درامد زایی ببرم. شما نساجی را در سه سال آینده ببینید. قول میدهم بیشترین لژیونر و جوان را تحویل فوتبال ایران بدهیم
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/138427" target="_blank">📅 23:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138426">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
زمان و مکان نشست خبری پیش از دیدار تیم‌های پرسپولیس و استقلال خوزستان مشخص شد.
❌
❌
نشست خبری سرمربیان دو تیم در هتل المپیک و طبق برنامه زمانی زیر برگزار خواهد شد:
❌
ساعت ۱۹، امیر خلیفه اصل | استقلال خوزستان
❌
ساعت ۱۹:۱۵ مهدی تارتار | پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/138426" target="_blank">📅 22:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138425">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✖️
✖️
🤥
🤥
#شایعات
🖍
پرونده نقل و انتقالاتی باشگاه با جذب مبین دهقان بسته خواهد شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/138425" target="_blank">📅 22:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138424">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gml0BeAekSk6L7Ro_bBnOeC9dbuk4ANOnnF1bYAEUu_btLpqR6as3KwSPoO7a6A4Ih4ZOYTxk_lcwvG1H4s13-oZyC91HXyglbYB7GJqjRuwnhELmqIssBv8va4ZaP98lKEsA88M0qMSAuO9ITPDAA7H67dgjl5ZZinSLqC7imnDTWkJJzpBC_T7QBVsbJmb5RkDfWR9UsqXCtE-c9wDPNpm-jutFhamPynuFUFKqVJN0Mz2koSw0VDlizqEsLosWkW-hM96DcG2liAurzXWiQpzGHwAxcdit2e8eL45T0duFsVvsTe4IT2PSVcE6UbC8HbeFSCDapC2tnoDoVJy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دانیال ایری تو تمرین امروز اینطوری ازش استقبال شد
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/138424" target="_blank">📅 22:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138423">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
💢
💢
💢
به احتمال بالای ۹۰ درصد از بین مبین دهقان و محمد قربانی دوهافبک‌جوان الوحده؛ باشگاه پرسپولیس یکی رو قطعی جذب خواهد کرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/138423" target="_blank">📅 21:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138422">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyD_ObJWIfwovRILoF52q8pGVfPfjdiKdbUwX0yThG9QBLDKpysd-QRiQhr69fHrJHaG8IV4V9iRX2eZJe6fhw-uhO7Xjx_a0LidzaACh8Y_4sfi75s_XaFdchOKh8RFMMv9iKrvpRbRgoS1998ygfCcL3sZ_2qyHd4m176WAdc_90flkpII-0A8H7dqkpcPWe5DI2UGsuwfM80xeAfaL-sfZVL3ODlAXk04cwoZKoeYWV1NBWkA8vSU3ZeDiPtOg8jYiU9I1uYXdUTpHtXbmmvtglw_Qo_qiYtAdmVOqv7p9Xe1Tkp0gqaCrNIx0gRRt8QjQ62nf6n-b5folm5nHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
#تکمیلی
؛حاجی‌محمدی‌خبرنگار باشگاه تراکتور:علاوه‌برباشگاه‌پرسپولیس باشگاه تراکتور نیز علاقمند به‌جذب محمد قربانی ستاره‌الوحده است اما گلزنی او دربازی اخیرتیمش کار روبشدت سخت کرده و رقم رضایت نامه‌اش که زیر یک میلیون دلار تعیین شده بود به بالای یک میلیون دلار برده شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138422" target="_blank">📅 21:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138421">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">➕
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
➕
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
🔗
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138421" target="_blank">📅 20:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138419">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
رامین و فولاد سر همه چیز به توافق رسیدن فقط یه مسئله کوچیک وجود داره اونم اینه رامین 150 میلیارد میخواد و فولاد 60 بیشتر نمیده یعنی حدود 90 میلیارد ناقابل اختلاف دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138419" target="_blank">📅 19:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138418">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
سید بندی لیگ نخبگان آسیا منطقه غرب
❌
استقلال در سید اول در کنار: الاهلی، العین، السد و ترتر تو سید سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138418" target="_blank">📅 19:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138417">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
✅
گویا داره میره اهواز  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138417" target="_blank">📅 19:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138416">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
رامین رضاییان داخل هواپیما: انتخابمو کردم بقیشو میسپارم به خدا!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138416" target="_blank">📅 19:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138415">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
شنیده میشود مدیران باشگاه قصد دارند در صورتی که رقم قراردادی رامین رضاییان کاهش یابد و او تا ۴ شهریور با تیمی قرارداد امضا نکند او را جذب خواهند کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138415" target="_blank">📅 19:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138414">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
حجت کریمی مدیرعامل تراکتور: دنبال محمد قربانی هستیم و همه شرایط باشگاه الوحده رو هم پذیرفتیم ولی فعلا باشگاهش اجازه نداده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/138414" target="_blank">📅 19:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138413">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
باشگاه تراکتور گفته اگه سپاهان کسری طاهری رو مقابل این تیم بازی بده به فیفا شکایت میکنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/138413" target="_blank">📅 18:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138412">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
❌
پرسپولیس نامه زده به باشگاه الوحده و خواستار جذب مبین دهقان شده / فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138412" target="_blank">📅 17:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138411">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
فوووووووووری
🔴
مبین دهقان‌ در لیست خروج باشگاه الوحده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138411" target="_blank">📅 17:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138410">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQJyoSzThzn8mgbCmifq8RlAuIvi97WN0XI8LuwfAkxfyAgCw_V8n06oI0H6Pnjw0uIYbziazJLosTnCXauYH2gpTtH-l01sdBSIU7fFvhaDzq8UoRnfKl95mxww_9JDqON7OkL8wCZb2BRg8pSlJhP7nwL9kO5WRZ7nRy3exxY_VUhnK5Y4yjNP6P-STCskN50X89UusXuRRddGoyeK-iLXLIn6PAhkJFxy1kMNSRNqswGbTA24HR7m38vSBt_osHQ-qwbVHXVnPit1JGeBTFF1Xe35NmiEZOzZz-uFWlZEtTB_4OdPJhyXiyMzgBxb0m2LVFij-17XPPpwYd0m9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
عشقم (دکتر جون )فقط یه قربانی
🥲
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138410" target="_blank">📅 17:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138409">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqWEmpCoUJoycLxgQV9evr3jK3EtT1XOcV6iGUM-V0HPmmEuKmSDZoLyZtSALVCQDpwBdogeFY2qEAudBfmgSrFAM_3LDhhtUtCJ4TjvRsgkTYR-Qr4q4VAkj2hBoHvxtO8RbBNFlFDVzjwgC1_Q-cwJxisRLSN6xXnp575vfh0Wz3ZowRvAoFVMBDi6gxXwqCRq2zSA-5b_EJjG8nnr7pKmiiyokC2-2Wu6RiOTSIom1S6Vx_gAyrR8eLLm_Ybw03HX2ImM49uLEP4ayeGd4JfeG_PBvrGqnxOsOU32BN0wAAzoQgYdh1VIOBdSw-5ZqJC7O80fXqt6q538zjGkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرسپولیس باارزش‌ترین تیم لیگ برتر شد
❌
پرسپولیس پس از خرید و اضافه شدن ایری، تبدیل به باارزش‌ترین تیم حاضر در لیگ برتر امسال شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138409" target="_blank">📅 17:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138408">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
⚽️
✍️
دانیال ایری، مدافع ملی‌پوش و جوان فوتبال ایران با امضای قراردادی ۴+۱ ساله رسماً به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138408" target="_blank">📅 17:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138407">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🤝
🤝
🤝
قربانی رو بیار و بهترین پنجره تابستونی تاریخ رو به نام خودت ثبت کن دکتر پیمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138407" target="_blank">📅 17:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138406">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6470685323.mp4?token=j5s07EXV2qDxvIRWGhi_tYO7r5nyJFaF3YrHuPkmQBzDr2iOhd6xcvBlKeCKcS45QYXV2E6CeDoc7W4h2SaebVse4FgFvrv76VJ4iLJDt2hCPyBh9PgsvQiSXyKqFx3kzB6_XIhDd-WMaf30fHizsSKqv5J4Xn8Q7jc1dr_7A-EdVX2jz9Nzg1zGB7Y5nvxmhPmZlLkJ85SnEqqQToedisB3gxv45A3o1XNJR0KDd-pv3jCXlBiqd-DNdejXicYLDHxkqIcMSQYd1EDMJeA4GkNuI_ltC75GC2zyu5xvPB52JamGFi2opQ8i8hTdyq8wmA_s_t9Q3H8mziVDCIfjU4VWLXep6RUTbZHBJ6JJ83aM-Lzw5ElijBjYep8Tx-by8pri_uiyIK3tiWrI9f57XPMNbMPIFUkXHYai88PKmu98qM7hscrVbv_v-Dgx7cFde6Zd9KHTQ3rh0EozHI-EYTGcUo-yIR8TtE5SV5OjPM7S_cEf6JneaUJ3L68FP9Sie4BGh0dhQHoLFwdaKX7SRykghrSQph5Tj9RtsoqbvkOhE88VXVeN0zJOP3fiAnHhF8Sraqe5bdh5RnnxMtdImWRSeFyquW6_D7SpqHCdGSkcq7VJPSO9Ui2e6fCzI_Du5H-Vhlf9EcP0t21XFXG9KTMNC2ZYoKUgaIgNW06Mmbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6470685323.mp4?token=j5s07EXV2qDxvIRWGhi_tYO7r5nyJFaF3YrHuPkmQBzDr2iOhd6xcvBlKeCKcS45QYXV2E6CeDoc7W4h2SaebVse4FgFvrv76VJ4iLJDt2hCPyBh9PgsvQiSXyKqFx3kzB6_XIhDd-WMaf30fHizsSKqv5J4Xn8Q7jc1dr_7A-EdVX2jz9Nzg1zGB7Y5nvxmhPmZlLkJ85SnEqqQToedisB3gxv45A3o1XNJR0KDd-pv3jCXlBiqd-DNdejXicYLDHxkqIcMSQYd1EDMJeA4GkNuI_ltC75GC2zyu5xvPB52JamGFi2opQ8i8hTdyq8wmA_s_t9Q3H8mziVDCIfjU4VWLXep6RUTbZHBJ6JJ83aM-Lzw5ElijBjYep8Tx-by8pri_uiyIK3tiWrI9f57XPMNbMPIFUkXHYai88PKmu98qM7hscrVbv_v-Dgx7cFde6Zd9KHTQ3rh0EozHI-EYTGcUo-yIR8TtE5SV5OjPM7S_cEf6JneaUJ3L68FP9Sie4BGh0dhQHoLFwdaKX7SRykghrSQph5Tj9RtsoqbvkOhE88VXVeN0zJOP3fiAnHhF8Sraqe5bdh5RnnxMtdImWRSeFyquW6_D7SpqHCdGSkcq7VJPSO9Ui2e6fCzI_Du5H-Vhlf9EcP0t21XFXG9KTMNC2ZYoKUgaIgNW06Mmbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس دانیال ایری با شماره پیراهن ۸۹ برای پرسپولیس به میدان خواهد رفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138406" target="_blank">📅 16:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138405">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎤
🔴
گفتگوی خبرنگاران با دانیال ایری، خرید جدید پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/138405" target="_blank">📅 16:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138404">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBANdo8g4hod1bgfixZ9QBoOmzjBMShMdbkJdcHsZOhJ_-VL9dCkJF2OkJ26aXs9lF73p40OddNIPcrvwioPCgd3bLU0kcMDmeCK9mo-Fopx09_Q6Gb1WKKQDeDDCyjUrGf-ht1haQWbQYQcPwEptIS-HR8qh__zimWmXDSzHEcuCS3N_xI8ktUVIF6595wpv_1VPgSijZQnv5bX4uRjfIYPrwT5rzugeUk3wQJ1eDszZWJayT-GRow3_AWiCYus36VlKJ6Tw59sDPkhc_YAQijwVSi0T5veXsOiMLknaA0eqS14a5Hd5P0tIAnQgkzFIt6TDaLVGwap4N8reGi7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✍️
دانیال ایری، مدافع ملی‌پوش و جوان فوتبال ایران با امضای قراردادی ۴+۱ ساله رسماً به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138404" target="_blank">📅 16:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138403">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c01b72802f.mp4?token=UrxCyJ5BcgohnTYIfeB6XkATMWvHPsVWOEey6LeHUY1T9Rk2G2FBXEUinDicGJagon63UKO0Z35zIMNj-Hdmt-PiN45dIh1OLAlxKluEDxfGrc4OAtN2XqpJhtKugP_yhNbGSa9jcX1YqvLYIFfZycnOU7zhRVK8ThCuQ_5oJO8HA3nJersfKz8vhKovdi4t8FfIYckfc556RzENrvQLtTsKEDM3EXLP30CV66bLFGOwd8vbSbO7azfXbk7ztX_IeNMqyQE_labqCOGncaJ4njPn39FVlufQ9_qMt5ddTWc03FQjFt2l7KdjcPF52Yw7Heu9IvlsS5hJ1q1cyTcNcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c01b72802f.mp4?token=UrxCyJ5BcgohnTYIfeB6XkATMWvHPsVWOEey6LeHUY1T9Rk2G2FBXEUinDicGJagon63UKO0Z35zIMNj-Hdmt-PiN45dIh1OLAlxKluEDxfGrc4OAtN2XqpJhtKugP_yhNbGSa9jcX1YqvLYIFfZycnOU7zhRVK8ThCuQ_5oJO8HA3nJersfKz8vhKovdi4t8FfIYckfc556RzENrvQLtTsKEDM3EXLP30CV66bLFGOwd8vbSbO7azfXbk7ztX_IeNMqyQE_labqCOGncaJ4njPn39FVlufQ9_qMt5ddTWc03FQjFt2l7KdjcPF52Yw7Heu9IvlsS5hJ1q1cyTcNcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚽️
ورود دانیال ایری، خرید جدید پرسپولیس به ساختمان باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138403" target="_blank">📅 16:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138402">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
✅
تنها 30 ساعت به پایان ضرب الاجل 60 روزه ترامپ برای توافق با ایران باقی مونده و هنوز نه صحبتی از تمدید آتش بس هست نه مذاکره و توافق.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/138402" target="_blank">📅 14:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138401">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
❌
برای اولین بار در هفت سال اخیر ترکیب پرسپولیس پیش از یک مسابقه رسمی لو نرفت  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138401" target="_blank">📅 14:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138400">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
ورزش سه:
❌
مدیران پرسپولیس بخاطر ترس از هوادار از خرید امیر جعفری انصراف دادن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/138400" target="_blank">📅 14:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138399">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
پیمان حدادی : امیر جعفری دفاع چپ گل گهر در لیست خرید ما نیست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/138399" target="_blank">📅 14:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138398">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
فوتبالی: دانیال ایری امروز ظهر در ساختمان باشگاه پرسپولیس حاضر میشه و قرارداد پنج ساله خودشو با پرسپولیس امضا میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138398" target="_blank">📅 14:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138397">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pt9O-lk721aiUB7tY3HMHrCXP3Yp14mh9bY4TLoIjeG8ClSO9hhIzeaV330z9DQyMspSqGE4u25eEY8LCeqbOJHV-j3GS408BcvBcVROseazgqZ80WdDdNMU1wyeftOQ9JiWJPXlQ9tEcCTSCHQ6VbViMKO3IPqXZ11qEcoLM_nPis2pdkPbjy2j6GMxbA54EluXb1MOExtqlXxR4cFuTBYH-j06gUuP46OhxIKkh9n8wAm8U9ExvA7vKyIUT2YVKnC8iljAyvLTU7XVbSojHtJv7h9auqym0vye5MhH5QZWX40d02p8T2iqefngcSTv5-PRLqbwaM1XroYdLLTWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بعداز مهدی ترابی ، مهدی هاشم‌ نژاد بازیکن تراکتور هم بدلیل مصدومیت دیدار با پرسپولیس و سپاهان را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138397" target="_blank">📅 12:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138396">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT_Mo2RcZC4tsw1coh1Fwk0Lth1UQfP_PhjrvyKGNew_DLUyixc1aXn3LVQZuAwfBvb0njA0Oz5REfBbXe1a4hpikFxvLI6Wpaoq4vY4ETn_NGGyaxbJPthdDVvTUZwcLE9IiLB153V6uQtBAjJbhL08ZXF6jT-P_Zbe-3L1LK5pJXfvNThLc3NevirEg3KNGs0hxxhHDy9rQfia0qp-u4lZ7UJGWd3ghHFIPMCI0M-Za8bdd0sWUG-CMQw3ghMm4tI2IxBxXhAn0fnAMyGdUL8Zb6VFPa7-PAVtPCzncI2lR6GPtRPD36db0SZ-a1qR8XgNnEeVcaTkXgYHEPXXlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
نبردهای جذاب در فوتبال امروز
🔥
⚡️
چند دیدار مهم در برنامه امروز؛ از تقابل مدعیانی مثل الهلال و بنفیکا تا بازی‌های نزدیک سری‌آ و لالیگا. کفه شانس روی کاغذ به سود الهلال، بنفیکا و ساسولو سنگین‌تر است، اما چند بازی دیگر می‌توانند کاملاً رقابتی و غیرقابل‌پیش‌بینی باشند. با توجه به اختلاف ضرایب، بازی‌های مدعیان برای انتخاب‌های کم‌ریسک‌تر جذاب‌ترند؛ در مقابل، دیدارهای کرمونزه با سامپدوریا و دپورتیوو با الچه پتانسیل غافلگیری بیشتری دارند.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای امروز همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138396" target="_blank">📅 12:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138395">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👀
هد اسکاتینگ پرسپولیس دستیار بختیار زاده رو تعیین کرد!
🚫
فرزاد حبیب الهی هد اسکاتینگ باشگاه پرسپولیس پس از فرو کردن دنیل گرا به اسپانیا بازگشته بود و سمت پرسپولیسی ها آفتابی نمیشد حال با کمک پژمان راهبر پانادیچ رو به تراکتور برد و حالا هم ماریو توکیچ را به استقلال/ویژن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/138395" target="_blank">📅 11:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138394">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✖️
مهدی تارتار:
😀
ایگور سرگیف مصدوم است و هنوز به شرایط آرمانی نرسیده است وگرنه او جزو مهاجمان اول ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138394" target="_blank">📅 11:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138393">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/are2y3cUtZGSyPKBSNolMNSW07jMwWXLTd5q3gH7HTAzQnrb_1RnZ9Lip4RjnJ1qZ8AOQfSeFd6bTrzExcPiA6-jOuNqUDIWhQARVkCiM6PylSpfIj9mVhw6dhGrk7cWvcHr93pk_PbhCONDm3xs2kj51gk2wHkxWIUDbhuA6TEybsIXw-qPxEWwfGkcfpOdgyCskfb8GJRDIEMzqqDpi-LR72NFNWLOyd0Z8Gasa2rmAUY1f-ZuUzNJnWkMKn03Ia3Mf-yhJ1IaM5yEMCwOGz9sqttVEgalCkN8Ik3JMbCGPZo3PMj83ZRuguKz21WUp23UYvekweNk4_PqImJpLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوتبالی: دانیال ایری امروز ظهر در ساختمان باشگاه پرسپولیس حاضر میشه و قرارداد پنج ساله خودشو با پرسپولیس امضا میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/138393" target="_blank">📅 10:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138392">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
🔴
🔴
ادعای فنونی‌زاده: قرارداد خلیلی با پرسپولیس 20 میلیارد تومان است!
💬
برای رفتن پیشکسوتان به باشگاه هیچ هماهنگی نباید بشود/ دوربین دارند و ما را می‌بینند/ من، بهروز سلطانی، مجتبی محرمی و چند نفر دیگر رفتیم و گفتیم ما در زمان رضا درویش استعدادیاب باشگاه بودیم و شاید خلیلی برای همین می‌گوید که ما سهم می‌خواهیم/ حقوق ناچیزی می‌گرفتیم و در آن زمان 30 میلیون تومان حقوق می‌گرفتیم که مالیات از آن کم می‌شد و مجموعا نفری 27 میلیون تومان به ما حقوق می‌دادند/ محسن خلیلی 20 میلیارد تومان با پرسپولیس قرارداد دارد و 6 پست را هم تصاحب کرده است/ لگد زدن به در اتاق پیمان حدادی صحت ندارد/ پرسپولیس خانه دوم ما است/ در را آرام زدیم/ بلانسبت ما مگر حیوان هستیم که به در لگد بزنیم؟/ بهروز سلطانی دستانش مانند نان بربری است و دستان بزرگی دارد/ سلطانی از خلیلی پرسید چرا در را باز نمی‌کنید؟ خلیلی گفت دیر متوجه شدیم/ خلیلی با سلطانی بد صحبت کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138392" target="_blank">📅 09:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138391">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7e369898.mp4?token=GiRXRV4zaZvMBjyfyOHZFpA3Sai4K-YLy1-_1IXwHvKT3dYuAO7oBdV4-kFqhlBm5RZHXznl3Gr2XAWX9bT2VrnOcdb8QgjLxzvikbhzClLI4UqoarUgf3MyM980jyTi-YaOYp_RK1q0TFGPmRH2jUMuGWHKxQsZD86GfAWQxwS9GfHH3GsuYq_jToUR2ijcuXQUQ9P5WSJKGnB2QiIR4UqMEtTJKVaAO9njufHikZ1cofJ6u5V3aIYGCQ-JECVmfLMmduFboCbZGNhPCRXnL3JplPAvsj9eXg69mmsHn_m5e7bxLD9tThaRDswItXe3h5BIfyyXC3xrngPPOdYRZoUhQyj53YLJRdnIht3DpYmboZ4T1sZy7RTlE9M89XoqgW0QgJSj4sv0lSr7oS4TK3B-ebH_8SSazLBWoBsha0WoYrsR3ww3m6_D7Kjyu7eRRFhdJNxRVC8C1RiA-MjPPd_6X79IT7tIoMXoqqnccFSOhpohwNEZEoY_Db37G-hkL3nVvgUDN8LlTo8SvEA2VoyH0cjKt56TJE2hBUJtGjSDdlNb9YauIuYKaRK_1a6fVdFioj-WZoJU3nj2pHNWVc8eWeXuDJsGuque5NT8Tq56VDLdGTHeVOgpZGmd9wE8mkUEXHbG8X9kGKU5tz_wOs3xnNMdWcru1_FXd6JTO6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7e369898.mp4?token=GiRXRV4zaZvMBjyfyOHZFpA3Sai4K-YLy1-_1IXwHvKT3dYuAO7oBdV4-kFqhlBm5RZHXznl3Gr2XAWX9bT2VrnOcdb8QgjLxzvikbhzClLI4UqoarUgf3MyM980jyTi-YaOYp_RK1q0TFGPmRH2jUMuGWHKxQsZD86GfAWQxwS9GfHH3GsuYq_jToUR2ijcuXQUQ9P5WSJKGnB2QiIR4UqMEtTJKVaAO9njufHikZ1cofJ6u5V3aIYGCQ-JECVmfLMmduFboCbZGNhPCRXnL3JplPAvsj9eXg69mmsHn_m5e7bxLD9tThaRDswItXe3h5BIfyyXC3xrngPPOdYRZoUhQyj53YLJRdnIht3DpYmboZ4T1sZy7RTlE9M89XoqgW0QgJSj4sv0lSr7oS4TK3B-ebH_8SSazLBWoBsha0WoYrsR3ww3m6_D7Kjyu7eRRFhdJNxRVC8C1RiA-MjPPd_6X79IT7tIoMXoqqnccFSOhpohwNEZEoY_Db37G-hkL3nVvgUDN8LlTo8SvEA2VoyH0cjKt56TJE2hBUJtGjSDdlNb9YauIuYKaRK_1a6fVdFioj-WZoJU3nj2pHNWVc8eWeXuDJsGuque5NT8Tq56VDLdGTHeVOgpZGmd9wE8mkUEXHbG8X9kGKU5tz_wOs3xnNMdWcru1_FXd6JTO6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔴
🔴
فنونی‌زاده: محسن خلیلی در حدی نیست که در مورد پیشکسوت‌های پرسپولیس صحبت کند
💬
به جان نوه‌ام و سه فرزندی که دارم ماجرای لگد زدن به در اتاق پیمان حدادی درست نیست/ محسن خلیلی در حدی نیست که بخواهد در مورد پیشکسوتان پرسپولیس صحبت کند/ محسن خلیلی سایپایی است و نه پرسپولیسی/ محسن خلیلی را حتی در کارخانه سایپا هم راه نمی‌دهند/ محسن خلیلی آکادمی پرسپولیس را در اختیار داشت اما حسن خان‌محمدی را اخراج کرد با اینکه خان‌محمدی قهرمان شده بود/ خان‌محمدی برخی مسایل را به رضا درویش منتقل کرده بود/ خلیلی بگوید چرا درویش او را اخراج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138391" target="_blank">📅 09:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138390">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
🔴
🔴
فنونی‌زاده: کنعانی‌زادگان هنوز هم شلوغ‌بازی‌های خودش را دارد
💬
در لیگ برتر بازی آسان وجود ندارد/ می‌خواهم به مردم آبادان هم تبریک بگویم زیرا صنعت‌نفت آبادان به لیگ برتر برگشته است/ حسین ابرقویی می‌تواند دفاع کنار هم باشد/ محمدحسین کنعانی‌زادگان واقعا خوب بازی کرد و تیم را هم به خوبی هدایت کرد اما همچنان یکم شلوغ‌بازی دارد/ کنعانی باید قدر بازوبند را بداند/ با حضور دانیال ایری، خط دفاع پرسپولیس خیلی مستحکم می‌شود/ شاید پرسپولیس در یک‌بازی 5 دفاعه بازی کند و حضور مدافعان متعدد به تیم کمک می‌کند/ مدعی‌های قهرمانی زیاد هستند و پرسپولیس یک‌امتیاز هم نباید از دست بدهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/138390" target="_blank">📅 09:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138389">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328262c761.mp4?token=DfhBtGsS13RtLAtjEOTAQXmnNu_q5-ePpTiNdUYzzqPVDICd2Bi2EtEx54B1YG07MABLdIWkNLgGkHi70cOlbb6hK9IH2_Qk7YsjIlnAKGdVEcIO2SxATxsQrI_Pdz-yYAhpN_KZC7_1rHYLjsp6oCr8p32YbztbHpyKAFJMOCuinqBkGr6k9YYq7TcfJQ5_JP0of6SwEcgLIWtOr_x0yHvWVCqattgHlxgedx49LXlBdjBvQo2kB6KT4UQzp0lIvXJc1LYKejLTANUixc4Ewd6KiHnfAFfyfc8ZWsZY2Qt0b34fkbzxXOeI_GD8zZcjmg1KdSZaVTmsZcHqM1CP3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328262c761.mp4?token=DfhBtGsS13RtLAtjEOTAQXmnNu_q5-ePpTiNdUYzzqPVDICd2Bi2EtEx54B1YG07MABLdIWkNLgGkHi70cOlbb6hK9IH2_Qk7YsjIlnAKGdVEcIO2SxATxsQrI_Pdz-yYAhpN_KZC7_1rHYLjsp6oCr8p32YbztbHpyKAFJMOCuinqBkGr6k9YYq7TcfJQ5_JP0of6SwEcgLIWtOr_x0yHvWVCqattgHlxgedx49LXlBdjBvQo2kB6KT4UQzp0lIvXJc1LYKejLTANUixc4Ewd6KiHnfAFfyfc8ZWsZY2Qt0b34fkbzxXOeI_GD8zZcjmg1KdSZaVTmsZcHqM1CP3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔴
🔴
فنونی‌زاده: محمدمهدی زارع مثل جوانی‌های من است!
💬
پرسپولیس بازی نسبتا خوبی را انجام داد/ همه بازیکنان جوان عملکرد خوبی داشتند و به نظرم محمدمهدی زارع از همه بهتر بود/ زارع دقیقا مثل جوانی‌های من فوتبال بازی می‌کند/ او کم‌اشتباه است، زیر توپ نمی‌زند و ضربه سر هم خوب می‌زند/ این قول را به هواداران می‌دهم که محمدمهدی زارع 10 سال در تیم ملی و پرسپولیس می‌تواند بازی کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138389" target="_blank">📅 09:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138388">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba104efaf.mp4?token=Q1-RVPLnKj0tPcz1xHTdACRsLcrsqNybGlxZUkx41ebAu3ENLlhoNguffR1BsovvxkGpsFA1tglncV2p9Sb2D9yl0DQdFNbDhruBO7xD5HxNpk9sWTXztTL7BMTQrCFDOsukBXCmXqE2DdnsTf85C-xX6YUiPgiFmNSuWu8XDn0uhmCS4D2wmUMLz61Sbhm6DGHwhdrRMrNhVd00k3OEItsKjZY5CfsDmQvVkcXLmrMUQI5KfZR8ILVDcdCFskjM19GNSWWdO2d-AOxl-HW9eBSE3QD89zb84FJblkJZrRP01dcl8gbiW1h2bOIDfOFkQK9A1SWoULD0fjtE96nm4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba104efaf.mp4?token=Q1-RVPLnKj0tPcz1xHTdACRsLcrsqNybGlxZUkx41ebAu3ENLlhoNguffR1BsovvxkGpsFA1tglncV2p9Sb2D9yl0DQdFNbDhruBO7xD5HxNpk9sWTXztTL7BMTQrCFDOsukBXCmXqE2DdnsTf85C-xX6YUiPgiFmNSuWu8XDn0uhmCS4D2wmUMLz61Sbhm6DGHwhdrRMrNhVd00k3OEItsKjZY5CfsDmQvVkcXLmrMUQI5KfZR8ILVDcdCFskjM19GNSWWdO2d-AOxl-HW9eBSE3QD89zb84FJblkJZrRP01dcl8gbiW1h2bOIDfOFkQK9A1SWoULD0fjtE96nm4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔴
🔴
فنونی‌زاده: پرسپولیس باید از گل‌های خود محافظت می‌کرد
💬
پرسپولیس باید از گل‌های خود محافظت می‌کرد/ فکر کنم مهدی تارتار قدیمی‌ترین سرمربی فعلی لیگ برتر است/ بازی تدافعی هم واقعا هنر است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/138388" target="_blank">📅 09:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138387">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f5fa4ac23.mp4?token=u_5BBRX0RBV4Sh_xi3-NcfjnN03ZNME-kFrhfUMnbRwQDCVC_4-2vgUKEq6ENCHbADzRXsu82XtbQPdNF955DctnsNFuBBt0SHXE6jJw6_63jeN2ShLE_Rd9XGDP8dwpXW--gktppiEPy5rowcPCInu6H3rPVoB_buTfiO83pbry1jmqsxkWx1lHGRz8HumHhN0cm7-9M2wh2XS2yIV80Dy3H2SOgvoEdo4-GR5mhfPFGc5JNu8lqKxgEpUgBNi1mculvkXfzORr1ef0UIvQ1SDiy-7CNR_8T4gEnxD7rd778V9OQOXzI0J1QxPXbeK32j6Wt3jZyXhdbrnjaQn4Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f5fa4ac23.mp4?token=u_5BBRX0RBV4Sh_xi3-NcfjnN03ZNME-kFrhfUMnbRwQDCVC_4-2vgUKEq6ENCHbADzRXsu82XtbQPdNF955DctnsNFuBBt0SHXE6jJw6_63jeN2ShLE_Rd9XGDP8dwpXW--gktppiEPy5rowcPCInu6H3rPVoB_buTfiO83pbry1jmqsxkWx1lHGRz8HumHhN0cm7-9M2wh2XS2yIV80Dy3H2SOgvoEdo4-GR5mhfPFGc5JNu8lqKxgEpUgBNi1mculvkXfzORr1ef0UIvQ1SDiy-7CNR_8T4gEnxD7rd778V9OQOXzI0J1QxPXbeK32j6Wt3jZyXhdbrnjaQn4Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔴
🔴
فنونی‌زاده: پرسپولیسِ تارتار در دقایق ابتدایی شبیه به پرسپولیس دهه 60 بود!
💬
به جان نوه‌ام فکر کردم پرسپولیس در دقایق ابتدایی، پرسپولیس دهه 60 است و واقعا به مهدی تارتار تبریک می‌گویم/ چند نکته منفی هم وجود داشت/ پرسپولیس دو گل زد و دو گل هم نزد/ شمس‌آذر تیم بسیار خوبی است و همیشه پرسپولیس را اذیت کرده است/ پرسپولیس در نیمه دوم به دفاع رفت/ سه امتیاز را عشق است و همین کافی بود/ دلم می‌خواهد بازی هجومی باشد و اصلا 5 بر 4 به سود پرسپولیس تمام شود و هواداران لذت ببرند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138387" target="_blank">📅 09:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138386">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFNhXxcxS5jHWyeSzV73o6SWxYvpstZfSfYD6ypEPjoIUKUb2V-Xx-8RTgCN_oXHYOxDM0A4gQ4bDNS12RXuUPAbFXakQHE0_9VgFltPvX71STrvy22wEtYqzOwUZVfB4LMJEaFRBik7BELJkhxQPE6xy5LlUeqBx60Lkpw1xsEwA6ky_QfpJOV1pVZY3X4SlQZFt9X4QdXpdtuS5VY-cFs-nXDwwI8Eje_OjXshO4VpPoZXwnNt4VtGB6d9304eT9HsKBNJPftev5dn1OwzCCnDOMZf0_k0vQt31xbygO_GzAGGUaU0OPi4htoYVMzkJV8owK9CKidHI9JPcbFLog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138386" target="_blank">📅 08:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138385">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZGTp4SD3PvZEORRXAcYBJcVNrCGI8whjEVpzqba49MmPzzZSPiuJg-XAhP-sX6Sri6aLtIG2XEGu1wuGLsLwbpmLBCyo6Qla02ESLAXqxIJY_dymollUr3Asgmj_FOPLMdyH_zcaSasmvc3rkHTTPRrdIKHpe44v8fyzvOxO0UHsL2WrwoYmqja2223cNIUlsosvsJ2dE6GE8LO8GGm_IpWvq-TLgB7yIBVMh3XS0iQUa_yuZRJWp1i-Zih4lDt6bh-5GAd6BW7GEPkGSeYDYeLxDF1EkxHg5i-Bd8l6IZxjow2A4lQrKCM-KvslCEbcKaRRXkeEO3YKveUgjmAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎰
هیجان واقعی همراه با ماشین
اسلات
اسپورت نود
⚡️
کازینو آنلاین
اسپورت‌نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/138385" target="_blank">📅 01:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138384">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">💢
💢
💢
🚨
مدیرای باشگاه میگن که نقل و انتقالات با جذب محمد قربانی تموم میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/SorkhTimes/138384" target="_blank">📅 00:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138383">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
باشگاه تصمیم گرفت از رفتار اورونوف چشم‌پوشی کنه و حاشیه رو ادامه نده/ایران‌ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/138383" target="_blank">📅 00:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138382">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔽
🔼
بازیکنی که امروز اصلا بازیش به چشمم نیومد عیدی بود، بنظرم باشگاه باید با جدیت سراغ رامین رضاییان بره…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/SorkhTimes/138382" target="_blank">📅 00:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138381">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
فاکس نیوز: تفاهم‌نامه ۶٠ روزه بین آمریکا و ایران تا چند لحظاتی دیگر منقضی می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/SorkhTimes/138381" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138380">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1875da2c0.mp4?token=eq3i6Rg016dRAJ6p3-OtTvX5BLLF8fh2KAaSk3_RGMILgJFnqt7RQzFDlk66NcVCLbsY6qNj-QlXCC0h3etyzI-NEEKaomUEi6A8t7WHBcZYO00mNrnk0rdseB-H7RcQ0nuEXu0zFZ-yQMpJKLzaZhGi1j-vopI8bC7VuZc2I5PzcEv_wWKyXgOfRjBbKsP-W-EuvNFYs_3UoNiWo288I_e1_hJMmBKqpoLFAvrFmh0lNAYUOeuVylZmHTI4G_op-BU_fJE00W1TE--pPO9tT1uTsimmo0mr2eIhcJYiK5AQEQyJAolXxUN1APpbPC_bL8udWuqQaHknyloDjlduLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1875da2c0.mp4?token=eq3i6Rg016dRAJ6p3-OtTvX5BLLF8fh2KAaSk3_RGMILgJFnqt7RQzFDlk66NcVCLbsY6qNj-QlXCC0h3etyzI-NEEKaomUEi6A8t7WHBcZYO00mNrnk0rdseB-H7RcQ0nuEXu0zFZ-yQMpJKLzaZhGi1j-vopI8bC7VuZc2I5PzcEv_wWKyXgOfRjBbKsP-W-EuvNFYs_3UoNiWo288I_e1_hJMmBKqpoLFAvrFmh0lNAYUOeuVylZmHTI4G_op-BU_fJE00W1TE--pPO9tT1uTsimmo0mr2eIhcJYiK5AQEQyJAolXxUN1APpbPC_bL8udWuqQaHknyloDjlduLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آنالیز فنی بازی شمس‌آذر- پرسپولیس توسط محمد تقوی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/SorkhTimes/138380" target="_blank">📅 00:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138379">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
برنامه هفته دوم لیگ برتر  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/138379" target="_blank">📅 00:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138378">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
ارونوف تو تمرین امروز سرحال و قبراق شرکت کرد
📸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/138378" target="_blank">📅 23:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138377">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
پیمان حدادی : امیر جعفری دفاع چپ گل گهر در لیست خرید ما نیست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/138377" target="_blank">📅 23:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138376">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
افتاد ساعت ۲۰ که هوادار قشنگ بره برای تشویق و ورزشگاه و پرکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/138376" target="_blank">📅 23:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138375">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
✅
مشاور قالیباف اعلام کرد: با تصمیم سران قوا، گرانی بنزین منتفی شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138375" target="_blank">📅 23:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138374">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
هفته دوم لیگ برتر خلیج فارس
❌
• پرسپولیس استقلال خوزستان
⏰
• چهارشنبه ساعت 20:00
🏟
ورزشگاه شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/138374" target="_blank">📅 23:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138373">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
برنامه هفته دوم لیگ برتر  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138373" target="_blank">📅 23:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138372">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYg75ksOm_VieZ-l4_zLzDH8ZtkeIUy1qDoeuC_KckVKaGZmON-7q0PaBVwp74ykjzyaTGvTHs--qB1Mqvx4TRAQL85Tk1vDKuY0rZgFjIjsNVfCE3kkgwswVy4LOdHhK_3cBDQM_NMzItCRMAn9VsqebHGmfrFdAeC6_t_OCPIJrHsLId6RhYWGu3jS0I0DLu6CNouKUkRIKThILWw-LwzKPKOvIU2ScHshiiWw-RaY7frWnh8-zt-rPFUS4zUgtT0A2F_OfgFrf2RuMnql2Qe8vzb0QYuro2IaGoKyv6eNwt8IXGGowx6MaOEnzOgUBUpLzF52NIwne0BEK26MjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
پرسپولیس و تراکتور همچنان پیگیر جذب محمد قربانی هستند اما الوحده امارات جواب مشخصی هنوز نداده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/138372" target="_blank">📅 22:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138371">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
✅
تنها 30 ساعت به پایان ضرب الاجل 60 روزه ترامپ برای توافق با ایران باقی مونده و هنوز نه صحبتی از تمدید آتش بس هست نه مذاکره و توافق.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/138371" target="_blank">📅 22:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138370">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_rfR7nt2Z2SJfkDdG4sSiFznhwmXEYYqflVBG49_Iqm8TpnQhbg4fdq5_QSfCNWE_mLsuV64tBQR4rtcmZ_u5GkCFF6eKffAsgpaTHW1XvIAUOJ__YGi5ZOCVB7ZJyPYr09S2ci03hxldy79VPvRnqFw6d8GTAqMt3cYBLkOm33x7M52fIg6vkuPBpFD1OzWHs-pqW3VM-CoLhcQm1UqE1RKWot-LMg_ulRg2lGmyJ6lpKoT-M3fHx_dWAZ5yKgeEWn1uo049MW53-BAuFPMvEC5_ZHrlAeyH_PPXZa31WKfBw7KjQrAXoOj1wwdRF0PudfbTJ4D-Oh_bKYhtl8sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آقای تارتار اگه کل فصل تیمت مثل نیمه اول بازی دیروز باشه و تماشاگر پسند بازی کنیم و نتایج لازم رو بگیریم، اعتراف میکنیم که حق با تو بوده و ما اشتباه میکردیم می‌گفتیم تارتار نیاد، فقط خارجی...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/138370" target="_blank">📅 22:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138369">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKC5MXOIEUoKe4wOxGgkCT3dwyzJ6EoRhulHnrip-1pUZalAGu8JjiJZEmrjvENvAGA2X-oljcXogMHv5s7FAM0olY7vbvIpdcqO-s4ffYa7q9M8VnGmODsVL4ZOjWnUgU21wEdnsxRkCHZYX3m71lSs9RrUCtNsE5cRa61eoNSdPyKLJ_YGkpO3yMZ2zgZvNN-ngo0NnH72Y8NvfiZ99YPPBmDbA2UjpxOtLoXuRlAoF88gc_-Vo5u5K5qUBtGqvqjfaPADZqMOQE2V_fVukWo2hBTn2B7n-HePq6LriVjwlpk8EbaO2GHLDrHAh8tofxG7IkzeaPZgwEiEjz8WLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارونوف تو تمرین امروز سرحال و قبراق شرکت کرد
📸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138369" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138368">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_1G7IAzy551pUqK_Ur_oxHBTsCxqPDOYoAsyev-qD-3iHqulbWg9_CYAK2DDmY8U8XDvjpDwQcdL-ht9EUre_iol60antbEZJHQUDL6CpSsmVjKcy2U59FPA6QDkfyIIm_1M3poLq2rAUp9_D2BdvdsP4OcLT_Iim1fa5JFL6wpt37HGFABKiULxzoWf7iHsUGu3KpUvAjwbhA9QjvUaRbOImnK7pFQAZr8nr2sp2WkuUYT8PK6khGpX2MxSEPIjBBiO88hq9dkyMz0DcgRF5Gwm5hlb3A6CETPq1URpNX7z4W6sOMPCoX_xquMTcWlPbuI8CXjL0hjn5Tk-IiFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138368" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138367">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS-1Crd609nsByg-vrF7P710VsBq9RVCPpgBWBROvGoExjCpoPAAGUfw68rWttkIZ9D-xJMpdSfswgvh-3EfVvM54Pf6V6lyMxThE5lPUwPWlB0m6eW9OP6tAHgzqdXFJG7Zv310-oRst9DCDEBHDCESZVhsbaEbAJR_ssQbpkEKISY3T5u0YPUGP2U3KCeJ63Q7jY1jWRqka1hshxDheWWRD73cZ1dmwgJBMiD3KzY-lKMc8RGVew8idilaNIy41AvXA_3HCjazZA0NOSaL8SILHCMHBYeXR6zQaBngQN_f7v2A4y4g83I0wd7Ur2A7LpUKfPdv67eCfyt1pB5WsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚽️
✔️
پیام نیازمند با 3 تا سیو موقعیت و ثبت کلین شیت بهترین دروازه‌بان هفته اول لیگ شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/138367" target="_blank">📅 21:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138366">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇵🇹
نشریه رکورد پرتغال : محمدجواد حسین نژاد در آستانه انتقال به ریو آوه قرار دارد
💵
مبلغ انتقال : 1/4 میلیون یورو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138366" target="_blank">📅 21:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138363">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پست ۶ : عنایت زاده پورعلی لطیفی فر پست ۸ : باکیچ خدابنده لو پست ۱۰ : یاسین سلمانی  واقعا هافبکامون ضعیف هستن</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/138363" target="_blank">📅 20:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138362">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🤑
در عربستان پول پارو کرد!
🇸🇦
کریستیانو رونالدو از زمان پیوستن به تیم النصر، مبلغ شگفت‌انگیز 625 میلیون یورو به عنوان حقوق و پاداش کسب کرده است.
😇
فوق ستاره پرتغالی در کمتر از چهار سال، ثروتی بی‌سابقه به دست آورده و او را به فوتبالیستی تبدیل کرد که بیشترین…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138362" target="_blank">📅 20:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138361">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMilad Gh</strong></div>
<div class="tg-text">پست ۶ : عنایت زاده پورعلی لطیفی فر
پست ۸ : باکیچ خدابنده لو
پست ۱۰ : یاسین سلمانی
واقعا هافبکامون ضعیف هستن</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138361" target="_blank">📅 20:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138360">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">همینا ک میگن پورعلی خوب بود  کافیه دیشب بازی با دقت دیده باشن  چند صحنه به راحتی تیم شمس آذر در موقعیت شوت قرار گرفت  چند بار توپ ازش عبور کرد کنعانی پوشش داد  یه بار هم از گوشه چپ تیم یه دریبل خیلی مسخره از ممی زاده خورد شانس آوردیم گل نخوریم   پورعلی و امثال…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138360" target="_blank">📅 20:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138359">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from♤</strong></div>
<div class="tg-text">همینا ک میگن پورعلی خوب بود
کافیه دیشب بازی با دقت دیده باشن
چند صحنه به راحتی تیم شمس آذر در موقعیت شوت قرار گرفت
چند بار توپ ازش عبور کرد کنعانی پوشش داد
یه بار هم از گوشه چپ تیم یه دریبل خیلی مسخره از ممی زاده خورد شانس آوردیم گل نخوریم
پورعلی و امثال پورعلی خیلی شاهکار باشند بهتر از سرلک هستند
ما بازیکنی میخوایم ک یه وزنه باشه فشار از رو دفاع برداره ن اینکه دفاع سوتیاشو جم کنه!!!</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138359" target="_blank">📅 20:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138358">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ما کی به بازیکنای اکادمی خودمون اعتماد کردیم و ضرر کردیم؟؟ پاسخ روشنه هیچوخ  نمونش امیر رضا رفیعی،عمری،محمودی مطمئنا اگه تو پست های دیگه هم اعتماد بشه نیازی نیس بریم منت کشی بازیکنای دیگه محمد قربانی ها و حسین نژاد ها خوبن اما به  وقتش با قیمت درستش</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/138358" target="_blank">📅 20:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138356">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
❌
هاشم نژاد مصدوم است و احتمالا به پرسپولیس هم نخواهد رسید
❌
ترابی هم با این مصدومیت احتمالا بازی پرسپولیس از دست میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138356" target="_blank">📅 20:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138355">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">ما کی به بازیکنای اکادمی خودمون اعتماد کردیم و ضرر کردیم؟؟ پاسخ روشنه هیچوخ
نمونش امیر رضا رفیعی،عمری،محمودی مطمئنا اگه تو پست های دیگه هم اعتماد بشه نیازی نیس بریم منت کشی بازیکنای دیگه محمد قربانی ها و حسین نژاد ها خوبن اما به  وقتش با قیمت درستش</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/138355" target="_blank">📅 20:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138354">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">➕
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
➕
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
🔗
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/138354" target="_blank">📅 20:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138353">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚽️
قربانی رو بگیرن ولی با همون ۵۰۰ هزار دلاری که گفتن میدیم به اروپایی ها نه ۱.۲ میلیون دلار، اصلا شما بگو ۷۰۰ تا
اخه ۱۲۰۰ ؟
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/138353" target="_blank">📅 20:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138352">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">باکیچ بدبخت هافبک پست ۸ هست یبار نشد اونجا بازیش بدن ببینیم چیکارس ، پاس های خط شکن خوبی میده خوب تکل میزنه</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/138352" target="_blank">📅 20:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138351">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmd</strong></div>
<div class="tg-text">خدایی باکیچ قبل مصدومیت عالی بود</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138351" target="_blank">📅 20:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138350">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چراغی تو همینی نیستی میگفتی باکیچ میشه رهبر خط هافبک چیشده ؟ وژدانن به جز اون گل رو به ترتر زد دیگه چه کاری انجام داد؟</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/138350" target="_blank">📅 20:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمد</strong></div>
<div class="tg-text">چراغی تو همینی نیستی میگفتی باکیچ میشه رهبر خط هافبک چیشده ؟
وژدانن به جز اون گل رو به ترتر زد دیگه چه کاری انجام داد؟</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/138348" target="_blank">📅 20:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommilaad zd</strong></div>
<div class="tg-text">برای اولین بار شاید باهات موافق باشم چراغی ..کسایی قربانی قربانی میکنن دو تا بازی ازش ندیدن این پول خرج حسین نژاد میشد مشکلی نداشت تلنت خفن و نیاز تیم به یک توپ گران قربانی نهایتا ورژن جوون تره باکیچ هست در کل هم تیم به پلی میکر احتیاج داره (جایگزین سروش رفیعی) تا یه سنترال هافبک</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/138347" target="_blank">📅 20:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran Jan</strong></div>
<div class="tg-text">کاملآ منطقی فرمودید
نرخ برخی  بازیکن ها را هواداران زیاد میکنند با فشاری که به باشگاهاشون وارد می‌کنند</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/138346" target="_blank">📅 20:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138345">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">#نظر_شخصی
💬
حوصله بحث با این بچه مچه هارو ندارم،عقل ندارن واقعا یه عده راحتن
‼️
خلاصه خزعبلات شون: از جیب تو میخاد بره، به تو چه، به قربانی ندیم به کی بدیم،پس چطور استقلال برای سحرخیزان ۲ میلیون دلار داد.
‼️
از قدیم گفتن عقل که نباشه جان در عذابه، اولا از…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/138345" target="_blank">📅 20:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138343">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">#نظر_شخصی
💬
حوصله بحث با این بچه مچه هارو ندارم،عقل ندارن واقعا یه عده راحتن
‼️
خلاصه خزعبلات شون: از جیب تو میخاد بره، به تو چه، به قربانی ندیم به کی بدیم،پس چطور استقلال برای سحرخیزان ۲ میلیون دلار داد.
‼️
از قدیم گفتن عقل که نباشه جان در عذابه، اولا از جیب من نمیره از جیب مردمم میره شما برو تو کوچه خیابون بگو از سرمایه مملکت میخایم اینقدر هزینه کنیم ۹۹ درصد مردم میرینن تو حلقت؛ دوما من هم علمش رو دارم هم اطلاعات شو هم تجربه شو در این زمینه،من نظرمو‌ میگم هرکسی سلیقش فرق داره اجباری در کار نبوده عضو کانال بنده بشه؛ سوما اگر یکی بخاد گوه بخوره با اینکه میدونه داره گوه میخوره بلا نسبت جمع شما با علم بر اینکه داری گوه میخوری این کارو‌انجام میدی؟! خیر استقلالی ها هم دارن چوب اشتباهات شون میخورن و کلی تو سازمان بازرسی علیه شون پرونده سازی شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138343" target="_blank">📅 20:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138340">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
✅
احضار اورونوف به کمیته انضباطی تکذیب شد و او امروز تو تمرین پرسپولیس شرکت میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/138340" target="_blank">📅 19:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138339">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIman</strong></div>
<div class="tg-text">پورعلی
لطیفی فرد
باکیچ
عنایت زاده
سلمانی
خدابنده لو
مگه یه تیم چند تا هافبک وسط میخواد؟</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/138339" target="_blank">📅 19:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138338">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">اصلا طرف ورژن ضعیف احمد نور هم نیست نه توانایی گردش توپ داره نه اونقدری شوت زنه تنها چیزی که تو این ۲ سال ازش من دیدم میاد رو کرنر ضربه سر میزنه توپ گل میشه
اگه با ۸۰۰ تا قبول نکردن باشگاه باید فرهان جعفری رو وایسه تا نیم فصل بگیره</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/138338" target="_blank">📅 19:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138337">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSCORPION</strong></div>
<div class="tg-text">تیم اینهمه هافبک دفاعی داره اینو براچی بگیریم خب</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/138337" target="_blank">📅 19:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138336">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSCORPION</strong></div>
<div class="tg-text">بازیکن معمولیو چرا انقدر میدن؟</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/138336" target="_blank">📅 19:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138335">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">#شفاف_سازی
⛔️
👀
دارن تا دسته میکنن تو کونمون با احترام، مندیت اروپای قربانی دست رضا مصطفایی ایجنت پیام نیازمنده؛ عددی که الوحده اعلام کرده برای صدور رضایت نامه محمد قربانی 500 هزار دلاره برای باشگاه های اروپایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138335" target="_blank">📅 19:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138334">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
🚨
مبلغ رضایت نامه الوحده یک میلیون و دویست اعلام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138334" target="_blank">📅 19:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138332">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
✅
⏳
10 روز تا پایان پنجره نقل‌وانتقالات تابستانی فوتبال ایران باقی مانده است.
❌
❌
پس از بسته‌شدن پنجره، باشگاه‌ها تنها امکان جذب حداکثر 3 بازیکن آزاد را خواهند داشت. بنابراین روزهای پایانی می‌تواند برای تکمیل فهرست تیم‌ها بسیار تعیین‌کننده باشد.  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138332" target="_blank">📅 18:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138331">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138331" target="_blank">📅 18:07 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
