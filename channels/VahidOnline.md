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
<img src="https://cdn1.telesco.pe/file/HMT-U8covYXy3tpq-y0ZG0a4MB3FCs62JSJJ_V1bC06Ii8XpqMtBTW7ECc2fahsncCcSTkgK9bTb9DmrEtOt4uWfdnUTcNw6pE_Pw1BUgbPO-9Yqyx02VlSZPCph6vibGB3j2rpR0-LWK6fF2dhIaaIn1PFPkfHlFsVakzpyzk_ll1cbWpqStZD00zckmMd4erphxOwkHDV-2RDu7B7_YvSn7Cn7qL2p-_TUSARns-9lc1KC7Zpu-U_pvlUngi3ifoP_xzVb8q5v5jvgVGufPdAopAgj7fynslCf_KrCez8wNfS0twIzmi5zdG9NkFTb14Q6-07pBDOaMHgdPpXy2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 17:39:47</div>
<hr>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V-P_gDvnq04fdrhMCvSt-KOV3kFu3aO_50Me4UhzwjDGIwZylc6v6aaSOOvV6cmIw6PnqFYGJxSiNPIj2EREnZbfHelm89ILnosMBMXfC4RrYlzJbxlDsX4PPc967fQ3R24WS5L3wrFob6DlATu8iuNJy_qxRlr-YKKF12W_KNoBwFah2V47j6Dj1t_ZHengYG0i7he4FRlYMecL04C4fQCZfcj-TteJVqJ4PNZ4rj0dKEIeOUL1Mzeo_78i6W1o_prA68sx2kcTak3ckCq-4a1qM6VgUKmq2Y6MY3BQAJmP_9yYHJc6FtF13qCHhD_QRIJ4cLJz6G4jAi1JJYyPEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vu5CnyLcuLL-CzUGNORBrhMr9aLPz3WHleKOljVeXuUMaaGgs8AmXMwtUy-HbhqElSFFyFVc-edOLMCJ3JgrwtLyfpuEz8A1lQd0jrhmQUnPqY7ZqSv6bo95wfRkleMiecu_VpQd7lKxU_OMG9apqPVmi0s3XWrj_CUXB9b1E2i2hrd7QsF41dsyDBK-rWR0C4hj9dWZCa1U_hfQcVoXczpwlt8diJXIJa1UlFFtg_cCO4a_dckiO_O_VCL6q5DAp8hFv2aN6CBHU3N4ZppPWyTWJYeRs7YLTslapGi8Xktg1CgoWDpz7Qv8fLJy7A2TfkWcegsJnS7bRUxiCkgPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GLCbzzhAQrWO_qBrJK6nGyHuY9f_UE3hQDX3Hz7r4ikd7J7T2oARGOTw1Cj1q3U7Bbg-aqxDmH5YCQ9uGkLRPzobmqayrXRIu7eHzd0XnuL6DoDDkHcWe0ddE8ZFclazelbO95IE2U8kG0Vz08XqcUzNVE74vqPrfEY9lPxdZPh-bwpa32Rpj-ctT2-zqzALk3bSvvaWFyLFC74VSmbyQTz-gTNceYUZxFSlcBkJXK_JwAqlh0wm6qtb0t0kORFpFtJ4XyvoTjJPCajbr1ZMRWfOKb3XlEKcMhFM2qn3Z102cHt-5umCWR-LrR4QYCc_AuVQDvGsUMWS6DUSm9jFsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UlB4-9vf2e-2TfGmBmwe4z1gVQZcrZIzGjlyJybenvxiAmzTMJN-f1pwgcC0PQqwGZ6barOJy93knVfAI4cGANMEY1Ly99zAUxb1ErNyAFcD37FRKZbTNFjGOUIhv74bCKlJYgQUjE8lX4amSQZ0B-tPx7jBM2ESP5bnekkGGdrsFMGba9Sh2eWgrRArbxd8cvAdgQb_-DnFbaWJZUz2VDw1o5QnRKYPmwLAOwON6XKOEogxTuRTU2oHCDZ5Db4f05oQSi5ACHYSR3HMYy-OlE5MvXiXyG6wyY9jqkHiqx5EAwNCSJpx7X3N2qw_aZTUzovBAV_ZL4oRliwEJFoBBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قوه قضائیه ایران یک زندانی دیگر به نام احسان افرشته را به اتهام «جاسوسی» برای اسرائیل اعدام کرد.
میزان‌نیوز نوشته که افراشته که «در نپال توسط موساد آموزش دیده بود و اطلاعات حساس کشور را به اسرائیل می‌فروخت»، بامداد چهارشنبه ۲۳ اردیبهشت اعدام شد.
در بخشی از گزارش بدون اشاره به جزئیات آمده که او «به عنوان کارشناس سایبری در یک شرکت وابسته نهاد نظامی مشغول به فعالیت» بود.
با این حال در گزارش مفصلی که ارگان رسمی دستگاه قضایی ایران درباره این زندانی منتشر کرده، مشخص نیست که او چه زمانی بازداشت و دادگاهی شده و از جزئیات روند محاکمهٔ او نیز اطلاعاتی منتشر نکرده است.
شماری از وب‌سایت‌ها و نهادهای حقوق بشری نوشته‌اند که احسان افرشته، متولد سال ۱۳۷۲ و فارغ‌التحصیل کارشناسی ارشد مهندسی عمران و متخصص شبکه، اوایل سال ۱۴۰۳ پس از بازگشت از ترکیه بازداشت شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/75439" target="_blank">📅 08:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bsF7u_naagB1G0Qv2GQTHoPSLRWlSMcP5vro5Uwme_5Cu2lTaHXl9URR76NV_NI2QVa07JUs79PplxctJeurSTyUu0sAedy_meyb_ow9GY-tXJeeRZJ8ZLK_-PH8VXJUpEss0SI0HJYjDpszlIqVyRFokOJIpLgIwGQwsP3pKyLFuwtjrDEQIS_hWFnrvXlBwOfed6MB_eE5O2mNGqGiRjhhqdiJbsPf7CFnVFRLMotPfmtIyY62pmHeLYaW8DW5cnaGDc8qz1guj0C-hVnA8v597SRF6oTO9DnanT9nN-N8fVgpsctYUX1SiXNqLzT2QhfZJZY5l6p6PGInurjN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه چهارم۰۰:۳۳
پیام‌های دریافتی:
دوباره لرزید  شرق همین الان 12:33
بازم اومد ولی ریزتر از قبلی
همین الان دوباره لرزید (نارمک ) ۰۰:۳۳
من الان دوباره لرزیدم
وحیددد نزدیک چهاربار تو پردیس
#زلزله
اومد نمیدونی تختم چجوری میلرزید
آپدیت: تصویر دریافتی بالا و متن رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
بزرگی: ۳.۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان وقوع: ۳۲ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۱۰ کیلومتر
🔹
نزدیک‌ترین شهرها:
۱۰ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۱ کیلومتری تهران
۷۶ کیلومتری كرج
🔄
آپدیت ۳:۳۰
پیام‌های دریافتی درباره لرزش پنجم
زلزله دوباره
ساعت ۳:۳۳ شرق تهران باز زلزله اومد
پردیس،۵ دقیقه پیش برای پنجمین بار زلزله اومد وحید جان سابقه نداشته تا حالا خیلی مشکوکه
ساعت ۳:۳۵
پردیس دوباره لرزید سه و نیم
سلام وحید جان
ساعت ۳.۵ باز زمین لرزه اومد پردیس، با صدایی شبیه به ترکیدن
🔄
آپدیت: لرزش ششم ساعت ۵:۵۷
یه کوچولو دیگه زلزله سمت پردیس حس شد الان
و الان هم دوباره لرزید
٥:٥٧ دوباره پس لرزه اما خفيف تر
آقا وحید ساعت ۵:۵۵ دقیقه صبح، پردیس برای ششمین بار لرزش احساس شد
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75438" target="_blank">📅 00:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">زمین‌لرزه دیگری به بزرگی ۴
این میشه سومین بار ظرف چند ساعت گذشته! اولین باردر شرق استان احساس شد و پیام‌ها از پردیس و بومهن و دماوند بود و یکی هم از لواسان]
پیام‌های دریافتی لرزش سوم:
تهران مجددا لرزید
دوباره لرزید کمی خفیف‌تر
وحید جان دوباره لرزیدیم  شرق تهران .. ۲۷
دوباره! پس لرزه بود.
دوباره هم اومد ولی ضعیف بود خوشبختانه
وحید جان شاید باورت نشه اما سومیش هم همین الان اومد، منتها خیلی کوتاه و کم بود...
ان، زلزله، ۰۰:۲۷
باز اومد، کوتاه، شاید پس لرزه باشه
دوباره اومد
یعنی اون رفت این برگشت
دوباره زلزله اومد
باز هم لرزش ۱۲:۲۷
سلام بازم لرزید حدود دو سه دقیقه پیش طوفانم هست خدا رحم کنه تو این شرایط فقط بلایای طبیعی کم داریم
اینجا ازگل، ۱۲:۲۷دقیقه، دوباره لرزید
🔄
رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
🔹
بزرگی: ۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان: ۲۶ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۸ کیلومتر
🔹
نزدیک‌ترین شهرها:
۹ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۰ کیلومتری تهران
۷۶ کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75437" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vjKNgPAwlYF9qwR2oHbJDVuyTqFlSy3pwU8t6Aass2MvrHntbdxkMD7Kwc1VA8XsKgrpmNgbG25Ju_7XYPLVsc7Vn4er1A-gBl2GY_DXNkulBwzLllSgt0_g821Wql6P_ohbmeMYjhnesADA3mYcLqmLGwS3Z0TdlLtVbBrpzTgJjIDN-KtoAomrFhXHmPh9KJfzYGIOdHPfV80aRE17toYn5g2kEgKWeC9wl4UJRkrsX6MS7Ebo_LLcZwZcZQIXtSQpi9VUbdcqL_t5Z-8DciBEw-PyWNxO1hoQleLV3dd30y5psQW6FH_7su2h4xXYoaNMF62Gf3RxfpkPrqZ4-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی «رسانه‌های جعلی» می‌گویند دشمن ایرانی از نظر نظامی در برابر ما عملکرد خوبی دارد، این عملاً خیانت است؛ چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آن‌ها به دشمن کمک و از او حمایت می‌کنند! تنها نتیجه‌اش این است که به ایران امیدی واهی می‌دهد؛ در حالی که اصلاً نباید چنین امیدی وجود داشته باشد. این‌ها بزدل‌های آمریکایی هستند که علیه کشور خودمان طرف می‌گیرند.
ایران ۱۵۹ کشتی در نیروی دریایی خود داشت؛ تک‌تک آن کشتی‌ها اکنون در کف دریا آرمیده‌اند. آن‌ها دیگر نیروی دریایی ندارند، نیروی هوایی‌شان از بین رفته، تمام فناوری‌شان نابود شده، «رهبران»شان دیگر در میان ما نیستند، و کشورشان یک فاجعه اقتصادی است.
فقط بازنده‌ها، ناسپاس‌ها و احمق‌ها می‌توانند علیه آمریکا استدلالی مطرح کنند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75436" target="_blank">📅 23:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">"وحید تهران لرزید"
+ ده‌ها پیام دریافتی مشابه درباره احساس لرزش زمین در مناطق مختلف تهران
به نظر می‌رسه بیشتر پیام‌ها از سمت شرق و شمال شرق تهران هستند گرچه در غرب شهر هم کاملا حس شده.
حدود سه ساعت پیش هم در شرق استان تهران حوالی پردیس و بومهن و دماوند زمین‌‌لرزه خفیف‌تری حس شده بود و غیر از اون مناطق فقط یک پیام از لواسان داشتم و پیامی از خود تهران نداشتم.
🔄
رسانه‌های داخلی:
زمین‌لرزه‌ای به بزرگی ۴.۶  ساعت ۲۳:۴۶ امشب مرز استان‌های تهران و مازندران را لرزاند.
این زلزله در حوالی شهر پردیس و در عمق ۱۰ کیلومتری زمین به وقوع پیوسته و در بخش‌هایی از پایتخت نیز احساس شده است.
بزرگی: 4.6
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
طول جغرافیایی: 51.83
عرض جغرافیایی: 35.82
عمق زمین‌لرزه: 10 کیلومتر
نزدیک‌ترین شهرها:
8 کیلومتری پرديس (تهران)
10 کیلومتری بومهن (تهران)
11 کیلومتری رودهن (تهران)
نزدیکترین مراکز استان:
41 کیلومتری تهران
77 کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75435" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bBawosfea_rE_PcnONrVfak1oCCCGmmbAuxNYcKMORQXNltgKYXA6Qoc5zGySzFoJWVjXm5Tu1StPnar7CbJiwKU16utyZ_Lo7RpoD2Gg9GXQr-9ZNmgI1-fFhZmVQJRq3FK6cNnw2SHrHwOun5MYlZTFn_ImKdtP7wISqev0fr3ZuwHnfl-WspdNcMCDfRS8GAj1fgTnGFe5Ejcz7s8RqBE2vhsUXE7OrMOB6vV3ht0GFT8op6sbzUf5vpH69hqT5pZP4d9n9wTLjl-vnVYkJDc4k0McPV4nK2WUuvCByPcbm5dWhL1GexsxruX00RvfCPOpkHbWDfmFXEUwx_ziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=cd1r0KQL9hHwFmCf5a9cVf7Oto2t6oRC1gAPfNgAtRwbAPow84e-Zf5ugK8wVj8OsClMU4lnDanEV1UlzxZLQ4JNNFF1tfhNpCP9AazgDd11hgy24RH52b3W8X8qIVD5oQPg3uskdyM9HjLI4quwW8RfoPoB5vHZKP8YehDk-63rVYi1uGQFsr55am9jQwQogOEHUKZhdkOMsVIMDYfSCVMxkUJuXdZ2wLuL_4SBfUaSN9CzSHCVUjfWahSncfCvA1Pzc5ETUgw_ezf6mAgOKBi_wYikhTofjwVJ8iorPltyByEHww11EHMSO6Ojn9fAwtJh68ipf-6u9jQ0u8GYIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=cd1r0KQL9hHwFmCf5a9cVf7Oto2t6oRC1gAPfNgAtRwbAPow84e-Zf5ugK8wVj8OsClMU4lnDanEV1UlzxZLQ4JNNFF1tfhNpCP9AazgDd11hgy24RH52b3W8X8qIVD5oQPg3uskdyM9HjLI4quwW8RfoPoB5vHZKP8YehDk-63rVYi1uGQFsr55am9jQwQogOEHUKZhdkOMsVIMDYfSCVMxkUJuXdZ2wLuL_4SBfUaSN9CzSHCVUjfWahSncfCvA1Pzc5ETUgw_ezf6mAgOKBi_wYikhTofjwVJ8iorPltyByEHww11EHMSO6Ojn9fAwtJh68ipf-6u9jQ0u8GYIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: خواهیم دید چه خواهد شد
دونالد ترامپ، رئیس‌جمهور آمریکا، پیش از سفر به پکن گفت که رئیس‌جمهور چین درباره جنگ ایران «نسبتاً خوب» عمل کرده است، اما واشینگتن به کمک او نیازی ندارد.
او روز سه شنبه در جمع خبرنگاران افزود که قرار است با شی جین‌پینگ «گفت‌وگویی طولانی» درباره ایران داشته باشد.
ترامپ تصریح کرد: «فکر نمی‌کنم ما به هیچ کمکی درباره ایران نیاز داشته باشیم. ما به هر شکلی که باشد پیروز خواهیم شد. یا به‌صورت مسالمت‌آمیز پیروز می‌شویم یا به شکل دیگری.»
رئیس‌جمهور آمریکا با اشاره به این که توان نظامی ایران در جنگ اخیر از بین رفته است، هشدار داد: ««ایران یا کار درست را انجام خواهد داد یا ما کار را تمام خواهیم کرد.»
او به جزئیات بیشتری درباره این هشدار اشاره نکرد، اما این اظهارات در حالی است که ترامپ پیشنهاد آخر ایران برای توافق پایان جنگ را در روزهای اخیر رد کرده و آن را «کاملا غیر قابل قبول» و «فوق‌العاده ضعیف» خوانده است.
رئیس‌جمهور آمریکا قرار است چهارشنبه برای دیداری رسمی وارد پایتخت چین شود. این سفر که قرار بود در ماه مارس انجام شود، به دلیل درگیری نظامی آمریکا و اسرائیل با ایران چند هفته به تأخیر افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75433" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZSdYI19yH98-TNBLYS5nyTeFyjXCV3_Y3fUr2LQGvvKm7juliOSeEGn8N_Dg5OhFWpD5gBIJqQlb_TCT_QvrsbK2C3ffzEmBycEp2O_8RvWfSAk-3TeJriw_JHPQLb2PQQnNSAtViXPYolkrXJiuZ3Vm75haLnRAgF3WoUUsgjw5AA9yiR_H-TYOz526r6-LROT_-KkRPvO3vGGx-bj-G0x-gPGD-7PSQ3neEWgcvUH14I31U6dK6nouVW7gmenQFUQRmXWeICpK_lS2xR8LlsjU8tN40XUd6sVvslNCU500JgmbQOHHB7y3V4jV1ObHG0_PjPxIZreNeuWvhVR6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با برنامه رادیویی «سید رازبرگ» گفت: انتظار داریم اقتصاد ایران زیر فشارهای ناشی از محاصره بنادرش فرو بپاشد.
او افزود این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.
ترامپ گفت ایالات متحده در حال انجام ارتباطات مستقیم با مقام‌های تهران است و برای رسیدن به توافق عجله‌ای ندارد و او اطمینان دارد که تهران غنی‌سازی اورانیوم را به‌طور کامل متوقف خواهد کرد.
@
VahidOOnLine
دونالد ترامپ گفت حکومت ایران با انزاویی روبه‌روست که آن را از منابع درآمدش محروم می‌کند و انتظار می‌رود اقتصاد ایران زیر فشارهای ناشی از محاصره بندرها دچار فروپاشی شود.
او افزود: «این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.»
دونالد ترامپ درباره اورانیوم غنی‌شده در ایران گفت مقام‌های جمهوری اسلامی به او گفته‌اند قرار است آنچه او «گردوغبار هسته‌ای» می‌نامد در اختیار آمریکا قرار گیرد، اما بعدا نظرشان را تغییر داده‌اند. او تاکید کرد در نهایت این مواد را به دست خواهند آورد و موضوع را جمع‌وجور می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75432" target="_blank">📅 17:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75431">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmhNoHaEik-Ll5juwD9o9NUVUp4WpfijvOhKH4aJbjs8-tGSlkv4TYLgndufHaqDia9OnJqpI5XGd3B6amU9KkdsMfyBWGhGgR5oWGvvDbKQo0LDqOkGkihVtDfe0zxOkCT-W-KduDV9Qsm0ysxev7zE56wvbfOsPKpdV3DoqZ7zDHAFqp5hMfHw0c7PsVG0H1xYwyqAGUn4HXVZPPiM7CjfiOkRcglZMV8C7lVThNVNTVeFeb9xMYddWjHQR2yEgtkchMMae5ZuXfd_SToG4eA2FzApWqtZDi9lipwMtU5t-m8W3Jy-zF0si0JKA9noUzw5yXklbNVNK7tt_Wmzvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد پنتاگون روز سه‌شنبه ۲۲ اردیبهشت اعلام کرد که جنگ ایالات متحده با ایران تاکنون ۲۹ میلیارد دلار هزینه داشته است، رقمی که نسبت به برآورد ارائه‌شده در اواخر ماه گذشته، چهار میلیارد دلار افزایش نشان می‌دهد.
به گزارش خبرگزاری رویترز، در حالی که تنها شش ماه تا انتخابات میان‌دوره‌ای کنگره آمریکا باقی مانده است، دموکرات‌ها در نظرسنجی‌های عمومی موقعیت بهتری پیدا کرده‌اند و تلاش می‌کنند این جنگ را به مسائل مربوط به هزینه‌های زندگی پیوند بزنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/75431" target="_blank">📅 17:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jyFL5x3nEMqh6laN9MhPbqP9ZnkCIkX-DdCfzUuwyfnUDf3iEWb58TRuF-oWNGHWEFX4rHJ6rXq9bGEZur7jYMnAFn_lRDynfOaiy2pEMUitcsfwXbA4IHPA64Onxy88eYfRp0wjx4w7KQwzmvSfivhNP8nlvDkoPgw-DR08btNsD_4iZ088QSP27zoiUcdd7JvS74pfQdrwTVkX-TK3BbbZ2F6MxprmKIYJ6Ta-5NSM8rqvCkC_E6dG9WpbogJfsSAM-W7K26DNsYyPc2xS_x89o2jcqs_7Vt6IXGzVjUvAkcj5pJA3Z0GEy3wJn_5G9jg19cqYx0GY7xmf1vc47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه در تروث سوشال دو تصویر گرافیکی منتشر کرد که صحنه‌هایی از حمله به پهپادها و قایق‌های جمهوری اسلامی را نشان می‌دهد.
در یکی از این تصاویر، یک ناو آمریکایی با استفاده از سلاح لیزری یک پهپاد جمهوری اسلامی را هدف قرار داده و نابود می‌کند. در تصویر دیگر، یک پهپاد آمریکایی دو قایق جمهوری اسلامی را هدف قرار داده و منهدم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/75430" target="_blank">📅 16:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75429">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=bETg-71rr9YsJVwujxHqd2UlBmGf_Ujo9HyLIy7UvLgJd2C4anoI1Rx_jtJ4sxsow6rG1vjs-q3TVVt1B3MdxvArrzGLdul8DVbkGNtCY9guqSYjHL-CCEu2GC96yX-nTY-JkTtdIfUbjisw4yNpmoFlZllO6lbyMB_2flc8DhM4WZgXr-Dy4IW33QoVMmt3FUI4N3TZ5hsYivPXW6fmgoYhPM24Pw6FNuoolPGKV9fF0HnaNIj-R1Jf4rdfZhApB_OE3zdATFxABhZAR0ATBMAZtftsGBlIPEg80jgjHrKh7Cpqo_80NwNlKfEATo12NezstCQosHYZeIdM0UCuhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=bETg-71rr9YsJVwujxHqd2UlBmGf_Ujo9HyLIy7UvLgJd2C4anoI1Rx_jtJ4sxsow6rG1vjs-q3TVVt1B3MdxvArrzGLdul8DVbkGNtCY9guqSYjHL-CCEu2GC96yX-nTY-JkTtdIfUbjisw4yNpmoFlZllO6lbyMB_2flc8DhM4WZgXr-Dy4IW33QoVMmt3FUI4N3TZ5hsYivPXW6fmgoYhPM24Pw6FNuoolPGKV9fF0HnaNIj-R1Jf4rdfZhApB_OE3zdATFxABhZAR0ATBMAZtftsGBlIPEg80jgjHrKh7Cpqo_80NwNlKfEATo12NezstCQosHYZeIdM0UCuhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری سخنگوی دولت مسعود پزشکیان روز سه‌شنبه ۲۲ اردیبهشت به دلیل وضعیت اینترنت به بگومگوی خبرنگاران با فاطمه مهاجرانی منجر شد.
سخنگوی دولت تاکید کرد که «اینترنت پرو» با مصوبه شورای عالی امنیت ملی که ریاست آن را مسعود پزشکیان بر عهده دارد،‌ مورد استفاده قرار می‌گیرد.
او در عین حال تاکید کرد که این اینترنت ویژه کسب و کارها است. [در حالیکه خیلی از مردم بدون کسب و کار هم پیامک گرفتند بیاید پرو بخرید]
@
VahidHeadline
فاطمه مهاجرانی گفت با توجه به وضعیت جنگی، فعلا اینترنت عمومی وصل نخواهد شد.
مهاجرانی در پاسخ به پرسش‌های متعدد خبرنگاران درباره وضعیت اینترنت و به‌ویژه «اینترنت پرو» گفت ما در وضعیت جنگی هستیم. رئیس جمهوری به‌عنوان رئیس شورای عالی امنیت ملی پیگیر حقوق مردم است اما وضعیت جنگی است و بعد از پایان شرایط ویژه، اینترنت به‌حالت قبل بازخواهد گشت.»
پس از این سخنان، چند خبرنگار تلاش کردند تا با یادآوری تعهدات دولت پیگیر وضعیت وصل اینترنت شوند. مهاجرانی خطاب به آن‌ها گفت: «وقتی رئیس جمهوری آمریکا می‌گوید آتش‌بس به تنفس مصنوعی وصل است، انتظار شما چیست؟»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت جمهوری اسلامی، با اشاره به قطعی طولانی‌مدت اینترنت در ایران گفت اینترنت حق مردم است و عصبانیت مردم کاملا درست است. اما در ادامه تاکید کرد: «عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود.»
او افزود: «رسانه‌ها کمک کنند که این ادبیات را جا بیندازند. دولت طرفدار دسترسی آزاد است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/75429" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SpvzjGlgh6a3D27-04Gs-BxDFL4hsiOg93_Cek46h8GsC_W6rvqE8isT8RB5OADdND7XXh_bVaEVMbJaCyfmcO7OBvWa971wtofpUyPqHkwi-ekJnalkpyIk352MlZkE9XZRKXk4mOZJV-LhpI1Tnrg1iHspBB2mP2JCrCbzwc9zblKCxpl5WPwkA0_D8UUZorMGa7S2sN7Y-m_-R_zdezqdM2a6_MfQRyOZh2dfQkep-GDdSe21cRVByhrSChppdLsfr-sKdWt5VGzJWgrYcQ_CkJw5FGDRrkOGUACc23J9kXKWRANGIwgqzcpCFKwvN07k_LlH8bRaijgL9dn9oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه از اجرای حکم اعدام یک زندانی دیگر به نام عبدالجلیل شه‌بخش در بامداد سه‌شنبه ۲۲ اردیبهشت خبر داد.
ارگان رسمی نهاد قضایی ایران، شه‌بخش را «تروریست آموزش‌دیده» گروه «انصارالفرقان» معرفی کرده است.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/75428" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75427">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBTOox00MylcFuPBXFLi2zeav7Qs4UTTgqytttSjTm_JripR_aFaQLYq-GUjJ3ITuSn4irFKc0X5cNMG-IVYAQM-eIRsOmS8UZKPAm6ZlWLhlYPZ3MA_S3Dv7z0whdQ_yv2X1eNrr6EWkEKS3Vr8NndMBjOXYFU70Yrsttk9RV3IU3n7S3i5q0T0ujDaRMAdEQ8PAMxrbED5AjrjbpQ9W5TZr5gAIwtxbFAnPj-_oZ4krCrGQHspNuSghx9I2ghF_JxAJpJk7C9g6s9oqnq8_AqeiMGTlY07H5EZHkCE_YnCO8nAG3IlobkEApi4shVvRMIneK5AbxzxkbvWhpO-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نشریه آمریکایی وال استریت ژورنال، امارات متحده عربی به‌طور مخفیانه حملات نظامی علیه ایران انجام داده است؛ موضوعی که به گفته منابع آگاه به این نشریه، می تواند امارات را به یکی از طرف‌های فعال مخاصمه با ایران مطرح کند.
منابع آگاه به وال استریت ژورنال گفته‌اند حملاتی که امارات تاکنون به‌صورت علنی تایید نکرده، شامل حمله به یک پالایشگاه در جزیره لاوان در خلیج فارس بوده است.
در اوایل آوریل گذشته و هم‌زمان با اعلام آتش‌بس از سوی دونالد ترامپ چند حمله هوایی به تاسیسات نفتی ایران در جزایر این کشور و اصطلاحا مناطق فلات قاره شرکت ملی نفت ایران صورت گرفت که باعث آتش‌سوزی گسترده و خروج بخش بزرگی از ظرفیت پالایشگاه لاوان از مدار برای چندین ماه شد.
ایران در آن زمان اعلام کرده بود این پالایشگاه در یک «حمله دشمن» هدف قرار گرفته و در پاسخ، موجی از حملات موشکی و پهپادی علیه امارات و کویت انجام داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75427" target="_blank">📅 03:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHusn0KlcVaAhkiFnfaS1oak5e2udiKTdM2gHgRyezzWOCEmU4x9wMeOac9X27w0pB2DJ33HXqzV6FumhLfe41hNjzZSyVb9AsJL-mMVRNDgGBLJB_CWW_RO0Z7wYnr9Ug95h8ablkysAdbsLNqdYqzNU2ZmOXuFWNljibLcFtee9pxTvloM1PLLcOyEf2hnlIStRDbT1Mydz5cjdmbnodZRQbDwpCoSviE9LmKLr6pA9clhtCAY4h4ttt-gCDl1HS3-fEWVm46gMmQH3wcmfpTTytXTelmUE9yxxqaVbnYz9l3jbE5QwEWtAGfgyRcKN97Nw4HYtTh3nUFKEFouKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده، روز دوشنبه، ۲۱ اردیبهشت‌ماه، در بیانیه‌ای رسمی اعلام کرد که پاسخ اخیر تهران به پیشنهاد دیپلماتیک واشنگتن، نه‌تنها از نظر سیاسی غیرقابل‌قبول است، بلکه با استانداردهای لازم برای لغو تحریم‌های مالی و اقتصادی نیز همخوانی ندارد.
این وزارتخانه تاکید کرد که رویکرد فعلی ایران مانع از هرگونه گشایش در مسیر مبادلات بین‌المللی و آزادسازی دارایی‌های بلوکه شده می‌شود و تا زمانی که تعهدات شفافی در حوزه برنامه هسته‌ای ارائه نشود، فشارها بر شبکه مالی این کشور ادامه خواهد یافت.
در همین راستا، اسکات بسنت، وزیر خزانه‌داری دولت دونالد ترامپ، در اکس با بازنشر این بیانیه، موضعی قاطعانه اتخاذ کرد.
او با اشاره به اینکه پاسخ تهران نشان‌دهنده عدم تمایل این کشور به همکاری واقعی است، نوشت: «در حالی که دولت ترامپ با حسن نیت مسیری برای دیپلماسی باز کرد، تهران با پاسخی کاملا غیرقابل‌قبول به میز مذاکره بازگشته است.» بسنت تاکید کرد که وزارت خزانه‌داری، سیاست‌های مالی را به گونه‌ای تنظیم خواهد کرد که جمهوری اسلامی متوجه شود عدم پذیرش توافق، هزینه‌های اقتصادی سنگین و غیرقابل‌جبرانی برای نظام پولی و بانکی این کشور به همراه خواهد داشت. او نوشت: «زمان آن رسیده که تهران متوجه شود هزینه لجاجت، فروپاشی کامل اقتصادی است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75426" target="_blank">📅 23:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PW72znyUiZ8wYUO55yn7qWjpuMaD0UNoXx4WNjvXxolsu6BhylimLDprGQSgHhpZai5jOXRrIIf_mZRSLtuCR8UyDC3KZizmgH1SE-WuBPWHTGqx9aaVcZD9KD2_eOkCOn3tsVmLPrODlEe4gY9OSjTDKKDtRYVpae37Lm70_anLdCKD_bjsdMlSdD0coKGxI4rLDwIKM2EpM1n9yP2_yfY_SWiR4FJmTpnp03UCt6QT2w5ivIFqXYs4MEcJt8fq0sq_RzOJ3Jgo1Ny6v50N4qIEj-6XMjE4UJhedQDVTeJzvT7JPpB3ZSBzqgeN5sJy0EUqu2rRGxgHDUDZTRK_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیات جمهوری اسلامی در مذاکرات با آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در شبکه اجتماعی اکس نوشت نیروهای مسلح جمهوری اسلامی آماده «پاسخگویی درس‌آموز» به هر تجاوزی هستند.
قالیباف نوشت: «استراتژی اشتباه و تصمیم‌های اشتباه همیشه نتیجه اشتباه خواهد داشت. همه دنیا قبلا این را فهمیده‌اند.»
او افزود: «ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75425" target="_blank">📅 22:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYtyCP3NbBysAiyRzrgCqmb9-zFLcMqYQX_i2kpt7ryoW0M9yn26tviomT_6j3eecOk1mSGdpNBoDqCG_vr_NagNdBZGTQwxyHuu6KO9fW9JoO_piV63ddWUxYOyPOde7NO3jyx3NKBXEmJr-wbm-Hyw0eaH98TKco8VFwG8kDrWW5WIMHrvsFvlek4AkpyxXv86FsAgZei5nB_WJ_KUrFBCzSF8D0iIvsGx3K3opk1wAP_0qWmuv3Ez788qvu_Rk8h4Oe5qqGHgxZjjpiKLNu-q7vXqSgqp3NfaE2rY493ImAPGlqH-opBFq9zh4tyJl7_R2VXK_YdvYqTtHvhy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس گزارش داد دونالد ترامپ روز دوشنبه روز دوشنبه ۲۱ اردیبهشت ۱۴۰۵ با اعضای تیم امنیت ملی خود درباره ادامه جنگ با ایران و احتمال ازسرگیری اقدام نظامی علیه جمهوری اسلامی جلسه برگزار می‌کند.
بر اساس این گزارش، سه مقام آمریکایی گفته‌اند مذاکرات میان تهران و واشنگتن روز یکشنبه به بن‌بست رسیده و همین موضوع گزینه نظامی را دوباره روی میز قرار داده است.
اکسیوس به نقل از مقام‌های آمریکایی نوشت ترامپ همچنان خواهان توافق برای پایان جنگ است، اما رد بسیاری از خواسته‌های آمریکا از سوی ایران و خودداری تهران از دادن امتیاز جدی درباره برنامه هسته‌ای، احتمال اقدام نظامی را افزایش داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75424" target="_blank">📅 22:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JFhxeBnX9l3a_8lQG3uLRh-wbucf8xnnsSc0IH-p8tdOVhZGEKbAHUx3sWiICW5vaeyESfylzYm7yMuMopX5tsEQG31Fk9AGHf33SUAMt7XUuLAFrcIXIwbdIawbzbcj0NGkpD4zO0QAQR3nWGGo3FTNSbAEsVpg2Y60CxdPiNkwnRr1kuvyW_OrORfgUAYSUqbKV5wGAeSoO_3yTJ3K52orx3pDfCpAIi6mlwrA0BEdGNuqBrWqY3JwxtzVZiSyZueoqcXDO5bkS4JAi-KS0fydJJPPUwnLFz3ZppBLbnVwV_JlyOFJwrSWTxwbRXUjtTOhwenwnTgZXnrY1GsvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AJJBmEMmSJc8qQadvczOqeuFd3wi4Zjcqb-oGGmTxwGRd-HZTduda-3qGAd4SF0GLqhA-5V4ESEd7zEw4YBbC2tf9_ST6QuFlNxQS4a06hgPnMGs1ZZImJDjxU5S_UdtmJGLE4I144zBtxPrrEvly9hrKTM9W8q1xw2taSpympaCWcOj7sxaT6g-CcNVmSayVdC1OEkkMTnnRpQGLGHxxPewJdF3qgXwgerHNPBW38IYuaX2GmgsGfYmN0KRmh1jUrXA8YeaaFTQlSZ7dR4xRKU1WngtNHbbfjS5K5VHq5el3TqopiMqcJitXdPmgTGfEO54EXL91rAfGIsbseRaSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eBLfoU9gLNdNqvA7JeItSQMEnC-gTi8fwXHDdDpW8RSMvSmaKaYNeZmaCWf_ZWJJA-XFwIMcXWBorsW2ZRKOkl0WuBjlECzA5v8DEZrNy0Ny-xQcH_dWgqi9MC6QOsaOi0KQUD0mmLYqDzizCFUCcVQHq1diVc1qJg8_DPAZNgE6N9O6u9CKndwUs9I9GqrE2JwHEYT99b2PJZhi04wwuo-VcoY_yoydWhZJ22hifCDhEKhWFdP2jxWWirBusBVJ5NGcHgeN6qXASnQCkdHMqjV6FiALECHb52Bat0ZOwmfhucnuSCNIQEh_oPcf6nVavel5xYfivnN0vuF3pzbjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UwpZdIavwOhKjHEqUcoeU3iq0M4fzv87oDJFEPXbVva2pn9BQ8z6s-gyF7z0QuodgttLhQTjAG-fCFfD9yE7-JKSUGqDUDXRllChGybjgmVQU63jS5PASAKd6rDZP9R72TIK1aCIPpCT-YTBFuFvxXX9Sxe6tI0uZeyRCnyNGMkGIjhHJh_OdjY0jYzwDq034T4XUoyVj4cGCr0pvqJdDVqXUJxEwMGpCMes3T_SH1-fsmcYvdyk0PAr0-rzr0SEk4J8futK2L8rBN73I1jlYL9Vp_OkMj6eTyow85JGEL2HH_927RLHTFg7dGwA0l7Y7PUvOLzLgLOGoPgdoutJAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی حدود ساعت ۱۹:۳۰ به همراه تصاویر بالا:
▪️
وحید الان برام پیغام اومده که من جان فدا هستم و ثبت نام کردم ولی خودم در جریان نیستم
😂
▪️
آقا یه اتفاق جالب افتاده. ظاهرا بعد از هک شدن دیتابیس جانفدا دوستان یه فکر بکر به سرشون زده.
من هیچ وقت در این کمپین ثبت نام نکردم ولی پیام زیر رو برام فرستادن. فکر کنم خودشون به صورت پیش فرض همه رو تو این کمپین عضو کردند، حالا هرکی جرات داره انصراف بده… البته نمیدونم انصراف داره یا نه.
▪️
امروز این پیام برای من اومده در شرایطی که من اصلا ثبت‌نام نکردم.
حتی برای پدر خانمم که فوت شده هم اومده.
▪️
امروز عصر واسه من این پیام اومده
در صورتی که من حتی تا حالا سایتشو هم باز نکردم
حالا یا خودشون دارن روی شماره هایی که از یک سایتی یا صنفی داشتن ثبت نام میکنن، یا اینکه یک ادم [...] واسه من فرم پر کرده یا اینکه مسیج الکی فرستادن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75420" target="_blank">📅 20:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nqovXvOAI9DexPaMXTcMITatM4IJ2p00dN4zG4enGOTaZqzqWGYibKl0EPE95xtlyoYMvjzoafgU_wB05Ytj9jsP4uXXDq-F-oOxIU-JGOidA460EjIgg6Va7IfDcMG9N1XvDsWRrJaC2jVzD2FFHT7uUmZzFYMCL-jeNratnyK_e8g7YbXNJ-0hAXUAUHER2Djh169RoeRcE_5AfLcSH7mNxVrDL-ucd8gPlAbfJhr6rSCejTrwyE7jf_a1C0gqoEQcsW49uGYTW6qTbqFE5mam0V03goR51_WbW8pN0iv8diY7fzlpk7RP-L1fx2udWyt1z_p3DLa6pYX6LZ8GgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/isEFtCj59w--CEzayGCTNj2QcY1UEF-Ms0au_9EimtSVz6Zpei1p-tj5nuZTPMWX45Zk0AiPPSvcI7bPf3JKB3s67OGvgQTr5vcpVf5Hb_JDdsJKHGdQ6ZgauyFm7yu3yYDMDWn3EkOli-pGzfGz17uojGrCbBfv1IPkXNL4q_VK8PE1ZivemQjqPU97ndnOvGfuLvzBxVzWRhs91OTGmUFCLq4huM-XpCsodHuphve7tRPxzWH5z3qlYC_j2JaLGnLSKxhDB3IjRoOVmH89YFsoRjxdkFhiodVinwmfO8WOeO2UburcpGaoFTSkHDMlO3iuAA536cG5b9DnFPa9wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QQ5bYB-Zr4S00N-ZorpFJLiXQp9zTCoIbAdCHhBY3SY4gZgPsEA6_RFSnHBTd8N_lzQeFshqwpB4PbC53s5h_KzqKNdEWqJV8rBT_sFvtFBmd5z_cntJnG4QxGWKJw5oS4ZudbF-YzDnw16Yw8RXsT8jE3WqR11u-XY-LFkOwdLvWyb19Eiutz0lANMNMYXVhimy1fiFfAWixKUX_HYab72_eWh9gEG1SNi6mpwdxdpn6HLO9lL-l6spLGB9Vk-1ek4IDeXW8rEv4fP0T2kmzi9ytk389Mn8qOI83oiXbjIoeITDN7mTgCnd3yaWyGp6xs_R5oMG2QbJvBgOagiL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LJZJ08G9NyuwOl73yu-iBNEu3BLblw_P9MDyGZ2F8_L5GfCsnGv9d64Pj3aZO5ia7NuwCWUxzoQZUFIiAokRmCcPBCmSoKGD7Rilb0paTT0syGN5qCxDqzHkwgZucvInfnG6k2obiuEEJ5et96g1_SrthpzB8ySXTe2aWbezSqrfQlJaxGGqtsdPsJq35CJboE2LV9r8twpEH6Ept4sBdXegIUlR09K8H3-jsVpFRdHYDGSr9VrbOkfCK637PZ6SO4giaC2aya4IylHRXpJIwfdH_Ey4sOtojahygh3wg78VPTxCETuEc_YrJ2ZBSk9CAlwv5onKqWJtyo4Icfyghg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=mE58JjvlLY_LctyZFVqG7xkLNyPOCpOMdb0Rzf3VB_2y8RVq19cOB0GGVtH5omgU7tmA7p5khfPN0aBgpdt0NRaQQrmUKOIX_KPJqsjSMYtOCYCek1dKd5YqKsgKAiMI8iwpU5NbhUX449ndUr5uZ-bnBRBP299I0EN3UiGNmEWlPIbNZZY1rYh1Byolr-0WF0qxfwle4ZP4GOk-i1L8vFCghnqpPJOeaNuAkcDffW0LXrnp0n8GN9LpoRNaD5FA0_JgO2nskZmq9X4_pQqmzV_LxiBljYdFlwClY3auJ402QcSngMvpva1S6L56rGMi7ZKjrF4972dls58ga__0Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=mE58JjvlLY_LctyZFVqG7xkLNyPOCpOMdb0Rzf3VB_2y8RVq19cOB0GGVtH5omgU7tmA7p5khfPN0aBgpdt0NRaQQrmUKOIX_KPJqsjSMYtOCYCek1dKd5YqKsgKAiMI8iwpU5NbhUX449ndUr5uZ-bnBRBP299I0EN3UiGNmEWlPIbNZZY1rYh1Byolr-0WF0qxfwle4ZP4GOk-i1L8vFCghnqpPJOeaNuAkcDffW0LXrnp0n8GN9LpoRNaD5FA0_JgO2nskZmq9X4_pQqmzV_LxiBljYdFlwClY3auJ402QcSngMvpva1S6L56rGMi7ZKjrF4972dls58ga__0Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت گفت پاسخ تهران به طرح پیشنهادی صلح آمریکا احمقانه بوده است و او از ادامه جنگ و فشار بر ایران خسته نمی‌شود.
ترامپ در یک برنامه عمومی در کاخ سفید و در پاسخ به پرسش‌های خبرنگاران درباره طولانی شدن مسدودیت تنگه هرمز گفت: «احمق‌ها نمی‌خواستند قبول کنند. فکر می‌کردند من خسته می‌شوم یا حوصله‌ام سر می‌رود یا تحت فشار قرار می‌گیرم اما هیچ فشاری وجود ندارد.  ما به یک پیروزی کامل خواهیم رسید.»
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت، در پاسخ به پرسش خبرنگاران درباره آنچه او تغییر رژیم در ایران خوانده بود گفت: «در ایران میانه‌رو و دیوانه‌ها را دارید. دیوانه‌ها می‌خواهند تا آخر بجنگند.»
رئیس جمهوری آمریکا گفت جنگ خیلی کوتاهی در پیش خواهد بود. ترامپ تاکید کرد که میانه‌روها در جمهوری اسلامی از دیوانه‌ها می‌ترسند.
دونالد ترامپ از پایان هفته سوم جنگ می‌گوید با توجه به کشته شدن دو صف اول رهبران جمهوری اسلامی، تغییر رژیم در ایران پیشاپیش روی داده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد که در حال بررسی دوباره «پروژه آزادی» در تنگه هرمز است، اما هنوز تصمیم نهایی درباره اجرای آن نگرفته است. او گفت هدایت کشتی‌ها توسط آمریکا در تنگه هرمز تنها بخش کوچکی از یک عملیات نظامی بزرگ‌تر خواهد بود.
ترامپ همچنین درباره مذاکرات با جمهوری اسلامی گفت: «حکومت تسلیم خواهد شد.»
او روز یکشنبه نیز اعلام کرده بود از پاسخ تهران به پیشنهاد آمریکا رضایت ندارد و آن را «کاملا غیرقابل قبول» توصیف کرده بود. همزمان صداوسیمای جمهوری اسلامی اعلام کرد پیشنهاد آمریکا رد شده، زیرا به گفته این رسانه، به معنی «تسلیم کامل رژیم ایران» بوده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، به فاکس‌نیوز گفت واشینگتن در حال بررسی ازسرگیری عملیاتی برای بازگشایی تنگه هرمز است.
او افزود واشینگتن فشار بر جمهوری اسلامی را تا زمان دستیابی به توافق ادامه خواهد داد.
ترامپ همچنین گفت هنوز تصمیم نهایی درباره ازسرگیری «پروژه آزادی» را نگرفته است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در گفتگو با سی‌بی‌اس نیوز درباره پاسخ اخیر تهران به پیشنهاد صلح آمریکا گفت جمهوری اسلامی در برنامه هسته‌ای خود امتیازاتی داده، اما این امتیازها «کافی نبوده» و پیشنهاد تهران همچنان «بسیار ضعیف و غیرقابل قبول» است.
@
VahidOOnLine
دونالد ترامپ در واکنش به اظهارات بنیامین نتانیاهو که گفته بود «هیچ‌کس پیش‌بینی کامل و دقیقی» درباره تنگه هرمز نداشت، گفت: «من داشتم. من می‌دانستم آن‌ها تنگه هرمز را بسته‌اند. این تنها سلاحی است که دارند.»
ترامپ افزود آمریکا می‌توانست در چارچوب «پروژه آزادی» این گذرگاه را باز کند و گفت این عملیات می‌تواند از سر گرفته شود و در آن صورت «بسیار شدیدتر» خواهد بود.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده یک روز پس از مخالفت با پاسخ پیشنهادی جمهوری اسلامی به طرح آمریکا برای پایان جنگ، به فاکس نیوز گفت که ایران فنآوری لازم برای بیرون کشیدن ذخایر اورانیوم غنی‌شده مدفون زیر خاک را ندارد.
ترامپ در این گفتگو تاکید کرد که اورانیوم غنی شده ایران آنچنان در اعماق خاک تاسیسات هسته‌ای دفن شده که آمریکا باید آن را خارج کند.
براساس آخرین گزارش‌های آژانس بین‌المللی انرژی اتمی، ایران دست‌کم ۴۶۰ کیلوگرم اورانیوم با غنای ۶۰ درصد دارد که گمان می‌رود در تاسیسات هسته‌ای اصفهان مدفون شده‌اند. این تاسیسات در جنگ ۱۲ روزه و جنگ اخیر اسرائیل و آمریکا بارها بمباران شدند.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده در اظهاراتی گفت: «مردم در [ایران] می‌خواهند به خیابان‌ها بروند. آن‌ها هیچ سلاحی ندارند، هیچ تفنگی ندارند.»
او ادامه داد: «فکر می‌کردیم کردها قرار است سلاح بدهند، اما آن‌ها ما را ناامید کردند. کردها فقط می‌گیرند، می‌گیرند، می‌گیرند. در کنگره هم درباره آن‌ها شهرت خوبی دارند و می‌گویند خیلی سخت می‌جنگند، اما نه، وقتی می‌جنگند که پول بگیرند.»
ترامپ گفت: «من از کردها خیلی ناامید شدم، اما ما برخی سلاح‌ها را با مهمات فرستادیم که قرار بود تحویل داده شود، اما آن‌ها آن را نگه داشتند. من گفتم آن‌ها آن را نگه می‌دارند، اما چه می‌دانم؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/75408" target="_blank">📅 20:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75406">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZQaE7oGU9DInqHVhtyp_2QovQaBr8-MwwUq0HszDrBAjap5bAx3YUmOEvr_qXqgHQim3T2AkMMn24chPe_eaNlmBSHuMUkusZjA54KvuQ9WM8vGcUuGOrgvTO8_-7X6Sdzf1hXp7j7C1fbPnKXEUwgm7wWhJZ68KGuxIY3wwHud6vEJeWfBsQguTj4wBXQFcTrSTHyWlgaQ8cDdjMZgeyCZ1AlsK6ycdSsD-D4bMsxyxRba0ZCt1Q5jMC7Q3Yd9cDGQDBetMA-0-17nGu4sCzrvrTDPBx-QiwfMy2Tgz48r_B8XG5bCneBEvgJZCiJv3Zp8KlTt4l9s87v-fE9T-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BKKchqd0-IIEhe31uHxfbH36joAYWhteLv2la21DZFSIwN7iO-uXE3mEfXUsx-1xDxiQNIQApRi0QEQ9DG_tg9oJ_4W0_L06bZQSwkthkIzWo4HAbCx871TuzUiH2MsjbTziesnhRQIapkeXM-swc_oSeBVyiRUHrAmt_RHCPQVnNR5f9k4clubGCLHvE6OyMQP2FGLSl0CbOM25Z2kdNkvX-lTFdyNVHJ2aW5E_Pcwonaj1Ah7ehf446Ye5Y8x0jaz-jngNvJ2_nq1KfF1aL4SkgSAhoVV_RUpEJTeGExoVNih3-HGlCzOC_PgZSuCUj2kSHEDa2dScW18UoGNqsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">AmirKh1982
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/75406" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قطع اینترنت نه تنها ربطی به تأمین امنیت زیرساخت‌ها ندارد، که «اقدام علیه امنیت ملی» است.
در ۷۲ روز گذشته میلیون‌ها گوشی، کامپیوتر و سرور ایرانی از صدها پچ امنیتی حیاتی محروم ماندند و در معرض انواع نفوذ و هک قرار گرفته‌اند.
در این
#رشتو
بخشی از این آپدیتها را مرور می‌کنم: @
hamedbd_channel
hamedbd
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75405" target="_blank">📅 18:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI2fT250iZiOAiX-MDRcoRJW4TXMktehfjV6lW4sZW99SKsrQ_cfa28vsfEWg69EyAdkRCww-tnYDnJLekTyQJE6f3otLYTM2vs5V72Tam2ao46M1WSFbDXxuhZjPuyyEBCZ9OYvnJ8r1StQfkS9inbyV57mHWLpzrO1rZm6UtDhKG2XJRDDgIZi2imRCSAT0X-ct_qtRn5_6sQFjXL2JWmaG36xvq-RZ2m5IsS6eZuBEBbvS8fYSI_EXN8BJh_mVIZrXD6gMZNQuWrxiCV4o0P7XpOjA90bWQD12us-mw1C4SnDhyoD-Eh-eVrGTu0S37-36dyVuDDN1l9c3VzzMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار روز دوشنبه ۲۱ اردیبهشت‌ماه در بازار آزاد تهران به ۱۸۲ هزار تومان افزایش یافت.
این جهش قیمت کم‌تر از یک روز پس از مخالفت شدید دونالد ترامپ، رئیس جمهوری آمریکا با پاسخ جمهوری اسلامی به طرح پیشنهادی آمریکا برای پایان جنگ روی می‌دهد.
علاوه بر پاسخ منفی ترامپ، بنیامین نتانیاهو هم اعلام کرد که کار اسرائیل با ایران هنوز تمام نشده و ذخایر اورانیوم باید از خاک ایران خارج شود. این اظهار نظرها احتمال برخورد نظامی دوباره را تشدید کرده است.
قیمت هر سکه طلا هم روز دوشنبه در بازار آزاد تهران به ۲۰۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75404" target="_blank">📅 18:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75402">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HaCNIdSwnEAAAbovL6PKyKxP4Mma4sTIGb-_F3yry7SbUFFQqRD_pRg1HSB7EkU6kPwzOD0aQvq6z2guR4yvj0m8rJAUDDhopYTpTyW0YnvMF9LUDGzjcXD2L51n2OwoxFAdpisuZwZjU67BVRdbscQpOXtXcPNRPDThR1-sVkVqts2eHu8KPm2m_a8Rz6M0xebosJwqayAaRtYE5YbikmLlNGoHSYl4Q_lAnoJbSK3MVRwFwcTM4vTDNwG20YfsltopggtdFcqTSfItViRXKHYgifaUO2koFYa9cEe0HrtprLSqXiSfk26XqtcAGCpdVi9AmTuKFfjh1pwJkL786w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fBUIDEnfQVsyhG9XEMtF5rGW1cIKvWKwW5do4YsS_aCifa2ORkJPqaBoYXpYFaKSARvMW2zI9cZtOWTn_0ktSE5uxA6ghWOkFtrXB68nnyQXT24OvqwqKogY5AznpPXycOGKBRwx5DswN1P_tsJwXFMsBn-T8hPpaj-C309qzQQbjPWAi0wC5Vah-JB3mU6QbQySfxNKtzFW6ESLg5NbzYp__d12rpRJEVp9xIl6ujWxgBmBC6beyj_yqb0GX7l7VKsWrij2mZ8M5-9oN1F9EYe311Wx8d6z-ruvryELqbSYgl6GVsolPHXpso_l-4t74P49013teGR9oYYdDSjLqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😋
💩
«محسن محمدی عراقی» معروف به «محسن اراکی»، عضو مجلس خبرگان رهبری، انتخاب «سید مجتبی خامنه‌ای» به عنوان رهبر سوم جمهوری اسلامی را «کاری الهی» توصیف کرد و مدعی شد در روند این انتخاب «دست هدایت امام زمان» را دیده است.
@
VahidHeadline
«ابوالفضل ظهره‌وند»، عضو کمیسیون امنیت ملی مجلس جمهوری اسلامی، مدعی شد حکومت ایران به ظرفیت‌ها و سلاح‌هایی دست پیدا کرده که «بمب اتم» در مقایسه با آن‌ها «ترقه» محسوب می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/75402" target="_blank">📅 18:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dsax45d2YzJwIyoJufc2GEgmd8B7aF7CeyE9Ll_f90vJoXqeAZLzxJKzXtEzzdEqpyx438lZwz5jzmrgIuwJBiN0A8HcpZsE4dZqxnq-QNcXEyW0gMDjrAKeI79JZCp20AOy_lsUR7qL47q40AVYk3Cwv-6zbc13EWahJdmg5m_OTO_l-iJt4wexMfm_TK-h_UqobVRO4p9N_MGVbmMx8khmHUkykkFP4enAxM14sRUyPykh-51_SaEAvCVG3NYon9f-mbulS-X7Epi7i4d_7hpRBu0sMzbWnbfurtSlk1mrHI51ExY2RC3uEipgHtMjcqFA4uTNTNTJPviOY0-2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UYy2QlZlqLZ00T-vttndZpZeHfxwUQhQHKLM-vSlK7AsTrR7F7E7vqTq5qWkYBxr5JgxptkRWWvsS4K-X3kSusvy9LoTiFaJPlr-EvGjuabX3h8Q62fRU5lNJ447SmK1yrhMqAoDlj6GzR68ppnvcPMb73fFVf4-HvWzgXj68KRVX1j-sjF3Ovn_qpbdS30er12iHJTB7rQBnBHhOdweIOKKjLD9P4nMQ4elaGQhjzZ8XdMXXsjHS_iLpb-rehzi566SAWQxBwvyY923tOPKrMUELnCISeggNMoFlBqxy_vdScQCxBdRIuygKtKbILc_2EtZbJsy7kDlVXK56aQD_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نخست‌وزیر بریتانیا تاکید کرد که از جنگ ایران حمایت نمی‌کند و افزود که شهروندان این کشور نگران افزایش قیمت بنزین و تاثیرات اقتصادی آن هستند.
کی‌یر استارمر تاکید کرد کشورهای دیگر می خواستند بریتانیا را جنگ ایران بکشانند اما او هرگز این کار را نخواهد کرد.
@
VahidOOnLine
دولت بریتانیا روز دوشنبه، ۲۱ اردیبهشت، ۱۲ فرد حقیقی و حقوقی مرتبط با حکومت ایران را تحریم کرد.
به گزارش خبرگزاری رویترز، این افراد به «مشارکت در اعمال خصمانه» علیه بریتانیا و چند کشور دیگر متهم شده‌اند.
در بیانیه رسمی دولت بریتانیا، از جمله این اعمال خصمانه به «طراحی حمله و ارائه خدمات مالی به گروه‌هایی که در پی بی‌ثبات کردن بریتانیا و دیگر کشورها هستند» اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/75400" target="_blank">📅 18:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7U_qxR8-Ly8FTliSq2ycB-CRabS3tCh1BEiktyZLlKl6vcIh0mCobw7WsCPO0n-gfWTsPpK1qK3CWw5DwDP7cled0cmoa2ZDaY4WQ8CrK75L6pCum3bnmkJXtYLfDpIWRR9O0UzpH_jDJAkeIuRltWyXnycArfZwphrbM9BWKGe6lXVT4PX2mQvHvCYonpVJw9DbQEt_4WxOxH-sQ1DeGszgRzsGMfXjDnzjPFa4M_L883lStdk5wVQhczSHZnEAUVPtO3ZY3VSjxGehgOkqPvwoFj_Qx-6574OH6vdPggv5jouvuSGF4kyhoMSsE8sGVrTKh8dacQVBy4btPW96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدعلی جعفری، فرمانده قرارگاه «بقیه‌الله» سپاه پاسداران، گفت: «تا زمانی که جنگ در همه جبهه‌ها پایان نیابد، تحریم‌ها برداشته نشود، پول‌های بلوکه‌شده آزاد نشود، خسارت‌های ناشی از جنگ جبران نشود و حق حاکمیت جمهوری اسلامی بر تنگه هرمز به رسمیت شناخته نشود، هیچ مذاکره دیگری در کار نیست.»
او افزود که با این سطح از بی‌اعتمادی به آمریکا، طبیعی است تیم مذاکره‌کننده با هدایت کلیت نظام، شروطی را مشخص کند که همه حقوق مسلم جمهوری اسلامی را تامین کند و این شروط «حداقل انتظارات» ما است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/75399" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a1CV6QrBH12Wpg-pow3QQcpAm-znOfLeQ6B3KxJL5hjofIXj2y9oBmn9k8aOydlkqTuTPnWdnfsTFC3e60xyzZzbaPqk2GhPOKoVnhEOAkzs3wcjDn5WZT3fznxM_Ddr3dvhvwZ2Bw18ZWCAjwJyq_x13wuH5aAlthHlmO3d37W7GTYht4Q3Xi8Ky6Q6LG11LdCw05CyzZXpb1xj3Dc3R7_DoAJo2l41G0o36n5kkcfG8wvzJfWyfP5HJMd2gbnc8IBbv_ee1KmulEmtc-g7pGH-Rz6DxOIJn78ULxg0fF6VCnkWFDlg6yUmc_J-LZ9RBp-P22hr9iWQ3YrXGybHcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RxHS9BR0fobo7PiOsPcLBGWklfiLNXo4I-GgC4ns46_8bovgKOhPBk4sDPhdhuXAT14QKNPnwzFdeX5Voo-F8UT7yiwMTS3BynRc1v2Jt1HluQhALbM0Lb_qyYVFyq91s3rlKM38Bx_6MYikOieo3kLvaPvfPE8hcDwbrH53-32cP8TIucBKiAsKXRaB_goyh5GYeEfwNhJMYeQLjByg6OI26XbrXKIMm34qNH5aoF0kWxCF6u08lT6l7Ar30I6dLQjm1pXhDHnKT2-6Z8xqi2Rf9hJkdS1n9DY9tPCJBBqASgjx_RgpIPEqD2RUnn5qyvjjE2eQc8bJRYtlYIrIpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=kXmsMCQwmMtx5V1sFJObDW4ssEVDyX7RrkdBnGJny1lmUf06VeySpugTnL-PJwkOL1FTNwOa9bUh1IwNaVwAuu-SPT9LWSuMYemgxnzENZwnU3q_0NtlooVRV57_2-hMXwCC7xJX4iP_JB23dwx-K60rG6Ln5yi2nLld4DhknFkXh3ZEW_B-6tWu_MWHK-t6iTnOsxLqj3lFHoBPn7dX3sF8T5THA_4mzXwDrQIt7n9C9sGLFLvvdI1p01bw1OvVxkmHDhhkzazMSj7UuN3Cnu-F3KNXamiO5to7cRyk_gyKhDPGpBgsUP8F0TElI3PeIAtjEbPZd8iwUK3aQHqc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=kXmsMCQwmMtx5V1sFJObDW4ssEVDyX7RrkdBnGJny1lmUf06VeySpugTnL-PJwkOL1FTNwOa9bUh1IwNaVwAuu-SPT9LWSuMYemgxnzENZwnU3q_0NtlooVRV57_2-hMXwCC7xJX4iP_JB23dwx-K60rG6Ln5yi2nLld4DhknFkXh3ZEW_B-6tWu_MWHK-t6iTnOsxLqj3lFHoBPn7dX3sF8T5THA_4mzXwDrQIt7n9C9sGLFLvvdI1p01bw1OvVxkmHDhhkzazMSj7UuN3Cnu-F3KNXamiO5to7cRyk_gyKhDPGpBgsUP8F0TElI3PeIAtjEbPZd8iwUK3aQHqc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، در نشست خبری روز دوشنبه ۲۱اردیبهشت۱۴۰۵ گفت در شرایط کنونی اولویت تهران «پایان جنگ» است و نه تصمیم‌گیری درباره آینده برنامه هسته‌ای یا ذخایر اورانیوم ایران.
او در بخشی از صحبت‌هایش بدون نام بردن از دولت یا فرد خاصی نیز گفت: «هنوز با کسانی که علیه ما تجاوز مرتکب شدند تسویه حساب نکرده‌ایم.»
بقایی در واکنش به اظهارات «ولادیمیر پوتین» درباره آمادگی روسیه برای انتقال ذخایر اورانیوم ایران گفت: «در مرحله کنونی تمرکز ما بر پایان جنگ است. این که بعدا در مورد موضوع هسته‌ای، مواد غنی شده ایران و مباحث مرتبط با غنی‌سازی چه تصمیمی گرفته شود و چه گزینه‌هایی را مد نظر قرار دهیم، موضوعاتی هستند که وقتی زمانش برسد حتما در موردش صحبت خواهیم کرد.»
او همچنین درباره روابط تهران و پکن گفت جمهوری اسلامی با چین «ارتباط مستمر» دارد و گفت: «چینی‌ها به خوبی از مواضع ما آگاه هستند.» بقایی مدعی شد چین نیز مانند جمهوری اسلامی، اقدامات آمریکا را بخشی از روند «تشدید یک‌جانبه‌گرایی» می‌داند.
سخنگوی وزارت خارجه جمهوری اسلامی در بخش دیگری از سخنانش، آمریکا را «بزرگترین تهدید کننده صلح و امنیت بین‌المللی» توصیف کرد و گفت: «جمهوری اسلامی ایران ثابت کرده قدرت مسوولیت‌پذیری در منطقه است. ما قلدر نیستیم، بلکه قلدر ستیز هستیم.»
اسماعیل بقایی با اشاره به حملات آمریکا و اسراییل علیه جمهوری اسلامی گفت: «حمله به یک کشور، از بین بردن زیرساخت‌های آن، ترور رهبر و شهروندان یک کشور، مصداق عمل مسئولانه نیست؟»
او همچنین در واکنش به انتقادهای «دونالد ترامپ» از طرح پیشنهادی جمهوری اسلامی، از مواضع تهران دفاع کرد و گفت: «ما امتیازی نخواستیم. تنها چیزی که مطالبه کردیم حقوق مشروع ایران است.»
بقایی در واکنش به صحبت‌های رییس جمهوری آمریکا گفت: «قضاوت را به مردم واگذار می‌کنم که آیا مطالبه ایران برای خاتمه جنگ در منطقه، توقف راهزنی دریایی علیه کشتی‌های ایران، آزاد شدن دارایی‌های متعلق به مردم ایران که سال‌هاست به ناحق محبوس شده، زیاده‌خواهانه است؟»
او همچنین گفت: «هر آنچه که ما در طرح پیشنهاد کردیم معقول و سخاوتمندانه بود و برای خیر منطقه و جهان است.»
سخنگوی وزارت خارجه همچنین مدعی شد که این وزارتخانه، از هر تصمیمی که از سوی نهادهای نظامی مانند سپاه پاسداران برای «تنگه هرمز» گرفته شود اطاعت می‌کند.
@
VahidHeadline
گزارش ایسنا:
isna.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/75396" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLhladzXUQmXELZrQJp_tVQ0uR0YrfPz2foZUUHWH13OdOCsO_FjjF62wkJQhzAM63n2NM6n9HQubmT3-vS0heurnLTa4KLJ3mNFIeWmLQH91JEZTQpWP8VUMfPvWCuCWWN9bmn7iyafo29uENnHxRmOfaA5mTZq770S5Iz1aQn72AjWJZQ2DWell44yoNnKhvNvmHoIt3c16yfAWUngQkpckdC_s_mgmCSL9i7tRZv5hqu7ytoaAgXZsGviCpBhCbXPDmvWRtfeVPGdhjLqf99rH2cDJtX_3y5wnA3dDl0N4glAVB_aadygGMgFwS6-3VaHrByrIpneB_CyORv65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار تصاویر ماهواره‌ای که نشان‌دهنده نشت احتمالی نفت در محدوده‌ای در نزدیکی جزیره خارگ است، سازمان حفاظت محیط زیست ایران می‌گوید: «منشا آلودگی مشاهده‌ شده در اطراف جزیره خارگ ناشی از تخلیه آب توازن آلوده یک نفتکش آسیب‌دیده بوده است.»
این نهاد گفت: «هیچ‌گونه نشت نفت از خطوط لوله، تاسیسات پایانه‌های نفتی و یا سکوهای متعلق به شرکت نفت فلات قاره ایران در جزیره خارگ مشاهده یا گزارش نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/VahidOnline/75395" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6eaJtwhMwQQ8w7wJ4iCgORHUaGi-s2Ll1krSdNhFt04U5TWk6mi4yxryS1t7BuofGuFVK8sIEYvMhqvCNrJxSZ4ytYNGZko78AL65hZk0afBDXhis-VzfVV0DISnbeRxBcrdjHsGvjDlnGn5oPcyGfuF9r9xGrGuhOATwRLZxU-zLDVq3AkqAeckFdpeBI9U_TUmb15IKA7LObcTgF9Gal3NYBNiU4uFZnHmqOS9ncu-7bvFcVgg91DRoobue4ErK4dFt0_a337S5CLvAp46NLkJK7WVthqn9w7oMyzYatgVpLMFCwoao8O6r9yJGYsPbA6j5absbL6fR7qMR8Fww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گزارش سی‌ان‌ان از اینترنت طبقاتی؛ «فکر کن با بدبختی وارد اینترنت می‌شوی و می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است»
♦️
سی‌ان‌ان در گزارشی میدانی با اشاره قطع اینترنت و رواج اینترنت طبقاتی در ایران می‌نویسد، قطع اینترنت در ایران اکنون بیش از دو ماه ادامه داشته و طولانی‌ترین اختلال ثبت‌شده تاکنون به‌شمار می‌رود.
برای میلیون‌ها نفری که زندگی و درآمدشان به اینترنت وابسته است، این وضعیت ویرانگر بوده است. فراز، ساکن ۳۸ ساله تهران، به سی‌ان‌ان گفت: «تصور کنید با بیکاری و تورم دیوانه‌کننده دست‌وپنجه نرم می‌کنید و به ترتیبی موفق می‌شوید ۵۰۰ هزار تا یک میلیون تومان جور کنید، فقط برای خرید چند گیگابایت وی‌پی‌ان تا بتوانید وارد اکس یا پلتفرم‌های دیگر شوید، خبرها را ببینید و صدایی داشته باشید.»
او افزود: «بعد وسط همه این استرس و خشم، وقتی بالاخره موفق می‌شوی اکس یا تلگرام را باز کنی، می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است؛ واقعا مثل مشت به سینه آدم می‌ماند.»
متوسط حقوق ماهانه در ایران بین ۲۰ تا ۳۵ میلیون تومان برآورد می‌شود. سی‌ان‌ان می‌نویسد، اینترنت پرو، شکاف عظیم میان فقیر و غنی را عمیق‌تر کرده است.
وب‌سایت «خبرآنلاین» نوشت این طرح «جامعه ایران را به دو طبقه متمایز تقسیم کرده است: نخبگان دیجیتال که از اینترنت سریع و بدون فیلتر برای تجارت، آموزش و ارتباطات بهره‌مندند، و رعایای دیجیتال که در محدودیت شدید، سرعت پایین و هزینه‌های سنگین بازار سیاه وی‌پی‌ان گرفتار شده‌اند.»
قیمت وی‌پی‌ان‌های بازار سیاه به‌شدت افزایش یافته و بر اساس اعلام سازمان «فعالان حقوق بشر در ایران» مستقر در خارج از کشور، قطع اینترنت طی دو ماه گذشته حدود ۱.۸ میلیارد دلار به ایرانیان خسارت زده است؛ رقمی که با برآورد اتاق بازرگانی ایران نیز همخوانی دارد.
روزنامه اطلاعات نوشت: «قطع اینترنت ــ که خود منبع درآمد شمار بسیار زیادی از کسب‌وکارهای مجازی بود ــ وضعیت بحرانی و پیچیده‌ای ایجاد کرده است.»گزارش‌های داخل ایران نشان می‌دهد «اینترنت پرو» از طریق «فهرست سفید» در سطح اپراتورهای مخابراتی و بر پایه «سیم‌کارت‌های سفید» عمل می‌کند؛ یعنی برخی سیم‌کارت‌ها، حساب‌های موبایل یا نهادها از سیستم فیلترینگ کشور مستثنا می‌شوند.
برخلاف وی‌پی‌ان که با رمزگذاری ترافیک اینترنت سانسور را دور می‌زند، «اینترنت پرو» ظاهرا کاربران تاییدشده را از مسیرهایی با محدودیت کمتر عبور می‌دهد. گفته می‌شود دارندگان سیم‌کارت سفید همچنان به اینترنت جهانی کامل دسترسی دارند.
بر اساس گزارش‌ها، هزینه اینترنت پرو برای بسته سالانه ۵۰ گیگابایتی حدود دو میلیون تومان است، علاوه بر هزینه فعال‌سازی ۲.۸ میلیون تومانی و حدود ۴۰ هزار تومان برای هر گیگابایت اضافی. در مقابل، اینترنت عادی ــ که اکنون به‌شدت محدود شده ــ هر گیگابایت حدود ۸ هزار تومان هزینه دارد و همین باعث شده بسیاری ناچار به استفاده از وی‌پی‌ان شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75394" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q0Y5zm7o5ZvTsiPGrk8s57fkwRX-GcDCZwxakBOrmaeCjMZR88MN8rUs_WKMiGZfV2lVjBF3kv-0BrKVm1AJKVQEL0OTvGgoNKgUgVXCeCauQfgL6HFa2UNi75vQx1iIu5oi4oXxc0KUfvyetaWgktQEeh_gTiFOftjbW6_ZrPJ1lcMZvKehFhZDs7_sJMUjldmm2X1MD4OORm8fzIOn5XaUTBmJMarogXflIs2Oc_ORbrkkf8COsmx_BH5tLUUhKXrkXXmqwsSUng9sIFZXFSfonTTYdjOtnzqsx4-guGPh66fIyULIsBmaYUeUxToJta3HqW8pNWB3InoQEnPnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، صبح دوشنبه، ۲۱ اردیبهشت از اجرای حکم اعدام عرفان شکورزاده، زندانی سیاسی، با اتهام «همکاری با سرویس‌های اطلاعاتی آمریکا و اسرائیل» خبر داد.
شکورزاده بهمن‌ماه ۱۴۰۳ از سوی اطلاعات سپاه با اتهام «جاسوسی و همکاری با کشورهای متخاصم» بازداشت و به اعدام محکوم شد و حکم صادر شده علیه او به‌تازگی در دیوان عالی کشور تایید شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75393" target="_blank">📅 09:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bPqtSGFhIWXQZwhoQvs9tMwhdTiiyRQ4H2eNXtMT9exQhgMTxqGSKEnVKS5FDT5HnVSb3y6g9ehxqxEnasZJ41Zxz-ZditWQyJtfv6s8U4nQ9TTZE6jywo6bOD0t5AXgkOwXjVW8LZtgcl4g5f1cb8w9OwlrMt27y3_ubpRUlyx2Bh767Pii4s9Fbl0x0yD9lSP46-1yZHMvJln6m07D6DOrBTzPc7M-o_a1DBfdVkGrDeqBgPZkrlysptKCr1YhdOSUi1na5vWHkYrRzMMog6Fja0LG9RskpR_18itD1r6WhMIHJUG1IMCNcLlh4yGK0Wj2XkZH-rGrsgd4bKYwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pXTqIOFxBciHqfO9i9QL5mg-2mSFsTro23Uebs24r-StM783T4ulf15NVyRM1x1uX3NlPFEZRJFuPrwmnLQ_lznKb40_UE-RdmajZcnDQVByFaIFblGFJ9VM7vYbweKV1pJPfeoksXBBQyhybGyiRFEgGvimyXc4SGx8XzSdkZfWY6RAYN3Fy99I_k1v3SaHneAu4RnG0RPsrK6FzTFvkfhHg6sA-jVluCRcZ2VDTEm4Yv3TKGzpEUgVQiuBN8eMkWjPvxxa4wIRJU9o9RLQJvzgPvJnzvpHKzfoZL89-nU3dpeRQ0xLYEVxbi8XcdrBIprxsllmIFFhqSwfFIRoOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آکسیوس
: پرزیدنت ترامپ روز یکشنبه در یک تماس تلفنی کوتاه به آکسیوس گفت که پاسخ ایران به تازه‌ترین پیش‌نویس توافق برای پایان دادن به جنگ را رد خواهد کرد.
ترامپ اندکی پس از این تماس، در پستی در تروث سوشال، پاسخ ایران را «کاملاً غیرقابل قبول!» خواند.
ترامپ به آکسیوس گفت روز یکشنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، صحبت کرده و در میان مسائل دیگر، درباره پاسخ ایران نیز گفت‌وگو داشته است.
او درباره نتانیاهو گفت: «تماس بسیار خوبی بود. رابطه خوبی داریم.» اما افزود که مذاکرات ایران «مسئله من است، نه مسئله دیگران.»
ترامپ در این مصاحبه کوتاه روشن نکرد که آیا قصد دارد مذاکرات را ادامه دهد یا احتمالاً گزینه اقدام نظامی را در پیش بگیرد.
سناتور لیندسی گراهام، جمهوری‌خواه از کارولینای جنوبی، در ایکس نوشت که ترامپ اکنون باید اقدام نظامی را در نظر بگیرد؛ موضعی که گراهام در سراسر آتش‌بس یک‌ماهه بارها تکرار کرده است.
او نوشت: «با توجه به حملات مداوم آن‌ها به کشتیرانی بین‌المللی، حملات پیوسته به متحدان ما در خاورمیانه، و اکنون پاسخ کاملاً غیرقابل قبول به پیشنهاد دیپلماتیک آمریکا، به نظر من زمان آن رسیده که تغییر مسیر را در نظر بگیریم.»
گراهام نوشت: «پروژه آزادی پلاس همین حالا خیلی خوب به نظر می‌رسد»؛ اشاره‌ای به عملیات دریایی برای هدایت کشتی‌ها از تنگه هرمز که ترامپ پس از کمتر از ۴۸ ساعت به‌طور ناگهانی آن را متوقف کرد.
@VahidOOnLine
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، روز یکشنبه، ۲۰ اردیبهشت‌ماه، به نقل از «یک منبع مطلع» در واکنش به پیام ترامپ مبنی بر «کاملا غیرقابل قبول» بودن پاسخ تهران به پیشنهاد واشنگتن، نوشت: «همین الان واکنش به اصطلاح رئیس‌جمهور آمریکا را به پاسخ ایران دیدیم. هیچ اهمیتی ندارد؛ کسی در ایران برای خوشایند ترامپ طرح نمی‌نویسد. تیم مذاکره‌کننده فقط برای حق ملت ایران باید طرح بنویسد و وقتی ترامپ از آن راضی نباشد، قاعدتا بهتر است». تسنیم نوشت: «ترامپ کلا واقعیت را دوست ندارد؛ به همین دلیل مدام از ایران شکست می‌خورد».
@VahidOOnLine
خبرگزاری صداوسیما گزارش داد طرح تهران که ترامپ آن را «غیرقابل قبول» خواند، بر ضرورت پرداخت خسارت‌های جنگ توسط آمریکا و حاکمیت جمهوری اسلامی بر تنگه هرمز تاکید دارد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75391" target="_blank">📅 00:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BHpkxQ_JeTZq2SAESBU15XiIo9237jRKsMoYdOkv6QmQXs4nkmyjD1oA_6GAv7knOVkKsSNdOolf6tyMu0gx7Vx6cWD9w8RxiN_NsnByJskxnQKRqWgFYGiapubj8nY9ZsBoxWMT8P0XUYVRPxZkxeSZj-T_08g9qTO5_5cjz24uNyWPd8D740bBYN7m0NY30l-TId94_rrXCQ80X_ZWZ_BkiiR5FVvAg5ifTF1Bnj6YQQvL0P_RiMqm6K_YpIE8J7BJulNA8KHGmHm5DuHPpO4mTDmBenHxcK-zs7zrSBT_3njQj5bL4fEycgbvf7atcYVI1k5I6cfMkvcbfvurwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ پاسخ جمهوری اسلامی را رد کرد
پست ترامپ، ترجمه ماشین:
همین حالا پاسخ به‌اصطلاح «نمایندگان» ایران را خواندم. از آن خوشم نیامد — کاملاً غیرقابل‌قبول است! از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75390" target="_blank">📅 23:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RDI24inJ0Sy8_kniPvt15rSKZHSuT9WA15qV-2A3F2yan4lPJQzQNAA2TuKTYJet64ZazNx9_pN89DSgVUuW6S7yFJatInRQyX87QeslskPvCAvvDfSERM1AQjg9qbheZmtlqOL0wN-W3ItxoSbVqqa2S0y69rCycIPKJWknz5TuFeNW7dYMSPJ8_ntizY_hdNAtzs_mJy24szc3CLI_o4kPivdp6-eidIas7fhFeHVOw1rzZGK2Afubb-0pPR03IQPffhYosRdtpJ_vzjXH9eP4UYTrzlUDs363AWKveOTGUC6pWGbCwZKyWm0k-fxvP4bdKbfgFs0Ph_l8MV5Q5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال، شامگاه یکشنبه ۲۰ اردیبهشت ماه، به نقل از منابعی آگاه، جزئیاتی از پاسخ ایران به پیشنهاد صلح آمریکا را منتشر کرد.
به گزارش این روزنامه، پاسخ ایران که از طریق پاکستان به‌عنوان میانجی به واشنگتن منتقل شده، همچنان اختلاف‌های مهمی میان دو طرف باقی گذاشته است.
به گفته منابع وال‌استریت ژورنال، تهران حاضر نشده از پیش درباره سرنوشت برنامه هسته‌ای خود و ذخایر اورانیوم با غنای بالا تعهد بدهد.
ایران پیشنهاد کرده مسائل هسته‌ای طی ۳۰ روز آینده مورد مذاکره قرار گیرد.
مقامام‌های ایران همچنین برای رقیق‌سازی بخشی از اورانیوم غنی‌شده و انتقال بخش دیگری از آن به یک کشور ثالث اعلام آمادگی کرده‌اند.
وال‌استریت ژورنال گزارش داد تهران با برچیدن تاسیسات هسته‌ای خود مخالفت کرده، اما در عین حال آمادگی‌اش را برای تعلیق غنی‌سازی اورانیوم اعلام کرده است؛ تعلیقی که به گفته این روزنامه، مدت آن کوتاه‌تر از توقف ۲۰ ساله پیشنهادی آمریکا خواهد بود.
بر اساس این گزارش، ایران در پاسخی چندصفحه‌ای به تازه‌ترین پیشنهاد آمریکا برای پایان دادن به جنگ، خواستار پایان درگیری‌ها و لغو محاصره کشتی‌ها و بنادر ایرانی شده و پیشنهاد داده است تنگه هرمز به‌تدریج به روی رفت‌وآمد تجاری باز شود.
وال‌استریت ژورنال نوشت ایران در مقابل، خواستار تضمین‌هایی شده است که اگر مذاکرات شکست بخورد یا آمریکا در آینده از توافق خارج شود، اورانیوم منتقل‌شده دوباره به ایران بازگردانده شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75389" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsmUhzg_T-FRSybHKdIiqwZ91WnVQBGDO0dPUEDbH9suGQ-WdfWMJMGNklKbdwa9xCRWGOXev_UgBVrFZyySWKXTni4RjSg31ESK31SxKclHtTDUfXCfOSz8jy13_qxBh06_4-ux2Vd4441IMSrwal7sYQLaIZQsEfg8bvmcE_NhsJs_aHM6OJcpJyT0PGS6rEOpUwDcbEKtiJwzsW4ZNkSY6Z431s0y8OnMnQOkbq3bnyn4H3-AtO8MBvKbvDD4Eo4_BseZUKG5QGCmbqyFulPgRU1qljDcEyCCFO4DmwvU2QpL3WneSjlB9ijGs74cf4_c1Xt7DMn6VZd6-YgK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران شامگاه یک‌شنبه با اشاره به شنیده شدن فعالیت پدافند هوایی در اندیمشک و شمال دزفول از سرنگونی «پرنده متخاصم دشمن» در اندیمشک خبر دادند.
شهروندان نیز یک‌شنبه ساعت حدود ۱۰ شب از شنیده‌شدن صدای پدافند در این شهر خبر دادند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/75388" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#دزفول
#اندیمشک
پیام‌های دریافتی از شنیده شدن صدای پدافند:
پیام ساعت ۲۲: دزفول حدود 20 دقیقه صدای پدافند میومد
دزفول وحشتناک صدای پدافند اومد.جدود ساعت نه ونیم
سلام پایگاه چهارم شکاری دزفول از ساعت ۲۱:۳۰ تقریبا یه ریز پدافند فعاله
پدافند پایگاه وحدتی دزفول فعال شده از ساعت ۲۱.۵۰ تا الان ۲۲.۱۷
فعالیت  شدید پدافند در اندیمشک ساعت 22.15
اندیمشک
ساعت 22:19 امشب پدافند فعال شد در حد 30 ثانیه.
یه صدایی میاد انگار پهپاده
سلام، اندیمشک ۲۲:۲۲ دقیقه چند دقیقه ست پدافند ها فعال شدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75387" target="_blank">📅 22:32 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75386">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QvDqd7bFjsixRPho5bl24Nv715VVd-N0ycYQIjF6X48PzooPplW4cNXg_sB4JEaBmL66hIwzEDF0zsgN9g1GNXywA1hAQAAPx_26FHen2U3Y0fKmSidfmwr_FSIOORoYEVd5_j1vcUeEfXxynrquM-eLHvDbjLRNctqLLt-VYBo1Hdrm9jNFMzbXHOhWC8tvAi904n3-HL6jHTGQjl85vz8CLU5jg5zTIfYkA6zFIFiXgkAO1gjf19Tt_AWcPVdz7avhnFcKhzbGcyk3vmi7oG6TrkR4BiVfLVrN7jgu0G5Myy63drLB6eEJa6QX-9yopLLu8xH1L81YhOE9SxbF8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: آن‌ها دیگر نخواهند خندید
پست تازه ترامپ پس از آن که جمهوری اسلامی گفت پاسخش را از طریق پاکستان ارسال کرده. ترجمه ماشین:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است؛ «تعویق، تعویق، تعویق!» و سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به گنج رسید. او نه‌تنها با آن‌ها خوب بود، بلکه عالی بود؛ عملاً به طرف آن‌ها رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت تازه، بزرگ و بسیار قدرتمند برای ادامه حیات داد.
صدها میلیارد دلار، و ۱.۷ میلیارد دلار پول نقد سبز، که با هواپیما به تهران منتقل شد، مثل هدیه‌ای روی سینی نقره به آن‌ها داده شد. همه بانک‌ها در واشنگتن دی‌سی، ویرجینیا و مریلند خالی شدند. آن‌قدر پول بود که وقتی رسید، اراذل ایرانی نمی‌دانستند با آن چه کار کنند. آن‌ها هرگز چنین پولی ندیده بودند و دیگر هم هرگز نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما پایین آورده شد و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آن‌ها بالاخره بزرگ‌ترین ساده‌لوحِ همه تاریخ را در قالب یک رئیس‌جمهور ضعیف و احمق آمریکایی پیدا کردند. او به‌عنوان «رهبر» ما یک فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
ایرانی‌ها ۴۷ سال ما را سر دوانده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای خود کشته‌اند، اعتراضات را نابود کرده‌اند، و اخیراً ۴۲ هزار معترض بی‌گناه و غیرمسلح را از بین برده‌اند و به کشور ما که اکنون دوباره بزرگ شده است، خندیده‌اند. دیگر نخواهند خندید!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75386" target="_blank">📅 21:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm6iCqMCxwTSsK4IKN60q7cXEfnaVmHxMZWn9zL43qTuJKnnud5W3QFdOJ_Gk_78nYtLwW9c7UOAdvuCBysburofB1l5rG47jHKwTLkoYC2uoacatD4g9GFvo7U7cCoILTl4CiYZ5_gEP2_jfDqPB-cq8AN96sZz6norX3_8LtJsofNKgGdTazf4kwG6E4Ys9S_FvwRfzJGGlkM_ERbuJOWCuwp88WyGXrj6-XVE6en_28mNty6zaKKrFLLmHe87yhRZmlA4QD0mqy01_VFJB2ZFeRfdWQuFYQGprarLJpeWLzsfPVQxQLblgp7DDDx5BBZQXHlK4I_Jj9KtoOOsRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در بخشی از یک مصاحبه که قرار است ساعاتی دیگر مشروح آن پخش شود، گفت که ذخایر اورانیوم غنی‌شده ایران باید از بین برود تا بتوان گفت جنگ آمریکا و اسرائیل با ایران به پایان رسیده است.
او در بخشی از گفت‌وگو با برنامه «۶۰ دقیقه» شبکه سی‌بی‌اس گفت: «این [جنگ] هنوز تمام نشده است، چون مواد هسته‌ای، اورانیوم غنی‌شده، باید از ایران خارج شود. تاسیسات غنی‌سازی هم که وجود دارد باید برچیده شوند.»
او همچنین گفت: «ایران هنوز از نیروهای نیابتی حمایت و موشک‌ بالستیک تولید می‌کند. بخش عمده‌ای از اینها نابود شده‌اند اما کارهایی باقی است.»
آقای نتانیاهو در پاسخ به این پرسش که این اورانیوم چگونه باید خارج شود، گفت: «وارد می‌شوید و آن را خارج می‌کنید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/75385" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75384">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qbhsyMlATUJTxP1MA5CKCeUdP7rArVLhzgO1MkMQlSDfQqG-lOFx2rs0UyHZ_sgH83jCVyh5N86kzysgZwGURR06uovVbr4sNbZtPBJ7DT2poivMlCg9xmgxhgE0ABbzcb0bn2YuGb_96ZCmp571K7umIALv89RUQsHeAQxNTc7vvyBdLTWHu7y5zdJJQ9PxHfV-ktDb82XXctmTNoAmTpIoTSEQBraGT2jKntnciPA6SYj2tQiE38mifo_h-H7dS4-eQ8Z2k80EvFV6_cmY12m-hUn8alCdhwIoQMl_M4JygFcM4BHpZyw1RC6JR8a19qlyKHu7w2OZ2Y_E4NKfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Afkham_minus
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75384" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75383">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYNHzpcL7e_Cm0EK0N8KvaEC7Euf7wQk3sWGQojd4a6_S4PwED2CWCp8iAN8JhTXlGgL_uhPIACHUPn5Yt-OUKRSD9oz8DuPf0Bb33CHVKA3U5HAPRXuqA2xsCKcXwL3d8_xQbMYm6PP2ptxGmQ0Watd-ZxRimdgIqNtyc3jkbfHvPn3M5rRmUH5l0VAmqNSW3tksVHv-k-g0lZzyIbiVWUyWj1YGJBMGwesyAWS7xWLLwn1YCsO2ilddU8SIIQt5qdqD-yLiJjx0Q9PCvWOb9bi_-nQRb4j_qvNjSO6bfSIqiyiuE6pTj72hPexDY8jgNd4EhZQWrtcGmJIhuz_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رحیم نادعلی، معاون فرهنگی سپاه «محمد رسول‌الله» تهران گفت: «در جشن بزرگ پیوند آسمانی زوج‌های جان‌فدا، خودروهای جیپ جنگی برای جابه‌جایی عروس و دامادها در نظر گرفته شده که با گل‌آرایی، پرچم جمهوری اسلامی و تصاویر رهبری تزئین شده و زوج‌ها در این خودروها در مراسم حضور خواهند یافت.»
او افزود زوج‌های شرکت‌کننده قرار است با «ماشین‌های عروسی به شکل جیپ نظامی» و «خودروهای نظامی گل‌کاری‌شده» در سطح شهر حضور پیدا کنند تا «فضای شهر را به یک شکل هنری و نظامی» درآورند.
به گفته او، هدف این است که نشان داده شود این «زوج‌های جانفدا» جان خود را «زیر پرچم جمهوری اسلامی تقدیم این نظام خواهند کرد» و «از هیچ چیز نمی‌ترسند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/75383" target="_blank">📅 19:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75378">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JRN0PlJQjrtVxxDM4VDf7x1r_sOZoFzdbT7dSdJaPoMDMSghB5wZlCuwJtLU9ajG2yKSrptHLtbzGFin7GUQDuVFTdnUSTO9xxHteUhuOBOjth9wlj3MfRvk1OXpiLkw1vMk6zKUEF-y5HHsJoYw4ORbgFG3H7F29rkX1gtS1F1QSMxHZmFqHaeCQKQW14QVfjne_b_h3nqNLf4Nd4omP7FpL1u8D9sLkZwUb3blxmJCvqrv1q_VKAPXONAh07efOl953anCzpBh--XTlTb7DmCqDJS0-nbC19NIT_NC7Ob1IKqYWPFI7ji-vxH_kn-doFcgn6GXmqGisotjnWFI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vlrx6c8-hR0cUs9A3wP8aNmOVzN68gq8OQHIMDieKRAglBpXdPsaGrdOItWn7VyFjtK_bG_rZLaiFrcx5pHMfCChcr2Uq_JlpUI5jxhTTlt_9AoLpDJ6BmQh23cAr2CQrMJndvCznP7e2lcKbtjMfTsxhStMlrkSv259y6KjftGjYooXK9SbihRtpYRg1k3UgCOBngBATDY1Qrw0leGBmji1mkG5Cu8E9MbI5sPvEDJL6_ALV11TjaHq7i0cBQX8P6IoIq4dWpz9-R69thVom8_iZRxJiVdJ0vYcLlO1aQ0zAttZnOMbT8z6uNVVi9LRHcwDpqCCOXtutAi7vyT3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o6C8etT931VNjFkHf3QjorcWfQ-xSWTUx1JUfohR1a-rVoMA1F0YwGf3reN5Chd871R6-E3x_ni6PQ4Io1Tk1O3sMqe2JAJLyoThT9Q-JKR4Nf-L3T41QoZPrYvuMvoDT1RsfFuwnXkdUzFR3oRfToDgZXcvb93nbeZFbCjIXeXlrmPyHlSSgcLjIXwNz22iqPS2ga2rCdXaJAhrSJ8NT7279aoNp3ARvTgENJAQ2CsaEcd1tu8GC6GUS0N6T_kdrKhCB7XueTkNq5Xx6jUE-BcOApsJ_u58pbZqFAalDPR5V7MtftOOKhezW-W-mpNOPMSw1gyzfiXjerMJrIaNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ppmEdpRlcuAp4VTJGLdKm-HGoyE-M_cibCy_Orc0g6VTZgaPYFd9GyO-FE1i9B2giXhZ1fz41J5DlEkgUlvKLFNFhbWwzJkM_eXZq1BNX-Ey4MUMyUmLnr0uDqPB-463cCeIMe_u8VSHroKckmF8GPSLaItwDo3qZv-a_csZykwRlQxuGcxt7yXmnILwnJhbgtCVp8pGPrqQpgtIbnTpCElDrtx_emy5-MAUk34wL96ybkHSqeyFccD-r2X3Uybb_B3Cm11igYzC6THmDNh1xz6lGFZMMMAzOoZJgzupX4OxtE5Uy8ZwtCtpzsfpqGC_mxhDJTIGj8FiWsUXuQ-76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X_TAWGYnAE3aoXjELsk0vP9l4GtdEOQ6hNwxxOS0lUEupXmacJUjdff2WJhH9VAKUe3TgHi_uIM0S3xS0mdTk1MGb5W_WnBZ5JCutrzIU_TRcpmUURrB1LUUKJco_wy86JSEtrpcfurQ55lZE6V7d62DEqzTL9KzTcnijHTLf8Omk4mhqqjU_41JsuMEfB618GVPT66kAkPGOcqNbcqU2maN_WoYIP49z-_SQnCB7sXRD6Td6hGzwWZD001zjEPaVxMMMMxurTXiIyIPVYfTyZZNkWJoHxcLg1BvBeyMXfuA7PUx96c1pY7mUWCmAnndr1lGsMnIUDtYk61yiSVPgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید عملیات نظامی در ایران تمام نشده و ارتش ایالات متحده می‌تواند اهداف دیگری را نیز هدف قرار دهد.
دونالد ترامپ در گفت‌وگویی با شریل اتکیسون، مجری آمریکایی، که هفته گذشته ضبط و روز یکشنبه ۲۰ اردیبهشت پخش شده است، در پاسخ به این سوال که آیا عملیات رزمی در ایران تمام شده است، گفت: «نه، من چنین چیزی نگفتم. من گفتم آن‌ها شکست خورده‌اند، اما این به آن معنا نیست که کارشان تمام شده است. ما می‌توانیم به مدت دو هفته بیشتر هم وارد عمل شویم و تک‌تک اهداف را هدف قرار دهیم.»
او با اشاره به این که در حملات آمریکا و اسرائیل طی جنگ اخیر «احتمالا ۷۰ درصد» اهداف مورد اصابت قرار گرفتند، افزود: «ما اهداف دیگری هم داریم که احتمالاً می‌توانیم به آن‌ها حمله کنیم. اما حتی اگر این کار را نکنیم، سال‌ها طول می‌کشد تا آن‌ها دوباره بازسازی شوند.»
به نظر می‌رسد اظهارات آقای ترامپ پیش از ارسال پاسخ ایران به آخرین پیشنهاد آمریکا برای این توافق انجام شده است. هرچند که او پیشنهادات قبلی ایران را رد کرده بود.
رئیس‌جمهور آمریکا در مصاحبه با شریل اتکیسون همچنین دربارهٔ اورانیوم غنی‌شده ایران که در عمق زمین و در تأسیسات هدف قرار گرفته در جنگ ۱۲ روزه سال گذشته مدفون شده‌اند، گفت: «ما در مقطعی آن را به دست خواهیم آورد… ما آنجا را تحت نظارت داریم.»
ترامپ اضافه کرد: «من چیزی به نام نیروی فضایی ایجاد کردم و آن‌ها آنجا را زیر نظر دارند… اگر کسی به آن محل نزدیک شود، ما مطلع خواهیم شد و آن‌ها را نابود خواهیم کرد.»
او بارها اشاره کرده است که توافق با ایران باید شامل تحویل ذخایر اورانیوم غنی‌شده ایران به آمریکا باشد. تهران چنین درخواستی را رد کرده است.
@
VahidHeadline
رئیس‌جمهور آمریکا گفت: «ما نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد، چون آنها دیوانه‌اند. نمی‌توانیم اجازه دسترسی هسته‌ای به آنها بدهیم. اوباما این کار را کرد. اگر من توافق هسته‌ای ایران را لغو نکرده بودم، الان سلاح هسته‌ای را داشتند و الان علیه اسرائیل و خاورمیانه و شاید حتی فراتر از آن استفاده می‌کردند. می‌دانید، آنها در واقع موشک‌هایی دارند که دیدید می‌توانند به اروپا برسند.»
از آقای ترامپ سوال شد آیا این درست که عملیات رزمی علیه ایران تمام شده است.
رئیس‌جمهور آمریکا پاسخ داد:«من این را نگفتم. من گفتم آنها شکست خورده‌اند اما این به این معنا نیست که کارشان تمام شده است. ما می‌توانیم دو هفته دیگر هم وارد عمل شویم و هر هدفی را بزنیم. ما اهداف مشخصی داریم که احتمالاً ۷۰ درصد آن‌ها را زده‌ایم اما اهداف دیگری هم هستند که می‌توانیم بزنیم.»
آقای ترامپ گفت حتی اگر هم این کار را نکنیم، بازسازی سال‌های زیادی برای ایران طول می‌کشد.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفت‌وگو با سی‌بی‌اس نیوز درباره اورانیوم غنی‌شده در ایران و جنگ علیه جمهوری اسلامی گفت دونالد ترامپ به او گفته می‌خواهد وارد آنجا شود و به نظر او این اقدام از نظر عملی امکان‌پذیر است. او افزود اگر توافقی حاصل شود و بتوان وارد شد و این برنامه را برچید، این بهترین راه خواهد بود.
نتانیاهو از پاسخ به این پرسش که در صورت عدم توافق چه رخ خواهد داد خودداری کرد و گفت برای این موضوع جدول زمانی تعیین نمی‌کند، اما این ماموریت را بسیار مهم دانست.
IranIntl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/75378" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TStqWj1bXTa-3u7_g0nB3k1d7QkW1A-1-6X3j1hXsPF8v_Tw9rkBdRFtcwERV0Xw1GMavzovxPTKv-ny2o_i8T2BNCbS9Z_UaOrPNJ8DlTvPFB-ztgO2I0SL7E2JbXR1EoiQSGclVCB6d31l3RJa40G1fueQnzVF_1mAEjffIDIrIxHGaJiVhg966uttznLv6k7NTkcjyBSDhhnDrBV6gtGlxZcpe6FFcg7tZTuEcE78vqCSJwObI0t6ulMYNoisabQYEd_yLZZpVIARVKuzXCZuL33Qykd2fZYt1wq5vXYPEBnbJbDirRMioGH_g1ak34pmoSTcmy18s_b-M9D0Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایرنا، روز یکشنبه ۲۰ اردیبهشت ۱۴۰۵گزارش داد پاسخ تهران به آخرین طرح پیشنهادی ایالات متحده برای رسیدن به توافق بر سر پایان جنگ، برای پاکستان به عنوان میانجی مذاکرات ارسال شده است.
ایرنا بدون اشاره به جزئیات بیشتر نوشت: «بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.»
وب‌سایت اکسیوس و خبرگزاری رویترز، چهارشنبه هفته گذشته گزارش دادند که واشنگتن و تهران به یک «یادداشت تفاهم یک‌صفحه‌ای» برای پایان دادن به جنگ نزدیک شده‌اند.
رویترز نوشته بود در این تفاهم‌نامه حتی به تعلیق فعالیت هسته‌ای ایران یا بازگشایی تنگه هرمز که از سوی سپاه پاسداران بسته شده، اشاره‌ای نشده است.
در مقابل، روزنامه وال‌استریت ژورنال گزارش داده بود که در طرح پیشنهادی آمریکا، تهران باید ثابت کند که به‌دنبال سلاح اتمی نیست، تاسیسات فردو، نطنز و اصفهان را برچیند، فعالیت زیرزمینی هسته‌ای را متوقف کند و همچنین بپذیرد غنی‌سازی را تا ۲۰ سال متوقف کند.
رییس‌جمهور و وزیر خارجه آمریکا روز جمعه گفته بودند جمهوری اسلامی تا پایان همان روز قرار است به پیشنهاد ایالات متحده پاسخ دهد.
@
VahidHeadline
ولی جمهوری اسلامی به جای جمعه، روز بسته شدن بازارها، صبر کرد یکشنبه پاسخ داد که ساعت ۸ شبش به وقت شرق آمریکا بازارهای مالی هفته کاری رو آغاز می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/75377" target="_blank">📅 17:51 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhUSnqLnCUMKqaIDQurMIAmwtt6_g8eL52KzkQoREHY2O-0QT23GArsRFGCpnQ-ZQCHdKHJpGTHUbKij4ssVANg_u8q4WIRI8z0UAGoOGsdtHDvcjAItt0-qKSLiKw7tl-bu72Qv2rnlRC6oiEf20gAicLkJ-B4bYUF0N-5QzMfBufovzRfvy9ijNrL8UR80Iw62FN9KkyHn_SycjxYTxW3MjnVvvanB-U3dMPaGlR_GaaWGHbLRQ_d4lArqIM2srGpB5HEfzJUpwpw8OMZ_4HcNkBXFhQmrp5ZpDH0DMuWpVAkzYV02pVTfsjGY3lIBmahz2mEvjrAjhFa1Ui8PAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع امارات متحده عربی روز یکشنبه ۲۰ اردیبهشت اعلام کرد که سامانه‌های پدافند هوایی این کشور با موفقیت دو پهپاد پرتاب شده از «ایران» را منهدم کردند.
این وزارتخانه تاکید کرده است که از زمان ««شروع حملات آشکار ایران، پدافند هوایی امارات متحده عربی در مجموع ۵۵۱ موشک بالستیک، ۲۹ موشک کروز و ۲۲۶۵ پهپاد را منهدم کرده است.»
وزارت دفاع امارات همچنین گزارش داده است که از زمان شروع حملات آشکار ایران، تعداد کل جانباختگان نظامی به ۳ نفر رسیده و تلفات غیرنظامی هم ۱۰ نفر از ملیت‌های پاکستانی، نپالی، بنگلادشی، فلسطینی، هندی و مصری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 205K · <a href="https://t.me/VahidOnline/75376" target="_blank">📅 17:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0bO3xY3SUL7YDk67Ia1GEv4VibMjwVOMnEx6o5B1yzkoxtUZvn8IwPtepifj4FSL5l7GL-Vs7XESOkFJnHROa_5K9h6JE_Y64iFGccQQQcsWTtTe3NnFGYpUVlPGJGqas9AXI2ZKZJpAk9IBgiJXBTJfZi8h8zOZTLDYsB0_2u2FumQwL6UAY6-030iCwJtO__VvzkBUNcyDrbOEiNQ2dNSJcTKto5ySVrAW9ODjY0D5Yau8q4A7k7e_pz5PPCO7WK7f9R25Z_gxpCeoxHjSbrYL8s8J7FC5GnVROIC0kks9ncU0ETDJ_fpNZMcF0WUJYU8mL10YclRJnpknewxPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی گفته‌اند علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، با مجتبی خامنه‌ای دیدار کرده و گزارشی از آمادگی نیروهای مسلح، از جمله ارتش، سپاه، نیروی انتظامی، نهادهای امنیتی، مرزبانی، وزارت دفاع و بسیج ارائه داده است.
بر اساس این گزارش‌ها، عبداللهی گفته نیروهای مسلح از نظر روحیه رزمی، آمادگی دفاعی و هجومی، طرح‌های راهبردی و تجهیزات لازم برای مقابله با «دشمنان» در سطح بالایی از آمادگی قرار دارند.
این رسانه‌ها همچنین نوشتند مجتبی خامنه‌ای در این دیدار تدابیر تازه‌ای برای ادامه اقدامات و مقابله با دشمنان ابلاغ کرده است. با وجود انتشار متن این خبر، رسانه‌های جمهوری اسلامی تصویری از این دیدار منتشر نکردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 192K · <a href="https://t.me/VahidOnline/75375" target="_blank">📅 17:46 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2cbPdXrmZlje_-Mf2Hu2IefSadDoXqBul1LO53Hp88I5x7oVJ5npCAK1c0MpqCz12Ca0zsBO2XvaNsbk3PT53Pc6qJvp5LEsFyBIgtoa-INib-PnWcOb5zE5D4HFdUyDFFQKg-K15RAh4vgp9cvm-aOuyQcLsliNn5vYhKsogBi-chAZ2Gw_o9f2ClcxFEGUpyP91e_iOM1FXs7oPJi4Ml6JdvedsWZR47NorVad2oeIR06687Bo9UImgFwMEmKC6ER33pi_82oBAxRtAJlC_6JefvSkHSCQS3Zy_vUr_c6Cwty_XvNh94LLyuQ1cNfL7hjmCKxxHD6jY-wIu7O8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران درباره کشتی باری هدف ‌قرارگرفته شده در نزدیکی سواحل قطر، به نقل از منبعی که نامش را فاش نکرد، گزارش داد این کشتی با پرچم آمریکا تردد می‌کرده و متعلق به ایالات متحده بوده است.
سازمان «عملیات تجارت دریایی بریتانیا» (UKMTO) صبح یکشنبه گزارش داد که یک پرتابه به سمت یک کشتی باری  در ۲۳ مایل دریایی (۳۷ کیلومتری) شمال شرقی دوحه شلیک شده است.
بنا بر این گزارش یک آتش‌سوزی کوچک در این کشتی رخ داده که خاموش شده است و تلفات جانی نیز نداشته است.
این خبر در حالی اعلام شده است که مارکو روبیو، وزیر امور خارجه آمریکا روز شنبه با محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر امور خارجه قطر، در میامی دیدار و گفتگو کرد و شراکت دو کشور را برای بازدارندگی در برابر تهدیدات و تقویت ثبات در خاورمیانه حائز اهمیت خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/75374" target="_blank">📅 17:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75373">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mghj0WOiT2-2S8AOOLGqSBI433F5TFgImaBmvb_RQtE0Rp7PY00cltQNbza8i6kaMPO_zKWY_5hlOI0Npy8GB708RBRQLnaEuiXfqfEBdRJzsSxRmzXLHikEYu-8bfasMpH8pY6RabRakZQpDza70LZBvyXM-Q_shTIy5IYAa2FwxY4RKkRS3dB4Jr-hMIx1kbdrBFLrXJVR1b3xNXVASNQ4GGIlVIwmI_Q2aN6zNoBy9F_c4WXxQfxM-CFtzBzoHAAPH23F5QNle9TOSmBMptYUDugCklvFRT-q6e5zLN-SUHrSw0QgN2SI2vBJqU1LRZvGt1FRnk6rX_7M2E7bsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
خبرگزاری فارس می‌گوید «یک نفتکش حمل‌کننده گاز طبیعی مایع متعلق به قطر به نام الخریطیات» با «اجازه ایران» از تنگه هرمز عبور کرده است.
بنابر این گزارش، این نفتکش «روز گذشته در دهانهٔ تنگهٔ هرمز دیده شده بود و پس از آن سامانه موقعیت‌یاب خودکار خود را خاموش کرد.»
به گفته فارس، «این نفتکش که مقصدش پاکستان است، نخستین نفتکش غیرمرتبط با ایران است که از نیروی دریایی سپاه اجازه عبور از تنگه هرمز دریافت کرده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/VahidOnline/75373" target="_blank">📅 17:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75372">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnYd5kqkfJ4ktt6O9A6QjcAeyUgqwLii5vkMNDbSOxMFuaCVKqttAvUnApXPZi-97mhAFi9WCf3IuatWNQE6uXrPywNhYYx2fgUdFNL6ZKxERGiXGEZ65GXN1l4OC_745oTbvbo_-4lLHBWgrh6UswKOXJwZRmYGFGJnozelUlAykhHCrrMqruDTXFe8H6sgmOQhAd9nw-aXy8TfHqRi3a2g3NBtczIaErqIfKtuqV3iomagdwFTAny-GXunKbV1HEUi-dhiELjf-xd4BJqi7YmbMS61kVa6z-R4Fip_srXtFVrV_g6Jxlkck8g3MN4sPFftH6bRuT3f-JubmWJ1cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های داخل ایران روز یک‌شنبه به نقل از مدیرعامل شرکت پایانه‌های نفتی ایران هر گونه آلودگی نفتی ناشی از تأسیسات جزیره خارک را تکذیب کردند.
او گفت: «به محض انتشار این اخبار، گروه‌های متخصص اچ‌اس‌ئی و اداره شیمیایی و آزمایشگاه، همه منطقه را پایش کردند اما حتی کوچک‌ترین موردی یافت نشد.»
خبرگزاری رویترز گزارش داده بود که تصاویر ماهواره‌ای ثبت‌شده در روزهای ۱۶ تا ۱۸ اردیبهشت، لکه‌ای بزرگ را در آب‌های اطراف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، نشان می‌دهد که به گفته کارشناسان با «نشت نفت» سازگار است.
بر اساس این گزارش، لکه‌ای خاکستری و سفیدرنگ در غرب جزیره خارک دیده شده که به گفته یک پژوهشگر «رصدخانه منازعه و محیط زیست»، مساحتی حدود ۴۵ کیلومتر مربع را پوشش می‌دهد.
به گفته عباس اسدروز، «طبق اعلام مرکز بین‌المللی «میمک» به نمایندگی از سازمان بین‌المللی دریانوردی هیچ‌گونه نشتی در زیرساخت‌ها، مخازن ذخیره‌سازی، سیستم‌های اندازه‌گیری، اسکله‌ها، خطوط لوله این منطقه و کشتی‌های در حال بارگیری وجود ندارد.»
اسدروز توضیح نداده است که لکه موجود در تصاویر نشان‌دهنده چه چیزی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/75372" target="_blank">📅 17:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75371">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wfgq_FCwohGT3ZlDee3R4fZkbTokmT3Zkcg_Rm-tPN7K1uNEI5TWCV3GEp-N4UaLpuwaaN5PXZ7fbJn4FROe_AdcOkYODwqonjVw_tvsEsdQefjQFp6k9Lonk9txbwCf4ipqTBa5P120n8dHm1v0wPIrZBbYhIbxtFQoEfcsiX1tf8JwI1IdZuu3Xh_mJaaSYirRdMfAPHzt5nU4alUAaZymVEKYawphXJ1HXFWBQjclSYv09r3adIyFwbB1Zngfru3mfgZ139FWji4wNWgu8ubvhtQUFIZzEVW0cwsL3pzlv23V6h_dKddRFFzX2kuBk2OVBypqbjXwmt98ytBAFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «وال‌استریت ژورنال»، اسرائیل در اقدامی بی‌سابقه یک پایگاه نظامی مخفی در بیابان‌های عراق ایجاد کرده است تا از این طریق عملیات هوایی گسترده خود علیه ایران را پشتیبانی کند.
این پایگاه که پیش از آغاز درگیری‌ها و با آگاهی ایالات متحده احداث شده، میزبان نیروهای ویژه اسرائیل و یگان‌های امداد و نجات برای خلبانانی بود که ممکن بود در جریان حملات سرنگون شوند.
طبق گفته مقام‌های آگاه، استقرار این مرکز لجستیک در فاصله ۱۶۰۰ کیلومتری از اسرائیل، نقش کلیدی در مدیریت هزاران حمله هوایی تل‌آویو علیه اهداف نظامی رژیم جمهوری اسلامی در خاک ایران طی هفته‌های اخیر ایفا کرده است.
این گزارش فاش می‌کند که مخفیگاه مذکور در اوایل ماه مارس و پس از گزارش یک چوپان محلی درباره تحرکات مشکوک هلیکوپترها، تا آستانه لو رفتن پیش رفت. در پی این گزارش، ارتش عراق نیروهایی را برای بازرسی به منطقه اعزام کرد، اما نیروهای اسرائیلی با اجرای حملات هوایی سنگین علیه سربازان عراقی، مانع از دسترسی آن‌ها به این سایت سری شدند که در نتیجه آن یک سرباز عراقی کشته و دو نفر مجروح شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75371" target="_blank">📅 01:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75369">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YJPQl7-32DtBlY-5ag_SN9QePhkpCxhHCLnu0ZnXE1V99uYkR1TAb8YrMYQIhgPMVecccZVMycVWBbDYMkJzKgqrcTi42U1RuhZ2BYZLG1ulTjMMqNvT69cHGgsUfvtUSfegI0eS5DH0RO0ch7nUJvBUYQmqkO2q_yk8KHbo60qXkb9wNhrd14-PmNLVULwZtQnVm9cHGOjBQ95_aQNaX2RpMoHVxMih8blqWv4l-92HlYw1sywqfFHkaWc7GnROVJuDitcP34bQ9_RGMkftiB53Anf3sScgcZpO7D-fQnxVCsbQN7_DDz_nz_OblllibQ2OQy8a_1WKstuPfFdkWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c_fHcvZ7N1ZY2i98oIOUwwsvFXbTQa30S3vEsb_kc4WknCbAkRa0HSD-ArnagPnJ5_jgYq7OGGXUhvM1EIBmf4Izf8BOA_XUF0kwoKt1rGFQNq6MnvLg6Qd_Z7sxBenqA5jypjNhouEl2UN2mH77jWneABvYXteIp31xb-iGApwZUUm0JjST43Pg4h2Gvl5H9k8qiBAp16lyFmrMq9ydSJdFqaKufd61xzdsuTGgSECmHxGy1z7wdSVB9IPNZHm2q9QAo30OW6VmCsALWJwy3PVa_4JDRTtzYnMv0b8V22mo1S3j5EHvAHPJHbjmVDj7Bslg603r8P6CYMdLlaRKRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر ساختگی دیگری که ترامپ در صفحه‌اش منتشر کرده
:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75369" target="_blank">📅 01:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75368">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ckEMG3GbHMTB_gyY3fbXH3wZzGysHCMZiyOpPiMx_uwNVtFEBRUIjyOimLb5oUDSQSo6bJyvMHhm2SdCsnnbEUN3_gbiWa4NYVTLKrh74D7pjdFXP4Vu0nek-3jcQJs0LnZmSlAIDC1s3lESpuysXxhOR2rhinDayLYXJcLlHF__-z0PpHn-DvzPo71Om-uF0FcdTSC3YUhOFsJCSrNJhm3dJUv_je09nyosiWWw0CblrXme2uhzKRU68fu2tU-x_3h-MKYp84-STr2_ot24imKUFlJitgCTW3-ktHm-HgHD-85kC14HATXPQ7Tw5jSsSzbvfYIi7cWPRYUe6UDgeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75368" target="_blank">📅 23:39 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75367">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9B_yoEt2Fi0GzSoSA6BmSOQ63mC7X71Xzfm_1ezLaWgu1cwUW2uG_5KUd4dii2lRFpJOS0c5IEIQSpPQ3exdrvP30Bw0OfZpjNZr3odPJXOWoFrVaBNn_7FZp4wl1Wm3JTKZZoMUDrqi5eBxAb59YMaFuX0FAtH30F5upt8X580L7vNU1EqkUewweV-DfUFCHsxH884IwnNLuPZZiNOGx83Wy6O4WKhigm8vlt2b1rAKAGHQ43th_Gttlqaz2QkzfU1ZRSJkDXXj4nM7dtPppnWyejud4oQMSG_p2dwBT8BK-WHyVurMV57i5jp0rAMDXw1K8kCyVfbovKoXgJbkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، با اشاره به کابل‌های فیبر نوری عبوری از تنگه هرمز و تهدید به اختلال در اقتصاد دیجیتال جهان در صورت آسیب به این کابل‌ها، خواهان اخذ هزینه از شرکت‌های خارجی و الزام غول‌های فناوری نظیر متا، آمازون و مایکروسافت به فعالیت تحت قوانین جمهوری اسلامی شد.
تسنیم نوشت: «کابل‌های تار نوری زیردریایی عبوری از تنگه هرمز روزانه حامل بیش از ۱۰ تریلیون دلار آمریکا تراکنش مالی (شامل پیام‌های سوئیفت، معاملات بورس و تبادلات ارزی) هستند.»
رسانه وابسته به سپاه در ادامه خواستار «اخذ هزینه مجوز اولیه و تمدید سالانه از شرکت‌های خارجی، الزام غول‌های فناوری (متا، آمازون، مایکروسافت) به فعالیت تحت قوانین جمهوری اسلامی و انحصار تعمیر و نگهداری کابل‌ها از سوی شرکت‌های ایرانی شد.»
فارس، دیگر وابسته به سپاه، نیز در گزارشی نوشت که ده‌ها کابل فیبر نوری زیردریایی که آسیا، اروپا و خاورمیانه را به هم متصل می‌کنند، از گذرگاه تنگه هرمز عبور می‌کنند و تهدید کرد که «هرگونه آسیب به این کابل‌ها می‌تواند اختلالات گسترده‌ای در اینترنت و اقتصاد دیجیتال کشورهای مختلف ایجاد کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75367" target="_blank">📅 23:38 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75366">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTdxHYIbgP4J-wpSvCstegX5tJjBglGatjB-19t1_9d7GGeNN6jh53p8Dchrekb6dZvlB76XzpPfYHc7twf9vscEPdmR-H9e1jWqySD___WWLNXidURuWjSPzQciK4TKmC7qD46Gp-RnodTP8W2zOOo0zisfNQNmKmE99D1yHj6mKE_x12daXKlZv0lXnS7pYOxgH-uONq8k0dGz0XUBwIe5MxLeMvNJU6pVbr0GIdYhhJM1F41eJELk2ZZcHJjn4Hg2mJq1vabJn55t4Ujd80Qb-hawJx5a9ac8Mmr7awoitH0mZXSyto7ek-pf4N0dWB39N3v09O4aOJXP5zEE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، روز شنبه ۱۹ اردیبهشت، ساعتی بعد از برپایی رژهٔ «روز پیروزی» در مسکو، گفت که معتقد است جنگ اوکراین در حال اتمام است.
او بدون اشاره به جزئیات بیشتر دربارهٔ این جنگ به خبرنگاران گفت: «فکر می‌کنم این موضوع در حال پایان یافتن است.»
روزنامه فایننشال تایمز روز پنجشنبه گزارش داده بود که رهبران اتحادیه اروپا در حال آماده‌سازی برای مذاکرات احتمالی هستند. وقتی از پوتین پرسیده شد آیا حاضر است با اروپایی‌ها وارد گفت‌وگو شود، او گفت که گزینه ترجیحی‌اش گرهارد شرودر، صدراعظم پیشین آلمان، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75366" target="_blank">📅 23:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75365">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6d6c074f6.mp4?token=qs1sP-vfCoTWgBk0n77nkfLm9FGdPRLPvP6vQvL9Uu9BUwrNlPzo-nPYaHj-jBpvoNPEEWlb1Ie2GvLmnCGtgie4Ko7BygYCLcNavTya9qGsdtHguus7lBAsyQDIc4jzVN_vUkSODzOhg0aNdGPzx_hGwM88IUXctad3HKnHBzdr_ESgdg0fVxMhtp22YpIlR82B8RA2nO3zCbWa4rajRagJVorD-MqN0eAveay34ddx5rEoEiXVezyOzZti5cMj_JP-01IharzGZZ29rI4wLcu2a5EHI_5k8T7oT0uPajqRJTSoYnkkAgdarCi2_uFrdWqRvGgAIalbjXwLFyVvgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6d6c074f6.mp4?token=qs1sP-vfCoTWgBk0n77nkfLm9FGdPRLPvP6vQvL9Uu9BUwrNlPzo-nPYaHj-jBpvoNPEEWlb1Ie2GvLmnCGtgie4Ko7BygYCLcNavTya9qGsdtHguus7lBAsyQDIc4jzVN_vUkSODzOhg0aNdGPzx_hGwM88IUXctad3HKnHBzdr_ESgdg0fVxMhtp22YpIlR82B8RA2nO3zCbWa4rajRagJVorD-MqN0eAveay34ddx5rEoEiXVezyOzZti5cMj_JP-01IharzGZZ29rI4wLcu2a5EHI_5k8T7oT0uPajqRJTSoYnkkAgdarCi2_uFrdWqRvGgAIalbjXwLFyVvgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از تجمعات شبانه طرفداران جمهوری اسلامی منتشر شده که در آن فرد خواننده می‌گوید زنان «کم حجابی» که در تجمع طرفداری از حکومت شرکت می‌کنند «نور چشم» آن‌ها هستند و ظاهر افراد ملاک نیست.
نظام جمهوری اسلامی پیش از این زنان بدون حجاب اجباری را بازداشت کرده و طی لایحه‌ای به نام «حجاب و عفاف» قصد ابلاغ جریمه‌های و محرومیت‌های سنگین علیه آنان را داشت.
با این حال، در هفته‌های گذشته حکومت سعی کرده با انتشار ویدیوها و مصاحبه‌هایی از تعدادی زن بی‌حجاب در تجمعات حکومتی، پایگاه اجتماعی خود را گسترده نشان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75365" target="_blank">📅 21:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75364">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMqyAjSxyV-brUwvzyzgF38AV46k9EuIuVNmf3H-oswhe3nm9C4SQZGYRfKp5mMalgpX0b_TxklZR_rkmufZxwQOrvJxcjZTlT4yWJg8lhXyE8WTVUoAYeNvclR2NfmNwXoCHBA3axISeclx7dgdFnwUJEIVG1FsAxvoEj2d4uY1OBbe87XCxLBmtYlgMYPk2U6Tydelbh3Y8GV18TCjXqTasepq5fClWxonptieJSHnRlaLJKa4oAo_FViFn27npFa3dkbvx0S2XQzka5RGc0yvHeEo6_qMTBEyR7EFhEig1RiKdvsEVETcU5km3-9z-qMrlSexYkI733chi5JIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های لبنانی روز شنبه اعلام کردند که در حملات هوایی اسرائیل به جنوب لبنان، هشت نفر کشته شده‌اند. همچنین بزرگراهی در جنوب بیروت هدف حمله هوایی قرار گرفت.
این حملات تازه با وجود آتش‌بس سه‌هفته‌ای میان اسرائیل و حزب‌الله، گروه مورد حمایت [جمهوری اسلامی در] ایران، انجام شد؛ آتش‌بسی که تأثیر چندانی در توقف تبادل روزانه آتش، عمدتاً در جنوب لبنان، نداشته است.
حزب‌الله روز شنبه اعلام کرد که در واکنش به ادامه حملات، نیروهای اسرائیلی در شمال این کشور را با پهپاد هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/75364" target="_blank">📅 20:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75363">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXzZfOoOlgV50syJx4pDl3LZv18naXlnwulNQnOQyYTeazz7TZIwS8xp5yspo6NqnXy88Hs88axJxd0hanM0aFKcedTfvEy6W8XsoXePVW45NBbIhtXUh25bsSeJoESCTNKNxUUw1POyX3MbXGjdHOaFcy1pKDpRzlPYhLgy0VMfx3K77R5krgHA-Lp8y2Vv5pVQRX1eKU10tQsZwS9DsVksFtlSsaD7NyHar2BAx6vEwtJFHzEpEK49w8LCZo9yx9egukMvSm3FCwKjuM3HCOgLvppACh9shtiw_fnlN_thNv0ZUO8_1SZk-4c4R2itegxwtECgw7N9tBFY2eG72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی آمریکا، سنتکام، روز ۱۹ اردیبهشت ۱۴۰۵ اعلام کرد محاصره دریایی آمریکا علیه جمهوری اسلامی همچنان به‌طور کامل اجرا می‌شود و نیروهای این فرماندهی تاکنون ۵۸ کشتی تجاری را تغییر مسیر داده و چهار شناور را از کار انداخته‌اند تا از ورود یا خروج آن‌ها به بنادر ایران جلوگیری شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/75363" target="_blank">📅 19:40 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75358">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lGQQ8ToTkjfaQFvSW-c7HsnTXknHp1IHrc4vzhceb9w-KrusiGUoiN6dINr-USH3vQL8ZeirBiBpEkyfLI-RcqtwQ12h03W4ioAKli5N41e2Tb7znG2dSVJl66FPj-vZG06HZyRekRf-NDMqiec1UP3Y8OZNrudrXRB4g8RMQkO-Yz_uOTlhEQgmXugINI7_AzwmNh0R14JrcDqdSB_g6QEc6QPzQmlV9YFLar7HFbNXn5ajyfX52SE5a5_7Ki6c8piK_IroCPQqU4S9wQhPHfuplN_yXHN17CEx_QzufiM-OJdd24SprPuYxQxodEZ42lkxcDnbg4Lw7P_iTMqvQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bHnkiN0vPUFisLQd6c5qI4NIRDi1TWvGIPV5WADkBUvgOZszzNoM0Mhhy5NE5vbt_aIWmyZurMpszE4Ad1ywamMd0d1LkQ4-Ipvs9kh_5u-J3sJ5JUJxu1c0ZO8FKa0AKANpgSA6B2AgmcsoCAepUMeUTmfZQFNtAg6iWRHrLLL5ShFFPGj2EXNxDd-y_PQGVsdnZYuzlsrpIO5s_rvQ5r0_o0jNzPyPsK1KC_lmNQ0zmYw2-OnnLndN4_oH-nj-FE7AfgPf1XIZvPjFfIoaj-hHdKNiFAV47rDBe9KdIgjVhUKYp0Z2tcatHD-wjHScoWkBDXRPXkp3ilRSaOHHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gtF3txkiipcjEQWzx9b619LH0wA7-8WLYLF1nQ9VFKDOE8uMyQ18yKNydNkS1mpVpzKLLsEwqygnqK-3j8NYkfDD2T_8C_rkuvpl_n9jkiM2brQqcAgDKSzsYE8T_TYb8kiPbb6Q12dJGZE4aLvs9kuAFcW54NA3vXFsa1FMk9-00kYl_1dxKZ9D75PMPfBBwwVMFt7-DV9TxPws33CwvQGjFG0tO4a3r21pWRmDP2SdbzcLuQLV4quTJAcP2S8vqj-OEFtyIj9XH7H8dRr7eFLDrgpmRQJ6ImGYc8tfxim8Z4lQaJ9ci4kWfTyYKhYzGRhAAo_DC4SJ69-VXxaPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FHOwaDp3daShtQMTkUI-tSY8jD1u3NAyVVILES6IpqM0sz_VHUcu0YA-BNJiJ3ZzXJeFvzZcIcbK5mfpj7tGAx3JqbUlp2tm_EmbSuY8hQ7STXm8QJ4Qtvax45AbmQWbWoxvvO6j-VnhN0pWI9tvKaOBvn0Hr6OE3Bi_pytMIt9S5xnJPT7ptjsI9H5NtcvuUUVG3z6fzxVEAA6LrY5KMzWoHSVDGLaS4hGWRs6L7ezO273_PRMbcbWoVJQmCHD2cFYfwoDxuhUoNHfptKHrPvQItOZTqrugsxQRB-hqUpitxqp41p7dMNJwGKztsOqjuXxaRwVIwuH1tNTkZy-uoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rQzF1XAeRsENBSeqjLOLPt90GVkdmYbeh4VvDvJm2noAvifyjNqUaxFApFzRqV6VrQFyjpUqtDJ2XN8nn2szztYD0c3tRZh8sbYgvQfuWA95X3PTon9qmVxlL3PI0eMOnaOPECbmgfttPL_CGaClyi9k_qcoyLQxV7mhzMuuziC_Da81caSv8ZLS563lF8fOBGThTXU16TUxvHOr7Rp8EaxDB7T_jOuZHsN656FwQFLpD8t-xW80nGoiSCSwl7r8pR8RoaL5ay1BJhBvqj4fizVqbB6-NPavj90MTIaJUPawKKbyZhR33YSgaY6qfBFmaC6kbHgBE7_2nPkl35FAXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذشت
‌ عبدالله امیدوار، یکی از دو برادر امیدوار که اولین نزدیک به ۷۰ سال پیش با موتورسیکلت دور جهان را گشتند، در سانتياگو، پايتخت شيلی درگذشت.
عبدالله،  برادر کوچکتر پس از پایان سفرشان به شيلی رفت و در آنجا ازدواج کرد و شرکت فیلم‌سازی در شيلی تاسيس کرد.
عبدالله۲۱ ساله و عیسی ۲۳ ساله،  در سال ۱۹۵۴</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75358" target="_blank">📅 18:51 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75357">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgb3_C8q4rOQ-TSEJISpdQ1r1xR00XXpWT9n6kibwxYw7Ug4s4vZGOgWSa_fTVB54AmwQZn_G2HAWX4eoTrL0TVNdyH989cMDDa2Qaqh47TbepOzH7_9t9bfuWMtTlT8T0pC6dWogzsw2e12NaoiBbzOeA431F0NcxGeuNkQ413AgHVpDBC_5IYaVncdDgt0oA4OObHYMgRKI5LOk3tT2jxnhw7XNIf4-3QuNasp7QiZzu2WwCmKqKZDFZ0lU1L4UmOaoW-hY28lk_74DHPEE1wk5soRv2NoOuMMJhm86YZVGmErlYAJyHd9i224VCI2TF22od0zAeVeMod-4A8G1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع بریتانیا روز شنبه اعلام کرد که پیش از هرگونه مأموریت بین‌المللی برای کمک به حفاظت از کشتیرانی در تنگه هرمز، یک ناوشکن به خاورمیانه اعزام خواهد کرد.
سخنگوی این وزارتخانه به خبرگزاری فرانسه گفت: «استقرار پیشاپیش ناوشکن «اچ‌ام‌اس دراگون» بخشی از برنامه‌ریزی محتاطانه‌ای است که تضمین می‌کند بریتانیا به‌عنوان بخشی از یک ائتلاف چندملیتی به رهبری مشترک بریتانیا و فرانسه، در زمان مناسب آماده تأمین امنیت تنگه باشد.»
لندن و پاریس چند هفته پیش اعلام کردند که طرح‌های نظامی برای تأمین امنیت تنگه هرمز در حال شکل‌گیری است و در بازگرداندن جریان تجارت از طریق این گذرگاه حیاتی موفق خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75357" target="_blank">📅 18:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75354">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qjy4N4nIEguJq7BcKWyN3qjA7wxyQXbjMIj7rWzEHMiTAxe8O6bj-M7rwe8HbU-ipSW4Oa8VR1jxM-YHNjCV-vf3EyhilKsspBjuAYnZIgYsuVUDuKovkSotEfZw2w8cGMdcsgK2jabbeYBoEfsk6jFMKDBV6V7becpRCeH1qr5vZ_I2IJMa3P05mFH0tH6_KvGvwV4Y6wbALNerMWa8hDN0PaJTiiOXvAcokQDHk0G1DvTuLwY2ZHFLUj_fpTmdPquBCIeuEeue7-Hd2RutP5PetO9kpjLhP4mdqcbllkgTJCdGzrxSFWZvDcEg4gJvaii2_qtgVzUMaKm-RAbi2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U6U1UlUBflJs4AXfSjno4mhTqEiwF01oxENEQ_YVrCbHKiEjgaDivKbdbgPVb0hio-sfPv_I8R26uitpgT6I8gZbxwRPkKlARVdOgN7IF2_S4S4hmid7KHkZnRHhmqPUh3UBiPVOnWZWIKCGVou8iCusAvLRWEqH9mwvKnimp_1h9qgd1AQihJwWaCsBWZpSGR8xhc8yL2IpPsSzWIj4uTFJMuIlb4Ad67rL_fEi7ZOU8kxxLMxL0T-KYFEP6xJAxchFYeL-oBXKC2cvBh-wTBtab53aZlnXClWowiHA2qcdbxifD_Ibo1NkbA4npUjp6fWwB0eyOsB3BP0Wz9lxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V67I967qo85plJKCG6XzHuJzzZZ39DKYvjWri256qL61zZQUNTOrby-IFvftYDzUq955Iv-dzGyfQ9MdvhBvi-rMy5yI08dktdYc7zRcy9pnGdME3xJ-LEEFvSJ81gsisUT71N-ghwyXaGx1hGZoBZDiarn5sBTK5k4hOBQ6_8Sy-029LSkLNwQXL-l35os7PW3naZhfycA-DSkCUMTHBzyBO9SDZqD2wAaMko5Ln2oplCCbLOlHk-z1IOBRlx23y8UwR3CW111hahugfA5rSlF7g7BDAZlxW_eyfgsYXMeLhpel2OCJNUjMJk49F9vr9t_yV95-Q9tOBdAuQNqcgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت کشور بحرین روز شنبه ۱۹ اردیبهشت اعلام کرد که ۴۱ نفر را که به گفته این وزارتخانه با سپاه پاسداران ایران مرتبط بوده‌اند، دستگیر کرده است.
خبرگزاری دولتی بحرین به نقل از این وزارتخانه گزارش داد که مقامات امنیتی گروهی مرتبط با سپاه پاسداران ایران را شناسایی کرده است و افزود که تحقیقات برای شناسایی و برخورد با هر فردی که در این تشکیلات فعالیت داشته ادامه دارد.
@
VahidHeadline
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی، روز شنبه ۱۹ اردیبهشت، با انتشار پیامی در شبکه اجتماعی ایکس کشورهای منطقه از جمله بحرین را تهدید کرد که در صورت همراهی با قطعنامه پیشنهادی آمریکا در شورای امنیت سازمان ملل، با «پیامدهای جدی» مواجه خواهد شد.
عزیزی بحرین را «کشور ذره‌بینی» خواند و نوشت: «به دولت‌هایی همچون کشور ذره‌بینی بحرین که در حال همراهی با قطعنامه آمریکایی هستند، درباره پیامدهای جدی این اقدام هشدار می‌دهیم. درهای تنگه هرمز را برای همیشه به روی خود نبندید!»
قطعنامه مذکور که با حمایت آمریکا و کشورهای حوزه خلیج فارس به شورای امنیت سازمان ملل ارائه شده، از ایران می‌خواهد که ضمن توقف حملات علیه شناورهایی که قصد عبور از تنگه هرمز را دارند، محل دقیق مین‌های کارگذاری شده را اعلام کند و از دریافت هرگونه عوارض عبور از شناورهای عبوری خودداری کند.
@
VahidOOnLine
وزارت خارجه عربستان سعودی در بیانیه‌ای حمایت کامل ریاض را از اقداماتی اعلام کرد که پادشاهی بحرین برای مقابله با آنچه «اقدام‌های صادرشده از سوی ایران» خوانده، اتخاذ کرده است.
در این بیانیه آمده است این اقدام‌ها به گفته مقام‌های سعودی، امنیت ملی بحرین را تحت تاثیر قرار می‌دهد و با هدف بی‌ثبات کردن امنیت و ثبات این کشور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/75354" target="_blank">📅 18:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75353">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddEJboOy1JrtwlSanG-ZkbMDZJSExJ4YJsiMAxXsPdRk27mEe_CvOWgMBuuKEk1ueQJ7K8_TkYvDpGc-j-eZbtOkZ8IN7b0VhwPghyvdM3C5G2FMWdF0Go02NaJZKR_eQ6LpKzo91TN3ozQaOTWevwDaPxiFyyLldv7KNNUhaVtkD_eB6xuzYDblEKIe9FwAWjHRV8bBVF_7DwavyiYFjNGnAjS0sctOSag8xVEXO9xFGtYK2pQsvQkR823DvOcAZgqTLELr9RcvijMu8TiQPwbOp2VwofsOkV5SoS91gEVQ2D6876d0Hwpf_83n-EvixmRZ-TslbitpgzuFqTsHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75353" target="_blank">📅 18:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75348">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sTGrvUvtrUHXW1DT_EsEyBTloj7zNnTCbMskn5kZplZV6IntIHv9QrHYd3tbWcao6REE6byQTCyxA3tMLpWrFWoXOjYA4A5Gncko27rm1jh-DlqnQ9-SI59n4mMIyM566AyV59fBuOsBzgBTcjYhnFRHY5xi7jp-u_3V4-8XYm3-ZIfNyYBkqIus5AlNmaz84o35cLWUj7h-0WkOM9hdLbm8uHBxGvwAuCA_UZ0iK8Dj6dpWtLEVrnsUUcb10b7Y2qvSQWkxESagw1JeGjoV3yzHGFxGvyWl-CC9BhNMteZdJf70igoodgWUw0t-9PH_8ihuEcU8GrjJI9dSrSo4oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iJWVRMORRu_1-gPGb94D22GVKXrLN0OECKc8l5VsgNmZ8ih7V0amY25gX9Dnw5CKMwsfWQC_JDYWW_xo4JFbmP2DKXI-CEicTjvmcgA2Umoinn9C6HqgvNItZFKpbJmtUbQKD4Bs_at4xALHp6atkPljEgOO1OdmpwAw5RQ1pfnoJ-ouIEuCnw-De0ews3ru6CmqoaAAeEjDfDdnR9vD5INL5dnwOcSpRvK895lj9_EItgA8M1nQ6E0wtYjPKAR7SVZb-VNQRhy0vzvQLbF52wMIoYRkTWYdrsbZX78Gn8ji99J67zMGFnv3H2Iyz_bO2axLiuXDDEoe8R6tn5P7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J1JaKxUi0PazIo9kkgSM3JnxaQO6JdkDzbJ7gA-dBwlCTBwd0OtUQgwP25QWW8_iegUh1Z51b9cUfPPV32-tuIBkpHFwSfuB5EYmMWuXXxMem6QSUdj5bubDBzKu_TskQruOEZyGb1A7yzl9P6Jg4bZTTDCnJHhYUDtkO1zlZmSI4eYJMO60fvv6Py98o7Zp-iNjMgljTUgtpXr5GHgneNUlwsuwFVmtuHW4Kx0HaeYhztrNkdw5abTtbw3Cp7GAfc1MnWp5_8eQvH_YSCXCLmWVA2H35VZfPrpS5WFPkisvOv0m11KpHee8dYnRDXjcdjMhW_azOwnL7ah8bWBD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ucbDcxf8c9K0bKfbS-WPkt7q0xU6tfLeIx9MOEQjdbACIG8xnz3Srx0S2excRixVyzT6duzsVIbWSuGYftXg5XhyTdCru0-hnGbMwJG2mFs-9EyaT1baZpMWfNSxyt_U_jVODOjSdBBl-Hoz_g1VtplPd6FsbowQX5lP7xX4NdoF-GmuH9dWF7DaLZc4YDA_gGXaipcjsWQc2RChSgI3DksbXMzZGaqUgNHiQHzdQKhuhPeylGJNdAka4RZtpfB8ekqNnATrvXe_vq2BwtUUJ5HDB4WgHRFM0pQyU_hbuKaWram-kL5qp9xApqmzz48P4bAQ2TtklgxZe52RgpopQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZIxlfVVnLPmsLDOPBsnIElAh8gGZTs6zY1niA6Yi1xUKza2eOIMFHduMtV4K8sjtNQlXAxL08Oe4rcwIfCtZA6eO0D1FvCw8tMAsdNmNT-_1ra1g4qgdr8D8CGU4JCaGRt1iRvrIEV7vsGLq7fm7byvr0S6YyPkqmV8B5rXzTFdCqfgDCkmXS7m_IAfg68unbEvgPzjOX0rI4vxByABcUSDRqJaVA0Zg6W532H7mCoA1oOBEx-yb7A69O0yIECYcnEssXT734LeqE-MeXAFI56APzKtSppatNRZ5Hx1rnwEle1FuJGYYrCFFYhlQlIDbcpa6SPZ_UhQDjfJvIm_36w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در آغاز یازدهمین هفته از قطعی سراسری اینترنت بین‌المللی در ایران، یک مقام دولتی هشدار داد که این اقدام حکومت در درازمدت خود به «تهدید امنیتی» برای جمهوری اسلامی بدل خواهد شد.
احسان چیت‌ساز، معاون وزیر ارتباطات در دولت مسعود پزشکیان، گفت: «قطع اینترنت فقط در بازه‌های زمانی کوتاه می‌تواند کمک کند و در بلندمدت تهدید امنیتی است.»
قطعی اینترنت در ایران روز شنبه، ۱۹ اردیبهشت، یازدهمین هفته خود را آغاز کرد، در حالی که مردم عادی در کشور تنها با صرف هزینه‌های گزاف می‌توانند به اینترنت بین‌المللی دسترسی داشته باشند و مقام‌های حکومتی و عده‌ای از حامیان جمهوری اسلامی با مانعی در دسترسی مواجه نیستند.
@
VahidHeadline
معاون وزیر ارتباطات ایران خسارت‌های ناشی از قطع اینترنت برای اقتصاد دیجیتال ایران، در پلتفرم‌های بزرگ را ۵۵ هزار میلیارد تومان اعلام کرد.
او گفته است: «مجموع عدم‌النفع (کاهش درآمد) این حوزه نزدیک به ۱۶/۳۲ هزار میلیارد تومان برآورد می‌شود.»
معاون وزیر ارتباطات ایران همچنین گفته است قطعی اینترنت در حوزه مخابرات و ارتباطات حدود ۶/۴ هزار میلیارد تومان کاهش درآمد مستقیم کسب‌وکارها را در بر داشته است.
آقای چیت‌ساز گفته است: «قطع اینترنت برای کسب‌وکار اقتصاد دیجیتال ممکن است برای چند ساعت قابل تحمل باشد، اما قطع گسترده و سراسری آن عملا یک شوک اقتصادی ایجاد می‌کند.»
یازده هفته از قطع سراسری اینترنت در ایران می‌گذرد.
افشین کلاهی، ازاعضای اتاق بازرگانی ایران، پیش از این گفته بود که خسارت مستقیم قطع اینترنت در ایران ۳۰ تا ۴۰ میلیون دلار در روز است و خسارت مستقیم و غیرمستقیم این محدودیت تا۸۰ میلیون دلار در روز می‌رسد.
@
VahidHeadline
خبرگزاری دولتی ایرنا در گزارشی میدانی از تهران، عملاً تأیید کرده است که قطع اینترنت بخشی از فروشگاه‌های مجازی را از فضای آنلاین بیرون رانده و به خیابان و پیاده‌رو کشانده است.
ایرنا نوشته پررنگ شدن دستفروشی فقط محدود به نقاط مرکزی تهران نیست و از بازار امامزاده حسن در جنوب غرب تهران تا شهرک اندیشه شهریار نیز دیده می‌شود.
به گزارش این خبرگزاری، مدارای شهرداری و «دستور آگاهانه» برای برخورد نکردن با دستفروشان، این روند را آشکارتر کرده و بخش‌هایی از شهر را به ویترین بساط‌گرانی تبدیل کرده است که به‌اجبار از اینستاگرام به خیابان کوچ کرده‌اند.
ایرنا نوشته فروشندگانی که تا چند ماه پیش با صفحه اینستاگرامی، پرداخت آنلاین و ارسال سفارش فعالیت می‌کردند، حالا در نبود اینترنت آزاد و پایدار، ناچار شده‌اند در خیابان بساط کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/75348" target="_blank">📅 18:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75346">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pvMmrYOwcredFoQahZCQ23VU6AZ2a23AJVggJuKVmpCwNrZEVf6drzCE6uZrfo8z347cMM5xJRuqYhSmxr383AWIHuEFuIayrIKxaKGsDAH_fyw9zhtL9UcGbrPT0BUZau0wYLSOLvrBRQ-MXlsrYbic2DIpSIr0mOo67Ct_I_UIJhQNiXAmWmewpm5DMf5RZ8w9fQno75rQuSu5BErzlR3cbergQIywQfMp0J1d0BQnLqPDkkkQjyOAM-X1MLIxjf0PJmYYmY3C4lmm67zvFruvabL3C1WJeaz3DN_7OvAhSf-XWbGqpPPq0B0vrx90TW-KheyolqaPoSm27eB4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AuZUaJkqrL8mI8zaqLY5vli4CZgZKpzypc-lFE6_obfmqrUZU6kKTKdEE1IBHni0w9Zpuy8NNM7-heUGyRrwrJScAKIG4bRDXYJoa0mKgLr7A8y9iWwBjwmewkc7RT_pXKdV8EXJl7wDebtgA30YHeFhPihz134ksMKKUaigce_K9tTQO66zNcI_Z6fICmtQomlcEyZC6P0j6wfB1U-vqCf-X1oK_7_8DaaqwFPsiFleusXVCTzaoQCZShUezi2iscFxj6xHACFvBljnEzs_Ou0B9hlZ54_MbNxymNANmm_mJq5WkipuIlh9SdXqNn1XPhC_u_oCtKyyeVV7oDS0Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه‌ترین داده‌های مرکز آمار ایران نشان می‌دهد قیمت برخی کالاهای اساسی خوراکی در فروردین ۱۴۰۵ نسبت به مدت مشابه سال قبل جهش کم‌سابقه‌ای داشته است.
بنابر این گزارش، روغن جامد با تورم نقطه‌ای ۳۷۵ درصدی، بیشترین افزایش قیمت را در میان اقلام خوراکی ثبت کرده و قیمت آن از حدود ۸۱ هزار تومان در فروردین ۱۴۰۴ به بیش از ۳۸۵ هزار تومان رسیده است. روغن مایع نیز با افزایش ۳۰۸ درصدی، از حدود ۷۴ هزار تومان به بیش از ۳۰۰ هزار تومان رسیده است.
برنج خارجی درجه یک با رشد ۲۰۹ درصدی، مرغ ماشینی با ۱۹۱ درصد، سس مایونز با ۱۹۰ درصد و تخم‌مرغ با ۱۷۰ درصد افزایش قیمت، از دیگر اقلام پرتورم بوده‌اند.
این جهش قیمت‌ها در حالی رخ داده که فعالان کارگری سبد معیشت خانوار کارگری را بیش از ۷۱ میلیون تومان برآورد کرده‌اند، اما حداقل مزد پایه ماهانه کارگران در سال ۱۴۰۵ حدود ۱۶ میلیون و ۶۰۰ هزار تومان است؛ شکافی که نشان می‌دهد حتی درآمد رسمی کارگران فاصله‌ای چندبرابری با هزینه حداقلی زندگی دارد.
@
VahidHeadline
خبرآنلاین در گزارشی نوشته اثر افزایش ۶۰ درصدی حداقل مزد سال ۱۴۰۵ تنها در ۴۵ روز از بین رفته و قدرت خرید کارگران دوباره به سطح پیش از افزایش مزد بازگشته است.
بر اساس این گزارش، حداقل مزد پایه ماهانه امسال ۱۶ میلیون و ۶۲۵ هزار تومان تعیین شد؛ رقمی که در روز تصویب، با دلار ۱۴۳ هزار و ۷۰۰ تومانی حدود ۱۱۶ دلار ارزش داشت. اما با رسیدن دلار به حدود ۱۹۰ هزار تومان در نیمه اردیبهشت، ارزش دلاری مزد به حدود ۸۷.۵ دلار سقوط کرده است.
خبرآنلاین نوشته قدرت خرید مزد بر اساس طلا هم افت کرده؛ حداقل حقوق که در اسفند معادل حدود یک گرم طلای ۱۸ عیار بود، حالا به ۰.۸۱ گرم رسیده است.
این یعنی افزایش اسمی دستمزد، زیر فشار سقوط ریال، تورم و سیاست‌های اقتصادی جمهوری اسلامی عملاً خنثی شده و کارگران دوباره با شکافی عمیق میان درآمد و هزینه زندگی روبه‌رو شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/75346" target="_blank">📅 18:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75345">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS3EE8FBO6I9idYd8RSF89XkChp68tBL-n05LlEwZMOCTD6K8dHOHL7R12aWdYd3ZMOHeaBwDkNKEbuuS6OvoiFXXWw-UbCfHRZFlIn6I7r51lTNcRMsuMYqvpYJtSddVxuNfzvbFS_ytA-wheRvqMMAOQFUH1dkrcmBvVEEsykgI9RFkuaDAqj3QihyuXkxXG32hC_qV5k_MAma125-jbukP4fhEGw55YkhE7QVgbDqM6Br2TmQoXKv0GktWMZC8ZIZKfgTN-2EoO86EwZh--0gGOsWPH8k4NjKDpa00WIO4LudpSED7io-9UgG9lNiC5I4tgE8O0GxFr8b0fQU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جمعه،‌ ۱۸ اردیبهشت، یک خبرنگار در کاخ سفید از دونالد ترامپ درباره نتیجه تحقیقات دولت آمریکا درباره حمله به مدرسه میناب پرسید.
او در پاسخ گفت که این مسئله هم‌چنان در حال بررسی است و نتیجه تحقیقات «به محض آماده شدن» در اختیار خبرنگاران و رسانه‌ها قرار خواهد گرفت.
در جریان حمله به مدرسه‌ای دخترانه و پسرانه در شهر میناب در جنوب کشور که در روز آغازین جنگ مشترک آمریکا و اسرائیل با ایران رخ داد دست‌کم ۱۲۰ دانش‌آموز و ۲۶ معلم کشته شدند.
چند روز پس از حمله، تحقیقات رسانه‌ها نشان داد که این مدرسه که در نزدیکی یک پایگاه دریایی سپاه قرار داشت با موشک‌های آمریکایی هدف قرار گرفته است.
از آن زمان تاکنون هفته‌هاست که پنتاگون اعلام کرده است در حال تحقیق درباره چگونگی رخ دادن این حمله است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75345" target="_blank">📅 18:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75344">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQr90Q1rBcV6-KTeX-vLPFtyX0PfBuUUN_RW6GsIO-uVD284d1ZDNkynBejprXaEFrLMKO87dUfzs_tWxJ2FPzKPcj9za6HIHagkiF_m3Sw1bcI1cjYyn53H9VsZVKszooAd4FVP_BFzkYqDruZH2rjpKMsZhr3FBoEPdY3k6rst4mlmkTXGeuJbqv8XIT-d5MOZCpru1tuKDFeiBhXCDWysKBDshPVv2SlnOEjlcNGKth-X-FKfw9IJqyjhvbkxH79FqdlhSh1POeRbRepX5x2BnMShHEC7IkDawxsKLfyOb7qFGWZxObYrDdPGD5f2HgJir3xNEMSy8a197BT7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به خبرنگاران درباره چشم‌انداز توافق با جمهوری اسلامی گفت: «اگر همه‌چیز امضا و نهایی نشود، مسیر متفاوتی را در پیش خواهیم گرفت. اگر اتفاقی نیافتد، ممکن است به پروژه آزادی تنگه هرمز بازگردیم، اما آن پروژه آزادی پلاس خواهد بود؛ یعنی پروژه آزادی به‌اضافه موارد دیگر.»
او در پاسخ به پرسش یک خبرنگار مبنی بر اینکه آیا جمهوری اسلامی عمدا روند مذاکرات را به کندی پیش می‌برد، گفت: «به‌زودی خواهیم فهمید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75344" target="_blank">📅 03:02 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75342">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rEcYso6OjLT1T2inG-PBVoPJaTqQaGsgLp7rvZ1SAb8I9iP93gZfzAYWCGnu7QoIEvbBaPxwu-IIpp7pR-8nlEutVg9ZDo0pErJSqoVvT9rUTDd6cRokYUn1UW_Oe5wZ2UrkX-0rtocSAFU7yRlEa_c8dmOdpjGqR50KuDakC_MnF8KBdULjdEHOJCe7Wv3Hkdu2UKTn2hEjnlKVlmPg97aD725WsZWfrPzf9lvsdU6vcivDPC-JCh18avaRflrQLRa6-B4MuxzTwCRDkSqM7XPFI1DigZEeOpgwpGvr0UXnTOOg6WtXNbVw1oR-hJUczr5-TBqnCroloq7wSSzkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس گزارش داده که لکه‌ای نفتی ظاهرا از بخش غربی جزیره خارک، پایانه اصلی صادرات نفت خام ایران در خلیج فارس، در حال نشت است.
آمی دنیل، مدیرعامل شرکت اطلاعات دریایی «ویندوارد ای‌آی»، به ای‌پی گفت که از روز سه‌شنبه، معادل حدود ۸۰ هزار بشکه نفت از جزیره خارک نشت کرده است.
@
VahidOOnLine
شبکه خبری فاکس‌نیوز به نقل از کارشناسان می‌گوید این موضوع ممکن است نشانه‌ای از فروپاشی زیرساخت‌های نفتی جمهوری اسلامی باشد که زیر فشار فزاینده ایالات متحده قرار دارد.
به گفته تحلیلگرانی که خبرگزاری رویترز از آن‌ها نقل قول کرده است، این لکه که در تصاویر ماهواره‌ای کوپرنیکوس سنتینل بین چهارشنبه و جمعه دیده می‌شود، منطقه‌ای به وسعت تقریباً ۴۵ کیلومتر مربع از غرب جزیره خارک را پوشانده است.
مقامات آمریکایی بارها گفته‌اند که با محاصره دریایی جمهوری اسلامی، ذخایر نفت در ایران به زودی پر خواهد شد و رژیم ناچار می‌شود که تولید خود را کاهش دهد، امری که می‌تواند آسیب دائمی به میزان برداشت از چاه‌های نفت وارد کند.
حالا، نشت مشکوک نفت در دریا این نظریه را به وجود آورده است که جمهوری اسلامی نفت خود را به دریا می‌ریزد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75342" target="_blank">📅 01:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izy6fVXa0aRrTEKYR1zF-rOkKxwjyd3iCt0Rjl_JPgEVADvtNJi7SDdGUSw2OZ3rMfwIJjVwfG-j4KqKt9evkmmXKnHnnw9xv3bgBWQKOBMgmGO0k5aPW9k9uR-YPQIpsvpYrAgwnDODgiNSt_y38R1JTCnXaUn55wFiC9vtLj1O-4jQ_ZaCGuQaHNTGSEfODgxDJSlzh__eOLifj4IAN616H0SijzuL-K00e4kSt33AwY3jCSFrqktDKNu813ojlELTgFEO4_PFbzz7YlVplTFkMWK6ThqY0x2LLWkJtg8kl7vt7I0xaAWoZ2nJcQT52HcN-sKtrTEhwzOUWfnj6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «واشنگتن‌پست»، معدن‌کاران در میانمار موفق به کشف یک یاقوت سرخ بسیار کمیاب و غول‌پیکر شده‌اند که از نظر وزن، دومین یاقوت بزرگی است که تاکنون در این کشور کشف شده است. این سنگ قیمتی ۱۱ هزار قیراطی (معادل ۲.۲ کیلوگرم) در نزدیکی شهر «موگوک» پیدا شده؛ منطقه‌ای که به دلیل استخراج یاقوت‌های سرخ تیره و باکیفیت که در جهان به «خون کفتری» (Pigeon Blood) شهرت دارند، شناخته می‌شود. اگرچه وزن این سنگ حدود نیمی از رکورد کشف‌شده در سال ۱۹۹۶ است، اما کارشناسان معتقدند به دلیل رنگ سرخ ارغوانی منحصربه‌فرد، شفافیت بالا و کیفیت بازتاب نور، ارزش مادی بسیار بیشتری نسبت به نمونه‌های قبلی دارد.
میانمار تامین‌کننده حدود ۹۰ درصد یاقوت‌های جهان است، اما تجارت این سنگ‌ها همواره با مناقشات سیاسی و حقوق بشری گره خورده است. سنگ‌های قیمتی یکی از منابع اصلی درآمد برای دولت نظامی میانمار و همچنین گروه‌های مسلح قومی به شمار می‌روند که برای خودمختاری می‌جنگند. در همین راستا، سازمان‌های حقوق بشری مانند «گلوبال ویتنس» از جواهرسازان بین‌المللی خواسته‌اند تا خرید سنگ از میانمار را متوقف کنند، چرا که سود حاصل از این صنعت سوخت لازم برای ادامه جنگ‌های داخلی و تقویت قدرت نظامیان را تأمین می‌کند. با وجود تغییرات سیاسی ظاهری در میانمار، ارتش همچنان کنترل بخش‌های کلیدی این معادن را در دست دارد و کشف این یاقوت عظیم در میانه بحران‌های امنیتی، بار دیگر توجه جهانی را به ثروت‌های پنهان در مناطق درگیر جنگ جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75341" target="_blank">📅 01:18 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75340">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b37b7b7858.mp4?token=eNT4MZ07DbUawH9tA3EdDiXZisCo9bxZjVJsIFGwztSRXk0kJsZjkD8xa4LYigCGjiDbYxVCE1-LBpWR__o3lOdsd6CjSfsi3ju35rKTayElKEYLknxWSlwVywabeYuVy9ZuY9Ge5h9MLbwVOu70_48XXDUIDYi0mv1Mt-j9F51wo_KONL9jIR1SVixIQF5-JGJtWzw55LXDIpvSFucLbPo4SBLj0j7Tv-Wnf5X7fVTTrw_OQNJUcf08WtmfzQ4VxXVp1SeDmmSmtUopIokYYrw9o5sBeJabW2pZkNhHht5i1kQC5mP1fu15LgXzyVUZE6-u_GUbeU2pNtzBGWi9Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b37b7b7858.mp4?token=eNT4MZ07DbUawH9tA3EdDiXZisCo9bxZjVJsIFGwztSRXk0kJsZjkD8xa4LYigCGjiDbYxVCE1-LBpWR__o3lOdsd6CjSfsi3ju35rKTayElKEYLknxWSlwVywabeYuVy9ZuY9Ge5h9MLbwVOu70_48XXDUIDYi0mv1Mt-j9F51wo_KONL9jIR1SVixIQF5-JGJtWzw55LXDIpvSFucLbPo4SBLj0j7Tv-Wnf5X7fVTTrw_OQNJUcf08WtmfzQ4VxXVp1SeDmmSmtUopIokYYrw9o5sBeJabW2pZkNhHht5i1kQC5mP1fu15LgXzyVUZE6-u_GUbeU2pNtzBGWi9Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مظاهر حسینی، مسئول دیدارهای دفتر علی خامنه‌ای، در تجمع شبانه حکومتی، گفت که مجتبی خامنه‌ای در جریان بمباران بیت علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، از ناحیه زانو، کمر و پشت گوش آسیب دیده است.
حسینی گفت: «زمانی که در دفتر بودم، در ۳۰ متری ما بمب خورد که شیرازی [رییس دفتر نظامی علی خامنه‌ای] و دوستانشان پرپر شدند. ۷۰، ۸۰ متری ما جایگاه کار علی خامنه‌ای را زدند که آن اتفاق افتاد.»
او افزود: «منزل مجتبی خامنه‌ای را زدند که همسرش کشته شد. مجتبی خامنه‌ای در بین راه که آمد در پله‌ها که برود بالا، موشک آنجا خورد و خانم حداد [همسر مجتبی خامنه‌ای] کشته شد. مجتبی خامنه‌ای در بین راه ضربه موج [انفجار] خورده و روی زمین افتاده است.»
مسئول دیدارهای دفتر رهبر پیشین جمهوری اسلامی، درباره آسیب‌های وارد شده به مجتبی خامنه‌ای گفت: «یک خرده کشکک پایش صدمه دیده و یک خرده کمرش. کمرش در این ایام درست شد و کشکک پایش به زودی خوب می‌شود و در سلامتی کامل است.»
حسینی گفت: «یکی از عزیزان در هفته پیش با او دیدار داشت، آن بحث پیشانی که گفته‌اند بی‌خود است. یک ترک کوچک پشت گوشش خورده که آن هم پشت عمامه است و اصلا مشخص نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75340" target="_blank">📅 01:17 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75339">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhyhOWpBBIyMscp9zNPC5laMVHPzYm49yFczJKARco2VHCPRqa1dntRCPxBSMBDUsBey7Ki3PaagOXd_5WNaIS8mmZFhNvxKu3UubNArY4AmABYGsLfnJCMJLOOTaK-T8q8qKpl0abmOvO59egK3EFVp7Vh6Gh35ZYdO42OZ40yi8JWJE3yr9n8EC6-aq66uo4cdCdYjgcrSY3iQsOukFmIXjub-OMZTnCYZ0irfoadVIhdAx51v29mWtedhq3IJMx7KWpB_O2DqW1vn2ZarU_AN6hIfe519Ly12flTOo-MR78diC4iGUPy_DstBEalhCvdrfj7zWnDVvDq0wYXiFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۱۸ اردیبهشت، اعلام کرد که روسیه و اوکراین بر سر یک آتش‌بس سه روزه که از شنبه آغاز می‌شود و همچنین تبادل متقابل ۲۰۰۰ اسیر (۱۰۰۰ نفر از هر طرف) به توافق رسیده‌اند.
ترامپ در پیامی ابراز امیدواری کرد که این آتش‌بس در روزهای شنبه، یکشنبه و دوشنبه، «آغازی بر پایان این جنگ طولانی، مرگبار و سخت» باشد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75339" target="_blank">📅 22:20 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pndprIBMbnMfea3BHcojeSJg3uIclR6AwDuryUI3jAPy38WC4sWUFIv_5L-kh52jL76XPmCCQ-08YXbuiOf1EPS_vsMQYbQI2NH6LpwibVL23K7qY7Ats_AYkg1IgETL5FEUDjhp_iZ_1cVffGp8TzVlmGuug72sB5D9GqZ6Uidi2HumNYzJgICVjZhmIAlElKFsyaZd2Fpp8dHUrCTSInG5NsFmJqctcSmB7SA2YSZsuGLukTAgNKmMDQ0-VzAPb194RMHr5RQOTCg12XMdXnUkRsJEHVYpNjgIVA00Jwv-IV4DZjYDPCqwi-Fua3mJSmn50rbC7HTi7V8CDpCPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «تسنیم»،رسانه نزدیک به سپاه پاسداران به نقل از یک منبع نظامی نوشته است که  «پس از مدتی تبادل آتش، هم اینک درگیری‌ها متوقف شده و فضا آرام است». او اما در عین حال ادامه داده که «اگر مجددا آمریکایی‌ها قصد ورود به خلیج فارس را داشته باشند و یا برای شناورهای ایرانی مزاحمتی ایجاد کنند، مجدداً پاسخ قاطع دریافت خواهند کرد. بنابراین احتمال ورود مجدد به درگیری‌هایی از این قبیل در این منطقه همچنان وجود دارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75338" target="_blank">📅 21:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75336">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jg16TopvDC3mZWMqjQfMe1OtcM_3vU6xIbqQ08gv3c0tTfaqaSJja-x1K-8fPZFTgwAovSa-vkAXZ9WOPY5jhnkD613Kvpq_2vS5YuOJ0YQz5BA5lAYhxvjD0O6U_hQye8pBu4qTsKtm_lzFuFQ_IxfdIwKjUGSjiBz34m1VCAraq7oD7fgety4nm28mNPXPp2URv_ByMoBji-3MBePGyxl7wavJSt7llTm5fuoZhAV_vXowXkc0zFWHZnX08c_2v7K39KHuPMDk_2bLyOKvs65KfXtG88l6VC_m4REEX518G5i-Hchl2TSfLcW9ib86G5iGExLG3Ki0IzDUW5KBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/chc4HOGqN0tr1RCsHOTmTPTWMugUU0oKinglSCxMgL2l4VaYJcdN_MIycAuIn5R9Z7THDU2aHmCz_LJtb7aZhBmQj-5vHiu_oR4OFlWZAofuS28aYROHyu76o6OiJsIiaTtQtoQGRDfIS9AaSslbfHaRZgtaCZHMAWpI4CfjpX_V7MvxGBy2xQMBtXnHmnVuJmQVmJsFG1cmYVucOoA-F1lbmIp0G7CkKAPrbdSYhwsdVewhdaVak3Yp3jMuenhjP3sYNWFX_JYlCDEQFBSXeY1wHlRbCOOdG_0QXnR3HhctlOVGJC8DXEP6GHsTGsOqHyiAfrGkZV9aHU2YYlqssw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که در راستای اجرای محاصره دریایی ایران، نیروهای آمریکایی طی دو عملیات جداگانه، سه نفتکش با پرچم ایران را که قصد ورود به بنادر این کشور در دریای عمان را داشتند، از کار انداخته‌اند.
در آخرین اقدام در تاریخ ۱۸ اردیبهشت، یک جنگنده F/A-18 سوپر هورنت برخاسته از ناو هواپیمابر «جورج اچ.دبلیو. بوش»، با شلیک مهمات دقیق به دودکش نفتکش‌های «سی استار ۳» (Sea Star III) و «سودا» (Sevda)، آن‌ها را از کار انداخت و مانع ورود این کشتی‌های خالی از بار به بنادر ایران شد. همچنین در ۱۶ اردیبهشت، جنگنده‌ای از ناو «آبراهام لینکلن» با شلیک توپ ۲۰ میلی‌متری، سکان نفتکش «حسنا» (Hasna) را هدف قرار داد و آن را متوقف کرد.
دریادار برد کوپر، فرمانده سنتکام، با تاکید بر پایبندی نیروهای آمریکایی به اجرای کامل محاصره، اعلام کرد که این سه شناور دیگر به سمت ایران در حرکت نیستند. طبق بیانیه سنتکام، تاکنون چندین کشتی تجاری توسط نیروهای آمریکایی از کار افتاده و بیش از ۵۰ فروند دیگر نیز تغییر مسیر داده شده‌اند.
@
VahidOOnLine
خبرگزاری فارس، وابسته به سپاه پاسداران، روز جمعه ۱۸ اردیبهشت از وقوع «درگیری‌های پراکنده» میان نیروهای مسلح جمهوری اسلامی و آمریکا در محدوده تنگه هرمز خبر داد.
فاکس‌نیوز به نقل از یک مقام آمریکایی، اعلام کرد که این درگیری‌ها ناشی از اقدام آمریکا برای مقابله با حرکت یک نفتکش متعلق به ایران بوده است. بر اساس این گزارش، نفتکش مذکور قصد شکستن محاصره را داشته که با مقابله شناورهای آمریکایی مواجه شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75336" target="_blank">📅 19:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75335">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsklA3pHy96mG8UGZmxGKbibO_ibIK4pHFPIfQW-9QFnUQCfLhf7DQ1yq9jhL4rCNgc_HjCc3y7PB1gr3KQTNCuqisIBnvAKZfGD1iW5R7PwgBSWuzJGZ0SvpzEenxaZd_KvWATkNLIbdA7YVJnktpIn5Y12gT-sjMeeE_bUjT3XUhOng8sjgWQcShupGdvx46YVoVcshpz7ktZoDOtZP9EebGGccB7xDx67jJsDlYcHTsOBZeMaiF2syeripcwnCjaKSXquRQLdlfBvQ4rSrDeGVM028AfY-OZpTAguCRSqMVpxEACRKg07UHVroNqBGyaKj88LSe1VRAUrD4Mo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روح‌الله مومن‌نسب، دبیر ستاد امر به معروف تهران نوشت نمی‌شود نیروهای مسلح، مرزهای ما و تنگه هرمز را به روی دشمنان ببندند اما دولت فضای مجازی را در اختیار آنان قرار دهد.
او افزود که «فضای مجازی به هیچ وجه نباید به حالت قبل برگردد؛ همان‌طور که امام شهید ما به حالت قبل برنمی‌گردد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75335" target="_blank">📅 19:23 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OS9tamMsWTi8D4Siybu42i1yyNoqdD3weGSFonCMgzCcbfNFGHXkwxTmjNv0DPjmeF3y7nEtO7oqAaMerB7CdoE8WmG4NM83ZxK8col2aRe7CusrD0mjWoQY4oAv1tBFdLGOsSRLp2JcUoYJy8iCqbQ_9gacttUxG_SSWFucC4O9PpOko15BW5lI12tRZqJqGrvXUOWO0TJBpqGMbYYxuJqcjRbgheqEgzefNQwS29vMsKy-FUV2-BR5M6F7JWI3Q-SBmOZW0nXI-Owj7DmB5nCOnmK7cejgF5qvKBadFIE41WZGv2C3YGuQrpemQMM7q4Ze0Fa2A7qbRjQtSKwePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در حساب تروث سوشال خود با انتشار تصویری شبیه‌سازی‌شده از انهدام یک پهپاد ایرانی توسط سلاح لیزری نیروی دریایی آمریکا، سرنگونی پهپادهای جمهوری اسلامی را به «پروانه‌ای که به سمت قبرش سقوط می‌کند»، تشبیه کرد.
او در واکنش به درگیری‌های شبانه ناوشکن‌ها در تنگه هرمز، این تبادل آتش را تنها یک «سیلی از روی محبت» (Love tap) خواند و تاکید کرد که آتش‌بس شکننده منطقه همچنان برقرار است.
سلاحی که ترامپ به آن اشاره می‌کند،سامانه لیزری ضد پهپاد «لوکاست» (LOCUST) است که پیش‌تر اعلام شد بر روی ناو هواپیمابر «یواس‌اس جورج اچ.دبلیو. بوش» نصب و آزمایش شده است.
به گزارش وب‌سایت «وار زون»، این نخستین بار است که یک سلاح انرژی هدایت‌شده روی یک ناو هواپیمابر کلاس نیمیتز نصب می‌شود.
مقامات عالی‌رتبه نیروی دریایی اعلام کرده‌اند که هدف نهایی آن‌ها، تبدیل این سلاح‌های پیشرفته به گزینه اصلی مقابله با تهدیدات نزدیک در آب‌های بین‌المللی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/75334" target="_blank">📅 19:22 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75333">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z19hwt2WRTU4kW_j1OFcZ9oZxfIfCwEGpd2LRdaZocvWHjwS3bqdL1EUb3oVmNCvCiKWKPiynTex55L-e7-LqFLLvUdyVqhA6KGExQVObHYtRqGscvfMh0nT9OR62aQiNf8bag3yT2cfCDtwmJmm-OfFRUl6CcwAW7BqD7gWsOj6IPv01UHmyv0S5QUuByX4hqXfffrq4EpO1eV-mwbxJwTFo_yEbbRITIhQ-mLRDZOguGGy4XUBYZskNDA7FlGyC8rWrk1tiMSVdu9BYZ8ezyF44Xuhbx4K-Nqs5llRMhcYxIdEGleaALY_poUM8VYBzlwfouLkjhABsIhENXm--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندار میناب: حمله آمریکا به یک لنج باری یک کشته و چهار مفقود بر جا گذاشته است
فرماندار میناب می‌گوید که در حملات دیشب آمریکا یک لنج باری هدف قرار گرفته است که منجر به کشته شدن یک ملوان و مفقود شدن چهار نفر دیگر شده است. [گویا قبلا گفته بودند پنج مفقود داشته بعدا جسد یکیشون پیدا شد]
به گفته محمد رادمهر، ۱۰ ملوان دیگر این لنج هم مجروح و به بیمارستان منتقل شدند.
به گفته آقای رادمهر این حمله در نزدیکی آب‌های شهرستان میناب رخ داده است.
عملیات جستجو برای یافتن سایر مفقود‌شدگان ادامه دارد.
دیشب نیروهای ایرانی و آمریکایی در آب‌های جنوبی ایران تبادل آتش کردند، هرچند دونالد ترامپ می‌گوید که آتش‌بس همچنان برقرار است.
آمریکا می‌گوید که نیروهایش «بی‌مقدمه» هدف حمله موشک‌ها، پهپادها و قایق‌های تندرو ایران قرار گرفتند و ایران می‌گوید که حملاتش تلافی‌جویانه و در پاسخ به حمله آمریکا به یک نفتکش ایرانی و یک کشتی دیگر در منطقه تنگه هرمز بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75333" target="_blank">📅 19:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75328">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rZEjW3_ubkq14YAQtEIdiacglGUFyxMh8vrBaOdWMZUSnzxvIzx9U-X1t69hkspfy9HZKNSJd6ovRwiirig7r-H6HZGwmStNwIdoK_kfDNBV3mvK3TaydaGWb2lWdwwf2Fby6ksY0hrDFpj5ujM-6fI7bu1pjrAoHtx57MVgy_b5nXFm6K4W9HbkBCqX7plN3im8Pj0d30UZyl4uiuOZNxZILAHiDAQvlrew6yHHWw9FhkLxLoEaeR0VVOiQNDR-Gur_akzL1DmoLaaLlzZlLb6VbErWIqh-qDOVLOAiIe_WF1k401Rb077vW79nQJetiFEX1qWrWSco9XC6uLVe5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NpHCWaYzS7qE1QLGJvgt-cA5h89Im0-RcqqmDjrr3sNZO0DIRkf2A2rGeXsa3Cc8-sOQ1RdbTiAwDcpuqn7oQAGnRSvhmgA05JAsinrKNl0Kgx0W4Zmbh6H8RhRksDMffGCrSNm3rSArus1-1mnVhSE7KByplMYPLq7pz_6qsXoVjH_-EnXGv8dsW8etNn2K9XUvaKdfD1SurokE28EDaNAwH3qbhDJXi46uXzbyOfwAbfm8mpuA1uVlflKCRWF_-G8Q_55L9tOXYF_lz3sBO4waIRqCqlF_KibfC-VhA7wU6I-FjnhfAU92TJHOJupnCTciI-DgSuUtZ2CO102SmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ly80T9aQjhJnbwlLtDwV0CvnsbVaIoaGbOndgFDS24HU1DZxVc3846DiOKo8HsFPZhktI3Ssq31kRsCfhnap_IMLmTFUnE_HfOsJod-UazIpSt_7iB_XWSWLxWBpYCdc-fbLHukNXKKTmYxBnPccZhu-iPmxcPsJpS5IdUq91txXmgBnRxMkDVaYOgVULYm-xHwzgRmXTrMuENFzo_l6b67wW7nybwOV19nzNKftQ-o_Bg_ykQgbyfR2kuKkN4H0GPNFTOqQxLEh0O1xj_4v54Q3Xl6-MNBTNO_fi53WjS7VMqEJFXMLPTedbgvuycb1Qxa_tDh1Sk-a-nhhLoBgxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/858d7055f6.mp4?token=PNFW3HXUVSiEA_mM660dtK-j_G3I7-YYPiivxadqM6HkFqLy-jrFFDhUYiZBBmbwta677_vqaZzOrLdE4uh7maR5hcq5SJfXmWcDoM8_WLueM1YUBWSdACsNDmXice8XvTN99bUYpDQfRpKo_wowhy1MYBoYUhbt9i1xUH8yXM6Yr6SSsEPDcNetngn_1YhU8rsfULKzDBIo6LBnE7KslGVCNTDDK10c-bYu_w5ojTp6mCqT_Xrc9eyRYqBO6fWOM1cN1bUv0BdyukFLXg7A3fnH4rAtM_6MR8s40izPO4XhxAbaiu3AzUkpCZ28Ek-Du683r5M4yl1bcHvAKSV76w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/858d7055f6.mp4?token=PNFW3HXUVSiEA_mM660dtK-j_G3I7-YYPiivxadqM6HkFqLy-jrFFDhUYiZBBmbwta677_vqaZzOrLdE4uh7maR5hcq5SJfXmWcDoM8_WLueM1YUBWSdACsNDmXice8XvTN99bUYpDQfRpKo_wowhy1MYBoYUhbt9i1xUH8yXM6Yr6SSsEPDcNetngn_1YhU8rsfULKzDBIo6LBnE7KslGVCNTDDK10c-bYu_w5ojTp6mCqT_Xrc9eyRYqBO6fWOM1cN1bUv0BdyukFLXg7A3fnH4rAtM_6MR8s40izPO4XhxAbaiu3AzUkpCZ28Ek-Du683r5M4yl1bcHvAKSV76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، گفت اقدام نظامی آمریکا علیه ایران در بامداد جمعه «جدا و متمایز» از عملیات «خشم حماسی» بوده و ایالات متحده همچنان به‌صورت «دفاعی» واکنش نشان خواهد داد.
روبیو روز جمعه در شهر رم، پایتخت ایتالیا، در جمع خبرنگاران اعلام کرد «خشم حماسی» که او اوایل این هفته گفته بود به پایان رسیده است، «یک عملیات تهاجمی بود که برای نابودی سکوهای پرتاب موشک، نیروی دریایی و نیروی هوایی آن‌ها طراحی شده بود.»
او افزود آنچه ساعاتی پیش رخ داد «ناوشکن‌های آمریکایی بودند که در آب‌های بین‌المللی در حال حرکت بودند و از سوی ایرانی‌ها به آن‌ها شلیک شد، و آمریکا برای حفاظت از خود به‌صورت دفاعی پاسخ داد.»
دیپلمات ارشد آمریکا گفت: «فقط کشورهای احمق وقتی به آن‌ها شلیک می‌شود، پاسخ نمی‌دهند. و ما کشور احمقی نیستیم.»
وقتی از روبیو پرسیده شد که آیا آمریکا خطوط قرمزی را به ایران منتقل کرده است یا نه، پاسخ داد: «خط قرمز روشن است: اگر آمریکایی‌ها را تهدید کنند، نابود خواهند شد.»
وزیر خارجه آمریکا همچنین خبر داد که واشینگتن انتظار دارد روز جمعه پاسخ ایران به پیشنهاد واشینگتن برای پایان دادن به جنگ را دریافت کند.
روبیو در این زمینه توضیح داد: «خواهیم دید که این پاسخ شامل چه چیزهایی است. امید ما این است که چیزی باشد که بتواند ما را وارد یک روند جدی مذاکره کند.»
او همچنین تلاش‌های ایران برای کنترل تنگه هرمز را محکوم کرد و گفت: «ایران اکنون ادعا می‌کند که مالک این آبراه بین‌المللی است و حق کنترل آن را دارد... این اقدامی غیرقابل قبول است که آن‌ها تلاش دارند آن را عادی جلوه دهند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/75328" target="_blank">📅 19:18 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75327">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXjTV4V8lOwt8J60tMGnHNViiihrqglDeDsA90nhuTSi1Nwa5XtZorhVzn1IoQl7TZQUiGDXYYHRz9KDQc0vgSdXkGye31S81AtqMA7nvPYk6HROMmWDPmRRC3Mb4OiQyPy8aty_TiKRpyWsRPw6p7O6JO46VMwcyXVfqMtNFq7oERtGvQ4qwVnFbA8FZ9GYW8Bfh31hJaTG20UPQyDcDjRTSQserQZV2fYT97bklIW-RbFIjNJgWTNpHJnlMVHJC0f9avx8ZzT08ru_gqTV1hYnohHk4bikqOmXcnLpcKY-fmNnz2uPwpk4acffzDrN1Ufu7gyFZNWFxjcCWAf7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه جمهوری اسلامی، آمریکا را متهم کرد که با «ماجراجویی نظامی بی‌خردانه» دیپلماسی «قربانی» می‌کند.
عباس عراقچی در پستی در شبکه اجتماعی ایکس نوشت: «هر زمان که یک راه‌ حل دیپلماتیک روی میز قرار می گیرد، ایالات متحده به‌ یک ماجراجویی نظامی بی‌خردانه رو می‌آورد.»
آقای عراقچی در ادامه می‌نویسد که دلیل این اقدام چه «صرفاً یک تاکتیک کور برای اعمال فشار» باشد و چه «فریبکاری یک خرابکار» که می‌خواهد «رئیس‌جمهور آمریکا را به باتلاقی تازه بکشاند» و یا هر دلیل دیگری «نتیجه همیشه یکی است: ایرانیان هرگز در برابر فشار سر خم نمی‌کنند، ولی این دیپلماسی است که همواره قربانی می‌شود.»
او همچنین ارزیابی سازمان اطلاعات مرکزی آمریکا از ذخایر موشکی ایران را اشتباه توصیف کرد و نوشت: «ذخایر موشکی و ظرفیت پرتابگرهای ما نسبت به ۹ اسفند در سطح ۷۵ درصد نیست؛ رقم صحیح ۱۲۰ درصد است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/75327" target="_blank">📅 19:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75326">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urcrxy2GG7R8q6Zk3dRSU31xYWBp5QdXQZsm3u3wAPhkAQE7MI3M9gRiJOzSfZBSkAAhQRgMW-E_cLB5fxDMETfIA4obyoNdsvarjc1h_GlSNGjokoL43xew63A2p4bwQyU-hUvxN8CdI8pHz3HI85CQxeVgbyHewRfreVHcXOOdbWKkgMtNAbGe-dBbW4z-vc3QIXQ1dSy8P3fxu06TCD_nd0nNdYO22cx6lkRA0H70CD6VSF7oG5fTv3ucvS3GfqmvWtJI9moj01Jh9jr3HWcuIbD0_eu-LY35l93-hFvZ_RfwjfgVpAdT3XVI0pc-R__MpfksI1VtHbPwIDuEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام، فرماندهی مرکزی ایالات متحده، اعلام کرد از زمان آغاز محاصره دریایی تا روز جمعه، ۱۸ اردیبهشت مانع از ورود یا خروج بیش از ۷۰ نفتکش از بنادر ایران شده است.
سنتکام در پیام تازه‌اش در شبکه اجتماعی ایکس نوشته که این کشتی‌های تجاری ظرفیت حمل بیش از ۱۶۶ میلیون بشکه نفت ایران به ارزش تخمینی بیش از ۱۳ میلیارد دلار را دارند.
این موضوع ساعاتی پس از آن اعلام شد که ارتش آمریکا گفت نیروهایش در نخستین ساعات بامداد جمعه حملات «تحریک‌نشدهٔ» ایران علیه ناوشکن‌های آمریکایی در تنگه هرمز را رهگیری کرده و در پاسخ، «تأسیسات نظامی ایران» را هدف قرار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75326" target="_blank">📅 19:10 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75325">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1KBbJjcm93W-UP-RocTuCpBwfidOd69fc16UeFI2lZ6UpUQw51VZl5deBPX6wksovhcxT4oNHR_IfLt4s9Uls8qcsRJlLVEsHLXlLIdkXThvO2VCznZlN5eXbEsOw3WRIHnTwgnO5lIi7uCCyeK9zSihRfMGCQVGLGiPow7rF2A2cQVgLCZ_RKU35vQMUp5ykgP64w0ATPGsXFjWvjjwO0Txq-DxDgkBd7fEgsV18t5wkxwHLYvbODUIoGwfX4StkejwyC34MDx-DfepkG9aGDqlB3Y9HZPg7c2BP5R6w-kYi5nZsemWoBpDV3b0nk3TLn6tEJbXCYxNm737ii1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز هفتادمین روز قطع اینترنت در ایران است و به‌گزارش نت‌بلاکس این اختلال صبح جمعه ۱۸ اردیبهشت از یک هزار ۶۵۶ ساعت فراتر رفت.
این در حالی است که مقامات و افراد نزدیک به حکومت یا کسانی که حکومت خود با واگذاری «سیم‌کارت سفید» انتخاب می‌کند، هم‌چنان به اینترنت دسترسی دارند.
علاوه بر آن، اخیراً برخی اپارتورهای نیز اینترنت موسوم به طبقاتی را باقیمت‌های گزاف در اختیار برخی مشاغل و طبقات قرار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75325" target="_blank">📅 19:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75324">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scgLsjI6STNaDO80SOlzZ5QGQ4Wp-7yMI6ism1BQUIJAdNDzWglBlSBkRW3iy9GgcwXlFCtUmaZ7vUj5uw7HrBlqgqZSbhCQ_moM6G-RffGnusX6ORKZZM_ePfX_01z_djKSTXjO-4zJuZTpMdfBiFHE-OpLRe-YkJfYdJo3mYnDBW7u1g6WB2mjCtaKr7917awj2jH7ceg2hvm7wx1AW-z92Q8J7LGwt6mTiqGRwzantmSnhmERRi7-gYzuvEJKnJrELnlprTN45z6GKJzoPOV06ytPj6B_Q5f5usIbx4fea6nipsjtQeqfNsTk3GDc3Y_jMdvZZQkENTZf9pCaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز جمعه ۱۸ اردیبهشت و پس از حملات متقابل در خلیج فارس، تنگه هرمز و انتشار گزارش‌ها از مقابله پدافند امارات متحده با موشک‌ها و پهپادها، پیامی «تهدیدآمیز» به زبان عربی منتشر کرد.
بقایی در این پیام نوشت: «اگر دندان‌های شیر را دیدی که بیرون زده‌اند، تصور نکن که شیر لبخند می‌زند.»
به نظر می‌رسد با توجه به حملات روزهای گذشته به بندر فجیره و دیگر نقاط امارات و اتهام‌های قرارگاه خاتم‌الانبیا پس از درگیری در تنگه هرمز، بقایی با این پیام امارات متحده عربی را تهدید کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/75324" target="_blank">📅 09:38 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75323">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WOb2v--emzuwv-zRL888Y8xIPb1WC0wq-4fz0Yvqd2kO6vnZ5SHMMzQpbIiFWVhoHMpTUGk6KaVEu23l2d6p6UyktRQK1gQOcB9-nQ3KOns5JL5voELu4LTovqr5JO5qjVORvp2nJv8WKJB6csMUPP9z2lxHi7HzNHzAuNHm1FqaaAGVA3rVhWlqWjZ0e5XlSu6RCYCSuw2uGL4d0ww1-3ocnQheiLMMVfeY8VyowpHdfH-0xiBStFEdFk2uIXZ4tzdf8SN502oDOFa8loYcxny-WdVnN3j3ZxFXDzZf9_gM1izpKh7BYjxLC_KumnaWsPCOOxbpRrqKo5wKKhwz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی اوایل روز جمعه اعلام کرد که سامانه‌های پدافند هوایی آن در حال مقابله با حملات پهپادی و موشکی از ایران هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75323" target="_blank">📅 06:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75315">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cmLddrDRN7rihSwOXYcREin8QQfrN_fyBkxmDkcYLdpaHNirMis8whQB7ImviKoEMWIk8L85r2Q2dExhzk4rfCa2QyqMdVFXMwYWqMubQO9PTyllVUWDgIg2qeSS3kwqp9eg77Mcu5Z62EdfEsjIzfzhG1Ro_XTl-HIzaiNIU9Sm2LpuLmMyNlyi_CHAnsJ0BVRrnrqaWxzPM1-uHOyd076tWO2zz6W4ssq5gvtFaggz5U3uGxf-2iBaORXXxf8sPll1OrVtoEapelHCpwQsC0f8zRwyFM9tYC5im1tn5yVT39sMG8p-VSD0EwBNpvjzQChyN72CN9z_Z2J0aIbqMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cg8Ij86DG7FLProAFiR4uqD4v-kfxNupkmxCKbzVyDw9ckw_ssJKiTRqx5HwJhmYuQ_PXjiMbRwzorwcwicfx5YJPKv7_hJW_TU7MzHWBx0GdKICWQl6kfupmYtPhBtKE15ukkHknUNn2owHTw7AdaYytFx9L34iZbUB-hIpXwYZ7OA8BkEMUP_7ni68mR4Dt6hzf1r7_6Te6dEfN0o3fppnqolsBGPHtnn8dYiFEUBN7sr2xkaA6RAYTrk8sYlQV91lS9H7YCcyUOa03OdtkIJJr5gZXMQsgoTaKchaolGXApv9m78KInFGLljLTz4c4_N08u080c9Wcwqhcjcuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kxKEZynwcAnILrL_gTW72lYU29eOxIUtes3B9XLszVQnMSoKiM3qMrk3m_br1vJN1N7UNZk-xHv2DQnVBRxNF6TMyz3-fD2pLvb_wliyX27lB-3XVUpUhl9ZkyVZKCGnxvvLC83bjAYyapgWC3Rad7ZYPJYbZsosH5Xqe1srGPo_8FwuXASqdRfYO_nHIH2p82MK913w2Eg1zk8Yf5E1GKNMUg4GwG0s_KukEVnLGchUWSFKnMHnaY3WZHgeD1DB5bR4DWjE7tBFGwnbCRKzIQFCty7nvAiFFzbJ7LxDL7ca9SNSSKmdTFmzf3hiagtwWM0QawRTay9PaJX5V8wcaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NaG28Mx8S46-nAFiR9B5Wp17zDnpcs_XKnu7g4a1F8TWKZnBFoJW6UT4pM3_2aKGu0Nm-_lXo8ioyZ3-ywG82kFIlPNHhheznbGrUEUfzSnRLG9fIYqz2qfAaU9I3ctAVvQQOsJU4PLiMmSWsNAFR7bCXtJS3yS-ynSi8slAWJIMiWLb63hSnIa7qSv6lDSrVKgic1tbG04lwSQMxKPAmHCRB6tYMGN_CBbY7VvMEDwXSyVfPnCB2jSRRAK5pJxgMrZqE1Chr5c4WMkwTZC-n6Y0EKe610tFTKC3NWddSfeGI50TsYCS_GoM1AhFbl9I3sQiVNVPxJAUP69ybQZ5GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AG83VgXBPXxnzapL8hOMTkRAtdm_Excu_frXamAaGCgdFU607VXVif2HvuylUSCvBPM-TO50i4OjwOwgKZLCKVpUwp1nFIuBspkZzqGZOxL_Q_epZw48KI_bmro2iM5rfY0Kr-fRtQVbKPrBQUNvI-cC_p2zuHVw4BoAn8IdSX4FcjGXPFY3Mu_w3VnZvRSP8qTY4u4fDx2RDAvGxfLK7HwqtxsDiX1HbH6B2Oge8rpoCMqQM1DqHAjhLH85Pi-4OuKC4YzDbaPz1fED1uOtqLp2Z_u5biM4Dh_uOVM_x_F0Vf_j4HdK-kLpXC-gSksCcqsEw-XJl2qP0fgCWGXeWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qjUvhsXj1ABKFz57dpZ-YgUUFLoFgoC8EYao0-6dPqOI4o3JjH-QuJwRS8qDRF4VC713xmvGM0wPD6GnbjnGA0hNImlfjnq6PcqW8pSzyVsWXz6kLmkRJyMVswH-1g4p8rd4ioV8XT6csLqHPfFhGqBbgdPwo0EQyFRrp8rWay_RXFfVVq044oAlEg-fdxyt8H_CG_PW9mshCBzLdXoexTjODP_pMiKBJjeGxsk6yyaq8Xds1iwC474XXwLvRCpr9ORcDOkdtvuQw6xrsddNx-vwRMCA4BJNbcf6-VeJ8CE-UUtZElfyPzmEU1HF0r-YKIHwKXu7rtgLjqNWL-jVOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e24b568a6c.mp4?token=BE0uvXp-2HfIu8cqzy8uC3FFuvIVj_qQVVwVNOwpa2z9kwrwk-jV-1Egpmzvu85VQGI60q4n8zTNr45HrUP5OAzvwuz1PIrAlsGe5NaZETXsCAAKGmuZI2yceHFv7EmxIG3LFQvJ0baFreCNVLiiwoT9XGGgxOhIFjk9cUGyGb309qZmML1QZRi-iVrbWvrwShRucAj-3PLCprzAfePFOs_ay0G3EtzyPM8WNQxs1hntuQl7AluNpaMoYY_Wy2MCxX0v_Y--SUCgba9RAMTzTlkDqiGwUpquLA7y0heNEKRNlb6ZKVj3VKY4TU8eVXzbrH05mW6np4dhfxIV0iZ_hw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e24b568a6c.mp4?token=BE0uvXp-2HfIu8cqzy8uC3FFuvIVj_qQVVwVNOwpa2z9kwrwk-jV-1Egpmzvu85VQGI60q4n8zTNr45HrUP5OAzvwuz1PIrAlsGe5NaZETXsCAAKGmuZI2yceHFv7EmxIG3LFQvJ0baFreCNVLiiwoT9XGGgxOhIFjk9cUGyGb309qZmML1QZRi-iVrbWvrwShRucAj-3PLCprzAfePFOs_ay0G3EtzyPM8WNQxs1hntuQl7AluNpaMoYY_Wy2MCxX0v_Y--SUCgba9RAMTzTlkDqiGwUpquLA7y0heNEKRNlb6ZKVj3VKY4TU8eVXzbrH05mW6np4dhfxIV0iZ_hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در گفت‌وگو با خبرنگاران در واشینگتن، با اشاره به درگیری جدید آمریکا و جمهوری اسلامی در تنگه هرمز گفت نیروهای جمهوری اسلامی با آمریکا «شوخی» کردند، اما آن‌ها ظرف حدود دو دقیقه نابود شدند.
او گفت: «امروز سه ناوشکن درجه‌یک آمریکا از تنگه عبور کردند. هر کشور دیگری در چنین شرایطی چنین کاری نمی‌کرد. به آن‌ ناوشکن‌ها موشک و پهپاد شلیک کردند و این قایق‌های احمقانه را به سویشان فرستادند. آن‌ها ظرف حدود دو دقیقه نابود شدند. نفتکششان هدف قرار گرفت. می‌دانید با نفتکش چه کردیم؟ نمی‌خواستیم شرایط حادی ایجاد شود، بنابراین سکان آن را زدیم و نفتکش شروع کرد به چرخیدن دور خودش. نباید امروز این کار را می‌کردند.»
ترامپ افزود: «همه موشک‌هایشان سرنگون شد. همه پهپادهایشان سرنگون شد و کسانی که آن‌ها را شلیک کردند نیز دیگر در میان ما نیستند.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه گفت پیشنهاد واشنگتن برای پایان دادن به درگیری با ایران، بسیار فراتر از یک «پیشنهاد یک‌صفحه‌ای» بوده است. سی‌ان‌ان نوشت، تهران همچنان در حال بررسی پیام‌های ارسال‌شده از سوی آمریکا از طریق میانجی‌های پاکستان است.
ترامپ در پاسخ به پرسشی درباره اینکه آیا ایران به آنچه «پیشنهاد یک‌صفحه‌ای» توصیف شده پاسخ داده است یا نه، این توصیف را رد کرد.
او به خبرنگاران گفت: «خب، این بیشتر از یک پیشنهاد یک‌صفحه‌ای است. این پیشنهادی بود که اساسا می‌گفت آنها سلاح هسته‌ای نخواهند داشت، گردوغبار هسته‌ای را به ما تحویل خواهند داد و بسیاری چیزهای دیگری را که ما می‌خواهیم.»
وقتی از او پرسیده شد آیا ایران با این شروط موافقت کرده است، ترامپ گفت: «آنها موافقت کرده‌اند. اما وقتی موافقت می‌کنند، خیلی معنا ندارد، چون روز بعد فراموش می‌کنند که موافقت کرده بودند.»
او افزود: «و می‌دانید، ما با مجموعه‌های متفاوتی از رهبران طرف هستیم.»
@
VahidOOnLine
ترامپ در واشینگتن به خبرنگاران گفت: «مقام‌های ایران بهتر است خیلی سریع توافقشان را امضا کنند. مذاکرات بسیار خوب پیش می‌رود، اما باید بفهمند اگر امضا نشود، درد زیادی خواهند داشت. آن‌ها خیلی بیشتر از من می‌خواهند امضا کنند.»
ترامپ گفت: «ما اکنون در ایران با مجموعه‌های متفاوتی از رهبران سروکار داریم. وقتی درباره تغییر حکومت صحبت می‌کنید، آن‌ها مدام از تغییر حکومت حرف می‌زنند. ما حکومت اول را کنار زدیم. حکومت دوم را کنار زدیم. بیشتر حکومت سوم را کنار زدیم. بعد می‌گویند آیا این تغییر حکومت است؟ من فکر می‌کنم این نهایت تغییر حکومت است.»
@
VahidOOnLine
دونالد ترامپ عصر پنج‌شنبه گفت: «ما هرگز اجازه نخواهیم داد» جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند. آقای ترامپ گفت: «احتمال آن صفر است. خودشان هم این را می‌دانند و با آن موافقت کرده‌اند. حالا باید ببینیم آیا حاضرند توافق را امضا کنند یا نه.»
@
VahidHeadline
ترامپ پنج‌شنبه به خبرنگاران گفت آمریکا با وجود تازه‌ترین تبادل آتش با جمهوری‌اسلامی در نزدیکی تنگه هرمز، در حال مذاکره با حکومت ایران است و افزود پاکستان از واشینگتن خواسته است در طول این گفت‌وگوها، طرح او برای اسکورت کشتی‌ها به خارج از این آبراه را دنبال نکند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/75315" target="_blank">📅 06:17 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75314">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bsAkIsSoTWCia4PGH9KL6RtfZlzwezAtrIgyiMyE_g7TJm64mxnooN3oiMMjnVMNu-ioUOUHO2QKj4VKULsYFXqO1TKa-1Vl32juXYhjG8Cczfx7ZtDP0WavoVbluaMDdTAnVpfLIin2sbZaDBBpfDzUSGUAV3raXlWTwlFQhN_Hem0X5QNvJ0xY4NXMSt9sq7PFTqnBejRdRxpIfmlecpCJj43ZnzAcvE3NCmZSocqbcoVQ9lGrcdq4lm8ieNuxKfzDHnmqJxPRlBwPFh05_IFtsnO4vrencS0VyGHHcrYUvX2tVDH7wZzlv3Lz2SWEIli6Gt8lyNVQDxa6fbvfqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران را دیوانگان هدایت می‌کنند
پست ترامپ، ترجمه ماشین:
سه ناوشکن درجه‌یک آمریکایی به‌تازگی، با موفقیت کامل و در حالی که زیر آتش بودند، از تنگه هرمز خارج شدند. هیچ آسیبی به این سه ناوشکن وارد نشد، اما به مهاجمان ایرانی آسیب سنگینی وارد شد. آن‌ها به‌طور کامل نابود شدند، همراه با شمار زیادی قایق کوچک که اکنون برای جایگزینی نیروی دریایی کاملاً از سر بریده‌شده‌شان استفاده می‌شوند. این قایق‌ها به‌سرعت و با کارایی کامل به قعر دریا رفتند.
به‌سوی ناوشکن‌های ما موشک شلیک شد و به‌راحتی سرنگون شدند. پهپادها نیز آمدند و در هوا سوزانده شدند. آن‌ها به‌شکلی بسیار زیبا به سوی اقیانوس سقوط کردند؛ درست مانند پروانه‌ای که به سوی گور خود فرو می‌افتد!
یک کشور عادی اجازه می‌داد این ناوشکن‌ها عبور کنند، اما ایران یک کشور عادی نیست. آن‌ها را دیوانگانی هدایت می‌کنند و اگر فرصت استفاده از سلاح هسته‌ای را داشتند، بی‌تردید این کار را می‌کردند — اما هرگز چنین فرصتی نخواهند داشت و همان‌طور که امروز دوباره آن‌ها را از پا درآوردیم، اگر توافق خود را سریع امضا نکنند، در آینده بسیار سخت‌تر و بسیار خشن‌تر آن‌ها را از پا درخواهیم آورد!
سه ناوشکن ما، همراه با خدمه فوق‌العاده‌شان، اکنون دوباره به محاصره دریایی ما خواهند پیوست؛ محاصره‌ای که واقعاً یک «دیوار فولادین» است.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/75314" target="_blank">📅 02:19 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75313">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qec3sNKrZCzo5qpbCyT0CY60sej19zPUACuhw7NDgJqPdEyuEn9ZAxpRIoh-85DBuYX7VMGXOSpurF8TxnNSrdwXqw00TDzRA3wX-NXv0hdIimLpN88EyzvKf46GHyxDYA3liD98LVVL2tGY5UZys9-HWGM7OMK8_Vi2MEqG9hGA-p335BrEuDnGJCTzoq1skoqbkILx9Kljr7mxFwswngrXk_p2tbJ5SuS_jhTenl5OEOBsA6JaeRzt0L4OqZficnzlDOvv35ks4mk21ulCN1xK7Z_6p0neYtCj5Adfb5iJ6VINZzz5PcEOYugWN0rkx-WfK7H7ZyfIaMJZbJa5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا در پی حمله‌ها به بنادر جنوبی ایران و شنیده شدن صدای انفجار در غرب تهران به ای‌بی‌سی گفت که ارتش آمریکا در اقدامی دفاعی به رژیم ایران یک «نوازش دوستانه» داده است و آتش‌بس همچنان در حال اجراست. او گفت حمله‌های متقابل به ایران فقط یک نوازش دوستانه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/75313" target="_blank">📅 02:14 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75312">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_Y3IUa9nkR0SxhDW5euYq3aMQn8Jzi--byYZRK7ZMWVeo-E9YotcdDUedXVHGQ3YVUemMqrAmG85ORddIISHk9K63hKGRXJqsmtsVlthmcN9uMZFCi1k7Ytcm4hEKc7FnxDnp3PVqrkXJdjyP9pQnm6e0Te69U-iyOnJMENetRunFNACnkm0QJBEWQR7Ed0g4OtocOQqyERnp3wMfuOUqvosWPE3VdcWcX4vqqyP6PpAGtyIjOMmq5CEx5MCa7A2f3AhAIDKa4CnVY5G5wEuguc3_K4xCK6ekEZYMZ9XLkSRApt4ry29EjeZulKy3bv2U-MrJPER4giag7x7X_c4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنیفر گریفین، خبرنگار فاکس‌نیوز، در شبکه اجتماعی اکس به نقل از یک مقام ارشد ایالات متحده از حملات نظامی این کشور به بندر قشم و بندرعباس خبر داد. این مقام آمریکایی تاکید کرد که این اقدام به معنای شروع دوباره جنگ یا پایان آتش‌بس نیست. این حملات دو روز پس از شلیک موشک‌های بالستیک ایران به بندر فجیره امارات صورت می‌گیرد. گزارش‌ها همچنین از حمله به ایستگاه بازرسی دریایی بندر کرگان در میناب حکایت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75312" target="_blank">📅 01:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75311">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSBFuPP39ozFI8calART6vBRyquiVz-uxq2CcH-5S1HKhrG0suMVWClBierQASftiGr5ZVXMFfSCirqaBH90Dv1dOYwC1iOtvRuDMAE65UNZ-AOT3y-QXlUq0kpZq8g2qlhV9w4ahv1I3lE6siLRuwIglIwW18EZa-UGBjemmHT65Z7NeKCvQxELVPx_WTZ6cjWrv6UZO0-xBxNSun3aPyJGsTRmTh9xjWYDmsN9FOHo4tF79p_18AsnC3OjWsZ8AjhseWWSNUEsmIsWDjDvDJ2uD523bu5kOXCCwFjHPgeIKuioGTC3VXP0ELadBPunm_rmBTjtrBmnzW46Cq6MPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، سنتکام، اعلام کرد نیروهای آمریکایی ۱۷ اردیبهشت همزمان با عبور ناوشکن‌های مجهز به موشک هدایت‌شونده آمریکا از تنگه هرمز به سوی دریای عمان، حملات موشکی، پهپادی و قایق‌های کوچک جمهوری اسلامی را رهگیری و به منابع این حمله‌ها در ایران حمله کردند.
طبق اعلام سنتکام، نیروهای جمهوری اسلامی در حالی این حمله‌ها را با چندین موشک، پهپاد و قایق‌های کوچک انجام دادند که ناوهای یواس‌اس تراکستون، یواس‌اس رافائل پرالتا و یواس‌اس میسون از این گذرگاه بین‌المللی دریایی عبور می‌کردند و هیچ‌یک از تجهیزات یا دارایی‌های آمریکا هدف قرار نگرفت.
سنتکام گفت نیروهای آمریکا ضمن دفع این تهدیدها، تاسیسات نظامی ایران را که مسئول حمله به نیروهای آمریکایی بودند، از جمله محل‌های پرتاب موشک و پهپاد، مراکز فرماندهی و کنترل و گره‌های اطلاعاتی، نظارتی و شناسایی، هدف قرار دادند.
سنتکام تاکید کرد که به دنبال تشدید تنش نیست، اما همچنان در موقعیت مناسب قرار دارد و آماده حفاظت از نیروهای آمریکایی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75311" target="_blank">📅 01:25 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75310">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b377a19a19.mp4?token=bXXGId_t39kn5WhMyFogdfse0S1Xo8mfUyr0-h7a2LPnIFbpNR-9o1wOu1WENOXMs1cZ3eoq8FABWE1gmLOPngBDwfoSbtT81a_rjD-ysCzlLPg7Ny5G0CWv4mSsL7G7kp0LZDYi5eBJpxFjUIRKygKkV-Z5nMmcWq46JAsPhXNlV9rsxIwTc33t2lSSyw_Gf6ZckB_C51ANPZAX9tPiXqfvDYsILDE0ULI9P_ExOmpSm-B15gr_GI4lGMJlVlKzghkAGBlz_Z0Vc8YV2A7zg0fQYL8uAou1ZYaYFwUPt-5kprYIS2Q16rFa_pvr33gKZAGc92qWhS4bpM2e8tBdEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b377a19a19.mp4?token=bXXGId_t39kn5WhMyFogdfse0S1Xo8mfUyr0-h7a2LPnIFbpNR-9o1wOu1WENOXMs1cZ3eoq8FABWE1gmLOPngBDwfoSbtT81a_rjD-ysCzlLPg7Ny5G0CWv4mSsL7G7kp0LZDYi5eBJpxFjUIRKygKkV-Z5nMmcWq46JAsPhXNlV9rsxIwTc33t2lSSyw_Gf6ZckB_C51ANPZAX9tPiXqfvDYsILDE0ULI9P_ExOmpSm-B15gr_GI4lGMJlVlKzghkAGBlz_Z0Vc8YV2A7zg0fQYL8uAou1ZYaYFwUPt-5kprYIS2Q16rFa_pvr33gKZAGc92qWhS4bpM2e8tBdEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرارگاه خاتم النبیاء که مدیریت جنگ در ایران را بر عهده دارد، ساعتی بعد از گزارش‌ها از حملات و رد و بدل شدن آتش در حوالی تنگه هرمز، با انتشار بیانیه‌ای این حملات را «نقض اتش‌بس» و در پی «همکاری چند کشور منطقه با آمریکا» ارزیابی کرده و گفته است: «ارتش متجاوز، تروریست و راهزن آمریکا با نقض آتش‌بس یک کشتی نفتکش ایرانی و در حال حرکت از آبهای ساحلی ایران در منطقه جاسک به سمت تنگه هرمز و همچنین یک کشتی دیگر در حال ورود به تنگه هرمز را روبروی بندر فجیره امارات مورد هدف قرار دادند و همزمان مناطق غیرنظامی را با همکاری برخی از کشورهای منطقه در سواحل بندر خمیر، سیریک و جزیره قشم مورد تعرض هوایی خود قرار دادند.»
این قرارگاه در ادامه مدعی شده که نیروهای نظامی ایران به این حملات واکنش نشان داده‌اند: «نیروهای مسلح جمهوری اسلامی ایران نیز بلافاصله و در اقدامی متقابل شناورهای نظامی آمریکا در شرق تنگه هرمز و جنوب بندر چابهار را مورد هجوم قرار داده و خسارات قابل توجهی به‌ آنها وارد نمودند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75310" target="_blank">📅 01:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75309">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuN5JtNdN7aJDdY9Mk70DqRgeICwiz9wb6qYi8dy1FhzAHgPHKkcgBjKa04gZPD3DPCy9lRhPvlQLhMBNeCVP1n3iaeGKFDXmcoBcNdWeU1G6_VQ_e9-kX6mB52MTvmzodkmC3uSZQvCnkqK_xB1-xnu1oGV-qYXRkIahIpCDiYYhmc7km-HK2y3ZCaaiufNSTYfjS8Sb8A4jpmCyAvaHYSaTXdLC72F76jMEbqkzcoSw1U35Oj00rkaIX1VxB6OhQzYbcABvWq-zUo25VPtBbmdPb5zgQGKHC9_jFNOfqPlwZIRTMIjQaVQ1ytKVwvusrWMprBmZzmmS-MEjEXDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا پیام دریافتی پست قبل درست بود:
خبرگزاری مهر بامداد جمعه ۱۸ اردیبهشت‌ماه به نقل از محمد رادمهر، معاون استاندار و فرماندار ویژه میناب، گزارش داد یک پایگاه دریابانی در این شهرستان هدف حمله قرار گرفته است.
به گفته رادمهر، این حمله ساعت ۰۰:۱۰ توسط اسرائیل و آمریکا انجام شده است.
همزمان فاکس‌نیوز گزارش داد آمریکا حملاتی را به جزیره قشم و بندرعباس در جنوب ایران انجام داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75309" target="_blank">📅 01:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75308">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هرمزگان
پیام‌های دریافتی:
وحید بندر صدای انفجار اومد الان
الان ساعت دوازده شب صدای دو انفجار دیگه در بندرعباس شنیده شد
همین الان بندرعباس صدای انفجار اومد
سلام بندرعباس ۰۰:۰۰ یک صدا اومد
۰۰:۰۲ بامداد جمعه ۱۸ اردیبهشت صدای تک انفجار این دفعه از فاصله بسیار دورتر ظاهرا از مناطقی در نزدیکی جزیره لارک یا هرمز بود.
خودم همچنان در همین محدوده نزدیک اسکله بهمن، محله دوحه و چابهار هستم
👈
پاسگاه بندرکرگان در میناب استان هرمزگان مورد اصابت موشک آمریکایی قرار گرفت.
پاسگاه دریایی است. می‌گفتند پهپاد از همین نقطه بلند شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/75308" target="_blank">📅 00:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75307">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/95a8a7b0ee.mp4?token=gyfaH-kZYW4nIApfMiM_0AATPs9zS3MpV15Tt5kuJ_WlEBgJ8-q9H_MDOFHlFJbY_bGCGeMdW67LVD-PAPzm0GzOyVERhITc2Yox2e2ubdSC3bllzqapfCChuQ9jyxrYbVKRDaSEuDfpaSk0H4AErIHPb6ihCbsknyAFZ2AurSUstrlJ5dEfEmSlTpcIgySvKiD42ov-7X8Ihk-RZppEhAwHyfsbgfwS3Myrb_XLEFgF9ThPgiwgObnoEFhdJgc7K6LYm6KKOeG6ez2hrtXTgPIxUezcWOPWidrpv7naE8MUoj_fmKmRK_k8G06FJLRZZo6szJo9cXh42Es_gcFgAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/95a8a7b0ee.mp4?token=gyfaH-kZYW4nIApfMiM_0AATPs9zS3MpV15Tt5kuJ_WlEBgJ8-q9H_MDOFHlFJbY_bGCGeMdW67LVD-PAPzm0GzOyVERhITc2Yox2e2ubdSC3bllzqapfCChuQ9jyxrYbVKRDaSEuDfpaSk0H4AErIHPb6ihCbsknyAFZ2AurSUstrlJ5dEfEmSlTpcIgySvKiD42ov-7X8Ihk-RZppEhAwHyfsbgfwS3Myrb_XLEFgF9ThPgiwgObnoEFhdJgc7K6LYm6KKOeG6ez2hrtXTgPIxUezcWOPWidrpv7naE8MUoj_fmKmRK_k8G06FJLRZZo6szJo9cXh42Es_gcFgAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو و پیام‌های دریافتی:
وحید جان سلام ۲۳:۵۳ غرب تهران فعالیت پدافند
غرب تهران نمی‌فهمم صدای پدافنده یا انفجار ۱۱:۵۳
سلام غرب تهران چنتا صدای انفجار و پدافند ۲۳:۵۲
صدا ها مرتب و پشت سر هم نیست
وحید من غرب تهرانم، ازادی. ساعت ۱۱:۵۳ صدای انفجار دور میاد
چندتا پشت هم
ساعت ۲۳:۵۰ امشب ۱۷ اردیبهشت صدای انفجار یا پدافند محدوده غرب تهران.
۱۱:۵۳ تهران شهرک اکباتان ۴ افنجار دور شنیده شد
مطمعنم صدا پدافند نبود انفجار دور بود
۱۱:۵۴ صدای پدافند به صدای انفجار ها اضافه شد شهرک اکباتان
ساعت 23:53، ممتد صدهای پدافند و مشابه انفجار باغ فیض غرب تهران
صدای چندین انفجار الان سمت شهران ۲۳:۵۴
سلام ساعت ۲۳:۵۲ دقیقه صدای چندین وحشتناک انفجار  سمت غرب تهران شهران
پدافند غرب تهران داره میزنه
از غرب، جنت اباد نمی دونم پدافندها فعال شده یا داره می زنه
غرب تهران بلوار فردوس ساعت ۱۱:۵۴
صداهای متعدد میاد
شبیه پدافند
صدای انفجار و پدافند
جنت آباد ساعت 1154 شب
امشب
سلام وحید همین الان دوتا صدای انفجار اومد سمت بلوار  فردوس غرب صدای پندافند هم میاد به شدت
چند تا صدای انفجار و پدافند میاد سمت غرب
منطقه ۵ ساعت ۱۱:۵۲ دقیقه
بلوار فردوس شرق، غرب تهران از ساعت ۲۳:۵۰ دقیقه صداهای ممتد شبیه فعالیت پدافند میاد، و یا حتی شلیک یه چیزی فراتر از پدافند
سلام محدوده چیتگر فعالیت شدید پدافند ساعت ۲۳:۵۴
وحید ۱۱:۴۵ شب، جنت‌اباد مرکزی تهران، یه عالمه صدا که فک میکنم پدافند بودن
وحید جان همین الان غرب تهران (سمت میدون آزادی) صدای پدافند شدید میاد
سمت شهرک نفت هم همینطور...
صدای پدافند از دور در مرکز تهران ساعت ۲۳:۵۵ شنیده میشه
صدای ضد هوایی بوضوح در جنت‌آباد شنیده میشه
سلام وحید همین الان کلی صدای پدافند تو تهرانسر اومد ساعت ۲۳:۵۰
وحید سلام شهرک غرب ۲۳ و ۵۳ پدافند فعال شد.
سلام وحید جان ۲۳:۵۵ منطقه ۱۰ صدای بم عجیبی اومد چند بار پشت سر هم. شک دارم چی بود.
وحید جان ساعت ۱۱:۵۴ جنت آباد مرکزی بنظر صدای پدافند میاد چندتا پشت سر هم
سلام وحید جان ما تهران، جنت آبادیم، پدافند فعال شده، انفجار نیست
۱۱:۵۷ دو مرتبه صدای انفجار و پدافند شدید غرب تهران شهرک اکباتان
ساعت ۱۱:۵۷ باز صدای پدافند شدید و صدای انفجار. جنگ اینجوری صدای پدافند نبود.
غرب تهران، ساعت 23:57 تشخیص نمی‌دم صدای انفجاره یا پدافند، اما صدا مهیبه
وحید جان ساعت ۱۱:۵۷ جنت آباد مرکزی بنظر صدای پدافند میاد چندتا پشت سر هم
صدای ممتد پدافند غرب تهران ۲۳:۵۷ همچنان ادامه داره
۲۳:۵۷ سمت مرزداران غرب تهران صدای پیدافند میاد همینجوری
ساعت ۱۱:۵۷ باز صدای پدافند شدید و صدای انفجار.
غرب تهران، ساعت 23:57 تشخیص نمی‌دم صدای انفجاره یا پدافند، اما صدا مهیبه
11:57 صدای انفجار میاد بعید میدونم پدافند باشه جنت آباد مرکزی
صداها وحشتناکه ۱۱:۵۷غرب تهران جنت اباد مثل زمان جنگ
الان صدای خیلی شدید تر میاد ۲۳:۵۷
جردن ۲۳:۵۵ صدای پدافند میاد
سلام وحید همین الان دوتا صدای انفجار اومد سمت بلوار  فردوس غرب صدای پندافند هم میاد به شدت
ساعت ۱۱:۵۷ بازم صدای انفجار و پدافند، انفجار هم هست  ولی انفجارهای بزرگی نیستن
باز هم به صدا انفجار میاد، به نظر پدافند باشه
ساعت ۲۳:۵۸، شهران
ساعت ۱۱:۵۷، همچنان جنت‌اباد مرکزی تهران، همچنان صدای پشت سر هم به احتمال زیاد پدافند
سلام ۸ انفجار مجدد ساعت ۲۳:۵۷ غرب تهران شهران
غرب تهران سیمون بولیوار دوباره صدای احتمالا پدافند ۲۳:۵۷
سلام وحید جان ۱۱:۵۶ صدای پدافند شدید محدوده دریاچه و میدان المپیک میاد
همین لحظه ۱۱:۵۸ همچنان ضد هوایی شدید
سلام سمت شهرآرا صدای پدافند میاد پشت هم
ما مرزداران هستیم
از دوردست خیلی صدای انفجار میاد
ساعت ۲۳:۵۶
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/75307" target="_blank">📅 23:54 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75306">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/872058ebf9.mp4?token=Jdth3e3sSac3ql_vfmKwJb_yj9W0-7C8YYrrM-J1EEhYVCWEQyvXUuRAONCOosw7cxAa7Jk3eS8kna5Hgqw7WlvLnA-Yvlm3LEgUCESg1UTVx8AgO9Kc66BSMmBpbSU8D4U_GsmIsI7O2scGRD_-03YUHYry4BOl2EbZ3dRGTMt2QhwoFuHRQPKRPRGR8hw3K_x_0F7Bhx1bqwpq9UpKeMtYwPciJs5BPZL0fFv5-we8fAqoHaHbyaXt0I2_lSQtzehG6y1KKxBQcCJlO1ZosAKiNT7EAvR2ZjXjc8Ep2M5jcMYsM5sh-NFws3Jl0RHQSNn6q7-C92DGnMwGGF5ELQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/872058ebf9.mp4?token=Jdth3e3sSac3ql_vfmKwJb_yj9W0-7C8YYrrM-J1EEhYVCWEQyvXUuRAONCOosw7cxAa7Jk3eS8kna5Hgqw7WlvLnA-Yvlm3LEgUCESg1UTVx8AgO9Kc66BSMmBpbSU8D4U_GsmIsI7O2scGRD_-03YUHYry4BOl2EbZ3dRGTMt2QhwoFuHRQPKRPRGR8hw3K_x_0F7Bhx1bqwpq9UpKeMtYwPciJs5BPZL0fFv5-we8fAqoHaHbyaXt0I2_lSQtzehG6y1KKxBQcCJlO1ZosAKiNT7EAvR2ZjXjc8Ep2M5jcMYsM5sh-NFws3Jl0RHQSNn6q7-C92DGnMwGGF5ELQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما به نقل از یک مقام آگاه نظامی گزارش داد «به دنبال تعرض ارتش آمریکا به یک نفت‌کش ایرانی، یگان‌های متعرض دشمن در محدوده تنگه هرمز زیر آتش موشکی جمهوری اسلامی قرار گرفتند که پس از تحمل خسارت مجبور به فرار شدند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75306" target="_blank">📅 23:38 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75305">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9Gx3EkpJ7pOSpshWbRze8wxcG1FJrnRZFXae-osqtKoTRoG4QN-X3xN_-o5TNKuqKIr07qjUWf3i7FdoZzB0-IEg5imftj1ongvTE4mDknVKeUJaratypuPO1hf7zO5B7dUswKjUmJazTAXk5cO1f8N1TaY8hKpWbqpRNr5upp2jZZbNSDnPzli3s6FOYS3bFF4gmKo-2W87k48Vgo0NwqWJoVKF8qiMoZ5UnggQ6xzVkHr3eOjFFPs0IL3nq7WFWwoZ2lXu7h_5W4T2QCvPrtsiDTmLJJgCFqqPjqAeShhm64wV7fHza1W4xTwjNPiBiMnBAsIF22QVAxYeNgZtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، در خبری اختصاصی اعلام کرد که صداهای انفجار که پنجشنبه‌شب، ۱۷ اردیبهشت در حوالی بندرعباس شنیده شد، مربوط به «تبادل آتش» میان نیروهای مسلح جمهوری اسلامی و ایالات متحده بوده است.
به گفته فارس، در جریان این تبادل آتش، بخش‌هایی از اسکله بهمن در جزیره قشم هدف قرار گرفته است.
@
VahidOOnLine
آپدیت: منابع غیررسمی حکومتی و سپاهی میگن امارات اسکله بهمن رو هدف گرفته.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75305" target="_blank">📅 22:53 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75304">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/prk6xbnrW7jUImwhp0esf2f9DyAI_cROfq7Ip-woT0q8YFruaMuXFsV4-l4Jq-FZ-I1f4O3ryFJTZ2DY2SwWcuTPfoD3hGqXmk4ljlg1M7lg8llFx0kIhSnTS-gzO3d84yWqKxXZ2Lz-sR1pFnyt4MuAdvJbzRoVc3zGz4wYhmsVCJ6-5i1BA606nNFfcanMyzOeQyJHsXavBEu5rRAQlwCSrTFEeYKfOFfsIzhFMGwout_WOhykswaHWN_qdBiMXcdS6kdxx28LSS33ERh6uoccA4nDRlk7d7zqmg8hqLJKBdFNwi97685tKIeLGERgmpbDGgbhHHsSXG2_S1njlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
تماس بسیار خوبی با رئیس کمیسیون اروپا، اورزولا فون در لاین، داشتم. درباره موضوعات زیادی گفت‌وگو کردیم؛ از جمله اینکه
کاملاً در این موضوع متحد هستیم که ایران هرگز نباید سلاح هسته‌ای داشته باشد.
توافق داشتیم که رژیمی که مردم خودش را می‌کشد، نمی‌تواند کنترل بمبی را در دست داشته باشد که قادر است میلیون‌ها نفر را بکشد.
من با صبر و حوصله منتظر بوده‌ام که اتحادیه اروپا به سهم خود از توافق تاریخی تجاری‌ای که در ترنبریِ اسکاتلند بر سر آن توافق کردیم، عمل کند؛ بزرگ‌ترین توافق تجاری تاریخ! وعده داده شد که اتحادیه اروپا سهم خود از این توافق را اجرا کند و طبق توافق، تعرفه‌های خود را به صفر برساند!
من موافقت کردم که تا دویست‌وپنجاهمین سالروز تولد کشورمان به او فرصت بدهم؛ وگرنه، متأسفانه، تعرفه‌های آن‌ها فوراً به سطوح بسیار بالاتری افزایش خواهد یافت.
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75304" target="_blank">📅 22:46 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75303">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-mBMb9Xcym2lH-VyuPpfxTDyzvT2Fcvg4sRat8yebuyBJUf5LEWkYUfFUz_sWoZA1wCPm7tSaCXrrVGFnpcs0fofT36lkLAts98tIsQjJjzo-de2jItaVGBIP1qxWMzGsuUmOLr6QmLmpByJPOa0LNVF7e8cFAsKT9JXJZtgDtbSKxGkRHbpZZII-sdrMlqoLZVu9p-MQKnHBrR8pcmiaJlj3_EdoMs6_8xSpjmy9ixA-_SYOL8TkHXLEq4t1exNLdZ9IoBhHwQfRpnJDAYBQFhP8tLZq4QlrcAuheJfPVvCPiYJaob-upHvFNrL5MMrYZ196TgHxDXBzAyfh8eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با تلاش‌های ایالات متحده و بحرین برای پیشبرد قطعنامه‌ای در شورای امنیت درباره بازگشایی تنگه هرمز و آزادی کشتیرانی، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، این قطعنامه را «یک‌سویه و تحریک‌آمیز» و روایت‌های مندرج در آن را «گزینشی و جانبدارانه» خواند.
عراقچی در نامه‌ای به دبیرکل سازمان ملل و رهبران کشورهای عضو، محدودیت‌های کنونی در تنگه هرمز را ناشی از «جنگ تجاوزکارانه، غیرموجه و غیرقانونی» آمریکا و اسرائیل علیه جمهوری اسلامی خواند و به جامعه جهانی هشدار داد که نباید اجازه دهند شورای امنیت به گفته او مورد «سوءاستفاده متجاوزان» قرار گیرد.
او در این نامه تاکید می‌کند که تردد در تنگه هرمز تنها در صورت «توقف دائمی جنگ و رفع محاصره و تحریم‌های غیرقانونی» علیه جمهوری اسلامی به حالت «عادی» بازخواهد گشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75303" target="_blank">📅 22:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75302">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هرمزگان
پیام‌های دریافتی با جزئیات تایید نشده از ساعت ۹:۲۵:
درود
ما غرب جزیره قشمیم. از ساعت ۹:۲۵ به فاصله چند دقیقه ۴ بار صدای انفجار اومد و موجش شیشه ها رو لرزوند.
ساعت ۹:۴۸ یه صدای انفجار و ۱۰:۰۲ صدای دو انفجار دیگه. صدای جنگنده نیومده ولی
صدای چندین انفجار پیاپی قشم همین الان
بندرعباس همین الان صدای انفجار اومد مثل صدای برخورد بمب بود
بندرعباس صدای انفجار اومد حدود ساعت ۹ و نیم شب
سلام، ساعت 21:30  بندر خمیر استان هرمزگان انفجارهای پیاپی و شدید
سلام وحید جان قشم صدای پنج انفجار
سلام وحید جان بندر کنگ ساعت 21:50 صدای چندین لانچ موشک شنیده شد
ساعت 22:01 شهر قشم در محدوده [محله‌های] دوحه و چابهار صدای دو انفجار پشت هم شنیده شد
ظاهرا انفجار ها از سمت اسکله بهمن شهر قشم بوده
خودم حاضر بودم و شنیدم
صدا بسیار بلند بود و موج انفجار هم حس شد
امروز ۱۷ اردیبهشت ۱۴۰۵
سلام داداش
قشم دقیقا الان ساعت ۱۰
دوتا موشک زدن اسکله دوحه
خیلی وحشتناک بود کل آسمون قرمز شد
همین الان بندرعباس صدای دوتا انفجار پشت سر هم از سمت دریا اومد  نمیدونم لانچ بود یا برخورد ولی هم صدا داشت هم پنجره ها لرزید
درود بر آقا وحید گل
بندرعباس ، الان ساعت ده و دو دقیقه شب صدای دو انفجار پشت سر هم آمد
ساعات پایانی روز پنجشنبه
سلام آقا وحید. قشم  همین چند دقیقه پیش  ساعت ۱۰ شب دوتا صدای انفجار اومد همراه یا نور روی دریا. چیزی رو توی دریا زدن
همین الان ۲۲:۰۴ دقیقه
صدای سه تا انفجار سمت دریا میاد
سمت سیریک استان هزمزگان
یه موشک هم بلند  شد
با فاصله نورش دیده میشد
به سمت دریا رفت
الان سمت میناب دوبار صدای انفجار اومد
با شهر فاصله داره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75302" target="_blank">📅 22:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75301">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SIFDpsV1ht-lca9GPdKp0PcD95mo_QxYkXWIphfytXZ2TBLq_SSO4slMnca6lpSJVoIwY9cOgy9X73BkadWB-DsBpari90iMOkcT8neXr7DL1EHHAjWXn_0HfiFscErSKUYRl9JQbJFukg1_DFdKhuLSI5WrlElWWqmsCncEba2hTlBXeSZVaC3NwuQMfUU3qKQ-s8KwEbt9pzKYn8XYjDDMBX__o5C7_2Ugd1QZBlJIEmhV4SXuZQprlz-0YjK3mgvQznnaLCVPZ_T5zPSRW6QPZgvzrPMzXFaTeheXjbqDjnNF8QIayoiC1RFgchkC5fSegm9ZBrq9bQtwsPj1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">mahshids979
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75301" target="_blank">📅 18:34 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75300">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MsyyiUuarkoIsg8X5nQ1ITNqwILY-EuMSXfM1ygd0D2U67Vz8Yxtr31n0VZJ1t1u_ac9t7AM2V0szFngAUGWSSZ9ANeMTl_D5PvuNJjwCP5NMJkgMm3sTQBzsyrKqgmO3Yd_vxWpTf7uLv3tXRBddSvJv5g7kI_uhL-CeW9nl3fwEZd8WtQsUhgxdzviHZKZ3NX3ccHtG56b9qGBMLC4Ob1fSrrVO0t9ipEdVWcpuhp2RMiVp6MKjGG4tSrN-9bGx0I1ObR6UFy60voCvgTwC32gP_k9GyWCLSjpzstmrezFGV6zhN7w6iPaM3SM82AtH0ZuN-lQu4Jafat2QR41LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SheykhSharzin
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75300" target="_blank">📅 18:31 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75299">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pznCmeRwi0lHwVQ_HnPMS5fd3EIroSpZHQdCwm4yiPqxWch-DTdVE9fO_DojOxNx_7Y1lUzL4enc7K0eYeLb61pB5vQ5G2D0yKmGvgYxtqn17WyDQJHmwiDEwt3CD2cgp_C7pkRn9GRzL-dZ0gnoFOz5p3jneTNnKVoAmSNIO0DRF5BQ10XA3v9h4jD66UUvWbYQX8rJFEP2xu4Mb1kIx2YXrYf00w4jY185iHKJHFZ5uT9wHbNVAcFQQiS24cWD0J9xKDchy9frAiFnXJpJJFsVl7rhEwP1jj3babUjQD9z82gIrLKP7gh60VFuSEmqu12AGHATaNeGY3ARvZsCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">t_golpoone
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75299" target="_blank">📅 18:29 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75298">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TddIbplZ8OxkGUCdSVu2Ggfab29BDKEprT9YbzqESiHwCrOJgJSrUlrSOmS1RJOe7SCg6FJQiEYGOuszzqytdHlbR5YWw07Ip1rETaP9KeHngZa6Kf8WaKREZ66vnuYc3vp9cIuWMgNbIXqDFfH2T-4OlFh5Zf-_8PPvWFBmXcJBs3SkWv5HSTghlBEIJ7dq5eVQe2DO3-mrt22oTJ_gW8req5s1FXjS-3T3GZ55XlnXMf3I1c2wEosky8Z3P0MYFTLEF7RWj9ygF2xxjBKEirLjNy9nWPn3FFdH2ZVAZWrN9gYGRnCAD_0aiwHnIke0_ogsVGePZxY9KV97RXGyYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود نبویان، عضو کمیسیون امنیت ملی مجلس، در شبکه ایکس نوشت: «با وجود سابقه بدعهدی آمریکا و به ویژه حضور اصحاب توافق ذلت بار برجام به‌همراه قالیباف در مذاکرات، هیچ امیدی به مذاکره و توافق مطلوب برای ایران وجود ندارد.»
او افزود: «لازم است قالیباف اصحاب توافق خسارت‌بار برجام را از تیم مذاکره‌کننده کاملا حذف نماید.»
نبویان در پست دیگری نیز نوشت که برخی از «مسئولین و سیاسیون ترسو و غیرهمسو با ملت مقاوم ایران»، به دنبال آمارسازی‌های غلط برای تسلیم هستند، اگر اصلاح نکنند، اسامی‌شان افشا خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75298" target="_blank">📅 18:20 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75297">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FroeHyKunQ1ANfjmeOysI4NHv0jKUl3SWXMSUVJplHEPNcA0S2LK7ZxNZZ-46XoxR-M86os3FjsUTMjwkHF14EYkKmu7zNiD6jRkg3PWh9NfnsfCy2uqdksLTQjLod3jdvZDt9-jd0uxRb8gp356CCfeelG_td4mUGmN9ycFsvkaswdXuumWK6QL0pL8lFWlLgbG1cyl23y2Q9_Sa0ecWVwoo4V7k5j6zfIiKZgu-cVJY635D_VaLBcKKOD9WaR51wQtBj4oFw4LmlWMbONip3k0-UT5Dd5lJV_iQPX6oPrYbBgaZalHJYXEnDNE9QJ8PxjD59myXEH9jifxxpoaPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژان-نوئل بارو، وزیر خارجه فرانسه اعلام کرد تا زمانی که تنگه هرمز توسط نیروهای جمهوری اسلامی مسدود باشد، هیچ تحریمی علیه تهران لغو نخواهد شد.
او در گفت‌وگو با شبکه «آر‌ال‌تی» گفت: «ما خودمان تحریم‌های مهمی علیه ایران اعمال کرده‌ایم. اما تا زمانی که تنگه هرمز مسدود باشد، لغو هیچ‌گونه تحریمی قابل تصور نیست.»
بارو افزود: «این تنگه نمی‌تواند بسته شود، مشمول عوارض گردد یا به‌عنوان ابزار فشار و باج‌گیری استفاده شود.»
او همچنین تأکید کرد فرانسه نباید دوباره در موقعیتی قرار بگیرد که مجبور شود هزینه جنگ‌هایی را بپردازد که خود آغاز نکرده است.
به گفته او، اروپا باید وابستگی خود به نفت، هیدروکربن‌ها و فناوری‌های دیجیتال را کاهش دهد تا کمتر درگیر بحران‌ها و درگیری‌هایی شود که مستقیماً طرف آن نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/75297" target="_blank">📅 18:17 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75296">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkKA4vm0kRu9NZejVwulZnQmUW3BEJ05utqufy5TBIKtS1xOtyPDhfIHGzPznPPTEU66wKQVZMcuueuc-SHlnrylSeNkz5CNsRMSvsWe-wr5l2r6VMHeq_24DJQRnxAkZHmBNuBi9PWR0EWh0IRWIDFM2inE1CwmMJMVIc-oZNN7PA6Q7pADu7t6P3ztJMVrjmc5BEt9xOWRYFN9PYJwlA8VGnUx1A5HZvBNVL3oTTpW5rrQwAtckZKtT6tfG2jtfJFUK3abSjv0YAc9lrIJCObJpgcvXBCzOd_TofeigWHP7qRf3uL2AfuHEfZGUcPdtFr1ZAj0n14BXZs5IsAGqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، از ملاقات اخیر خود با مجتبی خامنه‌ای، رهبر جمهوری اسلامی، خبر داد و گفت با گفت‌وگوی مفصلی داشته است.
مسعود پزشکیان که روز پنجشنبه ۱۷ اردیبهشت در نشستی در وزارت صمت سخن می‌گفت، به ملاقات دو ساعت و نیمه با مجتبی خامنه‌ای اشاره کرد اما در مورد موضوع و جزئیات ملاقات و اظهارات مطرح‌شده چیزی نگفت و صرفاً او را به‌دلیل «صمیمی و متواضع بودن»، «الگویی برای نظام مدیریتی و اداری» کشور توصیف کرد.
پس از کشته شدن علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، در روز نخست جنگ با آمریکا و اسرائیل، مجلس خبرگان رهبری پسرش مجتبی را به‌عنوان رهبر جدید معرفی کرد. با این حال از آن زمان هیچ تصویر، صوت یا دستخطی از او منتشر نشده و رسانه‌های ایران فقط شماری پیام مکتوب منسوب به او را منتشر کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75296" target="_blank">📅 18:14 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75295">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQ1foQAfvAYZJT8UCUy7B5c3NDtQifA5E9ZBIgMcZisX6PStGOxd6IriEc3ZEJZ0rs5XWFTO8H3laQdBsb2rYNjkfyvJLTTP0P2I-kFfUbUWTEit4BrtwrmKGChUnsCBv00pUCvc-z0ZIDJ9j-b4pF_DJARw0DMHPtWIwHOd9DGBjiqX3H5Nx5i-haEajPOFpES0_B7BOaGinHxgh4RM8lDhBT3c3oBRo045DUTA8eOO79mW9djoKBWlr3Xt5JNn0CZECGSYMtdzX0eh-tkht5DPgXxHF1czlwKKEKJiCOEe36Disl7QKVCrWc-5UyCpL_OWjB8sAzOpdNH9gUrI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال در گزارشی درباره توافق آمریکا با رژیم ایران نوشت که ایالات متحده می‌خواهد همه ذخایر اورانیوم غنی‌شده از ایران خارج شود. به این معنی که هم ذخایر اورانیوم با غنای ۶۰ درصد و هم ۲۰ درصد و هر میزان اورانیوم غنی‌شده دیگری که ایران در اختیار دارد نیز باید تحویل دهد. این در حالی است که مفامات تهران همچنان می‌گویند موضوع خروج ذخایر اورانیوم غنی‌شده از ایران، از دستور کار خارج شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/75295" target="_blank">📅 18:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75294">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgdEYiGz2M8UfmVOQWLJEfPqzdZc-7SPOf2sJQQhzgDWqBbkAEKnCsT1UHceDJBB2Nd2ybFPP4WqaltgDiLiQ_SeNh6q8v00C8ywV_f_m0Qy3WImJmr2ylchzNSeB9F1RPrqiO2XFYXxM5HFjrxgJc2cB-aVXr4CrcefMYMouShjM-Q8h23gWdDcAZ5tzdjxBN2bUn8SQlXkXS_lPImqBcR6qXbhqV_wWqaZp26PYmxSTom1xIM74OBvQZ7MPkL0enlb6CI9d3zSjhwnE6gcy527h3nuhfCjLq8V_vaWDYFfobfh1XKtYpdk1phlhZC6ESPrazDQhu9Ire4oYE7jZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی نیوز به نقل از دو مقام آمریکایی گزارش داد چرخش ناگهانی ترامپ از «پروژه آزادی» تنگه هرمز پس از آن رخ داد که متحدان خلیج فارس از این تصمیم غافلگیر شدند و عربستان سعودی امکان استفاده ارتش آمریکا از پایگاه‌ها و حریم هوایی خود جهت اجرای این عملیات را به حالت تعلیق درآورد.
به گفته این مقام‌ها، ترامپ بعدازظهر یکشنبه با اعلام «پروژه آزادی» در شبکه‌های اجتماعی، متحدان خلیج فارس را غافلگیر کرد و این اقدام موجب نارضایتی رهبران عربستان سعودی شد. در واکنش، عربستان سعودی به آمریکا اطلاع داد که اجازه نخواهد داد ارتش آمریکا از پایگاه هوایی پرنس سلطان در جنوب‌شرقی ریاض پرواز کند یا برای پشتیبانی از این تلاش از حریم هوایی عربستان عبور کند.
این دو مقام آمریکایی گفتند تماس تلفنی میان ترامپ و محمد بن سلمان، ولیعهد عربستان سعودی، این اختلاف را حل نکرد و رییس‌جمهوری آمریکا ناچار شد «پروژه آزادی» را متوقف کند تا دسترسی ارتش آمریکا به این حریم هوایی حیاتی را احیا کند.
دیگر متحدان نزدیک خلیج فارس نیز غافلگیر شدند؛ رییس‌جمهوری آمریکا پس از آغاز این اقدام با رهبران قطر گفت‌وگو کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75294" target="_blank">📅 18:11 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75293">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KZjl-o4_PcBnIscvI2COXluJHMY7xLhBr8ywlZvFQBSXb7zgQypwJHsg0MJJU55qnLyrXI1gVzAPoqGollpJTjhhQi4vOUhccS5_gz8_oZhIA7VqcsRccoIXLXKImIicuybLQa_OfBb3QwmKrhBQ8KyI2Y2kPeafGPA8Dd7KAtcwAfcgjnQQkJiNWW-d_AKAbSNnztD4HqycsCWrd7bwI0qKtigsaGLFQb0AsgmD0bqGpiWeN3bi1s2JhAslN6_pjPPAKUkM1bXZHa_Gc5EAAPQuuNscFwWFPhUkoAZIR3MsvQIqgWf6c471namtIfPcL66KpmplVW5alozWregyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ چهارشنبه شب در
تروث‌سوشال
تصویری منتشر کرد که مدت‌زمان جنگ‌های مختلف در آن نشان داده شده و از مخاطبانش خواست آن را ببینند.
او بارها به کسانی که مدعی‌شده‌اند عملیات نظامی علیه جمهوری اسلامی «طولانی» شده، پاسخ داده‌است آن را با جنگ‌های پیشین آمریکا مقایسه کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/75293" target="_blank">📅 06:28 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75292">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">غرب تهران
پیام‌های دریافتی:
صدای انفجار 2:38 دقیقه جنت اباد تهران
شهران صدای انفجار وحشتناک اومد ساعت  ۲:۴۰
یک صدای انفجار خیلی بلند سمت شهرزیبا (غرب تهران) ، شبیه موشک نبود بیشتر انگار یه چیزی ترکید
پونک تهران
دو صدای انفجار شنیدیم
همین چند دقیقه پیش غرب تهران یه صدای خیلی بلندی از انفجار اومد
سلام وحید جان دادش غرب تهران ۲:۳۸ اینا صدای یک تک انفجار  اما سنگین اومد ولی هیچ جا نگفته کس دیگه!
چند دقیقه اخیر راجع به صدای انفجار توی جنت اباد پیامی دریافت نکردید؟
صدا شبیه انفجار پهپاد بود. موج نداشت اما شدید بود.
[دریافت کرده بودم ولی چون تعدادشون کم بود صبر کرده بودم تا پیام‌‌های بیشتری برسه. چون پیام‌هایی که بعد از انتشار پست ارسال بشن اعتبار زیادی نخواهند داشت.]
سلام منزل ما جنت آباد مرکزی هست محدوده خیابان بصارتی
حدود ساعت ۲.۴۰ صدای انفجار شنیدم اما دقیق نمی دونم چی بود
شهران صدای انفجار بلندی اومد ولی یه دونه انفجار بیشتر نبود.
ما سمت باغ‌فیض هستیم؛ ساعت ۲:۴۰ صدای انفجار اومد، آنچنان نزدیک نبود اما بلند بود؛ بنظر نمیرسید شبیه به صدای برخورد باشه؛
اما همین یکم پیش هم حدود ساعت ۳:۰۵ صداهایی شبیه به موتور اما تیزتر و ممتد اومد که حدود ۳،۴ دقیقه طول کشید؛ فکرمیکنم شاید پهباد بوده باشه؛ با صدای جگنده که در زمان جنگ میومد متفاوت بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/75292" target="_blank">📅 02:53 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75290">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/551509ade1.mp4?token=t1UHZx3weIob-KhpGqf5tYgd2lyBLV3FafOAFgeaBRjS2ZqtcUhJqLUO5iPUghu1_PluUmXK9dLAI1Rjg1JnnKFRVmqJFeYynCuPmHLH5eMx-jXzJgK1k8HDRam18e7rkj6-KvIrZLAraeC3ZGjB26Km9pKb-cOKobWWRYt5bUvVa9EW09YKFYhRwUp7eKedQclb7mVSOHdjP7o-C724Rgro1rxyBl95MvpJ-AeQtg_CJCf26Qv1P7FeDvbkwBhRFBa42i17-YgitWmdcvsEozVRPhIy8343bXFGWsvKSdtEBzsmDrIMpztB4TJMId8cSgAHq83cwtA_PxyQy2NwaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/551509ade1.mp4?token=t1UHZx3weIob-KhpGqf5tYgd2lyBLV3FafOAFgeaBRjS2ZqtcUhJqLUO5iPUghu1_PluUmXK9dLAI1Rjg1JnnKFRVmqJFeYynCuPmHLH5eMx-jXzJgK1k8HDRam18e7rkj6-KvIrZLAraeC3ZGjB26Km9pKb-cOKobWWRYt5bUvVa9EW09YKFYhRwUp7eKedQclb7mVSOHdjP7o-C724Rgro1rxyBl95MvpJ-AeQtg_CJCf26Qv1P7FeDvbkwBhRFBa42i17-YgitWmdcvsEozVRPhIy8343bXFGWsvKSdtEBzsmDrIMpztB4TJMId8cSgAHq83cwtA_PxyQy2NwaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، شامگاه چهارشنبه گفت که پس از «گفت‌وگوهای بسیار خوب» در ۲۴ ساعت گذشته، دستیابی به توافقی با ایران برای پایان دادن به جنگ «بسیار محتمل» است.
@
VahidHeadline
ترامپ با اشاره به وضعیت نظامی کنونی گفت که توان دفاعی ایران به‌شدت کاهش یافته و نیروهای هوایی و دریایی این کشور عملا از کار افتاده‌اند. او با بیان اینکه «ما پیروز شده‌ایم»، اعلام کرد که جمهوری اسلامی اکنون تمایل زیادی برای دستیابی به توافق دارد.
رئیس‌جمهوری آمریکا شرط اصلی هرگونه توافق را دست نیافتن ایران به سلاح هسته‌ای و خروج ذخایر اورانیوم غنی‌شده از این کشور عنوان کرد.
@
VahidOOnLine
او تاکید کرد که ایران «نمی‌تواند و نخواهد توانست» به سلاح هسته‌ای دست یابد و این موضوع را بخشی از تفاهمات مطرح‌شده دانست، هرچند جزئیات بیشتری ارائه نکرد.
آکسیوس پیش‌تر گزارش داده بود که در یکی از بندهای پیشنهاد آمریکا، توقف غنی‌سازی در مقابل رفع تدریجی تحریم‌ها مطرح شده است.
این در حالی است که پیش‌تر مقامات جمهوری اسلامی هرگونه مذاکره درباره توقف غنی‌سازی را رد کرده بودند و بر ادامه این برنامه در چارچوب سیاست‌های اعلامی تاکید داشتند.
@
VahidOOnLine
ترامپ گفت: «ما در وضعیت خوبی هستیم و حالا باید آنچه را می‌خواهیم به دست بیاوریم؛ اگر این اتفاق نیفتد، باید یک گام بزرگ‌تر برداریم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75290" target="_blank">📅 00:06 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75289">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6KyG1q115nSTVF9kO9ENBNuKUisYKOyoAYNBf9f4LQsbkDNlIeJzfjRK11zO9p545R5TGBQ4pkQ1riitBrjsJBRC5s_4FKDbNCzEUkf7exnd6Y5hsnGO_IxMOiZuQ-dv6H9vsA4eY-czorOLYrsgIZnNFpmZMho7MJb-kl9On8htQESeMpPw2GB8XAmzlfsuVa2Dk6roKMEbDItCOyZHhKUYnux7B6aiXwKqtWGMcWWRqCx2lS43VmD8fK_VZAPZutY5vTfVRWkmjAYZRb3Qv-G5un3JOVmkEP3CL4uGpSRs4-qaNUyUZ5Q74M4V15jJyvwNDYbDZzXmowQ8ez1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل عصر روز چهارشنبه در حمله هوایی به منطقه ضاحیه، حومه جنوبی بیروت، که تحت نفوذ حزب‌الله است، فرمانده یگان نخبه «رضوان» این گروه را هدف قرار داد.
این نخستین حمله به حومه بیروت از زمان آتش‌بسی بود که روز ۲۷ فروردین بین اسرائیل و حزب‌الله برقرار شد، هرچند درگیری‌ها در جنوب لبنان متوقف نشده است.
در بیانیه مشترک بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و یسرائیل کاتس، وزیر دفاع، آمده است: «عوامل رضوان به رهبری این فرمانده مسئول شلیک به مناطق مسکونی اسرائیل و آسیب رساندن به نیروهای ارتش اسرائیل بودند.»
خبرگزاری فرانسه به نقل از یک منبع نزدیک به حزب‌الله اعلام کرد که «مالک بلّوط، فرمانده عملیات در یگان رضوان» در این حمله کشته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75289" target="_blank">📅 22:38 · 16 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
