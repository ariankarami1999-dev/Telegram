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
<img src="https://cdn4.telesco.pe/file/Xrpecfhh4mmjC7QpsJqzy92vUpklfRToNPS9WFpPAu5LFmxvA7CCLtbaB6w5MApazSfrghrSIYOcBsiklynbKJnqH7Y--eSt2D1YPu6iZJrA58YFcJYriQudrjSiml1wG2CBfRtI1ETnIX5tg2ogxaxUp6xqCVzUW_Arv404Bti_c-EOrtpc66gZImLKuYGD7lGdL8xZgHGPbrYYY9FgpwBES_dqPS4u63cu1DYEgK3HdxzQXazRS3WeQvtJSTT4FLm-GdbDb98xxZhiG8IbjK2rhA-BbD2IxWC9ydU3B3RGc2sB6ZfGDuNC2KjvkuY1StKHVdp4hmF_ckEsjQ0QQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 17:28:34</div>
<hr>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=RcYulb-NLyH9YavVDYWEXvsa56GaDx9sjwfYR-7jn_4LlPuNueZgAtoC09Nnsh2oqdPoYj68Cx_hkWmztXWfWkzTce9Mx9mRFNj3KqBNo3cM_AxExF4H6eZkTPtmZNN6tSdwGPkD8HMH5j1fS9mMk2cK-B8aLQsq_hsjf9I8KvPXP7AbF-JHm-WG_vdB8tWZnRJW6WGMdW0YBSqmSFJlvyii0XrSJb9Dv64Z3beC9toZXSAl5kn_w7NJWI36PDu8dilgYoydQoyzTyXietKo6DFiuComjOordPkIr4deeqTP3DqG1u-tw5xI20bBGalm64qXCdVE5K2RwPboLzj9ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=RcYulb-NLyH9YavVDYWEXvsa56GaDx9sjwfYR-7jn_4LlPuNueZgAtoC09Nnsh2oqdPoYj68Cx_hkWmztXWfWkzTce9Mx9mRFNj3KqBNo3cM_AxExF4H6eZkTPtmZNN6tSdwGPkD8HMH5j1fS9mMk2cK-B8aLQsq_hsjf9I8KvPXP7AbF-JHm-WG_vdB8tWZnRJW6WGMdW0YBSqmSFJlvyii0XrSJb9Dv64Z3beC9toZXSAl5kn_w7NJWI36PDu8dilgYoydQoyzTyXietKo6DFiuComjOordPkIr4deeqTP3DqG1u-tw5xI20bBGalm64qXCdVE5K2RwPboLzj9ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzb0Pcl03Qh68m_aeP1jNKBdkDOSbZVwxuVfUTcFLuW1Y2XQCZr_HXYGeI4RvVVYozacCN2V5e72k0u9JRDGrd9cJGGZGC4yd-h4dBQCzcfOO5X_AYndSJ8E44SBJHRqLBP3bjKhZlEWWQl6sy9hQXUN9BKpwIra3YbvY47DfTfXZDaOZVM6ftYvsLoIAtCa-HOiEPbtCIP3LU1ywhTi11n5H5H8Hk239YVOiCnqadimOun3ZsDwxQYfMBgZHRh5X6a4-L80K8dEwcjQxlHCKdP6XzozW-3zUyu3o6xHI6egGeGQRaU5TOvCJVtsoltvPt2aK5Z680eRH_ZjOWul8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=hKZOZSLlvmPJgpQYIu5hn3Zy1i_Vv1mJuMt_3coQgYMa2VLKrWQHQq8xwxVyWZ_xtJRF_n5MSPN5h19GTJh2sTRPkHCmknMwxRyWk5okBrxrm3pIjWv_auryvKXsRQEDtsoPBowrTag-XMwRnK6FwJyesxYr_qduVVorr61DP_7q2pmJ4kpcXOy-no5vOu0PS-C_cDmc4js4AX90zTHRS_51V3tgyhSmpXzng6fZaYHzZm85Pk6s9zPlS2RkCxugQFGc_8YryW7hxPpZyT6DczsRYs9Qed0tQlbWw9B72Oz99fZWLRVyBR_7eIEmqui8A1y63tZg2oGzZflAeyLfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=hKZOZSLlvmPJgpQYIu5hn3Zy1i_Vv1mJuMt_3coQgYMa2VLKrWQHQq8xwxVyWZ_xtJRF_n5MSPN5h19GTJh2sTRPkHCmknMwxRyWk5okBrxrm3pIjWv_auryvKXsRQEDtsoPBowrTag-XMwRnK6FwJyesxYr_qduVVorr61DP_7q2pmJ4kpcXOy-no5vOu0PS-C_cDmc4js4AX90zTHRS_51V3tgyhSmpXzng6fZaYHzZm85Pk6s9zPlS2RkCxugQFGc_8YryW7hxPpZyT6DczsRYs9Qed0tQlbWw9B72Oz99fZWLRVyBR_7eIEmqui8A1y63tZg2oGzZflAeyLfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnAla-brxSe-EtswqNXTezxiWztkV9Mh3am2v5qeACCGJUTbtmnuBfMQUlvt4CS2ZsI82CGlQfKaYJrcs-EmC619jZe1jkeAVVj0Qib2T6T2b7j43wuCshlkjVr0vv2efKza69XOhGZbouk6aeNNDQ_yZEwIU4eFvsf7bqG-DveRW64_K2GQE_h98_d9yi2l9OPl3Yl31rjJNiHw6AUTDoY9y1NSyE-IJ5qwqgIzPiL51u4khK8CTjj-R9tQU6keyJ5vgRDwDzwQLqwTGtDrDwMt6hn-AYHyRoICb82bzZjNiJB6lENstbBWfpLtniENV5EeRxsTFDsl8U25r8au8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbe07vhqkMmtXln-SBm3NkJaJx3VKKhz4B7BS8deEvsgXdEcKBwB5jUQsfrF6xWoo-t6sFNgBmraR6FQtknFK-8vsLttMyQwSajKkhRxjSStHquJdBpKgrr6Xn87CMqzMEJf9EJABscakrnXTrS8GY7-G65Az0VCA5lmPP_WTe9sGGb4cbgN91_zz2-JbQYzMC2MUnvBODXRYwUEVhzkEAbmvCwcQgGf9hQv5wWTRnH8fRnOgH4CfqEmjSreDugXGmhrYrdAKY7-pCJf2x_1x51hHd7ExBaRCKye-zsJ1W4mt5qYLnRvqJ_pv8kowhsa8JjvnuenhF4305ENVu8rcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX_rCbrlzt5dkjLwgRV8Xg44fDx1-juVPGjKBnePhIaw-AQtwqqAC7cfvy04i5YJkJIR00PAI6XekJzZ7F4i_JK6SCZp1vIe9wZu6NsfVy4mP1OruENpj77fRwShakzDLq7ehawXO1-7BHDkGALWtFjjc-avP0toCRxTG0wRCc62LC7OjBxkhkTorEfXBisMRtWfA7MR4mWITBBu20RdmVgysV1N0aBFrwFxPnqCuP3aP59qb4TSWTiEo110abWzQVqV4oeWHl8E__QUcMmaENl2J9wtPycK2TuYPc_H32bv7HLKU3gb6UuEZDjCqpeXilyjaIUlpu79w_7XWdZJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCH1ESOC_Fy75vLp8dGVYiFAqe5ny7-jIpW3544gqljxJ_FJVBb8gp86cNwyKTHpEj-AvUaSUfNkLyflkdP8PY0qfRQ_TV103Q5bNjHAt81yTzgz4J70lrP6KWXLhOBdZ9HDOESdfoUL-MjFX3zgCXBHwy0zOcfH6gJGs3-5AQJsjDP258vV5Z6dKBehwQMVI0FnmZNdUxs_06EPOqFS2G80VOJ2pEZqs4yVN1gZLvEz6B-6xXuwnQpo1eMxrzdRewERhSrKas8NugQxfPUvzPlPwMqCTlKKHIAtC8m54FLBMRXFTfGRu_khTadaT-YW1n5r-G_nyvj_S6Hv3iAGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3G4P51dIoVK1rqziPHY8T4_wBt8ZQYLDKUdjXPevv9MpfTPFFmt7f006CnIKnR9ktFnhhBGxbh0OdqxSzvKzwdiKTtiynV6R_el-OpqVGrHJjDHCyrzAVjYO_wfNOQX9cYc5cY-PaZrxcO-wK7sDxdUWFSUEbW89sRE1BnEPcf20w8Wt9DQGGpnCScB_d3D2i_J0fMB7U7V9XaHLSNbEF4Z8WnQpKcNxeponq6g0KNe0KjBqnaxESmgDiHvtztEJ8Emb4_d8zp01f2rh-VJcF7lUa-XSXBZuHKVi7WXBnexfJ_Zm_jR8OK8PDT6jRprVLt5itR46895rYF3tB2XXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTs4Dm6NMTIYcNcXOnQelVidJkS6xVxndcRerbc5QHrr7tXpqDo3onIHptvWnf-IB8HiIBzsD21LiCf91eQml9DjFbymrjdEjSIvqLljUhTIv8yeUrPCWwgUp8PjzWxKfuzbNVOp3fCXHQRYYZ6t03Zb1gqdFWKp9tYnJJeuOezzPFDq657JK4c2Xhq_tNtG-gEq22acOuwK5daDyZkPxodXZsSuVTE868_bzfSu7qq-d-WVEpKVsnQF3G1dgSGWWsj1IdeZcggUQ5QZRAH26vD53i4pklMJBjM_08V14jIL7tslxP_CoS1MJuNM9dITRs9tn3670qLB7ldQiSPeHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=EaNN_DRmgLljJk3s4RbKtmVvKOx2eHUVMoCEjrk1uwRAs4rFeIV5mbQ3g7tnHxaYKX41qNVT4sCspePpptf42WHUE3WAUwEx98vjK8rr39ERSl0sxj6v9GaKbi8IG6SVi5O2RkY6CeQTwc_jgTddciubYZv4LHvjKJ6rjzPvhdL5a-Spx2TIgXecgV80AlzlJy_OT2dGB67NsghTIZ11207bmR8cs_WlZYp23cbX12ZFWRRZ85pUTbpzl-LcsOCqK6upVi3oCZAq5yZ_DJ0uWUcy0XLlygunkFQai_Z-LemUhpMZEZI4jLoDvI61l0V4oWK1bl7MFHBuq1XXUY5QeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=EaNN_DRmgLljJk3s4RbKtmVvKOx2eHUVMoCEjrk1uwRAs4rFeIV5mbQ3g7tnHxaYKX41qNVT4sCspePpptf42WHUE3WAUwEx98vjK8rr39ERSl0sxj6v9GaKbi8IG6SVi5O2RkY6CeQTwc_jgTddciubYZv4LHvjKJ6rjzPvhdL5a-Spx2TIgXecgV80AlzlJy_OT2dGB67NsghTIZ11207bmR8cs_WlZYp23cbX12ZFWRRZ85pUTbpzl-LcsOCqK6upVi3oCZAq5yZ_DJ0uWUcy0XLlygunkFQai_Z-LemUhpMZEZI4jLoDvI61l0V4oWK1bl7MFHBuq1XXUY5QeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7vcECloDA0bRqfh3zCA3376RWCeMBWJ-tkDzDoVTMnC-MUn5PwofEKMY3uZTZ08A7rVjqZjFQCnU7z0roeZOpc-FzwKcfV-9h1bkeQB60LytVLrqQAfG8wH6Sw0Cj16CHY1uTQVpqWZ88LzsaccOQTKUQbRMB2tLXkk8MOIFwxOG_rmhpfLpOSfSGOpwPO1C4SNQxS4BR7s6gqDm60TW7Tt8k8XYP-Qm2dPkzX_cvmeFDLpltcxUmydHKvWza04rEUbACJCYZSsEkHc4RfDA2bbWKa_xeWVITn1kMwaGNyhvvNarLWdv-11pwlUwxPVCbXwSPtM6_NVEPbeAxFa7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsGvpmpuBO1x4amq2Lg1zgNFpw6B7JjVEM7fCoGK5cy0pXpRUuMGDlBQXWAg65sGIo9HqT4OmrKJonPkdhdzqkhwAgl_bSSrmWvAaThYZj7EPE_J7wgoP_tJ8CFvTTzd5psq8k4oPRJ1y9P0ZWF8af7uqbBgT3B11suL32ksSjukpK40i9-ZtqRRcNiLi2zXYnUvUaxaiAY9FOOBjyI7QIHPGPlKxChSuotVelWCQW97wnHZ7P1tvmNpv0pYKDMVOhgXU12WM16tI89gD-l3n5Z9yRo3RlUBgdZfprheQJoEneiKzLG3eT2qUoQLvcFkGpxdInhd_4CfLp5Ibqx5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYQVs4U_eBmIXtUErXyE8HxX76F-j_GilL6S92JyOXdm6AFkn_Jgievckb9a3daZgbYSta75FjlBU79Z4OLC2c9YSqEtxZsWBJssfKjzXFc3CY7Fj1IDEuCcdO6MMQ_ArsP3buqMtZq2mUomNZ_-2e45Htqw6-fzT4pA0AJsAEWsn4exTGcZB8z_iMa4T2QNHWMJ_AMapiEtxGuUNw0RcdgRYhVHIZwsrzPqePERsfZhfb-tkkUDRmPXDlLtO8E8x_L5_apm9PKS5VVJ8SGFvT-ycAcrTZOnUynzJ8y6SEkf1ZwyB1Of7qjBU7yUjYT2p21_mvjHpnbJJ1pwAXuD3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQYEEmSVK7jsd2o5WWGD4jLSQFlvZxrTqfQJhR6gt1ex5Ni01I_Q-muk7aXIkzFUHFaZ8EQsYGxlmcO1Kj2PNA69-iXphx8OA2GTJx_UEdADv57bITOYKtTp81MZaNhDqntzIN_V24zljUZsEKj9WbbazTvx-L5-8OXd3goADczDrQKoomzgq0pAvgckww9iuEIszD8VO4BnTFeIU1QPMwkEkgqCzxSwceBv-B_Xn6X3hVeCUg4tCwfD0bD-vrKWMCRsEMU_DKtn2Hb8PMa7JxsJshxcfYe9nlOES5FPg8HmY6q_EPkH3Dl1O6oJz2sg-q-9xdjnIfWuRHTXPUdYHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=bCkV-vQRXCDpqvqujuzJlbchbJsefuPTJgUsaAHpmTIMUDVanDwdlTboMruv2P_MPupTY_Z2cPsuSjigHHHdNYjvGJMWS-7fo6yiO_wv8oLZqUrovf6EMW4VmQm47S-aZG_pA1nSrsuoTISDZ0tFddKoJLtx-cxW7Ig7sMQlMkMLFpGoCNPKGiD3d8W_Dj81aQ-1NaLqcQsDnev81PhGcumv_bGXr_FjxrVHTRX_8a5RvFm7ApJD5EFGzzc9kjFTEXGxHMSzgrYNe9yuxroW3xbW_8PoWd-bwBGkExvBfzts2w0anU6AyTjhlLnYJCvRe844wBTqjs7CNWOQf64slA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=bCkV-vQRXCDpqvqujuzJlbchbJsefuPTJgUsaAHpmTIMUDVanDwdlTboMruv2P_MPupTY_Z2cPsuSjigHHHdNYjvGJMWS-7fo6yiO_wv8oLZqUrovf6EMW4VmQm47S-aZG_pA1nSrsuoTISDZ0tFddKoJLtx-cxW7Ig7sMQlMkMLFpGoCNPKGiD3d8W_Dj81aQ-1NaLqcQsDnev81PhGcumv_bGXr_FjxrVHTRX_8a5RvFm7ApJD5EFGzzc9kjFTEXGxHMSzgrYNe9yuxroW3xbW_8PoWd-bwBGkExvBfzts2w0anU6AyTjhlLnYJCvRe844wBTqjs7CNWOQf64slA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTsRDx1IPUYVTxtyfyhJjuZ2-PyZjmHOfJ8ZsP8-Oa-kN2h7xYmQKTx9Zkw9hBS4LkzTwAtPpUQ62Wrj0M3qMijahkJheIDegiSGMDfHFMiH1U1yXO9apqup_laVWinBpGuCY9M01B9XC8HPh5oO0HPkAHKQXPDycuYkPehGOFVkG3DebLiRcOoyYVqqKvWMPPbLsnX3YEoOpz2X8l9STDxLviSh-NQPptgR1qvK3Sa3RRGPWe5x_v1833PKFMMg_vITritL0cnSLG6uKdWeldQde5Vb3Zw7zG-6ynJouzIvVX5K5TWOH8EcapwvLr8tyFE6cx-dteXFxhPSikcVVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPFqM_TmfbP6VQXasBbRvQ_UoZCSsayK7YWzYxNvXYbaNkWpKtoYZcGksiuMpDet_M_e2OZ3bdwgBoF1_cP9qLDHk_-rszdgCRx3flJJejjGyApdd4hh-0lpxCk6Rb7JU1iidB4AVodzn56jDH3QrqO-l7YHWUTDitX_pfU8uzkVD-pb2YvrlA3AxbFnqiMIKdf47q7zyo1E3bx6aPdUsZtTJY2VKYXcG5MdLHoGRbnk_fvSEJO82IcpiNkc5Kb-WS53CScQG5CBY-Uqtcfwv9wnq5q22SrIBXBldIitrFnzC4lI1gjOPGJ1i47EYvjQosiFmSDfh6-w90-0btgKDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrOlOKXoGc57vdQphCp6q7DZDZrVTZp56QYbiuYOOTPtJV25y6PYspx9KMNSpTSzUHYU8Ch31EwyQVDPO5z__EUm7BHVLtYvm_ZGZgDBEakH7VNmuVotSvIiOLuVXPJAPTLwA2JWy5_VianBQrUZTtxUzF55HsWKlO_JpHEif4NdlLGtJuDCES202_q0-QqXdi_9svdY2yabjYApJi_1MUlMd3kh4y3kmspjrQ8LzUOjvMvGH0S2RmVk-806Oby3zR8HXDWojTn-fAieTyMM7p-xIxma8M3TbbyL_M6TxMJJXzHg18ktAZcJHkxNxX6V_waZpkfYCK1qiGHvt4aBMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJHxHLIhiPzOecIjKjITahmFkOq0ihgcHMLwd4T07mDsts8xoNc63DptM8B7bsE_pvBqb2QZuCi6XbmvSPwlcQtPs3021cjBw1DYAnodJdVyhJUbsSKecFFPLqNViYd6DoNvV5gXiTQinqj0OYXNUxASNbRmQMis7jmWaJlpf8mObjMnFFLBUaWC5Dy9LUiFTbNtDDDrUpMA6FzITS0amAMW7u5H4Q2x4tVhUIeoALhIRzVVIBsrntnjt25OO01xe3zu7Vf5JsqbbU1QLXhCXAcQhl-gy0mo5lk63DvOmBJBuJsYVxI8ANldHTgnbTJQ2kdrFsHXkRnuX1cVPPSljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdtOpX05-xqbU5nKb6W_onEQUAHQirmJhku6AFom_goFNP5eJa3xKh05l3HejExmT9pVxPMkc5U8_ZN-BvNmDI_OOKp14PwXStOZ-dmaUmEcheHdkKhD02JYWMXVxVreiDPC2cXGTCwBjiGLzNKCE4yF_-Yfqx1IkGuZ7ICPgotMFr42ybrnP_6NIHOFt9_G1ZB6fqfrsFyA6WO-XgWcwWsC6_PTv3Wj1s726zlwM-QKTsGN5K_-2ZkloYFNYozFHIjdyev1hTNVc1JPmsSlaw0LVqeYQ2s0vaoFK4wVyov4C4lu20kk1JXwnwxQzd2E9VGlB9NbJLq7C-WkpXL4Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BguSuXxAklhA_WOC2WglCX5WeEQ8rDUFvumKeZIedqdt3pfl3W1yUmLFixjGTzKCOj04JDgvexJoHJfo6SCBGy3lmdta2jhcxKYTHZWX_8VMX29h1YNM1xtOlE1jB1zoDYcH1ooVaVjmVonmrIJIg7ViDtDG4HJlgSqjmL1G2Dt5oKF4b76zmbJgUhxxQZaweGrnXpn0EDAGgNEXqS1hTU8QZSXOJzgiV8-gUoPf9WHaljjJNfcEW-vTYF3vCtKlaNWwVV0oBjL1MQ389Zc2nvmDMaOMN2uEnxiiR3cbo-WICWm8JMx0QWwHETh4VfJ0psl1g4Lvm8_l4XSnVA3XNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYJI7N5wsw7zUyWBQddWEIpKoF3OL0AoBUdfLBjk2ZuwvqacIeinSxqPQzjjbhsfUdeci0oWa_yhDLE-FcC2JdEnKMUutmDhKfPFl5RZWMNHGuPtGDbyHna8zcQOr5eRsKDuLfPCiLA9_71McJ-IQ_R9WaWw7gxPbg97Bt86YKHW7eVPcUPFvn4-0KDUHn6YFCk0Pn5CG416jc3VTWvDk_lCKAD0r8E1B7BMNzPAEAcL9BwZYezF_Y-6yu-TnkjoyydtKIiqYZG7BfUkT_QeiLAg73WRReWksgzzqnYIvmDq-k7qs84GerAxdRcJcSNIJv8YwT1G04rD2FTlAHejUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCBwrSv-JDWbiNfwI66Z0XN74VaPa7kbBs4jzqkZTlT-JaOn1XXiJ3qUo8oeq373AOkZPWZqlVw_GDxwrnTMWQ-OgBpqWusvcXbdaQSm8VgtpvicGv_2vwgKi6pn-tYxwOMIsev2wOIxYIrubdluoq2vXeXD3M4pdD1uOg1dyHpLEmZ4zs6XuRdJtHRObqKN3XQxmdC1zcrX2bW4Gvl0MhzJzYVDU2pd2cyt6DVeMdXlpresignJNguvrHNMyHHuGbSJ6y8NOiy4rfeo5ROcWx830ROTNrTOB-_0ajJ5y1napY8ygOy5Uc3xYWJj0xCzs2r2eKPfawPTo9ta032S_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRyEYfTHnHxPZoijZROtoX6yhBiHxP-qGrA3XuxJtDDpifMpz7MXXH6EJ5qTYlRa4e8QMmA-LNMF6vJQqsJUR5iSmcMKZJERfge0tSSfo1seaeBp6YGJYYmbiz6NU6I_qxGJAoo1uQCybct7DhcIfmHaW5TMehS0ta-Fbb_CFmOw45yZyZNTAY4oXENvp85QnnAAWVt52dc82xDUgJvdXOjXvRxp8w-s0wyJ0n_XfgmgeU1b1KLlb-0irlGl9RgQ-uP5UCxm1CUVirCZod9DIZeXXBLGZNu13Phc9FuwmIjX7EGKt03TinpvUYpRoPEsq_1-PZuNXIFfNOnu-m73sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS9-MjajM1ReyoAjIg9gO8T-mIyln4M5uvFiybJMTIdwGvmHmnfBtKYRkQG6GPNlj8pC5zFk24EkD5UH_7SI9d2AHRA7oDujFHd8mWzCZLr2_H_BzdMmrQMqvbAbZcLwjGqDflda29GK49DcVz5NT6lfxGb_sZ26lRsN7pfahDiaXGysV8_Uf-K20WQS0ePjEqkCZMuTFWnnI51O1Lijci89gjjO57RXH93Vf5gniWVqKhmWVnA8nMszflHZZRkQRdS26fQw1-pYiwXAyHAbtGt17IBZLs--8nv1GObid3MLrO_hE9jtvf0g-dBo8EeiN8J8QHiFvG9uQHbAd2GaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=VwJBLEJdCudxuV-TDwJ4ep3yn7y66JB75raBZRRDcjfaL3ev3pR09fdujG6ZIznFetSPl-UYAd6c21FSpm4qGLIHGJQgSZe9u82aLFi17vEzDcs7WagMvIcJwG4vUDutGc_CQqqMMhlImPPq4ZxlRO6jw9Dg2aMBQrRsB1HnqMW4_yfuIkYAuAAiCJXuPyIoEuxmW2DS2_pgn7t21GZFkOpx-xkGMk4c4D4_7Awgm025fk6EPk3Xy0HcLHH-SDJ6JLUWkaW3veyfiE43YQy7Hlso1IS9DEgP7O9jWvbZd5kHkZhYdr2yqou8azu9kSwwmwkkhbU95o9WuH73vsOU9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=VwJBLEJdCudxuV-TDwJ4ep3yn7y66JB75raBZRRDcjfaL3ev3pR09fdujG6ZIznFetSPl-UYAd6c21FSpm4qGLIHGJQgSZe9u82aLFi17vEzDcs7WagMvIcJwG4vUDutGc_CQqqMMhlImPPq4ZxlRO6jw9Dg2aMBQrRsB1HnqMW4_yfuIkYAuAAiCJXuPyIoEuxmW2DS2_pgn7t21GZFkOpx-xkGMk4c4D4_7Awgm025fk6EPk3Xy0HcLHH-SDJ6JLUWkaW3veyfiE43YQy7Hlso1IS9DEgP7O9jWvbZd5kHkZhYdr2yqou8azu9kSwwmwkkhbU95o9WuH73vsOU9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbvwI8bdSLpkwvEPkCTwQjCFuok1MEXGPkdgvtk1VO-okudoZuGz2367Orj4DD9Bt4TuWI1rpLmpxCJ3M8b_IU5itx9EOgj2C4zPj_PE-RYTseaF3iNGyuC1SeuHszESqggEZvod_naFVah_ANbSXqe6-D9UxrhczJegyIiR3FsCpirjqB22wDSk-Msy6yl6_c_B0SZVOcmwz3-OPm_pc7PlVU_7fk5dY13wfpOeKR7C8dKe12680br7BzpxQth8NPqvRrwAnFl_5GEJ30dqP45cETwGG7L2RmIUkmXqqdnNFNCUpbk2y0SbsIZc8Iv6_hhr9E5vjDHYEpHtTMC7Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmBGuKAh8V39VEtA723z8yDwcImE6-9ypR4ErnKCvo3MxAQvAMYCJe7ZwZIjU0Z1zKoij9t_zv0CK4qYpqUgrA8zFM2aiQwN_Fx7jM6X1NdDeP0hU_DzT6D-yFifwg-q-x3pPqPodZWBhDvdCQZcc9JnKY_eLco7nK9HWnYk5pClZuEzfIXpYeJRP9KeUDGFoHXzPORlixsiaIqp6iWCBdjQL7tLULxJfT3JFvBEB19XXJWL1q8GPgX3KaDoIlKP0pH4Ef-6jnzPLgjkl76gJB6J5pthrhHzfWz3bBImldM3mlddtzv_c3DXg-nCtYiZ0DMix04JPITT9BUeswzLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=TrMuQfB2Dl66SQUUuxNLaSkV9OMZsuYHxa21rpaOYrypV0U1KZbfCAlhnaidUtEtv2yUyELsEHIOrHoz8NqbsVQcyKl-hl7V_kTQZJuLiHPMmLY9d0tD_sJsJ6xZYLs5ckZBzzmqWWzUowZMPoAy1CJi9Y4Nw33N4X1LRk9mFPPcEJAJvKQK43VA822dlKaecW7HMQsGBnqsFAwCG5afx4MCDwcfWVXjO8FuI_YPXX8kMUc1MDJc0sKcWN77gXI5uyMOcvrwv5uuhJrELiUeZUzDJxjx98AQW-LrsSKsjwWC1F7r2Mtt6IX8mlgktiwNL8w1He8iPQC27YDQ7HdzVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=TrMuQfB2Dl66SQUUuxNLaSkV9OMZsuYHxa21rpaOYrypV0U1KZbfCAlhnaidUtEtv2yUyELsEHIOrHoz8NqbsVQcyKl-hl7V_kTQZJuLiHPMmLY9d0tD_sJsJ6xZYLs5ckZBzzmqWWzUowZMPoAy1CJi9Y4Nw33N4X1LRk9mFPPcEJAJvKQK43VA822dlKaecW7HMQsGBnqsFAwCG5afx4MCDwcfWVXjO8FuI_YPXX8kMUc1MDJc0sKcWN77gXI5uyMOcvrwv5uuhJrELiUeZUzDJxjx98AQW-LrsSKsjwWC1F7r2Mtt6IX8mlgktiwNL8w1He8iPQC27YDQ7HdzVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpeKqZXNEEGKfQIaPuFQ31bGqEJiLimcsLw0OHOVqi5sB07nzCdGWYYwPvF3ogm6LpdpSL97FfJsgs16RYPsZboMASCGQimDY4DUSWu5N5HF0zL4C1s0r6GhELFPO1NikHpNyWQW6GH9038Sg1rL5mf_QmLb7gx1EdSXCx48CUt0VQWyQgEN0Kxcdh0MPIMMW6drB8Z99gYg2_bK6ehlHnU-ykBfc8IY_SgviTj5UGmRGbj9EX-pHdFwyRoqoicws2NojB9sM2DZeUSTELLRF3GbKo4KwBVRAkfnWudabRIMi5YkQriC490M0_DZgGbAvbJprSq6ZDt6LzE7_MX14g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEeMYb5SEXgVnPCeRNpRLJZO2IAxwqi5lo8P-dMXtBWpkr-P9T2Wy3f2QnE3xul3medgE49LCPLVexA5KqBCQ-GZuQTAW70sfowqMOFRyZB8bE69OhhPkfxVdx2dzjerm6RrXcnYy_oYwx6CGStu1GqdYbfW-UyGpfNTtderT-sRQzDlsayr9UMvaj8doWm-g6WC5ecJfx6vK4x_rU1lX8AkZ2lOzQ_CmpI2xa7Q3K7ZSGwcIiFSLOefOWchmr0ZFSMsDn4VAKImJZNu_9buadhc5Yw35dszfOzRcYl1W14xXhMYjOGacH7ig1GCn0aQaflShRlH01hGEp9EX4EQ0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=gdRlA8qk1GR0W3ulNupU9NB1ZS8JSim3Aw4IV21INjpcl5T39y_H_ks_WYVyS6Nk4wbtPM128kaSY5DrAlq2JaSbZuzF-bD8f9fsrka6F7Fjo89pYVxjqoseQauP88eizxVptHhc_hM0HsZ3_2_pI2ZXqwT_q4C_BNWoQgkwKpCvwyepzWkjnor_AQY9T77bToZUW3SQc1c5yQKIYjlYfu1vjYisD84_Tb10PzduFf12KPrHxG1hOOOUmPJFWV1YLAh7Q39PnJ-1FRyliHhyQev46aZ6pwz3tRYvM9hOknItsK-_qPRYNQStYBBApU5SJmAcIbnTbMrJkHuRZI0jFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=gdRlA8qk1GR0W3ulNupU9NB1ZS8JSim3Aw4IV21INjpcl5T39y_H_ks_WYVyS6Nk4wbtPM128kaSY5DrAlq2JaSbZuzF-bD8f9fsrka6F7Fjo89pYVxjqoseQauP88eizxVptHhc_hM0HsZ3_2_pI2ZXqwT_q4C_BNWoQgkwKpCvwyepzWkjnor_AQY9T77bToZUW3SQc1c5yQKIYjlYfu1vjYisD84_Tb10PzduFf12KPrHxG1hOOOUmPJFWV1YLAh7Q39PnJ-1FRyliHhyQev46aZ6pwz3tRYvM9hOknItsK-_qPRYNQStYBBApU5SJmAcIbnTbMrJkHuRZI0jFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcLZ4CIYKKV4rQD8ZWTZWZ8muWr5TDTku-1nYp1Jnek0LV1MjSNcPAEyb1oTnnOkJV4JoGqB_UsvtV0KEOBkQ4bJTSj1phBEm1l5AKN-pw1fUpvg2WtyXRfeC0Pt8Qc2pB6CHiDpwix4kBrn7uLgGmIXXC94XvxlvOTf0NcPL6QG7GNA1o-awkdBLsxk_8aarPbog2yx-xNaEs8sCBJnSw51kfYTdlIW844lVgdWdPfQNPslEZPW9gIWhnwvUao9vzKOYCL681PzvNwOyWyarNQ_XlZcsaIXwHP7G1KQ7mBgzRxml_0v8SFY7wQVjXFHKVY8I4EtK8285ODcphWKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFmPx9HqJLTC7ZfVrpN7aSmaWH_De0P-hLH1OlT3h942JIr0xLAZ1Pg7qBiaJ7bEYYz4VVaF_dW_N5wzMH41xXlrA1BowYI0ryE88SZU6EyQ5hIXQ9LXK53nlyTzIPEbXH1Qv8gUFvcGbnqOhks2ORvIwlGU_pFMBpBTZH3jCzXGZyhLU3McPfXEN60ywC3-qu8dOvkFUrcP8dVIRLbyZjCMZ1HM4TzBt-bjr13kQ6la4QA554RuVeR5KVgQeWwHqWs_w0lxAJbzB2jnspDfancBpKBDH__xJ7AAuQNVbM549WwjiFVzkZ45sMlxZ-8LorRLuhP3tgCkSoDNJlTi2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=UUhc0OMMfaQL94xxNjBDcfoRKvF_sVq-tYkPliieVKjV5jL_GiSu1MRPPaMQdRpC1BPUw6WRNeA9iH-scR8N1YvrOTCjah3-jb4qAk-VudUIK19tilfUhbxW018yDg3MXCNtcJfJOuOVKJ6dpObLugXhEoqZX9teq3hZvLMgmjTb1OK2OoP0kUswUm5g11-WHKb53jWL40WPKalCPp7dTeLfWF_xoqaw-qauTIhtwm5IT3luyLhp7syshkjiNVOG3liZTY6twvx_WhVAyorBsvP1tuIhd815M-x_K7DcHMup4oG8MRzmNaqKUUjzQMmDrh_tQ-hZIhngrzvW2H1lyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=UUhc0OMMfaQL94xxNjBDcfoRKvF_sVq-tYkPliieVKjV5jL_GiSu1MRPPaMQdRpC1BPUw6WRNeA9iH-scR8N1YvrOTCjah3-jb4qAk-VudUIK19tilfUhbxW018yDg3MXCNtcJfJOuOVKJ6dpObLugXhEoqZX9teq3hZvLMgmjTb1OK2OoP0kUswUm5g11-WHKb53jWL40WPKalCPp7dTeLfWF_xoqaw-qauTIhtwm5IT3luyLhp7syshkjiNVOG3liZTY6twvx_WhVAyorBsvP1tuIhd815M-x_K7DcHMup4oG8MRzmNaqKUUjzQMmDrh_tQ-hZIhngrzvW2H1lyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUSXtDYL_fgXNy0HZF4-P44adnqvcK5sMBvKE22Rdi7raH7u3QAigGdJmyigUnik7oInVDwH9R2PYZQvyeDGUd3d2c9INe7R7UA2op48iXA3I36fd4Au4XlTnk4UBz4FplPy4CIbKc4UTOH_6e9_axvq-acYkUtMQXIMaT_ElcacGr9xgIFianABvakSqRck9CXFPgdD3Q9Y5muOvG-saf7dWnyXs2HXfRYwynimH2yXl-x36GBM6s9fG4XGGE9vy2fHvqzOw3bud4sIeJXSH792x6X8HuWDX0QkJuiGWLLfR_8e3opPAAhvdhbwY-qANOOc04iMOcaAi-BilxT-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnI1GoT5kvtdRCH4NIp0QNOEoDAdbR0K-FzbSAQ-hydLaKQuwOpURafQ3WEpdONQBGWIVP3PJwTz4G_7CMs0h9Eag2pLcrhaqDrjnWqLCFvwELzwt7_FnwXXEz7fJkJQ-VPLf1aXl9i-zc8rW_WpCmWkO-0SWPt4cAWzQOfKdxEQohYD0lI3rb_G8MP15NljYbKQcyNmewgdRTJe1AeWZfBad10cCQDbli5grJ5i4fYaImv4hKpS7l9lJx6u-K6LHF7rYPEwNBIPSjXl4ZlCGA2YNVd746oPes182jPf0B9aISIcjOj_wdUzN1kMYC8qTwCJwZ2OR9ZZH0-vczp23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmNucEVKb5s5gSmxTlu2p23ORmMp99jYX0cszJPKcHoElv8glqade061iDlogs_pbhazMXNBywBgw-EkcGStMGIAkB2ieMgWL2kzEmnGHjls2rcQyI3DeM7mD3BuScYzaK4OJVwNMnEJ_JzH9_PTG6QRV3_ugoPwF_sBDw7Q3kxNZZgDBRhjlEmo0HSOequAoUFYx_BAw8bLvYoefbPFRuHG6Xqz_3zsLKdZtfxKmoiNqS9jKddH0aIqhSfWmROmXoXNKrNu6p4yQa4u3XfpsRKw73pwbUNsnOlgSv2NtyCpMnXAQRQcmRc6W4732whX9fb6jjjrdq-MQEominKyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhxvVMxpQ6nYMreGqqYP83T38eNN_PjoJElrcJEIcKZnkzlEQfWhMVaivrXs0_3HBvNrc2uCe6LRuPdAtvfBYyRw18Sw2IH_wx9L_LJGLIOyLy5lXusfrLWbI4ZuTd81hRiGOg0eYa_wjeWojSrnMUx2wzNyyttlqMixYd3wD7BskgM6eKJfasae9FQQzNTXTrWLWjRpuoAELskYVGO_rKLEdBlmbe6ULcNhYR-9I2vvUIfebK4buQ_pB2zC1aduUYBK6p7A7W08S6WkvegVD0RwSL-Wc9Khwx64ei9awnr6WfM_xxVsoJAohhPBrpD0gWhz9GZqSbaB04ZP1ZshYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5ICs0avuCQqp6kKTbeXSYhKmwIV1AAjsXCc7n5KtNqIV6H_rQdln7c1_MoTpfUevNKCDVmQx6hlGVJ2xcO5s5bNWaBEr1uPRrMYKhkmFtEw2dMR6K5M6cbCaW0K41ahzeF_FvIRZPGtu2efsYU2npvNsMylABXbkXQqsoiTvVhQmLKa-4z1uckHpfromxiv0V2aaceIernKyP8XHAxjR2b152XN_pDfkezk7fIiqhFKBXURHKrFHeWbRFbxQSN-0xXeU7IKk7o8xCy30JQVciFBzoyP_TlNuo9hbSjNxEwFCFBCxBOadHAEFB0zTHPV5_glnvqRcDLhpxb8tvthTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abe-Ry7D2cWyD3_YdQwz8MjjzxqLvhQHMcWprlk40zC2LLnGVA99swk6DRSLZdQVXg6BXr8ifREFO9eViJxMPPKJlyVBrelrqUUJIWTsPYqjNlPVvD7wVXEo5oMp0q8uvSXx7TQ_0-WgjRpxgDOTyv9vHvTLeWuEHJuBPLdMxd9kpuNiG81BUrhw8oASCGRHpEmOQ86vg-ZiXI8YARHgWaz6G7MnxpL0iyVCRGCkkl14Ggdwy15flOnNtE4C1ZiRdwga5Bg0ssoYJvSG2Iqv7nLwOjxTsCax9eTX28GBiKyeazNuV0Ngh-VN8KgCD8KYasriX1_fpn4yRuHQSAw__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEl4rUO8mWTihRZKFu0MNNOlgNfuNngN_6Axepx2kHW5oyIM9tAKANBvlc8Oe95CFSIMKMjd2vC00WGoqm-Q_E1gTxTGOOweSIwbNILb_jKqigJ4aUD2ojy65OD7NYS9AW_BzYs9W_SNaDqEt6HCDQOO_J7PNi-jDElO8nzVHl4e0F-8M0XMqgtKuHn9EN3RHw4tmgM5YwbCsHtre8LN-QcxknogCEl_G9o6l4ZsId4_QG21WNswDN7E7gyj-HEweiY4r-wGhIEWgGuoNq4GOrOljGO2LoxIuomZb3ycR3X6chhGIm29VXSMpyT1aYWGyZnJhp6mMXTlSnshaZ-wqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgipfRTEORfXXS_wzujaVto7OziOd8NbWvYhMzibpQJY2kVfzvXve_KyWMLS6sm3xYIiEiP4zZaaSDmyWC8jLmQlA9tH_G_zW0N-g-VBgzcoM_X9juSwP4JxDiT6EYeU4e2dyv_2XmEuAvTgH1qFxDaax058tzVoK2F0SflYFb3itS7ZrLuR85w9OmEMm_kuBPAth_0Az6aHqCsQWEnCMko610K2SQwhxxS_lZDhy41ssp8jMzZ2NdEPROYoDlzp1Kph5R8WUQApDLoUlL1G-IQ1ipKvcCVc9smfweX0k4ACKiXfXMZxv61Uoo17vaRWVVjuIDJXyeY6exGgokU4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=p-a-sRfvo3crYJos2iV-dnxZZQ3S9vKwdWB9eUgyUW-fxvu4WEaRVrxOrU22Rnmyunx7WUBBPqwAVdW1o6X49jAjoa3HgVQAS9EYcKoWLmEtHwEKbVBGRMBlVscLc94OJSkMa3abu9CvLEByotSVDzCE1chAa1Wr2JVK3I-Pj-YWnlUc2mBPeTflb_2063JHi3ugPbmjxN3qCXiCUalhu3DxhgkXggcuO6GZiI9tgNfAzFKPs_tVo9fZ56UNxyBNfffK6o-TGFG_HLV3d2Cc94DpnfQ-WNHz6_nvC1Y89beHhzaN2na3HjJ0086lz1an9rW9BuPNXPODQCapPLnL5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=p-a-sRfvo3crYJos2iV-dnxZZQ3S9vKwdWB9eUgyUW-fxvu4WEaRVrxOrU22Rnmyunx7WUBBPqwAVdW1o6X49jAjoa3HgVQAS9EYcKoWLmEtHwEKbVBGRMBlVscLc94OJSkMa3abu9CvLEByotSVDzCE1chAa1Wr2JVK3I-Pj-YWnlUc2mBPeTflb_2063JHi3ugPbmjxN3qCXiCUalhu3DxhgkXggcuO6GZiI9tgNfAzFKPs_tVo9fZ56UNxyBNfffK6o-TGFG_HLV3d2Cc94DpnfQ-WNHz6_nvC1Y89beHhzaN2na3HjJ0086lz1an9rW9BuPNXPODQCapPLnL5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/se6OTRvkt7MuoI-LSJZ6DPGOK2LH3PFekto05iG0OCvq7Ym2ekAZd4H_ASzqxDuqRm5992l9jDSzd0TSH3Wr2AKcYEtyoct6_DJL3NfvZbqc95lWIwAslBAvI6LL-8xLrP_65SiAtrZeGD7F6QIGGvhJU6rq41L4-yEBuToCPiJ1x0wHKc9PxamxL8HZzkACVWIwCx5vuq6v-x5HOXAfwQ4qQ8JNUEyLr0UNhQyAjjfe_BDeffk8XL49EIxW7GF8gqBTF-n9X_qEE8pzwKjRj5TD5oVAQ0OuVU3cF96gFv-mJRbhtDVmAVeyS2j6KQX0Dn4ItiBbHeOCA8V7_82i7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=AGgaIXCRvswUgPkaWjgJrJfYnoOVHD4cq5r6xeiZaI_iSSB8a4HZB5JEtL1HzAuPrNtjdt0OMQparnLx17n1eb24x8Xuys3vq_Su63LA-uCAMldf5gEJJSorYc7ug7fFH7ZCingbbnMlZunGj8P7ct62eJ3TPaDrIbZqG1yTGk42OWbWFRXtB0WfsMe7LesF9t_CvXfpKNW5x2hUGpRaAh7iSXW00Du53vL4SH0ospI7Uq-hTmf5X0hEeCRq0GfnQS8JejSsDfpraKbGYeC0lUky63MudveW5G-QuOUw1eYLLo8A80YtNg6l-8DCAV4HMeHoaAKqiF4REGnmPo2Z8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=AGgaIXCRvswUgPkaWjgJrJfYnoOVHD4cq5r6xeiZaI_iSSB8a4HZB5JEtL1HzAuPrNtjdt0OMQparnLx17n1eb24x8Xuys3vq_Su63LA-uCAMldf5gEJJSorYc7ug7fFH7ZCingbbnMlZunGj8P7ct62eJ3TPaDrIbZqG1yTGk42OWbWFRXtB0WfsMe7LesF9t_CvXfpKNW5x2hUGpRaAh7iSXW00Du53vL4SH0ospI7Uq-hTmf5X0hEeCRq0GfnQS8JejSsDfpraKbGYeC0lUky63MudveW5G-QuOUw1eYLLo8A80YtNg6l-8DCAV4HMeHoaAKqiF4REGnmPo2Z8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=GfewtQJLw2bVAJEyHsM7BCSvautMhOyUfHA3KR_NhrtwZN9dt_yd2ifDXXalRfeMPUD0mKcP_U1MXpRTb-Oiz89E6m2FPoT6AAoCjs_drXR95RCCI4wcD4vx2mo6u6ec8YqhmmYqoCh09RP0TrGk9l1-P73Wv5uVGEn9PGcrzlQICMHo-A14ggc8gbO1KzeqQnm5aQDL62Fstb2bu-M5Z5heZkw8yP2u3nf0X1P2OObCEI-eFcAAxIeHb5oGQrahejVhaR4WPSNmqbhV3EsHgZnTtYQ2YOD9S8HUBwkrcQfgYUgWaPkflC1QaOXxEJjMVwChLjO_qTPxu2Kmk5Ov6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=GfewtQJLw2bVAJEyHsM7BCSvautMhOyUfHA3KR_NhrtwZN9dt_yd2ifDXXalRfeMPUD0mKcP_U1MXpRTb-Oiz89E6m2FPoT6AAoCjs_drXR95RCCI4wcD4vx2mo6u6ec8YqhmmYqoCh09RP0TrGk9l1-P73Wv5uVGEn9PGcrzlQICMHo-A14ggc8gbO1KzeqQnm5aQDL62Fstb2bu-M5Z5heZkw8yP2u3nf0X1P2OObCEI-eFcAAxIeHb5oGQrahejVhaR4WPSNmqbhV3EsHgZnTtYQ2YOD9S8HUBwkrcQfgYUgWaPkflC1QaOXxEJjMVwChLjO_qTPxu2Kmk5Ov6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=v3gqFUFW1oov3urb_H4iTUjyrCLOPjMTo2vJdhnjC9967TyoHvX8m09LNVMlG13ibLboskrzGLa799lf92kTWdiOOPildMx8XVblxabTBG6DgsWhqqOmBP2h8sn2jXjeFu4RjZVTXbEzJ5FEUOs5BIp1FGpL3rMlqjXu4axLEzRQe6BPqPK3tiuN7NqWjJvMMvAEnq9ZXc_891-rbmpk5L-MH-oIibgU_JBBCiClcgUOcTRxIsqvnkPcgLFUAYnxpspHo6wW6cJfocCHNP1lc6rf8F_DhcO2RW4BDjU069399GtmsCZStrUPSKeI2w52N__abyi3cCH3rDjkdf2byw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=v3gqFUFW1oov3urb_H4iTUjyrCLOPjMTo2vJdhnjC9967TyoHvX8m09LNVMlG13ibLboskrzGLa799lf92kTWdiOOPildMx8XVblxabTBG6DgsWhqqOmBP2h8sn2jXjeFu4RjZVTXbEzJ5FEUOs5BIp1FGpL3rMlqjXu4axLEzRQe6BPqPK3tiuN7NqWjJvMMvAEnq9ZXc_891-rbmpk5L-MH-oIibgU_JBBCiClcgUOcTRxIsqvnkPcgLFUAYnxpspHo6wW6cJfocCHNP1lc6rf8F_DhcO2RW4BDjU069399GtmsCZStrUPSKeI2w52N__abyi3cCH3rDjkdf2byw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pCzPs1Uyw7hH_DV0hfl27awgkbUZy-go5Fb0HlkuTs5MqaR-FD4FVoCdJ9xbaHENvk7qtcUKV8mEgoZYwH1qneq0eDkUuV_aWmpF233GkAG3_ryPt2vBXip5Qj7gFwCfHShISKB4UjmfrfsfhHmJZ_glz7YlLY7Ma4SwpBcUZ9dyQCT-pH1JFPJ491Urbyzdd8TuYjTyFNOoJGtJ1VaQzsYunDnItC8s8BG_VOXg8nxEN41LB1YWnk_YFc-HBltpZdE6V6_D31ApBTnlmx6_5oq4soiAMcoaYeogkHfmOcJPS4g8v9_7mZuB2tiJLD98b67hHy--cjYCj0uSgGoWZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLCk33UxUleLb8C6cBcoWRob5xdf3K6p6Xse1qWqXVTl7D8bkiPFKPG61NGJ-nxO-kFKpW39jArkNYNnEXN4_-4hx8i-Qd9Rt2T-I5vAv365CT3O7AFIUNP6kslH1_1T12ohz8u3ya3HuvLsSqF_R3ewF-ch_UVa1A2o8KhniGsUtgWnmscdJKjDtpkUnDqVcsIxPfe26PUkQRlwLPmmrlYv1dGl1G3q39cSC_LCSdKNh9zkGiY-LCNRZBCEsbb3xAQCTIEBTgE8AyKnAl6ZjO_6J6ay7cfWoBjLdpDKySM2fcYR4Sd_RC8AggW-q2OUWloEL7gmm-kfxfzlSfHahA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=bVJvwZngG1TcM5M4DhKoCvmAVJ6hpoYFj6m0vZAGCz6SpMRnHPzR6yKgbhyrMO7iePi9KuBBefkpAn1ZbNAU9NyTukmh3rZ4u5LpVIJzwYCB3nviEzTkl30FtBQqB3uoqVI3dHOU17gQoryqvdmHX5YQn3t3LUIugRVNYWGF9RU8LQ0fKSNbmaL3HFbdW1GgkmzChk_Zj4tTMGIpucyEcLyEYxDv1L7yR30nkxD4J56J8r8H8WokTHmuWd6hH8Y3jPaVoBqALKb4Uujgz_ue14Iwz41Z2E16-m1Ccc6AgtSZGWYRPCG6vZY-ami2H2pF2teEbu5cnWh2I3JaSsu2Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=bVJvwZngG1TcM5M4DhKoCvmAVJ6hpoYFj6m0vZAGCz6SpMRnHPzR6yKgbhyrMO7iePi9KuBBefkpAn1ZbNAU9NyTukmh3rZ4u5LpVIJzwYCB3nviEzTkl30FtBQqB3uoqVI3dHOU17gQoryqvdmHX5YQn3t3LUIugRVNYWGF9RU8LQ0fKSNbmaL3HFbdW1GgkmzChk_Zj4tTMGIpucyEcLyEYxDv1L7yR30nkxD4J56J8r8H8WokTHmuWd6hH8Y3jPaVoBqALKb4Uujgz_ue14Iwz41Z2E16-m1Ccc6AgtSZGWYRPCG6vZY-ami2H2pF2teEbu5cnWh2I3JaSsu2Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=nuszTVvINstZaHkNo70-9hWyyHtVpirhD3EYQAxV2SrF-jFHAM6ZLf28YWU81Vi-evdcXqjUNtbTtJy3Lj-Gg-QYzOtVuEciyiz6CTG37d8UWFmIXAf96kH_cL8j4J11WemjTCo1nCjOpNNMD8BRnR_N3cPMU4-te2CyNKZNEsVkN66GW-sJYGFi4v1FgDYdG_46GJsZULuSONs-HVSXhAOyroFLrep7nHC6-mSci-i1im0NsI8-cx6kZeT6YyXayDfQlEAlXmqsMdLDTs1aAQAnfsjonxidvn2tfobgpT0k2xowEWTktTogNTVU-bFtsSbzdEaOSsEPs5HP2RYW3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=nuszTVvINstZaHkNo70-9hWyyHtVpirhD3EYQAxV2SrF-jFHAM6ZLf28YWU81Vi-evdcXqjUNtbTtJy3Lj-Gg-QYzOtVuEciyiz6CTG37d8UWFmIXAf96kH_cL8j4J11WemjTCo1nCjOpNNMD8BRnR_N3cPMU4-te2CyNKZNEsVkN66GW-sJYGFi4v1FgDYdG_46GJsZULuSONs-HVSXhAOyroFLrep7nHC6-mSci-i1im0NsI8-cx6kZeT6YyXayDfQlEAlXmqsMdLDTs1aAQAnfsjonxidvn2tfobgpT0k2xowEWTktTogNTVU-bFtsSbzdEaOSsEPs5HP2RYW3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
