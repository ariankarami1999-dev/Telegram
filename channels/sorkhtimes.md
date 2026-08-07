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
<img src="https://cdn4.telesco.pe/file/tm6My5s2HZ1IxTHUZipp4A1sBcSuiXyP4ade9rCaw-7a4K0p-mIFu3i2THHzsGiZqaLc042kRbES2t2z9OUZg38FH2crsgeTgKssl9WryujJB7jUmd5fiHBZFGm1VJSGYEd7AQGF2DXiHecPCiI7DH9EMyBc6kn1FmzdA1H3rH7JD9XWDTGJ9fsng0TSgkw_zSFoBD86CeBanbzVIfdYNnO1bbIqJnZ1E4aljFNlrfkg4_gfOu65v0q0vyfaM4YdQi25vc-T02Psp2RrHfeZ5QIq1496GKMalj1BCoZMF3vdHkQiAryX2uwlBCPZwMkY4LOB0i3kG--2vY7wIiQttg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 21:10:53</div>
<hr>

<div class="tg-post" id="msg-137536">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
‼️
نمودار ترسناک و فوق العاده غم انگیز... کمترین میزان ازدواج در ۳۰سال اخیر  و کمترین میزان زاد و ولد در ۷۰سال اخیر! سلامی تلخ به پیری جمعیت باید کرد... از هرایرانی بپرسید علت این فاجعه را چشم بسته عاملش را "اقتصاد فاجعه بار" خواهند نامید.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/137536" target="_blank">📅 20:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137535">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLDXePaD0XHDWzsPwl4pbYpuT5rd_c1UDEFqa-9cDI4GrFpjrHoPlOZHUw6lIeok1E3TPB3M5ZJrrJiAqEntjEjRZcu3KMmbSpduU6lZkjnfqrv8iek7oZ13kSDDrJanR5s2wSRK4yflras5dIORb8OYA7PIdV2O0wsmUYkE8U3DzsLBYvzoAnMWbMCrYpj9V4ES_bN6VuZmDMwZVxeJT-JJ1IdNcOJ0mKgK-gsgqHTRcH-7qjCWAz_hHKLyb1K8T9NqGHC9MFJe5XVIkPvE6ldFyaxPIHmXxr5e1Jd2NRZjuEvTLXV584KPwRLzui4835BxtjGiMEaBu9zW2eABPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
صلاح : کاش زبون ترکی بلد بودم. طرفدارای ترابزون خوش‌آمدگویی ویژه ای به من نشون دادن، من اومدم که براتون جام ببرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/SorkhTimes/137535" target="_blank">📅 20:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137534">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjfngq3-70BeIVRHqczzJCacKtOzdGxZiBE-KPAuMDGCqbw_NZdK8Vf9coFaBj4hDekgrs3OXeWmFvlgfj8-02axvz0hKq-qYgeav4OmHn89nC7x6xKBPMNyIdC7lhFxx5I1PdoSLDvz0wKlEFRPbY0pg-oqUnrO2keTqzPo4m-q7u7Lcb4f8JPyXo4iN3GSGe3E_qD_DiZaFyLXfC3P515v4aJ9Y01Nqc8inUJOVoGiRNEBYl9iITecGRw3TcR3k50X2yYu89Q9GbHOtMLUTOQmqZQVynTt5NDnjraFM4Vhl2o9HJeUJr2lEmdD0jVCMujGBFpfoqJhxwtFnMQBcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
فقط تا پایان فردا برای بونوس ویژه Egypt Power x1000 فرصت دارید!
💰
تا پایان ۱۷ مرداد با هربار واریز حداقل ۱ میلیون تومان، ۱۵ گردش کازینو به ارزش ۱,۵۰۰،۰۰۰ تومان به صورت رایگان دریافت کنید.
📌
نکات مهم این بونوس:
👇
▪
︎ ۱۵ اسپین رایگان ۱۰۰ هزار تومانی
▪
︎ ارزش اسمی بونوس: ۱,۵۰۰,۰۰۰ تومان
▪
︎ مبلغ فوق تضمین‌شده نیست و میزان برد به نتیجه چرخش اسپین‌ها بستگی دارد.
▪
︎ پس از پایان اسپین‌ها، برد نهایی بی‌قید و شرط به موجودی حساب شما اضافه می‌شود.
🔗
آدرس ورود به سایت
اسپورت‌نود:
👇
🔵
sportn5b2.com
🔵
sportn5b2.com
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SorkhTimes/137534" target="_blank">📅 20:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137533">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
امیر رضا افسرده: به پیشنهاد پرسپولیس جواب مثبت داده بودم ولی به خاطر روی گل ماه مازیار زارع در ملوان موندنی شدم و به پرسپولیس نمیرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/137533" target="_blank">📅 19:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137532">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
قدوسی: حضور دانیال ایری، ابوالفضل رزاق پور و کسری طاهری و حسین نژاد در پرسپولیس منتفی شد
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/137532" target="_blank">📅 19:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137531">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
❌
ورزش سه: مهدی تارتار از روند نقل و انتقالات پرسپولیس راضی نیست و مدیران باشگاه پرسپولیس دارن لیست خرید شو روز به روز کوچیک تر میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SorkhTimes/137531" target="_blank">📅 19:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137530">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
❌
ورزش سه: مهدی تارتار از روند نقل و انتقالات پرسپولیس راضی نیست و مدیران باشگاه پرسپولیس دارن لیست خرید شو روز به روز کوچیک تر میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/137530" target="_blank">📅 19:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137529">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
تا این لحظه تارتار مخالف بازگشت رامین رضاییان به پرسپولیس است اما همچنان رایزنی و مشورت ها ادامه دارد.
📰
سپهر خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/137529" target="_blank">📅 19:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137528">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
فارس: نساجی با جدایی و انتقال دانیال ایری مخالفت کرد و پرونده حضور ایری به پرسپولیس بسته شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/137528" target="_blank">📅 19:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137527">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⁉️
⁉️
⁉️
فوووووری
⚠️
با اعلام رسول باختر کارشناس حقوقی مطابق قانون پوریا شهرآبادی خرید جدید‌ پرسپولیس سهیمه لیگ برتری محسوب نخواهد شد
⚠️
رسول باختر: بر اساس قوانین بازیکنان سهمیه جوانان (زیر 21 سال) جزو سهمیه لیگ برتر محاسبه نمی‌شوند. این سهمیه شامل متولدین…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/137527" target="_blank">📅 17:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137526">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ترامپ : من دیگر ترجیحم این است با ایران به توافق برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/137526" target="_blank">📅 17:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137525">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
با نظر مدیران باشگاه پرسپولیس و موافقت مهدی تارتار؛ تیوی بیفوما در پرسپولیس ماندنی شد / آنا
❌
قرارداد بیفوما فصل آینده 850 هزار دلار خواهد بود…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/137525" target="_blank">📅 17:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137524">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🗣
آنا : حسین نژاد پیشنهاد پرسپولیسو رد کرده ، و جذبش کنسله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/137524" target="_blank">📅 16:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137523">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
✔️
فرهیختگان:
🔴
پرسپولیس همچنان با دقت درحال بررسی وضعیت حسین‌نژاد و قربانی است.
✔️
اولویت باشگاه حسین‌نژاد بوده ولی به شرطی که رقم رضایت‌نامه‌اش معقول باشه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/137523" target="_blank">📅 16:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137522">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
❌
❌
فووووری
👀
امیر جعفری در پرسپولیس؟
😀
برخلاف اخبار منتشره امیر جعفری مدافع چم ۲۴ساله گل گهر گزینه پرسپولیس و تارتار نیست.
✍️
قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/137522" target="_blank">📅 15:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137521">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
فارس: نساجی با جدایی و انتقال دانیال ایری مخالفت کرد و پرونده حضور ایری به پرسپولیس بسته شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/137521" target="_blank">📅 15:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137520">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
مدیرای نساجی اعلام کردن ایری تا نیم‌فصل جدا نمیشه/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/137520" target="_blank">📅 15:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137519">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq9K3niHeglWubB3hrG2huXliW0fOt9FiMZ5fUCYC_IR8LId5btzIR5vyiPQY379Vg1BAXpaN2HC-eN-f7aKrXyybWdMSmAwzg6bSpNshIb97muoNqo55erda5-ln2G4eMR-lG75FxWE_rC-mjPe1jAoVKeOocmyhWMPfbUGAS5-6sH0xV1JyCewSmHFcuR5KDvTRonNAOj9NtSnRphzP4Y3d9v9hM1qSa7ryGtgp3bcKkca7bUnK3Gggh5M591gUBrTxtZ5DwqvKho8CCVm8MR2RqVtfVGI938gQpSkxpMSZ49w8KYQWsre4qQ5T1Me8Y6HISb1W81lYJaBIsFJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
هاردکورت آماده‌ی یک روز پر از نبرد و غافلگیری
🎾
بازی‌های امروز مونترال ترکیبی از تقابل‌های نزدیک و مسابقاتی با برتری نسبی مدعیان است. روی هاردکورت، کیفیت سرویس و توانایی حفظ ریتم از خط پایه اهمیت زیادی دارد و چند دیدار می‌توانند به ست سوم کشیده شوند. در مجموع، انتظار بازی‌های فشرده با چند شگفتی احتمالی را می‌توان داشت.
⚽️
بازی‌های امشب رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/137519" target="_blank">📅 15:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137518">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
رسمی: با اعلام باشگاه مرتضی پورعلی گنجی و سروش رفیعی از پرسپولیس جدا شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/137518" target="_blank">📅 15:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137517">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
#فوری
❌
مدیران باشگاه نساجی تصمیم گرفتند حداقل تا نیم فصل دانیال ایری و کسری طاهری را نگه دارند، بدین ترتيب حضور این دو بازیکن فعلا در پرسپولیس منتفی شد.
✍️
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/137517" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137516">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
بازیکن آزاد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/137516" target="_blank">📅 15:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137515">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⚠️
⚠️
بیفوما ماندنی شد
⚡️
⚡️
پس از آنکه در فصل گذشته تیمی نامتوازن بسته شد و تعداد وینگرها به شکل عجیبی زیاد بودند، مدیریت پرسپولیس برای هماهنگ ساختن تیم تصمیم به فروش یا فسخ قرارداد با بعضی از وینگرها گرفت.
🚫
🚫
تیوی بیفوما وینگر کنگویی پرسپولیس یکی از آن وینگرها…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/137515" target="_blank">📅 14:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137514">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
باز بازی از اول شروع شد ..دیگه خسته شدیم
❌
#فوری از آنا
🗣
کسری طاهری و دانیال ایری تا پایان نیم فصل اول در نساجی ماندنی شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/137514" target="_blank">📅 14:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137513">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
مخالفای جذب رامین در پرسپولیس خیلی بیشتر از موافقانشه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/137513" target="_blank">📅 14:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137512">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
باز بازی از اول شروع شد ..دیگه خسته شدیم
❌
#فوری
از آنا
🗣
کسری طاهری و دانیال ایری تا پایان نیم فصل اول در نساجی ماندنی شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/137512" target="_blank">📅 14:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137511">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
✔️
فرهیختگان:
🔴
پرسپولیس همچنان با دقت درحال بررسی وضعیت حسین‌نژاد و قربانی است.
✔️
اولویت باشگاه حسین‌نژاد بوده ولی به شرطی که رقم رضایت‌نامه‌اش معقول باشه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/137511" target="_blank">📅 14:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137510">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
تارتار، به بازیکنان و اعضای تیم هشدار جدی داده که هرکس اخبار و مسائل داخلی تیم را به بیرون درز دهد، بدون تعارف با او برخورد خواهد کرد تا قصه تکراری «جاسوس» و حواشی رختکن را برای همیشه تمام کند.
✔️
✔️
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/137510" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137509">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
قرارداد گرا ۷۰۰ هزار دلاره که ۶۰-۷۰ درصدشو میخواد
⬇
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/137509" target="_blank">📅 13:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137508">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
قدوسی: مدیران باشگاه پرسپولیس به ما گفتن با وجود عنایت زاده، باکیچ، خدابنده لو ، پورعلی و لطیفی فر امکان جذب توأمان هر دو بازیکن (محمد قربانی و محمدجواد حسین نژاد) وجود ندارد و یکیشون جذب میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137508" target="_blank">📅 11:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137507">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
تارتار جاسوس را پیدا کرد؟
👍
شنیده میشود تارتار تعمدا چند ترکیب را در بازی های دوستانه در اختیار چند نفر میگذارد و مشخص میشود چه کسی ترکیب را به برخی کانال ها میدهد. باید دید در شروع لیگ باز هم ترکیب پرسپولیس به کانال ها میرسد یا تارتار بعد از هشت سال مانع…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137507" target="_blank">📅 11:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137506">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
❌
علیرضا بیرانوند این فصل سرباز هست./ ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/137506" target="_blank">📅 11:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137505">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSC-xhBbbHRAeYhJLY84ZuBRBmbuKdcNpZav-NdxLwg0JH68dItGhYL9ukjtXXqHbVxOjyEcUVsA7bBwL-DeYHzWYSlrlwrvyJCAVLt1wFAowmzVcGdIcLq8GqKA75s-RYeaq4P6Vd4bBxF0HzArKKMGqHUjCnSDfvay6H92IoK_vKQzyE4vARKFXOZaudhm0bkBZvpwZO6iG6uHN2mliq_EB8rhiPKawRkZsLrZntcLxOkEiizu-AmES9ygUze5N93NOkE7G9iXXvEkhyV4x-i8ZCRek9l85ceH9Xdx6fiwvrMQk078tIgD93bajkXC8Q3rrIe5vEqTs_Fy1JQWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
فرهیختگان: ماجرای محمد قربانی داره شبیه پرونده محبی می‌شه، تراکتور منتظره قربانی بازیکن آزاد بشه و رایگان جذبش کنه، اما پرسپولیس می‌خواد با پرداخت رضایت‌نامه به الوحده، این انتقال رو نهایی و دوباره هایجک کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137505" target="_blank">📅 10:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137504">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRGc4myyj9Xt-3aSsael-vmERtsY5DR567Nc_TrgICmAqHHv0o6ADvgHO_w8PfxCA6Iip5zU5fo9UYmCROrsAj-iFZKRZAwnYtWjvmEXIJSyGRV6C-Q2j9Kia6vDz9SZgnuInUHjbHiuuL5epQzDzf_eDxGh0rB0J3sQh6HJx_LaOUBoNk0VF9OJ1BJe-mnzT1OoVUU8DfKqVshDJlzoCxsD4T9ONxz0xygEnNgO8Orv2oU56YYwPfokxY2Hq2MsK1jUCPNHfaStZErykybseOEyu0xwiOZt0XghtLlt-SM_BiKbJNSjCf2-fUtdJ66i3_JuUp_qXr6ea4RVGllSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔹
🔹
🔻
هزینه رضایت‌نامه ۴ خرید پرسپولیس روی همدیگه تازه میرسه به رضایت‌نامه سعید سحرخیزان، بعد رسانه‌ها تیتر میزنن ریخت و پاش پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137504" target="_blank">📅 10:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137503">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
هوشنگ نصیرزاده، وکیل بیرانوند در دادگاه CAS: چه قبل و چه بعد از جام جهانی هیچ چیزی بیرانوند را تهدید نمی‌کند. اغوایی توسط تراکتور انجام نشده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/137503" target="_blank">📅 10:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137502">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
اضافه شدن بازیکنان امید پرسپولیس به تمرینات بزرگسالان
🔻
🔻
با اعلام باشگاه پرسپولیس، در ادامه سیاست‌های باشگاه پرسپولیس در مسیر جوان‌گرایی و توجه ویژه به استعدادهای تیم‌های پایه، با درخواست پیمان حدادی، بازیکنان تیم‌های پایه که دارای قرارداد حرفه‌ای با باشگاه…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/137502" target="_blank">📅 10:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137501">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
قدوسی: مدیران باشگاه پرسپولیس به ما گفتن با وجود عنایت زاده، باکیچ، خدابنده لو ، پورعلی و لطیفی فر امکان جذب توأمان هر دو بازیکن (محمد قربانی و محمدجواد حسین نژاد) وجود ندارد و یکیشون جذب میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137501" target="_blank">📅 09:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137500">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
شایعات: رامین با مبلغ باشگاه کم و بیش موافقت کرده و تارتار باید تصمیم بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137500" target="_blank">📅 09:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137499">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwefL0N3SMGCE3-1VHOkWEcKlNs_aj_YvnDSjGGG6_R6B7zFET0fbtqGYYIZ9-AhXAVPCHo-d7jExp1C2gf0KwG0qkpzynWeKB78iBGtnNb6NXByUnmyqmxM3xb0ozeIuS2ROzK-LqMEINeVX1h9CSC-adzo3E47BGlwy1k7ZWug1MGALd7Do0aDVakEZTgVlHuQ09RVTKdBp4bLUEkpCsu4CnJu-y999p6tFVevroOecIg6jwO81sLVv8kuXYeTaS6TwaYbBVEZr6Z6JUys6l3J8rRBjYoa60k1rmZGC-EDUGoSJcWoipfvw9vURQvU5iPB16XHck8GYHgTxJmuxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/137499" target="_blank">📅 09:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137498">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0995cd13e9.mp4?token=Kwj9G--FRaTKewUz-ryNRdK_gsUsLdGbr3i_WPQKdZ5Pj89BXvEdNO4KPyUkbcJGUYScq8Gk-7ubElz9Dm3QNO64PMWp_o0gaJMMsGZf2ttuFJ6M6SbVVEU6Sb-yIKKWz25EtwCgNlIuY_ac2qxnKZUdghiRoJxfhss65YAtAFhPsdQ3eII2vAab0_d9OZ9CsXOP0v_T3CPphG6J789PRfpfPqH8YcD8X4kMKNseSdk-ikOD3RG8BtG0CCFbP3Je3srnrOwooLTHY1qfYR5_k-g6pcYljP-OdRbH1jQ9ALGqZeyIFfZcqiC2fPd5qiX5eiyMiIukb2Bgmd70A8Zgw4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0995cd13e9.mp4?token=Kwj9G--FRaTKewUz-ryNRdK_gsUsLdGbr3i_WPQKdZ5Pj89BXvEdNO4KPyUkbcJGUYScq8Gk-7ubElz9Dm3QNO64PMWp_o0gaJMMsGZf2ttuFJ6M6SbVVEU6Sb-yIKKWz25EtwCgNlIuY_ac2qxnKZUdghiRoJxfhss65YAtAFhPsdQ3eII2vAab0_d9OZ9CsXOP0v_T3CPphG6J789PRfpfPqH8YcD8X4kMKNseSdk-ikOD3RG8BtG0CCFbP3Je3srnrOwooLTHY1qfYR5_k-g6pcYljP-OdRbH1jQ9ALGqZeyIFfZcqiC2fPd5qiX5eiyMiIukb2Bgmd70A8Zgw4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power x1000 فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ حساب کاربری، ۱۵ فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
🔹
پس از واریز، بونوس از طریق نوتیفیکیشن داخل حساب کاربری نمایش داده می‌شود و از همان بخش می‌توانید وارد بازی شوید؛ نیازی به جستجوی نام بازی نیست.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
sportn5b2.com
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137498" target="_blank">📅 02:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137497">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjQ-LoUqeiNeDW8rh2pDOZ5-K-vuBjKhnWHuOqmLHjdHHqmPrkwAzubbNYfmr2mxkWD_nwrduzL44udasBZfoJYIgxPXoGY6agVX2kkjP1LBrOltnmkTXSNndA4MDebtXoKTPxfgM3C_s-cYbATGOmo0ejqSY86-ThoVUjK1D0__0kpDUX1Xosm_c5EoHow02q2od0-K-unsGowO9I05kSI2rPklRb0Qc8Yd90bfgVudy0DychROt5eNB-Km0RXxHPq3Dmid0EYGkCUNfeA3kIHaHIyGgUrURWbPkRCYpJc8FGNvmkidVDE65lmxXP9mL3czL7c7X0GRVVyaSnW3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شبتون بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137497" target="_blank">📅 01:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137496">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
❌
🔹
🔹
برای محمد قربانی فردا جمعه میتونیم بگیم تمام و مبارکه
🤝
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137496" target="_blank">📅 01:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137495">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
قرارداد گرا ۷۰۰ هزار دلاره که ۶۰-۷۰ درصدشو میخواد
⬇
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137495" target="_blank">📅 01:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137494">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔹
🔹
🔹
🔹
پرسپولیس و الوحده برای قربانی فردا تفاهمنامه امضاء میکنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137494" target="_blank">📅 01:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137493">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tne38HrAGRp4kl06rPEjtFcG9qSXnghSSYsULcLo9IXIrLblgqd79kks9fBrjxopn3OfF53IYaRwP8Rm7N2eViOuvqYFUaYJ3t7PjdqH1hSPgtD3ywMFR1Lg_LSc9b5KMfLNZsLzF2j3P3HEsRzltIRDENHmOf5gfbn6ZYZhpqQY6UHT2Sho-8DD59E_kcx2IVm8YlkQwHuBZaoWIAcEBZQuPsy4hyNbBWq8plWMjOXhX7zPRt6SUtcLTfWArGAk4EzkkJMU9ftBxapfaMvjszP_euHLwGJW0bLlqafgbsdNPrpLY3PQwG6H5OCXgGeSn6Cf99YAp-4786AhzHO6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
باشگاه پرسپولیس در حال تواقق نهایی با هواپیمایی وارش متعلق به مالک نساجی تا این ایرلاین یکی از اسپانسرهای تیم در فصل آینده باشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/137493" target="_blank">📅 00:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137492">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
#تکمیلی | ترامپ:
🔻
من در مذاکرات با ایران مشارکت دارم. اوضاع به خوبی پیش می‌رود.
🔻
احتمالاً به زودی به توافقی دست خواهیم یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/137492" target="_blank">📅 00:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137491">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
ترامپ : من دیگر ترجیحم این است با ایران به توافق برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137491" target="_blank">📅 00:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137490">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
فوووووووووووری
🚨
طبق گزارشات رسیده، پرسپولیس به جذب محمد قربانی خیلی نزدیک شده و امکان عقد قرارداد‌ طبق مذاکرات انجام شده بسیار زیاد گفته میشه
😀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/137490" target="_blank">📅 00:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137489">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔔
🔔
🔔
تراکتور با قربانی توافق کرده بود که بعد مازاد شدنش رایگان جذبش کنه که حدادی به الوحده نامه میزنه و حالا تیم اماراتی میخواد او رو به پرسپولیس بفروشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/137489" target="_blank">📅 00:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137488">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
قدوسی: من اسمی به جز حسین نژاد ؛ قربانی و رامین رضاییان نشنیدم و سوپرایز خط هافبکی که ورزش سه گفته احتمالا بین دوتا اولیه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137488" target="_blank">📅 00:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137487">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✖️
✖️
✖️
قدوسی: رامین دیده مشتری نداره و گفته با ۱۵۰ تا میام پرسپولیس میبندم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/137487" target="_blank">📅 00:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137486">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⚪️
⚪️
⚪️
پرسپولیس برای تکمیل لیست نفرات خود در پست‌های دفاع وسط، دفاع چپ و هافبک، به دنبال جذب سه بازیکن جدید است. با توجه به محدودیت‌های سهمیه لیگ برتری، سرخپوشان برای دور زدن این چالش قانونی، استراتژی جذب بازیکنان آزاد را در دستور کار دارند؛ بازیکنانی که تا…</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137486" target="_blank">📅 00:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137485">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووووووووری
❌
❌
باشگاه الوحده امارات در آستانه توافق با باشگاه پرسپولیس برای انتقال محمد قربانی به پرسپولیس /فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137485" target="_blank">📅 23:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137484">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/137484" target="_blank">📅 23:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137483">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
دنیل گرا از پرسپولیس کنار گذاشته شد، اما برای فسخ قرارداد بر سر مبلغ جدایی با باشگاه به توافق نرسیده است.
❌
مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137483" target="_blank">📅 23:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137482">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5wLL6Bc5xsbOFxsuTeNPvPE4XxPJAWqRGT8zdBJGGXBr1pX9Qx6YPYYostqc2b_MQA8BPnOfwBmdX1YTmPWJIuUTgzXd0N78JbMzh84OqQIexscBrDq947YJ7eeUBJWRspxV4A1TBAjRLwP7m9M11_Xj9o6xyBfyeU-nrEhQpFg10YedPK5yPTGh_2CnlMK2eQdkRiYb6hrYx5oYfijJDRH3m4EBM10hs8yXgf1di4FZbW-X4K7PzOwerMQijfWsNHGu-UhChHbm__n5C54OCvGUT2pG538N8D-fes4-ctFYEP-GG9myS_MFI2vPf-RZxYVqYR-uboq-rKY66kQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
میلاد محمدی تو اولین بازی تیم جدیدش امشب تیمش تو پلی‌آف لیگ کنفرانس تو عرض کمتر از ۱۵ دقیقه ۲ تا کارت زرد گرفت و اخراج شد :)))
😄
😄
😄
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137482" target="_blank">📅 23:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137481">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
قدوسی: من اسمی به جز حسین نژاد ؛ قربانی و رامین رضاییان نشنیدم و سوپرایز خط هافبکی که ورزش سه گفته احتمالا بین دوتا اولیه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/137481" target="_blank">📅 23:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137480">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fz5NT_pxBtmpNqwOCfgfXeqKtPNH2QXM587uWrejk0Bh7IgYpaahy1WfNjIJ9PiPg9VAbzsjI911lpv8c0tUeaVkdUebvbN5EBvX7yVp3XyT4MyoNLtMo2O164tP3cirhsZr6UuvHXT9EnJ1nwF-J4DtmGOKGZcjKe5cnTMCWljqC1cAQ0j72YOkJWzCDfkHxOVX_xiqVgCsvrplbL-G12OYdonhw4mG2RbCQDw9uHhqNswMrYrdzg2ODnlQKP84zvjqcnXLCCeT0NP6xSQ1v9lhQLCV5lUvHQ1ctwau4TNnO0dWQ6EAqvsnnbOvNfC32DoneLyRgfAF6t3QagZ44A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
علیرضا اشرف پیش از تمرین امروز بعنوان مدیر رسانه‌ای جدید پرسپولیس، معارفه شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/137480" target="_blank">📅 23:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137479">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⭕️
تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137479" target="_blank">📅 22:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137478">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
العربیه: تماس‌های غیرمستقیم میان واشنگتن و تهران که از طریق میانجی‌ها در جریان است، وارد مرحله نهایی شده و در حال حاضر، میانجیگران در حال تدوین سند نهایی مرتبط با بازگشایی تنگه هرمز هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137478" target="_blank">📅 22:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137477">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYAtvlNuDr1dI1M2l914bq6Xd8jWtLYDENdu6MjDPO85GJ9oXFjwAHWnJyZ0dU-L-dGLW2j8KjJ2ekvXK-0cBoCpk6NNVLCaol6bO3CTBSzwVRfGPzlQjWTSdpZqW5a3esm3DXzlhxt11IMjypywgP_3JCHB86EHlko6c3PcAJm2lVXnXu4-8mKxIC7TXgQ_clc209qZ9HLbX-oIzXsC2PxsoTPhpbzni8Ciay9cK3Aa_ym_9dAU5uTKGbCoz5MQoH3bPLI6hQBci7zSDfYq2xrIMKLj5_o7aVr9R5IVCzIr2H4BNJoHxbu_ONr8HAIbWFYVsWvGOj6OjpuHe6z2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137477" target="_blank">📅 22:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137476">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKHwgthw5TukqSftBP-GLTQviXPbpywxOlgwuuy_UshS_IxC6NJzVGFLVGNM0UUbLmFAn-7SmjU8-VwxcBTUfdHBI9A7XXICwQJNILJ7ghrTN0D1KH1Mks7ATc0zf5Fd3ZnuFP5VeLANaGhL-s0dXL2FhXakWLT0OxSWfN6oSGS3KIE-9Zqhlq79ofKhza1pTfhJ9zqfLYyj0uLQ2lJ195kSgNuU_iJ7jdn9CbW5D63PgjW3_jgNykBndO-cNHY6o64zgTKQkI6HBPvmKez-hmKuW1KD5XblQAX3QMTh89GaS132cHIPmNWS5xMhFstaXxTwKt8oLOSxN4vc_udd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7️⃣
تنها ۲ روز تا بونوس ویژه ۱۵ چرخش رایگان بازی Egypt Power x1000 باقی مانده!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ حساب کاربری، ۱۵ فری اسپین رایگان
Egypt Power x1000
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
⚡️
پس از شارژ حساب کاربری و فعال شدن فری‌اسپین‌ خود، وارد بخش بونوس‌ها شوید و ازین فرصت چرخش رایگان نهایت استفاده رو ببر!
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137476" target="_blank">📅 21:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137475">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIA2n8jFFexOFmyAdPcsOzt7y_xHkEgw9MVruDdU_pC15zXoIA1_jhGiR0aRK3LNy7JeKLHTwbQ45bYRQSnlbdpTlpyLLfUY3c0RV_khWo6Uu_-KnLO_zqyt6XQfDbIVOBg4gh8p2S9I37JrO5ZBJaPQEIkLIgk6y2z43l7krDcSsBvxt9vGAXuNtu5OEsFvAiWLx0FufQr72UwyMlSOzAxUATL3XdBmx_3LZXF0NrelSlnYktBYn2Hr8xqw5HVYTi35sgpWIbtXyyxEnLyhPiq1vy0Uub9Ts2xsSnRxX8-oZgn75ei4aVV6rBNBsERD-DoUIZwhebr2pzPQQdlj6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اضافه شدن بازیکنان امید پرسپولیس به تمرینات بزرگسالان
🔻
🔻
با اعلام باشگاه پرسپولیس، در ادامه سیاست‌های باشگاه پرسپولیس در مسیر جوان‌گرایی و توجه ویژه به استعدادهای تیم‌های پایه، با درخواست پیمان حدادی، بازیکنان تیم‌های پایه که دارای قرارداد حرفه‌ای با باشگاه هستند، به تمرینات تیم بزرگسالان اضافه شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137475" target="_blank">📅 21:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137474">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
قدوسی: با فروش علیرضا ملکی از نساجی به خیبر، پرونده فروش طاهری تا نیم‌فصل حداقل بسته موند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137474" target="_blank">📅 21:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137473">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
‌قدوسی: کسرا طاهری موندنی شده و بعیده این پنجره از نساجی جدا بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137473" target="_blank">📅 21:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137472">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✖️
✖️
✖️
قدوسی: رامین دیده مشتری نداره و گفته با ۱۵۰ تا میام پرسپولیس میبندم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137472" target="_blank">📅 19:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137471">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
⚡
پایان همکاری استقلال و رامین رضاییان
⏺
به گزارش سایت رسمی باشگاه استقلال، با توجه به مفاد قرارداد یک‌ساله رامین رضاییان و عدم پذیرش شرایط پیشنهادی باشگاه از سوی این بازیکن برای ادامه همکاری، همچنین با پایان یافتن مهلت تفاهم‌نامه فی‌مابین، باشگاه استقلال…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137471" target="_blank">📅 19:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137470">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137470" target="_blank">📅 19:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137469">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137469" target="_blank">📅 19:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137468">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
آسوشیتدپرس: پیش‌نویس توافق درمورد تنگه هرمز نهایی شده و در انتظار تایید مجتبی خامنه‌ایه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/SorkhTimes/137468" target="_blank">📅 19:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137467">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
❌
ورزش سه: مهدی تارتار از روند نقل و انتقالات پرسپولیس راضی نیست و مدیران باشگاه پرسپولیس دارن لیست خرید شو روز به روز کوچیک تر میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/137467" target="_blank">📅 19:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137466">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووووووووووری
❌
ترجیح مهدی تارتار از بین محمدجواد حسین نژاد و محمد قربانی جذب محمدجواد حسین نژاد است و مذاکرات مدیران باشگاه پرسپولیس برای جذب این بازیکن آغاز شده است / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/137466" target="_blank">📅 19:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137465">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
حسین‌نژاد اولویت اصلی پرسپولیسه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137465" target="_blank">📅 19:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137464">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPWUFAdKT6NL7lDODAIctR90UTldXx4dhirkWkVs7O3z9j7BMu5MXxLpQHi9q0QPrWh9KXBObnCN8G0zodzdM9CJGCoSI2WKH_xq03p9e0z9DRcbm60AUVVopISHu-26TpkdWm_VCBZINfodVpx506XE8TP08dBVe5_aFzFmaQcYwd4VNuHkCx8TVarhg7AEcIDwTvzZamSQoL2Nw98yPjO2F1NCctY3sgRRewdNiqYLpe58E0jjYyhI07ZYeEbY53pjCbSkxoB0gUO1hLI8LZx-RLCHZ24L4hWVlqjXNxtyZG02ZH0p2Cy6zkWs_m4eV5GxdjxxA3hP5y_pgA2pDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حسین‌نژاد اولویت اصلی پرسپولیسه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137464" target="_blank">📅 19:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137463">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVHgeakNomZeKuHjCEjv1kn2PBD0a__FuRIpW8aSVPIMXcyLyqwk5Y5H4SSoR4A6Jf9GYfyVKRGwj5FMetH8EEigfb1UB4Enbb8XgiUqwlRKSM1n81pI_qpt5uq_aEYpbYif7KuB-PgCqM0qhfDxSOVriWQD95_-_DbQee-wBoaGHrBvAnVEphC-uaVoINgv6s65YiPnTJXL2WBmzVPq4pcZN8hYr2Ulg-he2CrvOBPaMoE5rmRvLY25m8vNb84RtPZm06Eme2WpPhqYrn9_Uy0YFLj7Fl9iHGvLpvxzQ62RQLsct2c8qCuRHLzJ4IZ6ndXIwt3LrVsKrghZfZILkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انتقال دانیال ایری به پرسپولیس به دلیل اینکه این بازیکن بیش از 16 هفته پیش با نساجی قرارداد بسته پل‌ محسوب نمیشود و این بازیکن در آستانه عقد قرارداد با پرسپولیس قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137463" target="_blank">📅 19:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137462">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
پرسپولیس در مذاکره با دنیل گرا به این بازیکن پیشنهاد داده که با نصف قرارداد فصل آینده اش بیاید فسخ کند که این بازیکن این پیشنهاد را رد کرده است و خواهان تمام قرارداد فصل آینده اش شده است..
✍️
خبرگزاری مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137462" target="_blank">📅 18:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137461">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
❌
محمد امین کاظمیان: آقای تارتار به من لطف و تمایل داشت بمانم و باشگاه پرسپولیس هم موافق جدایی من نبود، اما در نهایت تصمیم گرفتم جدا شوم، چون دوست داشتم در تیمی بازی کنم که شانس بیشتری برای حضور در ترکیب ثابت داشته باشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137461" target="_blank">📅 17:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137460">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
❌
فرزین معامله گری سرباز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137460" target="_blank">📅 16:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137459">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
اعتراف تکان‌دهنده رامین رضاییان بزرگ‌ترین اشتباه زندگی‌ام را کردم!
🔴
طبق شنیده‌های کاملاً موثق، رامین در محافل خصوصی صراحتاً اعلام کرده که پیوستنش به استقلال، بزرگ‌ترین اشتباه زندگی فوتبالی‌اش بوده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137459" target="_blank">📅 16:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137458">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
اعتراف تکان‌دهنده رامین رضاییان بزرگ‌ترین اشتباه زندگی‌ام را کردم!
🔴
طبق شنیده‌های کاملاً موثق، رامین در محافل خصوصی صراحتاً اعلام کرده که پیوستنش به استقلال، بزرگ‌ترین اشتباه زندگی فوتبالی‌اش بوده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/SorkhTimes/137458" target="_blank">📅 16:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137457">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
💙
رامین رضاییان میشه گفت تنها بازیکن جهانه که از نظر فنی فوق‌العادس اما از نظر اخلاقی و رفتاری میشه گفت بدترین بازیکن ممکن و با تمام مربی های کریرش لج افتاده ؛ بنظر شما حق با مربیان بوده یا رامین رضاییان؟
⚪️
رامین رضاییان
👍
⚪️
مربیان
👎
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137457" target="_blank">📅 16:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137456">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔔
🔔
گفته میشود مبلغ قرارداد تیوی بیفوما در فصل آینده 850 هزار دلار معادل 140 میلیارد تومن است و احتمالا در پرسپولیس خواهد ماند. باشگاه فولاد خوزستان حاضر به پرداخت چنین مبالغی به او نشده و پیشنهاد معاوضه با رزاق پور را رد کرده است
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/137456" target="_blank">📅 16:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137455">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
امید عالیشاه بعد از 13 سال حضور در پرسپولیس به گل گهر سیرجان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137455" target="_blank">📅 16:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137454">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
از اونجایی که پنجره کیسه بسته میمونه راه پرسپولیس برا جذب بازیکنانی مثل ایری و حسین نژاد هموار تر شده و فقط باید بانک شهر سر کیسه رو شل کنه و یه تیم جوون و درست حسابی ببنده برا امسال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137454" target="_blank">📅 16:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137452">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
🔴
👀
ورزش سه: پرسپولیس در آستانه جذب یک هافبک قرار داره که گفته می‌شه یک سوپرایز بزرگ برای هواداراست!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137452" target="_blank">📅 15:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137451">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
❌
خبر ورزشی : پوریا لطیفی فر خرید جدید پرسپولیس سهمیه لیگ برتری حساب نمی شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137451" target="_blank">📅 15:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8uNoF4Gz32p6OEwlJzWLxtHwPZMP5IdPcD0Y2F9mM2L8_QfEaAPsxxH110werNorqM_ZIZz-ROXinzq9mWCOZOWAwgmKg2sU09KQIDSXkWcsJiWjD2su9IafZMBwcrswlz4tjWH-LTBFSF3FbwojYFDCP4agOaO2c6fwBblIW6Gu22e0-fRcxgRLx6AzomC4kE-oK3WC8sVg0bMi623o2rbLUi4LgkQO-Cm2CaE2DyrV-suHj2IoqDwuf1OpriOMCrM9XSRwy5lWN0HZEMsVjJzKCgltQYx_ro9XSIocnoivSUyxPz95QBsglN-uaGSB7q6HdCXdIZ1SG-WN3GKUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
پیمان حدادی سفیر افتخاری چوگان شد
😀
✔️
دیدار مدیرعامل پرسپولیس و رئیس فدراسیون چوگان؛ تأکید بر همکاری‌های مشترک در توسعه و ترویج ورزش ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137450" target="_blank">📅 15:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137449">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
آسوشیتدپرس: پیش‌نویس توافق درمورد تنگه هرمز نهایی شده و در انتظار تایید مجتبی خامنه‌ایه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137449" target="_blank">📅 15:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137448">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwsFdTgbcwshhNS3y_G0vuMlBvwsHu6bvQ7J8EnMhCF_gB3yx8qi4VHWhGjdUU-KHN1r4WuXwmf_-zdeREbWL084eIlxfgqaWsJiPrULiUKygepXeE_XTyF3GnwP-zvNMCx4i0DzwokQl8hz9QtMl0j80VPrz8R-5thQkT40DuFbXpOkpDfe24mI0bOadiYCgLOn60mUfClHpqdmSinB64BW4CYmEsPyFls1DWT6uSVmiRUDF2DMfjGBqUxwUmP7dxr2M3IDH0IJMKJTXBcksRb3Cpm1NE5_2arAD4BNL3MP5FHPvzlOyJ19soDBpgqtX8Yi_Xd_yiUYWYlduJZDdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🔴
ایمن حسین مهاجم ۳۰ ساله تیم ملی عراق، در انتقالی آزاد با قراردادی یکساله به پاختاکور ازبکستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137448" target="_blank">📅 15:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137447">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
باشگاه پرسپولیس هنوز در حال مذاکره برای جذب دانیال ایری است. اگر مبلغ انتقال شفاف و مطابق قوانین باشد، احتمال نهایی شدن این انتقال وجود دارد / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/137447" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137446">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🚨
آخرین مرحله مذاکرات پرسپولیس با نساجی برای جذب دانیال ایری با در نظر گرفتن تمام جوانب حقوقی در حال انجامه / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137446" target="_blank">📅 15:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137445">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeA4HnRnESEUFqHTmWMMQKeU8lf6p6uvP8dSN5cuEkLmfuxJ98-X2LbueteJvi680fuyA_7I-4jBrThE9cGMrt45fm12kqDCNKCilEIn5zOda53Vahns-aeedCVzdNKY3dfCB_Erp292JXreMf1wsvZFhkFiJ1pxGoqTR5YtpvPIHXO65KNZJ1azv4TOKiT0aotJMC5acAIaf2_JL6aUB8bhhx7EiZ5BBWJhdPaT6RLUpG-tPbuJpU1Tvj8_rm6HbNYiiiIGu7XdGIKuihNStJZqXQJgHctdoGRmXy4y53HpdJq0WlRwOP_IbC-hr1oq-UkVcC-bOjBLR8_ckd1D3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
نبردهای حساس لیگ اروپا؛ آغاز مسیر صعود در شبی پرهیجان
⚽️
دیدارهای امشب دور سوم مقدماتی لیگ اروپا، تقابل تیم‌های باتجربه با مدعیان جاه‌طلب را رقم می‌زند و نتیجه بازی‌های رفت می‌تواند نقش مهمی در تعیین سرنوشت صعود داشته باشد. رنجرز برابر یاگیلونیا، بنفیکا مقابل هارتس و سالزبورگ برابر پافوس از مهم‌ترین مسابقات شب هستند؛ دیدارهایی که انتظار می‌رود با فوتبال هجومی، فشار بالا و رقابتی نزدیک همراه باشند.
⚽️
بازی‌های امشب رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137445" target="_blank">📅 14:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137444">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📎
📎
📎
یه سوال پیش میاد اگه واقعا حس میکنید هنوز تو دفاع راست مشکل دارین پس عیدی چرا جذب شد؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137444" target="_blank">📅 13:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137443">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
آخرین مرحله مذاکرات پرسپولیس با نساجی برای جذب دانیال ایری با در نظر گرفتن تمام جوانب حقوقی در حال انجامه / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/137443" target="_blank">📅 13:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137442">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⚡️
⚡️
خوش‌آمدگویی پرسپولیسی‌ها به محبی
🟪
🟪
کنعانی‌: بازیکنان جدید باید بدانند به چه تیمی آمده‌اند. خوشحالم محبی به این تیم بزرگ آمده و امیدوارم لژیونر شود.
🟪
🟪
علیپور: در جریان بودم که محبی چقدر دوست داشت به پرسپولیس بیاید؛ به او تبریک می‌گویم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137442" target="_blank">📅 13:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137441">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه نساجی برای امضای تفاهم نامه قرارداد ایری امروز و فردا می‌کنه/ قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137441" target="_blank">📅 13:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137440">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jeo223NLxlKQgl2PYCYiGz4dXKph7nRqmBoiCUwta61wvEKUIc2CsVYp8gyerB6V54ZzIGfunXHYu7NOs-__8hpp4CKjKQeYb33eRP3vfsOP_41Dc1PJFicAMHvQraPA2L192hG6Hq3Mp_yHnj17MhbUKwFDfKQppqogmYtc-jrQn4juMeFTPHVNIwvw00Aq7AdX_ijwEQw9lJ41VlPotC24-UQCW8Qc70RseRwmnvzRubslpsNX_QC0Lqf2LiqwTrBJy_jSUF9DSsiBzbQ6ih6wP9VCySJ-EGaycmlbiHmNmI3MZVy8WVmeLDYkprhI67gFw77MdUYCm0K1B-nyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پرسپولیس در مذاکره با دنیل گرا به این بازیکن پیشنهاد داده که با نصف قرارداد فصل آینده اش بیاید فسخ کند که این بازیکن این پیشنهاد را رد کرده است و خواهان تمام قرارداد فصل آینده اش شده است..
✍️
خبرگزاری مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137440" target="_blank">📅 12:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
❌
تارتار گفته جذب دفاع چپ خیلی مهمه و درصورت مصدومیت جلالی تیم دچار مشکل میشه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137439" target="_blank">📅 12:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137438">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">💠
💠
💠
پرسپولیس با وجود ۸ خرید، هنوز در خط دفاع، به‌خصوص دفاع وسط و دفاع چپ، کمبود بازیکن دارد. اگر این ضعف‌ها برطرف نشود، ممکن است از همان هفته اول لیگ برای تیم دردسرساز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137438" target="_blank">📅 11:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137437">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🫥
🫥
🫥
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137437" target="_blank">📅 11:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137436">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5EP4uoxFlB_uCRRwrrsqXQC1SSgvhFwJB5jSdog81bepuG1Bj56yw5taDvVSFLkDllKJ7kV_KWb4KBwQQcputBafcJq_IiuAVZ1OIUyR3wfiLdRK1OkgPz2ji4ZZ9za6W1H5o8ncXoTQS_GfKfwbTPG2Tyn1IjR8SsDvljFR7yDPcqjbWAq41XgmtWq26cJW2u8RMoKw2jgDcFMKB6OzVXeUK2IE65DfqplT4Te1qOuqkKT2qU07So9Bs8KobZxv9-YED_a4H8XWhTQugC-WSXv4cpXx1gjS3VD7VsACY1jvr-Og863aBb_GbGf6gMZhSNRMsN-ME9QkRlfpBmmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
💙
رامین رضاییان میشه گفت تنها بازیکن جهانه که از نظر فنی فوق‌العادس اما از نظر اخلاقی و رفتاری میشه گفت بدترین بازیکن ممکن و با تمام مربی های کریرش لج افتاده ؛ بنظر شما حق با مربیان بوده یا رامین رضاییان؟
⚪️
رامین رضاییان
👍
⚪️
مربیان
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137436" target="_blank">📅 11:46 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
