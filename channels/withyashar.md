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
<img src="https://cdn4.telesco.pe/file/vkr3Ud69VSP6xKDWzuSF8BHYM030NUsP3JES7G0OSEqP_Sp0JhE2YN1j_iApSkEgKn03aeoTRLowdy6S0bysCLXHJDHfeYaIHa4E86lATTKZm85cOh4vQO3uw2dfAkouGeMa8D2qJ5vrgAQN39zMjOl3eJq38YNfCje7HR4Gm6RFoiHXVPpklLJv4I9BNy7omAvIKCsOZfWRna_5NsUmCZTGqzPIu9s9PyjvJ6UyCZDwh0yb6f3z_b_qCJFdh6XbQ2SNaMYxR1So7pfAx5cF8qs8Kz-CDHSkV4cI1lJq8Ub4ZLlSW94B9ZPjUVr8JP-s9KJiecwa7f0nOXAyILtroQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 444K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-22001">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رسانه های رژیم
: نقاطی در بندرلنگه و جاسک در استان هرمزگان هدف حمله قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/withyashar/22001" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22000">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قشم رو دوباره زدن الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/22000" target="_blank">📅 22:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21999">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سیریک کلی کشته داده نیرو های که اطراف دکل بودن ترکش هم پریده اطراف
@WarRoom</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/withyashar/21999" target="_blank">📅 22:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21998">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">معاون امنیتی و انتظامی استاندار کرمان از اصابت یک پرتابه دشمن آمریکایی به محدوده خارج از باند فرودگاه جیرفت خبر داد.
@WarRoom
تو که راست میگی
🤡</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/withyashar/21998" target="_blank">📅 22:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21997">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فارس: منابع عراقی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/withyashar/21997" target="_blank">📅 22:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21996">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/21996" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21995">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAZSOl-wgGzh0eZJxqH8RtF8dv87XWxVxrbmrAIOsox8TNi3ksSjYqt8lKWIWxRL85aW50K0PS3teVs8CicWzslwFJ2xDH4hbC-kSBDSt-FkjmxvdBcBAk3BwNA6ciNiFAo3ELx5TZyHWAWl0YWjjcmJMHFgpDfGCrUJYl7ZIXQY6YD77EUKyIKfC8d0tqkf369YncO0sFZO8wfQJ6q0NXkzezhyzOnnBdFSfg186EW_WqkOvIgcaOGDu6rwhWf9msi1JKUkNTmBeTc1e5Aj3bWMkX5UtWZxJjaplhi3YDFyMTWxmzyr6QhZGkQ8x2fzYPTk9LNcJtmyiTUHuZpEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک موشک با دکل ساختمان وزارت اطلاعات سیریک برخورد کرد؛ شاهدان می‌گویند دکل متلاشی شده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/21995" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21994">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0159d75a.mp4?token=opY-tOg2enmoxbDy9hWXenVZkZovr_r8mk_V7mCqxJSNT1DUl50tO9XXKwliTHAHbwEvzzReY0pdmKkHrO_WqxEB6odVQCxTPlX_FOWT73FqBG3Sh0SHa-IjfeRNpaP9kd4D0fG70PCGSBCtxDAGuc7LCZ4-uIsv7gSvhgmPd4WVKUdgDr5ECsEGOIhpgK33rqP9KXjXxfM5l7JBWCRd1FIRGY0LngiFH8E1pntuFfv9NI_gRjnAhQZH5ITvdL7s8iy95F1Jv-izFqJj6VtfDI_049QSvoQVRswlYA99VqcUQo1B_p9Km22Y2-iC4jcJmu8txT5htAFGXhVFPnUn9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0159d75a.mp4?token=opY-tOg2enmoxbDy9hWXenVZkZovr_r8mk_V7mCqxJSNT1DUl50tO9XXKwliTHAHbwEvzzReY0pdmKkHrO_WqxEB6odVQCxTPlX_FOWT73FqBG3Sh0SHa-IjfeRNpaP9kd4D0fG70PCGSBCtxDAGuc7LCZ4-uIsv7gSvhgmPd4WVKUdgDr5ECsEGOIhpgK33rqP9KXjXxfM5l7JBWCRd1FIRGY0LngiFH8E1pntuFfv9NI_gRjnAhQZH5ITvdL7s8iy95F1Jv-izFqJj6VtfDI_049QSvoQVRswlYA99VqcUQo1B_p9Km22Y2-iC4jcJmu8txT5htAFGXhVFPnUn9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/21994" target="_blank">📅 22:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21993">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گزارش انفجار جدید در قشم/تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/21993" target="_blank">📅 22:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21992">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رسانه های رژیم : پهپاد شاهد در وکردیم
💨
🤡
😂
@WarRoom</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/21992" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21991">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اتاق جنگ با یاشار : حملات آمریکا همچنان ادامه دارد , فرودگاه جیرفت رو زدند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/21991" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21990">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e93ddf06.mp4?token=iOiTML9TeXNwfnpug8L66-b52-UGCo0DsimFHm-4kR5XNeAi1Kp_R-IodVvclAMyMBGjI6a7DHXyn5048lx8wl-w8b1eTsk1rEmcummpXCQmBTs_Xix7YB2_NZcq_0GAh1xeTGYBCkCoGMy49ECFRQqAWSIXNv0QN6EEl3z2F3u0Deq6uKCReFym5K8IsZBsl0qu0xzT70LicUgEDMisQbPcjY2aS2yjL3M4JLwnqXChCkUeLV6RHH52VgGR3xRDM7HAmb0Y8yr9S-MjOqUOpEzK6cjZzD5fMBgx_zaOz65KCw9m-3Gihv5lg1xcJr1uN2e9K7geUICvQb19vABzbDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e93ddf06.mp4?token=iOiTML9TeXNwfnpug8L66-b52-UGCo0DsimFHm-4kR5XNeAi1Kp_R-IodVvclAMyMBGjI6a7DHXyn5048lx8wl-w8b1eTsk1rEmcummpXCQmBTs_Xix7YB2_NZcq_0GAh1xeTGYBCkCoGMy49ECFRQqAWSIXNv0QN6EEl3z2F3u0Deq6uKCReFym5K8IsZBsl0qu0xzT70LicUgEDMisQbPcjY2aS2yjL3M4JLwnqXChCkUeLV6RHH52VgGR3xRDM7HAmb0Y8yr9S-MjOqUOpEzK6cjZzD5fMBgx_zaOz65KCw9m-3Gihv5lg1xcJr1uN2e9K7geUICvQb19vABzbDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : گزارش ها حاکی است امریکا امشب مکان های حساس جدیدی رو زده که شاید تا پایان این رژیم هم اعلام نشه ولی کار اساسی انجام شده ! @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/21990" target="_blank">📅 21:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21989">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش انفجار عسلویه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/21989" target="_blank">📅 21:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21988">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ به فاکس نیوز: آن‌ها سعی کردند رادارهایشان را بازسازی کنند، زیرا چیزی نمی‌توانستند ببینند. ما منتظر ماندیم تا این بازسازی تکمیل شود و مجدداً به آن‌ها ضربه زدیم
@WarRoom</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/21988" target="_blank">📅 21:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21987">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ به فاکس نیوز : ناو هواپیمابر USS George Washington به طور کامل با مهمات پر شده است.
@WarRoom
💥
💥
💥
💥</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/21987" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21986">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بمباران سیریک هم اکنون
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/21986" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21985">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ به فاکس نیوز: اگر ایران به حملات ما پاسخ دهد، موجودیتش از بین خواهد رفت
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/21985" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21984">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/21984" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21983">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f800b25bb.mp4?token=EEg9m72POBXpPufeJd4vkMr4Ci5WtP358rZxUuvTBiucsjspTtX8gSMkz_EUNRLWuupkXOzLoZjizMDEUxcdPwYTX15tyeMuVPV8KaD4kHwPh_NAqHdIvjzHXC6uY9Ipx7lpa2d6u8KUo4jqL73cP9F1wOYBQaLuqQhreCgMQvI76rXdGPS7slv7JjnktMbxfBW1oowVIJ_V1KYm2FwLk0j_aVvQu79E_I32_CTgdhIfptbiYsc1uMUDSGYME-R4AENgWwGpkZZn4CicbZKDeJ2z_fpzanGx0J16XmIp_R23TiSR7I0U5GBZ92ihqEdC4yhkztxP9FNL8qCG4-nWmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f800b25bb.mp4?token=EEg9m72POBXpPufeJd4vkMr4Ci5WtP358rZxUuvTBiucsjspTtX8gSMkz_EUNRLWuupkXOzLoZjizMDEUxcdPwYTX15tyeMuVPV8KaD4kHwPh_NAqHdIvjzHXC6uY9Ipx7lpa2d6u8KUo4jqL73cP9F1wOYBQaLuqQhreCgMQvI76rXdGPS7slv7JjnktMbxfBW1oowVIJ_V1KYm2FwLk0j_aVvQu79E_I32_CTgdhIfptbiYsc1uMUDSGYME-R4AENgWwGpkZZn4CicbZKDeJ2z_fpzanGx0J16XmIp_R23TiSR7I0U5GBZ92ihqEdC4yhkztxP9FNL8qCG4-nWmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از دیدبان اتاق جنگ از خمین
🚨
🚨
عراقی ها مردین بدزدین
😂
😂
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/21983" target="_blank">📅 21:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21982">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پهپاد های آمریکایی حضور قاطع دارن
💥</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/21982" target="_blank">📅 21:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21981">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">موشک خمین رو رو هوا رهگیری‌کردن زدن و سقوط کرد
😂
🚨
🚨
🚨
🚨
برگام
@WarRoom</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/21981" target="_blank">📅 21:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21980">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سه انفجار کوه گنو بندر عباس  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/21980" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21979">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش پرتاب موشک از خمین
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/21979" target="_blank">📅 21:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21978">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مقام آمریکایی: حملات آمریکا به ایران حدود دو ساعت است که ادامه دارد و بر زیرساخت‌های مورد استفاده برای هدف قرار دادن تنگه هرمز متمرکز است. واشنگتن انتظار واکنش ایران را دارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/21978" target="_blank">📅 21:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21977">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پیج دوم شاهزاده (دفتر شاهزاده) از دسترس خارج شد @WarRoom</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/21977" target="_blank">📅 21:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21976">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش انفجار عسلویه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/21976" target="_blank">📅 21:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اتاق جنگ با یاشار : گزارش ها حاکی است امریکا امشب مکان های حساس جدیدی رو زده که شاید تا پایان این رژیم هم اعلام نشه ولی کار اساسی انجام شده !
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/21975" target="_blank">📅 21:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21974">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e6376e3d.mp4?token=V3ofrjJ1nwzWSfhEx8xwUF2Qt8Xjd9C7MrE47Ub0sQXc3iP2RN5iSurowH6M807Xqxf3vqlSDHEf2tqPNFlR8v38VAT2QXUhcLH1SkY7ZwsE_Bupf-w61BTL7_GpHcQMM8tmXmpZLhtieG5UJM4onoZWpZ4rOcvwbQIjHnG80RCafsIU0rZhlxZEdT647U-B99FpyC2Cr6o8jksIzYm54O7IM-inUZyYhbD7koVUwjpdRpfCyAr7Us4IrypjtVeRB5l21vg-VdhQXpvl7iSyGYfRn8XRWzKn0bTwvF2Qx-kNrQUtH6ooL4BUUZU7V5c2ag3nT2j0XOUkxQLF8SYB3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e6376e3d.mp4?token=V3ofrjJ1nwzWSfhEx8xwUF2Qt8Xjd9C7MrE47Ub0sQXc3iP2RN5iSurowH6M807Xqxf3vqlSDHEf2tqPNFlR8v38VAT2QXUhcLH1SkY7ZwsE_Bupf-w61BTL7_GpHcQMM8tmXmpZLhtieG5UJM4onoZWpZ4rOcvwbQIjHnG80RCafsIU0rZhlxZEdT647U-B99FpyC2Cr6o8jksIzYm54O7IM-inUZyYhbD7koVUwjpdRpfCyAr7Us4IrypjtVeRB5l21vg-VdhQXpvl7iSyGYfRn8XRWzKn0bTwvF2Qx-kNrQUtH6ooL4BUUZU7V5c2ag3nT2j0XOUkxQLF8SYB3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سه انفجار کوه گنو بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/21974" target="_blank">📅 21:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21973">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش مردمی انفجار در فرودگاه قشم
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/21973" target="_blank">📅 21:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21972">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سپاه : مجازاتشان میکنیم
زاااارتتتتتتت
@WarRoom
😂</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/21972" target="_blank">📅 21:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21971">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رسانه های رژیم گزارش‌ها حاکی است در حملات آمریکا، یک کارخانه تن ماهی در قشم، یک اسکله ماهیگیری و یک سکوی اداره بندر در سیریک هدف قرار گرفتند.
@WarRoom
😂
ارواح عمه جان</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/21971" target="_blank">📅 21:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21970">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یه انفجار بزرگ دوباره در بندر عباس الان
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/21970" target="_blank">📅 21:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21969">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هم اکنون انفجار جدید در بندر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/21969" target="_blank">📅 21:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رسانه های رژیم : صدای انفجار در مشهد مربوط به ترکیدگی و آتش‌سوزی خط لوله گاز در جاده کنه بیست مشهد بوده؛ علت حادثه در دست بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/21968" target="_blank">📅 21:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjbQp99o6m_9hlpg9iTI1tZfge4cldhDM_BZdzoYXYFhuM-JWCn7oiuYlAScm5kvAGoJdhLbXzG6t2O9nrafCIYLfifJzyf9IRsE4Z-f3HoTf_Rdfa9FT0ECPGEf9Rutevio3a7oxgc4PiDu4nLUR1s6J9JKvpzNbAogcbpH9Y4TpJby7qZeVX14WopVcrZNx7bx36nNQB0m0-wIrPIg0bc9vny1lZSv0mJskg_UHnwxSMaHv6iaaCFy_MigLajSFsUjPck6m_odtreilz9BZhiLGmdA9B5-aMfVqINbhBFVZjjkFqssqLRljJkeDpz_5pYQj7886CuOCSjMEtQsDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده همین حالا در حال حمله به اهدافی در ایران، در نزدیکی تنگه هرمز است. این حملات گسترده و قدرتمند هستند و در واکنش به تلاش نافرجام ایرانی‌ها برای کار گذاشتن مین‌های دریایی در تنگه هرمز انجام می‌شوند؛ تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد، زیرا همه مین‌ها کاملاً جمع‌آوری یا منفجر شده‌اند! همچنین در واکنش به شلیک هشت موشک از سوی ایران به پایگاه نظامی ما در اردن که همه آنها با موفقیت رهگیری و سرنگون شدند. اگر کشور شکست‌خورده ایران در واکنش به این حمله کاملاً موجه دست به اقدام تلافی‌جویانه بزند، بار دیگر هدف حملاتی بسیار شدیدتر و در سطحی بالاتر قرار خواهد گرفت؛ اما این بزرگ‌ترین حمله از همه نخواهد بود. بزرگ‌ترین حمله همچنان در انتظار است و وقتی به پایان برسد، چیز بسیار اندکی از جمهوری اسلامی ایران باقی خواهد ماند!
@WarRoom</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/21967" target="_blank">📅 21:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLv50qGrb5sE5ad7ten94AqtnOtzFKQGPrTm-7Fnpuv2qsB0Ec40IyF7NvT9l0Py8tVNcdlZyCc4Xgh6TboTq9gmn8TrPvJO5lL0X0AWKw6aPoKsQqbRWQBDtlSmgXX5bYaZxEGo80IGYdzEH466zSgnu-urCR4R_KL1u-BsAXFn4QXfwGoWQHJfFZIEuYv-GmCzraofdbXGOQlhL9ViYxSo9CiQKn5qfT9MZ7HFAt02TjZh-sM-asWKn0NjOIfmoWESmeAzVxa1SM-sSWr-b3Sj9gi__-dWdOo-O1G_pWAM7R48a2KH-QRSY6e2Xczx13T8VC10URG2s_kIS-dwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود ناشی بعد از ۶ انفجار در محدوده/خود فرودگاه بندر عباس
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/21966" target="_blank">📅 20:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دو انفجار پشت هم هم اکنون در بندر عباس
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/21965" target="_blank">📅 20:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">باراک راوید اکسیوس : ترامپ و مشاورانش درحال بررسی طرح های حمله علیه ایران در تنگه هرمز بصورت بدون توقف هستند
@WarRoom</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/21964" target="_blank">📅 20:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21963">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مقام آمریکایی به آکسیوس از ادامه‌دار بودن حملات آمریکا به ایران خبر داد
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/21963" target="_blank">📅 20:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21962">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تایید اصابت ۴ پرتابه در چابهار و کنارک
معاون امنیتی و انتظامی استاندار سیستان و بلوچستان از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21962" target="_blank">📅 20:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سپاه : موشک در وکردیم
@WarRoom
😁</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21961" target="_blank">📅 20:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/21960" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دایرکت هنگ کرده یه رخست بدید ۱۲۰۰ تا پیغام تو ۱۰ دقیقه لود نمیشه ! خواهش میکنم یه بیت رهبری برید
😂</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/21959" target="_blank">📅 20:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjdr_WlJKhgALOXFf-iRAzjSHEVwLm6jVyAY6pKmTZwgSgf5i0MtOMSTDSqRRNjpfrb7Be37Pus0sLxM1fIlC7-K8mrvbySsg1FldQ-s5mcoQIo2uBYbphMgLoeT0XncryAgwXkkeeTj5RTcxDypQWRF7Kkidhtit87ZjZuE598pLxgDudih1A7Lxy5hYl-cJKsjiu7y1xb24_vJ-vyJuxrKYlGjRFNZMsoZcK-_2R5LKTfZXh9OOXzS-XnwQLaZ_wa2766fE_LhSw_UvheczQOgJGSj_wKhDxqF1nteiVs7vba7bcfenxW_lYkPQjUibAmKLX83sXgjDhW-GxgBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بنتلی با بدنه کامل فرج کربن
😁
یکی از ۶ تا ماشینام</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21958" target="_blank">📅 20:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/21957" target="_blank">📅 20:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">موج جدید حملات شروع شده سوم یا چهارم میشه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/21956" target="_blank">📅 20:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دکل سیریک رو برای بار۴۶۸۰۰۰ ام زدند
🕯️
🖤
💔
😂
🥹
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/21955" target="_blank">📅 20:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21954">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارش انفجار جدید بندر عباس
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/21954" target="_blank">📅 20:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21953">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دایرک بیجا نفرستید ای مشرکین
😂
، فدای سر کل بچه های گروه که تو صدای انفجار قشم یا هر جای دیگرو نشنیدی می خواستی بشنوی لطفا درک و فهم داشته باشید با اونای‌که این گونه پیغام هارو میدن هستم ، اینا گزارش فوری مردمی هست من که اونجا نیستم !</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21953" target="_blank">📅 20:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21952">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صدا و سیما : صدای انفجار در بندر جاسک و شهرستان میناب در استان هرمزگان شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21952" target="_blank">📅 20:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21951">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فاکس نیوز: نیروهای آمریکایی در حال حاضر در جنوب غربی ایران در حال حمله هستند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21951" target="_blank">📅 20:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21950">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مقام امریکایی : حملات آمریکا به ایران تاکنون با ترکیبی از جنگنده‌ها، پهپادها و موشک‌های کروز تاماهاوک انجام شده است
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21950" target="_blank">📅 20:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21949">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش انفجار در بندر کنگان
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21949" target="_blank">📅 20:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21948">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ناو لینکلن در میدان کلارک کرج دیده شد
@WarRoom
😁
😂
🚨
👀</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21948" target="_blank">📅 20:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21947">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش‌های مردمی از بحرین حاکی از آن است که موشک‌های زمین به زمین، احتمالاً HIMARS یا ATACMS، از بحرین هم اکنون شلیک شده‌اند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21947" target="_blank">📅 20:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21946">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سنتکام:
امروز، سه‌شنبه ۱۰ شهریور ۱۴۰۵، ساعت ۱۹:۳۰ به وقت ایران، نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات در پی تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و همچنین نیروهای نظامی آمریکایی مستقر در منطقه انجام شده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21946" target="_blank">📅 20:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21945">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دلار ۲۱۵،۵۰۰ سقف تاریخی
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21945" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21944">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFsEniUVZPtcpMfefL_rH0hw6zBVj1bQlBSBMjqluBqNMe_VULqQHXNt5VqaAg1Ju3s7VGQNQ2Jusz7S6io_VPBURtjC9A1gaLUVlk_CS-xUgC7pDS72GRFSqXGuciHfZi5xfHstR9Nq4wpYvdUVnoi5tJkEo-R7CsUzkSlmY6wVCirrJfnLBOsFsHWggHEGigp2ZJOMjLJ_Z2cKAAcdF_JOEbOMKzCMdletQArQ5GrA6jWNqqZXDV3EVKmN87NXUOnKpzJ-6CjO12Pz1IsbkFpV9e2Rj2Kb1I5s8xnpKPd-OdLfHDLyF7DlO37purHECfsXuPV8emk-d3D7j82DwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاطی که تا الان گزارش انفجار دریافت کردم
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21944" target="_blank">📅 20:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21943">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">العربیه: آمریکا تا الان حمله به بندرعباس رو تایید کرده
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21943" target="_blank">📅 20:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21942">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">باراک راوید ‏آکسیوس: هشدارهای امنیتی در چندین پایگاه نظامی ایالات متحده در سراسر خاورمیانه صادر شده است، به منظور آمادگی برای یک تلافی احتمالی از سوی ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21942" target="_blank">📅 19:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21941">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رسانه‌های دولتی رژیم وقوع
انفجارهایی در مناطق جنوبی ایران
را تأیید کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21941" target="_blank">📅 19:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارش انفجار جم بوشهر
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21940" target="_blank">📅 19:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">زارتان زورتاااااان ملت ما آزاد میشه
🫱🏼‍🫲🏽
🙌🏾
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21939" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هم اکنون منطقه دقیقا مانند قبل جنگ ۴۰ روزه شلوغ شده پهپاد و سوخترسان زیاد! @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21938" target="_blank">📅 19:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش رگباری مردم از شنیده شدن صدای انفجار در اطراف‌ بندر عباس @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/21937" target="_blank">📅 19:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بندر عباس رو سنگین دارن میزنند
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/21936" target="_blank">📅 19:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سنتکام: به دستور رئیس جمهور دور جدیدی از حملات به ایران آغاز شد
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21935" target="_blank">📅 19:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کنارک در همین لحظه چنتا سنگین
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21934" target="_blank">📅 19:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جنگ ایالات متحده جنوب و ایالات متحده امریکا شروع شد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/21933" target="_blank">📅 19:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارش انفجار در کنارک و سیریک
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/21932" target="_blank">📅 19:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قشم رو سنگین میزنند
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/21931" target="_blank">📅 19:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گزارش انفجار در جاسک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/21930" target="_blank">📅 19:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">از قشم و چابهار هم گزارش انفجار دارممم چه خبره
🤯
🤯
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/21929" target="_blank">📅 19:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">باز هم صدای انفجار در بندر عباس
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/21928" target="_blank">📅 19:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش رگباری مردم از شنیده شدن صدای انفجار در اطراف‌ بندر عباس
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21927" target="_blank">📅 19:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21925">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92ad1d93de.mp4?token=Reb4hQmaC40w0Azw2IfxiSfQIq4YrZzeEIKix-VqaujnXm9R65JEwDIhAN-6JPRN07QNfneEEJx0i6l_Xf5AfXIros4heXBwFpQ_d6FdPothV_9BPXsuYtkCgw6QGJbYoBzlOsqCFUEgLwZd3wfQutUwj12V1HGz-WZI8DNyDlWqrtRGboF76aHP2vHVolzVZBx0001U6K1vRC6OxGVq2kFkhhoAgIL8nuxmcEmXDweOtxKT89P7wX1JVmnQnScxpDVZx-FhreSe3ZINdZbHzgiRpFqO4v-jRERX0VMSMogGfw6ddnt1ZnGk1ZlHL_4NZ6wrIm-3xPAUe3EAobXoCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92ad1d93de.mp4?token=Reb4hQmaC40w0Azw2IfxiSfQIq4YrZzeEIKix-VqaujnXm9R65JEwDIhAN-6JPRN07QNfneEEJx0i6l_Xf5AfXIros4heXBwFpQ_d6FdPothV_9BPXsuYtkCgw6QGJbYoBzlOsqCFUEgLwZd3wfQutUwj12V1HGz-WZI8DNyDlWqrtRGboF76aHP2vHVolzVZBx0001U6K1vRC6OxGVq2kFkhhoAgIL8nuxmcEmXDweOtxKT89P7wX1JVmnQnScxpDVZx-FhreSe3ZINdZbHzgiRpFqO4v-jRERX0VMSMogGfw6ddnt1ZnGk1ZlHL_4NZ6wrIm-3xPAUe3EAobXoCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز فرماندهی مرکزی آمریکا(سنتکام) اعلام کرد که ۸۴ کشتی تجاری را به مسیر دیگری هدایت کرده، سه کشتی را غیرفعال کرده و دو کشتی را بازرسی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21925" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21924">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بسنت گفت : «احتمالاً این هفته در چارچوب کارزار اقتصادی خود علیه ایران تحریم یک بانک را اعلام خواهیم کرد و هفته بعد نیز یک مورد دیگر را اعلام می‌کنیم. ما در حال گفت‌وگو با متحدان خود هستیم؛ همه آنها جلو آمده‌اند و حمایت بسیار خوبی از ما نشان داده‌اند.»
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/21924" target="_blank">📅 18:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21923">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که با انجام عملیاتی فریب در غزه، معین محمد عرابید، رئیس دستگاه امنیت عمومی حماس در غزه که مدت زیادی به دنبالیش بودند را زنده گیری و  بازداشت کرده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21923" target="_blank">📅 18:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21922">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نائب‌رئیس مجلس: باید محاصره آمریکا رو محاصره کنیم
@WarRoom
🥴</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21922" target="_blank">📅 18:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21921">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbQpaDSpa2oZk3hHUQoE_yWxG7xaS79zu3TPOsidqKSTnCz-eDkpA3FpcVKWNJ7vzQGHvDKVyKxtyyuX10Uukoccp4a6bMG74m7UMB24VS8rHfPfwiRWuknxx3bqCtQ4SxDteoBhXHzf-VO89nH98y3Wn2SWoUAG7V6g1at85tuVFddbYIjFE-Kq9Cp0-CR4Y8kR7LTlB7VW09xDt0Z-u1k4R03C9v3PXZ6u3PF8KHSEUBNjsD9e1igoXKqEw3W4tZIndNcdjjL9HI1r2t2UWWnzkxeNzHRGPXQS8iDxEIEUkqWjkwDNFoQ3u83ql8AKWLmoDBQ94N-oriqtbt0Aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط ببین کار این حکومت به کجا رسیده؛ به هوادار خودش هم رحم نمی‌کنه! از بس زیر فشار و تحریم به خاک سیاه نشسته، با اسم رهبر مرده‌شون هم از جیب همین عرزشی‌ها پول درمیارن. طرف هنوز نفهمیده چی شده، اینا دارن جیب خودش رو می‌زنن
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21921" target="_blank">📅 17:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21920">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نتانیاهو: راهبران ایرانی می‌خواهند من در انتخابات شکست بخورم؛ و حزب‌الله و حماس نیز همین را می‌خواهند؛ و ترکیه، البته، همینطور. آن‌ها این را صریحاً می‌گویند. از خودتان صادقانه بپرسید: چه کسانی می‌خواهند در این انتخابات پیروز شوند؟ من می‌توانم به شما بگویم، آن‌ها نمی‌خواهند من پیروز شوم.
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/21920" target="_blank">📅 17:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21919">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/21919" target="_blank">📅 17:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21918">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یک هم میهن زد نامجو رو تا شیشه جمع کرد @WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/21918" target="_blank">📅 17:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21917">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba29001cd.mp4?token=qBVAVOaeoLGjnpeNbxUcg5O9wJrXVEZLsPLsA3x7iqIjwygR_swS5mK4xLz4LNNIzkweXneEt05oUz9uMSrw9aLfvHpgcj9CTjzZxXBkxDt5yoUlXEeTR-8H1zUUscn3AYfCSgSQVFbxI7ktJBCttx84V8raHi0nZFaMvYpv79bnxjtXbkdFERmmveMtZSJaPkm5xSEkWo93WrVxuV9mP9OX9uDaDKmsfTsWrTmaOb4emVwJONx3aGh_ehLmiy-SYVo4ZjfMpq2DZl0_wUCRt5UMpL9r64Y_A-t2J7PbgBxCusrleq6lwxCNQSx0OsFprV0tZanHa2U4HXIx0iARPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba29001cd.mp4?token=qBVAVOaeoLGjnpeNbxUcg5O9wJrXVEZLsPLsA3x7iqIjwygR_swS5mK4xLz4LNNIzkweXneEt05oUz9uMSrw9aLfvHpgcj9CTjzZxXBkxDt5yoUlXEeTR-8H1zUUscn3AYfCSgSQVFbxI7ktJBCttx84V8raHi0nZFaMvYpv79bnxjtXbkdFERmmveMtZSJaPkm5xSEkWo93WrVxuV9mP9OX9uDaDKmsfTsWrTmaOb4emVwJONx3aGh_ehLmiy-SYVo4ZjfMpq2DZl0_wUCRt5UMpL9r64Y_A-t2J7PbgBxCusrleq6lwxCNQSx0OsFprV0tZanHa2U4HXIx0iARPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هم میهن زد نامجو رو تا شیشه جمع کرد
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21917" target="_blank">📅 17:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21916">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نرخ دلار ۲۱۴،۴۰۰ تومان(سقف تاریخی)
دلار کف بازار ۲۱۹-۲۱۶ هزار تومان
تتر ۲۱۱،۶۰۰ تومان (سقف تاریخی)
بیتکوین ۷۷،۸۳۹ $
انس جهانی طلا ۴،۳۵۲ $(آخرین قیمت)
نفت برنت  ۹۲.۷۲$
@WarRoom
۵ عصر تهران</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/21916" target="_blank">📅 17:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21915">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skgVsUSdLjAwjxjjKihOS5e4HPBd4zmqCuYnF_wxM8e2bY58gzjsDMVv4EEqE8wAvQJ0buSflPIBY5Oi_8LYZLRjb3dUUqatp_pbdlsj8i80hjZFZ2cueJnQZx1FNkrm2-mf1rI6ijkWeXh8OsxJHRiTdUzncbgynhYM-ZLTZ6PrZyr3tqNAsZey7yRPvGwFyClc67Qz2yDtWLlyVcRZUxklevFWJqDSfivlBuxi1LugEBB4u-RyDojahHJzixLd0urlXkyKXeOMJeSfLScp0H5hyNqhKPLFveLGiqI9QCq3vSD8J9HmF3nNrXDUIdOT4kwOa3DDWmWSgpA61tfVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون منطقه دقیقا مانند قبل جنگ ۴۰ روزه شلوغ شده پهپاد و سوخترسان زیاد!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21915" target="_blank">📅 16:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21913">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4002634599.mp4?token=H57setBkaT1SlNb8twkgeZm3Y822OX0PKV21PKtM77wXtwEDecXs8t7TwbdJ9zZyPqDFzfbKbE-_5WWmPA0-b0uwvF1dRtN4m232UDwj32_Qv1Bf_6FK27uZMoVs4P6qJdowt_8G1cOpLvMUz0qutWn3grNRsvxEOkewfm1CLkqTc_o3hSCT7RR4x4lvvwkXNt4q8FtcEloFC2R70TmTMao53w6rDmny97ttPmr_hN1TYyJuH3JrvBiivgkROgiJnmKujBPc9zne-t3tzxEyZLdP0ITZYjs1p8gnVIp3_PKL3sob0akZ74LZE6nsbDRiX8RyRB7kjcKPPaO7NAKNfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4002634599.mp4?token=H57setBkaT1SlNb8twkgeZm3Y822OX0PKV21PKtM77wXtwEDecXs8t7TwbdJ9zZyPqDFzfbKbE-_5WWmPA0-b0uwvF1dRtN4m232UDwj32_Qv1Bf_6FK27uZMoVs4P6qJdowt_8G1cOpLvMUz0qutWn3grNRsvxEOkewfm1CLkqTc_o3hSCT7RR4x4lvvwkXNt4q8FtcEloFC2R70TmTMao53w6rDmny97ttPmr_hN1TYyJuH3JrvBiivgkROgiJnmKujBPc9zne-t3tzxEyZLdP0ITZYjs1p8gnVIp3_PKL3sob0akZ74LZE6nsbDRiX8RyRB7kjcKPPaO7NAKNfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقال دست‌کم ۱۵ دستگاه تانک و خودروی زرهی با استفاده از کشنده‌های تریلی در شهرستان بمپور , بر اساس مشاهدات موجود، این تجهیزات زرهی در مسیر ایرانشهر به سمت چابهار در حال انتقال بوده‌اند.
‏این انتقال در حالی صورت گرفته که پیشتر نیز گزارش‌هایی از انتقال تجهیزات زرهی به سمت چابهار منتشر شده بود. بر اساس تصاویر و گزارش‌های پیشین، دست‌کم هشت دستگاه تانک و خودروی زرهی نیز در مقطعی از زاهدان به سمت چابهار منتقل شده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21913" target="_blank">📅 16:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21912">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حتما. اگه از طریق تلگرام با من آشنا شدید حتما پیج اینستاگرام رو هم فالو داشته باشید. یک سری مطالب فقط مخصوص اینستاگرام است و یک سری مطالب فقط اینجا مخصوص تلگرام.
instagram.com/Yashar
(پیج اصلی)
instagram.com/YasharMotors
(پیج پشتیبان)</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21912" target="_blank">📅 15:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21911">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXmsU7pi3fiSpX3jjmAVlf1lph8llo980xuKdDc_-uHNYJ2fY-GzoFebv1xYA-j6YLjedFQpScL1S6hM4wR3dhu1pGveAgGrrsgWaJTlfGGkyf4FdCv6kce8lKOEESharNhF6kKpEdvGyi36oo-OFPMI1DGzpW-DPhP1-OwiFrPJZJISJPSdLupyYec7G3oibjW68pAhdKiFt-Am41Rafq4eC4vVoGdXNnbeMe4mKiNeBGBEj366dvhS1bTX216V01-R22N2x7Y3gtuhMjSDMrJfNynlCuF1XVeinsvOPDCF5AE020gTBiz3uDfcMLKevn6acZOxy4lrn87X-wa2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار پزشکیان و  پوتین در حاشیه اجلاس سازمان همکاری شانگهای
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21911" target="_blank">📅 15:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21910">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501b5e7e6b.mp4?token=GbCsw1EMbZ8qbNjWvjq6wSaHwhM0eTTMEiWuuUKWbn-ehM82qREKhHknJRXWH44nWohrcjOrwvYu8jh8Lx0yKmk2CN0FGCewtVlNvUL4tOgqoZyv3Z2MOPIBrjVsm_gniEPoW7tBvboUg32P7SLMNCyWmbe5fok4a_KKqyNTw2klUWNJRlaTdBVNsiwc258yCutcelIC5VYQqRIPVAkZUvqYC-Qu1jHwO4gXJIxnJf8d-SBx1azPYQ2nhAC0uN2kOlrj-rFhJQzoF6bC6LDtd75Za4sVAWklXs9ya2NgQD4OKO-m_1tbpooaHNXRRmiv3w7RTQA0dL2bapFKa8OXUqCxJBioCiYxzRJ3ZtNsoVQ5OO2zVlU6EPsxYg0wb-BCmn9U_MBBUBgYKqXvOwlbddHPJAv80YRSitoYcqzaxCEuTghuBFQe8yEUYR4uGobQkVDT_RISsDchSdmvsaZl5pkFQSGHqv6Y7L5pJ6M2k_F04RKnlEHrX4xqSQOGreEnuz8MTKxnyvx3XEanRHzhxGGUpvnrXnTsIeLTR_vOnj7gPXACOQml2n5T9G5sXw4vpuyJr97F6VBYCE8TOXzMMGzq7vNz17qRTgHpTNK6zhPge83M9BzEFBvv2_KJhPXdjiHM8xR8TjDgi5-KV3ANSbhV4jpcXsg695we-TMh-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501b5e7e6b.mp4?token=GbCsw1EMbZ8qbNjWvjq6wSaHwhM0eTTMEiWuuUKWbn-ehM82qREKhHknJRXWH44nWohrcjOrwvYu8jh8Lx0yKmk2CN0FGCewtVlNvUL4tOgqoZyv3Z2MOPIBrjVsm_gniEPoW7tBvboUg32P7SLMNCyWmbe5fok4a_KKqyNTw2klUWNJRlaTdBVNsiwc258yCutcelIC5VYQqRIPVAkZUvqYC-Qu1jHwO4gXJIxnJf8d-SBx1azPYQ2nhAC0uN2kOlrj-rFhJQzoF6bC6LDtd75Za4sVAWklXs9ya2NgQD4OKO-m_1tbpooaHNXRRmiv3w7RTQA0dL2bapFKa8OXUqCxJBioCiYxzRJ3ZtNsoVQ5OO2zVlU6EPsxYg0wb-BCmn9U_MBBUBgYKqXvOwlbddHPJAv80YRSitoYcqzaxCEuTghuBFQe8yEUYR4uGobQkVDT_RISsDchSdmvsaZl5pkFQSGHqv6Y7L5pJ6M2k_F04RKnlEHrX4xqSQOGreEnuz8MTKxnyvx3XEanRHzhxGGUpvnrXnTsIeLTR_vOnj7gPXACOQml2n5T9G5sXw4vpuyJr97F6VBYCE8TOXzMMGzq7vNz17qRTgHpTNK6zhPge83M9BzEFBvv2_KJhPXdjiHM8xR8TjDgi5-KV3ANSbhV4jpcXsg695we-TMh-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زندگی ملانیا و آشنایی با ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21910" target="_blank">📅 15:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21909">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دیدبان اتاق جنگ : هم اکنون پرتاب موشک از محدوده شیراز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21909" target="_blank">📅 15:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21908">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21908" target="_blank">📅 15:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21907">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الجزیره: حکومت ایران می‌گوید به مقاومت در برابر حملات و فشارهای آمریکا ادامه خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21907" target="_blank">📅 14:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21906">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">«دادن استخوانی به سگی ، نیکوکاری نیست؛ نیکوکاری، تقسیم غذایت با اوست، وقتی تو نیز چون او گرسنه باشی.»
جک لندن
یاشار :
کمک واقعی زمانی ارزش اخلاقی دارد که برای کمک‌کننده هم هزینه داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21906" target="_blank">📅 14:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21905">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سعید لیلاز، روزنامه‌نگار و تحلیلگر اقتصادی و از چهره‌های جریان اصلاح‌طلب :  «مردم می‌دانند  خر ما اگر از پل گذشت ؛  برمیگردیم به تنظیمات کارخانه»
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21905" target="_blank">📅 14:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21904">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0mV1j03mcMezdLFLiyiVIKBbmWlGHWmqMe4Z7G2rPPK5lgXR0w6UrfyWJUFwdnQnf5xCSC8i3f4BSIS6bDGHI08Q28xqw4U20jzgMt6T4wTxqc4eYPFUnphYMgUYgPd3pNtUNM4mLNOXT3ilJDuvk6vgZFVwulbUzLq1gD20PpI2ZAVateKTUWWFsXVT5vjXG3uefp6pbpNR8hKO60mqMOc-5BjiCxY7056vCJF5PMOTlaxHgi2_KNjMaQlF84oCRnMqpYVVcmrcNs1_TXhVkhfMafknIhFLBnqZcmwOZ1F_lwocEdvkOJBm968FwOYy7cAU2dBffyj-2c3Di5Qxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث بازنشر خبر : ترامپ قصد داره بعد از اولین درگیری و تبادل آتش با ایران توی چند هفته اخیر، قراره یه ضربه «سخت» به ایران بزنه
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21904" target="_blank">📅 14:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21903">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فاکس نیوز از قول ترامپ : هرمز در «وضعیت بسیار خوبی» قرار دارد. پول ایران در حال فروپاشی است. تورم ۶۶٪ است.
«این بدان معنا نیست که ما آنها را نخواهیم زد.»
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21903" target="_blank">📅 14:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21902">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسرائیل غزه رو داره شخمی میکوبه و چپ و راست هم زده گویا یه سمت و زده برای فریب و تروریستا به سمت دیگه رفتن که تله اصلی بوده و پوکوندتشون @WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21902" target="_blank">📅 13:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21901">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نبویان: اکنون بهترین زمان برای حمله پیش‌دستانه به منافع آمریکا است
با توجه به کمبود ذخایر جنگی دشمن، افزایش قیمت سوخت و نزدیکی انتخابات کنگره آمریکا، دشمن به دنبال کاهش تنش است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21901" target="_blank">📅 13:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21900">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نتانیاهو
:
نزدیک به ۴۰ سال است که با مسئله ایران درگیر بوده‌ام. زمان زیادی طول کشید تا نهادهای امنیتی اسرائیل را متقاعد کنم که مستقیماً با خودِ ایران مقابله کنند. همچنین زمان زیادی طول کشید تا ایالات متحده را به این درک برسانم. توانستم این کار را انجام دهم، چون نزدیک به هزار ساعت در شبکه‌های تلویزیونی آمریکا حضور پیدا کردم.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21900" target="_blank">📅 13:37 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
