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
<img src="https://cdn4.telesco.pe/file/Y_9jYxvmFl1znpbbK4uJLDO-WndKTwTstP8Bl8JSfUfFrClFjrnbuJ7zcHS-_wuX10r5E-YAaJVFpMRZIwx6N1N7xxiQtjqDs5LO_f8OEDpmQzAOQVTriLv9fIxRaG6pd0YAIlU_7XZGw2NmHzJyz5be7W4XLZpPK-qCp3MAIJUuho-j15cpyfKKtkqOfKzyV3o9sGd_a7vzkIueNvF5NsDmQ9wVW3Ki3bbBm2Vizu6RSap1VePe79ro03wIlEB5Vas0b1Ez35LBimoNguU40rQA_uaGd2syZg2Qzrr5kESi5WlFHYOdIm1kcoA_kTKvzZoSSnXQlJU2iJDgMqGrhQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 339K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 22:37:13</div>
<hr>

<div class="tg-post" id="msg-16462">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ در تروث : اروپا دارد یاد می‌گیرد که وقتی مجرمان جهان سومی را در خود جای می‌دهد، خودش تبدیل به یک کشور جهان سومی می‌شود. این اتفاق خیلی سریع می‌افتد، فقط در یک چشم به هم زدن. من درست به موقع انتخاب شدم!!!
@withyashar</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/withyashar/16462" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16461">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فردا عصر کابینه امنیتی اسرائیل یک نشست
ویژه برگزار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/withyashar/16461" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16460">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رئیس‌جمهور عراق:
عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران
@withyashar</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/withyashar/16460" target="_blank">📅 21:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16459">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نتانیاهو ۲۵۰ سالگی استقلال آمریکا را به ترامپ تبریک گفت و گفت:
«ممکن است ما در قاره‌های مختلف زندگی کنیم، اما به دلیل سرنوشت مشترکمان، به شدت به هم متصل هستیم. آمریکا بزرگترین نیروی آزادی‌خواهی بوده است که جهان مدرن به خود دیده است. اسرائیل مفتخر است که در کنار آن بایستد. زیرا اتحاد ما نه تنها بر اساس منافع مشترک، بلکه بر اساس ارزش‌های مشترک بنا شده است. امروز، این ارزش‌ها مورد حمله قرار گرفته‌اند. مستبدانی که با آنها روبرو هستیم، شعار مرگ بر آمریکا، مرگ بر اسرائیل سر می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/16459" target="_blank">📅 21:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16458">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Bitcoin +63,100
🆙
@withyashar</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/withyashar/16458" target="_blank">📅 21:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16457">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش انفجار شدید در سلیمانیه عراق
@withyashar
🚨</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/withyashar/16457" target="_blank">📅 20:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16456">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">العربیه : ارتش اسرائیل شنبه 13 تیر با انجام چهار عملیات جداگانه، اقدام به تخریب گسترده خانه‌ها و مجتمع‌های مسکونی در مناطق شرقی و شمال شرقی شهر خان‌یونس کرد.
@withyashar</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/16456" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16455">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده  - ممکنه همین هفتهٔ آینده این دیدار انجام بشه @withyashar</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/withyashar/16455" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16454">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ به آکسیوس : ایرانی‌ها برای امضای توافق تقلا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/16454" target="_blank">📅 20:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16453">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده
- ممکنه همین هفتهٔ آینده این دیدار انجام بشه
@withyashar</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/withyashar/16453" target="_blank">📅 20:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16452">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ به اکسیوس : "از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند."
@withyashar</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/16452" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16451">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ به آکسیوس : هیچ یک از طرفین در طول مراسم تشییع خامنه‌ای، به سمت دیگری شلیک نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/withyashar/16451" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16450">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ به آکسیوس:«همه آن‌ها آنجا هستند. یک گلوله می‌توانیم همه آن‌ها را از بین ببریم ، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@withyashar</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/16450" target="_blank">📅 20:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16449">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد @withyashar</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/16449" target="_blank">📅 20:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16448">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECYQWsnKOg39QdR02Vcrlx-THOJQBZH_jGLpmWJtmN8fhdeFVJwZLAG0xBGpTOygYSKOKppbwUyGugMKFV6qFavyWaGxthRxmoWMhH_3jVQuszx-M-4IPv0mQAj7hv9ayik3jLXFZXPLgdBdZf1OsbytYxaVyM7DxJgTKPvwAHu_2TdyGTiMaJT0o88wvpYX_BKyu3haSiEeB5Lf4KReiS6TJ06cvQFq1xQBWEym3JPg_krQCPEyaAHaVqft11zRI-oIrugeUF47urzfXiawimWspSSEWITKLBuqQiHHYXqRkf0TF2a5-AquKCtkwMQLn6yBHJwoDW_1NMiuORkeEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای…..
@withyashar
😂</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/16448" target="_blank">📅 20:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16447">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJUeHTpvuGJGNULg5Q8q40YSSmsefQTDEmnpws8wSWisEPqRz254906km0yWPk1E54_gMrNmuHDe1EkP529yVR7lmxDHnqKMm-FT-b9OkBD2yLX7dHBE5ygq6a74t0uBJGIRjpfYqoPjsE3h9qpACrqdJJcbOsKwiJDHdb05xl778UjpoGS8hX0zxuS4E7tqe9AXas-z9zHrnPiIV68FKqIL5lkca4_IUHp_gO42O4X3xKWJxfZmxeAjTaxs6tGxLEUUBxcEhugBYz2Q2QTdHen_-zu1GLyaea1jVwSIIUXz6qPZeG__5QVFMe4fGD9tTVDk8Lf5mxD25zfeOkiYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد جهانی علی خامنه ای
بیشترین فاصله زمان مرگ تا زمان خاکسپاری رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که علی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ ثبت کرد
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/16447" target="_blank">📅 19:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16446">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است. از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/16446" target="_blank">📅 18:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16445">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند. @withyashar</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/16445" target="_blank">📅 18:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16444">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8xaE79NXJZGaB_rCEHcHZfz5NrCw1njOBWjFS_UWz_JvEIHelu69Y9AaBR-581V8bTUQqqpoqyH1Nvgt5g0BwAGFfP79xOHd6bEnN6tKRla7aSAVi5Ho57wuRrZeM8SaqU4loiK_Nr2Hovdxjjm5KKbGzUCaQcz-VtYRfu-srKLhWanu4wjPuHmrGjaF2gho0bUdFNA7DlUyk78PqgB_Inwrn1BbKCfGZgp5z008ZNsSH4-qfd4S-wIpUnNqu5rNQZE8Mr38aW4COmGKnQtaXJMCGVIA7IQzTmhkpKZESLk9R1bjXczCqmk5LT3gvPAumUS0DwLJgpXqRiy4mC5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشریه نظامی «میلیتاری واچ» نوشت: کارخانه هواپیماسازی کومسومولسک-نا-آمور روسیه
تولید ۲۰ فروند جنگنده سوخو-۳۵ سفارش داده‌شده توسط نیروی هوایی ایران را به پایان رسانده است.
وزارت دفاع ایران در حال حاضر هزینه نگهداری و پشتیبانی این جنگنده‌ها را در داخل روسیه پرداخت می‌کند تا پیش از انتقال به ایران، در روسیه نگهداری شوند
احتمال دارد نخستین سوخو-۳۵ها از پایان سال ۲۰۲۶ وارد ایران شوند؛ آسیب‌دیدگی زیرساخت‌های پایگاه هوایی همدان یکی از عوامل اصلی تأخیر در انتقال است.
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/16444" target="_blank">📅 18:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16443">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/16443" target="_blank">📅 17:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16442">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نیویورک‌تایمز به نقل از منابعی در سپاه:
مجتبی خامنه‌ای خواهان حضور در مراسم خاکسپاری پدرش در مشهد و اقامه نماز میته، اما مقام‌های امنیتی تاکنون با این درخواست مخالفت کردن.
به گفته این منابع، نگرانی از احتمال سوءاستفاده اسرائیل برای ترور یا شناسایی محل اختفای اون، دلیل این مخالفته.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16442" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16441">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b97Y8aWNmf57yt_kJS7HpT6QuwVKz9N5DIavHrdwZoIgFRJDO7jQ8wtZHQvHhfNGtcr-WaB-4NqjkM0D4oB00DT6LpKLoH4xf0cBOHrngQQaKhQk2KNIsrQJZVs9YeX7PSdy32hgYXK4IDUM6KlrwW0OgS5YqNsfsg-vMy9GuDLEbP5IpSxqkzEBoamYswR83N39CFdJGUif9nHQdjDOmiq0gY-LODSMuYVNbwoOO7aoolz5dwXVKCcHESdV2aylchBa4laKXGbDKm2rYuE6aC3dmu5FiXCZQb-ml47nBQwRKeVsgFiTD-hxcMuqMSabxpVkShFZpM3lQ25IB_UgFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار علی عظمایی امروز به عنوان فرمانده جدید نیروی دریایی سپاه معرفی شد.
فرمانده قبلی سردار تنگسیری بود که توی جنگ کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/16441" target="_blank">📅 15:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16440">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نیویورک‌تایمز:  عبدالناصر همتی به مجتبی اطلاع داد که در صورت تداوم محاصره دریایی، ذخایر مواد غذایی و دارویی تا پایان ماه اوت به اتمام خواهد رسید.
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/16440" target="_blank">📅 15:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16439">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=EHyEmEY75bUKbheAotGMaSOIkYwjjpSP8U6Sq3oFut9OycEzQ35H3Ed0UPnnNMbD5BLu5Vgg6LL7SbvgZHvfcxCAuWIivw3Gs_mfWAUoWSAnS4lAcTbpxBWK4ZiXORYV1KcZqMweTRdYW5T1PxFqWVJ37HldKYSOT4ma0sybuw3YV7Ms_sZmKn2CT_nzqvnJJRR3msjtC_gfABPOyViyEtDRgGxQRQwUBE7r3V5MEXiXwUeANIPqrUDjMjdqAb1H2ADpGBnfS1nO3zYrXc2H2OSEHPKDVR2C_I-lCm-qTRPXfuTaUIoWVmeuT9-BrZWa2fo72ImP_KavCwAEbrEzkJtTvm_iUj-UYehhK_4Jfy4wbtT2VgOfN6lTU1hm7SW0DpX52ygmzBPaN2q6DBhwFqGq15a4NEAmCr_TqX3ijRjRlKEh2EpWg4fYPYw_XyW2wfz4_ymDVrfbcw1Nlx0cV8HOUwJ4ZG8QmVzULDpXB8i0uanlIm0h8pa5eDhBNEAFXjKwCxXW-Xa1twa1KHasnsksD6-BRr3w5aPIPmxKwlHDCZxhmORrycx4YHV7lo3S0488KS0yJiYw5khp0AkHcId72scfNRY4gpWXyAXgr7luuI44npgzPRPRjkplMpTSSu1klw1td-rKDuCLVsS5HjL-pm1V0p36N29QUiq7JxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=EHyEmEY75bUKbheAotGMaSOIkYwjjpSP8U6Sq3oFut9OycEzQ35H3Ed0UPnnNMbD5BLu5Vgg6LL7SbvgZHvfcxCAuWIivw3Gs_mfWAUoWSAnS4lAcTbpxBWK4ZiXORYV1KcZqMweTRdYW5T1PxFqWVJ37HldKYSOT4ma0sybuw3YV7Ms_sZmKn2CT_nzqvnJJRR3msjtC_gfABPOyViyEtDRgGxQRQwUBE7r3V5MEXiXwUeANIPqrUDjMjdqAb1H2ADpGBnfS1nO3zYrXc2H2OSEHPKDVR2C_I-lCm-qTRPXfuTaUIoWVmeuT9-BrZWa2fo72ImP_KavCwAEbrEzkJtTvm_iUj-UYehhK_4Jfy4wbtT2VgOfN6lTU1hm7SW0DpX52ygmzBPaN2q6DBhwFqGq15a4NEAmCr_TqX3ijRjRlKEh2EpWg4fYPYw_XyW2wfz4_ymDVrfbcw1Nlx0cV8HOUwJ4ZG8QmVzULDpXB8i0uanlIm0h8pa5eDhBNEAFXjKwCxXW-Xa1twa1KHasnsksD6-BRr3w5aPIPmxKwlHDCZxhmORrycx4YHV7lo3S0488KS0yJiYw5khp0AkHcId72scfNRY4gpWXyAXgr7luuI44npgzPRPRjkplMpTSSu1klw1td-rKDuCLVsS5HjL-pm1V0p36N29QUiq7JxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت نیکسون در ‌تهران ۱۹۷۲
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16439" target="_blank">📅 14:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16438">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDOT5xqGrx6_6aIQT9d0aHwVViAmQVVLrvHMz9Zd60XgwsD_4PSZQcqCTeVGK-PQh0JJeGM4FAVADkL3TXSDwlgd6L6kHIlX9elLJYd-t-OEI5GgNqtbhHum5-PlitPS2iRkjRRsO0Py4PU4WS9g6F5md6ybHPjVEt8mbx4BamMtHXGw8_oOcdDpNW7EWv5VCJPgZ5_4wX2e1jVnu7xmWZPV0wt5IS03bH-Ihtz7-nTLuu-SFGNBEg9lD36678kLL841jGfJ_JH8T_xb83SOt_fa9Vme8FpvMEFB1UVNZCTnB6_mn66XM5BTCzO3TJZkrKPo789K2f8KzmcKElwB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16438" target="_blank">📅 13:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16437">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DefKqHIRss-mDqL16Az75XTg88fdQUgKusF3rySHcVNHgOlni5LAx6-3o8PrfqXiq_pehtX9Ew926ME6JcIs05RwRNt6SGWwjvrXW647b77L8k7XxnVdqgyCohoHu_tPwknZ16qAciocsVy7D_4P6spo6to7CRee9I_w0zms8PjKmooYSMxouTMFWfQ7Qc5KCBQBofuozeGQfkkFFKqi1IyI7ekUklndvpmt1J-c7hO1fLT7BrgUa1QKQhbJlvT_fm41ZjsanQTA4OIZqeWTsWqkw3vEmYO2AE7t9NU43IP7Ntn3ZdtKQbJK_nfkjQSpoEn7L1_QpE2HLU1M_lP-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان درست شد ، عباس مکار و ممباقر نره
@withyashar
😂</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/16437" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16436">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSDAociZJEPOSMHE1LN4mhd4eqaw0yw4IQ66m9t7YvXH9iFGb4Q_KOdwSgQixxvPe5gsEhMEJC_Gmorm5K_hiqC4kqKf8-C8HntJ5lVmQvo7lsyLK3C3eVftjvRs2_CF8f2OvjnOwKM57CUYwC9V3Z7s76bMlyFwTGwD-CFm3fmeLT8OFRUWkXtkE8Br7lg9OE-c67e3Q23e3hD3xWDfzIPQFb4Ol7jTplBTG-aii3KgTQUaYwieZ1Mn9M6NSxSRBBCHfVjthy06SsjAUs0DpgASLFtpqwcrF3_scIO2RgpcK6SMv5tOnYvWmBe3cSj5RNYl-lfYSxqXMWsJQLju9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره حمله اسرائیل به لبنان
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16436" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16435">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwYnlfD9wImvOnqwFCtfmpeoAjaMTgIrC2bn_QerlYR9CGJwxGtom1zNBI1zIYrlnXzmn9jx7pp2cFL_HnlB3O0CRrKHn1k5bEslXfKlmXAqNVT60ErfNDLyyxJk-bSmSQzlmCoDaf_9nANHhwgKqOoL54UyIfo_Qb_ICZ8Cqdkk9cMyzhVjCcbZtb5IXWzDGUbuY_HMJg2yIXrpugBsu0VnS7SLasH0iaGG30x2st_2DVnpKYK9QtnKm5P1NYL20rwqtJPAT_N6MZN4IMNYH2bMoN9VnduM9UY62S0Ngd2iUd-Xa0wwidsogdGzRBn2cBmt6jd3F11PPrL-eJAi1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : سری جدید ۱٠٠ دلاری با امضای ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16435" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16434">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">افزایش تولید نفت اوپک با بازگشایی تنگه هرمز
طبق یافته‌های نظرسنجی بلومبرگ، تولید نفت خام اوپک طی ماه میلادی گذشته با ازسرگیری صادرات تولیدکنندگان خلیج فارس از طریق تنگه هرمز در بحبوحه تفاهم‌نامه ایران و آمریکا، افزایش یافت.
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/16434" target="_blank">📅 11:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ان‌بی‌سی نیوز به نقل از چند منبع آگاه:
آیت الله سید مجتبی خامنه‌ای احتمالا در مراسم خاکسپاری آیت الله علی خامنه‌ای حضور نخواهد داشت، چون در حمله آغاز جنگ به‌شدت مجروح و چندین بار تحت عمل جراحی قرار گرفته!
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/16433" target="_blank">📅 11:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کانال ۱۴ اسرائیل : حسام حسن، سرمربی تیم ملی مصر که اولین پیروزی تاریخ این تیم را در مرحله حذفی کسب کرد و به مرحله یک‌هشتم نهایی جام جهانی 2026 صعود کرد (در مقابل آرژانتین)، از این فرصت برای ابراز اعتراض سیاسی استفاده کرد و پیروزی را به مردم نوار غزه تقدیم کرد: "امیدوارم خداوند پیروزی را به آنها عطا کند."
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/16432" target="_blank">📅 11:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیکلاس لیساک فعال رسانه‌ای نوشت:
"یک منبع موثق می‌گوید مجتبی خامنه‌ای در اواخر ماه مارس، پس از آنکه بر اثر جراحات ناشی از حمله هوایی‌ای که پدرش را کشت به کما رفت، جان باخت.
او هرگز نفهمید که رهبر جمهوری اسلامی شده است.
قالیباف و سپاه اکنون در جست‌وجوی افرادی با شباهت ظاهری (بدل) هستند تا آن‌ها را در انظار عمومی به‌کار گیرند."
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/16431" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">منابع اسرائیلی به «کانال 15»اسرائیل اطلاع دادند بنیامین نتانیاهو، در انتظار چراغ سبز ترامپ، برای تصرف پایگاه «حزب‌الله» در ارتفاعات منطقه «علی الطاهر» در جنوب لبنان است.ترامپ از نتانیاهو خواسته تا زمانی که مذاکرات با ایران ادامه دارد، این عملیات را به تعویق بیندازد. برآورد ارتش اسرائیل، بین 30 تا 40 نفر از نیروهای یگان «بدر» وابسته به حزب‌الله، از جمله شماری از فرماندهان این گروه، در داخل این پایگاه گرفتار شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16430" target="_blank">📅 10:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16429">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/16429" target="_blank">📅 10:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16428">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم @withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/16428" target="_blank">📅 10:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16427">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=rfcA-mJ5pvXvrvMq__i-EU5XYXx1T6RL686pzwoWdrU5AIYqzlmfRUQxEQD83iJfn5_e1xnx1QhTKljHNrbA21OPNVEbX0wpDf002e3DPxKsYDh5B6qTStWOCKG-5X832FyE3D-kXugGWHWBdd1JMHhE7SqyAcuXhNB8oJ69r0jI6El_SdidCwgTk0pQBSO65mUwCCBLvYLLWOVB9JiE0rJK332yOLRMsdt6zncIMWFHMgjC5d2GXX9Iziy7i1oVwo3hLWdvmqOahCjlRT6_3yj7XEwQ2RtEyTwqQh-XdHHTtpruVyLbAmcH-9-YL8jTpdDuj6zLemAvSzquU42GkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=rfcA-mJ5pvXvrvMq__i-EU5XYXx1T6RL686pzwoWdrU5AIYqzlmfRUQxEQD83iJfn5_e1xnx1QhTKljHNrbA21OPNVEbX0wpDf002e3DPxKsYDh5B6qTStWOCKG-5X832FyE3D-kXugGWHWBdd1JMHhE7SqyAcuXhNB8oJ69r0jI6El_SdidCwgTk0pQBSO65mUwCCBLvYLLWOVB9JiE0rJK332yOLRMsdt6zncIMWFHMgjC5d2GXX9Iziy7i1oVwo3hLWdvmqOahCjlRT6_3yj7XEwQ2RtEyTwqQh-XdHHTtpruVyLbAmcH-9-YL8jTpdDuj6zLemAvSzquU42GkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد  @withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/16427" target="_blank">📅 10:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16426">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت. @withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16426" target="_blank">📅 09:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16425">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال ۱۲ اسرائیل : مقام‌های اسرائیل ارزیابی می‌کنند که طی ۲ تا ۳ ماه آینده، احتمالاً تا سپتامبر، «هیئت صلح» ممکن است حماس را ناقض توافق غزه اعلام کند.
چنین اقدامی می‌تواند به اسرائیل آزادی عمل بیشتری برای فعالیت در مناطق تحت کنترل حماس بدهد و به‌طور بالقوه به ازسرگیری درگیری‌ها منجر شود.
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16425" target="_blank">📅 09:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16424">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=jQ9VHnisiFc8nUwk9F5rM4GL0vumGyi_urZLkICqqYgWEJFIBqiIKtlCCft_bMwnAHWBFnd6aw7j63Y4ZGQVUidEauGQqpzGXJuMg0tmYupjsvlAvpnq8ZvwIwNBS93SP5FGt84A16anjGwbNc5H9EK80vWJly6QfxgI_tO8Pds_Ima89D8UFVE8Ve7nQSNZ_edlx_DcU1US-N78et1pVn8OV4A179rOhJFNe8BP4Y2lLBWQLuPeF9kyA1BqfPBROWCMBeBXf1yeAiMF6gt4k424G_bUquziAVeN7cQlorYjeRq-GFHrPI-LtK7BqPXHJGJmD3AVwXSohM2m7LeBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=jQ9VHnisiFc8nUwk9F5rM4GL0vumGyi_urZLkICqqYgWEJFIBqiIKtlCCft_bMwnAHWBFnd6aw7j63Y4ZGQVUidEauGQqpzGXJuMg0tmYupjsvlAvpnq8ZvwIwNBS93SP5FGt84A16anjGwbNc5H9EK80vWJly6QfxgI_tO8Pds_Ima89D8UFVE8Ve7nQSNZ_edlx_DcU1US-N78et1pVn8OV4A179rOhJFNe8BP4Y2lLBWQLuPeF9kyA1BqfPBROWCMBeBXf1yeAiMF6gt4k424G_bUquziAVeN7cQlorYjeRq-GFHrPI-LtK7BqPXHJGJmD3AVwXSohM2m7LeBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما ضربه مهلکی به ایران زدیم. آن‌ها مشتاق به حل و فصل [مشکلات] هستند. آن‌ها واقعاً می‌خواهند این موضوع را به پایان برسانند.
ما به آن‌ها یک هفته فرصت دادیم تا مراسم تدفین برگزار کنند، زیرا ما مهربان هستیم. این حقیقت دارد
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16424" target="_blank">📅 09:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16423">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/16423" target="_blank">📅 03:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16422">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/16422" target="_blank">📅 03:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16419">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">@withyashar
🪓</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16419" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16418">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzace-HpVs6jw5YjsSsnMlQY39pYAiHohiywFTHYef4YxGC7LfWain8dQsBlIC5jUNnkOlbX1k1KcTPjGyGMiuQWRhs7h1UbOOUgolM5niPnB1VNKsw0rD_T_GDhqnW4y95wLqf-PAAPtcleTNN9FpVTywbGKgezH5-DNMD1n0rgA1nfycr89zZ-7Wkb9FWqLjmCv2GhZKAMRY3Fi7-MOm8xJn-60tORShqIq58S46d9gepyYk8h3OZ4TsW65jxlYGZzqmmUhk9jMrKnpomQ34BrARGTn2xZ08MaSdi7OtYd5FZ3nMZvAzKNK3qhB4o5pgx6er8apyKB9gLAADaHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون عزاداری سنگین نیرو هوایی آمریکا کف تنگه هرمز ، قشنگ دارن سینه میزند
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16418" target="_blank">📅 01:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16417">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjNfMkUJNBVx-gMbGKZa_e-LlBF9t4x45WMzZ92uZA2e-M_CyFBK6HBarOqccMzURpfqVKBGuVFknBRjF-4iouuSU7XJfiHtDdm77jBbMSUEo-R7eUe6pwEw4jXrSI9hveS65Kr3ytY4XDJCtSkUBkR99JFRzn85VQDQoDlD0OORChZCv83O-jWN3RK5iCuI4s9sZdrOgk7okZw12erV5BS7zgNOV_31Ec-gc5wP5XjVRb7rgFyH1qWoq-8EhnmYpveKeLnwZdIGy7QsTTCU0vPEvzzOrZeLb5nctlIE0khc_TIZELHCMjA9gus1pMExCZN3MHEFkiMRnj5rGz_kSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16417" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تعداد کشته‌های زلزله در ونزوئلا به ۲۶۴۵ نفر افزایش یافته است، به گفته وزارت اطلاع‌رسانی این کشور. همچنین اعلام شد که بیش از ۱۲۰۰۰ نفر مجروح شده و حدود ۱۵۰۰۰ نفر خانه‌های خود را در اثر این فاجعه از دست داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16416" target="_blank">📅 00:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16415">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba3ecf0ff.mp4?token=h_kjf0GRU4DZ-ct5HjedTgKHskkx5_wegvpwLThRWzAVcfzYExVvQztEtnEUf0UXUx8aDcNfh7L91WCDN8ayy3nFfpYR4dGcCoDt-KfHluw1SCedjdoBedIGImd4I6DS4eKpicXLo0BMbUwaI5DsQF_zlkzSX07akbFml1Or5kp25SA8QU2odpe3QxIwj5a_IWW8leHWPqykIjaPrO9-YYcHLomCIOui-scVXntJI1rwn4W3t5AFNitOhUjKabuIqWbxuaExRQ2WYF024rLV-fmZaAK73p4rJjvPlneyNjmamet6FFQOP4YbQcAuYHBXLOnsaO0y-0CHpDzGf9kMXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba3ecf0ff.mp4?token=h_kjf0GRU4DZ-ct5HjedTgKHskkx5_wegvpwLThRWzAVcfzYExVvQztEtnEUf0UXUx8aDcNfh7L91WCDN8ayy3nFfpYR4dGcCoDt-KfHluw1SCedjdoBedIGImd4I6DS4eKpicXLo0BMbUwaI5DsQF_zlkzSX07akbFml1Or5kp25SA8QU2odpe3QxIwj5a_IWW8leHWPqykIjaPrO9-YYcHLomCIOui-scVXntJI1rwn4W3t5AFNitOhUjKabuIqWbxuaExRQ2WYF024rLV-fmZaAK73p4rJjvPlneyNjmamet6FFQOP4YbQcAuYHBXLOnsaO0y-0CHpDzGf9kMXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی و قالیباف امروز
😁
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16415" target="_blank">📅 23:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16414" target="_blank">📅 23:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16413">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وای نت عبری : هزاران نفر در مراسم تشییع جنازه در تهران شرکت کردند، اما در اسرائیل این خبر خنده دار بود که "بسیاری نه برای عزاداری - بلکه برای اطمینان از اینکه او واقعاً مرده است، آمده بودند."
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16413" target="_blank">📅 22:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">المانیتور:
مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16412" target="_blank">📅 21:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79266b9c5c.mp4?token=kqrBYqo6T7cVgjTAyv3bdK9TTm46p4hGogtkpBMZpmbT66WoxF3srctBtBotE4c31tmy8HmSiqUQ66VMxzGsae5d8ZQG9qUcmrRQqXmXnZEMGdT49-R3Qpiyg88CEu4Piin174_CPKVCMTwKMk_G98mFeaN1gdI2tAIoD1QMX3frn50NI61KEFdfvzPXGjxyUazYF_BFzhuaFrS1mKm7DkwVIkjZoPUROcl1kTz0idxWVD8pyn-OQuykkCuGVRdniuNi41ntJrInsMW6lFBkjN7ySZyBPsq9ZRAOE7WXmbfrICZjLn6LNhNP3_ZW29LKZDKykKSM_lLCQsrSmkLvbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79266b9c5c.mp4?token=kqrBYqo6T7cVgjTAyv3bdK9TTm46p4hGogtkpBMZpmbT66WoxF3srctBtBotE4c31tmy8HmSiqUQ66VMxzGsae5d8ZQG9qUcmrRQqXmXnZEMGdT49-R3Qpiyg88CEu4Piin174_CPKVCMTwKMk_G98mFeaN1gdI2tAIoD1QMX3frn50NI61KEFdfvzPXGjxyUazYF_BFzhuaFrS1mKm7DkwVIkjZoPUROcl1kTz0idxWVD8pyn-OQuykkCuGVRdniuNi41ntJrInsMW6lFBkjN7ySZyBPsq9ZRAOE7WXmbfrICZjLn6LNhNP3_ZW29LKZDKykKSM_lLCQsrSmkLvbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمل پیکر علی خامنه ای در کامیون یخچال دار
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16411" target="_blank">📅 21:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یورونیوز : در پی انتشار ویدیویی از زنی که با لباس زیر در پارکی در شهر یزد قدم می‌زد، مقامات قضایی جمهوری اسلامی از بازداشت عوامل انتشار فیلم و «برخورد قانونی قاطع و متناسب با رفتار آنان» خبر داده‌اند.
خبرگزاری دولتی ایرنا با متهم کردن این زن به «هنجارشکنی» مدعی شده که وی به «اختلالات شدید روانی» مبتلا بوده و بعد از بازداشت کوتاه اکنون وی به آغوش خانواده‌اش بازگشته است.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16410" target="_blank">📅 20:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">باراک راوید خبرنگار  آکسیوس:
ترامپ امروز با نتانیاهو تلفنی صحبت کرده.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16409" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16408">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آکسیوس: نتانیاهو به زودی در سفری ناگهانی و قریب الوقوع وارد آمریکا خواهد شد و با ترامپ درباره ایران دیدار خواهد کرد.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16408" target="_blank">📅 20:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16407">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تکذیب خبر نیویورک‌تایمز درباره ترور مقامات ایرانی از سوی دفتر نتانیاهو
حساب رسمی نخست‌وزیر اسرائیل در شبکه ایکس نوشت:
«طبق معمول، آخرین گزارش نیویورک تایمز درباره اسرائیل و مذاکره‌کنندگان ایرانی، خبر جعلی است. یک جعل کامل واقعیت.»
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16407" target="_blank">📅 19:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16406">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صفحه‌ فارسی وزارت امور خارجه اسرائیل در X:
واقعا توی اون تابوت چی‌ گذاشتن؟
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16406" target="_blank">📅 18:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حوثی‌ها ادعا می‌کنند که با هواپیماهای سعودی در آسمان یمن درگیر شده‌اند، به منظور جلوگیری از فرود یک هواپیمای غیرنظامی ایرانی در پایتخت صنعا. حوثی‌ها اعلام کرده‌اند که هرگونه حمله سعودی دیگر، "با حملاتی به فرودگاه‌ها و منافع حیاتی در عربستان سعودی پاسخ داده خواهد شد."
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16405" target="_blank">📅 18:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16404">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آغاز مذاکرات ایران با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت
به گزارش جروزالم‌پست، منابع آگاه می‌گویند ایران مذاکراتی را با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت آغاز کرده است؛ مذاکراتی که در چارچوب معافیت موقت از تحریم‌های آمریکا دنبال می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16404" target="_blank">📅 18:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16403">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKWoMt1eB68So_t2dEnWPyNrBBJBfoKOroei9CbTz6OnUzasLza-wYGWVIc4ST7jxcspoJG0Czx3VnWb-Vh19bxsbIW5wIR-Vhj3Ed8ng6hhNMxJQcq6cpKqwnFfOpMcmeMeQIYVOsF3XaPixjyxfd46krQfyi44ewhIBFibDvVlHDHb1Pps442pPyZsMyx2-LykTeHEDWnD2vbq3i_rUMgfByuUvyMtEwfqHz3ORSeyHb8m2ztzQbKL4Stilrd_8VZ8bDBoqN15PsxKzLsHMaAmYGmveoxPRCPTgzmotr3QfRvg8uO3wyvJ9x8a-PSBVTFYzlOKiRpi1dIPlQIrvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: جان اف کندی بعد از من دومین رئیس جمهور خوشگل تاریخ آمریکاست
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16403" target="_blank">📅 18:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16402">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هفت خواننده سوپر عرزشی به نام های علیرضا افتخاری، محمد معتمدی، پرواز همای، مصطفی راغب، رضا صنعتگر، رضا شیری و حسین حقیقی ی آلبوم به اسم بدرقه برای رهبر ضبط کردن.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16402" target="_blank">📅 17:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16401">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الجزیره: ۵۰۰ میلیون دلار برای ترامپ، دسترسی برای پاکستان؛ چگونه شرط‌بندیِ کریپتویی/ دیپلماتیک اسلام‌آباد جواب داد؟
وقتی این هفته جزئیات درآمدهای مالی دونالد ترامپ، رئیس‌جمهور آمریکا، در سال ۲۰۲۵ منتشر شد، یک رقم بیش از همه جلب توجه کرد: شرکت رمزارزی خانوادگی او، ورلد لیبرتی فایننشال (WLF)، فقط از محل فروش توکن‌ها در سال گذشته بیش از ۵۰۰ میلیون دلار برای او درآمد ایجاد کرده بود؛ بخشی از یک سود بادآوردۀ بسیار بزرگ‌تر از حوزهٔ رمزارز که در مجموع صدها میلیون دلار دیگر هم ارزش داشت
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16401" target="_blank">📅 17:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16400">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2a30f1a3.mp4?token=NZUx085nZzCQXeXbHqCfP2hNPhoG-8ALlYeuAD63VG-A689GhS7cwpEsRF8l-KKEEaChkdi1vDCU5IFt6wL61tkLcrwFLlVlHOncnJEXn6ejGhvGnDpjEVEFXwgODrl4q5922Cq8Cve9lTi-gmkuihc02u8tH5Txe8-o4QhyQ6ZXFeVCM3nrL7g2-8xxPsw3ZP67M7bWSQ0OhKhdZe805S5oOki8hcFdiufJFZHR-TAt_jpDrZAPLRBsuOgkYoRJmwsfa0UdsKUStYiGPk0BNTR6o3PhFgXsVQVdE6_M-5wSo8TS6V6MXyu7IR53io9oNH3QZezeGZB9qp4YHO82mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2a30f1a3.mp4?token=NZUx085nZzCQXeXbHqCfP2hNPhoG-8ALlYeuAD63VG-A689GhS7cwpEsRF8l-KKEEaChkdi1vDCU5IFt6wL61tkLcrwFLlVlHOncnJEXn6ejGhvGnDpjEVEFXwgODrl4q5922Cq8Cve9lTi-gmkuihc02u8tH5Txe8-o4QhyQ6ZXFeVCM3nrL7g2-8xxPsw3ZP67M7bWSQ0OhKhdZe805S5oOki8hcFdiufJFZHR-TAt_jpDrZAPLRBsuOgkYoRJmwsfa0UdsKUStYiGPk0BNTR6o3PhFgXsVQVdE6_M-5wSo8TS6V6MXyu7IR53io9oNH3QZezeGZB9qp4YHO82mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
خطر حمله قلبی
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/16400" target="_blank">📅 16:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16399">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f09f9f705f.mp4?token=rZJp3ZQMJ_Y-xFc_HkFuBCD2kl-KEyod73iANIYP1Pxzi_zCg8w8R3pUm0ICGdXngXXXsQ7NLC9u_oPdfZGtg3sE_mk3jDIYibSqU2cKPcIM5sf3P-sOpGIlzR7dFH4doEiAf0nsPi8Qw04hAHVBMUo9YxybNE48O42OSWtBxNjvPkIqo987BQeQ9UC7umpPl32DvpNYa1bVfpUhlNopvKaMsJpE3XPb4gQUdY9ycE84jqHv0tG3WCNwhHVT7A2T_KOVE4yuqCaV2bvOI0vGaGD_UA8t3hh1tFqE3NAdP921QZtdIrjtOI1fia9s94EKf3MmVIrvQifMLoT2dilR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f09f9f705f.mp4?token=rZJp3ZQMJ_Y-xFc_HkFuBCD2kl-KEyod73iANIYP1Pxzi_zCg8w8R3pUm0ICGdXngXXXsQ7NLC9u_oPdfZGtg3sE_mk3jDIYibSqU2cKPcIM5sf3P-sOpGIlzR7dFH4doEiAf0nsPi8Qw04hAHVBMUo9YxybNE48O42OSWtBxNjvPkIqo987BQeQ9UC7umpPl32DvpNYa1bVfpUhlNopvKaMsJpE3XPb4gQUdY9ycE84jqHv0tG3WCNwhHVT7A2T_KOVE4yuqCaV2bvOI0vGaGD_UA8t3hh1tFqE3NAdP921QZtdIrjtOI1fia9s94EKf3MmVIrvQifMLoT2dilR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16399" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16398">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">محمد نعیم جُندیه، رئیس امنیت نظامی گردان شجاعیه حماس توسط ارتش اسرائیل کشته شد
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16398" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16397">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">واشنگتن پست : مقام های آمریکایی فاش کردند اختلاف اسرائیل و آمریکا با ترور لاریجانی آغاز شد
واشنگتن برخی طرح‌های اسرائیل برای ترور مقام‌های ارشد ایرانی مثل عراقچی و قالیباف را متوقف کرده است.
در این گزارش آمده اسرائیل به دنبال براندازی نظام ایران بوده، اما آمریکا به این نتیجه رسیده که چنین هدفی از طریق جنگ عملی نیست و به‌جای آن تمرکز را روی تضعیف توان نظامی و دریایی ایران گذاشته است.
همچنین ادعا شده «ترور لاریجانی» نقطه عطف این اختلافات بوده، چون آمریکا به دنبال فردی برای تعامل در داخل ایران بود و با حذف او این گزینه از بین رفت.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16397" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16396">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هواپیماهای مهاجم ، حریم هوایی یمن را نقض کردند، پدافند یمن درگیر شد @withyashar
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16396" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16395">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16395" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16394">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLzoKN9By2NMDwZ656ht1h84dLIfJIP5wVEWBf0kDZw4sfMW1kpJ1Jf44Azf1PEt1MS7dyDuez0TluO_svWRG5k338k_ieqk1OU72Erxkef2B8rtTZcqGPV1wJWkRpNPB747HkmPyV0yLcZLk8cMDGW2eBT2lynnm5PcSpGbsfyk8kBF-18UepnXxn41pV2SAB8C8K0oQ0HuR--3U4rnocYvmARV1L3Lvz40T-XVhZ1gWJKv0eGKWrEOLUbfTOSCE7VoZrX0cFG6STz5R3vHWMcqLPl4fLujbVIoE606WXnldLNQEgbDB9RPQWdGm_K4TArv4j5K5efyxJXhSUl5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فشار فروش آلت‌کوین‌ها به پایین‌ترین سطح در چند سال اخیر رسیده؛ به‌طوری که اختلاف بین خرید و فروش در آلت‌کوین‌ها (به‌جز BTC و ETH) به ضعیف‌ترین وضعیت چندساله خود رسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16394" target="_blank">📅 14:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16393">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7_8Y6NF5387AR_qjWYXR4txj1BpiYftrZTp_MBg47UAhJDfKPoTFadYjXza9AyOv8V3CHiN35t_y7CYjfT5VxZdgvoJBe3vz6ALS6Urtyz9uCrfzfy83LPO_ktDOGZHwkFUOeRFcDxizoB3pWG2bJBA_mLlviabwP5v0JGSQHCurEln8poWWeQ30ql1kboFPrlSrFcaCW_KNArdLZlELhp9HpW0Fc5YKmB9qblXpvuGbicMSzWgfN4Uf2X40kdahtieHsvM5Nac-8R4jSSXXjaGmxsPmlAiVXHzwHABL0VmJDkE3vvMFPPoJRctHtt08pUvlozKjFjd6Jn_363hMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16393" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16392">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تکلیف امتحانات نهایی دانش‌آموزان مشخص شد
رییس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، با تأکید بر اینکه برنامه امتحانات نهایی و کنکور با هماهنگی کامل سازمان سنجش آموزش کشور تدوین شده است، گفت: امتحانات نهایی پایه دوازدهم از ۲۱ تیرماه آغاز شده و تا ۱۲ مردادماه ادامه خواهد داشت. همچنین امتحانات پایه یازدهم از ۲۲ تیرماه آغاز می‌شود و تا ۵ مردادماه ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16392" target="_blank">📅 13:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16391">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">WarRoom with YASHAR
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/withyashar/16391" target="_blank">📅 13:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16390">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">1$ Tether 176,000 Toman
Brent oil = 71$
Gold = 4173$
BTC/USDT binance = 61,685$
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16390" target="_blank">📅 13:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16389">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsfL0etOfD0w6a6_mML1Lp2Ssub5RauOqT1Uj6h-JAfrRVd9VCEoV1Of5A5LCfZIamnyLjZycnGiKEMYv3p2BEIkX_dwe6KfMkP_dllcaElt7JT7X2Z1yCisEbJSSW7QqMNsnnvAUr_YOp9NghRayRm_3q6ufGuXuzCQhzgJBmO3tI1f6wi41LDmb47XbmWZGYPX3QEdqo9UO4A7vJ6cwLRQ2MkI4xQ68VG-me9HryfN2vCHP2yO3PnV5RFg8T5xNitT596HiVdndwXFQwGb7oIm70zQjVYPlOgK4_DwJ_UEG7AGxl-PfukGGemsbX415VwLdCKks4bul6LCn-W5uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس از تفاوت تابوت محمدرضا شاه و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای  انگار پرچم عربستانه
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/16389" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16388">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فیلم مستند «جاسوسی از تهران» هم اکنون با زیرنویس فارسی
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/16388" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16387">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۴ تن از نیروهای نیابتی جمهوری اسلامی عضو کتائب حزب‌الله توسط سرویس ضدتروریسم عراق (ICTS) در بغداد بازداشت شدند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16387" target="_blank">📅 12:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16386">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU86UY-sDz4f25988BGrKTjb7UyKAi2L0ovVDjp7OcQN5I4G9cjzAuo2QD1zTGcpFUMe39DfYQ7EHEYrDFGnSNJFidSWA_mH38fnRYzdyI-pmd1Ao02N2NxN3NgTcbH1gao5hdNKbbExBCMsT629KeL7VaKXgezOGCpXB9TS1Un69-XUt6hNibNN6tV7f4uy6gDg7rS_DF_Z2sjZmNhCoOmW0ZhmXOAmWNlfLVC8hBUdGBjSzJZAZ3rdNfeMEs2_PULhC_dZaojJAA6OMhLvstjW0P10AnIeWLFSCS7_DA7wpIry6VpjJeT4skm2eIPwqYzLZDMuFUyDrajgrE8Clw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رادان : یک بمب گذاری ناموفق در مصلی خمینی تهران شناسایی شد و خنثی کردیم
با برهم زنندگان امنیت تشییع جنازه بشدت برخورد خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16386" target="_blank">📅 12:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16385">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پشت گوشتون رو دیدین، بیرون رفتن ما از جنوب لبنان رو هم میبینید. @withyashar بنیامین نتانیاهو: تا وقتی تهدید برطرف نشه ما از جنوب لبنان بیرون نمیریم.</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16385" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16384">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIDxK1gdj73Yklu8SYJ9m7HkyBBJ_VhYKcMxFS7QMq8Uz0_wHMDrUigkiWBoECXLIAAZZJEwZYInr39sHyrot79HwHm671xzJRB0l-kyally9j4W1Z2fnY2Jp5tYQCI8xx3KmTPqB7RoFyR2B_7N3QjKc2dT5QcNoscatjfMp3dmpCFTGcGWI5OS0yishi3d1k-bvIAk9cfYswOEcVa4TBqs2D8BUIJRTa4G7zVTt6HjEZxeUyHoMR4dclOTYNo3y_j3AqcGHWxGc4nBN19wmS46wIwvdHp7QnsITikxyJmDbsep5Nqpp05ZOMV3ijSoeZHccZx9TfrdW8i9_34utg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس تصاویر ماهواره‌ای به تاریخ 7 تیر 1405، آواربرداری و پاکسازی اغلب سازه‌های آسیب‌دیده در جنگ اخیر در حال اجرا است و برخی از آن‌ها کاملاً پاکسازی شده‌اند
هم‌چنین جزئیات موجود در تصاویر نشان می‌دهند که فعالیت‌های تولیدی در بخش‌های سالم این مرکز با شدت بالایی دنبال می‌شوند
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16384" target="_blank">📅 11:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16383">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کل تهران در زمان خاک‌سپاری رضا شاه (۱۷ اردیبهشت ۱۳۲۹) جمعیتی حدود ۵۵۰ تا ۵۸۰ هزار نفر داشت.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16383" target="_blank">📅 10:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16382">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc8Z7_FpFqhRkaYPowo2SAl6DR2V8q5o_PNEPR3e69iV_xY49rLH-Bh1mXixPNfMHdsEzG705K5evjLR5MCaVwKEUsumYGKZKeuYxUgALeu-tGl4BfyS9i0DNbBQrFYSt_DD2LLMyrc472AdJaGChhpuCcCwrWC5z-OZbGES2vbjjCC8fD2WXDzZQkNrJrKDjK63B2pu8su8piCPLFCVaiPNfjAc-fZWRkt0rcuvTqHAp0P98zwkO4fyiP_WTiJacQKngIdC_oCljsGuj_KEnCgL27B1qg4_1ueR1PgGae68ZS8s25LBGqvmH625IHGcltjk6os2or25A2sL50Pzxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16382" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16381">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس:
به دلیل تهدید مداوم وزیر دفاع اسرائیل به جنگ و ترور، ممکن است در دکترین هسته ای خود تجدید نظر کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16381" target="_blank">📅 10:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16380">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwIebEMpdLz06Ykg-Kamg_53LHQXP3i90Sw4qBbbz-IF3zF9tYyH11vGrTBOF35dwU4Hqb6sf5dQbXx6cUXct8i3P207Jz4E1EgwnulV3HkRGCmI6JcNNy5eXPOpIAQuPPCXnYo4ghrJPIa_BByhshtwzAyIhMIGJ5mFvHdWyYt7a0DWoklBEbSb5VtlKhCPrnZ-c4KRDhVRKjbJ2XZpicwxrsjTstP7o3uUfMqWuKRWOUnGpgsKIrpfn72ZDpLfmxCDkhDHfiJCbnxkQGatuvNUKD-igUnN9p8xai-h9bp3pl2PBp9kIF74RA72ZpxWZ4d1Zv2DJkBKEaGkrkcxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادای مفلسی احمد مسعود
(فرزند احمد شاه مسعود) و هیئتی از افغانستان به تابوت علی خامنه ای
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/16380" target="_blank">📅 10:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16379">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هواپیماهای مهاجم ، حریم هوایی یمن را نقض کردند، پدافند یمن درگیر شد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16379" target="_blank">📅 09:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16377">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ورود هیاتی از حشد الشعبی عراق  @withyashar چند نفر از‌ موساد حظور دارند ؟
😁</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/16377" target="_blank">📅 09:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16376">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ورود هیاتی از حشد الشعبی عراق
@withyashar
چند نفر از‌ موساد حظور دارند ؟
😁</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16376" target="_blank">📅 09:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16375">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ: من به دنبال تغییر رژیم ایران نیستم
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16375" target="_blank">📅 09:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16374">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اتاق جنگ با یاشار : با توجه به داده ها به نظر میرسد کشتیهایی که از مسیر امن آمریکا در نزدیکی عمان رفت و آمد می کنند، نسبت به مسیری که جمهوری اسلامی تعیین کرده بیشتر است. @withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16374" target="_blank">📅 09:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16373">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2642f2a070.mp4?token=SS0xfOYeKp5hqvs_zuhMqP2Woj4L_W-sivwFUt8kLKj52QJ62QWmwAqhUhnPosrR2HvkpoVCtLrmpOHZB033Sk7-Gwt1V5W3tVvN02Sftq9NER7hrVAycSvt8qpxx28zqSCg8ns8u-Xjq7G1GJydi8qtZsAJuSrUUktuY9MU0NZn9jSUH966cu1EdkXsouvNFCjjnXMocyeDrI2843J9UA8Cdr2KmgUaVSczoKLNOwi9uffyJzFZMI-xi_klNUNWGZPiwmBmte3IDn6mFxPIjDDU1kCo6CwXWmx3hUSjDPPY5sjUOqmsdT_6aaXeGbm864LP3GAeB2dXwFU9BvasyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2642f2a070.mp4?token=SS0xfOYeKp5hqvs_zuhMqP2Woj4L_W-sivwFUt8kLKj52QJ62QWmwAqhUhnPosrR2HvkpoVCtLrmpOHZB033Sk7-Gwt1V5W3tVvN02Sftq9NER7hrVAycSvt8qpxx28zqSCg8ns8u-Xjq7G1GJydi8qtZsAJuSrUUktuY9MU0NZn9jSUH966cu1EdkXsouvNFCjjnXMocyeDrI2843J9UA8Cdr2KmgUaVSczoKLNOwi9uffyJzFZMI-xi_klNUNWGZPiwmBmte3IDn6mFxPIjDDU1kCo6CwXWmx3hUSjDPPY5sjUOqmsdT_6aaXeGbm864LP3GAeB2dXwFU9BvasyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون بمباران شدید جت های اسرائیلی در جنوب لبنان، چندین انفجار مهیب در عمق جنوب لبنان به وقوع پیوست. @withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16373" target="_blank">📅 02:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16372">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl16JL6D6PvYJDYBbhUStFUvDKvVeQov2kfO-6Fr0v_XC8rLUMqbD0FCvi81q-e36QBBhs_nx9YglQVavc8TTGc4UaExYqp0y4tRLaWGZhvcc-5LZCyqDSucJqnRz-xOR_QRd8tLLfYENFc02pZvGIPPRdyhTQN4Cy9rcD7Txwucitvc7W85zHwRnDyBvjmfUMkfgnzxSpAvbwAJcwLRo5te-zeHM6Ktg4RyV2LtiB-if17Zw9z2XmtHPFhQQ0DeBIAk69bQyMVlzo1lhQAXgd_Uvbut8VF6xHv_Tb_I7CgR1s5hAnp5jbaKCq2k23tJQ_WoaZqBSkcDT5a2gnsSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان تجمع و عزاداری شدید نیروی هوایی آمریکا برای عظما
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16372" target="_blank">📅 02:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16371">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هم اکنون بمباران شدید جت های اسرائیلی در جنوب لبنان،
چندین انفجار مهیب در عمق جنوب لبنان به وقوع پیوست.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16371" target="_blank">📅 02:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16370">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ-qpDmj6aQa5l4QgTsasiNwzy4uPTJgQajc866rI7QKrBuD0P_S1d3BDDFpqlCn33jAhgf1mMO0eKe8rTdrC7eJPGRu9vyrHEgZ30bvAcMnh0QN6ZikHefO1mLW-92bIia9q8vvBLstZ3eRnEEbLbqwl6GGwKXGxktiKBo_fFhsTn43KtXirn1SCbgmmVXtI2uqH0EhmI8uP1kCvKyHfK6vi2lQ9Jo8tAyTCR2rpb1ltEiHD4jWETNtJJQoEBRhU2_EGAp2CKiAyiDRaq8IU_0iEDxkthYjZ1NA4nhe5ud9EqStgw2EEGG8xx4Tfm046Fh0j2Wu7sqpprC4KMvXFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند. ما هفته گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم. @withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16370" target="_blank">📅 02:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16369">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3226c235ec.mp4?token=wBXOgpTfxQu6x97kyX3eWkS_S3qeXqRG7DrD4BkBDlc7Fs1BloDnrJAsoEwy99O4G2FEHNzg2tyHsHOp6hwe-CsoMJ8bVT9xFMNOyn9SswtmDmP8udTWTqgSfz_xTqZcaRp-W52OaqY0pmymGkASRDBHMFj4DdzslzGZ0Ac5IlWRuQ2A65Lzd0I44jKFTwX3bZ7NNFltT3GhASKzyv7fdHdpypoAl592pnaFg7nHhgCPp4R-a0-6rcdbp7tcfLAcNwiUdIv3DCWNiQiG87o1atOUh7L1gjU4VcTMf8twNHAkMXNgJCshi2BvPvYX1Skg0sxoknwDzSF6asZs_1ePdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3226c235ec.mp4?token=wBXOgpTfxQu6x97kyX3eWkS_S3qeXqRG7DrD4BkBDlc7Fs1BloDnrJAsoEwy99O4G2FEHNzg2tyHsHOp6hwe-CsoMJ8bVT9xFMNOyn9SswtmDmP8udTWTqgSfz_xTqZcaRp-W52OaqY0pmymGkASRDBHMFj4DdzslzGZ0Ac5IlWRuQ2A65Lzd0I44jKFTwX3bZ7NNFltT3GhASKzyv7fdHdpypoAl592pnaFg7nHhgCPp4R-a0-6rcdbp7tcfLAcNwiUdIv3DCWNiQiG87o1atOUh7L1gjU4VcTMf8twNHAkMXNgJCshi2BvPvYX1Skg0sxoknwDzSF6asZs_1ePdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
ما هفته گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16369" target="_blank">📅 01:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16368">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cdd54f95b.mp4?token=e8KgLStmsILaXi7vx2pNSrbcG3NiRxNHizI21J5j73xwJObWQKY_eZKxhODi4cndKskjPW0YG1ZZZF4zfaZNC67-JpXJiwGby3Vv6px43j4ZEr0P6KJKAg1mb2779_sFBHxLRh3oZyTkkPRosKR_tVxvGXMgHT910GbT_QUQvdvRxCQt9UDX6YYDf17darQ2T6E4_NBuTFz5qzN9hmKDXoKAhdy1BCYBNLzL1imFrIbJ9ilk8rgr9tyVhGx5noTgzvbyeDxmYcmpVnoVrjNVi3PKIJgJ_cO_7rpPVveRrGihys9qk_zB-lWLQXGk-x7o19oy2oAx4MYaFcKfWQ5K9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cdd54f95b.mp4?token=e8KgLStmsILaXi7vx2pNSrbcG3NiRxNHizI21J5j73xwJObWQKY_eZKxhODi4cndKskjPW0YG1ZZZF4zfaZNC67-JpXJiwGby3Vv6px43j4ZEr0P6KJKAg1mb2779_sFBHxLRh3oZyTkkPRosKR_tVxvGXMgHT910GbT_QUQvdvRxCQt9UDX6YYDf17darQ2T6E4_NBuTFz5qzN9hmKDXoKAhdy1BCYBNLzL1imFrIbJ9ilk8rgr9tyVhGx5noTgzvbyeDxmYcmpVnoVrjNVi3PKIJgJ_cO_7rpPVveRrGihys9qk_zB-lWLQXGk-x7o19oy2oAx4MYaFcKfWQ5K9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو رو قبل از خواب ببینید تا پستای قبلی جمهوری اسلامی رو بشوره ببره.
@withyashar
🌟</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16368" target="_blank">📅 01:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16367">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.
@withyashar
نسخه اصلی با زیرنویس انگلیسی و حجم کم تا بعد با زیرفارسی شو بزارم</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16367" target="_blank">📅 00:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16366">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdc81a4ce6.mp4?token=NjA49Q3HXLAzYL2k3d-kp80Uwwwz2Q8cMiGcinL5KO99CgLpUKNX8nvTGSAB48Vz0TIfuS0xukR6wWKbAA4iufIKVVHy9K4G66m78Elf7Gc2kRvQZWBc0otJj0vbGMDZbVC6hHP3PJMWPI9KQnNAtCpZi30RZO5S-IXe6hmB7oBPkJf7KJtkcMrD47Rhw9r4TnKnwHPHbXZu2BTSnMeBk17kP2AP54kFD-ggAxHg_qicZqUeM4xuHVQpzWVMsXTCqKD-eoEoGmnO1CALTRZB_uxk-CK0alpZeb01fHDw5ryhJmiQJ5lHPqR-WhTF4fCztLaGGti5G5fqRIyGJZItOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdc81a4ce6.mp4?token=NjA49Q3HXLAzYL2k3d-kp80Uwwwz2Q8cMiGcinL5KO99CgLpUKNX8nvTGSAB48Vz0TIfuS0xukR6wWKbAA4iufIKVVHy9K4G66m78Elf7Gc2kRvQZWBc0otJj0vbGMDZbVC6hHP3PJMWPI9KQnNAtCpZi30RZO5S-IXe6hmB7oBPkJf7KJtkcMrD47Rhw9r4TnKnwHPHbXZu2BTSnMeBk17kP2AP54kFD-ggAxHg_qicZqUeM4xuHVQpzWVMsXTCqKD-eoEoGmnO1CALTRZB_uxk-CK0alpZeb01fHDw5ryhJmiQJ5lHPqR-WhTF4fCztLaGGti5G5fqRIyGJZItOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های یک مداح حکومتی:
ترامپ رو هلیکوپترش غیرت داشت، اونوقت رهبر رو زدن هنوز خاکش نکردیم.
چرا راستش رو نمیگید هسته‌ای رو دادید رفت؟ چرا نمیگید هر روز لبنان رو میزنن ولی بازم کاری نمیکنید.
۱۰۰ میلیارد دلار طلب داریم، بعد برای ۱۲ میلیارد دلار مارو کشوندن پای میز مذاکره، تازه نصفشم گفتن ذرت و سویا میدیم.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16366" target="_blank">📅 00:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16365">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd374ffde1.mp4?token=vVIqiV9ORLgTDJOUNxq0SWOKHMTjQghYt7fzQZjtL3qX0kuxoI2uf9U8W5Ep-6-Ogva4VKWCI32LVCQWNKmAFzfD_qjV030KwukqvaAEr9tUZ7mBqCWcCto5--kG5N5d6wn9D9dKEaULwL0AridWbg50eFsLc2q_ZqvWAOwnETSi0mB2vtmuw9ojsYymXz9-W5BfXTHKdWhpfFq0aU-AvYhwB_pXTPa8By-NuVjuzPFaWQG21Rb6t8yuucTK2u4enJSZJvyShujfBUAJC9O9VWB_iu4RIaM6RS6tCacJsqnajqAXpNYEyNteZcFwSOi_88cIhafJs3-fjQL9Z8ieYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd374ffde1.mp4?token=vVIqiV9ORLgTDJOUNxq0SWOKHMTjQghYt7fzQZjtL3qX0kuxoI2uf9U8W5Ep-6-Ogva4VKWCI32LVCQWNKmAFzfD_qjV030KwukqvaAEr9tUZ7mBqCWcCto5--kG5N5d6wn9D9dKEaULwL0AridWbg50eFsLc2q_ZqvWAOwnETSi0mB2vtmuw9ojsYymXz9-W5BfXTHKdWhpfFq0aU-AvYhwB_pXTPa8By-NuVjuzPFaWQG21Rb6t8yuucTK2u4enJSZJvyShujfBUAJC9O9VWB_iu4RIaM6RS6tCacJsqnajqAXpNYEyNteZcFwSOi_88cIhafJs3-fjQL9Z8ieYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت
دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16365" target="_blank">📅 00:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16364">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">لحظه ورود تابوت علی خامنه ای به مراسم
،
امشب در حسینیه عمام خمینی
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16364" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16363">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : خشک خشک ، از دیدن بشقاب پرنده بگیر تا نرم باز‌ کردن تنگه هرمز
💥
کارای اداری یادتون نره ! برام بنویسین چند وقته منو دنبال میکنید ببینیم ترمیناتور شدید یا نه
😁
⁩
https://www.instagram.com/reel/DaTbNq0x1Pf/?igsh=cmx6bXhnYXB6aTN5</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/16363" target="_blank">📅 23:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16362">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بلومبرگ:  ۵۸ میلیون بشکه نفت و میعانات ایران روی آب انباشته شده و ۹۰٪ این محموله‌ها مشتری یا مقصد نهایی ندارند.
با وجود تعلیق ۶۰ روزه تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خریدها محدود مانده است
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/16362" target="_blank">📅 23:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16361">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSdu_QRMiFNLNdAr-jADQU4hj32Gxktr6n95OuoM7fhjmCB34n6wKGRp0pJOAqubSZmkwRrvnCxxCFZuNKXGmcN2EG_RwoHm7EdvIuj6cCJxNy5qBxnvj1NP8ysiPFHKJRkmE2wgiqdFuS9CS50x_LWfhFPrz6LJ_ADFAtG46YVKah3RMKsrNLelEbwLrpPSHRXhfLxwaA8D3hckCnXhGzqYWt-olETARf9u9hP7oPS6pJL_QZdVKIl2UzI2fAxnyQ8P0EcyAQRqsVyRj7LVg-0sJxsvHVDDRg7e5aHudZKQR_QED1Q6vMWANImqkzsVDM1s-eMeV5cwRAc8b6fz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور پست جدید اتاق جنگ
💥
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16361" target="_blank">📅 23:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16360">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مهران مدیری : با مرد ۳ هزار چهره که دارم میسازم باز به اوج برمیگردم
@withyashar
😐</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/16360" target="_blank">📅 23:03 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
