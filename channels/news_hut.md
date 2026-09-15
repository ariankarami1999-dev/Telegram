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
<img src="https://cdn4.telesco.pe/file/R5Ywu0DohZXruQ0yJzGH9O4PAuy9CIvbhT3YBBvSfE2_fsCg-y9CUt53rVbP6LKvptjdAZAnMfIB3aQr4r1emi59zIW-MhztpHfUyxe6s8wEtElw8SJG-7JKAZo_fWzVkDa-gzmdwnoWYNoi0kC51Pm8wit_XlcffCcWsy7P7X6hCPRKCd4d8RkAQpom2rn5m518q30l_AC8ghqMQjvasECczkvCuS4iO-F6HAfGJKER3qGr08MwM32Hb1HGzTDid2z6dWWIsKYm6flHbcnf-YAQJ67SInMI2UfrxsGIHyyck4c4M1d0_YSzTIvVhRIcFct42HbbV1sUVc8HMujfpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 107K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 02:03:36</div>
<hr>

<div class="tg-post" id="msg-71702">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 617 · <a href="https://t.me/news_hut/71702" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71701">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF74KEl991UPZ95IRQWdVu2IMDfEzbcjnN_PKPEGvy53R1SQBpmJKuxNE0UYkw3_pmQblTCfF0jvfN9RhSZ6Rog2acAULED3-oYdkrxIjiCjvBvPUFS5-deBPRi9zsG_mDaBWxiFFodcKlnnQcDI30I-WyLrxnKgJiV5vcpYMUTV8tS2HrblkYsadKGvBNoZznzpPa3fV7rl6YY05Lt6BD3OfwMGWygnYZVSANJSWGA7oR2ZzXOvi4PcUioN0HZ7Y5kL9DVV0t_BEbFjAx8FLM_DaFkap0JMglTkfifGRHgc6W7wAc_7eDaw5-QLh7KVIKbryAA-38JhnuqcoUp_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 677 · <a href="https://t.me/news_hut/71701" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71700">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم  @News_Hut</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/news_hut/71700" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71699">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/news_hut/71699" target="_blank">📅 01:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71698">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGBhlm2p60MqAlMw6ctkBKrw8XsGpp6MnwQEJwsWT_xAT19NqURRg2IPwDPqZmsGr-0bYbbJ69LuE38OTQw3_zOcJmSf2HoRbsFfl6metcZEakMDMpiL7A0Y1u_HQebAAD4-2IXKR13xjziBgePC1cIrcC8U9dqafkUoQJnDfN6lk6K-rH7Ok0hnCxNDC0GwkQV-AmIyk5CDerDf_-VumcDXFKwntXqE8E2V4xHA1ztmNcOahXblduB4q0Sqyqd6i9k6298n7MqJZmTGvAQAcBhbsKLKarJ1W-se8cVEae-jfyS4rwFI9Bb_zNClyOy0_dbRAySjCehe6lntePGmcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آلمان (DPA) مدعی است که حوثی‌های یمن اکنون در تنگه باب‌المندب مین‌های دریایی کار گذاشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/news_hut/71698" target="_blank">📅 01:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71697">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=FVd1WAAyb2LyFI0SxKqM9bXiEQMSgbVeMshnVaXmKyHXYr_0MVbA8A3u7Y9PfVGtR8cvNeNwyqpXhpOMDXt5JIdgxcZU8fhLSwc1Btrp3pC7L-TAwHeBhexsjGPUexPoxu9jjESS6pFpi8w_VP_0YTXFLc7eq-TtIui6a-GVJ7jkmwwFxUYq2w8PgIahbBAguCbJhT7cFIp7tS6PwLVlCTMAvKD5nqaIg-FwzI4FUuq5MV_bp__iLKWM68SZy7ZRNYB2icoa-aMbn7a2fXR3ktvJCLutr7HurATWT4UBCiKEQvpuPuyRD-r4h2QPt05eHprod8M-Tj9HPIIXkjKu2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=FVd1WAAyb2LyFI0SxKqM9bXiEQMSgbVeMshnVaXmKyHXYr_0MVbA8A3u7Y9PfVGtR8cvNeNwyqpXhpOMDXt5JIdgxcZU8fhLSwc1Btrp3pC7L-TAwHeBhexsjGPUexPoxu9jjESS6pFpi8w_VP_0YTXFLc7eq-TtIui6a-GVJ7jkmwwFxUYq2w8PgIahbBAguCbJhT7cFIp7tS6PwLVlCTMAvKD5nqaIg-FwzI4FUuq5MV_bp__iLKWM68SZy7ZRNYB2icoa-aMbn7a2fXR3ktvJCLutr7HurATWT4UBCiKEQvpuPuyRD-r4h2QPt05eHprod8M-Tj9HPIIXkjKu2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا به‌تازگی طرح استیضاح دونالد ترامپ را که توسط «اَل گرین» (نماینده دموکرات از تگزاس) ارائه شده بود، با رأی قاطع و سنگین ۲۳۲ به ۱۴۷ رد کرد.
بخش بزرگی از دموکرات‌های مجلس به این طرحِ پوچ و بی‌معنی رأی منفی دادند، چرا که اَل گرین خودسرانه عمل کرده بود و آن‌ها می‌دانستند که این قطعنامه به جایی نخواهد رسید
@News_Hut</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/news_hut/71697" target="_blank">📅 01:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71696">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ونس امشب گفت که تو ماه‌های آینده، جنگ وارد مراحل جدیدی می‌شه؛
اما در شرایط فعلی همه‌ی تحلیلگرهای نظامی معتقدند که بخاطر انتخابات میان‌دوره‌ای، جنگی گسترده از آمریکا نمی‌بینم.
اما یه نکته‌ای اینجا وجود داره، انتخابات سنا و مجلس نمایندگان آمریکا  نوامبر ۲۰۲۶ (۱۲ آبان) برگزار می‌شه ولی نمایندگان انتخابی، با ۶۱ روز فاصله به سر کار میان، یعنی از ۱۲ آبان ۱۴۰۵ تا ۱۳ دی ۱۴۰۵، سنا و مجلس نمایندگان با همون اعضای قبلی ادامه می‌دن و می‌تونن قانون تصویب کنند؛ بنابراین از لحاظ تئوری، بهترین زمان برای حملات دوباره‌ی آمریکا همین دو ماهه (در صورتی که دموکرات ها پیروز بشن)
ولی یادمون نره که ترامپ یکی از غیرقابل پیش‌بینی ترین سیاستمدار های دنیاست
#hjAly‌</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/news_hut/71696" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71695">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM9onFjRvK1ID4z9x1dG6EoXtRvqKlDSai6jKDYEOLvI141lZrmSesUWXR4lTjyQ5Gg7Z5Xu6VFiiQXQZIuhXntd-f1cmgeu_8ZEafeXZRFHlvvViCdPWlMH_pm-kYLLZIJqyoE2qv385EB7xMDRFf6GsE5a-MDKNyzda95yL7xhj6fqS3gxir_m0KLd2IsuCD8xKbMyAV6K6D6TGlwOonsvvFBhqzcZV30BAmtUk67f7y1KUvvYoywDfYnRwKdcFAUL6WxN7Ln9IzFAqJIm82oM-PZjhBgQ_jhvXOCzV0fQ4t6fBH2D3EHmKB0oyJyC3zSB66KTvBIssRFKxohPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلیا هاشمی:  امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت. مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/71695" target="_blank">📅 00:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71694">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ایلیا هاشمی:
امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت.
مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین لحظه لغو شد؟ یا مسئله‌ای دیگر…
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/71694" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71693">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=JcAXVaAzQIowGZrLan9ha8Q0TMot1QPpdd_8IT1Ckwl5ZvPK0hpYQf7VZEgc3M_NHwjbZK5QkfSl-FdYlarCmxNnuT1zVr2XYAUqsfKjz2m4fh0cDSsNp9oTaack5ANSqtrtEnDuBtCVgrQAU3W7lAWF5YE8HndCFtnTpO7_Wov6BC3Z0fdl0iE7bM4wXz0cIm9mKy4N8C2a20ElTW02_zs-qhpIwBAOzP80ssBhTF1r_iMQ_x5Iyv2ofu7PeHgQjjNXTq-gFszIstK70yaenX5txDpsxHkpDMVI3nhau6q_mKVGKFcDpjXMpIaKk_c7k45hxG8YlyksRJSyav8HyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=JcAXVaAzQIowGZrLan9ha8Q0TMot1QPpdd_8IT1Ckwl5ZvPK0hpYQf7VZEgc3M_NHwjbZK5QkfSl-FdYlarCmxNnuT1zVr2XYAUqsfKjz2m4fh0cDSsNp9oTaack5ANSqtrtEnDuBtCVgrQAU3W7lAWF5YE8HndCFtnTpO7_Wov6BC3Z0fdl0iE7bM4wXz0cIm9mKy4N8C2a20ElTW02_zs-qhpIwBAOzP80ssBhTF1r_iMQ_x5Iyv2ofu7PeHgQjjNXTq-gFszIstK70yaenX5txDpsxHkpDMVI3nhau6q_mKVGKFcDpjXMpIaKk_c7k45hxG8YlyksRJSyav8HyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سریع‌القلم:
آمریکایی‌ها بعد از انتخابات کنگره به سراغ عملیات نظامی علیه ایران می‌آیند چه دموکرات ها پیروز شوند چه جمهوری خواهان!
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/71693" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71692">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/71692" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71691">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/71691" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71690">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=kyHWkgB1BqkKfs1IbGL7nSIaU0FqiQzmZwXxdZplGpYx5v3g9yj-H-9KjF3FFeoRAnBDxEIqfLOED46n4jTbqSan9AXN4Gj3fUyobDKRFO1EqiURMinqd1kYqjei4wAGjRNIIxTnQRG8nQCsi-ru-xYcwUyq1xNqHR5lJkA9gqaPeRtBdWPoLnogcYkpOAmDPN-_7fPsQL3PDwpyMVoxVl1Nvy008azY3dujo8bPeBXrhqwyDu_0a81pJ6zQzSiudZ83y7HGxsHvmMvgPSVnE7pf46ZKSN8YfM0PUczAS7ZMF_gHDbp_Y_eBnI196DZ3kehaxb5MBR1P8Hih9P9q8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=kyHWkgB1BqkKfs1IbGL7nSIaU0FqiQzmZwXxdZplGpYx5v3g9yj-H-9KjF3FFeoRAnBDxEIqfLOED46n4jTbqSan9AXN4Gj3fUyobDKRFO1EqiURMinqd1kYqjei4wAGjRNIIxTnQRG8nQCsi-ru-xYcwUyq1xNqHR5lJkA9gqaPeRtBdWPoLnogcYkpOAmDPN-_7fPsQL3PDwpyMVoxVl1Nvy008azY3dujo8bPeBXrhqwyDu_0a81pJ6zQzSiudZ83y7HGxsHvmMvgPSVnE7pf46ZKSN8YfM0PUczAS7ZMF_gHDbp_Y_eBnI196DZ3kehaxb5MBR1P8Hih9P9q8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای جنجالی یه
جنده
: دختری که ادعا می‌کنه باکره‌اس، دقیقا به چی افتخار می‌کنه؟
تو قطعا ایراد داری، مگه میشه یه نفر با کسی رابطه نداشته باشه؟ آقایون حتی توی سوراخ موش هم فرو میکنن، اونوقت تورو نکردن!؟
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71690" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71689">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=DxzIw9wcFfUSjCn-FKljniA1a_wxDTeKprcD1cVRqrs6JXTyBRXzaP3ug3XHO-yZQQCNJshoyukRqhQDkb8p3vmRpRAsbepSYTLUXxcy11w4SnXZgUJ7zSVw98Q8JYDw98zRiw_WmJhBCC7H1rAD9ah-S9tnw6tE0BHWv0GDDPW8NAGJ7yzfCHPAIqI84TBtUGHNMOOkOioh_5Tk9JwWGofEE2Vs77eSj5OJTYG-Gf_qA37qNSdustnXBrFe8WRhJFt8BBUtEoz-8bO4_gaUccq-iiFVH2SujlXA8lXuU0eUmmADkoCzRYHnYv_fh6xT96dpkFmgzNnbS3Svkphozw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=DxzIw9wcFfUSjCn-FKljniA1a_wxDTeKprcD1cVRqrs6JXTyBRXzaP3ug3XHO-yZQQCNJshoyukRqhQDkb8p3vmRpRAsbepSYTLUXxcy11w4SnXZgUJ7zSVw98Q8JYDw98zRiw_WmJhBCC7H1rAD9ah-S9tnw6tE0BHWv0GDDPW8NAGJ7yzfCHPAIqI84TBtUGHNMOOkOioh_5Tk9JwWGofEE2Vs77eSj5OJTYG-Gf_qA37qNSdustnXBrFe8WRhJFt8BBUtEoz-8bO4_gaUccq-iiFVH2SujlXA8lXuU0eUmmADkoCzRYHnYv_fh6xT96dpkFmgzNnbS3Svkphozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی ایران یه تور راه اندازی شده به اسم «هیلینگ آب دریا» ، این شکلیه که میرین کنار ساحل و تا جایی که میتونین باید گریه کنین.
برای شرکت در این تور هم میلیونی باید پول بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71689" target="_blank">📅 22:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71688">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان با انتشار بیانیه‌ای مشترک، برای(فردا) روز چهارشنبه ۲۵ شهریور ۱۴۰۵ (۱۶ سپتامبر ۲۰۲۶) فراخوان اعتصاب عمومی صادر کرده است. این فراخوان هم‌زمان با چهارمین سالگرد ژینا (مهسا) امینی و آغاز اعتراضات «زن، زندگی، آزادی» اعلام شده است.
در این بیانیه از بازاریان، اصناف، کارگران و دیگر اقشار جامعه خواسته شده است با تعطیلی مغازه‌ها و بازارها و خودداری از حضور در محل کار، در این اعتصاب مشارکت کنند. صادرکنندگان فراخوان، وضعیت اقتصادی، فقر، گرانی، بیکاری و همچنین آنچه تشدید فشارهای امنیتی و صدور احکام سنگین می‌دانند را از دلایل این اقدام عنوان کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71688" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71687">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265561794f.mp4?token=kGE5ckojkGscB4XWsPw-FpY_u_6lMor6-BmqWF6E9utAoaKvLd6HY2ho4EwZv3Sea8tpcizDtV09-jgcKgabgJv6YLKahiQXYzGBJy8RfJGkVghfSl9IiszlXjcyuAbpXenszkZTGuBb_-wlhzMHuef7m9kI0vqV0kQ8S4okV7Sldym7Q8bqAsMYqos_KvXJdJPymFmGT6hnaHMY5-H4W6XKbUAJXEE7Rs49AmbaS3Nj08ownaIg9zNZ7Jl2V_y9711bVcFkHwHUJXEHDjp0tW2fS676L5f55fyFnzVId1S2scvVJ9KeoaEA3eyYBpx_JRtwF1K9Iysh8DraMZ-Thw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265561794f.mp4?token=kGE5ckojkGscB4XWsPw-FpY_u_6lMor6-BmqWF6E9utAoaKvLd6HY2ho4EwZv3Sea8tpcizDtV09-jgcKgabgJv6YLKahiQXYzGBJy8RfJGkVghfSl9IiszlXjcyuAbpXenszkZTGuBb_-wlhzMHuef7m9kI0vqV0kQ8S4okV7Sldym7Q8bqAsMYqos_KvXJdJPymFmGT6hnaHMY5-H4W6XKbUAJXEE7Rs49AmbaS3Nj08ownaIg9zNZ7Jl2V_y9711bVcFkHwHUJXEHDjp0tW2fS676L5f55fyFnzVId1S2scvVJ9KeoaEA3eyYBpx_JRtwF1K9Iysh8DraMZ-Thw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی سخنگوی دولت :
امیدواریم نیازی به تغییر سهمیه‌های اول و دوم بنزین نداشته باشیم؛ ولی اگه بخواهیم گرون یا کمش کنیم حتما شما مردم را در جریان خواهیم گذاشت و بدون اطلاع‌رسانی کاری نمیکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71687" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71686">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شنیده شدن صدای دو انفجار از سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71686" target="_blank">📅 21:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71685">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/61894edf33.mp4?token=A1J2p_XF-SJeyqNFFHXZ5B_WMrVqrzp7OcGHkA8N3thuk6e3-KnQytW9KzHKp6JsR9f2NzqA05AgawmUkJnzxZ-uVcWuwQxfkkjfV32MIN2_IsCs-EOqdBh5rvgxWBtQelhU9qc8SMDwV8Ot25hsASsi61C8k76vi3mmmzxomEVxBaUahIg3UMxmdGDUoF2E-4tQvlnu2S6RYwBgpeOwUhMOkaBNhVp_Pg74a8D8e7JAc1KqgEoWaJURysNkw9sEiHjEaNyDxtg5WcrhMLZH2Ff-0GpNYHuDsly-HcOIbmhyQG-46UhpmEvVSgYOsmlnhtDQPpCHQyn9qceTi1yOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/61894edf33.mp4?token=A1J2p_XF-SJeyqNFFHXZ5B_WMrVqrzp7OcGHkA8N3thuk6e3-KnQytW9KzHKp6JsR9f2NzqA05AgawmUkJnzxZ-uVcWuwQxfkkjfV32MIN2_IsCs-EOqdBh5rvgxWBtQelhU9qc8SMDwV8Ot25hsASsi61C8k76vi3mmmzxomEVxBaUahIg3UMxmdGDUoF2E-4tQvlnu2S6RYwBgpeOwUhMOkaBNhVp_Pg74a8D8e7JAc1KqgEoWaJURysNkw9sEiHjEaNyDxtg5WcrhMLZH2Ff-0GpNYHuDsly-HcOIbmhyQG-46UhpmEvVSgYOsmlnhtDQPpCHQyn9qceTi1yOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، هواپیمای تهاجمی A-10C Thunderbolt II نیروی هوایی ایالات متحده، مواضع داعش را در نزدیکی «جبل‌العمور» در شرق استان حمص (مرکز سوریه) هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71685" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71684">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1QdwUeNvTTaRd3l3W-AxIG5ONgTFoAAR_xEPvclStGG6YgNdKClYSJ8-xJqNLF8e4hvfPKIB2ZEHrzxYeJnFuhYxH9LX4Mu9o4TPxDe9qbxpW2LpAjkUyAH_8rcWnygumXkttijTPA_D5s-7Xjy-lrXgCYnP3dWownPIYOPuZqPKxLiQ5GVEeCvws40JjfjH7TRry8dIsZMijmBMQJKggPtYrJcB6epoha0YKTLcLCC5nEsiU6UI0gRcbB8nHIyK-OsohJaPhytGDDonrm37beHT59l1vkJd6r6TA-t1tz4VuiwBirr_9dieGknVXNg0lgwm9PYNL2hWomvCw2t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن پست:
دولت ترامپ در حال تدارک فروش ۴۰ هزار بمب سنگین (از انواع MK-84 و BLU-117 با وزن ۲۰۰۰ پوند) به ارزش ۲.۸ میلیارد دلار به اسرائیل است؛ این بزرگترین معامله تسلیحاتی از این دست در سال‌های اخیر محسوب می‌شود که هزینه آن از محل پول مالیات‌دهندگان آمریکایی تأمین می‌گردد.
این‌ها همان بمب‌هایی هستند که بایدن پیش‌تر به دلیل نگرانی‌ از تلفات غیرنظامیان، ارسال آن‌ها را به‌طور موقت متوقف کرده بود.
این قرارداد برای تصویب به کنگره ارجاع می‌شود و می‌تواند آزمونی برای دموکرات‌ها باشد؛ چرا که در ماه ژوئیه، بیش از ۱۰۰ نماینده دموکرات مجلس نمایندگان به کاهش کمک‌ها به اسرائیل رأی داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71684" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71683">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=YWVDJPkUdkbI1-FNut-9vghZJYcvmIyhgFX3sv8gJFhnnvAwUP9KYKqsQrfMZzFoErVyHTu1oPsH3WHncyktcyp3AnRm5OehlxLTZ2dZwpH8fcwsTbuBCqii-nTdOkn4kj5cxCQfCfCVVWA2_fNV546oQGS1y4w3j9SKjn7R1AkVe-HSr5WToetLedE2ARanfdkDAGheuuz4cm5heW3jFhBNI98kz--c1NNQkoaVqWazuh5KfPwGnTSjVTQl8ouLG_nHZuSgWCL4bksg5S_NnLB-qOl-Hor2F4ziCokF8DYarONutkGRzm2jLJxcLQyksKzurNDn7lNZuPcxntwBBYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=YWVDJPkUdkbI1-FNut-9vghZJYcvmIyhgFX3sv8gJFhnnvAwUP9KYKqsQrfMZzFoErVyHTu1oPsH3WHncyktcyp3AnRm5OehlxLTZ2dZwpH8fcwsTbuBCqii-nTdOkn4kj5cxCQfCfCVVWA2_fNV546oQGS1y4w3j9SKjn7R1AkVe-HSr5WToetLedE2ARanfdkDAGheuuz4cm5heW3jFhBNI98kz--c1NNQkoaVqWazuh5KfPwGnTSjVTQl8ouLG_nHZuSgWCL4bksg5S_NnLB-qOl-Hor2F4ziCokF8DYarONutkGRzm2jLJxcLQyksKzurNDn7lNZuPcxntwBBYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از نفتکش «ال‌گایا» (EL GAIA) پس از اصابت به آن در بخش جنوبی تنگه هرمز منتشر کرد.
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که ایران ماه گذشته با موشک و در پایان هفته جاری نیز با پهپاد به این نفتکش حمله کرده است؛
در مقابل، ایران مدعی است که این شناور پس از ورود به «منطقه ممنوعه» در بخش جنوبی تنگه، با یک مین دریایی برخورد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71683" target="_blank">📅 20:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71682">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbKAAWY07A0k3HPbI7Ge3exU-lxhjPjeUeqPv8SskLIR4oZVw4bK3qswcHXzufopv6DxOZuy7vBTUBHRaBlZ6LbtjQORVqyurUD-DOOzoGzVEdVNZUGYkyzNFov2R05XMILqk8t8lEFMAWpVjkvLnM9VDzPUgXIguX9upRoa1lOmG3y9FU2P1IMXfuNd8caJjtQS4uRFwbwXUCweCRFtmsJvC8s46j66RZA0UDwBLd57IXHnnWIqe8qCeDHplFjj9glORTUeDzmX17IijD2lsSXTllfeb12_F-d4-Q6_mvdewOY0pqIlW6a8JgbukN3txVBI5Fwk75eHVOk-e7Jg5lIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbKAAWY07A0k3HPbI7Ge3exU-lxhjPjeUeqPv8SskLIR4oZVw4bK3qswcHXzufopv6DxOZuy7vBTUBHRaBlZ6LbtjQORVqyurUD-DOOzoGzVEdVNZUGYkyzNFov2R05XMILqk8t8lEFMAWpVjkvLnM9VDzPUgXIguX9upRoa1lOmG3y9FU2P1IMXfuNd8caJjtQS4uRFwbwXUCweCRFtmsJvC8s46j66RZA0UDwBLd57IXHnnWIqe8qCeDHplFjj9glORTUeDzmX17IijD2lsSXTllfeb12_F-d4-Q6_mvdewOY0pqIlW6a8JgbukN3txVBI5Fwk75eHVOk-e7Jg5lIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
تنها کافی است به سخنان رئیس‌جمهور، رئیس مجلس و رئیس بانک مرکزی ایران اشاره کنم که اذعان داشته‌اند اقتصاد کشور در وضعیتی بسیار وخیم و بحرانی قرار دارد؛ هشداری که خطاب به هم‌قطاران تندروی آن‌ها در سپاه پاسداران و همچنین مردم ایران بیان شده است.
ما شاهد سقوط ارزش پول ملی و تورم سرسام‌آور بوده‌ایم؛
و در کمال ناباوری، کشوری که سومین ذخایر بزرگ انرژی جهان را در اختیار دارد، اکنون با قطعی برق سه تا چهار ساعته مواجه است.
این وضعیت اسفبار اقتصادی ناشی از تحریم‌هاست؛ ترکیبی از تحریم‌ها و اقداماتی که ما طی ماه‌های گذشته برای شناسایی و مسدودسازی مسیرهای مالی و سیستم‌های پرداخت آن‌ها انجام داده‌ایم و در حال اعمال فشار شدید بر آن‌ها هستیم.
به باور من، واکنش‌های تند و خشونت‌آمیزی که اکنون از سوی آن‌ها شاهد هستیم، درست مانند رفتار حیوانی زخمی است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71682" target="_blank">📅 19:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71681">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=ekkFnccnzeMli2rfOysqx3Zva1OoJCiqNFhaldWO8ioEi6FURRzBZN7b3-cV8lwgr1cwUw_VKTTEpliermRjfyNzV_stlZlpLaNGAD-rzMp8kOHrjWQF-HGGOIEfR_g57bNgFmmUY-EQGDgC89-7MReOXvptp2wx_qzV0YEC1-XQ7nqSej-P5rwZSsstJL823BRVqKdwowDI6HUtLz3Pg8-mr-s67ZPQv9TCEjKl-VofHGQdSgJtDw0oFWYlAm1zsMZYA5vypKyp2a7VwKEV3KybW_1Yi-hKUTsY4MA1-iM0IfgOjhMhPoxwyJKY1PfwUpr_ujyHuRI-Y26TP_eFrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=ekkFnccnzeMli2rfOysqx3Zva1OoJCiqNFhaldWO8ioEi6FURRzBZN7b3-cV8lwgr1cwUw_VKTTEpliermRjfyNzV_stlZlpLaNGAD-rzMp8kOHrjWQF-HGGOIEfR_g57bNgFmmUY-EQGDgC89-7MReOXvptp2wx_qzV0YEC1-XQ7nqSej-P5rwZSsstJL823BRVqKdwowDI6HUtLz3Pg8-mr-s67ZPQv9TCEjKl-VofHGQdSgJtDw0oFWYlAm1zsMZYA5vypKyp2a7VwKEV3KybW_1Yi-hKUTsY4MA1-iM0IfgOjhMhPoxwyJKY1PfwUpr_ujyHuRI-Y26TP_eFrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر، آتش‌سوزی‌های گسترده در تأسیسات ذخیره‌سازی «آرامکو» در «ابها» واقع در جنوب غربی عربستان سعودی را پس از حملات پهپادی و موشکی حوثی‌ها نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71681" target="_blank">📅 18:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71680">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
لحظاتی قبل یک پهپاد دیگر از نوع MQ-1 متعلق به آمریکا بر فراز تنگه هرمز با استفاده از یک سیستم پدافند هوایی متعلق به نیروی قدس سپاه پاسداران انقلاب اسلامی سرنگون شد.
این سومین پهبادی است که سپاه مدعی سرنگونی آن در روز جاری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71680" target="_blank">📅 18:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8132b94509.mp4?token=dq_SlCtrwzOnbZxUSB8-kPNKTiK7G3eJvyaNA2KXDTZ8NpcnbL5Y50Dbx4hkJjmP7Zl5hdm_IlrmUMjIsoYSmXgzihjpBHgx7lsS72QQY2oXjQ72pNQVbPeTqBjfY9b-jqNP580Pg6WWFR7rWQgc6wphCFbD9vFKowE12hdE_F-W6qRA2O7b2duzcxGgt5_EfjGAa-ZBfd-7TyMo_CZnePPZDfRCpqjNpYsCBM2QJDJ49OO1rfWaYH6Iy2IEvD2_BGczAQRsx3jrKTNLB7_GER9hRryhSpDrSWHqK3U6vgUKCjyvtYGBm5hcibdg1TI0nkTmXA7dwomPhdHDb47u7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8132b94509.mp4?token=dq_SlCtrwzOnbZxUSB8-kPNKTiK7G3eJvyaNA2KXDTZ8NpcnbL5Y50Dbx4hkJjmP7Zl5hdm_IlrmUMjIsoYSmXgzihjpBHgx7lsS72QQY2oXjQ72pNQVbPeTqBjfY9b-jqNP580Pg6WWFR7rWQgc6wphCFbD9vFKowE12hdE_F-W6qRA2O7b2duzcxGgt5_EfjGAa-ZBfd-7TyMo_CZnePPZDfRCpqjNpYsCBM2QJDJ49OO1rfWaYH6Iy2IEvD2_BGczAQRsx3jrKTNLB7_GER9hRryhSpDrSWHqK3U6vgUKCjyvtYGBm5hcibdg1TI0nkTmXA7dwomPhdHDb47u7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پروازهای داخلی(کرمانشاه به مشهد)دچار سانحه شده و بخشی از کابین دچار شکستگی و اسیب میشه، خوشبختانه مسافران این پرواز سالم به مقصد رسیدند. جزییات دقیق این پرواز و نقص فنی هنوز مشخص نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71679" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71678" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71678" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71677">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crMEWfHuMyOHXrfUtnN81NGw5j9cc6FzdekykFE8CaKEfBx-fOXUyPKmsxrPlh6Wxu1SO6D7TwGwAJ4NGTus-dSFZwNfSYXq2Wje8UiubCX4_i02UOGM7ZCTrcEevJTQgqs6SUmDf4HQPxCeZKFg1RPSXXdJNynghfLw116kPVswdTBdm4pAIema9czlF98Eu6s9o3g7A_AGwGWjmvM1BnB3ShLRYVTNpXbYobEpkBbjoYRyBvvPJQFwRExHmfIW7re7Zxnq_OD8Y_fpQQ1aihg6eFXoO9gz9cJHPN4nJeLE-Sx_SZg6beKrcodVYWTRVtYYM99v_p4gR6n2O9rUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
تاتنهام
🆚
لیورپول
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
تاتنهام: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
⚽️
لیورپول: ۲ برد، ۳ تساوی و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71677" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71676">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=ZhwmMuxNIs8f28Pv_vuZbiwfuoIQ-7Hcd6fZLsANNWV75tZ-lqpJXDUOrW1x48O8l3uq4Mw0d25SG45RrU1oXgXLvso6BGqHCq7mKEEuW-WqxRULfStpu1h4orwm5mxOsJvcSdnbs1K8sjwfOetDjUHo_wSxnhvY70sZpnStlkvLNkyKhoqPQjbezpFIrUmqbS-CLsJVha_88oLM9EbiVjBxO-tjWDNBBPEiPsRAyz-vOHiml7pkcpLg7xPejydI5aeG_uktdLW_RVuJeunvKh3g2M_rKs0TbIidZtvDfkynfer4TA305e6qYhZ3iqw0_IfyECj-v5_IDTXE6JVZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=ZhwmMuxNIs8f28Pv_vuZbiwfuoIQ-7Hcd6fZLsANNWV75tZ-lqpJXDUOrW1x48O8l3uq4Mw0d25SG45RrU1oXgXLvso6BGqHCq7mKEEuW-WqxRULfStpu1h4orwm5mxOsJvcSdnbs1K8sjwfOetDjUHo_wSxnhvY70sZpnStlkvLNkyKhoqPQjbezpFIrUmqbS-CLsJVha_88oLM9EbiVjBxO-tjWDNBBPEiPsRAyz-vOHiml7pkcpLg7xPejydI5aeG_uktdLW_RVuJeunvKh3g2M_rKs0TbIidZtvDfkynfer4TA305e6qYhZ3iqw0_IfyECj-v5_IDTXE6JVZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
بسنت درباره ایران:
ترامپ در حال اقدام علیه رژیمی است که خود را وقف شعار «مرگ بر آمریکا» کرده و برای تحقق همین هدف به دنبال دستیابی به سلاح‌های هسته‌ای است؛
اقداماتی که رؤسای جمهور پیشین مدت‌ها از انجام آن طفره می‌رفتند.
تحت رهبری او،آمریکا دیگر تهدید ایران را مدیریت نمی‌کند؛ ما در حال پایان دادن به آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71676" target="_blank">📅 18:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71675">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAkNQmCT4ANharl8wCrNIyeR3ZXziJ__c5YCKiTIgaoikeLnUE-kXTEOcWIsraZV4XVNBr7vJi3dMXt8QDKRuZr3L1UyZBkhiUuT50L0s6lp4temXTEukvVJlg5AVacpAVD9mlbptzjxLEJNmxwZR3Z43dOyQJiBqpiFHv1twCl5wgfHpK6FY0WdEi3J8SAjukbxWgjccKdAGuGou0m_Bu3ZA3G_htIs2ZzO3cCgsl1H2rvBxi-jmaaDJhKR21DsefQ2gI3QQoxF43IYVolkFF3x07ko1He9HweWW53wVY78FNRx2e5tL-REM5McIs7IYm2Cf84jQL0ZWWOb6-qT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس. تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.   @News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71675" target="_blank">📅 17:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71674">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=ip7hYvmURuGxFaJU-GwLNcKUAb0roSU1IWvm6GaY1hfWRNSbsY8RFUYSPhfB2eHZ1WCxs9Tol1pCsPLuAIOQnUkN8YkcP9YI3jyt6ljjM_9eFvE283TKd0LsfOVPch7zRmoHSh-uf6MApXCZtGIQk0299RPBk9_tely6bdmQyDY9J-S6rrjpCmsasWdvOt6mh2m9lpOIm4TIZuc4fmsyHmHP8XRYSX9VCHdP-ODbNk9zuvliJcDbXVQnuAGzvkdHd6qO5pH8jSqi-xOj6Ki_fmSIMSdGRfaAk16u6ABfCULQRcpVDIVtBi1h2y5yEX4kv2XHrLPx8narIjt97b2P8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=ip7hYvmURuGxFaJU-GwLNcKUAb0roSU1IWvm6GaY1hfWRNSbsY8RFUYSPhfB2eHZ1WCxs9Tol1pCsPLuAIOQnUkN8YkcP9YI3jyt6ljjM_9eFvE283TKd0LsfOVPch7zRmoHSh-uf6MApXCZtGIQk0299RPBk9_tely6bdmQyDY9J-S6rrjpCmsasWdvOt6mh2m9lpOIm4TIZuc4fmsyHmHP8XRYSX9VCHdP-ODbNk9zuvliJcDbXVQnuAGzvkdHd6qO5pH8jSqi-xOj6Ki_fmSIMSdGRfaAk16u6ABfCULQRcpVDIVtBi1h2y5yEX4kv2XHrLPx8narIjt97b2P8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو سی‌و‌سه پُل اصفهان، یه پسر نوجوون اومد مثلا یه حرکت نمایشی بزنه و از یه ارتفاع نسبتا بلند بپره پایین که فرود ناموفقی داشت و با سر رفت تو زمین...
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71674" target="_blank">📅 17:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71673">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=sMVlULXfSiGxf5YD8DqHByav7aHyngq6B4szgeb5cg8C5rPAqt8o-r9-VistBpYzKQXVY5y3rgyMj1aVeJ0uJlg6Mm0NIt9ncjze47bUyYKx7rHu8lIwthjexR86zVYcbZ8zdjQ2Em4OhEYxbXnkHqQOmuujIgNKD-wRHUu_gkoBk9oS8l5Dw5GwutVi2lQl0nRPgGDHCaD_pEcfFbcXe5wCt-SZWHBf4Zd4RZjtO0PqAoAhHweCE7KNCuN4UO1yqsnMrGKwoojr0oQ7eY1DyNrvFRQZN2kaxPdr1xQFB3lZ-Q_hNw-EZ-nL4COJSE9-1lGjEYpFOJIvcg6GdrRl_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=sMVlULXfSiGxf5YD8DqHByav7aHyngq6B4szgeb5cg8C5rPAqt8o-r9-VistBpYzKQXVY5y3rgyMj1aVeJ0uJlg6Mm0NIt9ncjze47bUyYKx7rHu8lIwthjexR86zVYcbZ8zdjQ2Em4OhEYxbXnkHqQOmuujIgNKD-wRHUu_gkoBk9oS8l5Dw5GwutVi2lQl0nRPgGDHCaD_pEcfFbcXe5wCt-SZWHBf4Zd4RZjtO0PqAoAhHweCE7KNCuN4UO1yqsnMrGKwoojr0oQ7eY1DyNrvFRQZN2kaxPdr1xQFB3lZ-Q_hNw-EZ-nL4COJSE9-1lGjEYpFOJIvcg6GdrRl_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71673" target="_blank">📅 16:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71672">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نفتالی بنت درباره ایران:
این رژیم فاسد و پوسیده است؛ همچون درختی که از درون دچار پوسیدگی شده و سرانجام فرو خواهد ریخت.
در مورد این درخت پوسیده، می‌توانیم اینجا و آنجا حفاری‌هایی انجام دهیم. منظورم صرفاً اقدامات نظامی (کینتیک) نیست.
صحبت من درباره اقدامات اقتصادی، کارهایی که نمی‌خواهم نامی از آن‌ها ببرم، و همچنین تقویت معترضان داخلی و تقویت دشمنانِ این رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71672" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71671">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=AU7qe3XrZunjlX5bRnW_hjE6_KqiXRil0xuqneQBSxgbB-OJGmF4p2a_PYp2aYNqKLsxWngYX6RZTmEuUSNq8orRRYxpmA3VPnaHo7Q-UXGS2wjpy5hYMKlxNPuZcBxd493nkINXS1yrvnmE4dI24V7ADNET8s_XVg_g2yiqfAEmev-d2snk5nEM8eE3jg-q7YpmCWZM5DoUGtlwVvoMrI81auJNanuLQBD93xAdKrTxBJhVH1r2R69N3HyWp9GWQvkegSs0fK22SLHAt-bkuBZ3UNc3zvq9130kfN4UKaBTU4Obg8YKCbV4CALEJhbiKrXwLGb6xsxRdHlJI6Q7tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=AU7qe3XrZunjlX5bRnW_hjE6_KqiXRil0xuqneQBSxgbB-OJGmF4p2a_PYp2aYNqKLsxWngYX6RZTmEuUSNq8orRRYxpmA3VPnaHo7Q-UXGS2wjpy5hYMKlxNPuZcBxd493nkINXS1yrvnmE4dI24V7ADNET8s_XVg_g2yiqfAEmev-d2snk5nEM8eE3jg-q7YpmCWZM5DoUGtlwVvoMrI81auJNanuLQBD93xAdKrTxBJhVH1r2R69N3HyWp9GWQvkegSs0fK22SLHAt-bkuBZ3UNc3zvq9130kfN4UKaBTU4Obg8YKCbV4CALEJhbiKrXwLGb6xsxRdHlJI6Q7tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌ های این خانم به‌شدت وایرال شده و دخترا هم خیلی بهش انتقاد کردن:
اگه یه مرد، دارایی های خودش رو به نام خانومش بزنه، اون زندگی رو با دستای خودش نابود کرده.
آقایون اگه ۵ تا خونه هم به نامشون باشه، هیچوقت تو دعوا خانوم‌ خودشون رو بیرون نمیکنن
ولی اگه خانوما یه چیزی به نامشون باشه به این موضوع فکر میکنن که میتونن بدون اون آقا ادامه بدن.
من خودم خانواده‌هایی دیدم که به دخترشون میگفتن تو که ماشین و خونه به نامت زده دیگه احتیاجی بهش نداری، خودت برو زندگی کن.
خانوما اصلا جنبه‌‌ی اینکه چیزی به نامشون باشه رو ندارن، اون اگه بخواد زندگی کنه با یدونه سکه هم زندگیش رو میکنه، آقایون بفهمید من دارم چی میگم...
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71671" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71670">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=I3ko91kt1zMYZVdHDZabnWM9I-XJ2R3J4ilLY5VN_yvXZL3nkAkfEmeAZeOvUmB_oAJ7e4M10Wwonwli_Jqy2b0quZM1krwAUQvkNUyT9NL4GMFXnRahpCawD9vnknhiRXNroy-w4gqQm2qdpID2k80sprUUjdZW1su4PP0w8hg3g9ytRa02AwLoGQYLzy34psHdZ0vNywfd_aX8DRO_ordLk1-2MN0R9pbF8AiXG5MnU68HB4tcB7sA-y9Nclx8q1y4pnRWyc4i56icY6mlj-0QumgkG2AfuaRnH-F7_ixLE9fUx96CnUFBuMfS-CRdE6n_bECNkTyzvevsZyUBLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=I3ko91kt1zMYZVdHDZabnWM9I-XJ2R3J4ilLY5VN_yvXZL3nkAkfEmeAZeOvUmB_oAJ7e4M10Wwonwli_Jqy2b0quZM1krwAUQvkNUyT9NL4GMFXnRahpCawD9vnknhiRXNroy-w4gqQm2qdpID2k80sprUUjdZW1su4PP0w8hg3g9ytRa02AwLoGQYLzy34psHdZ0vNywfd_aX8DRO_ordLk1-2MN0R9pbF8AiXG5MnU68HB4tcB7sA-y9Nclx8q1y4pnRWyc4i56icY6mlj-0QumgkG2AfuaRnH-F7_ixLE9fUx96CnUFBuMfS-CRdE6n_bECNkTyzvevsZyUBLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیراندازی نیروهای انتظامی به سمت بالگردآمریکایی در جریان عملیات نجات خلبان مفقودی آمریکا در روز روشن
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71670" target="_blank">📅 15:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71669">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=o7ZfIASwl0ZECb3I2i4WvV9lcCrTRmNWDU1jJDyfNIcCimUWP9NBNIjXheZIgHHL9d8fvRMCVR-_yjKaELghGHim7wIFpgt-OjYz_LBJgZhvvRPSXabhYXPTi1X_sIeuMAbYI3FHSTaUMF2UwnPHMA-ccmVtlhKcnoHgEtDIdVsyxudvGD9o7QQYr1DXlOO3447BZzy9j4Q9XIuADJTIaIYZnuAUFP6lnaaR7OgPbHyiuKVkcPClhqfmNRmtUBrZKK2mA07qTCM3yi4ezErF9T5uWKDOAJiU4xznjoAydLDX9jaofb_Mkg2ty4aq5uf1zV414Wj1zlSRmB4jHbtAJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=o7ZfIASwl0ZECb3I2i4WvV9lcCrTRmNWDU1jJDyfNIcCimUWP9NBNIjXheZIgHHL9d8fvRMCVR-_yjKaELghGHim7wIFpgt-OjYz_LBJgZhvvRPSXabhYXPTi1X_sIeuMAbYI3FHSTaUMF2UwnPHMA-ccmVtlhKcnoHgEtDIdVsyxudvGD9o7QQYr1DXlOO3447BZzy9j4Q9XIuADJTIaIYZnuAUFP6lnaaR7OgPbHyiuKVkcPClhqfmNRmtUBrZKK2mA07qTCM3yi4ezErF9T5uWKDOAJiU4xznjoAydLDX9jaofb_Mkg2ty4aq5uf1zV414Wj1zlSRmB4jHbtAJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر زنِ مجتبی خامنه‌ای:
مجتبی خامنه‌ای با همسرش سریال " فرار از زندان " رو مفصل نشستن دیدن و درباره اتفاقاتی که داخل سریال افتاده بود هم صحبت میکردن.
یه بار تو یه جمعی گوشی یکی زنگ خورد، من گفتم این چه آهنگیه دیگه؟ که یهو مجتبی گفتش این آهنگِ یکی از فیلم‌های کریستوفر نولانه دیگه، چطوری نمیشناسیش؟
‌
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71669" target="_blank">📅 14:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71668">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hizZnXTmJ3TpkH-MsNYy6bwmkbpfGq5WCPQwAvHQ1IdDO66IzVty6I0d7XKBzka5G5AcJodh5s-oqbtovn2fPc7wtIhdRxIuQBgOdhLGaSh8tcT9DpobEwP6ahMfTFLKQ2hRh3wvNHyMtytRP9QyvSjNLlMZaZBZZXRimHeNI6w48f5DW7JUKrfjov-QUw3bLwzYzo0H9rQKi0aNK3A1RpCdPTI1QavR6so4BebY4_gaTj26PSW58C4iJ4-6GYnUJzrIWzv1X0KGGy4d9gnFhD0g3TwcLoI6d4gaGYc7CV0MmAsoUmyL4NiPxe12aAnwl3C9PBguY-8fR5R13srDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی:
«نشست عمان» با حضور کشورهای خلیج فارس برای تثبیتِ مسیر تنگه هرمز، با نقش‌آفرینیِ جدیِ آمریکا و برخی از کشورهای حوزه خلیج فارس فعلا لغو شد
عربستان» به بهانه اصابت خط لوله‌اش و درخواستی که از پاکستانی‌ها داشته تا ایران را راضی کنند که به انصارلله بگوید از فتوحاتِ جدید عقب نشینی کند، «بحرین» بابتِ ناراحتی از جنگ رمضان و پرتابه‌‌های متعددی که بخاطر میزبانی از زیرساخت‌های نظامیِ آمریکا در خاکِ کشورش دریافت کرده و «امارات» هم بابتِ اُفت جایگاش در آینده‌‌ی منطقه در صورتی که مسیر جدید تنگه تثبیت شود، در نشستِ مهمِ عمان شرکت نکرده و کارشکنی کردند!
ولی بازیگرِ اصلیِ لغوِ این نشست، آمریکاست!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71668" target="_blank">📅 13:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71667">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حملات موشکی/پهبادی حوثی های یمن به مکه، طائف و جده عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71667" target="_blank">📅 12:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71666">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTMmgLqweKFXh4V8TDByf0C3ghpnaYO3yoQlU-EB57QNISxUXtB2zj6VVlOii3i4KjzDHOqUeG9rD4xRyE-k6GG1ZkgciTzr3qVkSiEuIIHCrxlQl081Sopirj0JEx-6L8xC4zgDF6K-Z1_2fWt0acuwKG6B2eVW88vKtvq1fqplqXgnmpj3ssCFC7zbNw5_54SClVwu0mXF_03PIAF0pFTH5LsCTsSAtebNStgv3I1xarRtP7TPJ1Pe-oepCegOCgnVV3N4nnCRqgxQT88LSd-BvzmOkU8JsnGr9Yl9HsUEaj-0WrJeomwxw7L9oPCb8RP5yWLRNu0n39HSZ6724A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) :
گزارشی با تأخیر زمانی درباره وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک منبع موثق گزارش داده است که شناوری مورد اصابت یک پرتابه ناشناس قرار گرفته است.
هیچ‌گونه خسارت یا پیامد زیست‌محیطی گزارش نشده و مقامات در حال بررسی موضوع هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71666" target="_blank">📅 12:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71665">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=pArkhTMapF2y-Bjb6PdgWHU9RNcmhcVu-2ZmYRVmPIlawipYCN_0GYtWO8NOEWSoMxtpOMU11Wn5qKCawzWEqMiAgzcAzyCmVLTg8EYGEa5MA-2OMbz1a81zAsC4Q8h_jqR8dpkPAU06glmvHzh0LUi3HUYFbAf5IjMFvSAviXWSS0Jw9WJp2Pr-ir3Al1CAQK_LHMHhbXxDl6XwjpT2nkmXd35ffCceNcQz3udjwjST48dHIovs_TUZrsKxOZ73XZxuJzxVNA7Ib7sinILjJTG50-w_2nT5FzvFV9cpAx1u9HXHCOe-Jp6DU4pppAku9zyV-IThuD-rgqQrzymdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=pArkhTMapF2y-Bjb6PdgWHU9RNcmhcVu-2ZmYRVmPIlawipYCN_0GYtWO8NOEWSoMxtpOMU11Wn5qKCawzWEqMiAgzcAzyCmVLTg8EYGEa5MA-2OMbz1a81zAsC4Q8h_jqR8dpkPAU06glmvHzh0LUi3HUYFbAf5IjMFvSAviXWSS0Jw9WJp2Pr-ir3Al1CAQK_LHMHhbXxDl6XwjpT2nkmXd35ffCceNcQz3udjwjST48dHIovs_TUZrsKxOZ73XZxuJzxVNA7Ib7sinILjJTG50-w_2nT5FzvFV9cpAx1u9HXHCOe-Jp6DU4pppAku9zyV-IThuD-rgqQrzymdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبه ناو سپاه با عنوان «رودکی» که در جنگ ۴۰ روزه منهدم شد در حال غرق شدن است. این کشتی تجاری بود اما به نظامی تغییر کاربری داد و گفته شد هلی‌کوپتربر است اما هدف حمله قرار گرفت و نابود شد.
در جریان جنگ ۴۰ روزه تقریبا تمام شبه ناوهای سـ.ـپاه و ارتش از بین رفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71665" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71664">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71664" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71663">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvU14PhTcthUwSwA4yy-3VWggmBmELpZU6jtEyVSUm65EvWH3jLslntFY22OcxKcLaEMMIR7Ay3Hw6lCAnt9GYC4i6z3bZXb68OY8hHEDOuEqMYtOK-zDXkJRi3OclDapcgPa7BwtmkY5r7Dh_77Fgp7BMDa2p-iXPcCLEX0KU6TNN9mqdLJANy-Vwz86z9jO8yPiADVzzICOmKjom0XTN1GgFOTo0BAkbFMBAu-Q1vQX4PREx3fB68DU-acxLvU1bayi2RU6g-9VUM_45DB05hbDkkjSODJ3Hk6VQUxdcidXjRwPktJR4xB1Lol0gAGozQTfUv6Y-AHWQR_RE8NBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
رئال مادرید
🆚
الچه
⚽️
را در TrexBet پیش‌بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
رئال مادرید: ۴ برد، ۱ شکست و ۱۴ گل زده
⚽️
الچه: ۲ تساوی، ۳ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71663" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71662">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FT9UxbGmOFFF6HRBCFSyUrBQiDOFdVa8p7eujWaP0zHhwziMedVV2Kj68dLTEqL2OwT1Jge-fURVa3S-t7oXMyVuuo0IyCAZ2AThrkdhOZRXv2BDtjip0pQZ9d9fkJXZXZPNvUydDmR07MshhsqF-ghCiL8Wg1M1cciGhqBjXOCNeOLT81EeGc6d2buJzwLQnk60Vnzy5YCcRUt0_Q3soeK8fcUJhDS3AAD9CQeve7iufYuJXIflpvx37YsvkRAI3UA_QyPE6FFEkklfYh7BDtc-ShOsj0l5JZCJWpGPE3Uz6PXHp0AeRayITALhbKyOzVo2g6gcYhAhCJe_3hXDxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71662" target="_blank">📅 11:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71661">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=MsmvV8clz14we2K0XWH7XZAB_QC4lBU0B2axfos8qxsfK6M0SmDa1OezZYHOfWLQFgNg5adk0rVkm4n2cupKqkJ4ja-zcJuQ8AaS80bR3GN5-5J36zzRU3dvKiaFAm1ACzmzhBQGzQh8chMg3ifHj8xGD-F1g2FkKHqC1Mcis77dvWpWxS3TQNZ83L-Awur2UgmBkdsp2NA1DC1VShHV_Pjt5Zyj7K3qks0cIghxmrSu3u0ydSa0fOvYB2AV1vtQ5pMrFxHKzYcn4KwZtj5HisoCFJbsjJVMenBTL8m8U3oXOBxDV6gmI0GgDx204dn7w-uduQ0ky-Lq3xIgZhpW9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=MsmvV8clz14we2K0XWH7XZAB_QC4lBU0B2axfos8qxsfK6M0SmDa1OezZYHOfWLQFgNg5adk0rVkm4n2cupKqkJ4ja-zcJuQ8AaS80bR3GN5-5J36zzRU3dvKiaFAm1ACzmzhBQGzQh8chMg3ifHj8xGD-F1g2FkKHqC1Mcis77dvWpWxS3TQNZ83L-Awur2UgmBkdsp2NA1DC1VShHV_Pjt5Zyj7K3qks0cIghxmrSu3u0ydSa0fOvYB2AV1vtQ5pMrFxHKzYcn4KwZtj5HisoCFJbsjJVMenBTL8m8U3oXOBxDV6gmI0GgDx204dn7w-uduQ0ky-Lq3xIgZhpW9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: آیا قرار است همه ما تا ۱۰ سال دیگر بمیریم یا نه؟ موضوع بحث همین است.
ایلان ماسک: خب، متأسفم که باید این را بگویم، اما همه ما خواهیم مرد.
مجری: می‌شود یک بازه زمانی مشخص کنید؟
ایلان ماسک: بله، نرخ مرگ‌ومیر همچنان ثابت و ۱۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71661" target="_blank">📅 11:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71659">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎙
صحبت های این خانم درباره سگش:
خرج ماهانه سگم حدود سیصد/چهارصد میلیون تومنه
😳
روتین روزانش صبح حدوداً ساعت ۱۰ بیدار می‌شه، یعنی صبح همه رو بیدار می‌کنه. بعد تا ساعت یازده که می‌شه، یه مربی شخصی داره که میاد می‌بردش یه جا مثل فضای باشگاه.
بعد هم که ساعت سه و چهار غذاشون رو می‌خوره. پوستش حساسه و یه سری شامپوهای خاص داره که ما همیشه می‌زنیم.
شب‌ها من یه دور پیاده‌روی می‌برمش و بعد هم شامشون رو خودم می‌دم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71659" target="_blank">📅 11:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71658">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=U5Cf3bttInFollQLRlPgawmke740xKZRZNCuaTn_HcSNX2kpJo94wJCClsThAR7fhYUbIwaOk-tnWua3B1XmXqlJS3aaV5CR3JnLpNOXDXFtJhGmH3WVrKEaBll1D61PzSJ1tLyvZqdl0FK3FpKBnU09hsJ2IJoRIU1pNhV-ja7Jp-BMkW-Iy9Ul2-DFhvaunowIVc00Aee2PH9s1lOGFsCnM3dfdNuMfjAZGGPMbsaqLmweGMWYfKx-VP5LLrDuDVDuZsJzq0qt-zINCS3BtewFCeOG_-hm8fK01qu0hT9XbZp73woCIbjqGpvOcPYTOinfPameKK65GOXx1rW1jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=U5Cf3bttInFollQLRlPgawmke740xKZRZNCuaTn_HcSNX2kpJo94wJCClsThAR7fhYUbIwaOk-tnWua3B1XmXqlJS3aaV5CR3JnLpNOXDXFtJhGmH3WVrKEaBll1D61PzSJ1tLyvZqdl0FK3FpKBnU09hsJ2IJoRIU1pNhV-ja7Jp-BMkW-Iy9Ul2-DFhvaunowIVc00Aee2PH9s1lOGFsCnM3dfdNuMfjAZGGPMbsaqLmweGMWYfKx-VP5LLrDuDVDuZsJzq0qt-zINCS3BtewFCeOG_-hm8fK01qu0hT9XbZp73woCIbjqGpvOcPYTOinfPameKK65GOXx1rW1jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب علیه روحانی در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71658" target="_blank">📅 11:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71657">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوباره آمار مبتلایان به کرونا تو کشور داره می‌ره بالا، خیلی مراقبت کنید
من خودمم دو روزه به شکل عجیبی گلو دردم
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71657" target="_blank">📅 10:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71656">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840407be05.mp4?token=LQfz4lvZN9mIcNIadPFhcJEP15PA86OnRF9rapaPiF6Rzd4JvgXrkOO-7LnO5MdzPHks5PYNJ1AUtesnrX2f3LStSqsH_2qJP-wQ4YiBSv9ajrv3paYwWlS4MkX01ui9jexOwrWcYuDCwoF3GvX9PZdBDsQMLZRTGFf8hHwahmu7RvEiOrfaBC4YRbH4kpylRFPWGlaHyDMq6dIcE58iKiYy1PRG-idKegSA3vaMQEEAapXb5X9OC_AupAEucHrf44E1sfUDI5JULnfJhgJKHKAN-gF4kxHK0Cuxw6h-AxpFrndFU5Bmf61sgpg5wrL081bYx8tfZI408NULBdCevA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840407be05.mp4?token=LQfz4lvZN9mIcNIadPFhcJEP15PA86OnRF9rapaPiF6Rzd4JvgXrkOO-7LnO5MdzPHks5PYNJ1AUtesnrX2f3LStSqsH_2qJP-wQ4YiBSv9ajrv3paYwWlS4MkX01ui9jexOwrWcYuDCwoF3GvX9PZdBDsQMLZRTGFf8hHwahmu7RvEiOrfaBC4YRbH4kpylRFPWGlaHyDMq6dIcE58iKiYy1PRG-idKegSA3vaMQEEAapXb5X9OC_AupAEucHrf44E1sfUDI5JULnfJhgJKHKAN-gF4kxHK0Cuxw6h-AxpFrndFU5Bmf61sgpg5wrL081bYx8tfZI408NULBdCevA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار شده 240 تومن؛
همون لحظه صداوسیما:
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71656" target="_blank">📅 10:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71653">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=AMc4MXCdCeLWqn8-9plkZyPfo2eY9YtVDiM0UVHO4RM6ooVy-Rhgywfpo-I0Ax9F_Yq3X70DYIQsMgpmviw3K8Hc1rfie-8OGBAzk-hAq1jj7wKlJ77biODBkMSnqlue1oKyrAaOCw4iTQtGClKpUsBkZc6USh9ggZPCvM8eaNfreZJTgJ8phZhixZiFk73V8-kIayQhnyhBuh-2i9-LVvK3ojNkFFYuZ-jZ1t4IZign0yI4XejWNEoArXpRhvSpllB0aH27NT1suJ8bRFW4yz5dmpcsAOPmnjmBAsrjspiTGfViMJ6FVBHEmKrRB48bhs0VIYqNPzMs1pwVW_53jaOD2YtR-7ZPKUYvc5_WKTlTvMuPWsSzkoEStIG16mFlYY59jwxPfde5N0XPefvWcKl8s_mMXZmXlUEyTG0HFjFmJAUgvYjy1EacpPf__bro4wonVlgNudEF2KWkc16lhxuyUEbDF9Eblm9iFyajOxJca3WOPWGErkVo4CG9OHdXhA_LTXmB4DlddRfYjh7T5ASHsK2B7ZJT0o9hUbyUHcV26I3SCzEx9SFsBjK-nQ1UlW6S6OAegWmvucZw_Bpwst2JjbeW2dWnIicNWCO1k7c29Y2NLrZHa8rZYLw8GwGJBPl5jRt_I7JO_RkDL46Va-emPLc2NzQoWIPuhHuC3TU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=AMc4MXCdCeLWqn8-9plkZyPfo2eY9YtVDiM0UVHO4RM6ooVy-Rhgywfpo-I0Ax9F_Yq3X70DYIQsMgpmviw3K8Hc1rfie-8OGBAzk-hAq1jj7wKlJ77biODBkMSnqlue1oKyrAaOCw4iTQtGClKpUsBkZc6USh9ggZPCvM8eaNfreZJTgJ8phZhixZiFk73V8-kIayQhnyhBuh-2i9-LVvK3ojNkFFYuZ-jZ1t4IZign0yI4XejWNEoArXpRhvSpllB0aH27NT1suJ8bRFW4yz5dmpcsAOPmnjmBAsrjspiTGfViMJ6FVBHEmKrRB48bhs0VIYqNPzMs1pwVW_53jaOD2YtR-7ZPKUYvc5_WKTlTvMuPWsSzkoEStIG16mFlYY59jwxPfde5N0XPefvWcKl8s_mMXZmXlUEyTG0HFjFmJAUgvYjy1EacpPf__bro4wonVlgNudEF2KWkc16lhxuyUEbDF9Eblm9iFyajOxJca3WOPWGErkVo4CG9OHdXhA_LTXmB4DlddRfYjh7T5ASHsK2B7ZJT0o9hUbyUHcV26I3SCzEx9SFsBjK-nQ1UlW6S6OAegWmvucZw_Bpwst2JjbeW2dWnIicNWCO1k7c29Y2NLrZHa8rZYLw8GwGJBPl5jRt_I7JO_RkDL46Va-emPLc2NzQoWIPuhHuC3TU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوهای این خانم معلم برزیلی مهربان و زحمتکش بخاطر سبک خاص تدریسش حسابی وایرال شده:
تو یکی از ویدیوهاش که حسابی هم وایرال شده به یه دانش آموز فوت فتیشش که درسشو خوب بلد بوده به عنوان جایزه اجازه داده پاهاشو لیس بزنه…
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71653" target="_blank">📅 10:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71652">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=CsmvdjGd28KtDP7u3k-ogDcOYHP1m0UDF6847p08BTx4MYCfxUHWuQ-dvezJq1pyi9K1WC07NSvY3P75gygSayC8c3AsVVXWlqWyn3l28v1RWI-ZsXHK4u8ElKAlnFHF6UtozG-qjhjV-RTnU6simobEzA7sypJBCkURBSsalSHcDx44u4BaNikED0z00o2_bIHgN8VHKC_fYphERhoJ0M6PwliwPZUADXtPuyUY-KWo8QgPaP5kZe_kW9rcPXJvDDzBydFDxhxtuNCxDbUUQfvBbsjWRTyerScZelaG3SWkhJm6DjZP3vpk5jS-FR4lv89sVS7rMHSgWyeoKF1ulA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=CsmvdjGd28KtDP7u3k-ogDcOYHP1m0UDF6847p08BTx4MYCfxUHWuQ-dvezJq1pyi9K1WC07NSvY3P75gygSayC8c3AsVVXWlqWyn3l28v1RWI-ZsXHK4u8ElKAlnFHF6UtozG-qjhjV-RTnU6simobEzA7sypJBCkURBSsalSHcDx44u4BaNikED0z00o2_bIHgN8VHKC_fYphERhoJ0M6PwliwPZUADXtPuyUY-KWo8QgPaP5kZe_kW9rcPXJvDDzBydFDxhxtuNCxDbUUQfvBbsjWRTyerScZelaG3SWkhJm6DjZP3vpk5jS-FR4lv89sVS7rMHSgWyeoKF1ulA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش‌چشم، کارشناس صداوسیما:
در عرض ۴ ماه موشکی ساختیم که هنوز اندیشکده‌ها و رسانه‌های غربی موندن که سیستمش چیه. موشکی که بدون نیاز به ماهواره، ناو در حال حرکت رو پیدا میکنه و دنبالش میره.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71652" target="_blank">📅 09:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71651">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168229fd60.mp4?token=JajxvmGGkCSqxPYOaKLF_QOtLhYnf5dYv2QiOjEPMKD2TqdxioXUtym6BPooQUyiuAy2UY-t6AmnokKlhGuKsxTs4X1lJPrVHvr2EHZqnN64T9c081d1q1mL28NRKqxdzdq1qHmltsdX8JkoSo5fwTcLcAk-6RZLBs5TBQDyTwl-VcfK0IUyr5eEyZUKc2YiLxigqwKEFQQrqK_gdTMd8R2PZT4tFM6p0QkJz8y__6ipU4ccJp6x2m72jqe85M6Xd-CHRgIL5d2NFXtJtKQjEevyrm_jUbw2x2sWsR51kTOvRq3hfP5pSz1HpJyuwa8YneDRr0505KfczdWnPp_G8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168229fd60.mp4?token=JajxvmGGkCSqxPYOaKLF_QOtLhYnf5dYv2QiOjEPMKD2TqdxioXUtym6BPooQUyiuAy2UY-t6AmnokKlhGuKsxTs4X1lJPrVHvr2EHZqnN64T9c081d1q1mL28NRKqxdzdq1qHmltsdX8JkoSo5fwTcLcAk-6RZLBs5TBQDyTwl-VcfK0IUyr5eEyZUKc2YiLxigqwKEFQQrqK_gdTMd8R2PZT4tFM6p0QkJz8y__6ipU4ccJp6x2m72jqe85M6Xd-CHRgIL5d2NFXtJtKQjEevyrm_jUbw2x2sWsR51kTOvRq3hfP5pSz1HpJyuwa8YneDRr0505KfczdWnPp_G8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواب رییس کمیسیون امنیت ملی به روحانی:
اون روزایی که تصمیمات غلط میگرفتن اون زمان دنبال رفراندوم نبودن بلکه دنبال حاشیه بودن
اکثریت مجلس خواستار برخورد قانونی با روحانی هستیم و این تقاضا رو ارسال کردیم
قرار نیست یکی تو گذشته مقامی داشته الان از عدل الهی و کشوری مصونیت داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71651" target="_blank">📅 09:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71648">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=Sh7zisg6dBH-ktVRzGKpaiVAPkThBJ_WWV2jJCpyoGkkZJLR3WXMKQ78vkqhrai4XowztFcqn6B8YdaDd0r6eUCKPtLnJeA_8tueGCjY59Mq-ssgI47-2PRsL1on0QVqa1h6Nik5IfxMS314ntyylsK-9UFg5EUlzD3qj_QcC1EJIzV-WdQkDacMRRnitt1nvN8q4zSSxvnKGYYMp0Fh9uQHjoIQL1bAQOoe46V9PRHt-sTAeNIw9_HfTBwvCFF7G2X5ZDD82fns4RmH-yzBGICUaQ8kFRs5IrN05HZ-N6myIHB2d003kJNsi2r1Cn52Y-GmZnrRcJUpy_pUIfY5cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=Sh7zisg6dBH-ktVRzGKpaiVAPkThBJ_WWV2jJCpyoGkkZJLR3WXMKQ78vkqhrai4XowztFcqn6B8YdaDd0r6eUCKPtLnJeA_8tueGCjY59Mq-ssgI47-2PRsL1on0QVqa1h6Nik5IfxMS314ntyylsK-9UFg5EUlzD3qj_QcC1EJIzV-WdQkDacMRRnitt1nvN8q4zSSxvnKGYYMp0Fh9uQHjoIQL1bAQOoe46V9PRHt-sTAeNIw9_HfTBwvCFF7G2X5ZDD82fns4RmH-yzBGICUaQ8kFRs5IrN05HZ-N6myIHB2d003kJNsi2r1Cn52Y-GmZnrRcJUpy_pUIfY5cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل یک عملیات ترور علیه یک فرمانده حماس در غزه انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71648" target="_blank">📅 00:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71647">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raH2DYYGn66eijjjnTr0zlwXMDYrLDrQLkUZpWjRdvC0BMUxKvIydMB38mjofg6IcsuDr5aW-o_D1VrNhmfKdM_dRPSQ3NMxBQrCgoTEpjJp2C8QOZEPRDBeFzKaZSI2deIg2821-gz2Z7poF1tiTvxDGI5DMVPkfxfFHgwPywNDweLnlnVR4vPME6zMSPU5Xhi0E2gWPuTpuVa3mL25HhGWjYZ82jkfGfPhJF5_aVEgt9s4OTb96wKWxoGn-fyPLopYAL4nfYBtVb2BHgWvvdINk6e2Xz03O2H0PqupUaaJL-9l6_e_AbNOuBrTRK-8E89aZODO0x0gUCR4KAmNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
با سیگنال‌های متناقض رئیس‌جمهور آمریکا حواستان پرت نشود؛ از «مذاکره نمی‌کنیم» تا «برای گفت‌وگو آماده‌ایم». معادلات مربوط به نفت و تنگه‌ها تغییر کرده است. دست و پا زدن برای کنترل تبعات، جلوی آنچه در‌راه است را نخواهد گرفت.
تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71647" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71646">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس.
تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71646" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71645">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFbjeyja1ANp6j2c9Ll9W2V8ZtQlfzLcc0un9mjALdgqAs7WfpNKKlLHM0bRb_mlYdWR-fM1boY0T1bCmNsndQ8yO72KnENphWnV3-8IVph2jw8Oo_m8462-G73YFArkOOKqSFgKuW1bxId02kTV3LWGcuc6fbTzrpgMRIJwEr5bDNM-kuXQ3oZnMwW6msyxwJVwkhuCI5IuJ_C4bCfwJ46xsX9fb8VEYlse-T6Xi-PJO-hah0jd8skosP78mTyU0n3aXYfn9nVMMeg1ddAWxqBm8pcMzv62m5efEYZyXJUfpW8ps9ylc1QBE0szZ_bRKMs__F0p7SbKhEdVQRYKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
ماه گذشته، نفتکش «ال‌گایا» با پرچم پاناما هدف اصابت موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، در حالی که این کشتی در آب‌های ساحلی عمان لنگر انداخته بود، ایران بار دیگر با استفاده از پهپاد به آن حمله کرد.
این نفتکش هم‌اکنون توسط یکی از شرکای منطقه‌ای در حال یدک‌کشی است. ادعای کذب سپاه پاسداران، نمونه‌ای دیگر از دروغ‌پردازی‌ها و تلاش‌های این نهاد برای ارعاب و ایجاد مانع در مسیر تردد کشتی‌های تجاری در این تنگه(هرمز) است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71645" target="_blank">📅 23:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71644">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دیروز در بروجرد گروهی از معتادا در اعتراض به شرایط بد کمپ از اونجا فرار کردن و با این کار انعطاف و آمادگی بدنی بالای خودشونو نشون دادن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71644" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71643">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71643" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71642">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71642" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71641">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gvlse5pL6zBtXN2tYdYXNfd-yGFwC-4aHYlk6tsM-08ctgmI5IhdvROU5s9unm4J75SOAqgpBJQtUuuyXHr4O8vkAbEXXsGby9hXyt1MCO4O04iJOfBQ0UEvZzpO94bX_hhagBiBnAdhi9F5_pyncCLMWC2M7qfEk2DsYBJVOLVCLQRSG9y2NxS3i347HxhP6WzElWlRTrWMOtbpC1yX5T5_Opm_ztNOM6DwTSzsHCUSdut_ZNgXTzUIY3U2gxHTEE0JErdfErlgMOhsOkuQ_nrU3QQW0zKMQkFj3NqJD4vFGTNz7m8BhajVx5VjFwonEU7LoyMYxRSf_pYkQmDa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
نفت‌کش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در جنوب تنگه هرمز، با یک مین دریایی برخورد کرده است.
تلاش‌ها برای مهار آتش بی‌نتیجه ماند و تمام بدنه نفت‌کش در شعله‌های آتش می‌سوزد.
سپاه پاسداران اعلام کرد که پیش‌تر درباره خطرات این مسیر غیرقانونی هشدار داده بود و تأکید کرد که تنگه هرمز «همچنان بسته و تحت کنترل هوشمند ماست.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71641" target="_blank">📅 22:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71640">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d776b60914.mp4?token=KkNsqQskojdkMjL0DUQp2w2WKcJ99DV-7o_fCAUk48Tui5IKZL6LQTJ6IHoBnt1JEdkD0xPBQKEsgVEpLvFjhEOtNS0Qcf8g2s1C4QnhyIxofTl9FYksNUQJmF1a6EL22I2Kzq4Ic2ozPb05kCjA611wI1mHcXEYop02eiV0vvuGjt2aiBN4exFASpXCrDJ3t12oH_WQLqeqh-xaXa68XLN43GzwmJV_fPVFxx8GhoV7xQUilwTiYsfFruzfoTaJxu2mmWKtaDbBSF4YqBlV_LEWWw_Y8vOQ8jergf5apUWfqd337h4bK76ZJJw7x9BETiHghuBxOMY--X9mY9k68A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d776b60914.mp4?token=KkNsqQskojdkMjL0DUQp2w2WKcJ99DV-7o_fCAUk48Tui5IKZL6LQTJ6IHoBnt1JEdkD0xPBQKEsgVEpLvFjhEOtNS0Qcf8g2s1C4QnhyIxofTl9FYksNUQJmF1a6EL22I2Kzq4Ic2ozPb05kCjA611wI1mHcXEYop02eiV0vvuGjt2aiBN4exFASpXCrDJ3t12oH_WQLqeqh-xaXa68XLN43GzwmJV_fPVFxx8GhoV7xQUilwTiYsfFruzfoTaJxu2mmWKtaDbBSF4YqBlV_LEWWw_Y8vOQ8jergf5apUWfqd337h4bK76ZJJw7x9BETiHghuBxOMY--X9mY9k68A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره سرگرمی های روزمره :
سودوکو بازی نکنید اعدادی که کنار هم قرار میگیرن یه رمزه یه چیز نهفته رو آزاد میکنه
فضای سیاه سفید تخته و شطرنج هم شدیدا جذب کننده اجنه هستش
🎙
مجری:
اونوقت بگو هیچی بازی نکنیم دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71640" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71636">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bkRd3NHz5HC1f72Vrvefo41QliIAWrePImXqs6qD7-FrcKhUqvOkTs4EmzXW5o-JN3NuB5op0HvCm4IQt50Mo7y9J3vlUUcURxiNXNUw2Bnl3YmLs37urq7MqQ0ZE49idhrdL5mcmix0orXqW9mlaSeMMP3RApOfw-UBI27tTRXErDTFng4kxjW2gLuxSL1mCq_ksoHXmPOuBRXYs7dJJvGNPvHSNCd9WyKSLh3AdlAcWXa_PMGKvJ1iGWNnP6c0QWmYppQmlU8Fj3KNdyB_TLrs3ZdVM6cT4MHQYjn5Ocmbm-O9nlMztqmvGOGvVQSRspYPgxHSFX9bS4RDMeVuOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/juADQHbWRBJo-2bbmZhunwvwrJwzfHVDngyAIabz8lFz8VTBmt5z7NYZtONZbpTM-jBVYt4las4IlCqZ2XkHz9poGo6_0LExZda0CzGGTh3VvXX5A6scTo4pZgW62e-t6HjCcg43WtJCUWbW64oZqR02TGPtcfSsNCVuwha_exRUKkpCqs1ns-OUhXOUFw21CpIuT1qcDhlw38AWPNEWTdoVvWcpfSi1ndt1ZRJQ8Mdxh-cJJb9SPVnC6jiUs1FzQinQA-uBCx49HmZkjaCxnayPhxR3H3SeL8BvasVuEXe-_JfM8nsTCIs1_54cy0p-Z6tQVXq2aMurrLdRY-Z-Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیامکی که داره برای مردم ارسال میشه، از فردا رسما جانفداها برای شرکت در دوره‌های نظامی و امدادی، اعزام میشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71636" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71635">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9266483.mp4?token=iskV3wne4c57bzBN1eziDUZQ9Qkgo9jB3N6Sx8F1NJZ6Xhqpc5XHLcrXVVkh8aGALTlhdzS9ELgz48Mp9MBRo4BHxx5v7kG46qDMYe7psXmnaqn7fjm0OkpR3S-GHEd-jG2uJnIJU0Eob0kgdvxngwF6XUi_WvtD3R9mqfaoKEFSu-weGZytpqV9knbfbvP7jaVPZROMo6xOao_chXTL7QI8m87T42PpMMJyfYP4Z919LxE50ae6O5ZpnYb922qU3CLsKw7RnLWzSqgwojHI-Ksp1lcF1MrPMp4eBh5IdJY9y_8vaUuqshfmO92suzUimCZiFmL1DxyWmfKcPWGnXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9266483.mp4?token=iskV3wne4c57bzBN1eziDUZQ9Qkgo9jB3N6Sx8F1NJZ6Xhqpc5XHLcrXVVkh8aGALTlhdzS9ELgz48Mp9MBRo4BHxx5v7kG46qDMYe7psXmnaqn7fjm0OkpR3S-GHEd-jG2uJnIJU0Eob0kgdvxngwF6XUi_WvtD3R9mqfaoKEFSu-weGZytpqV9knbfbvP7jaVPZROMo6xOao_chXTL7QI8m87T42PpMMJyfYP4Z919LxE50ae6O5ZpnYb922qU3CLsKw7RnLWzSqgwojHI-Ksp1lcF1MrPMp4eBh5IdJY9y_8vaUuqshfmO92suzUimCZiFmL1DxyWmfKcPWGnXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
سیاست ما روشن است: ما به نابودی زیرساخت‌های تروریستی در «منطقه امنیتی» لبنان و رفع هرگونه تهدید علیه دولت اسرائیل ادامه خواهیم داد.
به دشمنانمان می‌گویم: اگر تا به حال درس نگرفته‌اید و تصمیم دارید دوباره به ما حمله کنید، ضربات سنگین‌تری متحمل خواهید شد.
هنوز کارهای ناتمامی باقی مانده است و به یاری خداوند، آن‌ها را به سرانجام خواهیم رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71635" target="_blank">📅 22:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71634">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu1Mc3gffk3oUXu0okMEoE29cygfZe0S02ShIauoum6Voqjus57DhjFNTaNlDS_fl_M6M8WnXBcgEA98QRq_RLA8ldt6N9WLYOU--2MKXPEqnIA5teCFmaAuEWp4uqJ39ovUI2KP1AytijG1lRksA-q_OwNu64xUDdnBJ-0bBIqoErmlyut8JmdWFmy3RHkM-pkmMovEdTU7DhBqXQ8U9vQg_s4OK5m42utB73Bt5s5wWg1B086dv8GN7SPiP0xInROAN3-8InGSOACAwIXV8hVRo2B8k6kJD_Ms_7U1EpM3J86G6n0XuyoVq_K1wOHZaB3rIpdB1P01ihNJCIKAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری «عملیات طرد اقتصادی» (Operation Economic Outcast) را با هدف قطع تمامی شریان‌های حیاتی مالی رژیم ایران و حامیان آن آغاز کرده است. به همین دلیل، من فراخوان جدیدی صادر کردم تا افشاگران اطلاعات خود را درباره کسانی که اقدامات تروریستی ایران را تسهیل می‌کنند، ارائه دهند.
خطاب به هر کسی در سراسر جهان که اطلاعاتی درباره این شریان‌های مالی دارد: این فرصت شماست. اگر اطلاعاتی قابل‌استفاده برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت پاداش باشید؛ فارغ از اینکه کجا زندگی می‌کنید یا چه کسی حقوق شما را پرداخت می‌کند. اگر چیزی دیدید، اطلاع دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71634" target="_blank">📅 21:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71633">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHAZXITBkfSjZXU9vfXjjAe5_bWvYVBwpSY_X-MaGuw13PlHC4ZwS6LRrPqtN0JyfJsl3hDRcMyMWAGrqELUGbBbNYWIuUx8b9DvNSiHKMdgJn2wjuIZ8bWXqzUXQh-jzIKs6NPv3f1ehsdpSiBvkCA9OmGu0L4UOc9vjb-iNXL4UL7QmrjqBUFlmPtpBFla7QaWCzf7M4dudRFS3RgTE6xX15kEksLnnvM7Bd1aX901WOOif-7BCPA4LlUtTKp6gG619fWW6UDoYz-1Ban9O89emO2djJU_vbzJXvIkpifEP-9QQj_Mf4oBblBHP8TQ5kFtgZFDKy35AAxnOj2vEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
نفت در حال عبور از تنگه هرمز است.
کشورهای جهان — که هیچ‌گونه کمکی به ما نکرده‌اند — باید پس از پایان یافتن این غائله و فتنه‌انگیزیِ ساختگی، هزینه‌های ایالات متحده آمریکا را جبران کنند؛ و قطعاً چنین خواهند کرد.
ما این کار را بسیار بیشتر به خاطر دیگران انجام می‌دهیم تا به خاطر خودمان، و نسل‌هاست که چنین رویه‌ای داشته‌ایم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71633" target="_blank">📅 20:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71632">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0sPXCtCWg7Myzl7xx3soHFOwMQPju_GCY0uXGVlcL3UT3BN4HvZXkeOt3bpH7IZnHJsqxjnI0Sf72S-OS8_mui16pw4-ccqrvN5-91kJPo5p_B02D-qQa8R1BUsZJzLiEUb-8IEUtoZtu9D7gbGluYiVBxEBu4CPDbWnHOhyI-k9crFF-rit-CiG8iklF_RgaFfieHIHwgWLOa24U6wXK1nKKHCi9M9gh6JQEihM7SgVYiCvhgEVFEPqsjmmBC-G4Nkk8uFvIYoDpbpVKga3P-f9ohm2DnejH69Z6aqgO_adpPQJ8SYuEmdUQL77jVZRFQJ2K6aSkiy2MRkD0Qskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
امیدوارم همه متوجه باشند که افزایش قیمت‌ها در سراسر آمریکا ناشی از عملکرد «جو بایدنِ خواب‌آلود» و دولت او بوده است، نه «ترامپ».
حتی قیمت نفت در دوران بایدن بالاتر از سطح فعلی بود، حال آنکه ما مانع از دستیابی ایران به سلاح هسته‌ای شده بودیم!
به‌جز نفت که فعلاً وضعیتی متفاوت دارد، قیمت‌ها به‌شدت در حال کاهش هستند؛ قیمت نفت نیز به‌محض پایان یافتن درگیری نظامی با ایران — که زمان زیادی هم تا آن نمانده — به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71632" target="_blank">📅 20:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71631">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvAxdx0E8EuqDjicfmPGaCsfWRIZrNdpX-9z6JCob3Q66ffMhoFGk4LZaX5YgI4hBOhDHLmQ_r1Yhg9sWGRPEE3pO2YrfILgVCFIGK9R-R_27R2nnFIldKW0fLb7hiiXFK9qsfaEIIVsGU5GI0ivTfkzM0yUwGq7VIh9XQ7eTWyhgpoJPG9jh_nhRiJ3JsW_LjdWedCufBDjLEEQIbrHsQG7boc93zjxb-R0KlAOyvt74g3Oi4s_-JgEC-xRfRaejjcIAl1yX0SXSY8CNDZOYxLbln1HP7Stjss7K4DaCDU1VfuZWJWG3bMKMABcOP12nfMHrMoonQnrpPilawN8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
من به تازگی گزارشی دریافت کرده‌ام مبنی بر اینکه ایالات متحده بیش از هر زمان دیگری در تاریخ خود، سلاح‌های نفیس و ویژه تولید می‌کند.
این سلاح‌ها روزانه به نیروهای ما در خاورمیانه و فراتر از آن تحویل داده می‌شوند. کارخانه‌های شرکت دفاعی ما به صورت شبانه‌روزی در حال فعالیت هستند و همزمان به طور متوسط هر کدام ۴ تا ۵ کارخانه جدید در مقیاس بزرگ می‌سازند!
تمرکز اصلی این تولید بر روی پاتریوت‌ها، سیستم‌های THAAD، تاماهاوک‌ها و سایر سیستم‌های موشکی استاندارد بوده است که ما در حال حاضر تعداد زیادی از آنها را در انبار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71631" target="_blank">📅 20:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71630">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
تسنیم:
ایران بارها اعلام کرده است که به دنبال مذاکره برای رسیدن به توافقی با دولت ایالات متحده نیست.
ترامپ همچنان ادعاهای نادرستی درباره توافقی با ایران مطرح می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71630" target="_blank">📅 19:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71629">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  «ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد. این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71629" target="_blank">📅 19:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71628">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXst7RZIh4VqxghDRpMES5_NDxQj47sWwhCh5LSewqD2KKuu5Nxb1D9ioZ8qRdzzu0kTrRZaodjQDd-X1gOinFazpZDKTQVH-QTTxXVzxhKx8FfbfGSUepSxAW71S5U7aS3Swj2FM0yq8ih8GBK6hZIUeuyqvN9GDsyFdf4lt6xK5M97r6rotfX1gwj4wQwj48ljY7sPpPp3iDxUaywyAn9eX6XzU6maQ_MeHmJWIByHG67Zdak0-X-afP7Q2REB1Cf6eamKvy6KwI17WCNhn4jQ5_epgxdgjfpN86TSuyDzT7yRIn4__2NO1ngHbUDxl37wSw2vV5zlyRaDORhFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
«ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد.
این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71628" target="_blank">📅 19:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71627">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=hloZfamgnA-_qcnECzVS1cWyg07pPAiA4ylnI771ZwKguSOyza05jWUCTvXi6APPNLquehXEL2vXk490cnVbgv4kEcjE_UI0pakm4meokmjtWIThxFdIrwbq2hl-1kqn61aFzTc-1RImO_cN4ymTWadZ9FCbhl_mlXgg-blPLiUe4ha6ZVEEj45Omc1b5rpjATltWyujuF02QPeTh6JqvR5b83O3b_8Mf7_w0-VjsUVX6gaaQD4UJ8e3sXXCZodnlyiqjocy27N-M_TyequinEtVdA35csc7sckh861hcrG5rH3nGmOp8fry4NGRnSZq1T044-DHi_Z5q3cw1TVpzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=hloZfamgnA-_qcnECzVS1cWyg07pPAiA4ylnI771ZwKguSOyza05jWUCTvXi6APPNLquehXEL2vXk490cnVbgv4kEcjE_UI0pakm4meokmjtWIThxFdIrwbq2hl-1kqn61aFzTc-1RImO_cN4ymTWadZ9FCbhl_mlXgg-blPLiUe4ha6ZVEEj45Omc1b5rpjATltWyujuF02QPeTh6JqvR5b83O3b_8Mf7_w0-VjsUVX6gaaQD4UJ8e3sXXCZodnlyiqjocy27N-M_TyequinEtVdA35csc7sckh861hcrG5rH3nGmOp8fry4NGRnSZq1T044-DHi_Z5q3cw1TVpzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ رفته ایرلند و چپای ایرلند هم برای اعتراض این حرکتو زدن؛
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71627" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71626">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71626" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71626" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71625">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmyY3xdn_yDPzCjpYdkw2Fe0Dc4Xw2RVf2qSWInm9AsLhNOsrkjwyzcrSSoelfLuTvPSeSSyHRH1gJn5hXmWkJ7Xby48A5opE4R44AKim0nIUdFtryQOBWTN8Eb0B7l5bhvGrMzZdaoSEYVx27XOxEtOhTi0MkZFlcPUkU-gTjfOcbgBQMH_oQOhhNwkieCu-HA5fAbIY88H0f62v7WU6Adv89bxGYNFXDqkRI0H1Q5dliJN3FkZHvMbLQwpNoeGQFS38QU8cvTJyBHqw9DQU2D2qSlw6qVD-fB-6MEjpukgcLALTHeLjP9fN54eRkzWTpFkjjcShQIavQmJy0p-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شب بزرگ فوتبال آسیا !
نبرد هیجان انگیز
⚽️
السد
🆚
استقلال
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل دو تیم باهم:
⚽️
السد: ۲ برد، ۳ تساوی و ۱۰ گل زده
⚽️
استقلال: ۳ تساوی، ۲ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71625" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71624">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-wlTG1gDYpSaOH2Ty8fp2WQPnA2ikS06ZCY6hKulA7X0kskAsKbG-6vJ9xFPA8dLaOg0braDPxh5b8-NytEW3H64CKzYhoEIPZfL6K2PhWyjdsuu-VhNH_bhRsTcqleP4ArzrjWPSB88AaZbmVSMdK7vd9COWu3yRZVezhIE_95yPOwQny3mNxrlp2x2aG1yOS-cUyso_F_uyHfXqpfp878fi0jd19EKB6KXxMv8hRPYI-xHN_L6Iwc5OTHyETog_n8kPcyzFISP8xVLQCOtPxzB4t16Zz76fIOhDhu_9DOYPxCDQcoGLktYZ_u1w6h9_bEaiNhRoj7N9GP3u--WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
اوکراین موافقت کرده است که به تأسیسات انرژی روسیه حمله نکند؛ روسیه نیز متعهد شده است که همین کار را انجام دهد!
افزایش قیمت جهانی گازوئیل عمدتاً ناشی از جنگ روسیه و اوکراین است، نه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71624" target="_blank">📅 18:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71623">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
دقایقی پیش چندین انفجار سنگین در چابهار سیستان و بلوچستان رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71623" target="_blank">📅 18:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71622">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
ویدیویی از عملیات نجات افسر تسلیحات ملقب به "براوو Bravo"(زیرنویس فارسی)
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71622" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71621">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQjawRuNH7tcMrhB11PbITgdHHQLDx8kHpDDfT_n5zqXelnT_ijmBk5wVPSz0SORcs4H2echjApUChVk4Jrou7ULL7_yEAVfLCGPk4dCrdJm6gopUuERf6ntCYvjmdA6Jj55VVlH-MNszwmk19ZdtcUTaA0K165IBFe5F8z-bgE6tWxKdgMknvWr7gprCCuGmpvb1fPMaPqBP3ex0L_uGnNyw6uVKdsfxqEoAV380sj5I2OgLN_-S5nevzLjFz-H3v2-eF1ajZ5aCJjhCV-5fJysAoppWQ5-GE5H4fTaFnVY8Q7rEkt5kjI6cM9Cocmnn2CBtr_qSXEN8U_iGzpJiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو هفته آینده برای سخنرانی در مجمع عمومی سازمان ملل در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71621" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71620">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=mLp6RLJpCI5zzFrUvgrIPk2aPZa-otukDbZeoFowGd_r3FxRi0bMiR0ZycPbBRjzR4zrp7XxLuKPIx3CR6j8mbCxrLyqg8h7Eia2MrzYo0p9Mke4WgmQEvIoe2hg0O3-LlkiiO5vwwtkB8QUUVyGOYz-tCO7pOcewJLT-dufYf3L_huGW0VLXpcRqf4t_80d-dhzRFyRyVYuV498ldwyK6UEZbAQ6A_1y56RSLhU6_e-QnYq-MUmlGnYYcgdB6QJ_MJzD5mJfN0RFDVrsHrb58TRO_n1Gnv-OYsYwGxY3n5Kv2li9UK0mrc-RrTBQe866aketkx5_AoMhx-x_DLXvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=mLp6RLJpCI5zzFrUvgrIPk2aPZa-otukDbZeoFowGd_r3FxRi0bMiR0ZycPbBRjzR4zrp7XxLuKPIx3CR6j8mbCxrLyqg8h7Eia2MrzYo0p9Mke4WgmQEvIoe2hg0O3-LlkiiO5vwwtkB8QUUVyGOYz-tCO7pOcewJLT-dufYf3L_huGW0VLXpcRqf4t_80d-dhzRFyRyVYuV498ldwyK6UEZbAQ6A_1y56RSLhU6_e-QnYq-MUmlGnYYcgdB6QJ_MJzD5mJfN0RFDVrsHrb58TRO_n1Gnv-OYsYwGxY3n5Kv2li9UK0mrc-RrTBQe866aketkx5_AoMhx-x_DLXvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک پهپاد روسی «گران» (Geran) در بخشی از جاده در شهر «پاولوگراد» که مملو از خودروهای غیرنظامیان بود، سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71620" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71619">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=lq_IpqkOss5SokCPUKPqDRrc0_bCDbB1u7ljr869xAc_eDEEhGK77ZqsOMAAFfY_lYNpe94A765EnS2D0Q0gomK4bHs28bg4hvSnwBnLo4MpnsvKzc9TDYzfalCmzUTEE__UrnozLNkwBb-lYQk5X08Oa-opFlXRpTzVJfySTwX0kwyOr73hVkb1kOt69DilY8pDD12d25m-vdZonsV_fNWCxK9syoQN4M6tzKWmWF4pWjEBdxGx824OI1O73ndha5Yx8xgL25aoiN8Rx-ruwAN--GhxAjg_wbI2wAQKcUOihUlkldPhUcf6LbvP2WJLCOYBZpokdQhwn1P6WEARKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=lq_IpqkOss5SokCPUKPqDRrc0_bCDbB1u7ljr869xAc_eDEEhGK77ZqsOMAAFfY_lYNpe94A765EnS2D0Q0gomK4bHs28bg4hvSnwBnLo4MpnsvKzc9TDYzfalCmzUTEE__UrnozLNkwBb-lYQk5X08Oa-opFlXRpTzVJfySTwX0kwyOr73hVkb1kOt69DilY8pDD12d25m-vdZonsV_fNWCxK9syoQN4M6tzKWmWF4pWjEBdxGx824OI1O73ndha5Yx8xgL25aoiN8Rx-ruwAN--GhxAjg_wbI2wAQKcUOihUlkldPhUcf6LbvP2WJLCOYBZpokdQhwn1P6WEARKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگزاری این کنسرت خیابونی مختلط توی کیش باعث شده صدای طرفداران حکومت در بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71619" target="_blank">📅 16:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71618">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=AwdLSegy6C8HEoxwfeo8ddkOXZp4TZtRbFQDj0ibOEgQq750Q_Ygi6j-gsuOEuCNT3w7tZsJX577SdBC28va5fuxUHD1NywKpddSlvXRvYq8BYeXI-P1SXiJmRwYmiMYh1K_s8qImlREEKiSAYc9GBn_d7RRgVOFWtr38VhNZ2EPJANV_wtsY1glEeaTOg220IUyrGM-9qKOvWaw9Ot1_DTPbPTsTiEByL5gQy4mCV7eAznbLWJRg6DqqNyvujO93f_kBWCKJdWlWVfZmBxVONYEp1i9oLJdh8qUsjlmLG5PRi3K6GY8bpjvzafewYCMtGhBmRfuRsM-UoiadSEKag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=AwdLSegy6C8HEoxwfeo8ddkOXZp4TZtRbFQDj0ibOEgQq750Q_Ygi6j-gsuOEuCNT3w7tZsJX577SdBC28va5fuxUHD1NywKpddSlvXRvYq8BYeXI-P1SXiJmRwYmiMYh1K_s8qImlREEKiSAYc9GBn_d7RRgVOFWtr38VhNZ2EPJANV_wtsY1glEeaTOg220IUyrGM-9qKOvWaw9Ot1_DTPbPTsTiEByL5gQy4mCV7eAznbLWJRg6DqqNyvujO93f_kBWCKJdWlWVfZmBxVONYEp1i9oLJdh8qUsjlmLG5PRi3K6GY8bpjvzafewYCMtGhBmRfuRsM-UoiadSEKag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ و بی‌بی ترسیدن نکنید اقا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71618" target="_blank">📅 16:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71617">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=IitSl_uqhpvCywDF-wVHIk6gfyPmcgkONTnsWgDToQ8pX57dXpJxmYsz6IDqxITYxiugZdLUte_uebkPZBTrsDEBok_lYJMnsgG8mKtbaTF195b2kYPOzSfNIv4h2MlwfGPVfZSxJP6SbZeBPj-0mDJ2o8gch-CPtxoGa1avct0SDTo7KJT-Sj7498d6QpTaKO3r1U3gG8YF0hdbGhP0JanSUDRUeSyLzfMzsO2or1cnbK7rHRz-jXYTyevpEDzYf0EqSetfch1xW6k9D_FsEbO8eh0vHWwIcH7RjemZfvemEmbmfZ4D7u4f3wqln2GQNtK5iuTeG1ArCvN4uMmOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=IitSl_uqhpvCywDF-wVHIk6gfyPmcgkONTnsWgDToQ8pX57dXpJxmYsz6IDqxITYxiugZdLUte_uebkPZBTrsDEBok_lYJMnsgG8mKtbaTF195b2kYPOzSfNIv4h2MlwfGPVfZSxJP6SbZeBPj-0mDJ2o8gch-CPtxoGa1avct0SDTo7KJT-Sj7498d6QpTaKO3r1U3gG8YF0hdbGhP0JanSUDRUeSyLzfMzsO2or1cnbK7rHRz-jXYTyevpEDzYf0EqSetfch1xW6k9D_FsEbO8eh0vHWwIcH7RjemZfvemEmbmfZ4D7u4f3wqln2GQNtK5iuTeG1ArCvN4uMmOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سرقت آیفون ۱۷ پرو ، در کسری از ثانیه در کافه ای در اندرزگو تهران
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71617" target="_blank">📅 15:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71616">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=NdNjzXAPvgINWgTalbtr_ocWSphpWSsSHFQkv7iMDCLFSPz2ikEQBNprIvJCD-RYyMYLts4oQ2waW0YOW0VKmflqWuo_IhvMzPaGJaKWY3SNj5pBpGvsCjfEzQINlhOZNFcUJnCOkayeHF9FdSP-R1DQ52LKNOu6Nd3I9dE0-wzK9hYUv9coNHhXl_LeW5ruKUNUt8ywq3QAcDjcPIn39yzQLwSyPc5Yw6TPchAumvOQAVboMPV7NENnZSoaoUr00YP-Cr2KgrM_RiBFmgpGlthg45h3dwXrJrctVajbjiBy_0R87JQB1uUmcJf5hISyfh94NkDjGAJEe1xW7JAqmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=NdNjzXAPvgINWgTalbtr_ocWSphpWSsSHFQkv7iMDCLFSPz2ikEQBNprIvJCD-RYyMYLts4oQ2waW0YOW0VKmflqWuo_IhvMzPaGJaKWY3SNj5pBpGvsCjfEzQINlhOZNFcUJnCOkayeHF9FdSP-R1DQ52LKNOu6Nd3I9dE0-wzK9hYUv9coNHhXl_LeW5ruKUNUt8ywq3QAcDjcPIn39yzQLwSyPc5Yw6TPchAumvOQAVboMPV7NENnZSoaoUr00YP-Cr2KgrM_RiBFmgpGlthg45h3dwXrJrctVajbjiBy_0R87JQB1uUmcJf5hISyfh94NkDjGAJEe1xW7JAqmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
در ۴۵ روز گذشته، ۹ آتشفشان فوران کرده؛ انگار در جهان، یک تغییر بزرگ در جریانه
!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71616" target="_blank">📅 15:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71615">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=P80JTKfZJM8fR_oyPSXmw_G_xcyl8bcQGWuQrLCVvjKkGONgGhf7KvGn3Wz-gRxIi7clYYfMPPTGkhob0ikBzFgm7C9MdhO2ZjZSYidCCBTEGAjnxH6IPrr3DK7NBHc9AeDWjf8CbFhERy4JLhbtWjP-vytt3pPLcnlChFhSoL7MJmt0rkTLq2jp8lFGNaerFV2yUiM9_Z3YL9PwcMyNkb6XebydEMhew9U_23HTHWpxBRSXIGzR4be_Ht3gsitZhA8K2h9Q38YwBRcxtrlnGM3X6KWaAJ1UI2Giv30m8aupet9cZmS79HMGnPFJ4RY_96Sxih2efEMvAKoMvV6-tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=P80JTKfZJM8fR_oyPSXmw_G_xcyl8bcQGWuQrLCVvjKkGONgGhf7KvGn3Wz-gRxIi7clYYfMPPTGkhob0ikBzFgm7C9MdhO2ZjZSYidCCBTEGAjnxH6IPrr3DK7NBHc9AeDWjf8CbFhERy4JLhbtWjP-vytt3pPLcnlChFhSoL7MJmt0rkTLq2jp8lFGNaerFV2yUiM9_Z3YL9PwcMyNkb6XebydEMhew9U_23HTHWpxBRSXIGzR4be_Ht3gsitZhA8K2h9Q38YwBRcxtrlnGM3X6KWaAJ1UI2Giv30m8aupet9cZmS79HMGnPFJ4RY_96Sxih2efEMvAKoMvV6-tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
ما امروز از قبل از جنگ هم آماده‌تریم!
تو حوزه مرزبانی، انتظامی و خدماتی آماده‌تریم.
با امنیت مردم شوخی نداریم، ما شرایط‌مون جنگیه، اگه وطن‌فروشی به دعوت دشمن بخواد ناامنی ایجاد بکنه، ما اون رو مثل دشمن می‌بینیم و باهاشون برخوردی رو می‌کنیم که دارن با دشمن برخورد میکنن.
دشمن میخواست چهارشنبه آخر سال 1404، همون مدل دیِ 1404 رو راه بندازه ولی حضور مردم تو صحنه، متوقفش کرد.
مردم ما فریب دشمن رو نمیخورن، 30 میلیون جان‌فدا داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71615" target="_blank">📅 14:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71614">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnolN9qOV4hyEhNBOA1thcfy-LMqfd6oHp6yT7D9maN8Qpbl9MUpxDiwxSfSxUg79pP0vVLtrnrDTujufwPQ2cuHSBofMovu6eSPluDi-_JEmDetQouvto0A3g8MBuTXIQzWcAovo2VzZuHaIxM76a0ReEY1_GXeu5SQVqO-yKv_Seu8xzOHJ7I0LpsfqT6IHkLM_TYk2kEaUtUo9QZPFhmGjIlORmFk1ZUPRGPNF2Vxe-fnk48u4Uw061htMZLiKgE-etRRqHWdY-lSn7SKp4bZYxsZr8AAHopHn6O9bGmQYrVucJBRAdl9neG3aNqmff3BvyLsC3KRJ_P-7G3mwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🇮🇷
🇺🇸
بلومبرگ:
پس از آنکه اتریش تحت فشار دولت ترامپ از ورود محمد اسلامی، رئیس سازمان انرژی اتمی ایران، به این کشور جلوگیری کرد، حضور او در کنفرانس عمومی آژانس بین‌المللی انرژی اتمی در وین منتفی شد.
قرار بود اسلامی روز دوشنبه در این کنفرانس سخنرانی کند؛ اکنون احتمال دارد نماینده‌ای دیگر از ایران در اواخر هفته به جای او سخنرانی نماید.
انتظار می‌رود کریس رایت، وزیر انرژی آمریکا، در این کنفرانس ضمن تأکید بر اینکه «ایران هرگز نباید به سلاح هسته‌ای دست یابد یا آن را تولید کند»، خواستار همکاری کامل ایران با آژانس و دسترسی بازرسان آن شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71614" target="_blank">📅 13:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71613">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=qI0fryDEKhitbxQH-7QgkD5Pk6xeK85uE8PYetEiB4_zaSYlYm_DgAb7QUlq7AZDoGdj_DWbKkcqWOVzi1q3J4Pq0gEC0f2R_BAuGFcd-RU0oTxLfQ202sEdK6q5auKDrkJ7YCxuWcMqHiYMKWU4uLFn1_g3_RZx26AKcyW7qbqnWKfHo4O-GONQ5lTNLUyVyj53wpkQwDvySTXWmA8OwJJIbQaM7q59vBFi2U4aBPr22DWrECdk1yAA0E69IjYZJod7iVGg6ALNd6o04iybTJqSea7wRXxntuHTLkAXsrt7yMhbVhr2Fv3RWIvPF0VcQ2qhhdkeHfupfqi2Kx9nzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=qI0fryDEKhitbxQH-7QgkD5Pk6xeK85uE8PYetEiB4_zaSYlYm_DgAb7QUlq7AZDoGdj_DWbKkcqWOVzi1q3J4Pq0gEC0f2R_BAuGFcd-RU0oTxLfQ202sEdK6q5auKDrkJ7YCxuWcMqHiYMKWU4uLFn1_g3_RZx26AKcyW7qbqnWKfHo4O-GONQ5lTNLUyVyj53wpkQwDvySTXWmA8OwJJIbQaM7q59vBFi2U4aBPr22DWrECdk1yAA0E69IjYZJod7iVGg6ALNd6o04iybTJqSea7wRXxntuHTLkAXsrt7yMhbVhr2Fv3RWIvPF0VcQ2qhhdkeHfupfqi2Kx9nzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇳
سخنگوی وزارت امور خارجه هند در جریان سخنرانی مسعود پزشکیان در اجلاس بریکس در دهلی نو، با خوردن یک‌نفسِ یک ظرف آجیل — شامل خوردن، لیسیدن انگشتان و برداشتن دوباره از ظرف تا زمانی که کارکنان تشریفات آن را گرفتند خبرساز شد
😏
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71613" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71612">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567356c89d.mp4?token=W-yPgwKBCJWydiGwf1D1CMSX-4IsLHq9rtQJ7oILJAqOlMSEhbVjvFMquSYly-P76Zyfif6BCMPHrxJ5fMpxufs5WLew1bYWjnA5Np9eLXfogZ2ih3QL8SxWqehxZL_1HWf1yaeZgR0qZwiGlvxL8yCm-H_HOJEuJ9ZjI-MBoWttkdMh6tlmGsmaXZE8pUNEuDp1KRbM2RMkFgggCY2dnq6WdDQ8Z07bcbiI8oB-hAAKEX82DdQPNNcqMrQ_MMKSpNk4ghgRohPaT59czuOf31hQ-Oqtc88OxiWEgTOuMYYGBJej81FBKkiN2zWwJbAbWx0bup5cnJ5PAd7I0c3g4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567356c89d.mp4?token=W-yPgwKBCJWydiGwf1D1CMSX-4IsLHq9rtQJ7oILJAqOlMSEhbVjvFMquSYly-P76Zyfif6BCMPHrxJ5fMpxufs5WLew1bYWjnA5Np9eLXfogZ2ih3QL8SxWqehxZL_1HWf1yaeZgR0qZwiGlvxL8yCm-H_HOJEuJ9ZjI-MBoWttkdMh6tlmGsmaXZE8pUNEuDp1KRbM2RMkFgggCY2dnq6WdDQ8Z07bcbiI8oB-hAAKEX82DdQPNNcqMrQ_MMKSpNk4ghgRohPaT59czuOf31hQ-Oqtc88OxiWEgTOuMYYGBJej81FBKkiN2zWwJbAbWx0bup5cnJ5PAd7I0c3g4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی:
توافق میان ایران و عمان حاصل هفته‌ها مذاکرات فشرده است و حقوق حاکمیتی هر دو کشور را به‌طور کامل محترم می‌شمارد.
از کشورهای همسایه انتظار می‌رود اختلافات گذشته را کنار بگذارند، برای تقویت امنیت منطقه‌ای گفتگو کنند و نفوذ بازیگران مخرب فرامنطقه‌ای را محدود سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71612" target="_blank">📅 12:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71611">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZGqTpKCpHcRZLgRtq2CtYJVVaM3TTigNMQkibYLBf3AidWKrYMOydIvDo3x--lTeMyqPlW2CcEXFbzA_Rm0alRmvx_AipuavPJqf2jxO3srqh6Dz6DwD6pWJWQ44s_Y2-cMqLrW4PxMvwxNV0rU6VjS58b3Ojr-hsoUhN2zmF7zWAQwti_cjhPF78JEB0DEUzrGe2jgUiXRgLHvPzCdqfWk-fOVs4OU3gowx1Xs2Cav2q50db05_zlx_dfQywQPILzrgnAt8oGl5JydbW0ab3y2xgy2lz9FqDIq_uScA7unDAD5XcSsc-Toxclb5K-LGx8r3D__HexTg0Ma-aVxDVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه دختر شماره یه پسرو که روش کراش داشته داده رفیقش، و رفیقش تو نیم ساعت این اطلاعات رو از پسره درآورده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71611" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71610">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71610" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71609">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBhDtu38vsHSdOTAv0fJpbOo0kcUGivtT2y6eowOOkTopD1ORPZMItwU3dOTRjIlEd4BCzLqdZ_m-ZKZfCYfvGbVBF9eraULkphVlJxEBX-8GkYLuMyoaPs38Xg9ydWyHxohNSgwti4N0tz-gRzeXu6H5N4z834kYL6S9UhL1haZ3Qm9o5wG9ZlFecUsa9BGIvWoOCiQRSSkrW7W4_P0A2h55zDvIdtszlMnlYGwa9swQ0Zw7dKDe_0UR7GJIdOc3d2ks_0MNQelKhrraE51zttJf4jriHHx_2kC4zzaqJ0UQszOMqNJTNrUec3zB4GpPlTqa_pzuHxzJbCLk2L7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
لیدز
رم
🆚
تورینو
اودینزه
🆚
اینتر
السد
🆚
استقلال
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71609" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71608">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001bfae793.mp4?token=l8iy-dYamoz1MWsfBffP49AwxMOtpTjgSkRD_yIrE_eR31DVF9Vy2zvieoPe4qD7nXb8aE7w9Cg_umfTc-Jy3Bnhh7Tq6nwZwNaP-34_YdlF4D06cALdELQlrAftt-DxoSBi3EjU-RCliQ86WR06RxRXCesbOkCkNYr7_mUB07dAHB0gVlY2IZTM3Z3zAVFgAMqU0zyMMZeDb-ubCRDzKHizdVBfJ6YIYn_dPBefWSiHPlIG9_5knJ7me9pS5O42QGnwtoNPqbuwvw8yObcvOM4nTwrBaaCPWITGMRUc_GpqhZfJ9Z_TQvmPUgEZWjaSbXoFpRGSyFd54s9cTAQXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001bfae793.mp4?token=l8iy-dYamoz1MWsfBffP49AwxMOtpTjgSkRD_yIrE_eR31DVF9Vy2zvieoPe4qD7nXb8aE7w9Cg_umfTc-Jy3Bnhh7Tq6nwZwNaP-34_YdlF4D06cALdELQlrAftt-DxoSBi3EjU-RCliQ86WR06RxRXCesbOkCkNYr7_mUB07dAHB0gVlY2IZTM3Z3zAVFgAMqU0zyMMZeDb-ubCRDzKHizdVBfJ6YIYn_dPBefWSiHPlIG9_5knJ7me9pS5O42QGnwtoNPqbuwvw8yObcvOM4nTwrBaaCPWITGMRUc_GpqhZfJ9Z_TQvmPUgEZWjaSbXoFpRGSyFd54s9cTAQXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤡
مجری صداوسیما:
اصلا نگران نباشید اوستاد خوش‌چشم مجدد توی برنامه ها شرکت خواهند کرد و انقد پیام ندید و مارو نوازش نکنید که چرا اوستاد چند وقته نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71608" target="_blank">📅 12:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71607">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=gRJ3sJ0ylOWA3qZJgZrRRJl_DPQ1_1lK68OnL4zWX3WpS3Nw6KI3hREb6K17pryWdwexA3W7lc5y43TGBamjAYZ0JJX96HqDsOvlurEqC49az5eZlf6cLP9d-fJL1GPzJUwzD0pfT7czMT1uJW62Q9sAjcU2eI8U8u-WK6z8J5oIKrRvzRzAfIlOH-5TbrP5cBgRMzUeXwBnGnd3NEsOsvE-45hIg5Olzol92UZT03RAD3_68K9O8lUfDS93wVemBPlSLCuh2IrhwOxZpfV-JT2qvkesvTCwMx_Izb5_XnKIuGwigX3KP8YUYYCg6mZpA9fTZvQ0PxXqqlmbir7D4gJ2UyuqvEJZrGou47ATD68HBLlee6IbQctIBHSI5AvpJ31FNTkH0Xn28rW0utsi23SprSQhPRpETkEFtOB7EmdXW41wMzwYfbAssmDFiFgBkn9_ISMkBwaYieqenhcSRJ0-i5mYSVnm2SyFg-I60QEFUuO7bM8xd-8tf0f1Po1Rsp1A28cGd1J67eFNApc8LT5Fuc6ShUb1NTISEb1o1hy4M5OjdoVAPgJtPSqi3ZRV-nt7iLYPqCkmUbPW551t-L5P9U9FzH6E4dKbC8cpf9K8v14OTTqQIql_t5QihSB61QzyvaT5xyD4mfaGuLCXUDOmOctrECImyrakMUzSdgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=gRJ3sJ0ylOWA3qZJgZrRRJl_DPQ1_1lK68OnL4zWX3WpS3Nw6KI3hREb6K17pryWdwexA3W7lc5y43TGBamjAYZ0JJX96HqDsOvlurEqC49az5eZlf6cLP9d-fJL1GPzJUwzD0pfT7czMT1uJW62Q9sAjcU2eI8U8u-WK6z8J5oIKrRvzRzAfIlOH-5TbrP5cBgRMzUeXwBnGnd3NEsOsvE-45hIg5Olzol92UZT03RAD3_68K9O8lUfDS93wVemBPlSLCuh2IrhwOxZpfV-JT2qvkesvTCwMx_Izb5_XnKIuGwigX3KP8YUYYCg6mZpA9fTZvQ0PxXqqlmbir7D4gJ2UyuqvEJZrGou47ATD68HBLlee6IbQctIBHSI5AvpJ31FNTkH0Xn28rW0utsi23SprSQhPRpETkEFtOB7EmdXW41wMzwYfbAssmDFiFgBkn9_ISMkBwaYieqenhcSRJ0-i5mYSVnm2SyFg-I60QEFUuO7bM8xd-8tf0f1Po1Rsp1A28cGd1J67eFNApc8LT5Fuc6ShUb1NTISEb1o1hy4M5OjdoVAPgJtPSqi3ZRV-nt7iLYPqCkmUbPW551t-L5P9U9FzH6E4dKbC8cpf9K8v14OTTqQIql_t5QihSB61QzyvaT5xyD4mfaGuLCXUDOmOctrECImyrakMUzSdgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ℹ️
باز و بسته کردن (مونتاژ و دمونتاژ) کلاشنیکف AK-74 توسط این بانوی روس
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71607" target="_blank">📅 11:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71606">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
اگه نیسان کشنده ندیده بودی
این ویدیو رو ببین تا ببینی همچی توی ایران ممکنه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71606" target="_blank">📅 10:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71605">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=frw9o4l4RdsT9FsAGqN2YqABz5lXje5hXr3IBo9InkQMAsmMPl7SC9jeR97mYupur-M9NgREyKeGP1DyxqOgVnN5_mNrwKt8Nkl_cYqFww6y9gyk_kofrNc2bHhI4ZIhq52Tr4itCs0GGbrezXGidRI5gqIM1Y0t_O2WPH-Zsn8g3lYit90YzHazcu2l2sOIB8KFe1DO4_RWe6yoPU5yP-7nHw15_oFVfPASOOgec1i48gNAZHikgmnQf4_eHe0EuHCkT8O6-f-G0jWsDSvGtcRo5fW2CZINB4Uv6zdaqjUt0SRaBYua2zX4AHJY23rVKB93nFN5-G0Ka2Qs5vbvdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=frw9o4l4RdsT9FsAGqN2YqABz5lXje5hXr3IBo9InkQMAsmMPl7SC9jeR97mYupur-M9NgREyKeGP1DyxqOgVnN5_mNrwKt8Nkl_cYqFww6y9gyk_kofrNc2bHhI4ZIhq52Tr4itCs0GGbrezXGidRI5gqIM1Y0t_O2WPH-Zsn8g3lYit90YzHazcu2l2sOIB8KFe1DO4_RWe6yoPU5yP-7nHw15_oFVfPASOOgec1i48gNAZHikgmnQf4_eHe0EuHCkT8O6-f-G0jWsDSvGtcRo5fW2CZINB4Uv6zdaqjUt0SRaBYua2zX4AHJY23rVKB93nFN5-G0Ka2Qs5vbvdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست سلاح جنگی بر روی شتر توسط یک عرب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71605" target="_blank">📅 10:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71604">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=XoAUgeAInDroAxIbDVx6euSRZztZS92PnsAEWvB9kBGb0Ou9IQnUudLXM95oLh4EjSwXBz1uT-QEyQ6oxJMa-iar1x__ORpdI7rmBLPYlZIXDHKAQsXmkhFgswrTEMRSuL7ReHdv_ZOsJdX2UKmEjoHtxNSzuBSVP2wPJ6wE-Z7R24BK6L9-GO_GRa8DNrxKcw_IfMI06MWRQKoGJ3USR9VKgV-gIuDnhHjyMYqw6PBXukgEz08jxKvY1ytVYZnGSGqtS98lGg1tbrx0XvYou4w0kBwI6BgpF3lhzDCgtwFiWy7th6oX1by-qrZOvKwl49-S7rafaiepZTEXVeK13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=XoAUgeAInDroAxIbDVx6euSRZztZS92PnsAEWvB9kBGb0Ou9IQnUudLXM95oLh4EjSwXBz1uT-QEyQ6oxJMa-iar1x__ORpdI7rmBLPYlZIXDHKAQsXmkhFgswrTEMRSuL7ReHdv_ZOsJdX2UKmEjoHtxNSzuBSVP2wPJ6wE-Z7R24BK6L9-GO_GRa8DNrxKcw_IfMI06MWRQKoGJ3USR9VKgV-gIuDnhHjyMYqw6PBXukgEz08jxKvY1ytVYZnGSGqtS98lGg1tbrx0XvYou4w0kBwI6BgpF3lhzDCgtwFiWy7th6oX1by-qrZOvKwl49-S7rafaiepZTEXVeK13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
زنده یاد مانوک خدابخشیان:
تنها برگ برنده دونالد ترامپ این است که پرونده رژیم جمهوری اسلامی بسته شود. این بزرگترین پیروزی است، درست مثل فروپاشی شوروی؛ این را فراموش نکنید.
چرا او باید وارد جنگی شود که سال‌ها طول بکشد و دوباره در باتلاق خاورمیانه بماند؟
هدف این است که از خاورمیانه بیرون بیاید.
شما به اصطلاح آن دکه جمهوری اسلامی را ببندید، همان‌طوری که دکه کمونیسم بسته شد و همه فرو ریختند، تمام این‌ها هم فرو خواهند ریخت.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71604" target="_blank">📅 10:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71603">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
لحظاتی قبل یک فروند پهپاد پیشرفته MQ۱ توسط سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور بر فراز آسمان تنگه هرمز رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71603" target="_blank">📅 09:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71602">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
یه ایرانی رفته توی تجمعات حامیان فلسطین توی خارج و بهشون میگه <<کص ننت فلسطین>> یعنی فلسطین رو دوس دارم
😂
اونا هم بدون اینکه معنیشو بدونن دارن تکرار میکنن
در ادامه میگه فلسطین رو از حماس آزاد کنید
در آخرم شعار جاویدشاه رو سر میده
👑
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71602" target="_blank">📅 09:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71601">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
مصاحبه کامل و ترجمه شده افسر تسلیحات نجات یافته ملقب به "براوو Bravo" با برنامه Minutes 60 پیرامون عملیات CSAR که در ماه آوریل در عمق خاک ایران انجام شد.
@News_Hut
|Cataphract1</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71601" target="_blank">📅 09:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71600">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
⭕️
تصاویر تازه‌منتشرشده‌ای که توسط برنامه «۶۰ دقیقه» (60 Minutes) پخش شد، عملیات نجات دو افسر نیروی هوایی ایالات متحده را نشان می‌دهد؛ افسرانی که با نام‌های عملیاتی «آلفا» و «براوو» شناخته می‌شوند و جت جنگنده F-15E آن‌ها در ماه آوریل بر فراز ایران سرنگون شده بود.
این دو نفر در حالی که نیروهای ایرانی در جستجوی آن‌ها بودند، در منطقه‌ای کوهستانی در جنوب اصفهان و با فاصله‌ای حدود پنج مایل از یکدیگر فرود آمدند. در این گزارش همچنین تصاویری از حمله به نیروهای ایرانی به نمایش درآمد.
آلفا» هشت ساعت پس از خروج اضطراری (اجکت) از هواپیما، طی یک عملیات پرخطر در روز که با مشارکت ۲۱ فروند هواپیمای آمریکایی انجام شد، نجات یافت.
«براوو» حدود دو روز در پشت خطوط دشمن باقی ماند. او با وجود شکستگی کمر و سایر جراحات ناشی از فرود سخت (به‌دلیل نقص در چتر نجات)، از یک خط‌الرأس کوهستانی به ارتفاع ۷۰۰۰ پا بالا رفت تا اینکه دو تن از نیروهای ویژه امداد و نجات نیروی هوایی به او رسیدند و وی را به بالگرد آمریکایی منتقل کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71600" target="_blank">📅 07:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71599">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71599" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71599" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71598">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrlKxYcO4zXSbqKbh5yRZFWZjRVy5hgJqcBjQJrpM1gcArkG_0HH5B5_UkigOgEKpKXLiyxOx_oD_QD4-cV5JLwWSq8ZiMsEBeihvG0lRWq5pmDOiz9kICut96l_e1b4qZJs9NGdvVmOBjfDAgRI1Zzr52PmiPwfgp-815NiXcO_ltF85YLwt1ifbBP1GZW6aoTgTPKSH_PMYJUXjTRrvnvWmLlj90arMUkwGHmzuGrI9-pQFfpuMS-lW3-Y6N4VF1H71bWbsszFMfK3hlDRWRMzOSBnxTxa_5b5jKW8FEapHb-KOWJP3Mqy2yldDM4NiY57qiBtXfW1nd7OROFhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71598" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71597">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=D5TZ8cJ4S2Uqg3D4NZ6_W6YUK5vsOe33vPebhbG2vzp1bMHdIKKV3ySMU9UMrxeUZ2o5rhOqnaWD1maCorrLH6EaSV3Wuhluy4WOr2kBSeec10_fYdnytZG0QEAtKKiXqn-lf6uiKuqJ1QdhcMkufMK6ps0p39QGNA7WI9LYnAUAY_ayQAS2wsH6IbYkEvkFbFqx-V5QBNOihc3BIZu1JOExNjF8Jp0AbG-wGnaOs-8sU-_3EVyVDU0-ujnkif3hURaHcvJ5KiJeCsiWQcpPh2eFws-BKPbfLpzhPzmvL4MaN2l6i4RDI6LYM7npQ-7pCijlYnPRzCLfwbv4_NSwHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=D5TZ8cJ4S2Uqg3D4NZ6_W6YUK5vsOe33vPebhbG2vzp1bMHdIKKV3ySMU9UMrxeUZ2o5rhOqnaWD1maCorrLH6EaSV3Wuhluy4WOr2kBSeec10_fYdnytZG0QEAtKKiXqn-lf6uiKuqJ1QdhcMkufMK6ps0p39QGNA7WI9LYnAUAY_ayQAS2wsH6IbYkEvkFbFqx-V5QBNOihc3BIZu1JOExNjF8Jp0AbG-wGnaOs-8sU-_3EVyVDU0-ujnkif3hURaHcvJ5KiJeCsiWQcpPh2eFws-BKPbfLpzhPzmvL4MaN2l6i4RDI6LYM7npQ-7pCijlYnPRzCLfwbv4_NSwHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سپاه به طرف تنگه هرمز موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71597" target="_blank">📅 01:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71596">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hml5Y4ATPFFIJkrZ9YFmyhDyd9Ihf1mMK5fO00mFgjlXw9i8eMLkmo39_rJe_Siekc0eUgXer1lV9iiqcomhdqBPTbU0CoOfSKYDfIKPm19z_wJNb1UU9db116h3Tv3NCg4YjjG_pWXjVPXgCn-WvUefoV6nWBxuRmYU2bHkcUpyhkf5QP4DPEcga1Kipm_5EWh9I1lSabIKZ57xdAMxr5WMfA9EOufrUloL10Du__WoniwlRA3hE4cU0pc-LOaqHGpTD52liqkpjbU__BasaetEMD9r4D1uwj0NxW9mU8oR_qCLkkON7xlhaSujvp5hENjdMyDjYOoFy5KqrMA9PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
❌
🇮🇷
🇴🇲
باراک راوید:
یک مقام حوزه خلیج فارس به من گفت که عربستان سعودی اصلاحاتی را در طرح پیشنهادی عمان و ایران در خصوص تنگه هرمز ارائه کرده است؛
زیرا نگران بود که عبارات پیشنهادی عملاً منجر به ایجاد وضعیت موجود جدیدی در این تنگه شود که برای این کشور یا سایر کشورهای عضو شورای همکاری خلیج فارس قابل قبول نباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71596" target="_blank">📅 01:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71595">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=WIU7ei2ZmVDybnh__XtYmdN_FGm-ahJvQ0P2AVlFdd3C2BWBbeSPtg-U_h9efcZtLNU0F2VRsMfPmnDJs3_PFhWphOsP37750TqCLEbQsB83MUKqxTzVIwfZo95519T9LilLB74gwNqP_HHk-6n8pTtmaPDY7g7f5APqdACJ8zLlKaO1kvEbINeTFyxcZ0nZ836Auykb3ziuHesvW7LcWud_BtYE2BOgldxS0Fd6ZLcL5snW9D_j-qv8xF0WH2wzQ2VrM1TQaPbRKEgLpbU3F16pUPelotyH55kRt5UV-Roa9otNGbVk8QDPeQPXAl1uUc6eGfYau6atpbCRnjU56w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=WIU7ei2ZmVDybnh__XtYmdN_FGm-ahJvQ0P2AVlFdd3C2BWBbeSPtg-U_h9efcZtLNU0F2VRsMfPmnDJs3_PFhWphOsP37750TqCLEbQsB83MUKqxTzVIwfZo95519T9LilLB74gwNqP_HHk-6n8pTtmaPDY7g7f5APqdACJ8zLlKaO1kvEbINeTFyxcZ0nZ836Auykb3ziuHesvW7LcWud_BtYE2BOgldxS0Fd6ZLcL5snW9D_j-qv8xF0WH2wzQ2VrM1TQaPbRKEgLpbU3F16pUPelotyH55kRt5UV-Roa9otNGbVk8QDPeQPXAl1uUc6eGfYau6atpbCRnjU56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
ایران می‌گوید دیشب به یکی از شناورهایش حمله شده است. آیا کار آمریکا بود؟
🇺🇸
ترامپ:
نمی‌خواهم بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71595" target="_blank">📅 00:58 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
