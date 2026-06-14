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
<img src="https://cdn4.telesco.pe/file/ibnf0F9-tf6r2wrUf8JY-Sr5svkjz_sBvxtmdvzkiEQ60wtDTR9u6zqMHOIx_CuPmvZmFNUkBM-IJF4MuSc_TXpNIylZ4WXVQtR7wGJIvTFXrcclxDGLKwjqKpFeQq0ANz0CSR_99UUCysWvTJCJ54zoAbERpwM3NqUuM1FXQmsvKre0OLmXw7yvyaepOv0vht88u3VzddDQ6bfR_Zrw5ywuc3paHMPdrhStciXsYFnGx0bIK706qsP2BekQKI-AEeH323FT6punZ9IOPRYMnesySnv2HQYe2xuXWm0IoE_QPXqjFNg0_vnzPDi_UQAZcaAcVHzxcmXUN19Evyp9kw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 03:12:55</div>
<hr>

<div class="tg-post" id="msg-14939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پرزیدنت ترامپ به نیویورک تایمز گفت که در صورت شکست مذاکرات برای دستیابی به توافق هسته ای نهایی، حملات نظامی خود را علیه ایران از سر خواهد گرفت.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/withyashar/14939" target="_blank">📅 02:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/withyashar/14938" target="_blank">📅 02:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">@withyashar
khatme kalam</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/withyashar/14937" target="_blank">📅 02:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/withyashar/14936" target="_blank">📅 02:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نیویورک تایمز
:  محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، و عباس عراقچی، وزیر امور خارجه، برای امضای توافق با جی‌دی ونس، معاون رئیس‌جمهور، به ژنو سفر خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/withyashar/14935" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هم اکنون محاصره دریایی آمریکا علیه ایران کاملا برداشته شد
@withyashar</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/withyashar/14934" target="_blank">📅 02:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/withyashar/14933" target="_blank">📅 02:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/withyashar/14932" target="_blank">📅 02:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/withyashar/14931" target="_blank">📅 02:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">@yasharrapfa
👻</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/withyashar/14930" target="_blank">📅 02:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قشم شنیده شدن صدای انفجار از سمت دریا
🚨
@withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/14929" target="_blank">📅 02:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش های از صدای انفجار از فرودگاه مشهد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/14928" target="_blank">📅 02:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جزئیاتی از یادداشت تفاهم ایران و آمریکا
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
طبق گزارش المحور نیوز، آتش‌بس کامل در تمام مناطق و خروج اشغالگران صهیونیست از جنوب لبنان اعلام شده است.
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/14927" target="_blank">📅 02:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/withyashar/14926" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شعار مرگ بر آمریکا دیگه کنگله
@withyashar</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/withyashar/14925" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiEIz3vFgQWhvEVIwISKR3UtdpXl4bgEzC4sY2-Bji326aO2HPtjsb_aVJvmvK2GUZQU_QqtvQ6a089FDHURfX1o_-Shb-e_AdKy0dBXDrjocX6fbhES7bz6G5FJ3tqcNRPOtsTLvPJ929hCyD7P0Q8t9w4Z_UdcH0OOWLU3wHunS_OG9J3_Auh0U3atIEekAiNPYGCCwEyE8ImCGCBEu7B7o7goCbDAXTmbZ7t_FoLQ_DE3ANIRVoOWAWRdANKtb3KC4XqJcBY9oZQcz5l8hCIv2B7Pp_vu9J25_jmYc7q9zMvHR6B5Pyy_TA0wMqFsMs73aylDvFMrF_UUIn4FYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : این توافق بزرگ، صلح و امنیت را برای سراسر منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همگی پیش از من شکست خوردند. رهبران منطقه برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آنان در دستیابی به صلحی واقعی کمک کند. با بازگشایی تنگه پس از امضای توافق در روز جمعه، به‌منظور رفع موانع مورد نظر من، نفت دوباره از هر دو سو برای منطقه و جهان جریان خواهد یافت!
@withyashar</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/withyashar/14924" target="_blank">📅 01:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش از سیریک پهپاد شلیک شد به سمت کشتی ها !
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/withyashar/14923" target="_blank">📅 01:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">@withyashar
⚽️</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/14922" target="_blank">📅 01:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/14921" target="_blank">📅 01:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جنگ تمام نمیشود بشینید و ببینید
✌🏾</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/14920" target="_blank">📅 01:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ اعلام کرد: من برای شرکت در امضای توافق با ایران به ژنو خواهم رفت
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/14919" target="_blank">📅 01:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/14918" target="_blank">📅 01:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14917">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/14917" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14916">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/14916" target="_blank">📅 01:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14915">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فارس: دقایقی دیگر بیانیه رسمی دبیرخانه شورای عالی انقلاب ملی درباره توافق آتش بس منتشر خواهد شد
بر اساس این گزارش، ایران پس از حمله به ضاحیه بیروت، مذاکرات خود را لغو و آماده حمله به رژیم صهیونیستی شده بود. اما در نهایت با امتیازهای لحظه آخری که از سوی دونالد ترامپ، رئیسجمهور آمریکا ارائه شد، از جمله حفظ تمامیت ارضی لبنان و عقب نشینی اسرائیل از مرز لبنان و بازگشایی بلادرنگ محاصره،  متقاعد گردید که از انجام حمله خود صرفنظر کند.
همچنین مقرر شد نظام حقوقی تردد در آب‌های خلیج فارس با همکاری ایران و عمان  تنظیم شود.
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/14915" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14914">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/14914" target="_blank">📅 01:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14913">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/14913" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14912">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/14912" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14911">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwRZTS4Ds9dxsBRymKJ-u9Ogb4OAqWUKtu3GKBxBHkJWcqQnok00UBlhUkEQwaU5nvqW3RkKg6HghuRKeNaNG8y820h9jI4EYXNjb3ZAxPGPo4YY-mgy3-qhkt3nBJ-mM6M_oQtBmM4YJvGDrbTbQtt7cxoZmtqfoImjf7AeoZHogK5n9Gw0fFpIs5tywSUcOWPj4GicQKIjCh4lBm5QI8rhJ7lTYBEGI3nEF7OvHi9fNAOmhfq465lecmAuU9lFlvamO84e69xdPaDoB1E0J4X1SkBQ5hZ8EbUo-rIq5i58CyxQ-7bomvyV9lUPenL7N7XyHRqgfUJLDlBN71cl6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداسیما : ترامپو  وادار کردیم در همه جبهه ها جنگ رو متوقف کنه
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/14911" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14910">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتریوم داره پرواز میکنه
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/14910" target="_blank">📅 01:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14909">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvBO96YT0lv2G-RgbYKQpg64k7l_yyp_v017LFiBqRKEYal7J4yIwaAO1vfldKVNzuzfL1hyyFWRBiHd2oVQ2aovaZv99FFJN9N1G64VT_DUv-ZWpcgYcyU9fQOCv10t6XIKk0yo6wqKRD8_V4S3_XKkKfEMdejEE3UoDpQLfMVqJR2vdq2cR6DtVQ1QWSSpsQcMp8A1rqOgFye55F4zT2vW843pRtiHhR4wR19AFYNg42yvZilJQE6tNKAOD5uXGzcWpz9LRIZse4i9yR25H7kx2Ql8W396HFHY3Ii-nsmeAdStE1li35yuY1S89HNMKqR6XbsKuzrmb9TI8fhuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «توافق با جمهوری اسلامی ایران اکنون نهایی شده است. به همه تبریک می‌گویم! من بدین‌وسیله به‌طور کامل مجوز بازگشایی رایگان تنگه هرمز را صادر می‌کنم و هم‌زمان، دستور رفع فوری محاصره دریایی ایالات متحده را نیز صادر می‌نمایم. ای کشتی‌های جهان، موتورهای خود را روشن کنید. بگذارید نفت جاری شود!
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/14909" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14908">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/14908" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14907">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/14907" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14906">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چیزی‌ امظا نشده
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/14906" target="_blank">📅 00:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14905">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pao7wAINXEXDJEPLCajQq2Nr_4Jk_SLhsg_M2lb9Zcbfh36jqE58zxsJCpPJ9jTnEwU6_h7fSxfYQe5U_UMEiBYeWZ2IgBwttN2sXdAq-EnvS_VJi_XTkg_vuakjaX9lagbdOHaFbT555BCEGdddq8HVv1fj7q_mESjUwfhCLywzOlq2EjuyMYwdELWfNN9Zuv2j8mJfwXBVA2uMAQUOCbFj9uNTqUBrv8d_hB17Q20QWZkD_Xu6yq23gPCdfH_8q9oQG06q_5EUGAZumZwblNJ6TF6u9nHTrD4_fmJi5EK6OSgS1IWutVJoxiooM2EZzq3S-n17oPxTvmH2lgVIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر :توافق با امریکا انجام شد
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/14905" target="_blank">📅 00:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14904">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نخست وزیر پاکستان: پس از مذاکرات فشرده، با کمال خرسندی اعلام می‌کنیم که توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است. هر دو طرف توقف فوری و دائمی عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، را اعلام کرده‌اند.
مراسم رسمی امضای توافق‌نامه روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/14904" target="_blank">📅 00:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14903">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ: «بعداً مسائل هسته‌ای را حل می‌کنیم» و افزود که «هیچ عجله‌ای نیست» و می‌توان ظرف یک یا دو ماه آینده به آن پرداخت
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/14903" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14902">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ: بزودی یک بیانیه خواهم داد
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/14902" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14901">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبر تسنیم فیکه مثل خودش
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/14901" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14900">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🤣
🤣</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/14900" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14898">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ می‌گوید توافق با ایران قریب‌الوقوع است، اما تهران تاکنون آن را تأیید نکرده است  رئیس‌جمهور در مصاحبه‌ای می‌گوید که قصد دارد به زودی بیانیه‌ای صادر کند و تأیید کند که ایالات متحده با ایران به توافق رسیده است @withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/14898" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14897">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmXfIga44BPQk3uP480fbBqy27Iflkq16ilV0_zuYrVWNS86xPY8hO8g4kgfR7hqgogFb-AmygqfVK3jDSbZtICMr8daOaRomejZ11_JRu6ShdpYLtFN9aYe7yZulCSI5DY-SzSWKHrcC5xp2zToLgfyiyM7Slivgm6LZ98lgwjzx-t-4ra_fHpTgDB_Txix_GH09S-xf1xpl_vjWeSbFQJPnxTQogxP5R5S4G7bEQfUzFXOR3WKpLafh0COt-YZ51MitkmPa22u-uUaRRSGi4H_iP5XMJtB0whOmarNjaTHHgbO9Su9Y8jBpFmUEATSHMiRk-2dpns3Am54SwPwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید توافق با ایران قریب‌الوقوع است، اما تهران تاکنون آن را تأیید نکرده است
رئیس‌جمهور در مصاحبه‌ای می‌گوید که قصد دارد به زودی بیانیه‌ای صادر کند و تأیید کند که ایالات متحده با ایران به توافق رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/14897" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14896">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ به وال استریت ژورنال گفت که قصد دارد به زودی بیانیه‌ای صادر کند و در آن توافق آمریکا با ایران را تأیید کند
@withyashar
ترامپ کله پوک: من علاقه‌ای به تغییر رژیم در ایران ندارم</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/14896" target="_blank">📅 00:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14895">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">توییت وزیر کشور پاکستان: الله اکبر
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/14895" target="_blank">📅 00:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14894">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">میگن توافق امضا شد
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/14894" target="_blank">📅 00:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14893">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سی‌ان‌ان: مذاکره کنندگان قطری همین حالا تو تهران حضور دارن تا با هماهنگی امریکا توافق رو به سرانجام برسونند و از نهایی شدن روند مذاکرات اطمینان کسب کنند
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/14893" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14892">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حسین پاک، خبرنگار صداوسیما در لبنان:
امشب به صورت همزمان ایران، یمن و حزب‌الله به حمله اسرائیل به ضاحیه پاسخ می‌دهند
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/14892" target="_blank">📅 00:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14891">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7rJzAJEft5DmZE3UrTRik5FFpKP0d9UdqXDxPaNMQ1nyWmbOJER6pHKZowG5udQPkb35NSaX7ODHLBbVlPA34Bus_lg5TLJ6u3FtS6PJlAsk9ZDTdeVpXZalGUhU2J0dhmqMehx07-IU1tmunMjf9DxaSuuVnS1QDcmLajGEO74VyJZcOL8jCh4yReicGkf4AsjIjL7A3llXHUgSPgVUsoumo_2QL-okyCDx6pBSp9MqWTH7FF7-TKnxa_qsLFSpM2buUmyeYC2OHND4Zb5MmWIuWQJn3nDo250Bbc_2_9WdlHWTX4gLBOiLlaHClkaXKCihEFLt8V_wyH7zWAk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد اومد بازی‌رو از‌ نزدیک دید
😂
بازی امروز آلمان و کوراسائو (Curaçao) در جام جهانی ۲۰۲۶ با نتیجه
۷ بر ۱ به سود آلمان
به پایان رسید.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/14891" target="_blank">📅 00:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14890">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ در تروث : ویکتوریا کوتس از بنیاد هریتیج واقعاً فوق‌العاده است! او مثل کمتر کسی این موضوع را درک می‌کند. ویکتوریا، متشکرم. ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز خیلی زود برای تجارت باز خواهد شد!!! رئیس جمهور دی‌جی‌تی @withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/14890" target="_blank">📅 00:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14889">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ در تروث : ویکتوریا کوتس از بنیاد هریتیج واقعاً فوق‌العاده است! او مثل کمتر کسی این موضوع را درک می‌کند. ویکتوریا، متشکرم. ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز خیلی زود برای تجارت باز خواهد شد!!! رئیس جمهور دی‌جی‌تی
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/14889" target="_blank">📅 00:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14888">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال ۱۲ اسرائیل: دقایقی پیش ترامپ و نتانیاهو گفت‌وگو کردن. ترامپ، نتانیاهو رو در جریان پیشرفت‌ها برای امضای توافق با جمهوری اسلامی قرار داد؛ توافقی که ممکنه حتی از امشب امضا بشه.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/14888" target="_blank">📅 00:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14887">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیویورک‌تایمز: قطر در تلاشه تا اختلافات باقی مونده میان آمریکا و جمهوری اسلامی رو حل کنه تا همین امشب توافق امضا بشه.
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/14887" target="_blank">📅 00:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14886">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuwmwKFCVMNtFZdGrJmk1UQ76IneR1QkCAq7Y7l3B9XkJqExa1Fq03DGzop63oqFQY6I7943T0CABeihAKODcUhsU-0qMtVjJ9tQTpnFGa7_ySV9xoN98QLM3kbEPoSVu6BtkzXYg8eMUQaECn3T0BmmdFpPvE-rXocMq6KGsbgljxd8xIw_8RUi8yTER43bC3Sd6MBntBLnLLrJ2qzleahQgVYEZfzJ65fyyIZyl9ZIcQRI6LS2qB4ruxlFhF5j8hQ_TKZY6Fg5eG-UJVQSSy8Feu3IxjU39LzZ3GhjanTmoDYSpf_zMjxFnNHSS7GAOZs2VL84iXJc6rq0Emu_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : جک رید، سناتور رود آیلند، گفته توافقی که الان بستیم از توافق زمان اوباما هم بدتره
به نظر من یا داره عمداً دروغ میگه یا اصلاً نمی‌فهمه موضوع چیه
توافق اوباما عملاً راه رو برای رسیدن ایران به سلاح هسته‌ای باز می‌کرد و کلی پول هم بهشون می‌رسوند؛
یکی از بدترین و احمقانه‌ترین توافق‌هایی که آمریکا تا حالا بسته بود
اما توافقی که ما الان انجام دادیم دقیقاً برعکسه؛ مثل یه دیوار محکم جلوی هرگونه دسترسی ایران به سلاح هسته‌ای رو می‌گیره
مقایسه کردن این دو تا اصلاً منطقی نیست. جک رید باید پاسخگو باشه
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/14886" target="_blank">📅 00:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14885">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/14885" target="_blank">📅 23:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14884">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏سناتور لیندسی گراهام به انتقاد از ترامپ‌برای سرزنش بی‌بی:
«آمریکا در شرایط مشابه چه می‌کرد؟»
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14884" target="_blank">📅 23:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14883">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کارشناس شبکه افق:   امام شهید ما چونش را برای اورانیوم گذاشت ولی امروز مسئولین جلسه می‌گذارند و می‌گویند اورانیوم به درد نمی‌خورد/ کسانی که امروز به ترامپ امتیاز می‌دهند بدانند که حتی آن‌ها را هم ممکن است آمریکا ترور کند @withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/14883" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14882">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کارشناس شبکه افق:
امام شهید ما چونش را برای اورانیوم گذاشت ولی امروز مسئولین جلسه می‌گذارند و می‌گویند اورانیوم به درد نمی‌خورد/ کسانی که امروز به ترامپ امتیاز می‌دهند بدانند که حتی آن‌ها را هم ممکن است آمریکا ترور کند
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/14882" target="_blank">📅 23:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14881">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q87h9trelWbs8HwI1AxW9pcHiP8Y-C7pTY2lgNvQsZ8yAzTuBEEknr3wmzQ7H7xIkSQaBD1sGPNxqFVt_svYVH6NBHSUOc9DvsidPzfg5P_8-v4wcH9ahEZEBYWKpgj4k7VNs6SD4_BpssDxX0E9f78tbfla-CRlX73MZkZhKbelwU_2oJmsDTOrjpBf2soj_ao5SCaJkH32btXbf5QkSFm-A_mYuPIKjtrRxzg7YIKTxOQgXkyLGv8wYqQWofnadtZ0Ho4AvJBJcGfzcyaWU77Za_MPUOKLTaruu-PyVKviKppw9p7TK2DewUsqVXvocIBqPWw79vwEe1rBvOVPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی: فرمان صادر شد؛ لانچرها آماده پرتاب میشوند
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/14881" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14880">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تیم جمهوری اسلامی با ویزا ساعتی عازم لس آنجلس شد برای بازی با نیوزلند
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/14880" target="_blank">📅 23:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14879">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وای نت: ممکن است ترامپ در حال آماده‌سازی برای برداشتن فوری محاصره دریایی آمریکا بر بنادر ایران باشد تا از هرگونه حمله ایرانی به اسرائیل جلوگیری کند
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/14879" target="_blank">📅 23:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14878">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07020c75c7.mp4?token=NeyYFpfV0xcNQVedXPhnBUjTww7A3m0VRmcdjCTYJ6sNUwARx3d3jBpG982QDTn3ttSX8zHazQRmgxhkIWVE-wUyrV-Q_1dw7TKmxJ-PkUbp0A3IFj1HhOq1k6959lbfno6X6R2CasivtqJthexI56QYwBP3Vkw0PqgAx2UPs3fkrX9DwBNdFF2-vEP2_qI23GAkyDyxfKPYUbtg6iuJEfdHpsFDVDCKw-z6gOXfhuJ1_OvI5LE9qWhiWb12AQYCAXaznhrV-WcAlt8QoLt2fHHxTl4kMnAXcHUxeMkkVItqaxaiJWupC60pQOVB2MoEZgCmbHMjdp-4_2F2p6f5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07020c75c7.mp4?token=NeyYFpfV0xcNQVedXPhnBUjTww7A3m0VRmcdjCTYJ6sNUwARx3d3jBpG982QDTn3ttSX8zHazQRmgxhkIWVE-wUyrV-Q_1dw7TKmxJ-PkUbp0A3IFj1HhOq1k6959lbfno6X6R2CasivtqJthexI56QYwBP3Vkw0PqgAx2UPs3fkrX9DwBNdFF2-vEP2_qI23GAkyDyxfKPYUbtg6iuJEfdHpsFDVDCKw-z6gOXfhuJ1_OvI5LE9qWhiWb12AQYCAXaznhrV-WcAlt8QoLt2fHHxTl4kMnAXcHUxeMkkVItqaxaiJWupC60pQOVB2MoEZgCmbHMjdp-4_2F2p6f5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما:
امشب اسرائیل به شدت بمباران خواهدشد.
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/14878" target="_blank">📅 23:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14877">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">راشن تودی: ورود اضطراری «جی دی ونس» به کاخ سفید همزمان با اوج‌گیری تنش‌ها در منطقه!
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14877" target="_blank">📅 23:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14876">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کابینه اسرائیل: اگر ایران حمله کند، ما نیز حمله خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14876" target="_blank">📅 23:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14875">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارشهایی از شما مبنی بر مشاهده موشک در آسمان
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14875" target="_blank">📅 23:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14874">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اسرائیل بی‌اعتنا به ترامپ عملیات خود در  لبنان را ادامه می‌دهد ، سه انفجار مهیب در شهرک الطیری در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14874" target="_blank">📅 23:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14873">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ادعای رسانه‌های عبری:
تحرکات موشکی سپاه پاسداران در یزد، شیراز و اصفهان درحال مشاهده است
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14873" target="_blank">📅 22:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14872">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e1cd002a5.mp4?token=vwI4p_TMemc_3M_m_BDHI96mKLvyd8ECQ24VrsTOTN77MCuqr5a1Ne7cxEHPF37TpbBHgWAA-XJbEH_GqUGPPEz-5wqDjlH4lwX9-a2qoZFnl2m8im3ANUjvFkUZNhbyGWVCvii_xsZz9UqzsXCxMED3efOcpeUOlrGvMedb17Br6g9dccmPjDJ71yK2glKw0JWO6AuryxrxC_7gGyzoRtgszJgAI587FV0umNkQItkdyT72cHN5WobacLw-R0JsLHhWyJIfgpumq4pphE0Ht844jetwce58oAawQ_jXf9bmg9uucho_oYLBAKJzbnoNa7OYg6NEQxsHvZPVRjcjKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e1cd002a5.mp4?token=vwI4p_TMemc_3M_m_BDHI96mKLvyd8ECQ24VrsTOTN77MCuqr5a1Ne7cxEHPF37TpbBHgWAA-XJbEH_GqUGPPEz-5wqDjlH4lwX9-a2qoZFnl2m8im3ANUjvFkUZNhbyGWVCvii_xsZz9UqzsXCxMED3efOcpeUOlrGvMedb17Br6g9dccmPjDJ71yK2glKw0JWO6AuryxrxC_7gGyzoRtgszJgAI587FV0umNkQItkdyT72cHN5WobacLw-R0JsLHhWyJIfgpumq4pphE0Ht844jetwce58oAawQ_jXf9bmg9uucho_oYLBAKJzbnoNa7OYg6NEQxsHvZPVRjcjKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست : ما در تمام این مدت کنترل تنگه‌ها را در اختیار داشته‌ایم.
‏مجری : اما شما در حال مذاکره با ایران هستید تا تنگه هرمز را دوباره بازگشایی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14872" target="_blank">📅 22:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14871">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هاآرتص: نتانیاهو به ترامپ
نه
گفت
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14871" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14870">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خالیباف خطاب به اسرائیل بچرخ تا به بچرخیم
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14870" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14868">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👻</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14868" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14867">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هیچ نوتام جدیدی درباره محدودیت پروازی صادر نشده است
مجید اخوان، سخنگوی سازمان هواپیمایی کشوری در گفتگو با خبرنگار مهر درباره برخی اخبار منتشرشده در فضای مجازی مبنی بر صدور نوتام جدید برای محدودیت پروازی در فضای هوایی کشور، اظهار کرد: هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14867" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14866">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تسنیم گفت ایران با هشدار NOTAM پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است. این تصمیم در پی شرایط موجود اتخاذ شده است. @withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14866" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14865">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLKr4ONChqRiTRauDKkBWd-Xvc2IojQFkT45jSCP_4nuiNOnfWf_5URxKvgGPsE2Lknt_NCG2YgIdjKygRBTikoGddNwPwHuSPbqwk4Lkoj8Iz9IP2rCiqU0gKT4dpgnRUNDUstaaxE9Btf1ORolcLMWZJCq86VHE8JaKfbJ-bzurvY2A-sQTG81bcnzqVRRVoODQNrVd1W2Gh7U1uEC3-1S65KN_BtIqE24rWt4dRF37yNmImxXWXihZt-NzzKCtDuLpoWqYW46mKIPsM4Cfj48Ig61enO9Ifx-oDIP1W-L6_TNKCniilM16NwvsWlDPyuZ1nDjCdDu9jwOlCClaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ از بالا پشت بام : آخرین پرواز در تهران نشست
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14865" target="_blank">📅 22:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14864">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تسنیم گفت ایران با هشدار NOTAM پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است. این تصمیم در پی شرایط موجود اتخاذ شده است.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14864" target="_blank">📅 22:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14863">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ea26e8e3.mp4?token=cJI8570MsIVYL08T7k9YCgQ5ojFI29VJopNBB097U3yTshQWKplb9iwnGC1-haS5r1ijig8cIPLqxHxAJLrzotLPdBZcjhKyQYdFNMWpqqp1U6TzCYKwy9Oy2dWttHRblueAYT9TPrJe66rvgGsU1OricXmr6gn7yRr-ygVgigq8EmRLoX9kUR_muUDfWaYqYAWvMv_APIe6ICZ4cfx-9UFnH6_VBTLaaF0yO4W2kBR4tZKT8yUjtXAeaZLdsKotiNE_DbGDkLCKzaXVSenSEl1e6htvedIkMAZzMtawtE3Vyu9vSpPohwCP4sL6oatU6jkGg5y_8XpbnCN9REr1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ea26e8e3.mp4?token=cJI8570MsIVYL08T7k9YCgQ5ojFI29VJopNBB097U3yTshQWKplb9iwnGC1-haS5r1ijig8cIPLqxHxAJLrzotLPdBZcjhKyQYdFNMWpqqp1U6TzCYKwy9Oy2dWttHRblueAYT9TPrJe66rvgGsU1OricXmr6gn7yRr-ygVgigq8EmRLoX9kUR_muUDfWaYqYAWvMv_APIe6ICZ4cfx-9UFnH6_VBTLaaF0yO4W2kBR4tZKT8yUjtXAeaZLdsKotiNE_DbGDkLCKzaXVSenSEl1e6htvedIkMAZzMtawtE3Vyu9vSpPohwCP4sL6oatU6jkGg5y_8XpbnCN9REr1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل اختلال در سامانه‌های موقعیت‌یابی GPS را در شدیدترین حالت قرمز قرار داد برای دفاع از خود و ایران نیز این روند را هم اکنون شروع کرده و در حال شدت بخشیدن است.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14863" target="_blank">📅 22:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14862">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گروهک هکری حنظله وابسته به حکومت : امشب سپاه قطعا میزنه
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14862" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14861">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4hrzZ4LxzQTJoeSFP1xQUltM21WoWmsmVXaXdwIEiZfGJ_mZonHun6aGCXG9tlZm2Y_uiUz3hkUxSubfg0sTjW42WU8QAm-bTjXyn7tXwfWeFmwOXLjZQiaPeuOjOOw_FOqrzUY5RxZ-ShPcjlufBf5F6cU0A40LJ3hZfvLjP_iem7yyWkUF2I2QTmQplDTQSUq8iR0sEcQFK2e2d2Fs_CsQ-bTlIT6kqj_g0Faq5XnGG4huwUWnHRuppmTfMkMTdyffgUn7gIbPntXNgVPUhbY8uGG2D1STQyvsTzUX0kS4mMi55vRKfAa0nmCNq1moxC9xTLyARZy151embXBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا دقایقی دیگر آسمان ایران کلیر میشود. یک پرواز در تهران میشیند و یک پرواز از مرز غربی خارج میشود.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14861" target="_blank">📅 22:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14860">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ارسالی : دوست پسرم سربازه میگفت که لانچر اینا اماده کردن
🤷🏻‍♀️
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14860" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14859">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیده بان اتاق جنگ : اطراف سایت موشکی شهرک مسکونی ویلاشهرنجف آباد  تحرکات زیادی دیده میشه ورود ماشین های سنگین به پارک‌‌ کوهستانی پشت سایت
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14859" target="_blank">📅 21:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14858">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14858" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14857">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یدیعوت آحارونوت: ایران خبر درخواست ترامپ برای عدم حمله به اسرائیل در ازای مزایا در توافق را رد کرده و گفته است که به اسرائیل پاسخ خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14857" target="_blank">📅 21:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14856">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14856" target="_blank">📅 21:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14855">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb472a4ecd.mp4?token=uvkSeu2sOf6H8x9BF5JuUOBOFRJj1xRhEuoONjn2uyj6aCUSXkYEtlNOGQS9C0BTXyZ1MAiT6hVlLVHaWXrHoq8RSoCuyRqH4_OU7osG8Kjs6W6TnunOKJaSTDXIjnyRe9w1UWl9Tm85cwX3vFHECI9dfRoN7lUB7o7AcisJHBDlLyFjZcqydGs3524omq1Y_aj73sPWM5eS_xt3E6ktIDge6y2tQ7LahqkDQEVbcSuvHzbBOhP24w7017gRIsKFeizgPxlExsvbzLa5LQffkEKzQ9-ttOl7RYNIT26kUKxOZE8z4BwLPxgGxSSET-65m9Fn5gw5Pk97ZvGl3fMM-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb472a4ecd.mp4?token=uvkSeu2sOf6H8x9BF5JuUOBOFRJj1xRhEuoONjn2uyj6aCUSXkYEtlNOGQS9C0BTXyZ1MAiT6hVlLVHaWXrHoq8RSoCuyRqH4_OU7osG8Kjs6W6TnunOKJaSTDXIjnyRe9w1UWl9Tm85cwX3vFHECI9dfRoN7lUB7o7AcisJHBDlLyFjZcqydGs3524omq1Y_aj73sPWM5eS_xt3E6ktIDge6y2tQ7LahqkDQEVbcSuvHzbBOhP24w7017gRIsKFeizgPxlExsvbzLa5LQffkEKzQ9-ttOl7RYNIT26kUKxOZE8z4BwLPxgGxSSET-65m9Fn5gw5Pk97ZvGl3fMM-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو پدر و  دختری،  احمد ایراندوست(غول برره)، وسط این هیر و ویر‌…
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14855" target="_blank">📅 21:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14854">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قالیباف : بازی پلیس خوب و پلیس بد قدیمی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14854" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14853">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خضریان، نماینده مجلس:
ارتباط واتساپی عراقچی با ویتکاف باید کاملاً قطع شود!
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14853" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14852">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">زیرنویس شبکه خبر :
پاسخ به حمله اسرائیل قطعی است.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14852" target="_blank">📅 21:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14851">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">لارنس نورمن خبرنگار وال استریت ژورنال:
در عرض دو هفته، ترامپ از این موضع که «لبنان از موضوع ایران جداست» به این موضع رسیده که «لبنان مرتبط است اما اسرائیل حق پاسخگویی دارد» و بعد به این موضع که «لبنان مرتبط است ولی من فکر نمی‌کنم اسرائیل حق پاسخگویی داشته باشد چون باید توافق را منعقد کنیم»
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14851" target="_blank">📅 20:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14850">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ادعای ترامپ در گفتگو با اکسیوس:
این توافق به نفع اسرائیل خواهد بود، زیرا مانع از دستیابی ایران به سلاح هسته‌ای شده و این کشور را ملزم به رهاسازی مواد هسته‌ای می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14850" target="_blank">📅 20:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14849">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یدیعوت آحارونوت: کابینه امنیتی اسرائیل امشب تو یه مکان مخفی تشکیل جلسه میدن
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14849" target="_blank">📅 20:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14847">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">https://t.me/withyashar/s/5</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14847" target="_blank">📅 20:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14846">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ به پوتین اعلام کرد توافق پایان جنگ با ایران تقریبا کامل شده. پوتین هم از پیشرفت این موضوع ابراز رضایت کرد
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14846" target="_blank">📅 20:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14845">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فرمانده قرارگاه خاتم الانبیا: فرزندان ملت در نیروهای مسلح «دست به ماشه» آماده شلیک به قلب دشمن هستند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14845" target="_blank">📅 20:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14844">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس: پاسخ به حمله امروز اسرائیل توسط جبهه مقاومت قطعی است
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14844" target="_blank">📅 20:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14843">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:
توافق با ایران از راه دور امضا خواهد شد، سپس امضای حضوری آن ممکن است یک هفته بعد در اروپا انجام شود
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14843" target="_blank">📅 20:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14842">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بن‌گویر خطاب به نتانیاهو: قوی باش، نترس
@withyashar
🥥
🥥</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/14842" target="_blank">📅 20:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14841">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ به باراک راوید گفت: چرا بی‌بی (نتانیاهو) باید یک حمله‌ی لعنتی انجام می‌داد؟ من خیلی عصبانی شدم. به او گفتم.
او اصلاً هیچ قضاوت لعنتی ندارد. من این را به او گفتم.
اگر توافق امشب امضا شود، فوراً دستور لغو محاصره دریایی ایران را خواهم داد.
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/14841" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14840">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ در گفتگو با فاکس نیوز اعلام کرد که از ایران خواهد خواست که به حملات اسرائیل علیه حزب الله پاسخ ندهد. ترامپ همچنین اعلام کرد که توافق با ایران ظرف ۲-۳ ساعت آینده به صورت الکترونیکی امضا خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14840" target="_blank">📅 19:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14839">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: از ایران می‌خوام موشک به اسرائیل شلیک نکنه. این توافق در ساعات آینده امضا خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/14839" target="_blank">📅 19:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14838">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صابرین نیوز تایید کرد :
برکناری سعید جلیلی از شعام و جایگزینی باقری کنی با وی
@withyashar
یاشار : پوست اندازی رژیم  ادامه ‌داره</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/14838" target="_blank">📅 19:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14837">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ به باراک راوید از اکسیوس گفت:
قرار بود امروز صبح توافق را امضا کنیم، اما حمله اسرائیل به بیروت آن را به تأخیر انداخت.
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14837" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
