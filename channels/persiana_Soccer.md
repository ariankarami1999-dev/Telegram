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
<img src="https://cdn4.telesco.pe/file/t__wUD5960hfXh1yJzC1VboECe33bVVc130ScU6CzuLMnVPSJ1z8_IElWBps-Ya-jwkz3N-gF55iFyySrQSHJFl4XnWK8TUP-4TV9B1FXWUozqNLN0UW1BiXlXh5PvDY5i5FzPrCUgGUkInFiGcjmwSpJAMMfu5mkyOl3ixhfmbnYSOQxh77fdbFeexTdvgRUGl-n94PUl_BwykOCNRB1jqTfl7Po8aY7OU6oXwjej0mMqQdliB4KoojOuPbKyuq9gSEQM0kJd76mINUPOWVbehrU3VzpVl3nqFsi43_t1IPketbQsb3eea_J0a-UjZT_avp9lx1MddaDI4GNRWb-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 489K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 12:08:39</div>
<hr>

<div class="tg-post" id="msg-25840">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSXzOGkKsDDbL9EOxh6QdHi1tk1w3fBYbhVk0-SyiBY50x-fgcmXMACaIdDy0YS5s8642-p6Z-KG4rTByOkoqXm20N-rfOXwt81Y9YcUbfqJk49ChHGPNd6AOy0DMamzmd2IDvianSpPVf2jpqxeI-Q7vAkYxnlJk4n6fWK975VoN9GdJZ3n14sX0NGEcLAHNAzqVaZgLqOH8MsoaTlbQI8E2WafU5FhWExVfhNZTLyBHX5z2I8L5s4CNhIvyI_2EYwDqJErsa_2cYy7-FoNUr14PRjc7TIIKbk_HBR3VGxG_-xIGjkcl7uU-I0UTArGHYWmqOyU10pHTIdnBAzdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/persiana_Soccer/25840" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25839">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8168388efd.mp4?token=Ccttcyd9l9ht73YY8SZIkO65qEYpK5K7ExY_2RoDkL2aUQMuYI8PVtRNH7mESjp4-j5YsvqdQz3cM3Uuze2_jgDAw89uS8PcPODC1jr9O13zCfYcQ8U4kLtyAuoONFzqLoVT4_dlqznaoYPjdXXntBo0qjbVXL8UPJhEIfWLpIRLNWWhh6VyWAUuiVM1zo6ZNCOuLGa9E1EOTqEfQPcfHlyX78VgGwRJghJ-j38_59oU6iJ_uqEuB2bUH3hFuSZNPn8O0RvxpQBeiSTpHcD3_t6im4nUKd8dST6ke_ZVv4-NHgouRZkLwdDuz4d5pPEFfewz1JvY_1N_YoX-UEmUtIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8168388efd.mp4?token=Ccttcyd9l9ht73YY8SZIkO65qEYpK5K7ExY_2RoDkL2aUQMuYI8PVtRNH7mESjp4-j5YsvqdQz3cM3Uuze2_jgDAw89uS8PcPODC1jr9O13zCfYcQ8U4kLtyAuoONFzqLoVT4_dlqznaoYPjdXXntBo0qjbVXL8UPJhEIfWLpIRLNWWhh6VyWAUuiVM1zo6ZNCOuLGa9E1EOTqEfQPcfHlyX78VgGwRJghJ-j38_59oU6iJ_uqEuB2bUH3hFuSZNPn8O0RvxpQBeiSTpHcD3_t6im4nUKd8dST6ke_ZVv4-NHgouRZkLwdDuz4d5pPEFfewz1JvY_1N_YoX-UEmUtIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شش پاس گل تاریخی و حساس لیونل مسی در شش جام جهانی که در ان حضور داشته رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/25839" target="_blank">📅 11:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25838">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXkBEItC53yDj4HVMH_nKCZrGNNH68knPnfAr22eI1F8XMutcGi9apiHGpXExsEW49arPdfm8LmuXwi4GNjip8V4dGm-5sa7cqfcn5PA1oS5ofPe_PE2Wn5YAiR4Ub2anG4pnqiVz6zc3acMRgErce96PeYeFCmSYXEKFK3K-L5krozDlPN25wDYTCUoTtP-hn83n76jJXyw9FQmFtK_8TxOh-s9acFeAdXSvYNXKXdSMDdq37edPtnar4HdUaN5QqaPnqjtlpUpltmvtTCSKBnvb1tQPIL_UEr_KQTvAAQwDmJrlNPJzCU_cIDc1YpX0gsqvClFK0CY0Txh3vld9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/25838" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25837">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇦🇷
شادی‌کارمندان‌خبرگزاری آرژانتینی در طول بازی با انگلیس؛ دولت آرژانتین گفته اگه قهرمان بشیم یک هفته تعطیلی رسمی در کشور اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/25837" target="_blank">📅 10:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25836">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=QnR6WA1tWVyluF4H7nYyRFzy3VMWb8-kBi-RCkbkpwzkp3mmFBjMCxM3-hYbf1TGhDwUp1Hx26a4NTV8GkxUGrcK-_Ld9oJsPN4jV5MUcATetTPd3mvzYI79GeqUz9ubVnOgXnmO289scwa87GqsSUWw-ORbqRAjf3Lg3kPRlMgPPsQYPY3xqcfPnVJDbR-OC7plvqMOD-1_JYXgVX9HBW6v7ponNIjD3db5wCSrXVCPFaoAadGDqyyL1lIEKXW7WP8vBmksngscrm37GlshiQYS0FODwnrNiswm3546r7mx4uJQvqqEWMQByU92trsYmAM5WqsJliy5K4uIn4ID3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=QnR6WA1tWVyluF4H7nYyRFzy3VMWb8-kBi-RCkbkpwzkp3mmFBjMCxM3-hYbf1TGhDwUp1Hx26a4NTV8GkxUGrcK-_Ld9oJsPN4jV5MUcATetTPd3mvzYI79GeqUz9ubVnOgXnmO289scwa87GqsSUWw-ORbqRAjf3Lg3kPRlMgPPsQYPY3xqcfPnVJDbR-OC7plvqMOD-1_JYXgVX9HBW6v7ponNIjD3db5wCSrXVCPFaoAadGDqyyL1lIEKXW7WP8vBmksngscrm37GlshiQYS0FODwnrNiswm3546r7mx4uJQvqqEWMQByU92trsYmAM5WqsJliy5K4uIn4ID3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌توویژه‌برنامه دیشب جام جهانی پدر تشریفات‌ایران رواورده میگه تو دیت اول چیکار کنیم طرف خوشش بیاد و مخش طرف رو بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/25836" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25835">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Whq92oQLf3fetoHvJvLJ0iGvlTr7GU3HpxcZ-igdHtACyk5T2niTkSAMMfAaiWT7wxZ97f1xsR_7ezrrg9tYV4EHnNQVQnQp8-JQcNUVWTCQizgr1UQqKb3XsXeIEQ1HHC2g8r1Idp5V7TdT1BvqUhrvkxYig-_SWmJRXCLQnDYcyh6MFih85Nih4WYzSaHdgjeRfeI54g2gih_bhLjiK1_bh7-GNhvZUtvlPll-WL5jbsAYMiMQBUV4fVVlnDvartFEdZKvb6eAYTF_Q25jV8h7Pkv1r4wmnR4M1kXpnDDgCzrBo6ZK8uKX5MWpTem8UWaAq6G3zmbnr0NoGe0D8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درآمد تیم‌های ایرانی از جام جهانی
2026
🔵
استقلال: ۱.۱۶ میلیون دلار
🔴
پرسپولیس: ۱.۰۶ میلیون دلار
🔴
تراکتور تبریز: ۸۸۰ هزار دلار
🟡
سپاهان اصفهان: ۵۲۵ هزار دلار
🟠
فولاد خوزستان: ۱۷۵ هزار دلار
🟢
ذوب‌آهن اصفهان: ۱۷۵ هزار دلار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/25835" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25834">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=Pk8do904CYTsg3CFn1022rN2vkuFu_m7axQmmWbp4Y5Zu_Bso2eXl_KpcKFX9Ro25sZhbSf7hUSm34reewkCjzAOYA53ByYOEfQpGsCpia9ko8C3tMOgY-Uf6EPt4edtzWowUvU2niGXJjLpSb-c6yWKrary5I2tdb9d0VbA4letrGkWWJnS3qe6PczLtwoI9qfCnii3EQ3qI-zqMiHcXgeRq2nTr9aHiyBrQ3yuk2UWcjKMtp4rAQ38-2NH2yIWFt1ocTl90yV1xuS7m8hf2jXJhmOCVtewfPMj1nFWlgokoXetFwxcaRBZ3SOPMvoS02DcP9wRBBgmoL0XYkYqdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=Pk8do904CYTsg3CFn1022rN2vkuFu_m7axQmmWbp4Y5Zu_Bso2eXl_KpcKFX9Ro25sZhbSf7hUSm34reewkCjzAOYA53ByYOEfQpGsCpia9ko8C3tMOgY-Uf6EPt4edtzWowUvU2niGXJjLpSb-c6yWKrary5I2tdb9d0VbA4letrGkWWJnS3qe6PczLtwoI9qfCnii3EQ3qI-zqMiHcXgeRq2nTr9aHiyBrQ3yuk2UWcjKMtp4rAQ38-2NH2yIWFt1ocTl90yV1xuS7m8hf2jXJhmOCVtewfPMj1nFWlgokoXetFwxcaRBZ3SOPMvoS02DcP9wRBBgmoL0XYkYqdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/25834" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25833">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=pNJ0phUxWpi2qbpX5G3idGGpK9d_hrw6X9T5ftEfBxPacjZFYnaA26dqtGKGWIi89CfNV3Sj2OA8dFRzbRGzrXPzRyjB5DVRmzpDu1HobfdPBAAZi2f9Itt1GiAe6OemZNLaEKihWebo1aqIlaFU1-aBd19J0VRKUieq78cMnGi2T6ud2PEushCyVN7YFZufbI9qwVxperIHlYaKVm9KjZQVEtgoh-_DC5PP78psvktD72dbzGAOkoy_nKuIg8wKulqY1pZNv7XrsgWM2IpHd0uEZp1WeikS8LRje9pE9YaELx_nOwWRHNDubDfHC8umAsm3PP7dPPy4iEfLenqI5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=pNJ0phUxWpi2qbpX5G3idGGpK9d_hrw6X9T5ftEfBxPacjZFYnaA26dqtGKGWIi89CfNV3Sj2OA8dFRzbRGzrXPzRyjB5DVRmzpDu1HobfdPBAAZi2f9Itt1GiAe6OemZNLaEKihWebo1aqIlaFU1-aBd19J0VRKUieq78cMnGi2T6ud2PEushCyVN7YFZufbI9qwVxperIHlYaKVm9KjZQVEtgoh-_DC5PP78psvktD72dbzGAOkoy_nKuIg8wKulqY1pZNv7XrsgWM2IpHd0uEZp1WeikS8LRje9pE9YaELx_nOwWRHNDubDfHC8umAsm3PP7dPPy4iEfLenqI5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/25833" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25832">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLXdhQvBpHP721VE-20ikVmNuBzY-fI-22ZrCiZaa7bg5Xt1DGoaDOIL_7zewlcycNdDDTwnyO7v1j5slMQalzNARX-l3yqjXBCboH0dUiW7-4UWxi6KdwZi-woTSd_2iQ5W7kbG-_RfgWm_kpoVmSnIxRsphnQylo1MnRCLzFyny5NDa_ic_hbNICs0aeAX6c-Fj_Wq0goFgf8th_TQkgImJ2we2LgS1HqghhnTC3QrXQrmGHB9fmYE_hJXwjiCz-jX71nHoF0t19zHlWR_0ZQY7yWzCRAYi_4PIyUmJ-wn2C62Zz6RRx2GGKhWAAjmZ06XmWB2YpJYki-8rdzx0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😈
لذت رقابت های والیبال با بونوس ویژه ی وینرو
🏐
🏐
بونوس 3+1 وینرو مخصوص والیبال
🏐
🎲
با وینرو همیشه برنده ای
💰
🎰
با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۵ میلیون ریال برروی رقابت‌های لیگ ملت‌های والیبال در طول مسابقات،‌ درصورت پیشبنیی اشتباه مبلغ 5 میلیون ریال‌اعتبارپیش‌بینی رایگان ورزشی از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr25
📩
@winro_io</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/25832" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25831">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXBUO7FXEFyDV2FpwddXl-zpXpHgIm2yok1LT_yCGgJnLMGKJzYc5Hi07G_T34fRm8Vu0UA5LJTa5L50r1sFRB9Zp6qXaqsPVsG_GQDcGOMbnFWQ9bwFG8yEZNq6Y9vqqsfI79eVz6pxMSt8YDH-MuUqvcfITxUIw1E17gOvXNJB5dQL_cCKiNBGkhl-pJ-8fuvtyvNq_k8e-fu2F5y7TFNCucsMrdxvXFw643M1bBjRuS4CcESn2iMBOLOTrUoIbsJAKibBY3uZ4JOzgwLEc8FPSbw9dAhHp0Tx93Jq2JlF4tZV14E_DI0hagn_BAum2JxftCJ8sd__M0C1OI67YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌مسی‌داره باخودش‌فک‌میکنه که کاش همونجا تو تشت خفش میکردم که الان برا خودم آدم نشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/25831" target="_blank">📅 10:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25830">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/25830" target="_blank">📅 09:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25828">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvfK6r1j7kp5OrV-WT5-nGNaMHzlDuVqUr4BOVH0Tn9EYDd2lkeCdVXJuQXz9gZ0mNd7cEar0uK96W8rxUVCdE5sgYScQPBBYGAkJ9L9u5eJqockFzVGs2t2ZeXZtU4LVjdwJCk91thWbzAd-foSrXm2vcW7YrLzAn8_fE2RKSMSl_mjs30u6tUUYf_sZ5xDfik7IJWplX8nGaBdJpY6DI4PzldMsMXf0xHll3hXJ34Hub2f8Krty2Y1BsNH1YEWdVyGyJQ9xW1CSpS2EM9JYQXY5aJQvP9uciODJSMX2wz-RolSthNYk3iFcFOu9oRbQ7CMxO_7fAY_bdWYjm1WLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnTUtD4xtpohC7B3_oip3WA9uMaGENyVVIxjTaef5bQ9hm3Sc8R60KLWbDkWLe8_a1A3AHX_0_Y6rDBzfpOVLb5sCOQwVtKleP7kDj8H2eBCt7R15Tb6do1sfb1tcZ-PDI1CZA4NJRS4nU0yEIdl728D43siUhE7z0JNnEQ9LlqywbBsR7XhHg-MHL3DR3p-8tnUIXOUpQJD2J-F5CCs-GKHjZah0Ppry-dpOCtv4c9_kVYuzbwppUwkg2ZjJ-AIw_eGlmlhmIcVZ_bYU1PCh8IB6geeoxatuw7hCkHBMvF5ujUabfqfO-C2yEbVOaobDpvUA3N0XNyZBxInGngp0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رده‌بندی برترین گلزنان و پاسورها رقابت‌ها پس‌از پایان مرحله نیمه‌نهایی‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/25828" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25827">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvCD8qDAeopqRDw6C3vEdY_WK-w5KHw63vbXt8J_g7OTAWAQtckeeOYVj-N3sFAMC64iaXwO1bS__CNGtWQUTTbW1b0wRffrrpKUikxYR8waTHQ8tS6zabkFt8u68MXSicMTQkvLIq4a987MUnVwmm1tdBTZwsjxBlCCXi2_AmnvZ3z6dgmSLnKVS-C-tIO0xZplDAG-6xmx2Xn1HGQsUxeJS2hYktIY0-tfQOZH8lfFSTROlHmCuufuoT6pUyOYCKjTDpQ4Rdrgm_SJd0ZEr7rnKwL3AwY8pVn14qLL6v3znXCQs26X65k3a3lHUVCpAMNsjnsuFXjxHnOqDFGMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
هری کین:
باحذف‌ما من دوست دارم لیونل مسی برای دومین بار قهرمان جام جهانی بشه. من طرفدارش هستم اون سزاوار قهرمانی دوم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/25827" target="_blank">📅 09:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25826">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=YHn1vkZiXT16AZLlpB9jU9z8bGZHHoSwo9_DEvoQaHWtfovlrsPYasQ8gQU_FbACY3TOuFPOlBer22SfA2CDHTpcIR6qrcLmKPD0pv_X4v3wvtx7kAtPk8GyZCsvynxFk-x85QeZUdWL4X8WC4yZ2zMWX9Xn5PbJWPh0jHQHiNYwB85JRbYtZR_Z2dAh8Bp0RrQ2ibG3YHrLaZL74dbLHHeNuTHM3WEv_iuncaOQCT6o00T4be1mQ0KLkzIp9hTZ572JEp86_O-hm6aIBAatSTBfHHDDmTh57RXiU8OKr4Tk48EJIyxHOSfy2p_Kj3s19z_ApLI0plvx1m_OlOHgVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=YHn1vkZiXT16AZLlpB9jU9z8bGZHHoSwo9_DEvoQaHWtfovlrsPYasQ8gQU_FbACY3TOuFPOlBer22SfA2CDHTpcIR6qrcLmKPD0pv_X4v3wvtx7kAtPk8GyZCsvynxFk-x85QeZUdWL4X8WC4yZ2zMWX9Xn5PbJWPh0jHQHiNYwB85JRbYtZR_Z2dAh8Bp0RrQ2ibG3YHrLaZL74dbLHHeNuTHM3WEv_iuncaOQCT6o00T4be1mQ0KLkzIp9hTZ572JEp86_O-hm6aIBAatSTBfHHDDmTh57RXiU8OKr4Tk48EJIyxHOSfy2p_Kj3s19z_ApLI0plvx1m_OlOHgVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/25826" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25825">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl7yIoSIFVxt7bRdLSt2_wfDcjHE50AiBiqrduLpwfh2jTQGQLNFLfHVcj6oOnsDMQjuRpVsru00WkXRQOue0UWli0mPRuePsUCyK9mdevFrhUPf20KILLN5cH0y8KspkHx0HionXjXj12heDDqvDeuGV-mDg09klreecnKgHnEMcZWlYtbUp3m4RhB3OVsNHmN-sc4uzxHVhbrbNyak6homBNvk_uIdpJRn_1I0mRWp92j-rVqOnf-jOBHWOevgbG5znmPKPTKmLza7efCFNp8a_PJBT2Mo2gHKJDEK69dpdqXA28k6eSo4AkV2j1KvWwAh-z_9AIQcuOnumB9o-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#فکت؛ تو تاریخ بنویسین، مسی 39 ساله، پرایم هالند، امباپه، کین و بلینگهام رو گذاشت تو جیبش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25825" target="_blank">📅 02:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25824">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiZZcVtczkCjPLF7wgdNyVFnMYgzv-vbsHjKU_G2pfMTxJOtdI2cWeuYDSQV5CVlICy9OS2duw0PqfPnPpct0b3SyShMhQ6uZVvl1X3LCSvka4ltWR-k3wsNZdfkZfo4zufWVqK2MyvxYsTjckRzhbe008uabGZ4Y8W_wGfMedspg4gJ6mM8znCyguqfFpmHUxebpvH9vR7lOHt16DLK-Af7ndemBd71nrH1q7ONYug71CxIJC8mahsG9MwalLa2neiGTEiAmPmsphAakjpt8-dxaImy-fmwUxrybCZyqxIQlq2XQwl1fqDm7_i0WG6uZxusSx4xjJfuL-nYuyWdBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه ‌تنها دیدار‌ دیروز؛
کامبک دیوانه‌ وار آلبی‌ سلسته مقابل انگلیس بادبل‌پاس‌گل لیونل مسی؛ جام جهانی 2026هم به‌آخرش رسید. روز یکشنبه 22:30 فینال و قبلشم بازی رده بندی. بعدش یکم استراحت و آغاز داغ رقابت های باشگاهی در فصل جدید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25824" target="_blank">📅 01:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25823">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=lYeZkKmeX4jzAE6OiDhSElINAJENgkXtl0b9APuvbvRb7NrWufXPFk05UvQrKVdoV3w3flzrdXUhl82pU0wuDKUcRk2Qr9vmce6Kp-EiqxnYu-OcKJAbLu85CZRvLAyz4asz1rKUJPSwIypwVkpkko_O7WLPCyPXuXVcjZpiOUGJRqw-c3T_u7_jh7_ccZbEtlMjYN_cWcDDO6Ue12JNWZtG39lrfCj4z-uh41qHG6k50Xgul1kjXz5DuDF71fu3uE46OZeNtmSQtmVtHBYH80RKHfYEWd1DxmORqtUO-BpvJlYTk1d_C2l326ryMOOjorUk5w3WzzJTr504RZahDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=lYeZkKmeX4jzAE6OiDhSElINAJENgkXtl0b9APuvbvRb7NrWufXPFk05UvQrKVdoV3w3flzrdXUhl82pU0wuDKUcRk2Qr9vmce6Kp-EiqxnYu-OcKJAbLu85CZRvLAyz4asz1rKUJPSwIypwVkpkko_O7WLPCyPXuXVcjZpiOUGJRqw-c3T_u7_jh7_ccZbEtlMjYN_cWcDDO6Ue12JNWZtG39lrfCj4z-uh41qHG6k50Xgul1kjXz5DuDF71fu3uE46OZeNtmSQtmVtHBYH80RKHfYEWd1DxmORqtUO-BpvJlYTk1d_C2l326ryMOOjorUk5w3WzzJTr504RZahDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25823" target="_blank">📅 01:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25822">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏆
تصویرجالبی‌که ESPN با عنوان " لیونل مسی و بادیگاردهایش" از بازی امشب با انگلیس منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25822" target="_blank">📅 01:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25821">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLrcfHAIJE9i6_dTJ8pU1QiIGR5dBaM2wjsQI70Z3QWfTdsBbojuVhUy_Ab3ycyQW_TSjFKUGlhOIq5K7YTUVF44-jHy33GTj7cPI-A5FL9u7-jkEm7N0s9ITDOoz4Sk5AFhPHwqjF69osqH4bC2amPhk9_K6SW84CaQ-Bs-W1CNZC2ZcKj5eRBX6NjWXvWvP9Qx08EQZmKuICBhmij9bMFwJ-8JvlrrdUXB07sR1M7AF3STd54qdCiC8qOgHx2XoncK1q1eVn6VqU8jDY9a7I-6XJr_aTxi2kgvamWWLUJ7S802s2Nx5h0jV-zy324wFKdoc9xRF92Vwd3sHDXvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25821" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25820">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=LaaVBJki3vC3xGxCur_sB_YqvAfahrj9Rg0oXOZklCecg0SIUGchnWg33ao4LjdvXxAJx43U7z8QBa8kMkXMyFvV44r0vHicnPTK8CdbCFUsNmbuNqR4S2RSJWDhxDuGf3nDMRs_DNQRuPOWufY0Qh7iWSrAL5kQu8ySkpkiCIFbyMCT8tZ3pztN0Z62SjsaYfQblpenqlxyVS5fzLJ312lY2Lxbo1Bad8k-i9_R8nRvn3DIkyvTR3IBadueBPKnv0lrLiksW1iAaYbtH1tADjzJtsyIFprGO2As50tBavZt4gc4xh7AutHfKETD3PhNgdc_BX3O1LTIOZ9UL_MGPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=LaaVBJki3vC3xGxCur_sB_YqvAfahrj9Rg0oXOZklCecg0SIUGchnWg33ao4LjdvXxAJx43U7z8QBa8kMkXMyFvV44r0vHicnPTK8CdbCFUsNmbuNqR4S2RSJWDhxDuGf3nDMRs_DNQRuPOWufY0Qh7iWSrAL5kQu8ySkpkiCIFbyMCT8tZ3pztN0Z62SjsaYfQblpenqlxyVS5fzLJ312lY2Lxbo1Bad8k-i9_R8nRvn3DIkyvTR3IBadueBPKnv0lrLiksW1iAaYbtH1tADjzJtsyIFprGO2As50tBavZt4gc4xh7AutHfKETD3PhNgdc_BX3O1LTIOZ9UL_MGPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرخیو اگوئرو که امشب بازی دو از نزدیک دید گفته اگه آرژانتین‌قهرمان‌بشه به هرکدوم از بازیکنان این تیم یه گوسی آیفون 17 پرومکس هدیه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25820" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25818">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmYJ6fiq_ccNo6ABk7L_Z2u-uJ0o2vpGlF43vplJkrmSP35c74BKqrlKjqq4MtzRuZCaDH2DCYTDVROuD10n4FA_Q889hanbeltrs2lV91iGAqvwqLfZJDWUQwRepXhlZZvHpU0g4iKgm4upbi4tcjLp9caGoZA-quhOdts9SpXs1z_7XhgNNJtZxkzgVPwZGx0NMBqb1-deoP3WkMnVzdQDWgYEUrMw5O6issSi9TPykYwN0OpmkuJytTxmIjMzBlCNijaB0UKtM-obnBwzilLdforuejy_jjVn33xdIcceSRlDATKpAEdBQKLj50Y_RatQ3jUWaPhFiiCpTt64_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگلیس‌دقیقه۵۵جلو افتاد و توخل درجا تیمشو تا منتها الیه باسن‌جردن‌‌پیکفورد عقب کشید و ۶تا مدافع گذاشت تو زمین‌چون میخواست تاخودسوت پایان تو محوطه خودش دفاع کنه. تمام این باخت گردن خود توخله. حتی اینکه بعد از عقب افتادن هم میخواستن سانتر کنن هم تقصیر خودشه…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25818" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25816">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1FPKZem2D_GqdXjMSEUjAC0k-1NLaVITW7SYVNi8z1JPmd9VnxLPXJHrXRgM5_-krdCqrDQk6g8T907hAFHWyNuJ_ZJjwOw_zw-R_u43P04fvrSDo8pGGSHJ6aQZzitGKInAcmVb-cKwnaWC0W7MAGI1cc0XKRTkSUQl2-kT5NnQ2ee5icMU-gOB67l-CZMDvTTW-x1OnuTGkpym_2ihHI4-I1fvAonMWO3-8pVTpnr6KMTMcmk1ISurhMENHxeoAcTOeOaL77-fM5L5nxSmqCSWqM2JSDyI8cZ6pJCilZRKt_y_I_yf29zHCa51tN-Lh3jO8FROpMnYiWWOItSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بهترین‌بازیکن‌جهان؛ اون‌حتی از جام جهانی ۲۰۲۲ قطر هم‌قویتره. لیونل‌ مسی همچنان به نوشتن تاریخ فوتبال ادامه میده. عملکردش رو ببینبد فقط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25816" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25815">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeP39BCQ9PziENzDbszGIpTEwcVJX-Vg_YKvvTop1Cw4saLAGZUEPRzCiy45BXRpnPsfV4YVF_3Kw97j7ZvrXoMuGZzFFrVL_SMasPbIlDyBcP9_CkmExorirNbSVfybtyNjZ-vKj0l1mgGy2wgkYcCP_pGCNxTRC0kpL147sdjTMogpPb8kOtDSBtPY4rF0vmzA6zjpT0yBegR1I2l6oy_KL9VmTvqE08tzI3021dHH3weByJisSWlK45zUvmGT7x0b52IAHmvAkkasg9X_CJRH_bTGRkMqtLyjtBwBAN4cijVgRdhDKke3444IJBE5L7CKVe5J_G7R1X_2x-UtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25815" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25813">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcEFqQhZ0DllI0yiTumTYgOkTUiCeXYtkbix7Z78b8x-eYXkesKG9tXZWD-1AYtQ2jfHpfK1wpj3mw0zqvW7hlsto4Qy4D3zMzdK5CA-vzgZB6xcreujEM2pOAxzf_fKgUl0vesQZnvAngOyNWg-vVaOte6zdnrnKim8KplGN5A-mIDxrvzDoOTOh3d6I5ll7saXcEjufqYOLPQ8UhXpwY6UIr1U2sWvlIBn5-SWZ2ylS90GX2B66MBxZwMmi3ZR0TvHmjjL3QoCRfEriM8cJXq9p5696-wn-CLyofKqmrY-YFSiUGjXAnhmtZ_Wyhz6xS8v_8DwwVXk6lP9vbK5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25813" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25812">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdtY3jA-fM_JVO4hJo8sqpQOGFKNKB4esiAHWTDCKRJ-uWegfCGOG4YwYTwEacUKZnYmTGxeDqMl_oIXi6mWMaieg07uDDQxh-e8jAAAnlnZJ95ZDBAXCtxj-J0kuhds0GlbFdzzy9YMFFGE49AN0eWBMlV4uVGqWXCtvS8mLNcLUk4yyEzi-6yRLm3ned1cQKzogO_d22PQniX8Ak3jtvfLrXlLfkGGRPQm7OtabNzcHCc8M2bky0KzZb2A8DbEscuK35sE_VttvFC3WA02rJyvyng9j8-Vi6GfzuQtncYjMRT6XKXQccF7-qbfuXoQSRyL6Wk_ETpdShGFfRq_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25812" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25811">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOCYWebnztwqiXGijjhcwocz_s9UUNfysrJuw89OiLiztK7wDN0_33SMA_MzRaOcx5ApA1wGl3D2GCNvRQpdxW_3_cUvIAFNryUGQH6UwRIroVpDmAMABA9PYWRDDZmWVHxtyFVQ9QXwbapHSD0iQMKSMkrINbvBNibanUV4qEgldZCMwV_UtApiG_uOMMFvXg4nErV3biLinxbsCrWNsLMCmk6178lJD9puLacQ2UffAeHNdJVhii2sbc7sYBhv_lfIyPqsa2FpBK1QyYuP1Y4Wji5PjzFOx6_nqPMhTzJnQHF-7BQT_BOOVRuIPTa4g04k_5Ry0i23sNkbaWHwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25811" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25810">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W00okSFxNfJ0D0N3HIX_XwP7bB-zLH1Ky5rYsZLue4J0X0G4tbK1FWK7yHo7UCrKyH4TXX8SvRY7mcJd6cKKhRrbWP1k2_PMITD7tbIVb8aPjSyWTpc5f9IOVGLct7j3_NDxqIoDY-YNpKjdG3vl9NLZAyYw0Z3Uvm25CwhwDRBXrejXdiAaYn3pGvyrmo0oGNZyTzDYNtSbx2YCaEQE2hrvUNa0rJVwqySruQj5vzB0bfShZ586CbJgoJFaDHMyvo65cl4zmaQqZ6azGmYa1n7IU6Y_TH2xoyE2VfTXO_fNbOI9kWQj9phLsfIqXsAmbahdhd_Gys1X8344OCio1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25810" target="_blank">📅 00:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25809">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL-Q-RDq-_8XMFoCAj4POf8gUWrzvVIJAsoP3QNYjH9k_QY3R0_PJ3qgZThHkoHN3qjtWvwVMiKHMfZj14BASXi0x4gfPvu0_cDlNVXJExRK46xOXiDesXi7--ucG2vefQYWTYpSIfLNF4fyGKe2hQkV9JAQMaQOpgcxnBMwGGkbkfQUddDrHblYOtFjrMLttfCg3l1eU-s041UqxPiyZFBS8URBkdA_NxdNJTc0PRf0kX17RvvrvvV3-bIvmBekP3uC4Ri0c_GkMx9nft5r9vaNmKJzG5QIG1NjYSHtDwVwS96EfV_8-q0WkFPfuGfE0YaUmRfwlNTvmaayFvxWbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25809" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25808">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0JwCK05mSgC_k3CRdl48XzXFS78KGOTQ8EePKJJvBsxaYhCnlgrbtFyAZtcj7rv7_uV8ziW5zG78O0CdCjsg3UypOChJnM73P8WHBlxwOATeGg-6q4Ja4F-ZG5TKKQUBN41LzqC9FbnAm4qF1HAvBax8-FVBZMnZNQ3fxuH-RN_cC4tdaXlHTN76ZvJ9sw5KkfFWYyX3R1EB9ijpz5f1K9nTqnjEqgsyVVbrMvGs_5hR4WTR13GI61cL1HTu49VIV3AOeDjKHcA992AOgwxlnytT6TL0NmnjIH66HUa-feWX_fidcU4FpBoiNlOMku9ywKqWnKjrur9iZ-6GN_QKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25808" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25807">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTH1cvH-6lcF3SbG4q0TPyLNLOIv0VY8w_ekjob_1fgFpwwMANCWkXIaqryQdAV3_GcXQfj0nE-O_FmXCRnHnTaX6nA9-C-qkFqy5iM3IidXHH1htUoH6y6quINjRGGwS3hESTh7M0cu80gsAOZcluEOWNNq4nf6PW3JdoBjWi-GXQRdQweTQ3hiBDX7VDUvA4noJ6IRZ3jYk73TLYdUdcOpInsLsu3xVys-cgeMXe1C6NO4dzY_2owgm6nQKLw-XJkE47zSz1dy2Hl-a_4KhCCwldTaTiZ4zYkfHfe980f0133Eht4eeOrisczdxp9Sfuf_AJ2JVodWs2--zrNA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل دوم آرژانتین به انگلیس توسط لائوتارو مارتینز روی سانتر فوق‌العاده دیدنی لیونل مسی؛ این یازدهمین پاس‌گل لئو مسی در تاریخ جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25807" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25806">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=PKE2_iKijYoMnyOy_DxZyl0T8HwUkm0rBlp4kCRoCEvxOPTe2baY43NV4aDYw-3q8Jh1yPE9hQNGcxFrDYXbgNd5eqsIWcWGH4AY0qO0Q_uGYtxGGBaJOayX3Jvh48N_YHyxfkYB-ZCsOMsPpPvGIT6GRBkYjv7E8jBDRpnsqwZ6z3zkNRxlmPQwWB8t5q9lfSd0sTWIWSI7_d9B6oAIOzpDB4-vhQQ2BKlyoekQiwS2_vcDFrzHyqVm6QN-YSOR8wESs0NTXPvSrhObtky-nGt2TdDspIMOk01MFKS9AzY1p0YZrLf-Xjuvjy3qMju3GNBhKCuxYDfywCPVvQ131Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=PKE2_iKijYoMnyOy_DxZyl0T8HwUkm0rBlp4kCRoCEvxOPTe2baY43NV4aDYw-3q8Jh1yPE9hQNGcxFrDYXbgNd5eqsIWcWGH4AY0qO0Q_uGYtxGGBaJOayX3Jvh48N_YHyxfkYB-ZCsOMsPpPvGIT6GRBkYjv7E8jBDRpnsqwZ6z3zkNRxlmPQwWB8t5q9lfSd0sTWIWSI7_d9B6oAIOzpDB4-vhQQ2BKlyoekQiwS2_vcDFrzHyqVm6QN-YSOR8wESs0NTXPvSrhObtky-nGt2TdDspIMOk01MFKS9AzY1p0YZrLf-Xjuvjy3qMju3GNBhKCuxYDfywCPVvQ131Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25806" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25805">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=FUnmGUdL4rlIdZviFZ-v6h0vunQuECgFtMmjcvx5CEMHBk0j65Z-9wyySsiXPMiv6-NbFlfUo3ueauxpm1pbJtx1GZpbgwHJ3dc2YahaOpf4cT0_GR0i3YQ4-qOQHRsydVfRn5zG_tHGCP7gzF3QrWwN8_juS8_kUPzlOFLWLAyHRq4g12e66SkHnMPdvLf2DPeZlupLGHbsFrt2eilyDz9Azh0dvy38sQIpLrmjBmfv1omrYrm0RLScaJ0KbWf_bMdQRPRROwXKhJJXM6NwT6KQ3b2UaXDpmmt8pPC5DR7a_qNxzonCxStMjwkSa6tPkCCQ5AYekRmeSP_v1nh6VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=FUnmGUdL4rlIdZviFZ-v6h0vunQuECgFtMmjcvx5CEMHBk0j65Z-9wyySsiXPMiv6-NbFlfUo3ueauxpm1pbJtx1GZpbgwHJ3dc2YahaOpf4cT0_GR0i3YQ4-qOQHRsydVfRn5zG_tHGCP7gzF3QrWwN8_juS8_kUPzlOFLWLAyHRq4g12e66SkHnMPdvLf2DPeZlupLGHbsFrt2eilyDz9Azh0dvy38sQIpLrmjBmfv1omrYrm0RLScaJ0KbWf_bMdQRPRROwXKhJJXM6NwT6KQ3b2UaXDpmmt8pPC5DR7a_qNxzonCxStMjwkSa6tPkCCQ5AYekRmeSP_v1nh6VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25805" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25803">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=lGPw-6FfMrQBHZIDzpZNzs0A9K7RMMAXvEioiBbOGFB-yhFx2ERphvdIJIrebqP5nwrMyUn8nA1ik0sS08UBONpdwQlQ5Sujhw5SNNe1eQtHX1r6B8SpUov4hAuei_E9twMJMkDx6QEXcgrAIa0PFKIdUqhv1BZucPzyr3zUDQfIUXKkTQD8eTpxcTkxNRCCURS32QW2DZ4hiTPgDgUalWbjUFAMK55Z5KkWoRphqeq4k-V0jFXHniNGzxcaPHvNlJX74ndlvptfFfGLDUliGhvtIae1yzKC1DD8izX69x4d9rMKj49r_s-7ghgtHC0f6YZu6TDeb3tK1uvXulOpsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=lGPw-6FfMrQBHZIDzpZNzs0A9K7RMMAXvEioiBbOGFB-yhFx2ERphvdIJIrebqP5nwrMyUn8nA1ik0sS08UBONpdwQlQ5Sujhw5SNNe1eQtHX1r6B8SpUov4hAuei_E9twMJMkDx6QEXcgrAIa0PFKIdUqhv1BZucPzyr3zUDQfIUXKkTQD8eTpxcTkxNRCCURS32QW2DZ4hiTPgDgUalWbjUFAMK55Z5KkWoRphqeq4k-V0jFXHniNGzxcaPHvNlJX74ndlvptfFfGLDUliGhvtIae1yzKC1DD8izX69x4d9rMKj49r_s-7ghgtHC0f6YZu6TDeb3tK1uvXulOpsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25803" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25802">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrQiOA5yK0IYGidHBZpqIVi6bdB87yc139ykw3AK8RfiZuLZjToYHj9u2J5fW9x0egB_DWF4LlafXOXUpTVlQSaso1dG6pwuIG20mbgpQrAShnMjILZVIkFh9ogLw9rTIrq4lfHeyMp0apyZZ0k50YMcTY6SsfAP2Nfpnb58xlvQ57mHyqkKj8OtR2yQIyVNldxtzP8jxCSWYJnFDelcqLJ55RKf6Oeho9_nUACLGVFwr_HmIT6dc7POyX3JQlk9rh5kORLc2BbWNPmcAilhahyuSvPnMLscoMwCu7DeorRhrGA1gKysW_Xi0UbLU9OmgeG7yjRS5rbZFtvAifkWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25802" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25801">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F29qotqvfoZesTaAc1qlVQNKn7e-ar745NztRNQ2_1kjCto8q48IpD93WkOnaUtavBIywyDSzKIhr0smYpuAteryh-l3fnOYY01inq5NlddJUYUV-tyNeLM__etrVcN7mYsar8qvictYXIi70_6PUy6Gvebw3GiaVMWiC6CRXeZTcFHcqPRALHP42wcoB1M1fFztXJFjruhY9fUdJEJFMP6xeQ9iV5sJsMmBknDHl1JsONPpemG8wEoVD0SAag-Uah-E09EPLoZKbMOB6_KtNW1WTLNZsFsY7hHrMoYb7WN-JdzljEU3ruymsDu-UsziBjL14lQyIJS0jn7Tx8JawA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25801" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25800">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8axSPAWzmwnKQsPI8bjgwlz7mRCIBI8h1AahwzB4TgQqMFA0J7X0HPlefynVvM0MO7Dp4AG1S24QZnNT1chsIwk0zmm4OKGOZWWINraGp7lO22A32TjO9qfIOoNGr3tckeaS3uG__bBYw_hYpn_SIqzI9TL2zS6BPc1S27pCMKLYIKeVw2sRme9zyu5Qib8ICh9F-DPVjobFAo3vA-zNxf04aQqSajM_DaJVrtD6E3B-3T1Or08t1mDILhAkX2ZC36i79OTz5wT2b3OVEfaNoNSAgYjEj-3SSqTgzseQPffPCr0uh8a-k_mcS1z0BPoeJ5fMolOQqJfs8OoYZOmOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25800" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25799">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=KtlZERYcuoE0Wpl_wg8lM4aHP55sKIxjSMVTfcvMl5f4N8AYgculIyITM6FQOo1GDqWNyNFceaoMHU6F4yNYbq4tidZIoXp6gYir0F9HPLpyrS4OCqILJD0w0eKECqfkA7BfvIhZGGVCt2n55AyJG5NcJU5-1GtJy1kPo-kQMqqCAf6I-zI5hw0EHsny1QpuespyU-7Z4a53-vlTYLzuOfgYiBhWDIs7O5uT1gBECtXTHB6bGXwI3EC_Zd3K-gbF93UQLXmIQS0WzwdkIyhU5-NiJR9u_eRTFncKNYK5DfnptHDWoYg_A2yxpmVyIUAatIeIFvZAVbelAU13BcyTFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=KtlZERYcuoE0Wpl_wg8lM4aHP55sKIxjSMVTfcvMl5f4N8AYgculIyITM6FQOo1GDqWNyNFceaoMHU6F4yNYbq4tidZIoXp6gYir0F9HPLpyrS4OCqILJD0w0eKECqfkA7BfvIhZGGVCt2n55AyJG5NcJU5-1GtJy1kPo-kQMqqCAf6I-zI5hw0EHsny1QpuespyU-7Z4a53-vlTYLzuOfgYiBhWDIs7O5uT1gBECtXTHB6bGXwI3EC_Zd3K-gbF93UQLXmIQS0WzwdkIyhU5-NiJR9u_eRTFncKNYK5DfnptHDWoYg_A2yxpmVyIUAatIeIFvZAVbelAU13BcyTFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25799" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25798">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_yKkza6KYFUfJ1rYTlitJQbmASfdIkQo509TR7drT48e45x-DjibM38TsbW1nX989xXOwLMEhOFWJ2yy5g8bfoqCIKtiN2-MqteOquVC_-FHkNfj8Bnj4oGjp_7fEoDXuO4jrUfxPBLg2WiU0sjjnYes75ejmRhkHt8RjhrXjs_l7zlBzyBPrpBSnQlVRzItiRVtaJSAWgM2fqbMqiGDFrzchJjh3myGTzwlUouTJBjJKi7b1GqHUP9uqgOJc5yfIQWM5q1oSAzL-KOGc8S8g2vLq492ZFKhWfeXF0ZG7rCyTXcetmJSrYZC19xLFGk-6HVSKvSsxB2wGPtEMkQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معرفی زیبای عادل خان فردوسی پور از مهمون‌های ویژه‌ برنامه‌ امشب؛ علی دایی: تیم ملی ما وقتی‌حذف‌شد که سردار رو خط زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25798" target="_blank">📅 22:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25797">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c436909609.mp4?token=Kf4Tv_rfDEQOiT6amI-wRYWg2vU9eKAEbW2YHnlTs_Eb-xhvQu-mPVp13T--cY6sF_cWvFI_U5Vgh6VojREc4fMjV7v3neEGgG77BSgIw1iFMFs43JARjRoqNw1KsrC12TrQbW8z4xihEIlp87NdeHc1159d90Ce7NZbUutwdp--CiizzZAsRKIq6-n1szsVAaFDxtQsRQtyQyfNp6ZmYF3uAzJEjbS-vM80CY-gMXKpbTjOV8AL2lH4sivsDkeBVd0cBdDr5WvqrmuDARh-UwDaRFN0Ta3pT4Bi_G-VLDSpNuPrreIFIIgMDP0o3Q82TOPy5_mm4jlMOvC821-HNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c436909609.mp4?token=Kf4Tv_rfDEQOiT6amI-wRYWg2vU9eKAEbW2YHnlTs_Eb-xhvQu-mPVp13T--cY6sF_cWvFI_U5Vgh6VojREc4fMjV7v3neEGgG77BSgIw1iFMFs43JARjRoqNw1KsrC12TrQbW8z4xihEIlp87NdeHc1159d90Ce7NZbUutwdp--CiizzZAsRKIq6-n1szsVAaFDxtQsRQtyQyfNp6ZmYF3uAzJEjbS-vM80CY-gMXKpbTjOV8AL2lH4sivsDkeBVd0cBdDr5WvqrmuDARh-UwDaRFN0Ta3pT4Bi_G-VLDSpNuPrreIFIIgMDP0o3Q82TOPy5_mm4jlMOvC821-HNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق دستور علیرضا بیرانوند مجسمه امیر قلعه نویی درمیدون‌ازادی‌ساخته‌شد. بیرو دیشب گفت هر مربی دیگه‌ای بجزقلعه‌نویی این نتایج درخشان "سه مساوی در ضعیف‌ترین گروه ممکن" رو گرفته بود تا حالا مجسمه اش در میدون آزادی زده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25797" target="_blank">📅 22:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25796">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lim9CgYsEkWROadF4F6CgtyqdyWdxHg8F6d2nr2lh1QTHcxr-NxtgLkWRZB46eWtDtTlcMh36YAFTBJwB4d3yaBL_BexhuvU6JCwSIuvDSbkBcbfyz4T7G22L-te_6W0ukwK2BOhNtmecde2UR5SGwY1jJh4Soib707eOOGzmV8SzFBmYqC-nt1waucPGR0D6tAHZIrxKCnLnfjg41WmsLF2wuW4p2i5jp3u5m71J8pFdBelzG_vWuHmKaRUbqudFN5E5iYElBDiSWlmDcnofOEkO9XSnkePSDl1bmFmg0NL3jhnomCNmw6zPR0R6EO5Qg6IBUdf28ujihHWETROAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هفته اینده هلدینگ خلیج فارس؛ تغییراتی مدیریتی گسترده‌ای درباشگاه استقلال ایجاد میکنه و بچه بالاخره از هیات مدیره رفتنی میشه. شخصی که تاثیر زیادی در جدایی ستاره‌های این تیم داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25796" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25794">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=gBQW335Jasyi0ErWLeGO14zF-EbMV7PhH099NHqK_2FCyiejDUPZGv3Wuyv87Tl_DPsUPqUgl0PdtXGX-ZZR-RupW2hl9tuqPoG1Uadeguh0rEHKM1x22UMJz1wcDHdlDoaMAKarFqiDO0ZFl8s2RkdBFVWrN6XVGz-rF1FZpnTifi3BHGdmcU-TZ_bxc2NNMK1R8ERiOeRHZs0_7Hd6MRPPUliFGIczgC340kKZakd86zYJZsf59MCSpalJ3J-T6A_4B9XBrmRBtELWVoUJUD3EwZRPrfeNn-2JKB7x-dLw9sCHCij-I5bJD-_46excmE0kBef8HrLm4tcbBSj0Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=gBQW335Jasyi0ErWLeGO14zF-EbMV7PhH099NHqK_2FCyiejDUPZGv3Wuyv87Tl_DPsUPqUgl0PdtXGX-ZZR-RupW2hl9tuqPoG1Uadeguh0rEHKM1x22UMJz1wcDHdlDoaMAKarFqiDO0ZFl8s2RkdBFVWrN6XVGz-rF1FZpnTifi3BHGdmcU-TZ_bxc2NNMK1R8ERiOeRHZs0_7Hd6MRPPUliFGIczgC340kKZakd86zYJZsf59MCSpalJ3J-T6A_4B9XBrmRBtELWVoUJUD3EwZRPrfeNn-2JKB7x-dLw9sCHCij-I5bJD-_46excmE0kBef8HrLm4tcbBSj0Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قابی بسیار زیبا از سه مرد شریف و عزیز ایران در آستانه دیدار امشب دو تیم آرژانتین
🆚
انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25794" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25793">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=lwD2VQWyAp6mESmecYdhqOnrJlNcSzkU6MtJouVPIIcdmHPYo6oLIA16PuutS0OSDa6VRtDw4IG7byO0zrxIT92f7lnfdP_X9ihWoTugdWxR6CxCXDhnZfOLO-Vka6iH4MFWHwfCeNL5XkmrbLCdyCCIW_QRE5oBpPkFlgLSqDYR04U-qfxB19dQyFZx4td4PL7wLY3xLOX980wjilFAdkDfld40N7zC8NExZEdbUnFT_rAsH9twymspUfa7MCfy3a5qoxZ2ooDV3WkKkbmwE3zLumTvutKqHOMfDcufYstOXJsBw6_wwPIpo8Gsu0S97QP30gVnlHon0OWUkcU7pYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=lwD2VQWyAp6mESmecYdhqOnrJlNcSzkU6MtJouVPIIcdmHPYo6oLIA16PuutS0OSDa6VRtDw4IG7byO0zrxIT92f7lnfdP_X9ihWoTugdWxR6CxCXDhnZfOLO-Vka6iH4MFWHwfCeNL5XkmrbLCdyCCIW_QRE5oBpPkFlgLSqDYR04U-qfxB19dQyFZx4td4PL7wLY3xLOX980wjilFAdkDfld40N7zC8NExZEdbUnFT_rAsH9twymspUfa7MCfy3a5qoxZ2ooDV3WkKkbmwE3zLumTvutKqHOMfDcufYstOXJsBw6_wwPIpo8Gsu0S97QP30gVnlHon0OWUkcU7pYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#فکت؛ ‏بیژن مرتضوی تو فینال‌جام‌جهانی حضور داره، اولیسه و امباپه نه؛ تعز من تشا و تذل من تشا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25793" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25792">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmS8igid4sqQWQXR4pkiipgD6egeVSHE9VxTALZxw04l_biFAXpMcjhdhNWOSgaqX55YG3rsZjuDTIDO32HVzxqj_8cgzCP96DF2lPbD047SbCmh-PilfOHMb-G3S3lPJF2HQ8uR-igb_h0RrcBsz-2eq_tVu5s5W9rvFsmgRXQOJARrA5DfNn6fRD4XEpOVfDt3HLAHXHkOn9FNM3t6ftCA9fYyO9DwtZNaUvCEOdOn2UTluaC2b9U2-ozOQP1WN_Inzsf4vT3Ew2dXSX1P7AxY4yJraUgWT-Y_fbAPmGR7RL4xRxV_9Ky5AzXkeogba0bEAGjyi-uRPSOGBfZD1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
🇬🇦
#فکت؛ با دبل‌دربازی‌امشب مارسی؛ پیر امریک‌ اوبامیانگ برکورد 400 گل‌زده در دوران حرفه ای خود رسید. امار فوق‌العاده اوبامیانگ در این فصل درمارسی: 18 مسابقه، 10 گل زده و 8 پاس گل.  گرینوود هم که در منچستر سرنخواستنش دعوا بود آمار خیره‌کننده داشته: 15 بازی،…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25792" target="_blank">📅 21:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_sKnxrPw3yz9zH7kzQ7lUIUmspQ6lJ4Clrkjtq6bUAm7DCmwwjWlTLX6IHmV3RZz0aNGHzdTDLQo425VAj5aQYTMcCFErtMq2P110LMmh0cIOpHUwVrw67f9vh2HTjXGBTr2LCEHYIwfCbsJufYBrTuBj3f7OxLSiNiKcGClPLdbtpesul7vzuafVUvqAYeiktX8IRtcKfQOZyT0FJ0xD-2fCn9WueMQxLqoV00oAJJuiHNI69DKNj4WxiN7Vqed7WHPTayO9gSlE8OATZaw8Jj7820roK9K87Sj9DG28tKb3G0SHxpDpTekgNI2ct5YNUQ26nDC40nVpPpFNQyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujeq5gJ-57d7ZHfQMDKRXLn9Xg7F0gbkmqywZgPzlQ5yCljWI6IcuoIDV8gJHTmytpjsEAuBuC-jvaKNpgY2G_HWlIwuJsT9uBxDQVB_l3s0uXdYedfajbyr-cRZGZMhURISFai-A0jOiVy1mBMzWomSha1TeW9FclxzXhmMO526nYowQZ6l-nGU1-_SNtRtpMorJEnCGScDGcPbiKWuiQjMN55hjK_5A8Opgq8-lKdp12lRV5v7u_2E2zHsXuRqu6InnQZtXE3EYwsWcuOjnx09a3pSpcaCF50yCROXkPnjcev73iH-QEnQA1HSsebhMTYPkIbttCPHj4jtHasWwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی
؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25790" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ9T2njBY-uWgWA-wwFv_bWk9Ps078IJamKRsWWlMZxeeGTVAzuOTLOVqSKACgpTVSCXEn2Wc1Dke7T7gWXDKQ3B0UDTbvBYV5M-ULA7YElLLph3EERDb29ahGXmmZcIHEUi6PUyLCKm6X1TkzofEKpfH6pmJ6Jzhdcblb7oD25omKYPcTmSGwZs6VyIMNB4OVmsa9SHjaJoWnj5nTd0TCfHGN_YZTPaakWtzrQTL2TGLTDLjYLx_CLB8EmhcIAJCDtwDWc7NP950rN8IyGSdv8uIW4En4zeMAeJxlG_H3V3gKzhPWgrKGHXmHp_qveylGLqVeb5pzLQlKdmmUYgWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25789" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQaRW7Ddcf4dpD5ksEgqxZRYrxqlNlsoCr7R9lRHZm1IlKFd5XlsRK1n1npIxnMtjujEh9gWNqZ5rmFknsT0NasRf-nDObQ1jOLRjLFsp9FFc8Xp8N7NYv3IbFU6mhux5ogjjvkezxFKFpFnotJZDI80jRMOEyStGEnFPHHWgrNzuh7bEfW30KoODyDOjdiUaqIHqr5AJimM5tQ6qGy9V3i2MgYgt-pef5bBu__jfL15mH77hlCDk88acbs87GTB-DQmulW67Htq1_ez6tjisnR7vJ4KAGiyqgVHZD0dFIw6PXnNqNjs6YuuTTXaLwesEJWsSjyZEjr8FBQ5CSlO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لئو مسی در نیمه‌نهایی‌های جام جهانی:
دو بازی، یک‌گل،یک‌پاس‌گل،یک‌برد، یک تساوی؛ هر بار که‌ مسی به‌نیمه‌نهایی‌جام‌جهانی رسیده موفق‌شده راهی فینال شود؛ این اتفاق تاکنون دو بار براش رخ داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25788" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=LKgD8Eny_3wwmpYVFgRIwR3iw0JFyyqtXiIhviZTC0rl5G0lUaiSsohYE9QfWaFG-rT7-dKGipcG_Y9vhnlaOeBZY6j8VdX1CKCyJCUbmDRobE8KjWJPHR44FNXo3z6rQVxd36QybTtfvUOA30ceF6923Dwhqi4TxF80z29qgnQ7mXAgq6TKOVEwAfWhdzeIjAMsIhy0K_vSoknqAqIyx27EcAYMvCLpQb1aunBYKTXsieJy-19MJFh7o1XRe_fSxheRX0KX9qrzs99Hj3pj8VAaBdxFOYrNwuJfqGV5YssnX_BzPav1QNRI9tk3Q0I0J1aYdvVJyXIkQuVWiMSm2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=LKgD8Eny_3wwmpYVFgRIwR3iw0JFyyqtXiIhviZTC0rl5G0lUaiSsohYE9QfWaFG-rT7-dKGipcG_Y9vhnlaOeBZY6j8VdX1CKCyJCUbmDRobE8KjWJPHR44FNXo3z6rQVxd36QybTtfvUOA30ceF6923Dwhqi4TxF80z29qgnQ7mXAgq6TKOVEwAfWhdzeIjAMsIhy0K_vSoknqAqIyx27EcAYMvCLpQb1aunBYKTXsieJy-19MJFh7o1XRe_fSxheRX0KX9qrzs99Hj3pj8VAaBdxFOYrNwuJfqGV5YssnX_BzPav1QNRI9tk3Q0I0J1aYdvVJyXIkQuVWiMSm2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
چالش ترند این روز های اینستاگرام این بار با آنا ماریا مارکوویچ ستاره تیم‌ملی‌کرواسی با خواهرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25787" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPyyL4FxznNKXEPpJLP2YyJbixwOl69wLQ1PNQ9bkadg8p-6Zc_dUE0u5ZSxoTELUqfwnaVBwRIWEtBFOlZaTLEuMce5JZAPw3xlLcbyVUgASJkI3ey_1KGjswSBu_AoPLWuk7YaJRcBTK-SupYBJbT1lepRhkOa1jmC6hj1ZBkmhEsF52kj2YzWIdwvLSocWBAiUqMWUwbUlM5Tm2iLMBzvabcwx_JlSdxOG1mNbMvqq7yeF60k7GcGNdHpFbBHs81F1sPX83Nl0KQIL5n88mhF40_JtFJhR9CnfZtSI4_bYNxLGMUj4AxqbcEVyNfkcYRU-bU6pl9yDMnGR1xDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— آرژانتین
🇦🇷
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
📶
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی:
https://t.me/betegram_bot?start=p8_r4EF37DCE</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/25786" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di4H74VtZhOr748qHK-1uEpy-OltnXsO3oY641cXkkGdF_UlZpODQTgjV-7uomOjwFiqb2coisJLGWOCQuCG_7-4oMTxbJrodVhGxNwDhy6-zWhJdAWe_QvS5kHm7OZDfes0e-gQRND8V6DAIdsgQ1FC4fw4g-KX7uvW0nv8gu2udF-3n64JRdSaAEqQVdtsa74VG9rBnwyqMK7seJPdhengPCG6Q8E_dtR1_VKgoc0Clg7sO6_C19Ey_CRrbrR7KWWyDzTzlfZZsFDr62QTTv-SIjPYyJr3fyP1GXve7yanQeXF79lg6af--KdSqop6nqVAa3J38xG5TUulGRaE-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌دایی‌ و کریم‌ باقری دوتااز اسطوره‌های بزرگ فوتبال ایران مهمون ویژه‌برنامه امشب عادل هستند. ویدیو کامل برنامه رو در پایان این گفتگو میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25785" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3tljTi6CFlDkiMZizfTVz2jYcQc1xsrzAly1EyarW6gaGKaD_bJAl5xOPBpRZgCejOCgUSKUKarUqv3rD3NeEQj6pKFKpTwa-EZev8sUiLWH71yutg0lyaUujgaxTT6Mk3YPYPEbfLpOQqRO6nqhX1_6molSiFuw_vqg9ri5n9cfBC5rSoVYhzeeiX4GyLp_r9dXymSQqiu7FIBMSBHZAfT__lLbe7MbgUFUn-udhgIw9TRFP-oVi5rdKJuTI7nTZxEW0TwGcsnwKeaF-AoMU0a50ZC1bc2biCi3vKt1SoKYjBRYPiWAbwpHONd5zhCI3wY5Or6e3HpHg3rohK5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس برگ‌ریزون بازیکن جوان تیم ملی والیبال در بازی امروز مقابل تیم ملی اوکراین؛ خودشم فهمید خرابکاری کرده زد زیرخنده؛ اشکال نداره این همشون 17 18 سالشونه جوونن. اونیکه تو 33 سالگی و اوج فوتبالش مفت پنالتی خراب میکنه اون درد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25784" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTMQ7aRlXpmQ96CsAeMS5_YdnHiVToj296b1xyEs8YWiLeNVXeGjqloXFPArfD4k-TDKHNsX6TZTizItPGeN8gIbRUn76SNRxj_HRAHBq6qXjJh1nOkC7HD0r8DxhfR18HcusBC6Q4pePUcimjvprsC7yj05uWYNWqTImw7tAka8GPaxIgNQXf9SYjvS9lmwwNa-ncGw-jX6xmsrRDFu8k22WP44wCWHlTmScI6e3L7z2QUuzRZ_ysdlOQoWHWhZz1pRhZRR2u5z-zXTPYnkxXPChhwQOKwI2kSlHjIaTSQ1U_B3_dmf675qI_hqhgrLUAK_JrdSPbIlOkDgKwc-Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
واکنش جالب ابوطالب به انتخاب بیژن مرتضوی بعنوان خواننده بین دو نیمه بازی فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25783" target="_blank">📅 20:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=lhqsv1Cd8i-v0crSkJMNPPww-k73ck5vaNx_V9Lec-jozZ6PATzZ-YFuPeYWzf1UQ8pIVAKQNaG0dCrEeN3am43wVXMSSaZN7T6IcZ_M045XsQrtTAKa5fArtUQYbEN25UWdHdo5k7e8YeyxFoKX2N5K-HYhOMQk3ga0KI3uYvGmyfdmhOAI7UYryuIrMttPc4YfHXJHotLdMHNMvLsCyouq_2T-j9iQuNW8KD1JftpQzdYNBVO0azYwz5-V9zrPaLrT6x6RRZ0Fvbr8twYsvvz808JV4tkc-vqnpiPdkooXImPEf8Z7yQyZ2BB8c9OfnKrtArIgP3D1IZdmA3Hleg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=lhqsv1Cd8i-v0crSkJMNPPww-k73ck5vaNx_V9Lec-jozZ6PATzZ-YFuPeYWzf1UQ8pIVAKQNaG0dCrEeN3am43wVXMSSaZN7T6IcZ_M045XsQrtTAKa5fArtUQYbEN25UWdHdo5k7e8YeyxFoKX2N5K-HYhOMQk3ga0KI3uYvGmyfdmhOAI7UYryuIrMttPc4YfHXJHotLdMHNMvLsCyouq_2T-j9iQuNW8KD1JftpQzdYNBVO0azYwz5-V9zrPaLrT6x6RRZ0Fvbr8twYsvvz808JV4tkc-vqnpiPdkooXImPEf8Z7yQyZ2BB8c9OfnKrtArIgP3D1IZdmA3Hleg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه بازی‌های تیم‌ملی‌والیبال+جدول رده بندی لیگ ملت‌های والیبال قبل از شروع هفته سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25782" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=e38boZs32_q_LldFitgk3zEXQndSZqhF8jGogQ9Oo_gz9fmBfo-siw7S5dAJOYZfgk_wZULciNYSmAHvaBrGUXbkwoF33PeG5Ae7fppq_miUjOSl4L-xYge9R5wMl9dzH-BInWsZ3WotvnBUJipSd3Ep9VzxWHDlP-QAETi-FMp3VHpLLXynn0ntDOVHqOhqBadtY7t45cI-I9s1UuNT9ZjfThNrHGLy2UvsQeff44sMLMZB23Bi_HDriBSXPS7kkBxxgKfwDI-GCSGBq8KSc-69jkVKqVnLLSUHg0bNNfBPM0sa1doU2LcTc_cfOPwIxqlre8mQnsFkOXJdgKkjmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=e38boZs32_q_LldFitgk3zEXQndSZqhF8jGogQ9Oo_gz9fmBfo-siw7S5dAJOYZfgk_wZULciNYSmAHvaBrGUXbkwoF33PeG5Ae7fppq_miUjOSl4L-xYge9R5wMl9dzH-BInWsZ3WotvnBUJipSd3Ep9VzxWHDlP-QAETi-FMp3VHpLLXynn0ntDOVHqOhqBadtY7t45cI-I9s1UuNT9ZjfThNrHGLy2UvsQeff44sMLMZB23Bi_HDriBSXPS7kkBxxgKfwDI-GCSGBq8KSc-69jkVKqVnLLSUHg0bNNfBPM0sa1doU2LcTc_cfOPwIxqlre8mQnsFkOXJdgKkjmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوزیبا از حضوراسطوره‌های تاریخ اسپانیا در حاشیه دیدار شب گذشته دوتیم اسپانیا
🆚
فرانسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25781" target="_blank">📅 19:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=oYiXOW76uImWkTfTLWIxJkb4Remh67zgD3msBLdWy2-FLrkwLjSnBFKXKcXGzuh-Cxac3fW2ao9VBa9jGP9kKCo9tMR47uKNL0Tw9baVOzQwKTufo_o8j0HXolBRZvZbj1_v6BHOpFOEMif96XqtPe7V2da2qb3reLqoFEvr9wZ55ziXCpa3J8ZsNjj5gfkQ3jMghrENU7D2h_YJVvEMaT5DlVN_hpizw7-udfHZW86z_yO5hFGuDt4fb95X5KJy7LFmpCJNJWp67fX-bmOJo3kQjJe6UEG0xhO8PUWsUtm6svBsTwQlCNYtiub2DBYrSHH1FtlA8b-SClfaUUrCHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=oYiXOW76uImWkTfTLWIxJkb4Remh67zgD3msBLdWy2-FLrkwLjSnBFKXKcXGzuh-Cxac3fW2ao9VBa9jGP9kKCo9tMR47uKNL0Tw9baVOzQwKTufo_o8j0HXolBRZvZbj1_v6BHOpFOEMif96XqtPe7V2da2qb3reLqoFEvr9wZ55ziXCpa3J8ZsNjj5gfkQ3jMghrENU7D2h_YJVvEMaT5DlVN_hpizw7-udfHZW86z_yO5hFGuDt4fb95X5KJy7LFmpCJNJWp67fX-bmOJo3kQjJe6UEG0xhO8PUWsUtm6svBsTwQlCNYtiub2DBYrSHH1FtlA8b-SClfaUUrCHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
#نوستالژی
؛ یک زمانی میلان تیم نبود مجموعه از سوپر استارهایی بود که همه جام ها رو میبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25780" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25778">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ki1UKn9hu5NhTM2Z9YlHEhbthPwqoehCmfwt7v0t2uBB_5Kzb5FHSWaBcwQj5e0qmbQkFJDleJFqUuhMV15YXXWA20VcB8xx5jytKGKLZfoScDKIZMRF1bVLAEITQwLti3hiodwe5TpnH2YGGevZi0e7EsPeO409AJmo26BRTHGLVsYn2hnL12qE6YXyllfIdBDTl6LltRBj-ry76WiC8gmJBmQbXCqcZk-2SLtMQm1shvCK3zFcN4PDekQl27GVl-NMTwf-Ze6tuK62fKIAUmHwR9oltmIbU0PP34aZK36CAybPpPWWolbaUuk0Ya6xxd8G5VaaPItteKaG2C8IeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mo08UxTSvDGUeX6mp1WRBtGct3S2L2YazMqnZDhVO40oD620QCWckfpJ1TzGDqsjcXp8HL5jOMUYvyV6Ck48HpEVLa_QcnwP0UDqOoQ1HIXt2d0bWIC6N5tB681TCeUlscFXCGrz2YCCD-ywaE-oQ-baHaCs_yHd5uzToeNhvnXsbGpntwCjCGm5LU2yKLKLpoDWS9S-m9YBLEMz0vp4mKRqt8Tu4l7JMAv89rvCDCFDg57mjNvZIduZ2qlw8Wgh1mD1xMZMQl6mYAacDXPIOwHh4dTOzbgdWfNqiI-6lAG7QTdABTDbEtUt0OIIMj3BubYVM_tmP_mA4jxoOOdLEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
👤
مدل موهای جدید مهدی قایدی ستاره ملی پوش النصر امارات؛ اماراتی‌ها رقم فروش ستاره ایرانی‌اش را 3 میلیون‌دلار اعلام کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25778" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25777">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGhuibfDW9Pt_L4dl739DbbLHlHxqdHlrx7Byee3fm-pWgmpaEgYy1rYMoOXSIHVu69r_oiCIAvTtRsI4oPsyUj78LGJn9-ZxhcH73ZNicDk1cQuxc5Wczxcxp7dKrb5tPOvMYHOtmmWjSUQhcYQyF8XJXpMsAvA8kpA1BPNKMKZP3JAVzFNN5znrICre-uPVDaulbX-y_IilruzxzhyW5iC6dAg0xwVK04ZNxSOXj7Xmyt4cE7FmcOR80ZDM8Cfb0uvg-AJfzsSKotFykj8BSKPlmYaWROVB1oHaFPaTDez-kIZMekw8ladaI2_bHSXYqTASPyb5KAWyhAiajS_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛ جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25777" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25776">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRfrFDhccTxJT4ED7lhquFYwuRuDpnN89E09_hDuQGAp7ZoWBTOPuZcyc2vSuyTQCD7DRxRQTjx-Q8TlUU3kUEW5tRCa05-ADOxJ10sxCK-7AjTtu05Ir2FNpg91FwPG-6sGDfGYf5llO9roceqOYrP-u-YcQf7KdGTZbQ5pcUpMJ2LvH4LZB9UtQ97YNPN3e8KWo4mYhuY83RTm9rPFxAkpkVhPf5UEB0BaJ4AuhsWr2T6q09N7vAcCX-0C4JGrbBIEkBGEmJetPbqywk9ThnVVK5HE2oTOD10n6DNFp_nrmLSv2geZBiob2DITkhq_NAytUsCY-zJC-VqSVvX2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25776" target="_blank">📅 18:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25775">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOrOST-AnLer1-v5M-VBjyABJtpkhndJeJIoPFmwAjQlQYQkl4KrjeWVPIX-AA0gITP2aEVZjZY8SUkmaetDqj6VOmOxtfNrHm1NLKslBp7NzEcWwMwzxZ7AuFQGe7occG6PgzCpM9l73_xOS3RH8oPbXfbg8pZsuuHlZlr5xAKYi1V9hkON6HWB6AtD_deSEemAQXUOPjvPgT85bs-AnUbk1y7Bc62koIKWPJIvz7sKvdjMO8l8GenobkXL5HlsxRMoLHxyf7tu6Szqhq-Ex6IstsqCW0OWSTFSXS-ndRz83_IPdLV5PxEQclwjBLMloMfC-8vxN2CFPVpttkaxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخبار دریافتی‌‌پرشیانا؛ احسان حاج‌ صفی قراردادش‌روبه‌مدت 1+1 فصل دیگر با سپاهان تمدید کرد و تا 38 سالگی در این تیم خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25775" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25774">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul61GhEJgCli9ifk-C349AKnNxrall8wnsUJcPyWoQmNf4upqVCvQU1Tm5ZkVdxCsWXXuZN4CIYaeDq4blR98zb0QUC9YIXxoZQwNM7kDcO1Sbmt3osAEu4VHUh0Yt9u-otpw2rMDTocoN_hPjFWvfqmv-VtC3I92tsojQXV53kKum6ywiRRAkg_jiNgx3afFQiTu4ngb3G1QxfczHt2S2V0_ss6jiQJOFPSHdU_KwrnKHT02eMR75UOF-sYP2eXlmIRd2JUmlqvqyAuA6kWDcoRZ_jlSKDweFA_lySfIkZB42u7UgWcyd9vPPrJXfOgGMoYHtqOtE5elAw-ksASbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#فوری؛ سانتی آئونا: مایکل اولیسه می‌خواد درهمین تابستان به رئال مادرید بره و این موضوع رو نماینده او به مدیران‌باشگاه بایرن مونیخ اطلاع داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25774" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25772">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQiErxKK1ayZWN7U-rMul-PHK-dn7GOzT5Ywx26aAMaBzFsLdS58kJXdOPViO8YMa7c_gGPg0WJEWgpJ30fGwpP5LtBhNqTEjRokhHZWjBIxRU7gQhjlNEm04Tn8Cay-44HcuTMf6g3dJq401BWwcUSvh8XcrHM2j9tEg9XXovTJLVpeJ9DubhxG1HXYXzqsURx1dYPY8pTqipoRJRaXkok3A8TTogZZt6kx_hxxQnGw5zyjNFGWVR1_tKS_de_wSUgZ13yPNeawGACfiu7w3adr2HwKJ07Cn-77lX8OtBBgckivt6R8xI9jP-r33CrB6W0pN_OnK2lnyVPH-HJ_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
فابریس هاوکینز: مایکل اولیسه پس از جام جهانی دربارهٔ آینده‌اش بابایرن‌مونیخ گفت‌وگو خواهد کرد. اگر آفری‌بالای ۲۰۰ میلیون یورو برای اولیسه ارائه شود ردکردن آن برای بایرنی‌ها سخت خواهد بود. پرز رویای حضور اولیسه در رئال مادرید را در سر دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25772" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25771">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msa9--CQTdQXSOiRf3FeIcWG7junYAJyEEp91IJBauMLPwiOZlrOysgEC_FlZQfXlALd-wPfi3m0sEEcgK2xqSq4sXM3VtcMmj-h7Yl7Fsyd1AGg7TZaOf5KyLojZBhidIOPZir3Zm2ADDCdN6Y7hY7w19i_cclIbyPZeGQPeCmp8WaN4hSAPcOekl0dX1H8FVZqL9Ba09Llcbz7iRu8tVe780Nla0UIW7i64wdKDzNFoksAoAISyJsVmc0STJ82DfO12ct-5rjTtBfvbpanRHk6zwGbi1D_j5sH69su7kr-iYv-tcXzVUAdZmKSX1j9bJ4hYydu0eOpDQGwrvTgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی استقلال پنجره‌اش بسته و دوفوق ستاره فصل قبل‌خود یعنی یاسرآسانی و منیر الحدادی رو از دست داد که فصل آینده نماینده ایران در لیگ نخبگان آسیا خواهد بود. کار بختیاری زاده سخت بود سخت تر هم شد. ممکنه حتی بختیاری زاده استعفا بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25771" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25770">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_wbGT1N8f0Ky6cGY6pe6qPF4CI_bIn6nRGDNYlXx9iVMDOloHUlXAxzj0wY8tGMGXkBcQQcQx195eCzHxScduMj2UVVTROMZPZCHb5wz5mgfLVu5iMgObp0TPOa_zxAfRU88ZSF4npJNJX7dMF54vYToa489m2jkMIc2VONndFUiDBlKIsoYY8rKb6BWtg0BxKkpR2GuM_rJZHya743D7y7q8xCinsXuC-uEdBFMqhd4OxqsTcd9noaWvXJ03NhL3-zUZDyscgIkvX45LfvEWi32j9OpALI8vSiT66MjdpMjmoYOJRzwtWbTJW0_7xrje6Oyde_ufb6HULck3gnsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب‌بعداز بازی فرانسه و اسپانیا درنیمه نهایی جام جهانی؛ خونه یامال تو بارسلون مورد حمله قرار گرفته. دزدهاداشتن‌از دیوار بالا میرفتن که نیروهای امنیتی بارسلون متوجه‌شدن‌وجلو دزدی‌رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25770" target="_blank">📅 17:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25769">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1IfJ8HfuX7uYfjKs72QzvHe4r1zdvWVpWuIFStRRZqUY1unhEPAfAc9pjoyagBaZikJiA_KjHzELFUCzGexy9nDsNk1LrLmElDT6BjP3DwH0aIGbwQ5OmlQB1rqzJKperRgs0eJZpuL46O39thN7uMC5YxzDGCtGzU_JDvuGKajNEF15rK40I_34syrh0w2zt9zPDEu-cUTEnvTQlf_TYUVWOO6vEM-ONzQWnoOycg3ERj-zp2j2ltybvVcBvqsQm_RKbccEZNcBvb7ZjPzX91Z8GpWxyFoAYVgazG4aprlpNftUdy1UxVu7_4HDg8czwXiHlGBsohuqT358ByPfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/25769" target="_blank">📅 17:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25768">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1tEv0Ow8-7wtNj5012tRQ9uSlpJ81R287CE6hb9-HJwMvlhJ_AOzDs5r8_66U7gzmYHQxDB3xMcxlgLPz_HEFHAVRflqs0-G3ToNePK3xKa7epPHVOH3bn4X9TWAVMtkgTqmAdAOZQvNskkTDA4XGx28bA9wNzypCLrDQrX7g9n47R4T_ZaPwkh1-Pp8czjXO4mwNZdhJtaAbUM5OAg8LAahdn3S0L_iXSU0np5HKUtGgRGBvTCZB-Z9EjC5dPQquQAn1TgjGZ9k8Gygwg5u37cdPkh44jlkmsIAIdKqWeA-BaaOel7L4X8800pN25ZD_0CPyqlJxwMySfPCM_Dog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/25768" target="_blank">📅 16:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25767">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJpkisfbB-wrKlRNT3u9EpizwsT0vGozDKfXsJ-tJZLuQifbr7WBVq_msBDPWWhL3kLzTMcxGNFN72t1-o_f3ng5Aqjk2JZdEGAZ9owhgPMeLqGfS1lFKvcPun20cPYWsflKcmfIWaBXOk6uO1ptd5VTap27nIZdbxHJsctfgULRrECt3HvFSOJcgTQIO5z-zlwcHDtfVMsBw_hfAU2jGfpMZyC65YT6qQiSNgxPt6vtb_cC8tqG5JA-ImTOvxZoQ9RvwXpPhop-kxP1dczIT_ll9nAxrm2LcMg0AjLOb1IdbKqg0Nx3APUsv2tIxrwlt4ZT1RZJLN9rjwB4xRQGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری:
باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25767" target="_blank">📅 16:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25765">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=jEbKiMdvlDUPfDfvfabd_JTYRYRx2nxszXnT9a3RYBxeftIXLM5itLm_7pIJbTxZJG-5rtm_iTfeX-PCUoj5kg-_Xnp1aXYk4u68rZr8rFUOtQm83jpjqttRvBk0qN6iqgAP5EGmb3Q9OzVsQ8QjqWuSjZeXC4fnjOdazo7-ojAzn--bkvCSkXNBcx6vRyE-K-K6pdnvkc6rnPffWyipn_dDjGwPSA6rxPmx_XdRpytZcgmiqbc3RN9BaZ8v6gLcz6DY0eWWb2Y86eMKrq7p5gimGYvNUnPrXgRy5iUlFD5-dWoOEtYVgJNlf_znwTYbBKF11bGN_oKwX7kliEnbvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=jEbKiMdvlDUPfDfvfabd_JTYRYRx2nxszXnT9a3RYBxeftIXLM5itLm_7pIJbTxZJG-5rtm_iTfeX-PCUoj5kg-_Xnp1aXYk4u68rZr8rFUOtQm83jpjqttRvBk0qN6iqgAP5EGmb3Q9OzVsQ8QjqWuSjZeXC4fnjOdazo7-ojAzn--bkvCSkXNBcx6vRyE-K-K6pdnvkc6rnPffWyipn_dDjGwPSA6rxPmx_XdRpytZcgmiqbc3RN9BaZ8v6gLcz6DY0eWWb2Y86eMKrq7p5gimGYvNUnPrXgRy5iUlFD5-dWoOEtYVgJNlf_znwTYbBKF11bGN_oKwX7kliEnbvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25765" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25764">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_mFv1rl2DhNPW-8AjcuBegN00o6H3rGZ99i7WMdD8OpRcANGE6izGQESPCdxzcT2ApOo3c_Mq6Rh-hBTQwpyVG6STUfzNU8_84g2Fbwte08oZVWraHe-FUY8r2nDcpKl6qj3SPuWHePaooNVQuDQB3Rh0nHMPWAXhD0lvS430zJO053bWH1epzaIrJUaBDeehTrAhCmWVRGtO8ExVF8uuJQXM3q8ovyL7XM8g6wT_4bXODL8HyATUaaiwzQod_wdqooPoY3caQ88MITeI_sdyl_SsAOCWAdupS5Du2-wjmimx1MKRY7OaOyC0DNHbQr0tnZ0yNCS6up3bA4j-EW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛ فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/25764" target="_blank">📅 16:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25763">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6orEy3tFofXPF-M1ogrfl2l4nPHPs-ErQMFtO2mjQ8-cWcnr5Pp4ayZMkagAc1KsygtYAO1E3a61GNnWDmtTAHu1OWAE8BijuYFNZKB9OY8Ip0b9w5rxA9-QcXTsa40Te60ZR9bERE-o6rf5ZFbNONe7EbjnoHanJjUpc4yS5tCU21JkbIJ104HJrtmOR81HPcW4oB0dbM-uhzI1-uJQ8Vifosd-eacahkr6Tei_77-daX0dwb9PJhlKJIxrH1e5zlynEjT7hLp_TgH4b0jZPK2Ly2bG8vMmLBS0ApjGyjzRoQx9aAjONyjC7E8B6j0gcg2xqGwNnH4j-mCzD0l3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/persiana_Soccer/25763" target="_blank">📅 15:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25762">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUwLf5rA6drj7w5ZGIH7WeIixuyUth-b_ebXStyIFiOfXEjtfULZ54XGQtu10rG9LGphVGVqvFKuI_LiWgHBzfyNuE4Y84sp9KF9IRYZx1QSht4OGwhzBhgej47jjYQ-0tltADdkEtzfGpQduL-cquIGW4x20RSjIOLGdHrvRyrQz-SW38k17_LskvnQzeFOCQ6f4SrjERax0gRWQTDem8OalADGJ9UZ-BExGhWOEwS7Mi88uYEw1Pg9sMXEeTD4TNznBk5NBO92PpYSrfIUfKl-W9wVVm4clR6K_lt9RmwGYxwh825fMiR_ee6_J8K2Y_nN5LerThQy7P6DIbExCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/persiana_Soccer/25762" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25761">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=VWfLiR49dsGFTQcxrHha1WV61uv-L9WKPxAsjAYV50-LVCnXdAD31XIesZE2vp0OMHqvSxy3WmmKqYVfg-nB6vliJUz_aG-f74JtmOV7Jk3w3eQ-fa-SPqTMD1AUYzoAByXfL1qbNvfjQpCkooLHNSx3nV_s1NVOwl35KomAyQucLfhYTMAffZompWx-M4ul7TFX_gfuoKBX5hvqUoIv4M64ilvftTGT8yB2f_zxhTMCcDVMTpibuk_Kepwtt93-GEK8h9HsDjwSPKfci7jKQvStYLe-V8o6iF1-I4PwbjXYquj_brrL3Vu9SFxdByQQTWHabgQc2U2eDDkM-n4W1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=VWfLiR49dsGFTQcxrHha1WV61uv-L9WKPxAsjAYV50-LVCnXdAD31XIesZE2vp0OMHqvSxy3WmmKqYVfg-nB6vliJUz_aG-f74JtmOV7Jk3w3eQ-fa-SPqTMD1AUYzoAByXfL1qbNvfjQpCkooLHNSx3nV_s1NVOwl35KomAyQucLfhYTMAffZompWx-M4ul7TFX_gfuoKBX5hvqUoIv4M64ilvftTGT8yB2f_zxhTMCcDVMTpibuk_Kepwtt93-GEK8h9HsDjwSPKfci7jKQvStYLe-V8o6iF1-I4PwbjXYquj_brrL3Vu9SFxdByQQTWHabgQc2U2eDDkM-n4W1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حماسه‌ای دیگر از جواد خیابانی در ویژه برنامه دیشب جام‌جهانی؛ از خداداد سوال میپرسه نمیزاره حرفش تموم بشه دوباره یه سوال دیگه میپرسه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/persiana_Soccer/25761" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25760">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MS8RgZTfNVGCN7H3ssD9i-qUD6d_OHyuLL_ANVyBzN0jo0XXCxmsWQpb4sCr-R3THIyl2Cq9guFiR-Dy2tGroxjvnSIqWzxzZDydcJYNXYyg4n29Mn7rmuqCHW9WUz56dlqm16zrVnSBn6Ju-G85K7QQ8OiLqQ89-9OB4W0KYVrGCSXY01YdMR9mZpKaMA5GxoSKAe1bTjRHNcTnsoQCEishKE07PeUKWpDeWEE84e6SyNjblj5M5-fOGt6tijufSb_S4P2SY56OjRGl-gniTWdTCGMeygY0AUaosgcjxLcCuO2f060YoaqiX_FgeTqywiQYUfN0TonF4Cy1HCzpfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#نقل‌انتقالات
|اسپورت:
سران اتلتیکو بدنبال جذب رونالد آرائوخو مدافع 27 ساله بارسلونا هستند. مذاکرات باشگاه با نماینده آرائوخو آغاز شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25760" target="_blank">📅 15:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25759">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMNGSbc1-sFRz4rclF6I9hRQfhelCKez0-7cB3L9pknx_FKrJVl8sPyd-7Co5RzMMMduAQXyAYZgtP4GJMFPEmPtPfKjhj-ti2skRdERPYqnc4zcK8W09-xDWtHBjFxaq5a61ABCIYPAh-3NTRUTsSo2-h5pgwF9hzVbC4Yqq_DO9M-pITPk2JT0EzrcRwTUPJ9KYbla-iZvhSUf3ChFDXKJ5sdnrXh-StGPAkmpzmy7OfYntyFfpVjjq_7Dzkbc-jmpBqx-eepMWnyLVdSfdmtfCAZ-eqz855Ga16FHC3kVJnERMHC59bkPopNkDq13m_m5UZ4MkcNRdDypCqY2PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25759" target="_blank">📅 15:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25757">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv9SClrorZfvpmjz2T3BLmPzS-YBzBgk14hL_Zf1PN-gyJ_bzfIiTi4yo3SOSqtqBUUsOeRo0yZUmz13BW-mom-J1rUb4sShj3OkT9j9XFPQHD2jZKjLGHQ5HVMNlRcwk5WN4NDAYUT7XNzHF4xDPYE4q4jx4xVBABEAkXZ_7SeiBoM77pJVYp--aREimI-Wb1922E3FydbcP4fuKccV-vMy4awmyjHoQy7svVAsec-TJP7ImnPppNPTRXIHqI9c4UbQK0SN36diUXPEPgw8dXZE597QgASJAXqJRCaybHnjzw2N5a_LqaQioTTDJz3DxS9xc5KDjKC7ms1iWdG8dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق‌ پیگیری‌ های‌ ما از ایجنت ستاره‌ سابق استقلال؛ قرارداد فصل‌ آینده یاسر آسانی 1.2 میلیون‌‌دلاربوده که فوق‌ستاره آبی‌پوشان برای تمدید قراردادش1.5میلیون‌دلار درخواست‌کرده که مدیران استقلال با این درخواست مخالفت کردند و به مدیر برنامه‌ های او اعلام…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25757" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25756">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYCCDeCYFyYFSdXBIuZJJq6iNjHNI6c_SPU0uBITIVIJmAv4wyngsrHsP_bJcJAlwI5DomkqYORiOc2W6SawKeCJvvOdcoqO_wTsR--bKfYOiSJf1_pEgggzBqeR_SnpGUu9KeI9RiG21bXt2ljw3dPDJ6I1t9O78c3N6ZxrmuPxydUxQfUXd1X2v3y7KCF-X2U7TWvtq9PPfAL0sixy4FMfIRQRwW1p4MlI2z90AytTXhWHQykdvTPwP12EWqrq0vZW_sWn4ZpSlMlfG20OogO5MJMMt9lX_m8tfn6e5n3AvJnyOXE8Q_WsU_alXTbi-7jtS2HOXIrD2vzFOs-xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمکت‌های جام‌جهانی 2026
؛ چه کسی ماند و چه کسی‌رفت؟ از 48تیم‌حاضر درجام جهانی 2026 برخی سرمربیان همچنان هدایت تیم‌های خود را بر عهده دارند و برخی هم از سمت خود کنار رفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25756" target="_blank">📅 14:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzThv-DWutyGFztRtvlG4pHSq32AEsi2L2qX9nZrO4LD3uD4huA0j7bMsoHIlZ7Bc6tT8QimEfAW1vKAOr-dEoOf8l3JuC3YUjdzyFS1hvf1ztg2TtFfWVKjOB_qwCNEsmiFF-BWx9pXZ6kq0_Ypgabz0ssixHgMV5OzCPGI9eAYh2NCn_9amJPbefN01BCaqcGfxOOLwOHV7_T5bCxPWYcrJZ7-JodcxoHakc6PftFxxJ2edk8jkseLbwdXwlSRmO5AtMVbLtwQhnj9q4WSzxa_Wp9srKbqhpD-mqheoJ9n452voAwDAr4NCYI5gP3I3yNbFBcuNvPYdegw9c9tXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPfsXfjb3-eA7hM2QIKJkhUyUmCqiPluuZHtkqGtU5Oi7J-zQmwoP2n_lfGabCtrKnKQCoRI_q-z1F5pkMM0dAodugtFeNvo9nYEr9fwKZ5bC2gz-kaSwAo5Zo-TVqNl7U_-9Eti_fGVOxHP-MjYNzqpITtNgVpH-daTIV53LVDovpn34QLXndcb_b7SisoOPsjtqkEWbMcUCYdtnDJzbJlYYEMMMX4IHp9un1UAhA0RKWstsGZaudKCZf4_iJbzfknE-nII940iAwHdqZLnZ4nDZOSDn4W4MKQdoIYJ4bLuL3Yrz-oosLZqomD6DydlVbuIUD3EGr1KeTKopm3oRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25753">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e68WBLBxboqqDiWYTGA0pmoxCJdqianOFgS1V_v25HuYuX50yfdPEMont43-K1Agedm69Vg_CpzyQ9jIh6rOsxzTQPD9AvLmjq7ShoFxi_7a0L4eQCl3k1avcmYKNtcOXLi44Eyc6h5YZ3bfen6hGtv4CmhWW8u6GzlF6Rnj9WvuQj5YX_uSf7DHylWTM2j-iX2wlxRppE8V_msdFUPXBxKigCe7nPvTfQVeutH_fUeA_6nEaTlYpFoPhCyJivp7J5ExcSH53uZXp5wTLNP18zbgd-BmaneP4MkyR_FmPFlq7uSp4O3rsMwl9nl5ob88Py4F3ItKh2RMc6cFEZ4ZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممکنه حتی بختیاری زاده استعفا بدهد.</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25753" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25751">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXIVdpZninj71kvqvzdJ4UoeARY6z-p7I_TDOT7dPckaiZbo7MeF0wiSFAMnCGa62l4zssaJgxXGB_e7n1TSawj4g9Hla0Tbyk7u2uZMAp3rTFvNcK-2URBScutB22iOcBso2HFgkZcfZ2s53Yd6Tv8SXjj8r8owzojieM2M8cPOk82C6VukUVcTqNpG6gKmrEEOF3JLjy7ZPz4Y2XI-EzQqWnO1pDqkjxt7TmRPGIEU3sEzNaqGOGE95SixCR6qEifrvC10lFBXbvTHJN6wxD180qJfYs5OmplAoMBzVrOG6D_Zr1v7zAJ76hLpi1y9pNdZYxb1OIa6Hsz66Hk9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کمیته استیناف حکم خود را درباره پرونده باشگاه پرسپولیس و علیرضا بیرانوند اعلام کرده که باشگاه‌پرسپولیس موظف‌شد که مبلغ یک میلیارد و دویست میلیون به گلر سابق خود پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25751" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25750">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qawMKR-MGSXiEg5vF-TEDF4M4AZgqGjYp4Fcmpk_Ey-VumJT6ZD7vACKhUI-zKMxQExwUg1qOwXOuWktiZkcbwANRDK1H7Se0o41x7_L4STdEgqRPyKGveUkETpmtVqRRqPSJvTDE2LTAeOWVu1eYgLvx5j9Bfdx1VdrgT0HgPe9bKZwxs_0fIGHSlGE0BvxV4gYE1QC_837HM07ghnaqtXH09Ykd5tVq_Xqh6xHGaGGcgZPgD66uGRkBku_AGf14sDUOc8KzfJJJZSEIzTU89DCIRzXtyQYK-oUJPQhyIjbSRIl78-kLRgM2SJWfqZZxDatOxIQysfrfRFu8ZYh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25750" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25749">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=bump7aGjXz0kpowIIRHGA8r5Fto_8GAW1cm_4osTx54HjC2NWr3Nh7syu1OOz7rtIQi8BgmmU2vm7Q_QWYZcSw1zGowK6RFjVuW-jwkHF8Cg1Xmx2Bh8gyL_BNQqU09I7REBoyHuhU_h020VLpZ4D1Iz8RFuVbrP8C6K0DBGPbg0XBVFvVnwULiLUWuAPgglnNzlgVHxpScoXBi1ND8DuDJ6oTld2fFOGO3Gr6iyHnt9cNSyfMPHZYLLDIRI2joDJHo0Y9-u2ynFD0Yk3asN8gH7v13zfQX7Ka_Zcm3bJe6DCu-OX5l9CQtv1fuCnCAh2F7ZNuZyjmgGXJladF3gGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=bump7aGjXz0kpowIIRHGA8r5Fto_8GAW1cm_4osTx54HjC2NWr3Nh7syu1OOz7rtIQi8BgmmU2vm7Q_QWYZcSw1zGowK6RFjVuW-jwkHF8Cg1Xmx2Bh8gyL_BNQqU09I7REBoyHuhU_h020VLpZ4D1Iz8RFuVbrP8C6K0DBGPbg0XBVFvVnwULiLUWuAPgglnNzlgVHxpScoXBi1ND8DuDJ6oTld2fFOGO3Gr6iyHnt9cNSyfMPHZYLLDIRI2joDJHo0Y9-u2ynFD0Yk3asN8gH7v13zfQX7Ka_Zcm3bJe6DCu-OX5l9CQtv1fuCnCAh2F7ZNuZyjmgGXJladF3gGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25749" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpKL9S049iVWfT24cwkRExGQmpaAIkkINIItp9a4LIY5wqEYaXJANJVoDOrgeQFQX-P8BXfmZaynnYL9ybgRrTtFoiyK_XnPpZsOeUT2pjF7xEzcNN67rzVx_i8OFTNnKdp1XwJZpaw7A8qCPkHY4WMqwToKnGlzTboaiEPROFjeibcsoxRn4Fhvpty2006nLfmAs-psuNGbc5_fd6m9Yhu83-aTdj8xDAAmifTlfIrXkBsSvAg-UlHoLR_bdgUcV_Y5jpJ4SlrcZWKqoDlxsSdavOfwaDBsuKuk9lnjwlawbJ02PFiSCmGzqtVcnODzOecs4RYmcvf6KufePMoW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLr2jheTX0rHFLgCVAApmfjJ_mBfbFp5gxlIw_AQe05jUCNWGP3mBhuDQru-ySa9VXAJjLhXZfMpTICUrOM6jzKl-GVmpezzW0r3qgIQRLS0xTL0d0kx82JYhfq5Tds8EUPNP2bElZGl7Huo8YRba_ErWl0VBsnpEia5xAYyGgrA12zcTcr5y8BD_2tBLkjBiBslhfBeiOOd0rTshgd4qS442wIKUIaUALDzms3BFKYqsqYyS74qreu3bhFrJsKyZZv9VqUzH0gbRTDURcPx6OxAz0ABcAYE6HDR5t9RLjGupSbV3vX5FAsaWIT7Eoi6okflLR08bM3yUIAj6NRTgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru_jj-REycZiTtFR1h0LrTK4_R6Cyf-eO0oom1TLDD0F_LRy2BuBkyCFYOkLWc3t89WwPinRkC8bZBm1Oht0spxDfpDd41g6vqaAUbgaeo1N-Q5E0BvSej3flhAbfiC57YRTEj7rGTJPFBc_x1vTH0cKJcRN3evbmBozZ3FwOk31WS6SRkg5eq4W9q48ZP5gJTvhee7Ib_nF43OnoqUXbqnzFID-HqmJWc4JFsrxPipIwPbPTcfvgqhO5CCNjsB1gY3XUrikl1_Nx_z3m6YHMrRJSwB6_PSG4xp9v6HRDYvUN68lFXHFOLaVohEf__UXmg_WGqXrXTVKKd-LKIAJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr2j_w12avOhbSZzWPY_EurXqgI4oeNz7CB0gWlqY2PfCqrOYjUj-qAldPoPq0-YgOJPYXBHTkDSYC1pb1rNtgwhHK4E3ewKBQCKwfkZ43sMItAU_1b3sEqphPL2dByxSdowS6OSfRQ3fxH5pw0RQz1WXHUP51Ndhl0K7c-GCDNtD_zR5YDokh-PxrigztDbOC-t0brZbKv-uTlbNV2enarKttL52iJVDwrnYKnNzcgjsq6zWm_nm-73-kcNVs-gJRhDrXCZpmXQUCWdkKwkceKSmXq27o4GumGuWIKSDQDNVeL0UBIpUVGYyb-RaS_lUNCnUOFUSSiC7aGftZxHyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_44wkCnGYvDs04aLEg4yBPi78FklDGhb6tTTWLZsB_XhNfWjxWa4Alcg6d0GrCslbt7KOpYAEvgbBsBY9iU7M1qMNtAfHIwbVYeOd7TBvRPliYFb87qXQ83VYE9ZNCcs649BmvoIpLucgE2_XuxIc1DzM2NijZl819vFSWhML7mQcZXv2mcQbWLblkqu6ieZr4TDXy2zhiErKCDjhvAxg5a5zNTvkKVLkMQ9g18o345Ai6q3l3itUTWxwUbaNoRQzPEhhiaGGq3XtP_ndFekGzfEApSpVXylyT4mhwZ9JKzS679AE-xU9kxJ8-TYzYih7uRqLQI_szNBqssny2OVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=LZZ7y8IgYCY2NgC8U3msUjqkM_DNXfSo8yb8benEw-E45NNR5Mya4kxLtdiO0OTpclADZ3emmYhhBBV46O9L_zX2EQZzx7icyAx8kpEOC80pxW-3tTONyUkEysGmk7peBY6j-UQK8h6Ot203BErzMPDENbDiQLsQrw6snGvJf5-sFGQfE6lbvA_o7pfpkLaugWMjpuufYYL74DEI9WU5TFz2EQ5j7IqdQBLGgOC8bQ9yV1L_3Gdget8e5PcQKgDodxOj4ozY2vMJy4zrpXhlfF0Loc9TmuiUhytPT1Hj4pqsRLuumfcARxRtzxgtUKrrDA_R6wWv40J_kagJxcZJAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=LZZ7y8IgYCY2NgC8U3msUjqkM_DNXfSo8yb8benEw-E45NNR5Mya4kxLtdiO0OTpclADZ3emmYhhBBV46O9L_zX2EQZzx7icyAx8kpEOC80pxW-3tTONyUkEysGmk7peBY6j-UQK8h6Ot203BErzMPDENbDiQLsQrw6snGvJf5-sFGQfE6lbvA_o7pfpkLaugWMjpuufYYL74DEI9WU5TFz2EQ5j7IqdQBLGgOC8bQ9yV1L_3Gdget8e5PcQKgDodxOj4ozY2vMJy4zrpXhlfF0Loc9TmuiUhytPT1Hj4pqsRLuumfcARxRtzxgtUKrrDA_R6wWv40J_kagJxcZJAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25742">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25742" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25741">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnePkR6_uRsJVP9FSaIfbP2Eps6hXw6bUEmnxRJqQV59AjpawkBRHz3ppLUiO7hOcx0vobDTywvQLerWXXz-19gabZcm6c-8Frhxnd8nfksSobmb1bejL8ZmVo-7mg1v5t_F0uakn2jpuFcSCt5kMINLgkWbxS6TSn0jwB_MOLoaLXMtH1F5tMB-sQRkxKpYIdxHtpW8bfNHeU7w2C0gnTRlpyf0lvZurD0IO9mq6nrmBmf7eOerGLcSDKsBnoucgNHXAiNu7Nf_eAkR6F8cfAtqDHbcKOl-WJyu2UvzJHMqL1ZqgB6PeWNTFaBuUIoyFDPLDO4UU3HSsLXd1AEu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25741" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25739">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4Gk8pHSIGfok8-lPiYTXuMHX6X8JhBdTGzeDPTXYE5fC0iaSqOOMh68cbdXBpuiyA_RTv_KyYV-6FHixn_IAc9zmFFh6zmS3bS9cmSfUfS-BtUvT5cij28K3qDqXsRM-YcYYOJp7ZbBxz9rVTy-Wzsw1q2MyK64kqRKnoH_i84Sbrxr-QlIAgQWwQw3Abgv15A8hPLC9GItRkALxkw4IOlmha7l0JGPKzFJW8tEJmY3BJWM3hO5AktOmU5jfRux2YjiCuWkA2peNLtw0aqcNv1udgIuoo-_k62IGUGrSjrLWS1JOkdRNfXm8xL0hB8Azhb9Ajbs4pQ8olKu1o0ZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم؛ سال 2016 دقیقا در چنین روزی؛ باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25739" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=UYrT-ZO0NZc2FTjek3mH2PMjGdNxvPvF4PI69wND76gAJ2ZK4R781uD27jx19YPDnPEmbVlFIryvsFIH4r-RKZ-uvbZ3ndCip2hHNCfa-dsqFA-6K8FDOafXjIZQ1uZHchrW6Fo-ar5sFDZhAcUTVU-HFDhMDNq95dMcYkF4xh9QGmsLWNiUWbO0-kTdiY_S0GuQHhaA_lhyCeK9RGSmJokIfBLCPMC6Ds-ncd3VyGQedRuWdcyd2rKbu-2GOAwXcxoCINJj_Dz4pqB-dPJ8Edy7DytdKfLVxorkjHV-PsHYgaA1ep3Vw3sG5Shn8MUbZ3gyzwvTOLEtj0MMBF1AHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=UYrT-ZO0NZc2FTjek3mH2PMjGdNxvPvF4PI69wND76gAJ2ZK4R781uD27jx19YPDnPEmbVlFIryvsFIH4r-RKZ-uvbZ3ndCip2hHNCfa-dsqFA-6K8FDOafXjIZQ1uZHchrW6Fo-ar5sFDZhAcUTVU-HFDhMDNq95dMcYkF4xh9QGmsLWNiUWbO0-kTdiY_S0GuQHhaA_lhyCeK9RGSmJokIfBLCPMC6Ds-ncd3VyGQedRuWdcyd2rKbu-2GOAwXcxoCINJj_Dz4pqB-dPJ8Edy7DytdKfLVxorkjHV-PsHYgaA1ep3Vw3sG5Shn8MUbZ3gyzwvTOLEtj0MMBF1AHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو لو رفته‌از اعصبانیت‌شدیددیکتاتور کیلیان امباپه در رختکن فرانسه بعد از دیدار برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25738" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=rbnvy_r1S1QDSdmI93SsU9O-l-Ldp9G1FCayyAiBfC4g9s2YZy7tKHd0WdiiF3Vf6lSKnw2vkeTOQFTjCP58D9dImbvWsnjLDYl2Ym0SCi5_nO7y3WhDq5G5FqOrho314CgBBjguvGKkXTNsD5_V7-8ohi4ekGATB1ej2jZVZp5egZNXuta1GstdRSB_niQtmJ3c3Ri64gDC3R3MrzuaabePUzyfjfhucxf_TpuQo5UC-wHb7BBLAZ11mL-0532zyyQsze61C7FvIu5inp4FzdERt3hCz6ehAPj5RU0Y0R9fsZIkooLL8IFzRps__BPje6TOIZnVlXSBnNyY5DCxHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=rbnvy_r1S1QDSdmI93SsU9O-l-Ldp9G1FCayyAiBfC4g9s2YZy7tKHd0WdiiF3Vf6lSKnw2vkeTOQFTjCP58D9dImbvWsnjLDYl2Ym0SCi5_nO7y3WhDq5G5FqOrho314CgBBjguvGKkXTNsD5_V7-8ohi4ekGATB1ej2jZVZp5egZNXuta1GstdRSB_niQtmJ3c3Ri64gDC3R3MrzuaabePUzyfjfhucxf_TpuQo5UC-wHb7BBLAZ11mL-0532zyyQsze61C7FvIu5inp4FzdERt3hCz6ehAPj5RU0Y0R9fsZIkooLL8IFzRps__BPje6TOIZnVlXSBnNyY5DCxHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBPA15jfWbRvO_D4F-lDfsHM82u54TMpc-iuD0KQcYmbrbdVKm4Bz3YUpUHraYWTovYlFWTZqLtBj-krIsNlyL3kuU7MOuJ36iLkxgP8tnurgW9Bv4a-f0lHyKtZGLKvfUzjy8nbVUfsy4ai8rzjTzOV96ZBftG6nWzXbTiuX9iXxmBXxVhxf4pERd9AtiDcD1Rh4k7nPF7ANbhs2vhJxtIMmbSCWa9bhyP4ZQ9YX9DsPPIh1l40XuBYjfW1yiETb9xHwFnmmN1rDZHgHvtWYmYT_hk6Y632MYEbFsmdprxIU_6tQbPLO13bDX22Wgv86GHECzljKE-jLADV3HEAiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFrkoTMzJyIrKvKci1h0Pru2qz5tdWl3BMrfgpxVf9jFjAvzAF7_O7WMaRX9Utw-re2hfey80hmYmxADd52ZzIcpfwgCMax_dlDuaWh9GhC4tKS3nGo8ABM3alSuuF75qYBm8FJVJe17oDWCPC4j2CU6EwOYVYB84B-VpsJoNfRkuOdzXJ3D0BS6odIhKa90womkD5n6eWCZp6STTnFkx9-rlapSDMKs25d4f4lVZ1KiL1TcUKquzu8CTIGB0wyDrPXV-7AlqssPJxBrlgyQrM7tKbAuSnI5-vfMYvUkyBFqBq2sdH1gH_ltUnSuyL1uOhnpoJQGoWTWsDgXLqwUng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=mTnb-R_VXoaqK8K7CYn1FhKHz1zHr4eU_ga3JYgehGdaWcFMtdXWPif6xtAMWg6y20nxhof2AttJ2qC1IabCShVZn-LqygBj9X4WsnHCT7jY6srAJCPnG75YgWKVkN2-QAN59aPpeydxoCtQZqJ7fmiiN5GNk27sJ0QC70_25OQLjcL_nOSTKg3BPq2lTmpM_Crvvll8Bjy2VbuSmnBMBpW4oFuP1xnuc5FQpFOiOF0kI8Mv_MO2o3RDvYqdLM8iJu5lj1-tqGXbdKuJu-FbOd29SB8zKaXY8819mmd0V9CjqoWtRLQGBpJlKs5z4xyffmJFvNwYHq1OgR-ao5B_fEZqhs4hw5RBL1xH65Mtqm4Ii5a5IrdVbAUUQUVSCfszQJApmaF0VCmeiFabAduYsZaU_q5hILkai5qgMHGh7Fvr81Mak7DQZZUXEszQYRaT6ErXR-TRiXMuAFEIkFTjJVT8t9cuFVi4gE1joMUtbFeJI8xROMzbh_dmkNBq0zudiBIB2EwpJbmbaq93ljolmIM77qyHaN7HALcO9uPhy84sDWSSlHACXVKhBPJRlmnZpsCfzflM58C07fvI8Tzb2ViITCfjHPoG-JsUQAjFGaszqibyKKP8iE_P2m9U0N2o8P4-f45YhRhJ9-NC_X3XEfggcmeyf0ZPzMeQ4HIk0xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=mTnb-R_VXoaqK8K7CYn1FhKHz1zHr4eU_ga3JYgehGdaWcFMtdXWPif6xtAMWg6y20nxhof2AttJ2qC1IabCShVZn-LqygBj9X4WsnHCT7jY6srAJCPnG75YgWKVkN2-QAN59aPpeydxoCtQZqJ7fmiiN5GNk27sJ0QC70_25OQLjcL_nOSTKg3BPq2lTmpM_Crvvll8Bjy2VbuSmnBMBpW4oFuP1xnuc5FQpFOiOF0kI8Mv_MO2o3RDvYqdLM8iJu5lj1-tqGXbdKuJu-FbOd29SB8zKaXY8819mmd0V9CjqoWtRLQGBpJlKs5z4xyffmJFvNwYHq1OgR-ao5B_fEZqhs4hw5RBL1xH65Mtqm4Ii5a5IrdVbAUUQUVSCfszQJApmaF0VCmeiFabAduYsZaU_q5hILkai5qgMHGh7Fvr81Mak7DQZZUXEszQYRaT6ErXR-TRiXMuAFEIkFTjJVT8t9cuFVi4gE1joMUtbFeJI8xROMzbh_dmkNBq0zudiBIB2EwpJbmbaq93ljolmIM77qyHaN7HALcO9uPhy84sDWSSlHACXVKhBPJRlmnZpsCfzflM58C07fvI8Tzb2ViITCfjHPoG-JsUQAjFGaszqibyKKP8iE_P2m9U0N2o8P4-f45YhRhJ9-NC_X3XEfggcmeyf0ZPzMeQ4HIk0xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSWH4AS35GDpKwbvbVep_WI8wjW5SPR_DSTTPXEXYHHNyCDs932AHy61M_iP1OI6QuPmK452lg9IbRK0LAUOeYumVStjooMemqSH5QRR9ROLXhSO2JRTsYNy51N0PQ8ZhXertwE3NX8_VWlYS0SB4esn-2w8n4bQ4W3THC85y9CtO4vLBr-gTWcdFcYk7xECA0zpBG-JTOFsFC3TtjDcNJDZUZY96RHbyN_-JCX0su--WUhddXt4NjyNLn39HccRx6H7okUzBjzyPzqhAsvKShhssIMUtX81gCsu2DLKD59WvOL-Wk0P_SfarGP9jzjXdA91amgIt4DZmBCJAUSCqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHmiY6bb82JQ4kAeSNk2XW6yjEcgxzpv3AEHBMFWzv2GZAYJpwq-oyUeujPd_cu2nHiA1jUWSiI0JqpWS4PJrbTNM3pqc1VtGVkHEvop_xQ6B7HpJuJmUc8pQdTfeku6xGC8ypHuqJC-03AQ9fmmQKEt9HJ-exdNTQkSlYB0nnPfHCnpt3y2RJKDp86be7JgsKVlgGVUJ5Wtek3t85hFDzwUb8RdgCey48KD4a_ZXZegrG7dkpQw2u-Jwn5jIjebPMdgSl5s4-TthH5ashL8l3rQhq0CxCqPU7gL06ai_pLQn4vUV6lHwOMmwimNmJ75jf4B7Bhi2CxuJt2ZfQalpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMwgB6na1TA_9STcK8thfJdB1tUUj676wEdl_9Iiyx8Q46evc4G_vHsoAjVRbS8upZwHvFIrzIcp8XdtXj3XGXBiyrBT_2Rd4ZRwyLnuXJYESkXKPx-Az7fS0TV_tXTaX6DtEFgsoUu7zQJ24B_Nh5c63YTQbCQ4usv0_2HVGP3SDTCrwRbsqTg6vzGVyVJYQJ5mYJ4ZaxfaN9TVJkj3xKGSOjX3MbajsX1JN2M0btmkW1SlV8qIU4BhbCuyzTBsS58wKgivMYeoI4bmLhoppK1oPzi6xCOA8LBRBWmYqfAh12ncVE0LDujIun8jTw1tk2d2JbcyUqT0xCF5TSUcPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKdmxujjlzZjIWYO-ztSu19abJmwVsg4iu_Tqif8t222UqdTU0OBSGEf_mry41q0-grm9qaEgx1488zoDM3BltLYY63u5qLKCeEWuAxmw1h3uF3HR4_zGhW2JCihJiPeSFrJCZQLR2YrgWIZ7rGlVWa7Yy5LDGIzF4cBaGpfNh4Fc5kTpLfizA2iz6BwdaaTfWN2fP4zcuOQjpmOICwxmrHZ4owcKLh5Q218AjT8jPO-0vIUVyPCi8fviVF90k-e_ijCnRtipIOJgNDnX_beouzAHKzTWhQdl7og3PD2TTR8MKfWV6zFP1YosHgS7wxdd0CjkqkBwfKjcEm06GkiZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=LNVzxBH-hjt2l9XgIGdD7-zj1gQgkF_SJVqGbILzJ_mA9eF1i5QvsvCPatxVE0Ve59u0vW87mr8FLAVpQYzamx-qvwlzsf_vnQpduppAmICGk-TQIUTnXqxB0I0U0dzZGr6tYGPXv_uQeP2BvT_bhGwC39_jDuIgxpuUOFOfjJuAxlW5_SIffSwSJs0BZVl0S8e1eJF5Qqr2qz3spXJHtfofh74GqPJDHLfwd1IT6l6gJe81j28EnZjqQLilvG8JQOMsCCPmvLextlttm3CD9Nb1TVyYebskcBhwZ-WT5QjcKljB-dIgV9_FE8x0fsJus6CLtEt8Dsi0hSG9ay0OXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=LNVzxBH-hjt2l9XgIGdD7-zj1gQgkF_SJVqGbILzJ_mA9eF1i5QvsvCPatxVE0Ve59u0vW87mr8FLAVpQYzamx-qvwlzsf_vnQpduppAmICGk-TQIUTnXqxB0I0U0dzZGr6tYGPXv_uQeP2BvT_bhGwC39_jDuIgxpuUOFOfjJuAxlW5_SIffSwSJs0BZVl0S8e1eJF5Qqr2qz3spXJHtfofh74GqPJDHLfwd1IT6l6gJe81j28EnZjqQLilvG8JQOMsCCPmvLextlttm3CD9Nb1TVyYebskcBhwZ-WT5QjcKljB-dIgV9_FE8x0fsJus6CLtEt8Dsi0hSG9ay0OXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T80_ePxnxRQKMW8clrFpVIstyEXfoFfhtroZJ0E4ceBV-6POFQClD8wlxJt3zjdJIwB5mGKBnv90RVUT9L31_37sivm4lxokA0QtM86gEc97RQMXbD5FLJidiUuei_epuYgE3OU47iBl4DzBysjPNlF6WJXNEjb-aApqXijrhKkJ0dbEuwXxwfLE3y34JExvhAI1kyYGlBd5OTqeWDpMOt44LuKnFLGRDA7aH4tXHs_40uK1bVOgRxwjdvS21kOIo0TJXVz4fZ8Jdy2Gc7Axtb4VvQGW-7D5S2SGfJudLBu8GwJmtPy-ku_XmBKbblyE-lLbnvrbVGDE4xeAYb3SIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
