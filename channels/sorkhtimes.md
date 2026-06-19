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
<img src="https://cdn4.telesco.pe/file/sFw0xdcMFxYsODGSTi_kFLM-1bLwCpBRYV3o0IaNuoyo4UTvWHsF4qzm17hzM1oeUSBtPvUiF2mJNqqfqNkdEReWeDLg69-tDp3UgKLs_x7uEEJmiJ8OlYD7UtA3VhdRIxfUN9YRYNPuIhs4ysvuCUbk2C4QcgCjkm9nVWLkKs7Ew0ROxoixfcFesBxDVMFwBeQUUa9xx1FU9lg3MYnn0rjHcM-F_Nx5D_iOWvW4DPog3s5w3ZYk4EDMbJ56Arv9rgF-CaxEi18Hr89rTLE9cPZR8_X7_x9UZ_MaUHMJ9BU58wVvNXz_GNzxQVDjH7Gp2umCLwCx6bCTEVbv9baR5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 09:01:53</div>
<hr>

<div class="tg-post" id="msg-133840">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj4iqMnJwCZxiXYbK_WQFcCu9AHNaMPpmrvlFaHTw6z10cK00BZEfRhX3Fe9ZjzWHjZSD68jmB91x3jV28VLF3OBrSFt77oOlGTDVBOU8rnlCJqMUPMaPu-pMR5TqvDzoWQNAuA4IqLlJLVMebCGs6cV3n5PrFzsKEViFrPNeyyfGzoTRbFekRv3CMEHFh3zVVoJMAwXSlg-FjHT31cjOUYcsIrSqL98NK_NEjdoc_Yn-zIVkdv4Mr-_7mOaOs-yMeNMbeN0mcCayGAOUmy8vfNqQfCtkXCWOv421bOVE8TtPyGkoUUYEv48_JwiPBZkjYxo7waCcbN2tJcm5YEj5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه A جام‌جهانی ۲۰۲۶
[
مکزیک
🇲🇽
🆚
🇰🇷
کره‌جنوبی
]
⏰
بامداد جمعه ساعت ۰۴:۳۰
🏟
استادیوم
آکرون
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SorkhTimes/133840" target="_blank">📅 01:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133839">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
کسری طاهری با قراردادی یک ساله و قرضی از روبین کازان به پرسپولیس پیوست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/133839" target="_blank">📅 01:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133838">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/166bff416e.mp4?token=sArildA3xxuaI4wVo8rigoXBAuefhRf8GWOR3CNO09AwEPiFZVuAUs2zF9oG7vjXMsCSS0rRXMdlFeYLFTEjFPyCJ-xG6TFdjSGeI4iLC09Dp7EWmPS_NUxQutzDW9SJz_qOrAdUZJcI0DE47yDvYg7GdzmRM1OBePMmEgawAFOclpPyF77Ev0je4fv0PN-RFXDW_pGV6oxmbIhTNhTRG-tzV1pzEHV4pZWhBjwgKrWxYyhYOgem2T_84W8CGtNio4I8W8HPeYGbgvE5OP6w2xFvHwwYJb4TZrxV3k0GWVJVARVsyCFbrrbc9zBgogP1pdHRMuxcZKkL9KAMca3YlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/166bff416e.mp4?token=sArildA3xxuaI4wVo8rigoXBAuefhRf8GWOR3CNO09AwEPiFZVuAUs2zF9oG7vjXMsCSS0rRXMdlFeYLFTEjFPyCJ-xG6TFdjSGeI4iLC09Dp7EWmPS_NUxQutzDW9SJz_qOrAdUZJcI0DE47yDvYg7GdzmRM1OBePMmEgawAFOclpPyF77Ev0je4fv0PN-RFXDW_pGV6oxmbIhTNhTRG-tzV1pzEHV4pZWhBjwgKrWxYyhYOgem2T_84W8CGtNio4I8W8HPeYGbgvE5OP6w2xFvHwwYJb4TZrxV3k0GWVJVARVsyCFbrrbc9zBgogP1pdHRMuxcZKkL9KAMca3YlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مازیار زارع:
✅
پس از مصاحبه‌ام علیه داوری فینال جام حذفی، علاوه بر اینکه حق تیم‌مان خورده شده بود، ۲ میلیارد هم جریمه‌ام کردند!
🔴
هرکار دیگری می‌کردم، دیه‌اش کمتر بود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/133838" target="_blank">📅 00:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133837">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
فاکس نیوز به نقل از مقام کاخ سفید: مراسم امضای رسمی تفاهم‌نامه که قرار بود در ژنو انجام شود، پس از امضای آن توسط ترامپ و پزشکیان، لغو شد
🔴
این توافق هم اکنون لازم‌الاجرا شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/133837" target="_blank">📅 00:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133836">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
تسنیم: اوسمار تخفیف نداده و تا شنبه تکلیفش مشخص میشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/133836" target="_blank">📅 00:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133835">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyW9b2xDQb0Fo1uqMNkyE4tBqd4v0YjySjh2_vKPaDRlLyVzyvMiWvC4XjyZSNKtmfWY1Qeap5KTZsoM6E6p3bsL2e1F1yoaWWDcvLHS2d5OPyhdxJtBw4wr4Yh17Lysj75190p8gf6XbKwylXqTAnrD2mgBFtet-DFSYhFqpxfLxCYuvFlDP7gG51cGPwu19ppxGoSgxtpMXM9hTHNvRBVNBMB_SRMfBzV6gkSeFWozeSVxJ3WQ-vpm-Q_o77DwOoRkSRxEwIeBVKbfDrwJgSuSltYh5YjhwaEuBUR5VZaUTTeFoY8PuQfTSfheQLGGcZrFcEiEOK_YSL7c6kSQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
روزهای خوش در 36 سالگی!
🇮🇷
فیفا، رامین رضاییان را به‌عنوان خلاق‌ترین بازیکن دور نخست مرحله گروهی جام جهانی ۲۰۲۶ انتخاب کرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133835" target="_blank">📅 23:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133834">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔸
شنیده ها
🚨
🔸
میگن فردا از کسری طاهری رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/133834" target="_blank">📅 22:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133833">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
اوسمار برای توافق جدایی پول زیادی می‌خواد!
🔴
اوسمار توی تایلند زیر ۵۰۰ هزار دلار می‌گرفت، وقتی برگشت پرسپولیس رقمش رفت بالای یه میلیون که همون موقعم بابتش باشگاه رو زیر سوال بردن.
❗️
حالا خبرنگار آنا می‌گه اوسمار یه میلیون و هفتصد هزار دلار می‌خواد! پرسپولیسم…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/133833" target="_blank">📅 22:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133832">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXIVGbm5rtAfir14XzhjQ_4jhFHDdNW3axQfBTTUzkAlY8cKyXIjMvhhZrskkme8SBXAyY0ETFvnd7JP6TTfgbnHj6neKST7ehX8rb4mJ2SkR9tGXIdk-wNmdLBxbDn0rO-TWUB7ZGU65Lz7c9PO2hRmsZv2No1Br8DxpszMXdOSgpAB9XF6uDfC3WUpxWaNKWBV38VYMzmuoUBj_f353dc-PRQbTlMa-FFsWMoklxOPUXNu2tt5WWgKZWJj7dIhmycEBhDagP8wliFUc0vzgpBmsLxwCRqNCHuE0gsDA1xtNIC6Asi_o82fdLG1xaOU6Jkar2MLB3af_dajk9AzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
الهیار صیادمنش در تست های پزشکی لخ پوزنان لهستان شرکت کرد تا به زودی هم تیمی علی قلی‌زاده شود!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/133832" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133831">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔸
🔸
اوسمار و حدادی به زودی جلسه میزارن و راجب درخواست‌های اوسمار برای تمدید و نقل‌وانتقالات صحبت میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/133831" target="_blank">📅 22:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133830">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNL9MalrK4euFbUquMVqsJeD-nGkC8cde-UIs9vlZiZS0KW1DaINEfIv4xS6M2ew1TGRlK4DQAKdrozch1YL6_QS3f11LWZ5SKI_ht6IgsXpZtaNSUFpxQNNYInY0t9wKelVMY_A5KeLnX2xoxlObPBnu51z1sH9h3niM53pzCZgdk4KSrFvWCUbZp1j14W31GZx2CYJ66mEm6RK1ItDVpNK-GfGPANcxep0Wo8yw86PIxkrCy7Twxgg2sy2mwmcf_6gBjnUUYtXVsmkLx6s0tXGWIxAGebkevhnyb02gVwN3pSA5WZSYexFJ_wN1ULkTAtqPI_3ib15gDbsFoERFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/133830" target="_blank">📅 21:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133829">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38845ba49a.mp4?token=ajRIVoOdKI2Fp5taozczGfkH-wVyOdG18irUBoJK8jUlG6x3TklDy_D7D5l_tyVnAc6pI59FJNriYJhHYZiUALiJdjk18yfTmZc8EFyMfFAqCQsKK_ieF_boJN5o6mMsVshS1CzTcsogoMeelCurzHV4-63qWrv289uEIONN060bSh32TkG7DliF2XAI4epk9Ccs14xTd86S85KsIQ4swfCcispov1xWBYe5b9OxK6ALagBq9414smtiBXIXP2f9lZVytF03y9stPEsIdiYp2T4QOCkQHt2cZBTX-lnxnbMscKL13sWXSd6s7aLjZ9si-2c7E8pib6SD0eQRrQnozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38845ba49a.mp4?token=ajRIVoOdKI2Fp5taozczGfkH-wVyOdG18irUBoJK8jUlG6x3TklDy_D7D5l_tyVnAc6pI59FJNriYJhHYZiUALiJdjk18yfTmZc8EFyMfFAqCQsKK_ieF_boJN5o6mMsVshS1CzTcsogoMeelCurzHV4-63qWrv289uEIONN060bSh32TkG7DliF2XAI4epk9Ccs14xTd86S85KsIQ4swfCcispov1xWBYe5b9OxK6ALagBq9414smtiBXIXP2f9lZVytF03y9stPEsIdiYp2T4QOCkQHt2cZBTX-lnxnbMscKL13sWXSd6s7aLjZ9si-2c7E8pib6SD0eQRrQnozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
خداداد: هنوز با پرسپولیس قرارداد امضا نکردم
💢
درمورد اسکوچیچ هم از نظر فنی و اخلاقی واقعا حرف ندارد؛ هم در تیم ملی و هم در تراکتور نشان داد مربی قابلی است. اگر پرسپولیس او را جذب کند برد کرده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133829" target="_blank">📅 21:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133828">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭕️
⭕️
⭕️
🚨
🚨
🚨
🚨
🚨
دراگان اسکوچیچ سرمربی پرسپولیس شد/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/133828" target="_blank">📅 21:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133827">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
فاکس نیوز به نقل از مقام کاخ سفید: مراسم امضای رسمی تفاهم‌نامه که قرار بود در ژنو انجام شود، پس از امضای آن توسط ترامپ و پزشکیان، لغو شد
🔴
این توافق هم اکنون لازم‌الاجرا شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133827" target="_blank">📅 21:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133826">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvrj5TCne25OJBO8aAVkCmuwYEvs9otreG7ZK1ipZu0AWI7vKlaReRoqie1RCbh65sR2end_C7-Kce37Mc9Eff5d0npRQGk35rzVtnsuqp3mafgoWiV6V-jjnnVYtacxJWL36hrVNsPyxE2VHyTef3trA0YqR_W13rrk_RjkIC3rolqwgSpOGIV1nj0ulUegPnodJ8Tz3jPx4qVpSr74tfqlbHw88CdL4iouaRbj3m5YLRMSyp5Q_b2uYHYJDHB44lWFjuCgH6mq6u0ul3e3BSykCrnVjykYDnzQLSSAFfLataw2pR98Ehs15S6kSow5FIUe0sXzQT9t_U75h5Kqyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اوستون اورونوف و ایگور سرگیف اولین خارجی‌های تاریخ پرسپولیس هستند که در حین عضویت در این تیم در جام‌جهانی بازی کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/133826" target="_blank">📅 21:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133825">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
خبر ورزشی : اسکوچیچ از پرسپولیس در خواسته قرداد یک میلیون و هشتصد هزار دلاری داشته و ظاهرا حاضر شده ۱۰۰ هزار دلار تخفیف بدهد و هپچنین مقایسه با پیشنهاد استقلال  این مربی قیمت دستیارانش رو کاهش داده
🔴
🔴
و در صورت عقد قرداد با پرسپولیس سه مربی اروپایی به ایران…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133825" target="_blank">📅 21:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133824">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
🔴
حبیب کاشانی: برای حضور در پرسپولیس با من صحبتی نشده است/  برخی می‌خواهند خودشان بیایند اسم ما را مطرح می‌کنند
🔴
با من صحبتی در مورد پرسپولیس نشده است و دنبال سمت مدیرعاملی هم در این باشگاه نبودم.
🔴
پرسپولیس باشگاه بزرگی است. من با همه علائقم پیگیر باشگاه و نتایج تیم هستم.
🔴
نه صبحتی با من شده و نه من پیگیر بودم.
🔴
برای پرسپولیس آرزوی موفقیت دارم. برخی نام ما را به رسانه‌ها می‌دهند درحالی که هدف دارند و شاید افرادی به دنبال این سمت هستند و با مطرح کردن نام دیگران و استفاده از نام دیگران فضا را برای آمدن خودشان مهیا کنند.
🔴
این‌ها شبیه بازی است و صحبت بیشتری نمی کنم و امیدوارم پرسپولیس به آرامش و روزهای خوب خودش برگردد.
🤩
خبرگزاری آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/133824" target="_blank">📅 21:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133823">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKOclNjDll3ErIWM3VoFqGrncMmEaR_MmAipywFZQyT6RN7omMnFCWG69ZfuJ2QZpGGV_YuDJbT4ggamiB_hcPv7w7Z-L4KOerNSd27xWOcRKneVB00Y_Bl0ss0P8PHPIS1SMRBGge1Xy8IyL6ZC34um9nPtkj3BVlh6gyZGENTa3KAUFNJZg_YsmzFmN4goa597vSGEFeI6-ksYgvw6TuGr73gEp3S19j5xrAMcoOGu9fCDg3SkGO43QgglueiyrQjqDvagu1ys-TfdgNM314HCBbXYUUN9axcGl2u_9jato6oCdYPX9CWK2QORCZRwlr_xaDeIvgKT276vwkOBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه B جام‌جهانی ۲۰۲۶
[
کانادا
🇨🇦
🆚
🇶🇦
قطر
]
⏰
بامداد جمعه ساعت ۰۱:۳۰
🏟
استادیوم
بی‌سی پلیس
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
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/133823" target="_blank">📅 20:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133822">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔹
حمید استیلی : با وحید هاشمیان صحبت کردم و ایشون گفتن که آقای انصاری بعد از تمرین گفتن که دیگه نمیتونیم در خدمتتون باشیم
🔹
ناراحت بود از این مسئله اعتقاد داشت که فاصله امتیازی ما با تیم‌های دیگر خیلی زیاد نیست، پرسپولیس از صدر جدول سه امتیاز فاصله دارد و حتی…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/133822" target="_blank">📅 19:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133821">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭕️
⭕️
⭕️
🚨
🚨
🚨
🚨
🚨
دراگان اسکوچیچ سرمربی پرسپولیس شد/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/133821" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133820">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
پرسپولیس و مسیر جوانی در تیم
♦️
شاید بعد از چندین سال بسیار واژه مسبر جوانی برای سرخپوشان مهم و حیاتی باشد چون تیم از لحاظ میانگین سنی در وضعیت بسیار بالا قرار دارند و شرایط ایجاب میکند که در فصل جدید به جوان گرایی رو بیاوریم تا از لحاظ سبک بازی هم شاداب…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/133820" target="_blank">📅 19:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133819">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
بازگشا: اطلاع رسانی لحظه‌ای نقل‌وانتقالات به سود باشگاه نیست صبوری کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133819" target="_blank">📅 18:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133817">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
🚨
حبیب کاشانی مدیرعامل باشگاه پرسپولیس شد/ فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/133817" target="_blank">📅 16:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133816">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtKQ9ItXwJNhErqyMKRR15rhotHTBpMSNDH_7MAa-eOthvlSKkWamygE4lU_TPLQdNOWdTyYy6TxF4nPVyGMW5jk3qPWf_BMoKcTCEs-dpy7tMFFnTghYeTBS87J6S7wLAr8bo6r_d9YclCoe8zI2QkHMLamZqqg2hwEupLBFVYUbgDull27Q-66KvBWo4vDfzRwVtBMqESLvS8vBnqGXo8wqcwh691nXeoVX-zVfkI7o6dbcfYNFRkX7oenl2Ca6hkrj1SbqcuStN7loWLYQXNvcIu2QI962YfYk6d57XMuexJ0fZ9ESxbWkjbpEf2LGKim0wo4H2rqzy3Yipz_UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تصاویری که از محمد محبی در حال پاره کردن تصویر مهسا امینی و شعار زن، زندگی آزادی است، فیک و ساخته شده توسط هوش مصنوعی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/133816" target="_blank">📅 16:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133815">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmQUiYYiBixJDDEWGIUTRFgImCF6ACAoG-IPfkC0ruZbUgqoV32db-I33F-8Fa-DlCvu65vJBb0IWJbWt__gA5n2frLvt5ZDhw4piolWPDA3yG1PCk5Mj5Qh2VrZsUWoO9piJNsIP5wI3zDILyw2Kr1cnidUTto9e1PvjJ-UxhvHiRVPyWPJ3yhFlHYkgvhwAZeAOBlt7klttSDZ--iiMaGRbDqIf4GqNZh5nP_elV4ycZdTzN42ShYa7wG3sKxQfk3hpGAxaVkLCgj8lmzI8cnGVnFapZSLcLADSzDoTc9DeSZLXqykbmlL4BvHNyQrYG0AgAe4wXaUhO_HL_K9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازگشا: اطلاع رسانی لحظه‌ای نقل‌وانتقالات به سود باشگاه نیست صبوری کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/133815" target="_blank">📅 16:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133814">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
خداداد عزیزی که ارتباط نزدیکی با مدیران سهامدار عمده باشگاه پرسپولیس داره و بخاطر همکاری موفق با اسکوچیچ تو تراکتور، گفته زمینه حضورش تو پرسپولیس رو فراهم میکنه / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/133814" target="_blank">📅 16:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133813">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[💠🍃 ғᴀᴛᴇʜ ᴬʳᵗʷᵒʳᵏ ]</strong></div>
<div class="tg-text">یادمه کریم باقری رو ترنسفر کرد و گفتش ابرام اسدی فقط پنج درصد با کریم اختلاف داره!!!!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/133813" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133812">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3oQlwMrujocQ_q4GexlufIVGxFwljivg_ob7F4OKYyKA-TDE6YIT5ksNuTrlTkjpWXgfFrhPwWqmg0kV9R_Hh093Rutg7H2POREkqFvfseXx-jbBwGKHvLE4o-tHBTbNMlg4V6AUOSej_QWzJYkppdUEtghwDA9LGf_6agKV_m8UhlV6Y9TKliS3OPkKKBCJvFZceADJDqWMjClR7Q3-0fe88NM9d9_jGus6WmHEnnLEznqiA5hlbvyQQrTuSQ48AwZb_ek4pCWWtuqvxbjhp6Eh3akjkSTSCooyNPaWAlIhVVIi8_Xl8iYgV3NVFtLFT6mzGMRPkBSKEgskkx2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇿🇦
🇨🇿
تو بازی امشب آفریقای جنوبی و جمهوری چک ، سه داور زن آمریکایی برای اولین‌بار در تاریخ، داور یک بازی فوتبال مردان میشن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133812" target="_blank">📅 15:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133811">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
🚨
حبیب کاشانی مدیرعامل باشگاه پرسپولیس شد/ فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/133811" target="_blank">📅 15:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133810">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommilaad zd</strong></div>
<div class="tg-text">یادمه استقلال جاسم کرار رو گرفته بود جانواریو مجتبی جباری برهانی خسرو حیدری این اقا اومد تو برنامه نود تک تک جملاتش یادمه گفتش کرار بمبه مگه؟ جباری جلوی  کریمی بمبه مگه؟ با یدونه خرید کریمی داشت پز میداد فتل بازارو جارو میکرد</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133810" target="_blank">📅 15:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133809">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خداداد عزیزی
، سرپرست
حبیب کاشانی
، مدیرعامل
یهو
حمید استیلی
هم سرمربی کنید
یاد دهه هشتاد زنده بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/133809" target="_blank">📅 15:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133808">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝒎𝒐𝒉𝒔𝒆𝒏</strong></div>
<div class="tg-text">به خاطر ۴۰ میلیون بدهی ۶ امتیاز ازمون کسر شد تو دوران این ادم</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133808" target="_blank">📅 15:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133807">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from@M</strong></div>
<div class="tg-text">ارش برهانی تو باشگاه  پرسپولیس باهاش امضا نکرد رفت استقلال</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/133807" target="_blank">📅 15:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133806">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⚠️
هوادار هم باهوشه هم حافظه خوبی داره، بخاطر همین نظرات مردم رو گذاشتم تا چشم گوش عزیزان باز بشه اگر دارن شیطنت میکنن….الله اعلم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/133806" target="_blank">📅 15:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133805">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommilaad zd</strong></div>
<div class="tg-text">کاشانی سیستمش اینطوریه که یدونه ستاره میاره با سن بالا اون زمان (علی کریمی) بقیه بازیکنای معمولی و دلالی اون زمان فشنگچی میثم بائو نورمحمدی و امثالهم رو کرد تو پاچه تیم سپاهان و استقلالم هرچی بازیکن تاپ و درجه یک بود جمع کردن تو تیمشون</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/133805" target="_blank">📅 15:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133804">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromhossein</strong></div>
<div class="tg-text">همین حبیب کاشانی تیم ملی امید رو داد دست عنایتی و نابودش کرد
بعد رفت سایپا و اونجا باند دلالی تشکیل داد و سایپا رو نابود کرد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/133804" target="_blank">📅 15:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133803">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromH9009</strong></div>
<div class="tg-text">ادم نمیدونه بخنده یا گریه کنه
اون زمان که نصف تیم ملی تو کیسه بودن و نصف دیگش تو ترکیب سپاهان بودن این کاشانی با امثال فشنگچی و مجتبی شیری و سامان اقا زمانی و شوهر خاله آرام میخواست با اونا رقابت کنه
که نتیجش شدن سوبله چوبله شدن جلو کیسه</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/133803" target="_blank">📅 15:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133802">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from@M</strong></div>
<div class="tg-text">گه ترین مدیر تاریخ پرسپولیس
هیچ وقت یادم نمیره ستاره ها نیاومدن پرسپولیس ابن حبیب جدا می‌گفت پول نداریم
مهدی رحمتی خودش مستقیم از اصفهان اومد باشگاه این مردک گدا گفت پول نداریم بلافاصله استقلال خریدش
آقایون خواهشاً دست به یکی کنید کاشانی یعنی نابودی پرسپولیس</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/133802" target="_blank">📅 15:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133801">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromع ر</strong></div>
<div class="tg-text">امیدوارم مدیرعامل صد در صد تحصیل کرده و عاشق و پر کار پرسپولیس عوض نشود و این اخبار شایعه باشد
از بس دنبال حق پرسپولیس بود زیر پایش را خالی کردند
یک زمانی هم آجورلو با ناحقی  در افتاد
ناگهان حق کله شد</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/133801" target="_blank">📅 15:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133800">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromR...</strong></div>
<div class="tg-text">حدادی بهترینه باید حمایت هوادارو داشته باشه</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133800" target="_blank">📅 15:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133798">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
🚨
حبیب کاشانی مدیرعامل باشگاه پرسپولیس شد/ فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133798" target="_blank">📅 15:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133796">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔸
🔸
اوسمار و حدادی به زودی جلسه میزارن و راجب درخواست‌های اوسمار برای تمدید و نقل‌وانتقالات صحبت میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/133796" target="_blank">📅 14:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133795">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔻
🔻
🚨
فووووووووری از رسانه های ترکیه ای
🔺
اسماعیل کارتال با تراکتور برای حضور در این تیم صحبت های اولیه داشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133795" target="_blank">📅 14:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133794">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEpHgYdVe79BLVG6LYZaU7W1KZdfvkE4WVJSil2Eos8rZiexRKeo7QY1DthhEKlRsRvDe7UvVgB60wptaI2gTVArNZyTs2eKa0LV3aQO8UU9wP9Tn_d5yDSzT1zTbjaCgzuMmqPgcg6wRs2oDjbhGWJXDo40qTDnkpF8CBXkAqXRmNuHnUNFW-uLdtRM9rgSKra8sj3ptwy2gycm-6JWkd7QEcpMMs4VNp0ZnMCxD-d8bXh2vbTbM-Mvg6FWRcFZxiEYIhzUIKp-tpgALn4CcPKZU_-l_SLHEwWiKfp-3vg8Ew7K-TQ6wpNDQ4Lr0KBasZ6m_C8fIJMMn_wXy8Cl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه B جام‌جهانی ۲۰۲۶
[
سوئیس
🇨🇭
🆚
🇧🇦
بوسنی
]
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
استادیوم
سوفای
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
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/133794" target="_blank">📅 14:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133793">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgXXF3XQ7TcYd_cVCEnMwGg0gK8a1v7u-X1ivzaXQT2ZyiscIxTpv7vcSBih-oqJ6DEe2AdBmRvxrKQx1Dg6ZB8Ec5UiY0u6mWbvd2ofArZeV1uMREmZU-TJ816Z7TUgbSArtuw2bRPw_F1KEY-G4FYb3erlVn2qmjjswajn_bRUeEwLg8Jv0E7jf1PyRK_vpc4bQOxa9nfQSKiY29Ld8SlcGspMNaOFG8O9_sZqh9Bp_chmvhyUNV3SKr6ibmdmdwHQDQcUVtNrkstpDDtOV2d2gsI2tGdY34O-q-HzBXPGUVkzjVyAzQoyVvHMr0v93YiPzyx6Mql2MbnrVgTrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
تصاویری از تمرین سبک تیم ملی در هتل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133793" target="_blank">📅 13:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133792">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
دراگان اسکوچیچ به عنوان سرمربی جدید باشگاه پرسپولیس انتخاب شد. دو بازی بعدی، بازی‌های آخر اوسمار ویرا بر روی نیمکت پرسپولیس خواهد بود!
❌
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/133792" target="_blank">📅 13:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133791">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
ایرنا خبرداد؛با تصمیم هیات مدیره و بانک شهر اوسمار از پرسپولیس جدا و اسکوچیچ جانشین وی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/133791" target="_blank">📅 13:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133790">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
تیوی بیفوما وارد تهران شد
🔻
تیوی بیفوما، امروز (دوشنبه) و لحظاتی قبل از مرز هوایی فرودگاه امام(ره) به تهران رسید تا از فردا به جمع سرخپوشان بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/133790" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133789">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⭕️
⭕️
⭕️
🚨
🚨
🚨
🚨
🚨
دراگان اسکوچیچ سرمربی پرسپولیس شد/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/133789" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133788">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
اسکوچیچ با پرسپولیس به توافق کامل رسید و پیش‌نویس هم امضا شده. او به همراه خداداد عزیزی رونمایی خواهد شد؟///ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/133788" target="_blank">📅 11:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133787">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItZKtpPYYVGEep6NgNOXpmAja9yNDMOazECxKt05N8GgjRNflZUtpekiRyKbmJBOgc3uxUzrybuIVf9jimPtu5hYsvIkp8D_wcBFboEIzwn2hNIggQis1NiCZ9XwPL0sGVWsz9rzopxpoBOaX6OyKtYJvADqOo_1I6mWbYDILemWLgTiV8Zj4k2t1Gl-jR49COOY_3pvJ4ynp3zq42mtmP8Jho2rTR83TVbza-5XYeo_jLCWSqlGcytRhITOAuoLLpjp0HAv8e9Hg82OZAa7zXFvh2kPxFuLCq_Ddh0h4n1xxKQRD-aqSz8DynzUpPv3NJrHXbBqGT75EP4XsZtYLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
اسکوچیچ با پرسپولیس به توافق کامل رسید و پیش‌نویس هم امضا شده. او به همراه خداداد عزیزی رونمایی خواهد شد؟
///ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/133787" target="_blank">📅 11:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133786">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtbaTUjxqZLZvMmJGRCqAvfAaPla1tAV2U-eO2nTLNk7GhIzVUODRMLkNhMuHikEqqnKkKyffpQRhBbaNlKxl0FUTzR2ZORcitD2kbPS88mOJF294F8V3c2ICyx24gFNxZNsWfqI_ul0CXO9YhptWGZsw8uLvOcK1tBJ04W44vVhu0_NMy2yMKpMhPXM2btg68Eye1DcJZVFqIkwsE9hzv4zyOP2gEvL1P3mxjQ0BXJ_4WUZp5uQJACZPF1RFHMr0i5FgDC4v_0NMDnp4MDrJxRPxU4pyTo2uLWRo4_mhOnbW7qECBC1wVY6-ySr7iYLbkC7pd6D-RjvxXacV9F6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی12گروه رقابت‌های جام جهانی در پایان هفته نخست؛ از امشب هفته دوم شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133786" target="_blank">📅 11:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133785">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
رگی لوشکیا، بازیکن تیم تراکتور ایران به الظفره امارات پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/133785" target="_blank">📅 11:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133784">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
سپاهان و تراکتور دارن پشت پرده می بندن که آریا یوسفی و لیموچی به پرسپولیس نیان!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/133784" target="_blank">📅 11:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133783">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84f37be82.mp4?token=hc2AKYNVgEgIAJCbhOOs2IxlfcPu981WlsfypgqMXXoCG1AaIQhzCApjrBWEu7Z4n1zpiU65m2ICATyT-GzVlRDOkAGRvADQS5oha0uudQhW3DcKLwyt2PhEFDbOflz4ys7krGPw5SfMFuPahNcJEgqqtYJqTBHdsfcUTS7XdXQ5NCySjrufZziV8h8pDLKj3MPZENXyK0CVYnagCaysO2b_kWtncesBoq6LZeYINnpeJQ2ThVhPucwXxP8rwR4fe6YNetzy0iA1fVUTSH3pmRfPNTZ7wCdXEjGJHgVfNfUixwihk8u2lh7u8vrm18X0NxKNhusOM_bDg6-jEhM68A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84f37be82.mp4?token=hc2AKYNVgEgIAJCbhOOs2IxlfcPu981WlsfypgqMXXoCG1AaIQhzCApjrBWEu7Z4n1zpiU65m2ICATyT-GzVlRDOkAGRvADQS5oha0uudQhW3DcKLwyt2PhEFDbOflz4ys7krGPw5SfMFuPahNcJEgqqtYJqTBHdsfcUTS7XdXQ5NCySjrufZziV8h8pDLKj3MPZENXyK0CVYnagCaysO2b_kWtncesBoq6LZeYINnpeJQ2ThVhPucwXxP8rwR4fe6YNetzy0iA1fVUTSH3pmRfPNTZ7wCdXEjGJHgVfNfUixwihk8u2lh7u8vrm18X0NxKNhusOM_bDg6-jEhM68A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شادی کارلوس کی‌روش پس از پیروزی غنا مقابل پاناما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/133783" target="_blank">📅 10:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133782">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">💬
اوسمار سرمربی پرسپولیس: مدیران پرسپولیس کارشان را به خوبی انجام می دهند و به ما کمک می کنند/  دعوت امیرحسین محمودی به تیم ملی؟ ج اگر چه در لیست نهایی تیم ملی قرار نگرفت اما حضور در کنار تیم هم تجربه خوبی برای اوست.
✅
مارکو باکیچ ، بیفوما و دنیل گرا نفرات…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/133782" target="_blank">📅 10:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133781">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
امضای پزشکیان و ترامپ در کنار هم رو قرارداد توافق
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/133781" target="_blank">📅 08:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133780">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuPvX9MB5gDXf8b-itwFS_-UbnvczDM1rxOzvYDu-JKHYwU2wTwG-AAZ9YRiAaOdzoViomiOGTss6WE09Qu0jee43cNv4Hg3J0rM-P-mdkRCbgnyaCptUJTM6MUhUK0gKl4eaaYcyJ9FmLpXuj9jAGWUZ54gYVZKwAX-sr3-e1jwJ2FE75MNUZ9_PtOwLdD0dP2xBY5-QgZ5trqC9mkx4hLjSagAfJNNMfIyq3tO5RYKsyn4sxCsYAWRurhW4oiDPmpgp1TV8yZ2ycv6L7nabqRIGN-ErtfIoSeeY6-NQapJuTVHQ3hXLKRMxOJvfRRdLwfxv76xIiJAACNbLHD7fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
امضای پزشکیان و ترامپ در کنار هم رو قرارداد توافق
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/133780" target="_blank">📅 08:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133779">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/14ae173143.mp4?token=oD0LQ_YNdwpVWwg0gMwphNfMTM0Ziqu_TvqoU_Xmg9K3C_bpT8UdzQedSiXW8dCcZC2suyFYfO04V4ZEAP2J8C4SfkIVJegsqLfMqA-v57utEc1IE-WxmKjeppPvcLXNKX4So84VQh5g6voz929QyEc1jZkSRsxN_cvci73YjI_GKCsYf48UPFTzb2hCYk-2PAoCNNACJTmIYy3_oIhd92d4ew3Rg_joH8iovpm2kBasMgFolI6GuA6e1GN-50uTdOVEzSO5NU4Zu0aV5RqxjWI4VhLYXjmBaSYPzWx5-tIZ0QfGRPsUsfNJry2CwlK423LnoQ--eO3mylaR_DQuEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/14ae173143.mp4?token=oD0LQ_YNdwpVWwg0gMwphNfMTM0Ziqu_TvqoU_Xmg9K3C_bpT8UdzQedSiXW8dCcZC2suyFYfO04V4ZEAP2J8C4SfkIVJegsqLfMqA-v57utEc1IE-WxmKjeppPvcLXNKX4So84VQh5g6voz929QyEc1jZkSRsxN_cvci73YjI_GKCsYf48UPFTzb2hCYk-2PAoCNNACJTmIYy3_oIhd92d4ew3Rg_joH8iovpm2kBasMgFolI6GuA6e1GN-50uTdOVEzSO5NU4Zu0aV5RqxjWI4VhLYXjmBaSYPzWx5-tIZ0QfGRPsUsfNJry2CwlK423LnoQ--eO3mylaR_DQuEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
#مهم
| لحظه امضای نسخه فارسی یادداشت تفاهم ایران و آمریکا توسط دونالد ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/133779" target="_blank">📅 08:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133778">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔹
حیدری عضو هیئت‌رئیسه فدراسیون:
تورنومنت ۳ جانبه لازم‌الاجراست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/133778" target="_blank">📅 08:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133777">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skk_zJ_9LJzXr-9aIHRC-89CN0ZCYmMI8Zntls7He4n8U4oRqug9b1VfP8QthghvQzPeaIzRP6QLam4DIKqZ4gkC1BWqZB2btwdoW7AvntKZ-jb9esX8SIodXG88Wrs8_RNY6i7Aei74X0L0ePJ88nj6xc0qb2SIsdpqKf31pxlGJmTjSz14KeRAU2SmluKFkj3L6xyN_cPFzOzuMlaS36h9uixsZGZ0tv407pj5YtQwONXccWBycTjDelauCeu7digpk-ZqbKfTSpyojRB7YDBysjg98Flk12Sry7BobqvnpydztmYqKegKYQuGx5SU0rMS0yU1xcC4Dkm9VPd36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه K جام‌جهانی ۲۰۲۶
[
ازبکستان
🇺🇿
🆚
🇨🇴
کلمبیا
]
⏰
بامداد پنجشنبه ساعت ۰۵:۳۰
🏟
استادیوم
آزتکا
مکزیکوسیتی
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
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/133777" target="_blank">📅 02:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133776">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/133776" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133774">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🟦
🟦
فوری و رسمی/تفاهم نامه توسط ترامپ و پزشکیان امضا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/133774" target="_blank">📅 01:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133773">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⭕️
🚨
سخنگوی وزارت خارجه: متن تفاهمنامه ایران و آمریکا الان رسماً نهایی شده است چرا که دو طرف آن را امضا کرده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/133773" target="_blank">📅 01:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133772">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⭕️
🚨
سخنگوی وزارت خارجه: متن تفاهمنامه ایران و آمریکا الان رسماً نهایی شده است چرا که دو طرف آن را امضا کرده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/133772" target="_blank">📅 01:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133771">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به کرواسی توسط هری کین (P12)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/133771" target="_blank">📅 00:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133770">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">#نظر_شخصی
✅
خیلی ها از من میپرسن تو موافق موندن اوسماری یا اومدن اسکوچیچ هستی، من حقیقتا جفتشونو دزد و دلال میبینم
✅
اوسمار که فیلمش در اومد رسما و سه تا دلال دورش هستن که با اینا کار میکنه که باعث فساد و انحصار شده تو تیم
✅
اسکوچیچ رو با قاطعیت نمیتونم بگم…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/133770" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133769">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">#نظر_شخصی
✅
خیلی ها از من میپرسن تو موافق موندن اوسماری یا اومدن اسکوچیچ هستی، من حقیقتا جفتشونو دزد و دلال میبینم
✅
اوسمار که فیلمش در اومد رسما و سه تا دلال دورش هستن که با اینا کار میکنه که باعث فساد و انحصار شده تو تیم
✅
اسکوچیچ رو با قاطعیت نمیتونم بگم…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133769" target="_blank">📅 00:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133768">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
درسته با اسکوچیچ چند روزه صحبت شده ولی اصرار از طرف بانک شهر و شخص خداداد عزیزی بوده، و فعلا نه توافقی شده و نه تصمیم قطعی ای گرفته شده.
➖
آقایون دوست دارن زود به استقبال اخبار برن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/133768" target="_blank">📅 00:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133767">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏅
مرتضی پورعلی گنجی، مدافع پرسپولیس: پرسپولیس در یکی دو سال اخیر با چالش هایی روبرو شد
⏺
بازی نکردن در ورزشگاه آزادی به ما ضربه زد. از وقتی آزادی را از پرسپولیس گرفتند به مشکل خوردیم. هر وقت در ورزشگاه آزادی برگزار کردیم به سمت قهرمانی رفتیم. بازی های فصل قبل…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/133767" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133766">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6d45ae17.mp4?token=iCq4brQVU516s8xA44EckotDVlIey3aY0Ov1tUCzM5hBW4froanXebjEUGR_SNYzlManrkJNJ76djZy7jcZ4b7Hvd7yWsDdLwQAHZG-sGPfmDXC-5HEM_2TWkLBJ3WxClfD551y3xY_1AKniHUXb-ME0x331uBCv_HWqGRqKJYnF8h6vl5ohwU3r2Hv3FbFB-beHZ5FCDR9IgRMIrD6IDJJ-leaDon3Kf9MYNr0hhQT0ImpXA2jz4jXsOsW1GbjL4e79RF1fG2wrCsAWvK8o7W3806WKn0mE0qMT0QdTTwfebRsBOLCe8oh7xNRq4_-a9H5sibOXAI6s6Qwn82AB2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6d45ae17.mp4?token=iCq4brQVU516s8xA44EckotDVlIey3aY0Ov1tUCzM5hBW4froanXebjEUGR_SNYzlManrkJNJ76djZy7jcZ4b7Hvd7yWsDdLwQAHZG-sGPfmDXC-5HEM_2TWkLBJ3WxClfD551y3xY_1AKniHUXb-ME0x331uBCv_HWqGRqKJYnF8h6vl5ohwU3r2Hv3FbFB-beHZ5FCDR9IgRMIrD6IDJJ-leaDon3Kf9MYNr0hhQT0ImpXA2jz4jXsOsW1GbjL4e79RF1fG2wrCsAWvK8o7W3806WKn0mE0qMT0QdTTwfebRsBOLCe8oh7xNRq4_-a9H5sibOXAI6s6Qwn82AB2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به کرواسی توسط هری کین (P12)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/133766" target="_blank">📅 23:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133765">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNKjEMuhrIomcnQDGCD5wBo3XDi8xbWsmHebSQs531_EEB8TfFRkjZMghzJonqhasj0pSjgtMOHH0LNiu9uPEyT3dq4AKNRVtmBctnNZHYPSkIqrPsBHURI9OrcRvnElmjCwa2qPI8-x62Q5HWaQchp2QAB-AkTZgxnMS04JTMyrPEL4Hl3uH6vaKM5sFYqf113ucv1vMZajWErnBIQuomjjo5p7rmhipkfu8FBH3lXRRCSHQ6si4hy1itjaLEXZ7BlBrLJOVg48uqE0FpAu9HMYziDAV3PSEncQNWVmoH8YIiDNygvj_qfARNJpBAuSwwjwqjdfiMjXVZxhU05dRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سپاهان به مشکل مالی خورده و داره قرارداد باریکناشو کم میکنه
✅
طبق اعلام خودشون آرش رضاوند و میلاد زکی پور با کسر قراردادشون موندنی شدن اما محمد دانشگر حاضر به کاهش قرارداد نشد و جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133765" target="_blank">📅 23:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133764">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
دوستان به شایعاتی که توسط قدوسی در رابطه با اوسمار منتشر میشه توجهی نکنید،این عزیز دوست گرمابه گلستان ایجنت اوسمار هستن و تمامی مطالب شون خط دهی شدست تو هوادار رو به جون هم بندازن
🔻
اوسمار از ابتدا قراردادش ۱+۱ بوده و چیز تازه ای نیست اقایون احساس خطر کردن…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/133764" target="_blank">📅 22:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133763">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
دوستان به شایعاتی که توسط قدوسی در رابطه با اوسمار منتشر میشه توجهی نکنید،این عزیز دوست گرمابه گلستان ایجنت اوسمار هستن و تمامی مطالب شون خط دهی شدست تو هوادار رو به جون هم بندازن
🔻
اوسمار از ابتدا قراردادش ۱+۱ بوده و چیز تازه ای نیست اقایون احساس خطر کردن…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/133763" target="_blank">📅 22:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133761">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
دوستان به شایعاتی که توسط قدوسی در رابطه با اوسمار منتشر میشه توجهی نکنید،این عزیز دوست گرمابه گلستان ایجنت اوسمار هستن و تمامی مطالب شون خط دهی شدست تو هوادار رو به جون هم بندازن
🔻
اوسمار از ابتدا قراردادش ۱+۱ بوده و چیز تازه ای نیست اقایون احساس خطر کردن که نون دونی شون و دلالی هاشون به خطر بیوفته دارن یارکشی میکنن تا به هر ضرب زوری مربی که قراردادش بوده سال اول تو پرسپولیس ۲۰۰-۲۵۰ هزار دلار رو الان با ۱.۷ میلیون دلار حفظ بکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/133761" target="_blank">📅 22:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133760">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JulH6TS_GWSdfw_h-1wTo3ZbnlFDZ-zqQHIXS9ut1M1KPn4nX54DNe81321KOv2eS0Q6aN_1cyuU33-x3ZcA1kAbBCUE7rHW1ySxq0TostnZQjpg6kkAYTxgOZAgq5kHinS5R_UAMWeX9qD8MEaaN-lEFHQEqda4t47ui5fOW-HXgtStbswdjIFQsGvamdxB153nbZ7G5By2cvQcAqd6oKXvb4DnaBy5Kts035kO9oflU1v1C7NrNmBsmywdtWgzg2OhXcPXrUinK9AL9E8vr_BzlRJnX7yVACzFz72sKHAUNB_vH5Q-uW2wUIH0bEYAMhxHcphmpfkGxpkhnRdmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شبکه خبر| انتشار متن تفاهم‌نامه ایران و آمریکا تا دقایقی دیگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/133760" target="_blank">📅 22:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133759">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
😂
اولین گل تاریخ تیم ملی کنگو تو جام جهانی زده شد به پرتغال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/133759" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133757">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔻
🔻
🔻
فرشید حقیری :
⬜️
⬜️
بانک شهر تصمیم گرفته برای فصل بعد یه تیم قوی ببندد و امیدوارم در حد حرف نباشه. پیش قرارداد برای اسکوچیچ ارسال شده و تا شنبه نهایی میشه. خیلی ها از این موضوع ترسیدن که نتونن به پرسپولیس بیان یا نتونن تو تیم بمونن.
🔴
🔴
اوسمار برای فصل بعد…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/133757" target="_blank">📅 22:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133756">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🟨
پرسپولیس با چنتا از جوونای تاپ فوتبال ایران مذاکرات مثبتی داشته/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/133756" target="_blank">📅 22:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133755">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
ترامپ:
🔸
این یک یادداشت تفاهم است. اگر در ۶۰ روز انجام نشود، اشکالی ندارد، ما دوباره به بمباران بازمی‌گردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/133755" target="_blank">📅 22:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133754">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
🔻
🔻
فرشید حقیری :
⬜️
⬜️
بانک شهر تصمیم گرفته برای فصل بعد یه تیم قوی ببندد و امیدوارم در حد حرف نباشه. پیش قرارداد برای اسکوچیچ ارسال شده و تا شنبه نهایی میشه. خیلی ها از این موضوع ترسیدن که نتونن به پرسپولیس بیان یا نتونن تو تیم بمونن.
🔴
🔴
اوسمار برای فصل بعد…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/133754" target="_blank">📅 22:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133753">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
گفته می شود په په لوسادا مربی اسپانیایی پرسپولیس اعلام کرده خانواده اش تا زمانی که جنگ در ایران تموم نشه اجازه نمیدن به ایران بیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/133753" target="_blank">📅 21:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133752">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
بررسی داده‌های سامانه‌های پایش اینترنت از جمله رادار کلودفلر، نت بلاکس و رادار ابرآروان، نشان می‌دهد که اینترنت ایران در حال حاضر در وضعیت پایدار قرار دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/133752" target="_blank">📅 21:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133751">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
کریس رونالدو کاپیتان 41 ساله پرتغال : من میتوانم چهار سال‌ دیگر بازی کنم و در جام جهانی 2030 نیز حضور داشته‌ باشم. حالا حالا ها برنامه ای برای خداحافظی از دنیای فوتبال ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/133751" target="_blank">📅 21:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133750">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔸
🔸
🔸
🔸
ایران ورزشی طی یه خبری مدعی که شد مهدی ترابی و مهدی هاشم نژاد در استانه پیوستن به پرسپولیس قرار دارن
☝️
☝️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/133750" target="_blank">📅 21:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133749">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🟨
🟨
فوووووووووری
⬛️
اوسمار ویه را به زودی از پرسپولیس شکایت خواهد کرد/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/133749" target="_blank">📅 21:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133748">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
❗️
فرشید حقیری: اسکوچیچ‌ ترکیه ست و به‌ زودی با امضا قرارداد میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/133748" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133747">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔻
🔻
🔻
فرشید حقیری :
⬜️
⬜️
بانک شهر تصمیم گرفته برای فصل بعد یه تیم قوی ببندد و امیدوارم در حد حرف نباشه. پیش قرارداد برای اسکوچیچ ارسال شده و تا شنبه نهایی میشه. خیلی ها از این موضوع ترسیدن که نتونن به پرسپولیس بیان یا نتونن تو تیم بمونن.
🔴
🔴
اوسمار برای فصل بعد…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/133747" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133746">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
فوووووووووووری
🔴
فرشید حقیری: قرارداد اسکوچیچ با بانک شهر شنبه امضا خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/133746" target="_blank">📅 21:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133745">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووووووووری
🔴
فرشید حقیری: پیش قرارداد برای اسکوچیچ فرستاده شده و به زودی امضا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/133745" target="_blank">📅 21:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133744">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
فرشید حقیری : بانک شهر تمام سهام سایپا رو خرید، از کارخونه بگیر تا تیم فوتبالش
✅
احتمالا با توجه به این موضوع پرسپولیس ب که سال بعد قراره تو لیگ یک شرکت کنه، جایگزین سایپا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/133744" target="_blank">📅 21:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133743">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRiz0PlWI-S0wbeGd-I33l6YFKyHiWbaNpmcU_M9tSOlNh_1OqRWfBoO3xf-YR6BKqJ4rIbgPZdiVg9-nz-YFoV_sMfdWYtaGbJwLTENp8mF53Mj4iIkIY3_je8mMs9v-F1a5hiDJadGUIVqVZQd5xmLliNse5Etm9Zd1y9G52ykPxKcXHu-Csxoh3oqdt_Q9tMVIQ_LQwQ4kPm9dTgy-HZvB-j4NCgRPCBL8K95nI7zFoA-Ld1mi-oJ1qCq9ptt_na26LAon1SWFxty7sd3GfotkO-7_JXjR_7_rRjtC-AGq_c5uSfm91mFgNbN4FBpCpmoPsDewsxCINtTTBGKWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🌍
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
🏆
گروه L جام‌جهانی ۲۰۲۶
[
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇭🇷
کرواسی
]
⏰
چهارشنبه ساعت ۲۳:۳۰
🏟
استادیوم
دالاس
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
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/133743" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133742">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
ترامپ: ما موظف نیستیم چیزی به ایران بدهیم، اما ممکن است برخی بخواهند آنجا سرمایه‌گذاری کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/133742" target="_blank">📅 20:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133741">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
#فوری | ترامپ:
🔻
توافق با ایران فردا یا پس فردا امضا می شود‌‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/133741" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133740">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QE1vlqz2fxv9Rbg1Gx_sBaG5YTjW2ZNWYsxV98uU0nENPknugk8a7-3LBevoBLVe_JaDea-ewh_8O7Qex7cxqcGOs7NIPF8E63LAAw3gGE4Y38HOyn3jf_goyBs0DaOprGsF32TVk8oTC3yWOmMvlUPjld-UsOmetnfl4tbKPza6vlPh57NLyLvO4Yl3rpm0QapJv_5VwnZ7Xlg071ydZdR6KnWOonlKLghJamfnK8uvAJTPmpXFaTNVGOeAYGU60gk_VjIGLHkmthYiXhqRCe4KA_vBYajLT3ORSnCrz71UWExbHEpsBMzWslLJwmvlG8XcBZ02obr4682QreAdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخلاف ادعای مدیرعامل گل گهر، انتقال مهدی تیکدری به پرسپولیس نهایی و قطعی شده است.
✅
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/133740" target="_blank">📅 20:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133739">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
ترامپ :
🔴
رهبرهای جدید ایران آدم‌های باهوشین، خیلی هم باهوشن؛
🔴
به اندازه قبلی‌ها تندرو و افراطی نیستن، فکر می‌کنم واقعاً کشورشون رو دوست دارن و آدم‌های خوبی هستن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/133739" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
ترامپ: متن تفاهم‌نامه را نه تنها منتشر می‌کنم، بلکه احتمالاً یک نشست خبری برگزار می‌کنم و آن را کلمه‌به‌کلمه می‌خوانم تا رسانه‌ها آن را به‌درستی پوشش دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/133738" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133737">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
قرارداد تیکدری بزودی امضا میشه/آنا   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/133737" target="_blank">📅 19:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133736">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/133736" target="_blank">📅 18:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133735">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
نیوزیلند از دستمون فرار کرد و خوشحاله یک امتیاز و گرفته .چون واقعا زورش به ما نرسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/133735" target="_blank">📅 18:53 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
