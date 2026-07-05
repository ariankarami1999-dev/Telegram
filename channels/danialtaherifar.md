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
<img src="https://cdn4.telesco.pe/file/b1nMRV5r8tXh8ehlKhEoSsS-y5dldVXZ1WGfe7cdItmu3I-bLk9aTAFfj9jZ0Uch3Ge72jVa1xa24DlFRFwixFRZxD0KXJWsfs2ldRnVmTleFLgDtx3653-w3ITJ2rJUrDZk0UPU_543LIe8fBN8t9LAumu5bIqp79ahMWLXj0FBhZ2coSPVLd1Ad-t-UgvIKMUuN9-tLjV0QyptTbfdXf3eRdjQk7f23iUwOtUo8P1FA8t1QlTH9D92RQ1_jlpRkdcDWrEgMvLhW3RbJh2P0_ayXyOdkw2i2tonBxup2ITVYzoPspNS98_Aj9tj1JkaK81h7CUcaFw3bzrp8KBh1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 21:30:48</div>
<hr>

<div class="tg-post" id="msg-940">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگر دوست داشتید MiMo AI را امتحان کنید، با لینک دعوت من ثبت‌نام کنید.
😊
🎁
هر دو نفر:
✅
۲ دلار اعتبار رایگان API
✅
ده درصد تخفیف اولین پلن
🔗
https://platform.xiaomimimo.com?ref=WLBKSK
ممنون از حمایتتون
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 126 · <a href="https://t.me/danialtaherifar/940" target="_blank">📅 16:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 362 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAyGsqwbpokvrjoakSU4xARjQ0TLcFvc20umYpP36eB_VFBEFdEJifP0-TcPAhR63t-5OKpiKxpdh7670pXjRbhMT3PCgMnooTvliYoOzRlgPYDPBGFH57kuXgOF6P1NHEQa5WYDli7ZRiEsy-4JNDfBO5H8bWpo6fd-SXwlWGDxNlAjVXW-RDin7AepRnG4Z4JbQNSbC24vGqvgcmbxDrMiQled8O_hqsut-rqGROhKVcV4vP63IGYORYj-Z3J5innuvPGXDJ7-d7KHK587x32n0lcvDDOoP_xjLv9o80dN6bwQhgmj7BuvynRVS-_elmnAgUjcIFdG6piIK4nhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 569 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 722 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 794 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=YuTLntbzHCeK4-QDBWr3rP-TGZs_8Q6rtW6jg-5nbM9jHJYjkbuN5YI_SvIzBTDkxB2NJdo_MXZQJHA1Gt98QFrjtoweQFXgRAdgigpRNV_68lC6r5_tLQTkEQoh0s86Kx0OMJ-Lcn93JYvfpllOCqNttfHpb6qB-AiJvZSBpG5b_UpJTQS4Pn_aqV9wEBydzkdRqueQmbw1G30tzqMM6-9zoGxNjg3BsuIISaXYXLNuBS_usqCR_Uh-S1TmhxWHKOw3nc99o-QsQx1rOqnSrLH8t-9b5xP6oSl1UYU3_7jmyPAaPHncwYmzeqdFQqZorL7Y87dT5mX9s2dXoIl9Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=YuTLntbzHCeK4-QDBWr3rP-TGZs_8Q6rtW6jg-5nbM9jHJYjkbuN5YI_SvIzBTDkxB2NJdo_MXZQJHA1Gt98QFrjtoweQFXgRAdgigpRNV_68lC6r5_tLQTkEQoh0s86Kx0OMJ-Lcn93JYvfpllOCqNttfHpb6qB-AiJvZSBpG5b_UpJTQS4Pn_aqV9wEBydzkdRqueQmbw1G30tzqMM6-9zoGxNjg3BsuIISaXYXLNuBS_usqCR_Uh-S1TmhxWHKOw3nc99o-QsQx1rOqnSrLH8t-9b5xP6oSl1UYU3_7jmyPAaPHncwYmzeqdFQqZorL7Y87dT5mX9s2dXoIl9Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnEpiMQttDPAxjkFQnIwP0fW93fsH_36GzrKKe2n1Athvi2zCq8X4BkUg8PoeiJ5FnXtwWdxWJ-KOQJF5HBPvlBJvYhN1jYsRDIVH194P0pvZu0lMcAixZ2c3HT0vIvCPlJ6QMtUOgvUcmb7UOL3vwqEg8Xd2Ww3pOv5_1scQroR9eYbNDh3PSFbbp_ZbYT8K7De4ZteLylNK9fGxkf6gxvzBy9K4RgrUmde0Xc1eQ4ZcS1_A2KbGcbbeQazqxR8TFAzVakswULZX3cIgmf9IIWm_4_IXlBzkq19u7wLZhvx9kMSUFZoGW6cFjXnzwHbM8YWJ5JgJXv7YZNLva9hBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 647 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 728 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXkFmLqfiAnfDcExfs-21_XbhKlgdzAbmZfS_8l6RI4yyRXzsB2DrcfOBzwYyWmummCJltO7Ud-_1tAoMnC8jfkzMfhmpyBYWQTs_ehNJ5h3MIFE5GcMbYO08BF2fzGNqiUlFUtBOdQdiXU5TW8NbT1bMeLGlw5ttc44LbvVa8YGgl598is799wtwShRCzQiVvlKvdje2oc8Hmpf__R0_CMj-iEr1PmU1yXsgrpGZut_jBoGG0cOUhKp49jOa5-DY8ZuDxJqMMcKQHayNnjLkVPL2EoE_0tk7x_Y5KHUvJNuqYNtGPAhnekc_N9BWkYNpVyA39Wk3iZ7yWDm80yO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPE9CBWC0SwbE7CYRM2mlwmGDt83tj7yS2YtseegqRrNZHsvlLZy4MjvLhFH3f-M3RssAT1HnqVLa0HZG_GuDYcmPhgobEBOjPy47xYN3w0NWwY4rqHdt_ipoaALW7mZP9JTiXF-yRylgJ4liEYsUYt5PVNpTDVNKI_u7ZBQ7xAt5m95wUgWL_tXgLzW27baTZtC21JMTyLlhLMwMaVvwesYyyaT3hjxoFt0HhB9_7FhC87tG_4bbbWw0n5iT6flHymGxNKmbbmOHjvsDk5YEetf8vvNCIZM0miAkDoxw_qA8weT6dDtBLJZ6XWAAkQnqKxLRCMRjq8rXw7fDtiEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg0czVheKPdyU18dI6_w9-TOeSfkhfyrXj6jZ9zLGQQ9DqmSC8TvD5vr07n4xGoAKIbR1njdT_8MiS24lWoGFZg_rrueVoKMZHuU88sQpfXxZlDmSD7XVy0uqYPq2CIf9zHzHFsVDnnjRH-0rVKhVNXwrA6p6w8rebGGQ-Q9cWK4IjP0atL-BOD30vSRSt-BgC5rlQvoYMmq3zYrYmO4y7Ma2QbJXhGbfP65HEhPI9J_yBxf6g0cHDJWtL5G1I-ZQUqDuQ2jTv7nAQoTEBSA_PzVN4gXEx7DeO7wca0fIK00DEdaGujVV1tV8Ea-OqcfJnfBvzSk0jGfNgmV__PkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezPAGKpbON1v1vzcbGxE-cWjGfXmT511E67sjJIsCDdKuCkHhuIgIaEzrRpWfoE3o4Mf1or_ESTEGcxj4ZdZOZQ15irYt7TbEDJSbUH_lnOa-4tf5_L0Srb5IC8EFbkfHEN1153YgoJ-DfeGPRJPMaZmKrmgcHFJKtCZDSNr3HdUCzq1f3mUMcHTRr2NRgM43PrgOEHkzZr0V3kPL6AAwG4YmgRvd_APhFctruARUkwtIkOgJ1a3aKfhMDKl12WrL7o6L1CmQQCXa0zX48xy3uNJbiohafMlhIInaFwZi2cP-f4rb5H07UTzKq8frkBWBmbtpuwkhkjoS9sTnGM7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLF2DRoBTU-ZUezstkIKfsX2QG5jQ38r1W-hFsCdYy2rSs8PKgMImRNWNc1be9an_7bRHcTiz7VR286O3UOhTWj-ykR55x9um9wAzRG-5NpGGFod6zx2UaQ9FSTzkmlxvo8glWaXxbhBYgvciHRMoUsV77Qgg4yrUeaXTqPCXkSUfXefhoTy9L6TGK7rCievUBG63QegDnP6eV1IYChcTpMvHkIPlfBj_RNFPGRlMBGNCrNjXw4OPvm9HS9eNA2_JzBR1gzT8AchwInRisCt6FFWiwbDE3J7Aq-coaRk8gKvCAv8UpN1buoLlq6kPXC2ipoq17hfdTOgw9rebbg_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 952 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 912 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Suy-IK0s8e91V7xcX9LZNQUWvgikgUz0-zjwcJtOWLzX1jXlniJfui-aLFcdtazizMkPzvRShloVd8tPXFR5ewqG-DWHaGugFDsiOQmvEWx0BPC4A_uuMEMOJeyu7d1RllvymE54FmZQaXOcK6VH6blHgncGHU1ENgGEx2IUDeTtLxZ0Mq_kN_6m4ueQjzUCwv5YItC_GvOz7jau986k5Nec_GIOBv9oJXQUuCLEiXyTwgEtAitW9oRuFqwuWqEYJzbfZZCHKWIR3KKxzy3wcQwoUgZhwPZ0VGneexCQv1MU7rXB2NH6NNCksLzuTjftOnY3CVrRxHL48RC-4RwSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ennu4eNQNet9Fw40Q1ZsyyUv7Q4O68Z9gbouUmBvOi0bbMalJXWiClJhq99mW906H24DHfEnwgGrtG-BCnYOQ7_cJmw7Lxuz50h9MSGAQCqvo42on-JJazcYd7tRbtyTRnOcJ5mU-Kd9gUsZpfolkbxBFCpDoSvrv0zyQc9s3-AcqX5mEZfDUv7Tk0bS80VcKdXscLyoq5NgabW8Yl3diSs0GpgPly-POMfkuITT99pI87AakE9bNQgVFivdNJWqo54BrmF3Q2u47wAapmy6LUl8qvviNIuLb8JAShQ9i2S4e6sewHn_EJQNNwloUNvqilpm3cNAR1IEDvU6vNn-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCsilQPI-WqZCMyT8S1VrOjA0V3keig0xawUP6Fl-qXdQUZDLYkBsiR_wVi74x7N9fr7vIW1jLEpj2Kc3sH161A8J7tCBfiilf_WZ0N6mUa6p1KeX84Mg5LxlVxhFjBzm_JcZ2ruj2kH1L1fUgAClOKHRS57UrBpcPgtYnbKaFv7FiIG9lxI0EOHNHMPSZIT2g-U3_8Zr07zCbJsCuT6ood4Yx44Xo25rHaTcfHdn0nUZIRY9vg0X8kA2kTS1VhdUSbyWDnYibgtv4wPUy33CXoZgPmutPBRR2UJ4Xb7wCAYQz2gNuTA9xQSBHblnEISybMNqSs1ibuHw3_vdpO1-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z29tQ_WKpfXf_zL5FE9gsMgqNcDJeYbTySeo7GmgOi-AUVIjeZXAAPHhv9trOkVFqg_jzMG3Ur0Y7ZyFJy9sXneP_OrwJH2womJ8XdXef6plMmkzj6BugnbnzkmiNJYteVAp_uVGEfCGZAuvOYIc32WrMSZ5X8K87_23wLbz7pBSmtbInkkvCV1uBT0qatuDWEn16BzMvIfKfI_9dcdRRjs2bqUK_8Jzd3VsC584_Edg7gUyXxDji7gWEtv4RSDSmPeGVg772z5R4QoTjCYOUjr_FHgVMjN3IXROj1eeKBuxHJB0rc_1juc22yG6RWM044NggYC66id3_m4cpcH5KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 965 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6D1xpTGA2GYMH9t2rZHOUlM4ogUY69oPqdItv8CpZdcg9N6k2-JkgjOjGN7B-ZRSGyfX8OjIhwOsQifsISEp1U6gYEjkGLgF9vUP92yDUAE5ni9zRB9yMU1si3t84m4IOx18bK4DISP-W7fSRXzmHNztMqMhrv2f-xlMUqQyF4fN5sHsTDxMg4PwOAe3-fnD68Jqj7OdgTa31B3bKtaDjTIYsMuKlu6nddKk2NJYh_ymSggrOMXBNZn-jxNxbr2EgWqcizpJ_vc1yAWrEILkfNZmGjkHutSHCkIE0rUZ0tBQJMWSRKOpkJoNmioswD-AlJwA8yiv9Ah35RRHJPn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUVjLxcCUGc6TzLDjLVjNdCCIrk-B3tYYhdhohkXaey1gkZLiD0Zgf7-A3VlSalBalPHAZzWjOJ2zUdm7rBGo4COTi_EHfKmj6EgKR5WfA_nF0ylCdBa1tjjqelperxz6-rDZhFsA1m_nfRHQBsiGgk2ETu8HvG3Ys9TUeeomRsLw2PUaAFobgKAfHyUXC_VcwbZ2VXZJM9thgDRc-IMDNblJ9G_wn93Fo-KDLLbqIq3jQYW_eMLnEjERZggbri2-pvuK6RhbKedtJOlcL3J0Nf87B2IVsy2jveUKeEiXCTHjKd69PWaXRRzO49DlRuNN_l_D4uZx-yCWP9UByZSmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpY1OyBqYOfqpDEeGFGrSfUZv-iU1PT1KVsduMeXhuyCUoDTRPTsKqYu3AvOPpSecGCVpNC8gkAqMZVDkJ3jZX6ChCFoiR1tOdV0__uEGhSXA4A6fAjDpgZG7nGnwuwS97hoZfE7kOvQZ9aLfA83l7UeisfpYG9MDb_PYQTr0StWcQJQt1zV41leSPImyT1tPZ0jfBPNnV64gI4g14tog9ZZ0qOjz39MeUT4semLGAG4HjEwe5ezZJgY3jLlumGzykokGWDgRAsgC6gMTCvACfnth1A1ymSIKII80CFKXlTX97-Rvl5O6Mcl2y3ZZNZRUNyWdqJ4nIVap_KoRBJCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlFSAPOWpT2gKn1Rs6wIO8ihddoLjwdtGs9YdCsayZygOtoo9OkrEtGAfbQ3S_evnAX12N2A9_8BtTwi9x27TLPOszSo-S58-SP0sp33egZSFD1ZZS0UHLGdJBrKMfYh479csowUMsPImhhfWx6-MtLJJ5J3k9AvMUoW5mnjEgOWTIfbz24FplcHQmE8bGA9Xk7Fgx2kHHyDDROb4XzUp_vG4lUk_OOD4c0EpZIZhqfitpYmqu_9ZgjJVWSZyHbAKnzaOjv9QwMW5Zm2LVQjtCYvgDDPd5orI4b7IxJ6QZdSDNPDjwOUCz42KwaOmOJkviH7Iu8r-MCT1Bl7vnS0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFhi8UDcnYqbUYqODeQDjJQ_ijiNWiD-vaAFIlwZUbLATK4lL7mbCEGnc01zed-lK33tL1qB36ZUXCK1gn8X9hNlZ19QEAaRzzu9UX6556jvmFtsLmUNvItuB-Ir8WO9d4oWAQmohCcQz9qF8fIbpewKdf33NAhriipZFFZSC-lp9HC-ucxr5o6oA7Ieoenp9XeI2lAYo5ckfK5ftfWuqldy9PsKEq-XMBUkr09lAonAbJmxf_AFpQOCdP5uzFcoxBnV5hm1bZ75kig-2VIVZ3OJ_rhfmuymu4RMCjdjFthBeeyQBmJOoH_C3ekFL_OqzGuSH2VekS5iaPR4D4Jwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ho6NaQHEZeFYPT-rnYxzkp4DAEGnULI4HdctQx28wHbiMvVrkyx7PBrCdh-TNRBhgAnBE_Bf5m5iesD7vxzGyZUXnxP1mWkr1tP_Wox7GK_e5mF0VYnuQzhOxY19s5JPO5TsWVHAwuuR5oKmLjJbBDNbAbldmi6fUsnLjOUow5HL06mScvatI24sVyEh0sbb4Tn8znWS363m-VgpL9A2wELNkFf-bTN9B_IoNWarp8CYP3ygpJZSp4AVV0kD21IsbcQtpFPm0x5ahNpZ8FeEG4ms0686NFsPyQ3etcNiiOvjpP-JK_mSXVdM7P3LBSPamYBCYnAXwm07uzgRtWHKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STm34fDmYr6YubxnexrGtCwc16dflRcp2E1_BVZn_mpzEjsyS0JjmnMA9UeYzyhaJ7YFHAZBKg8aOduezn74l-exIy7TGtSEzBLos4rXxKpY37tbyKwmJ5ez1M6HbNhPVWjC2RZ5BV-vD_09yadKD5sOikcZij8KAPH17IYeWLWJmd0rlbT4CjWMPnJCoo5hS7YqjbC266oXDe68rANHeLaTAheoADMYiuOMlMF4mZb6PMTB_lFeU2Apep5WvO-ilcqnScUsu49EHMtBTpLInpQklHNm5UZ1uKZ7Jl4HyZ3eqMoHj5jJjGE-7JyVdl7b4wWbgeWAnHY8hZy3A7lxhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx4x3LQbNxjbdtNImBefxnbyV_V9jXf84G0PAs93ngaEoU7vQ4fXfDme9qMpzRMhg7x7iNTQ7xO_y7DBn_S8IkGnRDHAGLHmzeJSLBp6wISfDMejjBp6c110LXX2JoOvC6AjH3LIx1wjhs6qro7d2pssLg7SkPImD1usDFEg0bgXVm2HOUkU432pvOSOdyfLFBUu3hDG_I5Cg4PqRZF2wvdq5Pg7rKdawB6Z39isfvnYE8XKsGRLMhiJnnnfdNyW5MOnsV3yOuChweHnwBTYAW94MNYIa6JeSYNk18K94jKzqIY_vRj0k5oCUwBN4h0UFtbs46vCSqwQGJFUTC_S0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=sr9FGVMzGC7-grPI5zZrlfelnHEvQDFft8cwVDjJnM0OMgeZ8qOsY4FzBJScKEy7qaqER77rNbBUIew_yKIsOKwr3NBGVjzVFZAYlNSKidNWxg82rDzbh4WNWMS3YcZ6PF6kT-FnEwheclnmzrltyd--Bk9zx0RLWoH8vkart0A_6ZguhWD2mcmuXqptR42MmNk4ppbngGRrtMR3tZY70vNOjzkJnV3uOIiy59_Usk8jZDW-0MAPYbvSwWa1PZwgqJMJ3-aWCKGVU9w19iKmI_TkYyW54jpIT9GjzppPWHPAb2FduD7BoAoDXUdELSVuFZxA2fmAV7GSbCHVszTTPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=sr9FGVMzGC7-grPI5zZrlfelnHEvQDFft8cwVDjJnM0OMgeZ8qOsY4FzBJScKEy7qaqER77rNbBUIew_yKIsOKwr3NBGVjzVFZAYlNSKidNWxg82rDzbh4WNWMS3YcZ6PF6kT-FnEwheclnmzrltyd--Bk9zx0RLWoH8vkart0A_6ZguhWD2mcmuXqptR42MmNk4ppbngGRrtMR3tZY70vNOjzkJnV3uOIiy59_Usk8jZDW-0MAPYbvSwWa1PZwgqJMJ3-aWCKGVU9w19iKmI_TkYyW54jpIT9GjzppPWHPAb2FduD7BoAoDXUdELSVuFZxA2fmAV7GSbCHVszTTPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRQqJoM3xQSSHRh7I4aUJOETUBljcFh8_bcwltmqDYkJKgFz30x_fo5rl3oE-fGQYdsdCQmOqjNha1ld7Saq2ZuUrd_TPZl0wTfw5_WQIQflaaanf-mk-mzlbXrh-mSOiwGP1QqtJ_A64G_OkA_IeZlPLK0hGdwHmhus9HS3Ky6QO3IxfjLrL5h7qGjx59EW3g2NNNEQ1ZsUA5DCc-Ah_F50YxS5pfeQEzEjdcaVhXPiNVzbwLame85n58MAsPVp_S6Yg0WoDR2CCjuEImvdt2BqtIbIxgh4hTacOZw9b1YIEZVSBsf5qKy--vlbk4UUp2Z_sp348rfFH5JxeWlKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvy9brRepbHzFP3MqeJjDN5jS0p3emKd8hlZnpsG4Q4wG20SaAkspjwO6EmljwItNCQmo4jHGo3wu3hfPfAAARfJbMpunK1qAjlj-SyMHGEUO1qD7_QyIEvTlBCglxmA0G3VUduLKoKwPz0aMDr9-yNpRvzu8pnDuO_9HT7nXuPuazRvCE6Lth90MbOe0f_mSBmLAUURkeK4Ok7x1DLQyDbgeRjJgqEHhEZ_Rv5w8w3Win4EVUmYbldQhB7jeCe4cyEM5jaS5yK47AZCKbdlYsmICI1V-tv8NV-Vidmo93_JVVbPCYxc8pM86NwR9fQCXhxauI6YPPe1kfETElWlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3d0BAFp2GS9yl_ORx9blbuUaAPqmle1RtjkzchJ2jdS4N37wZWMr-VrWyxFjI5mAYk3hiAg2Cu-IfsnywUNBANlOge13OWbD8u7tct243PdBnBFLggY8os-oL-_NJIHyrLKwYFsJVsz17Ntm-wGvKCwS2CFdMfOtmSxngBff3FSRcl1mt51kRR8jU0LgO8BJXqciYXF7k2ZLn4Qc2pVywxJ21bT8aAByQ32vtZDLvV34YBrjl8NDfcldFmHiwf1lVi_oAyOgl-Bsocq9OiUmhm8zf1zJ6h6J0BrNouZ0gPh7Ri1Gip1SpqpFu5Ep3uwHG1VwvY1Oe5ddXFMQlGznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-BsqcPNa6scWxV9QUmt5cXSpZVIsDSE-ocdP2HHkbwAcisW0RfJsRS-f1Mpz9mAbmfaBs52gdxiUyHYc722bOEJViSjrcrbTdfWVrAzH1obuLe5-dL92riO8SWmAQV5GI0964bHUPDFr5rJ3neIb5sGDY-aBPagBKTJMYo6y0Bzct50xeawsGbV3RiCwJ6jUfpJwE7MXZo_wUEJ7vpCF3QiWHZuAxNABdTSW55wEHrX5kt2hw8jHFgWHdA8hSw2T-zmErHqpN4lKlt6kI2TgJyY9PA5Mj136Z5WsfQpySfaha0dKcM4yF5qP-tJOahlr-AnAuXMvW1faiy5qRXQ4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 804 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 992 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSWw116_WorCy9CjIv_dKEX4maiNnjUYb7RMRFvw_NxfTuENpFQB0f9CCUDVzli58cKVIJAe04LArsMXtWJDO5d2op8SSiYEg6W0k8cflTNLT1tAiuakMhVP7yKHlwlHm7HG4Lu2Mc5fOFAL_ZFO06yy62siKgyrqxCkJyM7ytCfk2BcyhPZb9jHZU0PXqj8XRQgnCQPZnCZMyqDoArKnAv8btpnStXjZ6sxKqMNHNlOM4eKVY1y1enmUcJyjjwMtChFhMSO-cYRt3e9mDDWgkpCMSSAU2_l2sANAnRufx5Z5QkKu2mAEbg8zEKyaZ3iNjbq2tJM2t1-kuf5JtufLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8A4s0VsWb0Bl2agV3NO_wu9gQ6iuObkklrZ_c829V6kRnHctd15_kOX686dnZK_D6WJb5hujOiAAN-voZpYu0zup0uBOzA0vhziNTKLb7lhr3clwrYkXpAujvBa_0rVf6V3a4kKYuXui8570f-vGUPdBFOYT2olAMYZx45-OrShr5gw104u0bTR4ZZgvDeBlk6Z_EUKC242XfmvQ7WVLQMd2lyrQGwbRp1rP3IMp3fFCBtRe4xc9dh59mKczgDOI0MMzpk3QurTNQ_rsY6JOZRHKp3Z1-aOjtXWlqFIatgm-8waNivBQh7E_ZhP4SNjy_ifr64kVgGq6t8iNgiamg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AH0FUYUVdJ32DsykIox0GBbowarzMaNfkkVEj0KlkS8NCqXtx--L37PBPOTwH87WRaH_LGaO98trQpprDDp8oupCXlJ7OhXpohKmJqV6bILpztk44oi_ji2lH4kR1ZoqXWMvo6vlMl6UOARAEsDv2zi8MZ8cmzJr8EhOc5jpKwmQGWhSskxUuDlxukfnn8lQPTSNm3H-Ny2XPHn6GZE_K7TxHMs4wN8UoNUUsvnvUVG1YLE8VdU4zFHhGopxqPM_FGRSn8Tw1Ipa64dNoZ7lDEZ-y9YW2kUek7pKm-d-QT1g9yJm1guu43EPVT5Hz03zXqLXzEZkfZaTYrPDAbU12w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTyqAqRD8TlpapyeCTRELkiRRc00C6uOSZW5UNEIuz9HggGHV0zvwG97UWqJxoAhSALCEqr-OADfj8FWsURK3sCwQ3_lBP4-R1jRwZCrgS9iFC7kh-297T5pT909gFrtUPb24-VbgAyeM7LnsBsxQGqyH_B-NMTgLXHFNNkdRCJUTecjJSn6GdeYXNx-6Md-50ihmDpnj1Tk3_aQkkQn3dKA5tsM-AEcPaNJsFYg77BtZUJr1FeJpOQ9lAat0g7RCmgI7NUtvhu3Eyua8Duq8z9ZVx8rQYieNIRtIiq86EGI771nqmoiR4aIgEko2SSZHzGKLJ0bPZLfeeq8XwUs2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 757 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBqsr_wsnzezRo2nS7cWxzVqz46_s2-Bw1Co6mXkiFrgiSLf4Dyq9pBOKsF2TykkCQ9jJQEVcnESKYNaSuo2DSbA323OCbtNS2ptNN2XN60NMWxPPipPa89sQcFJnbUIPV_oKg2IfZRyD2vcFLEIdmvyE-hNxYUyEqkWpEj4R_a828ZjGtK70oA1DDrplkZc_FX45yDc0pmcqQkr4E1wn1LHIEfIrohDmV7BMk3e2oXzLbEcK6tim3S65_d0Dykw7w2eFnOXJ7lMuYNnZrq-4xkLOHIqWJMWQZtVFIshR4yAESupOZy-wms1IivRsbnADuyQedv_xaNk2VllbyRYaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 721 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ5y2yWCKJt1mB9myuViCEXeS5y02KXGJyETxVfsL31ElVV-t8Bzg4HMhbRc0fyoso64nS-_WoNxssGLJ_oxN21VEwF9sdq_U4pMba8TjwcqfJ745cjmuQotf4N-m6uSlMyUaMF7JB2rdcmiH6AjnSa0X6guKCw6CrWUX8Gw4qJeFDxUEiAN8sJOJ3P64GGw6b_cUqpQKBULkjOOZqqvrwHV1QWRDG0V1vnN3EdvVN9wfj-0Xd5ks78lVuEaASO3NIbRwCLHoebzqRU6UbsNqMpYTXGLJK700PmqTfUhx3tBbfR9dhxiloqxJAMcM9quTQIbT6AEIfwmQUvIawOiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_iXmMcx8SkraBpHZHVFJkMkRwzB0IMc9TezeQyCECjmrgjBjbwgf1zcLbQlwCSY_yrB2xxY0MasoJvCUmSVIdHx0QajQJaUh1wv7-tIf1dIXKrWQl1fvPgxlifrBxJieQbdIH5HbzbuH7NSTKCnvdVCt2nfuDRk4yDcC1f-V4blSJ8ILZ7kB04eyofCcsAZ_ohEPZ-Bn_si_BQ-H1FduyvgxdmRqhvcT91TWWkm2zU-plz_9dcT-gKt8Ivq56t453x_sXzPXKeNXTInXiyfhMefpI8l44PMRsxOJYHE8EwA4k6Eryfbi6YHdPaTDwdzSzzRcKCR_SIklz4RDQB3mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 604 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE6kW5siRBRgPP03X_sPlHdApE-xRPjkDjZe8daibwGE_ePMYGBkT-z2M_QDVsGlZl_XKnhpeB3oTYOiNpv9zX4OUWuwNJvtHBiADb_nAnY4wqXItw67QbcaF1WX4K6DDcPdGhh5S71rKU8F52STUtuxUVA5mDa8-zEhKHARWALA89pEPgpNYeRQnuErJeyucxn8nZ-1RL__zHju79rmuTmTUk0EVEVdg51ynw6LN2NAGjEOAxDQZSg2oUg4PjqGWk_JJfpgTVRK6k6zEorJPmDvyzy1e9hI9zse6vVTnUWQr1rGXP7pVAVwk8EFh6AEf62uMMbJFlV4qdPkb2b3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 697 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 641 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AUJnHr5757hu6ztc3XrTeOqbC7LHqMYsfeiEYL4PYEjhvZWAtmEIz_ep9emUUQIOWeKSn7B6vhQwTQ2Cp-_upWWgho0fgSJGXEe8-N9hRuG1Yjuo4OFBR3geHyWGVgNbjSGf0iv8WFQzy-H-E3BJypLTmbYEYpQPIURStaJJ21su3qefIxn2aFe6XxywMFWk6UYXNP3gknLVgjG8v5vNZf3akNbnL59H8TeLr6la2UrP46-dhQhyTvBSKUe5pL4DhCYT66zTEjG9EiuBY3Lp3WyV5fu5d1i2ci9ripyJld0-nmK7JLPsA6lvQjp4Cebqa58fX_fWdOOELMUzJSg9jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNk9boYiDI74uK68rfbcpVtxZKZdzWeIJAkd4ktqG8ylmGj8gQIFLJ0-EZafnOG26SC5dzr124WwnMNGp-JomAVxXo2FiBkHyZ3ZcOz-YAp1qtHndKnW0phgBcge8yaFBDgvFvIBiIxaqPbjIbUhnsU6ybEkJ9iioqGQVG2JptGlUmTbz8CEUIDaOHEiJu8EvoN4-X66jp8O6LKdGlaQhMM1YrtC9FMYgxHM4kG34O6JRHzi3iP0kFORgnTYn22ZbI6nyaLZkGGHsflksJUFeHg0Iy7-Z_FJHULKMFn-K-5EtDljKD8nvihpZ4lVymiGgrm8q_YlEyed04_fygxWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VsMluUaJciiEjAz2-JfWf08hZIpNrWDy_5bqEH0jCkrXCKkGdswDzEhcg5zNfQ0V6Znnjt-gwVZ-71370FLDrw9IsoEpfy0UBdEDxZEa_-HcTPx48-GbOd_k1bfw_F1rhsYP9U7iIT10mrGWUclmnSlMkmSIitdXVlN6GKFzCHNdlXYv0N_KWjPHKLF0TOcDrLVqJveZVcDUhW8KFHmrkdyXRdaFEb6RugR-D5ePYdGMEkTdd_WKmjM-mbZpussgH_DctENtG12Pt6U56j4SI4bT5LIv_QIfzYV7OTXEWg6XJPTNrRHytndvGeYcsc17Fd8UfxJSRI9xqco6NsXz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgxbgiBNu7mF8emgavSbgRxB2szEvSQPnl9WrY2zgL9iF0ifvu5KQZoqArGB-nog87odlHqS_p7cJDafpbMWFuyes74JQa1trTqlj72tECSd4UuYOEbnrUke12egpRlySir2iDEPsCJltHxKEiu7ytDgowPLULQyiB-XiBPOcoYrHaRt2PKCnkE1KkoUqnN7zAbQD8vUAP9o-JwIX5QgsRbNwoLhuVMaa0qO596QR8ng94FbqPolicwnILHeNczCe2HuPHLb7YeU7pyvAIRkltYMMB1Kh-KybcyCLrff0QcYX23zxMfCNb0h4NmhNNbpImGYl1sMjcP5de1UZQGi4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KBRXWvI4Iryj9cljTGhqktR1fO7MapulMrxD6nXJGPjuVvm0MAorQExULTuMO9eA1pHxI-c_5VRzWCDjhTB5aPuA3dgeWxM9hVj2aWfS1Oz6iBq8nB-GHGQNmyEIYh0dLCXY8gWgFJDGX0W-sJfx8Kgn2BxvZ6-7cbDCifmtKtvFzcMRLM4KDvISS6v2jTaJyQoZeZbqFRa_wUIh3xILO-lCOEl8kHDQpGN3IV0bkTqE0UgkC9jhAui58Lp2ff1SYJHCDZvpvBRDx1gxQOqge2guEJHPZrPFhHXA27KA8rudL88xFYeEdCNfnqodDxfPa0Sq_UweiS7OvEKCgRvwnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnZy3mRGKlqh9rWzjTWuVObYmNXi17r8bg2oTIbFaByLJiw0i9R6yKaBlLNDXOXicJgJAK-7QXEBC0BlfbvewhMmv9750XERydd9EBqxd9PY-ShneAtzLWMk1iEd-6DveWqgHLOr3bqAC3h3xLAeDhI5tHMW4AO5hAyyv3blKRIS_OPYJTfxHi6BQz4T2zPNuhSGhXRQHkBAIpcKvUxUeMYvFMnifMwN75Bgb7JzqoJXLD6oX4CxpjrOlSbAzu3wy3EXP4RVgB0qdSGcFfPUDtKz2bP6LPaGyAgvi3d0gkpRNzikUYR3uqX-yrpcV_N1XcPFXAhv6_tOhz-dIuYQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 582 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3ttpM5VKVHPEuvOiATxFam5dUjxGuuI8fbRdd3tQPJez1ulh5hhpfmPcjFPDWMd4IR-wU1s4ojv5H9S9KM96mkQxn4SS_ck1zkMKdz8VWGfN4LJKQjgg4OQ2ivgtjn8aCIlk7rXgZhRWI3FRltU6NBCAsRJJP1QANUs7Y3R0nNehtGhjSgR9Fb6XaP9wxaOePvExGRPBk3KJKcb-Lvg2SzhmMmJHxJd3N977qLp_rXLTa-lJNF5Yu6y-0jv42hgWxjwOqNcW3RHPt0IsWPNV31-rRiTgPRYj-M-F4TtWjSoYtldAXs_xzRMLwRwlbVnoECy2TsLOT9ILVvRO4Xrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 594 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1Dl19vd8UpqzFKtFcPuxokeCuILqCGcjrGnXH0JpRyZfRaJNKwQUO7AsiA_4yqYtOlxkJn8z9BgI_fLZGCiaaDQJSGVteCCOqgdQoaX_-8rR7oEJrdmNkSkmzgf0zjvjlzJh7pBsU9CtdfYeQwb04CoQWz0kuAzw21JfwrB4ys9UWrl6QshqbyU2Mh3_HbrRwMqC3kDGUiyK0-6WA35tVDASmfFelRvdEig1vL_nm-CakXROsvo_CJVZapkaDvcBOK4Yqhl0LL28Ee75Bp-OSZLp-yvs8O2vF7NFe30V6DPhEQupB-ukgmlanTbRBPsKXrM1jBLI6kaU3iYLuz5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1iUJ8uXPukGhUeqCnDxZKkOB9bIEG6HGA8MeWxG5zRxQYYPPQL1f-NaJnvyMNf5urSn8NfjGWnze15kOGzRXs7K9j5c5od9f2JPPokZZOxojicNIYDUr4v04RxzqmSv8j102pW7jTqJ_C1h0n7oIeSZoKQRRw9Q_a6C99n3Eaycs8_rZuJHwRQX4x__hwftU01I5o33fSCAcm9RqjZu5a-Zm7cWPfsAizX_xOa0sUPp3v8ksTYapGf5ZeXbJAfPFl-fk8YfbNpobwcZK0plvAkldanaZBYyrgPkS4tAVRh-twTXVoDZ5gHGvOnJ8y_Y9S0wtZmNT2T_Yg1kwJ3BSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 647 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIM09y4lKJTL8OjLITxiBNIelUdqGvhjeRJX1soWSswDe3-zPTR1fLuDdD0ssDEhqf3NV9YPUS34giQ-Mman1ewFtLp6hBn_3L3sK5xc_ryhM1GNCNPUBipySrrt1HblqRf5kDVTXkxtFVl2CvrY5RjodQ7nirgZvtL8-luEaLWnZmc199rjYmFDvdMtUHjDhdgydK_5bBmmvdEe7ZoTjhnrdtO5atN1ywCovHiFwpPC_HkslehvJgnC0rZOHLV5uWiS6sfHdmIkDsN2S2b9cfFKc34BzXvFmTa83957d8XEOA66sZkmUudSH18E3nyUD0-Vb5Y3oF50ZdV6EbL1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 715 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIFSkRqzFlnB_XFrsyjHr0L6fzpR7PD7wNVkUKZEQ0sYU561iUeWtAJJ4-6qqb80_4ilGea2BcMs8U69TBOXm54rk8QmGxqo1EilFcfpnRp5oQdJ3gCPilxPxyF_OxAn5iBA3tHNXoHHe1UvR68-BtqbU4XvaaRtGDGO1b7xwws7tvPQYBZIXFPw-Kov_pIBVuswEUghJdPRoNiVSqlTPnjmnVsZF9nLcuce9IC7HPFjXIQ7KwOOUHin96IYcE9b0XLpL3Fvb7GHQI2rGVQPgn3b6M2qjerTwCOekHX14pNojNGlRIA0ShT53iELydd1lKgGiqt5U2TquwxoR326pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqXhsFwNagmkaP6l7xIY7sA9gi-a9lPEl77yquNm4j7naloS6-K148RMkg2DQwZuIKw6Zh1KEQfBXLASvE0ddwNGmJPhSxMzXBIvxg-yZwN0UarZ9-oDd47O0_NdF0flWpT5VpuhtWAxzSQKF56F_z26ez8wlc0tx9ZivcUi2eBCYhqvqaf-opG-1YfhTQutuCnbugJR9ktEpW8nsK4h5134EsGiw-ot9LH4Te3hHgICE7bBArBvJiPDdnA5CL9TrTGeIsFsXjcNw2xKJG1QQKlCQWNc7HTd-RC1IxXmaAnux28jNpD5Bi1fqpq5dThM8L3czKKnv5PHQ3HM2eneIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1d9B3zG4pZXHOawmqX_a9AGfcy7-VafFvYbZmoPFJaB0JRi4bnp7f3-XDGMZ9k_S2Ogc1fV6EaPGMszjIFOGNgaxxTXr0YRapyITs1VVw1of7yzBZ6njuhuG3WIkxTCuEmb-ACGUG3fgOzaEBbjaLPUooiuxW7-m4I68eVww0DqtQ_URs0Aprg7it7Cf6MhQsy24PLijd2wbZNL3EQQCS_ASV3oeDPyfsoqaDnODu2P6MGen694RKxTWfi9WX97CgsBeWyEFcgs_HqtuCEufbDV6f7q3CDDkhmdLRIgDZwGMyLoOw1T3lhCi0w05VW2-af9IJJ7Qz_-NMlF9R-rYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWqi4UewNSRqc5wT9wQYiWsXSlYZOqIgMz9O4yLYMP9kyImW_eaOlhfQsLCKHlywpKQCKUrGRu32xvac7EMJjoT5BCaTLPIjgMdIeWCY0BJ20_9VZ_uaFhyaD4cy3JXJevrsd5SOpnlyxpOFZ0RyLUOjS4Bu-AUhsSSXODLN21NC3XhSzdM2EWB-dmiQedPdN1R_U8qOcph1mVS8lqWXDfPoZHb3b92FTiLOciegsZHWEjM9ceNODmQDdiIIOFXUm0KiyzfxFSknPUr1PCVUOlSf7EgiUclqe5yp7Ipgld61YkLwn1DHriS4h8tcdObFU1us_q17zRLrR9pZzp0UpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h58KfeSdxwOgx5PJJxKEvvi1jhCs9itvgj2n37bdHACAW2LbWDVlAhKco56Gke19flZK-C1vKVIx8jRn-trdscdrfgi2tcVNDRiSAD8yfEGqYK-M_r8KKSlYpN3sZuQKdJKrBstsbrClRs0p8LcPIFJr5jEfRUNJoJ2aAFJoVpTXi7Hw8l0QPfLaLxkzmR_0fcoHv3WbTwN-rSO3vEQcH9AYUGr72Xr8D6zl2yAZqLBGLUSDaRc4EIaw9t1gjbiM4BtaXE2PTSY70kV8eNcvCqrYOYcMjQF5_1syJ9GUT4Gl7JRJI68m8OyTasOslucY9PfaD_RbDQC75drsh7HwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 546 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJUZ8LG0s7P_uAJmqWHI-soe4lzpCNw4p78UHWK-43ESQ9qXzURcr7KQcW0jBoWHAe_ZjI99vaxqOn8LwA5aNIi5TZsVJM7hh0u9yi6c7kUiqaS_DqMx9S91DriCkM8qo-TZYjz2_3zfWjRWwAfjumBnD5d-2Zof0zJvK7fwJRYzFGErXTNO4LnuNkoD5rIEDK8Y-va2VrOCHE5K6HPwWQX5z5iarE1l-NY4QSVZkf0F5SHeAvrz3uT_N1Cn8VNHBjXhWaboB_WUPBy3arwp-4fPdwE4qSWILliyj2OvjwRqCRiq6QSU0f1Vp8JjIKQT8i4_eiUgUYArQ86U3kiLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 545 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emvqjhsGk1UG_rPqDfqy1fvqJiWCR22w2vQotCQ_uCPTyiOxpJCZkRglq_MyF-ZXE1CIw0W8V347v-Md7k7lw5265tSgsqKMOqXiK_CADRf1I4DYMQBz3JomIjpwNSz3ut7ooU1IEiSXe1qh7fSFDfrUh7zaYj9rvUxYNJ3NDSdCXjJIl8e4NXwpsmc5zCue50UZ1LpC_-zNCQXb0RBMZhoHWrhcWBv9M-KNfHeLkc6FQQafZ7VLWl9UFOCRcPyfFz2w5oAwdaIo1YrXOYgSgtLIH_v4d8f31dlE5xHWiRufHYjAfzHferr9deHL9OCpD5Xn0hyqo168n84aBFzi_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP6xPiQvODRQTyR600IGa8l1anGwcFhU0s3kutMG-ENi6mgdHNAMIDNM7ukefJvXt0jubU4R3AlT5eSKh2kIytttUo20_MeVwEHVWDnTgwA0rtlv_7We2xirgSM4gEofCCSNuRFFFx72qyBPPnrmroySWl0NlQdz1PpZY64JNmBVdGDbVIKTTcKGleKESptPl0EEVAs4tmsbkFp--3t9OixcDTYZGzgFabvAEL4u5BhSrjYbumdrc6XyHdSxTuHFPFSvLT4_y0zVabdoZL1LaqxcGBCTC_7-v17Ap-VXddOC8DwR98ynog5P7pf6oaJQ6Ny5KM996j5yqtizfEKiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 683 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 692 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0ZenvPbl1PqMu-J6jV4qf2SL-rm5HG2rR7Bxb1sZhzoL6X3JOPsqsBYuKkJ09VMl1hPHLb2CVHtQv3ee6ITD7HhQ0Xu7ZBCgfiX95OvwjooEV5-mu0k-fIFWjvtdPwrkT-dyZbisyfsRG2t7m2SEFexEc_cPgeb5SByD5L4Qte9C5P-bl65hV2qljAELJQeWN59uixNsr4Y9txl0Bd34U9VzmDFe_NWX-JJy02BmQjQnyeQB-App5kiBM7q7l_8Ek_6JBRUxxeI-jTzjcyxtPoMgViurgnTbhWPiXFVbXWW9tpPj2x2eRflGCC-OnZyRcET-rk7oDZjUEhI7MqbEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5ZjF7mDK3mSFJxj9mm4cC83cLrMAqSMI6gaJFLNDIKuF1GzfGJuew2ZjWm8N9x6SHmHhCJM3iooVXj88SEhClQgnO4i33r4aE3yNfaTxSrStArLMztWjBd63tlYa6TBtgFt76x8_LhDHnpLp8PNEIdzfekEHKJFQB1wAG3rx1JqnuwqfyQDDwlIGeFe694DaoOUXHLjKyuuv7SbxagkQhGi7vTtUKwINMpsLcF15zoyBeErqBTlUY9q1XZAtZy_HLzvQOSRrK9FQTKSWyK4hQxMrQzQUbSzSiP4av-ECkElxoQZCyWoYEIGvOR8rmAHQ66daDYWqfxSC_b3Hu6NKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3sV6JRlNUJvyYj95MhWfaOm9FlC1wurTu23zuhEgfQQD5Aks3K6x7upw4NMXf4qewOxfUnlD5s7DfuBD5s5hAAOBjVnVHXR2T9ZPeCLy59rBg7bsPLrlo8T-4Zrm5Vcu5VVeABn4Bi_Yb7ZpDue4FC29RjD9O6fvRaketW00S2kF2z2n42p117t43ZgFUZRmNMsNGGGG4naq6pQd7403Vr7YVJqo0ABTe8c3jzWixJ0nlmBePm67sxHrLR43F4kA4z41jHkcuCU8cR5_BFrB_NdsE0ljrJx8gOPKHwd6VnKm4ILBQeKy6ovZojlaNfF1G7yZAlwoI797RluihXmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNE6mdtkxrK-r5sUMq2jUHOYGmVtP6hfG8Gn1uzpPdEr8IHiqvKnTyZRN0Yr98zce5LpU-9zDDD64MgNTQRekk_9PRNKYo0AuIF4bx_705e5Q2thfVECfjBHrnapXI-0YM0ym48l_e1PDsPwbRC6YnVtfigBPL-Oq3zje324TgxnjtzRgNIL_z91TPM4PT5ZCFVlga7OIVk_xHDZRUpyAiDU6bMMkiGEvp4uU1p2nD3tov63Tn8WG_69KZVip3e7EXYxjUD2TB-_taf_cqxrFDApkrayw33Vuzso2-KOGrNXnqv04KZp3J7Ergh9Fu73RcFM1hwyV4ihKT6cCf6srA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 806 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAMI07R9lnijxY241cLEuoda4MqdLOY6rnodckxMEQ1IpcAwfBw22nwEciB5KZfa6ywrkphA7gj7V8dCpkr51a5-9OGKNmCXGYXVVhD0E5NicdS-hs0y2-42e0wt10VJ8yVAJEOVRNPSIkm-K7kIAlCcEsFjGEgVAfmZcAIaYAVfRTOm2qCqdN5Yy-gNqf6W0TXRZCKDbQvMEShNm67EEhj1TeA76TL9WTDAaKVeUuiVz1o-xaz1WGyVFQcG0M8UPUOqvmTOs-LHK3Z_A-iv_QRoIai9mSN3QY6-aggSeRgqkElWCxmlo4aB5Pgu0xKyg-jX-QGB7X_lXzzNSdcyrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gB4dpGzUR4gYgxe393cYX4fC-DsKSV2nNjVzaTuBA5jfgJu-5ZbpAGU9HYQ2mqu_FNJIcG2LJGnOf-Tcxhqqu1VoXCthXp87Zv6JR4C9WpAk8r0DYxS_D27hvRqv_Tp-Z94tNpAZctMxfZNkpGVxOA08ETqlWT-ufBAAImjgiyBkgORf05Fjhfe7hVo7WyMGjA2fpe_N6i_S2DA1DkDZTXlwmlFLlFk_qcN8vxABChp9jIL6oO4bqRBYuTrL8QCZXV326963ouX4RpKpSQyyJTb0fR_Zab8YqbYYi_5rdDUsrcPMnqaWCEVoXwujpqxIa-K2CJmuuTdvxL-yFmlLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFCupZMn7L6_-e7zkqukewqLmNiF8whxXPNMKZkhuePpZu1lVHaxwQCxfhA6IfOe7zb6aGe2BXnYgxWflRvxm5Rn99JR5uQXg94frd_Mjti2LfuWZpclP15-05JeBQ-3KrQewkmUOvDiXKS43uj0O8QFiLkrA6SeZ4C2qCRXaJMQ94-K_I-5zZQTqN6gPyy23-T_83ho0cewzR2brQnIVcz-FWNAa06rCGtAQiqBjNkU4uptvko_W_rWzkO1RuP-fyrSB3qVDUlEhh_O7PSxCJ4KOXnyplUGOVWzaomTmBkd17uiEqo9fkt3F8LIg_iaemQaJ5kHgrdg9DVewBzXUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKyBPrPW5RAXomQEP_mpFgx2YEdVIgOs6FJebygY_xj5kwhL4UAHsQTvZ-GOQvLIhaA2eppQ52-YHjx-geUJIAWtcButeRf4lg4rjB7phCFzSYFBbwAcRRBruCzPbJRsVywwS7OB6UbP-jcpX1ptlBRCEFRnKQUGQ_m0m3TI_NA8MuayGKdvghotkeJC3jUZ-GBVLEpe8FgkQ8hEwaQBiISq6Itz9UXwpkJQSRXMR5xm5Tq4zAZrI7L96w2-tsBka0EayKgYPCAURhdVqDADPkQxK1T2jicuHpoOb9MAbFoTtmORrX84lcd9xX_mAD1t1w9XEb-_65PzkTGZaZeo2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMbyQ5BS-Zd6OQjm6NCYEAgj5gLPZmpHSwwKGhJbTX-AIahTYwIu12jITFo1NnnWl7vPWE0Oxrm87lJ9FgYZFUNbjaPIf5u2d1Bvj5HAKTa-UdTjfoZ9nIIgvYEGvJl0jRGmkDcONQmTsWVLCtsIOJoaDfHh2HeoQRzTbYtV6ATrU-AuovGmp-0vx4B-CYX8oUOOLKthQvIkK6x7M0jF_My1af1oywilHsLJX3V_iObw69gD6R3_3jhk791KnT6cGJ2E4i_VPVPQeTJBzsOxuxP9g3Ucm56TE-XWIIHXgbiMqfcgXc8tycNhSAHjhrXWN2DTBZ2wKzbpEqvTCWPiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGolFEKvye18BrVQ5Ib2JjRIEukJ9e5xNVvw7TPnb8fF5Np71n7QCgG3GWNt86KT0FwyVE26_JobgtnvSFa8ueo0zoWpUjzKfd9L9rolAbJ844jjCDUpdlAsbWLhpMKZdmHi8KsN-_Nt63EBi8mOY3HPOG7pLX-KH8ih5fMMgVyQt3S56h37rCsxewwW2oCThLsxlPrsERjZ6JnkHl9zlDlxaMX28YmBG798z7FHxJL0TGZclsF3QwVADH9HvnCw03NDI460MZch8lpUpbX9XmXds-bVpgko0q1EePwgqYHbMOVnZz3oXno58VoYhgWp8kW76_BC-btqLLI8Ft129A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 770 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnsDSTGmghwRR6usKpX3j_DMsqCgG3to1nUvVoCMvhrwBbvsn18GGPFmCYgg6vdbqtu1r2N-6OVNs5Fb2SSHLhfOfFRQgVl7ZtQZHbXLL6_-W9TEUCKOjboCrMrUKY3ggmwFzSyJteysypLnU4iZycWaL4EiTUmZ5nr0l56dpGWXDo7d3gUZGCleqpkayrbxYK4sDbCx-v4Du3--i_qa3n-i0t7mUpmQUC0l0NE6dzeLN39UD04-cvR4IO6hsQrMdvzIorpLjMFBRn59O7pK7rPqm2bGrMVev1I0Dg6iZqt_-qNel8WuV5u0rvyemoaoDPgVL9V5hWNbrs3S-fIUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cuV5wIT_g1YWXbmJyMCcQ-2UgjPeMerO5SpRPWBpYAco3G_V-6GeDRc5pmm-IpAOi8oW3mHWV62U5_BRBGdm4DPG7QMDHLHUpH4FOCS5SQClWRx8WzAiKpnGcH7iBcL4pGO4B4lWD5FeW34B17YEHiGZKNrNgUbqABfFFJyGAbhXm736cn0fAg8bjcDNozsowCpHdp7Wtpc7RWwcUuj0otXMa6Quf4lJ8dmYNIJfzWksl2-KwxrKuFiUcJ2rXgL_9gqmEzEyM0_VYCCzW3D5M3T8x84zJl1Gkv-9yiWheKXE2V4gN3OI27RllPtQ81cZhUkkqh7vLpun_SvfXeX_Xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvP5SNsQqDTcaei7rOUYzFkAGAtNCRBRzYDfpDikzyVVLTTCgGtdhvaPzyMv1GcMuQ-t_F1V3Z4aKHbq6NyIa1DachcpyDLwX_YNfoUvTxisG1G2JZb0viJ6osEX__IQWw4cHkTuvwfPlxpLEoWIObD8JQ0K9axIe7Gkqa1st7gAZtrs0ztZR9K_9hll-2-IcLvNcsYlSMe7FN88bHJ6Vep2lW5jAglZq3u_2hUYD4V3ABdkk2SNc6TQjHzO_mG4FYzqkHlaiEQggnBEM2qc0gXDIwNP_DNPHml0uS1ki_QVD2AUxoISw_8NmLiQUW6DlSbRT399vKITPDELYvdwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mu2XxckLCybsC01mB-Pcc8FAlDmCSRtMBWjujIElLi5xY8S5BLU0dQyTz99l_hD-MEx66oCdwlUdA7px6lOwGB4901b5SQfRrP11kD7riOzSOgcH9zyygHjwTPCmqiDe958C2OesEJ1qKo3LhO1XNoL9T0CvEL4eesCnnLIPMdxXg2ocshSC0XRXRLm1n91BWsiFJKmGCQcHp0_Lgx5bqZsr9-UDM9KsjAcYaWQrSskM3Z7NPzd0qz3YZW7Lm9wxGFGlZyss12mzvavI3BuEoKh2qUm2e9y8jcyWNtGQglasebLN17QXgPswiLg30pGkYrfl9vlxbIDSiFb5d_vn-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDmaIWOKT7BHS06phPcmtO25XS7ZvcduzHvmmOlAEhCfcBoycvMeiU_Ez_OVYBsGDKht_YsIDRTsM0Us5UttnNvdbA7ngq3LRc7gO7Sg4jjeEkoWmqTuoqBYfttQZJC3CRtZ3EbiUwdpGsCQ7-e9MwoC15d9wqaX_n8Ib1a_m-vKqs_fDHnY4xFmg9xfc8DgINQ9c8RBDyFfmBCw2SvYQ2K43sSCHQ61RvUaZQKOnAFo27Bqt3uYFPKvlCkbdjBSb3nzCWz4R88dYHs8ebJJLwwHdH7z4oQFsXRZgmM0VHWOjJcQPcS9kyxf97Z5paV194xHlYGRKL3CHARdGEH8Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgudZpwNI9u7j6FDLRTgzCWuAA2dc2nt8quEj7IVa02PVhbZ29k64Knt6SzeuMwiStkFa2GYOOfo0FpORetTBiKvvaLjKvHB1oZ2MT--wWq0_7UL2XdzRpZAVlUAvqloBynXqG1ElRl0Ae9lg-XI5xmb71Bnv70qLUxYll7MCSaN7mRxwCOXdlSUQKguK2H2y_lNhy0j0UVijll4xlfrB4Oxvq0lRygFk45UbdxysJcCUkjZpWCXjkiwZEp89Vlh3kUQhwS4KdAdeC_JU5bBc89ZAfeCoDXxiXzdMnwAi9EjcDXpMi7TXhsKDNV_DL_40jXvk8Qe3ekZ_DUMGv9ZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=UjF-xPNErhRRVdwGTyLRtXF_60UoQVoFWBe4FM4X9YXkGaE7SbWexd9HTe3SBjQBfhPNd25nbphYcEBCOPJvrRFfZFSzw7xGyrAjEVLjrDHr3hLuFYJjNZypZopNhsKyNEVfoj9J8qHYEhcVxMj1FlqqLSpAMJH7TECA9n-CnvxJONOPCZjxrtksw3r_5QMwqUoG8WnLy2XNiKcNEtiWgbkvFt-eFJPQNMgUZF6U5Ier9tMmSwZex2GahocxfDo8WRXh-3cmTd4DoqPujmZeBotSNyzOAETc7GzGXL1XiLfYEth32k0GBhMstYgFnJTIFyzSfo7FJxWOMeq3LuZQlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=UjF-xPNErhRRVdwGTyLRtXF_60UoQVoFWBe4FM4X9YXkGaE7SbWexd9HTe3SBjQBfhPNd25nbphYcEBCOPJvrRFfZFSzw7xGyrAjEVLjrDHr3hLuFYJjNZypZopNhsKyNEVfoj9J8qHYEhcVxMj1FlqqLSpAMJH7TECA9n-CnvxJONOPCZjxrtksw3r_5QMwqUoG8WnLy2XNiKcNEtiWgbkvFt-eFJPQNMgUZF6U5Ier9tMmSwZex2GahocxfDo8WRXh-3cmTd4DoqPujmZeBotSNyzOAETc7GzGXL1XiLfYEth32k0GBhMstYgFnJTIFyzSfo7FJxWOMeq3LuZQlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4OBKOArI36JXZ8P6QCu9GtWPAOs30w1aS0IH9iTJlAGL1CMBXDoWBx6f46i_zCLhIhk3gZr_Xl0QnSmuL747Vxb859P1lItfEII4AlxElXzR1ujVEszxmp6bPhmY_I0BKwkru6pqo16Tz31DiGhYL79lJSALp--K1MxyiChzg7k0b9FdH22IzyrkGIrtElry73SZp1wrMpq5cepwbB13ZhUvbwYI26vT2QwapQzJpPszyFTDryfxmQbtTLVHdTude8vCuxRqDhU-oZLFzr0MvWBvutX4nmm2o8_DvYgsSvwTfWPfYiCPa-P867voTkVHbN7L3yagPEFA2bmjajNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNmR0u8Mc5DQXaFmtvk_TCzOgbYapv_2o-rnLrzLZy7RmoSq3QfmM-9xdZx3Fha17hZ9kfW-Wyo7Kyy1wUzqJhphTjlBCLsrKFAr5jWAxE-_x9JsGHN2Wp9rmPsbbTSIsjhE6wu99mi75RgTSFTN0hK6T04mgmk1FsSt5lkok9krHS_KJ8str_g3McMuHA5ajI5AraxU62L6g700yOO-TE1sZeBK8obuObLu1vt0hKWtf9-mdJy1T7nhYLbA5yFppHp34dq3KB70-M0dkCKkEyFTKCKeTMxhBew70IE6_-jE46l5LyGnxIKNOSaSl1FgBcU_BIhug2JpYTHcXfOoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xd7LLxdBihpGHfzvvVZQdMuQsuEKugj3LqG_z04WnCw1VFAWFV5xuPGGUun_SLQAoH6nIo5RRM739OMOm4zrz28UQcqxooU2oNI81cAzTnBWwBfGztwkOL59zuYJcfKzNwHsPcHgvMK0BV9i8jkivEftlpDuF3KPow2UotTOBSOzn9lU1rQCbUuEHy-elzeo3EewRsmhMTVYwza_nL5RevYoewkxueLDRcvSEmH6iotTqgwDPBYdTl1OpYyuuUpkE0dtLMTTjYJEiVi5L3niWTd17Q8Mx_tqIv1AVp9MoNk27bxeHKfBAH29F-B4XTxJF_p7DIEZWRyka9Y_c3ltSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRNTyTU_yswvdq4vk7VsWIIL7l7uEQ9kwd7G3-LILc5us3nLvn3zfuW8lhpYCJkMOYqgiXBikHejfmvFYzmVJp3UEXUZLonqQyYVQHzSt8G3rj-1jicgc9YzmFO3TTtAKUyap6bLhcBj2mOelXw44_d7zwfRT5BP_syVed8XRbI7ZQBO-_bRaIAklEaJhwGcWdbF4asMyfK-RhFZ4_PFnr90Nvlmwtg9IBbebfr9vMg0jaDLUDnAx6PxG-duSbSbuX37TVGij2YwxcDsg4rF21mcS_WJZonEYqSaYKrEQuFQqGSCpIed7DLlVRLkG0oKSVyalInKP70wVPg1cI_EDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUUnlrqvxAu5NkKN87CpRAkho0eOfV93hEcs6fe9-GKzVQhObxyHid_y2XMVJTYueF0stqEEsSeQ5vIhsUciaSns5ViJ__t3BPwFbxxtD2EFxBXUCOgvbc-pyC26OEjwRvB3moeZDe2GSQqvbHzDlxMn77GICtYCzc97_yg2h9ZNNXP-WjirKq18WDNhx6kmyR32A9lH22XI3wv-F_GJqlSOUnv20IPue-vGUl1pMBSENKuEbywlVCHRe-V8oRWedj0FbR4zt7YR5oEkvtJ7YCB4huCxwrONdSUJW1vx0M72L-winx03-brifElQORfHCNiIxMFm7_oUJjFIlX2HFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JK8N50gtltbUK4ihwIgBNde1pR8o-LuumGpFYs7_JSP22IJjzU8Q7irjM693jx2_6pbqy5M_VppuLsmE_fv8ftMnpNsXyV31OjHTZqCrCnVB26uWNfdv4qzLijoaFAklbcyOOG5mptrLOgmBslqFSyqyNIJsNrsjZR9Hrle4wHPEbtg6XmvIP_U8qxl53YfeiyVSDu_MNcMK5JDWlylOE4seRU-oO0F2uWKd2PMbvAbEidlxeF7D3bKUgk7E9TF6-l0LQLv6b2ElflDPB-OE-FpRh2fv8fFgEGXWPXbtFeUbEKprpNwUy8n-rpdNzZ4Mz7wdU6ASO1txbd865LedJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sw8UPvFgXo_M1Qg8ZCfbgcJjwj1_6OndYcBSgBbA-JGVf_3gjEErAw_Ms-SizIbjB4ugbB1oIGggttNTUTeTPw6HWPmOlSpA6nBregN0oVeZK2HOLxdNgJF3hYzQ19lsdLlCqxN4Ugspj6UJDcXj3UcXVF3f_jl9E5H_yQU97qnZ5NNHBvMCQFAKKFTOcEsQiYWqeLQU9Zqoxr2G51z8DFgkU60jf75BzH6zXkscb0mmIPsKI82xpYoekyKuNrs1MfFEDeCDS5PWONSb08Ni6Qg3TMqjhbX2r0_LNYeGXDA1LMPSVsWZG87adOjy4j3yTsuGNyJvDyCfGaIlyamINw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=ON78TVpxck_q5Vw9B4G4tJxsJi2tx9NuD7FaxsYSh0HUgm9o2NajLVR2-Hf7RSeY5DcHIcmqUiB-ngKCxUAVw4qarjb7t6n31QZske4yCG2J3-iGpv-lb5Z-gt5xOdO_jCqGhF1aoWt5FmFk-Eij47awTdDJTOvxNXyeMzlnHqhqdi29ababsSYdNx4wBRWXWmVDo1Z3qif8P2btlwUSx5hzQPl4mMO_SmYiIWvNMHdgp_1ycXIFkwX1WqEXwyb6k5WxmSPdcHhP3MsM1MAig2NETRFsyvt7OQrAZtiaIbxJfdk8xb-p6tENRaynmEEvGipx6OKXMp2d8b7T_KiBxUMcCd_duozCXUy-QKlrdgi3aTNJYi6RFv2M4w1RxwvQGMajruNNb19TZPB2s24UjQp6-cpBpVQGPxP8gVuVdqYmHAqLOHHI0WOwv5zaHL6Sqa_wgA6NATCxea7SFy7I87r26r9s6PG4pLlH7vH2xDPfWyQhyrOSG47RC5g6lk8gTPzwXImWHaa4MLdlswi__M6ZGfhyJd7Jnc9lP2mjuNm8x0Hvn0iQv3FQGKyA13_VCKflAKm6ka56hACgVXObxVlduyNsyH4j2pxWz6T96AAxv8FczCW-dgqjaaZkKfvwcK9akS1CPCs5bCqmlzZN-n_Z5recgMnd06ZigHgkyoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=ON78TVpxck_q5Vw9B4G4tJxsJi2tx9NuD7FaxsYSh0HUgm9o2NajLVR2-Hf7RSeY5DcHIcmqUiB-ngKCxUAVw4qarjb7t6n31QZske4yCG2J3-iGpv-lb5Z-gt5xOdO_jCqGhF1aoWt5FmFk-Eij47awTdDJTOvxNXyeMzlnHqhqdi29ababsSYdNx4wBRWXWmVDo1Z3qif8P2btlwUSx5hzQPl4mMO_SmYiIWvNMHdgp_1ycXIFkwX1WqEXwyb6k5WxmSPdcHhP3MsM1MAig2NETRFsyvt7OQrAZtiaIbxJfdk8xb-p6tENRaynmEEvGipx6OKXMp2d8b7T_KiBxUMcCd_duozCXUy-QKlrdgi3aTNJYi6RFv2M4w1RxwvQGMajruNNb19TZPB2s24UjQp6-cpBpVQGPxP8gVuVdqYmHAqLOHHI0WOwv5zaHL6Sqa_wgA6NATCxea7SFy7I87r26r9s6PG4pLlH7vH2xDPfWyQhyrOSG47RC5g6lk8gTPzwXImWHaa4MLdlswi__M6ZGfhyJd7Jnc9lP2mjuNm8x0Hvn0iQv3FQGKyA13_VCKflAKm6ka56hACgVXObxVlduyNsyH4j2pxWz6T96AAxv8FczCW-dgqjaaZkKfvwcK9akS1CPCs5bCqmlzZN-n_Z5recgMnd06ZigHgkyoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvtagYSUH9nYIHxve1K9ImTc6-rs-xe3KI-yVZFoNCOluaVhOKmIA3vifMi-v7SlnUUnIpxdjsVVsjQ12O0UCfnLr28GaE29J52IKXH8SGBNXYYCjX28YtdulvMWjiVVDM9yU5pq-zMlJoGli7ZW6dTH0Rp4qcWyiNRvxc0F7ddjVd4cNVCZRS1S-1PW6iJnvt6RFqhg099kLmKSdxMu6h979LQ60yiofE1I5kt5ez4W-sd7QtNGPxBRXwjKQYMFYJisImhWLg_sghYuHoNJ3uNsfaMd1DYUx_o-uR-Vxzx-50AJjocFqcJr35tsNDeymQ_Qo_IBBhU3gaj6-0cUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-wV_FNkSF2GohY_Y1h5MMKt3sbWgCKMkB44ujjFT-1ExoST5Iznj41KPD4wJH7OhRgpmdYWQQcOFY9iyUdn_3kf6V-1MPtWMUSPyYG1uTcblRmPuPgfkV9r3-1sPs6_GLHo0PnmWqhRCprjwLhj1EspXYRl_mh1KJan0zc2sGniDNYYdZ3DWG5UGt4DdOrhZRBXX-dxaLrIzanLqkjdXLcLhWKuD2q8TGOKQCHiLqZAu5CT7zbgusehIrassKwUeQWMjQngIt21fcnLAJkEsoqyOVQzZJaG4iM5mbzykClgFYCSLdwjoMZJqLmj36T4ZP-hBumiLDHDSyHHUXF1bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQXty3Ht1JjzD_w9xAL05TVQAZvOoBpexq30cfhp8c-lF4o0jMAdCBwNJclt14VDw3kmXzdisg6h-jlbfQvkFo8nDwx4QDq8AxDyf06C4Qhb_LB_jEOKZAtGNrWFfvmyw40mwDHoK7UsnWAxBrvuydk3kgs-ZoFpBBwut7YqHdFX0z6tZN-5HKe2bqm--bzwTolJhitxu7xRrTFK_qbSwRbW2uSFyARgYaKV3vxxUQZb_kRnzUxGphsKhKUTjkBuRE8pg8253IKZJRZ4ll1mkSmjtx61us1ZoaLT-PMQFWvyCdZrhk0qshJlNu6GVxfsbJji29vg4pZv1nPJiBw0JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyZpInvGdL696ZmTpS-J7btjksCtbUN7gLp_AJqyihDhfrJFwfINiqRS-hyMQONKp0F7dM8HnrtB8HrbTOfeW52AXYpHm0gfN0HU4ahPy3ikmVhzq6iBhLtE0TGrGta-ri_IHdC1gNJLvNYeUumzz533U1h4JfjzoCryDTwq4UBU1YbJkm6bvbo3m1xxFNhc1N9TLew-8rvzvj7fDu7noXbqK0pTe4kbGqAQPlIY91u2bs3hX27FfIbiSiqy5AN37JAndEW7SwNofaON8Bo_W27lj1HIevAP-SpoT0yGgcYDm3XiF2TViSCN1HRpzaWK_yvX9lGz8UnBq_v2PVvKcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqKuEq2CR5FNCKj2HvlP6keu_FnoSCZIuvb3IDf6QSUPmLPQom69Drf7AtZdkWLU7C-ViKSJvFFEj9u1igFKsYUkcRkc00pmEHcBSdocsJ2B87srkM514t_H302cqwhzUFURENP5kozrOIwL7dMlniYjI-XoIdcIaxrArk1HgUJeJH2r0lOJhzjx6F3PJS-F-rY3hlDX_c5RMFB1b2rGlq9-URTYjoexAODKrgdrAHvChn96DBJtALxknYpdeO2fQo8YjHp_Gl-MjOf9B7l7OMrhD2JaiGw2nMQPkyvwwQL1DM6Pnsn2S_YtJzRcf7ieRtsWw0awyuhQ86noGixHMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Tu299SMZiqXJ2MvYL6-h_tORdNP2IoVWPwKIlrRpRBzSR2TT0ROl3mFPhOLyJuoZvzl2kBtFyRNEtnZ5_6wbOR5E9cp-eLK3iwal1G_ihhqhTxcjAqOlM5HPDlOOUOkJqmMwHfbNlqAADqlM-xxxTBVg0i3-FhtC29b1LLDU5hwqkwFJ4kyxB1naPGbiP-RNUTlQpnbvo1GQuVV62__b8etC6c0sQ-nbukRPj5-hPsx-o2TZ7TbSFzYyabTsvB9rSjgHjkwanLm_41WR7oiCR04cX7V3eb3yhzTtnO9Nsl11pFA9DkFrmBp8jVFB8Dscy_e0-PvsaViAWhXNHhTImo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Tu299SMZiqXJ2MvYL6-h_tORdNP2IoVWPwKIlrRpRBzSR2TT0ROl3mFPhOLyJuoZvzl2kBtFyRNEtnZ5_6wbOR5E9cp-eLK3iwal1G_ihhqhTxcjAqOlM5HPDlOOUOkJqmMwHfbNlqAADqlM-xxxTBVg0i3-FhtC29b1LLDU5hwqkwFJ4kyxB1naPGbiP-RNUTlQpnbvo1GQuVV62__b8etC6c0sQ-nbukRPj5-hPsx-o2TZ7TbSFzYyabTsvB9rSjgHjkwanLm_41WR7oiCR04cX7V3eb3yhzTtnO9Nsl11pFA9DkFrmBp8jVFB8Dscy_e0-PvsaViAWhXNHhTImo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
