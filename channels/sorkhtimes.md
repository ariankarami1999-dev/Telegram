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
<img src="https://cdn4.telesco.pe/file/KYGBn2ju5zM-6h5jXh0lXD1ijRVRY9OctGDLVnilMnYSYCf5Z9T4bXn0EXdkcq45qTnqb6ypvv1_-p5FjMQgJ-D7Xcv-iV61wAmnEk-U-BEIvLD2qkeDJ5ozTZe4P2_cp48UtPKY955xZQV4GaSUUfFM4lHlKjSh-RNaq6xqwL2ru5xdlJL8WH38vqa27aEkcM0XbQ7SjjLwl8jyakkV3n0QsjLdgkuZcYVYL06ATDg31CBI79953OlK8c1cge2i4VSpC1375tocI4_UnCyLVw8B9NN7xEv6GiBYDRp4WV5xIurBjsqubJclIpOO-FOndzjHifyFc1pL7WAFvLbe9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 21:42:35</div>
<hr>

<div class="tg-post" id="msg-141317">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qptULSh6VybIhN0KkdE7Q1F6CELnXDgEfAqnz_P13HqALsvqLbcZ1Fqi4zD1qK322vxKJu8Dir0KReJq9GMRL6RDPkcu6sWwTpprxFsNzP2eQ9dVOfENRp-JVJiJLtGxIVAboQL_2OqsjbXzqUrOFwTg51b1OgvlGV5kde0Lmqt688KVmMJGOPyfpShjvGuxO-eOLvpgRteHYI3siE63C0PP3hdbOnXnCau6vUnpr-ceRM9DLiMzTOCo6qRo0CD4BlbMQY1uM6AcwIM51nYenfqxGs6oU4STS61u5tUB-K_jvRVkAalDEdXqbRr710ZPHC_caLlvgdxkC2R05MxAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بیانکونری در کمین ۳ امتیاز؛ کالیاری سدِ راه بانوی پیر!
🔥
⚡️
[
کالیاری
🔴
🆚
⚫️
یوونتوس
]
⚽️
یوونتوس از نظر کیفیت فردی و تجربه، دست بالاتر را دارد؛ اما کالیاری در خانه می‌تواند با پرس و ضدحملات دردسرساز شود. کلید بازی برای یووه، شکستن دفاع فشرده حریف و استفاده از موقعیت‌های ابتدایی است؛ هرچه بازی طولانی‌تر بدون گل بماند، فشار بیشتر می‌شود.
سناریوی محتمل: برتری یوونتوس در مالکیت و موقعیت‌سازی، با احتمال بردی نزدیک و کم‌گل.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/141317" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141316">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووووری
✨
میلاد محمدی در لیست مازاد تیم‌ بلاروسی قرار گرفته است و به زودی از این تیم جدا خواهد‌شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/141316" target="_blank">📅 19:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141315">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9yd7hoqnwSqri5dIPryumfqArcg7sbhyusFlrqHKhxD2LkIikiyLbnfDIWTPn1MbhU4T97qFrwbExi3Vgwkr5AMK43NJFMpyDQziJox36ivUcNwvsL1jxl1daAmsTcCBXUjrPQOD2w6eChcyvGcmJFfUzJKFv6nbIHTP1gun6Jk8myt0mPQVClziLXHJjTJYuYkEwKWP1kQv0mQnkjdR5fLVs6EdJC1FaxT-7Z11xokjI1DT0HU-0a-I5TIFQBKaHeAI9Uxh1uEm_q2hBJJGMtH5oS6O0jt_LHHFYtFIinGcvElg1NNdjq2RtSaTb5fR8meWEznTcwENIRyyp_cJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر فاصله دارن.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/141315" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141314">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
پرسپولیس بزودی اقدامات نهایی خود را برای جذب عباس کهریزی انجام خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/141314" target="_blank">📅 18:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141313">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYjiTV4uEha2TfpFYJP4BxLzOVIq7j_gFOYjcD8m2UKeCgl02orBIS0td2wWZApJPegRmSlbZnfQdpjiJXBZF7SCTRjw9iVNmQFygVWtC-O-r2Q3KtJhtlQQX0YrPkQnhKohAIBJhegqLmtnYWUdGkw1afmqaZMwGdYH5QZ-mbyGUkMh4wTx9r-crnZGUB3y-zT6oQFZusGJjctiUpvE70MIkgpeWT9cubKqMF1ZsU1pgMh0f-Azu0YJjcQm1jO0zC2Qj71p31GzBVaf51_997bugTOT7RwC5s-pYWwVlalWQnmuJFi27ZMR13qHXuxvsCvV5AuYSd3bHT1i900D_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
علیپور؛ کابوس همیشگی صنعت نفت
🔥
🔴
علی‌رغم بازگشت تازه از مصدومیت، علی علیپور در نیمه دوم وارد زمین شد و از روی نقطه پنالتی گلزنی کرد
🔴
او پیش از این دیدار ۶ بار دروازه صنعت نفت را باز کرده بود و با این گل، شمار گل‌هایش را به عدد ۷ رساند تا برترین گلزن تقابل‌های یک دهه اخیر پرسپولیس و صنعت نفت لقب بگیرد
👏
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/141313" target="_blank">📅 18:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141312">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
⚪️
⚽️
تاج: با یحیی گل‌محمدی برای هدایت تیم ملی امید به توافقاتی رسیده‌ایم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/141312" target="_blank">📅 18:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141311">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
مهدی طارمی زمینه آزادی ۸ زندانی شد
👍
مهدی طارمی در طرح حمایت از حقوق اجتماعی و رفاه زندانیان نیازمند استان تهران، زمینه آزادی ۸ زندانی را فراهم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/141311" target="_blank">📅 16:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141310">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
فوری ؛ خبرگزاری ایسنا :
🔴
🔴
🔴
فیفا در جواب استعلام باشگاه استقلال ، پاسخ داده که یاسر آسانی رسما فسخ کرده است و بازی کردنش غیرقانونی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/141310" target="_blank">📅 16:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141309">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
با تصمیم زنوزی، علیرضا بیرانوند تا اطلاع ثانوی و پیش از سربازی خود در هتل تیم امید تراکتور مستقر خواهد شد و حق حضور در کنار تیم اصلی را نخواهد داشت
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/141309" target="_blank">📅 14:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141308">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
#شنیده_ها
⛔
⛔
استقلال با هواپیمای تشریفات دولتی ( ریاست جمهوری ) راهی قطر شده.
⛔
⛔
نکته: تحریم هوایی آمریکا شامل هواپیمای مقامات دولتی نمی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/141308" target="_blank">📅 13:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141307">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
#شنیده_ها
⛔
⛔
استقلال با هواپیمای تشریفات دولتی ( ریاست جمهوری ) راهی قطر شده.
⛔
⛔
نکته: تحریم هوایی آمریکا شامل هواپیمای مقامات دولتی نمی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/141307" target="_blank">📅 13:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141306">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
گفته میشه دولت قطر به تیم فوتبال استقلال قراره مثل آمریکا ویزا ساعتی بده تا این باشگاه برای بازی با الغرافه مشکلی نداشته باشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/141306" target="_blank">📅 13:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141305">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhN9yjs-yn1kdLgMIfeIVgMQhSC-g0usXfylQ6dLN-pH-d5QZLXjbpZXYg9VPrQX5-GPkbB6PEYeC4dtjCZMG-bOUqcch3Ht15kW3nE_TZjlA8UqYO5r1TpAyVtt6GQ9TPlrlOfVN_jWa6OVOZ_V_dH4K3ueA_xJe1aVGy2bdOzVuS8VGU6F-LzjvCeJxgtWYY0lrRYM4rju1fnGY4nB6l3m1R3Qs_if4WLiy8Lok1rDYLCYWdEK4B-gHEELNVIU1UYsfuGZ-TeNrNz1cOoM0nlkNF2xPY718GvygOE2aM6liz0Gzl0gxePjM9CZMDPufVnqUaXecaTIYErbFHlBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیژن حیدری داور بازی‌ معوقه پرسپولیس - خیبر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
😀
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/141305" target="_blank">📅 13:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141304">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9LoDE47Qp4E-WbXqaQ0oNP98TEGB-Rakf8deRRMup4tciAFxKKaBZxO8K8DxzhC3uFF_s7obbLb8eaL7r5O162D_F87lbMEHKC56ZFVPAXZ17_VKR3qRxcjdVvGapQwOXyRgPOSPjbL5RDyBMkml9FquPFjeThQRCqNWkNldyhCHm5tau-JdZZYlSnSdiZ5q68hgmBR0WslVtf7RT_j3aXUST-crXQWKYGK_kXbdX59qA12-6PyusyLIrftS_cB9uH160UPuSlvD2e8KIANBF_BaQT3GzcEYxaUe_9EhyJFAI9_jaKSTr_k2mHoVqnVU5knyWDxnKMiKOC2ul2fcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Liverpool
🆚
🔵
Man City
⏰
Tonight 19:00
🏟
Anfield
🟣
سیتی در ۵ بازی لیگ ۱۳ گل زده و با میانگین ۲.۶ گل، قدرت تمام‌کنندگی بالاتری نسبت به لیورپولِ ۷ گله داشته؛ در مقابل، قرمزها در آنفیلد از امتیاز میزبانی بهره می‌برند. غیبت الکساندر ایساک و کودی خاکپو می‌تونه قدرت هجومی لیورپول رو کاهش بده، درحالی‌که هالند با ۵ گل بهترین تهدید سیتی محسوب می‌شه.
از نظر مدل آماری Opta، شانس برد سیتی ۴۰.۷٪، لیورپول ۳۴.۶٪ و مساوی ۲۴.۷٪ برآورد شده؛ برتری آماری خفیف با سیتی است.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/141304" target="_blank">📅 13:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141303">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUMRLUyuzuASfYHvZsZ8h_MlDrDOAyR7k2zm-I6rTo-4aou0QCe1DgUDdt3doQ4LfYENXu4Dwz2EfSvC378m9QFKNhlUWuZPEFa034dB8H4Ew0tk35LDc-LmEqhXotBiqbL6wVTAzKkyM35Tm8mmoyOCS5L4n3LSe0dKs4BdmFlMfsYaaAmPzgbEsYb9zAoQM_eHsWqfps-jGVSc1_VJw7ZaDSQ6wDpaRoPdVjVXA4ZKnorEXZdTynlrmmjAf3BRc0X4wLG4k-YlNqrDutc1v8Zn_V08lA5GJVpBL_0Y2iv1vmiG4balK_M485sHC__FTpzOFEjcK4RC764yGy15Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ابرقویی تارتار رو راضی نکرد؛ با بازگشت کنعانی و ایری، احتمالاً دوباره نیمکت‌نشین میشه.
🎙
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/141303" target="_blank">📅 12:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141302">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🇮🇷
👤
🎙
برانکو ایوانکوویچ: می‌توانم بگویم بهترین نتایج ایران در 40 سال اخیر را من به دست آوردم؛ قهرمان بازی‌های آسیایی شدیم و به جام جهانی 2006 صعود کردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/141302" target="_blank">📅 12:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141301">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
درخشش سرخ‌پوشان ازبکستانی پرسپولیس در رسانه‌های کشورشان!
🗣️
ایگور سرگیف با پاس گل در دقیقه ۵ و اوستون اورونوف با گلزنی در دقیقه ۸۴، نقش مهمی در پیروزی ۳-۱ پرسپولیس مقابل صنعت نفت داشتن.
🗣
درخشش این دو ملی‌پوش ازبکستانی مورد توجه رسانه‌های کشورشون قرار گرفته…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/141301" target="_blank">📅 12:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141300">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
⚽️
گل‌های پرسپولیس در بازی تدارکاتی دیروز مقابل فولاد هرمزگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/141300" target="_blank">📅 12:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141299">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
باشگاه با انتشار این ویدئو نوشت : نگاهی متفاوت به شانزدهمین گل ارونوف برای پرسپولیس
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/141299" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141298">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf86a8d14.mp4?token=iy_km9n7chSonDhxNcsIXKZTNrpoMpLVwJBX4cmvEHVjUMJhPNbmkQx_XOyLiyvJMe_GYqzjXt7K5Q9_Xffg-esdsew4n9qvYlzkpjA9T0yO4YuKaxbbIYe_WvGGS71ku7TbShKvjhajj-sTeiRPj6C2eVjq4e6UQfLqNcvf8IBE8kkF1SM5cINaUDvySk-7-oG4LDyAQcgFaKwsMtUZONc4h6UStaT4soAnD1l7hMfkjM817Ojis51gNGgrDQTeFEa6Flp4tG3WDTa_7_oXYjHvX09oRF0N9Z7e64nWW0UaTv5S1GuqBkDSa9B7g0zUxmT-CLUcVFaetQ-qtuzrQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf86a8d14.mp4?token=iy_km9n7chSonDhxNcsIXKZTNrpoMpLVwJBX4cmvEHVjUMJhPNbmkQx_XOyLiyvJMe_GYqzjXt7K5Q9_Xffg-esdsew4n9qvYlzkpjA9T0yO4YuKaxbbIYe_WvGGS71ku7TbShKvjhajj-sTeiRPj6C2eVjq4e6UQfLqNcvf8IBE8kkF1SM5cINaUDvySk-7-oG4LDyAQcgFaKwsMtUZONc4h6UStaT4soAnD1l7hMfkjM817Ojis51gNGgrDQTeFEa6Flp4tG3WDTa_7_oXYjHvX09oRF0N9Z7e64nWW0UaTv5S1GuqBkDSa9B7g0zUxmT-CLUcVFaetQ-qtuzrQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
باشگاه با انتشار این ویدئو نوشت : نگاهی متفاوت به شانزدهمین گل ارونوف برای پرسپولیس
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/141298" target="_blank">📅 09:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141297">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2Jm0_YaUREhoE6aoRM6dlXHMr6uzC-GAKIF9H4fMd943yMEGVWXeEZ3vbPg3pmjS7W3k3ID0cuMH5y54jRs0iOUTb1elzwVhq2MTnC8WPzyy-ap5CuTyUnYEnqvxd3tclyqujpWjPxNX8f6BPQq0EBwU4NNiwpy_mxcRwZwJ-kOpdox2U6iWB9voNx4OmLNfcWhBlpssWXZJH1ots2aKV7XBkyIOjGGGcT5zNH-9h8Ow8Io83pwS6idrxfYy3pt3OpV9YBImmBAjPBcwbM_SniTAWSNNlHTeQ_WO758mC5PDykwQ5KYn0JVUWKyaEwte7y2Q7cMkJlJa9cKpbjyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهرآبادی از هفته‌ی بعدی فرصت بیشتری برای بازی کردن برای پرسپولیس دراختیار خواهد داشت.
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/141297" target="_blank">📅 09:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141296">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9DJXT8DG-ZQCBUlV3kHqfWCQ9jCN3f0C2l6Spwy__BwCgqqIC0c8ZysGsis0TUVSFHn5Ak-W0t0KRJYC345d9cRJWcOR6BuoZoGrno4Lxa5mzqsv2zTS-yYULoIGiOY-tIIZL0_d3BT98npFMfu9Krqgo36a5wo79BuQ1AsbG-VES-JsmSBq0MqGTRzLpH8AEUADtzkecFwc68fTiopM_uA6fNffy5MSqBq6vTy3zFgWxydGP8ZMZ2Czr2pGo_jbqdK9msCkNb93wWGtZm_LWz2Kt8jatbCvDnB0mE_X3kwGgSfapeUOOr9SMFAvLdFs0kj94dEmEPyEfHtdGaXsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/141296" target="_blank">📅 08:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141295">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=V2f6tWCrOFphqoKlrvCvt5920XfXDsHY0WXkgiXOR92q_CkiOMizKKFFVdEuZ3FiOXl4SNT4zRyNqCUAPTWiSkf5I_cIzK9nIk-v0thrwOdN00qfgEPL_bimMZVQrkj6cET88CRlLLO5Qix8xKTXVbjzKPFWM1gmfXyZwetOlmfl6pxYhvALYgRh6vvhx6DUHiPSr7veySNEDzurCI-2aWce-H4je3sqYeDIp-aw4o-qJLUts5R8YdFGd6gXdIfsaMruxSfGpTIIU5fn_uHKfzy9N7bNlHkVTXer1AoI1G86KAQfBxWvadRfziWhJrRfIW_ETHDrk80jpjoItwNWaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=V2f6tWCrOFphqoKlrvCvt5920XfXDsHY0WXkgiXOR92q_CkiOMizKKFFVdEuZ3FiOXl4SNT4zRyNqCUAPTWiSkf5I_cIzK9nIk-v0thrwOdN00qfgEPL_bimMZVQrkj6cET88CRlLLO5Qix8xKTXVbjzKPFWM1gmfXyZwetOlmfl6pxYhvALYgRh6vvhx6DUHiPSr7veySNEDzurCI-2aWce-H4je3sqYeDIp-aw4o-qJLUts5R8YdFGd6gXdIfsaMruxSfGpTIIU5fn_uHKfzy9N7bNlHkVTXer1AoI1G86KAQfBxWvadRfziWhJrRfIW_ETHDrk80jpjoItwNWaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141295" target="_blank">📅 01:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141294">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP9PpsbMARArGcMee67IEXCOfhPf5ALa6madbfh8EQcID1WULqmJekZ_gKOWdDgtZmUQXNQePmVjWBKsS7pRdcCm3LEjJNciEFoh-ofpadMl9hXfVWnHUFtYPyjEYsU69e4ZTNgfvsdyO5_9RF-TscTEBaZP8Nxzy6x2JMYj3aDqp5dReYPDwl5E1XHrtV79xNk7KFx5Yef9f6a0nnVrD6WcYPLbtxG3vDdScQ8DMd3eBaTBvPW1DpRVWGkcwHfSXz4vILfnt2GT8qPssKvvuuw-CCEiACpcHwqcB8jrb8D5NG3WjARuQzwUD-yftQuQuTxCFzw172L1QtS1AdgruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد خدابنده‌لو به اردوی بعدی تیم ملی دعوت خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141294" target="_blank">📅 23:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141293">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=G-PDiRlGZHInxlK-S1hcs9SAwyH612MpyH1yHM_Z1aFLS3j9TVcMsmwPvg9OhRKaZNx6R_SCORW30I3ldE1t5wgmt3ZVZ0BSfSvPqiiMhm65-Cs4HkaWV3RTKr_DNc_oEaA2nyb8ypbwFu6CCvaDFvj9rnu2vVBt3jtlnTAjs08e38CMcmd4luBa85bOCs6_Mq_CdwIq1TFh4Q5xlrhJ5S9uVxRqUFtXhU8WzDn-JTEh-7Klr-HQjXKclJamURsSfWbQlpvs0i5vBbpCR_fkXR6AymIGB9y7c0K7sCvYfkywtEctSMmx1jdZ1J308fb4ZvAFVyW3kpNieI0CLMnajBD0n7dDmt3QFgb_RS0M9NfVsBpl2-kZDPs7aMUaNDX3nMUmkvhRqJgjpTPd2YTB_24Y6yh4dSWAn5pWx5QAmzbMq4HCqsHJfue3iFendaDnulES4aA-TOhwtFFEn3BAlZs6Mm0RPBMVQbnWf1674znZYjbCVflV3RlvtjRpg8mEMA_wCxFreQyVA_ZXSQxd_rxJ-WXEnMhPu7dUX7HnJWigelKg3VrzNwzQFZCfV6i7vzhX-Qp8LwRpOUbsn7j_jpOkVf4SNW4sudCwUVWUUrYaK7ND114N64QB6n9WEKuLtJ11M84TpDlESWXHBA7ZAcMgxqaZoYo72EJgUTcTyZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=G-PDiRlGZHInxlK-S1hcs9SAwyH612MpyH1yHM_Z1aFLS3j9TVcMsmwPvg9OhRKaZNx6R_SCORW30I3ldE1t5wgmt3ZVZ0BSfSvPqiiMhm65-Cs4HkaWV3RTKr_DNc_oEaA2nyb8ypbwFu6CCvaDFvj9rnu2vVBt3jtlnTAjs08e38CMcmd4luBa85bOCs6_Mq_CdwIq1TFh4Q5xlrhJ5S9uVxRqUFtXhU8WzDn-JTEh-7Klr-HQjXKclJamURsSfWbQlpvs0i5vBbpCR_fkXR6AymIGB9y7c0K7sCvYfkywtEctSMmx1jdZ1J308fb4ZvAFVyW3kpNieI0CLMnajBD0n7dDmt3QFgb_RS0M9NfVsBpl2-kZDPs7aMUaNDX3nMUmkvhRqJgjpTPd2YTB_24Y6yh4dSWAn5pWx5QAmzbMq4HCqsHJfue3iFendaDnulES4aA-TOhwtFFEn3BAlZs6Mm0RPBMVQbnWf1674znZYjbCVflV3RlvtjRpg8mEMA_wCxFreQyVA_ZXSQxd_rxJ-WXEnMhPu7dUX7HnJWigelKg3VrzNwzQFZCfV6i7vzhX-Qp8LwRpOUbsn7j_jpOkVf4SNW4sudCwUVWUUrYaK7ND114N64QB6n9WEKuLtJ11M84TpDlESWXHBA7ZAcMgxqaZoYo72EJgUTcTyZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خداداد عزیزی: تو فرودگاه بغداد ۲ تا سگ دنبال مهدی شیری و اعضای تیم افتاده بود!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/141293" target="_blank">📅 23:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141292">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4B4EDqcM4nK6IR780LLBrfI8aUAmHSXqG6er3jJJk9iuu-fkVumlPmsquaCU_xeZwHVwoLUZJwUNZEFzWmIPsG2UOntoBoqW4W_lszbEB9lrzLyJZPon6iUFLjMzYv29DvdC7XNC18iIpH9R2LKHj7LuEQ0tCoSm22KJ_4g0oXJoBXrzc6McDQ39TW0pCmdDKeLWX51x80aZkDH50WwufPcIBrq789iNdGu4jwuFwkOWbemKdKOGICmzIzlx5tq6BKVLCWxv4pS0Qm21ie9M7P1NykHFAYGwpFewAKcKt0I0aDHkclICT_Vhggz78uBiCTBoIVD2uORvsw0wFhzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
❤️
⭕️
⭕️
علی علیپور و تیوی بیفوما با هم مجموعاً روی 73 درصد گلای این فصل پرسپولیس موثر بودن
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141292" target="_blank">📅 23:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141291">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭕️
⭕️
⭕️
#جنگ_کفتارها
🚨
محمدرضا زنوزی مالک تراکتور به تمامی ارکان باشگاه دستور داده  که هر کسی با بیرانوند در ارتباط هست فورا  قطع ارتباط کند!
🚨
به گزارش فارس امروز یکی از اقوام  بیرانوند که در مجموعه زنوزی مشغول کار بود به محل کارش راه ندادن!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141291" target="_blank">📅 22:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141290">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
✅
تاجرنیا: بیرانوند دوست دارد حضور در استقلال را تجربه کند.
😀
به صورت جدی درباره بیرانوند صحبتی نداشتیم اما به ما هم پیامهایی رسیده است. اما الان فرعباسی و خلیفه را داریم بنابراین بحث بیرانوند یک مقدار این موضوع از ما دور است.‌ در هر صورت او هم شایسته است…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141290" target="_blank">📅 22:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141289">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fcc915c7d.mp4?token=a1PYdBPEAJPn6q4KoDOUdUHN90PlOyp-uWWSnsVNe7pPs9gESLMuqr_-yJY8_ZvZNd27yuVq62N5uiD8lTf9X_IwMqnse78OALr4-Z3eizb2jijNpiWTLIQSTfztBIgHxA4rhuHtvEpg2O9lu2RuR9P9RfvjPjbmSq6_M_vFCam_qkKurGb13AU1SH9Wt8FCMw9RNONO6cvLMaPG61Yd8yqRiKTcy7HNqUTai2sk4vIB3zDWwJiPUEAQyC3hy0_bBuzO6nwEjZbtU0vKrDU9Zy4M92U6WszpG7dfYL4nS7ZZoIVlKbg4UZvWTBGEN15Bg-uNL_XHQibq4kLJxhlA_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fcc915c7d.mp4?token=a1PYdBPEAJPn6q4KoDOUdUHN90PlOyp-uWWSnsVNe7pPs9gESLMuqr_-yJY8_ZvZNd27yuVq62N5uiD8lTf9X_IwMqnse78OALr4-Z3eizb2jijNpiWTLIQSTfztBIgHxA4rhuHtvEpg2O9lu2RuR9P9RfvjPjbmSq6_M_vFCam_qkKurGb13AU1SH9Wt8FCMw9RNONO6cvLMaPG61Yd8yqRiKTcy7HNqUTai2sk4vIB3zDWwJiPUEAQyC3hy0_bBuzO6nwEjZbtU0vKrDU9Zy4M92U6WszpG7dfYL4nS7ZZoIVlKbg4UZvWTBGEN15Bg-uNL_XHQibq4kLJxhlA_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕
محبوبیت؛ فراتر از تصور
🥹
🔴
هواداری که با وجود سختی‌های جسمانی و مشکلات مالی، خودش را به ورزشگاه می‌رساند تا پرسپولیس محبوبش را ببیند و تشویق کند، به معنای واقعی عشق به پیراهن سرخ را نشان می‌دهد
🔥
🔴
آقای بازیکن! قدر چنین هوادارانی را بدانید؛ آن‌ها بزرگ‌ترین سرمایه پرسپولیس هستند
❤️‍🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141289" target="_blank">📅 22:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141288">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-0-eo1uMoGaP8GX-EmJF8FBy-vcCSZbv3RefI-3LEcmxNphR_0MobJAJ5XU2BMZ7Fj10UdkWIVUU6VxU0tYq7Av_v9zGBk4ykRcD06_MAznloI-tDXxs52xUvHj5TKp1hZqjZ649RaLNKCA3qVGP4aRwwScPs1F4n81PwDaeZPxyNeNUPdbWPthUPVwJ8i_Y_fVXCfLUoF7KJxx1miQWrQkxK4XyExYynCrYqvgT0OoFpno8yVkMUYm_1ObZsSDp3H8r7hIk8fUNJNMiqpN1QrqMMpzpIiXq7EvuOMc6WQu2y8pIlSVV_TrHzzlHIcXR1MMpTHpHxrkEGasP4oApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
محبی؛ ترابیِ جدید برای اورونوف
⁉️
⭕
محمدمهدی محبی در ۷ بازی با ثبت ۲ گل و یک پاس گل، عملکرد قابل قبولی داشته است پاس گل اخیر او روی همکاری با اورونوف، نوید شکل‌گیری یک زوج جذاب را می‌دهد
🔴
محبی می‌تواند با تبدیل شدن به مکملی شبیه ترابی برای اورونوف، هم به پیشرفت خودش کمک کند و هم اورونوف را به اوج آمادگی برساند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141288" target="_blank">📅 22:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141287">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
خطیبی از هدایت فجر سپاسی برکنار شد
❌
با اعلام باشگاه فجر سپاسی رسول خطیلی از هدایت این تیم کنار رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141287" target="_blank">📅 22:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141286">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY2cW12zidW5cgDvW9dO5t4IcfgIoTHDWXpD07uYHhu0A6eBDKw5JhkYjAZU6p0fWIlvVKjjz_p4-j2qpgd7KiIRVZhsJgVCOzUK_SdawnNHi7Rl64JCYMLZUXnSRSqWBME54xmmUe7lIqsJCx4JOrVXCsWMqc7_U9zotGWsEE9E0mXYmFMPBRK9N8CLrbQF-Sou6K52XYNgBpz7p5VodVINH_m3iW6nWnVsOVwj__4SqaSDaZ-cHiUGcVmFebvQ4w80Nx7P8dptOjvQoRRpw8nPgUGttQRldUy0HXhpFOx79apP8HPzGcKPMlUk9OtP86c6x2VdqWfLdxvL2W60Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141286" target="_blank">📅 22:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141285">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j288PXnypmm4k8o-qsyH3zc6rcvu534KrCbB7yKxG7CmgEuQCwFEirfqflahGHEoqxPIEBNa4ujSGN6spewq7RaQrP0uzdGZwUmSxW9LJ3mAcsvVDN6F3chgokR2zfoNQB9jKEFDCed_4rhkv8c89mxc7c-whKlBpycNV7-gKztQRAVICQNv2pjHsEwxJx4KOm2_rATKPIz1s9N5C30DBfrqdexTdb11hecQhrhQq5Whf4X4JoyhZdFNzRyZ5XiJNz5a7T6JCxhwfZ3Jhid9MvHuSssI-L1yqzr80udlXpaz4tyuiSKyJ3Mx5UFTMWogRJhO87fjrsczwYe_I4axVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جدول لیگ برتر در پایان هفته هشتم
✔️
پرسپولیس در دیدار معوقه هفته هفتم از ساعت ۱۷ روز چهارشنبه به مصاف خیبر خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141285" target="_blank">📅 21:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39e252ccf.mp4?token=vfuCat5ws3uC5MJbyuL-xDpfD-6JfU8srg2B4ZqA4S1ZNGwAZ_CfXIZL4nivzB-1Hkn2VZZ8_XRgkbJdLwJnaSa4ckQK7pjzqZhhca1MuC87fGijiiVOwWHg9HmET9zZoI9TTl8h8BxMmYqzzd_7bypGzT_Ecas7B9ceQikORHb1WGrV4_VfZu3ntcDDbghaZtW4nvdm8uVV-m1ybeIIQAWpnbOjmlFly37PmOe8OWgb3kU7oTmEPlp1gpB8-0Gw1zwgHaWZZZa31eale2B9Q8ZYCWM_f8O1riH16V6lyZwWduZMv0kQ6AgljDeNo6SZiJnlvDDaXPcPcrxDiRRAHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39e252ccf.mp4?token=vfuCat5ws3uC5MJbyuL-xDpfD-6JfU8srg2B4ZqA4S1ZNGwAZ_CfXIZL4nivzB-1Hkn2VZZ8_XRgkbJdLwJnaSa4ckQK7pjzqZhhca1MuC87fGijiiVOwWHg9HmET9zZoI9TTl8h8BxMmYqzzd_7bypGzT_Ecas7B9ceQikORHb1WGrV4_VfZu3ntcDDbghaZtW4nvdm8uVV-m1ybeIIQAWpnbOjmlFly37PmOe8OWgb3kU7oTmEPlp1gpB8-0Gw1zwgHaWZZZa31eale2B9Q8ZYCWM_f8O1riH16V6lyZwWduZMv0kQ6AgljDeNo6SZiJnlvDDaXPcPcrxDiRRAHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در پایان بازی پیکان و شمس آذر، رضا شکاری که پنالتی تیمش را خراب کرده بود، دل و دماغی برای خروج از زمین و رفتن به سمت رختکن نداشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/141284" target="_blank">📅 20:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141283">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b96d408ed.mp4?token=Z3DyMbNL3VjtgSqlmW3Zengxfmema7PJDY_gCMsDU63RsdS_93v110a0a8VqTHdzKbQSb5TSb-vmqqV7oBg9eohrJKqW_AbqiSmVord5P29XMBo-vRxmEa_3vqQab5N0jrMbSZOGSe0WdAlmdtYnZsSDkvaQvDWikiC2_ewmKnA2QKu-d9LR52Icgv9v5Hvty4ABaCnG4zHhhx7ldb15qlL97z6xuBMC9IUN7HVAdr3_TICYLhWPBUq_-Z0VUBc0TfYMQXxxYoZFCzNofXe4-s9cnESVP0gg65WZ1df3iYXXNfO62mws44hrpHj-m8Okgt2eGcoihnedT2sHdBwWEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b96d408ed.mp4?token=Z3DyMbNL3VjtgSqlmW3Zengxfmema7PJDY_gCMsDU63RsdS_93v110a0a8VqTHdzKbQSb5TSb-vmqqV7oBg9eohrJKqW_AbqiSmVord5P29XMBo-vRxmEa_3vqQab5N0jrMbSZOGSe0WdAlmdtYnZsSDkvaQvDWikiC2_ewmKnA2QKu-d9LR52Icgv9v5Hvty4ABaCnG4zHhhx7ldb15qlL97z6xuBMC9IUN7HVAdr3_TICYLhWPBUq_-Z0VUBc0TfYMQXxxYoZFCzNofXe4-s9cnESVP0gg65WZ1df3iYXXNfO62mws44hrpHj-m8Okgt2eGcoihnedT2sHdBwWEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ساکت الهامی به بازیکن تیمش اینطوری سیلی زد
‼️
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141283" target="_blank">📅 20:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141282">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0eUqkKWtFKXEPjYr7Dbd8nD5X2Y_wOQbnVRFnIFdymuh1R6vKhjQZqAIPWZcfM2dGZ6eR5CuDnabcrHy4VBefljpvcQ1yUsrBM52RNZPQUhW46YWQLxD8VMWr7AwTcBhbV3YTNDAmLhNOx9FAC9mlan4Ui3BVO0q6nFZR8_A5KwSsUMDA3xlpa0HY_7NkmVURTg0uZggz0bga4tzp2FT90Ne_GVTOSF07B0n-J5rjQhW_wqOESLHUebUZ9Ow6r9BMYdN1SxplmSDfWewYwikPlIziB-KePhgfdr9dvx79rNKJRU4bATxZcytipIw65DcHgQ-HknsfMrBZF0Jl0Ozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Real Madrid
🆚
🟡
Villarreal
⏰
Tonight 22:30
🏟
Estadio Bernabéu
🟠
رئال مادرید در ۷ بازی ابتدایی لالیگا ۱۸ گل زده و فقط ۸ گل دریافت کرده؛ میانگین ۲.۵۷ گل زده در هر بازی نشان‌دهنده قدرت هجومی بالای این تیم است. ویارئال نیز با ۱۳ گل زده و ۱۲ گل خورده، توان هجومی خوبی دارد اما در خط دفاع آسیب‌پذیرتر است. باتوجه به میزبانی رئال در برنابئو و اختلاف کیفیت دفاعی دو تیم، برتری رئال و احتمال گل‌زنی هر دو تیم از سناریوهای قابل بررسی این مسابقه است؛ البته پرسینگ و مالکیت بالای ویارئال می‌تواند بازی را رقابتی کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141282" target="_blank">📅 20:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141281">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
تصاویری از آخرین تمرین پرسپولیس پیش از دیدار فردا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/141281" target="_blank">📅 20:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141280">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
به تمام دیتاسنترها آماده باش داده شده تا در صورت وقوع جنگ٫ اینترنت سراسری قطع شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141280" target="_blank">📅 20:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141279">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
🔴
🔴
محسن ربیع‌خواه مهمان ویژه برنامه تلویزیون باشگاه پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/141279" target="_blank">📅 19:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141278">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
پویا اسمی که در بازی دیروز برای تیم بزرگسالان پرسپولیس به میدان رفت، امروزم در بازی مقابل جوانان استقلال فیکس بازی میکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/141278" target="_blank">📅 19:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141277">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
تیم پرسپولیس از دقایقی دیگر در دیداری دوستانه با بازیکنان ذخیره خود به مصاف فولاد هرمزگان می‌رود.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141277" target="_blank">📅 17:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141276">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H2jU9rMkuq0I-3uwtHu-dCQfwWrIsQuGjmwPcQdaG16b2HppUSvdlFelFc7Q7efJJUva13frfE0Yfr7y_hDkoeFb4ZEcP-wnGvfJXRCyt-zaDyks_bP18GEEh8cDstx37jB2XYW_6AY3ZleaOml4jWyzNyypSuuCudr5MZ5QEEBjq0Dzz73C0wK3PTWnepm0LCbcCYDVN5Y6tVwqSHH1i9AuIfii6kZF7DvPuNjSHRmz2vIGUoB1-Kihd-ogtGcIlKCoWMCF00q5_atCJiYuUQ07ZwOgfXBRJ1gIDIzPYVe-q4FsqfaLg5TS5KLkJkW7i18QC3dpZXIfU6ICmDbmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
#جنگ_کفتارها
🚨
محمدرضا زنوزی مالک تراکتور به تمامی ارکان باشگاه دستور داده  که هر کسی با بیرانوند در ارتباط هست فورا  قطع ارتباط کند!
🚨
به گزارش فارس امروز یکی از اقوام  بیرانوند که در مجموعه زنوزی مشغول کار بود به محل کارش راه ندادن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/141276" target="_blank">📅 17:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141275">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/141275" target="_blank">📅 17:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141274">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/141274" target="_blank">📅 17:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141273">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eW2MwCM9UkJr8c05-wHZh_KRrVLkYYicRslVW97pU8ifQ8sgz636WZjVDNA4_x8aQh-grG68RcK1hs_EzyeDnp6rW_SnijcEWtHnaQaOlrUFaIXOTbK-MdC-leuHPHj24nBhrVVl3CDnF-Q75WLRQK7XZfJ5V-9nhzNX8_W2s7D_E6z8qBsJ_uQurjEq1LOWEOz8azPR33fqj9BuHVDBmCFN7KoG9-sgDdYUL67WUpK-UffS_M9khdBibykD0MmCSpr8tJoeitkrjyU7gWAxY8Z_dZTnGi8JzntVyzg-4FhiQdeIxyq5p44DG8TbrhC_ZSr2GNfc2hy9UrfWgiojaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
ارونوف با ۱۶ گل، دومین گلزن خارجی تاریخ پرسپولیس شد؛ فقط ۴ گل تا شکستن رکورد گولسیانی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141273" target="_blank">📅 16:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141272">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/141272" target="_blank">📅 16:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141271">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/141271" target="_blank">📅 16:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141270">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">💢
پرسپولیس با ۱۵ گلِ زده، بهترین خط حمله لیگ برتر را در اختیار دارد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/141270" target="_blank">📅 16:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141269">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f241a3512.mp4?token=WvsajNJa0e_FR0OUwHGlSItt6mVb93Y-nPxH5i05i3diehKqEfRupcs-_QHc8j4_MLXFUK6Nq-TQrkelxP2EwSQrVopz5s3f_tprI2M9uQlwhbMws6BbvMDjwxxh37dpn7dJpN2ph0xEcW9aQTPGhrOt6VisgMNSKd9HjPaPAMjCH0jkwL1uQX1HDtkRuPfU5xF4fddBDTFBh1pEvrv4vFoqPzM--mMLafc6q_p1ISuFhNPGbv9UM1-ED9MaICkBq0NES2ai4l6Dj-LzmG_rcrv_eviOVQF8vosuJkGeYCCQ5jZLjgjNn0H75lPC1rzkxVscDT-kP9caBMcJhDccKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f241a3512.mp4?token=WvsajNJa0e_FR0OUwHGlSItt6mVb93Y-nPxH5i05i3diehKqEfRupcs-_QHc8j4_MLXFUK6Nq-TQrkelxP2EwSQrVopz5s3f_tprI2M9uQlwhbMws6BbvMDjwxxh37dpn7dJpN2ph0xEcW9aQTPGhrOt6VisgMNSKd9HjPaPAMjCH0jkwL1uQX1HDtkRuPfU5xF4fddBDTFBh1pEvrv4vFoqPzM--mMLafc6q_p1ISuFhNPGbv9UM1-ED9MaICkBq0NES2ai4l6Dj-LzmG_rcrv_eviOVQF8vosuJkGeYCCQ5jZLjgjNn0H75lPC1rzkxVscDT-kP9caBMcJhDccKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
ضدحمله زیبا رو ببینید
🔥
🔥
🔥
❌
با ٣ پاسِ تک‌ضرب و پاس‌ تو عمقِ زیبای محبی به بیفوما تک‌به‌تک میشه اما حیف که این کارِ تیمی با گل تموم نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141269" target="_blank">📅 15:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141268">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4b0NQ8CIVkK4R8sN50lZL2zM4simny5weoymYO5gLLTh6mhETeIxSB2MH5FXAPOFssz8d4kvZqkQdp50JEi3mJVl24k9hJAZfKTJ0ZatebA6GnZA10-7atA9pwJrPw0eaSN7Eyjk7OzKceY-jFRyHpU7fEQU7GSZZ30y7mCq6wUfsNur1ZmUfLGnqfUDhrqoc53XdihfbsVPAh9_udxM3abjanduADw2mSmCZ9o2aVewde6-ENqCGNLC9vIyDt09j8p9U-Cxu2DCCqk0Nf_V3H_wxqlHvdOSD43ZCrzDYkBqZvrypz8eiXFgT_1vRhaC2HC-kSSRoszlEmGYbS-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/141268" target="_blank">📅 15:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141267">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4727e2d06d.mp4?token=NozL4QJ4856_Vr_MScMz3L9lj7I0roIaXcd0G2KoMmB_I5KVf72AL3IxfakE2mV1oUrDeSLaxjwNPMDb9Kc6jARa2abZshFsycxTgH6i__CFC_Inar09C1uN8z-wYAQmTsjP1MVV0lLFdZEqCPq3Gf0OpNXwcSHxIYDs9MXE5T4-1ZOLfyP3syBvPxtRn7yNhpzaLR-cD3gCCuEpkSn-OYWpJb-BmxVxsuFnDza1If3Ni2P4vvc7SZ7jN7lpSx6yDAqpkC01o8Sg65pE7lbsotiCTa0k8IIaXgejRct-Rrm8SB53YOwtsvWQ74JsCHn_DUy9tjwDDGMAMCgNjeDi2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4727e2d06d.mp4?token=NozL4QJ4856_Vr_MScMz3L9lj7I0roIaXcd0G2KoMmB_I5KVf72AL3IxfakE2mV1oUrDeSLaxjwNPMDb9Kc6jARa2abZshFsycxTgH6i__CFC_Inar09C1uN8z-wYAQmTsjP1MVV0lLFdZEqCPq3Gf0OpNXwcSHxIYDs9MXE5T4-1ZOLfyP3syBvPxtRn7yNhpzaLR-cD3gCCuEpkSn-OYWpJb-BmxVxsuFnDza1If3Ni2P4vvc7SZ7jN7lpSx6yDAqpkC01o8Sg65pE7lbsotiCTa0k8IIaXgejRct-Rrm8SB53YOwtsvWQ74JsCHn_DUy9tjwDDGMAMCgNjeDi2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بیفوما و آن فرارهای همیشگی‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/141267" target="_blank">📅 15:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141266">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
گویا پویا اسمی که امروز به میدان رفت و جوانترین بازیکن تاریخ باشگاه شد یکی از بازیکنان مورد علاقه تارتار هستش و شدیدا بهش علاقه داره و بهش قول داده که بهش بازی بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/141266" target="_blank">📅 15:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141265">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
این وسط شله زرد هم فجر و شش تایی کرد ..رسول خطیبی ی تنه فجرو نابود کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/141265" target="_blank">📅 15:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141264">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
فووووووری
🔴
باشگاه پرسپولیس وویس هایی از ایجنت یاسر آسانی داره که به پرسپولیس گفته آسانی بازیکن آزاد هست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/141264" target="_blank">📅 15:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141263">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4sj3NPRdH0-IjRW3Vr8es6oSdyRDJVJFIc0xBzHu0j9IsT2UY95zc1r-7vP7rWJ2PbfgyztBbzXBlLfBfERglRdJyFSeDcQtKxJTJhsnqhwzqzavYeEetwSOOZEnql1Ck2wPPJs-yZrrWt9xj8Sq1_mfuvToEgCKVN4ihmUUTwDhcZOIUCQysdta2eA8fnHxTd_MrZsVojkNZIS0_5TsLIX9THZ69Ps43rJZxXHrV5tdS34mso1HOFRpUR1qedL53P1XfUS5xFD3PfB4BkkKzspDkhB-8jTFRUWRU_0AbeRQw-486CcqL-ZhQM5op8x4HfntzE8LhAB-BHXEqnZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
نبرد حیثیتی در لیگ برتر؛ شیاطین سرخ مقابل تاتنهام، جدالی برای اثبات قدرت و تثبیت جایگاه!
[
منچستریونایتد
🔴
🆚
⚪️
ت
اتنهام
]
⚽️
منچستریونایتد با تکیه بر امتیاز میزبانی و قدرت در انتقال سریع توپ، به‌دنبال ضربه‌زدن به فضای پشت خط دفاع تاتنهام است. تاتنهام با پرسینگ و بازی مستقیم می‌تواند موقعیت‌های خطرناکی خلق کند، اما فضای خالی پشت مدافعانش نقطه‌ضعف مهمی خواهد بود.
سناریوی آماری محتمل: بازی پرموقعیت با شانس گلزنی هر دو تیم؛ نتیجه نهایی تا حد زیادی به کیفیت استفاده از موقعیت‌ها بستگی دارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141263" target="_blank">📅 14:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141262">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
🔴
باشگاه پرسپولیس با ارسال نامه‌ای به مهدی تاج غیرقانونی بودن قرارداد یاسر آسانی با استقلال رو یادآوری کرد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141262" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141261">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzOjCGmoSJ-QXmq1StsmxymGwltHgYTtj-fP4b-U0pKfaNvGmJYeuSrVlyVmJlqRQOrJ65INK2R94VCgWoaUYA1BXmB7ryMFAfqmQQJazLgmW3vN_8MUgECD20exzyLhAE_7hD_TAw5vkTDBkoNQ3zJyMVpTgw-mnqQlBEJ3CTdJNNfpoFchVroSkbIYIVvRyYY2ecu-mjuLyiIPDH9XyrUCMzLZwq4tIJ1mDVFn5-bVeGXPcH_EzSWbFF5ACN666jysCcgBDl_BjHjFXFmIWL40kE1FTWfKrh20YN88YxfnMmz6Awi_4eP7TBV5PqcXVd9JWXDvSY8pWHdix_LQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
پرسپولیس با ۱۵ گلِ زده، بهترین خط حمله لیگ برتر را در اختیار دارد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141261" target="_blank">📅 12:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141260">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141260" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141259">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭕️
تیوی‌بیفوما وینگر33ساله پرسپولیس با نمره 7.8 بهترین‌بازیکن‌دیدار امشب‌سرخ‌ها برابر نفت شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141259" target="_blank">📅 12:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141258">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvUKXCyz5HYkNHrRCPD7BNrgLYSEFowlNjlJZY2B7OBYnyy5X1anHz-85_8RPkMMXbI6OxR65gonFUi_HMUrlLjBEb3XvPTPmPa9ZL1nF9aqmWR1E9feFOk1yXJxVfoRODDEqsKAH_cdDvqbL_gAJIYiwsPpGZvhm2G0n2IVLqHcxn_91nFFPkNlDFbf5AcEXWDvPs_9acoLoSs_5dNIlAIJ2R8By9aVYLvq_n98m4u0pjNKYvxQnrsUTAYUnJH6erBA7qFdTe23E_28gq9B2DRouSiRAo2MbwvzIAiYaWa1it0hSC4aPX50Bm4IcSuSEKQdbJ3W_aZjv9AytzX5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
معوقه هفته‌هفتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
خیبر خرم‌آباد
🇮🇷
🗓
تاریخ چهارشنبه ۲۲ مهر
⏰
ساعت ۱۷
🏟
میزبان خرم‌آباد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141258" target="_blank">📅 12:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141257">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🔴
◀️
مجوز خارج شدن امتیاز باشگاه پادیاب خلخال از استان صادر نشده و باشگاه پرسپولیس برای خرید امتیاز این باشگاه با مانع روبرو شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/141257" target="_blank">📅 10:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141256">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/141256" target="_blank">📅 10:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141255">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/141255" target="_blank">📅 10:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141254">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a373367fda.mp4?token=VDrk9Hctj_0AwCOz304immXmSpvGk5Q8trIZBfGiHxSb9ukQsE6XHC7AEQyxGySHTdg-LmpeDtIqWZVGEGwrFdRjMUwhxgcjYZQJH104FP0vrHZBfWYJuAJe6qrk4yk1GUAqVNdATYdfOdiAPmNNsp5MzYSWjpGP-KMTRupTFIHQmblM2uiiGBcxLW6Q-GQcSOhOTBYJZShUic-Z0jbGwkWgYNvvHY2hUsCOnTcbT7TxEDOR427o3NOiihQwql7BNZj7699lTE5UCdgUc4Ze2gC5pmQsSpQoSbHT9Lk6PFkSnF5JcjdWLm8ZdDKokXynJXShMsxYaIZhZkEhUlwnOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a373367fda.mp4?token=VDrk9Hctj_0AwCOz304immXmSpvGk5Q8trIZBfGiHxSb9ukQsE6XHC7AEQyxGySHTdg-LmpeDtIqWZVGEGwrFdRjMUwhxgcjYZQJH104FP0vrHZBfWYJuAJe6qrk4yk1GUAqVNdATYdfOdiAPmNNsp5MzYSWjpGP-KMTRupTFIHQmblM2uiiGBcxLW6Q-GQcSOhOTBYJZShUic-Z0jbGwkWgYNvvHY2hUsCOnTcbT7TxEDOR427o3NOiihQwql7BNZj7699lTE5UCdgUc4Ze2gC5pmQsSpQoSbHT9Lk6PFkSnF5JcjdWLm8ZdDKokXynJXShMsxYaIZhZkEhUlwnOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آنالیز محمد تقوی از بازی پرسپولیس-صنعت‌نفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/141254" target="_blank">📅 10:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141253">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/141253" target="_blank">📅 09:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141252">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141252" target="_blank">📅 09:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141251">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
پویا اسمی که متولد 1 شهریور سال 1388 میباشد به جوان ترین بازیکن پرسپولیس در تاریخ لیگ برتر با 17 سال و 1 ماه و 16 روز سن تبدیل شد.
🛍
پیش از او این رکورد در اختیار احسان خرسندی مهاجم پرورش‌یافته آکادمی پرسپولیس بود که در 29 اردیبهشت 1381 در دیدار…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/141251" target="_blank">📅 09:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141250">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
فووووووری؛ سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکی‌اش حق خروج از کشور را ندارد و ممنوع الخروج شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/141250" target="_blank">📅 09:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141249">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❤️
❤️
❤️
صبحی که تیم برده و 16 امتیازی شدیم با یک بازی کمتر و تیمهای دیگه تو حاشیه هستند و پرسپولیس تو آرامش بخیر   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/141249" target="_blank">📅 08:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141248">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❤️
❤️
❤️
صبحی که تیم برده و 16 امتیازی شدیم با یک بازی کمتر و تیمهای دیگه تو حاشیه هستند و پرسپولیس تو آرامش بخیر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/141248" target="_blank">📅 08:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141247">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUYdqyJ2xDaVJ-AZzexYT8QQkLrxrpWRJ6zN2uUVkPo1Un98ySaybBtsKjg5oBdX0HZrC0pgjVu4zdFENgy2wBkfppK3QfNAWhOmo9sac5wEWrWJtPgekE0XX6Asy-GpHnhrLwJgc7D6rVuqeTdze1E1Fitc4DLX3AKvvcXQGDYIGV721rAsFs2-HwGt_aNr4IZKi7wC_VHlcM9rs6NbWUlRcDQienHT7exWmhQELHsMoMMeUT2_X_tu6ImZ5blYmosgu5qPUEWlmyLzY70ogtvbXxOHAjPEpBAHqpwta0uj3d0WHkTl5VELKajR56dn_IEjEmfoufuaoUvSXkI_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/141247" target="_blank">📅 01:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141246">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏅
صحبت‌های جنجالی احمد گوهری درباره دلیل جدایی از پیکان: سرمربی فصل گذشته پیکان به جادوگری اعتقاد دارد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/141246" target="_blank">📅 01:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141245">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏅
صحبت‌های جنجالی احمد گوهری درباره دلیل جدایی از پیکان: سرمربی فصل گذشته پیکان به جادوگری اعتقاد دارد!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/141245" target="_blank">📅 01:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141244">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
فووووووری؛ سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکی‌اش حق خروج از کشور را ندارد و ممنوع الخروج شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/141244" target="_blank">📅 23:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141243">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
#فوری/بیرانوند با دستور نظام وظیفه ممنوع الخروج است و امروز هم مجوز تمرین نداشته.
🚨
کریمی و نکونام می دانستند بیرانوند حق خروج ندارد و برای خوشایند زنوزی اخراجش کردند.
🚨
اکنون هم می خواهند سر هواداران را گرم کنند و به رسانه ها می گویند مشکل حل شده و به…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/141243" target="_blank">📅 23:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141242">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0aq2XIEHXvW7A5ZAUUU7UrU2FjVMgmk-Gxd-Zvd8etwFbJUKf-TrlPGVH6tERMJ10NQ5iLbXfqtD0v2DK1ZQolPatkFSc5ZCKkqnudDbrk_aqz7kqVb-kr9fMRY_N6ISbt0vPX01Yo0th7TWuG4s0KOwAYP5wYFkcqmzjz-L8MHRmswm02t76H7H37F78xr5AWZFwow-SGezrjqXqgXM2zFd31YV7MeBng39eIlLoo1so4VSq2cPeOT_VSmwlDTgzp6knbTIF0qQwHqzQQos_9JrJiwgoYRU_SbcLQgCM509mtvJkmCsvNZu6P1F7YvS605MsBncYvwKKaNm3AucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/141242" target="_blank">📅 23:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141241">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
‼️
🇮🇷
منفوری بیرانوند ادامه داره
🚨
فوری؛ بیرانوند از هتل هم  اخراج شد!  علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/141241" target="_blank">📅 23:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141240">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTgfQrSw6g-VOGsjQkDsskLqrvti9Agwqv8_rU6IeEk665Oo5tiP-5b7lyQ6YvgjmeFR9NNXVPofcQfBSRvMfvuHq-OylRYMsrJFtcuchahy4RdbTlXgN-APgkIVvV93gyOJgV4THQCjdte4IxpkbvA-CxbRd8wVaI40jlHlB_ysY-5cWGxjrvFDJpCRHCj-dSpbyEpBb9jjdjj5nSnMFUkCEajrWCGRZUUxczQk1N0Ta3GfFtbAdSvZSFGeoZG_nqp56cCPxh8-1jkj6WeqbQF5Va0Ifpq7uDr-1SOv7NaFDRCHUIpGqLIbWk95nOrkrQnSZ27HRfzf4AEPXnzQ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
❌
محمد نوری پس از شکست مقابل پرسپولیس به صورت توافقی از صنعت نفت آبادان جدا شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/141240" target="_blank">📅 23:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141239">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ce1b9f2c.mp4?token=SQXdLjKMQxZsyPRtWEAO_9F2SBUQJVzLQ4LvMBw-AFY8y_KXXlbCKjxZYB3MNEE3GCW6HqWaeJd1HF1tgHkTPTUWzPfHYWl_cGOOuSAa4bWV8eS2pdtAkSdygYW8RYf96Wz1wzJV4qUMJqGDOQvoUAVSp57Gv6NBPSvLtyAs6nVB0NuWqXNzLrj71W3i-l5vi0ToaC4qof47Fro8MUGisujGcLuKBYLORgel731Gk3Dt16ZmUHeyZLL5Z-5QQ6y-Lojpc_M_Wn8RtVFv0pv8GXsAsoLtErUVrOzsaFsBbigPHbCUKfL3Z5FAZIpJvnRuwHwBCuvLy0gxA8US5nVJoIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ce1b9f2c.mp4?token=SQXdLjKMQxZsyPRtWEAO_9F2SBUQJVzLQ4LvMBw-AFY8y_KXXlbCKjxZYB3MNEE3GCW6HqWaeJd1HF1tgHkTPTUWzPfHYWl_cGOOuSAa4bWV8eS2pdtAkSdygYW8RYf96Wz1wzJV4qUMJqGDOQvoUAVSp57Gv6NBPSvLtyAs6nVB0NuWqXNzLrj71W3i-l5vi0ToaC4qof47Fro8MUGisujGcLuKBYLORgel731Gk3Dt16ZmUHeyZLL5Z-5QQ6y-Lojpc_M_Wn8RtVFv0pv8GXsAsoLtErUVrOzsaFsBbigPHbCUKfL3Z5FAZIpJvnRuwHwBCuvLy0gxA8US5nVJoIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
⚪️
⚽️
تاج: با یحیی گل‌محمدی برای هدایت تیم ملی امید به توافقاتی رسیده‌ایم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/141239" target="_blank">📅 23:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141238">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
✅
تاج : آزادی تا 2028 باید مسقف بشه، وگرنه دیگه اجازه میزبانی نمیدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/141238" target="_blank">📅 23:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141237">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fbe6664d.mp4?token=hVyG69g5fF4P7itL5XPkXxXWxeKGxXG5MwZW6Pny_V9aGXfV4VAuesWefwHjBOVU9IwBQAqtZ4zcCwllO0b5FYb_vN0pWVH0R_JXF7AgKh6AtMh-lsgPuOdNKyd8PmnULuqCiozN3cDSGhNfxaEJ1CeKekf414du7B1ipI-wcGjF_DLw1OAd7Ni3amTQlS2t620rI7XUiZXmzSKfqDosa3OCNh28aTggf61zN8VFD8WOtYJOZEqosxTBuuaSFGDhdlD8JHgxZF2-_XhZb0JvIUEFxwhQOsqvLKONNYdmseLO5uu9UP6s8BXrn4P4beZk7j4JO4-4wBpeP4hsFPxjyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fbe6664d.mp4?token=hVyG69g5fF4P7itL5XPkXxXWxeKGxXG5MwZW6Pny_V9aGXfV4VAuesWefwHjBOVU9IwBQAqtZ4zcCwllO0b5FYb_vN0pWVH0R_JXF7AgKh6AtMh-lsgPuOdNKyd8PmnULuqCiozN3cDSGhNfxaEJ1CeKekf414du7B1ipI-wcGjF_DLw1OAd7Ni3amTQlS2t620rI7XUiZXmzSKfqDosa3OCNh28aTggf61zN8VFD8WOtYJOZEqosxTBuuaSFGDhdlD8JHgxZF2-_XhZb0JvIUEFxwhQOsqvLKONNYdmseLO5uu9UP6s8BXrn4P4beZk7j4JO4-4wBpeP4hsFPxjyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در اتفاقی غیرمنتظره پس از پایان دیدار با صنعت نفت، تعدادی از هواداران پرسپولیس با قرار دادن موانعی از جمله لاستیک خودرو در مسیر اتوبوس این تیم، مانع از حرکت آن شدند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/141237" target="_blank">📅 23:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141236">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYtVT9bpgAD7Hzf7-8Tx1OPma73YVr7iv3y-r76taxgTH6FACDBJGLeYotuB3WS9L2yYTTHPDo6UwZpsuec-8nfxyj9izqX8nGISxR8to5H-3dsNzd6wFXQ-3dsoPfVnGpmnaglgj-Fc6ajQm9dSgeqW0R_UBrAeyWo987NTDHZSfiIgmHHLnaczQCMLoJ3l3I3wQYrRPdXQwtRb1uoCB9kMB7qVKV6uj3EdNsyh6D2zve2GYbgqbhe2FZiQlhkrFOLRh59EXrx8OO3rvt5pcGDrWR5lXdZDJ4Uq9RbRTezVIj3lZhGarpp6A4jWUMiC5tRE_uy3rAtDweXtG6-12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
منفوری بیرانوند ادامه داره
🚨
فوری؛ بیرانوند از هتل هم  اخراج شد!
علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/141236" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141235">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37a5e6308.mp4?token=tOrTV34qnSZfR8pfxLe7ytCpUnXDvtWYFONSKk7BWaushrcM7H3kw1XdC8eeNAwhRXLp4wZPlihh4RX8l2F6i6sMORorJDADpAnCBbmQ2LfNfgr66juT3pBMU5z6wbv-LiU2ohXOtHLsmZk1yhdfTq8scB9Y4oR7ctZLsTBOZ3C3S7914NVFPf5ajeYsVZV3pdChwUxQcXVRZy7_ddTy-gDEriOYRsTkgiHANngpUmbE6obWQlSxiWUgUzXo_9-9ZtNBQ4Fv3FI67-mMhZE0YY4XOUlM1Bc2Cm547zYyezdFwYPEGeAwkWbgyMt8UNjVnjqgRM_BtiW2NIsqy_FsPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37a5e6308.mp4?token=tOrTV34qnSZfR8pfxLe7ytCpUnXDvtWYFONSKk7BWaushrcM7H3kw1XdC8eeNAwhRXLp4wZPlihh4RX8l2F6i6sMORorJDADpAnCBbmQ2LfNfgr66juT3pBMU5z6wbv-LiU2ohXOtHLsmZk1yhdfTq8scB9Y4oR7ctZLsTBOZ3C3S7914NVFPf5ajeYsVZV3pdChwUxQcXVRZy7_ddTy-gDEriOYRsTkgiHANngpUmbE6obWQlSxiWUgUzXo_9-9ZtNBQ4Fv3FI67-mMhZE0YY4XOUlM1Bc2Cm547zYyezdFwYPEGeAwkWbgyMt8UNjVnjqgRM_BtiW2NIsqy_FsPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
❤️
فووووووووری ؛ بیرانوند رفته هتل محل اردوی بازیکنان تراکتور ولی توسط نگهبان هتل راه ندادنش و گفتند سیکتیر
😂
😂
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/141235" target="_blank">📅 22:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141234">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc26b95b5.mp4?token=RGxtmF--OVRFaPaQ2lP9ZRJqDYBw9yuSB_4Y8VtV0SjNUWDW3Zk1khiwWqwfJ03S5NrcEYfYP-E0qkcPuAbf52W_kOIzJ4HGZFx1j4UIflARVWGz3r0NComuSzl7mfVJ3PsL9Ahwo_BnHon_3Q9T3-XbmLKb3SY-Nm5UJnoOCfjdoTAAwfGEX1sWkHcmbdBJVgSbFnn1aEPHKTU4IKaFfQailKkBepjcGlA7j8R5mRcJ_DqCCtP3RvqGoB8vmkHMZOpyqiUIQy9fQHjqD1v1zk4RNU2g8ugZIRZqqiPuLAzFr_6QltimWFpA2YIWj7iB99KqCfAJgOyQK9VKLaQw-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc26b95b5.mp4?token=RGxtmF--OVRFaPaQ2lP9ZRJqDYBw9yuSB_4Y8VtV0SjNUWDW3Zk1khiwWqwfJ03S5NrcEYfYP-E0qkcPuAbf52W_kOIzJ4HGZFx1j4UIflARVWGz3r0NComuSzl7mfVJ3PsL9Ahwo_BnHon_3Q9T3-XbmLKb3SY-Nm5UJnoOCfjdoTAAwfGEX1sWkHcmbdBJVgSbFnn1aEPHKTU4IKaFfQailKkBepjcGlA7j8R5mRcJ_DqCCtP3RvqGoB8vmkHMZOpyqiUIQy9fQHjqD1v1zk4RNU2g8ugZIRZqqiPuLAzFr_6QltimWFpA2YIWj7iB99KqCfAJgOyQK9VKLaQw-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اتوبوس تیم ابوالفضل جلالیو جا گذاشته تو ورزشگاه
😐
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/141234" target="_blank">📅 22:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141233">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
#فوری | شنیده شدن صدای چندین انفجار در شرق بندرعباس و اطراف قشم منشا صدا مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/141233" target="_blank">📅 21:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141232">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
❌
یاسر آسانی؟ باشگاه تمام مسائل را از صفر تا صد پیگیری می کند. داخل کشور به نتیجه نرسیم صددرصد در دادگاه عالی ورزش دنبال می کنیم. ما نگفتیم این پرونده پایان یافته است. مندیت آسانی به پرسپولیس؟ بله او مندیت را داشت اما زمان همه چیز را در این زمینه نشان می دهد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/141232" target="_blank">📅 21:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141231">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
تارتار:
🔴
به خاطر گلی که خوردیم و موقعیت‌هایی که از دست دادیم ناراحتم
🔴
از شادی هواداران پرسپولیس خوشحالم؛ آنها همیشه باید خوشحال باشند
🔴
همه بازیکنان از کیفیت چمن استادیوم شهر قدس گلایه داشتند
🔴
از مسئولین کشور می‌خواهم ورزشگاه آزادی را هرچه زودتر آماده…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/141231" target="_blank">📅 20:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141230">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7Ihd50ZTe7wFPGifVF5HDcded7PYdxG9rpd2iLhG7-goklYR8aHNVv5r86J5hG5HDsnoNas8CbcG31DZWYQSDiKFLdnK7n-7zW5jpnRpXMRPJyQWztPgpajtZms_hhZ5iKPi7B7tFJX6lenc_AafiXPCxSo8pxGQsStV6Gqb5R2J6gWHtJexxU-XnPKIwMbNh1jcSTKsV2WLz9kHKs4cUQF0FlhLHtu_FWFUUUY0vp4H_vcoAJQJHrB0mfX6UlDY_QqhL3EaZdSuPu0XcI3zDcod30TZYlIwswtowYXa90AR8HeDXI4Pfue-hg-wOkvNFIfTmdmZKwdqUZyGzjOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرخپوشان پس از کسب پیروزی، جشن خود را با هواداران تقسیم کردند
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/141230" target="_blank">📅 20:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141229">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR2oxNcED5UN5AXoilmfWztGH3DiikiVsZ2vt8bdZ2RrJ4vCt14yyRyVaJBXBT5FQdZD_ceP_hHvJT1S_cdC2MNE9RMmuARR6fMbGCHMntVEGyaEDV8FhiyBTnJrWMIqzBb1CXezWShJKkl1esuAENpMdz-RsrWjiHMMlivs6hPSgTYynGZ1vPGGWtU_RkP83A2K4JfFScWHqEFXrWrcwyhQhw_hvSC991WJiRHO7_e5F7R_3Jju3kcmC4qMPvzB9fNnM8wZ_EWQIKzeuH1QSmXZiGhw-c7Mcan6OfCgS7AztOIfbFo6vnqu4TsGtWGUnnilM2lqPYUxFtg0N6-JOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
زنبورها در کمین سه امتیاز؛ وردربرمن آماده شوک در خانه دورتموند!
🔥
⚡️
[
دورتموند
🟡
🆚
🟢
وردربرمن
]
⚽️
دورتموند با ۱۲ امتیاز و آمار ۹ گل زده و تنها ۲ گل خورده در ۴ هفته، برتری آماری محسوسی نسبت به وردربرمن دارد که ۸ گل زده و ۸ گل دریافت کرده است. دورتموند در ۷ تقابل اخیر مقابل برمن شکست نخورده و با توجه به فرم هجومی میزبان، شانس بیشتری برای تسلط بر بازی دارد.
سناریوی محتمل: برد دورتموند؛ هرچند برمن با توجه به قدرت گل‌زنی‌اش می‌تواند برای خط دفاع دورتموند دردسرساز شود.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/141229" target="_blank">📅 20:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141228">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/141228" target="_blank">📅 20:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141227">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎤
🔴
علی بازگشا: اسناد کامل و جدیدی درباره پرونده آسانی به کمیته استیناف ارسال کردیم
🔹
امیدوارم این پرونده در داخل کشور حل شود/ اقدامات قانونی را در داخل کشور انجام دادیم و اسناد جدیدی خدمت کمیته استیناف ارسال کردیم/ امیدواریم این اسناد جدید و مهم که تا به حال به این ارکان ارجاع داده نشده موثر باشد و رای جدیدی دهند/ تمام تلاشمان این است که موضوع در داخل کشور حل شود چون احترام به ارکان قضایی کشور است/ نامه‌ای را روز گذشته به فدراسیون ارسال کردیم و ادله ما شفاف است/ چیزی که از فدراسیون می‌خواهیم اجرای قانون است نه مصلحت اندیشی/ قانون منع مصلحت نیست/ تاثیرگذاری یک بازیکن غیرمجاز می تواند نظم جدول را برهم بزند و به بقیه تیم‌ها ظلم‌ شود/ پاسخگوی هوادار و سهامدار باشگاه هستیم/ ما مندیت آسانی را در آن تاریخ دریافت کردیم/ باید رای قاطع و جذاب صادر شود/ کسی تماسی نگرفته که این موضوع پیگیری نشود/ اسناد مختلف از جاهای مختلف رسیده است/ اگر نتیجه دربی به نفع ما شود دیگر طبیعتا در کاس پیگیری نمی‌کنیم ولی ما درباره این موضوع صحبتی نکرده ایم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/141227" target="_blank">📅 20:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141226">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
پیام نیازمند: بازیای بعد فیفادی همیشه سخته/ تا جام ملت‌ها خیلی مونده و تمام تمرکزم روی موفقیت پرسپولیسه/ کاپیتانی پرسپولیس برام افتخاره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/141226" target="_blank">📅 20:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141225">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
✅
پیام نیازمند برای اولین بار در طی حضورش در پرسپولیس به عنوان کاپیتان کارش را آغاز خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/141225" target="_blank">📅 20:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141224">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/141224" target="_blank">📅 19:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141223">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKAASPhaHfSZ1PysfHGWkbQtEEIHbmEbGa04TKjoGnxcQcP5dIQg6TMnKYaW6PWV4hIMJwvL2YeoRSb5OaPIOrTE8NckhZpJm1HAU3PqkusZwp7H66gPpDPvk3Yhy9upccUjaQRUZrRz8yfVp9yUUnHy-aU1iWAcB0TpJCPP9kAwyjZkdBtv3Trtx5qwiOhGDzDMjIdzIrvG2x5INJxDYxIqabmySnmuPmHev4Igqux5GCExxoaQP3xlDWMZwZAxgUr7ZNhTB02jyDnSKoRpi8P1TxSid08kUGicZ5tid-sFzoIr3n7tcHdQmcuA5lnOXBCoYOQwKy9_69HTtVJ20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
جدول لیگ‌برتر پس از بازی‌های امروز
🚨
پرسپولیس با برد مقابل خیبر در بازی معوقه، به صدر جدول میره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/141223" target="_blank">📅 19:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141222">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
چشم نوازترین پرسپولیس چند سال اخیر و میبینیم ..نیمه اول و با یک گل بردیم ...تو نیمه ای که سه چهار گل و نزدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/141222" target="_blank">📅 19:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141221">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس 3 - نفت آبادان 1  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/141221" target="_blank">📅 19:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141220">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74657a541.mp4?token=uWwYm4UYTStPny6fMX4WQkGV49XnRwaZlBEYIdXrcVog6fPcoIFweuBpKaLXCaZLQTUjsmJj2aeiFHFBP7jELA8M7z-Hvp1jAVALF9m--FruVKZ4Hs9TItJiuhKTUtr5iBhTF7nw8xoP0t09EO9rfHvv46f4egVPTKI15wEhO8vtGhL9mweEO9w-1phwiALRYwmRo_zMERBl_mCeZuqRvqBnk0MKxqpLuTKGjPZct8WKiHIJ6nEU2tfAF_fxW4kL6ZxQOnWtZpsQJSATPa6UoA8PwzKtan2Ua58oXsWOPl-By2yy2dRTUlNQr3PijTPDpuNgUVYc9Gfo0mFfQkUj3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74657a541.mp4?token=uWwYm4UYTStPny6fMX4WQkGV49XnRwaZlBEYIdXrcVog6fPcoIFweuBpKaLXCaZLQTUjsmJj2aeiFHFBP7jELA8M7z-Hvp1jAVALF9m--FruVKZ4Hs9TItJiuhKTUtr5iBhTF7nw8xoP0t09EO9rfHvv46f4egVPTKI15wEhO8vtGhL9mweEO9w-1phwiALRYwmRo_zMERBl_mCeZuqRvqBnk0MKxqpLuTKGjPZct8WKiHIJ6nEU2tfAF_fxW4kL6ZxQOnWtZpsQJSATPa6UoA8PwzKtan2Ua58oXsWOPl-By2yy2dRTUlNQr3PijTPDpuNgUVYc9Gfo0mFfQkUj3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
شادی ایسلندی بازیکنان پرسپولیس در کنار هواداران در ورزشگاه⠀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/141220" target="_blank">📅 19:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141219">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس 3 - نفت آبادان 1
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/141219" target="_blank">📅 19:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141218">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/141218" target="_blank">📅 19:02 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
