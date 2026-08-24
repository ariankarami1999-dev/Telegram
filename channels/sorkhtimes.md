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
<img src="https://cdn4.telesco.pe/file/nBXE8GDzQwgQletVowe28iQN2FnmT99t00mSV3TZ0bMks3czizjWjhJbIwmTcAI1siENorOWZFkOSMl33nXOZOmzG9XKlq_Sdt9E4JtH7sgy_QXz6us2FfP7wpTAmbFAdvzbjiJ7eMPQ95phthkicjm2witM99E708ZpWWpPAEyv3tdR8EPbTZeY9fsaXZNqMpT9y8M2U27iR5n7ca4FMvSe2YSbDwIM9e_OJqZ8CegjoPsMQuW6ncaFgfgKG190SuisE4lO_-QiKt05VtG6J_A0IzNvKfKq8iD1EmrsLVHZwLyEAf9JG7CHZsukjVJKx1sU4VuYqF5odGtxd3u0NQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 23:49:18</div>
<hr>

<div class="tg-post" id="msg-138918">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
با تمام وجود امیدوارم این آخرین عذرخواهی شما باشه از هواداران ///اعظمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/138918" target="_blank">📅 23:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138917">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
حدادی مدیرعامل باشگاه:
🔄
🔄
ضمن عذرخواهی از هواداران محترم همه ارکان باشگاه در باخت مقصر هستند؛ از مدیرعامل تا سرمربی و بازیکن.
🔄
🔄
اما برای موفقیت، یک راه داریم؛ حمایت از سرمربی و حمایت از بازیکن، بخصوص بازیکنان جوان، اگر جوان‌ها اشتباه می‌کنند. مقصر من…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/138917" target="_blank">📅 23:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138916">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
جوان بازی دادن تاوان داره
🗣
لطفا با یه اشتباه اینده های باشگاهو خراب نکنید
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SorkhTimes/138916" target="_blank">📅 23:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138915">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqP1H1Q-03BW2XuHWUsSj9vAXxC5voPp9Oc3sX3Q6nY1AVAwl1LAgX8TGkkYRK6x8pBYS1ODEoxptor9Ki_agaoGpzF3S0ZWgUsi8ubqBQH-lEZe8u-llcqzOF_XxPq0dsE_C0ORmGMCauz7QVrcabXPr4TETE-Y1Whqj4Q_0DxIGH2uVvU6E2byfNMJG1mr8wNP3Fmclny6aRvyCorwEhKVp4-miW2y238aqn_l7qq6CgV9PJUNdaXd36D5nhXaym_lWeJxrlF_A_p-QFbs3PsziOKBNV5htGnevwqe1PMpJf-MWdu4hsEnjO-6WbR-BDTJS7VXdf7Psz2l6E1-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
جدول لیگ برتر پس از پایان هفته سوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/138915" target="_blank">📅 22:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138914">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
باید بچه ها به خودشون بیان ...فاصله بازی ها کوتاه کوتاهه ...امیدوارم این باخت و جبران کنن ...با فاصله خیلی کم شنبه با ملوان بازی داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/138914" target="_blank">📅 22:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138913">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚽️
⚽️
⚽️
⚽️
از بین ابرقویی، تیکدری یا عیدی یکی دفاع چپ پرسپولیس مقابل تراکتور خواهد بود/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/138913" target="_blank">📅 22:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138912">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
⚽️
✍️
دانیال ایری، مدافع ملی‌پوش و جوان فوتبال ایران با امضای قراردادی ۴+۱ ساله رسماً به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/138912" target="_blank">📅 22:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138911">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
⚽️
✍️
دانیال ایری، مدافع ملی‌پوش و جوان فوتبال ایران با امضای قراردادی ۴+۱ ساله رسماً به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/138911" target="_blank">📅 22:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138910">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLwJ_q4Pdfl9LmdG-0nvaeCR6hs0nl6mtJeE9C1ac-1zq2rd8z9Xjrmr59qknPFpoOw7XGd2gZFDBHZmLcwn9VEb4XYVq0NOC5m6bmPotQgh7kt_ygHd7Oxc5ez-hU88RoOSAN7_sPFnBdNu7ICTM4FDkPycsXTnNWCWcVpz17Usxv02_GxTPsFpLqqoBPKddbgc-JPQPkfH98m6NdemdWsiV-8JZNNv6MxM_RqHLarl_UkhsJCRfhObO3dlckWnAEKJUJddeoJevfFCd9OPgOpGl7tttAeTWdOiuL41SN1uMUfgVH-iJP29l3MkptOZcAGFoU7_Fxa4okdZDpUFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تنها فقط تا آخر امشب فرصت برای بونوس ویژه بازی Scarab Temple باقی مانده!
🔵
کاربران اسپورت‌نود می‌توانند با هر بار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود ‌اسپین رایگان کازینو دریافت کنند.
🔵
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
📌
نسخه جدید سایت:
Sportn5b2.com
📌
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/138910" target="_blank">📅 22:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138909">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
ترامپ درباره ایران:
🔻
به نظرم این جنگ به‌زودی پایان خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/138909" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138908">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
✔️
تارتار: مسئولیت باخت امشب با کادر فنی است؛ فوتبال همین است اگر اشتباه کنی بازنده می شوی
🗣
جوان بازی دادن تاوان دارد/ اکثر بازیکنان تعویضی ما سنشان 20 تا 22 سال بود. نیمه اول موقعیت های خوبی داشتیم/  امروز کم شانس بودیم و کم تجربه، تاوانش را هم دادیم…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/138908" target="_blank">📅 22:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138907">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
کمال کامیابی نیا: هواداران پشت دانیال ایری و دیگر بازیکنان باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/138907" target="_blank">📅 21:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138906">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
با تمام وجود امیدوارم این آخرین عذرخواهی شما باشه از هواداران ///اعظمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/138906" target="_blank">📅 21:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138905">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
خلیلی: امروز فقط بهای جوانگرایی را دادیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/138905" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138904">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
✔️
تارتار: مسئولیت باخت امشب با کادر فنی است؛ فوتبال همین است اگر اشتباه کنی بازنده می شوی
🗣
جوان بازی دادن تاوان دارد/ اکثر بازیکنان تعویضی ما سنشان 20 تا 22 سال بود. نیمه اول موقعیت های خوبی داشتیم/  امروز کم شانس بودیم و کم تجربه، تاوانش را هم دادیم…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/138904" target="_blank">📅 21:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138902">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
امیر رفیعی، ابرقویی، عمری، سرگیف، شهرآبادی، محمودی، اورونوف، همایی فرد، سلمانی، باکیچ و ایری، بازیکنان ذخیره پرسپولیس بودن.
‼️
اصلا شما نیازمند به همین ترکیب اضافه بکنی به قرآن شانس برد مون ۷۰-۸۰ درصد بود/ حالا شما کنار این نفرات چنتا از نفرات اصلیت مثل کنعانی،بیفوما،زارع و حتی محبی رو اضافه کن اصلا تو مخیلات منم نمیگنجه ارونوف،سرگیف،باکیچ،محمودی حتی یاسین بزاری نیمکت استفاده نکنی، بازی هجومی و چشم نوازی ارائه نکنی حتی نتیجه حداقلی هم نگیری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/138902" target="_blank">📅 21:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
با تمام وجود امیدوارم این آخرین عذرخواهی شما باشه از هواداران ///اعظمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/138901" target="_blank">📅 21:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2280d396d6.mp4?token=npqyOmdveumW24XI6M548RO1L6RJjwOeEPietefXqvPKAqSsAoQ7Vxw5pUfAxK1YKM3aVuWisBSho6-HR4npB9tDpt20dztJG1igGzuK__4-8kL-vuEz-7ZTVTm3PIMBYRL-2BHUCHjmiCeIfhNCFC4uAiZS96j2ZA93y1-h0WQZE1H9ZScylYRagt7MfoQLcIcrrARH9Z5HX2mWDh_yPrmtBE3OhKQEYent5UguEBu8bojqEZTSKE5Pwg3NEiDeNyZcNwosbC4KCdtUaBrqnDlUITaJU4t1_TCLz24kPIg2qHSQyKq_w-67qRK5RjXyKermn6SI2EZRAzHomOsJOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2280d396d6.mp4?token=npqyOmdveumW24XI6M548RO1L6RJjwOeEPietefXqvPKAqSsAoQ7Vxw5pUfAxK1YKM3aVuWisBSho6-HR4npB9tDpt20dztJG1igGzuK__4-8kL-vuEz-7ZTVTm3PIMBYRL-2BHUCHjmiCeIfhNCFC4uAiZS96j2ZA93y1-h0WQZE1H9ZScylYRagt7MfoQLcIcrrARH9Z5HX2mWDh_yPrmtBE3OhKQEYent5UguEBu8bojqEZTSKE5Pwg3NEiDeNyZcNwosbC4KCdtUaBrqnDlUITaJU4t1_TCLz24kPIg2qHSQyKq_w-67qRK5RjXyKermn6SI2EZRAzHomOsJOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔄
🔄
گل اول مس شهربابک
گل به خودی عجیب !!!!
که می‌تونه نامزد پوشکاش بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/138900" target="_blank">📅 21:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
تارتار: عذرخواهی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/138899" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔄
🔄
تارتار سرمربی پرسپولیس: بازی کم رمق امروز؟ به دلیل نبودن هواداران بود/ امیدارارم از این به بعد تمام بازی‌ها با هواداران برگزار شود
❌
❌
دلیل بازی نکردن ارونوف و سرگیف؟ این به کادر فنی مربوط است و دلایل فنی نداشت
⚪️
ما تیم پرمهره ای هستیم همه با هم رقابت می…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/138898" target="_blank">📅 21:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🗣
🗣
تارتار:اورونوف و سرگیف به دلایل فنی نیمکت نشین بودن و من این تصمیم و گرفتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/138897" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
تارتار: عذرخواهی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/138896" target="_blank">📅 21:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
پرسپولیس پس از ۷ سال در تبریز برابر تراکتور شکست خورد‌‌‌‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/138895" target="_blank">📅 21:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138894">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
پرسپولیس پس از ۷ سال در تبریز برابر تراکتور شکست خورد‌‌‌‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/138894" target="_blank">📅 21:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138893">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
❌
تو روزی که تراکتور هم هیچی نداشت حتی یک موقعیت بازی و باختیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/138893" target="_blank">📅 20:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138892">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⛔️
کوصکش خر لج کرده با خارجی ها، کدوم کوصکشی سرگیف که بازی قبلی گل زده میزاره رو نیمکت ؟! اورونوف نیمه دوم نیاوردی تو عمری آوردی گذاشتی مهاجم سایه ؟! شرف تیمو بردید به جای مهاجم و وینگر آوردن دفاع وسط اضافه میکنی؟! پرسپولیس با ۵ دفاع قهرمان نمیشه اقای تارتار…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/138892" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138891">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⚠️
آقای جاکش بخای ترسو بازی بکنی تیم میبازه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/138891" target="_blank">📅 20:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138890">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⚠️
آقای جاکش بخای ترسو بازی بکنی تیم میبازه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/138890" target="_blank">📅 20:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138889">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
تارتاری که ترسو بود ..سرگیف و ارونوف و نیاورد و دفاع آورد ..با ی اشتباه دفاع بازی و باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/138889" target="_blank">📅 20:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138888">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
توی ی بازی سرد و یخ و بی روح و کلا دو موقعیت با ی اشتباه بازی و باختیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/138888" target="_blank">📅 20:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138887">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❤️
❤️
نیمه دوم هم شروع شده امیدوارم با تعویض ها هجومی تر بشیم و بریم برای برد ....امیدوارم تارتار از باخت نترسه و بره برای ی بازی هجومی و برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/138887" target="_blank">📅 20:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138886">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❤️
❤️
نیمه اول حرفی نداشت برای گفتن و گزارشگر ..تو نیمه سرد بازی صفر صفر نیمه اولش تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/138886" target="_blank">📅 19:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138885">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❤️
❤️
❤️
الهی به امید تو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/138885" target="_blank">📅 19:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138884">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
✔️
✔️
کم کم بریم سراغ بازی حساس و استرسی ..امیدوارم تارتار از این بازی بزرگ هم سربلند بیاد بیرون ...امیدوارم .بیرانوند و شجاع اخر بازی از باخت فشاری شده باشن.امیدوارم ببریم بازی و انشالله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/138884" target="_blank">📅 18:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🟥
💢
گرم کردن بازیکنان پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/138883" target="_blank">📅 18:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f3c54f76.mp4?token=eoAYnXXs9UE8HgLvqfj6KauGe5hO8wT4epELBkzCtVnAtMoGmzd8Dezl8WxDSPiWexrwY1b2Z1GtWY7rySr_40--GAb1b9tygCTbN-t1xNv7V27gcRGx8KToyTw86K5B3oagEoqL2Zx74h9CGiL13afEprjQe1oCvdgyLaw-nRR6s546Txq3qjLMazwEzB5zjQ4qkOJr2-RdHVS8sDcFRsXDDpmug3Q2K7iBIp0nSCyArjGY5J-E2pMhjv6zBta8P-jpMIAsBUea3km8QpCsdwB0V8b4MxjAYhqRTwT4wprKOv-_y-FnFpCRzQj1mtfKbOgAKtFDrAcXpYqy-wOdag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f3c54f76.mp4?token=eoAYnXXs9UE8HgLvqfj6KauGe5hO8wT4epELBkzCtVnAtMoGmzd8Dezl8WxDSPiWexrwY1b2Z1GtWY7rySr_40--GAb1b9tygCTbN-t1xNv7V27gcRGx8KToyTw86K5B3oagEoqL2Zx74h9CGiL13afEprjQe1oCvdgyLaw-nRR6s546Txq3qjLMazwEzB5zjQ4qkOJr2-RdHVS8sDcFRsXDDpmug3Q2K7iBIp0nSCyArjGY5J-E2pMhjv6zBta8P-jpMIAsBUea3km8QpCsdwB0V8b4MxjAYhqRTwT4wprKOv-_y-FnFpCRzQj1mtfKbOgAKtFDrAcXpYqy-wOdag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
خوش‌وبش گرم و صمیمی کریم باقری و خداداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/138882" target="_blank">📅 18:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138881">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b25482bf71.mp4?token=tz5QVwY9hroHYGJw5tP4x0UmKaaGaBoLAabR_4XzwUBCrGmOqfY6DtiTr9_utoRlRQYYoYRK69qp3aa7GcGRZsPQjiF2wFeAyfsbLSvnD1DXaGme-KYPGP7zB7lA503yl47t7ti5MucLnQyxGBhqbb1h1YZPBklTyNQ_WY-mN9iC2XtupszyWHJabQcvagKIsaU5e2LhtZed6y9iCGzASZuHh1w1G78UDUqxM-2Dm_IGf1bs2gO0Ivafhh-z9hd0zmroGzXxDA3_ZIGR50JZXY4QA_lwMm5I0Xul_G_QCC8yuFvL9UCQhaRL2dm0k-_E2WjRjz7t3P42uwbGuKeUmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b25482bf71.mp4?token=tz5QVwY9hroHYGJw5tP4x0UmKaaGaBoLAabR_4XzwUBCrGmOqfY6DtiTr9_utoRlRQYYoYRK69qp3aa7GcGRZsPQjiF2wFeAyfsbLSvnD1DXaGme-KYPGP7zB7lA503yl47t7ti5MucLnQyxGBhqbb1h1YZPBklTyNQ_WY-mN9iC2XtupszyWHJabQcvagKIsaU5e2LhtZed6y9iCGzASZuHh1w1G78UDUqxM-2Dm_IGf1bs2gO0Ivafhh-z9hd0zmroGzXxDA3_ZIGR50JZXY4QA_lwMm5I0Xul_G_QCC8yuFvL9UCQhaRL2dm0k-_E2WjRjz7t3P42uwbGuKeUmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
💢
گرم کردن بازیکنان پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/138881" target="_blank">📅 18:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138880">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hc84Op38Wq1MpGPCbZGi9fdQ90T8XAN6UX6xCJkpbo9Pgxr9uxZHMSAuCwueMEMF8O9_9a1F9VUxy-vIaORCmtZIE-3rzQvpgyVPDYMKqBp75VjPRXIaPWtUn4ehJ5HgflQ6htwFB9Lf4C5ik0ib5NBE2f2McJgQJO2oim4XJtAjx4kgayHxcnFW9bhmzBZfZlkX3FO8N7JhgTNjvr1iWAR_o60AsIVF3ZpnVKHBiuzsFE4rdwsFUMKToZQ2by5-3il-EuR6gZplDmJqs_N4rFv2eP5tvs3GeptbrSvukWG1d-CwsH7rN2Y-iKHVqgcOT-OCVKCuQtI_iYPLQyDLlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
انفجار در تبریز؛ سرخ‌ترین نبرد فصل!
تراکتور و پرسپولیس؛ امشب فقط یک تیم می‌تواند با دست پُر از این جنگ بزرگ بیرون بیاید!
[
تراکتور
⚽
🆚
⚽
پرسپولیس
]
🔵
تنها فقط تا پایان امشب فرصت برای بونوس ویژه بازی Scarab Temple در اسپورت‌نود باقی مانده! کاربران می‌توانند با هربار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود اسپین رایگان کازینو دریافت کنند.
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
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/138880" target="_blank">📅 17:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138879">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/138879" target="_blank">📅 17:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138878">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/138878" target="_blank">📅 17:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138877">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30428072b5.mp4?token=MUkSAOKIhdAXnB7LWiilj8GxdHnHMPeWBOuqAEEP-b7FjtcL5V8_Qn2UCp96eauBfwC2kAMeCl1NWdidreeja7i09gRbzhwWKipnf48EeFfqjes3w5XcKkBzVt4OYeiSwssuCCgQUAOaxd8JnktF0uXfw093Ht8wusuV1_jv-YZRi6MYsPthXk_g07nyzjGUB3or2MiwYn3X3M_FaxkJUozi4yJ3G66S-FKaT4L9MDO4kfJcPLrX4TBHEAKcYvwSZc5UQwKpWasSVwKGt40TfMdrJykyKUuJ1xR33bpzYE-qdv4ROR8mejSLE1YMQ7QoFBRkYpGeEavdrCuaZCYZrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30428072b5.mp4?token=MUkSAOKIhdAXnB7LWiilj8GxdHnHMPeWBOuqAEEP-b7FjtcL5V8_Qn2UCp96eauBfwC2kAMeCl1NWdidreeja7i09gRbzhwWKipnf48EeFfqjes3w5XcKkBzVt4OYeiSwssuCCgQUAOaxd8JnktF0uXfw093Ht8wusuV1_jv-YZRi6MYsPthXk_g07nyzjGUB3or2MiwYn3X3M_FaxkJUozi4yJ3G66S-FKaT4L9MDO4kfJcPLrX4TBHEAKcYvwSZc5UQwKpWasSVwKGt40TfMdrJykyKUuJ1xR33bpzYE-qdv4ROR8mejSLE1YMQ7QoFBRkYpGeEavdrCuaZCYZrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از ورزشگاه یادگارامام در فاصله یک ساعت مانده به بازی تراکتور و پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTime
s</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/138877" target="_blank">📅 17:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138876">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSP2FcbVlzYokZ2qWwhji58g4pGJgKn2ylapo5ebHOb-aMbrkncNuIXJL8LQ64mmRnSQAVIfLgUewjC5FkMpwbAj0rDZISyC7_HEQMW7vDHDKeLNzdrqfl9Q3kN1C4QxKc_AsPyBMbBNCtKEQWf-dDd7-BbKnsQN3IiP9nPSB3bILW29twfAVDH6Wv13DCXOuIe42JSc7bof5dCtfOjHMYQ78j-99NSpjPPcKlLlB4bT0atWReVCwIk-GN2T0vs7FCCOTZxw9IaQoHTGPNtr7PLAuyNa2TT88UfW2D6-ZkLq0wIMyoM17ScZwWQJ3dbWinzStB-_S9bhV4-xyMcEgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/138876" target="_blank">📅 17:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138875">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
جواد نکونام؛ مهدی ترابی به دیدار حساس‌فردا باپرسپولیس رسید اما مهدی هاشم نژاد بدلیل مصدومیت این دیدار رو از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/138875" target="_blank">📅 17:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138874">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/138874" target="_blank">📅 17:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/138873" target="_blank">📅 17:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138872">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZE0e3mfUyuxkODizCq6yVjGoGZUqewo9H1VYiBDZCP-h5RPgHA0lScvXRSLzeXgY8DwOmcWqOZyMt_SvqC12JiGmDg3jjnTLxDr0r8RVL2v4DALhu2rKT_zpGNjBgkyihj0I_WkGop5XtVlIXwFpyUFSGgexT7Cu-ag7cJDrsupewDOxty8mTtobIvNmw6YqXuYegqrBDnBVJb1p1q7D7ccuCbut64bYAP3YiM3g6qab2WD4TgI5zpNZ06aDT86WoFd_hnwSGlzFIHasCsGBoz_7E3I7aogAHmzKKnTHi8YdeuDARR2pxIVh5VoNjbIbW5sPuLOuKPuIF8K9Z4ITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/138872" target="_blank">📅 17:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
🎙
بهنام ابوالقاسمپور؛مدیرعامل استقلال خوزستان:‌
🔻
با حدادی در مورد بیفوما حرف زدم.
🔻
ما باید مبلغی به کمیته وضعیت می دادیم اما چون ندادیم نورشرق به نفع پرسپولیس رای داد.
🔻
الان پول رسیده و باشگاه پرسپولیس هم گفته مشکل را حل کنیم و دیگر کار به دادگاه عالی ورزش…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/138871" target="_blank">📅 17:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a78fd471e.mp4?token=r2qhQVTZw98gEKCHuPQMfwMAd1Xo0qPsE9Ty146qlSBUHEyIJGH-IlXHUrA6GD4AoPu3kuHhiI18mPK_Rheul3KWC9yEvUGz7whX8aZQwy747ipkCfaV32Zioq9unH8_45qGhqkdwCJn7LMl02IV2FQaC-B8g78qf-P9zCKlmw3FAFRrt9cUxA15JJO8YMY5SdMlikPNq_X0TdOrruONWDUx-P4EqymM4B0cws_0SRoZ8SV3KMlUy5mwTQqvQSjGL5w-_cdW6U2WRnvH1_5N0u9M-LWGQLyYY3utEe3vrqlV4K3PU8JVVIfVedd0xYC-Gl1xEYnu0SEjaQemj3Widoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a78fd471e.mp4?token=r2qhQVTZw98gEKCHuPQMfwMAd1Xo0qPsE9Ty146qlSBUHEyIJGH-IlXHUrA6GD4AoPu3kuHhiI18mPK_Rheul3KWC9yEvUGz7whX8aZQwy747ipkCfaV32Zioq9unH8_45qGhqkdwCJn7LMl02IV2FQaC-B8g78qf-P9zCKlmw3FAFRrt9cUxA15JJO8YMY5SdMlikPNq_X0TdOrruONWDUx-P4EqymM4B0cws_0SRoZ8SV3KMlUy5mwTQqvQSjGL5w-_cdW6U2WRnvH1_5N0u9M-LWGQLyYY3utEe3vrqlV4K3PU8JVVIfVedd0xYC-Gl1xEYnu0SEjaQemj3Widoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
چمن خوب استادیوم تبریز؛
🆚
ورزشگاه خالی از تماشاگر آماده مسابقه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/138870" target="_blank">📅 16:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
نتایج 10 تقابل‌اخیرپرسپولیس _ تراکتور در تمام رقابت‌ها: 6 بردپرسپولیس، 2 برد تراکتور، 2 مساوی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/138869" target="_blank">📅 16:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✖️
✖️
پرسپولیس ول کن رزاق پور نیست
🗣
آناورزشی: پرسپولیس پیشنهاد معاضه همایی‌فرد با رزاق‌پور‌+ مبلغی برای رضایت‌نامه رو به فولاد داده که توسط فولاد رد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/138868" target="_blank">📅 16:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇺🇸
ترامپ: از این لحظه شدیدترین فشار اقتصادی تاریخ که تا به حال علیه یک کشور بوده، علیه جمهوری اسلامی اجرا می‌شود و‌ «هر کشوری» هرگونه کمکی از جمله اقتصادی، نفتی، صرافی و بیزنسی به ایران بکند را شدید‌ا مجازات می‌کنیم. این دیوانه‌ها گرفتار شدند و به آخر…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/138867" target="_blank">📅 16:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138866">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
فوووووووری / فارس :
❌
جدایی رزاق پور از فولاد منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/138866" target="_blank">📅 16:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138865">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
برخی هواداران ترتر جلوی هتل پرسپولیس جمع شدن و دارن سروصدا ایجاد میکنن تا مانع استراحت بازیکنان پرسپولیس بشن!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/138865" target="_blank">📅 16:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138864">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
✔️
ویژه‌برنامه تلویزیون پرسپولیس؛
🗣
🗣
🗣
تراکتور - پرسپولیس
🗣
🗣
ویژه‌برنامه تلویزیون پرسپولیس برای دیدار هفته سوم لیگ برتر برابر تراکتور، از ساعت ۱۷:۴۵ به صورت زنده پخش خواهد شد.
🗣
🗣
این ویژه‌ برنامه به صورت زنده از صفحات رسمی باشگاه پرسپولیس در یوتیوب، اینستاگرام،…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/138864" target="_blank">📅 16:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBf8stYRq0r8QRqg0bIDBiqcFQg2uk_7Z5pASU9OjuD20v4Ju5-5ekTIrFWHyKbDCccJ_BWe4tMJirV1paApRwElPHHVep9xNAwfar0NCpEkei2uSPEWp5EElr9x-lwSQht8sYTJeMrQwo2i6PRhMeHnk8ZyUSA4QrqLb9yq80cY5lHJyN-PQOU9gSnb5f1f0i9HKuz0PtFnJMtVYAwpCqcy4NB_grmmyCnsaz7-Qnle1xtNkdy7CGbe9g36uLwvEVLdiP5rkMSxTQWyxIF35fS0jj2MxyefggxQDV7ji-3lNo7CWakVe5vhT_-1rB5LBSrSrf4U1Dv0rA87Pa7bbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🗣
دنیامالی، وزیر ورزش: 500
هزار
میلیارد تومان اعتبار برای تکمیل پروژه‌های نیمه‌تمام ورزشی کشور نیاز است
😐
😐
😐
😐
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/138863" target="_blank">📅 16:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
فوری، با اعلام مهدی تاج سهیمه آسیایی ایران در فصل آینده لیگ نخبگان به 3 تیم افزایش یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/138862" target="_blank">📅 13:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138861">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔄
❤️
❤️
پیج باشگاه 10 میلیونی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/138861" target="_blank">📅 13:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138860">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔄
❤️
❤️
پیج باشگاه 10 میلیونی شد
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/138860" target="_blank">📅 12:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138859">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
❌
حجت کریمی مدیرعامل باشگاه تراکتور:
🔴
سخن‌گوی سازمان لیگ اشرافیتی به موضوع نداشت هم‌چنان درحال رایزنی با فدراسیون هستیم تا بازی تراکتور و پرسپولیس با تماشاگر برگزار شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/138859" target="_blank">📅 09:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138858">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔄
🔄
فوووووووری
✔️
مهدی تاج: ورزشگاه آزادی نیم فصل دوم در اختیار پرسپولیس و استقلال است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138858" target="_blank">📅 09:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138857">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGKE6q6Vu_mrjwTxRaSjWzi7pJir8oc9XOjNrCrwNYhUcuNGTHqLKjb9JwezhHuZENQmR3h-UVD4nDe7ZSWMYltXDsW8tNGJ7sBt4wIG7R-QYrjnLIaDszYH2kKumeGVEF8_Ljje8HCcuWLvsL9c209vgWaRM6FbnZW4sZCNenTIU0hABaGqoBVXe8ZpuSpO74tmFuIYqYZq8cLSYC2bECP85syDrUO5qnHdxtQC6wrmCLCXU-eRrch1_ijPb56AyXXpeoWI18Mtjyc2jXUpV69oy3xbpW4A-Mlzx0q02UBKrghn0rMWrvpNF7tXOSE6vK4F2pJ_1lnduDDUAOD7Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
ترکیب احتمالی پرسپولیس مقابل تراکتور از دید ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/138857" target="_blank">📅 09:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138856">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
فراز کمالوند: یک بازیکن از پرسپولیس برای معاوضه با ابوذر خواستم و اگه اتفاق خاصی نیفته بزودی این انتقال انجام میشه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138856" target="_blank">📅 09:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138855">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
تارتار:
🗣
🗣
فیفادی که نیست‌؛ به تیم امید که هیچی به هیچکس بازیکن نمیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138855" target="_blank">📅 09:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
🔴
🔴
🔴
صبحی که ی بازی سخت و نفس‌گیر داریم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138854" target="_blank">📅 09:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🟢
تنها فقط تا پایان دوشنبه برای بونوس ویژه SCARABTEMPLE فرصت باقی مانده!
🔵
همین حالا با هر بار شارژ حداقل
۱ میلیون تومان، اسپین رایگان متناسب با مبلغ شارژ
دریافت کن!
🔵
شارژ بیشتر؟ اسپین بیشتر!
🔵
هر چرخش، شانس دریافت جوایز نقدی
📌
فرصت محدوده؛ زمان زیادی باقی نمونده!
🔗
اسکرب‌تمپل
، با یک سیستم اسپین پرهیجان و جوایز متنوع:
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
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138853" target="_blank">📅 01:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138852">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
مخالفت با معاوضه و انصراف پرسپولیس یا مصاحبه ساختگی ؟
❌
❌
فراز کمالوند در واکنش به مصاحبه منتشر شده از سوی وی پیرامون پیوستن ابوذر صفرزاده به  به پرسپولیس به شرط معاوضه با بازیکن مدنظرش به رسانه باشگاه خیبر گفته:
❌
❌
من هرگز چنین مصاحبه‌ای انجام نداده‌ام…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138852" target="_blank">📅 23:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138851">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c596c40e2b.mp4?token=vYQdT1R5K8uHZktmkJLbpucm5q-KTgl-yFY5bitSOi0uot9IJlGA_LrzKgGQ-0YYpYgBYg4xNoQvA0nbpU-bpDPHaLqxXcfR7ggZa606CrsuWuMQdG7YC-56NcoCktEeZ54PeTJgjYF2GjOz3s2KQz712ld84TlRd_WnzIyY-x7ASCa-yxSibsULJ00tmaZ5w6HANd1f1SWj1SwZSuknxxYBeTfPKoQY7CB_QlCsv0EaFwsDOuK1jA57_i22ik3_pIwAAUvSbhfigNsproWRVKxZf-6jnYqTF1kJOGCWR6glBSK5Kj7PxNFHLMgdLLo6eyEDoyRq_82eTv6s_szf4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c596c40e2b.mp4?token=vYQdT1R5K8uHZktmkJLbpucm5q-KTgl-yFY5bitSOi0uot9IJlGA_LrzKgGQ-0YYpYgBYg4xNoQvA0nbpU-bpDPHaLqxXcfR7ggZa606CrsuWuMQdG7YC-56NcoCktEeZ54PeTJgjYF2GjOz3s2KQz712ld84TlRd_WnzIyY-x7ASCa-yxSibsULJ00tmaZ5w6HANd1f1SWj1SwZSuknxxYBeTfPKoQY7CB_QlCsv0EaFwsDOuK1jA57_i22ik3_pIwAAUvSbhfigNsproWRVKxZf-6jnYqTF1kJOGCWR6glBSK5Kj7PxNFHLMgdLLo6eyEDoyRq_82eTv6s_szf4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخی هواداران ترتر جلوی هتل پرسپولیس جمع شدن و دارن سروصدا ایجاد میکنن تا مانع استراحت بازیکنان پرسپولیس بشن!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138851" target="_blank">📅 23:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138850">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
فوووووووووری از ورزش سه؛
🔻
سرگیف و علیپور زوج خط حمله
🔴
بیفوما فیکس خواهد بود
🔴
اورونوف نیمکت‌نشین
🔻
تیکدری دفاع راست
🔴
عیدی دفاع چپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/138850" target="_blank">📅 23:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
رونمایی از کیت دوم پرسپولیس به یاد کودکان مظلوم میناب
پ.ن نظرتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138849" target="_blank">📅 23:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138845">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhwl0earxtnOv3u3JsF1fXOn-oEnTzoH45m-Ms3jHQEKGQGeuZZ3Xyyp5ONpPUtSYh9gWIowIWYSJX9p_VJ1KxVD-oCVT_JQXf3pjlv4YL24sVoeeQDde4ff7DGcxC6TVAxEz_OLxOf6zGF13_y7SZsJBQHbbU51baT-WOEhMYQ9t4SKCBM2rsBGWwLA126RfIyAP4H14d3X8mN-Wa3eckN4eQI5agJWj2z-HEBCau0H9uP6hekyG28EgbjaGsJPQeolsFefuZ97RqsIhGHO4h4Fro0SwW282dm9DTMBSJEmtiIZqv678CMuTyrBtdaIR56oBTxIRbrwBXbjAjIg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-2jZHoZF_QnofsxdsILmvSVxOSEvqGjZbpjGrUR_19zIDg6hNWN1zpBtnzvFRdA1PnyTzSAri1IKtT5zHsGY9mzgrxgS06c-zrQk5wOE_1_lHVCmgKSNCJwxnbvXTZ9RUU8uaToC4pw4Klx49AK_SZmHlv5lFVbina1HMaXqalsu20M4AGoP6GWCGqwDqHjtxmLfNhGLoTMz5Ft3AiWDTvlQ8j7nbKUwA-CD0mTkWbT1pSASzUxfChIYhSkZ2W5RE3G1817bzX0a4UkLd3YsZ1fKZcDzpdlW7dQkcelljX-sKH4P9Uq25plF7KvNdZamZ6o_HCErH6uZdqUuO-3DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kepi7ZuY0ljMn5BgPK-CpmARcaraOIBcbBl6oF-ecQ8bdmuqJGDsSRfcfrcuf_CbAdYOjw6xjrfzfFHRiMW4MCc-5scnB21loJdRLTYoi68IZSPHoz6MNZlEo6StYGgw4zD__K4G8dctVxCuHyLSesdWSQXNG-93ne4mYElY5g5VtUf4erOQzwG_evsWSHIej9z9szgHRN32B8R3FgoKCOIyYwZl-lo-hlm-Z_jLIuU9RqWf3X-kd55XRpfDa1cgVD4fdvnCp6l04H6A33RKUfpnvR2e3Z-UTyYwEh48NNAYjtH5ccZt6d_oE77S0EZ59JARp0M7PeKxRFAEG5C5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VsZGIyg-kNcMQFeK3h8kQj3V2jkjJSmx3-i3L9_lUsbMOnqycPdiM7ZwG3FJMrc7-9H4DriaQ834_hbPoBi6Vzl8unJrXbiOlbJWOP9Jm2Xx66dfTigpZiIXHA348auqsUMyOG679vhJBvVORNq5_x863uNgC8AGlDpAvd9JBD4I2oK3gn6JKGDghGYV1W-bUd5DaPHkXsOm_nRwXs-Q8zmUELELVYa3eLpK8LimGp3vHUCgFnZaGvOh1dJXXCsse_ADa-fEwE4_CbvB6Ur5o_3R4U_Z6_BHk4q0iGkNT09SjqooTArLCAwcKYFbYQlxcXaJ33YAeiAMpQbsQAeLGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
💢
پیراهن فصل‌جدید بعد از ادیت نهایی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/138845" target="_blank">📅 23:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138844">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
🔴
ترکیب احتمالی پرسپولیس مقابل تراکتور از دید فوتبالی:
🔴
نیازمند
🔴
تیکدری کنعانی زارع عیدی
🔴
پورعلی خدابنده‌لو
🔴
بیفوما محبی
🔴
سرگیف علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138844" target="_blank">📅 23:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138843">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🤝
🤝
🤝
کمالوند، سرمربی خیبر: ابوذر بازیکنی است که به کار پرسپولیس می‌آید
✔️
✔️
ابوذر صفرزاده از خریدهای خوب امسال ماست و من به باشگاه اعلام کردم تنها به شرطی که مانع جدایی او نخواهم شد که با پرسپولیس برای خرید یک بازیکن جدید به توافق برسیم.
✔️
✔️
ابوذر بازیکنی…</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/138843" target="_blank">📅 22:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138842">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
میثاقی: کمیته انضباطی شکایت مس شهربابک و نساجی مازندران رو رد میکنه و گفتن آسانی مشکل نداره و هرکسی اعتراض داره بره cas
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/138842" target="_blank">📅 22:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138841">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🤝
🤝
🤝
کمالوند، سرمربی خیبر: ابوذر بازیکنی است که به کار پرسپولیس می‌آید
✔️
✔️
ابوذر صفرزاده از خریدهای خوب امسال ماست و من به باشگاه اعلام کردم تنها به شرطی که مانع جدایی او نخواهم شد که با پرسپولیس برای خرید یک بازیکن جدید به توافق برسیم.
✔️
✔️
ابوذر بازیکنی…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/138841" target="_blank">📅 21:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138840">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X84y17eJu_g0v0XdKKSYXMeeCSbVGYem55Wi8TWtePhe5z3jzqEdu-14J2rs-WU5LKDkWgbd5Kpq28pbMq4Xss4SqxMx8ZRsU4aGClR8Uw4ufXpgSCKAwrXAGEejfqg_BD95nNm1AOcTee32r0yeMIvGbjGfhhfQg_vW33-6MEAnuIX98z_g1Ku6C84tFPSYz5NeigcVZS46NNzD54ssu_P2dkwiLJTiZ5fmt9cgJ7bg22d2ZGgTnDRo2Mz3wvhT1fQ-0OJWS7UP-b23PTrcPyKuI1WFL041tq6zAtV_Ndk7bs84I9QkE76SlCDxI5sd_k3hJAOVhALOREglSn3Ouw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام ترانسفرمارکت؛
علیرضا عنایت‌زاده به صورت قرضی به مس شهربابک پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/138840" target="_blank">📅 21:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138839">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHH4XM0r8yWZ5zDA5yROvynSizjDeH9d-pUtXhdBKc8fnMRTukWT3qY9iO8nolxcSUmr6SgSEs79MAJPUeFcgiyGGHCiZHOqXmrf2lQnXbp0eZgT6jem6f48xa4g-iB-mqa_uRtOkgtsTSiC9NoIYLK8Vj3pxcacg_UqP85RWg9p-wG3WD4sGeHXbYb0IQe7Eb2SATTyUi2RmdvbkiemZnLuUjnUVaz-CkOjEP6Dypogdxkm9wJLQoFHyVZEbmciQmMv7OhyWutATDOvSA797iBOgLsqVAmR5aaB81R-yZ9I0Pj4g-yIi3-ynTFlSK3yXLY8UXnr2kedlN8-HnXMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
نتایج بازی‌های امروز هفته 3 لیگ برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/138839" target="_blank">📅 21:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138838">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
❌
کیسه دو بر صفر از سپاهان جلوعه.....
❌
❌
سپاهان خیلیییی شخمیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/138838" target="_blank">📅 21:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138837">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
🔴
ترکیب احتمالی پرسپولیس مقابل تراکتور از دید فوتبالی:
🔴
نیازمند
🔴
تیکدری کنعانی زارع عیدی
🔴
پورعلی خدابنده‌لو
🔴
بیفوما محبی
🔴
سرگیف علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/138837" target="_blank">📅 21:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138836">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
✔️
✔️
۷۲ ساعت سرنوشت‌ساز برای پرسپولیس؛ تلاش برای جذب گزینه‌های نقل‌وانتقالاتی
✔️
✔️
در حالی که تنها ۷۲ ساعت تا پایان پنجره نقل‌وانتقالات تابستانی باقی مانده، باشگاه پرسپولیس تلاش می‌کند پرونده جذب گزینه‌های مدنظر خود را نهایی و ترکیب تیم خود را تکمیل کند.…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/138836" target="_blank">📅 21:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138835">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
حضور هیچ بازیکنی در ترکیب پرسپولیس تضمینی نیست و تارتار از روی عملکردشون در تمرینات ترکیب میچینه/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/138835" target="_blank">📅 21:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138834">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjGnYulqp3SPt3ftpcJnmDxZpSGZAOlinOq-2ZxP34-twPDjX4p9YAmhk6TT5INUZcXYvUmrFiLzfAdPYDathiqXd_LjtRGa2jS6V6WEtlNQEClWEBvFMQF2cjuSIVvN4UYofEYMp9DlnO-7EKLi_NCAa0CiF1pDskwAbaSq9tQrj0OlB3U74UMBE96_f7mfGCFvo_KeF0HfeUeMRJ-4bsHmQVDzxQgSU92zwHetjiHi7iXPwcCpHB_eN6pf4zcQxaFqX-FOjUFB-tkZrlAKIyq-PflBFroBj0cciOAoYffU9cF6s5NOFRYQ3qqjrJ_QiBDjag9DVtGKOmwIuY3TLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تنها فقط تا فرداشب فرصت برای بونوس ویژه بازی Scarab Temple باقی مانده!
🔵
کاربران اسپورت‌نود می‌توانند با هر بار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود ‌اسپین رایگان کازینو دریافت کنند.
🔵
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
📌
نسخه جدید سایت:
Sportn5b2.com
📌
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138834" target="_blank">📅 21:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138833">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🤝
🤝
🤝
کمالوند، سرمربی خیبر: ابوذر بازیکنی است که به کار پرسپولیس می‌آید
✔️
✔️
ابوذر صفرزاده از خریدهای خوب امسال ماست و من به باشگاه اعلام کردم تنها به شرطی که مانع جدایی او نخواهم شد که با پرسپولیس برای خرید یک بازیکن جدید به توافق برسیم.
✔️
✔️
ابوذر بازیکنی…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138833" target="_blank">📅 21:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138832">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
با اعلام فراز کمالوند سرمربی خیبر خرم آباد ابوذر صفرزاده به پرسپولیس خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/138832" target="_blank">📅 21:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138831">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
تارتار:
🗣
🗣
فیفادی که نیست‌؛ به تیم امید که هیچی به هیچکس بازیکن نمیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138831" target="_blank">📅 20:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138830">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
فوری؛ بیانیه کمیته انضباطی علیه استقلال تراکتور و گلگهر: ندادن بازیکن به تیم ملی در هر رده سنی به هر دلیلی تخلف حساب میشه و حضور بازیکنان حاضر در لیست در اردو ملزمه و هر تیمی سرپیچی کنه باهاش به شدت برخورد میشه و بازیکنان از حضور در لیگ برتر محروم میشن و…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138830" target="_blank">📅 20:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138829">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
نکونام:
❌
تارتار با گرفتن سهمیه آسیایی با گل‌گهر کار بزرگی کرد و حضورش روی نیمکت پرسپولیس هم نشون میده که واقعاً لیاقت این جایگاه رو داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/138829" target="_blank">📅 20:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138828">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
جواد نکونام؛ مهدی ترابی به دیدار حساس‌فردا باپرسپولیس رسید اما مهدی هاشم نژاد بدلیل مصدومیت این دیدار رو از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/138828" target="_blank">📅 20:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138827">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
✔️
وضعیت عمری امیدوارکننده شد
❌
❌
وضعیت محمد عمری که در دیدار مقابل استقلال خوزستان دچار مصدومیت شده بود، بهبود پیدا کرده و شرایط این بازیکن امیدوارکننده‌تر از روزهای گذشته است.
❌
❌
عمری امروز تست نهایی پزشکی را پشت سر خواهد گذاشت تا مشخص شود می‌تواند پرسپولیس…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138827" target="_blank">📅 20:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138826">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
❌
فوری از عطا حسینی فرد نزدیک به تراکتور:
✅
هاشم نژاد و ترابی به بازی پرسپولیس نخواهند رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138826" target="_blank">📅 20:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138825">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
حسینی قشنگ داره بازی و برای کیسه در میاره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138825" target="_blank">📅 20:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138824">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
سیدحسین حسینی: این توپ ها تازه به لیگ آمده و هنوز به این توپ‌ها عادت نکردم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138824" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138823">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
▶️
⚽
به گزارش رسانه «سرخ تایمز» جذب محمد قربانی به دلیل مخالفت باشگاه الوحده به انتقال او به باشگاه های ایرانی منتفی شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/138823" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138822">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
با اعلام فراز کمالوند سرمربی خیبر خرم آباد ابوذر صفرزاده به پرسپولیس خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/138822" target="_blank">📅 18:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138821">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس به دنبال جذب ابوذر صفرزاده مدافع چپ سابق تارتار در ملوان بندر انزلی/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138821" target="_blank">📅 18:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138820">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
فوری؛ بیانیه کمیته انضباطی علیه استقلال تراکتور و گلگهر: ندادن بازیکن به تیم ملی در هر رده سنی به هر دلیلی تخلف حساب میشه و حضور بازیکنان حاضر در لیست در اردو ملزمه و هر تیمی سرپیچی کنه باهاش به شدت برخورد میشه و بازیکنان از حضور در لیگ برتر محروم میشن و…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/138820" target="_blank">📅 18:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138819">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
❌
استقلال، تراکتور و پرسپولیس اعلام کردن قرار نیست بازیکن به تیم امید بدن! با این حساب ۱۰ ۱۲ تا بازیکن از این لیست خط میخوره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/138819" target="_blank">📅 18:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138818">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🤥
🤥
#شنیده ها
👀
مهدی تارتار قصد دارد در دیدار مقابل تراکتور از سیستم 3 دفاعه برای مهار شهریار مغانلو و حسین زاده استفاده کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138818" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138817">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
همه شواهد و مدارک حاکی از سرباز شدن علیرضا صفربیرانوند پس از بازی با پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/138817" target="_blank">📅 16:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138816">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
پرسپولیس تا پایان نقل و انتقالات ۲ بازیکن دیگه جذب میکنه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138816" target="_blank">📅 16:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138815">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azIVlsV1jXwNt_E_LCEC0RjDe38jgm3YG9ZUG1g0pO3KDqjJFX8YmcHNmfe7gvFkUaBRvn86TJoJpznxWZbRr7d3qAF8I3dJGIF-1p2KTMWkyKkE4k1C2DD7mYwFY6QGehXuyqQ_a97Oy9IaHoLzsFnrwYdXjbamYFpaOHJ_VV-sNrbqZhUdCt3_JOdOQA_HdPUFRVpmzZV5xhA7KkEIEGxwreBLozyU01fXhY3gb1iq4VuPx1WfHV70vMLZTvN5BcGbh_z81h9BlHtJCXKv0uwp11NeuCTSQbbxZF1Kh5rRNvgvgwUUut_uQHwHAhWeyO5oyJBFRk_TGAiIf4Wn4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
همه شواهد و مدارک حاکی از سرباز شدن علیرضا صفربیرانوند پس از بازی با پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138815" target="_blank">📅 14:55 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
