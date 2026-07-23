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
<img src="https://cdn4.telesco.pe/file/kCat4hp4X8SibgNgSZm4boPvNKWrcga-qN_PotTX_zRRI0e58PyPf9buS2iBV55ohbTa0Auq8T0ntWmPBD5iQV_I__OVm2BP3h0POV9DlPYHUkdHSpX23tAMZ9Pu4vDbcFGDtkgvkaHF7KelWVtw3ih8tav6kBnK0IaC-8n23f4_MA4qt9FypNW7hND0ShSLP0TjVSxfL7uRJkxvCobUsR2TL3kIB3ppU2j-Vv08ZtzNreWpwTaP0NEesx7uagd9sJoLnJytW0RzGZxwcstbcrAKSF337d70mYiPP1TFpuu5ApNYsdhENUAYB_un1Nk1UohkGSMgEHqV4hzdkCreLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 425K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 01:27:42</div>
<hr>

<div class="tg-post" id="msg-19505">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">برمیگردم
😉
من جنگامو کردم که اومدم اتاق جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/withyashar/19505" target="_blank">📅 01:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19504">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awBvn2izt9i7LImIVjRbNUdM060hqXkPQKuH3g2nFAjQ0ym_4xizOdshs8sNpLTA5B8BSJD7EShvHdhgm8dq8ci-lcfTZEoTUK6LI_UFsVveMzxrExsL-GHk82USYHIydlMQTxPnltOf_f_7x3xmQ1gOGPKmfEG0FO_mbvxsTnv1VJhs-hizRzfRUj4yxSgjPF8hVdl7uPFTB1_Yhr5cJs1UUYOl8IZoXsylttTBri5j6JBq7M2e1cchsN-eXR11GCeKSvKEUsXtRDHUkWTlO3EIpbZhA83Au4G8ZfBDFYmB44sSJ6BsjTw4nYazktZF2kuFLjr0Ftifn7eSWS0dIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : سرطان
حتما تا اخر ببینید و نظرتون رو کامنت کنید میخونم
کارای اداری یادتون نره مخصوصا اد تو استوری و ریشیر
https://www.instagram.com/reel/DbJowDnR54h/?igsh=MW0yMnB5cG5pa2FyNQ==</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/19504" target="_blank">📅 01:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19503">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گزارش انفجار های شدید و پیاپی در تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/19503" target="_blank">📅 01:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19502">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پرتاب موشک‌های کروز ضدکشتی به سمت تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/19502" target="_blank">📅 00:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19501">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نیویورک تایمز:نخست‌وزیر عراق، در جریان سفر خود به تهران، پیشنهادی را ارائه کرده بود مبنی بر برقراری آتش‌بس بین ایران و ایالات متحده
@WarRoom</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/19501" target="_blank">📅 00:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19500">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ایران به پاکستان هشدار داده است:درصورت وقوع هرگونه حمله تروریستی علیه ایران، با تمام توان و قدرت خود دست به اقدام تلافی‌جویانه خواهد زد
@WarRoom</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/19500" target="_blank">📅 00:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19499">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کانال ۱۳ عبری: نهادهای اطلاعاتی غرب بر این باورند که ممکن است ایران آغازگر اقدام علیه اسرائیل باشد
@WarRoom</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/19499" target="_blank">📅 00:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19498">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd98bed83.mp4?token=SKJzKF2cSXaU9Oa0tdTSIuCB2__0kConMySSkPHGDvCtVYYdynuSd3JTjlRw5Mk1o_ISfOQwZHK_0QEl6GjGdGg3OeKkzh0QJHitJ4VaXLXWTYvYKuWXni7gPTSw9xN5X37pxd-qcdS8QJJb5eJ4dCByaAWFSrLu9sAVWblZBEtBFd_0sbBZ53vjkenNsQIPJnxvt92lpNILWFhzA68Q5sIVqzCyciCwM_I7VvShDDZss0u2peCewmt5JozLEOBDU6SrawBpBA9yuyZxk0IhQkeRxWGHeB4A-E7IIvoCJ2w5J_-fDSe12UX54lJ-JmRxEorwX5O_uOnwGXkVsHPHrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd98bed83.mp4?token=SKJzKF2cSXaU9Oa0tdTSIuCB2__0kConMySSkPHGDvCtVYYdynuSd3JTjlRw5Mk1o_ISfOQwZHK_0QEl6GjGdGg3OeKkzh0QJHitJ4VaXLXWTYvYKuWXni7gPTSw9xN5X37pxd-qcdS8QJJb5eJ4dCByaAWFSrLu9sAVWblZBEtBFd_0sbBZ53vjkenNsQIPJnxvt92lpNILWFhzA68Q5sIVqzCyciCwM_I7VvShDDZss0u2peCewmt5JozLEOBDU6SrawBpBA9yuyZxk0IhQkeRxWGHeB4A-E7IIvoCJ2w5J_-fDSe12UX54lJ-JmRxEorwX5O_uOnwGXkVsHPHrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ده‌ها هواپیمای باری نیروی هوایی ایالات متحده (سی-۱۷ و دیگر هواپیماهای سنگین) امروز از پایگاه‌های اروپایی به خاورمیانه پرواز می‌کنند.
این یک "پل هوایی" تمام عیار است که بعد از جنگ۴۰روزه دوباره فعال شده.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/19498" target="_blank">📅 00:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19497">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رسانه های عراقی : در حال حاضر، هواپیماهای جنگنده آمریکایی بر فراز عراق پرواز می‌کنند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/19497" target="_blank">📅 00:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19496">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارشهای مبنی بر دو موشک آمریکایی در نزدیکی روستای مسن در جزیره قشم اصابت کردند.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19496" target="_blank">📅 00:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19495">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19495" target="_blank">📅 00:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19494">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19494" target="_blank">📅 00:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19493">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نیویورک پست : روز چهارشنبه، یک حمله دیگر از سوی ایران توانست سامانه‌های پدافند هوایی آمریکا را نفوذ کرده و به یک انبار سلاح در نزدیکی همان پایگاهی اصابت کند که سه سرباز آمریکایی در آن در اردن کشته شدند. این حمله منجر به انفجار شد و در نتیجه، یک "ابر قارچ" شکل گرفت.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19493" target="_blank">📅 00:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19492">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مقامات ایران آخرین پیشنهاد ارائه شده از سوی میانجی‌ها رو هم قبول نکردن.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19492" target="_blank">📅 23:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19491">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Tether = 194,850 Toman
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19491" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19490">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آلارم حمله موشکی روی موبایل های کویت اومد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19490" target="_blank">📅 23:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19489">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">از اهواز ۳ موشک با صدای مهیب زدن سمت کویت
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19489" target="_blank">📅 23:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19488">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbfb1bbbe.mp4?token=c2BtzziZlCzzVKhclTNgazGV1zSFXDoltgH7QVblMDTEpf5-Bj0su9T-dD4ef-ynNbjJDM4f8juRxdjTCfiMhKS91BRCaEL8pnq3CuxTOhlKNXDHf3-XzxhCGPEBxG_Lb3RZ4bvzZGAbK4JziCUzEAogxdTn9M8Abo53IpwBignNSVG6BHhyaf-NwAFRke9Hpm12tlvEbVy6t5sx4hOYfWonAULLUMKzphDUFQuyRC8unNRt1dqpLt6TXKsq3R7erUX4fQ5JDf4blfLMltDzjA4-xkQ9bAyg_MJR0NF0FIC-3dUP34b5cDWT7diwR6jPyoQhr38f0DBDATWK86owkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbfb1bbbe.mp4?token=c2BtzziZlCzzVKhclTNgazGV1zSFXDoltgH7QVblMDTEpf5-Bj0su9T-dD4ef-ynNbjJDM4f8juRxdjTCfiMhKS91BRCaEL8pnq3CuxTOhlKNXDHf3-XzxhCGPEBxG_Lb3RZ4bvzZGAbK4JziCUzEAogxdTn9M8Abo53IpwBignNSVG6BHhyaf-NwAFRke9Hpm12tlvEbVy6t5sx4hOYfWonAULLUMKzphDUFQuyRC8unNRt1dqpLt6TXKsq3R7erUX4fQ5JDf4blfLMltDzjA4-xkQ9bAyg_MJR0NF0FIC-3dUP34b5cDWT7diwR6jPyoQhr38f0DBDATWK86owkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون کیش
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19488" target="_blank">📅 23:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19487">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ: ایران دیگر ارتش ندارد، فقط افرادی باهوش و آقای ماکرون(رئیس جمهور فرانسه) را دارد، اما همچنان سطح مشخصی از توانایی‌ها را حفظ کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19487" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19486">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07325a864.mp4?token=QXZB32y0jut_AaNYRxrzIGiFLyDFX8MBr6F1ZU9XoF15zaH5eR2MKj0wl6PjnGdfHxBET0mCx5JF-nUb0GlK2z4c0NSjMsmxmYSgu5H10HSCqhHYdgMe7aULOYC-VEnng05N_C5vK50oTxPciGd17a1HUJpN_2jIybe7UahcgAmq8YsS28G8gROFEgrdXcXgjLSJUxt2wQhXVxy0HwGx4BnpaFWUwagwwrYk0Ovz7o8i1gn791M4fGDQmVARVCG38sAlvtX-Zn_vwBhhaxF6wO2MKHHK1w_kqhtD34sGMx6gR3BRorgA84SS9RFi7WG4o6tX3-7f3XaiuCuLVXK2Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07325a864.mp4?token=QXZB32y0jut_AaNYRxrzIGiFLyDFX8MBr6F1ZU9XoF15zaH5eR2MKj0wl6PjnGdfHxBET0mCx5JF-nUb0GlK2z4c0NSjMsmxmYSgu5H10HSCqhHYdgMe7aULOYC-VEnng05N_C5vK50oTxPciGd17a1HUJpN_2jIybe7UahcgAmq8YsS28G8gROFEgrdXcXgjLSJUxt2wQhXVxy0HwGx4BnpaFWUwagwwrYk0Ovz7o8i1gn791M4fGDQmVARVCG38sAlvtX-Zn_vwBhhaxF6wO2MKHHK1w_kqhtD34sGMx6gR3BRorgA84SS9RFi7WG4o6tX3-7f3XaiuCuLVXK2Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ،: «
ما در برابر جمهوری اسلامی ایران خیلی خوب عمل می‌کنیم، ما فوق‌العاده خوب عمل می‌کنیم
»
«آنها دوست دارند کاری انجام دهند، اما من می‌گویم که هنوز آماده نیستند.»
«آنها به چیزهای بیشتری از این دست نیاز دارند. آنها نیات شومی دارند.»
«جنگ ایران بهتر از آنچه هر کسی انتظار داشت، پیش می‌رود.»
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19486" target="_blank">📅 22:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19485">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1c7f0727d.mp4?token=FeYwXMG8RZBAhCbAfmE9_fxEMCyNSHYQB-BaOVFy7T_P2zRDf0qvgqRztj8vzxyBJjcjIGa953r9oJvThZ8DvqsAczvSDgt41RZovqhhbgxMEWWiRdEj-arWwMqjyqoXHc-EXMOQMjtaGrwU5aC4snjpK8yHr3YrqWV7CDYtgVPMvIu3rRDHSGeDxbOz0sT4ykOW4KBR1ELKXKm3P8zcjY6xejZUOVoFIF2su9homNE1ZWwUr52aK4QAaGVIhDwKazepseONOQwpSy_pwI9QgfusEeyPBs_tzhNNhXo0vb6P4UjBFtnmK84HJDFH_D0O3Yr4nEhwBm2BqxeObZ8KoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1c7f0727d.mp4?token=FeYwXMG8RZBAhCbAfmE9_fxEMCyNSHYQB-BaOVFy7T_P2zRDf0qvgqRztj8vzxyBJjcjIGa953r9oJvThZ8DvqsAczvSDgt41RZovqhhbgxMEWWiRdEj-arWwMqjyqoXHc-EXMOQMjtaGrwU5aC4snjpK8yHr3YrqWV7CDYtgVPMvIu3rRDHSGeDxbOz0sT4ykOW4KBR1ELKXKm3P8zcjY6xejZUOVoFIF2su9homNE1ZWwUr52aK4QAaGVIhDwKazepseONOQwpSy_pwI9QgfusEeyPBs_tzhNNhXo0vb6P4UjBFtnmK84HJDFH_D0O3Yr4nEhwBm2BqxeObZ8KoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران هیچ نیروی نظامی ندارد.
آنها هیچ چیز دیگری ندارند جز اینکه شرور و باهوش هستند و هنوز هم توانایی‌هایی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19485" target="_blank">📅 22:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19484">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed657c044.mp4?token=lTMzvSAQ32L7tQyOn2JyLTNIJeOI0bTOWeYpsgDVk7klTU7aIF8S2yMASssvBTVERjIx1I9kBsaAb5pDWn0OZrhTiWUYisCvOStZA5ustzvdBxjlNBtnZFfTdgQSNp8MfDzHdOGWZoyJVDW2gEyhUmXjdKp_BvH_SISNYKx9NYQoFxN-iOVYv2Jx58YZx-o0mD3da49VGrYaLnaIqJXUxQG-sCzo2R2gD9uA5hU0wdYRxPupLo6msALDZp5JhSNCtc7g3sPt337IHKvP8pwXeFqRyvn9WQl1VaZcP8MwqRu1NZz-AVRDip_1ikGS9J42NDXSyGeHIr8uj4Qdy6tezIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed657c044.mp4?token=lTMzvSAQ32L7tQyOn2JyLTNIJeOI0bTOWeYpsgDVk7klTU7aIF8S2yMASssvBTVERjIx1I9kBsaAb5pDWn0OZrhTiWUYisCvOStZA5ustzvdBxjlNBtnZFfTdgQSNp8MfDzHdOGWZoyJVDW2gEyhUmXjdKp_BvH_SISNYKx9NYQoFxN-iOVYv2Jx58YZx-o0mD3da49VGrYaLnaIqJXUxQG-sCzo2R2gD9uA5hU0wdYRxPupLo6msALDZp5JhSNCtc7g3sPt337IHKvP8pwXeFqRyvn9WQl1VaZcP8MwqRu1NZz-AVRDip_1ikGS9J42NDXSyGeHIr8uj4Qdy6tezIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام  : از زمان از سرگیری محاصره دریایی علیه ایران در نه روز پیش، سنتکام ۱۲ کشتی تجاری را تغییر مسیر داده و ۱ کشتی را از کار انداخته است تا از ورود یا خروج کشتی‌ها به بنادر یا مناطق ساحلی ایران جلوگیری کند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19484" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19483">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شبکه12 اسرائیل : مقامات آمریکایی به همتایان خود در اسرائیل، آماده‌باش ابلاغ کردند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19483" target="_blank">📅 22:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19482">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">منابع عربی: کره شمالی در حال تخلیه سفارت خود در تهران است.
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19482" target="_blank">📅 21:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19481">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گزارش کامل فاکس نیوز با موضوع حمله به قلب انرژی ایران که امروز بیشترین دایرکت و درخواست رو در مورد این گزارش داده بودید. ویدیو کامل به همراه زیرنویس فارسی.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19481" target="_blank">📅 21:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19480">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvqJNZnZhmeITNLlYPXAMwLmWFYR5F9ub_a5-AwpKzdDjrYnKJBihx_TIt1L1Mc-rbFR2xg0ESJIqYcc8EyxdpcC_QC0XfMjpYBG4eGKStZPCGJErNb8-GVeAyS7JcOf-OsB43DwQ_mc34VAeZMcMydPzyL9wXtwKWX3HpUMRiZ1ecwMfekAz8KxGyELAlXj0DA7vmID1CxFf2YrlFktKs4rsXmWDccTaiTzFc61FPJbdeNkODKUU6j7sqnkM6YMmhKZFTNV_YmMBmEdfTTVOSpuwePItOeYtvjhGQl4yzfJWVJIcgeHuIS5Lr0S2rEGQrU3ce7GYISeZ3CovhN1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون؛ نفس های آخر رژیم
،
استقرار
موشک ذوالفقار در میدان آزادی
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19480" target="_blank">📅 21:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19479">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به گفته منابع غیر رسمی اعضای سفارت آلمان از ایران خارج شدند
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19479" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19477">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بریتانیا پس از تهدیدات جمهوری اسلامی : نیروهای ما آماده مقابله با هرگونه حمله هستند،.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19477" target="_blank">📅 20:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19476">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تسنیم: تکذیب هرگونه اصابت جدید در جزیره لارک/ صدای انفجارها از سمت تنگه هرمز است ‌@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19476" target="_blank">📅 20:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19475">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تسنیم: تکذیب هرگونه اصابت جدید در جزیره لارک/ صدای انفجارها از سمت تنگه هرمز است
‌
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19475" target="_blank">📅 20:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19474">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کانال ۱۴ : موشه سعدا، نماینده مجلس از حزب لیکود، در یک برنامه زنده تلویزیونی گفت: «همه ما می‌دانیم که به سمت حمله به ایران، شاید حتی همین آخر هفته، می‌رویم»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19474" target="_blank">📅 20:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19473">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سنای آمریکا سد راه محدودیت جنگی ترامپ شد
مجلس سنای آمریکا، طرحی را که قصد داشت اختیارات نظامی دونالد ترامپ برای آغاز جنگ احتمالی علیه ایران را محدود کند، متوقف کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19473" target="_blank">📅 20:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19472">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزارت امور خارجه آمریکا: از شهروندان آمریکایی مقیم خاورمیانه درخواست می‌شود برای احتمال لغو پروازها و بسته شدن مسیرهای هوایی در این منطقه آمادگی داشته باشند. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19472" target="_blank">📅 19:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19471">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزارت امور خارجه آمریکا: از شهروندان آمریکایی مقیم خاورمیانه درخواست می‌شود برای احتمال لغو پروازها و بسته شدن مسیرهای هوایی در این منطقه آمادگی داشته باشند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19471" target="_blank">📅 19:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19470">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی:
ایران آخرین پیشنهاد آمریکا برای صلح را رد کرده است.
ما در حال تلاش هستیم، اما ایرانی‌ها تمایلی به همکاری نشان نمی‌دهند
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19470" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19469">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امیدیه ستون دود دیده میشود ولی صدایی به گوش‌ نرسید
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19469" target="_blank">📅 19:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19468">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اهواز هم زدن
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19468" target="_blank">📅 19:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19467">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝒎𝒐𝒉𝒂𝒎𝒎𝒂𝒅</strong></div>
<div class="tg-text">https://t.me/boost/withyashar
یاشار لینک boost رو دوباره بزار اعضای جدیدی که پرمیوم دارن هم حمایت کنن سطح ۲ رو از دست نده کانال.</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19467" target="_blank">📅 19:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19466">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبرگزاری‌  رژیم : یک موشک آمریکایی منطقه ای در ساحل شهر سوزا در جزیره قشم، در جنوب کشور را هدف قرار داد. @WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19466" target="_blank">📅 19:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19465">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجار در کویت
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19465" target="_blank">📅 19:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19464">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خبرگزاری‌  رژیم : یک موشک آمریکایی منطقه ای در ساحل شهر سوزا در جزیره قشم، در جنوب کشور را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19464" target="_blank">📅 19:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19463">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارهایی از جزیره بوبيان گزارش میشود
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19463" target="_blank">📅 19:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19462">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پدافند قشم فعال شده
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19462" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19461">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ به نشریه "اکسیوس" گفت: ایرانی‌ها می‌خواهند مذاکره کنند، اما در حال حاضر آمادگی امضای توافق را ندارند و هنوز به اندازه کافی تحت فشار قرار نگرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19461" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19460">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مجری : آیا مجتبی خامنه‌ای زنده است؟  نتانیاهو: فکر می‌کنم او زنده است. @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19460" target="_blank">📅 19:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19459">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ به نشریه اکسیوس: اسرائیل در عرض دو دقیقه به حملات علیه ایران خواهد پیوست، اگر از آن بخواهیم، اما ما نیازی به این کار نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19459" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19458">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ در گفتگو با شبکه ۱۲ اسرائیل اعلام کرد که در حال بررسی یک «حمله گسترده»، بزرگ‌تر از هر آنچه پیش از این انجام شده، است و گفت که به اتخاذ تصمیم نهایی نزدیک شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19458" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19457">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbda7bde91.mp4?token=RvDN5wq-uPBX3xhwrHVrjoMRzJNNXsQGgbn6uOsa7XqJdWZuTEM23G23ps4A8zVr_9I9vEuu35W8Ma-gw0jO-KC7xxUXy3Yrqu6Z14ZgwDmcoWNe9VaoK7_3yLmVZ2qqoZA34W7-XiUTQbGRr5-Ft8_VQIs0OIJ1mAmzEBdVdSKTU8VqtvMXppmZGjG9knmVK1fo-rGRLXnvDN2e29LVo5_-uNtaA02KDtF2frcOLBwFSchoXBsuqzbcjUaaHgM9TJfcZZINIJVzH6h3Lv6P6jiBQ0_njXP2qFMvm0VsnLcOYJkr946NedbmNm1TGdWtPKaA3W_egMImnqP4vh2BXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbda7bde91.mp4?token=RvDN5wq-uPBX3xhwrHVrjoMRzJNNXsQGgbn6uOsa7XqJdWZuTEM23G23ps4A8zVr_9I9vEuu35W8Ma-gw0jO-KC7xxUXy3Yrqu6Z14ZgwDmcoWNe9VaoK7_3yLmVZ2qqoZA34W7-XiUTQbGRr5-Ft8_VQIs0OIJ1mAmzEBdVdSKTU8VqtvMXppmZGjG9knmVK1fo-rGRLXnvDN2e29LVo5_-uNtaA02KDtF2frcOLBwFSchoXBsuqzbcjUaaHgM9TJfcZZINIJVzH6h3Lv6P6jiBQ0_njXP2qFMvm0VsnLcOYJkr946NedbmNm1TGdWtPKaA3W_egMImnqP4vh2BXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
: آیا مجتبی خامنه‌ای زنده است؟
نتانیاهو: فکر می‌کنم او زنده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19457" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19456">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کلیسای جامع ملی واشنگتن اعلام کرد مراسم یادبود سناتور لیندزی گراهام در ۲۸ ژوئیه(۶مرداد) برگزار می‌شود. این مراسم با حضور خانواده، دوستان، همکاران سیاسی و رهبران ملی برای بزرگداشت زندگی و چند دهه خدمت عمومی او برگزار خواهد شد. دونالد ترامپ نیز در این مراسم سخنرانی می‌کند و از نقش گراهام در سیاست خارجی، امور دفاعی و حزب جمهوری‌خواه یاد خواهد کرد. جزئیات بیشتر درباره دیگر شرکت‌کنندگان و برنامه مراسم بعداً اعلام می‌شود.
@WarRoom
یاشار : بی بی هم حتما میره !</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19456" target="_blank">📅 18:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19455">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سپاه: دیگر اجازه نمی‌دهیم آمریکا با آتش‌بس‌های فریبنده، ذخایر نفت و مهمات خود را جایگزین و پس‌از آن مجدداً حملات را از سر بگیرد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19455" target="_blank">📅 18:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19454">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبرنگار زن : آیا روسیه به ایران در هدف قرار دادن نیروهای آمریکایی کمک می‌کند؟
لاوروف، وزیر امور خارجه روسیه: مدل موهات قشنگه!
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19454" target="_blank">📅 18:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19453">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رویترز : ایران این ماه چند تا از فرمانده‌های سپاه و تجهیزات مربوط به موشک رو که با هزینه خودش خریداری کرده ،برای حوثی‌های یمن فرستاده! به ارزش بالغ بر 20 میلیارد دلار
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19453" target="_blank">📅 17:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19452">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46d0627615.mp4?token=tKfV14FiW_c5C90BilkR4hU7IRtKBnpE2ZZBZIm3Bq_bEySL1lBUNfzJBhmlqkU93J02wr-UJlI3A5iAA-oge5Z4KAF0UM2pk3vRQvma8iPTkV2bkrUfrwjLPEoRViJ34zg-fxws8I82XGkvcUd4Lz3zJ63Wuc6kFR0_yjU6xR7wqeHWr-7r2d3sjJEv64HhgqSFvWLBKNQSkaQ0UMwHOIZxPRRsHzdIOmWT-FsI2h-kmnwMZloy24QzQzE2p6st081EXRsyUgUv7aHrp0Zckikp6BIZZJhaH1fbGnFUqEs0e6yKCnIPe2SSEReJPnfkFoUB1Xz2NGMFFylYqcHueA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46d0627615.mp4?token=tKfV14FiW_c5C90BilkR4hU7IRtKBnpE2ZZBZIm3Bq_bEySL1lBUNfzJBhmlqkU93J02wr-UJlI3A5iAA-oge5Z4KAF0UM2pk3vRQvma8iPTkV2bkrUfrwjLPEoRViJ34zg-fxws8I82XGkvcUd4Lz3zJ63Wuc6kFR0_yjU6xR7wqeHWr-7r2d3sjJEv64HhgqSFvWLBKNQSkaQ0UMwHOIZxPRRsHzdIOmWT-FsI2h-kmnwMZloy24QzQzE2p6st081EXRsyUgUv7aHrp0Zckikp6BIZZJhaH1fbGnFUqEs0e6yKCnIPe2SSEReJPnfkFoUB1Xz2NGMFFylYqcHueA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی پیش انفجاری عظیم در جنوب لبنان منطقه کفار تبنیت  توسط حمله جدید نیروهای اسرائیلی انجام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19452" target="_blank">📅 17:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19451">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تایمز اسرائیل : بانک اهداف کاملا بروز شده
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19451" target="_blank">📅 17:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19450">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بیانیه شماره ۴۶ گروه تروریستی سپاه : ارتش متجاوز آمریکا که در تجاوزات خود بعد از شروع رسمی مجدد جنگ از پرتاب موشک های کروز از شناورهای خود در اقیانوس هند بهره می‌گرفت، با پایان یافتن ذخایر موشکی ناوهای مذکور، روز گذشته به استفاده از هواپیماهای B1 با پرواز…</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19450" target="_blank">📅 17:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19449">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عراقچی راهی قرقیزستان شد
عراقچی در راس هياتی سیاسی امروز به منظور شركت در اجلاس وزرای امور خارجه كشورهای عضو سازمان همكاری شانگهای عازم قرقيزستان شد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19449" target="_blank">📅 17:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19448">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بیانیه شماره ۴۶ گروه تروریستی سپاه : ارتش متجاوز آمریکا که در تجاوزات خود بعد از شروع رسمی مجدد جنگ از پرتاب موشک های کروز از شناورهای خود در اقیانوس هند بهره می‌گرفت، با پایان یافتن ذخایر موشکی ناوهای مذکور، روز گذشته به استفاده از هواپیماهای B1 با پرواز از پایگاه هوایی فیرفورد انگلیس روی آورد.
هر پایگاهی که برای تجاوز به خاک ایران استفاده شود، هدف مشروع ما است.
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی های مردم منطقه ما بوده و سوابق سیاه تجزیه کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات اخیر آمریکا و رژیم صهیونیستی ایران داشته، هشدار میدهیم بیش از این پرونده خود را سنگین نکند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19448" target="_blank">📅 17:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19447">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏دفتر نتانیاهو: پیوستن عربستان سعودی به پیمان ابراهیم جهشی تاریخی برای صلح خاورمیانه خواهد بود,  اقدام نظامی مشترک آمریکا و اسرائیل علیه رژیم تهران و درهم شکستن محور ترور جمهوری اسلامی، زمینه گسترش دایره صلح را فراهم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19447" target="_blank">📅 17:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19446">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYUkJh7tNBq9RrlhExbMWHcE4NvkAhVlLABKNoxwAJy8_pPE6JnJikV_goKOqQDv0DX08BYJH4PPWs7mGsu9Sf0c3zZOfsV5XuwxV39VABLyxpXSfm040k8KgQdTr2GDV8Ju6bnVnBDGgGZhz2B75gqwPYfK0fjUaQumrUxJK6i4vVPmho9O4IfIS-zQMcvt4PELJIOG_HoDtaM0YGZDiuMPQXHty6Gj-LWgabjA33gS7Hnk2TWkdCB3lpNlH9pyTymb5CajRSoRGFCW8owo8Mji3b_4cW7WGBnWM5fU2K3LH_OYTSYajEYLC-g1-yf0NXWZuEoE6TjsoitXbPJwkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت از ۱۰۰$ عبور کرد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19446" target="_blank">📅 16:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19445">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ در‌تروث : اگه حوثی ها دوباره به کشتی ای حمله کنند، ایران را مسئول خواهم دانست
یک سال پیش، ایالات متحده آمریکا به طور جدی به حوثی‌ها به دلیل دخالت آن‌ها در تجارت و بازرگانی، با شلیک به کشتی‌ها، حمله کرد.
از آن زمان و در طول درگیری ما با ایران، آن‌ها به طور مسئولانه عمل کرده‌اند. متاسفانه، اکنون آن‌ها دوباره این کار را شروع کرده‌اند و شب گذشته به دو کشتی سعودی شلیک کردند.
لطفاً این حقیقت را در نظر بگیرید که اگر آن‌ها این کار را دوباره تکرار کنند، ایالات متحده ایران را مسئول خواهد دانست، زیرا حوثی‌ها یک ابزار و/یا نماینده ایران هستند، و مجازات‌های نظامی جدی بر ایران و البته خود حوثی‌ها تحمیل خواهد شد. من از عملکرد آن‌ها بسیار ناامید هستم، زیرا آن‌ها تا به حال به طور حرفه‌ای و هوشمندانه عمل کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19445" target="_blank">📅 15:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19444">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرانسه کارکنان سفارت خود در تهران را تخلیه کرد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19444" target="_blank">📅 15:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19443">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOIeBLJ8PsyJ8eW36XBR2-9CJMsM3r20xz_DghHvAGmHn4UVqbrXdZBYsXcbJMdK92uedIBTfsm1-Ptn3By8HNwcsG4aHD02zqZFv1Z0S6HTVYOaQ369feWHaIBYRepoDE8_dNaYJMAvJt0QNMrYkwPfhFGRcfDfI2_H-mjzybaE8OmnPvw52P2XWHtQneBylFI3xcjv11pIrd9QaT0ikyCUH927unDxhEqjdPlidmwfJbR5fLOsqsVsuHuMYcT_Bc8DzBFExFZPKzEyepnEjB5APFKciOhOa9nHxMuNrX08uCyngk18gLQm1usge61AqoJCjqQUv-SYgFNe5gpoIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : توافق هسته‌ای غیرنظامی (هیچ‌گونه غنی‌سازی مواد در کار نخواهد بود!) که میان وزارت انرژی ایالات متحده و عربستان سعودی در حال تنظیم است و صرفاً به استفاده‌های غیرنظامی، مانند برنامه‌هایی که ایران، امارات متحده عربی (و کشورهای دیگر) از قبل دارند، مربوط می‌شود، تأیید خواهد شد؛ اما این تأیید کاملاً مشروط به پیوستن عربستان سعودی به توافق‌نامه‌های بسیار معتبر و موفق ابراهیم است.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالفتی ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19443" target="_blank">📅 15:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19442">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">متأسفانه امروز صبح خواهران دوقلو رومینا رحیمی و  ترانه رحیمی اعدام شدن @WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19442" target="_blank">📅 15:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19440">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk7g0jx6e_qRk_6rMgLS26AI1Zu5XRR0tuoqVKoM9f7UmRKeeclVb-ZlO01QGN56T1GRWHrzh6AUddPHSOUVEylOYgUZun2mxmI72jEmr1ECJisSoJ5ZH2EaYNGc2A8Rwj-qrzWrSDmz0dw3vvfC-9sNm3-iIY1aCML8tEI-oRB6g3wF9zybmfdEwq1Gt60v-OR1QRG1ZB7-dt-sM-3mLbrCdVQhhOGnKx7H1-A9Vl29JfGJvFmZS2fvjd7Ca0WWnqrV-MpLeCRmxEPcA-E1nCpL1BDYY4gcs6oBhxn2jQ835yfhwyKHSZM0yPsSq5mRY5psFPgDK7s-gzuaYdgUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85c6b93d2.mp4?token=vVS6LODRbZKmoJuxiJKYA5Vn0ygs9-upzqa1OaCA6s-oeiM0WwbR5eD_jOXH7GDlIlP4uFHZKfKZ88VhUiaFHUouXy82cvqCihT0Y8z-fnaVm92LMaOOvYxp1CsqVrCv7Dc6gvrlDjzVSaBAP0S6QPQlJPSDrXqTX04sXYEjSnNjc4QvIogH0JQKPufifHNlXrRnvfLTTK6J8hBs0sfuKEXyCh9LlglQCdApYel1qoYv9n8vE5wPu6Ej-_bqvO3Mh30tSvo907K8xN_QQrtM86zljs5qIPxFfHhdxAA9sWVtHU9Jpl5N5c2rs-cbvpnTIHCZTQFvNYFVhIneJT5fJ1JYTNovKUN6TJYvX-fbZv8JtIzxNJuPoJy2juVW9NLuYCJAgyQq7LWfjKgUIdESU3R6oZzA9Yd8bpZbHIIU1iffDiA_zqcrXg1tGvUj_D07QgGa07aJW91SqiO456XC5Mv0Ps-F92vCVhXKvVDmxZgeYa1xRrr8ecDfZKRtJdbLMTOry6pS6iuwWcztedQRA36hHSKfD85DL_1fRUwtC3J0pNyWaitCd2iWEDXvU6Wjt-xJ__9T3u8lasXi8gxXrF-HH1AL8ztxeflj5o7Yg_r8Sw95eiweBKj-0VuqSu8cDTsTd5hzjQ9cyJiA3nUfihZDps7eRmhUBTDcDDWjlaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85c6b93d2.mp4?token=vVS6LODRbZKmoJuxiJKYA5Vn0ygs9-upzqa1OaCA6s-oeiM0WwbR5eD_jOXH7GDlIlP4uFHZKfKZ88VhUiaFHUouXy82cvqCihT0Y8z-fnaVm92LMaOOvYxp1CsqVrCv7Dc6gvrlDjzVSaBAP0S6QPQlJPSDrXqTX04sXYEjSnNjc4QvIogH0JQKPufifHNlXrRnvfLTTK6J8hBs0sfuKEXyCh9LlglQCdApYel1qoYv9n8vE5wPu6Ej-_bqvO3Mh30tSvo907K8xN_QQrtM86zljs5qIPxFfHhdxAA9sWVtHU9Jpl5N5c2rs-cbvpnTIHCZTQFvNYFVhIneJT5fJ1JYTNovKUN6TJYvX-fbZv8JtIzxNJuPoJy2juVW9NLuYCJAgyQq7LWfjKgUIdESU3R6oZzA9Yd8bpZbHIIU1iffDiA_zqcrXg1tGvUj_D07QgGa07aJW91SqiO456XC5Mv0Ps-F92vCVhXKvVDmxZgeYa1xRrr8ecDfZKRtJdbLMTOry6pS6iuwWcztedQRA36hHSKfD85DL_1fRUwtC3J0pNyWaitCd2iWEDXvU6Wjt-xJ__9T3u8lasXi8gxXrF-HH1AL8ztxeflj5o7Yg_r8Sw95eiweBKj-0VuqSu8cDTsTd5hzjQ9cyJiA3nUfihZDps7eRmhUBTDcDDWjlaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو فروند هواپیما جنگ الکترونیک آمریکا،مدلEA-37B CompassCalI II ساعاتی پیش در مسیر خود به سمت خاورمیانه به فرودگاه RAF Fairford بریتانیا رسیدند.
تا کنون فقط پنج فروند از این مدل ساخته و تحویل شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19440" target="_blank">📅 14:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19439">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قیمت نفت خام برنت به ۹۹ دلار به ازای هر بشکه رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19439" target="_blank">📅 14:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19438">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فاکس نیوز : ایران متوجه شده است امریکا شنبه و یکشنبه که بازار جهانی تعطیل است را برای جنگ انتخاب میکنند‌ و ایران مابقی هفته را برای فشار به بازار جهانی
نفت که در حال رسیدن به ۱۰۰ دلار است
پاییز غرب زودتر فرا میرسد و جهان نیازمند سوخت
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19438" target="_blank">📅 13:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19437">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری هاآرتص : در اسرائیل خود را برای احتمال حمله از سوی ایران در شنبه و یکشنبه آماده می‌کنند
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19437" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19436">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">روبیو: ایران توسط روحانیون تندرو اداره می‌شود «اگر آنها پولشان را صرف مردم و اقتصادشان می‌کردند، امروز ایران احتمالاً ثروتمندترین کشور منطقه بود.» عراقچی می‌گوید سیاست آنها چشم در برابر چشم است. سیاست ترامپ سر در برابر چشم است.  اگر وضعیت با ایران به همین…</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19436" target="_blank">📅 12:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19435">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قیمت قراردادهای آتی گاز در اروپا به ۶۴ یورو نزدیک شده و از بالاترین سطح خود در زمان جنگ در منطقه هم فراتر رفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19435" target="_blank">📅 12:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19434">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هم اکنون آژیر حمله پهپادی/موشکی در بحرین
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19434" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19433">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">روزنامه maariv : شهردار رمت گن در اسرائیل دستور بازگشایی پناهگاه‌های شهری را صادر کرد:
«احتمال شلیک موشک از سوی ایران در پایان هفته افزایش یافته است.»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19433" target="_blank">📅 12:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19432">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یک اسکادران جنگنده پنهانکار F-35 با عبور از اقیانوس، توسط دو سوختستان استقبال و کمی دیگر در انگلستان به فرود میآیند. یکی از آنها، احتمالا به علت نقص فنی یا برای نشان دادن خود به جهان و تمرین ، آلارم فرود اضطراری روشن کرده است. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19432" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19430">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35bc0c2eb1.mp4?token=Zx-VQoSnjhw37uT6WKuiMxhamO2r1ul2Zj3O9b2xHp-pPctZHrbZzgP0AVVUZ_Ddmn4SRMSpB1No42niJg3YI4ocMfIWH28CALKGfUO6myDNW6wT5lVDQp1YH46KjB_cWFMgW3t4i0IUuBmMGAeyJBu2u6NrtAMXDTd6we6h87RvvX0xDvkO2optXJViL789LDK2anLnM2xSDxxH2OIgw8Eu35vG7FoPh4bMPKRrn3qdbk5jYVRs9oMJzIkR4TiIXysRnGHcCxqSaaUEmaz66Tm22Ke6L495gN46giCFuKSUXYya6sYVImSuilaN9C_nZoTMX-W06oix3X4DaAvstWr5K0j8cWulGyv7tokUOcBGQZpI98XScYUTAby3pNBFocHydUvdohsGLH2LnbshZyCLXpdtbmP6R7L1hfo2IRJXH753Ror0eXb8oKu2F9wNs47w0FcFZ-tkha1aUaAeW32mBuewpfQ20la63-BfxCn6CTSkYn_0k_LRCkY57-Qxp6be9lHsORgJw7wkaHd1HPzzSWIuMyhiJYyvHvVyd9s2IXXMFuHlYBiPTksjnOcdO18NjjjxoKARvDovLTWKX7mvCyyTblvXksRxg_JvLIsVwVkNcf7EVR_7-Ok-2tH834rueBLVU5uETyfph-I4j2R6T0AZoR5tQpy7R3i8OMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35bc0c2eb1.mp4?token=Zx-VQoSnjhw37uT6WKuiMxhamO2r1ul2Zj3O9b2xHp-pPctZHrbZzgP0AVVUZ_Ddmn4SRMSpB1No42niJg3YI4ocMfIWH28CALKGfUO6myDNW6wT5lVDQp1YH46KjB_cWFMgW3t4i0IUuBmMGAeyJBu2u6NrtAMXDTd6we6h87RvvX0xDvkO2optXJViL789LDK2anLnM2xSDxxH2OIgw8Eu35vG7FoPh4bMPKRrn3qdbk5jYVRs9oMJzIkR4TiIXysRnGHcCxqSaaUEmaz66Tm22Ke6L495gN46giCFuKSUXYya6sYVImSuilaN9C_nZoTMX-W06oix3X4DaAvstWr5K0j8cWulGyv7tokUOcBGQZpI98XScYUTAby3pNBFocHydUvdohsGLH2LnbshZyCLXpdtbmP6R7L1hfo2IRJXH753Ror0eXb8oKu2F9wNs47w0FcFZ-tkha1aUaAeW32mBuewpfQ20la63-BfxCn6CTSkYn_0k_LRCkY57-Qxp6be9lHsORgJw7wkaHd1HPzzSWIuMyhiJYyvHvVyd9s2IXXMFuHlYBiPTksjnOcdO18NjjjxoKARvDovLTWKX7mvCyyTblvXksRxg_JvLIsVwVkNcf7EVR_7-Ok-2tH834rueBLVU5uETyfph-I4j2R6T0AZoR5tQpy7R3i8OMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو: ایران توسط روحانیون تندرو اداره می‌شود
«اگر آنها پولشان را صرف مردم و اقتصادشان می‌کردند، امروز ایران احتمالاً ثروتمندترین کشور منطقه بود.»
عراقچی می‌گوید سیاست آنها چشم در برابر چشم است. سیاست ترامپ سر در برابر چشم است.
اگر وضعیت با ایران به همین منوال ادامه یابد، آن‌ها بهای سنگینی خواهند پرداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19430" target="_blank">📅 12:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19429">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزارت خارجه آمریکا برای سومین بار پیام هشدار صادر کرد:
تنش در خاورمیانه بالا است، خطر تشدید ناگهانی وجود دارد.شهروندان آمریکایی احتیاط بیشتری داشته باشن
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19429" target="_blank">📅 12:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19428">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a1de54c5.mp4?token=naRz9FowRqgNqkUaQbnvGHXOieZSAXFBKa7Xs8Shir0Iapq9RuQOW5PmZ5_SKahIYuOme9vdj-NqET_RT9jSavKXXNH-fDFS-oHI-UzmvV85d6lKTRejK_P6rrtuTbSmkUWJwPEob8nohF4OUv00PPl924ewbQva9wDoDfMVc1CiYvR7uUICAJhKHOa45bf0T5Io096yO4aWXNJn2oNY9V68ntCpJAawWUve5DGJwOvGNKxUXwd17mIFix6uT8jbNCdK0yxwcY_C3fyKWSwU3O6rwS-rrKATF1ZN704Eo2_S-MDvUFjQYLvpDN_oq1S4xC6ooU1dkR_1WgYMD8AbHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a1de54c5.mp4?token=naRz9FowRqgNqkUaQbnvGHXOieZSAXFBKa7Xs8Shir0Iapq9RuQOW5PmZ5_SKahIYuOme9vdj-NqET_RT9jSavKXXNH-fDFS-oHI-UzmvV85d6lKTRejK_P6rrtuTbSmkUWJwPEob8nohF4OUv00PPl924ewbQva9wDoDfMVc1CiYvR7uUICAJhKHOa45bf0T5Io096yO4aWXNJn2oNY9V68ntCpJAawWUve5DGJwOvGNKxUXwd17mIFix6uT8jbNCdK0yxwcY_C3fyKWSwU3O6rwS-rrKATF1ZN704Eo2_S-MDvUFjQYLvpDN_oq1S4xC6ooU1dkR_1WgYMD8AbHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله صبح امروز به منطقه دوم دریایی ولایت نیروی دریایی ارتش در جاسک ، جنوب شرقی ایران
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19428" target="_blank">📅 12:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19427">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">صداوسیما:دقایقی پیش صدای چند انفجار در کنارک شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19427" target="_blank">📅 11:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19426">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏رویترز: آمریکا در حال اعزام نیروهای تقویتی به خاورمیانه است
‏خبرگزاری رویترز گزارش داد پس از تهدیدهای گروه تروریستی حوثی جمهوری اسلامی، آمریکا در حال اعزام نیروهای نظامی تقویتی به خاورمیانه و گسترش گزینه‌های نظامی خود در منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19426" target="_blank">📅 11:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19425">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزیر امور خارجه آمریکا، روبیو : ایران در حال حاضر آمادگی لازم برای انعقاد توافقی با ما را ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19425" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3405b1189d.mp4?token=v8KDJvyAcHA6Y3h63MFBaQhyn_CYCWvJ9vKYCRO2CMU9f4n9-w8UFdmOhH2EuIhaEySTAzS2abJob8oHNF0AVeNkojy4B7oIu9URN1vk8xR8ueylVQGbPcDDdOkyR61rSKbeqN0fCVxCoMBkSw_4vDvovGUn9w-x2SKqGX_qifZksxT7-OyfLzKb9POwhq4J4YNLJ5SITGjFM-uj01QaVmYfhXlcdTGzrzD1QNGR7yIenHvhT7IPjOGYhcIxaS1KjW3tBvP6PFUjtdeOsmiELHYFvZmEnJRTHM-2ztCLCdfLw7ffooSltB9FstjWUjzpALIeEMSXFCuRGfOuk9Vkdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3405b1189d.mp4?token=v8KDJvyAcHA6Y3h63MFBaQhyn_CYCWvJ9vKYCRO2CMU9f4n9-w8UFdmOhH2EuIhaEySTAzS2abJob8oHNF0AVeNkojy4B7oIu9URN1vk8xR8ueylVQGbPcDDdOkyR61rSKbeqN0fCVxCoMBkSw_4vDvovGUn9w-x2SKqGX_qifZksxT7-OyfLzKb9POwhq4J4YNLJ5SITGjFM-uj01QaVmYfhXlcdTGzrzD1QNGR7yIenHvhT7IPjOGYhcIxaS1KjW3tBvP6PFUjtdeOsmiELHYFvZmEnJRTHM-2ztCLCdfLw7ffooSltB9FstjWUjzpALIeEMSXFCuRGfOuk9Vkdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب ۲ موشک با صدای مهیب از خرم آباد لرستان  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19424" target="_blank">📅 11:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نفت ۹۸$
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19423" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19422">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارش انفجار ‌در ‌قطر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19422" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19421">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ka46ClHNTzjTueZgVl6YDi1n1IV0tUI1ebxDxgZvgKKhFjm1a7f_NXdWeKhy1q670FNx_Qobel5CYFKsTty6kJ7R9Qv7e_cMb7cOv_a2wnFVQfc64_cvnK6B8-Vcb_mstYXZYqZVzNo1Cu8KVG3AA_a0KjMwYF39vHk3z_WrMUoX8CYF3VOoydykvWGV1b3TVLecUe1YrHAimLH-XgCFS4QW71cGRU9sI6a6INNq1hLvmZW1OAmTdsnqgfrjEwResMl1KQ7L2-5xdjq6WHHitKuevk_oaBKUlH5_ROzPccILJLtUt5YQEqvftW-brn7CBlLyrldih7_cZY1H7PRKhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب ۲ موشک با صدای مهیب از خرم آباد لرستان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19421" target="_blank">📅 11:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19420">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">معاون امنیتی استاندار بوشهر: شهر دشتی سه بار مورد حمله آمریکا قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19420" target="_blank">📅 10:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19418">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آلارم اتاق جنگ : فردا شب از نزدیکی منطقه های حساس نظامی ، تونل و پل های مهم که مسیر عبور تجهیزات نظامی هستند عبور نکنید !
⚠️
⚠️
⚠️
@WarRoom
یاشار : فردا شب ویسکی و آبجو میکس
🤒
⚔️</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19418" target="_blank">📅 10:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19417">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkl_zu33yHFtot6muhDxP0_AfDNBEXycUgNQ7ZY5yl-52qcaLZTQc9Nd2gX48-PCTUBk5JvhmHhOa_x7dR0Dx19WE-XE1ftDrDF0RSaeyinegvX8ozw9I8M5M1-otl9k3reIAIhw_LvvWDUgPxvET9p7hfv9JEpTsgj1XSvq_LCg9waMl7-91sXvtS--dhb6ZdQvMxbAAu65N8Y0riUUL5p9Wgb3BDkL0WojYE7Svf-kSfnI3x_VASYQI8LziMzEs869TMrKczMgD--EWM5mS1_nuOxuDDjsfHMh9Kbfrs2xz9-MgRZDDecOV5HkBw5lM-yxJWQo_q8PzhrdvLbmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همانطور که در پست اینستاگرام (اتاق جنگ دروازههای جهنم) نشان دادم، هواپیماهایی که دیشب از آمریکا حرکت کرده بودند همکنون روی اروپا و نزدیک به خاورمیانه هستند.
فعالیت هواپیماهای ترابری نظامی C-17 و C-5M نیروی هوایی ایالات متحده در مسیر بین اروپا و خاورمیانه، به سطحی افزایش یافته که مدت‌هاست مشابه آن مشاهده نشده است.
منتظر یک جنگ تمام عیار باشید. دروازهها باز شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19417" target="_blank">📅 10:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19415">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFbdca9cXhwsxBit0adpi9sHWSsWsw0OS9_zZm7RLyZNhSoWW0ApX3eQ7z92gFud9XzzgM1y_Qc6D835ekzB2JtR92aDYrHwaw5EaYSu7UNiLirRvLhd4NiHkpYALXoJvBX6N6_NowoCiR5HAgcWEN62g3OYPO9JqIj9cRKwF_t7VKp9U6L6-DmiMsTfIZQhbyowodSYcelQiSVCHMVrA9hm-RFaTnWa6FTOkrw9Aav8cy-BWk7supYUA9wXq22ysrVn-2di0EK2Bm-ucYzmrl7jSIBq1l_WhLfhW1bJdlHL1Sejq1U63ohm4GAZRL_eqIK9exuCuGYKNP2OZhr2ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه امروز صبح خواهران دوقلو رومینا رحیمی و  ترانه رحیمی اعدام شدن
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19415" target="_blank">📅 10:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19414">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnyBr6J12QZIiLVAbJsvZmp7HHdEXW4AXfDZVyDj5RvpNn-zOwL-IFmciPjhg2-1QK1X8ECW3XJ0zdRry00vTItLbYOFS9NMdhwzqOyE6ED_hflxjPinmMrMNxnKNi4kbk1KIkxgm2ohxN0lBuM3LgxMPp0kbrQ6WAGZp8a0NpXoeWcvR7bOA_whx15PJJ_78PguSLD1fX-KTizdxGQLn_ok2u30eod5yp8fU86A6HXz5b7HUX7uimh39qrnOxaQUsE_55EFj166Dz9YU4Ehjj3lDKMBb-wiAdT06N6t7R9nEy8nBvKhHKJGXNIXAXnXs52C3l6yNdRSDXvor9C-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج جدید موشکی سپاه : هم اکنون پرتاب دو موشک از خمین
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19414" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19413">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vadEU8-N5uokEEAtPtyiPEXh3nQcv5NpC4LaPYDUDg0fDm2NXTKbCCrLcpL1xBcyIcb0qvbyr3kcuPEhkuOEFWk4zDpSkrmP5Z-ElzW80TopM1uvZMP0RnDBVGf84_RA1AS4We4DCH1qYmEw10GWfb05SW5-fBzQ3AOBQDi4s44dUanmy0PpaTnfGLtwkw6d8l1RqQkOKuhLQrWnw8SROqmJttuSCJQfux6s366in3w7d9rccP5mMDlzUkpG0Vg0h47covFa8K-j-7GQcftmKQKB505GsZIlaZN5V7ugxTtmIvsk5uuC-FeqKdExZhWKfTgiTLX5nLFe2HHaxxiezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏مجله معروف ایتالیایی "اسپرسو" با نشر مقاله اخیر خود، اذعان داشت:
‏دیگر نمیشود به محمدرضا شاه پهلوی گفت «آخرین شاه ایران»
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19413" target="_blank">📅 10:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19412">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بامداد امروز، در پی حمله آمریکا، نقطه‌ای در شهرستان کیار هدف حمله هوایی قرار گرفت.
عبدالعلی ارژنگ معاون سیاسی، امنیتی و اجتماعی استاندار چهارمحال و بختیاری با تأیید این خبر اظهار کرد: این حمله در ساعات اولیه بامداد امروز رخ داده و دستگاه‌های مسئول بلافاصله در محل حاضر شده و اقدامات لازم برای بررسی ابعاد حادثه و ارزیابی خسارات احتمالی را آغاز کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19412" target="_blank">📅 10:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19411">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران: من آن را یک درگیری می‌نامم. ما با جمهوری اسلامی ایران درگیری داریم. آنها آنقدر ضربه می‌خورند تا معامله کنند، اما من می‌گویم که آنها آماده معامله نیستند. آنها آماهده نیستند چون بعد زیرش میزنند. اما خیلی زود آماده خواهند شد. @WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19411" target="_blank">📅 10:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19410">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کنگره آمریکا نسخه خود از قانون بودجه امنیت ملی سال مالی 2027 (NDAA) را تصویب کرد که شامل بندهایی برای افزایش همکاری‌های امنیتی بین ایالات متحده و اسرائیل است.
این بودجه، بیش از 750 میلیون دلار را به برنامه‌های همکاری‌های امنیتی بین دو کشور اختصاص می‌دهد، که حدود 65 میلیون دلار بیشتر از سال گذشته است، و همچنین شامل طرح‌هایی برای گسترش همکاری‌ها در زمینه فناوری‌های امنیتی می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19410" target="_blank">📅 10:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19409">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1f97fe0f.mp4?token=p7h4yk9jT2ssh5YRDTAqoYgPFyZ7SYTSAxISFaqiL6hcrLw2FCmgeF7n2-6lF9DeW7RSsjRPJHNYQgjuPJQ4fN_TmOQ7a_QcozjURlYPOCViUni7WMikjjMKBMucJbSzCHPO7DRw8xlit4ZfgdQ4eXI-MnSA0fVDEqIBmzqYZum8y_eP3rgnwIfSpt-IQ44hhBxu8S4nWiIfHZkxGRH77Z2k-qFbxfylSwZ9BzwmPeAYKLAT96qqyLbajztZh3lH37UhmizZfxIK3mUOFIbAkUYmET3D_cIyttddaCDl_XkJDAYWZEBSpyHARVVthKMeUEKiCuPOGoxlhMuyP88v1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1f97fe0f.mp4?token=p7h4yk9jT2ssh5YRDTAqoYgPFyZ7SYTSAxISFaqiL6hcrLw2FCmgeF7n2-6lF9DeW7RSsjRPJHNYQgjuPJQ4fN_TmOQ7a_QcozjURlYPOCViUni7WMikjjMKBMucJbSzCHPO7DRw8xlit4ZfgdQ4eXI-MnSA0fVDEqIBmzqYZum8y_eP3rgnwIfSpt-IQ44hhBxu8S4nWiIfHZkxGRH77Z2k-qFbxfylSwZ9BzwmPeAYKLAT96qqyLbajztZh3lH37UhmizZfxIK3mUOFIbAkUYmET3D_cIyttddaCDl_XkJDAYWZEBSpyHARVVthKMeUEKiCuPOGoxlhMuyP88v1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب یه دلقکی اینجوری پشت ترامپ ادا شو درمیآورد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19409" target="_blank">📅 09:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19408">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEd5_nHeNV_DG967-XlPajk6RJk5BbMLzAWLqpb1tHa5bZhQYXqNhxneneJIzEYG6v9PIZHoPKXkXJEz2-n_3uhrtfEfZC9XL1uuRm_waSixeKnW6jbCQrUo0sRt8SbXymYaQdc2LgKf0IKt7GH1I6U8dfPoirdlThw4NxEMJpZFqKx5oIKjJVQaOwjCGYKxj2z4kQx0K1Bmt7IVjfG5gtWkHB56ExmwsO8P0c1mxKlPCJHZ36pdFVmUkoeKD1U4zq6V9iawFmZEKnWi2hjhHfK90l5P3f58mvJbFoPwsT9VyPDuDR4QnE5HonJd33PjnzewE2R7GFh4cgEAGbxj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏گزارش‌ها حاکی از آن است که بامداد امروز دو شناور جستجو و نجات دریایی «ناجی ۱۵» و «ناجی ۱۶» در حمله نیروی دریایی آمریکا هدف قرار گرفته و آسیب‌های سنگینی دیده‌اند. بر اساس گزارش‌های اولیه، احتمال غرق شدن هر دو شناور وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19408" target="_blank">📅 09:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19407">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F59lK2Fg7QRCDSW7NRWEk07Pz4rQhKKcSEqEG5-PEuFva5nFx1QcoEpRzROerHC-29vKK9mIz_rz7Axz5Qj0XFZ1q4adMMHr2w1ANXdbqL84FeaV5zIZ6DnX-E4ENLaeWcs6Sv3urL0YptUzBjym2pSyDL40BhiljMmNFUUt9mtQWzqAynthBErYmKRVPpytXZM6Vcx90PcVYufZYEU0ZsEksGp0J2R0QT4GMSXcv0ldy3sZt_bS6_qvaJxJPgOSdFkiDa3P-yps_78RlAVCWpPj48ZaqbYBrpnJdzu01LooXD2_ibMoDQloomK80kmm8eLhbTBt9E997-4EdmzBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان، با توجه به سوالات شما، حضور رادان ساعاتی قبل از حمله در شلمچه تایید شده است. ولی این که آیا هدف ترور بوده و کشته شده یا نه، هنوز مشخص نیست. در لحظه که خبری به دستم برسد، شما را در جریان خواهم قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19407" target="_blank">📅 09:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19406">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لیست نهایی شهر هایی که دیشب مورد حملات آمریکا قرار گرفته‌اند
💥
شلمچه
💥
سیریک
💥
رامشیر
💥
بندرعباس
💥
بندر جاسک
💥
بوشهر
💥
اهواز
💥
بندر ماهشهر
💥
اندیمشک
💥
اسلام آباد غرب
💥
ابهر
💥
کرمانشاه
دوازدهمین شب و کشیده شدن حملات به غرب کشور
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19406" target="_blank">📅 08:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19405">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گروه حوثی‌های یمن امروز پنج‌شنبه اعلام کردند دو نفتکش متعلق به عربستان سعودی را که در حال عبور از دریای سرخ بودند، با موشک و پهپاد هدف قرار داده‌اند. ساعاتی بعد، عربستان نیز اصابت پرتابه به یکی از این کشتی‌ها را تایید کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19405" target="_blank">📅 08:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19404">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش CNN: یک مامور سازمان اطلاعاتی از تیم امنیتی معاون رئیس‌جمهور، جی-دی ونس، به دلیل افشای اطلاعات به رسانه‌ها، از سمت خود معلق شد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19404" target="_blank">📅 08:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19402">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a54a3c2c.mp4?token=i-2aD-gEUUkITCucsS60AQrAt1h9f_xNz65ksJDMWHzLuWmPRaCyuZljH1RQPvMzyOTl_fr-al04NXAlDrcUaXUAR5KB6gmtQtu2piAtj0VOko00ZUeU7nc3gj_PJ_TaHg5ZQIp-WQauA_1EthMC5v1ClSugGTuYg9YGazKGadin-U6A4tdLeL4HlGkRJ9QwnTpuYzBhlZRm9edw-H5cagAuGmF62KIkHHNp1ETvzwzmVKS05kiFxB_zq9RcwT-coOmkOWZOJ75AwXrj_3pS-abuK310W_ZZ0aqxyWdIw0GKfS7N82ZFr3ndIhIR3y_9vXa82IaQU04zOZP5TwcKwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a54a3c2c.mp4?token=i-2aD-gEUUkITCucsS60AQrAt1h9f_xNz65ksJDMWHzLuWmPRaCyuZljH1RQPvMzyOTl_fr-al04NXAlDrcUaXUAR5KB6gmtQtu2piAtj0VOko00ZUeU7nc3gj_PJ_TaHg5ZQIp-WQauA_1EthMC5v1ClSugGTuYg9YGazKGadin-U6A4tdLeL4HlGkRJ9QwnTpuYzBhlZRm9edw-H5cagAuGmF62KIkHHNp1ETvzwzmVKS05kiFxB_zq9RcwT-coOmkOWZOJ75AwXrj_3pS-abuK310W_ZZ0aqxyWdIw0GKfS7N82ZFr3ndIhIR3y_9vXa82IaQU04zOZP5TwcKwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برج راداری گذرگاه مرزی شلمچه
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19402" target="_blank">📅 07:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw0KTKs9PWoYfgxIdkrCa357jmRWpZwEX0PuLV4DB4-cSDPAKh4Iy9wIVfvcglCb8ZeiHZwDG66RbYZ8_d5tGYyyqy6hVFc4O_nMaQFgHB_zNpfEEGxd0an0dQSP9gQdFzs68ro9LLMnz-xVS96B4KM5shUvcmKB7R6uuG0njDi2bPV2WFnGyIRTpOTu5ASkonsKjwXN0kZNyAaZc4MdXyTt6YXDsCJA44fFWJVvejFz124Sd_8kEoXFyE7BL8KqBngdVnKuYCzKvs4Twrywr_UEwzHyyDdQSHe_DV61gy7UcIg8UJLoMvGdIibH0Aluw3x2iQ2uoajUMhSqmbiKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: بمب‌افکن دوربرد بی ۱ آمریکا مواضع سپاه پاسداران را هدف قرار داد
‏اکسیوس به نقل از مقام‌های آمریکایی گزارش داد یک بمب‌افکن بی ۱ نیروی هوایی آمریکا روز سه‌شنبه با پرواز از پایگاهی در بریتانیا، اهدافی متعلق به گروه تروریستی سپاه پاسداران در ایران را بمباران کرده است. این نخستین استفاده آمریکا از بی ۱ از زمان ازسرگیری درگیری‌ها در ۱۲ روز گذشته است. این بمب‌افکن فراصوت توان حمل ۲۴ بمب ۹۰۰ کیلوگرمی یا ده‌ها موشک کروز را دارد و از بیشترین ظرفیت حمل مهمات در میان بمب‌افکن‌های آمریکایی برخوردار است. مقام‌های آمریکایی و اسرائیلی می‌گویند هم‌زمان با تقویت حضور نظامی آمریکا در منطقه، پرزیدنت ترامپ در حال بررسی آغاز دوباره عملیات گسترده علیه رژیم تروریستی جمهوری اسلامی طی روزهای آینده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19401" target="_blank">📅 07:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19400">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">معاون استانداری خوزستان:
در حمله موشکی آمریکا به گذرگاه مرزی شلمچه تاکنون دو نفر شهید و ۱۱ نفر مجروح شده‌اند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19400" target="_blank">📅 07:26 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
