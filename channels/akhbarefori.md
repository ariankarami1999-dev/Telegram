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
<img src="https://cdn4.telesco.pe/file/gUkzXDvRQKSYAdTwVyn94PbukzFkyfYOnyG4B3Nms8L9ycX_4L241Igcs7NVU2qYxC0WwVLSLCAEXmupKppzVOVsA_2FUXfuAThYKx8wiEun4rKRRXgUbHgpxBhDPSybJETOzS6gGY3p4KJSyrKNSH0-MEqu4lS1mi_GnbqsXMKL10h5pte2pFj_1gUsSatDK0MtJMbCM5GXKiOxoJ5CHn8_DpAiC8eQ_FOn7Tpak-wW8tx1I_yjhmuCXZCdJ9WRLGGPitz2U_Tsm172xgFB0BJTG8FsQ9lc_3iLN471sWVF7XGNqXJ57wO7KHTU4XKzvd9YT3voqL1IRWuutB0OXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.04M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 02:05:02</div>
<hr>

<div class="tg-post" id="msg-691342">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcAQmr6ItzFrxc7qb6T8Lcz1uiwE62dM_ak1jT_pWnJ6KkQaIL1mZfAsaALcc511Cv78kvIK14byhFa5XavmnMWuc-hcatMjZ1F2b4UB1Dz5rEsvA-GGbEnbPNsRpXCFU_MXg47TqujLYiJbQoqMbRPc-Mxp7bnUn4WEGncqtZOGjdd9KqE2iIuBxzBqhrNFG2AXylQvKwYLHeykmAYEXu4uqFDN5WKT7Uik_3ZHzoIye8Lm-X7gIT2jx5egthE_9Q6aFjmhhxfX178rDYrt0LQ3xbsNt-FK0aYS6xmuj6LM9Jw83Mja8MjQ838kZ51zxSfXkVrkWgt2Q8Dtp79yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج دستگاه تست قند خون دیاباتان SMM 1000 +دستگاه فشارسنج بازویی دیجیتال
یک ترکیب کاربردی برای کنترل راحت‌تر قند خون و فشار خون در خانه. مناسب برای استفاده روزمره‌ی سالمندان، افراد دیابتی و همه‌ی کسانی که می‌خوان وضعیت سلامت  رو با خیال راحت‌تر پیگیری کنن
🔴
قیمت: 2580 هزار تومان
پرداخت درب منزل
خرید
👇
https://memarket24.ir/product/brief/63615/180124</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/691342" target="_blank">📅 00:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691341">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aafb71c373.mp4?token=dNBJ8UFFbw6zh0ShKf0eMQVC2xia3f9Tt-JQDjmwwzeOakazg3U8lbEQq7c1n6uO0TTMTFYJu3XAtPDRJ0u4-5dezWrHOAHoGfHZ4vyhJ5zONRJbvlLykTW47nCUslkA1DBjgglLnugR_aRwu3ucA_xeohQNo82KyJzjVBHpS8uXQW_utyotaXEffhHe4jbRwYmcYL0nydNq8SkSysNhjP4FrJSPtZaOYLUp9jQyjF2UnphbTc4rRWhPOolLKz3rLvFN0ZuTsfPb-7JDOKEFLEJ7N0IK0peXdomyqL-mDQp9qQkd9fT1kpkAjqMUjFcPE8PWaREESYwl1GLODCsd3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aafb71c373.mp4?token=dNBJ8UFFbw6zh0ShKf0eMQVC2xia3f9Tt-JQDjmwwzeOakazg3U8lbEQq7c1n6uO0TTMTFYJu3XAtPDRJ0u4-5dezWrHOAHoGfHZ4vyhJ5zONRJbvlLykTW47nCUslkA1DBjgglLnugR_aRwu3ucA_xeohQNo82KyJzjVBHpS8uXQW_utyotaXEffhHe4jbRwYmcYL0nydNq8SkSysNhjP4FrJSPtZaOYLUp9jQyjF2UnphbTc4rRWhPOolLKz3rLvFN0ZuTsfPb-7JDOKEFLEJ7N0IK0peXdomyqL-mDQp9qQkd9fT1kpkAjqMUjFcPE8PWaREESYwl1GLODCsd3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت ترامپ از افشاگری رسانه‌های مستقل
🔹
ترامپ جنایتکار، در اقدامی خلاف قوانین بین‌المللی ورود خبرنگاران شبکه‌های خبری سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و وبگاه پولیتیکو به کاخ سفید را ممنوع کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/691341" target="_blank">📅 00:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691340">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f7dfdd8c.mp4?token=L3K3BMGlBikatIedVIhhNax7VrT6BTNSM6_3o6-GWDA7R83JsKrhCnyH1wzPFA8ghCiqEy559Ws6tRkjn8eHFs7FqBbKadQTvkmHVZGlxBrjPhJFoXxjBpBNOkg8Wb7E6Q_s5fxKv0VGqO1fHYsM06ZMhbBGnssQ_mTVg_LP2k7NeN1oTm0ZNFhUaK7U347rEyo56Recduc9x83MHfhQQvYdeAOSyISGFPIM-JkHL88149mq91Fso-NuAtcXq8V_n_wd3bQq-kMD-Nx3Rbjow3_qkFkiSlwG28ImKaZ7KwqphZySTB0KRWwMsyDmvhAKoQUziA7HdDJPGj2aMN6U0DzwwZv2vMG1NvTzP7PRxEmuLRxL27VplcvOhT0gpA4rEE1_q4jf_CoGB-JLDvmY6RDeGZDJux0X6He09OsaVF5VBnT60K_Y_xiKKoJiTBMpumdrSKLnEKpMWc3QOIFZNKre9FiwJTZhgDWKr9MunJbo190qBwPV649A6NIGmg2ByOTKFCWlAVOT7T6hb9cHSTBABIgk9oEMi8NX-Mmr0QFA3Qev8yV_zjgm3C7RqQWV-ffVU2qBoy9pLcdxNUJudscEX5yMEFUilji0at5c0_XY4ksZ9Lp3FwkSdGgMAeyQ-PsSXTDE7EHn2_Cz5zpJJWrUPEIeqKYns05WxZKfo4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f7dfdd8c.mp4?token=L3K3BMGlBikatIedVIhhNax7VrT6BTNSM6_3o6-GWDA7R83JsKrhCnyH1wzPFA8ghCiqEy559Ws6tRkjn8eHFs7FqBbKadQTvkmHVZGlxBrjPhJFoXxjBpBNOkg8Wb7E6Q_s5fxKv0VGqO1fHYsM06ZMhbBGnssQ_mTVg_LP2k7NeN1oTm0ZNFhUaK7U347rEyo56Recduc9x83MHfhQQvYdeAOSyISGFPIM-JkHL88149mq91Fso-NuAtcXq8V_n_wd3bQq-kMD-Nx3Rbjow3_qkFkiSlwG28ImKaZ7KwqphZySTB0KRWwMsyDmvhAKoQUziA7HdDJPGj2aMN6U0DzwwZv2vMG1NvTzP7PRxEmuLRxL27VplcvOhT0gpA4rEE1_q4jf_CoGB-JLDvmY6RDeGZDJux0X6He09OsaVF5VBnT60K_Y_xiKKoJiTBMpumdrSKLnEKpMWc3QOIFZNKre9FiwJTZhgDWKr9MunJbo190qBwPV649A6NIGmg2ByOTKFCWlAVOT7T6hb9cHSTBABIgk9oEMi8NX-Mmr0QFA3Qev8yV_zjgm3C7RqQWV-ffVU2qBoy9pLcdxNUJudscEX5yMEFUilji0at5c0_XY4ksZ9Lp3FwkSdGgMAeyQ-PsSXTDE7EHn2_Cz5zpJJWrUPEIeqKYns05WxZKfo4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفت و گاز چگونه به وجود آمدند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/691340" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691339">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای وزیر خارجه ترکیه: شرایط جدیدی برای مصالحه بین ایران و آمریکا پیشنهاد شده؛ امیدوارم آن‌ها این شرایط را بپذیرند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/691339" target="_blank">📅 00:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691338">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed220764ce.mp4?token=pGblxxoXO0DKKf11IyYFwGthCZVn-P2CUOEW2WOT9hVrV7FUIx4tSfj_U-QugjUXCu861k2NDAl09TvOqCPHQfW_X5UucUfIf5zmwBf1sA6scJLcp0Uj1mLjGPgXFYKYlr0os6PJIEoO_fl3PUenE5QbTtXt3HJZNhdLj_YCxvyTwhVNFa7vRMtt7Tijo2npQDsO_3SOe5Tkz5e2Ki7-dAmS72CTzEK47i5oKXiBIMBihuPCHBx6Ia-o6VgDSfiK5UXb7u3NX4LbfuY3KpQ-GR35RO2aZrGTQT51c4sapSV24l0vuCLRTUzpK0nifEwJ9bm0I2aFG8tz_FR44sUkdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed220764ce.mp4?token=pGblxxoXO0DKKf11IyYFwGthCZVn-P2CUOEW2WOT9hVrV7FUIx4tSfj_U-QugjUXCu861k2NDAl09TvOqCPHQfW_X5UucUfIf5zmwBf1sA6scJLcp0Uj1mLjGPgXFYKYlr0os6PJIEoO_fl3PUenE5QbTtXt3HJZNhdLj_YCxvyTwhVNFa7vRMtt7Tijo2npQDsO_3SOe5Tkz5e2Ki7-dAmS72CTzEK47i5oKXiBIMBihuPCHBx6Ia-o6VgDSfiK5UXb7u3NX4LbfuY3KpQ-GR35RO2aZrGTQT51c4sapSV24l0vuCLRTUzpK0nifEwJ9bm0I2aFG8tz_FR44sUkdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نبستن کمربند ایمنی، کمک‌راننده را به بیرون خودرو پرتاب کرد
🔹
در حادثه‌ای در ویتنام، یک کمک‌راننده که کمربند ایمنی خود را نبسته بود، هنگام تصادف از داخل خودرو به بیرون پرتاب شد و آسیب دید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/691338" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691337">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuphLmsCDwopeHcJLSH-UHI3wQaxXaC81CVdmgKMvwTGxzBOV4DwO6a-vRgbFY0SJoqPkAZg-uu2Gp1hvhSuCcQ-CJHoKI3RbJ9skxilz9mOmWxeGbQO1wqoYyRCEm-SsezYLtmNYt8oBG-tGmNSKPejH-XdZL7v1lKPihgOI3JukxWVq-pfGr09RB-gwItFm0DMMiP2SNTd49bLMTKAVQoI1ZmM9kXG8YXf-X5dVx2KOuAX_dvqwQEm9D17mUxjy25HohoJFu9wlk9c_3_N2PLEH8UUUvn4cpOHkh6pHEUnrcebVY2vx5XweCSawBphAK2H1J1J9Jkln40zCAmb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/691337" target="_blank">📅 00:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691336">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ائتلاف سعودی: ریاض هدف حمله موشکی نیروهای مسلح یمن قرار گرفته است
🔹
ائتلاف سعودی در ادامه مدعی رهگیری و انهدام این موشک شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/691336" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691335">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
امارات میوه و تره‌بار صادراتی ایران را برگشت زد
رئیس اتحادیه ملی محصولات کشاورزی:
🔹
بیش از ۲۰۰ کانتینر یخچالی ۴۰ فوت حامل انواع میوه، تره‌بار و سبزیجات صادراتی ایران، از سوی دولت امارات متحده عربی برگشت داده شده است. هنوز دلیل برگشت این محموله‌ها از سوی دولت امارات اعلام نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/691335" target="_blank">📅 23:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691334">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/691334" target="_blank">📅 23:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOv81J_dCZbzlgf6Cc2_W04alHSj89lo_RmVNCe7eAq5vqC8e0LchTg70vigN6A6ti8-Xerz63zU-W8DQWK3ph6IMURLw2lGSOiT1OJnI4cadEInO9SqdEa4t8jtcD-nAOJcP5E6gbLSqGlRvkyaHnaB1qSZZfiyV8gBNsvF6soCz354pWd__Nhshqs3MtqIHSDrx_T7-fVFdf9K9xNfa2DCpB0Uo5R29i4c-GlO-bOu9vk-eiAikS7NVh1F0sPhI_Q9Tn9pqGsq24A4RkIrkM7ti6yABsjQsCCk7SxqZNNrHXX1CsYUT7ftzG_iyD3g1IVs4YjAeXNpJcpHvgwPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
جعبه هدیه «ختایی»؛ یادگاری از حریم ملکوت
این جعبه، مجموعه‌ای نفیس از تبرکاتِ آستانِ مقدسه است؛ ترکیبی از سنگ‌های متبرک، تسبیحی با عطرِ مشهد و عطری آرامش‌بخش، تا هر بار که به آن می‌نگرید، قلبتان راهیِ حرم شود. هدیه‌ای فاخر برای آنان که عشقشان، زیارتِ بی‌واسطه است.
✨
مشخصات محصول:
▫️
نگین: قطعه‌ای از سنگ‌های متبرک روضه منوره
▫️
مُهر: قطعه‌ای از سنگ‌فرش صحن‌های مطهر
▫️
تسبیح: سنگ‌های یادگار مشهد (سنگ متبرک)
▫️
عطر: رایحه ملایم با طبع دریایی
💰
قیمت اصلی: ۲,۴۵۰,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۲,۱۰۰,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/691333" target="_blank">📅 23:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b559054a3e.mp4?token=liNcmKFfDYhdmYwZjN8bip9pe7R59IurfEP4TU5N-Rt9YM1RGsLdRPUlZADCkXtl7lwiMF1JuoksDwoT4zngyjhwKPHmwZqOPANM9QS58DZBJQtvTe98A9C_C3LGXfI6QTORSI6t_V5CAM4s5LD-h7Uy8OptYBboEc-1tWVSFj01zmAs0WUWMmQwJ-Rd6vW2qbg0XHWMvGa9cM-uAH7oSx2ZVMy5pe_pYAn_CxTdyRMNDeAjtBg0Gtf3mziSZo4C39UyaYYF3tjfeUD0eloSDyc-HSGuktAGHjC7r3li0ItVk8-vUE8ZNQ1hM9pfTMgfgTCqha9u97iQYuNWtqgyj5oYGv3zM56aDP9XlCVQiCwIM76-JXOEBigNRAc72IglbEp7PGfHa8M6T6GUQkVF_SZCf6IL27KSzehB8JvrTVQd_HpZEKTp8HuVK-jjcoG9S_R_Q80Cf3iNsCHV_tZPj5Xtpg-lyVfCKMZ2l1Rr2cM_zCHK7n3ThNoFoBqoGVDWt6-nV0HggSaSRJFNREqGmy5OCGAdtyh9MbIq14A133ox64HyHM3qNn-glfAXEaIFdvIHg-5bAZl4cAA9O_T631Bkw6qYiUOJpYuQaAL1sGsTIhFYj3tQm9UEAUPyXut0PmQDVFzxyzfR83MDsX0-7w7gk39Cqn3NSp98-vHw_Mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b559054a3e.mp4?token=liNcmKFfDYhdmYwZjN8bip9pe7R59IurfEP4TU5N-Rt9YM1RGsLdRPUlZADCkXtl7lwiMF1JuoksDwoT4zngyjhwKPHmwZqOPANM9QS58DZBJQtvTe98A9C_C3LGXfI6QTORSI6t_V5CAM4s5LD-h7Uy8OptYBboEc-1tWVSFj01zmAs0WUWMmQwJ-Rd6vW2qbg0XHWMvGa9cM-uAH7oSx2ZVMy5pe_pYAn_CxTdyRMNDeAjtBg0Gtf3mziSZo4C39UyaYYF3tjfeUD0eloSDyc-HSGuktAGHjC7r3li0ItVk8-vUE8ZNQ1hM9pfTMgfgTCqha9u97iQYuNWtqgyj5oYGv3zM56aDP9XlCVQiCwIM76-JXOEBigNRAc72IglbEp7PGfHa8M6T6GUQkVF_SZCf6IL27KSzehB8JvrTVQd_HpZEKTp8HuVK-jjcoG9S_R_Q80Cf3iNsCHV_tZPj5Xtpg-lyVfCKMZ2l1Rr2cM_zCHK7n3ThNoFoBqoGVDWt6-nV0HggSaSRJFNREqGmy5OCGAdtyh9MbIq14A133ox64HyHM3qNn-glfAXEaIFdvIHg-5bAZl4cAA9O_T631Bkw6qYiUOJpYuQaAL1sGsTIhFYj3tQm9UEAUPyXut0PmQDVFzxyzfR83MDsX0-7w7gk39Cqn3NSp98-vHw_Mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکمه‌های لباس چطور ساخته می‌شوند؟ فرآیندی جالب پشت این قطعات کوچک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/691332" target="_blank">📅 23:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b57bab2cd.mp4?token=uetLUyqcG8fcU7Frc85d3cCLAZnvoOb2i__pKyLI7O6p8U3vB6_6yxSdbMHtDCyG8ezEWjzKabaEbJ-7tSJzxjsXkklZstLrQoE8hjZnf-q0EyNz2bNnANvYKvPIkL1g51jFMHOWCRV2Mz_tPnQT5A0X62tLnLG6BaswvkyHSUGVRy6hOMezTiwntQKzF48_2SUaR8FOFABXqeI0D8-7M3t7Svg_TFLcXsZ3MnYIbCYnfHiE0pXa31qSbpVQuYYwW2F9BX1SNPZOjAMgecmVDlcRbse2yULGxeOWR_HjLbVzPPw8K1hZVPbrAqABJ9Yqxwb8KUc9F-wrVdTY79I6ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b57bab2cd.mp4?token=uetLUyqcG8fcU7Frc85d3cCLAZnvoOb2i__pKyLI7O6p8U3vB6_6yxSdbMHtDCyG8ezEWjzKabaEbJ-7tSJzxjsXkklZstLrQoE8hjZnf-q0EyNz2bNnANvYKvPIkL1g51jFMHOWCRV2Mz_tPnQT5A0X62tLnLG6BaswvkyHSUGVRy6hOMezTiwntQKzF48_2SUaR8FOFABXqeI0D8-7M3t7Svg_TFLcXsZ3MnYIbCYnfHiE0pXa31qSbpVQuYYwW2F9BX1SNPZOjAMgecmVDlcRbse2yULGxeOWR_HjLbVzPPw8K1hZVPbrAqABJ9Yqxwb8KUc9F-wrVdTY79I6ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات رزمی باورنکردنی استاد ۸۰ ساله در برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/691331" target="_blank">📅 23:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691330">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
معاون توسعه مدیریت سمنان: روند تعطیلی پنجشنبه‌ها در استان سمنان تا پایان سال‌ جاری تمدید شد
#اخبار_سمنان
در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/691330" target="_blank">📅 23:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691329">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
یک منبع در وزارت حمل و نقل دولت صنعا خبر داد از دهم تا هجدهم سپتامبر، میانگین به صورت روزانه، ۳۵ کشتی از باب‌المندب عبور کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/691329" target="_blank">📅 23:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ترکیه: آنکارا تحت ائتلاف مکه، نیازهای نظامی عربستان در زمینه فنی را می‌تواند برطرف کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/691328" target="_blank">📅 23:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840966b12e.mp4?token=k9pqZZKiVSSGJazqGY-lo5WswS5_AtoSZui-ob2eotndBda8JGgG9OVuTvHbnwAq7cAoiSyBjuAxMzhHn0VrF0x_MWe1epq8PhI6MoxQlaSwq8rDLuMvUnKyzWW5CtKz7cv_hSffsnBcjYqTOgsUyU7wSmtjJckXw-3jn-m4WG5vRwoEsrMkhf-t1SmXxC46o3jZODuQfVhG9uDooCOOGH71dxXGpn4s_V0sqTPvYkN6a2TJ8oUce-o11A-afLU6iFwq1fX4SC3HjnTDYpDpsxzKFErASM9OjQEQIxq1NOkrqIa5FnzHBaxnjKVE9tO0RyKaK9GadiVqKRqDIp03OEAOv2ToErn5JXoP57HSr8SLihQyEvbo6aNPS6naa8rAzoFjfy6DfET50GJcav7YWcdx3OvoFmyWVMBCrTPZcd0lLETj7-nUzt8wgyHyfa5GNB42rdo8w1QXDuhx2NT17aghLTtTAGjJQ9N6i0VuBZSuT7PHGZ5PzfyLzKKwTCD8VfMoOsRyEi0vdDz8Gv06dVbrW3rsGBG6s0LHHw-inVep0AWfU5-fSVfd8u-w7a6GuHJFydzhCBBMevCQ-5tD6cHrmAMm7_VaPZ5i5r5-UfdlT9DQlifgR0EXKW-s4uYAzEr3zevH4dQFpkyz3TtWsVjkvDQHVqmeKrxrs_9Yyfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840966b12e.mp4?token=k9pqZZKiVSSGJazqGY-lo5WswS5_AtoSZui-ob2eotndBda8JGgG9OVuTvHbnwAq7cAoiSyBjuAxMzhHn0VrF0x_MWe1epq8PhI6MoxQlaSwq8rDLuMvUnKyzWW5CtKz7cv_hSffsnBcjYqTOgsUyU7wSmtjJckXw-3jn-m4WG5vRwoEsrMkhf-t1SmXxC46o3jZODuQfVhG9uDooCOOGH71dxXGpn4s_V0sqTPvYkN6a2TJ8oUce-o11A-afLU6iFwq1fX4SC3HjnTDYpDpsxzKFErASM9OjQEQIxq1NOkrqIa5FnzHBaxnjKVE9tO0RyKaK9GadiVqKRqDIp03OEAOv2ToErn5JXoP57HSr8SLihQyEvbo6aNPS6naa8rAzoFjfy6DfET50GJcav7YWcdx3OvoFmyWVMBCrTPZcd0lLETj7-nUzt8wgyHyfa5GNB42rdo8w1QXDuhx2NT17aghLTtTAGjJQ9N6i0VuBZSuT7PHGZ5PzfyLzKKwTCD8VfMoOsRyEi0vdDz8Gv06dVbrW3rsGBG6s0LHHw-inVep0AWfU5-fSVfd8u-w7a6GuHJFydzhCBBMevCQ-5tD6cHrmAMm7_VaPZ5i5r5-UfdlT9DQlifgR0EXKW-s4uYAzEr3zevH4dQFpkyz3TtWsVjkvDQHVqmeKrxrs_9Yyfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستین اگر آب هویچ یک روز بیشتر بماند، باعث ایجاد سلول سرطانی می‌شود؟
در این ویدیو ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/691327" target="_blank">📅 23:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691326">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔹
از داغ‌ترین خبرهای امروز و امشب غافل نمانید
🔹
🔹
ترامپ در جلسات خصوصی درباره جنگ ایران چه گفت؟
👇
khabarfoori.com/fa/tiny/news-3246285
🔹
استانداردهای دوگانه غربی درقبال اعتراض؛ از تهران تا لندن
👇
khabarfoori.com/fa/tiny/news-3245872
🔹
ایران برای پایان جنگ ۳ شرط گذاشت
👇
khabarfoori.com/fa/tiny/news-3246417
🔹
افشاگری تکان‌دهنده خانم بازیگر: ازدواجم با این چهره سیاسی دلیل خانه‌نشینی اجباری‌ام بود!
👇
khabarfoori.com/fa/tiny/news-3246265
🔹
دلیل حذف صحنه‌های جنسی در فیلم‌ها چیست؟
👇
khabarfoori.com/fa/tiny/news-3246406
🔹
خبرهای جنجالی هر روز را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/691326" target="_blank">📅 23:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/691325" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">گزارش بازارها شنبه ۲۸ شهریور ۱۴۰۵
ریزش عجیب بورس
طلا ۲۴ میلیونی
ورود پول به صندوق های نقره
@Titretejarat</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/691325" target="_blank">📅 23:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b0a0ab95.mp4?token=QnQHi2wDbtUU2tkbXb9Q-Xwxm8llvZECobUuaOZi2fBfWASTGHGdqGhN-pUt0tC3Kif24UZinqaDMhXOxBf8A4SAonOVIgKeJzM40iHaQz14KvvN2YGu7dk6NOyzHZUwqXoqLgi24XQjGfbpcT0MoXMyiZwzfH15OeI7FEDffuWq10oty0A_Gh3uFDc3J35Hg9d_AC8TLm8Wp3GypDWFD9mddn97osnj3uXCdXQU2Bv41rc5ziUM7X1g0R-Y7A6fpTBoDOCW69yj4G484Ic1VkPtsXeteFe6I3X7xTuY6i18Zk_3amS3vV7dokYNdqXR1zRFAVHPzD5ctAH_BNUNWRlAOlnM_JRo6p924ZIEHiWYIwqajrJUWJ4l5H4jTBpraeOMSp34RQ17tIYPzdzpPNKVt8F-jrZEG1Xh39KsvUt6oVp7PT0xT3rbvnDqrX6KVrBH9CutvJpqxjNX9E5Lu2gIQfSqHX_PqOvGngNafQj25A1oCY4pL3eqSwa8lrhUi91nuL-4vzFDdYy7RzNbDjRXa7c7iC4iO3yV-e73eqo2fdgIyWdtpqpPUf1IgY0S_WOXSfsJy2Ut1TMpFJu0LAYJlMsriDRgSfVLwRalV3uNEJqFtXdIyDH8ddmh8O4h0e1ndOaHgnDy80FHNi0tJ63e3MHlemGdt9sCRRvi0VM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b0a0ab95.mp4?token=QnQHi2wDbtUU2tkbXb9Q-Xwxm8llvZECobUuaOZi2fBfWASTGHGdqGhN-pUt0tC3Kif24UZinqaDMhXOxBf8A4SAonOVIgKeJzM40iHaQz14KvvN2YGu7dk6NOyzHZUwqXoqLgi24XQjGfbpcT0MoXMyiZwzfH15OeI7FEDffuWq10oty0A_Gh3uFDc3J35Hg9d_AC8TLm8Wp3GypDWFD9mddn97osnj3uXCdXQU2Bv41rc5ziUM7X1g0R-Y7A6fpTBoDOCW69yj4G484Ic1VkPtsXeteFe6I3X7xTuY6i18Zk_3amS3vV7dokYNdqXR1zRFAVHPzD5ctAH_BNUNWRlAOlnM_JRo6p924ZIEHiWYIwqajrJUWJ4l5H4jTBpraeOMSp34RQ17tIYPzdzpPNKVt8F-jrZEG1Xh39KsvUt6oVp7PT0xT3rbvnDqrX6KVrBH9CutvJpqxjNX9E5Lu2gIQfSqHX_PqOvGngNafQj25A1oCY4pL3eqSwa8lrhUi91nuL-4vzFDdYy7RzNbDjRXa7c7iC4iO3yV-e73eqo2fdgIyWdtpqpPUf1IgY0S_WOXSfsJy2Ut1TMpFJu0LAYJlMsriDRgSfVLwRalV3uNEJqFtXdIyDH8ddmh8O4h0e1ndOaHgnDy80FHNi0tJ63e3MHlemGdt9sCRRvi0VM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیدایش سالپ‌ها در اطراف قشم؛ امیدی برای بهبود آب‌های جزیره پس از لکه‌های نفتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/691324" target="_blank">📅 23:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6nFpgSHi7NEyRjBWUSqjXuBZJVpsCWGxx2ChODVKkEQzcJHAX0Qm7jaW3uhlBurOF-q69HPQPt8iDwu7PPXkrZLGiykuqfsRcQ8fU3wXix6QbyuWqj3t0fF_-bLBSdmMmpZKqhzXNxutHSd0b3PsJ7lFmGAtXxAsj-ogj9LaQVXfSg-IQ2XtPV_COgTqQM1NeYzXp1mGDf9Qq8BgApVVXjh5RsJUdk3Am4VWaPaSPlM4CSIjl8LKyXYB8II32NiSEieB8OO0MfK_3wht13gflpYpfYEgppGsGDt0LS5md4lzrsEBMmr7g1cvt-z7YNEDCc_mS1OmYBVAIrt1wTWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: ما با میانجی قطری که شرایط ما را با هدف توقف جنگ به واشنگتن منتقل کرد، در تماس هستیم و منتظر پاسخ  ترامپ هستیم   رضایی:
🔹
شرایط ما عبارت‌اند از: پایان‌دادن به جنگ در تمام جبهه‌ها، آزادکردن دارایی‌های توقیف‌شدهٔ ما و پایان‌دادن به محاصرهٔ دریایی.…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/691322" target="_blank">📅 23:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691320">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mawovho_-r6o9X5OuQlSjEatqdP4GXqTMA0HiKpwar4xD0_mwp4PM0YNjrNk-3focSIvpGfniQyiqKEbrwknA8LfRh289nj0KjloBTPrZYFrTHuYNMdRPC-RUNX0U9qxPNtpUIGzkAJeIUe7h3SugSkdB9Cz3hZ7_4EEs4lnqFq8B807nG8o2AkraVEVwnL0nGXP2x_w-YL7IQK-La1Npj2_2mizQYqVIaVHHMidb0WL_Q9dKCQt4T971_0F1vsd8ubX1uLq4jZWQVSYCZ0-73k5aBFnMq41IEZ9KUFrXEVH26aFBVeM3h8qwbJkVmTlNB523JiiUs6aBrKwmGPEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقایسه آمار حیوان گزیدگی در سال ۱۴۰۵ و ۱۴۰۴
🔹
میزان حیوان‌گزیدگی در پنج ماه نخست ۱۴۰۵ نسبت به مدت مشابه سال ۱۴۰۴، حدود ۸ درصد کاهش یافته و ۱۵ هزار و ۴۳۷ مورد کمتر شده است.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/691320" target="_blank">📅 22:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691318">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نقض حریم هوایی محل حضور ترامپ در کمپ دیوید
🔹
هم‌زمان با اقامت ترامپ در نزدیکی کمپ دیوید، یک جنگنده اف-۱۶ امروز شنبه پس از ورود یک هواپیما به محدوده پرواز ممنوع، به این منطقه اعزام شد و این هواپیما را رهگیری کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/691318" target="_blank">📅 22:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691317">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0YuE91Xy-rSO-FaZCk7RFa1HIuk20qOabvQEoDftqEAUfZGKk_3H4kvZzDSSn8die8ZOK3Y25Fjz9QctpyfVhMvYsdAYmX59-JD_63RQ5O3Z-VpaDVJwtM93opUV7kvuAmHR8qgzHvyr3uOxlIRwW1Zr7giBNSTmjien9saI0Xkh8P7ywMY4qQMkCSpJ_u0uLwQ8CmRuqgOlhC75DOHAjOyeh7WiHughyG6G-MdFWuR9hDRH1T9d8l_tOzGUlBQrJiW1p0Qm5eMUPrBOYbrE6TsM4HnLpaBg2giMxTQIk1-6b-PW7Wu4FTYzoPjOz2S7CZYvZRyXO4L5F-D9GAasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثبت تصاویری خیره‌کننده از چشم‌هایی که در قاب عکاس ترک درخشیدند
👁
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/691317" target="_blank">📅 22:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691316">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: مقاومت تنها راه مقابله با صهیونیست‌هاست؛ سایر راه‌ها تلف وقت است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/691316" target="_blank">📅 22:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691315">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
افسر اطلاعاتی سابق آمریکا: روایت واشنگتن از عملیات نجات خلبان آمریکایی از ایران، ساختگی بود
🔹
برنامه‌ای که در این زمینه ساخته شد، یک اقدام تبلیغاتی و سناریوی ساختگی با همکاری وزارت جنگ آمریکا برای قهرمان‌سازی بود.
🔹
آمریکا پس از شکست در جنگ با ایران و عقب‌نشینی از پایگاه‌هایش، به‌شدت نیازمند یک قهرمان برای افکار عمومی خود است‌. این یک شکست واقعی بود که در آن ایرانی‌ها عملکرد بهتری داشتند.‏
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/691315" target="_blank">📅 22:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691314">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4363b66699.mp4?token=bx-jPNUzSvTgepQ9qAytlPOHePxGZSPJtRwnamhb6pPuavqaBQCVg42v5HAWNyhHkv0Fo56DCwDOcIaNvpJl_ho9HFDVLRyKhSdHcskk6maXvTsVgpeDTsRyjs6eIeqJfvG2pvWTHHb-2rAAZ3rVIQE0Sl-UzhE4aIWQ5N7SmzQXuHFOCICTVGlNJA1ycfXrld3ayIVus6fh3l-jIlHbmPGpEKTRo6spR3nnhLdO67pwCywQIgqlmHp_5SEzMqVIUUBoMbOdUyCHMK4ZDdIhUbNz7003b6lrwaVAcEl3nqhd3rPhJY2U_DQR4d0GwoOBuN36CFU7Knonsyx4ueFBrYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4363b66699.mp4?token=bx-jPNUzSvTgepQ9qAytlPOHePxGZSPJtRwnamhb6pPuavqaBQCVg42v5HAWNyhHkv0Fo56DCwDOcIaNvpJl_ho9HFDVLRyKhSdHcskk6maXvTsVgpeDTsRyjs6eIeqJfvG2pvWTHHb-2rAAZ3rVIQE0Sl-UzhE4aIWQ5N7SmzQXuHFOCICTVGlNJA1ycfXrld3ayIVus6fh3l-jIlHbmPGpEKTRo6spR3nnhLdO67pwCywQIgqlmHp_5SEzMqVIUUBoMbOdUyCHMK4ZDdIhUbNz7003b6lrwaVAcEl3nqhd3rPhJY2U_DQR4d0GwoOBuN36CFU7Knonsyx4ueFBrYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری محراب قاسم‌خانی از چگونگی دور زدن ممیزی صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/691314" target="_blank">📅 22:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691307">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2160bb83eb.mp4?token=FbVlObWZELobhJA9V4SIYLwEIYDCqmEgzxWeyU1JujKW_btzewfapce1SlztC_9aIV9ofV4pIR15Uon6BfhznIKHGbv_lBRwRR6TrV1-UwqnA8cHIuE8Ufzs08Hv1DD-HmP2Y5caVY0XjrwbFaCLKhYyB7aovMv6oR-O-rYeeeZ96UZxPD6VLhR3IPv1VeDZ4LKAxvriP_YupNJS-Fy1_QemzurB4otvbD009w1GhKkgfrx9HFd3dmPRL1Rdmbb9xjs3GqPPN14sCKaCrOcV46jFH6m9dEDroEfcQjQElO1IuENokkOHxE8IkpGPp-9kGZ_Nn2JVj3rk_OceDhK5dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2160bb83eb.mp4?token=FbVlObWZELobhJA9V4SIYLwEIYDCqmEgzxWeyU1JujKW_btzewfapce1SlztC_9aIV9ofV4pIR15Uon6BfhznIKHGbv_lBRwRR6TrV1-UwqnA8cHIuE8Ufzs08Hv1DD-HmP2Y5caVY0XjrwbFaCLKhYyB7aovMv6oR-O-rYeeeZ96UZxPD6VLhR3IPv1VeDZ4LKAxvriP_YupNJS-Fy1_QemzurB4otvbD009w1GhKkgfrx9HFd3dmPRL1Rdmbb9xjs3GqPPN14sCKaCrOcV46jFH6m9dEDroEfcQjQElO1IuENokkOHxE8IkpGPp-9kGZ_Nn2JVj3rk_OceDhK5dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
ای که تو دنیا وارث حیدری
کی منو باز به سامرا میبری
تولد پدرت مبارک یا حجت بن الحسن العسکری (عج)
🌸
پک استوری کلیپ های ولادت امام حسن عسکری (ع)
میلاد
#امام_حسن_عسکری
(ع) مبارک باد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/691307" target="_blank">📅 22:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691306">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3514de7ece.mp4?token=a-466oRN97cZU06TpZVfK_C1yCppdZMs92KSSM8FeCeHKHEXmie2LzwsD-tJEWd5ftcrk6qP4RtZzjmpUOlWprwg3OWLX7peugaAfUWEe_jDiJTf8UU_-IoXCRzM4CCI6HEZD6ObHAJwRKcIW7ACC_6ObbO2x4M7YS916Ey0k5MenWmGAScV_I39Z9FUnGXWNvafCl52fvBnFqIaCC6RLGclC8Pz-9lrQ2vmPPFTQWGMjF6TCh_Ynolxr6yfLcO3_EbxTq3W1mtv5J9INSqLr2VzztWwKOrU8SWClnot8VgnpSwzRZ61k36nmvoKrOVpf307lJERk6TthIU-AQyytFh42uuo1ClZs2eYsJym6nV2ZqLqwSCDNd7gn_PtkWMPBdjcbCF_pB3nZgJechFZayMg84cSCv9va4sNe_jUg7vzeuk5cejKRXSB_ixvvkHdGJAtk3Bga8GFF15GFjmpOILM6H6ed8uBRTXLFXVwR7tVw9LnYHiiWNgZFoi566ZbnLLA87N19w1Q8Sx_AS1I6WszE8HGbpeFT5rk-yad-AgQ6TzQ_3YrWssUQ44aVJY6Eht3NtgliGvdJTKbEG585yEnftDspZt69JPuEP-TrXF4TKIqTa6kxv_19o5pobm9Sl4zLY_x8ki2yn093jYx2owu4vRFH4evVfRtXHtTs6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3514de7ece.mp4?token=a-466oRN97cZU06TpZVfK_C1yCppdZMs92KSSM8FeCeHKHEXmie2LzwsD-tJEWd5ftcrk6qP4RtZzjmpUOlWprwg3OWLX7peugaAfUWEe_jDiJTf8UU_-IoXCRzM4CCI6HEZD6ObHAJwRKcIW7ACC_6ObbO2x4M7YS916Ey0k5MenWmGAScV_I39Z9FUnGXWNvafCl52fvBnFqIaCC6RLGclC8Pz-9lrQ2vmPPFTQWGMjF6TCh_Ynolxr6yfLcO3_EbxTq3W1mtv5J9INSqLr2VzztWwKOrU8SWClnot8VgnpSwzRZ61k36nmvoKrOVpf307lJERk6TthIU-AQyytFh42uuo1ClZs2eYsJym6nV2ZqLqwSCDNd7gn_PtkWMPBdjcbCF_pB3nZgJechFZayMg84cSCv9va4sNe_jUg7vzeuk5cejKRXSB_ixvvkHdGJAtk3Bga8GFF15GFjmpOILM6H6ed8uBRTXLFXVwR7tVw9LnYHiiWNgZFoi566ZbnLLA87N19w1Q8Sx_AS1I6WszE8HGbpeFT5rk-yad-AgQ6TzQ_3YrWssUQ44aVJY6Eht3NtgliGvdJTKbEG585yEnftDspZt69JPuEP-TrXF4TKIqTa6kxv_19o5pobm9Sl4zLY_x8ki2yn093jYx2owu4vRFH4evVfRtXHtTs6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از فتح رتبه اول بورس کالا تا جهش ۲.۵ میلیون تنی؛ روایت یک ربع قرن غول‌سازی در شرق کشور
🔹
فولاد خراسان در ۲۵ سالگی، با حضور وزیر صمت و جمعی از مقامات کشور، فصل تازه‌ای از توسعه خود را با افتتاح واحد انباشت و برداشت مکانیزه کنسانتره رقم زد.
🔹
این مجموعه امروز ۵ درصد شمش و ۶ درصد محصولات فولادی کشور را تولید می‌کند.
🔹
فولاد خراسان با نزدیک به ۳ هزار اشتغال مستقیم و ۸ هزار اشتغال غیرمستقیم، یکی از پیشران‌های صنعتی شرق کشور است و در سال ۱۴۰۴ رتبه نخست عرضه میلگرد در بورس کالا را به دست آورد.
🔹
مسیر توسعه فولاد خراسان ادامه دارد؛ از پروژه ۲.۵ میلیون تنی فولاد شرق خراسان تا توسعه زیرساخت‌های انرژی و پساب؛ گام‌هایی برای تثبیت جایگاه این مجموعه در صنعت فولاد ایران است.
ادامه مطلب در سایت خبرفوری:
https://www.khabarfoori.com/fa/tiny/news-3246426
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/691306" target="_blank">📅 22:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691305">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اخلاقی‌امیری: شهریه برخی مدارس غیردولتی به یک میلیارد تومان رسیده است!
حسنعلی اخلاقی امیری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
شهریه برخی مدارس غیردولتی در تهران در یک سال به یک میلیارد تومان می‌رسد و این رقم، از نرخ رسمی شهریه اعلامی آموزش و پرورش بالاتر است.
🔹
اگر حقوق یک کارگر را ۲۰ میلیون تومان در نظر بگیریم تعداد قابل‌توجهی از مدارس غیردولتی شهریه‌ای بالاتر از ۲۴۰ میلیون تومان در سال دریافت می‌کنند که بیشتر از حقوق یک‌سال کارگر است.
🔹
حدود ۷۰ تا ۸۰ هزار کلاس در سال جاری به مدارس کشور اضافه شده اما جبران عقب‌ماندگی‌های آموزشی و رسیدن مدارس دولتی به استانداردهای لازم زمان‌بر است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/691305" target="_blank">📅 22:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691301">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6779b43190.mp4?token=gsyRtOUTokZafoDdDPaZ9b64csKEwqCeMn0r7hiAOq-I6RpnqYZ7rrN8-jTi5Sj_vdfLEnMLXC0M3WsitDIIgPTx7YhCKVH3hw-flMHGlqhN27jNGxtTLbG0wRRbYBJ8kiG8KuTTrfGzRw9FAtY8e6ZYydiwou2qWIJoTtZW7ZIyzKw8ogNBStRhI_48VvF_n5jtOb3145qAhE1TG7SaIVn6ySG1uwUeNHatSh7gU6Ojfwp6QQ8gVN8QEOaEMhMX72Kdsq6NH1re6itHTKJp2ftdGqW4RrU_6bLLaxlvkJH-csl048ziHTSf6ScZ8sBmMhg_5-fIGtUb9QTz8BHOGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6779b43190.mp4?token=gsyRtOUTokZafoDdDPaZ9b64csKEwqCeMn0r7hiAOq-I6RpnqYZ7rrN8-jTi5Sj_vdfLEnMLXC0M3WsitDIIgPTx7YhCKVH3hw-flMHGlqhN27jNGxtTLbG0wRRbYBJ8kiG8KuTTrfGzRw9FAtY8e6ZYydiwou2qWIJoTtZW7ZIyzKw8ogNBStRhI_48VvF_n5jtOb3145qAhE1TG7SaIVn6ySG1uwUeNHatSh7gU6Ojfwp6QQ8gVN8QEOaEMhMX72Kdsq6NH1re6itHTKJp2ftdGqW4RrU_6bLLaxlvkJH-csl048ziHTSf6ScZ8sBmMhg_5-fIGtUb9QTz8BHOGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترس از جنگ، بی‌طرف‌ها را بیدار کرد؛ چرخش اروپای بی‌طرف به سمت تسلیح
🔹
حتی کشورهای بی‌طرف اروپا هم در حال تسلیح و تقویت دفاعی هستند؛ سوئیس استراتژی امنیتی جدید تصویب کرده و سوئد پس از جنگ اوکراین به ناتو پیوسته است.
🔹
برخی کشورهای اروپایی مدعی‌اند روسیه قصد حمله دارد، اما پوتین این ادعا را رد کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/691301" target="_blank">📅 22:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691300">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
تاس به نقل از یک منبع ایرانی: ایران آماده بازگشت به مذاکرات است، مشروط به اینکه آمریکا حسن نیت خود را ثابت کند
🔹
تهران همچنان برگزاری مذاکرات درباره موضوع هسته‌ای را ممکن می‌داند، اما تنها پس از اجرای کامل توافق اسلام‌آباد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/691300" target="_blank">📅 22:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691299">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ywm3BJTI5m6XoQTP1Hyi2w8-en7iqFvpdpEAGid5s2zGKTQ_YEc-6VMaazvfGCRbgXEzgcQtm8oEKtwrle0ygg7t7cIJXab2aIKPaP38VaHYEhyCC7ogp9uKoRVNLkI2A-FuuAjxR9XZ5I8FHdVYL_2jBo3PMR-u0pkl9w9yvU5V1E80cwLHoKchBTBQOf8tSe1EuxQCCmro-dHelHOA4PZL7BNOqNZhOgjzrF9CILa0omygayzPvvUHn86EqLctbcYdLDjxJJo8kospwcG_judFuDo_hJCUCEViKHpwkTwy2oNDNKb7rIYionerk3mkzuzoz0-G6RXyXVoi_POPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبق پیش‌بینی مرکز آب‌وهوای پکن (BCC)، شرایط بارندگی در فصل پاییز برای سرتاسر  ایران مطلوب خواهد بود و یک دوره نسبتا پربارش در بازه زمانی ۱۰ مهرماه تا ۱۰ آذرماه پیش‌بینی شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/691299" target="_blank">📅 22:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691298">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8e6bd18f.mp4?token=vrw0K8CZNhKeyCz4j2E46thnOidoAOvPO_jJMtx_o_PlheVltOtzy-uby59zDuAYo0Al2fvd4a0ECj8lrXFobaDeBnxD7TIPj3K-4CFK4QAc1aSmlFc2LXM-eIGeEE0DaCWJJEe-WKUYISX0Z_cTQtS6YN5trN-RRFfuz3MpZQ6G3uH8gkPrSW5qasGiRtAk3PugAZUELbcc6h_yDUUW5Mcv7n2xQt3vC79zUnsVyBlFBEF7vNOTciN3xZy9kCdWV2hdA3I-ZDF3vqLj3OrJrcBFslYt7RSZcJhG68V_lSi_FcnCa2v5vXmL2SlMqzqIzfouiIanwDgf1nRa-v4Kcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8e6bd18f.mp4?token=vrw0K8CZNhKeyCz4j2E46thnOidoAOvPO_jJMtx_o_PlheVltOtzy-uby59zDuAYo0Al2fvd4a0ECj8lrXFobaDeBnxD7TIPj3K-4CFK4QAc1aSmlFc2LXM-eIGeEE0DaCWJJEe-WKUYISX0Z_cTQtS6YN5trN-RRFfuz3MpZQ6G3uH8gkPrSW5qasGiRtAk3PugAZUELbcc6h_yDUUW5Mcv7n2xQt3vC79zUnsVyBlFBEF7vNOTciN3xZy9kCdWV2hdA3I-ZDF3vqLj3OrJrcBFslYt7RSZcJhG68V_lSi_FcnCa2v5vXmL2SlMqzqIzfouiIanwDgf1nRa-v4Kcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو دفتر سیاسی انصارالله: این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید. اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/691298" target="_blank">📅 22:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691297">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927422b7c6.mp4?token=cWjkpj549Ke3DfSTBtkKXwDVSAbJM-jbvJcQx8zxcYnopkd_QWtDR-JFDCZU27HnDYRB99J9GzDlmnXiMIdvgG6R4O3ePycuesGgWlZBOyN5q119uxaX8TD-b8qIkLgpswktEEbs-hC_OpH4TAa7IHDJCXUuq_AcAEwRKmMyy4oggQcDLp8Devp10W0OvsEcRoeLNVeSYc1-07se1_NbDGtldmaAcBq8T9McElnc1sCCvNmJmcIZxNfWp-CejG80EfyDhklnqmXHc0VG8IY7B3bQPXdlC3s9nLBPoPSWUjyPirFsxvrZAdJ7qFE3HJpnae44kmlmHTSmo4DyxfL7IRS1ycQ91ozPIBMZwor47JhjstV8Zf_W5mogLtrs-H-5XqNZ3etT94vYkyrPayHjesW1tM2cGDXyINzf1X6wXKv03i2UeCkn9OIfpMop1jIQfede5pK05HGPbnrHkMPbp2RRjAZzAn3jbea5d7qogjvoIWUlI-IM64IbtiIpyxnYgeAn5nftdf8ONWiGM7EfylEuvDpsK4NsIgDAlUx41oYPt9aZpAdFevJ1sDY9kZLgv3RYZ8RzGLFz6o_FEDQ1EQYxkAXh4xN9ETMt4iGxJZn_sVUpiLCObU9Ow08Ya8a7EfrM86ohfnanI8rat1LvJoWvaSZ73TE20boxpHpWfjs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927422b7c6.mp4?token=cWjkpj549Ke3DfSTBtkKXwDVSAbJM-jbvJcQx8zxcYnopkd_QWtDR-JFDCZU27HnDYRB99J9GzDlmnXiMIdvgG6R4O3ePycuesGgWlZBOyN5q119uxaX8TD-b8qIkLgpswktEEbs-hC_OpH4TAa7IHDJCXUuq_AcAEwRKmMyy4oggQcDLp8Devp10W0OvsEcRoeLNVeSYc1-07se1_NbDGtldmaAcBq8T9McElnc1sCCvNmJmcIZxNfWp-CejG80EfyDhklnqmXHc0VG8IY7B3bQPXdlC3s9nLBPoPSWUjyPirFsxvrZAdJ7qFE3HJpnae44kmlmHTSmo4DyxfL7IRS1ycQ91ozPIBMZwor47JhjstV8Zf_W5mogLtrs-H-5XqNZ3etT94vYkyrPayHjesW1tM2cGDXyINzf1X6wXKv03i2UeCkn9OIfpMop1jIQfede5pK05HGPbnrHkMPbp2RRjAZzAn3jbea5d7qogjvoIWUlI-IM64IbtiIpyxnYgeAn5nftdf8ONWiGM7EfylEuvDpsK4NsIgDAlUx41oYPt9aZpAdFevJ1sDY9kZLgv3RYZ8RzGLFz6o_FEDQ1EQYxkAXh4xN9ETMt4iGxJZn_sVUpiLCObU9Ow08Ya8a7EfrM86ohfnanI8rat1LvJoWvaSZ73TE20boxpHpWfjs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماهی غول‌پیکر پیراروکو (Arapaima gigas) از بزرگ‌ترین ماهی‌های آب شیرین جهان است؛ تا ۳ متر طول و بیش از ۲۰۰ کیلو وزن دارد! در این فیلم، یک نمونه کامل در حال سرخ شدن توسط مردان برزیلی است!
🐟
🔥
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/691297" target="_blank">📅 22:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691296">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
خوابیدن با نور روشن ممکن است بر سلامت قلب تأثیر بگذارد
🔹
بررسی یک مطالعه روی بیش از ۱۰ هزار نفر نشان می‌دهد قرار گرفتن در معرض نور هنگام خواب، با تغییراتی در ساختار و عملکرد قلب، از جمله ضخیم‌تر شدن دیواره‌های قلب و کاهش جزئی قدرت انقباض آن، مرتبط است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/691296" target="_blank">📅 22:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691295">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqykq49hJXH2_sW76v1GMhsuu-6Vmfbb4EK3RI_gYGd5IPJodzUGGOJdWkwdvGiyVbwzwp-eubMFiHgXin2s3xOAdrzb1j92PYbgkZf3S4861LDgpyJIIpcusziaHXxvo9dus4bGpHQKEy3ZBLB1u5kbzBoR0-sErealhxeqNpujE0yM9l6-9fEiwJ5nlgBzPRZB_LaVfMmzBNjjhtwk9Ko_8SINnix6sHHWpgeyy-331ji6VSgSEcL3J7V0_6AgmMVKLTappX_vWGVoouk6ua9uqjGp_UT7Uy912XmAlJntb63vYBUTZT9OpY94_QZyedQXFNhipnGTd55F56a3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر سیاسی و ژئوپلیتیک: نمی‌توانی ۱۶ پایگاه را از دست بدهی، در حالی که در هرکدام حدود ۲۰۰۰ نیرو مستقر هستند، و فقط ۱۳ کشته داشته باشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/691295" target="_blank">📅 22:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691294">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">🔶
فراخوان کمک برای مادر سرطانی
🔸
این مادر دارای دوفرزند خردسال وهمسری کارگر ومستاجر می باشد برای انجام شیمی درمانی وپرتودرمانی نیازمند حمایت است
🔸
اینک برای  درمان وبازگشت به زندگی درکنار خانواده نیازمند مهربانی شما عزیزان می باشد امیدوارم بخشی از هزینه ها پرداخت کنیم
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید
شماره کارت خیریه مهر مبین:
6063737004808968
6104337806663215
شماره شبای خیریه مهرمبین
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در کانال خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/691294" target="_blank">📅 22:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691293">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiP_4hy3ubA8kdkzDhQtfWZEV9WrWWmGratfWnSkHL0aOkmdUSsinBINipZFE3UgLul0Z6CGdLwYRPiiBjDohK617AAvZxBNzUFs-sxVFr8_pV3VwtRyGJaFxTjJewBSuVArBCaPJtg7fUmYt4XqMlWhrBjqPDoHbnYyNQYFcGcJZtd5vfJ3cLyMw0XHfhVnTdSwjJvQho8EAug_OrlMKbR64z-Pw3amew_4VZOZjxkh0tPfgtXm087SDIBSk0rGATcx93DY19Bj7dd8j2ibxD1pe-GdnO4nP5khm2nKbIIx3s9Da_47-1s6Q52YiAeCsB-exgpG8GVsXofLQgNM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
برای انتخاب آگاهانه بیمه‌بازار داره!
وقتی قرار باشه برای ماشین یا موتورت بیمه بخری، از کجا می‌فهمی کدوم شرکت
بهترین پوشش
و
مناسب‌ترین قیمت
رو ارائه میده؟
من ترجیح می‌دم چشم‌بسته انتخاب نکنم!
وارد سایت
بیمه‌بازار
شدم:
✅
همه شرکت‌ها رو کنار هم دیدم
✅
قیمت‌ها، و پوشش ها رو مقایسه کردم
✅
و آگاهانه بهترین بیمه رو انتخاب کردم
👈
برای مقایسه و انتخاب هوشمندانه وارد شو
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/691293" target="_blank">📅 22:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691292">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO12-8NHM4ONtE3MgIMt82_7kWZSAyUkwbeL2PBZ1gwfn2LuAxYO3DirTUt66oDwrj45J12y_z7XIyL7z0hEwYfQS5LyOiG_LY-lVR4hhI_CaPuv98M5IFz5w_5xrjyjM1XVqFl3FFqmDgtoYYDPOArs2CnJO-bPt8ZiBFr9FslHL9xo09kibr-C-tKHeSL9yPKTvW0NFtS2Ggky7ukXzCQymzdiRT9luQr54_bjRkzAv5mDKmyvCz-9c3b-EXmMDJ-SRcQL1xEm4ihgKcwMx6sGl50SqTuNNbzfJbMH8yDnzCtnD605peGj0SbqJ02yQ5sI0JehPu_9GXUGvHHlyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: آمریکا به متحدانش هشدار داده تحویل برخی سلاح‌های مهمی که قبلاً خریداری کرده‌اند ممکن است تا ۵ سال عقب بیفتد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/691292" target="_blank">📅 21:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691291">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f37a29cd.mp4?token=JnybuYvhSr8JktlBW7Xt98pKxGjjOmpsmL8X3f5hiCxYDgQ6OdMTaZOzlMAGp2YmNFPZkWuf5fAwM_ox-XuIE2k_L8vSWOu3jVOSW4a04DninhK0HLigCavqUNnmJOsGZXVgvrFnwmE3BIj02ntQTUc_LgDWhZodyeSpETzANx1Dc9A1mPehq-LD-gRlgjIuV2GGcNAVqsS_gUuOuwTbg_Euj1bt6IkR1Xs5M25omm7T82q_KtAkevyTfADjPAvl16u2OPKnMEARpqV-6cXJ-Bhm-v6EiE1hROZO5vci6xffIbs4EEXrwQgknYVqwAmtH06cdPW5aQ-eOrhQYm1M8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f37a29cd.mp4?token=JnybuYvhSr8JktlBW7Xt98pKxGjjOmpsmL8X3f5hiCxYDgQ6OdMTaZOzlMAGp2YmNFPZkWuf5fAwM_ox-XuIE2k_L8vSWOu3jVOSW4a04DninhK0HLigCavqUNnmJOsGZXVgvrFnwmE3BIj02ntQTUc_LgDWhZodyeSpETzANx1Dc9A1mPehq-LD-gRlgjIuV2GGcNAVqsS_gUuOuwTbg_Euj1bt6IkR1Xs5M25omm7T82q_KtAkevyTfADjPAvl16u2OPKnMEARpqV-6cXJ-Bhm-v6EiE1hROZO5vci6xffIbs4EEXrwQgknYVqwAmtH06cdPW5aQ-eOrhQYm1M8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ سوژه تمسخر خرد و کلان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/691291" target="_blank">📅 21:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691290">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
نتانیاهو از ترس، به فرودگاه نظامی پناه می‌برد
🔹
بنیامین نتانیاهو، به‌جای فرودگاه غیرنظامی نیویورک، در یک فرودگاه نظامی در خارج از این شهر فرود خواهد آمد. او سپس برای ایراد سخنرانی خود در مقر سازمان ملل متحد، به منهتن سفر می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/691290" target="_blank">📅 21:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYfBsWGheoSVq5K59BnbFqamNwcijiEuy2HnN8o7kKE0WYR5aAjJjWjmc3X3N5HYlvYeqR43fwi0iDS3Q7gcl33s4a9fsI2pXsthxaYHay4gTk4hCyxqnHnEj_yBEHDiY7JEK9oC3A8E2iRe6N-AMywy-28YVLkOjVdMyIxoh-0Idl720VBVXJnLvvi9CfwJkxBVdRSb2XPi617dGM6DxaK3wyLA6WeXpU8I2G9QlIm_brbYWYPWPJ1r2K9vGWgB78Wwwo1YJ76-OEL-xXUbB3k6CmShp0bR0LmWZIMFZoIJMFWyeP37rHAag63Woqst9NeLPImBMpH2JWXEpZCyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیاید رایگان با این هوش‌مصنوعی پادکست بسازیم #هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/691289" target="_blank">📅 21:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691288">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/388a43995c.mp4?token=O12lW5xZ92YhAueUaaWSdHHuV5z7_lHT6LmSYMdC70HW2_-yC7ZSMyRDoPv5vt4inAxZDZ0OSUz6iuZOOicS4wd6V4YgQ7fooq4DcXoMN3dxXRlMc9R0esZk_UwgOIDC-wu_S0rITGSOZ7Dniu_nuvv1-YWItPJu-9F-NG7vBI9QRRPquZwl3GDLIdAXyjHTmqPysdz9AYX4BYACrhp1e6HykK__sgoH6MaiHT6BvWFEARM7YrZhxR9l4wXjWPPHx2Jny7NwfOzTIb2OvQYGuGA_caedAv9YzGc9g1gK4V5xvf6nx8qfNqjquqYJcJE3eDG8Q_JmgIi2gVMl0yi5fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/388a43995c.mp4?token=O12lW5xZ92YhAueUaaWSdHHuV5z7_lHT6LmSYMdC70HW2_-yC7ZSMyRDoPv5vt4inAxZDZ0OSUz6iuZOOicS4wd6V4YgQ7fooq4DcXoMN3dxXRlMc9R0esZk_UwgOIDC-wu_S0rITGSOZ7Dniu_nuvv1-YWItPJu-9F-NG7vBI9QRRPquZwl3GDLIdAXyjHTmqPysdz9AYX4BYACrhp1e6HykK__sgoH6MaiHT6BvWFEARM7YrZhxR9l4wXjWPPHx2Jny7NwfOzTIb2OvQYGuGA_caedAv9YzGc9g1gK4V5xvf6nx8qfNqjquqYJcJE3eDG8Q_JmgIi2gVMl0yi5fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی تازه لگویی/ هر رأی به ترامپ به‌معنای قیمت بالاتر بنزین است. هرگز دو بار همان اشتباه را مرتکب نشوید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/691288" target="_blank">📅 21:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691287">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
برخی از رشته‌های مهندسی و صنعت از انتخاب رشته کنکور امسال حذف شدند
رمضان رحیمی دبیر کمیسیون آموزش مجلس در
#گفتگو
باخبرفوری:
🔹
براساس برنامه هفتم پیشرفت، برخی رشته‌های غیرضروری دانشگاه‌ها باید حذف و با رشته‌های مورد نیاز جامعه جایگزین شود و در دفترچه انتخاب رشته کنکور سراسری امسال بعضی رشته‌های جدید اضافه شده‌اند.
🔹
در انتخاب رشته امسال بعضی از رشته‌های مهندسی و صنعتی حذف شده و برخی رشته‌های مرتبط با هوش مصنوعی به انتخاب رشته اضافه شده‎اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/691287" target="_blank">📅 21:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691286">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1ntwNdVKnLaAwNIqHL6TlWL5xRc26g2bHl_3ZAOHZWlK4121J1rttYE2UAdANHOa_4D3-Gxf7_sdfbEmWcwMJC8XIHSXRURQ4-uhvNh6kj5Ldveknd3iUGyoOAeuVPSsdU5AcJbcTQoG4o6ufAw_wFXb_rFvGKlA6WmuIEZepuu6LdtctMWtLc-BmY1_IAKdZicXlD6cItV2Nr1vbt3hAMJM4Uuo2dzEYVSAWqDPPvV3E80gBHpq4OClfqf8hJD6bR5MscPPB8-nibo_jEbqmuU50hzQQiQnGZ_tLtqyUPvsCkThXxXzemXof8Ztliw0IhHPxc4qMZL5cXfw-rGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: تجمع گسترده در تهران در اعلام آمادگی برای دفاع از ایران
🔹
الجزیره با اشاره به ثبت نام ۳۰ میلیونی پویش جانفدا برای ایران نوشت: صدها هزار نفر برای دفاع از ایران در این پویش اعلام آمادگی کردند.
🔹
الجزیره گزارش داد صدها هزار نفر روز جمعه در تجمعی سازماندهی شده در تهران برگزار شد، به خیابان آمدند و آمادگی خود را برای دفاع از ایران و در صورت نیاز به‌دست گرفتن سلاح اعلام کردند.
🔹
الجزیره با اشاره به اعلام حضور ۳۱۳ هزار نفر نوشت این تجمع با هدف مخالفت با آمریکا و تأکید بر آمادگی برای فداکاری در راه ایران برگزار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/691286" target="_blank">📅 21:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691285">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b4317f40.mp4?token=b1zbQFrNzFuHzVVXARS-NZB8YqXkZMb_1nDCe7K7DAXTRe53E50C_VEFBWYNGKI4McsZRw_B02vsYx4zlg4ynIHggHX796LUrPFiiA3r73m5NWmdU91QC2SPEU5pW8jpji2MxEJa36xgKXB5SlrkPGUcwaipAqz0RUvUlElabVfa5QC_-MdRVJEqZoZ1ImkMmUG2Ny4TWzsw6kAOaqO5mlLFT6y1sTugObVBBDFpZmKO045w1jvzoOoSQgZ4H26uketBmURsKWn1fb-3kXRxvY0oqC6EgP6xLmw3BHCXdOC-c8TEaCV1S7-euLaY40OOhX9jnvHxZFOZfpBTpHWI8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b4317f40.mp4?token=b1zbQFrNzFuHzVVXARS-NZB8YqXkZMb_1nDCe7K7DAXTRe53E50C_VEFBWYNGKI4McsZRw_B02vsYx4zlg4ynIHggHX796LUrPFiiA3r73m5NWmdU91QC2SPEU5pW8jpji2MxEJa36xgKXB5SlrkPGUcwaipAqz0RUvUlElabVfa5QC_-MdRVJEqZoZ1ImkMmUG2Ny4TWzsw6kAOaqO5mlLFT6y1sTugObVBBDFpZmKO045w1jvzoOoSQgZ4H26uketBmURsKWn1fb-3kXRxvY0oqC6EgP6xLmw3BHCXdOC-c8TEaCV1S7-euLaY40OOhX9jnvHxZFOZfpBTpHWI8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت ترامپ از افشاگری رسانه‌های مستقل
🔹
ترامپ جنایتکار، در اقدامی خلاف قوانین بین‌المللی ورود خبرنگاران شبکه‌های خبری سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و وبگاه پولیتیکو به کاخ سفید را ممنوع کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/691285" target="_blank">📅 21:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691284">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ4LhmGje30hUm3UNlgr0Y7FJE5t8XV0TUWzIbzScCu5NbuVlHn56JiXzwP7fqyQJ8Z2w3_HsqU8wo7jDgTG6UMhMcu-knYOaxTi2XNZx_lIGcIj8V3XliRVrTZGpiZ-S-CC6OiVfx4UG_L9FVkmlL3EyBQSwYCnhEVEaiWQJIcTo-OhwK3GcRHsq-3tk_xo00EgUnVhHcRMZgz7hziIJT0JI6KKMQOzMyOmd-taClcHfl21RwVtJgYuD6sG458cLAKNocagF3UZ9yXxIw7fHS6VenD845cWh0gGm7mY2e7IuDJJtqcw0jLGjv8eZJ2FafxM_J3UmKZ4I40jj1OKNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشریه لو پاریزین: میانگین قیمت گازوییل در فرانسه به بالاترین حد تاریخی خود رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/691284" target="_blank">📅 21:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691283">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8aea9937.mp4?token=EROWk9lZbd45r52ZWsXRy3SJGdrhSaHEUksvlSJ4hrGiL6B3bPMhS5qvWAzzegfEa0Cx-2GonSZnj21K_9tq6-MkrsaD2zEN-q1EES5K8nCFD5DtaI_0KGyZEF7mDeCW8yV3s08T5ou6wdsgWlvIFhej6BGGpfCdcoS5UMs2kUZmbFTNhMAM_SvUelwGj3SpiFzwgpZtsOE71APCYBy1TcQoo6IP61gh38swT2_BveIDDRtettgdVc5RFUunj-5weRx1hBndbOuzgFqRwnCg6X_ITv7WOFzbAhODLuhXXqTQOVjMlJqlpxx5cDzd-eT7JAS9qul4jxM_4FORzF1Tug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8aea9937.mp4?token=EROWk9lZbd45r52ZWsXRy3SJGdrhSaHEUksvlSJ4hrGiL6B3bPMhS5qvWAzzegfEa0Cx-2GonSZnj21K_9tq6-MkrsaD2zEN-q1EES5K8nCFD5DtaI_0KGyZEF7mDeCW8yV3s08T5ou6wdsgWlvIFhej6BGGpfCdcoS5UMs2kUZmbFTNhMAM_SvUelwGj3SpiFzwgpZtsOE71APCYBy1TcQoo6IP61gh38swT2_BveIDDRtettgdVc5RFUunj-5weRx1hBndbOuzgFqRwnCg6X_ITv7WOFzbAhODLuhXXqTQOVjMlJqlpxx5cDzd-eT7JAS9qul4jxM_4FORzF1Tug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیکن سابق استقلال: بخاطر تصمیم علیرضا منصوریان با گریه تمرین می‌کردم اما هیچکس حتی همسرم خبر نداشت!
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/691283" target="_blank">📅 21:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691282">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3588f464f6.mp4?token=nsNLxJjvPM_Eu0ISKIh_afR95LMoZPi8TccONiO_NNSyr7DfPhneI-owyCKzy_iZd8FYH_aX1q55pHnOT6Bzd4nQ_ITykDhoLrH6a3X48XYvhjA12hg2NUdePSty2RDbp_l-Vaf0mPlGT9jpHZzZDUMVpr6wvG-t0GxF5snVqW2A6dbp1LBBaeSjCbtZoAmYNallNaz4qDnNOogqJB4begtalbtvgD9GcXXs-x91HFQ9ixP5-t2ysr9SiQhIDhvjdDuxmXAWZQv8iNxhFYqSpYBsIvekjR346qcCBZ4sONbl6VVCw6p_8Hh-mEubQ843T_MaFpmBjqIIoGuw9xDRBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3588f464f6.mp4?token=nsNLxJjvPM_Eu0ISKIh_afR95LMoZPi8TccONiO_NNSyr7DfPhneI-owyCKzy_iZd8FYH_aX1q55pHnOT6Bzd4nQ_ITykDhoLrH6a3X48XYvhjA12hg2NUdePSty2RDbp_l-Vaf0mPlGT9jpHZzZDUMVpr6wvG-t0GxF5snVqW2A6dbp1LBBaeSjCbtZoAmYNallNaz4qDnNOogqJB4begtalbtvgD9GcXXs-x91HFQ9ixP5-t2ysr9SiQhIDhvjdDuxmXAWZQv8iNxhFYqSpYBsIvekjR346qcCBZ4sONbl6VVCw6p_8Hh-mEubQ843T_MaFpmBjqIIoGuw9xDRBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصف‌شب دندون‌درد گرفتین و خوابتون نمی‌بره؟ این کارها رو انجام بدین!
🦷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/691282" target="_blank">📅 21:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691278">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجاباما تور</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5tEmcrsGxpmGhnnTT5tRJxhjDlXDKzd0kG9XLfoE8McqJmMip6myVvaTVQedzD5XfnKL_cIMyPkJZInkvlZZbfHpah8sySJCOgJaYvZFb1QdfYs04a4YlcW3znGseyYMVAojG4RJgfJYBcCI_Rdn2rJj43lyeM0JT3-_TkjLg-CvtyarpF-5-HsW0CSecSfZ_JTU9dTDvIxWyERRpabQxPLN1ZW5Zu44RkXwyxJ0xWRyiVso_gXQJGERVddqOREzjo3UXmnOq9zkOFkVFjYE6dKRLTwQrO_AEupp21IdzaSYSntaI3RskE3GlXKiBzNgwcozXypqfRoZmhpe9foLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vV01VDGHcUKPjwgvRLvfdgsNb1ztMBDSI2mdPC-9grgrQEjlTXsahMRM1Lnld4X167mmUubsoAPsBL462ue3xZ1DUlJIFGNTavSYu2A2i8wLfAHmM1WJ2VWnadTMqcEI0BOdBFYdD7JlYWnK0vhiEAG-WmmcgnVbzCWEnHRch58w2Jam1njqZ_lF8R--J0WFxUyArvPtAlzjYcl8ovuO9Y18NjYD3GwZ5XDj0P0Ar4lpQtflQuCNbYR9OvJP4YIaKjX_6jMbU2SLtko3TYXiNI_94OhY8-cHOwxFYyR3-2IEoYPF6mw0fyDOQEs99q2b5AIc1EOwbdYgdmol9H0hxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehwMZcu0v0RkftLG5YxdWs20ja7pxMPV4DL28f4bJ3wJMyTNByheq5MNzljT-yXtG6uFm5apgQ4eQIPJ7bOgvoJ6Q17THLCH8n8HI7_CbT2_Z8PPSf2BTLMR_hpTkykrbzBxyV6Re40wufWrRxYnX3b44dHGvTvW7KeI24r_QKb6gxTS_-NSdmGWdpayr0ZFVH1nTEQ6Rs5x_JnSOBDh3UCtXddaKEeHvFgCc7-ho9M8o281KyIbamz5ImpNedyWaxYtTkZ5610Ealzfg-Cc7QQlztHd0WuLIkvrn6OXRCORVnstUBFlLO9nrIfC3lX4HDvWOhJUA7ytKo2CAMCSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dNuLsT701nmGYOTWxXBu1M1N3Rz3HSTT5MyM8TtRRYwA_KnnpSfAJq8kE9Nh9lxM1OadBMXh7RkjCekZFTpBWqPHxrdnMAorL1i1fTGrvRYty-e3LvVMW46uVx0df9Gg9xoihSaVjfn6UEkI_gHCSMlmFc1Oalel67yq0uB_YPQswaRR1HG7hAdBhvPfitQSFYerBfuMmzqZ9Hd0MiHy7k1RoJZzjKjT-lHmig5wGli4NWhXgp0nQm2N0hCVPqkRkKmMFi5hl7pc88ym6sxpfTo_yoxrAEBkfBUl1oJuHuadpA0NSI3sUV1vY5M6iBdVBEbJWA5Uq8vZiJpIFVtExw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برای اولین بار در ایران می‌تونید تورهای کمپ هتلی لوکس رو از جاباماتور به صورت ۴ قسطه رزرو کنین
😎
برای اطلاع از تخفیف‌های لحظه آخری و مشاهده تور‌های بیشتر کانال جاباماتور رو دنبال کنید
👇
@jabama_tours</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/691278" target="_blank">📅 21:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691277">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXwbig0Y9Bmos-FE8nS5SNcmVvCffGB6bcH2dTqgP_AYhehjTCQo6I6fhmvpr418uToYDuznCN3YNT1hQFNpDXorCqOtJGazTbDh7Xvw33Fk8mO_ADF8yuNsUL7wsg-ixX05032bxLyEsNVQ62e3xJCpoEXoYDiPitB6w_NAH8rIsWFl4umOTD41Qu9eOXN3_Aecro74ERVcbI-NWXSESdPODcV_JDIWrTlj29yGOoy7uUevQ0QvCD8ZRl-idy-ZKRNte2oKM0TXK1jesz4yrBugO8I92MnyZKqlDY2QU2WdcDfCrHnRMeKq6znK3gNmKK3bM4ZlWl8a9-zwOkkyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین پست رسانه رهبر انقلاب با بازنشر سخنان ایشان:«بنده قاطعانه اعلام میکنم که ارتکاب هر آنچه به‌ضرر انسجام اجتماعی باشد، ممنوع است»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/691277" target="_blank">📅 20:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691276">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای ترامپ: من در حال ایجاد نیروی هوش مصنوعی هستم، درست مثل نیروی فضایی
رئیس جمهور آمریکا:
🔹
من در حال ایجاد نیروی «هوش مصنوعی» هستم، درست مانند کاری که برای «نیروی فضایی» انجام دادم، که در دوره اول ریاست جمهوری من، موفقیت فوق‌العاده‌ای به دست آورد.
🔹
به همین منظور، من در آینده نزدیک، رهبر یا مسئول ارشد هوش مصنوعی را معرفی خواهم کرد. فقط افرادی که ضریب هوش بالایی دارند، می‌توانند برای این سمت درخواست دهند!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/691276" target="_blank">📅 20:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691275">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teY3xvM7D9I-eirByb-Ae0tYFtrdlxWlceEXYN5ucmeOfBZmmYlVBj7-4HzWP0XZPJs1AhEg2JOZvarkOfa7YDynQNrb2noQ3nyPOsgqmKvdFLCxoAXrYy9mcCjqtweIsuDAbisxlvNDH113CLp7ldF1m78WBlr0JSTIdH41vEikrgWIxt9Dv0vBDODDn0vegAnAEMENWu06vVjPiTN4AtyVGChDrkJ2aiGckiF9mhhV6EJMUeaBhdC6j8u6NINsKY6jIylmEcisC74NjCGMbHdaMuV-_dlWiw6iZV6c0LW7FZgGfjVdpPgsFj4RuCjQibCj1GD_VFDDb98FOfPx3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از هرمز تا باب‌المندب؛ درگیری‌ها در خاورمیانه به کدام سو می‌رود؟
نیروهای حوثی عملیات نظامی خود را در یمن تشدید کرده و جزایر راهبردی نزدیک به تنگه باب‌المندب و در داخل آن را که یکی از گلوگاه‌های حیاتی دریای سرخ محسوب می‌شود، به کنترل خود درآورده‌اند. پایان این درگیری‌ها کجاست؟
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3246392</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/691275" target="_blank">📅 20:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691274">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcFOoRjOSKUmfZszxernfW4H1UXydczlHNJHM0osUVlMXE8m5z5WA96jWJHMpounc4pms5rRBUY0YePlwuCEc4ocJjRfdxk2fD6XV8KyweuTqCwx-ydEWmuA7bSDliJ5nYw2gULVrXKQoboJsKOtseXjbcugZr8eHhwLGKbNcdD7kaVZc3AY78vrx41bPsyDD2isbrQONHNit2wvsdYu59XPWc8-8miHtuR8EYr4KmTvu_hAmmtVizkFrrG465HiQzjy6C_3ZLx8nV9wPTnMa5Wxf8LhPLNEko6lDfkJdEy-xdUBcrh8ozFPvuGZgdiFAkcEbOUyhdrLmhNwooWQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یورونیوز نتوانست قدرت نمایی جانفدایان تهران را انکار کند
🔹
یورونیوز از برگزاری بزرگ‌ترین نمایش قدرت حامیان جمهوری اسلامی در تهران از زمان آغاز جنگ خبر داد.
🔹
در این گزارش به حضور صدها هزار نفر در خیابان‌های پایتخت، مشارکت نیروهای بسیج و نمایش تجهیزات و پهپادهای نظامی در جریان رزمایش «جان‌فدای ایران» اشاره شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/691274" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691273">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
یمن: با موشک‌های بالستیک و کروز و پهپاد به اهداف حساسی در ریاض و شرکت آرامکو در ینبع حمله کردیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/691273" target="_blank">📅 20:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691272">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/503821f386.mp4?token=liOnqAW6-X2uvZVqXx5a6SD9nvZuEYYYsk2NRRyJCbUNRgTbFgTp-Q7HIR4tF02n8W7cQ83oHv1LNavdAPGsC66rtI8j-8rWtB5Qh0cNsAaIjGOD68Il2gyG9setaROQyCmi-3nMqKsljcRHfDiLJcdv5wO-rOtuU3rU1m1qERi_hM4_CvOzCBZmYszi06HH9RJQ41LaAPnPZut64YX4o5RiUUnVE-iQkzeODZYwc-JHrOBQbdjAb_xqTeKeC-3Vg1RP-ANXRksxo92R7wxt0Vi5yNinXmNhKG6MZ8N5EaV2RnLAlhssvBt6Y64_HSKGgB_ydaa8ZAf6dABz2qXlPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/503821f386.mp4?token=liOnqAW6-X2uvZVqXx5a6SD9nvZuEYYYsk2NRRyJCbUNRgTbFgTp-Q7HIR4tF02n8W7cQ83oHv1LNavdAPGsC66rtI8j-8rWtB5Qh0cNsAaIjGOD68Il2gyG9setaROQyCmi-3nMqKsljcRHfDiLJcdv5wO-rOtuU3rU1m1qERi_hM4_CvOzCBZmYszi06HH9RJQ41LaAPnPZut64YX4o5RiUUnVE-iQkzeODZYwc-JHrOBQbdjAb_xqTeKeC-3Vg1RP-ANXRksxo92R7wxt0Vi5yNinXmNhKG6MZ8N5EaV2RnLAlhssvBt6Y64_HSKGgB_ydaa8ZAf6dABz2qXlPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه اصابت گلوله به خودروی یک رهگذر در جریان درگیری افراد مسلح و نیروهای امنیتی در زاهدان
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/691272" target="_blank">📅 20:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691269">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
بقائی: آمریکایی‌ها سال ۲۰۱۸ از برجام خارج شدند و مدعی بودند آن توافق برای رئیس‌جمهور قبلی است. واما این تفاهم نامه که برای همین رئیس‌جمهور بود و ۲۰ روز هم دوام نیاورد  سخنگوی وزارت خارجه:
🔹
سفر وزیر کشور پاکستان به تهران دربارۀ روابط دوجانبه ایران و پاکستان…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/691269" target="_blank">📅 20:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691268">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بقائی: آمریکایی‌ها سال ۲۰۱۸ از برجام خارج شدند و مدعی بودند آن توافق برای رئیس‌جمهور قبلی است. واما این تفاهم نامه که برای همین رئیس‌جمهور بود و ۲۰ روز هم دوام نیاورد
سخنگوی وزارت خارجه:
🔹
سفر وزیر کشور پاکستان به تهران دربارۀ روابط دوجانبه ایران و پاکستان خواهد بود و قرار بر تبادل پیام خاصی دربارۀ میانجی‌گری نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/691268" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691267">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba3982e96.mp4?token=kc8XtVd6MCfNPsgRNV5MyBUTHmom6AMzgJofV-YkOGmZzC1-9T36OC5MwnuQSIv5lTpUDqjKHnmpTQ-oE2duDLV1owjH2s2HGifHBkXrwRwX5kIJWZ6kET079HyT0UskeSvhLczb56mkHZ-KLchllO7Q4atQncxV-2t7Q90HIpPNvSrBWXtDWEIf5MuWnHM0rO3B6xJ29VJhvgbKPovKMW9BJtShjxmnIubGuasRA0n_38MqMYQclwRMB6C6TgRJiXUzhMIDIBXFFoLeUFynPYI-DuPoL-_eqqiCM-VjxYIGZREorbz3s-NlSUcC1Te-UHhTzfjCbzcL9KqCSP6X3V8PvwQl2ghMVLFSHua0ltuniJrm-qimOPKEuone0_JzzoxM6WyDzFHS4RIkzV_RPgDNJ90IY9cJRiOmzalyjsoSC2ch2AxPdESogcL23709OwZo-WURKBAKxnc-BE-sTljm2h9n_TxjqtpcAMGqbyVUugXicpaDHGxTU-WcwMcdcRCh0nb4iwQH0KLC1BDXcC7qF6tp5vX8E1q4gx6tTSB0kYhwTpbyy01nFLDJe50wTxgB3KmmbyhD6GtsvlZSQimThSLKJSrFuvww6iq6R-Xs1EWjy7KYmdSRk7sLfbyHusOmEG35EhIOAyPon4Ms11mW_XUvmGfRLDTlIMQx5Ss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba3982e96.mp4?token=kc8XtVd6MCfNPsgRNV5MyBUTHmom6AMzgJofV-YkOGmZzC1-9T36OC5MwnuQSIv5lTpUDqjKHnmpTQ-oE2duDLV1owjH2s2HGifHBkXrwRwX5kIJWZ6kET079HyT0UskeSvhLczb56mkHZ-KLchllO7Q4atQncxV-2t7Q90HIpPNvSrBWXtDWEIf5MuWnHM0rO3B6xJ29VJhvgbKPovKMW9BJtShjxmnIubGuasRA0n_38MqMYQclwRMB6C6TgRJiXUzhMIDIBXFFoLeUFynPYI-DuPoL-_eqqiCM-VjxYIGZREorbz3s-NlSUcC1Te-UHhTzfjCbzcL9KqCSP6X3V8PvwQl2ghMVLFSHua0ltuniJrm-qimOPKEuone0_JzzoxM6WyDzFHS4RIkzV_RPgDNJ90IY9cJRiOmzalyjsoSC2ch2AxPdESogcL23709OwZo-WURKBAKxnc-BE-sTljm2h9n_TxjqtpcAMGqbyVUugXicpaDHGxTU-WcwMcdcRCh0nb4iwQH0KLC1BDXcC7qF6tp5vX8E1q4gx6tTSB0kYhwTpbyy01nFLDJe50wTxgB3KmmbyhD6GtsvlZSQimThSLKJSrFuvww6iq6R-Xs1EWjy7KYmdSRk7sLfbyHusOmEG35EhIOAyPon4Ms11mW_XUvmGfRLDTlIMQx5Ss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«جان‌فدایان» در قاب رسانه‌های انگلیسی‌زبان / مشارکتی که حتی از منظر تاریخی نیز قابل توجه است
رسانه انگلیسی‌زبان فرست‌پست:
🔹
این میزان مشارکت حتی از منظر تاریخی نیز قابل توجه است؛ زیرا در جریان جنگ ایران و عراق در دهه ۱۹۸۰، حدود دو میلیون داوطلب ایرانی به خطوط مقدم جبهه پیوستند که در آن زمان تقریباً ۵ تا ۶ درصد جمعیت کشور را تشکیل می‌دادند.
🔹
رسانه انگلیسی‌زبان الجزیره: این اقدام فقط به آمریکا و اسرائیل نشان نمی‌دهد که ایران نیروی نظامی برای مقابله دارد، بلکه نشان می‌دهد صدها هزار غیرنظامی نیز آماده‌اند در صورت ضرورت، به جنگ علیه آنها بپیوندند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/691267" target="_blank">📅 20:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691265">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
بقائی، سخنگوی وزارت‌خارجه: من فکر می‌کنم خود مقصربینی یکی از نشانه‌های جنگ شناختی دشمن است. بعضی‌چیزها به قدری عیان است که حاجتی به بیان ندارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/691265" target="_blank">📅 20:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691264">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU8Kl5x3CqPx_pOfpm8y7aA0ofafEuJZ4XdsKwh6r_lNDX_d4fAZDxso4KeeZIO_CUWuMdITgdCkAFbUhc56g8SnRc5B75r9Fq6F5vUtNljouSlvMzKOfsr89m8Lfaim_xgAVDvT1yPjUVEex5Gn41KYiESyiRCo7zamW-EShgIoRYblRDncukm7Q04UZna_ZhNf_jvABi36Hg_Fp2bEg4ECwllPoe10aTXGpghBnLAuU3dGGPrjDFDAXfBi6Zyy8ylsIWFagMptxOd8Iob00A1TxdX17IRFLUe7RrLHb2eKKB_appXD32Wgr-m2WU9PFN51BhQdSou7bOBnqflCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاد دانشگاه میامی: اسرائیل و آمریکا غول‌خفته (ایران) را که در هزار سال گذشته خوابیده بود، تحریک و بیدار کردند. حالا تمام دنیا با یک مشکل بزرگ روبه‌رو است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/691264" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691263">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c148f5e986.mp4?token=WMPKYwL-pBUyEeDFGKXaUQMQgwT40pVnjOG1EcjoS7ybsEkiaxcklV2l9dNhYV985Ory3sA7gsdiBNY2BmV9Vp5LZJRuQGsTdHAIdlZu1TeKDIG2IASBE4VNQVrt_H0e5Bxh6KAjGPGAqp32hMJuEmKA3rOvgiKmOalLnW3n4ceEibOxsrAC7NAtT7v_q_bvux-z2trGzq_0_vdhg87saiH9zP3zkTHhAfT8nlRsF0DvtkjcYfVS5hfJ5VUVu83j_lj9jevZiXgIJVVZhApf_PMIojx4aY-ylBEXoZUIEI4XPPuT950zo8rDkUZkzoAxHac1l_4CQzsJir2egm26Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c148f5e986.mp4?token=WMPKYwL-pBUyEeDFGKXaUQMQgwT40pVnjOG1EcjoS7ybsEkiaxcklV2l9dNhYV985Ory3sA7gsdiBNY2BmV9Vp5LZJRuQGsTdHAIdlZu1TeKDIG2IASBE4VNQVrt_H0e5Bxh6KAjGPGAqp32hMJuEmKA3rOvgiKmOalLnW3n4ceEibOxsrAC7NAtT7v_q_bvux-z2trGzq_0_vdhg87saiH9zP3zkTHhAfT8nlRsF0DvtkjcYfVS5hfJ5VUVu83j_lj9jevZiXgIJVVZhApf_PMIojx4aY-ylBEXoZUIEI4XPPuT950zo8rDkUZkzoAxHac1l_4CQzsJir2egm26Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی دونه‌های ذرت هم می‌تونن تبدیل به یک اثر هنری بشن!
🌽
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/691263" target="_blank">📅 20:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691262">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
شوک قیمت‌ها در ویترین مدرسه؛ آیا لوازم‌التحریر به لیست کالاهای غیرضروری خانوار اضافه شد؟
🔹
شمارش معکوس برای مهرماه شروع شده، اما لبخندها در بازار لوازم‌التحریر کمرنگ‌تر از همیشه است.
🔹
گزارش میدانی ما از قلب بازار نشان می‌دهد که رشد سرسام‌آور قیمت‌ها، خانواده‌ها را در «مهرماه» غافلگیر کرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/691262" target="_blank">📅 20:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691261">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jama0AKUTkCyz2MRhyeyvfh1IceVtNlra69THZp4RlIZ80xxtTed9Dhk8Z_GzTEYXGFfXFGXHTP7Eyxxs_kts2Ei6apdAKvGdKPqhgHvmgfYadwjhLZDyu9ixIvatJiD5Y8qqEj9Mwapnb_ydGj3ast3caZZxIDTsmoovmT6r4e_XLU27xJjSEuGAewSLuxsN9BYG2VLgoPGLsBXOzwqiTADqSPmitwQ1MsAmI50BE5Z6CTFPJaFCTMN4hG44otG3MiO08V2GVN6DzWnjGwflaYzhn6GDzPG-ShD6SdCA6SQKVb9n6_Fm6HlEVzDyY1iWcvJZTXZVoY1_fa2zkfyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: ترکیه مجوز فعالیت بانک ملت ایران را لغو کرد
🔹
نهاد تنظیم‌گر بانک‌های ترکیه اعلام کرد این تصمیم بر اساس قانون بانکداری این کشور و به دلیل احتمال خطر برای سپرده‌گذاران یا ثبات نظام مالی گرفته شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/691261" target="_blank">📅 20:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691260">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bis16vOUDqnFmAnKEImpzr9q0zLgMSglsy256z2fwf0gpCxijAQKONSJUE3TYa0TjGV0n6ATKvVEwi5-iMEPARlcTGQjWuLsfc5ThR--Tl-ThsIhZ0Uvf2GchvMs1eMsubkN9v_Jz3oyNUv_y9NBJbD-frygtCRYOg7dfo21syg1lg-tp2Pi200QAJDBcyFuECjXJ-BH9yh_NYEXBc3tm69DfOHv2hXkKwwtu14IDvINO_wpJvNFDUR0S3wb8b-43tyxhg-CnIYG6E1nMC5e2TygdyBt2PkHcg7I4mGaIDQxT3URCCqAhmiQvr2oPPUBh-H9rh5EUhL8DQzRhZ2Rew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به صدا درآمدن آژیرهای خطر در شهرک‌های صهیونیستی اطراف کرانه باختری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/691260" target="_blank">📅 20:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691259">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">16-1 Ane Manaee (1404-02-01)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/691259" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه شانزدهم؛ بخش اول
حجت‌الاسلام امینی‌خواه:
🔹
قید اِحترازی در تفسیر واژه “ایمان” و تفکیک مرتبه خاص ایمان از مراتب عام [01:04]
🔹
نگاه مرگ و زندگی به قرآن! حقیقت گرانبهایی که بی‌توجهی به آن، گم‌ کردن دنیا و آخرت است [05:40]
🔹
قرآن و عترت، امانت ثقلین پیامبر اکرم(ص) برای پیوند فرش به عرش! [09:16]
🔹
قرآن، معیار حقانیت و سنجش حق از باطل در عصر غیبت [16:04]
🔹
در دوران غیبتِ امام، قرآن حجتِ الهی و حقیقتی‌ست بی‌نقص و مصون از نفوذ هر باطل [22:46]
🔹
حکمت‌های عمیق و شگفت‌‌انگیز قرآن و روایات معصومین در عرصه‌های مختلف زندگی از پزشکی تا اقتصاد! [26:44]
🔹
قرآن نسخه‌ای تبیینی از عالم تکوین و مرجع راهگشای مشکلات جسمی، اجتماعی و اعتقادی بشر [35:03]
🔹
معرفی دوگانه حق‌گرایی و حس‌گرایی در قرآن؛ و تفاوت ابزار سنجشِ مؤمنانِ حق‌گرا و کافرانِ حس‌گرا [41:54]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/691259" target="_blank">📅 20:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691258">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
متروباس‌های ۲۶ متری برقی در راه ایران
معاون شهردار تهران:
🔹
با ورود اتوبوس‌های جدید به گمرک بندرعباس و تحویل ۹ اتوبوس داخلی، شمار اتوبوس‌های نوسازی شده طی ۵ سال اخیر به ۲۵۰۰ دستگاه رسیده است.
🔹
همچنین ۷۳۸ اتوبوس فرسوده در این دوره بازسازی شده است.
🔹
شهرداری تهران در پی ورود مد جدید حمل و نقلی به شهر است که با ورود متروباس‌های ۲۶ متری محقق خواهد شد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/691258" target="_blank">📅 20:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691257">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromستاره یک / #1*</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32dd295af.mp4?token=djNxTI7uNv_DNklo0BmghN4xyau1TyD1uFQR_TeryveTFyCOZ7Ywi2YZGJYZ6nEP8LKt-Gr_giShMugNK2g437mAgVhnk756X78sKhq32h9VVwql9zckamPEMvLbiV3dR7Pv2Y0XOtLTTH2luOctjkDTUiWZY14MRtU3xR89krGTt2FJtyPL4PaprkBOS6BadJ8BB-oS9vHWGbXOKvvmm-ECudX98y6hTizJ1glpicWiVIgyip2pvPkm7IzVvIs4d0hwYvraWtpk4rf0aRryOs2TQYERnvT-WIzlW9q9S44ietMOT80aaPQsTVs9CZBU5yH2Y94Z52EC7bvXEjOz0jFpSR0K4cQKHrt4R2pcN7cCvgJKpkaARKxToHunIM34TB8Pas6k9Gkz2WLPlbmYGOvKW8KiuFAZafQc_1a4vPOqUsClMrXsenTqGm95tXXCGY68HqXB3FDiHe2dMGhmzTj_avdTaHDpWQRAtuymot-LC3cZZYnDli7h4uXkyZ1HoVgw-YaingT7jQiLEqpZXm5M-1Dgseeqsooilm3o9Np76ZbS3KjFF4Y1Beta9nbHj_giOSwKlg6MzSvEiITxWJh2znhMo6BpChwHxY2YjJwzus_IYfrA5O4NPW1Cg6jajFLO1wBnT5Jcbwf_Q8qUF4SC922qrEDc9S_ne3QSeDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32dd295af.mp4?token=djNxTI7uNv_DNklo0BmghN4xyau1TyD1uFQR_TeryveTFyCOZ7Ywi2YZGJYZ6nEP8LKt-Gr_giShMugNK2g437mAgVhnk756X78sKhq32h9VVwql9zckamPEMvLbiV3dR7Pv2Y0XOtLTTH2luOctjkDTUiWZY14MRtU3xR89krGTt2FJtyPL4PaprkBOS6BadJ8BB-oS9vHWGbXOKvvmm-ECudX98y6hTizJ1glpicWiVIgyip2pvPkm7IzVvIs4d0hwYvraWtpk4rf0aRryOs2TQYERnvT-WIzlW9q9S44ietMOT80aaPQsTVs9CZBU5yH2Y94Z52EC7bvXEjOz0jFpSR0K4cQKHrt4R2pcN7cCvgJKpkaARKxToHunIM34TB8Pas6k9Gkz2WLPlbmYGOvKW8KiuFAZafQc_1a4vPOqUsClMrXsenTqGm95tXXCGY68HqXB3FDiHe2dMGhmzTj_avdTaHDpWQRAtuymot-LC3cZZYnDli7h4uXkyZ1HoVgw-YaingT7jQiLEqpZXm5M-1Dgseeqsooilm3o9Np76ZbS3KjFF4Y1Beta9nbHj_giOSwKlg6MzSvEiITxWJh2znhMo6BpChwHxY2YjJwzus_IYfrA5O4NPW1Cg6jajFLO1wBnT5Jcbwf_Q8qUF4SC922qrEDc9S_ne3QSeDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏳
چند روز بیشتر نمونده!
🚗
شاید این ۲۰۷ مال تو باشه
🗓️
قرعه کشی آخر شهریور
⭐️
افزایش شانس با خرید شارژ، بسته اینترنت و سایر خدمات
✅
از اپلیکیشن ستاره‌یک یا #۱*
⭐️
Setareyek.ir</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/691257" target="_blank">📅 20:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691256">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDTul7LZ_8F2_XMJss48rMg2BFma7GAHDYCk0sF1iE180AqEj_01-xvo1AYn2zM7dPizB-jk5emBLnoKkBgPGZw7Q_N0f2iEkPz-NlktQCUBFSUqqG2qkfFFS1qg_pa7wmg-R7w3iyVOCjFYl4pjq-cZ7InKDUq3fmc0K5kmxFYObOHRqNmPHnpDGSGOxl2gU-1QOa3z4OCGYrugMDA1nxzHupmwhqm4oGWJjnlTFYAWMULQs6fv6b9FOCirGBFLgZso3DAIVWKYSfFFusXIaLwhRPGnOxGWzFsco_-U3yXltKhASAf3xyadcDL4Gi-OygUVt5n7wecHLsnoh_kPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوشیت دیر شارژ می‌شه؟
🔋
⚡
با چند ترفند ساده، سرعت شارژ رو بیشتر کن و کمتر منتظر بمون! #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/691256" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691255">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn5oMCj39PmjByNGsx8_9EDC-mbxZms3cSl5hDDK18ygL7tGZ7OhSI0BlmUOIQzKLl6Fo7DiImIVi_3-UfnpSHBYn2qKGuPalL0SUToa9i0UERSDEFKYQvItPFQGJqxkFg8pFJMseCr84k4n94kXmMT6lb6ejxmPheJfKMj_LKj6Z9sp0oqGu3-Hqh53fIZUdrSP9IfpLZJ-LbO4d3gxxADLHlYkzTtXgGdxQi26w04w0OtKy4xoiWP8o_OHNiJeNScj3i8QwdhfYBXccajvYe-W41FH1jAFyGZi2TbFtVMyZ-CUrAMq8yCaHz9hzoJRZUL6c_Ub7VAyR2lOwrfQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عربستان سعودی: یمن به مکه حمله کرد.
مکه‌شون:
به توییتر خبرفوری بپیوندید
👇
https://x.com/Akhbare_Fori/status/2101314072545480794</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/691255" target="_blank">📅 19:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691254">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqeiP6AdjV5ct-J8Nipdh0EedUEn5V3nyo2SQ93su3abT1wRmW4nlTTlMABUk1h3TIL77Q2ks968Y8xJoSoRHdXIAIuh8AyQHGTBGEJ950CCzsakPRG7EC5ioJ9dEPAkFU3hl1BKKcT64AIPywdv6kqRN0mKDu2zICnuLqztHg24vYIkN1FFH8CldlG9rJLB8hLNsaaXvEbwj9mL3KL31BkIZc8xHrSUVhkQey1dafsuAHKptZ22C-ZpdFqyUKYdANuo6CY_xoGA5VJdDCDRW-ntK1UfY4TaQzskb70vwuR5uy-i9kucHA309g2KlWs5F1yWoRaflpNNF0Iq6qJ9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر اروپایی: پیت هگست میگوید اروپا بیشتر از ما به تنگه هرمز نیاز دارد. سوار یک قایق شوید. این جنگ آن‌هاست، نه ما
🔹
این احمقانه‌ترین و شرم‌آورترین دولت آمریکا در تاریخ آمریکاست. خودشان جنگ را شروع کردند و حالا می‌گویند: این مشکل شماست بروید خرابکاری را جمع کنید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/691254" target="_blank">📅 19:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691253">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZuGjcVJAAol9qkaWSJJ2PL1ZiPv2isG8uWHJkXpxGa5CvOnHuhaFMl8d6i2gbpCoFaPQ1DmK4mgyq6ndcnVovq2nSuckxl10hfJ8xpF6MNe1I9NecrVtkSIz1M_nRH2FuNtzPMwt0Zrf0O1dUBch_z6yzmVtPUAINI-WYNqdx1MlnPF_BkCHy8-OKGZZs4D8ultSXoBITXeGVALg-OacnbEq8A8d9skn1X0X37aX9NMa36JBMusDMr8h1ri9dZtQ9QGlLWC_GEe9Sj_x19qGcqPMxOZJzSJLb3j2hRcX64NK4Qey6CeFz8iweM3GRhFyG_jA8nc0Cj8Xua716MIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لس‌آنجلس‌تایمز نسبت به حضور صدها هزار جانفدای ایران واکنش نشان داد
🔹
لس‌آنجلس تایمز گزارش داد که صدها هزار ایرانی روز جمعه در مرکز تهران تجمع کردند و در جریان این راهپیمایی، بر آمادگی خود برای به‌دست گرفتن سلاح در ادامه جنگ با آمریکا و رژیم صهیونیستی تأکید کردند.
🔹
این رسانه، تجمع روز جمعه را بزرگ‌ترین نمایش مخالفت و مقاومت از زمان آغاز جنگ توصیف کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/691253" target="_blank">📅 19:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691252">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سفارت چین در عربستان از شهروندان و شرکت‌های چینی خواست با دریافت هشدارهای امنیتی، فوراً به پناهگاه بروند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/691252" target="_blank">📅 19:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691251">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdef470d2f.mp4?token=YSLAaVphT-vzSp8JMQRfCJtGDQrGSctS5_ube9EywN7GH7Nr4FXuyheGBgc7dmSjmhH3Pa6PzJB09gQy50I4muk36eYMnf8tH3qpm3_ngCEUoxzrGYpO3DuFJZEn1RdQvkQtlxC_YYc8jkzbD_phqN1Oc0_Io-dx_Kl0SlSwVUSDqaL3Jx67uq2jy-WVp2w3l-yfFKg_YYlGfXXvmo4z6JgKpJH06TeRgh_6VKjukvG8nfrmOjAy7aiUA6-tu8SWI0TrMwybUhZbpYKebKH14sYNeTHvSxkzythgmexoT_ylIqzc8fVtg6Af-uMVQIx7ifk1sPE-TUcB0ptNdsY0tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdef470d2f.mp4?token=YSLAaVphT-vzSp8JMQRfCJtGDQrGSctS5_ube9EywN7GH7Nr4FXuyheGBgc7dmSjmhH3Pa6PzJB09gQy50I4muk36eYMnf8tH3qpm3_ngCEUoxzrGYpO3DuFJZEn1RdQvkQtlxC_YYc8jkzbD_phqN1Oc0_Io-dx_Kl0SlSwVUSDqaL3Jx67uq2jy-WVp2w3l-yfFKg_YYlGfXXvmo4z6JgKpJH06TeRgh_6VKjukvG8nfrmOjAy7aiUA6-tu8SWI0TrMwybUhZbpYKebKH14sYNeTHvSxkzythgmexoT_ylIqzc8fVtg6Af-uMVQIx7ifk1sPE-TUcB0ptNdsY0tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فلامینگوها مهمان دریاچه مهارلو
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/691251" target="_blank">📅 19:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691250">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPut7QTpcZODlrPegMxCDoCmkQHr4zXHqpgOhot9Hig5DdlsmvjzOC9fHR-HS_6K44FhZWTwP84_NEFNoDF8O6B8z5ZtoutKIwi4zIr4cIMN1hfWdmcvMSnrSJ8-Wp6-3vgMIpDa4oGVGeNGPCqZFBbS4PViz4fP8_BekF-AqH7NN4nYJfqq9Dt8g6R4mipSWsgfoI7yQn-SVIm7oj8Bz67YbXIkhnWXIbG2aN7y0cc5XoiNJhlouYeX7jI2nwGSGO70kxl5z54zymploJskKGTH14ev9eiNjkRTICmruGBdm9FvxVPqgT0QtY2XVQNZCVyiUIEDai7PtBXrosHtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جانی‌متواری
🔹
آمریکا در حالی از شورای حقوق بشر سازمان ملل خارج شده که تنها یک روز پیش از آن، هیأت حقیقت‌یاب مستقل سازمان ملل اعلام کرده بود «دلایل معقولی» برای مسئول دانستن نیروهای آمریکایی در حملات به مدرسه شجره طیبه میناب و یک مجموعه ورزشی در لامرد وجود دارد؛ حملاتی که می‌تواند مصداق جنایت جنگی باشد. خروج آمریکا از این نهاد، در چنین شرایطی، بار دیگر بحث درباره سابقه اقدامات این کشور، مسئله پاسخگویی در قبال نقض حقوق بشر و استفاده سیاسی از سازوکارهای حقوق بشری علیه ایران را مطرح کرده است؛ مسئله‌ای که می‌تواند نگرانی‌ها درباره تضعیف سازوکارهای بین‌المللی پاسخگویی و تکرار حوادثی مشابه میناب و لامرد را در سطح جهان افزایش دهد.
🔹
هشتصدوشصت‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/691250" target="_blank">📅 19:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691249">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs1ABfzblGDwlwrREubC0O9TSanLwtH_c-twws0IlCBl0LehP4Itp1Yyh_6VZMGE8f7-PWYDxYkF3dqNZiMzRRo96MSvsljt_jvG2PVf7jMEHGCSpYMQ8I5YLlLKM11OATv8YV4MqQT_4CBLaa-AKHkss7flcmXjOvRx87Hk5DRENqO-N8AS2JV0Llk5oYMpUY8YwGAACRUOeQtu9vpWwiffiSHtXNK8JchlRYlYRBQR1JnSs0uoUAVtX-BNL2IS1klqv13c345HKmOW-fBWXF8utIZyIxv46rW51zYZtU--XLVMnO23HCY-Lw9hmI74EzHydcqY7JTg0zHLVbSVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساعت کاری ادارات از اول مهر تغییر می‌کند
🔹
طبق بخشنامه سازمان اداری و استخدامی، ساعات کاری دستگاه‌های اجرایی از اول مهر تا پایان سال، ۸ تا ۱۳ تعیین شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/691249" target="_blank">📅 19:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691247">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgJmqp3n5HWjhwE7qGvhfGndzqNqRh2opJtf3IgdBL0BeA-Fqk5ygjf0W8x2R-_QTYD3VcpZz1ETd9tT5LeQ202ytQUKaeyE3ZVFjnaI3oE4hl2IpR7oqe7CpJRmyLaym6GV6wy8tY_pvgg6puvWRuV0rrjTSRDkJg8tdmfgfP5xp47TMRkRPzGMkBWK9T9HRUaXE-ES6JWJtO15jWHT_TGka_VhNXBT43sQs2O99cBujTvgDDfriebDpFXAnhIb542ib2Rdmff3ToONbmV6qlzjhtb68QmFnlH0VvDxExLt5a0uR46qiZaTX5cftXE5WGIIwrJnCbAsJ1fOeMNC_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZxS2gtUiUKp0maa2EscYR7QvdSEQRycqvs_h3qPRqgAiNtOPJbgF0fCwn2OKKSq4CSC5tSuwT9_kX_aCp3cfMcibigbaT0aM3mTr13mm4SVea3veU2smKp77vzJq2zIIPW0354PkgTEt56KKKX-ZCsbXtQB0wE05VsSvTvpuNadxrf3N2AguxcVOFPjXwUKxGyfI8CvVPC6OmzUhHAfkGhwNI2yMCvmj9lGPnt9qebj7Is4iYH6cfjBbSnfQTmD0KeZJJsPqpPkLR8Rip5eg1aB8M_LhkhCDyr5pw-VpEtUHngIStfUnKSv1A28veMVslaEAN2XGbLONgeK-8QkcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پوشش رسانه‌های عربی زبان و انگلیسی زبان الوفاق و تهران تایمز از رژه عظیم جانفدایان ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/691247" target="_blank">📅 19:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691246">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
نایب‌رئیس کمیسیون امنیت ملی: عبور کابل‌ها از تنگه هرمز منوط به مجوز ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/691246" target="_blank">📅 19:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691245">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
محسن رضایی: ما با میانجی قطری که شرایط ما را با هدف توقف جنگ به واشنگتن منتقل کرد، در تماس هستیم و منتظر پاسخ  ترامپ هستیم   رضایی:
🔹
شرایط ما عبارت‌اند از: پایان‌دادن به جنگ در تمام جبهه‌ها، آزادکردن دارایی‌های توقیف‌شدهٔ ما و پایان‌دادن به محاصرهٔ دریایی.…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/691245" target="_blank">📅 19:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691243">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
محسن رضایی: اقدامات آمریکا و اسرائیل این اجازه را به ما می‌دهد که از معاهدهٔ منع گسترش سلاح‌های هسته‌ای (NPT) خارج شویم. هنوز تصمیمی برای خروج از NPT نگرفته‌ایم و این موضوع به رفتار واشنگتن بستگی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/691243" target="_blank">📅 19:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691242">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoO4pIMmAkzlwzCSSVX_h5WoOK-Ip6FAr-Uzk-6c4C5Of0_gL1YWJa4lAq48Dh9p0Un-qHdLGsDFNjxgzsP0e_Z1wjytjGmdQB3SMfmRgnU8ToK7T0519HQNNm7DIoVcMuzPH_LwlnhS5NE4d0vMGgVihIWaQTFvueTUu_WO5oi8ZVMQJvSZBiEufgE52pXj8TzhARU5mgkJe8NJpyCJnhvGIpuiko5PALIfky8fS_b_LZIM0Tr6cS3r4FRsN6AMwyf2UIyTlH2NPR6DXMq05FPm4-atCmvTcw2owDmE39K_KIh3SjowO8gJtiAHZrMaa3VqC10P_KjfjvV1GJBqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل از اینکه یک حادثه هزینه سنگینی روی دستتان بگذارد، خانه‌تان را با «جام آسیا» بیمه کنید
آتش‌سوزی، زلزله، انفجار، سرقت، ترکیدگی لوله آب از خطراتی هستند که می‌توانند به خانه و اثاثیه شما خسارت وارد کنند.
🛡
طرح جام آسیا؛ بیمه جان و مال
با پوشش‌های متنوع و
۵ بسته بیمه‌ای
، متناسب با نیاز و شرایط شما.
از سرمایه‌ای که برایش سال‌ها زحمت کشیده‌اید، امروز محافظت کنید
📲
برای مشاوره، استعلام و خرید بیمه جام آسیا کلیک کنید
👇
👇
https://online-li.bimehasia.ir/issue/jaam
https://online-li.bimehasia.ir/issue/jaam</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/691242" target="_blank">📅 19:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691240">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
محسن رضایی: اخیراً یک موشک ضدکشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کردیم. به نفع واشنگتن است که برای خروج از جنگ، شروط ایران را بپذیرد  دبیر شورای‌عالی امنیت ملی:
🔹
ما همچنان به فتوای رهبر شهید انقلاب پایبندیم و دکترین هسته‌ای خود را تغییر نداده‌ایم،…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/691240" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691239">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/713eda6e84.mp4?token=VsGWJeDNHKXCBiMVw-kF2OCnlO7Xxb8UT4G4qbUHbLUZtcmX1NcCYhkftrskr-WQGrMQKNwORbGkvjJZKsa3tJBKHM6BWal5pKHok76CVQGMjYjIzvLPgl7Emjq73LYGxZM-ALPENrUNhx8Ss9FPMogpxDmg8w6aa9oItv-r5HLLIQTeYVVSP_COvQ-FeDC8P1kkDg6ckK12UpQNgPhkNpiOiEZkeS9pOsr-PNWve8_vHtxhzF2S04tZm6b3wxTTBoBquYT2eDREH8d_H7tU1MgYqkEsvdqTInuHwNHvtdf6TKZjg1lLiWNwcXn1dYEy8AvQ11tem6NotgiS5mu5Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/713eda6e84.mp4?token=VsGWJeDNHKXCBiMVw-kF2OCnlO7Xxb8UT4G4qbUHbLUZtcmX1NcCYhkftrskr-WQGrMQKNwORbGkvjJZKsa3tJBKHM6BWal5pKHok76CVQGMjYjIzvLPgl7Emjq73LYGxZM-ALPENrUNhx8Ss9FPMogpxDmg8w6aa9oItv-r5HLLIQTeYVVSP_COvQ-FeDC8P1kkDg6ckK12UpQNgPhkNpiOiEZkeS9pOsr-PNWve8_vHtxhzF2S04tZm6b3wxTTBoBquYT2eDREH8d_H7tU1MgYqkEsvdqTInuHwNHvtdf6TKZjg1lLiWNwcXn1dYEy8AvQ11tem6NotgiS5mu5Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرخ زندگی
🔹
مسیر موفق کارآفرینی؛ داستان کسب‌وکارهای نوپا و موفقی که با پشتکار رشد کردند.
🔸
روایت شما از آغاز کسب‌وکارتان می‌تواند انگیزه‌بخش دیگران باشد. در یک ویس ۳۰ ثانیه‌ای، داستان شروع کار خود را همراه با تصویر محصول یا خدماتتان برای ما ارسال کنید تا در خبرفوری منتشر شود.
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/691239" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691238">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: به نفع واشنگتن است که شرایط ما را برای پایان جنگ بپذیرد  محسن رضایی:
🔹
ما برای یک جنگ سرنوشت‌ساز آماده‌ایم. ما نقاط ضعف ارتش آمریکا را می‌دانیم و بیش از هر زمان دیگری برای مقابله با حملات هوایی آن آماده‌ایم.…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/691238" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691237">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: به نفع واشنگتن است که شرایط ما را برای پایان جنگ بپذیرد
محسن رضایی:
🔹
ما برای یک جنگ سرنوشت‌ساز آماده‌ایم. ما نقاط ضعف ارتش آمریکا را می‌دانیم و بیش از هر زمان دیگری برای مقابله با حملات هوایی آن آماده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/691237" target="_blank">📅 18:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691236">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: سخنگوی کاخ سفید فهرستی طولانی از اتهامات علیه ایران مطرح کرده، اتهاماتی که بخش عمده آنها، با دقتی شگفت‌انگیز، همان اقداماتی را توصیف می‌کنند که خود آمریکا آغاز کرده، مرتکب شده یا از آنها حمایت کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/691236" target="_blank">📅 18:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691235">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd708c6b05.mp4?token=LtgXpHxBVuL7OpMyZcmpeaEM2wTQsgLx05ZB1ukqIhkNR_tKbQqYDmzAwKrUoSM704mSRZGd8LxSBRcsjtTWHCBP26UZSZYSzpo37XZ4mooH7SMzgs-eAd5bTxy8M4sJ91x9JAbU-pn0CDWTka8hLw1Q2tX4sNEqESwkYpjCt_Nd_nrYLh90gDIXugBqe0jw45diIRdzEECLtS-guoSC5-5J2syuCweGmKGFjoTIyFdalT6s4d9PbdpGG8f_kYb9UJa4F9WVGqZtT4JE1k4CtvTfgTkl1El2SqjIdHXKHWWsVSh_dM5r4TfgVfCGbJsoqhngfZQhhXWBy1_94PaSVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd708c6b05.mp4?token=LtgXpHxBVuL7OpMyZcmpeaEM2wTQsgLx05ZB1ukqIhkNR_tKbQqYDmzAwKrUoSM704mSRZGd8LxSBRcsjtTWHCBP26UZSZYSzpo37XZ4mooH7SMzgs-eAd5bTxy8M4sJ91x9JAbU-pn0CDWTka8hLw1Q2tX4sNEqESwkYpjCt_Nd_nrYLh90gDIXugBqe0jw45diIRdzEECLtS-guoSC5-5J2syuCweGmKGFjoTIyFdalT6s4d9PbdpGG8f_kYb9UJa4F9WVGqZtT4JE1k4CtvTfgTkl1El2SqjIdHXKHWWsVSh_dM5r4TfgVfCGbJsoqhngfZQhhXWBy1_94PaSVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش نوشتن پیام‌های طولانی با گوشی سامسونگ؛ بدون دردسر و محدودیت!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/691235" target="_blank">📅 18:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aobj1cjjyKPg6KWO4u54HrQVEQIG59OKjKA_fntJA3VbpHZH3mdzlH2En-SR3zBa3qXkdpfRk2q6MkH962TxnjHWdRSlMzfnpYMBL1k8oGdqoT8N-Rt6d-QXxymSTz8lNhy___F0xTqecGDuyzvJnHWaBR5Pk7kTVKPrBds2XUvztHz5TlM2c1V7udDxJV2kJB6xUYal2aanaegLlul_5_rpbPzgs4Ha51ClazuZLwj46B58Tn4U7j0CJ2WlQhd2ssLx0GnQ788JMykXnLnViud-lQwAD-7zjjBjZFNuuyjsrp8RxVR_vPInzMXSKgeLPdHRjNvyDNuTRONgUU-TvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8Ls33LCJew7q5iU1IE3PvH2WTGnsA1t1ds9AtDqDlrghFvjeLKsAGf74b6C7CEzf5XUsj4PgmFHXL-Yxq1COB5kair-2EENtQM8lltcgIbutpOMWr3bIk5Ghfs6ygfYGdVI6Os2Selp5HgNZlD9R4JEJACxt8A8UpZZzTpPTczvV0agfTHmrFF8eU32ZJyhdCKG6eXziZsVQ6NwXIYkQYE6hgt0aB8-bn6gcAEMtAKZ8vyUcg6z0v7-QukIDxE87_FXqBFC9xWJOi6JsbMTXjEUVuQdzN3edowe2V03XjTfqKQPQsjudqHYThK9li4qdDtSWuRhlBqFiWe736WsGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCU_r-5K5cwS92K72HJL5RJldcE_aXjUcE7MZBEw4iV5eUbHGRdEZ_v15CcGMEFDe4OmJsWPTjIpIXOMREznXdXZYzzZhURDGCp9Bc2GCROlAOek5D0j9UVihJVHTPoL3aMBYQqGzD6UKWBKm--omRZ_u-0bdu_kCDUCG6FOKE2MCsJLTuiHB9d4SdXdgNKZnn3GSioqOnE6pe7BH4TzGKzwnqgygkORbG4XUY1-S-O_lBBUzrvk9QbF32YyNA27RudBdhN-zDTHi1bK3G9I08jHxYW7wf9BUyO1BuLk7cj-efpiFprN4oQZhDVm8lp-hULT0PrG3mCX_TpBUUkxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lucoR2zLlRCRl9iZI56nJVIp9oE67mVbo3ZNeQUbeF9tPwjSCvjD-q7Oh15nsfOUmDhYSDDBm1GhK4t5JTyJFSIb_vcKewlJ4bRNsma5itVdwKP2YjfWgznbu6OonoJLpmGcjavMHj34psRNRVFoD6MsTJEdv42oHD9c5Ui_-lY1urNPam0DiuLFsgyIHVaZBBoW0FuT7YwS_ZnfeMNBuhhu8kVFUCRPAxxuMvUo28EO_6ffY-7MtnA3zRRMV82A2TbNn7Qj4EUmxlGDurxL6I_Zf13dKnwnMMFqsP7Urgtu9MoL07kXaoGYNh6spRwf9K8MjQwcEn87IRuxOHWtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnecApdm_8xhj_Pta1pbx9FXquQbLgdS_PEHg-YLh6K7wr6joSx2TJ26HUpKNxdTHSXpiemjCkwWDJd5SncXid3fvGxaHi2vAJxHbXmnxu3mvrwnFnLifIjNiLufk6D4PbQ1Td1lhdQLyQs1i4s2wTdoFjo5jj1T5cPxmDwBU0fX-Kc_COjOZbIIDcE6nFi2wnHumIBi5fbrjGYO6Fh9DfslFAuCpvzrQIUVhutKP2WcXTzx-9UZp_Cff-qVX0wcJEZVZcv_jdWll783EbKwybvh-8V-LMjTUIJCEeUiq4_WValTkCZo4LvkWSAEaT3iAuVPoBR0sA7n-Ozi-Xt3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5To3_Mxv_sqY9lQX3Tdo9fI-GO47_8Xve__1zY41TIkO1SdbAX4ong5yUu6S_VaS-RT4GBcY5aeADnwmjDTwyJh5TVFT_Frle7AmrgAW0iwTaLa0D56eIV1j7sqT0P43NcOVh3_XmexlidpXwn_dQcNzgD_D9w0-72KZ6FPdkeWXAwJ5eYmmC1LRUxp-UWxhsMHz6a2j8RaUtiGrBYkgLaEJ64ybOBRTWtvT7IUB0EAg81dfRo9u3nEd3u2OY2Y9706ZZ_xyVGbJhUDrq5hnKcY52AKrcVM8qlIhLQG1cqrlKn4UZxeay6rBHbGAq6EUEqq7ELqcIuuyEWdWox7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4I19XYfQ2iZoDZH0nJumtWhjptpC2_V7Pn9Lk8ufPnTNrXHi0k1aXa2tOMhqRt_0lCW38tlqYv0Vjsb0Qvn1fKrZaSOr51rD_AE0mctYxjzf8Vn2hZNpA7T7SESuzHIhj0yQ3e91FhxWNX3osUVGs-5HzxCCoCmWiYKZtvdzvgwYSfjYBjAxWVRcXrSKTNv7Qo5SzVVBDfNp3tNbH0xFNMnEAsrE12u-e0TMgs31UHpi29K94I8Wni62hX_KGvMSgd_B0ITmoGZ_NRtJ2ZxbSA6nemsYEpvDSWU0lUb1C7Ocdillj8BCYLOx9_1rev4MRUk8JzUWzBGJAh4CItxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eyiTRsjbVfyrrKpk7Kjt6nYIClY-QBP5h8edM2aAF1zLFFoUF2TsPXk1d8KYT44yJKbmRxXwNKMi21GvnrjYmjVJ_KKkp990ZVh5I2Da30ZVnA2PgsEJjC_artMjQBTefhFAPSMs5-f3XCo1aq6ao7rQhcTt_1PovwSswp-STmESiyeFUm7yA_MehXSkm_A3Rrp_QqPWgk0bX0QnSBjGk5UqlMYFm_KuZw11pvHDcBnyMgFY5z7PBA93WPLhxZgUWwko5m8hXQ9NV9_o2SRAB9Q62YsraoWAa-w48kl9P0DRPYJn2puTyKZiL9n7sf-bIkEEPouhcrboyvza4nwfAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پوشش مطبوعات داخلی کشور از رژه جانفدایان ایران (۲)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/691227" target="_blank">📅 18:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uROMedK3W0n4fLDQqXfRK3nZ2hJDeT7dP7f0KBEI1PcDdc9tRk0v064QvXZiIs6rdVQL0BNb4kFNkFgJRgsn8_RBZ-JsUXBhC3049m-uMIcByrG-8nUBWN9Zkj9ifZXWiKJ7OEiuR1p7xsJ3Sfk8IsjEblDwQcUHPGrYM1fFbxJWeO385fiYjSE3Z-WrGysd3U0pfDYZ8bGljKIVwS22YNf3cx2Qz_iep8ABjK4aBHZK2PVVNlYC4cVyQbQTYoOzRi8EuoEIAcKpEp-4UNnb49xmqejVRwoeut27UdkYlmq2g0hZE5Hs11YwsZxfBYB60JJkJz_vR7iArXCi2daqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام
انصارالله به عربستان: حملات بزرگتر در راه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/691226" target="_blank">📅 18:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691224">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtyDqyGdF80OYMzZ6hfxNo1Jbi5OF745YfBUQLmp3IuxMniWFi3qoqiKpIfuVA0Q3q8QX4XtSpbTEG3_73cq1tazSRShaOVf6SAmpXydhthXcTl6M56FfhOWePd6aPmuCrzaGC0anCdKyTiZlBCZ36YiDBbH23miCOEX1ERE3lyCVCnyCy9zl4OfJjN5HS2saYCAb1aM8jLswts9nQzE2rBBpNavLxZktiagRwvBeuz_RzYLPdp0ROnwWllMDpuDAq81npYBpzzgtWQiboyvsjdJ1A4kEcQ79I90LL4US4ShtrQNVNaflODX2KDP19TJvmVoW0txZC0Bm3BuaQ5jDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wkjg2G66nq2c_FRNVopWoAmD-oE7KWGfYR1BVF4e4--uCEvs1K97DCFFdRDVtPf7mGwMzW5PsQuSaIRmdqyQQi1PcXZNK_ZOolTUZWNey3zBSTocFJjXQouPKr5GuHMFtq8keoVfwm8PO-23o0zIjK1oz6K0ly0aTILTSVjhoAB3-l8CfLk_rjYriIPwjjKllpp536ZLLROK9YjIqrhhBgOEdSA-EybrKzFI-AgAPEHQ0R_L_md6ejUje91OOXLN9umsk_HgOFZ34FZDSDZ_Oy-v0ouUA3nOrJaDgho39JY-qx65l7r7D9WejczmiwNfvoUCK0VXvJUg-Z5ApN8U0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جایگاه دانشگاه‌های کشورهای اسلامی
🔹
بر اساس رتبه‌بندی تایمز، ترکیه با داشتن ۹۱ دانشگاه در رتبه نخست کشورهای اسلامی از نظر تعداد دانشگاه‌های برتر قرار دارد.
🔹
ایران نیز با ۸۱ دانشگاه در جایگاه دوم جای گرفته و کشورهای پاکستان با ۴۷ و مصر با ۳۵ دانشگاه در رتبه‌های بعدی قرار دارند.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/691224" target="_blank">📅 18:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691222">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f01df87d.mp4?token=DHpQ5A6LdEt7KBGQZaTOpLbKo8D7U85l-6xllKQqe18LNBqSsoJ8IYnAUWZ7922qajgpafs8y3JQkNlZ4YsLEyd0UbPi3A2uJvY1u4UuEL0lNp_nZkCTRuDeH7jJBIqqQSKeOPRSzck5wU57XZwN5i_RDDPllOadgMjMnqsyzTci31xc-X4U4tvrTuH0YUZspA1uwgWfRxDkyeuDihmiTSRHQKGpIfH659nemyi6bqypO7sbq9s1rcWCUvwPITvm-5l7XN-cpDenYyZ7axDVQQHQ-EEsBYPASxcc23go_Sojp0QkIk9jxFnGNRx688bp2CHNIorfFksufsTjNVaZ9TU4rsDfg4T4xfvpCo-pEbCN36Y_XwMjdYv3VAxXCSZTKkW-Z6iRUrlP1-KuZymRjAtH-iHPM2PJaVkgjMZbLvyNUHGrmUPnKTq6b_0WS0UmDweeaXrtqZ5VNzVsfnnQCLaKGnzT40o5OQ9Aofg2ErlBI4VRsT1_GvvJZ7qemPaA6uvoGTY2ubiZKlkpo6BGEG2JygwnFLd4rwN0_zOWJecDCpdW74VSNa7J7KO8P-TsmzGiBp98oaSa5jWpEoYMthDypcP6JXKFJLz6k3MUW9EggpAZyeFiXxJvFJNXvHJO7jkRoKcHUz0OKquTAaYv9s6LBakkKxRT089IrBldE1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f01df87d.mp4?token=DHpQ5A6LdEt7KBGQZaTOpLbKo8D7U85l-6xllKQqe18LNBqSsoJ8IYnAUWZ7922qajgpafs8y3JQkNlZ4YsLEyd0UbPi3A2uJvY1u4UuEL0lNp_nZkCTRuDeH7jJBIqqQSKeOPRSzck5wU57XZwN5i_RDDPllOadgMjMnqsyzTci31xc-X4U4tvrTuH0YUZspA1uwgWfRxDkyeuDihmiTSRHQKGpIfH659nemyi6bqypO7sbq9s1rcWCUvwPITvm-5l7XN-cpDenYyZ7axDVQQHQ-EEsBYPASxcc23go_Sojp0QkIk9jxFnGNRx688bp2CHNIorfFksufsTjNVaZ9TU4rsDfg4T4xfvpCo-pEbCN36Y_XwMjdYv3VAxXCSZTKkW-Z6iRUrlP1-KuZymRjAtH-iHPM2PJaVkgjMZbLvyNUHGrmUPnKTq6b_0WS0UmDweeaXrtqZ5VNzVsfnnQCLaKGnzT40o5OQ9Aofg2ErlBI4VRsT1_GvvJZ7qemPaA6uvoGTY2ubiZKlkpo6BGEG2JygwnFLd4rwN0_zOWJecDCpdW74VSNa7J7KO8P-TsmzGiBp98oaSa5jWpEoYMthDypcP6JXKFJLz6k3MUW9EggpAZyeFiXxJvFJNXvHJO7jkRoKcHUz0OKquTAaYv9s6LBakkKxRT089IrBldE1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کافیه این ۱۵ ساختار زبان رو هر روز تمرین کنی تا خیلی سریع انگلیسی یاد بگیری #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/691222" target="_blank">📅 18:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691221">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c94427c5.mp4?token=aNjewiKspeyecyG9Dtt7qzXNP8IEztwo54BZZZk2R3KMGGKnkhudIId-LDMXHBEidqvp-iFkk1HQVnFh-vHtA4xdWBd527DgOX5FtujdLrWpPx8QA6fm5Q4bECo-jhskiOOgbyfgfaiJ6DCPWVFzRFMWc-y7lytut8W2Je5WUX-elIY7vUBTG7zWHecB47KbNf0b0WUY2ODvrRFtzLn0X6RvPB3gz3o3X57E1t3AXUJfXslHEab5BXySPLzDMiPvP62NyXn4jRga9CmKSSqk8myfcHJb4ydA1-G3XD76qQTysbw5MRm1VhDzj1k3oKSjtHWqFXyHg1Cy-ScZ9ZQsgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c94427c5.mp4?token=aNjewiKspeyecyG9Dtt7qzXNP8IEztwo54BZZZk2R3KMGGKnkhudIId-LDMXHBEidqvp-iFkk1HQVnFh-vHtA4xdWBd527DgOX5FtujdLrWpPx8QA6fm5Q4bECo-jhskiOOgbyfgfaiJ6DCPWVFzRFMWc-y7lytut8W2Je5WUX-elIY7vUBTG7zWHecB47KbNf0b0WUY2ODvrRFtzLn0X6RvPB3gz3o3X57E1t3AXUJfXslHEab5BXySPLzDMiPvP62NyXn4jRga9CmKSSqk8myfcHJb4ydA1-G3XD76qQTysbw5MRm1VhDzj1k3oKSjtHWqFXyHg1Cy-ScZ9ZQsgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک قبیله بومی منزوی در آمازون که از هوا عکاسی شده. آن‌ها نمی‌دانند ما وجود داریم؛ و ما نمی‌دانیم در ذهن آن‌ها جهان دقیقاً چه معنایی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/691221" target="_blank">📅 18:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691219">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caugzHpFW6s2DYbzwaVOKXFAfRKNnOF04FgPLISBCS4VaFaJ2kZ_3ETA5nGrKWwL2O7lvNxHemWMfoGc-WEpB9mxc3q3MHNiBW2lBW7tzl90ps-2JWAIt1MaY8rszayfmFrQ7dSmgcPVhcTYNt_09L9wNtBowAFt9me28ciyD9ihhJY0u6Uz9Nx7Xi-I-HfrA8n3j2AfY99dFTHdyk_gTcOMvrWM30TwsSQO8i8wZ-a_UthYzwf4DKKJGGXksOrPpSOImFJKCXEkWavFGrhoaowI5jv3PRg6E5EH2riMk1EMX6P4N5qYIbvj3YiU_y5YKhFBFjT7eiWRudh2V6r4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخبه و مخترع باشرف، خانم لیلا کشاورز در بیست و پنجمین دوره مسابقات علمی و فناوری جوانان و نوجوانان آسیا در مالزی با کیف مدرسه نمادین به یاد کودکان میناب ظاهر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/691219" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691218">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcP3JuqO4dCpK0xS4U2VkfG7Ew7dodngbMzXKq6cOtGaJWNd97SfnnzyZXPq_cgGKkJua-6n-8CNTmeSuGqsBKfc6MIN9TQkmcEnKihV4qWpnoWFRLFoKjvumFXK8I6hCZh305ybaOm8gy5EiC8DT9JpQ-yueXzT3gratpNYnIaN6ak9E23ajfx-rn1qS5A7p2CA82QUzLAUNf39OO7t2JKa5Q0D9Gkh2vJKi53XwGMjjUzLXfC3m3Jq3QTqNIDg4QKN_FTRs9Ds4dWk5Pfe-b-f9IgZDBUlG-IAGFa6blbvfpI1kXVsXJi-gG-Cg_yUho9mNcbcnCg_eKERWIi4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه سفارت ایران در مجارستان به بلاتکلیفی ترامپ: راه خروج از جنگ!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/691218" target="_blank">📅 17:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691217">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40dcd9622e.mp4?token=FHWcjkTRV-6xOOBB7fh_HMVHD2ziqmSIEzBln9IxE0YmWJZlVEE-SsFYPWAYwEbHGbQPZT3AYqdfe7XJ-hMOQA1fhjzNn3AOjhjBWoRoVCNop8uyYeZ0PEc4-60X3glxaQdsGa7EJFw8_rF8LniPv1Ed9W9TedH82Ylceb7UM2xcsolY8zjRLvRC9q2UZP3wHRepzcstaAMgD49rgf_GFkTLVUFcoqe99iCDeLbgorzljLclleq_jC5PVdfjN2Thz0EIUyR9aZ30-dkstmg6plcyiR3E_Fd3N4FD49dsDIAmZU04EP8Ce-PdCG3oLJPJeEPRooU3Dqj0gKzXyG4IZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40dcd9622e.mp4?token=FHWcjkTRV-6xOOBB7fh_HMVHD2ziqmSIEzBln9IxE0YmWJZlVEE-SsFYPWAYwEbHGbQPZT3AYqdfe7XJ-hMOQA1fhjzNn3AOjhjBWoRoVCNop8uyYeZ0PEc4-60X3glxaQdsGa7EJFw8_rF8LniPv1Ed9W9TedH82Ylceb7UM2xcsolY8zjRLvRC9q2UZP3wHRepzcstaAMgD49rgf_GFkTLVUFcoqe99iCDeLbgorzljLclleq_jC5PVdfjN2Thz0EIUyR9aZ30-dkstmg6plcyiR3E_Fd3N4FD49dsDIAmZU04EP8Ce-PdCG3oLJPJeEPRooU3Dqj0gKzXyG4IZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش تند حامد مدرس، مجری کودک‌ و نوجوان به لاله مرزبان!
🔹
چطور تونستی چشمت رو روی ۱۶۸ کودک معصوم ببندی؟
🔹
اون جایزه ای که گرفتی چند؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/691217" target="_blank">📅 17:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691216">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اوضاع نابسامان درآمد پرستاران، ۲۴ ساعت مراقبت از بیمار فقط ۶۰۰ هزار تومان!
محمد شریفی مقدم، دبیرکل خانه پرستار در
#گفتگو
با خبرفوری:
🔹
تعرفه خدمات پرستاری برای ۲۴ ساعت مراقبت از یک بیمار حدود ۶۰۰ هزار تومان محاسبه می‌شود و پس از کسر کسورات حدود ۵۰۰ هزار تومان باقی می‌ماند.
🔹
این مبلغ برای مجموعه خدماتی که طی ۲۴ ساعت توسط پرستار، کمک‌پرستار، مدیریت پرستاری و سوپروایزر به بیمار ارائه می‌شود، است.
🔹
در مقابل ویزیت یک پزشک حدود ۵۰۰ هزار تومان محاسبه می‌شود و این اختلاف یکی از عوامل نارضایتی و کاهش انگیزه پرستاران است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/691216" target="_blank">📅 17:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691215">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
رئیس‌جمهور لهستان: پوتین در حال برنامه‌ریزی برای حمله به کشورهای حامی اوکراین است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/691215" target="_blank">📅 17:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691214">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c66205bdc1.mp4?token=ShDwsbOitQ9s6f8oaKpph83wRGzhEW8euOLGe9zyWbeBwrIO8Gx6Briqu8Q0mg1pavXOp9HZc88GvNtZUblI_zEgOBMy-XWGggYlyIHgq9jhISqpSv5ITHtIeEXYi-_wv4-ZKstVX1SnFtY1GUnv2pxgyJrxGJ5v_ZKbpUj4cw3tRz0RBa2cSTPB3PzAwR-U7R7lduqHIcCLZ5EaiSThkKNlN1ZxwG23KxzWXxlPYtkPJOLFKrvChjidMX6OqxCMllhDP7vDarNH4O0snw2IakO1HX2kboDmOaFsGjRIXCtV2y7asswU40rUQMri6xhyaHLuguXT37TNgotFU4ojgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c66205bdc1.mp4?token=ShDwsbOitQ9s6f8oaKpph83wRGzhEW8euOLGe9zyWbeBwrIO8Gx6Briqu8Q0mg1pavXOp9HZc88GvNtZUblI_zEgOBMy-XWGggYlyIHgq9jhISqpSv5ITHtIeEXYi-_wv4-ZKstVX1SnFtY1GUnv2pxgyJrxGJ5v_ZKbpUj4cw3tRz0RBa2cSTPB3PzAwR-U7R7lduqHIcCLZ5EaiSThkKNlN1ZxwG23KxzWXxlPYtkPJOLFKrvChjidMX6OqxCMllhDP7vDarNH4O0snw2IakO1HX2kboDmOaFsGjRIXCtV2y7asswU40rUQMri6xhyaHLuguXT37TNgotFU4ojgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال‌شده از تهیه و جمع‌آوری تخمه آفتابگردان با لاستیک ماشین در ضعیف‌ترین وضعیت بهداشتی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/691214" target="_blank">📅 17:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691213">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTahagasht(Tahagasht Social)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs835RAb9d4R8TUcsja6G9pJUvdEeUa4fFs1SsIrBDFJKYO4jmDvlbABJ6tLIALfo5VZkxGqPujfJyAb8cjsAAoOsoVG1VadDFz9dJdhTOuIvbnMTRemQ4lnO2aArhKWHF7R8irkeB2a3i1eG6VYQqS0UezUo_bkbw6tT9XVTpCLTxi4WEJoqJqtFTpWFV91XSSpJXJGUu4s99LkUpEFCgP492i-dLEuAnvhiJ2FnqIG-GIHMeoXnvRzpcVXIZuhfvr2Xkx5BjhwjXLKEiuUBnsfK1O3SvBy8IP0bTXcr-yJedkhM0bbaDAzYVWc-y0Mlk4x2smZBr_EHIztr3Se1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
تورهای تکراری ممنوع!
✈️
سفرت رو خلق کن!
سفر رویایی‌ت از همین‌جا شروع می‌شه!
✨
🔹
بهترین نرخ پرواز و هتل
🔹
تنوع گسترده هتل‌ها برای هر سبک سفر
🔹
انتخاب مقصد، تاریخ و مدت اقامت
🔹
طراحی سفر متناسب با سلیقه و بودجه شما
🌍
همین حالا سفر دلخواهت رو بساز و رزرو کن!
📲
تلگرام:
https://t.me/+2wRXAjoDIG44M2I0
🌐
www.tahagasht.com</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/691213" target="_blank">📅 17:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691212">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای مضحک سنتکام: ایران به‌لطف محاصره شدید ما حتی یک بشکه نفت صادر نکرده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/691212" target="_blank">📅 17:05 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
