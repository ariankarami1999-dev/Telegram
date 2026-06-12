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
<img src="https://cdn4.telesco.pe/file/rr-yTw7LaHsD1liy1FAwbi4sHkmJm1qiXVPdqIUzakMu-165OvxxRcT-apcGXa-08v3rTPeZ7cNrTg2PG1sQX_GZkqLP5mn0jsJCFjCWx_oUWeLiYU4nsiA8etf1PIiEE2uq71nDOaluRZxiZ3oKlr145nGPQmMyJXCAZ3SQbXWLmJonAGyS78JOLVtSsTHGs-QX1QzOihPe6TtYjyB8-QBcKw2XvpBTe7wmhiMBAsBHvsxcBvm9Yybkqk9x6j1DiAG08GT3m3YKCKi1l8HSLsol1fniQp7sVqILk-uS6xc7_xRNSw7DlBG6uE0t1o-AYwcypBPwrQgu1xHwhKZYgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 326K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 00:32:11</div>
<hr>

<div class="tg-post" id="msg-14677">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1ff8xU_nN4vE7VqEqWljwp2w5X1B5dWF1dnxfmwf2_zGYVkxSU40EZr3PQochLeAMrDh_ETEpISK5yzV3XnXBYQM99zECG4xP4faihidC5YMu6tSyfQ4QEbAgYHen014nHEvOQqD9GBuPA_KQqa5D2eqmhoHkd4jrDWKrJpqIL-MesHXAJpvbD98JzTos99HJmXlWgVyopDFvV72Q4xdE9kn9IYtaPrOYeh81AFdXqn1J1IEOO0U_YGdtH6V96uOMusmuRXRxxpPL-xh4d8TIH3K_kPsSSsR0TvsL05KVXlbEa33EyV6ZDDWmwzazqR15g7oTOv6eWMiDGI10MrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/withyashar/14677" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14676">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تو تنگه دعوا شد
@withyashar</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/withyashar/14676" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14675">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مهر : شنیده شدن صدای انفجار در حوالی جزیره قشم و سیریک؛ گمانه‌زنی از درگیری دریایی
بررسی‌های اولیه نشان می‌دهد، در پهنه شهرستان سیریک انفجاری رخ نداده است و احتمالا صدای شنیده شده تلاشی برای کنترل تنگه هرمز و از سوی دریا بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/withyashar/14675" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14674">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/14674" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14673">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صدای انفجار سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/14673" target="_blank">📅 23:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14672">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عراقچی: در مذاکرات ۶۰ روزه چند حالت رخ می‌دهد
۱. تمدید مهلت مذاکرات در صورت خوب‌پیش‌رفتن مذاکرات.
۲. نرسیدن به توافق، به‌علت بی‌فایده‌بودن مذاکره‌.
بستگی به شرایط آن موقع تصمیم می‌گیریم که اگر نتیجه نگیریم چه خواهد شد.
تنها کاری که می‌توانیم برای اورانیوم غنی‌شده انجام دهیم "رقیق‌سازی در داخل" است!
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/14672" target="_blank">📅 23:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14671">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عراقچی:به‌زودی ایران و عمان بیانیه مشترکی در مورد اداره تنگه هرمز منتشر خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/14671" target="_blank">📅 23:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14670">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عراقچی: عوارض نخواهیم گرفت اما هزینه خدمات میگیریم
ممکن است در دوره ۶۰ روزه این مورد کمی متفاوت باشد
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/14670" target="_blank">📅 23:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14669">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عراقچی:  این توافق دشمنایی داره که اسرائیل اصلی ترینشونه
امیدواریم تفاهم‌نامه امضا بشه ولی اگر نشه وارد دور بعدی مذاکرات نمیشیم
اگر قرار بود به تهدیدهای حمله به زیرساخت‌های خود تن دهیم، قبلاً این کار را انجام داده بودیم.
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/14669" target="_blank">📅 23:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14668">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عراقچی: به صراحت میگم که این توافق دشمنانی داره که در راس آنها اسرائیله.
سکوت کنن رسانه ها که برسیم به توافق خوب
وقتی ما به توافق میرسیم که دو طرف راضی باشن
حالا توافق 50/50 هم نیست و درصدش مهم نیست
مهم اینه که توافق کنیم
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/14668" target="_blank">📅 23:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14667">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عراقچی: نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم
بهترین زمان برای پایان دادن به جنگ زمانی است که دست بالا را داریم؛ ما واقعاً در میدان نبرد پیروزیم.
ما به مدت ۴۰ روز در برابر ابرقدرت ظاهری جهان ایستادیم.
توافق و پایان جنگ، پیروزی را تثبیت خواهد کرد.
توافق نهایی هنوز حاصل نشده است؛ اگر نهایی شود، قول می‌دهم هر بند را به طور کامل توضیح دهم.
توافق شامل دو مرحله است و ما مسئله هسته‌ای را به مرحله دوم منتقل کرده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/14667" target="_blank">📅 22:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14666">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15f030f45.mp4?token=IjuJVfncy7AkJInSemklO2CTRoJ5H2nMAy0IARdRjC_IgwZOUjO94FZOKnmNLKNk7OnGgNX4cwGcqqHoJQbccf4_v6zgN728nKCD0um0N1_ZMkF0CRHREFLUW3Q2EW7-Fw4TUHCJVzTEilJIft4FrVAEoD1biWRHKQf-2K1yaOOUjxMWSKn6ZGRGKeYIfADw0Hbzt6PLpPaydPjkuUWBE5yrOGaBnPd5aqg37Ufm9oH_rpsn-xdFNnEzigeYcsLlOBbDi16Zt6rxyZYJ6NpuNWM-My4wYzrS2IHzeou1l4NDDcXdfq1THZfC-WTxN6BGisNYnxJCp-jsyX6PkkOAnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15f030f45.mp4?token=IjuJVfncy7AkJInSemklO2CTRoJ5H2nMAy0IARdRjC_IgwZOUjO94FZOKnmNLKNk7OnGgNX4cwGcqqHoJQbccf4_v6zgN728nKCD0um0N1_ZMkF0CRHREFLUW3Q2EW7-Fw4TUHCJVzTEilJIft4FrVAEoD1biWRHKQf-2K1yaOOUjxMWSKn6ZGRGKeYIfADw0Hbzt6PLpPaydPjkuUWBE5yrOGaBnPd5aqg37Ufm9oH_rpsn-xdFNnEzigeYcsLlOBbDi16Zt6rxyZYJ6NpuNWM-My4wYzrS2IHzeou1l4NDDcXdfq1THZfC-WTxN6BGisNYnxJCp-jsyX6PkkOAnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند مشهد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/14666" target="_blank">📅 22:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14665">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14435d52ae.mp4?token=RWIkdkm6CGUm5f_5deLtJCIj7NEEwjSmvLd7TSoGmjaf9Rc3SyZVnxZzkciZpU4CDyTVERaeHeG1GmWxEHCwK8unrjxCKWBXIaKhezd-y7sSsh1ixxvtjzFisNlyL97C776e6Zz3LE7hsJVBagSLbY1PSBUidbRT3CBFArPf4tNFMXczhM_dMjQS1maYXMOhSREDLygryKEkaePxFvgUFXg9C5sRwxg0JmLo6icGx8niyMc49m5QfK9NfI682BrbM8NLKA22kmP93qZxsmiMgzkrVvHqlf_smHMSRX0bUcBP3P92gLfNO4sI9QgpMm3EB1bebqoTGCjO8a6Hg56DEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14435d52ae.mp4?token=RWIkdkm6CGUm5f_5deLtJCIj7NEEwjSmvLd7TSoGmjaf9Rc3SyZVnxZzkciZpU4CDyTVERaeHeG1GmWxEHCwK8unrjxCKWBXIaKhezd-y7sSsh1ixxvtjzFisNlyL97C776e6Zz3LE7hsJVBagSLbY1PSBUidbRT3CBFArPf4tNFMXczhM_dMjQS1maYXMOhSREDLygryKEkaePxFvgUFXg9C5sRwxg0JmLo6icGx8niyMc49m5QfK9NfI682BrbM8NLKA22kmP93qZxsmiMgzkrVvHqlf_smHMSRX0bUcBP3P92gLfNO4sI9QgpMm3EB1bebqoTGCjO8a6Hg56DEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشهای زیاد شما از مشاهده چندین پهپاد شناسایی هم اکنون در آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/14665" target="_blank">📅 22:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14664">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea29ba51ad.mp4?token=sqNWUm8l6wpvSqe72QW7L_sB7VQC_aNFttMdCAKP-H8oX8JG9iELllI4xChV86cm-y9Xu5y1j4CUWAfvbCYv2wMbDDzwfNzLSd_NPDfMiedeTh3rtGYlszJ3EOExHJ7e9nXUIHrSF2uNemZPet6iaF-RApXltuO-vDnRo1uTGvrhUJqqdUfB2k_Ru053miVhgkRmLQoZwigQ8Vkq_mKH8cYpUgtn3jDndDci03PdnLIJPX_ijAY_9Pvu8aylxpT-qej6gVTtHJmeVNXIhUY80ju38SeN6FV6WU5p16zMERjxKMFIKx6ccXrqNwNNb5XsxVqapFS1PWFXoxqU0JfzBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea29ba51ad.mp4?token=sqNWUm8l6wpvSqe72QW7L_sB7VQC_aNFttMdCAKP-H8oX8JG9iELllI4xChV86cm-y9Xu5y1j4CUWAfvbCYv2wMbDDzwfNzLSd_NPDfMiedeTh3rtGYlszJ3EOExHJ7e9nXUIHrSF2uNemZPet6iaF-RApXltuO-vDnRo1uTGvrhUJqqdUfB2k_Ru053miVhgkRmLQoZwigQ8Vkq_mKH8cYpUgtn3jDndDci03PdnLIJPX_ijAY_9Pvu8aylxpT-qej6gVTtHJmeVNXIhUY80ju38SeN6FV6WU5p16zMERjxKMFIKx6ccXrqNwNNb5XsxVqapFS1PWFXoxqU0JfzBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سهام شرکت فضایی و موشک‌سازی SpaceX که تحت مالکیت ایلان ماسک قرار دارد، امروز برای نخستین بار در بازار بورس آمریکا عرضه شد و معاملات آن با قیمت ۱۳۵ دلار به ازای هر سهم آغاز شد.
عرضه اولیه این شرکت توانست بیش‌ از ۷۵ میلیارد دلار سرمایه جدید جذب کند و ارزش کلی اسپیس‌ایکس را به حدود ۱.۷۸ تریلیون دلار برساند.
در پی این جهش تاریخی، ثروت ایلان ماسک از مرز یک تریلیون دلار عبور کرد و او رسماً عنوان نخستین تریلیونر تاریخ را به خود اختصاص داد.
در لحظه نگارش این متن هر سهم حدود ۱۷۰$ است
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/14664" target="_blank">📅 22:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14663">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حزب‌الله:
بر اساس آنچه مقامات ایرانی به ما گفته‌اند، اسرائیل بر اساس این توافق از خاک لبنان عقب‌نشینی خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/14663" target="_blank">📅 22:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14662">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">طبق گزارش ها،فرمانده کل سپاه، احمد وحیدی با شرایط متن تفاهم نامه ایران و آمریکا موافق نبوده متن تفاهم نامه با همکاری عراقچی و قالیباف تنظیم شده است و پس از مخالفت فرمانده سپاه به رهبری در ایران ارسال شده،
رهبری در ایران نیز تاکنون مانند دفعات قبلی متن تفاهم نامه را تایید نکرده
@withyashar
🚨</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/14662" target="_blank">📅 21:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14661">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سازمان ملل: از روند مذاکرات دلگرم شدیم!
@withyashar
😁</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/14661" target="_blank">📅 21:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14660">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبرنگار فاکس‌نیوز نزدیک به ترامپ از نقل یک مقام کاخ سفید درباره توافق :
۱. مواد هسته‌ای نابود و منتقل خواهند شد.
۲. برنامه هسته‌ای برچیده خواهد شد.
۳. هیچ‌یک از پول‌هایشان تا زمانی که تعهداتشان را انجام ندهند آزاد نخواهد شد.
۴. تنگه هرمز باز خواهد بود.
۵. هیچ تأمین مالی از سوی ایران برای گروه‌های تروریستی وجود نخواهد داشت.
این مقام افزود: «این همان چیزی است که آنها با آن موافقت کرده‌اند. این یک توافق مبتنی بر عملکرد است.»
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/14660" target="_blank">📅 21:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14659">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الحدث: وزیر خارجه پاکستان امشب عازم ژنو می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14659" target="_blank">📅 21:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14658">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یک مقام ارشد آمریکایی به رویترز:
توافق با ایران اهداف اصلی ایالات متحده را محقق می کند
این توافق تنگه هرمز را بازگشایی خواهد کرد، ایالات متحده مواد هسته ای غنی شده دریافت خواهد کرد.
توافق ایران همچنین شامل یک رژیم بازرسی است. اگر ایران رعایت کند، پاداش اقتصادی خواهد داشت.
منافع برای ایران تنها در صورتی حاصل می شود که آنها واقعاً به تعهدات خود عمل کنند.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14658" target="_blank">📅 21:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14657">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانال 12 اسرائیل : سرانجام توافق شد ؛ این توافق قطعیه و به نتانیاهو اعلام شد!
ترامپ از ایران خواسته به‌صورت علنی درباره توافق شفاف‌سازی کنه و هشدار داده در صورت انجام ندادن این کار، با پیامدهایی روبه‌رو خواهد شد.
ترامپ در تماس تلفنی با نتانیاهو گفته:
«این همون توافقیه که دنبالش بودیم؛ یک توافق عالیه و وقتشه این جنگ تموم بشه.»
طبق این گزارش، نتانیاهو در این گفت‌وگو زیاد حرفی نزده و ظاهراً متوجه شده که توافق در آستانه نهایی شدنه و توانایی متوقف کردنش رو نداره.
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14657" target="_blank">📅 21:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14656">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آکسیوس: ترامپ به بنیامین نتانیاهو نخست وزیر اسرائیل خبر داد زمان پایان دادن به جنگ ایران فرا رسیده
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/14656" target="_blank">📅 21:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14655">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بقایی، سخنگوی هیأت مذاکره:
همین الان جلسهٔ نهادهای ذی‌ربط درحال برگزاری است؛ در مورد متن تفاهم ما در مراحل جمع‌بندی در داخل هستیم
اینکه گفته می‌شود ما خیلی به تفاهم نزدیک هستیم، حرف جدیدی نیست
مشکلی که ما در این مدت داشتیم اظهارات ضدونقیض طرف مقابل است.
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/14655" target="_blank">📅 21:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14654">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ: جمهوری اسلامی به‌طور محرمانه بابت ارائه اطلاعات نادرست در مورد توافق عذرخواهی کرد.
@withyashar
😁</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/14654" target="_blank">📅 20:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14653">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ثابتی:متن توافق احتمالی از برجام هم ضعیف‌تره و نه گشایش اقتصادی ایجاد می‌کنه و نه جلوی جنگ رو می‌گیره
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/14653" target="_blank">📅 20:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14652">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ : پست اخیر عباس عراقچی، وزیر خارجه ایران، درباره توافق را بسیار مثبت ارزیابی می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/14652" target="_blank">📅 20:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14651">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ : هنوز هم معتقدم که توافق ممکنه تا پایان این هفته یا نهایتاً روز دوشنبه امضا بشه.
ایران به‌صورت محرمانه بابت ارائه اطلاعات نادرست درباره توافق عذرخواهی کرده
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14651" target="_blank">📅 20:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14650">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزیر جنگ اسرائیل: رئیس‌جمهور ترامپ در حال حاضر به سمت توافقی با ایران پیش می‌رود که از دیدگاه منافع آمریکا، از جمله منافع مشترک با اسرائیل—برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای است و ما انتظار داریم او این اصل و اصول اضافی در حوزه موشک‌ها و نمایندگان نیابتی را حفظ کند.
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/14650" target="_blank">📅 19:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14649">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سناتور لیندسی گراهام:
بسیار خوشحالم که ترامپ گزارش رسانه‌های ایران را جعلی خواند، چرا که آن توافق افتضاح بود
آنها در ضعیف‌ترین وضعیت خود در ۴۷ سال اخیر قرار دارند.
ما نباید فراموش کنیم که نظام ایران ۴۲ هزار نفر را تنها به دلیل خواست زندگی بهتر کشت.
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/14649" target="_blank">📅 19:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14648">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به گفته‌ی CNBC معاملات سهام  اسپیس اکس $SPCX تا پنج دقیقه‌ی دیگر آغاز می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/14648" target="_blank">📅 19:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14647">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6u-G1qs00HiyPT4Ds2K26AU3ZDbHVfRzJ8Glj-TUki7KxIZSEHf_LvSjUUWh0j-Ny9BkzErX1JMKd3lL6RjjqX9M6RlQnSBWbHq0qvQh6kwoofzHyM_L83BHrHWgVN945TN3A9UXgeXlwELJLkYVaqjBfwr8_W0i9YwFBE0VFZym-bbxvgVtFhPGXkI2_CfUf8H_ka-gxII8xdsj1f8d6hWqyHaGu13Q-6rsDbpi9cVNatqR0Iv6ZoezNEBGKPoO92DLDyrA975vNCuGvqWd2VSnD_hwjkIG3xqNOCzKVY5ghn6fAZuLwJU9-U9dawvdTnHWuAOu627frH5KjsBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چپقچی، وزیر خارجه: حفظ یادداشت تفاهم اسلام‌آباد هرگز به این اندازه نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از ورود به حدس و گمان درباره محتوای آن خودداری کنند.  در راستای رویکرد مسئولانه و شفاف ما، تمام جزئیات در زمان مناسب با عموم مردم به اشتراک…</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/14647" target="_blank">📅 19:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14646">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اوهو‌ووووو‌‌
🤣</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/14646" target="_blank">📅 19:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14645">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جی‌ دی ونس:
اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود
این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد. این توافق پتانسیل بازسازی منطقه و منجر شدن به صلح پایدار را دارد.
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14645" target="_blank">📅 19:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14644">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سناتور لیندزی گراهام: ایدهٔ یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی در ایران مسئول است، به نظر بی‌توجه می‌آید.
این مانند طرح مارشال برای آلمان است در حالی که نازی‌ها هنوز در قدرت هستند.
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/14644" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14643">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بعدن میگم
🥶</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/14643" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14642">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یه چیز بگم مغزتون سوت بکشه
🤯</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/14642" target="_blank">📅 18:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14641">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">جی دی ونس، معاون ترامپ:
این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به آن‌ها و کل منطقه خواهد رسید. این توافق پتانسیل بازسازی منطقه و ایجاد صلح پایدار را دارد.
در گزارش‌های چند ساعت گذشته چند نکته عجیب دیده‌ام. اول، افرادی که (به درستی) یک ماه پیش گفته بودند دونالد ترامپ رئیس‌جمهور تاریخی بود، اکنون بر اساس گزارش‌های رسانه‌ای تأییدنشده از توافق انتقاد می‌کنند. دوم، افرادی که می‌گویند نمی‌توان به هیچ کلمه‌ای از سپاه پاسداران اعتماد کرد، ظاهراً به پست‌های ناشناس در شبکه‌های اجتماعی باور دارند.
رئیس‌جمهور به هر حال نتیجه خوبی برای ما به دست خواهد آورد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14641" target="_blank">📅 18:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14640">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چپقچی، وزیر خارجه: حفظ یادداشت تفاهم اسلام‌آباد هرگز به این اندازه نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از ورود به حدس و گمان درباره محتوای آن خودداری کنند.
در راستای رویکرد مسئولانه و شفاف ما، تمام جزئیات در زمان مناسب با عموم مردم به اشتراک گذاشته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/14640" target="_blank">📅 18:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14639">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/14639" target="_blank">📅 18:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14638">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDqmHQKm4gCjaA1lPAWNGICkEWGgBYZBPtMicXodsudBoy8tIvR_U_fpL3-37IZzRGMaaXNP89RAfw5O0aLGJlPLLbMWzvOQ39hdGj-fHu-KqZVXToAeSBy0PAtNA4WU94CTy1dhmNYH_zO4hUbCPIhT3Fdj5SV1bZ8ruevyfAsTLkZir9VW0dLJ_hWeznD5zihg4JdU8_EHzhONqg15mRyWLIoeTRJ3mKClpXNgiobtXvstBvJU6_UTjW-qYBahweBFXzJJQkMmQwBbLKgRlaWPz1dTDZ2RZE8XVEAF5R2ujX-xOPPRNs9pvaUo8_pWQMGKz5Jurxd3EJaz96HpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : مفادی که ایران به رسانه‌های جعلی (Fake News) درز داده است، هیچ ارتباطی با مفادی که به‌صورت مکتوب بر سر آن‌ها توافق شده بود، ندارد.
آنچه آن‌ها گفته‌اند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود یک توافق، هیچ نسبتی با حقیقت ندارد.
آن‌ها افرادی بسیار بی‌شرافت برای مذاکره و معامله هستند. در مورد آن‌ها، چیزی به نام مذاکره و رفتار با حسن نیت وجود ندارد. شگفت‌انگیز است!
همچنین، حمله پهپادی کاملاً ناکام‌مانده آن‌ها دیشب علیه کشتی‌های هندی که در حال خروج از تنگه هرمز بودند، کاملاً غیرقابل قبول است.
بهتر است هرچه سریع‌تر اوضاع خود را سر و سامان دهند؛ وگرنه با عواقب آن روبه‌رو خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14638" target="_blank">📅 17:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14637">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خبرنگار وال‌استریت ژورنال: برای اینکه توافقی شکل بگیره، مهمتر از تایید مجتبی خامنه‌ای، تایید فرمانده‌های ارشد سپاهه.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14637" target="_blank">📅 17:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14636">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">منبع ارشد در تیم مذاکره کننده ایران:
یادداشت تفاهم نامه برای ورود به مذاکرات میان ایران و آمریکا نهایی نشده است و در حال بررسی است و
هرگونه امضای یادداشت تفاهم در روز های آینده کذب است
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14636" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14635">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏شاهزاده رضا پهلوی: در ایران نوین با مافیایی شدن ورزش مقابله خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14635" target="_blank">📅 16:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14634">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رویترز: توافق توسط جی‌دی ونس و قالیباف امضا می‌شود.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14634" target="_blank">📅 16:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14633">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نبویان: ما آمریکا رو زدیم زمین، رو سینه‌اش نشستیم که کار رو تموم کنیم یهو رفتیم پای میز مذاکره، میخوایم توافقی بکنیم که اون بیاد بشینه رو سینه ما اخه.
@withyashar
😂
🍋
🍋</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14633" target="_blank">📅 15:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14632">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع اسرائیلی:
اسرائیل به آمریکا فشار میاره تا دارایی‌های مسدود شده ایران رو به عنوان بخشی از یادداشت تفاهم آزاد نکنه.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14632" target="_blank">📅 15:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14631">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0uYHXqPUaDOsyvw24rKgS1nlwdemwenFI0qb1yTHNlIwvSrhq6plh_XFp340JRuZgLgBH87vumZ6VBPP17DMMCH6_BL1aeqYXRZ1hNCvIhUvfmn-4GPu0XxJHTxl25tr-ySFYQ-s3cxBS6hCG5I7kbLH2hMfWt8vDDho6uwUxBWuqWy-UPfRIFc2EOMCCiL1slSDnb30AjJ9lXJYJYa9PAf3xKUpB8sqPS1k0ro-kaI0fNrsy-ThrfB_gW_lCBKtiENiCsUl5HiN4Tzu3hQi-LotCdpPVzVMxHR1rnM3WU8z1AlFwnLulX6Fszl9juZUctrZ73zGWBdgObQRgou3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: ناوهای جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان در آب‌های منطقه‌ای به گشت‌زنی ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند.
تا امروز، نیروهای آمریکا ۱۳۶ شناور را تغییر مسیر داده‌اند و ۹ شناور را از کار انداخته‌اند تا از رعایت این محاصره اطمینان حاصل شود.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14631" target="_blank">📅 15:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14630">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرگزاری ایرنا درباره جزئیات توافق احتمالی میان جمهوری اسلامی و آمریکا:
متن یک توافق برای پایان جنگ با دقت بسیار بالا و وسواس زیاد تدوین شده و هیچ مجالی برای تفسیر خودسرانه یا فرار از تعهدات از سمت هیچ‌یک از طرفین در این توافق وجود نداره.
در این یادداشت تفاهم هیچ توافقی درباره پرونده هسته‌ای حاصل نخواهد شد و جمهوری اسلامی هیچ تعهد جدیدی ارائه نخواهد کرد!
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14630" target="_blank">📅 15:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14629">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو:
تا وقتی من نخست‌وزیر اسرائیل باشم، ایران به سلاح هسته‌ای دست پیدا نخواهد کرد.
من و ترامپ در این موضوع کاملاً هم‌نظر هستیم.
بیش از ۳۰ ساله که در خط مقدم مقابله با برنامه هسته‌ای ایران حضور دارم.
اگر این تلاش‌ها نبود، ایران سال‌ها پیش به بمب اتمی دست پیدا کرده بود؛ بمب‌هایی که به گفته او برای نابودی اسرائیل استفاده می‌شدند.
ایران به‌دنبال نابودی اسرائیله و من زندگی‌ام رو وقف جلوگیری از این موضوع کردم. تا وقتی نخست‌وزیر اسرائیل باشم، اجازه نمی‌دم چنین اتفاقی بیفته
.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14629" target="_blank">📅 15:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14628">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فارس: هر گمانه‌زنی دربارۀ امضا در سوئیس یا دیدار حضوری، چیزی جز فهم اشتباه از پیشنهادها و آرزوهای آمریکایی نیست!
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14628" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14627">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ایرنا؛ تفاهم‌نامه پایان جنگ چه مسائل و موضوعاتی را در بر می‌گیرد؟
۱.
موضوع هسته‌ای دست‌نخورده باقی می‌ماند
هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت ۶۰ روزه پس از امضا انجام خواهد شد.
۲.
تنگه هرمز؛ نه واگذاری، نه نقش آمریکا
ایران هیچ تعهدی در مورد واگذاری مدیریت تنگه هرمز نمی‌دهد. آینده اداره تنگه در چارچوب یک امر منطقه‌ای و از طریق گفت‌وگو و تصمیم گیری مشترک تهران با عمان حل و فصل می‌شود.
۳.
پایان قاطع جنگ در تمام جبهه‌ها، از جمله لبنان
هدف اصلی تفاهم‌نامه، پایان جنگ در تمامی جبهه‌های منطقه است. آمریکا تعهد می‌دهد که اسرائیل را وادار به پایان جنگ در لبنان کند و عبارت «تمدید آتش‌بس» در متن جایی ندارد.
۴.
آزادی دارایی‌های مسدودشده با ساز و کار مشخص
بخشی از دارایی‌های مسدودشده بلافاصله پس از امضا و بقیه به تدریج در طول مذاکرات آزاد خواهند شد. تهران تضمین‌های روشنی بر اساس ساز و کارهای مورد نظر خود دریافت کرده است.
۵.
غرامت جنگ در دستور کار
خسارات وارده به ایران در تجاوز آمریکا و اسرائیل از جمله موارد مورد اشاره در تفاهم‌نامه است. ساز و کار اجرایی دریافت غرامت در مذاکرات ۶۰ روزه پس از امضا مورد توافق قرار خواهد گرفت.
۶. جزییات رفع تحریم‌های اولیه و ثانویه؛ موضوع مورد بحث در توافق نهایی
رفع تمامی تحریم‌های آمریکا و قطعنامه‌های بین‌المللی در مهلت ۶۰ روزه مذاکرات هسته‌ای بررسی می‌شود.
۷. سه موضوع و ۶۰ روز برای توافق نهایی
در مذاکرات ۶۰ روزه تنها سه موضوع بررسی می‌شود: استمرار برنامه صلح‌آمیز هسته‌ای، رفع تحریم‌های یکجانبه آمریکا، و ساز و کار جبران خسارات. هیچ موضوع دیگری در از جمله توانمندی موشکی ایران، دستور کار نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14627" target="_blank">📅 14:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14626">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سخنگوی وزارت خارجه : متن نهایی تفاهم‌نامه تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد!
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/14626" target="_blank">📅 14:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14625">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مهر : توی توافق با آمریکا، واشنگتن متعهد شده بخشی از تحریم‌ها رو برداره و نیروهاش رو هم از اطراف ایران عقب بکشه
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14625" target="_blank">📅 14:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14624">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خبرگزاری فارس : آمریکا ترسیده و عقب نشینی کرده ولی ما هنوز داریم پیشنهادات رو بررسی میکنیم و جواب خاصی هنوز بهشون ندادیم !
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14624" target="_blank">📅 14:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14623">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری دولت: هدف اصلی امضای تفاهم‌نامه، پایان جنگ در تمامی جبهه‌ها در منطقه است. در این تفاهم‌نامه پایان جنگ علیه ایران به اضافه تمامی جبهه‌های دیگر منطقه به در برگرفتن لبنان هم مورد اشاره قرار گرفته‌است.
عبارت تمدید آتش‌بس در متن فعلی ذکر نشده‌است و اشاره به چنین عبارتی در برخی گزارش‌های رسانه‌ای نادرست است؛ متن تفاهم‌نامه خواهان پایان قاطع جنگ در تمام جبهه‌ها می‌شود.
تهران تضمین‌های روشنی برای آزادی دارایی‌های مسدود شده بر اساس ساز و کارهای مشخص و مورد نظر تهران دریافت کرده‌ است و در صورت تصمیم تهران به امضای تفاهم‌نامه پایان جنگ، بخشی از دارایی‌های مسدود شده بلافاصله و بقیه به تدریج در طول مذاکرات، آزاد خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14623" target="_blank">📅 14:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14622">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcxksH09ibaS4TNKlPv0IUeNVSOU4inoijDOndacT2GGklqO0lfhehSYLUApHIraoVPG2aNiGITfiAqspH8Jp5Uidtz4IUDSVhMn7O4bsIazdQEgB08wdz65wgunft-Vxcnnb13wzHJsI0U9pMyJaUJhbi4wdw2ZbWvTsIPGokjuE4ttsuk57ROYk_MchosfgeDsOKl-f7CEkvbQwjT-qp8NUrixP97Sju_rzpkX42jJrb5Vu-HlLH4ZkCRi021_m2-yourbCGioGUA9PZ8IQrx72mK8qfASwD2n7syp3TO6aIkquHJvTakceJytEDoBUMNF_Pm2hlxw6MtEbXImnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی اعلام دونالد ترامپ مبنی بر  احتمال امضای قریب‌الوقوع توافق با ایران، قیمت جهانی نفت 5 درصد کاهش یافت.
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/14622" target="_blank">📅 14:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14621">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">️تسنیم مجددا این خبر رو منتشر کرد:
متن تفاهم تا این لحظه در مراجع ذی‌صلاح جمهوری اسلامی به تایید نهایی نرسیده.
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/14621" target="_blank">📅 13:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14620">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسرائیل هیوم: ایران موافقت کرده است اورانیوم غنی‌شده خود را تحویل دهد.
از غنی‌سازی بلندمدت صرف‌نظر کندو  آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.
ایران باید متعهد شود که به دنبال دستیابی به سلاح هسته‌ای نباشد. تنگه هرمز بدون محدودیت باز خواهد شد. هر دو طرف متعهد می‌شوند که اقدامات نظامی بیشتری علیه یکدیگر انجام ندهند.
پرونده لبنان همچنان شکافی بین آمریکا و ایران باقی مانده است. انتظار می‌رود یادداشت تفاهم روز یکشنبه در ژنو امضا شود، در حالی که ترامپ برای اجلاس جی۷ در فرانسه حضور دارد.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14620" target="_blank">📅 13:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14619">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بلومبرگ به نقل از یک مقام گروه هفت: توافق بین واشنگتن و تهران به احتمال زیاد یک یادداشت تفاهم خواهد بود، نه یک توافق نهایی
!
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14619" target="_blank">📅 13:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14618">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ادعای آکسیوی : شرایط توافق بین امریکا و ایران:
1. باز شدن فوری تنگه هرمز
بدون دریافت عوارض یا محدودیت جدید.
2. برگشت ترافیک دریایی حجم حمل‌ونقل و کشتیرانی ظرف ۳۰ روز به سطح قبل از درگیری‌ها برگرده
3. لغو محاصره دریایی آمریکا
4. تمدید آتش‌بس به مدت ۶۰ روز شامل لبنان
5. ادامه مذاکرات هسته‌ای
6. توافق دوم برای پرونده هسته‌ای
7. تسهیل محدود فروش نفت برای ایران
8. کاهش تحریم‌ها به‌صورت مشروط
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14618" target="_blank">📅 12:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14617">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رسانه عبری i24: از جزئیات توافقی که تاکنون اعلام شده کاملاً مشخص است که ایران تضمین‌هایی از آمریکایی دریافت خواهد کرد مبنی بر این‌که اسرائیل تا پایان دوران ترامپ هیچ‌گونه فعالیتی در خاک ایران انجام ندهد
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14617" target="_blank">📅 12:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14616">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شبکه ۱۲ اسرائیل:
مذاکرات نهایی ایران و آمریکا بر مسائل اقتصادی و هسته‌ای متمرکز خواهد بود و شامل بحث‌هایی درباره برنامه موشک‌های بالستیک ایران نخواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14616" target="_blank">📅 12:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14615">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPGhXs9RnQerX5hgQCi8Y2QsFBDMG9sAXaj8-R4gd_OyLgK_k590TaNlRuttCAmjImfQgBPmgklHIbL516lp0Oq9_hCBRsBy_ZQob6AGv1NR6EGHI8dzB5jDP2tLbhHtVDkSkc05VQDQ50EvDP2HLaaBWpylbzdeQ8DSCGzUyPwPAMRC-xkQtNqSPLA5JSIIu0R_FHkFUrciyTHpTN4aEzWxQn8Gw7YA-sVQGm5zGx-pJ8uZZt3g2cuVmXlHWyaODQep9Sxv2HgnPwUj6Y1zRz-mAxTIyctuO_w5RcPwI4tshoB8VjCiwk2j35_yZEvR-6pDsXn5NG5ICY0brpN25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات امروز اسرائیل به جنوب لبنان شروع شد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14615" target="_blank">📅 12:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14614">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKOjoXF2tEj-5hNyXckf0ishZr741t64PUwd6ldkUPYlKyOeSC3D9Faa8MfwMoEiwoBhKmMDELX3I9BkuhRxz3rxSw-_RNJHxsEzB3wC99Owe-eDG_3qfB6t-Jm0uzkbau2ClMF8VekVvLWSbtb4BBXboA3G9CBV0v3UNo5u02qhMBHaRJ9gSrP1POxyvVcDFR96ppmt3HWwFB0KygVfN4W9Q7D8P4Qfmek7IrkV8IBdSK3DpDdSbq7mpUvyXIQSs9Eb9DqECJgGumc1Z2fzaAK0sGRXjQW0Jf3bUydoteX0wamJI1aP46pnS24SbQWMRrKDqAjMKwNCwaJZmc1-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوشش یکی از طرفداران تندرو تجمعات شبانه حکومتی
@withyashar
🥴</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14614" target="_blank">📅 12:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14613">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یدیعوت آحارونوت:
نتانیاهو گفت که به ترامپ اطمینان داده است که تلاش‌های او برای رسیدن به توافق با ایران را درک می‌کند، اما اسرائیل نباید قربانی چنین توافقی شود
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14613" target="_blank">📅 12:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14612">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کارشناس شبکه خبر:  با صراحت میگویم که متاسفانه بخش عمده ای از شروط ده‌گانه رهبری در توافق وجود ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14612" target="_blank">📅 11:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14611">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffd5b99a6.mp4?token=peYilhUA5g8QN4SOuVroNFR6pSgT8zAzqOOES0ps7TeYToCu_7mS4dDaVGw5VMIPOMxJzGZpgmI856kOP_v0kStqhku_ZKmi8MFpT_7fn030O-2_U3lFjMcTWEqMRSInQBYKelXWZeoAlPBlzjJGWeX5pCJwiCh6-Exwjhsyoepz5WbYbjBpWfRqkVGc8IKA9NikWiIVW2pHQaOHEcfHMypWdLYnnQKBqP2EwDRYoFuD-cncPZg9_an8in_cY_QAPav1WuPHEmOqHLMsLBiDNXttewxWtMdfv81A_4vvswYxSEzntJFlB5XhzNcH-M6B9OHalv2rE2SKNg7bWjDLMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffd5b99a6.mp4?token=peYilhUA5g8QN4SOuVroNFR6pSgT8zAzqOOES0ps7TeYToCu_7mS4dDaVGw5VMIPOMxJzGZpgmI856kOP_v0kStqhku_ZKmi8MFpT_7fn030O-2_U3lFjMcTWEqMRSInQBYKelXWZeoAlPBlzjJGWeX5pCJwiCh6-Exwjhsyoepz5WbYbjBpWfRqkVGc8IKA9NikWiIVW2pHQaOHEcfHMypWdLYnnQKBqP2EwDRYoFuD-cncPZg9_an8in_cY_QAPav1WuPHEmOqHLMsLBiDNXttewxWtMdfv81A_4vvswYxSEzntJFlB5XhzNcH-M6B9OHalv2rE2SKNg7bWjDLMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکرار ۳۹ باره ادعای «نزدیکی به توافق» توسط ترامپ از زمان شروع جنگ
شبکه CNN با انتشار ویدیویی از اظهارات دونالد ترامپ، نشان داده که او از زمان آغاز جنگ با ایران، دست‌کم ۳۹ بار ادعای «نزدیک شدن به توافق» را مطرح کرده است. این در حالی است که با وجود این تکرارها، هنوز توافق نهایی امضا نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14611" target="_blank">📅 11:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14610">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اکسیوس :  توافق ایران و آمریکا در ژنو سوئیس امضا خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14610" target="_blank">📅 11:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14609">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14609" target="_blank">📅 11:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14608">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کامنتم هم زیر پست ترامپ، کارهای اداریش را انجام بدهد فقط همین رو لایک کنید  https://www.instagram.com/p/DZdJ2LZvAza/?carousel_share_child_media_id=3917330556395457754_347696668&comment_id=18055196378739071</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14608" target="_blank">📅 10:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14607">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی:   احتمال فریب از سوی ترامپ بالاست
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14607" target="_blank">📅 10:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14606">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14606" target="_blank">📅 10:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14605">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14605" target="_blank">📅 10:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14604">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14604" target="_blank">📅 10:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14603">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14603" target="_blank">📅 10:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14602">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تولد بیبه
🥴</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14602" target="_blank">📅 10:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14601">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14601" target="_blank">📅 10:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14600">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی:
واشینگتن، تهران و قطر در مورد سازوکاری بحث کردند که به تهران اجازه دهد از وجوه مسدود شده برای خرید کالاهای بشردوستانه استفاده کند.
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14600" target="_blank">📅 10:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14599">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اکسیوس: چهار فروند هواپیمای ترابری C-17 نیروی هوایی آمریکا روز پنجشنبه به سمت اروپا پرواز کردند و تجهیزات لازم برای احتمال سفر جی‌دی‌ونس به مراسم امضای توافق در ژنو طی روزهای آینده را منتقل کردند
.
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14599" target="_blank">📅 09:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14598">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ: با ایران به توافق رسیدیم، توافق خیلی خوبی بود، دیگه هیچ سلاح هسته‌ای در کار نخواهد بود. تقریباً همه‌چیز نهایی شده و ما به هر چیزی که می‌خواستیم رسیدیم. مهم‌ترین بخش ماجرا اینه که ایران هیچ سلاح هسته‌ای نه خودش می‌سازه و نه از جایی می‌خره.
ما امروز جنگ با ایران رو پایان دادیم و آنها موافقت کردن که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن اصرار داشتیم. این هدف اصلی بود. این 95 درصد از کل موضوع رو تشکیل میده، و آنها این کار رو به قوی‌ترین شکل ممکن انجام دادن.
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/14598" target="_blank">📅 06:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14597">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فارس: یه کشتی متخلف تو هرمز رو هدف قرار دادیم دلیل صدای انفجار سیریک همین بود
@withyashar</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/14597" target="_blank">📅 01:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14596">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9c-uNQnfjsaoSUZiRf-tyDvKz4C52GKbStdrG0lNbdzW3bZWGptiMbck_DR_hfL9vVlwCGC0LC0R-P8e9dofhhvMNpUq8f7DQ1aRfa9oRrXnAwzkUjQTVeBiR_nA6Kp3j07hmqQrzzGhKXnp-3i2FKWnUjmTILCzi0LO-E1_TodQBEhGofRHjiGmI6fTkEbw9ZRbmXClKHtehbNBqEecg7PG2fDGlX9WtJeSLnAPbmk9oFb6nQcNEiOHJPdz5AookiMozZAeBHiac-pmeXgNgvriWMADAivgefbZxZYzZGnFYUw9uuE6H0RCACWRSDhOaJ5TwlBBSCCYXFW34Hg8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت توافق به سبک خاورمیانه
@withyashar</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/14596" target="_blank">📅 01:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14595">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfxVKKZDGdgRnO3PkvNNVs-ZN8AEEE32W3mAAOs3lEUYu9jqgNMpqCKG3yOHBg-Bvn0DEnOXVtF_OxYS7qwORaEMsmpt15mgCofBip7jt2vCYtBf1TjePvpv6iLfvYp-GHAolPTjKtycHRbu08NF0KAouyscar8YjuUzkG4y6kpOuTg8_Zcv33m3vtS_2XQmJFSx6MDxNijpgn0fno9YNQhKNQfBc0ib8DA8iAAd2Yiqr3DhP7cquQ84Pu0crnjNZuk732KpuajP6kUqQpG7wO5kVciv4WO4WHX1N4V76NkjVgxgcavYl0GJqOnC5Ow5qD4zkdzosa4-CoxBD6hvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه اف۳۵  کد اضطراری 7700 داد!!
فرود اضطراری
@withyashar</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/14595" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14594">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صداوسیما: دو انفجار در بندرعباس شنیده شده.
@withyashar</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/14594" target="_blank">📅 01:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14593">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoyMQYEx5oV8JzCkSOfMTuOuz9E6JW6RF6GjWH4bYNUfKJCWwRldXn2R8E6fPIPW9gg4AOgkX2G6bRlhTdZErVnM3CzjIuDBIH6yQ2uqXVmZC_moHJcc47tym4jbEMCPw8Dbt8f9ZgUTn61tKWbNpkxnT4NsBqdvJV5NUgo96JETIHbmL45IvAqWXAo0N6fe8Wihk4ZFSi2ie3z2_z9vW4wTptlV950HSJQN48XRzQ7Eqe-HrpwrYzDSBJcgwXZ0pp9oXXrJRXGxQ6sOa7bG5qsFHwK_24pS6glZ1cmcnpkWdVB2q52M5kAToyZwVZpY0Gk_3lut5BmjZCKrS9DARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : هر کی میگه الان تو جنوب کشور جنگ نیست، ببرش کنار یکی بخابون زیر گوشش.
@withyashar</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/14593" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14592">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">صدای انفجار در بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/14592" target="_blank">📅 01:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14591">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">صداوسیما:
برخی منابع آگاه صدای انفجارها را مرتبط با مدیریت و بسته نگه داشتن تنگه هرمز می‌دانند
.
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/14591" target="_blank">📅 01:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14590">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش صدای انفجار در گناوه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/14590" target="_blank">📅 00:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14589">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پدافند خرم اباد برای مقابله با پهپاد ها فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/14589" target="_blank">📅 00:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14588">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارش درگیری و تبادل آتش هم اکنون در تنگه هرمز
🚨
@withyashar</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/14588" target="_blank">📅 00:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14587">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/14587" target="_blank">📅 00:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14586">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer"><a href="https://t.me/withyashar/14586" target="_blank">📅 00:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14585">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجار در سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/14585" target="_blank">📅 00:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14584">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اکسیوس، به نقل از یک منبع: نتانیاهو هیچ اطلاع قبلی نداشت و وقتی ترامپ بیانیه اولیه خود را در مورد توافق با ایران منتشر کرد، غافلگیر شد.
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/14584" target="_blank">📅 00:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14583">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">https://t.me/boost/withyashar
بوست داره میریزه…</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14583" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14582">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرنگار: دیروز گفتید که ایران ممکن است در حال همکاری با ایالات متحده باشد. آیا شما معتقدید که این بار در خواست خود برای پیگیری دیپلماسی صادق هستند؟
ترامپ: این به سطح هیجان آغاز شده در آن بستگی دارد. ما در سه روز گذشته به شدت به آن‌ها فشار آوردیم. امشب حتی سخت‌تر به آن‌ها ضربه خواهیم زد. آن‌ها این را می‌دانستند.
ما دقیقاً به آن‌ها گفتیم که قصد داریم چه کاری انجام دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14582" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14581">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">️واشنگتن پست: توافق بزودی در رم یا ژنو امضا میشه
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14581" target="_blank">📅 00:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14580">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ درباره رهبری ایران:
من این افراد را بسیار منطقی‌تر از کسانی که دیگر در میان ما نیستند می‌یابم.
این گروه متفاوتی است و فکر می‌کنم گروهی باهوش‌تر و دارای دلیل و منطق است.
همه آنها این توافق را تأیید کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14580" target="_blank">📅 00:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14579">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad8668d6f.mp4?token=Q_Z1N3IxQbvdNYsqoeIYtIuTsOnCCrLCVm7O8KFD31YIX7okJnbYRJF3WsZvzVxATwHQLBK37svI0EHcJmW6k0fscH-OB4eCTAQAn6gkFXXCdkfBJxvbWDRESpWrXJIz7OvouIdtGavreQnJjFuEJFmpqkz-sN8Db6ZzLqPp42-E7ZZFc7mOlyW80cvRDJSIRArqNKVUymf8PUpSy75AlUCEVtX6BwprAOVjVMtQog1AhGPW6PbUGFYMgDAmYQTpDyz_4qdjz95RyYtb44z0L1ztnps-oem3-0fkmndqInhD6WLzRKZnYw50bdJZOU6ljwdjo1WMg4jSqzano7XpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad8668d6f.mp4?token=Q_Z1N3IxQbvdNYsqoeIYtIuTsOnCCrLCVm7O8KFD31YIX7okJnbYRJF3WsZvzVxATwHQLBK37svI0EHcJmW6k0fscH-OB4eCTAQAn6gkFXXCdkfBJxvbWDRESpWrXJIz7OvouIdtGavreQnJjFuEJFmpqkz-sN8Db6ZzLqPp42-E7ZZFc7mOlyW80cvRDJSIRArqNKVUymf8PUpSy75AlUCEVtX6BwprAOVjVMtQog1AhGPW6PbUGFYMgDAmYQTpDyz_4qdjz95RyYtb44z0L1ztnps-oem3-0fkmndqInhD6WLzRKZnYw50bdJZOU6ljwdjo1WMg4jSqzano7XpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا رهبر ایران این توافق را تأیید کرده است؟
ترامپ:  تا جایی که می‌دانم پاسخ بله است.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14579" target="_blank">📅 00:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14578">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14578" target="_blank">📅 00:07 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
