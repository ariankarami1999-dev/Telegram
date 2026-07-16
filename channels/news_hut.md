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
<img src="https://cdn4.telesco.pe/file/i871apWkffRI_T15boix7iBelk-uQC8wQk7xfuk8hbA06nZiHpYC5eBI391lrpgdQtRMcsfmSdjrLHUu3DPzlPMxdgEkOlCH8wOSpBXoORbcCNEEzQkuEYSef0fQp-rUeazATDWCCnEkEUYDbX_mnurg2AqhOd8vnVbSyuMkAl51LRxZPbKLE_ECK3aLzpIN4kROSNeKqFy_bV-fwxph1yvMwdnS0TAMAnhpsV22V-X9qEiTcURTpAa9Th3cBc9mWYLAojALwsIReDNDEdaKfq41WHc74x4jN--zgqU4aU7vCFobrRDUogv361juSaq40T4JcskFZ_wV12ObN0yGuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 168K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 02:56:07</div>
<hr>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g53QVvz594KOjZjlDBgVrF5SvZDZpPCG-7XKGcwFq-UF14Y8UZG-Ly6sXguZF_QWGxha8_E4UonkIeyYpkmH26WnNAIcuVfH2E-uGGwTLgqgNl89510MF2bay9tavUbRgUNvV75s05HYuCmJ0OkVwxZipzoyRZ-69ZVfuKhLqcqj-DTc63TE-WhVCJUfvklxWngppK0DLMyh2noHezxhNmjD_RjThaVjrLBB8TvbbGnH3GQs7kcWuUKcr8oP8Xj-KeHFLpuFM673VQLhBJy1Ffbh2EgkfuZXY7Ak5BpaFw2mxJ1gfBhDrzHNkJxex2d9XMFne78JDxAZkdo0N6QhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68320">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=Rp1DA2SUkQUihrkFHDbVqwmO_rtP0PbEuKKKRZYVs0HJIWWrCkNxIyN8Z_fdYoPHZb_OD4zL7Kk75xT8BQc12UqrUiH4Ny7lIBB5c7TQpQmLcu_qnI_Yul9BRIkBpvibhR7rU8r_F-qr2Q4eTKrcipXVa4Pfnj8jwcu4NUGJyPjzkrz9ByxhiDZlqyo4mQksgYVOjOGo45MQkvVr18874ncXpfI2D9qrVGv8n2PeiH86Ys3KIpVsoV4IntVwPSZcKwjwUthu8UrT3jzIJdRR71zGJm5gdxeMt0yPszJmVBTwTq0LD1eKkDV0ZVc3doYZSSGqlQK2cPP5H6xQ6fKU3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=Rp1DA2SUkQUihrkFHDbVqwmO_rtP0PbEuKKKRZYVs0HJIWWrCkNxIyN8Z_fdYoPHZb_OD4zL7Kk75xT8BQc12UqrUiH4Ny7lIBB5c7TQpQmLcu_qnI_Yul9BRIkBpvibhR7rU8r_F-qr2Q4eTKrcipXVa4Pfnj8jwcu4NUGJyPjzkrz9ByxhiDZlqyo4mQksgYVOjOGo45MQkvVr18874ncXpfI2D9qrVGv8n2PeiH86Ys3KIpVsoV4IntVwPSZcKwjwUthu8UrT3jzIJdRR71zGJm5gdxeMt0yPszJmVBTwTq0LD1eKkDV0ZVc3doYZSSGqlQK2cPP5H6xQ6fKU3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/68320" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68319">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=XW4OYRDWEIcvDgby5FG0PCYp22hGunylWu6C6JmcfnRZxboMG9jcLT4J23qluMbBi3rf9Cpw8eVzENMzMdbiUOpqgabXeJKKoLeKdTG_kBimy_HnxI9D46G4xxLZZbqRXmct5mkxZV_laz4g1OrfUxdXYWedna397Mi-zJwBb5UudaTldDb7A0C4VqV-1OTLRmt-apW8MfUCdpWQ3AKIMiKt4ezdB49iftIPyzXerxFDrjbXLR7ConQV432rUb9E0GgfW1Vv-km-bXpZvvZ_9wt2x3hatPMe4z8eQnkGE353CbUKxPDI4lUKfUIEr7ch-6Cvhw5UeSnwOlowDFpSmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=XW4OYRDWEIcvDgby5FG0PCYp22hGunylWu6C6JmcfnRZxboMG9jcLT4J23qluMbBi3rf9Cpw8eVzENMzMdbiUOpqgabXeJKKoLeKdTG_kBimy_HnxI9D46G4xxLZZbqRXmct5mkxZV_laz4g1OrfUxdXYWedna397Mi-zJwBb5UudaTldDb7A0C4VqV-1OTLRmt-apW8MfUCdpWQ3AKIMiKt4ezdB49iftIPyzXerxFDrjbXLR7ConQV432rUb9E0GgfW1Vv-km-bXpZvvZ_9wt2x3hatPMe4z8eQnkGE353CbUKxPDI4lUKfUIEr7ch-6Cvhw5UeSnwOlowDFpSmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات موشکی و پهبادی سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/68319" target="_blank">📅 01:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68318">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
در حملۀ دقایقی پیش به بوشهر چند فروند موشک آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/68318" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68317">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
فارس:
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی در استان لرستان را مورد حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68317" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68316">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=IwVrbsOYV7AidQTZ_ovWmsou52Hfj0D2eAcW6f73M-kS6O0hKv879wV_Jcm8zQ9sj-qrs5nkNYb3ZAmYfLzrM0gjVQ39te5YS4Rkcz8D6iHLEsuCZ1CN1f402RtoCqxM4Ny3ShCEYfE7XoK9WgbXGyi2MAqjaKZAl4-85psx66-Ypo2MGCnnreqiGZm801KKWr9WvRV8MEH3OhOoxuawOhpp2glFvSTcbpR0cytt5yzEZHuRYY6Jojn4vU8FZ1MDFDvMBh0XWohSFUFIvJBRqPNqsMEXZHi5DNYWlkfqbzVcwWpNSTTdMYSDV25uZbhJa3Bw9Bw6Ov6Gdg0mpWCCjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=IwVrbsOYV7AidQTZ_ovWmsou52Hfj0D2eAcW6f73M-kS6O0hKv879wV_Jcm8zQ9sj-qrs5nkNYb3ZAmYfLzrM0gjVQ39te5YS4Rkcz8D6iHLEsuCZ1CN1f402RtoCqxM4Ny3ShCEYfE7XoK9WgbXGyi2MAqjaKZAl4-85psx66-Ypo2MGCnnreqiGZm801KKWr9WvRV8MEH3OhOoxuawOhpp2glFvSTcbpR0cytt5yzEZHuRYY6Jojn4vU8FZ1MDFDvMBh0XWohSFUFIvJBRqPNqsMEXZHi5DNYWlkfqbzVcwWpNSTTdMYSDV25uZbhJa3Bw9Bw6Ov6Gdg0mpWCCjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68316" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68315">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/68315" target="_blank">📅 01:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68314">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68314" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68313">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=OePmuX4dWSXmS7BT8CaxiMy7QK5ILANFuk3ZhDu0VKFtH349m859jothFu7G7aRJrJ9m_VOJmraqhduMnhoFCPxdWIhtC0D_buFw5Da5_1WhfRObw_EfqGKVZWkBZUpk2XrgI3BwaHva49ElSjpjSon2c32YAJPeBbTl7Sa8BcdGCjgJS6G-gkkCYyntSaJ3Kx2Rykqr-7SXAFAz3Pk8g9oQnwitZHH0tTzsZep4vNZbvrSu2H0hY_jjQzP8Rafm_w1jp0-gs08aBg2ruYO7Rqlir2BcuutAz7jT58VP3miYfXUOHmV6ykY0y3siZJvdEGnAXe6w9lmYD7qs3QNGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=OePmuX4dWSXmS7BT8CaxiMy7QK5ILANFuk3ZhDu0VKFtH349m859jothFu7G7aRJrJ9m_VOJmraqhduMnhoFCPxdWIhtC0D_buFw5Da5_1WhfRObw_EfqGKVZWkBZUpk2XrgI3BwaHva49ElSjpjSon2c32YAJPeBbTl7Sa8BcdGCjgJS6G-gkkCYyntSaJ3Kx2Rykqr-7SXAFAz3Pk8g9oQnwitZHH0tTzsZep4vNZbvrSu2H0hY_jjQzP8Rafm_w1jp0-gs08aBg2ruYO7Rqlir2BcuutAz7jT58VP3miYfXUOHmV6ykY0y3siZJvdEGnAXe6w9lmYD7qs3QNGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو وایرال شده از حمله وحشتناک آمریکا به بوشهر
شیشه های ماشین فیلمبردار درجا ترکید!
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68313" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68312">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d811948267.mp4?token=psNCTgVd6LmQ2mVrbbsyEe8dKcKutWQrSJlz3S15hEZsotlJrBJoyb8DINqELnImz1GK-r4a77dz-oRseAxBliKwJbNs9BpCzx7SoNAwwFFr02GFd_n_L94a-gK0TxSmOJfc-N7abpOW4td_qp4iZY1D4GFbmVjEb_e4UpB82MkVRVdEKe7qxmLJhvxTeAyXxaYUZ3Se59_MKmgnY9xTMQcUIi58VGdhMHN7I8KYp4nSVINp39THDgAS7JNV2HzKOqW5NAuZmb9jfjrF6_x5xJJ6GGWemAhxFbRe0SiOLT7BxD6QM9TtqyZAoWPqTrBzr2RkxelRsLC8uPCgo-qGznq1IPOsVjEKtM_DZa7xP9J_EeFESAdVVi4dmKWO70LiucszqzqVR73GOaN7fKnHZh2kSdA7IaeYFl3Cb9E7OygrhNxonCZ31M3aKpnzAbCImNipL0V4U5pGb4OsFl5nd4sWVPHxO0szdTfcO-3MMJBYGgh1mcCIgqSGCITCa4emfZ8mqsQlw3wx8o_Dhw76KXVkH6qFox8OJYgFxkbvXUZCcPDZmJNi0mXzKulsQzQsH-lEy6pvAHEpy53XzH61fUEIvPilCjbCnfIfKEM477TCoh_ewCf8BPkV0LT4A8sxI0wkYJSWH3JfZ11FdRX0EJJ0hTTaoYlRq6ozmfZRrJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d811948267.mp4?token=psNCTgVd6LmQ2mVrbbsyEe8dKcKutWQrSJlz3S15hEZsotlJrBJoyb8DINqELnImz1GK-r4a77dz-oRseAxBliKwJbNs9BpCzx7SoNAwwFFr02GFd_n_L94a-gK0TxSmOJfc-N7abpOW4td_qp4iZY1D4GFbmVjEb_e4UpB82MkVRVdEKe7qxmLJhvxTeAyXxaYUZ3Se59_MKmgnY9xTMQcUIi58VGdhMHN7I8KYp4nSVINp39THDgAS7JNV2HzKOqW5NAuZmb9jfjrF6_x5xJJ6GGWemAhxFbRe0SiOLT7BxD6QM9TtqyZAoWPqTrBzr2RkxelRsLC8uPCgo-qGznq1IPOsVjEKtM_DZa7xP9J_EeFESAdVVi4dmKWO70LiucszqzqVR73GOaN7fKnHZh2kSdA7IaeYFl3Cb9E7OygrhNxonCZ31M3aKpnzAbCImNipL0V4U5pGb4OsFl5nd4sWVPHxO0szdTfcO-3MMJBYGgh1mcCIgqSGCITCa4emfZ8mqsQlw3wx8o_Dhw76KXVkH6qFox8OJYgFxkbvXUZCcPDZmJNi0mXzKulsQzQsH-lEy6pvAHEpy53XzH61fUEIvPilCjbCnfIfKEM477TCoh_ewCf8BPkV0LT4A8sxI0wkYJSWH3JfZ11FdRX0EJJ0hTTaoYlRq6ozmfZRrJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده آمریکا، دقایقی پیش تصاویری از عملیاتی که دیروز بر روی یک نفتکش ایرانی انجام شد، منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/68312" target="_blank">📅 01:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68311">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دیشب که داشتم با دوستای جنوبیم حرف می‌زدم، می‌گفتن حملات بیشتر داره به سمت پادگان و و قرارگاه های نیروی زمینی کشیده می‌شه، حتی دیشب مثل اینکه به پایگاه لشکر ۹۲ زرهی هم حملاتی شده...
امشب هم که خودمون با چشم دیدیم ته حمله به پل‌ها آغاز شده...
حالا سوال همه الان اینه که آیا قراره بهمون حمله زمینی شه؟!
اولاً اینکه ما در جایگاه تحلیلگر نیستیم که به این سوال، جواب دقیقی بدیم، ولی شواهد اولیه داره اینو تایید می‌کنه، اما وقتی کمی عمیق به مسئله نگاه می‌کنیم خیلی موضوع فرا تر از چند تا کلمه‌ست و عملا داریم از یه لشکر حداقل ۱۵۰ هزار نفری حرف می‌زنیم، حمله زمینی به خاک ایران، برای آمریکا بشدت پرریسک و پر از تلفات انسانی خواهد بود، ولی اینکه دارند شرایط رو برای تصرف جزایری مثل خارک فراهم می‌کنند
اون هم به قصد فشار بر جمهوری اسلامی،
یک موضوع دیگه و موضوعی محتمله.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68311" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68310">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861fef7828.mp4?token=JGeVRq8SXeDEHI3DbqDseJi0f2ISUy-66rKO4ipPnoaUbBsJgojIInUXfzlqxjoRRd_VSz7l1L-vtUNdXqcBLO84DG5Wj2DGFMgr7LJjRtDjQRbBsMsHzr605k1sF0bEfqCwKoTW_telJbNNpWhqHM5SaSQAQQdYN9eTTzbyUZyzLJXtT1UdqFj5ptMAQBGOUb1F54HomyMR0nIpfkOz8OZF1bA2G41WesnupgOgf-pHuJdlO5eyuYiMqqrEsnEm1JyIzdnZSvavFK86vdwkCW0-4wLwcaSxtMsmUxjesDmRciOAVntrciSk6xZupq25G9WHbn0xYKCsjSiwJ9U-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861fef7828.mp4?token=JGeVRq8SXeDEHI3DbqDseJi0f2ISUy-66rKO4ipPnoaUbBsJgojIInUXfzlqxjoRRd_VSz7l1L-vtUNdXqcBLO84DG5Wj2DGFMgr7LJjRtDjQRbBsMsHzr605k1sF0bEfqCwKoTW_telJbNNpWhqHM5SaSQAQQdYN9eTTzbyUZyzLJXtT1UdqFj5ptMAQBGOUb1F54HomyMR0nIpfkOz8OZF1bA2G41WesnupgOgf-pHuJdlO5eyuYiMqqrEsnEm1JyIzdnZSvavFK86vdwkCW0-4wLwcaSxtMsmUxjesDmRciOAVntrciSk6xZupq25G9WHbn0xYKCsjSiwJ9U-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
تفنگداران دریایی ایالات متحده از «یگان یازدهم اعزامی تفنگداران دریایی» در تاریخ ۱۶ ژوئیه، عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «وِن یائو» (Wen Yao) در دریای عمان اجرا کردند.
تا به امروز، نیروهای آمریکایی مسیر سه کشتی تجاری را که قصد عبور از سد محاصره را داشتند تغییر داده، یک کشتی را که از دستورات پیروی نکرده بود از کار انداخته و برای اطمینان از رعایت کامل محاصره دریایی جاری ایالات متحده علیه ایران، وارد یک کشتی دیگر شده‌اند.
تنگه هرمز و آب‌های پیرامونی آن همچنان آزاد و باز هستند؛ مگر برای کشتی‌هایی که قصد نقض محاصره آهنین آمریکا را دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68310" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68309">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68309" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68308">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR8K_mSzHaHcZCOcphnjNDPoOcsiRdMk97wglXx1Uo9n8c1_aJrM8oiSOSBMD02NY3Y2E3iD1Bp_6uGkhlIrPGFEBVbK6IoLmyh43ejkx2AmfbbFhF6McWDOcqd-k08LAS9WyGyLrDDVcgOJx9kwWCJCn89NavPbj3BBxIf3OXY_Trd_pP3dTyMTIiDCQHPYg_MpCyjmRLT4xtgth1Zsxo1bPNvwlvJYfZSNVPlunoiiIW7WybblMDVjyyu2yLtpTek8n74PkML80D89YmjJZBB7adNCA9xHMdeIriJwD7EjlHpoLzfVft4bAKirlcFdsLAfOHyolvlj1zQYxXfyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/68308" target="_blank">📅 00:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68307">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
دفتر فرماندار هرمزگان اعلام کرد که تا اطلاع بعدی، جاده‌های زیر مسدود خواهند بود:
جاده بندرعباس - خمير - لار به طور کامل مسدود است.
جاده کشار - کاهورستان نیز مسدود است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68307" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68306">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6vcJ7g2RIZVUL1Q4Zht1HwImYHTNuZ0Md37-Zf4cb79FwVhV89qbTUqgqMiuP4OLuNgp4pW3MHBnjEsJMjfI9BjlIJ3k48h-rfS-c1kly0qujIJN-1o4XEckiLBaUXsOub5JFNb3cT0muaZ-uV8LB7xkwkAt_Xpigd2uuBBLO2nag2Vc7EVcI4FFcgEE0aWdD3yombZVBQR0USk7qsduR8E6Y40sX975nahEEy-uCnuOMizMPEQHq3OyuIcpQmZtbeEKislmvSuFRaqHJdiO0l2MVEexeHtcUPCuOcUDJrj3g-CNXRRLLMRaYEyfJgPS9sbnOeR6ys4PJDm7wVvHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رشیدی کوچی :
⏺
«حمله زمینی به ایران از سمت جنوب رو قطعی میدونم و به نظرم تنها دلیل تأخیرش، گرمای شدید هواست.
به نظرم تمرکز حملات آمریکا روی مناطق جنوبی هم در همین راستاست و ایران هم تا الان با هدف قرار دادن عقبه دشمن در کویت و بحرین، اجازه ایجاد مراکز پشتیبانی رو نداده.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68306" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68305">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPK4eZYmGok05cgBzhTORQ-3wb3m-WAVV3lwY4Gkm6vl4Urh_8UQ7Tyrp9thdKxBSZWJT1Zl8qQz4L3desyQvUsGUZS5IiXZP6FeqswL2STc1ZOgMp9t7zh_czBLVkBenTrpHCMoIH5s3WPX4bcznvkfY_XFXRAX1NhfcB8jOws2Fkh2X1e86DiCBu-9wlzjGhtEZkGQXLRKybUgrvgrkiLtPES3UB1shw2isTFecsJVoNtp2Y8GMJlVHaERm6kWckgzFHH6F9_KTTKFTAPIv8GmWt7987lOdphqbhgA1R4MSJKxe4dfrx_MozRQbKm74samDCVU8zc02icmKa2irg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68305" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68304">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgVKeqDaBoWJoEqpQG0iUlo5wqPS93_kW2idfRfwuFbaBIB_0phD9tvKBTtbodvoVOJPKkUL2uDvwKWhb5DpNculi5Lt46364JzU-OQHZEowhpRHhsYIEQyCc3DAHyCLQ6yBX5VCEQyHIUQaNeAU9-CjLdlZfB-JoRAMXdbwvqs78xeBkV9A_zraz-XMpYlmBe7Jrwp3KUJfPSjo_Ps-Ib_0YVzdii8rYJbV4fMeg82i3Xb0FoFhDKrcY_Gj7hIkkM5LAHp75wmA4qvDuruibYITxgl5UGoRINh6OiUHF0gEFoxN9NYh2BWAGgOXKwI1D6-X1rhPFyJaZUSklbOTPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت   @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68304" target="_blank">📅 00:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68303">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68303" target="_blank">📅 00:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68302">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=fJZ44tloNEcBh1TwOnWfqRsU83elKTndUTqR3BqCxCl1gCO2lLXCAja-agrHRLiymumqxPkbNBUHTd7s-ZuyOoOKNhnQMLiopV_gR7eH4d9s5HdFOfEwZUI6uJ1B0iBZ18TZl7-R4-g8JZasxEP6rX0FnFUu-xBNZFHUGWJnw02dWa-DK5wkxhRe6NT9pu6ybEHxZoCtxcdSx3HmwUMlPhUd87cDfdXK_NvzDvfyKo7H7GOCpvra620j6ugkaxFsqCqDtm5uOzH2sqX-9sT3hqrT0k1kchmesCxcj4esTAHUNNfJ0TIIXKninC6KKnp5nHNovKGOuRfCkMaE1oE9pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=fJZ44tloNEcBh1TwOnWfqRsU83elKTndUTqR3BqCxCl1gCO2lLXCAja-agrHRLiymumqxPkbNBUHTd7s-ZuyOoOKNhnQMLiopV_gR7eH4d9s5HdFOfEwZUI6uJ1B0iBZ18TZl7-R4-g8JZasxEP6rX0FnFUu-xBNZFHUGWJnw02dWa-DK5wkxhRe6NT9pu6ybEHxZoCtxcdSx3HmwUMlPhUd87cDfdXK_NvzDvfyKo7H7GOCpvra620j6ugkaxFsqCqDtm5uOzH2sqX-9sT3hqrT0k1kchmesCxcj4esTAHUNNfJ0TIIXKninC6KKnp5nHNovKGOuRfCkMaE1oE9pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو دیگر از پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68302" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68301">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
اونا به شهرستان بندرخمیر و بخش کهورستان حمله کردن و پل ارتباطی بندرعباس به شیراز که معروف به پل بندرعباس - کهورستان - لار هست رو هدف قرار دادن.برق مناطقی از کهورستان هم قطع شده
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68301" target="_blank">📅 23:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68300">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=DzUfq1q5T5pWd6Ld8ob87_6RwXNsGm0jj-VFguU8pUzjBqVvtfCgjeCkwiA3NnnExouhiVjNwYL9xexKzc4piNqSe-3P1bJklkxarJG5cc_-2XANd9TKPwCiE4dHuSQZZikqA9qldwMPJgJA0MepP1K-JyrrUEb6iXLGoBbUshwYj0AN_TPgVGZpRZTwz6mAsvHgA3-eK4S--9iTGQZC7Zk0UQPhNU7bO7b9S-nzVWF4kGJnsxdljPg7E-BSsRkRaugZX6VleRkcP6LTaTOEwpmFmhRiqCFWtzOserVucaiGCv-A35N3xgm0UD489RqZvWCn_nlNqynDiML5JOzytA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=DzUfq1q5T5pWd6Ld8ob87_6RwXNsGm0jj-VFguU8pUzjBqVvtfCgjeCkwiA3NnnExouhiVjNwYL9xexKzc4piNqSe-3P1bJklkxarJG5cc_-2XANd9TKPwCiE4dHuSQZZikqA9qldwMPJgJA0MepP1K-JyrrUEb6iXLGoBbUshwYj0AN_TPgVGZpRZTwz6mAsvHgA3-eK4S--9iTGQZC7Zk0UQPhNU7bO7b9S-nzVWF4kGJnsxdljPg7E-BSsRkRaugZX6VleRkcP6LTaTOEwpmFmhRiqCFWtzOserVucaiGCv-A35N3xgm0UD489RqZvWCn_nlNqynDiML5JOzytA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
در کهورستان بندرعباس یک پل هدف گرفته شده.
موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68300" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68299">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
پل ارتباطی بندرعباس به شیراز و معروف به پل بندرعباس - کهورستان - لار مورد اصابت قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68299" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68298">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=p5veEIsCHG0zNKjylD0VfUgsCu3BdlSFtIh8lCDh8XfLhSvm0yaVJ30MwO9_TYLT5_p1AzpIRj-afys7w_2umo7wEqk2NPcaTh64qlMw5jcaGZ4wQe6y3gcx2DjyuS_A6lWVtoVpb7GZn06FoPSbwKbeID8853jzsIE5ynR3BTHigjQ1iBfduVECYFKcWv_0ZT7A1Hb8SMfjw5gCDaoZNyOUBLdMWgixTtEbs3XP9f9aSDsKZNyGWiLLrMx6wClm6bGl0aTgRqErEiCfJbrtQCWwzc2egxC7AAJKpUZXa8lpDMCeFYiInxNZ0Ifw7dzsdmyn2PZI6ZtSJxy-3mhXYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=p5veEIsCHG0zNKjylD0VfUgsCu3BdlSFtIh8lCDh8XfLhSvm0yaVJ30MwO9_TYLT5_p1AzpIRj-afys7w_2umo7wEqk2NPcaTh64qlMw5jcaGZ4wQe6y3gcx2DjyuS_A6lWVtoVpb7GZn06FoPSbwKbeID8853jzsIE5ynR3BTHigjQ1iBfduVECYFKcWv_0ZT7A1Hb8SMfjw5gCDaoZNyOUBLdMWgixTtEbs3XP9f9aSDsKZNyGWiLLrMx6wClm6bGl0aTgRqErEiCfJbrtQCWwzc2egxC7AAJKpUZXa8lpDMCeFYiInxNZ0Ifw7dzsdmyn2PZI6ZtSJxy-3mhXYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملهٔ آمریکا به یک پل در بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68298" target="_blank">📅 23:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68297">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
طبق گزارشات اولیه، یک پل در بندرعباس هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68297" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68296">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
به گزارش ممبرا ساختمان مخابرات بندرعباس هدف حمله قرار گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68296" target="_blank">📅 23:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68295">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
حمله به ایرانشهر سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68295" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68294">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzi3s8Lj-85q_zS5fgUdDfiFW8R50TZDmtAAtxN-SvhZJJnGw_mDZPTKRfG3IDXLSONOdH7IW4NMisHWmxT0oL8gqmDK1qkWC6aC8N5m60Fna4fK1fOSAbb5yK9k3cbK7ucaqe6an9JpKYYxgbGbpjGeufVyj2qGRk47INAgD5r2gYNq7f7Y9n35C7LM9wRco6uAEwDps7VwNiZCDHYj5OyjZh02YMAMSwb93ieALQixABNqjqeS_0tIaqgS0AKgzdWxy-qFnsFscCm0D_iLSHbgvAiORRPek2TYMVEEBJqj5M2NgSdn-WKGjIrHyUSCRG6cTp3uSkarlQyqbnXOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68294" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68293">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDOpDTruZQ_2vqPrex59wNbfK8aIhos1b-FO9yN43FLWWIxqGfFtkiKQ6Dd0vGIKo7ZhMkQBlahmsHXsHoti2XW5M4mKOYQAR28LjJdSDyr5JWrBC0LssnDlVxKLDlEQm8i2c7VEdPVulsEcq93TdXwHmcL1nkj9FDfK3ARm38JkBqry1tOA-n3VV8rdZZnhK8GLM8XbbGf-7zH-WNfR89J0JFcznaXB_rNsuFjEy340HxEJw4S-S9Ueulwiar9JHomWuJXLPq5j54YxktX9b6v_neYkxFwNT2maMMgLCt0ZGCej4b4qQsTcvsAfBoD5c1gi9t3XQbJCP8BIq9SKrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت دفاع کویت:امروز جمهوری اسلامی چندین تاسیسات حیاتیمون رو هدف قرار داد.
از سپیده دم امروز، نیروهای مسلح 32 پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده‌اند؛
این پهپادها رهگیری و با آنها مقابله شده است
این تجاوز شنیع ایران چندین تأسیسات حیاتی در کشور را هدف قرار داد.
علاوه بر این، رهگیری اهداف متخاصم منجر به سقوط آوار در مناطق مسکونی مختلف شد که خسارات مادی به بار آورد، اما خوشبختانه تلفات انسانی نداشت.
نیروهای مسلح بر تعهد مداوم خود به انجام وظایف و تکالیف خود با کارایی و شایستگی، حفظ آمادگی و آمادگی مداوم برای تقویت امنیت ملی و حفظ ایمنی شهروندان و ساکنان تأکید می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68293" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68292">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
پنج انفجار مهیب در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68292" target="_blank">📅 23:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68291">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به قشم و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68291" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68290">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS-</strong></div>
<div class="tg-text">داداش ما الان تو کوچه ایم تو اهواز بچه کوچیکا ذوق صدا بمب رو دارن</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68290" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68289">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان  @News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68289" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68288">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=QYf16M5HW-87rfy6dV0HcbhMNQWlvN9E6x3A0VEOYuYfEy1tgMSknPPmHdYiHiF8l1YfzdTZkzNM0KiP69rmhzpPUOtA-GHbcO9htL-OgPqhXL1n51pPoJfEpfqyfEfXNfbCS_KAXqOk988MEnhmyIS5SuOoUkmEJBk2OphjedcGnH1iAv2JWovQKeGuZT9XqxLic0llBTR7K4T-egXurh0G6LeFcUKi1WUORwhtzlR753yir5j7N5LcrU4dMRwBp-R2reSzOPWO5vf72F9I42pRDCZ-xXMjLohuE8wG-i5x9dQ4GTuvvK_CB9U8VnKA6XlRUlepFAbl7CF6nWSHOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=QYf16M5HW-87rfy6dV0HcbhMNQWlvN9E6x3A0VEOYuYfEy1tgMSknPPmHdYiHiF8l1YfzdTZkzNM0KiP69rmhzpPUOtA-GHbcO9htL-OgPqhXL1n51pPoJfEpfqyfEfXNfbCS_KAXqOk988MEnhmyIS5SuOoUkmEJBk2OphjedcGnH1iAv2JWovQKeGuZT9XqxLic0llBTR7K4T-egXurh0G6LeFcUKi1WUORwhtzlR753yir5j7N5LcrU4dMRwBp-R2reSzOPWO5vf72F9I42pRDCZ-xXMjLohuE8wG-i5x9dQ4GTuvvK_CB9U8VnKA6XlRUlepFAbl7CF6nWSHOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از کویت به خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68288" target="_blank">📅 22:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68287">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68287" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68286">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68286" target="_blank">📅 22:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68285">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=h2ZsveNLXTNcijXSX1MwNHfAkYjd4RrN1TufUquCjKXBR9QBU8BOCAiFmmuCtQklq5la_odck5fb8EmznbIe_ZDjOqxYpBV4SPEY_IsO8AXixnOWt7YkuKehp1z-1HsN5LPs-Yel6lpIk_Ke3F3tGXtsTcV24uevZi2tjbCFhbi5k_V06HYfDGKw6uqwsLADAiSGSBxAUMoF3O5aVa02CXTvnRtfDlV5NRb8DOhJ6g8FN6iWK4y1Hl5kHNjcuszp5K8V4lu2voXX4Q98ndiV6eiunxr2zFult9NyUnjGia2BEIpB5UeuwdpFeDaDqkcS0lrmOlxrpkVY5KYWXDfTFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=h2ZsveNLXTNcijXSX1MwNHfAkYjd4RrN1TufUquCjKXBR9QBU8BOCAiFmmuCtQklq5la_odck5fb8EmznbIe_ZDjOqxYpBV4SPEY_IsO8AXixnOWt7YkuKehp1z-1HsN5LPs-Yel6lpIk_Ke3F3tGXtsTcV24uevZi2tjbCFhbi5k_V06HYfDGKw6uqwsLADAiSGSBxAUMoF3O5aVa02CXTvnRtfDlV5NRb8DOhJ6g8FN6iWK4y1Hl5kHNjcuszp5K8V4lu2voXX4Q98ndiV6eiunxr2zFult9NyUnjGia2BEIpB5UeuwdpFeDaDqkcS0lrmOlxrpkVY5KYWXDfTFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68285" target="_blank">📅 22:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68284">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68284" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68283">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_Wpu78rfsdtzGGJ_kVT5MfFwRy3EfFQS1saZulNl1bolPEHDHg9A4jy5PK2Ho0_ST2cc5NPYwbaEuUUAp558-YuONysXZpwvEpkMhZJ3E7VgRhz_Z0dwFeGQCeqvap6XTnY_NnBDBhUDwltMASisAVqo6XaLJ6CGhMb-ZwPvowOhVJOE-vmCTs-AcZTXuwAs3LSnOaeDOag1V9O2CRM-v2QhLClUe-CWyPAmA2ZAx2B0XQE_dqeD1vKCPvzHbty4f30X1cJK0KOQRV2US0XyKebhO3bTODoQ9RQYrEFY4Hpc80c-yZ31JbXr7WyGVxuYKv1zT7qnr1yOVagSy1IPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68283" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68282">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=tNMRH0PzmNG7XypId6EH2vYHD92fynQrdEpTfR5Ss9Pi4YcSSLUipCQY4TRyT1spHeKMRJ2VuHREhJeXTNT34eqdco8adEIi7vcAopy7eAAOn5SZshmWgm-eNd1h0bENHmcxgrfoZBxdx7y0fabi1mk0fE_MF3Ay4FLeJAshDP8G17Lmimv8GsyO5K1pqdTtIBl-drdiwL47YkJhbFY_dp1c2Fo0njocRdKG84vvtF6_MnnG34yIu_IA61Zsnwa301vBlkTEDYbemAUgLvcXoqBy1A0WEPLa0Js9criqXiwFuZDrQVZo337mBumSK5TaUZDT-QTbsPeMPSn0xPpl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=tNMRH0PzmNG7XypId6EH2vYHD92fynQrdEpTfR5Ss9Pi4YcSSLUipCQY4TRyT1spHeKMRJ2VuHREhJeXTNT34eqdco8adEIi7vcAopy7eAAOn5SZshmWgm-eNd1h0bENHmcxgrfoZBxdx7y0fabi1mk0fE_MF3Ay4FLeJAshDP8G17Lmimv8GsyO5K1pqdTtIBl-drdiwL47YkJhbFY_dp1c2Fo0njocRdKG84vvtF6_MnnG34yIu_IA61Zsnwa301vBlkTEDYbemAUgLvcXoqBy1A0WEPLa0Js9criqXiwFuZDrQVZo337mBumSK5TaUZDT-QTbsPeMPSn0xPpl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68282" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68281">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKfj-zB9XykRkwZskQscvd8JO_lh1LG1uJT8GE222G7hQ2s6JYNmh-tweg09ulFlKPB02TzxwrkEkFh-2lke_vu0y2vQNU9fb3ip_U_EFT3IgJhfDi5sq0zRbLvrFBcbPSzwBUKSgkgZELwiCO5HoUR-QOV97NZ8oRdjUCh2W_5M254szsr4lBZT2bhL8WI0WmBURh5ij2VUctu9Ny2IX1HwkI3y2KpGzOsDz104lfX4MaBNN_kc-lCYNHwWN_c9OZsjncX3sEit89FbqiahaXfck-x347U4YJsg1ftLoqoPWluNoRgtR1o9iyPVSGtfEYEz35uvii5z_SUVR7KfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۲ بعدازظهر به وقت شرقی، نیروهای آمریکایی برای پنجمین شب پیاپی موج جدیدی از حملات را علیه ایران آغاز کردند تا توانمندی‌های نظامی ایران را بیش از پیش تضعیف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68281" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68280">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68280" target="_blank">📅 22:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68279">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68279" target="_blank">📅 22:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68278">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
پنج انفجار در بندرعباس گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68278" target="_blank">📅 21:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68277">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68277" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68276">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=uxhzjVUfBL64tWV8qjJpI9vmdbcWOHJKxVM44cOfMNLPA7GNV5_QL3uJN5AGLFYOrT1oJu9J3C1jNwTQ1pbNUuUBKjTnt0itquS0bWgkGKUdsNs219ShrcvXV5yX76-1BhIBWSUcB7WVsjs4n8zR4WSuUPgHj9xQJ_-SzrabsrAYa-WsaIQscYOgSI1rEPI66PHp2HqC4yS3-OZGGlqh3ZbRqxywL42yY2Cs-dV7LOF40hS91ieCnexBLdWatbJXVEBfy2cxbzVvpSl9gAl0hfdxtp78QgvT4jgPwS9APi2e6ba-zBK7Jkqrl9uc9KuaJjPOGDNlDu_vsURMFoOtWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=uxhzjVUfBL64tWV8qjJpI9vmdbcWOHJKxVM44cOfMNLPA7GNV5_QL3uJN5AGLFYOrT1oJu9J3C1jNwTQ1pbNUuUBKjTnt0itquS0bWgkGKUdsNs219ShrcvXV5yX76-1BhIBWSUcB7WVsjs4n8zR4WSuUPgHj9xQJ_-SzrabsrAYa-WsaIQscYOgSI1rEPI66PHp2HqC4yS3-OZGGlqh3ZbRqxywL42yY2Cs-dV7LOF40hS91ieCnexBLdWatbJXVEBfy2cxbzVvpSl9gAl0hfdxtp78QgvT4jgPwS9APi2e6ba-zBK7Jkqrl9uc9KuaJjPOGDNlDu_vsURMFoOtWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت سخنگوی سفید کاخ سفید:
«ایران همچنان به شدت با ایالات متحده آمریکا در حال گفتگو است و ابراز می‌کند که خواهان توافق با ماست، زیرا آنها از سوی نیروی نظامی ایالات متحده ضربات ویرانگری را متحمل می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68276" target="_blank">📅 21:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68275">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=eOVj37TVQMWCcEeGJYLAvI_fuZcH0Q41Du7Kx0eeVeGUI8JNfmN3zB94i-Hez0fu0wT9K9ROkJLqMjdpUbFCOKOxfTwTTE22WD988Q2Pn2xquguuHePpCIMCpapmgacrY1SpnRtQ9G5fvOA-5XhkjVrbUyZtinaUXxPtKiY83tR-2q4-eHLYvJqCHgGGvj44tpMmds-YYN75HUtpaXpOjulP53nzgJ2vIT3yNWEU_lSAUi71eKhL39-r2v-KhsbqLrHbqGxlClUsf-6l0sQqnlcEjMLl3vrHsbQDUIJezogF6eU89hIkm8wZ83UW2rY2KBt2OPduPZyooYjGPe9jnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=eOVj37TVQMWCcEeGJYLAvI_fuZcH0Q41Du7Kx0eeVeGUI8JNfmN3zB94i-Hez0fu0wT9K9ROkJLqMjdpUbFCOKOxfTwTTE22WD988Q2Pn2xquguuHePpCIMCpapmgacrY1SpnRtQ9G5fvOA-5XhkjVrbUyZtinaUXxPtKiY83tR-2q4-eHLYvJqCHgGGvj44tpMmds-YYN75HUtpaXpOjulP53nzgJ2vIT3yNWEU_lSAUi71eKhL39-r2v-KhsbqLrHbqGxlClUsf-6l0sQqnlcEjMLl3vrHsbQDUIJezogF6eU89hIkm8wZ83UW2rY2KBt2OPduPZyooYjGPe9jnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز ظهر تو خیابون ولیعصر تهران،یه اتوبوس تندرو بی‌آر‌تی بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت میکنه!
این اتوبوس میوفته تو مسیر سرپایینی و با ۶ موتور سیکلت و ۲ ماشین سواری برخورد میکنه که نهایتا ۶ نفر مصدوم میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68275" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68274">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8F0fkB9MLFRL3vXMd7nMnvaSs96bpEEtutX90L3vKV4dXqco24rQX-CiPVyi7IKhAwFmAVgwyZitreMdxaRIw_mnfL7LeP7ab_Hw8QIXp74jH7QkBCpSVdIJsO_F6fDLJFmbmJ-kkPCvn94YVSmjOojkw2N4dJNb311IvHvuxh-cmBsnGjJE1HwYIKZI6hI-ZsNepbGNhFHYGniTR8b1GNZiP7JAwloOsKaep3TGjBByjuOq6Rh-yVVtWFVDhspgOYU6aEd4E4XckiML1g6Y_1BcpWIeysCbxsRQ-88NgFdHuEdHcBb90ufQlv6D-k6jXazO--CsvbnaKIPtr5RQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68274" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68273">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZsiQfraa-Q_VRQfHMgYo9SSQ_mZYuaw4k-_R_5Mf3QdT6kzA0bJ11KtWq9OyLHmasy9sikcW9Fo2oCyd5hS67nVrP-6djEM-iNlrMuwcNZvP4gwGr8t8jNZG6_jt4X14L6vCalsja_XAuazHfhQJosMfKuec6k90_ZAZqFB1ABnRGej_RP9IGlZ52YVb5D0Piy02XQgiSp0oDn2R_kG51GenVEKLVQjU5FSR_7g8fp7-NNSfyr6OL6dm2HPorKOXOcrp6XGqur49oDLM9TIpPsQTrhovn52R1AFKRdGUpra86GTAFpy0ANWt6kYqC7_vbf5rV5cYullOWHOJGHdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏شاهزاده رضا پهلوی:
در حالی که جنگ‌افروزان جمهوری اسلامی در تهران و پناهگاه‌های امن خود پنهان شده‌اند، سربازان وظیفه و نیروهای جوان را در پادگان‌هایی بی‌دفاع رها کرده‌اند، بی‌آنکه حتی توان حفاظت از این نیروها را داشته باشند. این رژیم بار دیگر نشان داده است که میان جان فرزندان ایران و بقای خود، همواره بقای خود را انتخاب می‌کند.
جمهوری اسلامی این جنگ را بر ملت ایران تحمیل کرده است و مسئولیت جان همه قربانیان آن، از جمله‌ سربازان در پادگان بمپور، بر عهده همین حکومت است. آرزوی همه ما، صلح، امنیت و آرامش برای تمامی ایرانیان است، اما تا زمانی که این رژیم بر سر کار باشد، نه امنیتی پایدار ممکن است و نه صلحی واقعی.
این رژیم تبهکار بیش از آنکه دل‌نگران امنیت مردم ایران باشد، نگران حفظ حزب‌الله لبنان و دیگر نیروهای نیابتی خود در منطقه است. برای این رژیم، بقای بازوهای تروریستی‌اش از امنیت و جان مردم اهواز، زاهدان، بندرعباس، بوشهر، چابهار و سراسر ایران مهم‌تر است.
خطاب من به سربازان، افسران و همه نیروهای میهن‌دوست است. جان خود را برای بقای جمهوری اسلامی به خطر نیندازید. سوگند شما به ایران است، نه به رژیمی که در لحظه خطر، سرکردگانش می‌گریزند و شما را بی‌پناه رها می‌کنند.
من با خانواده‌های داغدار سربازان وظیفه که در حملات اخیر به مراکز نظامی جمهوری اسلامی جان باختند، عمیقأ هم‌دردی می‌‌کنم، و از خانواده‌های همه سربازان وظیفه می‌خواهم تا آنجا که در توان دارند، اجازه ندهند فرزندانشان در این شرایط خطرناک به خدمت سربازی اعزام شوند. هیچ پدر و مادری نباید فرزند خود را به پادگان‌هایی بفرستد که امروز به جای محل خدمت، به میدان مرگ تبدیل شده‌اند.
این جوانان، فرزندان این سرزمین هستند، نه سپر انسانی جمهوری اسلامی. آنها نباید بهای بقای حکومتی درمانده را با جان خود بپردازند.
هم‌چنین از مردم شریف ایرانشهر و زاهدان که برای اهدای خون و یاری رساندن به سربازان مجروح پادگان بمپور شتافتند، صمیمانه سپاسگزارم. این همبستگی ملی یادآور این حقیقت است که مردم ایران، حتی در سخت‌ترین روزها، فرزندان خود را تنها نمی‌گذارند.
ایران به فرزندانش زنده نیاز دارد، برای ساختن آینده‌ای آزاد، آباد و سربلند
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68273" target="_blank">📅 20:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68272">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
فارس:
حوالی ساعت های ۱۹ و ۱۹:۲۰ نقاطی در  بندر عباس مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68272" target="_blank">📅 20:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68270">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=PyRtZr-_zuASV4OOzP7oBHATIW7YNH5ZrX4Lw00F63LjBUj4G6RwkCYR4tfWW_vjtNoQXXRA896ZYPf4ueJ3YUFCP-Yf-uP90oc2Olkl7bfYOLRvWnpZtW3VGEjPonJHcyY64r78PcOVA_qriiI-oWXIFuuMzBsUvcCHHG5vYBmpy8JAJT7NEpWRf-lWK78SrHvDyI39f-16gbndBHpJCgWy9IMzo-MD5Bh8oKDknleO7wgVNXUnROWjnCco7AH6awY4ut1UggFhqxvAHskl-Wh9oL_6jjYtmoQdOJAS1HvKMyeDwoNbUyw4qHNppOZWgrREI_ryoxzaU9RiKb-XMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=PyRtZr-_zuASV4OOzP7oBHATIW7YNH5ZrX4Lw00F63LjBUj4G6RwkCYR4tfWW_vjtNoQXXRA896ZYPf4ueJ3YUFCP-Yf-uP90oc2Olkl7bfYOLRvWnpZtW3VGEjPonJHcyY64r78PcOVA_qriiI-oWXIFuuMzBsUvcCHHG5vYBmpy8JAJT7NEpWRf-lWK78SrHvDyI39f-16gbndBHpJCgWy9IMzo-MD5Bh8oKDknleO7wgVNXUnROWjnCco7AH6awY4ut1UggFhqxvAHskl-Wh9oL_6jjYtmoQdOJAS1HvKMyeDwoNbUyw4qHNppOZWgrREI_ryoxzaU9RiKb-XMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در بهبهان استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68270" target="_blank">📅 19:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68269">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=XGBPzDGvgAvMXbK5Bi4ZBrxh8dNGC3zh0j2YJL2Doq0TIf2494hIWlSTeapGK4tmg7yoQVt5tOQ5-uxfLkwztl6i_R_A3g07Lr4GrZjmkrFdJKBTDLEcGUxg6Kj3JDEs_5wi7Qo6yaOrwQElu5_so26BdIWU-w4nFnuEXHL4w7iQvAiX4MylCLdcthQcoO0afr2tObqN45JTSPJhofxCxwjigcHb70aV58fTlvcynd7HbsqiKWMsNrPXIOdxu-0MSUVwDVtjtyjt-a_sgMGij3tRWppuqNKHD0WGRyDdbQE5jol6Dsp0sifOOX2k5-zXZsuZTukbB4TkzDqNBsPA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=XGBPzDGvgAvMXbK5Bi4ZBrxh8dNGC3zh0j2YJL2Doq0TIf2494hIWlSTeapGK4tmg7yoQVt5tOQ5-uxfLkwztl6i_R_A3g07Lr4GrZjmkrFdJKBTDLEcGUxg6Kj3JDEs_5wi7Qo6yaOrwQElu5_so26BdIWU-w4nFnuEXHL4w7iQvAiX4MylCLdcthQcoO0afr2tObqN45JTSPJhofxCxwjigcHb70aV58fTlvcynd7HbsqiKWMsNrPXIOdxu-0MSUVwDVtjtyjt-a_sgMGij3tRWppuqNKHD0WGRyDdbQE5jol6Dsp0sifOOX2k5-zXZsuZTukbB4TkzDqNBsPA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای عالی امنیت‌ ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم، نمیتونم ذهن خونی کنم
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68269" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68268">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4SaEyKJejI1GnkyIQhKNZRmCs0Ca0LTerIPoOhAhxVWVyVfnumJXDprO2vkjsj0Ai5RDipuVLDzxIUu4Fb7Pn8MjkRRhQOBfZJZ8wo7zfFVzZein2eeJIHOJpULAz0MFuP_kgZJ3bXJcHSvn4FyADsa8jdSFGIze_kDboLKpObojNWMNzpgXRGsqYXkigsKDyYRkIfugJM_YPcalvYQOopwuQeP9k1YaBuTgBBuFuUsTrr4Bi_khvuVKyVMVEaGCqHCSLrCc_aw8NpP5-svcCPeHuWqzGzlafSs94USzFjS48oQ_BX8KMrF9VQemew3x4nYnA64ALkFZWs7fkPkSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68268" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68267">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Prwi-zfgwY6nw7hKOFuWm97YqZ20uBuFvWJLbTsioCzirI3HIqGBtqEvWhY8ortcRvCg-QspNRGZ4q3Cpo09WX5vYpuOPPTK-GYD9nv2SoVWZ0T4TmJgKB_Rc_YMYkgqe-K8xzUYwukHNao_rNeD5r1zWeuNOfIAoGxj-JUqVvpe58scPo_ghaHjivbO1ljOK9KfYCsVQrI8YMZWTzvjYgulr3wHpqEe-7KGPJitZF9m46KKqWjsdwfVIMcALEar6DBS1L3xEdkNq0Q_8FPUTwcojXnd4qOWO0NXJhjj4HQ4yaHLJmJv6z_3Qk4pZuwCZjgneInhGCI52hxEqoGlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68267" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68266">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06389032d8.mp4?token=tZCNlel5jKzQ2AdbtCW3WgGQAhDymIBVIAgF8iH2jahZfrNFZFTD0aW8sS1JaNO5wi3YGsKcixW_7Qx8PpG3Y-KzKOnMISDKePluiFCX7YsgXv1WWmVDAjyBDDCTMwHqZmsQI2lyZIiiOw0htG_wRSoW1FdHsf4sTawi7NMMx1vV54n6crSCOl0DUcawMvhHtASUisGcFaFBTPGLMYs-z6aH6gjaXMXheI2tRX7HikvXVQC1Ghm_3ftOIjylo1umtSAA4GvaUD8bWtpt5pNRndwgevoWFLFrng_eTb8sidgTsyhoeubNFo7G_3eXSgCc2mcgLOoN13pVPJNw_epcNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06389032d8.mp4?token=tZCNlel5jKzQ2AdbtCW3WgGQAhDymIBVIAgF8iH2jahZfrNFZFTD0aW8sS1JaNO5wi3YGsKcixW_7Qx8PpG3Y-KzKOnMISDKePluiFCX7YsgXv1WWmVDAjyBDDCTMwHqZmsQI2lyZIiiOw0htG_wRSoW1FdHsf4sTawi7NMMx1vV54n6crSCOl0DUcawMvhHtASUisGcFaFBTPGLMYs-z6aH6gjaXMXheI2tRX7HikvXVQC1Ghm_3ftOIjylo1umtSAA4GvaUD8bWtpt5pNRndwgevoWFLFrng_eTb8sidgTsyhoeubNFo7G_3eXSgCc2mcgLOoN13pVPJNw_epcNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، درباره ایران:
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، این تصمیم با خودشان است.
اما ما قرار نیست ۱۵۰ هزار نیروی زمینی برای تغییر رژیم اعزام کنیم، مگر اینکه خودِ مردمِ حاضر در میدان بخواهند به چنین نتیجه‌ای برسند.
البته ما در هر صورت قصد اعزام نیرو نداریم، اما پیشنهادِ اعزام نیرو عملاً به این معناست که ارتش آمریکا باید این کار را برای مردم ایران انجام دهد.
ما دیگر دنبال چنین کارهایی نیستیم؛ واقعاً نیستیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68266" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68265">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwK1O-t8oZaj6EIk3Pn6Kx_Z6TDtRKS_shEO4PeAkChk6vaKOLaz4xEq44D_tEWEhl_iA-YL_2iT5bIMZrmmjMEoqvpHECXFmOJgETnYGMb3eXtmle1-UbtdeC7hpgN5YhJKXYdLwtML9qP1ciW5UEmk0QFRCC-kEgAM7sUk4KFrGINqYj1aXS8CR6zkqxkAgrTDoxtpvazhY25kVyhK6JGfvJdBB2o0OpYQ7u8UqtA6s5H5y36zsS9IlVGVBbG8YvdeW9J5CumjQi1UtNDKeqgoCD0SAuGLNJPp3JO_nRHfUeA-aM2D0UYM-M-STtDTSdPC2jj_w1yCHFNK0VRh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
لاشه پهپاد انتحاری آمریکایی FLM-136 LUCAS در نزدیکی بندرعباس
پهپاد LUCAS در واقع همتای آمریکایی پهپاد ایرانی «شاهد-۱۳۶» و یک پهپاد تهاجمی یک‌طرفه (انتحاری) و کم‌هزینه است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68265" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68263">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=Pf99yjhevzXKvXjK1gRTi2vB2B30kI7xspe8LzrxixZ0up5mOLTccO65NeedlGbvuj3Ss4oU4wrvN4vbvhvXCqzTeGl5KGxpHcfD5KsyvBMptow9BGP4UqdUIpn9BQCPZG0NDn25XzJxwwriDqNp-Z0T5Ciu_mDYdBDcx9Vs-oT6DIHXT7UATGXAX_BysOwTIn7TAaqNK0IbMJimOYjx96GmSHE-WxVQM5LXNeTN6uAOfXUKYZcI0lbYLmYTsrbVAEZoLNN8SI2FvFmga_q8a7Ms-yAzLSgJHdFSt5ktOBzL0rb_Ovq1P0W1b0ibG7NBuCAUKuq-9aQrQ090gKn99w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=Pf99yjhevzXKvXjK1gRTi2vB2B30kI7xspe8LzrxixZ0up5mOLTccO65NeedlGbvuj3Ss4oU4wrvN4vbvhvXCqzTeGl5KGxpHcfD5KsyvBMptow9BGP4UqdUIpn9BQCPZG0NDn25XzJxwwriDqNp-Z0T5Ciu_mDYdBDcx9Vs-oT6DIHXT7UATGXAX_BysOwTIn7TAaqNK0IbMJimOYjx96GmSHE-WxVQM5LXNeTN6uAOfXUKYZcI0lbYLmYTsrbVAEZoLNN8SI2FvFmga_q8a7Ms-yAzLSgJHdFSt5ktOBzL0rb_Ovq1P0W1b0ibG7NBuCAUKuq-9aQrQ090gKn99w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عموپورنگ هم اینطوری بصورت دردناک برای مادرش گریه کرد:
من دیگه مامان ندارم...
دیگه در باز کنم کی بگه چی اوردی برام؟
💔
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68263" target="_blank">📅 17:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68262">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=uN7Ygx_z7gph5Mvm9zNKcar3LTXTOeML06uakYetT_4XWCSPY18U3-ZA4tvwrcCmW6BuvFzfpzzd4NCm_AlZtYSZTSGvdnALxKsvhfyCxFCDoS_IKKFBwfQd62WorsUxh-fGi6iYPmdx5K4HmM7X3Scg4mrHORlCGqir4Vhcy4_V8PB-8439V8jjjXrixXWHTk3mCu4VhcMZwKtXecf3TPcEaXnHwWrpqwJ8GY9mXV_lhT2K8E3Sih3RadX8ivmmZE8Cn-mOmA_8mpzCW1pDw4QQKR6HzPjNzrE_Bhr7FFWVnbCYH2uq8kz0kiJpzJRoLvlIutkdrbxyH6587kG3YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=uN7Ygx_z7gph5Mvm9zNKcar3LTXTOeML06uakYetT_4XWCSPY18U3-ZA4tvwrcCmW6BuvFzfpzzd4NCm_AlZtYSZTSGvdnALxKsvhfyCxFCDoS_IKKFBwfQd62WorsUxh-fGi6iYPmdx5K4HmM7X3Scg4mrHORlCGqir4Vhcy4_V8PB-8439V8jjjXrixXWHTk3mCu4VhcMZwKtXecf3TPcEaXnHwWrpqwJ8GY9mXV_lhT2K8E3Sih3RadX8ivmmZE8Cn-mOmA_8mpzCW1pDw4QQKR6HzPjNzrE_Bhr7FFWVnbCYH2uq8kz0kiJpzJRoLvlIutkdrbxyH6587kG3YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام:
هواپیماهای جنگنده F-35A متعلق به نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط هواپیمای تانکر KC-135 هستند، در حالی که در حال انجام گشت‌های هوایی بر فراز خاورمیانه می‌باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68262" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68261">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahq509R6cejKpo1XI1IxS88WOjefyVY_pgN0lhmzV9SgpP72tCpsN0XHrDnyIB0c8yAOjqxNHuyW_kxJnZKbeOoRktLY4zc37FaHQVK4UG38NOH7Hcbc3jqrxg1K6MHz2HVRmeaScmAxzxxEqrwdQobzwqjjSW2yzElPRGLd4KvEgL7XRSWGz3i4VXG8_MG4gjZzD0-17DJ5nocjZJusxB--q93tjPigvdJLEokOtSqL9S262zz0iGkF2onXJD4sEmfU0Vs6UEJ9XA3jDFd-Gp_Klvw6wyGpggOmsxh-LaHKu17Sas_p9ID_vRJ7Fi4V7ecBHVK2SKy-uDic3TKcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سال ۱۲۸۷، محمدعلی شاه قاجار مجلس رو بخاطر مخالفتش با ایدئولوژیِ مشروطیت با کمکِ روس‌های حرومی، به توپ بست، و بعد از اون
دوره‌ی دیکتاتوری و استبداد سنگینی
تو ایران شکل گرفت و
آزادی‌خواهان کشته می‌شدند
یک‌سال بعد با اینکه ستارخان تو محاصره شدید بود ولی جبهه هایی شکل گرفت و شمالی‌ها از گیلان و بختیاری‌ها از جنوب به سمت تهران لشکر کشی کردند، و بعد از به‌هم پیوستنشون، سه روز درگیری خیابونی شکل گرفت و در نهایت، روز ۲۵ تیر ۱۲۸۸ محمدعلی شاه به سفارت روسیه فرار کرد و تهران فتح شد
خلاصه که مردم حتی بعد از
یک سرکوب و کشتار سنگین
باز هم ناامید نشدند
و پس از اتحاد اقوام ایرانی
، در
نهایت به خواسته‌شون رسیدند
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68261" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68260">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دیشب تو اوج حملات، ترامپ از جمهوری اسلامی بابت آزادکردن یک شهروند آمریکایی که تو سال ۲۰۲۴ بازداشت شده بود، تشکر کرد
خلاصه اگه امشب حمله‌ای نشد یا شدت حملات کم بود دلیلش رو بدونید
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68260" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68259">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DblqGxbHhG9SGKTZLYxLZfo2keg1i9oPpUr5C8b1h4d5cnU89r6Izr4oXvdpaZ7yPqEodOIGHOKPb9AuXpYbAjJNR-evS8n3gK8sK8QA5up0WRmk_UIpxvBGUZUnzYpnM55TxzLaA7AASQq710RG3eL8hertBa61_uJDnf6nqKeONPzCQ1ulUCgHhFMCsHGStpI5OcmnSoYoszpaUFk9o7c09xaZ9oJcG37HQKzO5I4AdfE_hc-d8MMPUw44DP-8BegNTXk56HGChX-YhUTEeo4Om6bdBSA-Dm_Tu_ufnph2BPOBjCMuw93M-ZOyaHG5VUP1YAexRUvrqZeJBPj2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوارنگاره جدید میدان ولیعصر تهران که نوشته «who is D nexT one»و هشتگ لیندسی گراهام هم زیرش قرار داره.
همچنین ‌حروفDT- اول نام دونالد ترامپ رو برجسته نوشتن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68259" target="_blank">📅 15:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68258">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">💢
مرد پاکستانی ، عاشق محمدرضاشاه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68258" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68257">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2UvBAffc8QdtR15R1TFo9V2x9Bw-x93nO3CibuwBfr5VaGP8as8W6O_fBedWDEaSo8fYSSi8Z_717u4PhLb6cq5S2eniPj8umkPstwlglMmnJ4QDnAY0CMtEfa2k4c3GTE4G41DYD8oJmHK0YJcBrxPU4bo7tQq8EvY0wfB8kRrK0SGr1iBDWM_3xy066Sv138-etGzuWqhKZg1dcWtYLv23iXgKHxd8rBuQPNKEcShw2beRGhfSECGOWx2-Vu6KNJuJF_OOpf-CacRPKllvew0Dk6jDlHKv8EOf3GPV3reUgoicPCsfXdMMhvn_2lY-U9bmWE6IHqBUl3fwDchGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نتانیاهو سفر برنامه‌ریزی‌شده خود به ایالات متحده را به تعویق انداخت؛ این تصمیم پس از آن اتخاذ شد که مراسم خاکسپاری سناتور سابق، لیندزی گراهام، به زمانی دیگر در اواخر ماه جاری موکول گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68257" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68256">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=B95_NwwU85hpnzi65hAuvVSQ98O8NOcamMqRxMjdUReLp91LkKVditcX5p3DQJ7jjOWjP98C7j78cqe0zt0byF46H7pSwqpIk2WC9ZQCsmm6yj-ECgsouPlx1WwWGjuX5vNzl-UR24PM5SwJglq1sEOIvXnTQFdh6EiusN7YQjjUPEbklZ9BeHlZfRXrAjy4ukXnRxEX2WUzPplfMF2ukun_XzhwjLtnsM2oKBxMtuLtmJaF3LBtpzsmix16l-mBzFO5pGey_rYu-WcKxh1KZwCwNN7GSmTR5z2Ur95I3nu0Ta3a_aWHe1_hk4fLwuOpHkQigJZHnbF2BNT8LyDGOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=B95_NwwU85hpnzi65hAuvVSQ98O8NOcamMqRxMjdUReLp91LkKVditcX5p3DQJ7jjOWjP98C7j78cqe0zt0byF46H7pSwqpIk2WC9ZQCsmm6yj-ECgsouPlx1WwWGjuX5vNzl-UR24PM5SwJglq1sEOIvXnTQFdh6EiusN7YQjjUPEbklZ9BeHlZfRXrAjy4ukXnRxEX2WUzPplfMF2ukun_XzhwjLtnsM2oKBxMtuLtmJaF3LBtpzsmix16l-mBzFO5pGey_rYu-WcKxh1KZwCwNN7GSmTR5z2Ur95I3nu0Ta3a_aWHe1_hk4fLwuOpHkQigJZHnbF2BNT8LyDGOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش مجری‌ها وقتی یارو میگه تشییع خامنه‌ای ۴۰ میلیون نفر حضور داشتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68256" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68255">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVpcmc9W2VPwuh6UY64nXonsDNC-lBzXoSCaBIU8fZ9Lh80lYqcfkpzWNgbJHEOn5J26DFe8DTolwPAi9giTDbvi65VNkjP4WIqUGVsaPtnC6MMH_Ye-5wqfenhVsKxDA5tHKaxK1RP97hGTlLBhahCVIMK6VY9ZvTiZJxAcJFvEsnYVdPNobk_REc5OS75hePlllcMK7th1E9E8lLvPD4BLwmqE4rTCTVubn4QXQtK_JUaX3CibUHxnM1QXwmT01JCUVsrrbNbDqFz8A13gkXSE4hm7I0aTYoTvbnrGbmxRmvfFcPTif9HtrR66TUosD0-2giDjN_536cSaMPRNOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فینال جام جهانی 28 تیر (یکشنبه) ساعت ده و نیم شبه؛
- یازدهمی‌ها فرداش عربی نهایی دارن
- دوازدهمی‌ها هم دو روز بعدش عربی نهایی دارن
بهترین راه اینه که فینال رو با گزارش عربی نگاه کنید
دیگه عذاب وجدان نمی‌گیرید
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68255" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68254">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2gqH5SuC78mBVHmMhpXpveY8yRE8psRatTAaNTRCL1P7BIrg9Gm69N7Uo9kty5TXBPNjqLfZuAOklAAG2LsmFKTa56XzuCdxGfNteMxzqL2zRZoyRP4yUKUpoOaJ_ESTrHU6-HIXjuxLUB-NYj9yVceO1mbKBBeg5RdqLGZUpkmvVax3K6b8HBIQMblUJ3GaNklNHMJ_CHv2wIMtZWLOrLGYIqsr7Ww0J08iex9MCulOn9s2roxUFtqudsOvNNZzUVsLMz3H8XhvMOQxay3b1YzqD7dNK-1NruHSOsSsnFULGJ4m_9TDoYzoxiSwVA3SZ0QZPkx4Goh7KQoovp8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:  کارگاه قیرسازی حرم آتیش گرفته!  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68254" target="_blank">📅 13:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68253">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=TPCbenQNcq0MzSBV7MhXgfVAndEJb2g0OWIQqHw1kFTLIaHJiITUwpnAZioVUCr5Pa8ZJKGeNp-47goGgNpUikNylR1ejGa0IH8RyxYqmjB4qDVOjWkmXbb3kD_NnoRXfGDMNPKl-Im9pMlQUGxVNVLXAC8coRj_Aw4QDfC_clrdJFwgoAjmuphFer0jfXX1n3lolQ2NmYaeyQj_oO-wsP-rGapY01mKnwrdGJjPlCtlAPIqLQoFu4tu65UcLSe4mJFOCxtqC59VCco0YqpOkK6zRN9RDaC46ioHwXbxCbV7o5RmaBnyHvTEad6CKL9LFm_m6yGuH-MW3oBC1VUbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=TPCbenQNcq0MzSBV7MhXgfVAndEJb2g0OWIQqHw1kFTLIaHJiITUwpnAZioVUCr5Pa8ZJKGeNp-47goGgNpUikNylR1ejGa0IH8RyxYqmjB4qDVOjWkmXbb3kD_NnoRXfGDMNPKl-Im9pMlQUGxVNVLXAC8coRj_Aw4QDfC_clrdJFwgoAjmuphFer0jfXX1n3lolQ2NmYaeyQj_oO-wsP-rGapY01mKnwrdGJjPlCtlAPIqLQoFu4tu65UcLSe4mJFOCxtqC59VCco0YqpOkK6zRN9RDaC46ioHwXbxCbV7o5RmaBnyHvTEad6CKL9LFm_m6yGuH-MW3oBC1VUbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تسنیم:
کارگاه قیرسازی حرم آتیش گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68253" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68252">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwMlAiFq8L1ambIh3Ec6WikB56yBlbda-F1vuYuWWx0usF7UJV8T7ZOs6gx3cS026x4Woh04PxZEx7mz8y7FOjsGyakhtxw49ro4iwB5cTeqFZ1YVQ09FJUPTozaiXkNNFVr5yt8tnkjwXKNIiWcjHOT0bqgbPrfipXECcXkOkJ0K60xHO_R0BTXrCEsA3h48gwEAiDR2ZVxM58qdD9MW54qSUNDz03U4eiI_tEqym_cEaRxXit1FJ3vB_oEBlXgbB9LRGXF7ijb7a6a7HD1o3CPfJInl_cgf53LdFjC1ZtzY_i_PKJUwIYG7P4kXBOc_PIXS5W4DSzIG_u1CiKpCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتش‌سوزی در حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68252" target="_blank">📅 12:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68251">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314324694e.mp4?token=gqFdjQWDp54FrN5nLFu9uLpvVZCREA20_5-D-Y9bmVJoeeYIxIdD0hxTuz4w1-9Gefa8qM54Lrdzp9rJHHqD3MG2iJHPRNla1IONCdtPYT-W6gtIYKzmvY-8xPnvLqLmIg6lUFywNv0m4xiBQRiKja8W1C96jSqXXc4JR5J4A8iIyz0qNN5c_M-f97egAmRq2H35qVHlWMVTyfeXoduFKWPCUq-9ho4RmFA7MkA0NHe0AcIl_Fm4VMhlbxMcclkkSrVBuUTeOVzIHTDvKpbX5LYYOisgK_SxXLycRToPIDa3ZrpXF1W_rKLs7T1Gsp2FNfnE6JhIG4biw2ZYK6s2zoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314324694e.mp4?token=gqFdjQWDp54FrN5nLFu9uLpvVZCREA20_5-D-Y9bmVJoeeYIxIdD0hxTuz4w1-9Gefa8qM54Lrdzp9rJHHqD3MG2iJHPRNla1IONCdtPYT-W6gtIYKzmvY-8xPnvLqLmIg6lUFywNv0m4xiBQRiKja8W1C96jSqXXc4JR5J4A8iIyz0qNN5c_M-f97egAmRq2H35qVHlWMVTyfeXoduFKWPCUq-9ho4RmFA7MkA0NHe0AcIl_Fm4VMhlbxMcclkkSrVBuUTeOVzIHTDvKpbX5LYYOisgK_SxXLycRToPIDa3ZrpXF1W_rKLs7T1Gsp2FNfnE6JhIG4biw2ZYK6s2zoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام تصاویری از حملات به ایران منتشر کرده است.
این تصاویر شامل برخاستن جنگنده‌های «اف/ای-۱۸ئی سوپر هورنت» نیروی دریایی ایالات متحده از ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس آبراهام لینکلن» و شلیک موشک‌های کروز «بی‌جی‌ام-۱۰۹ تاماهاوک» از ناوشکن‌های موشک‌انداز کلاس «آرلی برک» است.
اهداف مورد حمله شامل پرتابگرهای متحرک موشک (TEL)، سایت‌های پرتاب پهپاد، هواپیماهایی که پیش‌تر قطعاتشان جدا و از رده خارج شده بودند، و یک دکل مخابراتی بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68251" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68250">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9rsg0NQu_WWMIH4SduUHUj6lsRPz58FvMAvqEbKKVhddmhalkrzoPBKgnH9hdScWtWfhk5OFwwsaNp3xdl9BBo9CAPEmSxmfylpoYdqsfH-INHXcGjejOauSRBsOY83Qdp-H2OReraYJFogPoiw6Q63bgYvEbMMSPi18chNP3LSKlaa6yG3_TwqjnMuOO10YNfp-zIp7eeloAes7cNuRVHLZwW_Fl-LeaBU-9OY_y7fjj5OmTb1V0XbHGf8yjX6lKpc0mM-vh7pknv4vK7EuukQfnavQuKbWZgH-yz1a76cJrWZOvoiaJiz-huwUX-kIBHDKx-WT-RZ84umoux2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ:
ایران اجازه داده یک شهروند آمریکایی که در دسامبر ۲۰۲۴ و در دوران ریاست‌جمهوری جو بایدن بازداشت شده بود، از کشور خارج شود.
این زن اکنون در سلامت کامل و شرایطی مناسب خارج از ایران قرار دارد. آمریکا از این اقدام مبتنی بر حسن نیت ایران قدردانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68250" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68249">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=sUSjDBsbedv_kPCKmiOtKoMa_hI0ZaSWpulPx-yQfzlQ-tGdZ-BoqtdfnSmRyxeAPYMCFN5ApBCO1JyIAqyjWqUuU8g38VgqZsYO1sMrTVkXVY-VFKZDNXbnVBeHo2cYt1ycWnuX9f3vNCbLPOQf8Uh5ZrYrqkjoTGYYn4chZbOf0mairouuLOf6W-zzL9op7cKCNU_EHvzc5RhAQMQEInFqStinCDDTO07xrSJ-0p3HQTC8_1Lb3M1pCCPJMcuGsGNzfRAZF6tyvWBSKKnD9fdzdnOar0BiVIstxf4ah0P3M7Cmn0JFJLa6TVmGsWoZcacyZQp6lTK7XeUJtSySwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=sUSjDBsbedv_kPCKmiOtKoMa_hI0ZaSWpulPx-yQfzlQ-tGdZ-BoqtdfnSmRyxeAPYMCFN5ApBCO1JyIAqyjWqUuU8g38VgqZsYO1sMrTVkXVY-VFKZDNXbnVBeHo2cYt1ycWnuX9f3vNCbLPOQf8Uh5ZrYrqkjoTGYYn4chZbOf0mairouuLOf6W-zzL9op7cKCNU_EHvzc5RhAQMQEInFqStinCDDTO07xrSJ-0p3HQTC8_1Lb3M1pCCPJMcuGsGNzfRAZF6tyvWBSKKnD9fdzdnOar0BiVIstxf4ah0P3M7Cmn0JFJLa6TVmGsWoZcacyZQp6lTK7XeUJtSySwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پهباد شاهد در حال رفتن به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68249" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68248">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=KhZo0yPoMkhOG_Ho8mdM0d6iQJETmJwVTjKYq7FGF5u3pq4Yp6Pz7FhKrvR6NyK2tcepNWmkcSviW3vYHqB9zqAP6QaAhAzVx7k-JWVCN2wKE_8PDCfxFMwKFquwWEynRRz4-cLUzLUk2Cms9AcJ9Umsc-ox0OHjEeJmVGC1XY2wKVPImUhY7sGAQSuE7hz4u2ssBYHr2FDhifLmknuJeAGZXsBJoCxpSNB4xFz3e1QLmbP_7YSnHElb8ijy9DC0SEQuPSETOziImIaRhOP6TbmIe1X_qUHX23vCXOEfwr_sDka0htY3RlqSB7MZfu_B9e53_8weSekap2KmuUXDTq_D45FicXSAMB2plrb3bJnABHAooc9fofQR2pkC2eSM4en4TAivH_J66E30HEETN3Vl7X7-44XnjbMB0-vB8JjPwZB4vGuoLCylLPlkdMKCpFUbbKlQSmA8Ycbp8C7GXmOtxcZNs5RCr67TIBU9XYzmnmpQyVwrdVnFC3IFQ1oZyTbDkoxaAVNAANnFVqtLD1ZEqp-FCvI1po0xkW0QBuDsPHhCExp3pudCQPwOTdjyOcXMBINCsSYj6SUnBMR0DSDMKR47nt_iIO4a1r3SaY7VocVleZXcAyNZzGW1AlzHbTWcqCVZEiCGjcVsuFfAPEwPg3umwBTAoymf9NBbvTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=KhZo0yPoMkhOG_Ho8mdM0d6iQJETmJwVTjKYq7FGF5u3pq4Yp6Pz7FhKrvR6NyK2tcepNWmkcSviW3vYHqB9zqAP6QaAhAzVx7k-JWVCN2wKE_8PDCfxFMwKFquwWEynRRz4-cLUzLUk2Cms9AcJ9Umsc-ox0OHjEeJmVGC1XY2wKVPImUhY7sGAQSuE7hz4u2ssBYHr2FDhifLmknuJeAGZXsBJoCxpSNB4xFz3e1QLmbP_7YSnHElb8ijy9DC0SEQuPSETOziImIaRhOP6TbmIe1X_qUHX23vCXOEfwr_sDka0htY3RlqSB7MZfu_B9e53_8weSekap2KmuUXDTq_D45FicXSAMB2plrb3bJnABHAooc9fofQR2pkC2eSM4en4TAivH_J66E30HEETN3Vl7X7-44XnjbMB0-vB8JjPwZB4vGuoLCylLPlkdMKCpFUbbKlQSmA8Ycbp8C7GXmOtxcZNs5RCr67TIBU9XYzmnmpQyVwrdVnFC3IFQ1oZyTbDkoxaAVNAANnFVqtLD1ZEqp-FCvI1po0xkW0QBuDsPHhCExp3pudCQPwOTdjyOcXMBINCsSYj6SUnBMR0DSDMKR47nt_iIO4a1r3SaY7VocVleZXcAyNZzGW1AlzHbTWcqCVZEiCGjcVsuFfAPEwPg3umwBTAoymf9NBbvTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون طرفدار حکومت:
من الان شرایط ازدواج ندارم چون نه خونه دارم نه ماشین
بدیهی ترین چیز برای ازدواج اینه حداقل ماشین و خونه داشته باشی اما خب من ندارم و پدرمم پول نداره که بخره
دلیل وضعیت الان بخوام کوتاه توضیح بدم ؛ سخنان حضرت اقا یک طرف ، وضعیتی که مسئولین درست کردن یک طرف
الان ما باید تا30 سالگی بدوویم تا بتونیم یک زندگی متوسط درست کنیم
الان یک میلیارد طوریه ک ما شما با هفت الی هشت سال کار هم نمیتونی بهش برسی و انقدر هم پول کمیه که شما باهاش نمیتونی یک واحد اپارتمان بخری
با این اوضاع 50 شبه کف خیابونم و هیچ ربطی بهم ندارن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68248" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68247">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⏺
صحبت های روح‌الله زم درباره حلقه نارمک و جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68247" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68246">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvdpt7C37oUlzJYoPntqWan_sTIwIYDqjs9PDHLtgFSz1RccJCr6hQWpDShOjl7Hx4E5Y2xiXla4SFEvEqK_fH88g5LjnSxTzdHuiAjUpRIk8RwYuqH9ezAyyFOqgdDZknNQ6L3NbITOAzOGXtboMI9drbdA5d6qtjbep7EKlH_c26zlVGNYMmh9UyyVz5_w-ZVvYXYlkvOhN4zKuqoGY-TEuq10RU3sC99NqbZcqzNoJwW2PR_oKvMrFrWTOVQv33GQ_AnNdoMhk9ll6fnTh3aM4yPERUuAb1tnBAKZoFwBR-axqcjkLszdxnCo2dDVctXfxcX3Ctb3eTYRCKHJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان به نقل از دو منبع آگاه:
دونالد ترامپ، رییس‌جمهوری آمریکا، در حال بررسی گزینه‌های گسترش عملیات نظامی علیه جمهوری اسلامی است. به گفته این منابع، در نشست سه‌شنبه اتاق وضعیت کاخ سفید، راه‌های تشدید فشار بر حکومت ایران برای کاهش کنترل آن بر تنگه هرمز بررسی شد.
بر اساس این گزارش، ترامپ احتمال عملیات برای تصرف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و حمله به تاسیسات زیرزمینی کوه «پیک‌اکس» که گفته می‌شود با برنامه هسته‌ای جمهوری اسلامی مرتبط است را بررسی می‌کند. با این حال، او گفته است ممکن است عملیات زمینی برای تصرف جزیره خارک را کشور دیگری انجام دهد.
سی‌ان‌ان همچنین گزارش داد جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگویی تاکید کرده است که جنگ تنها با ابزار نظامی به نتیجه نمی‌رسد و در کنار فشار نظامی، گفت‌وگو برای حل بحران نیز ضروری است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68246" target="_blank">📅 09:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68245">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68245" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68244">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KRtlzhi_Y3xdn5W1PQWAmctqqHsTVjpFX5vUH-48Ohr0x3CUK7FxMsejtEiPZPv8gKfqBKqUlUnhlNj62OMQgME7ioBJAdwKvSBNSV86-BEXcJURWiaJaDRLM173LIEt2ikNxZG2G-iyfXKEyOmUmv1Q0yH39IHYDqJq2gkOwdTnq4pd_n3KmYLMT2u42WLN25MkgC6qpV0b2Ir3_Yb6pY3mXPRuIzVwU4DbBN3R7nJ1FaxpRlpYzXgbHxb6HjQE-dCETQ5emfjRGmuXSvKpZFkoINHDjmJvsqjcqNaUVz-3qsL8PDqQt3X3z_aLSj2kbKI2AqFln46LBc0lRf7R5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68244" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68243">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=t01O5MDke84_K0BOT4tshgEaPXxQYOyaK9XEImvn40i8mVBu4gBe3WAXgcxhL3iFDtgcnS3W7vrXwrejY9eaPPT9-PCTc74FAxLXmdg1haCzRgo4c-jsi7tlRqIOwMzXriY52eogNn7_UJq6XbpZ2XG-ziPj-UIQs-x8SVrfTqZuBZSQcQqvaamCzB8o5lLkD0yLngKpjkcw8Y_LfNFnLCH2wtkyBE_tTb7rVaFJ4R8_mIhj4A9EgzrnWETEIZeOUufBlK7Y3hZWp3RZ2y0KI8OJYCmQDZYx9STPduXiYdItyV5Arp_U0hgd74xvkbF0rPp_dFdtAJHuBtXGkzWc0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=t01O5MDke84_K0BOT4tshgEaPXxQYOyaK9XEImvn40i8mVBu4gBe3WAXgcxhL3iFDtgcnS3W7vrXwrejY9eaPPT9-PCTc74FAxLXmdg1haCzRgo4c-jsi7tlRqIOwMzXriY52eogNn7_UJq6XbpZ2XG-ziPj-UIQs-x8SVrfTqZuBZSQcQqvaamCzB8o5lLkD0yLngKpjkcw8Y_LfNFnLCH2wtkyBE_tTb7rVaFJ4R8_mIhj4A9EgzrnWETEIZeOUufBlK7Y3hZWp3RZ2y0KI8OJYCmQDZYx9STPduXiYdItyV5Arp_U0hgd74xvkbF0rPp_dFdtAJHuBtXGkzWc0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پرتاب‌های متعدد موشک‌های پدافندی پاتریوت به سمت پهپادهای ایرانی:
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68243" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68242">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=QIOgo_qOP7UZSEwPYlzfEnDs7F7ra4yfOdeMozNxY2-7tA9ikLot3hWeA0t5oz-cnCo0ED6v2wOskbs9ZSfjYGx1k4j0ubePueu6-7YO6zZumVWNb-Am4wvLRIgaEX6ZU96eyUBWgaszyrRIzgNXbrt4NQAfjRbRt9RUcM_OZKrLOiZ639rQmAG8xl3X1BHlYCYv51Jb18sjlPn9YUSdbbl4vUgVFNgd0GGRkdoXo1l42Y83CqRMktRpzLAbFlg3sEdGzuDds7L6EtgOFadfENV-ocHhRWs9WPBxIgott3bSEv0Wmh3Vi37DAKqmm521To1JeOPnN5dTD09wqIJRww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=QIOgo_qOP7UZSEwPYlzfEnDs7F7ra4yfOdeMozNxY2-7tA9ikLot3hWeA0t5oz-cnCo0ED6v2wOskbs9ZSfjYGx1k4j0ubePueu6-7YO6zZumVWNb-Am4wvLRIgaEX6ZU96eyUBWgaszyrRIzgNXbrt4NQAfjRbRt9RUcM_OZKrLOiZ639rQmAG8xl3X1BHlYCYv51Jb18sjlPn9YUSdbbl4vUgVFNgd0GGRkdoXo1l42Y83CqRMktRpzLAbFlg3sEdGzuDds7L6EtgOFadfENV-ocHhRWs9WPBxIgott3bSEv0Wmh3Vi37DAKqmm521To1JeOPnN5dTD09wqIJRww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68242" target="_blank">📅 02:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68241">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0lxo6fmmbhhdqlaGkvoCA-WMUao_S-b-AVz5dK3e6oJJ5k5LBXhP2BqKOJlOOORJbsCHntszRBYZV00svGerZDgt_SVFVtHRV4aGc1l7EZFXT6KjCF_mji9dAG_cPhaOYvvdan-Xxd1AR49YrO_og7fpXXpI3rOyqTkNHvsqLsN0tzKxq5sDavRsMNZFD2DlJb_IDpRiREutz3zFF-2rkXavUYsxAR_ssNO10-ltGIgCcrD9dkLmRlhbDEPS_Ez3M1WBbPijN-gkB9vnGEZ-7Tle3GtK9XBPLr2PMyqcs6eGGAhK1sx8drQQi2ZbZNl7IFtJfGzP_0N5O4sy22BqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68241" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68240">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68240" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68239">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=sR93TwZEkuA6R6pvbK9xvE_Gu6Kip-rjO6ktKceTlVeF-tXZbPpkLzqYX_hf5KI_MDujlbq80NhTVZEvXqlhkK-ga87sZIYHgdqRteiJGXjQ6WlY4chv-o1J2xyZwZN0HkCmhPcMatTBqu3p3DiC1mUjZLSZrwLyC_nUK1snH-giB0_dDlx3dFfmYBwlt3KP2PuEvj5Hiyvjvkt736ALwlgEgD3gge8SynSeVHrkgAQIjxI6ul1YRR28u0tDhWgDHVbq1ej_pZKv0hS7QCxM4aij8vVWG3sDg-01JUgDkWj7ImFKLkntItYQyLUfI7eJuiEDT425afNKAiDbU7ACRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=sR93TwZEkuA6R6pvbK9xvE_Gu6Kip-rjO6ktKceTlVeF-tXZbPpkLzqYX_hf5KI_MDujlbq80NhTVZEvXqlhkK-ga87sZIYHgdqRteiJGXjQ6WlY4chv-o1J2xyZwZN0HkCmhPcMatTBqu3p3DiC1mUjZLSZrwLyC_nUK1snH-giB0_dDlx3dFfmYBwlt3KP2PuEvj5Hiyvjvkt736ALwlgEgD3gge8SynSeVHrkgAQIjxI6ul1YRR28u0tDhWgDHVbq1ej_pZKv0hS7QCxM4aij8vVWG3sDg-01JUgDkWj7ImFKLkntItYQyLUfI7eJuiEDT425afNKAiDbU7ACRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سنتکام تصاویری از اصابت چندین موشک هلفایر به موتورخانه نفتکش M/T Belma که در خلیج فارس در حال حرکت به سمت جزیره خارگ بود را منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68239" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68238">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
بندرعباس بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68238" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68237">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baTF9VW49ZfQ1VeDdM4wmnkwZbof0ncZsiY859jdxSUgQm6nLH6qCeZ0hB_f8gKvDFlJ-SxQ_Bfvgxzy1L73-cKMVec4oCvsOsLCZugIuZ-j-1AlX6gnsqK6YRksNBAt7vSRVWGQCZulBJ3rmfFNMzCx64am5B-XRqVTj-tX7h-a1xV1Btwwe4za7iv1FzpD-yu00DP_dMNghsYIt82XnsFGmHeA-rLpXJyVUxFc402O1r18MRz6kfG--RRVRAVko2QpjI2bu2WivnUNd9Ub1y92m6z-ZoHReWAsv_jmTcItHXI9Y3QX9vHCCEgoIw4IwhyBID7LLdYFLiwS2N3OHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68237" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68236">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68236" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68235">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J4YyIlfG-npUHdNxk1VUYUhWPvU6q1lNnyC8X8CZb8l4OSh8ZjdYplzUz04F4FKHo_uL7Cz7yQGfEHgJ0JZKTukhqOqKsmd9x87QCFitLjYN77_SsBxgjQ7nwkti5ZTDAj2LGmHxbNyBld-_nK4NT8TL7OpHxL0fr83w40-i2JRY5S_vbWNFwK4GpG2_W4fVSfVRD-MCAv9uPK91Qz6HPkebdYZ1sQmLXfcTmxXBZle5kMy2sO7tHR7kbqa4CYjtyq77A6-24Wen-PzaZ_8fBco5Ff-ArCMFF3I8HxKA35FAndNUWGdmuAq8RRajPCB8oEZvlazydsW56liYCPpJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68235" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68234">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">من خودم رئالیم ولی برای مسی باید ایستاده دست زد
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68234" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68233">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=F5bgmKiqUzHzthe38Mrz1VGQfSg7duodJUNrK8JNqup4vlYPvNlH_6akooUP5HOF0pNrgebaIyCyfcREXBIxVJKeguWny5tuNVovSukx85vONN-nkRVgePX6cnBcaBCu8EZ5DVn-cW2LYrmkWbiTOur4934xMNFnB7RfxR7GrTO5-Wz0B5Q2ooQON2WrcBKGmaGhKX9Y8U6eKJkNP345rKwP_Cky7VlEwaMJkNSbAuakcw1L8lIK-xlHV3wTZLBU_U2adrSLpQisH-qMJQG83esvYJFNS35KlBLsJg1Q1Ln9SXWRvhDCiKCS9aWX6DCr2C3muLBBTf5RtrGkbswfSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=F5bgmKiqUzHzthe38Mrz1VGQfSg7duodJUNrK8JNqup4vlYPvNlH_6akooUP5HOF0pNrgebaIyCyfcREXBIxVJKeguWny5tuNVovSukx85vONN-nkRVgePX6cnBcaBCu8EZ5DVn-cW2LYrmkWbiTOur4934xMNFnB7RfxR7GrTO5-Wz0B5Q2ooQON2WrcBKGmaGhKX9Y8U6eKJkNP345rKwP_Cky7VlEwaMJkNSbAuakcw1L8lIK-xlHV3wTZLBU_U2adrSLpQisH-qMJQG83esvYJFNS35KlBLsJg1Q1Ln9SXWRvhDCiKCS9aWX6DCr2C3muLBBTf5RtrGkbswfSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68233" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68232">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گللل دومممم آرژانتین
💢
💢
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68232" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68231">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گگیایایتیلیاایایاااللل دوممممم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68231" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68230">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68230" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68229">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68229" target="_blank">📅 00:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68228">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">درووود بر روح پاک مارادونااااااا درود بر بیبییی</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68228" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68227">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کلم کیریه، کیر تو انگلیس کیر تو کیراستارمر #hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68227" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68226">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379978a151.mp4?token=RASNzojDQdEmXaLBW6uF7pX1ZHoTo4Oq4xtdrkbmftgzPRxKO1KT6AtfD902DoXww6EFPZ5XNXAXzNry4jY8_WyUyFhN0jLljEyyP_ycvinWHAW6x31jOf5m8fTmrrYKx2erQZsUBHmsCOPNMErLI2_0JQ00-Xmd0B_ubxT2_tRClZ37lgPLyvq-tWwkteM6c78bgdrKRHcOBUAtrbvxC-OKT5ovFPaCwboEeEAxVN9xKzedzWPMAMeAWm5saedW6M7zxUWf5Xau8PjYMzRi8jPvMHcgkx6i7fwWhusuOBDccjD3uqxcR07T_pOEm1xjk9i62YtrVjSqfyL6RZhRPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379978a151.mp4?token=RASNzojDQdEmXaLBW6uF7pX1ZHoTo4Oq4xtdrkbmftgzPRxKO1KT6AtfD902DoXww6EFPZ5XNXAXzNry4jY8_WyUyFhN0jLljEyyP_ycvinWHAW6x31jOf5m8fTmrrYKx2erQZsUBHmsCOPNMErLI2_0JQ00-Xmd0B_ubxT2_tRClZ37lgPLyvq-tWwkteM6c78bgdrKRHcOBUAtrbvxC-OKT5ovFPaCwboEeEAxVN9xKzedzWPMAMeAWm5saedW6M7zxUWf5Xau8PjYMzRi8jPvMHcgkx6i7fwWhusuOBDccjD3uqxcR07T_pOEm1xjk9i62YtrVjSqfyL6RZhRPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی به زودی شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68226" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68225">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94485380c.mp4?token=BXeiDAAk97OyKXHuoYFtlCWF5jvqXWuZFnyuSCIucvn805CgqFqaevnvCK2aczBRWhXe2crvodY4ts3hhBkCOTQk3e7v6eZr29UDH-gT3QuFzmuiUUxPD-pIAWtAQ1FNcDPiRwjvnZ5dBBVxpVW5ejal9AOjn3yRNTFz6vL9tyq4X0U2-rWk_y_3aT5vNtB_kdkB7ngZMEkyQvppZueHM9UkqDd7c3auae5PmWdrOVVIf4tbY58SA45fGxPQIkOsb-0TNYKTV93ih3iC6dNm0U2KkDDs0u3-C55UoQ9Eeotf88cV39UHslCHWuugqYNFVBmSXtMNVNbxDeLTSfYQ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94485380c.mp4?token=BXeiDAAk97OyKXHuoYFtlCWF5jvqXWuZFnyuSCIucvn805CgqFqaevnvCK2aczBRWhXe2crvodY4ts3hhBkCOTQk3e7v6eZr29UDH-gT3QuFzmuiUUxPD-pIAWtAQ1FNcDPiRwjvnZ5dBBVxpVW5ejal9AOjn3yRNTFz6vL9tyq4X0U2-rWk_y_3aT5vNtB_kdkB7ngZMEkyQvppZueHM9UkqDd7c3auae5PmWdrOVVIf4tbY58SA45fGxPQIkOsb-0TNYKTV93ih3iC6dNm0U2KkDDs0u3-C55UoQ9Eeotf88cV39UHslCHWuugqYNFVBmSXtMNVNbxDeLTSfYQ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به سپاه راسک سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68225" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68224">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به آرژانتین توسط گوردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68224" target="_blank">📅 23:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68223">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
انگلیس اولیو زد به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68223" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68222">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=qidd4kAGyflu2N_SE_cx8Vswf0x7aumnLYR7G2UElSovx4XWEOxs9a-MzhyUj0q5XuTtNv9vdNiuVlDjQYF0Dax7nmOniSVOddpUKa0nEC5Yl23Gz69vcXyo2mG7B9rpWEi-sVwa-YcX686tHAFtC_yCmb_v8OkxzvGT18liT52i7dUanwq1fbHRctvQWpE4At7_z9RUaGXRWR043rszpOO18tI9uvJk5z7ww6hzkyqiJ6_QNKjfmu0prnmn7z0Y80fejI16WG4IMaQC8LpgA9Awd2PmZEoke6gRAxcNztr12SL2ml_j4viujPBrkmfZDhUISv0qgZfbaJEPUIQtIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=qidd4kAGyflu2N_SE_cx8Vswf0x7aumnLYR7G2UElSovx4XWEOxs9a-MzhyUj0q5XuTtNv9vdNiuVlDjQYF0Dax7nmOniSVOddpUKa0nEC5Yl23Gz69vcXyo2mG7B9rpWEi-sVwa-YcX686tHAFtC_yCmb_v8OkxzvGT18liT52i7dUanwq1fbHRctvQWpE4At7_z9RUaGXRWR043rszpOO18tI9uvJk5z7ww6hzkyqiJ6_QNKjfmu0prnmn7z0Y80fejI16WG4IMaQC8LpgA9Awd2PmZEoke6gRAxcNztr12SL2ml_j4viujPBrkmfZDhUISv0qgZfbaJEPUIQtIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما به این نتیجه رسیدید که نمی‌توانید با سپاه پاسداران مذاکره کنید، آیا این به این معنی است که ممکن است آنها را مانند داعش از بین ببرید؟
🇺🇸
ترامپ:
بله. همینطور است. درست زمانی که داشتم به اینجا می‌آمدم، تماسی دریافت کردیم و آنها (ایرانی‌ها) می‌خواهند ملاقات کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68222" target="_blank">📅 23:43 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
