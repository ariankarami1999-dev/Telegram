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
<img src="https://cdn4.telesco.pe/file/qBw32K-FIc_TpGgH61CrFSkFQTB4ZAdIwC8LWVgOZcRXAZ8vDFQjpaJIfJHq2pg7mKBvAyqOw3Gaoq1RLUcVH4kr3T6bB8T-rIsSfMIhUCqkh_mEEompaHlUEHV78ohDmezAUBxGJvfVVkxTC3V6slEzO13UcutMAitu-2qlsL-mEWHFpno1Et1XeP9_x4fVpH3NSTNea59P2n5-ABUtLqufxRMu2RPqtpdvIMBtM5WvOgG4qKEAe5WIS0cnUitDc3U5W8i2LE-Wki0HAIhIGync_jJCc6SPGab3MRfgXeA1kzOPps_IYcP6IAuOCWcz3qnDiw8ubJK6yajS0G0zJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 13:38:17</div>
<hr>

<div class="tg-post" id="msg-136588">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
❗️
درویشی وکیل ورزشی :از نظر حقوقی انتقال کسری و ایری از نساجی به پرسپولیس خطرناک و ریسک بالایی داره..
🤔
امیدوارم مدیران استعلامات کافی و گرفته باشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/136588" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136587">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
با اعلام ترانسفر مارکت رامین رضاییان بازیکن آزاد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SorkhTimes/136587" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136586">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/136586" target="_blank">📅 12:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136585">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❗️
پرسپولیسی‌ها نخستین جلسه تمرینی خود در اردوی ارزروم را در سالن وزنه‌ پیگیری کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/136585" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136584">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
✅
محمدامین کاظمیان بخشی از قرارداد توافق پرسپولیس با گلگهر برای جذب پوریا لطیفی فر می‌باشد
🔹
محمدامین کاظمیان + حدود ۸۰ میلیارد رضایت نامه = پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/136584" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136583">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
شنیده ها:قرار بود دیشب از پوریا لطیفی فر رونمایی بشه ولی به خاطر بازی تدارکاتی گل‌گهر، جلسه لغو شد و به امروز موکول شد
🔴
امروز به احتمال خیلی زیاد، پوریا لطیفی فر پرسپولیسی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/136583" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🌀
🌀
امیررضا رفیعی این امکان را داشت که قراردادش را به‌صورت یک‌طرفه با پرسپولیس فسخ کند، اما فعلاً این کار را انجام نداده و منتظر است تا باشگاه ابتدا گلر جدید جذب کند و سپس از جمع سرخ‌پوشان جدا شود.
⏱️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/136582" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136581">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCnrj6L6hA8qyNYO1k4PCW93s0koUXeeF9Rek94LVKNuD1R7xLvh5h9w6MyLP-KVfQq3xFHSotRRmPQ5z_2sRVnTtX-zKRmCMtXink5PQI6WxrR0LW-lv2OPw8zku6X5Gmxf8rgVpyBe3Gm3QlaJmdIYiVjO3XwgDvHp05r-qY5A9qGZQ489Hil6MgQl2ok9iE5grGzf63Lfl7Z49Y1ZwUvyE4gyLPkAICx0ku9i9ZE4z-OSWBIlqSWu2jYsu8nr46ucDFmYR8atnWm3AjWwT-CK4Tm5jnFGM75FMKtQxnIqXhvbmWPL1OOSnjFx2QXeQ-pLQl-jqE0tn-I6v_k2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سؤال بزرگ؛ ثبات یا آزمون و خطا
✅
❌
🚨
درویش تو سه پنجره نقل و انتقالاتی آخرش ۱۷ خرید برای پرسپولیس انجام داده که ۱۱ نفر از اونا از پرسپولیس جدا و افرادی مثل بیفوما و کاظمیان هم در لیست خروج قرار دارند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/136581" target="_blank">📅 11:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136580">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/136580" target="_blank">📅 11:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136579">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
❗️
هنوز قرارداد اخباری، ایری و طاهری امضا نشده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/136579" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136578">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/136578" target="_blank">📅 10:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/136577" target="_blank">📅 10:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136576">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB_3l2CHDFHbVp9VoPlO9D24kR8mgP8gj4mUy4xTAWKJJ5Fj52lFmxk1LWuWAyO0lpNu4P-J8UUtCq7EBdWNRmVKrol5c0BMdG4mv5nHdpeY1OZpeUUF6m3UYypEaHXtJ5V-WPZSLmnJtoPmf4NqNMXu9QRHZm_bxhWZ6H_qIAD_iHFvVVWvUPYsnNF8lAev0_M_lzJNtoh1HUe12GoKYEkmQep-F7A0_ZZ4N2LrEBpxl-1yTgbEQ8lA_eAdwJ_tdBflTaHCzgEl92LS5yaKr2aHiSK6tcRVFy-GOoj4TIwsm2SMgEd1Iwdb5HXvGbpY2DrwVrxhG1ylNvXU56bz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
با اعلام ترانسفر مارکت رامین رضاییان بازیکن آزاد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/136576" target="_blank">📅 10:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136575">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
فورییییی از رسانه برزیلی UOL: جنگ بین آمریکا و ایران مستقیما تو این انتخاب نقش داشته و ترامپ در انتخاب داور فینال جام جهانی دخالت کرده
❗️
رابطه نزدیک اینفانتینو با ترامپ هم به عدم انتخاب فغانی کمک زیادی کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/136575" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlQmV4AqwAyLoL6mQfROuvSyEvSVujX50k-q-wGsZbgsDtd0wjM7og4n9I136zdqqE-f98vHfszqK5pZ6TYfznUPAq1LTVTECHpHYTeY70badTwqZGl84cP6eImqy8MNJoFueVZTbsrPURzE4YPu3deQm94Av9CHhrw-3W4TzxK_hTGcNRT2c18ETxE6pvIm9qAohTPlVLX54rwKoMt4bqyK_DTSlM6FOkIdC_fm0J2Fc8tID1HT5DtuT_O1Asw7xFS_o1aF2GLMDv9Ny8y_pUPLcV_wAq0nVM8CukV-hql2uQOHTS5I-g8O9qoDBAtJUVCLcBjyj2OI-_23QgV9ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تارتار در گفتگو با پیمان حدادی از وی خواسته که هیچ‌پیشنهاد خارجی را برای اورونوف بررسی نکند چون این بازیکن اصلا فروشی نیست و فصل‌آینده ستون اصلی ترکیب تارتار خواهد بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/136574" target="_blank">📅 10:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136573">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🫥
🫥
شایعات: محمد قربانی در لیست مازاد الوحده‌ امارات قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/136573" target="_blank">📅 08:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووووووووووری از هفت ورزشی
🚨
مذاکرات پرسپولیس با پوریا لطیفی فر، هافبک ۲۲ ساله فصل گذشته گل گهر مثبت پیش رفته و اگر اتفاق خاصی رخ ندهد، لطیفی فر هفته آینده بعد از امضای قرارداد با پرسپولیس راهی ترکیه خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/136572" target="_blank">📅 08:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/136571" target="_blank">📅 08:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136570">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136570" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136570" target="_blank">📅 01:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136569">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOyLskX6gkohgrb190DwxnTDZPX72Inm40HDfWaHGhcHduQNG9smQpoDcfut6MoSJ0i-QU5eV5U-HNeBhQ0s4U2dGR_kPm2uuTjd9NjYB3kYTrtzsUdKwD_y4K6IO1DDRYLhuER93bXaERCSZ6jaz1xWFf5btIl9tnb5_f9WFAGfjFfVAUCx8bPNUlNibtStZJnroUOzIhEasxpskWPjw-P0t4LtEML7eMW8MIHruMLXP_OQwrPiDVOM3IaMH7kL5gLWRff35fnglI-MtxxwRcHUQucMDt3013Nw8RPjb39rL7djsAzjQxqAs3KGwMh5mfNJf2QBxPoyoGBhOdVaBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136569" target="_blank">📅 01:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136568">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
🔴
فووووری از تسنیم
✅
مشکل سربازی بیرانوند دیگ قابل حل نیست و امسال یا باید بره ملوان یا فجر سپاسی
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136568" target="_blank">📅 00:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136567">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136567" target="_blank">📅 00:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136566">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136566" target="_blank">📅 23:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136565">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136565" target="_blank">📅 23:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136564">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
❗️
زارع به اردوی پرسپولیس اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136564" target="_blank">📅 23:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136563">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JT-3ippX2Vbf5bGesPSZh3ezEYRcRLep8RAHGMQ507ynHbjKdE5ioiydH1R1e0OcSQIca2R1wODdWgifbksUJBjtxH0xqLYlIeI4nza9a4u_r6IbqO86mArAqRZcF2r6hOX5pWSpCQgxqbPh6mRJ4flrm3d01XA7mVFF4GxwpH5gLaUnxw1H2q4hV7g-pDlHKf8F9SpeUNfbx2Wl41ccx4iuwJfvypJsC4OIfjOK1SZ_fJ3Uyqv_iA6sDloDPG8UTCXuKg92Jatm3B60UyZgqfCwz4FaLK2ZBsT3bnmBoXO_XkPwKRRN4zZxtJbQyimpmjbw2pEdHLLgQRuSVaLUXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
پرسپولیسی‌ها نخستین جلسه تمرینی خود در اردوی ارزروم را در سالن وزنه‌ پیگیری کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136563" target="_blank">📅 23:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136562">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
کاروان پرسپولیس دقایقی قبل وارد ارزروم ترکیه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136562" target="_blank">📅 23:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136561">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
✅
رضایتنامه‌ی قربانی خیلی سنگینه و کنسله/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136561" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136560">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
رفیعی خودش قراردادش رو با پرسپولیس فسخ کرده و حالا دستش بازه هر تیمی خواست بره. احتمالاً هم راهی گل‌گهر یا شمس‌آذر می‌شه و اخباری جاش به پرسپولیس میاد.
✅
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/136560" target="_blank">📅 22:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136559">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
#فوری |ترامپ به شبکه 12 اسرائیل: من در حال بررسی امکان انجام حمله‌ای بزرگ‌تر از هر چیزی که در گذشته شاهد بوده‌ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136559" target="_blank">📅 22:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136558">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
فوری از سپهر خرمی:
🚨
بعد از کنسل شدن تمام گزینه های پرسپولیس در پست هافبک دفاعی، مسئولان این تیم دوباره سراغ محمد قربانی رفته‌اند اما اینبار با پیشنهاد بهتر!
🚨
قربانی از تراکتور هم پیشنهاد خوبی دریافت کرده اما تمایل داره به پرسپولیس بیاد!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136558" target="_blank">📅 22:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136557">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136557" target="_blank">📅 22:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136556">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLUgpTYk8e2QsDtvP6AK2mvv_20dVKoPfjZPuQwt-Jspi9SiGNp_r6-cRIOa6MLdboUvIgoe6lE4gqLhL4110I_tzp5Dtpx5YgdHvFbsL8KgmlH77CYjkt1npEcK2wcV_prbbLPpWbOZbQmQA9n-5JpnONksrZ7kIrVDT5ShA2Kj-S3Hc9ZMtUS9Iq2dhmYtdST09GXHhguLcfo2N2O_bllNeUH7woD4oUGCPwEA27niex8CMNjSpqw4xg1_QSj20qFWmy79SHCw19x8o0KIZNDVP1a51vKybnsp5jF4u5zjIkduXMN4V9odwrwj0HXy-iZZZkg3YCqGNxT1JlLBkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاروان پرسپولیس دقایقی قبل وارد ارزروم ترکیه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136556" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136555">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
قاب ماندگار بازی پرتغال - اسپانیا؛ دلجویی یامال از رونالدو پس از سوت پایان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136555" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136554">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
مرتضی و کاظمیان با تیم به ترکیه نرفتن و جداییشون تقریباً قطعیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136554" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136553">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136553" target="_blank">📅 20:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136552">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet.apk</div>
  <div class="tg-doc-extra">54.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136552" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
