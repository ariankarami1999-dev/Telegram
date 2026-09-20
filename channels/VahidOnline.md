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
<img src="https://cdn1.telesco.pe/file/bs6rbOrc1r1zqLuhaYfbYL2o1N9o_ZgIBy9dpn3-X93_fLgm5jKCjJFhb6gerKUI5h9IPGdtNtt8mkq9qDyKUOzwGnn8EdagLn_5G_OcSCck_kCs-wPv8_aBS49rN-8DxBwqdz_3GqDnS-t0G422qwoqs1u7BWfwE3eHB6vEaQh9V0EuSoa6a2yAoDc7Xgc5n4JK0-YamVF9KBDz_CJVIAL_h7oMqNJgXYGv7itS-VxRRqGA9JwNG9Ns1uXTO-hnv39Q0CSdGArUtn1cYZ9Gb1cskG1NdjXdjXRnsCly2MQWhwbdH9RM8V4nTIfGgpQ9fVJL11mllW_I6QYFvl-8gQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 21:02:41</div>
<hr>

<div class="tg-post" id="msg-78460">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=aDMGiginlG1lYyI76a4j2S_LTOHGSCKIdFNe4XL79QE0R7rec75nodS6G_83L08Pqnn7XUv8o06FGgkT5NSMnAfGlRu-ZPb_C0NDxPB7Z_KI2apUOdeAlwZNqZSxHfF7w18Yg7UzQOPGVR3jV6RoiBHRx1jNYEP7PE3m5UQQR4E3uQjXo4MRikCHa1sDLgFejDqP94_qpZ5gyEK2Gbz4Bx7XHWIjIdICL1SCB9jkS3MEcD6Zv_Ungynr0L6G2fGYAKSECGM9UGB-2SHuUe3cg2uKS-h3teUVzwADdRWXIH1bYXT2zlXpYf7N7KMUlRVv6_L6fbVLc4cKzyfc6TVo6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=aDMGiginlG1lYyI76a4j2S_LTOHGSCKIdFNe4XL79QE0R7rec75nodS6G_83L08Pqnn7XUv8o06FGgkT5NSMnAfGlRu-ZPb_C0NDxPB7Z_KI2apUOdeAlwZNqZSxHfF7w18Yg7UzQOPGVR3jV6RoiBHRx1jNYEP7PE3m5UQQR4E3uQjXo4MRikCHa1sDLgFejDqP94_qpZ5gyEK2Gbz4Bx7XHWIjIdICL1SCB9jkS3MEcD6Zv_Ungynr0L6G2fGYAKSECGM9UGB-2SHuUe3cg2uKS-h3teUVzwADdRWXIH1bYXT2zlXpYf7N7KMUlRVv6_L6fbVLc4cKzyfc6TVo6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: ۲۹ شهریور، ساعت ۱۷:۳۰، اربیل عراق
هم‌زمان:
رویترز به نقل از منابع امنیتی عراق اعلام کرد که سیستم پدافند هوایی، یک پهپاد را در نزدیکی فرودگاه بین‌المللی اربیل در اقلیم کردستان عراق رهگیری و سرنگون کرده است.
@
VahidOnLive
آپدیت:
نیروهای ضدتروریسم اقلیم کردستان می‌گویند که صدای انفجار شنیده شده در نزدیکی فرودگاه اربیل ناشی از «تمرینات نظامی و فعالیت‌های امنیتی» بود و «هیچ خطری ایجاد نمی‌کنند.»
این فرودگاه میزبان نیروهای ائتلاف به رهبری آمریکا در اقلیم کردستان عراق است.
رسانه‌های محلی کرد گزارش دادند که ائتلاف به رهبری آمریکا مهماتی را در این منطقه منهدم کرده است.
یکی از خبرنگاران خبرگزاری فرانسه گزارش داد که شاهد برخاستن دودی خاکستری از نزدیکی فرودگاه بوده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/78460" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0mzjss6vSa5w46NDyo0jEvK_2_yVVa76SLaXh9J9isRJow8So5c2hYJKHPmF5kTyuhbmtLG55lE4OnxrVuF8-AkVFko3rc77uT0k2Jkpl7_p_-b3_I5-l0CXYTH6hdDCuQ-Y0wbADvujvHFjbbIGQ30QSGYVWzHXWzcuGrlO86sFlwxCQb4975gWdTFoerOWsoMQG3lVJyXyfO5-y9u8Da_pTCx3WEoNadaSw-8HhYEHAX0m3AGNf3UyxYY6BjOiFt5FxnOpfvXgG8qHwkGim_BTnGR88-UxIx_l3o8wK-3jBYwE8bIWlOVTZ6kX0GXbZWRGAYuiQQTOej4tR0NDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز یکشنبه ۲۹ شهریور ماه در گفت‌وگو با شبکه خبری فاکس اعلام کرد که در حال تصمیم‌گیری درباره ایران است و «در آینده نزدیک اتفاقات بسیار بزرگی» درباره ایران رخ خواهد داد.
ترامپ گفت گزینه‌های فعلی روی میز شامل «محو کردن ایران»، «رها کردن آن برای فرسایش اقتصادی» یا «رسیدن به یک توافق» است.
رئیس‌جمهوری آمریکا همچنین گفت: «سؤال من این است که چه زمانی و آیا قرار است کل ایران را منفجر کنم» و افزود: «بهتر است آنها رفتار خود را اصلاح کنند.»
ترامپ گفت برای دیدار با مسعود پزشکیان در حاشیه نشست مجمع عمومی سازمان ملل متحد در این هفته نیز آمادگی دارد.
او در ادامه گفت برخی مقام‌های ایرانی پنهان شده‌اند و نمی‌توان افرادی را پیدا کرد که قادر به دستیابی به توافق باشند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/78459" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvXgVytiifKwdZ4htvWxyn1VYKAujm3esiBCvupkzMSom8Wf8p399W1VMvyjHjrbmbUpWMan3c4cf2da1iYkIyhvnfd7wktahQozQ0HgZwWHgnKuJBJm_6_jW6ic2cZGyUVnIK_lxsdVvaMOpC1vzwOiZLeej8Iinfmkhbdjuji9cOziZk56ajNohV5DvwQ1RAQvgDELAtzRh8MEWWvxhUVOGJsliS_-QBkzEfAQVWn31d49fbCrfm4XL_YOSwZkrsNMN41ja8I7oVvhf5P4wVSk99OnOr2-IRsruQFYpGjeJKMrWTCKwN3118HCZfupwONyuCF5BlbkQnYgVnAVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا با انتشار بیانیه‌ای نوشت به اطلاعاتی دست یافته که با آمریکا با حمایت برخی کشورهای منطقه، برای ازسرگیری حمله به ایران آماده می‌شود.
در این بیانیه آمده است: «براساس اطلاعات دریافتی، آمریکا بار دیگر تصمیم گرفته با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران را از سر بگیرد.»
قرارگاه خاتم اطلاعات بیشتری درباره شرکت‌کنندگان و یا کشور اروپایی میزبان ارائه نکرده است.
این نهاد عالی نظامی به کشورهای منطقه هشدار داد که اگر با حمله آمریکا «همسو» شوند، «همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.»
قرارگاه مرکزی خاتم‌الانبیا همچنین به آمریکا هشدار داد در صورت حمله، «تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/78458" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g15brb5IEAVsIQP_SDTtd9yx76YCEd8_8JH-aLo0qpryc0-Kxsq3Gb5hNSnWjIMwohzK82G7mV5wpg8M0Oi8ob6moTp139ZIiarYfkTRMW6mmGBjn4_Be4ZZHxxnj_YfJrqERFHdp8EHguX-XXR82kSQI0hBKkL731y9vlHmb4FQKGw01UpHMDDncAXTtB80jQhAqRLPenLaRr5tdZNLQRtr2FQFo_lEVdxO-25AfRAajtLGu6j72-IX-jMFAdwbI1Z8acEZLz3dPAdx3PRLO6bN_OZC7r4VnUOISthlRdvcSqHNIwwtE-ENEQMNvdC4Hl8ZaMpYQcmeEe_eSzBAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی از جریان‌هایی انتقاد کرده است که با رد هرگونه تعامل و دیپلماسی، ایران را به‌سوی «فرسایش و جنگ بی‌پایان» می‌برند. او هم‌زمان تایید کرد که تهران شروط و پیام‌های خود را از طریق میانجی‌ها به آمریکا منتقل کرده است.
@
VahidHeadline
محمدباقر قالیباف روز یک‌شنبه، ۲۹ شهریورماه در نطق پیش از دستور خود گفت: «انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده... و تا زمانی که این شروط محقق نشده و حقوق حقه‌ ملت ایران به رسمیت شناخته نشود و تعهدات آمریکایی‌ها اجرا نشود، هیچ روزنه‌ای برای بازگشت به شرایط پیشین مذاکره و باز شدن تنگه‌ هرمز وجود نخواهد داشت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/78457" target="_blank">📅 16:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHSo4ISrf_DzDemmQDNQ-uJ_OnhMfPcKi_tdA_6pX1zspVlKpV57mt-ABb-2VeBLSLcRfOTodCN-VZu4333pQpqF7NbHDcPLxAMpDRzoQ9b_KRwFeYLUBdArPELOF90I_U5Py_peS1OUbscA5ANnReIE5O7__mu4_hnYDM1w-yzllT2gV0w952aLmJEZujE9uEftWWkJHYsfI4BzhrAcMW2IOazRfnYS2B2xbIAyj2LOM46--DknJctluuDt4hZYDSAlQKC4lI55Np2_HC7qRN7tYsn4K--CEfISPdMf7e3WgrvP2dNnKtERI0DnhED2yii9RXzC65RiYAAF6tD2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه یک دادگاه تجدیدنظر استان البرز حکم مجموعا ۱۸ سال زندان «منوچهر بختیاری»، پدر دادخواه پویا بختیاری، از جان‌باختگان اعتراضات آبان ۱۳۹۸، را تایید کرده است.
براساس رای صادرشده، بختیاری با اتهام «تشکیل و اداره گروه در فضای مجازی با هدف برهم‌زدن امنیت کشور» به ۱۰ سال زندان، با اتهام «اجتماع و تبانی برای ارتکاب جرایم علیه امنیت کشور از طریق همکاری با یکی از گروه‌های مخالف نظام» به پنج سال زندان، با اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به دو سال و با اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس محکوم شده است.
تایید این حکم کمتر از سه هفته پس از آن صورت می‌گیرد که شعبه اول دادگاه انقلاب بندرعباس، منوچهر بختیاری را در پرونده‌ای جداگانه به ۱۰ سال زندان دیگر محکوم کرد.
در پرونده بندرعباس، او‌ با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «تحریک مردم به جنگ و کشتار» و «ارسال فیلم به شبکه‌های مجازی بیگانه» روبه‌رو شده است. این پرونده با شکایت دادستان بندرعباس تشکیل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/78456" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=r3OZmD4WfNnKmnW3kbItfDmU4G4A5S4tS7Q2xfsDQBT0z40cYnVGI-pJjz07k3NjEpKiiiG-N-PQXRIKzx6xGKyOJMjpSiEvKwdpXJJqfD6esoN8z4v923C4UhCcqCOXBy-XFImxasT6OVqYr1fs6ygSjO2UWgMhc_N4sLBlVm-JObZXtVgDsL31atWJg1JVjG9zRIhq-_NLKZj1IaVTt6Z9OhP72HSR5jGiXC1bN4KR3RFKmfmzaIgPuPd1tva4Pyr6JtTzRnY6SBHo-r6QZxHNTIUXrwc0MWZgFKfKJgtaJ4lyKanpOV21yCnS81QqC4YvVwSosGeog3VrDxTWtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=r3OZmD4WfNnKmnW3kbItfDmU4G4A5S4tS7Q2xfsDQBT0z40cYnVGI-pJjz07k3NjEpKiiiG-N-PQXRIKzx6xGKyOJMjpSiEvKwdpXJJqfD6esoN8z4v923C4UhCcqCOXBy-XFImxasT6OVqYr1fs6ygSjO2UWgMhc_N4sLBlVm-JObZXtVgDsL31atWJg1JVjG9zRIhq-_NLKZj1IaVTt6Z9OhP72HSR5jGiXC1bN4KR3RFKmfmzaIgPuPd1tva4Pyr6JtTzRnY6SBHo-r6QZxHNTIUXrwc0MWZgFKfKJgtaJ4lyKanpOV21yCnS81QqC4YvVwSosGeog3VrDxTWtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«نجمه امینی»، دانشجوی حسابداری و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در پیامی صوتی از زندان وکیل‌آباد مشهد اعلام کرده است که دادگاه انقلاب  روز ۲۵ شهریور برای او حکم اعدام صادر کرده است.
او از سازمان ملل متحد، وکلا، فعالان مدنی و نهادهای حقوق‌بشری خواسته است پرونده‌اش را بررسی کنند و برای برخورداری او از حق دادرسی عادلانه اقدام کنند.
هرانا پیش‌تر نوشته بود که او با اتهام‌های «اجتماع و تبانی» و «توهین به مقدسات و ائمه» محاکمه شده است.
نجمه امینی روز ۱۱ بهمن ۱۴۰۴، هم‌زمان با اعتراضات سراسری دی‌ماه، در پاساژ فردوسی مشهد بازداشت شد.
امینی ۲۳ ساله، دانشجوی رشته حسابداری و ساکن مشهد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/VahidOnline/78455" target="_blank">📅 15:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5bb8WOoUVKUwcnZ5Fbrbab4_pCGZceE3MAH9liuQseYN9VRoAB30qAW3RQQ7ZbYMRcN9C63u41A5XpbGgAkPuJ1VFj5LHFxbgVRXH_m6S9tzp-hpQ-3lpXVqjzZx0tX9XtpUITshpRxOQFEceA5eMcaVNUZ92tuxAuBY4bxIoE-MBEIe04tp87vv0bZ_1tbGz39bmLv-qDRqQ9_Lz6AiLQaZgOFrJVsfH9FWwubQzfoSCq7LWQLqt7MXebHRVUvVQsicBOMT09XkIxdoQ7HAmTG2UE9scKbfes9DUSwCB7D4BZxf_-gZfhdm3Ci9denSyyl9AkRem-9rErwA10ahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی جمهوری اسلامی، شامگاه شنبه ۲۸ شهریورماه در شبکه اجتماعی ایکس نوشت ۷ شرط ایران برای آغاز «هر مذاکره‌ای» به دولت آمریکا اعلام شده است.
رضایی در این پیام نوشت: «پیام تهران روشن و بدون ابهام است؛ اگر واشنگتن می‌خواهد از مخمصه‌ای که خود ساخته خارج شود و بیش از این در آن گرفتار نشود، راهی جز پذیرش حقوق و شروط ایران ندارد.»
ساعاتی پیش از انتشار این پیام، رسانه‌های دولتی ایران به نقل از گفتگوی محسن رضایی با شبکه الجزیر گزارش کردند، ارتباط میان تهران و واشنگتن به وسیله میانجی‌گران قطری و پاکستانی ادامه دارد و شروط تهران برای بازگشت به مذاکرات به کاخ سفید اعلام شده است.
رضایی با اعلام آنکه تهران منتظر پاسخ واشنگتن است گفته بود، پایان دادن به جنگ در همه جبهه‌ها، آزادسازی دارایی‌های مسدود شده ایران و پایان محاصره دریایی شروط ایران برای آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78454" target="_blank">📅 23:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cSx37eznbA9FZyZZDbWbHE_8lDSuoAGCPJlLUdsmvuNygwX4clqMHbPYkexx8DH0ejI-Yt83pDokVVxttnK4gt2h0hg_uflSbgM_grjOWN8wLVScg7MtTQGEeHbeBb7hQR95TtSBbj9g3XYcQGZY6OAWfPyZF-08DqsEeLJ8M2EttGkXqA_sD_a6melBuNG9Bhfm92LAuF7iu-KExrRcJIDwQv-7hDASHA3ek9C4iGmu521OiQbzllDZFhhjpVoxXs1k101HQweC4vvLYsaNExHdt2pwQayKrCBD3lzSSW_Udtux1yuo4JoSGj1daRdSlF9gyAAqpnGR6IMrmb9JNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاکان فیدان، وزیر خارجه ترکیه، گفت در پی حملات حوثی‌ها، عربستان سعودی ممکن است در برخی زمینه‌های فنی نیازهای نظامی داشته باشد و ترکیه برای پاسخ به این نیازها در چارچوب «ائتلاف دفاعی مکه» با عربستان سعودی و پاکستان مشکلی ندارد.
فیدان شنبه ۲۸ شهریور در گفت‌وگو با شبکه «ان‌تی‌وی ترکیه» گفت حملات به تمامیت ارضی و حاکمیت عربستان سعودی جدی است و ترکیه در چارچوب توافق میان سه کشور در کنار عربستان سعودی قرار دارد.
او همچنین گفت عربستان سعودی تمایلی به ورود به جنگ آمریکا و جمهوری اسلامی ندارد و کشاندن این کشور به این درگیری «غیرقابل قبول» است.
فیدان در پاسخ به پرسشی درباره ارزیابی برخی منابع اسرائیلی و ایرانی مبنی بر اینکه «ائتلاف مکه» تنها روی کاغذ است، گفت: «ما به این حرف‌ها می‌خندیم. ائتلاف مکه به یک سازوکار بسیار تاثیرگذار و تغییردهنده معادلات تبدیل خواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78453" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/205953bb15.mp4?token=tvZ5OkkwLTwSaxwjua1XehitQMuc_a_T4OHWD8jiw8CYn9hdmTvEG-7r_DchgkZInxlClLaWztTDwKOaIc8VQpzjeB-OnL6h6YasUqGfDRd8WDvy9CdCC19yOCh5hnvUwODcc3P7AM1nq32KIwJF2wvdFCaVC-wF82M8GuEYkkIR52_TQ_CAIUeFEiTl-rCfzAKEA_ym3Z3L6mh0uEuT3deA9CcB_pPSzQ8FZuigTw8v_QCAb1SU88dz_w9QXUavNjANUpc7mAa-R5xOK_upa4bVt1RRzzZ4gErtDXGsZq5lKg6nNeaJrdzWIWkAob8R0fwrYmbubNfZUGL7O7piHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/205953bb15.mp4?token=tvZ5OkkwLTwSaxwjua1XehitQMuc_a_T4OHWD8jiw8CYn9hdmTvEG-7r_DchgkZInxlClLaWztTDwKOaIc8VQpzjeB-OnL6h6YasUqGfDRd8WDvy9CdCC19yOCh5hnvUwODcc3P7AM1nq32KIwJF2wvdFCaVC-wF82M8GuEYkkIR52_TQ_CAIUeFEiTl-rCfzAKEA_ym3Z3L6mh0uEuT3deA9CcB_pPSzQ8FZuigTw8v_QCAb1SU88dz_w9QXUavNjANUpc7mAa-R5xOK_upa4bVt1RRzzZ4gErtDXGsZq5lKg6nNeaJrdzWIWkAob8R0fwrYmbubNfZUGL7O7piHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، روز شنبه ۲۸ شهریور، در پیامی ویدیویی خطاب به شرکت‌کنندگان در «مجمع گفتگوی جهانی ۲۰۲۶» به میزبانی انجمن سیاست خارجی اندونزی، با انتقاد از رویکردهای مداخله‌جویانه در خاورمیانه تاکید کرد که دهه‌ها حضور و فشار نظامی نه‌تنها کمکی به ثبات نکرده، بلکه چرخه‌ای بی‌پایان از تنش را رقم زده است.
عراقچی گفت، ریشه بحران‌های منطقه را باید در یک حقیقت تلخ جست‌وجو کرد؛ چرا که سال‌ها مداخله خارجی، فشارهای همه‌جانبه نظامی و درگیری‌های پی‌درپی اثبات کرده است که مداخله نظامی امنیت نمی‌آفریند و اعمال فشار و زورگویی هرگز به صلح ختم نمی‌شود.
عراقچی در ادامه این سخنرانی ویدیویی خاطرنشان کرد که در شرایط کنونی، جنگ به‌جای آنکه آخرین راه‌حل باشد، عملا به ابزاری معمول در روابط بین‌الملل تبدیل شده است. رویکردی که نتیجه‌ای جز عادی‌سازی خشونت و تداوم الگوی درگیری و تقابل دائمی در منطقه به همراه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78452" target="_blank">📅 16:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2Lim19z38lduHl3tNKLYUiBkpYBqwjt4cnYPdG0FsowcrllJix2xB4O9tbUzT2n0nig-l7MrNYNDiUxuLt9h7r5KMLpOcKF0fTJGsJcm9PV1fIepC4FpamOKOXztYPRHBXCVuVDOUfKmmlHCaTdOkiwMa8Zqy0Z3E2RkER9sh8FHFWbXfdnjyoqeAHRwbhA4xIR7N-3nZeH_lvJRhoM7aACXmAgVAwFdvQU38agqq1-lJJnr_nZoTWyoV9Tyt3q2yxOItAAXYDXYrh5XyXFto3VG2Pfg3JWbOxaD5mMds4kIsC9mZb-QA7cRh3VmTCQp5ZGSLMMzaj_mznigDRCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است. دادستانی مدعی است که در این رقابت «موازین قانونی و شرعی رعایت نشده بود».
مسابقه دو ۱۰ کیلومتری بامداد جمعه ۲۷ شهریور با حضور زنان و مردان برگزار شد. انتشار تصاویر شماری از شرکت‌کنندگان زن بدون حجاب، رقابت را به موضوع بحث در شبکه‌های اجتماعی تبدیل کرد.
بنابر گزارش خبرگزاری فارس، برگزارکنندگان اعلام کرده‌اند مسابقه با مجوز وزارت کشور و هیئت دوومیدانی استان تهران انجام شده است.
هیئت دوومیدانی تهران گفته پیش از آغاز رقابت از شرکت‌کنندگان تعهد کتبی برای رعایت «حجاب و شئونات اسلامی» گرفته شده بود.
حبیب ستوده‌نژاد، مدیرکل ورزش استان تهران، به خبرگزاری تسنیم گفت مجوز رویداد از شورای تأمین استان صادر شده بود و با ورزشکارانی که «خاطی» شناخته شوند برخورد قانونی و انضباطی می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78451" target="_blank">📅 16:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZAmEw-QEmPSKNsLLGmecePbMHVTATdonZqeCEDmEAfAQRTlJmwFA7KGezN1PqoQjJLkz7UPGkw9CMnpIiSk7neOzq4OFbyQiv4sBdzm2itT6uJ_d8c8cMMfrucDvnbIsewFuSybZfqMUsJF7kipVFgSuZFPGGxq9AMqHSXkVvd8Oj-TMfH7ojtTgcFmD-4--kJLTI37z4cv2xhzjZwTalS2Xpc8-OcgTQMomjZJKVAOPF4-FNLtQ8npOnMVFkw2EBET9rR07u-mditJXiqNShTrN2iWChSWc-Up8aylExJ29MY-sjQej1VknaqA9GfFV4Q88KezMvYaS4KXzwRCzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد تنظیم مقررات و نظارت بانکی ترکیه مجوز فعالیت شعبه «بانک ملت» ایران در استانبول را لغو کرده است؛ تصمیمی که پس از توقف پروازهای شرکت هواپیمایی ماهان میان ایران و ترکیه و مداخله نهاد ناظر در مدیریت یک بانک تحریم‌شده دیگر اتخاذ می‌شود.
براساس اطلاعیه منتشر شده در روزنامه رسمی ترکیه، هیات نظارت بانکی این کشور روز جمعه ۲۷ شهریور ۱۴۰۵ لغو مجوز «شعبه مرکزی ترکیه بانک ملت مستقر در استانبول» را تصویب کرده است. این تصمیم روز شنبه ۲۸ شهریور در روزنامه رسمی ترکیه منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78450" target="_blank">📅 16:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcQxo3MKMfDIsKggpW-XDxyTXPMOCqOMiRhSrcmI35grIm5xvYGaYiDlDenkzuxSt_QYxVIlrAGXivJzxPvmwhNzpL2yWH-Ryoca5WNMzngQUzkmxEp3_muM_WO1DkK8PZI7zsMZ-5YkfSFTegVdX4BgAoptlzTEXq6UP568GHO8vy5vcfTem4X8ZkkMYgHe8tCf4Vmyyp-uOV7uw9pcRizHLvW_1vazVRNAKN6nN7rtJWYCkbc_u-5dwKaE3cclYwBQcgxWM78CiJAfYTF9gKU0i-RaTwtZE0JFHwJP1dbN3m9qjkOeC7ZijeGdqeGu7Q61OzyCmDSQ2VBjcWkf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز جمعه ۲۷ شهریور و اندکی پس از تایید کنگره در هفته جاری، لایحه‌ای را امضا کرد که مجوز اعمال تحریم‌های جدیدی را برای تحت فشار قرار دادن روسیه بر سر جنگ در اوکراین صادر می‌کند.
این قانون همچنین تحریم‌های مرتبط با ایران را نیز تمدید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78449" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXyZzhG2BK1Y-UG88VWiEnNI-r75vaUebwx-EPYlJyFRNQh7ejigQ3dgclXFssyUmjMLuhGoJWZUGelsnTNgubcPQvqi12GNiP8Y2l22F9DiEkZ2VP58NNBC2X9rMgtBT84s2tfRDjm3thhZrs-G3cC_1yLUoNi6bKRxNuXxHaEOH9M0qrQnFrvAMCi4Jl4QigH1uQhIPwSZl1XgEjZKYli_YaDpe1jSmp6TgP8aJ9KMuoCFsEqrDRjroVmfqG6uBOQH-7coX4wU9ZanHinQzV9YSLMGufqsawGApxTfKQR5OtDjMjyTWPW8dLj5D7yv7blWkpDUYxVpj_4srDjK7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اعدام «حسین پدران» با اتهام «جاسوسی و همکاری اطلاعاتی به نفع اسرائیل» خبر داده است.
براساس گزارش رسانه‌های حکومتی در روز شنبه ۲۸ شهریور ۱۴۰۵، حکم اعدام پدران پس از رد فرجام‌خواهی و تایید در دیوان عالی کشور اجرا شده است. محل و زمان دقیق اجرای حکم اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78448" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q700saESb_CmYBzhKQyC8gv5E5Rr9ZP_UjmJW0W4SllFw23S3d96L09aGthuK2h86a8jVtvhPTpovAL0iGkgXz-TKjzdrP2Z7qq-l0vw4Ll9gAL3f7JgvSF31nHa-yOD6_lRREVvcHPEp0Et675e-Pjy1uBBZMIYEoTJfGQJNv74OIURZ5p5SDgvY30o14dsZOaT7NgcetmHSlOigSKzmeYYd1LdOTFwLOcylc1Yj6UjCZR4IF61CZ_Ew75DqZXXWY_9CcN2rsknuNdK2LFcACQxmRE3V7z-hNio7-H21_1O7nrA7YFnwDfP6BAMOv8O4UH9UrCvQ1Y1EmpfDsE04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌سوشال اعلام کرد آمریکا با دانمارک و گرینلند به توافقی دست یافته است که کنترل دایمی امنیت و تمامی نیازهای دیگر در گرینلند را در اختیار آمریکا قرار می‌دهد و به تمامی نگرانی‌های متعدد ایالات‌متحده رسیدگی می‌کند. او گفت این توافق هیچ هزینه‌ای برای آمریکا نخواهد داشت.
دفتر نخست‌وزیری دانمارک نیز اعلام کرد انتظار می‌رود که گرینلند، دانمارک و آمریکا هفته آینده توافقی را برای تقویت امنیت در منطقه قطب شمال و اقیانوس اطلس شمالی امضا کنند.
ترامپ گفت: «از این پس هیچ دشمنی از سوی آمریکا نمی‌تواند بدون تایید کتبی صریح ما در گرینلند پایگاه ایجاد کند، حضور نظامی داشته باشد یا سرمایه‌گذاری‌های حساس انجام دهد.»
پیت هگست، وزیر جنگ آمریکا، نیز گفت: «ما بلافاصله روند حضور نظامی گسترده در بخش مناسبی از گرینلند را آغاز خواهیم کرد؛ بخش‌های مناسب زیادی برای این منظور وجود دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78447" target="_blank">📅 04:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=ex9ejYpqh044pwBOOS3J7owT5QToGszA6BfiUuGOOBYW7PuakpkEQz0d2gaXLqOOudrABPG9TU79I5zyep86bv-jj46a2OGLBO6oM7aa7YcjT7zZAEwlbAjgYRqotVuXcugIRa__kFqrjDkAkJ9pjCvXewjGvBqWdMKSJ_sALjX6p_PAssQJdjOsbBR5b5KAEvjCLKFj7f8ndZWI7NHGRGV9lkc01ir2PEwy5HbUY3lvOWycHaB3Wf8qaMrrOa-D1ubftSjux6g-0nhrIFvGcpRMhltf3fe4g-B-DlQewELslDFPbBYubRVMfoChQBIVVWdFcMqlGim1OzGtJLFy2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=ex9ejYpqh044pwBOOS3J7owT5QToGszA6BfiUuGOOBYW7PuakpkEQz0d2gaXLqOOudrABPG9TU79I5zyep86bv-jj46a2OGLBO6oM7aa7YcjT7zZAEwlbAjgYRqotVuXcugIRa__kFqrjDkAkJ9pjCvXewjGvBqWdMKSJ_sALjX6p_PAssQJdjOsbBR5b5KAEvjCLKFj7f8ndZWI7NHGRGV9lkc01ir2PEwy5HbUY3lvOWycHaB3Wf8qaMrrOa-D1ubftSjux6g-0nhrIFvGcpRMhltf3fe4g-B-DlQewELslDFPbBYubRVMfoChQBIVVWdFcMqlGim1OzGtJLFy2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۲۷ شهریور در گفتگو با خبرنگاران در کاخ سفید گفت جلوگیری از دستیابی ایران به سلاح هسته‌ای موضوعی است که به آن «بسیار افتخار» می‌کند و ایران دیگر سلاح هسته‌ای نخواهد داشت.
ترامپ با اشاره به افزایش هزینه سوخت گفت تحقق این هدف ممکن است مستلزم آن باشد که مردم برای مدتی هزینه بیشتری بپردازند.
او افزود: «اگر مردم می‌توانستند بین قیمت پایین‌تر بنزین و اجازه دادن به ایران برای داشتن سلاح هسته‌ای رأی بدهند، فکر می‌کنم نتیجه با اختلاف بسیار زیادی روشن بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.»
رئیس‌جمهوری آمریکا همچنین گفت انتظار دارد جنگ با ایران «به‌زودی» پایان یابد و پیش‌بینی کرد پس از پایان جنگ، قیمت بنزین به سطح پیش از درگیری بازگردد و «شاید حتی پایین‌تر» برود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78446" target="_blank">📅 04:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=Ozb7xVnDidtoAj2kskWKuZNs3-v_sLw6Fag9KZUKwsop0p7zcm7wfbqhMdpAUqjDpo0Zq8cuiQA5OXniay5oD0SxY7tXnCUMryLC_3vqio1ol4ewrOH9YnC1Akij4WOX39tc-qnBB6cktpY5jLKnL4wUq6GNWcGSyp7B9_GQeam6ChwQQztEJImfsu_Wc_A-0o_N-Akc9w3lda7I_2sKrcqwF8R7uWGodK301UYaudG-4IDXezYDYNF6aJYqYvqVEFsmNN0YhJMNUWPUEr4qkMY41rgTjD8-i_uCVyRu9PKrYQbske0HS285pHXcxjHvYKpr2dxFaWKBdsCpjmCUmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=Ozb7xVnDidtoAj2kskWKuZNs3-v_sLw6Fag9KZUKwsop0p7zcm7wfbqhMdpAUqjDpo0Zq8cuiQA5OXniay5oD0SxY7tXnCUMryLC_3vqio1ol4ewrOH9YnC1Akij4WOX39tc-qnBB6cktpY5jLKnL4wUq6GNWcGSyp7B9_GQeam6ChwQQztEJImfsu_Wc_A-0o_N-Akc9w3lda7I_2sKrcqwF8R7uWGodK301UYaudG-4IDXezYDYNF6aJYqYvqVEFsmNN0YhJMNUWPUEr4qkMY41rgTjD8-i_uCVyRu9PKrYQbske0HS285pHXcxjHvYKpr2dxFaWKBdsCpjmCUmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با برگزاری
رزمایش "جان‌فدایان"
تصاویر بالا رو هم تولید کردند:
مسابقه دوی ۱۰ کیلومتر تهران روز جمعه ۲۷ شهریور با حضور گسترده زنان برگزار شد.
در تصاویر منتشرشده از این رویداد، زنان با پوشش‌های متنوع و اختیاری[تر از قبل] دیده می‌شوند.
رقابت امروز در «بوستان ولایت» و در دو بخش جداگان زنان و مردان انجام شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78444" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OkPV1VQ1bo3CD_CGa-iuRXnZnIeqb2NF_-prAZlwQyRH9DvGRbrhnliW-gb10X9vCHaU-AUW9AHCVj4NY6q5HT5NZu52vRLVkFuRPWW3wKVsdPUrbJ2Z5aXICiaoD2nIWumr8lSOuosfR4GnTovWkmP0HcoHH4eqj0_DpADRXSSzotb0kL2Ne8Zjs07Ks-clvVzfKJK3Rcm_ivpBhgmjyA0fUNfM7FQV7eND6kqmLALXyFHRtF3T_ZM6CnClUbH4k_gTMd0V-_3OjEqwjoLlD5PmoJ8FSr4SElI4Km4Me6gpANvll70FEzmEwrZPQyyjpsCEfBxzf6JG-yHIP-7R6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TllV65QR-Lr3xGtaMCEDtRgSlvShTvC6HSlQcUQ_AmG4P4TC-hB07opeHl7AKtDygtbVSIs9yntfwMzhISBD_Qc6vlWNIMV7a6_YKF6TdNKjUZBtrjg027JMVisBKGv7z3ZaNDJeaB9Qqexhzp2ouVWRQqWb9WmtSI-3nQU0sAgvtTrX84zuMksQlt3EQc-7qJCx_KnZzFLC285oN1k-T8DH-usG-bWqIHnO2nak38eOvDazpj9jAxz95zFw3D7tQDtxdTE8vU00JBErQuPpWRa4D0S-rYv7pVWsV_8LEXVEmXLEUq70Us3MAtJ0yLlsRzoSynpJfc43sCCE1vdYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/evEQN-iltve1owyQKrUgyXgxPJ01AGj2Vf1PC_QI4bPCxELFa5HaGvCAopd_B9Cxbl35O80rPceoN9U6lJyDkKxctEYBZcgdyIvDh-20IKCaE_egPDpihhk4D-3sb4PKwUG5RlslQD1ea1ok57eIm3qlozOWAW5F6NP72qW2HbDFGynsEwS-RYC5SSyiRXdyPotxhP8qnmelvIgW_p05Ng4Dvn8_esv4J-aQxHpUaH5rnFuJINuVuTzqiyE7GiIKQnW6zIePqi5FfoArxRmTNGIIbzEJo4J8I9lolOhzz12phAir2EX9ud0LLJfysMdd8JkJ7GvVuMUnRRifnFPpjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pq9adBFmfpI1-3V0rcxwnSeQlumhK2T8k2_J6-3kdH8Zk6pi8-fmwWcjvL74H0urcCvDPUqGv9tquIV0xfQZ-Ueqaj0cX2SJgVf2ghqUfkZH_IypJ7hUd-37JrJseEe6IuvwjyFs9Nkgs1iDDhn-WPdVEs9m_6y75gdNLAkWqu9wJbU8z6lSH_-dHpJqNETsC-M-caQ14uuY7XY7d9yfCVs6yu5iRqNKDqDlRJnLKbWPVq88GK_pGXoIHt_T5gmqmaO2-lj3hjKYJT2IHT_EQu6D-0ljcPTPMwVZ1c6YwAbrDscqT1Vx7rU78Udt8mPDup3u9v4UuBryp8Bfkntb1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/egoFoJ6gv5uDY4j9bbfKb6FfDteDGf2om6WXEbiTlDzatac9LjQkQb_tXRyvjbB_c-SOAyoHQO4YdFIyCmC1pR_6o8Xfr3Z9z9a-rikKhNXZyhBSQe93SNjjQV0S3uvRkO-FUMbH3ATEKB94h3XLxM4EaAyFpPeQ9JUX_2k_Wu6mxxp4mtrZBzqePfgL-tlty9r3N1C4KRIJmgRyu7SduuHUWkbsW7juFhPVlqpgfU-fsuOEGPw2uq0ixkJkKP1fbbK_TtKh-rd4aFfgGqJ8bZVwHIlin36WHGaZC0FX3n0iVXUi_y8avrA7uhljbGP-1ZauQtewxvtmZlIMSNGaHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=EUXCThIbX3FG6RVVrJ3-CSDhCBZvtgh7KVP0QtDbB3nPaIwu-_aaMduBnm_F2NZARQdHBGW59PnhpoJHL7knUfPYUmrkx69Ytiz3aFSQnEILtcKA29Q7GKmL3f5figp0kgFi0RQ_Kdzfe2bWb8shf1z3chdaZ4cL0xZJ5n4oxw5cEzibcKahcpIEzWFjh0HdwjpN751qpF14zumXO0-mV1khSzWQDCTk6gEb9fFzBn7PiZj843dm46hLGa5hNYhmRTYCcmPaHKkdceI_CGlrsr6mSig12bSZEJX0wu-Fq-8VVsBmGqvjClej0ez3Gu_5_6661B-Jh1pDiBQYsdswLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=EUXCThIbX3FG6RVVrJ3-CSDhCBZvtgh7KVP0QtDbB3nPaIwu-_aaMduBnm_F2NZARQdHBGW59PnhpoJHL7knUfPYUmrkx69Ytiz3aFSQnEILtcKA29Q7GKmL3f5figp0kgFi0RQ_Kdzfe2bWb8shf1z3chdaZ4cL0xZJ5n4oxw5cEzibcKahcpIEzWFjh0HdwjpN751qpF14zumXO0-mV1khSzWQDCTk6gEb9fFzBn7PiZj843dm46hLGa5hNYhmRTYCcmPaHKkdceI_CGlrsr6mSig12bSZEJX0wu-Fq-8VVsBmGqvjClej0ez3Gu_5_6661B-Jh1pDiBQYsdswLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین طائب، رئیس سازمان بسیج مستضعفین، اعلام کرد صدها هزار نفر از ثبت‌نام‌کنندگان پویش حکومتی «جان‌فدا» در تهران سازماندهی شده‌اند و روند الحاق آنها به گردان‌ها و یگان‌های دفاعی جمهوری اسلامی آغاز شده است.
طائب روز جمعه ۲۷ شهریور در جریان رزمایش موسوم به «۳۱۳ هزار نفری جان‌فدایان ایران» در تهران گفت برای این افراد دوره‌های آموزشی مقدماتی و تکمیلی در حوزه‌های زمینی، هوایی و دریایی در نظر گرفته شده است.
این رزمایش از صبح جمعه در مسیر میدان امام حسین تا میدان انقلاب تهران برگزار شد.
@
VahidHeadline
حسین طائب، رییس سازمان بسیج، جمعه ۲۷ شهریور در همایش «جانفدایان ایران» اعلام کرد نیروهای آمریکایی «به‌زودی با شکست از منطقه خارج خواهند شد.»
رییس سازمان بسیج گفت: «جمهوری اسلامی از تمام ظرفیت‌های راهبردی و تنگه‌های دفاعی خود، از جمله تنگه هرمز، با قاطعیت حراست کرده و دشمن را وادار به تسلیم خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78434" target="_blank">📅 16:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaRrZ3tJXxdaSMSrHh7-4FZBCJRsEg-_Eebl4B8t4-XFCRTX-NrIrAdShDxmyysCEyzXNrp7DXkhsF7Pj47eT2uCdR2WDPfHx1APOedZy-NvxXZZw0JbKijbsmeDdeWf1mJvkM9VhGJEyZOt06ZrkCYoI4RQjEcDV9kVY5JVd4OSwTWibmSPu-_eF7E0b18jNMyLITjEo-vSxaEOWGyykz1JDGNSOVyiKySViqnTvBs5igkT2ueq3LN32yrdefyOyvb8RcrqfnXF1mmUd-XZN9hQ-FOmq_b_SLKilnfcI29sdGD1x642nDUavQeJMr5Xg9NrLS7BE4-VSpzsjz46kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کره جنوبی اعزام نیرو یا تجهیزات نظامی به خاورمیانه را در صورتی که به مشارکت سئول در جنگ منجر شود رد کرد، اما گفت کشورش ممکن است برای حفاظت از کشتیرانی تجاری و انتقال نفت در منطقه نقش بیشتری بر عهده بگیرد.
لی جائه میونگ روز جمعه ۲۷ شهریور در یک نشست خبری گفت: «هیچ اعزامی که به ورود یا مشارکت در جنگ منجر شود، انجام نخواهد شد.» او تأکید کرد کره جنوبی برای چنین هدفی «به هیچ شکلی» تجهیزات نظامی اعزام نخواهد کرد.
او در عین حال گفت سئول باید مانند دیگر کشورها «حداقل اقدامات لازم» را برای حفاظت از کشتی‌های تجاری، انتقال نفت خام و امنیت شهروندان خود انجام دهد.
دولت کره جنوبی در هفته‌های اخیر در حال بررسی احتمال اعزام نیرو یا تجهیزات نظامی برای کمک به تأمین امنیت کشتیرانی در تنگه هرمز بود.
دونالد ترامپ، رئیس‌جمهور آمریکا، از سئول به دلیل آنچه حمایت ناکافی از تلاش‌های آمریکا در ارتباط با جنگ ایران خوانده، انتقاد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78433" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78432">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lnc0YNa5MD7MnqViQv-NWlvNPqi0wjj0iG3MTrMduTy_DyX7s_Z90HOOhbHduaBTKVxiy2XfCHayNN4tMznT0YzPla60v8S1-fGMzERYwuCBzVtgG2zj7lIxT5rtBhxRZtYjLRuYnj02a41r9sA7eL6lNXcKAh8GbfwPTq4-EkBmBIyzMcgl9YtVv8c5dVJQreVQweCV3XaCXrd3trIJ2ITRhMeSCVh28Q5kOaCBm0zJhhmXe2nS3Lr8uwa97AQw90lC_hq9byuBBOe1JHJvADQuWUS0fKzMCRxG6IAomXqXm0I4Y-zIjidKk9u7lJisaV48I5CkLvNgeqnDPtwxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد یک نفتکش با پرچم توگو را هنگام عبور از تنگه هرمز هدف قرار داده و مدعی شد این شناور پس از اصابت و آتش‌سوزی متوقف شده است.
@
VahidHeadline
UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی درباره وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت (CSO) یک شناور گزارش داده است که یک نفتکش با پرتابه‌ای ناشناس مورد اصابت قرار گرفته و این برخورد باعث آتش‌سوزی در عرشه شده که اکنون مهار و خاموش شده است.
گزارش شده که همه خدمه در سلامت هستند و در حال حاضر تأثیرات زیست‌محیطی این حادثه تأیید نشده است.
UK_MTO
در گزارشی دیگر نوشتند:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) یک گزارش تأییدشده اما با تأخیر زمانی درباره حادثه‌ای دریافت کرده است که در ۱۶ سپتامبر ۲۰۲۶ رخ داده و طی آن یک نفتکش هنگام خروج از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
گزارش شده که خدمه در سلامت هستند. گزارشی درباره ارزیابی خسارات و تأثیرات زیست‌محیطی منتشر نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78432" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78431">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLVhWV5EzCGXd5l0NB738VjoGyhHhC0lKn8TQuewH53hHv3WNH9muFepsRsE5deRFVch6qD7ITphyL_abMdvD6uPazYr7FBAaE7gzGLiQFoVwJdrIGghWc6jJfeWj2_XLXh800fcfyHsUOmkcZKk7LEvfbZ7ZtboZNxcbHFy141ClRqgv3SgmVrdlaziy34kY6CILJuG-6xTVi_Ofu1g88f9KCG__k8JHr-4yeCbjBMbBNQaQkzNmVhEq368hRJr2qhh09ydPerdrEC_5UUYgHjVV7XVK3ngtTngXKEc493K6aIJ_EJq7RjwhWyvz98VohQX31Fy8dsjld6N5lK2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد کرمی‌اسد، جانشین پلیس راهور فراجا از جان‌باختن بیش از ۱۶۰۹ نفر در تصادفات جاده‌های برون‌شهری در شهریورماه خبر داد.
به گفته این مقام فراجا، این آمار به‌طور میانگین به بیش از ۵۰ نفر در روز می‌رسد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78431" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VcQJt24wtGRlJpboQINzQzJxWh2k0cvXORgZdlahS75Z2ul8YoL80NH2wCa32peOP_93VJPnLJ8G28xNi5Py2gm2DWvvosKGZMSCmDMH9huwZjWXaVHes-A3QCvsnc-j1qR19Y1EPCd8sz9VE4suTivM6IeAZBWFC6K4Tf_fh-ppjOf1LnLkhyo5ohSGHqqWkxUMspx4AHhdLEcxkKr3Kydu44gwLgUPbu-CVL8xvTPLU93HL45OSyPzPGnMtN8jrtivn4pH51IyKjXJQX8kl6Q_vwsoAThwPdE9mlmoOBw-JlPnUkEZmkOdXivl_jdDHlj8-Oac8BcqIuT7zgisqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=jqye7OTkavrvV0nIencF9uei8pbH9U9cSxGwQ68pazw9yaZSEar974N2E10dNXF1xAqSUFKlRQwgsRrycjAM05vrcpXWnJ319OMocfenQ0hrxud5qoo896pNkV3-wyaDs0ff2Kly6MAViICGx-PAJ8C8-1ZkIx_hH-knJ3BP6vl4UZ1JVHgiUnEAaMbiIOOXtfwmH7R2ghK0ftVBXfLZa3gb7B0dYL7ZdRLqYZOZVKKvxBhr0Py6Ef6At2UOXBXgkY0Izp2D2ku-LNqyQ5zdeeY71ssYYbItvt2eMu8ZA1OsBWwQ_eK4-4969kMvrWoJeiFWAjlGX_liES9H0iToyg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=jqye7OTkavrvV0nIencF9uei8pbH9U9cSxGwQ68pazw9yaZSEar974N2E10dNXF1xAqSUFKlRQwgsRrycjAM05vrcpXWnJ319OMocfenQ0hrxud5qoo896pNkV3-wyaDs0ff2Kly6MAViICGx-PAJ8C8-1ZkIx_hH-knJ3BP6vl4UZ1JVHgiUnEAaMbiIOOXtfwmH7R2ghK0ftVBXfLZa3gb7B0dYL7ZdRLqYZOZVKKvxBhr0Py6Ef6At2UOXBXgkY0Izp2D2ku-LNqyQ5zdeeY71ssYYbItvt2eMu8ZA1OsBWwQ_eK4-4969kMvrWoJeiFWAjlGX_liES9H0iToyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با انتشار ویدئوها و تصاویر مختلفی در شبکه‌های اجتماعی از وقوع درگیری مسلحانه در بامداد جمعه ۲۷ شهریور در شهر زاهدان، خبرگزاری برنا از کشته شدن یک مأمور نیروی انتظامی در این درگیری خبر داد.
ساعتی بعد خبرگزاری فارس اعلام کرد که در جریان این درگیری دو نفر از مهاجمان کشته شدند و یک نفر از آن‌ها دستگیر شده است.
وب‌سایت «حال‌وش» هم که اخبار سیستان و بلوچستان را منتشر می‌کند، می‌گوید از حوالی ساعت ۳۰ دقیقه بامداد جمعه در محدوده خیابان دانشگاه و اطراف خیابان دانشجو زاهدان به مدت دو ساعت تیراندازی رگباری رخ داد و سرنشینان یک خودرو پژو ۴۰۵ هدف حمله قرار گرفتند.
این رسانه به نقل از منابع خود همچنین افزود در این درگیری «یک فرد مسلح، سه نیروی نظامی و دو زن رهگذر مجروح شدند و چندین آمبولانس به محدوده خیابان دانشگاه و اطراف خیابان دانشجو اعزام و در برخی خیابان‌ها ایست‌های بازرسی برپا شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78426" target="_blank">📅 06:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxbVc_PhXV2vXfgJPbSJNNFv04FaeAWP1ODgWI_4xjt-tjnVSCOc0LNupluEmtjh1JRPJcV4C2q5TAlcAyauGOzj-iFSW51wN4kugpE9S300BmHBHjybFFxkd0yJZsjfFZ9ydyjF7eu-iQW6YveIEeGX1ZjO9HmPICkdvVtmsCsPx5Ot55tCjQ4vJuo9qE9y1ImTcMfDO8VjvG6SX-_e2KGqnzEoHMblVXGD7aOYu5UtVzH1saWhOtpO4yFOQD-uPhmJ9N8Rbe4FYGeoJ6fL3guCxDYSvD_K1x6Z-Nkz4VCLZxdlZW6wFFHNQyzOvtQVq5KxkFHA09shkYQvvbfFJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران بامداد جمعه ۲۷ شهریور در بیانیه‌ای اعلام کرد نفتکش «ترند» با پرچم کشور توگو، شب گذشته هنگام تلاش برای عبور از تنگه هرمز هدف قرار گرفته و پس از آتش‌سوزی متوقف شده است.
سپاه پاسداران در این بیانیه گفت که این نفتکش قصد «عبور غیرقانونی» از این آبراه بین‌المللی را داشته و هشدار داده است شناورهایی که به این شکل عبور کنند، با «نابودی» روبه‌رو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78425" target="_blank">📅 02:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NGYGYlibuPs9csrbcPpQ9Tk8LwxfEjqyhRTaP-7_zsdj-pN877ZC37fri0fyu4F1ZYhKrlFr1sgKB1xKWuL-R9B-au6AMU_vfCUPsC80QOHkhm-8patL1WKp79Khg0kg8DBCRBNvWlqNhZYwbyvxY9sR3Xyp17VdpI0Q2K-O2OHByRNX-DpIXtPsMT0hMwQi6MAx-CsS8ge91pbRatqNEt0hCD2TtEuOg_aTjo30YxU6BSWHgRtCTJ8iq2-uqMVe4cPk6Jmf0hM-OI1ebM8mgOf-t6EepsQGdsjPpeQZe_VMl_PGOWS87O9pcnfEEzGJl4BVxr345mJqT6WMkG_2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصبِ عمان، دریافت کرده است. گزارش شده که خدمه در سلامت هستند. تا زمان انتشار این گزارش، هیچ پیامد زیست‌محیطی تأیید نشده است. مقامات در حال تحقیق هستند.
به شناورها توصیه می‌شود با احتیاط تردد کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78424" target="_blank">📅 23:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78423">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iCRc5gjz1in9tSwFaiB09v_FXRpoMTniZ22tsypT8Ue1Y-SL6Eis0cSsb1gaG0AjmffNHVNIQgVr6U3Xrf4xLRCp-A5F4dVvR5tgOa-zn-CLbrImhNNMcU_b0eqWg0jbpowepNAAkeP0_OMcKg5jQsZcNqm-hv9XzsCOWeDwgCji6f4E0_1m7VsA7XKzx4S-65ylwi8xZASeEYc7GjTs1DTluKXqfVs4qRK93DYA3elNtG3nIHWcmIrdH7OYQczbzwj2esYdjw1aHDTweaqFjLn_A_OoHv89DpKglX_gyTTAgiXB8H_4kfhN5VCekvNRpUW1KR5rKxAM2dXE1tTgKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس می‌گوید در جنگ ایران به یک دوراهی بزرگ نزدیک می‌شود
ترجمه ماشین:
رئیس‌جمهور ترامپ روز پنج‌شنبه به اکسیوس گفت که در جنگ ایران به نقطه‌ای حساس نزدیک می‌شود و باید تصمیم بگیرد آیا برای پایان دادن به درگیری، حملات گسترده را از سر بگیرد یا نه.
▪️
«تصمیم بزرگی پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر اتفاقی ممکن است برای من بیفتد.»
چرا مهم است:
اگرچه ترامپ پیش از این نیز تهدیدهای مشابهی مطرح کرده، اظهارات تازه او در آستانه دیداری برنامه‌ریزی‌شده در روز سه‌شنبه با رهبران شش کشور خلیج فارس در حاشیه مجمع عمومی سازمان ملل متحد در نیویورک بیان شده است.
▪️
این دیدار می‌تواند مرحله بعدی جنگ را شکل دهد، از جمله اینکه آیا بار دیگر برای دیپلماسی تلاش شود یا اقدامات نظامی تشدید شود. اگر ترامپ بخواهد عملیات رزمی گسترده را از سر بگیرد، به همراهی متحدان منطقه‌ای خود نیاز خواهد داشت.
▪️
رئیس‌جمهور در روزهای اخیر چند بار گفته است که جنگ به‌زودی پایان خواهد یافت. برخی مقام‌های آمریکایی هشدار می‌دهند که این درگیری به بن‌بستی ناپایدار و «نه جنگ، نه صلح» رسیده است و معتقدند اگر تا آن زمان توافقی حاصل نشود، ترامپ ممکن است پس از انتخابات میان‌دوره‌ای دوباره به عملیات رزمی گسترده روی آورد.
آنچه او می‌گوید:
ترامپ در این مصاحبه روشن کرد که می‌خواهد از نشست سازمان ملل برای شنیدن مستقیم نظر متحدان منطقه‌ای درباره گام‌های بعدی جنگ استفاده کند.
▪️
ترامپ گفت: «می‌خواهم بفهمم در چه وضعیتی هستند و اوضاعشان چطور است. ما خیلی از آن‌ها محافظت کرده‌ایم.»
▪️
کشورهای شرکت‌کننده عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان هستند.
▪️
ترامپ از گفتن اینکه تصمیمش درباره مسیر پیش رو را قبل یا بعد از انتخابات میان‌دوره‌ای خواهد گرفت، خودداری کرد.
زمینه خبر:
در اوایل اوت، ترامپ پس از آن از ازسرگیری عملیات رزمی گسترده خودداری کرد که عربستان سعودی و قطر ابراز نگرانی کردند ایران در اقدامی تلافی‌جویانه تأسیسات نفت و گاز عربستان را بمباران کند.
▪️
از آن زمان، ترامپ رویکردی «کم‌سروصدا» در پیش گرفته است: تعلیق مذاکرات با ایران، آغاز کارزار تازه تحریم‌های اقتصادی، ادامه محاصره دریایی بنادر ایران و متمرکز کردن ارتش آمریکا بر بازگشایی تنگه هرمز و افزایش جریان نفت به بازار جهانی انرژی.
▪️
ارتش آمریکا عبور نفتکش‌ها و کشتی‌های حامل گاز از تنگه را به‌طور قابل‌توجهی افزایش داده است. با این حال، ترافیک همچنان پایین‌تر از سطح پیش از جنگ است و قیمت نفت نیز همچنان بالاست.
وضعیت فعلی:
به گفته مقام‌های آمریکایی، ترامپ و پیت هگست، وزیر دفاع، به ارتش دستور داده‌اند سطح نیروهای خود در خاورمیانه را تا پایان سال حفظ کند تا برای احتمال بازگشت به نبرد تمام‌عیار آماده بماند.
▪️
این مقام‌ها می‌گویند ترامپ باید به‌زودی درباره مسیر پیش رو تصمیم بگیرد، بخشی از دلیل آن این است که ارتش آمریکا نمی‌تواند خیلی بیشتر در وضعیت فعلیِ انتظار باقی بماند. یکی از این مقام‌ها گفت: «بالاخره در مقطعی باید تصمیم بگیرید که هدف نهایی چیست.»
▪️
ترامپ به اکسیوس گفت از اینکه محاصره دریایی مانع صادرات نفت ایران شده، بسیار راضی است. او گفت: «از وقتی شروع کردیم، حتی یک کشتی هم به ایران نرفته است. تلاش کردند و ما آن‌ها را منفجر کردیم.»
▪️
رئیس‌جمهور افزود که ایران مستقیماً با آمریکا در تماس است و گفت ایرانی‌ها همچنان خواهان دستیابی به توافق هستند.
تصویر کلی:
کاخ سفید همچنین در حال کار روی یک راهبرد پس از جنگ است که خواستار تلاشی منطقه‌ای برای مهار ایران و هم‌زمان گسترش عادی‌سازی روابط میان اسرائیل و همسایگانش است.
▪️
هرچند این طرح هنوز در مراحل ابتدایی تدوین قرار دارد، هدف آن هدایت رویکرد آمریکا در خاورمیانه پس از پایان جنگ ایران و در دو سال پایانی دوره ریاست‌جمهوری ترامپ است. دو رویداد بزرگ بر این برنامه‌ریزی سایه انداخته‌اند: انتخابات ۲۷ اکتبر در اسرائیل و انتخابات میان‌دوره‌ای آمریکا در نوامبر.
چه چیزی را باید زیر نظر داشت:
وقتی از ترامپ پرسیده شد آیا هفته آینده در نیویورک با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد، گفت: «شاید.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78423" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78422">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKRB0NylQ5yFUT9Yo38wH7skc7t7IAXgXK4J4jXpjtBnk9-4N8ym9-i-Pjv3JgWBbZPTOLs8bpCP0VetNDbJWWcffMt55ndgdauLBOO17x_q0UILhfVY5gehMl8aF-le6MAh7Wu5MVgJB8CJ8D2cQMHQzPn6FeQ4D1HaIhFRH288biAf0QEAmtxfoaY5ficxkp45W23zQbc5yez9hsyv04CzkvnFQkbopdHVfxxZm9ASIaqkQGVDQyJ5bbImJUjGopRUPn5hkgpkVBHyXRl-xjXV5Iy76mitoAWQ1ew9uk7luMvX2w1rEDAv94d_DFDEEWDoNBLf7HS1YFT74qOwYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز پنج‌شنبه ۲۶ شهریور به نقل از مقام‌های آمریکایی گزارش داد نیروهای جمهوری اسلامی در روزهای اخیر دست‌کم دو پهپاد ام‌کیو-۱ آمریکا را سرنگون کردند.
مقام‌های آمریکایی که به شرط فاش نشدن نامشان با سی‌بی‌اس نیوز گفت‌وگو کردند، مشخص نکردند این پهپادها در کدام بخش منطقه سرنگون شدند و از کدام مدل ام‌کیو-۱ بودند.
این پهپادها برای ماموریت‌های اطلاعاتی، شناسایی و نظارتی طراحی شده‌اند و قابلیت حمل موشک‌های هلفایر را نیز دارند. سی‌بی‌اس نیوز نوشت این پهپادها در تنگه هرمز می‌توانند برای نظارت مستمر بر آبراه، رصد فعالیت‌های نظامی جمهوری اسلامی و شناسایی تهدیدها علیه نیروهای آمریکا و کشتیرانی تجاری به کار گرفته شوند.
بر اساس گزارش دفتر بودجه کنگره آمریکا، از آغاز جنگ آمریکا علیه جمهوری اسلامی دست‌کم ۲۴ پهپاد ام‌کیو-۹ ریپر به ارزش تقریبی ۷۲۰ میلیون دلار از دست رفته‌اند. یک پهپاد ام‌کیو-۴سی تریتون به ارزش حدود ۱۵۰ میلیون دلار نیز منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78422" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78420">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VDs3C9EXR9uJMg6Mb0RVsvV43oCYCYL7i8Gk7SxogYvjQ0AZSzIEc4SBRif3xfu-GxVV35igEZ5GZSNZtak00ckghI82ClVritBhV8OdEA_ckJ_hAU8thZZHb-OkaLo4oLJ-s5pIi0phxSUD3GNt8-VAhz8kPNoFCEiSFPidE1woMtSDZ4B264rFQ-B3kiVD8IkwuGoY88_5O3B-Hk8xPjpa4LueAHd6Godtrz7WNKxM5e0bM1P9b_PHfE3wTQ92031VmX_TV5sxpIt21ZpwRr63DES487t8qbUYfeRFGQSaTz_jpGjNBs1AWFjULfGBW-_w1JBWARHXgRYai2nhiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=mzJKCpF_dI-N3oQPSAvHgkAbyolQ8Jy5R-8ccDEIOtujDv3CTgFgil_dIBNJ5bh60ooCLwwcpgdLgBFUFIJX1AfMZJj7zJDjx5gvVLPdu1P53Mv_JJU_YCdcZAoPga2YmrW_y4UyaqIEQmc2lAn_N7dWT6KmIUwP0n0PcW0lsIG4H0RYpSiVcqM17qU0YUZBBE2E_luHNlajhYQOctSNTi6WnSNC2ugyavL549eV8flNDox8IXXMkCGdNyNe-RkqCvLxZn409zkFKx2LmdVetUVGK6FqgkWq_USWoZxqi5bSiPYM5ofq_WH0QzgRz_yknYl9KUa5aRCVJjEI4Oq7rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=mzJKCpF_dI-N3oQPSAvHgkAbyolQ8Jy5R-8ccDEIOtujDv3CTgFgil_dIBNJ5bh60ooCLwwcpgdLgBFUFIJX1AfMZJj7zJDjx5gvVLPdu1P53Mv_JJU_YCdcZAoPga2YmrW_y4UyaqIEQmc2lAn_N7dWT6KmIUwP0n0PcW0lsIG4H0RYpSiVcqM17qU0YUZBBE2E_luHNlajhYQOctSNTi6WnSNC2ugyavL549eV8flNDox8IXXMkCGdNyNe-RkqCvLxZn409zkFKx2LmdVetUVGK6FqgkWq_USWoZxqi5bSiPYM5ofq_WH0QzgRz_yknYl9KUa5aRCVJjEI4Oq7rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز پنجشنبه ۲۶ شهریورماه در مراسم تقدیر از کارکنان برگزیده شاباک در بیت‌المقدس گفت اسرائیل بخش عمده ماموریت خود در برابر جمهوری اسلامی و گروه‌های متحد آن را انجام داده، اما این ماموریت هنوز به پایان نرسیده است. او گفت توانایی ایران و متحدانش برای آسیب رساندن به اسرائیل به‌شدت کاهش یافته است.
نتانیاهو با اشاره به ادامه عملیات اسرائیل گفت: «هنوز کارهایی برای تکمیل باقی مانده است و ما آن را به پایان خواهیم رساند.» او سپس تاکید کرد که اسرائیل حماس را از بین خواهد برد و در مورد جمهوری اسلامی گفت: «حکومت ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سرنگون خواهد شد.» او همچنین گفت اسرائیل به اقدامات خود علیه حزب‌الله ادامه خواهد داد.
نخست‌وزیر اسرائیل همچنین گفت خواست ایران و گروه‌های متحدش برای نابودی اسرائیل از بین نرفته، اما به گفته او، توانایی آن‌ها برای تحقق این هدف به‌شدت تضعیف شده است. این اظهارات در مراسم تقدیر از کارکنان برگزیده شاباک برای سال ۲۰۲۵ مطرح شد که با حضور اسحاق هرتزوگ، رئیس‌جمهوری اسرائیل، و داوید زینی، رئیس شاباک، برگزار شد.
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در شبکه اجتماعی اکس نوشت کارزار نظامی اسرائیل هنوز پایان نیافته و این کشور «اهداف مهمی» در برابر ایران و جبهه‌های دیگر دارد.
او گفت اسرائیل برای دستیابی به این اهداف «با قدرت نظامی و تدبیر سیاسی» اقدام خواهد کرد.
کاتز روز پنجشنبه ۲۶ شهریورماه با اشاره به غزه گفت سیاستی که همراه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دنبال می‌کند بر سلب توانایی گروه‌های جهادی برای حفظ قلمرو، زیرساخت‌ها، فرماندهان و تجدید قوا متمرکز است. او افزود اسرائیل این رویکرد را در غزه، لبنان و شمال کرانه باختری اجرا کرده است.
وزیر دفاع اسرائیل همچنین گفت این کشور فرماندهان «سپاه فلسطین» در ایران را هدف قرار داده و اجازه نخواهد داد ایران یا هیچ طرف دیگری حماس را دوباره مسلح کند. او تاکید کرد اسرائیل به عملیات خود برای تحقق اهداف امنیتی و جلوگیری از تکرار حمله‌ای مشابه هفتم اکتبر ادامه خواهد داد.
کاتز همچنین رجب طیب اردوغان، رئیس‌جمهوری ترکیه، را خطاب قرار داد و گفت اگر می‌خواهد به همفکرانش در غزه کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما «قدم به غزه نخواهد گذاشت».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78420" target="_blank">📅 21:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78419">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCSPzw7LJSj6iBB1iZ_2h1uNWQS1HiJt30RpQikD6AmkE98w_PCF-NUDEFjXsy0-_Fsh9S8ZEVpGEBlMTvwI3kHyuRM98M9gZh3YYtFlItT8CUDaWCMbydBgT4jNHkj2p0wic3zWgBr5HHl3e-LnqIMYBJD0UN0yEhcH3EjNzcqtfQzlH1_PEdkACokehsuXV4r1mkeGYg-xIUVI1DHH3Zr6PJtok_ob9P4JlUGSauXnUffMmppen_UtbiXqDcr-eyym4AyAfaFoienfLQZaSSglEQYxq_uHIwSJyWEOdsQxtDTDG1dxNM3_6kFUj1NG2ItW7X2Yxdiv57LCjkaSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیات حقیقت‌یاب مستقل بین‌المللی سازمان ملل درباره ایران در تازه‌ترین گزارش خود اعلام کرد دلایل معقولی برای این باور وجود دارد که آمریکا در جریان جنگ با جمهوری اسلامی، در دو حمله هوایی به ایران مرتکب «جنایت جنگی» شده است. بر اساس این گزارش، این حملات دست‌کم ۱۷۸ غیرنظامی، از جمله زنان و کودکان، را کشت.
این هیات در گزارشی که به شورای حقوق بشر سازمان ملل ارائه شد، حملات آمریکا و اسرائیل به ایران در ۹ اسفند ۱۴۰۴ را بررسی کرد و به این نتیجه رسید که آمریکا در دو مورد حملاتی بدون تمایز انجام داده که به کشته یا زخمی شدن غیرنظامیان و آسیب به اماکن غیرنظامی منجر شده است.
بر اساس یافته‌های هیات حقیقت‌یاب، در یکی از این موارد، موشک‌های تاماهاوک به دبستان شجره طیبه در میناب اصابت کردند. این هیات اعلام کرد این مدرسه به وضوح قابل شناسایی بوده و در این حمله بیش از ۱۵۰ نفر، از جمله حدود ۱۲۰ کودک، کشته شدند.
در موردی دیگر، آمریکا با استفاده از موشک‌های تهاجمی دقیق، ساچمه‌های تنگستن را بر فراز یک مجموعه ورزشی و منطقه مسکونی در لامرد پراکنده کرد. بر اساس گزارش، این حمله ۲۲ زن و مرد غیرنظامی را کشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78419" target="_blank">📅 21:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78418">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpZg58aUO3zkJTHlMd3N6B3l-tgX2R4LyCnPs0KK_lZJbT5YYXZeJelh0aDRV65QXGXi06L1xb4PKGAQda3i_-__8ZxtLM1oq_f1vQ6cpl7bY7xgrqlDhBqg0To2sgjZ6R_x4qBqEU0ATUUPJgHWjm_t51dHq3vpGTiai5xVAIXBV7LdW4CvH_mS8IdEso6_8puUsccEqfOga6Onmu4-6BJE71g1cCuXKnlRQ7fdkVQElpBlNhWcQlg2Bj9b5T87-s_9Nob0qHY1gsAt8sEZnN8327OP8z-xUp0cGiVLCjVQLOMN2PpY814GM0IIqgnPnojQ7V9Xy1Ct4SNUUjZjsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه و چین روز پنجشنبه، ۲۶ شهریور، در نشست شورای امنیت سازمان ملل متحد، پیش‌نویس قطعنامه پیشنهادی ایالات متحده برای تمدید ماموریت هیات کارشناسان کمیته تحریم‌های ۱۷۳۷ علیه جمهوری اسلامی ایران را وتو کردند.
این نشست با ابتکار فرانسه که در ماه سپتامبر ریاست دوره‌ای شورای امنیت را بر عهده دارد، در چارچوب دستورکار «منع اشاعه» برگزار شد. در جریان رای‌گیری میان ۱۵ عضو شورای امنیت، این قطعنامه ۱۱ رای مثبت کسب کرد، اما با مخالفت صریح (وتو) مسکو و پکن و همچنین رای ممتنع پاکستان و سومالی مواجه شد. برای تصویب یک قطعنامه در این شورا، علاوه بر کسب حداقل ۹ رای موافق، وتو نکردن اعضای دائم الزامی است.
دیپلمات‌ها پیش‌تر از مخالفت قطعی روسیه و چین با این طرح خبر داده بودند. مسکو و پکن معتقدند که با انقضای قطعی قطعنامه ۲۲۳۱ برجام در اکتبر ۲۰۲۵، تمامی سازوکارهای تحریمی پیشین از جمله کمیته ۱۷۳۷ فاقد هرگونه اعتبار و اثر حقوقی هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78418" target="_blank">📅 18:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78417">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/caed21affc.mp4?token=udFy5y-znLpJqkYi0OYSHouhNI4I78iFUR55hH1gayWT072SOYtz7lwntKgf6SlPCrJUritKfGyvUH4OP709z4f7K5TLUbws7or4A6nZ6YC_4ZenR6H8KADL7DO5N6Qgep9EuhUrWkaG93UlYZNRfVSBGMaFiPzW8r_ejcWM-jFzcGNrbLYLXPHc-K5IQU3EzeYkrgHV_jjDmG9rTLfis2_Yn8ev5Y5oJ_cqGV6ZzZoX8MIO2DrBlXSPeODYQIUUWpE0lvgkBKgCmw_8SSyw_WuaOYwb9jgIWhnofIw64wwkY43bwl4VFKQn_hG3Iq-JJeD3GfdUDzq7ZCkNju1ZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/caed21affc.mp4?token=udFy5y-znLpJqkYi0OYSHouhNI4I78iFUR55hH1gayWT072SOYtz7lwntKgf6SlPCrJUritKfGyvUH4OP709z4f7K5TLUbws7or4A6nZ6YC_4ZenR6H8KADL7DO5N6Qgep9EuhUrWkaG93UlYZNRfVSBGMaFiPzW8r_ejcWM-jFzcGNrbLYLXPHc-K5IQU3EzeYkrgHV_jjDmG9rTLfis2_Yn8ev5Y5oJ_cqGV6ZzZoX8MIO2DrBlXSPeODYQIUUWpE0lvgkBKgCmw_8SSyw_WuaOYwb9jgIWhnofIw64wwkY43bwl4VFKQn_hG3Iq-JJeD3GfdUDzq7ZCkNju1ZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خشونت و آزار جنسی)
ویدیو نشان می‌دهد ماموران فرماندهی انتظامی جمهوری اسلامی ایران یک نوجوان را مورد ضرب و شتم و آزار جنسی قرار داده‌اند.
این ویدیو خشم بسیاری از کاربران را برانگیخته است. برخی  گفته‌اند که «وقتی پلیس مقابل دوربین دست به چنین کارهایی می‌زند، معلوم نیست در بازداشتگاه و پشت درهای بسته چه به سر بازداشت‌شدگان می‌آورد.»
فرمانده انتظامی آذربایجان شرقی گفته که این اتفاق ۱۴ خرداد ۱۴۰۵ در جریان یک نزاع خیابانی در تبریز رخ داده است.
برخی هم با اشاره به انتشار این ویدیو در چهارمین سالگرد کشته شدن مهسا (ژینا) امینی در بازداشت گشت ارشاد، به تداوم خشونت پلیس در سایه نبود قوانین بازدارنده اشاره کرده‌اند.
پس از پربازدید شدن این ویدیو، فرمانده انتظامی استان آذربایجان شرقی گفت که ماموران حاضر در ویدیو «تنبیه انضباطی» شده‌اند.
علی محمدی به خبرگزاری فارس گفت که این افراد «تنبیه و انتظار خدمت» شده‌اند و «اقدامات تنبیهی تکمیلی» در مورد آنها در دست اقدام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78417" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78416">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WqxS_8eUeEBQCqkg1Z0hIrNoVscLBWgdl6M3xVdIwpzEz4ayxkONOalbFFxsGhl5gz0_ylZnRGkpbXPELqtTZAY5-xDBhNLBdUn2Yq7W4JgW6ROb85jUymnTFnJMRSauOOuVVu3YyCgV_SFB3chJK5yWn-lhEhfkCsHpMtF7YRhizXUy7H9ELkfck2vgXPK6YnPei8NdroO0ygCfjIqxOuIn9x_xMl25gGBOJNmzbmJ7XV5lYgiH_Yg_cimfpCWB-SFw-Hhv1V2Qn96o16joT6iDnJ3ow4TxLb1t6CvtRdxs5XU6nXKF_rpmfz1whrGot_e82YH8XWI5MXcKyq2Opw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، مدعی شده است جمهوری اسلامی مستقیما با دولت او تماس گرفته و «بسیار» خواهان دستیابی به توافق با ایالات متحده است. او همچنین ابراز امیدواری کرده جنگ نزدیک به پایان باشد.
ترامپ بامداد پنج‌شنبه ۲۶ شهریور ۱۴۰۵، پس از ورود به ایالت کارولینای شمالی، در پاسخ به پرسش خبرنگاران درباره مرحله کنونی جنگ گفت: «امیدوارم به پایان جنگ نزدیک شده باشیم.»
او سپس درباره احتمال دستیابی به توافق با جمهوری اسلامی گفت: «آن‌ها می‌خواهند توافق کنند و خواهیم دید چگونه پیش می‌رود.» ترامپ در پاسخ به این پرسش که آیا پیام ایران از طریق میانجی‌ها منتقل شده یا تماس مستقیمی صورت گرفته است، گفت این تماس «مستقیم» بوده، اما درباره زمان، سطح و محتوای آن توضیح بیشتری نداد.
رییس‌جمهوری آمریکا ساعاتی بعد در یک گردهمایی انتخاباتی در شهر گاستونیا در کارولینای شمالی، بار دیگر گفت جنگ با ایران به‌زودی پایان خواهد یافت و «پایان واقعا خوبی» خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78416" target="_blank">📅 03:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fyYrflCxmWIpvUsTRysX4trlSObC7N9qMdfX0bfY6E7ZWVeg1C2VIa7YIRiVE4-KBFUScrpsg2qtYe4fWXfVLTngq384RHXcg6338LlETZ-68lDSd5fd57m1p2BfNGGa1PusSDOl0szu0qlX8X99re2RLl7p0qxJXB8NEGleLSzOGI3Pcju1y2BcQ2bFTTHiRBrW8Vhg_7ZkBnqOWvUEHDUvnZvAWl2e2zdktLlJTMKuZr1zDjl501OJVyYTVISA-eTmwNxEglcYY9xnApAounb2hQL8L9CqsZOxsRg30LBPgMhsCtXtYb_Pj0EHbRzACuTUIBuXkE4816QZMV8TBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هواپیمایی ماهان چهارشنبه ۲۵ شهریور در اطلاعیه‌ای اعلام کرد پروازهای این شرکت در مسیر تهران-مسقط-تهران از ۲۶ شهریور، برابر با ۱۷ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان دلیل لغو این پروازها را اعلام مراجع هوانوردی عمان عنوان کرد.
این شرکت همچنین در اطلاعیه‌ای جداگانه اعلام کرد بنا بر اعلام مراجع هوانوردی ترکیه، پروازهای ماهان از ایران به مقصد ترکیه، شامل استانبول، آنکارا و بالعکس، از ۳۰ شهریور، برابر با ۲۱ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان افزود آخرین پروازهای این شرکت در مسیرهای تهران-استانبول، تهران-آنکارا و بالعکس روز ۲۹ شهریور انجام خواهد شد.
خبرگزاری عصر ایران نیز سه‌شنبه ۲۴ شهریور به نقل از یک منبع آگاه گزارش داده بود دولت گرجستان در پی تحریم‌های جدید آمریکا، پرواز همه شرکت‌های هواپیمایی ایرانی به این کشور را از دوشنبه آینده متوقف می‌کند.
عصر ایران افزود بررسی این رسانه از چند آژانس گردشگری نشان می‌دهد فروش تورهای گرجستان نیز تنها تا یکشنبه ۲۹ شهریور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/78415" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/foBpl_s0UFJQtQinXX01eD7kArfRHPMevNSataUZHwyJqcRPhBeRBSSb07si1YlKAXvSEEoNa0npV4smQ6KLH_7UeN8tD5QN7fdzIgwq2YXqCBtNgJTGw996tijh13kaUkFXUrvZPhMhqsvSriNTUkpTCXUb8qzxjYkpgBsGwirNVCrDadfa89eUToQ2WzT48jjq8vXUXn6bNDSRdBL_fy3y6GQzmZbgL3mpB43Aa2dEFHBumIB3PlucGMP_ulvYfuIDfwPODNrKhIvNBvMWx--G4KC2V3AM73FiQBvvYK3k-AnJuyHRWK2TAzGNKNJqokkU7-BtZ8Fgfv6NnG8Q7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل قدیانی، زندانی سیاسی محبوس در زندان اوین، روایت جمهوری اسلامی درباره نقش «تروریست‌های وابسته به بیگانگان» در کشتن معترضان دی‌ماه ۱۴۰۴ را رد کرد و نیروهای حکومتی را مسئول «قتل عام» آن‌ها دانست.
قدیانی در بیانیه‌ای که روز ۲۴ شهریور از بند هفت زندان اوین نوشته، با اشاره به راهپیمایی ۲۲ بهمن و تجمعات حکومتی ماه‌های گذشته پرسیده است اگر عاملان تیراندازی به معترضان، آن‌گونه که حکومت می‌گوید، «تروریست» بوده‌اند، چرا در تجمعات حکومتی که در امنیت برگزار شده‌اند، اثری از آنها نبوده است.
او از رسانه‌ها و نهادهای حقوق بشری خواسته است درباره این تناقض در روایت جمهوری اسلامی پرسشگری کنند و نوشته است: «تروریستی در کار نبوده و نیست و قاتلان [...] همان نیروهای [...] حاکمیت‌اند.»
قدیانی همچنین در این بیانیه علی خامنه‌ای و پسرش مجتبی خامنه‌ای را مسئول این «جنایت سهمگین» دانسته و نیروهای حکومتی را به تیراندازی به معترضان متهم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78414" target="_blank">📅 17:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78413">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pY1y2ga44tcDhmwF3XgXOJda8-jBiq_ifMPgnklAlzswU8sikTVAoL7vJQ3C_fqfNLNAW02f_AeIPpL9SnotAoS4f8d7dj3heb8Z6GmpntwPcXUOvyC7qIMmaqJ3Ez7bK88mnW17_N0Y4fuHMEzzp0FjVZZB_RqHRer1FKQDduaZYW6yxGICP4wqFD9Wr2RL6YS4jTodran910H6cDUzAgjsY8rlyzzHcpMDRVfPdQVyyoOeEjmCiu-eXs-HM0wlmg8LbZGCqoP0opx2r0raoULwRr44c-U2LzOPLAnGCv0we02igHfgDl3p4N2GLIKlpj-Xhott25MdgEzw5WSvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین با صدور بیانیه‌ای اعلام کرد که وانگ ئی، وزیر امور خارجه این کشور، روز چهارشنبه در دیدار با عباس عراقچی در پکن گفت:
چین، ایران و ایالات متحده را تشویق می‌کند تا عقلانیت خود را حفظ کرده، خویشتن‌داری نشان دهند، به یادداشت تفاهم اسلام‌آباد بازگردند و «در گفتگوهای ماهوی درباره مسائل مورد علاقه طرفین مشارکت کنند.
براساس این گزارش، وانگ با بیان اینکه چین «نمی‌خواهد شاهد سرایت بیشتر تنش‌های منطقه‌ای به یمن و دریای سرخ باشد» افزود: «ما از همه طرف‌ها می‌خواهیم اقدامات موثری برای بازگشایی هرچه سریع‌تر تنگه هرمز انجام دهند.»
وانگ همچنین گفت که سیاست چین در قبال ایران همواره ثابت و پایدار بوده و چین مایل است ارتباطات و هماهنگی‌های خود را با تهران تقویت کند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، چهارشنبه، ۲۵ شهریور در سفر به پکن با وانگ یی، وزیر خارجه چین، دیدار کرد و بر گسترش روابط تهران و پکن در چارچوب مشارکت جامع راهبردی تاکید کرد.
عراقچی شرایط کنونی منطقه را ناشی از حملات نظامی آمریکا و اسرائیل به ایران دانست و از مواضع چین در محکوم کردن اقدامات این دو کشور قدردانی کرد.
او گفت: «جمهوری اسلامی ضمن آمادگی کامل برای دفاع مقتدرانه از حاکمیت ملی و تمامیت سرزمینی و صیانت از امنیت و منافع ملی ایران در مقابل متجاوزان، از راه‌حل‌های دیپلماتیک که حقوق ملت ایران را تامین کند، استقبال می‌کند.»
عراقچی همچنین گفت شرایط منطقه پس از جنگ ایران تغییر کرده است و در نظم جدید منطقه‌ای که با گفت‌وگو و همکاری کشورهای منطقه همراه خواهد بود، جایی برای حضور و دخالت نیروهای خارجی وجود ندارد.
او با اشاره به آنچه نقض مکرر تعهدات از سوی آمریکا خواند، گفت جمهوری اسلامی خواهان بازگشت آرامش به منطقه و روابط دوستانه با همسایگان است و در همین راستا گفت‌وگو با کشورهای منطقه را آغاز کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78413" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dt7qnCrVlS9JgpgoVYfe89jXn6y3xv0t-Nns43ZhJKyq7n70oha5PME8Dh6NAkQNkvK-kYvZtbgvYbPPA1cmXOTEYg2aw6cHeeu7n1OPMYGwXCyfK44zAvAC5n0S21HvJ2MajCLYb3iGE1f_9fh8BnlYDO1wO8EyvJNO2Ec78_xAubMp4J0DTMPTTr1Zsce2506z2U5byt-qQ51LC39EITfjt4MwS7VNt7PZByxd6eycHAz4ZET_oQpkhe_f1j-334Qeb3jWk9pNvZ_A8qWFOWU-ZZPjekcm_xp1YI3mEtnFbHIzMwEuK0-b5uXTT69e4vwRjvNpd67T5c_OIrWVuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز چهارشنبه ۲۵ شهریورماه به نقل از پنج منبع آگاه گزارش کرد که مقام‌های ایالات متحده آخر هفته گذشته (روزهای شنبه یا یکشنبه) با نمایندگان شورشیان حوثی مورد حمایت جمهوری اسلامی ایران، دیدار کرده‌اند.
براساس این گزارش سه تن از این منابع که خواستند نامشان فاش نشود گفتند این دیدار که رسانه‌ای نشده بود، در سفارت آمریکا در مسقط برگزار شد. دو منبع دیگر نیز اشاره کردند که دولت عمان، به عنوان میانجی باسابقه منطقه‌ای، به برگزاری این نشست کمک کرده است.
دونالد ترامپ در سال ۲۰۲۵ و پس از بازگشت به قدرت حوثی‌ها را در فهرست «سازمان‌های تروریستی خارجی» قرار داد و هرگونه حمایت از این گروه را جرم‌انگاری کرد.
ترامپ روز شنبه گفت حوثی‌ها با دولت او تماس تلفنی داشته و از ایالات متحده خواسته‌اند از جنگ یمن دور بماند. جی‌دی ونس، معاون رئیس‌جمهوری هم روز دوشنبه بدون ارائه جزئیات تاکید کرد که ایالات متحده در تماس مستقیم با این گروه است.
دو منبع آگاه اعلام کردند در این نشست که به گفته یکی از آن‌ها روز یکشنبه برگزار شد، حوثی‌ها به مقام‌های آمریکایی گفته‌اند قصد حمله به شناورهای آمریکایی را ندارند و به آتش‌بس سال ۲۰۲۵ با آمریکا متعهد هستند.
یکی از این منابع که یک یمنی است، گفت این گروه همچنین اعلام کرده‌اند که به کشتی‌های اسرائیلی یا هرگونه کشتی تجاری دیگر، به‌جز کشتی‌های متعلق به عربستان سعودی، حمله نخواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78412" target="_blank">📅 17:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78411">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uc7HO_AjVgkeO53CJXSjx2Bdj_VApe-6TsHE_jC21GFb0qti6-sRzbjgX4dh0CUnXLzE0CvMHgF_8VFDSCKltcFH1FwDY8WxiWN-XvWfiqO_RXgaifyedRYwixcjEdFdKu3J_i5h_wR0E8G92HGev6eG0beWg5oc3O7ByySqAVDthwQYrQKgTd2GF2yzv2IWcnJqkcxAHenSzegoaDXR4xdORkfw23-nreACyFcA5uSmDORnM3Z1MxhJgM2o7URe6VSvswHwd_QJKutM1_qJMLirFo7TNmWsXtqgv33Ca3nc7JVrA55nQhW7LqVONRm8WlKdN4hBzKLTwhjrpIH2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جی‌دی ونس‌»، معاون رییس‌جمهوری آمریکا، گفته است جنگ با جمهوری اسلامی طی «یکی دو ماه آینده» وارد مرحله‌ای کاملا متفاوت خواهد شد و واشنگتن در مرحله بعدی باید مانع بازسازی توانایی‌های هسته‌ای و نظامی حکومت ایران شود.
ونس همچنین با پیش‌بینی «دونالد ترامپ» همراه شده است که جنگ پس از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت؛ هرچند توضیح نداده منظور از «مرحله متفاوت» تشدید عملیات نظامی، کاهش درگیری‌ها یا آغاز روندی دیپلماتیک است.
معاون رییس‌جمهوری آمریکا در گفت‌وگو با نیویورک‌پست که روز سه‌شنبه ۲۴ شهریور ۱۴۰۵ منتشر شد، گفت: «نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم رییس‌جمهوری درست می‌گوید که این مسئله طی یکی دو ماه آینده وارد مرحله‌ای کاملا متفاوت خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78411" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ACX-xWehrTFdB9kpHEJbGTP_t6UHodnjOktiq-9UbgXbAD_MaLmF4g3gSCGzRdiZHwDf9TT7VAha4zle775DSEUNDtuWDGsIMlrG3cgaoauqwW5VObtMcA6DcGrlLIfIrpBfWX-XLkw0w-ORlHQmF3l1W4vDkza3_Sg9RvO0b1GqFnQTMeLP4WBS82rslDlZUFCZxg45zGGLG1lgN8Lrmy3DUdsTgQO1rMLPsLg0VFCR9UkLAdnIzyM5Jb8-GapwFCoNtka6YEE5YiTRpHF4aIu48UeUnvPYs4JFR3pl7Nva5SKQi87w-f6J6W2r9S8GtcBLGETYCiiPH8esdnihUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین قشقایی، همسرش سارا شمسایی و ابوالفضل قشقایی، برادر حسین، از معترضان دی‌ماه، پنجشنبه ۱۹ شهریور بازداشت شدند.
حسین قشقایی و سارا شمسایی در لاهیجان به دست نیروهای وزارت اطلاعات بازداشت و به اراک منتقل شده‌اند.
محل دقیق نگهداری آنها مشخص نیست و احتمال می‌رود در بازداشتگاه اداره اطلاعات اراک باشند.
ابوالفضل قشقایی نیز همان روز در زرندیه ساوه بازداشت و به اراک منتقل شد. به گفته یک منبع مطلع، ماموران هنگام بازداشت با خشونت وارد منزل شدند و گوشی‌های تلفن، تبلت و لپ‌تاپ اعضای خانواده را با خود بردند.
حسین قشقایی با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «اغوا و تحریک به جهت برهم زدن امنیت کشور به جنگ و کشتار»، «نشر اکاذیب در فضای مجازی» و «اجتماع و تبانی علیه امنیت ملی» روبه‌رو است.
درباره اتهام ابوالفضل تاکنون اطلاعاتی به خانواده اعلام نشده و پرونده این سه نفر هنوز به شعبه‌ای ارجاع نشده است.
از دی‌ماه، سیم‌کارت‌های حسین و سارا و حساب بانکی حسین نیز مسدود شده بود. آنها ماه گذشته به دادسرای عمومی و انقلاب زرندیه احضار شده بودند، اما در مهلت پنج‌روزه تعیین‌شده حاضر نشدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78410" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78405">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=ErCwAzRbcRLW5AYEKtPms0jHAw9f1Fam55I_tdJGL6DMEzhdgVjqSr4l6ZGPe-86hPy_rD8_u53LEnwfauqj3Pyx6Le1iNi6NXMyLzd7tlpy94e_1-JxDna9agPbPP-nDMSgynPolftBLHBFJdtiWkQNDyuGPYVFx9qLgh1Fju0tdr59O_aRUzjhKTuSJwGgTt__38ca5xaLc8n8SrST-oGfep-62nf0Qg22Uh-dXd5N6Wbei4jSLnbMSRjNnMMk4LK_LZsdNaaDDD5qLpUz7YWF84_F-4ZiifrZ6gVV3ycUUeuJfGcu_tTl_wiMTHhsPrGqNbPM6_TQ7wQWdsT5V3oXpf1UnJPM94yeuac80sYMWry_4UReR_qbZ_DMg9WB7HgCqObX38VDpGHk6iIsc207byWA_ktp3c0H6cFe7lWjmc-SXJ3hYZW3HCmt7myu1T8fRcRo5CoCMeWYpApNRQASEYn7jWnpXZpKKOINYWdC9g6HzKcnhRNNELc6nN1w6ow-5yHMuJj7eaIalhsN3A3v7fXGEGohJk0vlLJnhItw1ZY8JmZDt__xdmmN_NfFeU2xRhuEdQ4FAYpQZyNcjaU1MtqBw_GN7oHdM7YrhufFn-8kBN5_qnZIhPEfhm1CoOq64gcHneKOxKIX2uO0xlaw5m7v6TSc-PtsNZyf95E" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=ErCwAzRbcRLW5AYEKtPms0jHAw9f1Fam55I_tdJGL6DMEzhdgVjqSr4l6ZGPe-86hPy_rD8_u53LEnwfauqj3Pyx6Le1iNi6NXMyLzd7tlpy94e_1-JxDna9agPbPP-nDMSgynPolftBLHBFJdtiWkQNDyuGPYVFx9qLgh1Fju0tdr59O_aRUzjhKTuSJwGgTt__38ca5xaLc8n8SrST-oGfep-62nf0Qg22Uh-dXd5N6Wbei4jSLnbMSRjNnMMk4LK_LZsdNaaDDD5qLpUz7YWF84_F-4ZiifrZ6gVV3ycUUeuJfGcu_tTl_wiMTHhsPrGqNbPM6_TQ7wQWdsT5V3oXpf1UnJPM94yeuac80sYMWry_4UReR_qbZ_DMg9WB7HgCqObX38VDpGHk6iIsc207byWA_ktp3c0H6cFe7lWjmc-SXJ3hYZW3HCmt7myu1T8fRcRo5CoCMeWYpApNRQASEYn7jWnpXZpKKOINYWdC9g6HzKcnhRNNELc6nN1w6ow-5yHMuJj7eaIalhsN3A3v7fXGEGohJk0vlLJnhItw1ZY8JmZDt__xdmmN_NfFeU2xRhuEdQ4FAYpQZyNcjaU1MtqBw_GN7oHdM7YrhufFn-8kBN5_qnZIhPEfhm1CoOq64gcHneKOxKIX2uO0xlaw5m7v6TSc-PtsNZyf95E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فراخوان ائتلاف نیروهای سیاسی کردستان ایران، همزمان با چهارمین سالگرد قتل حکومتی مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی»، کسبه و بازاریان شماری از شهرهای کردنشین اعتصاب کردند و مغازه‌های خود را بسته نگه داشتند.
از صبح تا ظهر چهارشنبه ۲۵ شهریور، اعتصاب و بسته بودن مغازه‌ها و بازار در دست‌کم ۲۰ شهر، از جمله ارومیه، اشنویه، بانه، بوکان، بیجار، پاوه، پیرانشهر، ثلاث باباجانی، جوانرود، دیواندره، روانسر، سقز، سنندج، قروه، کامیاران، کرمانشاه، کرند، مریوان، مهاباد و میاندوآب گزارش شده است.
@
VahidOOnLine
وب‌سایت‌ها و منابع خبری مختلف که اخبار کردستان را منتشر می‌کنند، از جمله هانا، کردپا، کولبرنیوز، زاگرس ۲۴ و شبکه حقوق بشر کردستان نیز گزارش‌ها و تصاویری از تعطیلی مغازه‌ها در شهرهای مختلف کردنشین منتشر کردند.
در همین حال تصاویر و گزارش‌های مختلفی از برقراری فضای امنیتی شدید و استقرار نیروهای نظامی و انتظامی با سلاح‌های سنگین در شهرهای مختلف کردنشین منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78405" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PToTwirw_UHyWRkjvAIS-YIZzOqPHo0yRKlIJUIERfB6RnrtdXOVm1h_MfLRm5t2gyoJ3pfecE6jxK2WAMfgAMmgkEfwzMXfvkhOsGI3DJtYPcjo6m7tcIJxXT6ARUoWpaKa8y-hc_07-wrzjZK39mR7Swd5SOzAa1NgN41HEfSn6rkBnNMVouNuLKgPrLkCWRtPGQ6-2u7DxBYo9t6EOYfCQUapGmOamMicIb-WcS72yRuqY_zA9G0Cs3fF0w6C9AwdRKnfbaj_zjs52U0R3L7WNIqIzPo5G8dpUqjCrrelOShni2svUMAse4qfX5tXn0WdsUJsYqYbonzX7WNLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HDg4xmHFlyvFcgIsvg6C4KKeVvojFE71HzJPfv6VFbdzYxwn8By7aU3oMoa-29pMVWy9DMM6V81qx8aIND2ZZVUGutRVuO8Rvc7SYrigxFb0AyYcMh72kzWSI6Ldg-4-9ktwrTVWe7-PM8vLFHIyaCVnnInrorT6YqzvOErvasFgX5WF1g35hDXP3dQiNLVcYuZgmrDuahUSy9n3dPspVCYdbrn2EXjXE_l2GbWpCPTEwgefR-4YQy0g8XR6SORUml89rK_i9F8JrRJaX5U2jrVNsEjC3NVRooOqwKBPgRxtT40kv3uYEvnh7zUEbSnyMP1j_SWeEQJ9yAis1_xY1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ljModTa_YsNxlbu3fLX5j8NHNoNQYPti7Js2nS_AdIOy5Ld-drm8sZGbBU2AZrLhxMEVfsSVX5xNP6c9TIkKYKD0p0EmIBXuTWWiHQTadEXPiQguFl6bndloXV4ymUZsAa8Re3UrNt8ZiQLXlk9yGXQvYIkctjuqvE0mSNAL5bqfzoVjwkj6Sg-lgsg8EzRgbmVqvqA9gvoOW9c13ysmdPkEy8tt6pUIOonKja_-K3OJckEpRu3VpaDDkE-bv5E9GBVIVmVzrqXAEeSkvcI__Sj9VauKZI413cyhDG2ZwI8TTCUlXG41-3x9hvg0AUjicnIUNHwvYJdoUNYmTK0SWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rksMXf7lpfC326rqyhU__UjrE6q64XTFPA6P7tuB1w2S-D1KwloaVkoW36fGIsVLS1sorcWNxh9D4H7Dn-LL-68dXnm8_5hH04uy1WkNnRC-55rE9oeXKLcdBjl8kAWnSvPBTuOGKHlw6_IQe2WEzlcfInYm61ySkgbhqRNCz7WB_HK-8275vZrLPVI3F-lIFcoBCJKsIXROruL1FS2BhGhZG68lqKNQJGEumXdpbskLvL6TEthHx16beRbIpr87J4hrkgk3byN0nvCWaKvkbA-3BaxiqiVefJDh_shTuuGV7FJWkrJGCyLLG0TAfwooML24flkzRoCsGpytJQfDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kW3SebBFc5cxAkI2kAgxRDbd_4tA44yKsnvoqNWO2uPBoXFqAfkHj3G6t-cxrhYbipQ_CzgjthaT2optIZANTWcB8E37nob4UgA-Z_NYAB3BldBHRgXU_gZyohHi6MtUxtQekDKp7HFDfk4y1pdBOQUes7J8vzS4zemCNLiOpK58Dv-wG0OYzlxmQO45TzN5fYOtDOquuUy4SYUQSawyMWAyL089zJBUyqnc08gnr3rL5s_Aw0RFjOGrtYDDF3pob1UFmm-rL8NQ0WTtMYpBoT2srDtYK2lxTwwS1rfGR__a9Fbz_CSfRp4jJIr-XfUO93iJWa4rr33npgtAde1IyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jx3G-LfQynBvwKFA7Bjz4QqRcgjtiDL6OiMxbeKwQsGDJlxC2yGJY952CTwbLdfWz1OUCQHEF3bxgAgFwedpUq0Uap5kgBPg4HOhEIJki0Yoz-TtwsJ-oKbvVwJ2Lv9IB06YjaHP9tv0K1sm8qdOLeHuWIXdMwI9q523S70h55WPjArcfA5DR1attwOnhUIpk_pxGZQo0uFzvPLeSczu8zcXADGi7UM_D8m-SKXw11UXkXMl9tnr3Ysmyot9x8PlBTprz0CluzoMQqTyv6Xq1WM1Y21n37-Pq5tE8ejV-NI6fvBjfeXOQsvSur_4seFC0xATqPfq13-AKDNxX03gZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌بی‌اس‌نیوز گزارش داد تصاویر جدیدی که به‌طور اختصاصی به دست آورده، برای نخستین بار گستردگی خسارت حملات موشکی و پهپادی جمهوری اسلامی به چند موضع نظامی آمریکا در خاورمیانه را نشان می‌دهد.
این تصاویر را نظامیان آمریکایی در اختیار سی‌بی‌اس‌نیوز قرار داده‌اند. یکی از آنها گفت خسارت گسترده به پایگاه‌های آمریکا به اطلاع مردم این کشور نرسیده است.
در تصویری از پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای چهارموتوره بویینگ ای-۳ سنتری دیده می‌شود که موشک به بخش عقبی آن اصابت کرده و دم هواپیما از بدنه سوخته جدا شده است.
تصاویر دیگری از این پایگاه، ساختمان‌ها و آسایشگاه‌هایی را نشان می‌دهند که بخش‌های داخلی آنها تخریب شده است.
سی‌بی‌اس‌نیوز همچنین از ثبت خسارت‌های مشابه در کمپ بوهرینگ در کویت خبر داد؛ پایگاهی که محل استقرار و آماده‌سازی نیروهای زمینی، خودروهای زرهی و شماری از هواپیماهای ارتش آمریکاست.
پنتاگون به درخواست سی‌بی‌اس‌نیوز برای اظهارنظر درباره این گزارش پاسخ نداد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78399" target="_blank">📅 04:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78398">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4v0lDqPX_k1ILJyCg9f88df0nwiJDh2_JcZ1w1nRRiVHVRfrUHbSIw4CwhtjfylEhiszQUWDSejVdrriPgMfJ--MY5opsPdWJiIuxuU2uZzTh_L8lnq6GLqV0KU6Nqun_WsR24TiPZvNi6DsjI-xmwegj9SplokZJe9a8ldket4TF75qVt06nmI0KcnKK_nV0cjYHsWKhWPewynCZQhDZ1as1rFKcucjyoKqW-UPri-X2I9hyGQ0flgpZKgsoh4w1DLIHe-LAvpi5aQ7EkbK4NQrhj9uKX8yfN6CZ8VZ3jZFpDeMtOQcYhZvQNBjVj5DECVCtuqfeTmqrsN03_wjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد پدافند هوایی این ائتلاف یک فروند پهپاد پرتاب‌شده از سوی حوثی‌ها را که قصد ورود به حریم هوایی مکه را داشت، رهگیری و منهدم کرده است.
به گزارش خبرگزاری رویترز، ترکی المالکی، سخنگوی ائتلاف، در بیانیه‌ای گفت این دومین تلاش حوثی‌ها برای هدف قرار دادن مکه بوده است.
به گفته ائتلاف، پیش از این نیز حدود ۹ سال قبل یک فروند موشک بالستیک به سوی مکه شلیک شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78398" target="_blank">📅 03:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YAiXfp6KcESiEfWqDnP3SZUDsoOhA7QG8-_-KVGyOhD99hu2tOrtYHri6fQbenlH8C1GfsEBN4dral6XGhxZn-11kqHBF6ovTrbbbR4YcD4tOrAMHVYutAvDz_9b4ykXmeB4LGRpOlzOc4RuoWkXx_g4WUsb5glOF8xj7dGwqeC12-vvcVGxD8Lvlh-pfTOsVxD2ZeM3Nl7ZzK5940It0Ix7OW6sf0aUTUqQJa8sUBwt2kA_IWOkJotAWQrOL05VgEFbuPniXztDwhxtvevw0IP6nASKK_ChOmDSZQK6b7AklLRcRn9WUrSceOe5T8SifFUo-ZKWyBf4eZDSJPaCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو مقام اسرائیلی گزارش داد فرماندهان ارشد نظامی آمریکا، اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر هفته گذشته در نشستی محرمانه در آلمان درباره جنگ با جمهوری اسلامی و تنش‌های منطقه گفت‌وگو کردند.
اکسیوس گزارش داد نشست محرمانه فرماندهان نظامی در آلمان به ابتکار برد کوپر، فرمانده سنتکام، برگزار شد.
به گزارش اکسیوس، برد کوپر در نشست محرمانه آلمان، فرماندهان نظامی اسرائیل و کشورهای عربی را در جریان برنامه آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78397" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78396">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=N4ddia7Dj3q1rTWzLPXut4B8a6T-FakL65zFym0kugJJCC9RlTIgDylByCRlWyzkpDq5MCkvZXAtSQdH_RrCpQJGIQ5JutwCiaILyFh1N0mOkruW4SJfBdYbTU8DD87HTPPU7uJ3hlS6YsFhCFecMCStzqLKjdseEFTCvECW3osJSHAIcu2cCv34g7bY9Ae5O2AxZTT3iT46Pez5dzgrI5vrrsgOfk2L63lDOy0UF64EsGGgDjTbOU3r9w_h0x87MjB2gZZvSB-Lmx0n91FdGqETq66vW-aN41yLVwvbP09WWlZ_hWNUcVNlZbHb0fdg6qm6HcjuPv0q9XTD_s16Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=N4ddia7Dj3q1rTWzLPXut4B8a6T-FakL65zFym0kugJJCC9RlTIgDylByCRlWyzkpDq5MCkvZXAtSQdH_RrCpQJGIQ5JutwCiaILyFh1N0mOkruW4SJfBdYbTU8DD87HTPPU7uJ3hlS6YsFhCFecMCStzqLKjdseEFTCvECW3osJSHAIcu2cCv34g7bY9Ae5O2AxZTT3iT46Pez5dzgrI5vrrsgOfk2L63lDOy0UF64EsGGgDjTbOU3r9w_h0x87MjB2gZZvSB-Lmx0n91FdGqETq66vW-aN41yLVwvbP09WWlZ_hWNUcVNlZbHb0fdg6qm6HcjuPv0q9XTD_s16Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده در جلسه سالانه درباره وضعیت اقتصادی آمریکا و سیستم مالی بین‌المللی با دفاع از سیاست‌های دولت دونالد ترامپ در قبال ایران، گفت رئیس‌جمهوری آمریکا اقدامی را انجام داده که به گفته او، رؤسای‌جمهور پیشین آمریکا سال‌ها از انجام آن خودداری کرده بودند.
اسکات بسنت با اشاره به جمهوری اسلامی گفت: رژیمی که خود را وقف شعار "مرگ بر آمریکا" کرده و به‌دنبال دستیابی به سلاح هسته‌ای برای تحقق همین هدف است، اکنون با سیاستی متفاوت از سوی آمریکا روبه‌رو شده است.
او افزود: تحت رهبری رئیس‌جمهور ترامپ، آمریکا دیگر صرفا در حال مدیریت تهدید ایران نیست؛ ما در حال پایان دادن به آن هستیم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78396" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78395">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JsY3y8YffT8sXvb-8W0V3kzeIOHXLWEU-Uoaqa0rNEn0xgjrvxmZifG2GFIX4Q_4a1ZhlJYBWRpgpeL4KKAWT67olDGncFXwR-8XTqLxG7K1e_zgf44gXnf0-hm33iMQR8FNclts8izccv3jBXFVF-c90ydJZNRzvFcfJKuuRQU0mAZdpfZx_AMuZafPnfjVGqn783qSYR7qIaJhRPTe0tmfrpUM7ZYTwQg5uOCHEGZpmNvHTC08-KILRQ-9NZAghh2yKjLSDkILdUR6VjFKXZLPCtQOOqUILPoJ1ySjHMQ7X6wSobMpH0mKumlNEMJYfn5rj2aW7Pax7sXERTbbQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره خبری که تسنیم با شرح
حمله به قایق‌های صیادی
منتشر کرده بود:
وبسایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده روز دوشنبه ۲۳ شهریور ۱۴۰۵، دو قایق کوچک ایرانی را پس از تلاش نیروهای سپاه پاسداران برای تصرف یک پهپاد نیروی دریایی آمریکا در تنگه هرمز منهدم کرده است.
به گزارش اکسیوس، نیروهای سپاه با استفاده از این قایق‌ها تلاش کردند یک شناور بدون‌سرنشین آمریکایی را که برای گشت‌زنی در تنگه هرمز مورد استفاده قرار می‌گیرد، تصرف کنند.
پس از شناسایی این تلاش، یک پهپاد آمریکایی دو موشک به سمت قایق‌ها شلیک کرد که به انهدام آنها و کشته‌شدن بیشتر سرنشینان منجر شد.
تیم هاوکینز، سخنگوی سنتکام، تلاش نیروهای ایرانی برای تصرف شناور آمریکایی را تایید کرد و گفت این قایق‌ها «تلاش کردند یک شناور سطحی بدون‌سرنشین آمریکا را تصرف کنند، اما پس از واکنش قاطع نیروهای سنتکام موفق نشدند». او تأکید کرد این شناور همچنان تحت کنترل عملیاتی ارتش آمریکا قرار دارد.
این در حالی است که رسانه‌های ایران حمله به دو قایق را به شکل حمله پهپادی به «قایق‌های صیادی» گزارش کرده‌اند.
به نوشته اکسیوس، این دو قایق در نزدیکی بندر کرگان و جزیره لارک در استان هرمزگان هدف قرار گرفتند و احمد نفیسی، معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، حمله را به ارتش آمریکا نسبت داده و از مفقود شدن شماری از صیادان و آغاز عملیات جست‌وجو و نجات خبر داده است.
این حادثه در شرایطی رخ داده که ارتش آمریکا تلاش می‌کند با افزایش تردد کشتی‌های تجاری در تنگه هرمز، عبور و مرور دریایی در این مسیر را به وضعیت عادی نزدیک کند.
یک مقام آمریکایی به اکسیوس گفت ارتش آمریکا و کشورهای عربی خلیج فارس در ماه‌های اخیر تردد نفتکش‌ها از تنگه را در طول روز نیز آغاز کرده‌اند، در حالی که پیش‌تر این عبورها عمدتا شبانه انجام می‌شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78395" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78394">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=uBlJiWRKGlMaui2FbKNt9RyyXBuibVFf8EasV4sFOfelW2Uvx10kD2D432JtgAnEMv1CRbLJBKtHxMNUYGFeNojBO5J490IqWlLWFqswnOdnSQY9MddKbAkebRER4RUlVH9joOX0gatRJuwoJTxbpSvgSDBza9_U7H3eRXra3TjOnBL5auv1h2C8LWIvThCWFTRWJKmK_J_o_GVnSVrQLngTll1LkW8zWRVxJ1Vsf-FP3q5lyu_9zav958TV1LRn-6g44o-WZ2WnHl6JTEN99nma8bEfRou8IdREVbH5WHycLRKOhJpTknDXN7yAZ9gqPoXgXClAlsp5ZwvOgS7rbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=uBlJiWRKGlMaui2FbKNt9RyyXBuibVFf8EasV4sFOfelW2Uvx10kD2D432JtgAnEMv1CRbLJBKtHxMNUYGFeNojBO5J490IqWlLWFqswnOdnSQY9MddKbAkebRER4RUlVH9joOX0gatRJuwoJTxbpSvgSDBza9_U7H3eRXra3TjOnBL5auv1h2C8LWIvThCWFTRWJKmK_J_o_GVnSVrQLngTll1LkW8zWRVxJ1Vsf-FP3q5lyu_9zav958TV1LRn-6g44o-WZ2WnHl6JTEN99nma8bEfRou8IdREVbH5WHycLRKOhJpTknDXN7yAZ9gqPoXgXClAlsp5ZwvOgS7rbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیوی منتشرشده در خبرگزاری رکنا، لحظات پراضطراب داخل هواپیمای بوئینگ ۷۳۷ شرکت سپهران را نشان می‌دهد که دوشنبه ۲۳ شهریور پس از برخاستن از فرودگاه مشهد به مقصد کرمانشاه، با ترکیدگی لاستیک مواجه شد و با گزارش آسیب به موتور، مجبور شد به فرودگاه مشهد بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78394" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78393">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ypfr_1VQ32zb0h0AHfih16ZDrs6_BKaZPOqFBlRmPE7wTuaLv89C4_-ikyzJT3ehxCSLkPhBFoWmU2-jcmrqlvB6yS81Q4wk-piPEqGG2uDhESklUqlC96yOwCJB0eHmrM189RIcyitmUZ8q6pjHzwibhePx_6-hYynBpRbeuMKVXKOIq_7NXQzf8YZkYCoApAPQ0dAddnyHmZrFQdcIK2RbGSwricfdZNoJP2sWY-BLvoE87YAbMaJm37S-NQ7IW1Xx4z561MsimD4gHn0cZea1Mok6Hhq5F4BMFTGwSKzreMrsWFsF8LXKdqSHl7vUS3nuiuYFHs0APPpjSljSDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل دادگستری روز سه‌شنبه ۲۴ شهریورماه با انتشار پیامی در اکس، از تشکیل پرونده کیفری برای رضا درمیشیان، کارگردان سینما و تئاتر ایران خبر داد.
به گفته رئیسیان، سپاه با شکایت از رضا درمیشیان  به اتهام تبلیغ علیه نظام پرونده قضایی تشکیل داده رسیدگی به شکایت از او در شعبه هفتم دادگاه انقلاب تهران در جریان  است.»
رئیسیان با اعلام این خبر گفت در دادسرا برای رضا درمیشیان قرار جلب صادر شده و سپاه پاسداران به عنوان شاکی، تقاضای توقیف اموال او را کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78393" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAwUiorDYN-FzLasRbXyNvvJ_efxZeX-uqlegeonc8AX4fm8Cgh8vAKyxSrLZEIgVRbg_PHSatPTx3YFrfhWFWF_Y_dZpBElNlsEx9vAkNb2N2UhCXiOo5eDdlQIx9SppjRylPM5Fuk_CG_NldC24xl4jsd1e-QDUMZVyOej8Wyk6UZhSyB6MlaEIt5sf_FfRPDFwv7Xm3kQ-0uHaJIQOvzcQXkYDuhpZXt48T3cySvPnPXHVzVOjOMOZ_QXwh3-C_83vFBlqoZa_Exc_4IPgsQ8R8NG91vPw1oM-QHgULnHhjlpVAtyZDlpDvnkcGraLmx6Cb98Pjpwh9hjNM0nkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استودیوی «کارگاه» با انتشار عکسی از آزادی «آریا کسایی»، طراح گرافیک و یکی از بنیان‌گذاران این استودیو، پس از نزدیک به دوماه بازداشت خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78392" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78391">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oU_P1wnc8UkCga6TqwfZndBL8nPYrewx7U617O4Nxgazc6ZzeXZvek8Uq77WpscHP1WNry4f1AsK0YtbosfV4vlYYRuZqVypGb7SZho33xynt6TgCNPI-aS3VrBsgTKLT3tcQBY2FSh4_m-82c4Cy3Rk14O8mv7yjuxG1zfOu8OrkT8pP8Txs20xzTMFDXxJcgIEqkBSMd0GuHISSI6X17QQadswW9DVrau7NWXwCApdAnAogWLTfe9N1nD64KKzej-vnOXPueYkoRfFoOCSdS0Vg9SrS4hQV4jCCU2V839R2i_UssOcDVENwsh19kR-aW7dtMpzjLwCqmHsyLVngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس تهران می‌گوید فردی را بازداشت کرده است که شامگاه دوشنبه ۲۳ شهریور به سمت «جمعیت حاضر» در میدان پونک تهران سه کوکتل مولوتوف پرتاب کرده بود.
میدان پونک از جمله میدان‌های تهران است که از زمان آغاز جنگ ۴۰ روزه تجمعات شبانهٔ حکومتی در آن برگزار می‌شود.
بر اساس بیانیه‌ای که فرماندهی نیروی انتظامی تهران منتشر کرده، «این فرد حوالی ساعت ۲۱:۳۰ از بالای ساختمانی به سمت جمعیت سه کوکتل مولوتوف پرتاب کرده و پس از آن گریخته است».
در این بیانیه ادعا شده که این فرد «قصد خروج غیرقانونی از مرزهای غربی کشور داشته اما ماموران با شلیک گلوله از ناحیه پای راست او را دستگیر و به بیمارستان منتقل کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78391" target="_blank">📅 15:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bnTNAexot87nwq7y1naeYmKphM4UjVxZhlQIE1TakgFxGdXYSDBbszvDtmSvtgge5CT6xrmijx45_UZ9HvWr_w8g8KxZy9HBMSR13i3LFhiBWW6vLL9CzWL48zlrAiUyG7gopb_lVcwjEg6G9flDluoU3DuTLweyaCTwXpTBa5Z9YPucDg4TRpdAgXqrucX-inNuVkpqZ01_GWwxSVmGRT6Yrxv9i1oQ5X0AXTrCM2-zZiOzjQ6MTKo9Jc0z7xkeRiJy3Qn_CBbQ9TOWTFZfbEij32PRQuWeaX7x8-Y-2RVdk1eG-RPlod9tvRK3tDy3fzWklB50bY-Ihm_UXVLVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش رسمی آمریکا از هزینه‌ها و خسارت‌های جنگ با ایران منتشر شد
یک گزارش رسمی نهادهای نظارتی دولت آمریکا می‌گوید جنگ با ایران به «کمبودهای راهبردی» در ذخایر برخی تسلیحات پیشرفتهٔ ایالات متحده منجر شده است.
نخستین گزارش رسمی نهادهای بازرسی دولت آمریکا دربارهٔ عملیات «خشم حماسی» که روز دوشنبه ۲۳ شهریور به‌طور عمومی منتشر شد، می‌گوید مصرف گستردهٔ تسلیحات در جنگ با ایران «به کمبودهای راهبردی در موجودی‌ها منجر شده و گلوگاه‌های پایهٔ صنعتی برای تأمین مجدد مهمات را آشکار کرده است».
بر اساس این ارزیابی، پنتاگون برای مقابله با این مشکل در تلاش است روند خرید تسلیحات و زمان تولید را کاهش دهد و ذخایر مواد و قطعات حیاتی و برخی مهمات را افزایش دهد تا در شرایط اضطراری امکان افزایش سریع تولید وجود داشته باشد.
این گزارش همچنین نشان می‌دهد آمریکا تا ۲۹ ژوئن (۸ تیر) حدود ۳۳ میلیارد و ۴۰۰ میلیون دلار برای جنگ هزینه کرده است. نزدیک به دو سوم این مبلغ مربوط به مهمات مصرف‌شده بوده و ۳ میلیارد و ۷۰۰ میلیون دلار به تجهیزات از دست‌رفته اختصاص داشته است. بر اساس این گزارش، ۷ میلیارد و ۴۰۰ میلیون دلار دیگر نیز در ردیف سایر هزینه‌ها قرار گرفته است.
پیت هگست، وزیر دفاع آمریکا، اواخر ژوئیه (اوایل مرداد) هزینهٔ جنگ تا آن زمان را ۳۷ میلیارد و ۵۰۰ میلیون دلار اعلام کرده بود. شبکهٔ ان‌بی‌سی نیوز نیز پیشتر به نقل از مقام‌ها و افراد مطلع از برآوردهای داخلی گزارش داده بود که با احتساب هزینه‌های گسترده‌تر، رقم واقعی جنگ می‌تواند به ۸۰ تا ۱۰۰ میلیارد دلار رسیده باشد.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه و همزمان با انتشار گزارش ارزیابی «عملیات خشم حماسی»، در شبکهٔ اجتماعی تروث سوشال نوشت آمریکا اکنون بیش از هر زمان دیگری در تاریخ خود تسلیحات پیشرفته تولید می‌کند و این تجهیزات به‌طور روزانه در اختیار نیروهای آمریکایی در خاورمیانه و دیگر مناطق قرار می‌گیرند
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78390" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78389">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwpNa79mTbDNbG874z_p-pZP8rRt8NF8KGVHQ3tnAkWFLRViR9ZKgNYpI7lKpHUVxrkuNLtPvyQoyeCt050vu3q5e_QFN8lBVumu-vGgVRUi4IZrxaxZ_6T0NV4cRdlhTMwRBifpMKflZYaLcEyr9MjEdQcP_3ITrceAgHYcZlgb7R2fXb6A7MZtH2wQd0WdqtUTb4q3H1nFXZ4ip8BM-i_3vtIxzrBOdzfBHhb-_T6ZYkCNcZTcGawZcmp1YUjFF01VEW6Xq2ltBUjXUlHEK-jjLsPXDuu57OdXeMNf1WeElygCnsQE5QLhnNkar4NXadFGQsFhD3El6ZTkPzC2Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پروژه امنیتی با نام «علاج» با انتشار اطلاعات شخصی شماری از ایرانیان خارج از کشور، از شهروندان خواسته است افراد بیشتری را شناسایی و به این سامانه گزارش کنند. صداوسیمای جمهوری اسلامی نیز به تبلیغ این پروژه پرداخته؛ پروژه‌ای که مشخص نیست چه نهاد امنیتی یا حکومتی آن را اداره می‌کند و اطلاعات هویتی منتشرشده در آن از چه طریقی به دست آمده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78389" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78383">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nkBbWUQTqQ0hpDAqDZj97ie38Xje87YjF0MppNuVxGIlvTsNr2ZAJVHz_kP-vnucQ3ZCqJXfjcWwYFKwfVX6fDeJjIicS4NJp1wAlvoiR53WCuiJqkVoI_FJVQV5HdQf5CGcbRWQMTqjiJB3gq8DHc2arzoaBf54EVjkZ4bdMzvxuyosbAsxsAnJKSRJNEs061u3hQuAMPdhgjSzKj4t3lX7L6lHCK20sH4pFWeJ278GZPdOmBLO2VByXSPz9PE9G1Ms42gBHAHUAKggBgCktzcb895I5vgoogMp8aqGQd-9AR22pG8UgvTsQr3vlYfqI_WnCEKtYP8UMxu_73ejJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HUULUDIF-DfW8aNtEkFU5n_uuJVjCQ8McdPz8x8QxDNV6J-XLP_STfTMpY-K79WGeRCp52TLdn-d9MD2iekpASNCS47mc_tVxcUzdnvOxRHPRqLQU5nmcSW3MNSa0m77CHQxZYFsvwKprRG0rG4VnKIWgziGGsc5K64u6EWsPMFjTYNwalGnRMDP2w0L1GqKVRaWymtZUNI-agCeRc0esp1BGAotFL0PMVstyEI1_je7uphrkkEHQR2QrLV2mguj6Gy7orfGb2y_x0hAKZRjNfINPazI-aYJ27RBFcBBJTeyIOsiXuW36vagkm7uvVaJsLerOlOzlQGLwN041GeyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/olWE7E7QVZCcm_YEnRNr6QhcKV3xWstRDLhBdOeH3-zX3zJdJjcMYX1OumN3yFjH-EHI7wToUpqRxqOh3IgQrZeimYg1v1pYiZQM8gc0_-DlRhzGNFes-AQeDbK5sWOIvg549VconzgpFxsMwakxzq2xwFAgbCfRwlX_0cfm7GGyv09TPwq29FQObus3c0m_C4Rng5_zDWKnBWgMn3y9_VqHqwFcroLSHwGwkywE-V9dtifPlcxqDeJbYK-MU24NxiKY-aaOdWFP7njIr7Dtt6xFHJsNHlRdWqUptFTT2Vov3UH8Kyo4NddUz4ZJ_AyH3ydSfrevTmPwxpeKUIFakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qCS6gO7qIYUV9StEFl_uY1Wuytq5BUf6maDC_AwtB4HxZmbFaXyilzybV6ndboPX1WNoZol6LXpcWn_BcmtLEYdFRvb261A9o7i39vunKiIvwkAqvF0nk9l-sAGJ47md8GHb6Y93M8SmbvcRdz_SfPKksQulC82o8afyKCBnB1_RR6MRZSR9rFbm7gQ203g8SFA2L1Bn36h32qOFhqxOe0GMgZ3mTPSw7Fgx2vbM7R7ZUcvmBgT-pf3tRHjJRc8tdS38hfmRaVAQ6-Bl-SBpHXpNoodSXOYvfsSgOOa1qPe3waGSZWJ420FNMnnbDsdJi_Gi6cxk-hhVaJYYF-X_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bvChiK8xpHsaovg43ENiTqjHVSLgT7tValDn1ArmLkrw6KjSTxoG-1Id8Zq0UpsfvtZbylguVfrTSYb7hBD-84n0CWs0_ZtC44RtOSZArnuIV1KZ64C5gvyjJQi9EqEplE_KL_f-ApzC06LNK_BU6Ffa8RxDctOn2bvJAa5k2jhF5NUlllonUrEP6C6js5gLK99BUgpuQz9CXV8teura6TrEOD868dKk8CZtwmkmZIP6wsQ8p5947iXb8BqJ_yOQvs-oivIq4uImfeoQ5PSLzAqsALBHL3_hExsBdToP18qGHUyHCejHXxrajbbh2G8HaoNg-F0ifMxqkDHb6js7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YPLpdlIC2tvQnc1ODkrhCHw3120kCGd9MPMtEecPorrfK5s6VfoZ2HCKJJdtQtL8aiI9zfrRczwxlCSYEks5k_Fn-D8R0ChZf0aOxIF6g7X9qpLhL8JUx_Wmxks2nXxzrwfjpnApnC2MtnkfqVRTnQlVwJCvup91-1XSJgudnVabrxvNOiMzvqvYd1U5iT98zAAn3YOhmCmnhnz6MX6_0eWtiV_NhjZ7D_pS4W738hM2nIznmfS2DhlKcMsuXZ68Bc8Eb5c5pu2hhe2ad5IqYl_hv47b39xExV535KewZh5YCRmyX8MLc1eFUEE--rrwOfrYuoZNAMEIBnupmBQIrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«پویش جان‌فدا»، کارزاری وابسته به نهادهای تبلیغاتی سپاه پاسداران، ارسال پیامک برای ثبت‌نام شهروندان در دوره‌های «آموزش نظامی و امدادی» و سازماندهی آن‌ها در قالب «گردان‌های مردمی» را آغاز کرده است.
در پیامکی که برای شماری از شهروندان ارسال شده از مخاطبان خواسته شده از ساعت ۱۷ سه‌شنبه ۲۴شهریور برای شرکت در «دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جان‌فدا» ثبت‌نام کنند.
پویش «جان‌فدا» از ۸فروردین۱۴۰۵ با محوریت «قرارگاه فرهنگی و اجتماعی قرب بقیه‌الله»، از نهادهای وابسته به سپاه پاسداران، راه‌اندازی شد. سامانه‌های اینترنتی، پیامکی، تلفنی و ثبت‌نام حضوری برای جذب افراد بالای ۱۲ سال در این پویش در نظر گرفته شده بود.
@
VahidHeadline
دیروز کلی پیام دریافت کرده بودم از شهروندانی که می‌گفتند در این پویش ثبت‌نام نکرده‌اند ولی اون پیامک براشون ارسال شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78383" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP110Jo8DVj35q4JvG2zrpEiylnvgZ_FIhzvy2f0UD5YN5FICbE9ZZqih4GRQPif6UtTrgfO7m9pEIb23mcsT_TWfbSryBGZPtgEzrHbZUylpHc050EnCVu9raSg75CtGj9WJzi13CCuH6dZoM9pmBVLIVTs1EkihXhTfJ04skVNYpCxZRneWj-WJ-e7YV18ThgkljsClowglSR_JTgrQOepARIzr6WbuaQHhbagiutyb5fPmEjztYSYjoaqVH79F7Cr6g8awqF8yu7w_OmSr_FZqvMH9T9eaVDH2zx0_LFH1ae47Ezj3BluIX_tH4AjzTHiFbgiaaKj9daJ6TNTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دادگاه فدرال آمریکا روز دوشنبه، ۲۳ شهریورماه، به عدم اجرای دستور دولت دونالد ترامپ برای محدود کردن مدت اقامت دانشجویان و خبرنگاران خارجی در ایالات متحده حکم داد.
‌این دستور که به گفته قاضی دادگاه به دلیل «استدلال‌های بسیار ضعیف» دولت صادر شده، قرار بود روز سه‌شنبه به دست وزارت امنیت داخلی آمریکا اجرا شود.
‌بر اساس قانونی که دولت ترامپ سعی دارد به اجرا بگذارد، روادید دانشجویان خارجی و روادید افرادی که با برنامه‌های فرهنگی در آمریکا اقامت می‌گیرند، به چهار سال محدود می‌شود.
‌این قانون همچنین می‌گوید که روادید خبرنگاران نیز نباید از ۲۴۰ روز فراتر رود.
‌هر سه گروه، بر اساس قانونی که اکنون دادگاه جلو اجرای آن را گرفته، برای اقامت بیشتر باید بار دیگر اقدام کرده و روادید خود را تمدید کنند.
‌به گفته قاضی دادگاه فدرال، اجرای قانون جدید تعداد دانشجویان خارجی و روزنامه‌نگاران و خبرنگاران در ایالات متحده را به شکل قابل توجهی «محدود خواهد کرد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/78382" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtOLWaOgr7fOzL1EVrtFzxJ1hpusUk5mOSmTwDOWI47RjQSJaPDZRP7PdmE2etiep3KyCXoKMshBlZkO4Smxd1KnLP6S-qPXgLkIE_DRs9yZB405lYkV0QRGorBoOEOyCwGCXLeMDRD-_x-1zV-eMeeKZjC5yYd75LjYCc7ADWkZhDLBf9keQ44fHJ1sByM7SDqGc-n8gjU4N6KBJYnlHeUnB1zybwX6mYCzAOwSw77evDzcmQc2w59b9OjRVcEEgs1ehwcliUymBr8OhNT91aZVgsuI3ozKzRyPt1ESXPPgW3DpaHJiG555CfD7h2BAZF2VNwNJhJIv_n4DHvF14w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه اتریش اعلام کرد برای سفر محمد اسلامی، رئیس سازمان انرژی اتمی جمهوری اسلامی، درخواست معافیت از ممنوعیت سفر سازمان ملل داده بود، اما درخواست رد شد.
بنابر اعلام این وزارتخانه، رئیس شورای امنیت سازمان ملل به وین اطلاع داد که درخواست به دلیل نبود اجماع رد شده است.
وزارت امور خارجه اتریش افزود با توجه به تعهدات بین‌المللی این کشور، ورود اسلامی امکان‌پذیر نیست.
اسلامی در راه وین برای شرکت در کنفرانس عمومی سالانه آژانس بین‌المللی انرژی اتمی بود که اجازه حضور پیدا نکرد. او از سال ۲۰۲۱ در همه کنفرانس‌های عمومی آژانس شرکت کرده بود.
ممنوعیت سفر از سازوکار «اسنپ‌بک» ناشی می‌شود که تحریم‌های سازمان ملل علیه جمهوری اسلامی را بازگرداند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/78381" target="_blank">📅 15:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vCo2jlCNxqCZkEjHgZjo8TB2HdKOpdrIp1qG-CTRzP4c3A2Cqm67VQDU_OCZNJYhQH6a8rDv737CWQij-KOEekwJPuzMnhhIJj6EXfZfov-qBOlyGz6f3PJf4Hc2o3DJ8f5x5qev32gBLnA-OYoYU79cSvzQTz_mQet58ahCrz3D0X7eyTGxVp2b72zNJXogDSRVTyyYjVuvPNaQ_6Cr8eCYRu9w6WvN32cNSBw6olDktovgyRFYwtWmqTW1_uzpmuFvezQB3xhxSnYbxDVCCVmpKX5-9TcyH_aUXIo3PH2yBF0icHRdr2FT-6B2ZZbO6nSMYxUGSlr5ciKMH6WIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش الغایا پس از حمله در سواحل عمان و آتش‌سوزی در موتورخانه، به یکی از بنادر این کشور یدک‌کشی می‌شود.
بر پایه گزارش رویترز به نقل از مقام‌های عمانی، ۲۳ خدمه از شناور تخلیه شده‌اند و دو نفر همچنان مفقودند.
روایت‌ها درباره علت حادثه متناقض است.
سپاه پاسداران اعلام کرد الغایا با پرچم پاناما هنگام عبور از «منطقه ممنوعه» جنوب تنگه هرمز با مین دریایی برخورد کرده است.
فرماندهی مرکزی آمریکا ادعا را نادرست خواند و گفت شناور «ماه گذشته با موشک ایرانی زده شد و از کار افتاد».
سازمان بین‌المللی دریانوردی گزارش داده بود الغایا روز شنبه آسیب دید، بدون آنکه علت را مشخص کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/78380" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78379">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MxeTJ9IWrZXhVvau_ayZidnK7YJIO7ssbPDh6sJ8W4H7ER3qZu-Awzba7BuVCUGL_fJ0W0u5bMYgxHbSKpN9rWhw3nUq-zKqN_G3XiiUMgIC48R3r4pywJdnh0BQcJF95amXNBPk28prJZADLh0Zlo01Cyiup6FPLTvpkP5g1HHC-AyaVWX1rzZmplASu2ZReQI5PRQilox_5CjQTg-k7ctM4aOhjOjqeImjEGiK8I_zsbz538z-VtH20yrPUSWEsqdtpq3H7krH7Ty8NgW8YBw0GUYHuVHEDpfMvLWOc6LUGgFwwH8SpSUGEgWpOqD4sGJ8OMEXgq4VlT5fo2IoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۱۰۰ معترض در ۱۳ استان ایران در خطر اعدام هستند
سازمان "حقوق بشر ایران" اعلام کرد دست‌کم ۱۰۰ نفر از بازداشت‌شدگان اعتراضات دی‌ماه در ۱۳ استان ایران با حکم اعدام روبه‌رو هستند؛ بیشترین شمار این افراد با ۴۶ نفر مربوط به استان اصفهان است.
بر اساس فهرست منتشرشده، پس از اصفهان، ۲۲ نفر در استان‌های تهران و البرز قرار دارند.
همچنین ۱۰ نفر در فارس، هفت نفر در خراسان رضوی، پنج نفر در مرکزی، سه نفر در یزد و دو نفر در سمنان در این فهرست ثبت شده‌اند. در استان‌های خراسان شمالی، گیلان، اردبیل، ایلام و قزوین نیز هر کدام یک نفر با حکم اعدام روبه‌رو است.
این سازمان می‌گوید فهرست منتشرشده تنها شامل معترضانی است که دست‌کم در مرحله بدوی حکم اعدام دریافت کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78379" target="_blank">📅 15:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BnhnqKqdRuB_dfg0dB15kAKHBLv8sk8JtXc5SbSaAW_hpJjlAAa8kNfHMvXH5QNnmxWoJ8-LFPy6U-XQMPwfh9aC7JaB3UIYVc3rpFcqF7SuYYgFcTOoux5Y0WF2ARDmV5072mp1DlRi203cIgCJ7ZjdrBY1XIpz5ENqGizjUAjgKq5Jl7Ab-EbrfhtF4TFHn_5U2XiZdqIJIiC_WZ1eRicIULMW0CPGX8lo6pgTRU0J6WsYw00VJZ8GNjA5q_c-d_37-fVtt_v0JFP8RUbOuskLX98n8_EfMAood4vOgFsnbEJWdwZox6xj-W5MZBDFYdBFIipuZrARwdBhhmlC9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، شامگاه دوشنبه ۲۳ شهریور ۱۴۰۵، از حمله پهپادی به دو «قایق صیادی» در حوالی بندر کرگان در آب‌های خلیج فارس خبر داد.
بر اساس این گزارش، در پی این حمله که تسنیم آن را به «آمریکا» نسبت داده، تعدادی از صیادان حاضر در این دو قایق مفقود شده‌اند.
عملیات جست‌وجو و امداد رسانی برای یافتن مفقود شدگان آغاز شده و نیروهای امدادی و دستگاه‌های مسوول در محدوده حادثه در حال جست‌وجو و نجات هستند.
تسنیم نوشته است جزییات بیشتر درباره این حادثه و وضعیت صیادان پس از دریافت گزارش‌های رسمی اعلام خواهد شد.
@
VahidHeadline
آپدیت:
اکسیوس: آمریکا دو قایق سپاه پاسداران را منهدم کرد
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78378" target="_blank">📅 03:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FxwL_xBiIXJS9BjhIdXCzUV07UxDxyw349qtowK4IeM-dYDg3GKdeACBWDd-7ELddoc73ypLw2J9VBU0h2V9IUfKDZRhhS7St4JxtaoP_3yyfKNUp44Q9gESxk5OoHsLk-LSpIgVAyDtEOd5SO4RRkWqFOkeeJasBivKEOwMlrvK6U80QDvyadilnUJaCm2Tpi3PnyMYf1q7vE8meecWCwhhoZ5VAutKUfA90K2bJ3hEZixkYlErmpjeaIGfz8cDX_lHy_m-kUFc4Rb_rdajiW_DFJXGd5vXLQnGDs1CEEIxffaEjaIlnZ6u6GOOP6UP-WclA25L3yK3ibcu_7SoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی نیروی دریایی سپاه می‌گوید یک ابرنفتکش که به گفتهٔ آن قصد عبور از «منطقهٔ ممنوعه در جنوب تنگهٔ هرمز» را داشت، «بر اثر برخورد با مین دریایی منفجر شد».
خبرگزاری‌های ایران شامگاه دوشنبه ۲۳ شهریور با انتشار بیانیه سپاه، نام این ابرنفتکش را «اِل گایا» به شماره دریانوردی «۹۳۲۵۳۳۶» اعلام کرده و افزودند که «تلاش برای مهار آتش بی‌نتیجه بوده و کل نفتکش در شعله‌های آتش گرفتار شده است».
فرماندهی مرکزی آمریکا (سنتکام) این ادعا را «نادرست» خوانده و گفته که نفتکش «اِل‌ گایا» که با پرچم پاناما حرکت می‌کرد، ماه گذشته هدف موشک ایران قرار گرفت و از کار افتاد.
@
VahidHeadline
پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است یک نفتکش با پرچم پاناما اخیراً در تنگه هرمز با یک مین دریایی برخورد کرده است. این ادعا کذب است.
✅
واقعیت: نفتکش «El Gaia» با پرچم پاناما ماه گذشته هدف یک موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، ایران بار دیگر این نفتکش را در حالی که در آب‌های ساحلی عمان قرار داشت، با یک پهپاد هدف قرار داد. این نفتکش در حال حاضر توسط یکی از شرکای منطقه‌ای یدک‌کش می‌شود.
ادعای کذب سپاه پاسداران نمونه دیگری از دروغ‌ها و تلاش‌های آن برای ارعاب است؛ آن هم در حالی که می‌کوشد مانع تردد کشتی‌های تجاری در تنگه شود
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78377" target="_blank">📅 23:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G7A0bzbcmShNduKyqTS2asyHF6qGrvbASCnOj8n5VxjXyNgrJRr-aRj4hHX14LWdmJpstdwfNb4161_tu-DiwndN4VvsGn_PZhVhbatNXQJtQP612osb5sTm1AC6Vn8aB-UVvTdU-A_in_YCJEs2bH1KnrA3cJjrRd2cZd2rN4NlPmgC1db10mTyiWilMiffjGzhEvQxRs7Od60t8JyNl9VbI7pjbjTm_BdYPCDSubLw_kx0CuO0OM9Hm7WC7A8V8TxPHKObTqJREXyEg6KwiwnZxkZRubChSt55WIjFNCOVtQgXcW51yWwUNuCuD2qmTvYgdlYIX_q3X9OSpoj99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rGoJ3mN86TuiskLUlZ8JQGDlwwDqnFRiJBcn4Gr74d6SlDxAtLvjXFG-ocaHg0DRFqNO4_dA5EY8Z1L9nMPK5dFOcdrByX5QNJZK3SVO9Mv9dV0Cdu8-x8iZB5Bj7cFT7LiGkEHxwH3ssGxQNg3lWcNyKpoDGW8xfUklXO4Hx5Em1hNarXPWql1VMw5aBk5rKMkWW_uUABoXfhqYEGhs9sJAl_cCkzMb78cS-_JXY8-Ckm16FLP355Sxlzv_3U3TLxZPWyZVZXDoNiM2zCceZ4AXGGB7beZPZCJ8W8hgRni1PoJ7dA78cpH9gzxb8TRTS-oVQETDULfTHc7sXbLC1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پیامی در شبکه اجتماعی تروث سوشال تاکید کرد که افزایش قیمت‌ها در سراسر آمریکا ناشی از سیاست‌های جو بایدن و دولت او بوده است.
او نوشت که حتی بهای نفت نیز در دوران بایدن بالاتر از سطح کنونی بوده و دولت او مانع از دستیابی جمهوری اسلامی ایران به سلاح هسته‌ای نیز شده است.
ترامپ با اشاره به اینکه قیمت سایر کالاها به شدت در حال کاهش است، افزود که بهای نفت نیز به محض پایان یافتن درگیری نظامی با ایران—که به گفته وی زمان زیادی تا آن باقی نمانده است—مانند یک سنگ سقوط خواهد کرد.
در دوران ریاست‌جمهوری بایدن، به‌دنبال وقوع جنگ روسیه و اوکراین و بحران‌های بازار انرژی، قیمت نفت در بهار ۲۰۲۲ به بالاترین سطح خود رسید؛ به طوری که قیمت نفت برنت تا حدود ۱۲۷ دلار برای هر بشکه افزایش یافت.
@
VahidOOnLine
رئیس‌جمهور آمریکا در شبکه اجتماعی تروث سوشال از کشورهای جهان خواست پس از پایان درگیری‌ها، هزینه‌های ایالات متحده را برای حمایت از کشتی‌ها و کمک به عبور محموله‌های نفتی از تنگه هرمز بازگردانند.
ترامپ با اشاره به اینکه نفت در حال عبور از این آبراه است، تاکید کرد کشورهایی که هیچ کمکی به آمریکا نکرده‌اند، باید خسارات و هزینه‌های این اقدامات را جبران کنند؛ زیرا واشنگتن این ماموریت را بیشتر به نفع دیگران انجام می‌دهد تا خودش.
پیش‌تر کریس رایت، وزیر انرژی آمریکا، اعلام کرده بود میانگین تعداد محموله‌های نفتی که با حمایت نیروی دریایی این کشور از تنگه هرمز عبور می‌کنند، رو به افزایش است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78375" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hyGWrAEFFXiBMoz6lo7goczc0ssmepUv_zGxQIoeTZ7njSghRRqt7cnz2ohtoKiTySAYT4-AGEz3Og4n6qpax117bpFUOex_C42iALgwtqU96PPo-Jiz6spXAdfs8DxgaaI8nRY3JrwQ4yxfaAEG-OYrMC_idLNSbAlUEZdScE9AUiajvsECWAITVTyDZW--D-yo1-eVTycuuCkNRmlNRqkn_YWY43NU6ZwOEPnY8NsPNis2Fro0YA3MI7Z58eZHhlWaFlwRjbRPCnVaj7yG36kXdmmpzW7tzVR4c6jqPW2XWQVIcqXu4-JLS2VrbplYigdq1GgK4A8e-gA6i4bqSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایرانِ شکست‌خورده می‌خواهد خیلی سریع و به‌شدت به توافق برسد.
من تصمیم خواهم گرفت که آیا ایالات متحده آمریکا وارد مذاکره بشود یا نه — ایده‌ای که نسبت به آن آمادگی داریم. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
ترامپ نوشت: کشور در حال ورشکسته‌شدن ایران می‌خواهد سریع و به‌شدت به توافق برسد. من تعیین خواهم کرد که آیا ایالات متحده آمریکا وارد این داستان خواهد شد یا نه؛ چیزی که ما نسبت به آن نگاه باز داریم.
پس از انتشار این پست قیمت نفت اندکی کاهش یافت.
اظهارنظر اخیر رئیس‌جمهور ایالات متحده در حالی است که ایران گفته برنامه‌ای برای مذاکره با آمریکا ندارد و شروط متعددی را برای توافق با واشینگتن اعلام کرده است.
در همین حال، اسکات بسنت، وزیر خزانه‌داری آمریکا در راستای برنامه فشار اقتصادی بر ایران موسوم به «عملیات طرد اقتصادی» از همه افشاگران خواست تا چنانچه اطلاعاتی درباره «تسهیل‌گران تروریسم ایران» دارند در اختیار وزارتخانه تحت امرش قرار دهند.
او با انتشار پیامی در شبکهٔ اجتماعی ایکس خطاب به کسانی که در سراسر دنیا اطلاعاتی درباره شریان‌های حیاتی اقتصاد ایران دارند، نوشت: «این شانس شماست. اگر اطلاعات قابل پیگیری برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت جایزه باشید، صرف‌نظر از این‌که کجا زندگی می‌کنید یا چه کسی فیش حقوقی شما را امضا می‌کند. اگر چیزی دیدید، بگویید».
او همچنین بار دیگر تاکید کرد که وزارت خزانه‌داری آمریکا عملیات طرد اقتصادی را «برای قطع تمام شریان‌های مالی رژیم ایران و حامیانش» آغاز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78374" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=VkJkJwOPRzJAmSBQgmCutnaumSjl5ZVAwspoqmI5Mqve52OYTsWmtG7J-b0j_xkn5y6WIoO1VnP9s2tDzbWnzBKXFR-jRFTHLWHZciUVcbawyvM8YNvFgAsEJwHXLPJf1EABJeTnBGp7A4rJ6JbOPDOpJ0aKSoQEwLNjFMIIHzg-ZA5cPE9wmC2cj8783E-ZwWM14Jh_ixPToogo_Kbw0COUekMJzhcO57KpCSN3DexwPg9mhAn8qDFsvMaIjz7JGBRp8bTayOBma-1W37EUH2pGItRDjO6k_EgFPts70cXm3vKMWoYfaCbfPopTLaf_buWDJLeZpbw__Uvwb7Ad6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=VkJkJwOPRzJAmSBQgmCutnaumSjl5ZVAwspoqmI5Mqve52OYTsWmtG7J-b0j_xkn5y6WIoO1VnP9s2tDzbWnzBKXFR-jRFTHLWHZciUVcbawyvM8YNvFgAsEJwHXLPJf1EABJeTnBGp7A4rJ6JbOPDOpJ0aKSoQEwLNjFMIIHzg-ZA5cPE9wmC2cj8783E-ZwWM14Jh_ixPToogo_Kbw0COUekMJzhcO57KpCSN3DexwPg9mhAn8qDFsvMaIjz7JGBRp8bTayOBma-1W37EUH2pGItRDjO6k_EgFPts70cXm3vKMWoYfaCbfPopTLaf_buWDJLeZpbw__Uvwb7Ad6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رشت، حامیان حکومت شبانه به آشکده سحرخیزان حمله کردند.
در ویدیویی که آشکده سحرخیزان منتشر کرده بود، عبارت "آش برای افراد با حجاب رایگان است"، به دیوار نصب شده بود و در چرخش دوربین، چندین مرد محجبه در صف ایستادند.
همین بهانه‌ای شد برای یورش و تخریب مغازه.
این اتفاق یکشنبه، ۲۲ شهریور ۴۰۵ رخ داد.
دادستان بلافاصله علیه آن اعلام جرم کرد و مدیر رستوران بازداشت و خود رستوران پلمب شد. ولی انگار این واکنش از نظر لباس شخصی‌ها کافی نبود و دیشب ریختن رستوران رو تخریب کردند.
via
pkhwshhal
,
yaghma_fashkham
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78372" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشگاه تهران - دانشجو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYTya7AGSmmjLwzExk_6FajAsto58B3o8CA2XM5Qo202z3Nj5SgKNmekgIMhcMMfMjhV4eb1LCOIe325AFbIzL5HpjdU_46H9DdpmUr3H_s9Hvm-S7lNaeLMp1VJe6ZnvAhtyVxVqSovHgXSIzibnUOsEWhCy7Ttc7jf3TlNvtKv_nCVvgxUhA8YNKLEHFgCbPK1QN3jtyi_0hUSox4X8ukrhylAvKnK11ZOY1_tgTKihZL9NGiDja_GGtHzbz3lMSvMrCGCQcpwI8RsJ7rYTF7M8O-X6_RLy_pzz6AvCumZWGFWzBBZrP6YT_tt6RVebFiiSVLnaeiYu3zi_6HD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اتهام «بغی» برای محمدپارسا گلچین، دانشجوی دانشگاه تهران و دارندهٔ مدال طلای المپیاد!
بنابر گزارش‌های رسیده به تهران-دانشجو،
#محمدپارسا_گلچین
، دانشجوی ورودی ۱۴۰۳ کارشناسی ادبیات دانشگاه تهران و دارندهٔ مدال طلای المپیاد ادبی، به «عضویت در گروه
باغی
» متهم شده است.
همچنین، «اجتماع و تبانی علیه امنیت داخلی» و «اقدام تبلیغی بر خلاف امنیت ملی» دیگر اتهاماتی‌ست که به این دانشجوی نخبه وارد گشته است. او در جهت دفاع برابر عناوین مذکور، به شعبهٔ ۲۶۸ بازپرسی دادسرای عمومی و انقلاب مشهد احضار شده است.
محمدپارسا گلچین، شنبه ۲۲ فروردین ۱۴۰۵ به همراه جمعی ۱۸ نفره از دانشجویان در جریان یک بازدید دوستانه، توسط مامورین مسلح و به‌طرز خشونت‌آمیزی بازداشت شده بود
. پرونده سایر بازداشت‌شدگان نیز در جریان است و در انتظار دریافت حکم و احضاریه هستند. درصورت دریافت اطلاعات تکمیلی، گزارش پرونده‌های سایر دانشجویان متعاقبا در تهران-دانشجو منتشر خواهد شد.
#سرکوب
#بازداشت
#دانشجوی_زندانی
دانشگاه تهران-دانشجو
اینستاگرام
🆔
@Daneshjo_UT</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78371" target="_blank">📅 17:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=ODQVjhJn8uoIKw_wxG40qO6MBlwPkz3VCJ3sCd7aOZwtizpU7WrgSw0EeS6NWTUAshzB4PY9EQpY7qPIByD_-dGdAVgSWj5anyDK-yoJCgmrkDmYcXY0PMbP6-D2BIKtHfWaSe12V8MY5JFJLR5td2Da9ClCMMqzeGVMM5DPrhgmPMC_cmbpmUri1037LopMB9r7Ch3kolAA9-9z2as1mHv0YCD78GhRM5jkFuhBTxq_DdmhnnzPvUp7YQszT8IGF9Rk8eNuXzjUwpwHkkStBRi7JPRPof31QYRPzX717kCeiRKoLDKJ-yx8Ckssb_tHjWGqGmZtbx1wF1PcUyXilw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=ODQVjhJn8uoIKw_wxG40qO6MBlwPkz3VCJ3sCd7aOZwtizpU7WrgSw0EeS6NWTUAshzB4PY9EQpY7qPIByD_-dGdAVgSWj5anyDK-yoJCgmrkDmYcXY0PMbP6-D2BIKtHfWaSe12V8MY5JFJLR5td2Da9ClCMMqzeGVMM5DPrhgmPMC_cmbpmUri1037LopMB9r7Ch3kolAA9-9z2as1mHv0YCD78GhRM5jkFuhBTxq_DdmhnnzPvUp7YQszT8IGF9Rk8eNuXzjUwpwHkkStBRi7JPRPof31QYRPzX717kCeiRKoLDKJ-yx8Ckssb_tHjWGqGmZtbx1wF1PcUyXilw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
پیش‌تر نیز در سال ۱۴۰۱ نواب ابراهیمی، آشپز، در پی انتشار دستور پخت کتلت در اینستاگرام خود همزمان با سالگرد کشته شدن قاسم سلیمانی، بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78370" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ahHJKdYBgqnM8sZhL1SdiBkA9pL4WheKjAHvfJ1ggNnDjbgCWO5D-lwzOmqI1XkXsKzatwO4EtXFHRExt-3mDFryPVBM1TfbPjRb-ZsktA3BL9SxCjxRRSnmjIutbVPsP6mmvnMrZFctKpgDfwd-9P36IUJfN3Viqm9XWFF8YSVwcoz7f3KbZnOi9c4vewCuGRdUTMXFFjcuJXgUYBdmvOKKtqHkTwjf4gxueD4fx3_JEIsD7TMIROgK8KukRNsXRX8_nI2BMPBhWUcQRZKI7QXWJjF7o2I8dmwmyrFcSlLKQs7FlcuSWZBHJjb4NqUmOwOhbpOP3Bnxd4iF3rC3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lNW_974j5FheN4STMlK2d5Aqr8wNKF4o7yD6vGoTvs4HX_IYlyiTH4ly-53qcRkSiMzIZIIPcZ3JrGacGLQJ5MdKKsFLpMSPMcpjBKV9MuWr4WOmnPzO_UzZvjEs7FOw6oTzz2fZzyCh3uJ4RqxbFPCoatk1AXUsz4465LWWIruLz3CK_QJzuN8-v5qOPY4yaFA3NjWUr7MNH0NbdKD8RFTxV-x9zD64SxnO8FtwKLdB89B1ZDdtIu-IC5fHteJ3viry0JcHwFxv9KeO_cyBNWEMt-owZylphre6uhtrfyUpY8w70j7ZrbM0pfOSzZK2TKcJdsLh374IAcnsmQ5nTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«یحیی سریع»، سخنگوی نظامی حوثی‌های مورد حمایت جمهوری اسلامی، از انجام عملیاتی گسترده با ده‌ها پهپاد و موشک بالستیک علیه اهداف نظامی در منطقه خمیس مشیط عربستان سعودی خبر داد.
سریع گفت پایگاه هوایی «ملک خالد» در این منطقه هدف حمله قرار گرفته و آشیانه‌های جنگنده‌ها، رادارها، باندهای پرواز و انبارهای مهمات از جمله اهداف حوثی‌ها بوده‌اند.
سخنگوی نظامی حوثی‌ها این عملیات را پاسخی به حملات هوایی عربستان سعودی به یمن دانست.
@
VahidHeadline
«محمد بن سلمان»، ولیعهد عربستان سعودی، امروز دوشنبه ۲۳شهریور۱۴۰۵ در جده با دریاسالار «برد کوپر»، فرمانده فرماندهی مرکزی آمریکا، سنتکام، دیدار و درباره تحولات اخیر منطقه گفت‌وگو کرد.
خبرگزاری «رویترز» به نقل از رسانه‌های دولتی عربستان سعودی گزارش داد این دیدار در شرایطی انجام شده که درگیری میان عربستان و حوثی‌های مورد حمایت جمهوری اسلامی در یمن شدت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78368" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4QZ41Tqqfl4glzfektxm62dHkmIIqxmUvkGd-i1OSy_Hj7u7z4JaIy7ZP5gc4wLrBmoVsotI6Jvn1ucVytvwlXXPYYAabwho_ThOtuGiHA-G3rz3ffUyZKCSu7ihtWbArMlK9BogSTHybAjJCEv5n61IZX18UkhO8TqEIbvC9p0wQDd9i-q_ydRjtX0e4C0jdi22Idlp1Wt7belLUj_jsBwzLa4aXzHj4h-uFCQxNDOVI1gRSz9ajBByYLz_NMZVJEKwCVB_uPA5UZxK75cWKHqgr5GhD-i25L1VUHKX7LYFyim-Kvjpde8JhAA24TYPAljuH5dUJnM2gdokbhR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین امروز دوشنبه ۲۳شهریور۱۴۰۵ گزارش‌ها درباره کمک نهادهای چینی به جمهوری اسلامی برای هدف قرار دادن یک پایگاه نظامی آمریکا در اردن را تکذیب کرد.
خبرگزاری رویترز به نقل از وزارت امور خارجه چین گزارش داد پکن «قاطعانه با این اتهامات بی‌اساس مخالف است».
این واکنش پس از آن مطرح شد که روزنامه «وال‌استریت جورنال» به نقل از مقام‌های آمریکایی که نام‌شان فاش نشده است، گزارش داد جمهوری اسلامی پیش از حمله موشکی ۱۷شهریور به پایگاه «موفق‌السلطی» در اردن، تصاویر ماهواره‌ای این پایگاه را از نهادهایی در چین دریافت کرده بود.
در حمله موشکی جمهوری اسلامی به این پایگاه نظامی آمریکا، سه نظامی آمریکایی کشته شدند.
براساس گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی نام نهادهای چینی را که گفته می‌شود تصاویر ماهواره‌ای پایگاه را در اختیار جمهوری اسلامی قرار داده‌اند، اعلام نکرده‌اند. این مقام‌ها همچنین دولت چین را به مشارکت یا دخالت مستقیم در این اقدام متهم نکرده‌اند.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، نیز روز یکشنبه ۲۲شهریور۱۴۰۵ به گزارش‌ها درباره دسترسی جمهوری اسلامی به تصاویر ماهواره‌ای یک پایگاه نظامی آمریکا در اردن از طریق نهادهای چینی واکنش نشان داد.
ترامپ گزارش مربوط به دستیابی جمهوری اسلامی به این تصاویر، پیش از حمله‌ای را که به کشته شدن سه نظامی آمریکایی منجر شد، «کم‌اهمیت» دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78367" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/upJJE0fjuPNW7XmnIaVFzN8tRsc9qF_m3zPqr1e-GwxFecXdI0hS9HVTeubrgJv_vg9YGmfcXI1WeMn1BXIXvuRH99l_zmbmp18R2YvD2NwXranP1BdQQDDfQPN1F13RYv23odVQeVVjUdVwfQVocdOExXZdxExlqd91GK6o0QB4-xWq-tD4ttx4_6oiRU6oNIHNCn0guAhOQnqCooKq1Js1Vy3t-v-HrDFocyelG51JTCZdJI0xD1SoTGfRIvvHlBywbCWjjqOVCKFQHJrKX1ZXkapEe6XGCfvrvtZkp0fU-dGQMaMxNVHNj-43FsZVhoo2_4AHymFGwbP52kTHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q_pHsM2BqjNM_pZymfZfg8ZrObcmla4M_7acZ7aiHx_3-oRN7SQoukxDZpjdEZzmaVF441RjByHP3llK-GANK7IMUillxnsSkLwBeRicAI2qUbdXqidzZM407SSzEG-9niaIKemDWiyjYlMevAAdaqpdi4dBnkrSph7_GMWHvfURir6GKDat4auH1D4cjzXQY00iSMNkPT4v6ii4VJkopIkAOJjLLgp0j2E_peq_NNnmqgnidp826eBfqpjWy44RSat81Jz2a8rC4cbpwwn3NaGoqmDPI8mPVv32H7j_VMUJqwc56jy80zcEoPn1tMxgM73mKuI5uyJbu6Y3RGjwHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه و پس از اعلام خبر صادر نشدن ویزا برای محمد اسلامی، رئیس سازمان انرژی اتمی ایران برای شرکت در نشست مجمع عمومی آژانس بین‌المللی انرژی هسته‌ای در وین، از احضار کاردار اتریش در تهران خبر داد.
بقایی با اعلام این خبر گفت می‌دانیم که این تصمیم تحت فشار آمریکا گرفته شده است اما این واقعیت، چیزی از مسئولیت اتریش کم نمی‌کند.
@
VahidOOnLine
پیش‌تر:
به گفته یک مقام آگاه که با اسوشیتدپرس گفتگو کرده، محمد اسلامی، رییس سازمان انرژی اتمی ایران، برای نخستین بار در چند سال گذشته احتمالا در نشست سالانه کشورهای عضو نهاد ناظر هسته‌ای سازمان ملل متحد در وین شرکت نخواهد کرد، زیرا از سفرهای بین‌المللی منع شده است.
این مقام گفت اتریش از کمیته تحریم‌های سازمان ملل خواسته بود برای اسلامی معافیت از ممنوعیت سفر صادر شود، اما این درخواست پذیرفته نشد.
این مقام که اجازه اظهارنظر درباره این موضوع حساس را نداشت، به شرط ناشناس ماندن صحبت کرد.
اتریش به عنوان میزبان سازمان ملل متحد در وین می‌تواند برای مقام‌های تحریم‌شده درخواست معافیت از ممنوعیت سفر کند تا آنها بتوانند در نشست‌های بین‌المللی سازمان ملل حضور یابند.
به نوشته این خبرگزاری آمریکایی، حضور نیافتن اسلامی در کنفرانس آژانس بین‌المللی انرژی اتمی نشانه دیگری از وخیم‌تر شدن سریع روابط ایران و کشورهای غربی است.
از زمانی که اسرائیل و آمریکا در جریان جنگ ۱۲روزه به تاسیسات هسته‌ای ایران حمله کردند، جمهوری اسلامی اجازه دسترسی بازرسان آژانس به تاسیسات هسته‌ای آسیب‌دیده در این حملات را نداده است؛ این در حالی است که تهران بر اساس تعهدات خود در چارچوب پیمان منع گسترش سلاح‌های هسته‌ای، از نظر حقوقی موظف به همکاری با آژانس است.
آژانس همچنین نتوانسته است وضعیت ذخایر اورانیوم ایران با غنای نزدیک به سطح مورد نیاز برای ساخت سلاح هسته‌ای را راستی‌آزمایی کند.
تحریم‌های سازمان ملل که دوباره برقرار شدند، شامل ممنوعیت سفر، تحریم تسلیحاتی متعارف، محدودیت‌های مربوط به توسعه موشک‌های بالستیک، مسدود کردن دارایی‌ها و ممنوعیت تولید فناوری‌های مرتبط با برنامه هسته‌ای است.
با وجود اظهارات این مقام درباره احتمال عدم حضور اسلامی در کنفرانس، خبرگزاری دولتی ایرنا روز شنبه گزارش داد که اسلامی تهران را به مقصد وین ترک کرده است تا در کنفرانس آژانس شرکت کند و با نمایندگان کشورهای مختلف دیدار داشته باشد.
مقام‌های ارشد کشورهای عضو آژانس بین‌المللی انرژی اتمی قرار است از دوشنبه تا جمعه در مقر این نهاد در وین گرد هم بیایند.
آنها درباره بودجه آژانس تصمیم‌گیری و آن را تصویب خواهند کرد و درباره دیگر مسائل سیاست‌گذاری، از جمله پادمان‌های هسته‌ای در خاورمیانه، گفت‌وگو خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78365" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g07G44nwNP5wWGsU0tvO0F_HpJzFhyYUon-IafMqD0zArdkmEFeEgZ7FSfzlSLYay_AhPARC0-xLWY8NHbBVHVYQmAcDb8uMedNb4vgy4S7Bebr05M1KjiRtRo1fe7Fllvqvm83vr-aJ6hPccf0SWwfALLb32dP5m4X290OVcUPGNRD1EN0ATbz8Fq2eyPnEnUIhQ8JtDXF7nH9-8-DcJYh-dVe4MmwO_m3qzJKKmhnL2jO18eqJpNiUtfsbQxlm6Xu7oz2fW-sUaa-iV0prVK-INoumq7zI0yWQoL3q8cUvGEb9f0AaeGeydGplqeSMCr2MheLCF4CXm_VCJPhFdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آستانه چهارمین سالگرد قتل حکومتی مهسا ژینا امینی از اصفهان، رشت، فومن، مشهد و نیشابور ‌خبر از تشدید فشار برای تحمیل حجاب اجباری و حضور دوباره گشت ارشاد، حجاب‌بان‌ها و نیروهای لباس‌شخصی در خیابان‌ها می‌دهند.
یک شهروند گفت در میدان علیخانی اصفهان ون گشت ارشاد مستقر شده‌ است و ماموران «بدون تذکر قبلی»، زنانی را که حجاب اجباری ندارند بازداشت می‌کنند و با خود می‌برند.
شهروند دیگری فضای اصفهان را «به شدت امنیتی» توصیف کرد و گفت نیروهای گشت ارشاد در مناطقی چون جلفا، مرداویج، چهارباغ و میدان نقش جهان مستقر شده‌اند و با زنان بدون شال و روسری، برخورد می‌کنند.
یکی دیگر نوشت: «در اصفهان دیگر ون گشت ارشاد نیست، اتوبوس است. با اتوبوس دختران را جمع می‌کنند و می‌برند.
...
در مشهد نیز شامگاه ۲۲ شهریور، نیروهای مسلح وارد پارک ملت شدند و به زنان تذکر حجاب دادند.
شماری از شهروندان از رشت گزارش دادند برخوردهای قهری درباره حجاب اجباری در این شهر شدت گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78364" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=qGtYyBuxEvRXYzFd59ryz-S-XeYAAdtjYEMdHsUiNN15F_6rtBk_c-aV2OcmFTBIF1qCucpPHqF9l_m5qMmMzkQi27oBB-LGAPsmrusnQuMQKLbZjNqNQoSfjkZ9BdQh2TaLLZ2eUUzj7bu9-Xx1p9yfkLK4iAIVMREWQu5zwklmdS2cRodDVdPaz5Cmx3-yWZpI_a2w9U2VQDaN6C8b88EgNx0yLoTGdJzVta1RCGoUfwvlTHF8boS8JrMAhm8SN8KvT6YNUD_yTpU73ffUikaGs2IWyX-0a5eayOoTusok9CMvzKPub2yblPllv871AXkLPDiytsAFFw941Keoqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=qGtYyBuxEvRXYzFd59ryz-S-XeYAAdtjYEMdHsUiNN15F_6rtBk_c-aV2OcmFTBIF1qCucpPHqF9l_m5qMmMzkQi27oBB-LGAPsmrusnQuMQKLbZjNqNQoSfjkZ9BdQh2TaLLZ2eUUzj7bu9-Xx1p9yfkLK4iAIVMREWQu5zwklmdS2cRodDVdPaz5Cmx3-yWZpI_a2w9U2VQDaN6C8b88EgNx0yLoTGdJzVta1RCGoUfwvlTHF8boS8JrMAhm8SN8KvT6YNUD_yTpU73ffUikaGs2IWyX-0a5eayOoTusok9CMvzKPub2yblPllv871AXkLPDiytsAFFw941Keoqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ویدیوی نجات خلبان آمریکایی در ایران
۲- یک نفر از ۷ نفر سوت موشک که داره به سمتشون میاد رو می فهمه.
سعی می کنه به نفراتش خبر بده اما نمی دونه کدوم طرف بدوئه. در نهایت یک انفجار هر ۷ نفر رو می بلعه.
A_z_im
سی‌بی‌اس پس از پنج ماه با یکی از دو افسر ارتش آمریکا گفتگو کرده است که در نیمه فروردین‌ماه هواپیمایشان در اطراف اصفهان سرنگون شد.
این افسر که براوو معرفی شده، لحظه برخورد موشک دوش‌پرتاب با جنگنده اف-۱۵ آنها را مانند برخورد یک قطار باری توصیف کرد و گفت به همراه خلبان که در این گزارش «آلفا» معرفی شده، تلاش کردند هواپیما را نجات دهند اما خیلی زود دریافتند که امکان نجات هواپیما نیست و باید خروج اضطراری انجام دهند.
پس از خروج اضطراری (ایجکت)، آلفا و براوو در حالی روی زمین در بیابان ناهموار در ایران فرود آمدند که حدود هشت کیلومتر از یکدیگر فاصله داشتند و هرکدام تنها بودند.
آلفا سالم فرود آمد، اما براوو خوش‌شانس بود که زنده ماند.
براوو گفت: چتر نجاتم در حمله اولیه آسیب دیده بود. یک لحظه به بالا نگاه کردم و دیدم چتری وجود ندارد؛ ترسناک‌ترین چیزی بود که در تمام عمرم دیده بودم. همان‌جا مکث کردم و دعا کردم: «خداوندا، اراده تو انجام شود. اما اگر قرار است از این ماجرا جان سالم به در ببرم، به کمک نیاز دارم.»
او در پاسخ به این پرسش که «فکر می‌کنید هنگام برخورد با زمین با چه سرعتی حرکت می‌کردید؟» گفت: براساس توضیحاتی که دادم و جراحاتی که داشتم، متخصصان معتقدند با سرعتی بین ۱۱۳ تا ۱۶۱ کیلومتر در ساعت با زمین برخورد کردم.
او افزود: یک معجزه در روزگار مدرن بود. باور دارم این اتفاق گواهی بر لطف خداوند در زندگی من است که باعث شد از آن لحظه عبور کنم؛ به‌گونه‌ای که هرچند دچار جراحت شدم، اما آسیب‌های فاجعه‌باری که می‌توانست توانایی‌ام برای زنده‌ماندن را از بین ببرد، متحمل نشدم.
این سقوط باعث شکستگی کمر براوو شد. او همچنین دست و شانه‌اش شکست، مچ پایش پیچ خورد و سر و صورتش بر اثر بریدگی و خراش خون‌آلود شد.
براوو گفت، مجروح بودم، اما همه ما آموزش دیده‌ایم که با شرایطی که با آن مواجه می‌شویم سازگار شویم و بر آنها غلبه کنیم. با وجود جراحات، تا جایی که می‌توانستم سریع از محل فرودم دور شدم.
براوو به سی‌بی‌اس گفت امن‌ترین جایی که می‌توانست به آن برود، ارتفاعات بود.
بنابراین با وجود شکستگی استخوان‌هایش تصمیم گرفت از مسیر کوه بالا برود و خود را به خط‌الرسی در ارتفاع حدود ۲۱۰۰ متر، برساند.
@
VahidOOnLine
چیزی که می‌بینم رسانه‌ها و کاربران فارسی‌زبان دقت نمی‌کنن اینه که این مصاحبه نمی‌گه که افسر آمریکایی با دست و پای شکسته کوه ۷ هزار پایی رو بالا رفته؛ بلکه می‌گه خودش رو به ارتفاع ۷ هزارپایی رسونده. بین این دو تا خیلی فرق هست.
در نظر داشته باشید که خود اصفهان بین ۱۶۰۰ تا ۲۰۰۰ متر از سطح دریا فاصله داره. یعنی ممکنه ایشون فقط با صد متر صعود خودش رو به ارتفاع ۷ هزار پایی برسونه.
Ardeshir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/78362" target="_blank">📅 08:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Opivj9WU2ApnFybIkaMFPLC4PsHXDNI3-Dqy22989SppLwyr2XLL3eIZiyusDEhIYyNmv4sVdBVX0jp7IkdAtVKtH6BDu3OobHb0nFn47WutuiVTZJ6jQtAlCQBmLkMwv8yQKoMLobQHpkUZ4xw8giyagDaiNYSgbWzTF3YzP9e_M0A7C-68ZhrViPTc5TJgB4mDtHsBLPZXBpuVGMbmUQOVhd2C-ndas4XO-REZbOFYrag0fedaPgMhzq2uGQX4J4trzDNHFYR7eat0SiiUyaHGWAIbCvK01I0ya77L6eYK2sa_zw4ntJzbX88P0F6DTx_5cF38p0SDqqyPdqcZ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه عمان از تعویق‌ نشست ایران و کشورهای حوزه خلیج فارس و منطقه خبر داد؛ نشستی که قرار بود روز دوشنبه ۲۳ شهریور در شهر صلاله عمان با محوریت وضعیت تنگه هرمز برگزار شود.
بدر بوسعیدی، وزیر خارجه عمان، روز یکشنبه ۲۲ شهریور در شبکه ایکس نوشت که این نشست «به منظور دستیابی به اجماع» به تعویق افتاده است.
او تاکید کرد عمان همچنان به تقویت گفت‌وگوهایی که به «ثبات و همکاری پایدار در منطقه» کمک کند، متعهد است.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، پیشتر گفته بود که روز دوشنبه در نشست هشت‌جانبه وزرای خارجه کشورهای ساحلی خلیج فارس و دریای عمان در صلاله شرکت خواهد کرد.
قرار بود در این نشست درباره طرح ایران و عمان برای ایجاد سازوکاری جهت تردد امن کشتی‌ها در تنگه هرمز گفت‌وگو شود.
تعویق این نشست در حالی اعلام شده است که آمریکا پیشتر تاکید کرده بود در مذاکرات مربوط به تنگه هرمز مشارکت نخواهد کرد و هرگونه مذاکره مستقیم با جمهوری اسلامی را بر پرونده هسته‌ای متمرکز می‌کند.
مقام‌های آمریکایی به کشورهای منطقه گفته‌اند واشنگتن درباره وضعیت تنگه هرمز مذاکره نخواهد کرد و موضوع اصلی مذاکرات احتمالی با تهران باید برنامه هسته‌ای جمهوری اسلامی باشد.
مارکو روبیو، وزیر خارجه آمریکا، نیز پیشتر گفته بود تنگه هرمز نباید تحت کنترل جمهوری اسلامی باشد و آمریکا برای تضمین امنیت کشتیرانی در این مسیر اقدام خواهد کرد.
در مقابل، جمهوری اسلامی و عمان تلاش کرده‌اند کشورهای منطقه را در گفت‌وگو درباره سازوکار تردد کشتی‌ها در تنگه هرمز وارد کنند.
قرار بود نتایج رایزنی‌های تهران و مسقط درباره مسیرهای امن کشتیرانی در این نشست به کشورهای منطقه ارایه شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78361" target="_blank">📅 22:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0c_FGt4Bgaf3LUdA31ouPvYlv_YeC0XcueBji7PoJof20Ud-g6JaAGYyUyFsIDcB3mOk1i3-cPKpC28LwGHqIxL0lO_rK1bg79hmONe4XrbYmYvZp13vR9eSIEAwkpTg_dUKJuKgoc8vyoeBs4HvL0zwOa6Jz88N3ODCQdC2msu76m3zFQtZAYBIPynX5Tqcv3XRjNW1Q0iURg7dQ7GQE0FCI7d_0TF35Mef9GIpo5zqoiGVpFe38ZFIeNxaA8BL2krFiHWUZIYGGUJBRx5yFbvO4DWGTtwj_x8-7ifEgFT_a7cBPZok8shDI9dRFcP-0_EzGNAYp1e-huPrV8VLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز روز یکشنبه ۲۲ شهریور ماه در گزارشی به نقل از چند مقام ایرانی نوشت، مسعود پزشکیان، پس از حمله نیروهای سپاه پاسداران به سه کشتی تجاری در تنگه هرمز در اوایل تیرماه گذشته، به‌شدت خشمگین شده و این اقدام را «بی‌پروایانه و غیرمسئولانه» خوانده است.
این حمله‌ها که منجر به آتش‌سوزی یک نفت‌کش حامل گاز مایع قطر و آسیب به شناورهای دیگر شد، درست زمانی رخ داد که ایران به توافقی با ایالات متحده برای پایان دادن به درگیری‌ها نزدیک شده بود.
بر اساس این گزارش که فرناز فصیحی به نقل از مقامات ایرانی نوشته است، پزشکیان پس از آگاهی از این ماجرا با احمد وحیدی، فرمانده کل سپاه پاسداران، تماس گرفته و با لحنی تند خواستار پاسخگویی شده است. با این حال، وحیدی ضمن سلب مسئولیت و ابراز بی‌اطلاعی، به رئیس‌جمهوری اعلام کرده که نه مجوزی برای این اقدام صادر کرده و نه شورای عالی امنیت ملی از این عملیات مطلع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78360" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/930e263d13.mp4?token=jjxOr5mAZhNRqPTQ5Uj3Ky5jPv421S9ul3GimQACqCZwSlrYC2O7gfBlnkwMVwGjhPL90sYl7lDWiSUFEvuv9d463wUbV91UuVBE-ZiqFbQdyfFXS-PUMtoKTsmtHgNkPEDE6GWI5vbgx1I7lEQIjiSvh-LJmXG1LDxyNi0rQMHmyB1DhsvwI4JuTLEFPpwFImJMai-gaMF4tFxF_n44uC0YkEA6KL83mUQRHAtVro8i6Bu5OYdcYlS4JNyFcAD9A41NCdi7muwgWYo5pjO4LXH9cYtSyiaWrwyevkpLCEITaeUFeuqI9QL-s0BFQB1r__6rXExBhgJSlK736RGFpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/930e263d13.mp4?token=jjxOr5mAZhNRqPTQ5Uj3Ky5jPv421S9ul3GimQACqCZwSlrYC2O7gfBlnkwMVwGjhPL90sYl7lDWiSUFEvuv9d463wUbV91UuVBE-ZiqFbQdyfFXS-PUMtoKTsmtHgNkPEDE6GWI5vbgx1I7lEQIjiSvh-LJmXG1LDxyNi0rQMHmyB1DhsvwI4JuTLEFPpwFImJMai-gaMF4tFxF_n44uC0YkEA6KL83mUQRHAtVro8i6Bu5OYdcYlS4JNyFcAD9A41NCdi7muwgWYo5pjO4LXH9cYtSyiaWrwyevkpLCEITaeUFeuqI9QL-s0BFQB1r__6rXExBhgJSlK736RGFpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش، پس از اعلام نرخ سوم بنزین در ایران، تصاویری واقعی در شبکه‌های اجتماعی منتشر شده بود درباره اینکه بعضی از تلمبه‌ها در جایگاه‌های سوخت (پمپ بنزین) امکان نمایش همه ارقام بنزین ۱۰ هزارتومنی رو ندارند و مجبور شدند در ادامه نمایشگر یک صفر بچسبونند روی بدنه تلمبه.
حالا محمدباقر قالیباف، رئیس "مجلس شورای اسلامی" در «ایران»، اون انیمیشن رو پست کرده.
ولی درباره قیمت سوخت در یک کشور دیگه:
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78358" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fiubxrc6g_CjRlr7YCISvOkMfPHhtWAO42pphyf9xQU7Zg278zu-xfKXhY_RDOdo7-uEzRvdgp1LCxUGuWhVmkkHe4gZqZ7jObaoSzKkgRkZ9L50u2rhUjPd4Bxbhcf936WN3Imqzq0qroQhFvx6x_PPusOGVlXABp2xJvFvVtbJn6ZQLhVWZW_XZ5hdeJ0FW0M_S2fRS7EWEqpURKjMnKY13bSHNFPExRDcRfVEg-kM2McdQ6n6VFVIc1P1-tUsoccvj2AxBcsOKKryCEP2Z7fmEQWrjObkWI-NecwDlS0kOBHy0cH3fB5w1OkeaLut2Ez1vwPLQmYSa-0MfpfjKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین رسولی‌نسب، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در شاندیز، به اتهام «محاربه» از سوی دادگاه انقلاب مشهد به اعدام محکوم شده است. او در حال حاضر در زندان وکیل‌آباد مشهد نگهداری می‌شود.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، روز یکشنبه ۲۲ شهریور ۱۴۰۵، گزارش داد حسین رسولی‌نسب به «محاربه از طریق مشارکت در تخریب اموال عمومی» و «اجتماع و تبانی علیه امنیت کشور» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78357" target="_blank">📅 18:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iV1ix0ug2ra0cJUWzLwinnkG9prFqAunCIxayMLcufUtAx945QLFH7Pu4IbkJ31xOW1S1ou4V-RWsSvsK2UEDVRiqr88RUG3VoCUkaAIdBO0FPX8aBAib88yuSagIsibXemGfM6699iQoYN2hMtenjNWonDIVMQGsBhygZldt2xssy-rKgy1NhBauFlGJlmNq4FEie0pYanVx-DBPspkUHpdYTpP3lf3C8rL3K-5p2F5aEKrYmyVE83VgIV2xdLcTpSh4IhEb8UZH-NMNe-T-Av-iqUu_Sz9BDQaKd7L9a3rIqU-ihfM2TPqIFLrw0xxW5ooPwLIP_He0WRwMMjKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WeFUIp9ZSfrWZ-zfg52UEB0FgLORqq1hILMFtRMlnTZw0NghwaevKJMmIGLN4W7H0DuRj7pn4yYrWMCWvITkxk6T7ULWpuYWwOKv6L4H3QzRmk8vZGaF5VlEW5QtD6ADnVIAmCfrwq8JI4YxodkJOBwvqRoD5SHyT-RkxCcFEvab_uai2L1TH3EqSoW4gIgf_g4Ir0MYhnHj0TtU9nyWPckrIAPr2DOdwBtqCslpr3ahcHUHKkcnu2YvKEFI0UJ7-S_MLJvxQxE8aBwfhT7wydfh3F5yVYH24ZmmMaWcREDenLTKC_C77wDhd_UmchimDp3Ra_KfReRLMdajlq3ppw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78355" target="_blank">📅 18:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HBxo9oKUfklXLzjaSkrm5phpcp3Fne2meDP1OY_WAhdut34DXEdjUL8JsAO5M6Shi04uTnwpOSQBJVlgs5D_WMjRCSrSiSGJPGPrLFv2y9q48JoFtJ3zUG3J-xQt0AlfL2gsNtZZhtZk6E28sFqLia1XAtf8stkN3R8d54lzqZmcCLfHQx9PS4SovaF1Gl9SXNmJuFW7xi_Amo1o3kfTz-InNKw-_uMmYVmDoaxZrN71BtlByuS_M_5h4H6XZjK9nQSLe5PMPATKzSxJRsfDsvG32Xo80xqIu9d3t_knEHSED9-mV6xQMsAP-dpzTmjocYCK5ii-SViQbHDO1HyXwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز یکشنبه ۲۲ شهریور۱۴۰۵، گفت «موضوع ایران» ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا پایان یابد، اما در هر صورت جنگ با ایران بلافاصله پس از این انتخابات تمام خواهد شد.
ترامپ در جریان سفر به ایرلند و در حاشیه مسابقات گلف اوپن ایرلند، درباره احتمال توافق با جمهوری اسلامی گفت ایران به‌شدت خواهان توافق است و به‌طور مداوم با آمریکا تماس می‌گیرد، اما واشنگتن تنها توافقی را می‌پذیرد که به گفته او «درست» و مطلوب باشد.
او همچنین در پاسخ به پرسشی درباره دیدار وزرای خارجه کشورهای خلیج فارس و دریای عمان با ایران گفت این موضوع برای آمریکا اهمیتی ندارد و تصمیم درباره دیدار با جمهوری اسلامی به خود این کشورها مربوط است.
قرار است این نشست روز دوشنبه در عمان برگزار شود. ایران می‌گوید یکی از موضوعات مورد گفت‌وگو در این نشست، مسیر جدید تردد در تنگه هرمز خواهد بود.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز بار دیگر گفته است شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78354" target="_blank">📅 17:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BwtJ7vhyzaitin4KC-X-98xsoDA7uE2xUvsRG-n46NaRAM1DGDKtFYAOq4qPr2xsAoDFkOnaept3m_HI-Vi7ndupJU5IglojRrIVpqGfDJwSWz1TVPwV4lAxH0xJVJSfgMznvy11ZewVE57SYRNWKQ6A_FKJ-aI8epWEjune_7eGayj0V4J01RhzU209yjCAg9HDarGM-CVoZQ38nhZ0r-CaF5LRHwZj6sOfnI-TfLWifWflrwzg4Vp9xXq1Eg_VMqfED3rUCRVs6zD2Lm-tuxK1-cm1106UxBysaEOMP3nJBp0U4o-3mvUEF9UZ-K25X3ku9OR9S2akbAaR4gJaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/asK1rbumylHHYsIydXLFbmQKoCwuhUDTd-Cz367lISeOAIJqQyu1nJpd7ml5fjq5OTQFITEZnY87zqD7FzqSgG7DJIKL6BK2f7lRxITce4TFZIOeGMNzKOfGsq4W6BLz-ZKdIoIQzCCQcM3GNqSxyDqMhYxvE1NHI26S-UfgQOsV7qz45enFmN0R-_WZR1RBjgVEQ9GQV8Isvdd6SC8spbyiex3Wr2IrIcCD2_0h0oa28ITINbmpsX697AWgLNrh0muK34Dh2Ze38yDaZg3KIIbDHYHPo7xhCbD0Syeda6QpapziItVZppcJF3AvzKEQR4Z4lfgeaOm82eeBw6qtYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز شنبه، با صدور یک هشدار امنیتی، از هدف قرار گرفتن یک کشتی در تنگه هرمز خبر داد.
این نهاد نظارتی دریایی اعلام کرد: «گزارشی مبنی بر وقوع یک حادثه در محدوده تنگه هرمز دریافت شده است. یک کشتی هنگام عبور از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.»
@
VahidOOnLine
امیر تیموری، فرماندار شهرستان قشم، اعلام کرد یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب‌دراز جزیره قشم هدف قرار گرفته است.
به گفته فرماندار قشم، در این حادثه یک نفر کشته و سه نفر دیگر مجروح شده‌اند.
تیموری عامل این حمله را آمریکا اعلام کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78352" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=dYSgHyEeWBpJeq90qms4SjfgqwoLlB7zaJZm5eiuBbfJNLBEotGOsOb0Wfr9LYL7UpkbIEU37Rud2-AQDZUjuMXTdCHVRg_WHJ3Ff9PrF9AEdifTsZ9rUb-Ft3rEUqUzATlWCx_RVDn3SRBB7ddDn9egTKUYziUosyOwcGhp6mBuGj3qRm3vd74I3mKCYXc59uGuTGiQSYGADl27hdwJAjuz0CjQp5tnUspGFWp314H6OgGyNJRhE7j_8WMXxFJlH8SJYppL3mFYIsinJalhtZxV4qGvfrPqlIYKZWfHEJ0vpiKuWcuPeYgRnSc87Dij7sjqBK8YRKRetH0HYJyoFYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=dYSgHyEeWBpJeq90qms4SjfgqwoLlB7zaJZm5eiuBbfJNLBEotGOsOb0Wfr9LYL7UpkbIEU37Rud2-AQDZUjuMXTdCHVRg_WHJ3Ff9PrF9AEdifTsZ9rUb-Ft3rEUqUzATlWCx_RVDn3SRBB7ddDn9egTKUYziUosyOwcGhp6mBuGj3qRm3vd74I3mKCYXc59uGuTGiQSYGADl27hdwJAjuz0CjQp5tnUspGFWp314H6OgGyNJRhE7j_8WMXxFJlH8SJYppL3mFYIsinJalhtZxV4qGvfrPqlIYKZWfHEJ0vpiKuWcuPeYgRnSc87Dij7sjqBK8YRKRetH0HYJyoFYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تور اجبارى اتاق شلاق براى "عبرت" متهمان
یکی از شهروندان با ارسال ویدیویی که مخفیانه از اتاق اجرای احکام شلاق ثبت کرده، مشاهدات و تجربه مستقیم خود را با بنیاد عبدالرحمن برومند در میان گذاشته است؛ روایتی که به‌زودی در قالب یک شهادت‌نامه تفصیلی منتشر خواهد شد.
او درباره انگیزه خود از انتشار این ویدیو پس از چند سال می‌گوید:
«آنچه در جریان بازداشت و صدور این حکم بر من گذشت، در برابر حجم بی‌پایان ظلم و بی‌عدالتی شاید اهمیتی نداشته باشد؛ آنچه برای من اهمیت دارد، تاباندن نور بر گوشه‌ای از این سازوکار مخوف است تا همگان ببینند مردم ایران برای داشتن یک زندگی معمولی با چه مجازات‌های تحقیرآمیزی روبرو می‌شوند.»
@
IranRights
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78351" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=YgZWUD4eR-jPYEBR4aFeTISKBGPMqTavMRJj-7yXNUYQZjrJ8agvjeJdqxiWbIaJBnRN1gYKpoRWQPjyawW4j14EChPv7Qs06uXeYrJnsuTodGHgcfNbu6f4JkPamuTjcqJmhRNT4tduZUtYx92weWNVwIGQ__fmjLBNJzge_L2Vk3eSHEZYzqynYa0OrRfu-eIyH_aU6EVdsymzuwMUbn6HHsEqF-zWUWe5sNi0-XAp-koBdBqTvnvk96Co-grVrcFxPZZkXeyHARBZ-N6DTj5-UuD6tzkIj7DD8J5pP3vA1WnDJkCxMhMf-YuTA56cB_UZ_mpV5-jXB-yf3A47Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=YgZWUD4eR-jPYEBR4aFeTISKBGPMqTavMRJj-7yXNUYQZjrJ8agvjeJdqxiWbIaJBnRN1gYKpoRWQPjyawW4j14EChPv7Qs06uXeYrJnsuTodGHgcfNbu6f4JkPamuTjcqJmhRNT4tduZUtYx92weWNVwIGQ__fmjLBNJzge_L2Vk3eSHEZYzqynYa0OrRfu-eIyH_aU6EVdsymzuwMUbn6HHsEqF-zWUWe5sNi0-XAp-koBdBqTvnvk96Co-grVrcFxPZZkXeyHARBZ-N6DTj5-UuD6tzkIj7DD8J5pP3vA1WnDJkCxMhMf-YuTA56cB_UZ_mpV5-jXB-yf3A47Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهوری آمریکا در جریان دیدار با مایکل مارتین، نخست‌وزیر ایرلند، در دوبلین بر اعمال کنترل مقتدرانه و یک «محاصره دریایی باورنکردنی» بر تنگه هرمز تاکید کرد و گفت این اقدامات مانع از جهش شدید بهای جهانی نفت شده است.
دونالد ترامپ همچنین گفت نیروهای سنتکام به‌طور میانگین روزانه ۲۵ شناور و قایق را متوقف و توقیف می‌کنند؛ اقداماتی که به گفته او بیشتر آن‌ها در تاریکی شب و در جریان گشت‌های شبانه انجام می‌گیرد.
این در حالی است فرماندهی مرکزی آمریکا، سنتکام،
امروز
اعلام کرد طی ۶۰ روز گذشته و از زمان ازسرگیری «محاصره دیوار فولادی» ایران، مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78350" target="_blank">📅 23:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxmiCj63yCTrQ_xgil__YzF1RcGTH8FDaubs06EeCO-nIcf6dq-iUBBmP0XPsiJw1o99K1jpIu1zb0F9L4rPYzguGNf0tYb7Fdl3j-9zceB1w_Wbmc5b1oARIx1tpFLZiz8ohyPNeOutVM6tKVnXEipTz7DcAE_UNa7D8HkOEPzfx-_-hlb96rPB6tavgwLQrbxkDmc5PNRfgbn7A7v-d7IJZ1c9M9wczlymY-RNMXvhdYYexip-mhiZZlgTKRyn2ddShb-OxAUhVuHSvx41BxsqbilpRaIcMbWIJHhYBcB3A9kXtVwedJqFngQzdRZZwgSLWSvbcusv_-M-z0VwGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی یک دستگاه اتوبوس حامل کارگران مجتمع مس سرچشمه، در صبح شنبه ۲۱ شهریور، یک کشته و ۳۸ مصدوم برجا گذاشت.
سید محسن مرتضوی، رییس مرکز فوریت‌های پزشکی رفسنجان، با تایید این خبر گفت ۳۸ مصدوم این حادثه برای دریافت خدمات درمانی به بیمارستان منتقل شده‌اند. به گفته او، بررسی‌های اولیه نشان می‌دهد ورود یک دستگاه ون به مسیر حرکت اتوبوس باعث انحراف و سپس واژگونی آن شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78349" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b10cD4tA-JgJPt6sC69fQQL4K0Ta3-UHLspDmCXWV4HTJboLQI6dqHucpctyDucpGBVuf1sMpV23Ss3gdQhPtXgMO_FxJueuOavNVu8xtAUh8qU0H6QT8PHK8S_zcvsVYGa4pP0Og2m0_dZp69rufgKKuGeb7ScxOPUf94qAv6bIplPP03-y3q1DwUD1ldJv_Xl5KHnVqsEhntt8YK0DEHHzZWhmwnxpgVw5nhbYwLbNv_Lwr_I1NwPtm55q7yisLipAbEpamR1YYjBF7yIQZwlJOqvf_ATw0uzGb6lxT3HVu8M1rL-EMLnTFfkGByWWHgHpZfJBna5i6xk2OA1eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع امنیتی عراق به خبرگزاری فرانسه گفتند نیروهای امنیتی این کشور سکوهای پرتاب پهپاد را منطقه دورافتاده الطیب در استان میسان در جنوب عراق و در نزدیکی مرز با ایران کشف کرده‌اند.
همزمان خبرگزاری رویترز به نقل از دو منبع نظامی در عراق اعلام کرد این منطقه مرزی پس از کشف سکوهای پرتاب پهپاد بسته شده است.
کشف این سکوها پس از حمله به خط لوله نفت عربستان سعودی انجام شده است؛ حمله‌ای که ریاض و بغداد گفته‌اند از خاک عراق انجام شده است. بغداد روز شنبه گذرگاه‌های مرزی شلمچه و چذابه را نیز بسته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78348" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0fjQQwiCldWtVRptP_Kb0RBo0t87KG7899Cp9TWaAsN4v59wKvE4qpnxMUE6nUxVP0ALFoMqqS4EfzR9yoH57YcX4id2Cfk5Kcr0FKQgP322D4LCV2wsZ3DrC6E2VKp6coMVPGB9mLhPVbE5636SUj3cRU_EtWu4ZpbenXpOv1TFk33YwcFegpgJ1tJVHRjSjPwHVpTiiDfA00P-RVqzrsfad9LyYc0xKbuWWBd0WA3U04Cbku18U_CrukYMQedPwiJvFK6vojm1ssuxOgW2D_FMa5HImW5FGpgD0vhGMcrbkwXowCKqzHOZK3NEYeQsuQJLvd37Rli32ctC0Tq_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، به نقل از یک منبع آگاه گزارش داد تفاهم نهایی جمهوری اسلامی و عمان درباره مسیرهای جدید کشتیرانی، به معنای بازگشایی تنگه هرمز نیست و باز شدن این تنگه به اجرای هفت شرط تهران از سوی آمریکا بستگی دارد.
این منبع گفت تهران و مسقط پس از گفت‌وگوهای فنی و دیپلماتیک، در اوایل شهریور درباره جزییات مسیرهای جدید ورود به خلیج فارس و خروج از آن به توافق نهایی رسیدند و قرار است این تفاهم به‌زودی با حضور وزیران خارجه کشورهای منطقه اعلام شود.
بر اساس این گزارش، تفاهم تنها میان جمهوری اسلامی و عمان است و کشورهای دیگر، از جمله عراق و کشورهای ساحلی خلیج فارس، برای اطلاع از جزییات مسیرها و ترتیبات تردد در نشست حضور خواهند داشت.
مهر نوشت مسیر ورود به خلیج فارس به‌طور کامل و بخشی از مسیر خروج از آن در آب‌های سرزمینی ایران قرار خواهد داشت و تردد در این مسیرها بر اساس ترتیبات تعیین‌شده از سوی جمهوری اسلامی انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78347" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=cSfqBZCfLwu_ng9Uk5wVRHdOIAfPAPCvobv0yKkEra_svShlNsOmRWL5C9bdmCKGptMdbazSDXJ4nAM14y2qCHF_fF-LP-LexFAPK_SZcJCMIQr6_SZz_5xDHz_9KnqyZm0EfkAkXwLwPKeNjs65V7oh7nz739T_DL8WA4YZ3v2jRxPgaUGsMls9KY180Mouy7UAT_YYzZv4oH4u0qLHQ8rJlGDijpAMWbloWv7MwqICKYg3YhBXn22m7e9rSe67ULc3cLI27zmemtmBSH6Krm1TqLsoS-d7VHZEh2hHBVwtWyczEV5XJBZQ2DiI1Xo5-eG7ZIiiExNxZ8-INgIHPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=cSfqBZCfLwu_ng9Uk5wVRHdOIAfPAPCvobv0yKkEra_svShlNsOmRWL5C9bdmCKGptMdbazSDXJ4nAM14y2qCHF_fF-LP-LexFAPK_SZcJCMIQr6_SZz_5xDHz_9KnqyZm0EfkAkXwLwPKeNjs65V7oh7nz739T_DL8WA4YZ3v2jRxPgaUGsMls9KY180Mouy7UAT_YYzZv4oH4u0qLHQ8rJlGDijpAMWbloWv7MwqICKYg3YhBXn22m7e9rSe67ULc3cLI27zmemtmBSH6Krm1TqLsoS-d7VHZEh2hHBVwtWyczEV5XJBZQ2DiI1Xo5-eG7ZIiiExNxZ8-INgIHPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، روز شنبه ۲۱ شهریور ماه گفت اطلاعات تهران نشان می‌دهد حمله موشکی آمریکا به لامرد از خاک یکی از کشورهای حاشیه جنوبی خلیج فارس نیز انجام شده است.
اسماعیل بقایی در گفتگو با رسانه‌های دولتی ایران گفت این موضوع نشان می‌دهد آمریکا «برخلاف همه قواعد و اصول حقوق بین‌الملل» از خاک و حاکمیت ملی کشورهای دیگر برای حمله به ایران استفاده کرده است.
او تاکید کرد ایرانیان این موضوع را پیگیری خواهند کرد.
بقایی همچنین گفت برخی کشورهای همسایه، برخلاف «اصل حسن همجواری»، اجازه داده‌اند از قلمرو آنها برای حمله به ایران و «ارتکاب جنایت جنگی علیه مردم» استفاده شود.
در نهم اسفند ۱۴۰۴، یک سالن ورزشی در لامرد فارس، مورد حمله دو موشک قرار گرفت که منجر به کشته شدن حداقل ۲۱ نفر، از جمله ۴ کودک، و زخمی شدن ۱۰۰ نفر شد. این حمله اندکی پس از حمله هوایی به مدرسه شجره طیبه میناب رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78346" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcaLr9jStebvPwCTKAA1KSVpRmyFQml-3bjUjK3Pw4MF7yFdw5gdVrtNXAFl9gCaZsbOQwYnRRU40SFLp4zcwXWznGJo-P1uTGg1DEEWdz6OjAf7dRwL5VA2XkVC79L5v3ZqKJ28MFs7GZLjHhlUqs_EaEaQ6nwqP7MC-MLOPMzPOAqiF1jOaanSLvLb5nEJNFVSaIPGKoQk2atiKOGs4uab_hbmm9bqM8dDT2-xvJZ_oNlFuWHMrLH7ARZ-eaUXwa0ss8pZsQrjVJG-U0URm7iRpy7WK12v8rXvjR3NTuDCPsCQLUvA8DrveffW-7YHGTXVFg0Wz_GGAQrt6jAHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت احتمالاً جمهوری اسلامی مسئول حمله هوایی به عربستان سعودی بوده که به تعطیلی خط لوله شرق به غرب انجامید.
او روز شنبه در دوبلین و در پاسخ به پرسش خبرنگاران درباره مسئولیت ایران گفت: «فکر می‌کنم مسئول‌اند، احتمالاً خودشان‌اند.»
ترامپ افزود با محمد بن سلمان، ولیعهد عربستان، گفت‌وگو کرده و او را «دوست خوب» خواند.
رئیس‌جمهوری آمریکا همچنین گفت حوثی‌های همسو با جمهوری اسلامی با دولت او تماس گرفته‌اند و اعلام کرده‌اند نمی‌خواهند آمریکا مستقیماً وارد درگیری شود.
او گفت: «آنها به‌مراتب ترجیح می‌دهند ما درگیر نباشیم و بیشتر شناورها را عبور می‌دهند. فقط یک کشور هست که از آن راضی نیستند و ترتیبش را می‌دهیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78345" target="_blank">📅 15:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=u5IEEoNCaoRRSHE31wswsNJQ0J2PNfILaJuIlGJAPne0UEa2pWD27MyuikpRI3lMIOZaFs2hVqfeq8ia9_rZul1SDtO6wFfkn2igCFzdj57wlT1BNdI_s_VJvSYaAODwx36_WK9sCRhsaS4zVrhqBlHtOoknhBUcQu9h6nyqnapa51i_4j4XcvXKEyqoafNcUN-yaNn5Z91dnlsEQKfaaVfcYx3n7M9cwCEqpqvD71rKlTc1zAjGObH4cLCOo6EI-jWRHOPVhSmU2LWISzzJox2AhPHP9uWFbjAvJPuVjZm-oTLyf2Y6iEu-AnmUeljiVB1tL0JWQjugYhteQfWN6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=u5IEEoNCaoRRSHE31wswsNJQ0J2PNfILaJuIlGJAPne0UEa2pWD27MyuikpRI3lMIOZaFs2hVqfeq8ia9_rZul1SDtO6wFfkn2igCFzdj57wlT1BNdI_s_VJvSYaAODwx36_WK9sCRhsaS4zVrhqBlHtOoknhBUcQu9h6nyqnapa51i_4j4XcvXKEyqoafNcUN-yaNn5Z91dnlsEQKfaaVfcYx3n7M9cwCEqpqvD71rKlTc1zAjGObH4cLCOo6EI-jWRHOPVhSmU2LWISzzJox2AhPHP9uWFbjAvJPuVjZm-oTLyf2Y6iEu-AnmUeljiVB1tL0JWQjugYhteQfWN6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشرشده در رسانه‌های اجتماعی نشان‌دهنده ازدحام در خروجی مرز بازرگان است.
برخی گزارش‌ها دلیل اختلال در تردد از این گذرگاه مرزی را «محدودیت‌های ظرفیت پذیرش در سمت ترکیه» عنوان می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78344" target="_blank">📅 15:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBMQ2dAEj2BNfas5028lYo5liv3HPwKnHp26EmBBgwCvxNwLkUSW-R8wc3PoxnzQulVRBdmbqiT_gAudzY1Gf4m5FIuqP4tLVtqd9O64vrqPxGlMoFtTp9SUGQJ9jXb8IfJM8-owqcrwHVujoQVeugQXcFQAjG5LXPGLlKvp49-6bcDVWUcYU24hbHDorpxGk2YfMnQr9gGQIiJfQfpSEmqUWUiUuTVWgiG0XEhl7JyUc_0WJnDYt90cvvcLjyTfnUWBhSQdME248AW81UJqe9oY3tRKqm1AdcvU6nWrl5vXKNxkjBjMdOxjYnmKjObDLPCXIzJ9ac2CEokBwF0ufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون استاندار خوزستان اعلام کرد مرز چذابه نیز همچون شلمچه از بامداد امروز با اعلام مقام‌های عراق تا اطلاع ثانوی بسته شد. بنابر اعلام ولی‌الله حیاتی، هیچ تردد کالا و مسافری از این مرزها انجام نمی‌شود.
ساعتی پیش رویترز بع نقل از دو منبع امنیتی نوشت عراق پس از تازه‌ترین حملات پهپادی صورت‌گرفته به عربستان سعودی، دستور بستن گذرگاه مرزی شلمچه بین عراق و ایران را به عنوان یک اقدام احتیاطی صادر کرد.
مرز چذابه در استان میسان عراق قرار دارد و دفتر نخست‌وزیری عراق بامداد شنبه فرمانده عملیاتش را برکنار کرد. این برکناری پس از آن انجام شد که تحقیقات تأیید کرد آخرین حملات پهپادی به عربستان سعودی از خاک عراق انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78343" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mmkZMHWJfLcD-vIgtEt0JJWoQvXz7qMWZMvtCQRzbOQZVcOD6GBIePgNKIQB-ZWmDLPbhghKNLo3lNbdLxkbAhjVigNTsuhqnVQfeu37Dg9T9Q6jounFNtjcZQSGEWSH-hPwf73f8Di8aMXAf7T6Z1Fwuo2qQzeIjRkEsavHSg74JKtR3xzqw2VNP3rQzHCAdsHLvTRo5dnOdx6RjEhcfL_lRW5SwbcP-Ykf4GKYAWX_S2VbdPouJoQjiULmCxGVz2Gdrxl8-aGoXhZWVdAobWBal4nYTZ0mIxgD0CUtWQMPPEZXSJULwFmnsqUMHnaGiSo0tmA59KBn6zsYWI4INw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lqLASEQFV75BHSrOllDMQbA2mCaFOVGING3wYIzA12FMwL_i2m7zVxB3vA2NBIU9jRxlOzH6OVsEoaLpUGgU3nlVVB5dNDpiYmwN8tMjLkYyguYfSodZ0avsxLDfDhE3ljJKg07jd2L5SBGZYPeMP9UeycgVU5FSDyvuHcV75G-_vz97o6P9l3VtZ_w9T4GlAQnfDNFcuojp9XKlrVuA3tQs-Of8zmhDX8yk3Uf-k2bL4NQHhEzgqkMmEm54LcTYIP9fBqNWMLO4MS5rtK0YG1m1TC-orGn_XQPEplydYpmlUUzFClZNos_jj0_VY3b-Dh0BHKjRLavdKsZcjfJLCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درگیری میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح در منطقه «بخشان» سراوان، پس از بیش از هفت ساعت همچنان ادامه دارد. «شیوار نیوز» از حمله به نیروهای حکومتی از دو محور، شکسته‌شدن بخشی از حلقه محاصره و خروج شماری از افراد مسلح از محدوده درگیری خبر داده است.
این درگیری حدود ساعت چهار بامداد شنبه ۲۱ شهریور ۱۴۰۵ و پس از محاصره یک خانه مسکونی آغاز شد. شبکه اسناد حقوق بشر بلوچستان پیش‌تر از استقرار گسترده نیروهای نظامی و امنیتی و استفاده از سلاح‌های سبک و سنگین در این منطقه خبر داده بود.
براساس اطلاعات منتشر شده از سوی شیوار نیوز، نیروهای نظامی و امنیتی پس از آغاز درگیری، محدوده حضور افراد مسلح را محاصره و مسیرهای منتهی به محل را مسدود کردند. بااین‌حال، در ادامه افرادی از خارج محدوده محاصره، نیروهای حکومتی را از دو محور هدف قرار دادند.
@
VahidHeadline
قرارگاه قدس نیروی زمینی سپاه پاسداران اعلام کرد در جریان درگیری با افراد مسلح در شهرستان سراوان در استان سیستان و بلوچستان، سه نفر از نیروهای سپاه کشته شده‌اند.
بر اساس اطلاعیه این قرارگاه، این سه نفر با عنوان «پاسداران گمنام امام زمان» معرفی شده‌اند.
قرارگاه قدس همچنین اعلام کرد که تا پیش از ظهر روز شنبه، چهار نفر از افراد مسلح ناشناس نیز در جریان این درگیری کشته شده‌اند.
این اطلاعیه جزئیات بیشتری درباره هویت افراد مسلح، گروه یا سازمان وابسته به آنها، محل دقیق درگیری و چگونگی آغاز درگیری منتشر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78341" target="_blank">📅 15:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T0UZu2dkUH_cdOMM1aA9p_WZtBgWAHFkPVQefQKyp7rxefAGbdOOf43QHMaa5d5kn0Uz4O2YTKf_ZItk_ESQOw8GlRuz9VwUmJ8jeX4RSCCAxFVTmqbdUm8FWRrXu_uM_XsMyRXxz7V3ruqC3dP5gP98FxiGLAkfg3SvnLC7Wna-feFnZ_ZeSz6i9KLQ2_97uN8kHfQJnMfP-cSbRjYumZbrmTeZ2MzpsV3FWzuETmw1CRutQE2XkT7pNQeDyqzeFSjhUH_6qo-hAfJo-Z5V_WCfrnyW15Qd77Tw_6tjfutNhKynM1TAmHX3eYwAFh2r2QMup0xKDdbfRPaEYOmdkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودا ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، که از ۹ فروردین در بازداشت به سر می‌برد، به اعدام محکوم شده است.
بر اساس این اطلاعات، شعبه سوم دادگاه انقلاب بندرعباس به ریاست قاضی خواجه‌حسنی، سودا ابراهیمی شمس‌آبادی را با اتهام‌هایی از جمله «توهین به رهبری»، «فعالیت رسانه‌ای و تبلیغی برخلاف امنیت ملی»، «اقدام اطلاعاتی و امنیتی به نفع دولت‌های متخاصم» و «عکسبرداری و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور» به اعدام محکوم کرده است.
دادگاه همچنین او را به دو تا پنج سال حبس، محرومیت از برخی خدمات دولتی و مصادره اموال محکوم کرده است.
حکم اعدام سودا ابراهیمی شمس‌آبادی روز اول شهریور به وکیل او ابلاغ شده است.
بر اساس اطلاعات رسیده، ابراهیمی شمس‌آبادی در جریان دوران بازداشت، به مدت ۲۰ روز در سلول انفرادی نگهداری شده و در دوران بازجویی تحت فشار شدید قرار داشته است. خانواده او در این مدت از محل نگهداری و وضعیتش اطلاعی نداشتند.
قاضی خواجه‌حسنی که این حکم را صادر کرده پیشتر در سال ۱۴۰۲ از سوی مقام‌های قوه قضاییه در زمینه‌هایی از جمله صدور بیشترین احکام و جدیت در انجام کار مورد تقدیر به عنوان قاضی نمونه قرار گرفته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78340" target="_blank">📅 15:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LpEjFW9XCSRc5DK1407XYxLTI6VG6wAYDMSzNma8ONUkzPxQqmP8xuOaX3F-K0E824kBRXvNylSc3GpoPk35JTwBEUsCYVLLIpkvZ2jaZ5LycvplwzWSlKmqtFmu6X42c3goMhHexxsMoL3oh7tpyyBHD5bjvc_KVxf-xKa0tj-i_2bKU2KyuMuXTQvmT89uFjakW8Z3BBGET8ypW6qRqbMS9Ltbfe3BD7gyIDaJw8W1Ph3TKgJABBX6HfkmQUnVVLKwWA4aShTYtWKJolNgyBJqdkrYzqv2lvV1LfGoleqO43m5QrADxXcMIAGv2U1iufcK6DhqZSpqSJc5IrQmmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e-w7jrZQSed09WHRmXBaaeklUB5t0OEIECSOZA59fXDxNbA3uxcifYzVjc2Jan2p9XWtKRXGru6IXrvRwoyaU03AIfqbwxc-law2Vr7L6AfnNvOUi87X0olk2-ptKWwTCtjMi-5CjWbZqktBUMIpYp_cvFJizu520Zgz8HgN22paGeLw783ZKvCIKmEv2lkcb3z_5whphhluFpJ2Dc-ZfMGF0rM60sl9kahPd19bdg_ljvm7r1ZoWdkbFGkCBoTgdXPmC-cqBCYGDDqGUfHR7h_moupwPgi0YscX8PJZ_9_E_LpW9Xj0yYzi2A4cpWAyH6Z2S9Y5GTb3uo6SwelQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tDydxLp8l71PSSbnzePKy5_WXZY9ZXZvqa-50yoBGxkFj9Qqc2BwZRT1YGn_pmcR9R5xAWwtBr7x2tZ4HM7ea4smRWO3sdDPC7eCF3VVzS7fKGKf4UiGSSc4wp1wXkoXWGPiaFPqpKzP8sELVuLtHeA7S5iB2EK1uqOUtTlM_rxE5bjhh-zI6ue6afcvZC1l_OLxJYflr5BE1k_lx2wMEgU_cO-jYxrOOKZ_iMqqhLMUvp8lhZ5mq1xV_JP_h2Bual2JIENGISlVKUdhOfKCMwLEeMAhHzJl6csUgIId_MQ88cb48Rd8HJcrx-4MEu5fKyeeF0opbZyX-86wJZN_Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت انرژی عربستان سعودی روز جمعه ۲۰ شهریور با انتشار بیانیه‌ای اعلام کرد که خط لوله انتقال نفت «شرق-غرب» (واقع در مناطق ریاض و مدینه) صبح پنجشنبه هدف چندین حمله قرار گرفته است.
در این بیانیه آمده است که به دنبال این حملات، عملیات انتقال نفت در خط لوله مذکور به صورت احتیاطی متوقف شد.
این رویداد همچنین منجر به مصدومیت تعدادی از افراد شد که خدمات درمانی و مراقبت‌های پزشکی لازم به آن‌ها ارائه گردید.
@
VahidOOnLine
وزارت خارجه عربستان سعودی اعلام کرد خط لوله نفتی شرق به غرب این کشور با پهپادهایی که از عراق پرتاب شده بودند، هدف حمله قرار گرفت.
وزارت خارجه عربستان سعودی افزود بنا به درخواست نخست‌وزیر عراق، در این مرحله تصمیم گرفته است اقدام تلافی‌جویانه انجام ندهد.
@
VahidOOnLine
خبرگزاری رویترز گزارش کرده که بغداد دستور تعطیلی گذرگاه مرزی شلمچه میان عراق و ایران را صادر کرده است.
دو منبع امنیتی عراقی به این خبرگزاری اعلام کردند که عراق این گذرگاه را به عنوان اقدامی احتیاطی و در پی حمله پهپادی از مبدأ عراق به خط لوله نفت شرق-غرب عربستان سعودی، بسته است.
گذرگاه مرزی شلمچه یکی از مسیرهای زمینی اصلی میان ایران و عراق است.
براساس گزارش‌ها پهپاد شلیک شده به عربستان از استان میسان عراق شلیک شده است. این استان در قسمت جنوب شرقی عراق و هم مرز با ایران است که مرکز اداری آن شهر عماره است.
@
VahidHeadline
رویترز نوشت: به گفته این دو منبع، عملیاتی گسترده برای تعقیب و پیگرد عاملان این حمله به عربستان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyCKVdS6c_cJwiUprNry2vOMmcXcYzA0niXx3ecsSM0m8KrTtzI6-7G3jpO4qF9F6H-tqU4RdgwUPoJUE8l5_EqVGtWFcbFm7PoSlG_sxojXOcg11KEY5xGAAK_tFPMHG4SCfrQq5lV4dr4lL799Eri8vxqlxzPclJQBgIvMNxCRqJ8T3DS605a4efnBmd_iWLiCr1kDYfLQsCZTefhzQtPvrggwtEo3PI2JbjrZEv9MP0A_9h59cyjqNF9bJQ2DV4UO2drAN_Pzlo7fKxavSZAulOIwU_YoHotKJSUqDln8tAzpfoRCLNIh6ajh4J06xH4T5WvMWyTvLOl57b9AOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=V2Dm7dOeorEZ-oh1EU_2HvNphHmsqJDW2ba4ZDAMR0hrBNZxRQ9X-RkFwAGN95ROPR1wFRy0lmvvtrXcCqAjANwbFAfih0eXciyYjEGhN2M4YRdvaoJQ_HDmbKtAmIFXxBrMXQ1j4jQ1N5NuOx7tKWHEn3euSFgH6WecSjCpEKK6_Y-vLnnAVwt8CavW4EdOEcFOtySFOHRmzAwqE2Rvq1UAqHAdfHNjmikr99eAM4AhUEEcDGAbQhx1lLhspzdK1D3nDsEnxwEbqeB5xPxtujwI6tkluw25ow5VBNDvfNbVnl2bDGR9iF9bVJgXzCwCttB6e62UlMUBVBzlUP44Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=V2Dm7dOeorEZ-oh1EU_2HvNphHmsqJDW2ba4ZDAMR0hrBNZxRQ9X-RkFwAGN95ROPR1wFRy0lmvvtrXcCqAjANwbFAfih0eXciyYjEGhN2M4YRdvaoJQ_HDmbKtAmIFXxBrMXQ1j4jQ1N5NuOx7tKWHEn3euSFgH6WecSjCpEKK6_Y-vLnnAVwt8CavW4EdOEcFOtySFOHRmzAwqE2Rvq1UAqHAdfHNjmikr99eAM4AhUEEcDGAbQhx1lLhspzdK1D3nDsEnxwEbqeB5xPxtujwI6tkluw25ow5VBNDvfNbVnl2bDGR9iF9bVJgXzCwCttB6e62UlMUBVBzlUP44Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=s74OVM_yIs1kRUZ_F5qUQnqeL_ODxPUurmsHEkgPfhinCVMfDVdvlAvmMKJZzwlKdtdesu8RoqaWxnUJ1L84Iu_pnBWJLtfS8cDDOPx5cKd0LdkXKnWVy_yInnyZoGwbFA5YPd8CWlgm012Z3lNEsAKvFsUJQ-mTxrbErIiHoicUIluxcvrPN8dwyIeNPPw6gXRVyUEjR32EIXwlfp8NnretBtUxoiqhC3D8ji81iUsXHgmkWp4FFW2HlXLBAQaul2edhwzv5eNflIMLT5NVUKTMwA04z-63liuxBQaIJ-nRshJKEhcS64UxdivjjBH1xw7mrGR4E37uC69l6ON-BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=s74OVM_yIs1kRUZ_F5qUQnqeL_ODxPUurmsHEkgPfhinCVMfDVdvlAvmMKJZzwlKdtdesu8RoqaWxnUJ1L84Iu_pnBWJLtfS8cDDOPx5cKd0LdkXKnWVy_yInnyZoGwbFA5YPd8CWlgm012Z3lNEsAKvFsUJQ-mTxrbErIiHoicUIluxcvrPN8dwyIeNPPw6gXRVyUEjR32EIXwlfp8NnretBtUxoiqhC3D8ji81iUsXHgmkWp4FFW2HlXLBAQaul2edhwzv5eNflIMLT5NVUKTMwA04z-63liuxBQaIJ-nRshJKEhcS64UxdivjjBH1xw7mrGR4E37uC69l6ON-BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LomK2sCF9TkRXpr5fEPOS6OUN2MNq0NL-wNOJ_e7NLrvyPMjy5Op-K5cnORk8eXi9T-ltC_XB7nV2bNlVvaY8CdAmEOiE8d7zMZqTeBtmHcgCrexiHc_NdmQJpycusyW429SHbRNIwep0RLXDaQbcuSYCd6j1hIAc09mE6dcX0JC8Q2uqX_NhL1prAx-LYnnT5T3VOSkj2HlhCmVXxJz2_-RLVGbxeEgg_k5NPTZ7rPO9VRhFKf__B6ciSQrtsidt_IRg_NFRy19ARcB4oWlYS43DvmYEGRkX3iJMmwRxrT9HUbBqZjPs10qBSv__PHqoQwObYEEdZvwUFXOWHEFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گزارش‌های رسانه‌ای مبنی بر آسیب‌دیدن هواپیماهای آمریکایی در جریان حملات موشکی اخیر جمهوری اسلامی به اردن را رد کرد.
او پنج‌شنبه ۱۹ شهریور در مصاحبه با شبکه نیوزنیشن، در پاسخ به سؤالی درباره این گزارش‌ها، گفت: «نه. هیچ خسارتی وارد نشده است. هیچ اتفاقی نیفتاده است.»
کمی قبل از اظهارات ترامپ، شبکه خبری فاکس به نقل از یک مقام ارشد آمریکایی نوشته بود که موشک‌های بالستیک ایرانی در جریان حمله گسترده موشکی سه‌شنبه، ۱۷ شهریور، به هواپیماهای جنگی آمریکا مستقر در اردن، آسیب زده‌اند.
فاکس‌نیوز این خبر را به گزارش جنیفر گریفین، خبرنگار ارشد خود منتشر کرده است.
شبکۀ خبری سی‌بی‌اِس برای نخستین‌بار این موضوع را منتشر کرده بود که در جریان حملات موشکی ایران به پایگاه نیروهای آمریکایی در اردن، «چندین هواپیمای نظامی ایالات متحده، آسیب دیده‌اند».
ارتش اردن روز چهارشنبه ۱۸ شهریورماه با صدور بیانیه‌ای گفته بود که ایران در طول شب قبل، ۲۰ موشک بالستیک به سمت اردن شلیک کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dHNF29hObSGZZWWqXwDEY9-5mPiz57mNtHc4F1aS9dwtbdIYz6uoCa1ir0LpUhPf0de5iFrQJGOzpTZQnrebUrmZYG6Wgh4-e-xRjMY0do1mVf-e4EJU4j4N4RaL2Cj9DWkhTj3TlHcOvkstbqGq1XdnHNRjSWZD4VykcYyO0bWHZpps8UYtNGUe-j7wvxi7k0qqRqE9-mf-n9pRqZEYhqwtyt9M3_0KhH6M8swOj71usINRTX5BXFTAmxDPdjtnTHrrlt7sEyXI7vHgvcNk6bAWsbioEP0bomoePz5NwhXJA6FtifUP0hSFbrXpP8wZiiHKfWZNq18MCJSC3DR6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت آمریکایی «آنتروپیک» اعلام کرده است که سه عملیات مرتبط با حکومت ایران را شناسایی و مختل کرده که در آن‌ها از مدل هوش مصنوعی «کلود» برای تولید و انتشار محتوای تبلیغاتی، طراحی سامانه‌های نظارتی و تهیه اطلاعات مرتبط با هدف‌گیری نیروهای دریایی آمریکا استفاده شده است.
این شرکت روز پنج‌شنبه ۱۹ شهریور در تازه‌ترین گزارش اطلاعات تهدید خود، مجموعه‌ای از موارد سوءاستفاده از مدل‌های هوش مصنوعی آنتروپیک را تشریح کرد. این گزارش فعالیت‌های شناسایی‌شده و مختل‌شده از دسامبر ۲۰۲۵ تا اوت ۲۰۲۶ را پوشش می‌دهد و علاوه بر ایران، مواردی مرتبط با چین، روسیه و کشورهای دیگر را نیز بررسی کرده است.
بر اساس این گزارش، آنتروپیک حساب‌هایی را شناسایی و مسدود کرده که از «کلود» برای اجرای عملیات نفوذ با هدف تاثیرگذاری بر افکار عمومی استفاده می‌کردند. سه مورد از این عملیات به عوامل همسو با حکومت جمهوری اسلامی مرتبط بوده است.
آنتروپیک می‌گوید هر یک از این عملیات از سوی فرد یا مجموعه‌ای انجام شده که یا مستقیما در یک نهاد تبلیغاتی حکومتی ایران فعالیت داشته یا به نمایندگی از چنین نهادی کار می‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78331" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzqcQMbhPYXh3TalTuUba2x68q3ayFO6XA-uSBriGJScaBnNP6Spn9AfpCYALeurO3Y93beJh_zW-FmtoMMgG7bYZ1CpamOmSTg8ARS2AmS4-Zv8Vu2miUeIxJvJICGeLQ1_88uw4ny2d0Oud9is6QNgExMHkaH0xkzL_QPDvnzs6FesXwknqAbuAabq8JxtNY9ifanDoyQXaL-2mpGY4Qlpe_mY8dfsT5lfbegCagsz33ddpNJqB5XqiigvxC2tVwIQ9LSeccdkR4G159htGUzf3TICZrdAImJlpsEazEw9bjeYMVCWHgYJKZAEEAeZ_90pea0PRO-TtUZcMgeUpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت مخابرات ایران با انتشار اطلاعیه‌ای در سامانه کدال (سامانه اطلاعات جامع شرکت‌های پذیرفته شده فهرست شده در بورس) اعلام کرد هزینه مکالمه تلفن ثابت با تلفن‌های همراه از روز جمعه ۲۰ شهریور ۴۵ درصد افزایش می‌یابد.
به گزارش انتخاب، بر اساس این اطلاعیه، سقف هزینه مکالمه تلفن ثابت با تلفن همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش یافته است. این تغییر در پی ابلاغ دستورالعمل افزایش هزینه تماس تلفن ثابت با تلفن همراه، تماس میان تلفن‌های همراه و پیامک اعمال می‌شود.
شرکت مخابرات ایران اعلام کرد میزان دقیق تاثیر این افزایش بر درآمد شرکت هنوز مشخص نیست و آثار مالی آن در گزارش‌های دوره‌ای منتشر خواهد شد.
این شرکت در خردادماه نیز هزینه ثابت ماهانه تلفن ثابت را ۴۵ درصد افزایش داده بود. هزینه ثابت ماهانه مشترکان خانگی در تهران و کلان‌شهرها به ۴۳ هزار و ۵۰۰ تومان، در مراکز استان‌ها به ۳۲ هزار و ۶۲۵ تومان و در سایر شهرها به ۲۴ هزار و ۶۵۰ تومان رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78330" target="_blank">📅 17:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=cuAhbN8JRLh8wySyBk2Q6sZxSLqSnbTBVfWGyo98W12uP9AqnpbzauzppZjo-GNI0brA-bZl6KcARV7RHJLlaxf6OqBwtGEWA2aFwc2v95_FTbYWtZhTK_-DNNnk9HgAL3nZoVPOw-ORVAM2awmDGqZcQ16hzAVKkQog_dRh1UHhtGMfdcKMT0T-YwV0J0Rpsd7KE0thVyy01v1uXALkVBj0WF57azbjpcYVSv0voIUcvygz2RRLW9A41en3IMCzCqiZartdc3e-0KiJ1d4Vm4wG26IMXvIpR-ji7FhGRtRjG-9tGKtRV_gtb-TCWfNj2BBliPSICHMa5Oh9BcDn0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=cuAhbN8JRLh8wySyBk2Q6sZxSLqSnbTBVfWGyo98W12uP9AqnpbzauzppZjo-GNI0brA-bZl6KcARV7RHJLlaxf6OqBwtGEWA2aFwc2v95_FTbYWtZhTK_-DNNnk9HgAL3nZoVPOw-ORVAM2awmDGqZcQ16hzAVKkQog_dRh1UHhtGMfdcKMT0T-YwV0J0Rpsd7KE0thVyy01v1uXALkVBj0WF57azbjpcYVSv0voIUcvygz2RRLW9A41en3IMCzCqiZartdc3e-0KiJ1d4Vm4wG26IMXvIpR-ji7FhGRtRjG-9tGKtRV_gtb-TCWfNj2BBliPSICHMa5Oh9BcDn0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.  بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی…</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78329" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78328" target="_blank">📅 07:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-fXFNUj37OaiduHUZE6QgmCKZu_FMfml1fi6QT6qD9xwk58COR5mMBZlZjd7Ht5GOZyZxuFLBRSpq1dZ4Ezp360Lw5U_J1G5xsXtVrrOgoGTrdB9iIRwXXd9Pi_vJx8thV2hWK1XjMjAsXxbCoK23eUDuATwvtf5shU32wRVryx3ds7GNHnQxAZclsoC4UlzY3Mn3huefZdwo1W1srknV5rjbtq_UmYBq4RBhQaDi5edSBR4NPXJ9YsJI-i8oycR3h5Ozg9M4m3kHigZ-Jrwu0DQ9xHOLXbRHHvRKQxmFbUm9ndGH215B7m_yrKYCiQt3-ya36_fkM8IBM5AJDqFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا در دومین شب گردهمایی انتخاباتی میان‌دوره‌ای جمهوری‌خواهان که در دالاس در حال برگزاری است، بار دیگر، تنگه هرمز را «تنگه ترامپ» خواند و گفت «ما تنگه ترامپ را کنترل می‌کنیم». رئیس‌جمهوری آمریکا بار دیگر تاکید کرد که هرگز نمی‌توانیم به ایران اجازه دهیم سلاح هسته ای داشته باشد و نخواهد داشت. او گفت که ایران در حال عقب‌نشینی از همه جا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78327" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0HxB8BNbv0Ggqyv54EHh-q-gfqC1LsQ3sSZTFkCyUoKYp4ZrvxpqFz0bDp34_qOwQKXvzyIyaffCqCx6S_NhEtByuW_OzBkDyznu7bJ5Ky3iDw99WvVmJyx8Z_KvjPozjubQYoS9-lCbCcPhDJZfpJrsYN5y2U-yH8oZlzbWjC7o4P2XdBsTA6y0zvcnJ5XuK5bnmIH_-421HhKCd9mqraCaEZSuHw4NHN5JsmO1jRe6mDPz12lAgObRAc4gC00Vl0U8xXBMe91qCY7FS-QfP1Lw7vd3khBHHAfkHP93Qe350iLIHI79Cv2aIpqVpwJV_YNvfmuP_0hT_WZd_O2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، به اپک تایمز گفت نیروهای جمهوری اسلامی خسارت گسترده‌ای به پایگاه پشتیبانی نیروی دریایی آمریکا در بحرین، محل استقرار ناوگان پنجم این کشور، وارد کرده‌اند.
کائو در توضیح استقرار اخیر ناو هواپیمابر یواس‌اس آبراهام لینکلن و الزامات لجستیکی عملیات طولانی‌مدت گفت خسارت واردشده به پایگاه بحرین بر امکان پشتیبانی از این ناو تاثیر گذاشته است.
او گفت: «خدمه این ناو جایی برای پهلو گرفتن نداشتند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78326" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7iFPIYZAWwHX59wLXee524-qLR0GW_jkzuUe-pYtOAzFxtiEP535dxm6XncccR0WZVmoLHi-TJxt_VRgS6vXaKNBsY0fUhRfFOSJd_ubDoade2Vs1ijOl18O0_Ttmpj-Yas8DvC6CA8Yx4hoXjfZrDXlfl-MH3yENzRlRIZcGWjcvaPiGlSrijSm25tOVAg3N52upe1EgTi6D97n4PF115JKEJaAT1zTgbID2gLNhsg_uQDnPbTlFg6cX7RCGNmWRdB7EluEfVN28xSiWN9Z2IjzyRG-5JkY0XIJHdEcF6o-4E7YMFOMngWtw8TYFlPZlAxaHs0fq31MLYCfDd-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت پنج‌شنبه ۱۹ شهریور هم‌زمان با تشدید درگیری‌ها در منطقه و افزایش نگرانی‌ها درباره اختلال در عرضه انرژی، بیش از شش درصد جهش کرد و نفت برنت به ۱۰۷ دلار و ۶۳ سنت در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت نیز از مرز ۱۰۰ دلار عبور کرد.
بر اساس داده‌های اویل‌پرایس، قیمت نفت موربان با بیش از پنج درصد افزایش به ۱۲۲ دلار و ۴۸ سنت رسید و سبد نفتی اوپک نیز با بیش از چهار درصد افزایش، ۱۱۲ دلار و ۲۵ سنت قیمت‌گذاری شد.
افزایش قیمت‌ها پس از حملات به نفتکش‌ها در خلیج فارس و دریای عمان و پیشروی حوثی‌ها در سواحل دریای سرخ رخ داد. رویترز گزارش داد تصرف بندر مخا و پیشروی حوثی‌ها به سوی جزایر حنیش، نگرانی‌ها درباره امنیت تنگه باب‌المندب و مسیر صادرات نفت عربستان سعودی را افزایش داده است.
هم‌زمان، تردد کشتی‌ها از تنگه هرمز به‌شدت کاهش یافته و داده‌های اولیه نشان می‌دهد ۱۸ شهریور تنها هفت کشتی از این آبراه عبور کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78325" target="_blank">📅 03:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=dir4eqCbcOvH0jjnCPrhg4qUOVQsa4OH0uNqeQJf9PTgBLAcu_4Lm_SzE73Gkp3zipqBbrdmA3H1hlrovpYeNe4KP3XnkNfZ5aPYvddiM6abCPiz793XBhr2PMIs4b5Cd3E_RhnIgczcxSWFGyuE-1vyYIu5Vm1xcibsXjr50mCs-g43fNWXwiKJGEnOVrCdaeasVH_t3ir1nn4Wb_fNxH9dq7lhTCiV3johiRwDFmRDmrI4Fejv14QkqDj1NaS0SfyeZHuCJnko0U2tiVmOWdCC4mtvtcUMFPV5zowWkrlgJ7mxGnym6zxt0xOqTZgvwwUh93Rp26cFh0P1FjVKDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=dir4eqCbcOvH0jjnCPrhg4qUOVQsa4OH0uNqeQJf9PTgBLAcu_4Lm_SzE73Gkp3zipqBbrdmA3H1hlrovpYeNe4KP3XnkNfZ5aPYvddiM6abCPiz793XBhr2PMIs4b5Cd3E_RhnIgczcxSWFGyuE-1vyYIu5Vm1xcibsXjr50mCs-g43fNWXwiKJGEnOVrCdaeasVH_t3ir1nn4Wb_fNxH9dq7lhTCiV3johiRwDFmRDmrI4Fejv14QkqDj1NaS0SfyeZHuCJnko0U2tiVmOWdCC4mtvtcUMFPV5zowWkrlgJ7mxGnym6zxt0xOqTZgvwwUh93Rp26cFh0P1FjVKDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی در شبکه اجتماعی ایکس نوشت
:
امشب بزرگ‌ترین پایگاه ایران در خارج از ایران، یعنی تونل‌های علی‌الطاهر در لبنان را نابود کردیم. در حال تکمیل مأموریت هستیم. سال نو مبارک!
پیش‌تر ارتش اسرائیل اعلام کرد شبکه تونلی حزب‌الله در ارتفاعات علی‌الطاهر را با استفاده از بیش از هزار و ۱۰۰ تن مواد منفجره تخریب کرده است.
به گفته ارتش، در این تونل‌ها که طول آن‌ها بیش از دو کیلومتر اعلام شده، ده‌ها موشک، راکت، پهپاد، سلاح‌های سبک، موشک‌های ضدزره، صدها مین و مقادیر زیادی مواد منفجره کشف شده است.
بر اساس اعلام ارتش اسرائیل، با انهدام این سایت، عملیات تخریب شبکه‌ای متشکل از هشت تونل به طول مجموع ۵٫۴ کیلومتر در منطقه علی‌الطاهر و قلعه شقیف تکمیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78324" target="_blank">📅 01:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tbweF43UUvJvOGJamUA75AGCgYofT-ejUQxJynjR-J1VNe_Ehqk1v3JK6FyxFaHF-zVsFgadSi7wjBcnLZGE5W908mFYx7szfO1nujz1rpra8_fALMo2N-Igy3h0O3UTnJXZcaNTga0f3nS_J9KYcbv4558-glaImjQVtS8xkMnAyb8D2BPRzTD6CgP-T4C0Ah0Eug8p5EGK1iehqFPQyQUvz4mgt6SOvUS_5vvxXbI35kFZXyqwVCUFtMoEMMxvKF3oLDre0ipFtgiN02bfdnhRsLKtiLeYy_1qZ5V2hULaWvZT6DiAo2xULG5MJeMjj9cAnD_vKbuHCiOa-dP9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا، یوکی‌ام‌تی‌او، عصر پنج‌شنبه به وقت واشنگتن از برخورد چند «پرتابه» به دو شناور در نزدیکی سواحل عمان خبر داد.
بر اساس این گزارش، این برخوردها در فاصله چهار مایل دریایی غرب شهر خصب، در استان مسندم عمان، روی داده است.
طبق این گزارش، کاپیتان یک شناور اعلام کرد که شاهد آن بود که چهار پرتابه نامشخص به دو شناور نامشخص اصابت کردند.
در پی این اصابت‌ها، یکی از شناورها دچار آتش‌سوزی شد و از وضعیت شناور دوم اطلاعی در دست نیست.
مقامات عمانی در حال بررسی این واقعه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78323" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=Jc0h2XMr8lIUUBndsXqNg2cbZTUkoCMTl4Illb1MgLi6-IlUiao7ugY8WwmbDe0xzZyegeXuOii2-x8HeJsZqEnjjTz_-k4BUoduOtnqFxaHyPmBGhf5mB_xq2GybDKv8s2keBB2ICxvXEZ-uehhZuPr0JLEC96qNzOntdDFl0UUNAyF8Q_XzJJbnK-3yWjaPEzEsiLzvQfcK6VjCUp2k3SpTRITZ9hhRCI3IJ9vKsQKv-YpcM2nmsZIHhg6fXiZ4WZSlLdSOSCM2Tm649Pk1SUmFmlCZ5Ob2Pc5oZYUGN4fU-0aBxTGCaZgJu8dwrm-bYou77GrlHrl-mWzNqKwZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=Jc0h2XMr8lIUUBndsXqNg2cbZTUkoCMTl4Illb1MgLi6-IlUiao7ugY8WwmbDe0xzZyegeXuOii2-x8HeJsZqEnjjTz_-k4BUoduOtnqFxaHyPmBGhf5mB_xq2GybDKv8s2keBB2ICxvXEZ-uehhZuPr0JLEC96qNzOntdDFl0UUNAyF8Q_XzJJbnK-3yWjaPEzEsiLzvQfcK6VjCUp2k3SpTRITZ9hhRCI3IJ9vKsQKv-YpcM2nmsZIHhg6fXiZ4WZSlLdSOSCM2Tm649Pk1SUmFmlCZ5Ob2Pc5oZYUGN4fU-0aBxTGCaZgJu8dwrm-bYou77GrlHrl-mWzNqKwZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز پنجشنبه ۱۹ شهریورماه تصاویری منتشر کرد که به گفته این نیرو، هدف قرار دادن یک شناور بدون‌سرنشین آمریکایی در ورودی تنگه هرمز را نشان می‌دهد. سپاه اعلام کرد این شناور با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون» بوده است.
علی عظمایی، فرمانده نیروی دریایی سپاه پاسداران، گفت این شناور بدون‌سرنشین «جاسوسی» متعلق به ارتش آمریکا در تنگه هرمز مورد اصابت قرار گرفته است. او همچنین گفت: «تنگه هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست و هرگونه تحرک خصمانه مورد هدف قرار می‌گیرد.»
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد ارتش آمریکا طی روزهای گذشته شناورهای بدون‌سرنشین خود را به تنگه هرمز اعزام کرده است. مقام‌های آمریکایی تاکنون درباره این گزارش اظهارنظری نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78322" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nj7gEPN8F0g-URriX2yp5mfvFy1nRpC3LhHjSuhR5bP-BErV8gaf5EwCd7IExGXdL69gao_zlu6npaYuIUwzyj6CIJ2PFd1JGzaWTgw5_0Ob2UIjONvXDPOg83uTxsqNmRWMqQBAPkBwLoMLUQJNe17-xnsDRvyGzwCYdrsQ7AvmhGN8MzwraZcphrjlD3VFMS9AZhgtmSNIw1Qy5afu39Ltp6d51h5ispky4PFH6nyzsuMSc8RnciNhBPwTVxKFXuz-DcBfJHMJFvCcRrhKnpYwhmfWYhb9nFM_CX4trsa1IFdLXCUT_ocZvSgc3WTeAgDfdfUlfcy8uCfpq9wR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
