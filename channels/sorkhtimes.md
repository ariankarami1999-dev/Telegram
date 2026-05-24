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
<img src="https://cdn4.telesco.pe/file/G_Rit9y_qcSqPOM47-J6BcqOLPOs0yzF04slESmbfdpxkYZT2rVYKq35Xy4tpAj3agsaftIcaPqIFZA8R0FRiNzI1PLz1CSOXk0WUNgo0XJwqBg6mv6_84mQjW1kvZtBauNprQN2jAw2VoutB1Cc4DcRW3IRJY506zpgT-NHYXC0ccXFk3yVssK8tIi1FJQY1Mx4en4BRYRme8cT54yZHsRVL02J4lBsNTrbcpS_GxknghTiAkaHG-9uTcEo84nPbPgSwfdRv2EifOzKID3eqHu-U6wlz4QGJu2T9gSRmqWdFElL-r1JGmd7PMkGkZtoxOwRYXc8aK0VBh8Jps8QKQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 11:48:48</div>
<hr>

<div class="tg-post" id="msg-132112">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
ورزش‌سه: محمودی بشدت آمادست و احتمالا راهی جام جهانی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 339 · <a href="https://t.me/SorkhTimes/132112" target="_blank">📅 11:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132111">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
تا قبل 21 خرداد حکم علی بیرو بیاد از جام جهانی محروم میشه / خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 362 · <a href="https://t.me/SorkhTimes/132111" target="_blank">📅 11:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132110">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
⛔️
احتمال محرومیت بیرانوند از حضور در جام‌جهانی؛
💯
حضور روی سکوها به‌جای زمین چمن!
⚠️
با شکایت باشگاه پرسپولیس درخصوص پرونده علیرضا بیرانوند به CAS و پیگیری شدید سرخپوشان تهرانی، درصورت صدور رای محرومیت بیرانوند طی روزهای آینده، دروازه‌بان تراکتور جام‌جهانی…</div>
<div class="tg-footer">👁️ 356 · <a href="https://t.me/SorkhTimes/132110" target="_blank">📅 11:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132109">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔰
سرویس VIP تک کاربره
🔰
1 گیگ 190
2 گیگ 380
3 گیگ 570
5 گیگ 950
10 گیگ 1700
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 426 · <a href="https://t.me/SorkhTimes/132109" target="_blank">📅 10:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132108">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3XCkLTz_Zjai2MI41V0umk_i_-xwpckWQGMXZ_grqnhZ9y9R80VIcZCM9mGUyfr3FM0w4LzlwrTSBHdV7AW5Np7PvkeUgqa9uoS9HpC529ckbNyUXRR6Z6S3mFbGnRceMrROM-cesf_1tSIEbRcZKSlAYFSERn-Lm075K2bwEremJyPpaV6a4SoWiWiI52ycbbMKCZowTWrFr4AveEiyQPfMxPHLk2H9Gq-hkYB6gmsbP5w_HXuFAiZC9Zniid_UDGWBuCGMJxUpaFSR8ls8rCXoeSJ5Iq22DnP8nXXO2gxJUx3hVEJYX4COniAFkaycArQblRmF32cFu7PsCaBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این روزا قبل از پیش‌بینی بیشتر از خود بازی باید نگران این باشی که VPN وصل میشه یا نه.
😀
ربات تلگرام وینکوبت دقیقاً برای همین شرایط خوبه چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
میتونی مستقیم وارد بازی‌ها و کازینو شی، پیش‌بینی ثبت کنی، واریز و برداشت انجام بدی و همه‌چی خیلی سریع‌تر و راحت‌تر انجام میشه.
🟣
آدرس دائمی سایت:
wincobet.com</div>
<div class="tg-footer">👁️ 435 · <a href="https://t.me/SorkhTimes/132108" target="_blank">📅 10:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132107">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 465 · <a href="https://t.me/SorkhTimes/132107" target="_blank">📅 10:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132106">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 479 · <a href="https://t.me/SorkhTimes/132106" target="_blank">📅 10:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132105">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">📣
#شنیده‌ها
🗣
🇮🇷
محمدامین حزباوی از باشگاه پرسپولیس پیشنهاد رسمی دریافت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 514 · <a href="https://t.me/SorkhTimes/132105" target="_blank">📅 10:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132104">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 518 · <a href="https://t.me/SorkhTimes/132104" target="_blank">📅 10:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132103">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
الحدث:
🔴
ایران و آمریکا به دشمنی طولانی مدتشون پایان دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132103" target="_blank">📅 01:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132102">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
الحدث:
🔴
ایران و آمریکا به دشمنی طولانی مدتشون پایان دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132102" target="_blank">📅 01:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132101">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
❌
آکسیوس:
🔽
توافق‌نامه همین الان توسط دو طرف امضا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132101" target="_blank">📅 01:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132100">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
علی هاشم خبرنگار الجزیره: طبق گفته منابع من، پیش‌نویس پیشنهادی که قرار است نهایی شود شامل موارد زیر است:
❌
پایان جنگ در همه جبهه‌ها از جمله لبنان
❗️
آزاد شدن میلیاردها دلار از دارایی‌های مسدود شده ایران
❌
لغو محاصره دریایی آمریکا و گشایش تنگه هرمز
🔽
خروج…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132100" target="_blank">📅 01:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132098">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
تاج رئیس فدراسیون فوتبال: طی جلساتی که با مدیران فیفا داشتیم به جای آمریکا به کمپی در مکزیک خواهیم رفت تا اردوی خودمان را برگزار کنیم/ با این کار مشکلات ویزا حل می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132098" target="_blank">📅 01:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132096">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
ترامپ :   من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/132096" target="_blank">📅 00:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132095">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
فرهیختگان: پرسپولیس بجای سپاهان به عنوان نماینده سوم اسیایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/SorkhTimes/132095" target="_blank">📅 00:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132094">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 220T
2 گیگ 440T
3 گیگ 660T
5 گیگ 1T
10 گیگ 1.8T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/SorkhTimes/132094" target="_blank">📅 00:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132093">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
ترامپ :   من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر…</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/SorkhTimes/132093" target="_blank">📅 00:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132092">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcJ5ogmJO_C5r0vGlmDhnF5ndLdw-hcxBi70AIUNiKXwVzhpk68dio56gh0gM1W-hIIcFaLeqx1jjs1z-3vgiqpcNRF5Ud_vZPfuF7Nk06RvLLSVtT984Tr78U6NnwGOsnRcrpmXxTgWNrnIxM97XIq8YbroIFK67Ow2aghFsIRCtiktg5b4Q5nSLhnvLViZ2KAgi90NzADBP0EdhrCBEgCPZcQzr-7REzQiPYguBeA8EAUbteLjAmOrpLeKlfP09NiVtYv6Ik-V7NtWz5nyVo63QFEIEZ8mde_GzQAdokU1aIGh04nROgi_FpuxB8FhMpGI2gZ66dxO8oXi4EVSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ :
من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر، فیلد مارشال سید عاصم منیر احمد شاه از پاکستان، رئیس‌جمهور رجب طیب اردوغان از ترکیه، رئیس‌جمهور عبدالفتاح السیسی از مصر، پادشاه عبدالله دوم از اردن و پادشاه حمد بن عیسی آل خلیفه از بحرین داشتیم، درباره جمهوری اسلامی ایران و همه موارد مربوط به تفاهم‌نامه‌ای درباره صلح.
یک توافق تا حد زیادی مذاکره شده است که منوط به نهایی شدن بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر ذکر شده است. به طور جداگانه، من تماسی با نخست‌وزیر بیبی نتانیاهو از اسرائیل داشتم که به همان صورت بسیار خوب پیش رفت. جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بحث است و به زودی اعلام خواهد شد.
علاوه بر بسیاری از عناصر دیگر توافق، تنگه هرمز باز خواهد شد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 935 · <a href="https://t.me/SorkhTimes/132092" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132091">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
#فوری | الحدث:
🔻
پیش‌بینی‌هایی مبنی بر اعلام نهایی شدن توافق صلح بین واشنگتن و تهران ظرف ۲۴ ساعت آتی، وجود دارد.
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 954 · <a href="https://t.me/SorkhTimes/132091" target="_blank">📅 23:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132089">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/SorkhTimes/132089" target="_blank">📅 23:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132088">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
خبر رسیده دو بازیکن تیم سپاهان 10 روز پیش با ارسال نوتیس به باشگاه سپاهان در آستانه فسخ قرارداد خود با این باشگاه قرار دارن و مدنطر پرسپولیس هستن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/132088" target="_blank">📅 23:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132087">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
👈
ادعای کانال ۱۴ اسرائیل: چند منبع معتبر تأیید می‌کنند که ایران با برخی از درخواست‌های کلیدی ایالات متحده موافقت کرده است و کمتر از ۲۴ ساعت دیگر اعلام توافق انجام خواهد شد که به تهران چند ماه فرصت می‌دهد تا کاملاً تسلیم شود
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/132087" target="_blank">📅 23:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132086">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
#فوری | ادعای الحدث به نقل از یک منبع عالی‌رتبه:
🔴
تنها ساعات کمی تا اعلام توافق بین آمریکا و ایران فاصله است
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/132086" target="_blank">📅 22:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132085">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
کمپ تیم‌ملی رفت مکزیک و فقط برا بازیا میان امریکا...کل فاصله ما با مکان بازی‌های ما در لس آنجلس 55 دقیقه با پرواز است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/132085" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132084">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
تاج رئیس فدراسیون فوتبال: طی جلساتی که با مدیران فیفا داشتیم به جای آمریکا به کمپی در مکزیک خواهیم رفت تا اردوی خودمان را برگزار کنیم/ با این کار مشکلات ویزا حل می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/132084" target="_blank">📅 22:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132083">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
🚨
🚨
عصر ایران نوشت: سفارت آمریکا به طارمی،شجاع خلیل زاده و احسان حاج صفی ویزا نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/132083" target="_blank">📅 21:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132082">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
روزنامه اعتماد : به احتمال بسیار زیاد در این هفته رفع انسداد اينترنت مصوب شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/132082" target="_blank">📅 21:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132081">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
👈
ترامپ، در گفت‌وگو با سی‌بی‌اس نیوز:  مذاکره‌کنندگان ایالات متحده و ایران «بسیار به نهایی کردن یک توافق» برای پایان دادن به جنگ بین دو کشور نزدیک‌تر شده‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/132081" target="_blank">📅 21:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132079">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
بر اساس گزارشات منتشر شده از فایننشال تایمز با اصرار و همچنین تلاش بدون وقفه اسلام آباد آتش بس بین ایالات متحده و مقامات رژیم ایران به مدت 60 روز دیگر تمدید خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/132079" target="_blank">📅 19:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132078">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
باراك راوید خبرنگار Axios
🔴
همه چیز پنجاه پنجاه است و دونالد ترامپ هم میتواند بمب باران را شروع کند و هم میتواند به خواسته عاصم مونیر آتش بس 60 روزه را اعلام کند و او امشب قرار است در این مورد با تیم خود مشورت کند و تصمیم بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/132078" target="_blank">📅 19:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132077">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🟥
ترامپ: شانس توافق یا جنگ 50/50 است امروز با نمایندگان خود دیدار میکنم و تا فردا تصمیم میگیرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/132077" target="_blank">📅 19:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132076">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🟥
ترامپ: شانس توافق یا جنگ 50/50 است امروز با نمایندگان خود دیدار میکنم و تا فردا تصمیم میگیرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/132076" target="_blank">📅 19:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132075">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
هیئت پاکستانی بعد از دریافت جواب ایران به پیشنهاد آمریکا به پاکستان برگشتن و احتمالا تا امشب این جواب به آمریکا منتقل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/132075" target="_blank">📅 19:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132074">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
فرهیختگان: دعوت شدن مغانلو جای روزبه یعنی قلعه‌نویی از عملکرد مهاجمان راضی نیست و احتمالا یکی از بین علیپور و مغانلو خط بخورن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132074" target="_blank">📅 18:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132073">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
دروازه‌بان سابق پرسپولیس درگذشت
🔺
شکرالله آغاسی، دروازه‌بان پیشین تیم فوتبال پرسپولیس، دار فانی را وداع گفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132073" target="_blank">📅 17:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132071">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
فووووووووووووری
🔴
مدیران فدراسیون فوتبال تیم فوتبال پرسپولیس را برای شرکت در مسابقات سطح دو آسیا به afc صادر خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/132071" target="_blank">📅 16:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
دقایقی پیش اسکای نیوز ادعا کرد که میانجی پاکستانی موفق شد بر مانع پرونده هسته‌ای ایران غلبه کند.
🔴
الان امریکا کوتاه اومد یا ایران؟
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132070" target="_blank">📅 16:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132069">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
سردار دورسون از تراکتور و سپاهان پیشنهاد دریافت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/132069" target="_blank">📅 16:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132068">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
باشگاه پرسپولیس اعلام کرد هیچ مصالحه ای با باشگاه تراکتور درباره علیرضا بیرانوند نخواهد کرد و پرونده را ادامه می‌دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132068" target="_blank">📅 16:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132067">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قیمت ها پایین کاهش پیدا کرد</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132067" target="_blank">📅 15:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132064">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
حمله تند وزیر ارتباطات به مخالفین اتصال مجدد اینترنت: این نگاه قیم معابانه به مردم چیست؟ کی گفته اینترنت را باید خلاصه در دو پیام‌رسان بدانیم؟
❌
ستار هاشمی وزیر ارتباطات:صحبت هایی که در رابطه با نقد دسترسی مردم به اینترنت آزاد می شود، نگاه قوه عاقله کشور نیست. ان‌شالله اینترنت برای آحاد مردم و به صورت عادلانه برقرار می شود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/132064" target="_blank">📅 15:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132063">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
نورالدین الدغیر خبرنگار الجزیره در تهران:
🔴
وساطت‌ها بین تهران و واشنگتن به مرحله‌ای رسیده که یکی از سران منطقه‌ای به طور مستقیم برای پر کردن شکاف‌ها وارد عمل شده.
🔴
ظهور قطر در این لحظه حساس به طور مستقیم و بر اساس اطلاعات و منابع موجود، نه صرفاً به عنوان…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132063" target="_blank">📅 14:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132062">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⏺
نیویورک تایمز :
🔴
فیفا قصد دارد دوباره ورود پرچم «شیر و خورشید» ایران پیش از انقلاب و لباس‌های مرتبط با آن را به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع کند. این پرچم در جام جهانی ۲۰۲۲ قطر هم محدود شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132062" target="_blank">📅 14:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132061">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
عراقچی: به توافق نزدیک نیستیم. زیاده خواهی های‌ آمریکا مانع پیشرفت مذاکراته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132061" target="_blank">📅 14:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132060">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
شبکه CBS آمریکا: آمریکا به‌زودی به ایران حمله خواهد کرد.هر لحظه ممکن است حمله‌ای رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/132060" target="_blank">📅 14:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132058">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس :
🔴
مسئولین دل‌سوز کشور به این نتیجه رسیدن که وصل کردن اینترنت به صلاح همه‌ی مردم نیست و فعلا قرار نیست اینترنت بین‌المللی رو برگردونیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132058" target="_blank">📅 11:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132057">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
شایعات: ویزا شجاع خلیل زاده، مهدی طارمی و احسان حاج‌صفی بخاطر خدمت تو سپاه پاسداران صادر نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132057" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132055">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
رسمی؛ روزبه چشمی به علت مصدومیت جام جهانی را از دست داد و شهریار مغانلو جایگزین این بازیکن در لیست تیم ملی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132055" target="_blank">📅 09:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132054">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
🏅
مذاکره سپاهان با ۵ بازیکن برای فسخ قرارداد
⏺
باشگاه سپاهان هفته گذشته با وحدت هنانوف بازیکن تاجیکستانی‌اش قطع همکاری کرد و حالا قرار است چند تغییر دیگر هم برای فصل آینده ایجاد کند. مدیران سپاهان در حال مذاکره با 5 بازیکن هستند تا با آنها قطع همکاری صورت…</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132054" target="_blank">📅 09:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132053">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
اکسیوس:برخی منابع نزدیک به مذاکرات همچنان بر این باورند که طی ۲۴ ساعت آینده فرصتی برای نوعی پیشرفت وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132053" target="_blank">📅 09:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132052">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=Ox6lec666IIH0yULTb3osAQPwoLiDsWJZjRxYsbobTmoSy9yNWorzr1Oqna_jWJPNL_G_f14rkvw3zOS6dPISZZE6RVm6pJBVuVERczXdw4QIVgvRg1EevILQVlFJFlSVjNxWmTStJ9hM5xqN1UgA4dp94UEHxclKi1NgSdcmYPunC4R_vXwBl0jU4Sz1EX_dkxz5bf26ALCzqef7zo3W0lbWTqA-gAARYYznMswGJDvTi5Mlh-LnH7yTM0Lh2PDT-YT9dRg4UD7oF8_L7uiRIFT9wzJ6zhQCwBlkaNRuAMasKoyngazLwzkVzflMPO4VDfoZ1mUS-HnuqqGvtgtew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=Ox6lec666IIH0yULTb3osAQPwoLiDsWJZjRxYsbobTmoSy9yNWorzr1Oqna_jWJPNL_G_f14rkvw3zOS6dPISZZE6RVm6pJBVuVERczXdw4QIVgvRg1EevILQVlFJFlSVjNxWmTStJ9hM5xqN1UgA4dp94UEHxclKi1NgSdcmYPunC4R_vXwBl0jU4Sz1EX_dkxz5bf26ALCzqef7zo3W0lbWTqA-gAARYYznMswGJDvTi5Mlh-LnH7yTM0Lh2PDT-YT9dRg4UD7oF8_L7uiRIFT9wzJ6zhQCwBlkaNRuAMasKoyngazLwzkVzflMPO4VDfoZ1mUS-HnuqqGvtgtew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪
︎با این وضعیت اینترنت،
ربات تلگرام وینکوبت
خیلی کاربردیه چون براحتی وارد سایت میشی.
▪
︎هم ثبت‌نامش سریع انجام میشه، هم کازینو رو داخل خود تلگرام میتونی بازی کنی و عملاً کل سایتو داخل ربات داری.
▪
︎پیش‌بینی، بازی، واریز، برداشت و همه‌چی همونجا انجام میشه و خیلی روون‌تره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/132052" target="_blank">📅 01:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132051">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
تیم فوتبال دهوک عراق به یحیی گل محمدی پیشنهاد داده اما یحیی میخواد تو ایران مربیگری کنه!/فارس
🚮
امپرور جان لطفا هر گورستونی میری طرف های خیابون شیخ بهایی آفتابی نشو…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132051" target="_blank">📅 01:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132050">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
اوریه معتقده در این پرونده پیروز میشه و استدلالش هم همینه که در ترکیه ازش تست گرفتن و همونموقع میدونستن هپاتیت داره/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/132050" target="_blank">📅 01:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132049">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">#افشاگری
رضا شاهرودی این روزا داره برکناریش رو میکوبونه ولی نمیگه بخاطر چی برداشتنش.
پارسال توی هر ۴ رده‌ سنی ۲-۳ بازیکن سفارشی و پولی اضافه کرد که وقتی تمرین میکردن سطحشون از همه بازیکنها پایینتر بود.
مربی‌های پایه هم چون دستشون به جایی نمیرسه زیر بار حرف شاهرودی رفتن و توی تیم رد کردن اسم بازیکنها رو.
۸ تا بازیکن هستن که یک دقیقه هم در طول فصل برای پرسپولیس بازی نکردن و امسال دیگه
خودشون نیومدن برای تیمها.
شاهرودی حتی وسط فصل هم مربی‌ها رو صدا میکرد و بهشون میگفت اگه اینا رو بازی ندی برت میداریم ولی چون تیمها اول دوم جدول بودن مربیها گوش نکردن و زیر بار حرفش نرفتن/فوتبال ویژن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/132049" target="_blank">📅 00:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132048">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
جباری: جای پیروانی بودم خانواده‌ام را به ایران می‌آوردم
❌
🎙
رضا جباری در خصوص برگزاری ادامه مسابقات لیگ برتر بعد از جام جهانی ۲۰۲۶ گفت:
◽️
به نظر من این طرح با همه ایراداتی که دارد بهتر از این است که یک یا دو تیم را به عنوان تیم‌های قهرمان و نماینده آسیایی…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132048" target="_blank">📅 00:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132047">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
فووووووووووووری
🔴
مدیران فدراسیون فوتبال تیم فوتبال پرسپولیس را برای شرکت در مسابقات سطح دو آسیا به afc صادر خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132047" target="_blank">📅 00:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132046">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🟥
خبرنگار الجزیره در تهران: به نظر می‌رسد فضای مذاکرات ایران و آمریکا تا این لحظه مثبت است و پیشرفت ملموسی در حل برخی اختلافات از طریق میانجیگر پاکستانی حاصل شده است
🔸
آمدن فرمانده ارتش پاکستان به تهران ممکن است دو هدف داشته باشد: حل اختلافات باقی‌مانده یا…</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132046" target="_blank">📅 00:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132045">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
نت بلاکس: قطعی اینترنت در ایران از مرز 240 ساعت گذشت  @SorkhTimes</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132045" target="_blank">📅 00:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132044">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
اوستن اورنوف شب گذشته بدون مشکل در تمرین تیم ملی ازبکستان شرکت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132044" target="_blank">📅 00:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132043">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
گفته میشه که پرسپولیس به عنوان نماینده ایران در لیگ آسیا 2 شرکت خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132043" target="_blank">📅 23:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132042">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
گفته میشه که پرسپولیس به عنوان نماینده ایران در لیگ آسیا 2 شرکت خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132042" target="_blank">📅 23:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132041">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
زمزمه هایی شنیده می‌شود که امیر قلعه‌نویی پس از جام جهانی از تیم ملی جدا خواهد شد و یحیی گل‌محمدی گزینه اصلی جانشینی او است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132041" target="_blank">📅 23:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132038">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
ترامپ: با اینکه خیلی میخواهم در کنار پسرم برای مراسم عروسی باشم اما حس میکنم که مهم تر است در واشنگتن و کاخ سفید در طی زمان مهم پیش رو در روز شنبه و یکشنبه بمانم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SorkhTimes/132038" target="_blank">📅 22:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132037">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔖
🔴
فرهیختگان: طبق شنیده‌های ما پرسپولیس به AFC برای سهمیه سوم معرفی خواهد شد
✅
باتوجه به تجربه بین‌المللی باشگاه‌ها، رنکینگ آنها در AFC و باشگاه‌های جهان، شرایط مالی باشگاه‌ها و... در چنین شرایطی و ناتمام ماندن لیگ، اوضاع پرسپولیس به مراتب بهتر از دو تیم بالای…</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/132037" target="_blank">📅 22:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132034">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
ترامپ: با اینکه خیلی میخواهم در کنار پسرم برای مراسم عروسی باشم اما حس میکنم که مهم تر است در واشنگتن و کاخ سفید در طی زمان مهم پیش رو در روز شنبه و یکشنبه بمانم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132034" target="_blank">📅 22:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132033">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgEyKBkrf4XvLnhB0BYQrYGkWdGt7mod5mkpGEo4GXSTIvFBSa33FxLkpY-xn9BGOqB0BxuJRZwc1S0YrmRBz0neESY8CABWwKZx1QogTgSELdWqLCTK-_UvuzwhG3FkqHmZrnxX5vRGIRL1n_fAP1ZmIEijd9pp5lqMx5PZkUM9mZjoRE44cWDAZI0FNf87Hv-x2YhbbKjYEeaolO2RnqQPRjo-ZLqEmwgxelgkQDhb1uLzE_HJ4Jsm1SOeD6uQblxlA9fmEfoTku2-QSAuLQbXPEPzGJzFQuyHD6WR-79QJfFvyE851XLJb0a3Jt0YKWP8AQupfV_ET_dv27Wkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ: با اینکه خیلی میخواهم در کنار پسرم برای مراسم عروسی باشم اما حس میکنم که مهم تر است در واشنگتن و کاخ سفید در طی زمان مهم پیش رو در روز شنبه و یکشنبه بمانم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132033" target="_blank">📅 21:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132032">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
فوری؛ محمد خلیفه گلر ملی پوش آلومینیوم اراک و سابق پرسپولیس به استقلال پیوست/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/132032" target="_blank">📅 21:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132031">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
شایعات: ویزا شجاع خلیل زاده، مهدی طارمی و احسان حاج‌صفی بخاطر خدمت تو سپاه پاسداران صادر نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/132031" target="_blank">📅 21:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132030">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHT3LMc01po8-bLCnx34JI5VXRSvzzgBu6raX5rmavLmDPkrSYF9i-W0OJslvnk391nuAoI-U5MZhDTO5yiM9LLN6acRb5QA4a4NE_MdILC-w1mEo4eCtWj1zuLyTiKpB-Jph6-y7y4DXLRDwyHRRXpbSygVRKp7_Gk7t2YHGrhi0aAct7P_wA9ND8h8LipUhv_UX1D8erTKaGE27IH4XxNpkHMcYopWGry-3Pwi_uq4EiM_7MPT8z0gYswTgGpICRcCyfNB2_QKk6_dUYUzJt06IvQZ3wwkdwtxpoxdQfKEYJzPdkd00wX6az6Yjolm1KvCnwrIDzT5WDsYnP5t3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فارس: باشگاه پرسپولیس قصد تمدید قرارداد میلاد محمدی را ندارد و به احتمال زیاد از جمع سرخپوشان جدا شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132030" target="_blank">📅 21:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132029">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
پیشنهاد رسمی باشگاه پرسپولیس به رئیس سازمان لیگ: حالا که‌مجوز حرفه‌ای باشگاه سپاهان صادر نشه استقلال و تراکتور رو به لیگ نخبگان آسیا بفرستید و ما رو هم به سطح دو لیگ قهرمانان آسیا.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132029" target="_blank">📅 21:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132026">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
شجاع خلیل‌زاده، با ۳۷ سال سن، پیرترین بازیکن تاریخ ایران در کل ادوار جام جهانی فوتبال خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132026" target="_blank">📅 19:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132025">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
باشگاه گل‌گهر از چادرملو بابت استفاده از آندرس، بازیکن پارگوئه ای شکایت کرده و خواهان 3 بر 0 شدن مسابقه این تیم برابر چادرملو شده است؛ در صورتی که چادرملو در این پرونده محکوم شود، جایگاه چهارمی خود را از دست داده و به رده ششم جدول سقوط خواهد کرد و پرسپولیس…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132025" target="_blank">📅 19:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132023">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
مجوز حرفه ای سپاهان صادر نشد و ممکنه یه تیم از بین پرسپولیس و گلگهر بره اسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132023" target="_blank">📅 19:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132022">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
شرزود تمیروف مهاجم سابق پرسپولیس با ۲۸ گل در ۳۲ بازی، آقای گل لیگ عراق شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132022" target="_blank">📅 19:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132020">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری | رویترز:
🔻
منابع مطلع گزارش دادند که قطر تیمی مذاکره‌کننده به تهران فرستاده است، با هماهنگی ایالات متحده، برای کمک به رسیدن به توافقی برای پایان دادن به جنگ با ایران
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/132020" target="_blank">📅 19:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132019">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🟥
🟥
🚨
باراک راوید، خبرنگار آکسیوس:  عاصم منیر فرمانده ارتش پاکستان
🇵🇰
، امروز برای بستن توافق بین آمریکا و ایران و تموم کردنِ جنگ، راهی تهران میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132019" target="_blank">📅 17:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132018">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
#تکمیلی | العربیه : پیش‌نویس نهایی توافق مورد انتظار بین آمریکا و ایران که طی ساعات آینده برای توقف جنگ در همه جبهه‌ها تنظیم می‌شود:
🔴
۱. توقف کامل، فوری و بی‌قیدوشرط آتش‌بس در همه جبهه‌ها (زمینی، دریایی و هوایی).
🔴
۲. تعهد دو طرف به عدم هدف‌گیری هرگونه…</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/132018" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132017">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
مجوز حرفه ای سپاهان صادر نشد و ممکنه یه تیم از بین پرسپولیس و گلگهر بره اسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132017" target="_blank">📅 17:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132016">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
عضو کمیسیون فرهنگی مجلس : طرح جایزه کشتن ترامپ، تو مجلس تصویب میشه
😐
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132016" target="_blank">📅 15:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132015">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYY4KssH_F7Q4VOUfUpeNQEaeYir6tpi-7taNX7BcSix_MZd57FlMPmg-nHcObjbT0kmJs6RMDsl46_dRKhFXZGExvhFvwaQ8w30JhR9KDxNVmnD4S-xC-PQ6V0WwBV3pmWkSLVarxTbNSnTNHyd1x5AkZp0DBvu0UbGl0zRVWTtY-iFfivjGd4n76Y0gvZ-h8bkaLD65MkLZMB7U_wJcJiv-ig8fhQYEVmvdv9BzVI0U4CrEW2QseoC1dduRL8SsXGlnv3JZb8kAOoU5TfEg_ZLGev3V56LuboRaeSKqNsWC-GL7UH62vBfUzRouC8b55ZZyEPSOeMeDHwD52MXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
هنوز دنبال روش ورود به سایت می‌گردی؟
📌
کاربران حرفه‌ای دیگه وقتشون رو هدر نمیدن.
✌️
✅
سریع‌ترین راه ورود به وینکوبت فقط از طریق ربات رسمی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡️
بدون نیاز به جستجو
⚡️
بدون لینک‌های فیک و اشتباه
⚡️
ورود مستقیم و راحت
🔗
فقط یک کلیک تا ورود کامل به سایت وینکوبت:
👇
🤖
@Wincobet_bot
کانال رسمی سایت وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/132015" target="_blank">📅 15:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132014">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
پیشنهاد رسمی باشگاه پرسپولیس به رئیس سازمان لیگ:
حالا که‌مجوز حرفه‌ای باشگاه سپاهان صادر نشه استقلال و تراکتور رو به لیگ نخبگان آسیا بفرستید و ما رو هم به سطح دو لیگ قهرمانان آسیا.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132014" target="_blank">📅 15:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132013">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس :
🔴
مسئولین دل‌سوز کشور به این نتیجه رسیدن که وصل کردن اینترنت به صلاح همه‌ی مردم نیست و فعلا قرار نیست اینترنت بین‌المللی رو برگردونیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/132013" target="_blank">📅 14:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132011">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
مدیرعامل باشگاه سپاهان: نامه‌ای به دست ما رسیده و در آن چنین نگاشته شده که برای سپاهان مجوز حرفه‌ای صادر نخواهد شد، اما برای رقبا مجوز صادر شده است!
🔴
عدم صدور مجوز حرفه‌ای برای سپاهان می‌تواند جوک سال فوتبال ایران و حتی آسیا باشد. ما شانس بیشتری برای قهرمانی…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132011" target="_blank">📅 12:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132010">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
باشگاه سپاهان با انتشار اطلاعیه‌ای با کنایه فراوان به سایر تیم‌ها، عدم صدور مجوز حرفه‌ای خود را تایید کرد و بدین‌ترتیب باید شاهد تیم جایگزین برای طلایی‌پوشان در آسیا باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132010" target="_blank">📅 12:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132009">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
سپاهان بگا رفت و مجوز حرفه ای نگرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132009" target="_blank">📅 12:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132008">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
با اعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132008" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132007">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKubX09jKXel6QDijLFeOym_IfgLlqqsiBbcPc5NsGgAcOcNIDPJDRpV4d_16cNXHHfj3effPtTS_Q0-p0dCsH7skzqlAvQeZTUbs-rt5wKV-xVtueIWjBpUy6syA_ylKP9uV87UZZhJvYvkKse2mSvERTGOiVyroV32Bo987gvOTKgz1ILbvYlQT8qIrU7KnQUkvuSilRaP6whLEYNQaJ3iYzUFWrIrKwunJmiwIPVMT-zZ89iVT5hQC3fyim0KBWhhBXGv3H0IN-nDwlFl-32k6cUUkEzXFCusKhhV6let6jNBXEDzbENmhdGU6_6nSc3yoXAqRsTLgE_BP4TH_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس :
🔴
مسئولین دل‌سوز کشور به این نتیجه رسیدن که
وصل کردن اینترنت به صلاح همه‌ی مردم نیست
و فعلا قرار نیست اینترنت بین‌المللی رو برگردونیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/132007" target="_blank">📅 10:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132006">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZaeNV6J4LuhGQHV-8la7Z4i1g3T0TMC_-A9S5wjUQ--eBr4VHuet681w91PAy-0LXUX1wwOxfUlgCuDgn77rnuvsubEsHVC3zqXzEnSKDTXwCrxlKsO0aNOKbWyCEouM69FUzqB00Hxzv0LevAXqhbhCQSBHLjOvT1TVizceAwpY-u1eZspgRfNLLEPLyNDgSjJGmFlY3gqNpySuFmRUC_b2QeMFHa2TliJH8jCnFf_Ye5ETMRqm2gVSBNLbsk2jgoPKYub2NK8fmwjFLfZYaH3pQWrObjhFdt9n1fZH9_-8rht7hHCKBuwAad3Crd-cLjSBioMNajSXoIRzmTwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونالدو بعد از 3 سال و از دست دادن 14 جاممممم بالاخره با قهرمانی تو لیگ عربستان اولین جام خودش رو با النصر به دست آورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132006" target="_blank">📅 10:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132005">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
اورونوف: با پرسپولیس قرارداد دارم و فصل آینده در این تیم خواهم ماند، میخواهم با پرسپولیس قهرمان لیگ و آسیا شوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132005" target="_blank">📅 10:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132004">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
امیر قلعه نویی و امضای پیراهن تیم ملی با جمله تقدیم به ابر ملت جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132004" target="_blank">📅 10:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132002">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">- همه اون لحظه‌ای که سایت نصفه لود میشه و VPN قاطی میکنه رو تجربه کردیم، مخصوصاً وقتی وسط بازی یا ثبت پیش‌بینی باشی.
😑
- ربات رسمی تلگرام وینکوبت کارو راحت و ورود به سایت رو آسون کرده:
👇
-
🤖
@Wincobet_bot
-
🤖
@Wincobet_bot
- برای کسایی که بیشتر وقتشون توی تلگرامه، خیلی کاربردیه.</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/132002" target="_blank">📅 01:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132001">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
ورزش سه: روزبه چشمی از ناحیه رباط صلیبی مصدوم شد و جام جهانی رو از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/132001" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132000">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tyq7eY43soFzxc7NJQSkAmU1tLMf5nvNqSvJzzKqWNpXAdyFn5XDVovvvtLcVO5QprzBjrLtSeChZlR9MAiZDUzbuQ8x1LfgoIYlODf1D2ql9mUfX0YQFyntlj-gMxGDepEfn-I8hiMJxkFcDVhBHjY42DshAbZ7tw50z59Xa9RRfcDYqACvsKuWYW-SHlbjsIxVmJOEJlF56i44FpPrAxc6OFNhPYyReyYJ6lEFfbxl-kVkcqlNV6qxRmnWVnbmuC0tnY0cXaEK9X_At2_onk5oOUyQZdy4MaMKh8zmDvw-sWJr4NXecv169K-XS0vpXhnnLe5zs7ZNcCH-FLFSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇵🇹
رونالدو به اولین بازیکن تاریخ فوتبال تبدیل شد که در 4 لیگ مختلف قهرمان شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132000" target="_blank">📅 00:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-131999">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا شوکتی</strong></div>
<div class="tg-text">درست میگه دیگه
زمانیکه یه عده داشتن از امثال سروش رفیعی حمایت میکردن و داشت پدر امتیازات تیمو در می‌آورد، بایستی فکر همچین روزی رو میکردیم</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/131999" target="_blank">📅 23:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131998">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
‼️
مجوز حرفه ای باشگاه صادر شده ولی خبری از شرکت تو مسابقات آسیایی نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/131998" target="_blank">📅 22:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131996">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PWhkwm7Uq19XNCmSGMq9sVTHkbuBYCB6lVT5-oFk4hlaXe9j4FtIaur50QS3bVYgCbet5rrDLhGoasW-S9G8oyf3pLkwI8juYJlH05pb3vk13JVBe1HfZEK9sP7lCcxnACKV_LYhy6lOlIGDu6jsYX0ttLpFSJVhwuCNawCRES7SrOHVRqb14grxfqtNySTNklAGdiX_y3FIIjYsLqAB8Yj_q1PluwCICV4ZCTGzYjJo0CdSZhyHwV5KOQ4mfjmfQe5o_A7rqoQajUrrWSdQZ3WmGPTh-zcOqh6IGrR-_HnVSNqUoe1iVXV_8P60AzhKatBYa2d9yyv7J6o4QGKAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی
| العربیه : پیش‌نویس نهایی توافق مورد انتظار بین آمریکا و ایران که طی ساعات آینده برای توقف جنگ در همه جبهه‌ها تنظیم می‌شود:
🔴
۱. توقف کامل، فوری و بی‌قیدوشرط آتش‌بس در همه جبهه‌ها (زمینی، دریایی و هوایی).
🔴
۲. تعهد دو طرف به عدم هدف‌گیری هرگونه تأسیسات نظامی، غیرنظامی یا اقتصادی طرف دیگر.
🔴
۳. توقف کلیه عملیات نظامی، فعالیت‌ها و جنگ تحریک‌آمیز رسانه‌ای.
🔴
۴. احترام به حاکمیت کشورها، تمامیت ارضی آنها و عدم دخالت در امور داخلی.
🔴
۵. تضمین آزادی دریانوردی در خلیج فارس، تنگه هرمز و دریای عمان.
🔴
۶. تشکیل کمیته مشترک برای نظارت بر اجرای توافق و حل و فصل اختلافات.
🔴
۷. آغاز مذاکرات درباره موضوعات حل‌نشده حداکثر ظرف مدت ۷ روز.
🔴
۸. لغو تدریجی تحریم‌های آمریکا علیه ایران در مقابل پایبندی ایران به مفاد توافق.
🔴
۹. دو طرف تأکید می‌کنند که این توافق در چارچوب احترام به حقوق بین‌الملل و منشور ملل متحد است.
🔴
این توافق از لحظه اعلام رسمی آن توسط دو طرف، لازم‌الاجرا خواهد بود
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/131996" target="_blank">📅 22:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131995">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
ورزش سه: روزبه چشمی از ناحیه رباط صلیبی مصدوم شد و جام جهانی رو از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/131995" target="_blank">📅 22:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131994">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوتبالی: علیپور مذاکرات مثبتی با حدادی داشته و از لحاظ مالی توافق کرده و اگه اتفاق خاصی نیوفته بعد جام جهانی تمدید میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/131994" target="_blank">📅 22:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131992">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
وکیل بیرانوند میگه پرسپولیس پولی برای رسیدگی به پرونده(هزینه‌ی دادرسی)پرداخت نکرده و ادعای باشگاه کذبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SorkhTimes/131992" target="_blank">📅 19:15 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
