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
<img src="https://cdn4.telesco.pe/file/LQgPBxoFaJQUZNJESKBeODd94U90dEuPeW4PTTVv44_uC2VQVRJrZjny49ZKP-KNnNqtjU_d53Z0RJ1PKInc5UQuFBM9FUOIJ8tujCaUWnClMa4BI_jZtVlFuU0H7_-AQq83OGPmjPq7xZ9gjgNWY_lqaM0xk45LtfHcKGiM_GZ3plxj--Ia8nsPJ91vwZxUxPRZ1wGzDJGOcy_xI_X0lQI8D1z1Mh05E8qNY9gM3HEUghgbkP7yB15Z0JDP3J1LJjyqW127ReqPQW8s9VLZKuSAdxOg-JmpdY8gI7_4SqAIBbbbDwFJZKyK1KyxITTFVXTEFzcGAW6Mj-7Cd5zZww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 20:36:45</div>
<hr>

<div class="tg-post" id="msg-151492">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXinHSJcs968qkcgIDBdBSPnff65OC3C6ahpzzj5K5aoZe7xgZ9Eh8KZw3uU8jn6b6qEb8jYrGjdWOeWjXwfHhzvzrzc_S50HaV012gTLem3AtU_NHZ44JPF4Q3E4TK1JROg10yzq82ep81sxOXtypq53jLXwSR_zZ76HQoWQC2oQbhOUHaZjISXSSSUlRP1foBuJ07wB-A1V6fkhEqOLGnVj1VcTx6Ff3HIZ23BpitJpEvNflY2HMhl2jqLDWsUZx42I_47wAtq6wUiYy7LFPx8a9l621xnNWLmyQzVkO_qOnsECNIO5_VYZ5Qx5Ie0NBdVIk9obsmShjOoSYPi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ پرواز جنگنده‌های آمریکایی در آسمان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/alonews/151492" target="_blank">📅 20:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151491">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 300 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/151491" target="_blank">📅 20:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151489">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
رویترز: بر اساس آمار منابع امنیت دریانوردی، حملات به نفتکش‌های عبوری از تنگه هرمز در به بالاترین میزان هفتگی خود از زمان آغاز جنگ ضد ایران رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/151489" target="_blank">📅 20:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151488">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qK9H5aXtRYdSdfO5N97DR3NIELpmK4qHabGIAa9C9zUzodF-KT-1PiYKi9SMwUGTMkWU5DgZLNu_1fSaJPBVSwyAqWWpWJffzoqwbIPnTBaR-zRbSNhUuXK0JcEuUWH_O-xeIGGqlK211wWV2GtCIwVL4v1OqcnpnRsVCT3G-D5fpYB8ybjO1edpznTAf1lYBedjwqaMSTQFDZQCjWzeLMPSVfYFUAgn3eUUYcCrnhMoc5NEgRn8Oyni-o79PPALxhGvGqBXUS8DZZnvm9taNEtAuAsFreNvoOTskPxCRcZ7dXmY5piTdp8MnIzE0JdeXaj0wtJaXLzEcYCkPROsVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرودگاه بن گوریون و فرودگاه رامون: بر اساس گزارش ها امروز چندین هواپیمای سوخت رسان در این دو فرودگاه فرود آمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/151488" target="_blank">📅 20:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37aac2aad.mp4?token=fB9dKeTL5QSo7AsoDXV3xGpvvLnqYD6j9PpWVdQgBdTu-rw3NM0fBCm_ZZQcEUnumOsNjjeA7hbCg1Rt1hQpvTpWg1FTC2wV2IZulijx2xUsAeVaNXe4aqy1ffCkbkg8mMgX0dKEcvPoZU8b9LyzJwKPxjsvkAWjvzCggZjFZmMPknQji3p19xRfh83jjXKA3CpzENP-MmVPIWtdwwwHDbFzH7FowANH0liklFxgeEjfJMnhJ4W3Jm4AbndiR_a3pyojWH8hHjWxRK7atnV-GlUoo9E1WcNzAQJjIWXZrh5MXslUPXuE1DrCBrIQpWSfCLpNMjDy0AqTgYyu2Wm7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37aac2aad.mp4?token=fB9dKeTL5QSo7AsoDXV3xGpvvLnqYD6j9PpWVdQgBdTu-rw3NM0fBCm_ZZQcEUnumOsNjjeA7hbCg1Rt1hQpvTpWg1FTC2wV2IZulijx2xUsAeVaNXe4aqy1ffCkbkg8mMgX0dKEcvPoZU8b9LyzJwKPxjsvkAWjvzCggZjFZmMPknQji3p19xRfh83jjXKA3CpzENP-MmVPIWtdwwwHDbFzH7FowANH0liklFxgeEjfJMnhJ4W3Jm4AbndiR_a3pyojWH8hHjWxRK7atnV-GlUoo9E1WcNzAQJjIWXZrh5MXslUPXuE1DrCBrIQpWSfCLpNMjDy0AqTgYyu2Wm7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: تو تگزاس یکی هی میگفت من گیاه‌خوارم، گیاه‌خوار یعنی فقط کاهو دوست داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/151487" target="_blank">📅 20:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151486">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوووووری / منابع عبری از شنیده شدن صدای انفجار شدید در حیفا خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/151486" target="_blank">📅 20:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151485">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
روبیو، هرچند ممکن است گاه احساسات، پیوندهای محبت میان ایالات متحده و اروپا را تحت فشار قرار داده باشد، اما نباید اجازه شکستن آن‌ها را داد.
🔴
ما باید با هم، متحدی را تقویت کنیم که قادر به مقابله با تهدیدات دوران خود باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/151485" target="_blank">📅 20:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151484">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع ارشد: تلاش‌های میانجی‌گری میان واشنگتن و تهران با بن‌بست مواجه شده است.
🔴
تنگه هرمز دیگر اولویت واشنگتن نیست.
🔴
پیشرفت مذاکرات به پاسخ ایران به مطالبات ترامپ درباره توانمندی‌های هسته‌ای این کشور بستگی دارد
🔴
واشنگتن از ایران می‌خواهد بپذیرد که به توسعه توانمندی‌های هسته‌ای خود ادامه نخواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/151484" target="_blank">📅 19:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151483">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2371df48.mp4?token=K4E5ph6jA3J8irbFEgRAP7ygZS0K7s3ovCCKtA3tOUjXJir67dtx7EFAe3gUQ-wE0yOGgvxoYnISs0jHQ32eNk0thM5qwx-WLLIj8jBzdOC37yj_dZu7ffuRs9E6u5om3KhXslEsCoSDS1qMJBb_5Ewd6gZxrQWA-wAl7oMcnCKprrzZKzLRhiVg2KPYj40SyWO-upagKOs24OBEFxa2I8DLtkNFdVnSbBGPHFiihpYQO9q6yt8T19_seNNkeJ8BDBwufDZF6Xum8X_LiJR8pGo1CFrAwEFFSb9X5DPe6a1Am2jgHoQypGxFokEERo8oJHqjn7hQ6zq-9han6CrLCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2371df48.mp4?token=K4E5ph6jA3J8irbFEgRAP7ygZS0K7s3ovCCKtA3tOUjXJir67dtx7EFAe3gUQ-wE0yOGgvxoYnISs0jHQ32eNk0thM5qwx-WLLIj8jBzdOC37yj_dZu7ffuRs9E6u5om3KhXslEsCoSDS1qMJBb_5Ewd6gZxrQWA-wAl7oMcnCKprrzZKzLRhiVg2KPYj40SyWO-upagKOs24OBEFxa2I8DLtkNFdVnSbBGPHFiihpYQO9q6yt8T19_seNNkeJ8BDBwufDZF6Xum8X_LiJR8pGo1CFrAwEFFSb9X5DPe6a1Am2jgHoQypGxFokEERo8oJHqjn7hQ6zq-9han6CrLCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی ساکنان غزه دقایقی بعد از عملیات طوفان الاقصی در ۷ اکتبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/151483" target="_blank">📅 19:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151482">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
فرانسه سفیر ایران را احضار کرد
🔴
سخنگوی وزارت خارجه فرانسه اعلام کرد سفیر ایران را دربارۀ آنچه کارزار انتشار اطلاعات گمراه‌کننده دربارۀ اعتراضات دانش‌آموزان خوانده، احضار کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/151482" target="_blank">📅 19:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151481">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31254ec41c.mp4?token=uT9eUfOUQpMXP2Wd3_M90uWL4FWllP2RxzJocyspNoz-j67Ag7rMHz83RKt6XOuTy-kITU_t-VsJPyQOh5qrzOWkz8jeGTj-jtYFnP2vGvcfI2FeyXEBPdhhL8xzw8dwOgEl8loGRhIklTFEK2aJLykNS7ixUcGyT_fgky0a-P0ft3R9cHNUwM2KQu7zOk0qv_wFo61YkJVY6fRrm8V0iOcKGjm1w6_Z13641zHpIvngugj4DE9P7ua8R4fad3oQ733AIeFwH8F3yDCJDJkNX4LdOdVmxiyKcbEX3kT9GL-CIacZ2poIPxXOeQQ4sd0scM4L6gITWGwLQt0O_8LX8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31254ec41c.mp4?token=uT9eUfOUQpMXP2Wd3_M90uWL4FWllP2RxzJocyspNoz-j67Ag7rMHz83RKt6XOuTy-kITU_t-VsJPyQOh5qrzOWkz8jeGTj-jtYFnP2vGvcfI2FeyXEBPdhhL8xzw8dwOgEl8loGRhIklTFEK2aJLykNS7ixUcGyT_fgky0a-P0ft3R9cHNUwM2KQu7zOk0qv_wFo61YkJVY6fRrm8V0iOcKGjm1w6_Z13641zHpIvngugj4DE9P7ua8R4fad3oQ733AIeFwH8F3yDCJDJkNX4LdOdVmxiyKcbEX3kT9GL-CIacZ2poIPxXOeQQ4sd0scM4L6gITWGwLQt0O_8LX8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه ایالات متحده آمریکا: ملاهای افراطیِ جمهوری اسلامی ایران و این فرقه‌ی مرگ، کودکانِ بمب‌گذار انتحاری را همچون قهرمانان ملی می‌ستایند و شهادت را به خودیِ خود یک هدف می‌دانند.
🔴
قهرمانان ما ممکن است حاضر باشند برای آرمانشان جان بدهند، اما قهرمانان ما مرگ را نمی‌پرستند.
🔴
دقیقاً به این دلیل که ما برای زندگی ارزش قائلیم، می‌توانیم قهرمانیِ کسانی را درک کنیم که حاضرند جان خود را فدای آن کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/151481" target="_blank">📅 19:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151479">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5yuSDdTgnnMNqlOH9KPwfBpOSkIjw6tV_Jwr7SrE-YHXdZUY2rFrJtqKUFYeqiUswZy4nMmeOmbZhN1Ns2WHCK_XhOBOPmZ9kH-wC-sGIOzAIn_cvdgR_Eih6fUUk-Uky4bX4ciu6Ar5r9tvQ5teZ4WNilQyckcPEfO5egweAU-g7LxB7gBRwL2IUCCDMvdgy72AGPJppa1986R6lVYqHgA_QBS0SJouKslZJt7blMsK3dZxRWMSnVWlSnX76XAIebxk1PUCFa9rWOaCUrEmbDNJ7D_aDi7Cc4gOJQDWZZI_2stVrbzKamxEOhFLs5YP9CnQhB-7eW8nozLwgv9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba0cc8e697.mp4?token=Nw-ES3aXodbDvx-8nti4H1_jDHSQALoc2sqByWoE6qHweVGF-Y4JKYVc7hdEsi-bhW8IQ1yUXtxk_kAmVDvtEdLF2MGnKh9ysPIznOzrSfzA2qhxx43XDWaPzbONAnNtDuwY_y4b92nOOkFEsT_DOA8i58q7b0DEJKloWEyBrlrlIzIdkM4nVCJvzwl9NdRnRWtJF17kEIURqMwyqLOCj2VoiOEnYp7WgCJF25BhDsjb77P1aZAXaAmQMPIwiH2yxSrnxrXWWz9in_3fODRvrRe3Y_lj_DNM9jpUuRM5OkZ7wJMo5HrnPa6TwRTGY7MuB3qruwTJmoYLYZlxtO-Bag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba0cc8e697.mp4?token=Nw-ES3aXodbDvx-8nti4H1_jDHSQALoc2sqByWoE6qHweVGF-Y4JKYVc7hdEsi-bhW8IQ1yUXtxk_kAmVDvtEdLF2MGnKh9ysPIznOzrSfzA2qhxx43XDWaPzbONAnNtDuwY_y4b92nOOkFEsT_DOA8i58q7b0DEJKloWEyBrlrlIzIdkM4nVCJvzwl9NdRnRWtJF17kEIURqMwyqLOCj2VoiOEnYp7WgCJF25BhDsjb77P1aZAXaAmQMPIwiH2yxSrnxrXWWz9in_3fODRvrRe3Y_lj_DNM9jpUuRM5OkZ7wJMo5HrnPa6TwRTGY7MuB3qruwTJmoYLYZlxtO-Bag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پلمب تالار غدیر بخاطر حجاب همسر علی دایی
🔴
دیروز علی دایی و همسرش رفته بودن قم برای همایش یه شرکت خصوصی. امروز دادستان قم به خاطر نداشتن حجاب همسر علی دایی، کل تالار رو پلمب کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/151479" target="_blank">📅 19:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151478">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
مقام ایرانی به رویترز:احتمالاً ایالات متحده حملات خود علیه ایران را بین انتخابات میان‌دوره‌ای آمریکا و انتخابات سراسری اسرائیل که 5 و 12 آبان برگزار می‌شوند، از سر خواهد گرفت.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/151478" target="_blank">📅 19:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151477">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJucnuVwzWZ3QmLrJedjxPCuF-WeTob9N5XuPYhNqq3Bwfv9FNfy8VvMnNDsmAhXMbOiKWkjFy6hs7_oVnAmdMsqrZQu7vVlMuSMTdRk19zFCCQYkpRZLpKSwkhcZHH0eotKcZTKvLiRtZl46uGSlUE-Uj2giIShBsEz_pJYh4v1gPyy5vfDltawZZVG-9bmHG6TMWnfRd7flOg0xmKB0eHTFSbFB1Uk0tR69ycDbkt0DNFq-rnHUGUcXvpZ1V7Z36LZmdJubIh9JOhdCGjvw9BbHhHgwSli0eWku3TgnPziQJA85Ib8wQsDxtAzdUViUuOh1HZIDBMG_f0uON8LrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از غزه قبل و بعد پیروزی ۷ اکتبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/151477" target="_blank">📅 19:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151476">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ، به همراه تفنگداران دریایی از گروه سوم هواپیماهای نیروی دریایی، در تمرینات بدنی صبحگاهی در سان دیگو شرکت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/151476" target="_blank">📅 19:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP0wvU-IbLEDK8XR7Cs3FPgVDCRxZbPYhy1kafHLeisDBYsH8wyvaPlfLawJ70_Xx5tn4TBLjUKwtO1583mJMPljxhZp2oA701KAOeLJfFgvJOlkOykwUgwg2jZ1OgYaV5pWU182LKSg_5-89SGH2wrmHvtOADpt60Azr-HNPOuvg_5O554OtpkB0NwCSA0dYKAmxQvvjKvhyMPv-9b6XE6tPZ6ejlvZtAZUjP2VqXUHnRZCrVL3B9pFA8OyrKkTXyWcIcMUfNNYcFRcevD40zAPt0RFe8hDt6eKK8JvGrooVTQ9Bk5D1xMbhSwmeYgCxpwyrgzNqshSQr5r1Ee-7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری رویترز:  یک ماه پیش، ایران 200 میلیون دلار به حزب الله کمک کرده.این پول خرج مردم آواره میشه، حزب‌الله قصد داره تو مرحله اول به هر خانواده‌ آواره، 3 هزار دلار پرداخت کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/151475" target="_blank">📅 19:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyOZBtoeaTp9AUXki6Tibkt-nX1eVDSvRXjN92VGF-8ni7x57f_RbpevQgxewr0AMEDXjQE9dtoda_V8UBG00BpObHl_Z7_cS-6taodWEc6VgBAFxX-dbjC4NFxj_lH59dzN3uOVRmfmv55fVfP-x1_k4H6giYrtnAUfFqc3T3dHKDTP9ESidSfQoy327rIotuj3lgD3LehKFHJx7dB1g5o4GvLTWqqe08BMDgObdg9QlRNR0zq1zogl9wY43OBy2o4L-u_Kju2PTAxnqjLSYDZ8fnYXrGvRBr942ycwQEDesg8vNkvqs3sPp5VYg4mK9Ir7L4WI5LjLaAprBLPCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعدام بخاطر یک استوری
‼️
🔴
نجمه امینی دانشجوی ۲۳ ساله مشهدی به اتهام استوری که در آن به پیامبر توهین شده شعبه ششم دادگاه خراسان رضوی به حکم اعدام محکوم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/151474" target="_blank">📅 19:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi4iDNb21qZ1MxrlrVr9CloAU0qIwKtNc-OdqI5DUb_d1TD6y0fTEAB0_aE06PjvVrZIzLDKgvcYGMT4GYkMyAjf_BnrFPGcVeD8iHeXrw5ToXj5QNDzberB_3nZOIWAv2Ji5zVtTzlFEK56BePxqOOuGr_uvOnQfMJ7geousyi4UbTLHYjUgwcMHf_z-fsISkmH4_YX9W4F5LBAfjyxgNmWtqh7d7Z1ygbivn9VifHf0t9F04Mnd39yI_d-AUuf6ITZzNDMdJoJkcuxOFNNChXWPsV3m314Ahj2jSNrmWO-Nl-6LmLU6bT7rSwLKBalMGireaqCJmUa9xjLO_gdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:
تنگه هرمز برای همه بازه جز خودمون
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/151473" target="_blank">📅 18:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f7cee201.mp4?token=O9xV-TLplKJdeG0IlZ48Da-IpqIp2XxM7s1UvlR3Vyu-c-ZCyxR6wfrGxy8kwsJRc_3D6vTtOF3cRUUdHFi8YcaKjgyHuxG19OPuvQ7ezBBa_zhhWJQZziF22x93p51mCP2ZhXPzmGGQynSVDD9we_K1bqonAW0AoNwcl2WrJi6Q5xkNKqWD3H2_ETZ4z2dfkaMCtWGo7xdZw07XeDLSGTkmK3JjrIm1pHdlVnSpLA9sJQYDEKvgivXkqzDQNL-ziMUzBGtIzkxx_LJu-dFQj1RLMrzCSXgfLegY8FoRV1a77Bd4EPC1ImpmOV_J0MMeGxhBQVlv7IBTW-t6qjZpHpDiXHOSFAxCk6yNn4MK4-33EnXNCgyJ2YEJA8yCHenEY5lgYM-SDQwBOoge3E4yrizS-DuCVQJrXU_PINv8mIOVJLVS8PZHy4kQ9YajkjnGbyC0HrR5-KuSxxCnmjYIqhIB-xDvTt15ze5KkjaG9hElLU07kGGWPW_q7sXorjvJYBf8TSw9xMRwISB1F0VaOscYX_XwWQkezrJiMh46amWW4Svu92yauDBW18w-C3c0BpicuTqE0ifugip8NaF5k595ymrSWBWUDD-QKTe6z_y38tLi_I9Q-TXU6iG4p9r6ZUyxKz7wJ4PROVYAbzjS9_Xt0eq7baMi9IzQsnEPgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f7cee201.mp4?token=O9xV-TLplKJdeG0IlZ48Da-IpqIp2XxM7s1UvlR3Vyu-c-ZCyxR6wfrGxy8kwsJRc_3D6vTtOF3cRUUdHFi8YcaKjgyHuxG19OPuvQ7ezBBa_zhhWJQZziF22x93p51mCP2ZhXPzmGGQynSVDD9we_K1bqonAW0AoNwcl2WrJi6Q5xkNKqWD3H2_ETZ4z2dfkaMCtWGo7xdZw07XeDLSGTkmK3JjrIm1pHdlVnSpLA9sJQYDEKvgivXkqzDQNL-ziMUzBGtIzkxx_LJu-dFQj1RLMrzCSXgfLegY8FoRV1a77Bd4EPC1ImpmOV_J0MMeGxhBQVlv7IBTW-t6qjZpHpDiXHOSFAxCk6yNn4MK4-33EnXNCgyJ2YEJA8yCHenEY5lgYM-SDQwBOoge3E4yrizS-DuCVQJrXU_PINv8mIOVJLVS8PZHy4kQ9YajkjnGbyC0HrR5-KuSxxCnmjYIqhIB-xDvTt15ze5KkjaG9hElLU07kGGWPW_q7sXorjvJYBf8TSw9xMRwISB1F0VaOscYX_XwWQkezrJiMh46amWW4Svu92yauDBW18w-C3c0BpicuTqE0ifugip8NaF5k595ymrSWBWUDD-QKTe6z_y38tLi_I9Q-TXU6iG4p9r6ZUyxKz7wJ4PROVYAbzjS9_Xt0eq7baMi9IzQsnEPgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرانسیس فوکویاما: جمهوری‌ خواهان در انتخابات پیش‌رو شکست می‌خورند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/151472" target="_blank">📅 18:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
حسام الدین آشنا: کاش می‌شد حالا که آقایان رسایی و تاج زاده هر دو گرفتارند؛ مدتی با یکدیگر هم سخن شوند.
🔴
حتی شاید پس از چندی اشتراکات میان خود را در موضوعات مختلف بیابند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/151471" target="_blank">📅 18:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
معاون وزیر بهداشت: هنوز ابتلا به طاعون قطعی نشده و تاکنون نشانه‌ای از انتقال پایدار انسان‌به‌انسان یا خطر شیوع منطقه‌ای و پاندمی گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/151470" target="_blank">📅 18:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151469">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نتانیاهو:
مطمئن باشید جمهوری اسلامی سرنگون میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151469" target="_blank">📅 18:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151468">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نتانیاهو: ما مأموریت را تکمیل خواهیم کرد و همه کسانی را که در حملات ۷ اکتبر شرکت داشتند، پاسخگو خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151468" target="_blank">📅 18:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151467">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
امارات استفاده کشتی‌های ایرانی از بنادر خود را ممنوع کرد
🔴
اداره دریانوردی وزارت انرژی و زیرساخت امارات اعلام کرد: ۴۷۲ شناور حق استفاده از خدمات بندری امارات را ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151467" target="_blank">📅 18:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151466">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
بلومبرگ: سوریه قرار است به یک مسیر جدید برای صادرات نفت خام عراق تبدیل شود، که این امر امکان ارسال محموله‌ها را بدون عبور از تنگه هرمز فراهم می‌کند
🔴
عراق از سوریه درخواست کرده است تا در زمینه صادرات نفت خام با انتقال آن از طریق جاده به یک بندر در دریای مدیترانه، کمک کند.
🔴
این اقدام، یک مسیر موجود را گسترش می‌دهد که قبلاً برای ارسال سوخت عراق استفاده می‌شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/151466" target="_blank">📅 18:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151465">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqPy8oxGIEvgNrXGAGeIbSNNVGXVLjsVxFlxIFLjNoTxfwmh1acZkv8Jcm-HMn3bM5YoLeq0yu9FDGWXstvmq0R0yNMs2qCjVLPWGJUreJk-dkPGETAR9BNLYje_YFI7HUaDjfopnK85KJzKViXE37foYBcQU6L-LmnMGBmIwADxsZHjoCIjWnXx9UB1K5dleJ-NoS93PyOCA_I2pI2CeY1ZVMBjE6NULYAk-F_ezFEmR0EEpagRCheUpptXsnmRGN5Acr92_C32ougJtNl6I65vnDEUos4Y43qp8PcUyJ1RoGFP-1N38j_GVS4emE0O-Ulu_nSXLaH2GBy0Hnz0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نادر قاضی پور: رسایی تو زندان هم موبایل داره هم تو یه بند مخصوصه، یجورایی هتل
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151465" target="_blank">📅 18:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151464">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ4NPEhi8SBQfz87IuRqKO0RRsY8QtBaGX1PPkj0HizSq4sc_dXnHaqmubtVZamRvaOG30q_Zy9L4vrizV6cGoUn3W8U-e1F5EvKcGVcOLlCgtkzBiMs0tlrZVWh4E3ay1HyHXbrjUGN-WVaL1DIREaT2br0lDSsjIwpI7E22kPJ5m3be1AZlf0DZRqABJ36WvJd90HwP-c8YYzcOQcO53BTn_9X4eAZLGFR5Pd-wsMMvxMn2azHOPW_Fh2lV0sRBK6dDnmIoYw2A9BXhzpcF3PDUiSkUgnFzNPk4CGDIpedexDsWDzPiueVVyHxivBIF_QeHDGuBlm0tVQ4FcL0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شعارهای سیاسی ملت معکوس شده در حرم امام رضا، صدای مذهبی‌ها رو درآورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/151464" target="_blank">📅 18:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151463">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نگرانی ام آی سیکس (MI6) از افشای اطلاعات پس از دستگیری رئیس جاسوسان آلمان
🔴
سازمان‌های بریتانیایی در حال ارزیابی هستند که آیا پس از دستگیری آگوست هانینگ، رئیس سابق جاسوسان آلمان، به اتهام جاسوسی و خیانت، مواد محرمانه یا منابع انسانی افشا شده‌اند یا خیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151463" target="_blank">📅 18:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151462">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3922c39860.mp4?token=B9AvNw5GTkCOnlqL96xqGHG2JFr-nJnKlpz04b0SUkzfs0lJHFqFEWsr_FiT35Q7a8PP_ZUbK4FRMBdz6leGWJ_6FFw5uQXSUCCkv2OkN7ZJavsprklByQsBtCLQ5bvx7ByVL7k_3ebLWtu8ZmmE75sH5MIpjWsz82Z_fJDRdHFzEvOXb63j6cmnR3KNaHpItpeAR75zviaaH0iXktVLW_u4lTb-7QlbtF8oQ2yBvEH_DZVkofUMAWgynRy2lBc-Vy1kjZe6IiEPXzoJLHvhXPp1COXA4Xb2W2ErjnLETB_jYjcRZEAtMTB0xYlN7cSfhv7e45ZIJ7GhkuANznMnWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3922c39860.mp4?token=B9AvNw5GTkCOnlqL96xqGHG2JFr-nJnKlpz04b0SUkzfs0lJHFqFEWsr_FiT35Q7a8PP_ZUbK4FRMBdz6leGWJ_6FFw5uQXSUCCkv2OkN7ZJavsprklByQsBtCLQ5bvx7ByVL7k_3ebLWtu8ZmmE75sH5MIpjWsz82Z_fJDRdHFzEvOXb63j6cmnR3KNaHpItpeAR75zviaaH0iXktVLW_u4lTb-7QlbtF8oQ2yBvEH_DZVkofUMAWgynRy2lBc-Vy1kjZe6IiEPXzoJLHvhXPp1COXA4Xb2W2ErjnLETB_jYjcRZEAtMTB0xYlN7cSfhv7e45ZIJ7GhkuANznMnWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دریاچه ارومیه پس از نخستین باران پاییزی
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/151462" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151461">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=Nf8OLd3S8CUHQLhS4tAwfcoOjvKaqxVf0rjt0dWqyf0JuxjwewGdm75z1kGzxuqarkCkP75-vxJgi0PxSEkj4D1MOkxm8_rqFUjwdn5_BUjMDlN5N_GeWeaxXRE5VJO4OceJ5A3MOh0d76BTcdAA9xXjOKrJjkP4wYXYKsNp4dTXXcZlxfU4lmwc1XqF4x5ZrW5acQh3_b-Dhn1_HcDZ3SjU1C5eQeuJ0UAvT-7BIRNBl2KXyl-I-INapGnbrTg7eNmGij94Q6Zp9_7Y5mgPxw9EEQrwIMuarKp_jxODdHX1sEgUPsQEBud145hbdjTBPOYYgu0tnqG51riNmR-Ywg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=Nf8OLd3S8CUHQLhS4tAwfcoOjvKaqxVf0rjt0dWqyf0JuxjwewGdm75z1kGzxuqarkCkP75-vxJgi0PxSEkj4D1MOkxm8_rqFUjwdn5_BUjMDlN5N_GeWeaxXRE5VJO4OceJ5A3MOh0d76BTcdAA9xXjOKrJjkP4wYXYKsNp4dTXXcZlxfU4lmwc1XqF4x5ZrW5acQh3_b-Dhn1_HcDZ3SjU1C5eQeuJ0UAvT-7BIRNBl2KXyl-I-INapGnbrTg7eNmGij94Q6Zp9_7Y5mgPxw9EEQrwIMuarKp_jxODdHX1sEgUPsQEBud145hbdjTBPOYYgu0tnqG51riNmR-Ywg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از حامیان حکومت میگه چون این مدت جلوی مجلس توی تجمعات حضور داشتم(شعار علیه قالیباف)، اطلاعات سپاه بهم زنگ زده و احضارم کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/151461" target="_blank">📅 17:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151460">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
عارف: امسال حداقل ۱۰۰ تا ۲۵۰ میلیون مترمکعب کمبود گاز داریم، دشمن ۲۵۰ میلیون متر مکعب از گاز عسلویه را از مدار خارج کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/151460" target="_blank">📅 17:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151458">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu42EWVOooM577T-kgtpcsI0HtqX0rCaQvsHcbYmsPm0euufH4ZxUi99Fk89ZwibZYCj1NLGRV6q88wo4wDxKdfZVWfdx4AJV00t7yKexMcHb8bxAgzoTmMTIOfZhni2qDSZq0ZdqBBquqNQxE5M9x6Eouy_My5FLpzs3nrrsXQvPRSZNGFDFewIAX4uKWOXbXZSEbJAxqF4HXSSH2nUZe6_9MQhCb65zpjhP8YIM3QLkGZMx6svps5SgmRHORIsRFVoBj18p0z-tUAdmhD7Og9tEEDO26zx15am4y-srXDk0Tz4eK_2CUjp2iU6Z79pPRgJjinsV_Mh4yz1I1ZxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی از مجلس بیرون انداخته شد
🔴
رسایی طبق قانون، با ۱۰۰ ساعت غیبت از مجلس، مستعفی شناخته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/151458" target="_blank">📅 17:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151457">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmT8b0Q2Dx3uAVBLpS9Vwd6bLcrAzGHZn0PYbMIg80a4mtlbqLnTBkIT589n1YQcOI975qvO5tHA7GzMKOZLI0mg3vsgl2ZGdB0GX1nU0mOMlVS7auDcVbGgZ7HrG1fXwLyenTMpF-N7ZFoW4kKx8lAm2vwhMn2ST6DJBOZ0dsnaj9zNx-gi5GEak375OuhCzKZLPeUvHJ2euRpfHsNPcuflaCXw3KeKVcgRzTpB8rsMvEVaj49MwgzyisWFCV0dS8ZCAxNqQ9-wWjP1TQSxKK5I3yw7Awx_RXQ9A3q0ErjbUr8G5Q8aUiw1l8fw2sY-yMILJShiQn9OdRgoKw8mGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس یادگاری فرماندهان فراجا با باقرخان
🔴
شبیه تابلوی شام آخر
🤣
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/151457" target="_blank">📅 17:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151456">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
واکنش لارنس نورمن، خبرنگار ارشد وال‌استریت ژورنال به سخنان ونس در مورد کاهش ظرفیت غنی‌سازی ایران:
🔴
مشخص نیست این موضوع تحت چه شرایطی خواهد بود، اما چیزی که مشخص است این است که غنی‌سازی صفر در کار نخواهد بود
🔴
لارنس نورمن، خبرنگار ارشد وال‌استریت ژورنال در واکنش به سخنان جی‌دی‌ ونس در مورد کاهش ظرفیت غنی‌سازی ایران نوشت: یک تغییر موضع قابل‌توجه دیگر در اینجا دیده می‌شود. ظرفیت غنی‌سازی ایران در حال حاضر صفر یا نزدیک به صفر است. اما ونس می‌گوید ایران می‌تواند در ظرفیت غنی‌سازی خود کاهش ایجاد کند. این به معنای بازسازی نوعی ظرفیت غنی‌سازی برای تولید اورانیوم با غنای پایین (LEU) خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/151456" target="_blank">📅 17:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151455">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmHfeBbQFOaOxO2_UofRc6uwhSnfdlaX-jGS6VuwD34wbtxXLCOyQSWiYkyKGR73K3ClKLZFo01bjqClH6rBF5sOrUZmiDYETFHp5e4c-V61MWYUQJWd1q4KhPSYOOLWWcje3QZW0GlRCihBMIoSuotz_Aud1KGT2zZ1aBb3ots650BZTLFn6_VVPlViSQn8C2GC3QewYsXWSDn9jZ74I00OfiScYqX9gqoXk-dSLFmNUQ3Yd-OXpw_zfV9jrJecZfD1eGeYb1wZjMYw3OVwTaQ8HJa4szagdjssngfXVPZZGRPyXu9LexYrvdw2EQzqLHP_NbGkp3P349LiRrMcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
برادر
بیلی آیلیش، خواننده آمریکایی: نگرانم ترامپ کالیفرنیا را بمباران کند و طوری وانمود کند که کار ایران بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/151455" target="_blank">📅 17:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151454">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
عملکرد حساب کپی ترید وسود ۲۰۰۰ دلاری معادل ۵۲۰ میلیون در ۳ روز گذشته
👆
👆
👆</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/151454" target="_blank">📅 17:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151453">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4842f342.mp4?token=ViKBff_WwbbwK_JHS16DckjX7YUE6DQf8YN7ihPXolmynIFTlrmLww9BJjdlsDti5Fw0meH3fXvGK7xPkkcQQXbVeD5msJ8Pt3kjJ8Tyowphcy8HboNV2YroLqt8Nn-l5nDk781aVM53X2Q0GD91p-v-a222vEeqp7IX-gXdcAO5zZ_Bgu60hUZZ-XfxG7HHKBntkJKxYnwYujV6P8iqyKvkLpqTbXud4ACNKD0QfVu7lt0yYFjhdoQX52_agwDgGSB4OtsEI9uiIFNY0YWYW_758wFrE_fhOMFQyiDsSBduZ7g1tCkwdji1YLZ2SbCp8Zzad3kkbHFxNSh6w4dyxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4842f342.mp4?token=ViKBff_WwbbwK_JHS16DckjX7YUE6DQf8YN7ihPXolmynIFTlrmLww9BJjdlsDti5Fw0meH3fXvGK7xPkkcQQXbVeD5msJ8Pt3kjJ8Tyowphcy8HboNV2YroLqt8Nn-l5nDk781aVM53X2Q0GD91p-v-a222vEeqp7IX-gXdcAO5zZ_Bgu60hUZZ-XfxG7HHKBntkJKxYnwYujV6P8iqyKvkLpqTbXud4ACNKD0QfVu7lt0yYFjhdoQX52_agwDgGSB4OtsEI9uiIFNY0YWYW_758wFrE_fhOMFQyiDsSBduZ7g1tCkwdji1YLZ2SbCp8Zzad3kkbHFxNSh6w4dyxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو میگه تنگه هرمز بازه و صادرات نفت از اون به اندازه قبل از شروع درگیری‌هاست. به گفته او ایران دیگه کنترل کامل تنگه رو نداره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151453" target="_blank">📅 16:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151452">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwGBnTLR2b54uw7XGdn0KkIxyTdt-fmtsviAcJSymjdJfmfcB4Ew7sDOL5DO1FZ7F0ZveUBXyx5n5W7cuI17sKLNBG1AblKMFbEo_LcDQBwD8phNtoDKpV72DiMZBGAFveBbaW_cdvYnqkrqbJs0Ygsg1iqxjYScI9PoNMFZ2dvFchuuuSMv2R19hsgjDw5dLsjJKk2uONINmVry7neJVPHxAcPWNcimVCjtrUFOW4z2_6_6XQX1JN22xRk6c1kkOwGekH-85JLujDb31Ef1qmzKPiMmBfU3O1Em49HymFhebZa8lh0wDDYLfxS1oepLHdVZbtCmtUcWVaEkzUzCqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه خبر حال خوب کن
🔴
نارین خانم دختر ۱۵ ساله سنندجی که تا سر حد مرگ توسط پدر و نامادریش شکنجه میشد زیر نظر پزشک تحت درمان قرار گرفت و بالاخره حال روحی و جسمیش بهبود یافته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151452" target="_blank">📅 16:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151451">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏
👈
معاون نظام وظیفه: اگه لازم باشه برا جذب سربازای ۶۰ ساله هم فراخوان میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151451" target="_blank">📅 16:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151450">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFWxJvtKnyNc8bQ4XFEJDRr7slCsyyqmjCV4nX29u8VmuuK0r8caCjTZigos2X9pAo6JGUBmmTyFndSuraeAkVdj_WTStijp5z1DZ0RTAcf-RKkZJRopfGLee4Tx5fZ8zIdDyuXtMMVQbGze7s6VHUXZK1m6_YbxnmNjoNOR94QZR0uAt98qZRMXoWATda8owG1b8-7uH5DRGsSbPSwSvQOeNXXuHtCeUuiXD5HPFYxUp1Eec1HEzftjsIMtCDUd5SqSjH2yAyMtErTe9GYtt-bMnsRSqcA2nFZKBwovCiWKjXSN09ta1AIeNbpigXW-9fsHo7sL011yZsRSK3Gxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قوه قضائیه: رسایی اصلا بخشیده نمیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/151450" target="_blank">📅 16:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151449">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⚠️
هشدار جدی در مورد صرافی‌های داخلی</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151449" target="_blank">📅 15:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151448">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
افزایش اعتبار کالابرگ به روزهای آینده موکول شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151448" target="_blank">📅 15:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151447">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
پزشکیان در تماس تلفنی با ولادیمیر پوتین، رئیس‌جمهور روسیه ضمن تبریک زادروز وی، برای دولت و ملت این کشور سربلندی، رشد و شکوفایی آرزو کرد؛ دو طرف همچنین بر تداوم و تقویت همکاری‌های دوجانبه و راهبردی تهران و مسکو تأکید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151447" target="_blank">📅 15:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151446">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bb0297a66.mp4?token=ICZ0mF2HKAFek8yQS49HMl5X_jMzAUVfahxEQbS3mSoQ5LwxbHyjcVtTF7rAXWfJoOIcniZ_MFrjJtAlDQU5JAWgh7JQsEJctKqs3xY6fXdxrDPYaVdlo536FYHikjnYOdq0UZtkXmZx9c96MQ8mBls_dLqWVGpmXpX4ZhQXRtkVU6_0RGkQrknYlYaGeP_SpqM-TXpt90uNYkamkJ3Xia6-au3z2vKQ1aL8r2rz2kNXgH8MYCo45T6_QYxWJOch38xTYpAacm1SSOthLTAC1Q-Ulrkm7rFxhTQMujtjNJIIhXurgrDaIVOkda7Q4RrMyhcE2GO-yqLZLVd1N894YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bb0297a66.mp4?token=ICZ0mF2HKAFek8yQS49HMl5X_jMzAUVfahxEQbS3mSoQ5LwxbHyjcVtTF7rAXWfJoOIcniZ_MFrjJtAlDQU5JAWgh7JQsEJctKqs3xY6fXdxrDPYaVdlo536FYHikjnYOdq0UZtkXmZx9c96MQ8mBls_dLqWVGpmXpX4ZhQXRtkVU6_0RGkQrknYlYaGeP_SpqM-TXpt90uNYkamkJ3Xia6-au3z2vKQ1aL8r2rz2kNXgH8MYCo45T6_QYxWJOch38xTYpAacm1SSOthLTAC1Q-Ulrkm7rFxhTQMujtjNJIIhXurgrDaIVOkda7Q4RrMyhcE2GO-yqLZLVd1N894YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تاسیسات آرامکو عربستان بعد از چندین روز همچنان درحال سوختنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151446" target="_blank">📅 15:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151445">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مقام ارشد ایرانی به رویترز:‌ دیدگاه‌های ایالات متحده درباره برنامه هسته‌ای ایران با خواسته‌های ایران در تضاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151445" target="_blank">📅 15:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151444">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuIzeYtU8UFUPW_J8gWFngd60Op51d0COqXt82OziX5Hvplabo7LyQdN_dBC1vIFyVceMWDzO_bCqGqkRtrWNRfWXjNONY8ueFjcgF9nSIofBP56LNN2sy2cevraFI4Z_lEncQutHrClohhv-gjEng6AZhRLfVNFOxFanPey6_mPPStIa-hGd3rvJnTf306VHycKQaP3E7SJppdKPLax3DH9ETCWwpUtRzKK6IlmTU6rjiARLWfH0lhxAZxZQBVHiS41xtXtHmDC9NYeaLhXcfR30F4Vi3tkBQmXq-ynhBQhkIb409am6vcmFqAH6y9wOshwnfAgxUMbYrgIKcU2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پارک‌ جنگلی چیتگر که درسال ۱۳۴۷ احداث شده بود در دوره شهرداری زاکانی به طور کامل نابود شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151444" target="_blank">📅 15:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151442">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
مقام ارشد ایرانی به رویترز:‌ دیدگاه‌های ایالات متحده درباره برنامه هسته‌ای ایران با خواسته‌های ایران در تضاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151442" target="_blank">📅 15:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151441">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رویترز به نقل از مقام‌ها: ترکیه برای کمک به عربستان سعودی در جنگ علیه حوثی‌ها، کمک‌های دفاعی و فنی به این کشور ارسال کرده است
🔴
این کمک‌ها شامل سامانه‌های پدافند هوایی، اپراتورهای پهپاد و تجهیزات و ظرفیت‌های اطلاعاتی، نظارتی و شناسایی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151441" target="_blank">📅 15:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151440">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نقدی: والله تنگه هرمز بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151440" target="_blank">📅 15:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151439">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfLe-IFQ8aoAa_h5vFul-stRssRvHdG2j3b6QrF10tQJoyfdUhiU3pZhoBQnLwMdxskgjyQjq0boxmacJ7goAkNx3png-_MIC02JkQxEvivYpcqXG-iRvVpWKH8Amrm-T9OetSt7aOXejfO6xo9qWm9-QexbDs_AbBYPjfZrW_nixDo4i4zRz34cXXTfRw4ZKkImslBrx-v8KkLs2DhUHBi5Kdoo0e5dW_kAI4jJHeegw5jTW-ZosavKIULR7bJmz16KdP2BhwLZLWNcAnVjCxm4tXbZjeBdmnSifCB3zGmudYqq2UCLTMNQ6lm4Hj7RrW4OQEDiOsk9Ogezp-kmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقدی: والله تنگه هرمز بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151439" target="_blank">📅 14:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151438">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jb46kKKuoYkDt_T6ANIr_hwovkNovz5Uxt_-viZP_I1-HdhltwN855q63S6ednbAM-6iyJjf93_Yq-qRZeBzliI8UgjTtRq95fcYrh8j37cdlwc7JtzwxXNVTAxrQBX6xBu0dH9-5iWRh4DxMQ_chvnXRq_VvPuTKN8ykENV7D-Na6GPfUMMDty8pv4KNunl1mm3o3K_QYDTnGoNsdLG9FJQoxwgqJLG_zdrTOhkIiUKZwcPlMCQSvRPqsuu45eIfZ4i9NUCEBbiQR1l9F5v6pNFHHO1A7BKQp_w6vnV3Y2PmlyC_fu8tSODGwulx6nnY85HK5prOcleMpv5j5VWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری آمریکا : با توجه به اینکه ایران از ۲۵ اوت تاکنون حتی یک بشکه نفت خام هم به یک کشتی بارگیری نکرده، این کشور وزیر نفت میخواهد چیکار؟ چه چیزی را مدیریت کند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151438" target="_blank">📅 14:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151437">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره
👇
👇
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/151437" target="_blank">📅 14:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151436">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c199c0f5b0.mp4?token=VSPlKuwWkBdZmvpacrM8cPAG1Ci2_YPPrWe10e4eqqOq7iJlCcmyv3YS0GKa5ctybRPpQ0p0gFAshCYHleLdWJSwL_B_nS6PX-Mu2VHGHlHuCjJrAYHat4GuCOc0QTfocLocAtRwMH2mYE8MkT4O5Drc-i5JcSgv09b0HrOgL4znXYv1T58tZWxCeAHW14acCqro13oiA5EaiQ-wO22RuT19pyMUxxiKEjqzBsrRiJmGcNfw0y0vxvsZN4pZD4pRjcEkhBVKgQwZovQkRDzxXbQQAGXdYsp3H61znIj2kin_1sH66qURKBXhRz5DFLTyJ0IdrZeDqy0sHU1-74CObA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c199c0f5b0.mp4?token=VSPlKuwWkBdZmvpacrM8cPAG1Ci2_YPPrWe10e4eqqOq7iJlCcmyv3YS0GKa5ctybRPpQ0p0gFAshCYHleLdWJSwL_B_nS6PX-Mu2VHGHlHuCjJrAYHat4GuCOc0QTfocLocAtRwMH2mYE8MkT4O5Drc-i5JcSgv09b0HrOgL4znXYv1T58tZWxCeAHW14acCqro13oiA5EaiQ-wO22RuT19pyMUxxiKEjqzBsrRiJmGcNfw0y0vxvsZN4pZD4pRjcEkhBVKgQwZovQkRDzxXbQQAGXdYsp3H61znIj2kin_1sH66qURKBXhRz5DFLTyJ0IdrZeDqy0sHU1-74CObA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شکلاتهای ایرانی هم وارد بازار اسفناک تورم شدن
🔴
شکلات ۹۶ درصدی پارمیدا ۵ میلیون و ۹۰۰ هزار تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151436" target="_blank">📅 14:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151435">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نتانیاهو: هنوز جنگ با ایران تمام نشده و کار هایی برای انجام باقی مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151435" target="_blank">📅 14:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151434">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10ebe1b77.mp4?token=MMQB-yY5fYSgQkIAjHN73b7K58nXmXDOzIOQ8cnipgwh9l_0Wq5eqdNT8gpUTiOt1z9KaVLsCCRtlQBiv25eRYzXGibu2_4CqMzyrLkrq5m9G_7pamdfYZHd-ML8DFrzEFEg-qxVD3gmgCncmrPXQ5JRIlQjMBXIu0ZgHWOij08hqDCe-5l2bmAEDXzgiN58z17LvhsaF2qNanAUYzwPn9svqoytwIX1-5j8TnoP0t4LsFZOXX0amxhJpufa4p7ycFnlxTMsQ8tbFQufe3-yADGSwD2XSTaPcVSveqGi64SN-XxBj8nWfNB9g7PIKQpu77auIzR_QT7ZmFOrnqqASnfIik0HnONm5NX7_ODLRzJj5MiorrOaGVO7eTVrdGsSSDrOd4VWsYQN3p59xHgYtLL7jB0FzDFw7iq8PDq7VsZr4tNdXfl8vO_Peo5OHEivcmUdGvLv3ukIuPrhVImActGEx50Zrdf8PC6t1BLb0eKKaiQ1aVyBp5WyQZbENj6VX9dyTLdHcyLiBrh-KHUKAe_TT1fRDKZB62HtdyZ05nl-hsnweuFJhi7imi93E_RxG4b6SwAonJXWVzibkzjlYCakMc8ykFXYU7akZu-5odRtCA6ncr5II7IcuJTkvE8FRyjuCvNk86TCCZdp5gVKTV4KMu3AZzSi7AePwI4CfD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10ebe1b77.mp4?token=MMQB-yY5fYSgQkIAjHN73b7K58nXmXDOzIOQ8cnipgwh9l_0Wq5eqdNT8gpUTiOt1z9KaVLsCCRtlQBiv25eRYzXGibu2_4CqMzyrLkrq5m9G_7pamdfYZHd-ML8DFrzEFEg-qxVD3gmgCncmrPXQ5JRIlQjMBXIu0ZgHWOij08hqDCe-5l2bmAEDXzgiN58z17LvhsaF2qNanAUYzwPn9svqoytwIX1-5j8TnoP0t4LsFZOXX0amxhJpufa4p7ycFnlxTMsQ8tbFQufe3-yADGSwD2XSTaPcVSveqGi64SN-XxBj8nWfNB9g7PIKQpu77auIzR_QT7ZmFOrnqqASnfIik0HnONm5NX7_ODLRzJj5MiorrOaGVO7eTVrdGsSSDrOd4VWsYQN3p59xHgYtLL7jB0FzDFw7iq8PDq7VsZr4tNdXfl8vO_Peo5OHEivcmUdGvLv3ukIuPrhVImActGEx50Zrdf8PC6t1BLb0eKKaiQ1aVyBp5WyQZbENj6VX9dyTLdHcyLiBrh-KHUKAe_TT1fRDKZB62HtdyZ05nl-hsnweuFJhi7imi93E_RxG4b6SwAonJXWVzibkzjlYCakMc8ykFXYU7akZu-5odRtCA6ncr5II7IcuJTkvE8FRyjuCvNk86TCCZdp5gVKTV4KMu3AZzSi7AePwI4CfD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرویس امنیت ملی گرجستان (SUS) اعلام کرد که یک شهروند گرجی را به دلیل داشتن غیرقانونی مواد هسته‌ای و برنامه‌ریزی برای فروش اورانیوم-۲۳۸ به یک تبعه خارجی(یکی از همسایگان جنوبی) به قیمت ۷۰۰۰۰۰ دلار دستگیر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151434" target="_blank">📅 14:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
مکرون: عربی به زبان دوم فرانسه تبدیل شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151433" target="_blank">📅 14:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
پزشکیان: ما قطعاً مقاومت خواهیم کرد و آمریکا رو ناامید و خشمگین میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151432" target="_blank">📅 14:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1f6da4567.mp4?token=higQ17GEetWVgzNRyDODRtkwJ2f1HxlqSDQJpOVPm4RoR2bSpqUKh0YEbNIatzfmTHu5Kk-_M-Y5dV6vJxBbcJvVdDk7gFqmTKN7BYDVox3LJgYpmiuqodxDozZLbKCkmL6wa24MZlhac6yAMThn4Zb3dmtjjYxgRwCwcyY9QlmXUdpiII11_WnGMiE8R9p7MZiOb8kWPw_NS6WaXkYylHDT4fF4gLxbTLdWcgxKLxSlW16c-pPFGHWWF7CwzGpjLwcNAav0B2e_YIhLndnWxdQFufYCKek-2NiVg5nD1N8m7uDO2ZlU680j46VFlstLF1CzUPBHAPhyhqBRJQ123g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1f6da4567.mp4?token=higQ17GEetWVgzNRyDODRtkwJ2f1HxlqSDQJpOVPm4RoR2bSpqUKh0YEbNIatzfmTHu5Kk-_M-Y5dV6vJxBbcJvVdDk7gFqmTKN7BYDVox3LJgYpmiuqodxDozZLbKCkmL6wa24MZlhac6yAMThn4Zb3dmtjjYxgRwCwcyY9QlmXUdpiII11_WnGMiE8R9p7MZiOb8kWPw_NS6WaXkYylHDT4fF4gLxbTLdWcgxKLxSlW16c-pPFGHWWF7CwzGpjLwcNAav0B2e_YIhLndnWxdQFufYCKek-2NiVg5nD1N8m7uDO2ZlU680j46VFlstLF1CzUPBHAPhyhqBRJQ123g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک وکیل خانواده: نزارید خانوماتون وارد سالن‌های زیبایی بشن چون به راه کج کشیده میشن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151431" target="_blank">📅 14:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پشمام پیش بینی دقیق ریزش و اصلاح امروز دلار رو ۲روز پیش گفت
😐
الانم گفته دلار تا کجا بالا میره</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151430" target="_blank">📅 14:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151429">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0251c17b80.mp4?token=sWtXIo-VddtWrBIpXsWSZPMndFKfqThaKZMzv1LMYVy0HR1eGfE9B1SlbAY8W2Y1Cik_DaNdWNTddb_k2Xfbf2mEYUcuiqey3uqLuhTASVG6wQFCWLagrr6lmGbK7bh8bBosJMHjoQP2j4ysqwD94_BYtpZpY0YAfhoYoatQezf5skdd3qtBN2VNDvA_2OBXR9mp6bIWCGHT8_U4i-MN_MFmLI4qDX_vTP8YO-CFtztlSPoVaxF3c7M6FM2LOhyD1lWe0YYp6CYetB8mqVCV4ecu2JdMrMGtg_HZLhoHdT7XmMVV3-24byYzfHFOr9vVGnzY3jiza0oLdFT55U31JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0251c17b80.mp4?token=sWtXIo-VddtWrBIpXsWSZPMndFKfqThaKZMzv1LMYVy0HR1eGfE9B1SlbAY8W2Y1Cik_DaNdWNTddb_k2Xfbf2mEYUcuiqey3uqLuhTASVG6wQFCWLagrr6lmGbK7bh8bBosJMHjoQP2j4ysqwD94_BYtpZpY0YAfhoYoatQezf5skdd3qtBN2VNDvA_2OBXR9mp6bIWCGHT8_U4i-MN_MFmLI4qDX_vTP8YO-CFtztlSPoVaxF3c7M6FM2LOhyD1lWe0YYp6CYetB8mqVCV4ecu2JdMrMGtg_HZLhoHdT7XmMVV3-24byYzfHFOr9vVGnzY3jiza0oLdFT55U31JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : «بیشتر مخالفان سیاسی به این طرح فلسطینی باور دارند.
🔴
آنها هیچ چیزی یاد نگرفته‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151429" target="_blank">📅 14:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151428">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
پزشکیان: چنانچه نیاز باشد، موقتاً در راستای اصلاح الگوی مصرف، ساختمان‌های بلااستفاده و مجموعه‌های فرهنگی و ورزشی تعطیل خواهند شد تا چرخ تولید بچرخد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151428" target="_blank">📅 14:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151427">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29226cb922.mp4?token=NCb2z1Yzu2EwCxyy9Nbzd8VBij6L8Gh5XdsYxN4klcGtjJRDhkoKj-ze9lc8vkIxcyyWfwpVAddjitUve369reQPBLWwCaccA1Rv9CS-0r7svPg3TkUFt7hTvuGasG4YxpphdIhDqjZ6wC_2jhfnJHi1JhxnfJlEvbLCxmHbwLb_Sayl0dm4lmoozksfhKgH2lV0tN2ZMzJH174nXruudEdOks4pClk3i_bqBMjtgEMlHps7wxoL6bgYym2MTnLt8q_9dqpj3SrqhJBkgUQlPW4DuBhI2soMOYyKZdBjleFs5Ms5dg2fhvLqwhoVW2Tvh-5PwNH01nHYKH175qLmMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29226cb922.mp4?token=NCb2z1Yzu2EwCxyy9Nbzd8VBij6L8Gh5XdsYxN4klcGtjJRDhkoKj-ze9lc8vkIxcyyWfwpVAddjitUve369reQPBLWwCaccA1Rv9CS-0r7svPg3TkUFt7hTvuGasG4YxpphdIhDqjZ6wC_2jhfnJHi1JhxnfJlEvbLCxmHbwLb_Sayl0dm4lmoozksfhKgH2lV0tN2ZMzJH174nXruudEdOks4pClk3i_bqBMjtgEMlHps7wxoL6bgYym2MTnLt8q_9dqpj3SrqhJBkgUQlPW4DuBhI2soMOYyKZdBjleFs5Ms5dg2fhvLqwhoVW2Tvh-5PwNH01nHYKH175qLmMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
رئیسی و جلیلی هم امام شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151427" target="_blank">📅 13:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151426">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
👈
پلن ویژه افزایش ممبر برای کانالهای تحلیلی و اقتصادی داریم جهت اطلاع از شرایط به دایرکت پیام دهید  دایرکت
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/151426" target="_blank">📅 13:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151425">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران: «اگر ما اقدام نکرده بودیم، بمب‌های اتمی می‌توانستند ۱۰ میلیون اسرائیلی را نابود کنند. ما به‌طور کامل از بین می‌رفتیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151425" target="_blank">📅 13:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151424">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزارت خارجه چین: ایالات متحده یک شریک مهم برای ما است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151424" target="_blank">📅 13:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151423">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات الونیوز</strong></div>
<div class="tg-text">👈
پلن ویژه افزایش ممبر برای کانالهای تحلیلی و اقتصادی داریم جهت اطلاع از شرایط به دایرکت پیام دهید
دایرکت</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/151423" target="_blank">📅 13:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151422">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpUZSpibUR1WZ2b2oe9Eb2s-3zKIG6Cl3nJsLqX45UpDQ0MtcrDwZFa-81BqtULKy9PSHLGtV8LGDESqxi2fmG68CJxM4UpFitNCcD_wp7M5e9-_ta2LLXFaUpNtfvx-rKlRkovk64BLnn0hsf_LhCt62X54pegCGW32nJ1-1UHEeAKstYK0sWG0HHBH8WQbZmwjk5Dnu5BKnl7M34SvlObE8ceDxdJzG9byQb7VASp0IJwnfUNZhCr44T21Ldq7KYgK3ccvX_Pe_MZVXX4yGCXqtOY7ixNTMct-1IsDEPn0gD_JlPQ7ZjbHu3eFacWTi4AKXaeC6HKNN5ICeX-Cag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو تهران بنر زدن آخر سر چین آمریکا رو شکست میده
🔴
داستان اون شخصیه که با ک.... یکی دیگه میخواست داماد بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151422" target="_blank">📅 13:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151421">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miTuBmDrXndjplQS0NxD3C4yhTEnpH3t8w399SIvLgNF0tJZi7TTc3Vg6j68XC_h4vIFfOKZOqaMmEH4rhcVvDho3FbsRUr3ePYTDXBchQr0B6HlOqI81TPQi9oPGezlzFe_fr9pDvgze6XhNO5OHq_fqJsh3EkHdjvDOn8hQLFoC4T2guomQ5uft8ncCh-HwiYgnp-cwqx4uglW73wyNdPDV2Xryh0kuwRjnd19Amw_mdCyFAuAKxIWzuN-RfaQVa__OEEb9d6bOUG3NnzTpMwONdQjuTl5DjSHdE25FmO10YQYc9W2Rz9BrJ0G9b9JbD-_pjtAYjhdbDN0bD3q0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوبل شیمی ۲۰۲۶ به هنری کاگان و کنزو سوآی رسید
🔴
«هنری کاگان» و «کنزو سوآی» برای کشف اثرات غیرخطی و خود کاتالیزگری در سنتز آلی نامتقارن برنده جایزه نوبل شیمی ۲۰۲۶ شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151421" target="_blank">📅 13:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151420">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
روبیو ، وزیر خارجه آمریکا : موضوع مورد مشکوک به طاعون در روسیه را بسیار دقیق و ساعت به ساعت زیر نظر داریم
🔴
روسیه طبیعتاً موظف است اطلاعات بیشتری را با جهان در میان بگذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151420" target="_blank">📅 13:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151419">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=F3yxtdnLfU1tcteMKJ9hUnf7Sf5AwVx1Q4wGRTQfQKl24P8GGpwJi2zw--322O1N2nTDFNTCunWRAhm02eG2dsXCxtHiqWX1XDj4K-a4XqG9SEt7rVnGxpnn-dRLkJp8-PWKyL1n6TuAjhMfToQYzy6aJARdKwvnk22QY95nVSyCQt-cSwJqZmqVb56UnTJD4nkItVQ95QnUurCx5I53PvSypKcb0WTv57zTd0q877iXdP-jr--PoPkn4stuzNtrGD7NKx8tysE9ZLGsHFQ09OBHYR-6QosgFOp3UMG-GNn1ZbFh-NWuqh5rzuYJC8wqH2Hd-Th1SnOrUoLzN4lsYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=F3yxtdnLfU1tcteMKJ9hUnf7Sf5AwVx1Q4wGRTQfQKl24P8GGpwJi2zw--322O1N2nTDFNTCunWRAhm02eG2dsXCxtHiqWX1XDj4K-a4XqG9SEt7rVnGxpnn-dRLkJp8-PWKyL1n6TuAjhMfToQYzy6aJARdKwvnk22QY95nVSyCQt-cSwJqZmqVb56UnTJD4nkItVQ95QnUurCx5I53PvSypKcb0WTv57zTd0q877iXdP-jr--PoPkn4stuzNtrGD7NKx8tysE9ZLGsHFQ09OBHYR-6QosgFOp3UMG-GNn1ZbFh-NWuqh5rzuYJC8wqH2Hd-Th1SnOrUoLzN4lsYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا، درباره ایران: آن رژیم هر دلار و هر سنتی را که به دست می‌آورد، صرف جاده، پل یا بهبود زندگی مردم ایران نمی‌کند.
🔴
آنها این پول را صرف حزب‌الله، حماس، شبه‌نظامیانی که از عراق موشک شلیک می‌کنند و حوثی‌ها می‌کنند.
🔴
آنها باید پول خود را برای مردمشان هزینه می‌کردند؛ اما در عوض، آن را صرف تروریسم و تسلیحات می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/151419" target="_blank">📅 13:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151418">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
الأخبار: اطلاعات حوثی‌ها حاکی از انتقال هزاران عنصر تندرو نظامی ارتش سوریه به یمن از طریق خاک عربستان و با کمک ترکیه و اعزام به جبهه های جنگ با حوثی ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151418" target="_blank">📅 13:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151417">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7RbgrDoaBnDnwvM1USNc9aqGf0bGvK98jvF49eM41sm6gsj1uClFS0BDZXpg_Ko0id0pNaphw18KX90ERSxrWsbeme3XIuRBw0khJTRF3mhGH0niY7ViO3xvOso_i9gaifo9qv6LSYPGktU7ORGSMjFChtU3CB0SCMEqJ2Gj-GtsTSsauNgCVpY7h-7eDcoALfdUdstSK08aMaqkIinefSywo7Kv3gs1zGokUwXNSLxiDLc8fdNhRkSv87tNDBGyYz_eIcivvPR2exJ23ZMM5D0YbHekCcEBnh1xZREWUSouozT69cthds4SyRWwspksnts2rKoJzy54bZFqyXwRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زهرا عبداللهی خبرنگار پارلمانی: یک نماینده مجلس در ملک مسکونی بدنبال زیرخاکی بود
🔴
اسناد موجود است. خانه در بستری تاریخی قرار داشته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151417" target="_blank">📅 13:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151416">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Thfjf33t_OCa78GLr-x-iwvoibqpAfup4CYYBEbxd49xWg6-9q_4imtvUdkW2WnRy6OROymGH71y2fFIWmnoBfTogsImUP5tC9-u3R5Y_SWA5tn9Ejo7v8lrsAIz568qCPvsp-eqAPSPrWUPS2FC1iHkTFPQhk1-hDUQmR_aOYRwfzQtiLtzngqswMri238VfSPJkt4tw7O6mTfpra9eq5uanzYtgcJDmkEZxVvXNrrP0zk-HbGxISU1Iah2_peI02g6rnd58mzuaTyowOTfJTaEbZtpE3KTGlaJYWWkFu2t3pr8cR4jjPAEKHuogMKQ2UNf_XUa2dp4qByxRvwzZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زهرا عبداللهی خبرنگار پارلمانی: یک نماینده مجلس در ملک مسکونی بدنبال زیرخاکی بود
🔴
اسناد موجود است. خانه در بستری تاریخی قرار داشته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151416" target="_blank">📅 12:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151415">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6513d8ae0c.mp4?token=JUDEdYx3VtEzmlaA4-RwDMppr65LxwYuv-c0647y5A3M4fql6TdcSnx5slXXvsPD2GHZq2-VwMoLQQEpuso8ogrOI-Kzq4t5mZxGUDQc5uwii0zmEd5cr77N86IHDlq3tU0r9TWo4VL1UAZwGTaO0Ft7CyadQH080Fp6iWzv6fhIamarWddWK2RmuGialBjcIAlE8t6Uif1atd7r7Qan_FVAXnmgJAkbVM0tOtih8weYBCkbgJ_ES6hgUiN_l0v3DXnfXKQJP6yeil1YeY25p6M2ZUEvSfqUL0W_WSqc8pZT5WNIGMg1FRFFXgL3SrQXK2dv7-eh3L_LEm5m2xAX5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6513d8ae0c.mp4?token=JUDEdYx3VtEzmlaA4-RwDMppr65LxwYuv-c0647y5A3M4fql6TdcSnx5slXXvsPD2GHZq2-VwMoLQQEpuso8ogrOI-Kzq4t5mZxGUDQc5uwii0zmEd5cr77N86IHDlq3tU0r9TWo4VL1UAZwGTaO0Ft7CyadQH080Fp6iWzv6fhIamarWddWK2RmuGialBjcIAlE8t6Uif1atd7r7Qan_FVAXnmgJAkbVM0tOtih8weYBCkbgJ_ES6hgUiN_l0v3DXnfXKQJP6yeil1YeY25p6M2ZUEvSfqUL0W_WSqc8pZT5WNIGMg1FRFFXgL3SrQXK2dv7-eh3L_LEm5m2xAX5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: اقتصاد ایران در آستانه رسیدن به وضعیتی قرار دارد که تعداد بسیار کمی از کشورهای جهان تاکنون از نظر شدت وخامت اقتصادی تجربه کرده‌اند آنها مردم ایران را در شرایطی قرار داده‌اند که اکنون در آن به سر می‌برند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/151415" target="_blank">📅 12:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151414">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjNftl9I_GCdSAsVOCu9ESDhB9tlM1XdMaAk2bFZdPW2W4KJLJIKwuP7-dphBodm7RG-B1zjy6UKS9sIhWGmphmBv7WuEbMbBRcfaCJT71nJSeJ2ab4rPWVGtx_0CJETYNh6SG970qUbJqrqPxYdnSepJ9tN0N_xZ8oElI62XMGSWWJNpVyKAZl9wgyxgZmuVrNkPnkeCAWBtL3pIBye-3VuSeLebL-qQab4c98-vUfR7rkM2Wqtmy50o6X0FxNjjmDgaS5fI8zpcyMMtMhpcLcXcHsP1RMRhhcrufGvwOjDxZfDF2ULq6G6STV4txmn99iOY-qC1N8ZhlD0nL5faA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیرعامل خبرگزاری قوه قضائیه به نقل از سخنگوی این قوه: حمید رسایی بیش از ۶۰ شکایت،‌ ۲۵ مورد قرار مجرمیت و جلب به دادرسی و حداقل دو مورد محکومیت قطعی داشته که سوابق آن موجود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151414" target="_blank">📅 12:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151413">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609f1372f3.mp4?token=pD4-rhNN-bvsIFEhGT2kRcr_ETpElZ6Rba5Ei2bRYbPkKf4FvfHd1jc5y87EF510voW5HMK1i5-TcfOX4SwwuukFuYYBrkLAY7RSqyMSbSyjJZMYFOVa8Uka_9sU8Y-auDz4BeuBnCUWSxVKwkHL1Eb-otoMNQ0pTjJaWet3w5VzBnaUpswAcv_7IMKhCHNKqi2h_X6L_QpwtfuF5p9BjhCR4S4jPNzBwvERl38xJlNsH1dIfINWxIlnhTcX1y3-9iVNvyzpIy2QSVhVNpSBSF1DIDNDUUED8dCLL0ZPhbUImiHQkflt_mxrIWbSPTkT6LA7AxrM9xWpYJkHEB-ubA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609f1372f3.mp4?token=pD4-rhNN-bvsIFEhGT2kRcr_ETpElZ6Rba5Ei2bRYbPkKf4FvfHd1jc5y87EF510voW5HMK1i5-TcfOX4SwwuukFuYYBrkLAY7RSqyMSbSyjJZMYFOVa8Uka_9sU8Y-auDz4BeuBnCUWSxVKwkHL1Eb-otoMNQ0pTjJaWet3w5VzBnaUpswAcv_7IMKhCHNKqi2h_X6L_QpwtfuF5p9BjhCR4S4jPNzBwvERl38xJlNsH1dIfINWxIlnhTcX1y3-9iVNvyzpIy2QSVhVNpSBSF1DIDNDUUED8dCLL0ZPhbUImiHQkflt_mxrIWbSPTkT6LA7AxrM9xWpYJkHEB-ubA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک جانسون، رئیس مجلس نمایندگان آمریکا: «فکر می‌کنم تمام دموکرات‌های کنگره حتی به درمان سرطان هم رأی منفی می‌دهند، چون نمی‌خواهند ترامپ بابت هیچ کاری اعتبار یا پیروزی‌ای به دست بیاورد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151413" target="_blank">📅 12:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151412">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b38e5687.mp4?token=HFFdCjtZBHHCUqjQHpORY6i7eRkevMc2BL_mOTF9WmThT-dOxs8TUCzq2l7iOyOGKi1KWRm5Yw0cxqC7FA9KcieXmO6pH7bERDyoa1fAaGg-GX-XrE0qH7O4GHxzCKmE9Uth-ojZ_NcGv9HgdB8S_aa7jU6S9OJOhagrDyVF6wCpUiY33SFEUiD6KKMKi1snhzte27n9AWUfnplTb2ICUdn98O3mMqCc-Rd9cnKEHKygBT07Zp7wTWF9VQr2sfIKj2izSXDmAQT2l5_fkpZIv8dQpUTq2q2TDeZMWt5SQyj-gfEBWqijNysa5smrpxikc623aMDEYMKowFKH2tz8Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b38e5687.mp4?token=HFFdCjtZBHHCUqjQHpORY6i7eRkevMc2BL_mOTF9WmThT-dOxs8TUCzq2l7iOyOGKi1KWRm5Yw0cxqC7FA9KcieXmO6pH7bERDyoa1fAaGg-GX-XrE0qH7O4GHxzCKmE9Uth-ojZ_NcGv9HgdB8S_aa7jU6S9OJOhagrDyVF6wCpUiY33SFEUiD6KKMKi1snhzte27n9AWUfnplTb2ICUdn98O3mMqCc-Rd9cnKEHKygBT07Zp7wTWF9VQr2sfIKj2izSXDmAQT2l5_fkpZIv8dQpUTq2q2TDeZMWt5SQyj-gfEBWqijNysa5smrpxikc623aMDEYMKowFKH2tz8Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک جانسون، رئیس مجلس نمایندگان آمریکا: «دموکرات‌ها حتماً تلاش خواهند کرد ترامپ را استیضاح کنند؛ احتمالاً در روز اول یا حداکثر روز دوم
🔴
یادتان باشد که آنها پیش از این در همین کنگره نیز مواد استیضاح را ارائه کرده‌اند. منظورم این است که آنها کاملاً آماده این کار هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151412" target="_blank">📅 12:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151411">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
تو یه ربع تتر تا ۲۵۱ اصلاح کرد، الان  برگشت ۲۶۰
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151411" target="_blank">📅 12:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151410">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
محسن پاک‌نژاد، وزیر مستعفی نفت ایران: استعفای من ارتباطی با صحبت های ترامپ ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151410" target="_blank">📅 12:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151409">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
روبیو، وزیر خارجه آمریکا: ایران فرصت‌های متعددی را برای دستیابی به توافق با ما درباره برنامه هسته‌ای خود از دست داده است.
🔴
ایران هرگز به یک برنامه هسته‌ای دست نخواهد یافت و در حالی که تلاش می‌کند نیروهای ما را از منطقه خارج کند، رئیس‌جمهور ترامپ این موضوع را نخواهد پذیرفت.
🔴
ما نمی‌توانیم بپذیریم که یک کشور به‌تنهایی بر یک مسیر مهم دریایی کنترل داشته باشد
🔴
باید مسیرها و منابع متنوعی برای تأمین انرژی وجود داشته باشد
🔴
تنگه هرمز باز است و حجم نفتی که اکنون از این تنگه خارج می‌شود، دقیقاً برابر با میزان نفتی است که پیش از بسته شدن آن از این مسیر عبور می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/151409" target="_blank">📅 12:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151405">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcG1IBtYm4BIlkCGWTT67E8cBMk8OUqQHl8jqrQzm6JbSlh-okwaL-leosu3hqxqjWlyRJL3jOcKMFAoHO8-Ol38V7BOf6f71Ut-PlzGzxfnhdhSM1ctxmwehymazpQhdTShQM2CtRSv2kkJ1-Oadw8ew9KJnh0QznAiVie6czCnCoohQc15R1SDDtmMpWninFEjl4Aee_fLMY1uMQLh3MVVK00ptVDX6Z0ViTJgoajmihjsQIFg10S5l3RBIglfSQN2cM2sa0L6XMJrRcUPbfLFfpdpfHs4ah3uWwfOOoGJVTZ92spWnNAOV6-7nH2JEoNktWlAeRTNBrUblKPN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f99fbadfe5.mp4?token=G-92ZjoN90avqg98HLZhJRRwUizX4zuQrrJousHZTPWbE9JUWUzptrkCWLOHYj5JxpsIhpzio7wXgJjU2ttD29euB3Z8cEulLg_ssJv9Gn4aR7rsm9IfF0aeQ28_a97gcZR9NSSVCUE0bO_ykono8ZskOdAVA2BTQWlWPkba_pLNXaJJ_15bGpjQka2cG1cbGumJbHbCC235F614CJTEpH6psHPjnzP7B_yVTnp5Ls1lCpqBysiTMTRjB7DzGEmeYpP5Zgv5zLoyXp_DZxwmcUVR3-C66iOb4IWHmifaqkYN1oIlUuQ6OXNoQpg4lOOXR6tAwCamJ7jnJZ1Ul7UbHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f99fbadfe5.mp4?token=G-92ZjoN90avqg98HLZhJRRwUizX4zuQrrJousHZTPWbE9JUWUzptrkCWLOHYj5JxpsIhpzio7wXgJjU2ttD29euB3Z8cEulLg_ssJv9Gn4aR7rsm9IfF0aeQ28_a97gcZR9NSSVCUE0bO_ykono8ZskOdAVA2BTQWlWPkba_pLNXaJJ_15bGpjQka2cG1cbGumJbHbCC235F614CJTEpH6psHPjnzP7B_yVTnp5Ls1lCpqBysiTMTRjB7DzGEmeYpP5Zgv5zLoyXp_DZxwmcUVR3-C66iOb4IWHmifaqkYN1oIlUuQ6OXNoQpg4lOOXR6tAwCamJ7jnJZ1Ul7UbHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از غزه ۳ سال پس از آغاز جنگ با اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/151405" target="_blank">📅 12:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151404">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
امروز یه دختر ۲۳ ساله تو مشهد بخاطر توهین به ائمه حکم اعدام گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151404" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151400">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bedLnp68QJYtZqwS2GASxQTW0fa9GrEnN8iTRCSonFp1YZsvsoPb5K_rjklYigBi-oXlj_U_aPqaYW71veGYx4s2tPEjV_oQvzZFZni-6JzwcYY3-75mRBcgpg-_TwKosK78s-r3HpErXGXjx7L75_ZUYrKKxNR1I7jkvvQwSl-CVMjjUfWi7UWNOw5Zma7heZ0O33BRzezMfMrzD5l7TWAKqS1D-MfB4j6qojoT0i6epJvNQhbLn1LEysHQh21Z6uSeTfPQuPlVXBfXA0RcWDqQyisvmQRi0wNFWwGY2rvs-sgQSYgrBcD5gRI4eGCylLgZZMWtgEAv5OuuYeWcKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3shxWuixK7GFpb3mBTA9LPm84HHOdsyIezdQ9dt369dngHuW-GrJcOAipBXi7Kjfe7OEHxdckarQzu6AOCM4b_uxQvYTHIprsn-tXAVf2jwXukFpiGW5jVEyXljqZJjnJzOSazBn8USe9KRULZ1pGhWEgA75mori_kUeMDrN6teLbfBLRgIl2bOTdl7VlPPmNCN2hTBp1mHPMePMldH6ZL2QWxPEoU_VpCdhd3mWB_sr_ypzZq86jepbLqCLuXteKDaz6O7hJjHRaTq8gnP9SjSwFCkl5AHL33eyv71KetRdDbh6uzYTab7udC3_itIe9BVoPQo2B-Hcvd0vrniRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hr_zUokrvf7tMuhkCNuDeoN8KJdcodkNrqJeobEG6Qom5yXuSowicer_HrMKwEuM4eKDf1vpT3fsCrVSMVR_NgeEDQjSS2Rg4UD4NfP8-K5AYtoiZywMppirI_z939Mv37bP6dzIJUk0WljjWvIEiG_LNpkyTPcwOPSDSM4XrNBBI-IYKFKu9-WcfqhADglSWFdvsx6FvMn-pvfO62s7Ty0aZxcRLgSOLRMshDvHsKCZ3-bLeAiO16ptRwdxivU7wTPQULqT1I8pgCngv1Ks-mRq9RHfbP6NjurvGlp_6hA-4phONrB-eELvwsw7EAjQeQ_12la63uaDVgeTcy75sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwLc7mM24uVKsbUBz7ZryZh9wQv49aY3SidHCF1-1I2-Pf0ulKYaSog1hFGWQWo4r2OVyKUbzvcp6OSE4OWtmIoJKuExsgzviVoGIXNRUKbv15JnMxA-ruG2BnVr2gvuvkKtYX1wguqrSr6AhlyBcC-UTXFx7bYWSYCEI6mSIw7h9I0ss5eacU-gahBNrYP9p1R2v75PjAstfJMuWEfKSd55ISwSfZAwxhy9FtoH93eqXWstqUxC68aBG2lC_RaumU9RVnMSbNsu6kFr_gkJwEQjOC5-wJrViJpissKMH3k4eW-efa8CXybxw2nSuoHMgZwoA-Rm0GVk5HiIm2nGfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آموزش شلیک با ضدهوایی به جانفداها برای زدن جنگنده F35
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151400" target="_blank">📅 12:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151399">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
👈
جبهه پایداری افغانستان(طالبان) بادبادک‌بازی را در هرات به دلیل تحریک بانوان ممنوع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151399" target="_blank">📅 11:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151398">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پزشکیان: به جای پرونده‌سازی و طرد دیگران از دایره اجتماعی باید تکیه‌گاه باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151398" target="_blank">📅 11:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151397">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d40b98ab50.mp4?token=AYxHVZ9h_fkMmu96g_lga3zfmg46C1ekWPysllX57IwKSuYQ_jRmfWnAY0RPTyXZqxcA6lHEpUiy-12nuqAAhnZ7dwAg_vQocWus5Hv7dMai3xT0kZBkGn8ox42xe7VgPVgMIkcX0tj4JL2er5L-pMJcO5Xu9eIJJwGNNOl6AEioGxrv5Y7X855GMzN2HhrbdPrsgA4HlDldKVn9N6oI3rFqrpkn-W9x-UCL_-DG8PnJriZmGDy-wEGp5l-Tqyx4vAnD5y7h6TKbHOz5Y4-R7aXXUQFqaqenuzedE67gFmrcLINDPkLe8voNH0HTAj65Fr7rk9ADxAPtrr60D2m9UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d40b98ab50.mp4?token=AYxHVZ9h_fkMmu96g_lga3zfmg46C1ekWPysllX57IwKSuYQ_jRmfWnAY0RPTyXZqxcA6lHEpUiy-12nuqAAhnZ7dwAg_vQocWus5Hv7dMai3xT0kZBkGn8ox42xe7VgPVgMIkcX0tj4JL2er5L-pMJcO5Xu9eIJJwGNNOl6AEioGxrv5Y7X855GMzN2HhrbdPrsgA4HlDldKVn9N6oI3rFqrpkn-W9x-UCL_-DG8PnJriZmGDy-wEGp5l-Tqyx4vAnD5y7h6TKbHOz5Y4-R7aXXUQFqaqenuzedE67gFmrcLINDPkLe8voNH0HTAj65Fr7rk9ADxAPtrr60D2m9UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: گاهی مردم به دلیل عملکرد ما از ما دور می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151397" target="_blank">📅 11:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151396">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
۷ اکتبر ۲۰۲۳؛ روزی که جنگ اسرائیل و حماس آغاز شد
🔴
در صبح ۷ اکتبر ۲۰۲۳، گروه حماس حمله‌ای گسترده را علیه اسرائیل آغاز کرد. این حمله با هزاران موشک از نوار غزه و نفوذ نیروهای مسلح از طریق زمین، دریا و هوا به مناطق جنوبی اسرائیل همراه بود.
🔴
مهاجمان به چندین شهر و شهرک اسرائیلی، کیبوتص‌ها و محل برگزاری جشنواره موسیقی نوا رسیدند. در جریان این حمله حدود ۱۲۰۰ نفر کشته و ۲۵۱ نفر نیز به گروگان گرفته و به غزه منتقل شدند.
🔴
این حمله که به‌عنوان مرگبارترین حمله علیه اسرائیل در تاریخ این کشور توصیف شده، واکنش نظامی گسترده اسرائیل در غزه را به دنبال داشت و به آغاز جنگی انجامید که پیامدهای انسانی و منطقه‌ای بسیار گسترده‌ای داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151396" target="_blank">📅 11:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151395">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d6d557b6.mp4?token=u4I6dnqOAgC60SSmtT28ZTWHQ981lwFCNJnreyO5ND_bwhHy3yMXeMZEWZkKztMFbNpvEjpVVfsA77cCOvcyhwwYzWSaGkieroLYWX6jn7ffivlFLyCppcPUH3g1XAxnwgKmLT4ugY8h9PGz06XuHRjZOue_14BJVjQGul28ksS_QvIME67-bTPgbmJCH6-o-GA2Im1dvDAMIUqCqOmb35_jXODZbAziDCF-YMa7QNOfKZmC1G4lF8oSjdIOOGtq3ydMvb5902rZI8D8c4FOgYmJu03y8a6n_w0F_f8QKR03wNsJHJR8iO5vPP2gSycgvKmmeDXtft8OYTl20fnZnCytGSg34NnJN0YRS7fmG4cEXqIwPOgu3l4t-20tk8Jo6_emPVpIw1h_YCCUnDcE9xljYglk4AWkl8N____0UUGLnAcQYqRvGj-8zZYnjFeA7WGaJmWe0BGeHJvnemsPoq4OtP4MT3WK9h2xqszVGoGdGZZ2RDhmrKdLP18-iAYksjQVUt0cwVu8rnJVnrmtGNExags1pUJ92wSpiP6vz8tABLSeqk0xY7izKPxy6JM-8w6zOGPKCSY7IdynHugoFI-ln8ceYE9Avzx7NFn7kkaJv9BBVdU6rwz_qjyDcQWBnpGOo5YcqXmaHOfzyr3ffKjyRvkXD3cVhLWnC1R_HcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d6d557b6.mp4?token=u4I6dnqOAgC60SSmtT28ZTWHQ981lwFCNJnreyO5ND_bwhHy3yMXeMZEWZkKztMFbNpvEjpVVfsA77cCOvcyhwwYzWSaGkieroLYWX6jn7ffivlFLyCppcPUH3g1XAxnwgKmLT4ugY8h9PGz06XuHRjZOue_14BJVjQGul28ksS_QvIME67-bTPgbmJCH6-o-GA2Im1dvDAMIUqCqOmb35_jXODZbAziDCF-YMa7QNOfKZmC1G4lF8oSjdIOOGtq3ydMvb5902rZI8D8c4FOgYmJu03y8a6n_w0F_f8QKR03wNsJHJR8iO5vPP2gSycgvKmmeDXtft8OYTl20fnZnCytGSg34NnJN0YRS7fmG4cEXqIwPOgu3l4t-20tk8Jo6_emPVpIw1h_YCCUnDcE9xljYglk4AWkl8N____0UUGLnAcQYqRvGj-8zZYnjFeA7WGaJmWe0BGeHJvnemsPoq4OtP4MT3WK9h2xqszVGoGdGZZ2RDhmrKdLP18-iAYksjQVUt0cwVu8rnJVnrmtGNExags1pUJ92wSpiP6vz8tABLSeqk0xY7izKPxy6JM-8w6zOGPKCSY7IdynHugoFI-ln8ceYE9Avzx7NFn7kkaJv9BBVdU6rwz_qjyDcQWBnpGOo5YcqXmaHOfzyr3ffKjyRvkXD3cVhLWnC1R_HcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زد و خورد و درگیری در پارلمان ارمنستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151395" target="_blank">📅 11:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151394">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=R3Lwy50hK4PduO4RF_bJ6hGlBGmoERDx077FHgEnbYKZDi4jAptbc8Qah3Yxarcw5e5unu0oPQ5p7PP3tY6J4FdLce7wWp2XasEqN06HI5UR0uJic-aeCY9Tql4S6tPJOB8u-XOU70KsDYFtmQcfXyNmc621jGEJQKNPfSaAsP4D9PD6Tya8wCyitQHJYX4GpH8oO3qtCJRUutevWXBywiPVQPqHFzuq355e7pRJlr19Yt8d9J56GQKaQ0DHauvb8UeGI96IY8vkZacfWizh0xGhOtwPQzQXCmyvzfowxaGrHH_CUXAj3YGA2xHz06tUpWCyv0jJGi57We6Xf8726g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=R3Lwy50hK4PduO4RF_bJ6hGlBGmoERDx077FHgEnbYKZDi4jAptbc8Qah3Yxarcw5e5unu0oPQ5p7PP3tY6J4FdLce7wWp2XasEqN06HI5UR0uJic-aeCY9Tql4S6tPJOB8u-XOU70KsDYFtmQcfXyNmc621jGEJQKNPfSaAsP4D9PD6Tya8wCyitQHJYX4GpH8oO3qtCJRUutevWXBywiPVQPqHFzuq355e7pRJlr19Yt8d9J56GQKaQ0DHauvb8UeGI96IY8vkZacfWizh0xGhOtwPQzQXCmyvzfowxaGrHH_CUXAj3YGA2xHz06tUpWCyv0jJGi57We6Xf8726g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ابداع یک دین جدید توسط نبویان
🔴
نبویان: نماز و روزه و گناه و... مهم نیست همه کار باید کرد تا نظام حفظ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151394" target="_blank">📅 11:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151392">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhwvqkuXwLviZT0XU7esMZpWmMpH6HWVy2nM7vdT4JPWsgcHAeOky7xcXcRULp0O-Ec6YqRqaZoS9m935UuvUi2-u97mMGOrOcDDAEH_V3_6D4-ZDiujUbGVHka6ExNjdw4PaA9O4uun2CuIfjgS7OcV24_on2I1q_IH675wjXGXHJUaFPkNIv9QIrxRjZULH3YaEoyeOqoHuz7IOD4DO9LJbS2CqbzZ4x0c_R6hDxQqymT4I2lEnfqZDonAIvK5difFheRiblJRSFkfesTLhLirz6ozC1Bvb5J3sbiVjFwVc2IkPWT4gTguafXAiUqIDWwINuj32N5TCJ1wUKJz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ciTcnNcSjHuSX33WW2PEQWOGBG2ggpTMdrVzkutS_AtDN8anWNERB_PMmNilH1loZ4kTnYkfjbdetA7wG-5hG62X65aMLw5hfL2w8G1GrIT4aoYC3cWZv2Vp-P5jG2XipPYYsTJBLAkTa6f6tXmA_f_bYqIiLhvNe6JYQQn9gowU5bBdF3HjQDka7V27-fRp1TdKBlqh1tp9FoO5KDY0Up0vMncn9p4V6t-_ZBXncwcQwF8DhX9vX33O94cUaHaT9y1UjEQpkMIqVE8-pFRErJBM-dInW_eu65qFwuMdJGOXU6dnZmCy-hoQSdEJBTMYcL-lh4lQcOKDPsIDN5tKBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اطلاعیه یک تئاتر قبل از نمایش
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151392" target="_blank">📅 11:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151391">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8bzVplfP75NhFa-hIj11gGqiC3VDrVqU3EjzxZwaDPrvLoXERmsDNSRYV8C1roVgrgRp-bZrcv4fdZRmPCmkRA0QB0uzal08MPnGRA3VfHxd6l27pO2cAUUC6It4ee4FkoxPI49Dt21_AAPxGdOHE2KtQH8ufpjQ9uA9clNwKiiT9s7eZ4KnY4avqTZumDwbsuOsN0ipnkRZNN67c1IYz-qYApn9Spm31zhrU47-nQ8ksfyVUyclWbK_KgiUsMb5JuB0KV8E0OEP224Dpw1u5exRIUa1JW55r-2vgXH5OjhIBF3w9vMqDge-kWN_E_l1wjeTs0GBd-CYzDmRr3FHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای سعودی و بریتانیایی برای سوخت‌گیری به سمت یمن حرکت می‌کنند تا حمله‌ای را آغاز کنند. همزمان، تعداد زیادی از هواپیماهای آمریکایی در تنگه هرمز، نزدیک به سواحل عمان، مستقر هستند تا از عبور کشتی‌ها اطمینان حاصل کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151391" target="_blank">📅 11:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151390">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
آمريکا به قطر گفته ایران اورانیوم رو باید رقیق کنه و هرمز هم کامل باز کنه بعدش مذاکره کنیم.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151390" target="_blank">📅 10:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151389">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbda2a8b80.mp4?token=atIdyM1dWQ9ULlB2__6zqLOniNG1WsFhe5kZnC-iOTUQjcRuCyoz1fP2rtc7aQhFQeYQoa3t9xmztlxRPb07U_ldidPW3Z7ukovdsMex00qeeuWoQDBMCEwnz1ib9U5ONnBqhmkDG_w1YFxn7UWE1bVnDA6oll_MxiOMQVEaVvVuL3F3KUS78u_jc0Aaovq4dkw-Vt8OirDnI-cHwoA22SoqarWzBMO0IhpYA1LqEvA-cYjKKTtDKS_KhkSaZFdboeqBnGJja9ZOHpzA7aWwsY-ou1jYAoPOMAtrT4rRKkIuzY44WP5WovDMfBFD2LtR8Mx4MmPDo3bwiYgkzsO2aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbda2a8b80.mp4?token=atIdyM1dWQ9ULlB2__6zqLOniNG1WsFhe5kZnC-iOTUQjcRuCyoz1fP2rtc7aQhFQeYQoa3t9xmztlxRPb07U_ldidPW3Z7ukovdsMex00qeeuWoQDBMCEwnz1ib9U5ONnBqhmkDG_w1YFxn7UWE1bVnDA6oll_MxiOMQVEaVvVuL3F3KUS78u_jc0Aaovq4dkw-Vt8OirDnI-cHwoA22SoqarWzBMO0IhpYA1LqEvA-cYjKKTtDKS_KhkSaZFdboeqBnGJja9ZOHpzA7aWwsY-ou1jYAoPOMAtrT4rRKkIuzY44WP5WovDMfBFD2LtR8Mx4MmPDo3bwiYgkzsO2aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جانسون، رئیس مجلس نمایندگان ایالات متحده، درباره ایران: ایرانی‌ها شرکای مذاکره‌کننده قابل اعتمادی نیستند.
🔴
آنها دروغ گفتن را بخشی از دین خود می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151389" target="_blank">📅 10:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151387">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd6dbe0190.mp4?token=ue8dyHpQiaw3xPdOSVo-HstmdKIIFpHD6M3pntAn7YAQ_LMM29Yplaa3Fhho8KYx0lQEevMqCMZIq57I136t4HnK8--ixDQynZG1WOPj-1YljaG4QBJ5kidV5jkAfxeBemXlRESvH9aYji0eb3M9dDCis6XzHKwWtJ3cCsMnQzytCk4YZBznJFLjsV3r1J3jZfgZVDozrsYLzAiAShXHlGmWgmow0-jrDhRSR0W-9P94PKtgsqHLFQMlzPhTIYcS7MB2aIKVm6137Krm2UufO4WE2t5sVN5vMAbhFG0W-QXHDU1uewoLpL5Roe7ZCQ_rCAa1zc2wpFOouQcE_kxNeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd6dbe0190.mp4?token=ue8dyHpQiaw3xPdOSVo-HstmdKIIFpHD6M3pntAn7YAQ_LMM29Yplaa3Fhho8KYx0lQEevMqCMZIq57I136t4HnK8--ixDQynZG1WOPj-1YljaG4QBJ5kidV5jkAfxeBemXlRESvH9aYji0eb3M9dDCis6XzHKwWtJ3cCsMnQzytCk4YZBznJFLjsV3r1J3jZfgZVDozrsYLzAiAShXHlGmWgmow0-jrDhRSR0W-9P94PKtgsqHLFQMlzPhTIYcS7MB2aIKVm6137Krm2UufO4WE2t5sVN5vMAbhFG0W-QXHDU1uewoLpL5Roe7ZCQ_rCAa1zc2wpFOouQcE_kxNeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسپوتنیک: یک هواپیمای مسافربری کانادایی و یک هواپیمای مسافربری آمریکایی در فرودگاه لس‌آنجلس در ایالات متحده با یکدیگر برخورد کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151387" target="_blank">📅 10:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151386">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffca39c1b.mp4?token=Nz6DuYqQmX_xE22emyNZfFIyzsYxP-6GWLkRdjkMSj_0VCZTN3AAMu1DOjZHxLOcW7CyaHsIEyxgBM8dSLSiPXpS0Zo3J9Z2CtpkzRFIK4GU4uK85FypcHoHxD2119Teidhquz29HECGuD1RfC5HaE5ImxsW-I5F1ApNgzb_XfltSGH0Bl2drS2Rjun760R1zQUBXtUJuobzSrkzku_uERR0LnlfkR9FE3MtaIAyoeQF2HFIg3eZiPJuA5A8sU4SRSayBIbamepuHUi-aGojAmKgYs6uvqyUh5NzpeH3tGX-yMsvPHOZLkv2YNqsFprTpNakDJerMd0XvQHQGaI6TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffca39c1b.mp4?token=Nz6DuYqQmX_xE22emyNZfFIyzsYxP-6GWLkRdjkMSj_0VCZTN3AAMu1DOjZHxLOcW7CyaHsIEyxgBM8dSLSiPXpS0Zo3J9Z2CtpkzRFIK4GU4uK85FypcHoHxD2119Teidhquz29HECGuD1RfC5HaE5ImxsW-I5F1ApNgzb_XfltSGH0Bl2drS2Rjun760R1zQUBXtUJuobzSrkzku_uERR0LnlfkR9FE3MtaIAyoeQF2HFIg3eZiPJuA5A8sU4SRSayBIbamepuHUi-aGojAmKgYs6uvqyUh5NzpeH3tGX-yMsvPHOZLkv2YNqsFprTpNakDJerMd0XvQHQGaI6TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز عده ای تو خیابون پاستور جمع شدن و به پزشکیان و قالیباف اعتراض داشتن؛ شعارشون هم این بود که «پزشکیان و قالیباف رو میدیم، اورانیوم نمیدیم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151386" target="_blank">📅 10:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151385">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
بانک مرکزی افغانستان در گزارشی خبر از شکست دلار توسط پول ملی این کشور را داد
🔴
در این گزارش آمده است که:
🔴
سال ۲۰۲۲ 1 دلار = 90 افغانی
🔴
سال ۲۰۲۶ 1 دلار = 65 افغانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151385" target="_blank">📅 10:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151384">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra9sF6KDsW-OK2Ifng5ZroxLxj2yGtR2tZ2I2UZVyezOg6zsP4LUhzUN7Ao-03LLG2t4K0H4Zd-qpOQXT8lyYSlmJdXoLq0txWY_8sN8MqdBq6u4nPuSGVJlMHVnHRo5KtwYqQkX-KnEnDveqYCpUjvnmyf7sHrYgPdNlMT07OBOKZUoG6Z7xxx5_7pPN8E2Wj-T2C4LOKm9xB-Cg-skw6Kl29cgjVU238xVE51oZllWe2e-LINUQEFhLt1CANtieEuWotgbZjKjtqctiD2fGT4pVy5wmG5UL5aXispV-Mqk_NWqxOqDH5Yj9mZwZjRzBJCJv6rGY3b-vGFYQWLQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور اقتصادی قالیباف: جنگ بدون تحمیل شکست اقتصادی به آمریکا به پایان نمی رسد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/151384" target="_blank">📅 10:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151383">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مدیرعامل آبفای تهران: ذخایر سدهای تهران نسبت به سال گذشته ۱۵۵ میلیون مترمکعب افزایش داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151383" target="_blank">📅 09:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151382">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن: فرودگاه ملک خالد در ریاض با چند فروند پهپاد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151382" target="_blank">📅 09:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151381">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رضایی، عضو کمیسیون امنیت ملی:
نزدیک به ۸۰ درصد از افزایش قیمت ارز، منشأ داخلی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151381" target="_blank">📅 09:35 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
