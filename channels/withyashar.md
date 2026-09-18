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
<img src="https://cdn4.telesco.pe/file/AAt8in0g0IBL4yQNShlUGtiavbxh55DqxHZlfsAEuoI6GRPFzfGTR3rb83QF3lSrZGHOzfGAbn_ojW38hxcaH5S5t6tWed-EaSGitWMD9oX7DNv0xowp1Bq1zkTw8Y3G-uUCNIeNbfa1mnEDndGIQOPXSCtWnpiPGtvXU1k2XMg9WrD7m6f7Sn9CNtT1yXvWYHPlR1tfJRvcW9yt9gLZce1x7-9EV-ZBVUPBf-U11GufdvrBKXSFUvfNLQr4UZPNDLbHFIstuLbKREUC2p3X3F8eeeCFJETVqMpveVqR-bk5sMTXpWbWlEepfkow5nKb-Txw7ImZl_5Gop-Qn6A2yg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 05:52:39</div>
<hr>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6a10ce6c.mp4?token=uIb5do5CBNrTD1S4hDPnq9Jz3cKWJfBO-UKTl2fI7MOBHywSkeZ4-C5dltnJM_NBAUJbWHgH2A0L4CAzMZjExZDuxR4su_sYIHyFAIyE6Zpzam2OwJIPnRk6E4Rbf_4BhnF-OrZq0euGYRQupy8zMKOJnBFYzSpA_VVe2sZ1DD0deYCQmVtENdqZwtgygmOiNC9kiS2ASI25pOsqcSGPr700hcwNrp-_GfFom2_H93dp0q4RzIzYtSfEmi2vAYp0iIUbs_MmV0NGyBdHM7HNaJMZXF1QwF53wG-Y8NAdhvTw5vn8IYoQGQ6gA9jrt_Ic0nTj43rkRcfKVvlwxI9VpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6a10ce6c.mp4?token=uIb5do5CBNrTD1S4hDPnq9Jz3cKWJfBO-UKTl2fI7MOBHywSkeZ4-C5dltnJM_NBAUJbWHgH2A0L4CAzMZjExZDuxR4su_sYIHyFAIyE6Zpzam2OwJIPnRk6E4Rbf_4BhnF-OrZq0euGYRQupy8zMKOJnBFYzSpA_VVe2sZ1DD0deYCQmVtENdqZwtgygmOiNC9kiS2ASI25pOsqcSGPr700hcwNrp-_GfFom2_H93dp0q4RzIzYtSfEmi2vAYp0iIUbs_MmV0NGyBdHM7HNaJMZXF1QwF53wG-Y8NAdhvTw5vn8IYoQGQ6gA9jrt_Ic0nTj43rkRcfKVvlwxI9VpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : سلام یاشار جان زاهدان حدود ساعت 12 نیم بامداد امشب درگیری افراد مسلح شروع شد تا همین الان درگیرن صدا تیر میاد بین خیابون دانشگاه و دانشجو خیلی کشته دادن حدود 9 تا امبولانس فقط امده بود سر صحنه
@WarRoom</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/withyashar/23436" target="_blank">📅 02:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزیر دفاع ایتالیا: ما کشتی‌های جنگی خود را مستقر خواهیم کرد تا از عبور ایمن در تنگه باب‌المندب اطمینان حاصل کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/23435" target="_blank">📅 01:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایلی دریایی شمال شرقی خصب در عمان دریافت شده است. بر اساس این گزارش، هیچ خسارتی به کشتی وارد نشده و هیچ‌یک از خدمه نیز زخمی نشده‌اند. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/23434" target="_blank">📅 01:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش حمله پهپادی رژیم به کمپ های کرد های عراق اطراف اربیل
شبکه المیادین از شنیده شدن صدای انفجار در منطقه «مصیف» واقع در حومه اربیل، مرکز اقلیم کردستان عراق خبر داد.
همزمان منابع غیر رسمی از به پرواز در آمدن هواپیماهای جنگی آمریکایی در اطراف این شهر خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/23433" target="_blank">📅 01:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/23432" target="_blank">📅 01:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/23431" target="_blank">📅 01:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اتاق جنگ با یاشار: آیا حلقه اطلاعاتی آمریکا درباره شبکه‌های جمهوری اسلامی در حال گسترش است؟!   یکی از احتمالاتی که می‌توان درباره بازگشت برخی چهره‌ها و افراد ایرانی به کشور مطرح کرد، گسترش دامنه دستگیری‌ها و تحقیقات آمریکا درباره افرادی است که با جمهوری اسلامی،…</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/23430" target="_blank">📅 01:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W432Stfs3gkDiMeVlhlwH0og6ArKsogBw5KT3sIfmgghwkYVfmlUbywpcTCsLoItgDShe51V8SMKWmPAapDRLSvnJ0WoX7BwH3yPTXvhoDb_uJpvSPa4c5fzLrOHyfyoGKpcpm9WNm_86ONbSvzUFNnYVwDkQVLUivhd8wFo7BtyKjeQboLQNoJhM0iQ8Wk5jpEebzsrG1v55ZmVuUVcPZiIzyxe3DtDlTD-XK5llRNcXtM7hb8AC0NAB01hvDieTOQjKI3KzhK1buvQ9NCZ3nhdJgBw4HdVTmqadd8oSyBrSgeXWUgY9lQFh159bkXdHIK64BZYTNLFidVKAW17Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار: آیا حلقه اطلاعاتی آمریکا درباره شبکه‌های جمهوری اسلامی در حال گسترش است؟!   یکی از احتمالاتی که می‌توان درباره بازگشت برخی چهره‌ها و افراد ایرانی به کشور مطرح کرد، گسترش دامنه دستگیری‌ها و تحقیقات آمریکا درباره افرادی است که با جمهوری اسلامی،…</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/23429" target="_blank">📅 01:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/23428" target="_blank">📅 01:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/23427" target="_blank">📅 00:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">میدل ایست آی: دونالد ترامپ «وسلی هانت»، نماینده جمهوری‌خواه تگزاس، حامی سرسخت اسرائیل و از منتقدان شریعت اسلامی را به عنوان سفیر بعدی آمریکا در عربستان سعودی معرفی کرده است. هانت، افسر سابق ارتش آمریکا، پیش‌تر دو سال به عنوان افسر رابط دیپلماتیک در عربستان خدمت کرده بود. این انتخاب در شرایطی حساس برای روابط آمریکا و کشورهای خلیج فارس و همزمان با جنگ ایران و آمریکا و تشدید درگیری‌ها در یمن انجام شده است. انتصاب هانت برای نهایی شدن به تأیید سنای آمریکا نیاز دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/23426" target="_blank">📅 00:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/23425" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پدافند شرق تهران درگیر شد ، اگه ادامه دار بود گزارش بدید</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/23424" target="_blank">📅 00:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSina</strong></div>
<div class="tg-text">داداش فکر کنم دارن تهران و میزنن
هم صدای جنگنده اومد هم صدای انفجار شیشه‌های خونه ما لرزید مادرم از ترس رفت پایین
شرق تهرانم</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/23423" target="_blank">📅 00:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSemiramis</strong></div>
<div class="tg-text">پدافند پاسداران داذه همینجور میزنه</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/23422" target="_blank">📅 00:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پدافند تهران فعال شده و صدا ناله های شاش قاسم میده همه ترسیدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/23421" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23420">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/23420" target="_blank">📅 00:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/23419" target="_blank">📅 00:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23418">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/23418" target="_blank">📅 00:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/23417" target="_blank">📅 00:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/23416" target="_blank">📅 00:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/23415" target="_blank">📅 00:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صدای ناله های تنگسیری از قشم شنیده میشه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/23414" target="_blank">📅 00:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نه دیگه بهمن پنجاه و هفته
نه حرف برق مفت و پول نفته
نمی‌ذارم سر من هم بذارن
کلاهی که سر بابام رفته
شاهرخ
@WarRoom</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/23413" target="_blank">📅 23:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/23412" target="_blank">📅 23:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/23411" target="_blank">📅 23:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385ac22afd.mp4?token=B7ScxfxfLWBmVZ5pnsl2ijDMhwPvF33DiVJjo-MvgBu3UaRhey0_nou1X-cAybGQ5NMwpWy6wAStTeatinUJ72fqw5PdgtPhpPre8EdFN61vG-VMQ5TNfDF1pS7ovf6vPNdkzAKAZgynuTcYH3zDrB-EPSWxkj-8JR3kmprMtSndQdeBe1RHaMkImaMc1tlEGXbrKED36EiV-oY2XFcjzODGKM8pjmspXVAOdIBl5kyHRM_aecmbfx-bcrPepRkJbKR-t_zmM-1CGVBZcF7xHAOs9lME0Fjc1ywRkncYUld6gZLXlAWtKbgXiSLVrSQ9lUvI-Fk9oGC2kEMzmEvO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385ac22afd.mp4?token=B7ScxfxfLWBmVZ5pnsl2ijDMhwPvF33DiVJjo-MvgBu3UaRhey0_nou1X-cAybGQ5NMwpWy6wAStTeatinUJ72fqw5PdgtPhpPre8EdFN61vG-VMQ5TNfDF1pS7ovf6vPNdkzAKAZgynuTcYH3zDrB-EPSWxkj-8JR3kmprMtSndQdeBe1RHaMkImaMc1tlEGXbrKED36EiV-oY2XFcjzODGKM8pjmspXVAOdIBl5kyHRM_aecmbfx-bcrPepRkJbKR-t_zmM-1CGVBZcF7xHAOs9lME0Fjc1ywRkncYUld6gZLXlAWtKbgXiSLVrSQ9lUvI-Fk9oGC2kEMzmEvO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نِتانیاهو درباره ایران: ما تومور را از بین بردیم و اکنون زنده هستیم. این بدان معنا نیست که تومورهای دیگری برای مقابله وجود نخواهند داشت!
@WarRoom
💥</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/23410" target="_blank">📅 23:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/23409" target="_blank">📅 23:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/23408" target="_blank">📅 23:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23407">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGguDDAJFUOb4bYq24IkDmmivdWWxOowlafUCYCQDh4juGQo-yit3wmn1wfac-u2kvGZLdlKs3VT2omiiGx2Wj86Yzv_fQi-drelabrGAkSYiIyCLs-9GBJyj4dH3bF0mcAqiGoIU2BE5Upw74HrYQIKgNeLm72CD4IyFC-44Oq-A0-rHZBVOIXduy1HaLYyIJaqDzMVQKCROzGVvK76sPIsjULbV6q87g0Y_FNierFNUUlMPQrQZqJolTeFq9X4ng4y-vDyoIleTAK2K_f9YhadFwk0ZZGT16Akf5uM1WlNmw_aF2Maq5IhWbzcw-G6J6KznhmcOGgAinOZj0bufQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/23407" target="_blank">📅 23:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/23405" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23404">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">page2 :
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/23404" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23403">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شبکه کان اسرائیل : کویت و اسرائیل در حال انجام مذاکراتی سری به دلیل حملات ایران به کشورهای منطقه، از جمله خود کویت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/23403" target="_blank">📅 23:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23402">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5129cb70.mp4?token=utRZqijRJXMSY8LnrmjoiVbLdaSXu5eIAw9eq8Z6LRzsi1xpCPaRgx1VAzFyZLovMkFFUhRsin3g8_5gTFWeULYezl32_vS6KvA-usfOtYd-qt7DEbJxTdAzWM2gVEtbczKmxMLoFebFwc0BYZNYcAIlEqSEoqkuMZozZViw-1B-RuDJz1DmFsQFGtPWy-28Gb8c0YxtwYhFjDo59g6RpNpc812n_usGgC1DIRMGPA3mEulqTHnBURFbAJmtzi9QOeGznCpDIuhsm-eeEPhVlFEKqsk9pqVr6FdCSNhMhUPbiH3cv-lY4rCNmbITjQxeIUibUPSPhpCeq15anFLnqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5129cb70.mp4?token=utRZqijRJXMSY8LnrmjoiVbLdaSXu5eIAw9eq8Z6LRzsi1xpCPaRgx1VAzFyZLovMkFFUhRsin3g8_5gTFWeULYezl32_vS6KvA-usfOtYd-qt7DEbJxTdAzWM2gVEtbczKmxMLoFebFwc0BYZNYcAIlEqSEoqkuMZozZViw-1B-RuDJz1DmFsQFGtPWy-28Gb8c0YxtwYhFjDo59g6RpNpc812n_usGgC1DIRMGPA3mEulqTHnBURFbAJmtzi9QOeGznCpDIuhsm-eeEPhVlFEKqsk9pqVr6FdCSNhMhUPbiH3cv-lY4rCNmbITjQxeIUibUPSPhpCeq15anFLnqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد بزرگ شطرنج ، نتانیاهو: من مسیح نیستم و(کینگ) پادشاه هم نیستم. پادشاه نیازی به انتخابات ندارد؛ من باید انتخاب شوم.
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/23402" target="_blank">📅 23:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1019a561.mp4?token=uUl0q_j8N5RcIOQk6uetLSC4XVrmREkxo_TpTHoCcQiOY1WkCzTIstmqhDYAdyqMENyZf1TzJBBlHFAzvgdE1lsFFTbyCpu92kukoYHc5TOaw-96FWDxHizWNRxRJCDgZY3yJeDeyVTmLOruXjue632yImNq3hrW2T917iGtepsfbG8juSm3VdA62plBbSGt6TI75csb2vUSeOC4zJ5sa7DVQTsc2JlLdrk7mGWfO6RPwWAacyRmTMybV8T9Mrr4b2uvj0aWzD_ZjPuowaz7AqOn9zgsWmIQQgorV8eYae4MtVwnAAC6kO7i6E3ZpRXUwyg6cxIgBVJ0pg-swazZ5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1019a561.mp4?token=uUl0q_j8N5RcIOQk6uetLSC4XVrmREkxo_TpTHoCcQiOY1WkCzTIstmqhDYAdyqMENyZf1TzJBBlHFAzvgdE1lsFFTbyCpu92kukoYHc5TOaw-96FWDxHizWNRxRJCDgZY3yJeDeyVTmLOruXjue632yImNq3hrW2T917iGtepsfbG8juSm3VdA62plBbSGt6TI75csb2vUSeOC4zJ5sa7DVQTsc2JlLdrk7mGWfO6RPwWAacyRmTMybV8T9Mrr4b2uvj0aWzD_ZjPuowaz7AqOn9zgsWmIQQgorV8eYae4MtVwnAAC6kO7i6E3ZpRXUwyg6cxIgBVJ0pg-swazZ5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران: اول از همه، ما باید رژیم ایران را سرنگون کنیم. این مأموریت من است و این مأموریت اصلی ماست.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/23401" target="_blank">📅 23:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLVCZs5pFFMeLwZfEH7iBRTk4_2qk5uBe4AG1a6UEM7aVk4QDPzeSiXvox3DU9rNY1MLsXHFJBar8WYKSSTOyzdH0XWihelFGtoYqd3O5CBTcelBeUI3sa37V_rWPqtLaC6kkbGIb9EI1ZDh15PnmwfMNx9mboCEcmVhoX1pHwxeMqdlwbO_gnIoR2qtyz4Et2tjgtE1mFFJfbe7Elr84W7L73lcwDqu8zwMK6bTLZ3Ycf3Agg6sa2U9X6bjlUXs1t56lBDucTfpIf-n-UEovTP89DtMzeaeG9rZfIGKeSXSTG7FAOCoe4Z_gQupFNMzolexYCiNYdp9HA7ofn8LMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایلی دریایی شمال شرقی خصب در عمان دریافت شده است.
بر اساس این گزارش، هیچ خسارتی به کشتی وارد نشده و هیچ‌یک از خدمه نیز زخمی نشده‌اند.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/23400" target="_blank">📅 23:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارش پرتاب موشک‌‌ از لارک به سمت تنگه.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/23399" target="_blank">📅 23:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تنگه صدای ناله های مرحوم تنگسیری ‌میاد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/23398" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا اعلام کرد صرافی رمزارزی «بیت‌بانک» متعلق به شبکه مالی بابک زنجانی است. بر اساس اعلام خزانه‌داری آمریکا، بیت‌بانک تحت کنترل بابک زنجانی قرار دارد و شرکت «پیشتاز سیمرغ تجارت الکترونیک» نیز به‌عنوان توسعه‌دهنده نرم‌افزار این صرافی معرفی شده است. آمریکا در همین ارتباط بیت‌بانک و افراد و شرکت‌های مرتبط با شبکه زنجانی را تحریم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/23397" target="_blank">📅 22:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یک مقام آمریکایی: برای ایران ویزاهایی جهت حضور در نشست‌های سازمان ملل صادر شد.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23396" target="_blank">📅 22:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نتانیاهو: ما کار این رژیم را تمام خواهیم کرد ، به‌زودی غافلگیری‌ای در انتظار ایران است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23395" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نتانیاهو در کنفرانس حزب لیکود، روایت ترامپ را تکرار کرد: ما اسرائیل را از نابودی نجات دادیم، و اگر این اتفاق نمی‌افتاد، احتمالاً کشور اسرائیل وجود نداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23394" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تایمز اسرائیل
: سه میلیارد دلار بمب تخریب گر در راه اسراییل برای دور جدید حملات.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23392" target="_blank">📅 21:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تحریم‌های تازه آمریکا علیه یک صرافی رمزارز و کوبا
آمریکا پلتفرم ارز دیجیتال «بیت‌بانک» را به اتهام همکاری با ایران تحریم کرد.
واشنگتن همچنین تحریم‌های جدیدی را علیه کوبا اعمال کرد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23391" target="_blank">📅 21:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ :تصمیمات آتی را با 6 کشور عربی خلیج فارس و اعضای شورای امنیت سازمان ملل بررسی خواهیم کرد.امیدوارم ناتو از فاز بی مصرف بودن خارج شود وگرنه دیگر برای آنان هیچ هزینه‌ای نمیکنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23390" target="_blank">📅 21:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">واشنگتن با فروش احتمالی ۴۸ فروند جنگنده از نوع F-35 به عربستان سعودی موافقت کرده است. ارزش این قرارداد حدود ۲۴.۳ میلیارد دلار تخمین زده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23389" target="_blank">📅 21:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سی‌بی‌اس
: سپاه پاسداران انقلاب اسلامی در روزهای اخیر، حداقل دو فروند از هواپیماهای بدون سرنشین مدل MQ-1 متعلق به آمریکا را سرنگون کرده‌اند، اگرچه هنوز مشخص نیست این حوادث در کجا رخ داده‌اند و کدام مدل خاص از این هواپیما درگیر بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23388" target="_blank">📅 21:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ به آکسیوس : می‌خواهم از جلسه عمومی سازمان ملل (هفته بعد) استفاده کنم تا مستقیماً از متحدان منطقه‌ای درباره گام‌های بعدی جنگ بشنوم @WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/23387" target="_blank">📅 21:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed20696f0.mp4?token=ddDmC7ky_uIwRmzo4dy3PjdRr48y2A2Y5AhBeChkCFpFTLWU8zzQXt5goXb5dqQJpmGcq-AJTR8hhbvzdjppLFRngdXco3jtQ5NcUGWdiq3xA91-E1DPQaKor8avkmPzyG8Mi92sIMfk3kL79g7LgQ8546aBZ_dZANWx0iavwz7vzbOwnUFJooY1RLKDB-fhudsy_LBw9fUyNNSacgMdyfwbJb5QOzJbBGAzKmABP7EZau5mF8m0_GxGNOfmqG2-Jg5wlwr4u_PHkGsDT8CgpFb9g9MkItZ4ztNgZqu8avsGgcwe6Gv0nS1pT1bUsNn0A_AsV5naD7hmNRSOqa5WYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed20696f0.mp4?token=ddDmC7ky_uIwRmzo4dy3PjdRr48y2A2Y5AhBeChkCFpFTLWU8zzQXt5goXb5dqQJpmGcq-AJTR8hhbvzdjppLFRngdXco3jtQ5NcUGWdiq3xA91-E1DPQaKor8avkmPzyG8Mi92sIMfk3kL79g7LgQ8546aBZ_dZANWx0iavwz7vzbOwnUFJooY1RLKDB-fhudsy_LBw9fUyNNSacgMdyfwbJb5QOzJbBGAzKmABP7EZau5mF8m0_GxGNOfmqG2-Jg5wlwr4u_PHkGsDT8CgpFb9g9MkItZ4ztNgZqu8avsGgcwe6Gv0nS1pT1bUsNn0A_AsV5naD7hmNRSOqa5WYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر شبکه فاکس‌نیوز از بمب‌های سنگرشکن و ۲۰۰۰ پوندی آمریکایی داخل ناو جورج واشنگتن تا دندان مسلح برای حمله به ایران
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/23386" target="_blank">📅 20:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آکسیوس به نقل از مقام آمریکایی: نیروهای آمریکایی مستقر در خاورمیانه برای احتمال یک درگیری تمام‌عیار با ایران در آماده‌باش هستند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/23385" target="_blank">📅 20:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23384">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ به آکسیوس : «آیا وارد شوم و آنها [رژیم ایران] را نابود کنم یا نه؟ این یک تصمیم بزرگ است. هر اتفاقی ممکن است از سوی من رخ دهد.»  @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/23384" target="_blank">📅 20:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ به نشریه "اکسیوس" گفت: من در آستانه اتخاذ یک تصمیم مهم در مورد ایران هستم. @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/23383" target="_blank">📅 20:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ به نشریه "اکسیوس" گفت:
من در آستانه اتخاذ یک تصمیم مهم در مورد ایران هستم.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/23382" target="_blank">📅 20:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نماینده ویژه سازمان ملل متحد در سوریه: اسرائیل، تقریباً به صورت روزانه، در جنوب سوریه نفوذ می‌کند، موانع مرزی ایجاد می‌کند و با توپخانه شلیک می‌کند، همچنین بازدید نتانیاهو از نیروهای اسرائیلی در کوه شیخ، یک نقض دیگر از حاکمیت سوریه است.
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/23381" target="_blank">📅 20:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23380">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیروی دریایی بریتانیا اعلام کرد گزارشی درباره وقوع یک حادثه در فاصله ۷۵ مایل دریایی شرق عدن در یمن دریافت کرده است.بر اساس این گزارش، یک قایق اقدام به تعقیب یک نفتکش کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/23380" target="_blank">📅 19:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23379">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سنتکام: فرماندهی مرکزی ایالات متحده اعلام کرد که ارتش آمریکا در راستای اجرای محاصره دریایی و تضمین رعایت قوانین، تا امروز در مجموع به ۱۰۴ کشتی که در تلاش برای نقض این محاصره بودند، دستور تغییر مسیر داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/23379" target="_blank">📅 19:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvUOnoTEnOXOM5zltX65TWnEEN8HC5KQ1bUicoS613lWDQ3olwP3Yk9fdX4yf2UzHlG4J-cYere6TbykuJkViivVWbodYtiRGGENrhxxmMkX5FrooEQ4ublVMMSHZ7_-ZSD0uRddjqOdq3giID-Zcs-rzZ5Tt2YLhPQkIBjxFyoi4pQ9Yl3cE6GH21X_SVhLLUc0ZNr_HsQ-OiNxwkkGB8qZ752xDsBjbbYkOT7Q1xZv96NJqpn9xgWkdVkGZtOPwFkdG5f2Kh_--MoJTX74ciewwJEOmNsJrFH8I6dhHP0MCZo48K_zgTT9GFiQgSoKzFERQroM7djwomABVSD2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار :
تصاویر ماهواره‌ای جدید نشان میدهد
ایران در حال بازسازی سریع تأسیسات طالقان ۲ است:
تصاویر ماهواره‌ای شرکت وانتور از ۱۳ سپتامبر ۲۰۲۶ نشان می‌دهد ایران بازسازی تأسیسات طالقان ۲ در مجموعه نظامی پارچین حدود ۳۰ کیلومتری جنوب‌شرق تهران را با سرعت پیش می‌برد. ایران روی بخش تخریب‌شده و مدفون تأسیسات یک پوشش برزنتی نصب کرده تا فعالیت‌های بازسازی زیر آن از دید ماهواره‌ها و شناسایی هوایی پنهان بماند. در محل، کامیون‌های حمل خاک، بولدوزر، پمپ و کامیون بتن و جرثقیل‌ها فعال هستند. بازسازی از ژوئن آغاز شد و ابتدا سوراخ‌های ایجادشده بر اثر اصابت چند بمب سنگرشکن (بمب مخصوص حمله به تأسیسات زیرزمینی) با بتن ترمیم و پوشانده شد. همچنین یک سازه بتنی تقویت‌شده جدید در سمت راست تأسیسات ساخته شده و سازه مشابه در سمت چپ که در ژوئیه شناسایی شده بود، اکنون ظاهراً تکمیل شده است. این سازه‌ها حفاظت بیشتری در برابر انفجار و حملات هوایی ایجاد می‌کنند
با این تصاویر الان مشخص می‌شود که
ستون دود امروز در پارچین برای باز کردن حفره‌های مسدود شده و عملیات بازسازی در این تأسیسات
می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/23378" target="_blank">📅 19:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIw1wRnOrZH1Swyj9cN2-C02iqXK04IzFLJMXAFJK9plyV-q6DkL4BMqCfTXg9n5vv-I13xFUJT7XvAgOe2SiYLy9SoRV0bB1s76gsUOQM5CY9R0f6aRn3T-iu7Q01_z6gSK_MYrFRCd3RdTA_leXWaIIzCbEm3nDnGy9xVjaXuFlo0UTmwP3qGP570jiU1jcmoAsSvktXTdJRJl4hyxONiujumzdbOXrujdx3Z81iaHXEZ4HLisvbsqLlGDe0fGWHeusEolIyCDtgSOTG5Q4vPcopFcAQPGc0kPIaJOBDODbqB9QJXwAr_Fo81-3xAdi_IiJqdfQ8j3U1_hFIDHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر تبلیغاتی جان فدا در تهران، آموزش رایگان سیستم‌های دفاع هوایی دوش پرتاب (MANPAD) را به شهروندانی که مایل به داوطلب شدن هستند، ارائه می‌دهد.
@WarRoom
😟</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/23377" target="_blank">📅 19:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23376">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مسعود بهنود روزنامه‌نگار قدیمی و ریاکار که در دو جنگ دوازده روزه و ۴۰ روزه هم حامی حکومت بود، خبر داد تا پیش از نوروز به ایران باز می‌گردد وی سابقه طولانی در همکاری با رسانه‌های خارج از ایران، از جمله به عنوان سردبیر و تهیه‌کننده در بخش فارسی بی‌بی‌سی دارد…</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/23376" target="_blank">📅 18:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رویترز: در پی درخواست عربستان سعودی از پکن پس از حمله نظامی برق‌آسای حوثی‌ها در هفته گذشته، چین مخفیانه از تهران برای آرام کردن شورشیان حوثی در یمن درخواست همکاری کرده است. @WarRoom</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/23375" target="_blank">📅 18:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جمهوری اسلامی عضویت آمریکا در شورای حکام را مغایر اساسنامه آژانس بین المللی انرژی اتمی دانست
هیأت جمهوری اسلامی امروز در بیانیه‌ای ذیل بند هشتم دستور کار این کنفرانس با عنوان «انتخاب اعضای شورای حکام» تأکید کرد که حضور آمریکا در این شورا، به کشور متجاوز اجازه می‌دهد درباره موضوعاتی داوری کند که مستقیماً با اقدامات غیرقانونی خودش مرتبط است
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/23374" target="_blank">📅 18:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">به گزارش وال‌استریت ژورنال،
جنرال موتورز (مالک شورولت، کادیلاک، جی‌ام‌سی، بیوک و هامر)
برای نخستین‌بار برای
لاکهید مارتین
قطعات بدنه موشک‌های رهگیر
پاتریوت PAC-3 MSE
تولید کرده و نخستین محموله را در ماه اوت تحویل داده است. این همکاری با هدف
افزایش سریع تولید موشک‌های پدافندی آمریکا و جبران کاهش ذخایر
انجام می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/23373" target="_blank">📅 17:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d12eec9e29.mp4?token=GinYBwbyvpN2h1Cd7xPkZHzKd19ddcvjYlieRmt6EzXAHgU62Q-vur1oEqaN2Gz4YVmtEylfWWcgj829zJI66YXUAqi0k7JMbXDbAStiR3wFwJP5TpfX7Gt-h4KEBBDuUuphJXDc-hPdqjchBH1WKhsyFCs_obapW6yGsBWoSMV9Y9FmwvWCHrcCEEcvpVX8MTDQMTYC5RvEGDVzLyQ4cVF3b-fBUt9GEebitBu6ZU3tFG25nB_htzPZDgKZ9SU0X8zFEOwJBBiVWwz0wF6T8kGv2WQvjJ3wrpqyxZNOBI64_OpWrw9QIaEdZgj9g5V5sqH_QW5Hmwv-jMWc9DSlww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d12eec9e29.mp4?token=GinYBwbyvpN2h1Cd7xPkZHzKd19ddcvjYlieRmt6EzXAHgU62Q-vur1oEqaN2Gz4YVmtEylfWWcgj829zJI66YXUAqi0k7JMbXDbAStiR3wFwJP5TpfX7Gt-h4KEBBDuUuphJXDc-hPdqjchBH1WKhsyFCs_obapW6yGsBWoSMV9Y9FmwvWCHrcCEEcvpVX8MTDQMTYC5RvEGDVzLyQ4cVF3b-fBUt9GEebitBu6ZU3tFG25nB_htzPZDgKZ9SU0X8zFEOwJBBiVWwz0wF6T8kGv2WQvjJ3wrpqyxZNOBI64_OpWrw9QIaEdZgj9g5V5sqH_QW5Hmwv-jMWc9DSlww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : ستون دود عظیم و قارچی شکل ، مشهد شهرک شهید رجائی ، صدای انفجار هم  اومد ، محدوده جایگاه سوخت جت مصطفی خمینی
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/23371" target="_blank">📅 16:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کاهش قیمت نفت با تغییر مسیر صادرات عربستان
قیمت نفت پس از گزارش‌هایی درباره انتقال بخشی از نفت عربستان به آسیا از مسیر
عمان
کاهش یافت. عربستان در دوره تعمیر خط لوله «شرق به غرب» قصد دارد بخشی از نفت را با
انتقال کشتی‌به‌کشتی در نزدیکی بندر صحار عمان
به پالایشگاه‌های آسیایی برساند؛ اقدامی که نگرانی‌ها درباره اختلال در عرضه جهانی را کاهش داده است. نفت برنت با ۳.۵
درصد کاهش به ۱۰۲.۲۸ دلار
در هر بشکه رسید.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/23370" target="_blank">📅 16:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بنیاد دفاع از دموکراسی‌ها (FDD) می‌گوید طی شش ماه گذشته دست‌کم
۲۵ افسر و فرمانده نظامی و امنیتی سوریه
در مواردی که علت مرگشان
«حمله قلبی» یا «ایست قلبی»
اعلام شده، جان باخته‌اند. FDD تأکید می‌کند
هیچ مدرکی برای ارتباط این مرگ‌ها یا غیرطبیعی بودن آنها وجود ندارد
، اما سابقه حکومت اسد در اعلام «حمله قلبی» برای برخی زندانیان و مرگ‌های مشکوک باعث شده این موارد در سوریه حساسیت و شایعات زیادی ایجاد کند. برخی احتمال می‌دهند این مرگ‌ها با
تغییر ساختار ارتش و کنار گذاشته شدن فرماندهان سابق شورشی
مرتبط باشد، اما سوابق قربانیان چنین الگوی مشخصی را تأیید نمی‌کند. دولت سوریه نیز تاکنون توضیح جامعی درباره این روند ارائه نکرده است. FDD نتیجه می‌گیرد که مشکل اصلی،
بی‌اعتمادی تاریخی به روایت رسمی حکومت
است؛ به همین دلیل «حمله قلبی» برای برخی سوری‌ها اکنون می‌تواند معنایی فراتر از یک علت پزشکی داشته باشد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/23369" target="_blank">📅 16:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23368">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSh9VrFkv7hzgN5wWHbTADxp9tYJX3_c3YEq0BQ36nhj5CJipCgl12FaKKDAY3SyqptXTG4av1tnR5fRokWHW0OA_IBAEsW2WM9ZkWE35a9Rg2o3OPO3qfHd-cFXjPiQ8NthbZGCBit79wf2j5KIiUsajyNtkWq3JO4eI0Lg2ycoDpTcelfjWtF-do_-eizqe1kAuhPr5CL0LorO-J23RfWtUYDJ2TsmsXqpAoyqNvr6CdltB8x69RWEdBmAwyqrQhbOkzuhj0vRKj078s74FoFs-hnCAHX0dNtZaFUxNf3j499HlLCaCAMN-_K78ZTiJaBXA1gSpHeQo4hlfn5N2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود بهنود روزنامه‌نگار قدیمی و ریاکار که در دو جنگ دوازده روزه و ۴۰ روزه هم حامی حکومت بود، خبر داد تا پیش از نوروز به ایران باز می‌گردد
وی سابقه طولانی در همکاری با رسانه‌های خارج از ایران، از جمله به عنوان سردبیر و تهیه‌کننده در بخش فارسی بی‌بی‌سی دارد
@WarRoom</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/23368" target="_blank">📅 16:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رویترز: در پی درخواست عربستان سعودی از پکن پس از حمله نظامی برق‌آسای حوثی‌ها در هفته گذشته، چین مخفیانه از تهران برای آرام کردن شورشیان حوثی در یمن درخواست همکاری کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/23367" target="_blank">📅 15:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNn_BBE03YLEm7ME5gmCZ8TGKOzsMn5WrPqmk2RgwZ8slofnKcI7zpNZkrDU_AnUwW2YyCXYGs5_ReFpkIlgZn3kvKeth2dgFkHhqrz8ejZNHmi88j27eO-R34k1vRqdoyM-tCGO1mnuM5jggUKS6LbGON-T-wf379iU8OFruEUfUsXsDjqKHDnYiR5153qjk6K4Hy43FCrKjXRJNslPq_H8vklKRiUe3smM7Up0ULky0oNSzfCc_2aTpktXZhW34QNJJQ5Wikd1Sm2PUmBjKK6OawVOloFO5Wcsa97YeAerH5YKeoMxOzTvvFFCO1q2cevRA1qw63sZ0dJgLpfbJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ستون دود تهران پارچین
@WarRoom</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/23366" target="_blank">📅 15:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7807d87071.mp4?token=RX0CMNeQumer1u3niCEC4Kb6q3DgGuYQdqlqfCraRBMk1ChmkBrQVuP5JyWj8cSzeyxtdBxG5E-GdFm7UOXYtaU0b0UIp0AENxwWIPM6fpV1kjHzP6KwRHPsphVDNEmZC-zjLL0RtnaRTjJdUU6E-tKJpJPcZEkNAM2mtG6rhCcCtMY6NwegVOKH9lz1k0_z_81u2i-7crJXpWxH1p5xPYxJ9_KdzkdNW0IFPZLN1i5FkHYPuNcdK7O9OvgsEPpo4vG9KYVG1W2lKcelt8K02RtY8Pb9s1Y1Q2hrE7YVKSV5JcCsb8fmNJ886T2rTUqQFlg6s7608sIVfws_SWpIag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7807d87071.mp4?token=RX0CMNeQumer1u3niCEC4Kb6q3DgGuYQdqlqfCraRBMk1ChmkBrQVuP5JyWj8cSzeyxtdBxG5E-GdFm7UOXYtaU0b0UIp0AENxwWIPM6fpV1kjHzP6KwRHPsphVDNEmZC-zjLL0RtnaRTjJdUU6E-tKJpJPcZEkNAM2mtG6rhCcCtMY6NwegVOKH9lz1k0_z_81u2i-7crJXpWxH1p5xPYxJ9_KdzkdNW0IFPZLN1i5FkHYPuNcdK7O9OvgsEPpo4vG9KYVG1W2lKcelt8K02RtY8Pb9s1Y1Q2hrE7YVKSV5JcCsb8fmNJ886T2rTUqQFlg6s7608sIVfws_SWpIag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تمایل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ فقط تضعیف شده است.
توانایی آن‌ها برای عملی کردن این هدف، اساساً به‌شدت آسیب دیده است. ما وظیفه خود را انجام داده‌ایم، اما هنوز کارهای بیشتری برای تکمیل باقی مانده و آن‌ها را تکمیل خواهیم کرد. ما حماس را از بین خواهیم برد. همچنین ابتدا رژیم ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/23365" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امروز، دومین سالروز بزرگداشت عملیات فرخنده «پیجر» در لبنان است؛ عملیاتی که در ۱۷ سپتامبر ۲۰۲۴ انجام شد
دو سال پیش در چنین روزی هزاران دستگاه "پیجر" در مناطق مختلف لبنان و بخش هایی از سوریه منفجر شدند ، این دستگاه ها توسط نیروهای حزب الله و سپاه استفاده می شدند
@WarRoom
🎂
🍬
💥</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/23364" target="_blank">📅 15:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJ6uBiDUMqGwTDPcRZOICrYzs-Lq2fEVs3sONqrMGFg479Zvx6F-zTzgcFq-LX3z_egkRHcroW4dXenoFDUNpMibk4-2FQZ1XHGqRcjyUU6HPts9s4Jv-poTGAhxDysulc27MjNrWm22IK0NMvrY8hAOdeemZ_MWi705PUQLgEN5Fz-fA6A4pBhZHGxGrFJVcOICJqnG5pgf4BAAeJwgkYdevcx7dQXjnJtq3Cwdf46BmInTb2MYhwe46kvn0Fws3hYl14UqoRiEWIuSS4MVM81CArHFOtLUM619X296ZkXvGkbReAAx9NSrf-X3g3FPTcUkbuA1LQe3AMixcxnteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار :
پرواز مشکوک
یک فروند
CMV-22B اوسپری
با کال‌ساین
MEDEVC11
از روی یکی از ناوهای آمریکایی مستقر در
دریای مکران
به پرواز درآمده و در حال حرکت به سمت یکی از کشورهای حافظ منافع آمریکا در خلیج فارس . استفاده از عبارت
MEDEVAC
در ارتش آمریکا نشان می‌دهد پرواز با مأموریت تخلیه یا انتقال پزشکی انجام می‌شود؛ بنابراین یکی از احتمالات، انتقال پرسنلی است که پیش‌تر مجروح یا دچار مشکل پزشکی شده است. با این حال، از روی کال‌ساین به‌تنهایی نمی‌توان تأیید کرد که فرد در جریان حادثه جدید آسیب دیده یا قرار است پس از درمان به مأموریت بازگردد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23363" target="_blank">📅 15:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23362">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وزیر جنگ اسرائیل، کاتس:
به رژیم ایران یا هیچ گروه دیگری اجازه نخواهیم داد که حماس را دوباره مسلح کند. اگر اردوغان می‌خواهد به آن‌ها کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما او هرگز پایش را به غزه نخواهد گذاشت. نبرد با ایران و جبهه‌های دیگر همچنان ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/23362" target="_blank">📅 14:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEznzxb8GBr2sweV-N8cY5BCCt-y7yJNiOmVVY60F9Na0-KUwYBQzMjkNI50_S9fi6nBxEOEvzlgSSIOnMx6DiNOPIlZfTy0QBDAkVs-dkOQCEM1JhYL4B2x_KB1hX4voK4DphWoJSp4GpGQVBnT1jtCKScbm0joYLVflKr6GNmT0viy7J5c5_u7OFbqrDw8x-0CqBNnGsOGl5wOcsKHvHIjXBxZgEOqQFO-lzdaJ6ke8hXxD_SZY84hiNINsoBPgEm40QuAwpOUxDHPPAOUDtfGOS883CeMD4bYsV8OZrBITbXRFjQRyjkVbB7fHbMAxnSfpqhCTavkMuxU59UM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ۱۰ فروند F-16C متعلق به یگان ۱۴۸ جنگنده مینه‌سوتا (یک واحد عملیاتی نیروی هوایی آمریکا در ایالت مینه‌سوتا) صبح امروز از پایگاه لاجس پرتغال (LPLA) به سمت منطقه سنتکام حرکتکردند و با پشتیبانی سوخت‌رسان‌ها همراه هستند. این انتقال شامل دو سل(گروه پروازی) پروازی است: سل اول با F-16های TREND71 تا TREND76 و دو فروند KC-46A با کدهای BORA24 و BORA25؛ سل دوم با F-16های TREND81 تا TREND84 و دو KC-46A با کدهای BORA34 و BORA35. شماره بدنه‌های اعلام‌شده F-16ها شامل 91-0336، 91-0405، 91-0421، 91-0349، 90-0831، 91-0339، 92-0915، 91-0341، 91-0347 و 91-0406 است. شماره بدنه KC-46A با کد BORA35 هنوز تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23361" target="_blank">📅 14:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">علت گزارشهای انفجار دیشب تهران
بامداد پنجشنبه، انفجار و آتش‌سوزی در یک ساختمان پنج‌طبقه مسکونی در
محله فلاح تهران
رخ داده است. انفجار باعث آتش‌سوزی کامل یک واحد حدود ۷۰ متری و تخریب بخشی از دیوارهای سه واحد و چاهک آسانسور شده و حتی به ساختمان مجاور نیز خسارت زده است. حدود
۱۲ نفر
از ساختمان خارج شدند و یک جوان
۲۴ ساله
مصدوم شد. به گفته سخنگوی آتش‌نشانی تهران، علت حادثه
نشت گاز شهری از یکی از وسایل و ایجاد جرقه
اعلام شده است
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/23360" target="_blank">📅 14:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23359">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عربستان برای مقابله با حوثی‌ها به دنبال تشکیل ائتلاف منطقه‌ای و بین‌المللی است؛ ریاض از پاکستان، ترکیه، مصر و کشورهای غربی درخواست حمایت کرده است
آسوشیتدپرس به نقل از دو مقام منطقه‌ای گزارش داده عربستان سعودی که با کمبود موشک‌های رهگیر مواجه شده، از
فرانسه، بریتانیا، پاکستان و مصر
خواسته است برای مقابله با حملات موشکی و پهپادی حوثی‌ها،
سامانه‌های پدافند هوایی در منطقه مستقر کنند
. عربستان همچنین در تلاش است یک واکنش جمعی علیه حوثی‌ها شکل دهد؛ با این حال، منابع تأکید کرده‌اند که فعلاً
هیچ‌یک از این کشورها اعزام نیروی نظامی برای ورود مستقیم به جنگ را اعلام نکرده‌اند
و تلاش‌های دیپلماتیک مصر و عمان برای کاهش تنش ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23359" target="_blank">📅 13:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47dac3f1f6.mp4?token=ZRm5ZoLNz6eDgAvTay12mQ_gKVcTiLBM-NXL2KDCwD8k0YUmK-q0S4wfYgCoW5HH02pTdAejrl2f-y9kimgdf-7P5KLH1XDsIFaGRGM98meqFyVImaWqoP2gg15g0WvmHXTdchXhmV04aVq0cHYhWEOVp5YL0SL3zathITMHYHlVXgbtniBn-SmsuhpQQqjF6J5PtuR9iynziZl1dDLaSS62mUC1j-D7GB8_75ZEBhFtHARHusin3t0aTmV8Kg-Ecg6Z8PNTz5y_S4ka-E13SwTVrqOjrZpmR_GDjTNSGfGz6oK57uZ19G5s6jPa1Fd9_K4VmxlHdOhQDeVH3hvme1rZSwmW2zesoDcyV59sEazlAQQQYzPuaxb9XewkeThHM1QXL9uc7qsk8TyMim5qLIyTXtVf08eWtoNa9S22xqujv2aWNIdodcmD8W2vqutCLi3KlgjV6e8PrxYo5jcSAyWoL3EDtAXiBQhbjpF6JufYOzr3uQraErrvIUy90ZTswJZTTIeZVqcO1tbWcsdW69nAugd3csCbQp2386B17drNgrijn5c_N6J9CONXXnWOPLnmhoFyN4LMkOIQ6Mc2027t8WtON6tzZ3Z0NLZbYfzmqMcOmozoNaPfDonXRKRgPgMEKUe09QAOSEzVTcjhgxchela4e2Ahl81ba1duOVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47dac3f1f6.mp4?token=ZRm5ZoLNz6eDgAvTay12mQ_gKVcTiLBM-NXL2KDCwD8k0YUmK-q0S4wfYgCoW5HH02pTdAejrl2f-y9kimgdf-7P5KLH1XDsIFaGRGM98meqFyVImaWqoP2gg15g0WvmHXTdchXhmV04aVq0cHYhWEOVp5YL0SL3zathITMHYHlVXgbtniBn-SmsuhpQQqjF6J5PtuR9iynziZl1dDLaSS62mUC1j-D7GB8_75ZEBhFtHARHusin3t0aTmV8Kg-Ecg6Z8PNTz5y_S4ka-E13SwTVrqOjrZpmR_GDjTNSGfGz6oK57uZ19G5s6jPa1Fd9_K4VmxlHdOhQDeVH3hvme1rZSwmW2zesoDcyV59sEazlAQQQYzPuaxb9XewkeThHM1QXL9uc7qsk8TyMim5qLIyTXtVf08eWtoNa9S22xqujv2aWNIdodcmD8W2vqutCLi3KlgjV6e8PrxYo5jcSAyWoL3EDtAXiBQhbjpF6JufYOzr3uQraErrvIUy90ZTswJZTTIeZVqcO1tbWcsdW69nAugd3csCbQp2386B17drNgrijn5c_N6J9CONXXnWOPLnmhoFyN4LMkOIQ6Mc2027t8WtON6tzZ3Z0NLZbYfzmqMcOmozoNaPfDonXRKRgPgMEKUe09QAOSEzVTcjhgxchela4e2Ahl81ba1duOVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادثه برای یک کودک کار که میخواهد از سطل آشغال زباله بردارد. واقعا وضعیت در ایران دردناکه…
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23358" target="_blank">📅 13:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بحران در ایران‌ایر؛ ۹ هزار پرسنل برای تنها ۸ هواپیمای عملیاتی
طاهر عبدالحی، مدیرعامل ایران‌ایر، اعلام کرده این شرکت اکنون حدود
۹ هزار نیروی شاغل، نزدیک به ۱۳ هزار بازنشسته و مستمری‌بگیر و تنها ۸ هواپیمای عملیاتی
دارد. او وضعیت هما را «فلج» توصیف کرده و گفته این شرایط نتیجه چند دهه سیاست‌گذاری نادرست، هزینه‌های تحریم و مشکلات صندوق بازنشستگی است. مدیرعامل ایران‌ایر همچنین گفته
۱۰ هواپیمای عملیاتی این شرکت در جنگ اخیر آسیب دیده‌اند
و شمار هواپیماهای آسیب‌دیده ایران‌ایر در نقاط مختلف کشور ممکن است به
۲۰ تا ۳۰ فروند
برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23357" target="_blank">📅 13:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رویترز: بحران اقتصادی ایران، مهاجران افغانستانی را به بازگشت به کشورشان واداشته
افزایش شدید قیمت‌ها و کاهش ارزش ریال باعث شده پس‌انداز بسیاری از مهاجران افغانستانی در ایران از بین برود و درصدی از آن‌ها تصمیم بگیرند به کشورشان بازگردند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23355" target="_blank">📅 12:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23354">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وانجون شی (Wanjun Xie)، فعال مخالف حکومت چین و رئیس حزب دموکراسی چین مدعی شده شی جین‌پینگ در جریان اجلاس بریکس در دهلی نو دچار غش و سپس سکته مغزی ایسکمیک شدید شده و برای درمان به بیمارستان ۳۰۱ پکن منتقل شده است. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23354" target="_blank">📅 12:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23353">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وانجون شی (Wanjun Xie)
، فعال مخالف حکومت چین و رئیس حزب دموکراسی چین مدعی شده شی جین‌پینگ در جریان اجلاس بریکس در دهلی نو دچار غش و سپس
سکته مغزی ایسکمیک شدید
شده و برای درمان به بیمارستان ۳۰۱ پکن منتقل شده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23353" target="_blank">📅 12:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23352">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مکرون: اولویت ما، احیای آزادی کشتیرانی در تنگه هرمز است
رئیس‌جمهور فرانسه اعلام کرد
اولویت فرانسه، احیای آزادی کشتیرانی در تنگه هرمز، حفاظت از زیرساخت‌های انرژی و تضمین امنیت تأمین منابع است.
مکرون همچنین از
گفت‌وگو با مقامات عراق، عربستان و قطر
خبر داد و گفت فرانسه برای کاهش وابستگی به هرمز، ایجاد مسیرهای جایگزین انتقال نفت و کاهش فشار بر قیمت سوخت تلاش می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23352" target="_blank">📅 11:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23351">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تنگه صدای مذاکرات میاد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23351" target="_blank">📅 11:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23350">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpQ0TUe-dGDpxJ04h94Itm3YOEEpOH5UozAb1tyAkj7gABk1KIVhpYGJPrRyeWYKLvZU66XkHGWEt6bWFuRDHFk6rMRw_NZyEf1k4Nt5FzRmb6OzyJpOuJCzR1IYaNZU9FlQFxjXeCLd_6No0fzqQSBkMmj0Tw3dw1yVIi4g40nDgGQfhFHvKmlG3PB0G0l8bqCCkEbGXo2vlqyFjyOIPu7UN5TGLRilp3lm9PL6zgT2ntRVH7mk0be3oO5OaKsmKoGntaZyTl9i5xuf1D1Z1Yty8sR5dU8Cd8Ff2hhrIZLMQ_tUQ7---am239DHVeoKzVQBUj9l8GlYKFx4l_W8bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز ۲۶ شهریور؛ زادروز «کمبوجیه دوم» پسر ارشد کوروش بزرگ است که در ایران باستان این روز به عنوان روز پسر شناخته میشود
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23350" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23349">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حقیقت‌یاب اتاق جنگ: ویدئوی منتشرشده از دیوید کیس، سخنگوی سابق نتانیاهو قدیمی است و مربوط به ژوئن ۲۰۲۵ است. کیس در این ویدئو مدعی شده بود جمهوری اسلامی «ظرف چند هفته» سقوط خواهد کرد و حتی زمان آن را دقیقاً دو هفته، سه روز، شش ساعت و چهارده دقیقه اعلام کرده…</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23349" target="_blank">📅 10:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23348">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCqy3c8RqEXhW0ELHdljAAOoR_GMe3OGTrXfz5x7Vs7bS_pSsVJW-Ma4fjFDlhhG9VKMnvxuJLcRsYURnerRRhZicteL-oPJlzqL0wbgvVtF0lML2z8E-b_h3ix-KGqJpi77DdK9FOeqTSrxQ0PzApat9asl5A1w3tz9zuejhGaDkVH7j9kjyaM8N7r-O0r2_bV2G-IdHgP3PzJq8MpSBRuZgdwHT_ONyEk_b-QB5et-lPmG2C3MrBJ2r1g0_uk1f6V0gOqwXvyW-xcDEAu1_7q-c-d_KfrcsP5XxbeESZz9lZNEeFW6tchAO569kQLnBznXffKJeQfsLlJvRzlWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت جدید از فروپاشی ساختمان «السعدا» در غزه؛ یکی از قربانیان محافظ اسماعیل هنیه بود:
در حادثه فروپاشی ساختمان «السعدا» در شهر غزه که به کشته‌شدن ۲۱ نفر منجر شد،
محمود سعدا
، یکی از قربانیان، از
محافظان اسماعیل هنیه
، رئیس سابق دفتر سیاسی حماس، بوده است. منابع مخالف حماس ادعا می‌کنند علت فروپاشی ساختمان، وجود یک
تونل قدیمی حماس در زیر آن
بوده که اخیراً «بهسازی» شده است. به گفته این منابع، این همان تونلی است که پیش‌تر
جمال زبده
، از مقام‌های ارشد حماس و مسئول توسعه موتورهای موشکی این گروه، به همراه
باسم عیسی
، فرمانده حماس در شهر غزه، و چند مقام ارشد دیگر در آن کشته شدند.رویترز نوشته بود ساختمان هفت‌طبقه پیش‌تر در حملات هوایی آسیب دیده بود و ساکنان آواره شامل زنان و کودکان در آن زندگی می‌کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23348" target="_blank">📅 10:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23347">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">واشنگتن پست:ذخایر موشک‌های پدافندی عربستان سعودی رو به اتمام است، که این امر باعث شده تا این کشور برای دریافت کمک از متحدان منطقه‌ای و غربی خود درخواست کند.در حال حاضر، مصر و عمان تلاش‌های میانجی‌گری با حوثی‌ها را بر عهده دارند، و این در حالی است که هدف فعلی، دادن فرصت به دیپلماسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23347" target="_blank">📅 09:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23346">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ سه‌شنبه با کشورهای خلیج فارس درباره جنگ ایران دیدار می‌کند
اکسیوس به نقل از سه منبع آگاه گزارش داده دونالد ترامپ قرار است
سه‌شنبه ۲۲ سپتامبر
در حاشیه مجمع عمومی سازمان ملل در نیویورک با رهبران یا وزیران خارجه شش کشور عضو شورای همکاری خلیج فارس دیدار کند. عربستان، امارات، قطر، بحرین، کویت و عمان در این نشست حضور خواهند داشت و محور مذاکرات،
مرحله بعدی جنگ ایران و طرح آمریکا برای دوران پس از جنگ
خواهد بود. وزارت خارجه آمریکا دعوت‌نامه‌های اولیه را برای این کشورها ارسال کرده و احتمال حضور کشورهای عربی و اسلامی دیگر نیز مطرح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23346" target="_blank">📅 09:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23345">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb2fa5d29.mp4?token=DdxK0vllbUk0jU4lr4POHIHZyzDk20A-sqBEIbzR-_2G4PZVyw_iWTWLkVmlUvKeMhYo8kOBdgMSmslUoVZLZZ8xWUYOEefBe91JKkNgWcNfKvyin0vpYxyJgYjifpSumwcqrUV6fLfTf1_tFxv455MFtaZJ6SjrVQe14q2ft7RJbw1N7xe97fBvM7UEm6Wdc6mP2-pEhHJ8fh8yGf7g8GKIHmL7FIW5hrbGhatk8B197rPf2kQAPfV0ECnO1YlVbOBqMeDkbM2gK2UNppR3HvxVbrUjUakb8B6qH8MuxgUVH2OJBUoceOhbRpRkWjeRx3_lfyyxhhHStU_3SSD1Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb2fa5d29.mp4?token=DdxK0vllbUk0jU4lr4POHIHZyzDk20A-sqBEIbzR-_2G4PZVyw_iWTWLkVmlUvKeMhYo8kOBdgMSmslUoVZLZZ8xWUYOEefBe91JKkNgWcNfKvyin0vpYxyJgYjifpSumwcqrUV6fLfTf1_tFxv455MFtaZJ6SjrVQe14q2ft7RJbw1N7xe97fBvM7UEm6Wdc6mP2-pEhHJ8fh8yGf7g8GKIHmL7FIW5hrbGhatk8B197rPf2kQAPfV0ECnO1YlVbOBqMeDkbM2gK2UNppR3HvxVbrUjUakb8B6qH8MuxgUVH2OJBUoceOhbRpRkWjeRx3_lfyyxhhHStU_3SSD1Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: من آدمی با ضریب هوشی بالا هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23345" target="_blank">📅 08:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23344">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1026f97d.mp4?token=nqzi1NhHGTSDc3s3Yfrl2ry0m-HSUQXFvK7lrW52Qc1uGi3a9CT51DBJdPACxMRtjmRzx6XS3pyRpewB4AlYZh-X72VvgleEfHlCgaxjVP_0vxHXhNyWub33J9qPHMAGocSwmxu8yMgegsBfGLPi8rPWhCxmUyxm_1cfFkFJZuKkHDZHMZVsRBvUByntBqF_9gtmoA6ed799OKwSRWrDJFgiy-kGuJQkVRPVwkwe5c74PQP54OBSYT9EL5NbcpZRqlDmOoN-sAkqWBGQ2PN5xDzI-pA1RcMbOxUKj5x4wycKukwEGzeNMfh0D2SIowpQ2T01XpcTwomG6pUB3Pn5TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1026f97d.mp4?token=nqzi1NhHGTSDc3s3Yfrl2ry0m-HSUQXFvK7lrW52Qc1uGi3a9CT51DBJdPACxMRtjmRzx6XS3pyRpewB4AlYZh-X72VvgleEfHlCgaxjVP_0vxHXhNyWub33J9qPHMAGocSwmxu8yMgegsBfGLPi8rPWhCxmUyxm_1cfFkFJZuKkHDZHMZVsRBvUByntBqF_9gtmoA6ed799OKwSRWrDJFgiy-kGuJQkVRPVwkwe5c74PQP54OBSYT9EL5NbcpZRqlDmOoN-sAkqWBGQ2PN5xDzI-pA1RcMbOxUKj5x4wycKukwEGzeNMfh0D2SIowpQ2T01XpcTwomG6pUB3Pn5TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ببینید چه اتفاقی برای ایران خواهد افتاد. پایان خیلی خوبی خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23344" target="_blank">📅 08:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23343">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f427520d32.mp4?token=PqD3-jspPz-YAFMObrV4d7biw_ZUeG1oyZwxODbcu_ncgXLUDOS9f7x4jgA5-rp_lmWUwbspoxvW9n6uQoFBe8XxiJBdYpmE4HK7wWTM-oz8Shmu4kLeJeYywYRznv1EDvOpBwJHxteU7hYpKDgtXt9omlTPLnnTNYwqk0LennL5vSpTQzX7E1St4YKUU6yuCoyjpnhz_JSBm8FncP-JcfBnj9R45AD4jMb9xM5ol3Kfu6uErA9BHQNskPROUlfHJgzCzZvHHcD72WkHNRDXwCxwJtVCqIRYbrmEQnlq_4dIAvm2XdTSq3F2-7ySWZnKDtfNG5elriGM-bwRePwiyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f427520d32.mp4?token=PqD3-jspPz-YAFMObrV4d7biw_ZUeG1oyZwxODbcu_ncgXLUDOS9f7x4jgA5-rp_lmWUwbspoxvW9n6uQoFBe8XxiJBdYpmE4HK7wWTM-oz8Shmu4kLeJeYywYRznv1EDvOpBwJHxteU7hYpKDgtXt9omlTPLnnTNYwqk0LennL5vSpTQzX7E1St4YKUU6yuCoyjpnhz_JSBm8FncP-JcfBnj9R45AD4jMb9xM5ol3Kfu6uErA9BHQNskPROUlfHJgzCzZvHHcD72WkHNRDXwCxwJtVCqIRYbrmEQnlq_4dIAvm2XdTSq3F2-7ySWZnKDtfNG5elriGM-bwRePwiyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ایران نمی‌تواند به این شکل ادامه دهد. کشورشان نابود شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23343" target="_blank">📅 08:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23342">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f449d446e.mp4?token=g6o62YcsyBw4ju1vDdKF3tk3pzafUnVW1Xg5Jpp6-wkkNJ-1M2BZ5UlmLfvCFnXqvwy7-55zjtrPBGSNCKrpqGKnkDhdsGCdAL4WxBKqVnueiVOSZcDns9tYtxLkfzq2HB6KRyDBiFSbZQ9xQOLUupGc0t9Q3Ehs8sBnc4wsz3sposJMZRhFm5QvruTmCk3AYs3rm0DjJhgLbiTLV188WLksc5cmNUA7vd4LJEZTrac5Xj5xJv3h0v8zjXqz4ljSSGPZR7n2SciytPtRGq5tvvkYv2XwS9ArU_iQwgnQfd_waWBf-khHxntL_CEeF1Vle5eq_kAIwyNQ5X8roNtSQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f449d446e.mp4?token=g6o62YcsyBw4ju1vDdKF3tk3pzafUnVW1Xg5Jpp6-wkkNJ-1M2BZ5UlmLfvCFnXqvwy7-55zjtrPBGSNCKrpqGKnkDhdsGCdAL4WxBKqVnueiVOSZcDns9tYtxLkfzq2HB6KRyDBiFSbZQ9xQOLUupGc0t9Q3Ehs8sBnc4wsz3sposJMZRhFm5QvruTmCk3AYs3rm0DjJhgLbiTLV188WLksc5cmNUA7vd4LJEZTrac5Xj5xJv3h0v8zjXqz4ljSSGPZR7n2SciytPtRGq5tvvkYv2XwS9ArU_iQwgnQfd_waWBf-khHxntL_CEeF1Vle5eq_kAIwyNQ5X8roNtSQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: قیمت بنزین بالاتر است. این بهای بسیار ناچیزی است که بابت کارهایی که انجام داده‌ایم می‌پردازید. این را به خاطر داشته باشید.
@WarRoom
(با مردم آمریکا است)</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23342" target="_blank">📅 08:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23341">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/633c533291.mp4?token=epimDx3-YBS9qrM5rrN-683ijGJyPKB29hb4sof5MD-hBWVw-GsJxOWqrrIUJYlMaPUXxnFRUc8bRS6c5b8rpWscXKlUro7AVStGhpjsKAzoN68J6Imqt-YD0LHQEGKwQvH0rIvoocmsdZRl2opcNRQ6Daj1AxgXj0KUf20kSNXrfXLrhTvf10RmUPFwXT0CKSZ6zJL8v6f0_jP7XPVB0qovgU_dpIfarpXOGfN7htOgrfwQzsNz44RwNPvTeI8wcvlYHb73MCoxhpeTlXYw2y4JzKccEYDOvA1tOz0Xe7SZNpPR4m0uP8Hr1yY3Md77UB45nGrkjXtJJe9PwO8ZZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/633c533291.mp4?token=epimDx3-YBS9qrM5rrN-683ijGJyPKB29hb4sof5MD-hBWVw-GsJxOWqrrIUJYlMaPUXxnFRUc8bRS6c5b8rpWscXKlUro7AVStGhpjsKAzoN68J6Imqt-YD0LHQEGKwQvH0rIvoocmsdZRl2opcNRQ6Daj1AxgXj0KUf20kSNXrfXLrhTvf10RmUPFwXT0CKSZ6zJL8v6f0_jP7XPVB0qovgU_dpIfarpXOGfN7htOgrfwQzsNz44RwNPvTeI8wcvlYHb73MCoxhpeTlXYw2y4JzKccEYDOvA1tOz0Xe7SZNpPR4m0uP8Hr1yY3Md77UB45nGrkjXtJJe9PwO8ZZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آنها تماس می‌گیرند و می‌گویند: «ما می‌خواهیم به توافق برسیم.» اما آنها هنوز آماده نیستند. ما هر زمانی که بخواهیم می‌توانیم به توافق برسیم.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23341" target="_blank">📅 08:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23340">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a920cfb96.mp4?token=dlyuNcXhZJUB2iXGwLu9UdbcSPppvs70yqPS0M5JfKQA4wPTwqFFXW8HibTMHyC5GMALk_weatGr0UHB1GD9kKJYwomby6a4LMUZUyNwAye307HXC7YZUuZ3NGcozQALP1HVI7H9icZIh70cCzY0zU1kuO3tCptwc7WUQtSgwJoVZVBeRL4wnJggCM14kSttUmkqY7WjZntUPZ6OY9dMrdJ9BmoT2jRBXmO5-XIss4kRqseMe9u9CQ59Li2W9kGhC3ebIs_iSyF4ReErxo7OOenIv41jEEBPb1O9oh1cUrrxFuyDI_fP5ICXy1Fr6kVOjqYd5LhOevoXELV1TJ2WLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a920cfb96.mp4?token=dlyuNcXhZJUB2iXGwLu9UdbcSPppvs70yqPS0M5JfKQA4wPTwqFFXW8HibTMHyC5GMALk_weatGr0UHB1GD9kKJYwomby6a4LMUZUyNwAye307HXC7YZUuZ3NGcozQALP1HVI7H9icZIh70cCzY0zU1kuO3tCptwc7WUQtSgwJoVZVBeRL4wnJggCM14kSttUmkqY7WjZntUPZ6OY9dMrdJ9BmoT2jRBXmO5-XIss4kRqseMe9u9CQ59Li2W9kGhC3ebIs_iSyF4ReErxo7OOenIv41jEEBPb1O9oh1cUrrxFuyDI_fP5ICXy1Fr6kVOjqYd5LhOevoXELV1TJ2WLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: دموکرات‌ها دوران تاریک آمریکا را برای ما به ارمغان آوردند و ما آن را به دوران طلایی آمریکا تبدیل کردیم. و آن جنگ، آن جنگ، خیلی زود به پایان خواهد رسید. تماشا کنید، فقط تماشا کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23340" target="_blank">📅 08:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23339">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آسوشیتدپرس : هرمز دوباره شاهد افزایش تردد نفتکش‌هاست
، عبور نفتکش‌ها از تنگه هرمز تا حدی افزایش یافته و برخی کشتی‌ها با استفاده از مسیر جنوبی نزدیک عمان و با راهنمایی نیروهای آمریکایی عبور می‌کنند. برآوردها اکنون حدود
۵ تا ۷ میلیون بشکه در روز
است، در حالی که پیش از جنگ حدود ۱۵ میلیون بشکه در روز از هرمز عبور می‌کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23339" target="_blank">📅 07:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23338">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مدیریت اتاق جنگ : گزارشهای زیاد شما دایرکت و منفجر کرده که تهران صداهای عجیب می‌آید، گزارش پدافند، صدای جنگنده و غیره. بررسیهای من نشان میدهد که این گزارشات در حد «باد و بود» است فعلاً و به مرحله«زارتان زورتان» نرسیده‌ایم. با تشکر از توجه شما به این مطلب.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23338" target="_blank">📅 03:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23337">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حقیقت‌یاب اتاق جنگ:
ویدئوی منتشرشده از
دیوید کیس، سخنگوی سابق نتانیاهو
قدیمی است و مربوط به
ژوئن ۲۰۲۵
است. کیس در این ویدئو مدعی شده بود جمهوری اسلامی «ظرف چند هفته» سقوط خواهد کرد و حتی زمان آن را
دقیقاً دو هفته، سه روز، شش ساعت و چهارده دقیقه
اعلام کرده بود. این ویدئو امروز بدون اشاره به تاریخ اصلی، مجدداً در برخی رسانه‌های زرد منتشر شده و به‌عنوان اظهارنظری جدید درباره تحولات جاری ایران بازنشر شده است؛ در حالی که اصل ویدئو مربوط به بیش از یک سال پیش است.
@WarRoom
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23337" target="_blank">📅 03:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23336">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا درباره احتمال
دسترسی چین به فناوری‌های حساس جنگنده F-35 از طریق عربستان سعودی
هشدار داده‌اند. طبق گزارش، یک ارزیابی آژانس اطلاعات دفاعی پنتاگون درباره توان ریاض برای حفاظت از فناوری‌های F-35 ابراز نگرانی کرده و به
دسترسی چین به تأسیسات سعودی و استفاده عربستان از تجهیزات مخابراتی چینی
اشاره کرده است. این نگرانی‌ها در حالی مطرح شده که دولت ترامپ در حال پیشبرد فروش
۴۸ فروند F-35 به ارزش حدود ۲۴ میلیارد دلار
به عربستان است. نگرانی مشابهی پیش‌تر درباره فروش F-35 به امارات و روابط رو به گسترش ابوظبی با چین باعث تأخیر در این معامله شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23336" target="_blank">📅 02:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23335">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537de6d757.mp4?token=Ould1mE-kOWHQbTGqal0WeKV8wdFvFl8d2OM6HVnnZQfdnpehs5EDoWmKajX7q4NUdhSw6dlJtNfhtwbmRo4XOcBS6ITquiJ7_EJMOItshe_nu3VPyfFwmcKiaZyAZMS6o9Cc_J1mszKiX-7iD9vGPKbhCnY2bsphyIhg6aWWL_4a3rq118ztyqXCABKTfhIxFZ_oq7PFXls-iN92ZSsgJ0E6eyBwOlGnowlUczePqvj_xcOvK8epcRVqWmkTWD9CIXhDWND7LPBuH67qY1G4OVFy8d3YX974YnJ7yScHrKirba7Q4p04AhP8O0b4rJ4_iDpVX51kmoj4j6MzMz5NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537de6d757.mp4?token=Ould1mE-kOWHQbTGqal0WeKV8wdFvFl8d2OM6HVnnZQfdnpehs5EDoWmKajX7q4NUdhSw6dlJtNfhtwbmRo4XOcBS6ITquiJ7_EJMOItshe_nu3VPyfFwmcKiaZyAZMS6o9Cc_J1mszKiX-7iD9vGPKbhCnY2bsphyIhg6aWWL_4a3rq118ztyqXCABKTfhIxFZ_oq7PFXls-iN92ZSsgJ0E6eyBwOlGnowlUczePqvj_xcOvK8epcRVqWmkTWD9CIXhDWND7LPBuH67qY1G4OVFy8d3YX974YnJ7yScHrKirba7Q4p04AhP8O0b4rJ4_iDpVX51kmoj4j6MzMz5NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
«آیا قبول دارید که آنها برای کاهش قیمت‌ها، به‌دلیل جنگ با ایران، نرخ بهره را افزایش می‌دهند؟»
ترامپ:
«نه، آنها نرخ بهره را افزایش می‌دهند تا شرایط برای ترامپ تا حد ممکن بد پیش برود. مشکل آنها این است که ما
بهترین اقتصاد تاریخ
را داریم.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23335" target="_blank">📅 02:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23334">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa149f9d4.mp4?token=aDKHyvlCztIGnRhFjpW1mPoc0Ffn17giL9dGbPEOxu5NFwOQ9Jh0ANMkKQv-h4X4zwqRYAF8AYHaCS6LOM9XmZblrCOg99R7l3b7eLw35MQuUwDeTPw9Fpvpb53Nl1VorpXo4Ik5Wc3fUfhLTVo-i19soa00S3ZvwOIPzROAZuPtp3OcrYFWvPyABkVAwxsMgHsOj913YG7zkl4fLHXVy0x-xuM8OzaLrh83N50x4KL2PM2BoA9p610yhXrQ-PO7fLDUCoOQikbp-jZRenPuN8x5vXAHmI-XFs4kr1NREecw15xffe57FRvdNa69u02Oo_gbeZSsb_JlR7KUy0nqHpGu8FgG0kXhbAXItPEZjcrXGNa8ODn1GjX73VtXl4W7VI_WSg_lR9kVa1HoCks6sGH-0Rpww7RjrJ7CyNT3m4Ro5RbM3jGpjHZ_tX4TPVzQXQHrqcmoAKVrmcRyscjpYKuTPf7cPFO7fUIc9bvlQwfkCXTbDmyh685HwJmU0oRX_SLFY29h4lWRx3EsHNBg_f0xRKiO0FIyBzZXI2o_3EpKMQSecz0935dgxBJOsL3SVXBe3w69O_hyXsCZ2bBcZgLYp2qxhBW5kTIs02VmLn9QsZL2s-i8b1_ohOiREt0_9c-6HNS9Px20_Rohl0us2r59IeoCYTryyUnHkCkItgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa149f9d4.mp4?token=aDKHyvlCztIGnRhFjpW1mPoc0Ffn17giL9dGbPEOxu5NFwOQ9Jh0ANMkKQv-h4X4zwqRYAF8AYHaCS6LOM9XmZblrCOg99R7l3b7eLw35MQuUwDeTPw9Fpvpb53Nl1VorpXo4Ik5Wc3fUfhLTVo-i19soa00S3ZvwOIPzROAZuPtp3OcrYFWvPyABkVAwxsMgHsOj913YG7zkl4fLHXVy0x-xuM8OzaLrh83N50x4KL2PM2BoA9p610yhXrQ-PO7fLDUCoOQikbp-jZRenPuN8x5vXAHmI-XFs4kr1NREecw15xffe57FRvdNa69u02Oo_gbeZSsb_JlR7KUy0nqHpGu8FgG0kXhbAXItPEZjcrXGNa8ODn1GjX73VtXl4W7VI_WSg_lR9kVa1HoCks6sGH-0Rpww7RjrJ7CyNT3m4Ro5RbM3jGpjHZ_tX4TPVzQXQHrqcmoAKVrmcRyscjpYKuTPf7cPFO7fUIc9bvlQwfkCXTbDmyh685HwJmU0oRX_SLFY29h4lWRx3EsHNBg_f0xRKiO0FIyBzZXI2o_3EpKMQSecz0935dgxBJOsL3SVXBe3w69O_hyXsCZ2bBcZgLYp2qxhBW5kTIs02VmLn9QsZL2s-i8b1_ohOiREt0_9c-6HNS9Px20_Rohl0us2r59IeoCYTryyUnHkCkItgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:امیدواریم که به انتهای "جنگ" با ایران برسیم. ایران خیلی زیاد می‌خواهد یک توافق منعقد کند.
خبرنگار: آیا از طرف آن‌ها با شما هیچ تماس‌هایی برقرار شده است؟
ترامپ: بله.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23334" target="_blank">📅 02:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23333">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مجلس نمایندگان آمریکا با رأی ۲۵۲ موافق در برابر ۱۵۴ مخالف، اصلاحات سنا در طرح «قانون تحریم روسیه و ایرانِ لیندسی اُ. گراهام در سال ۲۰۲۶» را تصویب کرد. در این رأی‌گیری، ۱۹۷ جمهوری‌خواه، ۵۴ دموکرات و یک نماینده مستقل رأی موافق دادند. در مقابل، ۶ جمهوری‌خواه…</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23333" target="_blank">📅 02:09 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
