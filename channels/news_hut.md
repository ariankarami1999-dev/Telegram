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
<p>@news_hut • 👥 191K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 08:59:38</div>
<hr>

<div class="tg-post" id="msg-67628">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/67628" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/67627" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67622" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67621" target="_blank">📅 02:29 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67620" target="_blank">📅 02:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
انفجار سمت آق قلا گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67619" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67618">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در گرگان
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0DTz1mRQH-_ZF3QcNaUPzPKPRTybhoa5jKovGU6haJ5EM50z_VhlHzJIf5kmiclsY3KGNzNtu4Yrd7LoFvbfcvW3YRT912g0BuZJZc-jvrra8AihadtsTMerF8W2yUiCV4dKn8KCb9e4IQEBnx8cyR6A-hY2gCVJ4K-5h0GF6NV92Hk4ia941ry31dRdMcfr27V1BOL47mNTCAhfTCuZeKzvTrYhDkxWE4oShpweRzHnTBRBT7r1Nw3gmxqS4Bj_9aWAzzLtnOENUv3ZXFUGArLc8Oj5Zx3Q_dO2-HDV_mv11yttIoZcwGM94XI_C-hnIosgI6sY9rGo_qLija78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقاطی که امشب توسط آمریکایی ها هدف گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67615" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67614">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر بسیار بالااست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67614" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67612" target="_blank">📅 01:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67611">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyvQOaESy4VINNR_v5j-kfxg57gfVLkLLnaNXUlW0ecrwMka7WoohEwRbqcwLyhkORb3oK_FxD1BATxmSUguJa_RG1ydLz0K2RbK8oDLolrfjv9JCM_Amf_JMw-JSiuAzl-YEnLcKaPw4RV5HfQ2qFO6gsD1gwz5be0O8wfVCZaAEDEOqywudqHKJIdFBho5osP91064m2JVrHeiAbiUX49Cat7ehul5ScTwnGupix7u0wLrDJ0VN2SLSpcvVGkc7YTWGWUr3L8h_mlhI8LFDmQAFj5qgwUTf7ClS7Sv0J1h9_tF0MIf6YmdclH_PHx3sdC89B2pfCddkECKKtnjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67608" target="_blank">📅 01:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دلیلِ این چص‌حمله هارو متوجه نمی‌شم واقعا، آخه کسی که زدین رهبرشونو که از نظر اونا جانشین امام زمان بود رو کشتین، اتفاقی افتاد مگه که الان بخواین با زدن توالتای پادگانای سپاه اتفاقی بیفته؟
صرفا این حملات شرایط اقتصادی رو سخت‌تر می‌کنه همونطور که امروز دلار ۱۸۰ تومنی رو دیدیم، خود ترامپ هم می‌دونه تنها راه حمله زمینیه و اولین نقطه هم خارک ولی جرئتش...؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67607" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67605" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67604">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
انفجار های مجدد در جزیره بوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67604" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67603">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ماشالا ترامپِ شیردلِ مادرجنده‌ی املاکی
😊
#hjAly‌</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67603" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67602">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67602" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67601">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGsCi7EaTgb5c_O6iy90qEyzvpg1zRmiyqLQPcAFm6MufUCJx7oEnZpA8BZOVhajiFD639doyUykKY6BWXd8Raht3s_DZkShlO76v-zIjQuW_Lf6XuLy7NalMjyhqgJ3qu7lz5wrQmWWr6wFL2bdmq_8vpLQ2eDp6ClSev3nlDZ_F0AQ-eEjDDtsPBBKwYkAJ2AKPsFmwBuTUpNfZQYd6C5slDbYEL3g7EPGIjFTJ4n8W4ojYbxfKGXYjqJsDsZSxpaY2SfcJS6fBQYP9dWNA2DsnvQ9xaKuj97SuqyFtW0p3qmp0V26l49Rvwm7A2EdWMB34sQdDEJQcF-suY8cYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
یازده فروند سوخت رسان نیروی دریایی آمریکا بر فراز خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67601" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67600">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMpFC7QrCFF8uSxjGPc5eDlOQiCo9X4ZxljVM-ABo9o3rY83IcWJsX3BhSNBdkCOw4Oqwx7SMiUN_kTOLaumQySyz69ZR5UmOE_6ArrMQLSkbVo7dsZQIcGAFjevLwdil_fn4qMeQX17Me1DK-QTgznhhQSlH8Pfim5DQyCibk_vWrH3TQqXmJeGUhddFSA4N4zsfDEQlhQxdGLdl6AEfkF9vo0CMVk5_5o4I7bgmCwhuV-nqsTm0vNovsFWtcTCJGmI6J3W1MKeokto58NqeW3V5u6geLd4t9aJUxfXYs5fw7L72aDYj8rsFQ8-9H7ek8enHj6pg48cu32pPMs-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت شهباز شریف بعد از حملات آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67600" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67599">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
صداوسیما :
نیروی هوایی آمریکا در حملات به چابهار، اسکله‌های «شهید بهشتی» و «کلانتری» رو به همراه برج کنترل ترافیک دریایی این بندر هدف قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67599" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67597">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/py2XkGRUos5BwA3E29zRiu56kL0eD17G92hWRBcDXzepz3vra-JRCtZLGM1dX0U3WLGSifTrvExFeuHJ4eGyy1Yo76mWXUlId4YfwVaNowuY5z3sfHxxt_xBStDr1wU_GSWD5lp3iuWdUQhDCJp8NmjbPhpd2crthXnPx_XQkEH587Q2fUg2deb6c99KqulFbRe5A2ibfJJkVS2prEoVOm3-6Gn3DBqBLHrtYDV4DQ7LHZ1JdsGGv0-NSVIcePWqUP1Bfz0qn0MR9yPqMtQq7eYF-z45YN1YPhMzsQ-qMibpa538wLxKyALC_uR93ejWJezQyicYmBgjjXt5Zo2pjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q05I0QyNmM8DzuWRKz-JHScZoS1B0up30JvpJ0QQjMT298ecsLBcNVRlnV8tFUQl7JaHM12VZvbylBM2xNXzcbH5B0ElMYBxR6cCQjyM9qwICksUnkDtaXAFELNy1xbobGn7ThKfDd8wuSWeIncgUuebKx17dUuXB3JVlU7GHVPHRk-is9jRomdSGgfNh0reqSAPTazcNNVjQMpAQgZED_g-pTkfDqyI22-b6YsWwkekmLi_lH8Jv1n6TSqhTPAuMfM0MinzOJ4t-e0akxxgCVvRnyR7nsSwRX5wrsSDP7dOvpqfnq3tjMl2C1ro0OrTM7Nd2QiBbbgSYqH4UhYD5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
برج دریایی اسکله شهید بهشتی چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67597" target="_blank">📅 00:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67596">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇮🇷
محسن رضایی مشاور رهبر:
دشمن متجاوز و همدستانش به شدت تنبیه خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67596" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67595">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67595" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67594">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
چندین انفجاردر بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67594" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67593">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
فعلا تمرکز حملات مربوط به خط ساحلی جنوب کشور بوده
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67593" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67592" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67591" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELKDIgLFli5TDlCipOKc_t6w1Msf1ny9-x2Dv7KvpI3WiWXROJZUM5_JJoT2eAqci192DEP3pTKiJhZWgG8IrF_9FvIiDGX9D0IDc8Zri3zk6Y_P8TfD-zxrxpLPm0L8ppD04QLGVWI-5-fAHc_Y4x3JUxG-9sbNv1lOhuvFTxNvLKKA8KSkoHmPcvOKNxOrdEhrg9ejzbJTul3ZfKccmgZcj9TKivF3OiFYwUCi-WJ1L5Z7w4cDlGnhd4JztP806mdCHbLEtHHBTij3UrM2cxNsjIcLkC8aGXzioALufxxcf4hpjKVsFp4iZSlACwwnoewdrrnw_YYy1kpkQ3VPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=b73oHy3Qh5jAhCsh83H1ycaUf6D-LruOd6CvttLwmp40h-8AnojwuKDd3_4VSuY-VCKScZ-mJkT7iQ1_g5gbUT0TH4cLykxYC-9uH3nzPt11J3HT6Wbw9XIK3op6RgPcWO6LLAO1VMJMqcvfhzd2xfXu_9hWXIQIChKK2h2mLTTqwrcKtJsJ00UC7TfAqbdmmMQwg6aHL_QcW8byg00Pbi-XKogLrU3VxjJbXqk7pLf5AAzVh06gXtZFFlizZPAZnBUXVwWP-XueAPbMU-4HbZqaXvlcCodAjS4Kkd6VsPwIMvzHsDmYB9BJPuv6uVTRHjcFnzZVEapO6IjTbwE36Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=b73oHy3Qh5jAhCsh83H1ycaUf6D-LruOd6CvttLwmp40h-8AnojwuKDd3_4VSuY-VCKScZ-mJkT7iQ1_g5gbUT0TH4cLykxYC-9uH3nzPt11J3HT6Wbw9XIK3op6RgPcWO6LLAO1VMJMqcvfhzd2xfXu_9hWXIQIChKK2h2mLTTqwrcKtJsJ00UC7TfAqbdmmMQwg6aHL_QcW8byg00Pbi-XKogLrU3VxjJbXqk7pLf5AAzVh06gXtZFFlizZPAZnBUXVwWP-XueAPbMU-4HbZqaXvlcCodAjS4Kkd6VsPwIMvzHsDmYB9BJPuv6uVTRHjcFnzZVEapO6IjTbwE36Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67588" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67587" target="_blank">📅 00:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67586">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره ابوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67586" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67585">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=l-UhpzsI3PF6lnRp8vMNX4_a5wQQ4sfCRdwNffcrTUQWmpm_6UmTkGsa4SbC7Hxd122_YzCv4H8sQBQbOpiizsTX7ZchxXtX-6UDzN5EUTPyy_K6Y55P-54tlMv6TrdkxOUubqgvxrag2drwvh5DhJ40lAY3zGaUplH1etjCbCJC60A8bVPg21L9QQYOV27BEDO2j8AYx4y5n8Ox_ems5NH1Q1G4B4uk-McZEY5KNz0TR1eE_3LigLqaxadHHKUME_CivbNI3Qk5zJ17Yl-HyYX2DQiuXJBv3WGOd43DelK0eZ1vKr78usrd5KahX6uIhfwBc63vVd3_Oc7Rmouwew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=l-UhpzsI3PF6lnRp8vMNX4_a5wQQ4sfCRdwNffcrTUQWmpm_6UmTkGsa4SbC7Hxd122_YzCv4H8sQBQbOpiizsTX7ZchxXtX-6UDzN5EUTPyy_K6Y55P-54tlMv6TrdkxOUubqgvxrag2drwvh5DhJ40lAY3zGaUplH1etjCbCJC60A8bVPg21L9QQYOV27BEDO2j8AYx4y5n8Ox_ems5NH1Q1G4B4uk-McZEY5KNz0TR1eE_3LigLqaxadHHKUME_CivbNI3Qk5zJ17Yl-HyYX2DQiuXJBv3WGOd43DelK0eZ1vKr78usrd5KahX6uIhfwBc63vVd3_Oc7Rmouwew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هم اکنون؛ آنتن زنده شبکه خبر
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها بدانند پاسخ کوبنده‌ای به آنها خواهیم داد و امنیت را در  هر جای دنیا باشند از آنها سلب خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67585" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67584">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=q1e-em_zB4nCxWFWkPaSHm_e5oe_wi1z-iBQ_NsC7AXaZRi_kUO4i6Awnyk4E3_uvCeRFXv7bki0UIaDLErqxEckJDMrAjPrgzU34iYQ_wG93hVcSqxiflmnSrhm4Q3VTJuQJQ7Te1p6qfgrpp_Xk6lRnoJ58wYuOfFtiCcTFAA8pfYBj3fwfolacfKBXdU92CjCx9e_tHj4xVbZniHJNxxVSocJwuxT84cTS9YizZG5ygRNyx0niZRUVe6z_PaKINuoq6gj0WaCHUjBXkyQ9_MkV4tT7xzli9t8KxidgFUw5AU73eikVYqmppVnjAH8IB0LPJg9B_8Qc1hOmBvsnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=q1e-em_zB4nCxWFWkPaSHm_e5oe_wi1z-iBQ_NsC7AXaZRi_kUO4i6Awnyk4E3_uvCeRFXv7bki0UIaDLErqxEckJDMrAjPrgzU34iYQ_wG93hVcSqxiflmnSrhm4Q3VTJuQJQ7Te1p6qfgrpp_Xk6lRnoJ58wYuOfFtiCcTFAA8pfYBj3fwfolacfKBXdU92CjCx9e_tHj4xVbZniHJNxxVSocJwuxT84cTS9YizZG5ygRNyx0niZRUVe6z_PaKINuoq6gj0WaCHUjBXkyQ9_MkV4tT7xzli9t8KxidgFUw5AU73eikVYqmppVnjAH8IB0LPJg9B_8Qc1hOmBvsnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67584" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67583">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02d221609.mp4?token=KnUw3VtYwQ0KJ2QJcsDHGj34x9QVwmu032JqaVhx84mpdbkZscoVATy939iTOG5UQ7inTUsVEQ5Lk-m28ZfVY614bEu7yrQunybMlgtZTS4FAGMM_2ZXjTbb-H9s9gFfDtFcjObneEK6KiP_JflqFX4aC3KN8pBS5QGLrHm1B5P0ct6yGAo7yRnGZhS3IX-Z4j5PJpSqQUF_fVrSO3En2ptdB0GlSUQOJgGuwrt7AZdX91CKsDSLv3WNZZkhfWeYrpQnjvJMPV6zGcxROJhckF2RuhQ2Yr87xNyKndOl6_zaUBpFpBAYj6AcN1V_EB7EHMzQxdO7fXqFsa6mT6fMEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02d221609.mp4?token=KnUw3VtYwQ0KJ2QJcsDHGj34x9QVwmu032JqaVhx84mpdbkZscoVATy939iTOG5UQ7inTUsVEQ5Lk-m28ZfVY614bEu7yrQunybMlgtZTS4FAGMM_2ZXjTbb-H9s9gFfDtFcjObneEK6KiP_JflqFX4aC3KN8pBS5QGLrHm1B5P0ct6yGAo7yRnGZhS3IX-Z4j5PJpSqQUF_fVrSO3En2ptdB0GlSUQOJgGuwrt7AZdX91CKsDSLv3WNZZkhfWeYrpQnjvJMPV6zGcxROJhckF2RuhQ2Yr87xNyKndOl6_zaUBpFpBAYj6AcN1V_EB7EHMzQxdO7fXqFsa6mT6fMEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67583" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
نور نیوز  :
به زودی حملات ایران شروع میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67582" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=e6_f7KaZreJv62NQ1Cmc-DFeBOE0XgMYCFwCbJOlQCm6GaAjOfw4mRsPJYvz8QF6x0TIHkQAjpgerLdJNNyFtJta8cTyuuuraL7PdbWP7hTIaPrpJ_88pndqYjQNYld-S4seqEzW8zrcXcBNY57ZuYXd5uGutMF-5pqYu56czzGSoR16RE3x626LfZ3XeGZXxjSYboKam-AFfw7tydgyvI7OS3cfuZNxcSFqh8tixcpCE1RPcTuAsn9RTaJqHJ8km5Y6EwtUHc8aLLa1WIhhyzNEaBoVWqysW7QqPjc2_lp_C66L5YjfHAO-0Ttfmt6Y7STZO7UoFH4dC--KPwzlMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=e6_f7KaZreJv62NQ1Cmc-DFeBOE0XgMYCFwCbJOlQCm6GaAjOfw4mRsPJYvz8QF6x0TIHkQAjpgerLdJNNyFtJta8cTyuuuraL7PdbWP7hTIaPrpJ_88pndqYjQNYld-S4seqEzW8zrcXcBNY57ZuYXd5uGutMF-5pqYu56czzGSoR16RE3x626LfZ3XeGZXxjSYboKam-AFfw7tydgyvI7OS3cfuZNxcSFqh8tixcpCE1RPcTuAsn9RTaJqHJ8km5Y6EwtUHc8aLLa1WIhhyzNEaBoVWqysW7QqPjc2_lp_C66L5YjfHAO-0Ttfmt6Y7STZO7UoFH4dC--KPwzlMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ریشهر بوشهر دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67581" target="_blank">📅 00:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=ZFA2BdWrsAGUsayN7pmXzU9jlgmYlbHm7uUKRMUvp2Aeh87_37ys80fklFzM_ZS07bWtb7dERsY512dLa1zXID3fldB4WxvXsWOMJZ5CnGLTopmEJ9i4ngnCl9yTG3Ea9KvOpJoYghynndU8UlzNT34xr8GqqZVEipSwHhu4P0A5BVv5jDQ4L2VOJ7CKwqQrCuy4Rklxk_hjiM__KDtk5LYVVond5lgKCP5bEhCeqye1_yIdsYuPwtOTZ709hlZE2J6hT0qhTi2YZ7iJ4oYQu_dMhXQxvikLcE5vPpRTaiV1Y8AQyV46cswPTcaoFqyjPSYUk5dh9of-uSfLf2Cxzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=ZFA2BdWrsAGUsayN7pmXzU9jlgmYlbHm7uUKRMUvp2Aeh87_37ys80fklFzM_ZS07bWtb7dERsY512dLa1zXID3fldB4WxvXsWOMJZ5CnGLTopmEJ9i4ngnCl9yTG3Ea9KvOpJoYghynndU8UlzNT34xr8GqqZVEipSwHhu4P0A5BVv5jDQ4L2VOJ7CKwqQrCuy4Rklxk_hjiM__KDtk5LYVVond5lgKCP5bEhCeqye1_yIdsYuPwtOTZ709hlZE2J6hT0qhTi2YZ7iJ4oYQu_dMhXQxvikLcE5vPpRTaiV1Y8AQyV46cswPTcaoFqyjPSYUk5dh9of-uSfLf2Cxzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظاتی از حملات آمریکایی به شهر چابهار، ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67580" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67578">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiODP-dbHXF4vAiBzv-AeO4MJS4eDne64WIfW1PnXmL32txrlXnee2s2zmPb5a2pJeATtDfBbH6DEGS_jnLaumMDiTqzO5Yd7vigUW2jW0SBMLotm25vsbzpI_hMiQ0KU6ElSZSpLRu4aC8U__kMbil4kuHoocTvpbkrbHnpMDbFBCcEwCMpXOaBJg-G6nZksCQ6dgsYeRPoHhsOxOKLrPDfqYv7b1VnQU6xc2Na4JShyvor3Wlgd7TMavAuyGQXchSoiXdV3__co9NIk5bFPOut-vJ19brnIOBYyXXQ0Z91nn_8DRhNI15fNfchJAZPE9SnN3mM4PD6z47BzON0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hD9M1y8srizqFlMcJLIaT3yaVDOb01OwKi0fpKM8zsyfqgd71X66G6Qgnuqxzc4l2XDlenbuc9n-TnzmxH8kbOI3bAysWgNfm2GUEZgVlOPEMaxc6RkvScbpWz4ZRE9GvNqnBNQiHf6sd__JQ56uk3HE8hkfF7_vUKFkFmClHhe9UjVPQXt3MKZp7FatkyrezLA_84J6zPsCB4Q_Bhmr65d4bj_1CXA0VYaPIcheciDCF3YxTUadho_BOhpRO1UN4LiYLFHDma_7-11YQlu-j-jvCsX4RyATczX9A_ZfsnU5QZXDNb5rypl0KpyeWvEn0tbSRAFs83WMAP3yAYpnNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به نیروگاه برق پایگاه نداسا در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67578" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67577">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=g2ikggRRjBwgmbuNyRvepecaHoJ2bYCjRk12q4V5zXVFaF4F7VkWME3AqufVe_NpJeQ_QekIJvYdM2Mc8awAuhPhTUiS3mE2kAyqy_2eBQ0DyNCMtSxabX6wk05DL8pMvhaQZVVn1OnmMK5sCulzzw_l4Wbm7QMUJq7dmVZdS890IWrMMdYzV8K-N5kpQer15H33W8NrphxhAGW4clS3qMGJbrmsnWmk5Hp3U_0EYvKfbWUDlvfwMC_JkK9KN6py0G9OTKfOdLJKl0qbRs3zzh89ESm_bdLTSLg_5Q3dn-3yDY7-nHFhfjntB6OmGuc7EvXT1aoAVbdOW5rNovK6_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=g2ikggRRjBwgmbuNyRvepecaHoJ2bYCjRk12q4V5zXVFaF4F7VkWME3AqufVe_NpJeQ_QekIJvYdM2Mc8awAuhPhTUiS3mE2kAyqy_2eBQ0DyNCMtSxabX6wk05DL8pMvhaQZVVn1OnmMK5sCulzzw_l4Wbm7QMUJq7dmVZdS890IWrMMdYzV8K-N5kpQer15H33W8NrphxhAGW4clS3qMGJbrmsnWmk5Hp3U_0EYvKfbWUDlvfwMC_JkK9KN6py0G9OTKfOdLJKl0qbRs3zzh89ESm_bdLTSLg_5Q3dn-3yDY7-nHFhfjntB6OmGuc7EvXT1aoAVbdOW5rNovK6_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش سوزی در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67577" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67576">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
گزارش‌های اولیه حاکی از آن است که هدف آن‌ها نیروگاه‌ها است. قطعی برق در چابهار گزارش شده است.
هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67576" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67575">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
انفجار های پی در پی در بوشهر و کیش.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67575" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67574">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مسئول آمریکایی:
حملات به ایران، رادارهای نظامی، پایگاه‌های موشک‌های ضدکشتی و سامانه‌های دفاع هوایی را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67574" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67573">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
❌
گزارش‌های اولیه حاکی از آن است که یک پالایشگاه در جزیره لاوان مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67573" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67572">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yll9v-unMfD_FGXf8rcycIfSL5n6uDiky_pt13QDMSFE0A3I7RpFzNkB-LoT5NGOtsB0eyxcJjtChz6LUl4OCyiOmT8OrrXrG6p6I_EynRHa92eCDuypeq7gkFspxl03MNWV-8wGsLBJZA_wp_8JQHB0QUfcSvHhiGugVsce6Y3KPQvvGvTEUlqQAfzg0H3hoEYzjwdEK6XZ_7Q4WSyOMFM3ixiCne3uKnrg4DcyXuolqJvpPm_z53VdunXFtWcqvqhwrIACScZ_nmnDClPueCjzMA6u5NLS0CGia0Kf-1BwpFKsynDWIZX4FWQ28g6jgZzksdxsl4XT7wk1ZqN49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
حملات آمریکا به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67572" target="_blank">📅 23:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67571">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
انفجارها در بوشهر و جزیره خارک
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67571" target="_blank">📅 23:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67570">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67570" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67569" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67568">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
صدای چند انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67568" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67567">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مقام آمریکایی:
ارتش آمریکا در حال انجام حملاتی علیه اهداف نظامی ایران در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67567" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67566">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
پادگان ارتش در کنارک توسط آمریکا هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67566" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67565">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره لاوان
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67565" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67564">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=CAt_2JLO_BR1S9Hi51-iuPnXERUyRLioGTm3Ls6HPmBzuAHfgLFQqFNhg-UpTuDUfOg-xBQ2nZIZFHCPjK69PDZYavpU7868QWUMyKZUp_TdRyt1e_D4HQ5stEIuTekaYCfJYwX-4qu3aQPXgMGQPtsH6F41ml01KYh7eiXrzERVUBWR0pHVByjVaLhGgWGfgvZSR9NoTvfGW6eFn5FMe7HqKFXPZua6ElbzNCv_PEHk0cHbJzGZlWE9ukKQWVKQn2wC6T_CnPc53Flcav2_WP7PAJ14n9ko3ljbCC9Nvn8heIXuqxyrha2fAGyUv8VJ94qjIXOM6PBu0_0HeBNNqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=CAt_2JLO_BR1S9Hi51-iuPnXERUyRLioGTm3Ls6HPmBzuAHfgLFQqFNhg-UpTuDUfOg-xBQ2nZIZFHCPjK69PDZYavpU7868QWUMyKZUp_TdRyt1e_D4HQ5stEIuTekaYCfJYwX-4qu3aQPXgMGQPtsH6F41ml01KYh7eiXrzERVUBWR0pHVByjVaLhGgWGfgvZSR9NoTvfGW6eFn5FMe7HqKFXPZua6ElbzNCv_PEHk0cHbJzGZlWE9ukKQWVKQn2wC6T_CnPc53Flcav2_WP7PAJ14n9ko3ljbCC9Nvn8heIXuqxyrha2fAGyUv8VJ94qjIXOM6PBu0_0HeBNNqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات سنگین آمریکا به پایگاه سپاه در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67564" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67563">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به بندر کنارک در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67563" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67562">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
گزارش صدای چند انفجار سنگین در بندر چابهار
به پایگاه امام علی در چابهار حمله شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67562" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67561">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
خبرگزاری آکسیوس :
ارتش آمریکا امشب حملات بسیار سنگین تری رو به ایران انجام خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67561" target="_blank">📅 23:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67559">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aXwz_YOLrFdV35LQJ1iqUOOYFCY1FrmTmM9shMhmZ2JPIwcz4K6x3aeQk_j7mRdJqiH6IHoEUgc-nXwz0zq37u-RNtx81wq8Jy1133QFjqpWvStibCFt_x4o3m9JMFwDWuwZvud0VVz_X2R9-hqjRDxUJ8nDX-M9vugxmKVmbogOIVOWzIuP-YJKi9uBhlCE17S88XYalIMZmQMNEwVwe9wTWmhxrF9aFgfl41KHLFvJqXMC4NaXgCKWYBc5ncNJHxBKpHxZcVyPDCUB-cbDG16Cm_kJhNKs5IoJFjF1AgPAhI-yhfjmTWH6f-WA7wlgmO-os7gpnlJBBsFMkJsk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-KqQrJqAqn4moMcPwFNybWEjl_E9yalrg-AT9P0m2lxEQM9DMRkQYBlQl8jiif5u0PwFxK5P9IPX5dfjeyvF245bkYYkGzqjG0CnmLMEmNF94V4EMcnn6mvVtFwx60kk7rhcXtOkFwqR8thgPV8D6gWLDc4HgZIqvC9o1Kq_ZbMnmey9N3ojOspZfpHPFMTo82ypDS2jGWpojOxpha6aflC94q_pAFaI1MgJ8YbYLEPPmE3Mm5wGIkesPjzOP0Pjaa5Z_lVMi54LsWeX7RKs--11ADccLP6dVb00bMakXopqOw2CpSHt08GoS8jU85NEc6muDT59s24pu6GuSZMeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
بلند شدن سوخت رسان ها از تل آویو و امارات به سمت جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67559" target="_blank">📅 23:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67558">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
فعال شدن پدافند در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67558" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67557">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67557" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67556">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67556" target="_blank">📅 23:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67555">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
❌
شنیده شدن صدای انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67555" target="_blank">📅 23:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67554">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c65cdf89e.mp4?token=KiVG2uq8i7U581WLl37Ek0f9xl5-MUaTesubxhl9OgLyK_JE0PDitGID_3O0sjnFBYVJlx4-vI3vxQBwjNzeKLp56qjHIzKTIqdikolllODcAjAS9sCk8tmgBS1oxenJS_q2L4cUUU39GqIBx0u5Krk4e_WULY4h-i8R1Ez-N-o64fkUgx0L4JwwCJ1JgoPm5gbg5BZY6M0tyFSmoD5C34TSWMndW50o--DHH9UvPC8MinrFXvD7LasVzXd4NrmuVZhGjyh60kzwXAgSwYKQys9a79k0pddOd0cd_Bhwk6Gw83C752nveSIUeJc3afIcnZK2uXhcZ0v1gM2xtdAP7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c65cdf89e.mp4?token=KiVG2uq8i7U581WLl37Ek0f9xl5-MUaTesubxhl9OgLyK_JE0PDitGID_3O0sjnFBYVJlx4-vI3vxQBwjNzeKLp56qjHIzKTIqdikolllODcAjAS9sCk8tmgBS1oxenJS_q2L4cUUU39GqIBx0u5Krk4e_WULY4h-i8R1Ez-N-o64fkUgx0L4JwwCJ1JgoPm5gbg5BZY6M0tyFSmoD5C34TSWMndW50o--DHH9UvPC8MinrFXvD7LasVzXd4NrmuVZhGjyh60kzwXAgSwYKQys9a79k0pddOd0cd_Bhwk6Gw83C752nveSIUeJc3afIcnZK2uXhcZ0v1gM2xtdAP7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
خبرنگار: شما امروز با هگست جلسه دارید.
نخست وزیر نتانیاهو: احتمالاً این اتفاق نخواهد افتاد.
خبرنگار: آیا این شما را ناراحت می‌کند؟
نخست وزیر نتانیاهو: چه کسی گفته ناراحت کننده است؟ شاید معنای دیگری داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67554" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67553">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/176e4f444a.mp4?token=NTHrM-2QNWA8Nkk7dGRc63Dj9wA1B9fLL6lE0ufcB_UynktIxzL08emZRxq9m8WYM69ZUIj8krLprlnjTgGSpcIbWD7CCV2DeD7QNXq1K6xZjsGbunlF0b6cDwdnnBQqW-HViQzvlv0-4AfbiXU_vAMBXgUWsQzNWAOr3ZqpCzaN6svQ7UnSCNk3nPDIwfYqB17OEH1fxoYmtsHVpjt9iaN0w-YdEQ_L64s0G9ShZsWjB1BbXmwknGfoeP4N86dv4FM2Kgg8AfINU--UgqpWkgxmKtcjooXSPil7rA5buC11HSsFojMBRD3fKk4XvH047q8wVWIRdlUCa81tyd6XvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/176e4f444a.mp4?token=NTHrM-2QNWA8Nkk7dGRc63Dj9wA1B9fLL6lE0ufcB_UynktIxzL08emZRxq9m8WYM69ZUIj8krLprlnjTgGSpcIbWD7CCV2DeD7QNXq1K6xZjsGbunlF0b6cDwdnnBQqW-HViQzvlv0-4AfbiXU_vAMBXgUWsQzNWAOr3ZqpCzaN6svQ7UnSCNk3nPDIwfYqB17OEH1fxoYmtsHVpjt9iaN0w-YdEQ_L64s0G9ShZsWjB1BbXmwknGfoeP4N86dv4FM2Kgg8AfINU--UgqpWkgxmKtcjooXSPil7rA5buC11HSsFojMBRD3fKk4XvH047q8wVWIRdlUCa81tyd6XvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرنگونی پهپاد MQ-9 آمریکا توسط جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67553" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67552">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697775e593.mp4?token=DLYB9jRifYwpvhSTjYDl09_eReRTVcg1qppO2iO6XfL3Hav0kOkcl2vm913JVjBggqu4sxjj3yDNOJxvp_C9Hl6imjmiNuGggmyGZT6rDWX6LIu2HBcxrMb-oYIu5Zuo_Escgk0DzeedgmfSFPvdCd29v4TIqzqXfFe-iW8-iAUZieXx96qqq-KsI-PWF85sWZBUdWtSIu3nTPNck97j0duTOhh5cAnTEC6C9dngklKG6NKtC69mhLUmlLlvgHvCfgEtv42NaOVVo6W2h60gl5z6Gs_0Px-bh8aFK1T5vGx9BuUJMeDhv07iCpl1zwKW3f57yWFvcOh3Od8Usi5Wiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697775e593.mp4?token=DLYB9jRifYwpvhSTjYDl09_eReRTVcg1qppO2iO6XfL3Hav0kOkcl2vm913JVjBggqu4sxjj3yDNOJxvp_C9Hl6imjmiNuGggmyGZT6rDWX6LIu2HBcxrMb-oYIu5Zuo_Escgk0DzeedgmfSFPvdCd29v4TIqzqXfFe-iW8-iAUZieXx96qqq-KsI-PWF85sWZBUdWtSIu3nTPNck97j0duTOhh5cAnTEC6C9dngklKG6NKtC69mhLUmlLlvgHvCfgEtv42NaOVVo6W2h60gl5z6Gs_0Px-bh8aFK1T5vGx9BuUJMeDhv07iCpl1zwKW3f57yWFvcOh3Od8Usi5Wiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ پس از پایان اجلاس ناتو، ترکیه را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67552" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67551">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd068</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67551" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67550">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5OAT2MTMG_P4p5RTarooB6dZAZRbGdQ0SVufUM2L4ELigmAxIJqmUgPygo_dvqT1si4g2EVHaK4O4wKK8KyqegkCxolqGEtmWPgWiOYT3UgS-YJqjc81kcVLuM08lEhT1SZbTdSOdoOBZy3j8X6Y_w9_6BsbUeij7URcGcYwvykd-k2-NRClCy4Newilszsf2RGCbPhG9j29tkxmbrljwQPe2Au4CWNhoIJaWiz0t3wR1h6GkN8sIsrczbQwSCwiBmqLdA3Duqr_8JUM-2w0ftTvH5UGCONnlMgMMWUXbRVBQkVMJ1Ee37h4AkVdq5mkdQvThc9pL_mcP-jGK8xbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
عراقچی:
صحبت کردن با لحنی تحقیرآمیز با ملت بزرگ و شجاع ایران، از عظمت آن نمی‌کاهد.
ایرانیان به خاطر متانت، فرهنگ و ارزش‌های اخلاقی قوی خود شناخته شده‌اند. ما به بی ادبی با بی ادبی پاسخ نمی‌دهیم، بلکه با عمل: با شجاعت و با از خودگذشتگی فراوان.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67550" target="_blank">📅 21:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67549">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
گزارشگر: ماه گذشته، شما گفتید که رهبران ایران بسیار عاقل هستند. حالا شما می‌گویید که آن‌ها افراد بیمار هستند. چه تغییری رخ داده است؟ ترامپ: من آن‌ها را بهتر شناختم. آن‌ها بسیار عاقل‌تر از سطح اول و دوم هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67549" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67548">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/412c846bfe.mp4?token=AyhiY2j6lmJ-7KRQekiDQFKSCVXZcG4KZofuE68Phbuf55S38xMUK6BzcQ35CJQiNNcVV87PpFDVQWz5XupFjB2YfDG-49S5vFb5lPLzeTdnCSExpfG3bon4jo3VF8xYv07Zc6Simz9IC9dI5-NGf60me4SdDqktKfblyI4ZkXGtB9-418M4-gVAqsc-yuaR6Bqpm1fCdlxX482__TYv2PmKAEDArPXG_o0JESKlgOWNCjZxiQAak-Yj8Hw_WrDKc0YpH3JdD8uoQramKTXhW66meMEUmZV9M87xw7EYwxOfaM-F3NOLjUboSHUrr7F4CpS3eD8RYVpwd6evjaRqBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/412c846bfe.mp4?token=AyhiY2j6lmJ-7KRQekiDQFKSCVXZcG4KZofuE68Phbuf55S38xMUK6BzcQ35CJQiNNcVV87PpFDVQWz5XupFjB2YfDG-49S5vFb5lPLzeTdnCSExpfG3bon4jo3VF8xYv07Zc6Simz9IC9dI5-NGf60me4SdDqktKfblyI4ZkXGtB9-418M4-gVAqsc-yuaR6Bqpm1fCdlxX482__TYv2PmKAEDArPXG_o0JESKlgOWNCjZxiQAak-Yj8Hw_WrDKc0YpH3JdD8uoQramKTXhW66meMEUmZV9M87xw7EYwxOfaM-F3NOLjUboSHUrr7F4CpS3eD8RYVpwd6evjaRqBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ خطاب به ممدباقر درباره اورانیوم:
ما دوربین‌هایی داریم، که بخشی از نیروی فضایی ما هستند، که می‌توانند نشان شناسایی فردی که به یک سایت خاص می‌رود را بخوانند. محمد، چیزی آنجا وجود دارد که با بیل و کلنگ در حال کار هستند.
بیل و کلنگ به شما کمک نمی‌کنند. بزرگترین ماشین‌آلات دنیا هم به شما کمک نمی‌کنند. این موضوع بسیار، بسیار عمیق‌تر است.
اما ما این موضوع را زیر نظر داریم و اگر کسی به آنجا برود، منفجر خواهد شد. بنابراین، هیچ‌کس به آنجا نزدیک نخواهد شد. در نهایت، ما آن را تصاحب خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67548" target="_blank">📅 20:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67547">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8dc7e8bc.mp4?token=VcICOlxrB9pDIviBXa_a5exiHimTxnhXGT4z2g-SdujCQGX9GR4Ug0WBeb8g5_QI9sSc2z6h5ivnIk0DNAGIEUVDgkNOBr0ewm4-yT6hmf0BgAgvnhiuFo0T0O1O4vbI5sxyc4ZzK8du5Q2b7CQbHVo4WBregFAMXen-AEMDsb6nN1pSJ4UfeKsmZcDaCZldQbgVTaNCzu1YQAZ9LGWi65wn17k6xrc0uB01inCyTlzT0T8zI92GFaH3iESIMXbG8JA8L3-UazmlHb2RpZtllyECNUbLcOjNZfD4CsiFgDsaUmam_2EXUx8S2TmcXbQ_kHQ1a9wxDMnEJr9hNRj4GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8dc7e8bc.mp4?token=VcICOlxrB9pDIviBXa_a5exiHimTxnhXGT4z2g-SdujCQGX9GR4Ug0WBeb8g5_QI9sSc2z6h5ivnIk0DNAGIEUVDgkNOBr0ewm4-yT6hmf0BgAgvnhiuFo0T0O1O4vbI5sxyc4ZzK8du5Q2b7CQbHVo4WBregFAMXen-AEMDsb6nN1pSJ4UfeKsmZcDaCZldQbgVTaNCzu1YQAZ9LGWi65wn17k6xrc0uB01inCyTlzT0T8zI92GFaH3iESIMXbG8JA8L3-UazmlHb2RpZtllyECNUbLcOjNZfD4CsiFgDsaUmam_2EXUx8S2TmcXbQ_kHQ1a9wxDMnEJr9hNRj4GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
مطمئن نیستم که بخواهم با آنها به توافقی برسم.
ما می‌توانیم بازی‌ها را انجام دهیم، اما مطمئن نیستم که بخواهم به توافقی برسم.
فقط بیایید این کار را به پایان برسانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67547" target="_blank">📅 20:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67546">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d009a331.mp4?token=Q3rnrwJeBl-zUNu6uli4d0I-3Mhipwis2VjuQZUQyOAW3tdtr95j_xU_XXaBWHa8oN_o85TkCHlOT_xhlbeuhnmrj1Jwqgba--aLlxMlsVWNOmYanTWreToMdeju1qh2JihSaYErb3fP7VG0YAnculPWLbK93gaUME_-TuAOyLqTclEmrq4gexpfiffT2GWIGlRyoaQQmPQpr7d-SmGVCW3Q_e_YxwNRGtqsnc4o3JpZ0S89VZGEONiP-tUXxyHMqnO-sAvAGSqdkb-2N_FXRJ4g9dBX0f2-hcqRpDsUsLfixRqs8NU9ZcLvaD5Dd1qlXAMGwzMB0gKzdNKoDHaUFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d009a331.mp4?token=Q3rnrwJeBl-zUNu6uli4d0I-3Mhipwis2VjuQZUQyOAW3tdtr95j_xU_XXaBWHa8oN_o85TkCHlOT_xhlbeuhnmrj1Jwqgba--aLlxMlsVWNOmYanTWreToMdeju1qh2JihSaYErb3fP7VG0YAnculPWLbK93gaUME_-TuAOyLqTclEmrq4gexpfiffT2GWIGlRyoaQQmPQpr7d-SmGVCW3Q_e_YxwNRGtqsnc4o3JpZ0S89VZGEONiP-tUXxyHMqnO-sAvAGSqdkb-2N_FXRJ4g9dBX0f2-hcqRpDsUsLfixRqs8NU9ZcLvaD5Dd1qlXAMGwzMB0gKzdNKoDHaUFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67546" target="_blank">📅 20:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67545">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
من می‌خواهم این موضوع را در مورد ایران به پایان برسانم و با رهبران فعلی بازی نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67545" target="_blank">📅 20:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67544">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966c88b1c6.mp4?token=dp4aRMTsYSlm2PK-jTfV5or64ApNcXYhSrp8B14GJWWztFbGhuhIIg0ETjoG9e105Viy6_isrbh-nppSw2o28eFbq-mmXRHCCRLhlx4pim5QGw0nWD_8p60UhZ3CaiXg64EwaSKbcobwT_FVw__z-OMcFvlHnlk2dSbXvABRaKidw5_FMI1qtdUQxACoo5RTyxQ8Wboewjjmxdw747jKNy4kgW8SpL-9ULc-7BAZMjhzhRIj2sg-3TG6qP8YZwF5Y1vTgulmjqOinPRyPWUwL-qdnS_vLmzCEusoM1y9bfaHFgGoc50631SgoixvR09d3mczSAX-Ox2hsGoT6Gv4Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966c88b1c6.mp4?token=dp4aRMTsYSlm2PK-jTfV5or64ApNcXYhSrp8B14GJWWztFbGhuhIIg0ETjoG9e105Viy6_isrbh-nppSw2o28eFbq-mmXRHCCRLhlx4pim5QGw0nWD_8p60UhZ3CaiXg64EwaSKbcobwT_FVw__z-OMcFvlHnlk2dSbXvABRaKidw5_FMI1qtdUQxACoo5RTyxQ8Wboewjjmxdw747jKNy4kgW8SpL-9ULc-7BAZMjhzhRIj2sg-3TG6qP8YZwF5Y1vTgulmjqOinPRyPWUwL-qdnS_vLmzCEusoM1y9bfaHFgGoc50631SgoixvR09d3mczSAX-Ox2hsGoT6Gv4Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
هر اتفاقی که قرار است بیفتد، به سرعت رخ خواهد داد.
ما به دنبال راهکارهای بلندمدت نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67544" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67543" target="_blank">📅 20:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67542">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6daa8309.mp4?token=qKsXWddHFJdB6VH6F266pChSZC_IiVwvwNBwdW8AGuVjLnglfOg_oDAnCLcuX8XfZAQL_E5PP9kFGZB7BK0fDRJRH0aK38uHk7ivRWtxO677wguYfYiUCRxatAE9RDANTahh_iS3iIviv_vQqjEy6zqdljom_FsxajO2_gPGgg3EBOK5InPs_DhaBzPjHGi7X_NzkDX3jRiPoxtQWLRzSkCFoEiCdewUSbyySypavn4bXGLQbZ3bt45N9d5QxTEwwHJtFAjWozI13K0Xsth9z6BDFxONtJ-QBAoWp-kEK8xW72VxjcPN7DXY_HG_OZgeRumGrxjXw8FvV8QopaLriQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6daa8309.mp4?token=qKsXWddHFJdB6VH6F266pChSZC_IiVwvwNBwdW8AGuVjLnglfOg_oDAnCLcuX8XfZAQL_E5PP9kFGZB7BK0fDRJRH0aK38uHk7ivRWtxO677wguYfYiUCRxatAE9RDANTahh_iS3iIviv_vQqjEy6zqdljom_FsxajO2_gPGgg3EBOK5InPs_DhaBzPjHGi7X_NzkDX3jRiPoxtQWLRzSkCFoEiCdewUSbyySypavn4bXGLQbZ3bt45N9d5QxTEwwHJtFAjWozI13K0Xsth9z6BDFxONtJ-QBAoWp-kEK8xW72VxjcPN7DXY_HG_OZgeRumGrxjXw8FvV8QopaLriQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
می‌دانید؟ ممکن است من هم دیگر نباشم.
من هدف شماره یک آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67542" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67541">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0540439bf4.mp4?token=d5e-EcuONw19YMleWZc2UzirUL-4zO2OeAKXfvgl2cJ85FYVEC1h9TgEPgZlgkLauvACwy-gerYn8_USdSmfdCkyZZFiDacSfkcQX3d4r8OHhKt5KK8P3QHGQg3aMYEwSrdgn1nP-31jZhUVDcq-VJAAuG5mZUqnCV2ynQi3C8tDPvE70dW7q72fp7yiBT24M1WKgI258K_3B-kuyeJzZ7Qu0CxQegJBynhrNfJNqlm30aNwq7SGcJDlwDnYhOZozH0f-4A3_idRH9-X56Jalj4x0NfD7F4dkyBm6umgjvGQFO5ahdtsoq8Dayh6-SwcxMBbd4_q1KSyQ5vbToDnkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0540439bf4.mp4?token=d5e-EcuONw19YMleWZc2UzirUL-4zO2OeAKXfvgl2cJ85FYVEC1h9TgEPgZlgkLauvACwy-gerYn8_USdSmfdCkyZZFiDacSfkcQX3d4r8OHhKt5KK8P3QHGQg3aMYEwSrdgn1nP-31jZhUVDcq-VJAAuG5mZUqnCV2ynQi3C8tDPvE70dW7q72fp7yiBT24M1WKgI258K_3B-kuyeJzZ7Qu0CxQegJBynhrNfJNqlm30aNwq7SGcJDlwDnYhOZozH0f-4A3_idRH9-X56Jalj4x0NfD7F4dkyBm6umgjvGQFO5ahdtsoq8Dayh6-SwcxMBbd4_q1KSyQ5vbToDnkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ایران می‌خواهد به توافقی برسد، اما نمی‌داند چگونه باید به توافق برسد.
و سپس، شب‌ها به کشتی‌ها حمله می‌کنند. من این کار را دوست ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67541" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67540">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff03b3210e.mp4?token=p3V58Un3w4BUbgJ5cKjNoRsKg0DY2UppNEdhKH8BItR1xCPDpqepTSEOGrFsrjWCGzjC3GE3l_xMoVtTLPpxmTXgJXY8_6nUwkQQKovEvbyco6HoyZ45VmknKqJotrIDcu6W7i0zDsrcX9V5U78x_nyOTzHwF8LrMx73-4FN-xGMVyBnqiiJCYXoOR8SLqaOCMegdrDYepEJVwgDrj1jD9NDvrjlJhciUS-6C5WUQXk2cjL4833thvYjs8QIaicHgpeSKMSQuV7p1jtooq8KkObKI3O0BWKhfO-LXc3z7hreAwAnH2ZAHf4E2Gh4mpjnSre6vNE2I0TEUPWJsGSVrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff03b3210e.mp4?token=p3V58Un3w4BUbgJ5cKjNoRsKg0DY2UppNEdhKH8BItR1xCPDpqepTSEOGrFsrjWCGzjC3GE3l_xMoVtTLPpxmTXgJXY8_6nUwkQQKovEvbyco6HoyZ45VmknKqJotrIDcu6W7i0zDsrcX9V5U78x_nyOTzHwF8LrMx73-4FN-xGMVyBnqiiJCYXoOR8SLqaOCMegdrDYepEJVwgDrj1jD9NDvrjlJhciUS-6C5WUQXk2cjL4833thvYjs8QIaicHgpeSKMSQuV7p1jtooq8KkObKI3O0BWKhfO-LXc3z7hreAwAnH2ZAHf4E2Gh4mpjnSre6vNE2I0TEUPWJsGSVrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز، بیش از 20 فروند از ناوهای جنگی نیروی دریایی ایالات متحده در حال گشت‌زنی در آب‌های سراسر خاورمیانه هستند، در حالی که نیروهای سنتکام به ترویج امنیت و ثبات منطقه‌ای ادامه می‌دهند. ماه گذشته، ناوها و هواپیماهای نیروی دریایی آمریکا به صورت منظم در دریای عرب حرکت کردند و قدرت نظامی و توان آتش بی‌نظیر آمریکا را به نمایش گذاشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67540" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67538">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
ویدیو ای که سپاه از حملات دیشبش به پایگاه های آمریکا در منطقه منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67538" target="_blank">📅 19:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67537">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735f956d53.mp4?token=r9ztEvAxSiDlpOXw2CsKw6neUymRogI-M9_Qy7UtxEtz4P5SbDUF4S-pS77w0oqcUyMhT1YlPN6eBNBsbADcVksPvgiOp_MkmgiD2UfyNkwrNXAus1tMsPrcUIEj4-QS4jdk3JZFH9AOCyog_VOa7gGDcmVJg2CI8dVcmZlzMRQggOG-EMyBfkDOsjtsIKvXAGU-U0fHrpYn0URLoZWDCsFGlpnRrAyqmTFFJS_FfpjIZyG5AetMgw63PKK8cmUBw1AL0Kmead1aXMq9A0u4iF3IyMIqOEcyaa_LuWiPzVm1OilB9HlfkYqPm1TbN54OEDT9SN1Z81gJDjYpUx1Xlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735f956d53.mp4?token=r9ztEvAxSiDlpOXw2CsKw6neUymRogI-M9_Qy7UtxEtz4P5SbDUF4S-pS77w0oqcUyMhT1YlPN6eBNBsbADcVksPvgiOp_MkmgiD2UfyNkwrNXAus1tMsPrcUIEj4-QS4jdk3JZFH9AOCyog_VOa7gGDcmVJg2CI8dVcmZlzMRQggOG-EMyBfkDOsjtsIKvXAGU-U0fHrpYn0URLoZWDCsFGlpnRrAyqmTFFJS_FfpjIZyG5AetMgw63PKK8cmUBw1AL0Kmead1aXMq9A0u4iF3IyMIqOEcyaa_LuWiPzVm1OilB9HlfkYqPm1TbN54OEDT9SN1Z81gJDjYpUx1Xlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
صدا و سیما و رسانه خامنه ای برای اولین بار فیلمی از حسینیه امام خمینی در بیت رهبری جایی که رهبر جمهوری اسلامی مورد هدف قرار گرفت را منتشر کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67537" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67536">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
یدیوت احرونوت:
نخست‌وزیر اسرائیل، نتانیاهو، و وزیر دفاع، کاتز، حضور خود را در یک رویداد لغو کرده‌اند و در حال بحث و بررسی مسائل امنیتی مرتبط با تحولات مربوط به ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67536" target="_blank">📅 18:55 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67535" target="_blank">📅 18:38 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67534" target="_blank">📅 18:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67533">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f85ab468.mp4?token=OJF1o1JomfY2O2uXxjzovO9VXkYfBFwcth5RQBZXU7NdrSOpu_P2wZwoS31b8XhrjlSJ0dAF1i8J9zjdb_M_qLS8Q-VBaOuakZaIQxZawqclSkig2j3Iry8X65FB3DELZzODwTfzAzAlTX-uX_2f_7ghvwVk1lYFZynOnzaBnGJHyv0wG7-e30OwlwGEMxQllZZht8Sk6bLCLtp0X3H7J2oL1ro7Jh6uaTKo9TSMVyUrRF2wDXwcaKp-UF1qES6iVuXr4wll3dn9rY0I5wDzQ7Gn0QAsL-HXDwotPAC3hgMVrS3qtcAG_szeYaeCEgL5-ogE_QeNY_5s2UhsiDt8_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f85ab468.mp4?token=OJF1o1JomfY2O2uXxjzovO9VXkYfBFwcth5RQBZXU7NdrSOpu_P2wZwoS31b8XhrjlSJ0dAF1i8J9zjdb_M_qLS8Q-VBaOuakZaIQxZawqclSkig2j3Iry8X65FB3DELZzODwTfzAzAlTX-uX_2f_7ghvwVk1lYFZynOnzaBnGJHyv0wG7-e30OwlwGEMxQllZZht8Sk6bLCLtp0X3H7J2oL1ro7Jh6uaTKo9TSMVyUrRF2wDXwcaKp-UF1qES6iVuXr4wll3dn9rY0I5wDzQ7Gn0QAsL-HXDwotPAC3hgMVrS3qtcAG_szeYaeCEgL5-ogE_QeNY_5s2UhsiDt8_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره اورانیوم های غنی شده:
این مواد تا این حد در زیر زمین قرار دارند که هیچ‌کس به جز ما نمی‌تواند به آن‌ها دسترسی پیدا کند، زیرا ما تجهیزات لازم را داریم.
این مواد در اعماق زیر یک کوه قرار دارند و اکنون مشخص شده است که برای دسترسی به آن‌ها، به ماشین‌آلات بسیار بزرگ نیاز است که ما در اختیار داریم و هیچ کشور دیگری این تجهیزات را ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67533" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67532">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=SCPFjip0P7H3uU5XhGeqaY1cFRkDTqPYeZHkyQ5ySnEkPeYgq6oY-bgBTeV-X9T4seoL8qMa8_MJB7CicTOX2wjP0Ldqqe-Nlm8Tv8HBwi65F5gknsGM2hDg1SxKPB7iUUiNF1MCm1A071NSXK9AloFyN6ptTuAwAR7SUsp5eo2JgV50fWnFcGB3je1QNDDpznKKBeNsihZV8PH38d1aDuHNSC5bTh9I0y4i4W9lz94Mj1Iaj-6ntzO1eJZGPc73PzHko_J4V_vVrYuKtLZibLW-SDvKEE6W15ljdaUrHgHAiAC1lFvu0JC77JwqKKm9AUx6FNYN-z7yVlmeB_jPhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=SCPFjip0P7H3uU5XhGeqaY1cFRkDTqPYeZHkyQ5ySnEkPeYgq6oY-bgBTeV-X9T4seoL8qMa8_MJB7CicTOX2wjP0Ldqqe-Nlm8Tv8HBwi65F5gknsGM2hDg1SxKPB7iUUiNF1MCm1A071NSXK9AloFyN6ptTuAwAR7SUsp5eo2JgV50fWnFcGB3je1QNDDpznKKBeNsihZV8PH38d1aDuHNSC5bTh9I0y4i4W9lz94Mj1Iaj-6ntzO1eJZGPc73PzHko_J4V_vVrYuKtLZibLW-SDvKEE6W15ljdaUrHgHAiAC1lFvu0JC77JwqKKm9AUx6FNYN-z7yVlmeB_jPhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:   «امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»  @News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67532" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67531">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=osqsAOjB1rm5wysiF6Hnq2vkhAB2UE3iM_xeXnowZpj43CzUeSJJ2Wsk2Asj6UZpnkkBoQWHLcSiIwbIOZWCUuNRZEaKvMLy7gvmTgsm6qZKItlVm3vh9j-sR1pOU0GLW2bCeu7h9H7DuHm7OFGN6InlWoonPBaoRsJIATTqkdOSFUZaIxqB9VkaaYWJE1jhfDMvfYuxyuZT1xEDgAtqWNRVXFC0Rq0CriVO7J4eMKguUj3gSqJ9jQGKLWmTQmo0YO4D5NAnGmHxiQc4ZJZPYroK3x34v7Yd-OtXTJ0FFkTOwu8-3Qi5hj-bfXRoE3SXqXIDmr6CJD-448Bjr963WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=osqsAOjB1rm5wysiF6Hnq2vkhAB2UE3iM_xeXnowZpj43CzUeSJJ2Wsk2Asj6UZpnkkBoQWHLcSiIwbIOZWCUuNRZEaKvMLy7gvmTgsm6qZKItlVm3vh9j-sR1pOU0GLW2bCeu7h9H7DuHm7OFGN6InlWoonPBaoRsJIATTqkdOSFUZaIxqB9VkaaYWJE1jhfDMvfYuxyuZT1xEDgAtqWNRVXFC0Rq0CriVO7J4eMKguUj3gSqJ9jQGKLWmTQmo0YO4D5NAnGmHxiQc4ZJZPYroK3x34v7Yd-OtXTJ0FFkTOwu8-3Qi5hj-bfXRoE3SXqXIDmr6CJD-448Bjr963WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:
«امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67531" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67530" target="_blank">📅 17:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67529">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=Wua1B14EPDUPSp3gkrfhwEd3CufQizQVyWCiFjzjbZgEMo5DJYjP5tWsg-QaxxmsPc-4RloAz1W-A2haMjHvri5F8tyhevsa3Mt66RdrioBnyIsTZXMLKoyembcTTytVXM4J0nJUJEt8ZhJFRQdBA7jGchqYbOC2H57zWPryRsp79LQspVet6DGWfxFOB6kMp_-0SYPOJJJ1ji4-ap5tCntV0sRhC7ESmKCCSzUvNlhdRRB5dAaeu5ISzN0YD4oDM4-KYg4T0652EXEnewnmF9sGayRPiDjmpu0uvxmyITgMW-kb9ToMGxQ6E_U0dA1cYicPtI10T-IxLH_a0c5Vog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=Wua1B14EPDUPSp3gkrfhwEd3CufQizQVyWCiFjzjbZgEMo5DJYjP5tWsg-QaxxmsPc-4RloAz1W-A2haMjHvri5F8tyhevsa3Mt66RdrioBnyIsTZXMLKoyembcTTytVXM4J0nJUJEt8ZhJFRQdBA7jGchqYbOC2H57zWPryRsp79LQspVet6DGWfxFOB6kMp_-0SYPOJJJ1ji4-ap5tCntV0sRhC7ESmKCCSzUvNlhdRRB5dAaeu5ISzN0YD4oDM4-KYg4T0652EXEnewnmF9sGayRPiDjmpu0uvxmyITgMW-kb9ToMGxQ6E_U0dA1cYicPtI10T-IxLH_a0c5Vog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
آنها توافق کردند که هرگز سلاح هسته‌ای نخواهند داشت.
و سپس، آنها به بیرون می‌روند و می‌گویند که ما هرگز درباره این موضوع بحث نکردیم.
چه کسی باور خواهد کرد؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67529" target="_blank">📅 17:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67528">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=aZC6i0h5u0_PdZaQPrZd2wd09T7m7g2L72CM3F0Fzh0BK02T6xM7orbatmdSaasq_Gqmy5219uJR7Wma5_fB0EfV20mgTh_pfAH5v3jSjftuS__Xp-xMqLtYEgP-JFHzWd2ZXSvUU-U8TayyI-tTIBLKQo8b8dXPeWASiXYzoxLHcSJsvULKN_GbhDBPUTdoub1VvWpQ_GH-Nn0N4KveHSQor9p_AHUp8GIougmGnYJwUEhlbvNzKjE36l644mhIzxFO1_gkseB_9PsGAkbDQJw9ID88t_KyTaGxeLqSjinwGBKQGHm04w6s0WfUhSRyD7r129Lzw65RVErzkppHhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=aZC6i0h5u0_PdZaQPrZd2wd09T7m7g2L72CM3F0Fzh0BK02T6xM7orbatmdSaasq_Gqmy5219uJR7Wma5_fB0EfV20mgTh_pfAH5v3jSjftuS__Xp-xMqLtYEgP-JFHzWd2ZXSvUU-U8TayyI-tTIBLKQo8b8dXPeWASiXYzoxLHcSJsvULKN_GbhDBPUTdoub1VvWpQ_GH-Nn0N4KveHSQor9p_AHUp8GIougmGnYJwUEhlbvNzKjE36l644mhIzxFO1_gkseB_9PsGAkbDQJw9ID88t_KyTaGxeLqSjinwGBKQGHm04w6s0WfUhSRyD7r129Lzw65RVErzkppHhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
جمهوری اسلامی ژاپن دیشب به ناو هواپیمابر ما حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67528" target="_blank">📅 17:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67527">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=Oci8ap_G9t9XPLGX0X6-Mpy_lJTtFFpr-Fgp7nYpxIyiT7KbFa7U-EXHeKpe6aNK1F4cQClQ7pXs-cRloDfr8Lrg0T78T6ok1IfLS0zHQJPQZh6JjtTcoUjwQWd3goKPUszTRmzDX4nWx0UPL4UWMNDwM-hj4IfzTUxVWy_sav6HVjWytVkbnCue58VQL7S2b9kv_SP1j6ph4M2lqVlnXtVxtv9ZI_CjW7pb742q4CaxCEhLVUXaRqyZz-AHQXUz-VmDZ31MeD0o9qulDQcvKB2lDKngBWLvWcchbSrjas9zdOj3R5weh4tEwa8Cpzd6EgdMGqqih63bMkfBgHmMlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=Oci8ap_G9t9XPLGX0X6-Mpy_lJTtFFpr-Fgp7nYpxIyiT7KbFa7U-EXHeKpe6aNK1F4cQClQ7pXs-cRloDfr8Lrg0T78T6ok1IfLS0zHQJPQZh6JjtTcoUjwQWd3goKPUszTRmzDX4nWx0UPL4UWMNDwM-hj4IfzTUxVWy_sav6HVjWytVkbnCue58VQL7S2b9kv_SP1j6ph4M2lqVlnXtVxtv9ZI_CjW7pb742q4CaxCEhLVUXaRqyZz-AHQXUz-VmDZ31MeD0o9qulDQcvKB2lDKngBWLvWcchbSrjas9zdOj3R5weh4tEwa8Cpzd6EgdMGqqih63bMkfBgHmMlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ممکن است محاصره را دوباره اعمال کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67527" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67526">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e08b208584.mp4?token=XGdSmLzqSGk0oOvlv_gkm4E77RvJDRZk0TgH2XADm95sBZnkqfL_ayAkHP5taavOvknuvXcy9anamH9CGB8FvyiaIFjXIEAXMkq_zqkx4Hx-Mki24ghBAWPg_tryCVJB8XQVhNy8vLbJlhTo0iqLBnxPGHm2JTJustiHPbrkKtAFi44-Uxqzy4Fti16Kp8Sbnp0VpJJEFUreDE50PIAjz8fsyeHiXQjcgydgS_RfFl8me63QYYijtoZ6asXJBNoHkCsuVnqNivvVkKNpI5eMRhsZNoHWLZ-G4fFuoIOMNVXDlbzLGvMnvWTYFwn2mKBtc9Pc5icR8KlGSurYQaG2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e08b208584.mp4?token=XGdSmLzqSGk0oOvlv_gkm4E77RvJDRZk0TgH2XADm95sBZnkqfL_ayAkHP5taavOvknuvXcy9anamH9CGB8FvyiaIFjXIEAXMkq_zqkx4Hx-Mki24ghBAWPg_tryCVJB8XQVhNy8vLbJlhTo0iqLBnxPGHm2JTJustiHPbrkKtAFi44-Uxqzy4Fti16Kp8Sbnp0VpJJEFUreDE50PIAjz8fsyeHiXQjcgydgS_RfFl8me63QYYijtoZ6asXJBNoHkCsuVnqNivvVkKNpI5eMRhsZNoHWLZ-G4fFuoIOMNVXDlbzLGvMnvWTYFwn2mKBtc9Pc5icR8KlGSurYQaG2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
آنها به ما گفتند: لطفا در مراسم خاکسپاری ما را نکشید. من گفتم که این کار را نخواهم کرد، و ما هیچ اقدامی انجام ندادیم.
و سپس آنها به سه کشتی حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67526" target="_blank">📅 17:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67525">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=TZ_8Ks0eNlX-b0P-vlZTD681mEAucBbRkMDy2Q_zKnBvpwRuX0OmrNa3ylZuE_UwFBK0FVzOjjgsDlGUeQBFvmV4T0IZREnLLdXHNvXq_pKhEOuz02I3NY6bv4PfFMGgTl04M5WuJ87jl9mb-7Ra7LFJzUoLBm2vzVnJ88_vYuPvlg82fmJJr-d3tdbCRwfDbNJZ9IwIo1eT-fSbkAVTzk1UJFDAvORApLi3i9io2WuWDWGCDAjWWQJA-cuchrDgghz0DGOa4gxwqXDa2fsdmkJPVNu7AH9pDceNHDUInXLrJA84MNpDumkiscxzuiohMNca9_ZbgvQ7_up_axzjcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=TZ_8Ks0eNlX-b0P-vlZTD681mEAucBbRkMDy2Q_zKnBvpwRuX0OmrNa3ylZuE_UwFBK0FVzOjjgsDlGUeQBFvmV4T0IZREnLLdXHNvXq_pKhEOuz02I3NY6bv4PfFMGgTl04M5WuJ87jl9mb-7Ra7LFJzUoLBm2vzVnJ88_vYuPvlg82fmJJr-d3tdbCRwfDbNJZ9IwIo1eT-fSbkAVTzk1UJFDAvORApLi3i9io2WuWDWGCDAjWWQJA-cuchrDgghz0DGOa4gxwqXDa2fsdmkJPVNu7AH9pDceNHDUInXLrJA84MNpDumkiscxzuiohMNca9_ZbgvQ7_up_axzjcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما شب گذشته به جزیره خارک حمله کردیم.
ممکن است کنترل جزیره خارک را به دست بگیریم. هیچ کاری در این مورد نمی‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67525" target="_blank">📅 17:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67524">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=FmgE8KtTIo1S8WTlnEtRVmGMRkHEgtxa0qKTiBKtWghi42DINp_Yz-cxcinF2QiJAh2z1PUZiOXIfDofQQs53vEHDaTIvMG3Adr33VOoTpOFll3p3lUiU86zP1ZbAvTpT4CcUXlgzHpgL8UDlT4tnrZHXtcK_pOxR9oFEEhOqie-EEd9wsHlcdtZhVAz5Mj4XurO2aFbt-7B5vT7bctZZrHHMU53oM7ULRXqoRQd7L6FXi2A1ZWg0UE2vhWYykWH_Jzb0wNRK_wuWogF-GHzKYx62xaYiQDTR0WvLD7k2j98h7Q0sLBJmEPqCrX9UH1bh5jpx_zOs0ucl3rRvMb2_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=FmgE8KtTIo1S8WTlnEtRVmGMRkHEgtxa0qKTiBKtWghi42DINp_Yz-cxcinF2QiJAh2z1PUZiOXIfDofQQs53vEHDaTIvMG3Adr33VOoTpOFll3p3lUiU86zP1ZbAvTpT4CcUXlgzHpgL8UDlT4tnrZHXtcK_pOxR9oFEEhOqie-EEd9wsHlcdtZhVAz5Mj4XurO2aFbt-7B5vT7bctZZrHHMU53oM7ULRXqoRQd7L6FXi2A1ZWg0UE2vhWYykWH_Jzb0wNRK_wuWogF-GHzKYx62xaYiQDTR0WvLD7k2j98h7Q0sLBJmEPqCrX9UH1bh5jpx_zOs0ucl3rRvMb2_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گزارشگر: آیا امشب قصد دارید قایق‌های بیشتری از ایران را هدف قرار بدید؟
🔴
ترامپ: معمولاً این موضوع را با شما در میان نمی‌گذارم، اما می‌دانید؟ آن‌ها هیچ کاری نمی‌توانند در این مورد انجام دهند، بنابراین احتمالاً بله.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67524" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67523">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f96f01d100.mp4?token=QvSz1qCPRrE4TNI_nNpmr2vi8yHUCdX85qXHNR5md4WY2Y6I3G8Q1ftfOpk-yirgbuaT48-6JZN51UvULIciuWuXCOvouGfZg6JmHMpZtzI5AdpUp4Ki9Nagtdkm-4_2UhcWJ_icHHWotHxWP9uRPxzn1KUtlkodRzSmlCjTK186nNJKioVQZod3lS_qNTqsx2yb9tBWDt9-oy-FOwpJBIiY0cWxqPagHzxF0ED1qYddbiygJP1XJT_J9cx2qLzv7-T8rmJdJn9SBRrszalx8yhZcbSOC20ipuovUbMXyY1LyO3lfJKk7lQexoe3fIotYUsVuT54y42XDZaM6sGPTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f96f01d100.mp4?token=QvSz1qCPRrE4TNI_nNpmr2vi8yHUCdX85qXHNR5md4WY2Y6I3G8Q1ftfOpk-yirgbuaT48-6JZN51UvULIciuWuXCOvouGfZg6JmHMpZtzI5AdpUp4Ki9Nagtdkm-4_2UhcWJ_icHHWotHxWP9uRPxzn1KUtlkodRzSmlCjTK186nNJKioVQZod3lS_qNTqsx2yb9tBWDt9-oy-FOwpJBIiY0cWxqPagHzxF0ED1qYddbiygJP1XJT_J9cx2qLzv7-T8rmJdJn9SBRrszalx8yhZcbSOC20ipuovUbMXyY1LyO3lfJKk7lQexoe3fIotYUsVuT54y42XDZaM6sGPTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انگار یه نسخه پرمیوم از ایران هم وجود داره که فقط مخصوص پولداراست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67523" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67519">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLlsHLqDdpoSMhTIX5l28aOmedtHwI9R7ZM8F3bYGeNIPBGEvtJ-1eLwptoas6P0yvNUs5kqzARNa7inmJ230x74UNvN2AS9BVpkBa3A8gEAJMVwogpcZ1uh65Jr44ZBaN-3RzeBbb4HKOt4nK8vzNF9TCquwdEmru8L4_E16-PhJxGPzorpDiADqwZcAbTOAvswXuwEYb1XjXt23kgVbzaPSFzfqCSxspQkNFzhSPYPDnjMKfIEIGEpTAFpE-pdBsVbSw_u18DbEMV-oN2au2513T5SEz2_98QwulgN7HsN2Y9lJCPM9QkicPidT8Pzq05SNT4aUnG6FpgSbGK5ZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67519" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67518">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rA_U1QwQEDalu6YrZiDlKIYCdfKusmN0C9Uq5ydNuTPdff6xjEp3gJMBOvMGyqQoDxwUpP0qO-fG4zU_ybV2OGN2Ppg-DSV8uZvQL_YJiHjuFq08D32oqwfSE5bcP9SOtyZ9e4i3Ybdd-cfHf-xwpmn0szeL7sh3kEURcqLu49F5zaVmzw6ptp_Ayf3O6KQsYlXC-3EPKFvX_dH-J6mK7m0wIlOoma44ZFLA2G1f3JnWC3menlwTXWXtzSpI6RyMvPGmjMPjOKkd5B64m3fbdqY29arZ3luywlYSL9I5qgtZmKPtkqtVatbojyGPPsS4XAl-Yau8W81zqoyKIxWXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری هادی چوپان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67518" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67515">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKAAuT50zr89S2zH9-D6XAtBmZZFv4voczpAYohFZQMVjEStuL8RJxShjBSkox6GYTe0as30x4YvZfH0cgGvPsWtf2dypQ8H_X5j50hVMm19sSFyY_K0Dl_ysjaN2LGdkoshsjpuIQSCUHv695CfcFPDyC4ix8riyLYyFohoLS1-n9FWRqEDt72_afPO6oucxQdcvZN1p08NGPlHf_It9lTkCxgm5kEc0NF2Zrw7qkxV70DDCW-oKZzx49QhptBzJPaSuq9IbMwkKvNiubAoiVyomFL_n74zRVa_HAOSQQgVY0_LLIDlGJd6aTwTpjSKdTYDrS8TF7zUcH81G5NILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKuuigbqGpjOp9CF2zvdn19qBAun6gXMhQmpPjgoBQjisSiNNt8FIhkklIpqEoN1EAaKL5_XK4V8_jFNWvzPVcWnOurFnlqgnZ1ZnZ5U-jHrxLGBzi6TCtOkWGDnZsYZdXjsvQH33mmGjM9Yc9PXI1XQX-G8LcqAVAnPkO9gdydf-A608LGc1XW1823Xj-ccIfnhPxzoLHTBfdgK2jpTmdOap0OtBzQr_-26oazU7_kdNsEn__14yF6be0deoLwVKiwb7oUMM8o9WF8lIBQ7HlQC_pbG67QlCVroNAL8B1ukjb19F-4vYdrpha5A3mEyguhd9bLni7V9XJRR6uVaNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e58f00c0.mp4?token=lE1ikD8Ij0VpCFwMOnJV7gwEOXBuTx7WQoMiyoxfxpip_fFFqdxib_YXwUfyaTVpyVbDZ0-Paqio5M7Dv2WvZIrWgFzYZJOmIqEk1X71OFhKYYGWLJKQR7TFGjcpoLHEYAg3fCzSRg-rKm5aqqoNEaB4iuOFWTbUK2fHyzjKfhtFg_l76vpae30TK3YsB7MKaoZ8cTLM67q4appUl3Jod5EEIRocD-izCT3zgFha0579CMdJLjMoMDciby8XwhSNjiCJrkHvVEOyYgvgMHJrNRxMQPOE25lqItpn93XhsnjSqDgPAP7PyHIFVnZIBkueA9tjF8H7vYEkUCdc4C2mKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e58f00c0.mp4?token=lE1ikD8Ij0VpCFwMOnJV7gwEOXBuTx7WQoMiyoxfxpip_fFFqdxib_YXwUfyaTVpyVbDZ0-Paqio5M7Dv2WvZIrWgFzYZJOmIqEk1X71OFhKYYGWLJKQR7TFGjcpoLHEYAg3fCzSRg-rKm5aqqoNEaB4iuOFWTbUK2fHyzjKfhtFg_l76vpae30TK3YsB7MKaoZ8cTLM67q4appUl3Jod5EEIRocD-izCT3zgFha0579CMdJLjMoMDciby8XwhSNjiCJrkHvVEOyYgvgMHJrNRxMQPOE25lqItpn93XhsnjSqDgPAP7PyHIFVnZIBkueA9tjF8H7vYEkUCdc4C2mKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه تو ایران با سنگ و چماق میفتن دنبال عباس و میگن مرگ بر سازشگر ولی تو عراق اینجور نیست!
مردم عراق انقدر عراقچی رو دوست دارن که اون رو تَبرک میدونن و خودشون رو بهش می‌مالن تا حاجت بگیرن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67515" target="_blank">📅 15:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67512">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pwq1dse3mXdJ6n9YQ1Jw2MSVClAT8vcPj6kw-96vsLd7tKXt7JZdvxklh0cqYA6tEMI1LKgIdBTBXSYIKY-gxqJMTRphSehOAYaY_kP-WMkkL8Yxhi1GKnUKWjk6IF4BoKxo7V2m5IGZTZrSKHtX63WpVLRbizYIaE1JnrJ8v0QgAANkbi_gT-CwEBpKMQBLjBGHbi4iWjFjz-L96g_zGNaI7qCwHIdlTMWNyLSR_r_yW3fsmuJ9-envcxWKJHN2ILbt0s0J1qM2b2Y6M_hgwkz97ppIF-pF5uroSmLNYmxv_7yMduDmFNL8_H1sYE8OEs0V__QHK0Wb4HgM6btehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOdY2hW3BsuXsOo4CcDkjTzPfB8aZ5j0qvQPzwmdhqH8WUKwun8JZ6vy3mCMJLyYBhSaYdS5_X24teCR5ju_DnTK5gfB35aXhyoyVCQyyVH5T7BvJgohLe20xX7R9F8QCl3CJIWwSmxBsEqxKbSkNhPs8pM5YBixN1ulu7mwqvil-lsOO_e9pG--xjigJj5YdfClgd2Z6LZqRhB-B83JChTtNGwM47F9QtfO6LGfcH1M6vqHrSGC8FiyJK4tOZd0-SP19MOziIyi7cIWzospS3pqNaRPf699jByG83VZYkQs4FKaCpdSgA48pJNYPG4TG1kZtUP_n3AphG0O8a3Efw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hi8Xeb7BGty50k5lNjrLM8je8E0rYaevmopVcUNilOsnwDbTvUPVnDSsBQ6mm7Y0ay6dJI17eFY2Bi-qBxJrSWhnyYOWGa3y32aShvGGym30PjbO58y9qFWxnECCTjvkeU2-QXnkoKfDmUXltmxjDY9Q6HMYIgJ9qY_7K9RLpUqEmU2mgWgT-UOZe-zeXMtxs6vGhSpyEfEb6PDSft8t05NzL0B9w1W0B_0LFfKpHRrmiXCRpMRPtFW2Q0-yUy0SriythFoXY_6bfwbNw3o4tYkvduw_jVGHEuF5_S-t5ktBDPeSkcHGhuc93xIqOrRnuGHQ3j_5OwaeltO_TW_IXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
خبرگزاری تسنیم اعلام کرد یک پهپاد تهاجمی MQ-9 آمریکا در آسمان بوشهر سرنگون شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67512" target="_blank">📅 14:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67511">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=tAqNvsBqRx7ldShVMeMF38_vCol3VfGmN4topvE2tlAwHi70SB6VyGzg9ygzF_OI8iWJaBqitjacWAcMKOE9FUG_j2BVH64MmhsRuNOjMqB1jWtqL0tfFDVz2d08sqjJVIKQ0YM5rEAuE65t3r9H10sfKTz96Gb29WzJmGpreKvCRHv5aiAMG0Bv7uLsc7XNjqM9sDeQrje_s7VJRA9Q7fttD7vOgbRXyVt3CemJjHwXoYlikUakfdebTvJkYrwaGDqSI1eyNbFcMPedgnGrd27c090bVGjTzMgmLSjYTPTQRDqrm6orBwwx54ycyfdouNxhY6tQvianMuEcYkyKBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=tAqNvsBqRx7ldShVMeMF38_vCol3VfGmN4topvE2tlAwHi70SB6VyGzg9ygzF_OI8iWJaBqitjacWAcMKOE9FUG_j2BVH64MmhsRuNOjMqB1jWtqL0tfFDVz2d08sqjJVIKQ0YM5rEAuE65t3r9H10sfKTz96Gb29WzJmGpreKvCRHv5aiAMG0Bv7uLsc7XNjqM9sDeQrje_s7VJRA9Q7fttD7vOgbRXyVt3CemJjHwXoYlikUakfdebTvJkYrwaGDqSI1eyNbFcMPedgnGrd27c090bVGjTzMgmLSjYTPTQRDqrm6orBwwx54ycyfdouNxhY6tQvianMuEcYkyKBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
احمدی نژاد : بابا داره بهتون فحش میده،یه مرد بین شما پیدا نمیشه پاشه حداقل بگه خودتی؟!
+ترامپ امروز به مسئولین جمهوری اسلامی گفت آشغال،پست فطرت،کثیف،تومور سرطانی، شرور،بی‌ کفایت،بی ارزش،بیمار،روانی و حقه باز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67511" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67510">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
رسانه های عبری:
ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67510" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67509">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUdqzvFIfg-HXtUeOACg51v-oUujTEqSnr8tzNojWI0p72lELZsYPgnZGL-c2NtJX_dHQ7uEpDPk1rSZesCQy_ScKX4UI4cPxzKzNtI5L03TZZbgFuzhgjPjyMVqFlDm4ZPM2_YJKGPjoYoc0_wZfo68hDRZoDPP8HLHx-Tgmqqxant3T0MXksfmZTWhvmjtDaBGFg0gftGx4yo4SkJcoz8r8KtBglyvlQIn-x54LgARY9Bon8EYYKGTxONOAuGnbfAsQ4I0Xc6y9Bv3_F76iF3zuJ5FP9_ERK7T7pco7tNc00dhbHm3eeXhWQv4kMai6NPHErwlSRFil5G2F1FPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
پزشکیان:
رفتار دولت ایالات متحده به عنوان میزبان جام جهانی، همان سیاست خارجی همیشگی آن را نشان می‌دهد: زیر پا گذاشتن قوانین، زورگویی در برابر رقبا، ایجاد موانع و تقلب. این همان روشی است که آن‌ها دنبال می‌کنند. ایران چنین بازی‌هایی را رد می‌کند. ما به طور قاطع از حقوق خود دفاع می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67509" target="_blank">📅 12:55 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
