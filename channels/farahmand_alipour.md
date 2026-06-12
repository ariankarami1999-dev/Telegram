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
<img src="https://cdn4.telesco.pe/file/fCTAvFmpGhIiDlGKyMLZf_I6ZNZU6_lrgFlDmDO06hhkU7ZSRONIF3hQTVywJjNRy4cC7XLETBShSqnJW5XZDMUeZ40qx8gnfnvwQIeZ0GYSbC2cHfBZk7h-3sfVlKAwvuJMD_64Jn9T99ohgEDSYStewm_QKbMY8Jf1xWevoXn1Myg_gBEmsbk70NTbxbjddQsNrcH2dloMQYoVqaxXtaDRC1NDn3LHLTq8ZnH2U-xUx5ABqnDBxUG64TmcxBIQmnSkIMUm2K3uNqhhVXLNvz_NgKXTVJCv_lkOm9XtMtO6dUvUCk9S0dKW2bv98ychhkoD-EfCKAqhuK3nktKSww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 09:56:29</div>
<hr>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=XV7r8qNCBmYeidozXAHEnHJ4hr-9HoobO5ZsUyqP2yvMpaGLBCUpr9kjS_79HGVkqu50O_AuCo2O3YFLfjqel3-DQ0YIe7O8VVxfBro3zJFPTwHQ16pvkLJalaoSjdBgzz7Z6AzVXgzrtMud9ZZORWBAI3U70ZvJ-BrE3mqA-fe0MTs-0L3rANnjxtf484ZNBoUoZ1GIGIgr64t6d6SfxlC6nhySXNm6r3_7L2al1zrXKUP00HsVY07kwdCg64b_IH-oRBrQLaQJerAaonhzSUc_AkaFnPA6vzUvpX2BvJZbJAfRobBUr4AnOju4ZaUbCWdpsY5_axiL_Lt41Q_cUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=XV7r8qNCBmYeidozXAHEnHJ4hr-9HoobO5ZsUyqP2yvMpaGLBCUpr9kjS_79HGVkqu50O_AuCo2O3YFLfjqel3-DQ0YIe7O8VVxfBro3zJFPTwHQ16pvkLJalaoSjdBgzz7Z6AzVXgzrtMud9ZZORWBAI3U70ZvJ-BrE3mqA-fe0MTs-0L3rANnjxtf484ZNBoUoZ1GIGIgr64t6d6SfxlC6nhySXNm6r3_7L2al1zrXKUP00HsVY07kwdCg64b_IH-oRBrQLaQJerAaonhzSUc_AkaFnPA6vzUvpX2BvJZbJAfRobBUr4AnOju4ZaUbCWdpsY5_axiL_Lt41Q_cUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=hKZOZSLlvmPJgpQYIu5hn3Zy1i_Vv1mJuMt_3coQgYMa2VLKrWQHQq8xwxVyWZ_xtJRF_n5MSPN5h19GTJh2sTRPkHCmknMwxRyWk5okBrxrm3pIjWv_auryvKXsRQEDtsoPBowrTag-XMwRnK6FwJyesxYr_qduVVorr61DP_7q2pmJ4kpcXOy-no5vOu0PS-C_cDmc4js4AX90zTHRS_51V3tgyhSmpXzng6fZaYHzZm85Pk6s9zPlS2RkCxugQFGc_8YryW7hxPpZyT6DczsRYs9Qed0tQlbWw9B72Oz99fZWLRVyBR_7eIEmqui8A1y63tZg2oGzZflAeyLfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=hKZOZSLlvmPJgpQYIu5hn3Zy1i_Vv1mJuMt_3coQgYMa2VLKrWQHQq8xwxVyWZ_xtJRF_n5MSPN5h19GTJh2sTRPkHCmknMwxRyWk5okBrxrm3pIjWv_auryvKXsRQEDtsoPBowrTag-XMwRnK6FwJyesxYr_qduVVorr61DP_7q2pmJ4kpcXOy-no5vOu0PS-C_cDmc4js4AX90zTHRS_51V3tgyhSmpXzng6fZaYHzZm85Pk6s9zPlS2RkCxugQFGc_8YryW7hxPpZyT6DczsRYs9Qed0tQlbWw9B72Oz99fZWLRVyBR_7eIEmqui8A1y63tZg2oGzZflAeyLfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkVg761KSZAfaC4OXcuYo7SAJa1RjV237Yyf-QwFenlX-GsGqWOJz477oFhfsHAhWKuHXbAWG-F5YMnKMzamSyRIXJ8CtOjfZb7ne9BrNPkMxQybLCI3O69OdVTEM8eGeAm0pAY0zGRDisHqOuKZ2PLYErCWs-8mlWTAQiQh90ETl-PWzCIOnGjdNi0fRIR6FRiCC8vF5FE_DCCIgIhzGcQ1NPHLF3zQltHYbWiACiXB05QqzRilX4lqOH08r61ppiTZWvn27oT9eYp-TYPzjrNZ8fjpOW53IOU45qp53u0b1EbzvBXePp6CgKzyVRIlu5VQ77QTQks8iondQVmPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=MTQx-xdvtNZ33E-O8VbdvvVNfKtatosZcGBfnetZQVqYTHXE0d30KKO2Kl0epVK6lRWiae42cZEfcfZ7U0lPF5IQ_8-KgkM_JyRvh00vcV8lANyB0pmuRIehsITR9Uc5QIx5hGn5N9piOA0kCgjWEjPeVRK8aCffa7Esa2Pw97VRZhic3Vjpp_VC0mIScTWuzV4PxFK-J_BV3noPsAZ8yY1C90rU02_5npd9ix1TpGfd8HgrQMqrPDDX0p1ueI0fKW310_RTxGTY2Jw5azlFQ1CfeYYOdm7n9s4HssfsVRfbyGueB7KG_pTQkwIDU9YWbOnoxxUnla-DKsC7KEq2jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=MTQx-xdvtNZ33E-O8VbdvvVNfKtatosZcGBfnetZQVqYTHXE0d30KKO2Kl0epVK6lRWiae42cZEfcfZ7U0lPF5IQ_8-KgkM_JyRvh00vcV8lANyB0pmuRIehsITR9Uc5QIx5hGn5N9piOA0kCgjWEjPeVRK8aCffa7Esa2Pw97VRZhic3Vjpp_VC0mIScTWuzV4PxFK-J_BV3noPsAZ8yY1C90rU02_5npd9ix1TpGfd8HgrQMqrPDDX0p1ueI0fKW310_RTxGTY2Jw5azlFQ1CfeYYOdm7n9s4HssfsVRfbyGueB7KG_pTQkwIDU9YWbOnoxxUnla-DKsC7KEq2jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OENnE6emzRs-rNh4mf9GKANY7T4xVIQqe5FSYR8mSKPIZvMWVRh8yst5GSfb6WyRAxW2I2zpJ4FZVJprAbfbGTD1LTgsEdoScAm1fFd67jAnAhkJwB_N27rQEn1T-DhcVEpwQHnNDkPDfWTMZEt1vGiNOr4FApRPIXuSK_7fsMo3rUVKzD9r91vQhrbsTpOW8g1-Hve0m3p_HUk7w18TLDqvwHW8fwE4Uxb6jt6HPp8-0Rlnju_GNvqEj1mliyeHqV3Wnl8SxNYBO0g2EzCs3WiduYTXQkmkQV9XmfGNL9rovFuogf4CGgKR_p9DJ6e8HSKgSPueVEkZJjpt-MGvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN5qa2K1Q6afAndskOz-9D4lLeFXOpKbeVnEbrnwtPxdWesdYsfUudAK8g51eXLnozGLrJIOieK_S1iuDXQ_dmajZSl2G6KFKIxD8BwgdskxuUAKeBP0yGCu3p_YrhK7_CSgHodEp7fretDtU4NFw5ui3W2oNohM9Uff4wZ1yr1rZ1dF0iy2wriNK5dcOuviaZoj7ky7N0-H2FUaVJRQhrt0QwsgJYYxrEg5sWx8RkBXOTpiNqAqiqebAi11i3vbpZl_RIc2ZG7QO8qH2iyX5bYj__OnNCCLoiu1r1PkEXsq7oMDLVaT-iXRC8wfwmC7JxRJzw7IKbslWPSnUyR_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtqSdSKpRFXwIWDMeR44L08-OgDfkD67WHOXuBtp3VvZ1cclyiC-YpOB_8-RUZpPCqPxTq3n3EqTl-1K7QXkVW_ge_kFiaW6qFjnFVZCAg8_Xe6ZjHpZAU4WyzZJa6wgIQwepjxEUceT3AEUbLS8T6aTKB_7KrQmdLxepS3LAwES2qvtkyuK15DQgdNU4M9RR7ONiIn480x7htYYLEb1quUv21MnQ1EAUoX49Ar32CGF0pYSed1zJRkMsqRQiGmAVGP6g7yyMa5S5AdHQqkBXTw5hRlyd1NRXB2eJUB3T5mqOqIqgUC8K63Ewba-tBehuUEiAdbdjGgwjsmJWdy3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csaBlTeHN3QgQ5LkyNMWUzsPUduhfrqUGAWZ0fUWY8pzzcN1H1LwY8hxjDvj7cd8kGUUG1aAKKUZlp2oKzQae7tRYGsBacTTXfnKPQ7OBg-qO4b7hy9tVnnwh5MT3Kd-Cx-3Vdp1Ded5Cu-lUDK4EkcBAmfauxUfaz0o1jnWHiFPIOK5Sw6H3OruxaTeCIEUqVhdhiqKdO1TuPTqv0GLbJ9FOM5Z-D9UTcFoQFADvUD5zUXH0_Kp6iNxrgm7FksBzmuSAGa2HEeV2OJhiSUOYxemKeNq_mjzRrDeBRI6leapX6XaXDpUybymbgZsChi4ksg0YoRxJN79mAzabK-4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMy6zA__ZvBA7D4_Gi8JrNrlrffDkTLOvoBV8Hr2VubfJuX1JQUOuMoLZIciDn65cb9glH-IopiXuaDaOvzcnPMRWo8dUYeNhY3ms-UVKMQQRJcHlWYBuYtssoixdG5dqkenCqWwvUQS2Q6mHD4FqtE_2ioVQZ_vUCsizFgxDBLEAWOsAutgciNGnOTTisPNLo1dE_OEc8Su1CQ5nXBSjiYXIQguVXTCyZeSVUn4up9x7bsIj11-7dFxH1UYeusaeHnQ27UcXgVNcXaXpNBJohlnqNzmm5HFM-0_O6RiExgWY5sLWJTaGxcduQR-9zkGCJZWDKpZonEeMu3A5Xa0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6fRAXIJKZv4KooSKMnjVYJEX2ecRRAgiTDqDqgz2hrrnnbYvPeORkoARUQpiPZq1vGEtgEUhW3ZfJtGNUcy0xA_r5ftFgWIEE2snb3IniYN34LsdSl6uQCugk_1xNZq_ia-9ppSfL_X0cNyyX63eIEHr7w5MD_3-IdybrW81UZysUXPFM_50S5YqvdOxE1QhD9duXh6a9ecweaTXlewTh8krw6d78SHxsvPocVeRNTI8ZzBc7lzjQqyDTMqgHJCx21L4TX_ekoPCHP1a6dIDiXYzQE1vD-SV3Ax65G1vXVAuiP9-CTRCy2qeQra4et65ZUkNdUVeeOhBYwmpRTE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=q5pdkvfwJn9KSTng06HDF4MMcBc766eG_OYjBbeJcyGI7PHwRyowZvGCe-0qFZS4gbyDivgkmsWtUwSeYrCTy6jzw6hCAptVG4rjErRaqZZn3_OBD-Gtmw4NAMt1bCo64n7RYQf94aKdCzXtnVmLK67YBCiHK3ZuUvhssnqIuJ9gAmE1lQAtEAavHsPoBRdENoiwTZZKDvqWt_CromP3ddXhnm6TFJ4lvufArK_ACsFtPpV8YZkX91GeAgz94mzVuX2y5LQdytzkmwpTMjTMIN69L2zaKXWBzu0qlkYPtgZC1kp48jqpISkSeECnL1SyLCcIq3u06_29j0HjCZZ5tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=q5pdkvfwJn9KSTng06HDF4MMcBc766eG_OYjBbeJcyGI7PHwRyowZvGCe-0qFZS4gbyDivgkmsWtUwSeYrCTy6jzw6hCAptVG4rjErRaqZZn3_OBD-Gtmw4NAMt1bCo64n7RYQf94aKdCzXtnVmLK67YBCiHK3ZuUvhssnqIuJ9gAmE1lQAtEAavHsPoBRdENoiwTZZKDvqWt_CromP3ddXhnm6TFJ4lvufArK_ACsFtPpV8YZkX91GeAgz94mzVuX2y5LQdytzkmwpTMjTMIN69L2zaKXWBzu0qlkYPtgZC1kp48jqpISkSeECnL1SyLCcIq3u06_29j0HjCZZ5tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMJXH61mP4sMqpGuM8DwcxN0HTMqo8yxrtfQl8HCtO1xf5-5guKZYd3yhB0rb5w032d6UxCybZcLUanz6a7HdTTpvl8m6JjMPEmJalM__T_MQMqs2tIyByR_VvU61AUbcZ5DmZ4TCVKuJaB21g2B2GwWu_5JEBtDbUYWI1mSEGRf29EapDqqSmVBH-miv8Fe0q2VIEwe85SzupbO_QRZzDWPQQIZiyf_AbxsEYUqctQSWwpOW8lbAurNTc3FfAr7LXQiV2d9v2UoRJHkB6iSfNxRqjfpCGAJVgEJo2TIGAdBgrKQ96EN4NgVTIe0-3UROhhuCl_CjeS26lJz9bBLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3g-AqnpQ4UauHrlTHT1z1Fi8R3DIQqBxargh79QSTJzjPNW5SNMzByA8Xnl_-CgVHRv4snk7_Ow9wdFOGrTobjyXcXSaSGZghg790wCvWT9acsW9j1i8CbxUnP3Mksp0Khuh3HdEnWFleYK2kk6bIcnKB4oJAC2bu8l9Npfm8KrRLaNBqnqZ6rfiU5wnciWj4_m2GGc9TcCtbSnFajiFtLZ6CtyWTmtUfn4rJ7VUn5H_eio2r6siKjYRuGFDCmGUudodhTksKhGJKD_377oOan_VPeSk5Is0tBxHbtlU6IZx175SPvY_7DKzkcQ3BAYdVDWfuptby4szSg8zcqxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vArpnyOoUeIPlwRedpoItCqXtYnthsafw4Tw5P3QlJzemeVOKSSt6REMFAQfUVdNXQM5jvP2h3J0wm94JwNMIf1rdOBnZu0SVGacCz8aSgaq7ZGCi01X7tSbwLebxOoFQs5UPVtysdZBZGoQbq8CZf8VyknJk8zUrP5tjgdlgvD6MWkPKunU8wN_OikxbFVMoYrQTouSZ8J7O42B_rFFfX51AgKIZkBKepRJ3edZ_YJZuYBdxzRWN1LT0y4680c3uYGNi3RIRW-r6j-K9apuMeZhz3Jq8kOvwJTK2Muh01IT4wRmtxUs4pHacAiE2Tq4G-ByGzvL7_T4o2qbYhj6NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5XL-9RmNrlNeTp2KOPFCgQAsm0HDhpwmrpu7odXC_C4fRP8EjBoaUH_5dvXPrGMP6sBzFJPBm6du4LIko0LvfylZbOmzauUosgbSOkAFSq9ePlj_Umi2a3SQ6zYGKiMLpoLU7dCohUSIu747wGtjiQQ3mQh52fyz916LGUC6jLWWG105LytckeblFuO9T5fI8-SRVR6cdRE1qBbOuxMNZAxB_fMu3N1PbMQhD9QBWapcfctZs7DR605_XnkilTalACPf6wKsHRsQUfuY2Hs8QmsYKELjDstZyAzHV7Y8P54kt5FdfVUtfJmoK1uwk-9Mh9caa7bk7VTYjDJ3zdtcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=D9LlmkqhXkSXxGk3NKMWYmY_dvn9lb4i1BtfRQIMVoaGaw2WjJwhm6rg1T1UURuPPNbPDusQMiBn68n1RegW67-b6uj8j8FkMxZ3JWzidgN7pDis4gLnXpL4LOFDllSX9RLnSSeCZT5lvQnuTOl5B2qHG8t8ebmK69wJGWuipU9OBfFt-KRJ_aIC9aRGtt00hnc5d1paBDzZOrAlnrEwfksqHOhXDcwJ9-TlW-C6E7cK3kAkwVRAElETB2wFhGoUQrSBQyrTIFoovMt-pPnLPYMQ09DbplKxSi0mUJni8fkc-LABWAfynp-c9uczt0SEZ4z2PFeuxuMAu4um73pVFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=D9LlmkqhXkSXxGk3NKMWYmY_dvn9lb4i1BtfRQIMVoaGaw2WjJwhm6rg1T1UURuPPNbPDusQMiBn68n1RegW67-b6uj8j8FkMxZ3JWzidgN7pDis4gLnXpL4LOFDllSX9RLnSSeCZT5lvQnuTOl5B2qHG8t8ebmK69wJGWuipU9OBfFt-KRJ_aIC9aRGtt00hnc5d1paBDzZOrAlnrEwfksqHOhXDcwJ9-TlW-C6E7cK3kAkwVRAElETB2wFhGoUQrSBQyrTIFoovMt-pPnLPYMQ09DbplKxSi0mUJni8fkc-LABWAfynp-c9uczt0SEZ4z2PFeuxuMAu4um73pVFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atB3YCPwI8jVMqu56Nq2N2Bswp65QS5pMrqOgufkfXfyVpLB1bKTlpmTUSmfzSr0Jcb32TGFntjoxSgSgFCaLsjbpGFGGeMmTWt5lHKKYxHjwjLT-JDyJo48x1R_qKB1_Zv1D9KewdF5naYpnyeEuyu5tZfA5LNY_CblA6imq7FcLm3Zh39NS6nyNcx10O3oCf7ZaVRCIAPNWpIWLg3R_aUJ0YeWVNLSZ6YNUfcy2rT8-m1IeuW5hSwg5xaXCqJ5_XHvUymmKnGKwmFrY2Yv_4JQIzoWSCidGkMtuPxQ4DRMTCY6XcYHvIcZ733627Hyi1jw2UQJUj5mJgE5BfVpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujCgpT3ZdFoRAKbc_Avi5iMpGUc0uYsGRfxAYgkO_kPUDSlbXDvL19H6U1IBa8a_IFizHVNS89F-MJ2gHcLADkI7i1dVvLAeuCDLmZ_NEUR2JlAw1KOc6GMcwxSw4bAGWGeMuEjpo64yJC54WaQiN8wUgEBDVBarHDsSjy7hKN7hmmQ9qGv5q28b1FSv8ECm8G-Oaysnerq612UNVwi76izlfYxXYSfRTXXb7SfDtj3a_6c1ptWGidyINwQ9bWLNPgMRUc95XAUqbAwxwjCpBOSvoU5r4-8cITL1sZGWR57yBDB4nisrqImKpjVCgYHBZrUIDgE_Rvwq3xQLFiI0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات
موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور شیعه هستند
و عمدتا به سمت شهرهای شمالی‌تر
چون صیدا و بیروت می‌روند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoCna5CVr5dZZwbUBINTFIuCe8xHUiWpxPKqEnYSlXscArVbByqffWkcwHp3PxOeqJMbxUZXekcmR5D1vyYGrGUFnxIxJt7Qu7dP7aLysr05UnQYPQ6tIXrysUQxzgSRTDDX7h3uunlgWvm0I0Nu37dhPhEUUxp-01_ymGVqyHfGLIR-HuD0mzRJRtd2mt6HGJ-Y4AWyusyWfKn9UQd1j7D9MOCVx2SuYDtjxIEBrRo-bPAw4RRfh1UV6R1ctffCiq0wP-aB_sqgbt-QPN7JBC2--zDT6lvMgtrY5RkCYL7j_hbIn-iNtFGsfEuaLE2AqLItLRbMqESbSyp6AOsN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtP06R86YWz6rcL3TuBt4G2Hx-2mQuNk396UBd6lxOWwOz0ED6hmpmf117J-xwSC5dCNI31WH7IB-M8gCektm_hTNznHPVmjYy4PzMDxv4g2PdmohSAR6LaRcIHAJcwBBQ17k-7vQ0rMN3fEsupO6CIrFe5OBjnzVzgz56kVg5SXd4-YXdeFpFCDB-t0RxHKM9iw8AI_1mf-ojSaOJLiJV0hWPljgSg6bJxjTpDTTW3BGbDxWr23Ybmm7zL21LSvWV1uSxvhoeXsrto6OsiWM7ugddvJcrFsHOv8KJV9Xj3az6W_CPuX6rqZmKhZXWhvDsu8io5z9s_WCK-Z9x0QdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxGYjH0h8AT50brXCb7aA9ivLPJgt2-geNmFeQHG3DSnni-Q4xM8qWz9tgmr8OHkpE-kzxEBIIM1BsztowtT6oPwnI0uAw56E4lMMEFkQmnFDq1ERc8uKNlqBn8RqUys57vGf_ALDbvj5ietNVDWBdg_1KuxDA6sJ2_DvfO5CQG5QzdoBOlCJYelrL5owKd1yZ1JkBs5h01-GU_XK9snHCWbl6k3oT3pgiUeIemZRpm0SIhM78hOrNwyJfqatPOgRKxUjzB6zYbRxkMJwZL0L35GSuFOwuLyCv2UausT14KfGPtz7_FeIdjMcWnOhJqZ6RFOLDzvVEekXDOzOaQD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swAnTshBY9aG5iJxMo26OpeK6EbSImAPLc5SWVQ228gtZt_pKd63bhsIDa3rQ7-70qip2KpEnpdicufb5Fam3Jfp3O8ugSMTqGUbQm66ecuDTU57D0E1PWPcs12kZFmFXdJ5TTvuJttktOfjLAtaj7Zjzp-YbmFdYy6YH6yfXlkncdhU-KEanIvXiRkyUH3UotOLm61VK9ZzUHcAsrLSDsh-Vl8tRA_xncXvZUSEe-3VmeXk1Re7FPFMgGSIs3QWHVhHM1zoBurwOsOilDRSP7PtJS2hRPjZRC8ZOjIO_7CE2hjuuq-3i_bxGaiDlVbiHz9lHJSaG1F3kB2rpTj3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOMwu6RCNJYhcbIe9SGt38M2mUJXJR3kZ4pEt15Q0U5u_vWGodTUt9kChJLGpB_lIsMo_l6fhBQ-KwBQIx_On8iS8zr41N4FvOqPdvoZuydXDyWwWs6Q-9ViUErFNjdgfab8SQVpLoTO15RrzZUvwJluwuX8ZPpoaS6_4ZLDKEesp-Kopdh2Swd1dTDgpiMP8Ps2IK6ut9abzr4huAzBjZ8snXwRirGrt8OgKoNolfOBmC1uyYia3Cdyb95WwI_UPKBc_CxvkUpI29q0oWLw-y2oZKY0S6nNj1ZxGtMLnVXfB8h7I6J8U2EPboW2b5B9nQUaoU5M5tzi3D_1FxG4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pU-jzezZQtxhqY7ObYOheAMG8mL2bEck1qs7qZIicRiPFgH4UwoJzyBgXAop2vsGtjjPLFGtwT5ScgxjH0who_fV_99fcyX41qMfJrz3spUa0vPqOVGoXHSJRz_QYPGeLSoCVpC82jgxCpYQnYefynHC5rdGmnGvh4zw2P7vZx_KGBi3QhO5AMcIryShCqEHXw5_J_rKlsSMIkQ9Sq83L2M63BLGESoXjKHdHM8CoxJTUrPs6b7Dr0Ay9mLNbOYaBvC3qnAlwq78H1IvJspPmUKSRjFCpmtSjb9DJiugBVdu4ukd3cyo6Bgztc-_HZmzPSdgNMeeUUbL3ZzYQ9E4IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته ارتش آمریکا، در پاسخ به حمله به یک هلی‌کوپتر آپاچی خود، مجموعه‌ای از حملات هدفمند را علیه ۲۰ هدف نظامی در داخل ایران انجام داد.
تمرکز اصلی این حملات دکل‌های راداری و تاسیسات ردیابی و نظارتی بود.
ارتش آمریکا با نیروی هوایی و دریایی خود با این اهداف حمله کرد:
بندرعباس
: دفاع هوایی، رادارها و تاسیسات نظامی
جزیره قشم
پایگاه‌های نظامی، ایستگاه‌های کنترل زمینی، رادارهای نظارت و باتری‌های موشکی.
سریک
: پایگاه‌های دریایی و تأسیسات مرتبط.
جاسک:
پایگاه‌های دریایی و نظامی.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q55KbvJcanZzNOEOdiFNWt6v3rrYpt9mFH_uAI2tHd7F8EXyKOx56C3T1yGky_Mh9AeHQnpQdbuH-w7m-9RyBMg7inbRGoaEUShG-ieh0GpQylR3Vvw96hLYG7aKb7Ffv68IbIJHH7a2huuBzEhoYQ_yyS8RzKOsrw1vNRKVtH0-UDOQMoU-YBYfEZjICWslSHJeQRoSeUWXX80ZaRTn6BZ1MOYRd_QXKUDAQhhLW99BugB0O9ypCvwihVFC2JeGNS4OOfOl3cKJ0i0LYQMQWcZLsfoCDU3R9yMEil3sJ-3uwxHLEcLzVjKTIq-3B7vPhEo6PQK_Vz9y_12rhUDpNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGTx7FEH0C8WZ0YiEXgGE7cZAV1FW2e4C20jAyTgbVJ_xF5HmH1hHJCwSfTBW7MifJp0FA5FTfMp-5lsE858h5kuL9bjmiebKftaIl4KuWWjgkMcyxCayylTL6ulbuSir4WGTBbsbF3WqUvXI2A-NWw1sniNtRqDcAa0lYscfIl1wbTjQx76I2lWBNbPG69blPGcdHUoVEMYCiFlSssFHDfX8IN0v71asdLmK6UShBKnB8zRaYFytyp16afBH_6beHZvKg6VuHEz13yReBciMuwSpzWbTGHpYXvgsdzLENiemElrgW6wHu6CJ4ChAcEdqU6fAleS1jOl859AnGYQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=vOIlkzMr_9O6ovhWhUHksvnqWaRfwbIJaMOvP9CDWjImA53J2Ipy3QTEVqQHJuB_TckeNFDnX-gThrLbs72mgRg2Qm6PVdybtNcdXln_y9xJ63QUdFgpkft1boNNV3NFkNZCJSG9sklAGwmzVKAQsTaIreZaFRkF7srsxcYZCu60sZwfMg701Zv5s7dBd12VX2ihF3kxynLRgG9rGq-33VdXb1nb8EpGKfCY4NjMKQC1tbYYQTg8v9vW6WEebGmPgi-Nx_MZPTpOd8eEYM8NfXfoh6a25uKDiWYtlLrAfgPsSuIxutQilQ1rDzuhV3t_BxyugC5WQSq1rljh-xXtiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=vOIlkzMr_9O6ovhWhUHksvnqWaRfwbIJaMOvP9CDWjImA53J2Ipy3QTEVqQHJuB_TckeNFDnX-gThrLbs72mgRg2Qm6PVdybtNcdXln_y9xJ63QUdFgpkft1boNNV3NFkNZCJSG9sklAGwmzVKAQsTaIreZaFRkF7srsxcYZCu60sZwfMg701Zv5s7dBd12VX2ihF3kxynLRgG9rGq-33VdXb1nb8EpGKfCY4NjMKQC1tbYYQTg8v9vW6WEebGmPgi-Nx_MZPTpOd8eEYM8NfXfoh6a25uKDiWYtlLrAfgPsSuIxutQilQ1rDzuhV3t_BxyugC5WQSq1rljh-xXtiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mgksgjw8O410IgqGdaMSfsI_blr1egbhUJaviqMKz34JSGDdDsTps0g-4z4_hxk0Mt96IRuhAaocQUX9h7RAHa8apF835yHOSuUj6iUe6-oUWt9T8_KMNyyI-gSrmjIe4OXC_sBt5itGwmVtwiGszlWR5D-dDNLF6MmoQ1rnPMfYHOdAssNb8LvptkQraj8DRjPdU5xrmwxeYC-4llRrAQ1KUgpeUJDaNMqqgTu6bYn3n9j4NoUdyUC95CcJc1-kie4xsNf5y75XxwS127NlrX92ezZFbgCDNIgrfzITlRmLfPic0eXGg4zQz1446SvRjgsCNyuG82CFQfHXVyjZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارتش اسرائیل از ساکنان شهر صور
در جنوب  لبنان خواسته است تا
فوراً این شهر عمدتا شیعه‌نشین را تخلیه کنند؛
شهری با جمعیتی حدود ۱۷۵ هزار نفر.
🔺
این هشدار شامل محله مسیحی‌نشین
صور نیز شده است؛
محله‌ای با حدود ۷ هزار نفر جمعیت.
برخی رسانه‌های اسرائیلی می‌گویند
که شماری از اعضا و فرماندهان حزب‌الله در مناطق مسیحی‌نشین پناه گرفته‌اند.
🔺
در اطراف صور چند اردوگاه فلسطینی
نیز وجود دارد با جمعیت حدود ۶۰ هزار فلسطینی! آنها هم دستور تخلیه گرفته‌اند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfnRnHtMkDfwLj4Ypp9eD8tofEFHsS7ilCduAFvB-LJiJKux37g1iQsEAkFXBWCfu_uf_ssysXijlEGQR5ZHnNpp3GUvlNTH8wUScOHcHc0-7i0vxHFbkthP7Yn20MW1OyLCAm4DKYE56AKAz0nB1zOL5DvHwQJIpnpBajMnTwzVCJbmvtq7yLd0K3Nv7BBQFqERRCJQMZGC16Kr1OG5pSez7tYTJIsEWzosPWfRMCHBZDqrK-GPq5nwqsWE18Aqv1M6tpNonB4_jvhfu1cJ9AKY5tne8O7tZIndQgm1W2qXWZ7-YaO-r49pkTxsHZ0saMa1kOsM1ajwD0ayqNJscQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=iWdBqWlYXwruuTB4Te0M1epVfRaZfTHe2NiUmkz09QWi1TjqQZvXAzWXusu0StZGdfsREA35jI-RVcS_49_Jm39folkqIr1Ufo6dVJBuAp84Cg3buu-qr1iPOgQKN340i6mgjbo7jEkqxnbegPeDGHHYP1x_3MEezPm1qVIpdiQhIY7K6A229z47nQMVOrzmPzp6p8LYvM63Ze9hx78DzET2BED6z9xZvW3cHN5Tm52IfBCKFHGtlUnVJN1o-iTTD2-kLE5D5b93wBSWyR9498l2ZYUWR3Aip1_BLrlVqtwoqzK9JqffyJ1nI1qoIR6aGoMmLcChU36Vr6qUcbW9ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=iWdBqWlYXwruuTB4Te0M1epVfRaZfTHe2NiUmkz09QWi1TjqQZvXAzWXusu0StZGdfsREA35jI-RVcS_49_Jm39folkqIr1Ufo6dVJBuAp84Cg3buu-qr1iPOgQKN340i6mgjbo7jEkqxnbegPeDGHHYP1x_3MEezPm1qVIpdiQhIY7K6A229z47nQMVOrzmPzp6p8LYvM63Ze9hx78DzET2BED6z9xZvW3cHN5Tm52IfBCKFHGtlUnVJN1o-iTTD2-kLE5D5b93wBSWyR9498l2ZYUWR3Aip1_BLrlVqtwoqzK9JqffyJ1nI1qoIR6aGoMmLcChU36Vr6qUcbW9ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9U_4p5b1l55ppeQxmHfYtoXVtaqQaA1w5JDibazpRykvLxbEMRM5THTARxdENyf5EnVcd3GZzBdjr_WoB3LxBij0RUnv9yTHTFE1nMM3v0-Q_uvcv5Ih28oPZ0cqYXNCfYCjw_FlKXgRpiDYpCVGzZXGulJuLVdsPuOvfiETaq-H5fqL1ptjQzBVyBze3TPa0wKbRz5ykmxGn6FL1nq2cOD-O9T6QhwZH61Eggy-udzXftaknQ2cJR2E-DzRk4Rq_Nb3tXzVc5a_xJjdmljXRRbNqIk1_9j9idGizZQMX5nhJtSEA_Vy-cFL1ztxY5Q1_Nc5A9w28ySKjCHCHEDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5CsL8m2xbGkfrXvx_MqXUeGds82DMdsJJ-jomtZorFnoYPZF9OCgb4i6f7rnDbHiPHROntaMp34LhjhTkgCdjEvP--hCuUknL3XGA24JOkSqXmudiJSQCV1XLmKsGTApObSWfbZIINpGM70rooDUxicMQ4k4yCu9t3TJp2d6bYYRMHxD_lmuycX5MC5NXCzNvibKaqZETDZPywdps7PCxuBXX9pS1toaa-3q8FBCoR45_KM18M0jX4qPRcypOR9Oah0AJCkSq_CWLgxdepAxnKR_86e5mFc4dvG7g5kTPJIVGm14fOyjRHAcu6FCSglPCaQ9f09f_ifPjuIe0H-vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=jYzIpYSWM8iV0Qne7ljfIoi07CNsX7JisfHep6TNGhltakAy2va7mv1fCOyi1X84tHj_IGo0l1t44lwPahgbtjZXjHID7TS4dO8f9iI31ivT8TIHIdu80gfSkR8oHc4xXDKMebxMMVQltbvAR4PuALicx7HMhLqIZd-IuDkTW8Kl2LAg2YK56Ojkyy01c_CNZzVBd6jgVtu3wLSnKx61qX5eLYrPR5RvOMLYhpN4WkJ-acwDXSQK4oz1w6S2nh3QgHROJHBDFDEMPTf-1wsW6JzvA35GsjYTU3eU88fOIeuEf1OiIMJ-3VtbPHrw7-vbTgd9Sd6NPC8TQjHBME0-4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=jYzIpYSWM8iV0Qne7ljfIoi07CNsX7JisfHep6TNGhltakAy2va7mv1fCOyi1X84tHj_IGo0l1t44lwPahgbtjZXjHID7TS4dO8f9iI31ivT8TIHIdu80gfSkR8oHc4xXDKMebxMMVQltbvAR4PuALicx7HMhLqIZd-IuDkTW8Kl2LAg2YK56Ojkyy01c_CNZzVBd6jgVtu3wLSnKx61qX5eLYrPR5RvOMLYhpN4WkJ-acwDXSQK4oz1w6S2nh3QgHROJHBDFDEMPTf-1wsW6JzvA35GsjYTU3eU88fOIeuEf1OiIMJ-3VtbPHrw7-vbTgd9Sd6NPC8TQjHBME0-4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شدید امروز اسرائیل
به شهر صور در جنوب لبنان،
اسرائیل همچنین امروز
ساختمان پلیس دریایی گروه
تروریستی حماس  در غزه را نابود کرد.
جمهوری اسلامی جنگ را به پایان رسانده بود
با این شرط که اسرائیل نه به بیروت
(ضاحیه) و نه به جنوب لبنان، حمله‌ای صورت ندهد!
ویدئو : حمله به پلیس دریایی حماس</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAjvNeg8UoTqFSX9xvX3SPkY35HsRbR9EmOm4vQ4PvHP30w8_L1T5If7FFaRhpJg6FmV2P98ezxa-5E9OcVlXGZlGld1L8m2PB7oUif_zjgO_kNfTN3EvEiThUkXOnn-gIDG_cm_-imiRP4DPTo83nLFEJz0DRAwH3ZLYXZUJWSrUQFqS7h1HJ2TEO1yIoFH3Rjt4y3Gj5rQcgoJ127YUsraFyNydkI5t7aj3d0MqNyQPPVTY_9_FpR6BqEvmBZMvsd1t-M4RndzLAHxkfNfr4DxwCwG3Bc-DxQ0D9Ybs4FTqsS9aSnAdsNJxm_81v-eJGENyNdWNl3jNp_P9OHApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8fEdZyRrivHClMbLfpjJYvZa0CjaOGEGbhDEOk1vxItuuhpxpzbKf0afRn1ZhXU7qwLpSsmYh6wGUWBmmBczMx3QvaCdna2O3fucGh5Ecn2EJQ6xW0x2YdeEJbH1COKrQCMB4egYjZHBiP423tMMBbZObE_o7QVrCdNivOlbEPRGJXGKuywPh3MEOTpSpc62FQZ6wEQoPUTRxH8WbFfX1hxEzuhb-D7tvuFsV4MM4BXZLTErwYJaNc-07kkaTO0jtcI8Zq_RHybmHfC26RIQs0vXJ5qEhZRGkWUpLfaqS_NtMt2lfkIRacMreQrEw0YxiF5OxgU4ZKxwW7g4XGAwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=hJELdR6UZi7LpUTN_ZeKF2TeZ7kbWByMpRSYckEEnZityH9ivvuFaJyKGbaIWZoP58edVZ8t0NP2zBKwScRdhPBKy02a_RfQbuY35l6Nk3M6ypJ5An2XcJGKIGCYF9AnjsA5MlKuQcPVphNAKAAshwOwvEjL3lJlUg_TVqjoVlqpTbUzrqTn0l7Oxg__Eo6VYOVjdwe257At0U79GuyE6scr7yp6ZyRS7cqrT8QQOCyItnTN6AgRbmaIStILgQ3plnsqQXae-B8XhOveI4Ytc-QVy71wOWXx4E_E3iwqChnAErv4avXG5dI0Ic7kPGvnx-RJi0CRvpySDdRSbQPyyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=hJELdR6UZi7LpUTN_ZeKF2TeZ7kbWByMpRSYckEEnZityH9ivvuFaJyKGbaIWZoP58edVZ8t0NP2zBKwScRdhPBKy02a_RfQbuY35l6Nk3M6ypJ5An2XcJGKIGCYF9AnjsA5MlKuQcPVphNAKAAshwOwvEjL3lJlUg_TVqjoVlqpTbUzrqTn0l7Oxg__Eo6VYOVjdwe257At0U79GuyE6scr7yp6ZyRS7cqrT8QQOCyItnTN6AgRbmaIStILgQ3plnsqQXae-B8XhOveI4Ytc-QVy71wOWXx4E_E3iwqChnAErv4avXG5dI0Ic7kPGvnx-RJi0CRvpySDdRSbQPyyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZu6GRmW4X5xeEtN-hzX9aY3r_dmC-PqxsHvlyVKlqfz5pJTTKhvS_ufVqp2P_RvroicLztRswmfcdbQ2R1OB3PlECV6Xo0WwXRVTCtF1PR_GMlbQXSMHJSsR7sY7QAvkNN78lpSFv8YEqMkhm1fzfB7eswQj5E9xOtWR5UWAyvugUdGrLc845uVzMqkAF770kaWq05gkXrPkXx0NmtuOKUJa9osxt17aZ_5V9BSaqDQgaxtm6be1sbMD7pslydBENMxlkPUuLGu0ZKiKPwoKQBfJyefvDwoGWWAGmYMdeKP8r9vZZliiN_5i2GLmA8iUM6vaySYreTSxOYF1_GY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7k0Zfizaa43BhfG8k-RPm2HOMEwhLfXh_wtmRAfh3ilZI2vQDmfPuZ3FhdXCDLyxibHS2HAJZxNDnhgaGZfGrvne1TWq4-1oVIiRVSwLmMNnBorbz3fYUOJeBKh9lLWwHTKV-8djasB9NgCqyagncdQtfrC5EfcjtejD-ccQIk3W6CyuRjvnZEOePWE0I5vtactVr1aLPl-ERxG4KAZAxQxWWkhaKNY_AaZwp2uDqVglZnlNfWzdnmlYcJ31fhblyNWxVeuwiLytbL6LANIrDo5a5kQ2xvUdnkfZFVlC6_LcZynykiIHF93ewQkWKgt2-L4MumvPkkifFqXfuyqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC5E3KGHoVw4NuZhie5MFexRQY7IrYOXFgFScbouOtqolkcmxmjd7qqfCFby7HXh3ktRnBdf1p4eAoCYrJRfVudj9F3d-Zt47E89ELhlVWBV8W56VykhKTiBzANHFyJC3XYj2VRCykCki2sXi_89qBiqchgnmC3j6s48RY3lNq0HhqvKPgkAWWFFy3ElzQcezPF00hc67c7UICjIQiJYfhnLmkBPtXtYa-Bk4MzKX8bRWsyHjJT13YGxnsxb_K9jvI7s2nV2gvJZQBH8k5oS-R9FIuVxPwnVDHDFA1QGPvzaIqYsJQ8xPClQ3yeLHW7MLc77xZEEd0i7kS2azcnwww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LHFSC-u6jTiIjfNQ8P6p0j7W3o9mMoGp2LetwH44ba8X-JCnf0E4H-gvaZeEgyYcarClIX8nOyFppgaGFSsm716ml7Qeuhfyys3qGmlV4u6HHYaxUNNeeDzAk0BfNj7k27ImxRFLYy-vHLSI7vhAYo7iHTnatsRj_s5qEmH6_tB61bxDrHfgB3bT9TRHpjakVpexH3vmC7uyFaBiCQm0DlrT83UjjVE7tTLgg61zBqdYxSB9_LVr7CvtWpwV-FnvtSBdCOLnL7wVX0YI6MHFInMuhpL13FOctoA2vl-_GymC6zvrRB2wQEGDpoWzyt6i5SI_1uf_j5wqvqpFv19QnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/io9Ja7oN9LB7cNZHvoo7k-hX8HekixECwXsFq6606PEqaue6UT72YfWdpOxOFz2fIpmuqWGWbn5pnUnWYcLw3Pku0mvVWrCohzHvZgo6Dro-OwaOL_b5QxYrbpEb_LeL3HL70V2ud-b8yRMGRkpsf-MZOb9hgtPeRPg3e0d1aNQ0MU5NRfB4dukptU4YsU0odSADf-EfeABRUTAM_b2dO3JRwLIpmigmsrUckIAXI612tOEdm1G5p7Ip-A2E28UJATeiyOHlOb2Nh83yU1D7iuGmx1rDWiyvtysDhXVvoDhMuHlETyDsDtgMeEJXdPvjwQU-u5qxGzP7F0EcQPj0KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkcD2tWbnuq4jHBH2G139Q2IyzaIowbZMGSNN9lDEEdASD4A8_TzIM53b3V0WMwuGE-VsmwLV-OOyW4H1eyZ7lgB2UxZw-dfdikKh0MM-yty54YNqWdXtH-VNGphs2DGTt6eHsvszTt7ZF721B-2PzX4NoR9DuRFaRek6D0zg7U4iIgh2giEu6iCQ4lgjmI9PgjwkyCWXn-Uz62eOtHgDDFa1rCuwqIfpxLam1_tpflXCxGv7viNGDpXsfSlAitxhwUZaEfhI_0zvrA6iMDk91v6h31-CHTOvjeE21k9utXJD7d3_0IKdxbmnhprkip-QOlZvL_qcUM4MIWRJDk3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeF__CoRhLeWNtOEnfOVzXyoy31rgkG6znEvn2U9Irb0OFyZsssEb9VMFf1pwrM61QHA0ivSe7JJ7_1JFirg7LbhxrTbEMY4LJPc7Uez77ZwQbjagji_vm31oGvkLplPdvGZ0CxIYYyAQhLFxl238AM-iKuBSN_uY8FnS2UoPO88lk30dvZz1dC8T3lutP8K3uPu07rc6pn4DKZQ6v-mFlJPDreAzhBZAsezHi4s6uWfP--n2JkuLAF80nVadFvHTkzo2RR_tnISXj42SLkZKi8wkbBpHJ_JQNhbUjv3p9LNRiXxuOhJ1UT7gBAHyJBVxToNLuUyLkltJhUNyA60hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVfyDfAVGNNehAYHf10uI_UK7J2jlgJyfAHb4Kxxb010cPiXBQ_vMhpe0DeOeNeGVFuRhpZ2R0_ItMW784De5pHUVmwscpM28xtf8J8hz9jTjcrXnoTQPxEq3A0DxGBZyxC6E99BmndZhJVLcgyHM2GHTyejZ24V11bmN1pG52gDuDrzJGIo1d9963E50Ldhg0juPM0FT16q0O13e8WslAioR4ITMdUi9hPqAbLBROXPAUin4rVNlfnGzc3_ypRgLJE2hGHq_Z6wwRkDphKHMcNppJMi6W65aQZ0IXhTTVCulq7geXvS0dhDgS5_8-ERsJvo6tHNCP5C5aytbNky7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=HXJo-1ESDOnnGv39A3BuE4OqYSpRbe_j3guCZociDnRhjnz4f4UDYvWAc4K3p9-1Meu8HbL9RB5s4j0IIi3t0PurDqoHdSmr6lMljBPNqpOAjig-q5pQt43lpnj1TrHm3eO_HnkH7eQdMJMni7RYEIEesjmf9SJjcUDs3h6uP0ZS30cj4J6ZhpgaUXRJu5gd9xVDHb2nDwIibWQLMhUIUsnqcUXn2tr3QEZFSxDr9hP_tzJ4xFEr7USVjgoJyQcUAmq1ZWo_Pob4O2c28mKLBc4IGYAr_uEMDkqa7Y5GldfBhnwvddYrK29hRbYvF62Cs0Z0ucVN4shXbUXrSglhBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=HXJo-1ESDOnnGv39A3BuE4OqYSpRbe_j3guCZociDnRhjnz4f4UDYvWAc4K3p9-1Meu8HbL9RB5s4j0IIi3t0PurDqoHdSmr6lMljBPNqpOAjig-q5pQt43lpnj1TrHm3eO_HnkH7eQdMJMni7RYEIEesjmf9SJjcUDs3h6uP0ZS30cj4J6ZhpgaUXRJu5gd9xVDHb2nDwIibWQLMhUIUsnqcUXn2tr3QEZFSxDr9hP_tzJ4xFEr7USVjgoJyQcUAmq1ZWo_Pob4O2c28mKLBc4IGYAr_uEMDkqa7Y5GldfBhnwvddYrK29hRbYvF62Cs0Z0ucVN4shXbUXrSglhBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله سنگین دقایقی پیش اسرائیل
به جنوب لبنان،  بخشی از هدف این حملات
پیام اسرائیل به جمهوری اسلامی است
که قادر نیست با اسرائیل معادله‌ای تازه
در خصوص لبنان ایجاد کند.
جمهوری اسلامی با حملات دیشب و بیانیه پایانی امروز حملاتش، میخواست این معادله تازه را ایجاد کند که حمله به حز‌بالله لبنان مساوی است با حمله به اسرائیل.
اسرائیل این معادله را نمی‌پذیرد،
در برابر حمله به ج‌ا به اسرائیل به ج‌ا حمله می‌کند و در لبنان هم از ج‌ا حساب نمی‌برد.
گروه حزب‌الله چند روز پیش آتش‌بس حاصل شده میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9eYVs0L1QQTl8F5WnoL7bfrSG8SCcCRiAncaj7VsayGC4LwIqO4JT_D_b2sUReDXONXHBX1W4BuHj0p80qU6zXRV60KisExmGZ0SFfkPOcvBUvbxAD4a37q2JGrtvLnNKWMA08rFFodeXadCy73Wr-LVdMWTa57iER8qQ3snZVSul2bV6-U6vI7rs3_87K5j9o7lKjNmAwhPfo4xrju5FYdiyWSTavIR5UBRJg-L85PvsA1lBouHLXe64WrrMbpHWRVb_4zavYobLBHLSB836tRlASNb4bz2Xhn54x2mkorECk7gakOja4nqzE9JeKCEwTVam9wjeHQbhuRJb-qxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=AXI6GfEoKYtzN7wFKYenVeYZxoLyC0u-c0pk-UPYi4XuyvSG0cZ_nYEPKz6Fk3yOnWRWNlIQJscN5FUtuiAWnwmGoB_hGNpbqjMmz-CwDyM7TAhWMrNnricihpzHKnIxOrmUy9oRV_9Hal6f0-pcZq5Pu2y6bmTeQS6F4IvsbAzT40M7zKXk39tK-pdFAvTlubGP90juGuV9jqqFuRKXTMj2yxlpyRK8Otx10TuiBRNDlg5jfpuBiYEyrnuamNOSVinvpwQo_97Dg8T-3eg1ZrSHsMtzhUkyG_3y0ScP2aSlaJqbWCxr4WNYNJlWqEocyLL8nVs5Nd3D27WlvAgAXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=AXI6GfEoKYtzN7wFKYenVeYZxoLyC0u-c0pk-UPYi4XuyvSG0cZ_nYEPKz6Fk3yOnWRWNlIQJscN5FUtuiAWnwmGoB_hGNpbqjMmz-CwDyM7TAhWMrNnricihpzHKnIxOrmUy9oRV_9Hal6f0-pcZq5Pu2y6bmTeQS6F4IvsbAzT40M7zKXk39tK-pdFAvTlubGP90juGuV9jqqFuRKXTMj2yxlpyRK8Otx10TuiBRNDlg5jfpuBiYEyrnuamNOSVinvpwQo_97Dg8T-3eg1ZrSHsMtzhUkyG_3y0ScP2aSlaJqbWCxr4WNYNJlWqEocyLL8nVs5Nd3D27WlvAgAXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=vNopzbM7A3aiiwjYeienQYXspxrNP-TD_Au8ECGjsUeWNkmkOc6UcEplyWNXOzs3fILahhMOelwA5q3yq4wQuCHKRKYpWosSRLWamokOyH_vMoYcTmyBsFmhmYJ5pmYajO5zXEUeoKJ-8eX83oVylLKb_kRGIYE8RsILERiLIAbNxI_VROLMR91QWSTsvkj2PTaXOOMMSb8N3Td8sFW4KE70lSeXwlNnU8Op-O_wsKN-56tDGKcRQ-tYfY-29ZVWmVs2TecZXatwrMb-3TvgNFnIsGBvEwdS2TVwINdVcq7C5IL9U2rDeIjrI18eBpcTr-hTAoP_YZOvUkaI75UsXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=vNopzbM7A3aiiwjYeienQYXspxrNP-TD_Au8ECGjsUeWNkmkOc6UcEplyWNXOzs3fILahhMOelwA5q3yq4wQuCHKRKYpWosSRLWamokOyH_vMoYcTmyBsFmhmYJ5pmYajO5zXEUeoKJ-8eX83oVylLKb_kRGIYE8RsILERiLIAbNxI_VROLMR91QWSTsvkj2PTaXOOMMSb8N3Td8sFW4KE70lSeXwlNnU8Op-O_wsKN-56tDGKcRQ-tYfY-29ZVWmVs2TecZXatwrMb-3TvgNFnIsGBvEwdS2TVwINdVcq7C5IL9U2rDeIjrI18eBpcTr-hTAoP_YZOvUkaI75UsXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=D81gvdpU2JU9JoloWv9jv-f6qsBxmtM5oToNntJMh_XbHSMwfzsVQHZLUNMxHI4oDgqZz_JIC10IvyNiVrNO7_xQ-64CNG6j6npID9Tn8WvzS71LnZ-6C0KfVK5N3GNGzLLM0mLIMenKaZe1hstPY7EWc-zGBowd6Pfil3xPZRadLLl2zhGA0BhOMCUTyMQHRDwj4a-QaJtEJbPW1zG20Ixcfcw0hzK8EEQqAa5UMdzPtLnMcgEsmCwpnW5iXMNcuij7vavvFeXT0hOXBO0F4ANJOI-dOc92kwV05Uk4BKGIiK6SWEWEEMs3iHCUQNt35WlNFXo4cJWt4iPVsR-qpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=D81gvdpU2JU9JoloWv9jv-f6qsBxmtM5oToNntJMh_XbHSMwfzsVQHZLUNMxHI4oDgqZz_JIC10IvyNiVrNO7_xQ-64CNG6j6npID9Tn8WvzS71LnZ-6C0KfVK5N3GNGzLLM0mLIMenKaZe1hstPY7EWc-zGBowd6Pfil3xPZRadLLl2zhGA0BhOMCUTyMQHRDwj4a-QaJtEJbPW1zG20Ixcfcw0hzK8EEQqAa5UMdzPtLnMcgEsmCwpnW5iXMNcuij7vavvFeXT0hOXBO0F4ANJOI-dOc92kwV05Uk4BKGIiK6SWEWEEMs3iHCUQNt35WlNFXo4cJWt4iPVsR-qpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANuljvXe2sFk-cL0NWk5zF7oZ4Symmfj2bpGaH9XlX5-6cmoFYqiJdo97u_BvQtVduvHHOVo-stJpnPoRPwswA3gwEdOB2glQcyPBZa-Ctz1Td20v-RR3fwNB0Qw7j8Bh6LBXsgNxDvjSXrdonYYSLvMB4Qf7WzIUwpTASJ27-OL4Tdr-SlFohrUEm5qq-DYK-9Lgk7fePv9g1Dmc2_uJQ3BrTnR5p0KssY-TeQ_tywbKNEs9jECTQTlOxezt-n6-uSPHoAtbPgq1y47j5iHcAEuoSNrgA1PzeBKW6mDSJQRBHEYAMLx0X1S4-YCYajvZak8uD25roK6Sbefcx4NJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGPEdcNEiNQOmMP3QwHGC3iUd0iWcOit3GQmEdZ2nTiGl-fbCNHSzURG_PzCCTLf1ywyGPu_DRoeU0AprFZ4ygK7B_zojPdbGqVt1BmRZxf9hSL54bn0Ep6MOXreqUTUKPk1gCog85aiW8caY48uPZRNXPpdqgVNeuCdE0E7uyUuud0rU-3SAXMFH6SxX-NiLzgVdV-DjgGXj-yML5Yvcn2h-yOAiuKl-pxAkT6CeSbPGTPt-WKkS6wOEGGxu0i6_7ILeBeFjVDLKYwEPNQWVyk8_4NAFY_U0IcRESqPGgZCOnzZgtfI-X54Llr2QfrNOqV9KFAZ0VQVheoSVGA3cA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=fEJFDw-PaG2sRFuBVgSaqyzZ3KjbIu9n9wLF9mccFAQlVoasUe-TKjhHxiP5vOY5fQ0n4ZXHVusoe1SBgKWbE-yV5oUqmdoRmlpSl18IhVehadFZ1ReiTTzAlxGgMQyGSCRltcfm5Y6rsrWcgI5hBVN-ynApbzFEXwvLD9u8XFoFKIWwdhwcMVAWYOOZi3aVEewEF1SMtuZRd-g1xWRpDu7yzL2qU__T5Z3RrMzZZjObv6eNZoNjLNGgvqT4S2il012Zv8QKl0VSWRuuvYVEFxnCb-c--YyXKcyvAh3JnWRNuojNlKDcVsZQ0Fu2hRaHATVGZvgaVKoDf2u6L1A-IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=fEJFDw-PaG2sRFuBVgSaqyzZ3KjbIu9n9wLF9mccFAQlVoasUe-TKjhHxiP5vOY5fQ0n4ZXHVusoe1SBgKWbE-yV5oUqmdoRmlpSl18IhVehadFZ1ReiTTzAlxGgMQyGSCRltcfm5Y6rsrWcgI5hBVN-ynApbzFEXwvLD9u8XFoFKIWwdhwcMVAWYOOZi3aVEewEF1SMtuZRd-g1xWRpDu7yzL2qU__T5Z3RrMzZZjObv6eNZoNjLNGgvqT4S2il012Zv8QKl0VSWRuuvYVEFxnCb-c--YyXKcyvAh3JnWRNuojNlKDcVsZQ0Fu2hRaHATVGZvgaVKoDf2u6L1A-IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=Ng-VbP-DLoRrGpdwokhZS02XBAQ7ncFGb2t1G2qhF2TBn7R0Qkz4oUVqhqSg0FnnVJYoJcms71pPbHeVJFpRIfiSwbniD9e-wnywjmQmvQOZdVS6QiwVWl_DPDAwlUaABZ6r3-w8VDMJRBk-6NOMFrU1ESkxNG6hvsn3ndPk6XntkhduQrOla1R4jyvH8S4mwSdunE-yAvKeMnGsfAs_rIBITpcRFcYjbzMDvtMoeyzPk_zTTQKCQakryD2ieexMbVcM2fH7KQy2xrTZvgir9lVzsXNEC8CAC9s-c7IP-36ur89ZSPYNEGp4FupPMZTRE_BXfa9MRwx9QZJmEB1k5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=Ng-VbP-DLoRrGpdwokhZS02XBAQ7ncFGb2t1G2qhF2TBn7R0Qkz4oUVqhqSg0FnnVJYoJcms71pPbHeVJFpRIfiSwbniD9e-wnywjmQmvQOZdVS6QiwVWl_DPDAwlUaABZ6r3-w8VDMJRBk-6NOMFrU1ESkxNG6hvsn3ndPk6XntkhduQrOla1R4jyvH8S4mwSdunE-yAvKeMnGsfAs_rIBITpcRFcYjbzMDvtMoeyzPk_zTTQKCQakryD2ieexMbVcM2fH7KQy2xrTZvgir9lVzsXNEC8CAC9s-c7IP-36ur89ZSPYNEGp4FupPMZTRE_BXfa9MRwx9QZJmEB1k5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg1heIeejAFmlRTal9RZmADtJOCjcrP8X1PXPt1fry2wMofwwc9svK4rIUGswREm5Yzb7oOERj8A4vPqGzYJN_9djG50NkAmxEhNEfROAf3hINRaS5qre7REhfjqJE1qcro-RPZvRbeR4pfEfYZM2IOcn8x4LIqo7i2eaUfB6eS2CZQ275NbOXC9-yhdyKvIoQEtJk7OXjuhsHHSb_HspGhfu4N6on_Xg1yFUzEiRePNul28V59HRIslhEB0eR1WLDIEyYcC_Oc0h5vvouJKB4wH5nmvbYrENaqMpzmuvK-ZWMn42ISUt4bazPYaKqXXZgmS8_7mFNzPqbfsZ_dxnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=KsqoaSqT-GI9LHv82k6iYNmuACqnSqwaoFFMyImdO9w52Zu5d1pG2vldu_uiEDUkq3CMB4qxAm7535lTYpW0_EG0pqTEvvjUp8Do_cN7DxackMGeSWd-EHXbJz-2bXq3G3GkQiUeR_XHNuqmj3-bJt5OjTalNwq0RNkGiQV0e47hbaSeClcHgxLKeKLMb6OTWG89SPkm9bSh_hJosogsRHkXu0zn5pY8Gnui-ARERar_JED2Khs1owSiqfTuxk2WhXUhKAMozDwCGYzbYVFRIUHdTEmYV4PVwOnwre4_pQEgC8DbL75-WfidgUEP1WjDDJ1SZ317LrEAvm9omfASrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=KsqoaSqT-GI9LHv82k6iYNmuACqnSqwaoFFMyImdO9w52Zu5d1pG2vldu_uiEDUkq3CMB4qxAm7535lTYpW0_EG0pqTEvvjUp8Do_cN7DxackMGeSWd-EHXbJz-2bXq3G3GkQiUeR_XHNuqmj3-bJt5OjTalNwq0RNkGiQV0e47hbaSeClcHgxLKeKLMb6OTWG89SPkm9bSh_hJosogsRHkXu0zn5pY8Gnui-ARERar_JED2Khs1owSiqfTuxk2WhXUhKAMozDwCGYzbYVFRIUHdTEmYV4PVwOnwre4_pQEgC8DbL75-WfidgUEP1WjDDJ1SZ317LrEAvm9omfASrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
