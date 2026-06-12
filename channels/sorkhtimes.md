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
<img src="https://cdn4.telesco.pe/file/LucBEnIW3xQ1js7fjDD14wqoWoMQ05EELkb7BkCQasP5vz1-FSGX7cqvcxPjyHxFzpXKd7AsKz8Le45UWl8wnTETdNggvRm7j11neUzpVrbCDx54nRbLU_q4PE1XegMg70pEZFIp30IEjJpmQfyf6K1NWNQV1qFXkRUjeUTmYuTlSC99PW0xbZBVVIBroD--by7i2ypjdgWtOtRM9E98Cx3amvL4V569DirCTKcnnfc5zbAlFEqnHQmmg-NmDM9feS7NERHCjtjCR9uKVJeI4FjbJp57kLk6ftj-U8MgetJ3ScaOZayv7N8Uhjlt7SQBfHRA3mtVDPjxC2cMMU-lrg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 22:28:47</div>
<hr>

<div class="tg-post" id="msg-133359">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd1dc6dde.mp4?token=bCZdFdSjRdpIOLXNyUa9jCUOv9YmG1pMLN7EJsL5omJ0v5aa15zJiqQhWqiEd0qUMv7EfqCwJ8-xwIIdZBTvvmvt93EMYxBX_kMWxUy-KCyzRt6UiM63sOr7iT9m-GrxqB0aGFA6Y3p_SQctoa4GfgXwGxV89UHoP_uMH1tE8i1YuAUzvyIuqzwTPbTIM9_b_L8XbPjbOpXkbU5qjPM3An-y_davPwl5P9VAdmuVB2_4hfpBap9uTFHQ7j-ef5FBs3vfIbUe09clHPfR99GnVIn5WplLXHn8ibqqdG27-LqDpJ75uexZXUP50__8oNuNeHMfW6_vEV5E7C_HVD_Qng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd1dc6dde.mp4?token=bCZdFdSjRdpIOLXNyUa9jCUOv9YmG1pMLN7EJsL5omJ0v5aa15zJiqQhWqiEd0qUMv7EfqCwJ8-xwIIdZBTvvmvt93EMYxBX_kMWxUy-KCyzRt6UiM63sOr7iT9m-GrxqB0aGFA6Y3p_SQctoa4GfgXwGxV89UHoP_uMH1tE8i1YuAUzvyIuqzwTPbTIM9_b_L8XbPjbOpXkbU5qjPM3An-y_davPwl5P9VAdmuVB2_4hfpBap9uTFHQ7j-ef5FBs3vfIbUe09clHPfR99GnVIn5WplLXHn8ibqqdG27-LqDpJ75uexZXUP50__8oNuNeHMfW6_vEV5E7C_HVD_Qng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
لحظاتی از مراسم افتتاحیه جام جهانی در کانادا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 579 · <a href="https://t.me/SorkhTimes/133359" target="_blank">📅 22:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133358">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
رویترز: امارات با آزادسازی مجموعاً ۱۰ میلیارد دلار از دارایی‌های ایران موافقت کرده بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/SorkhTimes/133358" target="_blank">📅 22:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133357">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
🔴
آکسیوس : ترامپ در  تماس تلفنی با نتانیاهو گفته:
❗️
«این همون توافقیه که دنبالش بودیم؛ یک توافق عالیه و وقتشه جنگ با ایران به پایان برسه .»
🔴
طبق این گزارش، نتانیاهو در این گفت‌وگو زیاد حرفی نزده و ظاهراً متوجه شده که توافق در آستانه نهایی شدنه و توانایی…</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/SorkhTimes/133357" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133356">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
⭕️
آکسیوس و کانال دوازده اسرائیل تایید کردن  توافق بین جمهوری اسلامی و آمریکا نهایی شد
✅
کانال 12 اسرائیل : سرانجام توافق شد ؛ این توافق قطعیه و به نتانیاهو اعلام شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/133356" target="_blank">📅 21:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133355">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
#فوری | ادعای ای‌بی‌سی به نقل از منابع:
🔴
پیش‌نویس توافق از سوی مقامات عالی‌رتبه در نظام ایران تأیید شده است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/133355" target="_blank">📅 21:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133354">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
حالا دیگر ارتش سرخ هست تا جلوی هتاکی شما و تخلف غیرحرفه‌ای را در راستای حرفه‌ای‌سازی و معرفی نماینده آسیایی بگیرد. حرفه ای گری کسب و کار پرسپولیس است.
🔴
با مراجعه به صفحه AFC در اینستاگرام با هشتگ #FairACL2ForIran به اقدامات غیرموجه فدراسیون و سازمان لیگ…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/133354" target="_blank">📅 21:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133353">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-Wr9wAvjQUJ6GUGgGIXU4szmlstNAHFVyhF5kdPVlHCLn9qlV32YnVPTtADsDWh1hOtox5xtxfPv_RU8NkcpUtGEgqFMZaE4CMiRBzFacQayLI2lxxs31ESoqEoROaj5hxrTKjOsm56LiRePK6n-jYbc9TSZ9jbkL_uUPZr4b8a87iDcQvmJI-CZsIx_tVQX-8dCs_wGhLX6KNymd7jvieog3joyB2FMb5CKcSyxEH8T_JnI1dpDY3S5ihXHsx_lPZjFTUOMF0-SNrOaAKSVB_nMWDE1w5GDPnxokPTfAhQvebAjFHN-EbpC_G6W8dM_eZ957ly96174EVrbRQwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حالا دیگر ارتش سرخ هست تا جلوی هتاکی شما و تخلف غیرحرفه‌ای را در راستای حرفه‌ای‌سازی و معرفی نماینده آسیایی بگیرد. حرفه ای گری کسب و کار پرسپولیس است.
🔴
با مراجعه به صفحه AFC در اینستاگرام با هشتگ
#FairACL2ForIran
به اقدامات غیرموجه فدراسیون و سازمان لیگ اعتراض کنیم
https://www.instagram.com/p/DXkUpt7k5yN/?igsh=MWU5dzJvYnd3anpoMA==</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SorkhTimes/133353" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133350">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAxbBD4jZ7btNCv0Uf3Yfk79nW_hYSV1epsJ37rEVQYiBtyhzUl5qjfn7oU79iqGLQ7dMfvZtoGTBGUXqtGEu23aRkg-BxoPyZITlhV8435lVm1V09WqxtJLx5PkZrK29h99SFQNoCk9vzKjDS_XYWJ7a3cwZ6fuedOVqjYp9JkewTClRBgZIgjscYt3iAhEJTABytGuautFzwr9i442E9kpqwsiEdq4pqPv0ql9nzHforK9Xo-ZzWqrROFBJ6Tvz-6hkVv90EdJFoLlT3qHl8m_IpIXi9x8KoulBsRMH0Mv1g2017wQ-HUa13Y88zonjib1HV0OJWIHD3voN2CmTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بازی‌های امشب جام‌جهانی رو با ۱۰ درصد بونوس اولین واریز پیش‌بینی کنید!
📌
جام جهانی ۲۰۲۶ رو با وینکوبت پیش‌بینی کن و ۱۰ درصد بونوس اولین واریز بگیر.
📌
چرخش رایگان گردونه، شانس روزانه تا سقف ۱ میلیون تومان.
🔗
برای پیش‌بینی بازی‌های جام‌جهانی با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔗
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SorkhTimes/133350" target="_blank">📅 20:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133349">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
⭕️
فوتبال ۳۶۰ مدعی شد که اگه اوسمار تا ۲۴ ساعت دیگه نیاد،باشگاه سراغ گزینه های دیگه میره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SorkhTimes/133349" target="_blank">📅 20:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133348">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/133348" target="_blank">📅 20:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133347">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
پرسپولیس که مجوز حرفه ای خود را بدون مشکل در فصل جاری کسب کرده، به دریافت مجوز حرفه ای از سوی برخی باشگاه ها معترض و معتقد است کمیته صدور مجوز حرفه‌ای در این زمینه دچار تخلف شده است.
🔴
یکی از مدیران باشگاه پرسپولیس در این زمینه گفت: باشگاه پرسپولیس قرار…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/133347" target="_blank">📅 20:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133346">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
مهدی سالاری مدیر گل‌گهر: رای قطعاً به نفع ما خواهد بود و توصیه میکنم تمرینات پرسپولیس رو تعطیل کنید تا بازیکناش برای فصل بعد آسیب نبینن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/133346" target="_blank">📅 19:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133345">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
خبر فوری رویترز:
🚨
توافق توسط جی‌دی ونس و قالیباف امضا می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/133345" target="_blank">📅 19:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133344">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
پرسپولیس همچنان دنبال تیم «ب» از لیگ یکه، ولی باشگاه‌ها قیمت نجومی دادن و فعلاً معامله قفل شده؛ با این حال سرخ‌ها هنوز بی‌خیال پروژه نشدن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/133344" target="_blank">📅 18:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133343">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🔴
پرسپولیس در مشهد کپی می‌شود
🔺
مدیران پرسپولیس در ماه‌های اخیر طرح‌های مختلفی را برای تشکیل تیم دوم مورد بررسی قرار داده‌اند تا از این طریق زمینه رشد بازیکنان جوان و مستعد را فراهم کرده و مسیر حضور آنها در تیم اصلی را هموار کنند.
🔺
گفته می‌شود یکی از گزینه‌های…</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/133343" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133342">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
ایرنا:
❗️
متن توافقنامه با دقت بالایی نوشته شده و دیگه هیچکدوم از طرفین قرار نیست بدعهدی کنن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133342" target="_blank">📅 16:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133341">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzWY_fbhURXEK1FNU1fJOyOArko3HuCq_jJFzt3hL9aIRW3c8aQx8eKgVgBarMJxgNyt8afHqbP4WmuEVpek7q5oMV0i2qdDtMNe0bS-qHd1mfV0GEoWp6qXSD19FZvNh45aEIt5iEpf1DEiXK_4QhL2sE3IZmXF1UmlyEMA-a-g7EYIjFWH_NlT1Xbcwv26hA4hW-xGKaDw2Qo1JfFf7lH5_v91Z9wjcl4tpWvbqpAmbrkf5lTezOOr97BTCH8O_i-7pghjRvWbyYbo8uhnNtcbCmu8n5v-b9i0YHPdbLBhXh4wWFeT-01pwYHaveM14L9VsqILwCH0i7g_Uc1ZIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در نزدیکی کمپ تمرینی ارژانتین تیراندازی رخ داده و تا الان یه کشته و دو زخمی داشته!!!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133341" target="_blank">📅 16:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133339">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
پرسپولیس معتقده مجوز حرفه‌ای استقلال غیرقانونیه و داره در AFC پیگیری میکنه/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133339" target="_blank">📅 15:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133338">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📌
📌
خبرگزاری دولت:تمامی خطوط قرمز تعیین شده از سوی رهبر انقلاب، آیت‌الله سید مجتبی خامنه‌ای، در چارچوب نظارت مستمر شورای عالی امنیت ملی در متن مورد توجه قرار گرفته‌است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/133338" target="_blank">📅 15:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133337">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚡️
⚡️
خبرگزاری دولت:تهران در طول دوران تبادل پیام‌ها، برای اطمینان از اجرای برخی مفاد تفاهم‌نامه تضمین‌های معتبری از برخی طرف‌های ثالث برای اجرای تعهدات پیش‌بینی شده دریافت کرده‌است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133337" target="_blank">📅 14:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133336">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚡️
⚡️
خبرگزاری دولت:تهران در طول دوران تبادل پیام‌ها، برای اطمینان از اجرای برخی مفاد تفاهم‌نامه تضمین‌های معتبری از برخی طرف‌های ثالث برای اجرای تعهدات پیش‌بینی شده دریافت کرده‌است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/133336" target="_blank">📅 14:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133335">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
#فوری | سخنگوی وزارت خارجه:
🔴
متن توافق پایان درگیری ایران و آمریکا تقریباً نهایی شده و منتظر تأیید نهایی نهادهای تصمیم‌گیر ایران است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133335" target="_blank">📅 14:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133334">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyd5uD36yAsgEeQkXptk34lA0XU9LsnF5CYGT2tut1Jsyxi0dSE5j3THM-loOIuxc8shq8PMG3xI6akqNw1txyWU8M9bxRrKFCFAlP7o_24D3Un4stcION_xRKcHfJCTEJqbjJuRgDHD0hIimeyfJmdihaQyyyLEdv8wPAfcs4xY3DdD6ubfTojSmymwmFgO5NYaaN5EvszBmmpxd7PsICWC1dReE7in9w-KFrZJc-pbLNDJc0JpDQ_rrriGlFTmsDJMV5gmZ8m8ijapkqY8_Q8-LI-IS2Ue8Hcc6jrlZWlUg-voOJLzltcKmb9UE1Qq7RioSSxgxSLrBLsDgYXKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای تورنمنت 3 جانبه
پ.ن نظرتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133334" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133333">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmBiieDm1__55HvoHnAoTgJTlbFoXwUBC-jATF6BuJ6ypzkQ6Hm4fCUZLTzSTug-6REDs3zNhNZWjELIZ0Z57auVrMAFuCT1CggX2Lb1Ogtlxu63rYTN-dHwequk_A6Yt2UHFnAFmaOMV1nlOByrWy4Ow-uPwCzA2mhEn1B9twDpA1EF6cLLkJk-FYactcEN6oNUSHgyxKYit7KAYPQ69cFiA5ahXo1LKL8o-c0O_6gBNMMRFI54n34hMEmRYTDvT9HMPOF3yOrZYBCMdfekdkpa16dPuWHBI0H1WWEDng2byJ2qktXgHBEpACMqLN-C2HFpb8wzCCrFapWP5hnSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سینا اسدبیگی در لیست‌ اولیه‌ بازیکنان‌ مدنظر اوسمار ویرا قرار ندارد اما مدیریت باشگاه قصد دارد درصورتیکه با احمدنوراللهی یا محمدقربانی قرارداد امضا نکند سینا اسد بیگی رو بار دیگر به جمع سرخپوشان بازگرداند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133333" target="_blank">📅 14:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133332">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
ادعای العربیه: یک تیم حقوقی پاکستانی برای حضور در مراسم امضای توافق میان ایران و آمریکا در یک کشور اروپایی شرکت خواهد کرد.
❌
ایران درخواست کرده است که توافق با آمریکا در یک کشور اروپایی امضا شود تا به آن جنبه و اعتبار بین‌المللی داده شود.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/133332" target="_blank">📅 13:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133331">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oAarWZf8Y_mWYkr2Z_MdvVaos-18mV-IY-J-xAwclyhjqV8a8r1_Aob5JFoymRVU_UoGMKfqygHy1QO-GttSy3lJ1lPthUCW8awv9FKviIqvWMtTf4LPyhtPBdu-9qedDiH-vU2eBD5EWOrhLPAkK2jPmNpm49m7Q-tJDNejV-VLI18OlRIU2OM35Iq7JFsRAtqgxE78FUblQqrm89v4d-RDgM2fAv623HzFETyK2AfN78eqzPCr5nUBnAXW4QqFy4dfYliFtCzwllyXAQxGnupY2eWxJindQRCv8kV7Fs3b9E09KZHoS_Io0kGs0o7kAtdIJwqIpdceBMBfFmoj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بونوس ویژه جام‌جهانی برای تمامی کاربران به مدت محدود
🎁
به مناسبت شروع جام جهانی، برای مدت محدود
۱۰٪ بونوس ویژه واریز
برای تمامی کاربران در نظر گرفته شده است، تا با قدرت بیشتری وارد پیش‌بینی مسابقات و رقابت‌های این تورنمنت بزرگ شوید.
🎁
این بونوس ویژه به‌صورت محدود و تا ساعت ۲۰:۳۰ امشب می‌باشد، که قابل استفاده برای تمامی کاربران سایت به‌همراه یک گردش پیش‌بینی با ضریب ۱.۸ ‌می‌باشد.
📌
برای ورود به وینکوبت از طریق ربات رسمی سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133331" target="_blank">📅 13:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133330">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
مقامات گروه ۷: تفاهم‌نامه آمریکا و ایران ممکن است همین یکشنبه در ژنو امضا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133330" target="_blank">📅 13:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133329">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
✅
مقامات گروه ۷: تفاهم‌نامه آمریکا و ایران ممکن است همین یکشنبه در ژنو امضا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133329" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133328">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
#فوری |دونالد ترامپ، رئیس‌جمهور آمریکا: ما امروز به جنگ با ایران پایان دادیم و این کشور توافق کرده است که هرگز سلاح هسته‌ای در اختیار نداشته باشد، چیزی که ما بر آن اصرار داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/133328" target="_blank">📅 13:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133327">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
فوری/ مدیران باشگاه پرسپولیس با ارائه مدارک مستند به afc خواهان رسیدگی به روند صدور مجوز حرفه ای باشگاه استقلال شدند. مدیران باشگاه پرسپولیس معتقدند فدراسیون در روند صدور مجوز حرفه ای دچار تخلف شده و خواهان حذف این تیم از آسیا شد/فارس
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133327" target="_blank">📅 12:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133326">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
حمله علیرضا نیکبخت به افشین قطبی: ذات خوبی نداشت؛ در قهرمانی پرسپولیس هیچ کاره بود! آن تیم را حمید استیلی و مرزبان قهرمان کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133326" target="_blank">📅 12:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133325">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1vRffZ4X8gWOnhcwPhhj0v-HqciTJDCel7T6aK3mmgvAlfXA31o_yrcVLTOwK7J-CJVSLjATzJJl-DPoEZjenHcrJBV2gEcYdy07pqMidzwWzyM6QzDaCIsQQDBU9xRvR9MKjTb-P_iUhk7aPwQDvP_5z32cr-nHlZGo_x14ItaihPDZfzgXcT3jJhAANqfRV33tdscQou8mbPKR9aG0d8IBOHeOm_FLLLKTdk0tRcxdqgyg9DxcduaD3bqTzzcCtI9bRmka8WtJlMMnEPqTMYH8xtCpjznzKTr05wF_F2X5OjXYOLCS39CzA244EXspCTTGU0KpEocdOMutiyIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
محبی چرا با پرسپولیسی‌ها میپره
🧐
✅
پ.ن خبریه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133325" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133324">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
فوری/ مدیران باشگاه پرسپولیس با ارائه مدارک مستند به afc خواهان رسیدگی به روند صدور مجوز حرفه ای باشگاه استقلال شدند. مدیران باشگاه پرسپولیس معتقدند فدراسیون در روند صدور مجوز حرفه ای دچار تخلف شده و خواهان حذف این تیم از آسیا شد/فارس
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133324" target="_blank">📅 12:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133323">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
کریس رونالدو کاپیتان 41 ساله پرتغال : من میتوانم چهار سال‌ دیگر بازی کنم و در جام جهانی 2030 نیز حضور داشته‌ باشم. حالا حالا ها برنامه ای برای خداحافظی از دنیای فوتبال ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/133323" target="_blank">📅 12:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133322">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 867 · <a href="https://t.me/SorkhTimes/133322" target="_blank">📅 12:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133321">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
دیبالا مهمون عادل تو ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133321" target="_blank">📅 11:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133320">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
🎥
لحظاتی از یک روز پرکار در زمین تمرین؛ جایی که پرسپولیسی‌ها با انگیزه و تمرکز، برنامه‌های آماده‌سازی خود را دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133320" target="_blank">📅 11:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133319">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133319" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133318">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/133318" target="_blank">📅 10:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133317">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
خلاصه دیدار
🇰🇷
کره‌جنوبی
2️⃣
🆚
1️⃣
جمهوری چک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/133317" target="_blank">📅 10:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133316">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇲🇽
🇰🇷
مکزیک و کره نصف راه صعود را طی کردند/ جدول گروه A جام جهانی پس از پایان شب اول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133316" target="_blank">📅 10:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133315">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
‼️
باشگاه استقلال صورت مالی شش ماهه (۳۰ دی ۱۴۰۴) رو روی سایت کدال آپلود نکرده است. به این دلیل که مدارک مالی و شفافیت در بخش‌های مختلف باشگاه در راستای حرفه‌ای‌سازی از سال گذشته آماده نیست.
🚫
یکی از الزامات اصلی مجوز حرفه‌ای‌سازی است که حالا استقلال فاقد این…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133315" target="_blank">📅 09:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133314">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNyiAAcg5m404pPmLxl7kZXWoDcXjw77YsBCPuPVElNV2qN8xVPETlj5vy-hrhroxa1s2F8pEdS8sP5h4_kC1la7nzXuKljPZFqOj19a3mDTf18Qc3BvtESY_DscdhlH_F1mR09oHeaLAhK3SK1hBr6GNMXWu8BZXDu63ELMmpo6s2PEBPAAITrB6iw7iLn5UMpLQEq_jSYDuW8Q0WkHBVnvA85uRWekJ6KA0geEtSmQUAoeUs0kRQsHyK2ZtnioDkaqzzvx0v5TgbvgfGrTDbE23YTfY5qztZQ5rfTC7kTeezSX1rHWEoyyOCutXL62wuZU00fyRNtSv9m9mx3xYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🇰🇷
مکزیک و کره نصف راه صعود را طی کردند/ جدول گروه A جام جهانی پس از پایان شب اول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133314" target="_blank">📅 09:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133313">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ed2nvvR-_TK3LOJOphJPESzmdYQz7OBfWL_Q2w1bTJlNELoonP7fWGnCCQ6LxjPlb5lEsm7MyOr5kXbeJTOHlyZ7wTO1fpQ2jG4wDO1kKh1aHBqfTL4XdScyrzlpGkRfVcklxlGGeV5zLsLjfbVGkZC_MvGeC5gutpS9jbnPdYAvUuhZpxCdAAiWxOVP_--_lEYAvKmZR91RQGKgceL-uMZo2TmAvmwfUkkfCduew0lvAsn4_TP2INoVr6KuIGQNIjnaysQRAoOi5ytjsODg61D-EUw5c3wiz3V2lqvD62EoNcexyBFUtcPPb_COx_f3pTA2DbeIizWsqwD6eZhKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بونوس ویژه جام‌جهانی برای تمامی کاربران به مدت محدود
🎁
به مناسبت شروع جام جهانی، برای مدت محدود
۱۰٪ بونوس ویژه واریز
برای تمامی کاربران در نظر گرفته شده است، تا با قدرت بیشتری وارد پیش‌بینی مسابقات و رقابت‌های این تورنمنت بزرگ شوید.
🎁
از همین حالا تا ۲۴ ساعت آینده ۱۰٪ بونوس ویژه روی تمامی واریزها به مناسبت آغاز جام‌جهانی که قابل استفاده برای تمامی کاربران می‌باشد به همراه یک گردش پیش‌بینی با ضریب ۱.۸
📌
برای ورود به وینکوبت از طریق ربات رسمی سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/133313" target="_blank">📅 01:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133312">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
✅
والیبال هم که زاییدیم و ست دوم هم باختیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/133312" target="_blank">📅 00:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133311">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
ادعای واشنگتن پست: رهبران عالی رتبه ایران و ایالات متحده این توافق را پس از دیدار با یکدیگر در مقابل رسانه‌ها امضا خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/133311" target="_blank">📅 00:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133310">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/133310" target="_blank">📅 00:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133309">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/133309" target="_blank">📅 00:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133308">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/133308" target="_blank">📅 00:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133307">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
ترامپ: عملیات جزیره خارک از دستور کار خارج شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133307" target="_blank">📅 00:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133306">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
والیبال هم ست اول و ۲۵ ۲۳ دادیم به بلغارستانیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133306" target="_blank">📅 00:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133305">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
#فوری | نورالدین الدغیر خبرنگار الجزیره در تهران:
🔻
همه چیز انجام شده، چیزی باقی نمانده جز امضای توافق
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133305" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133304">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚩
خبرنگار: آیا رهبر ایران این توافق را تأیید کرده است؟
🔴
ترامپ:  تا جایی که می‌دانم پاسخ بله است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133304" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133303">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
خبرنگار: وقتی این توافق امضا شود، آیا آمریکا فوراً محاصره را لغو خواهد کرد؟
🔴
ترامپ: بله، این بخشی از توافق است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133303" target="_blank">📅 23:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133302">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
ترامپ : همین الان با نتانیاهو صحبت کردم‌..او باید با توافق موافقت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133302" target="_blank">📅 23:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133301">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2zRh3UnZUTC45PP_MTaodtT8a1k5Kp9L4TUbGCVauhfkvsfkkKkfTuNqaaMXX05igkREF1m9KRxFluxGW3eV9ellyN3Hn9laFfDLVdW-HHLiZiluQNEv2p-tlAgBrOqTxBmOpJZV-W4nwhbLxMK61OX4p_3rlA0nHnok610ZvqP59kj5iiJICldYZjI89xD0G41m6r_HnTsOT1V9-smQLMF1Pk4XHAHj2M8v0ZIITmzOiOD3-26OaU6BD4sbjL_RSh5UJAm0q92iok26UAHO19K14mjxV8KT4QKR9kXR4RzH5m6bVUtw9nSTWOiJ99_hNSwiC2Ao81Y56WeN3jKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
توییت بزرگ‌ترین صفحه ترول فوتبال : خدایا، خواهش می‌کنم، بذار این اتفاق بیفته چون خیلی خنده‌دار می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/133301" target="_blank">📅 23:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133300">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
مبلغ رضایت نامه محمدمهدی محبی از سوی باشگاه اماراتی یک میلیونو دویست هزار دلار اعلام شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/133300" target="_blank">📅 23:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133299">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
بازی دوم والیبال ایران با بلغارستان هم شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/133299" target="_blank">📅 23:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133298">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
ترامپ : همین الان با نتانیاهو صحبت کردم‌..او باید با توافق موافقت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133298" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133297">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗️
ترامپ درباره توافق با ایران: همه بسیار خوشحال هستند. کل خاورمیانه خوشحال است. و فراتر از خاورمیانه نیز همین‌طور.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133297" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133296">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
🇺🇸
ترامپ: توافق به دستیابی به توافق در روزهای آینده بستگی دارد و ممکن است امضای توافق ایران در اروپا انجام شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/133296" target="_blank">📅 23:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133295">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb3074466.mp4?token=i1g9scXDZO9Mk21AQv93wLQ7pt6JYsMCqes1mfmrkaHObpHyMjpQfblII1-SvJ0VOArWo4ZvGjNEGVzas9V4ZXj4BsTgRFXirKmnVuJ8SKAWeYsFLef5NLDcDqJVB_J31W-CXk12yT1hKWESY5TlSmHJVs2d-a_l5dKQt_Rqw-kiJdQlOmdSqwxdhoiu23TyDGShqBUnv5ZFqQibICfjhFVDDPk73TDkZwIvvQlOKpybbH3xUIijLGjl4_NDdwsBHhTbb186A2Q07MUNCgyw584t3QXs67HOfWdHaBhXWNHZK0bszGYfdcCiXQg_5CzJAI3sSMd-ZNP-G6AGOagHkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb3074466.mp4?token=i1g9scXDZO9Mk21AQv93wLQ7pt6JYsMCqes1mfmrkaHObpHyMjpQfblII1-SvJ0VOArWo4ZvGjNEGVzas9V4ZXj4BsTgRFXirKmnVuJ8SKAWeYsFLef5NLDcDqJVB_J31W-CXk12yT1hKWESY5TlSmHJVs2d-a_l5dKQt_Rqw-kiJdQlOmdSqwxdhoiu23TyDGShqBUnv5ZFqQibICfjhFVDDPk73TDkZwIvvQlOKpybbH3xUIijLGjl4_NDdwsBHhTbb186A2Q07MUNCgyw584t3QXs67HOfWdHaBhXWNHZK0bszGYfdcCiXQg_5CzJAI3sSMd-ZNP-G6AGOagHkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول مکزیک به آفریقای جنوبی در دقیقه 9.
✅
اولین گل جام جهانی 2026 توووسط کینیونس زده شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/133295" target="_blank">📅 23:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133294">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
#فوری | منابع داخلی :
🔻
جمهوری اسلامی ایران پیشنهاد آخر آمریکا و توافق را قبول نکرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/133294" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133293">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
کانال ۱۲ اسرائیل: از توافق امریکا و ایران بی‌اطلاعیم و از اینکه رهبران ایران موافقت کرده‌اند ، متحیریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/133293" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133292">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
👈
ادعای اکسیوس: منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبر انقلاب همچنان لازم است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/133292" target="_blank">📅 23:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133291">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">☄️
☄️
اولین بازی جام جهانی رسمآ آغاز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/133291" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133290">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f10af992.mp4?token=ntQNY66RESxT7znX1AVQbmRYk-LeonMgGGwjiBCCxwMimrCKPgestd69ItAFe6M_KvuqXwAYQk3xGlfQPRmtJrNuoIP0UyRKW3NtJmmP2vBUFLw-pL_6D3cqFdli3ZKBn7bMw6BhC6RsjBgyz5o7jiBctrjPXOe-TQQAv3bmXb9DNL_chSE4w46U-kZyBzkZnN5_gE67M3bhUWFr1F6Hfrhn6-Q_rO65tCTn_Cd6Exw36mgpAUN5sm2leuueSIe1esos5Ou5QSMhcz5z0_RQYwK9xp7U-l0VUpg-Setoq8jK9eJQwjWuyiO1KDj75JHDEVLe9AL6V-ZcMEVurjsbcYiD0fPXeIKORLda9b-YzTXj6oEerSWvUHg30BTEmDTWhBAnii63h50iweRwdjQ6IkHe363YWdnW-rDxwimfxnReMWpies6cTErd8xpr4mMAwqa38ahiPOyJwLu_-aA7a9_ND4Y1HPVMdBeGBy3S1ldOym8OU9rbiCZGvyOprl7LTlQUrlZXbAl_E0a6rXlwZJ8ZvZcJSoRytiGlhXx8nZWXFyde78uCWyhdlY_fOi0zX4hEo3a_yjjjj34V9su0kp5t3vDl322xYxBsM92vZSQ3ISBqVHVcr17IYHJZ3sfLpZaGqLsGblPLTxsQZfNcCIbpXfl9yUoG9T24zsBxVcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f10af992.mp4?token=ntQNY66RESxT7znX1AVQbmRYk-LeonMgGGwjiBCCxwMimrCKPgestd69ItAFe6M_KvuqXwAYQk3xGlfQPRmtJrNuoIP0UyRKW3NtJmmP2vBUFLw-pL_6D3cqFdli3ZKBn7bMw6BhC6RsjBgyz5o7jiBctrjPXOe-TQQAv3bmXb9DNL_chSE4w46U-kZyBzkZnN5_gE67M3bhUWFr1F6Hfrhn6-Q_rO65tCTn_Cd6Exw36mgpAUN5sm2leuueSIe1esos5Ou5QSMhcz5z0_RQYwK9xp7U-l0VUpg-Setoq8jK9eJQwjWuyiO1KDj75JHDEVLe9AL6V-ZcMEVurjsbcYiD0fPXeIKORLda9b-YzTXj6oEerSWvUHg30BTEmDTWhBAnii63h50iweRwdjQ6IkHe363YWdnW-rDxwimfxnReMWpies6cTErd8xpr4mMAwqa38ahiPOyJwLu_-aA7a9_ND4Y1HPVMdBeGBy3S1ldOym8OU9rbiCZGvyOprl7LTlQUrlZXbAl_E0a6rXlwZJ8ZvZcJSoRytiGlhXx8nZWXFyde78uCWyhdlY_fOi0zX4hEo3a_yjjjj34V9su0kp5t3vDl322xYxBsM92vZSQ3ISBqVHVcr17IYHJZ3sfLpZaGqLsGblPLTxsQZfNcCIbpXfl9yUoG9T24zsBxVcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقدام جدید در جام جهانی 2026؛ بازیکنان ذخیره هم در مراسم پیش از شروع بازی شرکت می‌کنند و سرود می‌خوانند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/133290" target="_blank">📅 23:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133289">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
از امروز جام جهانی ۲۰۲۶ شروع میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133289" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133288">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZxYnd4otEXvGS2k9oZpNUDf-mzm7DtcigwPQYTTVnfXEfZPt8-Y6K8iqlphck9--SjiRkhzBENg56SRlZBRfd8BH5FEDsc---xCzMiDN2ZeyNdO9mDEgE5kyEMY3IeXAoT9UKlaeJtkxotBy77w_q8ungvINOoqJLHve5l-5a2pIIFGD85OCH89xsNgXXcWbXv92SORwzyWgkUgmK0T3mG1bDDR746Y1J-GSE9yb5-BGMsgqnkFdcuoTNokW5W-nBOBo0TycQpfxU_KbWMMtBEuFKsQ9QXKMhWeR_GGE3Eqw1r4LJrJhqVtylAY3TLP87ZcDVtfALVfzMo3_6gRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این دیگه چه وضعشه...
🔴
تا باسن بازیکن های سنگال و چک کردن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/133288" target="_blank">📅 22:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133287">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
فرشید حقیری: اورونوف و می‌خوان بفروشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/133287" target="_blank">📅 22:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133286">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
#فوری | منابع داخلی :
🔻
جمهوری اسلامی ایران پیشنهاد آخر آمریکا و توافق را قبول نکرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/133286" target="_blank">📅 22:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133285">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
معرفی تیم ملی ایران در مراسم افتتاحیه جام جهانی با نمادهای فرهنگی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/133285" target="_blank">📅 22:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133284">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
دیبالا مهمون عادل تو ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/133284" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133283">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ac505c0c.mp4?token=B34-IqfSbQ9OHETGYF2U3ZvfqXZDOv-P8mgZQol4ErZAUjt27hW8q8_DsHxLZuBbvQiwL17uXpp65Zg8587FvVXHHm-6xshG5Fc0NoXkJ7EQCK7r6r9ewXQTBK9Izg-JT7xEpTH4Gja8bJWqrWnTowQfoN3XzqAGNLQySn8ZRxe7TPyivEmC27acufMGq2bYbuIp9znSe_Y1-LgMCVI6IMrL-0Wo6tVaMMQzG_ejKL0m9eQbb8MdI8Be9hLdUB8kg6p9ALm0m9eO-xcQgfPqDVBn1O_M8asmNGQfP5ip9jCa6GvBzvJ34GA6zSfNqx__sMAjAqWqEBVocWqNhlMcIYMRMnRBum-0MYAwlDzLmIFG_NyUfc21UI2BswYwuxxaeoM3GB2cAqFe-LsN9yLfAxyixukOH2Vz2KOjLnH0XbJPQDCnySXIt3OSCX6NNEBugaidaUMGzfPocxMehXJgbxrQMWl6eJmS0-mSzlAx9HhAMzB_ePMCQJWLo-tBO0ExmDky08V9PCtAyikOMm81329BGrv4dLSNb8N5KXC_oSQZfaRPCAnNe7Jgjxhl2YPLTy2sVkDbqHHYcBzksMTDmymY7A23FoHmbOM4LUUZrNlA3w2A0mHixgOdM-u9geJEAkqUkG6poHUujl6ZI-dqu0xqJcHK97Ot_YqPFIn9YE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ac505c0c.mp4?token=B34-IqfSbQ9OHETGYF2U3ZvfqXZDOv-P8mgZQol4ErZAUjt27hW8q8_DsHxLZuBbvQiwL17uXpp65Zg8587FvVXHHm-6xshG5Fc0NoXkJ7EQCK7r6r9ewXQTBK9Izg-JT7xEpTH4Gja8bJWqrWnTowQfoN3XzqAGNLQySn8ZRxe7TPyivEmC27acufMGq2bYbuIp9znSe_Y1-LgMCVI6IMrL-0Wo6tVaMMQzG_ejKL0m9eQbb8MdI8Be9hLdUB8kg6p9ALm0m9eO-xcQgfPqDVBn1O_M8asmNGQfP5ip9jCa6GvBzvJ34GA6zSfNqx__sMAjAqWqEBVocWqNhlMcIYMRMnRBum-0MYAwlDzLmIFG_NyUfc21UI2BswYwuxxaeoM3GB2cAqFe-LsN9yLfAxyixukOH2Vz2KOjLnH0XbJPQDCnySXIt3OSCX6NNEBugaidaUMGzfPocxMehXJgbxrQMWl6eJmS0-mSzlAx9HhAMzB_ePMCQJWLo-tBO0ExmDky08V9PCtAyikOMm81329BGrv4dLSNb8N5KXC_oSQZfaRPCAnNe7Jgjxhl2YPLTy2sVkDbqHHYcBzksMTDmymY7A23FoHmbOM4LUUZrNlA3w2A0mHixgOdM-u9geJEAkqUkG6poHUujl6ZI-dqu0xqJcHK97Ot_YqPFIn9YE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عادل:
❗️
دیبالا چقدررر خوشتیپ بود.
خیلی خوشگل بود
😂
😂
🔴
نکونام:
خوشگل و جذاب هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/133283" target="_blank">📅 22:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133282">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leTH1fm05PpuRdt0w0j7qoMIxe4ygUDAYH8nUBqaTGJMTL0wbDf3LeUxagbLoDuNW9RE8G2zz5dp_mO4Sr4GT6KencvgyZaQ4UATZqr2fRdttroUvHKar2r6BczkYTv8CkTGVThkaj8UFAxBXGPzaJhbWzhKBtlAL7MITv0vFR8tOMOTj14U5K0yfM8yFen9cDmZdUwcvbTbpLnjP4iSVm9dOGKH81Bip6JDfyGTEyrQDmg-kxZAjZGdOq9jjfDiugx0sy7tMRW43SVJxSfvgJOM0mQMYhDHCv2eRSWzvolJQiPdKGsj-BIX6Z3WsqmA5x9NzIVzG6xvdkokszxQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دیبالا مهمون عادل تو ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/133282" target="_blank">📅 22:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133281">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
#تکمیلی | با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران ارائه شده و مورد تأیید قرار گرفته است، من به عنوان رئیس جمهور ایالات متحده آمریکا حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/133281" target="_blank">📅 22:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133280">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
#فوری | خبرنگار نیویورک پست:
🔻
ترامپ همین الان به من گفت که توافقی با ایران "تقریباً کاملاً نهایی شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/133280" target="_blank">📅 21:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133279">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
🎥
لحظاتی از یک روز پرکار در زمین تمرین؛ جایی که پرسپولیسی‌ها با انگیزه و تمرکز، برنامه‌های آماده‌سازی خود را دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/133279" target="_blank">📅 21:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133278">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
#فوری |  | ترامپ :
🔻
من، به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران را امشب لغو کرده‌ام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/133278" target="_blank">📅 21:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133277">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
#تکمیلی | با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران ارائه شده و مورد تأیید قرار گرفته است، من به عنوان رئیس جمهور ایالات متحده آمریکا حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/133277" target="_blank">📅 21:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133276">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
پست ترامپ از اولین بازی جنگ جهانی  امشب تا پاسی از صبح همراه با صرف موشک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/133276" target="_blank">📅 21:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133275">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJqDEGJ90cIojpRcexws0i2zpxyu6CxXLINvrfkH4gcVPJdCL8IB98p7v11Qdo8OWQUflQpBY6D-ijKzkDSApFCwjNj1u9npOT1eUFxyTn7vM4o7f0RnbdDHNEXDQ3_LUBKfZgjY9QHaCumtIMrKD79pee6-v9oASLFhhhon8vKm7wHk8shOm-rForiqVbB0ch1uijixtQX6jwIWzlaW4ABZ2dutkdYY7PlnwWYmla4J5ICeBLiwr9--k4k07w1L9CqEljpZaJkyfqAqg3IQZkQVkoOUBb4sBP9V0jGrLcGE66mEZ9yXe5EAf6bw71GBZGjHATzBpK-vWmsAeOaU9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
دیدار افتتاحیه جام‌جهانی ۲۰۲۶
[
مکزیک
🇲🇽
🆚
🇿🇦
آفریقای‌جنوبی
]
⏰
امشب ساعت ۲۲:۳۰
🏟
استادیوم مکزیکوسیتی
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
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/133275" target="_blank">📅 20:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133274">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
داستان پیچیده سهمیه آسیایی همچنان ادامه دارد!
🔻
در حالی برگزاری تورنمت سه جانبه میان پرسپولیس، چادرملو و گل‌گهر در هیات رئیسه فدراسیون فوتبال به تصویب رسیده و  اعضای هیأت‌رئیسه فدراسیون فوتبال به اتفاق در مصاحبه‌های خود درباره برگزاری تورنمنت سه‌جانبه صحبت…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/133274" target="_blank">📅 20:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133273">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98745e731.mp4?token=vI7LHZr8wa35_3rVM0HRQd8aW8xpF6d_0gxaC7kzCfl0QLeY3LBM4tqA1Yxq_7XfW18ECGYjSJYQv4BKECokpxvPqYiq8ifwk1OtYQvtDfi3J-vyrVQumeyBB1p5a5sHVnys1QtaalhkDY4ALN6g8jfI3InD-SiKa1bLpqVuhOajsuK5i8tODrfPeLWuC_0feIG2EulY-slfGOPZTeBwmEw-o__U-lSkuNOcehyzC4uLRI6TAd_gtDgFTRt1mn4vZ2E7fC0c5dSCVxfZgDmRYlY6ecg5SnSLoW1cZ-NLXa8cpy4ON2tcxfhnXAp79iJYrx7k-lDC2eAMVbavz8IoVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98745e731.mp4?token=vI7LHZr8wa35_3rVM0HRQd8aW8xpF6d_0gxaC7kzCfl0QLeY3LBM4tqA1Yxq_7XfW18ECGYjSJYQv4BKECokpxvPqYiq8ifwk1OtYQvtDfi3J-vyrVQumeyBB1p5a5sHVnys1QtaalhkDY4ALN6g8jfI3InD-SiKa1bLpqVuhOajsuK5i8tODrfPeLWuC_0feIG2EulY-slfGOPZTeBwmEw-o__U-lSkuNOcehyzC4uLRI6TAd_gtDgFTRt1mn4vZ2E7fC0c5dSCVxfZgDmRYlY6ecg5SnSLoW1cZ-NLXa8cpy4ON2tcxfhnXAp79iJYrx7k-lDC2eAMVbavz8IoVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کمتر از ۳ ساعت تا شروع جام جهانی؛
درب‌های ورزشگاه تاریخی آزتکا مکزیکوسیتی برای ورود هواداران باز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133273" target="_blank">📅 20:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133272">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f77Bp63GrdgfEU4VN7Xx_GI8dzMoPqDeInJYLiKS5JA3vcR0pCvLQatxJ9mKthRo8UFBvpCXwyAbkc7uJbQlSGMvEjB5YbGdhRNDfVtFGjUJo5nsv7dCuk_3c4PonAtXA9Xo78rkc8D28C-pqsaYAFtNFskVOmI7Li5sDzeq3PZN0rtRSjrFj9HrezAa47Xj6FcTivR_Za7-CaF1lpnnXd063Lfl_xXGxGf08LcqDDTAlFpS7zx9_7nKAW-4fvHjdBWQ41LWgJhXLe66R3zt-VPfaQyuP3fMYdjbIn-h4AnOqHfEx3n_dRqPRlAzCscwrOhJNdSlPy3Ret7SJ3nATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کشورهایی که هوادارای اونا حق حضور در آمریکا برای دیدن مسابقات
#جام‌_جهانی
2026  رو ندارن!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/133272" target="_blank">📅 20:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133271">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFeHVKCSYyPTKiVnRnUiJuf5-9WW4tJkHqSNtc_3j7XtnjPf52wFOXOHMX80GlbTW7Hi_2PtIr5Y0543x7YCpzw6ET82_Gr7aDOl3rwdTDaChBw_mRFmXe1duIgDPwtWAvyRobxoY1u9D-kj2Sar6MM91gVbu3TgBtKlzm7vAmB9kzL4yPMDusxJ_TP_3Y1_lcCYTX_2Hx9i5viSsApjKJKrx0r9CTF6r0t7rP2toAfC8dNrUuLtMnaFZ4_5qa7-VPfnD89WIeA0c_kAkA5BUUtyPmv_cmwWCpmqbyQHE7kLOA0mJ852rZa6LdQAccVy4qDItBaMq-8SnXlgnunHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پست ترامپ از اولین بازی جنگ جهانی
امشب تا پاسی از صبح همراه با صرف موشک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/133271" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133270">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
کاپیتان عالیشاه: بدترین کار ممکن الان انجام میشود مثلا ما تمرین میکنیم اما یکسری تمرین نمیکنند
🔴
ما نمی‌خواهیم سهمیه آسیا را گدایی کنیم این نوع سهمیه اختصاص دادن خوب نیست و باید در زمین مشخص شود زمان برگزاری بازی‌ها بود و راحت‌ترین کار ممکن برگزار نشدن بازی‌ها…</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/133270" target="_blank">📅 19:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133269">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
ورزش سه: مهدی ترابی مصدوم شده و ممکن است لیست تیم ملی تغییر کند و از بین هادی حبیبی نژاد و امیرحسین محمودی یک نفر مسافر جام جهانی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/133269" target="_blank">📅 19:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133268">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
گفت و گو با محسن خلیلی در حاشیه تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/133268" target="_blank">📅 19:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133267">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
گفت و گو با محسن خلیلی در حاشیه تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/133267" target="_blank">📅 18:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133266">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
اوسمار فردا راهی ایران می‌شود
❤️
❤️
محسن خلیلی:
🔴
باشگاه پرسپولیس بلیط پرواز اوسمار ویرا برای حضور در ایران را برای او فرستاده و قرار است او فردا جمعه عازم ایران شود.
🔴
او به همراه کادر خود عازم ایران خواهد شد تا تمرینات پرسپولیس را زیر نظر بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/133266" target="_blank">📅 18:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133265">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❤️
❤️
محسن خلیلی:
🔴
برنامه فوری فیفا همواره اعلام کرده باید بازی ها برابر باشد و عدالت رعایت شود
🔴
در لیگ ما بازی ها برابر نبوده و این عدالت نیست
🔴
اینکه بگوییم شرایط برای برگزاری بازی ها بود بماند
🔴
انتخاباتی باید صورت گیرد که شرایط همه با هم باید در نظر گرفته شود
🔴
دیروز جدول ای اف سی اسم گل گهر را گذاشته بود و ما اعتراض کردیم
🔴
ما دنبال عدالتیم و می خواهیم بازی ها داخل زمین انجام شود
🔴
چطور این قدر سریع سه نماینده به آسیا معرفی شدند؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/133265" target="_blank">📅 18:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133264">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd56fa69a.mp4?token=utZSJLe_UeewHIFBDntgAkTHLSzxOaAIBlGQd9vfV9CBxPR7ZbmwBuNrxkivYTLqtxWzpR4a17bjpb3izah1CI9Oe4N13pLcdsiSwTOvkp3M2AZkmj6YrD26pjHGlIGwOw2Op1GJg3MTmtpdrm0Xnpty1w-K8pY2p0dKvYimotmYFEVC6Xxy3ycrICWN2cFL43mb-Lvi1Ys2ar7OW3Pri0nibEMnewRc8p_2MAyOr_QD9wpk8_vFkeUT1-h75zkO8mqdCXmMdWeZyrowL8AmS0i9S_eOmwUeRqE01_iQ-yqmlJU4tmj_FT10eIeUPDg9Q8bk2Ok5LSYt-qwwLuE1ZafJA9D7hbaoqE8oUG8E7CTg7t4L85v9PXfaNf3vizDq-Dl4fTlZWbNMfDbCXgfe-8TAErlyfZWBRHScpn9VMDQCixUTS8YU8ux-pdxiav_ewC9Ycm8JA6S1_1mnvtgk0Z17BP_WWw2i_3oXbn6W3Mn1yJ-oQUuhXDCsSllvQyORPiS14U9-6CqOot1rphZlMYAtjjH47_41OHpV1sh3JDrw5-r3VWILPksB-LuOXnpJzW0PdwSU1I5YwbnvnkkcI6t8Pg91gCeiSUvAJbjZAeIX9CZgWRFxX8bOBpkAijuEJtPV-1XDru17uaS9V1c1UblJPjuAv0E3nOQ7B8yaPdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd56fa69a.mp4?token=utZSJLe_UeewHIFBDntgAkTHLSzxOaAIBlGQd9vfV9CBxPR7ZbmwBuNrxkivYTLqtxWzpR4a17bjpb3izah1CI9Oe4N13pLcdsiSwTOvkp3M2AZkmj6YrD26pjHGlIGwOw2Op1GJg3MTmtpdrm0Xnpty1w-K8pY2p0dKvYimotmYFEVC6Xxy3ycrICWN2cFL43mb-Lvi1Ys2ar7OW3Pri0nibEMnewRc8p_2MAyOr_QD9wpk8_vFkeUT1-h75zkO8mqdCXmMdWeZyrowL8AmS0i9S_eOmwUeRqE01_iQ-yqmlJU4tmj_FT10eIeUPDg9Q8bk2Ok5LSYt-qwwLuE1ZafJA9D7hbaoqE8oUG8E7CTg7t4L85v9PXfaNf3vizDq-Dl4fTlZWbNMfDbCXgfe-8TAErlyfZWBRHScpn9VMDQCixUTS8YU8ux-pdxiav_ewC9Ycm8JA6S1_1mnvtgk0Z17BP_WWw2i_3oXbn6W3Mn1yJ-oQUuhXDCsSllvQyORPiS14U9-6CqOot1rphZlMYAtjjH47_41OHpV1sh3JDrw5-r3VWILPksB-LuOXnpJzW0PdwSU1I5YwbnvnkkcI6t8Pg91gCeiSUvAJbjZAeIX9CZgWRFxX8bOBpkAijuEJtPV-1XDru17uaS9V1c1UblJPjuAv0E3nOQ7B8yaPdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کاپیتان عالیشاه: بدترین کار ممکن الان انجام میشود مثلا ما تمرین میکنیم اما یکسری تمرین نمیکنند
🔴
ما نمی‌خواهیم سهمیه آسیا را گدایی کنیم این نوع سهمیه اختصاص دادن خوب نیست و باید در زمین مشخص شود زمان برگزاری بازی‌ها بود و راحت‌ترین کار ممکن برگزار نشدن بازی‌ها بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/133264" target="_blank">📅 18:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133263">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b0d9daf7.mp4?token=nYVo1Mk_WsyJOyymrdVS55Ph4MnL9Tn-JkegMgSaXtSDSDL4csdXQGuCYlmjbf1AVTEd4bvKsNhoj_XpTvq4Vpjw3b2UDGI-D6wZGJDyv7NJtPrps3CR8KsMnz6TKvGBPCuyM8CMvN7eilnn-j7YUg5GY9Oyl-SMJ3Gkv0yikDCFEdd8KgWnxwJraKAzAJTM5tkhAuIYbhwxaM_o9VzMvUDRY1n9WIW-OGEIYhsMpBf3KFVrshluel-wzo8Rps1GXRm_XDrcAqpV5IOfFpqECNTNftQrXYKF3M0gdzX1PINQ2sTTqNAJefKg7bUds6e7j-V1FhMr42JtU02_zNY1nKIaxLXZ2mhUaUcT_hM6FMKgu27nJq-zceYVULe4uSKq3GnzN1jgQ7u4qFJfh1Wx9wx35w5nCFRY29EOY-5GAuwpWnDIzAtjhxabESpmPtCWYRBBFSMbRh2cPiT-6YhBd7QRAiv2Q0a7ZwZvAAS-abeRpksq4MTm7D373YIg357L8HBvsrtO-AWqGPFpRoxiwBG3fi0auG1gfq9uACzf2tw1KDcL_QXF3rCjgugjJmH0joTWTqEmT3qhBJd-sNiUbuvO7sIxQYiIJJ7M72_Terh44MrvpKsiErzPl1O9ly0JcRtcDGOITLqTYwr6cyOvsWfocEfbD0EqStqZ5FSK8xU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b0d9daf7.mp4?token=nYVo1Mk_WsyJOyymrdVS55Ph4MnL9Tn-JkegMgSaXtSDSDL4csdXQGuCYlmjbf1AVTEd4bvKsNhoj_XpTvq4Vpjw3b2UDGI-D6wZGJDyv7NJtPrps3CR8KsMnz6TKvGBPCuyM8CMvN7eilnn-j7YUg5GY9Oyl-SMJ3Gkv0yikDCFEdd8KgWnxwJraKAzAJTM5tkhAuIYbhwxaM_o9VzMvUDRY1n9WIW-OGEIYhsMpBf3KFVrshluel-wzo8Rps1GXRm_XDrcAqpV5IOfFpqECNTNftQrXYKF3M0gdzX1PINQ2sTTqNAJefKg7bUds6e7j-V1FhMr42JtU02_zNY1nKIaxLXZ2mhUaUcT_hM6FMKgu27nJq-zceYVULe4uSKq3GnzN1jgQ7u4qFJfh1Wx9wx35w5nCFRY29EOY-5GAuwpWnDIzAtjhxabESpmPtCWYRBBFSMbRh2cPiT-6YhBd7QRAiv2Q0a7ZwZvAAS-abeRpksq4MTm7D373YIg357L8HBvsrtO-AWqGPFpRoxiwBG3fi0auG1gfq9uACzf2tw1KDcL_QXF3rCjgugjJmH0joTWTqEmT3qhBJd-sNiUbuvO7sIxQYiIJJ7M72_Terh44MrvpKsiErzPl1O9ly0JcRtcDGOITLqTYwr6cyOvsWfocEfbD0EqStqZ5FSK8xU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
رضا شکاری: باشگاه پرسپولیس هیچ وقت سهمیه را گدایی نکرده است؛ما مطمئن هستیم با برگزاری بازی‌ها می‌توانیم به آسیا برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/133263" target="_blank">📅 18:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133262">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf92abe2e.mp4?token=F6vy5xrjsy14_8zibUaRMZRaSspc1JKYp0BLvTc8_-dNZQZIgt7QFLLvxSkrZK2ghsNnXlCeUkoBryKq9nx6GHHzWxeHajCrUrOA9jyWPv6M-kVKCImLkqghK9d9FSEmZsAGkmAK2iNtAmz7dMGhURgVwPg6_oJd3JzS7oeDyYwZwPLvZmb2R4VoYC6b0xoIqpaSP_TjnN17AEgrzU9RKdmIaDbnJE6nf4fQISjEgM2sqzcgSBIGv73GjTuYE36sxvtMNUYxgRaaceSR8RTYkPYOeWeVMD2YY_71bq9hwXJwlXdoYPx7QB4ZfexFUO5fErPH10_vgB_ch-yOsiBdYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf92abe2e.mp4?token=F6vy5xrjsy14_8zibUaRMZRaSspc1JKYp0BLvTc8_-dNZQZIgt7QFLLvxSkrZK2ghsNnXlCeUkoBryKq9nx6GHHzWxeHajCrUrOA9jyWPv6M-kVKCImLkqghK9d9FSEmZsAGkmAK2iNtAmz7dMGhURgVwPg6_oJd3JzS7oeDyYwZwPLvZmb2R4VoYC6b0xoIqpaSP_TjnN17AEgrzU9RKdmIaDbnJE6nf4fQISjEgM2sqzcgSBIGv73GjTuYE36sxvtMNUYxgRaaceSR8RTYkPYOeWeVMD2YY_71bq9hwXJwlXdoYPx7QB4ZfexFUO5fErPH10_vgB_ch-yOsiBdYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور باکیچ و گرا در تمرینات پرسپولیس
✅
تمرین تیم زیر نظر کریم باقری در حال پیگیری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/133262" target="_blank">📅 18:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133261">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
اینطوری که فرهیختگان گفته باشگاه به علیپور گفته فصل بعد کاپیتان اصلی هستی این یعنی جدایی سروش و امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/133261" target="_blank">📅 18:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133260">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a69b9d7d1.mp4?token=PuGriCu-4mDkFb98tpUDIb7C-iaRuJQRymdRUmvJ01O7HcEnq-TVFMlfDrYc2FL9d5U0EsWtDQ1Ospmf9dVL3vD9mH-OdxGLI6SKmlEnAydl6a6P64kdHyyTEe_rQblHEbesabG1UFTbNDQyx6xJR2bB6eFYhY5bn5x-kezLO7nEqTpNepm-u13oU3Oq-B4DHSpPFT5Z8W8Wn2jdO3qxAMV3SJ3w6JYBIQVCwcEu6VK8UxiEn1FdI3FaiEB0GsqVf4nhkl-9KCahiKi4djPcBj-NvOZh6mDMGfm71JpdKHgiF_JNwH7Rpb5XlAnScnqgKbLRUBlrDTjdXpGRxio2U0q6jAzoCXhWxaaaEZ4E4kSu-6Jq2dCx_7gS1Inr0QXIqgonVGUpfu8Wi4zcIdjDuqV0udzJduIxWOl38Ur5CJquPeg_SAYUwYCZaLKX9vf6MHOlmkLGGtGcxhw9FlpPZrMPzUCeB_3f_1pwFvjbIIdak8NeBBQcZ8MZTnjeLtf6LTzL5L64RCFXvuUKk-dLBOZ3KBZc0cD5oyMtDHAv4Vh4FuZOOjV6M8G_944zVDvAftvLJh-ydHU3ZZX5bHUdvSA2D-oHHc7DLfn6s4rYWgoW6C4oDkwzYSV8HniN8I7WWSyhnjP1Egihjm645EUSWehCxeaYQOks3h06ssoChss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a69b9d7d1.mp4?token=PuGriCu-4mDkFb98tpUDIb7C-iaRuJQRymdRUmvJ01O7HcEnq-TVFMlfDrYc2FL9d5U0EsWtDQ1Ospmf9dVL3vD9mH-OdxGLI6SKmlEnAydl6a6P64kdHyyTEe_rQblHEbesabG1UFTbNDQyx6xJR2bB6eFYhY5bn5x-kezLO7nEqTpNepm-u13oU3Oq-B4DHSpPFT5Z8W8Wn2jdO3qxAMV3SJ3w6JYBIQVCwcEu6VK8UxiEn1FdI3FaiEB0GsqVf4nhkl-9KCahiKi4djPcBj-NvOZh6mDMGfm71JpdKHgiF_JNwH7Rpb5XlAnScnqgKbLRUBlrDTjdXpGRxio2U0q6jAzoCXhWxaaaEZ4E4kSu-6Jq2dCx_7gS1Inr0QXIqgonVGUpfu8Wi4zcIdjDuqV0udzJduIxWOl38Ur5CJquPeg_SAYUwYCZaLKX9vf6MHOlmkLGGtGcxhw9FlpPZrMPzUCeB_3f_1pwFvjbIIdak8NeBBQcZ8MZTnjeLtf6LTzL5L64RCFXvuUKk-dLBOZ3KBZc0cD5oyMtDHAv4Vh4FuZOOjV6M8G_944zVDvAftvLJh-ydHU3ZZX5bHUdvSA2D-oHHc7DLfn6s4rYWgoW6C4oDkwzYSV8HniN8I7WWSyhnjP1Egihjm645EUSWehCxeaYQOks3h06ssoChss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
مرتضی پورعلی گنجی، مدافع پرسپولیس: پرسپولیس در یکی دو سال اخیر با چالش هایی روبرو شد
⏺
بازی نکردن در ورزشگاه آزادی به ما ضربه زد. از وقتی آزادی را از پرسپولیس گرفتند به مشکل خوردیم. هر وقت در ورزشگاه آزادی برگزار کردیم به سمت قهرمانی رفتیم. بازی های فصل قبل دست به دست هم داد عواملی که نتیجه نگیریم
⏺
هواداران همه چیز را کنار هم بگذارند و بدانند چرا نتیجه گرفته نشد. باید تصمیمات درست تری برای تیم هایی مثل ما گرفته شود. تیم ملی؟ از سوال در این مورد باید بگذرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/133260" target="_blank">📅 18:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133259">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 229 · <a href="https://t.me/SorkhTimes/133259" target="_blank">📅 18:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133257">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Umk-sF0O8EFmQKQmiLQO3JuRSYwu_JrOgWxBre-XAoUlBN0FVv13vDWHPJpiGnCWiFcAxjjW2eddPatE03hhMxb-Pc8f5JlMfW_e-LoXacjIWdj-cAXPgIgldbgom7onDiRq0GkU9WyakvcX2bJiy1HpsNyQImxoRu5aRWrYLD-xHR27zImIwklSw_T9RZQQFBjhglvuF-FgfWFZpT3jeKp9MGw5U59PBGhyglKmJgYvvNgJ_R3Pi5_V4FbHJabBmPFe6jIoG8RHO_a199J719BinIYR1FiBOQSiBPigjNOFgEDJsFmQxcgrsOzE0sDlJfv44uhsfRK_PwRjQWLzwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
رای دادگاه صادرشد؛ حبس ۲ دوومیدانی‌کار ایران در کره‌جنوبی و تبرئه ۲ نفر دیگر
🔻
حکم دو دوومیدانی‌کار ایران که در پرونده اتهام تجاوز به دختر کره‌ای در این کشور زندانی شده‌اند، پس از بررسی در دادگاه تجدید نظر، تایید شد.
🔻
دادگاه تجدید روز گذشته برگزار شد وبر اساس آن حبس ۴ ساله دو نفر از ورزشکاران تایید شد.
🔻
دو نفر دیگر هم تبرئه شدند و می‌توانند به کشور برگردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/133257" target="_blank">📅 18:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133256">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
لحظاتی از تمرین عصر روز گذشته پرسپولیس؛ پرسپولیسی‌ها با تمرکز و انگیزه، برنامه‌های آماده‌سازی خود را دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/133256" target="_blank">📅 17:50 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
