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
<img src="https://cdn4.telesco.pe/file/e8zjN7w8JGJmu-poBtrnMpWKpmwWog1meAAtnsUL6k1IMeQ0Cu3hUnYPL9n9b5sICKrH45WZZtowkTJ9aK03Aw3MNyNv43NRcIojLHQnRip_Qea52HdDg6E190xB4JHxhS4dohhosyv7-B3V_-Xcq2ATnjDMxarkmYCi-bMBFJneu6J0J5ONZk9p_9KEPtgXJYMWHG5E3fe2JmXIw6Hm6g_zd_ck6w2s7gVGJLWt28k8dMTcqMZM25p6MdfzzP0VWsLk1KyTs24TsngWq5uSNJveD_MBvqO-lX0JTqDpmGEbB5T3_Qxb9zc31gphFDKfid_PjoZCcWmCrd6kLVEwlw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 22:01:32</div>
<hr>

<div class="tg-post" id="msg-136039">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyE_YAzhrOqArP34FUtJGyZhkuz0rzzXSuK3Hrz1NppYVF5htkI9BJQg2ikibw5eFWFF4PuJhSjHc82LzM4r6qjd5QhrMVHI3NdFumIAk5nTQKATLFwnqM0iiw5s-vVwDPAkqZnLoYSlxPq63DdE8tXnqwzvsLPwzCJKdVt3im-2DTklCfFnSNs2dzh3y70UInHe81DUxQsnN15ccv1_0SouU9fiqew-jcpbhUCM2G09wd-a63OwJ_PCBkIUvMv55zr1xCFJ3KKiMqSjQZvNOGM_kKbA45FFNRk-UmXMp_Po5ZU8hCdgbT5-xWiopOTyeTzxw3nKWdTG3KEvzJynEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
عجیب‌ ترین بازی سال در لیگ یک رقم خورد، نود ارومیه با 7 بازیکن مقابل مس کرمان به میدان رفت و بعد از مصدومیت یک بازیکن، مسابقه به دلیل کمبود نفرات نیمه‌تمام موند و با نتیجه ۳ بر صفر به سود مس کرمان اعلام شد. این تیم پیش‌تر هم یک بار در مسابقه‌ای مقابل بعثت کرمانشاه یا تعداد کم بازیکنان حاضر شده بود
😂
😂
😂
❗️
❗️
نود ارومیه به دسته پایین تر سقوط کرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/136039" target="_blank">📅 21:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136038">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5faf86265.mp4?token=QluCx1qJguw3l9iy8yMuIOmZJsqaPPypXfr-ZahXJYzacWM_LwhCKefEco-Ep85lvU_KaC5d_ZLOftkDCUMguvr6lPSQYkGPba1wnK42kC8MyXPd4cz-mnIr5wVTdXAl2jbXkksvLAjc4CJVbNN_eR-khIyeMq_p79Dng3LpT-kMP95NV6Dx4VQi3tv6udb6sq6fpjFjkAgPf8RIkKidtu0LPTkXMjMK9u5wdMz2O1mUpIwW1kdLoBLUUuO-FDuGKbjTIPFPcTUm6Vh4hrdj249RI-Rhe0lJUBB1zs6e4-ODAA0oaasy7j1BHMBfOMgtw4qn-7mubL5a3bB-kKy9Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5faf86265.mp4?token=QluCx1qJguw3l9iy8yMuIOmZJsqaPPypXfr-ZahXJYzacWM_LwhCKefEco-Ep85lvU_KaC5d_ZLOftkDCUMguvr6lPSQYkGPba1wnK42kC8MyXPd4cz-mnIr5wVTdXAl2jbXkksvLAjc4CJVbNN_eR-khIyeMq_p79Dng3LpT-kMP95NV6Dx4VQi3tv6udb6sq6fpjFjkAgPf8RIkKidtu0LPTkXMjMK9u5wdMz2O1mUpIwW1kdLoBLUUuO-FDuGKbjTIPFPcTUm6Vh4hrdj249RI-Rhe0lJUBB1zs6e4-ODAA0oaasy7j1BHMBfOMgtw4qn-7mubL5a3bB-kKy9Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
میلاد سرلک تو اولین بازی دوستانه فولاد مصدوم شد و به نظر میرسه چند هفته نمیتونه تمرین کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SorkhTimes/136038" target="_blank">📅 21:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136037">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
باشگاه پرسپولیس با وجود داشتن پیام نیازمند، معتقد است با توجه به در پیش بودن جام ملت‌های آسیا و اردوهای تیم ملی، به یک دروازه‌بان با تجربه دیگر نیز نیاز دارد. در صورت جذب اخباری، امیررضا رفیعی به صورت قرضی راهی یک تیم دیگر خواهد شد. / تسنیم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/136037" target="_blank">📅 21:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136036">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
قدوسی در خبری فوری
❌
احمد نور میخواد برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SorkhTimes/136036" target="_blank">📅 20:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136035">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/136035" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136034">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/136034" target="_blank">📅 20:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136033">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJdpE02S6eTL_Yy9oAQFDEOT9Aevwmj2HsxyYESVQkVkLKGbmNWGs9rs1kEJKXoWWJSIAEYg_rp8qpE5ab-mds2vLX3gVshlOhhEHad5uUGfVYGRvKGkqcwFSAaB74N5wrc7bGb38zuH-ip8z7If2Jhg3l9T8OKN2SQ_YnEMF7jOvURL_butBpVWdIEWqUxEWDr8aGiqGYiuTmNImmkK2x85kAswx9k-p3rw0lamp4f08723x1XqwWx7PQP2J6f-EVTBd_KbFwEiTKl_rqNzlc88gFPwo061zmEffsYApDBregD_Jbmqj4GUVbF9Gb7omXlI0NPH5dVhx9Zzzd8qVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب حتی با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🤷‍♂️
@PeakyBetBlinders
@PeakyBetBlinders
@PeakyBetBlinders</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/136033" target="_blank">📅 20:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136032">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
باشگاه پرسپولیس درتلاشه‌که‌از بین مسعود محبی و دانیال ایری یکی روبه‌خدمت بگیرد و مذاکراتی با هر دوباشگاه آن‌ها انجام داده. امادرصورتیکه بر سر رقم رضایت نامه به توافق نهایی و کامل نرسد به احتمال بسیار زیاد قرارداد مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان‌پایتخت‌یک‌ساله…</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/136032" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136031">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/136031" target="_blank">📅 19:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136030">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
اولویت در دفاع چپ با میلاد محمدی است.او گفته اول طلبم را بدهید بعد تمدید.باشگاه هم گفته کارها همزمان انجام خواهد شد.محمدی هنوز توافق و امضا نکرده است.
🔴
الترناتیو میلاد محمدی رزاق پور از  فولاد است/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/136030" target="_blank">📅 19:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136029">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
فرهیختگان:
🔴
باشگاه تراکتور همزمان با علیپور و مغانلو درحال مذاکره است
🔴
شهریار به مراحل نهایی رسیده اما با علیپور بر سر مبلغ قرارداد تفاهم ندارد،
🔴
علیپور درخواست قرارداد بیش از 100 میلیارد تومان از باشگاه کرده که فعلا مورد پذیرش مدیران پرسپولیس قرار…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/136029" target="_blank">📅 18:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136028">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووری از تسنیم
⏺
محمدرضا اخباری در آستانه عقد قرارداد با پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/136028" target="_blank">📅 18:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136027">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
#شایعات
‼️
با وجود توافق میلاد محمدی با پرسپولیس، مخالفت همسرش با زندگی در ایران مانع امضای قرارداد شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/136027" target="_blank">📅 18:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136026">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
مهدی تارتار پس از تمرین روز گذشته نام کاظمیان را در لیست مازاد قرار داد و قرار است کاظمیان فردا قراردادش را با پرسپولیس فسخ کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/136026" target="_blank">📅 18:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136025">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
🔹
تارتار کاظمیان رو گذاشت لیست مازاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/136025" target="_blank">📅 18:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136024">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">💢
💢
💢
پرسپولیس در حال مذاکره با محمدرضا اخباری برای گلر دوم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/136024" target="_blank">📅 17:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hseZSkSQLX-z2_JVyUw8MTdDWCtwH-OmEM8YxtX01XDnBxEdKcLAvD6NZcCybpCSh5t-fvsHyzpeqsviN93JqP8319wx_EDtNcABcJ1iY293k_5oXVK92tcPY8C5jRufWZqezrvPO7QruuswPGMYbPM85kdXdSoxMQ6F_wA6kZL0HQgeOS6ZDqkOf5bxwtv0EzLLPfoJt__Jn258uAfv3XzAFli5_WKNIF_DxemE_Vwv7dW5YU8sJhgw6FmaiTweQ4qCKqXURo8cnRy6okruaiBlcR49ABO1YryP2x9mM8n7rthM4g327_mWuqVw9doNlAC-22kA6F1sAUM2hXFc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
رسمی؛ با توجه به پیروزی ژاپن برابر بلژیک بقا ایران در لیگ ملتها والیبال قطعی شد و حتی اگر دو بازی آخر خودشو ببازه سقوط نخواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/136023" target="_blank">📅 17:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136022">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/136022" target="_blank">📅 17:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136021">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/136021" target="_blank">📅 16:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136020">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
❗️
جذب لطیفی فر کنسل شده است / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/136020" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136019">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
تسنیم : سامان قدوس در لیست خرید پرسپولیس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/136019" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136018">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKkUVEvPzRmFtDlmGolsrb2biz7JOz-0AL-udBxX24V6PBFaVIxSuutiE2muOCQjCNV6IHHz-nVS-m5wMeMiFzyxWVB53OL9WMS03uXjHWidfsBfbrf9Uhm9bgFTqPX6DiVHvvq1ZoLg6N4RA5V3fXkrYbCiB6GNIxdRAf_6odxJdqr2JG6xFpZyOWaU0mBXmeYc1SgewpSshUGQExmf00FhiarWNdkJr3WMErC0r1npOkOpUrQuNqeG8g4vgZJDehPRsBca7OKMOFTOAhrPtyKaeKsmTjFvP0m2jOI7YpNyAGJmdIRFgWedXLgU8Zhwtb3k8NuiMv2pOVUuVupH_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تو 24 ساعت اخیر سرچ «لغو عضویت جانفدا» بیش از 5 هزار درصد افزایش داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136018" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136017">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
تسنیم : سامان قدوس در لیست خرید پرسپولیس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/136017" target="_blank">📅 15:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136016">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
❗️
اتحاد کلبا رقم‌ رضایت‌‌نامه سامان قدوس رو 500 هزار دلار تعیین کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/136016" target="_blank">📅 15:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136015">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
با جدایی سرلک، محمودی خواهان شماره ۱۰ برای فصل بعد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136015" target="_blank">📅 13:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136014">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
✅
سامان قدوس در فهرست نقل‌وانتقالات باشگاه پرسپولیس قرار دارد و سرخپوشان به دنبال جذب او برای پست شماره ۱۰ و جایگزینی با رضا شکاری هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136014" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
چهارشنبه هم گذشت و اورونوف برنگشت !
❗️
روزهای پایانی هفته گذشته اعلام شد اوستون اورونوف ۲۴ تیر ماه به تهران برمی‌گردد اما هنوز خبری از این بازیکن ازبک نشده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136013" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136012" target="_blank">📅 13:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136011">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
یا تمدید یا خداحافظی!!!  فرهیختگان: میلاد محمدی باید سریعاً تصمیم بگیره قراردادش رو تمدید کنه یا بره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136011" target="_blank">📅 13:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136010">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
تیم پرسپولیس که قصد داشت فردا برای اردوی اماده‌سازی راهی شهر ارزروم ترکیه شود، با یک هفته تاخیر اردوی خارجی خود را برگزار خواهد کرد.
🔴
🔴
پرسپولیس روز ۳۱ تیر ماه برای این اردو تهران را به مقصد ارزروم ترک خواهد کرد و احتمالا دو هفته‌ای در این اردوی خارجی حضور…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136010" target="_blank">📅 13:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136009">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136009" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💛
آپدیت جدید اپلیکیشن اندروید MelBet
❗️
🎁
کد هدیه 100 دلاری:
giftcodeir
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
آموزش ثبت نام و واریز
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را فارسی کنید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136009" target="_blank">📅 13:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136008">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">💛
چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت
💰
هنگام ثبت‌نام با وارد کردن کد هدیه giftcodeir بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136008" target="_blank">📅 13:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136007">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J02cszmE7EKq1QE_02OcG2dASC6ke3zKCVr4lvdJ37CBEEIAx3FsQSApckUvDAah6sNmxmQm1botxBko3bLtNijJaArE5gRB5S3ezh-pTpxyIb1xxIX8SqZgRZJkARb_Ent9N3d5Z2S9Xi9qXLgoTRHi6P4SCO6a5htCa1QK6OMBJeYMQd45_1gMGOmqnZevNE0_QfoHppJ-zzrtlS2cVvAp3fZ42zn7mkJPMxpDVF_LwqCPsGzfn4-SuQK1MBWGnXOqmn-zMd8lg4lb0omnhYpFEFCAOlkBhGlv6js3NWNZ2waaUI-3ekCg8-U-eS8uWVsjYGx0PTW5S-SctoVRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
چرا هیچ خبری از این بنده خدا نمیاد؟
❗️
حتی باشگاه پوستر خداحافظیم نزد براش
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136007" target="_blank">📅 12:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136006">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDzk2dfOgXkB9HVbdZ4x2iRchkuZP0dvj7jOx4Guqag0csvKV391ZrMtOIUtqmW0JiResKxaeVgwn2qgSJ7NM84C3sPwXsRnVKbx4mfR_TBZdYWuMlyd02u6v4Q0XUsgH_ze5jrAy79nGK03W8dsY26x3RuixIQ7fLsYET1ZFmoUInvqT33vq9JyS3KAfIN-pes1UPQk-SFrSNS5R8maNddFso1LU2wveEWMLSN-RmhEITqtJmy9kZtMhh2B4IZEmM8ml_0K136e8rziDoKWG8g14Tip3EP0RKl87NuyewXTrlDsSgmqfpYeNe1ngraaSchU9YpQVALzeaqK-BUNKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری
/ فرهیختگان
🔴
با توجه به بندی که در قرارداد آسانی با استقلال وجود داره پرونده حضور این بازیکن در تیم های دیگر در لیگ ایران منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136006" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136005">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
ابوالفضل قاسمی به پرسپولیس پیوست
❌
#پسر_پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136005" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136004">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgW83K3PrbnKiT1PHNNK8N4VScrwiTKwKpWCSdqtxmgq8P0FQlAvpGXxWg1b_yiJpAYBEZi5AuqCMjtAMY7XoJn_ANcCyL02u19wYmu4OxDzVdH1Qj03m7DXUJslMi5iUNfXqAhImgT9rEG-VDxescODAEMS36alyLH11Y-vMphxyrc-UjIRExCL7hsNNgqbyRQSCq6gSyzenrofp16CKt7aZ4Jz2SQahtJE30lR6S62M05MY3TRmyjrFJoS1DD_Xl1bK9RBm0BZS2v3bSGhJnEg5RtxzYr50lMoQuRQBwCTg8KDzHWwTdt5CJTsDndOFeb3XBQ8-lFUAKLlwYbcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل قاسمی به پرسپولیس پیوست
❌
#پسر_پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136004" target="_blank">📅 11:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136003">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
برای این نتایج ۱۴۰ میلیارد پاداش گرفت؛ واکاوی پاداش تعیین‌شده برای اعضای تیم ملی بابت راه‌یابی به جام جهانی؛ رقم قلعه‌نویی، ۴/۵ برابر قراردادش!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136003" target="_blank">📅 11:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136002">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
برای این نتایج ۱۴۰ میلیارد پاداش گرفت؛ واکاوی پاداش تعیین‌شده برای اعضای تیم ملی بابت راه‌یابی به جام جهانی؛ رقم قلعه‌نویی، ۴/۵ برابر قراردادش!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136002" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136001">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
✅
فوری از سپهر خرمی: پوریا لطیفی فر به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136001" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136000">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/136000" target="_blank">📅 10:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135999">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
✅
باشگاه همچنان موفق به فسخ توافقی با بیفوما و گرا نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135999" target="_blank">📅 10:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135998">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
فوری از سپهر خرمی: دنیل گرا به طور قطع از پرسپولیس جدا میشه مگر اینکه به لحاظ مالی به توافق نرسن چون سلطان یه فصل دیگه قرارداد داره!
🔴
🔴
البته به نفعشه یه پولی بگیره و بره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135998" target="_blank">📅 10:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135996">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📌
۴۰۰ هزار دلار کمتر از ایری برامون تموم‌ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135996" target="_blank">📅 10:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135995">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
احتمال خیلی زیاد امیر رضا رفیعی به علاوه 60 میلیارد با لطیفی فر معاوضه میشه و توافقات انجام شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135995" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135994">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYBZNpSvM6Nx1cgWUZcMrNdR2d1Z7op3ujn6LHFI0ReMbowtuIacWTe4y30CQcUy77ODrPQ2r5E2Y3AVvOHG75e-Y5oUGmvqwh_ECAQ1o6ETkvIb-nCAP7AEqDc1cFRXZ8E-kJCpABYvOSFnGptOaZdvk9L-qwa2ptGvVyfUQ9Pd3s4Y3MrQv8rCb2FWRnirALSrOaEo6M9FsKvQVQL6Xy0WUoNEsot_O3EiwBPY8xU7q0GNcFpLYkyPvxXOGfCfKX-zEX4hmlqgKvljeGLjaxCcZ1c83nVytSnT6AceT98c7_Ykn1NQLXMd4GL_RLf-uq72ZaV2sJRs67ulRHzDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برج ۸۰ متری کنترل دریایی چابهار در طی حملات آمریکا بطور کامل نابود شد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135994" target="_blank">📅 09:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135993">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135993" target="_blank">📅 09:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135992">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
داورهای بازی فینال و رده‌بندی جام جهانی مشخص شدند و علیرضا فغانی در هیچکدام از این دو دیدار حضور ندارد.
❌
بر اساس اعلام فیفا، اسلاوکو وینچیچ از اسلوونی دیدار فینال جام جهانی بین اسپانیا و آرژانتین را قضاوت خواهد کرد.
✅
همچنین ژسوس والنزوئلا از ونزوئلا،…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135992" target="_blank">📅 08:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135991">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔺
فیفا قضاوت دیدار فینال جام جهانی ۲۰۲۶ میان تیم‌های ملی اسپانیا و آرژانتین را به علیرضا فغانی سپرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135991" target="_blank">📅 08:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135990">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKFDnVQJ10dOfTFL4Zs7pUJNKyaQEHPA7a9aMTeU8McSXN1j4HFQw2N3OlBAp8_J3yzJHn6nMbp9pufrr5kUMCH8KMAbk380QSP3xUAY0ANY0rbiJq69--bceqo8ah2HFlm-adPIp4BXEBDigpUKsB3vkYM9zpCZi-b_OssgNFqoGe5O_l6tbBcqQ8APGSfpzrlwpACJ_E1a1MT2X-HrUxE88GBMojzcWRMWsvUgHEP9maUWYQedUMmyo8NYvKYEIV1fMk_du5ZJy99M68dHMxGRu4Wb1sG-GXgUB73MFDiIsUOlMACzmL6YLrzqPN0c3lhr_MirjL1pn3PIFVoEUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس ممکنه زندگی نده، ولی
شادی میده
عشق میده
اینه داستان سرخ...
❤️
‌
سلام صبح بخیر پرسپولیسیها؛
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135990" target="_blank">📅 08:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135989">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135989" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135989" target="_blank">📅 01:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135988">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCTLXvyTBFFeqvY55aCFYVWWViRVoLuCR-YpeSkBjHHAgUw59CU6VxgHI2-qrHN5iz269xX93VIuOf2n-jmHq3vUtWARW47DtaxnFd64_MbSB-Fa5HWplcudkUAjcxZ4GGk54y12eUngbJRdV6NLVh5hoxzRbFkN1_3ftZp7x1pELY7P6ySmc4IDsi67KZgQ6Y1sX9nWeROb8emrQEAInxpbkSKYw62YiDz5XR1ipqbJ0j3qIf2-LYEEu-P8_xCKSNLI4cy3ylg_IM1CiBdhMHIZL8VIXzEPT-omLSR6dA7-4Lr19X0Gd4vWLdjVPrXAfKE9HHQ98AJLzdw2JbTkCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135988" target="_blank">📅 01:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135987">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135987" target="_blank">📅 00:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135986">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135986" target="_blank">📅 00:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135985">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/135985" target="_blank">📅 00:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135984">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/135984" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135983">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
یه خبر نصف شبی فوری، شنیده ها:
🔴
برخی از کارشناسان حقوقی معتبر به باشگاه اطلاع دادن کسری طاهری میتونه برای پرسپولیس بازی کنه و باشگاه داره مجدد واسه جذبش تلاش میکنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/135983" target="_blank">📅 00:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135982">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم : آمریکا رسما حمله به زیرساخت‌های ایرانو آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135982" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135981">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
آمریکا پل کهورستان بندر عباس را هدف قرار داد.
🔴
این پل، بندرعباس رو به شهرستان بندر خمیر و سپس به بندرلنگه و سایر شهرهای غرب استان متصل میکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135981" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135980">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
آمریکا پل کهورستان بندر عباس را هدف قرار داد.
🔴
این پل، بندرعباس رو به شهرستان بندر خمیر و سپس به بندرلنگه و سایر شهرهای غرب استان متصل میکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135980" target="_blank">📅 00:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135979">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
آمریکا پل ارتباطی بندرعباس و شیراز در جنوب ایران را هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135979" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135978">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم : آمریکا رسما حمله به زیرساخت‌های ایرانو آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135978" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
فووووووووووووووووری
⏺
ارتش اسراییل: آمریکا در حال نابودی زیرساخت های جنوب ایران است تا به راحتی به آنها حمله زمینی کند و سپس به مرکز ایران برسد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135977" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
🚨
حملات در جنوب کشور شروع شده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135976" target="_blank">📅 00:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
🔴
موج جدید حملات سنگین آمریکا به جنوب کشور آغاز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135975" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135974">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQEeW7wYrV0SHDFvc1nYnRv1zC3hLyX-IDL8wDstsmuxsoScPvUlaWyhuz9QJeT7rCkY2aEhC2j7-__8r4MSUaN_aIA2tZTtxpZPYDOzGzQqbbOFxydzAAgIm3wHaC2c8mCOjXxSqPiMRZw_rweCvMzlaMTl8YefLH5AsHv6-_zyeeQP5bGbDA6xBgN7jHisp_zmvpkfYl1C6fs4fQN8VO7GCxGSXsNK88xv7MP4vam5eoIb9j9eYdvAVAUB0r7jTUabBwDECfErG1J-_0bfWs_-Wp5HpgiuqeqBn3q94eOQS8orAGmHB6WhtcWOaddQV8p4i3iG0g852bdFuXh0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور رضا جباری در تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135974" target="_blank">📅 23:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135973">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zgy3CGdAAHnb6x4p1ChXE_ouApecij3Qc6GiiyodZy7vVfscRqxhsxsLq4OpEsetHmBMfR7cg1AVrW3zHc2E-YrALW0t67fJzpT-paT3aCjsRuWonLdnuHUSqU_0jbFGymbKCV7M2g-wWKjrZUeM3cMW__giKNOAVd6H8QLaRo0zEg-F2dQrffBgKOJyuBWAOc5AEkYW2J5wXIq08qHlv5Rl_T2IUX4eZ2HQApiTYyXFll2fEk6ECoC2YOwT4QVKe_WFUMNmtpSAhXMX28T-tckaRWEnCa1obxmQ4mJz5_OqE9JC4Vm2miZ40gIhftqFBzSC1XFk64NnAusXNSSXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری از تمرین امروز پرسپولیس
با حضور علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135973" target="_blank">📅 22:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135972" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135971">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeYcUww6naJADRgdzk6v3s26VVVUGiWbMBw0CHhOxPz5JqNWKH_lCa0vW01HXWtny3EGlQFCxqxsKLXrx44bVHBww9YpK9TeK8YC1TGQdDdNzcBSetbkKCNIaO1iIps0kiWTPdI2MbHahRDw1XKyBp_1K-ThmfUDy1nUker4IFxy9WdyHOVcf5UW8XT3fA6bE5XHxG0Tbi2JxKVmhnq_R75fs6h4JLds1Wq8PDT88JiiIVx4J5osw3lrkaIPUxBw2vEiwKtnkoL4Rqr4B6IOUUPylE_YIzb-FSBDWskNs8zz1JbEEo6FsRtg7x8SfiM8DB3uT6t6lr0R04BC9--g1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135971" target="_blank">📅 22:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
صنعت نفت آبادان با برتری 2 بر 0 برابر نیروی زمینی در رده سوم جدول رده بندی ایستاد و حریف مس رفسنجان در دیدار پلی آف لیگ برتر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135970" target="_blank">📅 22:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135969">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">#شفاف_سازی
🫦
📌
ببینید دوستان لطفا به مطالب جهت دهی شده توجهی نکنید این مطالب رو رفقای اقای زندی میدن بیرون که باشگاه رو تحت فشار بزارن، همونطور که چند روز پیش گفتم و امروز هم اشاره کردم باشگاه خوب نساجی نقدا پول رضایت نامه ایری و طاهری رو پرداخت کرده که بتونن…</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135969" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135968">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">#شفاف_سازی
🫦
📌
ببینید دوستان لطفا به مطالب جهت دهی شده توجهی نکنید این مطالب رو رفقای اقای زندی میدن بیرون که باشگاه رو تحت فشار بزارن، همونطور که چند روز پیش گفتم و امروز هم اشاره کردم باشگاه خوب نساجی نقدا پول رضایت نامه ایری و طاهری رو پرداخت کرده که بتونن با دو سه برابر پرداختی شون به تیم های دیگه بفروشن این دوتا بازیکن رو…الان که باشگاه با علیپور تمدید کرده و زارع رو جذب کرده،مدیران نساجی الان زیرش زاییدن چون سپاهان سقف قراردادش ۴۵ میلیارد هست، استقلال بخره هم الان به کارش نمیاد، فولاد هم بودجش در حد سپاهانه… جز ما و استقلال کسی دنبال ایری و طاهری نبود که بخاد پول خوب بده الان به گوه خوردن افتادن مدیران شون ولی با این تفاوت که الان افتادن تو فضای مجازی و دارن کصشر تلاوت میکنن تا هجمه وارد کنن، بگن ما موز میدادیم کیلویی ۳۰۰ حدادی خیار خرید کیلویی ۲۰۰ اقایون جای این لاشی بازی ها بازیکن رو به قیمت بفروشید که اینجوری قهوه ای نشید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135968" target="_blank">📅 22:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135967">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
قرارداد علی علیپور تمدید شد
❌
قرارداد علی علیپور، مهاجم باسابقه و ملی‌پوش پرسپولیس، پس از توافق با دکتر پیمان حدادی، مدیرعامل باشگاه، به مدت یک فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135967" target="_blank">📅 20:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135966">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUjzmvvleqC9X92yHyvlZRE21fBztZB69Z70MdpxyTzda10ID-VKGuGvyHyaMINuNlibAoqR3vYENrw6-c3jA3wEQ7t9ruLnAIq4IRP_T6n96OrWjnoy_NEUefs9hiNnF7i7EC9458dmb0g1NP7BzcM4I1t91xd_CR9wSXcthJVCTPn1pYCdVBLLc7bmvOH3Ghxb-U6grjyKuN9pX9lsnFVuDrUtjM__YebqMk4FsOzqoJoiB1p1xRFDp7m5FRiCnre_yisyxsFCMsMV4Kr7czkMdgr8IBN48XaSfDILaScVoJHf8hCmmtHfInJRNkAPpybhEFszJbREYRRuhTdUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه پاکستانی
😀
اکسپرس‌تریبیون:
❌
بعد از از بین رفتن تفاهم‌نامه بین آمریکا و ایران، پاکستان تلاش‌های خودشو برای کاهش تنش‌ها و ایجاد صلح بین این دو کشور متوقف کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135966" target="_blank">📅 20:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135965">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135965" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135964">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135964" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135963">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhPY8c0G7we5fcRbbfPB5yaJrhYzzQec8e_afFFVaeE5zaOu8B1KGOVjo8Fp5WNIz-_9LS5DtVc0T9DBwWq9kF-hSqXdHQ6-m3w4xusOUKuoDZZwGHzTJNEB4M9EA5tOKI5N1HWERtuqeH2UOoxlWnF7LpewiQQoI9DOyck-I6wpmXMo5ifrkWAPi_bfzXCEU-xU4gVmZBpJdaY8JN11IpzUWo_cywJ_fvVpqmEVEFBfWkdpk7WBR_ulrgJUQO1tou_DtZ9sK1slIK2om837MN75bG44F5UYCStMH_P4HkONc6N-J4aOCT6wqdL6Ea_HwhzYzmhepdt9Y04Mtms3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135963" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135962">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N00o_dy63aDhT_W7B6oe2M8mwYQIXJHMoPEm2dWNUNdZ6nm3DkCEHTp1R5CZH5bRY2sL8A7dKQwwQQVYi-Q77cZqBI0AdxGx0G5qVPNuu4FlRafm9HxotiFbSImx4Pc57gjqeekdY7wRKPp3Oh9OdWcTs801VU93MqWFpOq4XTvAhjj6BRu0ienfbvnMOcwGj-D3MGiKKDsFpJTDLnqDwTxlIk1BuD3j8nM4q3XyenPfMsgztZaL-CMz1qBF8rACMxvZ8bpQWV-LVUQqp2w7uGzQWjyPD-h3wZRtLEfbktuQfV-31ZAJwIXXaB62E6mxslzuAhItyMmxpg3AgT6Q4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیم ملی والیبال امروز تو یه بازی جذاب 3-2 مقابل آلمان پیروز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135962" target="_blank">📅 20:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135961">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
❗️
فووووووووری
❌
فرهیختگان : اگر میلاد محمدی با باشگاه تمدید نکنه ، مدیران باشگاه از مدافع چپ جوونی که با اون به توافق نهایی رسیده‌اند ، رونمایی خواهند کرد
🔴
گفته می‌شود تمام اقدامات نهایی خرید جدید تیم انجام شده و این انتقال برای نهایی شدن تنها به یک امضا…</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135961" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135960">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e071e1ff46.mp4?token=Ee5xQK4_RGRG9m0fGQa7XP1JWySW0Vgjx36HisGqcHJJ6vioJdF2WV3r2DudKxd0ETWcgJc9idVAUZkfMbOK8sHeOytosazl5xkwCgymxClhw3yhh4u7lVYhMkWaJ_6vXyhnWdrCUWEJ0gxIA4v0ewHA7kFUn6qprDDLctVfObdj30XyIf3ZUUf91anOhJ9inQy2wlK91tNQ5wwU8N9np2a9EPKy7Cs9ewEliKDKGPgrtBXqCeTxbwEqtiVk0MwNUHGMaCvVzC-JVQzMWdj6FYQ44f9aCzraYK94my2qlTxt68q0QQzlIUTLPyAvtbAmFVaicj2kLq7IAIIuw2sgp4Nk2vKMfULPHiz9aYhwzUBbGk9mgW3_-bWUMd0k-hR_mFPV8PqZwC51EleycK4Xi-417087FIhlS77u3cFsSySN_BZksh5Cs-GKb3LvGsRy_04BuzhoR5nXuNXlAnz3CrGPAINLT3weDAFDuZTKdG9h8B-ByxWX8CYPMiecv2WkMJMLzfqjW3gnHYri07sbkt8qXMoHhcEzGGzM5FiUIuH_B_g8IOU_8q13K1vqS3zohV_Rfq4_LKBJhA6Lu-zLNJWUUtltGF39FMBVhwf-ZhUgHzNkpYvwXGUAEizFcSg12149Ms1q4VZRXgud82KJvwVXh9Gg4B8UYp0UpW0loUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e071e1ff46.mp4?token=Ee5xQK4_RGRG9m0fGQa7XP1JWySW0Vgjx36HisGqcHJJ6vioJdF2WV3r2DudKxd0ETWcgJc9idVAUZkfMbOK8sHeOytosazl5xkwCgymxClhw3yhh4u7lVYhMkWaJ_6vXyhnWdrCUWEJ0gxIA4v0ewHA7kFUn6qprDDLctVfObdj30XyIf3ZUUf91anOhJ9inQy2wlK91tNQ5wwU8N9np2a9EPKy7Cs9ewEliKDKGPgrtBXqCeTxbwEqtiVk0MwNUHGMaCvVzC-JVQzMWdj6FYQ44f9aCzraYK94my2qlTxt68q0QQzlIUTLPyAvtbAmFVaicj2kLq7IAIIuw2sgp4Nk2vKMfULPHiz9aYhwzUBbGk9mgW3_-bWUMd0k-hR_mFPV8PqZwC51EleycK4Xi-417087FIhlS77u3cFsSySN_BZksh5Cs-GKb3LvGsRy_04BuzhoR5nXuNXlAnz3CrGPAINLT3weDAFDuZTKdG9h8B-ByxWX8CYPMiecv2WkMJMLzfqjW3gnHYri07sbkt8qXMoHhcEzGGzM5FiUIuH_B_g8IOU_8q13K1vqS3zohV_Rfq4_LKBJhA6Lu-zLNJWUUtltGF39FMBVhwf-ZhUgHzNkpYvwXGUAEizFcSg12149Ms1q4VZRXgud82KJvwVXh9Gg4B8UYp0UpW0loUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل چند ماه قبل پویا پورعلی به پرسپولیس با پیراهن گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135960" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135959">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664e6b20c6.mp4?token=DgKtUBf2ZI-35r_sqrSHis6wG9shKgYbxdkzXs8vA9uk9EWmiotC9KUTY4L4aAsjxE6rbJ_w1T2JY7c0KPSxTg3J0zPNYgeB-1t6qr1ZzcYpZcDZ5aKyhwKi44bxBk1boR0pw8DVGX6OfrRL9ny1JcQEduJPOV2ZUjDfwfZuTBli-a2BRauXYMCm1t9bxFiUuKod8xFlpnzmW6fsSjOE7M-ikvyTvh23bHmZWhaSEREl8gOov0YZQAkOFEXzIPIArC8VkgqYQSTcZsn6mQZ2nGKZd7Fp0Idi2oBTBosV-DKpSwy-dupjIIhgujW-r5yYeiNAYJjT6xz9Cz5IYIsmtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664e6b20c6.mp4?token=DgKtUBf2ZI-35r_sqrSHis6wG9shKgYbxdkzXs8vA9uk9EWmiotC9KUTY4L4aAsjxE6rbJ_w1T2JY7c0KPSxTg3J0zPNYgeB-1t6qr1ZzcYpZcDZ5aKyhwKi44bxBk1boR0pw8DVGX6OfrRL9ny1JcQEduJPOV2ZUjDfwfZuTBli-a2BRauXYMCm1t9bxFiUuKod8xFlpnzmW6fsSjOE7M-ikvyTvh23bHmZWhaSEREl8gOov0YZQAkOFEXzIPIArC8VkgqYQSTcZsn6mQZ2nGKZd7Fp0Idi2oBTBosV-DKpSwy-dupjIIhgujW-r5yYeiNAYJjT6xz9Cz5IYIsmtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب علیرضا، پسر نابینای ایرانی اينجوری با گل آرژانتین ذوق کرد
❤️
🔴
گزارشگر اختصاصی هم داره که پدرشه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135959" target="_blank">📅 19:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135958">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135958" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135957">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
اردوی خارجی پرسپولیس در آستانه لغو
❗️
❗️
در حالی که تیم فوتبال پرسپولیس قصد دارد روز جمعه تهران را به مقصد ارزروم ترک کند تا یک اردوی دو هفته‌ای را در مسیر آماده‌سازی خود داشته باشد، هنوز شورای برونمرزی وزارت ورزش مجوزهای لازم برای برگزاری این اردو را صادر…</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135957" target="_blank">📅 18:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135956">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
ورزش سه: تارتار به وحید امیری پیشنهاد داده به عنوان دستیار و مربی به کادرفنی پرسپولیس اضافه بشه؛ اما امیری فعلا دلش میخواد بازی کنه و دیروزم داخل ترکیب پرسپولیس قرار گرفت تا خودشو به تارتار ثابت کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135956" target="_blank">📅 18:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135955">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eda321934.mp4?token=cOe-T3Lz9uiJmSc3xmULD_RmF7ewmytgKirOzpCrYPbdq1mH4rd9saDLlN0yGQo-Ty4zulFeUeJ77EPXlIAL03LlZpitXz-xNfld1y_Z87EjOKegIZxeGTu96YJ9LYf4NeueDuKUWXTx9jEhpwexEtCQnEGicTJ5uHYlXTs-fHMg4FpSzP1J0WzTe0EQnqOLgLz4jlA9n7RqF2FXoznleyUyBe9qZETr4fRr-tDlnyZ76kxZXczXDmTLiiN7Z0uhepMD2k0Tjt_WhRIfFf7v3D6o80gQLfAYSKKuMg7nvi_dwKqeUbUZiF7K2SAs5mOPpNlVA4Mn3bLsP6AtnNNd0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eda321934.mp4?token=cOe-T3Lz9uiJmSc3xmULD_RmF7ewmytgKirOzpCrYPbdq1mH4rd9saDLlN0yGQo-Ty4zulFeUeJ77EPXlIAL03LlZpitXz-xNfld1y_Z87EjOKegIZxeGTu96YJ9LYf4NeueDuKUWXTx9jEhpwexEtCQnEGicTJ5uHYlXTs-fHMg4FpSzP1J0WzTe0EQnqOLgLz4jlA9n7RqF2FXoznleyUyBe9qZETr4fRr-tDlnyZ76kxZXczXDmTLiiN7Z0uhepMD2k0Tjt_WhRIfFf7v3D6o80gQLfAYSKKuMg7nvi_dwKqeUbUZiF7K2SAs5mOPpNlVA4Mn3bLsP6AtnNNd0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فوووووووری
:
🔴
ماشاریپوف و نازون از استقلال جدا شدن :)
🔴
پ.ن فقط از استقلال ی سهراب مونده همه رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/135955" target="_blank">📅 18:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135954">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
اورونوف چهارشنبه‌ وارد ایران خواهد شد.
🔴
پیشنهاد ۳/۵میلیون یورویی الشمال قطر صحت ندارد.پیشنهادی باشد هم با میلغ بسیار کمتری است و از قرارداد مالی او یک میلیون و ۴۰۰ هزار دلاری با پرسپولیس بیشتر نیست/قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/135954" target="_blank">📅 17:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135953">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
قدوسی در خبری فوری
❌
احمد نور میخواد برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135953" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135952">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnOGT3IDmsz4NmVpk95XW9sFt-6JSSSUUkrADI-6JiX4ePp3cHduDbF6TxUnmyTaQSkw8bgSdrRhqiM3_mrjfgZistOrB5VPXRRstGcoYM08NNbw8G6X-Tdz3kCmdW-LqQJMbFXifDF1PLvUY44WpDvmIPmf1mcPLq_NTxai_Foy3Vajknk9ogVr8aL_9KkqszAQv88HPY4DJ2pqyyf4stJeodckdw0xEp-liDn38bNiEbKdWN9w7SpK-ozfGCAjEyZSL_b3MiT7vd6gm3j-I_QrgjwNDJGcU4LnXk_T__CJAJ4q6WY5seoOViROhW4IwlGP-Im6k6XUOrfO8AsGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ابوالفضل جلالی بعد از پیوستن به پرسپولیس یه میلیونی شد
🎉
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/135952" target="_blank">📅 17:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135951">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
✅
سامان قدوس در فهرست نقل‌وانتقالات باشگاه پرسپولیس قرار دارد و سرخپوشان به دنبال جذب او برای پست شماره ۱۰ و جایگزینی با رضا شکاری
هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135951" target="_blank">📅 17:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135950">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
شایعات؛ محمدحسین اسلامی در حال مذاکره با پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/135950" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135949">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/135949" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135948">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/135948" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135947">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135947" target="_blank">📅 16:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135946">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJqcwoyFeMRunhKIsPZepUZrH99b6B9pQKLZTR5f9V6M90BXX-Cyi2rj6avqEbkiMVsHvhF-F5OTciHLWBsioerxPP9Q01j6ud-a8hAbmU4VPAUYm-Jm_yLPW-VdoAFwxHd7q-S2wUlgmqMIrEwptpJCkdRrhoD_-r-bkGex1B0s8VtPrTbb5e8IIrDQpCNFYXwq_rUGS_rF5z5JdLDQDbBzshPmspxU4KqclnrzDnZ3Le_W6ouwFBiNBR-XxwXzaWhTFA2HIQv3QZNMynubYUTlWxk3ITdxhfhEmTd_YUCZi7u7O4hfNil2Ofm89cVGwfr6tA-2x6JrQyvK5YqRgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ایجنت مرتضی اومده مرتضی رو دوباره به لیست پرسپولیس اضافه کرده ؛ باشگاهم هنوز برای مرتضی پوستر خداحافظی نزده
😑
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/135946" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlDL5gfIaEguhO0dF3zGs9S8ednf0cxQt1fSY8YPlxONcscu-OkgBbF-RiS6QxbL58Vv-mb-93jD3t-yBgksRKd9XRFA8Dx4eatxYlRL2pyjuFxT71Ni5oJZHhe8RZPpfcRjnywgGUawERQuRTBT--pOzJKgZLKRlLxoW37jfXUTmwpBx7ywwbGRNE_qYaX-Y4m9F9PDJKLXQuTJ_AUOwIgU14cRlSYgDoyn_WGBYPGNei4MZGM-_ot8Xw8fX86kSl6zMja6xZ8sX2tWWIeijyqnu0em1wsxnHMSZFBhDtW-INfoHkQ-_Cf5p1T0xmVYTe-kB2_l2ay_vi1nFESGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سامان قدوس؛ بمب بعدی پرسپولیس؟
🔴
🔴
ورزش سه: پرسپولیس برای جذب سامان قدوس هافبک ایرانی اتحاد کلباء امارات درخواست داده و این بازیکن در لیست خرید سرخپوشان قرار گرفته است.
🔴
🔴
قدوس که سابقه بازی در لیگ برتر انگلیس با برنتفورد و تیم ملی ایران را دارد، یکی از گزینه‌های جذاب پرسپولیس برای تقویت خط میانی محسوب می‌شود.
🔴
❌
باید دید مذاکرات پرسپولیس با ستاره کلباء به کجا می‌رسد و آیا شاهد یک انتقال بزرگ دیگر به جمع سرخ‌ها خواهیم بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/135944" target="_blank">📅 15:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
عملکرد پویا پورعلی هافبک دفاعی جدید 30 ساله پرسپولیس در فصل گذشته لیگ برتر :
🔆
21 بازی ، 1 گل / نمره متریکا : 7/03
🔴
سابقه حضور در گل گهر، تراکتور، ملوان، ذوب آهن، فجر سپاسی، خونه به خونه، بادران، شهرداری جویبار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135943" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135941">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFCsjWha5Eo8MflK8jzNDMLo1zdRibux_Cg6_YUqtbwRNG2Lh-LZHwb-5LpzzeovKM3_iiBig9qOl4ko3_d1urR1e3TC3VtoogymqMllGhnL4L0uowcKMzvp1umbcSWi8l3JMeAZQAae10VaO-4k-ai1aXvW2n-CvOOVdU4_ezrVy247hURDk6FM5GgT1VNXPF2WI2fIRUEsScIGs16rLwxU69Kv4qlptVUfVPhZHjwqKU2-6OJYNSi6nEbRfpPSuo593o14in0DlMHJ2VuscT3VhjV2UYTabDp7dkqqECxYeEqHEm1w9K9L_i1puvTK3lmUATYtBU-rnr_h3fHmkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
فیفا قضاوت دیدار فینال جام جهانی ۲۰۲۶ میان تیم‌های ملی اسپانیا و آرژانتین را به علیرضا فغانی سپرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/135941" target="_blank">📅 15:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD6Lw99u5YPwE9Aue6Q40FLy6zvsmbHhiLd9wBONt3pZd1sZXGTf9wxGqQDmwlha2NQ7Y6I37vjcMwGwEiwIYo-1EdhLX4nDKL0LTgYc-wK1_StqZcXt1ykVeaaiQr8mB5XCFvfhEL1uHw8CcybVgHAG9oQxoxnO6ozF4YglZQPWNuror7EEIsBz2AT20cc4ESVNhPYSVt6L7akw5tajqLkPDptY20Nm0NYFeEiAiQDMoZsxi7iyYhhmmTOkByyHfyZUCTd4P35PZ1iHYK1a6o5H5E3Q38OMPWYZwy6wiwLRKs46D_5-X2s8Q1HtkYnlXejau9VzVDW-88pbf__xSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز:
مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135940" target="_blank">📅 15:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙷𝚊𝚓𝙼𝙰𝚑𝚍𝚒</strong></div>
<div class="tg-text">تو دور زمونه ای که فساد حرف اولو میزنه کسی که وظیفشو انجام میده باید قدردان خودشو پدر و مادرش بود...</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135939" target="_blank">📅 15:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135938">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompourya</strong></div>
<div class="tg-text">دیگه نمیتونی زحمات یکی رو بگا بدی خیلیا به وضیفشون عمل نمیکنن</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135938" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وظیفه اشه  دیگه دمت گرم نداره  مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135937" target="_blank">📅 14:55 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
