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
<img src="https://cdn4.telesco.pe/file/LFcuQXxrf274e7JT5cOiGo5yQyWuJw5afbfTOptWp3lSN3CrQeIKnUsonMOYbJL8CUv-8HFeFHswsF-atpVCPdGK_cFux9kDymmZnY9RPzW7xE5kUxnNtvGoucj9tQMFM9BhdpgVMg24mKAUkQ_C1Gazr7AFWkEu3Dka5OGgn_W0FoCdAzsyhiqusGo13bS18ZHDh-o3ZslMEqqOTHNS61pqWJY1vaZXD_eQbtjTH9nb_ehqrTT8TxzC-Ikl_I2jzmTeRz7iKL4TclgE-CPtcMKMi_5lkMFJHhux7l4Cpff0Ql9rTSO44G5iPRHTFBDFt3Go5AlKDj8b4aBS3nsxVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 283K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 18:12:19</div>
<hr>

<div class="tg-post" id="msg-13053">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">متن چکیده نسخه  ۱۵    بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی  شاهزاده گرامی، این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت…</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/withyashar/13053" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13052">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/withyashar/13052" target="_blank">📅 17:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13051">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">متن چکیده نسخه  ۱۵
بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی
شاهزاده گرامی،
این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و ایجاد مسیر عملی برای آینده ایران ارائه می‌شود.
در شرایط کنونی، جامعه ایران تحت فشارهای شدید اقتصادی، اجتماعی، امنیتی و سیاسی قرار دارد و یکی از مهم‌ترین چالش‌ها، نبود یک ساختار منسجم و قابل فهم برای سازماندهی ظرفیت عظیم مردمی است.
1. ضرورت ایجاد ساختار یا پلتفرم سازماندهی ملی
مطالبه گسترده مردم، ایجاد یک ساختار منسجم است که بتواند نیروهای مردمی داخل و خارج کشور را شبکه‌سازی کرده، نقش‌ها را مشخص کند و از پراکندگی و موازی‌کاری جلوگیری نماید.
2. انسجام و اتحاد میان جریان‌های مختلف مخالف
درخواست جدی جامعه، ایجاد سازوکاری برای همگرایی جریان‌ها و گروه‌های مختلف مخالف حکومت است تا انرژی سیاسی و اجتماعی در مسیر مشترک و هماهنگ قرار گیرد.
3. ضرورت اعلام چارچوب زمانی و نقشه راه عملی
یکی از دغدغه‌های اصلی مردم، نبود زمان‌بندی و مسیر روشن برای اقدامات جمعی است.
مطالبه عمومی این است که سناریوها و مراحل حرکت به‌صورت شفاف و مرحله‌بندی‌شده مشخص شوند و در صورت امکان، برای اقدامات جمعی و هماهنگ، چارچوب‌های زمانی روشن و قابل فهم اعلام گردد.
4. آمادگی میدانی و سازوکارهای حمایتی در شرایط بحران
بخش قابل توجهی از پیام‌ها بر ضرورت ایجاد سازوکارهای حمایتی و سازمانی برای شرایط بحرانی تأکید دارد تا از طریق شبکه‌های امن، هماهنگی اجتماعی و توانمندسازی، هزینه انسانی تحولات کاهش یابد.
⸻
5. تقویت ساختار مشورتی، ارتباطات و شفافیت عملکرد
یکی از مطالبات اصلی، تقویت همزمان ساختار مشورتی، ارتباطی و شفافیت عملکرد است.
در این چارچوب پیشنهاد می‌شود:
گسترش تیم مشاوران و کارشناسان در حوزه‌های مختلف از جمله سیاسی، اقتصادی، اجتماعی، رسانه‌ای و امنیتی
استفاده از متخصصان حوزه امنیت، مدیریت بحران و مطالعات راهبردی در کنار سایر تخصص‌ها
تقویت و حرفه‌ای‌سازی نقش رسانه‌ای و ارتباطی
ایجاد ارتباط مستمر و مؤثر با مردم و مشارکت گروه‌های مختلف اجتماعی
فراهم کردن زمینه ورود دیدگاه‌ها و ایده‌های جدید از جریان‌های تخصصی و فکری مختلف
افزایش شفافیت در عملکرد و تصمیم‌گیری‌ها همراه با گزارش‌دهی منظم
هدف از این پیشنهادها، افزایش اعتماد عمومی، ارتقای کیفیت تصمیم‌سازی و تقویت هماهنگی میان ظرفیت‌های مختلف جامعه است.
6. معیشت و وضعیت اقتصادی مردم
در کنار موضوعات سیاسی، بحران معیشتی یکی از اصلی‌ترین فشارهای روزمره مردم است.
درخواست عمومی این است که در کنار برنامه‌های کلان،
راهکارهایی برای کاهش فشار اقتصادی و حمایت از اقشار آسیب‌پذیر در حال حاظر
نیز در نظر گرفته شود.
7. ارتباط مستقیم‌تر با جامعه و گروه‌های مختلف
مردم خواستار ارتباط فعال‌تر، مستقیم‌تر و مستمرتر میان رهبری اپوزیسیون و بدنه اجتماعی هستند تا اعتماد، شفافیت و هماهنگی افزایش یابد.
جمع‌بندی
در مجموع، پیام مشترک این دیدگاه‌ها چنین است:
جامعه ایران آماده تغییر است، اما این مسیر تنها با انسجام، شفافیت، ساختار اجرایی روشن و ارتباط واقعی با مردم امکان‌پذیر است.
⸻
درخواست پایانی (از طرف جمع امضاکنندگان)
در پایان، جمعی از امضاکنندگان و نمایندگان این دیدگاه‌ها، با نهایت احترام درخواست دارند امکان ارتباط مستقیم برای انتقال منظم دیدگاه‌ها، هماهنگی بیشتر و ادامه گفت‌وگو فراهم گردد و پاسخ این پیام  ارسال شود.
این جمع، جناب آقای
یاشار
را به عنوان نماینده و پیگیر دیدگاه‌های مردم معرفی می‌نماید.
راه‌های ارتباطی:
….
پاینده ایران
و درود بر خاندان ایران‌ساز پهلوی
@withyashar</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/withyashar/13051" target="_blank">📅 17:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13050">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205d44aab0.mp4?token=noRaik09ZdDyN2ygdGcuwRPJ8l9OcEWd7NXTJbQ4MytgAt9wCglzJ8rmy20w1QQ0xzUd2cxzSmNjS-X1pORwKMZQ0Cf_8wZUWMZ1fQHXZ86e2sAyAvTUa6j3qXlYZ8gMIofJEx1oWRLNvBdeoYdz3xXXW6Hd45PAcrdB5SzqYpgTJ7UyTnGyJ5-HcxKYd2uQiY5dS1iWRzyZ1Gp6xQipCWWkBD-7yEgNkrizcOnW6H95E8OkCAYR0LoDuPpoabvTASHeeuW-qD4VY7a0yLEW1e3j4t2i20m84DQzzXuApD5lKGSpXisgYbyHRNXmwuAZYam2lmIJm-PCPywRv30ESw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205d44aab0.mp4?token=noRaik09ZdDyN2ygdGcuwRPJ8l9OcEWd7NXTJbQ4MytgAt9wCglzJ8rmy20w1QQ0xzUd2cxzSmNjS-X1pORwKMZQ0Cf_8wZUWMZ1fQHXZ86e2sAyAvTUa6j3qXlYZ8gMIofJEx1oWRLNvBdeoYdz3xXXW6Hd45PAcrdB5SzqYpgTJ7UyTnGyJ5-HcxKYd2uQiY5dS1iWRzyZ1Gp6xQipCWWkBD-7yEgNkrizcOnW6H95E8OkCAYR0LoDuPpoabvTASHeeuW-qD4VY7a0yLEW1e3j4t2i20m84DQzzXuApD5lKGSpXisgYbyHRNXmwuAZYam2lmIJm-PCPywRv30ESw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از یه زاویه دیگه اتوبان ستاری ,جنت آباد جنوبی
@withyashar</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/withyashar/13050" target="_blank">📅 17:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13049">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69bcf1699.mp4?token=TuK1q0ZRB0AfSX573X_2KdSO1aO6Bz4XscxpVJQCbtOESboK25ITyKSPX3vrqUBh01NmReN44FCFVUmXG35KXMraUiG3jzteZcRbz_fzuAc2huwgLnkX4JlZKa3prWlMjNDRTuGI3uGlg-CIuD-LML0rdt1RqIk-hEv12vS6Zc32abeMaEToeOM0HUo5KJ0X55u8DTMqf2hSu90UKCra-KfQ0YsVYzqYl6iagrbEtlGxaPQ4lbu1M-1uWNvIIMkGkcrSNcGGiXbhRit3f55E3zfFLDh7JZP4ME4w_0UC455mSewvFqHi-2U3GDAYemgu4iB_d5BHW9K2feiY5SqRBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69bcf1699.mp4?token=TuK1q0ZRB0AfSX573X_2KdSO1aO6Bz4XscxpVJQCbtOESboK25ITyKSPX3vrqUBh01NmReN44FCFVUmXG35KXMraUiG3jzteZcRbz_fzuAc2huwgLnkX4JlZKa3prWlMjNDRTuGI3uGlg-CIuD-LML0rdt1RqIk-hEv12vS6Zc32abeMaEToeOM0HUo5KJ0X55u8DTMqf2hSu90UKCra-KfQ0YsVYzqYl6iagrbEtlGxaPQ4lbu1M-1uWNvIIMkGkcrSNcGGiXbhRit3f55E3zfFLDh7JZP4ME4w_0UC455mSewvFqHi-2U3GDAYemgu4iB_d5BHW9K2feiY5SqRBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبروی پاساژ کوروش
@withyashar</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/withyashar/13049" target="_blank">📅 17:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13048">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اصلاح ۵ بخش ۵
5. تقویت ساختار مشورتی، ارتباطات و شفافیت عملکرد
یکی از مطالبات اصلی، تقویت و گسترش ساختار مشورتی و ارتباطی در کنار افزایش شفافیت عملکرد است.
در این چارچوب پیشنهاد می‌شود:
تیم مشاوران و کارشناسان در حوزه‌های سیاسی، اقتصادی، اجتماعی، رسانه‌ای و همچنین حوزه‌های مرتبط با امنیت و مدیریت بحران تقویت و گسترش یابد
نقش رسانه‌ای و ارتباطی به‌صورت حرفه‌ای‌تر و منسجم‌تر ارتقا پیدا کند
امکان ارتباط مستمر و هدفمند با مردم و گروه‌های مختلف اجتماعی فراهم شود
از متخصصان حوزه
امنیت، مدیریت بحران و مطالعات دفاعی
در کنار سایر حوزه‌های تخصصی استفاده شود
زمینه ورود ایده‌ها و دیدگاه‌های جدید از جریان‌های فکری و تخصصی مختلف ایجاد گردد
شفافیت در عملکرد، روند تصمیم‌گیری‌ها و مسیرهای حمایتی (از جمله رسانه‌ای و سازمانی) افزایش یابد و گزارش‌دهی منظم در دستور کار قرار گیرد
هدف از این مجموعه پیشنهادها، افزایش اعتماد عمومی، ارتقای کیفیت تصمیم‌سازی و تقویت هماهنگی میان ظرفیت‌های مختلف جامعه است.
@withyashar</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/withyashar/13048" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13047">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/withyashar/13047" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13046">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش WSJ: سازمان ملل در حال ورشکستگی است، زیرا ایالات متحده و چین میلیاردها دلار را از این نهاد بین‌المللی خارج کرده اند
@withyashar</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/withyashar/13046" target="_blank">📅 17:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13045">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/withyashar/13045" target="_blank">📅 16:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13042">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cau7M3lQeNENkUFBrqdU-oZsfBQF41ocuBn5RrsooygktkVcEVoBv7GKk3yi3-FVinPhGXHUYke89MLmcSlx5vifpp5E9Gzw-6VcBZQrSmD2RPo5spnHAZu6MPQPjXu9W3bJmFHqb5YrTe7WtmRGCW-CwR8SYWCTmTf_RGvThVsnhEW_6t1fnXDv22_xTt9uyh0QUSgeAm1aBMFMSO6hjzL8o1v6QsYecKG-FqpaMSIiZS8UYpxcRULcQTkBXxcHdyZpAia7_MAtojiqYXwWY0o5neNZgyLmUHxG4xZ3Yg_LBahFy0tlMKpRmO7GFawijJktDO8V3TPSN3rztFkBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان آتش‌سوزی غرب تهران سمت ستاری
@withyashar</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/withyashar/13042" target="_blank">📅 16:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13041">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/withyashar/13041" target="_blank">📅 16:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13040">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/withyashar/13040" target="_blank">📅 16:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13039">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سی‌ن‌ان: ایران ۵۰ ورودی از ۶۹ ورودی تونل‌های تاسیسات هدف قرارگرفته موشکی را باز کرده است
@withyashar</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/13039" target="_blank">📅 16:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13038">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سی‌ان‌ان: برای وارد کردن آسیب به تاسیسات موشکی ایران باید از سلاح‌های بسیار پیچیده و بسیار گران‌قیمت استفاده کرد، اما عملیات بازیابی با فناوری بسیار ساده‌ای انجام می‌شود، فقط با بولدوزر
@withyashar</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/13038" target="_blank">📅 16:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13037">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">متن چکیده نسخه ۲
بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی
شاهزاده گرامی،
این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و ایجاد مسیر عملی برای آینده ایران ارائه می‌شود.
در شرایط کنونی، جامعه ایران تحت فشارهای شدید اقتصادی، اجتماعی، امنیتی و سیاسی قرار دارد و در کنار آن، یکی از مهم‌ترین چالش‌ها، نبود یک ساختار منسجم و قابل فهم برای سازماندهی ظرفیت عظیم مردمی و تبدیل آن به یک نیروی هماهنگ است.
⸻
1. ضرورت ایجاد ساختار یا پلتفرم سازماندهی ملی
مطالبه گسترده مردم، ایجاد یک ساختار یا پلتفرم منسجم است که بتواند:
نیروهای مردمی داخل و خارج کشور را شبکه‌سازی کند
وظایف و نقش‌ها را مشخص و قابل اجرا نماید
از پراکندگی و موازی‌کاری جلوگیری کند
مسیر فعالیت گروه‌ها و افراد را شفاف و هدفمند سازد
امکان هماهنگی عملی در سطح رسانه‌ای، اجتماعی و میدانی را فراهم کند
⸻
2. انسجام و اتحاد میان جریان‌های مختلف مخالف
درخواست جدی جامعه، ایجاد سازوکاری برای
همگرایی و هماهنگی میان گروه‌ها، جریان‌ها و افراد مختلف مخالف حکومت
است تا:
اختلافات مانع حرکت مشترک نشود
یک محور هماهنگ‌کننده واحد وجود داشته باشد
انرژی سیاسی و اجتماعی هدر نرود
⸻
3. ضرورت اعلام چارچوب زمانی و نقشه راه عملی
یکی از مهم‌ترین دغدغه‌های مردم، نبود زمان‌بندی روشن برای مراحل مختلف حرکت سیاسی است.
مطالبه عمومی این است که:
سناریوهای مختلف به‌صورت شفاف و مرحله‌بندی‌شده مشخص شوند
برای اقدامات جمعی،
چارچوب زمانی تقریبی یا بازه‌های مشخص تصمیم‌گیری و اقدام
اعلام شود
مردم بدانند در هر مرحله چه انتظاری باید داشته باشند و نقش آنها چیست
همچنین بخش مهمی از جامعه خواستار آن است که در صورت وجود شرایط مناسب،
فراخوان‌های مشخص، هدفمند و زمان‌دار
برای اقدامات جمعی و هماهنگ صادر شود تا انرژی اجتماعی به‌صورت پراکنده و فرسایشی از بین نرود.
⸻
4. آمادگی میدانی و سازوکارهای حمایتی در شرایط بحران
بخش قابل توجهی از پیام‌ها بر ضرورت ایجاد سازوکارهایی برای حمایت از مردم در شرایط بحرانی تأکید دارد؛ به‌گونه‌ای که:
شبکه‌های حمایتی و سازمانی امن شکل گیرد
هماهنگی میان نیروهای مردمی افزایش یابد
آمادگی اجتماعی و مدنی برای شرایط حساس تقویت شود
هزینه انسانی تحولات احتمالی کاهش یابد
⸻
5. شفافیت در ساختار مشاوران و تیم تصمیم‌سازی
یکی از مطالبات مهم، شفاف‌تر شدن ساختار مشاوران و نقش افراد در حلقه تصمیم‌گیری است تا:
جایگاه افراد مشخص باشد
اعتماد عمومی تقویت شود
از ابهام و چندصدایی غیرسازنده جلوگیری گردد
⸻
6. معیشت و وضعیت اقتصادی مردم
در کنار موضوعات سیاسی، بحران معیشتی یکی از اصلی‌ترین فشارهای روزمره مردم است.
درخواست عمومی این است که در کنار برنامه‌های کلان،
راهکارهایی برای کاهش فشار اقتصادی و حمایت از اقشار آسیب‌پذیر در دوره گذار
نیز در نظر گرفته شود.
⸻
7. ارتباط مستقیم‌تر با جامعه و گروه‌های مختلف
مردم خواستار ارتباط فعال‌تر، مستقیم‌تر و مستمرتر میان رهبری اپوزیسیون و بدنه اجتماعی هستند تا:
ابهامات کاهش یابد
اعتماد افزایش پیدا کند
و امکان هماهنگی واقعی میان گروه‌ها فراهم شود
⸻
جمع‌بندی
در مجموع، پیام مشترک این مجموعه دیدگاه‌ها چنین است:
جامعه ایران آماده تغییر است، اما این مسیر تنها در صورتی به نتیجه می‌رسد که با انسجام، شفافیت، ساختار اجرایی روشن، نقشه راه قابل فهم و ارتباط مستمر با مردم همراه باشد.
⸻
درخواست پایانی (از طرف نماینده جمع)
در پایان، اینجانب یاشار به عنوان نماینده جمعی از این دیدگاه‌ها، با نهایت احترام درخواست دارم امکان
ارتباط مستقیم برای انتقال دیدگاه‌ها و هماهنگی بیشتر
فراهم شود و پاسخ این پیام برای اینجانب ارسال گردد.
راه‌های ارتباطی جهت پاسخ
پاینده ایران ، جاوید شاه
@withyashar</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/13037" target="_blank">📅 15:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13036">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/13036" target="_blank">📅 15:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13035">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خودمو یادم رفت
🥲</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/withyashar/13035" target="_blank">📅 15:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13034">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoheil</strong></div>
<div class="tg-text">یاشار چرا درخواست اینکه با خودت حرف بزنن تا اینارو بگی رو نداریم ؟</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/withyashar/13034" target="_blank">📅 15:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13033">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenyamin Qaem</strong></div>
<div class="tg-text">پس این متن چه اشاره ای به تو داره؟
ما میخایم یاشار با شاهزاده در ارتباط باشه</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/13033" target="_blank">📅 15:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13032">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHannaee</strong></div>
<div class="tg-text">جاوید شاهم بگو یاشار</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/13032" target="_blank">📅 15:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13031">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/withyashar/13031" target="_blank">📅 15:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13030">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">متن چکیده شده نسخه ۱
⸻
بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی
شاهزاده گرامی،
ایرانیان داخل و خارج از کشور، با وجود تفاوت دیدگاه‌ها و تجربه‌های متفاوت، در یک نقطه اشتراک دارند: امید به عبور ایران از وضعیت کنونی و رسیدن به آینده‌ای آزاد، باثبات و شایسته ملت ایران.
در سال‌های گذشته، اعتراضات و جنبش‌های متعدد با هزینه‌های سنگین انسانی و اجتماعی همراه بوده و بخش بزرگی از جامعه همچنان در وضعیت فشار اقتصادی، ناامنی روانی، سرکوب سیاسی و ناامیدی نسبت به آینده قرار دارد. در کنار این شرایط، فضای سیاسی اپوزیسیون نیز از نگاه بسیاری از مردم دچار پراکندگی، نبود انسجام و فقدان نقشه راه عملی و قابل سنجش است.
مطالبه اصلی بخش بزرگی از مردم نه صرفاً شعار، بلکه
وجود یک ساختار روشن، قابل فهم و اجرایی برای گذار سیاسی و دوران پس از آن
است؛ ساختاری که بتواند اعتماد عمومی را حفظ کرده و انرژی اجتماعی را به مسیر مؤثر تبدیل کند.
در همین راستا، مهم‌ترین پیشنهادها و خواسته‌های مشترک به شرح زیر جمع‌بندی می‌شود:
1. ضرورت ارائه نقشه راه روشن و مرحله‌بندی‌شده
بخش بزرگی از جامعه خواستار آن است که مسیر حرکت، شامل اهداف کوتاه‌مدت، میان‌مدت و بلندمدت، به‌صورت شفاف مشخص شود؛ به‌گونه‌ای که مردم بدانند در هر مرحله چه نقشی دارند و نتیجه نهایی چگونه تعریف می‌شود.
2. ایجاد ساختار منسجم و شبیه «دولت در تبعید»
پیشنهاد شده است یک ساختار هماهنگ و چندلایه شامل بخش‌های مختلف شکل گیرد؛ از جمله:
رهبری و شورای مرکزی تصمیم‌گیری
تیم‌های رسانه‌ای داخلی و بین‌المللی
تیم‌های سیاست‌گذاری و برنامه‌ریزی اقتصادی و حقوقی
شبکه‌های ارتباطی و سازماندهی اجتماعی داخل و خارج کشور
تیم تحلیل و نظارت برای ارزیابی عملکرد و اصلاح مسیر
ساختار مقابله با جنگ روانی و عملیات اطلاعاتی
هدف از این ساختار، کاهش پراکندگی، افزایش کارآمدی و ایجاد یک مرجع واحد برای هماهنگی فعالیت‌ها عنوان شده است.
3. شفافیت، اعتمادسازی و گزارش‌دهی
یکی از مطالبات مهم، شفافیت در عملکرد، نحوه تصمیم‌گیری‌ها و مسیرهای حمایتی (از جمله مالی و رسانه‌ای) است. ارائه گزارش‌های منظم می‌تواند اعتماد عمومی را تقویت کرده و مشارکت مردم را افزایش دهد.
4. استفاده از ظرفیت همه اقشار و تنوع اجتماعی ایران
درخواست شده است که نمایندگان اقوام، اصناف، متخصصان، جوانان و گروه‌های مختلف اجتماعی در ساختار تصمیم‌سازی حضور داشته باشند تا احساس نمایندگی و مشارکت واقعی در میان مردم تقویت شود.
5. سازماندهی مشارکت مردمی در داخل و خارج کشور
بسیاری از پیام‌ها بر ضرورت ایجاد شبکه‌های منسجم مردمی در حوزه‌های رسانه‌ای، اجتماعی، مدنی و حمایتی تأکید دارند تا انرژی عظیم پراکنده در فضای مجازی و میدانی به یک مسیر هماهنگ تبدیل شود.
6. تمرکز بر انسجام به جای پراکندگی
یکی از نگرانی‌های جدی، تعدد صداها، اختلافات درونی و نبود فرماندهی واحد در جبهه مخالفان است. درخواست عمومی این است که انسجام، هماهنگی و وحدت عملی جایگزین فعالیت‌های پراکنده شود.
7. ضرورت فعال‌تر شدن ارتباط با افکار عمومی
بخش قابل توجهی از مردم خواستار ارتباط مستمرتر، روشن‌تر و مستقیم‌تر رهبری اپوزیسیون با جامعه هستند؛ به‌گونه‌ای که ابهامات، پرسش‌ها و نگرانی‌ها بدون فاصله زمانی طولانی پاسخ داده شود.
8. آینده‌نگری برای دوران گذار و پس از آن
در کنار موضوع تغییر سیاسی، مردم نسبت به آینده پس از آن نیز دغدغه جدی دارند؛ از جمله ساختار حکمرانی، عدالت، فرصت‌های برابر، توسعه اقتصادی، و جلوگیری از تکرار تمرکز قدرت.
⸻
در جمع‌بندی، پیام مشترک همه دیدگاه‌ها این است که:
جامعه ایران آماده تغییر است، اما این آمادگی نیازمند سازماندهی، شفافیت، برنامه‌ریزی و یک محور هماهنگ‌کننده قابل اعتماد است.
در پایان، این مجموعه نظرات با نیت خیرخواهانه و از سر دغدغه برای آینده ایران ارائه می‌شود و هدف آن تقویت مسیر همبستگی ملی و افزایش کارآمدی حرکت جمعی ایرانیان است.
پاینده ایران
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/13030" target="_blank">📅 15:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13029">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/withyashar/13029" target="_blank">📅 15:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13028">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نتانیاهو: عملیات زمینی در لبنان را گسترش می‌دهیم
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد به ارتش این کشور دستور داده است دامنه عملیات زمینی در لبنان را گسترش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/withyashar/13028" target="_blank">📅 15:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13027">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسرائیل هیوم: ترامپ به دلیل ترس از شکست در انتخابات میان دوره ای جنگ را متوقف کرد و بعد از انتخابات جنگ را ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/13027" target="_blank">📅 15:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13026">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">صدای انفجار در قشم مربوط به یک مین شناور بود که در حال حرکت به سمت یک کشتی بود و آمریکا منفجرش کرد
@withyashar</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/withyashar/13026" target="_blank">📅 15:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13025">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdieh</strong></div>
<div class="tg-text">سلام اقا یاشار ،لطفا به اون اقا یا خانومی که بلوچ هستن بفرمایید  که  من یکی از اون افرادی هستم مه هر ماه برای مردم سیستان پ بلوچستان کمک میفرستم و واقعا ذوسشوت دارم چون واقعا مظلوم واقع شدن و از دیروز که فهمیدم که ۲۴ الی ۴۷ ساعت اب ندارن  انقدر حالم خراب که انگار منم الان اونجام  ،قلبم به درد میاد براشون ،بلوچ هر چی بگه حق داره از بس توو این سال‌های اذیتشون کردن</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/13025" target="_blank">📅 15:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13024">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/13024" target="_blank">📅 15:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13023">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓟</strong></div>
<div class="tg-text">یاشار اگه حوصلشو داری‌ میتونی برای کسایی که جدید اومدن ویس هایی که مهمه تحلیلش برای رسیدن به اون درکی که باید برسیم رو پین کنی که با دیدن پین ها دسترسی سریعتر داشته باشن</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/13023" target="_blank">📅 15:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13022">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from..</strong></div>
<div class="tg-text">مردم ما هیچ اتحادی باهم ندارن اقایاشار از مردم کشورم خیلی دلخورم، من ی بلوچم، الان حتی توو همین مجازی هرکسی ک منو ببینه فقط توهین میشنوم فقط چون بلوچم واقعا خیلی دلم شکسته از هموطنای خودم  اخه چرا مگ ماها ایرانی نیستیم مگ ما چیکارشون کردیم،  ماهم سالهاست داره جوونامون بچه هامون کشته میشن سال هاست زیر ظلم این رژیم هستیم . اصلا قبل همه این داستانا با تمام بدبختی ک داریم  تنهایی جلوشون وایسادیم هیچکس نبود، ازتون میخوام این پیاممو بزارین تو چنلتونن
🙏🏼
تازمانی ک ماها از همدیگ بدمون میاد حتی این رژیمم عوض بشه این کشور هیچوقت درست نمیشه</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/13022" target="_blank">📅 15:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13021">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">روابط‌عمومی ۳پا : صدای انفجار در بندرعباس مربوط به خنثی‌سازی مهمات عمل‌نکرده است.
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/13021" target="_blank">📅 14:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13020">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیویورک‌تایمز: ترامپ شروط توافق احتمالی با جمهوری اسلامی رو سخت‌تر کرده و نسخه اصلاح‌شده رو برای بررسی دوباره به تهران فرستاده.
طبق این گزارش، اختلاف‌ها به‌ویژه بر سر آزادسازی منابع مالی ایران ادامه داره و واشینگتن تلاش می‌کنه با افزایش فشار، روند مذاکرات رو تسریع کنه.
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/13020" target="_blank">📅 14:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13019">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/13019" target="_blank">📅 14:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13018">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPari</strong></div>
<div class="tg-text">به عنوان خردادی میگم حالا که موضوعش پیش اومد
😂
ما اخلاقمون دقیقاااا همون عربس که داره مسافر میبره قاهره
کار خودمونو میکنیما ولی پستی بلندی زیاد داره مسیرمون</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/13018" target="_blank">📅 14:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13017">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دم کسایی‌که حمایت میکنند گرم
🙌🏾
❤️‍🩹</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/13017" target="_blank">📅 14:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13016">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm</strong></div>
<div class="tg-text">ی روز درمیون ب صد نفر میفرستم</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/13016" target="_blank">📅 14:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13015">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm</strong></div>
<div class="tg-text">لینک کانال تلگرامتو</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/13015" target="_blank">📅 14:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13014">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چیزی ‌نیست صدای
“واریز ناموفق: موجودی کافی نیسته!”
@withyashar
🤣</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/13014" target="_blank">📅 14:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13013">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صدای انفجار در قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/13013" target="_blank">📅 14:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13012">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">چندین گزارش صدای مهیب در بندر عباس
@withyashar
🚨</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/13012" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13011">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
دونالد ترامپ ( ۷۹ سال )
۲۴ خرداد ۱۳۲۵
🇺🇸
مارکو روبیو ( ۵۵ سال )
۷ خرداد ۱۳۵۰
🇺🇸
پیت هگست ( ۴۵ سال )
۱۶ خرداد ۱۳۵۹
@withyashar
😃</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/13011" target="_blank">📅 13:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13010">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARSALANVK</strong></div>
<div class="tg-text">یاشار در داخل ایران فاز مردم مثل آب و هوای خردادی هاست واقعا!!! مودی و اصلا مشخص نیست مردم هم خودشون چی میخوان!!!</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/13010" target="_blank">📅 13:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13009">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/13009" target="_blank">📅 13:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13008">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">https://youtu.be/tRWhvFylQtk</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/13008" target="_blank">📅 13:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13007">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سلام خواهشا بگید مگه چندسالتونه ک جام جهانی 1997 هم دیدید..نمیخوره بهتون ک سن بالا باشد</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/13007" target="_blank">📅 13:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13006">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA</strong></div>
<div class="tg-text">سلام خواهشا بگید مگه چندسالتونه ک جام جهانی 1997 هم دیدید..نمیخوره بهتون ک سن بالا باشد</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/13006" target="_blank">📅 13:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13005">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الجزیره: [جنگ آمریکا و اسراییل علیه ایران]، فضایی را ایجاد کرده است که در آن هر دو طرف احساس پیروزی می‌کنند و بنابراین تمایل دارند در مذاکرات احتمالی برای امتیازات بیشتر تلاش کنند و این امر تلاش‌ها برای کاهش تنش را پیچیده می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/13005" target="_blank">📅 12:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13004">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حالا چرا اینا الان نشون دادم ولی کم میذارم؟ یکی این که نگن پس فردا یاشار اومد اینجا، نمیدونم فلان جا بهش پول داد… بدون اینا رو داشت و ول کرد تازه و درس دوم این که بدونن که میتونست بره برای خودش عشقشو کنه کنه، ولی نکرد و قید همه چیز رو زد حتی‌سلامتیشو …. اونایه دیگه خون مردم رو تو شیشه میکنند و هزار جور کار می کنند که تهش شاید بشن این ! شاید !</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/13004" target="_blank">📅 12:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13003">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حس میکنم تریدری
🌚</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/13003" target="_blank">📅 12:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13002">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-text">حس میکنم تریدری
🌚</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/13002" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13001">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فعلا میرم بیرون  یه کاری دارم  به اخبار‌ ادامه میدیم منم یه هوایی بخورم انقدر عصبی نشم…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/13001" target="_blank">📅 12:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13000">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLtpU7EGbgdv4RKZ-Dpui0-0NgRWYn2-57AOm-Z8MJIADBgMPR04pPcrTIyVhOF1-QqFj0Op3kIa4QGPEZ130dxC8uQ7QQMNbUqif_IbysRTNcgHG9icAr6KsD_EazBbRKQ1imgUelJHAgNlSOtXp7IeBLYRP1UR4TdkOKNTe0JuJi6zItHYFrq4xhyQ78zzNsHbzeiemGC9OY-cqYaNx0d7LJOfns6FOOG5YXQ-mjsyPWWWrQ3DOfUkia5qVto2EgkHplLnRRM5D26HgRA9sARhWo1J77TBwolF-_FceUyz6yoNyDdpOEVZH-v6cCqx1i50Z5woJotJpM5Wx2eK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم SVR و G63 البته یه بنتلی GTC W12 و یه مازراتی MC و یه لیموزین بنز ۶ در و یه SL fabdesign هم دارم ، ۶ تا کلا
🥹
حالا به وقتش‌میبینید</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/13000" target="_blank">📅 12:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12999">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مشروب یه کالای‌ مصرفیه ! کل اون مشروبا ۱۵۰۰$ بشه پول یه ماه یه کارگر معمولی اینجا ، البته نه کل مشروبام تو کمد هم باز‌ هست
🤣
…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/12999" target="_blank">📅 12:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12998">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFarham</strong></div>
<div class="tg-text">یاشار میشه شغل اصلیت بگی خواهش میکنم‌جواب پیام بده خیلی مشتاقم بدونم اون همه مشروب چطوری کار کردی خریدی
💔</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/12998" target="_blank">📅 12:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12997">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b74ad7b47.mp4?token=sQTaoBc83pBFM3bYjrbGJQs-jMFPgVPK8SOd-s1SCa4d8uC7aOHxPttz2s-3jJvR2JoARwsrW-UaXe6WEkTNzgafejmH4lJEhUzfnWTwjILBb4BOaYPkm_Uv7_10UXDVuCmFHJY5btSf4pmbPKP0cApBQBK4ScAhtAnoj73iAPg2CU4gzKxizVc2s7Uogo3iPV9ZTHuESxDIklui6Q8r_YZXyo46Bhy5cUUfDHCufOpu7jPl9B_0uebOLxdqCO7_mEygYoTAnskC16oCSAMfvIb-ex_1wduIjrHToz_biq7-d_gUv3akeAUFFAdIKpjFux9qHeT3zSTc4XvoSuP0Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b74ad7b47.mp4?token=sQTaoBc83pBFM3bYjrbGJQs-jMFPgVPK8SOd-s1SCa4d8uC7aOHxPttz2s-3jJvR2JoARwsrW-UaXe6WEkTNzgafejmH4lJEhUzfnWTwjILBb4BOaYPkm_Uv7_10UXDVuCmFHJY5btSf4pmbPKP0cApBQBK4ScAhtAnoj73iAPg2CU4gzKxizVc2s7Uogo3iPV9ZTHuESxDIklui6Q8r_YZXyo46Bhy5cUUfDHCufOpu7jPl9B_0uebOLxdqCO7_mEygYoTAnskC16oCSAMfvIb-ex_1wduIjrHToz_biq7-d_gUv3akeAUFFAdIKpjFux9qHeT3zSTc4XvoSuP0Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/12997" target="_blank">📅 12:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12996">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/12996" target="_blank">📅 12:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12995">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیویورک تایمز:  ایران خواسته های واشنگتن برای تسلیم کردن ذخایر اورانیوم غنی‌شده‌اش را رد کرده است
.
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/12995" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12994">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/12994" target="_blank">📅 12:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12993">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/12993" target="_blank">📅 11:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12992">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromkamyar</strong></div>
<div class="tg-text">یاشار خیلی حرف های درست و حسابی میزنی دردش اینکه هنوز یکسری هستن که حرفاتو قبول ندارن چقدر باید هزینه بدیم تا همه بیدار شن؟</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/12992" target="_blank">📅 11:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12991">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/12991" target="_blank">📅 11:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12990">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEmmmmmaaaadddf</strong></div>
<div class="tg-text">داداش ما باید فحشت بدم جواب بدی</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/12990" target="_blank">📅 11:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12989">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/12989" target="_blank">📅 11:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12988">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/12988" target="_blank">📅 11:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12987">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehran</strong></div>
<div class="tg-text">درود یاشار جان احتمال داره دوباره متحد بشیم برا خیابونا</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/12987" target="_blank">📅 11:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12986">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/12986" target="_blank">📅 11:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12985">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARVIN🏎️</strong></div>
<div class="tg-text">درود یاشار جان خسته نباشی
♥️
این حرف که میگن مردمو مسلح کنن باعث جنگ داخلی و سوریه و عراق شدن میشه رو نظرتو میگی راجبش
🙏🏻
♥️</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/12985" target="_blank">📅 11:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12984">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">@withyashar
SCARY MOVIE</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/12984" target="_blank">📅 11:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12983">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from2585</strong></div>
<div class="tg-text">درود
موافق پوریا زراعتی نیستم
جولانی تروریست بود
مردم ما معترض عادی‌ن
دست به اسلحه نیستن
برای متن نوشتن برای شاهزاده مخالف نیستم</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/12983" target="_blank">📅 10:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12982">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/12982" target="_blank">📅 10:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12981">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/12981" target="_blank">📅 10:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12980">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-poll">
<h4>📊 نظر شما در مورد فراخان اینترنتی ۱۱:۱۱ دقیقه شب</h4>
<ul>
<li>✓ شدیدأ انتقاد لازمه اپوزیسیون و تمام مشکلات رو همون اول بگو</li>
<li>✓ ایجاد ارتباط و اشاره ریزی به مشکلات برای شروع  (راه خودت)</li>
<li>✓ اصلا هیچ نگو اینم کنسل کن ( من تندرو هستم ‌یا عرزشی )</li>
<li>✓ من اصلا سیاسی نیستم فقط تماشا میکنم ، فل فل دلمم🫑</li>
</ul>
</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/12980" target="_blank">📅 10:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12979">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/12979" target="_blank">📅 10:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12978">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/12978" target="_blank">📅 10:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12977">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89c68ff2f2.mp4?token=IgVAVJWvHdbtrOdFZLDpelyo3m-4iZNjNjh2UYV_SNC684Xan6dV_JPOm-CYCc9h8XxX_vUa6mfmmsjIFSOzT7IMQSuSGxnuPL8aeb_Wgnna8Lq8M8TkGQylZDni5RuCEEf41YeZ5lKPOVvRx4IBc5GTmP6pdGIvsoZgk3UEzJMpGWay6-Kxgk2ksSYLETvObY84kDCYTSYnPooOU4V6kla0GsH78OUtq24bMeZGit1Qr2j_Ouanx84qwI4QDENFvTTBEPeh-3Dv5Fgfxk0SVziakDsmpZxVPlqdPkgHPwuhdq0BBuIYgwH5Gf48tsvB7Vgm1CyEgGXKuCFp02xlvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89c68ff2f2.mp4?token=IgVAVJWvHdbtrOdFZLDpelyo3m-4iZNjNjh2UYV_SNC684Xan6dV_JPOm-CYCc9h8XxX_vUa6mfmmsjIFSOzT7IMQSuSGxnuPL8aeb_Wgnna8Lq8M8TkGQylZDni5RuCEEf41YeZ5lKPOVvRx4IBc5GTmP6pdGIvsoZgk3UEzJMpGWay6-Kxgk2ksSYLETvObY84kDCYTSYnPooOU4V6kla0GsH78OUtq24bMeZGit1Qr2j_Ouanx84qwI4QDENFvTTBEPeh-3Dv5Fgfxk0SVziakDsmpZxVPlqdPkgHPwuhdq0BBuIYgwH5Gf48tsvB7Vgm1CyEgGXKuCFp02xlvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوریا زراعتی مجری اینترنشنال: اپوزیسیون ما رویا فروشی میکنه و وعده هاش دروغ بود
ما به کسی مثل جولانی نیاز داریم نه رهبران فعلی اپوزیسیون
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/12977" target="_blank">📅 10:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12976">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ارتش اسرائیل: کنترل قلعه الشقیف در جنوب لبنان را به دست گرفتیم.
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/12976" target="_blank">📅 09:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12975">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/120549a54c.mp4?token=iKELT0E0FZhBgJ4pbZG4ZaEh2fhvj5MKA4wGnM7dd8fZh4bIKCrML16O4Bs5jhupw_piVgWM5Ygh3wNXNW4MGwfm1nO5ko9AkbuhN8GkLbj_KUtlFF1bBNF3UScnPO29bGMkyiGSJTEWGI9urtVc-QvlRUP5jMCr6zs8PlukofvtLxvLATl1X-Xc4piliLZjq3YHntNwSVrIWIP9l6dIKkc7HBxT3-7HqYX770-z8MEPB_P5BRNYdFPFEP0SfOSEv1YDefDMZVQfodq6bAqHuRmS21iqxDzYhqAHy2_2e9E_-9Xm2KP6sxNlD9u6r91TESMsjfuvqySaG5fFqTg2bbzpbM2Pjded7bVCjcirCUYFafwjTCB9OzfsMaeVWSTYC1VCFDccQwiNygEK4F0U8ovlvH_oll6mk27ZJjSx_alNTipOliE2mnQ_EZ0fdI6G522ThuiOQDP9ybRRFoPZFighxO5ruujdXC1kKe11BYJ0iOQ2MHvisI306tMP9zYADfAjpzI7oCnUrJhLojqP-vYDfWPzJUL1TSiZGthfAtC4EPvfWuWV-ryJg_eOF3PwA5jFE5Q39WuaDmuRRRsL2zY9fIZbpjyWQzTuRo0LX0yFbDoPieXOCISyryrN8bipsFWLGTPZhRvSU6jhPUysVtE9NqCOGiksp5jr5_xjjmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/120549a54c.mp4?token=iKELT0E0FZhBgJ4pbZG4ZaEh2fhvj5MKA4wGnM7dd8fZh4bIKCrML16O4Bs5jhupw_piVgWM5Ygh3wNXNW4MGwfm1nO5ko9AkbuhN8GkLbj_KUtlFF1bBNF3UScnPO29bGMkyiGSJTEWGI9urtVc-QvlRUP5jMCr6zs8PlukofvtLxvLATl1X-Xc4piliLZjq3YHntNwSVrIWIP9l6dIKkc7HBxT3-7HqYX770-z8MEPB_P5BRNYdFPFEP0SfOSEv1YDefDMZVQfodq6bAqHuRmS21iqxDzYhqAHy2_2e9E_-9Xm2KP6sxNlD9u6r91TESMsjfuvqySaG5fFqTg2bbzpbM2Pjded7bVCjcirCUYFafwjTCB9OzfsMaeVWSTYC1VCFDccQwiNygEK4F0U8ovlvH_oll6mk27ZJjSx_alNTipOliE2mnQ_EZ0fdI6G522ThuiOQDP9ybRRFoPZFighxO5ruujdXC1kKe11BYJ0iOQ2MHvisI306tMP9zYADfAjpzI7oCnUrJhLojqP-vYDfWPzJUL1TSiZGthfAtC4EPvfWuWV-ryJg_eOF3PwA5jFE5Q39WuaDmuRRRsL2zY9fIZbpjyWQzTuRo0LX0yFbDoPieXOCISyryrN8bipsFWLGTPZhRvSU6jhPUysVtE9NqCOGiksp5jr5_xjjmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اصلاً نباید وارد ماجرای ایران می‌شدیم، اما...ما تا حد زیادی کاری به ارتش ایران نداشتیم، چون فکر می‌کنیم ارتش‌شون تا حدی میانه‌رو هست.
اما افراد دیگه‌ای هم دارن که میانه‌رو نیستن؛ اون‌ها رو از بین بردیم.
ببینید، دو تا موضوع وجود داره: اول اینکه تنگه باید فوراً باز باشه و رفت‌وآمد در اون آزاد باشه؛ هیچ عوارض یا هزینه‌ای نباید گرفته بشه.دوم اینکه ایران نباید سلاح هسته‌ای داشته باشه
همین. قضیه به همین سادگیه. بعدش هم ما از اونجا خارج می‌شیم.
ایران الان تو موقعیت خیلی بدیه؛ ولی احتمالاً بزرگ‌ترین سرمایه‌شون همین رسانه‌های فیک‌نیوزه.
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/12975" target="_blank">📅 09:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12974">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ادعای اکسیوس: دو مقام آمریکایی گفتند، ترامپ خواهان این توافق است و انتظار دارد آن را به زودی نهایی کند، اما مصمم است چند نکته را که برای او اهمیت دارند، به‌ویژه در مورد مواد هسته‌ای ایران، تقویت کند
درخواست ترامپ دور جدیدی از رفت‌وآمدها (یا مذاکرات رفت‌وبرگشتی) بین طرفین را آغاز کرده است که ممکن است چند روز به طول بینجامد.
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/12974" target="_blank">📅 09:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12973">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اسرائیل هیوم: ایالات متحده به نفتکش‌ها و کشتی‌های حمل گاز مایع قطر اجازه داده است پس از پرداخت پول به ایران، تنگه هرمز را ترک کنند
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/12973" target="_blank">📅 09:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12972">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آکسیوس‌: ترامپ در جلسه اتاق وضعیت روز جمعه درخواست چندین تغییر در پیش‌ نویس توافق آمریکا و ایران کرد که باعث آغاز دور دیگری از مذاکرات شد که ممکن است چند روز طول بکشد
ترامپ خواستار زبان قوی‌ تری در مسائل کلیدی ، به‌ ویژه در مورد مدیریت و انتقال ذخیره اورانیوم غنی‌ شده ایران و همچنین برخی مفاد مربوط به بازگشایی تنگه هرمز است
موافقت‌ نامه فعلی شامل تعهد ایران به عدم دنبال کردن سلاح هسته‌ ای و دوره 60 روزه برای مذاکره درباره محدودیت‌ های هسته‌ ای و رفع تحریم‌ ها است ، اما ترامپ به دنبال شرایط مشخص‌ تری است
ایران هنوز متن نهایی را تأیید نکرده و مقامات آمریکایی انتظار دارند پاسخ تهران ممکن است چند روز طول بکشدrیک مقام ارشد دولت گفت : یک توافق حاصل خواهد شد ، اما خاطرنشان کرد که جدول زمانی نامشخص است و ممکن است از چند روز تا بیش از یک هفته متغیر باشد
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/12972" target="_blank">📅 09:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12971">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فارس : براساس برنامه‌ریزی‌های انجام‌شده، حجاج ایرانی از فرودگاه جده به شش فرودگاه شامل تهران، مشهد، زاهدان، شیراز، گرگان و اصفهان منتقل خواهند شد.
نخستین پرواز بازگشت حجاج روز ۱۱ خردادماه(دوشنبه) از جده به مقصد تهران انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/12971" target="_blank">📅 03:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12970">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عجب سکوت مرگباری …</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/12970" target="_blank">📅 01:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12968">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">@withyashar
JangHub</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/12968" target="_blank">📅 00:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12967">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86254cf93.mp4?token=OMyHIPRmOLbhqxC243NsPlT5uG5nGQpvDDkSWU3Pw3XWZLFrO56P9ySnU0AC1jV8Og2EWWjWTr_fEmv4CTUCdsHpKkNEwfJR3zKVZa6iT-9QyA3J0ERi1DyhZGxhbDwkzoRedE_3u1DBMcr0xmPhczvqrPpPYdhP5NNxL2RAFDFgPS7NSB-dYGdEeFHwv2mBSfqsiab4AuPbjTB1b179-20hnP7F8c4MzliCUvyWaFnUGLvkNUEja7ev1ETZYX4mpSjDCnUpSF6ZLK4NbK9fqX0O--RzLs9Lh9MyvRfkXSru5ChdfyGRT8MVir4fgtOTZIjr-GxoTnTm5tITOhV1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86254cf93.mp4?token=OMyHIPRmOLbhqxC243NsPlT5uG5nGQpvDDkSWU3Pw3XWZLFrO56P9ySnU0AC1jV8Og2EWWjWTr_fEmv4CTUCdsHpKkNEwfJR3zKVZa6iT-9QyA3J0ERi1DyhZGxhbDwkzoRedE_3u1DBMcr0xmPhczvqrPpPYdhP5NNxL2RAFDFgPS7NSB-dYGdEeFHwv2mBSfqsiab4AuPbjTB1b179-20hnP7F8c4MzliCUvyWaFnUGLvkNUEja7ev1ETZYX4mpSjDCnUpSF6ZLK4NbK9fqX0O--RzLs9Lh9MyvRfkXSru5ChdfyGRT8MVir4fgtOTZIjr-GxoTnTm5tITOhV1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای کانیه وست :
کنسرتم در استانبول رکورد ۱۱۸ هزار تماشاگر را ثبت کرده و به بزرگ‌ترین رویداد استادیومیِ بلیت‌فروشی‌شده در تاریخ تبدیل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/12967" target="_blank">📅 00:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12966">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89387a1183.mp4?token=RZP4gmf67Iw7AtT9R1A6yEbvYxqgJeoTruGwPGBKqQxx0SRzB-oDLJ5ZLX9S3g7147WLULDTN_W8yVZ6OHV4P8kv_4LR6HmkrCzbtjRTF7OJXgQvf1SpMSx-H60A_ahMn9hjWIs-0vMWyqftz6OsDrFWxEOTiUPRIBeEHRrs25QlMUXTj5hjLQNo093KlDjPyxPy5hvTFPW5gmuRGM1ZKPO2o86gM5GzDcvA324fx83QYzw89p7laYSoCH2FVD3qbAOhiQJHuNfklk1tSe5KMoPvDYbEL9hBhp5LtY1XfibxyoHZApPuhLYXKUXVKvc-4jsS4GF0g2wkudKDJ41Elw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89387a1183.mp4?token=RZP4gmf67Iw7AtT9R1A6yEbvYxqgJeoTruGwPGBKqQxx0SRzB-oDLJ5ZLX9S3g7147WLULDTN_W8yVZ6OHV4P8kv_4LR6HmkrCzbtjRTF7OJXgQvf1SpMSx-H60A_ahMn9hjWIs-0vMWyqftz6OsDrFWxEOTiUPRIBeEHRrs25QlMUXTj5hjLQNo093KlDjPyxPy5hvTFPW5gmuRGM1ZKPO2o86gM5GzDcvA324fx83QYzw89p7laYSoCH2FVD3qbAOhiQJHuNfklk1tSe5KMoPvDYbEL9hBhp5LtY1XfibxyoHZApPuhLYXKUXVKvc-4jsS4GF0g2wkudKDJ41Elw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی :
۴۰ هزار ایرانی برای تنگه هرمز یا برای یک توافق هسته‌ای کشته نشدن.
ما باید فشار روی رژیم رو ادامه بدیم تا نتونه منابع مالی لازم برای تأمین و پرداخت به نیروهای نیابتی و مزدورهاش رو فراهم کنه.
اما بهترین راه برای اینکه کار به حضور نیروهای خارجی در زمین نکشه اینه که به مردم ایران کمک بشه تا خودشون اون نقش رو بازی کنن
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/12966" target="_blank">📅 00:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12965">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رییس سازمان عقیدتی سیاسی انتظامی:
حکم قاتلان خامنه‌ای رو باید در ملا عام اجرا کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/12965" target="_blank">📅 00:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12964">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7_zNp6KtK2ctGcOUM4qV4GwLaHVPSBVEXMBJVdfLgOGAxm1QO23Mcx1LqFJB23fMUlSYzEGQCNFWnECj_meFCy_akuU1c5I_HevNkn6aMlmwdxcgw1m83iBX77U8DTTKp48MxfcPPJ4piCK3ICAeLMCs9of0BEArrN7UExAq9DJ_lCQSaGcYoYxq-WPcVyo366scg96ASVcw-MUleOvYulSuKvTx26sJkC6aufyZXGNWrux2b3fnTjTCmOsoNoZtt5ooRQdK6biiS7MJ7g5asOu6O_2hIvIb1LN8GOp5Iqx0VSV6-ls4zI3GPHicmzFpW_sioDe1IMNHBuCeWBcfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث
🤣
:
«یکی باید برای پاپ توضیح بدهد که شهردار شیکاگو کاملاً بی‌فایده است و اینکه ایران نمی‌تواند سلاح هسته‌ای داشته باشد!
رئیس‌جمهور دونالد جی. ترامپ»
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/12964" target="_blank">📅 00:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12963">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31f4e3fc3.mp4?token=uobt75H5ukzhMYzffS9xeubBfBiNH4iuPuVhD1XwTjzD-wWRREHx2gddpEQ9aldY4t7vvmBaoSf-04OcxNDLjd_YlKeDfxoil08CW4XLyYE9K8cywuLt_CbZcAEtA-G1xy_5CfI3izzU5-P0b-f_BkYaph_PU6ZA96VedYzJjle0xfk5-LRa2cJjBnRTVW6UXBGoLwQktIalgrbY-gYTgbz2q3SrcCV6kjYGzXrrsVSV_JiaU_WOX3FSaam2QXQObll1vWcmP4VHWtKXSexl4zpIfSlzcuhWX-FVfbOPfs6-x0Z8Nl76cYT0Hml2_jvKH7JYX0AkoCBmTYxvSfIT4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31f4e3fc3.mp4?token=uobt75H5ukzhMYzffS9xeubBfBiNH4iuPuVhD1XwTjzD-wWRREHx2gddpEQ9aldY4t7vvmBaoSf-04OcxNDLjd_YlKeDfxoil08CW4XLyYE9K8cywuLt_CbZcAEtA-G1xy_5CfI3izzU5-P0b-f_BkYaph_PU6ZA96VedYzJjle0xfk5-LRa2cJjBnRTVW6UXBGoLwQktIalgrbY-gYTgbz2q3SrcCV6kjYGzXrrsVSV_JiaU_WOX3FSaam2QXQObll1vWcmP4VHWtKXSexl4zpIfSlzcuhWX-FVfbOPfs6-x0Z8Nl76cYT0Hml2_jvKH7JYX0AkoCBmTYxvSfIT4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا:
کشور من از همه طرف ضربه خورده؛ از داخل توسط همین رژیم، و از بیرون هم به خاطر پیامدهای بی‌فکری خودش. با این حال، جمهوری اسلامی هنوز سر جاشه.
بعضی‌ها توی این جمع ممکنه اینو نشونه‌ی قدرت رژیم بدونن. من اینجام بگم که اینطور نیست.
این فقط نشونه‌ی اینه که دنیا هنوز نتیجه‌ی درست از چیزی که داره می‌بینه نگرفته.
پهپاد شاهد فرقی نمی‌کنه کجا باشه؛ چه یه ساختمون مسکونی، چه یه میدان اعتراض تو تهران، چه دفترهای تجاری تو دبی.
پهپادهایی که آسمون شهرهای اوکراین رو تاریک کردن، توی همون کارخانه‌هایی ساخته شدن که زیر نظر همون رژیمی هستن که توی تهران برای شکار معترض‌ها، توی خیابون‌ها پهپادهای نظارتی فرستاد.
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/12963" target="_blank">📅 23:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12962">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پست جدید بوگاتی شاه   https://www.instagram.com/reel/DY-ObumIJEK/?igsh=MjQ5cGt6dWo0dGg= کارای اداریش رو انجام بدید
💥</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12962" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12961">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">در پی حملات سنگین حزب‌الله، به بیمارستانی در شهر نهاریا در شمال اسرائیل دستور داده شد تا بیماران را به تأسیسات زیرزمینی منتقل کند.
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/12961" target="_blank">📅 23:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12960">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شاهزاده رضا پهلوی:  با جمهوری اسلامی توافق نکنید، بلکه به آن پایان دهید.
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/12960" target="_blank">📅 23:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12959">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جلسه کمپ دیوید که قرار بود امروز برگزار شود ترامپ اعلام کرد: جلسه کابینه به دلیل شرایط آب و هوایی در کاخ سفید برگزار خواهد شد، نه در کمپ دیوید! حالا صحبت‌هایی هست که کمپ دیوید یک تله برای شناسایی فردی بود که اطلاعات را نشت می‌داد ! فرد مورد نظر گیر افتاد !…</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/12959" target="_blank">📅 22:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12958">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIBOVZcDSAe7txNIbkoGyf_uNITQ6DS0-l-R_qEy5JwW-NbdovbTmYtgcJNNUZ-ou-qjpGm_ViCUVGWlxHylQ_47w6UoIkKnlzc-bkr_hf6v6inyP61e7FZWbUcJjoX3lniQ3EEqTmG0rFgvJZIdunKrr4REr-XNSWcLk5sMuqWcI8Ai7EAFKvGi1YIg9eGE31CMHSvhlMt5IGUfDPdV_d-GFwxe5MNB0T6n-7uV_9b2TYXEsTFSTMjh5W5njLCXmVpCdwBvUellO7C6HHJdcRBpXcf2iORkCqY9GCPgCdBBr1PLLPO2YXKsY_N5nHRVihkJm5SbniQlBnHl8mbzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به ادعای آمریکا در جریان این جنگ، دست‌کم ۱۶۰ شناور دریایی ایران را غرق کرده است. هر یک از این شناورها می‌تواند منبعی بالقوه برای آلودگی باشد. وقوع یک نشت جدی در تنگه، مهار آن را بسیار دشوارتر از حالت معمول خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/12958" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12957">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12957" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12956">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKiasha</strong></div>
<div class="tg-text">یاشار امشب ردبول رومی خوری؟</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/12956" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12955">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سنتکام اعلام کرد کشتی تجاری Lian Star که از یک بندر ایران خارج شده بود پس از 20 هشدار توقف و عدم توجه آن توسط یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت و در دریای عمان توقیف شد.
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/12955" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12954">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پست جدید بوگاتی شاه
https://www.instagram.com/reel/DY-ObumIJEK/?igsh=MjQ5cGt6dWo0dGg=
کارای اداریش رو انجام بدید
💥</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/12954" target="_blank">📅 21:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12952">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صداوسیما جزئیات غیررسمی از یادداشت تفاهم (ایران و آمریکا) را منتشر کرد
‌
یکی از مهمترین محورهای توافق (ایران و آمریکا) بازتعریف قواعد عبور و مرور در تنگه هرمز است
‌ایران مرجع انحصاری تشخیص ماهیت شناورهای عبوری است
هر شناوری که محموله آن تهدید آمیز تلقی شود یا بهره‌بردار نهایی آن در خصومت با ایران باشد به عنوان کشتی تجاری شناخته نمی‌شود و اجازه عبور از مسیرهای تعریف شده را ندارد
تعیین مسیر حرکت و تعیین هزینه خدمات ناوبری در حوزه تصمیم‌گیری ایران دیده شده
‌
هر شناور موظف است اطلاعاتش را در اختیار مرکز مرتبط با نیروی دریایی قرار دهد و فرم‌هایی شامل جزئیات محموله مالکیت و مقصد را تکمیل کند
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/12952" target="_blank">📅 21:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12951">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الجزیره: ترامپ برای جلوگیری از جنگ با ایران پیش از جام جهانی بسیار مصمم است
او همچنان برای دستیابی به یک توافق موقت با تهران تحت فشار است، اما پیشرفت فوری بعید به نظر می‌رسد
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/12951" target="_blank">📅 21:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12950">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شبکه ۱۴ اسرائیل : نتانیاهو، قراره به‌زودی یه جلسه امنیتی برگزار کنه تا درباره نحوه پاسخ به شدت گرفتن حملات حزب‌الله تصمیم بگیره
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/12950" target="_blank">📅 20:49 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
