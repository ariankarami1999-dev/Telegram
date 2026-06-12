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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 20:15:04</div>
<hr>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=B5fnVtnz-zDq_qaGHzC9YM44M4_7atKagBNH1UJH035cpEy1wP6DYKK09waQJxKbsUk6ERjw0yXwXemA_DCeCxIRFMszgzJ_x1K35iQ_-80WN2NBxf3Kj2-H7Mt9eUD1DC2z8rH3bUhoOAVa_2bCDQfbobS216U74v3ShPLFrtq6CemKJSrTea1mZaPWgJgvrSdBQon1sSWYtusPmmjBMjt2M8ABJrrMaTfzLhnJig2XnVbh5iFobd4n5lagx1SM9DOCUvUOlh7y1lCpYINaKGXknkYeJBqfSz6BPn0wR7O4JdZlsjGgPBeen-IQ0-peiqSsYjoZpSUIUKqdRedEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=B5fnVtnz-zDq_qaGHzC9YM44M4_7atKagBNH1UJH035cpEy1wP6DYKK09waQJxKbsUk6ERjw0yXwXemA_DCeCxIRFMszgzJ_x1K35iQ_-80WN2NBxf3Kj2-H7Mt9eUD1DC2z8rH3bUhoOAVa_2bCDQfbobS216U74v3ShPLFrtq6CemKJSrTea1mZaPWgJgvrSdBQon1sSWYtusPmmjBMjt2M8ABJrrMaTfzLhnJig2XnVbh5iFobd4n5lagx1SM9DOCUvUOlh7y1lCpYINaKGXknkYeJBqfSz6BPn0wR7O4JdZlsjGgPBeen-IQ0-peiqSsYjoZpSUIUKqdRedEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg5kACutvpkyY3sNxAE17vhfygDp0_U4Gpk17VX9ydYMbkReSlIEumOIdAGajs6NqkqrhyuNrJgqu8q30stWVyv0-v5r7Fdi1oQEqELbiun0h8U7pM01qXsf6PLqlHJ8zr8EI5rsPGJ54MytzEIEIT9Wmiu47yWv_vaFBMjjQnyjgD2nRFkyAKCk3uYgUThUSIqB3KNIpme_38c4rdFfFuZhqW9H8j_fYDTFw_rqfBHh83qd3GgRY0q2JPhElvPd-dEhv3opYyt9B8zAPt5p6m1GQsKq_b2tAyMJ2QpMVP0EKrdhcJzdL59v5EqqwDQW9gRfUjx_Iwi75591lhfJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=RcYulb-NLyH9YavVDYWEXvsa56GaDx9sjwfYR-7jn_4LlPuNueZgAtoC09Nnsh2oqdPoYj68Cx_hkWmztXWfWkzTce9Mx9mRFNj3KqBNo3cM_AxExF4H6eZkTPtmZNN6tSdwGPkD8HMH5j1fS9mMk2cK-B8aLQsq_hsjf9I8KvPXP7AbF-JHm-WG_vdB8tWZnRJW6WGMdW0YBSqmSFJlvyii0XrSJb9Dv64Z3beC9toZXSAl5kn_w7NJWI36PDu8dilgYoydQoyzTyXietKo6DFiuComjOordPkIr4deeqTP3DqG1u-tw5xI20bBGalm64qXCdVE5K2RwPboLzj9ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=RcYulb-NLyH9YavVDYWEXvsa56GaDx9sjwfYR-7jn_4LlPuNueZgAtoC09Nnsh2oqdPoYj68Cx_hkWmztXWfWkzTce9Mx9mRFNj3KqBNo3cM_AxExF4H6eZkTPtmZNN6tSdwGPkD8HMH5j1fS9mMk2cK-B8aLQsq_hsjf9I8KvPXP7AbF-JHm-WG_vdB8tWZnRJW6WGMdW0YBSqmSFJlvyii0XrSJb9Dv64Z3beC9toZXSAl5kn_w7NJWI36PDu8dilgYoydQoyzTyXietKo6DFiuComjOordPkIr4deeqTP3DqG1u-tw5xI20bBGalm64qXCdVE5K2RwPboLzj9ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzb0Pcl03Qh68m_aeP1jNKBdkDOSbZVwxuVfUTcFLuW1Y2XQCZr_HXYGeI4RvVVYozacCN2V5e72k0u9JRDGrd9cJGGZGC4yd-h4dBQCzcfOO5X_AYndSJ8E44SBJHRqLBP3bjKhZlEWWQl6sy9hQXUN9BKpwIra3YbvY47DfTfXZDaOZVM6ftYvsLoIAtCa-HOiEPbtCIP3LU1ywhTi11n5H5H8Hk239YVOiCnqadimOun3ZsDwxQYfMBgZHRh5X6a4-L80K8dEwcjQxlHCKdP6XzozW-3zUyu3o6xHI6egGeGQRaU5TOvCJVtsoltvPt2aK5Z680eRH_ZjOWul8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=hKZOZSLlvmPJgpQYIu5hn3Zy1i_Vv1mJuMt_3coQgYMa2VLKrWQHQq8xwxVyWZ_xtJRF_n5MSPN5h19GTJh2sTRPkHCmknMwxRyWk5okBrxrm3pIjWv_auryvKXsRQEDtsoPBowrTag-XMwRnK6FwJyesxYr_qduVVorr61DP_7q2pmJ4kpcXOy-no5vOu0PS-C_cDmc4js4AX90zTHRS_51V3tgyhSmpXzng6fZaYHzZm85Pk6s9zPlS2RkCxugQFGc_8YryW7hxPpZyT6DczsRYs9Qed0tQlbWw9B72Oz99fZWLRVyBR_7eIEmqui8A1y63tZg2oGzZflAeyLfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=hKZOZSLlvmPJgpQYIu5hn3Zy1i_Vv1mJuMt_3coQgYMa2VLKrWQHQq8xwxVyWZ_xtJRF_n5MSPN5h19GTJh2sTRPkHCmknMwxRyWk5okBrxrm3pIjWv_auryvKXsRQEDtsoPBowrTag-XMwRnK6FwJyesxYr_qduVVorr61DP_7q2pmJ4kpcXOy-no5vOu0PS-C_cDmc4js4AX90zTHRS_51V3tgyhSmpXzng6fZaYHzZm85Pk6s9zPlS2RkCxugQFGc_8YryW7hxPpZyT6DczsRYs9Qed0tQlbWw9B72Oz99fZWLRVyBR_7eIEmqui8A1y63tZg2oGzZflAeyLfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h__8Q8EMfOnGTivsQtX05uS1Z7gdiY73o8orTMVI1xcmVCuQNMZTddXFVR5oZLbh2LCHL7eK9qIq6ymlA3b5EFEZEP8UCFxosRyUKFV6lU91bikxKlRoZJ7oJJaNcH5855cH7H4Suv7kr2GqoCWHi8S7RffK5Yj_nT45WPp1WCgOfXIvfZFWzXZCQBNsGQ1qRLZVODTyi33vRFYrf27HjxXwf_rIZUZZLR2W2-zV9VbfjmlhHS8gf3O2RYDCKfPE8DF7SmmcAsH-UtdNeiGbs_iE3wHzhsws9-G0iNk0UT63BLD2dWsuEqlm75mKv1IW2Ayj9xyR74Jh0D53mXJLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=RlglJR64KkDg-zl3SUBGoiXOnrmCxK7Yx9QxQNTdqD3NbjBXQAoQP8qJfIrZiGBJ7VxfXZzz2MShCd-j8xJGTv_Eja0J0BdK2_jCsH1Ad6WKhQxbZ8TFxvo8jVU_zcIu6nXIbFnLXc8H4mGx2HTJpXET6VsvZATZX73AvWAknJ0OVJCsd5_JXkP7HQKvGKgdbOP1YXpjUEJSpFAOSjzPnc0f_ETh6_IkHw_2TKtAKHgOEeWtb8-GesP4gu3ZlnWLytWyltjfouV-wY5cXgmT8reR5y8EH5Tu1v7iiu7J8qF9cAaN66XJQ-7f9G2ILR1GVXOPRpt3N4itBJCuiT2oBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=RlglJR64KkDg-zl3SUBGoiXOnrmCxK7Yx9QxQNTdqD3NbjBXQAoQP8qJfIrZiGBJ7VxfXZzz2MShCd-j8xJGTv_Eja0J0BdK2_jCsH1Ad6WKhQxbZ8TFxvo8jVU_zcIu6nXIbFnLXc8H4mGx2HTJpXET6VsvZATZX73AvWAknJ0OVJCsd5_JXkP7HQKvGKgdbOP1YXpjUEJSpFAOSjzPnc0f_ETh6_IkHw_2TKtAKHgOEeWtb8-GesP4gu3ZlnWLytWyltjfouV-wY5cXgmT8reR5y8EH5Tu1v7iiu7J8qF9cAaN66XJQ-7f9G2ILR1GVXOPRpt3N4itBJCuiT2oBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnAla-brxSe-EtswqNXTezxiWztkV9Mh3am2v5qeACCGJUTbtmnuBfMQUlvt4CS2ZsI82CGlQfKaYJrcs-EmC619jZe1jkeAVVj0Qib2T6T2b7j43wuCshlkjVr0vv2efKza69XOhGZbouk6aeNNDQ_yZEwIU4eFvsf7bqG-DveRW64_K2GQE_h98_d9yi2l9OPl3Yl31rjJNiHw6AUTDoY9y1NSyE-IJ5qwqgIzPiL51u4khK8CTjj-R9tQU6keyJ5vgRDwDzwQLqwTGtDrDwMt6hn-AYHyRoICb82bzZjNiJB6lENstbBWfpLtniENV5EeRxsTFDsl8U25r8au8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbe07vhqkMmtXln-SBm3NkJaJx3VKKhz4B7BS8deEvsgXdEcKBwB5jUQsfrF6xWoo-t6sFNgBmraR6FQtknFK-8vsLttMyQwSajKkhRxjSStHquJdBpKgrr6Xn87CMqzMEJf9EJABscakrnXTrS8GY7-G65Az0VCA5lmPP_WTe9sGGb4cbgN91_zz2-JbQYzMC2MUnvBODXRYwUEVhzkEAbmvCwcQgGf9hQv5wWTRnH8fRnOgH4CfqEmjSreDugXGmhrYrdAKY7-pCJf2x_1x51hHd7ExBaRCKye-zsJ1W4mt5qYLnRvqJ_pv8kowhsa8JjvnuenhF4305ENVu8rcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-kbD3uNlsdqMMfklUU4pXW1_3QIWkqKI8QQEem9haLCWWv83n_CTGQdMBE9nxmbaPzjEPMhkb3SRlAto3NyUEhaqjraBnFJoFG3NVKvdFQua2EKSoW_-ZTyBcgSbyR7YcX-50pDQaXzjkJKNJhKWT0Vy1M0mRE4SmkiezaNFpaIZl1RqeUpIEJzYNBo0wtNnfn_zFXtozs5SF-a-nTb_ZTe0tdXLutBVfgQ5WRXPwgu7uV9v5fej9ZMRehM7_0Qpo-PRcKvCupJ92xARBM-les2uTyqTix7DDdS3lH78fMhF6H4aRmC4LXOUoVbSiYlYU8qUCJpcTPGQhYSnQYjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppxVxfCRkw08pUZMw7eoU3i2W3O6nvt_adCIy5SNZWHrV3WJNMNe3Ymf10pWJpkgvpC5jQvnj3AL5Q-LYY2VNGUtbY67JMZvnsMgjWHov3swNNY2SO6KSybvtHuwWv6OsjoQ0xI8flbnB9qyUvqkS_unlS8-pJnOnHaplyhXT5Hieh_8DEbjwjhJ64Nthqh-lgUcHHIYmN7SS8FoCGO_Jimiw8dKvKP7r93_e8ZJOUrFs20xrKVstf2WSb1PAOUFdgH58GwHaeMRwtKAP-6Fmawv8yBPHHAi7KqPK-0jBqpywkZXc93Dc31ODF77Z-VWJTBDq_crd7b6n68_6QEIsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqbKb_7PyVysc3nxCJe1VovSk9KlBGCzf2gBDdup2joBRHgrXCnbjA3Xjgt3z9jbv3YhYCY17PYnGt2d2wtt4wRhSDpgZ8RoQVI2IlZkbOljSQos8f828CCBsCuIVBylnSuf-6ocW-nlsX9xVmLzp-V9hJINxsSYFSftsfNzdCjCLVQnA5JzBLKOlZmOM4_ZjrFDFwdHqqlSo5AtpQjRiUan5F4Hq93LbbV6HetUI3gZR6CRpTIBEhclPYsEt31R2Gixj_YPkSytZYTO0WAwlOi7YFwfv6DTOyCs6-OmYti1nYSGte2eS2M5JY1M6Q6kHqZpWcqc40u1uWpvD6ACWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_7G0qFiAI_Xsgvkr5w1TM9LZa0Jh3w7tzzHvDPtpEtM1he2WQOsJh4V9zKcv3Xl7IFFXVjqztMEGqCdqdNQliRZE8dAIpvtFEcIiWQQwuXpNDhjls-wyMp75270e-fIuIZdcaMbJI98JyFfWNjBtS2pyJrwL8k_-48ulEk7a1YrwQQ-xkkhSomVcyEmpfthVtzUbk_ql7ipmN9ih_LOQFWhJcRMy_JVke3ZitcrS2wQjk2YrKQEObjQzKtlRP-PEl4MNfwVJ9ZrR_oEl2ROQPEKRHziTEgD0NzZS0LyfWrOPcG0EtUIuhD7GedtntbXDt4LDdhCtHjl0KDVoTv4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=W52L7vcZdKywj9BlDTeJ0YU7K4pOgBMH0V9Y4hztO8wzVosGJdh6h9QmYvVLURgqt7IjVkBOpZ4ndiKk7NMkBMckvhubDeEEKEW843nFpiv2F3jbdNJmj_JZdH2gOOTAode4rszWfub_1N3UTuuuWFfGJsuMRys7Ljme6OIAY-rZNFlqW9Q9yTc27H2ChBGuS5-bMLkEc3ZRTf_aHKJ0wXP87ebWvy6P56x8T7x4F_mFOgqvHthDk__eCwbJmZq40_OC0t1AoVRJXeuaPoUGkfVqs3qFPe4kOfnkb5JRx7C1V7a0BT0GdGasBdUl7XPwZtJGAGyrfauerLdnOeUc4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=W52L7vcZdKywj9BlDTeJ0YU7K4pOgBMH0V9Y4hztO8wzVosGJdh6h9QmYvVLURgqt7IjVkBOpZ4ndiKk7NMkBMckvhubDeEEKEW843nFpiv2F3jbdNJmj_JZdH2gOOTAode4rszWfub_1N3UTuuuWFfGJsuMRys7Ljme6OIAY-rZNFlqW9Q9yTc27H2ChBGuS5-bMLkEc3ZRTf_aHKJ0wXP87ebWvy6P56x8T7x4F_mFOgqvHthDk__eCwbJmZq40_OC0t1AoVRJXeuaPoUGkfVqs3qFPe4kOfnkb5JRx7C1V7a0BT0GdGasBdUl7XPwZtJGAGyrfauerLdnOeUc4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPvps2Zq9DpG1gQVjgQVUiCm1XIU82xl5QCH8FJzRdd9Vsxd-4S0KHsda0u_wqoxNjJ3_zJRz1p1Zr2nnbL90P5ayHKFC1GRktlpfaiSazqzgT9k2sqJ8TT0X5M7BlF8iupb2YtI_KGv7feTQ7bRq7mjXdJcau1900ucFDvJ-QONp93ktvnXISC5NibtPO203-gji4KB5yvhveZrI2tuCSy8329R3gUbNOP1gx-4rtWp_a6SSGjQn8i3G4UQaLJ715U-YqBRHJMIep6on7m-pA_iKGYasKiMBqCpIZmRIblIc1po_HP9IbZZYSAemV1-Znz3-G1zCskz74GZq_0Ydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-W5uSs9s6EpznxIzLIOLo72D17pcnwmdYKWBFQyQbV4_Jtc958VCM3I-7nAOHkzlAUkYfLr2UDfWESXBwhq7-od1LifBE4uMCuAM9AeIL6SBJGBtvOMeiRMkZMtEbTfN8NBlphwyioX5-zZ9v6p3ipaCSBkHxK3RYKO_8tAjmSsXrQaUVRthZHBBY2hR0-aDPe5nU6Giyi83aRqC1BIUhq2qMsP7HaIBksr62yM3cBwLjtO6-yGkHY4BUnwN0AYef71zuyfC6GhKJNoMnWQ5BSX2KqEuIYVsXwqlIOML--Dsnd-UCGQ25LFPRgXpyeTjqFihvJRULLKQelNsUI_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFoDyLGnUe1RVlhbIsP8I9G11PPM-QZPf1o40o_0Jw59X8fe99b6QDTSqftAH3-MK_E0sRYS05a613VUuF1gW1RaUYaf2Ik33Yk0uqfksHq7ioUpf2yKYRzvyiAhAUMjO9CoGX9ZgxBQPKWaiH4E7XVIvFbNc1YG4kRdAJhu9cH1GiMd2tCODV11niZRfBxumjmffIDOoUO-9vYrMB8CQzVdtoUinAzW55cE4yWfkmT_y08ymeX0B2UJ6eIIjIIH_K9dM0eyh7gatViR_frTu_8Qs3Za3A7z6CYmcZp5_oJSe-5eaMEmuMjS0gDaK4lOq5gCgIa-KLM47waTQJIYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdM-IS-MGGBT4S8pXJlmlAvdwlcHBwHuYh8Ek_EyuNSaG16IbfW8NqTuLjtMtfgmCaqypkwvIpdWUFcAORPVhBFfTHA6D_1ac_a29c4NZkt5C_IS-JetnntZTPxVni7Yg31JYxOsz5QqXUpk3aiiZQgK7N2NuVkK8c_mJVFvH45mUmJZNxDG9LeXa7Fljcf5lvyxuAOktRzpePrk8j4f_Wko1EdkQYoGxYVdw8QGSEBPKlNowtU7c5nBvG4ycOo3hzS2TKVKvQAi0NzDBj2VONggKkZ03lrkEWHZJKkuqcHB78Wa7zvEE7Rn-nXxwtQjXHtVzkcACnciONRazDGkeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9bMsAvF6wmEi8d0mSjKoYftChYYD6x5Oil1wUKHsrO692Iils-9IKRlHy-6aKiA_r9svyggEKTZaFqk1lO-Je_X1--ErX7xrpmtyTvauxA-WOArYdqezKinwBj0aKTCCaYBrktBJ-UWqvFi8EQ4dwpsswSUNc0HpNs0l6LO7ghOQP9owfOpaS5g-wlqEn3uK_gMcFV2cwYkf5_hWByCp2n8ss2QUqWBx_fbcxNudE0yN-8C5o2stbinver1LS5mPRQPSuVXmVgmBteudhwA_ZD7OqSibj1NsCK8wNJFiShJ0yY1RIHCeZJaxf3Xrt1NDOENn0hVhwD6lbA9c2bNpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C00rctBr-C0s9s32ArNzr5P2Gca0ChoKkpKk-JAHCJzB0nZtVSIbgVt0KCV0HyqG_dU3vD22ddsVQrEpSNNMzJ35lKKVkgsECGvkpNcrU8FzvgGB-nI9IM1AoXF70h13zW9kBEhjnH7pqXKXfx3gcDSeMn239Dgt53i1L-JnmN4kSsez6BFFAmg8TdYJFWrGtZGJ5XxHwHCLb8Hq7wpmcENjDg1bXxv_HbMc30feaLqs9LUY5M2a7rJS4bttCd3Ppwlar4RqHRxJ1UP6ZzB1EIwI_NPgMQvkb4ZDysfI857M_o1_va5G1a3voWrR1P11gpajI5VdVKvy2_VxKBnSLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuuoqPXQr7p98NYAW8xABlpv7pmwPBTrKStgT3SsljnjsF70f_xFLI-7IlL7iJnZnPYUGzmACJGokl30_bxBo4mekAihvimiAuK9tL3Y2gBEpuhFKB80TCUAsX4x4eNfh0q8CQynHl2TmtZ6WJ0vKdowlCkPFF0k1aDLjp2AisGETt7o-W6a7O9DRQjtbpGbP8D1Q75N7LkTdmzq6HlQURlXg9BIfbMwcykWFtrGohZOrKB_q3RH7brQNhFSPdnkGp3pOo9laFlJ_NAZ2BUukrKsiIfNULLxNwmXQbu6_7jS-HIjrtPxxPVoKmjKO-iy7k_5a8Aw9aB8ELBp8pI3aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq1Tky53Axk4FhpH61QegHNV3xVl9Vc2PJhjKCw5kgmfy0xj81y9Q1U-P2QUi0LVZLtM9YtRP-Izk3L2ofqyCIApiKDNKtQaoslY4Xm-9UDeJNYyHntbeX8u_myTA6cxKTYsHUKcwV2hMwKsjIx_I1i9yBvBpvFnqnhR71H0bquwU38PoCG42BERCLAU5fgZc2y_PdeGlyttodkcO7No2mbQ4kYJP27hMQurTBtyFHtOe11li5JDxFlhuct47-So0jDwRmq_ZIfClmFF_wygWeEl4jlf7c0Z1a7dLnHrmiGal_JZaOSrEWxRjqXuQjZDxWPRBzL0Uc-QmEjKVDvkFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BguSuXxAklhA_WOC2WglCX5WeEQ8rDUFvumKeZIedqdt3pfl3W1yUmLFixjGTzKCOj04JDgvexJoHJfo6SCBGy3lmdta2jhcxKYTHZWX_8VMX29h1YNM1xtOlE1jB1zoDYcH1ooVaVjmVonmrIJIg7ViDtDG4HJlgSqjmL1G2Dt5oKF4b76zmbJgUhxxQZaweGrnXpn0EDAGgNEXqS1hTU8QZSXOJzgiV8-gUoPf9WHaljjJNfcEW-vTYF3vCtKlaNWwVV0oBjL1MQ389Zc2nvmDMaOMN2uEnxiiR3cbo-WICWm8JMx0QWwHETh4VfJ0psl1g4Lvm8_l4XSnVA3XNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fC2-wDsyH6OBN6a2JRwaU1QlTxZpfZPwpVlq8c4ZLBqaJWtBaTidKiV44pkuARxHe--UoS2BxolvrOR7dl-SqehF0N052qglREccc1YG7qzuGMAJ7Grq1cT0eI_q0loGqlTXpBxTMnLVwim2172FNRvGXXe_i3NR2FSlDNrkeM28ZFMKFGKdvtn2TlfD_2kkU2KTcZNyRVzhgLf8KZVIOuwi0McqyN9Th5_i9w0w1FihA8YCXxPDhzgJAmjALEkOL-4FdMUy8n9XFflgrxofgu4MJY_UVJcqRg0oEXd7tf6YpRYkQxzotKAfPtkvBMGj61IqFEqviToois_-Tcrjrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STYtRCFsgOdu-zXlsaoY4rnYpv1mlS48UnIXrmX0H_XLfsEzSj3ZGlk_QNJssfJ73QZBOcPahAiHwgt-rxGAdndF-BMOa9vX87F7hnSkOj9H9lcQ4TnVgfQedbdnuEmYgUjALMPbbpnEIFXMirY-Opf4i3Y4JK1l7riaopI3nRUrzUW1FDujkyEl-57DCGliaMK4fBepQXY-Q9hIpr1ERLo6ML_OqGpQGdspn1HFPI3vFmfIykF7YmJGYWsNHYhLC9cLPaAMTZQxxcRehuK8A5DD5YZxuHUJ1A5g93PWiaD3BIGUIgm8ahDlO73ClHUuPDM2nhlr_bJRKsCXpFPQEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6GlQqCIHYLq0rXvWQ59C3xzC-H1866sA8K4RkQpxj27MN8X1IDfqdvQjGdh7ZpIsWeXMeojoUdabU_l0TpXhncL4rPxZ4YBfiEe8bPG8zvLCmxuvjU8fMX6e_iOYA-ylMrxRALZ6njpfFFH0otU6FpJ_Kpx9H88lZRv1t4eFMJv1jI7OTHC3h0qbwMDhwE2Mhg1JrrNsBOWgcpTnHN0MAiW81mkvRddcOXNeSx0MKG1Vf9J718kmJndu-pUrgBEAxDe2W7gEfVElnOghjoFXjEFiVGt4rxVH3ZkH1jtYtum-nMTZ4P6okePubD3bBE4ewd0JBhHXGh1yrOkU7aATw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDy4_qyN069CdUYs2uVLnE_O2uSOhCAa4t-RAhMfhsLaXRVcLQZFYFQsiqMPoDmpzT2Ui80jkAVg2Pi6eNRSQ3b5LTSZ1jnOy6fSnlppFHFB9zw_BKvGKuINUXObGsvdrqPOBFsc5OJw7OIZefuycvnT7jITz2ofHupJ_dQyejnb89TAdo8KW4IhzanhCJTG9Hwsa8BVo9amnplgNEOJJYmVBb2I-lrSsz8UkRLpO5NnwWnVT5FppGLLJa2KWG1OvxgiHjAfWtqvAOi4guwXZ9AdxF7BmgPazqHCFmHzVDJlZt4-jZlPNGviqn86jY7bMiX8nW7xTuvV7E0Apywwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=lGdrEgMSktEWFIxUIsbhnwxj15ql1hI3ZEiateQ796yS87pshcJ08DJ1kHlcCdmsfqDwl_vUF2KJZjHW8pircYEES28onrq0018eaD_AWjrm710LBboca9VTk6X4iIJOxSG3xo424NPEDFfLCkRItvRkViPA0s3dwJCM8FXtFU8l_VISHebYDZ_44MyQDWDSHYX5yz3vYBbZG3kJgK4ONps1U-BKx1pQ-6BoWB0RfNRJ6wozU-kuV_QiDvgP3eRaZ6wEaD6GddTMGfDLYp3ZpjHf7xRSyOwf5hJ8Gbn0PpnLYDB9DY6DkxKsxov8wpth1zugBPbo3LlJ1XrSJXGVBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=lGdrEgMSktEWFIxUIsbhnwxj15ql1hI3ZEiateQ796yS87pshcJ08DJ1kHlcCdmsfqDwl_vUF2KJZjHW8pircYEES28onrq0018eaD_AWjrm710LBboca9VTk6X4iIJOxSG3xo424NPEDFfLCkRItvRkViPA0s3dwJCM8FXtFU8l_VISHebYDZ_44MyQDWDSHYX5yz3vYBbZG3kJgK4ONps1U-BKx1pQ-6BoWB0RfNRJ6wozU-kuV_QiDvgP3eRaZ6wEaD6GddTMGfDLYp3ZpjHf7xRSyOwf5hJ8Gbn0PpnLYDB9DY6DkxKsxov8wpth1zugBPbo3LlJ1XrSJXGVBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMDOn8_bp9lB6CxrindXsBW6dKs9aVHHp1iq-Yneo-lIC_7d583b8GRuHFKviPwMeIfNtzySL-QtLUIbr2hCJsLmNiXTtIAYZMTcVx_p90Nsk0M4TW85nBIrOT5OOqOt3XnQPcG4K7ww9-Ly939m4pgFk_Fk8AzRsRiVNey9U6qtjk7UgYhN6qFNuSpJPitkp7qoVw2LQGDhga4N_w2o0ZJ8oCeK5Bmr7SIhnSMXGF1P4OB__WwSmrSRqtdbWACXjyzweGRFPSwuz0Q4MHa8fw1ybSwic6uumV-i_EOsT4n-KT6uoKWpxRAe3zEEkfGEXKmVV-JBltjZnT7s7TVgVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py3VKen3QoGcSw9wFnrFimaDj__VIGZDWLk5ubUTwCClxidyzEpmRNHo1cU1gNh4UBUxBZm9_2-w152ETQcUTf7p4ZSfAjPZ0wV0BNQxbNdZNcA6gwv82Voxr8fHom26sCUUOvQUgxurFh6M7Kw2OSSuB9rT7V55gNG_qD8FmHvml6ZyIeQdJZkTnjwoicqdIUxipdVbeelC1MteTmcgv2IpAu2rxZP8_ZmPiKtN_lrekjG3Pbul2DOPa3Qv29Eh8eBwaP1OfaMaxeg4PUecfRW1zkJ-8T7pzrKeE6JYtGnW51gzE4vS_4izasFnb2APueFlH1y32R8y6O2JVlJb3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=ROiDOzlQGbjUGFNzFsCJqAWRXjA_eEJZa5lyjn2EaiRwCjLKt3xRWA1HjuEr9muXgpnGrT9snIzIfex2qrhRbk2v6l0C3z0ULy_DOLhekKJ1VL0JIBaOh0bCgzJhjDblAN-yISzYCoc32_xdB7h-q7J-k7Ehr9ahBMozSoo8wyiGao0gzRhRi710nF3kPc16TeLnPyM1hzawp4QolsPZ30Q9k4STz-vSE2Ek6dWOkodExLI7J0wV-pJDFJRd3-_beUgxiNPhqgI3szY_JyT4mIqXPGjdZcA18OJfLUFA_AOEjfJtadJYrkokKgccLlb0qE1IiMmRev-wB9_8j1ER7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=ROiDOzlQGbjUGFNzFsCJqAWRXjA_eEJZa5lyjn2EaiRwCjLKt3xRWA1HjuEr9muXgpnGrT9snIzIfex2qrhRbk2v6l0C3z0ULy_DOLhekKJ1VL0JIBaOh0bCgzJhjDblAN-yISzYCoc32_xdB7h-q7J-k7Ehr9ahBMozSoo8wyiGao0gzRhRi710nF3kPc16TeLnPyM1hzawp4QolsPZ30Q9k4STz-vSE2Ek6dWOkodExLI7J0wV-pJDFJRd3-_beUgxiNPhqgI3szY_JyT4mIqXPGjdZcA18OJfLUFA_AOEjfJtadJYrkokKgccLlb0qE1IiMmRev-wB9_8j1ER7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-JTncC7ja1aNK0I-Wr1f8vLM_JbJN3WkYmQ48ws6Pi7XrO1_IYny-MgI4k1_SR3pxKKcMcaTyMuSmXbe0B6yQzWnYxUqx6JrKCDaysm0UiyacUZEwS6Bmy0CvdrUpNeplh1IXk1T5BsArhfkX4ywdt8WOQloVz4yTv5oUx8i7llicVf2ItdK6C5Bz_EfGPrDWjwBmp-1E-PHhGdpbMem_X6F-BYXxDkY6BQKNLiuvCG1oueQ3lu-4fsSiWRhevY9Z3zZTzyPv0ElA_7S3mTJzkGnrVnt42CbLYaKVveBr4605xGzip0LqwKeTICPnd16gA6-S4LGdh2X5Jeia-7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQv7SX2PQSZppLPR-mW3NFr4lsZnPaEY7DAkOuP68v1BfPGfTM70RxLsDQVuTiPdpc91G1Ej5d4bFY3Bd_tTgkBKseUZIWjdhjx-zVnGs1eacHoKIIMrRBfX0QQB7My4SgdIGKPR9gu88SoQP_z6wXPdHek1Mz5hgDSQZCjGLyLORKPSmOevd2hcDDmIxlE516X2KrAO-X0AaZYBGS7LJXOp6KUjHXNviE4pLydzlwEaVq96v1hopwDHFV2hKzy3AcNJGrWOmHxT8LL75Hg7jmd7YwvdHLZHz4wuUlvgec7RffhD9CdpR8LU5TSJwWbdz4lI_cuw_lynauTnRAeGQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=gFlMh04TztLKyXw2Y1d9dPcvMv2BubxzI9qZEFfwSkmyQygLCwIrqp7XaQ1NO3KQWM6r4b_jgtMfdNe9DWdEKmviRruOmI1d4uYEooImmRS9vRvtD_ApNi3uBaYT1gCC1uSvv-k9sTfzqB_6xZJQMk5T-1u-VRS9-ETauO67fNlptLCY5_T87pakXTJ-sAtL0tSEm0YuDBku18DT83vANMFjT5DqLOczp4NFRNACgCN1Tojo1SWrvJElbykDD7eaBIO7Ya5egUStlkbIONXoK5IrwOYvc8ihv9jtuz1CDuMycb3OwAtrcs7hIpcB2Lgls3sjQ2UMLNkUhylDIBmDfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=gFlMh04TztLKyXw2Y1d9dPcvMv2BubxzI9qZEFfwSkmyQygLCwIrqp7XaQ1NO3KQWM6r4b_jgtMfdNe9DWdEKmviRruOmI1d4uYEooImmRS9vRvtD_ApNi3uBaYT1gCC1uSvv-k9sTfzqB_6xZJQMk5T-1u-VRS9-ETauO67fNlptLCY5_T87pakXTJ-sAtL0tSEm0YuDBku18DT83vANMFjT5DqLOczp4NFRNACgCN1Tojo1SWrvJElbykDD7eaBIO7Ya5egUStlkbIONXoK5IrwOYvc8ihv9jtuz1CDuMycb3OwAtrcs7hIpcB2Lgls3sjQ2UMLNkUhylDIBmDfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orhz9zMz0bDDkjgavW-2gUAb8I1SIaEG2DaO-AO0aXl0oZHdgdsmYM5QQhaw7t75SyAqDl3mE8tRkPyRsm_3SpPtwJFCrSDl84nEANEKJR5B3TqXx7jDTszb6NjD30MvkqNExdVDbDj_TczwC5PhXgCxhkUm4ezZmHU0aUnxEj-IaDpFWkOX8UviUM8s2P5CgOSti_drsyB4Cc3Kvim9otBXsEhU9Lj0YavE9KgkyiDnUkZvcVxfEoMAGX4dvr0Aim5ZQqxWkd2d1ry68U9pFqB0fI69jsi4e7gtXqT2N15jFK1PSGxrT3dKjuEzZ2EQHAs5122_elNZ00Rsg9S98Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Klb3DsFplrm8HMzRPPUMcYgGvcNZ_Alem6nSRhja0cSZ1hHGGs7o9m83W5gbsVpmkBZTegO5xekgWey_eZg1cwTLlsbjQVOHFpkwWw6NlOE1FJL3cBYP-5SD8PG3Ug7o1kIpQV7GjPHnjMuKvsTqykX3qAe7uV9LoWKww_P0MRciX3UI-JvjEjD4saOPdkWghBEfzX7CQkUvEPXwpL50X2CINGNyXgelChfPcp6RBdeoP16z1OBHqEKhou_O_SfloXMKbRaGOCHEMhqoNzdLLFmKSsgx05rduBqX-tRAPR4v6GiM_MoCb3gDqBzlYIWTw8TvChHBwF-c5uzNgc31LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=swOYNtocKrS5komj7wS0k_AqK2FGxajBLlC4axStbq9yehP2uiW0rS5g7E1NlvpZ1ek4_jg3syATad2seirnXbtiLzw3O_f8aG-KLVru_fNWXIpFDZZk162zCnjZ_k3zXFB13uLpks7d8ekQ9dHNO7vbhaRlqpUE3YzInk7Ck1sPknzw9iBL1CRqfG0Tn3-OQ-Ns-Jk_MOKHqzCfmXD7eyudFcctwWMzi3pOEOl0jL98fclHk0ic0gN-tkblMc_u--TNpTBFclOl10mkTzSrLVsUux1B3R6bJTtnIBSCQxZ2PLJyhCVei5tO5e8mvQzrbYEL_deivV313JXij4BQcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=swOYNtocKrS5komj7wS0k_AqK2FGxajBLlC4axStbq9yehP2uiW0rS5g7E1NlvpZ1ek4_jg3syATad2seirnXbtiLzw3O_f8aG-KLVru_fNWXIpFDZZk162zCnjZ_k3zXFB13uLpks7d8ekQ9dHNO7vbhaRlqpUE3YzInk7Ck1sPknzw9iBL1CRqfG0Tn3-OQ-Ns-Jk_MOKHqzCfmXD7eyudFcctwWMzi3pOEOl0jL98fclHk0ic0gN-tkblMc_u--TNpTBFclOl10mkTzSrLVsUux1B3R6bJTtnIBSCQxZ2PLJyhCVei5tO5e8mvQzrbYEL_deivV313JXij4BQcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvkZuatFUuXZoTYw8FhRuacWwAbniqdIw9BMiXUqoTokmY7Y2uWV5QRrbGv6TIJ3ug74VipJrJNpNgXPiEwNHQIXIYj9dgWHF0fPdDXQZ8iVarRhriyBP6wbrMw7vXgXOnyI3SNigxiU2qFSxWIYtAj6gsJmPBBtl6bpABci8zJW5muSEjH0q4t-QEA-GZWWnRnvkIHCUYla9slyEIQzzXvjceJaumg7T_abd9T-xiG3cDkC_EH6n_hYlQxQJ-6I7OJNKW4XN-f8ZENgk1Ao-XJxrBEWStyS7ZDjnTUz0v0G2wdJBq4YlngNc5ehwquTYfgIbYDKulluklXi1kyoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2RocHewJOzxLat7l2BynkaW6U-rmitzRwIhkLqCz3h4PN1RgRyMdTpC-XjkMea_j5fyLzH_sfGgFlgJjrNJZERDEqZzIUK82NtAYWb3AS0XF359OJmldXELwnMgD_agcAT0UfqRMMPlTRr7J46fSwabsC1Gf_R6ylPm1fxoLZPp4_8r8f5B8QejBCQCFUTqA2zT_1kY7pPzOqHxzupZpb30HcB937u_vOH2kLW8qeKd1uJckp4zzA2oFsSUoWBjdHXhEoZlohxvqmEmfUKqJd74GqBFcO5pCW79kEo_58Yfr2vngPjMMaO4DnuhKZDr5szsgdZdGjevOi1e4JFGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or2KN04gSBvpZy6au2oqrqbVael5hgNqTd4xZ0SC1_heWg9Xby8UlsPvXm_92TijqaLVc2Sug52SzOZmjUqXGEaHkVE4LwQRH43sLbjR-7Q7tv4uia1OhblI6beqhNFA52In0wk1n8xU1f51CeX7ca-5Orw91XVSMlPryQzF8ObVlU7ZEnX6HiD-8Yg-1Bez0UkUL2El902hITTljZjdm6sZbIpOy3SE5aQepaMscZMiDfyN2Pqgvc7L_EewR1V_POBYn2629IP_sSI0b0CzoYJTja3b1ibJXwU_FuzM0tJ8dMi2iMqyH6LqD7K35nkZ0NVAEqV9ouDIEjamicGkhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLXW-ZA5LyUbcn_G-aD__NBmnmnWNIuQKCvn38rwPCdlHMb8Qw6NcIjiBnijBltUNlhIaJ7bwzPA0al2tauaM-gZh3EIZltko4SZplind34e5qWTAj24qbHanVBzhNeTUG5vs-qMWi1hUvwnaGQlem6SGxh7pZSGUehd5ArrjoLyumtGQnlWoxcpA8p_7xklOeQnnL9U9wrY7Lfqb1yWjzfRknhzzpD8w22AmK32Fq_mNPqV72TEgpzXLPd7QlDz-Re237HWyg3FNbgg99zwD8YDbwaG2bKboX39-uVDoejj3GpV3-EvkErRA3zce-iD8bEi9WZuPSAkRh-x7jyNDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYiIkzhgapdY_8vH_7T_sqpxvi-Ff0kdGsRrXdCkL0Fc3TWpZgdysvGy1yES55Mw0Ltd6h5sHWqBEy_dWHJGhjx9lUx6_RikZGg4Dg8M0ABeA2gjr6qxxIZcLG-0dxL-Zawt_gnMQ6-uY6w5JVz4KbhpFDFbTXfEPKl3l_flgEgNr2h23_UiWzcFAba2L9YTU7-Pgj4fMj_kLMG7gFi71G0CLTlM2k4CAMh7g3os5pspkzrtVyE7lVNwSB_1BanlR9bWNQwfGdEJyTEWRgyzUqM9xh2zqwQKinM4ROfGiSPW4xCI6k8wwu7dQs-7wk7Y3JYSfmWjxjjaHWsU1Ui2Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCvD62XzPdozAyMaeiQnh0Fx9fWGUh9m6dGhHpJVI473aXxFYFDGQrkggyOdWEeCTcgoviBDWZtjWBW-r86vLztD9d7In9PKBdanLivmE4ExamKOtVGBW4qVLvDsNaw2BHK5U9uLiBrG8fSI4RSnrMvlPeyOpD3CGanYPE0e565ru43t5aHYCRF88th0gHopjpJQwufhJMXekMxLgk-RECy6Y845lPqlyCXzPg1CQnaFgTNqmHVKSxTHVScpLb75CJSUSTAmi3QrvAzomzeri3V3Ii93GpNqTMwNRnhS358w-BRQoWLBNHLxcC-ctEy6cHQehwVKtYUOsT0Pabwa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igVZI5yPrn6utQ0iVNraW2kUe-gETHnJrYY4Zzdd79QU8xAwVDkZedu_U0O6ALylvfbsuj8bFyL0FYcSZ3h1KGCTZgkBzisJlYg6jFqY88VMK6nk9VocHfKubO8eYm31f83P-FNQNbWY2wJgWyFGRmODX5jsNh92QEeIi1eRH_wFOC2hCX3_zCJzTxgmnqrn1UgP8RpZJC23n9v7O7zzz7nZcAZTsqsPaCCPVN5eDrliwXBBET9l0CM3xyi3QtdYrVerQ2eSM_Lrennyz4FGVYBnyouUIDh2qQIfDKRTJ-PUJJvS2GApy7Ey36FjyYARPgM4vGhcOWryZ_JDAoHS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkgkKTZBsaSVIZFkbQ5Rh5bwpBEKrtrrzEsE1Sf0KUua7xP3ZfjyL0Wv51mxxdgYNttnEVYN_W1ds0SLWg5IfhRINq5DLnWw7I8-LRM9WXSXaTI_IPIrc_81Rh7ipPBqA_9bHwPrCLOpIO02kLQlflMs8AeMr8crWePlAb7wP3IZd-hRGt8UFqWKMiUrAHwYXw_5salceRX5hy4mUMztTqqRsOkBPNv3GKRsPZbqetg77cZokQ08EeGY4gDoOSdd9qC9d1Jm9HKC7EHjMQ-JQmQL4YwVWYrbkD8KMBKj77r-9xP5nMOGErbVBU9K9SVOXA2JeFA-wMne1sQYkmMJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=U1xYWctcmR80eHd-Hz7FMeDo3irenKusa9vLzCa8vTHDRo-XH38TCU22HOwqxVi1yZ0uNu6bpztbmL8u1xisN_okEbUGw4OJz_QM_JCBOa-z75Tl4FV_eU9UZsvraEU2vcR1plXHTR38fHqC5UkLLwnMZXUahZTjFAhrsLDsNW1e64nceAzfSwfeat72aGYgeqOUKLdSQYuhZYzVNd6mjW0Kh0CqUhV29219dM8_W55SDWI_o71sNZQIdTfwLz01Ou2IJELM5NR7ltizp1AXlB1PvhrX8R-A8HWTKRUVBuisOgWDLd21nEQn581QY38Ccxcf4HCPTAg59LIC-idG8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=U1xYWctcmR80eHd-Hz7FMeDo3irenKusa9vLzCa8vTHDRo-XH38TCU22HOwqxVi1yZ0uNu6bpztbmL8u1xisN_okEbUGw4OJz_QM_JCBOa-z75Tl4FV_eU9UZsvraEU2vcR1plXHTR38fHqC5UkLLwnMZXUahZTjFAhrsLDsNW1e64nceAzfSwfeat72aGYgeqOUKLdSQYuhZYzVNd6mjW0Kh0CqUhV29219dM8_W55SDWI_o71sNZQIdTfwLz01Ou2IJELM5NR7ltizp1AXlB1PvhrX8R-A8HWTKRUVBuisOgWDLd21nEQn581QY38Ccxcf4HCPTAg59LIC-idG8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWXKHgsvhKknlQqYSm4jmltMQQ-GFDNgGUb6cWsvtxSLP6kwa1Uwx2ohkF4g-j7a_rAr22Jpm6yNo3HEnNcNHIfhybo9z8NyabpgR0hsfsEuwwAKyraZFvMZAnDkG-kexl0bRB3z4LjOEJ-sBEWKN5zR8wRqYlxjKieQZZN3DmT_OZjHTojU_fOwClCXHsny-EsUdhfaqWmbTGQRofMW7-vaJizyknFaPdlXMGsSbLlOV_tKRSFynIgCEg289u0fP8hwQQTRktifn6TwwAXEtMl3VqhurAbRjUmYWpIvcUJ6Nci8RCH7n4R54Tt9djvIgvhGoExrNx2Ej6G89GysmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=ZyQdgwhZdKhZxM0qfOogIkn41R8YINfr7beEO6f4Vzdnw2JtfA4l-RqIF9Vv6SqYESQbkGyoiyok1mahqc1VOuhydJ1gWkHZ1rzoTydkInNxLJU8GasbrzkexrS60hK6VdOLZpnaDDjxGaL0WYeGPws7iwEbRGmY5sArZ371MKQ1VefO5Ajd2939Qbtlpm43dCkwFIZ06RA-JJ8g168MObtBlgfobzfnXI7g4HK-tyPakzQz6DbOmbzQnv7MILgvgVUW8ITqR1Tl96JI40aWE1Jj4gaCvjmh-L0uBtsfDZhpAYLSuk2H6gkCQNSlyORhsIVafUh39DDqDS6NoluMSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=ZyQdgwhZdKhZxM0qfOogIkn41R8YINfr7beEO6f4Vzdnw2JtfA4l-RqIF9Vv6SqYESQbkGyoiyok1mahqc1VOuhydJ1gWkHZ1rzoTydkInNxLJU8GasbrzkexrS60hK6VdOLZpnaDDjxGaL0WYeGPws7iwEbRGmY5sArZ371MKQ1VefO5Ajd2939Qbtlpm43dCkwFIZ06RA-JJ8g168MObtBlgfobzfnXI7g4HK-tyPakzQz6DbOmbzQnv7MILgvgVUW8ITqR1Tl96JI40aWE1Jj4gaCvjmh-L0uBtsfDZhpAYLSuk2H6gkCQNSlyORhsIVafUh39DDqDS6NoluMSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=bO3i8WP_tV3DKm1Fbm8Lulwe8lhiqhj7MTfB9q2m-iY4oR-Z-HtoSCAU1r8yiM6DLPtirK0ipZnx6peORz--bo5TOjI8hbB7yv9oUR5euQGinSiJfGBPHBXb0Ld-wGFPtl2HHLoOOAU6qN7seMlzcxweDilU7Jf1lLjmGyT7KC7USk5sNWtxLyAyFOTSQgxG2Tu_Pp0Wx8zELNIRgYZxu7uQCDW6-2HqgSXOkKxBKHSbW5aC3F1cxL1ujaQyaxU7nh17Gsc02LMNZOX69eNy5MGa4St9V7Rk_IUthDBcrNwYAMx_7suXjpuCEhsNbLZv-98_T6JeGJGsWD9OOVpkjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=bO3i8WP_tV3DKm1Fbm8Lulwe8lhiqhj7MTfB9q2m-iY4oR-Z-HtoSCAU1r8yiM6DLPtirK0ipZnx6peORz--bo5TOjI8hbB7yv9oUR5euQGinSiJfGBPHBXb0Ld-wGFPtl2HHLoOOAU6qN7seMlzcxweDilU7Jf1lLjmGyT7KC7USk5sNWtxLyAyFOTSQgxG2Tu_Pp0Wx8zELNIRgYZxu7uQCDW6-2HqgSXOkKxBKHSbW5aC3F1cxL1ujaQyaxU7nh17Gsc02LMNZOX69eNy5MGa4St9V7Rk_IUthDBcrNwYAMx_7suXjpuCEhsNbLZv-98_T6JeGJGsWD9OOVpkjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=c2djkWLdv9hQ00Dyd6nqkktOZiDygSJGSYqXSs9ycrO7UGIdurGL2nr4NrwzJKeYxuHTcOwE3BKdoX4eIrvkFrLzzAZfj-Oq4A6IGLAxOcLc_69ceLUlY0Y-pYeV17MuYjzcofrcqSGtiz0pyXmCktEzx-87r4wGoi2FfepSf2Hig3GJv8fUWtSmqUfDclao8Cs-GBZMoEqyKyEJgfDYDi3CVz7O0i2hQnmiHEpBCN2DfXQ3phmAi2V4ptiHzu_RbKQdq3Zf5b3YmiqU4eqHDvle4Rmhu-8NQEO9sMxKsjhBd_67Cv750M0Q6XcOZsqFxRuqm08-mdPmamS4z3Zt5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=c2djkWLdv9hQ00Dyd6nqkktOZiDygSJGSYqXSs9ycrO7UGIdurGL2nr4NrwzJKeYxuHTcOwE3BKdoX4eIrvkFrLzzAZfj-Oq4A6IGLAxOcLc_69ceLUlY0Y-pYeV17MuYjzcofrcqSGtiz0pyXmCktEzx-87r4wGoi2FfepSf2Hig3GJv8fUWtSmqUfDclao8Cs-GBZMoEqyKyEJgfDYDi3CVz7O0i2hQnmiHEpBCN2DfXQ3phmAi2V4ptiHzu_RbKQdq3Zf5b3YmiqU4eqHDvle4Rmhu-8NQEO9sMxKsjhBd_67Cv750M0Q6XcOZsqFxRuqm08-mdPmamS4z3Zt5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-UWIw6m4aZnRxfBtjV21f4ry7FZsEXstRA92MxcjDSG7eHLqaGU4oSAm2gShl1Nf6SAjTEOUGS2VkMXydoFWdFSzJIrIrFhIyefm6v5u2fyvaD77xsL4tHvCe8EYyZOOC7CWpuuGJB9wPHVGTKacs6F5fJ9_xTq9W41BYy9Vv3gAEh5RRn5bp1eyQDVS4nGmxeuIS_9fFuptmkriUmvU074iMlfhnZQNTHhMMSlVSjWnAi34wKmWYWZZmznCwIaLgTj2lRTBYNZKQ1J4oV75w8ISnFXP5ov2d9ASHBKc0NK8IRiWYPPIZZRu-mWU7XWwdBJsNbcBX3Z97bwnlGehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MdazxZnsSZpQJIfZHyVHc1DYc7wUhoaMQuEjVWKJ759FY_5_S8SM6BIMEavTQOpLNP5HwxlPjezQg_0pVjXUH2LdWjalakXo-T88wRySlHsb8WssrZ9jfuHw6RCjEnwzDUPprRPGnPHfOwE2m-CP_E3wLtLn1Mbp1wdBeGhAs92MvTlgHiuRue8Vby4DzWnRDOnsxXXzSqZ-p0Onhun2Qc6DhkzfI4t-BTX0xsYJ8HrJU07hb38gWLbNwRJaWiyTIfSHiYe2H40DMLXLe14oIRYBV7X_755hdwJZMMoif1nFfzTwpTcgcivOjHTNvcqaqsSQTC8nvmGACrFbkx2ctw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
