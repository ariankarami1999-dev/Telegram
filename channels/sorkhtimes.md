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
<img src="https://cdn4.telesco.pe/file/FduoEuv5dTfRUMzyM-D7xGx-uUEnptrwreYnufN8T-qOcF2twJvHsDjK0jjhiBZuthAun1a_S7P5Gtb6Lbe_bqhMpx7ytr5ubc9pDCpl6xM-_LgjvJ6KT3UD8XTqRzJJc_G1twwy_FOe-zL5prsbGnUhO7W50B5mATXfinsXVXCcfI5joMMMubqAIlYPOg1dbiq5Gu6NviEFDTuPDK6kp-ZTBJ4CM0T6Vy3ONBddvgPJ2J-3hok1_0uGTvbDrrYkReC9c4E9gc39jDZSBmEEM6YOI8nUF_d8vaZQPPlHEzr4PmFF1JneUW3xzCZ-AlpIWazQg6rIJcod-k0Kr2aBIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 19:42:19</div>
<hr>

<div class="tg-post" id="msg-133952">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
پاکستان: مذاکرات فنی ایران و آمریکا فردا در سوئیس برگزار میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/133952" target="_blank">📅 18:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133951">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
فووووووووووووری
🚨
قرارداد اسکوچیچ دوساله خواهد بود
‼️
سه دستیار نیز به همراه اسکوچیچ به تهران خواهند آمد. همچنین گفته میشود مربی دروازه‌بان‌های اسپانیایی پرسپولیس در کادرفنی اسکوچیچ باقی خواهد ماند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SorkhTimes/133951" target="_blank">📅 18:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133950">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
پیمان حدادی برای بستن قرارداد به ترکیه رفته و اگر اتفاق خاصی نیفتد، تا ۲۴ ساعت آینده اسکوچیچ رسماً معرفی می‌شود.
🔸
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/133950" target="_blank">📅 18:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133949">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇵🇰
🇵🇰
🇵🇰
#فووووری شریف، نخست‌وزیر پاکستان:
🔸
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد. جنگ در تمام جبهه ها پایان یافت. مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SorkhTimes/133949" target="_blank">📅 18:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133948">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">💢
💢
#فوری؛ ادعای #فرهیختگان:
▪
پیمان حدادی برای عقد قرارداد نهایی با اسکوچیچ به ترکیه رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/133948" target="_blank">📅 18:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133947">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
#فووووووووری از فرشید حقیری: حدادی صبح برای بستن قرارداد با اسکوچیچ به ترکیه رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/133947" target="_blank">📅 18:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133946">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i3jn2AJlUT5b-4sEVAeW35nm2pzOnSrqHFx7NTlQdOkaF5FycIiKOpwgYXNgeFGeLyoyZaxVhVdC5CHA14jycVvOoXBTryEG15B-rwX2xw54FwD9AW36JgQaKmE-wOnS3OtRtu0IIuvFzGkk5Jq_hyxj2rFVtYifDyCvXpYQxXWho1L5Vc5DB9h8MAStKB448-F8uAg6Ag9Tq43KOJWZ5zW0vS8we9NQQhDpxXDrucTkEFqhyikGDFv_60agHE3oo3BvRAoJe9CrZAbWER8XK9DmItveLIPMoixxHx6MGoiFhjSqvhnBPVo40xueNXstjf734teiqC8dRFKIsst8pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عجب بازی‌های آسونی دارن تیما آسیایی تو این هفته
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/133946" target="_blank">📅 17:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133945">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
قرمز آنلاین مدعی است دو تیم خواهان سروش رفیعی شده اند اما او دلش با پرسپولیس است اما به حدی از برخی واکنش ها و رویکردها ناراحت است که ترجیح داده سکوت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/133945" target="_blank">📅 17:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133944">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
❗️
فرشید حقیری: اسکوچیچ‌ ترکیه ست و به‌ زودی با امضا قرارداد میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/133944" target="_blank">📅 16:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133943">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
سروش اگه پیشنهادی نداشته باشه خداحافظی میکنه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/133943" target="_blank">📅 16:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133942">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
⚠️
⚠️
تنگه هرمز مجدد درش تخته شد
🔥
قرارگاه خاتم الانبیا:‌ تنگه هرمز به دلیل نقض مکرر اتش بس توسط اسرائیل تو جنوب لبنان و کشتار بی رحمانه‌ی مردم بسته شد
🚨
اگر عهدشکنی‌های آمریکا ادامه پیدا کنه پاسخ سنگین‌تری میدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/133942" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133941">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
متن کامل پیام رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا :
🔸
بنده علی الاصول نظر دیگری داشتم ولی از باب تعهدی رئیس جمهور محترم به عنوان رئیس شورای عالی امنیت ملی به حقوق ملت ایران و محور مقاومت جلو اجازه آن را صادر…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/133941" target="_blank">📅 15:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133940">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
تیبو کورتوا:
✅
ایرانی‌ها یک مدافع راست به نام رامین رضاییان دارند که در حملات بسیار فعال است و ارسال‌های دقیقی دارد. باید مراقب او باشیم، او می‌تواند خطرناک باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/133940" target="_blank">📅 15:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133939">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇧🇪
تیبو کورتوا دروازه‌بان بلژیک: در بازی فرداشب آماده گلباران ایران هستیم چون برای صدرنشینی و صعود باید برنده شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/133939" target="_blank">📅 15:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133938">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⚡️
⚡️
⚡️
گئورگی گولسیانی در لیست مازاد باشگاه سپاهان قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/133938" target="_blank">📅 14:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133937">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1K2fUzBovWylGxoViliyZiD7YeNdmX7PRV-UAW7hBmFTOPEdXPkqtBFBgGod-6RTNLtjppdYqcH4hEvo8RvRKAbkZIawFPEuoO18qJaeT9BXzoqxHrHfU3cPs8DTpp6bc8R5DILiTjJeK7YTyjULHJWYYBcmktr3EI04qWGj43uG5iwFWVecS6scL6ZK5B6BKZd-h14lb5jIJAyNIRD_A6PqSYUfIgPfqraqyBaf9yEDUIsH-9jpz4w_LA75Yy86i2NEu2c-do41VtC-8oQuweukk91OIIchdeduzRW9nRhrS6tuJ_HBbBqYDsX1-aWkoK3XPYaFqJ4BgbExRzVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
روزبه چشمی، سوگولی گروهبان قلعه‌نوعی که رفاقتی رفت جام‌جهانی بازی بلژیک رو هم به دلیل مصدومیت از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/133937" target="_blank">📅 14:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133936">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
تصمیم نهایی با بانک شهره و انتخاب اونا هم اسکوچیچه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/133936" target="_blank">📅 14:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133935">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
برگزاری لیگ بیست‌وششم در اواخر مرداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/133935" target="_blank">📅 14:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133934">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
برگزاری لیگ بیست‌وششم در اواخر مرداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/133934" target="_blank">📅 13:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133933">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8eRQbF4ATPCX-DW8CWTYvrg7utwKx5o9y-2udh5SVrGbaB3zR46BScodJyhM7tvv1OkB-6quM66ZxrznynHzECYoh9NGxfStsiBj7wxUjcpfk2T23jZS42IZ4rPJpfci1ij_Demx6s8NRYjClJoSNnDbduXP2_3AvRvJ4BIbfzw6TmWZvolppAQql0JskOc07nZqdN3Md4FTIAKCGRCDK6wWQWM8XKYRtK-7FCNniXwQ8YOS4iui13c7pOTBMDyoG08C0JiSzNZqHh8lwLZqnuwuKqOwgjd-1TeK4sq6s-F7xfhbLLxBIev_SDqDDPyMmfYr8rmThqyQElntkCQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقل و انتقالات تابستانی لیگ برتر فصل 1405-1406 از 31 خرداد آغاز می شود و تا روز 4 شهریور ادامه خواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/133933" target="_blank">📅 13:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133932">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
از دیگر نکات، این است که پیش‌تر باید حتما یک بازیکن آسیایی در بین نفرات خارجی می‌بود (1+7) اما در مصوبه جدید الزامی به آسیایی بودن یک بازیکن وجود ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/133932" target="_blank">📅 13:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133931">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
این مصوبه البته یک استثنا دارد؛ اگر باشگاهی در فصل گذشته بیش از چهار بازیکن خارجی در اختیار داشته و این بازیکنان برای فصل آینده خود قرار دارند، استفاده از آنها بلامانع خواهد بود. در غیر اینصورت اگر قرارداد بازیکن خارجی تمام شده باشد، برای تمدید قرارداد تابع…</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/133931" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133930">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiowML8DDRlPS-uB5_JzvHEmsDM8HpLzN3KMgJoqEktD65fmPH5Af4NJ8WhFf2lNKm_gXTTKgHm6MC5hX4LzEqrs3YGVMfuY2z7GMDhPWVrWcEYU0Dv7Wkjig0RkfTPc7g5bLkNtxE3UJbdA1YjFANrmugqdFLwoeK8GqTxHfdYXG_WrQBdNyRNmKMk4g18UXr2RRb_KPaIdi7vHlouWZc6rRAnae7-Ub-szIkDMrG5L6b6nPSZ2mt3H-WDMJ_zTJv90x8TuS2lz_BruQ8rzzdbSi8sjnteVLH5X6qFF9Sgb1bzdc5aNoNPlmt1tuFkWe6UhSkck1SMT7pOH3QS9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه F جام‌جهانی ۲۰۲۶
[
هلند
🇳🇱
🆚
🇸🇪
سوئد
]
⏰
شنبه ساعت ۲۰:۳
۰
🏟
استادیوم
ان‌آرجی
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
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/133930" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133929">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
یکی از مصوبات دیگر و مهم جلسه امروز هیئت رئیسه فدراسیون فوتبال مربوط به بازیکنان خارجی بود. طبق پیگیری خبرنگار تسنیم بر این اساس سهمیه بازیکنان خارجی برای باشگاه‌ها که در فصل گذشته 1+7 بود، به 4 بازیکن کاهش یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133929" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133928">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
✅
ورزش سه :  طبق تصمیم فدراسیون و سازمان لیگ، لیگ برتر فصل آینده با حضور 18 تیم برگزار می‌شود و از لیگ ناتمام امسال، هیچ تیمی سقوط نخواهد کرد و قهرمانی مشخص نخواهد شد .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/133928" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133927">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🖍
فارس طی خبری مدعی شد باشگاه پرسپولیس با ارسال نامه ای به الوحده خواهان به خدمت گیری مبین دهقان شد
🔴
این بازیکن از الشارجه نیز پیشنهاد دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133927" target="_blank">📅 13:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133926">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
جدایی اوسمار از پرسپولیس قطعی هست/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/133926" target="_blank">📅 12:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133925">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
فووووووووری از ورزش 3: اعلام رای استیناف کنسل شده و تورنمنت قطعا برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/133925" target="_blank">📅 12:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133924">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
فووووووووری؛ تکلیف نیمکت پرسپولیس تا هفته آینده مشخص میشه. باشگاه از اوسمار تخفیف خواسته اونم موافقت کرده ولی میزان تخفیف رو اعلام نکرده/ فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133924" target="_blank">📅 11:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133923">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
اوسمار : امروز من سرمربی پرسپولیس هستم تا روزی که باشگاه تصمیم بگیره و بخواد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133923" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133922">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
فووووووووری از ورزش 3: اعلام رای استیناف کنسل شده و تورنمنت قطعا برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133922" target="_blank">📅 11:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133921">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
از باشگاه پرسپولیس خبر میرسد که با توجه به حضور مرتضی پور علی گنجی و حسین کنعانی زادگان در دفاع و همچنین احتمال جذب یک یا دو بازیکن جوان دیگر اگر اتفاق خاصی رخ ندهد مسئولان باشگاه قصد دارند نام ابرقویی رو در لیست مازاد قرار دهند
❌
البته مبلغ بالای دو مدافع…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133921" target="_blank">📅 11:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133920">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
فووووووووری از ورزش 3: اعلام رای استیناف کنسل شده و تورنمنت قطعا برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/133920" target="_blank">📅 10:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133919">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇧🇪
تیبو کورتوا دروازه‌بان بلژیک: در بازی فرداشب آماده گلباران ایران هستیم چون برای صدرنشینی و صعود باید برنده شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/133919" target="_blank">📅 10:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133918">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎥
خبر میثاقی برای تصمیم درباره نماینده سوم آسیا: تورنمنت سه جانبه بین گل گهر، چادرملو و پرسپولیس برگزار می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133918" target="_blank">📅 10:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133917">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
🇱🇷
#رسمی؛ آمریکا با برتری مقابل استرالیا به دومین تیم حاضر در مرحله حذفی جام جهانی ۲۰۲۶ تبدیل شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/133917" target="_blank">📅 08:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133916">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/133916" target="_blank">📅 08:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133915">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
کسری طاهری اعلام کرد با پرسپولیس به توافق نهایی رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/133915" target="_blank">📅 08:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133914">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkOLOkaqoNT1lZeo1R06j0H8q40VOJxdFn_0zY_cmjoW-swcCbaZ8Yn9z0lMphARi0aeZtRW0nLr9JPir4XGC1-RcAmhkI5PkeAkUSkui-SpNgOnkoR8tmbF5XAkKiwXVZSzYV5GunQd0-ULPyap2rXQUxnexPQ_Y5aduPdt0NX_dCx9heHs2DQZgoyogc3uBlsBDYQNbI5WfZYORXSpTg5F1sIDIexMZZHGcAfuYfde8Vq_sEBqbiTaUDk_DFrH9JDNcuUwBbnDGmTTpKJyNo8h8yFbvvK5Ms-rqWUN2_qt_QlxMx4HeLqIm5gyqXhhTs5YbAZzM2Ze_2MpCR-cnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه C جام‌جهانی ۲۰۲۶
[
برزیل
🇧🇷
🆚
🇭🇹
هائیتی
]
⏰
بامداد شنبه ساعت ۰۴:۰۰
🏟
استادیوم
لینکُلن فایننشیال فیلد
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
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/133914" target="_blank">📅 01:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133913">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/740f6c6148.mp4?token=EJL5mK73wWg2pSL0E5vtVnjZGXqcQYqQH62Zgv5gk25IzXYcQgtnDSEFP6pNo1jx_TOo9u89TV73xXDawxzvi_YBqLCxvpX6mIuwBWGNsGmnB_gxSkoJwyMf3JWoFjQOr4NQEmzGnseRQ-PCy4wuraaDGVeFBuutJDaZtLCNSYwidBR-gfa205wN53KVMQbZFIUshSWhwejSXkgMpu8AasNJWhjaacNfmvR9rfUb_YW-pBa2K1PUoXF23iKcb8QCSFkcMl86eDz_dxkJc7GHVSDA7d-sPimDz1z9eA_DTDbUlpyZrrNOs57aonjMBTsANZ6A-0ZP2__JETSo7Ha2yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/740f6c6148.mp4?token=EJL5mK73wWg2pSL0E5vtVnjZGXqcQYqQH62Zgv5gk25IzXYcQgtnDSEFP6pNo1jx_TOo9u89TV73xXDawxzvi_YBqLCxvpX6mIuwBWGNsGmnB_gxSkoJwyMf3JWoFjQOr4NQEmzGnseRQ-PCy4wuraaDGVeFBuutJDaZtLCNSYwidBR-gfa205wN53KVMQbZFIUshSWhwejSXkgMpu8AasNJWhjaacNfmvR9rfUb_YW-pBa2K1PUoXF23iKcb8QCSFkcMl86eDz_dxkJc7GHVSDA7d-sPimDz1z9eA_DTDbUlpyZrrNOs57aonjMBTsANZ6A-0ZP2__JETSo7Ha2yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
تا 37-38 بازی می‌کنم؛
پورعلی‌گنجی: در ایران فقط پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133913" target="_blank">📅 01:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133912">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
رونالدینهو: مسی، فرانسه را نابود خواهد کرد
▫️
کوچکترین شکی ندارم. مسی فرانسه را نابود خواهد کرد. نتیجه بازی به نفع آرژانتینی‌ها خواهد بود، آن‌ها قهرمان جام جهانی خواهند شد. مسی فراتر از یک فوتبالیست است. من می‌خواهم بعد از فینال به سمت او بروم و به او تبریک…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/133912" target="_blank">📅 01:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133911">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VajpKknSc31I5QmoDFNCaiffM2VoKvOUQn64-eTCEz5qoULB_snKJ2CAQw6dqO19iyiI0SJAuFGFpNbAVhV9p6cWLgtqUCkLbi2wJoVp87eUS7Ry_PKFBvl8JozPgnoZMvKsSgm-H_8_aT2wO3OHIlvrU39x-6i3q8rvwK54WkK8DsYXCPPAHCjUd80kOZrjQhzveEZjXMc7hkKfY1FeS22OPUWaWsZIz_k1SjtBRGHZMNhVTKUudGMJAMl4GIrzaJFp4l40yTTLLOBmLK_Ik8JysPqTW17gI5qYBCbWzRnBCZUpAdQ2CiqxFzfXg8vwWieUMSgeh9frGtIuEGryig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه روز دهم مسابقات جام‌جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/133911" target="_blank">📅 01:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133910">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
🇲🇽
تیم‌ملی مکزیک به عنوان اولین تیم راهی مرحله یک شانزدهم نهایی جام‌جهانی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/133910" target="_blank">📅 01:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133909">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فرشید حقیری : اینانلو همه تصمیمات رو داره تو باشگاه میگیره
🔺
پ.ن: باشگاهی که سگ صاحبشو نمیشناسه همینه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/133909" target="_blank">📅 23:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133908">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❗️
خیلی دلم برای تیم ملی تنگ شده؛
🔴
پورعلی‌گنجی: انتظار داشتم قلعه‌نویی فراموشم نکند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/133908" target="_blank">📅 23:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133907">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
#فووری؛ ادعای #فرهیختگان: اگر اوسمار با پرسپولیس به توافق نرسه تراکتورسازی به صورت جدی میره سراغش و برای فصل بعد اوسمار رو جایگزین محمد ربیعی میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/133907" target="_blank">📅 23:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133906">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
#مهم | لحظه امضای نسخه فارسی یادداشت تفاهم ایران و آمریکا توسط دونالد ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/133906" target="_blank">📅 23:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133905">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
بازگشا: ما فعلا با اوسمار ادامه میدهیم و توافق برای فصل بعد با او به آینده موکول شده است یعنی با توافق دو طرف تمدید یا قطع همکاری خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/133905" target="_blank">📅 23:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133904">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a7d67143.mp4?token=G3ex4w4DX-IbKFAWt_zL6uGFrrbJi6J-h-jGSmb24lBRNOmMEw_bX7NjdDbEXSkleSVJKVylRUq6WlthW3HkT1X8qwr99ou3HijGMvCFZKGaM1c3B-iNIqpYMXcTTa0Fxc3Wv3W1-TCpsGmO2iXtH58WuiPHQqJ0rDu1ZcBYJ4LNTgoVHm4zkiv9oqTEv-oJYHFRqyYyYnNtsXpTUfbG7oi9-OQ3giuPApgX7sQHjsM0xE1GEWk1d9fe4ibEzW4oc7fdTCKx89nnSDCt0HO8qogFMdMLadcfZ3KtB79wbL1gyF9jFUIfMxpsWIa9kFMSNbExmxo804jEZ04rNIJLmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a7d67143.mp4?token=G3ex4w4DX-IbKFAWt_zL6uGFrrbJi6J-h-jGSmb24lBRNOmMEw_bX7NjdDbEXSkleSVJKVylRUq6WlthW3HkT1X8qwr99ou3HijGMvCFZKGaM1c3B-iNIqpYMXcTTa0Fxc3Wv3W1-TCpsGmO2iXtH58WuiPHQqJ0rDu1ZcBYJ4LNTgoVHm4zkiv9oqTEv-oJYHFRqyYyYnNtsXpTUfbG7oi9-OQ3giuPApgX7sQHjsM0xE1GEWk1d9fe4ibEzW4oc7fdTCKx89nnSDCt0HO8qogFMdMLadcfZ3KtB79wbL1gyF9jFUIfMxpsWIa9kFMSNbExmxo804jEZ04rNIJLmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اوسمار: اگر بودجه کافی باشد شاید ۴۰ ۵۰ درصد پرسپولیس تغییر کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/133904" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133903">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
🔴
نظراوسمار در مور اینکه اگه باشگاه با یه سرمربی دیگه قرارداد بنده :
🔴
من یه مربی برزیلی هستم و تو برزیل ممکنه با ۳، ۴ باخت یه مربی عوض بشه
🔴
درسته ناراحت میشم چون دوست داشتم اینجا بمونم و کارم رو ادامه بدم اما شاید باشگاه فکر میکنه بودن یه مربی دیگه میتونه…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/133903" target="_blank">📅 23:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133902">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
صحبت‌های علی بازگشا، سخنگوی باشگاه پرسپولیس درباره تورنمنت ۳ جانبه و آینده همکاری با اوسمار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/133902" target="_blank">📅 23:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133901">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcfd460d83.mp4?token=if1ZMpDx-17yYgj0u-LNAj9MyGVfXei_xIl5j4EDm2ZzgxFHaDwhfniWRQa7KIEv9c8yHn_OIBWHXpSS-eBZ1sbGB0rhcb6ZQ4Dl54iol7ldV2eF_3tsMMKw5FM47IELR-dEY06S6AfgNIaiq8GBgSIRkkborH5ha7AsVEiwDOzuExnObInVdYB36SHnOFYjd5XovTeIIsDfU-eJOBI62QyiEafZYc11s0in0JMl0HV-YyQRz-M635wa4l-CZQFUCo_GZQiCx4o3uUuWrEqTVCzKZHf3W0BSHXPflMSYiCKNqwg8JHVtx5cbUmUC2FcaoF2TkcS98h_jRdZeJkxJF6zQC3fCAyfMmWLltQeBmZf5mClfM-HSJVsIWbUHH5VPqyk5tVzV1TtoZqZeZELWmt30ph_vUXzcB2CG_xJFhoNZxwvAE3iBlE9bOIDuRwY2wBwwJNPj7-fIXucneBQfGuN2zQbEiuT_Rr0LvTAPfMflaWHMDjXgZSYkcjL8IOswtMrUrE6RIxSTO3gKPxeexoikgD-wnmmXgZGkYSlJ9GYAI0Vh9yuHEWuYlkPzP0NzM4s7FAK1sbmY3ZG8B3qpqew4JJiiR_KkNcP9p1sYXwzUGBNhijrLuKDOJIvNQ9l9UI81qQolcmBiecGH4mmxiUok3sR4HAt9amGnpN7ufg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcfd460d83.mp4?token=if1ZMpDx-17yYgj0u-LNAj9MyGVfXei_xIl5j4EDm2ZzgxFHaDwhfniWRQa7KIEv9c8yHn_OIBWHXpSS-eBZ1sbGB0rhcb6ZQ4Dl54iol7ldV2eF_3tsMMKw5FM47IELR-dEY06S6AfgNIaiq8GBgSIRkkborH5ha7AsVEiwDOzuExnObInVdYB36SHnOFYjd5XovTeIIsDfU-eJOBI62QyiEafZYc11s0in0JMl0HV-YyQRz-M635wa4l-CZQFUCo_GZQiCx4o3uUuWrEqTVCzKZHf3W0BSHXPflMSYiCKNqwg8JHVtx5cbUmUC2FcaoF2TkcS98h_jRdZeJkxJF6zQC3fCAyfMmWLltQeBmZf5mClfM-HSJVsIWbUHH5VPqyk5tVzV1TtoZqZeZELWmt30ph_vUXzcB2CG_xJFhoNZxwvAE3iBlE9bOIDuRwY2wBwwJNPj7-fIXucneBQfGuN2zQbEiuT_Rr0LvTAPfMflaWHMDjXgZSYkcjL8IOswtMrUrE6RIxSTO3gKPxeexoikgD-wnmmXgZGkYSlJ9GYAI0Vh9yuHEWuYlkPzP0NzM4s7FAK1sbmY3ZG8B3qpqew4JJiiR_KkNcP9p1sYXwzUGBNhijrLuKDOJIvNQ9l9UI81qQolcmBiecGH4mmxiUok3sR4HAt9amGnpN7ufg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
مهدی تارتار سرمربی گل گهر سیرجان:
🔴
برای برگزاری تورنمنت سه جانبه اگر باشگاه و فدراسیون فوتبال تصمیم به برگزاری بگیرند ما هم تمکین می کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/133901" target="_blank">📅 23:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133900">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac325be43e.mp4?token=GaVbVjkwznwdZJop1MJI9rbBmUNeAImRxsAlIHNmZu-c6_Q1a9KTMS6RbjTXbZFomiUAioJOIsrWLKozSuRyVKE58Q_GnSA-hZwFWKAHA79KsCbxEqfz7msuTtGIi1Okm4CmgxTt3Oj1mhTuAszGTpRVtqVMicnVr4TwOWrapylQouyJlzH0KxDugBTXcKOa-GY_fS7uVFWDSdStlgGtXHvcI8eUP4AhvNpOqQSbXy0l_3-Ur2o4UalIXSr9xcN5rnja6a-Nshy0iGSHSMi9jSFPwB2REpmHhLi_tVyJHHiLMkMmVsDBfkdxIOupSTcmqjbDu6T6g3R4TPu0gXIcr4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac325be43e.mp4?token=GaVbVjkwznwdZJop1MJI9rbBmUNeAImRxsAlIHNmZu-c6_Q1a9KTMS6RbjTXbZFomiUAioJOIsrWLKozSuRyVKE58Q_GnSA-hZwFWKAHA79KsCbxEqfz7msuTtGIi1Okm4CmgxTt3Oj1mhTuAszGTpRVtqVMicnVr4TwOWrapylQouyJlzH0KxDugBTXcKOa-GY_fS7uVFWDSdStlgGtXHvcI8eUP4AhvNpOqQSbXy0l_3-Ur2o4UalIXSr9xcN5rnja6a-Nshy0iGSHSMi9jSFPwB2REpmHhLi_tVyJHHiLMkMmVsDBfkdxIOupSTcmqjbDu6T6g3R4TPu0gXIcr4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اخباری سرمربی چادرملو اردکان: ما از فردا تمرین می کنیم که پنجم با پرسپولیس بازی کنیم
🔴
چیزی به ما برای بازی با پرسپولیس ابلاغ نشده است اما مدیرعامل از ما خواسته است که از فردا تمرینات خودمان را شروع کنیم/ مجبور هستیم که رای را تمکین کنیم و بازی کنیم/ به بازیکنان گفته ایم از فردا تمرینات آغاز می شود تا پنجم تیر مقابل پرسپولیس بازی کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/133900" target="_blank">📅 23:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133899">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c26a7662b.mp4?token=bYcBy_h18OQG2vvxXk6Sj2v_YdEE8kDNMTNHTQ0W2SlpQbCbXJMuun0-NhzL3wTL8Ca8EUN59zRhRqqSsFYV5Q982t4sMIopLcjxsQ3XLp6pEiFuecHnxc7EJI2uw8JYayAT36RpthJ4wLyJTdW61doZNof1mhmx_z7iTrYWBZNJLJoLryE2s5bvp1KM-Dq34rD7fYGAY0QIndigjGSpsFKt2iHbWdCwI_X8dQTSkJ4qrS1Y0LC5EhSRZ_fJO3GDxXV6xZxHo8uipmBOTTJ5unTWvSbIlKFY6mVkzw9LnwsjqLLuG9ke24W1FG5rvfo0NY-0XUCGYgWqcJmT71YNvTH-nvq_ZCvLkqK78Gnq1he3YaOqnoImWRaWONRlySMdl07QfGVixXLdMLx6MVAqDnh7xnX76WFw4UNEB3ZFY7S3mkfIcSKR0ikYa15X3Q0XDfjIsP2kaBxph7gCL6qyEnq0FaG_nz6En3eFa9_A_PV7lmCn4mpGwR0dFswKievUjmEVl2Rgo7jGqptZ5yyeKaWXLmlbNRHfTZR2Goj-2vOT-_0AX8NvjE9aUNyy4a9LdsdZpc1mGxZHhpDNHME0SwCVxZ_CVcV14-2BNSErxiPZiPIiEC0k1rsIOMhjh8fo8IikAe_11jLizCAve9Xcoa6futqsRQweHKyxvDz1RVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c26a7662b.mp4?token=bYcBy_h18OQG2vvxXk6Sj2v_YdEE8kDNMTNHTQ0W2SlpQbCbXJMuun0-NhzL3wTL8Ca8EUN59zRhRqqSsFYV5Q982t4sMIopLcjxsQ3XLp6pEiFuecHnxc7EJI2uw8JYayAT36RpthJ4wLyJTdW61doZNof1mhmx_z7iTrYWBZNJLJoLryE2s5bvp1KM-Dq34rD7fYGAY0QIndigjGSpsFKt2iHbWdCwI_X8dQTSkJ4qrS1Y0LC5EhSRZ_fJO3GDxXV6xZxHo8uipmBOTTJ5unTWvSbIlKFY6mVkzw9LnwsjqLLuG9ke24W1FG5rvfo0NY-0XUCGYgWqcJmT71YNvTH-nvq_ZCvLkqK78Gnq1he3YaOqnoImWRaWONRlySMdl07QfGVixXLdMLx6MVAqDnh7xnX76WFw4UNEB3ZFY7S3mkfIcSKR0ikYa15X3Q0XDfjIsP2kaBxph7gCL6qyEnq0FaG_nz6En3eFa9_A_PV7lmCn4mpGwR0dFswKievUjmEVl2Rgo7jGqptZ5yyeKaWXLmlbNRHfTZR2Goj-2vOT-_0AX8NvjE9aUNyy4a9LdsdZpc1mGxZHhpDNHME0SwCVxZ_CVcV14-2BNSErxiPZiPIiEC0k1rsIOMhjh8fo8IikAe_11jLizCAve9Xcoa6futqsRQweHKyxvDz1RVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت‌های علی بازگشا، سخنگوی باشگاه پرسپولیس درباره تورنمنت ۳ جانبه و آینده همکاری با اوسمار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133899" target="_blank">📅 23:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133898">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎥
خبر میثاقی برای تصمیم درباره نماینده سوم آسیا: تورنمنت سه جانبه بین گل گهر، چادرملو و پرسپولیس برگزار می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/133898" target="_blank">📅 22:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133897">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
بابایی مدیرعامل چادرملو: پرسپولیس با گل‌گهر بازی کند، نه با ما
🔴
اگر رأی کمیته استیناف به سود ما صادر نشود، باید حکم دستور موقت بگیریم و پرونده را در دادگاه حکمیت ورزش (CAS) دنبال کنیم.
🔴
به این مدل تورنمنت‌ها اعتراض داریم، اما راه آسیایی شدن همین است…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/133897" target="_blank">📅 22:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133896">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
این فهم و شعور رو میشه تو امثال آدم های عین اوسمار میشه پیدا کرد .بی ادعا و با درک بالا صحبت میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/133896" target="_blank">📅 22:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133895">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
این فهم و شعور رو میشه تو امثال آدم های عین اوسمار میشه پیدا کرد .بی ادعا و با درک بالا صحبت میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/133895" target="_blank">📅 22:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133894">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
🔴
نظراوسمار در مور اینکه اگه باشگاه با یه سرمربی دیگه قرارداد بنده :
🔴
من یه مربی برزیلی هستم و تو برزیل ممکنه با ۳، ۴ باخت یه مربی عوض بشه
🔴
درسته ناراحت میشم چون دوست داشتم اینجا بمونم و کارم رو ادامه بدم اما شاید باشگاه فکر میکنه بودن یه مربی دیگه میتونه…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/133894" target="_blank">📅 22:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133893">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
✅
تایید شد
🚨
میثاقی: پرسپولیس 5 تیر به مصاف چادرملو خواهد رفت و برنده این بازی 9 تیر با گل گهر مسابقه خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/133893" target="_blank">📅 21:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133892">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
در صورت برگزاری مسابقه، این دو دیدار در تاریخ 5 و 9 تیر برگزار خواهد شد.و بدون تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/133892" target="_blank">📅 21:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133891">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز | #افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» امروز پس از شایعات و هویاهو های روز های اخیر ایجنت اوسمار ویرا در اقدامی غیر قانونی نامه باشگاه پرسپولیس به اوسمار رو در اختیار خبرگزاری فرهیختگان قرار دادن که موجب بروز برخی شایعات بی اساس و نادرست…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/133891" target="_blank">📅 21:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133890">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
🔴
نظراوسمار در مور اینکه اگه باشگاه با یه سرمربی دیگه قرارداد بنده :
🔴
من یه مربی برزیلی هستم و تو برزیل ممکنه با ۳، ۴ باخت یه مربی عوض بشه
🔴
درسته ناراحت میشم چون دوست داشتم اینجا بمونم و کارم رو ادامه بدم اما شاید باشگاه فکر میکنه بودن یه مربی دیگه میتونه برای پرسپولیس بهتر باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/133890" target="_blank">📅 21:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133888">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
اوسمار : امروز من سرمربی پرسپولیس هستم تا روزی که باشگاه تصمیم بگیره و بخواد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/133888" target="_blank">📅 21:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133887">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
اوسمار : من با آقای حدادی جلسه داشتم و گفتم که علاقه دارم در اینجا بمونم و این پروژه رو با هم ادامه بدیم. نه از فقط از نظر مالی و هم برای باشگاه و هم برای هوادارا انعطاف پذیری خوبی داشتم. اگه پرسپولیس بخواد میتونیم به یه نتیجه خوبی برسیم.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/133887" target="_blank">📅 21:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133886">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
عادل : خودت حتما تو محافل و رسانه ها این چند روز حتما شنیدی که اوسمار تمدید نمیکنه و از پرسپولیس جدا میشه اوضاع قراردادت چطوره؟
🔴
اوسمار : من هنوز با پرسپولیس قرارداد دارم درسته تاریخ نداره ولی قرارداد برای یک فصله. یک آپشنی برای تمدید قرارداد داشتم در مورد…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/133886" target="_blank">📅 21:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133885">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
اوسمار : لحظات سختی بود برای تصمیم برگشتن به ایران، در مورد امنیت داریم صحبت میکنیم چون خانواده مون ما رو دوست دارن و خیلی سخته استرس رو تحمل کنن که ما اینجا باشیم
❌
شاید راجع به فوتبال صحبت کردن برای مردم خیلی مهم نباشه، خیلی چیزای مهم تری از فوتبال هستن…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/133885" target="_blank">📅 21:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133884">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
نظر اوسمار درباره عملکرد دو شاگردش در بازی ایران - نیوزیلند/ کاش علیپور بیشتر در محوطه جریمه می‌ماند
❌
اوسمار : به نظر من میلاد محمدی میتونست بهتر جلوی نیوزیلند بازی کنه چون پتانسیلش رو داره. علی علیپور شاید اگه بیشتر تو محوطه جریمه میموند بیشتر میتونست روی…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/133884" target="_blank">📅 21:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133883">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2cbc17f2f.mp4?token=esofi2GClfCxxuyU1I7TNq-cwrPTXqLCIXytjLJ40L0er3KfD51rEq5BgNrP04JqnhGG3HGzXbEQYUdNJzwywfQhGhf0c8GJiupq8KJa8MIGwccWEP_fEGxYOERCrYp-y0AN5v8MuoDeOTYUplebMebzfS6hVitSMhx1i6qVwocW46ui_FNbelDDAgXPyDf7CV8imlHR2MlfU34sLS0HucM-rTqrzezPGIzY_WWynVdXsc50AWRtMUvCoJxXnryQ-eIetBJ7GeAdhG8DgKBB9T8X7Tkzq1cnBMQuehGQG7mhHFBBLDy0_QvFDSbrt8PjBOdBNMru28_NRWOWJAWpBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2cbc17f2f.mp4?token=esofi2GClfCxxuyU1I7TNq-cwrPTXqLCIXytjLJ40L0er3KfD51rEq5BgNrP04JqnhGG3HGzXbEQYUdNJzwywfQhGhf0c8GJiupq8KJa8MIGwccWEP_fEGxYOERCrYp-y0AN5v8MuoDeOTYUplebMebzfS6hVitSMhx1i6qVwocW46ui_FNbelDDAgXPyDf7CV8imlHR2MlfU34sLS0HucM-rTqrzezPGIzY_WWynVdXsc50AWRtMUvCoJxXnryQ-eIetBJ7GeAdhG8DgKBB9T8X7Tkzq1cnBMQuehGQG7mhHFBBLDy0_QvFDSbrt8PjBOdBNMru28_NRWOWJAWpBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
خیلی دلم برای تیم ملی تنگ شده؛
🔴
پورعلی‌گنجی: انتظار داشتم قلعه‌نویی فراموشم نکند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/133883" target="_blank">📅 21:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133882">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26db6eea.mp4?token=Is8lhP-8lnYHD5ZfLo2dg-9cPPYNBmC7JzT75hFQq6qIU_uvK6Osuq4rx2NEYXCdUnnyn4GuQ8zLPUmhkZwb_CWRPhw2Zsawfo7j5m-zo9VWqMQN0sPCvh3YxwDVp9mtEdOv-9fGqv5I8URXXOJ1VO0EKC63BTK_CdZ9g7x9tyFT83QcBaTaOWCHTzQSBKPtPUjdBRIw9Fa8ffo21Sfr23zvYdWFTZDpKJh-m5DxkLo4mcMl70j4Ch0QdTxY9cJCaRGib8WYK_elGmYJdn4bIvDvM1GtEj05HDKDOe2GRZ_VGa-oOwKAA0Afs_fXElJvs6IGBAR9TYr-FJ_7Ekr02A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26db6eea.mp4?token=Is8lhP-8lnYHD5ZfLo2dg-9cPPYNBmC7JzT75hFQq6qIU_uvK6Osuq4rx2NEYXCdUnnyn4GuQ8zLPUmhkZwb_CWRPhw2Zsawfo7j5m-zo9VWqMQN0sPCvh3YxwDVp9mtEdOv-9fGqv5I8URXXOJ1VO0EKC63BTK_CdZ9g7x9tyFT83QcBaTaOWCHTzQSBKPtPUjdBRIw9Fa8ffo21Sfr23zvYdWFTZDpKJh-m5DxkLo4mcMl70j4Ch0QdTxY9cJCaRGib8WYK_elGmYJdn4bIvDvM1GtEj05HDKDOe2GRZ_VGa-oOwKAA0Afs_fXElJvs6IGBAR9TYr-FJ_7Ekr02A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نظر اوسمار درباره عملکرد دو شاگردش در بازی ایران - نیوزیلند/ کاش علیپور بیشتر در محوطه جریمه می‌ماند
❌
اوسمار :
به نظر من میلاد محمدی میتونست بهتر جلوی نیوزیلند بازی کنه چون پتانسیلش رو داره. علی علیپور شاید اگه بیشتر تو محوطه جریمه میموند بیشتر میتونست روی دفاع نیوزیلند فشاره بیاره اما در کل کمک کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133882" target="_blank">📅 21:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133881">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔹
سه چهار تا خبرگزاری رو حسابی امروز خوراک دادن و‌ پول پاشی کردن، بلاخره وقتی ۱۲۰ هزار دلار کمیسیون گرفتید الان باید خرج کنید دیگه
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133881" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133880">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUV1_f3mtUBRk1Um1IW6c8AwakVTHAa9253i3QKqyIvbuCTZlcXDHV0yQwg08YvjR8fB_LIjpCCjw2nvR8o-27bnNV0FpwgsLApr1cKqTtw_REOCPy8TvE3Thh0t9r9zoIJ3inQMPlZFiu4M03KB1mYo6OeFBXWqTKdUT7w4QLktPW2L5tTWdEYnLjgZpKgSKUA5O5L3no_0n8WBYUeJ8YrF7J7nckNKtOEoOS-jsHyGt-wIx0zvCMVJt26YjmK8Ny1BknB49LNTp4yy985fPV0USNxnfVs1NUqyKgahXKZnu1sER2eiI4m4WOC3UTJScG02akkI8N4RrUimQNYXhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بازی‌های جذاب و هیجان‌انگیز امشب جام‌جهانی رو با بونوس ویژه وینکوبت پیش‌بینی کن.
🎁
بونوس ویژه جام‌جهانی
6⃣
2⃣
0⃣
2⃣
همراه با وینکوبت ادامه دارد!
🎁
🔣
5⃣
1⃣
بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه وینکوبت فقط تا دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/133880" target="_blank">📅 21:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133879">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea592625ac.mp4?token=VJ2nlNgTm7k_s6o2SuDbEStkJxdCDPPuRZMUumqBQtMlWS4Xbi-bnqh3tKbodIcAUB0znOhDe_h_mMuSyrOOUNrputLcYYJ2uCIx1sneVgfIyiqMKgxxBfZFkDRdc5V3ydzm7jF0rBl3nSMIdWJhonFZSwHYBX71q52rDN6zI4iGunBiK9HfzJ60_OnF1_52gn9oq24bcwP1xgG-uHNDFeiZKYQg1zXCCgR3zVF87Ny6ATL2sQ8eq-Pb-Dramyu5ShndmXFqs9t1K25eYL24o3XgRuS_-0q8YC1ZTzRsxmJ0s-avxKFqSv4QJQSMXQ2q_CyZZ88l6Dxwk7sOzJoY7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea592625ac.mp4?token=VJ2nlNgTm7k_s6o2SuDbEStkJxdCDPPuRZMUumqBQtMlWS4Xbi-bnqh3tKbodIcAUB0znOhDe_h_mMuSyrOOUNrputLcYYJ2uCIx1sneVgfIyiqMKgxxBfZFkDRdc5V3ydzm7jF0rBl3nSMIdWJhonFZSwHYBX71q52rDN6zI4iGunBiK9HfzJ60_OnF1_52gn9oq24bcwP1xgG-uHNDFeiZKYQg1zXCCgR3zVF87Ny6ATL2sQ8eq-Pb-Dramyu5ShndmXFqs9t1K25eYL24o3XgRuS_-0q8YC1ZTzRsxmJ0s-avxKFqSv4QJQSMXQ2q_CyZZ88l6Dxwk7sOzJoY7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوسمار مهمان برنامه عادل فردوسی پور شده و چند دقیقه دیگه میاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/133879" target="_blank">📅 21:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133878">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823e8b1726.mp4?token=EuVnqeRr5YrvX7fImF3gSrTqowBQ-q6SrSytBFDJFmJM0NP-Tqei8QMJtd2jKWNLqudl_gZOPoMKGx6RuZKVDdQbg1FLbBoybKgC3B6DEUfoy-a6mldvXx2b0IWmSHM9bVcm1XWYni6Ld94Se-ZNo5WRjXS-uvszM3aqo32LlMstGHk0HT86TyZFfdvrY3ThpaMYUc8nYbp4PLBgSLx9gofAp-r5HSDBXFIDqKNQ3-ZMz0zlhxCsVJJxSEacei7aAPjnxOmmo_2CWxwtLyhLLooTxRXre4cV8pKG6nU_Pq7L3K7A3HQawdVUNkJloqInniToe7YNh5_WefFIF3S-LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823e8b1726.mp4?token=EuVnqeRr5YrvX7fImF3gSrTqowBQ-q6SrSytBFDJFmJM0NP-Tqei8QMJtd2jKWNLqudl_gZOPoMKGx6RuZKVDdQbg1FLbBoybKgC3B6DEUfoy-a6mldvXx2b0IWmSHM9bVcm1XWYni6Ld94Se-ZNo5WRjXS-uvszM3aqo32LlMstGHk0HT86TyZFfdvrY3ThpaMYUc8nYbp4PLBgSLx9gofAp-r5HSDBXFIDqKNQ3-ZMz0zlhxCsVJJxSEacei7aAPjnxOmmo_2CWxwtLyhLLooTxRXre4cV8pKG6nU_Pq7L3K7A3HQawdVUNkJloqInniToe7YNh5_WefFIF3S-LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
مرتضی فنونی‌زاده: پرسپولیس چوب ایجنت های بی کیفیت را خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/133878" target="_blank">📅 20:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133877">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
آنا: اسکوچیچ به زودی برای قرارداد با پرسپولیس به ایران می‌آید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/133877" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133876">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/133876" target="_blank">📅 20:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133875">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز | #افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» امروز پس از شایعات و هویاهو های روز های اخیر ایجنت اوسمار ویرا در اقدامی غیر قانونی نامه باشگاه پرسپولیس به اوسمار رو در اختیار خبرگزاری فرهیختگان قرار دادن که موجب بروز برخی شایعات بی اساس و نادرست…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/133875" target="_blank">📅 20:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133874">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
|
#افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» امروز پس از شایعات و هویاهو های روز های اخیر ایجنت اوسمار ویرا در اقدامی غیر قانونی نامه باشگاه پرسپولیس به اوسمار رو در اختیار خبرگزاری فرهیختگان قرار دادن که موجب بروز برخی شایعات بی اساس و نادرست شد.
🔹
طبق قرارداد فی مابین اوسمارو باشگاه پرسپولیس،مدیرعامل باشگاه برای فعال سازی بند تمدید قرارداد اوسمار باید تا تاریخ ۱۰ اردیبهشت ماه نامه میزده و اوسمار هم تایید میکرده، این نامه در تاریخ ۲۶ اردیبهشت ماه ارسال شده تا تعهدی برای باشگاه ایجاد نشه….
🔹
تا اینجا همه چیز گویای این است که فرافکنی و جوسازی ها بدون ادله کافی و مستندات کامل به چه هدفی منتشر شده.
🔹
حالا قضیه از جایی جالب میشود که اوسمار ویرا در جواب نامه باشگاه پرسپولیس اعلام میکند «اکنون زمان مناسبی برای تمدید قرارداد و مذاکره نیست و به صورت مستقیم اشاره به جنگ میکند»و از تمدید و مذاکره بر سر قرارداد سر باز میزند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/133874" target="_blank">📅 20:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133872">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚠️
ایجنت های اوسمار چه کونی از خودشون دارن پاره میکنن دست پا های اخرشونو میزنن بلکه اوسمار قراردادش تمدید بشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/133872" target="_blank">📅 20:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133871">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚠️
ایجنت های اوسمار چه کونی از خودشون دارن پاره میکنن دست پا های اخرشونو میزنن بلکه اوسمار قراردادش تمدید بشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/133871" target="_blank">📅 20:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133870">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
🚨
🚨
اسکوچیچ سرمربی پرسپولیس شد/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/133870" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133869">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
برانکو ایوانکوویچ: مذاکره باشگاه پرسپولیس و اسکوچیچ؟ بله شنیده‌ام. اسکوچیچ انتخاب خوبی است و برای او در پرسپولیس آرزوی موفقیت می کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/133869" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133868">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
فوتبالی: اوسمار حاضر شده تخفیف 400 هزار دلاری بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/133868" target="_blank">📅 18:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133867">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
🔴
#فوری
❗️
قدوسی : اوسمار برای پذیرش این پیشنهاد شرط گذاشته است که در صورت بروز جنگ، حق فسخ داشته باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/133867" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133866">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⛔️
فووووووووری
🚨
تا 72 ساعت دیگر تکلیف نیمکت پرسپولیس مشخص خواهد شد/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/133866" target="_blank">📅 16:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133865">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇵🇱
الهیار صیادمنش در تست های پزشکی لخ پوزنان لهستان شرکت کرد تا به زودی هم تیمی علی قلی‌زاده شود!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/133865" target="_blank">📅 16:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133864">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
🔴
اسکوچیچ برای باشگاه پرسپولیس شرط گذاشته و گفته برای آمدن من باید آلوز را جذب کنید و باشگاه هم به همین دلیل پیگیر شرایط این بازیکن شده.آلوز بخاطر اختلافات مالی، قصد دارد از سپاهان جدا شود
✍️
خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/133864" target="_blank">📅 15:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133863">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">💢
💢
💢
#فوری
🔸
🔸
🔸
قدوسی : اوسمار درخواست باشگاه برای کاهش قرارداد را پذیرفت و قرارداد او و دستیارانش برای یک فصل از ۱.۷ میلیون دلار به ۱.۳ میلیون دلار کاهش خواهد یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/133863" target="_blank">📅 15:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133862">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">💢
💢
💢
مدیران باشگاه از اوسمار خواستن قرارداد 1.7 میلیون دلاری (قرارداد خودش و سه تا دستیارش) رو حداقل 400 الی 500 هزار دلار کم کنه تا قراردادش تمدید بشه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/133862" target="_blank">📅 15:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133861">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
مدیران پرسپولیس در یک هفته اخیر مذاکرات فشرده‌ای با باشگاه روبین کازان انجام دادند و در نهایت با این باشگاه بر سر انتقال قرضی کسری طاهری به توافق رسیدند.
🔴
اگر اتفاق خاصی رخ ندهد، طاهری به زودی با حضور در باشگاه پرسپولیس قراردادش را امضا خواهد کرد./تسنیم…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/133861" target="_blank">📅 15:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133860">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⬜️
⬜️
⬜️
⬜️
فووووووووووووری
🚨
باشگاه پرسپولیس در اردیبهشت ماه قرارداد اوسمار رو رسماً تمدید کرده و این قرارداد تعهدآور شده است. اما مدیران باشگاه با این وجود رفتن با اسکوچیچ صحبت کردن و اگه اوسمار شکایت کنه مدیران باشگاه پرسپولیس باید غرامت بدن/ فرهیختگان
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/133860" target="_blank">📅 13:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133859">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVw_UpEkS8jYtukwVR4pXv2MeMAYKpNVeJEM4nmEIo1ocF8sXPoMKUs8r7BFJiPNF6YKBp43GViITqW3SzssHxc75tNAF1rUQ-ZXn3hUa0kp3Dftal0RcB6Y1fJ4uuDHhmtabD0grnuYjv_5EuGa0DXdtYJpCJTcnWssTESAwef5-yDCI9Ahbrjh6KcSflNeIGnUBQh7oJPWPY2bgHZA-uc54mY_c47iduumP_3DE-CZKnLPx_5WTYKZ-zjporm_GrSGWVa0Sz4YE2LGNBrUICbxSH33WDl-1rk764q_DtQv2smhF-W-Wdb_E8VwQyvNchfAnskt0LKogBABhmgklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
خداداد عزیزی که این روزها ارتباط نزدیکی با مدیران سهام‌دار عمده باشگاه پرسپولیس، دارد به مسئولان این مجموعه اعلام کرده به دلیل همکاری موفق با اسکوچیچ در تراکتور، رابطه بسیار خوبی با این مربی دارد و در صورت نهایی‌شدن تصمیم مدیران باشگاه، می‌تواند زمینه حضور او در ایران و نشستن روی نیمکت پرسپولیس را فراهم کند
.
✍️
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/133859" target="_blank">📅 13:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133858">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
✅
✅
اسکوچیچ خواهان حضور کریم باقری و 3 دستیار اروپایی شده/خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/133858" target="_blank">📅 13:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133857">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEcGzN0JlE3G8NxaHE6MLAc98G0STFTJ68bj6FdhZAgEfilfr_LRpf2_jqDah9-nYnIqqqLPygozTyz2PFE5VvVVCGmVrauxrFUuk1yNLKRTWPJhRxJV1a-_-lT3T3INWACkVcnrpBe1DSxX9s77HddOLk9P8SKsMSH7haqKqu6D45n5GTZw07i_0OlLbjS3E-XkKBq4f8mBEt7lvNWgFUF-njqQr-ytFu1Uao0Skeu9sTRud10A644Z_5Ye0F1OaaVuwiSwnJ0HcOUmcGFoSwQXHhzNwEbqk8y-wY3RIXu0qcwS4EGL3H02GR1d8lPlv2GzXhlKkRrvhJICIN_Ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این بار از همیشه جدی تر
👀
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/133857" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133856">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbVxcwIlwgtr-rEQtpMk0Bh0jde41cewMbeFOAaOhElplWsSLfxDbCE-fAVbEju2EPFQ139uGOohH7aMPYqhcR7URLcqDKW7y7TVrF-Ie9uTXIJyW5KxDYUMZ17GmDs0pcqSlqXerK7H3e1e7IFW3yltU48s-P_WrLr6anGRnHWEvx4w5mj5PmaegTWL60auBcmvw7doTBKCqKl6YIWowib5uPjOsLINN7Y8aqHB4gU-vi61z8qTHupJWnop7t4z0NCtIkym3KEcK82XtokObl9lwz4ldFinP6v_dMUk9CBK3Wx-rSNfsUZgYaNBjLmL8hY5W51DK7uq6DPqtub0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حسن یزدانی با کسب دومین پیروزی خودش از 3 مسابقه مقابل امیرعلی اذرپیرا ملی‌پوش ایران در وزن 97 کیلوگرم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/133856" target="_blank">📅 13:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133855">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
جلسه مديرعامل و سرمربی پرسپولیس برگزار شد
🟦
🟦
در این جلسه که محسن خلیلی نیز حضور داشت، در خصوص قرارداد و مباحث تیم صحبت شد. قرار شد طی دو سه روز آتی، باشگاه پرسپولیس نظر خود را به اوسمار اعلام کند. در خصوص تمدید قرارداد، مسائلی است که حدادی قرار شده آن‌ها…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/133855" target="_blank">📅 12:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133854">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
پرسپولیس میخواد برای جذب احمد نور به کلبا نامه بزنه/فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/133854" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133853">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nrxp-OUxS492bQgs-icqKIdGKBcWIW8XHTowXVQKjdGOXOtqSSDb2UfUdjfkCEw3v01t1qhAZ0otzuhMqM9eHuPcgvkMeCbG_DeJAFk6GEtc1cs-BlunIN2njvSEqeCDLRS1MIvIWt1gNNbn-TxqixPtLTInMZVfOVCoNwXYkHfwDTmOgXhtN3RupbTxiw1R8x3omDcX0bCg3n7F1KFsuB_uMh8jdehyVyZ7znxitDL-yDC52MTFJDYc4VUt457gjIsmZAOl4wMYaEhD-89nAn9WEierY8aY4Xl_M98zy3p0U8e1L0qTjGki0VyjXcRAWdJ_RhkqtHcyxNQb3ywc7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⛔️
فووووووووری
🚨
تا 72 ساعت دیگر تکلیف نیمکت پرسپولیس مشخص خواهد شد/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/133853" target="_blank">📅 12:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133852">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyLyN4Bsa4jFRNYC2HhPY85NxgrGmr3hUv-4Z8JcvaP_vUakMx-NZDksQQbwB4tdczz4d7dh4xHhgq0clRXWukbwzkZP2ZgYg6wsS41OI1jfwotDGQnVGUmnIKODc3AGFVb19TyhQufxECph0BU__w2PrTTFFWn8k2B4tNlWfwBX51gXipK6r0WSIszzmFo-C-hRzcX8jwY_pM0OCR5PN0tTi8bRmPZQ1jS1cyjymt0fToMot5vYEUQ1hxbQ7kVyEXXWHCIxDumZWorwqu8jsUHbw4obVPEaBiQ1v8gCSMKL9N7GJ6mLuTXIYGpccY_hc9n56lhGVkISK_HdrJhHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فدراسیون فوتبال رسماً اعلام کرد تصاویر منتسب به محمد محبی جعلیه.
🟡
فدراسیون فوتبال: «در پی انتشار تصاویری منتسب به محمد محبی در برخی شبکه‌های اجتماعی، به اطلاع می‌رساند تصاویر مذکور کاملاً جعلی بوده و با استفاده از ابزارهای هوش مصنوعی و تکنیک‌های دستکاری دیجیتال تولید شده‌اند. این تصاویر هیچ‌گونه ارتباطی با محمد محبی نداشته و انتساب آنها به این بازیکن ملی‌پوش کاملاً نادرست است.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/133852" target="_blank">📅 12:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133851">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
پرسپولیس برای جذب قرضی طاهری به توافق نهایی رسید/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/133851" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
