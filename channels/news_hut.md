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
<img src="https://cdn4.telesco.pe/file/QR1ePsiGx-a3pmKpiBAZi5GXhn55iS2k6AzlIscQ0VJDiQb2HnzNbIy58kmgMKbhI1yLumAOisYkIUNJGGylo6lB-4lOC1V-YJ_8k3rDr5crH4q1ZSfaYJEtEtzILLeNGBHD9794uPZBZKE3_1YBaiVeU6PecCpmEuS4gYEbv0_XWbewkNx4WpjL1S9QQn8SgjI2V2xsjfRMWqqH6HbDMKrJvt-Ld17QT5VkrI0K3V1ep7OkTLrFC4w_GWu_Z74-k62-BsJZI_f8qTXhNcYfvvCF71cWG4mMN1IHVciTjhWYmKIqb8wV_1nYgsAZS2Wqsiyi_rO6_CsD3xrTHsfsKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 192K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 04:37:41</div>
<hr>

<div class="tg-post" id="msg-67628">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/news_hut/67628" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67627">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qEJU9rkz96XVND6V6EvppLj6uQwbgG3-sEKSonmcYeCMequP6zRmqwm_Ur7MK6W7PgzabUx-Vzoy43n3p7E5oTM_7n9z926sPBSQ6dBwZZwXr4D9XF78L7rGNWzZfOGoX79m0_j-insVuS0Yo_o6LpkhMXG-OTpgSDrffislbQ6tIBt2f_wVzCyfT-k7c9RB8kDeGNu8U-j9cWLQKrOfCEdcnunUoRbFMyEzoiKgqN8YJqFmBoCXHKSbUNjITwq-BlmonkVHnNw6ldFJbaPM80NPyefb05WqVO63N7SpdTI-Tv8hhfiBfBGj2Wk0J75q0JBYf43Yj9Hb7ChQJ8rQ_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/news_hut/67627" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gg0rGcSO8kWazN2dmJcuR8VdfjfiqEcIW65DkwasRtl8vLmJhoYlroXxkBR4uT3cc15ox-oBdxFy773iJk1DbNX0nS30w3IH1nDNqnF_z5O4TI2o5HcmGA-s5WRb4esDefLKvAGA0SW62M_mxtfnxX0-T5ctTZzRa4UI7XaXAxcjNtJYKxonV8iUlPv31W5JOR0-Hq_ksycZA6nNDN9sXnwnkxfFEHKilCowIbEZ2opjL4pN5BvmVjC3jRFN8YrYlM9ea_kjsH5Vxmq5b1WjCpQfXd1RenA6rtEizCFgFTJ7eDH22wvMZTFAqAez0ad88l2Dl7RzKFMWWcwjVld3mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jgf1MirOVnZxYYapBvQCsLmPDk76ZacVegVgIiPoMKON7r7FcslrpIE2sjtAh9YlAUJ7uRQrl_txwZumRJfwuwbbw-tLEzGsKBmq-M8AVWwyD-_HFGlfDP8_u3mqXgLH70pumLBnshIZRNrN-ztjKUQbdJhRehQm_Y6sPEQxmTufHeK2OlMBydNZ3f_BiUzmr3fLoMzRVsF5xaGaWfmZOG-HGmox83EcWhi7ZCRBsmB01KLyhywko9sE2Xi7owq5Vdm-rNlClxumFHfSYwpLZ2hQ64zxHDuqEZGcZ8Uu0YEGDP0yNFjJszzAuqEHniSN0Wi9a1l0ItH78AEcnEGg5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENzd5fv3-3CqMA1J3C8Qgamcb2EwTAJZyrHFzdN-6DVvzlEhj_U-C8iLTJUnV_FM-r3QxGBfoATcoMmVyfIXzodGUJuwI4valKSPKyrSjCwqQXTGJA44RShjXBoxnXvjOeqGi-DHfOMnf32VCBD5iyzRpXxnUJtWSbwqes5wINSfmy3gShN42rrQmYruarCdDcS4JlUHC2MjSvRC_HaTorhOi02gwSN9GmRoiqs_GfhF-WGn8c1BQCKBIp1i5rhYmOwWxdHdv9he2cPdYQyLs3Xyzyot1p4tdRvuVTiX690UnvzfUNph8LY39Hx_kvh_-_Qamj-xxBdILTUvqK1xHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
راه آهن نزدیک آق‌قلا در گلستان هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=J0z6I9vm1-1TPMBZDZbILpDeQNCI9ulV6qwSERJAxRq2XmiCaE74C-RTsRQDMqHUXgJnsIEaB-staLom80ZXGF_CzGZFZp035i7BZ4ElCSIxaRk_gH_D3zNTqd0hGO4yaQK4VGG2ORMrUSJANoUjD5QLa5e9bioF9tc-6DDxkPVrIXYWzfaHuWA_sexiHV4OdfEt5M_9n907I1ePnbVXuaZyIhbxX8JOYekgkdNFacsu0DBYLyi-w1gIR47B8GAASDa4DdYACu73w60VXa_39PUxouz9T9K87IZk7A-TJb9f5BIDB2KDuMgjFzkIwBv8jGy3tIfuoCuSo3uSrGGGLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=J0z6I9vm1-1TPMBZDZbILpDeQNCI9ulV6qwSERJAxRq2XmiCaE74C-RTsRQDMqHUXgJnsIEaB-staLom80ZXGF_CzGZFZp035i7BZ4ElCSIxaRk_gH_D3zNTqd0hGO4yaQK4VGG2ORMrUSJANoUjD5QLa5e9bioF9tc-6DDxkPVrIXYWzfaHuWA_sexiHV4OdfEt5M_9n907I1ePnbVXuaZyIhbxX8JOYekgkdNFacsu0DBYLyi-w1gIR47B8GAASDa4DdYACu73w60VXa_39PUxouz9T9K87IZk7A-TJb9f5BIDB2KDuMgjFzkIwBv8jGy3tIfuoCuSo3uSrGGGLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
ترامپ: چون... راستش را بخواهید، این موضوع کمی عجیب است. کمی عجیب است. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان یک توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=UQohQwcvxKp3RcR-qr6RqXfd1DZOXTQfTYczVZNxBQAY5QGsFn-M6wNxrET2uQuFvVQQvHMKFpf2xPQSXJdrHVZC6SVgyxeAwRuifSQTJgi_3j79LfHt_9nRAbg7vNa0AZ89S2lNBT8RAvr3qNPmBAPu9HoSXyBv2gnjnno493lAdxiT5XgZ4SB16UUrTcJEEDlj0aZ7TBBUJ7NVvYN3_Bhtjipfq-wwHNcw9JWp30-dnlPKPHybnlGld-UAleIPsaos2bAWbRTPZeWGN-7gr84I1ztrwDSHcotHQdoZx-vzwOuJf3JUC-YDxEyiMJc7M9B-8BuPsjRUHJ6B9mzVwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=UQohQwcvxKp3RcR-qr6RqXfd1DZOXTQfTYczVZNxBQAY5QGsFn-M6wNxrET2uQuFvVQQvHMKFpf2xPQSXJdrHVZC6SVgyxeAwRuifSQTJgi_3j79LfHt_9nRAbg7vNa0AZ89S2lNBT8RAvr3qNPmBAPu9HoSXyBv2gnjnno493lAdxiT5XgZ4SB16UUrTcJEEDlj0aZ7TBBUJ7NVvYN3_Bhtjipfq-wwHNcw9JWp30-dnlPKPHybnlGld-UAleIPsaos2bAWbRTPZeWGN-7gr84I1ztrwDSHcotHQdoZx-vzwOuJf3JUC-YDxEyiMJc7M9B-8BuPsjRUHJ6B9mzVwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما از نظر نظامی، پیروز شده‌ایم.
آنها مدتی پیش با من تماس گرفتند. آن‌ها واقعاً می‌خواهند یک توافق انجام دهند. اما من نمی‌دانم که آیا آن‌ها شایسته این توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/news_hut/67622" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=R2sHnNSJCEfCIQWvRWrnxcu9wZXBBM4RKCbTEwEjC36w0N8TffvPHLJzuaj8TgXNiyUpJMwYgiwVI30q2dZtGE16lYis79GtZKcjnS-XzlxDkNkYvYLjviIrPf7IqgGhiBf-F1ROwGJae9TCS-zA_JmagrWJtHf56o1mc5syU2adLc0AGUOfVMBeIzmmTqvMg3diQjkrRPvyETQLqz-xdy3Mn4CSYq9J_Az3cCpPkYs2bOLFo4tNizdbF_cJ97uz-kvx6exFZbsIi7aGzzEU5bTO7grUoKwAkqeM73_ZSFPJMMFmcybeu81-SQiqAJXGnqJMHJy6SZod3VAxwgtzbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=R2sHnNSJCEfCIQWvRWrnxcu9wZXBBM4RKCbTEwEjC36w0N8TffvPHLJzuaj8TgXNiyUpJMwYgiwVI30q2dZtGE16lYis79GtZKcjnS-XzlxDkNkYvYLjviIrPf7IqgGhiBf-F1ROwGJae9TCS-zA_JmagrWJtHf56o1mc5syU2adLc0AGUOfVMBeIzmmTqvMg3diQjkrRPvyETQLqz-xdy3Mn4CSYq9J_Az3cCpPkYs2bOLFo4tNizdbF_cJ97uz-kvx6exFZbsIi7aGzzEU5bTO7grUoKwAkqeM73_ZSFPJMMFmcybeu81-SQiqAJXGnqJMHJy6SZod3VAxwgtzbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما به آنها ضربه بسیار سنگینی وارد کردیم، و من می‌گویم که ما به آنها 20 برابر ضربه وارد کردیم.
هر بار که آنها به ما ضربه می‌زنند، ما 20 برابر به آنها پاسخ خواهیم داد.
وقتی آنها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/news_hut/67621" target="_blank">📅 02:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d252421.mp4?token=cznnyZLYmE-2bM8pizCZEz04W7ZpWPLjaHxw7saRy7KTZ1jyNTRGEsY1D8u2YchJlPVOeimesD694mA7FCPiRjsLmpMMpdyWNCAID4iGnAgbp2jiSjqoY5s_diFKMb8zFTSA1OJW1Pj3G77Aw3umeQgYn_3yXCEvsQP5gasocHIeDlL5QHhueye6vvDiJNZ0lDTmtxr1P56fKQ0YOTGU11HgFh4TrqxGRMP-E6LcK6H-S8AwWBJo4cCVjIhg3fMyPKtpRaWiCgKtapMHg5FHkZzo3Q045fiku-NHGD3MNodIpIOftFqPwyaW7LpHdx0UyjrWpneEqeWsn1dOkHsYUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d252421.mp4?token=cznnyZLYmE-2bM8pizCZEz04W7ZpWPLjaHxw7saRy7KTZ1jyNTRGEsY1D8u2YchJlPVOeimesD694mA7FCPiRjsLmpMMpdyWNCAID4iGnAgbp2jiSjqoY5s_diFKMb8zFTSA1OJW1Pj3G77Aw3umeQgYn_3yXCEvsQP5gasocHIeDlL5QHhueye6vvDiJNZ0lDTmtxr1P56fKQ0YOTGU11HgFh4TrqxGRMP-E6LcK6H-S8AwWBJo4cCVjIhg3fMyPKtpRaWiCgKtapMHg5FHkZzo3Q045fiku-NHGD3MNodIpIOftFqPwyaW7LpHdx0UyjrWpneEqeWsn1dOkHsYUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
من در صدر فهرست(ترور) اولویت‌های آن‌ها قرار دارم، قبل از شما.
اما اگر من [مشکلی] پیدا کنم، شما هم [مشکلی] پیدا خواهید کرد. بنابراین، شاید روزی بخواهید شغل خود را تغییر دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/news_hut/67620" target="_blank">📅 02:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
انفجار سمت آق قلا گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/news_hut/67619" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67618">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در گرگان
@News_Hut</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67616">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=SzhejQl8Mcv-xGtUvYjwz24iDcsXMr7-Cd8l2LydYYS4uVwrgGsnZGzvfSRvOm5gTBrDkWTdL7CoQn_XxK2RHIsxYeeqRD3iVYsC7NuqeQZIDXFa7TbY_7K37ooy0GdgtRnlMbdU1Ouy8Bk8I-CQQCpE3XdkshGHFHGL7CAS19xQ-RsoSRvLOJlgaqqozTpYbHgvSuWfHGK9VWyDvw_R3MRPN8O0XLXasELv64jMVleZodCDj6LpIgGTsJGv1ATTb4ZyR_67pf-9jr8ut7m86OndnDwsqwWRseH80v4-4aP_08nmggFS4GQ0HIMCfVfJTBnzqRLIspWPLgE32JCvrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=SzhejQl8Mcv-xGtUvYjwz24iDcsXMr7-Cd8l2LydYYS4uVwrgGsnZGzvfSRvOm5gTBrDkWTdL7CoQn_XxK2RHIsxYeeqRD3iVYsC7NuqeQZIDXFa7TbY_7K37ooy0GdgtRnlMbdU1Ouy8Bk8I-CQQCpE3XdkshGHFHGL7CAS19xQ-RsoSRvLOJlgaqqozTpYbHgvSuWfHGK9VWyDvw_R3MRPN8O0XLXasELv64jMVleZodCDj6LpIgGTsJGv1ATTb4ZyR_67pf-9jr8ut7m86OndnDwsqwWRseH80v4-4aP_08nmggFS4GQ0HIMCfVfJTBnzqRLIspWPLgE32JCvrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت نوه خامنه‌ای رو با سرعت دارن کجا میبرن؟!
🧐
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0DTz1mRQH-_ZF3QcNaUPzPKPRTybhoa5jKovGU6haJ5EM50z_VhlHzJIf5kmiclsY3KGNzNtu4Yrd7LoFvbfcvW3YRT912g0BuZJZc-jvrra8AihadtsTMerF8W2yUiCV4dKn8KCb9e4IQEBnx8cyR6A-hY2gCVJ4K-5h0GF6NV92Hk4ia941ry31dRdMcfr27V1BOL47mNTCAhfTCuZeKzvTrYhDkxWE4oShpweRzHnTBRBT7r1Nw3gmxqS4Bj_9aWAzzLtnOENUv3ZXFUGArLc8Oj5Zx3Q_dO2-HDV_mv11yttIoZcwGM94XI_C-hnIosgI6sY9rGo_qLija78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقاطی که امشب توسط آمریکایی ها هدف گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67615" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67614">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر بسیار بالااست.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67614" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67612">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcLoHwfiXdnhoT_0YBlBbjfdirce2X7LO3MyvpZFG6b4RFM1vmoDRs3HXCi21A7B6ZgRwDLkga8goMXF8SKWyK7QtIXuXr8grpiXtajXplVpyg_1FkPbc465WjnFnYpM4jWFFP6FGf9Oahtgv5q0F4Mn8EZhcBHfeQeRO55_EL9cQj5BOVoN3PX_sMMKsVTu9yCR4RmEPd-zVYn5-_-ajls9_F6nUug9eozmPUq8VZVwftipjOopQD3N-r9ouSLSu7YN4o74Z0HC5MY03so7eJ0d8AuhhFApR_KFfjgDz8MfXWKzH1H61R_FUwzZXp3GeT1Hu_ViVNGmL4Ayve8D7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=lE1zZUvJhrMeRZMXVdJjQuLdVoLL5dJ_T02YhelxR__5szupH-ET14tj4Jclh66mMJmlf7AJdc2Q5lc6QJrIedQpB8kYi7w_wRaN_X0-DhTc7WvyCI7cQcsrfsrAlj3G6Lflo5n1Sml9WtLryyHaKj3QuKanyGaDjGgIRq5xjYDeAbPqDj8CwjgobxSZMGiFJC00kxgt84oIya6ZpbMBDyt8mY3qiIU3hBaeLkQweRAzewfInSEEwM6AQPs9N5gqv8xNrgD762E2ZgiT_WnpYqYe4Jfr5GfgsdXjMbYfBDM0hfeJase1JYRUFdlXGFAdlCVvY_AOsCq3--IAdvhlXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=lE1zZUvJhrMeRZMXVdJjQuLdVoLL5dJ_T02YhelxR__5szupH-ET14tj4Jclh66mMJmlf7AJdc2Q5lc6QJrIedQpB8kYi7w_wRaN_X0-DhTc7WvyCI7cQcsrfsrAlj3G6Lflo5n1Sml9WtLryyHaKj3QuKanyGaDjGgIRq5xjYDeAbPqDj8CwjgobxSZMGiFJC00kxgt84oIya6ZpbMBDyt8mY3qiIU3hBaeLkQweRAzewfInSEEwM6AQPs9N5gqv8xNrgD762E2ZgiT_WnpYqYe4Jfr5GfgsdXjMbYfBDM0hfeJase1JYRUFdlXGFAdlCVvY_AOsCq3--IAdvhlXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای منتسب
به
حملات آمریکا به ایرانشهر( سیستان بلوچستان)
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67612" target="_blank">📅 01:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67611">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyvQOaESy4VINNR_v5j-kfxg57gfVLkLLnaNXUlW0ecrwMka7WoohEwRbqcwLyhkORb3oK_FxD1BATxmSUguJa_RG1ydLz0K2RbK8oDLolrfjv9JCM_Amf_JMw-JSiuAzl-YEnLcKaPw4RV5HfQ2qFO6gsD1gwz5be0O8wfVCZaAEDEOqywudqHKJIdFBho5osP91064m2JVrHeiAbiUX49Cat7ehul5ScTwnGupix7u0wLrDJ0VN2SLSpcvVGkc7YTWGWUr3L8h_mlhI8LFDmQAFj5qgwUTf7ClS7Sv0J1h9_tF0MIf6YmdclH_PHx3sdC89B2pfCddkECKKtnjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NqoNhfh3XY2zxq1k2mjhlF0cvJbcCZa0trxhhRFJJCa8gY6TASv7NbdaH-fviopT-pFajoCNIVBZ6xlrOGKz6ivdmhUEokLzr5CVzaH_oQuu5T00ZLt593YWBc7pzhDIeSixz02wk0UbRGJaGcR-LfIEQwv8R3rkEbq5bllIInSXU8EWg8hC76DxOSzED4KrC6FeHG64sbCdgLMnLNKmgtYsOZUOTgroSqWH0V2BfhwTW582lYUb2a4l_l9J3dRk5mq5gyVOznzP6EMtq1ELMUdQEs73MEdvGCJHsABA6Zxzv80I3MZN4syLw9ryMTP3epHW1-YVKqTpuJjjmgUcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsKQIUIAqcD2DEZgAz9mURBqTol5Xz0h-fAY3UPXaxewfaYo5xT-wT5_LF4f-OKyWKWhskr2Yboq7qxObgoFC8uWus9wsWdK1g-eBuspIZNah_cK9JIjxiUHwbHq1yuAMmB40Gcw6khgrZ49VboXWN8u0Lga-RjJH5MUf906fB2RdgGT65vUGF8FBtLsgB4VO-EkOzfqfBA9rxjZJA2LloFc6MP79loN0arqMvLKhpjvfUQ1fH62Sj-8DTRI-mlQA_v8nXJp_YlAiGphmwOafyL6LsAQIU_MEgcxQJ0CnwonghLx1hcWO8A_vb5WmUV9HLYyj9HdKrGFYOZiZjXS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-xUowJeUfUhWUH05-Q99PPgmMMjlPv7dLm0YwYN4DdBPPct6h5Qb8Iqg5tiXpaP4MtNOTR_0kBKp6QEVlLhH8ftMr4XFrn_fjF2Ow5MNz9SdKv2IEhTmBmmdYnwGVXSTCy3xZl7ZC-8d3aEUbXnoOKEmpRHPQe5mwulYMJjuQ40kI74uU1nXUmddfT2WioW_PKIGHG40mWfM4qqx745K2dbvC-1NB9xY4ein38z8s9Thr5k1IViZQglR5aVrXZqmwQj6Fm1bOdjt_giJyf6WHErJO0v0EeihZfVSxvK-TVOAwaDVT9B4WbJM7n-9qbmdWsXqdnyo3NFuCgXtCjiZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ تصاویر حمله به جنوب ایران رو در تروث سوشال منتشر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67608" target="_blank">📅 01:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دلیلِ این چص‌حمله هارو متوجه نمی‌شم واقعا، آخه کسی که زدین رهبرشونو که از نظر اونا جانشین امام زمان بود رو کشتین، اتفاقی افتاد مگه که الان بخواین با زدن توالتای پادگانای سپاه اتفاقی بیفته؟
صرفا این حملات شرایط اقتصادی رو سخت‌تر می‌کنه همونطور که امروز دلار ۱۸۰ تومنی رو دیدیم، خود ترامپ هم می‌دونه تنها راه حمله زمینیه و اولین نقطه هم خارک ولی جرئتش...؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67607" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67605">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=arkpnGHhpmPcHY0MRKRvjKSr7JGg7jk3dlzhOmkss7g1czXq2Q24B9HnQC8VTEgnfnWZrG3qsZetfpAT2McR0K4GlvnG29ueeE4Q42FCtonJxR5S0MDB3sSZsxkJ72H2AZREyhIwCytpcCPCv7I4rSUtjaysED_H8tPfwrb6j-SE6_yxFEae1h_Pq8CwF_Vdz2oaxDqCWfkcYiRJh7TLacF1IdscFdOfyOhdeErHX6ARBTJuROLKHyxJZj5F9RegBYNKts6bgfLlzgNGPM389xnj1UknbNjO7mv14pEQS250aEfYUGUN0JNk4cIQAmTWrHWfccnQaU9e6ltxIH1CRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=arkpnGHhpmPcHY0MRKRvjKSr7JGg7jk3dlzhOmkss7g1czXq2Q24B9HnQC8VTEgnfnWZrG3qsZetfpAT2McR0K4GlvnG29ueeE4Q42FCtonJxR5S0MDB3sSZsxkJ72H2AZREyhIwCytpcCPCv7I4rSUtjaysED_H8tPfwrb6j-SE6_yxFEae1h_Pq8CwF_Vdz2oaxDqCWfkcYiRJh7TLacF1IdscFdOfyOhdeErHX6ARBTJuROLKHyxJZj5F9RegBYNKts6bgfLlzgNGPM389xnj1UknbNjO7mv14pEQS250aEfYUGUN0JNk4cIQAmTWrHWfccnQaU9e6ltxIH1CRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدئوهایی از لحظه حمله آمریکا به برج کنترل دریایی اسکله شهید کلانتری چابهار :
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67605" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67604">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
انفجار های مجدد در جزیره بوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67604" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67603">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ماشالا ترامپِ شیردلِ مادرجنده‌ی املاکی
😊
#hjAly‌</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67603" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67602">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67602" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67601">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGsCi7EaTgb5c_O6iy90qEyzvpg1zRmiyqLQPcAFm6MufUCJx7oEnZpA8BZOVhajiFD639doyUykKY6BWXd8Raht3s_DZkShlO76v-zIjQuW_Lf6XuLy7NalMjyhqgJ3qu7lz5wrQmWWr6wFL2bdmq_8vpLQ2eDp6ClSev3nlDZ_F0AQ-eEjDDtsPBBKwYkAJ2AKPsFmwBuTUpNfZQYd6C5slDbYEL3g7EPGIjFTJ4n8W4ojYbxfKGXYjqJsDsZSxpaY2SfcJS6fBQYP9dWNA2DsnvQ9xaKuj97SuqyFtW0p3qmp0V26l49Rvwm7A2EdWMB34sQdDEJQcF-suY8cYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
یازده فروند سوخت رسان نیروی دریایی آمریکا بر فراز خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67601" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67600">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFp9mRFQE4lOq7DzYIJiiKWIPlS3To8afzvdTXBlzKdpvWLYyOTDWAbuSZMO2mO5pp5BghDeRGaAvICqT_930yonnbuNuBOneQv5ST4pCsLaQqCnHG6y0x45EuZUJzDKNz1t90XU7nfuuUXlkfVWyPB8PYXIrwxEPK3304JluL5pg-L2sHcOkjSZ01F8AMf9FySgHNkR-mdQDClgrtJSPotyMY3_Murub9KgYHbzapB6NhhSbNwdnZuv1fCkerkCxqyzqL9hbzIEBqtki-tDtegvTFxianwyZzK0Mh25txokjHC1qxyju4XnflB5xVp-ek5tTeDL-VeIMmSwxvni7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت شهباز شریف بعد از حملات آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67600" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67599">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
صداوسیما :
نیروی هوایی آمریکا در حملات به چابهار، اسکله‌های «شهید بهشتی» و «کلانتری» رو به همراه برج کنترل ترافیک دریایی این بندر هدف قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67599" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67597">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rP6t7Nzi4m9kh50THwLnM7D1EWiaflnRccuJnwCryb5QEllEd060cWfT_VsqW_I5bWSJqGl4HL4MyYrB9fzAiS_PBfmM3JQ_hlXeySS9iz8_r2-BfoQnEVlwr3sITU8XrFG7ZzWYKkIVZMENpeSJoQ18Y4ajjzAOTfjGxn_HwQun4Ns3Gnx6HTnN7uo76peV6lEepdgIXaNNQGa7qOIuTSUetKVTRP-YImOg366RZu8Mmuy_SWLqfh9v9YZUd0bpwGEmcB2t0eCzdRGWmYrLMo4DePoS9O4gbwyvfW1ldcMxdnLQEbzeQbaNzxPftKP3zjgu9vVnTRfLpO6FQrjaNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H2RYjTSBJFaF_uUfGKML9a4wcqfXUGLSNPOq4cZfLSXIaoolAxKcvytjU0UHM-f6Ey9_sIZGwYS3zWVDebIeZ1HR5mSDkr8VMA7EMjUY1VtSqA2M7hlhHtDHclo5DBVYW3OpOovEYlaRBPXv0dUQg8FqsZK25FWdwwvQvfT38TtPy7jYUfp11w2Fd-Lec1vomXyZRLR-e80FX9Hgel2enLLz4F1HLXEG_i8Ug42dBIWyhfp9IX1BomMKnSkngnUYOmIXqwCoqwInGeS459YIRzEZDwg1WKN8GBIUvOFGKWRa_fvsbF-buXFfZrXDUOTB3e67o7o0_UWnbG8EeR-eKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
برج دریایی اسکله شهید بهشتی چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67597" target="_blank">📅 00:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67596">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇮🇷
محسن رضایی مشاور رهبر:
دشمن متجاوز و همدستانش به شدت تنبیه خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67596" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67595">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67595" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67594">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
چندین انفجاردر بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67594" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67593">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
فعلا تمرکز حملات مربوط به خط ساحلی جنوب کشور بوده
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67593" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67592">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60497304.mp4?token=XciHaoh89T20vPfKsZdi8d1RP2jGNDCxdK1EmvlzW9BV5pXJZmH0EmwEat2f5OS0n553HrTQwCEILikvJRoe72rNY3yMIaEouht_WdujTDvld-dPa1lwXHANkjVO3WhRLcSQDoY-Czg7wVWcp2HeYDmxAo4M9IOy0jz4u0_2uCUOfwBb4o4nudcpYcDSEB8erTId7F9JUyo1BJeDay5RqzFQZUYrz35k8KaxkfAGDSCMRImvX2Xzma5SUR78HkHh_NENNqg0I81b0AxnACPakE1XLZ08ZNveKR3wKfZkhk4eR5KKUY92E-sFUmswKXDZHql7he0sLyy3aAP8CqsGdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60497304.mp4?token=XciHaoh89T20vPfKsZdi8d1RP2jGNDCxdK1EmvlzW9BV5pXJZmH0EmwEat2f5OS0n553HrTQwCEILikvJRoe72rNY3yMIaEouht_WdujTDvld-dPa1lwXHANkjVO3WhRLcSQDoY-Czg7wVWcp2HeYDmxAo4M9IOy0jz4u0_2uCUOfwBb4o4nudcpYcDSEB8erTId7F9JUyo1BJeDay5RqzFQZUYrz35k8KaxkfAGDSCMRImvX2Xzma5SUR78HkHh_NENNqg0I81b0AxnACPakE1XLZ08ZNveKR3wKfZkhk4eR5KKUY92E-sFUmswKXDZHql7he0sLyy3aAP8CqsGdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67592" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67591" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1WCH7qbFLjayqRhyRkFyxvXIJc9qmPOADPW-ocRevqQfHUSLLvvBsgs5F-WgWafqb2bKM9jv0tJeidWbnV40892pshp8RLMPDxwkCv2E5pOjmTNmwogfQhvUU9bKTKMJXHU1TexNkZZDHhTQ6Ep4OKcZLnBenKR3iuiVGl3Wko5JMz4-72JhiD5I_I1HXjHEt7nLmsKOYhbMqlQi2qwNuh00rBXsXEGJGWe7bVVX0e-M61EGgtj8q8YCPtc8wPUJ9r60yCSBsjsX0A1Nc5p91tEcuEwu3pOIhIhSr-px5gdjbaYAYqFlmePctQn2N3YC2Pm2ri6vmQQMU09fNcb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=vuBbmdfAYFmu-hMPRaR5-X6OoSn5UvtKqimJx4Cc1qrmAUAF5xAd0YU3PA8rzCLkMAL9dYyU3TdjvII6038mDJLPssBBP8B-QOwBzZ76qnKJhp8TkEDb3GGJSNgwxoh1WJnfeOz7d66gBu-agvyR3iKfAssj4hHzw35Ei-5ko9jcqMV-tBRY_zPyWrpNAXhW32sO4-ZW0mXejwfEDukM78DQeAhMCWQW7s-VnDPtUNdMCWrmw5GceJ_fmwCFIcYFeIlTUtm2cCxXGpCvLwvel7L1jkbdX-uvQy2msI9bzXKMysl9phBrPqDtuZH2Q-FjxET-Ery7DfE1USdjHJ0HXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=vuBbmdfAYFmu-hMPRaR5-X6OoSn5UvtKqimJx4Cc1qrmAUAF5xAd0YU3PA8rzCLkMAL9dYyU3TdjvII6038mDJLPssBBP8B-QOwBzZ76qnKJhp8TkEDb3GGJSNgwxoh1WJnfeOz7d66gBu-agvyR3iKfAssj4hHzw35Ei-5ko9jcqMV-tBRY_zPyWrpNAXhW32sO4-ZW0mXejwfEDukM78DQeAhMCWQW7s-VnDPtUNdMCWrmw5GceJ_fmwCFIcYFeIlTUtm2cCxXGpCvLwvel7L1jkbdX-uvQy2msI9bzXKMysl9phBrPqDtuZH2Q-FjxET-Ery7DfE1USdjHJ0HXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67588" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=lMEuFHnfwKmkoP84k0ZaRzgqUsYnEKx18dCqgmlYRNv6KZsBbkbUB29af5nT5XbNalZjMMC7bQ3NnpBjYygvKuV1PXfp_zvnBrllsLYCSVtbsrLdaPsVWRs_5-AqtFR8RG-Rx_5F9ZyPGbAC_twmlIOCAMKzieFcmoAuKqHhaGMhC1UQe3FeO2BuBm0RasnSMDfO9grWKJsjwPkNTSF4iwXGLrxoEiPEXWN9ZL1UsRlH0qstolgm910t4y4miyVLLGyCHQ4Pw9Ou1jbbxhbBSvzBCmKcgY7ReEPOKxI2CvFHK0CcXqLwOudbS83euZh_SE2304K_z9ZsZzwJC8DraQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=lMEuFHnfwKmkoP84k0ZaRzgqUsYnEKx18dCqgmlYRNv6KZsBbkbUB29af5nT5XbNalZjMMC7bQ3NnpBjYygvKuV1PXfp_zvnBrllsLYCSVtbsrLdaPsVWRs_5-AqtFR8RG-Rx_5F9ZyPGbAC_twmlIOCAMKzieFcmoAuKqHhaGMhC1UQe3FeO2BuBm0RasnSMDfO9grWKJsjwPkNTSF4iwXGLrxoEiPEXWN9ZL1UsRlH0qstolgm910t4y4miyVLLGyCHQ4Pw9Ou1jbbxhbBSvzBCmKcgY7ReEPOKxI2CvFHK0CcXqLwOudbS83euZh_SE2304K_z9ZsZzwJC8DraQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67587" target="_blank">📅 00:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67586">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره ابوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67586" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67585">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=ZBn8hb6KkmQahoWxVvaiMz40fqnM1-E_On0C7vU8IUYGhgqv9xSGkr8utLsOcwooJpRfcIsQv3hBT7QWOYEJTg-kpPnmzgS85vvsf1F-yGkolDIDI6-YtEYjuACvAJo1iCQSAYvaZaWEkCrnn4gbZvqa0z1ieIO2MJZaD4YHBipPvkRHBtGLt7TAStA35ZNMFJPapBw-dBNkO7g2GnFzvOgSm_QHfCQegzg5oMu5ISsFX89gKdNe-Xix9q4ccroAavgd1AAHR-XkdF9wgGt2QUwglZ8L1WVOicwpb5J26fQbquSA3sfzw3NQOb19DtC81LcjlEJAOknWjWHQ6ZO5VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=ZBn8hb6KkmQahoWxVvaiMz40fqnM1-E_On0C7vU8IUYGhgqv9xSGkr8utLsOcwooJpRfcIsQv3hBT7QWOYEJTg-kpPnmzgS85vvsf1F-yGkolDIDI6-YtEYjuACvAJo1iCQSAYvaZaWEkCrnn4gbZvqa0z1ieIO2MJZaD4YHBipPvkRHBtGLt7TAStA35ZNMFJPapBw-dBNkO7g2GnFzvOgSm_QHfCQegzg5oMu5ISsFX89gKdNe-Xix9q4ccroAavgd1AAHR-XkdF9wgGt2QUwglZ8L1WVOicwpb5J26fQbquSA3sfzw3NQOb19DtC81LcjlEJAOknWjWHQ6ZO5VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هم اکنون؛ آنتن زنده شبکه خبر
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها بدانند پاسخ کوبنده‌ای به آنها خواهیم داد و امنیت را در  هر جای دنیا باشند از آنها سلب خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67585" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67584">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=PSuKPVaUxpwzcqzqzWZFEKgX4uC_LDAeIqgAaubSgu5bNxCEmCTW18NpHiuXVt84kSndug1LsvcFAoV7M_aiJOK1BXqX5qBK9d4qJqiomkzuycAC2wZe0LvlKYuIKlXwxLzHiVtjRQs5fVzzDlfNP2ZhUYiQZEWpBTS6nBd75t5nIAV6gQ6B50sX8PKcpWczs1I3Fo9yAjscDITHsP8a5yOckQsWy6OE6H3-qoeCzNmzcG5mnUGG0hlcY_XCoCZEAUV1eyteXfgyQ9c-PJfUv_8hohSb4kPFK_IVeaoaDDIT70aeeuPn5btVpPhO__jXEp19UnmILYkkDTgT-GeNxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=PSuKPVaUxpwzcqzqzWZFEKgX4uC_LDAeIqgAaubSgu5bNxCEmCTW18NpHiuXVt84kSndug1LsvcFAoV7M_aiJOK1BXqX5qBK9d4qJqiomkzuycAC2wZe0LvlKYuIKlXwxLzHiVtjRQs5fVzzDlfNP2ZhUYiQZEWpBTS6nBd75t5nIAV6gQ6B50sX8PKcpWczs1I3Fo9yAjscDITHsP8a5yOckQsWy6OE6H3-qoeCzNmzcG5mnUGG0hlcY_XCoCZEAUV1eyteXfgyQ9c-PJfUv_8hohSb4kPFK_IVeaoaDDIT70aeeuPn5btVpPhO__jXEp19UnmILYkkDTgT-GeNxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67584" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67583">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02d221609.mp4?token=aMQ649KW2HD1xa5NUopTOYI69qeW88HTXakMhzYNMSKLaFzlvNA0fB4XJuxxacqrPUQsZBiRXUHuTV_c3iDVCKYH_IManCIwbZWcJ14XPBKvPvxUigYLQ7rz3QQMF1IHbjNX8u0JiDOhws7b66T8zVehFKp97OEes7OZaJ6atPxUXPPEdIArW22cr94Nz1TI3-DZax9bMuAun4zMlbvKzT6gHkR5v9lkm3Rikeh4KOUPKJuafHONrxKP-5kb4cnXPflNluqydT1uqlYay0iZ0WbHSjnTmaGJLQ0P2iVKFXx8A36FFZJwjMH6Ia-skxJrDFOo0Plys-Kd54woj3IRKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02d221609.mp4?token=aMQ649KW2HD1xa5NUopTOYI69qeW88HTXakMhzYNMSKLaFzlvNA0fB4XJuxxacqrPUQsZBiRXUHuTV_c3iDVCKYH_IManCIwbZWcJ14XPBKvPvxUigYLQ7rz3QQMF1IHbjNX8u0JiDOhws7b66T8zVehFKp97OEes7OZaJ6atPxUXPPEdIArW22cr94Nz1TI3-DZax9bMuAun4zMlbvKzT6gHkR5v9lkm3Rikeh4KOUPKJuafHONrxKP-5kb4cnXPflNluqydT1uqlYay0iZ0WbHSjnTmaGJLQ0P2iVKFXx8A36FFZJwjMH6Ia-skxJrDFOo0Plys-Kd54woj3IRKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67583" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
نور نیوز  :
به زودی حملات ایران شروع میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67582" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=axECZAeBrnCDssdVQQXrKNh0wwIIKY80fnhBtgEovTM45RQ-grSHmLGi92E7hjuoOHoZWEqyLnh7gIoTZBm1uIlAl3Y8B6ZZe7Z9ASpHczMVZHhL72zYH2sgK2gENgjsB3X-rCYTYf-T5CBKXXwctJILP4iRF_uODBIlnVUKw1p7IL-jO5vbV00V9lkgfRTtc4ijzz6XkvEze984-2oU-W0as9TPRsw-EyMrD9lNHortyN014-n9tyNYSoMbrwgfkLbYap9ThMo-AFXCKihRhpP5vgLK8NSvwO6-FNCo_8m9MhJKX-Azj5gtesCqYsjaEtxteB-Jxsy0_FhdH06eFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=axECZAeBrnCDssdVQQXrKNh0wwIIKY80fnhBtgEovTM45RQ-grSHmLGi92E7hjuoOHoZWEqyLnh7gIoTZBm1uIlAl3Y8B6ZZe7Z9ASpHczMVZHhL72zYH2sgK2gENgjsB3X-rCYTYf-T5CBKXXwctJILP4iRF_uODBIlnVUKw1p7IL-jO5vbV00V9lkgfRTtc4ijzz6XkvEze984-2oU-W0as9TPRsw-EyMrD9lNHortyN014-n9tyNYSoMbrwgfkLbYap9ThMo-AFXCKihRhpP5vgLK8NSvwO6-FNCo_8m9MhJKX-Azj5gtesCqYsjaEtxteB-Jxsy0_FhdH06eFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ریشهر بوشهر دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67581" target="_blank">📅 00:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=rAx_w1xjHBP62denb173IntRbGLKW_uoiTMt5vc10_K1PikMbhvp5bN_bRtrTFPu0OalvDAmqwyL67ZAXQfPaPArS-ERN2zDS5lYpBDZEF9FvpBU2XU8adHmtRqPjmFUo1tFOlzZCzKv0GfB4X58QuNqMdSLDNp8x8a4btPWbom-8PPoIyzoI1xPm0gPAEAv3TDzDRNIw_c5EIuq2W-3bphTSA0AtlIyswCv8N_S9pnOxcd0zuBTdQ9KPWK9ABjd7xSnRcFZLdPf1DycGz06DWrJsTuwXHfDKc_HzZmszdAPlUn8xx6lFwUpUTXsDgfJQ5JxyGZJic-nyBh0tcuo5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=rAx_w1xjHBP62denb173IntRbGLKW_uoiTMt5vc10_K1PikMbhvp5bN_bRtrTFPu0OalvDAmqwyL67ZAXQfPaPArS-ERN2zDS5lYpBDZEF9FvpBU2XU8adHmtRqPjmFUo1tFOlzZCzKv0GfB4X58QuNqMdSLDNp8x8a4btPWbom-8PPoIyzoI1xPm0gPAEAv3TDzDRNIw_c5EIuq2W-3bphTSA0AtlIyswCv8N_S9pnOxcd0zuBTdQ9KPWK9ABjd7xSnRcFZLdPf1DycGz06DWrJsTuwXHfDKc_HzZmszdAPlUn8xx6lFwUpUTXsDgfJQ5JxyGZJic-nyBh0tcuo5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظاتی از حملات آمریکایی به شهر چابهار، ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67580" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67578">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4rJ2RGctZ_1eGle03sihEkeUb7XUqkxXcogmU-GoeNBm2Gtl84jXjtnCASR2_XZT8aJGy8dTbkfJJOCpTY4kDcuTuNHpkFYzetnvjz60HHsbNIk6kXpe4coasiNVGJTHreZqFs1eEHhrCBDJgkqVF0zuTfqh3l3R2qO4Gd0LVDfT6UCav8lEH3dDvY7XWOUilO1it1q_189fUqn3f4MxONp2U-vTq0R39Ku6rQtgOWUv4HFFp5DMvbsvOyjRUpSMxNt5PLOUz7EgGqEOMJbYe-1FnrHFo3KpextDc40ua0WqudZ080Nfm8xve3UY4vNWIjmhV4_cQQBE5FtGBWWvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2l39HsV7YTnA1wPipxIRoKsbjvQGqjPsWvv-WQojOWJz2NrojpMJTpVvmNy5toA6fMZw8K4s4x5aO-9_6LvIcYA0w2ArEK0m2qNFWCheeI2gCGuQIYESrN27QYW4XwdsAYu0fmwDg9WfrI0mxJy4pXiPAL1HjjEpRKUc4-yx5z2eBti5r_3g5f02gUNRGTbqoDi1Dfohl_tlZ3LSF3FldXjbFGULGXn2-sdDmV9G3WRfU5jXvA9Faf6y4c7IfQC4p7KpvLAD3S8mFZWCP2ya7oACsH2jyW8U6r6dqng1a9RenE7oc7-eGUb0l2aEj0IVC0Kb7SDt_EC-NRK-pqj_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به نیروگاه برق پایگاه نداسا در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67578" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67577">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=Kl6pvaPhhJ46I20b8GPFoUAzxbJkaPq_4HRAQAWpdXlti5bs1VC8zSi8uH1wXccFTfbKxt49PpBehb1XPbvQD1gFi05Ak8kOvKTfquX5sQxgyxS2-GEL5hpyCrk4t24Hm1psOO6QgH43-n6Fondb7vU2LFIp8JB0FUDt7-xTVUaGTlMTvXK8Se4hxW1W6Fc0KWm6QA3ByJpLPZQjgMvCJBoyEtdNKFmf6kGjDKb7sveaEAARwC1U3m1GFYhF1s-AfxwNok_5oZoQLiSdJBmiao0-c2dRp_j-H_eFfCsDpcuMd9XB8duQCp6BatkDj_hEbI04iVXnaKq2p6HfbPiVBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=Kl6pvaPhhJ46I20b8GPFoUAzxbJkaPq_4HRAQAWpdXlti5bs1VC8zSi8uH1wXccFTfbKxt49PpBehb1XPbvQD1gFi05Ak8kOvKTfquX5sQxgyxS2-GEL5hpyCrk4t24Hm1psOO6QgH43-n6Fondb7vU2LFIp8JB0FUDt7-xTVUaGTlMTvXK8Se4hxW1W6Fc0KWm6QA3ByJpLPZQjgMvCJBoyEtdNKFmf6kGjDKb7sveaEAARwC1U3m1GFYhF1s-AfxwNok_5oZoQLiSdJBmiao0-c2dRp_j-H_eFfCsDpcuMd9XB8duQCp6BatkDj_hEbI04iVXnaKq2p6HfbPiVBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش سوزی در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67577" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67576">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
گزارش‌های اولیه حاکی از آن است که هدف آن‌ها نیروگاه‌ها است. قطعی برق در چابهار گزارش شده است.
هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67576" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67575">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
انفجار های پی در پی در بوشهر و کیش.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67575" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67574">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مسئول آمریکایی:
حملات به ایران، رادارهای نظامی، پایگاه‌های موشک‌های ضدکشتی و سامانه‌های دفاع هوایی را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67574" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67573">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
❌
گزارش‌های اولیه حاکی از آن است که یک پالایشگاه در جزیره لاوان مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67573" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67572">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRN--RhfWexeGBXlj4X7GX1h9fJGiEeHQ9gktKEEeJBfwIKiBMJkrMFvqLGY5ztgVw22YFQ07c4NA1Ts9tgPfh0z0X8vEkYYPAXHG_mCAjH-CN2QlDN5lW7k7zVWnv4myAkr16xe66ejlw2wJmjlcS4fW3Yb4_G6eFW6b1bCZrKO2nbqjSUuiVAMaxwaC4QtaCWDQNrtEbg_Bc1GnFw-1uj_XFe1zZbeQgXLnATLh2OaKlGMfQJhtzuFtXh_PnNsHdFcc1seXgkyHuHIzswcOG-oSkMlBOPCplSbJrF7L9_uPcvvftCChtCGtDp7UENYSqeiuFWwDbf8nCeYwA2bLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
حملات آمریکا به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67572" target="_blank">📅 23:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67571">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
انفجارها در بوشهر و جزیره خارک
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67571" target="_blank">📅 23:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67570">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67570" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67569">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfrPEHiTZ6YcBpXukMpPWAa-hXRi5m-RIMiEJBX2J1q889bL_IM6E7hhg7_hcyIl5ZV9XYhofNDYQBO4RjeTcJsmi7WUYYLg1oFxiRMrYLbh6tUYvTZLjCGQ4HDjwktnAi7mT0MexGqgJDSPsTFvdrIPdElZJ1JY6JTrjW2UfshukXcY9JcF8KiIv3vNwoQDSmUiRphqyLJPMt6RbEcHUxPmsQFQ4FYuPGGUNoVuJf1Q0R2MtVsbT12KCEYECBykKRl9uDRK0RbREuOmiOJwftgjWmNcXzZw6udeiy-lNoH8D_-OCtoydCIbWsCpR3WQxbzfmcZu2AD6THTUQiKDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، عملیات‌های بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند.
ایالات متحده، ایران را مسئول اقدامات تهاجمی اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67569" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67568">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
صدای چند انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67568" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67567">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مقام آمریکایی:
ارتش آمریکا در حال انجام حملاتی علیه اهداف نظامی ایران در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67567" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67566">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
پادگان ارتش در کنارک توسط آمریکا هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67566" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67565">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره لاوان
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67565" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67564">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=KCa_TL_88otIxMCPb_iU-tz-68ITpi86m6Li-8RgC4DSFqESaRfjiXYAHzbUmu2IsN-SkvmK0ibBBFPu1ydTm3vHeB1-qxlNMKAmJxY13Iz-mobflqey6KubQeXPRioZuZG06SCNM5krkVDKhmPy7D3aFrx1MlezvLphQ7ph5HSM3ixrmcJFncnPrinasHTcURHhoZe5g-qlFZ70yv67wkjvJdftmprR5vVJTQ2mVjrlQZoFirXKihYJdELgtcdTeMXVX8lWeZHfJViqa90u9egp9blECmLyT2JiQjDARVdJPl4LrpU68p7XMwDt8MeyizcJFp48O9xLZwB2oa8jaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=KCa_TL_88otIxMCPb_iU-tz-68ITpi86m6Li-8RgC4DSFqESaRfjiXYAHzbUmu2IsN-SkvmK0ibBBFPu1ydTm3vHeB1-qxlNMKAmJxY13Iz-mobflqey6KubQeXPRioZuZG06SCNM5krkVDKhmPy7D3aFrx1MlezvLphQ7ph5HSM3ixrmcJFncnPrinasHTcURHhoZe5g-qlFZ70yv67wkjvJdftmprR5vVJTQ2mVjrlQZoFirXKihYJdELgtcdTeMXVX8lWeZHfJViqa90u9egp9blECmLyT2JiQjDARVdJPl4LrpU68p7XMwDt8MeyizcJFp48O9xLZwB2oa8jaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات سنگین آمریکا به پایگاه سپاه در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67564" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67563">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به بندر کنارک در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67563" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67562">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
گزارش صدای چند انفجار سنگین در بندر چابهار
به پایگاه امام علی در چابهار حمله شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67562" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67561">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
خبرگزاری آکسیوس :
ارتش آمریکا امشب حملات بسیار سنگین تری رو به ایران انجام خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67561" target="_blank">📅 23:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67559">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aXwz_YOLrFdV35LQJ1iqUOOYFCY1FrmTmM9shMhmZ2JPIwcz4K6x3aeQk_j7mRdJqiH6IHoEUgc-nXwz0zq37u-RNtx81wq8Jy1133QFjqpWvStibCFt_x4o3m9JMFwDWuwZvud0VVz_X2R9-hqjRDxUJ8nDX-M9vugxmKVmbogOIVOWzIuP-YJKi9uBhlCE17S88XYalIMZmQMNEwVwe9wTWmhxrF9aFgfl41KHLFvJqXMC4NaXgCKWYBc5ncNJHxBKpHxZcVyPDCUB-cbDG16Cm_kJhNKs5IoJFjF1AgPAhI-yhfjmTWH6f-WA7wlgmO-os7gpnlJBBsFMkJsk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRG-XdEA13NuXhlukA9xqF9ADYCiHA9FHuBkM_aQplLcJE_grND4T1SWJPdig8-DSVg3rs7tamsgLyypAC-e6DAcd3srAzlQNpRszYfACfe3jThx35499xVdr_AlXIUjZ5x_IYQzmnDSeTHa16SOo8qb-L7vscCiCcC2NaYO6shwcgNPZs16W2FDzDzLw0NlHMxo2oDl3vNV7FoTt6DF5GAi4M6QNTwhXPXrLAdMQqAWKTWvxm-_TEUS06mcp0i7axzIl_O9xIn9dZBX7DCMJ7k1xkESwZOkBOflKwualKLLdX7-4Bq6JHm2Yheg_srZ-6iAewWTS4PPuOjK_PphFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
بلند شدن سوخت رسان ها از تل آویو و امارات به سمت جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67559" target="_blank">📅 23:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67558">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
فعال شدن پدافند در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67558" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67557">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67557" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67556">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67556" target="_blank">📅 23:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67555">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
❌
شنیده شدن صدای انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67555" target="_blank">📅 23:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67554">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c65cdf89e.mp4?token=Q3Wjqwf0mYHfhZixBpu0pUzlwMirRb3k7vM4dWURgZSoseh1NS1kaVkXdQfjhrD0JwsdtRr5Ak-C7F1MPlF2wg-9a_E1Lfp_6zoRdy1vL4XPiWkx_4_J1HXjHU-_e89Uu58f2JXN9pafuFe1IlxwkwLvKKCUaBsfWmrMOHYCBEDaOAk5MAe-DijelEkJiTl_KegE3415WZhyxQgWL5T580BQrur9_beMegGvfOD4yBbBqaV2JK3-BON2odp5PZNkOlAl4eHhqxyZ8mzxsgtEXVIH_1Q9RqbtbOX7Cm37-9WH4Er4pzL9MKjRS0cV_STJVysDcHq7L8923pzKltEV9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c65cdf89e.mp4?token=Q3Wjqwf0mYHfhZixBpu0pUzlwMirRb3k7vM4dWURgZSoseh1NS1kaVkXdQfjhrD0JwsdtRr5Ak-C7F1MPlF2wg-9a_E1Lfp_6zoRdy1vL4XPiWkx_4_J1HXjHU-_e89Uu58f2JXN9pafuFe1IlxwkwLvKKCUaBsfWmrMOHYCBEDaOAk5MAe-DijelEkJiTl_KegE3415WZhyxQgWL5T580BQrur9_beMegGvfOD4yBbBqaV2JK3-BON2odp5PZNkOlAl4eHhqxyZ8mzxsgtEXVIH_1Q9RqbtbOX7Cm37-9WH4Er4pzL9MKjRS0cV_STJVysDcHq7L8923pzKltEV9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
خبرنگار: شما امروز با هگست جلسه دارید.
نخست وزیر نتانیاهو: احتمالاً این اتفاق نخواهد افتاد.
خبرنگار: آیا این شما را ناراحت می‌کند؟
نخست وزیر نتانیاهو: چه کسی گفته ناراحت کننده است؟ شاید معنای دیگری داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67554" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67553">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/176e4f444a.mp4?token=SCqoHwPcV8yItPRHiF7Rp3e992YBog6QhI43H34r7aF5GTH_3J542HpBR-EF-pViflZIGM1-KTSrhC-zeJ15WBpTh5COllteUTnFk-pigjm0ztFB8uiZ6mxEl6sMrZxGoNAnCPAzDzTH44mBZZJNHHifLnbKtCiphRQxpKlpVgWLtnjeMjmigy8l7Xo2oPvCTzXV7pmNVF9o1HZjEJAcMrUGr6PjDJVM23UzNTJc2g3nLq1VRllwOC2BzB3GXoMN114Dc3o4D7kvnkaB8W69W4X6qRWW6NBHqw_Jx2xQx4EzzsynUytNcTSPcnt95PSaTdvVglFYNr1xlACd5cHBBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/176e4f444a.mp4?token=SCqoHwPcV8yItPRHiF7Rp3e992YBog6QhI43H34r7aF5GTH_3J542HpBR-EF-pViflZIGM1-KTSrhC-zeJ15WBpTh5COllteUTnFk-pigjm0ztFB8uiZ6mxEl6sMrZxGoNAnCPAzDzTH44mBZZJNHHifLnbKtCiphRQxpKlpVgWLtnjeMjmigy8l7Xo2oPvCTzXV7pmNVF9o1HZjEJAcMrUGr6PjDJVM23UzNTJc2g3nLq1VRllwOC2BzB3GXoMN114Dc3o4D7kvnkaB8W69W4X6qRWW6NBHqw_Jx2xQx4EzzsynUytNcTSPcnt95PSaTdvVglFYNr1xlACd5cHBBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرنگونی پهپاد MQ-9 آمریکا توسط جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67553" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67552">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697775e593.mp4?token=FId8yRiQQPUrPG4uIuAFaFDqvShmnYrdiODv8HSvjC-vy2oudK3fT7sd_ph1KKfGPjVSlCx9LRAOp9wk0EQag1UPLLgAe2YQ0tqcgzMvhQZpdxX_wMw6DroiozFhTfdCbcIIpacxC_jBbyFA9DwPaz8qduN_Oo4GACxCpWJGqzpFK4j6r2-oNZm_YPzBOM3EPKtSBip-Ef4BfUOHlEgf_hhzfTP_J0dtfB_0q8aafHi5ibzO8_nh9k3g0dgaFPBuhAC_N-Gi5y0zGYukeoIvLEA8N89p2f8g0rAoHzxeDCK84f3LXqqgOTPOyBgfw4BB6XbAMGGSxJuSj4okqAgZiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697775e593.mp4?token=FId8yRiQQPUrPG4uIuAFaFDqvShmnYrdiODv8HSvjC-vy2oudK3fT7sd_ph1KKfGPjVSlCx9LRAOp9wk0EQag1UPLLgAe2YQ0tqcgzMvhQZpdxX_wMw6DroiozFhTfdCbcIIpacxC_jBbyFA9DwPaz8qduN_Oo4GACxCpWJGqzpFK4j6r2-oNZm_YPzBOM3EPKtSBip-Ef4BfUOHlEgf_hhzfTP_J0dtfB_0q8aafHi5ibzO8_nh9k3g0dgaFPBuhAC_N-Gi5y0zGYukeoIvLEA8N89p2f8g0rAoHzxeDCK84f3LXqqgOTPOyBgfw4BB6XbAMGGSxJuSj4okqAgZiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ پس از پایان اجلاس ناتو، ترکیه را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67552" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67551">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd068</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67551" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67550">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DicOS06xY8PJOekOurqvdH9gz-c2pkoAPrA3avjK8hJMg_OuyfBb6luDb00iMYbh55jXMJ2ed78xKAyOPalkCJcl71F1VwT9HtqoUgFeGs1dQb7a6SWO8yAoGaGaHP0HXzeT9rNFv3S0aldiwW1PE1EIbK40MxynFgF-6lwqsXGWn1HRJMQSgGxI2Dlq6BbPHdDqLfT21e7E56U9Ko-QtGX5N0jsseJA8ooYpFvmfHib5XRr0g2Y1HwJWjpU_T3JNlJdfF_kL6ewSZSWtMwgXNd8rF22OyQlgJqhtNVAjVxSF98UIxEGv6P4SSnU38uzIcX01obbxb6tspals3GB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
عراقچی:
صحبت کردن با لحنی تحقیرآمیز با ملت بزرگ و شجاع ایران، از عظمت آن نمی‌کاهد.
ایرانیان به خاطر متانت، فرهنگ و ارزش‌های اخلاقی قوی خود شناخته شده‌اند. ما به بی ادبی با بی ادبی پاسخ نمی‌دهیم، بلکه با عمل: با شجاعت و با از خودگذشتگی فراوان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67550" target="_blank">📅 21:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67549">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
گزارشگر: ماه گذشته، شما گفتید که رهبران ایران بسیار عاقل هستند. حالا شما می‌گویید که آن‌ها افراد بیمار هستند. چه تغییری رخ داده است؟ ترامپ: من آن‌ها را بهتر شناختم. آن‌ها بسیار عاقل‌تر از سطح اول و دوم هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67549" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67548">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/412c846bfe.mp4?token=tGFL9ixvGV6MXX60CWsR3WoytAlssudAj7S2wSEEw2R83iHDj6EAkvWo-kUVU41nr6yyqT_-57KbQ6DcAb0AGsXGz4ohUIrV9CC7cDEEBmzKw-TyniWJSfQ7Eqgu9aAoyZBlW0BuGS2mqrZvftGnZ3UeM317Fqnyy4spOtA9zIrcCgEZ8mPxBGxGXGzKSrU82rUqfQwqUf63QQppO8O-bNjP5OTydnBTIiBf4mmsLMzXijG0QqgaHupQYEhHDYD35z2a4pRZgqe6SqENSxtrqEblDWy1JnrBV4Lpwh9999ulScg-Xt1bEGYZ2oQurnUyag7LHRsj5SDCyIb4c5uT-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/412c846bfe.mp4?token=tGFL9ixvGV6MXX60CWsR3WoytAlssudAj7S2wSEEw2R83iHDj6EAkvWo-kUVU41nr6yyqT_-57KbQ6DcAb0AGsXGz4ohUIrV9CC7cDEEBmzKw-TyniWJSfQ7Eqgu9aAoyZBlW0BuGS2mqrZvftGnZ3UeM317Fqnyy4spOtA9zIrcCgEZ8mPxBGxGXGzKSrU82rUqfQwqUf63QQppO8O-bNjP5OTydnBTIiBf4mmsLMzXijG0QqgaHupQYEhHDYD35z2a4pRZgqe6SqENSxtrqEblDWy1JnrBV4Lpwh9999ulScg-Xt1bEGYZ2oQurnUyag7LHRsj5SDCyIb4c5uT-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ خطاب به ممدباقر درباره اورانیوم:
ما دوربین‌هایی داریم، که بخشی از نیروی فضایی ما هستند، که می‌توانند نشان شناسایی فردی که به یک سایت خاص می‌رود را بخوانند. محمد، چیزی آنجا وجود دارد که با بیل و کلنگ در حال کار هستند.
بیل و کلنگ به شما کمک نمی‌کنند. بزرگترین ماشین‌آلات دنیا هم به شما کمک نمی‌کنند. این موضوع بسیار، بسیار عمیق‌تر است.
اما ما این موضوع را زیر نظر داریم و اگر کسی به آنجا برود، منفجر خواهد شد. بنابراین، هیچ‌کس به آنجا نزدیک نخواهد شد. در نهایت، ما آن را تصاحب خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67548" target="_blank">📅 20:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67547">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8dc7e8bc.mp4?token=XVwssvTXM4Rd2JeeHGhz4u1lDt3joDuoPqmMtvI7-GtC--L-zG0R6aohkfHenGczB_wedJLQZO6N8Vb17PFqXLox0ZiFx3NxPbxvlEO_Qn6NVwzNhMk2nQdPPhg8IOqyJWpZJV4nrS0suDuZ3T2S1blfiQROtpCNpmI5Vyfhx_8dkMHWTEaMdji7ZOrBDwyckOIqZTQXdvn2pc56MUiGSD1BjjiiV89N3XtY3NqlxhbzC8Ba3AGtvToTqtzT93z5ZxNqEUN3ys9rEYvYDvgFjNpuokj4ydMyM-quE2s3_5IkX0JDyUvxXH3M7JwX6-1gsWiq2te-JdSaOUJrvIWaWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8dc7e8bc.mp4?token=XVwssvTXM4Rd2JeeHGhz4u1lDt3joDuoPqmMtvI7-GtC--L-zG0R6aohkfHenGczB_wedJLQZO6N8Vb17PFqXLox0ZiFx3NxPbxvlEO_Qn6NVwzNhMk2nQdPPhg8IOqyJWpZJV4nrS0suDuZ3T2S1blfiQROtpCNpmI5Vyfhx_8dkMHWTEaMdji7ZOrBDwyckOIqZTQXdvn2pc56MUiGSD1BjjiiV89N3XtY3NqlxhbzC8Ba3AGtvToTqtzT93z5ZxNqEUN3ys9rEYvYDvgFjNpuokj4ydMyM-quE2s3_5IkX0JDyUvxXH3M7JwX6-1gsWiq2te-JdSaOUJrvIWaWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
مطمئن نیستم که بخواهم با آنها به توافقی برسم.
ما می‌توانیم بازی‌ها را انجام دهیم، اما مطمئن نیستم که بخواهم به توافقی برسم.
فقط بیایید این کار را به پایان برسانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67547" target="_blank">📅 20:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67546">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d009a331.mp4?token=vxjcvb6W2PABM4EqQpqTQDBKxSXELA0prniydxl9fUEYdVlzeoghLJpqQ0JE6828AgEUbi6kbC-TC32lZcbA5khSmZlRGfugscD6NhHyEbpwZrp4sAuH6UVASant0sLZm6r5c2l4cgmGkajQFSdnXH3024sW1e00uja2vNoG8jN1bb6LlYws4dEwo7J2n5oJoPxn-XAvoB7OMYxP0Q-xrEKY77Z9JXcQakuCqN57rTX4L9wQCl2Bso4ckkDX1pEQtqk01Fe-QmWyAsXuv0tJ6Im7qxReSkjtkt6tJWEChmaUiCe5BDFfLa4MvoaGfUbk4fcwyM3y4ZHWnEixM7dszw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d009a331.mp4?token=vxjcvb6W2PABM4EqQpqTQDBKxSXELA0prniydxl9fUEYdVlzeoghLJpqQ0JE6828AgEUbi6kbC-TC32lZcbA5khSmZlRGfugscD6NhHyEbpwZrp4sAuH6UVASant0sLZm6r5c2l4cgmGkajQFSdnXH3024sW1e00uja2vNoG8jN1bb6LlYws4dEwo7J2n5oJoPxn-XAvoB7OMYxP0Q-xrEKY77Z9JXcQakuCqN57rTX4L9wQCl2Bso4ckkDX1pEQtqk01Fe-QmWyAsXuv0tJ6Im7qxReSkjtkt6tJWEChmaUiCe5BDFfLa4MvoaGfUbk4fcwyM3y4ZHWnEixM7dszw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
املاکی درباره ایران:
به نظر من، جنگ با ایران دوباره آغاز نخواهد شد. وقتی آنها حمله می‌کنند، ما ۱۰ برابر قوی‌تر پاسخ می‌دهیم.
شاید امشب به آنها حمله کنیم.
هر اتفاقی که قرار است بیفتد، خیلی سریع رخ خواهد داد.
ما به دنبال یک راه حل بلندمدت نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67546" target="_blank">📅 20:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67545">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
من می‌خواهم این موضوع را در مورد ایران به پایان برسانم و با رهبران فعلی بازی نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67545" target="_blank">📅 20:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67544">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966c88b1c6.mp4?token=ZkOOci7GFdWKbbbIdTEc99KQVOOuHuVDF4dieWL2mgyfiKZoDV4SdEP_VwU74lg1a3b3HZJybf-pegLI-mC_0jwpfgKTufpJRfj73Si7gJu4Z4EI7088DSxSprXdAoNed5OJBnYYJUulqLXKzRPAf1WCCj8swA3OAFGoF7N1yFfL6DpPYMCMquIoEIdNfMqOtNTdl3g-ogd5YeZbsxQQo6KeeQ7ukC0e7ea1CFwe1HuvskIqnHJNNHqmf1H13-P_f4TjjO-mQaDulOKCCsLvhufpgnhJxgPePye6vs3VjZ6zRsY8EGyUgZuZORxXzw13bNuXAps04P7fefnA8TOCgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966c88b1c6.mp4?token=ZkOOci7GFdWKbbbIdTEc99KQVOOuHuVDF4dieWL2mgyfiKZoDV4SdEP_VwU74lg1a3b3HZJybf-pegLI-mC_0jwpfgKTufpJRfj73Si7gJu4Z4EI7088DSxSprXdAoNed5OJBnYYJUulqLXKzRPAf1WCCj8swA3OAFGoF7N1yFfL6DpPYMCMquIoEIdNfMqOtNTdl3g-ogd5YeZbsxQQo6KeeQ7ukC0e7ea1CFwe1HuvskIqnHJNNHqmf1H13-P_f4TjjO-mQaDulOKCCsLvhufpgnhJxgPePye6vs3VjZ6zRsY8EGyUgZuZORxXzw13bNuXAps04P7fefnA8TOCgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
هر اتفاقی که قرار است بیفتد، به سرعت رخ خواهد داد.
ما به دنبال راهکارهای بلندمدت نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67544" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67543">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce02ad2ec.mp4?token=sqkdtPTufZacBFAriQNqLC420DBg9Nl17pcxZFSmKD9V8VEXLYHybbQVA8gYNGFHt-X5d5_vYhHZpIzv92sf44DX9WnbO2LlY5IC2eS3G5GhGDZETpsIdCYD1ysgOv3gJYlB1aAO-ZIxUlg2ZrsPdjB8_FxnLsVWZhCD5xSCfnSlGA8PU3hGZvlf2uHl65KEHv4lra_iaEqPnI62Of2-HfOfM0pn8IlIBtWJV-euNJhtb6OaH7ourrq6wYyylpljbwoi7uJOrYoe5OCFenpHBR4VZgrDbZ8QNFjJhqJOnIDpuRyEGVdsKUEmN-PVtTIEqAbZzwHqkW8tEM-U9Gfk-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce02ad2ec.mp4?token=sqkdtPTufZacBFAriQNqLC420DBg9Nl17pcxZFSmKD9V8VEXLYHybbQVA8gYNGFHt-X5d5_vYhHZpIzv92sf44DX9WnbO2LlY5IC2eS3G5GhGDZETpsIdCYD1ysgOv3gJYlB1aAO-ZIxUlg2ZrsPdjB8_FxnLsVWZhCD5xSCfnSlGA8PU3hGZvlf2uHl65KEHv4lra_iaEqPnI62Of2-HfOfM0pn8IlIBtWJV-euNJhtb6OaH7ourrq6wYyylpljbwoi7uJOrYoe5OCFenpHBR4VZgrDbZ8QNFjJhqJOnIDpuRyEGVdsKUEmN-PVtTIEqAbZzwHqkW8tEM-U9Gfk-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
گزارشگر: ماه گذشته، شما گفتید که رهبران ایران بسیار عاقل هستند. حالا شما می‌گویید که آن‌ها افراد بیمار هستند. چه تغییری رخ داده است؟
ترامپ: من آن‌ها را بهتر شناختم. آن‌ها بسیار عاقل‌تر از سطح اول و دوم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67543" target="_blank">📅 20:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67542">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6daa8309.mp4?token=SVVfLlLznv2Y8z9vcW80VrwF3p0nBgQlmZ7YVXj9NlhnkJw5f22MWFNG2ne9sYCfIjKTSGmxUPJSPuAIkpjy7gRFHIH3R5vsz2rzmZ8m9Kp-199e34EtxqyCShq4D6S-3fWNvcFOGxPH4C9A9Cdx6ynK8whV-aKOH3aKmvAx6eJ22V2r1SqFcFEzp6ydPZlAPIhy1Kdm8MplnFg7ZqytkyZpxyHzTjkDGXe5lnnnHABMKtGgF7DpVJgbV0czVTcqBgqycHAN6vCVnxWkLmGwyqawHf8WEBEIsLP26hbXxZdB-xiOALfhsJ4IW8xAeKSDSLgXSlhp44LeDM2de4V5-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6daa8309.mp4?token=SVVfLlLznv2Y8z9vcW80VrwF3p0nBgQlmZ7YVXj9NlhnkJw5f22MWFNG2ne9sYCfIjKTSGmxUPJSPuAIkpjy7gRFHIH3R5vsz2rzmZ8m9Kp-199e34EtxqyCShq4D6S-3fWNvcFOGxPH4C9A9Cdx6ynK8whV-aKOH3aKmvAx6eJ22V2r1SqFcFEzp6ydPZlAPIhy1Kdm8MplnFg7ZqytkyZpxyHzTjkDGXe5lnnnHABMKtGgF7DpVJgbV0czVTcqBgqycHAN6vCVnxWkLmGwyqawHf8WEBEIsLP26hbXxZdB-xiOALfhsJ4IW8xAeKSDSLgXSlhp44LeDM2de4V5-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
می‌دانید؟ ممکن است من هم دیگر نباشم.
من هدف شماره یک آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67542" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67541">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0540439bf4.mp4?token=ATsR_jDarvE1JfIJaW5mqjJqrQviK5cnTJcKPviDwwvBVZrCojZnIZ9FGa0pOqCOJOZWBof0rQii27bKeEpQZ-Obf7VJPLy-N1JIWEt2AItskw1lvozVvMke-dVRf3UnLHvDZ3U--Cz1SJr6Vu40eO9KgO5RRSs9ds4EaEdUcW-x3d6BxApqRjNn1EoFmWBDbwcSgL4Eg7XgKH0R8OxVc-OvkzOgyfkekzvoSZlOFtr9Wx8O0gxHSnTvsNuzq6mJfWJQDXDb9FrIjuLxMR5u18QL5e02rvTZwr4JdxGz5uefeURePxpuomChK5-sZhUhgavKHaTLGou0YXVOqoMi-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0540439bf4.mp4?token=ATsR_jDarvE1JfIJaW5mqjJqrQviK5cnTJcKPviDwwvBVZrCojZnIZ9FGa0pOqCOJOZWBof0rQii27bKeEpQZ-Obf7VJPLy-N1JIWEt2AItskw1lvozVvMke-dVRf3UnLHvDZ3U--Cz1SJr6Vu40eO9KgO5RRSs9ds4EaEdUcW-x3d6BxApqRjNn1EoFmWBDbwcSgL4Eg7XgKH0R8OxVc-OvkzOgyfkekzvoSZlOFtr9Wx8O0gxHSnTvsNuzq6mJfWJQDXDb9FrIjuLxMR5u18QL5e02rvTZwr4JdxGz5uefeURePxpuomChK5-sZhUhgavKHaTLGou0YXVOqoMi-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ایران می‌خواهد به توافقی برسد، اما نمی‌داند چگونه باید به توافق برسد.
و سپس، شب‌ها به کشتی‌ها حمله می‌کنند. من این کار را دوست ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67541" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67540">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff03b3210e.mp4?token=qfJIjTfupo0izLVTlx-8zB5DgJRPVke_5DbyLJ8jk1N4p4HeArBGG7Zv_62t1euD0WKw9Lff-PM3PPpHxPyD97Bdr2cG_ISAyinxGN05qyCAVJuJ7rGxQlsI26z0xS45tu7D7Xq3_Ni3Pa-ABeJza5PcpkJO5nQTGDkklSdL2RFEw6qCwQ5QObDJQerfHOFXOzLoVz5vt8LTSQeuUqrw__VfTlwbHHeeVOUcch6K1XXLCNswZcmjcn8VtLEPFnUpXJ_6VSY1wJQ70kwlfOMe25q18qQi-mALvOiwjUjwhW4H0shaOwRNpVJ1lYPDoIIPZDG20vhmKG7sJELDhE2GKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff03b3210e.mp4?token=qfJIjTfupo0izLVTlx-8zB5DgJRPVke_5DbyLJ8jk1N4p4HeArBGG7Zv_62t1euD0WKw9Lff-PM3PPpHxPyD97Bdr2cG_ISAyinxGN05qyCAVJuJ7rGxQlsI26z0xS45tu7D7Xq3_Ni3Pa-ABeJza5PcpkJO5nQTGDkklSdL2RFEw6qCwQ5QObDJQerfHOFXOzLoVz5vt8LTSQeuUqrw__VfTlwbHHeeVOUcch6K1XXLCNswZcmjcn8VtLEPFnUpXJ_6VSY1wJQ70kwlfOMe25q18qQi-mALvOiwjUjwhW4H0shaOwRNpVJ1lYPDoIIPZDG20vhmKG7sJELDhE2GKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز، بیش از 20 فروند از ناوهای جنگی نیروی دریایی ایالات متحده در حال گشت‌زنی در آب‌های سراسر خاورمیانه هستند، در حالی که نیروهای سنتکام به ترویج امنیت و ثبات منطقه‌ای ادامه می‌دهند. ماه گذشته، ناوها و هواپیماهای نیروی دریایی آمریکا به صورت منظم در دریای عرب حرکت کردند و قدرت نظامی و توان آتش بی‌نظیر آمریکا را به نمایش گذاشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67540" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67538">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
ویدیو ای که سپاه از حملات دیشبش به پایگاه های آمریکا در منطقه منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67538" target="_blank">📅 19:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67537">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735f956d53.mp4?token=Lshdof5khJVfSvMVv1VdIi0yEN9hOsWNJl1lFGF_lgpDh1hlXl7ZDdHQ8Nq-h7p7g4pfcOaBFzWjjqi_hy5HBPrzNyttjnoeJf3_hYRlIPMkcZyY4ERY1f3cHB3trqkQcG6qnt10Qp1kX84a_FnFw0CVJwcrKx-5Ju17lnddJ1Uzh5UIkLfNSESM7KN-jW0NKkzmgWnjKpnU99vXa34UbSMCbF1ZjQLx4hxbHTqS5ZQCfKOQZwq0qOhcnGpBkkyG30U428bzEYGHds6AzePMMM9wO9b94RSEX2YOkkS1IZ7aAvuccs7bo1C2C7zeF8e38bIsV8Wsav6O3TdWrECcMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735f956d53.mp4?token=Lshdof5khJVfSvMVv1VdIi0yEN9hOsWNJl1lFGF_lgpDh1hlXl7ZDdHQ8Nq-h7p7g4pfcOaBFzWjjqi_hy5HBPrzNyttjnoeJf3_hYRlIPMkcZyY4ERY1f3cHB3trqkQcG6qnt10Qp1kX84a_FnFw0CVJwcrKx-5Ju17lnddJ1Uzh5UIkLfNSESM7KN-jW0NKkzmgWnjKpnU99vXa34UbSMCbF1ZjQLx4hxbHTqS5ZQCfKOQZwq0qOhcnGpBkkyG30U428bzEYGHds6AzePMMM9wO9b94RSEX2YOkkS1IZ7aAvuccs7bo1C2C7zeF8e38bIsV8Wsav6O3TdWrECcMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
صدا و سیما و رسانه خامنه ای برای اولین بار فیلمی از حسینیه امام خمینی در بیت رهبری جایی که رهبر جمهوری اسلامی مورد هدف قرار گرفت را منتشر کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67537" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67536">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
یدیوت احرونوت:
نخست‌وزیر اسرائیل، نتانیاهو، و وزیر دفاع، کاتز، حضور خود را در یک رویداد لغو کرده‌اند و در حال بحث و بررسی مسائل امنیتی مرتبط با تحولات مربوط به ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67536" target="_blank">📅 18:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67535">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a14b7982.mp4?token=RGl8Rmu7u2hp6gkmd68Zf3ChfIzVgOcLtx2TYO_1b0zkskze7tG-Pl6-leQ9B-yIYCmt2g08q4X1MIFMgm5Kad0r-iJ8Zn4UhHGyptyfqvT5mP1G8sE_T4vHA6s9IZnW_4eLo0jzeYVnsmYB_MSC5seLQaZH6tVw6ZN60H47kc0KQniICIXkq28Xjc9frMJwcR7EOLiKboVC_is7_AZzKyCFFxG2EsFB9Ca0bNzReliQzz4ieXeaI6JzxmL7HivS5IEkZNWNbOju7ORBUWkj8qyr3k3GTGsmGd11Br4RppQExKZJiyzrAy0ByKQC5a5cR41a-k6jDYb_k_ElpNegYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a14b7982.mp4?token=RGl8Rmu7u2hp6gkmd68Zf3ChfIzVgOcLtx2TYO_1b0zkskze7tG-Pl6-leQ9B-yIYCmt2g08q4X1MIFMgm5Kad0r-iJ8Zn4UhHGyptyfqvT5mP1G8sE_T4vHA6s9IZnW_4eLo0jzeYVnsmYB_MSC5seLQaZH6tVw6ZN60H47kc0KQniICIXkq28Xjc9frMJwcR7EOLiKboVC_is7_AZzKyCFFxG2EsFB9Ca0bNzReliQzz4ieXeaI6JzxmL7HivS5IEkZNWNbOju7ORBUWkj8qyr3k3GTGsmGd11Br4RppQExKZJiyzrAy0ByKQC5a5cR41a-k6jDYb_k_ElpNegYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا برنامه‌ای برای اعزام نیروی زمینی به ایران ندارید؟
ترامپ: چرا باید الان وارد عمل شوم؟ من زمانی وارد عمل خواهم شد که آن‌ها کاملاً از بین بروند یا به یک توافق برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67535" target="_blank">📅 18:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67534">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2479db8c8d.mp4?token=b5NUGUFcwknfXWKcs04FgsSuep_LpSezJIU4y2xapqf4OuIfE5y9FI09cyLA0PkKIWuLmczxUS8nuQp_fsvEMM0fdbDpM6pU6RNFj2wdmRcQK-JZsxtMnDdSdNQv-U-Bmgrm8nm23zojB0BAHkfCh9FFyOvW1WvAaB4kXPr_q742RGJZKRk9K64r4jd-dNSWDkzVxMoKrNJwwWY-PZ4qr-2nHaXFtq-Y3TfSSy_Bqz6xWjoKKClZ2Z_SjIAHEGpx1ggHUDTd1nYFB4_8d6JWaMIhQ9OTHWc-lmyvIGp8Xf66632CzJRD4KKIpK6G6yL2_EfcjXYSDHa9zM10AdeTWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2479db8c8d.mp4?token=b5NUGUFcwknfXWKcs04FgsSuep_LpSezJIU4y2xapqf4OuIfE5y9FI09cyLA0PkKIWuLmczxUS8nuQp_fsvEMM0fdbDpM6pU6RNFj2wdmRcQK-JZsxtMnDdSdNQv-U-Bmgrm8nm23zojB0BAHkfCh9FFyOvW1WvAaB4kXPr_q742RGJZKRk9K64r4jd-dNSWDkzVxMoKrNJwwWY-PZ4qr-2nHaXFtq-Y3TfSSy_Bqz6xWjoKKClZ2Z_SjIAHEGpx1ggHUDTd1nYFB4_8d6JWaMIhQ9OTHWc-lmyvIGp8Xf66632CzJRD4KKIpK6G6yL2_EfcjXYSDHa9zM10AdeTWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
هر زمان که ما به ایران حمله کنیم، قیمت نفت کمی افزایش می‌یابد.مشکلی نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67534" target="_blank">📅 18:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67533">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f85ab468.mp4?token=Hp-e8uze6Hk2BHakwRlAgXVWCtFqRoxF9PdIMo1-qBEd6JFjb7yXrSFVDZF5jce1BcJnKYS1itU8OknuihjCvts_aC1OgpVtpw4v1IR8fvvUJwLpZb5gttuMQ_6-ZbOWr2gvteQxLfGMcalVQjADHWO6kqpUNMoYRiIfgU346aAAOboh9r1MdxDVNBMQgIO4oMM1uCrmBzWAic1DwOjruQ8Or88aGZSK79tl3eRmQ8d4zwprDIlbLixuUTyRCeVOoHnMsi39f4iKYIjNwlJrkLOn8cGgigIDK3inqj22F9ZeHtLNkz-VZkK8medf2raybGjoEpHFg-jMGnQrO9nK5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f85ab468.mp4?token=Hp-e8uze6Hk2BHakwRlAgXVWCtFqRoxF9PdIMo1-qBEd6JFjb7yXrSFVDZF5jce1BcJnKYS1itU8OknuihjCvts_aC1OgpVtpw4v1IR8fvvUJwLpZb5gttuMQ_6-ZbOWr2gvteQxLfGMcalVQjADHWO6kqpUNMoYRiIfgU346aAAOboh9r1MdxDVNBMQgIO4oMM1uCrmBzWAic1DwOjruQ8Or88aGZSK79tl3eRmQ8d4zwprDIlbLixuUTyRCeVOoHnMsi39f4iKYIjNwlJrkLOn8cGgigIDK3inqj22F9ZeHtLNkz-VZkK8medf2raybGjoEpHFg-jMGnQrO9nK5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره اورانیوم های غنی شده:
این مواد تا این حد در زیر زمین قرار دارند که هیچ‌کس به جز ما نمی‌تواند به آن‌ها دسترسی پیدا کند، زیرا ما تجهیزات لازم را داریم.
این مواد در اعماق زیر یک کوه قرار دارند و اکنون مشخص شده است که برای دسترسی به آن‌ها، به ماشین‌آلات بسیار بزرگ نیاز است که ما در اختیار داریم و هیچ کشور دیگری این تجهیزات را ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67533" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67532">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=KdSBRMk7bTP-uXoR6dxGAC-fnNpVZ3mVgnLJRNuT1rF1R6SZT9d95wH7-WKJPUrfFCsH8tuxZq-qF1iPxNN_l-cpNM5qY7p7pG0pxD9OWbGWCkADjxAh12E8O6d0wMUHKOUL0YBNbUwV-AzwYwyt2si3dwRfaFukqcz_0qacl4XJaI17PTQXWTU3pA8xLRQA4IUYNj2MJJGsSJ9mSCg32Ve7TkpNn60IPcYXJ_2jAJpvpFwOLqws2gLEGdxx2VqRG7oCsK564xpf08lM-IK8OACPNbtPUi6um8RTZISU4FrfW4S5OahT3--anCvsjKq7bwr8BEgd7e2p7LlwvAnc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=KdSBRMk7bTP-uXoR6dxGAC-fnNpVZ3mVgnLJRNuT1rF1R6SZT9d95wH7-WKJPUrfFCsH8tuxZq-qF1iPxNN_l-cpNM5qY7p7pG0pxD9OWbGWCkADjxAh12E8O6d0wMUHKOUL0YBNbUwV-AzwYwyt2si3dwRfaFukqcz_0qacl4XJaI17PTQXWTU3pA8xLRQA4IUYNj2MJJGsSJ9mSCg32Ve7TkpNn60IPcYXJ_2jAJpvpFwOLqws2gLEGdxx2VqRG7oCsK564xpf08lM-IK8OACPNbtPUi6um8RTZISU4FrfW4S5OahT3--anCvsjKq7bwr8BEgd7e2p7LlwvAnc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:   «امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»  @News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67532" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67531">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=pbH0O1IPTK4HWkN7RaoSGZzp2EgsADI43FmE74dIZg3gAF2Ht8T6ZjdahmG_UBuplq3cVrroCYO6PMPLcmugIOBPiwyVfmXrQ_LURSnoLtlnTBEFSN8MQi78czYeKsuQGaf2V-8eatXvYpPdUZvJGzQmUN6KIPDUz2BypUP2Y1-uP9G7y1V68GSu1GKnpVqsAeoLXm1DIzs4VRVkJninoZk8_Ln4MGjqtQn8glWkBNKbY_pXS8U3kXToB-6rmO23_oPMTAxW0tmY2GVJr9bmlDytpbNeQ7Tj7LygOCtg3Y2gKPPSMvQkBqqCPYSuvHa2xTa9qtNBdU-JSNIRtsTPTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=pbH0O1IPTK4HWkN7RaoSGZzp2EgsADI43FmE74dIZg3gAF2Ht8T6ZjdahmG_UBuplq3cVrroCYO6PMPLcmugIOBPiwyVfmXrQ_LURSnoLtlnTBEFSN8MQi78czYeKsuQGaf2V-8eatXvYpPdUZvJGzQmUN6KIPDUz2BypUP2Y1-uP9G7y1V68GSu1GKnpVqsAeoLXm1DIzs4VRVkJninoZk8_Ln4MGjqtQn8glWkBNKbY_pXS8U3kXToB-6rmO23_oPMTAxW0tmY2GVJr9bmlDytpbNeQ7Tj7LygOCtg3Y2gKPPSMvQkBqqCPYSuvHa2xTa9qtNBdU-JSNIRtsTPTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:
«امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67531" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67530">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛ ترامپ:
به ایران هشدار میدم، دیشب ضربات سختی رو بهشون زدیم، اما امشب قراره براشون سخت‌تر باشه و حسابی بهشون حمله میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67530" target="_blank">📅 17:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67529">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=lKW5l4jx1AeuKijz-6cj-VCMqmUHuAYscW6r6lqfwBtwef-os5NuY7sxX1H0V2R85mxVGAWyh5wvoK6lreu2pdkQiNPX8cTfvbsNJvIkVWcmZqW8QSAfI7pmdfZzVJxLhoMfwdxR3lXDekA6nhw-zcTnqqKeLZhzyrBr7cDCdw9y2gb2wBz1bmL2TsQEwmq1jb1ABY1b99m4vTlOpMIgURyOAPMkTFv9hW_LE6w5YmMI5wxxcdIkYHPo8NWuKSHFNAwSfHBYui0pRR9-xXHXdCu_USqby7lqaGXtaueoF3zW4chk5Pu8VR6QrewLrF6zHmjlmY6NbrKZM5Wn-g0lkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=lKW5l4jx1AeuKijz-6cj-VCMqmUHuAYscW6r6lqfwBtwef-os5NuY7sxX1H0V2R85mxVGAWyh5wvoK6lreu2pdkQiNPX8cTfvbsNJvIkVWcmZqW8QSAfI7pmdfZzVJxLhoMfwdxR3lXDekA6nhw-zcTnqqKeLZhzyrBr7cDCdw9y2gb2wBz1bmL2TsQEwmq1jb1ABY1b99m4vTlOpMIgURyOAPMkTFv9hW_LE6w5YmMI5wxxcdIkYHPo8NWuKSHFNAwSfHBYui0pRR9-xXHXdCu_USqby7lqaGXtaueoF3zW4chk5Pu8VR6QrewLrF6zHmjlmY6NbrKZM5Wn-g0lkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
آنها توافق کردند که هرگز سلاح هسته‌ای نخواهند داشت.
و سپس، آنها به بیرون می‌روند و می‌گویند که ما هرگز درباره این موضوع بحث نکردیم.
چه کسی باور خواهد کرد؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67529" target="_blank">📅 17:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67528">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=TcM2Ns-vPHDWzf59zyZQkg-k3RkKEOhqQgBJRw7rg6HC8O1bc4mpuzRxXfGySAQTPQCMWKppCJd59bRi0BxN3-RVlmw7pc9XAdyiycMH99_SRb2jgqcWjAgxLjREnbHoRrDnGC6EAdolizF4tHsnjUfWtkl1OtHF505MAuBX9hxulTn0H70vv_y39fuh-rnCKWeqUb_UDNSx0tgcfMv3SeVY8Lg17WIP9qJ3avR1Jb8SyGe3M3oigGaq7LlsI2IJiPY9yxdJbjfktLcmcED1ihDWfkKb0Ls9WZanTg88c26wxQsQJbiidOwITWFi_3CnVF-RQZg27VABjojVAjhbDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=TcM2Ns-vPHDWzf59zyZQkg-k3RkKEOhqQgBJRw7rg6HC8O1bc4mpuzRxXfGySAQTPQCMWKppCJd59bRi0BxN3-RVlmw7pc9XAdyiycMH99_SRb2jgqcWjAgxLjREnbHoRrDnGC6EAdolizF4tHsnjUfWtkl1OtHF505MAuBX9hxulTn0H70vv_y39fuh-rnCKWeqUb_UDNSx0tgcfMv3SeVY8Lg17WIP9qJ3avR1Jb8SyGe3M3oigGaq7LlsI2IJiPY9yxdJbjfktLcmcED1ihDWfkKb0Ls9WZanTg88c26wxQsQJbiidOwITWFi_3CnVF-RQZg27VABjojVAjhbDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
جمهوری اسلامی ژاپن دیشب به ناو هواپیمابر ما حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67528" target="_blank">📅 17:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67527">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=mthyQ2ZqYvBKY0SwmIG97xopG-amTHedeU5H4r4wzuZ5hfNtJfz6sXOoTp8WcwODBEz1H9K5xw2JI0axJ_qTs1rqEQH0h8y5s4UGmXJhETao3IWdbfxYCGZW4Y4KKP6PZPE08Ou9Gmcb6VKQU0te6U0FVEX4SW7a1uwAS6EqcgLH_Z0aLUAKKGDqkDD5VGYkvA4qTwx1jl227i-aUlwKFT_LBWVAKrS2O8gDgkpH9DI9LcO8FNBgZpZsvPFbyfKPmzt5RCA9aiNAGlc1Kppou9cyC0gjWFHc4aoj46b0xlGd55vgRBi1Z1vINsmyHqF1PfxeSsGRvFtB_RIrbYsCSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=mthyQ2ZqYvBKY0SwmIG97xopG-amTHedeU5H4r4wzuZ5hfNtJfz6sXOoTp8WcwODBEz1H9K5xw2JI0axJ_qTs1rqEQH0h8y5s4UGmXJhETao3IWdbfxYCGZW4Y4KKP6PZPE08Ou9Gmcb6VKQU0te6U0FVEX4SW7a1uwAS6EqcgLH_Z0aLUAKKGDqkDD5VGYkvA4qTwx1jl227i-aUlwKFT_LBWVAKrS2O8gDgkpH9DI9LcO8FNBgZpZsvPFbyfKPmzt5RCA9aiNAGlc1Kppou9cyC0gjWFHc4aoj46b0xlGd55vgRBi1Z1vINsmyHqF1PfxeSsGRvFtB_RIrbYsCSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ممکن است محاصره را دوباره اعمال کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67527" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67526">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e08b208584.mp4?token=UoUHmt2veR1nvA-31qKxo60y8HhAm9eq_Q5Q5crIa4XrqXKDuKrbqfv4HW3yvQQSWNrc_2stiOXwPuresdCij_oaVaI3cal3gwnkhTi4yXLjG9ioXsNFvX2CG1XAYMkcUlf2oL_vvUDvxZQcVDi-m6YnE091Sg8STRVwNUhJ-YhPLCrLQieXq6oxF-YkRgYQxjjDsAO6jU7doWeLXv-pgD-dbLohrYdHSgwZsAK6RpIIefqmRZyN27HThsgMdM5LtQYjuFpFyBqvACOOwkqQ0jVX3XzbWEDRgfEHx3zdFx1c5Sn4Rkk9k1nrey7ptE7t44C53kx39CKVqa2u2A1xYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e08b208584.mp4?token=UoUHmt2veR1nvA-31qKxo60y8HhAm9eq_Q5Q5crIa4XrqXKDuKrbqfv4HW3yvQQSWNrc_2stiOXwPuresdCij_oaVaI3cal3gwnkhTi4yXLjG9ioXsNFvX2CG1XAYMkcUlf2oL_vvUDvxZQcVDi-m6YnE091Sg8STRVwNUhJ-YhPLCrLQieXq6oxF-YkRgYQxjjDsAO6jU7doWeLXv-pgD-dbLohrYdHSgwZsAK6RpIIefqmRZyN27HThsgMdM5LtQYjuFpFyBqvACOOwkqQ0jVX3XzbWEDRgfEHx3zdFx1c5Sn4Rkk9k1nrey7ptE7t44C53kx39CKVqa2u2A1xYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
آنها به ما گفتند: لطفا در مراسم خاکسپاری ما را نکشید. من گفتم که این کار را نخواهم کرد، و ما هیچ اقدامی انجام ندادیم.
و سپس آنها به سه کشتی حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67526" target="_blank">📅 17:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67525">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=Z1NBO5aZshgpyO5gthrcd8fUEtmyfjynB4PC-wVtbeVtK_ZN-ih6dzt1OJHH6F14FUSX-QSsdD5owJU6egG6QrPcrQhya4lT-onKceK7myBJy6A1IDzbQuvepRUFRgl6z06AHxDYsFOA_EQJbmFza-TSvhi0dsTihABfNj3piHS6Y4bxx1_wUlql9RFNKcwxTR7NwHtur6QB0cOH6EEtTLuejtNmWv2FOvWoCx5zdoqXVKxazaOpwpQfBd3gWurBtoiJ1xxf5oX0MeR4WW663zHSJEXEI_rhwRB_Zi6UBI3Uq1VgrCBLnf_KSoZ_yxR1QhF1P-4oHxOpMvPtjI1RTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=Z1NBO5aZshgpyO5gthrcd8fUEtmyfjynB4PC-wVtbeVtK_ZN-ih6dzt1OJHH6F14FUSX-QSsdD5owJU6egG6QrPcrQhya4lT-onKceK7myBJy6A1IDzbQuvepRUFRgl6z06AHxDYsFOA_EQJbmFza-TSvhi0dsTihABfNj3piHS6Y4bxx1_wUlql9RFNKcwxTR7NwHtur6QB0cOH6EEtTLuejtNmWv2FOvWoCx5zdoqXVKxazaOpwpQfBd3gWurBtoiJ1xxf5oX0MeR4WW663zHSJEXEI_rhwRB_Zi6UBI3Uq1VgrCBLnf_KSoZ_yxR1QhF1P-4oHxOpMvPtjI1RTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما شب گذشته به جزیره خارک حمله کردیم.
ممکن است کنترل جزیره خارک را به دست بگیریم. هیچ کاری در این مورد نمی‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67525" target="_blank">📅 17:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67524">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=NJ8kUfJolKLI4brkmkFW7pFE_XcDBI5IWQxl3GXfUh_isnudGLRwu9fdohOhXEdeD2rTmpaG7x-7wzmtDk9mpcq8Kab5RTvDeXqI2vfIlIQwmb7gojA6RFBjxgOWzs7GY6Ufz22FqBpkG8G8EXzicd42m222gI29ZTdPXQAVK1dzdRdYJqvHQvXu_3admmSwlLqVapsHAz-vq3a583ES8lPjKUnS71V8nrI591TeWnXc4GzJIJHrK9rwSaeJmrasWNCpxF_jJuIMtKWNGH5rHoknrcNAVK6Hi-PjH7oHDj7T6EDcHCufvZAwQeyDAl5RmO4prj7V50MzihATDS1i5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=NJ8kUfJolKLI4brkmkFW7pFE_XcDBI5IWQxl3GXfUh_isnudGLRwu9fdohOhXEdeD2rTmpaG7x-7wzmtDk9mpcq8Kab5RTvDeXqI2vfIlIQwmb7gojA6RFBjxgOWzs7GY6Ufz22FqBpkG8G8EXzicd42m222gI29ZTdPXQAVK1dzdRdYJqvHQvXu_3admmSwlLqVapsHAz-vq3a583ES8lPjKUnS71V8nrI591TeWnXc4GzJIJHrK9rwSaeJmrasWNCpxF_jJuIMtKWNGH5rHoknrcNAVK6Hi-PjH7oHDj7T6EDcHCufvZAwQeyDAl5RmO4prj7V50MzihATDS1i5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گزارشگر: آیا امشب قصد دارید قایق‌های بیشتری از ایران را هدف قرار بدید؟
🔴
ترامپ: معمولاً این موضوع را با شما در میان نمی‌گذارم، اما می‌دانید؟ آن‌ها هیچ کاری نمی‌توانند در این مورد انجام دهند، بنابراین احتمالاً بله.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67524" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67523">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f96f01d100.mp4?token=TJ99zpNrynQwl5zG1bBSBoAIDp4m_zM8u-9yJHwUu_7Y-BGYD_PdflLkUXgpG4rUN1VhH9WdKyZpZbmEHfOm88YyeYX3vrecSkMKq4MwDOOyjkoq6BJ1knLYjsc-R67AqwQCONKwssYj9Fs6f1ALThuD_rRX1Q-MUDl1hCmSV06Jooue3qzgDzNWGHxIKPTrpilb-bf6TC59agvdNzUfsm4sKsy1XLInnFY3JIX8aypbBEQFCZGdQjy9Z1TcKFxJvbLQp1trTMt5Y6d4c2STMzSuh8bBqWCB4k_JmUiCNeQvrtd9Yr69fvNc2ei7lE_nU2SYEnP1hcaaB31cxD1dxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f96f01d100.mp4?token=TJ99zpNrynQwl5zG1bBSBoAIDp4m_zM8u-9yJHwUu_7Y-BGYD_PdflLkUXgpG4rUN1VhH9WdKyZpZbmEHfOm88YyeYX3vrecSkMKq4MwDOOyjkoq6BJ1knLYjsc-R67AqwQCONKwssYj9Fs6f1ALThuD_rRX1Q-MUDl1hCmSV06Jooue3qzgDzNWGHxIKPTrpilb-bf6TC59agvdNzUfsm4sKsy1XLInnFY3JIX8aypbBEQFCZGdQjy9Z1TcKFxJvbLQp1trTMt5Y6d4c2STMzSuh8bBqWCB4k_JmUiCNeQvrtd9Yr69fvNc2ei7lE_nU2SYEnP1hcaaB31cxD1dxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انگار یه نسخه پرمیوم از ایران هم وجود داره که فقط مخصوص پولداراست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67523" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67519">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfz15MgjzGb5ymlJSZl0cwqnxPCXdhzTRshfaJUvZiMplG_u0BS-ip-c_VXtSxKPk2hpZy0HDZnIUBfKuVHZtFKeHmR9EyjWpLoFRxK3XXD7jmmWS-3Hiep9sO2HhTUze6gxWBRzP2oppC1rszaCFrnT0axtBydHdmHio6_z_3Lo3xkTu3Lk7iUBu838Ohz3xUH9FwuyDlIgpL09SBsdtNB2gZ_b3Yi4ipocatgRi3AvuyOIxsCBsfslgyddGZ8ONT4ah1hnCMVWQfxfif3_LLXifWk_YyNs6cdUD6Q5oFhTKams89kIDU85dD1Y1lwst_hQCQMxMeyBLV7MtGiYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41735c920b.mp4?token=dArQ-Q9ojJWOHDZtoDXGe__Z_Fd7XYEJwxpWp2II_v3CJTlXxNUdBWQiXvWs90kZxVIDyIfGeV8Zej3E5rap_SA2jX5d4fGYg8jHndCc6UHzWnkvvcgy8eOfaeJkL49fMwWB9OgAtm-8QSiCUmSQ0yQRKn7muNt3lEQ9Zif1yUYmddn6w1L0r4wUog1NRX5e6GcSCkPUjY85FrF1x0Ij7APtd_Ov-t7FkOtSl9K6AkPhearIBGmKwye6BRbUMS6HBMij4ERTF7Jh9cFyHEGJ44o_eDn4CkgFQ00ARPLH4eGphsoQKNxoe1tXXLiWcCmKezKyai_Klqc25B8_IDaAjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41735c920b.mp4?token=dArQ-Q9ojJWOHDZtoDXGe__Z_Fd7XYEJwxpWp2II_v3CJTlXxNUdBWQiXvWs90kZxVIDyIfGeV8Zej3E5rap_SA2jX5d4fGYg8jHndCc6UHzWnkvvcgy8eOfaeJkL49fMwWB9OgAtm-8QSiCUmSQ0yQRKn7muNt3lEQ9Zif1yUYmddn6w1L0r4wUog1NRX5e6GcSCkPUjY85FrF1x0Ij7APtd_Ov-t7FkOtSl9K6AkPhearIBGmKwye6BRbUMS6HBMij4ERTF7Jh9cFyHEGJ44o_eDn4CkgFQ00ARPLH4eGphsoQKNxoe1tXXLiWcCmKezKyai_Klqc25B8_IDaAjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات موشکی شبانه روسیه به اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67519" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67518">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_fzl4NCcDIc0QpK0BxVSz93YUpE9ggkzMLVpDUM9ReIbXidx08jr_Dk0spD6sSkANRq7hG8wn1rVkA36nXddde47XWlIdJ1Ob68cUDRkhzRXKwC36b2Sh_cCyTAbhU4-jr0n1O3G0G1QmckNnsL0C_H1iY9PIIOqpu9RbfB_cG_U9gl9YKNG_H2-l2qMto0Is_M4vfUam5ZVHJeHR8cc8GR_hO4fZEta7qW9z7WN5mXU6rQm-hiErQhmw6ot-FFqTxfvHb_WFNr17GlSL050cGJt2uegew8uOK-CmMnjawJPVOMhL7W4y-fldAWZIxhnmon0HIEb2Z2N0j2hFKhKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری هادی چوپان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67518" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67515">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwdlH35WnJimMAaHpydFO_EmIklIZj6zp0DQfPCGltpyQNzNzWmayKUrvUJ7c1bu23QJ_4XwtZ8g0b8woaX4rgusBkFgIVfiay9AdjH_3vKOV5I6EuEK0dU7LXO_2NEQLcXZmerbW3poe2l88lkcxgwroSiqVU05w7-12v5-3lJMlzt0DShtyIGYddLrq0BPGtvOrxixADMVy_jDU1ISX4SqLh04Wc_F3XBr0plbQMQnfgyggvGbSy465WCBxbAMzasOa0Xw2H9BUd8ZbyxEMdtY6sKjtinDOC5vCsJP7KJ3y2yDPb66cj53GIyslgdVriI4BTdffhOH6s4AgOzLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKuuigbqGpjOp9CF2zvdn19qBAun6gXMhQmpPjgoBQjisSiNNt8FIhkklIpqEoN1EAaKL5_XK4V8_jFNWvzPVcWnOurFnlqgnZ1ZnZ5U-jHrxLGBzi6TCtOkWGDnZsYZdXjsvQH33mmGjM9Yc9PXI1XQX-G8LcqAVAnPkO9gdydf-A608LGc1XW1823Xj-ccIfnhPxzoLHTBfdgK2jpTmdOap0OtBzQr_-26oazU7_kdNsEn__14yF6be0deoLwVKiwb7oUMM8o9WF8lIBQ7HlQC_pbG67QlCVroNAL8B1ukjb19F-4vYdrpha5A3mEyguhd9bLni7V9XJRR6uVaNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e58f00c0.mp4?token=eaIftD7Q6gu-AoJj34a-TcZgRyxDIp34qw76JPdI9EhyFRssvcemixc7QdqMntsGRPL1RqdHq5hj42jJ7oWE1Im1W9DGyVthYyUpoCim8-Let5OvJcuH8oix0h7n4JpkSSOtoYjZzCCCRV6A5PbjzjHv0u30ZIY_LA-FshciZKkZCD5fnfuHO-pRaC1LEYq3AalvtVWpH9hmyXfrQbhRDucLvmxBkuJSUublU3Wx_-0PmwSXWY6Oa1vo0pJiG-rJLQnqz-XGDcatoxzePyiSaoE2hOGAulpFRZVtM1uYtn-Jrbjd2CmEoZisbAxM1bfwxAAzFGfb-RBsUZl1uOHPv4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e58f00c0.mp4?token=eaIftD7Q6gu-AoJj34a-TcZgRyxDIp34qw76JPdI9EhyFRssvcemixc7QdqMntsGRPL1RqdHq5hj42jJ7oWE1Im1W9DGyVthYyUpoCim8-Let5OvJcuH8oix0h7n4JpkSSOtoYjZzCCCRV6A5PbjzjHv0u30ZIY_LA-FshciZKkZCD5fnfuHO-pRaC1LEYq3AalvtVWpH9hmyXfrQbhRDucLvmxBkuJSUublU3Wx_-0PmwSXWY6Oa1vo0pJiG-rJLQnqz-XGDcatoxzePyiSaoE2hOGAulpFRZVtM1uYtn-Jrbjd2CmEoZisbAxM1bfwxAAzFGfb-RBsUZl1uOHPv4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه تو ایران با سنگ و چماق میفتن دنبال عباس و میگن مرگ بر سازشگر ولی تو عراق اینجور نیست!
مردم عراق انقدر عراقچی رو دوست دارن که اون رو تَبرک میدونن و خودشون رو بهش می‌مالن تا حاجت بگیرن!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67515" target="_blank">📅 15:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67512">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEoRnu0z-mjWbdv1M-2auWqRkyWqqBKSnl9OFjIOWKSiclWgKd0o-haaUtKnLcSWjdyS9FUq_XqfrqvIsXvR0xCpm_sNIK7cpSBOQMQmY3LwJloQgdsuVO3ggao5TPEESPOI0qb6v91CPGBv1j_xwz7h9LDV9pHLEdXBdRMP7o91Ndo39aPVJg5j4-ErYRxr7B5d5xagE5YDdYSiYTM76SJC-zSbLpPCgKbkV8UOEfh4tLOU7wPqWrQPpVZr1iBL7y-Jb3pPtASycFNqoTcENQwrgLSWwJhYAFFhTclsBJgHaDCha9S6lHTao_hjN2-kkmO7Mx3XkPLL9UOIPotkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuE8kcucSsobQbnZ4sdJsINlu5pp1J78ZjIgvbGpvrjc2QlMfbpnVbp5EvPTH2kHHYZvp8QR1Y23RlLjTWCOHTWfv8mWD2zeKZpjg8SFMuf2yaSZBvZgFfZrBQiRqQQQwqUV19DNN6WaJ1V9GJkWtZ_hwTzzA32XhTGeDnsDlmd3Bp9vYahrY-gNU1LVDxliOBCm7ncRaUrw9pytoQMWbOR61HHV5rxvO0Qt-wHfS82xBNbylL6-n-rbjrqteyVwXKX0CODAOCPdg-_m3D8i95is4XvsLmTBxiDE8cuHVRBaWGvOZRRRrwAkhjEqLkOGl2LbOzBLow0Zy7YsW3jBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hi8Xeb7BGty50k5lNjrLM8je8E0rYaevmopVcUNilOsnwDbTvUPVnDSsBQ6mm7Y0ay6dJI17eFY2Bi-qBxJrSWhnyYOWGa3y32aShvGGym30PjbO58y9qFWxnECCTjvkeU2-QXnkoKfDmUXltmxjDY9Q6HMYIgJ9qY_7K9RLpUqEmU2mgWgT-UOZe-zeXMtxs6vGhSpyEfEb6PDSft8t05NzL0B9w1W0B_0LFfKpHRrmiXCRpMRPtFW2Q0-yUy0SriythFoXY_6bfwbNw3o4tYkvduw_jVGHEuF5_S-t5ktBDPeSkcHGhuc93xIqOrRnuGHQ3j_5OwaeltO_TW_IXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
خبرگزاری تسنیم اعلام کرد یک پهپاد تهاجمی MQ-9 آمریکا در آسمان بوشهر سرنگون شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67512" target="_blank">📅 14:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67511">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=JN2RxP2POpSpo2bPzqGoczbiotzy8SvwEWXI6CsXYHmx2Uf83ldO9ADPCqwsawsT2s9pp88Zwj9ljTnLfxnd5A_aoUcjBbadOtWYGywOQ5O34IRRSklP7liB3QOcesev0it08B41cJAlcP90vZnUMCSCA5d12IcMME9e6-Blg02RKmSar9rMP8bpp10lOzHe_D_d_7f_WtADkweS8cWIaz0XG1qx4CfweH2_sccYnzCIQ2Q1yT2p1K-V_kmw6Tvu30avctAXrYRjkGp4gLFjVpz-hVKsqe-lqjTsjQw94ebEA2zhrCb7SrUjbmxiorZLFyldjLL9zW2kbpIPIgQLsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=JN2RxP2POpSpo2bPzqGoczbiotzy8SvwEWXI6CsXYHmx2Uf83ldO9ADPCqwsawsT2s9pp88Zwj9ljTnLfxnd5A_aoUcjBbadOtWYGywOQ5O34IRRSklP7liB3QOcesev0it08B41cJAlcP90vZnUMCSCA5d12IcMME9e6-Blg02RKmSar9rMP8bpp10lOzHe_D_d_7f_WtADkweS8cWIaz0XG1qx4CfweH2_sccYnzCIQ2Q1yT2p1K-V_kmw6Tvu30avctAXrYRjkGp4gLFjVpz-hVKsqe-lqjTsjQw94ebEA2zhrCb7SrUjbmxiorZLFyldjLL9zW2kbpIPIgQLsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
احمدی نژاد : بابا داره بهتون فحش میده،یه مرد بین شما پیدا نمیشه پاشه حداقل بگه خودتی؟!
+ترامپ امروز به مسئولین جمهوری اسلامی گفت آشغال،پست فطرت،کثیف،تومور سرطانی، شرور،بی‌ کفایت،بی ارزش،بیمار،روانی و حقه باز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67511" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67510">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
رسانه های عبری:
ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67510" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67509">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbjxAb4K3NmzOwRAU_Ewp3e91G7Ku0GoUGcRDEe4ZZYn2im51xGmuAQ1J9OJFssNioTiF8HravSUawirf5K5mU_JdkcQ3NJEY4AY1skevQJvJY4CD_9q-xNoS4Zivp3kmdM9um0wohRuJok0mgyFmZUXf_iGZSOlWoQqtFFV3e8RBT2IjSltQ5UUxN5TXo1sNLzlv1h92yQe0gLmY1al1eVa9mdTXWeI3OHaylqPwjlyevS2mDjAMqE1axEMQGXGWz_a9TqmPht03dj1NhiefIc3J7s2TRA7tSweRbYrbBkDCqbbQpdjk0SmBIEn-GZUJRh4g66U-UqQ7hjQI_sHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
پزشکیان:
رفتار دولت ایالات متحده به عنوان میزبان جام جهانی، همان سیاست خارجی همیشگی آن را نشان می‌دهد: زیر پا گذاشتن قوانین، زورگویی در برابر رقبا، ایجاد موانع و تقلب. این همان روشی است که آن‌ها دنبال می‌کنند. ایران چنین بازی‌هایی را رد می‌کند. ما به طور قاطع از حقوق خود دفاع می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67509" target="_blank">📅 12:55 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
