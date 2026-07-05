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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 19:13:36</div>
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
<div class="tg-footer">👁️ 108 · <a href="https://t.me/danialtaherifar/940" target="_blank">📅 16:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 353 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAyGsqwbpokvrjoakSU4xARjQ0TLcFvc20umYpP36eB_VFBEFdEJifP0-TcPAhR63t-5OKpiKxpdh7670pXjRbhMT3PCgMnooTvliYoOzRlgPYDPBGFH57kuXgOF6P1NHEQa5WYDli7ZRiEsy-4JNDfBO5H8bWpo6fd-SXwlWGDxNlAjVXW-RDin7AepRnG4Z4JbQNSbC24vGqvgcmbxDrMiQled8O_hqsut-rqGROhKVcV4vP63IGYORYj-Z3J5innuvPGXDJ7-d7KHK587x32n0lcvDDOoP_xjLv9o80dN6bwQhgmj7BuvynRVS-_elmnAgUjcIFdG6piIK4nhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 561 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 714 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 788 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 645 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 727 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 866 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 986 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKagFrykCvSVnJantoOPMhBI4ErK3DLAPq5LvNlEtEr7yHVvkMG8wPPdwVI9bFxRrb7Rz_wd6Vk7Jskibr6kq3g18V412BOkgvma6OCTzSuhOQT-kuz2HS_51aAYfDSn9XTJv1OCCxLJzrU_thl4UVSnImNsg1hVLmFJzyTEE2v0zv-YFFyOv1uOcn24XR85hWOIZ5YmmUdlYp2-k1QyMcYYxxrgu1orIQqHTgufQfxGmF2ZKd3ZxPS90P0C_oLUWsAeyMAoNR4CsozqSAwZCCHmL4Xsq3CF19WsOarVC9fOjp8pYSLPsPLgVLx6uDDece-Vq0rqd_90P6xo-83ejg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4pqIEkiWAjVU3b7EF2Bp1-LTEAxRIrkd3bHRfnjn_19U0Q1QYqRx9j78Lc7VeZnHiUiPlPvk97s8dhFxDEXLD3T9RWTAjFd3c4nqytLWkWK1Nc6SbMM8fkY8BitOu3_ITRIfsffLx1Chtcoz2pj7KXNl1tDVl3ApO4lqfxTQaBykQe8IEvp0Wrt1ixEjrB5-jxgNu4Lfp1S7cG9VHu9QJ_4Mvt1bvzPY1IA9pofSG1tQSnvJW9Mqx6RJajY3_XTZgu69Nxst-FWrGqUzz46TDOEvjouaGcXTLQ1SlGEpRHbhlAO1ENPVg7ek6PZAkk-CJDw4HGS_fEdn9XY3LKWww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBl7UhgPfguhlvUgSonhnLaDEV8dXpDGAKFNBc5ZddyiVxg140idjg4jXz12gDaiHWkBN9TGtsqQlT_eW8FH7xobrkiI1LRppWzGE7wv7KUSq7Nr5l8kqvspFSFMyLt1e_kicdX3GUwN-M3MVQWTbMuTVDIW8FLtNO_VlTykIQEeiM4qsWEBQGwQ8Nb6O0aA3dy0JULb1_xxpSjgEoRF3A5LfM-XSEP8u7wdqfYRhFmTSSWkW7428IpRgo85vW_WGkfGOEabxiCx7lUVmhk6hLKlRXSHwLvB1s7wyqvGXZNiG8cNTytKLPHW44gbuNpnNHb9o23E5gyqf5rrBLWYtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzZKk5Q8MN__HKOKHoJIE41E01sTVBnl0TFq3h0iLiuLMeEPw-QgquhoZpWH8x8r6Wic5oBXmfTvBUtGBsSQ2HfPt-yKuebfT2V1Sa1V_59ESPx_d3QpeFVZkyl9xVrVce78xeAeFMtkAcxWTzU9exTWkdDEs1H7UBXJG4vBSKAqVK7df8MTAPHMgJ1Wunpxu8g7AFKuTtIISPddlSxGhdSrXRRxwdJPnnfwrrQeZUXkJkigQlahchILR693pXAICu7CqFPdd9evCUf9WuZcTXMnG9LJ3HTk97zsUM60S0JZDGuVo0WTHUWigfHgmfzU2V1ieEoFWxiHi8SCTdrggg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMvhLCd6j8OI4gUTHQFsrzMNa99MZpu0zVsH0-OAeP_kwN7A6TU97zWaPJVHayCj4r15mMRHfy3x3Modd8q4z1axBfe_GVIVNPQFewRu_LAfMNSzU0wDuNbqd36Y7bdtXNHXT4882v9kFSPkbwk0T4olsr9BpjmBNtyFA8tLW8wpisaod4uXq48V6XHeSkLScmbMbEXL9W_chVODyslSyEaZp7fDEZJ5lIGi6yQfFVD_A8XiJ5ePlv7K3w-YituzP3IIhURsE1lNX6WHeH7nnQJS5-e1KnMLDRy0vn2tsk8bj_rZtHoT1n52G5hT03mNrQKdNa2H-1jUDEPVYukiDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqaYUYrIR4yY-ful3Ur6qsXRR1YzGN6mdBZ8rqAQB6E6U9KGfB7lh-RDKf9L9ZScE7tbadGmuSXNJ9M26dlOIvDMwFwZyxppIkzBji4x0i823sECYoJACAR1TzkCHplnzhw_PObPMMZQ7w_lk-KV9oM1XMoJFmCGOOhAGYp7hLjCzCS993Bl6BpPpfeY9TP0TUblifKQ8S1fMsXbrxGJEDiDGhK3iD5p1zhIvtBwdL9-fKorlwUkDeoJwmJ4AGrK8L3WweZEf3aSudLN7UE8NVn9k3GHyMDdJfecOLo4CCLBNB_q-doZ9tDjTFjnkkaZ1SIm_UxxeDOUVkmELxKdxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaIADfPQeWyBxmFTzFGxBtTtRGzWFKQag2rUEzEsvNgCT2wC1qHTWTFGlrsYEEWhq4rg3xa8385yEkrxTCLsFCLpKlS2DYBeu3uQxukC8ymayLp9X3-SlsHBwQpi7L9BizsIWbsqUDGav3ZES0SDq-cTym8vaRWsadTHXxhrKspWRxi0cKl8BX1-oI8MfdVguxFwC_rYRnEYp2vt1tci52lfjR-dp5MlMnmsqmd5_EaAVhq8-re4Subucw8qCVnnGGtTR5xIr1gHvoSSTxIeZHGcTw_04xBT5yNwm1e_njpAZq2aimIgrpT2WKuOClp5W6Kp23wPnWNxm2JezHjq0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUhYByh6rOn8K1I1FcMIJ_J3Fl45Bh72VGgfJ-6-xOz3Wp4OQH9zE2b-KrJMHBiD_pKO9aw6foX0BtAQc2Lg9hcx-XZwDbRf4l2CVteJaCuqy-ejfaKvvE3GbWp0NCiadU3Zm01uyZXqmtN8OyWUqOdrjTe5gi4037Wp23Xaqxw80ibZ3lhHLR4pGU_3I5HKvQeJ0p8f9oav7dPX9BJmZO_yahyeY2v1zdCXOUoeRm9As2OpnwuFBOXLCdK9cH1AgkPtRgJUs2lfR1OIseOgG_voCxADVRYkGgfbqWA1YKo0At8xglD8VppcZJ8Qjxj-OAnbAoY3TzRFuc2SQdfCbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3KbVm4fo6kHeEI9iPRHwNYKl8CqCRThZspbAW91ZBM-sSljzU5HFuLBPB2mPXNT-jU9UE9B6ycQ5UavCMw6YIcoiNR3X98rl4UIWwh0OiaWrRGOEk03gs29PJOE_8EIKRFEP8zIpJsyJpYUARMFzs8K0ia38MNfctyK2YiHfTwSSW-whKeXiS6z2-DVWSmcZg0cq05WtDaB-Q81kBkNBGJLczhJiDX7fdgbJ63qzgYc3i0tCc49zVahd2XXtYJ7tNemBcAv2xNxa2cy3TUxnrsFqtUi_GspZ-GS9r2F59OlzxaC7Fo2HUqzZ83uSZEzpVztn-nQRX5J3PaGt5jdlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpNBjZpDyrHbf_o_AXcKQ7r9qk8rYdtsDArw3gTGsRZYi5EY2a4a1OUIDDMQ4qEF-ED6ttaRqprofjkoBGP7dtHcWq8ZAgOTnomWax_rqvkD20vPNcBU8HZMnuXNxM2D3nN2MzNYJdzIlFDe6AzoSrEB1o8jqCoaY0Ghby7rFWC3zLSuTWORP9jsJJafdtN9pWtB-yFv3iiOabXEdVwbeCD1QxmlH2tQE96Zqj-ASyHViW0QiG1eK8BIPe44QAi788VbKwamBl_VUGazjZ6OPxN5vPoO55NZSNn9M5_99tmluyK-8ygSrcEQ_IwCVuLgPjB-NJJvEKL7quaugW9_2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7vCxr_EmIQwRQ64vUQmY4AjSOi2MK4s_wJrvIPdhyBz8lAmebwY9DNNILl9KnyukgUmJGDzuWW8jPmSZigASXyOaKxxj-uYZVg1FdJnXjM2NdCgVUShqZRkhdx0GgMoVpUkjGmZk7dNwT0WE5i2Fq4GDiPEe9YZIpiI7Ye6p8Z_7knLjvAUNL8MOwaItHQK3_4lJdkHTzZnLkbemWwFUEq6kdjpuuGC3Jkv9sQxDI0OMaEpaCtLIGjsmL8rfaVszxkNIIXAKkghlMlSm0sMDlaCyUuiEqUljtbgpbwiaaSAQ62xeqjtLDPWaUr-VCZffN957dgPV0Z8Dv2AS3cPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbqpV3U3Q4PwlnAmy0iFJ3w-hUBtSDHX0crxt4gCRi-IlMHLiaG2t8tq3-tO5ydpxCgrgQ-oCtp07S3_rh5LSDCEaI_qhP-0SGxuFAbI5C_SJDyjv8zYBi5fEXzP_6op2WoX_RA5uFupeVe4tgarnNhNHDySlnS3IXHH1WQCrTBDQoMNapGVrfAWHNqxobFmUZDVcWStmLYmfAbMU47BUuOFB0yM2Te_tvRrZ3vfF0FnXWKoVurhSC0Bp1K3zEbSJ5lOMlJjlUQn6XrKm2W6RA5_fyFTw-qM32A3wqBOZ1IHkW_bBsNBJsNg1mk36D6CQk2d8kvOjMTlAQO5pcj5kQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HERAx0KWgS-1i5mv4YXWHJ8R0IAtQaL8iRTZUo20luN9IxIASgisYDyhPuuv8Bgn28bLhqb619YJvPpkZC4GW4iWsYbKu-IQRFIdSU7QQnEbnjSx9IHurtxLHlAnUby_zX3Uw8euMkaHqeyUd0A8nH-JLJ9FWA6oxXXVEP95BF0S4OjF4zwlntnhfI6u_6WLnmtUPAwOjOF5A0fTrnw53PS9ZVrPOfDnmeijX0g6ZOsqiGiMCw_wsyaC4Ndg1sT_K6BeWr7hBsHjEGsiD1oiyoKneHeUSLClPo8uTeDjepxx2h_OIgMUNHmTvofuSDVuL2p2Q_n1LA7S_xmiE1lLOA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=foX_UXXJxT0kXcfMVrMY3hffm-cbU7Fqto9k1PqLlSy-xRzFo6ffhszG8-j-968NKlq73XIxPghOCKDqP_WyoV9e7lXQ0P0Zw77wS9mTuSbzSoYUoozmak8gFDLFEo23Ibd3CxUm4qAb7FbjMDIA9G4YTaJPpX_ypHvi4Cww5uJJjtzyBPWSux1oVPRw06jqfGfP8fVYfnfcGvVrLtT8xjZ1hjzifPHqwemj8FCfhGS0fGiRMBDZH1wIci7eC2HNLABhC3BxR3xE1TpJXtu0HTMFbp9v82A9uZG0GXP-mMeE7xlbTovN054sNbrj5NfGaGps6kNEcKZDvqOfJMDr6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=foX_UXXJxT0kXcfMVrMY3hffm-cbU7Fqto9k1PqLlSy-xRzFo6ffhszG8-j-968NKlq73XIxPghOCKDqP_WyoV9e7lXQ0P0Zw77wS9mTuSbzSoYUoozmak8gFDLFEo23Ibd3CxUm4qAb7FbjMDIA9G4YTaJPpX_ypHvi4Cww5uJJjtzyBPWSux1oVPRw06jqfGfP8fVYfnfcGvVrLtT8xjZ1hjzifPHqwemj8FCfhGS0fGiRMBDZH1wIci7eC2HNLABhC3BxR3xE1TpJXtu0HTMFbp9v82A9uZG0GXP-mMeE7xlbTovN054sNbrj5NfGaGps6kNEcKZDvqOfJMDr6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFHrtayiG-wvVXm0Qj6WMCFghOoVXwJzBVnp28Suz8w5HxaKriSsFYYyGFxH-EpAsJJfxbjsLii3zgGAL4_y-eTDezKX01FXk301uzUwBXhHFvVela7ky363aztZrApmKSSnE2zdNPFA7Gf40a_aHWu-I8-iTmRThirLA1aBvZ46KcqifKoBGly1uUyNmw0MBLITy9yxvXVyNByUo-PD1UBG_84LriRzx-TpMDQr24udYd8N_qA7B0Nb-PsNhLBGCFpPnguQKbkC2Fx-e6XfvuqMDKdnL69ULvyQQj0GUbvh4L6xZVPNvtJ-izqGBjLO8EVhYGCaJZSGYkdXhqoH5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEVeb0EwzTWaXq6y7h1WuG3E1IO_zr1RiMW-31zXzCXu64gKnrJiGE8uK4kcOruaK27_E-icZcM3Pa68O0TAZV-hKWjxdmGQ9FdSkPQuRpD_nYvomRSUZK4Y5ZugrDffv63i1f0RtH8zS1nZ3DKzHvhfICDlgFuG8LQO5XFV1kGewTkCdeKoCTmPc1jYZNsfaaa2TbEhzrljFk3gAeD94J-1KdU_UcYVIq8jMGUsNBYrfQ6Qnnx_AXOuX6KU0DVhXZAZA8CT8kuLb9hMgcbl5qeKZJQPkvmNka4B9Fwd_tFqserGaQ7sbR7cdqM64-b53uY3Er4PdDrg7E1eFS34Gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/heRdvyWBCN56AqLfjzXJKUz94Uv_IkvmeS3-Y0zwwdeR8iDPMy40ZLqid1wREFRZbudyN3EjXqAF0zrMWNTuJZnAG4OcSAVY4gfKGqvWypZhZzKp7uSPX7oVwZ7JhO-W0OaoX7W0Yw9ac4_-pPDWYYckXxWX6huxBX2yR6oIOpQ_upteztd64m3j16Y1nALr3yYuxgf_nAIVjZySxcDo_tCEDT6zBP73nmptZXCtPRzNwbStgC_eaubtxQCekodRpEaFEcX6bAkDjBOrd0KLfSrWXVYsC1PT4dRz7TL39EzFzQWuz1V0TunjkUrzoK6rzbAzh1WpLZ0E9PX9fWY1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rlr6bUgNwSjnLLrvue2jaOOV0j6YEm8WFOPGJrhh3JIKXTZv9q9r_5OaTbX8DfAp7F6PCYtjyAcZ5Zhj8xQCZXZCIvxhfTVWnoXSniovbil3pW7wwOW_B7taaLE8LMYEgz-gj7EUTaBVT90uyazAxQpDCYzkCV8f4GVoQs2Zm7Z99dPQWAjCSInHz9LG-MhKC81tTKa8fxxn0uOfmvcRVMD8xuABr4_ZJRq6pVIXTiEuS_7cnSUIgdvCHjS9vB3zpPrNewBAKqQu0ABoUUmMUnuJaDJuS9VSNWozVPcOeb190N_0vIWFbjenawrqHhMtHzGYDLK-1K0kvhztfQmK4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ku1YrdJZTHXbYf1i6nQHd_TOGBqXYnc6sjtD4kbfUxK9S8-SehVtpQkhhUnfzi8P2vsxYUN30-tcvhuoja_GVXNUFzPNfw0MOtER-fMnfIBOmlxddeR0lB7hDqZ4NnGfUJVbGzOcmlMtDE2myDCj5DpWGIRlorv0LKRYiq1g74jQGcgpW-eyKVyaWPKekgQKBnM4oJySbMRU5NB_5jp2hvnXuHjUWRwlUCi2eTahCsgFDGz6eV6xd6FfcUZM5cY0DnhgpGWnYdwmGCV7-4buoz1-Kxf2FQP2AJxponvkeJBMk8fAzZN2cB7RTAVhY22ybQsPXiNMxrOQNr60zvjojA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKoWWcu9ykgt0-u2sfsXJqLJjSE5mXrXZwMiN_8qKczxsZegnByWv-b-G5uvtQ4Hm_unJj6hPEKXLGuh8RWSlY9fu2WG6f800mif4rJD0ZhR391ZRGMsJ3qz3wk6njAJeQDufOvZb5YvQp4unm3b-Fkq6RVyfGRXTUocZ7a2TXL13zVvxK5MXtElVQ7SCt47h6VSXi8hzVtk6hmBKT4PDP9WPNTQ3da4zkf1mV-ESPo2yGGDBgSlaJBCTxqXI_sgtRmV-s1jk1NPV8oUM5Zo56sGiSExPAzEySfkpsdPP2ahXabyp93RlbQLZX3Mo93KgzvlTqYG7tEqwX2yYZtiUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHWwKEER8YT8oC7SNXCJ-NVI_VPeoMtVjk2D_LEAkY_24A097JIAxBgLTRMZoAOI_cOp01DvGj5YoDP-Ye5XW_uH--R0wKuQYiqFRiPOKIFhQRcbEOhXjm9UIn6qBGFHnFMlIUmRLqPeEJs88lUELeHlhmu-Yq6gN7jO6yPmnzyzz3m679kbQ8oKJXK5IDuoWvAt1U53rDYgwsmhtqDdZlKvmshoOAE4-defOVsxchoV2kFkTb0_3EZebQugOZ0hBuFgeJU7R5dFGHXPDsJLWqQOilRfC30mY_cdWSLfOQdjQ_5_fLitV9Al1FKzEWdp6cPJFmYqRPIi39znPw0D4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A30gylr0Ops_mWeICHRc2tDKL03bAHo8xCaR3mhYr-8WSjhyxRh1LCi_KY_0UDRYbmKrOO617DPFnuWnNouKB_Bc-pU0KDvpl8Tbvr8y3Xn8akCabGS7t4R2hsj-yJDTDrYZVx3XDk4FCb3WWx5WBvsb7NIbajABGlmqEMWmS20sdT_oWmCox2V39Oz0Jz0VpHItsPkfgxzOquFXI7x44Uk9esenAVa1-O_P8dKQUDU4IbF8E5ASu5DO_QM-SqY2X8k6lPZUGf3WiVPLFER95ipsgJQp59w1tiht5TS_8tFVhfI1a_76olwJq78OZDmfiHqlBTZQcGV_4f5yWoBKGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbhfopESAfnv_1Xe5ru9tYLDYHmvskoTT9XNw0U67rBKGQT01auchusBKmtpp77j2h8eXdbhA5FGhOzV_F04QPkUGGZTeTiwGY4IfjaHVjXPbIWerciCuguiWwSWPtWGX9KVlED-_CTmcvhre7rrQktHf9BeuBkPjfZrCVWljvOjKFzjMEUT7MXP9P_DJ1JS9R8zq_iDXidrlUmarfyHJOcTrsJh1-24sojUwRqqSNFeG8Cxd6pmYo8SBFxE92pOAz8UfJr8c5Rfet-DHvQKQF51OqivO576rKUIo6gT4vj7kbl93o9R8z8rywY5EZ1q_QQ0LF0CcBM5phqpcZkSDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwDlP4KAr6HhKFen3CMxy3jlnkM2-q2nz9ckWI97RuCbTxOVtfQPS-1GtOHjNN7I7z5d50lbC_E4cPWAcF3cUabCTS4g2LdorabV4DygYTOjeprR3U2EtL6yuVdeG3EzA841EEIEmLeR2YHecYEIK5A372vpoNnNbVfMiRlaOUvCpKdMouLj6ekErUwfkDLr8k7nrpYW32-YAsGWk4e0PaCbilrgkHNcTNBMltuJw8g_iTPNEHqjOJS6UY3GGkNKIZMjq3MtAfYbpN7QmC9XrMMrdgpB2Qz2PUrNk18y6lqxXBPcX0k12UUyimfg-wETWd5dsoBP7wxOAguP50XoSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEJo_K5XnvRHa6lBKDFiny5YqlGqIa3N4avIOoh9A27Z3ji5d8MCLWN0Qbh31p5GpKtrcnZ_fl89bQT0zpHHlZ0H3FHtgcWd2qbe5ScpnVchtbs0Z38RtTqeFVdmOP7sd1R-MWlRU75Box2bwmuNZzfIfgrtfRoyQHzNdvQHBh-HdBylCsrieynbk9pSMAYGUyRpSiSEnt22HifBXyvAm2O8KGk8xlvh9a1G5mN8WniDrNiEcuLnCFIcgMbLJRjhJvGVitwjQMO7TwaQ50duFsNEK0fG8EXdF9bXnBRso0PUDxYrrputRYCLFu29BhZ7aBtRn9tm52Vc1SOv7kpATw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ3sP-DZzuCjmXmRxU-QsP3zYdQe81oCewiidRYcZNrMSBWpDRup6YyY3Yn_pozoW_l79fcOosEP8PyNX46zUvvPAJO66f3ys-w_7dQJSq7ODD7zytNR21o5tvN5-RqYtIZc_67Cr2os7Lcmcnb6qfAU1sc3fqArnguh0FDQW3uvvosU4k5QHWIEkx8RSRoDv2VcCti_bE-Zs1fHwVkZ3qZVQAtkJdlD6RwzHOIv-qtcQ_DBUleKEuQS7rbljVwK5Vbn0aOhXqPdI6Z7IiH8pkyU5bx3wHjwLpYzb9LDCxbZ0cSgYHTESeet_xFVwzzmpYTYU-OzbM3CgJ4L_U7RmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AC9DzQCU2JzgrCR6vqA8wwxXqTfM2co1fdolA8yBhR2GK9WtyWmsNW8w91A09GzL7Mh7kXFWK64yEcoWHaXfOnBNmVgbfUZLsTdiDdVl-ySFsaMNW9DouTEFodrW1pQ1tAWY1NS1xc2XW02tIkRdKuV5Mxe9rF2svOpLHU_hSHiyLc0uTg2rMqPPb53_Tp03rYBJsMNq5bwpyVuk9aEsSYLRnO1EmdhtARROuqTgvMfdp7TlADeVELs8haKGxmdk-Yk5aYAL9Znuprh5mW5P_jAOeRCiYuPcWErAfl06xsI26BrzakoUyZuOl2FuRkUZW3P8U9D_Tyh0m7XG2aCm9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eL2uIz4yGI83Qm538OI-e5uzTAjJIwA05b_xtUpXJD80AyrwQTFMa8Czx7voUUy6UHnz0Pp4PYQJzSZEwSc_7hZKLFjAyaRxD5OJsUv3a_ki3Zd_h_l_WyNTSnOh422CgSCL9fgOx8KqQ00xuBlPA1hu_OWuqcZs-BGTVnSLU8pDncNmL0CXgCPAm433dtDZDpFELUIQeHVcRXiEnP1B3ZahNiIi6t5QmnDJGESwVfLyCqrKE_vs3iUoFliLqFkpB7ScKFwOI-Uyh1YirtK48F9OPO8-nzJMVEqlcsINNoX_jJFsGDja-aWPfovqVV2GTbfBTc3sM_OrVKGVPxVoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PRGzuopm4qIwYjLqHW5WT--Wgn4KtP2rqH5EloIknIw_o9auySgxcc_ttCJrBoP4YX_xFVIJoJgjb2r19t5GJlnuc09XuG3OkIHAe9I0P31D5rkTpi_sJmIMpbuI9Yv3B0HcxgfojGGgClXy8vmNfraXqOCga50WBPHnr-o3h8Kj2s6BBsWnVzaAZQoMFqwER7nqmqrfvBXxGQYPT1g3mksvvdrF6alpjpmOOWmT-9pGDuxYEnjhxZejCBXTAsmVxTlTtx0cvFdIWkZmP270AlYpwyQMUd2MwIc-HVo-QcIKso4IyFB_Ik7FtoFVWcxscyeYzChbjAPf_EshdXzdNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3SRsaMVDACnHxcpVFx5QXNzDDRDY2J8Mjxzw2xA35hYLe_YyhUc9AavF-WFZA4NodmaUZ-_U1usjhcIL0H3wufdx-Kj7oIlQ2Rikypukp37LxTLtbPK5vZr-MtACQCd_w5JJFgutiJkYt7bWpve18OOTs69qoV8keMl5TcMypJJt1wfu0VG501Rc0ZKZsy8hQz-WftfJ5UDSbHmVa407lNLguZR_SyjEVmWr8Lr7aJEsG4-7FsOnMR1kSZUO_gh534EmgTpGUDU_p_gomYTg9mnK4dWODlyjjzpF9TMpW-E0WiNT8BE42sm0Wa8fzqUEo0EihMq7b8FZNRIqZ7aPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/As_bICyWxGxI0giCnfaWGrnRoOh_pms7edAFKTnyoMqwF78RPHTwg830EsdkQhdBzvfoMNGoersGPDyNF3V39niUcnmGKwfAjQUsey1pOZIlouzwqABrynDpuSlZ6DiBhifV7GglvZ1zpaxTMcVo4_H460KPpkS4F1SyPwkhkeChH7gEiyGTjSKHEJ14naA_O4YXErzAG_dhvOWdwf36VKoqYsklKsZb1iXwK4oC9ZhSwD_Y3n8_bKAbHM4SnRqz8TVsRCRKl8pETUHNs9UAtsS7Z4WUJuGtCj1AXJxYI42xYtfql1bUkzGcaMHTFYV2O8mwZu7eK1Y_nHVGCsY5pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwo752nHneALTfIHbwwWqlcHnnIJFaiyliPSW6h6x433342QYvl9CBOQNIkLD_GvJrz5DnxDN_bdZgMVIr7E1Hw-7kb2xd9D3DvNDotPscsCp06tIocwPMWXJejEo2yaTOXm8LtI28y31LdtyNe5tdlcoJpRLJZl5pc8Gu1fKzdpgguhvALr990AEgqFp4VZbE6a2zpABE5YHQA-ZW4JnWawUbJCcdZWfq9LmNZOKCQxcQ7_TMRxdj_XJOWcmRniDQDk401JiDzw0IvRx6oGVEy1731tqqKT08Gy8jMGrpCdyKNSP2hjLs4-XOGal13A7V93hPz4UPfoiJl6lPISgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak_LFMkLKPJpy6vJg__T9JqLMn87-b7K0JkZWzEOqpMfi1C_jQwVH2HGsw6oR9WRL31t--lARdNPEyLVT1xqVfLVxt9FiYpSaIA1lsbSpmqJ7MGqY9HMvuPXPgboOCriLfzErR466wokvzKhfj83ThrfDegij23kT2ZawB3WqcJ1nBC3gcbJBpICXF5JXQlZHGDmE8I1bH54UF96AlPFni8duAprXllmVsj6jGXa5g0SG60oUTAM6x_wSBDTedRAqUj7v20mFH4gHJGh4-6g87PwiLgkTM-w29wWQcAGq0tMYaSxZ6191R1mazXS2FGfjotY-DRk37cEFu6d4ndbyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqmIBcXTsLugbtx0malWB7dgc2P-9XbYrFNFIjLqFfc1-6geOHI1Xr0cAWGfoBuEh3Zhjf8h_6WGly-19c-mbMtkIrza8CQpDI6pEFwLtlj6-LlPk7Zkuw8glvX8xgpQNdMj9okDL72S2uw37vpLfqPMXvzXtE4AMADLgnieuK-vMRV3-9IcWOP_xb2TOp00WLfPWXbCBmWo9PSOpVx6-3mxBmC6YKSMPXdPO0n4KSAavDzDSX06cMU5ZDglLs7RaMAL1Ln9FYQmN8h_VN8OjUlAlBizHi5DlXE_jpuKiL0xTmHizkcXSmzO5t4Qmv3Lkg-8sgxM48yDrAy3CbNsLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxTZMvJj6_PjWDiEuvJckG2Yv_PqRS-LxyBaq-NyQE20glfFO2Hvh9aHoOtgtuwWLU69f_lVKiQEc7onw36_6Gf7qsjLSlK3R3MJEAgUL5NPxX5nGOJFm90xJ9vvasM5fFpcPtazfBGxazaRWkLDiqWNYU5zOmgVDFikq8xIFloq_Ku9YGDqjmiaXfNJZMaD0QrtCjy0p7mGjhkUlgDqFQzdwUQZwEV2AzhzTZ3hQ58Toc2h3dvdz8mXVsv6sdd34rhZM9wVBxEQFya1BqMnH8z5TZn0pvymoitQcGuK-Lvm3j5eBbJPkS1mdJ3RPWu1SSsV1VZ4xBguQjUApsMeRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRw_MKSojmNLBbQbqsnvZZXE_D1CBpvblUVpr-IhL2xPGEhQSVNQdgysSKK1hUJQ9baNO-DY3ubCHipteAeKmFawEU5SFX9B8t93xDWo1yHVBWucKmXncdg457Yu49MDZoYFnJrNI24snbXhuLfN5nCDVORl8D0UjsNuEnZFwpx_B5MLUzhvu67gGlJ_lkLpsqubNyv_4N_sqv5qYJAMQ_S2GjILG4kdE_cg0HxicrjsYWIvgpRQoJe0v6KW7hw8j3stn6orl4oSensc4A30KJvwyxZCXtYR0TCq2IyGTa2BORusySiNlZYJmgii84BtYagvJsUFJZaBiMS88xtuxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXNOYCXWGJQ9zgpW4yWu0reBtaqouCBVC7lXFVbOFEwvoYaAIL5Jme26zzqXqcGWRS-yYpFmNP3Jh0fZjkKB4xeSgECkqnyOtCoGH52q8LznFj1KAqtu4ZJvExnUg8i8NU158SSo-w2MoNTJ5lo40a9F8xE7VK7FzVvHLcelX-2Y3WY3mnxCssLbx2JpfpdgoEm5xyZEr8PJrS_hPFpH5z5pacHeLJ9BBBt_zbwJQt7-5mMNxjhVdpGThD3biVu-goPUgTmBZepEJ4DVY5vafzRiLkLkaoaHUc9ZWwhmuV6ploLXku9H2o1z40YygpQMHHzfkeXGKIoSgRLs3oqLYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/un4-axGcfK_Xy5mNDCuRiyXXoW8gVgJzgJvYDbBBj_d560oaIwYp0NDCmBLrCYpj4B8F4GUemPDRuhTxjdW9guQ-yPgWfunG9rDWDtEiFRiCI13FrHibM7WnL11Twz0afFxjVdvgIWUAp51rRlPmNEpmLWPoOwPUZEZAMNI3HYDbDy5FUuEzzJ6b5GkuT1Ez5T6YhRACU9wykcHSXep-T3mVHPOl8jVmJmB9OkFgOM-XZ_KGhEcSmu3kki9_LfE8YF5PG-sTK1Gtj6ibFUQDWoP9nkrN-eWoYmSdySYhynWMsRd5xDd8RDqY3dM3DUYPEJUHpHIE4CUFAjGD9hjZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0ANGVoV2MO_Psm6W2VUzaYYaqA0kxmga0zJ-tEf3CrKwLrJyj-6dG-GACuguXuz40uXrhTVu_RFf7QQ07VGCKsWNQov49rASupVes-tPMuCayjYTsLzpGxMN89Hft_iw64kyfc3OywpxnWrdTzn1uZM4JBoPp_JGBWz0EpPzq8nYIAl2YTcuyseKihTbuxQlg1LJ8opNzUBt5YNe21u5_UASGd1s0qBPMM52fSBTzKmBgLo-PbRey1KAm5wael1oeJkBKjs2Y4xRiHreKgp3BSjh5bzsFt3T3hwI3gWqB6aogBolgAWEKToFZ__SYtqNlCDsrr26h3vNUzupsV9Vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DITrkQNu3RP566glPuMARCYu5GRfZXChAXy_inZe5Is9Ksj0_oaKqTnnMpYaQWFE-gN-wd6qN_IgLoXFr3ahXghPboybSDVoVue5PcyoG6kRynBU3fAp58i68C_N_bajoYcDqESsbrIT85Y_8Ip9moY_uNxpuxQMOA7JV-PM3p8I05xjEAMf1alQXqCi6twakIx4ozDgTUyzX3qVrTzmgpaw4JQ0w60BiI6J0mlEokEpFk2jMFnVlkG42SBhjgRPd9fZIdlyMRt-QMnf3OHtxGZ9k9M3GIM0GJd0Hf6NmQO5bw-KwdBKxO-Wfg_P1UJQdb7u4h0XBPXdtrVJMaLapA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrnsLfLurG6z3ycoPKka_ZjWvAN6If-Rzw0q_4oO58p8LpiJ2Y01ACIxD81LU89Dbult3RK1MlwP4MF1KQhO2Q5OxFJkFxvvuWkCP4JSZIe3fD3D8Q3zxKb9iDTedDQf9FzaKVBVSLOHYm9Uh2Qf3h5EniMasABhcz6c7Pro3oNtDuuW6u-ksNts3Msds9UtMTUdfmXqOaZchzlmVKbGI7Sal4kwEYCvi2X2NDmoJ7f1Z7cJgXQ9Rwf6B91wi5sOBWnuW8VYCwxR2zk70XDrju7PyWmF_ATYrZMYXW4JnLEBpOIT4ROGLIu-ZXIsS3-u7HSaZzV-vWN2S3YlhSCMHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNnrEJKYcTJeI0D1FQF2-pLUqcidBeXsSEXCDte5eZ5Nd-Bwqf0zfeZ04VqtjKw6kWYkP9EN5dZmBNIzRdBFCPhO5quAJq5pmiaegFztI5ziZt1VwEjyuIGO4jiF5OgqxsvdCyosK8rAzYcfzNoHiONmTSAQXT61IJAIkJkAWgQtwU00Vx5--uEm8f0nxqK-_NA2bu8yx3EM3hLQSfUlz8BHHP536IOaSazuU7IeNrv9Cx7JQAALrUiHGQnPTFjom1vmpPInwPEJ0neKQmqD6036YAuO-GNvzNPnjT49S5zbZ2lGJuJWa-FZcRT-v3Lu33SjfUpTZPwO7YNE3zXmYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bn57c6iHIxiVuxD9swP_wqwbfhZRK8Zy_N8G5Y1sYLLXylnEHb1OtWXTejF47-5LoNqN9zfXl-OsR0wv1WsyBZ-BvFWYHc3Ri9RXM-3_9dXFyOZG55us5LO6pw49F5nQbt8QZS5XzqXLyUtpv1WUP2ynM5VQcSJ8H-yQwfkTDyp05wi0WD5iM0ltIWvlde9Yj0tLG7-oC5ZNHiuP2JGj56rcXsWBEqYE5ZHwfgiQu0mm68Y8iK8YAORwLq5teY3L9amNHF0nZw0mLG2NXtFCo-cjglclGRsf5yDH0Ar5OxDabd1oWfEGKZ-bYPvrUuZu3qgxHMcXtInPtKZkAaqPWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqH3NWPJrs7PVGp3ZZKjItsuiSbuyqTndkvMJ7nBD91F0eGPj5-pqyq6yOUy4oEXlB9C10XgFw9FPLlfE3nvRVScEJAHb1KnwFgOzu5eZoTVuCj6xuSnMCCwnJeWl1El-yWcb4RG1qbQT5G36ROU-a_daYqDFvmVX51HmplAoOdiYXJINwpZrVWgEo_zR3ilVbBFsMHpHddqcp6akgQ9MP8DlhIMX2QelTFye1X9ayVfvqJnTttARHxQE_STBPRIrcK32cb-05Vl5sCIjaGDfflRJvV1iYgmVBYlohIKeyXcuDsVQ68_OcIdov5TUw1TDDNB-Oc4nyujUBQXL9EyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GA6vzYvFZqRm8e9unJyuXhamkgyw2w7KWjriOVZ0jRiaoVSUuIxBuXSe6Y9zTC5QCHS2Nhe29OAwszKt_psEfC2zVEgaCQBNy-KyKwkulyHVxFW9cQJaveVMPxTopwLuwZfgSTpY_vd6J0lGO3toOQ88IMKn9WO-pjjej3dsaDZPGw7h4b8Cb4BHGbn-1EmAeH-cG2TnW8sl6fnhR1qDJcog5lnCpBaA4dGANt93sY_xC4kjiaRH-AHGmTCNmQplQow3iFPo0akyt-JCtxqYR_2LvL2_xZDZQkB8v9SR7TfzHxQVRRx_gWedye2dufxosjDAJ-U6bL_y0NCaoWpY0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfgvANLxw12bUkMX854dwTYRYf_H2NtIqU6rxDKjVRcjHZDMYS2NGL4T-46iGp6N0uh7Tc5jj68Q1T4KN53AZSsF2-zFe5RAPJYKXgPKos-Y9a0_yQqtFlTxG5-Q4NmHrQ9c6-hjsu8uXV7qSORmUPFDOi3gGkQqPxJ8AVDT5KmCQVHtiphKSMq8goiCvLWUo2iEVf4q3FywhZerlkj8ujHJ332c0dsFVpkDh2mvb5S-03-qsoNcCZUXemgLFG3__IcfB9VHo1hCm5JDBThKvZntSgty0PBPCjAXlYlgf06VXn4kPMlyaxi0-Y8HsOyXFv3a5jgQqBoMoXUadxrE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLQDKYZuWhUXMOdrdO6fejDd_IJqtdoSvl43zdUqo9NAH_YKhIBJ0lNGUwi4e6TEJrtU9TM9h-ctIpdw9A02biaa3gHuLHbkyQK1SVTvJ1YBliU_x84T6smGJhJbBi0AaSEYvZQiltIRXWwm-Nm0bjX5wQRlNbTYB1GGpBpnBDyPt1rmfe04NwcmjIWIiNEHveBlYfGHU2sPZ8M5M3ofHmaoW_UxSdAZHMFVuAWuEyYu70nOlKTPCqxJAVDQdbKU5JCjWviwxYcLnuR8c3FiKPZcmKG4n71908FN2jfBch_hnl3qfztE8YAUFT2Bf_SyyiIQM0c4vcv26ch-s_b6_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dX8Aro4JX4YToAqVQ6g_XWqNic8w4lia-8LZXyl8plRNCzkqiYC6B1ermowqf4TO4LEmaTfa1zRHN3CK-a73bylZiGtxuAr-w_eiPuTjnK-klXyK3BN3ZMSU1RIBOT-b5N4A3Vfr4YyFJXcaC2Qxauk6XbaZH1-wkJhzy3bvm1XwwohcMwBrJRQ3qM5wY2oYpVtWzT4m_nRuItlmziUFFRe9hVspXpulefxXRG9n4P1sA_Iq41aBgCkqwV3AFm2p8VueWmMwoFczS2-ymBqzUjGLF16AukDKQxAQ4Lf3iT2z0fFHUfW4AM9hNtbLZ9waiLi4zau5A_mL0FygHmlEnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmoLVEyCq1_Bvfj-peYU0NZMQMHiNy5p86VHjFaka9jD10-95vHwEUuwtcEoy0o507QthGTci6dynGi8ODzzNSppwa9clI83KCRJ1Y-NIONh_oT_z81_tKl9tv4ZjUZj7Ihiw4AMoRkK-rqGOXKCRiQOK558bqUwKy8X3a9qdAkRFd439z23knvowjGzIzyuaI_B9C0pa3Uei3qTBSlplOAfCToaGLjOhmQvYvmwso8LdZGOS1pY9udkQBUzQZJoHLNhDV4pd40N2hJG7gNWS22EmFblYaxkMEpdUzhibrSjxbouZNFYoe-PSV1lWEWzWVhihSHcbsfHvsDumxoNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rw5BIwzA5B7S5RtYrRPBTW6tCJ9Ujs_WKuk2zjr38FwaXqZKP3OTwNm2N0qp3S8pMIlHXsmFSguqrobfqGnAiFNX3OEn_y7SwzwF7NZlHXeyp90HJL-2F3b0Pa2up1EhtMaSJGAi22WmyIwKVIOLmHdNoCIxinTPAw7RgFbFxkU0zNPUFK-tdNLbuvt6J2-3Tm-tGaTzmwGMVHfy-Uh6tyoxeQxujt6TmCJDOHs0HLz4oRUSIUwC9I22nLOvWz1Y9TBxzUEEZOfApDbZ4oY8DVDsyQbGWmCD2sWus2lSDdbu4nKKx97KCPqnTnd--R6MMz0YpxDIHU9Ek57_6y32BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhHGcO8RHtaa9OaPDMmMJ0oICG0nHbUCF61n3BY--LvxKnEJPFM2PWRs73zaD5dXinB4bCkUz6QYx31ZLyPKivfy-F8k11NJst6AenT0wUmcpZMFFExlBLQKVZVAzUZKvYPihdd9F1_aF--zatdp7fjnusdjD3arQK22H1bpNWWpYOA8uIsKDDk5UPxlFPVLer_TuvbDGlZNqgE9XXi4AkzMHc7aJFCUfi-n_Dw-yUWhssVBH1qpH5TRNm-DP7G8pBfNq8qYBMq-V8XNP1GxCjMsxqVgFk7xb5_pollDrqXVGDFbTuB7uLNgNUN2k8XaqbmlYgr8M1d7h_iewkmwcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0Fw91rzlIo6SVvJ_cwOseJuO6fGodljrqkdn6HT_7nVpBv3XCg_ceSZu4JbqS-RmY8j9OHBUKmk593rraCWaRo_OHJ9kIwnZ9zw8ib18g2nLDmwD5aT7PaACcJrvuTyeCCAROefALzCrJM6gvTR5CREsEZ3fWxyS2kN30EyIP9-bREl82Zrq65aOYOC-CO-8xUzJeXgRryzYrIJ-J1d5ljmX-R5lnPVU7YUHVSOA79r1BBfQPxHzg2Ro5hxF50s4oe2YnOrU56k0VsPBnSCO_D3pf7RzpEVQgXrTSHY-M9IR1W4rclTffyTuE_GBaV2BPcm_rEq4mU0ilVutG6tAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfMyGo-lkMw00BeEOkUeCG7-zQ8aUMVtt0CtLzuEGS0Bq-PxpDdjs5IoHLkR4DMf_FgVMfFFzLZawstf7DArjyzECPJZ05cyPhcervnIZChMw1wkEN8EHnAlJ4Ib-YqGxf8-veX6MESx3yAgewWVTBMF6cBoK6tPulOWg39q8FL3TQlSW3eGFsETAg-1K64gtR8dtW2bzsJrfdRo7TAloeLhRYZvvWjLYJee0EhJ_eNUanNES5nF-EUnIxbZZ0O6gHSzjVXBSvIfWvuz2Z1mcpDL0ak9qIZSQkLUflftD6DaKr3x8lYzW7ifN1FPu0VO8pQq5kmfpPMSF2Ck77zIrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dv811pG2EUCpDfskd6j0OEOC5S5MH7oCO5e0FbLg6I-B7RhLjCCRnXRumVpTTuzmDY59qIfbXMHh1MCQTjtvFwY_vwWPsSP6_IuEaSdLaAFnVNJYbebr2z9TWF2KEo3JoqNvT8zxw_DLVIPBtB4yvuQCao1wwEsJ1NduxPXw0bdwxnq9YIUL5b7pFIblhqKUh-9ItpQK6ByfX9NGikw-KighQA-bmwjN7JQ6U6Ogxkyo5bPIe9wfyCG09DLBUEHLZh2oJbDpY4TaP4PYg6TM_qrxnfmscrCSCA1UWUBkOTanyAHyBE3xy2nQ55X06LCT-vGY3a9XJx1AEpXrntKm9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsek5ym7KyTd--bBiQXelmC-dPM4U5njpCM5W2VgBj8O8DcFKrCO9A5DYzcJOM29mahosbkcAdXe92P6kZxtNsGVvSV4CxazLVU1jpZ_fz93UJTY68EkuL2EFHrbT6fdsN5jAfsm1CSZdLMMI-Mo6OCGQ3QTVvh_KljbNKeDBme6I8DLbOXuOjiwb_f1dwqgFELn5hMDMHJjgs9Ceb6tzCTqLE9fex6DGhudyfbC-UB_r5JKtdXoWDTMqMsi2gXlL7L5MkyeKPHs8ub7Yl8uak58yJUaY3wWyBFyGT_XDzP5oS-komjedFteHZZ2XQ6RPD6a5vvrNexFpDf_zH0AYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2W01j4jtiAkZ18kLIUSvcFChfelv4UFS-ax-NySPjybTxECOJYI4rzQeEuYD_8yDoXM7jNL7fnNqv21BALzgQljYHRpFyZdYOYNWOAO1yMnMCtthc_AztGxMbRcmtWZFZkTxNjck_4qGd8ZK6DSGPPehHhu7qD9gNXF8_W13TE0wZEAQzl1rEXlbQzqSLWzHxTxrYdVdaTafCi1WAuj3uem-a7-1t25TJAFFaDylnOmSOq7D-OZvcGcH6UzDoVcO0NOishem0XVLuWRIdGG2eiADfBibnQFPMmxHfIEtFlHazJnt2nsa81o8kWvFF9n1En7IS_E5pU-f0Ztiw4bmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9SKvCIP5Qx1jv57Tz05bplj_Pj64m2qpVSXGr23xJ4bH9kmFRG4oxziQtZYgQs1kZwgqkhDVOZkyZmLd-X6sN2wadPmDj_EhiVI3dRu1V-x_rHvbHprSeoKbfcjwUX5eDIMzujglFt-AFdG7k-fl-ega8yTbu6apTCzzwmb4-w6OK7ylMReGpdJeIYFN_R5ReNBxX6RZrF7qyd1ka7kO4HAXu8lHmN2TmYC6698j4ErVKSWcmaE7Gc790_vjsQrveMM4hB_eWUYEafbR34iVlsj_7FqhOWaejPO42MA56-CwSAAJx5hkRBNrs84my6zvM21GUPGJ8U0KjfiyfbOcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aw3ao80TFxJoKJfbtDCXQvI37X6aSGwygZjdfo2A13xCYVKMgjoOKAGGcE3I3Wi-qNiPcRf8G-x1sGWbkwmvDNSYSpHV5hMCB-g__QZduPYtmMnfzIUCfPdkDtwbkr0Q6Pn0SSWydwaOQu-bdi2WMbGaY6n1_ZKMuZDTHhqMY4C4IrvRrMB-ucUMMbUpd0hIU7NZQiFfWSJhMFnb_jwoKZMh8DvDoVgCmP3GqP3HUpRAtY4ybk6dy2h5RXkim7pQrru3YQ2l7n9P3djMcKleWhKEpMrIfS2mZwNb_OUKaliVuXcs8MUvEXxsuzGW4pUke8_rwsKyqcCznoLzyZHKnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFaOGlKQjJupzsdT4aAGnPa3D7XcXBfu11gylKPVecBqGrlJHiBdMQ0nRODNWjvxwvUpvIRyPZ0CV_MKBPImIm6YBylGCh3IDmdBlpJUIg602heOXVpkejk_1s5IH-rpOgHoRzknNDEF_APPw7-io2xLRyu1jjB3z7DtUNdh9dm328O4wcXZU7OenG-zy5LL6ckCZC-uS3GmbWrX7XaUSD9EDvcXDGhD0K9GcLQTFeGyydtJFE7O9d73uV0DVTthxvaEye4XMyk8qv-EZMSs-slFdibrqL_kNSZNKH4UVhj51Pu11s2SrKEWCMMEiqAk7ig484Jo7o9I76FMn8QbsQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=MMJTQnWrLW-AquvNcFOYROQ5xT_DaIMoTbW_VhXs_68gzpWbrgqMF5ArIThjJ-lSDa3MRivFtaGhyig6AUK_DmW6zNdT66t_UTltJibzPjIkWWla1NYwMbkydohFu5VPbZEReNMcqC-WvUwrdD69dJNkWIDMUytqF3ZE4Jha3V6aORu6_r8Gqonwv_Ji2Jh9uLGAI8HwWf31QJiANlFg04lDiI4Dn6I3goGsx7oFtXWKqErhFR-v4S1C5LWDjL6Xk0NH9ee0Zm2UtsziBYjTnMdOhMJUPT5t4mGmDxYWO5jZXSqi6Y_h5G9CgyvOU4UUC-hkFasbg_FlE9ojwnyy7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=MMJTQnWrLW-AquvNcFOYROQ5xT_DaIMoTbW_VhXs_68gzpWbrgqMF5ArIThjJ-lSDa3MRivFtaGhyig6AUK_DmW6zNdT66t_UTltJibzPjIkWWla1NYwMbkydohFu5VPbZEReNMcqC-WvUwrdD69dJNkWIDMUytqF3ZE4Jha3V6aORu6_r8Gqonwv_Ji2Jh9uLGAI8HwWf31QJiANlFg04lDiI4Dn6I3goGsx7oFtXWKqErhFR-v4S1C5LWDjL6Xk0NH9ee0Zm2UtsziBYjTnMdOhMJUPT5t4mGmDxYWO5jZXSqi6Y_h5G9CgyvOU4UUC-hkFasbg_FlE9ojwnyy7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPQQYZ7NSLb5LglKHqvwdVoSJhDLNqrpK_XdNkbo9biwDtMQ6DEvh2E_xcorC4QNtD_jrkV-KUOD8t8IvYFUyLi4GrD4Vz-wj9UG9IDdGOG5Y2J4mWGpo4IDhPXUgTr1n8xWcWV9L3NhhBuEel6vcptxqiY7lF_cvwk2Oc6s9calzBTPyNp0C6-ezYrkec3Q_rfCiDWZWwR8izsNZC9iIbPvOgumB9HprbuvFIOxP6iC6YZvlK_h-G9mXjgsfOndAFR4GkKmPdd1LCjqVN3P2vc8LQKuSWBUB4oTC8sb5bwqvdItV73GjrgsRAEjPK-vzBk5s6tlJ8uMW6Kn1-6o4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZN9GjoEGj5KJhwqvjIa82Kl2wSF50dGTeovkPiLfH6nvcm_eFzqOi16IhBBbE9pXCSieZTGVevhVyKqLma4uqPFgzVM5TlOKjZQ04csPg458R6NJO72G71yrgmXwWDozf0qmSbk7Uzc0Is7zRolq9i2rQwBeRN-4QfzqjGs7cPxe1UZgILLMUQiK8hMhnPwDFzJnsN4glERgxOovGOVBCDsG84KQYeLZpZPmPQpd9epQv7Rl0W-l1-dP9UWToAh7_UuYSjFyOMCJBqGwtpB97k1Z31hUasLdXYryXlWQO7UOaep8Y53VS41TUNTPR9s12h9wOXCMklhfsDrt2bihQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVcHwcuaOlVJKAoroQJWZC9XAsMWUrFJEpiTl_iQKkAIRDopAU8gmH-1xCEsXuOMcnyL33WSvT_54CyoGgH53ON-6c-7jun38hgwgs2d03rfTqRYKGxrAT3QCXq3elkke43mL5FaiwgXDWDfZAogFy8vLdncJ8qlLylQ6QkUpMT4-nLYYL9cEXFZWM_Q6DZCosAN0rTtaJ0GHlntWKZ0_iATuciZEumHdwCFx14qGB25wMWm11Ga2uoLefXac_f4A_evA5Pnl1GqEDss66FeSNCDlTcTGqJk1z5d82eynQkNRa4bKOyrshYFGApuIwZnQWquIKoy2AyVf0i9siXc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2oigjQMBYlktj1YCMOS_8ijXwz-xAAnyRobjee5ma0QfG6e3huPInqXkNzHdSkGJJoFGeMSiMCFdJgBRTYpZWgpvUU-d9MTrVGzoIZH3eelkb7lFOvNviEuovU14KvcDyvkNMfuq47TGzEk_Ym9iAcRHddUQZ-rWdMSXHEZY77CgHyDiS8J4wO4LGCYI4xx-wFsQERH4wjTAgeCGCd9-V9aU0UwHQiBwS71oZLY3pvQudG4LhUB_56oQIvfOkE4O1IZ_lUal_9ySLQeyIrKxq56ppmtQa1hcEd_ikxUJII0S8pQ1GYZ5rIXVU4gV-gHrduxQDfJpDNFnHn9IaXqow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSCZoThWu_ooWCGLYIvBNbGu93-jIFfPmOGJBldJDAHo8iN4k9VaGuwUSf4Wb6pjwmCPY6ApvnJUCzrKnQj2-wAkLLfB7N3FBUSENmW5hciPncRVCKWBuykZcSlv1UPofionjXy3KwcEV5ejRwLBbkIAxnuRHGOAjZxq2Wct0p_r4sZICe5E5Qq0Xpe442U0CrmvbQb9VWfscBz36yMALLI2xfsc3Le_DE8NMrLIWXV2RD0L95DT5LcbBRLR2IwDc1jNAs61JYpcsA9JoLEa0EzrF7GUoauGmGAupbk0lrvHSYKqhJN9LfnP7wP4GW2wEqKXqrqfAkoaw1qtS9X07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lkQB0wyc4RDm5GpVTAnJm8cd0eGGzN4M3JnbAuB-PgU0k72oq04msxcI3CB1B6e0m-5DteccwRyNNShIQUNDtsxGXHREaZuLVD10E_1SlzIDRiwwLqWMDkkMvyioQPa5efEmPdzbQAqhBCe6OWgZZrBSCqH0URHuQYqrGWezs4Ngn9OeLWPpp9htALobxvhC8eztdZr70TVWpeReas9KBSTXQcikEmfs3opuwMvVYvXh503BmXp0J2IlcMqBzR3_bzzXHZLBZcLHNBOBrXTjyJ2UUVrhr6RFDhAQAzIPG8bh7L-pm2h9OC_lxWcz_99uJ9ss3DZrgt-7LI-0jN57Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_LWaLElc3dAKvOe5VflmvS9WWPRSrlPAZNw7bLZTTJUnWvWvVS_39SOYTsw46kx1UXNZtilRdDazft9F2Rr_pUdgp-FmN48SW1zfAdBHv8peh-RVHPWrJz5Qs49McCqKIeiEba1k0p06sIPCYqhwTmLwXYSzfxr4nboOl8SHytYi1SSQkARGMKC50paObMCDoTJ2XuajpNKVj4j21MMBMFZZIjgmMi8nMLe8ptC-10Nk58SjWV2NAzKc--ICUvEifIIiA5mWU_aX5pSpUDs2_aW9y5ZUfCbM3YTypRKyDYVmh5abA51Y0-1fq3f6mLl7fFHkPk5qkGRecXIxikVmA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=a7mr2-9BYY4G9RpNulyEbvrEeKCY-uMcJcJpR7YmVfO8hwr6NJP64tkvLmzlF8GZxILFyX1maYBS0kHX5BZn72Eg59dUB8jDTvZoCAAwiLIuAuBR4Rp5FrZtAaUU5n-EA6UBZRVWcV5QDz30ZkrsY-wk_1YcHlwH7le1qfmOrk8zOayAuU0x6-hPEiiDBxwGY9OIMimAuSsdD1QlWYsfmdCS0WXP9kagmf3x2pVS-BqP5RghpD0JBxkcizSvVyh6TTw8tC3mRMMXuxzR-A7_wNYv6YRXMSxgiUQV5b0Jsd5nJfhk5Ei-UonHWA8zO4KGvItVsaC2xhZT89VIg9ogQxuDXQDayY3y-cSEKE3T2V1ptv0n3jgmvHhZVyg8o5ozY-BYbzx-UEqEJ-HKrNgfw1HjwnchXLZKxyaW7JTs9nTDZup1I_fedAkyIP5dx0miJ-uxXfdnYVDY_JAFQwy6WKwtAUgBI41rg20TwMmItP4M8Y4nfJxPUxKPZ3WN8ACUqwcwXUKiKqJudSlmzF8cFaljRxvofxdJF47NOaux24ix3cuxLlvdHzJB3-yAiHlCUD3VaOYF0Bxg6biHN-UGiJt6UOM-WG_QfljdCKNlQGUHUC0jub9fGalYkT5MdLVmXEI7j6d0pyeS99D5wusBbJJkQx_PGTCQ37zizMUY6b0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=a7mr2-9BYY4G9RpNulyEbvrEeKCY-uMcJcJpR7YmVfO8hwr6NJP64tkvLmzlF8GZxILFyX1maYBS0kHX5BZn72Eg59dUB8jDTvZoCAAwiLIuAuBR4Rp5FrZtAaUU5n-EA6UBZRVWcV5QDz30ZkrsY-wk_1YcHlwH7le1qfmOrk8zOayAuU0x6-hPEiiDBxwGY9OIMimAuSsdD1QlWYsfmdCS0WXP9kagmf3x2pVS-BqP5RghpD0JBxkcizSvVyh6TTw8tC3mRMMXuxzR-A7_wNYv6YRXMSxgiUQV5b0Jsd5nJfhk5Ei-UonHWA8zO4KGvItVsaC2xhZT89VIg9ogQxuDXQDayY3y-cSEKE3T2V1ptv0n3jgmvHhZVyg8o5ozY-BYbzx-UEqEJ-HKrNgfw1HjwnchXLZKxyaW7JTs9nTDZup1I_fedAkyIP5dx0miJ-uxXfdnYVDY_JAFQwy6WKwtAUgBI41rg20TwMmItP4M8Y4nfJxPUxKPZ3WN8ACUqwcwXUKiKqJudSlmzF8cFaljRxvofxdJF47NOaux24ix3cuxLlvdHzJB3-yAiHlCUD3VaOYF0Bxg6biHN-UGiJt6UOM-WG_QfljdCKNlQGUHUC0jub9fGalYkT5MdLVmXEI7j6d0pyeS99D5wusBbJJkQx_PGTCQ37zizMUY6b0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5DykyndSFbozrWf-yOL83M5Sm5T6nqhRgmnd0Z75sjPzaGqmXeldJc6fXd4n_rrtuAIV6mG3VieFFnSvAxCAUuTR9oSKE3uNri5XxQW4CxBgPjrEV_n8TtT-ae8fQz-Im1yKCbtycqK1Eu6oDKuQ0YAzu_natXm_sBEr0Ekdms7hnoNLSvoBwjvr9ED5aLN6-yLrxOzs0NoTuI5NAkswVknjIChtgdioMY0vFZkFUpn1Fhc_2cAF9IuFsqiZBtRtTZUkIwb2sm7rpBKs1pcxU2Ps3BwfMBYZfB61PnGx8eJ5UCW_YiVDqt-Lje9gFC-oMai9kY-9O1UC2UNkyDn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_oNeBOibtfIWTBRMiemcN4H3-_lDnymOXFgCMxujHg2uwHl5KiaD_Hw2t_h2AMHQUV-VX9Q82J8UlrGRKoK1Hil1fuKbpyQZhgsG4imV_LlVPLjkQlAqYlQirbvYoiqweksBpRdTaiU3ZdD3NE6zOc7mRzDowa6pmKnSiJ0_iFNlwv4pEbaBD8nwCMngHLvsIctThXuXVgO_voEVjA-e2L_mZuqsB3CMQYWCxfyiokq60g9kCjIPEPfAj_ySTVfSUaj7oS_pMTGUKNwN_NyI_rLbjhbxBYKqMIp_oYk4LtQWr0wYOp0LQCK_BBg8XwAEsZrPMl40IakXtZ6JL2p7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8plQ-gT1VF_SC6gaI7ToHpmns5p4nO7w57sq6EfxAlp1jIG5jJ-AxglkDkXvz0F64RYi1UIkIG8u9HkrgVJ_tKv9iu_qrcl89MIQtwjfw6gGXXQaGHHvMeoGvETqrHNOwqGOmSvGJ4X1DBHLlCB3dLD5CFOELZb_K_vTqMofFaJ7HncqOe2HX_wePi9vKRaQNq8pKx4gVb_85pQ8ZSgJFU1X4q1Qno5oW387ga28AKrhG-ryqUrByL8nRHv8UZjGh5npgtf75vKHhw1FUbMSVfFsBMA6iKyq_z9pxHOemINnGcyrnDJiEahXVkQyROvbcaoLKCSUFMjKxAJN4VYqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YE5-qUVI8KPe-uZd_CrNhWgDlL9YxY-vrw-5jYF6RP3iFuUQsX4XL-VzN-k8nhz1DarBbQK4HsXNSfSSlzlIwhByDwzBFGgm6nXCH2JzNReDgFkzWbPXhsSiBO4aWf5zql1MgeGYHZXVqn6b6-AsqVmQELeMEkw7DAsNTngCqUsJrAQzOAMcLVztc3d7fYh5j1QYlXIdEinkNqqIg3AoQ_j18tp7EEPRZeWfEffNASDyRDy1RnhuqLTXRNU155ZWvhPdi8HdmMMmjwn3aO1-kbR3W29oqWzI8qEBcfgeCKGbsvGq8BmLFoqtY0gpVEwCxokpOvzdXfDiRsvDJV2TmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oS_X1DEZTiTClzZzfY95BocxeidaD9jdXnSA-xBmLjt3dWc5UMn7JuMDI-Y8x8_3D6_XBVlx5TTlO_fIkMzRPmfGBuK06ouSc0sf3xb6lGhHVDOZ9mX71BD2hx-gBReZO20WpbBuaT6QXWBK5MBGiG5563w-ELE-j-rwhpVrh0FSqjyKwW6nDC93In8CX_oqN-jnHVBQr68qfnoYoIYfesbRKzPJMigwautNNtspvubW4ZuO37zvrQAszqE8tKt1zopLin66LQXS6a-w5HuhwBw8iaqTjuVajHbZwIS-2GqC4Z-7Qbg5h1lOIBYMwHaonLNGSkxTUv3nqihPpLdhFQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RMg6F7b943BeP3MH32H8PpZOX_XqVTlwAppwFqVUurpvLBEehB3M59E53MYtJ2Zia9nl7pU408T17X8GMCan326fKONpEtcX8etYePfD2NiKfCxF259qLGJfN4XfqzNd17ZSdGKA7ZaD5yHCAd5kzFyxPtzpDyu0Eh-C_ts6t1V36jCEYmHoJaov9fPgOI1N_wlc_lysbRYYJkxiZVi0XQQGr-qvtY4nWLH-1n8NtVcNdDlQlrKM-JvadkxkX4MA1MwupCqxc1hfuykye4sXh_DmrBWuG9fNNdKQRBLdl49C5vKvKUp_zFb3nazXcPfCQB1bCBLXrS2z9IJ58q2pMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RMg6F7b943BeP3MH32H8PpZOX_XqVTlwAppwFqVUurpvLBEehB3M59E53MYtJ2Zia9nl7pU408T17X8GMCan326fKONpEtcX8etYePfD2NiKfCxF259qLGJfN4XfqzNd17ZSdGKA7ZaD5yHCAd5kzFyxPtzpDyu0Eh-C_ts6t1V36jCEYmHoJaov9fPgOI1N_wlc_lysbRYYJkxiZVi0XQQGr-qvtY4nWLH-1n8NtVcNdDlQlrKM-JvadkxkX4MA1MwupCqxc1hfuykye4sXh_DmrBWuG9fNNdKQRBLdl49C5vKvKUp_zFb3nazXcPfCQB1bCBLXrS2z9IJ58q2pMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
