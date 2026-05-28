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
<img src="https://cdn4.telesco.pe/file/un6TNAbWI5MzWD1nf511yrkNGLxTULc1XXLbtUhaeLl5eDD5wxYwEz64CBcO9hR1AusC-niWIYeESjMc9FZw_NsNPmLKxfNDt0TAsBhOuF3F_TSfJE_phpDneo6EFr_6y_Nznnh_Awu4SsEWiTgEySbEmmDk6T1AAv6dVQlUW4XfhH6lOnyD-pzcCAuk91QezI3oA_3xmoi6inOBQpc3mOoDK4KxNZRfDOXtKOCEC8ozjVfuiYimOp5BnNsPikB73_-xkvXC1YMb-R-HT7Q68OIvEDHrrTjTrhSNR4up1GlkXP694QKdx74IAVBcwEu2m4IEocjwAde9ymetcMHOgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 278K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 10:05:14</div>
<hr>

<div class="tg-post" id="msg-12773">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آمریکا «نهاد مدیریت آبراه خلیج فارس» را تحریم کرد
وزارت خزانه‌داری آمریکا اعلام کرد سازمان تازه تأسیس ایرانی «نهاد مدیریت آبراه خلیج فارس»  را به فهرست تحریم‌های خود اضافه کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/withyashar/12773" target="_blank">📅 10:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12772">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6fdcea6c.mp4?token=VENfzIgsMpAYfE11TfW5AfgRFyLGGuSySzvE_0ENpvXd_rAyCeOhgEZXTZF1MxD2lz53SXM_o7jKQWy44tpbTc5d6H4z7hrbjTxFzrUuFTZ-V3j0DTwH0cdggYXqMWBbzXdgnUaw_LxkB7bLXdq2onlhLatVEJroixnO23bXwB4aqyYrIw2OgQvZKmBX2Ql6bjb8A7v3zC0q8k5l2YhgKSaTSdnEFBHsQbExAPfgJOHkxNm1Y54ykA0EoQ0DOyizSrscQ5AqPmSvluBfTznqySttKFmyLvz5VXsdkC18D07aM9kX-NypdbjUx7NTKnRZ3yDDMy-tLVhycG3OAEH-HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6fdcea6c.mp4?token=VENfzIgsMpAYfE11TfW5AfgRFyLGGuSySzvE_0ENpvXd_rAyCeOhgEZXTZF1MxD2lz53SXM_o7jKQWy44tpbTc5d6H4z7hrbjTxFzrUuFTZ-V3j0DTwH0cdggYXqMWBbzXdgnUaw_LxkB7bLXdq2onlhLatVEJroixnO23bXwB4aqyYrIw2OgQvZKmBX2Ql6bjb8A7v3zC0q8k5l2YhgKSaTSdnEFBHsQbExAPfgJOHkxNm1Y54ykA0EoQ0DOyizSrscQ5AqPmSvluBfTznqySttKFmyLvz5VXsdkC18D07aM9kX-NypdbjUx7NTKnRZ3yDDMy-tLVhycG3OAEH-HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
رد موشک های ۳پا در امیدیه خوزستان که به سمت کویت میرفت
@withyashar</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/withyashar/12772" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12771">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اکسیوس: ایران چهارتا پهپاد انتحاری  به سمت یک ناو نیروی دریایی آمریکا و یک کشتی تجاری پرتاب کرد  نیروهای آمریکایی پهپادها رو رهگیری کردن و همچنین یک واحد پرتاب پهپاد ایرانی دیگه رو روی زمین قبل از اینکه بتوانه شلیک کنه، هدف قرار دادن
@withyashar</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/withyashar/12771" target="_blank">📅 09:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12770">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فاکس نیوز: آمریکا یه ایستگاه کنترل زمینی ایران رو تو بندرعباس زده؛ همون جایی که قرار بوده یه پهپاد تهاجمی ازش بلند شه.
به گفتهٔ مقام‌های آمریکایی، چهار تا پهپاد انتحاری دیگه هم که تو تنگه هرمز تهدید محسوب می‌شدن، زده شدن.
@withyashar</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/withyashar/12770" target="_blank">📅 09:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12769">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">۳پا یک پایگاه هوایی آمریکایی را هدف قرار داد
روابط عمومی ۳پا طی اطلاعیه‌ای اعلام کرد:
به دنبال تعرض سحرگاه امروز آمریکا به نقطه‌ای در حاشیه فرودگاه بندر عباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع تر خواهد بود.
مسئولیت عواقب آن با متجاوز است.
@withyashar</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/withyashar/12769" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12768">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مقام آمریکایی به شبکه CBS نیوز گفت : آتش‌بس با ایران پس از حملات امشب همچنان در حال اجرا در نظر گرفته می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/12768" target="_blank">📅 03:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12767">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">«رویترز» به نقل از یک مقام آمریکایی گزارش داد:   ارتش آمریکا حملات هوایی جدیدی را علیه یک سایت نظامی ایران انجام داد که تهدیدی برای نیروها و ناوبری ما در تنگه هرمز محسوب می‌ شد @withyashar</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/12767" target="_blank">📅 03:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12766">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/12766" target="_blank">📅 03:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12765">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12765" target="_blank">📅 03:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12764">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارشات تأیید نشده از ترور سردار علی عظمایی، جانشین سردار علیرضا تنگسیری، فرمانده نیروی دریایی سپاه. @withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/12764" target="_blank">📅 03:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12763">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/12763" target="_blank">📅 03:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12762">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ، به شبکه فاکس نیوز: مذاکره با ایران درباره کنار گذاشتن غبار هسته‌ای به دلیل تضاد در تصمیمات ایران، رفت و برگشت دارد تأسیسات هسته‌ای ایران تحت نظارت مداوم ۹ دوربین، ۲۴ ساعته قرار دارند. هرگونه تحرک ایرانی در داخل تأسیسات هسته‌ای با واکنش مستقیم نظامی…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/12762" target="_blank">📅 03:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12761">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8116492af1.mp4?token=nsT8ZUP7c-sO-Yi6ztsSWN4wMQvpDYoyv3Qb76GXvJDDghxff1QybMkSHJlBVaEoPrKIZzEsw7cbUM0ivHkf7s8sXaR1hUpI-KozZCc61ra5rP7Y3gY6YCoe3xalBobbYIG-NZQNjhKa4vP76SIfcvA-SCDA6x2Ptx01orj0P00xB_G77IoPa9NfzMCdp4DyfuwmYcAmpCK-ujTXsP8ivT192EbIIIr6DT3spr9tJUpz1YL3RAQ4uwjSWWUk6UkXJRY38XbZ4XsAFDTWvKTHvsxut3u-D9cvGczqJGRm3N8Tg_ErRqXtrD9wJ4t5I071yeJ2F3hOd-RWZgQO-QNXRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8116492af1.mp4?token=nsT8ZUP7c-sO-Yi6ztsSWN4wMQvpDYoyv3Qb76GXvJDDghxff1QybMkSHJlBVaEoPrKIZzEsw7cbUM0ivHkf7s8sXaR1hUpI-KozZCc61ra5rP7Y3gY6YCoe3xalBobbYIG-NZQNjhKa4vP76SIfcvA-SCDA6x2Ptx01orj0P00xB_G77IoPa9NfzMCdp4DyfuwmYcAmpCK-ujTXsP8ivT192EbIIIr6DT3spr9tJUpz1YL3RAQ4uwjSWWUk6UkXJRY38XbZ4XsAFDTWvKTHvsxut3u-D9cvGczqJGRm3N8Tg_ErRqXtrD9wJ4t5I071yeJ2F3hOd-RWZgQO-QNXRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد شناسایی همکنون در آسمان اصفهان
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/12761" target="_blank">📅 02:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwN5XeWz8r6163r-efyu60d2v8lJweiQmLMkH3D_txD8Mo3zDcAA-44lF0atyB_TUBomlJXu2sQP-sCGwszZqDnenz2WInXoAjoZx9Sb8nlnWSq4_YUfxfUeCPfiMCwNLmWhYyXb8cGu44I_tDDInonWReUREyLcxZlGtdGMpyE6C15ZR5Fi5pcnWnFYR2cmT0wTSRodE8LBebIf9o9KV4dlnbagYi4fYPMjUExYnig31OpWe5T8H94bE4R6MjxSxFnYn4BW_Us82mc9tr49LzzM84YGXJFBdK7SqhvOR1c70lLGin35kpmTVKzRs6cNf4LIp42UfasgLiUicao13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«رویترز» به نقل از یک مقام آمریکایی گزارش داد:
ارتش آمریکا حملات هوایی جدیدی را علیه یک سایت نظامی ایران انجام داد که تهدیدی برای نیروها و ناوبری ما در تنگه هرمز محسوب می‌ شد
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/12760" target="_blank">📅 02:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارشات تأیید نشده از ترور سردار علی عظمایی، جانشین سردار علیرضا تنگسیری، فرمانده نیروی دریایی سپاه.
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/12759" target="_blank">📅 02:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12758">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/12758" target="_blank">📅 02:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12757">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/12757" target="_blank">📅 02:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12756">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/12756" target="_blank">📅 02:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12755">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یا موسی</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/12755" target="_blank">📅 02:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12754">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پدافند اصفهان فعال شد !
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/12754" target="_blank">📅 02:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12753">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فارس : شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد.
هنوز محل دقیق و منشأ این صداها مشخص نیست و پیگیری‌ها برای مشخص شدن آن ادامه دارد.
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد.
طی ۴ روز اخیر نیروهای مسلح کشورمان یک پهپاد آر کیو ۹ و یک پهپاد اوربیتر‌ دشمن آمریکایی صهیونی را در منطقه هرمزگان منهدم و همچنین سامانه‌های پدافندی نیز یک اف ۳۵ و یک پهپاد آر کیو ۴ را نیز رهگیری کردند.
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/12753" target="_blank">📅 02:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12752">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبر گزاری فارس‌ انفجار رو تایید کرد !!!
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/12752" target="_blank">📅 02:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12751">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تایید نشده ۳ نفر‌گفتن ماشین این کاربر‌ با آدرس گفته :
بولوار‌خلیج فارس یه ماشین رو با پهپاد زدنن رفت رو هوا و بعد پدافند با تاخییر شروع کرد فعالیت
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/12751" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12750">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">داداش من بندرم ۳ تا انفجار ۳۰ مین پیش بود و تا ۱۰ مین پیشم صدای پدافند می اومد میگن گویا یه ماشینو زدن و ترور بوده
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/12750" target="_blank">📅 02:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12749">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/12749" target="_blank">📅 01:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چیزی ‌نیست بی بی اومده یه قلیه ماهی ‌بزنه بره
🐟
شلوغش نکنید</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/12748" target="_blank">📅 01:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سلام همین الان پدافند بندر عباس درگیر شد
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/12747" target="_blank">📅 01:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارشها شما اکثرن به پایگاه هوایی/فرودگاه اشاره میکنه</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/12746" target="_blank">📅 01:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صدای سه انفجار در بندرعباس دوباره
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/12745" target="_blank">📅 01:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12744">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارشهای ززززیاد از انفجار در بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/12744" target="_blank">📅 01:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12743">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کره شمالی تشکیل ائتلاف چهارگانه شامل آمریکا، استرالیا، هند و ژاپن را محکوم کرد. پیونگ یانگ همچنین تاکید کرد که هرگز از برنامه هسته‌ای خود چشم‌پوشی نخواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/12743" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12742">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e19195ad.mp4?token=DouNo95Cg_wJESW8TAq4sUrYQKyiMqQVYpr0_FMGp-oDkN4TqenfEBVEM9rvJRC7kLQO8G43Y44aE6OmJUTXxjgA8u7zYWkSW_kyu9EJaCQ2CW2rJ6QSZXIODbO7H0vR8Am-Ro3sVx6mrtgNKWC2bHkdFUudyhSd3yerN-cO_my2nDIhLMMYEzsPLPoP1IRv8CQkShWEoYXR1oJZp-vy3U-_aCxG0Iwe0zAW_Zqn01mfEDI7g8_WbFAXyRlq8eyM0uqUyC3pCAgSGgAG79nkT80EpB1RJ4xX0Ai-gmqFyFoMgKtBSawR5QPMaSxj9vYYatRY89RUBwk5C_qSyCzp1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e19195ad.mp4?token=DouNo95Cg_wJESW8TAq4sUrYQKyiMqQVYpr0_FMGp-oDkN4TqenfEBVEM9rvJRC7kLQO8G43Y44aE6OmJUTXxjgA8u7zYWkSW_kyu9EJaCQ2CW2rJ6QSZXIODbO7H0vR8Am-Ro3sVx6mrtgNKWC2bHkdFUudyhSd3yerN-cO_my2nDIhLMMYEzsPLPoP1IRv8CQkShWEoYXR1oJZp-vy3U-_aCxG0Iwe0zAW_Zqn01mfEDI7g8_WbFAXyRlq8eyM0uqUyC3pCAgSGgAG79nkT80EpB1RJ4xX0Ai-gmqFyFoMgKtBSawR5QPMaSxj9vYYatRY89RUBwk5C_qSyCzp1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
حتما با پوشک بسته نگاه کنید
⚠️
میگن سیلوستر استالونه بعد از دیدن این ویدیو فروش آنلاین تمام فیلمهای رامبو رو متوقف کرد.
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/12742" target="_blank">📅 00:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12741">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">علیرضا فیروزجا با پرچم فرانسه نفر اول شطرنج جهانو شکست داد
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/12741" target="_blank">📅 00:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12740">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/12740" target="_blank">📅 00:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12739">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عضو تیم رسانه‌ای هیئت مذاکراتی ایران: سفر قالیباف به قطر درباره آزادسازی ۱۲ میلیارد دلار از اموال بلوکه‌شده، موفقیت‌آمیز بود!
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/12739" target="_blank">📅 23:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12738">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یاشار جان  احساس میکنم این جام جهانی امسال خیلی اتفاقات عجیب و غریبی میوفته ، دنیا باز هم خواهد دید که ما تا تهش پای ایران وایسادیم
☀️
🦁
خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/12738" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12737">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromE R F A N</strong></div>
<div class="tg-text">یاشار جان
احساس میکنم این جام جهانی امسال خیلی اتفاقات عجیب و غریبی میوفته ، دنیا باز هم خواهد دید که ما تا تهش پای ایران وایسادیم
☀️
🦁
خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/12737" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12736">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دایی جان، ایران همش دنبال پوله بخاطر این نیست که پول ندارن به ادماشون بدن؟ نمیشه جاهایی که ربط به دولت داره رو اعتصاب کنیم! و هر دفعه میگن قراره پولمون رو بدن تا انگار ساکتشون کنه.!!</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/12736" target="_blank">📅 23:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12735">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKnow</strong></div>
<div class="tg-text">دایی جان، ایران همش دنبال پوله بخاطر این نیست که پول ندارن به ادماشون بدن؟ نمیشه جاهایی که ربط به دولت داره رو اعتصاب کنیم!
و هر دفعه میگن قراره پولمون رو بدن تا انگار ساکتشون کنه.!!</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/12735" target="_blank">📅 23:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12734">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شاهزاده رضا پهلوی جمعه پیش در نشستی با شماری از فعالان رسانه ای  که ویدیو آن الان پخش شده گفت :  تیشرت های سیاه یا ساواک به خصوص و هر چیزی غیر از تم اصلی شیر و خورشید نپوشید این جریان در کمترین حالت ایجاد جنجال میکند و انحرافی است  من واقعاً درک نمی‌کنم این موضوع از کجا آب میخورد و این مسئله نگران‌کننده است.
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/12734" target="_blank">📅 23:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12733">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/12733" target="_blank">📅 23:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12732">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/12732" target="_blank">📅 23:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12731">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2ksulAz5C5DgXKE4YxLdhK5BaA0LtmqA_aA4b5L6dtAK9yQNks11zZvYFU9baBzSuPbSZr4kWMxsT6UC87VyglrYa5H5l2USl45bYelhhd0SbtflxseqYXdg2HAo72GWJDEq0eiyO0hgtDmAIWyKy65Tn6L5aH9QfZgLBaM-8qTpa2mROiQYEtMNs8B0vkjLCyAsJOoH2dFfLxy8kLPAQHvKMFmUZ5q1ej3Var_S4sBDTyIqgE1Hip8yP3cPUl2HYfcLFZccWz6cM-iQgNnSja181kwYl-diNf8cwh0eg_eBy56ukga3mX2MAzYRmO2OmbPArxEcg18b7jcRB4Ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : داداش این ایده ایی که دادی رو یه مقدارخلاقیت دادم بهش که بفهمن دقیقا چطورمیشه رفت بدون پرچم
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/12731" target="_blank">📅 23:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12730">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/12730" target="_blank">📅 23:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هم اکنون گزارش ها از دو ترور بزرگ در شمال غزه.
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/12729" target="_blank">📅 23:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اتاق جنگ با یاشار : کاری‌ نداره اگه همه با هم متحد باشن میتونن ، فقط با پوشیدن لباس های سبز سفید ، قرمز و زرد یه ابر پرچم قول آسای انسانی‌ پیکسلی درست کنند
🧠
😍
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/12728" target="_blank">📅 22:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12727">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/12727" target="_blank">📅 22:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/12726" target="_blank">📅 22:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12725">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58450dfb0.mp4?token=mJElCDyEkU953tqp7U1jMzw5YEum-q37qDSxDbtfu-q0DVLTgpIes41Csf8TIJSbx04NSotShiPejoWA1gUdriye5NJ14c6P7YAWhzQLfUn8dktPTxKbPBoC6hByfm0_vyCGZM2XbwZtMhc_nKWvBUMB8F9oWEtzDC-d3YS5E1EGw9sKOx_Ik4G93gptAhSFY7NidLIcrNhxuPSc65duBwx79MAVC1TXML68jtlQCBEUM8STkXuuvss3CywCQJ4Co610P2Ccx_Dc2tacpLU_GEsC67pRkwMjwojhN17MzO7z02JjgaJu_jRiDoV8tgUcfb_oVmpKs7zoiKIkaZosaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58450dfb0.mp4?token=mJElCDyEkU953tqp7U1jMzw5YEum-q37qDSxDbtfu-q0DVLTgpIes41Csf8TIJSbx04NSotShiPejoWA1gUdriye5NJ14c6P7YAWhzQLfUn8dktPTxKbPBoC6hByfm0_vyCGZM2XbwZtMhc_nKWvBUMB8F9oWEtzDC-d3YS5E1EGw9sKOx_Ik4G93gptAhSFY7NidLIcrNhxuPSc65duBwx79MAVC1TXML68jtlQCBEUM8STkXuuvss3CywCQJ4Co610P2Ccx_Dc2tacpLU_GEsC67pRkwMjwojhN17MzO7z02JjgaJu_jRiDoV8tgUcfb_oVmpKs7zoiKIkaZosaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما شرط جدید ایران برای توافق با آمریکا را اعلام کرد: پرداخت غرامت ۳۰۰ میلیارد دلاری از آمریکا به ایران
!
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/12725" target="_blank">📅 22:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12724">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">در اسرائیل پرونده‌ای جنجالی به نام «پرونده بیلد» فاش شده است. طبق این گزارش‌ها، یک سند محرمانه منتسب به حماس عمداً به رسانه‌ها درز داده شد تا خشم افکار عمومی از دولت بنیامین ناتانیاهو کمتر شود.
گفته می‌شود «آری روزنفلد» و پدرزنش یک مسیر غیرقانونی برای انتقال اسناد محرمانه از سازمان اطلاعات نظامی اسرائیل به دفتر نتانیاهو ایجاد کرده بودند. سپس تلاش کردند پیام‌ها و روایت‌های سیاسی خاصی را وارد سخنرانی‌های نخست‌وزیر ناتانیاهو کنند تا بر افکار عمومی از او تأثیر مثبت بگذارند.
این پرونده «بیلد» نام گرفته چون بخشی از اسناد ابتدا به روزنامه آلمانی
Bild
رسیده بود. مخالفان دولت می‌گویند از اطلاعات امنیتی برای اهداف سیاسی استفاده شده، اما حامیان نتانیاهو این اتهامات را اغراق‌آمیز و سیاسی می‌دانند.
@withyashar
اسرائیلی ها هم دنیایی دارن خوب‌ مردی بی بی برا خودتون اسن کارو کرده ! ولی مخالفاش داستان کردن !</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/12724" target="_blank">📅 21:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12723">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جلسه کمپ دیوید که قرار بود امروز برگزار شود ترامپ اعلام کرد: جلسه کابینه به دلیل شرایط آب و هوایی در کاخ سفید برگزار خواهد شد، نه در کمپ دیوید! حالا صحبت‌هایی هست که کمپ دیوید یک تله برای شناسایی فردی بود که اطلاعات را نشت می‌داد ! فرد مورد نظر گیر افتاد !…</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/12723" target="_blank">📅 21:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سلام یاشار جان خسته نباشی، ممنونم بابت زحمات
میگم یه سوال تو خبر دارین که میگن جلسه کابینه کمپ دیوید یه تله بوده که کی اطلاعات رو لو می‌داده و فهمیدن که جی دی ونس بوده؟!</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/12722" target="_blank">📅 21:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ارتش اتاق جنگ اعلام حضور کنید. مانور امشب شروع شد. این کامنت زیر پست بی بی را لایک کنید، ریپلای کنید و اگر میتوانید اد تو استوری هم بکنید و به دوستان خود هم بگویید این کار را انجام دهند. آماده میشیم برای مانور نهایی در دوشنبه. توجه کنید فقط همین کامنت را لایک کنید، حتی پست را هم لایک نکنید که کاملا دیده بشه
❤️‍🩹
🙌🏾
https://www.instagram.com/p/DY2dIhsM-VK/?igsh=MXFhaGU4NzliZzVmaw==
ترجمه:
تبریک می‌گویم بی بی جون، فرزند راستین کوروش کبیر.
دیگر زمان آن رسیده که مقدمات حمله به ایران آغاز شود.
مردم ایران در نهایت ناامیدی فرو رفته‌اند.
لطفاً این لحظهٔ تاریخ‌ساز را هرچه زودتر رقم بزنید.
هر روز در ایران، روح جوانان ما را از جسمشان جدا می‌کنند.
تمام چشم امید ما به شما دوخته شده</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/12721" target="_blank">📅 21:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اسرائیل هیوم: ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/12720" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12719">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/12719" target="_blank">📅 21:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12718">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSG</strong></div>
<div class="tg-text">ماجرا ری اکشن پر قرمز چیه دیگه ؟؟همه دارن میزنن
😂</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/12718" target="_blank">📅 21:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12717">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1s8mjW1WX-4Dc8OrLnxRJNAloAo3Plk88AN6raRLSKDk30rWliCl8hTTr3bUwo-rJGgS-m20MyiJ7TPu9tish135FPP4a0-ecf-j23IWfz7APGN4tOwzqz7U2VU3rO6rDsYK2PfHJvrgBHghncb33XFnYVag1jkwoyVg3RBVqfmfQ1_yI7HW7mME1FN0eocPpTudztHQPRm5zr5ITjXan8MqQseWjumqCf3pUslYsJbRIv0LOd9rvGXrwMmDySxsZq7Ux70be8pKA3xN5ttJDMjT_17x6mrkV-_Eei7oxWrdF5z079pnpBx22BemjBZNNWkQz_RmP6KNgLBUTX-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی رد لغو تحریم‌های ایران از سوی دونالد ترامپ، بازار سهام ایالات متحده در عرض تنها ۲۰ دقیقه، ۲۳۰ میلیارد دلار از ارزش خود را از دست داد.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/12717" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12716">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ: اوباما کشور اشتباهی را انتخاب کرد. او باید کشور دیگری را انتخاب می‌کرد. به شما نمی‌گویم که آن چه بود. او وقتی ایران را انتخاب کرد، کشور اشتباهی را انتخاب کرد.
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/12716" target="_blank">📅 21:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اتاق جنگ با یاشار : هیچوقت انقدر مشتاق نبودم حجاج هر چه سریعتر سلامت برگردن خونه هاشون
😅</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/12715" target="_blank">📅 20:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12714">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">داداش دقیقاً داره حرف تو پیش میره موج مکزیکی
😂</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/12714" target="_blank">📅 20:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12713">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnima</strong></div>
<div class="tg-text">داداش دقیقاً داره حرف تو پیش میره موج مکزیکی
😂</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/12713" target="_blank">📅 20:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12712">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ: دارن کم‌کم شروع می‌کنن چیزهایی رو که باید بهمون بدن، تحویل بدن. اگه این کار رو بکنن، خیلی خوبه.
اگه نکنن، هگست کارشون رو تموم می‌کنه.
ما درباره هیچ‌گونه کاهش تحریم‌ها یا دادن پول صحبت نمی‌کنیم.
وقتی اونا درست رفتار کنن و کار درستو بکنن بهشون جازه می‌دیم به پولشون برسن
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/12712" target="_blank">📅 20:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12711">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خبرنگار: آیا با این موضوع راحت خواهید بود که روسیه یا چین اورانیوم غنی‌شده ایران را بگیرند؟
ترامپ: نه(زیر دلم درد میگیره)
@withyashar
🤣</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/12711" target="_blank">📅 20:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12710">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ :
ما کنترل پولی را که آنها ادعا می‌کنند مال خودشان است، در دست داریم. ما کنترل آن پول را حفظ خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/12710" target="_blank">📅 20:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">داداشی امشب ردبول و میزنی یا نه؟</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/12709" target="_blank">📅 20:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12708">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhesam | امیرحسام</strong></div>
<div class="tg-text">داداشی امشب ردبول و میزنی یا نه؟</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/12708" target="_blank">📅 20:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12707">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پیت هگست درباره ایران:
آنها ممکن است موشک داشته باشند، اما در حال حاضر نمی‌توانند موشک‌های بیشتری بسازند. نمی‌توانند پهپادهای بیشتری بسازند. نمی‌توانند کشتی‌های بیشتری بسازند.
آنها آمدند و التماس کردند تا صحبت کنند.
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/12707" target="_blank">📅 20:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12706">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfT-Bs8WepRBa5hn7HmM8EPJvcDhdzcLTB8-sZKfESXxaCAIXUI8zWvlnoxKR7gX2nrLrEADsyWBm2ExCLHMoV11NvRwF1UPXxkiltLtG8DN2by-1s46FbYRV88MqUhGK40kbh18KB6zrQuGmbcUUmVYWA5VCagaQEso1DC2FfAtEcGIBspy-OI4R92lFEBYpnueFgZ9_dgY4k4a3SLQq-47Lv9jqJmcoHib06pw7gf8gQG29wbK5rSXmXO-PRa0cK1pjc5nKE6u31BG5URzNyOzyZkMD1wDlFO8WUjTPA8ijkKaggWjeztN74MzOn7Akcjt4D31qHGs56FxmIa9uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️رئیس روس اتم می‌گوید روسیه تصمیم  گرفته است بازگشت کارکنان خود به نیروگاه هسته‌ای بوشهر در ایران را به تعویق بیندازد!
@withyashar</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/12706" target="_blank">📅 20:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12705">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مارکو روبیو :اگر ایران توافق قابل قبولی مارو امضا نکند جنگ را شروع خواهیم کرد این‌خواسته ترامپ است
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/12705" target="_blank">📅 20:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12704">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و من به خاطر جهان جلوی آن را می‌گیرم.
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/12704" target="_blank">📅 20:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12703">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، درباره مذاکرات ایران:
آقای رئیس‌جمهور، اگر این کار جواب نداد، گزینه‌های دیگری در اختیار دارید.
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/12703" target="_blank">📅 20:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12702">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">روبیو : ما با جمهوری اسلامی پیشرفت‌هایی داشتیم اما در روزهای آینده میزان اون رو خواهیم دید.
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/12702" target="_blank">📅 20:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12701">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پست جدید یه یا موسی کامنت کنین بی بی و پسرش و زنش رو تگ کنین امشب بزنه
🤣
💥
💥
🌶️
🌶️
https://www.instagram.com/reel/DY2Hk4hoW2r/?igsh=MXYyMDlxdjY5b3QwZg==</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/12701" target="_blank">📅 19:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12700">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06481c5d63.mp4?token=dk6iYo8Qsi1x0_q2Cf66Ad2EkhpT5D2hooiKS9i6OKzpWEj6tvJpZSz3rhyAi7o78OoVPwvdgw9_PpoAf6qzO77MjUOmGACotwepDPInS8ZIJkjgchlhJH8edp5uVtdUGU3ZQQVsyNLrTdY6qyalLKKmzsuvRDM2Cmy2l7eKK6quGtkr0ce8_hGDawVEqj7VpUw8nQfkcpQoMERAY9hLRhFo1jzFWOdVtxwrSyvOR6fT-MMbAJoRUYvsspNspuQ4PuQyo30P6-RbA_loMiygw-gantwEnQ9mKZkWfUUG75XOsR5_X1mAN_eI5uBkoyrE_b0JhOwWEFs_cG-3v-pt_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06481c5d63.mp4?token=dk6iYo8Qsi1x0_q2Cf66Ad2EkhpT5D2hooiKS9i6OKzpWEj6tvJpZSz3rhyAi7o78OoVPwvdgw9_PpoAf6qzO77MjUOmGACotwepDPInS8ZIJkjgchlhJH8edp5uVtdUGU3ZQQVsyNLrTdY6qyalLKKmzsuvRDM2Cmy2l7eKK6quGtkr0ce8_hGDawVEqj7VpUw8nQfkcpQoMERAY9hLRhFo1jzFWOdVtxwrSyvOR6fT-MMbAJoRUYvsspNspuQ4PuQyo30P6-RbA_loMiygw-gantwEnQ9mKZkWfUUG75XOsR5_X1mAN_eI5uBkoyrE_b0JhOwWEFs_cG-3v-pt_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران :
ایران خیلی دنبال توافقه. هنوز به نتیجه نرسیدیم و راضی نیستیم، ولی یا توافق میشه یا مجبور میشیم کار رو تموم کنیم.
اونا دارن از روی استیصال مذاکره می‌کنن.
اونا دیگه نیروی دریایی و هوایی ندارن و رهبرانشونم هم رفتن.
ایران فکر می‌کرد میتونه صبر کنه تا منو خسته کنه
به انتخابات میان دوره اهمیتی نمیدهم اونا گزینه دیگه ایی جز توافق ندارن
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/12700" target="_blank">📅 19:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12699">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اینترنشنال باز خل شده ؟ چرا ترامپ رو انقدر میکوبه ؟!</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/12699" target="_blank">📅 19:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12698">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ: ایرانی‌ها فکر می‌کنند من به‌خاطر انتخابات میان‌دوره‌ای جنگ را تمام می‌کنم اما من اهمیتی نمی‌دهم @withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/12698" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12697">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-Roh1luHizqRmkwq2q3UbOPVEgURF07p37MDR8OEZO8VZTTqBzb9sJMt1CQfxHS8mMYASFbFs53Xu3k5uRlYpKmVlbJRC50u8LON6jiav_IG-ftZRqUr-loCqOgSKOeEO20Ij5Gvvd-0Fia0W0iUrn0lNYT6AQ5op-zE0UMWW3cvkmaJoWy3COTp_7n7Thz0bNfVs2iE-HQuZhzUKT-3gad8sHYj_mS1p-Z44tLTcmEMTbOU22vozVCT6800UM5JKVPg9HQ38J2ADs3fzinC0z-UjdkGwUNgL6jG6n-eT6fklWqn0hz0ApPA0EvV3WSUHZOLBbjLFarej4TsCH9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایرانی‌ها فکر می‌کنند من به‌خاطر انتخابات میان‌دوره‌ای جنگ را تمام می‌کنم اما من اهمیتی نمی‌دهم
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/12697" target="_blank">📅 19:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12696">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q71IlAWWn07iSBQjVcjdBTRidHSV1nQ4OM2NA63fjsc_0WNRLRseRTyBZSI55zbkjq6X-ylTpbjcBHh8DlxN_BZTIq9Bx5ImtB6XvVVcxhfWN0cQudn1xSGZImOWGVeRdG0-htsgXsSnHFyUVD4EiNHvqgpY7qFZN9IC4ALRtw4wwqSNL12u88P2N5wYeeHL9GmKPiDwoVVDTz912e6ijO3OdPZbraJn6dDsK_IZ0RqxM1dq8Xbp1P7kJPGMYU8l8DtRU40zcw_PT_AYx9vfITmLesrzmdd_9k-PifIl8T9Itn961VCiOm_elZrMBD9YfP3fy4jhf8h9sqVJfD7ctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها می‌باشد.
میزان اختلالات در شبکه از دیروز بسیار بیشتر شده است، بسیاری از سرویس‌های گوگل و کلودفلر بسته شده اند و حتی قابلیت استفاده از گوگل پلی و اپ استور نیز وجود ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/12696" target="_blank">📅 19:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12695">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA</strong></div>
<div class="tg-text">یاشار جان من دندونپزشکم، دو سال سرباز بودم، صبح‌ها تو کلینیک ارتش یه شهرستان دورافتاده کار می‌کردم، بعدظهر هم تا شب تو کلینیک خیریه کار می‌کردم، از نظر مالی هیچ سودی برام نداشت فقط دلم می‌خواست دوران سربازی یه کار مفیدی هم برا اقشار ضعیف انجام بدم واقعاً از دلو جون مایه میذاشتم
اما اون دو سال، از آدمای قدرنشناس  و پر توقع رفتارای زیادی دیدم که باعث شد بفهمم خیلی از هم‌وطنا وقتی برا خدمتت هزینه‌ای پرداخت نمی‌کنن قدر خودت و کارتو نمی‌دونن انگار وظیفت بوده بشون خدمت کنی
همین تجربه‌ باعث شد دیگه سمت خیریه نرم
خیلی از مردم ما واقعا قدرنشناسن
وقت و انرژیتو بدون سود و فقط از روی عشق به کشورت صرف کاری می‌کنی بعد یه عده‌ پیدا میشن که  برن رو مخت و پشیمونت کنن</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/12695" target="_blank">📅 19:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB40eFNTVf-ufV3AUcZYz7CL_RRooEJAEn-pCwHL-ew3CDrsaMJ4c5EmEp7k0cowueagiaf_mvUSR6KgUYI1mdtRfjuK-xElR2GIIalijkES6GgdzDymqxp6Y98Q2WIn0441kCJWHUnbRDvTxVIIfqbMagZ30l3ekYE2rbFnCSk3WZjxVtJvjrE6b24laQq1gVzZmRowG8ZHpI-rkjirA4ybBhTlsgcdTfJhvrDzN-BLwepGGS4J2nayYC_wSCi5zCqGDcaR0kxk4qCW9qEXIIbqYEVmkNxnngKokAsKksXptodiq3QRLJRkZmJb7OD0oFHIesD8kPiBYV5Q5fM8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به PBS گفت که ایران در ازای کنار گذاشتن اورانیوم بسیار غنی‌ شده خود، از تحریم‌ها معاف نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/12694" target="_blank">📅 19:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12693">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlXs3XZW84RWdxe5SN1NBmIzWthl-9T2OlDeBOnD6nslak-6nQxhDGUfSLhDcnVKwnfUhHC_WE_nNNGZhYk8hAQ1w_boloVdgNzIp0zj1fmD78Cdo200iqpf4TM9l1mEWyyz1jGGgexyr4mPrHkYFr4QNL-CGuYKIq7uuHmBslquZFi_6MllkAyOK1QBp_3Mdyy82bD5SX6J4mCe9WFwe6yDwN6oSTuUhuQdxF8SpS4CXkVJ3kUZcIJkAhQ_Rx-P3OaYhCDkMXnwDNuuAloxnuDBuLgXT7QzQLjrb_1CjjWq0XAwHctOqoRiVmPVjwDjyBzhbDJ0uIvXnrwuEqFAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار برج چیتگر پامچال چهار از طبقه ۸ به بالا آتیش گرفته
این دقیقاً روبروی همون برجیه که تو جنگ دوازده روزه طبقه ۱۵ رو زدن بعد گفتن نشت گاز
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/12693" target="_blank">📅 19:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12692">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خبرگزاری فارس: به عقیده ما احتمال دارد ترامپ در ساعات آینده به صورت یک‌طرفه اعلام کند که توافق ایران و آمریکا نهایی شده است
@withyashar
یاشار : عقایدتون رو …
🤣</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/12692" target="_blank">📅 19:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12691">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzqXjBDSTZ13RDLbhgilXULI7EEbj4ey_oBdYNuvL_1ASaosXcG0X-Nu_i8_ht7DoLFVga4ursM8n0IMz42n_EQAPFMy9nlSJeaHvSbTUXkYoGPUPN71VlLqFdQtU704G09HAbP0nuSqP0YhV37jzDoqs58_CcSzHvUbIs84qXjueKVikCzIB3BTXqtIb3uU31UFatt5sJE1-Lc2K-mLphAtydCFwN7OZE1I4XClyMtrviFgL8lV4sUDJCm3hk8P810-JtlN-245DdZIm5J9TYgm-KZERYfDgSRX0WRsJU12urFEnLIcoX3m2_fjrcBIVaSCVAFz4HoDuxMP1W97Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم.
عوامل موساد باعث بازگشایی اینترنت شدن.
@withyashar
یاشار : شاید باورتون نشه ولی درست میگه اینبار
🤣</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/12691" target="_blank">📅 18:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZAoGhm25jcsyXAaEmHCtbtvWMrgMm9oiqYp_io-7PCHkPXhdgjPW4zm3QqafbtzLBFYrgaYeTqR_o-LGMKyhIJSlO7TqKGT3iOn5lJeNQMuR2qs55I3aOcFmKQmwqEFv4ksYlWR2GBOuzTO0CjlD1ZHjLBL2ijnowUu6aodnDfu7h0FJZoS_NPWNvmWlKY21AxrVv39Its5otEXaLaQxVhtUmVRRJFenA_zIsciEuny3o9i1PuvcZpXeO0iE8AglcgbnAjVUnXTBNKK5esUB-gwwj8Ns_tolUEMNeK9TdT4ZzuDsWRPwaZHGU2LYFoDP_O9U3m9Dut9pubUwbSzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای از پایگاه هوایی رامشتاین در آلمان، ده‌ها فروند هواپیمای ترابری C-17A و C-5M نیروی هوایی ایالات متحده، چندین فروند هواپیمای ترابری C-130 و حداقل 10 فروند تانکر KC-135R را نشان می‌دهد که در آنجا مستقر شده‌اند.
در اتاق جنگ گفتم که رامشتاین مهم‌ترین پایگاه ایالات متحده در اروپا برای جنگ ایران است و به عنوان یک قطب لجستیکی کلیدی عمل می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/12690" target="_blank">📅 18:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12689">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پست جدید یه یا موسی کامنت کنین بی بی و پسرش و زنش رو تگ کنین امشب بزنه
🤣
💥
💥
🌶️
🌶️
https://www.instagram.com/reel/DY2Hk4hoW2r/?igsh=MXYyMDlxdjY5b3QwZg==</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/12689" target="_blank">📅 18:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12688">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کاخ سفید گزارش‌های مربوط به تفاهم‌نامه ایران را کاملاً ساختگی خواند.
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/12688" target="_blank">📅 18:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12687">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پست جدید
یه یا موسی کامنت کنین بی بی و پسرش و زنش رو تگ کنین امشب بزنه
🤣
💥
💥
🌶️
🌶️
https://www.instagram.com/reel/DY2Hk4hoW2r/?igsh=MXYyMDlxdjY5b3QwZg==</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/12687" target="_blank">📅 18:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12686">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ارتش اسرائیل در اقدامی فوری دستور تخلیه کامل شهر بندری صور، بزرگ ترین شهر جنوب لبنان به همراه تمام روستاهای اطراففش رو صادر کرد
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/12686" target="_blank">📅 17:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12685">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">زلنسکی در پیامی به ترامپ:
اوکراین برای رهگیری موشک‌های بالستیک روسیه تقریباً به طور انحصاری به ایالات متحده متکی است.
سرعت فعلی تحویل موشک‌ها به اوکراین دیگر با تحولات هماهنگ نیست.
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/12685" target="_blank">📅 17:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12684">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر دفاع ترکیه
یاشار گولر
:
ترکیه حقوقش در دریای اژه، مدیترانه شرقی و قبرس بر اساس قانون و تاریخ است و با هر اقدامی که بخواهد وضعیت موجود را به نفع برخی کشورها تغییر دهد یا جزایر غیرنظامی را نظامی کند مخالف است.
همچنین هشدار می‌دهد که نسبت به تهدید علیه منافع و امنیتش در دریاها بی‌تفاوت نخواهد بود و ارتش ترکیه توان مقابله با هر تهدیدی را دارد.
در مورد قبرس هم تأکید می‌کند که از ترک‌های قبرس حمایت می‌کند و به‌عنوان کشور ضامن از حقوق و امنیت آن‌ها دفاع خواهد کرد.
@withyashar
ترکیه با یونان و قبرس بر سر , مرزهای دریایی , منابع گاز طبیعی در مدیترانه شرقی و حق حفاری در آب‌های مورد مناقشه اختلاف جدی دارد.</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/12684" target="_blank">📅 17:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12683">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به گزارش فارس نیوز، آواربرداری، تعمیرات و بازسازی تمام واحدهای پتروشیمی آسیب‌دیده تنها در ۵۰ روز به پایان رسیده است و اکنون تمام تأسیسات قادر به تولید با ظرفیت قبل از جنگ هستند.
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/12683" target="_blank">📅 17:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12682">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مهر:
یک ساختمان اداری در فرودگاه امام خمینی آتش گرفت
دقایقی قبل یک ساختمان اداری در شهر فرودگاهی دچار حریق شده است.
این حریق در یک ساختمان اداری گمرک شهر فرودگاهی به وقوع پیوسته است.
تاکنون از علت دقیق حادثه و میزان خسارت و تلفات احتمالی اطلاعاتی در دست نیست.
@withyashar</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/12682" target="_blank">📅 17:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12681">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ امروز ساعت ۱۱ به وقت محلی (حوالی ساعت ۱۹ به وقت تهران) برای بررسی مذاکرات با ایران، جلسه‌ای با اعضای کابینه و دستیاران ارشد خود خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/12681" target="_blank">📅 17:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12680">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحسین</strong></div>
<div class="tg-text">واقعا این ملت باید به دیکتاتور وطن پرست بالا سرشون باشه . ملتی که جمهوری اسلامی پرورش داده جز دزدی بی فکری پاچه خوار تو اوج بیسوادی ولی ادعای دانشمند بودن میکنن آدم فروشی ...... اینا با دموکراسی درست نمیشن فقط باید یه دیکتاتور بالا سرشون باشه مثل رضا خان بزرگ . این جماعت تو هر لحظه رنگ عوض میکنن در این حد احمق حالا یه عده میگن توهین میکنی با کلمه احمق ولی توهین نیس واقعیته یه واقعیت تلخ . حکومت هر کشوری طبق لیاقت مردمش اداره و اجرا میشه واقعا متاسفم پاسوز یه عده جوگیر احمق شدیم</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/12680" target="_blank">📅 16:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12679">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">درووود بهت یاشار عزیز،همین که توی حاشیه اصلا حرکت نمیکنی یعنی کارت درسته.فقط(( هدف ))مهمه تمام.</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/12679" target="_blank">📅 16:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12678">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMilad Farahmand 🐾</strong></div>
<div class="tg-text">درووود بهت یاشار عزیز،همین که توی حاشیه اصلا حرکت نمیکنی یعنی کارت درسته.فقط(( هدف ))مهمه تمام.</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/12678" target="_blank">📅 16:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12677">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">لیندسی گراهام:«مدت‌هاست برایم روشن شده که پاکستان به‌عنوان یک میانجی، فراتر از حدِ مشکل‌ساز است. دشمنی آن‌ها با اسرائیل، ریشه‌دار و دیرینه است.
این حقیقت را نمی‌توان انکار کرد که هواپیماهای نظامی ایران در پایگاه‌های هوایی پاکستان نگهداری می‌شوند؛ و همچنین مواضع و سخنان گذشتهٔ بلندپایه‌ترین مقام‌های پاکستانی علیه اسرائیل نیز نگران‌کننده است.»
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/12677" target="_blank">📅 16:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12676">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/12676" target="_blank">📅 15:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12675">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6GF7tSkChkBsur9nZHj_5Pza5TXwwipIchOkq2gZYfoZsbeBXjSdg78BLyZuy40vcKJQNolcldrFNFinzaRkJutf1ya3B6tqlvD7HcBoD4xGcu2vJgM7QLgxbRMSNL6oxanVsFX3UDJJkuX_SK_xbh6VjeR6GqfMafE2GGsDJPYl1n4o8yg9ddm7qfJx4hsxKcR-K5mTZRAqYbxM7oVaAsn_UONx5TqUJdBla7QVYhudXAEaXMDohpGsqsfuKMsH7OytQBrbE5EJ3JL9rH7f6QpuDMQl5RqjMXCRbU9bDy8bd-bD5T5lSH-qMRZAwSC_RlrmtMiLvMGiAyENjb27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث از جروزالم پست :
آزار و اذیت جنسی در زندان‌های ایران در دوران آتش‌بس به‌شدت افزایش یافته است
جروزالم پست
آزار و اذیت جنسی در زندان‌های ایران در دوره آتش‌بس به‌طور چشمگیری افزایش پیدا کرده است.
یکی از معترضان به مدیا لاین گفته که هنگام بازجویی با باتوم به او تجاوز شده است.
مرد دیگری پس از آن‌که مأموران ادعا کردند به پیکر همسرش بی‌حرمتی کرده‌اند، اقدام به خودکشی کرده است.
گروه‌های حقوق بشری می‌گویند از زمان شروع جنگ، دست‌کم ۳۶۴۶ ایرانی بازداشت شده‌اند و قطع اینترنت باعث شده ابعاد واقعی ماجرا پنهان بماند.
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/12675" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12674">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyC8zaEL7YtTtIk6y5OF-gPYhUhLbnpFmvggxgyb4COh9ZooAycGIiHvwF5n0GaVrJy_JAP79NDn_sNjemdTgx3LISknG9vqbxO_waLGhHgF2zcxGw9fpyRuAZmHOcYAfx1VVt-TUAXb6Za5r18-o7_BgIZ_4TXmDepzy0W_EOkqZaj4OR6XXdhvWMvxi9EpLKEoxZpy_OjFX-cETDR6AgzfG-RgTlZpWTyeLpc2U_CesoF2eIO-LxvSBA71yW9Xk9UAulsanJVYVGQzt94aCzjYCP4FaBku2f3syo8ZU1xfxELWBEEtDF6ORXgBZViHf-x6rWM3oiDcQs6hH2tJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای سوخت‌رسانی جدید نیروی هوایی اسرائیل، KC-46A Pegasus "Gideon" (301)، اندکی پیش در اسرائیل فرود آمد و ایال زمیر، رئیس ستاد کل ارتش اسرائیل، در مراسم استقبال حضور داشت. این هواپیما اولین فروند از شش فروند سفارش داده شده است و امکان سفارش دو فروند دیگر نیز وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/12674" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
