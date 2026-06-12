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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 14:17:28</div>
<hr>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzb0Pcl03Qh68m_aeP1jNKBdkDOSbZVwxuVfUTcFLuW1Y2XQCZr_HXYGeI4RvVVYozacCN2V5e72k0u9JRDGrd9cJGGZGC4yd-h4dBQCzcfOO5X_AYndSJ8E44SBJHRqLBP3bjKhZlEWWQl6sy9hQXUN9BKpwIra3YbvY47DfTfXZDaOZVM6ftYvsLoIAtCa-HOiEPbtCIP3LU1ywhTi11n5H5H8Hk239YVOiCnqadimOun3ZsDwxQYfMBgZHRh5X6a4-L80K8dEwcjQxlHCKdP6XzozW-3zUyu3o6xHI6egGeGQRaU5TOvCJVtsoltvPt2aK5Z680eRH_ZjOWul8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=hKZOZSLlvmPJgpQYIu5hn3Zy1i_Vv1mJuMt_3coQgYMa2VLKrWQHQq8xwxVyWZ_xtJRF_n5MSPN5h19GTJh2sTRPkHCmknMwxRyWk5okBrxrm3pIjWv_auryvKXsRQEDtsoPBowrTag-XMwRnK6FwJyesxYr_qduVVorr61DP_7q2pmJ4kpcXOy-no5vOu0PS-C_cDmc4js4AX90zTHRS_51V3tgyhSmpXzng6fZaYHzZm85Pk6s9zPlS2RkCxugQFGc_8YryW7hxPpZyT6DczsRYs9Qed0tQlbWw9B72Oz99fZWLRVyBR_7eIEmqui8A1y63tZg2oGzZflAeyLfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=hKZOZSLlvmPJgpQYIu5hn3Zy1i_Vv1mJuMt_3coQgYMa2VLKrWQHQq8xwxVyWZ_xtJRF_n5MSPN5h19GTJh2sTRPkHCmknMwxRyWk5okBrxrm3pIjWv_auryvKXsRQEDtsoPBowrTag-XMwRnK6FwJyesxYr_qduVVorr61DP_7q2pmJ4kpcXOy-no5vOu0PS-C_cDmc4js4AX90zTHRS_51V3tgyhSmpXzng6fZaYHzZm85Pk6s9zPlS2RkCxugQFGc_8YryW7hxPpZyT6DczsRYs9Qed0tQlbWw9B72Oz99fZWLRVyBR_7eIEmqui8A1y63tZg2oGzZflAeyLfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OENnE6emzRs-rNh4mf9GKANY7T4xVIQqe5FSYR8mSKPIZvMWVRh8yst5GSfb6WyRAxW2I2zpJ4FZVJprAbfbGTD1LTgsEdoScAm1fFd67jAnAhkJwB_N27rQEn1T-DhcVEpwQHnNDkPDfWTMZEt1vGiNOr4FApRPIXuSK_7fsMo3rUVKzD9r91vQhrbsTpOW8g1-Hve0m3p_HUk7w18TLDqvwHW8fwE4Uxb6jt6HPp8-0Rlnju_GNvqEj1mliyeHqV3Wnl8SxNYBO0g2EzCs3WiduYTXQkmkQV9XmfGNL9rovFuogf4CGgKR_p9DJ6e8HSKgSPueVEkZJjpt-MGvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN5qa2K1Q6afAndskOz-9D4lLeFXOpKbeVnEbrnwtPxdWesdYsfUudAK8g51eXLnozGLrJIOieK_S1iuDXQ_dmajZSl2G6KFKIxD8BwgdskxuUAKeBP0yGCu3p_YrhK7_CSgHodEp7fretDtU4NFw5ui3W2oNohM9Uff4wZ1yr1rZ1dF0iy2wriNK5dcOuviaZoj7ky7N0-H2FUaVJRQhrt0QwsgJYYxrEg5sWx8RkBXOTpiNqAqiqebAi11i3vbpZl_RIc2ZG7QO8qH2iyX5bYj__OnNCCLoiu1r1PkEXsq7oMDLVaT-iXRC8wfwmC7JxRJzw7IKbslWPSnUyR_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtqSdSKpRFXwIWDMeR44L08-OgDfkD67WHOXuBtp3VvZ1cclyiC-YpOB_8-RUZpPCqPxTq3n3EqTl-1K7QXkVW_ge_kFiaW6qFjnFVZCAg8_Xe6ZjHpZAU4WyzZJa6wgIQwepjxEUceT3AEUbLS8T6aTKB_7KrQmdLxepS3LAwES2qvtkyuK15DQgdNU4M9RR7ONiIn480x7htYYLEb1quUv21MnQ1EAUoX49Ar32CGF0pYSed1zJRkMsqRQiGmAVGP6g7yyMa5S5AdHQqkBXTw5hRlyd1NRXB2eJUB3T5mqOqIqgUC8K63Ewba-tBehuUEiAdbdjGgwjsmJWdy3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csaBlTeHN3QgQ5LkyNMWUzsPUduhfrqUGAWZ0fUWY8pzzcN1H1LwY8hxjDvj7cd8kGUUG1aAKKUZlp2oKzQae7tRYGsBacTTXfnKPQ7OBg-qO4b7hy9tVnnwh5MT3Kd-Cx-3Vdp1Ded5Cu-lUDK4EkcBAmfauxUfaz0o1jnWHiFPIOK5Sw6H3OruxaTeCIEUqVhdhiqKdO1TuPTqv0GLbJ9FOM5Z-D9UTcFoQFADvUD5zUXH0_Kp6iNxrgm7FksBzmuSAGa2HEeV2OJhiSUOYxemKeNq_mjzRrDeBRI6leapX6XaXDpUybymbgZsChi4ksg0YoRxJN79mAzabK-4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMy6zA__ZvBA7D4_Gi8JrNrlrffDkTLOvoBV8Hr2VubfJuX1JQUOuMoLZIciDn65cb9glH-IopiXuaDaOvzcnPMRWo8dUYeNhY3ms-UVKMQQRJcHlWYBuYtssoixdG5dqkenCqWwvUQS2Q6mHD4FqtE_2ioVQZ_vUCsizFgxDBLEAWOsAutgciNGnOTTisPNLo1dE_OEc8Su1CQ5nXBSjiYXIQguVXTCyZeSVUn4up9x7bsIj11-7dFxH1UYeusaeHnQ27UcXgVNcXaXpNBJohlnqNzmm5HFM-0_O6RiExgWY5sLWJTaGxcduQR-9zkGCJZWDKpZonEeMu3A5Xa0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsdVABimqhqNzzLhON2qkFRI0UzXEjtVVYviCsO7CbsjfepW0EDcloURvccZ8hPsaZKExzfr1UgmxWaguojofUKWO1q5T785LhBIpO2yLVTFhi6TEwyOXNJJ5_bIDTHHP7474flg3Xu9x0vnK1MjurVtB2x8WQ00MXfeIO_XQxnC_jVT0GMMMcrcWZLWgXSvu_PRKBSHtRPHvv-r_NC32GWEe9Xca5POJ5U7LE4gGdNpZLCzpaVIsZE9kBK6iU94cy_hKEUOTCj2PuAEDQmrcIstYq3rC9IGwK8C2bNtg3pG2Tjo1xf_nXteJ8UFolZLVRQg8WLYXbQXEGrdFNSauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=qN5QKoNHdgzOaxqiYh6im-w72EZ_p8nzMYz_JwUFBrL5yTp_P1701DB9moBd5OvW0ZQU-_LDSg8Q9ciiayocbuwpkq-Aa119XONgGhf3f7J6BMqE9yBAXFkuyApshHM9bc08WnsmlyM7zA9GtdOz2QeEqeRx0a4kFCOfYHskFzIkRo13yPfHp8FhF9mqbiXhmVMB34n3tDxfQ5F2dsC3jnVDmdflSlgesQt1TluoHbn2qBCQ_xzHo-diboxPpUy6xv72ef0yNmif-moyggVGGMgVDez5O9aUevt841CAfqViAlg3Qe_L11846vYqLxRRlqUeMxMk7RjbA31HdyLO2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=qN5QKoNHdgzOaxqiYh6im-w72EZ_p8nzMYz_JwUFBrL5yTp_P1701DB9moBd5OvW0ZQU-_LDSg8Q9ciiayocbuwpkq-Aa119XONgGhf3f7J6BMqE9yBAXFkuyApshHM9bc08WnsmlyM7zA9GtdOz2QeEqeRx0a4kFCOfYHskFzIkRo13yPfHp8FhF9mqbiXhmVMB34n3tDxfQ5F2dsC3jnVDmdflSlgesQt1TluoHbn2qBCQ_xzHo-diboxPpUy6xv72ef0yNmif-moyggVGGMgVDez5O9aUevt841CAfqViAlg3Qe_L11846vYqLxRRlqUeMxMk7RjbA31HdyLO2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKvccDgAv4rOl0NbPG_zjWKf5dPMk1MYZBMbsLQRnyArw1X-q6Mzl3Tch4agG6plcYbBd0StDbQkDagkQIrk1a6Mvpw9IOBKPX1zQpnPLU7akXLUUtq7jjbK0qVFlw87YJGvfM2zLRM-kKVFbS5sxvrYBiMcmG0HvxhfwiaVpoqbT2hPkLQGM8D79JlwZzlLXc2wT1IptwqQ7Yes68FrXVH621PT_WKot6pXzTxlfvFIBiUHbhaSNbsHkpTQfPsF8M8tagfZ_N_QAo1CTI8KePuBdCAuu5vSkvloMuLWe92gzt9tAGN01Di1nD-gZQ7vAl0ktgG4C5ug8_tzuFQccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSWs_ZoQST4G7hufjELRj-NZhfighhenvhAtM3pe6ojZnfNAkGTRADV-ALzA-bR19hRFYAz8aIkWaFCubnttXuliQAPF3kyNStIfCAtLEI2YuRtRf-N1Rp6Od0KsIpHMAc2c13Rwje2VQLR-98lrvMIbYGP3WLT70jNiDN3UtOuhEZa8PBglimxjFUtr8H-9jMCOed3BKQcZLjG6f4zHEtaALCWrdp5KVOyo5tF2-NGVPULJu1YjCDQFCuDVCEc61CCENIhI6B2cDD9QVO76X7TnEdr6nc-J5NRd_3aGgvElqWipj1cQr7Dh090W7fdd5Ewz30amxv6MQVs04akCnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9MU-JN5tDMTHrasHceK_Tz_k44yVBFf7CznZt5c3uIUIMmORHaFmZdLe4rRf7mZ-0-nJI6Fwt10utQy3Mde3oeTdBHDe2yqkW2BbJlTiJjYIewJBB8pv6EcBXEMuNCxQ-tQSFg7aAaXbyTXW-PCDRwddFVRKN7-rmHGyW6Y-mZMcuWufbKnLi7A7x03ahV3F0y39SyILyxUsaW6uKh-lMPw6ZgjW-NQ08ELILN2VS76n-n2lB58OUbCbw2AQ3KYB3LjagmdFxECbv9T4znrNRNzVKyHwCD0POuBykU8JG8mPVRtNxgNzl7v2Vm3_qMQiIVQMSm3VUMd7mxmkG8gew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tr6yb1ISNLteE5Cb2b2iIzA0CeL-XCe4OFnecfKLZe1soNE81poulSX3jvLgbOl-e-DL2SPAhJGXylGtn-PTQGyeeiwCcoL4uc-HCylTLBkHnUXNuRT7RczdqNxe7DMm7-oayLkT8aQiakLSkrlA_bQ6NKPkZwpDoC5l3BPC9ySK_Y9lCP0b-V7JfGXTgcyFBPGPWMzi3_XUH1RIRIaVlqxli_CBqwsLcdLXxLEXa7ksFVDJfLCMllXl2bIXDp9SZziqA382YXZn4piUEBDpTWRi_NUMNgU19CvrRfjbMIlImLE4ToHJRii1FdSptcOmQwMaObwYcypxffFgv2WIig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=ekOnioQdUcdVi2zP5U15MhZ9Q0VMKXjrnBgcZOiy5aLcEo1jcd1XexStqdB3iRJJ1Wn46XhpGMlGh--p0na9kY9QrRC8gqEqNfks_nSvZQ07GiL8Wl79O-UduN4c9WQM-UqNhz3HkblAhepo9xtLYrDAFL4upB28Fdj2bnpLynZK1kLEZqwDz3LvfgPCu40jHL8l_KPNz_GdWL9vJaid9g6tTDbvIM-GlQnRXpLmi8lbLoa_TFmB7Q75Ta-9ykirJkEKbY2HImYLlwM1LKpFR0GqD7S15WGwzGG2FOkmpjfXA4iy15h_7RmRzcowEwbAG-YAXgLWzIS2sQhQnlZzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=ekOnioQdUcdVi2zP5U15MhZ9Q0VMKXjrnBgcZOiy5aLcEo1jcd1XexStqdB3iRJJ1Wn46XhpGMlGh--p0na9kY9QrRC8gqEqNfks_nSvZQ07GiL8Wl79O-UduN4c9WQM-UqNhz3HkblAhepo9xtLYrDAFL4upB28Fdj2bnpLynZK1kLEZqwDz3LvfgPCu40jHL8l_KPNz_GdWL9vJaid9g6tTDbvIM-GlQnRXpLmi8lbLoa_TFmB7Q75Ta-9ykirJkEKbY2HImYLlwM1LKpFR0GqD7S15WGwzGG2FOkmpjfXA4iy15h_7RmRzcowEwbAG-YAXgLWzIS2sQhQnlZzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzJopTGUUKohJoSUPLB8K02k0yklIugSz_4dz4Uf5pD-gC0r9WlT-OYIUWPQjSiuPsl0Daa5ph_oknDCLq9BGntrrIDeqR4N6135IBOCIdcGUw9fB2gCxETZdWyHSuZIF7UEk7p_zinAlxZX2IFf3iDS5SPKN6rwqxqPPeNtA9fLRj86A8-hzClgyvX-_EREiIoanPzfsanrZ3pBYJGNDJq4HjOBqMWIX85wZkquvvh9WXrxoslRK0rSoqOOtvVbhdXvIzP7ustET4JIRGgGl927TM5q7pmPwECJPpQMsppYqYX24u6aafvkgjxIrtJuiLapGbsiXSNxcMy2J2K0Xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jClK8bfLOf9Ka3PLUvTWeHvR6vj5PkzuGxI91MX7MTX1PtW1lJRqmx3wqy3IKpEGfm37AhsqxzW2DiODCOSHKfrWooccv_G34_E9L7Y7DL4B07JgKwFbrEOARHZBfgcvTfh5gOlzMCp5GUSXx6s3u-BGOvw5ba0DVzXylAnXuDh_pLUUYu_4vsi4iwznQfbG-hITuuS0Zjsk1iy7THegH6mo_iULnsD8Aquosl6Lrpjonys007jVFp3eTYyGzewksbVj087Ov9xTISRUMspHwTFQ1JgM2Z5SBoGxmyRJg4DAiTB9mrshPmcI-SkrFxjqVaLC5zS0O6hLQbzTMk711Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NS4p2wP3htbs-MLqv_KCEgdv3gM3pq-OlHp6rZlRrjly-B3IfUJ-7uy0rwAx34LrLXANBqtklr0HWxGY-2NQv8yoHqCLBN0XRPmX5LL_f7KfDc4YfmidNDv8xbq4yYP8821UOdYGpyIOp7b8l0ELaoTA4lKmLGKDJV4a6qY1hW7V0Yr5vRvjY7eequLBkJWBBxTqE5l7jwnGshcySSs8z_Ti5pE3Lch15KCgqkhagep6OPpFWLNrZoSX8YDSr4dWPeVRWFIkXET8gC6ffNUPHvO5xSb2-XFL1wqoJej37df0K8ohFyCaXsxyCudAzT_96xlG7VeB1-yKW-t4YCYbWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZ5rP3kC8-m4YJLkQawRYJHHUoMILY8wGSDbrp3FKdO9HkBI13Wo-UiS3ZWTxYk6Q99_j1zOPiYsrcl2uhVUnYZFjwGVVBlK6TZADYgl7A2vRDEFeh2bt5Bcni_r32M8GvbTMgOvrnXx14-iq63Q2VzHz7zQdzV-4UKquJ37R88oOIY6t2Gg8jF5qxFUAuxfFZmFgGy3kII8AcG8WTO32dWHlyK89FzzT1mJeTRb614H_nnu3WikINQ7twsdNa9GENNdUw-dD_qGBCqmH7VW7U6hpw6xY72e87oNcwN1KlgYNj3zG9wUo-nmJTL3nBMa3ivu1VEJKCir9TW05KvPOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY9IuBBLQ3gmo_v--ec7rMJo3nyGA558zO9DQbh0p0m8tEo_mXp3QlrI4Uz4cJi3VUQxsDB9P4Hx4T66j2u0mlgzQybtOFi6kvqRolfR-iAbWFYtmY7WguK8JrML40r3KWb2JGqvqX8IoHZV-3a9s2Ed5X5zUON4YX209yLW7NnBBrpCFAaghD4g3VVeK8aVfgAcLClzfKQFpsorZf0Nk_S0JbvUnScbaXmBbjM7ou5UB1cplcsqM1ZMaUfC0zTsyQR1odCdbRTzQ3HhaXerdVlHDLWM1X99aCjbTazoklpLeW3mUf9TsgRaiIhIQ1R7fcyaIxCKR0hJOgWOoVCelw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLHaF57tLOnw-iorz8VNBFuqvcmjy3hDoHRqUDiVCoV3eDLMXK_nyHC4HOKAZBbFeJYOSyolCVZJ9LS9nf8JQi5UUicTbsWFSCGyHWCPohcO7Mxbnlh5GgT8Okt2Xcf2l7NuvFW_JLUBLz1Q1Jmmq6vg0M-rx3cTiL5vqTp_MTX2wfF2Pc-h-vl7OA3I4YWwRj5nfULZHfLary_N67pG9Tac9erlbienhqK3OIoYTK_cXJ4Bc51wCy7D6p48oVYmIXMSdmtPi9C9dg4Nf3X9cgNoPp3j9UdF4REs4SJbN3CW78odzf7MT3042cnFeoWzqFb9vT3o2bnaKyL1fGtZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qliKucw6PdZhhZY5M1B_KboPF7DRV3NkfY5qpRIOvuN8ia7U04ajm8AJRpr9fkTv04fBrEa4jVUZ_1LxsXrAaoFBWbmKN8n3NB5JgZhx5Ugmt7V_29-uNCzhZSifAUH3X-8CTqM5Lt6p6bRG7SEcnmGDdgI_cXNk47qcv4gD4FllfWNGERP9te0yM3iWSBmChPGUddzMyckv6GBhWN59gzSkv8iRjeVH4MrHZqfxLD2_gB8TZZ14YhfbDgkcGKOoG1TAqjJPROJNOzuUyS40ZBAnCmlU-u8cicZ45oCrq31ss3jRw9y3HRKCrDbog8lHtbDXATQfMvau9rTW8-tmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1t_FRUoVy3GHbYPJrwkZZoJfHLnDzwXCMYOjhZ4Q3Rg1Ck1X-_lBBjvfX5GxgAYb-X0fFvyxVIhIn70wbptCn07PBTc66zgSrKqHudS0zTxULjZmvqBYs5NbwV-we6i0MxxHKA49HgAyLlJstVC3qbaAe4h-MV29Ks4048bhZiY5tE8XuZx870ePAvrRDsShhBU8N857Cznjjaj-kt-SuH3JoMP29eAugxzlnzMWey2DAfX9u983623H2r_zP7z3Yi9vhF8JNXl8pg76jgQa574fLnR5j8GFE7zNnHcAIaWeW0QjyoRjlv9AcnJNUfCf_CXjGQjAgBxhihVWDO_xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsDvj5WxFWyx4b3e2OM832M9fG5_CS708KLI1aiVtPt2BHNpP7KFfbGiHwCQpECwQi0LP5wfDRr2BC66_I3QcHU1UV17yle56dBxR4SRLB545CepFLejhh_aBtvU_HwrzUeRX85DwG8zQUK3VJZBUVLQqfHU5beHJfK1roC6ntu5oVJLCcQ4hGStLQGJk5VeP9kNBVrItVqBtTw9khDPenNF4uYduYvun5QS0lHO0L625_kFmv2bt2t3JhzR0bHLpLWxl1ezySthVm2M2nal5YAHPBsX17Pe9ZRy_LA8diIa4ijrbCjvnbBllxk_6k_caLjDxpkQ2wF_Ue4nhrvmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEkRdIMJMUggrpvTGuJu6CgpGlj9u52-O8LL6W_FDW4j673kY6wpONnRKszyeSOpAaI9mmaQTtQI0-610cEDEY52aPckmebsGsIXOXtsMfKO13lANFunbZkXL8nsQLOYew3lWoFv0V5UJ60ywtm-a7KS2s0vN_-VPDKIO6wAa004STdc7Ggd8zsCnRkkZaO6PKcIVlvchN16jylo_VBQomIntQiKR__kc7AqMvCamzIJY1vvxFXl9bWeeXL1duNG1eAsuUWolt1cOwLwIvfzLbKt0raOcGLKc8UlVorPFwJqTAIqF904it_mo1ztfm9mSJywkWc78sOYls5wlCZ7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=WxM-IFsGZWwWKr_P_4niStdvaDyoXWxnbXG2a89lCZEbtvl3qWAYLZspUPX3PKh6OOiBnTfmLwhRetm0Jr0iemhV0nnRspn4fcNCjqu5CJpGklnnvHac2jjRktEvlJFKmC3KoF9ThePQwAWvD18ZB3AXi9oZffI5tQ0FBhkuVxi6QPD0iHgA492UbH7P1qMdfOrq-eHvObW87s0m7DwpB9e1tXAMLliMjuKhNSpLq7CJSzlaBZY7fiApEZoGqKwieifh0b67VLMBSo6m0T09lNF3sPDZNc-M6QszDtqIT8lq8iCuGQFLdEF_S9LSITDmxbyLCQdkrrLYC_Q7S4SeBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=WxM-IFsGZWwWKr_P_4niStdvaDyoXWxnbXG2a89lCZEbtvl3qWAYLZspUPX3PKh6OOiBnTfmLwhRetm0Jr0iemhV0nnRspn4fcNCjqu5CJpGklnnvHac2jjRktEvlJFKmC3KoF9ThePQwAWvD18ZB3AXi9oZffI5tQ0FBhkuVxi6QPD0iHgA492UbH7P1qMdfOrq-eHvObW87s0m7DwpB9e1tXAMLliMjuKhNSpLq7CJSzlaBZY7fiApEZoGqKwieifh0b67VLMBSo6m0T09lNF3sPDZNc-M6QszDtqIT8lq8iCuGQFLdEF_S9LSITDmxbyLCQdkrrLYC_Q7S4SeBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0XmpkteA2bt-zoooixOIRflxQ6FqAyzGN1txwWqiZu12qVlioj9qgAcgZIpqQK6pukf58T9jgr-lw0Wh-z0KIkLFH-SvU9Ff_TbAaEFree1E_pfoCyN1iSVay13XM9lcca0yUz1b7O17S2H8VY3lyQENUydjDzSoT8zDkpBWugay_l23PBeS2S_w3DOcrJIJiCwsZzD9Msse6-7gIQTVF69sc51h7g7vtcXgjzTedbmxe_5IPV6GNPP1hjmwfxP62tZoaGDs0HJ29oh324dqiWnfSmhcxbBgY8j5myAobuKWbCCYQU3pIoGmskjl4kTp7b_2hUCJlwHHvARljKpbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e72Is6u92WU280biqZTNLWf3TgMRYbJJ3StT-NrfpiEocFml7zhFLZbqaezFIzqx3A0pqUQeXnMw8deF8kQrLo2g-7helpmBnLq6u3T_Ow8XQ0zK8GEAwQrm-0krfEx9BtvZAdLuwiEDJ6OLz6xRFwyQwpRSh7HoXF9qnMbhzbQA23n0TJHaj0XqH-vqy0efP1Jxiy0kiJuoP8JDzIlMHOS6S5PTr3OPmn5HUlkXkVi_1-z_0KvEMxGklhUkoejnbpnhdAbF3SVKyRsAfQ_WAChS1KMmha8fXNJ6JbJ0pwiiK0A0QQYot-mXyoYgl2UDdbuW9MdkpjoAUcpmIom5TQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=TkVmgAD1TvcDj3QHpQecKjPRF7y6qoPWdmd1t5Mt9yM0awMr3DZYtbaPVcFkRFGFZ1EXox4TZ3_BCh29pCyzCnd1u6S_fTQaf1jeZDbOiQpRhSNSozBI66hlnvXQ4SfnXHruVO4CqeLtOWRpfQUbLEz8610ziXG0xEVueaWSIz8IyNHB6Z7A-Rjyjui94og7ycUAHTu3UEti9AWV_FfVa7c23Whs5GOHaX6iQp4QpFnZIa1YcYVK8H0gAi-0s0CcJ2eYKXBRVyzsVO_a_bA_rBBEs7PCfnVQe-YJdFWtWeIT4gt8xF1cM7l9xMiJHq9KzikNeX8JNw8fHH_IEgi4kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=TkVmgAD1TvcDj3QHpQecKjPRF7y6qoPWdmd1t5Mt9yM0awMr3DZYtbaPVcFkRFGFZ1EXox4TZ3_BCh29pCyzCnd1u6S_fTQaf1jeZDbOiQpRhSNSozBI66hlnvXQ4SfnXHruVO4CqeLtOWRpfQUbLEz8610ziXG0xEVueaWSIz8IyNHB6Z7A-Rjyjui94og7ycUAHTu3UEti9AWV_FfVa7c23Whs5GOHaX6iQp4QpFnZIa1YcYVK8H0gAi-0s0CcJ2eYKXBRVyzsVO_a_bA_rBBEs7PCfnVQe-YJdFWtWeIT4gt8xF1cM7l9xMiJHq9KzikNeX8JNw8fHH_IEgi4kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AFGE8aE6fh8m1OVISdv3AsdiaZgkOSN2_D-3iaVzVdbjaLYhhqG62au3TRNI2fgZ9lE4RB6DjwXS14vwWvyBPQSGiThn_GDQ1_NDEf6JE3hEPHt3mp_PoYlbPG47j5MDJAOwxUPaY0ly60x-LzRVt6sXgH6T5rHtOcanJIv33tXgf3NaQBgoPkSb_qBMd5x0GvAy0yEGDn3UZGxwhnN6FmnRpKOvRGVm5XSLeXFRP9mhM4N0WhjlyMS8erNF0eWdkgHwX2fVOmZiaZ56-8zw1DE6AJMkmZo9cT-hJ02Kbve35Bl_jT1MIpjf04x8iSV83i6tSaKq5rGNvCwYEycLKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNNX2NKilXsdNEGVus9TyPgujXAQk-U0r4WIQ4ueakNbzCjp1ZSt3_DIz5NW8igSH4b_AxBVU2_slKO93PJLzxgr29tYNyGitDTp8hy8MIFY88oN0fg9QHhafq7rW1Ch7s-TfImC0Q0v_lVDDMha5E8Gqe64fKpnzgyBXMJTlSSUXn1JlpD_3EmivhhmQJlP8NTYzDAiFCz8WdgajNgDOONtehJkiB7ADxSj2GAuJovkp-AYev2t33PIkQtzNnit3OK1Z1pNJiw5PNXuTTmS07pD4XKDWa_eihfklqG7WswRXZMW2ZG72_r4LOD9b-rX05VZVX5DGPJhJCuzCv2YXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=PMio4rH4ltLfP3r6Vrns6aoHNdohvYHtYGLx5OiwtLKQWMUljcZsGlQQnAdtS3_vkeGCiRx4NuiUA_NSKKYp7LuUs3gVvtv4ufw189ejmz2rb3mCM8LfIQA2xZXJQJLH0Jgl4_6jA7z_QTDJ7MKqoyWQbemBv6_Ua1ka0dAAK1pryrLfjuAGNirlIScPU-NEEujtM1kyDfcmj0RczFdTibqnMfNB_k7E5rHPUlzwQGljbOGuXYhM1wca2C52wzIFNbcITLZjIZFikMF8GLh7_oUYz9ZhrZScZfWFwS8eeDlS7dBYoO85BG2UTqvfoREkf32EEOpmeoZkDJmTT2Y4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=PMio4rH4ltLfP3r6Vrns6aoHNdohvYHtYGLx5OiwtLKQWMUljcZsGlQQnAdtS3_vkeGCiRx4NuiUA_NSKKYp7LuUs3gVvtv4ufw189ejmz2rb3mCM8LfIQA2xZXJQJLH0Jgl4_6jA7z_QTDJ7MKqoyWQbemBv6_Ua1ka0dAAK1pryrLfjuAGNirlIScPU-NEEujtM1kyDfcmj0RczFdTibqnMfNB_k7E5rHPUlzwQGljbOGuXYhM1wca2C52wzIFNbcITLZjIZFikMF8GLh7_oUYz9ZhrZScZfWFwS8eeDlS7dBYoO85BG2UTqvfoREkf32EEOpmeoZkDJmTT2Y4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1b_jiAA1mTsKq8XoOTb2wnUMiDjlbyK6rukK6Bl9cs7ZtGJb0cyB14c9NvIC1IFcMMbw8vbfioXB1AvY3cjcrrI9l71JEKkMBylXdfBPu11Ihi1MtHiWNsCzgeH_J0HT_DAefn-tM46JZxW3hpAwbL8lZhS__ozFHAnzqlvp4ekv5Vwx_4E5yr1UyQQkYtHWjtNP1_H6upLjYDq-gcam3qEHjrKCTLi1k1LcK1ISOpBl8Ehi5S55rT2ywM0hkaTXTnD2y3j9mEV2yrLEW2fSD2DQUVhz0G1if1f_dBwjIxbVC6c7xfrsGUiCKDBNXdhmnEwDC8CFvZW8jfgN8M_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/msLt2gwJpMVcxzX6mfF7D89I2uz_79HHIzQ2n368svqzXTFOVulX9-twtAnBgVB2LDcYdsIJFAhKydfYuC2sR23_m6UwlzeGqEfXxVnYLCeS9ft9ZMAYnNMNh164Oiu7r9Ll2rZDXK8MGxTZwQjt5hrWQTkKHhsvu9Xbb5Y-w3G89GtKEJSFfi_E3gTmiAGrU8bA25xaI_apq652gh9255ByAwJhv_W4YLqrRR3RQoy7TAlmWOL04gllJBDxPBwy1oFpJuHGZoXm8_5FHE-Hif3fXcFVg7D5-6DeJw4ToRI1nplYPqP7TW6sjHI6MDW1V78O_yEPP00PPwCD9AuTUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=K-UfyItIM4P4wSgFKI_5NAVd2wqwkWHN_j5lTy5cywWIVDpVuI8_qdJOOl17C3paogjSEop0bAUWH1w3Vpi72yjWACC1XH-LZcMh2-yxvoaz2OfIihHzqKqjALqsvKMZTjrvlFPz0t3C32h0BDBpX4jqRtWLgYDZJTQS6umGj1Fgu97ZpNP___5vrUfyLCMP4s993Z7uKaNblY9rWDVsPA2nEJslP5zsCW_5YioIHR62cuL-pCu0EnEvjThT1pNdjdB-att0C3zCjM0JG5rddkzUVcwmNl2DWnEksnrmu5M65Cvi7ZuuveTs6tCBnT8mcmGbKhPxLvjhRBzab6e0NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=K-UfyItIM4P4wSgFKI_5NAVd2wqwkWHN_j5lTy5cywWIVDpVuI8_qdJOOl17C3paogjSEop0bAUWH1w3Vpi72yjWACC1XH-LZcMh2-yxvoaz2OfIihHzqKqjALqsvKMZTjrvlFPz0t3C32h0BDBpX4jqRtWLgYDZJTQS6umGj1Fgu97ZpNP___5vrUfyLCMP4s993Z7uKaNblY9rWDVsPA2nEJslP5zsCW_5YioIHR62cuL-pCu0EnEvjThT1pNdjdB-att0C3zCjM0JG5rddkzUVcwmNl2DWnEksnrmu5M65Cvi7ZuuveTs6tCBnT8mcmGbKhPxLvjhRBzab6e0NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sosUbaAu6YLL2NX7P792y438Kjh-cyw9wNX4HSYzNZXgr6tLqR-3nzcvWjhbbMYQzBUlZx1AmcJZ8Tlje8YIDQuHnbw-F1EQnMaxCnnjKXWdR_Kdr30bQH48y2bTDtCG34w64LoryXKAr8Cj3Lgbn4wbxVaXvX3DVV4Xt763aowX4vwkZ2UBfnKtZiV2bPePcudjShiZvcgM0rKlubWPCRvhTJrUtWomiODwtpws9_wkxluCWu7Gxvrw9CVi0MD8B0PscEYEP-QyKFpK8yBY4X_O31L_iVsx7NymsTQzhZgaTePW5yjY08LP3r8kS2pNRk5226pBMJMF3Mr_atYvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzesgTU6P70ELFi0UKmGLkgkkyeghLYsqTtXMsUrQhwU86uIIGJwYn0ef2XipLHWClr0EbBoOeUnzoaXNAEbLasrwucRr8cbmJfDtTks1z7b2knue4C0z_UILijbYEcGGMm12QqPcxHtB4m1pjTOXGpcpax8a0vxKIgjT06xA_sERIAF7eSFCiVyO0EujuuOLZR9n3Ln4GsZXUbWWjpfkB9piNrL7ogjiJyyAhimkI0XfRebWlYoFXnGF198En1-NLgzD4M9trmrSfEAStwMcVsp7oWcQxuJmbvCTm61WlRj9rU9nsxA4E86nEovFnMb5c9KVw0n3I35qUW4yQXCaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONJrSzShCe9Mdwu8jqVbNsKgsDYMYNQHmgz64WwLh_KTk87E9IHX1AFYFD0eSHqP6ReJW0iO6b_IN7L_3gGW0sLqZT6aggx5RY5YFTJiV6VOkIX9Y0Xq8YakLcpJkX8Kr28i6Mee-qQMBxnhdsXKBqxG6XSM0AeOTjoxrQmjcuRKg0LQQ1tQEwdjYS_syUyusY7JJSyl0fnEv4wDvWDPWMrDgSNReCsN6pfkZjxxA7yX9sCXt8qzaMjMHjZ7cEFoLCcdx73NiQWEjzOqbwq2zYhzmTdvBZil56Wmc13datER_v2S64hWj21b66oGgNlZoitLqu-CLESTCfYygb32Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azPeAl1IR4mkGSDtn6Xevt5bixP2mObkdnKf1nSQR5p9If9BqXjG1MvOgn7hZiC6rTOTjhQiBBZw9clymh41a_xTljzlTHPMmJWPi9qvCGSmx5OI3GjpugoMwuYMSvw2BQ8jLIVnYzxct59tFsuhI0Eopd0Ug5oBzZipk4A77NP-vDkXnKF3Am9ubmUBPKt4ErcRVZRoXhZKEqByw8W6PPqO2kzvpMv02vmOceBaiUnPGzuWXNX6DTu4q3eJ2PItI_EtGZi876BgjL3zIgU6yoPOsAjgZ9XBHKwHIu2NcGIF0uvtl3lH3O9urBb0THahwqpxjgiDQ80tzEI37S5j9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FyEnnZAxEsy_UrERH4LVhxNmyP0X2i9PPK5B3t-oL2-zcmHE7HYzm2Rxaiazed0DQY2ocCHD-REDGhPidQFokBA1zKswl_dKARgXunzRz5KKBdIrqQ28pfHUgxVZqFcTRiTVujmFhKet5a_SkDuG2CJQVnIQYbH3PYnl6CKciPRTJCrfGAjQkMCaybQTQkTkPQpy9oo9sjd-VsOjHiKC2ErTBMGiHhSOQgMW_16jG6fR3KYhYgpH78tKPHbhVgwK65ZBd_hFvVJsVmg0m-jcJhlWUUSV04I0lhzyL56rDkwQarNkQikzEB-Ww2bbTaAh9NwxohpgNjJpQQ3ZYKUIPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiK-pLWjNzWpaMXJIBPx0ufmv8qlyOnZ3YCavpVLt7nJliETHMhUmTbSkKvW8RofWVOmvO8pwHZ8rkhQ8uHnGtWCtj7F1jCFBe9PtWe0HNEiIeqOjjsG8kWMmgGhmF4T_fWlAw8qTH4D0jCYtac7d_3Z-sdJA_BGZ9-g7rSY2X95kLOD8_iDmbtMYq7JGX1V_X3oL-Sg1hUq2CQeOMYcGP9v80bNFP48_XGsEPq5G4B_Bjhl0beCDi-8mmsp-6OQc1SShFWKsFWYNW7uGUScu-Pq8iiPqVGCJggYfWJ-5cwfTJpZl-EqtU_GUuprswHecDXiI6-DceKCz9oMJbnYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiDzWOcPPYIzcBCzggwOzc-dp-9Vzf0Pvg8LWZThgzsjDmjcJu_fC4Y77_uY3bwG4XoWT6anR1X4x1Y0T-g_MkRaO-nBH1CFTQMOqiAdp7slfu7SS3Qz_4SsgDprYbEKZBF4x2Dk93dz4qxUsOWTbm8fmX7x4Xx0JWslMsdIS4jIGA7qtabqLXSlGS73dqWsLVTVxJuYkAZblSvNlZ8DGg2ZFQ2mqaMl5BUkTLVL76kEJPmXnaI8k21kjkHQkvsN17N0BZrx3K5BZ4dj8RAkR8pSCkcnDnkaB_NH8ZBIM1oWIr6LK0KzAotDiC4KmvnnqZV_fDpOkRZ72x77Wt2urg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRs1MfE3uvVc2Qsq-v2EbfUaUy3chdJmxAKfBYPD3s5pSjmjTWRTxQpPduraOn4tRNBeJSmzuiEvzt5SaPNVACHKp8jWYwy96ZrUgsKJjUYZvp4jD39ly2E2pkfVZ-jUxZBxTU4amdmnA0-0iIDtk_-2Z3QpoWcgM0ve7Mhp5hk-bbYsPOsphcuTcRcNpj6Zim6oxK9geVIBGvHkNTE9o9flaEMYMXgeYFDNEWGRBL4LQoCW2SNMhPEl8d32yD8VSLnEJH8hFipcONDs6zcIdV_OOmV4_-iOsQ3iu2YDG76yOdgxN3RfIOQMznP03vOjJPaJOMd3UrTQ5Rb3CDSBWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=NBuHzAy-8WyYgO6zs4LQuIxiQdxr9UqEUlpvMRovWXqaCRFzYm5gEsvheY69PZM6cBvRmezrjQo8FqOVBt7Gi0NB-bJBZZDfC_XaL2I835M4C1xNPiaE46wvVbWSidCNJf1hVEcDYz3uoSMPT5asBiRpCGnKxOUdLVD7vvkpm_AGU1oqsY9tNurI6GHNYAi-1ukbNYGE31fEuza0Yb4AD1N6ybh3dpyBq_yXJq8w53GWV8FH1C7dka-deRm5IL_dqDxU4Uz7MUPPjpQxmWHhpJfx6VanwlDMUBHi-EbV0yhqL_esp-grN6IAKSeXOiKodr0HTsFnTDwY1sbAyBgemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=NBuHzAy-8WyYgO6zs4LQuIxiQdxr9UqEUlpvMRovWXqaCRFzYm5gEsvheY69PZM6cBvRmezrjQo8FqOVBt7Gi0NB-bJBZZDfC_XaL2I835M4C1xNPiaE46wvVbWSidCNJf1hVEcDYz3uoSMPT5asBiRpCGnKxOUdLVD7vvkpm_AGU1oqsY9tNurI6GHNYAi-1ukbNYGE31fEuza0Yb4AD1N6ybh3dpyBq_yXJq8w53GWV8FH1C7dka-deRm5IL_dqDxU4Uz7MUPPjpQxmWHhpJfx6VanwlDMUBHi-EbV0yhqL_esp-grN6IAKSeXOiKodr0HTsFnTDwY1sbAyBgemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u70Ha2qXLFWllk3wPjGd3avAYqvVz0CzirW8gOpUMwyOYliJkbnywkmA-3N6U62bjKr-zkItVD9f-Ejlsh1NBfqtBNiIKzUhj3hRyDZ9gPIGfXIS_bus1r6I6j2isSvdeE9Mq7KSphWvu2Mxcqrpd32IpDg-Z_RgZGpclnOC7UbKtn2X4VHFKRVJ3--J14keZd2yA4WSnfHCnCBcRC3ei1jPGFZZI-pgNzW8HEK2HKp-TqE-rWTzoFhuHaaJQjN9t1ewWIyW3VEiV6BfQ4HHBBoDc-KFsTepbXMkJ6To5fvze9EgeyT4Un0I9sZVxCRTV13Eg2QRARq06yV4PrpxoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=gkK31eeG4JjAhjjP7UVeNi94YfS6UuHHwmwP7jeEyypMKj1-MRl6_DTPaAQIoM-QCVDMCBCimejsTcudNWWmkauNI7tsoI2WhlSjh1o5QF7vDdWGtB82_DQpt0cywylD5PNYjFxSAS7gsQChMfXJiEHjbpL3VztvrrCYCVnHcmMEGbEAmiIJSr9irvL6h8XK5z3zr9b0bNKFGAM4pD-jFkfgCJ02RhHarXXVyhCbtwywB5_X-YWqLyWGleYNzHXAsK0EuE5IEB7u_OuExuDU-h4INa2JUh7seoSpwJ4-LS6-unZML2G_DBYD4If_Ea_RF7dD1AsnArN6cWnVG3yl2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=gkK31eeG4JjAhjjP7UVeNi94YfS6UuHHwmwP7jeEyypMKj1-MRl6_DTPaAQIoM-QCVDMCBCimejsTcudNWWmkauNI7tsoI2WhlSjh1o5QF7vDdWGtB82_DQpt0cywylD5PNYjFxSAS7gsQChMfXJiEHjbpL3VztvrrCYCVnHcmMEGbEAmiIJSr9irvL6h8XK5z3zr9b0bNKFGAM4pD-jFkfgCJ02RhHarXXVyhCbtwywB5_X-YWqLyWGleYNzHXAsK0EuE5IEB7u_OuExuDU-h4INa2JUh7seoSpwJ4-LS6-unZML2G_DBYD4If_Ea_RF7dD1AsnArN6cWnVG3yl2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=HqzWGsRsg6gAwbhZR4_ll1LP6E18ZTw8VIl1gHaslIKY3yAm2BBDe8KEJ4KBOSioGrJBDZn-bvrkAKmCGnp23yB3rMFZcZ8QzW0d95afOOd7EvauJh7uz9f_Lp3xuYA4fEHpb2CYw9k6pknlnYeLLmXDiZjDgtEIiJvxk6Nxw21BlZ6rzU04Jubtc7aFu2PBVAbtMZAJ1FpAfP28gMiWO1zAJLfjlv6MnE533bMWGvhgFt0fNJA_BEcRIinSr1vAMtCAI9t1hBT_dsg29A4Kx5tsEbk-6McbARwmIImVOWgiJNWrDMCN1tShLXBTRlJQhMo4rGpUBhX2yT8qYcgM4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=HqzWGsRsg6gAwbhZR4_ll1LP6E18ZTw8VIl1gHaslIKY3yAm2BBDe8KEJ4KBOSioGrJBDZn-bvrkAKmCGnp23yB3rMFZcZ8QzW0d95afOOd7EvauJh7uz9f_Lp3xuYA4fEHpb2CYw9k6pknlnYeLLmXDiZjDgtEIiJvxk6Nxw21BlZ6rzU04Jubtc7aFu2PBVAbtMZAJ1FpAfP28gMiWO1zAJLfjlv6MnE533bMWGvhgFt0fNJA_BEcRIinSr1vAMtCAI9t1hBT_dsg29A4Kx5tsEbk-6McbARwmIImVOWgiJNWrDMCN1tShLXBTRlJQhMo4rGpUBhX2yT8qYcgM4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=XhEtfSBiIphAFY4la3Kr7sgjzhn9lPR72uRLgEj_OUh3SM0kZoC2k9xbjEbZvwx168ojFp12hrHVv4Cn2W2kuVmQ8jile0VhIUJapWl4cb22lfnnEprVO3lHQh9iltHCC3jyaykkDRaHOgCq2HOLu2iLgAtWiEYjbL8300NupqjZ43zo8fjGHw2UI3UuhJJXhjvVz91L80fg2wtPR5DF7Tn6dEFAIJ094LFvt4LWiUknSfoRD_UOEzmqRYEDql8L05QOuaq7BWSAGblauvBiIx9q4crXt4QFWcs5PuEqsoyj1VOubHndHeQBP4ziEzHWkyvCB9VhV3mWn8sZVtQhEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=XhEtfSBiIphAFY4la3Kr7sgjzhn9lPR72uRLgEj_OUh3SM0kZoC2k9xbjEbZvwx168ojFp12hrHVv4Cn2W2kuVmQ8jile0VhIUJapWl4cb22lfnnEprVO3lHQh9iltHCC3jyaykkDRaHOgCq2HOLu2iLgAtWiEYjbL8300NupqjZ43zo8fjGHw2UI3UuhJJXhjvVz91L80fg2wtPR5DF7Tn6dEFAIJ094LFvt4LWiUknSfoRD_UOEzmqRYEDql8L05QOuaq7BWSAGblauvBiIx9q4crXt4QFWcs5PuEqsoyj1VOubHndHeQBP4ziEzHWkyvCB9VhV3mWn8sZVtQhEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qlah8lM0VsgLK_0TVwXbQhSMPxuF2wRoZqv95jZ9laUVMyBltEgHG3kbKIMreRPcwkRZJCq5TBAhbWU8SDKspts5-vnmj0DIseXBaeysFAQKVQAAW6mHVAQrintONEPtP00_0Vx7L33iaXeui1pT02k5Y-qGh10BDdh6A7fi-5TRTNru7ckKh22xP3qmARAtzbEJ-FL1zYTyo2XBa-HGvI4Yfl1dsB3MpjvglP8_RVUJyLae6L16KAIvXuQzxZDjYN5TMMZd3_EsjOjIB_Kvt8d6eMq0tEMcAPCSkVBCc94oHRqwIoT1hNkPHo1nnkwKQ0KpP5mCYLEbKC4hdqE8ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cfUMlVl8-gRZ9joF78tp_3AMCPhXTyz06oHCwajQlB6meOF2oEW75AYMGQEV9CYI5TWUtVKCCgSjup9fJ_7PPmOYz8xK5nvY6y3-6PGZCQmTbiZTzD0vJ_no1FKg7q5p1jZItmDvUm25gAaf1rhB0ZmwfMwTMa1TbBRZx7Xl7XucsMW6KwXSINiQfyvpfXKFqVg34Rpmz07N4zEfJ2xe5_sSEOdmQRsstPk_zONQ0FUjhYdSAyLpj4aKi3XlggUp3PmVqdG-No9XS1Z9Jbt0nEQGQsBdJQ4LyLWOpiK3KrqxtDriIGc-6AEd0tYHXbOrAx46n1y4Pf5OThuAwlMU8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=M_uWo9X09ISeDRocew_0tQeOcpDgMcR1hS-b0Nk_5ZrQDF6uCbuJV6jVcml0bOJYw55w9X6_7SRGVxamiYrIyLt3proqpxw1kG1WU5OqmN9b0VAgvMflyGDzCAUyBU6wsW3ve_mKofZNsd0yEuOYPIHt4vkP7QZYupabAGI2HoNnQ3Y3Y6Y9Y1r9eBZExob2Hr-0JLuOMBsSQnOTO0gBSOCyzRUsxEhr-NUxkS0bUDHv4OtkCqy3k9XjBSl3cvqNljL84EkbBtCjfiI2Tj6UQBSnzEodpfvI4E8UC-xXoir8iEC6ybmIqaRt2FQb1cOSawx8JI3wTLauAl9YixQ0xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=M_uWo9X09ISeDRocew_0tQeOcpDgMcR1hS-b0Nk_5ZrQDF6uCbuJV6jVcml0bOJYw55w9X6_7SRGVxamiYrIyLt3proqpxw1kG1WU5OqmN9b0VAgvMflyGDzCAUyBU6wsW3ve_mKofZNsd0yEuOYPIHt4vkP7QZYupabAGI2HoNnQ3Y3Y6Y9Y1r9eBZExob2Hr-0JLuOMBsSQnOTO0gBSOCyzRUsxEhr-NUxkS0bUDHv4OtkCqy3k9XjBSl3cvqNljL84EkbBtCjfiI2Tj6UQBSnzEodpfvI4E8UC-xXoir8iEC6ybmIqaRt2FQb1cOSawx8JI3wTLauAl9YixQ0xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=Sq9I1564uykCXa7M-cE_kry9jOoYgD2HI3RiK3cp0e5ZHRKQP2a7-A1H_9W6bnjNLS0cYUks07giwe6gSAR2YUc1J04aepT8RCjgb9lMfcEBdeMD-jcKS5eYyOMQ5g07YE0KEqmPYhth_c5g_8_NAhKLrwE07GSaSFObn80i0bbFiEKC4NySKWsJY0nfVt5NiIs2uMFbSNtXu6L0Aaimz7g_SSPz1MWMSguE9mwfngpqOPsbkT3f5NGKFW93Q2aqnJ4ZhKknXL_IPc96lBbAM0IBv4T1V_qQWYEwjUKR-i4fvmdRTOTjS52T-PB6F5EIgpsizI1MnDjj34MF0SoPrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=Sq9I1564uykCXa7M-cE_kry9jOoYgD2HI3RiK3cp0e5ZHRKQP2a7-A1H_9W6bnjNLS0cYUks07giwe6gSAR2YUc1J04aepT8RCjgb9lMfcEBdeMD-jcKS5eYyOMQ5g07YE0KEqmPYhth_c5g_8_NAhKLrwE07GSaSFObn80i0bbFiEKC4NySKWsJY0nfVt5NiIs2uMFbSNtXu6L0Aaimz7g_SSPz1MWMSguE9mwfngpqOPsbkT3f5NGKFW93Q2aqnJ4ZhKknXL_IPc96lBbAM0IBv4T1V_qQWYEwjUKR-i4fvmdRTOTjS52T-PB6F5EIgpsizI1MnDjj34MF0SoPrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6eBPg3sMIu0xWvn-S7YH7U3yBmHwGbxNQTyQeCfL_M7nC2n9GozYMS0j7viuUo1On6MjheCaqGpqtKNisDvTjsqZ6rujsxC7okNwwrgSrls6uw_PSZFgbnAK4eNJvghKlq0MjTaloL2mF5BAdjZfHN7TZ083fc-RFmXU7WOzf0aNMl61AlxTO81uOGE_pOFxk2xxs0cy2jH-AG-RdeDL2WTB_ZOe3zqA-xVRfZSVknkCBvgvmQDu7AYQpVgxncwNLc7UelybA9gM0Gef7vfahKeiGDVmHvUkj-uMjlRID5usWa8j1Kj5za8JQ_TUzmvfWzj9XGHuSNJhJwm0Uw2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=dKJNUkgUn9bEFaZmB0B314H5Ful3PbQ9LKgRKwHNU0r9yTyQvXKSJsUGabWkU5ZlZgQoIjWVIPiAURpJp7WLrVAy-7quyjcC5LeLO5tHg5bOTSCV2KbyuJKEnspbvcpaU63dPcIYN3HcYMr3CUVhj7HZzjPVFfuA0x53VASL7zsMgpABmnTUor4kPrqIa2gxZx3uDLIw9TZA5cLZquFUTzemVS7MFjJOx9oUMZIiYuOdBMI1-nBsa70RJ4NX1mXegX-GQGMJoLIScVRaDBW5PAG2ujqUchXJ2BKP27fLMYicHGtPgJRUmZGlA9cCxLqjKxU-zbXotQDo93RdNRPnWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=dKJNUkgUn9bEFaZmB0B314H5Ful3PbQ9LKgRKwHNU0r9yTyQvXKSJsUGabWkU5ZlZgQoIjWVIPiAURpJp7WLrVAy-7quyjcC5LeLO5tHg5bOTSCV2KbyuJKEnspbvcpaU63dPcIYN3HcYMr3CUVhj7HZzjPVFfuA0x53VASL7zsMgpABmnTUor4kPrqIa2gxZx3uDLIw9TZA5cLZquFUTzemVS7MFjJOx9oUMZIiYuOdBMI1-nBsa70RJ4NX1mXegX-GQGMJoLIScVRaDBW5PAG2ujqUchXJ2BKP27fLMYicHGtPgJRUmZGlA9cCxLqjKxU-zbXotQDo93RdNRPnWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
