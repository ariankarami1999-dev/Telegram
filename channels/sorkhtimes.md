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
<img src="https://cdn4.telesco.pe/file/rkdFbq4FaUT-jWbuyhy3PgoAF91wCKLGCzd2_E1MQkPK6EpP5vpqiGAtEnUiq5IRo3eDEjiC_z-jshNY8jh8cVpwBVFXJVFchR9TAhPYgTgGF0t4o4wvVVoLEiUr7hjqHQgSh-dRzj81aCvSJwcJra-dI38CdWxBXWTniS7HdQyV-iFjIfYjORL2C3QqzFrVISmtIat2GAsAF4C9NBx4nEoh19hhuAFRKsxVTSK4-XJlf_RulHDzlyh2GS2SwX3e_b2-RKYFNhAyVw5Btc01vkEH0GRAo8vSpPGyPOLjCTiUTm9Nozds8hvkrqpnhQp7Cyg-pAPgOGdylbsmjQekRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 18:02:50</div>
<hr>

<div class="tg-post" id="msg-140193">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 723 · <a href="https://t.me/SorkhTimes/140193" target="_blank">📅 17:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140192">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 760 · <a href="https://t.me/SorkhTimes/140192" target="_blank">📅 17:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140191">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
❌
مراقبت از پوریا شهرآبادی از دست ایجنت‌ها جزو اولویت‌های اصلی باشگاه در ادامه فصل باید باشه. پس از درخشش این بازیکن در بازی امروز و احتمالا ادامه تورنمنت آسیایی، اسم پوریا بیشتر سر زبون‌ها میفته و مدیریت رفتار و دقایق بازی کردن این ستاره جوان، جزو مهمترین…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SorkhTimes/140191" target="_blank">📅 16:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140190">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
افشاگری عادل فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SorkhTimes/140190" target="_blank">📅 16:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140189">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حدادی اعلام کرد شکایت را به دادگاه بین‌المللی CAS می‌برد و ولکن ماجرا نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SorkhTimes/140189" target="_blank">📅 16:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140188">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
شکایت پرسپولیس از آسانی رد شد
✅
با اعلام کمیته انضباطی، شکایت پرسپولیس از استقلال بابت حضور یاسر آسانی در داربی رد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/140188" target="_blank">📅 14:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140187">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/140187" target="_blank">📅 14:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140186">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
دعوت نشدن علیپور و کنعانی زادگان واقعا عجیب بنظر میرسه.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/140186" target="_blank">📅 14:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140185">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/140185" target="_blank">📅 14:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140184">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/140184" target="_blank">📅 14:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140183">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
اورونوف به همراه برادرش که چند روزی کنارش بود، دیروز ایران رو ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/140183" target="_blank">📅 14:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140182">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
دعوت نشدن علیپور و کنعانی زادگان واقعا عجیب بنظر میرسه.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/140182" target="_blank">📅 11:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140181">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
✅
✅
علی قلی زاده: من از ته قلبم پرسپولیسی هستم و دوست دارم برای این تیم بازی کنم
❌
❌
اینکه به جام ملت‌های آسیا برسم یا نه بستگی به شرایط ریکاوری زانو دارد/ حضور من در جام ملت‌های آسیا نشدنی نیست و باید منتظر باشم
❌
❌
فعلا فقط دو ماه از مصدومیتم گذشته.خدا را…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/140181" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140180">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/140180" target="_blank">📅 11:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140179">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/140179" target="_blank">📅 11:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140178">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/140178" target="_blank">📅 11:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140177">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ9utubfO9Vbw4PTk_iFLja-jVRWnqQtx1B2XS8axVKYSGBoCxrGy02toJ1e_p0LFXjeKQbeOTy1NsDM4h496VJVZQy8Ajcw_hrKUY_8bmuihTtLUDmMg3n4_K3eMI49Bx56TVXwMWe8UHgmWk806O7EAn3cwexbo9S2WCicM9oWi1pf_vwDBQ0hg74iub77Re1_cjAaS4BIcsZA9YmSTcxkDv3TVSYQ3RGCq_mrPxWKWf1aM_KeWabR44XpMwnCPfFSqZo214a1tlJklXV3Oad3LN873wruksmeYNonI18R_PKvBDP0e-OAYXeX3JW0RaCNpzgR4eJoFhwHKP_KPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Juventus -
⚫️
Nijmegen
⏰
Tonight 22:30
🏟
Allianz Stadium
🟠
یوونتوس بعد از شکست پرگل مقابل ساسولو، در شروع اروپایی به دنبال بازگشت به مسیر برد است و فشار بیشتری روی خط حمله خواهد داشت. نایمخن با فوتبال تهاجمی و پرس مداوم وارد بازی می‌شود؛ بنابراین یووه در کنار مالکیت، باید مراقب فضاهای پشت خط میانی باشد. با توجه به شرایط دو تیم، انتظار می‌رود یوونتوس بازی را کنترل کند اما نایمخن می‌تواند در انتقال‌ها دردسرساز شود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/140177" target="_blank">📅 11:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140176">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/140176" target="_blank">📅 09:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140175">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
رسانه هفت ورزشی:
✔️
پیشنهاد نخست لوسیل قطر که خوب هم بوده به محمد عمری ارائه شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140175" target="_blank">📅 09:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140174">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
حدودا ۳ هفته دیگه تا دیدن دوباره بازیهای پرسپولیس مونده و عجیب چشم انتظار دیدن دوباره عشقیم..‌.
❤️‍🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140174" target="_blank">📅 09:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140173">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxvFZUFjy-dErWH1x1GzCApFHVlQUV1H4WHEfqSMm8S_brnKkI2vJReo0AoRKKLj_nHcUB5_U-naSnHV_LE8QLxxML3F9Q51QEQebsjkfInOdX4NrA77Zs_JIv4YuYc9hgKrzwHw8uugfolOwj2PqZOGwVi62T5K83nuPOTA6ZzBuFKM5-Xx5bmVnwmY3UbYhYQqo6n8AUBv6kqk_SE7OxCZV9JmAX3HPqdZ0gaV0P-IcT74iRVwArdMAyb3lmpEZYBXaTdHPuNDVxdlDVw9LgsWbJMALZGt-CbBxBWGX1O2hSMx6ehEtRBwQD2LTFxYDLFb7ZXSjY4M6AvwQiVMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حدودا ۳ هفته دیگه تا دیدن دوباره بازیهای پرسپولیس مونده و عجیب چشم انتظار دیدن دوباره عشقیم..‌.
❤️‍🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/140173" target="_blank">📅 08:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140172">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8euJ_xJrwbFORDE2t7yDk1xYbq2tE0LraDH96ObpdKgOGdhdOLWvLk3Akaw5xfMr4lkcTVOEWaofF_ypq3ApFMPjyX4M9j_lw4YQhmXno5rwK5J4ixkid24fSz_vF7zc13RPNDV2xufesytxSXio9i5xbhlaNOk8S1eJqhXb-16VCnZOxzkqg0i6SqTZOMf7dGe_hb7VT_lIZQp3GV0x-WSRob6LoCblJAyVPrV-p-0Mbn4aBU6yuJeJHXu09ZZ5GwasHb9OwUdZ3MvxdMocZZZm4gr97aV4ZZuSzKQEPPIq3LAhd35puq_m397XDoTdxhDtUhbu3Zza7sjvAa2CA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/140172" target="_blank">📅 08:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140171">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=WGNSn7eTs60wPAqvs8Xn6FHRvp4B0rBUOjgyIj3bhRDL1YU4tm86BSe_DinEKY8tCLT0brZ6aM-WAmjEGt_cj5EOFf2JSNhsD-dVPFoDxiHmBbJUgycybrNr0rDaBoEI23Qh4eqGkbgVMnitY5tueN3nMLNtfLDAKHnol246z9Oke9Ko4m7Qm2gS1HasF4T-o6H5k55m-EAStvBaHy4JTA6iDyZ1z-0TKrEfK1gKxVWAnH2-x5FS81tF64tr8_Bou1EOADSwxEPSl2WQsQaUEAXSuo7zjfz-AKIvwIaWvy93_JKUn_5W4gjcmV3cjVfXhubTUQZwwnggBWLaHuzY9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=WGNSn7eTs60wPAqvs8Xn6FHRvp4B0rBUOjgyIj3bhRDL1YU4tm86BSe_DinEKY8tCLT0brZ6aM-WAmjEGt_cj5EOFf2JSNhsD-dVPFoDxiHmBbJUgycybrNr0rDaBoEI23Qh4eqGkbgVMnitY5tueN3nMLNtfLDAKHnol246z9Oke9Ko4m7Qm2gS1HasF4T-o6H5k55m-EAStvBaHy4JTA6iDyZ1z-0TKrEfK1gKxVWAnH2-x5FS81tF64tr8_Bou1EOADSwxEPSl2WQsQaUEAXSuo7zjfz-AKIvwIaWvy93_JKUn_5W4gjcmV3cjVfXhubTUQZwwnggBWLaHuzY9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
آموزش ثبت‌نام و ورود به سایت وینکوبت از طریق ربات تلگرام
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140171" target="_blank">📅 01:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140170">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
❌
❌
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140170" target="_blank">📅 22:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140169">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
❌
#فرهیختگان؛ مذاکرات با ۵ بازیکن برای تمدید قرارداد آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140169" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140168">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
❌
مدیریت پرسپولیس در حال انجام کارهای تمدید قرارداد ۲ساله سید پیام نیازمند، است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140168" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140167">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
❌
❌
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140167" target="_blank">📅 22:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140166">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
👤
مدیرعامل فجر:
📍
انتقال علی بیرو به تیم ما قطعی شد
❌
چون پنجره نقل و انتقالاتی بستس تا نیم فصل باید بشینه سکو
😃
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140166" target="_blank">📅 22:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140165">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkUDqtg0HhljxEX0HaIXAUax2paV3C1nSVw8OpGDV4MqC8K-Th-AgDMyp3r6Yb_bqijMitSoiHexwdIITXXfgxg1kKHkiYiME3_AaRRQYII1KETtvJntYoPJ3ias1R17wCn0aXm5o65vLPF9hiBV1k-yXdJISS0vzeqrus5g_TgKGpRwnrbCapgqZ0NxDAfHrmAD4PG2nGkslmR45i2gOuV9zrtE9-eTu7mj_T8FRTev6O2w4n0TEEXVHUF_PcNCmxcI88xK6RyaFhDz2TZFrlLNf6jjfon1lu2pI6tI9XVU6FGHwAzsgC-IXZvQm0dCiowIjU2PfcUnmH_1GSDy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140165" target="_blank">📅 21:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140164">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
❌
❌
باشگاه پرسپولیس کارهای تمدید قرارداد ستارگان خود را آغاز کرده و امیدوار است بتواند آنها را حفظ کند/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140164" target="_blank">📅 20:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140163">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
❌
مدیرعامل باشگاه فجر سپاسی؛ انتقال علیرضا بیرانوند دروازه‌بان تیم تراکتور به فجر سپاسی قطعی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140163" target="_blank">📅 20:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140162">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M50tCTszq8PyPFuV9URXjkqkbTCAOu5DpBd1AogiCyfQdMrHkzpjRSSLIY_NTSN9RZtyJfBz-a0kmCFb0AAuH0kVw_2qXBHs-PyypmXJE9m1MY9T1sL8pBnIET_fV2YY52fM3P8yBcuUDWgLPnDZTcZv8PtKahp-BhGIcaMwD-V6t1E51LBFLjbdFFPI7plEjEw-DFpGJjtrxdN9V_tHUV1F9UbS2uieebc4oMarE8XWbbDt_QuFnEpIsuuxoaMlmtl8ZHrDCVDswGUEwWCdNqmBfyPLT2IS4ykA7k8ZPU7ciQH8i6cxCkGuuVoy6aK6Ussa8Mnt9ytBw47Yf29lKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سن‌سیرو امشب شاهد تقابل دو تیم بزرگ اروپایی است؛ میلان و بنفیکا در دیداری که می‌تواند از همان دقایق اول با فشار و درگیری زیادی دنبال شود.
[
🔴
AC Milan
Vs
🔴
Benfica
]
⚽️
میلان روی بازی در عرض و نفوذ از کناره‌ها حساب می‌کند و بنفیکا هم با جابه‌جایی سریع بازیکنانش می‌تواند فضاهایی میان خطوط پیدا کند. اگر پرتغالی‌ها بتوانند از پرس میلان عبور کنند، ضدحملاتشان می‌تواند جدی باشد؛ در طرف مقابل، حفظ توپ و صبر در ساخت حمله برای روسونری اهمیت زیادی خواهد داشت.
🟢
امشب چه کسی برنده این نبرد اروپایی خواهد بود؟
📌
میلان و بنفیکا را با وینکوبت دنبال کنید؛ همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140162" target="_blank">📅 20:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140161">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140161" target="_blank">📅 20:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140160">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
❌
النصر هم به طور عجیبی سه گل خورده از العین ..خدا به داد کیسه برسه با این العین   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140160" target="_blank">📅 20:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140159">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">💢
عابدینی مدیرعامل سابق باشگاه پرسپولیس: ‌چوب لای چرخ مدیران پرسپولیس نکنید، برخی بیرون از باشگاه پرسپولیس چوب لای چرخ مدیران این باشگاه می‌گذارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140159" target="_blank">📅 18:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140158">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140158" target="_blank">📅 18:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140156">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
رسانه های عراقی: بشار رسن دنبال اینه برگرده به پرسپولیس
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140156" target="_blank">📅 18:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140155">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">💢
عابدینی مدیرعامل سابق باشگاه پرسپولیس: ‌چوب لای چرخ مدیران پرسپولیس نکنید، برخی بیرون از باشگاه پرسپولیس چوب لای چرخ مدیران این باشگاه می‌گذارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140155" target="_blank">📅 18:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140154">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140154" target="_blank">📅 18:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140153">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140153" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140152">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
❌
شنیده ها: تراکتور نیم‌ فصل برای جذب حسین ابرقویی وارد میشه!
✔️
✔️
گفته میشه تراکتوری‌ها ابرقویی رو زیر نظر دارن و احتمال اقدام برای جذبش در نیم‌فصل وجود داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140152" target="_blank">📅 15:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140151">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
❌
حسین ابرقویی مدافع میانی29ساله پرسپولیس چند پیشنهاد لیگ برتری دریافت کرده و قصد داره توافقی از جمع شاگردان مهدی تارتار جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140151" target="_blank">📅 15:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140150">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgZqg0zQPk3XsMnBOwjif-r5fD1JM8xEvbHD0RB1SGZoviNH6WNP1yJhTs7PJbLS5b4E6A5APjxJrghr-kCdhR3pKZmMpuww-qCiYB7ctEPYRufY3OHTwaGaVm5my62QBFyCsKSP-kamZCnP3QJuCW6C33P6knuVEtCfUcFBlJ5Tvqk-KwY4c7p2f05Ae8AUgPIAy6DxBU6-mFBi1ifmzMbSNUw954jhrLpN8QNzRclmjSFF_zUWWW51J-CzVmb6m99MKazNmQe47zpoDDhweJiY-n2pAOEB6L9NC3qzZutLcPhSOcOdeE7RGF2fOu3zx0ghZ27uPsLA2CmDveD5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❤️
ایشون بعد از اردو ترکیه که مصدوم شد حتی تو یک تمرین تیم شرکت نکرده و حتی نمیدونیم مصدومیت‌ش دقیقا چی هست و داره چی کار می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140150" target="_blank">📅 14:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140149">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i85X0wd8vB02tJDJlUecFuLbaNqZTjcBColMJ1x4xgnVrRgMtWTaP1y4fqJQVGVcV4-dRUk5psBjbFlp6byTgMOSAOqA-NJ8Gg2OWzTWMwEVGmr2FVEd3pvEGNF17IkBfni9GNN76OiymBoNWXPVxGixvz3Ld5BDTyjNajBly9poPUJoo_WnSHgW1H_ZPfznHgQodHWtcomwBGdtKHrK0VpgAeldSEscPnV6Dl7mxMUu47WOqLwD8iMp7MkERmhsN22E037KLSd2TD6HlhajEVstPBKVrJ7TFp_3QlSh7EbqX-BLq43dYyjAUKLccndPCIuvwliSh6Vw4Shg7_8rVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گفته میشود باشگاه پرسپولیس دیگر برنامه‌ای برای خرید امتیاز تیم لیگ یکی ندارد و به دنبال خرید تیم لیگ دویی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140149" target="_blank">📅 14:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140148">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">💬
محمدمهدی محبی: خوشحالم که در پرسپولیسم، همه خانواده‌ام هم قرمزند!/ سیر فوتبالی محمدمهدی محبی، که پای او را به تیم نونهالان استقلال هم باز کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140148" target="_blank">📅 14:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140147">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqwbuVLbrTblKw4zY7Tir3yfD70KfxvKZDts5NJcqkDDytK5uJHoYOh3l4m8_y0fQ2oGe4Lnrrz1_dZM_Lt2Y2L-agSWLmUjR7HKN1qCaxdfbGvYAxJ7lPklBeXO2viuaEhzEmfozv-NKcLT698ffxL5Lj7W05T-WMhzbxtqkZclHTyH0gwyQHdTXXSEIrJ6FJL_IDqJRpcEKlw_M2CF1OpcJwfUevYU-VHs9gMa8AXnXbV9vaL0t03e2FFgSV1llSvOuvBQFUIscQGOgGhY9mUrN1ejUnHVPTERQPdT1pW-L1qHQKuG1cJEIODudEaJETRavMkstCYRXtn0ZzuBWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب؛ چندین بازی با چند مسیر متفاوت برای پیش‌بینی
🔥
⚽️
امشب کنداکتور با چند تقابل جذاب از لالیگا، لیگ برتر و اروپا سنگین شده؛ از جدال اتلتیکو با اوساسونا تا میلان مقابل بنفیكا و منچستریونایتد با برایتون.
بارسلونا و لورکوزن روی کاغذ شرایط متفاوتی دارند، اما بازی‌هایی مثل میلان و بنفیكا و همچنین اندرلخت با لیون می‌توانند معادلات متفاوتی بسازند.
شبی پر از بازی‌های قابل بررسی؛ جایی که انتخاب درست، بیشتر از اسم تیم‌ها به جزئیات مسابقه بستگی دارد.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140147" target="_blank">📅 13:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140146">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TimrK9U0LWXWYC0LGOPvw-LqkyPvWtXvOnfAMHfypAKhtcgqUnl_y5NI-jMBlOcVOZDgRtvWcLrUf3oz6J_3mOiYh7SuEKOZwBbPO4vOrw_TgJSaqcQ47IMk_h8SyepP9BvnfNsFDNDOxqXulYIrJHfsU-iL31g3bof_aI-H9TbFV5fzI9RC4X_fRjJlIARh0DoFOsTRyP26X7PrRQWg2lGXd7ChVIVCOe8g9UoJSkanUQl1Mu8q5RIavT3GCCBcBp1DhdUi59_zimNLrxpujq3HGFXWuW0bZ1v7b1o1LjEZEPqVdOwAxMYc65hGcZQ_zScgO8qlTASIzLJQsSd09w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔹
ماریو توکیچ دستیار سابق برانکو به پرسپولیس پیشنهاد شده و درصورت تأیید تارتار به کادرفنی تیم اضافه میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140146" target="_blank">📅 12:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140145">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cup3gktl19UmEjZJknbc_JUmOKWqGrOY8sB9L7wUlhmWxw2IVZVBPPTDe4X_ueyMeQsrxknLXF9iyws9Bw3WqltOS7EzDiZCWpO1jn2Sat8_WahpHOs71vdZ055bhmMdb3NZ3ikxFupKNvIWsiMeh1AN626usHofcoK5BggwGylgxWYEosObSXJpr0ghElzuqSfAz9BceQfzByGB7CoSlyBlNtVDvvwLGXAXJyvVtowaz9wyRiTzSWUIpjZehHm7nXaVup_txzWr0jTaZq-LuBFjnbMSWIO_RsIbl-ZeF6lrvxPDfIJ6WiHvjYQl8hwa008txAFQBFRCWjemyAfIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با پنجره ی بسته و کلی مصدوم و محروم و فقط با ۱۲/۱۳ بازیکن با علوان زاده ای که الان خدا میدونه کجاست و ادام همتی که بنگاهی شده رفتیم فینال آسیا.
✔️
✔️
با برد جلوی السد برای کی کری میخونید بدبختا؟ اخرین افتخارتون تو اسیا کوپا امجدیه بوده که چند تا تیم محلی رو بردید سماور گرفتید . حد و ظرفیت شما همینه پنجرتون بسته ست ولی بازم تیمتون پر ستارست با برد السد میخواید برید پای سهراب بختیاری زاده رو ببوسید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140145" target="_blank">📅 12:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140144">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140144" target="_blank">📅 11:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140143">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=mg4voLWa7G2V7U_bbubBsWulbqjv5cmz7k1NjD7cg54jfEN4W9uBq2pd_Peu1faN-ElO31F5lxzsKprFL3VXDsikSWqc22w5Sr5_mJ5mrsqTippYqeujfCgdJ4BKeM2gWp5rD8CorDKjtWuW_jtE0oNPNnq3sEOZCkoSMEBMxVaXCsf21W7GHpIBo-2xQb9A7TXgPtCqe9qTXe7Cb5nzya56nseq7qVufXF-aUryurGLuT3mmc3gz8RWTSi2Wi6DI-tTGgIpQnHdZIom3LQBteyMGXP9KZpuxRcfis8ITEaMB1ME2rAxM_-A0PN8wKHWf51dMelo25lMm3QiKK40lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=mg4voLWa7G2V7U_bbubBsWulbqjv5cmz7k1NjD7cg54jfEN4W9uBq2pd_Peu1faN-ElO31F5lxzsKprFL3VXDsikSWqc22w5Sr5_mJ5mrsqTippYqeujfCgdJ4BKeM2gWp5rD8CorDKjtWuW_jtE0oNPNnq3sEOZCkoSMEBMxVaXCsf21W7GHpIBo-2xQb9A7TXgPtCqe9qTXe7Cb5nzya56nseq7qVufXF-aUryurGLuT3mmc3gz8RWTSi2Wi6DI-tTGgIpQnHdZIom3LQBteyMGXP9KZpuxRcfis8ITEaMB1ME2rAxM_-A0PN8wKHWf51dMelo25lMm3QiKK40lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل سوم ایران به امارات توسط مزرعه(89)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140143" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140142">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=cGvuYPvt6xpnxNkhGc7X-adMbHn4bYdYEgyuLC8GAXzLMX3JPPAdq_Mik7Fc7NFKfF1rPHm9a2mqPXXp53PfzHWq4ccIgaaJXJjrgfIP7UNo7Rr4SUqlqJAhQ-4-Zt1GpjTsvooUev9ELWJhJtsrb3UzGJtJmbCgD4BTPzKoq8KT0vb6CJZQYg3ADnSJB7ShPO0eViofVPHf5Nus5_H4siYrpKu9MeFl9Pskw0KhNGzwEzm6CEJ4ajQeMXSZSU63TgSdILG5mAdIVrnL06mt_S6m0mJcebybnoDWCqtIaKmd2JBTzGDCPATXDF_1m6RGgF502RuRaTbm9NmPV0litg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=cGvuYPvt6xpnxNkhGc7X-adMbHn4bYdYEgyuLC8GAXzLMX3JPPAdq_Mik7Fc7NFKfF1rPHm9a2mqPXXp53PfzHWq4ccIgaaJXJjrgfIP7UNo7Rr4SUqlqJAhQ-4-Zt1GpjTsvooUev9ELWJhJtsrb3UzGJtJmbCgD4BTPzKoq8KT0vb6CJZQYg3ADnSJB7ShPO0eViofVPHf5Nus5_H4siYrpKu9MeFl9Pskw0KhNGzwEzm6CEJ4ajQeMXSZSU63TgSdILG5mAdIVrnL06mt_S6m0mJcebybnoDWCqtIaKmd2JBTzGDCPATXDF_1m6RGgF502RuRaTbm9NmPV0litg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل دوم ایران به امارات توسط پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140142" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140141">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=cZYxeQPCds39kDpsW0-zQwWNm6NSp_-6rqddyKVKN1qf7jeK5Mzi_uFoOVyA_M5WGQkzDR4J4riOkwR1JuxAnAGdGG-mU47wHzeRmkxzUICbNYHBDr5SyxWbX2DJIbDoOzTlhli-6u1K7L4-VDW-p0CT97DNju7Imso0jzQvxXiCdwD9UTXdlZs5zE_Dty2FCPx-6Bx8_DoBC4fDF0eH5_INjH-MgBdRFrtu2iwes3owNJAteiLdOJimL_mBcM6HEiKCNRcWJo4tg8P9SvoqwQvT1Ae1fjO5V61WEcQOwZEDOsiVNPUV9BwTFm5zs9I2Rf4BLdwF6T67s7Mt2poF5oQ7zj3c5HINMgDrzVG4Y3dYJjvvTirPY9tNeH04_6qx_mC8LcKF3YxSCOFFCOkUcSvJt95AI331TisaHCQGLjleJtnxAV2OUIkPKBdCqFI3GYRNbOi2f-R5IwYLJwMDwp7hQANvTB1FtZmV_7DflohKCH3c1p_gjrBZBLe10JfsJf5n1_QOMRbfrximFMIbGRsru9NFDgNtYEyKKtZTw2Uw9CGXlKwC_emjyo61jsvAgYyLaFM2AsjJfwxAjDvaAHZQ0RoW7vUKMZhX_wXDJNfqN0u0C7isOQ0XK-QQdYPixKzvCfYni0AFwZ5OsEDrllCnDgtd6IIz4mdE0tdl0FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=cZYxeQPCds39kDpsW0-zQwWNm6NSp_-6rqddyKVKN1qf7jeK5Mzi_uFoOVyA_M5WGQkzDR4J4riOkwR1JuxAnAGdGG-mU47wHzeRmkxzUICbNYHBDr5SyxWbX2DJIbDoOzTlhli-6u1K7L4-VDW-p0CT97DNju7Imso0jzQvxXiCdwD9UTXdlZs5zE_Dty2FCPx-6Bx8_DoBC4fDF0eH5_INjH-MgBdRFrtu2iwes3owNJAteiLdOJimL_mBcM6HEiKCNRcWJo4tg8P9SvoqwQvT1Ae1fjO5V61WEcQOwZEDOsiVNPUV9BwTFm5zs9I2Rf4BLdwF6T67s7Mt2poF5oQ7zj3c5HINMgDrzVG4Y3dYJjvvTirPY9tNeH04_6qx_mC8LcKF3YxSCOFFCOkUcSvJt95AI331TisaHCQGLjleJtnxAV2OUIkPKBdCqFI3GYRNbOi2f-R5IwYLJwMDwp7hQANvTB1FtZmV_7DflohKCH3c1p_gjrBZBLe10JfsJf5n1_QOMRbfrximFMIbGRsru9NFDgNtYEyKKtZTw2Uw9CGXlKwC_emjyo61jsvAgYyLaFM2AsjJfwxAjDvaAHZQ0RoW7vUKMZhX_wXDJNfqN0u0C7isOQ0XK-QQdYPixKzvCfYni0AFwZ5OsEDrllCnDgtd6IIz4mdE0tdl0FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول ایران به امارات توسط شهرآبادی(49)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140141" target="_blank">📅 10:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140140">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
🌏
بازی های آسیایی ناگویا | گام اول امیدها با برد مقابل امارات
🇮🇷
تیم امید ایران
3⃣
🆚
1⃣
تیم امید امارات
🇦🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140140" target="_blank">📅 10:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140139">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DifnCcDY9okv7ByEllQlajJ8Opc4o4o1UoGNRx4dQ7Uhg6rDP6NGY68mgH7uRNKn5HFKnv4LhqxIEBEesY-W37YNP26ETkPWzjFfN0WWuWEHF6XAnu-RKaa58ciMbXyZ96wtdSIJ63bOgaSgjCm3X9MWo3dLL8dXPcWCZHOKTkZ-5xA10FneTeNtxxClZlliCdIGwMmrxiQFz5rhN6vW2TrkwRidOUJ4jmSrTwyllDZ3--DDBdBNpj5dO53BPujV7lChtKL3vfHx8U3Dfz6Zrfkqt-F0Zl-Lwp79uPw-0Mw7dSLUbkBfIrZPRDOkByeonJiyfQTvrSkReIs8XlKV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🌏
بازی های آسیایی ناگویا | گام اول امیدها با برد مقابل امارات
🇮🇷
تیم امید ایران
3⃣
🆚
1⃣
تیم امید امارات
🇦🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140139" target="_blank">📅 10:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140138">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvLZwljtG14VHYIk5N17QjGJn6lGVtq-zVO18OB_6EJEFu55KwnbVjHcD0VBNgEM2yFhY9aVIkn6qr_G_L6lOBph7Zs16WhlpD_CLIOIB1StGicsC4jSwkDMmgYqArWt2XUz5JaSGjbwy3YqGfOrxFh9hfudvMU3c1gKkHs25EiRGwamfNAVuOLuoHdPBTcfxqEk-EEQax0NM3BdsFFOpFs0_0fAsi8-v1Si3PyvgdcMp1ab_Q1zj23YdTkQFlRL1GMLxEx3pvkik6Oog-XBlwBFnGj9g7wegiPZ-ERJRR-jVwLJ6bazPR0uZ42oMKe0HE3c5krUYsggLhJVzXa7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140138" target="_blank">📅 09:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140137">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JxRrv3sidPabs9tpVDWOFT50bzg1U2Fx1wignYq0IFapLEVEZbz6MzsB1X6AnP-G-G4QF6Bq37VsoDyWK5NeNm8au8R6N-bPOdvdWZQkWNCZWy2CL68c0c-uQDhNrXuiu1HRPWdHRtJpBa6i2UVp9Scy0cigeG4LR2tqSkwoupY8UCxrvAAmpOa0mUZPIIvSYqMyi7ZZmtlOmxdIQpS8ngkDvWtimkl2euAIlPdn3aGrPygN07C3CgCaksoQ5YXRPaHBHKA_mwHIsuaJFJPVts6D9m3hkshsfQ2Yyjocc3Nsenbwrsg-zhfanDfdDFGx-J3rGiKxEGEJYnHIHOUkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه اسپورت‌نود
🔵
با هر واریز بین ۵ تا ۱۰۰ میلیون تومان ۱۰٪ بونوس ورزشی تا سقف ۵ میلیون تومان دریافت کنید.
🔗
آزادسازی بونوس خیلی ساده‌ست؛ فقط کافیه یکی از این دو روش رو انجام بدی:
👇
📌
شرط تکی با ضریب حداقل ۱.۹
📌
شرط میکس با ضریب حداقل ۴
🟢
مدت استفاده از بونوس ۲ روز می‌باشد.
🔗
همین حالا واریز کن، بونوس بگیر و شانس بردتو بیشتر کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت‌نود:
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140137" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140136">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140136" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140135">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alL7Vy2woZ2_YIG-HF0UVakWTXDdD2lGPqHVFy8LLtqEzSAGchwQikqlagT_3Yg6C4Nr50wDE9T1cw6GoUOKO6oIOczi2kb3gKJbgd7dFG56lvMpy79udYoVSm9q845uWmR86P22mVoSJYqP7LpkXeyhCcGZClgI8jWFTsnVbZJZbKluG9HX1CI4K0r_TcW1TdIahXr3YTqF-lKVMb2RAkLa5GfReYj90TZzBm67EZThf7TRiOPHPQURMDA26j2VYZHkk-H5hpaFF_i0u8K4KzdGkkAOJrJz-ZOI3I0WWZ-E7rdAUbLalMHEdzGcFQzQsiEg4CePPm8EpF1rD21_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/140135" target="_blank">📅 00:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140134">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3657efb8.mp4?token=eK3SRZwU7RecQhO_6a_w3kMKPnJwaNcn1JMTozqlO6ZaAdV_btoxxOalJI8o9ZoKSIPxr01cRKyTdbvUV_gc3bdPXLLf3W_JI3UMSjPqVN0_KLVzI_z9bTSf2zTNHtxcXZkqi9l_YKhmvdAo8dXiwulqGAxq8YEu2432UPX6DGiRj6sagMLLT9B-3CXk65Xp6gK01Lp4QYDK-hCuONA7B3jYerKRuHfSXjR5hS2XOXQG6UPdNgoyS-sJBt6_xAJ1kZJjnWCsm2U7V0zgTAWuptapzShaIkkEEmt8tytGqmbo4zWXbWDz-fFUxJMRQWHc82XRr1XK2wpxOjissvu6KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3657efb8.mp4?token=eK3SRZwU7RecQhO_6a_w3kMKPnJwaNcn1JMTozqlO6ZaAdV_btoxxOalJI8o9ZoKSIPxr01cRKyTdbvUV_gc3bdPXLLf3W_JI3UMSjPqVN0_KLVzI_z9bTSf2zTNHtxcXZkqi9l_YKhmvdAo8dXiwulqGAxq8YEu2432UPX6DGiRj6sagMLLT9B-3CXk65Xp6gK01Lp4QYDK-hCuONA7B3jYerKRuHfSXjR5hS2XOXQG6UPdNgoyS-sJBt6_xAJ1kZJjnWCsm2U7V0zgTAWuptapzShaIkkEEmt8tytGqmbo4zWXbWDz-fFUxJMRQWHc82XRr1XK2wpxOjissvu6KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
پویا پورعلی، پسر خاله حسن یزدانی است
آیا می‌دانستید؟/ ورود همزمانشان به کشتی و راهی که در نهایت جدا شد؛ خانواده یزدانی و پورعلی همه پرسپولیسی، به جز پدر استقلالی پویا!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140134" target="_blank">📅 23:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140133">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=ZEeSl8FJYSRd-zaIHA-uwru0IwdrApP4et21RUu5hkM5RfJG_CW8LmV4b3wDWeMY8U4y9FpqeYiaHxKGETEATpD30MjFW0gI_mSq-IWuKtbI23vFKsDDjF1JyORRc3qnydgkknbC7CouH48jXOT4osg2vnxfrANzBsDlL_rUi8mdvn8TJ8TRXAEL_fGnUe9VuGO_qCdnCKJidEjjDDAF_fL8nHAGlFrjY6HnVCU3kVUcfj0dPRGV8rCHae5JUIr9eHo8aoQ2x-Lp_5ywtZeUGt5NjvpLuSzPE3p3ygiIoEzIlJykvNk6oG-1a3Il9EmzEY4YANHwd6KP2x49aNuUmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=ZEeSl8FJYSRd-zaIHA-uwru0IwdrApP4et21RUu5hkM5RfJG_CW8LmV4b3wDWeMY8U4y9FpqeYiaHxKGETEATpD30MjFW0gI_mSq-IWuKtbI23vFKsDDjF1JyORRc3qnydgkknbC7CouH48jXOT4osg2vnxfrANzBsDlL_rUi8mdvn8TJ8TRXAEL_fGnUe9VuGO_qCdnCKJidEjjDDAF_fL8nHAGlFrjY6HnVCU3kVUcfj0dPRGV8rCHae5JUIr9eHo8aoQ2x-Lp_5ywtZeUGt5NjvpLuSzPE3p3ygiIoEzIlJykvNk6oG-1a3Il9EmzEY4YANHwd6KP2x49aNuUmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
افشاگری عادل فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140133" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140132">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d778bc850.mp4?token=OVrP_NnyQ0cnn4sbzMkOP25mS1eJGUGNap5X_JuC9UwbNSoJHCVTWXzxMVEVxaRsowYPtIf9QyFRMa0RwB3ImP-42_r5c1nApUFfHwbAUGsi5DoeZS5bynES8-1cARjBVDXpdCNvvhVwH3JSoais6dFhjrD0mFRWKHHUYUl_eELihKGF0e54tgghJtmezfWhpQwI_Mp1s0LEkOM9caQvOIls7MFrKroOXEho3MSVDG_F0vyln3rjqQiG8fkEQRMz2MWudCV5t5wcWhUNV-cHbMsT78ulDsozlmE_Llebl9LIngPaYssa9slULQoACbjQgTrMXN5WYfD_wM8wX26zKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d778bc850.mp4?token=OVrP_NnyQ0cnn4sbzMkOP25mS1eJGUGNap5X_JuC9UwbNSoJHCVTWXzxMVEVxaRsowYPtIf9QyFRMa0RwB3ImP-42_r5c1nApUFfHwbAUGsi5DoeZS5bynES8-1cARjBVDXpdCNvvhVwH3JSoais6dFhjrD0mFRWKHHUYUl_eELihKGF0e54tgghJtmezfWhpQwI_Mp1s0LEkOM9caQvOIls7MFrKroOXEho3MSVDG_F0vyln3rjqQiG8fkEQRMz2MWudCV5t5wcWhUNV-cHbMsT78ulDsozlmE_Llebl9LIngPaYssa9slULQoACbjQgTrMXN5WYfD_wM8wX26zKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏅
💛
🎙
واکنش عادل فردوسی‌پور به اسم‌های روی پیراهن بعضی از بازیکنای استقلال در بازی با السد: مگه خونه خاله‌ست که هرکی هر اسمی خواست بزند؟ یکی نوشته گودی، یکی دیگه اسم پسرش رو زده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140132" target="_blank">📅 23:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140131">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9929527fe.mp4?token=j4LUg8Y0F6jRc70nJB7v5-OUq29pN2hw-tv6p9fXzYqySlfZk4xaux0iKmgONC-PZPpKYSJTHlLU58cDSNMoYq0IyUb_pwJ7IQckWX78IEWqX1HEfwM2NPIals72gJmtUIpEQvwpnPTY6B90It5jD_uag-xE48BqYtidLoTQNmngxPhxyYgUcwe7nZbioW7ZAvXnIH9uQSBxkDGpQ1T5j-Szp_394P3cIQUly0nlSP2nYLkqGjUxkj_OZ6uYKEQgwMMTVnd7blmB1fLTNfC9h96GKvVA26iTCOUFy-oIUb77K8qLXkD-t5ZVoyajipY69kaI8iPyhvebwZjgrSN0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9929527fe.mp4?token=j4LUg8Y0F6jRc70nJB7v5-OUq29pN2hw-tv6p9fXzYqySlfZk4xaux0iKmgONC-PZPpKYSJTHlLU58cDSNMoYq0IyUb_pwJ7IQckWX78IEWqX1HEfwM2NPIals72gJmtUIpEQvwpnPTY6B90It5jD_uag-xE48BqYtidLoTQNmngxPhxyYgUcwe7nZbioW7ZAvXnIH9uQSBxkDGpQ1T5j-Szp_394P3cIQUly0nlSP2nYLkqGjUxkj_OZ6uYKEQgwMMTVnd7blmB1fLTNfC9h96GKvVA26iTCOUFy-oIUb77K8qLXkD-t5ZVoyajipY69kaI8iPyhvebwZjgrSN0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محمدمهدی محبی : این همه هوادار داریم ولی چمن نداریم، شما کیفیت بازی اورونوف رو میخواین ببینین باید بازیش جلوی مصر رو نگاه کنین، بنده خدا تو این چمن نمیتونه دریبل کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140131" target="_blank">📅 23:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
پورعلی: الگوم آقا کریمه و هیچکس هیچوقت به سطح آقا کریم نمیرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140130" target="_blank">📅 23:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140129">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❤️
پورعلی : من به مهرداد میناوند قول دادم یک روزی شماره ۱۱ دایی کمال رو بپوشم و انشالله در آینده می‌پوشم ، می‌خوایم قهرمان بشیم و آخر فصل جام رو به روح آقا مهرداد تقدیم کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140129" target="_blank">📅 23:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140128">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3207916b83.mp4?token=iMwrPrVXNo_X4QSLjBEEFKy6CjkpOSwRbDmHVK_H_om8AFx9t2H0IXat8dA-pAFomjX8k5uNW7RlwiW9qqLPKc5WhKeS0nQvvb1jDWB548PLAC4CBC5hw1AlfQqTiM9zl1Ejnp7WXxbZ3LSpzTwwsS1ABSfOSQQuOzVWAID3FLFXtE0lddaiH5KJnAysb-17h6lKbAK7748fu7C_qiwvn1_Uadb-oLTTmPs-sSqt-vYc_zMdmD1dI8EU5kJIGddQwCwW0h4trlH8WSGzkIyJdl6qrKT69C7aOTZFfssn7d1F4kKP5szTrmR2UjPwKMETgo148WrQvYq3-YIUku1I07fz_mh_hqUT4wpANpFUwVhcKa-q5dmof-fW7cyA0rBBiNDOkA0Ejiy05feJZ4_hlXXY3S-_fY93opcgP6DqP8S3hTA7DO0hkrC218QOsO2R_Y0lL7XM9pQbkKHB_sZc22sKH45eQulqmkZLo4hz2e_2Wv5hiuOuiyPglEwEkmD6ltZY-6lQxynDfQn6ufmBaYNumXj5iSyoM8lkK-b8i41FQllFYj91hqKQNeet1kQtguCzC_C1Y1zi5wWlwxoD_kEQHyF_zrM8dbGd9uxXDmOjFIsiH4edZHQbpiV6DuDnbfX62efeWILdtjkxnYjguQrQNQfnvzoNLix7BO0K-ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3207916b83.mp4?token=iMwrPrVXNo_X4QSLjBEEFKy6CjkpOSwRbDmHVK_H_om8AFx9t2H0IXat8dA-pAFomjX8k5uNW7RlwiW9qqLPKc5WhKeS0nQvvb1jDWB548PLAC4CBC5hw1AlfQqTiM9zl1Ejnp7WXxbZ3LSpzTwwsS1ABSfOSQQuOzVWAID3FLFXtE0lddaiH5KJnAysb-17h6lKbAK7748fu7C_qiwvn1_Uadb-oLTTmPs-sSqt-vYc_zMdmD1dI8EU5kJIGddQwCwW0h4trlH8WSGzkIyJdl6qrKT69C7aOTZFfssn7d1F4kKP5szTrmR2UjPwKMETgo148WrQvYq3-YIUku1I07fz_mh_hqUT4wpANpFUwVhcKa-q5dmof-fW7cyA0rBBiNDOkA0Ejiy05feJZ4_hlXXY3S-_fY93opcgP6DqP8S3hTA7DO0hkrC218QOsO2R_Y0lL7XM9pQbkKHB_sZc22sKH45eQulqmkZLo4hz2e_2Wv5hiuOuiyPglEwEkmD6ltZY-6lQxynDfQn6ufmBaYNumXj5iSyoM8lkK-b8i41FQllFYj91hqKQNeet1kQtguCzC_C1Y1zi5wWlwxoD_kEQHyF_zrM8dbGd9uxXDmOjFIsiH4edZHQbpiV6DuDnbfX62efeWILdtjkxnYjguQrQNQfnvzoNLix7BO0K-ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
محمدمهدی محبی: خوشحالم که در پرسپولیسم، همه خانواده‌ام هم قرمزند!/ سیر فوتبالی محمدمهدی محبی، که پای او را به تیم نونهالان استقلال هم باز کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140128" target="_blank">📅 23:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140127">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📹
همه‌چیز از مصدومیت زارع، زیر دوش و در حضور پویا پورعلی شروع شد...
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140127" target="_blank">📅 23:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140126">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
پورعلی:
✔️
حاج مهدی یروز سجاد(پسر تارتار) رو اورد و یجوری باهاش رفتار می‌کرد که انگار نه انگار که پسرشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140126" target="_blank">📅 23:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140125">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
پورعلی:
🔻
من نزدیک ۳ بار میخواستم بیام پرسپولیس یبار نیم فصل ملوان که بودم و بار دوم که از تراکتور میخواستم برم گل‌گهر قراردادم رو بسته بودم با پرسپولیس و فشار هواداری نذاشت که بیام.
✔️
من و حاج مهدی رابطه خیلی نزدیکی باهم داریم و رابطه پدر پسری داریم…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140125" target="_blank">📅 23:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140124">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140124" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140123">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOZt5giFsBCKekMf7UYl-RFrLLCOi1onrhKFCiZMzqCDeJJfbK_mcmdyssMmPkSGyWE68MgSl0qdaaBbnTncFJZUfCRrq9Fu_gm5GGH_k17EWERmXjeASN6aGwwj2sgrSPACv2BL3HadeInuJj8G4wZYwlX5K0340RHSQlCoyOg6bqIspi5JW_vdfqJdC99hYsCf-3coPEbJpU9G6KqNePGD7z1aJ0AWhQ1U1F75z6iGDfYDtPRdMDTaqysKIrth53QajUL3Hr9ouCtECfV5A9CSyIqeimFXSDxPHsyHLHQJ5ONiDQKI59hunvUSLpeZPIHYIuW99bXStaVBKhB2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جادوگر استقلال عالی مینوازد
😂
✔️
اسماعیل بن ناصر هافبک فعلی الغرافه (که سابقه عضویت در آرسنال و میلان داره) مقابل الهلال اخراج شد و بازی با کیسه رو از دست داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140123" target="_blank">📅 22:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140122">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140122" target="_blank">📅 22:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140121">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGY_jBK6MbzW7dO5WxoYHDynQfX9mf8TLDd2gg9tlBzji9X1qS25LrVbU5reaxhmV_EPM-oTBUq7Ulm8FzymoaP6hnwTRgQpDVNvaERP2JdrNXld2-xlI_8rBBl6jTnCZ-khqVH92YjBAxyU2ATw74nwM-hA1mljrkO637Qh4XnFWFjDN33-QbW3ryQRR_QOLf_W7pWkvSaPuR0XkcO_ZTa8G0_3aA0m6t2ssUe3r_YptbEjZ7p4gbyiN8t_BzdKiyDYeF2ATCs5f015STV-YQETofhmkqfvaOQCp4qcchBUnyWRYq3YTHcG_GWW47J9-YCP_H2G1f2u8CIlvrRCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جام اتحادیه؛ لیورپول و تاتنهام، نبردی برای بقا در مسیر جام
🏆
🔥
[
لیورپول
🔴
🆚
⚪️
تاتنهام
]
⚽️
لیورپول و تاتنهام در جام اتحادیه؛ جدالی حذفی که کوچک‌ترین اشتباه می‌تواند سرنوشت بازی را عوض کند. کفه ترازو کمی به سمت لیورپول است، اما تاتنهام می‌تواند با ضدحملات خطرساز شود.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140121" target="_blank">📅 22:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140120">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM1-ACq3G2ezvM6e52XrzvUbDbUqJZ3XqNdd6ZI0wnLd16NoZ89c8krdKnjOqO1Cgd3yLJcJENYtkpE4FTEQkPlA5ZEsd3DvlUX6Z3v-cIBIDg61h0U2jyoGMCDlBiFe8Ypr571w-FOFpF8LmeiRQyDjBvU0dG9NWxVH5gDvvWConC2sbQ2ipS1D67bAfJTPhPZj1yqoCx3cVNOadJfOUBqhUlTig3mphMR6xfpNdgXpLPxaybtv_2mghy4d-3p2_3CTLf7q5CzaOvFwQvfev9hqInEBkV-mtqYgnjuu2iDY-f_23HbMfLZswdeo-o69idQ_BVZsQd14ylszjORHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
عملکرد یاسین سلمانی در دیدار های تدارکاتی
امسال پرسپولیس: ۸ بازی - ۴ گل - ۵ پاس‌گل :
پ.ن تارتار به شدت راضیه از یاسین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140120" target="_blank">📅 21:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140119">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
الجزیره امارات با مالکوم ؛ کولیبالی و تالیسکا و بیست بازیکن خارجی دیگه با گلگهر هیچ گوهی نخوردو مساوی شدن!
❌
پ.ن تیم‌های عربی زاییدن امسال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140119" target="_blank">📅 21:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140118">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbO_wyPkF_X9frGgPCEbY6Fp1kAlEj6iTdSXNkj12RitBe4FvKYJGceFloSwNDdHKpjA-IC4PVl6ZLVzkBzklTyaI-ND-OKJ3n2fKiCiyg3EdigTjX1b0d_KIC5uBn9rcnhdQhy-RUyr755B2jvaVwJRaZY6AkzhjXByiCgfHy0wPsWjp6oTj4MhHT-56zq6qGroBeCLBETIQyJil9p9GhMJ5CeVT7u6rELhJujr2pDDGj9uauyhfPk3Fa2Qc2itNE0ZRwssPgJYJkVpfnAfl3iP82dwf3ZObkv_VGqN4HVjCc0I8eFRUolvbdX5UEfWlcr4JOs3-UCa9ZbvLWnhHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140118" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140117">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4ET8RoebOXnoq945pIEuHxP7gH5VLK_i8YwQMXZ-26e_4z0B6ejfssJlT_oW8t4wkwKXXQedbxT3KqhtdMNNNpKYt2P1uzwBfOvuPDfU8ZeWa0j3z4dkkS_BIbUQrghkzj0Z3EtWXl8rQHQpSkqtleSKWPVa1f7IK98JBxmFSVOK_YOy9B6_syH59ZG5fe7s_kN_-iQ2WcNktwsjBTa3i-sOAtkx2miU9uaV9W524YkNenWc-BOYEaa7U4spzCkmxMT_h2bDxZeIklq_BcybQszQlj8FIuBNrgGO49zBjpcEP_ryBzfR2IBLiqGAGtHIO5_hurr4LeWcGOJH93uXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
ایران ورزشی: تکلیف دنیل گرا همچنان مشخص نیست و باشگاه هم پاسخ روشنی نمی‌دهد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140117" target="_blank">📅 21:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140116">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140116" target="_blank">📅 20:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140115">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
تیما عربی انگار ریدن اونطرف الاهلی که 2 ساله پشت سر هم داره قهرمان میشه دقیقه 90 تونسته به پاختاکور گل بزنه و 1 بر 1 کنه
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/140115" target="_blank">📅 19:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140114">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/140114" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140113">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭕️
⭕️
⭕️
باشگاه طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/140113" target="_blank">📅 18:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140112">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
🔻
🔻
🔻
سویه جدید کرونا، کاتریدا نام دارد!
🔴
مینو محرز، عضو ستاد ملی مبارزه با کرونا، در گفت‌وگو با #جریان:
🔴
کاتریدا، سویه جدید بیماری کرونا است که در اکثر نقاط جهان شیوع پیدا کرده و بیشتر در افراد مسن مشکل‌ساز شده است.
🔴
این بیماری، برخلاف قدرت سرایت بالایی…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/140112" target="_blank">📅 18:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140111">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
منهای ورزش
✔️
عکسی از افزایش عجیب و غریب قیمت دارو.
🔄
شما دیگه سرما هم نمیتونید بخورید. چون یه بسته آموکسی سیلین شده ۸۷۶ هزار تومن!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/140111" target="_blank">📅 18:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140110">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند در دفترچه خدمتی که پست کرده، بخاطر سرماخوردگی از کمیسیون پزشکی درخواست کرده اعزام او به جای اول، مهر، اول آبان انجام شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140110" target="_blank">📅 18:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140109">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
❌
پرسپولیس پیشنهاد تراکتور برای نیم‌فصل رو رد کرده و اصلاً قصد نداره اورونوف رو به رقیب مستقیمش بده. قرارداد اورونوف آخر فصل تموم میشه و موندن یا رفتنش برای تابستون هنوز مشخص نیست.
✔️
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140109" target="_blank">📅 17:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140108">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
اورونوف نمیخواد جدا بشه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140108" target="_blank">📅 16:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140107">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d87f4723.mp4?token=hUSfy__y6AzgqT3PvPxNceQ9Fir5Six1yUOn15Hwk0xwG4IxQBsgmHDH0VTV_uF8Cjjx4B5cGejfK75jlNoNw67M7O40kBvTOZjTn8saz97T-wHUpugELjlJEefeoaMRmQkqvn9gQfkdnM2DhfHkKMM6OiX9-0CBFZipIM6dWZtmPZo8jJk_chq-Uryd8Ac2q20A43hXaSVGA5-ADtnvtLn_XG8WkA8ffBh8K3DjeO18t4Z0qQtzBvycdP53eGG8OW4PcWdpXXNP10pX27VIaaZuWWs7oQduIfrnoa7TZZJFwdyGB6gZXBg84nxTTAdXAs1wUTZ6G0-tu25CMqAq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d87f4723.mp4?token=hUSfy__y6AzgqT3PvPxNceQ9Fir5Six1yUOn15Hwk0xwG4IxQBsgmHDH0VTV_uF8Cjjx4B5cGejfK75jlNoNw67M7O40kBvTOZjTn8saz97T-wHUpugELjlJEefeoaMRmQkqvn9gQfkdnM2DhfHkKMM6OiX9-0CBFZipIM6dWZtmPZo8jJk_chq-Uryd8Ac2q20A43hXaSVGA5-ADtnvtLn_XG8WkA8ffBh8K3DjeO18t4Z0qQtzBvycdP53eGG8OW4PcWdpXXNP10pX27VIaaZuWWs7oQduIfrnoa7TZZJFwdyGB6gZXBg84nxTTAdXAs1wUTZ6G0-tu25CMqAq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140107" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140106">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140106" target="_blank">📅 16:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140105">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140105" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140104">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔄
🔄
احد میرزایی، عضو هیات مدیره باشگاه پرسپولیس با جذب محمد قربانی مخالف هست و میگن لازم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140104" target="_blank">📅 16:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140103">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR7y2TKQPPGyEk_RbVpeHFmshVJCrLfrmOKDtUEz5z5435A65puSjYHefPR6YS016go-wHW-TeMuZ4PL1_6gwzsK8MwylI_9Q6PbJJJ0zdtZgVcUbr2WGFmKQC-ggg9_j8UX0IJ7diX2bAfw7T6dql4QH1ZljL28NDtaDZOk1ElclvSAHHa8Jlu5_ZmtxDN1pbHiKUFTKISuAAdedLdVjeYjgUJZauogIwy5ycHherxc0oIHzVnL0gOxYh4DecKRaL6_7xorPd9_CO-_lkKQCJ54u4q4pjpFXYBcRlhBE9-HVSA_1sJlqEVW90Xg0UmZ29-tdHnNtb04dEQHvktSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
حامد کاویان پور مدیر آکادمی پرسپولیس شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140103" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140102">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
محمد حسین صادقی برای اولین بار در لیست پرسپولیس پرسپولیس قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140102" target="_blank">📅 14:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140101">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند در دفترچه خدمتی که پست کرده، بخاطر سرماخوردگی از کمیسیون پزشکی درخواست کرده اعزام او به جای اول، مهر، اول آبان انجام شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140101" target="_blank">📅 14:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
عبدی: با ۱۸ بازیکن مقابل امارات قرار می‌گیریم/ بازیکنان استقلال و تراکتور روز بازی می‌رسند
✔️
✔️
زمان حضور رضا غندی پور بازیکن شباب الاهلی امارات؟ ما منتظر تمام نفرات ایست بودیم. مبین دهقان از امارات آمد اما غندی‌پور نیامد و متاسفانه او در تیم باشگاهی‌اش…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140100" target="_blank">📅 13:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or9fm_fHd1ZAukFNy-1Ssf-h5KzyGZz3tS-VHD751A-uKHYyxGmjhQG4EMgnBm8AwTEhWHOTrwb2Yba06CZDXHFUnUJDixPS3ctK1oX1X6HV_ff_vwtwsMHwu3MomdI86FmifjoB_O7ePm8NdE2DNQ-lPH0TtO-XQXSJ3cebMkmtjrboYp1TBYOUNwBJOr248PnKwE8Cm9danXPBknyH-L9Evn9A6f-fvtCfvMBEPDUpaM27oXPgzJ2YXSQ2AXY6HRMS_EotjMBGb-xfenJkP2bMNzINMJpzmhp3348iXNDWRr1nG9e9hxR2Qes0wfgiuJOzCCL4if8mc8IYMfLVQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
سپاهان باکیچ را می‌خواهد!
❌
گفته میشه سپاهان به‌دلیل عملکرد نه‌چندان خوب هافبک‌های فعلیش،
دنبال جذب مارکو باکیچ
در نیم‌فصل رفته و محرم نویدکیا هم تأکید زیادی روی جذب هافبک پرسپولیس داشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140099" target="_blank">📅 12:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⚽
امیر عابدینی مدیرعامل اسبق پرسپولیس: مدیران پرسپولیس عملکرد خوبی دارند؛قهرمان جام ملت‌ها نمی‌شویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140098" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgPvRvfsA6_mlJnzJ_bToLoZHcNYlToYI_vMr7D8EkqQgsiIr35chE5SKIqyck2rGPga4oEOatnxaWpJiPoWGZfpysl5sz_RWHTpxcjM5zCst2wAzCst8ibdgFQjylWNyGhXwBlQuPFpqfk7SEU4RlmR8hEbA9NSFoUKEyMNTsjmBbjMgZNH71xngYAhq-2mf7SGq1QCqN80BEwIrI73HjRoQazIn6dvTloLMFDjyGy7S1JmmUyUdF0TwxE5HDWVciQ22lD6-oFcwtl5K4SQCpDmOkEyKXM7tv-gNM3HmL4LJNI6zr20blxOG97wRM0Qdf1ZZsEIUvqpAuf8f4Q7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Liverpool -
⚪️
Tottenham
⏰
Tonight 22:30
🏟
Anfield
🟢
لیورپول با وجود احتمال چرخش ترکیب، در آنفیلد از نظر کیفیت و عمق تیم دست بالاتر را دارد؛ مخصوصاً مقابل تاتنهامی که در چهار بازی لیگ هنوز گل نزده است.
اسپرز برای جبران فشار فعلی احتمالاً بازی بازتری ارائه می‌دهد و همین موضوع می‌تواند فضاهای مناسبی برای حملات سریع لیورپول ایجاد کند.
کفه ترازو به سمت لیورپول است؛ برد میزبان محتمل‌تر به نظر می‌رسد، اما چرخش ترکیب می‌تواند بازی را از یک‌طرفه شدن دور کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140097" target="_blank">📅 12:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140096">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140096" target="_blank">📅 11:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140095" target="_blank">📅 11:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzfKmmmk7MZ0iBvWWiRL7LRnLE_nkiUkQTVgSfNh33-75CgD3FstSPKUETmim0U53bspLJ0D3gKlM7C5ZHFKQWov2YQmHRk9H1KL9uPD0VxGWekUgUZja2HBca7xv_gDQdxZxqSuow-nH1xnucbTvrVo5VBTojPsc2Co7q2q9fqmZk__B2ZJElZSAosacAYzUQRRZGLv48ywMxzbD3eqKjhnwGgRt4hrvLPCo5ZFBnsJxLPU5zltid-9qLAoKjBljLBE7mhJ6qvmg_ijnI0Rs_iDj7B2QZ24vdamhJwMV5GwHlYhzkoHWEUOOKjckdxunB94mJ7IoLsF7Pd5T3eCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرسپولیس؛ عاشق لیگ فشرده
🔺
اسکواد پرمهره پرسپولیس باعث شده برخلاف رقبا، سرخ‌ها از بازی‌های بیشتر استقبال کنن؛ حتی لغو بازی با خیبر هم با اعتراضشون همراه شد.
🔺
پرسپولیس برای برگزاری جام حذفی هم اصرار داره؛ چون با این تیم، شانس گرفتن جام بالاست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140094" target="_blank">📅 11:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140093">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
حسین عبدی: محسن خلیلی همین الان بهم زنگ زد گفت سه تا بازیکن مون برای دربی بهمون قرض بدین منم گفتم با فدراسیون صحبت کن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140093" target="_blank">📅 11:29 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
