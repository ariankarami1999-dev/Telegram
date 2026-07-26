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
<img src="https://cdn4.telesco.pe/file/TKgGLUZ5cWweTx26MqzBJ81CHUO2j9dQk0lC9-sFCbOP1k8nBeOeJFKvKZdTw-UjaCnIj094281BbthINKuuGzxXsPe0kixKPBzcUBZgF0IY0B0gnLe9EYOscWjiPQieqy6V3GdxibxZn8cmPWe5TDEUF6_-cjWTzsOETdfYDyepAPXzBSzgMhn-hK09ubK0z6l35D8fnD4mbcyvyE2v7Q2vvHe8kVixFoDxZjb03MWcLSOC0FNHgNmrjIiymEnSL1yA32oGt8xa25tHOTNBOYly-yysBVdzfzkCC0qGdR_WIJAzqDjU6hi9aL4YotaFpbjAadY-aXK7BZaCNfI-Mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 11:00:43</div>
<hr>

<div class="tg-post" id="msg-136713">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
✅
اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/SorkhTimes/136713" target="_blank">📅 10:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136712">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه پرسپولیس قصد داره‌ تا ۲۴ ساعت آینده از چهار خرید جدید خودش رونمایی کنه ///فرهیختگان
🤝
محمدرضا اخباری
🤝
دانیال ایری
🤝
کسری طاهری
🤝
پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/136712" target="_blank">📅 08:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136711">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
❗️
دیشب و بامداد امروز هم حملاتی به کشور عزیزمون نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/136711" target="_blank">📅 08:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136710">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم در واکنش به صحبتهای قلعه نوعی که گفته از خودگذشتگی کردم اومدم تیم ملی تیتر زده که آقای قلعه نوعی میتونه دیگه ایثار نکنه و از تیم ملی بره و برگرده لیگ برتر همونجایی که تو ۱۰ سال گذشته هیچ افتخاری کسب نکرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/136710" target="_blank">📅 08:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136709">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
بعد از 13 شب .دیشب و بامداد امروز هیچ حمله ای به ایران و نقاط ایران از جمله جنوب نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/136709" target="_blank">📅 08:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136708">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPvllPzfXrXUkstu42sQmutSrlhUuLkyMvQCAgVSADE6EfyHwKLC2EoP9wyI0beoycGLIoxdP7iopwbSt4bujirsdKoKN0YOQ2QLU6dtOpTBcXocfnacj9z5_e6x1bC7ncXASJrYrLAurGF_CH0rLYgUe0BrTrhnB_hCaiACmdDIJRnbuh5_gF7W1XSTry4qd4NcZcvQjcD040orFdSug7BEwuiiaV43V4ZZ6tz1Q61UB09vRT9I6dLKyNFrHWditiEE9Gfru8a8TSGh_iP137WbpHrjV1OEwRlCJLApROHQOua3jxiRTZijwyc2TDu8_X3ZuxQ9gGnWBO409aTV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SorkhTimes/136708" target="_blank">📅 08:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136707">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درآمد ثابت واقعی میخوای بسم الله
👍
سایت های شرطبندی دنبال ادمین این کانالن ، داره ورشکستشون میکنه
.
😂
👇
JOIN JOIN JOIN
JOIN JOIN JOIN
فقط یک هفته جوین باش میفهمی پول درآوردن چقدر راحته
😍
🤝</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/136707" target="_blank">📅 01:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136706">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qD5X9J7ewO8AuTl5pulxwaX6TEeLChYNLxaz5lTFvKa9QzALhatJZkpm7oGFHJpSrOjZlIm7yv1MM1bS6f6sbY1qSWlgNR4ri9sbjCfe92QJJisKDxBx_Et5IuF5GBK8o5uRIY0dFtNM7JHx_IsqCDORoebiwovo9umZHXDmyxedUUxRxft0Q6qOv3f6yf4ObSyNH3MOPqiVpp3-QLJryyCfz65-9ppxckLQDtrcTfjgSGIbKHOvT_GsBzcFDPymhKJGxGzSejPR7jY4-j3vzwf3USxAFiVUJBlw11rT45FcHhVRXZy-F8bk6nzl99hfQzO3m5wcyQ3YZ-MlYBk1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
رفقای بت باز و اونایی که اهل پیش بینی فوتبال هستن از همگی دعوت میکنم این متن رو بخونید
...
🤖
با ربات
هوش مصنوعی
پیش بینی فوتبال ماهانه 30 الی 40 میلیون تومان به جیب بزنید،
کاملا واقعی
🔥
📣
رفقا این ربات طبق آمار و ارقام تیم ها و الگوریتم افت ضریب خیلی راحت بازی های مشکوک به تبانی و فیکس رو پیدا می‌کنه فوق‌العاده پشم ریزونه.
😄
👑
t.me/+bReDKwrhVk5lMmM0
👑
t.me/+bReDKwrhVk5lMmM0</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/136706" target="_blank">📅 01:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136705">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
محمدرضا اخباری در حال حاضر دبی حضور داره و امروز با دریافت برگه مجوز خروج راهی ترکیه میشه. طبق شنیده ها قراره اخباری امروز به صورت رسمی معرفی بشه ///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/136705" target="_blank">📅 01:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136704">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎥
⚽️
ویدیو باشگاه از تمرین تیم با کپشن:
😀
از ضربه‌های تمام‌کننده تا واکنش‌های تماشایی؛روزهای پرانرژی پرسپولیس در ارزروم
❌
پ.ن حال پرسپولیس خیلی خوبه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/136704" target="_blank">📅 01:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136703">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
✅
ورزش‌سه: اورونوف، تیکدری، عمری و محمودی اماده‌ترین بازیکنای تمرین دیروز پرسپولیس بودن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/136703" target="_blank">📅 01:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136702">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
فارس: حمید مطهری گفته هیچ جوره نزارید رزاق پور بره پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/136702" target="_blank">📅 01:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136701">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🏅
🏅
به گزارش رسانه «سرخ تایمز» باشگاه خیبر خرم آباد طی نامه ای خواهان جذب تیوی بیفوما شده است،اما دو باشگاه تاکنون به توافق نرسیدند.
⭕
🤩
خیبر اعلام کرده از قرارداد ۸۵۰ هزار دلاری بیفوما ۲۵۰ هزار دلارش رو پرداخت میکنه و ۶۰۰ هزار دلار حقوق باقی ماندش رو پرسپولیس پرداخت بکنه اما حدادی به عبدی گفته ما نهایتا ۴۰۰ هزار دلار از حقوق بیفوما رو پرداخت میکنیم، درنهایت اگر اختلاف ۲۰۰ هزار دلاری بین دو باشگاه حل بشه تیوی بیفوما به خیبر خواهد پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136701" target="_blank">📅 00:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136699">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
تکمیلی :قدوسی : تارتار گفته بیفوما و گرا برن و سرگیف بمونه اما خلیلی میخواد سرگیف ملی پوش رو رد کنه تا گرا و بیفوما بمونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136699" target="_blank">📅 23:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136698">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">💥
💥
با جذب محبی و لطیفی‌فر سهمیه‌ی لیگ برتری پرسپولیس تموم میشه ولی قراره یه سهمیه بزرگسال و دو سهمیه زیر ۲۳ سال اضافه کنن تا ایری و طاهری و رزاق‌پور رو هم بتونیم جذب کنیم/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136698" target="_blank">📅 23:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136697">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
از تمرین امروز
👀
💪🏻
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136697" target="_blank">📅 23:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136696">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHwilIzyneV1TlYHfY7a-4iKg2IRj42uyqMtH5qY0Wq8wd7DYR1hAoiKBdoqG0R-UPEnYCDNf7Sw98w0XwqI8N1JL2XkhQgkwIAz_0En-dFaWVzUeMCMAU2V4XSlZJcMeYanGtahvswoch76_08aAkPnjp0r7Tf_GILEC8A_P8W5OpezAFjsWNDDMCZOfSw5yM8kxtod4prBXVB03k66ksPRSeTe9qzLi-eQBrixBxcP6Pcu6jcIb4-C9EDCk5tc07tQHwpC4lcrO8bTJHsv6xF2Qvtb3xfig3lRXm7OKO4Kx_s7PDqkhhidgH_lcrYeAxVExTd3Q_bFhGbxyPCaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
از تمرین امروز
👀
💪🏻
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136696" target="_blank">📅 23:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136695">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⬅️
⬅️
⬅️
وای‌نت: اسرائیل خود را برای حمله گسترده آمریکا به ایران در فاصله شب جمعه تا بامداد شنبه آماده کرده بود، اما دونالد ترامپ برای دادن فرصت بیشتر به مذاکرات، این اقدام را به تعویق انداخت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136695" target="_blank">📅 23:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136694">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136694" target="_blank">📅 22:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136693">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
فرزین معامله گری از پرسپولیس جدا شد و در اردوی ترکیه حضور ندارد و شماره بیست پیراهنش هم امسال تو تنه عیدی هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136693" target="_blank">📅 22:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136692">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
معامله گری که سرباز شده و برای دفاع چپ فقط ی جلالی و داریم و خلاص که اونم مصدوم شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/136692" target="_blank">📅 22:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136691">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHMhvlyUzOgDJKCi0r2R_T5xLV6ycqb0OrCAzO5InxtXqX12CmJh3BUWMUiBZZX1M5jIa-peyYLi5XT9arBp18Xc1A9CFppJ01AD9zbQXGl4M3pn-umLmslvL9MqhCMaeqgWGab9BknDOeiITfCajfgCd6Z0AskEBcjxbVWytNaz26KvfzfiocMhVXwBs-NxOmDAV3O-rV5hxPQVn1EImfuCQt7ZR15YpL2Cby7xF5MQ8NQ2_pG4NQj3K8GPVNHs7whJ9Ud_SjBJx8tR9sz_iNuLYXNspQFRrx9GCYBAgJgqkn-LCDVy-Rrc4KZsn3Rim_-oxpX1N_JvIPM01IiYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136691" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136690">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
ایگور سرگیف توی تمرینات پیش‌فصل بی‌نظیر بوده و تا الان انتخاب تارتاره برای نوک خط حمله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136690" target="_blank">📅 21:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136689">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0a656a22.mp4?token=GFC9a-tKnem8zAAAHgxaSrZhONHAcLP5zWSE-5HSJanP7NsUopBW7zJHIYTQOZpmbM1DqVSgYCxcGM40l8mtHRHQJZ-Xw2rmQd7ASi3ifXHI21zEVEQq7NM_ohtS4mITuQkriygN5xtPaq63SteXX-24QglcAXa5PCW7XrtW0DtUNc0kNfqLBapQPRwAsspc2K7e84FUD4CkzpgbFnpa1t9VWNa_qXjuy8VYNga3hQAM2jJzcBkdJ_SPvOExaqaXthoYJqKnI4PuhI4o_Z4JuMXAzzVuJ82Dogzb5ewpFe9hLWVzpm5jUzt55pUM9rH6VpywZFNbi3sk4Y3GU67sgaBb513wkN-gUEOxFkZJYHTEk42zN3DmIhrpUWsrW93fu9rAUA97uvL4xT77UTyZHII_YGNKJKlkPYrDcWmN8ZxxoM06vZTRDZ3I2NLy0-GT0e97NRMXWRZxoQv6AEY1ERifoWNtvVhhjHG0wKRcnE7ElaSZ2zoD8zQSSqmxENJpf_BbmaHSPtASIUzHTLsHQ6n4mS-f5SK9DcnqT0Tz1TZy_EW6YxYAuHQr8ljEOhH6FJzwBcwU5sOT6GdZTKkdVszCSNjWGg96TMBANsaIh_7joOmaeA5mGiZXHHLX7yhaDmOkBPWsL8B0p8hAN0QGM_s7MOSp0Zi5dd-OqOOSCKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0a656a22.mp4?token=GFC9a-tKnem8zAAAHgxaSrZhONHAcLP5zWSE-5HSJanP7NsUopBW7zJHIYTQOZpmbM1DqVSgYCxcGM40l8mtHRHQJZ-Xw2rmQd7ASi3ifXHI21zEVEQq7NM_ohtS4mITuQkriygN5xtPaq63SteXX-24QglcAXa5PCW7XrtW0DtUNc0kNfqLBapQPRwAsspc2K7e84FUD4CkzpgbFnpa1t9VWNa_qXjuy8VYNga3hQAM2jJzcBkdJ_SPvOExaqaXthoYJqKnI4PuhI4o_Z4JuMXAzzVuJ82Dogzb5ewpFe9hLWVzpm5jUzt55pUM9rH6VpywZFNbi3sk4Y3GU67sgaBb513wkN-gUEOxFkZJYHTEk42zN3DmIhrpUWsrW93fu9rAUA97uvL4xT77UTyZHII_YGNKJKlkPYrDcWmN8ZxxoM06vZTRDZ3I2NLy0-GT0e97NRMXWRZxoQv6AEY1ERifoWNtvVhhjHG0wKRcnE7ElaSZ2zoD8zQSSqmxENJpf_BbmaHSPtASIUzHTLsHQ6n4mS-f5SK9DcnqT0Tz1TZy_EW6YxYAuHQr8ljEOhH6FJzwBcwU5sOT6GdZTKkdVszCSNjWGg96TMBANsaIh_7joOmaeA5mGiZXHHLX7yhaDmOkBPWsL8B0p8hAN0QGM_s7MOSp0Zi5dd-OqOOSCKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
⚽️
ویدیو باشگاه از تمرین تیم با کپشن:
😀
از ضربه‌های تمام‌کننده تا واکنش‌های تماشایی؛روزهای پرانرژی پرسپولیس در ارزروم
❌
پ.ن حال پرسپولیس خیلی خوبه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136689" target="_blank">📅 21:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136688">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
✅
ترامپ قرار بود عملیات گسترده‌ای که راجع بهش صحبت میکرد رو امروز صبح علیه ایران انجام بده ولی لحظه‌ی آخر عملیات رو متوقف کرده تا به ایران یه فرصت مذاکره‌ی دیگه بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136688" target="_blank">📅 21:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136687">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136687" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136686">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
با اعلام باشگاه پرسپولیس، قرارداد محمدامین کاظمیان با توافق دو طرف فسخ شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136686" target="_blank">📅 21:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136685">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136685" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136685" target="_blank">📅 21:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136684">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8WpJA9BWE0rXLFspRZYM_vgmg3RKiB6H4siMrvEllNbqjJXa87QyGXvtFbB-54lPwikVAwx8jbOk92vDqwoEzlbXDabMSBkxHsFQRlhTC0SVAow7xNe42QuwlC_uQWRvZENe4mBAW6lvgyoGnRfEtd_JyKo29Tn6Ph-OnK9W_fl6KDadtr7U-zI1eyCdidtL6d-S3GnKO7ReKz99LejHg1NaY-zxXeuBk8wri8HYU3nNg8YyX8C266y2-o2WSrLMePKjGZspr5g5yyzDL3GfiDu2Zbv5jPyhHAeVA8Orjul6Y246zdsu5BUuFmGo4S-YFGwbJ6qFW6PbL0nAk6PmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هر
چهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
Ⓜ️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/136684" target="_blank">📅 21:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136683">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/136683" target="_blank">📅 21:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136682">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCNcOxDWM-esT-Y-pI-kcR-xMgyXf3bDTpLlHKrdsk_hA37W4qdY0GDGP-IYa7zY_22QaFrtvaMkBPO4fv6NccMxHTxCtbaWykxK5Pn0Tf_3-W2P32WMnkZCokINBIFfU6jLJozGwx1eFlc4LrDleowaSVx3-nQZOW7CXu6biTA6iPGW3K11b_VzyUTRnpbdzUR2SX5LVYs5Gqrftm2eC_wdmxKKL9fZzRFMLOa7L1PEIBF8xVUP93Jl6SD7bnCxPTLG33GkbGkfMJIlPIMgzcBtWSjArdhsdh3q7sjMIDFBch3kbMMCzQwHSgfiZ66ZVuqlj3H6nGTADui47dILTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام باشگاه پرسپولیس، قرارداد محمدامین کاظمیان با توافق دو طرف فسخ
شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136682" target="_blank">📅 21:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136681">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2wHUTtkdr8D1luKVelgggfl0sb0ewXHUE7yzHn_xrntR1Hi4MTYXAxn2Bq9j5_3t_rYWIwuOYJhtKJXxUR_hCeu-Uqsfmu4EtZ79IH46zv_59lZP8JHym_9fkq21lKpNEw6XRS8cJyQEgIF7GGCwdukyRJbjxGinGp9jfUiec8Br2lVM0_ra9vPnZeiqYuf7MxbIOJQkGvePad0_zaoNwtecxAU0n3XckFmDNzQGrsl6W8qXIsRXO9QOwK2GSwyQNaCSGVUzMGonPSEjdhDFh_V5nJNNF7JZWUuUm9YyJKMAzRxZyhCZ1b7m1sLhNLQW8Gz3eD3njl6GRAHrpzYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پوریا لطیفی‌فر با چه آماری به پرسپولیس پیوست؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136681" target="_blank">📅 21:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136680">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6dpjys_lp8rqKBS-KoH7i9gQA-3uj-QOEqOFO94dZpwZzOcZDo_UgynlsYT_AvcecMVgqnshDSvxtofcXiPIEOdvXafF7csVeGB_pHvzuvOZxMOnKERD1cSXzZQJK2deMhT2MRWDPGNkUQ7ilIUpL1U_H52aC1E2sdUxjZwSDcSc53S0MXFjbs70nR2M20OgrIEnP9Vke7KrLXpDaT1hZO3oDFYoboLx8UYwg0bVT_pv4SMW3jbzRrCso3VXNHhu4KTQBMt_SXIVP0ao9B99g0AKmB_oOKq8LYtGvZP6c32DGdyK8KRTcbjzXLsgAH1PICu0uwOG0xMXo8v6u6G2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136680" target="_blank">📅 21:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136679">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRLaTkN63T8_stdSr7Z--wleNRiJlQD5zbmtETyMJo7wr8QvHBOp9iq0urNO1A-HdHyhAemD5I5oa2Hyt5a1cUw9_VLAi5TdaqJYfESYrfhqWuq-tjWTo8RwtV3qaLQ49QLV2zmFPxTKD-XRsQ4-HGgZ5ML3Fffk76b_2tQVcR9tTQmBTghCQy3v1bsUZIivQxLwXP_rwah7pWULO2VIE09SCO-t3kRckIfh0_RZF8Yn2amQT2vc4s26C_8Wh2DPlgSuZFa56yaEDxEcb11TZSdNWAdgFHrKBn-YXHjCEDJO0dJh_FTtMjls5cBBSZRC9INRoWt4HKJqwFtQWPoDZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136679" target="_blank">📅 21:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136678">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
🔴
فوری
🔴
محمدامین کاظمیان از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136678" target="_blank">📅 20:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136677">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
❗️
با جذب دو بازیکن؛  سهمیه لیگ برتری پرسپولیس پر می‌شود!
🔴
🔴
پرسپولیس  زارع، جلالی، عیدی،  پورعلی،شهرآبادی  و  تیکدری را به خدمت گرفته و در حال نهایی کردن انتقال محمدمهدی محبی و لطیفی‌فر است.
🔴
🔴
در بین خریدها شهرآبادی چون فصل گذشته سهمیه زیر ۲۱ سال گل گهر…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136677" target="_blank">📅 20:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
شایعه: قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136676" target="_blank">📅 20:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136675">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
فوری/ ترامپ: مهمات برای یک حمله بزرگ به ایران آماده شده. سران ایران که خطرناک‌ترین آدم های جهان هستن باید تصمیم‌گیری کنن. شاید تسلیم بشن، شاید هم بزن تو غار قایم بشن. چون تو ایران غارهای بزرگی هست! ایران شروع کرد کل خاورمیانه رو زد. اگه بمب هسته‌ای داشت،…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136675" target="_blank">📅 19:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136674">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
۳ خرید ناب در راه پرسپولیس
💥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136674" target="_blank">📅 19:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV4EUGQK6p6R79J2JsRamZUHZBre0Tl9vPOoq0kHulPBMuJR9kmhVY-NtoqSLdBzY0AQ28tI-CILkzp4ufv9h7TVkKwqDKcMCYlXG6BVgAfNnXc-vPnoQTIbutKtmtPvCjOG-JFSPnOcfGqRuzguaRTx0s7MMkYmcyM1S3g8XNjauFdcMQ3Gav0LA5fhBMBd51_JfuYoA8AdlP58_Wf0pwoLzQi3K8yyz0cMaP7Hx0kSZhfHj9DNvTiyMZtGskQqhU0nKpxi8CLVCthzwzNpx6L_7HRBYAf7kOShLsaFhXwLyzEjKImn_4VUz1XIA3j6spAmf67yvkQ1_YLBVcsP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ایگور سرگیف توی تمرینات پیش‌فصل بی‌نظیر بوده و تا الان انتخاب تارتاره برای نوک خط حمله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136673" target="_blank">📅 19:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">💥
💥
شماره جدید بازیکنان پرسپولیس در فصل آینده مشخص شد
🔴
محمد مهدی زارع ؛ شماره 4
🔴
محمد عمری ؛ شماره 7
🔴
مهدی تیکدری ؛ شماره 8
🔴
ایگور سرگیف ؛ شماره 11
🔴
یعغوب براجعه ؛ شماره 13
🔴
پوریا شهرآبادی ؛ شماره 17
🔴
امیرحسین محمودی ؛ شماره 19
🔴
مجید عیدی ؛ شماره‌ 20
🔴
ابوالفضل…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136672" target="_blank">📅 18:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
❗️
سایت طرفداری: استقلال نزدیک به ۱۰ هزار میلیارد بدهی بالا آورده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/136671" target="_blank">📅 18:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136670">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
قدوسی: محسن خلیلی میخواد بعد از جذب کسری طاهری قرارداد ایگور سرگیف رو فسخ کنه . تارتار تاکید ویژه ای کرده که سرگیف رو میخواد اما خلیلی میخواد سرگیف بره تا گرا بمونه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136670" target="_blank">📅 18:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136669">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
❗️
شهاب زندی مدیرعامل نساجی :
❌
❌
آقای خلیلی میگه کسری طاهری رو نمیخواستیم و گرون بود، اصلا قرار نبود برای کسری پول بدن، اصلا ما نمیتونستیم کسری طاهری رو بفروشیم، ما خودمون کسری طاهری رو خریده بودیم و ثبت کرده بودیم
✅
✅
هوادارای عزیز، مردم، مسئولین و همه سازمان…</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136669" target="_blank">📅 18:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
۳ خرید ناب در راه پرسپولیس
💥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136668" target="_blank">📅 18:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
✅
محمدامین کاظمیان بخشی از قرارداد توافق پرسپولیس با گلگهر برای جذب پوریا لطیفی فر می‌باشد
🔹
محمدامین کاظمیان + حدود ۸۰ میلیارد رضایت نامه = پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136667" target="_blank">📅 18:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136666">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
باشگاه استقلال پیشنهاد 5 میلیون دلاری آسانی رو قبول کرد و این بازیکن شنبه به ایران برمیگرده !!!
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136666" target="_blank">📅 18:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136665">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136665" target="_blank">📅 16:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136664">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
تارتار اسم یه مهاجم خارجی رو به باشگاه داده و درصورت جدایی بیفوما و گرا مدیریت برای جذبش اقدام میکنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136664" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136663">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
❗️
خطر رفع شد؛ به ادعای ورزش سه زکی‌پور ۲ ساله با تراکتور بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136663" target="_blank">📅 16:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136662">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
دنیل گرا و تیوی بیفوما هم توی اردوی ترکیه کنار پرسپولیس هستن.
❗️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/136662" target="_blank">📅 16:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136661">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
۳ خرید ناب در راه پرسپولیس
💥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136661" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136660">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚠️
⚠️
تیم فوتبال پرسپولیس در اردوی ترکیه با فنرباغچه که هدایت آن برعهده اسماعیل کارتال است، یک دوستانه بازی برگزار خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136660" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136659">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
پناه بگیرید
✅
میلاد زکی‌پور رسما از سپاهان جدا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136659" target="_blank">📅 14:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136658">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔹
نگاهی بندازیم به هایلایت‌ پوریا لطیفی‌فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136658" target="_blank">📅 14:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136657">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
میلاد زکی پور، مدافع چپ سپاهان پس از قرار گرفتن در لیست خروج محرم نویدکیا، به پرسپولیس معرفی شده تا جانشین میلاد محمدی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136657" target="_blank">📅 14:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136656">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8lpt3_jiJKnyFLgpbcGq8Mo1M_5SakM492FvNbAWupYUrNwwT4PJnh_yFFs3yvGwq0KUqs5ylovCvPScbh8M80lFDBTbFeSETQR61ODmjtxXT5yx7ikij4poxOWC6W5zPR1wc_jL1Rfh0Co6ffWyRGLD3AVwINYpzeYjB_NgCBov2ztq9PvMLmasP8qERbmrzGnhsh5A-QQbnn1_8AeROG060BhpO4kOx6CdYN51JwZiJWX2mfCioucSnW0tr5Cn8PJSYhPzK9C8WOUxQM4GNYd_BAHP6jJT6IyyW-_YI2cenT1QwwXdbgv-Tp_vqlHAGmPnPCMVIsX3IZ4ifp0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136656" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136655">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMoqZL5mcEdWFAd01t6UJwhro-JnBvYi2lz23wA2b-xL8VPSkWp7A7M4bwCNxiaiWOVgFftLhVOXjlt01C6t7NFL-zgfI7PP5Et5A9Ggwq9aIIhkTnEHlHwingIEYd5F1UE9KQi2M4WRwWoEA12ayM4xe6XxUikYqdJbZ4qFHE6nwm_JcvrRT_Jq4XvvIuSWyJTdaC8A_V3UBJjziVqPKkt6QujUC7n9DxJt2UdKfbX8v5qF8H1_Amop_ml9dNgLP8P_ynpuJWokzjawacqxKxsXNidNd045As5OCn8MQzSYpDqB9-JFBpl8qioRvOSTW5_sdcicVDsgkzrlxVhDVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
۳ خرید ناب در راه پرسپولیس
💥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136655" target="_blank">📅 14:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136654">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTTicAHzktByJKEYBrcHPfJ3sX_XISslhSEFpxCxoYVjpDlTa-SROQu99T36nVM4eKAfFsm683bb09lbH8V5NiEBOA8IsSdc7KqwG3CQJz0YZ-1x49zpYwE9gaGO4JWY9MRK4NhVwRjROWcfBqcUEjyjGc3kovd3gxFT3YzIyhwHfAncI5_0kxSCHz45oAmwWWri0iJDCWqwREk-5sATNjl7ZjXD7ic6zhEKGS78CYncISkKUkE3U5--ZB7vKtARd_mNZMfd2da0LasKfNC5bxMoHnFATgwWZwxxNfKyBUG3HiPQ-AKk0Vmd8D06h7W8YLQIqVLeT_NaxaPE0FUsVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مدیر رسانه‌ای جدید پرسپولیس انتخاب شد
❗️
❗️
فربد بقایی مدیر رسانه‌ای سابق چادرملو و ساپیا جانشین روزخوش شد.
🔴
🔴
بقایی حدود ۱۰ سال قبل در سایپا فعالیت داشته و فصل گذشته در باشگاه چادرملو مشغول به کار بود.
🔴
🔴
خبر انتصاب بقایی طی امروز یا فردا از رسانه باشگاه منتشر خواهد شد و بزودی او راهی اردوی ترکیه می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136654" target="_blank">📅 14:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136653">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136653" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136652">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
واکنش ابوالفضل رزاق‌پور به پیشنهاد پرسپولیس:
🔴
نامه رسمی به باشگاه فولاد آمده ولی من وظیفه دارم سر تمرین بیایم تا تکلیف مشخص شود. خودم با باشگاه هیچ حرفی نزدم و دو باشگاه باید باهم حرف بزنند.
🔴
🔴
حضورم در پرسپولیس برای دعوتم به تیم ملی تأثیر دارد ولی امیدوارم…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136652" target="_blank">📅 13:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136651">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
مشکل سربازی فرهان جعفری حل بشه با قراردادی ۴ ساله پرسپولیسی میشه/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/136651" target="_blank">📅 13:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136650">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">#تکمیلی
⚽
💥
حدادی منتظر پاسخ محمد مهدی محبی؛توافق با کلبا انجام شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/136650" target="_blank">📅 13:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136647">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
💣
One Signature. One Earthquake…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/136647" target="_blank">📅 13:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136646">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🤩
باشگاه پرسپولیس فردا در دیداری تدارکاتی به مصاف پیرامیدز مصر خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136646" target="_blank">📅 13:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136645">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136645" target="_blank">📅 13:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136644">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIi8pC_ESTnCTwkok0Wo7VgFo4LcnbrxA3LNq6rq9I5KTEmsKXWvLK1kY9T4C_I-aAqmaRzHnt7zROVHOP3F8t7T0G7o5NKr2I0is8L9Qy05KJVm-2g3UMIcaBSMXIzeHDNhgF4FEmqCoY2qm33LkpSBrIqtG_V2378LC8Z-swKNg-hUUpoYcpF6_VIMp7wKcU0zOtJR5lnFFulCyhfBt5bD-lNSxwCujZS5yOnXadvYhyqiHNnub3WdPuKxEPunizoLzGVZCjynYOU-jFWXU9nDWoiRzs-8PbuQtPuDbSjrfHUzqj2o62XgFwejD3PUHOEFjVkx9EFRwnRmBxCf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لطیفی فر با عقد قراردادی چهار ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136644" target="_blank">📅 13:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136642">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136642" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136641">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136641" target="_blank">📅 12:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136640">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
امروز تکلیف نهایی دانیال ایری و کسری طاهری برای پیوستن به پرسپولیس مشخص خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/136640" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136639">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
بعد از 13 شب .دیشب و بامداد امروز هیچ حمله ای به ایران و نقاط ایران از جمله جنوب نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136639" target="_blank">📅 11:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136638">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه پرسپولیس قصد داره‌ تا ۲۴ ساعت آینده از چهار خرید جدید خودش رونمایی کنه ///فرهیختگان
🤝
محمدرضا اخباری
🤝
دانیال ایری
🤝
کسری طاهری
🤝
پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136638" target="_blank">📅 11:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136637">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
برخلاف شایعات ؛ حضور براجعه در تصاویر اولین تمرین پرسپولیس در ترکیه
❌
در حالی برخی منابع از عدم حضور براجعه در اردوی ترکیه پرسپولیس خبر داده اند که این باریکن در تصاویر اولین تمرین سرخپوشان در ترکیه حضور دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136637" target="_blank">📅 11:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136636">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
🚨
🚨
باشگاه پرسپولیس با باشگاه اتحاد الکبا برای انتقال محمدمهدی محبی به توافق رسید  #قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136636" target="_blank">📅 09:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136635">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StdDyOumQiLxIDlu5sQ-CUCFM5QZ1n5UniaoPPV8yCgwPcI0fxYXbSqpmPV25ZmB9jbied1L_40CseKE485Q7MyyUsY_6uzFdUgN5T9ateN7C2CSXxm9qRwD3kc5H1cADnnPIzizxVUbVxKw0O9XpweJz4K0ZWKaMaFinfXw7lmklFr9GZchGId0kFe1I10vBgzQtJTtHsPVP2EhVehZQjSkVsd9p20mYRVv4hrUBEEqAR92PeY-rETDNX2W8VxEZ977PrtgdXIutv9pCDXNV1grehZCWYaMt2wDK9euDgGYYC4su6QWs1AQ568NbHOtH_2JPb3Dq5WV_jyfSgWuZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعات ؛ حضور براجعه در تصاویر اولین تمرین پرسپولیس در ترکیه
❌
در حالی برخی منابع از عدم حضور براجعه در اردوی ترکیه پرسپولیس خبر داده اند که این باریکن در تصاویر اولین تمرین سرخپوشان در ترکیه حضور دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136635" target="_blank">📅 09:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136634">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
🚨
🚨
باشگاه پرسپولیس با باشگاه اتحاد الکبا برای انتقال محمدمهدی محبی به توافق رسید  #قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136634" target="_blank">📅 09:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136633">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
محمد مهدی محبی تمایلی ندارد قرارداد یک میلیون و ۴۰۰ هزار دلاری خود با باشگاه کلبا را از دست بدهد. باشگاه کلبا نیز قصدی برای ادامه همکاری با او ندارد، اما خود بازیکن حاضر به کوتاه آمدن نیست. با این حال، پرسپولیس هنوز از جذب او ناامید نشده است.///قدوسی
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136633" target="_blank">📅 09:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136632">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه پرسپولیس قصد داره‌ تا ۲۴ ساعت آینده از چهار خرید جدید خودش رونمایی کنه ///فرهیختگان
🤝
محمدرضا اخباری
🤝
دانیال ایری
🤝
کسری طاهری
🤝
پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136632" target="_blank">📅 08:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136631">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚠️
باشگاه پرسپولیس هنوز با مرتضی پورعلی گنجی برای فسخ قرارداد این بازیکن به توافق نرسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136631" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136630">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
بعد از 13 شب .دیشب و بامداد امروز هیچ حمله ای به ایران و نقاط ایران از جمله جنوب نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136630" target="_blank">📅 08:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136629">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
✅
#تکمیلی | رویترز:
🔴
ترامپ دستور حمله قدرتمند به ایران را صادر کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136629" target="_blank">📅 08:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136628">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9Zw_8gRgTHSyZszveY7AK5cmKyZk3SM8Eg5wT9RaAVK9ShpUZX9xJp_j8f-99tSaqrQbva6Q0Dn0pTX8d5XvAbKF9pfpG0v0bdnIIv4eQ4GRGgn2qQuCxOfV2-wWW2VZe0FEV1JVC7dY--1ZkTvyy6xIENTWl_n29JVCRBDX080d6xjKAIp6B7-WOFdnG1sytf_PhrKRIAHqS9shgs7m576vXRWI-Eo2tl1gjgdAmIOd05H_c0yCo4e3OUNlsy_I1aJjPySeafLVb35mQr-CAPpiTXHdnpLhlL7SFasNI52cTVTGmU-BdVBKw00alE6YiSbS4lNoY56lHDf_erfBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136628" target="_blank">📅 08:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136627">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136627" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136627" target="_blank">📅 01:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136626">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB7Nvx99G2Uu2ZlYoQqPeDVbu1OXRUDokMumozBS35EQ9Tf10mPE3Ef47KDEENce0FpuHn4yxSraVni3gALi-D-56yZVKbPeMxzjt6hc_Ea-uPSPoxlG5BxxGYMCj3i1G1IABLU5OQjtGbgjBxmqPxoOe36l8azvM2xwhgvZ_hGzhpHf4Idz-GfiLyKrfUdqFgu49yoqiXK-vHOYsi3mF0chJ0k7daZqTXU1rSKm5W00nkCn3oktibrw1szhEOEJYA_HQ4NX-Rjt3mIVafgwRuVM0zMnUEej0yTs5fnOiHmourbIGrJA0RoqCrBUmCj9YZtu8OeJVOAx6rnwvk0VJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هر
چهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
Ⓜ️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/136626" target="_blank">📅 01:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔹
دونالد ترامپ: با وجود اینکه درحال گفتگو با ایران هستیم اما باید بگویم که مهمات ما برای یک حمله وحشتناک به ایران تکمیل شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/136620" target="_blank">📅 23:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136619">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
#فوری |ترامپ به شبکه 12 اسرائیل: من در حال بررسی امکان انجام حمله‌ای بزرگ‌تر از هر چیزی که در گذشته شاهد بوده‌ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/SorkhTimes/136619" target="_blank">📅 23:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136618">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✅
تارتار دنبال جذب یک وینگر دیگه‌ست؛ بین گزینه‌ها فعلاً فقط با محمدمهدی محبی مذاکره می‌شه. برای همین هم بیفوما رو به اردوی ترکیه برده تا اگر وینگر جدیدی جذب نشد، ازش استفاده کنه.
❌
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/SorkhTimes/136618" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136617">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
تقویت پست وینگر و جذب محبی از کلبا تازه ترین هدف و تصمیم نقل و انتقالاتی تارتار است.
❌
محبی که مربی کلبا روی بازیکن خارجی دیگری به جای او حساب کرده نمی خواهد قرارداد یک میلیون و ۴۰۰ هزار دلاری اش را از دست دهد. باشگاه پرسپولیس امیدوار است محبی نرمش نشان…</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/136617" target="_blank">📅 23:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136616">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/136616" target="_blank">📅 22:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136615">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
معامله گری که سرباز شده و برای دفاع چپ فقط ی جلالی و داریم و خلاص که اونم مصدوم شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136615" target="_blank">📅 22:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136614">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">💥
💥
شماره جدید بازیکنان پرسپولیس در فصل آینده مشخص شد
🔴
محمد مهدی زارع ؛ شماره 4
🔴
محمد عمری ؛ شماره 7
🔴
مهدی تیکدری ؛ شماره 8
🔴
ایگور سرگیف ؛ شماره 11
🔴
یعغوب براجعه ؛ شماره 13
🔴
پوریا شهرآبادی ؛ شماره 17
🔴
امیرحسین محمودی ؛ شماره 19
🔴
مجید عیدی ؛ شماره‌ 20
🔴
ابوالفضل…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/136614" target="_blank">📅 22:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136613">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
پرسپولیسی‌ها عصر امروز تمرینات خود را در حالی پیگیری کردند که پیام نیازمند و محمدحسین کنعانی‌زادگان پس از حضور در جام جهانی ۲۰۲۶ به تمرینات تیم اضافه شدند و کریم باقری نیز در جمع اعضای کادر فنی حضور یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/136613" target="_blank">📅 22:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136612">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
باشگاه اتاق محمدرضا اخباری را در ترکیه رزور کرد و هم اتاقی کاپیتان تیم حسین کنعانی خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136612" target="_blank">📅 22:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136611">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVW0yoqjfzjFyy2lTVQdQJ3E1vuB-iOfpUcIBw5CTmNt6L-HwErNtqH7HyiLiI1DphT_AH_N-cBzG1T6iL98m6v5n1_j-DbyeIJEcEe9y93Njby5HjMYUuzB3odretoCgNDk4A74rmTYq1BRIAW79aJGr8wZXEejCHq7ScxE_MtxADjVz1YT4mHUmUBhmoOz4eP173STgvqNp7z09__pYZjiU7FLxEksLPhNi1AO8TKO-owJkNIO8MUAknYv3Lna2U9ztNhOyaskBsTzxaIIBtykaqjGWY9BKhRJkaNmmJ14-ne8BM_1Wnw_PI4sH1rhRwSAYeVvjL8lLrY1bp1iLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
حضور و اولین تمرین پوریا شهرآبادی و محمدمهدی زارع با لباس پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136611" target="_blank">📅 22:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136610">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
مهدی تیکدری وارث شماره 8 پرسپولیس در فصل جدید خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/136610" target="_blank">📅 22:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136609">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3Zxt8xnsovpqUv1edjf5A7bEd0PXGgY3H-4zjANDB4dmFaFSfEYjP5zsEZNLgIvaMYvxuadb_8FCcJR3IihagBd4FkcpPaS61UE02vBLDpFB2Z4WDTf6ro6cV9uXPzheAb8XLlojxmXTNmbfJOh2eVHeKjEES1nUUMNq-ukQqsR7tSTKRGW5_UmWnQVZoZQ85Iunv2ufDz9kExV0iq0DR1Kt_mi_RteE2HJdk6F8FlWJ1hg89a6pH3fo4G302-qz0Y_OWdwoFaIE_wk7KHqdJ09LE8a29hRCdv1YWzFQHjLxlthVG062Sm1e7ZVFpcOFiOEMaFhUto6V2kxQ5_vcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/136609" target="_blank">📅 21:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136608">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌀
🌀
هیات‌مدیره پرسپولیس فردا درباره جذب کسری طاهری و دانیال ایری تصمیم می‌گیره؛ با توجه به استعلام‌های مثبت، احتمال نهایی شدن قرارداد این دو بازیکن زیاده.  قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/136608" target="_blank">📅 20:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136607">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
فرهان جعفری در یک‌ قدمی‌ پرسپولیس/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/136607" target="_blank">📅 20:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136606">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⚠️
باشگاه پرسپولیس هنوز با مرتضی پورعلی گنجی برای فسخ قرارداد این بازیکن به توافق نرسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/136606" target="_blank">📅 20:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136605">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
❗️
2 خرید جوونمون تو این پنجره :
🔴
پوریا شهرآبادی 20 ساله
☑️
🔴
محمدمهدی زارع 23 ساله
☑️
🔴
اهداف بعدی :
🔴
فرهان جعفری 20 ساله
🔴
پوریا لطیفی فر 22 ساله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136605" target="_blank">📅 20:45 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
