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
<img src="https://cdn4.telesco.pe/file/r6J-4E1qW_GerCItk0yE_RggW-KeriRF_i9aJz6ZduK57UUVYLLX-t5hpbx_ixV72KmBNZLH3Y1Yl2TWEghu4Wz0oMt6QcFQJpA9k0UmbBOB3pjs5Te-dc9CpE2VAqKUh6AzKYOc0HGs2ZQUubxjW-wCWqixFkMBzWJuKP5tsXhDfyWs77rO7Uef4rGWYRuMaC5CCuVJ3qW3Kx80paxVRL-W7Tn6PsZn5JSAoOVBP8t05mzZVoywupbeEkP0HWcy6H0-XTbfOJkIIXLdaxU2avX-dLe46-Yj4ja0R2HZCX3N7KYGqX5uVjZv-2_b2rqFKyE8UpHDMGGzQm5Oueceng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 23:37:40</div>
<hr>

<div class="tg-post" id="msg-137739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
✔️
تاج: هنوز هم معتقدم گل شجاع خلیل‌زاده به مصر درست بود
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 850 · <a href="https://t.me/SorkhTimes/137739" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
سعید مهری : برای جلالی آرزوی موفقیت دارم؛ بازیکن پرحاشیه‌ای نبوده و به نظرم حتما موفق می‌شود و توانایی فوق العاده داره و هواداران پرسپولیس با آغوش باز او‌ را می‌پذیرند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/137738" target="_blank">📅 23:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
علی بازگشا سخنگوی باشگاه پرسپولیس:
⌛️
قطعا به زودی سه بازیکن جذب خواهیم کرد
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/137737" target="_blank">📅 23:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137736">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚡️
⚡️
مهدی تاج، رئیس فدراسیون فوتبال: تلاش‌ می‌کنیم تا فصل آینده بازی‌ها با تماشاگر برگزار شود/ تمام بازی‌های لیگ با VAR برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SorkhTimes/137736" target="_blank">📅 23:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137735">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔄
🔄
بازگشا :در ساعات آینده یا چند روز آینده  خبراییه جدیدی هست که باشگاه اطلاع رسانی میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SorkhTimes/137735" target="_blank">📅 22:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137734">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
استوری قدوسی  پ.ن منظورش رامینه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/137734" target="_blank">📅 22:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137733">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn3S_LAYpWAXKPksGqCfr1KJBy3zP6rfepshRsL0y45DbW6QpHblyzYT8oJiURU2yOKVTd2L3xCJTsiQzzqxNF2op0ihHzAWOZPA-Oygx0kb5u6JomGgRbuzGtTPeYRgFLf20OCu9c7ObfnJA8hjcv2qLBHyRCqeUX4FDuT3Whk30j3_A5h64jaUlXCh8EfzHxw0CRtIUXNiZqq1VBMq6A9APoYLwqZbSUH4OqDlT8vK3BeFqvnZXpuidxXMVgTtayLg6wT-wjjBwcvEtwsaq27Spb20ItcfH2kRDesLnZROAWRBmskK48c_CQjFyACXmgMVYsF2U4gl9b4Mp3AY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌سپاهان‌دقایقی پیش به‌این‌شکل‌از کیت‌های اول و دوم‌خود برای فصل جدید رونمایی کرد. باشگاه پرسپولیس و استقلال هم ظرف 48 ساعت آینده از کیت های جدیدشون رونمایی خواهند کرد
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/137733" target="_blank">📅 22:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137732">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
استوری قدوسی  پ.ن منظورش رامینه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/137732" target="_blank">📅 22:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137731">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
❌
سازمان لیگ باید با این تخلفات اشکار برخورد قاطع کند.اسانی هم فسخ کرده.فسخ فسخ است ولو به فیفا یا فدراسیون اعلام نشده باشد‌.تاجرنیا هم این فسخ را تایید کرده است.مدرک بالاتر از این؟
🔴
🔴
کارشناسان با تایید افشاگری های #قرمزانلاین گفته اند استقلال نمی تواند…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/137731" target="_blank">📅 22:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137730">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
❌
حجت موتوری: سرباز بودن علیرضا بیرانوند؟ فعلا مشمول نیست و هواداران نگران نباشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/137730" target="_blank">📅 22:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137729">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
طاهرخانی ادعا می‌کنه پنجره نقل انتقالاتی کیسه تا آخر تابستون ۱۴۰۶ بسته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/137729" target="_blank">📅 21:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137728">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❤️
عادل فردوسی پور: هر پلتفرمی برای حضور مهموناش چند میلیارد هزینه میکنه ولی من افتخار میکنم که سلاطین فوتبال ایران علی آقا دایی و کریم خان باقری فقط با یک تماس من به برنامم اومدند، به هیچ مهمانی حتی یک ریال ندادم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/137728" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137727">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚫️
⚫️
فرهیختگان :تارتار هیچ نظری روی دنیل گرا نداره و گفته باید جدا بشه ولی محسن خلیلی مانع جدایی دنیل گرا هستش تا این لحظه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/137727" target="_blank">📅 21:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137726">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
استوری دیگر قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/137726" target="_blank">📅 21:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137725">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWAaDlB_dUAoMoEajU9Dlsioc2xG0hxi5CRkbLy2xfJyR38ALD2GTaRSZehnTW6lZvo0YB2In7SIddZ1r7KGKrfyav4OaLOpVhQl4lxF53l_mG3LVOz5cCy8e8zClsiSa3YuIutWVIeUAWooatSP1YukTjG4l_Z3K8nuEr9Jo8KPhi2hRoYiVkPJOIDOZSId_AKFmeT-JKTkqkKcbLtn2QPOCVEtpPAENp83OejXcUTe5Zp9Yu6IBErcwN16o5lPh0byeC9rrj_7xVcNw3TkDD7I7id6bftRy2vrZ6e89RSNajeU9rqm8U6gr6xERdofkcWfi7hPoBpB1cqT2EMWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
استوری قدوسی  پ.ن منظورش رامینه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/137725" target="_blank">📅 21:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137724">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sObLBZA-IU6IiX3Dfos2cu5YEndludk7LSTE2z5ddUQ7H025rmduMs6ZgHiVYkNksl5agc5cY6XpYFalthIvfAju-itI_TMAvXRY2tXrTiYp-4Gcdv7en0QPZsS1ZDyBUCoX1f5UVZyH5wOSfp_ngBljWTN2_4ylHzbqgn0Y4ya0Ouhoymgr1amPnZU0ebkyp_gw-DvHKp8gsdicl9R5Xwrr3724DaecqTfnf9KkGug5TeAR38lzHp0jwfR4w5LqIuecVNvl3X6D2zl_XV6Zs2Dkx-UToAmlobPHFOBh1VI5e0az_WFUKnxtRaWDlxVxyYGCfP4qSzie0uiLkvOnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
رامین رضاییان که هیچ تیمی گردن نگرفتش امشب با کمک میثاقی میاد فوتبال برتر تا از سگ دو زدن هاش تو اسپانیا تعریف ‌کنه که شاید یه تیمی گردن بگیرش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/137724" target="_blank">📅 21:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137723">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
ترامپ: ایران خواستار غرامت خسارات درگیری نظامی ۵ ماهه است و من هم از آنها غرامت می‌خواهم چون سربازان امریکایی را کشته اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/137723" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137722">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
ترامپ درباره ایران:
🔻
به نظرم این جنگ به‌زودی پایان خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/137722" target="_blank">📅 21:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137721">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا، داخل بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه!!
❗️
پ.ن سیاست آوردن تو فوتبال و ترس از آمریکا و ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/137721" target="_blank">📅 21:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137720">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCWh3uA_PPgFDZ1R62JBF_jpJDBDxPPAtGX_vRgfqOk44b0ap8Fq_y8oJmccodUBR_U-ROLcSyiQrTzs8USt1CrTh9-nOUOp8c5XDyO9iRfgxw9bzKDFjcoI7azGX_oxNMth5qpbyBqzkpWMGrJKIdKCaLg-gMEgiXEYmPCjxYhwWql3_7ssEkC02wfYPIqSUUMyy9qdb0w4ikzUrszkt0O7UAZv5Ltr8Y1GKfyX2fZo5p-Jruagft4liagXMdXC1XbyjTcQsqZ9q0A3-6BmO_4pJgdczrTF_2VQ9HTWoVWRs-89Kneio7kqamXCmB2PQeGZG0Jid62NqpRd8GtZtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎾
جودار و فیلس؛ جدالی که می‌تونه تا آخرین امتیاز کش پیدا کنه، قدرت و تهاجم مقابل ثبات و جنگندگی؛ هیچ امتیازی ساده به دست نمیاد.
🎾
رقابت رافائل جودار
🇪🇸
-
🇫🇷
آرتور فیلس رو با آپشن‌های مختلف و بدون خارج شدن از تلگرام همراه با
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
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/137720" target="_blank">📅 20:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137719">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
پوریا شهرآبادی: مقابل منتخب کرج وقتی 6 گل زدم دیگر گلی نزدم تا شش بماند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/137719" target="_blank">📅 20:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137718">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ورزش سه:
🚨
مهدی تارتار از سیستم ۴.۳.۳ استفاده می‌کنه، برخلاف سیستم پرسپولیس در فصل‌های اخیر که ۴.۴.۲ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/137718" target="_blank">📅 20:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137717">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
رامین رضاییان امشب مهمان برنامه میساکی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/137717" target="_blank">📅 20:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137716">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
امید عالیشاه بعد از 13 سال حضور در پرسپولیس به گل گهر سیرجان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/137716" target="_blank">📅 19:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137715">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
|فوتبالی: رامین به دو دلیل هرگز به تراکتور نمیره، اولا چون تراکتور مدافع راست آماده داره و رامین میخواد فیکس باشه، دوما رابطه رامین رضاییان و جواد نکونام باهم شکرآب شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/137715" target="_blank">📅 19:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137714">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🔴
پرسپولیس رسما قید حضور قربانی رو زد و مذاکرات رو تموم کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/137714" target="_blank">📅 18:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137713">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
هزینه‌ی جذب ایری با دستمزد یک فصلش حدود ۳۰۰ میلیارده/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/137713" target="_blank">📅 18:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137712">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
اختلاف مدیران باشگاه پرسپولیس با نساجی بر سر انتقال دانیال ایری تنها 40 میلیارد تومن است…!/ خبرگزاری مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/137712" target="_blank">📅 17:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137711">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
✔️
استون اورونوف در تمرینات پرسپولیس آمادگی بالایی از خودش نشون داده و احتمالا در کنار محبی دو وینگر پرسپولیس مقابل شمس آذر خواهند بود
🤤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/137711" target="_blank">📅 17:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137710">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
❌
لیست بازیکنان آزاد ایرانی با حضور محمد محبی ؛ علیرضا جهانبخش؛ رضا اسدی ؛ مهدی مهدی پور ؛ مرتضی پورعلی گنجی و رامین رضاییان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/137710" target="_blank">📅 16:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137709">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⌛️
4⃣
روز مانده تا سوت آغاز فصل جدید لیگ برتر فوتبال ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137709" target="_blank">📅 15:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137708">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
فنونی زاده: با بازگشت رامین رضاییان به پرسپولیس مخالفم
❌
❌
من مخالف بازگشت رامین به پرسپولیس هستم/ بهترین دفاع راست های تاریخ فوتبال ایران از استقلال است و بهترین دفاع چپ ها از پرسپولیس/ بازیکنان الان فقط دنبال پول هستند حالا چه می‌شود دو سال پول زیاد نگیرید؟/…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137708" target="_blank">📅 15:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137707">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
اختلاف مدیران باشگاه پرسپولیس با نساجی بر سر انتقال دانیال ایری تنها 40 میلیارد تومن است…!/ خبرگزاری مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137707" target="_blank">📅 14:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137706">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
فقط
8⃣
روز تا شروع لیگ باقی مانده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/137706" target="_blank">📅 14:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137705">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
آخرین شماره پرسپولیس برای جدیدترین ورودی
🔴
🔴
لطیفی‌فر پیراهن شماره ۹۹ را که در گل‌گهر نیز بر تن داشت، همراه خود به پرسپولیس آورده و در تیم جدید خود نیز آن را خواهد پوشید. در گذشته محمدرضا خلعتبری که پس از ترک لیگ امارات مدت کوتاهی در پرسپولیس حضور داشت این…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137705" target="_blank">📅 14:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137704">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🟠
فوتبالی :
⚡️
جذب دانیال ایری کنسل نشده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137704" target="_blank">📅 13:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137703">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
🔴
🔴
ایمن حسین مهاجم ۳۰ ساله تیم ملی عراق، در انتقالی آزاد با قراردادی یکساله به پاختاکور ازبکستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137703" target="_blank">📅 13:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137702">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
سرژ اوریه به پاختاکور ازبکستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/137702" target="_blank">📅 13:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137701">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9oZpNPiP0jhmLQDCxWgghYkMM_6yjbL9tg9uXWb9PZZOto4ocVx7z7EfCj5rCgO_fxW-xIgorC8RyGFxpt30NGVZiQuH0aTZbo8Y8WkNut9UsGqjA5mwXuw6-uA47UFMxAEiIZE0QipDDY_41z0nTJ1RDwkowiuCHXuUVMpqTjeipOwfWCfjvqwZ7BV5JWpzXfqm1rhEwmx_iXWyTRWvpc4RVo5NMUDCrBdtChC36Trd767_wr4nOZPsSjrlp_d3YwjJxbBoyaX5-p_rLB8-Y0hQGcTyf0CNU3jBBvf-PWTAA_6VvclsLZV0PqPtwOA-4WfXLubvhXprouj_kNxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
جدال قدرت و ثبات؛ خودار مقابل فیلس
🎾
Rafael Jodar -
🎾
Arthur Fils
🎾
خودار با تکیه بر قدرت ضربات و بازی تهاجمی، سعی می‌کند از همان ابتدا ریتم مسابقه را در اختیار بگیرد.
فیلس در رالی‌های طولانی و تبادل ضربات از انتهای زمین کیفیت بالایی دارد و می‌تواند بازی را به چالش بکشد.
در مجموع انتظار یک مسابقه نزدیک می‌رود؛ عملکرد خودار روی سرویس و ضربات اول، می‌تواند تعیین‌کننده نتیجه باشد.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و با ۱۰٪ بونوس اولین واریز پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137701" target="_blank">📅 13:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137700">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🔴
پرسپولیس رسما قید حضور قربانی رو زد و مذاکرات رو تموم کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137700" target="_blank">📅 12:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137699">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0PnJCBl20ONTGgxyEV8D4IFlaY51aomV1pX4tY07Z-9tPhFAmbJ3-8SVwpFzVEcqfMvyCl7Hi1Y5L6WmixgbfZL_YxEEnip76Mpa_7zz_zFZiC567k9XsLBhtnxSa83dBW7rmg3_uZwYK42pvo5DTHjr__ghmvo9-HMOil0NWO93fjCsMIzFd7ol2DshlzU8tW8IDVPpCcdfyRrT52ZSrl2ZsUMDaRN3jBS33VSNtrc40Vbt6knt0Btls4sufwbU1iDyM1wz7waL5lYxGDWOuFrHRDbemwmRFzU2I3GxcE5vBbTbx01273lg-Ribtx3FBAjQGRU35cm5LyT9_0f5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پرسپولیس رسما قید حضور قربانی رو زد و مذاکرات رو تموم کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/137699" target="_blank">📅 12:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137698">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
ورزش سه که دیشب گفته بود ایری به پرسپولیس پیوست الان نوشته ایری به پرسپولیس کنسل شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/137698" target="_blank">📅 11:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137697">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
ورزش سه که دیشب گفته بود ایری به پرسپولیس پیوست الان نوشته ایری به پرسپولیس کنسل شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137697" target="_blank">📅 11:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137696">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
پرسپولیس همچنان پیگیر جذب قربانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/137696" target="_blank">📅 11:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137695">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
ورزش سه که دیشب گفته بود ایری به پرسپولیس پیوست الان نوشته ایری به پرسپولیس کنسل شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137695" target="_blank">📅 11:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137694">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
❌
قاب ماندگار از اورونوف؛ ستاره محبوب ارتش سرخ پس از جدایی سروش رفیعی، حالا یکی از صاحبان بازوبند کاپیتانی پرسپولیس است.
👍
دیروز اولین تجربه رهبری او با این بازوبند رقم خورد؛ افتخاری تازه برای بازیکنی که جایگاه ویژه‌ای در قلب هواداران پیدا کرده است.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/137694" target="_blank">📅 09:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137693">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
امیرحسین ریوندی مدافع چپ 22ساله سابق تیمهای اکادمی کیا، زسکا مسکو و بخارا کرواسی به مهدی‌تارتار معرفی شده تا درصورت تایید جذب شود.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137693" target="_blank">📅 08:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137692">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
✅
✅
ورزش 3:
❌
دانیال ایری دقایقی پیش از بازیکنان و کادرفنی نساجی خداحافظی کرد و برای عقد قرارداد با پرسپولیس راهی تهران شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/137692" target="_blank">📅 08:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137691">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
فوتبالی: جواد نکونام به رامین رضاییان علاقه‌منده و این احتمال وجود داره رامین به تراکتور بره و باشگاه تراکتور هم اجازه جدایی صادق محرمی و پیوستنش به پرسپولیس رو بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/137691" target="_blank">📅 08:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137690">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYcWGElY4Zk6YcMdAk2D3GjM0EPSzxBAnDeSHIQxekb_cgM5na7UGbqPHq5WIEAliFyYWRwglZZyBClcRYlrHU03FSwmPj5U-NLyqmNLAB4KZPScQ0vqaZlCXoCPohC2ogsUi5vyfmuF0ixy1SfPXjSkFnz9VmPZDNn8vqMjw4FtivfQbRIo82U8ZXFO_-1ghLlCcd1p21feXEN7Xxj8P_0Cujv1oXLJMw4-lPOqcljqD6tZBxyPBoEpoNC9tIZP76bTdXUF4Q0Fz8wrHW7aDoLRy-avK0iI7_1bOPPMQezZdiB49cuzL-Bk7ri26635qUagCqVNvzSMRnNY3oFpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
🇦🇴
لوکاس ژوائو، مهاجم سابق پرسپولیس به پترو اتلتیکو لواندا آنگولا پیوست. بزرگوار از زمان ترک پرسپولیس تو ۲۹ بازی لیگ یک ترکیه، فقط یک گل زده.
‼️
🫠
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137690" target="_blank">📅 08:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137689">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehU7mCpoeYkT_mRYmKtNCVV19O1xA2BtrnjpdfnBwC_M9eukr9vZNUjsFRln6BJmKZax82fPLwv3Xq_j3rjl9uUV7Dw20IAaP5F70uAu3QqjfO6XG9C9okksgFv4-tSpaU21zHhvOkuA0qyv-qjUaVQN7lk8jnMpSnL1w62ENr6Mo4FkmrzMil0_R4J-YENkG6V_1FHlzF88kkJZ62_-iyL8ftH5J5xmQCX29D6v9ry4Q7wBvYvfwdi5A_HgRSei2INRkYVpWsN82USwCrKHZADJhy6iik8CgaKzFRDqIwoXAEo974nx7SHWnU7jdvxNk9QWHUotVcevykbipWbFbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/137689" target="_blank">📅 08:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137688">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNC3nnBliVaPCFsDboImEbUtorKWMWMRapd_GiwGXy4jKNe4_U0s3YqETnbAtNY_Vjj1yCyenDgyz8pJJMh-S3k80A4EARe5ep34NCnZznYD0mJc23rnLSHcxacES0Xt9zGga9YUG6r95Rzh_rcmwEqXbN47uHKWTKTqvqeGGM7hwBFMsbFXbr_mHivUwlhl_JbHSEdKSn3UUMCeGQBBoP3xgSHVMGrBG2JaVu5eFrdmZFUFjSPBXboQaLGAyg5apUYcl1cZvnf-ehPxS2CdN_LPxCe_Is_zeG-P13l_9gpPurKPdEL0QQ5LJSJuIiKW9p2voARHn-QHEmLGbqUrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
هر چرخش یک شانس تازه برای برد!
🎰
اسلات با هر اسپین، ترکیبی تازه از نمادها و شانس یک برد هیجان‌انگیز را رقم می‌زند.
از بردهای کوچک تا جک‌پات‌های بزرگ، همه‌چیز در چند ثانیه مشخص می‌شود.
قابلیت‌های ویژه، فری‌اسپین و نمادهای Wild می‌توانند هیجان بازی را بیشتر کنند.
اسپین کن و ببین شانس امروزت چه چیزی برات رو می‌کنه!
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و با اولین واریز خود ۱۰٪ واریز بیشتر دریافت کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137688" target="_blank">📅 02:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137687">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5QSiipt6xeB3xPg_C9RBN-1GSaW6_I7Ob5p2RGoSNibfuoFRfkUqhvUmlKfo-GBFTdP3u_G50ZmYGfBtNn_d3xfL26ZHqbWRFIOt444O5Jlj_HHnWV0mnO9vHUmGaFnyh9DaV3B2-wCbQLUdRmE2u7kis2FRA9d_sNm4c6NbOikywJ3tpO-Bp8a4O6GDfmstMEO8kLeaY-ODVD7l_WnhIuDU7OjP3TKXIzaR1QHG3nELcIJX0RjphQMKNgskNbq_NnE88l-K7VphzSywlgfBzLSpu7Sm7yJ9iW4dCe2l9ymQxux-mMtOpotMdvws1RkCh-sBDcsn8jfYiUN76abXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤝
ردِ مهربانی، هرگز با گذشت زمان پاک نمی‌ شود ...
❌
❌
شبتون زیبا بهترین هوادار پرسپولیس
♥️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137687" target="_blank">📅 01:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137686">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdydoR3V7hv2pN5IgDHIWh0cLrCGuXDpxhpFLu5CTqajb9-V1HKAWG2ri5eDDNcFTPIto_CvtrnVOWHqdGpadmY5cGJPydFNVIRdjGHzmVnCuVP2Hgz_XkaieB3xLsH5KxVln9z8qCu1aRIOzljjR-hZbFgbXnjTiSAGwf0L3x32LI09R2Drocf18M55TF6Jto5JGXb3KVRJ-370kPY3gsCQsn6TYo_TS9BVexRRmxq_WqVG5hrFmOdDlX1V4HWwO9VDfAKJjuMsZryW7_pn0Mgnalfv4EoGN6G80QrRQPlpYqmVQItUnU42YDAc9yZtdsiLlGSshD715PmXiUMJog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امیرحسین ریوندی مدافع چپ 22ساله سابق تیمهای اکادمی کیا، زسکا مسکو و بخارا کرواسی به مهدی‌تارتار معرفی شده تا درصورت تایید جذب شود.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137686" target="_blank">📅 01:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137685">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
❌
فووووووووووووری
🚨
ورزش سه: با انتقال دانیال ایری به پرسپولیس، انتقال حسین ابرقویی به سپاهان درحال نهایی شدن است
😐
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137685" target="_blank">📅 01:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137684">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
کوروش اژدهاکش، بازیکن جدید پرسپولیس:
❌
اجدادمان گفته‌اند اژدهاکش بوده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/137684" target="_blank">📅 01:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137683">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
❌
تارتار به باشگاه اعلام کرده که فعلا با جدایی ابرقویی موافقت نکنید و هر روز هم پیگیر جذب دانیال ایری است
❌
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137683" target="_blank">📅 01:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137682">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
✅
✅
ورزش 3:
❌
دانیال ایری دقایقی پیش از بازیکنان و کادرفنی نساجی خداحافظی کرد و برای عقد قرارداد با پرسپولیس راهی تهران شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137682" target="_blank">📅 01:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137681">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💢
💢
💢
💢
💢
#فوووووری؛ دانیال‌ایری مدافع تیم‌ملی ایران با عقد قراردادی به پرسپولیس پیوست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137681" target="_blank">📅 00:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137680">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">💢
💢
💢
💢
💢
#فوووووری؛ دانیال‌ایری مدافع تیم‌ملی ایران با عقد قراردادی به پرسپولیس پیوست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137680" target="_blank">📅 00:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137679">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
❌
مبلغ رضایت نامه دانیال ایری فردا پرداخت خواهد شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137679" target="_blank">📅 00:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137678">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137678" target="_blank">📅 00:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137677">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137677" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137676">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
بازگشا، سخنگوی پرسپولیس: تارتار کاملا از اردوی ترکیه رضایت دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137676" target="_blank">📅 23:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137675">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
✔️
شماره پیراهن بازیکنان پرسپولیس در فصل آینده مشخص شد
⏺
1_ پیام نیازمند :  شماره 1
⏺
2_ ابوالفضل جلالی : شماره 3
⏺
3_ محمدمهدی زارع : شماره 4
⏺
4_ حسین ابرقویی نژاد : شماره 5
⏺
5_ حسین کنعانی زادگان : شماره 6
⏺
6_محمد عمری : شماره 7
⏺
7_ مهدی تیکدری…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/137675" target="_blank">📅 23:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137674">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
بترس پرسپولیسی؛ رضا اسدی از گل‌گهر جدا شد!
😐
پ.ن نیاد جای علیپور صلوات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137674" target="_blank">📅 23:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137673">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
فوتبالی: جواد نکونام به رامین رضاییان علاقه‌منده و این احتمال وجود داره رامین به تراکتور بره و باشگاه تراکتور هم اجازه جدایی صادق محرمی و پیوستنش به پرسپولیس رو بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137673" target="_blank">📅 23:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137672">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b26a5d521.mp4?token=AGyh8O0C2h7AEXMmNTjD-2Ti-AofDtCo99-SrEjbokHGA_fBOrIGDaYA8DuS2V6uupgBVTFwgWZFlwQILi4thqH_5VqRvef1zOQp0zbamXu-NXVp1z1L-dV4sqzUOsPxcRO_EHr39gYwUaCAIbYGaxm6DcJozHhD3SfVS3moPm58lsRoSu33Sn2q7GG1TMR-wzKf2czGCGJEXYnJznUdpb04ipVbfLLzyu0JxQ8Saaw8A86siYRYoMrpiI7xdfC5DMgphAIuvTOMeq6cD2O4D8YhD-w2EuN72dmAM4UztPcJziZ6roVIzZy5I3TdWJL3RVvSmx37ff-TfgNddAaw0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b26a5d521.mp4?token=AGyh8O0C2h7AEXMmNTjD-2Ti-AofDtCo99-SrEjbokHGA_fBOrIGDaYA8DuS2V6uupgBVTFwgWZFlwQILi4thqH_5VqRvef1zOQp0zbamXu-NXVp1z1L-dV4sqzUOsPxcRO_EHr39gYwUaCAIbYGaxm6DcJozHhD3SfVS3moPm58lsRoSu33Sn2q7GG1TMR-wzKf2czGCGJEXYnJznUdpb04ipVbfLLzyu0JxQ8Saaw8A86siYRYoMrpiI7xdfC5DMgphAIuvTOMeq6cD2O4D8YhD-w2EuN72dmAM4UztPcJziZ6roVIzZy5I3TdWJL3RVvSmx37ff-TfgNddAaw0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پوریا لطیفی فر: از بچگی رویای پوشیدن پیراهن پرسپولیس را داشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137672" target="_blank">📅 23:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137671">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
❌
محمد قربانی به مدیران الوحده امارات گفته دوست دارم برم پرسپولیس. اونا هم گفتن هر تیمی زودتر رضایت‌نامه رو پرداخت کنه، میری همونجا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137671" target="_blank">📅 23:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137670">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVjoZ61YHqHccqLOF6Sooa6rLFwnXTIXELcvzbuXmqcbrh-xMnEGuTzRCY64dL7Jj8LZRHUUOvcINKBHmtU7NJoDdphNwIEV4SPe33407JagsSoxnR44dN4riMNKGVYB5O6YEcDvdBQa87MS8zIYJS-NcRIqZMVnnTjl1f9wKFQTSlRSeg6bGmSS0CIqJpT8PncP8XcJHbvw1azl90E-8QCMYU-BafMUCcNEtC_n0zEA6np0pJMivsOwGMz0CI_MtCCGmzVA6lH5uVhRG19USq0UB_UF_0X9QPjBKf2emwALIXoIukCfrWir0bBbFQOq9G2XRmcpGYexzqeZk5M5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏
مسی در مراسم ختم پدرش
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‎</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137670" target="_blank">📅 23:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137669">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87be55d80c.mp4?token=LnAyHRcshCuzd0o23xGwyVt3sLPgdzlIoeSzehS6o1xBVZKfy6SLOl-RO2jhoKDVhLZfrNWJcAGPU66abuvoPgojQQ27xu3UoWbqY_8rb_MsAYAt-QaMu5VctcHEFzUFWCqe4p0iL7BK6jibvhbAqj9RkaCqQva6-p5pM4y1Ri0Q7QmHVJRHM2pQzcWph0Sp6ALoV5B1I-BopJvutBvxfOq7rOqyipMKTgRLLZylrqsz69US8zPiPeGUuGpgJ2RFzd7P0deBvCZwUUYm23o2_B1O9-F0ELBuIufxBsc-JqlnFVgEyhmpfp9NfzI_aJIMZhOb7aPC2_h4IubyKMgdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87be55d80c.mp4?token=LnAyHRcshCuzd0o23xGwyVt3sLPgdzlIoeSzehS6o1xBVZKfy6SLOl-RO2jhoKDVhLZfrNWJcAGPU66abuvoPgojQQ27xu3UoWbqY_8rb_MsAYAt-QaMu5VctcHEFzUFWCqe4p0iL7BK6jibvhbAqj9RkaCqQva6-p5pM4y1Ri0Q7QmHVJRHM2pQzcWph0Sp6ALoV5B1I-BopJvutBvxfOq7rOqyipMKTgRLLZylrqsz69US8zPiPeGUuGpgJ2RFzd7P0deBvCZwUUYm23o2_B1O9-F0ELBuIufxBsc-JqlnFVgEyhmpfp9NfzI_aJIMZhOb7aPC2_h4IubyKMgdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پویا پورعلی: شهرآبادی کامل‌ترین مهاجم حال حاضر لیگ است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/137669" target="_blank">📅 22:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137668">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎙
⚽
محمدمهدی زارع: آقای تارتار به من زنگ زد و گفت اگر به پرسپولیس بروی موفق تر از رفتن به استقلال می شوی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/137668" target="_blank">📅 22:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137667">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎙
🎙
محمدمهدی محبی : اگه یه چیز در مورد هوادارای پرسپولیس بخوام بگم بازی استقلال خوزستان تو ذهنم میاد که تا لحظه آخر حمایت کردن‌. امسال تیممون جوون شده اگه به امید خدا این نسل بگیره مثل دوران آقای برانکو میتونیم چند سال قدرتمند ظاهر شیم و به حمایت هوادارا نیاز…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/137667" target="_blank">📅 22:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137666">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✅
محمد مهدی محبی: اسطوره های من اقای مهدوی کیا و شماره ۸ واقعی پرسپولیس علی آقا کریمی رو دوست داشتم. امیدوارم بتونیم مثل اینها بشیم و کارهای اینا رو انجام بدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/137666" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137665">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/412b5348dd.mp4?token=mnCenvhjvWGHNx89M4Ki59xvjd8Sby_oljhg4QDZ0CSNCi-er-BJuZvJVekQFLqsDu4gjnIZGBFOSTRERCKt72CjdsOpKzSmqyu2n-lPYVrU42Ry7D__6l301YQUPZyMtcfag0QWk1pWqurk-B-x5mfjEY-AKPv6_Pb9zC6yh-EHAFT2XZx4DrzXP6dm94ZAdtHHmReEy2TFC1MH80CwM2uxdudh4U7GIlkbuIahm38nf4svc5F7Hh3SzZXWRpNs8XUR9raD950S1q4B9ytbpSFT4VzGldP2sTZn1NOe_ZGd2OXxAbdKqL7MNEKJ7iyNY8iJZ7pGULUiRqVi2wHj6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/412b5348dd.mp4?token=mnCenvhjvWGHNx89M4Ki59xvjd8Sby_oljhg4QDZ0CSNCi-er-BJuZvJVekQFLqsDu4gjnIZGBFOSTRERCKt72CjdsOpKzSmqyu2n-lPYVrU42Ry7D__6l301YQUPZyMtcfag0QWk1pWqurk-B-x5mfjEY-AKPv6_Pb9zC6yh-EHAFT2XZx4DrzXP6dm94ZAdtHHmReEy2TFC1MH80CwM2uxdudh4U7GIlkbuIahm38nf4svc5F7Hh3SzZXWRpNs8XUR9raD950S1q4B9ytbpSFT4VzGldP2sTZn1NOe_ZGd2OXxAbdKqL7MNEKJ7iyNY8iJZ7pGULUiRqVi2wHj6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚽
محمدمهدی زارع: آقای تارتار به من زنگ زد و گفت اگر به پرسپولیس بروی موفق تر از رفتن به استقلال می شوی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/137665" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137664">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
محمدمهدی محبی: آرزوی هربازیکنی، بازی در پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/137664" target="_blank">📅 22:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b7f1f896e.mp4?token=MqkgNgJEg2E6lsJBONkNFopHLsmteho_WzFkBmPN-5FBFxGWxHewSwwBwjdkRBiPt0xFeyEsS97i1lKLXWtUozfdS2HB61dPIgy6Qx0L1KecsrjnJOR4wsKK5cqjea54ipmBvAvrQhBL2vgKHvEvrZ5OvYmkN7MrozFsG8mItPG3Su2dxNLL-GtU260XiIms9nQVkC4k5YePgB7RlAI2kGUM2sEU27s4cQRK2d6espzm9P-KAqmwrKJjZO-49mTzJP0z6B7B7zBCZQvOoGDvzWV0JU7rJ3S8v8K3pPyyXGO53tErx8-_IDKmpHFF-dvn4rPf_wLYN1vi1NPg8miiPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b7f1f896e.mp4?token=MqkgNgJEg2E6lsJBONkNFopHLsmteho_WzFkBmPN-5FBFxGWxHewSwwBwjdkRBiPt0xFeyEsS97i1lKLXWtUozfdS2HB61dPIgy6Qx0L1KecsrjnJOR4wsKK5cqjea54ipmBvAvrQhBL2vgKHvEvrZ5OvYmkN7MrozFsG8mItPG3Su2dxNLL-GtU260XiIms9nQVkC4k5YePgB7RlAI2kGUM2sEU27s4cQRK2d6espzm9P-KAqmwrKJjZO-49mTzJP0z6B7B7zBCZQvOoGDvzWV0JU7rJ3S8v8K3pPyyXGO53tErx8-_IDKmpHFF-dvn4rPf_wLYN1vi1NPg8miiPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
محمدمهدی محبی: آرزوی هربازیکنی، بازی در پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/137663" target="_blank">📅 22:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137662">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f0ef813af.mp4?token=ZiAH363YRaZCva-LoyPn6cuinOCBECkIzMMuqvXhmuE9fAktLyadr2smlUYtnhmKTaSorLjH9vYC4KwKWruxm4Ir9e91WuTQZbPY0V7DYej_MEXQ4YwZJsDPKP2_jGTRs-3iMWfI5EvjweGc9nP1D7OY6A2Tj2l1IiaHWFpa5pMYsauRbT_q3CnRA-1RMw-QCoAGyDsR7EF6qsbpEvrZpUXQ-wLalV0_v2SD6JVgVNrG2vJ2TZyngVlcT-0yEIGtox30B25Y55YU21BmWqz4Cyu9p6W0dGGsZHpo2intcCdirj7EC4H9F7vflDmUeWJcUn--AkrcNjshHEUQFiedXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f0ef813af.mp4?token=ZiAH363YRaZCva-LoyPn6cuinOCBECkIzMMuqvXhmuE9fAktLyadr2smlUYtnhmKTaSorLjH9vYC4KwKWruxm4Ir9e91WuTQZbPY0V7DYej_MEXQ4YwZJsDPKP2_jGTRs-3iMWfI5EvjweGc9nP1D7OY6A2Tj2l1IiaHWFpa5pMYsauRbT_q3CnRA-1RMw-QCoAGyDsR7EF6qsbpEvrZpUXQ-wLalV0_v2SD6JVgVNrG2vJ2TZyngVlcT-0yEIGtox30B25Y55YU21BmWqz4Cyu9p6W0dGGsZHpo2intcCdirj7EC4H9F7vflDmUeWJcUn--AkrcNjshHEUQFiedXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پوریا شهرآبادی: مقابل منتخب کرج وقتی 6 گل زدم دیگر گلی نزدم تا شش بماند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/137662" target="_blank">📅 22:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ceeaa77c.mp4?token=h1UiLsY4_KoNbAP_EWSZIAlx7omONTW25K3r0v1BUy0Y1-8BmEkJTSIXuqSCp6kG40JFtPjdXDSQ1cHI5l_P11oh69BZlZL2Ky33HkVvQ6uHBT1VEAmwaeZPKMmZouzLObidNQALX_e-U35TnY7YwQTDu9vdbtKZG9PRqy2576zFnqaS1bu7nLyUTsaIG3XxfCK_UKhkM7NweHYp8QYfTwPAMy57rcHmZpLryQkkPLO67XvfBKyKkT6HveYQqk79T-JDBKY622EFyIrDA2kSNcGqvr99Uhw6sXaOCrfTItsREDZ8jgfDX2AOIok9f3gfRfZApxgQ9o80mvao4k1pGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ceeaa77c.mp4?token=h1UiLsY4_KoNbAP_EWSZIAlx7omONTW25K3r0v1BUy0Y1-8BmEkJTSIXuqSCp6kG40JFtPjdXDSQ1cHI5l_P11oh69BZlZL2Ky33HkVvQ6uHBT1VEAmwaeZPKMmZouzLObidNQALX_e-U35TnY7YwQTDu9vdbtKZG9PRqy2576zFnqaS1bu7nLyUTsaIG3XxfCK_UKhkM7NweHYp8QYfTwPAMy57rcHmZpLryQkkPLO67XvfBKyKkT6HveYQqk79T-JDBKY622EFyIrDA2kSNcGqvr99Uhw6sXaOCrfTItsREDZ8jgfDX2AOIok9f3gfRfZApxgQ9o80mvao4k1pGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
پوریا شهرآبادی:
🔹
خانواده من شاهد هستند که از بچگی پرسپولیسی‌ بودم
❌
❌
قبل از اینکه به استقلال بروم در نوجوانان پرسپولیس بازی می کردم. در زمان فرزاد آشوبی در تیم نوجوانان پرسپولیس بودم و گل هم زدم. در خوابگاه خواب بودیم که سرپرست تیم زنگ زد و گفت ظرفیت پر شده است و بعد به استقلال رفتم. با دایی‌ام پرسپولیسی‌ شش آتیشه بودم. شاید اگر به استقلال نمی‌رفتم به آرزوی بچگی‌ام نمی‌رسیدم. آرزوی بچگی من پوشیدن پیراهن پرسپولیس بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/137661" target="_blank">📅 22:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137660">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba743cb41.mp4?token=P7L3St0XzUJtBpoNrqpikvRVnUG7i8SetXHHBsivnkFyHq0mC3S8NDKrYLbgxlpKkzS1eIgk12GHcOuCJU9RjgogGoRBFlJLYB8EjnUQB4NIvv7qKngaf-m7-fgRFvVNYROh77K8OEkjY18N2PSDPPmBENT2q2GOavbYYbapNiqzc8gtj2XO9cUANC9QH9N4aILG7XMOs057YnIihCpctM75Bw8crd4YjnANrYxF6n6VBr2KSaycDy-Lff7l6JXsgWRGJ_lWlywiunEtWJwB2pcP9u-LnRiNBRmn4tmdR7pknq1C-YEDM07kSPtGq8X8vguNU0I24IAaEAIEAmqXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba743cb41.mp4?token=P7L3St0XzUJtBpoNrqpikvRVnUG7i8SetXHHBsivnkFyHq0mC3S8NDKrYLbgxlpKkzS1eIgk12GHcOuCJU9RjgogGoRBFlJLYB8EjnUQB4NIvv7qKngaf-m7-fgRFvVNYROh77K8OEkjY18N2PSDPPmBENT2q2GOavbYYbapNiqzc8gtj2XO9cUANC9QH9N4aILG7XMOs057YnIihCpctM75Bw8crd4YjnANrYxF6n6VBr2KSaycDy-Lff7l6JXsgWRGJ_lWlywiunEtWJwB2pcP9u-LnRiNBRmn4tmdR7pknq1C-YEDM07kSPtGq8X8vguNU0I24IAaEAIEAmqXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کوروش اژدهاکش، بازیکن جدید پرسپولیس:
❌
اجدادمان گفته‌اند اژدهاکش بوده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/137660" target="_blank">📅 22:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7ba4ecee.mp4?token=cfnjYBCc39VHmhGkr5fKUET-CajVW1GV3-xTSr62q3DrQIjTEM4k1f4EPaWu1dgC5jBslGXnhfKIe2lXWSmCsIzMF58pyw1U-Bzz_uFjspS1kAOEfB4zpZCWdrNLjKFqJr_4tgQCmArgy2aqCqT7s6eBQDXFFfwFBgVXR9y_9DZpd_DpcmDJxBFWvEi0olMZuAURvzwystduZp9qYU5vhW9mjd7C2vh9h4ghtS9_nH2_kE6zHbmw7hkqxlf6p1zkXTQy2g4tZHwmpVeL61Y1H3QVBDAamdVzYlFnpUsbIS67Ob03uHCyY2fDT2wxWomlqKqv_seFx1zWhE0Zqy6CPbQVip6JrhxNZ46AoCpWaMGy82joQV5oYx34puRBHRmOFWNtjOHTJR949wJrdyeI46QNipm2W3eLCNwj6Z-vYxiBasAWxvJ-9Zqhkgsqw-92P7uPI_Q1WTjpKK7UYGE-X-stXHZixAg8PJr-39ljTdz4ss2r-td8F3hLgs3_etKCJh1DkQDCO_V3cq4RCawPOBCAFYt_-GLSh6y9lDsxhDEzhhkFmDCZFi1v8LwtYGyjpx0fm9KV1slzxjHJvrm2Z9SM-fYqWd4_8V0k86mxXLQ858z2fBz7pD3JM4lKQbphY-HEMiNIlqQ92Zc1pGOtmhXflJATVbH13jaExP6izug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7ba4ecee.mp4?token=cfnjYBCc39VHmhGkr5fKUET-CajVW1GV3-xTSr62q3DrQIjTEM4k1f4EPaWu1dgC5jBslGXnhfKIe2lXWSmCsIzMF58pyw1U-Bzz_uFjspS1kAOEfB4zpZCWdrNLjKFqJr_4tgQCmArgy2aqCqT7s6eBQDXFFfwFBgVXR9y_9DZpd_DpcmDJxBFWvEi0olMZuAURvzwystduZp9qYU5vhW9mjd7C2vh9h4ghtS9_nH2_kE6zHbmw7hkqxlf6p1zkXTQy2g4tZHwmpVeL61Y1H3QVBDAamdVzYlFnpUsbIS67Ob03uHCyY2fDT2wxWomlqKqv_seFx1zWhE0Zqy6CPbQVip6JrhxNZ46AoCpWaMGy82joQV5oYx34puRBHRmOFWNtjOHTJR949wJrdyeI46QNipm2W3eLCNwj6Z-vYxiBasAWxvJ-9Zqhkgsqw-92P7uPI_Q1WTjpKK7UYGE-X-stXHZixAg8PJr-39ljTdz4ss2r-td8F3hLgs3_etKCJh1DkQDCO_V3cq4RCawPOBCAFYt_-GLSh6y9lDsxhDEzhhkFmDCZFi1v8LwtYGyjpx0fm9KV1slzxjHJvrm2Z9SM-fYqWd4_8V0k86mxXLQ858z2fBz7pD3JM4lKQbphY-HEMiNIlqQ92Zc1pGOtmhXflJATVbH13jaExP6izug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🎙
پویا پورعلی:
❌
به مهرداد میناوند قول داده بودم روزی پیراهن پرسپولیس را می‌پوشم.
❌
از 5 سالگی پدر و مادرم برای پیراهن پرسپولیس خریدند و من با آن پیراهن شب‌ها می‌خوابیدم.
❌
از مهرداد میناوند که مربی‌ام بود یاد می‌کنم.
❌
در خونه به خونه نزدیک بود فوتبالم تمام شود اما مهرداد میناوند 5 الی 6 ماه درگیر کارهای پزشکی من بود.
❌
اميدوارم امسال قهرمان شویم و جام را به مهرداد میناوند تقدیم کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTi</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/137659" target="_blank">📅 22:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137658">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc72057e80.mp4?token=dTk6NBat_xQq-5eKWV6GlKlxPyXueEhzUJU3stCHuD37FyyUFbZGlc0GwGVox2syT5L5j9emDWinRa7T4fmeP1E9Two6xyyKjtnb-K0AhqbIcPjuJZkGWLZZFsQ-z7eMcZsmCJ2n0vCRflWapv2GgNnIYgiOtbomSNKt8dZnJkjv-llJp9kM8t8NnFUHd2IKQP_PwVL-Z3QzGjNFSP7YyO-zSMymr9dbEo-RiByFo5dTQgETmkr79zGx2NR-no7P_wpXwtnoZOCquyZ5XLgSrgqwu4H6kmcIZl73d7n6V4cLitJesn9Xb9A7i-TCPIWCWRPd1RB-4LVufwJ18Tvx8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc72057e80.mp4?token=dTk6NBat_xQq-5eKWV6GlKlxPyXueEhzUJU3stCHuD37FyyUFbZGlc0GwGVox2syT5L5j9emDWinRa7T4fmeP1E9Two6xyyKjtnb-K0AhqbIcPjuJZkGWLZZFsQ-z7eMcZsmCJ2n0vCRflWapv2GgNnIYgiOtbomSNKt8dZnJkjv-llJp9kM8t8NnFUHd2IKQP_PwVL-Z3QzGjNFSP7YyO-zSMymr9dbEo-RiByFo5dTQgETmkr79zGx2NR-no7P_wpXwtnoZOCquyZ5XLgSrgqwu4H6kmcIZl73d7n6V4cLitJesn9Xb9A7i-TCPIWCWRPd1RB-4LVufwJ18Tvx8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
امیرحسین طاهری، بازیکن جدید پرسپولیس: امسال در لیگ، حذفی و سوپرجام قهرمان می‌شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/137658" target="_blank">📅 22:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137657">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
بازگشا :
❌
❌
اردوی خوبی در ارزروم داشتیم و امیدواریم فصل خوبی را شروع کنیم.
❌
❌
در پرسپولیس همه مجموعه امسال به دنبال آرامش تیم هستیم تا به سمت قهرمانی برویم.
❌
❌
❌
در باشگاه پرسپولیس ما نمیخوایم پول هوادار و پول سهامدار رو خرج رسانه کنیم. رسانه بخریم که…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/137657" target="_blank">📅 21:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137656">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
بازگشا تو لایو باشگاه
❌
❌
هواداران پرسپولیس تحت تأثیر رسانه در تلگرام و اینستاگرام میان کامنت میزارن که فلان بازیکن رو بگیریم خب ما اون بازیکن رو جذب نمیکنیم چون تو برنامه و لیست نیاز باشگاه نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/137656" target="_blank">📅 21:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137655">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
بازگشا، سخنگوی پرسپولیس: تارتار کاملا از اردوی ترکیه رضایت دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/137655" target="_blank">📅 21:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137654">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5143f09995.mp4?token=bPI7VpSvgC9PlmJjlWdmN_YQg51H3Fj1KSCT5LaRJVbpIhmH1yk7U-5oLf4gmgFbdwaHqyN7tcE4NIYcAWHZWCxFkShI8nPqRREHQ1oK-D-e6oQI64A66J6oL7yteYSqSi3rB9uHuHEnzCUg2PkQ-nuy4XZxuFf3QzS1yXut4YYduaWCLPfbl-iSSGssComqPuqdd2xfUoPJ5S0CASw4n2GUgc86SOA3RE7euqpgBhLaPn5Zm7JJZQTXMze7fb9Gmb1rapD5D8cUpeTq7RIEVX9viF_xnsHV3d854zr7lke0F9OhsCZjHb7Ycw54tLOW9xr0JP1aJnK6J-Y1afQ7Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5143f09995.mp4?token=bPI7VpSvgC9PlmJjlWdmN_YQg51H3Fj1KSCT5LaRJVbpIhmH1yk7U-5oLf4gmgFbdwaHqyN7tcE4NIYcAWHZWCxFkShI8nPqRREHQ1oK-D-e6oQI64A66J6oL7yteYSqSi3rB9uHuHEnzCUg2PkQ-nuy4XZxuFf3QzS1yXut4YYduaWCLPfbl-iSSGssComqPuqdd2xfUoPJ5S0CASw4n2GUgc86SOA3RE7euqpgBhLaPn5Zm7JJZQTXMze7fb9Gmb1rapD5D8cUpeTq7RIEVX9viF_xnsHV3d854zr7lke0F9OhsCZjHb7Ycw54tLOW9xr0JP1aJnK6J-Y1afQ7Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بازگشا، سخنگوی پرسپولیس: تارتار کاملا از اردوی ترکیه رضایت دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/137654" target="_blank">📅 21:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137653">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
❌
تارتار رسماً با جدایی ابرقویی مخالفت کرد/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/137653" target="_blank">📅 21:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137652">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-2_loxN0ne1XUq78J42yr0gvh8sW0M8aERz7DQZk0VPKXeRx52TeIbutltXqrFmghNKMz7RpWiptBDxdfhVR_WgIqW-VcnWgH_fS9CRt3yQLUWADHJwnFQpXL3p2h-8hGBnc2n6A-nrmnKb_Ap1WVekJOxpeaMC6RXvrJ1TZKytqni9H5BQ09-YN-iwTuT7k8489laeFSW-i8zSzUiW_ObCC4Civ_gwRUhf2ScbPsdR5532DYiHFjloveZROcwJ4G_WefewtGPcuYbwheunZ_BxfKP2BqSZgdfnavSIUIj7nKNeEe7G0Ve5o-haBI7buPoGuEKoNg1htgm_IxyJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد قدرت و جوانی؛ شلتون مقابل فونسکای آماده برای شگفتی!
🎾
Joao Fonseca -
🎾
Ben Shelton
🎾
فونسکا بعد از برد مقتدرانه مقابل کسپر رود، با اعتمادبه‌نفس بالا وارد این جدال می‌شود؛ اما سرویس و قدرت اول ضربات شلتون همچنان برگ برنده اوست. شرایط هاردکورت مونترال و بازی شبانه می‌تواند به فونسکا کمک کند، ولی اگر شلتون درصد سرویس اول بالایی داشته باشد، کنترل رالی‌ها برای برزیلی جوان سخت می‌شود. بازی نزدیک و پر از گیم‌های کوتاه؛ شلتون اندکی شانس بیشتری برای صعود دارد.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و با ۱۰٪ بونوس اولین واریز پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/137652" target="_blank">📅 21:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137651">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFUaVUlGKjckDxCechVOloRjGHADVheHHecymP8uDT7xBtu56BmpRtv3MchgD8Ks5i0ZNUgukYsWMW7-DBnkXETQBhzOZHBuu17H7stgz4o8SvFaMl-662ADRdwgg3JTuWgPoEEB1ed8CBtyh_83oI5NgoWI4sleyPeDfxNaAZlCgHz7lAUY2aR3iDCbWEi_KJEAmiSAGTfB8wT0zM6_MSwjHe0jN3FwfSktu9fbzR5NEnrvj_IMmVE6GdL5OvKFP08wU7cdYSQNF_iCJvR8W1UBP-ZMJVUQ-vdK7mCnwTqU7vgLemzNTCbIBNBKRskQxGr6ND28ovaOhUB_krN9cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مهدی تارتار با پسراش پیش از بازی تدارکاتی امروز که تو منتخب کرج بازی میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/137651" target="_blank">📅 21:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137650">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
❌
محمد قربانی به مدیران الوحده امارات گفته دوست دارم برم پرسپولیس. اونا هم گفتن هر تیمی زودتر رضایت‌نامه رو پرداخت کنه، میری همونجا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/137650" target="_blank">📅 21:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137649">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
وحید فاضلی در گفتگو با ورزش سه :
▫️
ما حداقل به 3 بازیکن دیگه نیاز داریم تا اسکواد تیممون بالانس بشه. در یک پست 2 الی 3 بازیکن داریم ولی در پست دیگه شاید 1 بازیکن داشته باشیم. پرسپولیس مثل تیم ملی باید 2 بازیکن تاپ لول در هر پست داشته باشه.
▫️
از ابتدا…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/137649" target="_blank">📅 20:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
میگن دیروز تو بازی دوستانه تراکتور و شمس آذر شجاع خلیل زاده بعد از پایان بازی با محمد ربیعی سرمربی این تیم درگیر میشه و همراه بیرانوند شبانه میرن سراغ زنوزی و خواستار برکناری ربیعی میشن و ربیعی هم همون دیشب حکم اخراجش میخوره و برمیگرده تهران و بجای اون نکونام…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/137648" target="_blank">📅 20:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137647">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
ابرقویی به‌خاطر نگرانی از نیمکت‌نشینی در پرسپولیس، به دنبال رفتن به سپاهان است
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/137647" target="_blank">📅 20:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137646">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
✅
✅
باشگاه نساجی به پرسپولیس اعلام کرده است تنها در صورت جذب یاسین جرجانی از آلومینیوم اراک اجازه جدایی دانیال ایری را خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137646" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137645">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
اعضای کادرفنی تیم پرسپولیس :
🔴
سرمربی : مهدی تارتار
🔴
دستیار مربی: وحید فاضلی
🔴
دستیار مربی: علیرضا محمد
🔴
دستیار مربی  : رضا جباری
🔴
دستیار مربی  : کریم باقری
🔴
مربی دروازه بان : حسین اینانلو
🔴
مربی بدنساز: یاگو
🔴
آنالیزور: میعاد قاسم زاده و محمد کهن  …</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/137645" target="_blank">📅 19:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137644">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس در دیداری تدارکاتی، منتخب کرج را با نتیجه پرگل ۱۱ بر صفر شکست داد.
✔️
✔️
سرخپوشان در نیمه نخست با گل‌های ایگور سرگیف، یاسین سلمانی، امیرحسین محمودی، علیرضا همائی‌فر و مهدی تیکدری، با پنج گل از حریف پیش افتادند.
✔️
✔️
در نیمه دوم نیز پوریا شهرآبادی…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/137644" target="_blank">📅 19:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137643">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
پرسپولیس نیمه اول بازی دوستانه با منتخب کرج رو ۵-۰ برد؛
⁉️
گل‌ها:   ایگور سرگیف، یاسین سلمانی، امیرحسین محمودی، علیرضا همائی‌فر و مهدی تیکدر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/137643" target="_blank">📅 19:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137642">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه پرسپولیس‌برای‌فروش‌حسین ابرقویی به باشگاه فولاد مبارکه سپاهان منتظر تاییدیه مهدی تارتاره. درصورت اوکی دادن تارتار ابرقویی راهی سپاهان خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/137642" target="_blank">📅 18:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137640">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_0WpC-sIMbQ19_fdX_If83eJ1Me0OjMvZztFU_5bjZEtmM0O1cHgwElaz1pLXl6Qmo-BCyNi9AKJuEvGiC1CeaF2QEssNE-vY23_Xnhafn9FldATwGXZag1yFeLQVRm1w4pI2e28kLkDoSH7UetljH_9L4zMb1IvPA4R9ggVEKrZXkgfp0l4TrTw8vL3kVV-i2K4iFnnCel1px79-s1eAU8yHF9z-OlNu3PW5J0Kic4N9fyi8DPpGdpOE987okJKain5kHPSWp4BViAp8Gt5sNjn5z8UiXD6IWAie6VkLzMTOxtJk720x9gPkKzXLN0dW7IIL1VeoNWfAUl9P746A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس نیمه اول بازی دوستانه با منتخب کرج رو ۵-۰ برد؛
⁉️
گل‌ها:
ایگور سرگیف، یاسین سلمانی، امیرحسین محمودی، علیرضا همائی‌فر و مهدی تیکدر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137640" target="_blank">📅 18:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137639">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
باشگاه سپاهان اصفهان امروز برای چهارمین بار برای جذب حسین ابرقویی نژاد به باشگاه پرسپولیس نامه زد ///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/137639" target="_blank">📅 18:12 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
