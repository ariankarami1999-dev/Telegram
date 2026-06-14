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
<img src="https://cdn4.telesco.pe/file/b2bNhR22nvJfFMnl76ue4-sWN0YcEUKkcYOyh_k2-KjCzYjRhHnKTbYeYcuTFwI_lUw3ikInXJx-DONdCyiR128EYCFmMpCJGEfLYXq9fQW4LOxGt3a_Nm1KvhouNCEFa4xqfP9EUIxpyNO3LQNtMJz-phBGRciLZuIVMO1JuGFFNAen4lsQ-CmLQTrTaryke682CF-T5kDuMAer79044yHOpSkw36TxWNptuCCEozq4faEsfvsVgSPQWlLV8G1sQ5TyEuia1Xv3NyAZqW7lQ22i6jQza6Bo4SrVTKmdDdmuMIvaXkxhS1gy2AHt9yTEV84W7SRNkSLkYt4vUNiw4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 15:50:01</div>
<hr>

<div class="tg-post" id="msg-133482">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
بابایی مدیرعامل چادرملو: پرسپولیس با گل‌گهر بازی کند، نه با ما
🔴
اگر رأی کمیته استیناف به سود ما صادر نشود، باید حکم دستور موقت بگیریم و پرونده را در دادگاه حکمیت ورزش (CAS) دنبال کنیم.
🔴
به این مدل تورنمنت‌ها اعتراض داریم، اما راه آسیایی شدن همین است…</div>
<div class="tg-footer">👁️ 728 · <a href="https://t.me/SorkhTimes/133482" target="_blank">📅 15:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133481">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
برخلاف شایعات مطرح شده وحید امیری قصدی برای بازگشت به پرسپولیس نداره/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/SorkhTimes/133481" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133480">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
امیری می‌خواد یه فصل دیگه تو پرسپولیس بازی کنه و بعدش خداحافظی کنه. اوسمار هم می‌خواد تو تمرینات ببینه اوضاعش چطوره؛ اگه خوب باشه قرارداد می‌بنده، وگرنه از فوتبال خداحافظی میکنه و فصل آینده به عنوان مربی رو نیمکت پرسپولیس می‌شینه
✅
فرهیختگان
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/133480" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133479">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSi4gq_jjlLh21AjRSlyaYppqxewprzXhkwTqnj-bjPgOxODceA_q7c5q523xnD94juTGTluQsEcJCz21ZbsxZGJoW-ZJyWF7ZfOMATlOZg0z9eYC14C6MGKRqZGLUFF7ybWTuh78WIis2RRlAc_qWjK19cLPB-C_n2spbhcUrE4xH2yO1-xwaJUjjw4FkP4UjU7JXcDtPK5V9A6LQ2zMbMLB9MbPwrbEoqiQMrsi5EBIZaHJAHlWm21yp2i1Thk7oeJCUH2Xk22b6OgloBpE7mW28f4-xqhuzAyyv4XX0QkYUASfQssfBWDKljoglP7jsyhl2Y5XGqR3qy3GUHgQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
کمپین ویژه جام‌جهانی ۲۰۲۶ با وینکوبت ادامه دارد!
⚫️
Germany -
🔵
Curacao
⚫️
جام‌جهانی گروه D
⏰
یکشنبه ساعت ۲۰:۳۰
🏟
استادیوم ان‌آر‌جی
🎁
۱۵٪ بونوس ویژه روی تمامی واریزها فقط با یک گردش روب حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
📌
این بونوس ویژه فقط تا پایان بازی آلمان و کوراسائو خواهد بود.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/133479" target="_blank">📅 15:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133478">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
مقام ارشد ایرانی : طبق پیش‌نویس توافق، آمریکا قراره حدود ۲۵ میلیارد دلار از دارایی‌های بلوکه‌شده ایران رو آزاد کنه؛
🔴
از جمله انتقال مستقیم پول و همکاری در سطح منطقه‌ای
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SorkhTimes/133478" target="_blank">📅 14:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133477">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
رویترز به نقل از مقام ارشد ایرانی : طبق پیش‌نویس توافق با آمریکا، ایران قبول کرده دیگه دنبال ساخت یا گرفتن سلاح هسته‌ای نره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SorkhTimes/133477" target="_blank">📅 14:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133476">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❤️
🇮🇷
ادعای العربیه: امروز نشست مجازی میان هیئت‌های آمریکا و ایران برای امضای توافق صلح برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/133476" target="_blank">📅 13:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133475">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
حمید ابراهیمی:
🔴
خداداد عزیزی از افشین پیروانی سرپرست سابق پرسپولیس برای حضور در این پست، رخصت گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/133475" target="_blank">📅 13:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133474">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
ادعای علیرضا محمد، دستیار تارتار در گل‌گهر: باشگاه پرسپولیس با تارتار مذاکره کرده و اگر اوسمار برنگردد، تارتار سرمربی میشه! او می‌تواند پرسپولیس رو قهرمان کند! باید چه کاری دیگر کند تا سرمربی شود؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/133474" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133473">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umN5BmOx44JxewomIqnGE4TQkQrcwg45dL8CEeMdV3T6yyu6X6K61e9wL7-bFRX_I6Bs8wvLyr-RDoM5jHAmiKX6U5q0minpbFHFSrjqls4p1qEaVtXqU3OMQnNYtl7unlx1sFBiNM5FUaDxDk40mwspEw5DoFnqigOnbDgI1A6e6gq1JU_f062C5pbyoYnjrvWG6jw5imF7cUNRC_VUuSSlgPc4eQy23OJ78r2R4X3OfE9KQQlguMqVYFQl625_TJyQsxRrP6606GBN85UoPSoEcPrVTtsijY0xlng8xbfH76FDq-lnx0U06vYvk-yUaXGjyTS3hiFqXHmcLr2QvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوسمار ویرا بامداد امروز وارد تهران شد و تمرین امروز پرسپولیس با حضور او و خبرنگاران برگزار می‌شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SorkhTimes/133473" target="_blank">📅 12:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133472">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
🔻
وزیر ورزش:
🔹
در جام جهانی پرچم غیررسمی بیاورند یا شعار بدهند، سرپرست تیم مسئولیت دارد که بازی را متوقف کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/133472" target="_blank">📅 12:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133471">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
رسمی
🔴
آقا یحیی گل‌محمدی سرمربی دهوک شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/133471" target="_blank">📅 11:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133470">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
ساعت پرواز اوسمار از استانبول به تهران تغییر کرد/ ویرا سه عصر فردا در تهران
🔴
اوسمار ویرا که قرار بود با پرواز ساعت ۲۱ امشب از استانبول راهی تهران شود برای اینکه بازی مهم برزیل با مراکش را از دست ندهد از باشگاه خواسته ساعت پروازش به تهران را تغییر دهند‌.برزیل…</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/133470" target="_blank">📅 11:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133469">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
❤️
ادعای سی‌ان‌ان: مذاکره‌کنندگان قطری برای نهایی کردن تفاهم راهی تهران شده‌اند
❗️
شبکه آمریکایی به نقل از یک منبع مدعی شد که مذاکره‌کنندگان قطری صبح امروز در هماهنگی با ایالات متحده به سوی تهران پرواز کرده‌اند تا به تسهیل روند نهایی‌سازی توافق (یادداشت‌تفاهم)…</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/133469" target="_blank">📅 10:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133468">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
فوووووووووووری
🇺🇸
ترامپ: قرار است توافق با ایران  فردا، یکشنبه، امضا شود
🔴
.در روز تولد هشتاد سالگی ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/133468" target="_blank">📅 10:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133466">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
محسن خلیلی: پرسپولیس همیشه خواهان جذب علی قلی زاده بوده اما خودش نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/133466" target="_blank">📅 10:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
برنامه بازی‌های روز چهارم جام‌جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/133465" target="_blank">📅 10:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
برنامه بازی‌های روز چهارم جام‌جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/133464" target="_blank">📅 10:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
امیری می‌خواد یه فصل دیگه تو پرسپولیس بازی کنه و بعدش خداحافظی کنه. اوسمار هم می‌خواد تو تمرینات ببینه اوضاعش چطوره؛ اگه خوب باشه قرارداد می‌بنده، وگرنه از فوتبال خداحافظی میکنه و فصل آینده به عنوان مربی رو نیمکت پرسپولیس می‌شینه
✅
فرهیختگان
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/133463" target="_blank">📅 09:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
⚽️
🎙
امیر قلعه نویی سرمربی تیم ملی: برخی بدون مطالعه می گویند جام جهانی با ۴۸ تیم آسان تر شده است اما به نظر من اتفاقا سخت تر هم شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/133462" target="_blank">📅 09:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pz8PyrkmGNtrhfgiV8lLvezQCyYzMXNWzYJGOr3WiBB_t6MXd3m5F2mW2gign6oa6I3Nw6dqQg0HP0KI1u9cT1rwyWubHqDlWKLNxoN7dOAendZ377kipNK5ljhibxloBiaM4DkTnhd2qa-_Tz6UynbZGyBEyp-BBQj9kxV5X-d99JbWVsPYLph-aD-bKMUVSEXrx1tO-QpKd7V-ZsXmVmZlytWQXa8xUQ8n74QNsX0HunrsymxiHa0vwR-X_f6k79jECGN2ijDFl6nAI37rpz0uCFC-p4KZTSnfCd0c8_aQYt27XpHnnXurSAx2moxwZJjLrtFy5oxkhY4HTe0bkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
کمپین ویژه جام‌جهانی با وینکوبت ادامه دارد!
تب جام‌جهانی بالاتر از همیشه است و ما هم بونوس ویژه را ارتقا دادیم.
🎁
۱۵٪ بونوس ویژه روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
فقط تا پایان بازی آلمان و کوراسائو فرصت دریافت این پیشنهاد رو خواهید داشت.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/133461" target="_blank">📅 02:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3RICUPqLfRk6S0Yg-cLtIQhD4rfx2sJV2RlHWHugpuoIQpI4KfdIWTOwlKOCCt6pnnxiLP9c2YJBlQuMj7qQsu5PXyZPi7zHv_dH3bh_H94crrIyJdENh-CaM6IO__ZDiNQ5sJ6sw8GypTiokKCm2Wq5H_hJT84xh4bjRc7T_GncjHFL1eev4CMojkwpKh43hJSUyXt1f5KrQQeG15V817piWywsnZCvgnPWN-k1G4nm9a2YmdU6q1LwY2Q9r-mxjZ-PZMa4XCXck_9_t5sTG3gKO2NlO91GRMp9vDoptCg2n4F4n7Dtz8z_WZeESnYZf0JHKX9LybhzOqPMupgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
برنامه بازی‌های روز چهارم جام‌جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/133460" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPsta4kEiC79VqGVDNLSf6ZBnhDS2xJyxD8izONeLR1-N8FF5av7BW8eRdA46zdWsdm4gyQY8xDYq9JMpuEPF54io2BsNB2BrPRSE6N8q9jFeHC0r1VWpzS_zkHTdTK1BAwkn60nlbFJ7lplTl-kGb82olBgUxmdUZjbJUjp8TX0asluFt4_7h0ptce83d2spzr3r_ZyyGuAbQPePvotl_21qVunU8BFNYDkeW_1MY8beZRsn-dWkNzrLj5nyPB2KUb5SaR06vMA5a633T8sXRWoVj85Mlo20NHCfeRSSz6ZpUXv4BFh2zCOK1RprZYm9a02GFkb6WySL7qdamDoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کریستیانو در سواحل میامی بدنشو تو 40 سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/133459" target="_blank">📅 01:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133458">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M85ThHuxmraN7E3untkIxBAJvfighDtB0bEP6atDFjxoP6kPzAqQEz9KJ6ZpnYGpr85GbI_9ckrCCadA6Jv5wFvdVQ0qZvXqcpJdj1vuMrCKNO-mTY28JEGEye9NJkrbfvhPR59B-XcR4iKDs2U2LdOiDWA7-zYAQOUm8OUjM_UlK375FT05HoRP5paDJ7YhRF5VVrNx6S-8afqYl_Ko6poRS27u_SlEtvHftRb2eSXQEn30bBHvC5F_hZYQHKJZggqg4DglW0vkl6M4A3PlIpO4_RLKkQwteaTScVMc7KxSdBFpIP3KXuBtO5g_3b6NVipskb0JfRGpv28yCccenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حاجی‌پور، فعال رسانه‌ای: خیال خام است که فکر کنید دولت یا قالیباف، سرخود با طرف آمریکایی مذاکره و چانه‌زنی می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/133458" target="_blank">📅 00:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133457">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkX556fwuwKROG_X4LM6hCcIrw3p8J4UwpOBxp9xauwbrOP1aTowUdbcfhmB4LGTv2eJAU2fBov8t1ZTymdAXO_fI1EYCoBFXZV1rFnY34pA2G_cZXK33FHSaJCZDJra_z17rXmWQWsHIYT0ojBjpy-sANR0pJlbCuvRP2eEGMiyg0vkEnsjHFpCfSYipZ9uG9chI3miS89_4bdoM7rHsijxA65zT5k1ykLvqJ69K0AGzXUidKGvvYuVY1y58gcE7NRAtVlvZHf2cDaY23wJYzm0-2x9GK7kF-jGxzUK2V1xOqc4ErmGFX1HNbLnaKXGveZTHqJ1tWFlB5OtVpDggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول گروه B جام جهانی 2026 پس از پایان هفته اول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/133457" target="_blank">📅 00:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133456">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
#پخش_زنده مسابقات ورزشی /شنبه ۲۳ خرداد ۱۴۰۵
📺
#شبکه_سه
⚽️
قطر
🆚
سوئیس (جام جهانی ۲۰۲۶)
⏰
ساعت ۲۲:۳۰
⚽️
برزیل
🆚
مراکش (جام جهانی ۲۰۲۶)
⏰
ساعت ۰۱:۳۰ بامداد یکشنبه
⚽️
هائیتی
🆚
اسکاتلند (جام جهانی ۲۰۲۶)
⏰
ساعت ۰۴:۳۰ بامداد یکشنبه
⚽️
استرالیا
🆚
ترکیه (جام…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/133456" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133455">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
فوووووووووووری
🇺🇸
ترامپ: قرار است توافق با ایران  فردا، یکشنبه، امضا شود
🔴
.در روز تولد هشتاد سالگی ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/133455" target="_blank">📅 00:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133454">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
اوسمار که قرار بود امشب از ترکیه راهی تهران بشه تصمیم گرفته بازی برزیل مراکش رو ببینه و فردا به سمت ایران حرکت کنه/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133454" target="_blank">📅 23:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133453">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5825796732.mp4?token=DI9R04ccf6bbxUoQzrT5wczCUoRx1yGLLTVARNNoC_4mMI1yVaErNQryiijxhhI4QsfvHFcRfPbG30Qs4yEE3AzMkDJc_rkpRZB1P6f_F1qDpnNMjH9tJlgB-ak0oAJXZu57ZwW8brtjJcB4kMt9k2YKp3WVVl_9-3AstavT0wte_3MwqrejLXZaTKpwCoP-ft1DdpN-5rbmaH7Q1L_N7b9sMLqqns8Ywue0UIXyZoKkKVOPKJAMPELUwkH_TQwtHdQmJPP-Q6WnhXj9Vdpf9TWG6NZrYv2m9YqWnCZmMJLP47ELbKGBUvEH8RILZi27H_9ldJQF6MxaSPCh6OmouDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5825796732.mp4?token=DI9R04ccf6bbxUoQzrT5wczCUoRx1yGLLTVARNNoC_4mMI1yVaErNQryiijxhhI4QsfvHFcRfPbG30Qs4yEE3AzMkDJc_rkpRZB1P6f_F1qDpnNMjH9tJlgB-ak0oAJXZu57ZwW8brtjJcB4kMt9k2YKp3WVVl_9-3AstavT0wte_3MwqrejLXZaTKpwCoP-ft1DdpN-5rbmaH7Q1L_N7b9sMLqqns8Ywue0UIXyZoKkKVOPKJAMPELUwkH_TQwtHdQmJPP-Q6WnhXj9Vdpf9TWG6NZrYv2m9YqWnCZmMJLP47ELbKGBUvEH8RILZi27H_9ldJQF6MxaSPCh6OmouDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
کنایه‌های سنگین خداداد به سعید الهویی مربی تیم ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133453" target="_blank">📅 23:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133452">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/133452" target="_blank">📅 23:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133451">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133451" target="_blank">📅 23:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133448">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
✅
وقتی کل اعضای خارجی .هم بازیکن هم کادر دارن برمی‌گردن و تمرینات خیلی داره جدی دنبال میشه .احتمال زیاد بهشون با قاطعیت گفتن بازی های سه جانبه برگذار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133448" target="_blank">📅 22:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133447">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">#تکمیلی
✅
مشکلی که وجود داره و باعث شده استقلال پرسپولیس برای جذب کسری طاهری دست به عصا حرکت بکنن اینه که روبین کازان گفته برای رضایت نامش ۲ میلیون دلار میخاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/133447" target="_blank">📅 22:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133446">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
قدوسی، قرمزآنلاین:
❌
اوسمار قبول کرده که مبلغ قراردادش رو کم کنه، باشگاه هم قبول کرده که درصورت بروز جنگ و ناامنی، اوسمار می‌تونه فسخ کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/133446" target="_blank">📅 22:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133445">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
پرسپولیس دیوان افتخارات و اسطوره فوتباله ایران بوده ؛ تمام این چندین سال ثابت شده
🔴
🔴
مقایسه کردن امثال خداداد عزیزی با این عزیزان و بزرگان گناه کبیره محسوب میشه درست
✅
✅
ولی واقعا انقدر باشگاه ما کوچیک شده تا یکی عین خداداد بیاد داخلش پست بگیره؟
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133445" target="_blank">📅 21:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133444">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
#پخش_زنده مسابقات ورزشی /شنبه ۲۳ خرداد ۱۴۰۵
📺
#شبکه_سه
⚽️
قطر
🆚
سوئیس (جام جهانی ۲۰۲۶)
⏰
ساعت ۲۲:۳۰
⚽️
برزیل
🆚
مراکش (جام جهانی ۲۰۲۶)
⏰
ساعت ۰۱:۳۰ بامداد یکشنبه
⚽️
هائیتی
🆚
اسکاتلند (جام جهانی ۲۰۲۶)
⏰
ساعت ۰۴:۳۰ بامداد یکشنبه
⚽️
استرالیا
🆚
ترکیه (جام…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133444" target="_blank">📅 21:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133443">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇧🇷
🇲🇦
بازی مراکش و برزیل شاهد حضور بیش از 80 هزار تماشاگر در ورزشگاه مت‌لایف خواهد بود و تمام بلیت‌های بازی به فروش رفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/133443" target="_blank">📅 21:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133441">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس در حال طی کردن مراحل نهایی خرید امتیاز باشگاه سایپا و همچنین تمامی امکانات این مجموعه است.
🔴
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133441" target="_blank">📅 21:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133440">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
فوووووووووووری
🇺🇸
ترامپ: قرار است توافق با ایران
فردا، یکشنبه، امضا شود
🔴
.در روز تولد هشتاد سالگی ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/133440" target="_blank">📅 21:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133438">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWjAbgLEoHp4NXrtMyfl7KEbTN7O74VUAiEI4wLkSaHMP3KA03JITr46OSa_fOcDYGXb4l5y7y3VJoAEsyhfw53TQx2N-fVxvS4AjvwW9_pbUWCAOhqBBiWVCP6vj57Gnz3JO9zbFUHKIc_mBk_AKZiwAKZU40C9NGpnw_Rmz4Z2Rp46IbM7D7gZl609wZ4g4KzP2df8rvqkDqZNEW_2PZLhe0Pp-kjNVjtnJvJ1S-jpKdX6CNrA1pRsUMbl-SYwPmhbyNx2jkHOc0Q2sKvRRkHSqG1Ob7N1i1z-bkNKuZHTTODyKWQGeUlKZdJn3BdvtFUIa288EFG76xYYfKeXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇲🇦
بازی مراکش و برزیل شاهد حضور بیش از 80 هزار تماشاگر در ورزشگاه مت‌لایف خواهد بود و تمام بلیت‌های بازی به فروش رفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/133438" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133437">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: توافق اوباما با ایران یک مسیر آسان به سوی سلاح هسته‌ای بود، سلاحی که ایران شش سال پیش باید به آن می‌رسید و خیلی قبل‌تر از امروز از آن استفاده می‌کرد. توافق من با ایران برعکس است: یک دیوار مقابل سلاح هسته‌ای! در واقع، آنها دیگر نه خواهان سلاح هسته‌ای…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/133437" target="_blank">📅 21:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133436">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: توافق اوباما با ایران یک مسیر آسان به سوی سلاح هسته‌ای بود، سلاحی که ایران شش سال پیش باید به آن می‌رسید و خیلی قبل‌تر از امروز از آن استفاده می‌کرد. توافق من با ایران برعکس است: یک دیوار مقابل سلاح هسته‌ای! در واقع، آنها دیگر نه خواهان سلاح هسته‌ای…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133436" target="_blank">📅 20:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133435">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📸
گزارش تصویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133435" target="_blank">📅 20:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133434">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc8aRbdeUiSdZeiO7Ov3ioTQOeGRXHHGZ4l852T0MY7-XWi02-eiznDepNVnRsONlVP-ZNIe2ZkxU84UXDYtTXWN19q3ABFxZDU3monJ91QSXkRFAExxSCB2FAIfdTMjavGWtqQ4vQ0ZXDsIoXPdGN2KFQfjZ-UEz5cUgA40MIEYR1f0q7Cjvio0dd0REHYcauqF-O_ic8J5hr-KtjqBY06NjFZm_Rtdb6bV_lICD1uUIzQmNLAsfJW-fxnujujheN9MkY11r02Bs5Q6D44HTu__BLhHZ_09T8dxKOIOGNORcnOH-nyRXEJdSM4ctij2_NpnTb8RBAvrcepuGQ4Fdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گزارش تصویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/133434" target="_blank">📅 20:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133432">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzYhRZwTkq-WNbxR_EZk7n28-geckLfhm0ZWzLlC9LgKkgpaNRpsSBOJLyrPpdZW1zbBJJyNmzP377RKQ-cJXUMJA--bk0iCceiQxIc0fp-2KgU5TwSCiLExRQvPPZldvNKCNDArLFv6pd6yxtiqrMBNYMFWMidKhpd8UsziUgwpY_XcpBd-Tof7KhBWpxCgkckrhzh7q0fB2udcQdgZ_foKHovxr-pW6s_oAW40HkEvvCZ6Qw9eBaVa1CKYchFRDd9ecqzeycNeFNnCv1R93C9GOoY0fH__-0nUIIQI7m1AMW1GkrhxN9GVMT3XSJ28n3Ah0Nca2YfTicv2gbe9Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه C جام‌جهانی ۲۰۲۶
[
برزیل
🇧🇷
🆚
🇲🇦
مراکش
]
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
استادیوم مت‌لایف
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
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/133432" target="_blank">📅 20:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133431">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: قرار است توافق با ایران فردا امضا شود و بلافاصله پس از امضا تنگه هرمز به روی همه باز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/133431" target="_blank">📅 20:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133430">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWPElH7a8m409xiqynOboCS8tcXvykxDFTSH9uFSVnPrPYJZnm0dYeRg98A1sMToht0jw2r5bd6p-5XpoPi-bbwtulq5PKq7gzRyTdvdTBzkL_qC7CRb_fMv0Zcb8xCiHsPASnJsKbxuh0uL_9_v1PgF0bLaj4Mc_r9bQcDZ7_-ZMspdo17H51C-Z8qcY8i0VdY6oiU6DHcVWXb5Pag0W4NzLQl0P1xqwdbyp5HoWZuK4dwyvTL5fkoOjWwsB-5lTZrNLnRUt0cBiHOg_zzVo8TLPOIGQFzPR2lPZmyWZ5PcfqLR5Axs3xdKpcANGpOzz9brxUiicbYLfs5m_RXHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ: قرار است توافق با ایران فردا امضا شود و بلافاصله پس از امضا تنگه هرمز به روی همه باز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/133430" target="_blank">📅 20:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133428">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
درصورت تأیید اوسمار، وحید امیری با قراردادی یک ساله به پرسپولیس برمیگرده.///فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/133428" target="_blank">📅 20:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133427">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❤️
🤩
پیگیری حدادی فدراسیون را مجبور به ارسال نامه به AFC کرد
🔴
پس از اینکه کنفدراسیون فوتبال آسیا نام گل گهر را به عنوان نماینده ایران در لیگ قهرمانان 2 معرفی کرد، پیمان حدادی مدیرعامل باشگاه پرسپولیس پیگیر ماجرا شد و تماس های متعددی با مسئولان مربوطه گرفت.…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/133427" target="_blank">📅 20:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133426">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
باشگاه با اوسمار هماهنگ کرده که وحید امیری در تمرینات پرسپولیس حاضر بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/133426" target="_blank">📅 20:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133425">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
#نیش
✅
مدیران پرسپولیس مراقب پرداختی‌های خود به محمدحسین صادقی باشند؛ از گوشه و کنار خبر میرسد که باشگاه تبریزی قصد دارد این بازیکن را به خدمت بگیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/133425" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133424">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
فوری؛ اوسمار به دلیل بازی بامداد امروز برزیل مقابل مراکش درخواست کرده که امشب در ترکیه بمونه و فردا اول صبح به تهران برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/133424" target="_blank">📅 20:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133423">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
رسمی
🔴
آقا یحیی گل‌محمدی سرمربی دهوک شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/133423" target="_blank">📅 20:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133422">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
کریمی: اجرای مصوبات هیئت رئیسه وظیفه دبیرکل است
🔴
سید حجت کریمی، عضو هیئت رئیسه فدراسیون فوتبال، تأکید کرد آخرین مصوبه هیئت رئیسه درباره تعیین نماینده سوم ایران در آسیا همچنان پابرجاست و هیچ تغییری در آن ایجاد نشده است.
🔴
بر اساس این مصوبه، اگر رأی کمیته انضباطی درباره پرونده گل‌گهر و چادرملو تا ۳۱ خرداد قطعی نشود، تکلیف سهمیه سوم با برگزاری دو مسابقه مشخص خواهد شد؛ ابتدا پرسپولیس و چادرملو در ۵ تیر به مصاف هم می‌روند و برنده این دیدار ۹ تیر مقابل گل‌گهر قرار می‌گیرد. هر دو مسابقه بدون تماشاگر برگزار خواهد شد.
🔴
کریمی همچنین از هدایت ممبینی، دبیرکل فدراسیون، خواست به‌سرعت از AFC استعلام بگیرد که چرا در شرایطی که هنوز نماینده سوم ایران مشخص نشده، سایت کنفدراسیون فوتبال آسیا نام نماینده ایران را اعلام کرده است.
🔴
او در پایان تأکید کرد: «مصوبات هیئت رئیسه قطعاً اجرا می‌شود و اجرای این مصوبات بر عهده دبیرکل فدراسیون فوتبال
است.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/133422" target="_blank">📅 19:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133421">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
🔴
برگاتووووووون بریزه
😳
🚩
🚩
بازسازی ورزشگاه آزادی بالاخره داره تموم میشه و این ورزشگاه بالاخره شکل قشنگی به خودش گرفته
👌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/133421" target="_blank">📅 19:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133420">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
آکسیوس:
❗️
فردا توافق بین ایران و آمریکا امضا میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/133420" target="_blank">📅 19:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133419">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
🔴
وزیر خارجه پاکستان به همتای سعودی: مراسم امضای الکترونیکی توافق آمریکا و ایران قرار است فردا برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133419" target="_blank">📅 18:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133418">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
بقایی: زمان امضای تفاهم‌نامه فردا نخواهد بود
🔴
احتمال اینکه در روزهای آتی این اتفاق رقم بخورد منتفی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/133418" target="_blank">📅 18:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133417">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
❗️
اوسمار ساعت یازده و نیم صبح امروز به ترکیه می رسد و با پرواز ساعت ۹ شب از استانبول راهی تهران خواهد شد.
🔺
تمرین فردا ساعت ۱۷ برگزار خواهد شد و ویرا در تمرین حضور خواهد یافت.اوسمار فردا نشستی هم با حدادی خواهد داشت.
✍️
قرمز آنلاین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133417" target="_blank">📅 18:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133416">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
فرشید حقیری : بانک شهر تمام سهام سایپا رو خرید، از کارخونه بگیر تا تیم فوتبالش
✅
احتمالا با توجه به این موضوع پرسپولیس ب که سال بعد قراره تو لیگ یک شرکت کنه، جایگزین سایپا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/133416" target="_blank">📅 17:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133415">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
❗️
اوسمار ساعت یازده و نیم صبح امروز به ترکیه می رسد و با پرواز ساعت ۹ شب از استانبول راهی تهران خواهد شد.
🔺
تمرین فردا ساعت ۱۷ برگزار خواهد شد و ویرا در تمرین حضور خواهد یافت.اوسمار فردا نشستی هم با حدادی خواهد داشت.
✍️
قرمز آنلاین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133415" target="_blank">📅 17:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133414">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔻
🔻
🔻
علیرضا فغانی : گل سوم پرسپولیس به شمس‌آذر آفساید نبود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/133414" target="_blank">📅 16:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133413">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
❗️
شهناز شریف :
🔴
«ما بیش از هر زمان دیگری به توافق صلح نزدیک هستیم. با توجه به اینکه احتمالاً نهایی شدن آن در ۲۴ ساعت آینده پیش‌بینی می‌شود، پاکستان در حال آماده‌سازی برای امضای الکترونیکی توافق‌نامه صلح بلافاصله پس از آن است و پس از آن مذاکرات فنی در هفته…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133413" target="_blank">📅 16:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133410">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❤️
🤩
پیگیری حدادی فدراسیون را مجبور به ارسال نامه به AFC کرد
🔴
پس از اینکه کنفدراسیون فوتبال آسیا نام گل گهر را به عنوان نماینده ایران در لیگ قهرمانان 2 معرفی کرد، پیمان حدادی مدیرعامل باشگاه پرسپولیس پیگیر ماجرا شد و تماس های متعددی با مسئولان مربوطه گرفت.
🔴
همین تماس های حدادی و پیگیری خستگی ناپذیر او هم باعث شد تا فدراسیون فوتبال ناچار به ارسال نامه توضیحی به AFC شود و در این نامه تاکید شده که گل گهر نماینده قطعی ایران برای فصل بعد لیگ قهرمانان 2 نیست و فدراسیون ایران تا 10 تیرماه برای این انتخاب وقت دارد.
🔴
در این نامه فرآیند انتخاب نماینده ایران در لیگ قهرمانان 2 به اطلاع AFC رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133410" target="_blank">📅 16:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133409">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Db9CTdFoxUuOGVzhIkDZ3Fm8kVLMKSBLjW8-Kpccp4T5EjnLDYFK0cjqskpWsoydSCfpEviTy-7guXn7JALEvBAGjB7NIx3ECtcZrsel9HC3-4lOOzEUP-_XR1YYQZWKtrQJUpGo7Vt3DbFl3vcL9TF37sC8tdFipMC59Yts2FElrsTsTkxzRIsnb3GgY7JNR1ZhHX9M7Lon4mLwAbxBznDATeU2egXqrUsLehRIsVw1B8ztqjvSyMlPjn3KK3BI5z5ob59nNjGep5lh5VEw5168uDCJvxtc53S0AyB9VowIHImaSbHpNk3Hy5rrYY9oXUjp2G7BU3ko-_WCburI9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی
🔴
آقا یحیی گل‌محمدی سرمربی دهوک شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/133409" target="_blank">📅 16:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133408">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87af10648a.mp4?token=PYdk8azYejdglIgvER2tryouhHzxu2I9nd_RbnbBweD2NgeEWDpZQApoaYDDq0vSC1EJRjm6IWAYQpjctYhDK7DY8MDfCpiwTBZfViEGNMJviUS7TflqyFDMAUo8Fz_tN6UlAmG6IqDhtUYUXHL8TWoA0gY8nq-Wd_qeCJaq7YO9fFJxuFlfQO2oDK7Wx34hqXe5jTj9BZ8HsKqPPvvoWULD5KoXBtv_yiMMCKGnF-0HvPu2yVet4O2duY90bvK70aMObxXZMyE8hVO4pqOgtY3AfP9xSRLzX494lEIkMYFrQ8f9b1w_Uuc2nliaizEKXaolwM5U8DOY-KN6kvNqlRDUF2VXxUbpZ0ekZ5hrirHKRz1TptO1R2iwDqcJworRZzME0f23YQp7rggQtXahnD7bs-E51kZjNAcqpFIzJ_3UWfUN-ZnqXARcJPEUJENp46lWNHgPfcOSyE5SrHI9SE9PIYU15dE0xKe_kIxxFyrrOtt1Q4i3VEtA32IL-OvKSH_XNORsMzahm39gi5r1X4mWW3rb7kR5PhYZj24-K_NlK1fG5t05D_fH48Gd41qeg5azYX2t36uPj1cVPH5Vy-rc00PgBmNtYaGktOEsKzs5f5EeDBcwPGUUL7xAy0ajrpGNhntKgB66a9XXrWIh0NRFOyBXm3rFsKEwrGXrlLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87af10648a.mp4?token=PYdk8azYejdglIgvER2tryouhHzxu2I9nd_RbnbBweD2NgeEWDpZQApoaYDDq0vSC1EJRjm6IWAYQpjctYhDK7DY8MDfCpiwTBZfViEGNMJviUS7TflqyFDMAUo8Fz_tN6UlAmG6IqDhtUYUXHL8TWoA0gY8nq-Wd_qeCJaq7YO9fFJxuFlfQO2oDK7Wx34hqXe5jTj9BZ8HsKqPPvvoWULD5KoXBtv_yiMMCKGnF-0HvPu2yVet4O2duY90bvK70aMObxXZMyE8hVO4pqOgtY3AfP9xSRLzX494lEIkMYFrQ8f9b1w_Uuc2nliaizEKXaolwM5U8DOY-KN6kvNqlRDUF2VXxUbpZ0ekZ5hrirHKRz1TptO1R2iwDqcJworRZzME0f23YQp7rggQtXahnD7bs-E51kZjNAcqpFIzJ_3UWfUN-ZnqXARcJPEUJENp46lWNHgPfcOSyE5SrHI9SE9PIYU15dE0xKe_kIxxFyrrOtt1Q4i3VEtA32IL-OvKSH_XNORsMzahm39gi5r1X4mWW3rb7kR5PhYZj24-K_NlK1fG5t05D_fH48Gd41qeg5azYX2t36uPj1cVPH5Vy-rc00PgBmNtYaGktOEsKzs5f5EeDBcwPGUUL7xAy0ajrpGNhntKgB66a9XXrWIh0NRFOyBXm3rFsKEwrGXrlLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
فیروز کریمی: عدم حضور پرسپولیس در بازی های آسیایی از اعتبار فوتبال آسیا کم میکند عدالت اینه که پرسپولیس به آسیا بره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/133408" target="_blank">📅 16:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133407">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
پرسپولیس دیوان افتخارات و اسطوره فوتباله ایران بوده ؛ تمام این چندین سال ثابت شده
🔴
🔴
مقایسه کردن امثال خداداد عزیزی با این عزیزان و بزرگان گناه کبیره محسوب میشه درست
✅
✅
ولی واقعا انقدر باشگاه ما کوچیک شده تا یکی عین خداداد بیاد داخلش پست بگیره؟
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/133407" target="_blank">📅 16:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133406">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPorAMEy1u4KCh5ykl-PGWet370zdK30-yyXZtHyRKFIWWJ6V8JyVGpF5YhpkYkOQdskZnN5T9rGZ6Qm05ozLLjcsfQi9AQ7tVeVBnYwdW9fBvhdMnvZvQxK90smdjCC4pTNM1Mc8aAnWDaWYBm5oOIx4tjdv6zDVBohN_OEJgXmsZ3x6IBCwfnjAoFkvN9uMUM-K5qaCZx6mNEr-9ERJWI555TK-B4uRKCN9Z2QsU1Fm_PRuy5ER-ymFIr3EjhuvWtXonlf4j6dJ8iv_NKyOlAQf9eum46W2lVxDAK3ySaIfiLsmFBQYcmv-bPyRRE0gmWpGy1nhCK5eSrMbfu7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
شبکه آلمانی eSports One مسابقات جام جهانی رو به این شکل پشم ریزون به سبک بازی FC پخش میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/133406" target="_blank">📅 16:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133404">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
❗️
فوری/ نخست‌وزیر پاکستان: متن نهایی توافقنامه صلح بین ایران و آمریکا به دست آمد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133404" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133403">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🏆
ادامه ابهام در سهمیه‌های آسیایی؛ سازمان لیگ با فدراسیون هماهنگ
🔴
فدراسیون فوتبال همچنان درباره سهمیه سوم ایران در رقابت‌های آسیایی به جمع‌بندی نهایی نرسیده و برای تصمیم‌گیری، کارگروهی تشکیل داده تا با بررسی سناریوهای مختلف، مسیر نهایی انتخاب نماینده مشخص شود.
🔴
طبق جمع‌بندی فعلی، اگر اعتراض باشگاه
گل‌گهر سیرجان
در کمیته استیناف تأیید شود، این تیم به‌طور مستقیم سهمیه آسیایی می‌گیرد؛ اما در صورت رد این اعتراض، تعیین تیم سوم از طریق برگزاری پلی‌آف انجام خواهد شد.
🔴
در سناریوی پلی‌آف، ابتدا دیدار
پرسپولیس
و چادرملو برگزار می‌شود و برنده این بازی مقابل گل‌گهر قرار می‌گیرد تا نماینده نهایی ایران در آسیا مشخص شود؛ با این حال، هنوز ابلاغ رسمی از سوی سازمان لیگ صادر نشده و همین موضوع باعث ادامه بلاتکلیفی شده است/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/133403" target="_blank">📅 14:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133402">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
پرسپولیس همچنان دنبال تیم «ب» از لیگ یکه، ولی باشگاه‌ها قیمت نجومی دادن و فعلاً معامله قفل شده؛ با این حال سرخ‌ها هنوز بی‌خیال پروژه نشدن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/133402" target="_blank">📅 14:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133401">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
یک مقام ارشد آمریکایی به نیویورک تایمز گفت: «میانجی‌گران و مقامات نظامی ایرانی تأیید کردند که رهبر ایران از توافق راضی است».
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/133401" target="_blank">📅 14:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133400">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❤️
واکنش بازگشا به شایعات برکناری حدادی :
✅
آقای حدادی هستند و برای گرفتن حق خانواده بزرگ پرسپولیس میجنگند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/133400" target="_blank">📅 14:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133399">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_ufi8O_QU-HYlvmW77oDnDS2RSZh3sxZCljkPByh8Yev1vJAoTaQViJeS7wjbEWHif5ohwZNNNHmMUZ3I-QiS9u9RplYzNiJwvDTAJ20wEt4lNvA9ikooA1aJjH5jsuAto9gzKuMEcALZAH02ucrgnASmUnYJsrxPBwfTeqrOwCv5ULPE37zvLqc8RqeORkngTd4cZTxRnaYJmLMDocCfGcf_tLwMixO8SfIi314VMBQPgE6KhAs464FCPuVcgr47SqBrc6q9sPGuuwRqBI-9Zg2HTjA7WlgjqVRRJQKBJilv2kCMsWQO6eysPOmeBX3TKT8mGvu4AZVIYzyzX8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
واکنش بازگشا به شایعات برکناری حدادی :
✅
آقای حدادی هستند و برای گرفتن حق خانواده بزرگ پرسپولیس میجنگند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/133399" target="_blank">📅 14:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133398">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
قدوسی، قرمزآنلاین:
❌
اوسمار قبول کرده که مبلغ قراردادش رو کم کنه، باشگاه هم قبول کرده که درصورت بروز جنگ و ناامنی، اوسمار می‌تونه فسخ کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/133398" target="_blank">📅 14:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133397">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klH4dNvOeVanUilfLNX2jEVoCvW5A2KeyFTon8JJZSMVUjfYitPjp6gGcPM_Zpm7gJspjColUXx9RVIysMlmwo-5yHTqvxiVTE8Ry8G_oOWTxG1RH82plmAuTdPnGDFb0Hq5jJcQ6I9MVBEwkjkGltdiU6-4uhWa3xEl73ALb-UBKt5p3GJbHNo1OgLBXH70Hsa8y1cRqB1w-p2x7zTmVm81hXwCXkglQb6ZG3EaOlg6oHYtL3s7ZznNNsJEsFun2bK193G_ZEpsg7o_Bw2LTDmEnE6LkViz2tUpK-7kTJsNaiWCwfrig4Fek50JuF2hpXWba_Z6oHR-xysftqu7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه B جام‌جهانی ۲۰۲۶
[
قطر
🇶🇦
🆚
🇨🇭
سوئیس
]
⏰
امشب ساعت ۲۲:۳۰
🏟
استادیوم لیوایز
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
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133397" target="_blank">📅 14:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133396">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
امیلیو آلوارز به تهران آمد
🔴
امیلیو آلوارز، مربی اسپانیایی دروازه‌بان‌های پرسپولیس هم جمعه شب به تهران رسید تا در تمرینات حضور پیدا کند. او از میان شاگردان خود پیام نیازمند را به دلیل حضور در جام جهانی ندارد.
🔴
تمرینات آغاز شده است و جمع اعضای تیم هر روز…</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/133396" target="_blank">📅 13:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133395">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
❗️
اوسمار ساعت یازده و نیم صبح امروز به ترکیه می رسد و با پرواز ساعت ۹ شب از استانبول راهی تهران خواهد شد.
🔺
تمرین فردا ساعت ۱۷ برگزار خواهد شد و ویرا در تمرین حضور خواهد یافت.اوسمار فردا نشستی هم با حدادی خواهد داشت.
✍️
قرمز آنلاین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133395" target="_blank">📅 13:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133394">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
عراقچی: اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/133394" target="_blank">📅 13:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133393">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzun6L8EoQ5MTp5-hSP3gteUWJAeZPeENJpqvVhu22ia4mwyYnEal0SYAD29xdRkRCGvwuSuJILrm6Ypp3dumzmpgJnoPlkP1LQEpweX0bx0XRBrJgtg_jy9SO5qI3tvrnQqX1XJ_LUwfbmdS2LKTorAuUfdKpw0smqYd81xF91Gz53OMIeFGLvdcEsUUN7JrmMj4bxmR5K_I8KXijfWHlBHF2diBZm32gesHjlKgGIqDdujuZJCpVJHB4ABYkjzYEdOiKBNgfdZLUKDaQkJCaYLtvYdfo8TxwMqR_jImUYc9VEyn7HHHvu5f6HzZp3p3J4pTT9V1HVjCabVbSaSRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇮🇷
فیفا هتل شیک و زیبای وست دریفت (Westdrift) را برای اسکان تیم ملی در لس آنجلس معرفی کرده؛ فاصله هتل محل اقامت فعلی تیم ملی ایران در تیخوانا با هتل Westdrift در لس آنجلس 265 کیلومتر و با ورزشگاه محل بازی ایران و نیوزیلند حدود 10 کیلومتر و کمتر از 15 دقیقه است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133393" target="_blank">📅 12:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133392">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
عراقچی: اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/133392" target="_blank">📅 12:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133391">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
قدوسی، قرمزآنلاین:
❌
اوسمار قبول کرده که مبلغ قراردادش رو کم کنه، باشگاه هم قبول کرده که درصورت بروز جنگ و ناامنی، اوسمار می‌تونه فسخ کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133391" target="_blank">📅 11:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133390">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
طبق اعلام سایت فوتبالی اوسمار ویرا در راه ترکیه است و روز یکشنبه یا دوشنبه سر تمرین پرسپولیس حاضر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/133390" target="_blank">📅 11:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133389">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohAyDWKOyjsI7_gPq0hSVvJon3b5orJ1KnTuFMr0rUqPeMxKturU3EjY7oo3CAr2n19p2m9JiBvW0NzVFVhPHQc3ScXTPLhzTMW0zqHUeVXJ1aE_zkCxMW-uJl40IyIEjxjx0KVYGUOhykjDl80bZz5Z4T9l_4jCMDncRAZMw3K0QlXss7mtbRs1CtPk_mm44rHek857YaP_qsr2l4i6yr7JDEe5L6t6bBtUAWZuHNuh9Wf1gin56Cfr6tlSqVWQvnDiFHQBY6n6h7YQ8DudZhB7f1AoL06nALRN3-FYULkeYJFOkAk_9OchE3JxEFFWIb_XgN4skZa3Ttyv6L0bQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
پرسپولیس دیوان افتخارات و اسطوره فوتباله ایران بوده ؛ تمام این چندین سال ثابت شده
🔴
🔴
مقایسه کردن امثال خداداد عزیزی با این عزیزان و بزرگان گناه کبیره محسوب میشه درست
✅
✅
ولی واقعا انقدر باشگاه ما کوچیک شده تا یکی عین خداداد بیاد داخلش پست بگیره؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/133389" target="_blank">📅 10:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133388">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133388" target="_blank">📅 09:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭕️
⭕️
شبکه خبر: سردار حسین سلامی فرمانده کل س.پ.اه به شهادت رسید
⭕️
سردار غلامعلی رشید، دکتر تهرانچی، فریدون عباسی به شهادت رسیدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133387" target="_blank">📅 09:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133386">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
دیدار چهارم جام و سومین و آخرین افتتاحیه رو آمریکا با پاراگوئه از ساعت 4.30 صبح برگزار خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133386" target="_blank">📅 09:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133385">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsiT5xZ_76s5Ah8qEvaoI9kgoWTcUXkZwF97HuQoXzoTRvTdMqKyvFl6N-jFt8a4omRRXHw86Y3xZ1J_QnjLjPZT6edXj7nrZzXjJIfRzPytrVRbqfSvSK4w3EdQWz2Vjo46-b5qL40J2rdk8YUPCMNGCqircDF9DcYDDsT_NsFIY3AYnF0IASu2FUs31dXzlem7c5HPCsajpOfLN4wd99hweWBfODTeADAc_pLIXcKjMbuEKllvFhdJyc3mUnmqzOwgJJXhZPHRk1NS-CidBM84jYeDY4udCGuXyY4qBeUcQrCBKYYYSvIaW03vacVZDh1FcRF0oX0GGMOEJO9tKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پایان بازی | هفته اول لیگ ملت های والیبال روز سوم
🇮🇷
ایران
3️⃣
×
0️⃣
آرژانتین
🇦🇷
🇮🇷
25 | 25 | 25
🇦🇷
23 | 19 | 23
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133385" target="_blank">📅 09:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133384">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZnVRT2S4_4Kh3HVRgO-7695mk7Ly3zxvrZoHZhCKz_OULw_o0fAmODOuakDgLKOVqTHiUOSqgQM9hNsA5-CjtcX5N8pxppHf7hzDr2srorFlAuz4nfmgWJC7-9Zl-c8NO1N1ysST6qggBOmHZ15QitDgSpKrcSPq4Xd2bxsHlfKlwZfY26aNjRZFGJeq-vnHRZL1bVh4Jr7DE3m9ccA4Ku1fq0F3I4_yMfP2btZ9Pkw56Vb5W2pGi3ZQPug5RP5LcIm8m95StqZ5MDzfO0LokQE2RzwftHQPa-z2NUzBf-rEbQ-w5xgR1YA6af3gQTy51zK8b8BYuzScjJLe8zkHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
طبق اعلام سایت فوتبالی اوسمار ویرا در راه ترکیه است و روز یکشنبه یا دوشنبه سر تمرین پرسپولیس حاضر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/133384" target="_blank">📅 09:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133383">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇦🇷
در نزدیکی کمپ تمرینی ارژانتین تیراندازی رخ داده و تا الان یه کشته و دو زخمی داشته!!!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/133383" target="_blank">📅 09:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133382">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❤️
🚨
چند گزینه درتلاش برای لابی و جانشینی حدادی/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/133382" target="_blank">📅 09:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133381">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
این هم یادمون می‌مونه، در روزهایی که حدادی در حال دوندگی برای درست کردن سهمیه آسیایی پرسپولیس ششم جدولی بود، خیلیا داشتن زیرآبش رو می‌زدن تا جاش بشینن!
🔴
عاشقان قدرت
خائنین به پرسپولیس/شاهین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133381" target="_blank">📅 09:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133380">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R29WaFlVp8thdRWceirP7DNioZWOeZY_9WM2cNcn0v23fthq8kNw5bFQlLRxY3lbk7Kf6JJv8TgbUJIi3ZGR2WSwaNeLOINGY5FJb0zt45uuuRrMCwkOQ1NgsQ8wM7mA1cwAr8AtauY24j52ezGPq49FROtwViHiqDm4vtBC6y7BglO2flfW5mm4fR5Ep2RtlE3SK8yCaNYPkXETRazKLtwYaN5F-P7rqieJwUo3BekXAK9_cPgka97CWuBF-FXVq9z_gbGIcKJOUbofR2loltdBpc_B3A2W8h-DmJccWw2L5u9sRQhGVivwVLETNn0T_sgPL7ERBAdjkvIBZwkpCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
دیدار اول گروه C جام‌جهانی ۲۰۲۶
[
آمریکا
🇺🇸
🆚
🇵🇾
پاراگوئه
]
⏰
بامداد شنبه ساعت ۰۴:۳۰
🏟
استادیوم سوفای
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
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/133380" target="_blank">📅 01:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133379">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2DMrArn3MWGgFzIOo5uPYStBFZLKKjRwtZmGf73NwJkXioW7I8hRFSRWmBGnHVWUF_XKvqkddmxZXny2X7GOjIUSAFE5zUx4goFxvAMa3qCf5BrX33NvzakkrBYi_BLI5ZNKMzcHpkM21_7oy4xYMrJa5CdZInXZq3OAOwZ-rhrL6r0tTi9ViFVaw2aS7aQeI_PqvxphATLo-1jPCvhcexWFaiyjlEmHLISr6DARylpbcx2U0GT7KAaOFSFVHGbANreICQOAYBGTa1xf0h9w5KAdo-XnQiCtyEyir06SJznGJxJOQUkT5yCTSbuUUc1D3KUv1PtsNrQuaQngvUvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
دیدار چهارم جام و سومین و آخرین افتتاحیه رو آمریکا با پاراگوئه از ساعت 4.30 صبح برگزار خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133379" target="_blank">📅 00:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133378">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇨🇦
گل‌تساوی کانادا به بوسنی دقیقه ۷۸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133378" target="_blank">📅 00:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133377">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnYf-qN29rD_d_Q0xBShr-80BznpcwW8lEXS9-WSXQJV6IhmLXdQElq3_oUcaP92OzQ6X8l6z0KGpU4GGTvUKpowzo3HI6rB7s6VzWdvB1JVvVd9gjcA4nijZY1jjaCzojfebkeMzM22LqJ3HJ_WeFadSO_tC4WvGDyqxmBW7hscCRZ5GZPN1IIRfGJTzNGRLe6xeVaTjw64xywuXYBXNV6EWJxNN8MauI-RiceIETc7_5-3XLwBcF1AMM3Ui5yg7LswNQQIhThYmaNhZQFLSVK0ZcbgqCXtAclMSF0rw1sg9YTTrixjW_40NXDxz0W4wKri-y-XpjjDPMzBzuEm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
برگاتووووووون بریزه
😳
🚩
🚩
بازسازی ورزشگاه آزادی بالاخره داره تموم میشه و این ورزشگاه بالاخره شکل قشنگی به خودش گرفته
👌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/133377" target="_blank">📅 00:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133376">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇨🇦
گل‌تساوی کانادا به بوسنی دقیقه ۷۸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133376" target="_blank">📅 00:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133375">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=GPBIWdgz7P8siucMx-UoEz8BqEOJ-NiA1gEB1LxgSOAwK5KqDkWRqCPlN8n3yN_LVPn0qGVJ6JKvOZdnahGxt8Rqop_puPUdXxu-zDzlhiQurRscdTD8c2nDB6lkgXViLsJ2MfizfTRnb0LfiZua1fxNJzrlY5iR3QfALM2zOT1VONt7r3bw05p9R-JSBi-ge_ShnEQSHJvMV31-JitidJ0VKczi_rRLe4frIgZZMNoDrYoSgOAfTgbSKiaRZLzfJxcTxhQ454foL9gJgoHOvhBGii1Uj1SFFqxXMVRZnnl2Hd56KHQBpcQs_YaAUkLEuKLWpqFHQC_8B5miOoKdlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=GPBIWdgz7P8siucMx-UoEz8BqEOJ-NiA1gEB1LxgSOAwK5KqDkWRqCPlN8n3yN_LVPn0qGVJ6JKvOZdnahGxt8Rqop_puPUdXxu-zDzlhiQurRscdTD8c2nDB6lkgXViLsJ2MfizfTRnb0LfiZua1fxNJzrlY5iR3QfALM2zOT1VONt7r3bw05p9R-JSBi-ge_ShnEQSHJvMV31-JitidJ0VKczi_rRLe4frIgZZMNoDrYoSgOAfTgbSKiaRZLzfJxcTxhQ454foL9gJgoHOvhBGii1Uj1SFFqxXMVRZnnl2Hd56KHQBpcQs_YaAUkLEuKLWpqFHQC_8B5miOoKdlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
حمله تند محمدحسین میثاقی به منتقدان تیم ملی روی آنتن زنده تلویزیون: آدم مفت بر از خاله،
کصکش
تره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133375" target="_blank">📅 00:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133374">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
🔴
اوسمار راهی ترکیه شد/ویرا شنبه شب در تهران
🔴
اوسمار شنبه ظهر وارد استانبول  خواهد شد و بعد از چند ساعت توقف در فرودگاه این شهر سوار پرواز استانبول_تهران شده و  شنبه شب به به تهران می رسد و ضمن حضور در تمرین نشستی هم با حدادی خواهد داشت.اوسمار احتمالا در…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/133374" target="_blank">📅 23:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133373">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
همسر اوسمار تو یک استوری از اوسمار خداحافظی کرد و اوسمار راهی ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133373" target="_blank">📅 23:37 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
