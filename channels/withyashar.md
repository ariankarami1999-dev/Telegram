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
<img src="https://cdn4.telesco.pe/file/oBfpaES4Axe1wKKIuW-qD39uKRjJoMVBkG0crslmv7S20c83jdKWBETEnIWK2w3JTU4ZXWte0Z0YbV5nDvmT8lEBHhN_xfEZQoYey4fXK4Kis3n4iQSF9LOEzpAIL47xoKfY3Wo1_EUAcCMyV7hbJst0bD7S5XU3LftORxUW707zWrnEGXR7Xt4iRrU5q7gq0S6UcHGGDCNO8iFA4osiU9aOPvs-1cNwYe7o3eZOJTmfpJ9jbeeY7VnUmgLSGum4lrF5kwkx_OgQaqSx58FotRqSebp__Hqkj99zxQqoz-Mom4UPgHFQcJcLe6hv38QDRvXOblbjRnl9Moy7OUI2Tg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 19:28:13</div>
<hr>

<div class="tg-post" id="msg-15797">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانال 12 ، نتانیاهو :
هنوز ماموریت‌هایی برای انجام دادن وجود دارد، هنوز کارهایی علیه ایران و حماس باید انجام شود. ما تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند
@withyashar</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/withyashar/15797" target="_blank">📅 19:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15796">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نهاد دریایی بریتانیا :
خدمه یک کشتی از اصابت آن به وسیله یک پرتابه ناشناس در جنوب شرقی عمان خبر دادند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/withyashar/15796" target="_blank">📅 18:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15795">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ارتش اسرائیل: اگر به دلیل عملیات ما در لبنان مورد حمله ایران قرار بگیریم، با تمام قوا به آن حمله خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/withyashar/15795" target="_blank">📅 18:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15794">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تلگراف: فیفا درخواست جمهوری اسلامی و مصر برای ممنوعیت پرچم‌های رنگین‌کمان در بازی دو تیم را رد کرد
@withyashar</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/withyashar/15794" target="_blank">📅 18:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15793">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کتلین تایسون، بانکدار و تحلیلگر نظام پولی بین‌الملل بریتانیایی :هیچ بانکی برای ایران، صرفاً به‌خاطر مجوز ۶۰ روزه تجارت نفت، حساب دلاری باز نخواهد کرد. تسویه‌حساب محموله‌های نفتی همچنان با ارزهای جایگزین انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/withyashar/15793" target="_blank">📅 17:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15792">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جی دی ونس معاون ترامپ: دستاوردهای مذاکرات سوئیس، توافق در اصل برای ایجاد یک کانال ارتباطی نظامی مستقیم بین ایالات متحده و ایران برای کمک به جلوگیری از تشدید آینده بود.
«یکی از چیزهایی که می‌خواستیم به دست آوریم، یک کانال در سمت ایران برای کاهش درگیری بود.»
«آن‌ها گفتند: "باشه، ما کسی از سپاه پاسداران را می‌فرستیم تا در دوحه با کسی از فرماندهی مرکزی (سنتکام) باشد و این همان راهی است که بسیاری از این اختلافات را حل می‌کنیم."»
@withyashar</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/withyashar/15792" target="_blank">📅 17:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15791">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0b1ba54a.mp4?token=AQ7lQhbJWcJ4ohy_bawBqQ3KIuLwho23nsai9HLn_idNExPu0blyDnxsb_YcE7oRSO9C_we5bXXr0sY1_ka-H6Pd06gyexoYH3ytao9OVHJ2eUGfSvHeDEMX7XKyir4tzGOMQX9cFaZFqknLQE2RgPgEi6GKarCIJ4YsfSqh6etTGN8kQLHBCPhelEfV6AQMEFARjhv9GeVgbNfYJ0DolJpMJkNGRXfpJcfzGBbGlT2VP7YhE4Qr8Ax__pfBYsrOyp6fMefCb3er4bDcmXJRYn5IpQgG7Xg_KQj8S7era04yxPASNDynLXGtLINDE_mOj2d2-PTMwIJSMSupRZ5NsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0b1ba54a.mp4?token=AQ7lQhbJWcJ4ohy_bawBqQ3KIuLwho23nsai9HLn_idNExPu0blyDnxsb_YcE7oRSO9C_we5bXXr0sY1_ka-H6Pd06gyexoYH3ytao9OVHJ2eUGfSvHeDEMX7XKyir4tzGOMQX9cFaZFqknLQE2RgPgEi6GKarCIJ4YsfSqh6etTGN8kQLHBCPhelEfV6AQMEFARjhv9GeVgbNfYJ0DolJpMJkNGRXfpJcfzGBbGlT2VP7YhE4Qr8Ax__pfBYsrOyp6fMefCb3er4bDcmXJRYn5IpQgG7Xg_KQj8S7era04yxPASNDynLXGtLINDE_mOj2d2-PTMwIJSMSupRZ5NsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۶ VHF نیروی دریایی سپاه:«عبور و مرور در تنگه هرمز فقط با اجازه نیروی دریایی سپاه و در مسیرهای تعیین شده امکان‌پذیر است.
اگر هر کشتی‌ای بدون اجازه ما، با سیستم شناسایی خودکار خاموش یا خارج از مسیر تعیین شده اقدام به عبور کند، مسئولیت هرگونه عواقبی بر عهده آن کشتی خواهد بود.»
@withyashar</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/withyashar/15791" target="_blank">📅 16:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15790">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">قالیباف: آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما صرف خرید محصولات کشاورزی آن‌ها خواهد شد. جالب است؛ تنها محصولی که ما در حال برداشت آن هستیم، همان چیزی است که شما کاشته‌اید: دهه‌ها بی‌اعتمادی. این محصول، ارگانیک، فراوان و بومی است. اما ظاهراً آمریکا تنها سویاهای تراریخته، وعده‌های شکسته شده و یاوه‌گویی صادر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/15790" target="_blank">📅 15:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15789">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e51659f85.mp4?token=RFgDTFVNd0_CFt54sBg8IRZEIbZg7Vcpx15JLoOA1reswIV_-KuAhDnbbdFDrCjZQUk9erEpKL6APK2b2qxWL7i89C1CPVWnxX3Cmrc1CW4v2hRXhl0aXVl1dwPZaei0yJrm9O-PApW0XJ55eupgmilkGmXnxMIKpvDWPwn0Bl6fyXCPBV8Fw0JtbWJIXbxz3doMfhS7b91D0Xf7xF_tOz8XNRW33IKqVxX2u_wfn1s-h2znbskFFA1xrt6v9QOhUjFtAl1ZskHoi99aQtOQOtDm8BEu48zNByHgfl1diM005HGDK3IdZWgXBms7u6wXl66IeXRP3sL7dQoiDJESQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e51659f85.mp4?token=RFgDTFVNd0_CFt54sBg8IRZEIbZg7Vcpx15JLoOA1reswIV_-KuAhDnbbdFDrCjZQUk9erEpKL6APK2b2qxWL7i89C1CPVWnxX3Cmrc1CW4v2hRXhl0aXVl1dwPZaei0yJrm9O-PApW0XJ55eupgmilkGmXnxMIKpvDWPwn0Bl6fyXCPBV8Fw0JtbWJIXbxz3doMfhS7b91D0Xf7xF_tOz8XNRW33IKqVxX2u_wfn1s-h2znbskFFA1xrt6v9QOhUjFtAl1ZskHoi99aQtOQOtDm8BEu48zNByHgfl1diM005HGDK3IdZWgXBms7u6wXl66IeXRP3sL7dQoiDJESQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: هنوز مطمئن نیستم همه‌چیز تموم شده باشه، چون هر چند ساعت یه توییت جدید از ترامپ منتشر می‌شه و با هر توییت، تیتر خبرها عوض میشه؛
واسه همین فعلاً روی هیچ‌کدوم از حرف‌هایی که ترامپ زده حساب باز نمیکنم.
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/15789" target="_blank">📅 15:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15788">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اختلال بانک‌ها بعد از چندین روز همچنان ادامه دارد
رصد گزارش‌های مردمی در شبکه‌های اجتماعی، کانال‌های اطلاع‌رسانی و بازخورد کاربران نشان می‌دهد شبکه بانکی ایران از فاز اختلال شدید عبور کرده و بخش عمده خدمات به وضعیت عملیاتی بازگشته است.
در میان بانک‌های بزرگ، بانک ملی همچنان بیشترین حجم شکایت کاربران را به خود اختصاص داده است.
@withyashar</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/15788" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15787">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">روبیو: آمریکا خواهان توافق با ایران است، اما توافق به هر قیمتی را نمی‌پذیرد
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/15787" target="_blank">📅 14:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15786">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فرمانده نیروی قدس خطاب به اسرائیل:
اگر امروز با اختیار خود عقب‌نشینی نکنید، فردا با خواری و شکست ناگزیر به فرار خواهید شد
@withyashar</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/15786" target="_blank">📅 14:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15785">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b7288a91.mp4?token=XkThPeFxgrSi2S1penzpRuWFE4E9yxzqW6XRoW2Fu6spUdDgWbAlDOWgDnNEzJR8Ln_jIGZYFya3KFvFCcD1tO6HYPYM_HWHkgwFk-hf6FSvqNpuz8SMWL1xfIsvkMUu5u9TiM4mSRFxSURnne90kF-vRR-ATeUehZXu93CJhBJPrJbruXj0sHmTDDxe_DyN9lSoQEvHETWLT12InOd3_wi00USV2wm4IMiLJPYZBSl6iAJQcGj-IqbSo4JJZuOkYqv_nkkK8U0R7W1DGYuPrbRFWv6BHxhtHrI09vy4AITaVpyXZ2810QI9jEFcHocvFd3HXWjCnQ6RJRgTDEx-DkanvTMYTTdsqbehAOsKGisQ8ocqA7zjYplki-DNqCoeeBpNd-mY9q-5855QVZ1CbjH1DfkRgUUcPolHrjfIW53KuaFCObGAehdgeEvRiSXEbYInKA4APaACyzSNNpTQOQkyqVsfUcqR0goi_d9AwYsXPB-GtRDREnuoaXv4u8tbymjwztdQk7cYr_z--7KXR9A41NgY4LSsMl3_vWGejAvW4g1bHqwJo6FQBt8r4nyW_h3aFdDxMxoXVTs-XPQeOw8Z0HfzPIfIisCs_yH9c_t6Y6oQ6gOOEkz3UxR4aXIrvuIUvv84MQxqoOL33z8CzmmRn_dV6PT8bJB9eD0LyDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b7288a91.mp4?token=XkThPeFxgrSi2S1penzpRuWFE4E9yxzqW6XRoW2Fu6spUdDgWbAlDOWgDnNEzJR8Ln_jIGZYFya3KFvFCcD1tO6HYPYM_HWHkgwFk-hf6FSvqNpuz8SMWL1xfIsvkMUu5u9TiM4mSRFxSURnne90kF-vRR-ATeUehZXu93CJhBJPrJbruXj0sHmTDDxe_DyN9lSoQEvHETWLT12InOd3_wi00USV2wm4IMiLJPYZBSl6iAJQcGj-IqbSo4JJZuOkYqv_nkkK8U0R7W1DGYuPrbRFWv6BHxhtHrI09vy4AITaVpyXZ2810QI9jEFcHocvFd3HXWjCnQ6RJRgTDEx-DkanvTMYTTdsqbehAOsKGisQ8ocqA7zjYplki-DNqCoeeBpNd-mY9q-5855QVZ1CbjH1DfkRgUUcPolHrjfIW53KuaFCObGAehdgeEvRiSXEbYInKA4APaACyzSNNpTQOQkyqVsfUcqR0goi_d9AwYsXPB-GtRDREnuoaXv4u8tbymjwztdQk7cYr_z--7KXR9A41NgY4LSsMl3_vWGejAvW4g1bHqwJo6FQBt8r4nyW_h3aFdDxMxoXVTs-XPQeOw8Z0HfzPIfIisCs_yH9c_t6Y6oQ6gOOEkz3UxR4aXIrvuIUvv84MQxqoOL33z8CzmmRn_dV6PT8bJB9eD0LyDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود، من نگذاشتم
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/15785" target="_blank">📅 14:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15784">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسرائیل هیوم: به ارتش اسرائیل هیچ دستوری مبنی بر عقب‌نشینی داده نشده
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/15784" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15783">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مخالفت شدید چین با اقدامات آمریکا علیه کوبا
وزارت خارجه چین بیان کرد: چین همواره با تحریم‌های یکجانبه غیرقانونی که هیچ پایه و اساسی در قوانین بین‌المللی ندارند، مخالفت کرده است.
پکن از واشنگتن می خواهد تا فوراً به تحریم کوبا و هر نوع اجبار یا فشار پایان دهد. ما حمایت بی‌دریغ خود را از کوبا در جستجوی مسیر توسعه سوسیالیستی متناسب با شرایط ملی آن مجدداً تأیید می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/15783" target="_blank">📅 13:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15782">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">moamelegari-trump(@withyashar).pdf</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/15782" target="_blank">📅 13:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15781">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رویترز
:
اسرائیل به نشانه حسن نیت از بخشی از منطقه امنیتی جنوب لبنان عقب‌نشینی کرد
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/15781" target="_blank">📅 13:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15780">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سی‌ان‌ان: متحدان ترامپ در کشورهای حاشیه خلیج فارس بیم دارند که توافق او با ایران سرآغاز تحولی فاجعه‌بار باشد
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/15780" target="_blank">📅 12:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15779">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏وو باهیانا، پیشگوی برزیلی مدعی شده است که در جریان دیدار برزیل و اسکاتلند در جام جهانی ۲۰۲۶ که بامداد پنجشنبه در فلوریدا برگزار می‌شود، فضایی‌ها به زمین حمله خواهند کرد. او که بیش از ۲۳ میلیون دنبال‌کننده دارد، حتی ویدیویی تولیدشده با هوش مصنوعی از ربوده…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/15779" target="_blank">📅 12:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15778">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ: به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، امروز ایران نیروی دریایی، نیروی هوایی، پدافند ، پرتاب موشک، و تولیدی ندارد و رهبری آن نابود شده است. برای اولین بار در ۳۰۰۰ سال، ما بالاخره صلح را در خاورمیانه خواهیم داشت. @withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/15778" target="_blank">📅 12:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15777">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edea42e58c.mp4?token=pzK1MOhGUHWfcNiLKdz2nymKQyBlLwV-bzEdDdKmxGt3wFr8h0ou3DufcuNzj96xuGpTI4H-tfSFMS23STQO6c16reMO7aeYE7jWH2TZuTxgw8WDIsKAUn_G-zYzuy-xJB88B0qGGVKxUomIrPMghICo4DPPXeoGasRu_yRyrad5Dq-WKirGUFB6k167n7wxS4FmW1UZHZ3VmYPIk5h6RZTPJkyw4c4kXNd66OFjB72PKCb84wcpcEsy5TzeRxv8z-m3g6vWn6P8uTs1frzg3IqOmz0BhY1EbVo9_dONHuxIup8tZHV2hBYnHoAJjiq5x7D4XjefFvZYXX-4Owc1LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edea42e58c.mp4?token=pzK1MOhGUHWfcNiLKdz2nymKQyBlLwV-bzEdDdKmxGt3wFr8h0ou3DufcuNzj96xuGpTI4H-tfSFMS23STQO6c16reMO7aeYE7jWH2TZuTxgw8WDIsKAUn_G-zYzuy-xJB88B0qGGVKxUomIrPMghICo4DPPXeoGasRu_yRyrad5Dq-WKirGUFB6k167n7wxS4FmW1UZHZ3VmYPIk5h6RZTPJkyw4c4kXNd66OFjB72PKCb84wcpcEsy5TzeRxv8z-m3g6vWn6P8uTs1frzg3IqOmz0BhY1EbVo9_dONHuxIup8tZHV2hBYnHoAJjiq5x7D4XjefFvZYXX-4Owc1LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، امروز ایران نیروی دریایی، نیروی هوایی، پدافند ، پرتاب موشک، و تولیدی ندارد و رهبری آن نابود شده است.
برای اولین بار در ۳۰۰۰ سال، ما بالاخره صلح را در خاورمیانه خواهیم داشت.
@withyashar</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/15777" target="_blank">📅 12:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15776">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حمله اسرائیل به جنوب لبنان
@withyashar
🚨</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/15776" target="_blank">📅 12:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15775">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وال استریت ژورنال:
ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/15775" target="_blank">📅 11:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15774">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ایلان ماسک در پی سقوط سهام تسلا و اسپیس ایکس در معاملات روز چهارشنبه که ارزش دارایی او را به ۹۷۰.۲ میلیارد دلار کاهش داد، عنوان «تریلیونر» را از دست داد.
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/15774" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15773">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi4HMwKQzSb-aSmAEcK461mJj26FAzYcVv4KatemMzl7TK5RK5jiiqeT-iza2Jt4i581R5JlfdbJF1uVz4VTxSpF5Wz4jWQj9ox1KhPpAG1PF4kgWXuswelUiazyse1ci9dhd7fmbLEpOVXVmnpVEUbvf3RDSiFOs7QIVkqprAIkfdISB-4FeJu9Qd_7l-NgNYnbYMuaQcMMaFU8ykaCbw2u9wsS-7d0UJREzx6OtbRgNW40qdeVPRJWCDciF0VeLIDxi3h0dIDDhTGy-tzoGWLmDCe7seYk6CRLUhADtYZmeHD50WoNjyDV3rN5ByOCJYXMvxZq7MvzsAfvHFVNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد! رئیس جمهور دونالد جی ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/15773" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15772">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2960b1463d.mp4?token=fA8O7E-jqbkdJTzmeLWlSf3JPRHm8n46nikD2O5Lr6HT5Uirpw7eZuukjTNQwXcyS9LEpPYgbT_bI7RQZ_dg6nmMOewTVNyARBVJhrI8gP-qce3aAQ2H3OyUQF80DDb9l4twAwp_IFWHeJQ0eqE9ON_yThHiXx4TkeeGLL513_d4frXKxnJ4vMYc7aEU60hGKq-IHlqsuwsr_ZTBiyH8dcXJG7rrtpq0F9mHsz6KGhsBMnrNTl5Ogyd-w3B0cOB7HWUs_NFwpr0byzrgR-8-3P8xlRrQkkT6wa55OF15urFWW0IW9zgCtNhxWMf6CTmvC-gyIaQaH9gHWFQK0JNcHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2960b1463d.mp4?token=fA8O7E-jqbkdJTzmeLWlSf3JPRHm8n46nikD2O5Lr6HT5Uirpw7eZuukjTNQwXcyS9LEpPYgbT_bI7RQZ_dg6nmMOewTVNyARBVJhrI8gP-qce3aAQ2H3OyUQF80DDb9l4twAwp_IFWHeJQ0eqE9ON_yThHiXx4TkeeGLL513_d4frXKxnJ4vMYc7aEU60hGKq-IHlqsuwsr_ZTBiyH8dcXJG7rrtpq0F9mHsz6KGhsBMnrNTl5Ogyd-w3B0cOB7HWUs_NFwpr0byzrgR-8-3P8xlRrQkkT6wa55OF15urFWW0IW9zgCtNhxWMf6CTmvC-gyIaQaH9gHWFQK0JNcHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در دو جنگ جهانی پیروز شدیم، فاشیسم و ​​کمونیسم را شکست دادیم.
ما باید دوباره این کار را انجام دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/15772" target="_blank">📅 11:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15771">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">«قطعنامه اختیارات جنگی ایران» متوقف شد
‏ سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
‏ جمهوری‌خواهان و ترامپ استدلال کرده بودند، تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
‎
@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/15771" target="_blank">📅 10:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15770">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ درباره ایران: هفته گذشته، ما یک توافق تاریخی برای پایان دادن به درگیری با ایران امضا کردیم، تنگه هرمز را کاملاً باز کردیم و کاری را انجام دادیم که هیچ رئیس‌جمهوری قبلاً نتوانسته بود انجام دهد.
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/15770" target="_blank">📅 10:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15769">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSYvjgdPrITMpTFe059zp_BsYJzx-KOatIQkj5xv6gZwtz0yLxNzZKnrnmii1ro4ktV0Wfwk_gEbPtUDQllrYvtzn3RwOdcxx9QV_QLYBF1J41mKThUUgMyshqYqyNWpl3jz9ma3Awuzh5x14jeX0LEPh7Y8zwqY8qEiwRjz59dEVmnVFoKznPjj6M1sf_JPo5muyMNM-we2Nt_AwCqQnZ4DCuyhzt3cj5KzH3pdp4qTVOmdFZj8u7SVI8d0xzT0Mt9VLOTWDpSTUqvXBJqJsE3os5LYeB7hSFAxfHopJ0WZQ1kR5Yev8ux86RUIXbHTfI4gnZIyIsgALN60OuS8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌ تروث : دو زلزله بزرگ که به تازگی مردم بزرگ ونزوئلا را لرزاندند، هر دو در مقیاس وسیع بوده و تعداد زیادی کشته به جا گذاشته‌اند. ایالات متحده آماده، مایل و قادر به کمک است! من به تمام نهادهای دولتی دستور داده‌ام که برای اقدام سریع آماده باشند. ما در کنار دوستان جدید و بزرگ خود خواهیم بود. گزارش‌های اولیه خوب نیستند.
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/15769" target="_blank">📅 09:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15768">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هشدار سونامی در ونزوئلا، بعد از زمین‌لرزه۷ ریشتری، ویدیو منتشرشده از کاراکاس، برخاستن دود و گردوغبار از مناطق مختلفی را در پی این زمین‌لرزه شدید نشان می‌دهد. @withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/15768" target="_blank">📅 02:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15767">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5061be29e3.mp4?token=WYRjJqfof9Zr3xSwiABcDzceQ5Z8OmgXr7CBZ1YSLYYu7QDrPFJOkGT22cWCgee0z1E0lsuBn-VX9DayWy7pN5yxBXMjpv6R_AhwSX7vyibtlvRqqhbuPQhZojaIXex8Jevbjnkm92XFb1Sf5mzvKV7iKNRiayFEy8QaYAUOFN-2nItzSRv1EN8naO3jj-PHlI0QpYfYTH6upJU-uttRTSGlvKTW20CIbB39dmNzG0lNF_rrqF64w5kcnXT-rSE1vLxzFawR6d6paQWEdtq4UAp1oiNOzh7lBWcbUe3knUPsOLKaUBFyuOf7dzBAQxx8SdXCK1X5-YniKJHukd8JIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5061be29e3.mp4?token=WYRjJqfof9Zr3xSwiABcDzceQ5Z8OmgXr7CBZ1YSLYYu7QDrPFJOkGT22cWCgee0z1E0lsuBn-VX9DayWy7pN5yxBXMjpv6R_AhwSX7vyibtlvRqqhbuPQhZojaIXex8Jevbjnkm92XFb1Sf5mzvKV7iKNRiayFEy8QaYAUOFN-2nItzSRv1EN8naO3jj-PHlI0QpYfYTH6upJU-uttRTSGlvKTW20CIbB39dmNzG0lNF_rrqF64w5kcnXT-rSE1vLxzFawR6d6paQWEdtq4UAp1oiNOzh7lBWcbUe3knUPsOLKaUBFyuOf7dzBAQxx8SdXCK1X5-YniKJHukd8JIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هشدار سونامی در ونزوئلا، بعد از زمین‌لرزه۷ ریشتری، ویدیو منتشرشده از کاراکاس، برخاستن دود و گردوغبار از مناطق مختلفی را در پی این زمین‌لرزه شدید نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/15767" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15766">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏وو باهیانا، پیشگوی برزیلی مدعی شده است که در جریان دیدار برزیل و اسکاتلند در جام جهانی ۲۰۲۶ که بامداد پنجشنبه در فلوریدا برگزار می‌شود، فضایی‌ها به زمین حمله خواهند کرد. او که بیش از ۲۳ میلیون دنبال‌کننده دارد، حتی ویدیویی تولیدشده با هوش مصنوعی از ربوده شدن مردم منتشر کرده است.
‏گفته می‌شود بابا وانگا، پیشگوی مشهور بلغاری هم، وقوع یک تهاجم فضایی در جریان یک رویداد بزرگ ورزشی را پیش‌بینی کرده بود.
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/15766" target="_blank">📅 01:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15765">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">طارمی و الهویی دوباره در مرز آمریکا «معطل شدند»
ایرنا از معطلی کاروان تیم ملی پس از ورود به خاک آمریکا از مرز مکزیک خبر داده و نوشته مانند دو سفر قبلی، روند عبور مهدی طارمی و سعید الهویی، توسط ماموران مرزبانی طول کشیده است.
دیدار با مصر در سیاتل (ایالت واشنگتن) که مرز شمال غربی آمریکا با کانادا است برگزار می‌شود.
تیم ملی برای صعود مستقیم به دور حذفی باید مصر را شکست دهد اما با تساوی مقابل این تیم هم می‌تواند به صعود به عنوان تیم دوم یا سوم باقی امیدوار بماند.
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/15765" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15764">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IurToX4mpFrpNSYmYuvf041E-3rDbQF5VTi_-a6klgSkyxm5678UmnIOioVd8GUTHg1JIog3FK2ip0ayS139wfXzHCpLdq14xbTa_ox4nmHFYX6FqzRKCs4JkUeKXLyVMSQUa8FuSIzIyXbUP-2TBxSB46jBh0TQIqiISVj1CGEWiGT59Mzv4_0MGGDOkFST0plGJ8FJEI4oGEDThpIKznGrpRwB6vxnKT6phpNjR2UxnScVklbk3-MGq-wqWPuZwKfvQaVTuEQGDfXNhS6hDQt3DuKlt3uJtOfWIeT0ffC_0NIup5ICPCuAMtTLdP6j6IFdxN9MefAHY88CLnWZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر «آبراهام لینکلن (CVN-72)» نیروی دریایی آمریکا در تصاویر ماهواره‌ای در فاصله ۱۴۰+ کیلومتری بندر چابهار ایران مشاهده شد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/15764" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15763">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فاکس‌نیوز : ترامپ به دنبال تأمین ۶۷۲ میلیون دلار برای حذف مواد هسته‌ای ایرانی است
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/15763" target="_blank">📅 23:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15762">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزارت امور خارجه ایران: واشینگتن باید از تفسیرهای متناقض با مفاد یادداشت تفاهم بپرهیزد.
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/15762" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15761">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارشهای زیاددددد از صدای انفجار دوباره  در بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/15761" target="_blank">📅 22:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15760">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15760" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15759">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جنجال در ایتالیا پس از افشاگری درباره همکاری پنهان در جنگ علیه ایران پولیتیکو: افشاگری مارک روته، دبیر کل ناتو در خصوص استفاده آمریکا از پایگاه‌های ایتالیا در جنگ علیه ایران واکنش تند گوئیدو کروستو، وزیر دفاع ایتالیا را در پی داشت.  گوئیدو کروستو گفت: تنها…</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/15759" target="_blank">📅 22:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15758">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جنجال در ایتالیا پس از افشاگری درباره همکاری پنهان در جنگ علیه ایران
پولیتیکو: افشاگری مارک روته، دبیر کل ناتو در خصوص استفاده آمریکا از پایگاه‌های ایتالیا در جنگ علیه ایران واکنش تند گوئیدو کروستو، وزیر دفاع ایتالیا را در پی داشت.
گوئیدو کروستو گفت: تنها پروازهای مطابق با معاهدات مجاز بوده‌اند؛ پیام روته کاملا اشتباه است.
احزاب مخالف در ایتالیا از این توضیحات قانع نشدند. آنجلو بونلی، نماینده سبزها گفت: ملونی به ایتالیایی‌ها و پارلمان دروغ گفت. ملونی باید فورا روشن کند چه اتفاقی افتاده و به پارلمان گزارش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/15758" target="_blank">📅 22:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15757">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فردا فرمانده ستاد فرماندهی مرکزی ایالات متحده(سنتکام( به اسرائیل خواهد رسید
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15757" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15756">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نعیم قاسم ، رهبر حزب الله ، اعتراف کرد که یک گروهک تروریستی نمی تواند ارتش اسرائیل را در رویارویی مستقیم نظامی شکست دهد
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/15756" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15755">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/15755" target="_blank">📅 22:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15754">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتَهمتَن</strong></div>
<div class="tg-text">داش تو ویست گفتی بوست کنیم؟</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15754" target="_blank">📅 22:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15753">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/15753" target="_blank">📅 22:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15752">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/15752" target="_blank">📅 22:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15751">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAdam Fazaei</strong></div>
<div class="tg-text">یاشار جان ایموجی فقط جاوید شاه دیگه نیست ؟</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/15751" target="_blank">📅 22:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15750">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromf</strong></div>
<div class="tg-text">سلام
داداش
بجز اخبار یه چیزی هم خودت بگو
مرسی
دلتنگ صدات شدیم
😂</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/15750" target="_blank">📅 22:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15749">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بندر عباس صدای ذرت مکزیکی‌ میاد
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/15749" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15748">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وال‌استریت ژورنال؛ ترامپ اقدامات جسورانه علیه ایران انجام داد که هیچ رئیس‌جمهوری پیش از او جرأت انجامشان را نداشت، اما در نهایت به همان نقطه‌ای رسید که دیگران هم در آن قرار داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/15748" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15747">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال 14 اسرائیل:اسرائیل در حال آماده‌سازی برای احتمال حمله دوباره به حوثی‌های یمن است
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/15747" target="_blank">📅 22:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15746">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78282e8e68.mp4?token=b_YHUBC0ogSzXKzxfNOB7m-WCZhLAHu5C4gFEHV8MvjPFzu4eWeaDZEe77hUQUybx-GbwsR3afwXR55VSBlJu_pHhT2V9JYaO12bEvqfyQ849k-YfWrr4ZY8KScjh12TTENAneWftmWPX-ShOl0xfCM5K_gssY3PJWRnTqLh5XkRq0LgPXFbCyV66CgcYmDZ3Y1s3qfc__4emxZQKL5Z-UXDvW-GTr8FtVUMi7ZsePs160cI-vxmYNJj4M0_3UOfshBjd_eN4QW9Ce8zMRsuejDKsPL_KWES4ZBkpa1KIvy00kXH0KUNzWEh8nSfv0vIh-Zj-OokNTL29AxNLhsR9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78282e8e68.mp4?token=b_YHUBC0ogSzXKzxfNOB7m-WCZhLAHu5C4gFEHV8MvjPFzu4eWeaDZEe77hUQUybx-GbwsR3afwXR55VSBlJu_pHhT2V9JYaO12bEvqfyQ849k-YfWrr4ZY8KScjh12TTENAneWftmWPX-ShOl0xfCM5K_gssY3PJWRnTqLh5XkRq0LgPXFbCyV66CgcYmDZ3Y1s3qfc__4emxZQKL5Z-UXDvW-GTr8FtVUMi7ZsePs160cI-vxmYNJj4M0_3UOfshBjd_eN4QW9Ce8zMRsuejDKsPL_KWES4ZBkpa1KIvy00kXH0KUNzWEh8nSfv0vIh-Zj-OokNTL29AxNLhsR9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شبکه کان اسرائیل : آمریکایی‌ها در حال ترک فرودگاه بن‌گوریون هستند
ایالات متحده ۲۸ فروند هواپیمای سوخت‌رسان را تخلیه کرده و اسرائیل نیز به‌دلیل نگرانی از اختلال در پروازهای غیرنظامی در طول تابستان، اسرائیل خواستار تخلیه حدود ۲۰ هواپیمای دیگر شده است.
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/15746" target="_blank">📅 21:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15745">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام ندهید. در غیر این صورت مسئولیت با شماست و توسط حرص و طمع خود شما انجام گرفته. به این مسئله دقت کنید و
فقط از تحلیلها و مطالب آموزشی افراد استفاده کنید
. هیچ پکج یا هیچ پرداختی به هیچ بی ناموسی انجام ندهید.
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
از توجه شما به این مطلب سپاسگزارم، یاشار</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/withyashar/15745" target="_blank">📅 21:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15744">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">1$ / Tether = 167,000 Toman
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/15744" target="_blank">📅 21:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15743">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزیر انرژی آمریکا مدعی شد: بازگشت جریان نفت به حالت عادی به دلیل مین‌های ایران به تأخیر افتاده است
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/15743" target="_blank">📅 21:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15742">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یدیعوت آحارونوت: فرمانده سنتکام به زودی وارد اسرائیل می‌شود و با وزیر جنگ و رئیس ستاد ارتش دیدار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/15742" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15741">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c79bdeee0.mp4?token=CdYBLajPJXrgBby-nOGmtuQwLRVz5XbhJrTQsILHHuTP_xB36n6R3zKdWAuVlzP8UuDe8dPeqD8Z3yxuUHNKWS8EOpSmPIzWZCQ7h6LyYoissvXC8QXzYdO2JmF0C7i-yZVsTXF5bx-yWMsfD26xmxDCm0F4RJItkJMYVTDdkrAlXOG-SwgwVYy0cDVyuG9EeRNoD3wVSRjZCT-WATweli9fnZfnfRBiYZRidUFt0SaZTRKhiaKq5XhMZfHGK-l6sB_Uf-i0FL0pxsRPyK23ZvMlzd0NvzC5GBp8Zcoc-LUzEdXouoZ_7a85XUFAblhdbI0QsH7Wgb79M-jSHR3HBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c79bdeee0.mp4?token=CdYBLajPJXrgBby-nOGmtuQwLRVz5XbhJrTQsILHHuTP_xB36n6R3zKdWAuVlzP8UuDe8dPeqD8Z3yxuUHNKWS8EOpSmPIzWZCQ7h6LyYoissvXC8QXzYdO2JmF0C7i-yZVsTXF5bx-yWMsfD26xmxDCm0F4RJItkJMYVTDdkrAlXOG-SwgwVYy0cDVyuG9EeRNoD3wVSRjZCT-WATweli9fnZfnfRBiYZRidUFt0SaZTRKhiaKq5XhMZfHGK-l6sB_Uf-i0FL0pxsRPyK23ZvMlzd0NvzC5GBp8Zcoc-LUzEdXouoZ_7a85XUFAblhdbI0QsH7Wgb79M-jSHR3HBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جنگ داره خیلی خوب پیش میره. همون‌طور که می‌دونید، ما داریم با اختلاف زیاد می‌بریم. ایرانم داره امتیازهای خیلی بزرگی میده. ببینیم آخرش چی میشه، ولی واقعاً اوضاع خیلی، خیلی، خیلی قدرتمند پیش رفته.
@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/15741" target="_blank">📅 21:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15740">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">روزنامه تلگراف به‌نقل از منابع نزدیک به ترامپ مدعی شد که رئیس‌جمهور آمریکا احتمالاً
پس از انتخابات میان‌دوره‌ای کنگره، توافق فعلی با ایران را کنار می‌گذارد و به‌دنبال توافقی جدید خواهد رفت.
به‌گفته این منابع، ترامپ برای مهار فشارهای اقتصادی و حفظ موقعیت جمهوری‌خواهان در انتخابات، به توافق کنونی با ایران نیاز داشته است , بازگشایی تنگه هرمز و دستیابی به تفاهم با تهران، نگرانی بخشی از جمهوری‌خواهان را کاهش داده است.
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/15740" target="_blank">📅 21:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15739">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آکسیوس: اولین دور مذاکرات اسرائیل و لبنان در واشنگتن بدون نتیجه پایان یافت و گفت‌وگوها در فضایی به شدت پرتنش برگزار شد
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/15739" target="_blank">📅 20:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15738">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ:ایران تاکنون 500 میلیون دلار مواد غذایی آمریکایی خریداری کرده است.   @withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/15738" target="_blank">📅 20:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15737">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:ایران تاکنون 500 میلیون دلار مواد غذایی آمریکایی خریداری کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/15737" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15736">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYH0TEwgxvnw2JVg3b8LhUDq9oz-zrz6FpEvnUEFyBr7KCAI3w1HF1xA6HQZhaYiTfxbANZrSNMl8xyUyPntLrJtx1yPp8xDPRWNFPvmplQVdcWGDfYeCURZuLXvefxLr8egs9V6h7yyj05IZcQ-hqcYL-ZmEe4M8rphu6KgZzU3OBa1__0lZN523jgmngAQcP5OwzVIDPu0fkwC0oqkwU4yUy3ZPL9baHGPNJ2z2mph3lfgUETa7oWnpB8rog-HglHKvADMaIGYSZiJjjpJ_Z4RX-jfqcjfRTDJ1zdjEoU8zMBS-c4zQA3JsG6Zy6m_lv95pejcjCBH-VwVUnbsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیت‌کوین به زیر ۶۰٬۰۰۰ دلار سقوط کرد
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/15736" target="_blank">📅 20:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15735">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مرحله دوم مذاکرات فنی ایران و آمریکا ۸ تیر برگزار می‌شود
وزیر خارجه آمریکا دقایقی پیش در اظهاراتی گفت که مذاکرات فنی ایران و آمریکا، روز ۲۹ ژوئن / ۸ تیر در سوئیس برگزار می‌شود. پیش از این نیز وزارت خارجه پاکستان اعلام کرد که مذاکرات ایران و آمریکا هفته آینده از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/15735" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15734">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58bddbc88.mp4?token=aX8nQMghLND6EXYm_uX-XBy3SHJgx3EQBtjqzhxBCFuj7CFibfqhTmgdMLyN46_7JE2ZRQ_MieupF19WSqXW2K3GNaCQ4MntX5y374jexmRou0Gi-gN2jmhwSoGUpWzk6nofGJ1CX71LI2JEAd1-ODnpU24JDsn1PoD-KuFKpQIh-1ElgLWa__Upw3Pm4KAYQXCuag5OUt-eW-QQjLytZsAHgzO3o1VpTZVwN0Bkvb6pqaXW-7R06otOJpfrqLec8kwRitPV9tP0_zR6QpEXVqcb9GGw8Qt7Mv_8qqLDTolxij0RstxLI7veWx-hh64P8514DUbfh0rGl6baTwJjqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58bddbc88.mp4?token=aX8nQMghLND6EXYm_uX-XBy3SHJgx3EQBtjqzhxBCFuj7CFibfqhTmgdMLyN46_7JE2ZRQ_MieupF19WSqXW2K3GNaCQ4MntX5y374jexmRou0Gi-gN2jmhwSoGUpWzk6nofGJ1CX71LI2JEAd1-ODnpU24JDsn1PoD-KuFKpQIh-1ElgLWa__Upw3Pm4KAYQXCuag5OUt-eW-QQjLytZsAHgzO3o1VpTZVwN0Bkvb6pqaXW-7R06otOJpfrqLec8kwRitPV9tP0_zR6QpEXVqcb9GGw8Qt7Mv_8qqLDTolxij0RstxLI7veWx-hh64P8514DUbfh0rGl6baTwJjqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : من بیشتر دوران بزرگسالی‌ام را به جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای اختصاص دادم.
آماده نبودم اجازه دهم زنجیره‌ای از هزاران سال تاریخ یهودی به خاطر دستیابی این آیات‌الله‌ها به سلاح‌های هسته‌ای شکسته شود.
به همین دلیل بیشتر دوران بزرگسالی‌ام را به این هدف اختصاص دادم همچنین به عنوان نخست‌وزیر
@withyashar</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/15734" target="_blank">📅 19:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ارتش اسرائیل: یکی دیگر از تروریست‌های حماس که در قتل عام ۷ اکتبر به اسرائیل نفوذ کرده بود، از بین رفت.
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/15733" target="_blank">📅 19:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کانال 13 اسرائیل:
نتانیاهو امشب یک جلسه امنیتی درباره لبنان و سوریه برگزار خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/15732" target="_blank">📅 19:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتانیاهو: از ترامپ اجازه‌ای برای حمله به ایران درخواست نکرده‌ام بلکه تنها آن را به او ابلاغ کردم.
ماموریت ما در لبنان هنوز پایان نیافته است.
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/15731" target="_blank">📅 18:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15730">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/832f75f201.mp4?token=UkqHvBNrYh8OkidWq_DNWBnn6HSpeH2oYiQskZUwcadNasy0m7zw5TQdBcZmyjKlDsr5wE53OTMpSRHXa-DwNzABO3q5iXzyXeBfrVfF6z4e2uJGmc1r1oQnGpC-rCeGndtX8vasp5xH9sWtv4UZlC-i-ppy9b7DUTMLJlqVGsjr2HA8X_WDgy9H32G8uq6bkLl3T13MDiwgALzDFr9jzFPZ3lKoEWtBEyb9BCFMA19vw5LmArm7sn0NZJvZRe_bFJ5Us9hYiq1G-Acofx-9B8uR6fw21cs67i_Lc-AJA8Y9_yWG3ExSRXfSqiCZsbtjRsKJfKedAhilXfZghalS5VCfarcpm3q05VIeLbrdob7OxL6WBsi_EevWgHecW9jWqqNYHR6w5MIRrl42sAQZm-hRUM1EYasedwreUYzFvLDZx2s5IilM0wHloMMGAJC7tQkySy-Tx52T7bKe3JlyVRTDomdAI-8u2n0g2F5i72oaHl6-gILgXAkdf9oMgc8WwAQq4SzRKgZfjLSjqxyCAC-oH7RWLVGXbpjuONlsX7dGTucy_3ETtTLIBWzMrBiUs5-SReO0y0izJu5UARaiJfrDJWTF0-04Jw29trhemzlRC-RFwlF2yUxxfx8OalUipJPK1N4QyEL40owCu5xXTdJFtBeI8Co5GbKeHAZqDBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/832f75f201.mp4?token=UkqHvBNrYh8OkidWq_DNWBnn6HSpeH2oYiQskZUwcadNasy0m7zw5TQdBcZmyjKlDsr5wE53OTMpSRHXa-DwNzABO3q5iXzyXeBfrVfF6z4e2uJGmc1r1oQnGpC-rCeGndtX8vasp5xH9sWtv4UZlC-i-ppy9b7DUTMLJlqVGsjr2HA8X_WDgy9H32G8uq6bkLl3T13MDiwgALzDFr9jzFPZ3lKoEWtBEyb9BCFMA19vw5LmArm7sn0NZJvZRe_bFJ5Us9hYiq1G-Acofx-9B8uR6fw21cs67i_Lc-AJA8Y9_yWG3ExSRXfSqiCZsbtjRsKJfKedAhilXfZghalS5VCfarcpm3q05VIeLbrdob7OxL6WBsi_EevWgHecW9jWqqNYHR6w5MIRrl42sAQZm-hRUM1EYasedwreUYzFvLDZx2s5IilM0wHloMMGAJC7tQkySy-Tx52T7bKe3JlyVRTDomdAI-8u2n0g2F5i72oaHl6-gILgXAkdf9oMgc8WwAQq4SzRKgZfjLSjqxyCAC-oH7RWLVGXbpjuONlsX7dGTucy_3ETtTLIBWzMrBiUs5-SReO0y0izJu5UARaiJfrDJWTF0-04Jw29trhemzlRC-RFwlF2yUxxfx8OalUipJPK1N4QyEL40owCu5xXTdJFtBeI8Co5GbKeHAZqDBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، بسنت : سلطه دلار خیلی مهمه
همه کارهایی که ترامپ داره انجام می‌ده، دلار رو دوباره محور تجارت جهانی می‌کنه
تو ونزوئلا و حتی مذاکرات با ایران هم می‌بینیم که معاملات قراره با دلار انجام بشه
درکل، همه این اقدامات جایگاه دلار رو دوباره تقویت می‌کنه
@withyashar</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/15730" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ به فاکس‌نیوز اعلام کرد که قرار است به بازرسان اجازه داده شود تا مکان‌هایی که اورانیوم ایران در آنجا نگهداری می‌شود، بازدید کنند. از سوی دیگر، ایران قصد دارد در اولویت اول، کالاهای آمریکایی به ارزش حدود ۵۰۰ میلیون دلار خریداری نماید. هیچ عجله‌ای برای ورود بازرسان وجود ندارد و تیم آمریکایی قرار است همراه با بازرسان آژانس برای یافتن اورانیوم غنی‌شده اعزام شوند.
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/15729" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ: بازرسان آمریکایی برای بازرسی سایت های هسته ای ایران به آژانس بین المللی انرژی اتمی می پیوندند‌‌
ترامپ: هیچ عجله‌ای برای دسترسی به این مواد وجود ندارد، زیرا پس از عملیات «چکش نیمه‌شب» در زیر زمین دفن شده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/15728" target="_blank">📅 17:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ در تروث : شهردار ممدانی با حمایت سه کمونیست تمام‌عیار به پیروزی رسید و رسانه‌های جعلی هم با سروصدای زیاد و به‌صورت یکپارچه برایش کف زدند. تبریک آقای شهردار!
من دیشب ۱۶ برد از ۱۶ داشتم و به انتخاب میهن‌پرستان فوق‌العاده آمریکایی کمک کردم، اما رسانه‌ها حتی یک کلمه هم درباره‌اش نمی‌گویند.
در دو سال گذشته، حمایت و تأیید من باعث ۲۵۹ پیروزی در انتخابات مقدماتی شده و تقریباً هیچ شکستی نداشته است، با این حال هیچ توجهی از سوی رسانه‌ها دریافت نکرده‌ام!
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/15727" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6227a74ce9.mp4?token=S98lbwgU7PouW9dEKA2NvtpMRIvYYJnQt9lhIcz6NiMy2NZBv2BqOZbT7esE0yVV2fQm5pJtrf9tMOcCOq4201Wzs3jA-G3i8D_AKxA88lDjjTTstXl-NmsqWBoTTTaW3iLb9IKkjaUCt3Om4599tXq4nPX_Q86HNsVtkQ2X03R6o4Y5l7XVsspJmzV2-CzrWkohQj3-BQ93JwkiTLAdIbvvBMjx9AS_ZdXcR2UcTrY27er__fUCABY5qrVkzlH5h5eYbNaRXgeH0iCGY_t-rOdUCzCTeHSfr0k7KaHWOQG4diW_ljZ6A-ZcMQHJkn10P9EWdyGPIVzLkUGkzw3PNm_QEEe0j1kyVVrDaFl_kQRdI21vy8Usr6MpHZagpSB7ogl15kVMs7F_5r3JU5mDcPMjqbYqD5rhkSY3Xo46P-hCVgKLRRo9Gn8L0NAPkZH5H6F3xh8i6Tv_DUlDeBwYvvcWYXFye-JtXMYc1GEKl1jXzNIIg4db5GCwQSHf6XHHxTVVJO-wi3QQS-yMf4SB24QEoaqIUX8-ZX4EUbbCn2fL7vDez5vcZBVnAbnMF9EgSvxkVdZ-yo6cSfGNr3gIrAvWewTHaABqyJE3iPxP4c7_UPgGC7aHt1AMVDAYC7Ls_QETP3G0P8pt9H0qerv0-h8uUTzwl_zRbzQ7plM5A_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6227a74ce9.mp4?token=S98lbwgU7PouW9dEKA2NvtpMRIvYYJnQt9lhIcz6NiMy2NZBv2BqOZbT7esE0yVV2fQm5pJtrf9tMOcCOq4201Wzs3jA-G3i8D_AKxA88lDjjTTstXl-NmsqWBoTTTaW3iLb9IKkjaUCt3Om4599tXq4nPX_Q86HNsVtkQ2X03R6o4Y5l7XVsspJmzV2-CzrWkohQj3-BQ93JwkiTLAdIbvvBMjx9AS_ZdXcR2UcTrY27er__fUCABY5qrVkzlH5h5eYbNaRXgeH0iCGY_t-rOdUCzCTeHSfr0k7KaHWOQG4diW_ljZ6A-ZcMQHJkn10P9EWdyGPIVzLkUGkzw3PNm_QEEe0j1kyVVrDaFl_kQRdI21vy8Usr6MpHZagpSB7ogl15kVMs7F_5r3JU5mDcPMjqbYqD5rhkSY3Xo46P-hCVgKLRRo9Gn8L0NAPkZH5H6F3xh8i6Tv_DUlDeBwYvvcWYXFye-JtXMYc1GEKl1jXzNIIg4db5GCwQSHf6XHHxTVVJO-wi3QQS-yMf4SB24QEoaqIUX8-ZX4EUbbCn2fL7vDez5vcZBVnAbnMF9EgSvxkVdZ-yo6cSfGNr3gIrAvWewTHaABqyJE3iPxP4c7_UPgGC7aHt1AMVDAYC7Ls_QETP3G0P8pt9H0qerv0-h8uUTzwl_zRbzQ7plM5A_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشد دارایی ونس و هگس در طی سالها
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/15726" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15725">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13a4e4286.mp4?token=cMUcFz7RNzztl7W7RX_JwW5sYx1YxwA0mH5B_RG55jag7FB2aiEf97Q-SrzSC45T0KeqWDbvOPeejCK2wtv83N7z0UVpHdeGwnhZwO9ug5pUZwXGT1SjspETXsEWQkwm8yexYblbqf1dEYo3AfGHoEzucMz9UCoQyBrDubMGiG03mR2QQoLrgVUOB8yhkJNUY5CxtRrQuLmHyKazsIY-O-cjvfA4XAcYl64rd4pIVwctoUbqpiRNd0XrC6M2v8TQpx1Qpy5_F9EQkqUTNdGVATu-MRbKLfVlShLvOVc4yCMGSjKDVcq7NjblX8nl7UWC-YxPzNm7TxcvAobFXshncg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13a4e4286.mp4?token=cMUcFz7RNzztl7W7RX_JwW5sYx1YxwA0mH5B_RG55jag7FB2aiEf97Q-SrzSC45T0KeqWDbvOPeejCK2wtv83N7z0UVpHdeGwnhZwO9ug5pUZwXGT1SjspETXsEWQkwm8yexYblbqf1dEYo3AfGHoEzucMz9UCoQyBrDubMGiG03mR2QQoLrgVUOB8yhkJNUY5CxtRrQuLmHyKazsIY-O-cjvfA4XAcYl64rd4pIVwctoUbqpiRNd0XrC6M2v8TQpx1Qpy5_F9EQkqUTNdGVATu-MRbKLfVlShLvOVc4yCMGSjKDVcq7NjblX8nl7UWC-YxPzNm7TxcvAobFXshncg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری دولتی لبنان گزارش داد:
یک پهپاد اسرائیلی خودرویی را در نزدیکی شهرک کفررمان در جنوب لبنان هدف قرار داد و دو نفر کشته شدند.
پیش‌تر نیز سخنگوی ارتش اسرائیل اعلام کرد نیروهای ارتش دو عضو مسلح حزب‌الله را که تهدیدی برای نیروهای اسرائیلی در منطقه علی‌الطاهر در جنوب لبنان بودند، هدف قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/15725" target="_blank">📅 17:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15724">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">قیمت اونس طلا به زیر ۴ هزار دلار رسید؛ آیا سقوط ۱۵۰۰ دلاری از اوج تاریخی ادامه خواهد داشت؟
قیمت نقدی طلا روز چهارشنبه ۲۴ ژوئن (سوم تیر ۱۴۰۵) تحت تاثیر رشد ارزش دلار آمریکا و افزایش انتظارات مبنی بر تداوم بالا ماندن نرخ‌های بهره در این کشور، برای نخستین بار از ماه نوامبر ۲۰۲۵ میلادی، از مرز روانی ۴ هزار دلار در هر اونس پایین‌تر آمد.
تقویت ارزش دلار آمریکا باعث شد تا خرید شمش طلا که بر مبنای دلار قیمت‌گذاری می‌شود، برای دارندگان سایر ارزها گران‌تر تمام شود.
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/15724" target="_blank">📅 17:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5b8c6375.mp4?token=cd7g4Azoeth5C39v1OS8pwZ2y_H7VqctvXi75vKt39GwgTVl9Sga9npflH21ym0cUhQyB3ZONuPzWLP1tcY9ZaZFmQigZlFzhd2GqBUf7VDSNcBRxrP0O0gbZgWjE-kqXh4icKUpiUJaFHdLrS7HcBElvyU5wKnclqnvH5YFDyEMvfX8ppk4PmPXrY6IW9hun9M_ehVSusJCFuQl-CVi2WdID2sufQZcUUGqCmQtdHR5r5_P0DJibHGMgMyG3VB-Jn3GmP4klJU_2gwvq9F9djDQnzBNt5b3L5uA9B5aef88NYoZ2kqBYGymoI7u_e_3qjwow21_rMvOdJW7HxNGYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5b8c6375.mp4?token=cd7g4Azoeth5C39v1OS8pwZ2y_H7VqctvXi75vKt39GwgTVl9Sga9npflH21ym0cUhQyB3ZONuPzWLP1tcY9ZaZFmQigZlFzhd2GqBUf7VDSNcBRxrP0O0gbZgWjE-kqXh4icKUpiUJaFHdLrS7HcBElvyU5wKnclqnvH5YFDyEMvfX8ppk4PmPXrY6IW9hun9M_ehVSusJCFuQl-CVi2WdID2sufQZcUUGqCmQtdHR5r5_P0DJibHGMgMyG3VB-Jn3GmP4klJU_2gwvq9F9djDQnzBNt5b3L5uA9B5aef88NYoZ2kqBYGymoI7u_e_3qjwow21_rMvOdJW7HxNGYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، برای دومین مرحله از تور خاورمیانه خود به کویت رسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/15723" target="_blank">📅 17:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سنتکام: «نیروهای فرماندهی مرکزی ایالات متحده در تاریخ ۱۹ ژوئن یک حمله هوایی در شمال‌غرب سوریه انجام دادند که به کشته شدن یکی از رهبران ارشد داعش منجر شد.
در این حمله دقیق، علی حسین العلوی کشته شد. این عملیات بخشی از تلاش‌های مستمر آمریکا برای مختل کردن و از بین بردن عناصر تروریستی است که در پی حمله به شهروندان آمریکایی در خارج از کشور یا خاک ایالات متحده هستند.
نیروهای سنتکام همچنان در همکاری با شرکای منطقه‌ای به عملیات خود ادامه می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/15722" target="_blank">📅 16:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بسنت وزیر خزانه‌داری آمریکا به سی‌ان‌بی‌سی:
هر پولی که رژیم تهران دریافت کند، متعلق به ایرانی‌هاست.
نسبت بسیار زیادی از پول برای خرید غذا و داروی آمریکایی استفاده خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/15721" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15720">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فاکس‌نیوز گزارش میدهد : پرزیدنت ترامپ روز شلوغی را در واشنگتن دی سی آغاز می‌کند و آماده می‌شود تا به کنگره برود، جایی که طبق گزارش‌ها قرار است با جمهوری‌خواهان سنا در مورد قانون متوقف شده «نجات آمریکا» ملاقات کند.
در طول اقامتش در کنگره، قرار است قانون «جاده قرن بیست و یکم به سوی مسکن» را نیز امضا کند.
همه این اتفاقات پیش از جلسه کاخ سفید بین ترامپ و مارک روته، دبیرکل ناتو، در اواخر امروز رخ می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/15720" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15719">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYQjeYMPuVof_02U0GrfoSWqJVxRQPCET5tPPODPalVdibCvMexLMQTdL5003gWFz9rbXN4MEEnITo2cHvtA2gCdvi9R94yV-t7w6xCILb0shA_vqlN9l7PWpcmpMrBTSv0v5a1L4LC1b9EtCYxdg1cWrrggB7_t37zq_a4lVD06eXa2hOzpQdRWiy9iFGXtrBq3TkUc94ONABOR1YjtmZVYxJxWe0KssSSuk8ZrGieae22IIDGjwtdqBWefXs_a5ifdhQZEKLvzFp5j2-IEIg2AmTFyUBmixgagrdfy12lpcgZFDHg7-5y_LOrWi0Qn-t5iFbz9EAgVKtXoXABWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در ‌تروث : «ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دردسرساز رسانه‌های جعلی، هیچ‌گونه عوارض، هزینه بیمه یا هیچ نوع هزینه دیگری از کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌کند. اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت.
همچنین، هیچ پولی از سوی آمریکا به ایران پرداخت نشده و هیچ بخشی از دارایی‌های ایران نیز مستقیماً در اختیار این کشور قرار نگرفته است. ما بخشی از دارایی‌های ایران را که همچنان کاملاً تحت کنترل ماست، برای پرداخت به کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا از آن برای خرید ذرت، گندم، سویا و سایر محصولات استفاده شود.
ایران به‌شدت به مواد غذایی نیاز دارد و ما این اقلام را منحصراً از ایالات متحده برای آن‌ها تأمین خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم.»
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/15719" target="_blank">📅 15:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBdfGK38Yjw65l4QK6J6cYFCXrKPl_Mkyr-fRs-2lPGDiFLfy0B1JX_nS0H_EvHjLzDk8AiVm5WBYUZc4XNoTtVUISITmXCV5FYU9fnM0e1QfzmSPa60g_pjw9yDQEIzNO2AQbrIyC4mQb0FI2oCAqAaEozBp-3ac97Vmw34ffL2S7RZC9EfyanETZDJ3lQXTGo2_yOLs_rWuFXl1rb_pRzPdYeK0i_oD3zYOk2CGOdKN-Cz21CwOgcPV1fUynDKD-ZzrLWar9iYvarsvYpDyKOQ1mdxatJ9CyMNgrBpaBwKjtJC5N8jjvUyE9VFp4nEzttTSgil2caOwaD-MJ5jBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارن پالیسی:
توافق ایران زمینه درگیری‌های بیشتری را فراهم می‌کند
!
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/15718" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">با اعلام راکستار،قیمت بازی GTA6 مشخص شد.
نسخه Standard:
80 دلار، معادل 12 میلیون تومن.
نسخه Ultimate Edition:
100 دلار، معادل 16 میلیون تومن.
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/15717" target="_blank">📅 14:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حسین پاک، خبرنگار مستقر در لبنان: در نقض آتش‌بس دیروز اسرائیل در لبنان، ۳ شهید داشته‌ایم
دشمن درحال برنامه‌ریزی بلندمت جهت اشغال منطقه طیبه است.
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/15716" target="_blank">📅 14:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">قالیباف در باکو: تفاهم‌نامه امضاشده برای پایان جنگ «اعلام شکست آمریکا» است
او در بیستمین کنفرانس اتحادیه مجالس کشورهای عضو سازمان همکاری اسلامی (PUIC) در باکو گفت: «تفاهم‌نامه ‌اسلام‌آباد نه نتیجه فشارو اجبار، بلکه حاصل مقاومت و اقتدار ملت شجاع ایران بود... یادداشت تفاهم اسلام‌آباد تبدیل به اعلامیه شکست آمریکا شد.»
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/15715" target="_blank">📅 14:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">غضنفری، نماینده تهران : امیدواریم قالیباف سر عقل بیاد و مجلس رو باز کنه.
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/15714" target="_blank">📅 14:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">معاون وزیرخارجه خطاب به ترامپ:
نمی توانید با هیاهوی رسانه ای، سیاست "راه بینداز و جا بینداز" را پیش ببرید.
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/15713" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ee6905e4.mp4?token=H-zra4HKBSbhDMUeeMYiIVFPGoPy9yQuW4Zhl3clKhE5Ume5bwT1C-CnNGGuWzH6y29HGGIxPPJvAaYW9pH7AmQp1B26TjwJk4GBaiGeYcMdWpWlh8G8-dRQJomHDIGyPhAu44jFM6-dKYqX8LQW0IM1sF-Oks-slCLFwvfpbp2hr6OVJGRNOsIz2ZnIOPUr0yXNeNlgEyZufezSh4_2mawEz5iW1YbG4KRI-3FuqpKd55cyxMMDcglgQQYBZQ-EbG8WSmAXL3Ib0cY1H7opvmUA93R97J8A8BpWVmAkKG_VQ0Tipi3oEUMQFqCSwpmPSq-y9sUJjBDQ2ipJZ_P8-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ee6905e4.mp4?token=H-zra4HKBSbhDMUeeMYiIVFPGoPy9yQuW4Zhl3clKhE5Ume5bwT1C-CnNGGuWzH6y29HGGIxPPJvAaYW9pH7AmQp1B26TjwJk4GBaiGeYcMdWpWlh8G8-dRQJomHDIGyPhAu44jFM6-dKYqX8LQW0IM1sF-Oks-slCLFwvfpbp2hr6OVJGRNOsIz2ZnIOPUr0yXNeNlgEyZufezSh4_2mawEz5iW1YbG4KRI-3FuqpKd55cyxMMDcglgQQYBZQ-EbG8WSmAXL3Ib0cY1H7opvmUA93R97J8A8BpWVmAkKG_VQ0Tipi3oEUMQFqCSwpmPSq-y9sUJjBDQ2ipJZ_P8-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترافیک سنگین در‌ جاده شمال
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/15712" target="_blank">📅 13:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/15711" target="_blank">📅 13:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پایان شهادت نتانیاهو در پرونده فساد مالی
بنیامین نتانیاهو پس از ۹۸ جلسه استماع در ۱۸ ماه گذشته، دفاعیات خود را در پرونده اتهامات فساد و رشوه به پایان رساند و با اشاره به شرایط سال‌های اخیر، گفت که «۱۰ سال جهنمی» را تحمل کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15710" target="_blank">📅 13:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وقوع تیراندازی درپایتخت ترکیه،آنکارا رسانه‌ها از وقوع حادثه تیراندازی در آنکارا خبر می‌دهند. @withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/15709" target="_blank">📅 13:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15708">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وقوع تیراندازی درپایتخت ترکیه،آنکارا
رسانه‌ها از وقوع حادثه تیراندازی در آنکارا خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/15708" target="_blank">📅 12:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15707">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اختلال بانک‌های کشور برطرف شد
با اعلام شرکت خدمات انفورماتیک، اختلال خدمات کارت محور بانک‌های کشور برطرف شد.
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/15707" target="_blank">📅 12:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15706">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آژانس ایمنی هوانوردی اروپا به شرکت‌های هواپیمایی توصیه کرد همچنان از پرواز در حریم هوایی ایران خودداری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/15706" target="_blank">📅 12:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15705">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رویترز: قراردادهای آتی نفت خام برنت به ۷۵.۷۴ دلار کاهش یافت که پایین‌ترین سطح آن از ۲۷ فوریه گذشته است
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/15705" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15704">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyEw0KmoBz0dKlEkIRHRE1dBQKjcZDdP1-0WlmagSrTnl72KErRuQ72b3CvQKX_tQReGQLrkpJrlp1pFuWpvFVt4Y84izuFx6Y6YJdEsCWhg1RSFbZed4Ktazlv3wLdX9SsMDJOiQi_pP394WTfAiw5BraMGflifnc-teOFMmT31RELIgw8JiZceo7ursO-Kgd5EggV9BbUaCMvLdP8OWESq0CXDozQPgSDJZL0N-3Xmr9RdAt9mh9wNoMZ6m2BdbJd8EVq9cJ8rdWEOOH_y4rjb8iX98nqepyFk2Dniag5aRbtqmK9jzqlslUbjEZPfUqOIR-qJQD1YkI2dz7J0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در تروث ‌: ایران رو کاملاً تحت فشار گذاشته بودم؛ در آستانه عقب‌نشینی بود، حاضر بود تقریباً هر چیزی که ما می‌خواستیم رو قبول کنه و واسه اولین بار تو چند دهه گذشته، احترام فوق‌العاده‌ای برای آمریکا و رئیس‌جمهورش، یعنی من، قائل شده بود.
ولی سنای آمریکا تصمیم گرفت تو بدترین زمان ممکن، یه رأی‌گیری بی‌معنی درباره قانون اختیارات جنگی (War Powers Act) برگزار کنه؛ رأی‌گیری‌ای که به بزرگ‌ترین حامی تروریسم تو جهان این پیام رو میده که آمریکا از کاری که من با اونا می‌کنم، راضی نیست و باید متوقفش کنم.
با این کار، عملاً به دشمن کمک کردن و دلگرمی دادن.
این سناتورها فقط کار من رو سخت‌تر کردن، ولی به هر شکلی که شده، کار رو به سرانجام می‌رسونم؛ چون من همیشه کارها رو به نتیجه می‌رسونم!
@withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/15704" target="_blank">📅 11:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15703">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هم اکنون دلار در تهران به صورت ناگهانی از 165هزار تومان عبور کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/15703" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15702">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgWca2zhRh8AKbxIBTiU7huSfui4ukG85pPXWPEvW38kySUKB2Ypyl1BFW-fjvcHL9Wd1NuLEKL8NvllvM1rzCxZ4uk-D01ffpQ7PJHnbdwsDofdBSa3aKOnGT13p3b-2DMrXpfbhvYBNhUw2wgNVFKyzJ1Uz0rx3oPLyAAY1COZh2pApl6ZLd58vBblVL302FVbUve0U05qb67iP-L_PmPCgGQZQwaev3KrLbQBQyd3nYDHzk89kyvqs4Ustlsh0Em2Ds82u88KeqSyvcN56Ojc0MGO8ibOs6MApbrndF3iix8GGb8ocArLqEae8nmpzHopqDQVoymT8pqTuHyC9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هگست:  اولین آزمایش سامانه پدافندی جدید «گنبد طلایی»، با موفقیت انجام شد @withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/15702" target="_blank">📅 11:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15701">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هگست:  اولین آزمایش سامانه پدافندی جدید «گنبد طلایی»، با موفقیت انجام شد
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/15701" target="_blank">📅 11:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15700">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پاکستان: مذاکرات فنی میان آمریکا و ایران هفته آینده از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/15700" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15699">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dj6bjlNnYjFy2bphd44uW0-Ueg8C29JUdgz4GTL8hCABe9NTUJiCOJOTsUcq9FDN23_Vf-6wEejBVJ__bhrGeAPLTEU8I7QgLuDORQXYGhLvUAtzoB1x-bj88eQGIvXTlk3PjC8ZZ-g7iR1GTzP6oEGwkQuAn6DQ0VO53NmDGZZ4RHSnp13P5IptKLUTnSWypC-o4_3w6EbjGIVeg58W8IFBWYowfEKxX67DD-BgZ4TQKHPkGlnZiqNqBoX8n-Z1QSjIQMzWUKyvNaE--k3oKXXt5-Fqg1o_E2yp9fCpz2plQJHNMyP8txl74uSIZnkxOQy0CZVeog_u65KQo4z1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین بروزرسانی از استقرار ناوهای نیروی دریایی آمریکا:
در منطقه سنتکام، دو ناوگروه لینکلن و بوش به همراه ناو آبی‌ـ‌خاکی تریپولی همچنان در منطقه حضور دارند و بخش عمده توان رزمی دریایی آمریکا را تشکیل می‌دهند.
دست‌کم ۱۷ فروند ناوشکن از کلاس آرلی برک نیز در دریای عرب، دریای سرخ و شرق مدیترانه حضور دارند که توان قابل توجهی در اختیار نیروی دریایی آمریکا قرار می‌دهند.
در غرب اقیانوس آرام، ناو هواپیمابر واشینگتن نخستین گشت عملیاتی خود در سال ۲۰۲۶ را در دریای فیلیپین آغاز کرده و ناو آبی‌ـ‌خاکی باکسر نیز در دریای چین جنوبی مشغول فعالیت است.
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/15699" target="_blank">📅 10:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15698">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی: از تأسیسات هسته‌ای ایران بازرسی خواهیم کرد
ما معتقدیم که بازرسی از تأسیسات هسته‌ای ایران در اسرع وقت بهترین گزینه است
اولویت اصلی ما مشخص کردن محل ذخایر اورانیوم غنی‌شده با خلوص بالای ایران است.
ما از محل اورانیوم غنی‌شده با خلوص بالا اطلاع داریم، اما مهم است که ایران ما را از آن مطلع کند.
به زودی با ایران برای تعیین تاریخ بازرسی‌ها و جزئیات مربوطه مذاکره خواهیم کرد
آژانس ما بازرسی را انجام خواهد داد و این به تهران بستگی دارد که واشنگتن یا ناظران دیگر را دعوت کند.
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/15698" target="_blank">📅 10:43 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
