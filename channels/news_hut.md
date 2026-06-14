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
<img src="https://cdn4.telesco.pe/file/puVy353vPb7d6UE4Gagx_fYfykHBsEkUqxeYAxpYXLs243-rOQSgE-wioe724d4EHr1uHyCnXaHVC0GBlUj2UEfKHZJPMi6qSMDFkYT1qvxbIZiIFct2pR1bKZYxB4FQYKFhCsHhch2xIc-H9-gX0sq4ItrSWywfIHgQXI5L5Wd7iXf6GbbdXaC8eqv8pnqz_PeGj4ht8v3labKRbIdtZUIUjLNu3I7wm7fF1RPcmy1NsFiDRHcuGaQRJuoCkPAcnTAiQ16QjuHcY-fHA_9updrAW63PsugthGpRpkyGy48KYAf70-HAtSdFtuqyPL8ATWsOguX1957MytrI_eFdfg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 224K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 00:14:42</div>
<hr>

<div class="tg-post" id="msg-66108">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q87RkcdzYMBSJD7JVJx1wvcPczTP8AaraPNp6nKJxVhmoUstwpbeTlcCQq_x7kqCWFD8CVqiWutgEwSPBNU3u2uXNbgnHbF5dD37E6_GifBEbDgaqxNeKO30AzERZhLD0PgZurcR1wU0_5LeVf0ZKE47jeqD2K4ni4-Pi7JdzHkci0L_fUcL1SpG7P5r4xHZtsbmFLvK6ZbJM30HRZm45LnJC4Jf6wPivLq2akXu9wz5ZsDZMT0zxiYNSCgd5HCWO6RAnb3vnd4VRkTAj2QkCqS2KUwK1uVI8BHzcp73ZH18Ad6znT09Jr1UN4bf1r4rNItX6O5vPrkPa3gxj5nGIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرزیدنت ترامپ از طریق Truth Social:
ایران هرگز سلاح هسته ای نخواهد داشت و تنگه هرمز به زودی برای تجارت باز خواهد شد!!!
@News_Hut</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/news_hut/66108" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66107">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
#فوری
؛ ynet:
ترامپ در حال آماده‌سازی برای برداشتن فوری محاصره دریایی آمریکا بر بنادر ایران باشد تا از هرگونه حمله ایران به اسرائیل جلوگیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/66107" target="_blank">📅 23:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66106">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">محمد باقر قالیباف:
هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛ مجاهدت‌های رزمندگان لبنان و دیپلماسی مقتدرانه جمهوری اسلامی‌ایران حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66106" target="_blank">📅 23:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66105">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بشتابیدددد که فاک بت آنالیز از بازی ژاپن و هلند گذاشته سریععع بیایید و ازش استفاده کنید
💸
@FutballFuckBet
💸
@FutballFuckBet</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/66105" target="_blank">📅 23:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66104">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
کابینه اسرائیل:
اگر ایران حمله کند، ما نیز حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66104" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66103">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRAKeRc_0WgTlbQb0Fo1Cm8JV7SraXImCLBGlN3PtHiJLE-WtBK5dntN7gp3AZEkj21Ta8ghusgBRDNaTLvOyc-ZMZfll9eZC8fwRNR73PUMKbGVlQl5fCMHonVOue9nPrJ2mJPWu9nzO7kx8DfourEWRrcudWFZd9gQECusRYuvTBMDUFN4lwb-Q9BcIqMZ9IDjwAju-DMnM9HMyL4GbskkJYBuXHWhC-3p6qEehIVoVqS_-utlPlyyRF44pD8T-crHX7iq0kf7BpCWh4gX4VJ-0771x59fVA2dNa7_2KoJ9ayIDki3WpHCV-7t9_mO7qmKzylR0xYJdJxRmdX9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور هیتلر در ورزشگاه و حمایت از تیم ملی آلمان.
آلمان این بازی رو۷/۱ برد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66103" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66102">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me8NL2J2d_jrUy4OZ_tJtZ0Xl6W_lV2TA8t6mAN9etut_a2UMQElOTfcghOhU93l1OU-DUcQfcNUXysSp4uTmRfqooXgyOUWmMVqxIgfW0HohlAejeHz8abOln0uQEa1uTUFEp0rruezJqG54B0roJeN0vATnFkfrdTodNsu7OvduzDAFKsBcAWxnAWgB3aWMoPa_DR_yt8-_vP8k8J3Fw25dIAOV_XpHSFJPQg47tssOnUg3mELH6NbOqXZR9p-wUfgXtVCfvL7ItNdwVtYhcqv3vIfNFNCVoLZFSCa6dPOtERbmbPtLFRaxA_owmoGQH46jgIL1u9czm5h3wHTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛ مجاهدت‌های رزمندگان غیور لبنان و دیپلماسی مقتدرانهٔ جمهوری اسلامی ایران حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66102" target="_blank">📅 22:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66101">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
به گزارش Ynet:
نتانیاهو درخواست‌های ترامپ برای توقف آتش‌بس علیه لبنان و عقب‌نشینی نیروهای ارتش اسرائیل از این کشور را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66101" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66100">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری تسنیم: حریم هوایی غرب ایران بسته، و تمام پروازها در این مسیر لغو شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66100" target="_blank">📅 22:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66099">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0112560fb5.mp4?token=DjvV2CfAD0GE0xD6uKhR3WS6IvQN_SoYVayoZXDvnuGyGbJKx2zCHGclO176O5pN-RxOsDXYDVbZKkW_3EOqHn1iUxZgXd5T96dYS4iBo5umJqDx8S38Sa_wVR0JzgNgjz8WOrbUlkkyQQAEvMqAwtlN_oisVHkiDVBz-UBt7GojE0PnXQYpu1cMhO0wDyflmsghpo7C2Toe46rRNRpgY4Jyz8Sl6vXDZruIrlU7ui5YBqokW1PN3iP-b88jbVmEtHilYAU5Mbm33DEyEMLPzIQqYCd6DSMPRsxxMxzvb6WIT6a9toJKFr02qu0WuoBmITl7ep2Ey_fbrNW6hvl5dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0112560fb5.mp4?token=DjvV2CfAD0GE0xD6uKhR3WS6IvQN_SoYVayoZXDvnuGyGbJKx2zCHGclO176O5pN-RxOsDXYDVbZKkW_3EOqHn1iUxZgXd5T96dYS4iBo5umJqDx8S38Sa_wVR0JzgNgjz8WOrbUlkkyQQAEvMqAwtlN_oisVHkiDVBz-UBt7GojE0PnXQYpu1cMhO0wDyflmsghpo7C2Toe46rRNRpgY4Jyz8Sl6vXDZruIrlU7ui5YBqokW1PN3iP-b88jbVmEtHilYAU5Mbm33DEyEMLPzIQqYCd6DSMPRsxxMxzvb6WIT6a9toJKFr02qu0WuoBmITl7ep2Ey_fbrNW6hvl5dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعار تجمع کنندگان تندرو
عراقچی بی غیرت اعدام باید گردد
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66099" target="_blank">📅 22:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66098">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
#فوری
؛لغو پروازهای غرب کشور تا اطلاع ثانوی رسما تایید شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66098" target="_blank">📅 22:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66097">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvCgiJHguvP2tqjxKz-iC1dF3nurqtkkOeisY3Omt_2kbQdbw-SbBrLmvUucr6m8ZhndulWUUZotEq2aLd51cyYdqK3jCBdZp4CI_A3Ccpi4i5Y3Piau-6oKclodbXSVzQVW_WC3wUmd_xmR9Ki5-YnRKeEvPKwO3rZXNFKHZJv99KxcVe9X6mf2IfI_V5UdpQx5pPLCO9xAa14vUjOJDMJMzCczD5Z0wxVpXwWspCsKH13DqsAR2NLrVrzGHqBSfAcFHtKJ1NbCB1u6XqkCPuC-CJxihk7sJVPxfo6yVOILu2rjHRpMGnriHuRsm7kkWh3P1Fw132nKir7y_KosNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به نظر میرسه ایران حریم هواییش رو بسته.
«هنوز به صورت رسمی اعلام نکردن»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66097" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66096">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ افتاده به دست و پای بکن‌ ملانیا (سردار وحیدی ) و ازش خواسته به اسرائیل حمله نکنه #hjAly‌</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66096" target="_blank">📅 22:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66095">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
حنظله:
تا ساعاتی دیگر، آغاز خروش آتش های سریع و خشن، به نقاط جدید الکشف حنظله در آسمان تاریک سرزمین های اشغال شده، هم اکنون به پناهگاه مراجعه کنید. شاید هنگام فرار حوادث دیگری رخ دهد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66095" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66094">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
یدیعوت آحارونوت:
ایران خبر درخواست ترامپ برای عدم حمله به اسرائیل در ازای مزایا در توافق را رد کرده و گفته است که به اسرائیل پاسخ خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66094" target="_blank">📅 21:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66093">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
زیرنویس شبکه خبر:
پاسخ به حمله اسرائیل قطعی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66093" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66092">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhRwEQ4K0SH8mwiHVeURiAm_b-cHjLi4KGqmxjuq5nzU3gmQ-6pxEF-Q3IP9wc6AdXzLFtaqiheV0xcayMiLB4NaM0OUAXzVjfTZMrE6d3w9IEvdQnPiWL_Hnw35foKGRphI4YioV6LhsqP-Xx3rKo59A8avIVh-Te18_fQCxIFlP1iikpGuv4q-3u7n42TNlXY08E9IUu92wvOEWjnZQroENLTAYs0itLIx8__yra14taOUVogHeuhj0zONgQRPiGur98pXIJmQ-yj2pKGOJT7tEOeL-aN3JXUk4TB4xuUCiUWhITJGTcbPm8HnoPRDsilMOJeGmWMIhH_Mp7_12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدباقر ذوالقدر دبیر شورای عالی امنیت ملی:
‏
پاسخ رزمندگان اسلام در پیش است.
وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66092" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66091">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ افتاده به دست و پای بکن‌ ملانیا (سردار وحیدی ) و ازش خواسته به اسرائیل حمله نکنه
#hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66091" target="_blank">📅 20:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66090">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOnZxYsNcbowskh25nP8sQUPWot1XNnwIPHTCdbp7b2grziEOmh9oyq7xSHUCBrlKuNXMOLNqQsFMibT97bMegzNbS12N5IG6nt-YbDSZ6PpKum13kdfGkT2qH58NsQPcSsOnWguBjVvfdHLqxUVd2mnsXei2pXf18TbdDK9LFBNa7uoAVa_axzMF_cBhVs7v654xpuVNuyhksDspfOTSXbcTQzEitgeChsh4bnTW76uNIh9o4ICwP9g0rhioeEQU1_U3MeZH1k9CZV6Y3rIAaQIVVVXJ6GR15Yr9gWcgQtO4c5kgqHywBV6GlS-ZK0fE2eJoIKHbwx-m18z7b7azA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رئیس کمیسیون امنیت ملی مجلس: پاسخ به حمله امروز اسرائیل قطعی است
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66090" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66089">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66089" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66088">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0qkbhLZQzCl31ZbEcC2d5udGeNhgg8XJ4et9l3XushVPXop5sDmqQC7DjII51TkpKhHtC1As3nvc8FKnP41TKO866b50cAXasoqIxpr188JK3LZ43anla4Sco86ulLSlH2ZTKmJnfh_hlOpOLkFhk8eNfYwYvPL7NF-0Q2sECgRbkoSGjSzSdbM0hC5-wesvrnsXGUO3kHjIRpF74glW05ogspTbVkRVzeb1RLWSFcuHmft5craQS9iSBuZ-2fGCEUuopfiIrmRJpys52J6CInMfa0qVumsbtaKsSJyjRmCQqG8MQ64CgEGvsFQrpjFq_i6jUvt22OMjiTnQBWw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66088" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66087">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a73d88cf6.mp4?token=Nt16g3moeBNtilo5M5AMiEFoeohh8WsoBqMQ8izJoQdJbS_cCA_RjJBnz10QMN8xji_Fcpp7UyYbhv4qOL0YGoBnQamTxnd1DJCk7dxASDCELcFPVHQzO8gcwnrvyH2gqoITYhdsnuL8Zxa8jRsjA1OQX9hfKdBQxAYIg6Q8OBIugklnSTjuZ1ppobOin4YUur3YLM277CgNR73dskl7HB9kxPZKaAAR8OWFL5dDNLZx4qoNvZZcTme6SICC3AU1g4rgv7xHVQIP33q2yLvubyO0auoZddUoTHsWR6DONJL-QPU42ac8p1OW489sIxfp7J0LLINqt_TqxN5gf38HzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a73d88cf6.mp4?token=Nt16g3moeBNtilo5M5AMiEFoeohh8WsoBqMQ8izJoQdJbS_cCA_RjJBnz10QMN8xji_Fcpp7UyYbhv4qOL0YGoBnQamTxnd1DJCk7dxASDCELcFPVHQzO8gcwnrvyH2gqoITYhdsnuL8Zxa8jRsjA1OQX9hfKdBQxAYIg6Q8OBIugklnSTjuZ1ppobOin4YUur3YLM277CgNR73dskl7HB9kxPZKaAAR8OWFL5dDNLZx4qoNvZZcTme6SICC3AU1g4rgv7xHVQIP33q2yLvubyO0auoZddUoTHsWR6DONJL-QPU42ac8p1OW489sIxfp7J0LLINqt_TqxN5gf38HzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ به خبرنگار فاکس‌نیوز گفت انتظار می‌رود ظرف چند ساعت آینده توافق  با ایران حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66087" target="_blank">📅 19:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66086">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfTKP-IXTgv7T8NfqGFD-RArQnFojymmAZP2XFTAfSfTOz1XUc2Cw6LUHPRwiZ71eN8GX0IXOcmqHdv4h-VoO2MnN1IYSQ6oZRPN3zIGIZmqGdYZDLXZN9FtB39YYbngzV6dNg7T7_AkuNaMQnGHY_Xy-ehJtBAL7RR47Xlb-XkeJ-0geItVEsGhVGHDGHVgl8WEG_bqEWR7eJTIe_L-O-RrzTzeXb7xcOR1rSDl4Y_Q0fhsfbb_PnSztXAWCWkC5WtKrnAZgpdbTlMJrxfq8hgYT2Dw3OvbFsrqXV27qWZCQoSTtbNhkpc-dO6ZhdfGHb55pE9KWjL0y1O4SyZuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید: رئیس جمهور ترامپ در یک مصاحبه تلفنی به من گفت که معتقد است علیرغم حمله اسرائیل به بیروت، توافق با ایران امروز امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66086" target="_blank">📅 19:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66085">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
پزشکیان:
شورای عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود.
رسانه ملی در حالی بیانات رهبری در خصوص عدم مذاکره را مکرر پخش می‌کند که بنده در مقطعی با ایشان درباره ضرورت خروج کشور از وضعیت فرسایشی "نه جنگ، نه صلح" گفت‌وگو کردم و ایشان نیز در همان مقطع مجوز پیگیری مذاکرات عزتمندانه را صادر کرده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66085" target="_blank">📅 19:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66084">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0x_nxc__lmvKZJMpgWhXZ97WgHuZcHfLu6Nj2I5CyTRkFtO2g2WRRQJ94gBlUhKZRRmce7U1WjKrIeUygBHegDsgMrK5SRnby1Caq9YF3Cwcd-JAlzzvdi7vEw3Z01059wyZYmCQf1bJRR5iUB6YEQmOM5fav7GcBlK9bLuu_-lDIiIPDPsW94nBzfn3fdRZ1pqURHFVm9PsG1tBtWYYZFsrwAot5ZT8g_dYjK8xMrPyNtmPihqvEmVDtOkT8BbzlQs_n82adJn4PFRo_16yBjiXGIQSm8s3vvO7Fdr2TVitA25dZOtasb1q6vIM3DJot6CirFoVL2ytiW3L8uXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ در مورد حمله به بیروت:
«این نباید اتفاق می‌افتاد، ما به توافقی که صلح را به منطقه می‌آورد بسیار نزدیک هستیم. بیایید آن را خراب نکنیم.» او از همه طرف‌ها می‌خواهد که عقب‌نشینی کنند و حملات را متوقف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66084" target="_blank">📅 18:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66083">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
وزیر جنگ آمریکا به سی بی اس:
انتظار ندارم حملات اسرائیل به حومه جنوبی بیروت توافق با ایران را مختل کند.
ما در مسیر امضای توافق با ایران هستیم و مسئله این نیست که آیا این توافق را امضا خواهیم کرد بلکه مسئله زمان امضای توافق است.
اگر ایران میخواهد این موضوع دوام بیاورد باید افسار حزب‌الله را مهار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66083" target="_blank">📅 18:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66082">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66082" target="_blank">📅 18:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66081">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66081" target="_blank">📅 18:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66080">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
احتمالا طی ساعات آینده ایران به خاک ما حمله کند
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66080" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66079">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5B4MM7ertBY3kNg49VDou3Jk9wpNMqqx9opJY3ra-_X3p7XUKbaZqEMSowdkYQDQMvq7b_D5JxBJVXkALO3gBSmPmxLUwr5kBv83qcOZRVsLBykhXRWMzmDEr1Nzc5eyznBusswJN-FdQ_wMg3nkrTOY6_1gh1VdOrpxHUTCeZUat2S4WEbBrKI2QcOgucucjLzE8jbRcO18oaf-WazFzs0I4wRPa_KYl-YtkBDZnlqit278J-41YZAZwzwTxE_yrBZFERkF6C2HxryCaHuYzrmRbTuLQLfn0cDDYWSclLqY509igk9oTe078q2yM7znQvRUaJ-BYToXxvp2PtooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی:
حتی اگه توافقم بخوایم بکنیم باید اسرائیل رو بزنیم تا ادب شه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66079" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66078">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXE9j7TV7p3hR-vXlvNbHVhMe_IEZCgRwJ5Sa0Ex7qtPBsAJrAEF3RKBBsblp7q3mk-g9kht-9KKoFrzU4_ypZqn6n_KMdP_XEbM0gQcS7mVFo4yPKIHzaw__yomgrCvP7DVZv85xCCfxcckjMHKwKCJAzirXAJmfaQz3ECVWIMxVKlKNSzyv0aFr4d0RwaWKfYn7eKTsPp3uzs9H2WKBi_MhedndwDtVekawdBwsG49ty76SsMJVHuVDzdustCNtvrxjP9O7LLBRT1P6JoEMCwdUK2c7ldBapeHlbZdYT_u_oS4BAKEYNcXuD4Ufi7y5S8BDkmd9A7e4Ze6i4NHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مرندی عضو تیم مذاکره کننده:
فعلاً مذاکره دیگری در کار نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66078" target="_blank">📅 17:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66077">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e954c10201.mp4?token=Az7HmaS3V97Ujw9QVYxfld3t-Qk83bQQ-r3cczxjUtQbOvJwJujZD3ZoGREY_COHGU_5OEI-VUusBwF4NbekCWWs9XHXgV1fIeYiDrrdiNSAaN5FmeKcUwHZfyNiYTE2bzT26eGf-_ds6O_oXyLfe5jgcuaLPs0cZl4BF-ofoICjuyB71zCRzFBfgxNxw4mRuFgH7LVC9HOqOqVyYHjZ9PrMOeFekz18AMOJWpS8Ye2q-6ZWtByfC4bYRobZvbFvq3ElYgAD0_8ZrT74WkG_dOGeFjek-ZHjVPV7YUMpYetWq25dfwFtC_6JIP-6_BrI0naLX7DB4H8dlr8UqIloyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e954c10201.mp4?token=Az7HmaS3V97Ujw9QVYxfld3t-Qk83bQQ-r3cczxjUtQbOvJwJujZD3ZoGREY_COHGU_5OEI-VUusBwF4NbekCWWs9XHXgV1fIeYiDrrdiNSAaN5FmeKcUwHZfyNiYTE2bzT26eGf-_ds6O_oXyLfe5jgcuaLPs0cZl4BF-ofoICjuyB71zCRzFBfgxNxw4mRuFgH7LVC9HOqOqVyYHjZ9PrMOeFekz18AMOJWpS8Ye2q-6ZWtByfC4bYRobZvbFvq3ElYgAD0_8ZrT74WkG_dOGeFjek-ZHjVPV7YUMpYetWq25dfwFtC_6JIP-6_BrI0naLX7DB4H8dlr8UqIloyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت اعراب حاشیه خلیج‌فارس توی این جنگ
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66077" target="_blank">📅 17:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66076">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66076" target="_blank">📅 17:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66075">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه!
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66075" target="_blank">📅 16:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66074">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60a237733a.mp4?token=W8PMAhE3o3HB-cph3iRxdto0K9KrbxwnM26EpaO_AgAbbHbMolbBlPHP7vt1eJk24x3Rf_lVWk-kJjKUcOd0At9-ffr-6eOgmiam_E3hrgvmIZ3HcX1mmCzjQuch24wU2H27EdFoP3u9RiLNv8evNO27o68DwNEZJZ-B2QJ9ubzK9RSn7lvNsEZuLUnkNx1qT-ifKTdhpt7YpGqt1fZAnSZ4TF_-gw9X6OnVE1ymJ8h6qtAhWP2NFJkklVevlKtG9M-V8XWaEH1oi3Zb1pDS9-mCA2o16re6HfNhpFBa90pukomplf24-uBHQSplQILBa9MJGa5Y9PTEz0zN9fp_Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60a237733a.mp4?token=W8PMAhE3o3HB-cph3iRxdto0K9KrbxwnM26EpaO_AgAbbHbMolbBlPHP7vt1eJk24x3Rf_lVWk-kJjKUcOd0At9-ffr-6eOgmiam_E3hrgvmIZ3HcX1mmCzjQuch24wU2H27EdFoP3u9RiLNv8evNO27o68DwNEZJZ-B2QJ9ubzK9RSn7lvNsEZuLUnkNx1qT-ifKTdhpt7YpGqt1fZAnSZ4TF_-gw9X6OnVE1ymJ8h6qtAhWP2NFJkklVevlKtG9M-V8XWaEH1oi3Zb1pDS9-mCA2o16re6HfNhpFBa90pukomplf24-uBHQSplQILBa9MJGa5Y9PTEz0zN9fp_Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسایی نماینده مجلس:
اگه میخواید این تجمعات شبانه تموم بشه باید انتقام خون نائب امام زمان رو بگیریم و این انتقام تنها با محو کردن اسرائیل از کره زمین به دست خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66074" target="_blank">📅 16:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66073">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyM8K7LK7oveGtSlA-TQaZE8QRPZRpcwLv2s8Bs2p91Ei038XMAVbYvvQFa_6isgTYMrrEi2cB4ejLNNzC7m3u337F7RhJihR1JVBlWKC9vL358nCwrOX3V_u5ARt_U0tVRaoDq5E6InhN6WKZJyJsTM6sTfaoute4z-5fADBjHIEHmpsmMcjfHbxdkXgZIBkojdrYA7AGVRzd-wI-uoUYHBblpamMtigiOEoGNXXr96-wKvS9hm7OkDnnkDGXIw9FiIjO183vAhWH1V5FjBp2CTE-Ms8PQPIW3XZORSYC-3G1yFGXmkyHIFHTJpF9ABDM5ByJCcgaa-espLq7iw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
تجاوز صهیونیست‌ها به ضاحیه باردیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را. با چراغ سبز نشان دادن به رژیم نمی‌توانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب قدیمی شده است.
اگر اراده و توان اجرای تعهدات خود را ندارید، سخن گفتن از ادامه مسیر ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66073" target="_blank">📅 16:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66072">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از مقامات آمریکایی و اسرائیلی:
ارتش اسرائیل،فرماندهی مرکزی ایالات متحده (سنتکام)را اندکی پیش از حمله به بیروت مطلع کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66072" target="_blank">📅 16:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=XufJCEUxH12hbA6lpnk0Ll7dAeCxEuAbmDzILRpBSJaxn3WT93oH7Efz5oLgkLbR56-ol2rOCwXloKK91PBZy77ezRfcCA7xitQz7RpLnc-zgAzb3DxxBte3s1BHcQ5-ebGVhGqTus9nWhtuwKN_pIvSolQYJdPMycn2uwKeskSPuhtAq6r4fHapV9UnfdOqYW0ds-ZzL43ine7JgV6DqPFCM-27c0Sb2S1B7C6IuLBaUhxdD6lNUVPlfp35gqKjYkl8kiHnS4XmdmZhLDVDrN6Z0q4EwXr_n4bo76emJFr2yAmVcLR-ED727hb4BGw0-WwCAwOf3EQl4wxjT-fr9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=XufJCEUxH12hbA6lpnk0Ll7dAeCxEuAbmDzILRpBSJaxn3WT93oH7Efz5oLgkLbR56-ol2rOCwXloKK91PBZy77ezRfcCA7xitQz7RpLnc-zgAzb3DxxBte3s1BHcQ5-ebGVhGqTus9nWhtuwKN_pIvSolQYJdPMycn2uwKeskSPuhtAq6r4fHapV9UnfdOqYW0ds-ZzL43ine7JgV6DqPFCM-27c0Sb2S1B7C6IuLBaUhxdD6lNUVPlfp35gqKjYkl8kiHnS4XmdmZhLDVDrN6Z0q4EwXr_n4bo76emJFr2yAmVcLR-ED727hb4BGw0-WwCAwOf3EQl4wxjT-fr9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم اکنون واکنش نتانیاهو به توافق
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66070" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66069">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">طبق گزارشات رسانه های لبنانی حداقل یک نفر کشته و چهار نفر در طی حمله هوایی اسرائیل به ضاحیه بیروت زخمی شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66069" target="_blank">📅 15:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66068">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66068" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66067">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d546d16a9c.mp4?token=U0SQg6Fy6-fv6T6Phkj2R87V6x9MTaI7f6JrIiPB2KMJLsMxLZl3s-TDSmnhJgfWAyl96-0CPoiSfTrJxACj_ph6cLSUbQRj-My3qBtsetcD1Yii_t41E710pF5eF5FzoHnCc6bjcAUXVQuyQtshpCr2GSqD-XKiHVblpv6dwikIvwRoneZ2upLWUSd_JBroLsEKlbrZfjjritCRd-AuAdgx0iCZGNXLtJ4lSVZQ06USHqTa1G6V5Xf4hX1WOtK_ElRnkDRDUXNxoHXzgeW1X5MBFBd5O7kN23hgQNHFSr9uEv90ERhnL-bI-AXtkDHryF7Eq7sIoN3JnAPbem6_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d546d16a9c.mp4?token=U0SQg6Fy6-fv6T6Phkj2R87V6x9MTaI7f6JrIiPB2KMJLsMxLZl3s-TDSmnhJgfWAyl96-0CPoiSfTrJxACj_ph6cLSUbQRj-My3qBtsetcD1Yii_t41E710pF5eF5FzoHnCc6bjcAUXVQuyQtshpCr2GSqD-XKiHVblpv6dwikIvwRoneZ2upLWUSd_JBroLsEKlbrZfjjritCRd-AuAdgx0iCZGNXLtJ4lSVZQ06USHqTa1G6V5Xf4hX1WOtK_ElRnkDRDUXNxoHXzgeW1X5MBFBd5O7kN23hgQNHFSr9uEv90ERhnL-bI-AXtkDHryF7Eq7sIoN3JnAPbem6_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: رسول خدا و همراهانش در جنگ لت و پار شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66067" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66064">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6b9063a8.mp4?token=nVtNhlJateqBmbPj7dPxDiCL2Htao0HVB7vEPRZtfCARnnCZsYANPabYhzSo4AoziEvYs91NwZlIJaNr7oL9A_xMrgTTOj8Yc2VFL_4-TDvBQpeSSN8oz5Ce-5hr5r7InBwTtEwxHFiukOEUvPQJAOBPpi8IJdgq68gSjf7JfStsc-KhOHB4TrzSqyElwQI_pxObQySYrf3h3YJpOqGqN2oHCZRkuoQpwTNaZq3Qo46eshVemTCUJ2o1gIHpiz-z_Hj5uItiQynVMyT_fZUNDj9GeVB8w_7P07kZkmwF4yifYGXbbIzJgzkWD4WAaVWE9zoRRxJEnRMbbEysEeTy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6b9063a8.mp4?token=nVtNhlJateqBmbPj7dPxDiCL2Htao0HVB7vEPRZtfCARnnCZsYANPabYhzSo4AoziEvYs91NwZlIJaNr7oL9A_xMrgTTOj8Yc2VFL_4-TDvBQpeSSN8oz5Ce-5hr5r7InBwTtEwxHFiukOEUvPQJAOBPpi8IJdgq68gSjf7JfStsc-KhOHB4TrzSqyElwQI_pxObQySYrf3h3YJpOqGqN2oHCZRkuoQpwTNaZq3Qo46eshVemTCUJ2o1gIHpiz-z_Hj5uItiQynVMyT_fZUNDj9GeVB8w_7P07kZkmwF4yifYGXbbIzJgzkWD4WAaVWE9zoRRxJEnRMbbEysEeTy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که ارتش اسرائیل از حمله به ساختمان حزب‌الله در ضاحیه بیروت منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66064" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66063">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
کانال 12 اسرائیل به نقل از یک مقام امنیتی:
این بار، ما حتی پرتاب یک موشک از ایران به خاک اسرائیل را تحمل نخواهیم کرد.
اگر چنین اتفاقی بیفتد، اسرائیل آماده است تا یک حمله نظامی گسترده و خردکننده علیه زیرساخت‌های نظامی و اقتصادی ایران انجام دهد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66063" target="_blank">📅 14:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66062">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
کانال ۱۲ اسرائیل:
هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66062" target="_blank">📅 14:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66061">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دیشب تو بازی قطر سوئیس، یکی از هواداران(خانوم) شرتشو در اورده بود انداخته بود وسط زمین
⚽️
@fotbal_xc</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66061" target="_blank">📅 14:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66060">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31239b7a33.mp4?token=UQHk3uNCUvUgRvDOWxHvyFmnakkJ9lXHWQkHtfRFQYjNMrZmqgRy2rRXtkvMheJTTMO4BQ9yxOG3oJ_sANwNqPFqbuvccxNyhZt-91EhtSbMp1mgerzYiU2vtZvwItF1c2vkvwJXA08L5E2bEnJw3CsjOOCoOSZQ7NHHa-7d-mbcvuRlb38kPoJRjLlWn8sNHes5n_CyjFOGMrNFRruzqolCIfvn6Bv9BdES_ZKyDdwfAoIjgXbweorZRgRIvXP7tGGhDBo6JtVVWEd_Ub_uckUvvN7LSaQrTw07T-A0VJMP3HzNrYu2X74F4jYQQgaKUNqt7krfE3dHzJdU9q6zkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31239b7a33.mp4?token=UQHk3uNCUvUgRvDOWxHvyFmnakkJ9lXHWQkHtfRFQYjNMrZmqgRy2rRXtkvMheJTTMO4BQ9yxOG3oJ_sANwNqPFqbuvccxNyhZt-91EhtSbMp1mgerzYiU2vtZvwItF1c2vkvwJXA08L5E2bEnJw3CsjOOCoOSZQ7NHHa-7d-mbcvuRlb38kPoJRjLlWn8sNHes5n_CyjFOGMrNFRruzqolCIfvn6Bv9BdES_ZKyDdwfAoIjgXbweorZRgRIvXP7tGGhDBo6JtVVWEd_Ub_uckUvvN7LSaQrTw07T-A0VJMP3HzNrYu2X74F4jYQQgaKUNqt7krfE3dHzJdU9q6zkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چندساعت قبل، اصابت پهباد حزب‌الله به منطقه ای در شمال اسرائیل.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66060" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66059">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
حمله سنگین اسراییل به بیروت  @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66059" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66058">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e4fa5e8a.mp4?token=c0oxsHxqTajFRcppAuaA2oCBo0NT85HO1Xz8J7d7NCB3NF_aUcO1bdLx0LrBfAxyGG9fbvh0B21nthgNpjN7_uIs_tZV4xAxHul8Y0rjB5kYLuy4ZULkGG6cQx8EiSW4ZHODto6UeCigjh30CYfoo5T-zCXyHBtXs5H90waEG8CW6AlYSu22BV4IDuT7axDrfaFY5zPyEnK9CxGubd0w3hfU44RMkiHTWehvIK5JVoLJkCguhOWwSyiWRwfyjctjHZ4YqykqOhHDmfqvx7beFcB6h4iLj6T9EceYyRQMJJbSAA0nMjj5lBk8HfQAS5EIrNX8U0DoYn3ykHtKSi-u1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e4fa5e8a.mp4?token=c0oxsHxqTajFRcppAuaA2oCBo0NT85HO1Xz8J7d7NCB3NF_aUcO1bdLx0LrBfAxyGG9fbvh0B21nthgNpjN7_uIs_tZV4xAxHul8Y0rjB5kYLuy4ZULkGG6cQx8EiSW4ZHODto6UeCigjh30CYfoo5T-zCXyHBtXs5H90waEG8CW6AlYSu22BV4IDuT7axDrfaFY5zPyEnK9CxGubd0w3hfU44RMkiHTWehvIK5JVoLJkCguhOWwSyiWRwfyjctjHZ4YqykqOhHDmfqvx7beFcB6h4iLj6T9EceYyRQMJJbSAA0nMjj5lBk8HfQAS5EIrNX8U0DoYn3ykHtKSi-u1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله سنگین اسراییل به بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66058" target="_blank">📅 14:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66057">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل:
حزب‌الله با نقض آتش‌بس، سه موشک به سمت شهرهای شمالی اسرائیل شلیک کرد و ما در پاسخ به بیروت حمله کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66057" target="_blank">📅 14:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66056">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcMu74mBsPhk_z4MCkHAyf5EJOalhqYfpWeIXBJQ5uWdbaSGy3QbT8jP4Sum5OSS84jxqsLk3rjQpgzcSgYg1IcSzTpc-PWc61x_mW57pwMT4Sl0zlOcH-_cNsohC8saF_86wpxoB4YSgfWO70N5XX7QXkMwkqL2QjnOfimYV79DCZPhP_uXqK3XFQBSRvj8kIVhXd2CR5fs3w6r5t3vk6L4-sDOVgIh_uehT3Pa_Li1rWmJVDywMFBTu-UdMQ8vt_d3rlustUJSRROgw1G7ktFwRr9z2aHaVdK3iNY6TvgM1TS0OO5PrIOlCcVTB6gpXZGvz8oT0lgrzNHuTWUwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بیانیه نتانیاهو و کاتس:
ارتش اسرائیل اهدافی متعلق به سازمان تروریستی حزب‌الله در ضاحیه جنوبی را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66056" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66054">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVBQekkR2H0dRgTfELLj-XOzcrQgjbIlqd6PhZ47f_hIcnRSGFto_-EZdMpaJ61F9gSWC7Jr887U2FLxre_cu6VVMUqW_sKnJVyT-zC3ha7G5nUT8CvP99cnD1195QnBq7QunqXYkE71UGik1sICpV7UHIzPItDBjHAv8N5CU8vM2etc-j9FnUxTPgKZOD38JNL-r_tbIqQ-diAHw0WZMz6AGBBeBtgExNsg-JdlYx5AmqVO8977McMwekIxTmPO7aXAZGmK6UhUIr2rek2F0osfsWwqx772GpnOwQBuXvCdTaRd0Rfl8IxjgltOQb382ftFPRPwcaItOeswqCte-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها ازحملات اسرائیل به ضاحیه بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66054" target="_blank">📅 14:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66053">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0119b4719.mp4?token=olyAvi7fREZlyu9k__ZSjlMWhTfI2FJDjXnfh21U3XOPyqi9Fw09vIM-5LLJ8GPrjNLaHKitJar68zVpkanZ6HFHBi0rbwoHTdaFNRTR-fUnLhKkTiIdtNtIZOlwg5jm4Xd1HCPnif8-xx2UsbjB_nq_mtYmXv0PYR9YLk2_PlbtbAVpWiiVDxmpjtrAYtRCBdC2foutFeOe78ZCkPeovnoP2clQo5DIc0FwOmvog2NiW3UDDM7pqyEEkX19Y12QcUNUkgsmrLKeDUKjqEYI5-D9Q7ictjGyejee9xl3O1On1gHutEVvdZRi4dkxPABYSdaD5qX7HGryvXjwn7bngQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0119b4719.mp4?token=olyAvi7fREZlyu9k__ZSjlMWhTfI2FJDjXnfh21U3XOPyqi9Fw09vIM-5LLJ8GPrjNLaHKitJar68zVpkanZ6HFHBi0rbwoHTdaFNRTR-fUnLhKkTiIdtNtIZOlwg5jm4Xd1HCPnif8-xx2UsbjB_nq_mtYmXv0PYR9YLk2_PlbtbAVpWiiVDxmpjtrAYtRCBdC2foutFeOe78ZCkPeovnoP2clQo5DIc0FwOmvog2NiW3UDDM7pqyEEkX19Y12QcUNUkgsmrLKeDUKjqEYI5-D9Q7ictjGyejee9xl3O1On1gHutEVvdZRi4dkxPABYSdaD5qX7HGryvXjwn7bngQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
تصاویری ترسناک از لحظه بمباران یک نمایندگی خودرو در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66053" target="_blank">📅 13:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66052">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17f35bf38.mp4?token=u8K6QAThkv5M1hF14I4uZNXvPmAzfvjWgctx7pLd9uFFtPl__3SwBV6USeII7BrBbtGrbNT3ucGSjkMJk8FFYnoAHpJWwHzBhGqK3vrXjAMNMFeRwZ9mmTqGtrrQ0TQ6RwgXtPikwXkDpOedcvjXZoJfjZ1W0dqawEi4-ShK7zKBwm4EbiTahTZRU3GLRJBKoCp3NCl92z-s1TKOf1YdhahrN9Bjg8OYyxAuoCf-0CEdlGfrZjE-xIywMPNhC7pczukQIlX8P0A4zSUndKv2q5wHvYkFe4Bvlc_kKNcAsWAiu-y8GEVlKAD7AqV3yLreQogZHH-UyW4vdLPmg5gioQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17f35bf38.mp4?token=u8K6QAThkv5M1hF14I4uZNXvPmAzfvjWgctx7pLd9uFFtPl__3SwBV6USeII7BrBbtGrbNT3ucGSjkMJk8FFYnoAHpJWwHzBhGqK3vrXjAMNMFeRwZ9mmTqGtrrQ0TQ6RwgXtPikwXkDpOedcvjXZoJfjZ1W0dqawEi4-ShK7zKBwm4EbiTahTZRU3GLRJBKoCp3NCl92z-s1TKOf1YdhahrN9Bjg8OYyxAuoCf-0CEdlGfrZjE-xIywMPNhC7pczukQIlX8P0A4zSUndKv2q5wHvYkFe4Bvlc_kKNcAsWAiu-y8GEVlKAD7AqV3yLreQogZHH-UyW4vdLPmg5gioQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو برزیل یه دختر 21 ساله رفته بانجی جامپینگ یادشون رفته براش طناب ببندن و انداختنش دختره هم فوت شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66052" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66051">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66051" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66051" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66050">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3rnOzZ-6IAHWTYVOQ8PpsPGqx7lrhgVSzOqjLm4ekVzyPEgp2FBIIjtnO_2HD_8PJOlTokhBzt_dvV2oCCfeCxThP8kpMt9NB97C6hyRFMY1NQChHUSwpCMOcJm7tS3B6TYmT6CpoDFDQ_Bzgg5gM2YpnWYZrISaerwqH-mhTg_Ger02EWuJ-KQaGR398vq8ZqxOcv11CUDSH0tFIi_USZaRFVxlQWq4p98yR0wqIGUCBuVtvxBNALUP7e0fx9jPFWIR3aYIf19uiwCzKkR_s6ZCa0jeCzNTyIAyhXLyWNTDvKodEYOSoOlu_UXd4RKqynH5Y62w6LHSQulY50PDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66050" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66049">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db36249809.mp4?token=sfOjLrIzIe54gOpIyJZqh6GIBFD3pjwdNvvNfre4yVLSuZpKjnWQBVnkEeQO5BUxPNrEpUMB2zItSYVY7xpT_9F8T0JpAc_Onf_lyA12hV7crSsRhimqJe3XISROJGZA2o4ZCkF5n-I_Cv-vjI9lzrnzBLNN_WxAQ1amUUZ-VkDTgweB4aUY197h-P0A6aq1-Ci4kFl9sX1VocIkYOktzlBmlZD__EoSodx9onNh_3HJCu4rafXMIS3c-d1DfW3271x7ynp8uAI2TjpNYFoiM7SbnsJMDTs0hbR3lAHuMNllZrLUiKqRGi1tMfZth6JiSa8YpT6W6bOTArkFZ88GMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db36249809.mp4?token=sfOjLrIzIe54gOpIyJZqh6GIBFD3pjwdNvvNfre4yVLSuZpKjnWQBVnkEeQO5BUxPNrEpUMB2zItSYVY7xpT_9F8T0JpAc_Onf_lyA12hV7crSsRhimqJe3XISROJGZA2o4ZCkF5n-I_Cv-vjI9lzrnzBLNN_WxAQ1amUUZ-VkDTgweB4aUY197h-P0A6aq1-Ci4kFl9sX1VocIkYOktzlBmlZD__EoSodx9onNh_3HJCu4rafXMIS3c-d1DfW3271x7ynp8uAI2TjpNYFoiM7SbnsJMDTs0hbR3lAHuMNllZrLUiKqRGi1tMfZth6JiSa8YpT6W6bOTArkFZ88GMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۱۵ سال پیش زنده‌یاد مانوک خدابخشیان جنگ میان جمهوری اسلامی و آمریکا رو اینجوری پیش بینی کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66049" target="_blank">📅 12:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66048">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
امتحانات نهایی پایه‌های یازدهم و دوازدهم به دلیل مراسم تشییع علی خامنه ای، یک هفته به تعویق افتاد.
پایه یازدهم: شروع از ۲۰ تیر ۱۴۰۵
پایه دوازدهم: شروع از ۲۱ تیر ۱۴۰۵
جدول زمان‌بندی دقیق به‌زودی اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66048" target="_blank">📅 12:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66047">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28745391f.mp4?token=ftVH9lmfyib7gtYmnxt14ofchq7QGrZGTmcHiNtZ3rwB8i9PIk-TeQPZQKzTO16CIQi1JmRa7tg08rCQ0-8pDW1igXv5jfaixVRopoxVescZoBjCaNgAZN85k-ZA0UAt4e47xq8rhyrYLi6lNXrN7xy0h3bGR_Kh9nDL5PaAUA-pPdRfb7EbSOSIFj0MyQhUtCqnQlpWkydvEuQUBufz2hTGlElSm9FoFcA8uN82-tsNaI_issC0443QTGjUd7vei2-1xgavu4B-PLzAE8yF8nrbzrlaQj9EmzUc49S1JvjJXl6582GFWf05G3jo0nFZFdNbhaKAMuwsuS3p37iKvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28745391f.mp4?token=ftVH9lmfyib7gtYmnxt14ofchq7QGrZGTmcHiNtZ3rwB8i9PIk-TeQPZQKzTO16CIQi1JmRa7tg08rCQ0-8pDW1igXv5jfaixVRopoxVescZoBjCaNgAZN85k-ZA0UAt4e47xq8rhyrYLi6lNXrN7xy0h3bGR_Kh9nDL5PaAUA-pPdRfb7EbSOSIFj0MyQhUtCqnQlpWkydvEuQUBufz2hTGlElSm9FoFcA8uN82-tsNaI_issC0443QTGjUd7vei2-1xgavu4B-PLzAE8yF8nrbzrlaQj9EmzUc49S1JvjJXl6582GFWf05G3jo0nFZFdNbhaKAMuwsuS3p37iKvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
صحبت‌های حمید رسایی علیه مذاکرات نمایندگان جمهوری اسلامی با آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66047" target="_blank">📅 11:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66046">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
ثابتی دیشب تو تجمعات بسیجیا: عراقچی خائنه و من طرح استیضاح رو به مجلس ارائه میدم
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66046" target="_blank">📅 11:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66045">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vchcdRY-zXlAc8y0wKfULFOg6d_ZKynquzuTxEV7XZ9QoQg2MpLfetD17-ejbU2WQlHQQbQr3nV6zB1wopqu2qHLsxkneVSvdQuGXwIzWh3AJEPRE4UV2uSPO_ypX9sX99_ZTzmumMA3BybluIqCzUlU_rJEol2gM-7I6NW22l7lAFiBLjqmqzrILLb6f5T1YJTKwwruMxlRJ42GE_hekp0zRVdt2iB0rnXRP8othxAQSap1Yn05SxVIHTKAX1WsVIHsBvbnJyZZ4QFTJvJ8Ina8vbB4pjWuYq3WCb_oxG9PqiBUwrDlEIhzXwnuTKyaRnIKSnT2pZt7ni70Myl-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی والا مام خوبیم
بابامو کشتن
زنمو کشتن
بچمو کشتن
«ولی رفتم باهاشون توافق کردم.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66045" target="_blank">📅 10:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66044">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375671acc0.mp4?token=i6fxX9hUSQHDKzNwLCD1ZQrgWAJLebqE36nDc_BEK1vdeKzFzwCft1EPb2GTsuNYnAuWv6WGwmA83kf7qIr572j3zUOMdd9rrmt2SakuPp3D5g9rN3M7XV4o1MZCez36ReTCrKQ_YKEQy8aSgDOx448QuEEqt2JPUOrrwEWnQ-QzGCNk2ulYfjv0KeyTHGzG6sPxIhBPNW52kQvYF_fYdqSRPFrBfYI5Hb0MLxlrUlm9iDMM4or2LGrkyCUWHmn6YMqOszdREDwbUUGnV8xs8jUC455PptNWs3VF35Ujq9zMmh9Di4xUiBApPBthhmVgig0cfOt6uE9bQfIqqS76Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375671acc0.mp4?token=i6fxX9hUSQHDKzNwLCD1ZQrgWAJLebqE36nDc_BEK1vdeKzFzwCft1EPb2GTsuNYnAuWv6WGwmA83kf7qIr572j3zUOMdd9rrmt2SakuPp3D5g9rN3M7XV4o1MZCez36ReTCrKQ_YKEQy8aSgDOx448QuEEqt2JPUOrrwEWnQ-QzGCNk2ulYfjv0KeyTHGzG6sPxIhBPNW52kQvYF_fYdqSRPFrBfYI5Hb0MLxlrUlm9iDMM4or2LGrkyCUWHmn6YMqOszdREDwbUUGnV8xs8jUC455PptNWs3VF35Ujq9zMmh9Di4xUiBApPBthhmVgig0cfOt6uE9bQfIqqS76Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ١ دقیقه رو گوش بدید
زنده یاد مانوک خدابخشیان میگه :
رژیم اگر توافق رو بپذیره به جاکشی می افته !
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66044" target="_blank">📅 10:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66043">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDjxbWXY_EVZplIBVNMN4ChmcP6hV5rQMs_7v30tRhTaOuApHWpsXSWIkuBmP7NSbpPPjoxT55WKE7FFYvDz_wZGw1Ya2Hm5Acn3fEJy2SmC-zDYO_bz4duCAvCSOQrkqiG-tarSLNnP-THpdUG4Sw12dJO9XGix2u5C3Gk735galw0XeIM6SNvtpuKUuoxoZkzJqD-ghTmeD_usylGlI8YjcbhUwRrOQ0a_cN-0BCSZss3r79RP5OKyPSmIfi1-UCsl1GwvLPlY2t2Vy1uy3oXyRZewhSF26GCOOyODtMi2Tba4W-NcXaVRp-mnrFL1r0XTM_73Sr8ly1EcnQrnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط عباس میتونه جوری توافق کنه که:
جمهوری اسلامی ناراضی باشه
مخالف جمهوری اسلامی ناراضی باشه
اسرائیلی‌ها ناراضی باشن
آمریکایی‌ها ناراضی باشن
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66043" target="_blank">📅 09:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66042">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518512af42.mp4?token=CRNESOeaUWy87vXCc04DyBtyTqdVt_cgNBzm4PXEPLnvMl7Np0l3AnJJglfm_o_6EO4HWxqr5-nBg1BAKQpphEq2-j8H00SasnpCLjd9yczBXGyD9KF6x6_wTwMn05kr4dD2wTP47GFLgb72GJdAYABb8Xkvs1J6bLKMn1mMz7Dt3c_HUmAyeMseRhNmrx8f8jD_UTwHN7_PMUa2W83i59CYYvg4soKUqVtzYFV-sDVyBzflweVs0-5uGu5OYtb8jVifThThj7RYJJqz3wLpjO8Rho2yfv9IHTOCuIVRrACKKYaKbrCkXupezxcVSFFDOxXI6SYEWh56iijLRyybNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518512af42.mp4?token=CRNESOeaUWy87vXCc04DyBtyTqdVt_cgNBzm4PXEPLnvMl7Np0l3AnJJglfm_o_6EO4HWxqr5-nBg1BAKQpphEq2-j8H00SasnpCLjd9yczBXGyD9KF6x6_wTwMn05kr4dD2wTP47GFLgb72GJdAYABb8Xkvs1J6bLKMn1mMz7Dt3c_HUmAyeMseRhNmrx8f8jD_UTwHN7_PMUa2W83i59CYYvg4soKUqVtzYFV-sDVyBzflweVs0-5uGu5OYtb8jVifThThj7RYJJqz3wLpjO8Rho2yfv9IHTOCuIVRrACKKYaKbrCkXupezxcVSFFDOxXI6SYEWh56iijLRyybNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه آخوند آوردن صداوسیما داره میگه به پیر به پیغمبر اماما همشون با دشمناشون صلح کردن شما هم شل کنید دیگه.
«
واقعا بی شرف تر از آخوند هیچ جای دنیا پیدا نمیشه»
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/66042" target="_blank">📅 09:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66041">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/66041" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66040">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkVIXh-7MqBoe2lSTmgrLcJbKpzFndHp5JIkz3yezQrPpi_VRMv8Rl3tUbq5jxjR-0oJTFM-MpNOcFkUE-qzLyP6MPA7uSB2zz0LC5gNIS_5Or8woLE5ENPwSPXEQNE0NT3br8LNDeP6sZWVqH3ytLsZTnkRsADG8ektcxGR0MSsPpUu3ToO-Blh7xNd-0vXF8Mr3tZ_Lb0CIPkOsYYiBhoVx7Ecq2WRS9aLY4dZTgVq1Q-S1OW9u0cA-9OEchkzMS5KCYnR-mzMyV7hW8uZBZFWDFTER23aZtVN-VZEs04nIaOMOp2MInDcAmSSDWwHqlRptMLxIPaxGc7XGA0Kfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/66040" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66039">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBSojXyyvjQrs5HUKKZKRWDbMHXz8wpCi9xVwyqY56c6MrCBwEgzFIYvUJggmAUDIsN0dDwSvSijV5w9xDd0alYLzc0QKBKyPektQxifntGVZE7JYh0qXe61GO2CWHFLUxeSjNpxkq6MTgkhSAv_hYbpXnVP1nPpSOcxycYOt8CM09vEG_Y55XtU0sxG8OZhHiEl4RrInJavAHHL4E-Gw2zRqgGtlGEutuGD0Q3qatgZZMxbQ8FPJQWMfskIdYnRLVP-39Stxqx6vbT_W2hFs7ByZBwbsIkkIOjM5p7mYzjTVDek31smBgEc4Mo02WRQEjZFHuTHEtBMDGr5aEFvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66039" target="_blank">📅 01:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66038">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=Tmi5W8YJRF0k8-1UKXFvTkKQORN62PpIuiHsukfWasno7GOl7UsZ3p1cMUxVdEMHsj6FwZb28L6kmqQhYp601cJKqiqzpUxTjKup93UFA5o7IbzNyVV8xTniSN_Yw-DIETofH1fy-mTQNJiUI59NpzPqSXlEklZsZbA1KTASg52ha-bt2U5cuXl8SbXWaYXbBuK4F1XLe0C8wA0PVc-mUs1lUEKa3IyfbkJtlWujH-RDs25SySCcPiEzj_ii38AxDKR1TpJhCJs5CD1FZN-Lk5meqGTLSZhFe2hg5m1L564A3E8LplNjUDO9JSjsmPTpL9MQ-cKnUi1ZOnTmwABc2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=Tmi5W8YJRF0k8-1UKXFvTkKQORN62PpIuiHsukfWasno7GOl7UsZ3p1cMUxVdEMHsj6FwZb28L6kmqQhYp601cJKqiqzpUxTjKup93UFA5o7IbzNyVV8xTniSN_Yw-DIETofH1fy-mTQNJiUI59NpzPqSXlEklZsZbA1KTASg52ha-bt2U5cuXl8SbXWaYXbBuK4F1XLe0C8wA0PVc-mUs1lUEKa3IyfbkJtlWujH-RDs25SySCcPiEzj_ii38AxDKR1TpJhCJs5CD1FZN-Lk5meqGTLSZhFe2hg5m1L564A3E8LplNjUDO9JSjsmPTpL9MQ-cKnUi1ZOnTmwABc2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
شعارهای معترضین به مذاکرات با آمریکا
اگر چیزی امضا شه، مسعود باید کشته شه
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/66038" target="_blank">📅 00:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66037">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
⭕️
شعارهایی که در تجمعات امشب حامیان حکومت سر داده شد:
۱_ تا باقر کفن نشود، این وطن وطن نشود.
۲_ مرگ بر سه لاشی، قالی مسعود عراقچی.
۳_ این توافق خونیه، باقر خودش کونیه.
۴_ خایه بخور با سینی، عباس بچه قینی.
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/66037" target="_blank">📅 00:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66036">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEF0rYhniRnh5j_duF7GMDZub4eDV28z6tsfS8t2K5E3JTaVJp81v-JVjnVz0hcsfurC59c0a3VwczDoQuy7NV_qITOUTTGB4xKtiLVw_e4PyKj7ce9Sddjy2LULuTWeFvlf_o3hSXxCOwqqkjXY_tojvyIAkNhDvUAkiPWOAMl7Vt04g9F49BVeoKIS_axGxSWpRruukEqGNKCyZpiuyZM3JeBaAn7rw3UXYLVf28YpferqpbGX0rS-BsTkk16wDnCTN7dmN7o81Xx4j6oekUMc0Ji6mWH8MgG11QFhDpwJtjDQBv2Eck2jB8O19FgoILxkg-4mHuCACNDAvsi94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ و پیت هگست در موکب هیئت محبان امام صادق (ع) کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/66036" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66035">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaR1zTC0D3suLUWEO7PPV4AwWxAbok-a15e6_r4Wy5JgHxH2Y7VhzX-FwziEdh3yhu4ARftgpoMF6hDjLlTIDIb3_uWmfUGsub3r17VBNyhm5fIVPl8xTaUKT0KxlqPdMdojLvgTWJnd0z19WhgfHyvuNWhZQRLIgw-PG9toJH0GDlxBNBI3RcpDyZLm21iUFXk8scsZ_EG5pMYubXZvuclkdU__DZmwDxgC9C7tZm7Xzrvb6JSsValVFcAlW1mszfMwtZNrbAbWYfqY-zyD7IEVgtF-bJI8E2whlob34ZUHKCQnwekTGB0xHFBsQUjlu05H6JoLHzeNZlMIrjF9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
توهین و کنایه بسیجی‌ها به آقا مژتبی
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/66035" target="_blank">📅 23:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66034">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
نبویان :
امریکا اومده به اینا گفته 300 میلیارد دلار بودجه بازسازی مملکت رو از عربستان و امارات میگیریم تامین میکنیم که خب مشخصه نمیده
اگه آمریکا بعداً بگه ما از عربستان خواستیم پول بده ولی نداد، شما می‌خواید چیکار کنید؟
«وقتی توی متن نوشته شده هزینه‌ها باید با توافق دو طرف انجام بشه، یعنی آمریکا هم باید درباره محل خرج شدن پول نظر بده. حالا اگه آمریکا بگه این پول نباید فلان جا خرج بشه چون ممکنه به دست سپاه برسه، اون وقت می‌خواید چیکار کنید؟
من بهتون قول میدم نه پولی واقعاً وارد کشور میشه و نه اختیار کامل دارید که خودتون تصمیم بگیرید این پول‌ها کجا خرج بشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66034" target="_blank">📅 23:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66033">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU7D5elcqY7gHL5fGv7ZzLh_v8OlrYLh-SgBn56DRcHB8394MFA3aQ_nLo9olW9eANL9B20sTOkS0YaTw0R6AmBKBaYnawoqGbl6aPoWey-jSuHwdWHkhQStTURb-uMtFqLKPUeBJ_d04DRyfHKNfCaX106TfKzVWQgFhU2Oh7SKF95p7KRTT9DJMPsKSSTGpqqHam4251KnkO1i37o97S_JG4I6iOTG6tq8wBshDxPZdEpC1Y09WhddtX5q52NUT4ZbajmZLUIVz6VVQr3G_yMlBrlCGXIOAWLL0l3piDLwsfYgaqy_0NpQlOHKV4ftuUmX9GQvqrsQAD5ak92LRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز دفنت نکردن فردا هم قراره با قاتلانت توافق نامه رو امضا کنن
😂
...
«چقد تو مظلومی»
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/66033" target="_blank">📅 23:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66032">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:  طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است. نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.  @News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66032" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66031">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077634d539.mp4?token=ulA0-5OBcz2huOisI6cG0uYp6NPXHmNNbsEve_FDWJGtnmBcJtEuj93ppXdrEq2CtV4aUZ9dkY4JcfCracJ3lR3UGU0UAey0C-ublXpaZidrP-VzAMRgeQJOq_GaLyCHHY_R_Pfp9d1wiQXPBncy_s2jv6bGuOB9UwI--3MaT2q-Xkpy1QN21Fit6c_hLKboaw4NCrOkr30R9SNCBgUZnzGJT1DmqaQLuz7CtS79UlFoL80rcTR5v8wDULJv3Za5j3wQHjEstpoBd7pplnkr6xAHbBOkEJhdwM5bOciegAzCzh90mwy1FKpX9HuHy_NjbhR1XF2rOo2sNbdzNN82fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077634d539.mp4?token=ulA0-5OBcz2huOisI6cG0uYp6NPXHmNNbsEve_FDWJGtnmBcJtEuj93ppXdrEq2CtV4aUZ9dkY4JcfCracJ3lR3UGU0UAey0C-ublXpaZidrP-VzAMRgeQJOq_GaLyCHHY_R_Pfp9d1wiQXPBncy_s2jv6bGuOB9UwI--3MaT2q-Xkpy1QN21Fit6c_hLKboaw4NCrOkr30R9SNCBgUZnzGJT1DmqaQLuz7CtS79UlFoL80rcTR5v8wDULJv3Za5j3wQHjEstpoBd7pplnkr6xAHbBOkEJhdwM5bOciegAzCzh90mwy1FKpX9HuHy_NjbhR1XF2rOo2sNbdzNN82fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طرفداران رژیم دارن شعار مرگ بر سازشگر رو سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/66031" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66030">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9383ea7d9.mp4?token=QdOjKngEYuOIUUeM_fspHg03G3RF2KicYvbh9ZUnzcs5WiILwTCztPyHgKaxb36fgH_WYqZygUrbBmlpBSt9VTs9CnhPHhi0XBhy3WYYE6YFI5kg7jmaqYh6bonXVrbwIU2g09w2jLISpjamo-hgYgOc_TLC_-ke7eXsYr515INX_flz14eSgiusJ5WfPTCI12RJ-8CTS9t1Pi5UykEUqvSmshO7d0QL1xIV4gpjN5lBojKBcPl37_tOAkmysY-iJ9FVbFvcZayQANMag9Kfg4CWBrKFfi8qJRXdwGigZgrSXTyebwV_2ZzvbPKubopg9KVOPVNJj2pNHMHu2MHS-76VE861dwtgVRq1uPPYyMgAUDH0mmOCC1l0RdWTYZ1h9Iqyti7VmO-t_sUQwA_fxcRWs9dk_D7tF5VM_22FXL_4jxJMlh3YUxmh4TOcdahe2otNcn1C92uWIEdV9vX35M1Dyvj77QGK3koL6ztXB2TNDo9p25orSemhwMLj74_BSxeN5yaz_1EY3jWwsq7Dhnhful9LHCpV-0wpnJr4KYBGm5feB6UBFuZ7G8_I_pnhu4r1SUf1-kUJar773XWsve32ezjUBmED_gQ3h4S1w226qBYU0m-kPELeUq_4AwVfTOd90ApdL4skJCQN7BaZlSHuBqiqE0sApWBbvGQqvc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9383ea7d9.mp4?token=QdOjKngEYuOIUUeM_fspHg03G3RF2KicYvbh9ZUnzcs5WiILwTCztPyHgKaxb36fgH_WYqZygUrbBmlpBSt9VTs9CnhPHhi0XBhy3WYYE6YFI5kg7jmaqYh6bonXVrbwIU2g09w2jLISpjamo-hgYgOc_TLC_-ke7eXsYr515INX_flz14eSgiusJ5WfPTCI12RJ-8CTS9t1Pi5UykEUqvSmshO7d0QL1xIV4gpjN5lBojKBcPl37_tOAkmysY-iJ9FVbFvcZayQANMag9Kfg4CWBrKFfi8qJRXdwGigZgrSXTyebwV_2ZzvbPKubopg9KVOPVNJj2pNHMHu2MHS-76VE861dwtgVRq1uPPYyMgAUDH0mmOCC1l0RdWTYZ1h9Iqyti7VmO-t_sUQwA_fxcRWs9dk_D7tF5VM_22FXL_4jxJMlh3YUxmh4TOcdahe2otNcn1C92uWIEdV9vX35M1Dyvj77QGK3koL6ztXB2TNDo9p25orSemhwMLj74_BSxeN5yaz_1EY3jWwsq7Dhnhful9LHCpV-0wpnJr4KYBGm5feB6UBFuZ7G8_I_pnhu4r1SUf1-kUJar773XWsve32ezjUBmED_gQ3h4S1w226qBYU0m-kPELeUq_4AwVfTOd90ApdL4skJCQN7BaZlSHuBqiqE0sApWBbvGQqvc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
نبویان: من خیلی ناراحتم این چیزی نبود که آقا گفت. پیش‌نویس توافق بازتاب خواسته‌های آمریکا است
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/66030" target="_blank">📅 22:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66029">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722ec8c49a.mp4?token=gfk2YZLNMAnV7FUPOT-dtZhGsC-zg2xwv-BAAKoLvWC0Umz2qxctCvGlW1TpEtPk1BO_6F1Q3kfRD1kEwYHMrWXf-UKlVeA6Tl4vXGChjHg0pl6TD08dvSyvTM-7lM4FbB8QbVFru6OMObovLLDDsoc79m_ISfFL5U9rjnEWQeLwOjUOi6-2D8_Jq2hsNtcOwXlrN4ZqzMX6aUJ2jw3OV-P5Ip2Mq2qukxi0G2kkXHof7--A1J6HFayIM3A0cWbb_joI4YOZM9reA0bPSqYaMCCkHzMMid8w9k3eYSG73wENkz32Op_j-HwlhBJF6kzJQ1eAA9w08zpoNNW5DfMXQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722ec8c49a.mp4?token=gfk2YZLNMAnV7FUPOT-dtZhGsC-zg2xwv-BAAKoLvWC0Umz2qxctCvGlW1TpEtPk1BO_6F1Q3kfRD1kEwYHMrWXf-UKlVeA6Tl4vXGChjHg0pl6TD08dvSyvTM-7lM4FbB8QbVFru6OMObovLLDDsoc79m_ISfFL5U9rjnEWQeLwOjUOi6-2D8_Jq2hsNtcOwXlrN4ZqzMX6aUJ2jw3OV-P5Ip2Mq2qukxi0G2kkXHof7--A1J6HFayIM3A0cWbb_joI4YOZM9reA0bPSqYaMCCkHzMMid8w9k3eYSG73wENkz32Op_j-HwlhBJF6kzJQ1eAA9w08zpoNNW5DfMXQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشایی تنگه‌ی هرمز که قبل جنگ باز بود الان شده‌ی آرزوی ترامپ، آدم می‌مونه چی بگه، دهن تحلیلگری که بگه آخوند تسلیم شد رو باید گِل گرفت، می‌دونیم که این تفاهمه و توافق نیست و توافق اصلی در طی دو ماه آینده مورد بحث قرار می گیره ولی همین تفاهم هم فقط و فقط به بقای جمهوری اسلامی کمک می‌کنه نه تضعیفش دقیقا به مانند برجام.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66029" target="_blank">📅 22:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66028">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGWnkXB-Mr5EYx7heQhzY0cnmW62VcR4RAvBdFBnVDvvLWJ3uDMdocfQypMDfHiX_sHTz_Fsoz7PhAgP77KUGrYiM8664URTUaYWsZPq8aX0j4HfI_WiFq7machV5Gp5No386DHqjHQlDMGwFereXoXWr9eUbYMkwQN7HMemetTLnaEHFW9szUjHhWlHd3Z8Y8AO3TrLQWg58aYBPBmwzdJh6ncxZ9Dlv6kJBcLEZtrlWRPIkSZcRc1C9AIyxAtEPqfKrJKVhIyxXdeDLCW6HJFNpSh0V_aD7w8hsSdvQwjobnZ7FVXVdMhjt9i6t-1OwpIlclOmk-hDuh8Sfdac6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فراخوان اعتراضی نمایندگان مجلس علیه مذاکرات و توافق
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66028" target="_blank">📅 22:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66027">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
رادان: هر فردی که در تجمعات شبانه برعلیه تصمیمات حکومت حرفی بزند یا شعاری دهد به عنوان تفرقه افکن با او برخورد خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66027" target="_blank">📅 21:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66026">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3933369d.mp4?token=G3xHcWEjCPFPPFsVqnZ3v8-9gPXz1FcJ8NSYLAYV-2wN-4SoDGLfCFxBc-fTSfT4gFpvc4DGnIEdZ3fyNqfD1KUsgMyD2Z5OhxLyZ4JAVZ4ubQ7wfKDGCQOrECdRoFEn70zrFHxIx3NcKBe-CDbXtiOsGisL-9WToFEjc2n1FVlGt02JReEFDvxWbsQHuyETenmFIvCOd3qNoHIz8RDEPgvcTQDEZ-9o_e-SQIyhjXNVf7-kP5CV9_ghj86yFbwVI4MBgfJh70_so5bRR3vMcf-04Zmca6fJ67WdFMz0hsKJCYuzU_yHi1_52uXM1jR_8Yzuy-HImvrHL1VDCLdT5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3933369d.mp4?token=G3xHcWEjCPFPPFsVqnZ3v8-9gPXz1FcJ8NSYLAYV-2wN-4SoDGLfCFxBc-fTSfT4gFpvc4DGnIEdZ3fyNqfD1KUsgMyD2Z5OhxLyZ4JAVZ4ubQ7wfKDGCQOrECdRoFEn70zrFHxIx3NcKBe-CDbXtiOsGisL-9WToFEjc2n1FVlGt02JReEFDvxWbsQHuyETenmFIvCOd3qNoHIz8RDEPgvcTQDEZ-9o_e-SQIyhjXNVf7-kP5CV9_ghj86yFbwVI4MBgfJh70_so5bRR3vMcf-04Zmca6fJ67WdFMz0hsKJCYuzU_yHi1_52uXM1jR_8Yzuy-HImvrHL1VDCLdT5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
در تجمعات شبانه:
عراقچی حیا کن
امریکارو رها کن
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66026" target="_blank">📅 21:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66025">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
⭕️
🚬
🚬
فرهنگستان زبان فارسی: از این به بعد بجای کلمه هدفون باید بگید گوشینه
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66025" target="_blank">📅 21:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66024">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGGcIsMC4Czxym0SWdp1i7MrxByKWdl8urfgJltQzwmKYwYNT3VeBVP1Gnm0bsoj6UhZumKQndYnvBnBBDRguy7q1O2vZ0rPRk9UY0w8ukAEhLKIwjrGRVryjhq8cSJ3YcHVqi8Ms4gsipS2hIpEYUxBU5SooBKNLGhNd4zj1hamcruIkeIzQpjshW--4UsO5VYXX9cD7OUEdjd4j_y5VP4mWrAKQKIQ2_m6Dw--j6yC6LbePbtGI4MNiMcV-umCwM3e72EvGrT5mLPoibi4neSiN9TkvqGcLypbbM-OnCdfuS0Ez__fJ2lJmV6EWkgSZ3CKDmJPYbVK9q5E_mKHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
⚠️
سردبیر مشرق: رهبری در کدام پیام ده شرط را اعلام کردند؟
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66024" target="_blank">📅 21:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66021">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71f300a74.mp4?token=CZrOdh9YOy_U5t0fXrrRl3-FMPXElMj6UWDxL2I1ExMH_A0GwetpgVQEFt5XwnxhNYi7HZgl85cLH2WtReGdHJLLP0Njsg4l15k8naZjX4XW63qj0rSU9f9BOihNZbhXIHVskrbLOBlzcCfYNSW5l1JJEYTY5elCAs17_pjspKFplcRMzeyoq4bLpzEEGX1qGY0Nl7E1lWXVu3hWv88rX2YUp23iSzLRop5hbxKcr3jfcsJUXIa6DirjT1zdsp6V3Qkdr7AbEfNDgs0nj4FbcoUkvI2MhPcw56k9oRnDOIdLIYyI7n4XzQKK9VELdKOsoVRCHbK2eFdsjP0ZtdTEOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71f300a74.mp4?token=CZrOdh9YOy_U5t0fXrrRl3-FMPXElMj6UWDxL2I1ExMH_A0GwetpgVQEFt5XwnxhNYi7HZgl85cLH2WtReGdHJLLP0Njsg4l15k8naZjX4XW63qj0rSU9f9BOihNZbhXIHVskrbLOBlzcCfYNSW5l1JJEYTY5elCAs17_pjspKFplcRMzeyoq4bLpzEEGX1qGY0Nl7E1lWXVu3hWv88rX2YUp23iSzLRop5hbxKcr3jfcsJUXIa6DirjT1zdsp6V3Qkdr7AbEfNDgs0nj4FbcoUkvI2MhPcw56k9oRnDOIdLIYyI7n4XzQKK9VELdKOsoVRCHbK2eFdsjP0ZtdTEOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربا با ماشینایی که تو ایران شده هرکدوم۱۵/۱۰میلیارد و شده حسرت برا مردم از این کارا میکنن واسه سرگرمی...
💔
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66021" target="_blank">📅 21:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66020">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66020" target="_blank">📅 20:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66019">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری؛ ترامپ: فردا توافق با ایران امضا می‌شود  توافق باراک حسین اوباما با ایران، برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود، که ایران شش سال پیش به آن دست می‌یافت و مدت‌ها پیش از این از آن استفاده می‌کرد. توافق من با ایران دقیقاً برعکس…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66019" target="_blank">📅 20:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66018">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nkcfsqb9FzNQ1SpVQbV1bAbXMWJ7GdhzXIm8Zx40CRllVkbhCX6pkjLpyg4wfhwqr4qKRD5mdeUjJQcQTkeVkVC4gE0bv0GVyptHU6YmdP0If-2lHLbZi6OHHmbVtDsUgS6B-eClMli7J_8hgIOZar-eBwh_xZYQfYjKMQy9j1q9mYMkreBrBmgwnzMB6RPAoP37vI9v4DQSSkWSN-38WdGKOqdoLCRUX_Cyv4CCmngvrMJq759X5Otce1F36KoaFmsJUi7LlUB9EOyuDPqepPWCkZyJF_WjZbCeA7lVpuvsBJ6eB7okUqwJT9QMSjpgAP4AWT_DHIkBkEbGQlD-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
؛ ترامپ: فردا توافق با ایران امضا می‌شود
توافق باراک حسین اوباما با ایران، برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود، که ایران شش سال پیش به آن دست می‌یافت و مدت‌ها پیش از این از آن استفاده می‌کرد.
توافق من با ایران دقیقاً برعکس است، دیواری برای نداشتن سلاح هسته‌ای! در واقع، آنها دیگر سلاح هسته‌ای نمی‌خواهند و نخواهند داشت، چه از طریق خرید، توسعه یا هر نوع دیگری از تدارکات. قرار است این توافق فردا امضا شود و بلافاصله پس از امضای آن، تنگه هرمز به روی همه باز خواهد بود. رابطه ما با ایران بسیار متفاوت و بهتر از روابط دولت‌های قبلی است. برخلاف صدها میلیارد دلار پرداخت اوباما به آنها، از جمله ۱.۷ میلیارد دلار پول نقد سبز و سرد، هیچ پولی رد و بدل نخواهد شد. در زمان مناسب، وقتی همه چیز آرام است، ما به لطف بمب‌افکن‌های زیبای B-2 و خلبانان درخشان آنها، وارد عمل می‌شویم و گرد و غبار هسته‌ای را که در اعماق کوه‌های گرانیتی قدرتمند و غرق شده دفن شده است، جمع‌آوری و نابود می‌کنیم، چه در ایران و چه در ایالات متحده.  ما مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در آینده‌ای طولانی هستیم. امیدواریم که این روند به سرعت، به راحتی و به راحتی پیش برود. اگر این اتفاق نیفتد، ما یک جایگزین نهایی داریم که امیدواریم دیگر هرگز مورد استفاده قرار نگیرد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66018" target="_blank">📅 20:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66017">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b00aed34f.mp4?token=DQuo0Z0RLqr886_M4VS8Za_-Vj5UHD1MTvBsczrpQv30UCqjhapenxcWuASP9Q016yMwNTEbJHv726CBr_KBdkWLnCp4JHct8jjDP-o2G27n8bq0gCJjRSxSv5N1rAytVJBkr7JHCpBzU07JpvGZ0AMeUhsRXo63OuqOhFW0V0v5Q9crgdLVtxTKRuilHrcO0aaTa-QuzbQY6qHQ0tqt_jshFSBoE9bPym9GIUM08FO0NR80CXY8v85IlRvU9JRvQurWHW3fmDgF6wK0T0TYPvzuuo4321ELeww9OIBMK1WMuzIJQeS3v54y3pgNfQWe8m4o8q4DLAyXrnrMptU6oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b00aed34f.mp4?token=DQuo0Z0RLqr886_M4VS8Za_-Vj5UHD1MTvBsczrpQv30UCqjhapenxcWuASP9Q016yMwNTEbJHv726CBr_KBdkWLnCp4JHct8jjDP-o2G27n8bq0gCJjRSxSv5N1rAytVJBkr7JHCpBzU07JpvGZ0AMeUhsRXo63OuqOhFW0V0v5Q9crgdLVtxTKRuilHrcO0aaTa-QuzbQY6qHQ0tqt_jshFSBoE9bPym9GIUM08FO0NR80CXY8v85IlRvU9JRvQurWHW3fmDgF6wK0T0TYPvzuuo4321ELeww9OIBMK1WMuzIJQeS3v54y3pgNfQWe8m4o8q4DLAyXrnrMptU6oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
تجمع هواداران جمهوری اسلامی مقابل وزارت امور خارجه: مرگ بر عراقچی بیشرف نفوذی!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66017" target="_blank">📅 20:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66014">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4e2f8eb4.mp4?token=aUBWDzr25th-PKiSZBhkupHzx4bqJTUtCNYo7YPeNO8XTzuwv3dApL9JociczYADq3MkQipUSfCY09kWqHKEQ2z6IxazwcH5NFba5VPO8xey7f-bHHtUccP1ZXIVVSlgZXgO6K70ftzH9HI-KPnCDxLt3fJW8Zt-f64C_SQD-zP3SeIb2nLGvfSIl357rgAtg82LlGbN7DRLQB2tQ-mXgaqwsNCqmuD5MYdkkDSCp5Y_h2rrYBA_QnvHZR4hltYaoyrWkgSOOqSLyVNwAp6VUUc0VBXF-IPQ18sLDXU6BAjT4P9RcsQMqfppO4B4HWZtdipGxz-dYLOOL5f5S9LyCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4e2f8eb4.mp4?token=aUBWDzr25th-PKiSZBhkupHzx4bqJTUtCNYo7YPeNO8XTzuwv3dApL9JociczYADq3MkQipUSfCY09kWqHKEQ2z6IxazwcH5NFba5VPO8xey7f-bHHtUccP1ZXIVVSlgZXgO6K70ftzH9HI-KPnCDxLt3fJW8Zt-f64C_SQD-zP3SeIb2nLGvfSIl357rgAtg82LlGbN7DRLQB2tQ-mXgaqwsNCqmuD5MYdkkDSCp5Y_h2rrYBA_QnvHZR4hltYaoyrWkgSOOqSLyVNwAp6VUUc0VBXF-IPQ18sLDXU6BAjT4P9RcsQMqfppO4B4HWZtdipGxz-dYLOOL5f5S9LyCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی وایرال شده از کیوماسا، گوریل باغ‌وحش ژاپن بعد از دعوا با دوس‌دخترش
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66014" target="_blank">📅 19:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66013">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOE3Zj7koKn2YuPbp4-0To2KA4Zx2ZWcFsnNQqQYw6fOI22kmk_RDd3lFCLdtWYB_SvbeObkEerVmhlkqO8imG-k0RFwbZKr-9UUp-I7hMhnNuPWG-4N_b2NAjUnaUjk7MDttg-q1ZJ4xVkkE0Y4op0iXaHeHf6zc2kb02z7uGPxbkEuUAN_XXwQ-mJWqkO7kfJtqGMQHuK2UmcLKkv-IN5rdFafQ2KDmGveWv06f2irs1VPssgKg5zI4pX9bdzkOUzyO-oMtr6pBS10Ns8FgC9VdgnEWKV7pIHgbbdKdMYSs9DbB3AANNj2TkSpkP1zpy_YEZDcqXP01w88RqXTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید به نقل از یک مقام آمریکایی:
پرزیدنت ترامپ روز سه‌شنبه در حاشیه اجلاس گروه هفت، دیدارهای دوجانبه جداگانه‌ای با رهبران قطر، امارات و مصر خواهد داشت. نتانیاهو در این نشست شرکت نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66013" target="_blank">📅 19:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66012">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrQ9__UZTOhVG_YZBxfFn71H6Jad9U-TOhBOh-IzhdFqKXnLabISdI5E_kqJoD78A4DpwFYNF_lpYi8fTQtOhYwvus-LqC528EbGMChxSXgTAXAoDNxr4L7mOptbcsAj4UyA9awvo5cdXKd4Kd3hXWLp59H0l6jaLnaIuZMaHZAoWbQLv_7yJ2QN3qF1ne5jjC85F2XPDgTZauX0SjGuPQ4H1jl77tUISH4IpTeBn-NKB9PMQ2uR6ylAHz9fqB7PGczq3DVs2vt5LT8KM2m-TR2feiHnTM2dMTdIcEHEMgzv2ROj-P-3CzzZQ7gPnQlGBsC1iy2qK7EB4YgIUo4E4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تجمع اعتراضی مردم تبریز به دلیل توافق با قاتل خامنه ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66012" target="_blank">📅 18:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66011">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
#فوری
؛پاکستان:
توافق آمریکا و ایران فردا بصورت الکترونیکی امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66011" target="_blank">📅 18:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66010">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu_MLLMnUSN6vrdaBq7rHetOTkKJwyTUoPKx5KKEWg_MiMptx8gvyxGF2XSO1mpX9V3gYJFsVyeuNBWhxO6K3q-uXSTAfgXlHF_ddxrBRJtzJiXtZjqcmhbDPGUWQaDIqiAvorZrRWvvSgaw__cu_csqFGT7JzXtPGEKI8MMzYR1TmNOtuzSZFbekO9MqfKA2AJUY1MfT5gwnTJIScodlsV6V9bqMIEBaNKgVvtJG_Pw2HP5Ez_XgF_5GmFsSIEAK-jqEOPzTEMLMapJzl6RMV5WPiUYVk0z1JQHUoOnocP0JfajIky9jLLXuCu6T89I2zqGKlOhzMoZRfvDwbW_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ توییت شهباز شریف نخست وزیر پاکستان درباره احتمال توافق تا ۲۴ ساعت آینده را در صفحه خود بازنشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66010" target="_blank">📅 17:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66006">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGMQJ59YoV7TiNvF99URdDNyKz0jjbduB-fVKlXNYyFRu6soLus7_QNy8ipLr5HqEQDv5trM49LrhRiUVUkGnweiyC8Wd65Q_cLuvXVXeS6hXyesWSpIAS9zbW4oWblGaAhqEBwDAnMUVvNL9xNk7BwI-fLAImmqb6mTbYwBI_IPricUPvrvRYjwitSl_PuAxhvK2JykjIQ0ZmVcjS-sMdLmJA8r4T3TXUSkkka4QbaeyF0Gv1UQppp9pwMMBeCaazgSFD85UzFA2P-Hln0kJrccCvXzLhgRYiAc9lxdntmQ36mEiaFxPSPsHhc5yeSJyJ32MXcGg5DeTYO1bVqAJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBIjDVcUlzP32aQN1c03ExqhMQY6GUHtW20ZKmFKp49bCMkSTTIqnUCObYze_QR-4_mCxjs42MLJ-i5swz2uyqy4icXx3rdq0jOZqjYQvRQeXDUEtY2DWcKLggISZjk7nTOYVOuXpGuhP41Dfb_IzmQtBk7vyB-Drjab6YiAUDhSUPECt-sKm942jq5HloM_GDIV_X3qi6UPSDZg5tqEF8GlQK_j63wmBZs6gVhdKBaycNH61s9LoOgVqxfD3jYHbq_l5qENSB_lH1ZzHuHOw9rLPvCBIpavqpx01wRq8B-gIkfCXZTdLcqgUXtBB1CaG_H_OXrQhNLkF_TbIlUt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDAZM2o52TuW7RIP_mQseUxJxnguUxnrUdhEvt695njw0lQ6v4zrD3ZklMMQ-VvLqhPjQzConYznvb2rtz6mWja9t8YpSauhTZpqREJfCXsS4HONsY2YEGPhMojqXOychPn5rmqfV92v2HoIhYBNwDmkZIiv-skX96W3T_M6H_RoTyxHN-4N_MJKkFwf_RJX6ahq1hGitERn9m9NQGPTvdCEE3SwRrRfw8A41HL2a9Nq732L_Pp5PShcRKaiFuiJhenasD0DA1RXCAE_WTywUJ0bNQYWMrmqCIlMgQOugJM4nkGRLzMhLZuXpX3xAP2xosiHOaSehAofn_7kD1Qf7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ey9t41BW7x0ylWzNkfZwhfjHu2d2yewNxi8URX6JXrnC82pd5ufH_VmRNGPGq4kI3Z0rguHdwGqPfF17zknE4gbkvFpJ1RQQ3TIsVSFUQYRCr0vWdEf4w_8lxbEWdLA-9bVzzG7RLce5e66MmKLHhe1-DrtbCvUI80TQNnhfTkWNM3d2Wl1qm_uRu5a62gFjCjFMJNrJgWQ9f92V7Q4-Xny95fAFt0CPh74oMdrnuX9vjGwJ2jzgvZ8kwmude3MGOdRJUGfscFwMgYtFtQKot4eotmIOHmF1Y_PjpQTyRSMFMopwIdb2b1EcuH5YH5ywu44KlKV85K55QbQ3YRnibA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جت‌های جنگنده نیروی دریایی ایالات متحده و هواپیماهای فرماندهی و کنترل آماده می‌شوند تا همزمان با عبور ناو هواپیمابر آبراهام لینکلن (CVN 72) از دریای عرب، از روی آن بلند شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66006" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66003">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usid1qDAHPQjEhVYNHJmf6KRLfDZIEXd3iDij6FOEvhxEtxLl46iFsa-IBXCsWy9L--J7S2V6HK6ji-QmNmcWg7Ry4PGfe_pWj7vGRO8EaEcUeLaUH7fKiWuplapc0j6R-FNLPLpJ0z0ZVYuT_MfELpLk8IjMADF4Q0Veg91nR2p5obowTPm2yzhjScrb-tB7OSOZZgSivWfFhOoIS235G9X8urp7lAwNt7d4EBfLvgQihRpbFNBhbkcPRi9wlYfuk9ZE-DEc9l2NkDeSqvXkGlBm58vxKzf_GMHOJ_XNbc7410ZI75SVfEwPHegF593zfGthQRpr9hswpVqXCeIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی از نمایندگان مجلس به همراه قشر تندرو امشب جلوی وزارت خارجه تجمع اعتراضی برگزار میکنن و به روند مذاکرات اعتراض میکنن‌
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66003" target="_blank">📅 17:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66002">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tex2TkL1cq-PpEXSNtCDKi3sZ2VR7nQtH-pdDvWWd2rWXjtqGDj8-V_b6O--rzgZDiI1gPs0z-T55AARwCqkvoq88Lp7_xrtHpuHc8GFijvTYe2NsE6sakjGdcYtEfcclWBq1j8Ucyfq_Y6Ij4v6mvsf7vIvDapifEDPmLK-98IIGaZLIFEw7RCkoavbZgKqaJf7IRMx45gR-go7VGhpOMvT5zdfO6MFEVB3tuGh69-sUawXHpA18OUGlUYYUinBoVw_Mwsot4dzek13uN2j39LZqabhr7dvgJhck_mhr9sthm0bLrjg2aF0AK2wY2hq2auXjp197brxWSVvZiHO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اواخر بهمن ماه پارسال، ترامپ مصاحبه شمخانی که گفته بود «اگه آمریکایی ها سر حرفاشون باشن میتونیم رابطه خوبی داشته باشیم» رو بازنشر کرد ولی هفته بعد کشتش ، حالا دیشب هم صحبت های عراقچی که گفته به «توافق نزدیکیم» رو بازنشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66002" target="_blank">📅 16:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66001">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b2c6552b.mp4?token=f-mmRiPMWrcn6FCvI9m4L3KZKMYr9yC3aQ684A9uiAhTAibQKeeIrUf0r20ElIraR7tYjCy7fD4DU_rUYILY-OPtYC4XP-tetJCV1E8dzh0H_x67-0ragYqJ1CsgXRcZH028SEUv5628wG2OzrdaN6zEj1V2DyYjLnCXoy7AyR75rB4Zs8y3koit7izIsHRCp3Bv29H2eA0lhqTMaqw924xJjGl9QsheYjkv1D-edOLzZrp7M3QBFLKqa3OrL0PvoDOTb1m9I9Y94A34slD6s0tfrf4lNCrf8PLkt9zp1q5QJnEdSHIoPVZj4FrCdVS1I5yC6aBCZscUC4iKArYTZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b2c6552b.mp4?token=f-mmRiPMWrcn6FCvI9m4L3KZKMYr9yC3aQ684A9uiAhTAibQKeeIrUf0r20ElIraR7tYjCy7fD4DU_rUYILY-OPtYC4XP-tetJCV1E8dzh0H_x67-0ragYqJ1CsgXRcZH028SEUv5628wG2OzrdaN6zEj1V2DyYjLnCXoy7AyR75rB4Zs8y3koit7izIsHRCp3Bv29H2eA0lhqTMaqw924xJjGl9QsheYjkv1D-edOLzZrp7M3QBFLKqa3OrL0PvoDOTb1m9I9Y94A34slD6s0tfrf4lNCrf8PLkt9zp1q5QJnEdSHIoPVZj4FrCdVS1I5yC6aBCZscUC4iKArYTZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه هدف قرار گرفتن راکت انداز Tos-1A روسی توسط پرتابه FPV اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66001" target="_blank">📅 15:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66000">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKTHfJL_sFm-45QopuJhp8Wsx-RZBrzsFzmUljmE6CjILWswUTciIsIWhyJX2YfwdYvtIAaJV7Nz7SNTNo_5UN_Fej_5U5PW5iyuDDCcyV5mA-p3ddsTnQFcc_dExaK2funbqhtD9smcjKcnUHgyoV5OT5JXReXfH-H5dTHkyltcVG766P4qvKZ1EjPJ43lfVGPyIxFw57AKcynfaA_z_btoyJQoO550dxATXyLsecjpKQTbMO3btP3h0ABh0H2j3hp4MbYCHX_bN0M9i7S8mwN7g03X8Iv0Q9XLgfE-gckYw1B8UnJbnLPew19YNwUQyRJiBtjfhoHCZ2BtR8UEIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقایقی قبل سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از حادثه‌ای در ۶ مایل دریایی شرق عمان دریافت کرده است.
گزارش شده است که یک نفتکش توسط یک پرتابه ناشناخته در دماغه بندر مورد اصابت قرار گرفته است.
خدمه در سلامت هستند و هیچ گونه آسیب زیست‌محیطی گزارش نشده است. نفتکش در حال حرکت به سمت بندر بعدی خود است.
@News_Hut
﻿</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66000" target="_blank">📅 14:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65999">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
من مطمئنم که توافق تاریخی بین واشنگتن و تهران، پایه و اساس صلح پایدار را بنا خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65999" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65998">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
مذاکرات فنی هفته آینده پس از امضای الکترونیکی توافق آمریکا و ایران برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65998" target="_blank">📅 14:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65997">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
پاکستان در حال آماده شدن برای امضای الکترونیکی توافقنامه صلح آمریکا و ایران ظرف ۲۴ ساعت است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65997" target="_blank">📅 14:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65996">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر پاکستان:
ایالات متحده و ایران بر سر چارچوبی برای یک توافق صلح که به ماه‌ها درگیری در خاورمیانه پایان می‌دهد، به توافق رسیده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65996" target="_blank">📅 14:46 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
