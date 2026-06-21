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
<img src="https://cdn4.telesco.pe/file/YnI1fTW4z5c5QNLGHFqp9BeD09X5cYMdChU-u8kGkF_ySypkIzktTofg2CpyD3YnsSb2co5-0vTsKbwbsEpDI3woqn9aWxjOD4UuukBT_Q3R3INCCgirxjTft7v8VjjKyHQsSAUNuAWh1al5u_sCkAWSu4hvpkSSX_evdlPxhKp3ij8APVt40rDBVpUz4-0BLShXHw1PizBDm9T3wWS1RNfHVY541ENF6xC4gHesWzlcLjyC4BYkFeL9Vp7UZWaCk0gWmSTpJPpkpQ_wg_OOWQoSbVGXpuzt_DOgkgszmQvEasevivi1lAVP6lAphOfIGo-2wlO_FzbuXXVtrdFYlg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 16:31:23</div>
<hr>

<div class="tg-post" id="msg-15495">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ونس:  از آنچه در لبنان به دست آمده راضی هستم تنگه هرمز بازگشایی شد
@withyashar</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/withyashar/15495" target="_blank">📅 16:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15494">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رسانه‌های عبرى: حادثه امنيتی جدید برای نیروهای ارتش اسرائیل، در هنگام عملیات انتقال مجروحان دقایقی پیش از جنوب لبنان انجام شده است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/withyashar/15494" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15493">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759c397f4c.mp4?token=XPbJHB16kA_PpUrFQmUBAJiLyNw1RpAS1DU_EliJjGREoPd9UckiNAOn0Yy4CU6bYeg1kwzNNtRAxp0oFa3sa0YHKKZt-nJW3tVsAnYexci_v20_i-JxIxA03cq06Ek4U_M8JBMrOQm93BhgnLznByVVcIaBEtFjKpjOHSlMNwIDOv7Mf8G8SG3nG8Sc39zdRy1-CEpoBNCM8yPq_juitL2ztikX1Y1UqXjvsOZSpzv07Ue9QGt9ljJiCvfKvkUqd92yDxFUz5bDAp3xYBFmcoQ0b3n8nbmiDwz5utCDDXIc6YkNoSiuWJDMn0si6B1unlA3UZIBtutFxnSbNTdcfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759c397f4c.mp4?token=XPbJHB16kA_PpUrFQmUBAJiLyNw1RpAS1DU_EliJjGREoPd9UckiNAOn0Yy4CU6bYeg1kwzNNtRAxp0oFa3sa0YHKKZt-nJW3tVsAnYexci_v20_i-JxIxA03cq06Ek4U_M8JBMrOQm93BhgnLznByVVcIaBEtFjKpjOHSlMNwIDOv7Mf8G8SG3nG8Sc39zdRy1-CEpoBNCM8yPq_juitL2ztikX1Y1UqXjvsOZSpzv07Ue9QGt9ljJiCvfKvkUqd92yDxFUz5bDAp3xYBFmcoQ0b3n8nbmiDwz5utCDDXIc6YkNoSiuWJDMn0si6B1unlA3UZIBtutFxnSbNTdcfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عن بازی همیشگی و انتظار هیات آمریکایی برای ورود تیم مذاکره کنندگان جمهوری اسلامی
@withyadhar</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/withyashar/15493" target="_blank">📅 16:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15492">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">محل برگزاری مذاکرات چهارجانبه ایران و آمریکا با مشارکت کشورهای میانجی
@withyashar</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/withyashar/15492" target="_blank">📅 16:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15491">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWUVZfD91gEDLTvZVhw6Vws8l7kWS9DHZorFhpSbE8stR9ABpJdWiaa1M-o2mkWaZU8GtAdGuA2KD2jHnD4cHOSOYuEoooel_LFEmXA2o6aBgyKfL-4mxQGQYvNlT63aiz4n1Me0GWwE_5xSUvoIntW1ofgqece-hdX9gsj_-aM9uf_CacWFlFrYwgG9Ekq8zi8D--gLZjvBWUO6iiKKzCCVj63VXylvUycTK-4hbCadlJggz4cROpbVGV_IInsskqw8yjf8clMU5AR4oS54pjx6zKPAEfO-riVW4zbmYcGpPFw2l42IM85ePGC2VQz8O30RGXi8SvIQy3wI8J-WkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
روز پدر مبارک!
کشور ما عالی عمل می‌کند. تعداد مشاغل و بازار سهام رکورد زده، بهترین اقتصاد تاریخ! بزرگترین ارتش جهان، تا به امروز. ما در همه جبهه‌ها پیروز می‌شویم، پیروزی‌ای بی‌سابقه. خدا همه شما را حفظ کند!!! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/withyashar/15491" target="_blank">📅 15:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15490">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMiaCyYZDLzS5zRnmKUS4D9n-kd7Gs55qUd11b1FxWRU_WwuvZtZCZZsPLIj_hBLZM-QcWsDGQieINlrXlU5GfmcYSzeTzs7WmQvuoGZenfleq4a41LnUjlOBkcRSR5ddXstE9NLWnNYhxfKQVn3kBusAPmZ93_n7-9gWmforZGkhxnGdjfggvM-UAP5Mjctm7Y2qOvw9SL4lfpJ3yepPDIH5JVb-ieoTv2wRkGkKCJXNoAse4IAsnpFfNmxUotLk-rEAj-h30n5RCs1Z9D2GE3WCF6lx26CUiRJTyj4sT-wigkxP6GoMx64R_PUry5e9PJBY96wI0WxsMCtN4QaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار شهباز شریف نخست وزیر و عاصم منیر فرمانده ارتش پاکستان با محمدباقر قالیباف رئیس هیئت
جمهوری اسلامی
- زوریخ سوئیس
@withyashar</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/withyashar/15490" target="_blank">📅 15:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15489">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نشست سه جانبه ایران، امریکا و قطر با موضوع آتش بس فراگیر در لبنان و اموال بلوکه شده ایران هم اکنون در محل مذاکرات در حال برگزاری است.
@withyashar</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/withyashar/15489" target="_blank">📅 15:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15488">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پزشکیان: مواضع ترامپ ۱۸۰ درجه نسبت به گذشته عوض شده
از حق غنی‌سازی نخواهیم گذشت؛ آنها هم مجبورند بپذیرند.
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/15488" target="_blank">📅 14:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15487">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صداسیما: اینترنت سوئیس ضعیفه ارتباطمون با خبر نگار قطع شد
@withyashar</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/15487" target="_blank">📅 14:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15486">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پزشکیان: اگر تورم ادامه پیدا کند و به تورم سه‌رقمی تبدیل شود، آیا جامعه توان تحمل چنین وضعیتی را خواهد داشت؟
@withyashar
😂</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/15486" target="_blank">📅 14:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15485">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">العربیه: شهباز شریف و عاصم منیر پس از دیدار با ونس، با هیأت ایرانی دیدار خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/15485" target="_blank">📅 13:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15484">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پزشکیان : از حق غنی سازی اورانیوم دست نمیکشیم
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/15484" target="_blank">📅 13:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15483">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">محاصره ستاد کل حزب‌الله در جنوب لبنان،به گفته کانال 14 اسرائیل:
نیروهای ارتش اسرائیل مرکز فرماندهی زیرزمینی و ستاد اصلی حزب‌الله در جنوب لبنان در ارتفاعات علی طاهر را که ایران در جنوب لبنان ساخته بود، تصرف کرده‌اند،
این مرکز فرماندهی اصلی که به‌عنوان عماد 4 شناخته می‌شد،بزرگ ترین پایگاه موشکی حزب الله در لبنان نیز محسوب می‌شود،گمان می‌رود صدها عضو حزب‌الله وسپاه ایران در داخل این مرکز گرفتار شده باشند.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/15483" target="_blank">📅 13:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15482">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسماعیل بقایی: موضوع اصلی مذاکرات امروز ما درگیری های لبنان هست نه مسائل ایران
@withyashar
بیا بد عرزشی هنوز فکر میکنه اینا برای ایرانن</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/15482" target="_blank">📅 12:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15481">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa86d8af0a.mp4?token=qtPWhW_agYxI1v1TS4U9T4aik9NoMJqRYF_ZQK6_rRUuVgGZbJ0-SfNR88S3R0_azQm_tfpPmqFOGY3GfIH4BnA276zmmo9nZsUjxSNwlJy7J8hWRRFXrJ52ksZiCojH3MH7v5chyCxH4_aVFJ3QPYnbOQcdoNOYbKoXku_EFsLv8329zVNaEWCcziR6Hp8-LGUYyog7j52x7lpUGNLyoaCzOqxN7aGGSEJF3prXibC5DpVN-93aMOmfDP14R2SHLoZZ-QQswRHngYZv8ae3DKMvstzJ82_C9WtRhXzEzq4htIXR4pywPujS5-XBWvmwVV3BjeoXBzl77wxboGI0Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa86d8af0a.mp4?token=qtPWhW_agYxI1v1TS4U9T4aik9NoMJqRYF_ZQK6_rRUuVgGZbJ0-SfNR88S3R0_azQm_tfpPmqFOGY3GfIH4BnA276zmmo9nZsUjxSNwlJy7J8hWRRFXrJ52ksZiCojH3MH7v5chyCxH4_aVFJ3QPYnbOQcdoNOYbKoXku_EFsLv8329zVNaEWCcziR6Hp8-LGUYyog7j52x7lpUGNLyoaCzOqxN7aGGSEJF3prXibC5DpVN-93aMOmfDP14R2SHLoZZ-QQswRHngYZv8ae3DKMvstzJ82_C9WtRhXzEzq4htIXR4pywPujS5-XBWvmwVV3BjeoXBzl77wxboGI0Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاسکو دیدبان اتاق جنگ در شیراز
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/15481" target="_blank">📅 12:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15480">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667b5ddaab.mp4?token=SfychAutxnlgOXKQoxazng_NzgWrzcq70ol1cPrsWwfphMra7SYdkxXMZqjNuUBBZMoFFixWNL2vh5k0FM6oPAAqnxm0sMypRU9HccwIEO06tPHcca6QqtAEnHTk223P1z6i7IHySa0dCqoA2sjXmvo09LGI0eXG26y9pRxsxiSXuQbOSfgRMLD_qrfcCeBjKkpyGnIkXO4Y95UJgqPRTiDJ4TcxwBNkVJCIMxww-G5EqrLxALqQYf94QZyBs8kwwO26IaSPAFuYs8sQk-5lsbS7RTofU-W4Zy3sR7qEVuQEIrZJADBHQ-6rOgfFpZJ2sthFZUxL3mMf1wV-IswRMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667b5ddaab.mp4?token=SfychAutxnlgOXKQoxazng_NzgWrzcq70ol1cPrsWwfphMra7SYdkxXMZqjNuUBBZMoFFixWNL2vh5k0FM6oPAAqnxm0sMypRU9HccwIEO06tPHcca6QqtAEnHTk223P1z6i7IHySa0dCqoA2sjXmvo09LGI0eXG26y9pRxsxiSXuQbOSfgRMLD_qrfcCeBjKkpyGnIkXO4Y95UJgqPRTiDJ4TcxwBNkVJCIMxww-G5EqrLxALqQYf94QZyBs8kwwO26IaSPAFuYs8sQk-5lsbS7RTofU-W4Zy3sR7qEVuQEIrZJADBHQ-6rOgfFpZJ2sthFZUxL3mMf1wV-IswRMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیات جمهوری اسلامی ایران عازم ساختمان محل مذاکرات شد
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/15480" target="_blank">📅 12:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15479">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سخنگوی هیئت مذاکره کننده ایران:
برای اطمینان از اجرای یادداشت تفاهم به صورت مستمر از طریق میانجی‌ها تبادل پیام می‌کنیم
در جلسه بعد از ظهر، هیئت‌های نمایندگان هر ۴ کشور در یک اتاق حضور خواهند داشت
@withyashar</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/15479" target="_blank">📅 12:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15478">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ادعای فارس: تنگۀ هرمز همچنان بسته است و نیروی دریایی سپاه نیز تا اطلاع ثانوی هیچ‌گونه مجوزی برای عبور شناورها صادر نمی‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/15478" target="_blank">📅 11:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15477">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb280fa86.mp4?token=IT79q-FLQa2xjOeOjkrJ3ZmllVACrNYxZ8lQvCpq3Z4TP5rjyx60lNJSFfCfB83qyQeM-USpqnJ3qnuczdzJ1960N38tjAGz5A-nfonSqk8GTRW9h459uCMRQa6b3243PruZs_VeB4g64-v3xV-uFTUmwli8GpEyIQrmJpPYlhprpsOuJPEHMhHqU6YDGp227CM2jk39PABIRGZzulQ15htP_eIqyC3L5m5BwhPMOGI8BFu13WQd1-u45ndx_gAlGtw2AUNYeh18xntpmO_TP_dxIl3E81L3HUBOmczpGUakJFWt04xBPycMvg6pX2CZ8F1P8rjEK-iP7wva_Tx7kYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb280fa86.mp4?token=IT79q-FLQa2xjOeOjkrJ3ZmllVACrNYxZ8lQvCpq3Z4TP5rjyx60lNJSFfCfB83qyQeM-USpqnJ3qnuczdzJ1960N38tjAGz5A-nfonSqk8GTRW9h459uCMRQa6b3243PruZs_VeB4g64-v3xV-uFTUmwli8GpEyIQrmJpPYlhprpsOuJPEHMhHqU6YDGp227CM2jk39PABIRGZzulQ15htP_eIqyC3L5m5BwhPMOGI8BFu13WQd1-u45ndx_gAlGtw2AUNYeh18xntpmO_TP_dxIl3E81L3HUBOmczpGUakJFWt04xBPycMvg6pX2CZ8F1P8rjEK-iP7wva_Tx7kYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارک لوین رو به دولت ترامپ در ‌فاکس نیوز:
بس کنید به خراب کردن، بدنام کردن و زورگویی به دولت اسرائیل!
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/15477" target="_blank">📅 11:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15476">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراقچی و وزیر خارجه سوئیس در بورگن‌اشتوک دیدار کردند
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/15476" target="_blank">📅 11:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15475">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رادیو ارتش اسرائیل:
تغییر بزرگ در سیاست عملیات نظامی با محدودیت تقریباً کامل بمباران در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/15475" target="_blank">📅 11:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15474">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک منبع مطلع به ای ۲۴ نیوز:  یکی از اولین خواسته‌های آمریکایی‌ها در مسئله هسته‌ای - اجازه دادن به بازرسان آژانس بین‌المللی انرژی اتمی برای بازدید از سایت‌های هسته‌ای در ایران به منظور بررسی وضعیت به‌روز شده
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/15474" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15473">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مدیر دفتر شبکه المیادین در ژنو: دیدار‌های دو و سه جانبه در بورگن اشتاک آغاز شده که مقدمه‌ای برای نخستین نشست رسمی میان ایران و آمریکا است
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/15473" target="_blank">📅 11:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15472">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">المیادین نخستین نشست رسمی در سوئیس ساعت ۱۶ به وقت تهران برگزار خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/15472" target="_blank">📅 10:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15471">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/15471" target="_blank">📅 09:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15470">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آمریکا می‌خواهد دسترسی ایران به پول‌های مسدودشده‌اش را فقط به خرید «دارو و غذا» محدود کند تا ایران قادر نباشد توان نظامی خود را بازسازی کند
روزنامه وال استریت ژورنال:
آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/15470" target="_blank">📅 09:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15469">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک جلسه اضطراری برای رسیدگی به مناقشه بین اسرائیل و حزب‌الله لبنان به برنامه اولین روز مذاکرات صلح در زوریخ اضافه شده است
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/15469" target="_blank">📅 09:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15468">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">معاون رئیس جمهور آمریکا، جی. دی. ونس  وارد سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/15468" target="_blank">📅 09:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15467">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
کانالی که ترور هنیه و نصرالله رو دقیق پیشبینی کرده بود، دلار ۱۶۰ تومنی رو هم دو ماه پیش اعلام کرده بود از تاریخ و نحوه حمله ایران به اسرائیل پرده برداشت!!!
🚨
نمیدونم به کجا وصله ولی از همه چی خبر داره بیا خودت ببین
👇
👇
🔴
LINK - CHANNEL
🔴</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/15467" target="_blank">📅 01:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15466">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
کانالی که ترور هنیه و نصرالله رو دقیق پیشبینی کرده بود، دلار ۱۶۰ تومنی رو هم دو ماه پیش اعلام کرده بود از تاریخ و نحوه حمله ایران به اسرائیل پرده برداشت!!!
🚨
نمیدونم به کجا وصله ولی از همه چی خبر داره بیا خودت ببین
👇
👇
🔴
LINK - CHANNEL
🔴</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/15466" target="_blank">📅 01:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15465">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حسین پاک، خبرنگار مستقر در لبنان: از ساعاتی قبل عملیات نظامی از سوی اسرائیل متوقف شده است.
@withyashar</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/15465" target="_blank">📅 01:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15464">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بر اساس آخرین اخبار، ساعت قلعه نویی در مکزیک دزیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/15464" target="_blank">📅 00:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15463">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a879665e8e.mp4?token=gjsKnJggl1hM-2QBNQybmS29eF51FtnrZHYIRh9ZWgnj_YlLtbkb9RLozdaR2OjpNX1SSq_CpxVnH8aylUiRNLv-HHen8f2Lta_OQzbjxpK2XUWvGreqPrdb9WFOOt5eeyEUXna18A0Gq9lsHlhrHKM5K7pW0Y-iJOGkuYz9Afu3pUPgWbE_D9D5XvvYYqLK_18e0Ctq_Jj-K-ICpHqxnKdjRlGUocwsaNOvNFCz7gg2SYJT36Y6LiYnog2TzQ7bSKoVw7WHOe11TvXCRGKEgCTFN0-6enZdfVW3PA3GQtIn0TphJEdm0aBfUCbCn-MTtTaNiOawyZjnWH4nNOqEpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a879665e8e.mp4?token=gjsKnJggl1hM-2QBNQybmS29eF51FtnrZHYIRh9ZWgnj_YlLtbkb9RLozdaR2OjpNX1SSq_CpxVnH8aylUiRNLv-HHen8f2Lta_OQzbjxpK2XUWvGreqPrdb9WFOOt5eeyEUXna18A0Gq9lsHlhrHKM5K7pW0Y-iJOGkuYz9Afu3pUPgWbE_D9D5XvvYYqLK_18e0Ctq_Jj-K-ICpHqxnKdjRlGUocwsaNOvNFCz7gg2SYJT36Y6LiYnog2TzQ7bSKoVw7WHOe11TvXCRGKEgCTFN0-6enZdfVW3PA3GQtIn0TphJEdm0aBfUCbCn-MTtTaNiOawyZjnWH4nNOqEpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️جی‌دی ونس :
«من مشتاقانه منتظر شروع مذاکرات فنی با ایرانی‌ها، پاکستانی‌ها و قطری‌ها هستم...»
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/15463" target="_blank">📅 00:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15462">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سی‌ان‌ان: «ونس» از پایگاه هوایی مشترک اندروز، برای شرکت در مذاکرات با ایران راهی سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/15462" target="_blank">📅 00:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15461">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f0d58b03.mp4?token=eRRHjbGyRUpVbnEOZZlwwomgmDAp7xwmTAz90V_Zgf0sH11R0OglEH8US0ClFs0yBeH4v7ct0nrJkBLBW_Tml74t8rmB-le4c6-nbTUgd1FqOpnp-rSGEc1xQYVhyEoFZYsl62uNWHedtGjWvgeC3_p9r-tR1-gYD79xb3_r9ufFh_ctwUS7bW2cKDqQ0wBH1qMiml6AlZMQIFhHBRmxJrI0LyRVOBSJCb53b1Ipm6pD3MNNwIAC1kShSlcIDMERc9pMrsFdrUJNtLH9s28GUy51JlvqXQYxOIFJCfLu42kaeRCqTyC2kMXL_YtY8_h9NmXqC2DM3S7dMplXPAX7AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f0d58b03.mp4?token=eRRHjbGyRUpVbnEOZZlwwomgmDAp7xwmTAz90V_Zgf0sH11R0OglEH8US0ClFs0yBeH4v7ct0nrJkBLBW_Tml74t8rmB-le4c6-nbTUgd1FqOpnp-rSGEc1xQYVhyEoFZYsl62uNWHedtGjWvgeC3_p9r-tR1-gYD79xb3_r9ufFh_ctwUS7bW2cKDqQ0wBH1qMiml6AlZMQIFhHBRmxJrI0LyRVOBSJCb53b1Ipm6pD3MNNwIAC1kShSlcIDMERc9pMrsFdrUJNtLH9s28GUy51JlvqXQYxOIFJCfLu42kaeRCqTyC2kMXL_YtY8_h9NmXqC2DM3S7dMplXPAX7AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت مذاکره کننده ایران، با اسم میناب ۱۶۸، وارد زوریخ سوئیس شد.
ونس معاون ترامپ برای شرکت تو مذاکرات با ایران،راهی سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/15461" target="_blank">📅 00:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15460">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTiti</strong></div>
<div class="tg-text">سلام یاشار جان
باور کن محرم شده میرن بیرون الواطی برای همین  ری اکشنا اومده پایین
😐</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/15460" target="_blank">📅 00:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15459">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from۞۩ ¥𝕒z∂𝓐Ｎ۩ ⓪⓪:①②</strong></div>
<div class="tg-text">شیفت شبی آ فوتبال میبینن</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/15459" target="_blank">📅 00:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15458">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895fd89b8b.mp4?token=KQYAREHpOrj3Ny8LvsS7Pu3f46jd6-IU4RdikatZJvBlxBbB_IYTkkdBvaA_Ic1-QDQRLbQb53XaI3ebfNN8ltp5oJpIJoYonhdA-wbdFmLJdRcrsrk5hWEfIWznlwaANoVFKWlsbVDdVfKqwWvp1k9JwPXF4ik4-zkqcL-ObWZCYhjk-A97P_UPLiWtm6KDfeeQioVmgfP_ElF3rFFWj8PUP3vpdcEL96ugPtKjbJl5_4e_u3HgRgqYGLOWckCwZ_eDtNLViaZlJEmSOgoIpheJuZqw7YFTd-hf6TnrVC6waTVawOLwO2lWbpC-HoTJLuOYnwO-VX1KX1GT7j54ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895fd89b8b.mp4?token=KQYAREHpOrj3Ny8LvsS7Pu3f46jd6-IU4RdikatZJvBlxBbB_IYTkkdBvaA_Ic1-QDQRLbQb53XaI3ebfNN8ltp5oJpIJoYonhdA-wbdFmLJdRcrsrk5hWEfIWznlwaANoVFKWlsbVDdVfKqwWvp1k9JwPXF4ik4-zkqcL-ObWZCYhjk-A97P_UPLiWtm6KDfeeQioVmgfP_ElF3rFFWj8PUP3vpdcEL96ugPtKjbJl5_4e_u3HgRgqYGLOWckCwZ_eDtNLViaZlJEmSOgoIpheJuZqw7YFTd-hf6TnrVC6waTVawOLwO2lWbpC-HoTJLuOYnwO-VX1KX1GT7j54ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن همای سعادت در ارتفاع پنج هزار متری دماوند
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/15458" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15457">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/15457" target="_blank">📅 00:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15456">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بی‌بی‌سی‌: کیر استارمز نخست وزیر بریتانیا دوشنبه استعفا میده
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/15456" target="_blank">📅 23:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15455">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbHesoCu-tTxPsIk2LmkVgknVeLuOp8ap0GhZGR9646tNOxd2nzIb80UfrB_N9Z9-OM4YUNqUC8XFtgKbnLOPNGuOiXJV1I68n79FJClQlTLMc_ZqUpV8gHIUQgVtcq46lTPf4wcDjujt2PK0iVTNUP5W5xqgsmKWYgfizNdG4xx4PG09AkYdmGAdBQaMQGGOSllKnxeM9vMqvT8cnCD0sYfXzleIoQh-NzcabBuTHSZqnsh0r0Jb9Rd6vWbMltqvwRrGidl_36-v9e0-P-Jl2HLIpgjLjDuoCEQDWQ9lrYRU6SAXgbxBMw3rSd6xVhk9la4Nqn32Sdlkgu96ITdvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ..  ..
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15455" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15454">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVGjCYki4lAyIPBKzdRwf4Ae8ds4vu3cjaWqRwO36Xrva8lyTh-zH4yFsYLGz5cBQvaDvWFOl28OJwDNVJ9UWZGDnm_NvI46ArzMCj4rGeBqafnO6DT1LAo5Fy8xqN3LAe1XKBz1yp2XBJvWFUQC3tFauYSP0J3ildu0qg0XLDy_d1u5-qJ9GQRWtpJ598yWBqcphwvPTwwLHwfNoQkCCit2ZUQw1LFPERivyIvoUYGLP5bVlpSvKon-o9pdHf5gdn4Bh0uibw4DLN29AK_sjOd1vttQLOMPerSuG3THf25kQ61kFkppMi5j-gycPFZNjew1-ew0EgYhWI22REECEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هیئت ایرانیش 15 دقیقه دیگر در زوریخ به زمین خواهد نشست. @withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/15454" target="_blank">📅 23:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15453">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آی‌۲۴ نیوز نوشت که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به وزرای کابینه این کشور دستور داده از حملات به دونالد ترامپ، رییس‌جمهوری آمریکا خودداری کنند، اما مقام‌های ارشد در محافل خصوصی می‌گویند واشینگتن درک درستی از ایدئولوژی جمهوری اسلامی و حزب‌الله ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/15453" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15452">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اتاق جنگ با یاشار : مشروعیت حتما تا انتها ببینید  ، کلیک کنید کارای اداری یادتون نره  https://www.instagram.com/reel/DZ0c0MCxXpl/?igsh=cTR0Nm90ajdrbWRh</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15452" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15451">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">️خبرگزاری مشرق:
نبویان، نماینده مجلس، به ۲ـ۱۰ سال حبس محکوم می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/15451" target="_blank">📅 23:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15450">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ در‌تروث:  در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به…</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/15450" target="_blank">📅 23:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15449">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نایب‌رئیس شورای سیاسی حزب‌الله لبنان: تلاش‌های آمریکا و اسرائیل برای خلع سلاح حزب‌الله با شکست مواجه شده و تسلیم سلاح غیرممکن است
@withyashat</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/15449" target="_blank">📅 23:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15448">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هواپیمای هیئت ایرانیش 15 دقیقه دیگر در زوریخ به زمین خواهد نشست.
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/15448" target="_blank">📅 23:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15447">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اتاق جنگ با یاشار : مشروعیت حتما تا انتها ببینید  ، کلیک کنید کارای اداری یادتون نره  https://www.instagram.com/reel/DZ0c0MCxXpl/?igsh=cTR0Nm90ajdrbWRh</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/15447" target="_blank">📅 23:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15446">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کاور
🔥
@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/15446" target="_blank">📅 23:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15445">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzNABFBACXY9xxIAbITgDaNUouJnyE0N_Tp9H5Tja15FI_oXSPabQ8AWS4hpXUAUqeVxEr46AOVbziK288Y_fenfkBzqNJ1LYwqtlssieVs7nabYJmDGZflLjEYz_2gwv5Og4NW5Wo4Q8-LIN9ycyn1A2Uu36G7CKGP19zBUH8arWj8a78BlaMZPpeXoysyktcmuedGK5ttzRdCKCpmgvscA4cMNC8BzM39PbQ3eT0P3mwJSFszFyy0ky8OL9cuoBEk6B-0BKxdsk4-esJW__HyxTGzUm8tOhbYbDljWh7pZ9kwb7Y24QHGPyXxf1WxNMDycBLWTAmAebgkWfvQDzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث:
در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه شده است، به منظور بازپرداخت هزینه‌ها در گذشته، حال و آینده، اعمال شود.
از توجه شما به این موضوع متشکرم!!!
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/15445" target="_blank">📅 22:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15444">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIKW2pHfnNbMwDxFbd5f4GXe_OLOKZbLE43WdrRRnX5yyKxLf5eCjQK2rwoh2qs-hc_yM17U51tebKE6g4scLtKsbX6xTWDelCm3ND70pjkyHZ9BTBjpiA7UU8PjfzCiuMG_YYguW-T5S4s3epchzbLxfFm7t38O_SzxIE-F7SA8q7ZbSfXjdE7S8188TWxMvWFIuNXlegeJAhj2H_bBN-ZBfAv2-0wic2YLg4BrOScSs2Ln4D2a9I78GKV0REVJ01C08yYqRlFgaa016Tv_OiyYXoqBi0svKKPpNpZnbSEMWuBIKwZGQjXBWGrco3_YDVvIoMS_ddhNIETEyvjThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
🔥
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/15444" target="_blank">📅 22:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15443">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/15443" target="_blank">📅 22:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15442">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/15442" target="_blank">📅 22:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15441">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15441" target="_blank">📅 22:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15440">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15440" target="_blank">📅 21:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15439">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره گفت که ارتش اسرائیل به سنتکام اطلاع داده است که به واحدهای خود دستور داده است که به آتش‌بس در لبنان پایبند باشند
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/15439" target="_blank">📅 21:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15438">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrkota_kM1__7nn7DFzZLp0qXaySNnhpNbRuU5V1GAel9_zIqC09t9FC15jaETfRKIx7zX6-WGghEvMxwK3EW_BEr7YGJaHglyn-cUVv9cR86G3Xl67YBjQrfBFm8Qlp482JI5D6a1UJ5Nu98rs4XS3wlT8aDdphGaZFY8C0VFaU0IKgMGaQw5v6yDrNTAqeurY4TxUvs-kjL2iFDPQq3XKV0HNfOsVVAesBbK6L07cHUv8-tsjx5R3ShJNa72LdGekIQVlvkfr12f39R6x7U34q30axkLczwE83wjUKu1VDEFazqf1oTvbBvO4V2qyA6qyJmKYFnYRn2fG4I_6eHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار وزیر کشور پاکستان با پزشکیان
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/15438" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3cb82d210.mp4?token=YymzmKVyuCueBl7pNZbjB5CLsjJyVlU7fMvAj1MR0zWBt31ANUbnMSTsHqaaz1yNAjA-co1iRiXTvfzHg1dv_s0wBS_vcTRG-STo2CpKeCjQ63HafvzMY-Qb5oe9J22Tw5DwbPDEPkCorSGDLTJyTM-gCHjXG94Iq1ITBlRcRMohGW6mujfW_sIrOJZIBZF1wyFpLSiUZj3SfttGYYY4M2bGsFhJgCVhMvp9XM15liKdrh8EqZhqIUcLXA5U5JuZyZzPb5tKMl2IOOn4IoLuY7e_VQQ5cY9c55oMuxLvvqstYYHxRVnBe6Pt0GdHwmq1zez0h8NVyVnkjTDVBHFcmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3cb82d210.mp4?token=YymzmKVyuCueBl7pNZbjB5CLsjJyVlU7fMvAj1MR0zWBt31ANUbnMSTsHqaaz1yNAjA-co1iRiXTvfzHg1dv_s0wBS_vcTRG-STo2CpKeCjQ63HafvzMY-Qb5oe9J22Tw5DwbPDEPkCorSGDLTJyTM-gCHjXG94Iq1ITBlRcRMohGW6mujfW_sIrOJZIBZF1wyFpLSiUZj3SfttGYYY4M2bGsFhJgCVhMvp9XM15liKdrh8EqZhqIUcLXA5U5JuZyZzPb5tKMl2IOOn4IoLuY7e_VQQ5cY9c55oMuxLvvqstYYHxRVnBe6Pt0GdHwmq1zez0h8NVyVnkjTDVBHFcmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قمیشی : به عمویم سیاوش قمیشی گفتم ترامپ برادرت را کشت
سیروس قمیشی
برادر سیاوش قمیشی (خواننده و آهنگساز مشهور ایرانی) بود و پدر «امیر قمیشی» (از تهیه‌کنندگان و برنامه‌سازان تلویزیون رژیم) به شمار می‌رفت. وی در جریان بمباران بیمارستان گاندی تهران کشته شد و طبق گزارش‌های خبری، تنها یک روز تا زمان ترخیص و پایان درمان وی باقی مانده بود
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/15437" target="_blank">📅 21:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نبویان، نماینده مجلس: آمریکا بعد از شهادت آقا از طریق یکی از کشورهای اروپایی، پیام داد که بیایید مثل ونزوئلا تسلیم شوید!  وی‌در ادامه با دلایل بسیار گفت  ماجرای مذاکرات رسما کودتای آقایان علیه رهبری بود! و صدا و سیما هم حرفاشو قطع کرد ! @withyashar
🚨</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15436" target="_blank">📅 20:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">@withyashar
ماجرای ببر از زبان امیر تتلو حالا شد جریان عاصم منیره پاکستان</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15435" target="_blank">📅 20:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الحدث به نقل از یک منبع آگاه: نخست‌وزیر پاکستان و مارشال عاصم منیر فردا در مذاکرات سوئیس شرکت خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/15434" target="_blank">📅 20:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">لیست هیئت اعزامی ایران به سوئیس به ریاست قالیباف
محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیئت مذاکره کننده ایران
سید عباس عراقچی، وزیر خارجه
علی باقری کنی، معاون بین‌الملل دبیرخانه شورای‌عالی امنیت ملی
عبدالناصر همتی، رئیس کل بانک مرکزی
حمید بورد، معاون وزیر نفت و رئیس شرکت ملی نفت ایران
کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزیر خارجه
اسماعیل بقائی، سخنگوی وزارت خارجه
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/15433" target="_blank">📅 20:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نبویان، نماینده مجلس: آمریکا بعد از شهادت آقا از طریق یکی از کشورهای اروپایی، پیام داد که بیایید مثل ونزوئلا تسلیم شوید!
وی‌در ادامه با دلایل بسیار گفت  ماجرای مذاکرات رسما کودتای آقایان علیه رهبری بود! و صدا و سیما هم حرفاشو قطع کرد !
@withyashar
🚨</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15432" target="_blank">📅 20:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مقام اسرائیلی: ارتش اسرائیل طی دو روز گذشته به 300 هدف حزب‌الله حمله کرد و 100 نفر از نیروهای این گروه رو کشت.
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/15431" target="_blank">📅 20:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بلومبرگ: عراق به میادین نفتی بزرگ دستور داده است که تولید خود را به بیش از ۳ میلیون بشکه در روز افزایش دهند، زیرا صادرات از طریق تنگه هرمز به تدریج پس از توافق آمریکا و ایران بهبود می‌یابد.
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/15430" target="_blank">📅 20:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مقامات ارشد ارتش اسرائیل به کانال 12 اسرائیل اعلام کردند:
عملیات نظامی در سراسر جنوب لبنان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/15429" target="_blank">📅 19:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سنتکام بعد از ادعای بسته شدن تنگه : نیروهای آمریکایی همچنان در منطقه حضور دارند و هوشیار هستند تا اطمینان حاصل شود که همه جنبه‌های توافق با ایران رعایت، اجرا و به طور کامل اجرا می‌شوند و همچنین مرکز مشترک اطلاعات دریایی با صدور اطلاعیه‌ای، عبور ایمن برای همه کشتی‌ها در امتداد مسیر تعیین‌شده را که عاری از هرگونه ادعا یا مانع خودسرانه است، تأیید کرد.
تردد کشتی‌های تجاری در تنگه هرمز در ۲۰ ژوئن افزایش یافت، زیرا نیروهای آمریکایی به عملیات خود در منطقه عمومی برای حمایت از آزادی ناوبری ادامه دادند.
امروز عبور ایمن از این آبراه بین‌المللی همچنان برقرار بود و ۵۵ کشتی تجاری در حال عبور بودند و مقادیر زیادی بار و بیش از ۱۷ میلیون بشکه نفت را به بازارهای جهانی منتقل می‌کردند.
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/15428" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو با دستور توقف جنگ گفت که این دستورالعمل‌ها شامل عقب‌نشینی از مناطق تحت کنترل نیروهای اسرائیلی در جنوب لبنان نمیشه و مناطق تصرف شده، تحت تصرف باقی میمونه.
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/15427" target="_blank">📅 19:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">محمد جواد ظریف: از مذاکرات استقبال میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15426" target="_blank">📅 19:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsBJ-BtwT4lPZpKgb_iJZihYHmq6JYl4VXVA39KFHI9LMu5TwX56KD820LGDL6RyBQHkqSvfAAAZRvJ_oIAPZoeZwlInl-OMl-pXb-wHUngJXO-c8VBSWB7zfkQK7KITRfqIAE66KbChIqpbbRXaSLLXcpMJFnfUarTQus5apuQ5qcpo3Jdb7DoO8xzBkjvHGbv96nj0cTiQiEm4KBdUUxHsWllkeNi_ffocrZhH6NN-BwzVK5WTroU5ACXt32wV4YkHBQrkDe7VoLTDuN_eT29j7osq8SGrg4fcZDE8e0tek57Nxu8SAd4SBmQHHF0arWL-Njfn6FSYGhemd6FA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه اولین تیمی شد که از جام جهانی حذف شد.
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/15425" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هم اکنون جی دی ونس به فاکس نیوز :
ما هیچ مدرکی مبنی بر اینکه ایرانی‌ها هنوز تنگه هرمز را می‌بندند، نمی‌بینیم.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15424" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سخنگوی تیم مذاکره‌کننده: طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/15423" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بقایی: سفر به ژنو فاز دوم مذاکرات نیست و صرفا برای امضای یادداشت تفاهم به صورت حضوری است
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/15422" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15421">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فاکس نیوز به نقل از ونس، معاون ترامپ: اوضاع در مذاکرات با ایران خوب پیش میره و انتظار دارم به سوئیس سفر کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15421" target="_blank">📅 17:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15420">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ایسنا: هیات مذاکره کننده ایران تا دقایقی دیگر عازم سوئیس می‌شوند
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/15420" target="_blank">📅 17:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15419">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الحدث: عراقچی امشب همراه وزیر کشور پاکستان به سوئیس سفر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15419" target="_blank">📅 17:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15418">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تندروها معتقدن کودتای قالیباف تکمیل شده و الان قدرت اصلی کشور دست قالیبافه. چون با اینکه رهبر‌ گفته توافق خوب نیست ولی مجری های صداوسیما میگن توافق خوبه
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/15418" target="_blank">📅 17:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15417">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فایننشال‌تایمز: پایان عملیات نظامی اسرائیل در لبنان بعید است
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/15417" target="_blank">📅 17:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سخنگوی وزارت خارجه:
هیئت ایرانی برای پیگیری و مطالبۀ اجرای تعهدات طرف مقابل به سوئیس سفر خواهد کرد.
در سوئیس قرار است دربارۀ اجرای تعهدات طرف مقابل مطالبه‌گری داشته باشیم و مشخص شود آن‌ها چطور می‌خواهند به تعهداتشان عمل کنند.
ما به تعهداتمان پایبند بودیم و طرف مقابل موظف است اسرائیل را به توقف حمله به لبنان وادار کند.
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/15416" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15415">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d9156929.mp4?token=rJM4vF4j8fJNLsI--tQbEYPr_edBMb7k3dWz_3yHfREe898BfSmtaO0k0xJC9D9qsJu8DzLzt8L8YWuwv-T0pi48aKwGlg0nHOeNmwhZWYB9j0DSMpdOKN4NKVd0_nzOH4Vu1VyS3-RIOij-XqAeB95a90m9Ex9tsVD1AaYS8d-UjvBXWNo5FOxedMZ0sxa59C1HjtdN77nYkTEPb9H2dQCTYGm6zs2kOMulTW4gB8fQYbIAAdODQBQ8eHbZHnXDvCm6l2uplpGaGyNyRZaq6jkLNRFZJ2_DoVE2At4xpRG5lY8Y9PyNRZlbXsZXTxGlNc5ybng1r91khNwhPurdWxlv-sTmjub7nfssZz6JuFjh4g4u92DaAJV3i9Tq50C40N6-MAPXRrArMicWwYHqif1ZjsHj2aLG33fWOdUDuButsiHlPDl0qitUfiNHAfii7Vsdq52eEp4_8dZfbb_iP2_twO8W7561OjxhcuhoAh_oasrWviDZJgQqPCczi8h5n0vyaxWRDNYBaiyloPEUWjY6uSrOd5VcHRaZ9x00ogWHhVrnTOLQN-v1afMl48TzT3ojZACNONaJNUbzfGmh6CMaac19WBd8rAhqmDGMXyMKD7Jl2KKTqk2RZgyH0m_2QzLEDbSQouvpVfGnByRQv_uNexJHkauBj7XJb6dilCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d9156929.mp4?token=rJM4vF4j8fJNLsI--tQbEYPr_edBMb7k3dWz_3yHfREe898BfSmtaO0k0xJC9D9qsJu8DzLzt8L8YWuwv-T0pi48aKwGlg0nHOeNmwhZWYB9j0DSMpdOKN4NKVd0_nzOH4Vu1VyS3-RIOij-XqAeB95a90m9Ex9tsVD1AaYS8d-UjvBXWNo5FOxedMZ0sxa59C1HjtdN77nYkTEPb9H2dQCTYGm6zs2kOMulTW4gB8fQYbIAAdODQBQ8eHbZHnXDvCm6l2uplpGaGyNyRZaq6jkLNRFZJ2_DoVE2At4xpRG5lY8Y9PyNRZlbXsZXTxGlNc5ybng1r91khNwhPurdWxlv-sTmjub7nfssZz6JuFjh4g4u92DaAJV3i9Tq50C40N6-MAPXRrArMicWwYHqif1ZjsHj2aLG33fWOdUDuButsiHlPDl0qitUfiNHAfii7Vsdq52eEp4_8dZfbb_iP2_twO8W7561OjxhcuhoAh_oasrWviDZJgQqPCczi8h5n0vyaxWRDNYBaiyloPEUWjY6uSrOd5VcHRaZ9x00ogWHhVrnTOLQN-v1afMl48TzT3ojZACNONaJNUbzfGmh6CMaac19WBd8rAhqmDGMXyMKD7Jl2KKTqk2RZgyH0m_2QzLEDbSQouvpVfGnByRQv_uNexJHkauBj7XJb6dilCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگه بابا جنگه !!!
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15415" target="_blank">📅 16:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15414">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تسنیم: نیازی به دیدار ویتکوف و عراقچی نیست.
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15414" target="_blank">📅 16:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15413">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تنگه هرمز مجددا بسته شد
قرارگاه مرکزی حضرت خاتم‌الانبیا:
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامهپایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم مظلوم این سرزمین و همچنین با توجه به عدم عقب‌نشینی نیروهای اشغالگر صهیونی از اراضی جنوب لبنان، اعلام می‌دارد تنگه هرمز به روی تردد شناورها بسته خواهد شد.
متذکر می‌گردد این گام اول پاسخ به عهدشکنی دشمن است و در صورت ادامه تجاوز گام‌های بعدی برای پایبند کردن دشمن به اجرای تعهدات برنامه ریزی و اقدام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15413" target="_blank">📅 16:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15412">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYyv8AV9oulYI_QCCCiZyLu34PDhjUsLVL0j8dVif9C1uStHtc2e3y5RR3Q1gUw_6BNabNjfylJr-eWaaqSCBdukucmbsjheB2hUbgsCHLADvbKK__dwpaUtoO4lXtNHVhVL0C7te146QhgPea_I3ElZl8L_4zdBoWKALvVMACLU2L7aXNXFmMcO7VuVvlbdfy_MX_mHkGkGyb8gYDPznHkQOEsLv82eEY6rw3lgU_hYcOYDxtYgvv6o0wk0oHz_WpiiJdDpELjCm1xnMRm4GMVhNSsQCyh6Fcckjk_pjKQXvLzPvIbZ30DN7XWVxDmpAnz4H9BsSZ16-XOEI4N3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ
خبری
درباره تاثیر خود بر آینده سیاسی نتانیاهو را بازنشر کرد
دونالد ترامپ:
«ترامپ برگ‌های برنده را در سرنوشت انتخاباتی متزلزل نتانیاهو در اختیار دارد.»
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/15412" target="_blank">📅 16:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15411">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37917b1e44.mp4?token=gguHt8D3q5N70DrIE-vmTkDgOxfvYmFaOz6rxv0rJ6UzT_Gqs7FQThviyoMaB6h0BFAqusR_07NzEKPhwtNTA5teHWVJ2wjhPu0wXa0_IztN11x8pMuRlKWF87PbseYStN95HXws8-MUKuedvCkFemGZAFXq3pzVoXxLyLX8nV6FMyz7YizmaoNVeTKHcaG5guZDp1eqkTopA4q5ZhXLvkgfSZAZZX-lvNDtn-mOldHuy4bSuubVV2nPzHP8zQ5bDjpbbvxBHeS40F4WCOmr9ZFp6LT5Bs8EdkOGAPnRS7r2fCkCqRi5r9PFVLlFN5MSiJARTfUrTs0nG0xccrcJbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37917b1e44.mp4?token=gguHt8D3q5N70DrIE-vmTkDgOxfvYmFaOz6rxv0rJ6UzT_Gqs7FQThviyoMaB6h0BFAqusR_07NzEKPhwtNTA5teHWVJ2wjhPu0wXa0_IztN11x8pMuRlKWF87PbseYStN95HXws8-MUKuedvCkFemGZAFXq3pzVoXxLyLX8nV6FMyz7YizmaoNVeTKHcaG5guZDp1eqkTopA4q5ZhXLvkgfSZAZZX-lvNDtn-mOldHuy4bSuubVV2nPzHP8zQ5bDjpbbvxBHeS40F4WCOmr9ZFp6LT5Bs8EdkOGAPnRS7r2fCkCqRi5r9PFVLlFN5MSiJARTfUrTs0nG0xccrcJbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در طول ۲۴ ساعت گذشته، نزدیک به ۲۰ شناور از تنگه هرمز عبور کرده‌اند.
از این تعداد، ۵ شناور از مسیر امن تعیین‌شده توسط ایالات متحده که از آب‌های عمان عبور می‌کند، استفاده کرده‌اند.
بقیه شناورها از طرح جداسازی ترافیک ایران استفاده می‌کنند.
در حال حاضر دو مسیر اصلی برای عبور کشتی‌ها از تنگه هرمز وجود دارد
اول ، طرح ترافیکی ایران (TSS) که همان مسیر اصلی و همیشگی تنگه هرمز است که عمدتاً نزدیک سواحل و جزایر ایران قرار دارد.
مسیر دوم کریدور موقت ایجادشده توسط آمریکا در آب‌های عمان و دورتر از سواحل ایران و طراحی‌شده در زمان جنگ و موقت.
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/15411" target="_blank">📅 16:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adN1QAve1EcZqxHEPnXTz8OVsAO25dPuMcyWCgsrT-C6HkXFey1oejUz83IRMJ48Odc1AydnYBVG6Zq5lifcDWREurawNXYjxr6wciRTS4TKNwgbHlEu8eOKab2mYn0HKEt_yVshCAvcHzH2CXR-HrqHLQ3nbXd7r32ZKI8Bh2HmntDd3uBrtt28pR3LgBYnzzFeX6B9fh5JMgnWj5GI-bne879sdHV94BkefB8jad5sweSaWQ9cctL2eL895bE9x5DIkLzXuCRfFdFSM9ZBBThs_FIWZ-HybxYagIj_4doxn0QCLGCdnZifNhpd4QRw6KmCFkroFK9vIRMSnv39rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه سوئیس: مذاکره آمریکا و ایران در فضایی محرمانه در بورگن‌اشتوک ادامه خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/15410" target="_blank">📅 16:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15409">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cthvs9MEoaKZz37iHEZXW0E--GiB7rQ2ofFXLCAnCdfNt5naxfPGD7kBwVGRKALwo9EvvAVG4NPWMCVLV7OzuN6KpW6PyXdb9tY1N3t3BsFJYEn7L3qFkiNovq5DmFpGAs074obqkK1NeRDVYuksKV6hYZCYR7yS4Ybsd6j4-lacJH693yezBR2otjCBEvjSnGUM84yqz1KUp-o6WeM0W6hjAFzqFBYT0B4o0r-l0vw_CPoLiewSUqZHoadWRkuIip8-lnoSKfia_oXWf7ffQyaYotTwQMEwVEYaZuBP1B8KJu_wgjE_MUKmRnTBioZf0qazCZ6EquKUPm9MTNADxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در ‌تروث :
جورجیا ملونی، نخست‌وزیر ایتالیا، در طول نشست گروه ۷ در فرانسه، بارها و بارها از من خواست که باهم عکس بگیریم. اون در ایتالیا از نظر میزان محبوبیت وضعیت ضعیفی داره؛ احتمالا به این دلیل که وقتی نوبت به جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران رسید، به ایالات متحده آمریکا—کشوری که واقعا ایتالیا رو دوست داره و از آن محافظت می‌کند—پشت کرد (البته ناتو هم در این مورد همین کار رو کرد!).
اون حتی اجازه نداد از باندهای فرود یا باندهای پرواز ایتالیا استفاده کنیم، که یک دشواری لوجستیکی بزرگ بود؛ آن هم با وجود این واقعیت که ایالات متحده سالانه صدها میلیارد دلار برای محافظت از ایتالیا و دیگر متحدان «به اصطلاح» ناتو هزینه می‌کنه. حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، اون می‌خواد دوباره با ما دوست بشه تا «آمار محبوبیتش» رو بالا ببره.
نه، خیلی ممنون!!!
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/15409" target="_blank">📅 15:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15408">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fc382a14.mp4?token=lqCmux8ZNjPzHEyV7xWecQUdVhTEQmI6y-gtbLks5gK7L-dywdbr-rRqCJiQRKk4YF57MozAdMrZnBy0NE3NzjRsddxrTdnWhUKaIgEx_DnHJrCwoE8sObItB9C-bUK3oyGCMgQP5ru9sSidFSIXsw3X6Bx2crHeS55N-RYcoW0jO8z7vTgXsKktXUfjII1aQIKfRHari9ZegptSyHhYGmzAQtlmA9htGCnpi9vbUPrfdW7DXnkl_MY3NL6ImhuIqmx6HCUsZ8KEZzEp93zc5BmGu81zG2suFb6x6q1cJv5DRE2WTuq_J4PRNIdQRiF-KgldDGbmZPNXMR5c-8xPsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fc382a14.mp4?token=lqCmux8ZNjPzHEyV7xWecQUdVhTEQmI6y-gtbLks5gK7L-dywdbr-rRqCJiQRKk4YF57MozAdMrZnBy0NE3NzjRsddxrTdnWhUKaIgEx_DnHJrCwoE8sObItB9C-bUK3oyGCMgQP5ru9sSidFSIXsw3X6Bx2crHeS55N-RYcoW0jO8z7vTgXsKktXUfjII1aQIKfRHari9ZegptSyHhYGmzAQtlmA9htGCnpi9vbUPrfdW7DXnkl_MY3NL6ImhuIqmx6HCUsZ8KEZzEp93zc5BmGu81zG2suFb6x6q1cJv5DRE2WTuq_J4PRNIdQRiF-KgldDGbmZPNXMR5c-8xPsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون خمین
🚨
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15408" target="_blank">📅 15:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15406">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ex2xiQvyaO9lIEKKOMjqi92uNLsQUPziQTiT9Cd_Rah27EyThIHhIHsff7N6uFrncPAKIbJGmb2yt3RpKbnUL-pzIL1Dq0YjMvZskgVTM3ysL1AqMlp1lb3HH41qfnUXYcvIYCB7W4maDm-Q-6SYhq7OGQhrkNwHTvR78GczNDJeiwSXZVuNyl40A3J4CTzmGdRMOxvqHZeW9dz1x7SubELb3q8e7eIwnPuApHYWXSEedmJhVg8BtPBScqvR7lHVzx-OThrJeG1Hdk9ddELiL3lEax3RcWPq9cs4TH8xexBO4Ukp4arKrtr5lu-iAQImZOZ4f4SHzteAezoo7p1A5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث برای بار هزارم : خنده‌داره که چطور دموکرات‌ها دوست دارن بگن ایران امروز در موقعیت قوی‌تری نسبت به سه ماه پیش قرار داره، با وجود اینکه از نظر نظامی شکست خوردن، نه نیروی دریایی دارن و نه نیروی هوایی. به همین دلیله که من بهشون میگم دموکرات!!! رئیس جمهور دی‌جی‌تی
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/15406" target="_blank">📅 15:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15405">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فاکس‌نیوز: ویتکاف و کوشنر در سوئیس هستند
شبکه خبری فاکس‌نیوز اعلام کرد، بنا به گزارش‌ها، استیو ویتکاف، فرستاده کاخ سفید، و جرد کوشنر، امروز برای اولین دور مذاکرات در مورد توافق هسته‌ای احتمالی ایران در سوئیس هستند، در حالی که اسرائیل به اهداف حزب‌الله در لبنان حمله می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/15405" target="_blank">📅 15:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15404">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خبرنگار صداسیما: شاهد یکی از شدیدترین حملات به منطقۀ نبطیه هستیم؛ نبطیه تقریبا خالی از جمعیت شده
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/15404" target="_blank">📅 15:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15403">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/15403" target="_blank">📅 14:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15402">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">@withyashar
خاطرات شمال</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/15402" target="_blank">📅 14:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15401">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15401" target="_blank">📅 14:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15400">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/15400" target="_blank">📅 14:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ در تروث : چپ‌های افراطی و دموکرات‌های احمق دارند می‌بینند که ما در جنگ علیه ایران چقدر خوب عمل کرده‌ایم، به‌طوری که کشورشان از نظر نظامی به‌طور کامل شکست خورده است. اوباما فقط میلیاردها دلار پول نقد به آن‌ها می‌داد و هرگز از ارتشِ آن‌زمانِ تضعیف‌شده‌مان برای کاری که باید انجام می‌شد استفاده نکرد تا بزرگ‌ترین حامی تروریسم در جهان، یعنی ایران، مهار شود. آن‌ها کوچک‌ترین احترامی برای او قائل نبودند. آن‌ها فکر می‌کردند او، مثل جو خواب‌آلود بایدن، رهبری ضعیف و بی‌اثر است، و در این مورد ۱۰۰٪ درست می‌گفتند. ایران ۴۷ سال از مجازات برای “جنایت” گریخت، تا وقتی که من آمدم. بعد همه‌چیز تغییر کرد. آمریکا بازگشته است!!!
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/15399" target="_blank">📅 14:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/872d942820.mp4?token=MWJX2sHYlbBM7oLNXzhh6jqPdUswIlezCFkCvLitQei8wKKty-tY0PxegBSQvYPl7VuKOsPJkMnxzUsJteIRXAAV3WHBtZTHgkykxMotbGABYeaMgTSV-EsuAe3rUwPjJD6cdU7Fc1zNGmZ-dlpXO3z_9dCpT4MgiPSVs4Ifpwocg63ODef_WHmULYCgTmudTX3Lma6SnHL7UWrQLeSgp49efxwe3vK0uDhSy3AosD2nPBL6eMDn2NQhPpGyuoT7jWLg1uBHGJqdwpGJHrCmseMT7woVbUo-VwAnhjX8e2YaPzS3EF_74eiMmeng85P-9WqivFJHFQdU_TLPE1Jqnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/872d942820.mp4?token=MWJX2sHYlbBM7oLNXzhh6jqPdUswIlezCFkCvLitQei8wKKty-tY0PxegBSQvYPl7VuKOsPJkMnxzUsJteIRXAAV3WHBtZTHgkykxMotbGABYeaMgTSV-EsuAe3rUwPjJD6cdU7Fc1zNGmZ-dlpXO3z_9dCpT4MgiPSVs4Ifpwocg63ODef_WHmULYCgTmudTX3Lma6SnHL7UWrQLeSgp49efxwe3vK0uDhSy3AosD2nPBL6eMDn2NQhPpGyuoT7jWLg1uBHGJqdwpGJHrCmseMT7woVbUo-VwAnhjX8e2YaPzS3EF_74eiMmeng85P-9WqivFJHFQdU_TLPE1Jqnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون خمین
🚨
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/15398" target="_blank">📅 14:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15397">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">العربیه :  مذاکرات تا اطلاع ثانوی لغو شد. هیات آمریکایی و هیات ایرانی سفر خود به سوئیس را لغو کردند
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15397" target="_blank">📅 14:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15396">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دولت هلند اعلام کرد مسیر حرکت یک ناوچه پدافند هوایی خود را به سوی تنگه هرمز تغییر داده است تا در صورت تشکیل یک مأموریت بین‌المللی احتمالی در این آبراه راهبردی، امکان مشارکت در آن را داشته باشد به گفته وزیر دفاع هلند،
رسیدن آن به محدوده تنگه هرمز چند هفته زمان خواهد برد.
این تصمیم در حالی اعلام شده است که فرانسه و بریتانیا برای ایجاد یک مأموریت چندملیتی دریایی در تنگه هرمز تلاش می‌کنند.
آلمان نیز روز پنجشنبه اعلام کرد دو کشتی خود را برای آمادگی جهت مشارکت احتمالی در مأموریت نظامی در تنگه هرمز به دریای سرخ اعزام می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/15396" target="_blank">📅 14:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15395">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرگزاری NBC به نقل از یک مقام آمریکایی اعلام کرد «نیروهای ایالات متحده به عملیات خود در منطقه برای حمایت از آزادی کشتیرانی ادامه خواهند داد و اجازه حمله به هیچ کشتی‌ای را نخواهند داد.»
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/15395" target="_blank">📅 13:51 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
