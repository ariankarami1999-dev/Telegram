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
<img src="https://cdn4.telesco.pe/file/sm34u3GX-FugpzXxNJZws_30XSj_ZCYJqvCElZwthPaVd-zLvbG-yQUz3_1gbV-yWh_2Lln7JQzHrWcdh-JS5tJbB_ueNsWTWmd1D1-xLQ2eI9cGFU_ptInRD8ck6-lk5h0D8lxkDQ1i_bXSdHAHwIk7RdrxiGhA0WspqYVdC0u-EP26RI_XWLH_ihOEgJBHWluI41VN7mc8v4qNI7cRE0CesdaRp0PIdVljHVSMYDosrEjAGMxkSFq0rU7lMYVwxWEs1f4FD9XHKZruWeuZum_-8-y2uFhhIKurg3c3c_1z_BQnW-nTSZJ-cs4irIALxSbGNu6DArus2hlPkVpO0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-14951">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تتر ۱۶۳.۵۰۰ تومان
@withyashar</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/withyashar/14951" target="_blank">📅 11:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14950">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانال ۱۲ اسرائیل: حدود ۱۰ ساعت از اعلام توافق بین واشنگتن و تهران می‌گذرد اما نتانیاهو هنوز در سکوت به سر می برد
@withyashar</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/withyashar/14950" target="_blank">📅 11:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14949">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نشست سران گروه هفت (G7) امروز در شهر اویان-له-بن فرانسه برگزار می‌شود؛ جایی که رهبران کشورهای صنعتی جهان درباره‌ی مجموعه‌ای از بحران‌های جهانی گفت‌وگو خواهند کرد.
گروه G7 یک گروه متشکل از هفت اقتصاد بزرگ جهان شامل آمریکا، بریتانیا، کانادا، فرانسه، آلمان، ایتالیا و ژاپن است که از دهه‌ی ۱۹۷۰ و پس از بحران نفتی اوپک شکل گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/withyashar/14949" target="_blank">📅 11:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14948">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ایران فعلا در تنگه هرمز پولی دریافت نخواهد کرد
ایسنا: براساس جزئیات تفاهم‌نامه، ایران تنگه هرمز را مدیریت خواهد کرد و عوارض را «در تاریخ بعدی» دریافت خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/14948" target="_blank">📅 11:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14947">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">️ترامپ به نیویورک تایمز:
«کنار آمدن با نتانیاهو فوق‌العاده دشوار است و او باید از ما بسیار سپاسگزار باشد، زیرا اگر ایران سلاح هسته‌ای داشت، اسرائیل وجود نداشت.»
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/14947" target="_blank">📅 11:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14946">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر دفاع اسرائیل: همراه با نتانیاهو سیاستی روشن را دنبال میکنم که بر اساس آن، ارتش در مناطق امنیتی در لبنان، سوریه و غزه باقی خواهد ماند
با وجود تمام فشارهای فعلی و آینده، خروج ارتش اسرائیل از لبنان را نمیپذیریم
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/14946" target="_blank">📅 10:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14945">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d30fe0e63.mp4?token=brBjXH3uOn5mhWNsSIl_BtiL-KU4HPkm7ELuOHytkrDNoR68Wo_P2lXOn3aMnt8xaT1X34D2TLWN3wiUWez6UX2LPYlt6NWuJUyHdcB7l5mi9Wztg9F5SCVBfceuBMJH-v_n5PLiLlslXC_2m3S6eP3WN84VDCyPBbv-FBLMQOgSlErLVsViw4OL5dRn8tqty_r3e07sRBbQF9fpGH3lFZmU68ri-puSZ1xNfUL1Zx9rjjrcxOC6EXnJ1ecm5b32vc7IQuwgYgNd65lsqAfMpKH45XwfS8KprHKTZRAKqX_XY-x6zCeFU53Uh0mLMqf52IGJnvxj5t7Dc2MAvGoHOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d30fe0e63.mp4?token=brBjXH3uOn5mhWNsSIl_BtiL-KU4HPkm7ELuOHytkrDNoR68Wo_P2lXOn3aMnt8xaT1X34D2TLWN3wiUWez6UX2LPYlt6NWuJUyHdcB7l5mi9Wztg9F5SCVBfceuBMJH-v_n5PLiLlslXC_2m3S6eP3WN84VDCyPBbv-FBLMQOgSlErLVsViw4OL5dRn8tqty_r3e07sRBbQF9fpGH3lFZmU68ri-puSZ1xNfUL1Zx9rjjrcxOC6EXnJ1ecm5b32vc7IQuwgYgNd65lsqAfMpKH45XwfS8KprHKTZRAKqX_XY-x6zCeFU53Uh0mLMqf52IGJnvxj5t7Dc2MAvGoHOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین شناوری که پس از اعلام توافق صلح میان ایالات متحده و جمهوری اسلامی ایران از تنگه هرمز عبور کرد، نفتکش گاز طبیعی مایع (LNG) با پرچم مالت به نام “دیشا” (Disha) است که از طرح تفکیک ترافیک دریایی ایران استفاده کرد
@withyashar</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/14945" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14944">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حمله اسرائیل به الخیام جنوب لبنان!
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/14944" target="_blank">📅 10:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14943">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کانال ۱۳ اسرائیل به‌نقل از یه مقام ارشد:
توافقی که داره صورت میگیره فاجعه‌بارترین توافق تاریخه. از نخست وزیر گرفته تا رئیس ستاد ارتش کل غیر از این فکر نمیکنه
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/14943" target="_blank">📅 10:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14942">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euvUvi7RkHL28vDif6U04MrVQMHQSeIdgR6GZDKVj9FmEzkK_AZqXAGmtyIeaRR_jaJg9yp8DpJ4yivRu-TxaGSEilqxuUpXlvB46qSj4pcqizqpDRE-YhTVMi7jPQmC1pMJv4uNAeJDZCE1V7OdcoT0IcxDJYrmyE2oPrl4ps1XRc49BrSVezYGVeoBLdtSnL2GgoKUbkHuPS7oTvTe5-bAxWTd3IEn3EP_mLXdxoUqryyMvQqyCEw8RTU0bL2NP0hvL5Xq55q43kwy1iRnJXwobIBcZvL7k9NXZV5TEpCLtg6UaGgA9FTcAQW7SW4ShgIdDWBSJ3je4pupPl6LlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق خوب، توافقی است که هیچ یک از طرفین راضی نباشند
-کتاب قدرت مذاکره جلد سوم صفحه ۲۳۶
یه توافقی بستم که هم ایران ناراضیه هم ملت ناراضی هستن هم براندازا ناراضی هستن هم آمریکا ناراضیه هم اسراییل ناراضیه
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14942" target="_blank">📅 03:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14941">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نیویورک تایمز: تهران نهایی کردن توافق را تا بعد از نیمه‌شب به وقت محلی به تعویق انداخت تا از همزمانی این لحظه تاریخی با تولد رئیس‌جمهور ترامپ در روز یکشنبه جلوگیری کند
اختلاف زمانی هفت و نیم ساعته به هر دو کشور ایران و آمریکا اجازه داد تا جدول زمانی مورد نظر خود را حفظ کنند، به طوری که ترامپ گفت توافق در روز یکشنبه نهایی شده در حالی که مقامات ایرانی تأکید داشتند که این توافق در روز بعد به پایان رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14941" target="_blank">📅 03:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14940">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ به نیویورک تایمز: نتانیاهو فرد بسیار نمک نشناسی است. او باید به شدت از ما بابت انجام این کار سپاسگزار باشد.
زیرا اگر ایران سلاح هسته‌ای داشت، اسرائیل دو ساعت هم دوام نمی‌آورد.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14940" target="_blank">📅 03:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14939">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پرزیدنت ترامپ به نیویورک تایمز گفت که در صورت شکست مذاکرات برای دستیابی به توافق هسته ای نهایی، حملات نظامی خود را علیه ایران از سر خواهد گرفت.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14939" target="_blank">📅 02:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14938">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14938" target="_blank">📅 02:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14937">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">@withyashar
khatme kalam</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14937" target="_blank">📅 02:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14936">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14936" target="_blank">📅 02:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14935">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیویورک تایمز
:  محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، و عباس عراقچی، وزیر امور خارجه، برای امضای توافق با جی‌دی ونس، معاون رئیس‌جمهور، به ژنو سفر خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14935" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14934">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هم اکنون محاصره دریایی آمریکا علیه ایران کاملا برداشته شد
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14934" target="_blank">📅 02:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14933">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14933" target="_blank">📅 02:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14932">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14932" target="_blank">📅 02:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14931">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14931" target="_blank">📅 02:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14930">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">@yasharrapfa
👻</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14930" target="_blank">📅 02:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14929">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قشم شنیده شدن صدای انفجار از سمت دریا
🚨
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14929" target="_blank">📅 02:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14928">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش های از صدای انفجار از فرودگاه مشهد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14928" target="_blank">📅 02:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14927">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">جزئیاتی از یادداشت تفاهم ایران و آمریکا
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
طبق گزارش المحور نیوز، آتش‌بس کامل در تمام مناطق و خروج اشغالگران صهیونیست از جنوب لبنان اعلام شده است.
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14927" target="_blank">📅 02:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14926">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14926" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14925">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شعار مرگ بر آمریکا دیگه کنگله
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14925" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14924">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiEIz3vFgQWhvEVIwISKR3UtdpXl4bgEzC4sY2-Bji326aO2HPtjsb_aVJvmvK2GUZQU_QqtvQ6a089FDHURfX1o_-Shb-e_AdKy0dBXDrjocX6fbhES7bz6G5FJ3tqcNRPOtsTLvPJ929hCyD7P0Q8t9w4Z_UdcH0OOWLU3wHunS_OG9J3_Auh0U3atIEekAiNPYGCCwEyE8ImCGCBEu7B7o7goCbDAXTmbZ7t_FoLQ_DE3ANIRVoOWAWRdANKtb3KC4XqJcBY9oZQcz5l8hCIv2B7Pp_vu9J25_jmYc7q9zMvHR6B5Pyy_TA0wMqFsMs73aylDvFMrF_UUIn4FYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : این توافق بزرگ، صلح و امنیت را برای سراسر منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همگی پیش از من شکست خوردند. رهبران منطقه برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آنان در دستیابی به صلحی واقعی کمک کند. با بازگشایی تنگه پس از امضای توافق در روز جمعه، به‌منظور رفع موانع مورد نظر من، نفت دوباره از هر دو سو برای منطقه و جهان جریان خواهد یافت!
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14924" target="_blank">📅 01:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14923">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش از سیریک پهپاد شلیک شد به سمت کشتی ها !
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14923" target="_blank">📅 01:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14922">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">@withyashar
⚽️</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14922" target="_blank">📅 01:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14921">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14921" target="_blank">📅 01:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14920">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جنگ تمام نمیشود بشینید و ببینید
✌🏾</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14920" target="_blank">📅 01:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ اعلام کرد: من برای شرکت در امضای توافق با ایران به ژنو خواهم رفت
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14919" target="_blank">📅 01:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14918" target="_blank">📅 01:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14917" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14916" target="_blank">📅 01:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فارس: دقایقی دیگر بیانیه رسمی دبیرخانه شورای عالی انقلاب ملی درباره توافق آتش بس منتشر خواهد شد
بر اساس این گزارش، ایران پس از حمله به ضاحیه بیروت، مذاکرات خود را لغو و آماده حمله به رژیم صهیونیستی شده بود. اما در نهایت با امتیازهای لحظه آخری که از سوی دونالد ترامپ، رئیسجمهور آمریکا ارائه شد، از جمله حفظ تمامیت ارضی لبنان و عقب نشینی اسرائیل از مرز لبنان و بازگشایی بلادرنگ محاصره،  متقاعد گردید که از انجام حمله خود صرفنظر کند.
همچنین مقرر شد نظام حقوقی تردد در آب‌های خلیج فارس با همکاری ایران و عمان  تنظیم شود.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14915" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14914">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14914" target="_blank">📅 01:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14913">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14913" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610e7fc5e5.mp4?token=Y34hxRxf18AH7y7CrqecGNucjcyRnHnaxF_ld9wYxkIJSldQw0aPOuFoHv4Lt0whX5lBffkXdcrefAYhBJGawmYFx4zyxMcUpW7fYnrBT5EsogsOYH7Ril6yVqh-2Lqu7D7mHXCWJg5pa7FFh_zfzKJdpi5PmsZTtErB43iDYOvCFWtz6ASCtGa57agXFwxdXJGC2ZAU_03hgXf5kkJY-yeR2ZToLzer6m7Kqca0OpHoHRq8DXm6IHIpcubHiwFwr-daVUOznEHtzMMecF4_Zg9kpJfpdql2-54r2oQELsKjYk2XR2HTp1SAa-_40rY2-Gt10HkaMEJz_nu7WD-fMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610e7fc5e5.mp4?token=Y34hxRxf18AH7y7CrqecGNucjcyRnHnaxF_ld9wYxkIJSldQw0aPOuFoHv4Lt0whX5lBffkXdcrefAYhBJGawmYFx4zyxMcUpW7fYnrBT5EsogsOYH7Ril6yVqh-2Lqu7D7mHXCWJg5pa7FFh_zfzKJdpi5PmsZTtErB43iDYOvCFWtz6ASCtGa57agXFwxdXJGC2ZAU_03hgXf5kkJY-yeR2ZToLzer6m7Kqca0OpHoHRq8DXm6IHIpcubHiwFwr-daVUOznEHtzMMecF4_Zg9kpJfpdql2-54r2oQELsKjYk2XR2HTp1SAa-_40rY2-Gt10HkaMEJz_nu7WD-fMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صدا و سیما:
پیروزی رو به ملت تبریک میگم
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14912" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14911">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwRZTS4Ds9dxsBRymKJ-u9Ogb4OAqWUKtu3GKBxBHkJWcqQnok00UBlhUkEQwaU5nvqW3RkKg6HghuRKeNaNG8y820h9jI4EYXNjb3ZAxPGPo4YY-mgy3-qhkt3nBJ-mM6M_oQtBmM4YJvGDrbTbQtt7cxoZmtqfoImjf7AeoZHogK5n9Gw0fFpIs5tywSUcOWPj4GicQKIjCh4lBm5QI8rhJ7lTYBEGI3nEF7OvHi9fNAOmhfq465lecmAuU9lFlvamO84e69xdPaDoB1E0J4X1SkBQ5hZ8EbUo-rIq5i58CyxQ-7bomvyV9lUPenL7N7XyHRqgfUJLDlBN71cl6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداسیما : ترامپو  وادار کردیم در همه جبهه ها جنگ رو متوقف کنه
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14911" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14910">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اتریوم داره پرواز میکنه
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14910" target="_blank">📅 01:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14909">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvBO96YT0lv2G-RgbYKQpg64k7l_yyp_v017LFiBqRKEYal7J4yIwaAO1vfldKVNzuzfL1hyyFWRBiHd2oVQ2aovaZv99FFJN9N1G64VT_DUv-ZWpcgYcyU9fQOCv10t6XIKk0yo6wqKRD8_V4S3_XKkKfEMdejEE3UoDpQLfMVqJR2vdq2cR6DtVQ1QWSSpsQcMp8A1rqOgFye55F4zT2vW843pRtiHhR4wR19AFYNg42yvZilJQE6tNKAOD5uXGzcWpz9LRIZse4i9yR25H7kx2Ql8W396HFHY3Ii-nsmeAdStE1li35yuY1S89HNMKqR6XbsKuzrmb9TI8fhuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «توافق با جمهوری اسلامی ایران اکنون نهایی شده است. به همه تبریک می‌گویم! من بدین‌وسیله به‌طور کامل مجوز بازگشایی رایگان تنگه هرمز را صادر می‌کنم و هم‌زمان، دستور رفع فوری محاصره دریایی ایالات متحده را نیز صادر می‌نمایم. ای کشتی‌های جهان، موتورهای خود را روشن کنید. بگذارید نفت جاری شود!
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14909" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14908">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14908" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14907" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چیزی‌ امظا نشده
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14906" target="_blank">📅 00:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14905">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pao7wAINXEXDJEPLCajQq2Nr_4Jk_SLhsg_M2lb9Zcbfh36jqE58zxsJCpPJ9jTnEwU6_h7fSxfYQe5U_UMEiBYeWZ2IgBwttN2sXdAq-EnvS_VJi_XTkg_vuakjaX9lagbdOHaFbT555BCEGdddq8HVv1fj7q_mESjUwfhCLywzOlq2EjuyMYwdELWfNN9Zuv2j8mJfwXBVA2uMAQUOCbFj9uNTqUBrv8d_hB17Q20QWZkD_Xu6yq23gPCdfH_8q9oQG06q_5EUGAZumZwblNJ6TF6u9nHTrD4_fmJi5EK6OSgS1IWutVJoxiooM2EZzq3S-n17oPxTvmH2lgVIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر :توافق با امریکا انجام شد
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14905" target="_blank">📅 00:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14904">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نخست وزیر پاکستان: پس از مذاکرات فشرده، با کمال خرسندی اعلام می‌کنیم که توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است. هر دو طرف توقف فوری و دائمی عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، را اعلام کرده‌اند.
مراسم رسمی امضای توافق‌نامه روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14904" target="_blank">📅 00:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14903">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: «بعداً مسائل هسته‌ای را حل می‌کنیم» و افزود که «هیچ عجله‌ای نیست» و می‌توان ظرف یک یا دو ماه آینده به آن پرداخت
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14903" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14902">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: بزودی یک بیانیه خواهم داد
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14902" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14901">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبر تسنیم فیکه مثل خودش
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14901" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14900">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🤣
🤣</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14900" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14898">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ می‌گوید توافق با ایران قریب‌الوقوع است، اما تهران تاکنون آن را تأیید نکرده است  رئیس‌جمهور در مصاحبه‌ای می‌گوید که قصد دارد به زودی بیانیه‌ای صادر کند و تأیید کند که ایالات متحده با ایران به توافق رسیده است @withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14898" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14897">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbGdbpIdmNAxtpvL4bqIdEd9zRg_7oRPG73_C5k9etdXcuCAhHnhkNfIJLbnDDbAjXpARwTwZd59vtvGFeXKXAvnHCjVrn_Tdco8BZdkT6UUmsFq0OojgxpiIGtPEdZiuQc0JOoQNiyEjFvXPw60k2jBuFBfG1hMeUuCkVna2cI6G8UYxepLeyiT2siOyyQD-TTFvIT748N79g-awL0iuouJkdiWDQZy-2kh56jAX40ukmHIklXUbwN3D4fmTfuHD6WbGEsM0nE2bfNehnQQGurChf418BeLQ1jtrD3LzceDaVXPHkFlJPxqn2l9PEEWg9F_kyUFmB9EuJIAv4lkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید توافق با ایران قریب‌الوقوع است، اما تهران تاکنون آن را تأیید نکرده است
رئیس‌جمهور در مصاحبه‌ای می‌گوید که قصد دارد به زودی بیانیه‌ای صادر کند و تأیید کند که ایالات متحده با ایران به توافق رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14897" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14896">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ به وال استریت ژورنال گفت که قصد دارد به زودی بیانیه‌ای صادر کند و در آن توافق آمریکا با ایران را تأیید کند
@withyashar
ترامپ کله پوک: من علاقه‌ای به تغییر رژیم در ایران ندارم</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14896" target="_blank">📅 00:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14895">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">توییت وزیر کشور پاکستان: الله اکبر
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14895" target="_blank">📅 00:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14894">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">میگن توافق امضا شد
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14894" target="_blank">📅 00:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14893">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سی‌ان‌ان: مذاکره کنندگان قطری همین حالا تو تهران حضور دارن تا با هماهنگی امریکا توافق رو به سرانجام برسونند و از نهایی شدن روند مذاکرات اطمینان کسب کنند
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14893" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14892">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حسین پاک، خبرنگار صداوسیما در لبنان:
امشب به صورت همزمان ایران، یمن و حزب‌الله به حمله اسرائیل به ضاحیه پاسخ می‌دهند
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14892" target="_blank">📅 00:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14891">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljiuv7y4z8ZABWTl3BNhovBJElW5H39WqXTRuFDPj0Azk7M9uyLv8JueLkdscl9XUmmRZh9EDes-dbOmcqzb1vxF1vBYIUNZJaiDvYW1DrMJ9wl_0RElSsCKPxGobg311sAQwtoHayBBR0l2fwjzkTAxcEBTOAGBRP0J1ev9ShGeAYAG8CWbGhRgFHvvnoC0XcNvGYDQP5tQrYIepDberj4EEy8-yAuRkDuijWXjkf_3IGhzlWauud5AetuFxaxOqnFWYdY0SKyQfxTh34kSwmd0Tfr6XQdhTWm2CB7PTdHme3XCWclAk66LHxFHLvx4mexZZzCDXoyTw--GCJ3zCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد اومد بازی‌رو از‌ نزدیک دید
😂
بازی امروز آلمان و کوراسائو (Curaçao) در جام جهانی ۲۰۲۶ با نتیجه
۷ بر ۱ به سود آلمان
به پایان رسید.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14891" target="_blank">📅 00:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14890">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ در تروث : ویکتوریا کوتس از بنیاد هریتیج واقعاً فوق‌العاده است! او مثل کمتر کسی این موضوع را درک می‌کند. ویکتوریا، متشکرم. ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز خیلی زود برای تجارت باز خواهد شد!!! رئیس جمهور دی‌جی‌تی @withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14890" target="_blank">📅 00:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14889">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ در تروث : ویکتوریا کوتس از بنیاد هریتیج واقعاً فوق‌العاده است! او مثل کمتر کسی این موضوع را درک می‌کند. ویکتوریا، متشکرم. ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز خیلی زود برای تجارت باز خواهد شد!!! رئیس جمهور دی‌جی‌تی
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14889" target="_blank">📅 00:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14888">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کانال ۱۲ اسرائیل: دقایقی پیش ترامپ و نتانیاهو گفت‌وگو کردن. ترامپ، نتانیاهو رو در جریان پیشرفت‌ها برای امضای توافق با جمهوری اسلامی قرار داد؛ توافقی که ممکنه حتی از امشب امضا بشه.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14888" target="_blank">📅 00:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14887">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نیویورک‌تایمز: قطر در تلاشه تا اختلافات باقی مونده میان آمریکا و جمهوری اسلامی رو حل کنه تا همین امشب توافق امضا بشه.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14887" target="_blank">📅 00:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14886">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7-tUM7mibVjDBS6zSVNck-0v1Jg36mYUx_hLUkzVET3aF4iHTs1SR4dRa3ifQHSJrnIveohByGN0sEhx6HqhoyhUm7phav85dRqPQc-Y_CDUabWUi6L1pUxmq1rE-wbxRE9k9jlaYSljyQKHI-p-KFmnkdApbySurExIRvJKlLHVB-cRxN3sV_zHQFTrggaa9KV6qgn4dryczbLxlMg_oUm7tgHrv_sVmTvHOQuq5tmZvOKakOG0dyufJxDvRw9NhWfJKXb4iyqiWVKsaXlyaZEIfRPWU6p9NpdPIDW5nzkfiKBd7JBfMkQOtiVUDnL_iAakEzC0ziOK4smsXHD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : جک رید، سناتور رود آیلند، گفته توافقی که الان بستیم از توافق زمان اوباما هم بدتره
به نظر من یا داره عمداً دروغ میگه یا اصلاً نمی‌فهمه موضوع چیه
توافق اوباما عملاً راه رو برای رسیدن ایران به سلاح هسته‌ای باز می‌کرد و کلی پول هم بهشون می‌رسوند؛
یکی از بدترین و احمقانه‌ترین توافق‌هایی که آمریکا تا حالا بسته بود
اما توافقی که ما الان انجام دادیم دقیقاً برعکسه؛ مثل یه دیوار محکم جلوی هرگونه دسترسی ایران به سلاح هسته‌ای رو می‌گیره
مقایسه کردن این دو تا اصلاً منطقی نیست. جک رید باید پاسخگو باشه
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14886" target="_blank">📅 00:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14885">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/14885" target="_blank">📅 23:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14884">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏سناتور لیندسی گراهام به انتقاد از ترامپ‌برای سرزنش بی‌بی:
«آمریکا در شرایط مشابه چه می‌کرد؟»
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14884" target="_blank">📅 23:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14883">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کارشناس شبکه افق:   امام شهید ما چونش را برای اورانیوم گذاشت ولی امروز مسئولین جلسه می‌گذارند و می‌گویند اورانیوم به درد نمی‌خورد/ کسانی که امروز به ترامپ امتیاز می‌دهند بدانند که حتی آن‌ها را هم ممکن است آمریکا ترور کند @withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14883" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14882">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کارشناس شبکه افق:
امام شهید ما چونش را برای اورانیوم گذاشت ولی امروز مسئولین جلسه می‌گذارند و می‌گویند اورانیوم به درد نمی‌خورد/ کسانی که امروز به ترامپ امتیاز می‌دهند بدانند که حتی آن‌ها را هم ممکن است آمریکا ترور کند
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14882" target="_blank">📅 23:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14881">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8M2X_xWSXQEKIXpKcexQfRPTbtdDN0EgYUkOEchEo55bZam5kG0RfoHm48lQJrr3GO55BNN9AiPfjXMHZduf1bl-zN5Zn8IcutfMtQ0eDD73ttqgd78G0r4eK4Fy82SGG8G7aLfQewLq8WT1bY1G4KDL2duRZ2CAA0uLAzONxn8A99EFpS0yQWB48H-irAqv1YXOqZDRzKr8BxoHopv5hLGJiAI4SGF0PHj3tsN0Q0PfkJD1o4aExLeVr6VQfQPOYy89yKUjSEvW44mFbIJEI8-IsYPvNv8c8Pmzuvpg67cQJUrOXYMIFikqwV1v2QCc7Lx6-XFVc_pjRqFJ-ug-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی: فرمان صادر شد؛ لانچرها آماده پرتاب میشوند
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14881" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14880">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تیم جمهوری اسلامی با ویزا ساعتی عازم لس آنجلس شد برای بازی با نیوزلند
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14880" target="_blank">📅 23:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14879">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وای نت: ممکن است ترامپ در حال آماده‌سازی برای برداشتن فوری محاصره دریایی آمریکا بر بنادر ایران باشد تا از هرگونه حمله ایرانی به اسرائیل جلوگیری کند
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14879" target="_blank">📅 23:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14878">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07020c75c7.mp4?token=BmGQzST8aqPOXOWHuP2Lnau-Ne9xm6dj5kOtB_s2QPKkmND8175LVumyJySfiocpOf-8XJAg2VvYq26hvtNzs7XGf5LJyenIAoURxUaVtGqA_q_szqu1c82FDp_FfOVrmrTllNxMEbmdBFEf4fWSWR7j0PstKQqN5kUq3uA21Zp3lju8N6OV6xXk0fC4IgdWyOjv2YSs8jwiwNzr38KX7v4CQFbhrbblPpymbVgh2x7q3lFP8Tr7zyMnHtyVO8vwg2On2TVtcTLYVwGs73NuJJiW_5OVQQf25hjtio1BbHKbnb92b1yI2ZatK1Jb5SmsLccxTOfjOCG02YInkwKW-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07020c75c7.mp4?token=BmGQzST8aqPOXOWHuP2Lnau-Ne9xm6dj5kOtB_s2QPKkmND8175LVumyJySfiocpOf-8XJAg2VvYq26hvtNzs7XGf5LJyenIAoURxUaVtGqA_q_szqu1c82FDp_FfOVrmrTllNxMEbmdBFEf4fWSWR7j0PstKQqN5kUq3uA21Zp3lju8N6OV6xXk0fC4IgdWyOjv2YSs8jwiwNzr38KX7v4CQFbhrbblPpymbVgh2x7q3lFP8Tr7zyMnHtyVO8vwg2On2TVtcTLYVwGs73NuJJiW_5OVQQf25hjtio1BbHKbnb92b1yI2ZatK1Jb5SmsLccxTOfjOCG02YInkwKW-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما:
امشب اسرائیل به شدت بمباران خواهدشد.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14878" target="_blank">📅 23:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14877">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">راشن تودی: ورود اضطراری «جی دی ونس» به کاخ سفید همزمان با اوج‌گیری تنش‌ها در منطقه!
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14877" target="_blank">📅 23:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14876">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کابینه اسرائیل: اگر ایران حمله کند، ما نیز حمله خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14876" target="_blank">📅 23:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14875">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارشهایی از شما مبنی بر مشاهده موشک در آسمان
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14875" target="_blank">📅 23:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14874">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسرائیل بی‌اعتنا به ترامپ عملیات خود در  لبنان را ادامه می‌دهد ، سه انفجار مهیب در شهرک الطیری در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14874" target="_blank">📅 23:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14873">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ادعای رسانه‌های عبری:
تحرکات موشکی سپاه پاسداران در یزد، شیراز و اصفهان درحال مشاهده است
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14873" target="_blank">📅 22:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14872">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e1cd002a5.mp4?token=MJjNIXefaRhhsHsEv2RXbv7QYOfbhQC1J1LzWy6OLmHcyzfYixWPz7xMvFBIuMAQvUbus0YzmiLBspSXzvj_tsYObrKywzsdS_CoOM2kWlU1OwOY_JlMmCGciZBCFZ165Y3AfnqfZuDaZp2V_FYJmkvHe6SIx2nXBdPG2R0lZLXeu4Sc6_YkOmL16Jw_Nab5OlIg3ZLVcEi1wk77hxX9GOzB_3eIXS8yEJI0EQQFiJGw2H1WFRnVEqMDIevnbEyYib-JBkHRaN9mKh1i-coQE48tnb5EzrUD54NjcZVmGIGrOleSc36HBjwI49sxSWvgDnXQQ90jr4oS40BySmhKkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e1cd002a5.mp4?token=MJjNIXefaRhhsHsEv2RXbv7QYOfbhQC1J1LzWy6OLmHcyzfYixWPz7xMvFBIuMAQvUbus0YzmiLBspSXzvj_tsYObrKywzsdS_CoOM2kWlU1OwOY_JlMmCGciZBCFZ165Y3AfnqfZuDaZp2V_FYJmkvHe6SIx2nXBdPG2R0lZLXeu4Sc6_YkOmL16Jw_Nab5OlIg3ZLVcEi1wk77hxX9GOzB_3eIXS8yEJI0EQQFiJGw2H1WFRnVEqMDIevnbEyYib-JBkHRaN9mKh1i-coQE48tnb5EzrUD54NjcZVmGIGrOleSc36HBjwI49sxSWvgDnXQQ90jr4oS40BySmhKkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست : ما در تمام این مدت کنترل تنگه‌ها را در اختیار داشته‌ایم.
‏مجری : اما شما در حال مذاکره با ایران هستید تا تنگه هرمز را دوباره بازگشایی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14872" target="_blank">📅 22:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14871">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هاآرتص: نتانیاهو به ترامپ
نه
گفت
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14871" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14870">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خالیباف خطاب به اسرائیل بچرخ تا به بچرخیم
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14870" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14868">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👻</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14868" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14867">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هیچ نوتام جدیدی درباره محدودیت پروازی صادر نشده است
مجید اخوان، سخنگوی سازمان هواپیمایی کشوری در گفتگو با خبرنگار مهر درباره برخی اخبار منتشرشده در فضای مجازی مبنی بر صدور نوتام جدید برای محدودیت پروازی در فضای هوایی کشور، اظهار کرد: هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14867" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14866">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تسنیم گفت ایران با هشدار NOTAM پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است. این تصمیم در پی شرایط موجود اتخاذ شده است. @withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14866" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14865">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2_rgmbvDN6gSf9fn9NULv0ebkGsaMZKybxj4Iu1BK_WDiA_P2myk6Pon-ImHAqgpvepOwHYWw1BvQ65i_v3CpWjPGhpQlWeCxLxdzcgzHt5n8tZx_tsAh4VOqTVYN0tvb1f40ruSl3MdXClj6E4RHAvfa0pCshx5I7WrcnQvJ8MzuLFuwJkJkz859-gy8wZbmEktwSm3-4CLEPcN_It-jl7yX3cJRw_a3AriEpTVsIM9DCgUJ8wfhqAw5GVZ5FENA1GtI1QPUoyncl_wE5TFt2Tzc_QVyA6L-Fhb2hlml9r59GOADX2L77Cc1W6zPdnidJ-MIza9e_0ljvzOekF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ از بالا پشت بام : آخرین پرواز در تهران نشست
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14865" target="_blank">📅 22:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14864">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تسنیم گفت ایران با هشدار NOTAM پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است. این تصمیم در پی شرایط موجود اتخاذ شده است.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14864" target="_blank">📅 22:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14863">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ea26e8e3.mp4?token=kMeinwkKXgMVwOzUEZgHBzkLthLMV5zErmL2V7UX-iJhfksHi_UOecqfqiEztQTGoN6_B97IlNQG9xTsZHtCaaUY3XCEM181LHD7iJtHgUmCWAncTMW89uerqfayLU_7bwKgUZU1AvATWSksIaeJCaRO5bXVHE6Mu8r6scebr_95hqJIWhr67G7nk7IP1KO_b9x95eWI7xQzAW62M-HST4RjxAn-mBeGDZmBgINW-jbNewXlqh6ub44O623CZfnHmq5URmLm48KJLEG0D_jBuL8hR4vdYoFWTtHO0I96WhryUGYMGmpJrkzlw2ejRWA69vyoNP_PPbOBrWti8Y9u6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ea26e8e3.mp4?token=kMeinwkKXgMVwOzUEZgHBzkLthLMV5zErmL2V7UX-iJhfksHi_UOecqfqiEztQTGoN6_B97IlNQG9xTsZHtCaaUY3XCEM181LHD7iJtHgUmCWAncTMW89uerqfayLU_7bwKgUZU1AvATWSksIaeJCaRO5bXVHE6Mu8r6scebr_95hqJIWhr67G7nk7IP1KO_b9x95eWI7xQzAW62M-HST4RjxAn-mBeGDZmBgINW-jbNewXlqh6ub44O623CZfnHmq5URmLm48KJLEG0D_jBuL8hR4vdYoFWTtHO0I96WhryUGYMGmpJrkzlw2ejRWA69vyoNP_PPbOBrWti8Y9u6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل اختلال در سامانه‌های موقعیت‌یابی GPS را در شدیدترین حالت قرمز قرار داد برای دفاع از خود و ایران نیز این روند را هم اکنون شروع کرده و در حال شدت بخشیدن است.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14863" target="_blank">📅 22:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14862">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گروهک هکری حنظله وابسته به حکومت : امشب سپاه قطعا میزنه
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14862" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14861">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4hHS1BZfmFzCr3q4zjGXpLJfht-sQjve_w0LK-5KT2qn0tNGiYAh0c__ssuGxnQszSBZYPEA5H86AszZ_luwzWjzIIptQYLMiAwJVG9xs7OG7vn0-ntL-7wYGeWMMHrzJ5HMKaq-fFfu9lsSEkC--nmC-eLYCgV7yjsKL3HP7V4TX4UBOHlKWZPrsMZdbM_X4bkqaQKkxt10_YTuF7dXV0Vf5onu4Kd2SsWNUE3hEhYiwcwj6ggomPs42Yj1xWIErPGeLkizJ2EB84bkPf40EaFbILpFE9dbGjHYYx8Sbc6NxPb6Hl9trLBRj0TurQQ9U33cCqhyhBClqQKcDXm8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا دقایقی دیگر آسمان ایران کلیر میشود. یک پرواز در تهران میشیند و یک پرواز از مرز غربی خارج میشود.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14861" target="_blank">📅 22:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14860">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ارسالی : دوست پسرم سربازه میگفت که لانچر اینا اماده کردن
🤷🏻‍♀️
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14860" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14859">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دیده بان اتاق جنگ : اطراف سایت موشکی شهرک مسکونی ویلاشهرنجف آباد  تحرکات زیادی دیده میشه ورود ماشین های سنگین به پارک‌‌ کوهستانی پشت سایت
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14859" target="_blank">📅 21:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14858">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14858" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14857">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یدیعوت آحارونوت: ایران خبر درخواست ترامپ برای عدم حمله به اسرائیل در ازای مزایا در توافق را رد کرده و گفته است که به اسرائیل پاسخ خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14857" target="_blank">📅 21:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14856">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🥊
UFC Freedom 250 + مراسم ۲۵۰ سالگی آمریکا (White House Event)
UFC فریدم ۲۵۰ همزمان با جشن ۲۵۰ سالگی آمریکا و برنامه‌های کاخ سفید برگزار می‌شود و به وقت تهران از حدود ساعت
۰۲:۳۰ بامداد روز دوشنبه
با بخش‌های قبل از رویداد و برنامه‌های طرفداری شروع می‌شود، سپس بخش
پریلمز (مبارزات مقدماتی)
از حدود ساعت
۰۴:۳۰ تا ۰۸:۳۰ صبح
پخش می‌شود که شامل مبارزات سبک‌تر و مبارزان کم‌تجربه‌تر است و نقش آماده‌سازی فضای اصلی را دارد، بعد از آن بخش
مین‌کارت (کارت اصلی)
از حدود ساعت
۰۸:۳۰ صبح تا حدود ۱۲:۳۰ ظهر
ادامه پیدا می‌کند که شامل مبارزات مهم‌تر و ستاره‌های یو‌اف‌سی است و در نهایت مهم‌ترین مبارزه شب یعنی
مین ایونت (مبارزه اصلی)
معمولاً نزدیک ساعت
۱۰:۳۰ تا ۱۱:۳۰ صبح به وقت تهران
برگزار می‌شود و کل این رویداد به‌صورت زنده از طریق سرویس
پارامونت پلاس
پخش می‌شود و در آمریکا بخشی از آن هم از شبکه
سی‌بی‌اس
پخش خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14856" target="_blank">📅 21:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14855">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb472a4ecd.mp4?token=KmMikQmG2TQEh6opMfKwrd06jPNiXF-J0GFX9UyCWeHywlgPbo8Jk3VVfER81EZ7PDeap7GYcU4z2HQD7Sd9wvTDN1ls24d-XdksKIVLyFWmPRMSDUM2UQd1TqZz2n63Fm0TQb0rl_4N5NrSlDX6qpOO8Oc1WRoQonrXXP7dYKNLVz5eDe_6AEuF6adZMNcpJ1RIJgnqkpzTX-CYu51JByZW4HyLAE5W0ZMTp6XmSfIYHmjVFM7dXXmK192Z_YsAkbFGYiViMG2YxKpwyKUDnsQKX1TVjzIfQJIGV8ixvw5HFW_Bp6hcCnE7ednhB7pS5V4ySj88TwGCyIovpFCOPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb472a4ecd.mp4?token=KmMikQmG2TQEh6opMfKwrd06jPNiXF-J0GFX9UyCWeHywlgPbo8Jk3VVfER81EZ7PDeap7GYcU4z2HQD7Sd9wvTDN1ls24d-XdksKIVLyFWmPRMSDUM2UQd1TqZz2n63Fm0TQb0rl_4N5NrSlDX6qpOO8Oc1WRoQonrXXP7dYKNLVz5eDe_6AEuF6adZMNcpJ1RIJgnqkpzTX-CYu51JByZW4HyLAE5W0ZMTp6XmSfIYHmjVFM7dXXmK192Z_YsAkbFGYiViMG2YxKpwyKUDnsQKX1TVjzIfQJIGV8ixvw5HFW_Bp6hcCnE7ednhB7pS5V4ySj88TwGCyIovpFCOPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو پدر و  دختری،  احمد ایراندوست(غول برره)، وسط این هیر و ویر‌…
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14855" target="_blank">📅 21:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14854">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قالیباف : بازی پلیس خوب و پلیس بد قدیمی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14854" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14853">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خضریان، نماینده مجلس:
ارتباط واتساپی عراقچی با ویتکاف باید کاملاً قطع شود!
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14853" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14852">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">زیرنویس شبکه خبر :
پاسخ به حمله اسرائیل قطعی است.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14852" target="_blank">📅 21:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14851">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">لارنس نورمن خبرنگار وال استریت ژورنال:
در عرض دو هفته، ترامپ از این موضع که «لبنان از موضوع ایران جداست» به این موضع رسیده که «لبنان مرتبط است اما اسرائیل حق پاسخگویی دارد» و بعد به این موضع که «لبنان مرتبط است ولی من فکر نمی‌کنم اسرائیل حق پاسخگویی داشته باشد چون باید توافق را منعقد کنیم»
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14851" target="_blank">📅 20:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14850">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ادعای ترامپ در گفتگو با اکسیوس:
این توافق به نفع اسرائیل خواهد بود، زیرا مانع از دستیابی ایران به سلاح هسته‌ای شده و این کشور را ملزم به رهاسازی مواد هسته‌ای می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14850" target="_blank">📅 20:41 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
