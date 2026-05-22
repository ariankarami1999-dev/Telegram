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
<img src="https://cdn4.telesco.pe/file/sJ1YRfUfbWtiRedatt0OVYTMRUI1635jzjRv5NdyhTYXSG-TIDTyoc71KAmbEVjcllNzNpVU4wzFKGAh1dNDVetf7LWQcXz9KDxSOAgq9NdToRsUn_zGS1RoxaQmuOgPUY3--xNwpPmLICe-7uejXLylv6rIAd98p-gcISJAbnupT0kOEzhkVRX01WrHg7j5HB6viue8w8VeUS_swg0dptDu1IPcrAtiO6SO498-IalU6NgxMsYo3UjnGlPDmXIIiZRDKBy_0oAWNn-ibfUZHjxT4D6ukZJI5B_jxDC1Gxun0j6x6lpvk6FHjQ_fgddEcukA86bTU6alC2Lt2F3MFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 00:22:47</div>
<hr>

<div class="tg-post" id="msg-132046">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🟥
خبرنگار الجزیره در تهران: به نظر می‌رسد فضای مذاکرات ایران و آمریکا تا این لحظه مثبت است و پیشرفت ملموسی در حل برخی اختلافات از طریق میانجیگر پاکستانی حاصل شده است
🔸
آمدن فرمانده ارتش پاکستان به تهران ممکن است دو هدف داشته باشد: حل اختلافات باقی‌مانده یا…</div>
<div class="tg-footer">👁️ 94 · <a href="https://t.me/SorkhTimes/132046" target="_blank">📅 00:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132045">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
نت بلاکس: قطعی اینترنت در ایران از مرز 240 ساعت گذشت  @SorkhTimes</div>
<div class="tg-footer">👁️ 123 · <a href="https://t.me/SorkhTimes/132045" target="_blank">📅 00:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132044">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
اوستن اورنوف شب گذشته بدون مشکل در تمرین تیم ملی ازبکستان شرکت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 183 · <a href="https://t.me/SorkhTimes/132044" target="_blank">📅 00:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132043">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
گفته میشه که پرسپولیس به عنوان نماینده ایران در لیگ آسیا 2 شرکت خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 426 · <a href="https://t.me/SorkhTimes/132043" target="_blank">📅 23:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132042">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
گفته میشه که پرسپولیس به عنوان نماینده ایران در لیگ آسیا 2 شرکت خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 415 · <a href="https://t.me/SorkhTimes/132042" target="_blank">📅 23:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132041">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
زمزمه هایی شنیده می‌شود که امیر قلعه‌نویی پس از جام جهانی از تیم ملی جدا خواهد شد و یحیی گل‌محمدی گزینه اصلی جانشینی او است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 409 · <a href="https://t.me/SorkhTimes/132041" target="_blank">📅 23:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132040">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔰
سرویس VIP تک کاربره
🔰
1 گیگ 190 2 گیگ 380 3 گیگ 570 5 گیگ 950 10 گیگ 1900
🛜
مناسب برای تمام سایت ها اپ ها   جهت خرید از پیوی =>  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 473 · <a href="https://t.me/SorkhTimes/132040" target="_blank">📅 23:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132038">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
ترامپ: با اینکه خیلی میخواهم در کنار پسرم برای مراسم عروسی باشم اما حس میکنم که مهم تر است در واشنگتن و کاخ سفید در طی زمان مهم پیش رو در روز شنبه و یکشنبه بمانم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/SorkhTimes/132038" target="_blank">📅 22:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132037">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔖
🔴
فرهیختگان: طبق شنیده‌های ما پرسپولیس به AFC برای سهمیه سوم معرفی خواهد شد
✅
باتوجه به تجربه بین‌المللی باشگاه‌ها، رنکینگ آنها در AFC و باشگاه‌های جهان، شرایط مالی باشگاه‌ها و... در چنین شرایطی و ناتمام ماندن لیگ، اوضاع پرسپولیس به مراتب بهتر از دو تیم بالای…</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/SorkhTimes/132037" target="_blank">📅 22:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132035">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔰
سرویس VIP تک کاربره
🔰
1 گیگ 190
2 گیگ 380
3 گیگ 570
5 گیگ 950
10 گیگ 1900
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 797 · <a href="https://t.me/SorkhTimes/132035" target="_blank">📅 22:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132034">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
ترامپ: با اینکه خیلی میخواهم در کنار پسرم برای مراسم عروسی باشم اما حس میکنم که مهم تر است در واشنگتن و کاخ سفید در طی زمان مهم پیش رو در روز شنبه و یکشنبه بمانم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 760 · <a href="https://t.me/SorkhTimes/132034" target="_blank">📅 22:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132033">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8mQlkbhvCEkHuwxdwamQtFUNcQBUv_YaHr-Boiw6tokBTUBSX3eYuDEA9IF1j_ScrKk_vJxjPgcjMqohknszOIbABaDlO6Q8udwfjDxnQRHTJlurZwwMVXMJB71DwsvYWtzowB_n8zbRXEjsOaZUJYjsOD1vXosM25T3_swmN-yZTTEQaHkgkWrMyrakcGBueICsxfAfMTg9ckLomiUQ5GFyUki6k3OCp602Fz6EjaF4GCm8OrOzs7MdSNtdyddgFs7uATSNAOBYkWJaMGgQbroysJPt3m6SgrHXttKUtgiGjp4L57I7u1oL0xRf9fT6yEDB6gXLYZwCcaICIk0mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ: با اینکه خیلی میخواهم در کنار پسرم برای مراسم عروسی باشم اما حس میکنم که مهم تر است در واشنگتن و کاخ سفید در طی زمان مهم پیش رو در روز شنبه و یکشنبه بمانم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 712 · <a href="https://t.me/SorkhTimes/132033" target="_blank">📅 21:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132032">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
فوری؛ محمد خلیفه گلر ملی پوش آلومینیوم اراک و سابق پرسپولیس به استقلال پیوست/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 677 · <a href="https://t.me/SorkhTimes/132032" target="_blank">📅 21:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132031">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
شایعات: ویزا شجاع خلیل زاده، مهدی طارمی و احسان حاج‌صفی بخاطر خدمت تو سپاه پاسداران صادر نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 689 · <a href="https://t.me/SorkhTimes/132031" target="_blank">📅 21:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132030">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdYMIeZVV2N8RNGlF-prTLyRuRy9kbQMS0yR_hUlb6ZE_rJ2EJlHmDib1dbuelgXaGPoWNH91Bwo8dmKEiGlpSL41dz_mwv__aJjpAeA4hIGWhn293iSAz1_HEGQ011zGoJm-ufKVkbkEwyjaM0xF6dW-2-zFrH_irvod29DOBFTPsQShIttB-N2zB_xqj8OYOsNegarPHJ1yBCzEkAX2OsaG3Q5KdVcZwuvqpdxo8inQwyVIQcj6gbyHmil1A6KPJD3bQU8qGjxwEpFEZGM0jZFQLgO_yYg9cHmGLfmqE5barhvWZjeFNcjPZLozGWCdA5vA4aKgHSN5Q_X4fs_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فارس: باشگاه پرسپولیس قصد تمدید قرارداد میلاد محمدی را ندارد و به احتمال زیاد از جمع سرخپوشان جدا شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 755 · <a href="https://t.me/SorkhTimes/132030" target="_blank">📅 21:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132029">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
پیشنهاد رسمی باشگاه پرسپولیس به رئیس سازمان لیگ: حالا که‌مجوز حرفه‌ای باشگاه سپاهان صادر نشه استقلال و تراکتور رو به لیگ نخبگان آسیا بفرستید و ما رو هم به سطح دو لیگ قهرمانان آسیا.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 772 · <a href="https://t.me/SorkhTimes/132029" target="_blank">📅 21:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132026">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
شجاع خلیل‌زاده، با ۳۷ سال سن، پیرترین بازیکن تاریخ ایران در کل ادوار جام جهانی فوتبال خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 970 · <a href="https://t.me/SorkhTimes/132026" target="_blank">📅 19:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132025">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
باشگاه گل‌گهر از چادرملو بابت استفاده از آندرس، بازیکن پارگوئه ای شکایت کرده و خواهان 3 بر 0 شدن مسابقه این تیم برابر چادرملو شده است؛ در صورتی که چادرملو در این پرونده محکوم شود، جایگاه چهارمی خود را از دست داده و به رده ششم جدول سقوط خواهد کرد و پرسپولیس…</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/132025" target="_blank">📅 19:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132024">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/SorkhTimes/132024" target="_blank">📅 19:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132023">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
مجوز حرفه ای سپاهان صادر نشد و ممکنه یه تیم از بین پرسپولیس و گلگهر بره اسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/SorkhTimes/132023" target="_blank">📅 19:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132022">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
شرزود تمیروف مهاجم سابق پرسپولیس با ۲۸ گل در ۳۲ بازی، آقای گل لیگ عراق شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/SorkhTimes/132022" target="_blank">📅 19:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132020">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری | رویترز:
🔻
منابع مطلع گزارش دادند که قطر تیمی مذاکره‌کننده به تهران فرستاده است، با هماهنگی ایالات متحده، برای کمک به رسیدن به توافقی برای پایان دادن به جنگ با ایران
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/SorkhTimes/132020" target="_blank">📅 19:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132019">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🟥
🟥
🚨
باراک راوید، خبرنگار آکسیوس:  عاصم منیر فرمانده ارتش پاکستان
🇵🇰
، امروز برای بستن توافق بین آمریکا و ایران و تموم کردنِ جنگ، راهی تهران میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/132019" target="_blank">📅 17:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132018">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
#تکمیلی | العربیه : پیش‌نویس نهایی توافق مورد انتظار بین آمریکا و ایران که طی ساعات آینده برای توقف جنگ در همه جبهه‌ها تنظیم می‌شود:
🔴
۱. توقف کامل، فوری و بی‌قیدوشرط آتش‌بس در همه جبهه‌ها (زمینی، دریایی و هوایی).
🔴
۲. تعهد دو طرف به عدم هدف‌گیری هرگونه…</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/132018" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132017">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
مجوز حرفه ای سپاهان صادر نشد و ممکنه یه تیم از بین پرسپولیس و گلگهر بره اسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/132017" target="_blank">📅 17:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132016">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
عضو کمیسیون فرهنگی مجلس : طرح جایزه کشتن ترامپ، تو مجلس تصویب میشه
😐
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/132016" target="_blank">📅 15:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132015">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEcz9kNMoYyHmeclVBQBUa3QFhK5YrnOlHxWG-GS808xXl4xkX5b2NdEoEB-ody6zN6fkJTIppqIdL48WsJsdaR3lf-c9QMOoxLkmVdBb0YRvn2RkPw6AmWa44-2Pfp1NEr0dfbq7sOoBFtFK1Wfk8rPFHV-wB_OtcdNs0BIzbp2qvsKHZDvZh-ieKnZVbxbClaVYGDRnfbI2cW57UEf66KSns0YLL3MR1579PDLN6-csj-5kof3d5bvwN3F0PQhsdfuJFKETz52LOFP90HS3LU69TYIw80oGd0txvtjfl-cnG8J1HFgCk5p97wChaVPqLpY_CJ1VtMug6vbdSUveA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
هنوز دنبال روش ورود به سایت می‌گردی؟
📌
کاربران حرفه‌ای دیگه وقتشون رو هدر نمیدن.
✌️
✅
سریع‌ترین راه ورود به وینکوبت فقط از طریق ربات رسمی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡️
بدون نیاز به جستجو
⚡️
بدون لینک‌های فیک و اشتباه
⚡️
ورود مستقیم و راحت
🔗
فقط یک کلیک تا ورود کامل به سایت وینکوبت:
👇
🤖
@Wincobet_bot
کانال رسمی سایت وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/132015" target="_blank">📅 15:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132014">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
پیشنهاد رسمی باشگاه پرسپولیس به رئیس سازمان لیگ:
حالا که‌مجوز حرفه‌ای باشگاه سپاهان صادر نشه استقلال و تراکتور رو به لیگ نخبگان آسیا بفرستید و ما رو هم به سطح دو لیگ قهرمانان آسیا.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/132014" target="_blank">📅 15:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132013">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس :
🔴
مسئولین دل‌سوز کشور به این نتیجه رسیدن که وصل کردن اینترنت به صلاح همه‌ی مردم نیست و فعلا قرار نیست اینترنت بین‌المللی رو برگردونیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/132013" target="_blank">📅 14:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132011">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
مدیرعامل باشگاه سپاهان: نامه‌ای به دست ما رسیده و در آن چنین نگاشته شده که برای سپاهان مجوز حرفه‌ای صادر نخواهد شد، اما برای رقبا مجوز صادر شده است!
🔴
عدم صدور مجوز حرفه‌ای برای سپاهان می‌تواند جوک سال فوتبال ایران و حتی آسیا باشد. ما شانس بیشتری برای قهرمانی…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/132011" target="_blank">📅 12:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132010">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
باشگاه سپاهان با انتشار اطلاعیه‌ای با کنایه فراوان به سایر تیم‌ها، عدم صدور مجوز حرفه‌ای خود را تایید کرد و بدین‌ترتیب باید شاهد تیم جایگزین برای طلایی‌پوشان در آسیا باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/132010" target="_blank">📅 12:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132009">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
سپاهان بگا رفت و مجوز حرفه ای نگرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/132009" target="_blank">📅 12:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132008">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
با اعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/132008" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132007">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXF8Y01ouhE6GK_MvXPkdv0ouB5uSZDNJkKOyzO_GF_3XLfR0GOVN9rW68b5reG4zA1hpY-XsDPX2RY0T4a0EPa6tL9A1myxyxlqcQFE5F82k3bB-rpJGoiSnhrEtS15f-eoMRb__ClCWKWFryUurgDMFS8DDKZ5IrwZIMOjgwr99bUIaQUEWP6y-WhLpGeQ8XUqM9J6x2sesEieAmkAo510iWzAQSjklB8AKYK3iVIPWxYv05kmdMgyWjTNi6ptK894QYKjieqmSTSWDBSlemnAZbT_rAKKpG07UaUzy94mRkReglnBHz_GHLb8RsLBzTsnPmKUWb8RElzzD8KrxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس :
🔴
مسئولین دل‌سوز کشور به این نتیجه رسیدن که
وصل کردن اینترنت به صلاح همه‌ی مردم نیست
و فعلا قرار نیست اینترنت بین‌المللی رو برگردونیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132007" target="_blank">📅 10:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132006">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeGr5Qv8bMGPj96mB6zcjo3LPMBX4NQlhtLJ-Izu0Jg7LniHJosQLcQJ082q_GOEUGPzJ7TJqWh60DRRn_K0QZnF-9JPlepftHm064BTu-4pjq_IShWf1J-WlPs6DqeionQ2cj1BJLN5qBy794Pq3Y3Trq_Vqfnew2tAMl2ce8IqT7htshW1s3cXSG9mgXqmue4Q0WdZPeWpcVgSFWB1UbdXxcSng4oA3fp_Jw91f5C-UYLlLwPPvbMUNJjNCMVSK0dCm14bvY6XtWqvLbIup8EH44CI28z7k7gaUtmMNmtFEsGxxse-28d_Tsu_Tr9CQO7Ok39iiWX-J0t9Na-Fbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونالدو بعد از 3 سال و از دست دادن 14 جاممممم بالاخره با قهرمانی تو لیگ عربستان اولین جام خودش رو با النصر به دست آورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/132006" target="_blank">📅 10:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132005">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
اورونوف: با پرسپولیس قرارداد دارم و فصل آینده در این تیم خواهم ماند، میخواهم با پرسپولیس قهرمان لیگ و آسیا شوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/132005" target="_blank">📅 10:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132004">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
امیر قلعه نویی و امضای پیراهن تیم ملی با جمله تقدیم به ابر ملت جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/132004" target="_blank">📅 10:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132002">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">- همه اون لحظه‌ای که سایت نصفه لود میشه و VPN قاطی میکنه رو تجربه کردیم، مخصوصاً وقتی وسط بازی یا ثبت پیش‌بینی باشی.
😑
- ربات رسمی تلگرام وینکوبت کارو راحت و ورود به سایت رو آسون کرده:
👇
-
🤖
@Wincobet_bot
-
🤖
@Wincobet_bot
- برای کسایی که بیشتر وقتشون توی تلگرامه، خیلی کاربردیه.</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132002" target="_blank">📅 01:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132001">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
ورزش سه: روزبه چشمی از ناحیه رباط صلیبی مصدوم شد و جام جهانی رو از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132001" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132000">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLNTT-bQkZ7U8aReknu7xBQU8Ca-8jnJIDh4NHD4jSMt8bB-LqDJKYB2ja3yXcoykHUPCLaso8mIYc57gU7MKQuZT1VgSGlVHrPz-FSnCleItJT45PRmOlz5OGPDGvIZr93EzHsm_7CRfGTeQZ15uZJWLQ6iAVEgf3bVUWBoej4KWBEdcRubqhYSaxUpz1UYCRaeg0l_fdT6QhOwXLy7WMCEjkqOiW2UYYYQownCeebJ9VHbkw6IG29PJ5l-yQzOGsG1Z02g1_92WtbtciFobbAcXkaPytv9Ks1m3f48t4bawdTYz-BulJFf2pzJK3f1lbVusnK4XhC6xvJ7FZs1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇵🇹
رونالدو به اولین بازیکن تاریخ فوتبال تبدیل شد که در 4 لیگ مختلف قهرمان شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132000" target="_blank">📅 00:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-131999">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا شوکتی</strong></div>
<div class="tg-text">درست میگه دیگه
زمانیکه یه عده داشتن از امثال سروش رفیعی حمایت میکردن و داشت پدر امتیازات تیمو در می‌آورد، بایستی فکر همچین روزی رو میکردیم</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131999" target="_blank">📅 23:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131998">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
‼️
مجوز حرفه ای باشگاه صادر شده ولی خبری از شرکت تو مسابقات آسیایی نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/131998" target="_blank">📅 22:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131997">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/131997" target="_blank">📅 22:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131996">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WwIJejI2aBunHZmm0m4luTqElCXgGItWw-Fe2_1jIOs9bqxqsLSmWGIApoiaqkSh0uiOMiGVBaCbzRKIpr8tujs-oXpG0eJBabFbFeB0pvJhdFngRdCfDAu7IQr-6q9BtOZoceezZTgO8Pe1W0JIfOQBTzufUDdfdzp4SuDp9ZkQUZoJz-fIO46fZFlfVa1LIy4ScM_GTJ2G9-pHhTfIYoeaV2pQpUnPzWS_iiMLjIkqSsuvJp7fUQJdMrL2Qnqk6vQnlXDmMEzdxtTXiGs2C8hfA7N7Vdxj-WfK69GjtpPg1K9FVkH3xt0z2j6DLvFUw5cn4oi00lb-Hg4p3LFSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی
| العربیه : پیش‌نویس نهایی توافق مورد انتظار بین آمریکا و ایران که طی ساعات آینده برای توقف جنگ در همه جبهه‌ها تنظیم می‌شود:
🔴
۱. توقف کامل، فوری و بی‌قیدوشرط آتش‌بس در همه جبهه‌ها (زمینی، دریایی و هوایی).
🔴
۲. تعهد دو طرف به عدم هدف‌گیری هرگونه تأسیسات نظامی، غیرنظامی یا اقتصادی طرف دیگر.
🔴
۳. توقف کلیه عملیات نظامی، فعالیت‌ها و جنگ تحریک‌آمیز رسانه‌ای.
🔴
۴. احترام به حاکمیت کشورها، تمامیت ارضی آنها و عدم دخالت در امور داخلی.
🔴
۵. تضمین آزادی دریانوردی در خلیج فارس، تنگه هرمز و دریای عمان.
🔴
۶. تشکیل کمیته مشترک برای نظارت بر اجرای توافق و حل و فصل اختلافات.
🔴
۷. آغاز مذاکرات درباره موضوعات حل‌نشده حداکثر ظرف مدت ۷ روز.
🔴
۸. لغو تدریجی تحریم‌های آمریکا علیه ایران در مقابل پایبندی ایران به مفاد توافق.
🔴
۹. دو طرف تأکید می‌کنند که این توافق در چارچوب احترام به حقوق بین‌الملل و منشور ملل متحد است.
🔴
این توافق از لحظه اعلام رسمی آن توسط دو طرف، لازم‌الاجرا خواهد بود
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/131996" target="_blank">📅 22:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131995">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
ورزش سه: روزبه چشمی از ناحیه رباط صلیبی مصدوم شد و جام جهانی رو از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131995" target="_blank">📅 22:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131994">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوتبالی: علیپور مذاکرات مثبتی با حدادی داشته و از لحاظ مالی توافق کرده و اگه اتفاق خاصی نیوفته بعد جام جهانی تمدید میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/131994" target="_blank">📅 22:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131992">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
وکیل بیرانوند میگه پرسپولیس پولی برای رسیدگی به پرونده(هزینه‌ی دادرسی)پرداخت نکرده و ادعای باشگاه کذبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/131992" target="_blank">📅 19:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131990">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔽
صدور مجوز حرفه‌ای باشگاه  پرسپولیس با ابلاغ رسمی دبیرکل فدراسیون فوتبال
🔴
رسانه رسمی پرسپولیس:
❤️
با دریافت نامه‌ای از سوی دبیرکل فدراسیون فوتبال، مجوز حرفه‌ای باشگاه پرسپولیس برای فصل پیش رو صادر و به طور رسمی ابلاغ شد.
🔽
این مجوز که بر اساس مدارک ارائه…</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/131990" target="_blank">📅 19:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131989">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
آسوشیتدپرس: عراقچی، وزیر خارجه ایران و قالیباف دیگه به هیچ عنوان مذاکرات رو در داخل ایران پیش نمی‌برن و کنترل کل ماجرا دست سپاه پاسدارانه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/131989" target="_blank">📅 19:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131987">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
رد درخواست خروج اورانیوم غنی‌شده از ایران
🖍
طبق گزارش دو مقام ارشد ایرانی به رویترز: ایران اصلی ترین خواسته آمریکا برای توافق که انتقال اورانیوم ۶۰ درصد است را به صورت کامل رد کرده است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/131987" target="_blank">📅 18:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131986">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔽
صدور مجوز حرفه‌ای باشگاه  پرسپولیس با ابلاغ رسمی دبیرکل فدراسیون فوتبال
🔴
رسانه رسمی پرسپولیس:
❤️
با دریافت نامه‌ای از سوی دبیرکل فدراسیون فوتبال، مجوز حرفه‌ای باشگاه پرسپولیس برای فصل پیش رو صادر و به طور رسمی ابلاغ شد.
🔽
این مجوز که بر اساس مدارک ارائه…</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/131986" target="_blank">📅 18:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131984">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgkdXrHl2jirs-rxtOHd_qs9aE0Y6Bqhe_5qPm5OLyOiAG5OV4i1oSqRUE02X-Zbvi2LskYgFVgzXP_ILnSGI8Vi0j8vdT-eQ5halckflMf8Joi_eC7lpJT8w4IBvt_7wWAKvyRjBmVaMbtFvr9FGLVuvX_S11dKpC6eOYIgqpGGhNRXRwVtX4IuQvbZTCbIboKCanC1024KkkSQUTx8pt48DBV-mWpr0ZhqcaGXT0xGKq1eC1iaSWw8c9r2hXDISJaEYReJ1kBocJy_-0yWsvCiwoS2Si-foaOWIsYOCQFjNxgXIEM1aO6lC7gfInIdHguIBVE94G8jObBh4A19Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔽
صدور مجوز حرفه‌ای باشگاه  پرسپولیس با ابلاغ رسمی دبیرکل فدراسیون فوتبال
🔴
رسانه رسمی پرسپولیس:
❤️
با دریافت نامه‌ای از سوی دبیرکل فدراسیون فوتبال، مجوز حرفه‌ای باشگاه پرسپولیس برای فصل پیش رو صادر و به طور رسمی ابلاغ شد.
🔽
این مجوز که بر اساس مدارک ارائه…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131984" target="_blank">📅 18:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131983">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
فدراسیون فوتبال به طور رسمی با ارسال نامه‌ای صدور مجوز حرفه‌ای برای حضور در رقابت‌های لیگ نخبگان آسیا را به باشگاه استقلال اعلام کرد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131983" target="_blank">📅 18:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131982">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
‼️
باشگاه استقلال صورت مالی شش ماهه (۳۰ دی ۱۴۰۴) رو روی سایت کدال آپلود نکرده است. به این دلیل که مدارک مالی و شفافیت در بخش‌های مختلف باشگاه در راستای حرفه‌ای‌سازی از سال گذشته آماده نیست.
🚫
یکی از الزامات اصلی مجوز حرفه‌ای‌سازی است که حالا استقلال فاقد این…</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131982" target="_blank">📅 17:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131981">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
۶ باشگاه ایران در آستانه کسب مجوز آسیایی
⚪️
برای فصل آینده ۶ باشگاه لیگ برتری مجوز حرفه‌ای از کنفدراسیون فوتبال آسیا دریافت خواهند کرد.
🔴
به نظر می‌رسد استقلال، تراکتور، گل‌گهر سیرجان، چادرملوی اردکان و پرسپولیس از جمله باشگاه‌هایی هستند که مجوز حرفه‌ای دریافت…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131981" target="_blank">📅 17:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131980">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
👈
ادعای «میدل ایست آی»: به ترامپ هشدار داده شده آغاز جنگ در ایام حج، آمریکا را در جهان اسلام منفورتر می‌کند و به همین دلیل حمله به ایران به تعویق افتاده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131980" target="_blank">📅 17:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131979">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
⭕️
#شایعات
🗣
اوسمار خواهان بازگشت دانیال اسماعیلی فر و مهدی ترابی شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131979" target="_blank">📅 17:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131978">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8RyvpZcNIoiOLrW6knECI_HXuIoc8xsX_tNYxGJteaAcGuDspReWZSB8W8ECBLyQkN6dG5t5kx8QJbFIPcE-7LqxVfoKxPJALM4BUxZ9oqiXm3gOspgPNO2Z7q5GHBMFwG5K2TkTR-oKR00MyayLvADJEHSYI4trRAvY5QUOiUhO7gz5cfBpt27tXr0nh2umHIDhlzsoxSVctCf0Iygooffjw-coEX1g1gAr28yMY_rUUuEluJ207CgKLV9R-WHgXr5MR1DKahwLP4qScn_WWu-IiDP7_qzQ08F50nOJAZnoD8NVacEi1MyJfTAceSxLiwFFRStbPBrZfQ0jQBLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رفیعی دروازه بان پرسپولیس و همسرش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/131978" target="_blank">📅 12:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131977">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔵
سهراب بختیاری‌زاده: پرسپولیس عادت به فساد کرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131977" target="_blank">📅 12:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131975">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
رونمایی از لیست ۶۰ نفره قلعه‌نویی برای جام جهانی ۲۰۲۶؛ غیبت قطعی احمد نوراللهی
👀
امیر قلعه‌نویی در حالی لیست اولیه‌اش برای جام جهانی ۲۰۲۶ را تنظیم کرده که مشخصاً نام یک چهره در این فهرست به چشم نمی‌خورد؛ احمد نوراللهی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/131975" target="_blank">📅 10:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131974">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
#فوری | آکسیوس:
🔻
یک منبع آمریکایی گفت ترامپ به نتانیاهو گفته است که میانجی‌ها در حال کار بر روی یک «توافقنامه» هستند که هم ایالات متحده و هم ایران آن را امضا خواهند کرد تا رسماً به جنگ پایان دهند و یک دوره ۳۰ روزه مذاکره در مورد مسائلی مانند برنامه هسته‌ای…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131974" target="_blank">📅 10:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131973">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🏅
باشگاه پرسپولیس هزینه کامل دادرسی پرونده شکایت از بیرانوند را به CAS واریز کرد
⏺
باشگاه پرسپولیس که پیش از این بابت پرونده علیرضا بیرانوند دروازه‌بان تراکتور به دادگاه عالی ورزش شکایت کرده بود برای اینکه این دادگاه رای نهایی را صادر کند هزینه‌های دادرسی را…</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131973" target="_blank">📅 10:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131972">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzo_jjC9ToHP_ZuCFD1JUyPyQjN5sfpNCENkQUf4gQ6YggrSSOtNOJfvoJS27JdhM2EABcylQJV4rJ-wyBun9OMWxJId8R8kmCdBUwDnSN1WlE_Lucq1B-FgGR9x2tZq-MpfHFCA_Cz0MHdDI5-atmkXHDCnjxpj4-qy3GLLYK6LywlXCn1L3YWxrovdU8lBvTGWp3etjF4IV8rXfS3Zjh_k7v0dmA8Tvav8ktDw9B_zN9avqPNmEnvzqb4_igxv0IcD7a_FZdtxBZCKFRhQYrdEpi65_7DAFyZ1X0o2SFHyIuzmZqvUSk8T81dNsKASTH1wFi2N7bWem5NqCvhcSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
واکنش باشگاه سپاهان به باشگاه هایی که با بازیکنان این تیم مذاکره کرده اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/131972" target="_blank">📅 10:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131971">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⚽️
❤️
سردار دورسون: از ایران و ترکیه پیشنهاد دارم
🔴
امیدوارم صلح به ایران بازگردد
🔴
از روز اول رابطه خوبی با هاشمیان نداشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131971" target="_blank">📅 10:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131970">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
فوری/  عضو کمیسیون امنیت ملی مجلس:  عاصم منیر فردا حامل پیام جدیدی از سوی آمریکا به ایران است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131970" target="_blank">📅 10:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131969">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
| فرهیختگان:
✅
باشگاه پرسپولیس با باشگاه سپاهان سر مبلغ قرارداد مهدی لیموچی به توافق نرسیدند و خود مهدی  نیز دوست دارد فصل بعد در سپاهان توپ بزند چون احتمال آسیایی شدن این تیم بیشتر است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/131969" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131968">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
#فوری | آکسیوس:
🔻
یک منبع آمریکایی گفت ترامپ به نتانیاهو گفته است که میانجی‌ها در حال کار بر روی یک «توافقنامه» هستند که هم ایالات متحده و هم ایران آن را امضا خواهند کرد تا رسماً به جنگ پایان دهند و یک دوره ۳۰ روزه مذاکره در مورد مسائلی مانند برنامه هسته‌ای…</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/131968" target="_blank">📅 00:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131967">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/131967" target="_blank">📅 00:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131966">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
#فوری | آکسیوس:
🔻
یک منبع آمریکایی گفت ترامپ به نتانیاهو گفته است که میانجی‌ها در حال کار بر روی یک «توافقنامه» هستند که هم ایالات متحده و هم ایران آن را امضا خواهند کرد تا رسماً به جنگ پایان دهند و یک دوره ۳۰ روزه مذاکره در مورد مسائلی مانند برنامه هسته‌ای…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/131966" target="_blank">📅 23:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131965">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
عاصم منیر فردا به تهران می‌رود احتمالا خبر مهمی در راه است
🔴
روزنامه ابزرور پاکستان: فیلد مارشال سید عاصم منیر، رئیس ستاد ارتش، به عنوان چهره‌ای کلیدی در روند دیپلماتیک ایران و آمریکا، فردا به ایران می‌رود. در طول این سفر احتمالی، انتظار می‌رود اعلامیه‌ای…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/131965" target="_blank">📅 23:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131964">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
ترامپ: منتظر پاسخ مناسبی از ایران هستیم تا از تشدید بیشتر جلوگیری کنیم.
🔴
چند روزی منتظر پاسخ ایران خواهیم ماند.
🔴
تا زمانی که به توافق نرسیم، هیچ تحریمی را از ایران برنمی‌دارم.
🔴
در ایران افراد باهوش و بااستعدادی وجود دارند و امیدواریم معامله‌ای خوب برای…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131964" target="_blank">📅 23:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131963">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
‏
ترامپ: اگر توافق امضا نشود، ایران این آخر هفته برق نخواهد داشت
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131963" target="_blank">📅 23:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131961">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
سرخپوشان نمی‌خواهند خسارت بدهند
✅
پرسپولیس به‌دنبال تنظیم دفاعیه برای شکایت اوریه
✅
فرهیختگان: سرژ اوریه یکی از خریدهای عجیب باشگاه پرسپولیس در بازار نقل و انتقالات تابستانی بود. در واقع همان مقطعی که رضا درویش بابت خرید اوریه در رسانه‌ها از بهترین خرید…</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131961" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131960">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
خروجی های پرسپولیس تا به این لحظه :
🔺
سروش رفیعی
🔺
میلاد محمدی
🔺
مرتضی پورعلی گنجی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131960" target="_blank">📅 22:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131959">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131959" target="_blank">📅 22:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131958">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تأیید محکومیت 15 میلیاردی شمس آذر در ماجرای فخریان
🔴
کمیته استیناف فدراسیون فوتبال رأی محکومیت باشگاه شمس آذر قزوین در پرونده انتقال مجتبی فخریان به پرسپولیس را تأیید کرد و به این ترتیب باشگاه قزوینی باید این مبلغ را به پرسپولیس بازگرداند.
🔴
باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131958" target="_blank">📅 22:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131957">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
🚨
🚨
#فوری | ترامپ:
🔻
همه چیز تمام شد. تنها سوال این است که آیا ما می رویم و آن را تمام می کنیم، یا آنها قرار است سندی را امضا کنند؟ ببینیم چه اتفاقی می افتد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131957" target="_blank">📅 22:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131956">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
عاصم منیر فردا به تهران می‌رود احتمالا خبر مهمی در راه است
🔴
روزنامه ابزرور پاکستان: فیلد مارشال سید عاصم منیر، رئیس ستاد ارتش، به عنوان چهره‌ای کلیدی در روند دیپلماتیک ایران و آمریکا، فردا به ایران می‌رود. در طول این سفر احتمالی، انتظار می‌رود اعلامیه‌ای مبنی بر تأیید تکمیل پیش‌نویس نهایی توافق منتشر شود.
🔴
این سفر می‌تواند به عنوان یک نقطه عطف دیپلماتیک سطح بالا باشد، جایی که تکمیل نسخه نهایی توافق ممکن است رسماً اعلام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131956" target="_blank">📅 22:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131954">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
باشگاه پرسپولیس با مهدی لیموچی، بازیکن سپاهان وارد مذاکره شده و این بازیکن به همین علت درخواست جدایی از تیم سپاهان را ارائه کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 955 · <a href="https://t.me/SorkhTimes/131954" target="_blank">📅 22:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131953">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00eb689252.mp4?token=FZYj1pUi21CW033yZbccJCAsxSxqatA3oa2rhZwQmuXT_zyG5mryLoJVUbmQGd8eW31IOCZKkb9s5NKkQNDqud7O5nMDxSSSIR8j7R4ut5Kgdb8qQw5p3y7-8zY15MMmi-Law9PGwO7fr0j5KtXbbdo2WvmcF_GM1oGw4uu8uGk-x1ej6nuPTx1FW2uzEdlM4FzFCpavXAdCBLPpSNEIAVjo8IEddIINyyTgZckFwL1ivTUSf4oQInJgXUKB_p6Gcvq0ryv628Ui-tUYGq9WUDjpe_qk96lZnmQKyzcBi90YVbbb1yjzkRDpZ0H-SmlZC547c9GbSiDXfGwELWFHiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00eb689252.mp4?token=FZYj1pUi21CW033yZbccJCAsxSxqatA3oa2rhZwQmuXT_zyG5mryLoJVUbmQGd8eW31IOCZKkb9s5NKkQNDqud7O5nMDxSSSIR8j7R4ut5Kgdb8qQw5p3y7-8zY15MMmi-Law9PGwO7fr0j5KtXbbdo2WvmcF_GM1oGw4uu8uGk-x1ej6nuPTx1FW2uzEdlM4FzFCpavXAdCBLPpSNEIAVjo8IEddIINyyTgZckFwL1ivTUSf4oQInJgXUKB_p6Gcvq0ryv628Ui-tUYGq9WUDjpe_qk96lZnmQKyzcBi90YVbbb1yjzkRDpZ0H-SmlZC547c9GbSiDXfGwELWFHiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قلعه‌نویی به نورافکن: آقای امیدخان نمیفهمی پای راسته؟ حتی اینم نمیفهمی
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 999 · <a href="https://t.me/SorkhTimes/131953" target="_blank">📅 22:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131952">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1098692638.mp4?token=UZRiNeDoyvlXa_587MmEcK61YMzHJpuudEihw0zB33HjDwKicKis1tKrooQpfy0JIoEz09qgwKjiDOpXEgpXv5Cf7vR_LcVzY1GlwpFmcS5lHoyyhgLcoVFwsWvAqTox6oKo1Un0Lv4znhT5qUb5USvXzE9xCFVw0NWHX0zEUQb7_gUoKuQO-k8Gz4viKGCs9w2ppBN8iB9594oODfAlHd5lBe135iL8tZZ8aHdp8iezdgoqmtRU_6XVR_MK13K2KyCicoetZedTmbTsiQxtOInl2X6BCHlVNBr38h9d8nlEpE_v0wfZqEzsaMI-hjuQ5xRssAmfVs0aCd37c37x4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1098692638.mp4?token=UZRiNeDoyvlXa_587MmEcK61YMzHJpuudEihw0zB33HjDwKicKis1tKrooQpfy0JIoEz09qgwKjiDOpXEgpXv5Cf7vR_LcVzY1GlwpFmcS5lHoyyhgLcoVFwsWvAqTox6oKo1Un0Lv4znhT5qUb5USvXzE9xCFVw0NWHX0zEUQb7_gUoKuQO-k8Gz4viKGCs9w2ppBN8iB9594oODfAlHd5lBe135iL8tZZ8aHdp8iezdgoqmtRU_6XVR_MK13K2KyCicoetZedTmbTsiQxtOInl2X6BCHlVNBr38h9d8nlEpE_v0wfZqEzsaMI-hjuQ5xRssAmfVs0aCd37c37x4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| ادعای آکسیوس:
🔻
قطر پیش‌نویس توافق جدیدی برای کاهش تنش‌ها میان تهران و واشنگتن ارائه کرده است
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/SorkhTimes/131952" target="_blank">📅 22:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131951">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
ورزش سه: روزبه چشمی از ناحیه رباط صلیبی مصدوم شد و جام جهانی رو از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131951" target="_blank">📅 21:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131950">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-_12_GjeV9d8XuoohIyzO7ceedLr4TkX8BNuI-5-EUqmlt1K_-SKVIFe2iSskXe7VsomXbU5hNwh2p4Q095w3gNvBtTcpcRnEu6IGxKMg-qNXUWmi-pw8o0ZXp2jvor0pvEeWr4LR9h_yqZvRw6N9jDGAbVt08oO3LwJofXitr38iIAWNrTmxWcnU0lf0NP-NcZUuISFUY7QHf-9hVN7ovk_tLXRTuyGFELQcat--rYb3CKMnhPZfUTXnb4D7G7v4aP8Ai63TDpFcI8axkk-W2-vQBEJQ0H41ovfFRpDM74NVlKWZrJltZXli6xALyS2RU-Yac-LzAMJvr68Oc68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
Final Europa League
⚫️
Freiburg -
🔵
AstonVilla
‼️
این روزا قبل از پیش‌بینی بیشتر از خود بازی باید نگران این باشی که VPN وصل میشه یا نه.
😀
ربات تلگرام وینکوبت دقیقاً برای همین شرایط خوبه چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
براحتی میتونید برای بازی فینال لیگ اروپا وارد سایت بشید و این دیدار رو پیش‌بینی کنید، واریز و برداشت هم بصورت آنی می‌باشد.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131950" target="_blank">📅 21:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131949">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
5 گیگ 800T
10 گیگ 1.5T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 985 · <a href="https://t.me/SorkhTimes/131949" target="_blank">📅 21:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131946">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050c7fea46.mp4?token=pkQpCEUmDx_2Mu8QzvY0-s2jUZtuGpcFnLTW8OD35FmTKC4SmZU2wesZjIR6sAfA84WWZgKpbDbiea8gAlrdvCeDMuqC_DoqYkkGEqOCQXiitdTLbqlAyTquiAdVyRb-aqKNSimYPfQjSuv6pB_px-n-oPe7JbpHSVoox1TjpqK0ZoQuE9VvP-FxVgQo9GfYLATeoeqw5B3vlJza6RS9CK_kmxYbI2HUWCqmP39XBvwRsGxDCSrHFTpfIIS9VGS-JvGxUpmL50XWQzYvK6k65oQ_SVeVuxjr5GK2hqqS10b72UjPIaxy2mTa0soYg-2LthRAw_yPiIj5UQdM5wdKmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050c7fea46.mp4?token=pkQpCEUmDx_2Mu8QzvY0-s2jUZtuGpcFnLTW8OD35FmTKC4SmZU2wesZjIR6sAfA84WWZgKpbDbiea8gAlrdvCeDMuqC_DoqYkkGEqOCQXiitdTLbqlAyTquiAdVyRb-aqKNSimYPfQjSuv6pB_px-n-oPe7JbpHSVoox1TjpqK0ZoQuE9VvP-FxVgQo9GfYLATeoeqw5B3vlJza6RS9CK_kmxYbI2HUWCqmP39XBvwRsGxDCSrHFTpfIIS9VGS-JvGxUpmL50XWQzYvK6k65oQ_SVeVuxjr5GK2hqqS10b72UjPIaxy2mTa0soYg-2LthRAw_yPiIj5UQdM5wdKmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
❤️
سردار دورسون: از ایران و ترکیه پیشنهاد دارم
🔴
امیدوارم صلح به ایران بازگردد
🔴
از روز اول رابطه خوبی با هاشمیان نداشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131946" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131945">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKM9KJJJ2Yzksrt2eCHwN3_OgkNf3F-sco1BTvJugeMQSY5Iph3MizHwX0RiOsDr1695djLa9b3ZWA0q8GfZwhRKkKAqS_af2FsCcfO0y0wggaXHmX-en_LPjuq2AL9TAfOfYDrNaGPHPQkikUgqLFiZU25tBqnCrQLEyZEcWosUFv2F9bNVeSw1FVEaWcFI_cfhR4qfU_OXauOt575IPwIGk1vW7H1yiAeXggI5yMCFDw-2yeHXWJkZXXaEj1QvG4QZA_XJu4Rar_jTHBWca-LM_SAxpG3J7xLEleajzEeE83fNtcj5oeeV0DbkVfXrjoemjlgf6DQWIAZ4G7wffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوووووری
شبکه الحدث :
احتمالا طی ساعات آینده، متن توافق ایران و آمریکا نهایی میشه؛ دور بعدی مذاکرات هم باز تو پاکستانه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131945" target="_blank">📅 20:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131944">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔥
۲عدد سرور ۱۰ گیگ اف خورده ۱۹۰۰
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131944" target="_blank">📅 19:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131943">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84765e9843.mp4?token=EEc4_9qRKqbize9hYXbzZEDWbTSGxtEx30_qkHfdO_AUy5LkaWDWDWSTUqb5ZHV0dPGxi54l2yTFfOwIYvexwt9i3wrT_OeBmpQnhPpUO_WhdcMlvEHtcExDTna8Dzjvxx4KOwNoga5Gdp-bqHdL_Wc9vXp2NIOPwCL0cqXqGWDNs3dWnV3giQd6kr4uI9qyOuuFH7umCFjNmmqLafgsCyf6tl3adpyTJS8OkVVKD8XY_KcMXBJh3Q6LVVXX1zXkbq4rLfqUtl3WnhP5lxWPO47MqtNVlfhjTCg6iwr49XXnMQqOe367T-AmCFDLaLtXPEszhgz3ZzthYuCbksB-M4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84765e9843.mp4?token=EEc4_9qRKqbize9hYXbzZEDWbTSGxtEx30_qkHfdO_AUy5LkaWDWDWSTUqb5ZHV0dPGxi54l2yTFfOwIYvexwt9i3wrT_OeBmpQnhPpUO_WhdcMlvEHtcExDTna8Dzjvxx4KOwNoga5Gdp-bqHdL_Wc9vXp2NIOPwCL0cqXqGWDNs3dWnV3giQd6kr4uI9qyOuuFH7umCFjNmmqLafgsCyf6tl3adpyTJS8OkVVKD8XY_KcMXBJh3Q6LVVXX1zXkbq4rLfqUtl3WnhP5lxWPO47MqtNVlfhjTCg6iwr49XXnMQqOe367T-AmCFDLaLtXPEszhgz3ZzthYuCbksB-M4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سردار دورسون‌ مهاجم سابق پرسپولیس مهمان امروز تمرین تیم ملی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131943" target="_blank">📅 19:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131942">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
#تکمیلی | ترامپ:
🔻
یا با ایران به توافق می‌رسیم یا کارهای سختی انجام خواهیم داد و امیدواریم این اتفاق نیفتد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131942" target="_blank">📅 19:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131941">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
نصیرزاده، وکیل علیرضا بیرانوند: در صورتی که حتی رای محرومیت ۴ ماهه این دروازه‌بان توسط دادگاه CAS تایید شود، محرومیت وی شامل جام جهانی نخواهد شد.
⏺
به محض اینکه هزینه دادرسی واریز شود، رای صادر نمی‌شود. تا بخواهند رای را صادر کنند جام جهانی تمام شده است.…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131941" target="_blank">📅 19:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131940">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
🔻
ادعای العربیه: ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده شود  العربیه:
🔹
کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران…</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131940" target="_blank">📅 19:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131939">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❗️
🔻
ادعای العربیه: ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده شود  العربیه:
🔹
کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران…</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/SorkhTimes/131939" target="_blank">📅 19:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131936">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
🇺🇸
ترامپ: آمریکا در «مراحل نهایی» مذاکرات با ایرانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 993 · <a href="https://t.me/SorkhTimes/131936" target="_blank">📅 19:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131935">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
ترامپ درباره ایران: من عجله‌ای ندارم، همه میگن انتخابات میان‌دوره‌ای و اینا، من برای جنگ اصلاً عجله ندارم.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/SorkhTimes/131935" target="_blank">📅 19:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131934">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIMXH9MYWflbZ-KQ2EIuTesk0sCU0xNyw87TOtGxLinWKY7hIAwzUuQE8wh-lNZF2nLx_ES8X9-WblF-VHwYNiti-rcAdnInsRSwQ9VNxKXp0uJ3_q8y5tKTeKTC3-lmgKv3twDsGgf0zzgYiaiZUNGPxJHiXsrJP83ja8tmkD62P63Cu9vnn75cYfyTtcgwuqxBV178w0LMiLIMV669rx8yVMbHKsv64gYycZrFnN4NHAAKZmfe7jGeojlwPMpeWGuRaAmZd6TbczHAiVlbH5D6Il32Vz2lsVMJpz7zGOV35GGyY7nfVZhNjXU91hiq2kQFsmmGmcZyMRotB9Vxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
شکایت یک شرکت تبلیغاتی از باشگاه پرسپولیس در دادگاه تجدید نظر رد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/SorkhTimes/131934" target="_blank">📅 18:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131933">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rA_DbxzrTGMyt9g0huWcIpLEYOlh3DHeNp0mDTYFPF1toXlIyd1AxXmSKOWrJNUP0ynTgtQJNC_19zF_VNpMkyTMeO9og7se-K3T9e5uvdpO2jL727v4ICJcD4Qufzq0Nj45bkfytGZwRBrxtx_E8K_HXs-0jF6WbC7r1E_NaduTl0GUJukTpx1JArETu6-0nwsS9DhYTH9AuTxOrA-lxl-lnQ_eAMFZ8C1-CxYNc2LyrXBGyUJNvhAC8_rxVsycVwzbcXwyvuUGVhZ62MzR3VavD--Em6qga38cA_eeSO9STUXYpCCtv5DdqUi7-snq6OZ26rqJjV6nPbvvBcGjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
بازیکنان مطرح تیم ملی سعی میکنند سردار آزمون تو لحظات آخری برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131933" target="_blank">📅 18:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131932">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ab8278f1.mp4?token=LvwVEBCSfoxaLf5k_PgCtuT7EoXXx8z8Wzkz2NG_NvrbHZqpnuWpPCrKZd_ArIjUH9Rpkjk9VwKYYyFl0ZmeXbTgTafSAiwy-MMChvdq46X_JAl7CkpiYVd8slVvj9t2kWJNk0HHg0hZBDi9_kX_iiA2IQyjahnHJ3RI2VeV1WDVps1OCPVPNY6bHM3I4beX6gtAoCbCDs-_9VK1gW6iEVdTr8KfBF_bjRCikL8JLVo3PfhotPptnnHtjXt6hsfSzhI0LQcRbBUl9c0rp0I2K1MqlXhs57soxrKeDIcrSECUbCDnePebaFOK8gO3-41pROOl1pDOljYcHuu_MtRGww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ab8278f1.mp4?token=LvwVEBCSfoxaLf5k_PgCtuT7EoXXx8z8Wzkz2NG_NvrbHZqpnuWpPCrKZd_ArIjUH9Rpkjk9VwKYYyFl0ZmeXbTgTafSAiwy-MMChvdq46X_JAl7CkpiYVd8slVvj9t2kWJNk0HHg0hZBDi9_kX_iiA2IQyjahnHJ3RI2VeV1WDVps1OCPVPNY6bHM3I4beX6gtAoCbCDs-_9VK1gW6iEVdTr8KfBF_bjRCikL8JLVo3PfhotPptnnHtjXt6hsfSzhI0LQcRbBUl9c0rp0I2K1MqlXhs57soxrKeDIcrSECUbCDnePebaFOK8gO3-41pROOl1pDOljYcHuu_MtRGww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ورود کادرفنی تیم ملی به کمپ تمرینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 897 · <a href="https://t.me/SorkhTimes/131932" target="_blank">📅 18:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131931">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcc1b48df0.mp4?token=flkrrR8iCtmqlMuoP097cgCXOzNVr_VN1sGcCtsR_7eBsV0BnKFEkSOAtf5LelY2zJp2FZVtixk-otQomkiQfGv_Yh8d-abgk9wgyFek2o2WGuxH5nFD9_s5hLmUNRlAUklypZPISGkc6v4RP8IpmPhumuK-lC-ih_jHnJaJw15C7trwLcBx5T4GUrnNxcNGtL7zrQuQWO8zkfrrG02NBG6j_El2nowWEmN189qu_FsDrg4gsNO64alzKKTBtEQ6ujiFs4NdygK2QqD-LpURKBmf0chSp2stv_kugxWV_6stAEZkv5NM524NMXFtRz3OW4PUBmHyfp7tXifMkTDRvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcc1b48df0.mp4?token=flkrrR8iCtmqlMuoP097cgCXOzNVr_VN1sGcCtsR_7eBsV0BnKFEkSOAtf5LelY2zJp2FZVtixk-otQomkiQfGv_Yh8d-abgk9wgyFek2o2WGuxH5nFD9_s5hLmUNRlAUklypZPISGkc6v4RP8IpmPhumuK-lC-ih_jHnJaJw15C7trwLcBx5T4GUrnNxcNGtL7zrQuQWO8zkfrrG02NBG6j_El2nowWEmN189qu_FsDrg4gsNO64alzKKTBtEQ6ujiFs4NdygK2QqD-LpURKBmf0chSp2stv_kugxWV_6stAEZkv5NM524NMXFtRz3OW4PUBmHyfp7tXifMkTDRvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
زمین تمرینی شماره یک تایتانیک، محل تمرین امروز تیم ملی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/SorkhTimes/131931" target="_blank">📅 18:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131930">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
پاکستان متن توافقات اولیه را آماده کرده است و مذاکرات بعد از عید قربان در اسلام آباد انجام خواهد شد و تا ساعات آینده و نهایت تا فردا عاصم مونیر پایان جنگ را اعلام خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/SorkhTimes/131930" target="_blank">📅 18:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131928">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | رسانه‌های سعودی:
🔻
فرمانده ارتش پاکستان ممکن است فردا به ایران سفر کند تا نسخه نهایی توافق را اعلام کند. ممکن است طی ساعات آینده نسخه نهایی توافق بین آمریکا و ایران اعلام شود
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/SorkhTimes/131928" target="_blank">📅 18:23 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
