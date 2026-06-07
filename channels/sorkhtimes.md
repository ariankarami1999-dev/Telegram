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
<img src="https://cdn4.telesco.pe/file/EVyY9FpJgJGsTG7rkTULSTTbqt79er8EkN5CjuE5UM6P6yx1bDd8cXF-akdGsdf5uqL61tlTdfv29NlQ_Z-rg5ci1591GMKCaUc3EMkEAVtNMeMn4X9XbOHFE0AIS2Jv6uafwj9QTQ6x3DIOqfGVwXq23MJyVid9OgZSpa85-oh85U7dbHupPtFoh3o-dlqL-S9wwSZFGqmPfqgYHwPl2kdvhZ5wKa_uECSTAS4ssmR4AgnTv_Fh8u-8bzY1yWwhgs9qmXRjw8rOPQjfiw_x2tZKmCXRIs6hllGKdMEbKQykJrfxKVKmzFooVU428o6Xo3z2VsQOOdNc1n-X4VfcWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 18:19:09</div>
<hr>

<div class="tg-post" id="msg-132946">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHfEOSqskYHMKyCcfYctLMJWasJUehanVQHOMyZ4G3xhB7dvNnPzFzW0c8DMxuY2MbMcX7y_2WZcABnOwtMkTJp3CmJMGvSUfdPV905_wLUbjl8GW2ypnXA_mRnUhzjXMb2kiOH4GbAIr-QtPtqQ6q2q56iP8i-K2xD_JlblVMac6qyw6ny9EDNMSNxlI6Q2dJ_Ix56NAv2dtlW6JX5q08OZiPQTCSPtjtzcGXFQ6qBgcDeeGM0Wylcf0zj2snIq20fu2CUAcVr8yV6uGRN6T4lBmBHJCZSQpIPBmi6XFRp6orwU9KGF098V7ns-nnYTkhYJngboA-c5JA4eBvwu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مارکو باکیچ در حال گذروندن کلاس مربیگری در سوئیس هستش تا مدرک A اروپا رو کسب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 488 · <a href="https://t.me/SorkhTimes/132946" target="_blank">📅 18:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132945">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
👈
دونالد ترامپ به NBC گفت: اگر با ایران به توافق برسیم و روابط دوستانه‌ای داشته باشیم، با همکاری یکدیگر اورانیوم با غنای بالا را جمع‌آوری و نابود خواهیم کرد. تجهیزات متعلق به ما خواهد بود و این مواد را یا در همان محل از بین می‌بریم یا به جای دیگری منتقل کرده…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132945" target="_blank">📅 17:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132944">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
فووووووری و پشم ریزون
😐
🔺
به نقل از فرشید حقیری: با تصمیم بانک شهر خداداد عزیزی به عنوان سرپرست پرسپولیس انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132944" target="_blank">📅 17:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132943">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
🔴
ترامپ به NBC
🚨
:
🔴
مجتبی خامنه‌ ای بسیار زخمی شده پس شجاعت خاصی در این است. بسیاری از مردم ، اگر آنقدر زخمی شده بودند ، درباره این که وضعیت ما با ایالات متحده چگونه است؟ صحبت نمیکردند. ذهنشان به چیز های دیگری مشغول بود. پس شجاعت خاصی در این است. اما او…</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132943" target="_blank">📅 17:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132942">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
اوسمار تا پایان هفته برمیگرده به ایران و تا اون موقع کریم باقری تمرینات پرسپولیس رو برعهده میگیره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/132942" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132941">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
👈
ترامپ درباره‌ مجتبی خامنه‌ای : اون منطقی‌تر از پدرشهِ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/132941" target="_blank">📅 17:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132940">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
فووووووری و پشم ریزون
😐
🔺
به نقل از فرشید حقیری: با تصمیم بانک شهر خداداد عزیزی به عنوان سرپرست پرسپولیس انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/132940" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132939">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
فووووووری و پشم ریزون
😐
🔺
به نقل از فرشید حقیری: با تصمیم بانک شهر خداداد عزیزی به عنوان سرپرست پرسپولیس انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/132939" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132938">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
باشگاه پرسپولیس معتقده مجوز حرفه‌ای چادرملو مورد داره و تایید شده .نیست و با چادرملو بازی نمیکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/SorkhTimes/132938" target="_blank">📅 17:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132937">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
ترامپ به خبرگزاری ان بی سی: ما می‌دانیم رهبر ایران کجاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/132937" target="_blank">📅 16:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132936">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/132936" target="_blank">📅 16:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132935">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">💢
ترامپ: اوضاع با ایران خوب پیش می‌رود
💢
رئیس‌جمهور آمریکابه خبرنگاری که از او درباره آخرین وضعیت مذاکرات با ایران سئوالی پرسیده بود، گفت: به نظرم وضعیت با ایران نسبتا خوب پیش می‌رود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/132935" target="_blank">📅 16:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132934">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
❗️
شایعات؛ خبیری به عنوان سرپرست پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SorkhTimes/132934" target="_blank">📅 15:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132933">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
با اعلام مهدی تاج ویزای ساعتی ایران بدین شکل است که یک روز قبل بازی وارد آمریکا میشوند و بعد از مسابقه خاک این کشور رو ترک میکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/132933" target="_blank">📅 15:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132932">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
✅
حسین خبیری مدیرعامل خیبر شد و خبری  از اومدن به پرسپولیس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/132932" target="_blank">📅 15:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132931">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
همه تیم در جام جهانی هستند تو این دو تاریخ  ..و باید بگردیم یازده نفر و پیدا کنیم و بتوانیم این دو باری سخت و بگذرونیم و جواز رفتن به سطح دو آسیا رو کسب کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/132931" target="_blank">📅 15:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132930">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">💢
شاهکار پلنگ مازندران مقابل شمیل ممدوف را ببینید؛
رحمان تا ۴۰ ثانیه مانده به پایان مبارزه، با نتیجه ۱۰ بر ۳ از حریف خودش عقب بود ولی در نهایت ۱۷-۱۰ پیزوز شد!
✔️
🥇
رحمان با بی‌رحمی طلایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/132930" target="_blank">📅 15:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132929">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/132929" target="_blank">📅 15:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132928">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❤️
تمامی بازیکنان باید تا فردا خود را به محل تمرینات برسانند و در صورت غیبت غیر موجه بازیکنان با جریمه انضباطی مواجه خواهند شد.
👍
دنیل گرا و باکیچ دو بازیکن خارجی پرسپولیس هم فردا و سه شنبه وارد تهران خواهند شد و برای این نفرات نیز بلیت تهیه شده است
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SorkhTimes/132928" target="_blank">📅 15:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132927">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgUr08yPg1Uc11ZENVD1tTXgABUWBMXlD5kLQKSw21tGkqMZjCanY_jJ9ItL8J8ybKcja7nP0s3NexjrhMhsxuVVD-_YRAXVBs4euF3caT6z1z-bgXh6NZNkuiriGRmTY7SA9vTxHofKviZ2mC8KWgoYLvhNN3g4zY0MXFt3Stzp7AkTYbFYsegZosDzDh6c2yPc2mLoLBx_r0M_db9aAUyZTZM75DsCFJ6yiLgAwcpy0Ldqr_VcuHWk3Dw-KNIqXXZ3OSraWJXyO0N8vIi9RbYKRLsN_CX-3cozy4hRMwxDUTFep9MOJwI55Im7hDfB2txaUF5CbptKcDB9mfalfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوسمار تا پایان هفته برمیگرده به ایران و تا اون موقع کریم باقری تمرینات پرسپولیس رو برعهده میگیره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SorkhTimes/132927" target="_blank">📅 15:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132926">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
یحیی گل‌محمدی به تیم دهوک کردستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SorkhTimes/132926" target="_blank">📅 15:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132925">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎙
🔴
بادامکی: دوست دارم به پرسپولیس برگردم و کمک کنم؛ تیم ملی توانایی صعود به مرحله بعدی جام جهانی را دارد
‼️
پیشکسوت و مدیر سابق پرسپولیس:
🔺
با پایان بازی‌ها، قراردادم با باشگاه خیبر خرم‌آباد به اتمام رسیده و در حال حاضر مربی آزاد هستم.
🔺
تمایل زیادی برای بازگشت…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/132925" target="_blank">📅 15:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132924">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎙
🔴
بادامکی: دوست دارم به پرسپولیس برگردم و کمک کنم؛ تیم ملی توانایی صعود به مرحله بعدی جام جهانی را دارد
‼️
پیشکسوت و مدیر سابق پرسپولیس:
🔺
با پایان بازی‌ها، قراردادم با باشگاه خیبر خرم‌آباد به اتمام رسیده و در حال حاضر مربی آزاد هستم.
🔺
تمایل زیادی برای بازگشت به پرسپولیس و کمک به این باشگاه وجود دارد و هر زمان که مدیران صلاح بدانند، این اتفاق با کمال میل خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SorkhTimes/132924" target="_blank">📅 15:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132923">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎙
🔴
پیمان حدادی مدیرعامل پرسپولیس :
🔺
با سروش رفیعی در تماس هستیم به معاون باشگاه اعلام کرده هر زمان که تمرینات شروع بشه به ایران خواهد آمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SorkhTimes/132923" target="_blank">📅 15:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132922">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMRyfiF-n1xyi4K6q8O_8oCB5lV0pjrDf_yWcEH0BXzXdM1s-lRgMvLVPQFSMEcwxCJjm2uV3UUewPIC18ctNCU5JvFj8jbP2SVzFPj5OSwE0GpWO4tV2gvy6TDMBoYm_IwGRvoOEvEs27AgcWjISurnNNon1fHVCnt7FzPyhKKpia_AXDcKUwAn1LNFhwWZFviLhDGwnT-uu2nOcrZB_h3aGI9c_imT3jVc6yhRLwMJlkDDQ8e4Rsj50ycYdWXswDyCkV-lJQVFVsq69gXbWPJA7cq1fCQt3RYcmXOToXDwjuqFvEYPo8eBPDf1Tv0XlXX7Ihdghp5Tzvp8pg4KiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
دیدار جذاب و حساس فینال رولان‌گاروس بین
فلاویو کوبولی
و
الکساندر
زورف
از راه رسید، این دیدار
هیجان‌انگیز رو با آپشن‌های مختلف در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/132922" target="_blank">📅 14:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132921">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❗️
باکیچ و بیفوما هم برمیگردند  باشگاه براشون بلیط تهیه کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SorkhTimes/132921" target="_blank">📅 14:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132920">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
زمان بازگشت اوسمار به ایران مشخص شد   باشگاه پرسپولیس در تلاش است تا شرایط را برای بازگشت اوسمار ویرا ظرف یک هفته اخیر را فراهم کند و اگر چنانچه مشکلی رخ ندهد او در این هفته به ایران باز خواهد گشت.
✍
خبرگزاری تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/132920" target="_blank">📅 13:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132919">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/132919" target="_blank">📅 13:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132918">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GknrXBcABMQ0_wGvdNBrFQPqttJR0YKrNcuKxVf_WpPhh8KfW-UhsJV-oThRfHbuapbzArdiTHeHUVZjzmm-lo7lO43KGnOr2DP8ICxr4sUvXVefON5kUJU5MMhWgeZ6PCNgYbv0VgvtxBJJscYFOshpk_jriDc1qTVh1jcZNNJayEaPzpzT897fBE0GcMoe22S6tYFqkraCwJzZUkEv-0LMTLZt0zi2DSb8CluQ0BRdxt5MQhd6nVdatNPnn5zUxKL6NGNsbFzELnE_kukoGdfVdjbykk63BJQOdNqMeQDgAX9a3DeQBUEqtQe1vpMjqpK1S4-RQ7iHJno4Z-L3RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
نامه ویژه پاکستان به آیت‌الله خامنه‌ای‌تحویل عراقچی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/132918" target="_blank">📅 13:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132917">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
رویترز:
✅
کسایی که ویزا نگرفتن برخی از مربیان و هیئت همراه هستن وگرنه تمام بازیکنا ویزا گرفتن.
🔴
آمریکا اعلام کرده اجازه نمیده افراد غیرورزشی به بهانه ورزش به آمریکا بیان.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/132917" target="_blank">📅 13:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132916">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">#تلنگر
🚨
‼️
اینکه سه ماهه هئیت مدیره جلسه ای تشکیل نداده و‌ از زیر بارش در میره به کنار به گوشم رسیده دوتا از این بزرگواران بیشتر از اینکه کارهایی که مسئولیت شو بر عهده دارن انجام بدن به دنبال لابی کردن،زیر آب زدن و به نوعی خارک…. بازی هستن تا زیر پای حدادی…</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/132916" target="_blank">📅 12:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132915">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#تلنگر
🚨
‼️
اینکه سه ماهه هئیت مدیره جلسه ای تشکیل نداده و‌ از زیر بارش در میره به کنار به گوشم رسیده دوتا از این بزرگواران بیشتر از اینکه کارهایی که مسئولیت شو بر عهده دارن انجام بدن به دنبال لابی کردن،زیر آب زدن و به نوعی خارک…. بازی هستن تا زیر پای حدادی رو بکشن به نوعی چشم دیدن این بابا رو ندارن که پله های ترقی رو طی کرده و به گواه اکثریت بشدت پیگیر و مسئولیت پذیره و دلسوزه و از جنس هواداره و خودش یه روزی رو سکو های آزادی این تیمو تشویق میکرده و الان در قامت مدیرعاملی بزرگترین باشگاه ایران قرار گرفته
❌
♨️
این کوتوله ها بنظرم بهتره ماست هاشونو کیسه کنن و بدونن به قول گفتنی مسجد جا گوزیدن نیست، یهو نسخه همه تون رو هوادار میپیچه و به سرنوشت بقیه هم کیش هاتون دچار میشید از ما گفتن بود.
💯
یهو یه چیزایی میاد بیرون که پس فردا دهیاری شاغالو رو هم دستتون ندن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/132915" target="_blank">📅 12:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132914">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
تمرینات تیم از فردا استارت میخوره تا برای پلی آفی که اصلا معلوم نیست برگزار شه یا نه اماده شیم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‌</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/132914" target="_blank">📅 11:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132912">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
چه پولای خرج کرده اقای پ.ج
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/132912" target="_blank">📅 11:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132911">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
زنوزی، مالک باشگاه تراکتور به صورت شخصی با مرتضی پورعلی گنجی، مدافع پرسپولیس وارد مذاکره شده تا این بازیکن راهی تبریز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/132911" target="_blank">📅 11:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132910">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
قدوسی: اوسمار احتمالاً چهارشنبه یا اواخر هفته به تهران برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132910" target="_blank">📅 09:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132909">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
رونالدو بعد از 3 سال و از دست دادن 14 جاممممم بالاخره با قهرمانی تو لیگ عربستان اولین جام خودش رو با النصر به دست آورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/132909" target="_blank">📅 09:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132908">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
رویترز:
✅
کسایی که ویزا نگرفتن برخی از مربیان و هیئت همراه هستن وگرنه تمام بازیکنا ویزا گرفتن.
🔴
آمریکا اعلام کرده اجازه نمیده افراد غیرورزشی به بهانه ورزش به آمریکا بیان.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/132908" target="_blank">📅 09:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132907">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwaSi3S5UChOsITOCvFH2gKUUkRVC__-X92gOPA65chEi8y-qpxvGeqv0DLVpiS-dDgJa54wNuUgfN-AFrhVCPiCO7MPHczRIkbX8Z-fbMG3weRCYF3etQ0_iy9jJsYwKlU94WoAwM86WrhSCldJVETHS1BdZWh6gLOU18LHhn2PANK74Y1mSh3HcJPXTildhRT3WhVzLOKela9O-rqcznOcJkdYKdHXOouA-Y9b3oJIYGN8IOhbAq9oPGw2APBPgaE79iqLdXxkNUmDWobYvKoiE3TXLMlKozOI7-XPrslsqi8E1axtUJkGRnXwaLsD3opYwC4SYiGM_-oibGSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
عارف حاجی عیدی به دلیل قرارداد بالای که برای فصل آینده داره در لیست خروج سپاهان قرار گرفته
/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/132907" target="_blank">📅 09:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132906">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
آقای پیاتزا ازت ممنونیم چه تیمی درست کردی ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/132906" target="_blank">📅 09:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132905">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
خیلی از هوادارا پیام دادن که ما کارت ملی مون نیومده نمیتونیم ثبت نام کنیم چون شماره سریال کارت ملی میخاد….و کارت ملی خیلی ها از جمله نسل z هنوز به دستشون نرسیده و با کد رهگیری کارهاشونو انجام میدن
🔺
بخاطر این موضوع با باشگاه صحبت کردیم که پیگیری کنن حل بشه…</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/132905" target="_blank">📅 09:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132904">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dd44R0LUMihFCzH9FCR7KsqgrBbO1uJAiMZ1JyL75_nllZLATqY6JiY0EjZZVvXbY_807dzQa5TJpC1x7eNoIUkZBBlOiK8Nf_U56gIhv7a76Ki80KTqzdXtN5qFaa5hRB-smPtBbOYaZ4mcTkdHSifPdDDsy7bSGTqVl0_zkBkJuQW_67tIqtc5xjjh_fP8WQEEuQMkQnvXWt1X0QNAw2BogZ3frY9-juETWBp7B-Sru_V__tBwzC2EYhdvamuQ44FaTF41gX1yWr5BiZH9qp3OEMUXsrHyRLClaKX7tG2aqnQanHobwAD6Sja1Ens9MPLN4t0ok_oNrMpWtELS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/132904" target="_blank">📅 01:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132903">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OesdnI4fb9XqVMiGCscSWMCNZ7AGBRzfIkx_S5kumsoayCh5zQdT5AhvWq3W7hptLJFO8c0vA1Lbb3u5pr_M-fCSTqiaWTySSZre1DSsk46x62ORmQ4c0t1Q2F4KEbC6CTpIAzfKg0BioyLBso1NEWq72puq5vVKZMC7PM5hIO4-y4ovuegisCrUGP0-C25xugtYLn571TJd0uNCFJMsIOfFcN0W-FtxSKcINjbUUdbzTwtfNGH0t1Vx9GCqlDVh2On3srXEc2pBzfx32z6CzE5BE9qeEYorPT5ZmT8GpiXkMqK3XjD-4IgPH-BP_txmiGjP_Fsw3RK7lJ5HqGViGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
PulseGate | اتصال بدون مرز
🔥
اینترنت مخصوص نت ملی
⚡
سرعت بالا
🎮
پینگ پایین
🛡
امنیت بالا
📱
سازگار با همه دستگاه‌ها
♾
کاربر نامحدود
💰
پلن‌های اقتصادی از 250 هزار تومان
📩
ثبت سفارش و پشتیبانی:
@PulseGatee
⏳
ظرفیت برخی سرورها محدود است؛ برای فعال‌سازی سریع‌تر پیام بده</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/132903" target="_blank">📅 01:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132902">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏆
موزیک ویدیو رسمی جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/132902" target="_blank">📅 00:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132901">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mITg_veiwYQJ-pSpMj1kNNW6_YdhooX-cpoEaQCeGSYMbH56YcAYE5iJg8htAp9qB1cU-HakWGHPds_gIo4nps_C8I4iHTzk3T71W-K0baGLfyWCng-ca_WFPoD0vQp6pOdOhFOM-mEtd2vEXWV-uWVwk4z_oVf5XxgJXlBbgJtkt8tGhXKS66ZzOXMIgiSZh2VOaU2eKry1hdXl64I3LTQTEOVreWL8RrzLjU8Qm_jBMyb51Bx1PWnjhZQrJoS1JmuI5YjvM165Bfk8tV3WP_SgQoPUlMHeUDeJm8rCR8hQcDDG_bTG7TFW6gHjQ9xWuV6TMPZmae11FI4bGQRm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اسفندیارپور، مدیرعامل گل‌گهر: «تورنمنت ۳ جانبه من‌درآوردی است و در آن شرکت نمی‌کنیم.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132901" target="_blank">📅 00:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132900">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
🔴
برگشتن سروش رفیعی به پرسپولیس خیلی محتمل نیست. او با چند تیم کانادایی مذاکره کرده، ولی هنوز به توافق نرسیده. اگر مشکل‌هایش حل شود، فصل بعد در ایران بازی می‌کند و دوست دارد فوتبالش را در پرسپولیس به پایان برساند.
✍
خبرگزاری فوتبالی
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132900" target="_blank">📅 00:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132898">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S_me0XKKebEAMfcQaWvcTsa6xwmXDwvWSgVWWENBqv62EEUAPS0_bEzJ2cxbGewmJHEfepLvQFtpzCdAkBO9z8JvSJfmn1qH0ux4Z5wRx2aJmpJU9lQUDsPEISPTf7SYsAZnGU0e4_7FaYsA8AB7eS9LnZwYxHZhewyP8dCzHFtEILZI7i3zqT0cMBAmgIprrtGtK7iZinFTPMC94AM14IvWgosstBFCcXi3FOQKJTsdA3rgaEKL_uB_6Zw0N13fonaJrkpKd8FlpeF8eWQ0CPQQbqholUFyIALGmVLuViV3oS8B2nPHeEvDx0PBZxfEg0fF68v5igpMR5ymnIDNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فدراسیون فوتبال عراق به دلیل همزمانی بازی‌اش با سنگال در جام جهانی با شب شهادت امام حسین(ع)، از فیفا درخواست کرد مجوز پوشیدن پیراهن مشکی را برای این مسابقه صادر کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/132898" target="_blank">📅 00:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132897">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
قدوسی: اوسمار احتمالاً چهارشنبه یا اواخر هفته به تهران برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132897" target="_blank">📅 00:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132896">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
🔴
امید عالیشاه، علی علیپور و میلاد محمدی شانس بسیار خوبی برای تمدید قرارداد با پرسپولیس دارند
✍
خبرگزاری فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/132896" target="_blank">📅 23:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132895">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
🔴
امید عالیشاه، علی علیپور و میلاد محمدی شانس بسیار خوبی برای تمدید قرارداد با پرسپولیس دارند
✍
خبرگزاری فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132895" target="_blank">📅 23:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132894">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
🚨
#شنیده‌ها
💵
پیشنهاد مالی جدید علیپور به پرسپولیس برای تمدید قرارداد: ۲۵۰ میلیارد برای ۲ فصل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132894" target="_blank">📅 23:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
همه تیم در جام جهانی هستند تو این دو تاریخ  ..و باید بگردیم یازده نفر و پیدا کنیم و بتوانیم این دو باری سخت و بگذرونیم و جواز رفتن به سطح دو آسیا رو کسب کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132892" target="_blank">📅 22:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
🖍
غایبان احتمالی پرسپولیس در صورت برگزاری تورنمنت سه جانبه برای کسب سهمیه سطح دو آسیا
▪️
ارونوف
▪️
سرگیف
▪️
علیپور
▪️
کنعانی
▪️
محمودی
▪️
سروش رفیعی
▪️
میلاد محمدی
▪️
پیام نیازمند
▪️
دنیل گرا
▪️
تیوی بیفوما
▪️
مارکو باکیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/132891" target="_blank">📅 22:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132889">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
مسئولان پرسپولیس به اوسمار ویرا، مربیان خارجی و بازیکنان خارجی تیم پیام داده‌اند که هرچه زودتر بگویند چه زمانی به ایران برمی‌گردند و برنامه برگشت‌شان را مشخص کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132889" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132888">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
در صورت برگزاری مسابقه، این دو دیدار در تاریخ 5 و 9 تیر برگزار خواهد شد.و بدون تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132888" target="_blank">📅 22:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132887">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
‼️
مجتبی فخریان، وینگر پرسپولیس که به صورت قرضی در ملوان بازی می‌کند، قصدی برای بازگشت به پرسپولیس ندارد و به صورت دائمی جدا می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132887" target="_blank">📅 21:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132885">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
مسئولان پرسپولیس به اوسمار ویرا، مربیان خارجی و بازیکنان خارجی تیم پیام داده‌اند که هرچه زودتر بگویند چه زمانی به ایران برمی‌گردند و برنامه برگشت‌شان را مشخص کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/132885" target="_blank">📅 20:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132883">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
از عصر دوشنبه تمرینات پرسپولیس شروع میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/132883" target="_blank">📅 20:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132882">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
در صورت برگزاری مسابقه، این دو دیدار در تاریخ 5 و 9 تیر برگزار خواهد شد.و بدون تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132882" target="_blank">📅 20:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132881">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
کسری طاهری تا سال 2028 با روبین کازان قرارداد داره و الان قرضی توی پیکان بازی میکنه، هر تیمی بخوادش باید با کازان مذاکره کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132881" target="_blank">📅 19:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132880">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">#منهای‌پرسپولیس
🚨
کسری طاهری مهاجم تیم پیکان تهران با پایان قرارداد قرضی اش با پیکان به روبین کازان روسیه پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132880" target="_blank">📅 19:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132879">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">#منهای‌پرسپولیس
🚨
کسری طاهری مهاجم تیم پیکان تهران با پایان قرارداد قرضی اش با پیکان به روبین کازان روسیه پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132879" target="_blank">📅 19:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132878">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcce26bb71.mp4?token=ntTYTl3LSqgsLxNuLP7PTc_Vp2cYk7dQcsxmRbb6lV54vSvuQE5gyPm6Yuk7pxU4HIEEBGPpC8EakRjIB2VVlSip1-j-O0nV6Y3a6KAlgAk7vn5Tsqb8ACWM7SFpABP1STuwoXb7NVhDNxOnwIqVx8ojESEbSx4zBCex4OTrDLlN_2jeOz64yKGYM7f-lStZ--IQokszcNWRc7qBFu3J-sa4AyZePT_kzLC_rC1LodBOtmbgpso8lGNywV-rT2-NugZ9p1ckgxTfTMp-F97Yxyovp0tL_Qmo8JbvaoaE0_5M1HFz04zaCMA-xHKmOmOOiBb_wJyYKDAxFHVHnP2G_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcce26bb71.mp4?token=ntTYTl3LSqgsLxNuLP7PTc_Vp2cYk7dQcsxmRbb6lV54vSvuQE5gyPm6Yuk7pxU4HIEEBGPpC8EakRjIB2VVlSip1-j-O0nV6Y3a6KAlgAk7vn5Tsqb8ACWM7SFpABP1STuwoXb7NVhDNxOnwIqVx8ojESEbSx4zBCex4OTrDLlN_2jeOz64yKGYM7f-lStZ--IQokszcNWRc7qBFu3J-sa4AyZePT_kzLC_rC1LodBOtmbgpso8lGNywV-rT2-NugZ9p1ckgxTfTMp-F97Yxyovp0tL_Qmo8JbvaoaE0_5M1HFz04zaCMA-xHKmOmOOiBb_wJyYKDAxFHVHnP2G_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
حضور علیرضا عنایت‌زاده هافبک جوان سرخپوشان مقابل فدراسیون فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/132878" target="_blank">📅 18:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132877">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTGC6mC-6scblIIIqK6UOxxWJGt4wZDHWVoCNEpZF0FK6wPPeocNKytWeEK1flxW-LtQdJy7lWRHvQ8uE5lS1UhC0z9zxsqwh8mpIDT4e8p9U7Cf6vHpJBKXtvCHJoCKDPYYlThMr76B79MnZlWY5rcaEmBNQCTGc8QYZHdfag7SSbAWydvd0MhrM-qV1o0nWV26-m7WH9IozoZR9dxvFc69he7HzZ-7oTnWMWe3jQMv2UDJzyAFibIF1VbDpnOBgZp2COaHNkU49YaQg2aYvtkb4tHElNdacVkA-U_5fUKCQJxULTtWv5O52gH3y6hqz0ki1x7WUbI4sjs1lbaeXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس خوش‌آمدگویی برای کاربران جدید
🟢
کاربران جدید وینکوبت پس از ثبت‌نام و اولین واریز خود می‌توانند از بونوس خوش‌آمدگویی استفاده کنند.
📌
میزان بونوس تا ۱۰٪ مبلغ واریزی و تا سقف ۵ میلیون تومان می‌باشد.
📌
شرایط استفاده از بونوس:
حداقل ۱ گردش با ضریب ۱.۸
🔗
همچنین حداکثر مبلغ قابل برداشت از طریق این بونوس، ۱۰ میلیون تومان می‌باشد.
🔗
همین حالا وارد ربات وینکوبت بشید و پس از ثبت‌نام و اولین واریز خود، بونوس خود را دریافت کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132877" target="_blank">📅 18:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132875">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/132875" target="_blank">📅 17:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132874">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
جنپو با گاوداری قراردادش رو فسخ میده و طویله گاوداری باید چیزی حدود 4 میلیون دلار به این سوپراستار غرامت بده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/132874" target="_blank">📅 16:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132873">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132873" target="_blank">📅 16:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132872">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132872" target="_blank">📅 16:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132871">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
پایان دعوای سهمیه سوم؟
🔸
امروز جلسه‌ای برای تعیین‌تکلیف نماینده سوم ایران در فصل جدید مسابقات آسیایی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132871" target="_blank">📅 16:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132869">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
باشگاه پرسپولیس پیگیر پرونده سینا خادم پور و دریافت 2 امتیاز به علت غیر مجاز بازی کردن این بازیکن می باشد
❌
یا در غیر این صورت کسر شدن امتیاز این بازیکن که به استقلال و تراکتور داده شده
3⃣
احتمال تورنومنت 3 جانبه وجود دارد و طی جلساتی سهمیه سوم آسیایی…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132869" target="_blank">📅 16:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQCBIUSuFfBUqRML3YD7sQ0iX9kDqR-5wdTeTQoezJgJIkprromODCFLCZca8a4hdsCg2Fj89A0Q_U7D0nZD3tx8luSR1Lc7TFiZikyseCidWi5gG3sgqI8jrDWnoYmE_x9x3IdJJV_vOnIZkPGDupwzaOD1vEkbO6196bMf_VZJw1lPNKHYpwqa9hLSlQ8nyuVC6kBCa2DWz_ChJQN23feBge-DYJnleL23JQl1M5eCNLoi93bAN6RNFq9jvIKPQSLKU3fb6SrnInS1WDHGkhcU2P9i036ug69d1PGxAjLnNFn4iNnFaIXueMXcPyiNlZFgxjA5JqGtKZ4krZVhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
۸ جفت برادر تو جام جهانی ۲۰۲۶ حضور دارن:
- گیلا دوئه (ساحل عاج) و دزیره دوئه (فرانسه)
- اینیاکی ویلیامز (غنا) و نیکو ویلیامز (اسپانیا)
- دریک برابی (غنا) و برایان برابی (هلند)
- جان سوتار (اسکاتلند) و هری سوتار (استرالیا)
- لوکاس هرناندز و تئو هرناندز (فرانسه)
- کوئنتین تیمبر و یورین تیمبر (هلند)
- لاروس دوارته و دروی دوارته (کیپ ورد)
- لئاندرو باکونا و جونینیو باکونا (کوراسائو)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132868" target="_blank">📅 16:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
چه پولای خرج کرده اقای پ.ج
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/132867" target="_blank">📅 15:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
چه پولای خرج کرده اقای پ.ج
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132866" target="_blank">📅 15:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132865">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
محمودی همراه با تیم ملی به آمریکا میره و اگه کسی مصدوم بشه جایگزینش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132865" target="_blank">📅 15:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132864">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
با رفتن سروش رفیعی شرایط تغییر نمیکنه امید عالیشا هم باید بره…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/132864" target="_blank">📅 15:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132863">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
بازیکنانی که به صورت قرضی یا حتی دائمی احتمالا از پرسپولیس جدا خواهند شد:
❤️
امیررضا رفیعی
❤️
محمدحسین صادقی
❤️
سهیل صحرایی
❤️
مجتبی فخریان
❤️
ابوالفضل بابایی
❤️
علیرضا عنایت‌زاده
✍️
خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132863" target="_blank">📅 15:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132862">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
❗️
پل پرسپولیس برای صعود به آسیا
🔴
باشگاه پرسپولیس در روزهای اخیر پیگیری‌های خود را برای رسیدگی به پرونده دیدار این تیم مقابل ملوان افزایش داده و امیدوار است با استناد به موضوع استفاده از سینا خادم‌پور، بتواند ۳ امتیاز این مسابقه را به دست آورد.
🔴
برخی منابع…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132862" target="_blank">📅 15:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c98a8b0a5.mp4?token=XdDirEMddhistykMLQelccsabdNuGt_QQAEyF6WEpWQ86ag_amKyh-XgPOMYgkl87PN9boLsswGSw-K-18Fn7Xnku8RkUuVoVC4cwqaKyG-MS7AjenXXxybUmc9l7U0JuJT01-YhgkOWLlLRj-BHDSvICz0VbhLOvCpbcyVGs_HXauSRkXqz6b9JRikhRHziaKDfUGjrG8w5v2HA9uQvy119OWekoJKFzmi_PtMrUGGL-XYivv2uVO2VcGX-8RmFvru14_wmXWAy9I_VsdFKAuZaXIzM9xvw1CcE4D1J83LKHjSeLLP-1UNHqMaG2qopyJxi6KE-zNMigMEzI6GrZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c98a8b0a5.mp4?token=XdDirEMddhistykMLQelccsabdNuGt_QQAEyF6WEpWQ86ag_amKyh-XgPOMYgkl87PN9boLsswGSw-K-18Fn7Xnku8RkUuVoVC4cwqaKyG-MS7AjenXXxybUmc9l7U0JuJT01-YhgkOWLlLRj-BHDSvICz0VbhLOvCpbcyVGs_HXauSRkXqz6b9JRikhRHziaKDfUGjrG8w5v2HA9uQvy119OWekoJKFzmi_PtMrUGGL-XYivv2uVO2VcGX-8RmFvru14_wmXWAy9I_VsdFKAuZaXIzM9xvw1CcE4D1J83LKHjSeLLP-1UNHqMaG2qopyJxi6KE-zNMigMEzI6GrZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جنپو با گاوداری قراردادش رو فسخ میده و طویله گاوداری باید چیزی حدود 4 میلیون دلار به این سوپراستار غرامت بده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132861" target="_blank">📅 15:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💢
با حضور در لیست تیم ملی، میلاد محمدی سومین تجربه حضور در جام جهانی را خواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/132860" target="_blank">📅 15:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132859">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
اوسمار ویرا به مدیران پرسپولیس اعلام کرده است که به پتانسیل رهبری امید عالیشاه برای فصل آتی در پرسپولیس نیاز دارد و این بازیکن حتما باید به مدت حداقل یک فصل دیگر در پرسپولیس حفظ شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/132859" target="_blank">📅 15:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132858">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
بازیکنانی که به صورت قرضی یا حتی دائمی احتمالا از پرسپولیس جدا خواهند شد:
❤️
امیررضا رفیعی
❤️
محمدحسین صادقی
❤️
سهیل صحرایی
❤️
مجتبی فخریان
❤️
ابوالفضل بابایی
❤️
علیرضا عنایت‌زاده
✍️
خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132858" target="_blank">📅 14:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132856">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
واکنش تاج به ناامن بودن شهر تیخوانا: کاری به مواد فروش‌های مکزیک نداریم و نمی‌خواهیم هم اصلاحشان کنیم!
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132856" target="_blank">📅 13:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132855">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚡️
⚡️
۴ بازیکن استقلال از حضور در تمرین منع شدند
⚡️
⚡️
عارف غلامی، ابوالفضل جلالی، آرمین سهرابیان و موسی جنپو با تصمیم سهراب بختیاری‌زاده سرمربی استقلال از حضور در تمرین آبی‌پوشان منع شدند.
⚡️
⚡️
آن طور که پیگیری ایسنا نشان می‌دهد، دلیل کنار گذاشتن غلامی و جلالی…</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132855" target="_blank">📅 13:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132854">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
👈
تهدید جدی تاج: آمریکا ویزای همه را ندهد، به جام جهانی نمیرویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132854" target="_blank">📅 13:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132853">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
پرسپولیس نمی تواند نسبت به رای بازی گل گهر و چادر ملو به cas اعتراض کند چون فقط دو طرف دعوی همان پرونده حق اعتراض دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/132853" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132851">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
محمد مهدی نبی مدیر تیم ملی، هدایت ممبینی دبیرکل فدراسیون ، مهدی خراطی مدیر اجرایی تیم ملی، سیامک قلیچ خانی مدیر رسانه ای ، محسن معتمدی‌کیا مدیر روابط عمومی و یکی از آنالیزور های کادرفنی به همراه افسران أمنیتی تیم ملی موفق به دریافت ویزای…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132851" target="_blank">📅 11:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132850">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
👈
خبرگزاری فارس : آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132850" target="_blank">📅 11:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132849">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f698e5343a.mp4?token=JjnYIUK7e6vrjIEIXLNrlHaeVfMsZVKaR67dEsALD-2RI6_27B40Fj3FdIAwfJwvblGN6nqbQ_3rM5vgW8pmtRmfWgzfdfb9e9aORLH51svGWAGVYcO8hENtDhmugk5u3cN4hodMRRGLtbb1FCTI9x-R9l8bp1eoBQYtRHQH8skgpbqqXmamFbzjmr4kT7-bRgfLcUOO2749UWgs4W03_9afqaNvyEia2KAxsCx3Za8ZhRopaRblFn7osvTLLcW4eWofYr_rw3r1B9KPOROelJMsMrSbAER2Av4HV0-b7I5cuY0tYrxYjbNKg5F7ITjUJrvNYf6fo2v93xe2pfSxlZnnm3WVBq6AZMrvtAd5aV0aEcTj7ekd9d-ggO50Le6tOU1zoDC68O7aT4fq535a6q356aKQSwgEmgwnEiOvVyFfRQULv3G3T0rYKlMZI41mEmjkKg1e_tjMeeyKSkm9ZmvmROIw_84yoWMDqYh8fhdx2vPLsuJxYzhaGzW62C_AnAWIka1UadguM39X53fI5xWhKWg7Q9T3i04JUIXH3B6nPPxy7OK8SFQbovTqDYpiDg_-5t37iFOUn0tvODRCxcQw01n0eopZ64IyG9I56ynCVOXxF5TWOSKOSWb5bfWlbhpEocefIpeSLv84AFzRPah6Jc1EOGlNPJZkrWgQEqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f698e5343a.mp4?token=JjnYIUK7e6vrjIEIXLNrlHaeVfMsZVKaR67dEsALD-2RI6_27B40Fj3FdIAwfJwvblGN6nqbQ_3rM5vgW8pmtRmfWgzfdfb9e9aORLH51svGWAGVYcO8hENtDhmugk5u3cN4hodMRRGLtbb1FCTI9x-R9l8bp1eoBQYtRHQH8skgpbqqXmamFbzjmr4kT7-bRgfLcUOO2749UWgs4W03_9afqaNvyEia2KAxsCx3Za8ZhRopaRblFn7osvTLLcW4eWofYr_rw3r1B9KPOROelJMsMrSbAER2Av4HV0-b7I5cuY0tYrxYjbNKg5F7ITjUJrvNYf6fo2v93xe2pfSxlZnnm3WVBq6AZMrvtAd5aV0aEcTj7ekd9d-ggO50Le6tOU1zoDC68O7aT4fq535a6q356aKQSwgEmgwnEiOvVyFfRQULv3G3T0rYKlMZI41mEmjkKg1e_tjMeeyKSkm9ZmvmROIw_84yoWMDqYh8fhdx2vPLsuJxYzhaGzW62C_AnAWIka1UadguM39X53fI5xWhKWg7Q9T3i04JUIXH3B6nPPxy7OK8SFQbovTqDYpiDg_-5t37iFOUn0tvODRCxcQw01n0eopZ64IyG9I56ynCVOXxF5TWOSKOSWb5bfWlbhpEocefIpeSLv84AFzRPah6Jc1EOGlNPJZkrWgQEqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هوادار پرسپولیس: سهمیه آسیایی حق پرسپولیس است. شعار سیاسی نمی‌دهیم. طبق قوانین جمهوری اسلامی تجمع کردیم. سه ماهه درآمد نداریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/132849" target="_blank">📅 11:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132848">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
استقلال با پنجره بسته خلیفه رو خرید و ما با پنجره‌ی باز همچنان اندرخم یک کوچه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132848" target="_blank">📅 11:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132847">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbkdPS_WLwFRTQoL1TkLVtsXU7k9NMOZ5afveKObo_auEIs0jQPGVaVCSJ2iN6kYBVC1jm1I1PF7o2Gt-4LJF-fHnh45efAu0pQGqnfOJzdAoKx2A_n6o1WFrevzA9-VJ-Mfkc8f6j74j1AOP_A5UyMdT1V1eHODwBKbDfe786yeN5nY_OUkZ0N1k75UPRGJ_LMwzimNPFj06UXw59s2mScKO0ODl9HkjarKpWYM5o9hqffyz1TXiu0NMWJmg3Ofi1sje49YT-jn7u4NeWvksOK22uZbktspm_vgNb9bbyOHU-cxq1zGdjIsGyM8GTzqa1WoxKJ-Eoo-rSjwvDJ3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمودی همراه با تیم ملی به آمریکا میره و اگه کسی مصدوم بشه جایگزینش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/132847" target="_blank">📅 11:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132846">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFVprsaKle75mn6K_JpzooFCUwIDvP4krjy2U4Vnne2GRhVGJrvcvf3eDy4uJHrd2NT6-DjZ1UE9ekYIImIYNt-OiyxHDsPZZAzm2D9BP30I-DZ4roaFUmT4IdIaAfbunnb21Zb8CFBaOpHfDh4aNfcEKv7SmRob3tRV_7SZt2JWGFUlzlmfjYwhS4yeqKy3WkGoOc1TFfkJFkGblpEG2wXrwGG6GJG2Tntq7H__Il9ilqD-OiZc3KCvLLzlr5OV2JEe47Vg2rPHeh8_zpiee3s9TFSSl3xQULbOd0gf2mqnCulMqoU6cs8PptZk3zdNHu_F3N8JOL5FRxbmRQhIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
اوسمار ویرا به مدیران پرسپولیس اعلام کرده است که به پتانسیل رهبری امید عالیشاه برای فصل آتی در پرسپولیس نیاز دارد و این بازیکن حتما باید به مدت حداقل یک فصل دیگر در پرسپولیس حفظ شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132846" target="_blank">📅 11:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132845">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوووری/ حدادی مدیرعامل باشگاه پرسپولیس: در صورتی که سه امتیاز بازی گل گهر و چادرملو به باشگاه گل گهر داده شود به فیفا شکایت می‌کنیم. چرا باید فدراسیون فوتبال در روز تعطیل رای صادر کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132845" target="_blank">📅 11:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132844">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=ZNnKvpkpE94pxwlCaM7tpb0UXuhvoRzciGXVM6TGWGnjOZS7-_eDRncwIao0VoEfQXrYh6pSUC8e_hRhzUofm8pq8wvoyguhzRmmBbPW0PTMwrXTkqBdOMPqDI__ZEun6OcSijoww6xHF6t_l3fOVA9a8KwNC_sPYN6A_sAM3Nyg9EiTeeIKmRquI7u8sG4buw_VC7_XOYDc1iU0kR0_kIwofemjbSl5Z-YgVcoB763GyROxkZdOYqqWMDG7A2gCLqF71vO3QAfVnnoU1OQWSEb3hzQyxXHH6nAUjHm0iTqdN8OWMxSUC4IMXGjJqtURx8K4SYvMldHjCD_zA9abSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=ZNnKvpkpE94pxwlCaM7tpb0UXuhvoRzciGXVM6TGWGnjOZS7-_eDRncwIao0VoEfQXrYh6pSUC8e_hRhzUofm8pq8wvoyguhzRmmBbPW0PTMwrXTkqBdOMPqDI__ZEun6OcSijoww6xHF6t_l3fOVA9a8KwNC_sPYN6A_sAM3Nyg9EiTeeIKmRquI7u8sG4buw_VC7_XOYDc1iU0kR0_kIwofemjbSl5Z-YgVcoB763GyROxkZdOYqqWMDG7A2gCLqF71vO3QAfVnnoU1OQWSEb3hzQyxXHH6nAUjHm0iTqdN8OWMxSUC4IMXGjJqtURx8K4SYvMldHjCD_zA9abSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فوری
👀
تجمع هواداران پرسپولیس مقابل فدراسیون
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/132844" target="_blank">📅 11:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132843">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtvmAnXAVppQWfQRP5oxRAkUS10MD3MnAXIXLewFAHrbKtlABcS9OasrdSNNadjRWXm-REU6oB9IJhE3EapT29LXc1n-urWXYFCUkWwJKOC1oi4-Xnf5pfUR6b7z33x23KYpICaA8EH0EiwT1vcc0ZsKTe-20-U7p_9Oo3ZCu3wViRIuVStG07vWVfj-bzU8H9KiMABTm4rGOV8Yt4j6QlQWPWMiLZHmfMFXTVS89UKmLwihyHoBlQ0MLkJTUHOsH0uFXH9f_gcb00KlmKVm5qonz7PS6Cud5KQsqq8q4jpldk200SgrWhHHh1R4a42FSGwAyZchC9RxxAWSFCHtAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
این یک فاجعه است!
😆
به
بازیکنان جام جهانی ایران
ویزای ورود به
ایالات متحده
اعطا شده. اما اونا شب رو در ایالات متحده نمی‌مونن. اونا در
مکزیک
مستقر میشن و سپس برای هر بازی به اونجا پرواز میکنن. یعنی اونا باید در همان روز بازی از طریق
اداره مهاجرت ایالات متحده
از مرز عبور کنن. این یک فاجعه است/ تریتا پارسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/132843" target="_blank">📅 10:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132840">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
ادعای الجزیره: ١۵ نفر از تیم ملی ایران ویزا نگرفتند!
🔴
بر اساس ادعای تلویزیون الجزیره، درخواست ویزای ۱۵ نفر از اعضای تیم ملی ایران صادر نشده است. هنوز مشخص نیست که این افراد شامل کدام اعضای تیم ملی هستند اما به هر حال جزو نفرات اصلی درخواست‌کننده ویزا محسوب…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132840" target="_blank">📅 00:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132839">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIxIunE10j6u4j7H3CXafXvDf8uY-urSAOoT34s7L0dBn9TpMEBj5b5Ay0IRZ1xalnTLgzVDuItLluxrmJJyYOujUHdPlEBrlIjI9f2K3lQwbpNweDKwdzMz4apml9G6lEUUeVgnAsxsjEbSx9yes4RZefgEWHfX1H5_ED8Agrhp6Wz2OROwu_ov7lEsNI2ddhL329T4Igx2HtuZfQg81e3Fw7Wx9C4mDcDBoMnunoSfdtHWSREgT5XZ7MAADq7UCA9p0NWWgfJLbc6tjvO-UT_vlUuiBLceu_JRDtqGbUwFXuwsxcU99lglVaHqTi8coZS_3s_ur5Xqy656ukNnkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
شهریار مغانلو:
❌
می‌خوایم سه پیروزی بدست بیاریم و با ۹ امتیاز به مرحله بعد بریم
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132839" target="_blank">📅 00:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132838">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGRBXSTyrZiS4mSeXikcZFS9mXMzu0KC5Ln0s-HKoyDCI_EiNL5oilIO1LjxeLnWr5DgQjs9HN5A9Qk_vobClrD2d2pYbobwug2kXyOmLOI8Nn7nxHIkcYVvaZ5im71fxRI5rcy3iLm4_XqCg4LVfnFmOKnV8OnOiql6SC9-0lbIaJtw7f_EMQQmZmn4VSAqVZsEpIx0yWd7rIQXD3Xl3BK88ccrmH8lWByQGTojZLNRRLjHlIklxgkAnQ8drIGS8W8UgmGgWR0K1VhK4wP_RfZnD2w-JXeRcnb_-6h-34dPAAbyhbuQe_Hl7XMru7R-LSdj-vN1y4ZkYFWm-2d5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرهیختگان: پرسپولیس پیشنهاد داده که میانگین امتیازات سه فصل اخیر رو برای لیگ 2 قهرمانان آسیا در نظر بگیرند و طبق اون نماینده ایران در این تورنمنت رو مشخص کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132838" target="_blank">📅 00:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132837">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
👈
خبرگزاری فارس : آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132837" target="_blank">📅 00:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132836">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎙
🤍
مهدی طارمی:
⚪️
اتفاقات تلخی رخ داده که همه دنیا از آن آگاه هست، اما کاری که از دست ما برمیاد اینه که با بازی‌هامون لبخند رو به مردم هدیه بدیم. ورزش از سیاست جداست. ما در ورزش نشون می‌دیم مردمی صلح‌طلب و محترم هستیم و نه اون تصویری که از ما در جهان نشون داده…</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/132836" target="_blank">📅 00:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132835">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a60445fb.mp4?token=sxJduj_2X4s2ttSOgpLxSAFN9Qta2uBw7oskftue0sDp4bz89VUfDlZzD_UebC3IcCeY_JEazWZs7lvakBq1L0C0XlnSyOCGfJqVBdp2N_YNcXOrmxaOkACpdouk0yzWW7laW6BC_SKeWbjvbyveT2dJPlDhuK-am1y8iwSEHek8kTi_jwfkfep0KIcUQnwLw2FeLe1rQWLMKik0xPEmlRcuAyEOpGySdc6-Ot7_KHX8SCkzHJIvEVpMIFHwGwyI-QGxJRMtYXXvZPoET2u08kzJ8xvMugGFT5VGoM7s3NnMDFuB0Bk7cA8tmMy4jxwYCGxQ_MsyqyAnq8mIsijVdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a60445fb.mp4?token=sxJduj_2X4s2ttSOgpLxSAFN9Qta2uBw7oskftue0sDp4bz89VUfDlZzD_UebC3IcCeY_JEazWZs7lvakBq1L0C0XlnSyOCGfJqVBdp2N_YNcXOrmxaOkACpdouk0yzWW7laW6BC_SKeWbjvbyveT2dJPlDhuK-am1y8iwSEHek8kTi_jwfkfep0KIcUQnwLw2FeLe1rQWLMKik0xPEmlRcuAyEOpGySdc6-Ot7_KHX8SCkzHJIvEVpMIFHwGwyI-QGxJRMtYXXvZPoET2u08kzJ8xvMugGFT5VGoM7s3NnMDFuB0Bk7cA8tmMy4jxwYCGxQ_MsyqyAnq8mIsijVdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ترامپ: اوضاع با ایران خوب پیش می‌رود
💢
رئیس‌جمهور آمریکابه خبرنگاری که از او درباره آخرین وضعیت مذاکرات با ایران سئوالی پرسیده بود، گفت: به نظرم وضعیت با ایران نسبتا خوب پیش می‌رود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132835" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
