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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 00:32:11</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg5kACutvpkyY3sNxAE17vhfygDp0_U4Gpk17VX9ydYMbkReSlIEumOIdAGajs6NqkqrhyuNrJgqu8q30stWVyv0-v5r7Fdi1oQEqELbiun0h8U7pM01qXsf6PLqlHJ8zr8EI5rsPGJ54MytzEIEIT9Wmiu47yWv_vaFBMjjQnyjgD2nRFkyAKCk3uYgUThUSIqB3KNIpme_38c4rdFfFuZhqW9H8j_fYDTFw_rqfBHh83qd3GgRY0q2JPhElvPd-dEhv3opYyt9B8zAPt5p6m1GQsKq_b2tAyMJ2QpMVP0EKrdhcJzdL59v5EqqwDQW9gRfUjx_Iwi75591lhfJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzb0Pcl03Qh68m_aeP1jNKBdkDOSbZVwxuVfUTcFLuW1Y2XQCZr_HXYGeI4RvVVYozacCN2V5e72k0u9JRDGrd9cJGGZGC4yd-h4dBQCzcfOO5X_AYndSJ8E44SBJHRqLBP3bjKhZlEWWQl6sy9hQXUN9BKpwIra3YbvY47DfTfXZDaOZVM6ftYvsLoIAtCa-HOiEPbtCIP3LU1ywhTi11n5H5H8Hk239YVOiCnqadimOun3ZsDwxQYfMBgZHRh5X6a4-L80K8dEwcjQxlHCKdP6XzozW-3zUyu3o6xHI6egGeGQRaU5TOvCJVtsoltvPt2aK5Z680eRH_ZjOWul8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvvQfVZsV0WNMI1ku1VTntZsSe5KRrScVqpMCMsq2pV1j5Qlm2LNHYsoNGoeCPQCtoH-Ee3q-R4w8OWjmLLGONU-D1LCrk4NB2qlecJH7d9bDfBclXxQTithjezAGW71FG9aqssk3x_7KnyUXX6Otosmlhf-l73ZB6Wmo7bgOPQ3BneiQCuejkk2f2LSzQye77nsyc19V7_AGGih1FIfJqypFrGdn1hIAGiHzJ1M1037fq0nqQvhA5Z4nuj0fXzvdQFuYvWW6U3b_27LXAGyySoQ9gMZqKRWLbjf4nrc-rLy5fG3iMaKDlPAQeb1gaQWOQrHegq-KfuWBmZdE8QUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=tAvSu56HR_0a8Pn0pEbRWAs01Gejp8Vq7Nh_QQXcTXEjnHN8gwplItSdXBp4cN3XDH5uyQfoggJhKAwlZWJ-6r8oD_9qI823Q_y69SD9RszO8JcloED2XwsTdr-ZKLJVnP0gnem5yRvrZiJvTyj84IJ5KjJIg4oRAkjY1sM7yAAbXxS7RODjBK0k2c7YXl2nlK_toZRSpz-h3KuGgP0Z-NiEVVk_5EVjigpnwmhC1MY13cOVb4cDziu-TBrzjdQ0np00kGjvj9SyPCReUxnmjI-4xPdtUzW_HRw1fkDladuYZ5Tmh2ZUuw1_DT5O7z2Ub6eXfr2JwsD4LvBRdqeo7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=tAvSu56HR_0a8Pn0pEbRWAs01Gejp8Vq7Nh_QQXcTXEjnHN8gwplItSdXBp4cN3XDH5uyQfoggJhKAwlZWJ-6r8oD_9qI823Q_y69SD9RszO8JcloED2XwsTdr-ZKLJVnP0gnem5yRvrZiJvTyj84IJ5KjJIg4oRAkjY1sM7yAAbXxS7RODjBK0k2c7YXl2nlK_toZRSpz-h3KuGgP0Z-NiEVVk_5EVjigpnwmhC1MY13cOVb4cDziu-TBrzjdQ0np00kGjvj9SyPCReUxnmjI-4xPdtUzW_HRw1fkDladuYZ5Tmh2ZUuw1_DT5O7z2Ub6eXfr2JwsD4LvBRdqeo7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9N0IInBxHchava30mC8FOVBii_tlYjG8SpyCnd3_Lrhb8Lcw4yW1TrRUGhTjmpTCz3OORTK4tT-Bh9jtCbYux6H7MvuvXIonGoHk09EVWmPe4wo1uDQ76E7RrlfcEaI1gSkXm8yXG9BcFmuqzgb0WwEu1ZNqgUh8KAlFRNwuyaF9gczVJ_sPHUn6a59v9f-hWIRhUrO-JLAc4M2IKklOrETvjjNqDF3iZG3BRX4N2jJymEPhXoSb46XHtipbT2tQ-RZodXoexytmY1IlpV3dQrV41Y4AbDX5fe5oE1Xcy0ENW_QSIWPw8IP8UBydNmVwxdVT3Y7Xmz3XJOxVKqNSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTGmoGYhcPl0eSnIR0EtKTjf02ngcd0FqWomLKSg6ww5Srb9zjImNymO_qFYmnA8h5wQHQhvlbCMwUIQbHT8_SQl2riJGHhen_vb9zZEM1-skcV-Sugs5Zba7sicXSzCBf4ZuZfHoL9wbA-vG9QLEZUvL5PcHRSQ_sc3iLAMyLPB966CY4wt06NMczT_D1WvdZnR7AUqZK-loU4ly2_jFeUylqiAu8ocCsxlhWapQZKK6CtSQehk0KfTtOqaHRcl1O0h8-pWGcCM39tHjkFpXaIk-rbWlLNaZtCMLRPNl2al9eS8pqEf27s5tTS4HxXgHKq2BvzZtHX_Pw5rHGngrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBch9mhCar0MzRecFRwpImUY21K53IpIzRpEBktH9jJsx_K15G3YU_jIgnWacn3MOX8VtvpSqOfzNaCDslxzqfp7tcWfdbvLChf-0sHJCuCsK27XFyCcigGJBrQkyq4HzZGcoAGw3n7re0XdbKqFIaxy7vEek1802FLxhsda1ftREdLSARtxPyxPBNOfIxGpo3bL5otRBQIxP9975q1uIdLw0kAQERhtitCnBtu68OrAc2EVwEXSaVL3d9kK3l8ZBopTpNhFbQ2XRY1z1OjxyfrXSVyjgQrhAjDBzJTNdOhWsOSw_WnRDT6yQANmrvt4bZEIStSQXdj7eyJwlkEtlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeiuuQ2Z4K1DWGkHoKw21r3JILzLCnIlxDpvdX035BnvDTF9lf39QZfxXmdswmCxHaOPMtIE491i5S8NoPdsa9-XO0_R1LS2rnhtTbFSZNp2qDuW7__6LUXV9BTCu3vurt9ktgyWL_DSBerCKWAymtoUAWfTwH5qwfBSJF6f-r8hqhF8ZBx7Vmq6-ulhEhPpfv98rR-J9kBgwNRaF1uw6yfmyPsacsIyS2GLdpbadI2sWUl4oG4UHJAH_17p2sYK1gT0IBd_vLYm39n0djcmRqhKGNQkfP2xC0lNNHHzFeP0eCsb_YGXN2gOaVbSpLPUPsvtKznMTjR-jcRTDJgUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLC1X9k6oxA8TQ5RcHZHpxyCCZAHAvs4BzRHrtaqnNO1HPqbGGwyz5jOZgKt1ILLYMnrHBHwc_wbSyMUsk0hNu6N4rJyy0joVfd_Ite-F9DKTpgsBfo1Fp4oKqrz6qkIbwMfci-JCuikA8qIM_A-b9d0_l6LW4NVEOmuBAfyDrxuYy_Nc34rxOMr-1u0q-sQ7XFPHKUrKCksXO9MZ9CsXOUcyWIrF4n4ISrc5_rWcqoyYzdUhAOHgf3tLjpIQe8SkQL3X4toMV0RiuSNjf7rcjuroz5sbWqWaNIjV4kPlOjJXGioZiUUaaMv82WAVtpAcr9kMy4L_epWVKFdBIXJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpB2x5x-90aPjM3DPPhMj_Fq0_xu2gxKQC52t6fGHcyrxJx88j6g9lGJVv3wemVqpAKMNo2cCXSQHrrazNw0sCpZrtDX7xA0udaSQAIg8nb1EffH0JsJYj1TocqyTUaD2IJOcxHqi8gn1xD6fyNL3zpkaX3QvJre8Lq2SxrumwwWuk5qg_cHHlbzgxvA-FUNnjpD2bV6XcUgTYqcSkU5UfGqgu9fHrUA4wSvnZEUte8CJQRiB2ul_J2-fP4Cc6hIU0PAFgJyynsWomVUjIxUyKlRS0WhjZhK1Dovv2V-sgFU28GikpycUPND2oHRsvfBw-BtRa1NFNarfBvNELvhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=PX7ezgKCzw8czYDU21kZojr3CRzO0DrSvRkTdlGcSjrq-GOgMXux3uULqLCpYKZYUv5rIhraGFJD0PoZqLZBXViBmNN2H6AwyHJRso24Ec7ZSCsHQbEfff9mAjUPgoWXmQe6cOzlZZVG7Z1Rz_wazzKqwV_Q2QAs1h02qy-3JhYs187qVqpgyAZxrZUfjnuG8fWJTZNXvl3EVNBSNEGsxW_ldQLRhM1vX_8aJWhYOXs0XR0T-HOH2cGi5r1TXlUEpeuTOIOpriotCF4Em6RGjeAbaWDkvZ46ZoFUiW8qlyMgLMilDkPcblz7ZDbtHsU1DSK9HZT6yEb7G7MxSB-zsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=PX7ezgKCzw8czYDU21kZojr3CRzO0DrSvRkTdlGcSjrq-GOgMXux3uULqLCpYKZYUv5rIhraGFJD0PoZqLZBXViBmNN2H6AwyHJRso24Ec7ZSCsHQbEfff9mAjUPgoWXmQe6cOzlZZVG7Z1Rz_wazzKqwV_Q2QAs1h02qy-3JhYs187qVqpgyAZxrZUfjnuG8fWJTZNXvl3EVNBSNEGsxW_ldQLRhM1vX_8aJWhYOXs0XR0T-HOH2cGi5r1TXlUEpeuTOIOpriotCF4Em6RGjeAbaWDkvZ46ZoFUiW8qlyMgLMilDkPcblz7ZDbtHsU1DSK9HZT6yEb7G7MxSB-zsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fe5Yl0aksZAk_GHuf-2YYL-6JEK8_IDNXgNWcszZD3e9-sCsvws3a-Nyq37gektUWeGFir-WZf7jhxGAJiVypng3CgSdkhYMTQL4aQcgnu_-zt3NJB3DHlBlWNatX1mPD2uUvrSSjMDOpueMv8g894XqWPUDNlTjMNwcsCVTbmXf_sZtA2_8ic15hanwhS3TWxa8F1UMgIebeC_xRSWHKUdAYx1mY9ohpdNNj7XeM0t4PE3ST2fI3h1NDc063dRG4VHG9kho-YXgtM6E9y1eKB1_oGTU_Sv4HNB8GoDKHp4JficNtQ7mmaRYW0kHYPytLIq1U0ONH-5NifI6DNUruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSkUAZdoGYcFjrpVZqgkIp-XwuOSHaM0rhpW1PtR6PHaThzIGffp7d5sAxxm32emrzqp9N38Xbjw2C9_sZTQeomqJQz1O5YxNxD3yKWBvSmqHBAy5YXicsKrAxT5agsm0FpBNrtFMtxYf6TEi4v7c9ioUasyM4aFtVosUq5bUewJGoj2AZEwl8fXcWbJiV-nCG-RHrhM4z8_pEW0_HS7r0a3bwLnRtBcIOKSAreGCRa6PpuccOxBkJ2fHPlsAW6LlaHB4SsgDI9zip8NGN3ua1QlwCWbsvipEdCUuwvd1dAOTyGw4EOk9fpDaA9Eh83Qi9DI60yvWyvrwBpuKUN3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iem9RPdmLzgze5lFyLfJe0cgu5PmCFR2hKNuBNkMZsMZYmwK4E9KtVeGPSaPMDux1HKtZd-0gQW4uhATkIwMZwu53nBQe2-FaErJpFI47WIDZvizB9MLX_m5lQ-RZKljsl51EYIqON0t96lTK7w2OPFmdKtMSiuZgpMwkWCaeyha5j0Xy8M8UDi76Jf2dudHWf_deZU7rb5_qTZjIm1AF-GLdGCC19ERaCnAHGPAzZc1kqfxekLv-9aMkFrV_j-GRHUM5-qOHOduYTENbnGOHBdaWEEMJ-oP2gL5peyUiw6bBC-PpVI3498yevt4tiSxlMAd1ZeLG1xjM3Glq8Bxxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1oiWFbURf9hy8FhBK7xXtXtYUr_Izv8FMkGSeDA-o-XIfhKi96WEfvFabTB4nepe70w140zlu8mPrIvf8peobP-xf94mmreazL4Ff7y9QLUli2za673NCHHOY6xWVvE9ihXkDfRuiZyzNWzwRu1KVWtUt8LZ620jIc2cGVkZIggxJ-Anxr5FsdhBNrLbqN8NUr5DiPLhV4uiVh_UBubVY4o_VWwY7kiDo8zpXGAP3L6SDfI0ACujngRcJCJEwtPcgwf2lKu0adRWmzyxMZbHm2WUp6WUNrop4tX2qa1bYWV4qiYQ5IFvBFNU3qRwqnwAOsOSddAmHoS91QB_QUKXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=ucMHDkJJwhKVAeQ97GNrk-G4BqG5DG_kG-JWvY_YfPHeY1SOSEADH2ahNBCz2QVTUbph12VGyQTgn0RI358BxlgaNcd5ImpLnaOsTS7tCfO9KFgCTYXao_GUPfXo9Y8SWDnAaj0oHS8HoYAzq3zOEGkj_vvigrI9l273ImtxHszUp8sEKFgvsokrfOhkd9iPFvISXYz137QVEZEuuCEpsB3XKgU-wTy3b2TaRzRtCbAQaLiawQT7bnDa4XoL8uRsLhi6FrkgKv-BzOKd_wMB01uBNzSG73Tjg46hQmtabZuG7ay7sWM0IJg_x9ZN8FpQ-vrMLqgV1_EddSgbiLLEUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=ucMHDkJJwhKVAeQ97GNrk-G4BqG5DG_kG-JWvY_YfPHeY1SOSEADH2ahNBCz2QVTUbph12VGyQTgn0RI358BxlgaNcd5ImpLnaOsTS7tCfO9KFgCTYXao_GUPfXo9Y8SWDnAaj0oHS8HoYAzq3zOEGkj_vvigrI9l273ImtxHszUp8sEKFgvsokrfOhkd9iPFvISXYz137QVEZEuuCEpsB3XKgU-wTy3b2TaRzRtCbAQaLiawQT7bnDa4XoL8uRsLhi6FrkgKv-BzOKd_wMB01uBNzSG73Tjg46hQmtabZuG7ay7sWM0IJg_x9ZN8FpQ-vrMLqgV1_EddSgbiLLEUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZiJ70dzQWci22S44EldyeKUUQiYeTYFGebM91DApHHwx9Fwm1ZMFTSLjWA2CsPuleaTw2dUnnA2-DRzoMWiB58kCG87-4Bp7D8tyL3fWTMm55RrFxZMljczQErlpBcR8YKSfoEezEVZtFHFcGu4jP_7JDjIoAw_r64jKNLWrXGdfsNQLgIEB6Up2C5yLG2vL7i2tXSQKFnZi62XbffVpMKCI2NCYwXxm565Q9fw3GLJO2MVV1ba5J_MuwhggdEJjeEkmGtfzPvOh_KdSK7sI4DNQsars8S1T6u27jn72x2YX14Lm0pAgmELaQeyjyIapgPRIBIZKYzxqkWKZw-Nag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RscxM6g9it7le3WlvLPMdeb3GMIcxDgR3In4ZI2PkkRhKXSQ3e8sZxO-nVTT70pz5BBaW-BR_bHJ-r9NEOG9Bq01GkstzNqOmDcbDsV7lk3lk_6WDzxbHdPZleTMs83Gflx4y-q2jv_23qI9XvsuxNAQxzeGKdCxqzn0e3Datk0gStsQXzBdK76t6oSkljeP1Mjstfx4no9ySnPF6I74DipigRjcxBlcvaTKO38CGF8WkrrK1X-2Ax-Naw9RN43mX9Mzn0qp0Lm2LYytT_Vy5m3JqX5ZNzk8YbFthKMIq-RZAusha6yL-SgW07940jO10w5oF-EOotK3TUsnhQKaNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAN8XkHJDpj3VAzB_-QWMp43mLtP-OW_kjY9p6TY_kZXuH9yWlSxyZV16nbYwHUDUfz0RviruR09UPcgYOXW-I0KoYb6WbFx5I6Vkpfs8PpgakugSa6uNTAzzXV4znEFvOMq6HxwmTTvq_Mhbiq7SkiH5aPAs_3CbhxDxshw-IIkzQ2RtakEolDhAjT3M4OftBtuMj-gk0tzSB_2aBI5MdcXPKtsX2rDm_70Gjex35_nUhBu73Z0D6jy4BegdxyAFJ_XoFOPedAwjTHaX3Znf9Yt4RsL_nwlBp2eCvAMO0eZvUhA390P0h-CBAKLNDYDwnRs-a2-UsqiMlUVXz2PHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qi1ILmURXZ6wUWObkcIR1UzHuwwa5f74iwyGz79OAIEo0zSpGwHrGiaIlVZCFaQiZG8bEu0L92h6SWJzmsURP4sMGmVh_eyYOUGBIJvcBWX1ESd-4l0AYZhjgRE5ts-4yK8NbanEVcRK9-wvah1kx9nVj17HByosN50w4M2NBXnNGtAM1RBkoQsV6hs1PxZsVd0cCHcS-MTOpS1XzreMmnOr3DXuNiBUSeTZ2-mUI0k7eTot4j5RU31GkjDqh4PIwbs2JBYbUeuAqPCCVREWznxaaudae1f8R5hR73bun1YatrtTKg6mC4zuC_ryTL9wgKjUQZHPGoduqiqFRQeeZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPsOgyeDCXw4nN4KzjBdvATSYDU6W9K99GpeKL78Bg-dUweGyY-bATQR-Din5VHdHLn_jkBsTYJnJoKza3TvTBucN8SdudjCUolBNTYwJ1-AxoM1XGHa22Y0ZjAKHTPOHqqBXj37VBlCQE-pAVZyJ3XKOPOjN2_nE2JwfgXKTopXDVeiUQx6jtjUkuqX1TkkUtunyBiUY8g9z9xb9s4Z5otJ2_MHbCY3Pa_D3Xk3Kcb3psNtKWJYPBXoLp9pwKJAO7BmAngTEi85zv5LsJZAhj2gM6BJJdQLtTYGXm2dc-fJT5H7ACfiFlKIg_T6uKe1vxhH99B8uqxlQFSn9N7-Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2RBCqQXTu7QcifJIza2sKJIYeWCISVH2UeHrSDa2WTju4FFjsHJxcljhjcu1blqbUmIL7q9ac0-5lRXyFW9aIWMUwSkKWxW8BY8CJXD3hOgF5GcTnMKdZXJAtm0kOnsJERZtx6VU39XqjJzDKeawh0FIxGu0k3XC2NQp9o6luJUemGS3jDUfz9qxWR7QIwl6vARVBCJOsIISOJeZzgQJd_fkquZkGn97pLh8n5P-cUCYaw4lFJMWNRLJ3a36Db4n2Q6UPw72BZtbydqmv5rvb8oDyU4Fgu_HaPqa-Yv7c0P09JeYEwBnMgzgMWQr5-G6pusAAqFBtBHPB0bP6GxQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fULkkZ1QzYO2Ro6RodYcySo3oMnWu-YYWBBaKUWe6_vPicEgptehJ8_N_OaQQ9_m6aFZfZwXwwQJeEDqMHDtT-Wr7NZjEig5PyTQrVxL5rMCQ9CG7nl15MSWHqbtEY2YT-25NslboXCC3FqbyNwGtAQQctaLD10MY162i407yc6dhrQyABsT7f35pN97LO3qic8TEJv1UR6aUxPTrycLvebMCrzhMaGMR3rm25EBKhING0kIlLpdZatuk6ON_yXtY1xfMC6NNLIh6aay5H9l7DBcE3yWNHTWHP_oIk_uRj4qK0-vJRd1-RKseH1kyn6xMg_uNzkZMiPCAu9lP_phtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqaLOCafSxg_eHInyK_U4GuoAo78cQJNUZVLSi5Oywd6w7YtWViyNQSb8kTfLfmd3MiooXDN2zbPPrPScxVOvLQ0wqO_-_kFu6sjJzUYCvBCQCn7fpljKF8_6T-8UHJlw75xnqpOnYz0EFK0QgQ7t-kjOE2OnPiccxIZEX0MJf1B6_cMHrvR663ynxRIpUnHjU6TF-c8SZgjmFad2Wa_spAr6FJL20spOabG_RPMakcFfBAj_kg6m_pCVSq3kxs88KsHl0LGe8E1FcbnUUytO4dUmjK4Je0c7qfhEHgrsKUeST-kWHxObt3AKti7szQ9vccWHiJqgdA6zZlMoZhV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWvo0DWXsdzCEhMXLkj4ffLjjITFqsnoTALJi1jY6wFwvjou4WtBPYiUZp_qaKKsY1KRFez3n64tnX0TXunzQe83rwOa2iD5vBc9_-GLbC25VrKGq43S3fItWmEmagaOTgzb609s0F7V3ayrf_M6-es1fC2zrYh2dJLuhx89E6fF3IPb45N_ojKu-p5cClMQYzCT4-PhMk6vlgX-VEIztVhHXlSuLVxa3LyWh9CQG3OE85F4-6lBITzs5NCiIU3laCqrxsOuAg6MsKGb2V-gKxgbMRnEZ-KUD8DHz3khoFpPUQmiZK4XeDxQWCoQlkOAf9nYRTUdu1BZZxtYptpHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHiOkf8EEa0NSNNfBlarJ0YUEX2gB9kYag_q6a5eBikSjVyb4sFyvUrUUbgYlopAs30zS0lTmx18wcr2wtuCPo7zhP6Bqa-s47Y94eJsr8eufa1xruUeLrcloRpIWKPrap68QX-hqNWbk_440EmTDzw0rMx-_MjsFpNIsDDXQMh0tWU5bBPLI5lUXi_TmJ4pcFqZjtbQS5FLobhKfeRQXY-huXsWcsJxocR9CGVEyPkGz50s9-mFTordsXx_PCLyZqDgSLZOlG991eNgVJ-JiXxNoqQM6Pc8Pmlgg3s4R9ebSmM2HHv1ruSlcPBnY_zgHkGUrI9Dx7rkO5KFb3Ayew.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=MYEsFbCWGDh7lnry2TEUNlhysh3I1SXA4rt789k--GX7iCIQvfGyKScBLf6rnsvWxZTBQ1eAN5s9Cgi6xip-c0stjsgWfOcRcId2HJu72DMgE6U9aboabKnJQ8P_-8Jr9ghiLdgpjmEtNMZ1PMmq-cn_wsUQe3HV6gAOoMMnqksXJr_wP4mvnTtCyflFHkIDVZeM7Ker05nCahjFz5htcYHCxcgk7eKmlWJjtCfWl1pdenC9-ZjvfTvL3P59bcTCAfW80XyuiMsKSHE6u3Lg-EnJId8nmwbPy4MgztPXhL2DPu2sZgqG4DA6kqpQHky1uOCqT9h4EKVHmcwO2jGAuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=MYEsFbCWGDh7lnry2TEUNlhysh3I1SXA4rt789k--GX7iCIQvfGyKScBLf6rnsvWxZTBQ1eAN5s9Cgi6xip-c0stjsgWfOcRcId2HJu72DMgE6U9aboabKnJQ8P_-8Jr9ghiLdgpjmEtNMZ1PMmq-cn_wsUQe3HV6gAOoMMnqksXJr_wP4mvnTtCyflFHkIDVZeM7Ker05nCahjFz5htcYHCxcgk7eKmlWJjtCfWl1pdenC9-ZjvfTvL3P59bcTCAfW80XyuiMsKSHE6u3Lg-EnJId8nmwbPy4MgztPXhL2DPu2sZgqG4DA6kqpQHky1uOCqT9h4EKVHmcwO2jGAuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaW--Wd8nwN43b7Sq25M8_fkfaIcwUgI3wI2S53DhniQvGu65PPPZoQdedK8EtWy_4cAVq9ZIptra9x-jeT8khkyjTe8BKKi-Iw53hzr4y4tbZpe62R-XwzSPHx8R5zI20mIDD4YWSvYg0ovdr_UKQjR9tg5xOcAh1F_2qcG5zF3dfjNZ9tNRZIloMPO13qEkgHMID_N-HreuqE9WKLAKc1BJNbfNhwnAuTkphcZGQ1wLsK97r6FeLZw-uCrT5Jgkb8_VZBYyvDErF6lDiGYkLQmTf2pJ1CPMkRBOKJvmHI5176c4fZG4Z7c_krFuw0xa5h10jl4s63VUmTgMiChpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VY4C4qXhQ8GW_yMomNAOAQu5b-fK_4MabUEslwqf9swlWss8QjcsAe5NMuxH3U3ESmRYbU31kl0t-APSk8vBZ-2KdqUQCZpprca0EzIfFoVYIFUrZW5tsUqpf06chng7herjAvjC1N9sPtQcxoruXwhUaTjzOefCCwht3YqVfdzhCZeDjmd1M84qKDzrcCQ_0qMl-Vrng4uiTr0kmDpG9zTaiHqWwXlNMy1zkgfKCO8NuvjJonVNt3GDkirxPBzVo5yXS9fyHuKDfjSdPCbaaWEVhmeApfM2mExxSDmy_LO9XElYPVNa9R5sGEqVd8yAvVzPsb4rpGTT8FLGS3mOEw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=Ey0CXBapRARlZIbDqlNKYU2hdZttlIh3Inc_9Sz380_3azTkvc3PaGr8O3txZLh5Dwkp1x6NbfVou3zJfp4f-xPpqj7J0O_ZGAUZcrO09blWajYW6t6qpP1D5pYQUll5fhrYjDgjGQLDdF_DT53z85-yhoYWSk_V2lTyox3s3UZH1Oxg9XeOLqPFWYn1_8BzezB_LKc6dKvYJytpmuNJRHdaDc4rrKWEsdYSnpsTeKgSGaAPFqMycwqZcyDykZvcwjv3_bQKM1GuAMyeIOqLGt_NqH2tVwWGppleT7oBq08slF66YhojH509AtA8d8lJjD0vYsl0R3NctiqC_NMejA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=Ey0CXBapRARlZIbDqlNKYU2hdZttlIh3Inc_9Sz380_3azTkvc3PaGr8O3txZLh5Dwkp1x6NbfVou3zJfp4f-xPpqj7J0O_ZGAUZcrO09blWajYW6t6qpP1D5pYQUll5fhrYjDgjGQLDdF_DT53z85-yhoYWSk_V2lTyox3s3UZH1Oxg9XeOLqPFWYn1_8BzezB_LKc6dKvYJytpmuNJRHdaDc4rrKWEsdYSnpsTeKgSGaAPFqMycwqZcyDykZvcwjv3_bQKM1GuAMyeIOqLGt_NqH2tVwWGppleT7oBq08slF66YhojH509AtA8d8lJjD0vYsl0R3NctiqC_NMejA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWZvudN52nVjJFv9HzbcrU2lxMLHOUGUOBWRvCD0GpU-K-ORJeDsPNSLWwJWddXf-Ag3RAzhW7t4cIPSpk3CiiSZIt35MzGS4NLBG0B1hzcNOWePns8bPWSaiqxzx-IYPyC4wDLHbiY5qjicTs0PDQsAIDl9T9v3snIa1iOq3Kpro6LQyf0OuGJWKE95ljTva9AW75VVMp1AS1G3cYt320CVoJsntlCSnCMhBwlB8t3UBLVx6xQdQDhTaHyxnPtxe7r4tTiIpzF3HlHdm_j67ayAf1XSK08KuVxDbP3WDm34wSV8BnMtxIWnsdWjvTIUlCsp8jgqBBXK1fiy4JfBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e50Ehk5qte2dY4uyqD8A0WU2kkj2aAhY4hZ2BBrWAtLPtH2tObsRiFK1iP0-4YXVqtTGDthMllthlvXOzh_ZgBTkiuFR8gV3gqKt0_FSdYCRWpHyQuSi1H3s2zR9PB8xKyvfTa_0KcIZA_w3nmIyPFw4LTm7SS-JnapP1RhdlgGj3Gmfp9Nt2aeADyCK8Hoh-n3d99fvo-HKfsAACkUQBkg4FuGjqZx9DkkfrOt9BelqbJRXPvk0GwPLGEFOPvNQQEubpwX7gWgXQBAztRpkqQKYvUfDStNpwPDuUeWmWcl6r7t1AwmDgsBpk3ZWkTthxcBEEU750sOKYuzE4r4scw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=cXtUFgF1HIokxQeYu2CYSU2E4IX43PdzkV5q9K6NzyCvYmBNUl78Q62t5dtfb0TlFzPAcEg4m5vxSc8Bz66xBbYurt5_ksRuoVT2tlJ3hKCxAvSc3Q4qAKtsSytRZkkjjZX8uxEsdODl7pa-XrF2hzJRktfzlefqeZhWi2sZ1W8EqzvPpW1RQycgpj6--u2Pg0WPrncXMTu6UxGtutV5HvnaAORgf8dN0UT3eYOZ6RD82s_3XMwSu3M9518pUBlbTk_RW0DVdBouhvxdW8GLuq50rV5p3QeZwKftn-8Ip5t9FjJBISnmM9Hkx3Om3iN3pSq7NM2bvyi2KgiBjBS5bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=cXtUFgF1HIokxQeYu2CYSU2E4IX43PdzkV5q9K6NzyCvYmBNUl78Q62t5dtfb0TlFzPAcEg4m5vxSc8Bz66xBbYurt5_ksRuoVT2tlJ3hKCxAvSc3Q4qAKtsSytRZkkjjZX8uxEsdODl7pa-XrF2hzJRktfzlefqeZhWi2sZ1W8EqzvPpW1RQycgpj6--u2Pg0WPrncXMTu6UxGtutV5HvnaAORgf8dN0UT3eYOZ6RD82s_3XMwSu3M9518pUBlbTk_RW0DVdBouhvxdW8GLuq50rV5p3QeZwKftn-8Ip5t9FjJBISnmM9Hkx3Om3iN3pSq7NM2bvyi2KgiBjBS5bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGPMpnAhxvIgpdQPxL_oYCEeE0bp0QmC7zNB-cTeclxHRULORSF9xBxMXLvHroye-w9SGddB7sHj5gvbmP5J33h6LVu-k45CiAvBzMv5xfkC1AUAnOSRnM9IkmF4no7Dz97d1IANT_2JSe-x3JAn2ifBnAAMO-fno77MRmOhzxy2f3KqT1S-V2GFTDwrv3BxRlzdVD9E0Uoxi59HNChUtx73HSvVCHaHcFCLApKBv9blHMgtIGkYpwZL3TQTQbHsLg5ZolJGVnVxvQ8Y8r-mW52sDQ3BDaGx54OiMWkVLHk6OntUK5c1eST_6aemtGyEefA1o2VUAn3NgzKcW_rx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJ9i_KALuqDtdNozF-mWWUrhi8o3lbEWnBRqvheFYam41s9w2SCTR_rqloPSkoV6Yqi8h5QwT_30VoNnfIg986yCn4TffprrAODI0tsYbRFzjWNsjN_6oWxEIsolv_Le3CYSa9XBv4EG-e5Crck9aPgFJeuUH6qv5D7zR0oTtWb7g5-yTx7uQGhTVw5InbGPFz71i-UEnURJPjSUfOOA_nv5HVuklPgQj28XIsvgAYPW68M0HBWuTrO_uZYZe0VWlRceVObV_Euzz-fX9vdsIVmnJ00K8a1s7k4DdIX6hz3CqEfhP1cMzEsr8Dz2zQ-NSGOSsMBdrgfPHIf6OEPnqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=kJwKf9jw3Obe1bbJ9ZLfNspOJiDbtMtdrOhL2HYj3_2eOqlkKJqyR5aoOYumfvri_hFVqxffJj2btxZ2UaBa8HuCvvmq42mKGVTs-PI0-4-dUQHe5pCmVS-Y7lDlYQKNKxaK1WSAyifFRnUow4KPM2GupxAhR-NT_3UqWpfdX-OJ1NQM1rSIK8V19IdCcgD-3WtVPd4iNOl7SafKXniozowyehKlRArDcV7_wn3ZOMxpAmyNFbzuFlRpMFA1O95vOjn8u6LJuPeErN0Zhqo-lVP1-eQgoNqX7lJOh6bfKrHLWpsWsYAP-mmPxCPVMFitrdvvWFkHGPiCtUY96Y1M_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=kJwKf9jw3Obe1bbJ9ZLfNspOJiDbtMtdrOhL2HYj3_2eOqlkKJqyR5aoOYumfvri_hFVqxffJj2btxZ2UaBa8HuCvvmq42mKGVTs-PI0-4-dUQHe5pCmVS-Y7lDlYQKNKxaK1WSAyifFRnUow4KPM2GupxAhR-NT_3UqWpfdX-OJ1NQM1rSIK8V19IdCcgD-3WtVPd4iNOl7SafKXniozowyehKlRArDcV7_wn3ZOMxpAmyNFbzuFlRpMFA1O95vOjn8u6LJuPeErN0Zhqo-lVP1-eQgoNqX7lJOh6bfKrHLWpsWsYAP-mmPxCPVMFitrdvvWFkHGPiCtUY96Y1M_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJN-lp_ll8q0CijkF1bKUxo6KUxzwfsit8nQYGsI18PrtvhGTxwZA09GbqYgvNDSiJuOsYQbtfM5IygDDMTuKZaO0tRUJcLtI4CLd57QgZccSABgohqVOM_aD4FWMDMFupkqCa073VQltmDwh6DaoSdB0SZwzpL-EAB2qz_w2W4qMMVhECMDTxYBgENRdvCYxOhMhyvP-ZGKctMUFEJUweu1klyguLNI1sNL2aU4bB-hXmbip5qEMLubB6EDUFKvw06L85MrK-CwELtUIeRMIDI-TaM5KzokG5VTKpyjScgpKNlnAqlft1XPDf6TOkaE1nldMeIIJ7GGR9GZavHy1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3Z9dcwYC9ozPannULIXh3Wnnb_PP1e_h3YzT-PAfzr0WS4NbuqD2uLPhB6cCpObhrkmxxSGT6Ie4wVu0wmRaLBE4o6fZJZfUc9bwy3qqxQLPGMZXz8ItMrGe7OagXnWsVLQY4VjIQiuZKuvLKq3Nje-NyVtSfehoAPgO5KDAaxAiN4dGfQ33XuEnUrNmwVFxw17stXGGt5oRpFLGPV1vxh3Vw06CdaquqgxpPRat3QG8l1WoSGYIjcySWhN5eEZ7tX90xucFsm5vfr0YKkruqUrHYn_s2VpSrjpfar04xtvjaNwub8DltD1UQm7NZqd_bws1QnFHAbAJt3skpTwtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCAaN0ARfIF-JKcqLRdgMJOoDjErd6F7BC2ILOMjr2wLFUN-lovPkx2NacqPTKWWh-20_6pchitV2fRS88HMU6t05L3DlwGrxjv4NGQFUQG58NW_Vl-ou3aqr7MImaqR99dehkY689tlTFmq0WhPaz9QMS-2HvYytCoEycJAxvYgzVkdUKTFhxN3HBq5G9nXGdFpWEvfoKXAKtkJC12HjS6dLP_D4bbwJbIgFvECEYYNY_vxUWbjYwneNYDfP62uKG9i2fx7z-oNVTa1HGPXq7a-ZmBmWfqHtuKNtEBZTojEP9LJtKMqQIfOJvIQx6iQ2vbR5EYexbDo7ApVseZVaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g4oC_FMSijyySk9mTuSAS0cqvrWxavZLAPJKXSPECblcpfk7zKVHVKH-sV8Y-ySLTyhsId_ScPRABgpsdEGX_sDA1xe7mx_-aK6di5gJ677Rv3hN-FtwWPJJCJxkdDHoGsqyfdTbU9EcaD0ARuH-G78DyUrI492_dO4lGmsSY3IfEHl853Uhe_RqP6NpxOxdlMElo8Cn-zDK-XKKUSM0X17Jd6xuz6nfbM6WYyVXU_uhIbSKZRiA8AVW6ImQucS2NsClOJGt9ZZPIS6AYn5i1IUOkmLFpRfm5j0VfY1gpdhqVXnZ5HAu1XD6__uf8wepJkKje_8J2sSfpdMQGfkrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esjS5ENgziqO-9liWPNht25oLUvr_xRZLLWS-yjcN4m-vqVpbBOLq22XcPkYmm1f2PTFR_GhWdmAjWz3gA7xtp1qwTzcBbDmddjelK04xIJRpimcgWXQXRWdyXITdMKNKg8QjGpUvbbDVxVh3boymSHLEDfCpb3wYG-4MtWMrgaaxYpMSisKYsFNfhV-p80tC_Vte_R6qTeosSajJyJM_yImKzmtsqBMQiE_yER2iDRU1ily2UPWOvHQoZzTF7_6ErbTy-3q8IT7FRVXx_j4d11Vk-A06AV053JYsec-XKHPqlo-7N_gwxOqCGo3CNIjH7_5xwS3XJ6GWjm73-h1-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okcdXShh0gu0OJRryus9ev4It5TfOL1fUqOWJfYzdqEVaeyT3pGv-yioCNpR-m8MCmoF1JqoiXCy9X-ydk9LwgCEI444DyjXiMsJJbkaS6pzzOLxEx_gUhA7oIsd7RxmcDhywYjYXw0fOdP2jN08BDsSmr8hvjRPe5gf2ie30mAQ3tIm7JidU0vnyuXpWmGQqXdBiUwdHKUSfbbQi4OEXYCzHO2xTIpz1Cu22nPpfsG54rPTOfEtCAteHow13ZqzrFS8-SPpAKwSI-CZ1_jiBAd5yElPd0jnDuh6_eyDr8D6eKooZiYoqUj0QpXIWl-3syWZxWxvlJH6oYPI1xGlcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuyBXX7loyLRZC7L3GJGGtK7v8_zVDgFb6Wx0ORdXKLTZs7XtTuxDIG7imU4_PFmXZ-nY0s477uOMY8N9Uw47KwxTG8OVlQrU8jmFbXmerRl_70FRY3hhkZHKl4srBneE9_Gnwmzr9ReQ_wEJrlembMABwfyUwRjKmqw7hvr63SSAkAAc9tZogQUbZg7OFCfLWlePHV_vmoKL5fayhxeWhtI1SlyRvS6B_CxrxkLD9X7EdipTtt016O3RPmr_bmkM2lNm3TiIcxCY9p0c9FUkJnPN3iTQsSSZgB71BaiyuKcaH3WfJRB53xJU8kVYx9cbB_9CkaPeE3VuAPxs0Ppgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwyBXtSedTzHYiFJW6-nmVGXFtuDWDB5q2jxfa1__vlD4vOC_pFiOpIKBS1DlCovUIl8SPxy7z_wFHiOnt6cQxfuw-zpsiJ9PdUmMoX0Hc975kd2c0AMFMHrxj0_oWR9iX_me4N-YYc5B2B6KM-zz2SRYkI5VXkSAr3BqRqK8-JUKmEv3I4fX_n6DYSIi2k1ngteomyK5x7S6Md9sBcVOMaBZCQHyvSdHrbKloDOQMNT08o6w2JllyhRUFSj8c5f2OOpGAu31awtezQU8jcw5XvVMcJfvEZSeim2O53obbttpLO9FgG8H5ukM_LVY6s8CCCr6ma5lTSfmT5I3GNFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=Uoj13SAFKHq1lwaJPb3QaVYQco0pDqqSVRs7mjd-LYinqOYR6aq5jtETjbz6jV1FerLlL9yvGqFfPSJWNkFoBg_J1lZSqXLTMoSxtvOJmC85BpE7YpOecuEx0DoYdA_bISwK67PMmfBXTOFbbgekqk16qvnCgA3026uxp_2MSMYMogx3FdyXk3QbXCvwSD_kVbGhT0jDdDrUBDMknaf-CzkTSwVoOLfZ3mTTmq6I2G07FkFRecP-Mu2hpaH8jY-XaS8xbNtck2RBHTGYcb5qYHrNXi_0JTiSDC40h1ENGzhrnWLlMhhu4_2f-q_mzmBp-59VV2QX5QlerPkJD2Vuog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=Uoj13SAFKHq1lwaJPb3QaVYQco0pDqqSVRs7mjd-LYinqOYR6aq5jtETjbz6jV1FerLlL9yvGqFfPSJWNkFoBg_J1lZSqXLTMoSxtvOJmC85BpE7YpOecuEx0DoYdA_bISwK67PMmfBXTOFbbgekqk16qvnCgA3026uxp_2MSMYMogx3FdyXk3QbXCvwSD_kVbGhT0jDdDrUBDMknaf-CzkTSwVoOLfZ3mTTmq6I2G07FkFRecP-Mu2hpaH8jY-XaS8xbNtck2RBHTGYcb5qYHrNXi_0JTiSDC40h1ENGzhrnWLlMhhu4_2f-q_mzmBp-59VV2QX5QlerPkJD2Vuog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQvo_3-E3fJdj4HTgBuVceignvCthiNPigkUQUshnYkNi46CZiKqWgLx5oNjHQPEEF053YuGaDc_sGOTJ96VzJA2sebXo8EcrKj9Jm9mHoXI18ugfRraA4kMErSIERjkDGFVvzfZY--28p7DNB3pQ6lEtiWgty0CrhYWW9BTRqXnYZOWI8gggECKGMCAa8ogYhVRsb8c4vhP0qtGMmiFHAtP6avJQMQqwMOnQNlPLs5iR2buwCn_wX6Y7UmJH_T4DHEQ23MiAYTLmquuD4NMZ3TetL7DzF5ktyMzDna5zK3IsRfOPaowjUbquEx-wvhJE6hZKG5Xxar6xP56zzFOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=sU1Jq0g40_4i_HfiSP1Bn9vhriVnMK6iKLqBRvhsJlcNjsoylntK6BhCDmRWq4ATXBEDvEC0JITLh2YC2wNQ1VNoO6xFiHNi4X2oTQVYvItTQHk2up4icNcurzUPr0Fomxlf0Ihrpxg39mks9eHQAvDlTW1OB1xKVkz6NyNH1E4e1mYb_-Xw1krXId-AOMeIWDMjwm78FHz6FcjHgI5X2HI4-IDIls2DMpRCsCFUtVggg0ILtr5yIOpELHIMNB79ycdnViDlmQL72GEgTfc0oWLI3FwzovmZjKZFbbIPZI35G2mvkI34XxFRXWOkk718nW7c1dmoFbW54xqATpc96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=sU1Jq0g40_4i_HfiSP1Bn9vhriVnMK6iKLqBRvhsJlcNjsoylntK6BhCDmRWq4ATXBEDvEC0JITLh2YC2wNQ1VNoO6xFiHNi4X2oTQVYvItTQHk2up4icNcurzUPr0Fomxlf0Ihrpxg39mks9eHQAvDlTW1OB1xKVkz6NyNH1E4e1mYb_-Xw1krXId-AOMeIWDMjwm78FHz6FcjHgI5X2HI4-IDIls2DMpRCsCFUtVggg0ILtr5yIOpELHIMNB79ycdnViDlmQL72GEgTfc0oWLI3FwzovmZjKZFbbIPZI35G2mvkI34XxFRXWOkk718nW7c1dmoFbW54xqATpc96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=YU29SHliYDRhA4JhQgx_scBv4dcXVnJKmaJUE5c6Vk4VJ50MlYQ6_TA5LmfYl9r50_FLsnUVhV0TpsbOlzLgnarzdA_Xbf8plEgEpv3aFynCx0ToUY8AUAOKrnTv0xDuVAVkkH_CKTD_s3-hYwd2aMw_PJ1-zYsYQn6r-o4J3vcjbKXZ87ytExcsziQyt92oLs9OUiPAmE2EPbzv672kV9HR-jBMvCkKDPXsWM6xojOLbaQdbDJ913zHuS3qxyODjZmi-4WovxbFbA08XUCJk1wAZhH2dtTi7p0djI0faOQu7braptptP3BiI1g0S1z0Nm0gb0m1mHY3tMCAg-1SOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=YU29SHliYDRhA4JhQgx_scBv4dcXVnJKmaJUE5c6Vk4VJ50MlYQ6_TA5LmfYl9r50_FLsnUVhV0TpsbOlzLgnarzdA_Xbf8plEgEpv3aFynCx0ToUY8AUAOKrnTv0xDuVAVkkH_CKTD_s3-hYwd2aMw_PJ1-zYsYQn6r-o4J3vcjbKXZ87ytExcsziQyt92oLs9OUiPAmE2EPbzv672kV9HR-jBMvCkKDPXsWM6xojOLbaQdbDJ913zHuS3qxyODjZmi-4WovxbFbA08XUCJk1wAZhH2dtTi7p0djI0faOQu7braptptP3BiI1g0S1z0Nm0gb0m1mHY3tMCAg-1SOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=qiALfz7cVBlYUkldPASl-6iHlE14GrwBJWKJpCvRLCvA38PxlSyEZkeeV22BfkJylLLwVRVb-4ypUkrv5lJeXlWxiZAR1y8LVnY5j2NzwDyNVQxRTt3ldSiJzwTxcTebJexSQuqyLjF6oQ909v1IshWtB_6duQmTxkrJvopyrMuSUiEra_AfP4RF3sHW_QSDmiG-4Tib-r0dS9_AHH16FoIhhFUVcqFQLq1kVbFKCr759MOQIV32YrOKj1rSL3YliBP-BbYPpxJ8rWBsi7lR4ACG9UtJQs-J5npKy8447oFVjpWMVi5H-TeKGwVHoTjZ-cIV1h2sbQkUGn09hyLX5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=qiALfz7cVBlYUkldPASl-6iHlE14GrwBJWKJpCvRLCvA38PxlSyEZkeeV22BfkJylLLwVRVb-4ypUkrv5lJeXlWxiZAR1y8LVnY5j2NzwDyNVQxRTt3ldSiJzwTxcTebJexSQuqyLjF6oQ909v1IshWtB_6duQmTxkrJvopyrMuSUiEra_AfP4RF3sHW_QSDmiG-4Tib-r0dS9_AHH16FoIhhFUVcqFQLq1kVbFKCr759MOQIV32YrOKj1rSL3YliBP-BbYPpxJ8rWBsi7lR4ACG9UtJQs-J5npKy8447oFVjpWMVi5H-TeKGwVHoTjZ-cIV1h2sbQkUGn09hyLX5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4G9Ki18H9TyR8VJZ81fyuqxGtcFZwzJv_xl-v4dj4EQDKWKpTNhSVKblFyW038RcCnmXVb3RQ--vDNUYjOc29hnWkznKlH1Cn_IarhYh1SxzM0YLhIi3zqMQ0QwBmPsQOUyIFA7d1yiUvezTtJ6_tNpyVx8MGFM5v7mhng3g7jRrWeYTo60bdS6OqlWYzinmqGSwPFQGIJ8sWLq6KLAvXKLRHXlwAE0qlvUlkp3fM6Z7RyQFkEpnh6nzZTeJMM3cj7Ngq184KMbPBfyK-in9VbfKtmKLRazpzs1WXRKdbpEaVWUJ42cZSK9-FF-zHp9BQG34cjr0s_nQWFujBXnog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eizjYh0Oy3qLSkaldSjRwIN8DC4xvFe56c4dkrd5p8-ByWWUXvXby4G3pjoTGZTgu0AmZ7bdNRfYdMD-kG04QkRa4rmnbj0nLy9rcwxP5t9CTWi5pTpv1MOdQ32iPwdy1-V1zwY43HPrmRO8CJ6fXqlvXyOI3yuQJ4fmaJAqE1TlDBDFy5udkrHxZfyPDVP8X5Nx1Oo6TxTfB4hHhtTmoBHs8AhemskPvF6y32Z8RawtVejMCrLNZXOzqnhKcPEL0UjaX8bLysB78NfrZNwyGSHzr_5SYyvN5vNtKkwhfygmtrEFmziC2mkL6-cH8vbt3tbulHWnT48kdUGG36GfYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
