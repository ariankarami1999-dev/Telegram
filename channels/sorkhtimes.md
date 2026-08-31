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
<img src="https://cdn4.telesco.pe/file/gh9N0Hke1pXe517XlndyDM_mLhIkNwjYMI4ZDR078KPRQu2M-xB1RVATOBGZuyzUG9hWa6tvrsaqLsS2VXUgHo-k03adIpN6IGv0g88J3isu6j1KR2skzq6ep_nmFwA-8Q0S14j64GQwTllOyIcWr4XQNRcC48K-0LQJeUgRtFHD8CBIyJA2IECJiXpaMpg7W0BrzEf9cPKX2bcIWxbMwH0uQGPa0YY05_EH_7zBOn434E3IoEiKDlfHJZ0IaGLyLsJcKKUnWu_YmrzDjRutXKonY7MreQJFg0BuAbEz0iVhEGHVyCs6K_5Qafuw3cFQF1-eiYCEW3TolY0MtoSehw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-139316">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WprF-r1orTYstjavr5zKJMxE5z9_Y6bwpGxoeBv-GvGOgSfjHqTJZCwEs4yE_JQ_jaHn3y85VTqAeHgnUxMr7Cct9JCnkXHxeJXTnx2dYZSx0APT0np-1o1KvCEb3cfPC4iQYNQWVTVj0jUdD-G4q3phbdzm_bl4H6_93YXOhjjITZ53_ZRqzW-bOC7VvNQS3QAhPg4T-p40HiYaJKIi4Y4clqQUaf4EQb75QxpEXhjWpR0ssfB3uWFXLKPiwWfQXX1MujwHnYcwZLi_oqEytsABGzdy_LDKvMe4RKr_3I3BC4cQFrSqwsZy5cGF-tDqy2QzFNUdCmpLFePJuoYdrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بارسا به دنبال ادامه مسیر بردها!
⚽️
رایووایکانو آمده تا کار را برای کاتالان‌ها سخت کند؛ نبردی برای صدرنشینی جایی برای لغزش نیست!
[
بارسلونا
🔵
🆚
🔴
رایووایکانو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 739 · <a href="https://t.me/SorkhTimes/139316" target="_blank">📅 20:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139315">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
اردوی تیم ملی امید تعطیل شد و کسی بازیکن نداد و سه ستاره‌ی پرسپولیس به دربی میرسن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 899 · <a href="https://t.me/SorkhTimes/139315" target="_blank">📅 20:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139314">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
احتمال زیاد پرسپولیس با ۲ مهاجم بازی میکنه و بیفوما هم وینگر چپ هس تا پرسپولیس تو حملات با توجه به ۳ دفاعه بودن استقلال کمبود نفرات نداشته باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/139314" target="_blank">📅 18:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139313">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
کامنت کریستیانو رونالدو برای مسی:«لئو، توی این روزهای سخت، یه بغل خیلی بزرگ برای تو و عزیزانت میفرستم. خیلی قوی باشین.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/139313" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139312">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SorkhTimes/139312" target="_blank">📅 18:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139311">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
✔️
جلالی مصدومیتش تموم شده و از دیروز به تمرینات گروهی اضافه شده
❌
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/139311" target="_blank">📅 15:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139310">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
تارتار نمی‌خواد ریسک کنه!
✅
به احتمال خیلی زیاد جلالی در دربی به میدان نمی‌ره و تیکدری مثل بازی‌های قبل در پست دفاع چپ پرسپولیس قرار خواهد گرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/139310" target="_blank">📅 15:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139309">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
فوری؛ هدایت ممبینی برکنار شد و با حکم مهدی تاج، حامد مومنی به عنوان سرپرست دبیرکلی منصوب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/139309" target="_blank">📅 15:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139308">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭕️
⭕️
⭕️
با اعلام یاسر همرنگ
🚨
کوپال ناظمی داور دربی شد
📺
موعود بنيادی فر داور var شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/139308" target="_blank">📅 15:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139307">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🤩
پیمان حدادی: وظیفه تلویزیون اینترنتی باشگاه، بازتاب صدای هواداران و پیگیری مطالبات آنهاست؛ رسانه‌ای که باید تریبون هواداران باشد و خواسته‌های آنان را به گوش مسئولان برساند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/139307" target="_blank">📅 15:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139306">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPCAfBRMtURk6T0V1Gh0zKH9ui50MpuXsypGgpt1suT3u3dOfK34ozlwbjd0oyXy36eswJp_1FisEI6D1eV-unAohMtplR_vhyDeDSMrI6XhZokB5_jYT0bfDJTY9cSa7F2KPdoOLjxk0flcBr3EEbuOldvgjVg5jaVod6WiU5-sST3gh5hWGieWFIPkiSRffwOihk_TUgZCZxwMr1zRI5pJXChuIO3OqquAvddIYoLIMgu0c4liJidbOKvvNO3nDC2qZZZiifFmv_-bUhjHHk_vZY31NG_ZrW8E8zpNyztW0liLJYhVSK0HkGiLfP-FyXV17QuiYCrHkpsqDAp6HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
ویلا پارک آماده یک شبِ آتشین
🔥
استون‌ویلا و آرسنال؛ جدال قدرت و جاه‌طلبی
اینجا هر اشتباه می‌تونه بهای سنگینی داشته باشه!
[
استون‌ویلا
🔴
🆚
🔴
آرسنال
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/139306" target="_blank">📅 14:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139305">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
حدادی قول داده فردا صبح پاداش پیروزی مقابل ملوان رو بریزه به حساب بازیکنا تا قبل دربی انرژی بگیرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139305" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139304">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
‼️
بلیت فروشی عصر امروز شروع میشه که ۲۹ هزار بلیت برای آقایان و ۶ هزار بلیت برای بانوان به صورت ۵۰ ۵۰ بین هوادارای دو تیم تقسیم میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139304" target="_blank">📅 10:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139303">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووووووری
🔄
🔄
با اعلام باشگاه استقلال بلیط فروشی دربی از ظهر امروز آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139303" target="_blank">📅 10:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139302">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
بلیط فروشی دیدار پرسپولیس و استقلال خوزستان شروع شد . از طریق لینک زیر میتونید برای خرید بلیط اقدام کنید   https://footballeticket.ir/buy-ticket.zul;jsessionid=23B55854CCBC6E89F276AA81C2DC01A1#  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139302" target="_blank">📅 10:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139301">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
ممبینی : به عنوان دبیر کل فدراسیون فوتبال تا الان نمی دانم چه کسی گفته است که تورنمنت سه جانبه برگزار شود/  هیچ کسی هم نمی گوید که من گفتم و اصلا نامه ای هم در این زمینه وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139301" target="_blank">📅 10:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139300">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5lICGObKy_ceA1EVpLjbCYxoGwQ7tzjlEdRXTFW66HFeWY1qCtW_Hf0Ih1CcL8nYRmnwG45HLYpx9rvXnhGObxtVGRU0iwWXn0A7VcfuUj2mfHVUGZ8e6yRdkSj9rbriahCjMGmMquKt2e0hEiiH2CbCYYxaPUwJspJubXSr_KtmSHz_emg16i6qGv6v_QMFLW5Qs5mIJ0__eqIYt-doDWAhw3nEEqIEyBDkKLt3XBEjtw2i9S5OSfE_1CxxMZ71LNUYhYBxqw9soT19SxQPrEMN80APbLnUJTJ3BisoRULAvNK73tEaFPmRixGYV14gt8qkhQW77wV6MmRzkqSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسپورت عراق؛ یحیی گل محمدی داره با سپاهان مذاکره می‌کنه، اون اصلا حواسش به تیمش دهوک نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139300" target="_blank">📅 10:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139299">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏅
هوادار همین سبکو میخواد آقا تارتار تیمی بدون ترس و سراسر هجومی تیمی که می‌تونست امشب خیلی راحت بالا 5 تا هم گل بزنه
⏺
خداشکر با روحیه بالا سراغ دربی رفتیم و امیدوارم تو دربی هم همینطور و همین سبک رو ارائه بدیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139299" target="_blank">📅 10:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139298">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
از هتل المپیک خبر رسیده است مهدی ترابی ستاره تراکتور به علت مصدومیت ادامه فصل را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139298" target="_blank">📅 10:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139297">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
چند دقیقه پیش تهران لرزید کیا حس کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139297" target="_blank">📅 08:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139296">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139296" target="_blank">📅 08:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139295">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ..
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139295" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139294">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCM7zyL1C8YiTfA-l2hAG-BXBlwU_EpVusgRLSHioxkb9OY6nxb_sMyf5HafqN8iyPM4TjvLNLJ15ghN4c4cayRn8HdtQgHlScjYh9C-EA6-xjF5nSXGIL9jra1t0Of41BbOclv2y3V8Nl5yeYksUp9VfFMMYD4N24bNMNvdBfuWPqI1O6xLlsCfKtpvUqGK9QUKcqWbIWXf1Y6u9Cx7TNnQzdxcXLIlmmFncYdbuxNhIvjH0hmxJYo5N6Hmvfc4v-0bVuYDVMqz9_xU_6eLC0jzCv3uuPRq1V08C44KqHDSK63xJLOFp0-N9a01MuT2m8ba2KCKkPUwtYPM8Csc_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک شروع شد!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
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
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139294" target="_blank">📅 02:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139293">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
سپاه پاسداران انقلاب اسلامی :
🔴
🔴
تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139293" target="_blank">📅 01:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139292">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
✅
قیمت دلار برای اولین بار در تاریخ به ۲۰۶ هزار تومان رسید  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139292" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139291">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139291" target="_blank">📅 01:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139289">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
درگیری ها بین ایران و آمریکا دوباره بالا گرفته و درصورت تشدید تنش، احتمال لغو دربی زیاده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139289" target="_blank">📅 01:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139288">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">💢
💢
💢
احتمالا دربی پایتخت لغو خواهد شد .
🟥
چون پرواز ها فعلا لغو شده
‼️
گفته میشه در صورت تداوم شلیک موشک ها از سمت آمریکا و ایران هفته پنجم لیگ برتر ایران به تعویق خواهد افتاد.این تعویق شامل دربی هم خواهد بود
⏺
همه چیز تا فردا شب مشخص میشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139288" target="_blank">📅 00:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139287">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">💢
💢
💢
احتمالا دربی پایتخت لغو خواهد شد .
🟥
چون پرواز ها فعلا لغو شده
‼️
گفته میشه در صورت تداوم شلیک موشک ها از سمت آمریکا و ایران هفته پنجم لیگ برتر ایران به تعویق خواهد افتاد.این تعویق شامل دربی هم خواهد بود
⏺
همه چیز تا فردا شب مشخص میشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139287" target="_blank">📅 00:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139286">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🎙
🎙
تمامی پرواز های کشور از جمله فرودگاه مهرآباد تا ساعت 6 صبح فردا لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139286" target="_blank">📅 00:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139285">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
فرودگاه مهراباد بعد درگیری ها تا اطلاع ثانوی و معنوی تعطیل شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139285" target="_blank">📅 00:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139284">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDRCPJ_PZSjhkkL9sOmSjHHgjsfu2OSv7FZistVJwT8hk1q6PbEgP1pLfbUP3FlXxvTivS8EdwtiOhYUZZRkGVSCeRVxITn4o_N5DwkXegduS1DtMLyykNiYjbeMSjVi48l4VHIV6YQ-eih4pykFhrHstOlvmClWKwxGLwyDwyKnDpDGuGlNoG_eD3uvaMpAGN2bUyolLm6PR1M8YGYm1dUWGL6KPdBzWFbFk1fb8JlVin_cAdmuJJ_qGlvz8IlcMMWGbjw9zgiOYYRanbmjwddKv_OxjQvqOsjzAh32JJRZ5vioL7a8FHN84EkCCLy6yqWs4s0fRH4aX1z_0I9phA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
فوری، با تصمیم تارتار و موافقت علیپور؛ محمدحسین کنعانی زادگان بعنوان پنالتی زن اول پرسپولیس در دربی انتخاب ش
د
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139284" target="_blank">📅 00:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139283">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egLLrCUTge8WzZGvu96LJYCBDlVAamCfYf27roxZR6zUrwSkhMBwcWBI6LUjqMDQfQscyxSiQ_1godw0NOmYojbjCGuCKjAaywS11UZ7Vx_To6sZGhnzPom1Fzo_AvUWRaafsm6Vju7z2_L_CmYdhDV5CzHc2HiI7OPDz34nOOXN4rpBXcMNWRUgxZnWQiW0pLUTvnWxjXY5cW7UXNP1sWa5XhOm2ASYNWyfAb4u-00SedMKINQ9FNHEHlAR-kgF1PAoHH6hoXTvmoFtGbfzeM_gu-dGDorqFOKy7x7spQbkvGWqgWyHPT8hKTuf0yaUPuXbOy0CKcNq_1ql5KIh9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139283" target="_blank">📅 00:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139282">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139282" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139281">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🟥
حاتمی: پرسپولیس در این فصل تیم خوبی است
❌
دربی‌ای که در ورزشگاه آزادی با نتیجه یک بر صفر پیروز شدیم در ذهن من مانده است چون اولین دربی من بود. ورزشگاه آزادی باید به این فصل می‌رسید اما این اتفاق رخ نداد. بازی‌های بزرگ باید در ورزشگاه آزادی برگزار شود. امیدوارم دربی خوبی داشته باشیم. پرسپولیس با مهدی تارتار عملکرد خوبی داشته است. همیشه هوادار پرسپولیس خواهم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139281" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139280">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚽
نورمحمدی: هت‌تریک ایمون زاید در ذهن من مانده است
‼️
دربی سه بر دو و هت‌تریک ایمون زاید در ذهن من مانده است/ هواداران دیگر مشکلی با حضور بازیکنان استقلال در باشگاه پرسپولیس ندارند/ زمان ما تغییر تیم سخت بود/ من پرسپولیسی بودم و استقلال را زیاد دوست نداشتم/ امیدوارم شاهد دربی خوبی باشیم/ پرسپولیس در این فصل یک‌تیم بسیار خوب و کامل دارد/ پرسپولیس در این فصل موفق می‌شود/ جذابیت دربی به ورزشگاه آزادی است/ اینکه دربی در اصفهان برگزار می‌شود عجیب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/139280" target="_blank">📅 00:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139279">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ
: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139279" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139278">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❤️
🤩
کنایه مدیرعامل باشگاه به برخی رسانه‌ها:
‼️
این سفری که به ترکیه داشتم و چند ساعت دیگر برمی‌گردم، از چند روز قبل برنامه‌ریزی شده بود. خداراشکر همان‌طور که ترکیب تیم‌مان لو نمی‌رود، دیگر سفرهایمان هم لو نمی‌رود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/139278" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139277">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c73b4d12.mp4?token=kw5mEt1pU-NmiuTNhgp0o8L8QnknTkLp8KPGYBHWrxUoFK5PsIY8wF7g-TedDejOio7rGOhilgMjwboVtxs3tkiRLZ3dyoiP6esoGd0mM2KUeleUhumS5gnDJTSVsbXweFbrv_3Zw_AVI5bbijqouZtrS8LbkugZJgZRZ7X3sudLUtvuqd1woWZazNf5RQgOYGIPPuD1swsDbHEXNPiEf3KsCCTb4VOvMqdz_FNgMhfj74ifB8v_MjoC-59AZvZa13Gu_sfQow3Ltw3HMGT_gIVtd2N_B69Dc5UaGMuKFkJmgB7_lM6JeoElX_MhCaduf-2fVo9IqBWUzZvAzEf1hbbDdG2A8zT8CKQjtLrei4czKhlP42g_QMgjJX3Kvdi-c2zA_-827cdTNb_ZrHDMw1z1AmqdVh7HplB3LHhE_pH1h948cGUWVC9fwxbgJ0hvN63efYRV_37RJ8sXkAaAL15OTK3pMv0sG09g-xdZwCfANNLXnXvwTtIH1mllfIMDFirzITN-lkFN-Br0dlSYlfiZuG0mqVkw13FfQp_PxwOEqs9Gb7NdhV1PjTVQ_a98BfLTuDy4oWT11JukvNVjJhoFrwYy3ipTN0Qd8FtfX0T0z1hpcIJKe3bepcuu2AoGnmINi2uhvbu1ajq6fIZ0w9LZ4LpsjO2P8grIom0_omg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c73b4d12.mp4?token=kw5mEt1pU-NmiuTNhgp0o8L8QnknTkLp8KPGYBHWrxUoFK5PsIY8wF7g-TedDejOio7rGOhilgMjwboVtxs3tkiRLZ3dyoiP6esoGd0mM2KUeleUhumS5gnDJTSVsbXweFbrv_3Zw_AVI5bbijqouZtrS8LbkugZJgZRZ7X3sudLUtvuqd1woWZazNf5RQgOYGIPPuD1swsDbHEXNPiEf3KsCCTb4VOvMqdz_FNgMhfj74ifB8v_MjoC-59AZvZa13Gu_sfQow3Ltw3HMGT_gIVtd2N_B69Dc5UaGMuKFkJmgB7_lM6JeoElX_MhCaduf-2fVo9IqBWUzZvAzEf1hbbDdG2A8zT8CKQjtLrei4czKhlP42g_QMgjJX3Kvdi-c2zA_-827cdTNb_ZrHDMw1z1AmqdVh7HplB3LHhE_pH1h948cGUWVC9fwxbgJ0hvN63efYRV_37RJ8sXkAaAL15OTK3pMv0sG09g-xdZwCfANNLXnXvwTtIH1mllfIMDFirzITN-lkFN-Br0dlSYlfiZuG0mqVkw13FfQp_PxwOEqs9Gb7NdhV1PjTVQ_a98BfLTuDy4oWT11JukvNVjJhoFrwYy3ipTN0Qd8FtfX0T0z1hpcIJKe3bepcuu2AoGnmINi2uhvbu1ajq6fIZ0w9LZ4LpsjO2P8grIom0_omg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
پیمان حدادی: وظیفه تلویزیون اینترنتی باشگاه، بازتاب صدای هواداران و پیگیری مطالبات آنهاست؛ رسانه‌ای که باید تریبون هواداران باشد و خواسته‌های آنان را به گوش مسئولان برساند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139277" target="_blank">📅 00:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139276">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDAA8hd8Xzux20eH9bgQeiI8s3bxEN0jTFdGaRXdUdlVOidHLroZeHqwic5fbG6o0a0aWPFhZa5tiqrVw3CaiAXakK3ZsbomZorb8VwiRuoyuGzbog3xWQ_8E_XI-GJN28uw4vY4WmE9mLj8EPEw5CXPqdLBj5zj67UzdxEo1sxG_KHMLhczgXELW69wBYQYCYNfytgb4YSLrm1Nh3Q5ze-Ki9zPJaYSB2MyGZV2ZX6RqssK8NOuyaUUaKWtSANBIiKdrEYjs7zZYLVCQ0hwEZ2IIvTkUs3Cf6NKNXFV9GMRiztxGMm0CVnLJehxrpAnjnTMFEV7ISORaQ55CGf4dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139276" target="_blank">📅 00:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139275">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3o9naZnLdmfBy5DaunG16OXWAjjfh9gYQtZd9jyidk3LKBkKHreB1wndPa9HcayJtKD_H0UyAIUgjIVHFZQ7nirNyVep2pEgexZu6G45hhCsBoDubnsEse_5KcPI1qASiZrFGxAK399tL_tpDZsjly3KUkipbbrZhXLsnvcULmtMOx6ZGksCrhX_JWnkEuOdnHhPgP51nVTd89LiRcMn167PhWRiT0BBed8cbo1Ogj84hRYMhJjOGP5DvDUJoA1csev7bhOsESrUz9pn6_DVe3IGRB6eM2ZkoSR4FIEXJvo9jmOB86MNk_LndCSvzpzOM6kdECY3aTevnvU0MkN6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| فارس:
🔴
❤️
🔄
تارتار امید چندانی به دنیل گرا ندارد و حتی درصورت بهبود مصدومیت هم نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139275" target="_blank">📅 00:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139273">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/324bfbe3b7.mp4?token=Yb6aG4IgVIBL6tCI7y5GKgzU6jLdmpfA5nnFNS2PnYaWi4zKw44O_AXzCTtzmwUyv2Yvx3TUYOVf74Txx_lWVqVafSvZr4ZOG3zfx5BykNk5mRWuy8D9dUAdSmjnULx3-7D7dANf1bYu7_IJtFkzrQ2YBp6KI0GezgckMtn-K1KVelznOMk5oZyE1_is3tPghAgOX1QJfvkbMhXjfJm3qm5ZV2SXMZAlpEjl612ybhmaLX7bgx02yrdOL4S2QrY2rs_zZ87NvQjcGhZXxAbJ8Nzj3VV8AL5ctKXNpICMJ6e3kpagKFQlET40k5XrYv-SvIY8xXZwwEg-1E4YNAtLXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/324bfbe3b7.mp4?token=Yb6aG4IgVIBL6tCI7y5GKgzU6jLdmpfA5nnFNS2PnYaWi4zKw44O_AXzCTtzmwUyv2Yvx3TUYOVf74Txx_lWVqVafSvZr4ZOG3zfx5BykNk5mRWuy8D9dUAdSmjnULx3-7D7dANf1bYu7_IJtFkzrQ2YBp6KI0GezgckMtn-K1KVelznOMk5oZyE1_is3tPghAgOX1QJfvkbMhXjfJm3qm5ZV2SXMZAlpEjl612ybhmaLX7bgx02yrdOL4S2QrY2rs_zZ87NvQjcGhZXxAbJ8Nzj3VV8AL5ctKXNpICMJ6e3kpagKFQlET40k5XrYv-SvIY8xXZwwEg-1E4YNAtLXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محمد تقوی، برنامه هت‌تریک در آنالیز فنی بازی پرسپولیس - ملوان گفت:
✔️
✔️
«حسین کنعانی‌زادگان در حال حاضر بهترین مدافع وسط ایران در بازی‌سازی است. از سوی دیگر، پرسپولیس با تعداد بسیار بالایی از بازیکنان در فاز حمله، به دروازه ملوان یورش می‌برد.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139273" target="_blank">📅 23:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139272">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2twve0jAISAlky1BWyyc4ODeZY3jy3zkLObz5l7wTn8zJQPW5CKowZfVk0hRQDLLOSj3KQ8xPwF8FH-g8IJuuQpzfBp1l74l6szHiTmC6-JOiCfMOkP6re-fSZEFuY0GyrYOXIMe2eDlmAZKrcTn3rSRg9EB66wotmHimlNsn4nSuIC_IT9tFj05YAj57xzkPWYt07OMFU67cLcxxgvDa40kmIPw5MqXsZspqC7ANiS4LTz7pNPZ2up-uHGt4X32BxU6_8zHCyVxXgNt6HjbIs9minB2643Ne9aMRDPRFi_sPifpNNN-CmQrCFoo3gvUWgxqWX6wO-tn3oMT5qQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
وحید هاشمیان: همه اعضای هیأت مدیره پرسپولیس به جز یک نفر موافق سرمربیگری من بودند که به گفته خود آقایان، این عضو هیأت مدیره در صورتجلسه نوشته بود که وحید هاشمیان ۵ بازی بیشتر نمی‌ماند و امضا کرده بود. سردار دورسون هم به من گفت شما تا هفته پنجم بیشتر نیستی!
‼️
👀
وقتی فصل را شروع کردیم، سقف بودجه داشتیم، اما تیم‌های رقیب شروع به هزینه‌های زیاد کردند و بازیکنان اسم و رسم‌دار گرفتند، در حالی که پرسپولیس نقل‌وانتقالاتش را زودتر شروع کرده بود. بازیکنانی که می‌خواستیم را به باشگاه معرفی کردیم که هیأت مدیره و آقای حدادی گفتند شهریار مغانلو گران است، آن یکی پول زیادی می‌خواهد و آن یکی هم گران است! ما هم گفتیم گران است اما وارد فازی شدیم که تیم رقیب ما بازیکنان گران گرفت. این اتفاق فشار زیادی را روی باشگاه و همچنین بانک و مدیریت آن ایجاد کرد که تماشاگران می‌گفتند شما چرا پول نمی‌دهید و بازیکن نمی‌گیرید. آن موقع دیگر دیر شده بود، بازیکن خوبی در مارکت نماند؛ بازیکنان مسن از قاره آفریقا مانده بودند که برخی از آنها هم مشکل زانو داشتند و آوردن آنها فقط بار تبلیغاتی داشت و مالی و فنی نمی‌توانست به ما کمک کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139272" target="_blank">📅 23:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139271">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚪️
⚪️
فوری / یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139271" target="_blank">📅 23:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139270">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⚪️
⚪️
فوری / یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139270" target="_blank">📅 23:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139269">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
ترامپ درباره ایران:
🔻
به نظرم این جنگ به‌زودی پایان خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139269" target="_blank">📅 23:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139268">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
اردوی تیم ملی امید تعطیل شد و کسی بازیکن نداد و سه ستاره‌ی پرسپولیس به دربی میرسن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139268" target="_blank">📅 23:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139267">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
✔️
✔️
طبق گفته رسانه‌ها؛ به احتمال زیاد داور دربی کوپال ناظمی خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139267" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139266">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139266" target="_blank">📅 21:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139265">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔄
🔄
یحیی گل محمدی در لیگ عراق :
🔴
3 بازی
❌️
0 برد
❌
3 مساوی
‼️
عملکرد یحیی مورد انتقاد شدید هواداران دهوک و کرد نشین عراق قرار گرفته زیرا که دهوک بیشترین هزینه را در فوتبال عراق انجام داده اما تا کنون بردی به دست نیاورده است
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139265" target="_blank">📅 21:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139264">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139264" target="_blank">📅 21:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139263">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
سه پرسپولیسی به اردوی تیم امید اضافه شدند
❌
❌
پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن تیم فوتبال پرسپولیس، به اردوی تیم ملی امید ایران اضافه شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139263" target="_blank">📅 21:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139262">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py6RSWFn5Nb82DkuYs578VaHV_06uhDsmgp5aXYgfxHkF94jpZ4cWhMdhqWCRDmvqrCkTOXGFYopCULpFQ2qgCowcEcfxnxZKculO-Wl9HFMoGQcCS_iDbPi75tvd6PglOw1yrtFl427v7DC7PIQdtUrI4JCAqK9zItADJnnKQSI427vRVvafJU2fExjalAbPCb-cjI-wtP2Bfi6bI8YiF3BOYDE824KmkEhah07dPc2K1g3MyFz6BXLr9D0pthY2FtwHltPezSqsh5pb1wm_5D8haBpUi9ObsFBLN3nb0GAXXkMzur22q5d8uuMtnN3DFp_8BTj__pjF8Cr-QJFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
منچستر دوباره در مسیر برد!
شیاطین سرخ مقابل ایپسویچ؛ یک نبرد برای سه امتیاز، اولدترافورد آماده یک شب پرهیجان
[
منچستریونایتد
⚽️
🆚
⚽️
ایپسویچ
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139262" target="_blank">📅 19:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139261">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👾
تیزهوشی و تلاش علیپور برای ثبت این گل کافی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139261" target="_blank">📅 18:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139260">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
نگاهی متفاوت به گل‌های اول‌ و دوم در برد دیشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139260" target="_blank">📅 18:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139259">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
🔴
دو گزینه اصلی قضاوت در دربی 107
💢
کوپال ناظمی و موعود بنیادی‌فر، دو گزینه نهایی کمیته داوران برای قضاوت در دربی تهران هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139259" target="_blank">📅 18:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139258">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eifeqlHDU7MptiXYBBUbKQ6czOCkARKSgk5BHflmzVWiifOHJqldF3JyTYTf4VaSlgdrWCndGPIXv8f0zieQw_AFK0jwY2h6yQAhtaqsQrMgb6lWVCpDoULG1CMbBYUUXowfea05z05Wb4wkWOaId2LerF_nBny9pjxX3tkSymSCT4MeRdkpFJIEKIG_m9yManULouWHxOMH_WK06-7P0n0t5MYDJYR2PF0b5zRJXNaSMmYB0q4bDcBnKRMUQ26xM7igHVSs8cRNAqg3uB0bwzzaSqIGJKD4JIN06MyXmEuR63kYg2GtVrIe_IwkQUkUJHimftdGpmmORTgbkIAljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئال مادرید آماده یک شب متفاوت!
⚽️
مالاگا میاد تا جلوی کهکشانی‌ها وایسه، نبردی برای شروع قدرتمند و یک برد شیرین!
[
رئال‌مادرید
⚽️
🆚
⚽️
مالاگا
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139258" target="_blank">📅 17:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139257">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
یک‌سایت خبری روزگذشته مدعی شده که مهدی‌ترابی در بازی با چادرملو دچار پارگی رباط صلیبی شده و فصل رو از دست داده! باید منتظر تایید یا تکذیب این خبر باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139257" target="_blank">📅 17:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139256">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
عبدی : من زارع هم میخواستم، پرسپولیس گفت نمیدم. هاشم‌نژاد هم میخواستم که شکمش رو عمل کرد. کوشکی هم جواب تلفنم رو نداد. حسین‌نژاد هم بعید میدونم که تیم خارجی به ما بازیکن بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139256" target="_blank">📅 16:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139255">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
با 5 بازیکن چگونه برویم تمرین کنیم/ می توانیم برویم گرگم به هوا بازی کنیم اما فوتبال نمی شود بازی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139255" target="_blank">📅 16:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139254">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
حسین عبدی: 23 بازیکن دعوت کردم فقط سهیل صحرایی، مسعود محبی، پوریا شهرآبادی، پوریا لطیفی فر و دانیال ایری آمده اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139254" target="_blank">📅 16:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139253">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
سه پرسپولیسی به اردوی تیم امید اضافه شدند
❌
❌
پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن تیم فوتبال پرسپولیس، به اردوی تیم ملی امید ایران اضافه شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139253" target="_blank">📅 16:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139252">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
فوری/ با اعلام مهدی تارتار باشگاه تا 22 شهریور بازیکنی به تیم ملی امید نخواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139252" target="_blank">📅 16:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139251">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
پرسپولیس با 9 گل زده تا هفته چهارم بهترین خط حمله لیگ داشته و امشب با ثبت امید گل 4 بالاترین امید گل رو 4 هفته ابتدایی ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139251" target="_blank">📅 15:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139250">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139250" target="_blank">📅 15:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139249">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139249" target="_blank">📅 15:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
تیکدری دفاع چپ پرسپولیس در دربی/خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139248" target="_blank">📅 13:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139247" target="_blank">📅 13:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">☑️
پرسپولیس برای دربی اردو زد!
🔻
با تصمیم کادرفنی پرسپولیس، اعضای این تیم بلافاصله پس از پیروزی برابر ملوان، راهی اردو در هتل المپیک شدند تا برای دربی ۱۰۷ آماده شوند؛ تارتار بعد از کسب این سه امتیاز به تیمش استراحت نداد و باتوجه به فشردگی رقابت‌های این فصل،…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139246" target="_blank">📅 13:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚽
👤
🎙
ابوالفضل جلالی:‌
🔻
حضورم در دربی؟!هنوز هیچ چیز مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139245" target="_blank">📅 13:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGDB--LfJ0WTBj7AaFKgE5tQCQGK_d20qcEap7GCpesSkQ3zA69MC0k5XrLtThnQi1V1vX_1K0X8jLuSi5E_FCVWLk0MjrK35fYBXMl4iO6dABNxvJablEiVTKVAgmqxVnqw3CyV13vFs_tSNzJbN2sDYzgHO9DpmBhR0xsAxcyWF_vNMuSPEuG-oDnUzTAqQ_X-PMHQeKV4IYRjqwK5APY1X4SRa6RCq_e2uPeiKSRvsgysRnw9f2pyGoTCn2wHg6CGOO6Z-O39ct9b8ZNoGOiW87V_yCGFiAImvKhJoEEYvXq6kn0DzXMIjiyhtm8rWq_2y5nj1UX_bk1ij8f9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی علیپور با نمره 8.45 بهترین بازیکن بازی پرسپولیس و ملوان شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/139244" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🗣
🗣
با تلاش کادر پزشکی تراکتور؛ مهدی ترابی به دیدار با پرسپولیس رسید و از روی نیمکت بازی را آغاز خواهد کرد. هاشم‌نژاد غایب است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/139243" target="_blank">📅 11:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrD7g1-ly1cz9xG8QctbL68jxsgIscpvvSpKxy37KurPKdvk93juDi77bS_wyAE1T3bUJ9eIBc16NENW_vNIVLfFhE6ZlTdQpctLLkiyXZsZNNlmjlP5HQ2rWMEfRQOTEoEOgKNPfqdNw1aRYmqt8wLjtzBbZjDBnITDWFAa41qSo0qRnkhY97oqYc9Ix5_k48BSh0qVLYmNYypYgX-Ta3hf_s0HsxYvQKVFkWvB2nVf5UPnegGc3XMziD48lXdYhPXRPAvwTwsYV_r8MQuDHzl43HVDLyG-fOsC3hpLBt-FcgLmjfv-T-32IIRrQ4Eq3wKRY8zLVtldUdEvLfMQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در آستانه ۱۰۰ تایی شدن ؛ علی علیپور به رکورد علی پروین در پرسـپولیس رسید و به دومین گلزن تاریخ پرسپولیس تبدیل شد
✔️
✔️
علی علیپور با گل‌زنی در مقابل ملوان، در کنار علی پروین با ۹۵ گل زده به دومین گلزن برتر تاریخ این باشگاه پس از فرشاد پیوس ۱۵۳ گله تبدیل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139242" target="_blank">📅 10:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
✔️
‌ تیکی‌تاکای تارتار؛ ۱۸ پاس و گُلی که نشد
❌
پرسپولیس با ۱۸ پاس متوالی روی زمین یکی از زیباترین حملاتش را ساخت و تا آستانه یک گل تماشایی پیش رفت، اما ضربه سر ایگور سرگیف از بالای دروازه بیرون رفت؛ با ورود اورونوف، سمت چپ سرخ‌ها هم فعال‌تر شد و ترکیب‌های…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139241" target="_blank">📅 10:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTv2rBnikuwchYXgfrOE4qjNhG3TSCZwLHT9l6fDewJns9KRv3A4ipRY-XhLbHR3c3wRKM6E5EKGtrfsSnQMJXqyQFkcHe2iyqAXV_XHXiI4rbaglY8WAyW4adCNqWTqbMciILdIc0U4NY-NpUvwjtbdUu1MIaltkBOBTpuWq5UgbHAVsMOAftITM54iIHEQgFh50i3cDT_zG5u-7MP36C88IN6DNxRGQNVBS38CEP3Al-K60GzUjExJDYKyPZREX5BdMgLUfVIP-ZO-TcGZwHyxJYhWXhDMk0PUV1JyL4nHwe-mx7bga66NP9PHbtxOYbtoTbL9_UiZhKw9dtJ14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139240" target="_blank">📅 10:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
اردوی پرسپولیس برای دربی بعد از بازی با ملوان آغاز شد و بازیکنا به هتل المپیک رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139239" target="_blank">📅 10:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139238" target="_blank">📅 09:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139237">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
‌ تیکی‌تاکای تارتار؛ ۱۸ پاس و گُلی که نشد
❌
پرسپولیس با ۱۸ پاس متوالی روی زمین یکی از زیباترین حملاتش را ساخت و تا آستانه یک گل تماشایی پیش رفت، اما ضربه سر ایگور سرگیف از بالای دروازه بیرون رفت؛ با ورود اورونوف، سمت چپ سرخ‌ها هم فعال‌تر شد و ترکیب‌های…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139237" target="_blank">📅 09:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139236">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
پرسپولیس با 9 گل زده تا هفته چهارم بهترین خط حمله لیگ داشته و امشب با ثبت امید گل 4 بالاترین امید گل رو 4 هفته ابتدایی ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139236" target="_blank">📅 09:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
صبحی که تیم محبوبمون توی ی بازی جذاب و دیدنی بازی و برده بخیر.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139235" target="_blank">📅 08:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGRoXWEgvxmzPlnv2ZOnTFxKZjwHtzLn2cPqgaCd9HleTFrRFr_lVQ2zoH2M57lgQdnEfOTPLkNzKdOo3lWIxYZ9O4VOLv51Ofw2MF-AKK5BCDFmlv7K6AGfjp16l2JB-nMPDxH4m1UdMi1_Qfj9blrdG6lXVuDMCmNIymvBCIUShJ_ZvE7p3AI-OlQBBw7OSVkqQn0kvFKgB7KGCYb9Io9ruIWlr8nWsh7z3JvdjOJGlRRKjgKZzmJRierO7OE24KBPvQZCAOxoydk3sPtZyrFqkHU-BT9YcOwBRxb_mUsg7WlsfwsqFGH5zRb1lp6f0yoJnH2JVZrOvPKaS0tteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/139234" target="_blank">📅 01:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
🔴
جدول رده‌بندی لیگ برتر پس از پایان هفته چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/139233" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
مهدی تیکدری: بعد بازی قبل همقسم شدیم که این بازی رو ببریم/بزرگترای تیم خیلی بهمون کمک کردن/روی یه اتفاق به تراکتور باختیم/هجمه‌ها بعد از باخت طبیعیه/ترافیک در خط حمله زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/139232" target="_blank">📅 00:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
دانیال ایری امشب به عنوان بازیکن ذخیره وارد زمین خواهد شد تا اتفاقات دیدار با تراکتور را فراموش کند.
✍️
ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/139231" target="_blank">📅 00:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139230">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
حسین کنعانی ، دانیال ایری ، مجید عیدی ، پویا پورعلی و محمد عمری پنج بازیکن تیم پرسپولیس که سابقه پوشیدن پیراهن تیم ملوان دارن
✔️
فرزین معامله‌گری هم که برای سربازی منتقل شده به ملوان تنها بازیکنی که سابقه پوشیدن لباس پرسپولیس داره
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/139230" target="_blank">📅 00:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/139229" target="_blank">📅 00:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZM9gc_ni7GR_-QLfUSXhjqsp00TpwPU0PJCtGo0WBGr1dJZDsxzFr9Pc3nmP_H01NAV6En8_jWQzyU5uKlyNSCYRC6a4_yDfZCKgobUM-WsbJRRwwlfCPnmuxVBhly7NH0Nb4tpB7D_VVNDfKkV-VCz-fDXSKhb976CIE3azixGVWbZIenN8URS90pXmqeYt1GMNkq6uvJchvyLw72jgu-047zg5kOvTYrzLFCVKPnfCj6cgkTjH4lnjx73vEq-Z0mVLzJocf_6rJ5kDNFUnzyrZjld4G4klxHS9b61krc0hPsJvMSrS5DH0E8e74t6IZWUzkyKgDlMVBQkTkNuLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/139228" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
مهدی تیکدری: بعد بازی قبل همقسم شدیم که این بازی رو ببریم/بزرگترای تیم خیلی بهمون کمک کردن/روی یه اتفاق به تراکتور باختیم/هجمه‌ها بعد از باخت طبیعیه/ترافیک در خط حمله زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139227" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
کریم باقری: پرسپولیس از هر بازیکنی بزرگتره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139226" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
کریم باقری: نگران نباشید. پرسپولیس بهتر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139225" target="_blank">📅 00:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139224" target="_blank">📅 00:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139223">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
آمار برگ ریزان بازی
🔴
۱۶ شوت
🔴
۶ شوت در چارچوب
🔴
امید گل ۴
🔴
گل ۳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139223" target="_blank">📅 23:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139222">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
🔴
علیپور با ۲۵۷ بازی، از سید جلال حسینی با ۲۵۶ بازی عبور کرد و به رتبه دوم بیشترین تعداد دیدار رسمی با پیراهن پرسپولیس رسید.
🔴
علیپور در ۲۵۷ بازی خود با پیراهن پرسپولیس، ۹۰ گل زده و ۳۸ پاس گل ارسال کرده است. او با ۹۰ گل و پس از پیوس و پروین، سومین گلزن برتر…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139222" target="_blank">📅 23:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139221">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
خلیلی: امروز فقط بهای جوانگرایی را دادیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/139221" target="_blank">📅 23:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKmTsteAL28nbydlYckPFJTuLfqRJ4L3F2OLLW3cmw2ktIgwzvdSZlqRYZtNXFbj9DgTlJVk0XFVAgtYpOo5nswdXglrBDOLvG8b4W8JKX1kTfyGh2FmfQVS7pAlEuLs0sewVxlsXQrmtVWJywSIwVjFflksQWOvzrQKQ-ERL7MXr14i0V3T5vzXnOj3qhCh1k4xAsYkXu9iYIWCp5HudFLB2-rUsM1KpLEokaWHf9bBaomZGhA-eKez-o5GGAhcUuBAyv3I-l3206TeKS6WWqQunQhZQ8Z5FJfty6ExCuL_jH1VukAelByz5Z4YSXWfzbWVbAfp9payQicl3Jd43Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
ستاره این روز های پرسپولیس تارتار
📊
عملکرد بیفوما تو این فصل
🔄
4 بازی 1 گل 1 پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/139220" target="_blank">📅 22:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
براساس‌صحبت‌های‌مهدی‌تارتار؛ سرگیف از بازی فردا مقابل ملوان به ترکیب سرخ‌ها برمیگرده و تارتار میخواد زوج علیپور - سرگیف استفاده کنه اما اوستون اورونوف همچنان نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139219" target="_blank">📅 22:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139218">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/139218" target="_blank">📅 22:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/139217" target="_blank">📅 22:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139216">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
کریم باقری:
🔹
به زارع دوست عزیزم تبریک می‌گویم؛تیم خوبی دارد و ضد فوتبال بازی نکردند.
🔻
خداراشکر برنده شدیم و توانستیم با روحیه خوب به پیشواز دربی برویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139216" target="_blank">📅 22:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139215">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
کریم باقری:
🔹
به زارع دوست عزیزم تبریک می‌گویم؛تیم خوبی دارد و ضد فوتبال بازی نکردند.
🔻
خداراشکر برنده شدیم و توانستیم با روحیه خوب به پیشواز دربی برویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139215" target="_blank">📅 22:28 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
