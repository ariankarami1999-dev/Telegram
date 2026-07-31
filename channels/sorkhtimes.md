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
<img src="https://cdn4.telesco.pe/file/kdBr0a4mn0Qr3QnbXnxLiieJiuxqAtWDam48omx6JtCRDw6lQHKpVd4WH-2hjvhOE7wAou4pvUymZTg6Oi5aZj-eWQrk_YD1aps_YlCmFNe2WJMEW3a2Q_cs_Uz1baqj3v1X0gkPmNfBCN0e6kdT8O35HHB2B9QMcW-i0uk5UpSjy0aRipYuMboonerhKXhUBTSR1CszKk8_Keyzfih_sHiXS5DVrFBLsmsX0z1LLJHC3XUthqsEa6J40vjQrri2CvcBRW5zMdVP2SAvV-R6DUTKOL_aPhRd9U9Y8hGno4JNUVfZEguUaOUSFp1pNE_Q6x_es35Mzii6mrbXfUo8JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 23:44:28</div>
<hr>

<div class="tg-post" id="msg-137118">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
باشگاه پرسپولیس خبر داد: امید عالیشاه با توافق دوجانبه از پرسپولیس جدا شد
❌
باشگاه ضمن قدرددانی از فسخ توافقی خبر داد و برای او و سرلک آرزوی موفقیت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 80 · <a href="https://t.me/SorkhTimes/137118" target="_blank">📅 23:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137117">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
❌
براساس قانون جدید سازمان لیگ مبنی بر اینکه تیم های حاضر در لیگ فقط 4 سهمیه خارجی میتونن داشته باشن پرسپولیس در حال حاضر 5 بازیکن خارجی فعال در تیم داره باید با یکی شون خداحافظی کنه که قانون جدید سازمان لیگ اجرا بشه
✅
دنیل گرا
✅
مارکو باکیچ
✅
تیوی بیفوما…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SorkhTimes/137117" target="_blank">📅 23:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137116">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚫️
⚫️
فرهیختگان :تارتار هیچ نظری روی دنیل گرا نداره و گفته باید جدا بشه ولی محسن خلیلی مانع جدایی دنیل گرا هستش تا این لحظه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/137116" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137115">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔄
🔄
دربی افتاد هفته پنجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/137115" target="_blank">📅 22:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137114">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
شایعات؛ رامین رضاییان تمایل داره به پرسپولیس بیاد و تارتار هم بهش علاقه منده!  نظرات؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/137114" target="_blank">📅 21:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137113">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
اورونوف که به عنوان بازیکن تعویضی به زمین اومده بود با دریبل دو نفر پاس گل را به علیپور داد تا او دروازه خالی را باز کند و به عنوان گلزن بازی لقب بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/137113" target="_blank">📅 21:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🗣
🗣
🗣
شنیده ها حاکی از آن است که دنیل گرا ، تیوی بیفوما و حسین ابرقویی بعد از اردوی ترکیه در لیست مازاد تارتار قرار خواهند گرفت مگر اینکه در ترکیه اتفاقی دیگری رخ دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/137112" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
فووووووووری از قدوسی
✅
✅
منتظر یه خرید خوب باشید......
⚡️
⚡️
این همون خریدی هستش که خلیلی ازش حرف زد و گفت داره قطعی میشه و هوادار پسنده.....نامش آشناست......
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/137111" target="_blank">📅 21:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚡️
⚡️
فوری/ دونالد ترامپ: در پاسخ به حملاتی که سپاه پاسداران به اردن کرده، ما ایران را به شدت مورد حمله قرار خواهیم داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/137110" target="_blank">📅 21:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
❌
فرهیختگان: همایی فر عملکرد خیلی خوبی جلو آلانیا داشته ولی تارتار همچنان خواهان رزاق پور هستش.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/137109" target="_blank">📅 21:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
✔️
علیرضا همایی‌فر دفاع چپ ۲۰ ساله آکادمی پرسپولیس تو هر دو بازی دوستانه مقابل پیرامیدز و آلانیااسپور فیکس بود و تو بازی امروز هم ۹۰ دقیقه کامل به میدان رفت
✔️
✔️
با مصدومیت جلالی و جدایی محمدی همایی‌فر فرصت بازی پیدا کرد و میتونه پدیده این فصل پرسپولیسی‌ها…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/137108" target="_blank">📅 21:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lo_gWSzieBSRKlMegP5ZDbwvJmTuY-_cF4IqZS7DcPnGvoMuMP9u7EQ7E-eTKdvQYBfBc4Pv70KfiR9YwH8nlxIovp0mE2iUWkFW6SecyJFOF7dfEZ0clMyhWqfSZUpNx8GFXz9DQAjzN85MZuqEM_bKCKUeBldViRNXeJYV-Ie090QErZE6HsO19itaWKRhBhsm0wbG8ccgq4ru5oHgL1uhx2IeUsgi4eBj_n4opY4pQykTBvArco2G6HeTvnxZHww3ll7GVovRV6ehEkHHUC3MFgyLHcssJ1HAIe9bx_p8JmHE1p4PzJSWFXs7YPd9PQAZ-PeG88JtDh963SoMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎾
نبرد نسل‌ها؛ جودار جوان در برابر تجربه و کلاس موستی، جودار در آزمونی سخت در مقابل موستی!
🎾
رقابت رافائل جودار
🇪🇸
-
🇮🇹
لورنزو موستی رو با آپشن‌های مختلف و بدون خارج شدن از تلگرام همراه با
ربات اسپورت‌نود
پیش‌بینی کنید.
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
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/137107" target="_blank">📅 20:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EA7BQVpHTAOUjW-Qf6ZaWjLFU2Dc5zBOmX1sWKBSL8sT-Nr6AqKPfnP5r9NI1WcxtBbmtRPrcIYmJV84Pgb_Gz2vgI272VyF-_asQFSChHkZFAmLnmm4l-Asu1eLZIxxrxvPZFyZISHxhSX8tEDRewCmo8EWuJg5wEhVSo8OpZnr7CW0Jml6rVXYAQv2zRE6kFk8999XxIFN8WvSGJ3o6CZqsO0XAKekTfTghXyXU9fzuTMXBOijtzXCqRlsXphquWKENpaE9iKaa4z9UJEDjy19lb00bSorQxUYv15YRhmaQgbLEOjWTH2B9ZMCspMn6iuOTsPpZyOoq4CKX6uV1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
بازیکن آزاد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/137106" target="_blank">📅 18:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-ji6VjacDvrAYBLeC04-YpkW89f7cGkpofN15NL6iK4TiOpYu5woOtc6KiKDl_g1QZ8BdMlNfthwe5f3GfIeBg0KtNoy7qxq-fswHXwV67G0WY-yQ2OVLAvV9_Nj7TGWKTxafWT613KE386xtsWB3r53OC48wLXPmq43U4eqHLPMAA0Lw5c-E314aVtQXHKDteYOjJ9rcX-daLtkzH3k1aJiMh6EhwbA_gSZCjwup2fxhV3IAMwxj1fsAaBa59dwafQV71FXL8qcn9BniZVV4q6P93KOhhHiKazYO_W-XQZ6dhZbBtrErdr5I0dSqFR58KJvrN2P9m8v2tXO63hsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌀
🌀
آمادگی بدنی فوق العاده پوریا شهرآبادی
🤌
🔥
⚠️
پ.ن عضلات پارو ببین فقط
😳
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/137105" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
15 روز تا اولین بازی پرسپولیس ورژن تارتار در لیگ برتر مونده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/137104" target="_blank">📅 17:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4YSnRQB9_lgL8jNsXs4OfYGsuflv1U23UiqBA8vUx4OuMPtuouvALzaX_mKjwE0yJb6DnI0F4VX7xMlbYCaK_jHl5YVEe4qMVhQpYlzENq9wuwrhwYApawmBHvQoO7ZapEvIUZbB8aiA5xN8fzHdcIoyceK--7jFwghSHb3o0JV-wEzT9a8kYAcJ0Om6IuMxG1asKvNqtzk8sb3dsS0snjwwKgHcibUFw0MFAzZxqTjBH3bYfqTVWSN7iwL2OtuzlkyerqsjdZZfr4WlB6eD3wNbj-aXx4G_effph6V4iuLSUYTw3uWTYGK_TomwYHcPm51wrL9VdCZf77eNgLWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
👤
ایسنا: سامان قدوس در لیست نقل و انتقالات پرسپولیس حضور دارد و گزینه جانشینی رضا شکاری محسوب میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/137103" target="_blank">📅 17:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUtk0drIB_FQD5b6KqH4JZWofHgAxkGCxj0fFnmrl_7VKXbtdRiL6FHu3WpgohzrZ8EWNoeYOy4kVhX-DgqjHCkmPDgQxsuk88FIA61fDgaNNmrIJcmv5tGIh96CtZTtEy_3oiJXlp-2DH774tDu55wae5Um7cEt4mIIMoDWlKFEAhWmtiGS6_lt1EQaJ-gMmtThoEEfqbqG6Fa6wXwg_MCw3kloyWh-A0umuljxxoC9lDjogjO4QV0XGkpmekIqxpN3df8_EPBzBpxArQuZJWWRKb_oDwjoVjJiEiBABR8P6FGVEDNVJdgYpSEMBbm2aG0HwTtROPAPPeGRP1S77g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
تمرینی با انگیزه‌ای مضاعف سرخپوشان در اردوی ارزروم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/137102" target="_blank">📅 17:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137101">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP0f6LJAsuI4JcyoUfTZVUoW6lJAAvRhBG7tyuDYq6z_qJRu2dkCOdccEhv6I2ry6BjPKAHWkIMm_F3SJgfVudGxoHyVyG54w9GWY4SSK5lDFs4O7-AKdFkbyDEUEXe1CNDMc0veMsua_ScaUQdsDt9211cen2fA4EMeKiz6aqdikTaj473YsN6ms18ZRQLV0MsRkcy_jmsQ8L0N0fG8nkQ5W7_USbUulkMbqfHbRfUpbx2HWMe-K3hQQPhozlYqEnDb9d8SKT2QjcAG8nsNPftqyUl01Axv0QKS-axJ-GEyXoYZQz3-gwHkjFzZvqGYmQqvHHXEcEZq6umVTmAIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
❤️
امیررضا رفیعی به اردوی پرسپولیس در ترکیه اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/137101" target="_blank">📅 17:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137100">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
تارتار نه از جلالی و نه از عیدی راضی نیست و دفاع چپ و راست میخواد
☹️
☹️
☹️
///فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/137100" target="_blank">📅 16:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
ترافیک مهاجمان در پرسپولیس؛ سرگیف مهاجم اول تارتار
❌
پرسپولیس برای فصل پیش رو به نظر ترافیک زیادی در خط حمله خود خواهد داشت در حالی که فصل پیش در این پست با کمبود بازیکن مواجه بود تا در نهایت ایگور سرگیف در نیم فصل سرخپوش شد.
❌
هم اکنون علی علیپور، پوریا…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/137099" target="_blank">📅 16:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137098">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tc0HQjekUXOLDjCnp36JhbGPOmsVUEKkwiqMwsRHCZFs3iiDvbrONM9AcI5XD8XUH3Co2kKLGDJKQQvwctpUm7PjEtssBFmJ_iBCDEBBIJTyYs2NQ40qy8L6FJGRSkv1us8tTn4X4V00gD2vZsxd2RIxXkMVBDAIK19XdcPkvjx_whPeuCqREG4TA9aVUZwyzapv0NcE7VsQkPWrmhqgAXqEZ5-1CON9bxZx5Y4cIeuK8XYvV6DugSISiq3Oi1Ci8LNzfR7QKF6OiCBNhHyk4k6czKETAu7J3lb3PGJzqjGx-5J1J-8XNNqaXKAG6PZWYboqJ0JYCh8xOWG7U2Je8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽
👀
‼️
محمد عمری ۵ فصل پرسپولیس بوده ۴ تا شماره پیراهن عوض کرده!
۸۰ ، ۷۷ ، ۲۱ ، ۷
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/137098" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137097">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
شایعات؛ رامین رضاییان تمایل داره به پرسپولیس بیاد و تارتار هم بهش علاقه منده!  نظرات؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137097" target="_blank">📅 14:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137096">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
❌
❌
#فوووووووووری   |#ادعای_روزنامه_هفت_صبح
❌
مبلغ رضایت‌نامه محمدجواد حسین‌نژاد، ستاره دینامو ماخاچ‌قلعه، به ۲ میلیون دلار کاهش پیدا کرده است.
🔄
هر دو باشگاه پرسپولیس و استقلال برای جذب این هافبک ملی‌پوش وارد عمل شده‌اند و رقابت برای جذب او همچنان ادامه…</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137096" target="_blank">📅 14:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137095">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
رکوردداران حضور در دربی به عنوان سرمربی
▫️
علی پروین: 25
▫️
منصور پورحیدری: 18
▫️
زدراکو رایکوف: 15
▫️
امیر قلعه‌نویی: 14
▫️
یحیی گل‌محمدی: 11
▫️
پرویز مظلومی: 8
▫️
برانکو ایوانکوویچ: 8
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137095" target="_blank">📅 14:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137094">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=vrzcuD3UkT4aaO4fBTzRBrY_IKxcjI0_bNeblunZ29BKfH6Kezv6LRbOX3erBkdbcczqVW5cgqGi09pY7qAHW-T2R-Dw9EqgFpO18BDnCBtsPaJo9N6MfS28yny7BpgOmNkU5xbpGeMcdexdHauQRNdDYin7WwJPW6twJ7HAO0lK9MIvBP-OTWZBVi8FOFN6PK7UC_sVmyeqwo1lPLnVqTMfp54sm4-422CCh8inO_KqQSf8AXlpOfEhPFFp4GAwR-TNGsqngd_SXxRHo1k3I1M8CTP--IN7i63TivOFNX9catNB627XrtIqJF8wjIuKq4UiZkXyhP5RxtmyMsBYFDyI-2d2NFA3MwpC1Q83G8xMeMiJak8z5BxUM0vz9GRBwxULZ6EsYdzEhy29swUut85gSqwiTkWHaIbku6SYCqL0sp8KZX3WbwEViAkYnNKLh67-GerVszuO0E_RteglCNGqjwwDZCIGcBEfvqSFWDf8oDTXJg8KxwNnpOnR_bCoC1VCYfFjBbbGIqn6JuA88wAYszpnh207-lLiBGHxvKoy3kSqO-T8R1DvtBK_PYxM3sOHiYjGszLQeg-p10CU5zp3m_4_y4NuLLOusAyNjVaURd3SUI-4PBnXco6gIyxxTxwdI8apQgkwXOBRfqrNaJFCTkBYusMwsAyp6Jw8sHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=vrzcuD3UkT4aaO4fBTzRBrY_IKxcjI0_bNeblunZ29BKfH6Kezv6LRbOX3erBkdbcczqVW5cgqGi09pY7qAHW-T2R-Dw9EqgFpO18BDnCBtsPaJo9N6MfS28yny7BpgOmNkU5xbpGeMcdexdHauQRNdDYin7WwJPW6twJ7HAO0lK9MIvBP-OTWZBVi8FOFN6PK7UC_sVmyeqwo1lPLnVqTMfp54sm4-422CCh8inO_KqQSf8AXlpOfEhPFFp4GAwR-TNGsqngd_SXxRHo1k3I1M8CTP--IN7i63TivOFNX9catNB627XrtIqJF8wjIuKq4UiZkXyhP5RxtmyMsBYFDyI-2d2NFA3MwpC1Q83G8xMeMiJak8z5BxUM0vz9GRBwxULZ6EsYdzEhy29swUut85gSqwiTkWHaIbku6SYCqL0sp8KZX3WbwEViAkYnNKLh67-GerVszuO0E_RteglCNGqjwwDZCIGcBEfvqSFWDf8oDTXJg8KxwNnpOnR_bCoC1VCYfFjBbbGIqn6JuA88wAYszpnh207-lLiBGHxvKoy3kSqO-T8R1DvtBK_PYxM3sOHiYjGszLQeg-p10CU5zp3m_4_y4NuLLOusAyNjVaURd3SUI-4PBnXco6gIyxxTxwdI8apQgkwXOBRfqrNaJFCTkBYusMwsAyp6Jw8sHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
تجربه‌ای متفاوت از هنر روپایی و تصمیم‌گیری با Crash Kick؛ جاییکه مهارت با هیجان گره می‌خورد!
⚽️
در کراش کیک، هر روپایی موفق ضریب برد را افزایش می‌دهد و هر لحظه وسوسه ادامه دادن بیشتر می‌شود. هنر اصلی بازی، انتخاب بهترین زمان برای برداشت جایزه قبل از پایان روند صعودی است. این بازی با ترکیب هیجان، تصمیم‌گیری لحظه‌ای و مدیریت ریسک، تجربه‌ای متفاوت و نفس‌گیر را برای علاقه‌مندان به بازی‌های سریع و پرهیجان رقم می‌زند.
✅
جسارت ادامه دادن یا هوشمندی در برداشت؟ تصمیم تو، سرنوشت جایزه را مشخص می‌کند.
📌
همین حالا وارد ربات وینکوبت شو و هیجان واقعی رو لمس کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137094" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137093">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
دکتر عزیزی دست به کار شد
🔴
خداداد : میخوایم حسین نژاد رو بیاریم ایران!  پ.ن مبلغ فسخ و شنیدن شاخ درآوردن
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137093" target="_blank">📅 13:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137092">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
✔️
طبق شنیده‌ ها؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ علاقمندسنگالی به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137092" target="_blank">📅 13:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137091">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
فوووووووری از ورزش سه
🔴
خبر شرکت هلیلیویچ در تمرینات پرسپولیس شایعه ست و مدیران باشگاه این خبر رو تایید نکردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137091" target="_blank">📅 13:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137090">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
✔️
طبق شنیده‌ ها؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ علاقمندسنگالی به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137090" target="_blank">📅 11:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137089">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔻
🔻
🔻
علوی سخنگوی فدراسیون فوتبال: با جزئیات مقصر اشتباهات معرفی سهیمه سوم ایران به آسیا را به زودی اعلام می کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137089" target="_blank">📅 11:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137088">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🫥
🫥
علوی سخنگوی فدراسیون فوتبال: برگزاری لیگ برتر بدون حضور تماشاگران؟ این موضوع در جلسات در حال بررسی است ولی لیگ با تماشاگر قشنگ است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/137088" target="_blank">📅 11:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137087">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
✅
✅
بابایی مدیرعامل چادرملو:فدراسیون فوتبال باید خسارت سنگین به باشگاه چادرملو پرداخت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/137087" target="_blank">📅 11:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137086">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
علیرضا بابایی، مدیرعامل باشگاه چادرملو: متاسفانه طبق آخرین شنیده‌ها برخلاف پیش‌بینی‌های قبلی، کنفدراسیون فوتبال آسیا با درخواست فدراسیون ایران برای جابجایی نام چادرملو با گل گهر مخالفت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/137086" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137085">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
#شایعات
‼️
3 هفته اول لیگ بدون تماشاگر برگزار می‌شود!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137085" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137084">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
✔️
گزینه خارجی جدید مهدی تارتار؛ پرسپولیس سراغ مدافع شاغل در روسیه رفت
❌
❌
باشگاه پرسپولیس مذاکرات اولیه برای جذب عثمان اندونگ، مدافع ۲۶ ساله باشگاه اخمت گروژنی روسیه را آغاز کرده است، اندونگ دو سال پیش تحت نظر تارتار در گل گهر خوش درخشیده بود
❌
❌
گفته می‌شود…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137084" target="_blank">📅 11:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137083">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137083" target="_blank">📅 10:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137082">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
❗️
حمید استیلی: هیچ جوری نمی‌تونید علی دایی رو حذف کنید
💢
برای چی باید درباره گرانی‌ها و وضعیت اقتصادی ایران سکوت کنیم؟
💢
مگر می‌شه سردار آزمون رو به همین راحتی کنار بذارید؟
💢
بین مردم و بازیکن‌های تیم ملی فاصله افتاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137082" target="_blank">📅 10:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137081">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
❌
حضور مسعود محبی در روسیه منتفی شد/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/137081" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137080">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfF_7RsP8jAceDenufpyvTjU3aDpexwV-9msoU_Sejn3jeWjC3MZNALhS6sZzKYXtaUvHbEXtOON9KEux09fff3q-CC8EbDRirHRfQliwioH8PYXyT0SlTFN8SaNR5eA7sHf_T4xgmVcCi-PXaR05XG6CJjAJtVHHraAIKQfnLr0LDtex1abNw09jsq8wI46Ps0F_ePnDN7Bevt0U7DU1GL-fLU4n9cJD9skn32syj6crPUb2nSjR5v9vNza85T-YB8j1OjRXJFU9J2IMR7dZSCl_5VXGST31HuWKD8gFoxHuIRwJ5ZdvAcab4fTebT0d_4Zjnh2Jx-o6tDKbI5Hew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🧤
عملکرد نیازمند در دیدارهای دوستانه پیش‌فصل:
۴ بازی: ۴ کلین‌شیت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137080" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137079">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFk1kVCIFPQVkQz2x1MRjAJyxdw6XZXFhzn74bJPF8esJZYSbdVGIYVHHL8m9i30TbTqDsx8QPKM_Q8nh02R5LlrtP8XHNb6DT8QoscjVrxsWf0NHUEXYuSqEfaGicVaFtddFYpufZaaq3q3VpUWhe9tr8fhsdmUnAc9mFj-389d4cqRPBPy9DZkkVlIWUM82BQjAhu08XypTxRRQputjWelh7dY32ftV4yzy_AzT-Pq8PVTI2zuZfNj3zwo1UWYcBr3UHDxkZlNcRa18myYbNHafIJXQknOYxaq-E16wP6_HZm4EUiiP-ha38lL0l2dG7FsSXvdyL8xFX70JuWUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137079" target="_blank">📅 10:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137078">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c21rkm5o5flq8ESk95yOVJxfyjsIxCXBHL5maZHdW8FtDis_6wmb0aT3UkOXjBkX215xPAa6pIcvoeYQzIVUMxPETD46CopNzRrzLTqdJ5Q2xBTxFfVTogbTrOcZbhjxxF89SuPBIUvED4PyyI7L7B6slctZzaa7KJO4bS1eZMdiEkY4O3Py5HNy3DjJA4X04gdtIE2Pd24RHaaAloIZtZLKUTQo1I_QtXmWC8ar20fSvBnRciHBew01463_dMrnwZyi_FIZkhVJBLZP9T7iJYOTDyS7jEAkRobw9nRaUbUl1CSEZW53P77GH0kJKKKBQkVP30UMRerGUW3DhTjozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
تقابل استعداد نوظهور اسپانیا با ستاره باتجربه ایتالیا؛ آزمونی بزرگ برای جودار!
🎾
Jodar -
🎾
Musetti
🎾
دیدار رافائل جودار و لورنزو موزتی، تقابل استعداد جوان با تجربه و کلاس بالای تنیس است. جودار با انرژی بالا و بازی هجومی به دنبال خلق شگفتی خواهد بود، اما موزتی با تنوع تاکتیکی، ضربات بک‌هند کم‌نظیر و تجربه بیشتر در مسابقات سطح بالا، روی کاغذ شانس بیشتری برای پیروزی دارد. اگر جودار بتواند فشار سرویس و ریتم بازی را حفظ کند، این مسابقه می‌تواند به یکی از جذاب‌ترین دیدارهای این مرحله تبدیل شود.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/137078" target="_blank">📅 02:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137077">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
فووووووووری از قدوسی
✅
✅
منتظر یه خرید خوب باشید......
⚡️
⚡️
این همون خریدی هستش که خلیلی ازش حرف زد و گفت داره قطعی میشه و هوادار پسنده.....نامش آشناست......
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/137077" target="_blank">📅 01:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137076">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
هالیلوویچ؟منتظر یک خرید خوب باشید.
🔴
🔴
الن هالیلیوویج در تمرین و اردوی پرسپولیس حضور نداشته و اخبار تمرین کردنش با تیم صحت ندارد
🔴
🔴
ایجنت او با مسوولان باشگاه صحبت هایی از مدتها قبل داشته و احتمالا در تست فنی شرکت خواهد کرد
🔴
🔴
هالیلوویچ به عنوان گزینه خرید…</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/SorkhTimes/137076" target="_blank">📅 00:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137075">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
هالیلوویچ؟منتظر یک خرید خوب باشید.
🔴
🔴
الن هالیلیوویج در تمرین و اردوی پرسپولیس حضور نداشته و اخبار تمرین کردنش با تیم صحت ندارد
🔴
🔴
ایجنت او با مسوولان باشگاه صحبت هایی از مدتها قبل داشته و احتمالا در تست فنی شرکت خواهد کرد
🔴
🔴
هالیلوویچ به عنوان گزینه خرید…</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/SorkhTimes/137075" target="_blank">📅 00:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137074">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
مرصاد سیفی و امیر جعفری دو گزینه نهایی تارتار برای حضور در دفاع چپ پرسپولیس هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/137074" target="_blank">📅 00:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137073">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
هالیلوویچ؟منتظر یک خرید خوب باشید.
🔴
🔴
الن هالیلیوویج در تمرین و اردوی پرسپولیس حضور نداشته و اخبار تمرین کردنش با تیم صحت ندارد
🔴
🔴
ایجنت او با مسوولان باشگاه صحبت هایی از مدتها قبل داشته و احتمالا در تست فنی شرکت خواهد کرد
🔴
🔴
هالیلوویچ به عنوان گزینه خرید…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137073" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137072">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌀
🌀
🌀
اظهارات کنایه‌آمیز محسن خلیلی: تیم‌های دیگر هم دلسوز بازیکن گرفتن پرسپولیس هستن. برای جذب هر بازیکن تیم حقوقی ما بررسی می‌کنه تا محروم نشیم.
📎
📎
📎
خبرهای خوبی درباره انتقال یک بازیکن می‌رسه.
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/137072" target="_blank">📅 00:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137071">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
تک گل پرسپولیس در دیدار دوستانه مقابل آلانیا اسپور
✔️
جادوی ارونوف و امضای علیپور؛ یک پایان بی‌نقص، حاصل نبوغ فردی اوستون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137071" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137070">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
#فووووری   #شایعات
✔️
✔️
گفته میشه یک مدافع چپ جوان خارجی در اردوی پرسپولیس حاضر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137070" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137069">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
❌
آلن هلیلوویچ به تمرینات تیم در ترکیه اضافه شده و قراره بصورت بازیکن تستی تست بده و اگه اوکی باشه باهاش قرارداد ببندن
🖍
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137069" target="_blank">📅 00:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137068">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⚠️
⚠️
عادل فردوسی‌پور با این ویدیو از خودش دفاع کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137068" target="_blank">📅 23:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137067">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2a693019.mp4?token=guXH8yRq6gwsx5tcU0ILHhFNkSSdvB6ea1epMKola2Vp2ZekAD_7LkPc1--EUURiYiR7ErnrY0cATvEmXS88q_Vj0ap74-8-vEV0YTX_cHBwoqNxlZZ2ps3FEoeFaSO3ZcFfan_sMQj1weOYt2zBt0imKagNwm0TL1YhciXMiyCNOrRxtqfaYFoN0hoHIMk0gdVj4oWn6JJbowlQhJughG_gSqKQYSTWhEUlZeV43HNAoZdEAwKdNb4ym3imA0ee27iPy5dIfM8-7Nxs4pWt5nSZNxNj_cuN-o_fVkL3idFHoiZGUPL4PhtLcwrqv-VJpU8LAI_UuyLwW76E4v7WMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2a693019.mp4?token=guXH8yRq6gwsx5tcU0ILHhFNkSSdvB6ea1epMKola2Vp2ZekAD_7LkPc1--EUURiYiR7ErnrY0cATvEmXS88q_Vj0ap74-8-vEV0YTX_cHBwoqNxlZZ2ps3FEoeFaSO3ZcFfan_sMQj1weOYt2zBt0imKagNwm0TL1YhciXMiyCNOrRxtqfaYFoN0hoHIMk0gdVj4oWn6JJbowlQhJughG_gSqKQYSTWhEUlZeV43HNAoZdEAwKdNb4ym3imA0ee27iPy5dIfM8-7Nxs4pWt5nSZNxNj_cuN-o_fVkL3idFHoiZGUPL4PhtLcwrqv-VJpU8LAI_UuyLwW76E4v7WMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
تک گل پرسپولیس در دیدار دوستانه مقابل آلانیا اسپور
✔️
جادوی ارونوف و امضای علیپور؛ یک پایان بی‌نقص، حاصل نبوغ فردی اوستون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/137067" target="_blank">📅 23:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137066">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
گفته می شود ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137066" target="_blank">📅 23:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137065">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚠️
⚠️
بندرعباس بوشهر قشم کیش آبادان و اهواز بامداد امروز شدیدا مورد حمله قرار گرفتن و گزارشات انفجار تو این چند شهر بسیار مهیب بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137065" target="_blank">📅 23:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137064">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
🔴
🔴
درخشش علیرضا همایی‌فر در دیدار دوستانه؛ پرسشی جدی درباره روند استفاده از این بازیکن در پرسپولیس
⚽️
علیرضا همایی‌فر، بازیکن جوان پرسپولیس، در دیدار دوستانه روز گذشته تیم خود، عملکردی قابل‌توجه و امیدوارکننده از خود به جای گذاشت. همایی‌فر که توسط مدیریت سابق…</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137064" target="_blank">📅 23:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137063">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geH1fjg0sw3GNaEpDSUqCqzhK8wut3f5opvXXHr_zcgXgpiUVXxy2jWbC3BqBBRHk-9yB3QVSoTIt8HO1tR7pbXGT_R1Ra_7GjF_cVNGzrUo70pVbh-Xo_eCMnHLX7sbHfNJ9YO2zJwq0-oeFNRaAXkr-WGMHMIU5N0YHSlIhZVoTsc5lThEeb84VeLI63w-L8DOd6b-jOpEv2Uoux9LG7CP8iYEQWLHBs84YyH7wmMWGJlE4RvsdXo1OFnKQY5tlUsttkrUMF1w9bZqkb59T0seO6DFVZMwrGM4aBj82VBdaPZYv4nGXqxIHE9EdKuc6gBER1lWpLYF2i3mOev0cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس تندیس عالیشاه، سرلک و پورعلی‌گنجی رو ساخته تا در مراسمی ازشون تقدیر کنه
فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137063" target="_blank">📅 23:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137062">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
❌
عملکرد تارتار در بازی های دوستانه
⚡️
۴ بازی
⚡️
4کلین شیت
⚡️
4برد
⚡️
7گل زده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/137062" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137061">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOvQ2pYPpI1Od9vsgowJzP0FwLe58qSGf0_AXUT3tE5sMv4-OO92P--gIyPfGa1_5xQs9nVlC4asZCuZlc8h-JJp2yDEiaXkG0fP2ULXOKK7dsAOQzUGKScFeUNN_8HHPMDMbi8POdteb_79JCfEvW9BQDsK1jMDi1lgXYslpFQN0LB-va6hwjiomi-Z3KrZjlMA5JyWAwdOXoGCQze8FN3_SQFo45lXONmTQYpZHxPTiCNSC6Hbfw0efNTVxvw1RzjXZdTvgWOsCCWr5h4dTLXDLlq2yHYnXy_8PQ-ajmpRxj8E3TBTx1jh_vJZHCkX80OcNceYQaaNChfU5xvxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شایعات؛ رامین رضاییان تمایل داره به پرسپولیس بیاد و تارتار هم بهش علاقه منده!
نظرات؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/SorkhTimes/137061" target="_blank">📅 21:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137060">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0Q0y8d3qzviDXQ77l4YOF_thCnZLmoGPvcd9bqRhsj6dHyZP2OLBPzInsA-YZL3XHTcIChdJAH7CieMfbFanbwPUqwi9HeuwCxjLcHRsFwseEkF9WqQ6FIALklSxaCnjI97FYrmHICqY7LmVM6bX4-CMxbO-tt5kc0-VT5C0nICao79Ysjl7ARPvG21YW-i1sPgxpZNlnnQ0eBrLGsqQL5ZLjozYGdWPVhsIOdbDCHxjXYQE9-9vAGlHaAIlcrca8InWkGlPYULcqjN_UpcvVOOv1VyT0k85iUYoqA5iUiHHeFNxjRl-nhAHknpML84cvvy2MQNMlhCfpiWm68iKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/137060" target="_blank">📅 20:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137059">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗️
❗️
عیسی آل کثیر یه ویدیو از زمان حضورش تو پرسپولیس استوری کرده، پروفایلشم به عکس پرسپولیس برگردونده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137059" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137058">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiOoAvRT6n8c2cgu63Bamt2bxq_mSac2c4el0Yo3vEpBiZeDNX8RGn78BUk-DSZayxx-F-2sYambNqGX43cJs_D3JjPibNcqYuN2I2hoxeBchMaZFaAoMksX-mra8uAFHYisuuiGTTgfhyz8YlsowNGTJiGWQjN_dCRM08Q9IUkwylQYg1TLn5463WJnrENW-8CVRwLfouFWSMj0EWJvc9vaKAgrjxx_hWrOfdNaCKUUgvWMj3UIKx13BnGNwI373DG6el1wBXkWPhdp_afOcXJbYmYlam9coImaLBYas4G8mEcVPaiFTBw2iRU8lsudQx76viD9NunfTTxYSMGI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی پرسپولیس برابر آلانیا اسپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/137058" target="_blank">📅 20:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137057">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚡️
پرسپولیس به مانند بازی قبلی در دقیقه نود به گل رسید و بردهای یک بر صفر تارتار در دقیقه نود ادامه داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137057" target="_blank">📅 20:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137056">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
🔴
🔴
توجه | مدارس و دانشگاه های استان تهران غیرحضوری شد
⬛️
استاندار تهران:
⬛️
با تصمیم کارگروه اضطرار آلودگی هوا تمامی مقاطع تحصیلی استان تهران بجز فیروز کوه روزهای سه شنبه ۴ آذر و چهارشنبه ۵ آذر غیر حضوری اعلام شد.
🟦
دانشگاههای استان تهران بجز فیروز کوه غیر…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137056" target="_blank">📅 20:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137055">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShVOOGzjIzEfS20_DXH5UdVD9lC6kfmjhBYPnBJDcoQsPRfilCIJroXMLnLos0ZLMY4unpF1qCXQL1-lYKMsB25XL5WilTxgnmJibU9LEKO3-XoiIUt6OEPvlA1_2AQMx0v_y74gVcPq2LupVkcFzWjU-57_VeWNFtJ6aJAEOM7Y_F35hc51j6AJH5iMyYUr4pu_psv6kP3Aseea_Ji_6A6_SNlVKGdHWKe0NkaSQQRvRDmYGNYBOjIOrFOp2mSMN7eqH7mCnxsvsn4qFMHNqkvIW0K97wwKPXwzkHx32QA9QgVxxbtiJG1YHyRKllDPEcoG1FI4ZttZQVZ_vKpuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
برنامه بازی‌های مقدماتی لیگ اروپا
⚽️
امشب لیگ اروپا بار دیگر با تقابل‌های حساس و تماشایی، فوتبال‌دوستان را پای گیرنده‌ها می‌نشاند. تیم‌ها برای صعود و نزدیک شدن به مراحل بالاتر، با تمام توان به میدان می‌آیند و همین موضوع نوید مسابقاتی پرهیجان و غیرقابل پیش‌بینی را می‌دهد. شبی پر از رقابت، گل، هیجان و لحظاتی که می‌تواند سرنوشت فصل بسیاری از تیم‌ها را تغییر دهد.
⚽️
بازی‌های امشب رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137055" target="_blank">📅 20:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137054">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚡️
پرسپولیس به مانند بازی قبلی در دقیقه نود به گل رسید و بردهای یک بر صفر تارتار در دقیقه نود ادامه داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137054" target="_blank">📅 20:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137053">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔄
🔄
🔄
جونم تیم ..پرسپولیس دقیقه نود گل اول و برتری و زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137053" target="_blank">📅 19:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137052">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⚡️
نیمه اول دیدار دوستانه پرسپولیس و آلانیااسپور بدون گل به پایان رسید.  در حاشیه این بازی، محمد عمری و اورونوف در کنار محمدمهدی محبی روی نیمکت و زیر باران نشستند تا یک قاب جالب و متفاوت در ارزروم ثبت شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137052" target="_blank">📅 19:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137051">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
آلن هالیلوویچ فردا در تمرینات پرسپولیس شرکت میکند.
🔄
مهدی طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137051" target="_blank">📅 19:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137050">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚡️
⚡️
تایید شد
🔻
🔻
آلن هالیلوویچ، بازیکن کروات با اصرار محسن خلیلی به ترکیه سفر کرده تا به صورت تستی در تمرینات پرسپولیس حضور پیدا کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137050" target="_blank">📅 19:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137049">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚡️
⚡️
فرهیختگان: مذاکرات تراکتورسازی با الوحده بر سر قربانی به بن بست خورد ؛ چرا که زنوزی دنیال تخفیف هستش و قربانیم حقوق بالایی طلب کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137049" target="_blank">📅 19:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137048">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt0jio-kERChrh74waV7bTigvTYv74YYo7YgSV3CvsUFN6vroo4ceb1GpNzKwo____5qFQSoKlInxBmS0dPhVxCkdeuOHG55Wsy6WD8x9PhGZp2G0QZpU32Hli_C_HtxlU8cM33NK6Xiy1ZdofaMZ_G3DCCFBf8VzqsaLr3B6bvyQ5LZgEcZPQ0t-tuFpn27Abcr-q1fdj-m1gAfGs5n_nUelFPiF9GswiuGvTqqY1kHbtHeC1Rj8VwtpuxE_QCVNd-Qjfm6er6eBUcJrRWb8tKwcHPjaqhGfGWfJagYVzcUVH9kET2bwz7dfVHZ5vfZ4pQYQnOD7ZuVanZ_b0xc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
نیمه اول دیدار دوستانه پرسپولیس و آلانیااسپور بدون گل به پایان رسید.
در حاشیه این بازی، محمد عمری و اورونوف در کنار محمدمهدی محبی روی نیمکت و زیر باران نشستند تا یک قاب جالب و متفاوت در ارزروم ثبت شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137048" target="_blank">📅 18:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137047">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🫥
🫥
با موندن امیررضا رفیعی پرسپولیس میتونه 5 بازیکن جدید در پست های دیگه بگیره
🔴
دفاع وسط
🔴
دفاع چپ
🔴
هافبک بازیساز
🔴
مهاجم
🔴
دفاع راست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137047" target="_blank">📅 17:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137046">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
✔️
طبق اخبار دریافتی غیر رسمی : باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137046" target="_blank">📅 17:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137045">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚡️
⚡️
فوووووووووری
⏺
باشگاه خیبر خرم آباد رضایت نامه مهدی گودرزی رو 70 میلیارد تومن اعلام کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137045" target="_blank">📅 16:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137044">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚠️
⚠️
⚠️
تغییر ساعت برگزاری دیدار تدارکاتی پرسپولیس و آلانیااسپور
⏺
این مسابقه که پیش‌تر قرار بود از ساعت ۱۸:۳۰ برگزار شود، از ساعت ۱۷:۳۰ به وقت تهران آغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137044" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137043">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
✔️
طبق اخبار دریافتی غیر رسمی : باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137043" target="_blank">📅 16:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137042">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-QW8Cic9GRzxcDBmShEMzj9BPGmNFdsghZaAkctf9HSMF52-rr2YVquI5bBEElgriu5N2NPwtA7EiqUF2VywD5mU2Acm99uvTDlGMrNtP_YJJW8cF25Oe_2t8Uslfaj9H_HhFOkLtnusO0KkrNOO_7YCFTKXitzkqIdxyhCJIQSNn2o56Tl2dVqFDjU2ZVK--hr-zd5ZzbRLTBM2W5jgau7_DwBb33woU0T746xD6fDfzoC1E8ybw0laSRO7cDCT9MjJvl1rfclZahfBlPDKZbBBiJ12cq03vTTETevkdZZxHiEd4rFOP7C1zTf9ZN27sQ8ILIB_Xp_vZmwc647Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
اوج
هیجان و جذابیت با لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
پنجشنبه ساعت ۱۵:۰۰
[
لهستان
🇵🇱
🆚
🇺🇦
اوکراین
]
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
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137042" target="_blank">📅 15:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137041">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
🇳🇱
رسانه‌ی هلندی:
🔴
آلن هالیلوویچ در آستانه پیوستن به پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137041" target="_blank">📅 15:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137040">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgbGaczqTI0OXYyoBvao1X-LlSK6zG4t4lNN3Ar0b3V-sS-qiCh2M89O0geQJ8fbp7Gjfw5PPsDdkAfuA4S1916Nxaf_t5oLWonE75v4KJ1UfzLbezJ2NJHSoDxVnqM0FC-CenC7nVJEWqLYzAutr9OY6SYrWcqth_VBgrKaljSMIkIchsv9PeEdkErFeCglXptTc0b_BIf_9FqIHvGx2pBlJGQHnYU8THLCP-sl0yhluJw6mci8Bmx0bEhynr0oBaWFoPADCX1hlZNQeJ13qKFlG4Wh9A7BX0I39oAwtGSk9HsDwfzOyAyDWdqbPJ7YY0XLcq7j57ZElm2imNBINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ورزشگاه دستگردی تهران حداقل تا‌ دوماه آینده بدلیل تعویض چمن در دسترس نیست و امکان برگزاری و میزبانی از تیم‌های تهرانی را ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137040" target="_blank">📅 15:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137039">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
❌
حضور مسعود محبی در روسیه منتفی شد/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137039" target="_blank">📅 15:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137038">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏅
آلانیا اسپور حریف تدارکاتی بعدی پرسپولیس در ترکیه
▶️
با اعلام باشگاه پرسپولیس، شاگردان تارتار، روز پنج‌شنبه در دومین بازی تدارکاتی خود از اردوی آماده سازی پیش فصل در ترکیه، به مصاف تیم آلانیا اسپور خواهند رفت که خود را آماده فصل جدید رقابت‌های سوپر لیگ ترکیه…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137038" target="_blank">📅 15:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137037">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
تارتار گفته عیدی تو فاز هجومی خوب نیست و ازش راضی نیست  پ.ن مگه با نظر خود تارتار جذب نشده .مگه بازیکن خودش نبوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137037" target="_blank">📅 14:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137036">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137036" target="_blank">📅 13:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137035">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
#منهای_ورزش
✔️
باز هم جنوب باز هم مردم بی گناه
💔
❤️
✔️
شهید و ۲ زخمی در حملۀ آمریکا به محله چاهتنگو شهر قشم
✔️
دانشگاه علوم پزشکی هرمزگان: در حملۀ دشمن آمریکایی به منزل مسکونی در محلۀ چاهتنگو شهر قشم، پدر و مادر خانواده و یک کودک ۲ ساله به شهادت رسیدند و…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137035" target="_blank">📅 13:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137034">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📎
📎
📎
یه سوال پیش میاد اگه واقعا حس میکنید هنوز تو دفاع راست مشکل دارین پس عیدی چرا جذب شد؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137034" target="_blank">📅 13:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137033">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915de24844.mp4?token=rhVONm7Rdt-bCbwBeS-6od6oHDVkQezJXO7Ry88d0VUFvP_V7lq_p7slYtQpDPZEJ9DulGUE0-LlZ05kRTW1EC-1q2DFSjOkxsEj-uLSGXO8o3bojqboQ8gRqQ1lzLPpCiZrR7AXHIapiK0NLbLHB91B35UK7vFsnLp87DaDuoajJC9JZHM4G_tIkVyjzYAGUukygjDKIMQry9EdXCWhaWuMh6emrBXXeIyuFMkBfADm8MubAKn03lgl033UwR7pkaeIZze8SMOelw-BR_CJomFZsYs4SWEKtjazXjpY8wPS2UVk6O0SX66RDkdPr3xKmMO3TxCtme4Ok2I6QERVhlfGjk7kCwBQbsmG7XEijqAMPqgJXwDnoh1uKNa9Presjqk7TqBLF9AshwZI7OG14W21fYq1SVeK4pFN6MflanoYb6b6Y7R4q8dwPlb5Ijuumfi0_LAEeKnnIJE5LNdSlHXpgzOmIC7kOmwC7hsxMSfSR4VtaLUMEX3sobMYdnNg8-hhp_BLyfJFlr1jarlEloK7v4eeY2Faw2dpRTKCHVb99sD03uDVsUAwxGOuoJtcqQScWze-SIaE2QW5rEeqEwnPzE14lXp4fgeRunuawmWgpDMvL0sxKR2rlRvLz3hAziv522O0hbPi4O7okikKaS--5k3HBONP01DOSxdzBM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915de24844.mp4?token=rhVONm7Rdt-bCbwBeS-6od6oHDVkQezJXO7Ry88d0VUFvP_V7lq_p7slYtQpDPZEJ9DulGUE0-LlZ05kRTW1EC-1q2DFSjOkxsEj-uLSGXO8o3bojqboQ8gRqQ1lzLPpCiZrR7AXHIapiK0NLbLHB91B35UK7vFsnLp87DaDuoajJC9JZHM4G_tIkVyjzYAGUukygjDKIMQry9EdXCWhaWuMh6emrBXXeIyuFMkBfADm8MubAKn03lgl033UwR7pkaeIZze8SMOelw-BR_CJomFZsYs4SWEKtjazXjpY8wPS2UVk6O0SX66RDkdPr3xKmMO3TxCtme4Ok2I6QERVhlfGjk7kCwBQbsmG7XEijqAMPqgJXwDnoh1uKNa9Presjqk7TqBLF9AshwZI7OG14W21fYq1SVeK4pFN6MflanoYb6b6Y7R4q8dwPlb5Ijuumfi0_LAEeKnnIJE5LNdSlHXpgzOmIC7kOmwC7hsxMSfSR4VtaLUMEX3sobMYdnNg8-hhp_BLyfJFlr1jarlEloK7v4eeY2Faw2dpRTKCHVb99sD03uDVsUAwxGOuoJtcqQScWze-SIaE2QW5rEeqEwnPzE14lXp4fgeRunuawmWgpDMvL0sxKR2rlRvLz3hAziv522O0hbPi4O7okikKaS--5k3HBONP01DOSxdzBM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
❌
بهترین خبر امروز: نوید قره داغی حرومزاده که دخترا رو کتک میزد، دستگیر شد.
🔴
امروز صبح موقع دستگیری نوید بیشرف ، این حیوون وحشی به سمت پلیسا حمله‌ور میشه. پلیسا هم سه تا تیر توی پاش و یه تیر توی دستش میزنن و حسابی کتکش زدن، اعضای محل هم هر کدوم یه انگشت توی کونش فرو کردن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137033" target="_blank">📅 13:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137032">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
شنیده میشه پرسپولیس دوباره رفته سراغ مسعود محبی و با پیشنهاد جدید دنبال جذب این بازیکن
🔹
محبی هنوز هیچ قراردادی با تیم روسی نبسته و امکانش جذبش هنوزم هست همه چیز بستگی به نوع مذاکرات و پیشنهاد مدیران تیم داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137032" target="_blank">📅 12:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137031">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/137031" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137030">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🫥
🫥
با موندن امیررضا رفیعی پرسپولیس میتونه 5 بازیکن جدید در پست های دیگه بگیره
🔴
دفاع وسط
🔴
دفاع چپ
🔴
هافبک بازیساز
🔴
مهاجم
🔴
دفاع راست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137030" target="_blank">📅 10:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137029">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
پیوستن پورعلی‌گنجی به الطلبه صحت ندارد
⚠️
⚠️
ساعتی پیش برخی رسانه‌ها از پیوستن مرتضی پورعلی‌گنجی، مدافع پرسپولیس، به تیم الطلبه عراق خبر دادند اما پیگیری‌های خبرنگار فارس نشان می‌دهد این خبر صحت ندارد.
⚠️
⚠️
پورعلی‌گنجی هیچ قراردادی با باشگاه الطلبه عراق امضا…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137029" target="_blank">📅 09:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137028">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137028" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137027">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚡️
⚡️
امیررضا رفیعی قرارداد جدیدی را امضا خواهد کرد
🔻
🔻
رفیعی یک سال دیگر با پرسپولیس قرارداد دارد مشکلی برای همراهی این تیم نخواهد داشت اما احتمالا با تمدید قرارداد در جمع شاگردان مهدی تارتار حضور خواهد داشت و زیر نظر حسین اینانلو کار خود را دنبال خواهد کرد.…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137027" target="_blank">📅 09:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137026">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🫥
🫥
🫥
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137026" target="_blank">📅 09:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137025">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137025" target="_blank">📅 09:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137024">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137024" target="_blank">📅 08:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137023">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9IVBjP_b41bmMJ2e53yUg29tgVNMR9FzKqyQBTALoBqj2FwOFOZZtf6DYdy19l_SARhTOdjEMODx1DONv0getwPekKc7jzzhvElFcPbRLP57HDKTsleaoW3pJFzLlP-F88hLH3eEpQmQIyUekmwqrzNGYS1Rq91iywdBpmtPXlDd1K1Wvb87c6yY-PKdyqyxfwyzehpzVNpZ1w3DJLlehBBj9xNaM2sgVIZ1snjeByOttNR7JWhak7D7GLBekYJDQfMO7QuvWuVq3U002rE6-AXq9sbuWPhXZW__UjipyPVZ2nqfB8CC3K9fg5XmlwxBSYWsdGw9YJC6T-JSCBwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137023" target="_blank">📅 08:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137022">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtXE2Q801NugBP208v5RN9WYMVzkNxcgJo7bssEFwVQinPZ9uxJcWsZELnDC7Jw7hOlW6c9sIuIQQCRpIMXDElQ_SBnbrB594pu5L0ie_WBByFDz4P-6FhCKWqf3mEIQ8cGCnCN1zpiImTdij374e4sBAquex6w2uuj4_V1NTjOK5WqCoyL-MjmZHjvch2X1ejWNukHLDmdlH3214kYgiY3y8Mxb7zvZ-vQFWlwrAj0RYsDBKhhg8i1K6eq8wCqyySKs-P4Hkw0sX93gmLG1iIeDmIXQ6-oiu6YrFqxJnQ_TIwstJEMtpVcrHGg-5lw73Le_Mf5w9zipNhvfWFDVvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
اوج
هیجان و جذابیت با لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
پنجشنبه ساعت ۱۰:۳۰
[
ایتالیا
🇮🇹
🆚
🇺🇸
آمریکا
]
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
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137022" target="_blank">📅 01:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137021">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De1ixxGiPnP_U9F7n3COcxMLeZJe-R5mMuijsiWdZHsWxeZXB3z-wjRnSwZ2ZaHsAghMEDx_VwJ7RoKFxVyNV1qwHCmxHrWtR0uMugHozf_Az62EXugFphV38I6YZdDjnqKPvyyPftkBWZWbOod6ci52vVVRo4T0LBAKFYiLvdxdtont15U9JF9nf3smUpmQDOae7QAhaaboig7NXZ_frAk2iQAtTgbvnxLFUNvfVvQSaQA_m3j4O8JlxJ1s_LawRIYPlosP4t9_LBg3KFpsttQNemUVOQ-d7CbrFArJOeWj5-HE47et7jCfr-tsRSixvktQ_osiu4Yep3kVEEHfew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137021" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137020">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❤️
❤️
❤️
❤️
❤️</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137020" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137019">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/137019" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
