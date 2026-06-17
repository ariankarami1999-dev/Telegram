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
<img src="https://cdn4.telesco.pe/file/OqkIfdE7UyyexyzDUvqd6gaCTPcDr6J_TTdSpaj9I7CPLVNoFpYvRJZvIav4OvTDonO9T69zL_vndEPzJGTJVF3isCOcKJuDWWAM1LylOLiJx-sd6TGpZ4UuCq2Ks5Oeznn5pgMhHSNct3tAEq5arE0_dk5afJKboRxsAIzRfX_qgnG9cC6moldalgZqEuzFLsl2XjYrHUyJpM67pnFOm_fn90MO-7YMyx8LwoPAoDzDijumUqsgRX5ISkV0wiMoMdFyRYfW1JjEq-SQshmvQbLHZq2oCjr21Hy5bLFcbi59IaMtmNN0sSOiiRSrA8HK63iClERNJsEs_ItsplrmOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 17:36:46</div>
<hr>

<div class="tg-post" id="msg-15155">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">️جی‌دی ونس: برخی افراد فقط می‌خواهند بمباران ادامه یابد، صرف نظر از اینکه آیا برای آمریکایی‌ها دستاوردی دارد یا خیر.
ترامپ سعی در ایجاد بدبختی برای مردم ایران ندارد
@withyashar</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/withyashar/15155" target="_blank">📅 17:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15154">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسرائیل پرچم خود را در منطقه‌ای از سوریه برافراشت
منابع خبری در سوریه از نفوذ نظامیان ارتش اسرائیل به روستای «القحطانیه» در استان قنیطره خبر دادند و پرچم خود را برفراشتند
@withyashar</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/withyashar/15154" target="_blank">📅 17:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15153">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانال ۱۳ اسرائیل: آمریکا جزئیات توافق با ایران را از اسرائیل مخفی نگه داشته، زیرا نگران است که تل‌آویو محتوای آن را فاش کند و کارزاری رسانه‌ای علیه آن به راه بیندازد
@withyashar</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/withyashar/15153" target="_blank">📅 17:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15152">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پاکستان خواستار تعویق انتشار متن تفاهم‌نامه شد
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در گفت‌وگو با CBS اعلام کرد که طرف پاکستانی درخواست کرده است متن کامل یادداشت تفاهم (MOU) فعلاً منتشر نشود.
وی بدون ارائه جزئیات بیشتر گفت که به درخواست پاکستان، متن این سند به‌طور موقت محرمانه باقی خواهد ماند.
@withyashar</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/withyashar/15152" target="_blank">📅 17:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15151">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سوئیس: امضای یادداشت تفاهم ایران و آمریکا با حضور نمایندگان ۴ کشور ایالات متحده، ایران، قطر و پاکستان برگزار خواهد شد.
بیش‌از ۲۰۰۰ سرباز امنیت محل امضا را تأمین خواهند کرد و برای تضمین امنیت، منطقه پرواز ممنوع اعمال خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/15151" target="_blank">📅 16:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15150">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تسنیم: اختلال خدمات بانکی ادامه دارد , تجهیزات شبکه فرسوده هستند
@withyashar</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/15150" target="_blank">📅 16:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15149">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ایران امروز یک تفاهم‌نامه با شرکت سهامی خاص هلی‌کوپترهای روسی برای ۲۰ هلی‌کوپتر سری mi-8/17 امضا کرد (۴ تا از آن‌ها قبلاً قرارداد بسته شده است) که باید تا مارس ۲۰۲۷ تحویل داده شوند تا برای مقاصد اطفاء حریق، انتقال پزشکی و نجات استفاده شوند
@withyashar</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/15149" target="_blank">📅 16:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15148">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff486d39a.mp4?token=IvIlFEG6AseEpBHGoOJ0fjOvo5wigaxQwV2DQQTx5JvEyyA-zcmvLEl6fS8ol8kx0nqTFZ-Yu4wbzpgziSiF1uxZZ1JPMZUD2BKnmai8Qo0vkxZMX-tYS1C3XvqLZXMXRNpbNluI53_67Ny1MHz0J48kLixIzSALcBbpdsFZrVaej4vD38hYrqCnWI__TILI1dh07a8oV-ZvzxvRKF7BtGjCxCIJ7lS1dbu1rqUqzGFBjvnkrmB8GJ_eM1XCmXTsOO4s5Yb7W7Dfk93awwff0EzfHELbGNAiVz786IO694I5Vu7lUwumHSaFLNgEvRLpl9g358zgi0lPepDuq9BHPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff486d39a.mp4?token=IvIlFEG6AseEpBHGoOJ0fjOvo5wigaxQwV2DQQTx5JvEyyA-zcmvLEl6fS8ol8kx0nqTFZ-Yu4wbzpgziSiF1uxZZ1JPMZUD2BKnmai8Qo0vkxZMX-tYS1C3XvqLZXMXRNpbNluI53_67Ny1MHz0J48kLixIzSALcBbpdsFZrVaej4vD38hYrqCnWI__TILI1dh07a8oV-ZvzxvRKF7BtGjCxCIJ7lS1dbu1rqUqzGFBjvnkrmB8GJ_eM1XCmXTsOO4s5Yb7W7Dfk93awwff0EzfHELbGNAiVz786IO694I5Vu7lUwumHSaFLNgEvRLpl9g358zgi0lPepDuq9BHPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: دلیل پایین ماندن قیمت نفت این است که هر شب کشتی‌هایی را از بین می‌بردیم که حتی شما از آن‌ها خبر نداشتید.
دو روز پیش، سه روز پیش، یک ماه پیش، ۲۲ کشتی را از بین بردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی را از بین می‌بردیم. هیچ‌کس این را نمی‌دانست.
نیروی دریایی ما کار بزرگی انجام داد. هیچ‌کس نمی‌دانست چه اتفاقی می‌افتد. به همین دلیل نفت به ۳۰۰ دلار در هر بشکه نرسید؛ بلکه به ۱۲۵ تا ۱۵۰ دلار رسید.
حالا قیمت آن ۷۲، ۷۳ دلار است. شنیده‌ام که الان حتی کمتر از این است
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/15148" target="_blank">📅 14:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15147">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: با احمد الشرع، رهبر سوریه، درباره مقابله با حزب‌الله گفت‌وگو کردم.
@withyashar</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/15147" target="_blank">📅 14:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15146">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10b0e16f.mp4?token=HtAowuMxu2kSFNyJMCjHIojtxZa_13TN6VhRbjJvod-cHYN4R1r_ZM6yUvWZYIPHUsL12VNku3hWPNIRDZNa6McBZNpeYlLJZcoT-3lv5LVXLVMfm9cliDVNwYE3LOqvo_WBz2ebrfiE40kqSW3zuKWMjNdgnPBkvbdmjLl5kL09Tus7gQparTlnEmmBzg9G1TYsayFDOD-8N0GuDoJIdZBazC7xXdsr3E7rK5o-HaiBr4Ig_eTFB_PUbokUzWwab7yRnJO8mBYJl4Kf3xnd2ZRlv-4DgOLZqreHh7kLz6ElCZIOJFvCS2lPC748CvxJb4iP8uaWD3KyBnvnd_W0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10b0e16f.mp4?token=HtAowuMxu2kSFNyJMCjHIojtxZa_13TN6VhRbjJvod-cHYN4R1r_ZM6yUvWZYIPHUsL12VNku3hWPNIRDZNa6McBZNpeYlLJZcoT-3lv5LVXLVMfm9cliDVNwYE3LOqvo_WBz2ebrfiE40kqSW3zuKWMjNdgnPBkvbdmjLl5kL09Tus7gQparTlnEmmBzg9G1TYsayFDOD-8N0GuDoJIdZBazC7xXdsr3E7rK5o-HaiBr4Ig_eTFB_PUbokUzWwab7yRnJO8mBYJl4Kf3xnd2ZRlv-4DgOLZqreHh7kLz6ElCZIOJFvCS2lPC748CvxJb4iP8uaWD3KyBnvnd_W0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ‌ در‌کنار ژنرال السیسی (واقعی): فراموش نکنید، هیچ‌کس هرگز به اندازه من با ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری از افراد دیگر انجام می‌شد.
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/15146" target="_blank">📅 14:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15145">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ: قابلیت پرداخت فقط یک حقه دیگر است. آنها کلمه «قابلیت پرداخت» را ساختند
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/15145" target="_blank">📅 14:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15144">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: یادداشت با ایران نهایی نیست. اگر از توافق خوشمان نیاید، دوباره به بمباران بازمی‌گردیم @withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/15144" target="_blank">📅 14:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15143">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: یادداشت با ایران نهایی نیست. اگر از توافق خوشمان نیاید، دوباره به بمباران بازمی‌گردیم
@withyashar</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/15143" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15142">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT5ZtwLy9qfwUOkdwEM53a8I-BtzAXLYDc75jwPauErju-2mCW1GXjZL6Wn2g83kOQ9GjE4BTToMy7GFavsKHvGSdvGwU_UmNTqSZzutnPMFK8ovyflkVGorABjYkINLaVi8XashJk7i_-3Q1lkUcQruymo7NSpO7sUQjkhgBe5dsmXhMOOJMpoM8uoHgwLaDCy0D5k_7o3FHQZxTCISrgpdoRY3BnBLViNKWWvfPmbG44Upd8BlpsX4zcoRjakLb6XQ96-P2wNZ9P52BLToD5WMFJpHcZyjXS-mFzcm3Uh8Y9mvkEWn2h5zBUs7AlrlSnnvdTgpLHylO7p6WthKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندرو تیت که ۱۰۷ بار لیکویید شده، دوباره در صرافی هایپرلیکویید با اهرم ۴۰ و حجم حدوداً ۴ میلیون دلار، روی بیت‌کوین پوزیشن لانگ (خرید) باز کرده و باز هم بخشی از سرمایه‌اش (۱.۳۵ میلیون دلار) لیکویید شد.
اگه قیمت به 64,626 هزار دلار برسه کامل لیکویید می‌شه.
نرخ فعلی بیت‌کوین: 64,800$
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/15142" target="_blank">📅 14:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15141">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d627cfcdc.mp4?token=VQZZJbE-T4dCo7xLRREddp-ke-McUskqFayXR0fI_EOIttFliRtHOQme0iJRfVN6CF4bOqj8TAix_I0x3bGkiQRUtVRfxllvLBKuhXdesxoV3T0LovQMEfpJF_pOpNgl7o7v3wxJ5ubBr4cfl5qGq23YBrFohA3pWNiqAWuQuD4KYK3O5S8AkcvD70hRb_Pp_Cmg85VX_xkuoiZlcv9OwBq_7GAzzivbOTl5yrqb5gtR8ZKvpIp09BD3J96rXyIuWOORP25qQr05I3yiP04rYO9R1GRWny5dmxUW4HhE5vIHF9Fx3D35LXO5QZfICBtsatb6hLDXGdEfB93NbBT9Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d627cfcdc.mp4?token=VQZZJbE-T4dCo7xLRREddp-ke-McUskqFayXR0fI_EOIttFliRtHOQme0iJRfVN6CF4bOqj8TAix_I0x3bGkiQRUtVRfxllvLBKuhXdesxoV3T0LovQMEfpJF_pOpNgl7o7v3wxJ5ubBr4cfl5qGq23YBrFohA3pWNiqAWuQuD4KYK3O5S8AkcvD70hRb_Pp_Cmg85VX_xkuoiZlcv9OwBq_7GAzzivbOTl5yrqb5gtR8ZKvpIp09BD3J96rXyIuWOORP25qQr05I3yiP04rYO9R1GRWny5dmxUW4HhE5vIHF9Fx3D35LXO5QZfICBtsatb6hLDXGdEfB93NbBT9Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎بخشی از سخنرانی قالیباف که تو رسانه‌ها وایرال شده
دیگه ساختار مدیریتی کشور از فردمحوری خارج شده و گروهی تصمیم میگیریم.
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/15141" target="_blank">📅 14:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15140">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزیر دفاع اسرائیل کاتز: تمام روستاهای نزدیک به مرز لبنان به صورت سیستماتیک ویران می‌شوند.
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/15140" target="_blank">📅 14:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15139">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فاکس نیوز: ترامپ به زودی درباره توافق ایران کنفرانس خبری برگزار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/15139" target="_blank">📅 14:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15138">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تسنیم: متن توافقنامه به صورت کامل در روز جمعه و پس از امضا منتشر خواهد شد
یک منبع نزدیک به تیم مذاکره‌کننده   گفت: تفاهمنامه همانطور که پیشتر اعلام شده ۱۴ بند است و موضوعات مربوط به ۱۴ بند نیز بارها در رسانه‌ها مطرح شده، اما جزییاتی که در بلومبرگ‌ درباره هر بندی آمده است در موارد قابل توجهی ناقص است.
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15138" target="_blank">📅 12:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15137">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRnw-DTlwwU2oABOhyOYtb5MyWtEb6sytpNukUzyHYNGJpk9MgyB5_COaR7DQHmm-6kS1P9g47rljxxVMxc3QtIhdE6zxktNKswkZ6Xk4YO4tpl8Xx9oz2aj7I_YiBigdIH0sSFmRRcv1tSV5GyHlMHmip_KlGz89BzfCeL3OIfijWEQBfgPWXlQwhgaL1p0tt-5jyqQvwdpqlAGQ-zqI3_7laZufBivP9mc3H2LNYOgYpo_HFFfv3CaXZ5ABNNoKu8rGHiYIC9XJQuNKtRRUp3v_CXtD58ymB4PrVWmtViHssyPGHYdAD-Dl1Uxhfxh-eix0VYI68U6T1Axnie6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودرو پورشه سردار آزمون در کرمان توقیف شد
به گزارش تابناک به نقل از ایسنا، سرهنگ اکبر نجفی ۲۶ در تشریح این خبر گفت: خودروی مذکور که به دلیل تخلفات قانونی و برابر با احکام صادره در لیست توقیفی‌های مصادره اموال سردار آزمون قرار داشت، توسط گشت‌های محسوس و نامحسوس یگان امداد شناسایی و پس از طی مراحل قانونی، به پارکینگ منتقل شد.
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/15137" target="_blank">📅 12:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15136">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صدای انفجار‌ سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/15136" target="_blank">📅 12:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15135">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بلومبرگ به نقل از یک منبع آگاه اعلام کرد: واشنگتن شروع به توزیع محتوای تفاهم با ایران به کشورهای متحد در اجلاس گروه ۷ در فرانسه کرده است
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/15135" target="_blank">📅 12:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15134">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرگزاری فرانسه: یک گزارش حقوقی دولت آمریکا نشان می‌دهد ارتش این کشور از ابزار هوش مصنوعی گروک متعلق به شرکت اسپیس ایکس تحت مالکیت ایلان ماسک، میلیاردر حوزه فناوری در جنگ علیه ایران استفاده کرده است
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/15134" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15133">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پمپئو وزیر خارجه سابق به فاکس  می‌گوید اگر برداشت ایران از موضع آمریکا درست باشد و تصمیم‌گیران اصلی (سپاه و رهبری) واقعاً تغییر رفتار بدهند، می‌توان به عادی‌سازی و حتی ورود سرمایه‌گذاری فکر کرد، اما احتمال چنین تغییری را بسیار پایین می‌داند. او تأکید می‌کند نباید هیچ پولی—چه مستقیم، چه از طریق واسطه یا حتی
آزادسازی دارایی‌ها—به ایران داده شود، چون به‌جای رفاه مردم، صرف تقویت برنامه موشکی، سپاه و خرید تسلیحات از روسیه و چین می‌شود. در عین حال می‌گوید اگر واقعاً تغییر واقعی رخ دهد، از آن استقبال خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/15133" target="_blank">📅 10:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15132">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBaBrDKqSM8YqLI1OnybSv9Ml3C20RhMDQI9b0QWE0aR3UhJO_rp0Hlx5cGyyrICB1Ebtw0LeOv5Ssen_o9HV2DSOPlOuN3MPETaApOIKayoQWcbqbtZFOhTknUUf2YkyllHoUKWoXRHWFBzaWSUZ1A3sXrI3-IQi2XP6DcrfQ1AvPDykv2eUb49OB4_X2uxFk_HX4D3yenyV5XzM0wngi579yVT63eMiba_QG2UEz5veIyZldQv1yltcJFqzgGWqaKIFZjd7f-yIjxvDgiYye2SWqqcyUWr790LSsJ3xhRpU1rv79FNmO3WxhCNi8YOafpTVpUZBVNeQldSzc_RqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ایرباس موقت ایر فورس وان که توسط قطر اهدا شده، رنگ‌آمیزی شده و در نیویورک آماده است — درست همزمان با تعهد سرمایه‌گذاری ۱ میلیارد دلاری قطر که دیروز اعلام شد، بعد از آنچه برخی آن را تسلیم کامل آمریکا در برابر خواسته‌های قطر و ایران می‌دانند.»
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/15132" target="_blank">📅 10:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15131">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یديعوت احرونوت ادعا کرده بالای ۵۰درصد از پول‌های بلوکه شده ایران دست چین و عراقه
رقمش هم کم نیست؛ حداقل ۳۵میلیارد دلاره!
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15131" target="_blank">📅 10:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15130">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرنگار اسرائیلی : این یک اشتباه تاریخی است.
پرداخت میلیاردها دلار به بزرگترین حامی دولتی تروریسم در جهان، فقط باعث تأمین مالی راکت‌های بیشتر، پهپاد‌های بیشتر و حملات بیشتری علیه اسرائیل و غرب خواهد شد. این سیاست «آمریکا در اولویت اول» نیست.
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/15130" target="_blank">📅 10:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15129">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c657925428.mp4?token=aat-EtukME0Nvj-M47dc7OZ3yUmjmm3WNZVTvGydl89MAXTiP0d01Vcyf1YgWQPqfxnsTGAzW69UlifVkyQw_MuUtKXnQDSJ5kXJBHR0ONZQk9L9C7L4lM8D0V8naFibrEtd9aC_031lWbC9poMzT7xg5SneHYhY4cW5cCnME5FL2eVl3tIkmJlGqePTEC1ikrfPBC9Ip-GR8Tu1Vs7ZAgiipLsA0VlYnhsFbmK-Dh-tk9wv4yonUcsFXvooYtWmxIPpzcPqsb6xjiuh4YPJXEymOGBbbQKPMVapZmxG29OMKRhqaHqZDLQ_Q2Oowy9YuS9TbCgWFfeU_TgHCnU8xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c657925428.mp4?token=aat-EtukME0Nvj-M47dc7OZ3yUmjmm3WNZVTvGydl89MAXTiP0d01Vcyf1YgWQPqfxnsTGAzW69UlifVkyQw_MuUtKXnQDSJ5kXJBHR0ONZQk9L9C7L4lM8D0V8naFibrEtd9aC_031lWbC9poMzT7xg5SneHYhY4cW5cCnME5FL2eVl3tIkmJlGqePTEC1ikrfPBC9Ip-GR8Tu1Vs7ZAgiipLsA0VlYnhsFbmK-Dh-tk9wv4yonUcsFXvooYtWmxIPpzcPqsb6xjiuh4YPJXEymOGBbbQKPMVapZmxG29OMKRhqaHqZDLQ_Q2Oowy9YuS9TbCgWFfeU_TgHCnU8xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک پنس، معاون سابق ترامپ: «به نظر من بهتر است به نیروهای مسلح ایالات متحده اجازه دهیم کار را تمام کنند، تنگه را باز کنند و قابلیت‌های تهاجمی ایرانیان را از بین ببریم و به مردم ایران فرصتی واقعی برای آزادی بدهیم.»
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/15129" target="_blank">📅 10:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15128">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چند ساعت پیش، دونالد ترامپ با استناد به قانون تولید دفاعی (یک قانون از سال ۱۹۵۰ در دوران جنگ سرد)، دستور داد تا تولید مهمات، موشک‌ها و تجهیزات دفاعی آمریکا سریع‌تر شود. این فرمان در ۱۱ ژوئن به وزیر دفاع پیته هگست ارسال شد و مشکلات سیستمی در صنعت مهمات را هدف گرفت: ظرفیت تولید محدود، زنجیره‌های تأمین ضعیف، وابستگی‌های طولانی‌مدت و گلوگاه‌های تولید.
هدف اصلی: تسریع تولید مهمات حیاتی، موشک‌ها و تجهیزات دفاعی برای دفاع ملی آمریکا.
نحوه اجرا: قانون به ترامپ اجازه می‌دهد با شرکت‌های خصوصی توافق‌های داوطلبه ایجاد کند، تولید را اولویت‌دار کند و زنجیره‌های تأمین را تقویت نماید.
توافق مهم: شرکت لاکهید مارتین اعلام کرد با دولت آمریکا برای چهار برابر کردن تولید مهمات حیاتی به توافق رسیده است.
دلیل اقدام: کاهش ذخایر تسلیحاتی آمریکا پس از جنگ با ایران و استفاده از مهمات در ایران و ونزوئلا، که باعث افزایش سفارشات مهمات شد.
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15128" target="_blank">📅 09:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15127">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdyhZgQADxwlQ0cib-NmlhtLz5KwklZ5eGyVA5k_-RiNTUwJN-XRvPR82uMOXtKJJwRMkY58kmXGDRgGyjic7g5G4Uq30_1oASE6Eso7fzxmLkPMFHE-ul-NXNXYr-3mMBN72GWjFIljfpAOy5F5ean6CAsa9VFqtPvGpt9d_t-bCNn66ML99F94eoHG0pldYcMly1dhaMQwuAJpT9c8JCPGyvIzjT9jscprT84u57pUmRxMU0K-CgIbYLMlblETvPwZWC_6szUVYtaehQnZeOWxtIskA30EFafCXK7FO93nAXfhJlo5SUdg7PAS5YpSOp7LBDPKgvILivECha7C8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️ارتش اسرائیل اعلام کرد یک انبار تسلیحات جدید حزب‌الله حاوی ۵ تن مواد منفجره و ده‌ها پهپاد انتحاری را کشف کرده است
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/15127" target="_blank">📅 09:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15126">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15126" target="_blank">📅 09:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15125">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تنکر ترکرز: ۳.۸ میلیون بشکه نفت خام ایران از محاصره آمریکا عبور کرد   تارنمای تنکر ترکز بامداد چهارشنبه گزارش داد، دو ابرنفتکش ایران که مجموعا حامل ۳.۸ میلیون بشکه نفت خام هستند، از محاصره آمریکا عبور کردند @withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/15125" target="_blank">📅 09:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15124">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرنگار العربیه: جنگنده‌های اسرائیلی دو بار به شهرک‌های «انصاریه» و «المنصوره» در جنوب لبنان حمله کردند.
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/15124" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15123">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بلومبرگ: به گفته مقامات آمریکایی، معافیت فروش نفت ایران فقط شامل محموله‌های نفتی می‌شود که قبلاً بارگیری شده است و شامل مجوز گسترده‌تر برای از سرگیری فروش نفت ایران نمی‌شود @withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/15123" target="_blank">📅 08:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15122">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15122" target="_blank">📅 08:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15121">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، با بازنشر گزارشی از شبکه 14 اسرائیل درباره کشتار دی‌ماه، در ایکس نوشت:
«قربانیان سرکوب در ایران و خانواده‌های آن‌ها شایسته حقیقت، شفافیت و پاسخگویی هستند. جامعه بین‌المللی نباید در برابر این وضعیت بی‌تفاوت بماند.»
او گفت: «تاریخ حکومت ایران با رنج مردم خود نوشته شده است؛ اتاق‌های شکنجه، گورهای دسته‌جمعی، ناپدیدسازی اجباری و خانواده‌هایی که بدون پاسخ رها شده‌اند.»
@withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/15121" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15120">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">منابع عربی: اسرائیل حومۀ شهرک نبطیه‌الفوقا در جنوب لبنان را هدف حملات قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/15120" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15119">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وبسایت خبری سمافور: مارکو روبیو، وزیر خارجه دولت ترامپ با انعقاد یادداشت تفاهم نامه با ایران مخالفت کرده و هیچ اظهار نظری درباره رسیدن به توافق با ایران نمی‌کند.
وزیر خارجه آمریکا امیدی به رسیدن به توافق هسته‌ای در مذاکرات با ایران پس از امضای یادداشت تفاهم نامه ندارد و تاکنون درباره امضای یادداشت تفاهم نامه با ایران کاملاً سکوت کرده است
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/15119" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15118">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwiTtxXShJqJHTdk_6sgcteliW2GkggLgCkhOBLqb-8V0YH8AEM8cZTRdZfnbIq4krqwcHRIlT55KvOtlP6kN2meAl4tyjED0N9y5FjdEhBlLlASBWppg6oMzBWOo37Nu-c_1yllVl9Wz0tffpMMVJPo61d0cVGO5bwxdcOxdp77zvBltBZBQgyXOWaFe9CWXMJ-4u7MV0Be3HNLlZFvgnSaLkFp1olb3_k-CfgE_2GUY_TRPscO7-6OpmueEf6QWmtNeyAs2ghNx3V2xPiP1F4OQZ_Kq5yZoueRdBq4d7Qj6ZB3B2n8dDZf8yeh8WbvjsXTRr4rJXs-s6q5HF2-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: به گفته مقامات آمریکایی، معافیت فروش نفت ایران فقط شامل محموله‌های نفتی می‌شود که قبلاً بارگیری شده است و شامل مجوز گسترده‌تر برای از سرگیری فروش نفت ایران نمی‌شود
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15118" target="_blank">📅 08:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15117">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NafGg3rs6ZbNayO8pLslCPlt04gkAnMcuQ0MJm5lhQxpbisCGrJYS7pTlOievSufEPezAZSzriQZIY1yPbBBLYsPhY0sOSY7zZtvLL_u5b3MuibG_hxJw5nyUFd9tPHG_ZK21qnN_-vWngKBN4vdsiEJ1HegwcdGudzzTzCEnOT-ql810KBqOOHLfv3jv9Gff7CGht7nsS9IKpBY3NlLXkGY285gLE8jTDc5inLcrsTrVaPgtrwTeOtafmrmOfbjzHBFpaudxhL90VPySIubIhB0uOt4-4O8-2lR8eJi3IUHq5ymB6hyOYCYNobHhN4X9Tv-Z_sqB7xlLYebpaPZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید:
«نه سلاح هسته‌ای، نه لغو کامل تحریم‌ها, نه پول»
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/15117" target="_blank">📅 08:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15116">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
اگه میخوای بدونی قیمت دلار طلا خودرو .... درسال جدید چقدر میشه این چنل تمام پیشبینی ها همراه تاریخ وقوع رو گفته
🕯
@link
🕯
🕯
@link
🕯
🕯
@link
🕯</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/15116" target="_blank">📅 02:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15115">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPGdg_iy1_aMouWTfZS_N-iyI-NDeAZEmKn244eaa5taB7IOtvs8zUcA-gULiG78sWpcVRAAi7rW8t2Dl4Fdbirkld1oYxaUwIWkj9-QNgZJwpbIjKbhIqpbr6PVvLTzlZKQOR7j7IbtXBtwu0i7kycrpwVfOnVmGRRN2EQq4ahO6yqgJ_rGS8urGF2SjF9Hr48H1MwpWbVjTSFq6BbfNpmzHPI0UJdIWgMgDvH5hWYgIyVFRUGr6nhsWRrq5DXGPhXECo4R0RQB9_CXUYdoOAFFR7AnL_17o4r7IqCVcj1lTn5jRuZQCux7hFjRHA8Gk9SVgxDFHPukZtUzRrr3GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین  الان ، چه خبره خلیج فارس
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/15115" target="_blank">📅 02:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15114">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/15114" target="_blank">📅 02:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15113">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95de30e10e.mp4?token=iG0ZynP2rd2iQ4cFJOO9SPXvtMfAoLsvhCo3gixvwwLmXHGwvLZqch_p1hck1QhgIbZmXf9BOUnxPQDghEjCWnBARCI2-wnhzV_0-xOjFwR_KqXK6nSVJaIBeCc9VhR7LmpKRx5bST94UsD_sJRoToVfuwZfH-jRNlMhgIkb0uGcmJtY9Oqk2U4M7iKni6Gn1dr0ufFKB9d5UbtmzVf1WR8I7xaoelnU1hGZHQdhWa9-3JHLhnX445DHHcvvoh3fd58kZTaiPVGsjVVk4TCbHH0HgOEHdVvvhx3HN7sTJ6S1N6PORZ22KPKbdopGvFxzZacKwPk2cxAY5odODFv6jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95de30e10e.mp4?token=iG0ZynP2rd2iQ4cFJOO9SPXvtMfAoLsvhCo3gixvwwLmXHGwvLZqch_p1hck1QhgIbZmXf9BOUnxPQDghEjCWnBARCI2-wnhzV_0-xOjFwR_KqXK6nSVJaIBeCc9VhR7LmpKRx5bST94UsD_sJRoToVfuwZfH-jRNlMhgIkb0uGcmJtY9Oqk2U4M7iKni6Gn1dr0ufFKB9d5UbtmzVf1WR8I7xaoelnU1hGZHQdhWa9-3JHLhnX445DHHcvvoh3fd58kZTaiPVGsjVVk4TCbHH0HgOEHdVvvhx3HN7sTJ6S1N6PORZ22KPKbdopGvFxzZacKwPk2cxAY5odODFv6jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس : اگه دونالد ترامپ حتی به عنوان رهبر معظم انقلاب در ایران هم انتخاب می‌شد، دموکرات‌ها باز هم می‌گفتن آمریکا شکست خورده
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/15113" target="_blank">📅 00:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15112">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23735193e5.mp4?token=NMEe0CQFmZ9Z9QUJr-9i-mGlUzkFbikQgPRBDnuuxsBwXXUZwTKpIJeD8nRY1VVyVLZ4wfZcqxsZZNqurQM8jdcwwzFAt0e_bNMsuFZAVu5HI5y5ugngYyitXsA3zfbKN4PZXQ18C6A6969Fli8CcopUtx6IVsSm5tpqutCDGKBQfuzvCZh2ZfP4QoJYuUhsvItshGnH5gp4x8T1sMBDjLr4OW8ZcrKuz8-2COCskPbhIuporjIovClbpYett6U6D7EPjcKpkL1ThACuSAD9umcjLRN005-OoGe5BagjebZm86esav0EugmGkkiSW5CKfc_ryydP-gJSSvh3YhOCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23735193e5.mp4?token=NMEe0CQFmZ9Z9QUJr-9i-mGlUzkFbikQgPRBDnuuxsBwXXUZwTKpIJeD8nRY1VVyVLZ4wfZcqxsZZNqurQM8jdcwwzFAt0e_bNMsuFZAVu5HI5y5ugngYyitXsA3zfbKN4PZXQ18C6A6969Fli8CcopUtx6IVsSm5tpqutCDGKBQfuzvCZh2ZfP4QoJYuUhsvItshGnH5gp4x8T1sMBDjLr4OW8ZcrKuz8-2COCskPbhIuporjIovClbpYett6U6D7EPjcKpkL1ThACuSAD9umcjLRN005-OoGe5BagjebZm86esav0EugmGkkiSW5CKfc_ryydP-gJSSvh3YhOCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور جی دی ونس:
پرزیدنت ترامپ هرگز نگفت که هدفش نصب رضا پهلوی برای تبدیل شدن به رهبر جدید ایران است.
آنچه گفته این است که اگر مردم ایران بخواهند قیام کنند ، عالی است. این کار اوناست این بین آنها و دولتشان است.
چیزی که ما می خواهیم توقف برنامه هسته ای آنهاست.‌‌
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/15112" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15111">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f65655673.mp4?token=SdYZfeJQleZpROczw2scQAlWLvI4uoqSz-1BMZlHlTkYDoxTGRL4atzw5SxvDW1ez8dJXxX6F17BdX-pUXQ8DXyQI2IMRYCBc4NQTOSurylb-FDpW2VC45Q8AyVAWi7E3yuN7zfsW4mJ3VsN0UPqv7ADhmDLeazSuefrDB1RSjFlk2VdI4ZgQCO2wyNfBv5PDAjfSYfiar1lnic7yIcArRX-_LrwFjThkEP73k9covWpSjR4Zi4frWAer8-n00h1fqlXd8hcP_iQe8ZwJSRjwI9RY_RwJket0X-U3D55T0rt8xaOg7GLRXfdkZMCexd5l5o_wiE2Cqzcc5lK6nrN4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f65655673.mp4?token=SdYZfeJQleZpROczw2scQAlWLvI4uoqSz-1BMZlHlTkYDoxTGRL4atzw5SxvDW1ez8dJXxX6F17BdX-pUXQ8DXyQI2IMRYCBc4NQTOSurylb-FDpW2VC45Q8AyVAWi7E3yuN7zfsW4mJ3VsN0UPqv7ADhmDLeazSuefrDB1RSjFlk2VdI4ZgQCO2wyNfBv5PDAjfSYfiar1lnic7yIcArRX-_LrwFjThkEP73k9covWpSjR4Zi4frWAer8-n00h1fqlXd8hcP_iQe8ZwJSRjwI9RY_RwJket0X-U3D55T0rt8xaOg7GLRXfdkZMCexd5l5o_wiE2Cqzcc5lK6nrN4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور در به در دنبال  دکتر خوش چشم هستم که او را به صنعت فوتبال وارد کنم
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/15111" target="_blank">📅 00:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15110">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">همکنون
انفجار های مهیب در جنوب لبنان،
گزارش های محلی از شلیک گسترده تانک های اسرائیلی و درگیری شدید با نیرو های حزب الله در تلاش برای پیشروی در جنوب لبنان.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/15110" target="_blank">📅 00:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15109">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اورشلیم پست: ماهواره‌های اسرائیلی در طول حدود ۴۰ روز اجرای عملیات «غرش شیران» بیش از ۵۰ هزار بار از ایران تصویربرداری کردند
میانگین هر روز بیش از هزار تصویربرداری
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/15109" target="_blank">📅 00:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15108">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جی‌دی ونس: برخی خواهان اعزام صدها هزار نیروی آمریکایی به ایران هستند
ترامپ جورج بوش نیست؛ در باتلاق ایران گرفتار نمی‌شویم
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15108" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15107">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">واکنش آمیت سیگال خبرنگار کانال 12 اسرائیل به توافق ترامپ:
ممکنه دشمنی با آمریکا خطرناک باشه، اما دوستی با آمریکا مرگباره!
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15107" target="_blank">📅 00:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15105">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کانال ۱۳ اسرائیل: ترامپ مانع اجرای یک عملیات نظامی‌برنامه‌ریزی‌شده اسرائیل در غزه شد
این طرح در بالاترین سطوح سیاسی و امنیتی اسرائیل بررسی شده بود، اما پس از ارائه جزئیات به آمریکا، واشنگتن با آن مخالفت کرده و خواستار عدم اجرای آن در شرایط فعلی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15105" target="_blank">📅 23:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15103">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">با این جماعت چه کنم
😞</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15103" target="_blank">📅 23:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15102">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArtin</strong></div>
<div class="tg-text">اسکل عقده ای یه پیام رو جواب نمیدی
عقده ای هستی زیاددد</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/15102" target="_blank">📅 23:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15101">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شاهزاده رضا پهلوی به نیوزنیشن: مردم ایران اکنون میگویند چرا بمباران متوقف شد؟ ایالات متحده باید بمباران ایران را ادامه میداد
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/15101" target="_blank">📅 23:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15100">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش حملات پهپادی سپاه پاسداران به اربیل عراق
🚨
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15100" target="_blank">📅 22:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15099">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به گزارش ان‌بی‌سی نیوز، کارشناسان ارشد صنعت نفت هشدار می‌دهند که علیرغم فضای مثبت ناشی از توافق میان ایالات متحده و ایران برای پایان دادن به جنگ چندماهه در خاورمیانه، بازگشت بازارهای نفت به حالت عادی و از سرگیری تردد در تنگه هرمز فرآیندی زمان‌بر است و احتمالاً چندین هفته به طول خواهد انجامید.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/15099" target="_blank">📅 22:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15098">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxBNMLFI7aEkL7CPO7bsxM4vH1S6LQj4267iOnGDu78Ufxu6BKnkAHh2XgnMQWuy914nagaUPEnKSVrWHalwCFQg_nGzA9hKjNeXpyf09RaFSN14tLZn4VxiO1k9vl8ePFBEOTLqXOaDrwubxYDM1ujKnTu-EaX4SSTd_VGqFoSvLZtPs7KTbauvJUxkIt37P_HMcD_X2TXHMthw8KhPrgaEGyuwfd_0uNVBMtlD9gGg61P88MHjwG8wbXuBMG6xQ9WT-2nI2X7zq2mH5dYTyum7FbkSie7AZ18Hz9k-gszZOL51JBpQJEJtWVxIvCk1gLNbeJOXII4dVvgA01JBEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پایگاه موشکی دیگر در شامل شش ورودی زیرزمینی، در حال ساخت است. یکی از دلایل احداث ورودی‌های بیشتر، قرارگیری این پایگاه در ناحیه‌ای استراتژیک از ایران می‌باشد
بخشی از فرایند ساخت پایگاه مذکور، پس از جنگ 12 روزه صورت گرفته است، هم‌چنین برخی از سازه‌های روزمینی این پایگاه در دو جنگ اخیر هدف قرار گرفته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/15098" target="_blank">📅 22:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15097">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b21de6065.mp4?token=q7Ygz2JGYxNjeZ1ZMptyf_uPFK1o3NJhF_09_RhN1LV58fr6YdVK4vZ48-HH8DauuIjGkGBO1kuHyEHGzatTFNPrNcBqSJhGLDPwBuz4RVPmy0qeHaFFyJvwSlOOGT5M7bHzCXpFUntxLp78O1eE8MrBATrJIOKz8JQJ9a-fiZ2az9F9nP40G8reigF8SYZETE0UlEwaKIpB8i9qHutnViDeSqAvFfOUzmU1loMitKWwL_rqWjGM2Dsw0KEInWxenRf_1UqMSv2UpSPHbQQE0MmGbqhBl78oduEmtcfXloQwDtkiIpiLjYXVNydw-PADcu2qd1SGBVxcBuwg1lwuZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b21de6065.mp4?token=q7Ygz2JGYxNjeZ1ZMptyf_uPFK1o3NJhF_09_RhN1LV58fr6YdVK4vZ48-HH8DauuIjGkGBO1kuHyEHGzatTFNPrNcBqSJhGLDPwBuz4RVPmy0qeHaFFyJvwSlOOGT5M7bHzCXpFUntxLp78O1eE8MrBATrJIOKz8JQJ9a-fiZ2az9F9nP40G8reigF8SYZETE0UlEwaKIpB8i9qHutnViDeSqAvFfOUzmU1loMitKWwL_rqWjGM2Dsw0KEInWxenRf_1UqMSv2UpSPHbQQE0MmGbqhBl78oduEmtcfXloQwDtkiIpiLjYXVNydw-PADcu2qd1SGBVxcBuwg1lwuZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدئو احمدی‌نژاد بعد از توافق
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/15097" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15096">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68844ebd5c.mp4?token=aJ8ocy78PrY1C4gIynhOmSXAOvpdwV06LXHQFTIwj2uVZGbA9mOfRVQDH2UcdGw_d4mwlIkuBiHxBjK1Aq3FkpJ-o4oUVIaI_W8k6hv5ROBj_TQU4LJWL4dtHSJC1cypmRo0PiF4vfXAyF-oLpzbV1lmcywc-HMVQDg12Inf0Yv23wtAVZ2tuYDcxL_Ns2WEYwp4-c6VWStrcOnt5IlNkRqpxFUBlq-UaGncTJe24KD9Qm0pM7TzhAykNY9taKZpfBe4rLPnzvWn8DmY9jVVVFQTo-zlixEasHYUpIYIwl9sFT3Sl74MrJQiajP8Wnlt0qBEQcW_GYdkn6rdqhZkWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68844ebd5c.mp4?token=aJ8ocy78PrY1C4gIynhOmSXAOvpdwV06LXHQFTIwj2uVZGbA9mOfRVQDH2UcdGw_d4mwlIkuBiHxBjK1Aq3FkpJ-o4oUVIaI_W8k6hv5ROBj_TQU4LJWL4dtHSJC1cypmRo0PiF4vfXAyF-oLpzbV1lmcywc-HMVQDg12Inf0Yv23wtAVZ2tuYDcxL_Ns2WEYwp4-c6VWStrcOnt5IlNkRqpxFUBlq-UaGncTJe24KD9Qm0pM7TzhAykNY9taKZpfBe4rLPnzvWn8DmY9jVVVFQTo-zlixEasHYUpIYIwl9sFT3Sl74MrJQiajP8Wnlt0qBEQcW_GYdkn6rdqhZkWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد اینهمه شب تو خیابون رفتن، آخرش بهت میگن اقلیتی تندرو
🤣
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/15096" target="_blank">📅 22:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15095">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا:
اسرائیل تو دو روز گذشته پس از اعلام پایان جنگ توسط رئیس ترامپ، 84 بار آتش بس تو جنوب لبنان رو نقض کرده و همچنان به جنایات و کشتار مردم لبنان ادامه میده.
هشدار میدیدم اگر اسرائیل به شرارت‌هاش ادامه بده، باید منتظر پاسخ سخت نیروهای مسلح جمهوری اسلامی ایران باشه.
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/15095" target="_blank">📅 22:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15094">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی: در صورت بدعهدی آمریکا، پاسخ  ایران، نظامی و کوبنده خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/15094" target="_blank">📅 22:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15093">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/15093" target="_blank">📅 22:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">12 بند توافق ایران و امریکا به گفته باراک راوید خبرنگار ‌آکسیوس :
-ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان. ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند.
-ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
-ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
-ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
-ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
-ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
-ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
-اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد.
-هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود. ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد.
-مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/15092" target="_blank">📅 21:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نفتالی بنت(نامزد نخست وزیری اسرائیل) در پخش زنده خطاب به جمهوری اسلامی: باور دارم به زودی یه دولت جدید در اسرائیل میاد و امیدوارم من رهبری اون دولت رو به دست بگیرم. از همینجا به رژیم ایران میگم؛ من قراره بدترین کابوس شما باشم، تاوقتی مردم ایران رو از دست شما…</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/15091" target="_blank">📅 21:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شبکه خبر: تمام کسایی که توی بیت رهبری بودن کشته شدن جز مجتبی خامنه‌ای @withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15090" target="_blank">📅 21:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15089">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شبکه خبر: تمام کسایی که توی بیت رهبری بودن کشته شدن جز مجتبی خامنه‌ای
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/15089" target="_blank">📅 21:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15088">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b67afa5b.mp4?token=S-RmhSrKi3fze6NnhzuM5An7alPKvSUDlKi60VI_0Rm4hyRXBfmJkDeQerjivTm9tr1ENjRXr57tBb0Sh8i40XAXIQjrkhSV4s3sOErz-lMVO_9Ht-1j27uM759PZsNq_bywYpA7VSa_f3hzE06rx6uMzpqspVHm8ZPfdg0DRdWY8iLT7vATjVxqrugz80NPm7N-LINt8M7o2Exm7PB9PaHQvbPuk0IcKJvKDGS1s9iz0h0U86F9X8pk-KPTewl7a_8EoZimW9ZnY8NzKIWpetvCBcCUCJLhXrCtOO4unv_Vlt9iKeuslErVm_JQo1vJn-YT5odO16yFbej-QmyvSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b67afa5b.mp4?token=S-RmhSrKi3fze6NnhzuM5An7alPKvSUDlKi60VI_0Rm4hyRXBfmJkDeQerjivTm9tr1ENjRXr57tBb0Sh8i40XAXIQjrkhSV4s3sOErz-lMVO_9Ht-1j27uM759PZsNq_bywYpA7VSa_f3hzE06rx6uMzpqspVHm8ZPfdg0DRdWY8iLT7vATjVxqrugz80NPm7N-LINt8M7o2Exm7PB9PaHQvbPuk0IcKJvKDGS1s9iz0h0U86F9X8pk-KPTewl7a_8EoZimW9ZnY8NzKIWpetvCBcCUCJLhXrCtOO4unv_Vlt9iKeuslErVm_JQo1vJn-YT5odO16yFbej-QmyvSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت(نامزد نخست وزیری اسرائیل) در پخش زنده خطاب به جمهوری اسلامی:
باور دارم به زودی یه دولت جدید در اسرائیل میاد و امیدوارم من رهبری اون دولت رو به دست بگیرم.
از همینجا به رژیم ایران میگم؛ من قراره بدترین کابوس شما باشم، تاوقتی مردم ایران رو از دست شما آزاد نکنم دست بردار نیستم.
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/15088" target="_blank">📅 21:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15087">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/15087" target="_blank">📅 21:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15086">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شبکه ۱۳ اسرائیل: امروز یه نشست اضطراری تو دفتر بنیامین نتانیاهو برگزار میشه تا بررسی کنن چطور میشه بین جبهه ایران و لبنان تفکیک ایجاد کرد و با این شاهکار ترامپ کنار اومد.
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/15086" target="_blank">📅 21:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15085">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/15085" target="_blank">📅 21:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15084">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">@withyashar
استادیوم</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/15084" target="_blank">📅 21:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15083">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMona</strong></div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/15083" target="_blank">📅 21:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15082">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">@withyashar
بی‌بی و ترامپ
mma رو  گفتم wwf</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/15082" target="_blank">📅 20:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15081">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=lhW8pJIb0ulV0qTgqlvaw_pjWulAb-SIDS7cM-v-OBkWqMwT-ujfDEgGkm0EeNLe2MyvcK-Q0fv4tp5UFynnl-62bNGmfNH-tcYZDyTCoCdO_cIQgmTvhmX_FRSrn0PWYi5ktv9d9rV6E-i7V-poYm5vsGr4qviGqAiijL1y0svRCRv2m0Htds00QG4rbsucIBUHzglmX3FotZ0S6E1Mj6SPEDYTXgyOthUBFcB2GHKBV7EkfosmNtnPv8ey4744pAc58fiAZhNj9fxE7TGPL_WGp6AIPpTQxeCIWsZs76eYhLlDJbb_xhn6m-2XGBsTaZThGzonX8wpme6qGfD-xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=lhW8pJIb0ulV0qTgqlvaw_pjWulAb-SIDS7cM-v-OBkWqMwT-ujfDEgGkm0EeNLe2MyvcK-Q0fv4tp5UFynnl-62bNGmfNH-tcYZDyTCoCdO_cIQgmTvhmX_FRSrn0PWYi5ktv9d9rV6E-i7V-poYm5vsGr4qviGqAiijL1y0svRCRv2m0Htds00QG4rbsucIBUHzglmX3FotZ0S6E1Mj6SPEDYTXgyOthUBFcB2GHKBV7EkfosmNtnPv8ey4744pAc58fiAZhNj9fxE7TGPL_WGp6AIPpTQxeCIWsZs76eYhLlDJbb_xhn6m-2XGBsTaZThGzonX8wpme6qGfD-xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/15081" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from자</strong></div>
<div class="tg-text">یاشار اخبار خیلی دارن میگن که شکاف به شدت زیاد شده بین بی بی و ترامپ
به نظرت زرگریه یا واقعا ترامپ پشت اسرائیل رو خالی کرده ؟</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/15080" target="_blank">📅 20:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شبکه ۱۲ اسرائیلی به نقل از یک منبع امنیتی:
کاهش محسوس در عملیات‌های ارتش اسرائیل در لبنان
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/15079" target="_blank">📅 20:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دلار ۱۵۲،۹۰۰
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15078" target="_blank">📅 20:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/15077" target="_blank">📅 19:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15076">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG_R5M2sIBIOBlA3z9_WM0ScgV8FvbgV359ypyO2wBfrf9MoLXc_fbaOLqZQW5bCT5faB4Lol1EUYmyYpdK2DKtQmIw1y1mkTByKmX12D1kmfy6OnTCeR1mbNPPe87fixKeuZXIJBJvHLyPaXeD-Rz76YMna4LqigEXWSlMlChgO4NYwVqII3qAmkUf_2_INXQM2IeP3JHEIG2SCoScCf68i9E8j9N7Qz5lG49fz-PusX1liYrc8a9Ny6gcQ7fBXxN6U7k8TtJqusOT7k5N1aZXKvjKzguDplUbo4zPW76WpAqe5WQS2lT6nDL8EiLYDCztHL83zt6Fg0nMo4VnGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقتصاددان سابق ترامپ می‌گوید توافق ایران به معنای رونق اقتصادی بزرگ برای ایالات متحده است
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15076" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15075">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRzjmfJill_fcYAnVsdNUy03n4BOD-3QmBsl_gfiWplTi_NnDz3BCpOpkH29FiC2tBxuVfjgq_oPv2ZzhyiJbaQBC49Fy2d5_ZEWg6SwtuYV4E37e7fzxBMn4_Adcwur-rr8JtxfsmHKc83G5ILXCpk1qyVCOmg4BB1XjYaXtL2l4FbErOcrqAz8hnzBREz25SV67vMdtCaxql3y6jvxmTmgi3jHbtcFj861PRxo9c9FMRiMTp31LrPXx5A9RyIY2kifp_yhnbVBtwZ6CzY6t4nAIgUXDbyzYlHUXlYLVR4JvMntE5oWoeTC78qcN23RraGZiayWD6gx5T7oOk2Jfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته ایلان ماسک ۱۶۵ میلیارد دلار سود کرد و ثروتش به ۱.۳ تریلیون دلار رسید
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/15075" target="_blank">📅 19:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15074">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نفتالی بنت، نخست وزیر سابق اسرائیل:
توافق فعلی بین جمهوری اسلامی و آمریکا فقط یک توافق موقته.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15074" target="_blank">📅 19:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15073">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ادعای وال استریت ژورنال: واشنگتن به تهران اجازه خواهد داد تا بلافاصله فروش نفت و سوخت را طبق توافق پایان جنگ آغاز کند
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/15073" target="_blank">📅 19:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15072">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دلار ۱۵۳،۵۰۰
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/15072" target="_blank">📅 19:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15071">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf74c8a754.mp4?token=CjyiizcoPeg5A-d_5mFA5PVaI9HDkRC7qzspJE-_qbNEBUbHtuR48g-JDdkI0EwnpiRGwQbmAFuaYNC3ftwUTzwKTKk2zTVfzoUWWFuClsbhGHl_CdRaTCZN0XoOMUH6cn3ciX7OwzpIzx1IdUbDuJ0UBFeJMQb5GCef5PRV_HA7s7-DS-k9JqE41ivxrWqsW5AVrUy02lwx7U6fpPIwRrHbyeQfwu1_6-BH5YP0b4_BbA3rm-n4V75uEzUFEBDXedhYDHm96q8ZU-DbPIeT4PuL3tWhqx8KRZqbuhZLecz1zANBxjTicmSs-b248Jlk1NKVLfFX7bvlyOykBBDdsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf74c8a754.mp4?token=CjyiizcoPeg5A-d_5mFA5PVaI9HDkRC7qzspJE-_qbNEBUbHtuR48g-JDdkI0EwnpiRGwQbmAFuaYNC3ftwUTzwKTKk2zTVfzoUWWFuClsbhGHl_CdRaTCZN0XoOMUH6cn3ciX7OwzpIzx1IdUbDuJ0UBFeJMQb5GCef5PRV_HA7s7-DS-k9JqE41ivxrWqsW5AVrUy02lwx7U6fpPIwRrHbyeQfwu1_6-BH5YP0b4_BbA3rm-n4V75uEzUFEBDXedhYDHm96q8ZU-DbPIeT4PuL3tWhqx8KRZqbuhZLecz1zANBxjTicmSs-b248Jlk1NKVLfFX7bvlyOykBBDdsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس فدرال آمریکا (FBI) در جشن تولد ترامپ، پهپادی که قصد ترور وی را در کاخ سفید داشت شناسایی و خنثی کرد!!
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/15071" target="_blank">📅 19:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15070">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرگزاری وابسته به سپاه:
اسرائیل آتش‌بس در لبنان را نقض کرد.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15070" target="_blank">📅 19:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15069">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618d127639.mp4?token=s-fGHqwQ--zBtn14UJX0MDGWheqw1BKkvUDpR4hxgWCNWnEQIb8NbNoxexTA1yBg9LhmWCe4qQsCI4Y378KNFop23NZ949zj_L0FR98GaTf8R0k4AmmI1O3lOBcp8GN_3VNMkNIAM9UjT_lwQzRxgsDREExBOeiLN98jAq9LOgmQtp7bbKr6I0vb6FQ4aY6Hwadwoo-iN5E1oPKGA6JymIggAC76kyT-xTJaOWcYIWNgzyd8gUvU0kToyEQk3y8JOwY2Ol7QJbXaRMhTNnj29Ogg9t-otseZz-NdQzoDUdReVfDl_6w46pI5Uy0EGCn579I0kgQ4DVel6kUmPRRLEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618d127639.mp4?token=s-fGHqwQ--zBtn14UJX0MDGWheqw1BKkvUDpR4hxgWCNWnEQIb8NbNoxexTA1yBg9LhmWCe4qQsCI4Y378KNFop23NZ949zj_L0FR98GaTf8R0k4AmmI1O3lOBcp8GN_3VNMkNIAM9UjT_lwQzRxgsDREExBOeiLN98jAq9LOgmQtp7bbKr6I0vb6FQ4aY6Hwadwoo-iN5E1oPKGA6JymIggAC76kyT-xTJaOWcYIWNgzyd8gUvU0kToyEQk3y8JOwY2Ol7QJbXaRMhTNnj29Ogg9t-otseZz-NdQzoDUdReVfDl_6w46pI5Uy0EGCn579I0kgQ4DVel6kUmPRRLEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند عرزشی هم صداش در اومد
@withyashar
اینو پیدا کنین استخدام کنم اتاق جنگ سبک منو داره میره
🤣</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/15069" target="_blank">📅 18:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15068">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5KN6sTzXfixU0qo5MwRMcILiKi_t7_M_XKHHr4B0KFLcZrijiKWMD6NOVVdgHCDj6KmGpV5y4ki11GEyKr4bLxsJ0g2XDi5wM4dpRAykyDpEgiRE4fNI3hg-BT7GmxrDT59uts10vco_Q8IsJUtCHYEuKZpimhX7RhHMhHb3xEuj7c-0u9kcEVeGwyBFxJFV_UPnokyPvgF-Y-gwZ-OjtKrTpEmQqqYS7luc6KFljEvGZ8x8n4JfVFi5RbAyaJF96mYM8b9uASvEV6k_xkL6BPmNIVvF70dP_X4nbYEpmz1nVZfijRnLGQKMVyGbp3gEyg_aUjAXzuboMiZdpwZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دراپ سایت: ایران برای تحلیل رفتار ترامپ، دوتا روانشناس به تیم مذاکره کننده اضافه کرده
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/15068" target="_blank">📅 18:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15067">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/15067" target="_blank">📅 18:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15066">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">صداوسیما : همین که اول بازی پرچم ایران توی خاک آمریکا به اهتزاز در اومد یعنی ما بردیم. دیگه نتیجه بازیا خیلی مهم نیست
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/15066" target="_blank">📅 18:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15065">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4feef4c4.mp4?token=n7X25D2nNHK5a6LhxLXVZlABK4nicJkfnyJ_yKsWY4a8gTlZEH7_y3KcWcj9oh-OfZN_dnwq-_OGVGm7ZoKNV3ZmX1NyMr1L7Er3-DN5MQYy5ZiTT1-6g13hdLeV6LxiRO1Dvyd4fg22SXdUeV1szEN_p-Rk-l9qunqE54k19R423UlF5yxHZZX_cCDAWFbJBnZTwieo4zBrxSJ5hXdZZ36I6apQUtZhFmzBxIAREHnqfXbrn58QqWHjCd73XLJq7MNXqAS7AJ_MQAWxUmw4nPNGWd8nNnsNUf71IubiZM7RFNZdWBFdwxVCLUPHyIkf7T8jACsSc7L6ISECd2JfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4feef4c4.mp4?token=n7X25D2nNHK5a6LhxLXVZlABK4nicJkfnyJ_yKsWY4a8gTlZEH7_y3KcWcj9oh-OfZN_dnwq-_OGVGm7ZoKNV3ZmX1NyMr1L7Er3-DN5MQYy5ZiTT1-6g13hdLeV6LxiRO1Dvyd4fg22SXdUeV1szEN_p-Rk-l9qunqE54k19R423UlF5yxHZZX_cCDAWFbJBnZTwieo4zBrxSJ5hXdZZ36I6apQUtZhFmzBxIAREHnqfXbrn58QqWHjCd73XLJq7MNXqAS7AJ_MQAWxUmw4nPNGWd8nNnsNUf71IubiZM7RFNZdWBFdwxVCLUPHyIkf7T8jACsSc7L6ISECd2JfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند.
اگر این کار را بکنند، عالی است. اگر نکنند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/15065" target="_blank">📅 18:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15064">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ونس به فاکس نیوز:
ما پیروز شدیم، چه ایران روش خود را تغییر دهد و چه تصمیم بگیرد به توافق پایبند نباشد
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/15064" target="_blank">📅 18:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15063">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانال 12 اسرائیل: اسرائیل درخواست دیدن یادداشت تفاهم بین آمریکا و ایران رو داشت اما این درخواست رد شد.
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/15063" target="_blank">📅 17:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15062">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ: ممکنه یه کنفرانس خبری برگزار کنم و متن یادداشت تفاهم آمریکا و ایران رو با صدای بلند و کلمه به کلمه بخونم تا رسانه‌ها اونو به درستی پوشش بدن.
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/15062" target="_blank">📅 17:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15061">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ: اگه لیندسی گراهام بیاد و به این توافق با ایران شک کنه و حرفی بزنه، واقعاً براش دردسر درست می‌شه و حسابی به مشکل می‌خوره.
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/15061" target="_blank">📅 16:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15060">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آکسیوس: جان رتکلیف، مدیر سیا، به دونالد ترامپ و مقام‌های ارشد آمریکا گفته ارزیابی‌های اطلاعاتی نشان می‌ده ایران احتمالا تمایل واقعی به اجرای تعهدات هسته‌ای خودش نداره.
گفته می‌شه تفاوت میان حرف‌های داخلی مقام‌های ایرانی و آنچه به مذاکره‌کنندگان آمریکایی گفتن، باعث این نگرانی شده.
مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر دفاع آمریکا، هم نگرانی مشابهی دارن.
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/15060" target="_blank">📅 15:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15059">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، سه‌شنبه 26 خرداد از اجرای حکم اعدام جواد زمانی و ابوالفضل ساعدی، دو زندانی سیاسی بازداشت‌شده در اعتراضات دی‌ماه در استان سمنان خبر داد. میزان اتهام آن‌ها را «افساد فی‌الارض از طریق کشیدن سلاح گرم و سرد در شهرستان…</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/15059" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15058">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6041510c69.mp4?token=qFwpkQP5AStVxHgEhu9WnCWQs6CEfXZsiHTro8WfwDhCxMuCswIQYEqFhodTDd0kguAaoOpaIhLe9lrPPLU01BOOM9Qq3SEFFfoaP0DseOCvrE-ZIPJAeyxP7wjye9kzUAuOztRPE_pWGdBZiWRcKHVJNDY7s6sconI4L0sHZovzu1ToSI11aVosFMQEitDVy9XCDIktNgwdadzomnY8anEK7Cz3kL2vEgh9fIw6d6d50mG_oyW0Q6mn-6eb1wTOIRiqPO2sHqSNSiPa-vYD4st78oBLnKKn6W7TwMY8ZhwP9RNK9GSEKndv3Oxl4z2fU6kLMydNNMeJqMTj9wqY2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6041510c69.mp4?token=qFwpkQP5AStVxHgEhu9WnCWQs6CEfXZsiHTro8WfwDhCxMuCswIQYEqFhodTDd0kguAaoOpaIhLe9lrPPLU01BOOM9Qq3SEFFfoaP0DseOCvrE-ZIPJAeyxP7wjye9kzUAuOztRPE_pWGdBZiWRcKHVJNDY7s6sconI4L0sHZovzu1ToSI11aVosFMQEitDVy9XCDIktNgwdadzomnY8anEK7Cz3kL2vEgh9fIw6d6d50mG_oyW0Q6mn-6eb1wTOIRiqPO2sHqSNSiPa-vYD4st78oBLnKKn6W7TwMY8ZhwP9RNK9GSEKndv3Oxl4z2fU6kLMydNNMeJqMTj9wqY2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با پراید رفته دم لانچر در حال شلیک
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/15058" target="_blank">📅 15:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15057">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرگزاری دولتی ایسنا:
محاصره دریایی آمریکا در حال لغو شدن است
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/15057" target="_blank">📅 15:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15056">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/563a3a2554.mp4?token=eKid2TDPfdV6IIMROCuvCa69WmJsdFAah2lspDju8hRSjpUb9o-X7j01v91pMLePOp0x06fUfibPDiBsCvRRsmxcHcDxucB2yqtuG3S7TlswU5q1vWxQUF2cm16P07N9QRS2Za5qyBCfoiUL22d6gBBWEfNA-GlIB2jQvVjTcGIO-tgLCB7sp4ve51w-F3lG5M5V-1oz6ZWOJP1BoNJkQ1nBhRwgJT0XdwtzpbunGATvfui5jdj_eaaD1tVXW-WGwdafJF9elImu6IfP_HOMG62r81SG4tu_N7Lf8QiMoKksQ2Bm5Yw45O1HnpzNy1TxdhGH25woENVQeKQ74IynEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/563a3a2554.mp4?token=eKid2TDPfdV6IIMROCuvCa69WmJsdFAah2lspDju8hRSjpUb9o-X7j01v91pMLePOp0x06fUfibPDiBsCvRRsmxcHcDxucB2yqtuG3S7TlswU5q1vWxQUF2cm16P07N9QRS2Za5qyBCfoiUL22d6gBBWEfNA-GlIB2jQvVjTcGIO-tgLCB7sp4ve51w-F3lG5M5V-1oz6ZWOJP1BoNJkQ1nBhRwgJT0XdwtzpbunGATvfui5jdj_eaaD1tVXW-WGwdafJF9elImu6IfP_HOMG62r81SG4tu_N7Lf8QiMoKksQ2Bm5Yw45O1HnpzNy1TxdhGH25woENVQeKQ74IynEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران حتی یک بار به ترکیه حمله کرد، من هرگز این را درک نکردم، هیچ‌کس آن را درک نخواهد کرد
این مشکل است، آن‌ها کاملاً غیرمنطقی هستند و اکنون آن افراد رفته‌اند، فکر می‌کنم ایران اکنون رهبری منطقی دارد!
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/15056" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15055">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش روزنامه New York Post می‌گوید که پلیس فدرال آمریکا (FBI) پنج نفر را به اتهام طراحی یک حمله به رویداد «UFC Freedom 250» در روز تولد ترامپ که در محوطه چمن جنوبی کاخ سفید برگزار شد، بازداشت کرده است. گفته می‌شود این طرح شامل استفاده از پهپادهای انفجاری، تک‌تیراندازها و همچنین تلاش برای نفوذ و شکستن دروازه‌های محل بوده است.
بر اساس این گزارش، FBI در تاریخ ۱۰ ژوئن از وجود این توطئه مطلع شده و سپس طی یک عملیات چندایالتی اقدام به بازداشت افراد کرده است. مقام‌ها می‌گویند در جریان تحقیقات، چت‌های رمزگذاری‌شده در اپلیکیشن Signal کشف شده که بیش از ۲۰ کاربر در آن‌ها حضور داشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/15055" target="_blank">📅 15:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15054">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf2f513ca.mp4?token=ENpq-UyJAAfdQ1tHCli-qnPQr_V1xuJzmV3s2bTqqroPfcQyiRilUVyv8N9Lh3BwLciefsrxsUvoYoe5yR0zeDRtlmBL976Vo6cEl_theSywYMYUjvNfadNjsFZ2ZYC8734100yqXh3eiVTiI17svjTp4ZT2iDZ6dGwufN3WtTE8G94wg9z2Ryjd8l5nWk-hBM8Xp3hYUOFIwVzmNGrhsCANRC59dw91GPVk1wrMX86c1wb123gSIh66FluytJXyDiLQDB1Wnet_LhQ_oENe93CALcySM8bHYb4cpsmf22e1bBGchoJXHs8XSiq4Ltpglb0O1BnipQzvbEz8KAOpPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf2f513ca.mp4?token=ENpq-UyJAAfdQ1tHCli-qnPQr_V1xuJzmV3s2bTqqroPfcQyiRilUVyv8N9Lh3BwLciefsrxsUvoYoe5yR0zeDRtlmBL976Vo6cEl_theSywYMYUjvNfadNjsFZ2ZYC8734100yqXh3eiVTiI17svjTp4ZT2iDZ6dGwufN3WtTE8G94wg9z2Ryjd8l5nWk-hBM8Xp3hYUOFIwVzmNGrhsCANRC59dw91GPVk1wrMX86c1wb123gSIh66FluytJXyDiLQDB1Wnet_LhQ_oENe93CALcySM8bHYb4cpsmf22e1bBGchoJXHs8XSiq4Ltpglb0O1BnipQzvbEz8KAOpPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدراعظم آلمان در جی۷ پیراهن «ترامپ ۴۷» را به رئیس‌جمهور آمریکا اهدا کرد
@withyashar
خانواده دونالد ترامپ ریشه آلمانی دارند. پدربزرگ او، فریدریش ترامپ، در شهر کالشتات آلمان به دنیا آمد. او در سال ۱۸۸۵ و در شانزده سالگی از آلمان به ایالات متحده آمریکا مهاجرت کرد. پدر ترامپ، فرد ترامپ، در آمریکا متولد شده بود و شهروند آمریکا محسوب می‌شد، اما از طرف پدری کاملاً تبار آلمانی داشت. از سوی مادر نیز ترامپ ریشه اسکاتلندی دارد. مادرش، مری آن مک‌لئود ترامپ، در جزیره لوئیس در اسکاتلند به دنیا آمد و بعدها به آمریکا مهاجرت کرد</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/15054" target="_blank">📅 15:05 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
