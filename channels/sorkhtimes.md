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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 14:24:30</div>
<hr>

<div class="tg-post" id="msg-138399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
پیمان حدادی : امیر جعفری دفاع چپ گل گهر در لیست خرید ما نیست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/138399" target="_blank">📅 14:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138398">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
فوتبالی: دانیال ایری امروز ظهر در ساختمان باشگاه پرسپولیس حاضر میشه و قرارداد پنج ساله خودشو با پرسپولیس امضا میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/138398" target="_blank">📅 14:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138397">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pt9O-lk721aiUB7tY3HMHrCXP3Yp14mh9bY4TLoIjeG8ClSO9hhIzeaV330z9DQyMspSqGE4u25eEY8LCeqbOJHV-j3GS408BcvBcVROseazgqZ80WdDdNMU1wyeftOQ9JiWJPXlQ9tEcCTSCHQ6VbViMKO3IPqXZ11qEcoLM_nPis2pdkPbjy2j6GMxbA54EluXb1MOExtqlXxR4cFuTBYH-j06gUuP46OhxIKkh9n8wAm8U9ExvA7vKyIUT2YVKnC8iljAyvLTU7XVbSojHtJv7h9auqym0vye5MhH5QZWX40d02p8T2iqefngcSTv5-PRLqbwaM1XroYdLLTWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بعداز مهدی ترابی ، مهدی هاشم‌ نژاد بازیکن تراکتور هم بدلیل مصدومیت دیدار با پرسپولیس و سپاهان را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/138397" target="_blank">📅 12:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138396">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/138396" target="_blank">📅 12:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138395">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👀
هد اسکاتینگ پرسپولیس دستیار بختیار زاده رو تعیین کرد!
🚫
فرزاد حبیب الهی هد اسکاتینگ باشگاه پرسپولیس پس از فرو کردن دنیل گرا به اسپانیا بازگشته بود و سمت پرسپولیسی ها آفتابی نمیشد حال با کمک پژمان راهبر پانادیچ رو به تراکتور برد و حالا هم ماریو توکیچ را به استقلال/ویژن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/138395" target="_blank">📅 11:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138394">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✖️
مهدی تارتار:
😀
ایگور سرگیف مصدوم است و هنوز به شرایط آرمانی نرسیده است وگرنه او جزو مهاجمان اول ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/138394" target="_blank">📅 11:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138393">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/are2y3cUtZGSyPKBSNolMNSW07jMwWXLTd5q3gH7HTAzQnrb_1RnZ9Lip4RjnJ1qZ8AOQfSeFd6bTrzExcPiA6-jOuNqUDIWhQARVkCiM6PylSpfIj9mVhw6dhGrk7cWvcHr93pk_PbhCONDm3xs2kj51gk2wHkxWIUDbhuA6TEybsIXw-qPxEWwfGkcfpOdgyCskfb8GJRDIEMzqqDpi-LR72NFNWLOyd0Z8Gasa2rmAUY1f-ZuUzNJnWkMKn03Ia3Mf-yhJ1IaM5yEMCwOGz9sqttVEgalCkN8Ik3JMbCGPZo3PMj83ZRuguKz21WUp23UYvekweNk4_PqImJpLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوتبالی: دانیال ایری امروز ظهر در ساختمان باشگاه پرسپولیس حاضر میشه و قرارداد پنج ساله خودشو با پرسپولیس امضا میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/138393" target="_blank">📅 10:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138392">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/138392" target="_blank">📅 09:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138391">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/138391" target="_blank">📅 09:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138390">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/138390" target="_blank">📅 09:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138389">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/138389" target="_blank">📅 09:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138388">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/138388" target="_blank">📅 09:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138387">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/138387" target="_blank">📅 09:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138386">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/138386" target="_blank">📅 08:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138385">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9-LGm5jaY4pAoXl7FXK4PqHlYcUFnfrMvPuz0EGeSkyoYZI0KW8w1MOhWCCyNMgp-XyjCo4f620vh0CW7o3Vd1iu3K6x62n6vkKepmQ1Xy1JkLXyLPfcRWAQmepdYP9w9gYcPYio84EbwrEoNJXIheDcwZ7GxmqpjONz8--lLMmns9-eB_l8JvDp2Z8NF9NC9nAH1Xp3u7e0YMzSsvKCmkxUxh40wI9ysyXGhK533q3e9x9cfuqUhvX7HHrbT7dSoZAc77QUaSq0qE_XXICnNmFEAYQeQnoPSEXb5jeMa6PBZl1tMNgkAJzrufoqaLbCs148VeBbB47GvkUGUfFwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/138385" target="_blank">📅 01:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138384">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">💢
💢
💢
🚨
مدیرای باشگاه میگن که نقل و انتقالات با جذب محمد قربانی تموم میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138384" target="_blank">📅 00:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138383">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
✅
باشگاه تصمیم گرفت از رفتار اورونوف چشم‌پوشی کنه و حاشیه رو ادامه نده/ایران‌ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/138383" target="_blank">📅 00:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138382">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔽
🔼
بازیکنی که امروز اصلا بازیش به چشمم نیومد عیدی بود، بنظرم باشگاه باید با جدیت سراغ رامین رضاییان بره…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138382" target="_blank">📅 00:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138381">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
فاکس نیوز: تفاهم‌نامه ۶٠ روزه بین آمریکا و ایران تا چند لحظاتی دیگر منقضی می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/138381" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138380">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1875da2c0.mp4?token=dWMroaD3wP2M5bMcRowoJH0LytluhKDkutemP2SKgb0rGQtB4txopigtSefw1H0tyfaVybgRHdimQJURdmv09W0hKkDY3muuWO8Zpk-kJRiL_ymIOvRGfrKZds18D5F-xN2YJKlmo9fq5dCLdiXtyXVQw9uV6ACAtcv_KIR8ezcvXEWW-9dF_0BvChexAzko7RU5nEvtuzzuTgCob_mTAHc7LIpr6ea5PLNLx7vm5hu0ViQJPiep53wiZX9tALHO8TGjKDmN1WLh9MqVD6gqEenvALvfYv41fcXnRjH0o38GMwxvSEBJ52y8OQQuRmXOnLYGyFwI0FyxferGmkpnDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1875da2c0.mp4?token=dWMroaD3wP2M5bMcRowoJH0LytluhKDkutemP2SKgb0rGQtB4txopigtSefw1H0tyfaVybgRHdimQJURdmv09W0hKkDY3muuWO8Zpk-kJRiL_ymIOvRGfrKZds18D5F-xN2YJKlmo9fq5dCLdiXtyXVQw9uV6ACAtcv_KIR8ezcvXEWW-9dF_0BvChexAzko7RU5nEvtuzzuTgCob_mTAHc7LIpr6ea5PLNLx7vm5hu0ViQJPiep53wiZX9tALHO8TGjKDmN1WLh9MqVD6gqEenvALvfYv41fcXnRjH0o38GMwxvSEBJ52y8OQQuRmXOnLYGyFwI0FyxferGmkpnDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آنالیز فنی بازی شمس‌آذر- پرسپولیس توسط محمد تقوی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138380" target="_blank">📅 00:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138379">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
برنامه هفته دوم لیگ برتر  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/138379" target="_blank">📅 00:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138378">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ارونوف تو تمرین امروز سرحال و قبراق شرکت کرد
📸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138378" target="_blank">📅 23:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138377">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
پیمان حدادی : امیر جعفری دفاع چپ گل گهر در لیست خرید ما نیست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/138377" target="_blank">📅 23:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138376">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
افتاد ساعت ۲۰ که هوادار قشنگ بره برای تشویق و ورزشگاه و پرکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138376" target="_blank">📅 23:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138375">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
✅
✅
مشاور قالیباف اعلام کرد: با تصمیم سران قوا، گرانی بنزین منتفی شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/138375" target="_blank">📅 23:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138374">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/138374" target="_blank">📅 23:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138373">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
برنامه هفته دوم لیگ برتر  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138373" target="_blank">📅 23:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138372">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkG9EeYufcZ4eyZZJGg-Bxg4CP8xmKxy1GSn_CKhs74A7PbK9A1jkvkluDZihlVVnEd4UimU0rlT4iQndrYnsG4aqb5D92wu3zlp-2DTT3WGdbOhEDOMNOtVzo155LrV-UV8yW4PSPF8ar2KPaqDcg4ylF2qCDbxLaP6cweQnXBLJUo53IJgUSq-cgvlavaKhIhsV8GLAqypgcDXPGsHCtDSIcU_fLIzc2c9mdkxk_o5L628FqodrW-cdlHDs_FAQuCK5KwNFdySa674ORQDZYVhLR9MIoZvrUwa_rqJXUmWHxq3DPEt6EGPO8fX7WE2FFTR9Cmu3EuFBc9r6idZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
پرسپولیس و تراکتور همچنان پیگیر جذب محمد قربانی هستند اما الوحده امارات جواب مشخصی هنوز نداده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138372" target="_blank">📅 22:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138371">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
✅
تنها 30 ساعت به پایان ضرب الاجل 60 روزه ترامپ برای توافق با ایران باقی مونده و هنوز نه صحبتی از تمدید آتش بس هست نه مذاکره و توافق.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138371" target="_blank">📅 22:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138370">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laqKlJ_K7h1l2AeyQamAM2WRHbg9BhiSunTw9zsDYIleFd6zy-lMU9RV519gt2yg63c7Gx70ZiqlivVSR_8i-lBupmvLyBJoXuo-5yozIGUYI3dy_4KBssJw49WAu8PPlvgy19stEEkUg6TH3eTBoTWUF56F9TUIGTwjcGUQCfv7zCTLrezO7A9h8YaUD14JY50Q1jQvodUZdpP8ohEKH7PQmozaXPuRV_t-uyJXirUJ1nHt8D8YLaumnwcnQA8DXhGOs3nIbUOt6t8pVLcSO6Gqoa3XtV7KibwpWgLmRxpVOAjzv6z0lRqVgYEoRuy5tNNc9hjzFwjiokDwI7nyRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آقای تارتار اگه کل فصل تیمت مثل نیمه اول بازی دیروز باشه و تماشاگر پسند بازی کنیم و نتایج لازم رو بگیریم، اعتراف میکنیم که حق با تو بوده و ما اشتباه میکردیم می‌گفتیم تارتار نیاد، فقط خارجی...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/138370" target="_blank">📅 22:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138369">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaRmHcn7FfG4LWWDrjzONPcVe0lgfNGbCHm50udq4xtDqaMPGH8HA-FuW_R93cAVDJjgSLcYSru-HuV_Y2y7KlyFNi-6rFk7piErF_Jih9Ejy_WykI3WNzYj30xAhXdWTY7trQ1N4iVF_9Czz_Gu2cBXnzEuL3-0XNpiyrxrk3wHJtZchXRGaUUzo-Pu_Umwzo-EnFZKWJN03PG4BPShZ9vDZDyNwWze3H-18v4lGpxs4XXyRhBhM33YmT_W8-prMwjN6mVoPG6a-g12m-1QGMccJXUbE6ZqM62k0dZZyuOzuUhPj1t10LuqKC6ahSQ6GbTg4biZV_f6fIbWu09pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارونوف تو تمرین امروز سرحال و قبراق شرکت کرد
📸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138369" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138368">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLK1g_d0KGnCYP7C_j5E7BBxyTCfYZx2NlK-0L1_9ZP8e_rmJ43fkW4mdOhRczaHG3xqzw_qSmrBB_gdMqCjgybgnagUIL7DAR35-bmxRVbEkv-yKJFOgQN3hKNye4V3uaDDEK1xNKVNdM29r5tg8VQbnubi-I2eZ73RQMIPLdsVRo0t5jBnLCW14DTqvBMaPyfS7Tpf8pzuuERcEDHboEelvtFxoQu1uJuzAFF76jEDnGOX2Eg0PEloj80061GZDKUcEB0X7x7ts1dM3ByL3k7K_AuknSVqNcFZwlDJvnJJtzzTNSx6QJVCf919mg-S8slIWIPq7GhD8Y6xFP53Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138368" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138367">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1mwXTK-DmSMwm6QD-_MKE34nhJq-P05-_4a7tcIRJ77ajFCseAKJId5yJKwYiz3de8VEiqxr5UVsYqF9S2lYWv8Y-xm4-O4IU6kzOsftvNWJxPZ9CJaIF7ss_g6glaKQJHXz0OreyfSt-f2KHSkHS2jxJdR8CWcqWqnPZhGja0Sb1FQEZKuqRV29Vy3GTqdsjz4r5zkrLEJqUUr6vejWjBQhcCPPZIvdprI-b-GtzRpG93IpNbNt-y1j2XRxkzfPsI6ltC_GJ-Lj7oAIDXD1ZQ4nnih42KB3ihRJ6nFR-YFBAvVMTjTCjDJ65lBPYsvagY28cmTWyFMp33NmHBYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚽️
✔️
پیام نیازمند با 3 تا سیو موقعیت و ثبت کلین شیت بهترین دروازه‌بان هفته اول لیگ شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138367" target="_blank">📅 21:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138366">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇵🇹
نشریه رکورد پرتغال : محمدجواد حسین نژاد در آستانه انتقال به ریو آوه قرار دارد
💵
مبلغ انتقال : 1/4 میلیون یورو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138366" target="_blank">📅 21:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138363">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پست ۶ : عنایت زاده پورعلی لطیفی فر پست ۸ : باکیچ خدابنده لو پست ۱۰ : یاسین سلمانی  واقعا هافبکامون ضعیف هستن</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/138363" target="_blank">📅 20:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138362">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🤑
در عربستان پول پارو کرد!
🇸🇦
کریستیانو رونالدو از زمان پیوستن به تیم النصر، مبلغ شگفت‌انگیز 625 میلیون یورو به عنوان حقوق و پاداش کسب کرده است.
😇
فوق ستاره پرتغالی در کمتر از چهار سال، ثروتی بی‌سابقه به دست آورده و او را به فوتبالیستی تبدیل کرد که بیشترین…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/138362" target="_blank">📅 20:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138361">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMilad Gh</strong></div>
<div class="tg-text">پست ۶ : عنایت زاده پورعلی لطیفی فر
پست ۸ : باکیچ خدابنده لو
پست ۱۰ : یاسین سلمانی
واقعا هافبکامون ضعیف هستن</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/138361" target="_blank">📅 20:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138360">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">همینا ک میگن پورعلی خوب بود  کافیه دیشب بازی با دقت دیده باشن  چند صحنه به راحتی تیم شمس آذر در موقعیت شوت قرار گرفت  چند بار توپ ازش عبور کرد کنعانی پوشش داد  یه بار هم از گوشه چپ تیم یه دریبل خیلی مسخره از ممی زاده خورد شانس آوردیم گل نخوریم   پورعلی و امثال…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/138360" target="_blank">📅 20:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138359">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from♤</strong></div>
<div class="tg-text">همینا ک میگن پورعلی خوب بود
کافیه دیشب بازی با دقت دیده باشن
چند صحنه به راحتی تیم شمس آذر در موقعیت شوت قرار گرفت
چند بار توپ ازش عبور کرد کنعانی پوشش داد
یه بار هم از گوشه چپ تیم یه دریبل خیلی مسخره از ممی زاده خورد شانس آوردیم گل نخوریم
پورعلی و امثال پورعلی خیلی شاهکار باشند بهتر از سرلک هستند
ما بازیکنی میخوایم ک یه وزنه باشه فشار از رو دفاع برداره ن اینکه دفاع سوتیاشو جم کنه!!!</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/138359" target="_blank">📅 20:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138358">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ما کی به بازیکنای اکادمی خودمون اعتماد کردیم و ضرر کردیم؟؟ پاسخ روشنه هیچوخ  نمونش امیر رضا رفیعی،عمری،محمودی مطمئنا اگه تو پست های دیگه هم اعتماد بشه نیازی نیس بریم منت کشی بازیکنای دیگه محمد قربانی ها و حسین نژاد ها خوبن اما به  وقتش با قیمت درستش</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/138358" target="_blank">📅 20:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138356">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/138356" target="_blank">📅 20:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138355">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">ما کی به بازیکنای اکادمی خودمون اعتماد کردیم و ضرر کردیم؟؟ پاسخ روشنه هیچوخ
نمونش امیر رضا رفیعی،عمری،محمودی مطمئنا اگه تو پست های دیگه هم اعتماد بشه نیازی نیس بریم منت کشی بازیکنای دیگه محمد قربانی ها و حسین نژاد ها خوبن اما به  وقتش با قیمت درستش</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/138355" target="_blank">📅 20:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138354">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/138354" target="_blank">📅 20:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138353">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚽️
قربانی رو بگیرن ولی با همون ۵۰۰ هزار دلاری که گفتن میدیم به اروپایی ها نه ۱.۲ میلیون دلار، اصلا شما بگو ۷۰۰ تا
اخه ۱۲۰۰ ؟
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/138353" target="_blank">📅 20:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">باکیچ بدبخت هافبک پست ۸ هست یبار نشد اونجا بازیش بدن ببینیم چیکارس ، پاس های خط شکن خوبی میده خوب تکل میزنه</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138352" target="_blank">📅 20:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138351">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmd</strong></div>
<div class="tg-text">خدایی باکیچ قبل مصدومیت عالی بود</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/138351" target="_blank">📅 20:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138350">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چراغی تو همینی نیستی میگفتی باکیچ میشه رهبر خط هافبک چیشده ؟ وژدانن به جز اون گل رو به ترتر زد دیگه چه کاری انجام داد؟</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/138350" target="_blank">📅 20:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138348">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمد</strong></div>
<div class="tg-text">چراغی تو همینی نیستی میگفتی باکیچ میشه رهبر خط هافبک چیشده ؟
وژدانن به جز اون گل رو به ترتر زد دیگه چه کاری انجام داد؟</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/138348" target="_blank">📅 20:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138347">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommilaad zd</strong></div>
<div class="tg-text">برای اولین بار شاید باهات موافق باشم چراغی ..کسایی قربانی قربانی میکنن دو تا بازی ازش ندیدن این پول خرج حسین نژاد میشد مشکلی نداشت تلنت خفن و نیاز تیم به یک توپ گران قربانی نهایتا ورژن جوون تره باکیچ هست در کل هم تیم به پلی میکر احتیاج داره (جایگزین سروش رفیعی) تا یه سنترال هافبک</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/138347" target="_blank">📅 20:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138346">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran Jan</strong></div>
<div class="tg-text">کاملآ منطقی فرمودید
نرخ برخی  بازیکن ها را هواداران زیاد میکنند با فشاری که به باشگاهاشون وارد می‌کنند</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/138346" target="_blank">📅 20:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138345">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">#نظر_شخصی
💬
حوصله بحث با این بچه مچه هارو ندارم،عقل ندارن واقعا یه عده راحتن
‼️
خلاصه خزعبلات شون: از جیب تو میخاد بره، به تو چه، به قربانی ندیم به کی بدیم،پس چطور استقلال برای سحرخیزان ۲ میلیون دلار داد.
‼️
از قدیم گفتن عقل که نباشه جان در عذابه، اولا از…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/138345" target="_blank">📅 20:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138343">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/138343" target="_blank">📅 20:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138340">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
✅
احضار اورونوف به کمیته انضباطی تکذیب شد و او امروز تو تمرین پرسپولیس شرکت میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/138340" target="_blank">📅 19:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138339">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIman</strong></div>
<div class="tg-text">پورعلی
لطیفی فرد
باکیچ
عنایت زاده
سلمانی
خدابنده لو
مگه یه تیم چند تا هافبک وسط میخواد؟</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/138339" target="_blank">📅 19:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138338">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">اصلا طرف ورژن ضعیف احمد نور هم نیست نه توانایی گردش توپ داره نه اونقدری شوت زنه تنها چیزی که تو این ۲ سال ازش من دیدم میاد رو کرنر ضربه سر میزنه توپ گل میشه
اگه با ۸۰۰ تا قبول نکردن باشگاه باید فرهان جعفری رو وایسه تا نیم فصل بگیره</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/138338" target="_blank">📅 19:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138337">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSCORPION</strong></div>
<div class="tg-text">تیم اینهمه هافبک دفاعی داره اینو براچی بگیریم خب</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/138337" target="_blank">📅 19:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138336">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSCORPION</strong></div>
<div class="tg-text">بازیکن معمولیو چرا انقدر میدن؟</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/138336" target="_blank">📅 19:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138335">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">#شفاف_سازی
⛔️
👀
دارن تا دسته میکنن تو کونمون با احترام، مندیت اروپای قربانی دست رضا مصطفایی ایجنت پیام نیازمنده؛ عددی که الوحده اعلام کرده برای صدور رضایت نامه محمد قربانی 500 هزار دلاره برای باشگاه های اروپایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/138335" target="_blank">📅 19:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138334">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138334" target="_blank">📅 19:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138332">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
✅
✅
⏳
10 روز تا پایان پنجره نقل‌وانتقالات تابستانی فوتبال ایران باقی مانده است.
❌
❌
پس از بسته‌شدن پنجره، باشگاه‌ها تنها امکان جذب حداکثر 3 بازیکن آزاد را خواهند داشت. بنابراین روزهای پایانی می‌تواند برای تکمیل فهرست تیم‌ها بسیار تعیین‌کننده باشد.  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138332" target="_blank">📅 18:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138331">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138331" target="_blank">📅 18:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138330">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🤝
🤝
🤝
قربانی رو بیار و بهترین پنجره تابستونی تاریخ رو به نام خودت ثبت کن دکتر پیمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138330" target="_blank">📅 17:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138329">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">💢
💢
💢
💢
مدیریت بانک شهر صبح امروز به وعده‌اش عمل‌کرد و 800 هزار دلار بودجه برای جذب محمد قربانی دراختیار مدیریت پرسپولیس قرار داد.
❗
❗
مدیربرنامه‌های‌محمدقربانی  به پیمان‌حدادی‌مدیرعامل پرسپولیس اعلام کرده باشگاه الوحده رو راضی میکنه که با همون 800 هزار دلار رضایت…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/138329" target="_blank">📅 17:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138328">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
500 تا دیگه رفت رو رضایتنامه؛ گلزنی محمد قربانی برای الوحده که داغ دل تراکتوری ها و پرسپولیسی هارو تازه کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/138328" target="_blank">📅 17:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138327">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
✅
با اعلام تارتار دانیال ایری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/138327" target="_blank">📅 17:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138326">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138326" target="_blank">📅 17:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138325">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
با اعلام ایجنت محمد قربانی این بازیکن امروز با مدیران باشگاه الوحده برای تعیین تکلیف قراردادش جلسه دارد و رسما تکلیف بازگشت یا عدم بازگشت او به لیگ ایران مشخص خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138325" target="_blank">📅 17:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138324">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
با اعلام ایجنت محمد قربانی این بازیکن فردا با باشگاه الوحده برای تعیین تکلیف قراردادش جلسه داره و رسما مشخص میشه که میاد یا نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/138324" target="_blank">📅 17:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138323">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCTELWXZziXhyqFIj08HAptyMRYsyaAqXgjrxyPaObeiUcVTdZnHQ2UHZj5eq75v49eZmo-z9TNqseKm9gD2Nknl3p-HUeO0SFJbWmit648ehHLYgQ6DwEKYYXcDQ0aqV1dg4wlVNis3_Ek2U-jRg1GK6KhIC3DMFlabYQGJKHBOZNV_osR3e09s_rjB5uRF6TBlI3PAQuk-hdZ3qFtGuG_tMiBNpQPbf_svBf1sJx2XQYcjmyvV4ozO4l6YhcKw_YSlQptOIbsxnjkJ63QE0fjXJWakMN4rGL0-bydhq8KYli6PPO8aJa0DX2ZHHv9RguPNDgW2_YZhl7jKWR5GYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
افشاگری و پست اینستاگرامی محمد یوسفی: خلیلی، اینانلو و دهن‌گشاد دنبال برکناری حدادی هستند تا خودشون جای ایشون قرار بگیرند!
🔴
زیر پای افشین پیروانی رو خالی کردی تا خودت سرپرست شوی.
🔴
آمدید که از پول‌های کلان بانک، چیزی به جیب بزنید ولی کور خوندید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138323" target="_blank">📅 16:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138322">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⛔️
سخنگوی بی‌درایت سرخود هفته پیش مصاحبه کرده که جذب دانیال ایری میتونه محرومیت برای تیم و باشگاه داشته باشه !!! درصورتی که پرونده ایری اصلا شبیه به کسری طاهری نیست.
⚠️
ایشون با ندانم کاری و رفتار زشتی که داشته، چالش بدی درست کرده در جذب بازیکن. شما وقتی دانش و اطلاعاتی در زمینه حقوقی و حتی فوتبال نداری بیخود میکنی چنین حرف نسنجیده‌ای میزنی.
‼️
اون از تیزر ساختنت که فقط سوتی میدی و باعث پاک شدن پست میشی. این هم از مصاحبه درمورد نقل و انتقالات!
❌
فشار بیارید تا هرچه زودتر این فرد بی‌سواد از باشگاه بره کنار. علنی دارن جلوی نقل و انتقالات رو میگیرن با صحبت‌های نسنجیده!/خرمی
#افتتاح‌مجدد
#کون_گشاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/138322" target="_blank">📅 16:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138321">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
با اعلام ایجنت محمد قربانی این بازیکن فردا با باشگاه الوحده برای تعیین تکلیف قراردادش جلسه داره و رسما مشخص میشه که میاد یا نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138321" target="_blank">📅 16:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138320">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b867823a4.mp4?token=q_sV9R49nd-l5W1nzS28NkzHBvT6d-y1POHj0a3N-i3SAzl1zPcKZwrSYpN8Q9aZusr0nB3eCoeO5wik2v_83StIxTz5N4fdZbqWETVhA_5TcgNDXPbxQXkr8U6IKt9OevgiIpQzqNIYleHV-C_WgXvULTPDasVUoY9Z5reOrSexokydGbEtv0VgH5sA-2jjb2Zt4uXjD6qPvDAg-GdqW0et8EiTnzxpT7BDHGVm38cC_qv91-6PI5rCGsjz7qFLnOUyr8VGWqAFHjPPQbwZqX_M__PFpDLJUZ-gL8q49s1uOvMw1HFwHDBbyzJepJ5a4bLlLmsLUrkBhIVoueAr8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b867823a4.mp4?token=q_sV9R49nd-l5W1nzS28NkzHBvT6d-y1POHj0a3N-i3SAzl1zPcKZwrSYpN8Q9aZusr0nB3eCoeO5wik2v_83StIxTz5N4fdZbqWETVhA_5TcgNDXPbxQXkr8U6IKt9OevgiIpQzqNIYleHV-C_WgXvULTPDasVUoY9Z5reOrSexokydGbEtv0VgH5sA-2jjb2Zt4uXjD6qPvDAg-GdqW0et8EiTnzxpT7BDHGVm38cC_qv91-6PI5rCGsjz7qFLnOUyr8VGWqAFHjPPQbwZqX_M__PFpDLJUZ-gL8q49s1uOvMw1HFwHDBbyzJepJ5a4bLlLmsLUrkBhIVoueAr8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏟️
آخرین وضعیت سکوهای ورزشگاه آزادی و وضعیت زهکشی و زیرسازی چمن این ورزشگاه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138320" target="_blank">📅 16:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138319">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
یا الله بسم الله اسماعیل کارتال ...
🔥
❌
پ.ن چه تیمی داره حاج اسماعیل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138319" target="_blank">📅 15:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138318">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✅
رامین رضاییان یه ویدیو از مهران مدیری استوری کرده که در اون میگه آدمی که افشاگری میکنه، کثیف‌ترین موجود جهانه. مثل اینکه دختره راست می‌گفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138318" target="_blank">📅 14:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138317">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
🔴
مهرداد کفشگری: احمد نوراللهی از تراکتور مشکلاتی با قلعه نویی داشت/ احمد خیلی صبور است اما اگر صبرش لب‌ریز شود، قید همه چیز را می‌زند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/138317" target="_blank">📅 14:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138316">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✖️
مهدی تارتار:
😀
ایگور سرگیف مصدوم است و هنوز به شرایط آرمانی نرسیده است وگرنه او جزو مهاجمان اول ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138316" target="_blank">📅 14:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138315">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🗣
🗣
🗣
بزودی باشگاه پرسپولیس جلسه‌ای توجیهی برای اوستون اورونوف ستاره ازبکی سرخ‌ ها برگزار خواهد کرد. اورونوف شب گذشته در پایان دیدار با شمس آذر درشادی بازیکنان این تیم شرکت نکرد که باعث دلخوری مهدی تارتار سرمربی این تیم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138315" target="_blank">📅 14:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138314">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcpAUP-EMgp8V17Im7lXv65rH6LuUERNlaKNcefvs3NKxq4ysU6iGQYu-CU5vj4DHER2EhYN4sqvShkdOhlCBZRHQ5Il9L6Dugb2slU_fwxCzfuepyR2ULtmlDAiGJWGcZ_ZgPoFQvP5i2LmEvTWuU2sVO5KhiE-pmnEpt1pJBOSueQUy_bqu0iorZMwX2qY3nbjmv_7dbbCUgKFK57vAMUJ1qR8gVlKMYjTpxTm1G-iwnCTZJJSmbQ3JuaWiWsPTk4Odr--MzFp9GxP8JPndbuQqTiJNfoL9oLmBHJkNeSc0xGotaCLvu3TcFrnjQXsCGsTIy3o35oZsP8Q7RBJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
نبرد قهرمان اروپا در خانه لانس!
پاریسی‌ها برای شروعی قدرتمند پا به بولارت دلِلیس می‌گذارند؛ اما لانس آماده است امشب را برای پی‌اس‌جی تبدیل به کابوس کند!
🇫🇷
فینال
سوپرکاپ فرانسه
[
لانس
⚽️
🆚
⚽️
پاری‌سن‌ژرمن
]
⏰
یکشنبه ساعت ۲۲:۱۵
🏟
استادیوم بولارت دلِلیس
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
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/138314" target="_blank">📅 13:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138313">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
با اعلام ایجنت محمد قربانی این بازیکن فردا با باشگاه الوحده برای تعیین تکلیف قراردادش جلسه داره و رسما مشخص میشه که میاد یا نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/138313" target="_blank">📅 12:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138312">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
اورونوف به‌دلیل اعتراض به نیمکت‌نشینی با تارتار به مشکل خورده و احتمال معرفی‌اش به کمیته انضباطی و غیبتش در بازی بعدی وجود دارد./هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/138312" target="_blank">📅 12:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138311">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
محمد مهدی محبی، محمد عمری و پوریا پورعلی به‌ ترتیب با نمرات 8.4، 8.1 و 7.9 بهترین بازیکنان دیدار امشب دو تیم پرسپولیس - شمس آذر بودند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138311" target="_blank">📅 12:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138310">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
با درخواست کیسه به عنوان میزبان دربی ، دربی رفت به احتمال خیلی زیاد اصفهان و ورزشگاه نقش جهان باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138310" target="_blank">📅 12:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138309">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔄
🔄
🔄
فووووووری؛ سه گزینه باشگاه استقلال برای میزبانی دربی مشخص شد
❌
ورزشگاه‌ امام رضا مشهد
❌
ورزشگاه سهند تبریز
❌
ورزشگاه نقش جهان اصفهان  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138309" target="_blank">📅 12:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138305">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYpSHgaQMQo5HX5YLQDPzcKbagLGV_RPH6SDmunwUlGffEtL9w0InJn9woCnWx-IvPR1u8xCMVbbbJrGAezmXs-AnHhkFq66sZXtFM3yfojP11Fl60MghpP6l9si9ou3_hcEDzP_8aZw44RWnlQ7AEonLWFkPLa-kRjixpamYi3H2U70Y7jeRPfBPKZMzOYCbjkqtHslFIk-1B31NNDbkbEHsTG8poRdJOJgGLLqwM_-YCGgR2Sdf0B3FTL04wztw2QJLt0XTtmiA73mUIitGHg8n_Nv8BnkaTAFTxMNXSygLNujLKbxPiss-Ml2uFNbhrwjAgvR8LQXG4YYH5GtlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJStsts2sITmIV7h-QaERtiTBuX-WngFV9F5iOHEjVGuLks6_qUEp892WQGne38Sig9zsSxG6U8M5fRAyzt1-N-oc8Ql7MozxA1gp4FingTiN_8dWe_6DF0rLAgYABc4hSS3gUzN56pwXq2FgMrFiHzg4ed2r3Sv0z2uDCRa3tuz1bc4JVkym9WAd1yGHTQ_H8rw2jfCNSJz8h5fCxa_i9gvTn169LpVwoQV1xn6I7NxE88cjE_d865O3TLQrS1bo0I3n6hgpW2rjp6G95WviuqeaqkDOhxEC56qoO2dNkXwGPR5RfDRi-uhLXK4TI-I-10m3V7JYnOYI6iOApDyJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cKgmFo8Qvc2b1H7xUlUaotAZ3LlH1eBuMMr6WOjq5lBP7GO_1sHn4OFWbjQzJPlJq-6uAIEmA6eFPH_xgZdMN7soCtRpl3h0GdSLwKNbXUnLEZuBeDrAZl2Fvfx9oOTYCskzTJrFZA1s9x2tZsYs84kR-PmjI2lDSI5Hm3z5AWVwc_krRLGVUS-Rhen1OCvyK3mvjYeOVjvhers761qiUPdmvDLi6-RZXcsqxy_z8O0YsWyZKo70MQFeEZucda2uQDdz_f2Zkf9yA5XP9_P1Fj45_v15QslTLZoNI9-5zvqSwEFbXxOcahCLK4Rasr3Gknl0lOaiP5JTHd0JbK1i2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/osNVKlsb0xyD-_Dm0KvcbVn8uAL6Tk3zWP4EKB4erEgzq8-VPsPS-eqeeUgQURdZo9DCxKhDZ0QzWTbzrzdMlosTwrrRTov9YdJVOfGtklGhUMacER_REhNskv09n_MKNneGAg6h3bOmNdGAed4unXxeiBFpdG4EWeLFRj80Ng9FKFIqqcQrmzm5OICZvwbCnOL6ROO-iaCuenKVyH3NTA2MdAXDML436yNHDxRGp2_JzNrvFoMuXabQFJEpKimBXUjf1VUd8mn8iS2TxnrdhPbCVgPUm_Z2D2wSfjasS2FmPNgHnvVF1OmcvnpLqcIj5pCLrwOT8D520MNikXdqQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⚽
افشاگری‌های محمد یوسفی(هوادار متمول پرسپولیس) علیه محسن خلیلی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138305" target="_blank">📅 11:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138304">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇮🇷
🎙
واکنش تارتار به ناراحتی اورونوف: برای من دیسیپلین بازی و تیم بودن مهم هست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/138304" target="_blank">📅 11:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138303">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
کمیته انظباطی برای شفاف‌سازی وضعیت آسانی ، از سازمان لیگ و فیفا استعلام کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138303" target="_blank">📅 11:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138302">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
رسول باختر کارشناس حقوقی: یاسر آسانی بازیکن غیر مجاز است و دیدار استقلال و مس شهر بابک سه بر صفر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/138302" target="_blank">📅 11:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138301">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
فرزین معامله گری دفاع چپ 22 ساله پرسپولیس برای انجام خدمت سربازی راهی ملوان شد
❌
❌
معامله گری تا تابستان 1407 با پرسپولیس قرارداد دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/138301" target="_blank">📅 10:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138300">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ps2HZ1KHB8SfLqqesjaJ9iLDiWXadAwSfrXXnItASAZy6l8UUr6W7-SAwpqwrL6X0RuM_VQi-Ngfan3cNBNowExA8bRaYokyNmCL_D3QO8QpYz25L5Hhqs2TJ-CDK3IYt3cCkKoaeEh_GcJ7-VNsi9ftQJPAPXspD_KMB3BsbyRa2o4T50Hu61Ll4n79K0RLPEUXe-cOG7P9-1YIzkCuflykO6xzCBf2Ot2jFQ5_cl8tqWLyKhgB5WnU8pEDKcV9QuoeJgTx5GzNVRQW5mxUw0nLkj6emy_-9eZHkgOlUyjhjXhK7hQSKmZ-RUf1GU5mhnFK0IUPfq41Pfu2fYeAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
سه بازیکن برتر زمین در دیدار پرسپولیس _ شمس‌آذر از نگاه متریکا :
✔️
✔️
محمد عمری: 7.84
✅
✅
ابوالفضل جلالی: 7.81
✔️
✔️
محمدمهدی محبی : 7.61
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138300" target="_blank">📅 10:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138299">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
با تشکر از سهراب بختیاری زاده که ایشون رو مازاد کرد
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138299" target="_blank">📅 10:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138298">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjtT4PqEmnJqG64AGls5yaDqS80XpDMaDeJStcnp9LmL_Jlug-Hig0fkNehvfXopRc6pfPtFeq3CEjn83r-V4RLLyOsaknXupDKAIxl4SaT_B7Y1l229MZtmbYx4hV27_ivP4kEUVOBGhRLKYPNq_8-aHKPbXzR3akBGcDSVZkUBiXXt0Q_kMRiirAXMGa5jB5-BnylYFWrb95e4XPLfseJPptjcZZz1q5dMB2fZY78WeLS2tL0m1JgPPlLkZHgHTEKc6K9BUCrsMQoMfase-XohwE4oOoSFdlAAQJmD6RQOisR6goKs0tdHZ_sqYQhoPtb7HsNT4r7vbTvv84trVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
با تشکر از سهراب بختیاری زاده که ایشون رو مازاد کرد
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138298" target="_blank">📅 10:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138297">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
⚽️
بااعلام‌باشگاه پرسپولیس؛ مصدومیت ابوالفضل جلالی جدی نیست و این بازیکن مشکلی برای دیدار هفته آینده مقابل استقلال خوزستان ندارد. جلالی امروز بازی  درخشانی در ترکیب سرخ‌ها داشت.  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/138297" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138296">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
صبحی که تیم محبوبمون بازی و برده بخیر.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/138296" target="_blank">📅 08:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138295">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AplnqyTndriB4XKLes2YxhEk6tawoiTqbcGIXXS04TKDwJYQZnvxGE5GQZ7Z6shrQtnENa-vhCYeCQXJzgUeCpFR6Myvd4PI-hZvNxhWTBU9o3R4AuEhp0DOgTo5Am4X_ToVD-YfoGwOLzeWdemAvBCPtqsinRxNUi-pnCI9wIeW5c6CE3ciVZTP6tMxGkRwPKuaLNsWEuXDAMbPkrgCNvsk8EP5wPy_CfULK-GsZiqCL51w0gnyevE-MW1uLKtTfswJ84IWJ-fu1f3FoscbmDlzW022RgzppF475T3AStHhuNXPDZOXnp7UrDZGkgcSelt0ZEu_d7dRZmDDh2Z-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نبرد غول‌ها برای اولین جام فصل؛ جایی برای اشتباه نیست!
آرسنال با فشار و پرس مقابل سیتیِ باتجربه؛ نبردی که جزئیات تاکتیکی می‌تواند برنده را تعیین کند.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فینال
سوپرکاپ انگلیس
[
آرسنال
⚽️
🆚
⚽️
منچسترسیتی
]
⏰
یکشنبه ساعت ۱۷:۳۰
🏟
استادیوم پرینسیپالیتی
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
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/SorkhTimes/138295" target="_blank">📅 01:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138294">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
انتقال محمد قربانی به پرسپولیس کنسل نشده و هنوز احتمال نهایی شدن این انتقال وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/SorkhTimes/138294" target="_blank">📅 00:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138293">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
زارع هم تو دفاع خوب بود ...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/SorkhTimes/138293" target="_blank">📅 00:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138292">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/SorkhTimes/138292" target="_blank">📅 00:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138291">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/138291" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138290">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
با اعلام تارتار دانیال ایری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/SorkhTimes/138290" target="_blank">📅 00:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138289">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
ترامپ به فاکس نیوز: به‌ایران از لحاظ اقتصادی ضربه شدید خواهیم زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/SorkhTimes/138289" target="_blank">📅 23:59 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
