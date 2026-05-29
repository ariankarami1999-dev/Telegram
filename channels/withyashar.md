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
<img src="https://cdn4.telesco.pe/file/AXI3kVeVnvMhtoMqjE7KhrY1VfRvc_B-jncJDO3BhaymhX0Z1iF39Fdvs9Wg6-o2Qbmv16JDdxN-rRTlJ1nv_ZKxqjobYXkE0kpRctwnP-Boo4DqAxKkmXYjVyZsvd8tMwZKrN8rog1KmaKAw9QROFEvJ7fEiELL2xFfJttfHs6mix7rI5NkpB10aEv86ERY409KVTOBE3IWRJOSVRClThbsGFaSkxUawmtPvQBc06ZH44U7libCZWmCK8ri-STBG6bJQgwiwbG7ZgNpyB0s6fY_A45qPDqXyTQ1d62QgOPkCIX15XQotBmH5_hRsKtKgZ0AoqMxzh8Cq8FivZN50Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 281K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 20:58:16</div>
<hr>

<div class="tg-post" id="msg-12888">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرگزاری فرانسوی: جارد کوشنر مانع امضای تفاهم‌نامه بین آمریکا و ایران شد
@withyashar</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/withyashar/12888" target="_blank">📅 20:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12887">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🤣
😃</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/withyashar/12887" target="_blank">📅 20:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12886">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/withyashar/12886" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12885">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مدیرکل آژانس بین‌المللی انرژی اتمی پیشنهاد داد که قزاقستان اورانیوم غنی‌شده ایران را نگه‌داری کند
@withyashar</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/withyashar/12885" target="_blank">📅 20:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12884">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">لارنس نورمن، خبرنگار وال استریت ژورنال:
این توافقی که ازش صحبت می‌شه فعلاً یه توافق کامل نیست که تمامی مسائل از جمله هسته‌ای رو در بر بگیره
@withyashar</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/12884" target="_blank">📅 20:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12882">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کاش جای ترامپ دو تا بی بی داشتیم البته همون یدونشم کارو در میاره .این کله زرد به خاطر پول زرد میکنه اخرش</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/withyashar/12882" target="_blank">📅 20:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12881">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza Rohani</strong></div>
<div class="tg-text">کاش جای ترامپ دو تا بی بی داشتیم البته همون یدونشم کارو در میاره .این کله زرد به خاطر پول زرد میکنه اخرش</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/withyashar/12881" target="_blank">📅 20:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12880">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خب دیگه عمو یاشار با پای پیاده میریم نه با ترامپ</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/12880" target="_blank">📅 19:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12879">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParsa</strong></div>
<div class="tg-text">خب دیگه عمو یاشار با پای پیاده میریم نه با ترامپ</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/12879" target="_blank">📅 19:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12878">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/withyashar/12878" target="_blank">📅 19:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12877">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پرزیدنت ترامپ در اتاق وضعیت کاخ سفید مستقر شد.
تصمیم‌گیری نهایی درباره مذاکرات با رژیم ایران در دستور کار است.
نیویورک پست: واشینگتن برای گام‌های بعدی آماده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/withyashar/12877" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12876">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">به نظر میاد قاهره کنسل شد مارو وسط راه پیاده کرد</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/12876" target="_blank">📅 19:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12875">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAm.ir_reza</strong></div>
<div class="tg-text">به نظر میاد قاهره کنسل شد مارو وسط راه پیاده کرد</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/withyashar/12875" target="_blank">📅 19:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12874">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">jangal bedoneh risheh (iG @yashar)</div>
  <div class="tg-doc-extra">siavash ghomeishi (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/12874" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/withyashar/12874" target="_blank">📅 19:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12873">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فارس: متن توافق که تحت قالب «تعهد در برابر تعهد» تدوین شده، در مراحل نهایی تصویب در ایران قرار دارد و هنوز تصمیم قطعی اتخاذ نشده است.
@withyashar
کلان رژیم جمهوری اسهالی‌تو کاره فیفتی فیفتیه
🥴
🤣</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/withyashar/12873" target="_blank">📅 19:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12872">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فارس : ترامپ تا نیمی از پول رو نداده همه چیز باد هوا است
@withyashar
🤣</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/12872" target="_blank">📅 19:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12871">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرگزاری فارس: ادعاهای ترامپ دروغه و فعلاً خبری از توافق نیست.
@withyashar</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/12871" target="_blank">📅 19:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12870">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncSuLScONCzFvuTQRm4a9V4fh5xPktyRg9yJNL4dqKsqTBaJXRfpwbMeMcLkbRggKV0gwYoTom3zQTCTSCz6SUWZYgcmhoiq3pfU9cZSXCP7cviuUNdxDggA_9IXeFzLI3X4fJAkqaAtsqPytNOI9TKNwmMqm3e5HjcNzqNNxRsqFglE7peCS7Ssk_6jrUs7xIEF6M0fiYtk3oz-mwfjw37Vf18IH1paRzVoPuPi83l6iDnixpr0mm6vvVFiVELa_9Rimc0Bvg5ZKaIWeL9Fr77KfYgYIZoFBZ0v3z8Z4KJLjP8ADB3FF_cFZS7u0hcQC1Elv2LiVMyCnm9ZAyWj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از پست ترامپ در تروث سوشال، قیمت نفت برنت برای اولین بار پس از 50 روز به زیر 90 دلار در هر بشکه رسید.
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/12870" target="_blank">📅 19:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12869">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اتاق جنگ با یاشار : ریلکس‌ باشید ترامپ در هر صورت کار رو در میاره ولی حامله میکنه
🤣
🙌🏾
داریم میریم قاهره</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/12869" target="_blank">📅 19:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12868">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خبرنگارهای نزدیک به کاخ سفید می‌گویند: ترامپ منظورش را در پستش اشتباه بیان کرده بود؛ او در واقع پایان محاصره دریایی علیه ایران را اعلام نکرده.
بلکه منظورش این بوده که اگر ایران با این شروط موافقت کند، آن محاصره لغو خواهد شد.
@withyashar
🥴</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/12868" target="_blank">📅 19:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12867">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اتاق جنگ با یاشار : یا موسئ ادرکنی
@withyashar
معنی ادرکنی : مرا دریاب و به فریادم برس</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/12867" target="_blank">📅 18:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12866">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتاق جنگ با یاشار : ریلکس‌ باشید ترامپ در هر صورت کار رو در میاره ولی حامله میکنه
🤣
🙌🏾
داریم میریم قاهره</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/12866" target="_blank">📅 18:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12865">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کانال ۱۵ عبری: به نظر میرسد ترامپ با یادداشت تفاهم با ایران موافقت کرده است
@withyashar</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/12865" target="_blank">📅 18:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12864">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الجزیره: ناوگان سوخت رسان های آمریکا در فرودگاه بن‌گوریون تا ۷۲ ساعت دیگر به پایگاه های اصلی خود در اروپا برمیگردند
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/12864" target="_blank">📅 18:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12863">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/12863" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12862">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.  تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/12862" target="_blank">📅 18:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12861">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhzWybJLCveQhCn0nBjuuv12wk7VyWmda06d4mRrte7EnjNcHmwf0g7DSIKSlWg1F9iErh5ZMXdzh_yMTQ9M72QKVc2qYF9ASBnpRMhfzwagwpx4ZgbGfCJtRaXzMby-SwfPd8TtWaDKdA9wmZPDsGm8uG2jQnKGuLJgFgmfWXzc11nR_ZXa0ZE97sx0YIPZHfzZ1s3WBKrvFv-3iVF75NxS39HeZiu4S12DHcr4qPL8-_R0vPC1YQO99w6ccqxEEazkvvzFN_r6zY5J-of-6o205pjlLUPeaOKqZJcSjK3Dw_uyNInW-6llQZttL-kTdPCSzLRaGPROtR-tOhLg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
@withyashar
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
@withyashar
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/12861" target="_blank">📅 18:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12860">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02caddcc.mp4?token=t32HNtNIISM17fbPwT6UmADc2rihdkwEecs4SZwzif7_PYAS1Xa2Xps9YpeYWUt5umWhNKiAAjml1SBMg57CPtRcUcdbor6W0AUwctuoumPJG1oD8GuSVI8tp097oxBcQE1m4YZGWsw1TTh79J6L4HRsfe38shnky9AVN17pYH2_H-KoYbaa-0JliyEy2TO1X4omP9-RTiDezK0L2hLBxAT-jlcqh3KvFC98HyajiSjs3oWhiU00L2sSZeUHYwAvheeIKfpcuRWS7bMuK-MNtATa7kooABrg6rqZkc-nM1wGJUkIKZpcrzwdTOM4pt3IxNd1MHsJmkFgeIbL9zbTOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02caddcc.mp4?token=t32HNtNIISM17fbPwT6UmADc2rihdkwEecs4SZwzif7_PYAS1Xa2Xps9YpeYWUt5umWhNKiAAjml1SBMg57CPtRcUcdbor6W0AUwctuoumPJG1oD8GuSVI8tp097oxBcQE1m4YZGWsw1TTh79J6L4HRsfe38shnky9AVN17pYH2_H-KoYbaa-0JliyEy2TO1X4omP9-RTiDezK0L2hLBxAT-jlcqh3KvFC98HyajiSjs3oWhiU00L2sSZeUHYwAvheeIKfpcuRWS7bMuK-MNtATa7kooABrg6rqZkc-nM1wGJUkIKZpcrzwdTOM4pt3IxNd1MHsJmkFgeIbL9zbTOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم تحلیلگر ارشد صدا و سیما:   دوران بمب اتم دیگه گذشته الان با عملیات میکروبی و بیولوژیک میشه حمله کنیم و بعدش نگیم که ما بودیم
@withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/12860" target="_blank">📅 18:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12859">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">️فاکس نیوز به نقل از وزیر جنگ آمریکا: ایران دو گزینه دارد: یا از طریق مذاکره برنامه هسته ای خود را کنار بگذارد یا از طریق نیروهای ما
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/12859" target="_blank">📅 17:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12858">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تسنیم : مذاکرات در جریان است و متن توافق تغییر هایی داشته است
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/12858" target="_blank">📅 17:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12857">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzQswYxV6hC0YK6L3_rVd8tCaihPxf2pk4PXTTOaPnhYH4851yRPl5H8cG8dtqr8wjhj9HvScdzMeSW6vl2hOMN7abA-vYzzEZv9WWtjeOQ0xaf3WJM14kmIKU53aKwRksgtJd-uKh37ZJBsTdmhG8JffmJgB5Bd20vgPD7-xWr_VZam_DD1ttpZg8XYpyzWlqLQn5bSSg7PNt-UrHE44gpE-ZBWV2-n49Q7ADCKiydS5RB7yfAU9DCvhhEo8K6MpDPGJSVivu_Ud3hhGKIc_c5sN3x0j1JaqRBe_G5gpTkPr-Iyn2qJwdvtxyeDYd9fwZQ87TRUAVa8tno106q1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مم با قر خالیباف‌ در اکس :
۱- ما امتیازات را نه با گفتگو، بلکه با موشک‌ها می‌گیریم، در مذاکره فقط آن‌ها را تثبیت می‌کنیم.
۲- هیچ اعتمادی به تضمین‌ها و حرف‌ها نداریم، فقط رفتارها معیار است. اقدامی پیش از اقدام طرف مقابل انجام نخواهد شد.
۳- پیروز هر توافق، کسی است که از فردای آن بهتر برای جنگ آماده شود.
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/12857" target="_blank">📅 16:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12856">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">️سی‌ان‌ان: ترامپ به مشاورانش گفته  که برای تصمیم‌گیری در مورد امضای توافق احتمالی با تهران به چند روز زمان نیاز داره
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/12856" target="_blank">📅 15:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12855">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEZD1ZDSl0z5CY5ygiFGwxVFGZ7Vnn5IkqQQ-8zmEyNdKoBG6CmjJICFJbDs-rwB86ZNs6oI4BTtK8fFIY7FaUF6qMx8fmoiW0Tlc5Sm9fnmwSazxIZWGe97k7P8fFVzIEwJXWaJzpchZ-47sH9WGSIb-6SVc13PJdaK536Y2YhN6TsoUc5g9tFl_9s3V1xEDU2wKZNRlqzOtLGeHCP1-IffbMYGnBrnzAulTe-s83ibJd3MeXy-RLphyLqxNv3LVjbHSMZPxzLWeO8QAt1gZ_ABUOLGtdbS4orvp58VhN34VCF3TzvwEJBtZWVDR8CV6rwapgD5uTDJKftKW5Yukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سری سوالات بی جواب تجمعات شبانه
😃
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/12855" target="_blank">📅 14:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12854">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded froms@ti🍁🍂️</strong></div>
<div class="tg-text">سلام یاشار جان
من نامزدمو یه هفته پیش از دست دادم سرطان داشت
😔
تا لحظه ی اخر میگفت ناامید نباش یاشار گفته میزنه،تو دی ماه هم واقعا به سختی نجات پیدا  کردیم از تو خیابون .واقعا اگه ما پیروز نشیم من حس میکنم خون این همه ادم پایمال میشه،ما فقط به امید شما داریم زندگی میکنیم.هیچ وقت اخرین حرفشو تو ملاقات اخر یادم نمیره.فقط پیام دادم بگم  حتی امید اون ادمی که روی تخت بیمارستان هم نفس های اخرشو میکشه هم  هستی
🥺
خدا حفظت کنه واسه ما
🙏
❤️
🌺</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/12854" target="_blank">📅 14:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12853">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ffdc5f87.mp4?token=olW2Gb_rGNmsCKuE6a3CoafzPWnHqFGnABoEd8QE__UNCKilYiy6zxfUnvgtL9ulCmeCsDSC8mjkrx_tXbe8Z3SENjSL73s-0lJca-zd3z-F_ZNEnNqMHg6rT4Tk5jcUpJ-Vtda2DWiYa0lkgpJN-4H_9F8a_yi77zryrmOLUCcsob9S_STQBDedV6jwCfC5E7UCmyFHZbLp1NYkwv4rAlIWNN4hG3dp5XslCc0DHFKLdWz0S9a-N87-v5YugQLQYr-IICfstsH8_r3_bpTUw-vrji3HZgoAyeYo-qAs1Ch_x45OW5e1WBUrgVwukVyVhHWyc1OhCh_NkIdARlcmiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ffdc5f87.mp4?token=olW2Gb_rGNmsCKuE6a3CoafzPWnHqFGnABoEd8QE__UNCKilYiy6zxfUnvgtL9ulCmeCsDSC8mjkrx_tXbe8Z3SENjSL73s-0lJca-zd3z-F_ZNEnNqMHg6rT4Tk5jcUpJ-Vtda2DWiYa0lkgpJN-4H_9F8a_yi77zryrmOLUCcsob9S_STQBDedV6jwCfC5E7UCmyFHZbLp1NYkwv4rAlIWNN4hG3dp5XslCc0DHFKLdWz0S9a-N87-v5YugQLQYr-IICfstsH8_r3_bpTUw-vrji3HZgoAyeYo-qAs1Ch_x45OW5e1WBUrgVwukVyVhHWyc1OhCh_NkIdARlcmiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست ، وزیر دفاع آمریکا با لاتی‌ پر مانند مربیی که تیمش را به زمین میفرستد،  خطاب به نیروهای آمریکا روی ناو USS Boxer گفت:
«رئیس‌جمهور گفت: ایران یا می‌تواند راه درست را انتخاب کند یعنی پای میز مذاکره توافق کند یا با مردِ سمت چپ من طرف شود.»
«آن مردِ سمت چپ، اتفاقاً من بودم.»
«اما در واقع من نیستم…»
«شمایید.»
یعنی شما نیروهای نظامی آمریکا هستید.
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/12853" target="_blank">📅 14:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12852">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromomid.behroozi</strong></div>
<div class="tg-text">سلام یاشار عزیز من امشب عروسیمه امشب میزنه آماده باشم تو باغ مهمونا رو از قبل آماده کنم میزنه ؟؟
😂
😂</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/12852" target="_blank">📅 14:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12851">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بر اساس تحلیل نشریه اکونومیست، طرفین درگیر ممکن است بیش از هر زمان دیگری به یک توافق نزدیک شده باشند.
با این حال، این توافق جامع نخواهد بود و جنگ را برای همیشه پایان نخواهد داد.
این نشریه در ادامه توضیح می‌دهد که چگونه ملاحظات و بازی‌های سیاسی، عامل اصلی ارسال این پیام‌های ضدونقیض از سوی طرفین است
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/12851" target="_blank">📅 13:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12850">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نیویورک تایمز: یکی از جدیدترین و شگفت‌انگیزترین عناصر پیش‌نویس توافق صلح ایران، یک صندوق سرمایه‌گذاری پیشنهادی برای ایران به مبلغ ۳۰۰ میلیارد دلار است.
ایران در ابتدا این موضوع را به عنوان غرامت برای خسارات جنگ (که آن را بین ۳۰۰ میلیارد تا ۱ تریلیون دلار تخمین می‌زند) مطرح کرد. طرف آمریکایی آن را به عنوان یک «صندوق سرمایه‌گذاری بین‌المللی» که به تسهیل آن کمک می‌کند، بازتعریف کرده است
یک چارچوب نرم‌تر که از کلمه غرامت اجتناب می‌کند.
به نظر می‌رسد این ایده از استیو ویتکوف و جرد کوشنر نشأت گرفته است که پروژه‌های املاک و مستغلات تهران و یک ابزار سرمایه‌گذاری گسترده‌تر را به عنوان شیرین‌کننده‌های معامله مطرح کردند
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/12850" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12849">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوستان من گفتم فردا میگم کجا متن ها رو بفرستید دوبار هم در متن تاکیید کردم! پیغام هایی که الان دایرکت دادید بین پیغام های‌دیگه میره و از دست میره حتی نیمتونم بخونم
😟
چرا درک نمیکنید خیلی واضح گفتم</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/12849" target="_blank">📅 13:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12848">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خب این متن را مینویسم که همه حتما ببینند. امروز و فردا روز بسیار مهمی هست. ما هر دو شب را بیدار خواهیم ماند برای گزارش و برای دوشنبه آخر شب هم در صورتی که حمله نبود میخواهیم یک پیام برای شاهزاده بفرستیم ساعت ۱۱:۱۱ دقیقه . در نتیجه از همه شما دعوت میکنم خیلی…</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/12848" target="_blank">📅 13:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12847">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71af41e04e.mp4?token=ePYGEpFlSmJeAbZ-7oPcF7fGMI18WlSEk3cVyKrmayoUOa85yTv3aKZ8jXvou5mEWDC4tnR6TYlE2j8_1T_vOpCc--Yu7Aw5wlYU__6Srnx9t0Co3iZetMLYMTVwfkoKsZlltukXLZOTxFsS-jMksGihNjCv_R8m0xhm60Ys1Xrq1Himd2kYhJVPsKJjdVbk3qn2z20gT8fBjM65Wc839pDzAemMRcD2M68TVAJBMmLhUVMZWhDXW7I7VzVYdr94jqdhVaJlamwe6FFMp_2IWbODXd5yxXqpSx_ZDw4ZqSfB4s1HNSXFphcjQdXyLCmwMzs7nPSgV1wgKMnAtttWX7XrPRnYnAam3t5O-lnLOp8IdYoQh6dZ_wTrrs0XLo4mNMs5bqYNjnom02O4-VWSJvScSzG7R1XKL3GJuIR0CwHP28tZ06Lz1I3mgEnDvYPt_DhgPPbrXjmcVFU7lGqPCRCo9NLPYGvKOU0VG_gidwaTVwtPadbUQFCFm6Jk87-MPeU9jCD5YT34v9mRyXgOAbQ2dLGe4PevTM1DjUQ0_F2-WrmtghTQSRVvZNbMmeer8dq-s3dK3S7KzNHP9VK9eo6YKeO1lVllD_szTnMWA0sTOe3STSWjFyd7RLV_ou1n_SkgclCPyuuzbqqeh2jNafHDu3wWp8gOUu-xFQxyhng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71af41e04e.mp4?token=ePYGEpFlSmJeAbZ-7oPcF7fGMI18WlSEk3cVyKrmayoUOa85yTv3aKZ8jXvou5mEWDC4tnR6TYlE2j8_1T_vOpCc--Yu7Aw5wlYU__6Srnx9t0Co3iZetMLYMTVwfkoKsZlltukXLZOTxFsS-jMksGihNjCv_R8m0xhm60Ys1Xrq1Himd2kYhJVPsKJjdVbk3qn2z20gT8fBjM65Wc839pDzAemMRcD2M68TVAJBMmLhUVMZWhDXW7I7VzVYdr94jqdhVaJlamwe6FFMp_2IWbODXd5yxXqpSx_ZDw4ZqSfB4s1HNSXFphcjQdXyLCmwMzs7nPSgV1wgKMnAtttWX7XrPRnYnAam3t5O-lnLOp8IdYoQh6dZ_wTrrs0XLo4mNMs5bqYNjnom02O4-VWSJvScSzG7R1XKL3GJuIR0CwHP28tZ06Lz1I3mgEnDvYPt_DhgPPbrXjmcVFU7lGqPCRCo9NLPYGvKOU0VG_gidwaTVwtPadbUQFCFm6Jk87-MPeU9jCD5YT34v9mRyXgOAbQ2dLGe4PevTM1DjUQ0_F2-WrmtghTQSRVvZNbMmeer8dq-s3dK3S7KzNHP9VK9eo6YKeO1lVllD_szTnMWA0sTOe3STSWjFyd7RLV_ou1n_SkgclCPyuuzbqqeh2jNafHDu3wWp8gOUu-xFQxyhng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس دفتر کاخ سفید در امور سیاست، استیون میلر:
ایران امتیاز های خیلی قابل توجه، مادی  به ایالات متحده داده که قبلا میگفت غیر ممکنه
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/12847" target="_blank">📅 13:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12846">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فارس نیوز ، خطیب نماز جمعهٔ تهران: دشمن متوقف نیست، ما باید در مرز دانش و فناوری حرکت کنیم
حجت‌الاسلام ابوترابی: تعرض آمریکا در سحرگاه دیروز به نقطه‌ای در حاشیه فرودگاه بندرعباس که نه خسارت جانی داشت و نه خسارت مالی، اما تعرض به آسمان و زمین ایران بود. این تعرض از پایگاه هوایی آمریکا در منطقه انجام شد
@withyashar
🥴</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/12846" target="_blank">📅 13:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12845">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خب این متن را مینویسم که همه حتما ببینند. امروز و فردا روز بسیار مهمی هست. ما هر دو شب را بیدار خواهیم ماند برای گزارش و برای دوشنبه آخر شب هم در صورتی که حمله نبود میخواهیم یک پیام برای شاهزاده بفرستیم ساعت ۱۱:۱۱ دقیقه . در نتیجه از همه شما دعوت میکنم خیلی رسمی و محترمانه صحبتهای خود را بنویسید  و امروز بر روی متن تمرکز کنید و فردا از ساعت ۱۰ صبح تا ۱۰ شب برای من ارسال کنید تا چکیده ای از تمام آنها را ارسال کنم و فقط کلام من نباشد. حتی شده یک کلمه از پیام هر شخص را برمیداریم و متنی باهم میسازیم که در خور باشد. پس از شما دعوت میکنم به این کمپین بپیوندید ،لطفا امروز و فردا از فرستادن دایرکتهای غیرمعمول بپرهیزید سوال بیشتری را نمیتوانم پاسخ بدهم متن کامل است هر صحبتی که دارید  در  همان متن بنویسید تا همه با هم متن پایانی را استوری،  کامنت ، دایرکت و ایمیل کنیم
🙌🏾
. شروع ارسال فردا ۱۰ صبح و آخرین مهلت ارسال برای من  فردا ۱۰ شب است.
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/12845" target="_blank">📅 11:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12844">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تحلیل عوستاد رائفی پور :
آمریکایی‌ها نیروهای بیگانه فضایی هم کمک گرفتن
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/12844" target="_blank">📅 11:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12843">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شبکه العربیه به نقل از منابع آگاه گزارش داد جمهوری اسلامی می‌خواهد اورانیوم غنی‌سازی‌شده خود را به چین منتقل کند، مشروط بر آن‌که چین تضمین دهد این مواد را به آمریکا تحویل نخواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/12843" target="_blank">📅 11:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12842">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اسرائیل هیوم در گزارشی نوشت موساد در سال‌های اخیر شاخه‌ای محرمانه برای نزدیک‌تر کردن سقوط جمهوری اسلامی ایجاد کرده است. به گفته منابع آگاه، رییس موساد متقاعد شده است که اگر ترامپ با تهران توافق نکند و محاصره دریایی را ادامه دهد، جمهوری اسلامی تا پایان سال ۲۰۲۶ سقوط می‌کند.
ماموریت ابتدایی این شاخه که در سال ۲۰۲۱ و پس از آغاز ریاست داوید بارنیا بر موساد ایجاد شد، عملیات‌ هدفمند برای کنار زدن مقام‌های ارشد جمهوری اسلامی بود، اما به‌تدریج به بخشی از راهبرد گسترده‌تر موساد برای «تغییر رژیم» تبدیل شد.
رییس پیشین این شاخه به اسرائیل هیوم گفت موساد در گذشته بیشتر از طریق ترور افراد را حذف می‌کرد، اما اکنون افشای اطلاعات شرم‌آور یا آسیب‌زننده درباره مقام‌ها می‌تواند آن‌ها را از حلقه قدرت خارج کند؛ روشی که به گفته او «ارزان‌تر و ساده‌تر از عملیات ترور» است.، مقام‌های موساد معتقدند عملیات‌های اخیر علیه ایران فقط یک مرحله در مسیر سقوط جمهوری اسلامی بوده است. رئیس پیشین شاخه نفوذ گفت این واحد اکنون با شدت بیشتری فعالیت می‌کند و هدف آن «سریع‌تر کردن ساعت شنی پایان حکومت است».
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/12842" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12841">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سنتکام : ادعا: تلویزیون دولتی ایران ادعا کرد که نیروهای ایرانی یک هواپیمای آمریکایی را در نزدیکی بوشهر سرنگون کرده‌اند. نادرست.
حقیقت: هیچ هواپیمای آمریکایی سرنگون نشده است. تمام دارایی‌های هوایی ایالات متحده در نظر گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/12841" target="_blank">📅 10:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12840">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lv_tjClMxaARchz8spPiXRCNswaJ823wXN-78iRDqzcfvqQYH7Ewfb0ajB7tTiUyxfEMYGuQvdWuruh2VZ5U5b6booJ9DtDeZNeqTLaAQV2Qbkq_Ot9joY9Zm8-eXwfy6KfJUtM8qTBqHAwRXFwB6pTOLSP9gUjRABDys0_2JaqTX4BY9YUehjVhqm6JXIEggOKEnLXB9C3hH5DUHjEhzaZTK-yPbJRjYKICORd9KydKPHclX9vPq16bTM4Mkf4zaVby8J6jXqc1Wa-MxEeEXxPBU96-EmAzkejn4fyKpAJZUgJ3cT3dF71-vU_DhU5GwuRj8IAmfEOfMy3b51Z6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید علی کریمی و حمایت از شاهزاده رضا پهلوی
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/12840" target="_blank">📅 10:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12839">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس: آنچه امروز جمهوری ایران دنبال می‌کند، مدیریت هوشمند تنگه هرمز است.
اعمال کنترل و ترتیبات ایران در تنگه هرمز ماهیت دائمی دارد و بی‌تردید مقطعی نیست.
ایران قصد ندارد اورانیوم غنی شده خود را به کشور ثالث منتقل کند.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/12839" target="_blank">📅 09:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12838">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رویترز: ترامپ در شرایطی به دنبال پایان دادن به جنگ با ایران است که همزمان با دو فشار متضاد مواجه شده است. از یک سو افزایش قیمت انرژی و نگرانی از تبعات اقتصادی جنگ، کاخ سفید را به سمت دستیابی به توافق سوق می‌دهد و از سوی دیگر بخشی از جمهوری‌خواهان و متحدان سیاسی ترامپ خواهان ادامه فشار نظامی و جلوگیری از هرگونه امتیازدهی به جمهوری اسلامی هستند.
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/12838" target="_blank">📅 09:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12837">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a0d910cb.mp4?token=BimHHU-2bY61dO5XgvDsykr3X1IDjspSUChz9btFELRshE02XwqVhmIENkntUaYKUU4nvLL_zUZdtuTrkn4LnyIgl7IhPBMuEq-0ToIxMmDrnl5XinHzVghltG3YXo5S13NoByC9mmW0b3y3bS-Oo0deVQHZjmUZjnLPfz5PO8QSdFLGOzNhs4Y9e1aigAT8OJUB9C-N_0SivsaJ-2IM1P-Ae8spQXqbl4a3A0GzKDHMIdU7SuwGATEItZ0nu7z-6y6gdj9Qd3O79j08tBw7KTr6Z4RWLJGSFvsu4IPQl4TkwH2FHN9eIAgv3FUeOdlEPSNZacglvUEmwYg_y2alpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a0d910cb.mp4?token=BimHHU-2bY61dO5XgvDsykr3X1IDjspSUChz9btFELRshE02XwqVhmIENkntUaYKUU4nvLL_zUZdtuTrkn4LnyIgl7IhPBMuEq-0ToIxMmDrnl5XinHzVghltG3YXo5S13NoByC9mmW0b3y3bS-Oo0deVQHZjmUZjnLPfz5PO8QSdFLGOzNhs4Y9e1aigAT8OJUB9C-N_0SivsaJ-2IM1P-Ae8spQXqbl4a3A0GzKDHMIdU7SuwGATEItZ0nu7z-6y6gdj9Qd3O79j08tBw7KTr6Z4RWLJGSFvsu4IPQl4TkwH2FHN9eIAgv3FUeOdlEPSNZacglvUEmwYg_y2alpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس: دستاوردهای ما علیه ایران قابل توجه بوده است
جی‌ دی ونس، معاون رئیس‌جمهور آمریکا: اگر به آنچه تاکنون به دست آورده‌ ایم نگاه کنید ،در صورتی که بتوانیم به یک توافق نهایی برسیم ،در حال بازگشایی تنگه هرمز هستیم.
ما پیش‌تر توان نظامی متعارف آنها( ایران) را به‌ شدت تضعیف کرده‌ ایم و در موقعیتی قرار داریم که میتوانیم برنامه هسته‌ ای‌ شان را به‌ طور قابل توجهی عقب بیندازیم،نه فقط در دوره این رئیس‌ جمهور، بلکه در بلندمدت.
این یک اتفاق بسیار، بسیار خوب برای مردم آمریکا است.
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/12837" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12836">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه مقام ایرانی به وال استریت ژورنال: تهران نگرانه که اسرائیل، آمریکا رو از مذاکرات خارج کنه
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/12836" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12835">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9915e2bfef.mp4?token=MG3B4AplDqjpc0mnYJ-AYMSb9A0Wl50Jkh1AKgCPkci_Fve86bGYH4bWBhZXo0SPBl-0JipvPl_10xyOtF0ScDdxqIP33P_83QTXV4Z2oYPcLmby6FYZd90TMn766ribbMFXFwPfij6veNpwHHPqGmEHnOPbSh3F-HEoYDjZ1mJW7wQ-JlzD3AeuJhpZeE67ml_08Hl8tQNHC3lsBSwKMb-xy0mSNrh-pEOUON6pl_fPZPsx7VG6_RdxFFMl8uz_qdrCWOKAjikAjaFqI9zB3bfvJrE8zvZhGXLtJlboXg2NmSCkHVZlw-8fjfsSXNuxdU-D5UldivbFrCgiv1-AZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9915e2bfef.mp4?token=MG3B4AplDqjpc0mnYJ-AYMSb9A0Wl50Jkh1AKgCPkci_Fve86bGYH4bWBhZXo0SPBl-0JipvPl_10xyOtF0ScDdxqIP33P_83QTXV4Z2oYPcLmby6FYZd90TMn766ribbMFXFwPfij6veNpwHHPqGmEHnOPbSh3F-HEoYDjZ1mJW7wQ-JlzD3AeuJhpZeE67ml_08Hl8tQNHC3lsBSwKMb-xy0mSNrh-pEOUON6pl_fPZPsx7VG6_RdxFFMl8uz_qdrCWOKAjikAjaFqI9zB3bfvJrE8zvZhGXLtJlboXg2NmSCkHVZlw-8fjfsSXNuxdU-D5UldivbFrCgiv1-AZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پودر شدن موشلی ۹۰ روزه شد
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/12835" target="_blank">📅 09:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12834">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">https://t.me/boost/withyashar  بوست داره میریزههههه</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12834" target="_blank">📅 00:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12833">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">https://t.me/boost/withyashar
بوست داره میریزههههه</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12833" target="_blank">📅 00:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12832">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دیکتاتور مهربون ردبول رو امشب میزنی یا فرداشب؟
👀</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/12832" target="_blank">📅 00:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12831">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan</strong></div>
<div class="tg-text">دیکتاتور مهربون
ردبول رو امشب میزنی یا فرداشب؟
👀</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/12831" target="_blank">📅 00:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12830">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پدافند اصفهان فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12830" target="_blank">📅 00:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12829">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تسنیم : یک منبع نظامی رهگیری پهپاد آمریکایی را تایید کرد
به گفته این منبع نظامی، این رهگیری در اطراف بوشهر از طریق شلیک موشک پدافندی به سمت این پهپاد انجام شد.
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/12829" target="_blank">📅 00:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12828">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">درود بر یاشار جان از جم پیام میدم حوالی ساعت 22:41 بود که فک کنم صدای فرستادن موشک یا رد شدن جت و این داستانا یهو اومد  صدای مهیب و خوبی بود @withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/12828" target="_blank">📅 00:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12827">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407ae75cd1.mp4?token=ccHXDHr9KchtTvk3ixwRm69ouqV6FOXqfxwvsfpnOd53LKSkgxxcArG1ut64RDnyW9WoNDJtJlvIKqmFDxSySaPrie7HVMX4zVF4ZDINXIFwqpYwHgRKelE7nZN3Hk4HTYgOZSQA3i-8TL3oS_sVHDCEIHgxhdGccbT85MYFITcL0ILODYw1PIFo1UVnGoOJRWsIJZ4OCuMoVGqSVpSppd_SeaFdZuNewaC8_5oluVPmKpL00JTnh6w3g2I2D5fXY5hi_El7HLeB2ckqEsQwxnVOXbM-12uL-UxvNfmIe9OVMR5JKxkN2e5U4dxvEtQG84bnktuxLRtTBr2r9hvGSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407ae75cd1.mp4?token=ccHXDHr9KchtTvk3ixwRm69ouqV6FOXqfxwvsfpnOd53LKSkgxxcArG1ut64RDnyW9WoNDJtJlvIKqmFDxSySaPrie7HVMX4zVF4ZDINXIFwqpYwHgRKelE7nZN3Hk4HTYgOZSQA3i-8TL3oS_sVHDCEIHgxhdGccbT85MYFITcL0ILODYw1PIFo1UVnGoOJRWsIJZ4OCuMoVGqSVpSppd_SeaFdZuNewaC8_5oluVPmKpL00JTnh6w3g2I2D5fXY5hi_El7HLeB2ckqEsQwxnVOXbM-12uL-UxvNfmIe9OVMR5JKxkN2e5U4dxvEtQG84bnktuxLRtTBr2r9hvGSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آنها مذاکره‌کنندگان بسیار خوبی هستند آنها زیرک‌اند اما ما همه کارت‌ها را در دست داریم، چون آنها را از نظر نظامی شکست داده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/12827" target="_blank">📅 23:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12826">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivitUi1TDf78BO3X8KRpG_77mtpibffKNhAvscB1Y5EUkO4STb3rVq8vpOQ6A1XIy5P7njR8Qbzst7vAfjntU8e9ZPdAjE8i6JeHq6FgaCnGCjbYxIrVj55qQ2djuO62LYUNOs9palhWc9WiUKlOlosu-0N2H-aA-jqTNoSjFry8d1nG3feWBHBootpZ6Pv4quw8jkpUWXg_g8-UMDPPjgfjHbBH-TH6LkzN5osBfjB2-4CvcScFVPs_rOZ7JD9D8rlPwK6fINo1N-m7LCBq6KYNm_GJzeaClbM_Tw7TWnAnwgDakREsLYvXjvQiVEIIPJvsop5vk--08mDYKn5WKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه CNN:  تصاویر ماهواره ای نشان میدهد ایران به سرعت در حال بیرون کشیدن زرادخانه موشکی عظیم خود از زیرِ زمین است
.
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/12826" target="_blank">📅 23:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12825">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ویو از کانال میلیونی ‌بیشتره، ری اکشن از کانال پوشاک زیر کمتر
😕
بد میگین ما ایرانیم چه کاری ازمون برم یاد بکنیم برات !!! خوب اسمت که نمی افته کاملا مخفیه همه پستا و ری اکشن بده دست آدم به کار بره…</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/12825" target="_blank">📅 23:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12824">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کانال‌های وابسته به محور شیعه ادعا می‌کنند که ۴ کشتی تجاری آمریکایی پس از تلاش برای عبور از تنگه هرمز بدون اجازه ایران، توسط سپاه پاسداران ایران مورد حمله قرار گرفته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/12824" target="_blank">📅 23:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12823">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فارس:  دقایقی پیش نیروهای مسلح ایران از مناطق جنوبی کشور به‌سمت اهداف مشخص موشک شلیک کردند.
بامداد امروز هم پس از تعرض دشمن یه مناطق شرقی بندرعباس پایگاه مبدأ این تجاوز مورد هدف نیروهای مسلح جمهوری اسلامی قرار گرفت.
هنوز هدف دقیق این موشک‌ها مشخص نیست اما برخی منابع از احتمال درگیری بر روی آب‌های خلیج فارس خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/12823" target="_blank">📅 23:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12822">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رسانه های عبری : گزارشهای رسمی از تبادل آتش بین ایران و آمریکا در تنگه هرمز خبر می‌دهند. @withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/12822" target="_blank">📅 23:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12821">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اتاق جنگ با یاشار : یا موسی
💥
یااااا موسیییی</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/12821" target="_blank">📅 23:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12820">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رسانه های عبری : گزارشهای رسمی از تبادل آتش بین ایران و آمریکا در تنگه هرمز خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/12820" target="_blank">📅 23:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12819">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ایلنا: شلیک اخطار نیروی دریایی به چهار شناور
نیروی دریایی در نزدیکی تنگه هرمز به ۴ فروند شناور خاطی شلیک اخطار انجام داد. این شناورها قصد عبور بدون هماهنگی از تنگه هرمز را داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/12819" target="_blank">📅 23:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12818">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رسانه های عبری : گزارش‌های اولیه: موشک‌های کروز «ابومهدی المهندس» از ایران به سمت کشتی‌های آمریکایی در منطقه تنگه هرمز شلیک شدند.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/12818" target="_blank">📅 23:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12817">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">درود بر یاشار جان از جم پیام میدم
حوالی ساعت 22:41 بود که فک کنم صدای فرستادن موشک یا رد شدن جت و این داستانا یهو اومد
صدای مهیب و خوبی بود
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/12817" target="_blank">📅 23:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12816">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتاق جنگ با شما : هرمزگان و بوشهر هم صدای انفجار میاد
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/12816" target="_blank">📅 23:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اتاق جنگ با شما :  انفجار تو علامردشت فارس  بوده
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/12815" target="_blank">📅 23:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12814">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اتاق جنگ با شما : یاشار مثل اینکه مرز بین استان فارس و بندر عباس و بوشهر رو زدن
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/12814" target="_blank">📅 23:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12813">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترور مامور فراجا در ایرانشهر
ساعتی قبل افرادی مسلح به سمت مامور انتظامی شهرستان ایرانشهر که در حال عزیمت به محل کار بود با سلاح گرم تیراندازی کردند که استوار دوم «عیسی عباسی» کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/12813" target="_blank">📅 23:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارشگر: ترامپ گفت که می‌تواند عمان را منفجر کند. آیا شما برنامه‌ای برای یک جنگ جدید با عمان دارید؟  اسکات بسنت:  فکر می‌کنم ترامپ می‌خواست بر آزادی کشتیرانی در تنگه تأکید کند. سفیر عمان به من اطمینان داد که هیچ برنامه‌ای برای عوارض‌گیری از تنگه وجود ندارد.…</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/12812" target="_blank">📅 22:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b307799edc.mp4?token=V0VIGNvJyOY94rRyD1BUBKrJXO64bAoEe0xirWq0f-rQ1NscMsVqvMrlqjm01vENW7Kz_UNOvKYM7Nz3xspXDG7H9fPExjZCgu2t-aewT6HXRKuvhaHcE3dClVy-kaaaWkGFW3pVZTPMECEZHAeHoW9BShd9W508JP6eAhhMiMC_uNQm5D8fJHbwhPCIENdxMYq78cawsPNZ57-2t7dcApBzHzMIsaAJ0opYgpkXfK6Gny-LQ7eHfskwqccv6DSPb91uwhJEzRVa1SrpHX9dWOidxFC3LzhkCsZgFzXW63rT0jKD38pwEORqlQRIK5qr5gubjLSg4KnY0cbc0HGuNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b307799edc.mp4?token=V0VIGNvJyOY94rRyD1BUBKrJXO64bAoEe0xirWq0f-rQ1NscMsVqvMrlqjm01vENW7Kz_UNOvKYM7Nz3xspXDG7H9fPExjZCgu2t-aewT6HXRKuvhaHcE3dClVy-kaaaWkGFW3pVZTPMECEZHAeHoW9BShd9W508JP6eAhhMiMC_uNQm5D8fJHbwhPCIENdxMYq78cawsPNZ57-2t7dcApBzHzMIsaAJ0opYgpkXfK6Gny-LQ7eHfskwqccv6DSPb91uwhJEzRVa1SrpHX9dWOidxFC3LzhkCsZgFzXW63rT0jKD38pwEORqlQRIK5qr5gubjLSg4KnY0cbc0HGuNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: ترامپ گفت که می‌تواند عمان را منفجر کند. آیا شما برنامه‌ای برای یک جنگ جدید با عمان دارید؟
اسکات بسنت:
فکر می‌کنم ترامپ می‌خواست بر آزادی کشتیرانی در تنگه تأکید کند.
سفیر عمان به من اطمینان داد که هیچ برنامه‌ای برای عوارض‌گیری از تنگه وجود ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/12811" target="_blank">📅 22:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12810">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اتاق جنگ با یاشار : موج مکزیکی رو میبینید چقدر زیباست ؟
😍
🌊</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/12810" target="_blank">📅 21:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12809">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ادعای سی‌ان‌ان:ترامپ در‌هر حالت  قبل از امضای تفاهم‌نامه با بنیامین نتانیاهو مشورت خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/12809" target="_blank">📅 21:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12808">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ادعای تسنیم: یک منبع نزدیک به تیم مذاکره‌کننده گفت بر خلاف ادعای برخی منابع غربی مبنی بر اینکه متن اصطلاحاً «یادداشت تفاهم» میان ایران و آمریکا نهایی شده و فقط منتظر اعلام دو طرف است، این موضوع واقعیت ندارد و هنوز متن قطعی نشده است.
وی افزود: ایران تا این لحظه به میانجی پاکستانی اعلام نهایی شدن متن را انجام نداده است.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/12808" target="_blank">📅 21:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12807">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">: NBC ادعای
آمریکا و ایران سه روز پیش تو دوحه به توافق رسیدن، ولی فعلا اعلامش نمیکنن
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/12807" target="_blank">📅 21:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12805">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efpOFPtiMne83wHxoLg2-r7LHA2W-LEqeuHlob8RqHkF-RvuOb5ASKOKX-UQMR4SG6CyyFQgMKqR0X_wbSEe46wdZyOv9nmN7y7ORSB23LvQ41DaCiTVxxV5EpB_hAuqTzvIICPYxSPtvsnkExpi6U6i221ecQqSH3zGyrLZEJ2VQ5jR9x5J0JZIGPlKPF1ccfZupJY69gaVCcW2zq0v4n0dKz9p9Kt3yOX8HbPhwmTNmNfppkxPhOb91jNTcWBzu3bW_pH6ntxITHfj9UHC327fbKnc_2mzvM33a5xLFTbYP4BrC4KS4JocWVJ6Pz6PH6EBjmtF0BKp3Y3F3a7cNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWm7edBjhgQLXE5Y-oNohcgPiL4eWmGK10mqQR_sHNBLP8CpDWUfowkOVplm0Tb1xmCRPfTWLoXbW-ce0p8QHpO4xN-JzLaAl6hlO7VNlSZV0gJ7MTDvWBMcR-itzEog7njOVadsXZXiYWxdX8yPa_4xK6EeX6K8C-Mvbb1aEVKXHm_xx-XSOnU8jNe9FxDDIeCjtzUVWytZtOXVh9BtF1A-g0FURCub8uq38GKO6s0Q2KUhcbUMcN5zi1uo_cEtPLoDr10Cp97GBXlA-b6qEfBjEkzK5XjSK5Ic9MZLrz03xNnLOm226zWLYgbfH0Prt45EPu4bv1CVkNJJ5zuGcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتاق جنگ با شما : تو ساحل انزلی ساعتی پیش یه کشتی وسط دریا یهو آتیش گرفت هی منفجر میشه ، ممکنه بار جدید مهمات از روسیه بوده باشه
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/12805" target="_blank">📅 20:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12804">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/12804" target="_blank">📅 20:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12803">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">https://www.ecolo.org/documents/documents_in_english/ramsar-natural-radioactivity/ramsar.html</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/12803" target="_blank">📅 20:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12802">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArshia</strong></div>
<div class="tg-text">آقا یاشار سلام خسته نباشی
❤️
رامسر الان صدای جنگنده اومد یدونه بود نسبت به جنگ خیلی صداش زودتر تموم شد ولی جنگنده بود
پریروزم همین صدا اومد همینقدم بود محلیا میگفتن داره میره سمت روسیه</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/12802" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12801">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">@withyashar
😃
وضعیت سیکیم خیاری</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/12801" target="_blank">📅 20:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12800">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آمریکا ۲ شرکت هواپیمایی ایران را تحریم کرد
وزیر خزانه‌داری آمریکا نوشت: دسترسی ۲ شرکت هواپیمایی ایران به نقاط فرود، سوخت‌گیری و فروش بلیت مسدود خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/12800" target="_blank">📅 18:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12799">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یک منبع اسرائیلی: رهبر ایران، مجتبی خامنه‌ای، این توافق را تأیید نکرده است، و بنابراین ترامپ نیز آن را تأیید نکرده است. قالیباف، رئیس مجلس و عراقچی، وزیر امور خارجه، حتی اگر چارچوب را پذیرفته باشند، مجاز نیستند؛ تصمیم توسط رهبر گرفته می‌شود. ما نمی‌دانیم که آیا هیچ یک از طرفین این توافق را تأیید کرده‌اند یا خیر. اختلافات هنوز هم وجود دارد، حداقل طبق آخرین به‌روزرسانی که اسرائیل دریافت کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/12799" target="_blank">📅 18:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12798">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌های رفت و آمد به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود.
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/12798" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12797">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو:  اسرائیل کنترل ۶۰٪ از نوار غزه را در دست دارد، دستور من حرکت به سمت ۷۰٪ است. با این شروع خواهیم کرد. ما در فرایندی هستیم که می‌توانیم قدرت خود را در جهات مختلف به کار بگیریم. ما همچنان باید بر حزب‌الله فشار وارد کنیم؛ در…</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/12797" target="_blank">📅 17:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12796">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900d5bba51.mp4?token=RLqhfnB8Tm-3PsdrS4lLMS5puHJ6Vp7xyfRlQVFYY1WGOICZmvHRk5dhIRm7G-a36HINc1wPrJEV9FRlB7HHBbu0Bt_3_-2iue8qH0BYhnrg4UmKq3uL8neAd9UMP_QQvKKzEKIF36NosgvmfO8aOe8WqZ2xpiI4QzqYAOYkTrm1MdE0xCbwTKzo56EJ4EaRCLRKbmLSj2yt2suCmxMnbJfdO3LoUvtIl86qj6In8Trh3NT3QDvuCSp8d9ZgJdor5UKAStrdw7GQoBXLpXaZirdTD03DZzOIPcuoOvgOT0m3whROjzAgh-WvyS6Ir0yKZ1t_XT1mcuk52QDzmC286w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900d5bba51.mp4?token=RLqhfnB8Tm-3PsdrS4lLMS5puHJ6Vp7xyfRlQVFYY1WGOICZmvHRk5dhIRm7G-a36HINc1wPrJEV9FRlB7HHBbu0Bt_3_-2iue8qH0BYhnrg4UmKq3uL8neAd9UMP_QQvKKzEKIF36NosgvmfO8aOe8WqZ2xpiI4QzqYAOYkTrm1MdE0xCbwTKzo56EJ4EaRCLRKbmLSj2yt2suCmxMnbJfdO3LoUvtIl86qj6In8Trh3NT3QDvuCSp8d9ZgJdor5UKAStrdw7GQoBXLpXaZirdTD03DZzOIPcuoOvgOT0m3whROjzAgh-WvyS6Ir0yKZ1t_XT1mcuk52QDzmC286w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
اسرائیل کنترل ۶۰٪ از نوار غزه را در دست دارد، دستور من حرکت به سمت ۷۰٪ است. با این شروع خواهیم کرد.
ما در فرایندی هستیم که می‌توانیم قدرت خود را در جهات مختلف به کار بگیریم.
ما همچنان باید بر حزب‌الله فشار وارد کنیم؛ در حال حاضر با حماس درگیر هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/12796" target="_blank">📅 17:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12795">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نتانیاهو:
ما باید ماموریت در ایران را تکمیل کنیم و من تقریباً هر روز در این مورد با ترامپ صحبت می‌کنم.
@withyashar
یاشار : من هم تقریباً زیر تمام پستهاش کامنت گذاشتم بیبی جون، فینیش د جاب</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/12795" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12794">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">روسیه: ترامپ با انتقال اورانیوم غنی‌شده ایران به مسکو موافقت نکرد
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/12794" target="_blank">📅 17:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12793">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیغام فیکی از ترامپ که از یک پیج فیک ایکس است داره میچرخه. ترامپ هیچ پیجی در شبکه ایکس یا توییتر ندارد و فقط در تروسوشال پست میگذارد. این مسئله رو دقت کنید.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/12793" target="_blank">📅 17:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12792">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ابوترابی، نماینده مجلس: آمریکا بعد از جام جهانی و انتخابات کنگره دوباره حمله می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/12792" target="_blank">📅 17:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12791">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سیتنا: تا الان تمرکز ۹۱ درصدی ترافیک اینترنت تو تهران بوده و بازگشت توزیع عادی پهنای باند، زمان‌بره.
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/12791" target="_blank">📅 17:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12790">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6oJnOG7QPcG6m8t2PqgPM5QhyV7IQq36LmiihmYOihxqR23aNNDu2wbAlAWBiAVNcynC6X8WNifo--_9hx0V5yXeLbyv9-z2grmOHN6S3VEGpSvl2sm6L_ncJRfN4qV2Jsojjrc2QR0UCKWsGvX4_XILB6XdqnnVcfILRg6db7qDq8MP7OjRYC6EjO3FeH3Ymw-HhTK62izBxqX94_UCOf2iemIwBwfWmrsYAb2RKi3yhfJTcwWA1HOv0mqP_wWgCDOoabyPowfZ18tZKdYMMco576EvxZcomUxuwWDKUsvl5mtAktTdyuh2_o34nTbg6pESlVWyfeohGrLCWtg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن پست
:
مقامات دولت ترامپ، اداره حکاکی و چاپ را تحت فشار قرار داده‌اند تا یک اسکناس ۲۵۰ دلاری با تصویر رئیس‌جمهور طراحی کند، که این اولین بار در بیش از ۱۵۰ سال گذشته است که تصویر یک فرد زنده روی پول رایج آمریکا چاپ می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/12790" target="_blank">📅 16:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12789">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل گفت که ارتش این کشور با قدرت به حملات علیه حزب‌الله ادامه خواهد داد.
نتانیاهو اضافه کرد که نیروهای اسرائیل از رودخانه لیتانی در جنوب لبنان عبور کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12789" target="_blank">📅 16:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرگزاری والا به نقل از یک مقام امنیتی اسرائیل: یکی از اهداف در بیروت یک فرمانده ارشد ایرانی بوده است
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/12788" target="_blank">📅 15:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سنتکام طی بیانیه‌ای ایران را به نقض فاحش آتش‌بس متهم کرد
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/12787" target="_blank">📅 15:10 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
