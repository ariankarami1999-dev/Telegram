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
<img src="https://cdn4.telesco.pe/file/f5CneY1ZmHC-EdsPeX0rWrP_ycM56U6emOhgrWJ81iyiKfpvkXhTPW5AssA0okJxzriOgEhJa8_Q9ydaKXI0Gvla0k9UZUpd4lKqf470xkmVXNJqsVCze1jlmzBfT4obc3T04OFbsEhkUFTbLbHfAD3AHLWqTqa7KbIqAbsAYaFUTcLEWqdWWElMEkT-aMKxK_QkLiP9Oq3Q_qaJCgAhZs1kMVULObJofL7djf3-N8fEEqIsbFIzrkESQhw4DhRwRVDJLvQfDcEJ2MPKFDYlFIdKNQjZFZmc2UJToGPON2biXS31jFbk48Eccy9cHsgfRXTAQiQGFwHcBz1RM9gzXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 260K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 08:36:54</div>
<hr>

<div class="tg-post" id="msg-11253">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/withyashar/11253" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11252">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBehnam Kok</strong></div>
<div class="tg-text">آقا ما استیکر حامله میخوایم</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/withyashar/11252" target="_blank">📅 01:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11251">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ در تروث : «وقتی رئیس‌جمهور شی با بیانی بسیار سنجیده از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او آسیب عظیمی بود که ما در چهار سال دوران جو بایدنِ خواب‌آلود و دولت بایدن متحمل شدیم؛ و در این مورد، او صددرصد درست می‌گفت.
کشور ما با مرزهای باز، مالیات‌های سنگین، ترویج تغییر جنسیت برای همه، حضور مردان در ورزش زنان، سیاست‌های موسوم به تنوع و شمول، توافق‌های تجاری وحشتناک، جرم و جنایت گسترده و بسیاری مسائل دیگر، آسیب غیرقابل‌تصوری دید!
@withyashar
رئیس‌جمهور شی به هیچ‌وجه به رشد شگفت‌انگیزی اشاره نمی‌کرد که ایالات متحده در طول شانزده ماه فوق‌العاده دولت ترامپ به جهان نشان داده است؛ دورانی که شامل رکورد تاریخی بازار بورس و صندوق‌های بازنشستگی، پیروزی نظامی و روابط شکوفا با ونزوئلا، درهم‌کوبیدن نظامی ایران (ادامه دارد!)، قدرتمندترین ارتش جهان با اختلاف بسیار زیاد، تبدیل دوباره آمریکا به یک قدرت اقتصادی عظیم، جذب رکورد هجده تریلیون دلار سرمایه‌گذاری خارجی در آمریکا، بهترین بازار کار تاریخ ایالات متحده با بیشترین تعداد شاغلان تاریخ کشور، پایان دادن به سیاست‌های ویرانگر موسوم به تنوع و شمول و بسیاری موفقیت‌های دیگر بوده که فهرست کردن همه آنها ممکن نیست.
در حقیقت، رئیس‌جمهور شی بابت این همه موفقیت بزرگ در چنین مدت کوتاهی به من تبریک گفت.
دو سال پیش، ما واقعاً کشوری در حال افول بودیم. در این مورد کاملاً با رئیس‌جمهور شی موافقم! اما حالا ایالات متحده داغ‌ترین و پررونق‌ترین کشور جهان است و امیدوارم رابطه ما با چین از همیشه قوی‌تر و بهتر باشد!»
@withyashar</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/withyashar/11251" target="_blank">📅 01:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11250">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فاکس نیوز : تو سفر ترامپ، بین مأموران سرویس مخفی آمریکا و پلیس چین، تنش ایجاد شده و درگیری لفظی و حتی فیزیکی هم پیش اومده.
@withyashar</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/withyashar/11250" target="_blank">📅 01:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11249">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB8oJUkyrSBysRzP-M_1gQ-TT5d3knMSu1TIdnQf7KJno1nPyjHRF6Nk9UMwmiNOWOfxnZKSbsmm18zk5JDZOAOMY1k7OQZnozCeBvVRZ2HqmelGWJVOTWlXErNhCjRmefjvt2zYqMklAS4TOt7Lqs4_nxvLCDx-5TrfP5YBRvsYzzl5kHkk3V-L9d7L9GmAikt69UL2F4PJFLHLfkTZlsxVQ582t8G9_8Hu9KfzajkH1hACSIRJUAzBnYvjI-agiAl7IOCneOOdOsueNcTNewe9hgs7r2CGy02s0oyO_EcnKKZfcM9FBa8wt5PaJdkIFu-c3UAJIvLIcz5O5CTv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کت کش ها در مراسم اربعین کتلت سرلشکر سیدعبدالرحیم موسوی در قم
@withyashar</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/withyashar/11249" target="_blank">📅 00:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11248">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591abd93e.mp4?token=c62lvPJg4n5FaSYq0sRyAY7_FWcXhjMKaox2rPsMnWzGi0lhaQwWdmNlSF6at01Hn2moIMrRQcuD4iiz6vQDJUsjF3C3DbVihHvcYpQsQOexe6Mbh5lvPHKkk64lRUuGr-hAfZFL_LmRw3h3rYMWn3uQHwS94SjyJQYb3yAkIV-t_6Fayx8TMQVONYTK62As8mHdHVDEvUEKUlg1PoycG2yX0FVm1454pMgw4o7jsyfh4SQN17FDoO9MT3JdQsOyDPO_XMsBT6GUI2QSNgBRUat8-XRn7hwPDgSCUCKBOJ0vBr39BP3GduTaSjYN_7Mb6OtVK06ClqYcE-7OQSolOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591abd93e.mp4?token=c62lvPJg4n5FaSYq0sRyAY7_FWcXhjMKaox2rPsMnWzGi0lhaQwWdmNlSF6at01Hn2moIMrRQcuD4iiz6vQDJUsjF3C3DbVihHvcYpQsQOexe6Mbh5lvPHKkk64lRUuGr-hAfZFL_LmRw3h3rYMWn3uQHwS94SjyJQYb3yAkIV-t_6Fayx8TMQVONYTK62As8mHdHVDEvUEKUlg1PoycG2yX0FVm1454pMgw4o7jsyfh4SQN17FDoO9MT3JdQsOyDPO_XMsBT6GUI2QSNgBRUat8-XRn7hwPDgSCUCKBOJ0vBr39BP3GduTaSjYN_7Mb6OtVK06ClqYcE-7OQSolOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ به دلیل مرگ برادر بزرگترش که بر اثر نوشیدن الکل جانش را از دست داد ،مشروب نمیخوره ،ولی اینجا جرعه‌ای از آن را مینوشه و به نشانه احترام به رئیس جمهور شی جین پینگ
‏ولی داشت بالا می‌آورد
@withyashar</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/withyashar/11248" target="_blank">📅 00:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11247">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">طبق گزارش‌های امروز، هرتزوگ رئیس جمهور اسرائیل حضور حضوری خود در نیویورک را لغو کرده و گفته به دلیل «شرایطی که مانع سفر شده» نمی‌تواند به آمریکا بیاید.
اما این سفر یک سفر رسمی سیاسی به کاخ سفید نبود،بلکه مربوط به شرکت او در مراسم فارغ‌التحصیلی «Jewish Theological Seminary» در نیویورک بود.
در عین حال، خبر جداگانه‌ای هم درباره سفر احتمالی بنیامین ناتانیاهو به آمریکا وجود داشت که دفتر او گفته بود هنوز برنامه قطعی‌ای برایش نهایی نشده است
@withyashar</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/11247" target="_blank">📅 00:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11246">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">طبق گزارش فاکس نیوز : رئیس‌جمهور ترامپ و هیئت همراهش در طول سفر به چین از تلفن‌ها و لپ‌تاپ‌های جایگزین استفاده کردند به دلیل نگرانی‌هایی که داشتند مبنی بر اینکه مقامات چینی ممکن است از آن‌ها برای نصب نرم‌افزار جاسوسی استفاده کنند
@withyashar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/11246" target="_blank">📅 23:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11245">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">همینجور این پیغام میاد دم همتون گرم مخصوصا عزیزی که یاد کرد از من
🥹
🙌🏾
❤️‍🩹
میامممم میاممم</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/11245" target="_blank">📅 23:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11244">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmd</strong></div>
<div class="tg-text">یکی اومد رو خط برنامه کامبیز تو اینترنشنال گفتش از همه مجریای اینترنشنال تشکر میکنم ، حتی یاشار وار روم توی تلگرام ک خیلیا اخبارا رو ازونجا دنبال میکنن دمتون گرم</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/11244" target="_blank">📅 23:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11242">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دیده شده پهپاد شناسایی و صدای پدافند غرب تهران
@withyashar</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/11242" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11241">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اعتراضات کوبا شروع شد کشور در حال  فروپاشی
طبق گزارش‌ها، شبکه برق کوبا در بامداد امروز دچار فروپاشی شد و مناطق شرقی از جمله شهر مهم سانتیاگو دِ کوبا بدون برق ماندند. مردم به خیابان آمدند، قابلمه‌ها را به هم کوبیدند، زباله آتش زدند و شعار «برق را وصل کنید» سر دادند.
دولت کوبا علت اصلی را تحریم‌ها و فشار آمریکا بر صادرات سوخت به کوبا می‌داند. رسانه‌هایی مانند رویترز و گاردین نوشته‌اند که پس از تهدیدهای جدید دولت ترامپ علیه کشورهایی که به کوبا سوخت می‌فرستند، ارسال نفت از ونزوئلا و مکزیک کاهش یافته و کوبا عملاً ذخیره سوختش را از دست داده است. وزیر انرژی کوبا گفته:
«ما مطلقاً هیچ گازوئیل و هیچ نفت کوره‌ای نداریم.»
در بعضی مناطق مردم تا ۲۰ یا حتی ۲۲ ساعت در روز برق ندارند. این وضعیت باعث خراب شدن مواد غذایی، اختلال در بیمارستان‌ها، حمل‌ونقل و حتی تعطیلی برخی خدمات عمومی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/11241" target="_blank">📅 23:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11240">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141998de31.mp4?token=mWjKL2syYnwh-XyrnfJBPHJ8rVi-6aZV8LWqYTdoxOToXzAtM6eyMdGUPLTLhHhn9i4PcpnklZS0g1eSAhFe19wCr4F-Ib1wIr7ho47yrZ6esNIL-apTeZymZZ6wLd2O_wDPcHFzS8R2FJKdT5tqIfQyeJ9_pFD7z8UTjlZnaB0e8bsqWAxnxNq5boTh56UnqHV0AqSLrCJNKJr-gti6kn2H0s5ttNudyjvSzSMPNF7jYd70J71HJS2Pqba2ZyWtmxD3bvhgeuJcK8CFhkYfAxAgn65GZxuCI-_0g8S6HHKDuKJf829-WZ9-1g4lzU43de0qiw7RnkkDaWGNh1MVzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141998de31.mp4?token=mWjKL2syYnwh-XyrnfJBPHJ8rVi-6aZV8LWqYTdoxOToXzAtM6eyMdGUPLTLhHhn9i4PcpnklZS0g1eSAhFe19wCr4F-Ib1wIr7ho47yrZ6esNIL-apTeZymZZ6wLd2O_wDPcHFzS8R2FJKdT5tqIfQyeJ9_pFD7z8UTjlZnaB0e8bsqWAxnxNq5boTh56UnqHV0AqSLrCJNKJr-gti6kn2H0s5ttNudyjvSzSMPNF7jYd70J71HJS2Pqba2ZyWtmxD3bvhgeuJcK8CFhkYfAxAgn65GZxuCI-_0g8S6HHKDuKJf829-WZ9-1g4lzU43de0qiw7RnkkDaWGNh1MVzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیروزی بزرگ برای‌ ترامپ ، فاکس نیوز تایید کرد
رئیس جمهور چین، شی جین پینگ دستور داد در مورد ایران، «هر چیزی که ترامپ نیاز دارد» را به آمریکا بدهید.
از ‌آمریکا سویای بیشتری بخرید.
نفت بیشتری از آمریکا بخرید.
از آمریکا گاز مایع طبیعی بیشتری بخرید.
۲۰۰ جت بوئینگ ۷۳۷ مکس بخرید.
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/11240" target="_blank">📅 22:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11239">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبر خوب
😍</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/11239" target="_blank">📅 22:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11238">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7bad13156.mp4?token=bpCAOSuqZtLMYAYqnB-HJEb7KW_ce2oe6N-ZpHUw8Uaikh-TrI0KkCfKFYF4fmaCiHTJoNx6Tt5QGt1Pqk2DwwI8NgFbCAxeY115PaztVOHpb9444oh4WXSpF8qkFVxbZGtloHkyaxJST0EfhddYwQKHh2DJIfe7W43JKios9YgIllAm-2eFZzsBro135NHjiCtadw66QKvNz86u0xR9Y4JCs5vi37__w4FjISf4yvbPwE331Lis6yMLC-CyYznquvE8peE--8g-CnJtOrYKqgog7eOtgYUe3aeJ4gAszehZ3A1fZZv0y86szcKsHF8Po91diT2KZClqBn8PKvgldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7bad13156.mp4?token=bpCAOSuqZtLMYAYqnB-HJEb7KW_ce2oe6N-ZpHUw8Uaikh-TrI0KkCfKFYF4fmaCiHTJoNx6Tt5QGt1Pqk2DwwI8NgFbCAxeY115PaztVOHpb9444oh4WXSpF8qkFVxbZGtloHkyaxJST0EfhddYwQKHh2DJIfe7W43JKios9YgIllAm-2eFZzsBro135NHjiCtadw66QKvNz86u0xR9Y4JCs5vi37__w4FjISf4yvbPwE331Lis6yMLC-CyYznquvE8peE--8g-CnJtOrYKqgog7eOtgYUe3aeJ4gAszehZ3A1fZZv0y86szcKsHF8Po91diT2KZClqBn8PKvgldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: دشمنان ما به دنبال نابودی همه ما هستند. همه ما
آنها بین راست و چپ، سکولار و مذهبی، یهودی و عرب تفاوتی قائل نمی‌شوند.
@withyashar
نتانیاهو: اورشلیم را تحت حاکمیت اسرائیل برای همیشه حفظ خواهیم کرد</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/11238" target="_blank">📅 22:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11237">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/11237" target="_blank">📅 21:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11236">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سومین دور مذاکرات مستقیم لبنان و اسرائیل در واشنگتن آغاز شد
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/11236" target="_blank">📅 21:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11235">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ اعلام کرد که انتظار می‌رود پکن ۲۰۰ هواپیما از بوئینگ سفارش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11235" target="_blank">📅 21:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11234">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کان نیوز : مقامات ارشد ارتش اسرائیل و سنتکام  هفته گذشته جلسه داشتن و منتظرن ببینن فردا ترامپ بعد اتمام سفرش چه تصمیمی میگیره
@withyashar</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/11234" target="_blank">📅 21:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11233">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016c112e90.mp4?token=Lyah6gFCEmODdi8dMub3GVR5nhEoc4Xbx22HDQWkX-6Q0iA0T7QoIA2pT7NvXoCmHDpq6ZdZD74W-y6MgeZHsK6h1JS4gFMNb5sRnBeuMKXAdO_d4T-DoNN_9RvwsDc05n31HV7mBDh_SulyZxeoXQ6st-076cu7bnHxVfMpdMi3wnf-C7A5AGug5vVudTJHmQolxTHjzF6Mxgb08b_Ua4ESfO0g0zbPm0WX-3fp2kf6Y_4WtLU-T_EPxyFd96VHt0xMUqUktNKDoPCQbZnSu1lhfG-WBOzHMSew48cP92kqfnCMj0ePYtuEMEObZST0QrSSqY-Nxo48lJZVNR29sHEFzOB99sQDGAHqhHPxcg8BP3yzckEoxOaBKa2O0rFhzbkEgHrYk26R6lVv2E9ZBTlfvaehndw9VJSS3NTocvLMd-sG2xEXzFj4RYdKWwNS7RrmgNCYSg6gF1efDf3vu7-MlOvgiYiy6V29XAl2tvoRsl5hU75eHd0NDqxi4RGqaBBn-YAIF7Qu_A7LgR0q1QkaT1FurO3S2JW8_S6SD3IJya44ZoIBIVVTI2-F8wQsPfmmkfOn8HRDK_l79U98HeK_XS3vaVG0A_llUVIR0tRgjSOmnvBYT4CPPzC6pX-VyP4ufVJXKfnLcaYjo80GQAPkZZm3ddGyAq5DB2da1yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016c112e90.mp4?token=Lyah6gFCEmODdi8dMub3GVR5nhEoc4Xbx22HDQWkX-6Q0iA0T7QoIA2pT7NvXoCmHDpq6ZdZD74W-y6MgeZHsK6h1JS4gFMNb5sRnBeuMKXAdO_d4T-DoNN_9RvwsDc05n31HV7mBDh_SulyZxeoXQ6st-076cu7bnHxVfMpdMi3wnf-C7A5AGug5vVudTJHmQolxTHjzF6Mxgb08b_Ua4ESfO0g0zbPm0WX-3fp2kf6Y_4WtLU-T_EPxyFd96VHt0xMUqUktNKDoPCQbZnSu1lhfG-WBOzHMSew48cP92kqfnCMj0ePYtuEMEObZST0QrSSqY-Nxo48lJZVNR29sHEFzOB99sQDGAHqhHPxcg8BP3yzckEoxOaBKa2O0rFhzbkEgHrYk26R6lVv2E9ZBTlfvaehndw9VJSS3NTocvLMd-sG2xEXzFj4RYdKWwNS7RrmgNCYSg6gF1efDf3vu7-MlOvgiYiy6V29XAl2tvoRsl5hU75eHd0NDqxi4RGqaBBn-YAIF7Qu_A7LgR0q1QkaT1FurO3S2JW8_S6SD3IJya44ZoIBIVVTI2-F8wQsPfmmkfOn8HRDK_l79U98HeK_XS3vaVG0A_llUVIR0tRgjSOmnvBYT4CPPzC6pX-VyP4ufVJXKfnLcaYjo80GQAPkZZm3ddGyAq5DB2da1yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار ، شواهد نشان دهنده حمله غافلگیر کننده برای کتلت پزون است
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/11233" target="_blank">📅 20:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11232">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30fb109482.mp4?token=BV3J-AOMgr2UlbOH4oH6JcxDjdlDz0Dxs0jIJrs8WQbP7FhaGoyHW0tsqhDAtC7xb879EfuNsn1zFJozH4RtX0KbIjXE8KmGQrfGlPP-zQmrvOKSih_yJ2DG-KBjACZI6gM3EyLe0Xjzy0zTyvRrwXiL_y4F_V0Jp1s5H4YHJP6BOrcr4ciPrekYUY4peFQc8cqJQEFUEcruKsfT7cOy3K64SJZwcKf489X-wVLyUpR42rUK5mXDKCfx0QzQGkOrFiHYQqFFm9yIIxu2TW1jrThgYQ-_xF3sET4Ftjm64uo9A56ocDzQC7IXvufEtumBeaoeFIAwNxv8j2cJY_j-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30fb109482.mp4?token=BV3J-AOMgr2UlbOH4oH6JcxDjdlDz0Dxs0jIJrs8WQbP7FhaGoyHW0tsqhDAtC7xb879EfuNsn1zFJozH4RtX0KbIjXE8KmGQrfGlPP-zQmrvOKSih_yJ2DG-KBjACZI6gM3EyLe0Xjzy0zTyvRrwXiL_y4F_V0Jp1s5H4YHJP6BOrcr4ciPrekYUY4peFQc8cqJQEFUEcruKsfT7cOy3K64SJZwcKf489X-wVLyUpR42rUK5mXDKCfx0QzQGkOrFiHYQqFFm9yIIxu2TW1jrThgYQ-_xF3sET4Ftjm64uo9A56ocDzQC7IXvufEtumBeaoeFIAwNxv8j2cJY_j-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سال ۱۹۷۲، شهبانو فرح پهلوی به دعوت رسمی دولت چین به این کشور سفر کرد؛ سفری تاریخی و بی‌سابقه که در اوج جنگ سرد، نماد دیپلماسی بی‌طرفانه ایران بود
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/11232" target="_blank">📅 20:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11231">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آیا درباره حمایت چین از ایران با رئیس جمهور چین صحبت کردید؟  ترامپ: ما در مورد این موضوع صحبت کردیم. منظورم اینه که وقتی میگید «حمایت»، آنها با ما جنگ نمی‌کنن یا چیزی شبیه این. او گفت که تجهیزات نظامی ارائه نخواهد کرد، این یک بیانیه بزرگه. اما در عین حال گفت…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/11231" target="_blank">📅 19:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11230">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/11230" target="_blank">📅 19:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11229">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">«دریادار برد کوپر»، فرمانده سنتکام:  «فرماندهی مرکزی ایالات متحده (سنتکام) مستقیماً در پاسخ به تهدیدهایی که جمهوری اسلامی ایران ایجاد می‌کرد، تأسیس شد.  رژیم ایران طی ۴۷ سال گذشته منطقه را دچار هراس و بی‌ثباتی کرده و دشمنی با آمریکا را به یکی از اصول اساسی…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11229" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11228">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/11228" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11227">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗦𝗨𝗦</strong></div>
<div class="tg-text">خسته نباشی یاشار
نظرت راجب سیم‌کارت پرو چیه به مردم عادی هم دارن میدن الان</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/11227" target="_blank">📅 18:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11226">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">لطفا عکس از اس ام اس هایی که رژیم میده برام نفرستید ! خیلی خوشم میاد ! اگه قرار‌باشه هر روز اونا اس ام اس بدن شمام همتون اسکرین بفرستین که نمیشه ! به هیچ عنوان اسکرین ندید دیگه مخصوصا ‌جانفدا رو … مرسی اه</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/11226" target="_blank">📅 18:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11225">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ: رهبر چین پیشنهاد کمک در مورد مسئله ایران را داد
او قول داد که تجهیزات نظامی به آنها منتقل نکند.
او می‌خواهد تنگه هرمز باز بماند.
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/11225" target="_blank">📅 18:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11224">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سناتور کنگره خطاب به برد کوپر:
برجام توانایی هسته ای ایران رو محدود میکرد ولی ترامپ پاره کرد، الان وارد یه جنگ بی‌پایان شدیم، آیا ترامپ هیچ وقت به شما نگفت چرا برجام رو پاره کرد؟
کوپر فرمانده سنتکام:
خانم سناتور زمانی که این ۸ سال پیش اتفاق افتاد من یک سمت دیگه داشتم! من سیاستمدار نیستم و نمیتونم جواب این سوال رو بدم!
@withyashar</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/withyashar/11224" target="_blank">📅 18:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11223">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e028b3e623.mp4?token=eKZes5MJDD9xhF7sj-InVyXMAtDiLGCIImg0lJQQsS1aDkCbbPL63ny1P5LLC2BXKf7E_GiD3QlMVEF0VCaU07ssGmClfpv-czaI7nXwD00Qznj4Gvt5SUUgedb7ts805UCdruL2_YlzmiUbRCqkCa0LPbWaOmFsvFF3_-6oHxB7bJV4GZCZipiS61HE5Y7PEx2vG4MojejiufSJCPasUwaAi2CDRxIy_G7tvTiGT7veaR9cgOLb3Uojc_ZI1CRKxtrBCtWx6iS_M9zmemtoAyKoE_W0ba5iZt31Xt-ndXCgoGTfBWamOhRhRSsG_EBJPKZHzE2n30HrGLcCErpCsYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e028b3e623.mp4?token=eKZes5MJDD9xhF7sj-InVyXMAtDiLGCIImg0lJQQsS1aDkCbbPL63ny1P5LLC2BXKf7E_GiD3QlMVEF0VCaU07ssGmClfpv-czaI7nXwD00Qznj4Gvt5SUUgedb7ts805UCdruL2_YlzmiUbRCqkCa0LPbWaOmFsvFF3_-6oHxB7bJV4GZCZipiS61HE5Y7PEx2vG4MojejiufSJCPasUwaAi2CDRxIy_G7tvTiGT7veaR9cgOLb3Uojc_ZI1CRKxtrBCtWx6iS_M9zmemtoAyKoE_W0ba5iZt31Xt-ndXCgoGTfBWamOhRhRSsG_EBJPKZHzE2n30HrGLcCErpCsYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«دریادار برد کوپر»، فرمانده سنتکام:
«فرماندهی مرکزی ایالات متحده (سنتکام) مستقیماً در پاسخ به تهدیدهایی که جمهوری اسلامی ایران ایجاد می‌کرد، تأسیس شد.
رژیم ایران طی ۴۷ سال گذشته منطقه را دچار هراس و بی‌ثباتی کرده و دشمنی با آمریکا را به یکی از اصول اساسی حاکمیت خود تبدیل کرده است.
سابقه خصمانه و مرگبار آنها علیه ایالات متحده کاملاً مستند و ثبت‌شده است
@withyashar</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/withyashar/11223" target="_blank">📅 18:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11222">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آیا درباره حمایت چین از ایران با رئیس جمهور چین صحبت کردید؟
ترامپ: ما در مورد این موضوع صحبت کردیم. منظورم اینه که وقتی میگید «حمایت»، آنها با ما جنگ نمی‌کنن یا چیزی شبیه این. او گفت که تجهیزات نظامی ارائه نخواهد کرد، این یک بیانیه بزرگه. اما در عین حال گفت که آنها مقدار زیادی نفت خودشون رو از ایران میخرن و دوست دارن این کار رو ادامه بدن.
@withyashar</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/11222" target="_blank">📅 18:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11221">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">برد کوپر فرمانده سنتکام مدعی شد:
توانمندی‌های موشکی، دریایی، پهپادی و صنعتی ایران 90 درصد تضعیف شده است. او افزود که نیروی دریایی ایران تا یک نسل دیگر نیز به سطحی که پیش از جنگ در اختیار داشت باز نخواهد گشت
@withyashar</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/11221" target="_blank">📅 18:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11220">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca974d01b.mp4?token=Kzb8u3kzXVeYZlCU0Cp3gjhK941OxS3P-q7tYfwAFETa0HhjvFk-UINAXbjsCwXWweJnUrCyqyur019aW2LJ8MPgbJYTR_jgPCxEB5k6TC1LB6mLHLTCsrlvgyzvPHg32gyEohPK-6A4C6Fks9o0Yn4_RhocOXKwCeyrk6bmTjfLfDPA4_TH9pB6xpSiBQy_1Hi5tx_wAqxRGyU_-hMJo-AAJTpeszmzEjpA8ISCl8P4gxvr7XWGxuTWKsp6wCgr6XkLgbI-CM7TtS2iaoZJMpbN6adRlY-4senYjO_q9O7OVrg7lF3XR8d8PNuNBDFCfORFe5lXGRJkPjKV5Sk67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca974d01b.mp4?token=Kzb8u3kzXVeYZlCU0Cp3gjhK941OxS3P-q7tYfwAFETa0HhjvFk-UINAXbjsCwXWweJnUrCyqyur019aW2LJ8MPgbJYTR_jgPCxEB5k6TC1LB6mLHLTCsrlvgyzvPHg32gyEohPK-6A4C6Fks9o0Yn4_RhocOXKwCeyrk6bmTjfLfDPA4_TH9pB6xpSiBQy_1Hi5tx_wAqxRGyU_-hMJo-AAJTpeszmzEjpA8ISCl8P4gxvr7XWGxuTWKsp6wCgr6XkLgbI-CM7TtS2iaoZJMpbN6adRlY-4senYjO_q9O7OVrg7lF3XR8d8PNuNBDFCfORFe5lXGRJkPjKV5Sk67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک و پسرش  «اِکس اَش اِی-توئلو» «X Æ A-Xii» در پکن
@withyashar</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/withyashar/11220" target="_blank">📅 18:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11219">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فرمانده سنت‌کام: ظرف کمتر از ۴۰ روز می‌توانیم به اهدافمان در ایران دست پیدا کنیم
@withyashar</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/11219" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11218">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نتانیاهو، نخست‌وزیر، و گیدعون سعر، وزیر خارجه، به مقامات دستور داده‌اند تا مقدمات طرح شکایت افترا علیه نیویورک تایمز را آغاز کنند.
این شکایت به دلیل انتشار یادداشتی از نیکلاس کریستوف که شامل اتهاماتی مبنی بر سوءاستفاده جنسی از فلسطینیان در زندان‌های اسرائیل بوده،
مقاله کریستف با عنوان «سکوتی که تجاوز به فلسطینیان با آن روبرو می‌شود» روز دوشنبه ۱۱ مه در نیویورک‌تایمز منتشر شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/11218" target="_blank">📅 18:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11217">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rk8mS669ytDWWFGOzAUSKR0q2Q-fJzLnYWVnIeQsgyOfXh0d66WL2L3cI7PZgc3vAmshxhLdQrTgok1jOmru-aXfNX95IZNQkE7OSHdYW0KYSoqUaCwMMBGb89ReCD7NRoqFbhNCeG0OGTwQMGZQo7vQbxaY9EIgwLXSvdWw7ZPXqI6faSwWBL7iBbMdpgqJKapwSLeL8SVePqzCpuNk7JxnVRPT1N6Au4IE9g3kuUFRjmoo2Ru2DuC_C73KysAYesxIdX1W2YZ3cEllrnJTu4LQcttkzslYAxpNb7fm_C7rWHdAPS_Xk6Ydv1invFFjmB_Z8KYeDI4_S1GRTQ4Gzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">INDOPACOM
، فرماندهی نظامی آمریکا برای منطقهٔ «هندو-پاسیفیک»ایندوپکام: تفنگداران دریایی ایالات متحده، واحد یازدهم اعزامی تفنگداران دریایی، در حال انجام تیراندازی رزمی بر روی ناو جنگی یو اس اس کامستاک (LSD 45) در اقیانوس هند هستند. واحد یازدهم اعزامی دریایی، که بر روی گروه آماده آبی-خاکی باکسر(USS BOXER) مستقر شده است، یک نیروی پایدار و قابل اعتماد رزمی است که به بازدارندگی و واکنش به بحران در منطقه عملیاتی ناوگان هفتم ایالات متحده کمک می‌کند.
@withyashar
یاشار: ساده بگم ناو باکسر وسط راه مونده داره تمرین میکنه و معلوم نیست کی بیاد !</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/11217" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11215">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d789d55b5d.mp4?token=h10bCR6bIIMerL24qgU-k5xaSWnzZ6YaQoOVJ9G-fyDSYp19znioXIDnAhFc7x5Jh0U8F7a2dpCzql3FD2KeP9Z1709EZ81Wfkvt0m87_MldDobCxMUbOHVP4EsqFzOuqj_OsiTtCi2GYY5UujQJYbqtyHpcVzsHTlQrJpu4QkbXdftQoPb4DXzLtYZs8cFT6AyFtP0lhtQTKXupOcLjE24h1d6IB3_Bate2cPbX31acvMogIVQ2ffJqwxeaKYgHpi4X2oL1ReNfb2rtvfYnwXLNoknY3y4uZ0ttNFdDWCuomQyFHWJHQ544uh436HyRfDsOiWUu81rxgfwLZqV02A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d789d55b5d.mp4?token=h10bCR6bIIMerL24qgU-k5xaSWnzZ6YaQoOVJ9G-fyDSYp19znioXIDnAhFc7x5Jh0U8F7a2dpCzql3FD2KeP9Z1709EZ81Wfkvt0m87_MldDobCxMUbOHVP4EsqFzOuqj_OsiTtCi2GYY5UujQJYbqtyHpcVzsHTlQrJpu4QkbXdftQoPb4DXzLtYZs8cFT6AyFtP0lhtQTKXupOcLjE24h1d6IB3_Bate2cPbX31acvMogIVQ2ffJqwxeaKYgHpi4X2oL1ReNfb2rtvfYnwXLNoknY3y4uZ0ttNFdDWCuomQyFHWJHQ544uh436HyRfDsOiWUu81rxgfwLZqV02A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشیT1 "ترامپ موبایل" بعد از نزدیک
یه سال تأخیر بالاخره داره عرضه میشه
یه گوشی طلایی ۴۹۹ دلاری با برند ترامپه که
چیپ اسنپدراگون سری ۷، رم ۱۲ گیگ، حافظه
۵۱۲ گیگ و دوربین سه‌گانه ۵۰ مگاپیکسلی دارهبه نظر میاد در اصل یه گوشی ساخت چین باشه که فقط مونتاژ نهاییشو تو آمریکا انجام دادن
@withyashar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/11215" target="_blank">📅 16:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11214">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مارکو روبیو : ترامپ موضوع ایران رو با چین مطرح کرد و این خیلی مهم بود
طرف چینی گفت ما موافق نظامی‌کردن تنگه هرمز نیستیم
با سیستم عوارض‌گیری هم مخالفیم، و این موضع ما هم هست
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/11214" target="_blank">📅 16:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11213">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزیر خزانه داری آمریکا:ایران رو انقدر تحت فشار اقتصادی قرار دادیم که توی پرداخت حقوق نیروهاشم به مشکل خورده. دارن نفسای آخرشونو میکشن
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/11213" target="_blank">📅 16:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11212">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c931f479b.mp4?token=iOaNZ98oGEPxdvUyy5LFrn3YBdADWRNtSB22ExecM4rxXfkfsV_0hwDQXL02Oy7aqgBVQttQI6-2swRC-HU7z6Q62z5s9nRhszPmprdT_trANymrp3fLvbEK1VW_pfufHAFewov4w3VgMsozqYzHsUB0U-KQ6lIginnCwEcu7TCHStpZQt9gdRQj-duepNQ18qm5ZsyH7ZH57hX5-ScYj5Ou_fXlUCy6yZOoqkvCkA0vJimvpdtjDp5BCiFkUF8djtA6Pk0mkQB9kBZLGyl5ObVl7ghcfzC0k9cYhvoB87qlCsHUtWPE0ap52npZS3HKq_p8pawk04fCPcaPOzcHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c931f479b.mp4?token=iOaNZ98oGEPxdvUyy5LFrn3YBdADWRNtSB22ExecM4rxXfkfsV_0hwDQXL02Oy7aqgBVQttQI6-2swRC-HU7z6Q62z5s9nRhszPmprdT_trANymrp3fLvbEK1VW_pfufHAFewov4w3VgMsozqYzHsUB0U-KQ6lIginnCwEcu7TCHStpZQt9gdRQj-duepNQ18qm5ZsyH7ZH57hX5-ScYj5Ou_fXlUCy6yZOoqkvCkA0vJimvpdtjDp5BCiFkUF8djtA6Pk0mkQB9kBZLGyl5ObVl7ghcfzC0k9cYhvoB87qlCsHUtWPE0ap52npZS3HKq_p8pawk04fCPcaPOzcHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز درباره ایران:
ماموریت ما کامل نشده است.ما برای احتمال اینکه ممکن است مجبور شویم دوباره اقدام کنیم - شاید حتی به زودی - آماده‌ایم. اگر اهداف تأمین نشوند، دوباره اقدام خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/11212" target="_blank">📅 15:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11211">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TioVXq-OeP-Ymnk9H6gizzrBMYqCfIPWkO5_5pIzrDj9CCxxphF62pDibaYUxdM6tAKLRTt0UgVpkNBY5CVCPlye1VF-vWPeDU2EA--GhxZUK-LI1wlE_6I3Y_bdeIUwjEOynGlcLql_r2psYIB51ksASzWEnWEsmgGfT9kqzuDo-eLfcc2aQvvsDnBLtk6xgod7sE7YENmss0N7Schfgnb-Hgfcyy3IM9fnf_XldDN7nzCJQiXB608vo2EL4_ftP36ufukJ1WgT79YMArCXmyAs36gAc81hFSZGNf81C4F0q4sgTe45kkW7Q15jB8-uzV4pPbSvxgX95Fx5QNKnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلفی لی جون، بنیانگذار و مدیرعامل شیائومی با ایلان ماسک
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11211" target="_blank">📅 14:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11210">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الجزیره: چین با آمریکا در مورد ایران انعطاف دارد، اما در مورد تایوان نه
مسئولان چینی پیام واضحی به ایالات متحده ارسال کرده‌اند:
چین در بسیاری از مسائل مانند ایران، تجارت و فناوری آماده انعطاف و پذیرش اختلاف نظر است، اما در یک موضوع حساس، انعطاف‌پذیر نیست و آن تایوان است.
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11210" target="_blank">📅 14:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11209">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda0441500.mp4?token=CWvbOoAwh6EYgGl5AJ0Bb9mg5sjWZzuboh23xrFXiW884tZtoCePyY9RGyD7iyeTmFk1eqPWSXCkZ_vaxyjwK0wCKa-X6tiD0_II5ir7Epk4YNZyn7qP72ip_AxK8oNvLtGJVJbWMT73gVFp4AP8Nmnwxi7qck4neXNAYJ15ZrDnN-6VxVnoYHjTlIin6-E1e7I7HYYlRQF-Jedh48subnc_VT9SzJdYpXCC7_GluSXxhQug3xIRQkJT_wNEl_0zdZ23iV-vqI9ZkG4IrT3T57Zxgh41iJW7IdjwmSJTGGtaFkMV65wlLAmt-sU5wSxukulIMY1naw1a_NEPdiok2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda0441500.mp4?token=CWvbOoAwh6EYgGl5AJ0Bb9mg5sjWZzuboh23xrFXiW884tZtoCePyY9RGyD7iyeTmFk1eqPWSXCkZ_vaxyjwK0wCKa-X6tiD0_II5ir7Epk4YNZyn7qP72ip_AxK8oNvLtGJVJbWMT73gVFp4AP8Nmnwxi7qck4neXNAYJ15ZrDnN-6VxVnoYHjTlIin6-E1e7I7HYYlRQF-Jedh48subnc_VT9SzJdYpXCC7_GluSXxhQug3xIRQkJT_wNEl_0zdZ23iV-vqI9ZkG4IrT3T57Zxgh41iJW7IdjwmSJTGGtaFkMV65wlLAmt-sU5wSxukulIMY1naw1a_NEPdiok2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان لوله لول سر میز شمام
😂
@withyashar</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/11209" target="_blank">📅 14:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11208">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
تأسیسات اصلی بارگیری نفت ایران به مدت ۳ روز است از سرویس خارج شده است
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/11208" target="_blank">📅 14:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11207">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرنگار صداوسیما به نقل از نیروی دریایی سپاه: از شب گذشته تاکنون ۳۰ فروند کشتی از تنگه هرمز با مجوز ایران عبور کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/11207" target="_blank">📅 14:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11206">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شی جین‌پینگ: چین و ایالات متحده هر دو از همکاری سود می‌برند و از تقابل زیان می‌بینند.
دو کشور ما باید شریک باشند نه رقیب.
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11206" target="_blank">📅 14:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11205">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ از رئیس‌جمهور چین برای سفر به ایالات متحده در ماه سپتامبر آینده دعوت کرد
@withyashar</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/11205" target="_blank">📅 14:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11204">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آکسیوس: یکی از گزینه‌های ترامپ پس از بازگشت از چین از سر گیری پروژه آزادی در تنگه هرمز است. گزینه دیگر  ترامپ حمله به زیرساخت‌های ایرانه.
@withyashar</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/11204" target="_blank">📅 14:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11203">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">طبق برنامه ای که قرار داده بودیم   ترامپ و رییس‌جمهور چین برای یک مهمانی شام با یکدیگر دیدار کردند @withyashar</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/11203" target="_blank">📅 14:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11202">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24c3a9a1e.mp4?token=D77iC7cbQMcVQkC30eCC4V7Ccgt46pPrKeS6OVV41mkR5zIDfcUQoPBcWs9yTzwCSvdevsbmxrX9P3WaMPbW8TqsTb7QoiLvEMc7lktKzO_IcMNcJD6eeW0qXlRinLntP9Ls5HvuHJksaSr7aX3qWF0__QFsymXEPIGYvhiczO4n-fydydxi5MXEQlJfhcQK916vpRYxWtKHK36bCOHJvSmo7QMs84mfCroDrfPmJ6_OBAXq1y1lG3gjLAEJyGAoFBiMM-Fo8Kph4c05h8wLZB7FBojAEfwumXA4jKnG2FHeWcZ7FuKA5FOGmZp10nq3UhfkQCTxWCxeF19gg50ozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24c3a9a1e.mp4?token=D77iC7cbQMcVQkC30eCC4V7Ccgt46pPrKeS6OVV41mkR5zIDfcUQoPBcWs9yTzwCSvdevsbmxrX9P3WaMPbW8TqsTb7QoiLvEMc7lktKzO_IcMNcJD6eeW0qXlRinLntP9Ls5HvuHJksaSr7aX3qWF0__QFsymXEPIGYvhiczO4n-fydydxi5MXEQlJfhcQK916vpRYxWtKHK36bCOHJvSmo7QMs84mfCroDrfPmJ6_OBAXq1y1lG3gjLAEJyGAoFBiMM-Fo8Kph4c05h8wLZB7FBojAEfwumXA4jKnG2FHeWcZ7FuKA5FOGmZp10nq3UhfkQCTxWCxeF19gg50ozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه های ترامپ با حاکم چین به این ترتیبه : مراسم استقبال تو تالار بزرگ خلق چهارشنبه رسیدن به پکن ، استقرار و استراحت پنج شنبه ۱۴ مه - ملاقات با شی - ضیافت دولتی با شی  جمعه تاریخ ۱۵ مه - جلسه عکس با شی- چای با شی - ناهار با شی و حرکت از پکن به آمریکا، @withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/11202" target="_blank">📅 14:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11201">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/11201" target="_blank">📅 14:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11200">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فارس:
عبور کشتی‌های چینی از تنگۀ هرمز از شب گذشته اغاز شده
@withyashar
یک کشتی ژاپنی هم اجازه عبور گرفت</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/withyashar/11200" target="_blank">📅 14:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11199">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کاخ سفید اعلام کرد در دیدار ترامپ و شی جین‌پینگ، دو طرف بر باز ماندن تنگه هرمز و تقویت همکاری‌های اقتصادی توافق کردند. این توافق شامل افزایش سرمایه‌گذاری چین در صنایع آمریکا و گسترش دسترسی شرکت‌های آمریکایی به بازار چین است.
ترامپ: مذاکرات پکن بسیار مثبت و سازنده بود
@withyashar</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/11199" target="_blank">📅 14:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11198">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">با رفیق اروپاییم نشستیم داریم ویدیو مسیج های شما رو نگاه میکنیم براش ترجمه میکنم که داری چی میگی، بعد یهو میگه اینجا چی گفت، خب من چجوری گربه گیر رو ترجمه کنم
😂
😂
😂
😂
😂
عشقی سلطان یاشار
❤️
❤️</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/withyashar/11198" target="_blank">📅 13:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11197">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdi</strong></div>
<div class="tg-text">با رفیق اروپاییم نشستیم داریم ویدیو مسیج های شما رو نگاه میکنیم براش ترجمه میکنم که داری چی میگی، بعد یهو میگه اینجا چی گفت، خب من چجوری گربه گیر رو ترجمه کنم
😂
😂
😂
😂
😂
عشقی سلطان یاشار
❤️
❤️</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/withyashar/11197" target="_blank">📅 13:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11196">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e51a90e1f.mp4?token=OZwlWylsLjq1EhRwvI2p6pT5-6oDx_tT5UmgxKR_SMzrbTHiGU1GfbccfOKGZckXa2gQX5wKTCbpsTlFPY-eXZOONe6T8zLgfIB0oqJwLFF9Mi61-C9ISvJ2nqXi-nqG7X3MuHLICcqJECq8JEmqtdAsSKaZ1JJViIfBgbSWXQao05h68OqtP8pGvheRnAdCc4tVerx4ilMV7Qa3letJ-i3KYrvGWwH3ATdjg7Vwyrnz9O0Hj-TB42TKTPt9fN-MwNsou7BdFv7qijZgXqYNzm4E2sBXc40nMIMKZCXzzxhymF41_dmmpBD9ZcbvMkKnbe3Blj0-qXHxMh8cb25pJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e51a90e1f.mp4?token=OZwlWylsLjq1EhRwvI2p6pT5-6oDx_tT5UmgxKR_SMzrbTHiGU1GfbccfOKGZckXa2gQX5wKTCbpsTlFPY-eXZOONe6T8zLgfIB0oqJwLFF9Mi61-C9ISvJ2nqXi-nqG7X3MuHLICcqJECq8JEmqtdAsSKaZ1JJViIfBgbSWXQao05h68OqtP8pGvheRnAdCc4tVerx4ilMV7Qa3letJ-i3KYrvGWwH3ATdjg7Vwyrnz9O0Hj-TB42TKTPt9fN-MwNsou7BdFv7qijZgXqYNzm4E2sBXc40nMIMKZCXzzxhymF41_dmmpBD9ZcbvMkKnbe3Blj0-qXHxMh8cb25pJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/11196" target="_blank">📅 13:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11195">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار : جابجای‌های غول آسا دو شماره یک «AirForce1» هواپیمای ویژه ریاست جمهوری و «B1 »بمب افکن اسطورهی آمریکا و خبر ویژه از داخل ایران  https://www.instagram.com/reel/DYQCr39RJ4i/?igsh=MThycjJiYWZmbnJ3dA==  کارای اداریش رو انجام بدید تا بعدش بریم…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/11195" target="_blank">📅 13:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11194">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آکسیوس به نقل از مقامات اسرائیلی:
در پی احتمال تصمیم ترامپ برای از سرگیری جنگ، در اسرائیل حالت آماده‌باش حداکثری در طول تعطیلات آخر هفته برقرار خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/11194" target="_blank">📅 13:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11193">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک مقام کاخ سفید به فاکس‌نیوز:
رئیس‌جمهور چین علاقه‌مند است نفت بیشتری از آمریکا خریداری کند تا وابستگی کشورش به تنگه هرمز را کاهش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/11193" target="_blank">📅 13:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11192">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جان بولتون: مذاکره با ایران برای یک توافق هسته‌ای هدر دادن اکسیژن است.
این افراد دهه‌ها پیش تصمیم استراتژیکی برای دستیابی به سلاح‌های هسته‌ای گرفتند و در این ۴۷ سال هیچ مدرکی وجود ندارد که نشان دهد آن‌ها این هدف را رها کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/11192" target="_blank">📅 13:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11191">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f2c74f17.mp4?token=ltYMt0bMON4iQrCniafuH8wJmRsI3boJC7JTDhSUcFy1LqoW4BOJ0fheNXfq2E421bOX_uf5fXTZkts45alUr012ocgP9xB4TvIuGMQN3CEgTzsa-Exd-eb62daUO3gO7jKJJh8me_WdOwLNDNX3YGooxK7ui1onaktj5mPzIuRpCHR_8uqHFgyRi4of8ECdr2VayCViDoqZpU_S_KUkAX4xa8wZPzmLOsn0tsBYMQ8ZQFkkZrzKf-jwt02p6ylL7L27NOEpSOqgLJufZB7W-_RnAZUBYW67orENPgzDJykMPXpD1UXgYtUzl86ECUaVFHpn9TfEZsq9IjVnj6Yl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f2c74f17.mp4?token=ltYMt0bMON4iQrCniafuH8wJmRsI3boJC7JTDhSUcFy1LqoW4BOJ0fheNXfq2E421bOX_uf5fXTZkts45alUr012ocgP9xB4TvIuGMQN3CEgTzsa-Exd-eb62daUO3gO7jKJJh8me_WdOwLNDNX3YGooxK7ui1onaktj5mPzIuRpCHR_8uqHFgyRi4of8ECdr2VayCViDoqZpU_S_KUkAX4xa8wZPzmLOsn0tsBYMQ8ZQFkkZrzKf-jwt02p6ylL7L27NOEpSOqgLJufZB7W-_RnAZUBYW67orENPgzDJykMPXpD1UXgYtUzl86ECUaVFHpn9TfEZsq9IjVnj6Yl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از ۵۰ سال، اولین رئیس‌ جمهوری شد که به معبد آسمان چین رفت
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/11191" target="_blank">📅 12:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11190">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کاخ سفید : ترامپ و شی توافق کردن که تنگه هرمز باید باز بمونه
@withyashar</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/withyashar/11190" target="_blank">📅 12:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11189">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7505bc627.mp4?token=E5sJ8IY79twftZbAObRN9Hwwo1T1osPtx-H8hAseBw8dBulLFs4-RUaFpSlVnmaZVFGiNUojBCkoPWZgdCE5opCqO-GkCcTG0l762-GO1YbPwT2bzNQpQqDfQvpSU23Vo6kP14EneqNpUVL64DGxLsnIJAgf1SZapqr_fVN9syVbL7Sl2BMm3iZv7UFsaPquWXpUvMeJHeaTIIsuyWz4AbQpBFe4AIyQMvrRDu74YsCP-M150T8JQBorwvbLPfIuj_-ioqw9jdrh9gBAieRybkmBTrmz8JfNPWWOcSN0p2JinyGxNSYhfyhQTi2zkisxoj9QC4NGxrOS_35fSOdODA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7505bc627.mp4?token=E5sJ8IY79twftZbAObRN9Hwwo1T1osPtx-H8hAseBw8dBulLFs4-RUaFpSlVnmaZVFGiNUojBCkoPWZgdCE5opCqO-GkCcTG0l762-GO1YbPwT2bzNQpQqDfQvpSU23Vo6kP14EneqNpUVL64DGxLsnIJAgf1SZapqr_fVN9syVbL7Sl2BMm3iZv7UFsaPquWXpUvMeJHeaTIIsuyWz4AbQpBFe4AIyQMvrRDu74YsCP-M150T8JQBorwvbLPfIuj_-ioqw9jdrh9gBAieRybkmBTrmz8JfNPWWOcSN0p2JinyGxNSYhfyhQTi2zkisxoj9QC4NGxrOS_35fSOdODA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز با حیرت : داداش بزرگه نگات میکنه ، لبخند بزنید شما با دوربین ها رصد میشوید
خبرنگار فاکس‌نیوز گزارش داد که خودروی آن‌ها در چین تنها دو دقیقه در محدوده «توقف ممنوع» پکن ایستاد و بلافاصله پیامک جریمه ۴۰ دلاری برای راننده صادر شد. به گفته او، در این کشور دوربین‌های نظارتی همه‌جا فعال هستند و تخلفات رانندگی در لحظه ثبت و اعمال می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11189" target="_blank">📅 12:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11188">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هند: حمله به یک کشتی ما در نزدیکی
سواحل عمان غیرقابل قبول است
یک کشتی هندی توسط افراد ناشناس دزدیده شده و به سمت ایران اسکورت میشود
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11188" target="_blank">📅 12:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11187">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بر اساس داده ها , شرکت تتر مبلغ 344 میلیون دلار USDT مرتبط با بانک مرکزی ایران رو فریز کرده و دلیلش هم بخاطر دور زدن تحریم‌ها بوده که شرکت آرکهام کیف پول‌های مرتبط رو شناسایی کرده
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11187" target="_blank">📅 12:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11186">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تسنیم: کیفرخواست زیباکلام و مدیرمسئول خبرگزاری آنا صادر شد ممنوعیت زیباکلام از انجام هرگونه فعالیت رسانه‌ای به مدت سه ماه صادر شده
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/11186" target="_blank">📅 11:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11185">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H258GsuavMkjie5tX1GNQCkUi5Zx0jd1EyxJGAn95EDg7aWGOLfLvbP2O6qIm1LHXqqoQprj_RiS2NOfPEl8KMNDmxNM6ytqU--1iZwAWemyrahzSXh_O8xFreq8F82xaTdGCwbl-1ZNvfxO5cU2zoDOC_ag42aIbZKUpmjuO-wB7XxX5chgIOLRq2GaALB4ozU4x-lRWlJP2YXc_fjZ_dgxYDutoWgkEHQuZ7M1Av1yi64Xi1evfC7C7hClZXpmeTDDBq7e8Bd37upYhLFo41zpGg9QKEuvlRynljLOo0rYueXisIhQXep9HCTq_JJ-PhhesYm2neCkXCZBf0bJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقایقی پیش زمین‌لرزه‌ای بسیار شدید
۵ ریشتری در عمق ۸ کیلومتری بردسیر کرمان را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11185" target="_blank">📅 11:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11184">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو در دادگاه حظور پیدا کرد و گفت: «فیک نیوزها گفتند من به بیماری لاعلاجی مبتلا هستم - این یک صنعت دروغگویی تمام‌عیار است»
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11184" target="_blank">📅 11:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11183">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تاج : در جریان آهنگی که معین برای تیم ملی در جام جهنی ۲۰۲۶ می خواند هستیم  @withyashar</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/11183" target="_blank">📅 11:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11182">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اتاق جنگ با شما : زمین لرزه خیلی شدید کرمان یک دقیقه پیش
@withyashar</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/11182" target="_blank">📅 11:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11181">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ed5af14a6.mp4?token=N3TX0qz2UmzqbTRZ7g5k_fWq-rXoTZulOnFHvZqF7pTlN3nHmVT6bIj4CiuYfakIOKR7kXR-V733x38H-D1P0VN8hq2zizZfmK0gqJBC5uTavQV6Fh2rzQtVB5-c6Qa6HgTCdCE3_mxcvkDUMs9a595JZfg6NZjm9BpYXEd72u8TIaWpCBCqItHp-w9rxRUZQOAWW2mLiSxXgKDD9KGXx1lsybckSjAWQT--85kSDa9DT36al0EXzf30U49RzAnKi0VXf4T74F6oHNFpLPU1Eqj1eAPs9L6da05EW9wAaeVfzuNf1V7tXyFFICnmv_vTLho5EYGEDXhRceCEwBnyOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ed5af14a6.mp4?token=N3TX0qz2UmzqbTRZ7g5k_fWq-rXoTZulOnFHvZqF7pTlN3nHmVT6bIj4CiuYfakIOKR7kXR-V733x38H-D1P0VN8hq2zizZfmK0gqJBC5uTavQV6Fh2rzQtVB5-c6Qa6HgTCdCE3_mxcvkDUMs9a595JZfg6NZjm9BpYXEd72u8TIaWpCBCqItHp-w9rxRUZQOAWW2mLiSxXgKDD9KGXx1lsybckSjAWQT--85kSDa9DT36al0EXzf30U49RzAnKi0VXf4T74F6oHNFpLPU1Eqj1eAPs9L6da05EW9wAaeVfzuNf1V7tXyFFICnmv_vTLho5EYGEDXhRceCEwBnyOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویربرداری عجیب یا اسکن ۳۶۰ ایلان ماسک از موقعیت با گوشی خودش
@withyashar</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/withyashar/11181" target="_blank">📅 11:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11180">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2386995c2e.mp4?token=avvsT6Qc5sPoGiNh59fn7l_vsIoJjQMyTrGrPg3lr58Jpf1gKIMW_abjGdBAY40XbaxIYRfIS4mv71_qFuYyUpeUrlJ_hZEh40fGErxDwaloNyzev1VefjKVNbhuFEmi_2l_PwKIAY2Mg_G3AuljlKleFN8Uo-gknN20xcX-ihkQ7OmAu4QcojapN-BB-ks8ZDRkrzmd4O5rFYi85sRUBjdYub4P_nWVnDF_27BtfurR_WaJVqv7wMXDH5FnIS8ST1M4ORD3oQPlrbhqvBWMg7ts8ZCwlPiZRaCDoP5YNhkM2FnEEF2zECB2veS8tpKiZAX707vwnmtSN0j66tEUnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2386995c2e.mp4?token=avvsT6Qc5sPoGiNh59fn7l_vsIoJjQMyTrGrPg3lr58Jpf1gKIMW_abjGdBAY40XbaxIYRfIS4mv71_qFuYyUpeUrlJ_hZEh40fGErxDwaloNyzev1VefjKVNbhuFEmi_2l_PwKIAY2Mg_G3AuljlKleFN8Uo-gknN20xcX-ihkQ7OmAu4QcojapN-BB-ks8ZDRkrzmd4O5rFYi85sRUBjdYub4P_nWVnDF_27BtfurR_WaJVqv7wMXDH5FnIS8ST1M4ORD3oQPlrbhqvBWMg7ts8ZCwlPiZRaCDoP5YNhkM2FnEEF2zECB2veS8tpKiZAX707vwnmtSN0j66tEUnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه ای زیبا در چین که کودکان به ترامپ و شی خوشامد میگویند
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/11180" target="_blank">📅 11:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11179">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38a96c0966.mp4?token=mFVRrMy6JJLS61iHNZh3PgLMCdzPlRQeD6OgLZtopsB8K7CjiHZ8w8BQGa8cduQhiSI8aRzdc7gi5nem4JAH60gDBxceCnurR3uV5bvVFgagqOz0gatXvrLV_PZp6GMIH5L3lguTAR5zcT31SYgwcmxqXVDFUzTtYhmBPEk9cvWoaY7k0W9gbG3yP69pT_NNjSFTrtwo0MjIVxK2_vGZNQLm3FraAMoZXnSpdRPkJl3qdAGXmJgwYXOhLlaQHd1oWEPUXdIXYlfsY_LlmSwzK66oYTy-Fh-sHKA5GleLvwzjpbi58UncVHQ9nvizU_QjWQqCb-Fvy4BA7IJlLj7xoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38a96c0966.mp4?token=mFVRrMy6JJLS61iHNZh3PgLMCdzPlRQeD6OgLZtopsB8K7CjiHZ8w8BQGa8cduQhiSI8aRzdc7gi5nem4JAH60gDBxceCnurR3uV5bvVFgagqOz0gatXvrLV_PZp6GMIH5L3lguTAR5zcT31SYgwcmxqXVDFUzTtYhmBPEk9cvWoaY7k0W9gbG3yP69pT_NNjSFTrtwo0MjIVxK2_vGZNQLm3FraAMoZXnSpdRPkJl3qdAGXmJgwYXOhLlaQHd1oWEPUXdIXYlfsY_LlmSwzK66oYTy-Fh-sHKA5GleLvwzjpbi58UncVHQ9nvizU_QjWQqCb-Fvy4BA7IJlLj7xoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آقای رئیس‌جمهور، مذاکرات چطور بود؟
ترامپ : عالی بود. چین زیباست.
خبرنگار: دربارهٔ تایوان هم صحبت کردید؟
ترامپ: (پاسخی نداد)
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/11179" target="_blank">📅 10:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11178">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مارکو روبیو تایید کرد چین و آمریکا به توافق رسیدن که ایران نباید تو تنگه عوارض بگیره از کشوری
این «توافق» فعلاً در حد موضع مشترک سیاسی و دیپلماتیک گزارش شده، نه یک پیمان رسمی یا قطعنامه بین‌المللی.
چین هنوز در بسیاری از موضوعات از ایران فاصله نگرفته و حتی در شورای امنیت بعضی قطعنامه‌های ضد ایران را وتو کرده است.
دلیل حساسیت موضوع این است که حدود یک‌پنجم نفت جهان از تنگه هرمز عبور می‌کند و هرگونه عوارض یا محدودیت می‌تواند قیمت جهانی انرژی را به شدت تحت تأثیر قرار دهد
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/11178" target="_blank">📅 03:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11177">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">@withyashar
سفر قاهره</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/11177" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11176">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قصه بگم ؟ شایدم بهترین شرحی ‌باشه که لازم دارید بشنوید …</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/11176" target="_blank">📅 02:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11175">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/11175" target="_blank">📅 01:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11174">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29e07a01.mp4?token=rNn3-uvVFCSPlxrtwLrvLM2maChJoKKbQiMVJtmCZG3tD_K5cIeUismu7NPQN7_zcsiWKn_zDb7sVdwjpAUtsA2MnqlLVNTWidtwltM5gWULAbKE_rNOPJXnpgecrHALidDxZ1nsRPky0BvawdULBzvfL3yF6TOpdkrIr0oQzu1wLlHEzVq7Fa_EuK05aaI8GF1Wf8T9Csak7kBejTKuCW94pXoE7LQN8mAts6uOt-sbceyd6GXIa-Yyrl-woy2N0MTTuNTBMADbKmTQaar5O2gwa_f254WN3E__mPoWQY3THiiETwfQJU463Es-NPZG4GqnpvNGAOYlZk-YxCx1hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29e07a01.mp4?token=rNn3-uvVFCSPlxrtwLrvLM2maChJoKKbQiMVJtmCZG3tD_K5cIeUismu7NPQN7_zcsiWKn_zDb7sVdwjpAUtsA2MnqlLVNTWidtwltM5gWULAbKE_rNOPJXnpgecrHALidDxZ1nsRPky0BvawdULBzvfL3yF6TOpdkrIr0oQzu1wLlHEzVq7Fa_EuK05aaI8GF1Wf8T9Csak7kBejTKuCW94pXoE7LQN8mAts6uOt-sbceyd6GXIa-Yyrl-woy2N0MTTuNTBMADbKmTQaar5O2gwa_f254WN3E__mPoWQY3THiiETwfQJU463Es-NPZG4GqnpvNGAOYlZk-YxCx1hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/11174" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11173">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm.rh</strong></div>
<div class="tg-text">درودی دوباره  یاشار جان
میشه سوال منو ج بدین چرا ترامپ وقتی وارد چین شد نیومد ریس جمهور استقبالش در صورتی که  باید بیاد ؟</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/11173" target="_blank">📅 01:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11172">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کانال N12:
ترامپ داره به صدور دستور برای از سرگیری درگیری با ایران فکر می‌کنه
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/11172" target="_blank">📅 01:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11171">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ائتلاف حاکم در اسرائیل پیشنهاد انحلال کنست در تدارک برای برگزاری انتخابات زودهنگام را ارائه کرد.
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/11171" target="_blank">📅 00:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11170">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f182o_T9B-ym9EDsQa_tSFInK2U2stwp-7Xv2KgHGL9MuoJz_oyC6-nWhZsSz-pMku50YaSnu1ZGAi3knbqCONvnl0pbyvPK6xgh1Zh-ClJz3JMKpsTeCd_KLWVzz0PcbLnCiL1J1D2ZCi4_LMW225JajzjKDKsI1logCIdsRysfqq7zTXQjJJBSh0c_avVFOAEJ9hHZLkLgARbeJeG2odgZDoGoCWq3_0E8qxz2AWFvkdf2SIdNeMwisMWAkUI-eQ89tQT_0IsnBsx_HxKB-N2Qt3zTxbVgnhxgDQ9jpsdlw1IHbQzK2JDn98tHkt54O3m9wHX8fjjBVS1NHKjaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارن تحلیل میکنن چیکار کنن
😂
😅
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/11170" target="_blank">📅 00:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11169">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خوش‌چشم: ترامپ رفته چین التماس کنه تا میانجی بشه که ایران جنگ رو تموم کنه
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/11169" target="_blank">📅 00:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11168">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کامنتم زیر پست ترامپ
https://www.instagram.com/reel/DYSl8QEMZja/?igsh=MTNieGh0eTQyOWtnYQ==
بترکونینننن
💥
🙌🏾
حملههههه</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/11168" target="_blank">📅 23:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11167">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246f928b9e.mp4?token=FRa2Fk1KFRCG6xDF1bwl5-pjNlj-rBVf3rNpCj6F_HZoz3ZBXzIGsQqrzw_bdxGoIxGJngse4tLOmIzbcYM0FSJl1C2A5Yw42fTeT7TDH0L80Tmy-adSvUDzHNdZeWV4G88O9dw3VjoihiqCT9zfow6q80ji1AWUXGNz8MJZLyiSpEPtLcg6cZcn1F1vwz7AdwDxqpKu8GiDSmb5LPqfGivezzSMsuCIlp5oRbC--yM28_fphszgfiwLFzSbrTooQ8O0mGKqda7KnF71oluKqDEe4L8goOf898_Tr10rZ5h9yM-vA8vhpYyNwMsIhDo1_hgPYVHSLU9tsdGuktt7wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246f928b9e.mp4?token=FRa2Fk1KFRCG6xDF1bwl5-pjNlj-rBVf3rNpCj6F_HZoz3ZBXzIGsQqrzw_bdxGoIxGJngse4tLOmIzbcYM0FSJl1C2A5Yw42fTeT7TDH0L80Tmy-adSvUDzHNdZeWV4G88O9dw3VjoihiqCT9zfow6q80ji1AWUXGNz8MJZLyiSpEPtLcg6cZcn1F1vwz7AdwDxqpKu8GiDSmb5LPqfGivezzSMsuCIlp5oRbC--yM28_fphszgfiwLFzSbrTooQ8O0mGKqda7KnF71oluKqDEe4L8goOf898_Tr10rZ5h9yM-vA8vhpYyNwMsIhDo1_hgPYVHSLU9tsdGuktt7wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه استقبال از دونالد ترامپ در پکن، چین
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/11167" target="_blank">📅 23:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11166">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/11166" target="_blank">📅 22:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11165">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/11165" target="_blank">📅 22:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11164">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیام سد مجید موسی ، فرمانده نیروی هوافضای ۳پا تیم ملی رو هم بردن وسط میدون مثل میمونای سیرک  @withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/11164" target="_blank">📅 22:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11163">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad1f53604.mp4?token=UpHc7gzr7uYXLhogHZbWlQ0QmRkl0NZ604Q_iWmecwycdCRrk_c4tg8tDsXQ0e7lYjFYlEQK84JatoE6799BNGd54kdZkYlf78SRRd9zeBltWZpQp2W8t3UFxL66IgWn9ArRi32E-PlP75WDZgbRuyrEyYpluOl2OJj14cDwEtrGXao6DRcIrEV0sJC6ZiydwUDPYdJLkok3b8rEhN2LFJWumHjc3czQ62Zr2ceLvIugnelojIrO54MsHvCekowc5xmNY6NXzMtbtcoEF_yOD146skXAxObgfm3Goqs-Bh3wBpZrQFA2u1XjkjmNlPjUXOgd_Ewab6s_ypEcTSFlVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad1f53604.mp4?token=UpHc7gzr7uYXLhogHZbWlQ0QmRkl0NZ604Q_iWmecwycdCRrk_c4tg8tDsXQ0e7lYjFYlEQK84JatoE6799BNGd54kdZkYlf78SRRd9zeBltWZpQp2W8t3UFxL66IgWn9ArRi32E-PlP75WDZgbRuyrEyYpluOl2OJj14cDwEtrGXao6DRcIrEV0sJC6ZiydwUDPYdJLkok3b8rEhN2LFJWumHjc3czQ62Zr2ceLvIugnelojIrO54MsHvCekowc5xmNY6NXzMtbtcoEF_yOD146skXAxObgfm3Goqs-Bh3wBpZrQFA2u1XjkjmNlPjUXOgd_Ewab6s_ypEcTSFlVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام
سد
مجید
موسی
، فرمانده نیروی هوافضای ۳پا
تیم ملی رو هم بردن وسط میدون مثل میمونای سیرک
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/11163" target="_blank">📅 22:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11162">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8efa0d4403.mp4?token=vkZweY9AuW3A1vPhT7V1Eslu3VDW1OKsxu-j5Ysf8ULCNXf5ytZEjA4-vsZWnaJSTk-YJINYS7W0sdEe_GwnJiJQPISlJ_i4ExZHEzNmea7ICnqrJ8TFLlObjXkyQUtHJz0HtpJm7LcIFBEK93Goyl24vkRfkR1QgriMUIbTbLFQTFlCL-mw_3q5sAZcXgSAlwossEgp6QdouWQ-FR8aWAWtWbyqLXdx8_5QrtHMrY8Gu99e509bYtxIYaBCrcvn7K7RMLO38jO2FbZtGAMJ4GXCJ1Z9ZRBTM1QEX-fDxoysPeV7p2AXkdZqMNz2UEoAwxWw7HxsiHFzCVJogL-07w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8efa0d4403.mp4?token=vkZweY9AuW3A1vPhT7V1Eslu3VDW1OKsxu-j5Ysf8ULCNXf5ytZEjA4-vsZWnaJSTk-YJINYS7W0sdEe_GwnJiJQPISlJ_i4ExZHEzNmea7ICnqrJ8TFLlObjXkyQUtHJz0HtpJm7LcIFBEK93Goyl24vkRfkR1QgriMUIbTbLFQTFlCL-mw_3q5sAZcXgSAlwossEgp6QdouWQ-FR8aWAWtWbyqLXdx8_5QrtHMrY8Gu99e509bYtxIYaBCrcvn7K7RMLO38jO2FbZtGAMJ4GXCJ1Z9ZRBTM1QEX-fDxoysPeV7p2AXkdZqMNz2UEoAwxWw7HxsiHFzCVJogL-07w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رقص امشب از گلشیفته
😅
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/11162" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11161">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تاج : در جریان آهنگی که معین برای تیم ملی در جام جهنی ۲۰۲۶ می خواند هستیم
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/11161" target="_blank">📅 21:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11160">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">طبق گزارش NBC که به داده‌های ناوبری استناد کرده است.چندین کشتی باری و نفتکش مرتبط با چین در ۲۴ ساعت گذشته از تنگه هرمز عبور کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/11160" target="_blank">📅 21:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11159">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شکست هفتمین رأی‌گیری سنای امریکا برای پایان جنگ علیه ایران
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/11159" target="_blank">📅 21:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11158">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d2e0e1e0.mp4?token=dXmmXkqcPeX_uVV8LebbOhYLXhm1YSNfURBVSXYt6EfoOOxjxHy94fHIibYpVQHEatZvP564KH2k4onQ7wALXNmHWgmij0VHOVIV1UMgdQjxDe40jIHDuFLAfY8RhlhyO8axNulPwwRqub6kN-GiCzFL1z8WeWk2-g2N-bdVD_4-oJyZxDwkohXBdBArpG_BtYrrJgSUJXFiNM7E38gFgwH7srm-o478Sz7lD9hMC7ajc_vbhhEwGRQQ0i3uLUVKXOj8ezY0Q6scySIytnj5sCohieNv5cNVTKTonAx3rUf1DNdem54f3b7JnxzpRn4NmZaO0Y_PfewOR5NgCfde3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d2e0e1e0.mp4?token=dXmmXkqcPeX_uVV8LebbOhYLXhm1YSNfURBVSXYt6EfoOOxjxHy94fHIibYpVQHEatZvP564KH2k4onQ7wALXNmHWgmij0VHOVIV1UMgdQjxDe40jIHDuFLAfY8RhlhyO8axNulPwwRqub6kN-GiCzFL1z8WeWk2-g2N-bdVD_4-oJyZxDwkohXBdBArpG_BtYrrJgSUJXFiNM7E38gFgwH7srm-o478Sz7lD9hMC7ajc_vbhhEwGRQQ0i3uLUVKXOj8ezY0Q6scySIytnj5sCohieNv5cNVTKTonAx3rUf1DNdem54f3b7JnxzpRn4NmZaO0Y_PfewOR5NgCfde3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب چین
😂
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/11158" target="_blank">📅 20:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11157">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bf96fe02c.mp4?token=hna7gIg4QVDHzoq_iG6qg_9njqnM_rbEDgBa4R5QlEbsGdqd0uJo10zJDcHnqqJpwF84yXmaDLF5fVDy4zSQhVQz3wzOoYvv491nfebNtD2gZKdmuJGnOw-O4TZfN01RRZEScuQ81x_RWgyQTqoD9qdhZalIGyox-KNTHxLJ_31CZklszkFIEzp9k3tiLoJ0EcvJcjJOsDE5fexDmNWixWsnWqQ3YTGP-elo1kkAB7kxGpRDfbieH78Sz3gEwQTwQeHHc2LwBiVLCX4WXn0n-mF-8ytRghfx24xJPZwwdAta-WtKdGG4ZeApyj4MyVWuhV2idr71xjlL-2ahy9EO4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bf96fe02c.mp4?token=hna7gIg4QVDHzoq_iG6qg_9njqnM_rbEDgBa4R5QlEbsGdqd0uJo10zJDcHnqqJpwF84yXmaDLF5fVDy4zSQhVQz3wzOoYvv491nfebNtD2gZKdmuJGnOw-O4TZfN01RRZEScuQ81x_RWgyQTqoD9qdhZalIGyox-KNTHxLJ_31CZklszkFIEzp9k3tiLoJ0EcvJcjJOsDE5fexDmNWixWsnWqQ3YTGP-elo1kkAB7kxGpRDfbieH78Sz3gEwQTwQeHHc2LwBiVLCX4WXn0n-mF-8ytRghfx24xJPZwwdAta-WtKdGG4ZeApyj4MyVWuhV2idr71xjlL-2ahy9EO4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همراهان ترامپ در چین
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/11157" target="_blank">📅 20:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11156">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سد عباس چپقچی وارد هند شد
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/11156" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11155">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">احسان افرشته، به اتهام جاسوسی و همکاری اطلاعاتی با موساد اعدام شد به گفته رژیم وی چند مرحله تماس از طریق پیام‌رسان‌ها داشته و در ادامه از طریق پست الکترونیک باهم در ارتباط بوده‌اند بیش از ۳۰۰ پیام بین آنها رد و بدل شده است. افرشته در ابتدا در پوشش راننده تاکسی…</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/11155" target="_blank">📅 18:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11154">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d224c82b7.mp4?token=iHGfJEmmvX5Cp7klvrWq-kCp5W-lZhFaKQfZjWmk70wKMCsdQDMOvEB8jhJzgBIbYCjZjzWgebQOD0IFjregAzBFG8QKuVDWIpNDuCUYccXIOoaPOtVIEE6SLj-TjpgDK_TE5AdXGYIxSl8AM40pUAD03EYElUy4lYeKSnF3yBbgULdVk49txhi5mO4YoY1RQks-CG40zvMsOPtNobm_F7RVrXK3nesFpSgRmAzHztg01aPK-FZrd_4I9AvaPAa109lpjwIERQdjhd2F_K2QOG0xe7f03tcoQf2sINzFPToeSvq9pvI37mWmzpPe6eexYfMwpyATT_0ZXB3g93mFeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d224c82b7.mp4?token=iHGfJEmmvX5Cp7klvrWq-kCp5W-lZhFaKQfZjWmk70wKMCsdQDMOvEB8jhJzgBIbYCjZjzWgebQOD0IFjregAzBFG8QKuVDWIpNDuCUYccXIOoaPOtVIEE6SLj-TjpgDK_TE5AdXGYIxSl8AM40pUAD03EYElUy4lYeKSnF3yBbgULdVk49txhi5mO4YoY1RQks-CG40zvMsOPtNobm_F7RVrXK3nesFpSgRmAzHztg01aPK-FZrd_4I9AvaPAa109lpjwIERQdjhd2F_K2QOG0xe7f03tcoQf2sINzFPToeSvq9pvI37mWmzpPe6eexYfMwpyATT_0ZXB3g93mFeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی‌حرکت ایستادن کامل افسر چینی هنگام عبور هواپیمای رئیس جمهور آمریکا (ایر فورس وان) در چند متری او، توجه بسیاری از رسانه‌ها را به خود جلب کرد
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/11154" target="_blank">📅 17:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11153">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک مقام ارشد کُرد در گفتگو با کانال۱۳ اسرائیل:
در واقع خود پرزیدنت ترامپ مانع از طرح اقدام ما علیه حکومت ایران شد و اتهامات او در مورد ضبط سلاح های معترضین در ایران توسط کُردها، ناعادلانه و غیرمنطقی است
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/11153" target="_blank">📅 17:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11152">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اتاق جنگ با شما : گزارش از جنگنده های ناشناس پرواز در ارتفاع پایین در‌ ارومیه و انفجار در شیراز
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/11152" target="_blank">📅 17:13 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