جدیدترین آپدیت اندروید اپلیکیشن 1XBET
🍏
برای آموزش ثبت نام مخصوص کاربران ios اینجا را بخوانید.
✅
ورود / ثبت نام از اپلیکیشن
🎖
بزرگترین اسپانسر رسمی لالیگا
🔵
بدون فیلترشکن
از اپلیکیشن استفاده کنید</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136552" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136551">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSRklsr3jFhcHjTAei_OxQLLzfeunEa9lADo4UqoEjsL_XSbUJoTO0tjVno7-hgd2R1JyG8Tw4OCQPsjAJARbnBUknpoeipejY1toWC4QHXenRToOv7rcdFWoYCHHIG2YxIqlzRTuloNI3Fr9bP5sGUCEL_PjsAXeCsWnWDh_Xkyc0nnSh_KOdozWVf4wbsL_iT6iPmzH7MM4_fMqr4ZcexlPwS4-76rVtdDErjgMg8hyRn_QK4U4FjhWXepkNu0reKq3TgpcjfnW_z7DNnGiUKpD9zqkBBJtjxyjjEDVxbgFMEhvA1CzXi45GYAip_9kZ3GESVrLdBxawGm-rY5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1️⃣
شما هم به خانواده
1XBET
بپیوندید
1️⃣
🏁
جام جهانی تمام شد... اما هیجان فوتبال ادامه دارد!
⚽️
🔥
🎁
پلیر ها پس از 5، 10، 15، 20، 25 و 30 روز متوالی، پروموکد Freebet دریافت خواهند کرد که تا 7 روز اعتبار دارد
🔔
آموزش ثبت نام و واریز
🟦
آدرس وان‌ایکس‌بت:
🌐
Link :
1XBET.COM
🌐
Link :
1XBET.COM
🛑
برای ورود به سایت از وی پی ان (فیلترشکن) کشور های آسیایی یا کانادا یا ترکیه استفاده کنید.
➖
➖
➖
➖
➖
➖
➖
➖
🌐
Channel :
@iran1xbet_official</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136551" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136550">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🥇
🇹🇷
تیم فوتبال پرسپولیس برای برپایی اردویی ۱۲ روزه تهران را به مقصد ترکیه ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136550" target="_blank">📅 20:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136549">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136549" target="_blank">📅 19:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136548">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpSjBKuzdLnXSeAGoNTHMUsrO5hhjsUreNw3SGd4aEgOT6oZmtCtCS4zJHVv3dDZWWNukjA_aRPINpMrW1DCcRV_6aezvgYanEUe6pAbh5jcT7N8QAjKN--VIXr2WIHqcDhqwFM_Lv3n8zWZPfoIH-LPPRFTxzlo0W0AhCMkVG0_L7q_1nzx-nLZNvBQOsUJycBzdg0IKYxvzb4spsOUg0i844KVi9YxJjK7NaqM-oNL2tshAequbW6Sc32go-1EB8mbVEJTONYdusyRyBd22fMn6NVExM9BeUNr_xdzGBywWNDcEIwPS-cMPJOZE_W3SvRV7FuEvWEDp4cRunxoAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136548" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136547">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
❗️
هنوز قرارداد اخباری، ایری و طاهری امضا نشده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/136547" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136546">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔹
فوووووووووری
😐
🔹
ترامپ: دستور دادم در های جهنم به روی ایران باز شود  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136546" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136545">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIaC_zPlT6OYWQ50HqgE8jQN972w9mJQIvWZRW62hzCjj8d8yloVUm8Yx7axzN-v9GYqYCQOEJoIYC3yRWHMEkZHz8EjfnlM0ToxYeFOkVaTv1alr-9Cs2BB1ATqKjnAMKkbrgVa6M5TqU9eK2y62NJ_op3yaCJmOmDKUh_oUHwFth3IQZ4jAyMQPC7aWSqA0d5xYldqOQQA3pjP69WNQqlYuuaqPaB-S288dw_iOq-qGnxutHWU-GCNbSni8SdymCY_xAOd2u4ofsbk1uLV3z-hTRTq8_UzGecSxYgG9I4MdFC6fr0McimsRXZ5EzKrxv3FDPr4t81pXxcxlmfAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیپور تنها بازمانده نسل طلایی برانکو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136545" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136544">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=E3B62XBFIGh92qEY8FJLQv1yrF9fIxxwlbR53HDHTXt7Eivddj2bBMBnFUFkaic40r4JFOFWvcSVSjXUswi-yTClP0-h45KxHL0O3LBP7IvPHTJCyIQM8bwH3my7vvlqd0YNuYUv3OUci0dWX_hKoFRNGvGa8dgGhbhUjVjHBATyHrqQyxtn5jhYnobNuRKptQjSZjcsWZPCJs3kml_CPCUCQpxNucYUM-WoGHuzZQdWhdjV6EojLuN9F2ipwS-yr1qaK0xXKNoZ6xXkZbBczIu4mrzj7wlGBEdH4K72Mv0cC0uxcFWCsIlGptGY-9cJ9NmlXQiiSU-aPAyFdlR7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=E3B62XBFIGh92qEY8FJLQv1yrF9fIxxwlbR53HDHTXt7Eivddj2bBMBnFUFkaic40r4JFOFWvcSVSjXUswi-yTClP0-h45KxHL0O3LBP7IvPHTJCyIQM8bwH3my7vvlqd0YNuYUv3OUci0dWX_hKoFRNGvGa8dgGhbhUjVjHBATyHrqQyxtn5jhYnobNuRKptQjSZjcsWZPCJs3kml_CPCUCQpxNucYUM-WoGHuzZQdWhdjV6EojLuN9F2ipwS-yr1qaK0xXKNoZ6xXkZbBczIu4mrzj7wlGBEdH4K72Mv0cC0uxcFWCsIlGptGY-9cJ9NmlXQiiSU-aPAyFdlR7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
استوک صورتی با کیسه فسخ کرد
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136544" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136543">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_s4FxwBd-h2R1XWUYzyMsJS3JugrKzhg6VDmnCKww1uocB9jdLWPIxrCjNRC5NCoMv8hz5qhDv-KkdHph5tATZUs3RJjirC3CKVJLEnHEVqw66MxhIt902rua6UI8MGdD-oRwjpXk_O3Gjeol3HsJxUXHpKPgSYUR8UFf73jvYHgP0sJ-BDeBbDQXvojLhnBjkwfWV5G_QsRA8-bSQbrCQW_KfUtxZwp6Vh7JMT4z4DaLK0TjGK8TywMf6bwYev5S0fg4Oy_uawKHnbN42Qdlx7Q13Cz16hs3akX1M-IG5_Cp9H2QaQ_hVvO3xxK3VaOKxS7Gi5yioX109ltC4-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از تمرینات خبر رسیده پویا اسمی کاپیتان ۱۶ ساله تیم نوجوانان یکی از خوب های پرسپولیس بوده
🚨
این بازیکن در این سن با این فیزیک و قد مناسب شدیدا آینده داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136543" target="_blank">📅 17:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136542">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9SHKabZbhAHHuhOrneO_9Ytlm53I-twjSgiIgvKEiOQ94-M59JS7CMffjMSx2-XYqeiwMCG7WeIxKr9YUNeTxXlDmJ0Z94b5yy5H-KO_07sk1uuHwgllcCu-q54D7wZFiVJ36E4iA6-MaRTgwO-zocXX1ECtn4-C-BCNxIedjIEz-U7kt6za41w5PglY1DMF6nlDe5ZEA6F6rN7mXscniF4eZ6_0R5qL67etkBaIwJ_0Tmumw9M3_JvtBUCi1mLzLdd0A7ddL-4v5r5XII9k9TDnHY1o4JtX4lTsj4gGJIM_gKFK1KVX5uiWMjycu1EL9yK2WJ0saf37ILOfFWPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
🇹🇷
تیم فوتبال پرسپولیس برای برپایی اردویی ۱۲ روزه تهران را به مقصد ترکیه ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/136542" target="_blank">📅 17:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136541">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
✅
طبق شنیده ها   احتمالا فردا باشگاه از سه تا بازیکن رونمایی خواهند کرد .که شامل محمدرضا اخباری و کسری طاهری و دانیال ایری هست.
🔴
باید دید چه اتفاقی خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136541" target="_blank">📅 17:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136540">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeFb1zQhXwXV9PhdPCrzCr2mS-8x38CvYIUIEdYQo5-ZlGZEwPOgReWZp2wVm91g_O_XatDHl0WFa_7x4bDIFKXxrVHeM6fFuTRVwUX8pnAE0MfxCAh7UrpAj6RnaBumNz_ikp5cioPPEKuLQeLtrTEDTEY2ssNeWKQy7uVwmDIil2d1l3NaurSJ8fBrF87wh6xTW73UIkIudh1O9V32WfGvyDYDd-by0bsdMMgy4yZ6NU8MTQmHvKil6eIRjNdnXve9ZkimipOeJNC79qRduhjeukbIeno7SB6IuQ4rUozse3UVD_vR6iiOFF1ktaagAxVdBOIVdZ7eHZW0FxWx5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیم رفت ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/136540" target="_blank">📅 17:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136539">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875cf546b8.mp4?token=nbi6dIcBDAJxq5XTwdjXGiKN5_AAhE5rY6juTUCQ8L87iMhLuL6E4QMVzfNqLElVVZX216vAEs0oE806U8vQcLeN8eWNZifBxOeAX3k6bOg1yTO5sI6dS3Sm9U7MnGvf4pq-7rgHfJiM-UHdV5VmVILcANis5WibSNYYQ5_14NxIBwEwPWgVTXx-7HfHKRklw6IvXnr4zse4uOzE-0OGYuVQekMlom4C5CnjbAQlF_CVjx8ESCBbtgj7AXl8QfYcP7tnJdx6RSWjx7FfemtTa28ezmi8MF9t7Qk62RqkC5mqeR0D_MEEZTO88_n-k7oapw-EMKaBJ2zY91g2vDgmFnBOxYMxYjezSCDBgriErCY_t-Usb2XwN6sXwpFu4QaPN7JbzT63f80GxaeybB68-cIdR_-Z_lvpFubebaLc2vB-P2ufLbUs0lUFnJZEq3tUDSYo6c0btrYV6l90DqKQs63lVyINWU0xl3xArHEbiJEwLoj8AlIVGem2P8vv3tWwSe337HV2jR5Q0eNzfpynbAEKChyDvs8QvkDQlBFTE6Bq_hEnaKSHWqzTTKI7Lz0AqIM3HRxzr0Z98du3Bp_ztm5l7OITIqwK8emuObB8He9IgJgy24yBaXlhksB_kLiiTuabeJGOb7c9Qvu8kpeFiIjIW3Tz7cdl9ycI30mfmFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875cf546b8.mp4?token=nbi6dIcBDAJxq5XTwdjXGiKN5_AAhE5rY6juTUCQ8L87iMhLuL6E4QMVzfNqLElVVZX216vAEs0oE806U8vQcLeN8eWNZifBxOeAX3k6bOg1yTO5sI6dS3Sm9U7MnGvf4pq-7rgHfJiM-UHdV5VmVILcANis5WibSNYYQ5_14NxIBwEwPWgVTXx-7HfHKRklw6IvXnr4zse4uOzE-0OGYuVQekMlom4C5CnjbAQlF_CVjx8ESCBbtgj7AXl8QfYcP7tnJdx6RSWjx7FfemtTa28ezmi8MF9t7Qk62RqkC5mqeR0D_MEEZTO88_n-k7oapw-EMKaBJ2zY91g2vDgmFnBOxYMxYjezSCDBgriErCY_t-Usb2XwN6sXwpFu4QaPN7JbzT63f80GxaeybB68-cIdR_-Z_lvpFubebaLc2vB-P2ufLbUs0lUFnJZEq3tUDSYo6c0btrYV6l90DqKQs63lVyINWU0xl3xArHEbiJEwLoj8AlIVGem2P8vv3tWwSe337HV2jR5Q0eNzfpynbAEKChyDvs8QvkDQlBFTE6Bq_hEnaKSHWqzTTKI7Lz0AqIM3HRxzr0Z98du3Bp_ztm5l7OITIqwK8emuObB8He9IgJgy24yBaXlhksB_kLiiTuabeJGOb7c9Qvu8kpeFiIjIW3Tz7cdl9ycI30mfmFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علی علیپور: از آقای قلعه‌نویی تشکر می‌کنم که شانس حضور در جام‌جهانی را به من داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136539" target="_blank">📅 15:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136538">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/136538" target="_blank">📅 14:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136537">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8ANVgSqkoJkeP_VxW-KfcQlfnW0_wig7E_nIYH8-CiWKaxOCqmzHwpPThEZB1SLQaux7z1VBxrUPmoYB2xeOgzkwhmoG8cCH9ZysZaSY6cNSsmHTDkt02TeVY6sDsU-F--ceBMvbWHuLoTHddvdQPhVL7lzI7WpH2T4r276bCmzOWyNJg7XNsgEeEotRUTjnPZF6J2fJpvKOpz9SqLfmvOh5wcomS1UuCpJ601P3j5_F0xYm32IJtRTjnA0MwqoDBkZ1AdIxTgj6q8SrqFzN1mf1asCjy1gUxh0qA5yV7qVE6uN112OKxOkHcJbOhviEEafRW1MphlBEKtvtZeuZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پرسپولیس امروز برای برگزاری تو این کمپ زیبا و
اردوی ۱۲ روزه راهی ترکیه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/136537" target="_blank">📅 14:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136536">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
میلاد زکی پور، مدافع چپ سپاهان پس از قرار گرفتن در لیست خروج محرم نویدکیا، به پرسپولیس معرفی شده تا جانشین میلاد محمدی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/136536" target="_blank">📅 14:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136535">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
فوووووووووری از ورزش سه:  دانیال ایری و کسری طاهری از نساجی به پرسپولیس پیوستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/136535" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136534">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/136534" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136533">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
شنیده ها: محسن خلیلی ساعتی پیش با حمیدرضا گرشاسبی برای انتقال ابوالفضل رزاق پور دیدار کرد و قرار است در صورت توافق شخصی با بازیکن و واریز مبلغ رضایت نامه این بازیکن راهی پرسپولیس شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/136533" target="_blank">📅 12:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136532">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
با نظر مهدی تارتار ، محمدحسین کنعانی زادگان به عنوان کاپیتان اول پرسپولیس انتخاب شد / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/136532" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136531">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
مخالفت AFC با درخواست فدراسیون فوتبال ایران؛ گل گهر نماینده ایران در آسیا شد!
🚨
🚨
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.…</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136531" target="_blank">📅 11:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136530">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
✅
پرسپولیس انتخاب کاپیتان را به تارتار سپرده؛ احتمالاً رقابت بین علیپور و کنعانی است.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136530" target="_blank">📅 11:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136529">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
✅
طبق شنیده ها   احتمالا فردا باشگاه از سه تا بازیکن رونمایی خواهند کرد .که شامل محمدرضا اخباری و کسری طاهری و دانیال ایری هست.
🔴
باید دید چه اتفاقی خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136529" target="_blank">📅 10:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136528">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM0sOH1nBzSODMtHr-3nSZo9ziRJJlyzYxyO3RDxBOXpnEZtXgvGlodHLWAajDc_vnqNJvHo5QX9TA-RuHVzoqau21TroXzka0jt1Q16nIuWOQn7euKK7kFNSdMdXU0abDnMw588o58jdMSjB9B0_T1tWepooOahQ0RjfFaBFNtogkHCelS1OvlX9lzk6TrYLQX7wCQZJr5mkkcmKAjWj00tfquHJuE06L5M3-YMTauq9ubeon4wD1YbBKES3aNfb902bGShzos-amI0Id9V8PSBmaUDRjLRtvChXeQ8wzOv_bULR1QLbuO8D3vDvnqEpnuGQKi1tmFmqxibMQ8c_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
خط دفاعو ببین پسرر
...شیر پسر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136528" target="_blank">📅 10:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136527">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d8vPT6t4Ji9pXViOSIX_An0uaBisKQAF-ynhL_c9d3SpTxT0tInsVJRoZM_1YuKIqs6SBBz4TjrSP71_QGmg9GAUsih1E5h8VuV8CpVtEY6hmNc1d4RCTahbuKoESR56ewm2bb6Bm_gmQCkE-T0OaPIl7PjtAR22UcwGiOPYWcE802G2hEuTiLdxWFG2ETl-_D3KIL6SjalAowT-xDJX0CjteJhw9GL7ka4XdMK4icN8x4Na4IX5fNOYNbpXhO3DYrmRy_clqCtatlvQLZQdEjr1aVQXkBnSpioXsCKWJrW0VbTqtM_7w30nHf_eFkngrDRc0Sq0Jw0UVZBB-egS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باراک راوید خبرنگار آکسیوس: یک فروند از بمب‌افکن‌های استراتژیک B-1B Lancer نیروی هوایی ایالات متحده، شب گذشته به ایران حمله کرد
❗️
پ.ن بیچاره مردم که دودش فقط تو چشم مردم می‌ره این جنگ ها و حملات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136527" target="_blank">📅 10:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136526">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO1RFLSdFcVTHl1c5TgodR5oi9mlVUBQbIudkGsTPfaOtts7vV2TgK-6DpoUF_RJhVcqPdAQfA2Y3OEXUd6kmwTAMzqaEfeLe2swHOSxydBz_hhpxx3_gkXTZm6p9kn1RGQx0Jc6nhrAM-AbPk55KpFCWlkIPaUOMO8A5zW58JTdgPh-6nZ-1uoD5N9E001m70KsTDxByB8LtcJ7lvvbydlWp-Ret6LYyRIyanWeS8zNOofjXXsQsh14hHjYF4gOEq7Vx6KvXBY0IUofXeuPO80fus2uWTPXd8kWi9htYhDdxdjYrmQAMztkLkpHpu87Ec8sNjMK6VZhjpd7Im-RFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرهیختگان: محمد‌مهدی محبی در لیست مازاد اتحاد الکلبا قرار گرفته و باشگاه اماراتی پولی بابت رضایت نامه محبی نمیخواد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136526" target="_blank">📅 09:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136525">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
کسری طاهری و دانیال ایری طی 48 ساعت آینده قراردادشان را با پرسپولیس امضا خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136525" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136524">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
محمدرضا اخباری دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد‌ دو ساله شو با پرسپولیس امضا کرد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136524" target="_blank">📅 08:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136523">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔹
فوووووووووری
😐
🔹
ترامپ: دستور دادم در های جهنم به روی ایران باز شود  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136523" target="_blank">📅 08:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136522">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uprTQ5VdT1PTLJB3WvaiYyLvCDqpsm0kL410q-vsW2f8DCr1omYEjTEqHVDx26o2z1OXDwVbnhSziJgAoKV9uKm53JFgLL0liwl5mfS6K1j7NWO6WpZ3Ky7USoKygVtYZp257pUORmCDHxrigaSDHU2tBSHKm1odnosQGe6h6vNw6ITXACRCEUCY-rwWd5godVMk7GyvMW15hVBVtJnYbCSMof7iw9yUFCLpjuKgYjBOvrLmThiY20g29eWiY0XCCyGBmiDLim2cqFNqW7xh486_eVPA6CtKEb9IZnqkRZ9eW9ZqbrZJ4k1WFQYJVQe1RvAjsJjd4diEV9ERaXdiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/136522" target="_blank">📅 08:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136521">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136521" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136521" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136520">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PG-69OA8CrL55S9iZxwBs83A0Dp6_zfdA6MwLXMrN5-2s505G3i-iGXQd3HQ5gW8l4Z2saDPM1us14Q8tufvH6CTvXIuo_pgYWStc-si6SrCmFMWa-nX8PmzrDz-tWAos6Dr5ytDRgoPQoAIxk_xE4SDsV_Tpmn3p3rhesb41X6UJe7gjS7tL2v_8-NOk76XcAuX8EilRoCGaoseDXqeK6LNQnknj2PUc4ZWA-OlddhpRVDtP7w5Y3afHG6RYTBRfXiBPmCK_FvMfQQkDf1_daxO8-BHIPOf9XGAfwVGEA-HAsho2SoCJfmaeh1ppsyQfnrrd8jjaNXeVs75ed86Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136520" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136519">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifdb8jP4RAUXlE1FJ8sTxmTN2ga_mw1q_4aROIi64BvpxZ1oJA-Nae8-6YhgfTsmb4mZmnNcNiuhiK7tHbtkm1XIdxqUMO0V39qoVjam9wo9on0YVEDDNvVWMIkqbYBEpr-iBSsbmdxmbfV8kGAA6vb3nbwMDqQB-DUtGy5CYhKQgABYdysK1SBxZC0gvE0sCXS4X3yu45zBmfTWWwbEF5rZY0CDtb7cXQs6VW8eAkCTJk2A6JrrhmgjXKQ98C1i7SULr_CYQbdnDdpZIo39CW_7qFkS37C6g6UN8Il614xUXN68iXV1KRmLAe1301fWDT7xrNP7Y_tAepkJguMhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
درگذشت قهرمان جوان ژیمناستیک‌ تهران
🔻
محمدصدرا رحیم‌زاده ورزشکار ۱۸ ساله و از قهرمانان ژیمناستیک استان تهران که هفته گذشته در حین تمرین دچار سانحه شده بود، دار فانی را وداع گفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136519" target="_blank">📅 01:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136518">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136518" target="_blank">📅 00:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136517">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136517" target="_blank">📅 00:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136516">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136516" target="_blank">📅 00:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136515">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
فوری/ سنت‌کام:
❌
دور جدید حملات از الان شروع شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/136515" target="_blank">📅 00:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136514">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
محمدرضا اخباری دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد‌ دو ساله شو با پرسپولیس امضا کرد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/136514" target="_blank">📅 00:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136513">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136513" target="_blank">📅 00:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136512">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
دیروز در بازی با خیبر، جلالی مصدوم شد و از بی دفاع چپی جای خودشو به دنیل گرا داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136512" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136511">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
یک مقام رسمی باشگاه پرسپولیس خبر امضای قرارداد دو ساله با اخباری که وایرال هم شده را تایید نکرد.
🔴
وی در گفت و گو با قرمزانلاین درباره اینکه گفته می شود مذاکرات امیدوار کننده بوده و توافق اولیه حاصل شده گفت؛قراردادی امضا نشده است.بیشتر نمی توانم فعلا توضیح…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136511" target="_blank">📅 23:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136510">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
فوری از سپهر خرمی:
🚨
بعد از کنسل شدن تمام گزینه های پرسپولیس در پست هافبک دفاعی، مسئولان این تیم دوباره سراغ محمد قربانی رفته‌اند اما اینبار با پیشنهاد بهتر!
🚨
قربانی از تراکتور هم پیشنهاد خوبی دریافت کرده اما تمایل داره به پرسپولیس بیاد!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136510" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136509">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
✅
پرسپولیس با محمدرضا اخباری به توافق رسیده و اگه اتفاق خاصی نیفته، امروز رسماً ازش به‌عنوان دروازه‌بان جدید تیم رونمایی می‌کنه.///فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136509" target="_blank">📅 23:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136508">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
🔴
باشگاه پرسپولیس در آستانه توافق نهایی برای جذب دانیال ایری و کسری طاهری است.
✍️
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136508" target="_blank">📅 23:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136507">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/136507" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136506">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
تیکدری امروز بازم مثل بازی قبلی یک گل و یک پاس‌گل به نام خودش ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/136506" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136505">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_vsdY4XXk-EB4tl07M6dNf5o73w-F5Mg2_GMkVUpUJHoPSaIQPmCeDWcU6X0ACnk38tcNXUv3TxI9hfus7U-4L6nx-g-x31NcCFUkQn1UBNMYIwRsHc6L41KQfM3t9losM-GlKBHDE1_V8296sHrw6ZKscEQUjtuJVQhKjA1HfoZb9r6NeYb-tvifGqpu8LQhWGqJCk6pXr7hSdLr8jB-LeKUJR7RqQcvfA792ws4Oc4vpWKDR2vYbzBr0Q8CKF8s4RADkB_2E06-Fq_STnb7sTCIjgHjk3fdjtDS71kn2I79m8nzYRHSJt-fSQzXq_rTDkBVDXEOG7rpuCJWyYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
فوری/ کان نیوز: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/136505" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136504">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
امیرحسین محمودی در فصل آینده با شماره 10 برای پرسپولیس به میدون خواهد رفت. شماره ای که سالها بر تن بزرگی همچون علی آقا دایی بوده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136504" target="_blank">📅 20:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136503">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
پورعلی گنجی هنوز با پرسپولیس برای جدایی به توافق نرسیده است
🔹
گفته میشه این بازیکن زیر بار کم کردن قراردادش نمیره و کل پولش می خواد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136503" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136502">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136502" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136501">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
تکمیلی :فرهیختگان: استعلام از فیفا اومده و مشکلی برای انتقال نیست و احتمالاً هردو قرضی رایگان تا نیم فصل + بند خرید با تیم راهی ترکیه میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136501" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136500">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBGpYHVsTd-STCZVZgB8LndJdpomM4dUkmCSPum2MGlmUw9_F2DGHv7rhEe70NTQsWZfRLsgS2HYX6UJG2wyOR_7GIY4HdBBLTtdixPYpCrXCDvuKOyiQxoG30eFaBvFApMicn5QNWoGfp-fuWQbRfohl3uNZ2ilin45QwuauCxJ8Ify3xkWCQO3_e7h8QExxLqMdXpK9pUHxp18Q1Lv8ds7XSJ-PMiUhpXkFR6yprP4huyC8upThc2HTXLoas93XLo8qjVregzsp-wFaTboIqoKSkUQ9ZjgYqRfhB1oKN1LBPJwOY1HaQPD2VaMmfyjAn9Y4FQpxGHeuFha6VzyRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی طاهرخانی:
❌
میلاد زکی‌پور با ارسال پیغام‌هایی به بعضی از افراد خواهان پیوستن به پرسپولیس شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136500" target="_blank">📅 20:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136499">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136499" target="_blank">📅 20:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136498">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP-lc4yOVvfBZOn5f6qgaFptxdJwkA-SqemyX_1f8VF6rVQtdMUxchls2CGIg8KgNDIgK2XRbcsFgwRokVLN91-xOxQOrcK3VNnUpgvxhRCIuyibQoCrb4AYkGf_0jB7KEmOC8CeE9E70ZYgTHLPJuGP6Gw7cVDrmMkYbvOyTjA3454rl7yG48aOLkPYm6H2wgFKi-jetXJGy228As1MXcWRnAtjzOJ1MIfNww_PclIp7SRF8BmDWEfzAlXoiAm9jr3IST7vlU2-BBMt9bgW--8HaPERs2iDlkEvrsDc-YMsZlNglNhKenUw7GLaduKZczvHJ4r-O6pQ75oivOnaiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
Ⓜ️
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@ARON_TIP @ARON_TIP
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136498" target="_blank">📅 20:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136497">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❗️
❗️
به این ترتیب با وجود رد شکایت باشگاه پرسپولیس، همچنان موضوع اصلی پرونده محرومیت 4 ماهه بیرانوند به قوت خود باقی است و این دروازه‌بان در شکایت به دادگاه CAS خواستار لغو محرومیت و جریمه مالی خود شده است.
🔴
🔴
شنیده می‌شود هنوز علیرضا بیرانوند در موضوع شکایت…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136497" target="_blank">📅 19:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136496">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
🚨
خبرگزاری تسنیم: عادل فردوسی‌پور نباید از علیرضا فغانی که از رضا پهلوی حمایت کرده، تو برنامه خودش دعوت می‌کرد و همین باعث قطع برنامه‌اش شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136496" target="_blank">📅 19:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136495">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136495" target="_blank">📅 19:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136494">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
پرسپولیس فعلا با احتیاط داره از اورونوف مراقبت می‌کنه و تو بازی دوستانه بهش بازی نمیده، چون دیرتر از بقیه بازیکنان به تمرینات اضافه شده
❌
❌
کادر فنی می‌خواد با برنامه ریکاوری و بدنسازی مخصوص، کم‌کم آماده‌اش کنه تا دوباره مصدومیت های پی در پی نداشته باشه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136494" target="_blank">📅 18:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136493">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27b7114b3.mp4?token=jDW9zApstwTxVjHpeJntLZqhwdXbdQA2wR8Ff5qeEeHSZRcNGWMMjjvSJE3JP7D75lrKL47H3idLxi54KLZw-fyYvPShA3U1Q7E7nuQSiEDnVtrW3At3lq3lD6rtwHy6XbbmrBqvKXmOksr32xjD9btaXBOYQ7DkU4lhbIMHPatQljwVMviI0Yx0KoHw5bqr6pA7HDeK5lKXMAFn5bfYFVgTg1NZlbYitwt6Su_pyIsOx9NJ-gTVsi7gn7ufck-FxHQ9Cn2SOHS2E8YoBcP7pkAdblVgTbnsc0z3it76zqo0tJBH1-zqadIaT8Z9HB3o13R708Mv6hh0lv7GrDAv5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27b7114b3.mp4?token=jDW9zApstwTxVjHpeJntLZqhwdXbdQA2wR8Ff5qeEeHSZRcNGWMMjjvSJE3JP7D75lrKL47H3idLxi54KLZw-fyYvPShA3U1Q7E7nuQSiEDnVtrW3At3lq3lD6rtwHy6XbbmrBqvKXmOksr32xjD9btaXBOYQ7DkU4lhbIMHPatQljwVMviI0Yx0KoHw5bqr6pA7HDeK5lKXMAFn5bfYFVgTg1NZlbYitwt6Su_pyIsOx9NJ-gTVsi7gn7ufck-FxHQ9Cn2SOHS2E8YoBcP7pkAdblVgTbnsc0z3it76zqo0tJBH1-zqadIaT8Z9HB3o13R708Mv6hh0lv7GrDAv5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136493" target="_blank">📅 18:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136492">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
#فووووووووووری
🔴
پرسپولیس در آستانه جذب دانیال ایری و کسری طاهری
🚨
پرسپولیس از فیفا استعلام گرفت و فیفا اعلام کرد مشکلی برای عقد قرارداد وجود ندارد
📰
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136492" target="_blank">📅 18:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136491">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
باشگاه پرسپولیس برای جذب کسری طاهری از فیفا استعلام گرفته و منتظر جواب فیفا ست تا برای جذبش اقدام کنه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136491" target="_blank">📅 18:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136490">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
🔴
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136490" target="_blank">📅 18:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136489">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
ویدیو باشگاه پرسپولیس برای خداحافظی و تشکر از کمال کامیابی نیا
❤️
🎗
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐️
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136489" target="_blank">📅 18:26 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
