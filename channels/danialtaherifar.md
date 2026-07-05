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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 11:56:41</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 288 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrWGa0v6VUuXO-4rtaP9ygD2iLUVN9BD_4vfaCdDEDyDnZfLao7yQ0rcTP--ROZ0yptZIL3NiwgeK0ZX0UpZPQB-jSrg5ccwF4i_Yw6WC8ViK4RjN2DkpuaK7hhHqIjt0ri5M1CFN_58lXwIE5lIxcfKk8kn1L1WwEdfB0vDuTTG7u3rBwqqUxfOJK2AZfxuv3cLoZhB4rX_URawPu20YDvPJWZ7YZyGmq-N0SFO35n-6LMEP1DadQ7fyugobVW4atlZoBrfVVzmPX58Ln7vIAfM6AW7-xKWRaBapq_I4B8Y09DkS0jxF5VCGc72tq8_Uf5lvyGDZdq9hQ7dNlH5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 514 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 758 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 766 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 634 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 723 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 863 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXkFmLqfiAnfDcExfs-21_XbhKlgdzAbmZfS_8l6RI4yyRXzsB2DrcfOBzwYyWmummCJltO7Ud-_1tAoMnC8jfkzMfhmpyBYWQTs_ehNJ5h3MIFE5GcMbYO08BF2fzGNqiUlFUtBOdQdiXU5TW8NbT1bMeLGlw5ttc44LbvVa8YGgl598is799wtwShRCzQiVvlKvdje2oc8Hmpf__R0_CMj-iEr1PmU1yXsgrpGZut_jBoGG0cOUhKp49jOa5-DY8ZuDxJqMMcKQHayNnjLkVPL2EoE_0tk7x_Y5KHUvJNuqYNtGPAhnekc_N9BWkYNpVyA39Wk3iZ7yWDm80yO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPE9CBWC0SwbE7CYRM2mlwmGDt83tj7yS2YtseegqRrNZHsvlLZy4MjvLhFH3f-M3RssAT1HnqVLa0HZG_GuDYcmPhgobEBOjPy47xYN3w0NWwY4rqHdt_ipoaALW7mZP9JTiXF-yRylgJ4liEYsUYt5PVNpTDVNKI_u7ZBQ7xAt5m95wUgWL_tXgLzW27baTZtC21JMTyLlhLMwMaVvwesYyyaT3hjxoFt0HhB9_7FhC87tG_4bbbWw0n5iT6flHymGxNKmbbmOHjvsDk5YEetf8vvNCIZM0miAkDoxw_qA8weT6dDtBLJZ6XWAAkQnqKxLRCMRjq8rXw7fDtiEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg0czVheKPdyU18dI6_w9-TOeSfkhfyrXj6jZ9zLGQQ9DqmSC8TvD5vr07n4xGoAKIbR1njdT_8MiS24lWoGFZg_rrueVoKMZHuU88sQpfXxZlDmSD7XVy0uqYPq2CIf9zHzHFsVDnnjRH-0rVKhVNXwrA6p6w8rebGGQ-Q9cWK4IjP0atL-BOD30vSRSt-BgC5rlQvoYMmq3zYrYmO4y7Ma2QbJXhGbfP65HEhPI9J_yBxf6g0cHDJWtL5G1I-ZQUqDuQ2jTv7nAQoTEBSA_PzVN4gXEx7DeO7wca0fIK00DEdaGujVV1tV8Ea-OqcfJnfBvzSk0jGfNgmV__PkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APDLAxMhLuDOmhC917XgiPKmK4W8pVFb4yXc2XOLR7lpX3a1kggVsqyC5sf3XTeVxNPfFpJIkK2LxpaZib-CMF53T1Ok2L3Tt2_mu-B5D3zopNxtL7NElsLa2c_7hsTGT8gH8kYCcB6Q6S-Xfv37WcJkE6q5xSG6Cc-UlAwqHCRjgQAiZQ_pQD1HQEb_bgFSIgAPLjTt0dAAntAYaVdwxWgNxnAQ2liXsz8AzPFbxe7AxO14Ep52pCL8nDDDfDUvN5K-Rww81Quvu2fIwVvLn03aeY-kra0STtndzK-xZNmhkQUNOmWqC30_1Dl73r-CTnPyzY0Yxpdguv_meFsTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 910 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3uq_iWOJ9JlvzkABr76JAD8vbJMLR6Am9PjlfxlPi9G0VNiVRrfsLl4WTyl54G9jXIhTEHmz1f5Z_AsvtUn0DIIX_W3TkepPosrPJJz_4F_C2H894svw1xUyA_mHtt2duXSWMeV2GDGLx-hkcsuYfhcDFXC8UOki9LKgKhRayoJNK7YOj4J0UxmMwpJklrCLEDm89H22uPURZlE77p9XncoK1NPWY5suTttXOZj34cvGomoWqdfHjTow2IoVvBd5-Q3VYRuWUmKtslQSIsU3wQsWwDHHYmqGcoHTObMJcwrzhKgMCAG-Td2uIqzF36dSPNyOh-UNKL0qJZsYstdyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKo4eun8XOU_NYwcMwOGY06lT-Sq39hww3iG8TlYkBStBCuABezQYYi20ntnsmkFI0K1Szk07hCawZTB5cU7lvvgYRjv9ANVSiLI7lXBVjesJDLAH3FWQxO2oMcyg-mo_bLOLA-FYFQU9RYQ6lMmrRTK2Y6oyyRVUTQpH_hgaQf-ol32HrU5kG4qT0f_fyIyH6vJ33fIInWt8m5jqSAUypQbcxl2aOZzVEPok76a1WjntyrDR-U0pubaKCm9haerGaDQNzlCQGlTgqePvELBR1rY3R5Ty13cVTfVS2ogUHm8VIyrrt-yS4YPLaaAWBfkQVoW3bTWpTzmLo56GxiVag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGWCaW91UZtFEDOkMHtTe--W2of_Tp4MCSfb2ql0Cc9u7_0lrYubRUQr5iAfc1fVXc0wnk4MH6xCRPkYInjQ1bJzSMYLw90dqa8qqFakEbZAgfwPOoNs9xD4MrLHOTmtkuAlRUkHdkhWwEIxma_vsUHhMJdHLawZUBfYFqOI8GPIyezic8etoaXfnn54q0EYmaFAvBrjKB9Xicn7LP836kYSJH4UiL9v6proZGEfNeeYOwWmUpnNTUHTjZycDf_QIGRD-bkJDkT4EgRH9vtDxMyYJ9MuMlHcvATBxsPDR0rCOpW1gQN4iYbdphtUDJNITngpqf9JtYg3BXEE_JTqig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBh-lLACdVqiuGNccgDuu9RNkKvWl6_ChA4pndPN7eMYRX3LWOBC-ifkwJMQV8tRYo-xXlQO8U2tn2sa4pjwDL720bDlqORzbJT62sFwUxSRl8FU6RutzOBPiiIfzpykUNWmX5nnPDJafVQnq1ypf4AYvUG_kfzE3GpvBU95ORVrXkfKduR2C1DqE09XrPV_Kwpc6gK0tq5EJF_9rWNbltEnWyQlhASNDeE4jmO1p6LFrNFDfBbQGEjf1Rtd1Y1okS7o7VosnMBiWTM0Td8ongrtK5ZPh7mqwMy9aHc9HVJvIFNMhbmcXmCtv1RqLtXvFg-mug6yvOt1k3eO0aEX7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyw4O6KNYlQoFKmner_cMp0saguPCnuTZryjgfUfjv6WEydX3cOqGLszBv1pL1w_xh6eihK7zyQxnNbbALJFhTxeMgjJ1YD5N3_yZ2BFX0-hXAqyW6mxovteMmmPl7UfDA9efRCFrw45nUguzKWQVaSA9bxTF1QE_unf77N2Wbaky3NPoqww2kUE2xb4L-6f9uzllR3fumb296QixbALo5fkMLv0PnbVRMCkyHL6F7EA837nS8ZMrXQhYoyVbdYTpiQ0tt0m1oyQDdthi3WWRPHtZMVpz7FE78mVbb7VS97Z5RJHHv4B5M5as8NM-kOYUZ7sIVGmfd5eNkOzd-4M4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xl0dC9dGnK0pfuuHFoSWcGUWsEbAL1M-1wxI5ah7B5sO6DMMWCW81aPiDkPxoZSSOlVR5LFJsi_cyUDDkHsC1AhXcyW_6WkPeA145NmAm8QBseiAsC67L7ZYhfjKzsmxCjfzvu3Wd5xdPZrPV--HejF0mBrlnuRx0M85ioleQvpqNTYibXFZ37mIkh8Wj3yHc_DxBI5qbuCO4-zQSnx_Gi_LuftbyZFzRhERGJdwzMpx3oNpu5IVKyyPTWfvyFd45kNl7WTmsZHTuei-wzOfme97uuOX3d8N1k7dLbtlHb-X4GjcYRM5CD2549IdIuOBzmb54S7e-Tx0P72qWKRs5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hm5ZLJOHo-4kfuQbShDkJxvIUd4Wq0j2LjwhRxaIln2zgFcnDXM8r_yExNtE09V5NrYQHlKO3SSOFypisN9w7l9EVrvqF5tTNcwXQlSkDUdy6H5eidXIZz0eX8QyxBieIBZoE74ha1EB1nAcsCiU3hmiXnqe2WKY_D1HjN1oSDaSiKNqKxVZ7r2PyUmoUo6XOzvsFb1fxde_w8MDgB5ymRx6OeBTCmyw7gn1W6_4fVWUoOGaG5Bqf9vzSIPa8OO8UskQcozpBj-hoKEJHbxXHqbpDl1awlLdXsftp79ZlSwv6iAkVFMVOpQe63tlqA8BpBwtePFvlVyD5Tk8ghV6Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PIUr0QgQzb7WJA6eeRYjyFfARV3GLvRZeCWBbIM6nKmhNrtFZ6pwChJaDpF6NE9kPGqLzkEHqoUdZyMtbGANPLMKDNTZ16KdaGr4RcIPRGLW3tFA-MxPIwJXWtm3BC3WTNTIfTrp8fMqfLtqzQjanyesgV4NE_0QFbSi2m39hjg7fDfde5FYZE2GQG8YEaOVYE7ovzin0aF_X2Uxt0e1DewV6KFQntw2S_-TDIBTYB3U0V_T8G5yTRbpGnz6vyfa3-ifwFs2m4HTdcl6JJ-NW_fUp2-CTw86qQrLaZqf9tqgGmfb4KGCtUfhGSe7vJpNm7MwIvBULS9zJdJwzkrZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFrQy1EsasnxFQJYA-NHoW_VOkv1POd9-F8kp3ICt_NMr9K6SXILRDCEa1BFPMiOL4ei9ULejnryjNghnZ4urjqKZ2eBXwWxiUGUI_xVMnh0OR3MQ2SlMsOjLzOfOSeyK5UGhpr4wDQRqUSeQkUAsg6hSYHga5_FFLeUvamWrcBeUTFF-KNiFvBWlN0Mct6KzgiUlh7NnYcsuu5y8ffT3VU_P-PhIteY1mqjWvE_s9Q7yJSs-GR-MJ8KmHNZfktHH8PuBEg43QDGoHUgEGqyG6DN3Ykz7gGWfbIqGWTKoadRhh82_I374-rfbYrUj-5O_Pc_uGTwgHgghjDaBPx3nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaVzHY3ZAboFYn5T8r-bqVjteesF6EgdB114bOVMpH6KE_Fv-9D7go5G9IhBsLWCdMsUs2Xmn0PfCOKAEHhH_8XqZH_dBRH5FPFHDc7AIMC_XHSSGGJHJM7ckPS1RCryQQFKOqhLWrTryQ0HNND9PHpl0n6ZFTWeYU5TG16NeDOG8g6zgXIRaRlD-YFZcwyVYSlFCQL5u_TJUeX96DkOv77YaRQdYeuc5VmwR1gtzwYSYoS5I-Ud7pHCAYHNR2mVipY3PhIJ3Pb9REhH6d9zDV0RlQvzapUW_93I3zMvnvCy2IgB7-tr6BXwS-WiRF7aKIumx0UzrrtUApcQxxiG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRFu482qFmEd4V26Kso0Bc-GBpBvEQjT4oZrwgCkItwecvQxPshzRhbI51RhXtp81kNgWJz4Lu88FCXNtWweMmEllyl0M65xREYbqW2l-SUrSrYeMXGCXoW2TtFpfzg5snFlOLNcGsF9yCUV_mpjFOCd8O0uiWxYmM4uWv-6SKvBVighbE3S_ot3zASWfMLCh0uK9SS7XiE-JUgHM5FAEIHSko7oa6RBSLKKZh3-r9vxMbIQxzkkI97h_29cxNwUaZacSEZGwS4INYIU-vITq_5RBWBSAPX_JVlKLo5f7ovNFgBwQte07Jj6hHnQEry9zTJG3fc1zRCF2WZHiNayLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUuAg_Olq5dPxiPoUYVPu6qLRtg1BO08Whpz9VPraVvaHWnilAIbOCFrBdbupn4QDsipBBnEGblyRJYa65O9PHmGrCShYL8a3OP0XLiQSNRfKIxe6rm-vsCy10vzsriMx4RRsjOUI8sD7-cClm80N_3jUcBDzkp7c__PGWlQa-SN5SSAEZwd3xgFIZqAZ0qC9avhUmmAlTWhIeh2WPXyxZvk8HCLP0mh5ReB8P1Z77UeYZ872KO72XFq-eVwWOLjpJQdT_8DnAckXcqNe72al4UlynCTpEmE0uDx9qyfxW70CIOQQL2v0YqOLNWMI-qCXrXlGkHn6Rp1kpG_x5B4xQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=u1XeacHo4_eYlaw_jz-ytWIiESWRqM-Jwhi51OEeD_vYpdjkgWRbHTWAhUSJK1ccfik0QVkDMFAJJ5l5g-43wmwJ3FmzOvpG2WS9b5YMqAvyOIGL9WwjknqfmPSy8oGC8fNWxWh3pPZtzAz7lYJRsmRuRMkycyc3SpA9LcUX18GYA_Z1Ytj0hLRnHcVSXvHqK836oSD-t_bLkySYILxkNMj3tPHEqEkCm02lNEAR6rVIkD_Y6iImTPISkAhPyQyAd2mocHDqBhkQ8M4NdgBTp7lb8TLt3DbhUQyqU6eHHCI3UnsqCkhz4UW5ZOzcSyjD-TNlI_IHbq6AlhxBrrlYww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=u1XeacHo4_eYlaw_jz-ytWIiESWRqM-Jwhi51OEeD_vYpdjkgWRbHTWAhUSJK1ccfik0QVkDMFAJJ5l5g-43wmwJ3FmzOvpG2WS9b5YMqAvyOIGL9WwjknqfmPSy8oGC8fNWxWh3pPZtzAz7lYJRsmRuRMkycyc3SpA9LcUX18GYA_Z1Ytj0hLRnHcVSXvHqK836oSD-t_bLkySYILxkNMj3tPHEqEkCm02lNEAR6rVIkD_Y6iImTPISkAhPyQyAd2mocHDqBhkQ8M4NdgBTp7lb8TLt3DbhUQyqU6eHHCI3UnsqCkhz4UW5ZOzcSyjD-TNlI_IHbq6AlhxBrrlYww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqa8WmFVucyy44TkwnLPa7vu6e7Tz9WeUvegNUFo0v-XwIuEjduLatWlLw3glxiQn_bLjcwfCKITKrbNdOZtAMfhc8HqilIEo9TjbQKmZmbnmWkSa86k9UK-5qNbEIcE1QSmRmlxi_nB-ZT0Eed0bW2MKDE7RmPRPjkwzU5frNlrIOOC4VgrQbSIkN70zRrQP28cAJPD4jmudIBgYO0eGxNmio32cS_G_lrGoweNe9kLBQBZqpc3CUkrecnX-Tz-xZhwX3Pl7EvhwWZPwmjkiWIV3Tvs9tQBpFX21GchGi8a0MkbbSF-GMh2ld7P3MDoMpCOjdmLO-VjdhvYN112Bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0Rv4Thv-JC6zhAuOt3LG9ZlEzXreg3DJ4kcdPy5NkC3eReiQiDqGbnzOIn9T4GSuJxx_EypqO2RcbHhlxBF1KDmXZZ3mHz19FYBLMNEw-9GbFCvZAcF35deTgjf6GLl8mc7Sy0LoO23le-elu5THFCXrfGsDhcYL9hAl183Mioa7KpGOdzpMcU1tf6YCvjPt9g88st4gES9DQPiTr25LMJba4gPvoxrB6prhiy35ElLERKb18lAIS3MlEVJZkthLTbu88HmjXpFutHGxexjTcBiLQoIkOjkybxN3y78aX8CamNgNVjxZlrtpeMcMDUumzHEnZwIximHOz_Tj9omTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfsALR8PkjtN06WqUjRmIrwHyYyHbOodtvvRn7Suyio4whTwXhN6s5KbH_HEMzujCtKHgMEveakr1mbABZlZt2ik77vtiQN5N10JmTF6oN_VcybGPiivlTPCogzBo2nu9GwLkeK0Znb9OmCQt-YTC-Surka3Tise6T1MKrkEy_kHgEli_2Kb4sj28cIFSSlO3zBK5T8Jso9c5omox_EdERKhE4VWOk4r7JrpJpnV_nBBmVTMWDclkIAl5ERVg65lnfcx0wWutr72zLiUxp1l-egVzbUtx8TY19mwnamlp0YrCBNr5JQVBbKfLe_5ybV3lobO-rDgtkFZH8eBX9amLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2NyP1PQ_7i7SC7BewdRtSIyPaP5qspZNCa5VufWHS8H84sXDOvm8dmQYE_ap_Cdh4x4JeLwliHagyUHUxvVnt1-a-paYeF_Eih4VuqStffcuLR_bu7K5jIaLo0c8Ub-owekTw5knK_BAImD-vW-73gbk2PgQq5wKijjKDZF--Xsul3cy_n8Wp44l0rUqyo3VLPirTptONvk7Xb_3_GLqgZz-avTeqxeE0eOBZ5ddnfGoHRwRCUWGs0uFnDhlXqBqrYnSznrv0XKaDhBbg9d0acz14uNh5xj3JOCx6WwAbf_vFOtfX5v7LNKIN0JJOsMG3TGfTLWHZNKudsUCthykw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLK3uLgruSdLVLF9wiRohkgDNBooaaKH7SirWkXid3jIfEd-69E7MukytGLQ-b9EzYzXPtydlF-Y2pm26ZqECoDK9TiJ9aGz0dkHg_sm8ByBW0yDUyP0OXrmMgsNV3Yepng53kOQC0ypy8x90TkGzMmopv2vQb6agNyPFROJ9ElitP8vUrBtdnSyf5XXJrP0kRucUjNpWZLr5-VOgO2TZXO6doXi2LqSnxbKiY5a5ITzp9TbGUUURQOiAKUy4EYFRnTq8AgL0arkMqGbL2y0QIwtY2eGkuqF51i2lusjYF-qcpSWTv-6ENtQPy8y4kxicFkAQLn-qsU5XiHeH612Dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2jJuP6EoYLWHDd-js4dZhRhxrqws-cyJiVRoQ3xXH2GvxkQgoB2eP5HCdUOGE5WDKOzfltgErlM8_5aGoR2er297bcYqfvUx_tvRMU9usRYM9Z084fa25Ox6j9HU80r3v74Sz1mcPH_B9AgV-kSUJgKo3vQP_lGtAa6kLQb9f4cmN36vjB2It-Lkb8zvpbDBYJMPCVBGgkYlkxqRFtZM4VRrPVPblaIAA4CGyD8glww6iIiWeKZ8JrH1kLZYLn7wD41maLjMCZ7R-iTWB0JzczMuvAaNkp1zp_W52nhQ414PBfaPsLDDXlGpt99Pgrk-TdO-MX4mtW5mf1r5Yn_EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQw544WWF5obkpxqzdZPrzw6iwQRaEQs-eooD-Tg3VDiNOCy2WM0fgC04K7abT-Nv7A9bUskR1r44V43P60PkstH_a6xunfzzgSUagXRHdFEFRumQAsKkmpDbEl10eopXMGTb9R-qZjeChAa5vXTLQ_fNE2DqtmSuPj-ktQGwPqIH8ZU5iK7rO3X0asBs97r0Cqex3WyPUHIF15jNidTi7N5-JQlnQpK9vxFa-ww1Sx6dfW--Lu0O0-ztjqb6iW2M-DMhPovY3SXjnpxJLRag-zDv--C-F-uSbXiB3d7iTa0LyQ7_jdim6-_dnOPGiheV5b3qS-KruftnckQFg2EFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njlAFWhJKB-rtNj4EwLazhNfxl_pteLdOT3h07G1jU16ULcY51L8QbP3GzeMEpz3doIF8EaAkFKTdEM7vb9IPCiA-u7s5CzgqujwVRx3f8IEaNNe-w2n9r69gR3rkvr81z0B6v73d8J0i-is_DS5YvH-HvlpojZtQ1295AgrMFSwdrNyfH-bcuSk4D2rfL7TWtmxUrp63MML3wiodaQguSYSjjPvIuGu93Kuj7exSCGOOBuo0sSCrk4g_SrQbmb4uNqyDpsMCfWdfcJzAo5KSG27QpcRBoBw0DVek0lkmw14_FOEdDmDJKV7kdyg1x6urYI7nRFfBr93v7lPzZez5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ__h5ArHecbYb8FjbPhqOrwQSlDCwuZvh8u-DR4F_qU96Gul9B7-jfMy5_ctvEVfsRJhbP_ofH9-KGsTZs612e6SJXueK3NtKqjNiWv0YWsY69oc_jY9ZajMRSNOkWlorOK-wHJwcODQ-BX4k9RbkmFFJDJOjnE-9m4If4xrZnBDqE2ziMCnConeWB1Fs7RFgLef4hl-a51Mb8aPKlR8gJigUdtH_W7UDAYl05OJsrrmv_CTlvjEKh-WHfctyo3swRhQvbUHc6_YTBKIWORId_Y56F4fOWXBozwmj5LuZTxyhvyFM2ZwpwQt4u8fds7KSfsEk6oLLvadvScka4B5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh_jnengyawxBd6IAc61CaEEAQyedAJcbTDgsdknr90qXZgtj2shTiX6vJemafRKQj7O9iYjgKsiymao0mXSWYb2g9t_ONFKEy-cjmqAfM56ZwC1Oyjm80Q63e0SmLlC-__VIvy0hMplhlkgBRY-BdqqWtcVAJtRY5ncSXu15cF3CwGmm6lGsKkqW1T04Bqt0TxbtbXYLv3tfdgC7Jj3s0Bu2uCmTUot2yZsTFB8Gzs0Fg0hycHetaTEVymZIKIBiweRjOrNlqOJzNESvkX-e491Gt2h61asTeA6iYNA98rp_h0N0MQ-z6ow8yCulvD37HuYHrW7nCVh2bar4RmaBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTAXHYiSfVWHSRA1oiCrYgaecmZD0wShWk-_B3Sj5Z84qo6JvqKAsP-59nSINSpwDia3DDH6YVQxjOSzc7adhURjlly9iYuwypSdDQgZq5TlMWxr-8wUFiPLPd4WZ8Pty9nRCFmJ4ZNrQghSu5SDSJIYK1Y3s1Ec2FT-Vmd_Y2tBdWYnGiQ6HfefreGladAWU2x0uiNmxdendddVe-z9Mp90a5ECNPwp5L8YuvpXQCzYmCBy_NyH6uKt57fD8c1uBVKEnWFMirwd3iPzJqLUkmhVJF28aDnZr-QnJyuUED8vBbJ2GTfe0nKkZSc1pUljP4aAA3Iegcz4WJJOY_b6sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kV1KEj1Msc-YQ3queHa16dYfRKq4OXaSn5lZagQqd_OTEaN-nfzZId8oRWa04pT1j0UsL43PIPbdCAhJ_DKUa52Zz4i14FaxlNq0_iGnQmHYRYPWc8r70lQ72S2UPvUDNfihWm2GTldcUBNoOM8YHlcL1WwEv3LR0LxP9Vv2y_I5z4MAWKPbn-PGODtkXofobTqQoogEkRgKxLUS_wYBRFPyVpKdv2EPOFD-T7A0i3y4NnxUzLBQIQAwsH0TOmAEzhSAxrTrqudbVG4s3qtvVwnnF8IhUUFOFjzgPzh3OtiWsyNXkWwesPxl7L0uGK9hdWVIW5Jw59zuFSTFvxVfbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/StTkw4k_2hMThjrqTDYV8W60lwfkoGnaon7UcWP0AncZgBTznSt9vCCZakudieQTwIECYFuWAx1_viy2GTK1uTy9zSHuc5eZZiNAutPPkmdEn5BmH7kCXWjpWmpWr6xwgocsIGLcPDGMmGkTuvCBq1epJa6JFujj0Disn9J-Z112YSWw7bvMjd4vb9KwW56iS375rIU4raXZsNwHEiGsN-mRuZUMMfVPWSsGpJJNyJJf1aXwOATit3Qw27q1_b6ItOeBVIDihLju7sNB19bzv8Fb6fMHQ3UGo_VkI7bz5z8-Dd9nM2I6vYap-0pWh3yZcKiPPTBocV_3AUZUoZAhfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Spv8EnbX9p9nioYEB3eSNtUrd8myjAdKrx_oPK89iBfo1Bcru9J_MzIwCNEPh1xJ96EPCOdgbmamu65VDNkScshdNSrz7utvnaUtb2iszFmUkGMiefXUOb2Mvs6xg7bnfqt50-BABlMIr6hqiaAVUB2TA6ZQsSarrpSJrBOfVGAlPLeu7zW_fsp3q3QMP3Wvq4jOSFkemhn6RCaaN-dVGFzK0eeYsgzvbRt1DorNzIboI0olFjmvlP6VZiBoILgamNmbEGV_RNHuCNDBo95cijdUGLd7t-J4QpzdqCcziCYVM8VVEgVfxyPMRaDIpBKxZNlJhLnccdXEy2eYBhU2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3h3omg75b3O-ZwaSdIsd-AvrejLl3LylFBlPYsXw1c0JJCK_UH9AzuN_OPaPQuD6xlXmzQQRJx9DqkNYatctCi0OBz4uB5Wc29Y9-f8qB1aflD91r4vETZa4XZAqfWxQABkScsQTYX_y84CgIR9j1ytzO__171f3wZeDwFLdarPwwG36K5uj9F8u8PiPv9C2YJBCAXUR3p8Y8ugg3XtF7kgySNpUWezXC0dydiL-r8D-ETrZnKBqwp7TmAu3Ae2-lqrVj1nhcTb5a0SWoaZtmt57dFhOW99zsJV2DQjymdrNhPwnyf6Cd9hbvwiyO_AKYW7aeN6wt_nplJKeC7w4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p19Ws8BYsnlAhUHZPUFCVepAPKEVcL2ZIFqWVMG-Bij7VnSb1AAXiBS7stGEdhXJMStnlEr5RfsqJcZr7wQcKciIg6xI0KB4yLtHvNuujRC5Mmp0jwCVVLwVyq3-_4T_fQZ6Kz0HFl1bM9OQfko-p-NDvhk6BEhKD7O1JtDifb9gS5Pt7HPTSlsX4gjwReWWgeOlWqAQwrvS31Tv_N3YgL4UR53EsxSZC4PE3i5sRdyqN1BRDBgMJZLHICW6qyscjfezRKv6-k4xbBiJu8Riiu6Tlkvt7EQuz7b2hMYObV71fTTl6kgPtYv3LxZijWO5vBPVWwYshI2MZ0I5JQNTeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRpn326GfyEYKkpHRPWgCWMXBJZRAF7oIUA8BJJ6GqEHbesdzI4ImKDE6wlcoIw4RXc4mHIWB1RP7X_pKptHZgfmmUgXn7xD_WMWPCt7KM7WQT73yjdhKiMyK5BH9nAFQ0MXvUzOCLpyYeKHR7HwZpoV4spHk0vouPizTOvYThUvkijnt7NYOTHnu6LLY3D49XyfGFzDtDhzk_H6z41Zp6Kdwiugb-jl0CMgWRXhZCLFq1KvnM4U41afaWMBc_Cd3GGU9ztRLXjqSYMfUbNuLSZ_bERBCCEQHEfy-N2AXtZB_Lyk5CTCD62g1aFNgyxcApibCkr4OKfyBsWKlFVy7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG2ouCnpzQytu7ppUnSxJoZ-G70wIxoTz2klZJpCRhKDcMpswu1DSt0Cr6jaaI9GMGwhWOMdAgb-ylw1pK2zFN33p93Co1P9EQ9sIvDwDzRnNX-tKAYs6kzH4VZ9psHl-fsP2i8V4LoIfH6joQgcgX7XKu6JX1cB7nYAdNpuPi9trRRhJ7K5A8GzQOEGFxxWsz0ezO-45uSM4OpMXYF6kqH7X5Q6bDPkxaFFZmGtvFcirB9ZIGioNLMpfYERV-jSTWCWgcnie6KyvX-Q_lWwP5eYgrM7MVoEx-VZUgICzjO3NGHJwGOaxoRayTfKSrNcfOM2htgAR8ENl6UFpRVkAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-h35j77UJMmzEYT-e7oEDKmnNFQrmR0S2RIgMDatHp2XM0FicASfNdGHSOxkm34JIzU7JsV6uKJmT816hG5c58DFQb0_erveukCJA7Ea1Ldw3108AVNTv6EkRE4uMe5UlkcM9O9C5Z8JNj8AGA0NCEGnYFx0ATpHsWbbdaJbpOAGyveGB7UghuYbrh9_KYAsHLfYkm6zTOZNioZcwWtEj0h6VvEE4aBAMMVXDES5gV0MSoaoEHJ53VX28ijKKiTeyEaHQX0kmQ5ZVC2BpnpnuMr_Fwp7sCJkJXvmr1JzpyIDG8koctDo6sfT63SqaUzUTNgdAJOmQkJILvLNtd-hA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0C4ZCJmQd0VvIjslVmCQNq6o79EKHXvDhv-nGwFl4ktYh6k-1Vk4QxKeNcJXlRi_k9h8KDKV2tDN2CikEK6mLU0uAoqqFlXsS7qCwgtruTZ7hZpv3MdOXf9N2lqflJ4AhnyGvdVcSRVrfTjlHFOpMvXA7zra4jVqBYaGZcMCKYmR9fvqKehE4BagHegNct8Wpzc1hWc_Adp6t3T7LrwPoepOATy1MBPOc-_XqqWU0Bjcc_SKdiZsWTgFSFkcMK0IoYkFsIzGYT_279fIQuPUvCkSkM1SiPpM0eZGqrfLRjR9n4Cbt4xJP_nHjZPH8hclZhUuijoYkQmMkbjxIjQuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxzNvnekmgmrLivVgcRwkExij6fYZjlEFj8Z-JJJxy8lH3ZTF3e9ZfyWM56Io5YNjSn7904SCf_k-Xw2ibA7IZQaXZgEAVyfHOSIM_Ttndal3kbbT5LcLgifd4uI6NkSFk4GyQealjFvWK03xbi0nZc3qEcaam5vXMqXkfqYSbRjDu9kqLlY0-7Hlb0Q80QsEwEiwz_xOeBP-BCmDcCTJRKPis-GX59HKsBPvogye2HWyIVlVm-mcPCqA0Hu5sWhMLmdb_vGHXp7c9gn8K50Ks3KuHqojVli_aSXwdyvs9c2lSFaV1NJBpryIZAsfbRjz2nWLiMy02BpcN0s4fwYqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHvA8j-gfW7KkrmzMIvPBG32JVxXANmAbREAP4WfxDoW7uUUunCWXqAGY4ewiiePCSU1N5fggV9aPusikRUeHynkI6pLqJSh_eNwaNiUAQEAkZPd5FTvIujsVYloTtRnHPAyUwvekA80yYmIv0qRE7V_S1ULjNHc-QThvMDteP1ZMk6jbPcFqpO55d7KojfxLcLEGwyzvwL22YCXjHukBrVtYyilB05S8x9Ga81mEsETMhVpa7K9t97qgDO3_mnRi1Dw2vvHIKDwWP37wArlpUttsKV-h6zH9QLEpECUliMim-iywLUVxQFBmknpoFDrhnxnI_GyPEuAckNHzVsbNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8gyTqGriffmDyLoEkbnTNzecDcD1y8SfSfcr9zx-R8JI8RpebhJAgxW2eM-PVN_QancxUfnj_DHhtS-E4J26PsznYcWTEvxZdnoMEe3QahxbYoLeLIUWqrqXfJZVRjBuGJJUKtiOanfsrBnsC_1Bzp_P_wS7sdrLiQkDLABlbyXTVYmXFOkOmmNfrg708y34XPoi43XADADC3ZWPr1lpaaidCAMa-HJbXrKpTcRssYgYF44-EozQnsv-YOlxcba7ySb1zRVRQIJ4m70YnHqMzwECWdzoo6GpjAnkSIXRFiOsdZoK1DtNNVfD9uLFSlip2_9a3zSMO4rhY6-5EWx5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOwWCh8dG8bsWaxfPbPlLFYytgwqibcOA3Q5i9wsNa7N8H5SF7N_zP9kC5SS0XJ6bodSCDViwl67ESH0OZp5u25NYq29b16Y222nCfD6EFfenp6gPQD1U_fi1T-9Q7wp0K6tYvQeja4mMRqf1CTR9Q3cNrVDW5QqfgP_0WWVkWuE30iTAyK3s-d9sKXWMinSH7y-CBoKTxFX6Gd3rZ2ldcfoHBMCdaCfNJxUQUzQr11b-eHSqF3WkGH3kzfpO9i0RC6LVlHrdKu3jlR_E8NYw7Wm8EVZMgI9licOosWlD7SGhZ2qtO5EAPNVL5Rqmbx8g5oUpeAvDZCggCOA_3pjlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCN5hvOnegOmOOgTXAQMJ6392pVpr4tl6_wfxF5NsG_wUOL3DvbRdXjNGIMP71_BeSqWXpR5oQOCFPvQUwHe5lYp1E-qXKveG6AdgDAmlc162L-3BmGjMlfvL3xnyS5DLUPaCPCzZCngMYQmcXfdsxcG4_v5Fv90oh6dSZs_DTPgVat2MpbyagLzgUb5Ci7jc3axqjlajT73rEVoQdF0HiIxlh_GLsuQrD_-DsYPYP67Z7XpKV93djEmwpecRwZvBcLXpEFyZ2C9XMdDqiEUhFP1I9i0LX843UbW7AfrHAa-z2gKzNL495_ZF7KKt-5efTfpzUZ4_dzZG8G4LuZW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v0J31shTk6YwTEN5MHQ0f7sUOJaY9a5Kaws2GK5pxlgaXlVfOLpNpQLIXUGYOFt_tZrFOY0tXeTAbg5LxOMZZhV2zAFPwaFObwMvS0UTg4sa76_EOBPrp2WyAkSfja0ewj1wcF3BSehlbp9ylEa4wBTzoJ4JRo9OTXO4aMVmTT1TPvq-k2Jd1-0c2Uf2iRY2GYrtgA97OVozFgzw3oK_nG11CJ4G8hG_yaL_6YKXBaG-cTQfGpZ7SIO-BUaJGeCrMQMhuWZGqYKnLvwrSmup8_POunvcseRxVkiE_vlALisiHRCiGfU6Ctmi56Ku-P2fL_XTxWVdPztKcbYGKZX6aQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH8gM7RJo8vTXchhq_HZlFCZbIF8e292S44lU3QBnKd2yImE1QIP8NIFHhF0j3tTotWhiTZS6jzumqJN2fzD3N1EDP2A670IYIhvP7CjBUV_kzd2ihIe2AYISpeYzantsj2ZhnAk2VjQx6vbThN16cbeA1VjZU3YFjzLp75ERp6T4BxZPOXODla_lZ_3xzlr4GAPjwaBCmbGBIaJqkW9KEbSkzArRG-6-tCCym5O1RmLVUtkhp-UmtrPpPcpf3QqNe_dtf8E_jPWcMhK4ls4YZ8ibwZmJfgrW9U9kf5eaR3j_qYYay23-wvS6KcpyDtMGwTL6OU2yF6355VR6J1nzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTWQ5gf-ANBupOKZZHzUOxj2sWvZzSUoXLbREgldCsFEPxUxd1qEw46SAJeyYcZ4qeuQffd5U_uFGJni3hA7gbv4cBgm5tR1zF1_H8ufPDM4Khm0MpsJjjPcoOYGnim7J6s6hU3_SJPQBKMpzLsqIOPm2WP_vPRGwWPWmOVmNCyOAMw0ft8LAd9cRj5SiTELS9_FnhrQzEIijv7zJnYImkor_ctkbrU4ZgBGHB5uGhv-ZOFYVL155pufxEVrtVoqJGEfiddpdmAG6utjkJidJhoqdpuA9Lldzhe3SGUW9bdfvHNkacADQoYl7WkJ0yEPtuI3PbjweZRnKDmj0_MAyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ch71v4WXdsfmbcTGSW8cD4laG2yWMoPrZhFGiWq1Y7tN7SP_t4EFmlNqiXHJp8ctlkvm9_E7DOdZ0qbszChZOYekwP-h6onG9Bte4ySQEQ-M8K3gDThgh4cX5xUmHqZPWKqzifeverXU6mqUjH9IOgqZybu_xv791tlPnbIuNf6seIme8f25edT20KXwgva_JFC1ru4FupGwx69vGkWZLQTlzksZn2O7H-NuDvnvMRJ4jBZe254owGzO_n-HoDP9W86_Qvw3CguzIwoXbb_38HvjV1DcNN1VsoMLZ5iPTFnMK2_Yci-xUsdb_C72856LDr-w3rqd7Fjsq-DtCEF3gA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbu9a1T2i4DwvvrEma4tlqBO5LQi5Cmrl_xYt__LBzIi4cv6zNi0VaBXXNIN6-MIw6f9AddfKYzI9DLiqnKyexhnrk3OrH6Y45xd5Ro3vzCVOUi60nEYYF2sQuJUzWZ7GwjsGjYfj7uB1IZ0GH1KH5aI93XUcKOznxNpdrkWtpFwjPSAuvfuLG0aLM-gNTRoyRZwMow7qDlTVBiFUV9hjwEaHYwcYpTMoE2fnKx9_VpenFTuRmWMT7dnjmishIppdkl3DRUMOASiMZnt5rmKpMMDQgnUTFSaRIsvv8IOatjoHpGy-gMbV16PqGMaF-HPhr6ZliTjVx-yxfLd6hMNxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNNqYw7x4D5IT2eXzqwzyrFwQkNMB8BdiMSDGVLsc2nUACCeqeUY6BCkrAYPhgmL-OdX9NwSg557ZeeD4S_yM7uqw03yW1zk2tiSxy1IYuOB9fHQtDme_tEongNsmr4uXqm__59uuWm4KAoRvZnO1EeakQ4kL2KrdWzqEsanF-OsLVc62XMMmZVe-PJrQ3CQxbi9Eemnp4tIvsx6D8EOr66q_bmadHA0Zq-scxU0X7nwOWeyQpJQR8ki9W15_naFLqTMG6n2XEyjL7bEpTJU_UpfUCmLsnyjeHYmRXyOqzo9wH3bcm52QZsak7LIse7Mx0d6NrgnhcFLEyh0J9HCzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wu29JnxYagYW1FdObSxloVd7UTUco0k75fUPJx-JltMW01EgqOmMbGcz9bX0GbQzThT6HIFewSg-aVy4M5Q1eBE-ogj62PiAWFobKTsLpnFCuViBuFByHzK9_wnwwqg_fALJ77jCFwno0wmt-pOfc5VaZNxd7DLColiOe6F0CTSBwLO-8cpwPyk0b32V8pyEs0dg1H399ggZBnTuliGcgm0YYgZzcWUX_z-fwgsvIAYfUEqX1cjmRRnmonhdAILbpBYfGIvcZb5msv5OiKLwHaA97pZ9CgeyYOusoCQiGCCeLH5jXkZrLXwuRib5QNBFr_1Rlm4MAImsOsP667IuFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etUU5-SeEsBbdRu5DJZUMRU0boPNjicHrEOkmrqdn-IS-ehLttu2Szw9yqNsMwSINghr-fCZQn8qBznn071P9vMuQRVkYtUYp_nqrPndeHGISpb9ZP544KGbAs6u9pc8-lEYWx3blpPFe_3hh27POF8Vvj7pjnKGtVBldaUQLkQI-y44UAv1U69jmOyiqsxo7Ajc6JIRd3tIB5fodoJCnwBSlQ-c7OoolOhQNpGsvPgxrx02udWaV82Pu0oIUQNQkyO9aEEy15UlsILHLMmhxFe75QcZBslCnFQJAGxeyuDURNb2t09Zvf6WMx33hc0r54nGxLReffzjNWo6OmZuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5Ey0lZSXQR7OZt3ZkdTvPS3FUoKEkkZkBiajx4oRAElQZ3myD4p-Y29u3il2LTr6yDSUpFZSQ9ThyvLSM-4yE_g_c9RMIGXSi7KUEPoGvvEwW4DCAL0l1OHMIDmiay_LdVLx9uekht3z-LzHsCnBBctzDqHnDD3b40dObXrVRsf4KDMp1Z0zVU-L-LkcpYGmJJEajLCsTSv3Vems98tOVc2hwYHUXeMCumgsvjKjVLGB6C_L8JM6t7UjxRFpj5NvK5vWAHUguEVPZACUBP93snAZS_TEy2-0-a1rVSPU90PsNat9a-RKJorbQ9qvsEiabbj8wYmw0TJZ72Gc-_uAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXskd-oLsM3JyxYQxBr4bUObvHU_UKhErJqoEXrRZ6pLtWdoScqQLkgOtiCTlFrXjQvxtHWxZWRGZm3QjqOpl2vxmJhtRtqWYgxaQcaeml2_xA28Ypo86WcZedbWMAppjs-2C8BvvTT-Z1kBeG_GhaKWSiYyD3T_IuBWRmAOly6Nm4ZT9ZjcM-2PXGFspceSXmI1CAv3dY4NGoUuzOMj5PochIUJg7bVQ2gcN4oVbz-BxzUdqGySDQ48BxtoKdyjGLCPkcaVLmZMiDurSdVya5jd02qJSGVHrrHcVl5CdynuGmsghTnLCOhzWF17AhJOpofo3SZNmv9SBJ8XEVAX9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_JHxvuLIMR_g04OJOkqIbI6rt5sEKxtL32WE5_pXKCqzVQHGkdDmrgNKZ4nladW4gJAGi9VP__M9TueU_uyCQMsSSBO4gt3tT5J_CHoR0W16BcbPVrlkRGgrVlDv8uvUuHG9nv_0g-1w6a9MPeq05ElVGdaO0TrBJKkJWtYaH3uohWXChjqHfqsIT1L721XjNWM71l_flaaIP6CPFHEaI2HhLuk7FPTh6P-GxB7ppNt7Y7w1b6OtH6f42ouaQKj7EEtW5kYAeas3VgVLBo8RgbhXNTSc3xR573CzQcMhUg2I4mrCSMiLBp9lfF4zZ2eXesSa_l1J6-y9Gc4cXhixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFceO_Ysb2fnXgMxUvflRYArgu_krx5Xu4lgeQH9r3OKDf3N9vZJ8UUBuC7qKy1iZV7q_JEmoxcpcCd4Tmh1I04HNOUtW5V8pQS00K8re20rrh3zydZ4jsudr8UiUbXm_usqccWpN3cU7JCpPMDjOm9FZz2pgru6j5jCv5VfNvNCVLN3p0pVuCyxDqJIhFzVnft7jGO3t8DkoDHx6m6wV179pViljAj7NpnWvpJ6iIpcBCOf5q9KZQpf-uat9QYlAmBqYNRoB4A8FTh2yD3Rz1Px5N1F1yvfcmjje-2EB3WEXIQOsX6hv8r7KArQSIyxs_d6UJKYtqAMdIuRguk4fQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwj6uFkO7McgvwcoZNBe6BTz3bf-0Pu_aTRmtcfyvdU9glDO1yGRpr4YnwSR8JFLbd6r1iTe0Kt4g67ZheZN1GKpwLQv-Sibtg7YmjLLtlqAGg1i6qEAZiGkIg0g3fn-NXLRQF57vds4Mkr5RDgPhumfrTUwgfNuq28uigAvCUpV5_5wDkSQownUXLVTGonHLvaU86ytfzRLx91z12OvqQX5hv3aWZ1RY3BUBYibd8O5EX_WzUGEZITq6KSpRpbB6JLVpmUG91mFzsfKfut10AXdhtDSxnxmneiuJ0oQ9KzpTZqneIN6QAyxOrpJDwcXoBcHMSKJ1zRUah7bndMwyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuiODuzRWCu0IX576lrTj-uJGof21zulF8ofPBk21MEzyDjtziV7UyNQRDMhI3qrwWR9GiK-X-dvsq6r8F5gVVTC4inswnhaHMtTFrAagIk6iFpMGy1QDOXkicOf1fg6bh2coLHdQ5Odnj4ddAHt4W0QsdbQQIKlyFjsclZhAfYf53JvFJn7Jnlm-OisMNG06SY4r6Drhj9TSbp5jbi1kvRC0iHTm38-9Vb0uqSU-mdkeRm9_xeek6Xt7J-wKMlGMhnlZtPiM3rirC9W_dZz8BVAcTSGwuRLFOtxDAwlEDsW5MnTTHH8dYFvyh66iNi9_NBDKqBwQ4S3Td_k-6gXcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/getmI8s6SGw_0m2fqJvi7v1fTVxWRyhdGTTqlBjrxjBMaqm3urUeMCy4qhfdX-TTU0sj1LJ84NMT8Jlb5fDZT4iKa4cWGcaoaDqqGCFjabM4eK_bQOv6U4W5OVm7Xss4S6rMXdDHZK4UaVRr4EBC6yeP9IyLL0gSMhHZsMwOqz6Mm-HoGW6CWeyXMKwqtai75oxX8OWFzrweqsnnF--eJPz1lpChP4lvI7e-b81bUOzrP-xWJWkgmzD7KEJz1k9QV2GrHnPngZGnLp4L8z0KxQFbV8BVLOlYrKHLkHMXYWjqWXHzrPFg88JRfVM_x5mGcw6dm9Ha-0W6V3E-ECuCnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GsMtSEQzl-xkIqAp_sL-NDOnNbox9hgyI3KffTpyN_rifZ_IwXdSqx1KUf7BFtzWMKUd4ZOxeuVY5722E-DrGxCAm48iXPbWhpF7PjwgBkx2YN9GikxY_Y_Xfh2W4Dksc8K84Ln7eBLPhF6s-QFklLWPxMiIa7DuTOcCARDwmol5c_1qlLJ-iO7xKV1URP35NPF7zka_ROd8cf9MBZaYEYlK29GsoCEd8NSLPr7AWAwhks_eecrbqcVdBIzwPeIIhnbgT5VA4GBt3CRZmeuWfJv_vDuBr6rdY3KHpt1BmsylnxW7VpxU9Bm7509mPzzXQxxqTDIZMdrRX1XWBj_vAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hc95l3FfuvujLkKrlpOCjZu1uAlrLkTiyKqN20G0PkGsKcFnoZDEzY4K1bZkFocKfk4xrbFuwtVTCm44wUByL3gjj8aw4eUFZnWgFWIhZws6b9Zgm74FY469Chrop4eLQPAWVM7uxWUaXPnHTDaaJzk2eUCER_Xc51niqkEfzhiIxlTMeto60XheXbIUlr_j0JGsvYyCoh7HKqy60DUVun70pzwz-Ryd3IV6gatTqP-1ujLZZWTZGtKa40ewQmPug9o89qBlC9-wIIcfIM-EIeHkQVCqd-f-SWijjIdrKcit-R17jIna9o0gH-MNcXY-BCKNOXTEVIaEUodKfWqJcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8wBOUuaSZ6VCIARYxaGKXuW-y1KWmSs5edcujRzyf7TCAWAktX4K1bwJ2f1EUMchE2Cy02ZAUGrQMsLb3ezp1jdL-owG1NmU2LNK6R-f4qMSBgNcXTbJGWauZnywFXa7ERnRB7mKdszOHcL2HT4AEuLiBJHlUHGVdMN-GJw1DD6ik_OtfuqO5lwCn1lyRS_rci8Dj6UHBnCeNkOLFraSFC3us4nN-k-h-o1CJXAz6CORgLVd05-ulaSK-JsBFE1xeYXJ1Gq__3kNs_uqBnwGNK-URH1HJ6QeNsYzD0OD4ygYTXRY0fPpt3FG5f0s0mzozzBx-G15A1Ifjamp8PBkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4hDApW2muEUbYmW7gMl9jQutKFhPWoUc0I4jIULJ05JgTdtz0gb0IOhPM7rgyVJRpEyZgl91xFzlXi5je4_YHdMFb6gygmYazet_yIq_eGjjM0AuLQ_xonlVIkSpT9jxzyhGoMTXKzZUYJi-MNKDS2d4LMM2oFQxlh8IOtKkcn7JYaQ4h6k2k7IYoHW-A4a3PrNpeTdHD70hEVmYopxDwvt2ZvxS5Ng2EjN806dFJdyZW-o5c9sUAmjVcLKbhdWnupOUXn_sggodt0om4OV5nwTzbLrU7qieyNwA1FM10A8z8LhykldOHisOR7BMb_nT5HZKVl6oUUtFcktVARScg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9yxUuidXPd-KcViys1JrWZwymcG2U8Y9_EUr52eK9N7mPM7AGOBGQHJVzIMYZb85XWQnjaPikJVw8oGJnJ2viUbo2SmmcwsodYmu7eE4S4b3qBUrUadtZstG13aokLFRalrztNuvXOWmqUJHuVY5A2TeJK8ODeKZR4yZllZBm404WxcSxk2An2ff5wM0oCliy0dGvEA2DNwubF74GR_2WcGl_ZNq1_ocYtAJ_YxarqIK9hhkWYFj2o9uY6suuYPZd4cYORmeHLmKa0v9a--at6M9WFtgZLOEFFR4tmGvG1wjYHbHKoujDqWg7Eb9N5XcKYJs3FjCOmQDNlJqRCtTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_dLLjVWNDvbUbFM1nsEZlAeTECiaDxHO8S-RokRJ-PYjXcCy_7GFzoj63FSUTOJaYg5K64U9BUKuWOOb4wHiaxDapZUOh09a-WAh50sHXi-hqqvhQ3u32CvdqymRhHmA2nWf58ZlL-ofg6z2LyZpUn29k5vfnChIVKhGQsSHdtx4HR2JRn4Szm0uYFHu6PYcilDVNXxEjqpGC6GQrcaYY-vNG9_gKJrxdczlilvtD59FZ7DoWdFUeycI6YXGQEPJvHtpxwtL_ruC479cLYKp5uW5dDJFvyMi_fQ-jIzcM2a7dcU0nvoBp9oxlFTuaRs-93UJSrAIyb9BTI1NVWgWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=sM1b3JEbAvaB59oNaIpwybFLxV1lJ1yLvrLVou5ojhFQsiLRr3YYl-Ku5OLiF7u7UUMUKlwmYFkNhAV1fyyr3EwXNHnDjWU8sZ69t7Jj_sVQNRB4mgNCMj0yOl0PGIBQ6q5phJGdSOMuiCgwCu2ol_vxibSy5X8blBh3Jkzon_7hGTH8A8qQUPKSs6QhYu12M9509F_tQFzB6i_FDhYvOTN7EVGOp8bBGgyrQqUCgT3xEQmDQpfmmg2jj4cUoVISVXa-0RHQu33yYtrBfxzdSmxMTCVRsWLSrcWNkqIC-F18_TN8FvpKiEgKetvZbm4omMFrzHPu4v8NglSJWcxw9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=sM1b3JEbAvaB59oNaIpwybFLxV1lJ1yLvrLVou5ojhFQsiLRr3YYl-Ku5OLiF7u7UUMUKlwmYFkNhAV1fyyr3EwXNHnDjWU8sZ69t7Jj_sVQNRB4mgNCMj0yOl0PGIBQ6q5phJGdSOMuiCgwCu2ol_vxibSy5X8blBh3Jkzon_7hGTH8A8qQUPKSs6QhYu12M9509F_tQFzB6i_FDhYvOTN7EVGOp8bBGgyrQqUCgT3xEQmDQpfmmg2jj4cUoVISVXa-0RHQu33yYtrBfxzdSmxMTCVRsWLSrcWNkqIC-F18_TN8FvpKiEgKetvZbm4omMFrzHPu4v8NglSJWcxw9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quKK2zJjRUblmKovksY1jaJQeaYBJ3TrCtbOAymvL1dDXQhZJZoCivXGHrL7nmPmW49zSDMN4I-La2hahGTnTDzEN-_swz9Fq2ggpLVJLbDXWuUDszk9KS-opJtml9GxoFhILJ2tKuuoFgi7p6nhdlr6z49PG0nk6H8NrcZIFIMhdGFSKKLaO7kNP4N_NikAw1Tex62WaoPvf8TpVhva_U0Qw1kc-WwaRRkI3ACj8zUw3JhQ-bgnyUlLJA5OW6iFSSn76NlV2ba4HNPSj3mTYFHwhxJ1ifBFEqKVi1i9vNCpYm2fwWw6R8hlHlg9GvRBvz2FusLmKAnZTPFU5jOwNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joEXe2WcYyraPa2mdAezCtI_c-uW5dJr4gvHsPo1An1ZeiYGetaoB5_MdPtMTffFWlJBQ2iRkuHgm0uHFQJfYwVUc38Qa7DTM0YGYa8S_05qgniz0-dPYT1Td-tKrqdzFbGxZR1u2BHFMY1eKLdPbTr7Q5MfzXu9ZsyHeVq62EBWnYU-JlzBGPUNiGEfuFtoPc5ygcYfhhwdJg7CCoXJyE1WBxHBCNK9KAoaGhiATTgoFLOkEA46_W9pdFXDEXsrBz1VmhplUI274pq3tlSmARbRwTv8W2mgYHKEet0Dxy86BXLH2ofqarfimNPPQtT3Ns4eDWv2z1317yzUpJS4Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZxM1gWAsJO8vPj0pqYdCguZx0yYtAXsUsF8CNX2tDLuf6HBR_8ZB4c4YfRtaJcQkSRGMdkj7eTlu9g2Ux3vwycO80h9ePMWzyuqwhqHxLcrn1NjwHuVEIfgI1U3LqeTVtX9K0g6tsZU1tR0trTzjr90pb_IsC-mupW5AM5x6DRDA0llOZfRcXXAEYys-wkwc8AUNYOrHo5CS5S1LKtFyOz57CW-175q4PewLAV6L3cjqJ2NEQp7C2jcuDbtooya8FsuTXi-I6DlIMmU56nZeZKR_BeypxkF0Eed5SIXtKSkoxTbjFcKp4SsIXZP8AG6CQqJ-C5KYGPkx3cyNoPIqxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5IDCmauDOUG-Ki3bYXuJpykoqlbMU8sq62mau4tUgZxFBV-Y1tMeQ2FqesnmX0FNqWhHfUDzU5yIWXVVREWW__Hu2WPhy-SUSVfotEimsUxGssPNmLL4EZm5G88cFwvlzv540YVp1mClDgjSfU6VwW67qlqhzi7O7akYKm3oz6HHUNrct5HxAQ_u1-CQckl0EJzthdVJ5KQgSLQmFdU9Cla6dUwWyCDim-wQ1_6ZXkfSZ9fz3C9_ACpdA7X6N3I0rccDne6aXsq1vc8l6dFQL8ih8gkoVLa-VP75NXH59f31vzJaZxSRD8vontZBeSpbCvTKZidF44IMQyCvgg8Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjHINi_nSQmlsV9nUvIOHMp8T8AFKLS2PfwWJIz3cTYGKIWYUetv2zz9t6O0Lg6SAiP0XWI2JrUbhBaabpFEGXvd3lJKAFhzsphZ7PF2uH36bh-LGA1UhPawW-FAvXewWGf8z5_91atDp1Ufn2EViH75QefJWCRpxFNYDklnJqpunRbEi8_0KhPfZSK8iHzkb2hdkjTULbJSwAcJEtO00OqjqV-Xcz_Hz35KKgl4KTVWEeGWB7e6XGgNjbIfZS7dNArE7Qrg-ErDuRGm4e7rd74EjKgxm03iEFB35YEXe74vZcjV87MzqTGPUuDsxpRKuVrmWoFqTQ2xJC7XbarQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YIEQFBMSTowKTf9konG4BzG6vzStA0PvozFq-GCRRNcP5h9MQMQkRYfNSa_tbgIRJTnXar8ylrIjEGd4fxyGNMXurUsts_gNkajnaYuYuUwi5siEv0_zzX2W4LkchbUlGQY_xH3zOvC-1a-fKsz9gPrCR8PqWHD-7jGEiRI0_a1i_7AIZRuwNVW7SnsSGaK2EFx3HI7cD2klHq6rC4BDw2eRaCDPneDjZ9YKDZa8arRFOFleNffO6PeLHmN3PZzLx9v0iO0dlcwcFMdWyOfQ7i2UtZwKBKKUM7KxhvmVx5_SRaxYf3JkulSFJswkP2cNYeXTcD6TRMGnDyiyhbiCYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htYlNYxxzJKnuXHJ7oMStwBwwOOccBUr0NbVZL8CBbQZyaUJvm4uKUoo_Jl9ruqho5VpPdI9bnf9UHW1CtvpH-g35eHmlVYmmQHtyBRfATC0-rQP-D97pmEo6gJII9jcWwSplxSJSsJa5DviOF6VOlMi0hfNC61gUb6L5qdOGiqIOqxM6cJpiEFlLEkexIfOX2PLz47dK7ZhvdzZYve_aTTdAMOtdf4uhRG5Gmcq5v0-MFc1zbPQTY7p1e_0WErYpgu869dXBm65RPfeMu79GUBjdJ-ZF5YyAJvYwyWgJKe6uKEJ1969JUhigujoQqNJpFP8wC_blpjZcWknjH7Miw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=bB-A-v2qQXdhjAvbB5VomzD823CMcPREF1O1fMDAWoJMJMTwzQ-fSdqnQ1hPb74NBWGy8lsweEA5DQR6zkWuf3dbulYJ5_LsRGcG3h2pOEb5aenynAzYmNFK9avh9GOnhkfhlKe-rgMePGhzmUGJVM6j44H6f9e1m4kzlWGPqj19tZnQPoQ7tA6zIAiY6GmDx9gZ1MNki6L3DLMF_HwKTrSxxTSW1KGKssF0VIj-aQcsMBeHVASpmrHzEh5aUEnMoeagiXcRnKrzqmSNR1WwON2Krv66pfTDyZVU2bzuqJltG5RvIixaYQ-_QdelV4pA4ZbUQErCtfFm7ENP3nAJhBtwzW8O5g_sz6ROcw5-Ukg1JaCy1_IPB8BNKo6ditCOlgtAZLdPrD8bn_bWdk1knNUqTKhGyM0hsVY8hLpDvPSEdx52bknClhFGD_au8H07jCkkpx4diZKmMEMDCrl0eh5dOv7mR3aS55lN4q97gKKRVFbTBHdz6ZGrcauBGXteY7taocCEFldkT_OJj7nJy6og5njGAOHbER5w3p_1xuvw_m4JAbkr8CjB0D7R7uFgHORn5Zju1U3yT31PWwKDbB6H5Or0VwHTQXCcSAco5y2ds4roeQFDs9Ghj9YzOrv9KyLYgG4Ztjk7h7nlHli9PllOujrudXzvqZ8pkM8BYOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=bB-A-v2qQXdhjAvbB5VomzD823CMcPREF1O1fMDAWoJMJMTwzQ-fSdqnQ1hPb74NBWGy8lsweEA5DQR6zkWuf3dbulYJ5_LsRGcG3h2pOEb5aenynAzYmNFK9avh9GOnhkfhlKe-rgMePGhzmUGJVM6j44H6f9e1m4kzlWGPqj19tZnQPoQ7tA6zIAiY6GmDx9gZ1MNki6L3DLMF_HwKTrSxxTSW1KGKssF0VIj-aQcsMBeHVASpmrHzEh5aUEnMoeagiXcRnKrzqmSNR1WwON2Krv66pfTDyZVU2bzuqJltG5RvIixaYQ-_QdelV4pA4ZbUQErCtfFm7ENP3nAJhBtwzW8O5g_sz6ROcw5-Ukg1JaCy1_IPB8BNKo6ditCOlgtAZLdPrD8bn_bWdk1knNUqTKhGyM0hsVY8hLpDvPSEdx52bknClhFGD_au8H07jCkkpx4diZKmMEMDCrl0eh5dOv7mR3aS55lN4q97gKKRVFbTBHdz6ZGrcauBGXteY7taocCEFldkT_OJj7nJy6og5njGAOHbER5w3p_1xuvw_m4JAbkr8CjB0D7R7uFgHORn5Zju1U3yT31PWwKDbB6H5Or0VwHTQXCcSAco5y2ds4roeQFDs9Ghj9YzOrv9KyLYgG4Ztjk7h7nlHli9PllOujrudXzvqZ8pkM8BYOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfSbnTNDUo0TLdwYhXOBv_pwOZjYhETGUxZbBgX9GZea_NYYiergNaULI_SQLs6NR1QQSz3mFRkv7PuEgromuOYCMd6YjRl9LiMVGmucYiwswJq4u-4vZ-e5IguFoEM-Krl80aJwARPdU4DSqJAm_L7b_pHWbO7uiqWZ1qcgrpbA1r9VR70lspwXyldVGXyz1zJKCFOrKGwOxPDtpLOaUjtHNuKC9xK-wz_Bvub8-uCUnHt05di19Q5Tc87HCsZ4j5PvTBUrVWyFPbgpdXFJjWg6wE-Oka8HjrLAgxmYG4W5zyDJd780qeZLJMEJFiLckr9C2vl684EcJRLEwVT-Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bLLuQbSIkmDdk7WJT31Pk27TZLDlBQ54Pr4abFMQwN6ODFf_kWUQ5SiU5eUusSu1jxVFM_ePYUrq3JsrOqIgsFra7AEYc8_7IMPUPKMj3JxgqGLbpuitST60dO5LBptDPDgPmE-S1GlwgkeZCkG3eXDIFeZwhiKUA_D74QyV9TzETrEUPFqlAvV158i0EFrbMQICUCT0_6b933h47aiAMiaagJysS0ebRHkcDB9ZJYBR9w0rsJ7dJ7uWXU7yRsofc9qPgbpyXEE4jwcQwfSA0njraz12dLSSnZmiqJdb31RwjkFONnxhiLEwJLYSr6EaT0vowSYuiR4V5Nmt8R6XWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NrDwYV3PNmn4ZXruUJm0fO-KHeVpcBusIQk9Qk1xxxzSMcwac4o14NbkPzqkst-jbnhOlL--m4DVhbVjeLUSIPcRWwqNP-7g8GYYJGe8b33pbu_RJEFnI6bx_fw9eWA4OI5zvgaiqbpZD13j6Qa81ukJI_G2hZ5SMk9LsFDo6Y39iapB3vjK9IBWjlm9sPpHt-kPwSx2hwUFBrRTEVovORv_jYl8wWEs1qsili7oLmC70-eB-8ElMx9CQg-4btag62gHt7Wyjav9bxmdKoge2xEZ-Znjda8VgJHL3AWwj30vvy5brgy0IyCNuKFlRIoxOvfjA8Jwd-hFZijQ9ScYhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kg5QoAScGOxRkcteRjjTjLzlBfg2frdLf5DgBKfR6G-4TAphSQS1mwIazrT5GB5kIWAbWkIvpxlJOeWVET4AEi3-AoG9e49wqa-muTm2eNIX8lpCexFlNWKrdaJ3bl1kSEjL_cLb4OE998hcQnAQwl5bp_0Y3NNMyMKD5Krd-q4Wm5X6LOcTxWwcrIxciyP_2HlOuxn-Kvf2WN9mNY66wS16KVECPXrlk-Yx3ETSqCzeprnwm83rRr6lcfXlxOlGMLcPweK083ZN1UJfT-EIfsUFTtdBN-ajX7TPJBLEa-7WvqmZ6fD6iHqeXfQhJvTz_pN3Ll9PS66qagjtuersfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwDxNaK8MoSIOka9yntqJNesV8N5WHluBnCt_rIt6Uh1s3baboHlD9TyOQ4B6e7O9UL5LViZOMVxXqlO7zWyyx566WQFWQoz2NWd3m3_6fbWg3EEFwAQHlXS52yMSvD_KZmgJg0HSnTqOfxVan4S76seHmVYir4qK9uaC_8zvTNAPPoY_ht5uOe7hEVTwEaSpC2mRhlMQDsCybocFW0HgCAewj3tEs52joFni6DJ8srXgeshPL21bDgrLbuEoppiC5IoYyOmoA9c37ucNOKD3kvTXDuziJnUPg56fKKSWR6-xH4UvCcElgwKvqeQo6SuM6kYa4K-wRZ3Qt5rau60bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0UhQYo4Q7wVIWzO6jfZB5hZgoo2lnXRJwD5XRbZU14NeOa80rYl58jnAQpSjshJ-zHo8HXmTfpLEpbXfa7CCSgYH92Jf3Y87WrZDuqkIrCH_33YERijZNZOyrPLjcidB-AdKZXPV112SETPLLbW-uv9RG1sV_BRptBZggc92WDT0egseM_1kwTWg0t-k2P-_MQ7D9sEX4AUIM82UiLckSmQK8RPpxlbTvvITMDzmP3N3YoHPaOutOXS_Xd5w1bilycO8nx_-niNWH4IR-EJ6V-w_rBGBheZLdbaywztvCh_jFhQyiGxrSKF7P1TphI86P60u01KOcqLgU8UTXag_txQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0UhQYo4Q7wVIWzO6jfZB5hZgoo2lnXRJwD5XRbZU14NeOa80rYl58jnAQpSjshJ-zHo8HXmTfpLEpbXfa7CCSgYH92Jf3Y87WrZDuqkIrCH_33YERijZNZOyrPLjcidB-AdKZXPV112SETPLLbW-uv9RG1sV_BRptBZggc92WDT0egseM_1kwTWg0t-k2P-_MQ7D9sEX4AUIM82UiLckSmQK8RPpxlbTvvITMDzmP3N3YoHPaOutOXS_Xd5w1bilycO8nx_-niNWH4IR-EJ6V-w_rBGBheZLdbaywztvCh_jFhQyiGxrSKF7P1TphI86P60u01KOcqLgU8UTXag_txQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q96I4jzDo5BUBXHc1UZV-O8qOE338dggmliwGnVaY2OywGjsKZ15F954M84BT7q40h2qnU4mWESbx9tOol8y10tBRLkbFn5izXcy1aDFFaRpA-zgwfHkG2c48TLOupp-ge5Wf9Q7SwQ5-Y2A5eheuY6-CGccqxFwQUPahuDnUKvPLPnHNWlZ83VqJuUVobAN66On2KPdM88F24qQQLV0hLGgmihl6Adkz0sww2drKIcQk3irOqGhAu5msvELX61Y_hnB8EKbs2nUgTAnwUb5FH_ctPrTT8U_OvHI0_Ti8zpU5Z_KtN3Ofc9of7XGSiKWVoVYG5Ob4C2WA6FlhRriRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
