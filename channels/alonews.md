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
<img src="https://cdn4.telesco.pe/file/cWt925GrnxF4zF43HIMG6F-JqYuH6Z0sAzTmmTaqoXb4CrSNVDqz5amntQOmdLjz8xuCtyorfO32Zl5AeadZ-YmkYx1u3hvpTzKepk0xB33qSgIOc3irTnE9qRIkWZu-obe-qOG0HFTxtncJaoL7xbbg0UxPZg8GXqOYjmtGIVjLr-XUMi-Z5LKqhR319AyEnDJogkFJJfV-BEmEoaF7thlVpR2AYrmGaJVf8hU9MJ7SSBjXQlxEkNs_6Gm0FbiERGkdnQAyapB7PdtdH3kqfV773y9Hh2snooNJVSDAuJ1Atjjak2Rz61WYxxmz_diX-EKUNPCbd5cghMbUib9iLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 961K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 21:45:51</div>
<hr>

<div class="tg-post" id="msg-129212">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/821720cf8d.mp4?token=gR07FM1ovo0_P_fDNytoJS89FUNXPlC74m7-W4O-nKdUGyijqgH0-LSYo0ZBt5mYIufNxJSxfrM0Qrejf6px9odNuuPY2c4pUv4TMQNPaYRO3-pfm5LdKPDtF6QrsZpJQdz57KDF8IJ66pPJrE-YVjAVhrO6fFMkZ6wtMWMiWRuQUtvvUZZh_L9lT7Ld6ocSuclFqAHDye4K5z2rnquFDLoRP8ZM-irSEjJEB1NmqWeoJIXQ1Bf3og8QtoV-FSBY3p8qRHEa0iml7wslnuNQmSrjeYTk0hyWIR5NoeE6oLLmGoQtJb8QCzEGIFkaa0L8RzxpTw-zHh4kv6MipT8CYYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/821720cf8d.mp4?token=gR07FM1ovo0_P_fDNytoJS89FUNXPlC74m7-W4O-nKdUGyijqgH0-LSYo0ZBt5mYIufNxJSxfrM0Qrejf6px9odNuuPY2c4pUv4TMQNPaYRO3-pfm5LdKPDtF6QrsZpJQdz57KDF8IJ66pPJrE-YVjAVhrO6fFMkZ6wtMWMiWRuQUtvvUZZh_L9lT7Ld6ocSuclFqAHDye4K5z2rnquFDLoRP8ZM-irSEjJEB1NmqWeoJIXQ1Bf3og8QtoV-FSBY3p8qRHEa0iml7wslnuNQmSrjeYTk0hyWIR5NoeE6oLLmGoQtJb8QCzEGIFkaa0L8RzxpTw-zHh4kv6MipT8CYYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مودی: مودی بسیار خوب است. او از جنگ‌ها دوری می‌کند که هوشمندانه است. ۱.۵ میلیارد جمعیت دارند. هند در واقع بزرگترین است. مودی رهبر بزرگی است و ما تجارت زیادی با آن‌ها داریم، اما اکنون تجارت عادلانه انجام می‌دهیم.
🔴
آن‌ها قبلاً واقعاً ما را کلاهبرداری می‌کردند. من آن‌ها را به خاطر این مورد سرزنش نمی‌کنم. ما سیاستمداران احمقی داشتیم که اجازه دادند این اتفاق بیفتد.
🔴
اما اکنون تجارت زیادی انجام می‌دهیم. آن‌ها از این موضوع آن‌قدرها خوشحال نیستند. آن‌ها قبلاً خیلی بهتر عمل می‌کردند. اما مودی عالی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/alonews/129212" target="_blank">📅 21:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129211">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سلام، نخست وزیر لبنان: ایران زور اتش بس آوردن برای لبنان را ندارد. این امر فقط توسط دولت و با خلع سلاح حزب الله محقق می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/129211" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129210">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4536cbb7a0.mp4?token=FLd3oETJBfy6kmqcj6mC88CYbb-VSp0Q00N4xSKLkhKHJEkLEl3994IA1DZ2nDSgK3D7YXfS5N-Jz5UzhbRi3MnUciVxk6tBKu5cmfC2eRBr0-cK9w9BK9HKHeWzLnQ965sxpFRdeqiOx9PmvX078G7sCAWAqV507VMyzCpRZhRbEdFcCNpVlePUbgsocIxg1Y__irF9A8a3gA51dPs73-d2EdzV6ie80yiGMZlpVffsnbQFF8mEZBM1MZgOrCeJhpbMX87etg5vpdqcgLWgFavAYdfKZgAu3VWAYxgIHRyUco6IQuEIR3va76p-WiBx5f-Ei2voFBiXMFEz2IPeQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4536cbb7a0.mp4?token=FLd3oETJBfy6kmqcj6mC88CYbb-VSp0Q00N4xSKLkhKHJEkLEl3994IA1DZ2nDSgK3D7YXfS5N-Jz5UzhbRi3MnUciVxk6tBKu5cmfC2eRBr0-cK9w9BK9HKHeWzLnQ965sxpFRdeqiOx9PmvX078G7sCAWAqV507VMyzCpRZhRbEdFcCNpVlePUbgsocIxg1Y__irF9A8a3gA51dPs73-d2EdzV6ie80yiGMZlpVffsnbQFF8mEZBM1MZgOrCeJhpbMX87etg5vpdqcgLWgFavAYdfKZgAu3VWAYxgIHRyUco6IQuEIR3va76p-WiBx5f-Ei2voFBiXMFEz2IPeQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس در مورد توافق ایران:
منتقدانی از این توافق بودند که می‌گفتند ایرانی‌ها هرگز اجازه نمی‌دهند تنگه‌ها بدون عوارض باز باشند.
🔴
در دو روز گذشته، ایرانی‌ها به هیچ کشتی شلیک نکرده‌اند.
🔴
دیروز، ما از تنگه هرمز نفت بیشتری نسبت به هر زمان دیگری از آغاز درگیری خارج کردیم. و حتی یکی از این کشتی‌ها عوارض پرداخت نکرد.
🔴
بنابراین، منتقدان این توافق در مورد برخی از آنچه می‌گویند ایرانی‌ها به دست آورده‌اند، و همچنین در مورد آنچه ایالات متحده به دست آورده است، اشتباه می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/129210" target="_blank">📅 21:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129209">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
اوباما در مورد توافق: توافقی در حال اجرا بود که در آن ایران توافق کرده بود که سلاح‌های هسته‌ای توسعه ندهد.
🔴
این دولت — یا نسخه‌ای قبلی از این دولت — از آن خارج شد، که باعث شد ایران در آن زمان ظرفیت هسته‌ای بیشتری توسعه دهد.
🔴
ما اکنون جنگیده‌ایم، میلیاردها و میلیاردها دلار هزینه کرده‌ایم، فشار عظیمی بر ارتش خود وارد کرده‌ایم، بسیاری از مردم کشته شده‌اند و به نظر می‌رسد که به جایی که قبل از شروع جنگ بودیم بازگشته‌ایم، شاید حتی کمی بدتر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/129209" target="_blank">📅 21:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129208">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e467c88758.mp4?token=IG3asSTBZbeoibjv4-rmJblSTBv0Duevd3Yr3II09bEZ1yI9PzZgXTy7IKVs0tC0i2Wut17VCJn7X96IpPWg9eROXT30BHjjrhJoJhte_kIomN6Rm2ktgKjwNqvxF4kYHJfQowF5RgupU4o_4y2ICiMggXHDg-c69_YbWmmjF5j1nN0RB4wMoeB3q5NwXG9NQH4FajlKSgV7oBdC1Y4JGv4S9_z3HkO4pM1wpn5Gs-QKI9_khgoMTs1mKLIfVT61v5INmR7XQV4iQ9ckCBg2Iufe9rhJzYmtQPKYOm3zuZr_dA5_RtY1VHkLbnenBCihd41Yenjl2IELwLRQEdcrMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e467c88758.mp4?token=IG3asSTBZbeoibjv4-rmJblSTBv0Duevd3Yr3II09bEZ1yI9PzZgXTy7IKVs0tC0i2Wut17VCJn7X96IpPWg9eROXT30BHjjrhJoJhte_kIomN6Rm2ktgKjwNqvxF4kYHJfQowF5RgupU4o_4y2ICiMggXHDg-c69_YbWmmjF5j1nN0RB4wMoeB3q5NwXG9NQH4FajlKSgV7oBdC1Y4JGv4S9_z3HkO4pM1wpn5Gs-QKI9_khgoMTs1mKLIfVT61v5INmR7XQV4iQ9ckCBg2Iufe9rhJzYmtQPKYOm3zuZr_dA5_RtY1VHkLbnenBCihd41Yenjl2IELwLRQEdcrMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس : باز شدن تنگه هرمز دلیل این است که قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار امروز کاهش یافت.
🔴
و همچنین دلیل این است که قیمت بنزین، همان‌طور که صحبت می‌کنیم، برای اولین بار از مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، زیر ۴ دلار است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/129208" target="_blank">📅 21:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129207">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
دبیر سرویس امنیت ملی اکسیوس:
یک دستاورد آشکار ایران در جنگ و مذاکرات این بود که بار مسئولیت مهار فعالیت‌های نظامی اسرائیل در منطقه را بر دوش ترامپ انداخت؛ این خود به روابط آمریکا و اسرائیل آسیب زده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/129207" target="_blank">📅 21:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129206">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
جی‌دی ونس: ایده اینکه اماراتی‌ها قرار است یک میلیارد دلار سرمایه‌گذاری کنند تا یک نیروگاه در ایران بسازند اگر ایرانی‌ها رفتارشان را تغییر نداده باشند، کاملاً مضحک است
🔴
آنها این کار را نخواهند کرد. ما اجازه نخواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/129206" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129205">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f65e2d930f.mp4?token=fa5Wm2wslQIsbBjbKVWpeBG_U0oq5SDzJR4mkhK7K2qpMjLx7w58Yw50yHTP-htK8JE7_wg-x19qIrGq4xTnh1IuH4Q6KHSRT86545_Bmsr8LpK3hNDIm-OcaZ75ZQe80smIT2MPa-LOcU_o7p3lRDIwgRfiokfN3d_wUrGmIsHwOGGWMiEaR5Juc8eI4Iq1iaM5ZUSLzHTCNsBQmzyiYkLg-EEkI4R7Mri04QR6YY9viETRti7Cvz2jWMg0Rg_0VWpEDrRhNNwEUoyLsYx2oOZm37l8zNHenFI6dhCuBogRBxsmCP3LuTnm2UwhzqTnMYxvHLnB2d1PjUgAh0XKogXH2FrK5uUsUSNynqU9eWvTaEY-PlRWA7mMGzbd28C63B0PqVpmygx0HCk63OVnPVR0LnYTxnyMLb5hbf6tE2n7DqW4yMv0J9F1OBBP6GU9GtZ18cuOamNny0hc3J9dxQ4SXxdlRZrNHSK7SfAIZMzcBnqq4O7FXyM9GRpaFCREsGFpZytcoOESmqTuwZKEdc2V19YegLkUBz0rCTStYyeifuWHapx9W0V7hpjT1Po12U8lf_3Nczf9veEbIeVbwYlAkS5MVZfgWulPZS7Mon_YERNxppZpLbW7ESfytO3cHoNkJLqxynFwVFp7SOdsIlsInkmA-z46e4tIJ3sI4mE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f65e2d930f.mp4?token=fa5Wm2wslQIsbBjbKVWpeBG_U0oq5SDzJR4mkhK7K2qpMjLx7w58Yw50yHTP-htK8JE7_wg-x19qIrGq4xTnh1IuH4Q6KHSRT86545_Bmsr8LpK3hNDIm-OcaZ75ZQe80smIT2MPa-LOcU_o7p3lRDIwgRfiokfN3d_wUrGmIsHwOGGWMiEaR5Juc8eI4Iq1iaM5ZUSLzHTCNsBQmzyiYkLg-EEkI4R7Mri04QR6YY9viETRti7Cvz2jWMg0Rg_0VWpEDrRhNNwEUoyLsYx2oOZm37l8zNHenFI6dhCuBogRBxsmCP3LuTnm2UwhzqTnMYxvHLnB2d1PjUgAh0XKogXH2FrK5uUsUSNynqU9eWvTaEY-PlRWA7mMGzbd28C63B0PqVpmygx0HCk63OVnPVR0LnYTxnyMLb5hbf6tE2n7DqW4yMv0J9F1OBBP6GU9GtZ18cuOamNny0hc3J9dxQ4SXxdlRZrNHSK7SfAIZMzcBnqq4O7FXyM9GRpaFCREsGFpZytcoOESmqTuwZKEdc2V19YegLkUBz0rCTStYyeifuWHapx9W0V7hpjT1Po12U8lf_3Nczf9veEbIeVbwYlAkS5MVZfgWulPZS7Mon_YERNxppZpLbW7ESfytO3cHoNkJLqxynFwVFp7SOdsIlsInkmA-z46e4tIJ3sI4mE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره تنگه هرمز: آنچه ایالات متحده توانسته با موفقیت انجام دهد – و به همین دلیل است که قیمت‌ها شروع به کاهش کرده‌اند – خارج کردن مقدار زیادی نفت از خلیج فارس با محافظت از کشتی‌هایی بوده است که در حال حرکت بودند.
🔴
در بلندمدت، ما نمی‌خواهیم حضور نظامی داشته باشیم که از تمام این کشتی‌های در حال حرکت محافظت کند.
🔴
ما فقط می‌خواهیم ایرانیان مانند یک کشور عادی رفتار کنند و از شلیک به آن کشتی‌ها دست بردارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/129205" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129204">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی گفت: من همیشه با نتانیاهو خوب رفتار کرده‌ام، او فقط باید گاهی اوقات آرام باشد و از عقلش استفاده کند.
🔴
من امروز با طرف اسرائیلی صحبت کردم و از آنها خواستم آتش‌بس با حزب‌الله را تأیید کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/129204" target="_blank">📅 21:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129203">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a782c50045.mp4?token=LHKqBH1T7A3JKyc2taUwCxPWoJc2jza08mssVj7hoE7FaV1Fs0rRLupqQIYJz_uAynJOzQhgd5elFLxLkvnivwho1zS3gvvbWrbLsBox4Zg-KoX7kwIFDU5905mSYUeh9TxuOlx3ADEmN4jBhR0rF8fOsuGnm7PkZGnVLmTJoYbpf3Qtth-bONnT9U2HbtnqDEI_mHu7xrb74KMlxlcg1P6kATqGrpygDgnf0EEZI4vyywSllw49GoEIbItpEylEfG8_wGfngALvL5upCJOnbAXdEPOpbvm_6IL_d07x4iiqkGj9dhX3Ssh5JAdPAvISQ2ehsxSbKy96CF8S259DGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a782c50045.mp4?token=LHKqBH1T7A3JKyc2taUwCxPWoJc2jza08mssVj7hoE7FaV1Fs0rRLupqQIYJz_uAynJOzQhgd5elFLxLkvnivwho1zS3gvvbWrbLsBox4Zg-KoX7kwIFDU5905mSYUeh9TxuOlx3ADEmN4jBhR0rF8fOsuGnm7PkZGnVLmTJoYbpf3Qtth-bONnT9U2HbtnqDEI_mHu7xrb74KMlxlcg1P6kATqGrpygDgnf0EEZI4vyywSllw49GoEIbItpEylEfG8_wGfngALvL5upCJOnbAXdEPOpbvm_6IL_d07x4iiqkGj9dhX3Ssh5JAdPAvISQ2ehsxSbKy96CF8S259DGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیشنهاد جی‌دی ونس به تهران: گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، در این صورت شما به طور حرفه‌ای هیچ چیز دریافت نمی‌کنید.
🔴
گزینه ب این است که مانند یک رژیم عادی رفتار کنید، و ایالات متحده در واقع، برای مثال، به قطر یا امارات اجازه خواهد داد اگر این خواسته آن‌ها بود که در کشور شما سرمایه‌گذاری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/129203" target="_blank">📅 21:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129202">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaf2cc7fa7.mp4?token=CfDKrBR2qwc6aB6VQonYIJrs1QL9Gr9CUROCQi9Q7ikUv_kZkxFMaRDOVJSXjdlVC4o1P-ivjvcXaDKemHYXdPq0nz1cYEFyZtMKdzK_t6UgxmzEyIQomCu2MyvJfuyb05F05t3H_uiRtHfVT26L9BCHqnJ37M89iPyVaukoCLUV8j3d7d3hQ823P-TxFfJvdq_YuB_dou8wItw2jxyn-zeA_Zk0adLmR3-_EA2hoWOZa0EYtAPsBWWznndvRQpOb1zPgHQvtdhIxOQPMXa6-EUlytdEDXNkB4oYkBKAgp-Jwxpxkxkv4sXZOfpc2VYROMOhyC0t3Dxof95lWimYVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaf2cc7fa7.mp4?token=CfDKrBR2qwc6aB6VQonYIJrs1QL9Gr9CUROCQi9Q7ikUv_kZkxFMaRDOVJSXjdlVC4o1P-ivjvcXaDKemHYXdPq0nz1cYEFyZtMKdzK_t6UgxmzEyIQomCu2MyvJfuyb05F05t3H_uiRtHfVT26L9BCHqnJ37M89iPyVaukoCLUV8j3d7d3hQ823P-TxFfJvdq_YuB_dou8wItw2jxyn-zeA_Zk0adLmR3-_EA2hoWOZa0EYtAPsBWWznndvRQpOb1zPgHQvtdhIxOQPMXa6-EUlytdEDXNkB4oYkBKAgp-Jwxpxkxkv4sXZOfpc2VYROMOhyC0t3Dxof95lWimYVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره اسرائیل: من همواره از تصمیم ترامپ برای پایان دادن به توافق هسته‌ای با ایران دفاع کرده‌ام و اغلب با استدلالی مواجه می‌شوم که می‌گوید: «اسرائیل فکر نمی‌کند این کار خوب است، پس بد است.»
🔴
واکنش من این است: نظرات اسرائیل اهمیت دارند، اما در اصل مستقل هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/129202" target="_blank">📅 21:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129201">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a172117b9.mp4?token=Dl8sxOuHKywVLU7IMJUFyX1aKlJXnGCwooYZxLbrXYCnmWzH4M_vI7nqjvX5earBR3LoxDhj3P3x0Rf42WOWc9rcPiKDds20OJBRfX2JU0HsGGjLiHRmfnANyBW1ugadNKWDuiAlL0w5_i9LCHNwidqkFjmMHC7_RdFfjcTjn1onOuKElchQnvotoJM3GobwL_RdrelIvxui0Fklfi1K9tadYLLt9RHBJ_p3bXn6h22oPLv7N0gmYnrhJXV8v8jkBL5LkwYakhrhjZPm_XHNN7-ttADC4ROiE5i2K7udoOkHz6DmoOEqyQuMiwtmKkhl2ThwleuIDSCECM3oL9pWLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a172117b9.mp4?token=Dl8sxOuHKywVLU7IMJUFyX1aKlJXnGCwooYZxLbrXYCnmWzH4M_vI7nqjvX5earBR3LoxDhj3P3x0Rf42WOWc9rcPiKDds20OJBRfX2JU0HsGGjLiHRmfnANyBW1ugadNKWDuiAlL0w5_i9LCHNwidqkFjmMHC7_RdFfjcTjn1onOuKElchQnvotoJM3GobwL_RdrelIvxui0Fklfi1K9tadYLLt9RHBJ_p3bXn6h22oPLv7N0gmYnrhJXV8v8jkBL5LkwYakhrhjZPm_XHNN7-ttADC4ROiE5i2K7udoOkHz6DmoOEqyQuMiwtmKkhl2ThwleuIDSCECM3oL9pWLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره اسرائیل: اسرائیل شریکی خوب است، درست همان‌طور که بریتانیا یا فرانسه شرکای خوبی هستند.
🔴
این به این معنی نیست که همیشه منافع ما همسو خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/129201" target="_blank">📅 21:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129200">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89d64d2b17.mp4?token=Y8UF5ir-IWXlklirde37Y0uCL90v1PHhX7KwwdlZCxElOfuzuHaXdYro7UjW31KF2YhX8ATbwJdGeo8tbaDw03HWtv2jYnHywEdC8SHtAGINAvNkrwwHUSyopxGFgUHNRpLGIN0YfChssAFgYSsVz-H6JpaP2R0AScX4b1yWxkQqNaI1EKV9XEhW-QVmniF4mUXPFQvOafCRfWmpbgcAEPkCTxnvWR0VpcggweVf8Uk5K1owTK1JO6C9Q8vgdKV0I38_5eormGcyPVZ-meieCLUidX_1geQPe-RWWGDRPS6SZeu5LtlF-H9KzPTBsFEtfWN4qVM81GyJ1FargJ4RvYWlTV_bBcNLDydyeAhhVDhXsCA_JHFQSSPGOryR91zvrwdifsoVasTzLzHqvDgxrhXGABWqTypQ5U0PZzpBKLErVMTp3qkM1i8igUJSuZt68l9bMHZuFFMVA5masQ8xRrlITcD0cd52c9BoDWVapXzGBUGDu1c5lGsTrI1R0bmgR5uqmmPZaePAYwKAAVo8AIz4suR5PLOGs1FjVL4lxjrJIr63h4YEupPORJ9hzDHtFn2SxHB2Q2HAVSuDv0d2tZCqpTARFoW1E3LZd_l_dFpaJ-VQnT1w3wbrqQih2aG0J7HXbUX7cZXyZxUjgMnSCifklIYdh5nWiUBpj7d0u78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89d64d2b17.mp4?token=Y8UF5ir-IWXlklirde37Y0uCL90v1PHhX7KwwdlZCxElOfuzuHaXdYro7UjW31KF2YhX8ATbwJdGeo8tbaDw03HWtv2jYnHywEdC8SHtAGINAvNkrwwHUSyopxGFgUHNRpLGIN0YfChssAFgYSsVz-H6JpaP2R0AScX4b1yWxkQqNaI1EKV9XEhW-QVmniF4mUXPFQvOafCRfWmpbgcAEPkCTxnvWR0VpcggweVf8Uk5K1owTK1JO6C9Q8vgdKV0I38_5eormGcyPVZ-meieCLUidX_1geQPe-RWWGDRPS6SZeu5LtlF-H9KzPTBsFEtfWN4qVM81GyJ1FargJ4RvYWlTV_bBcNLDydyeAhhVDhXsCA_JHFQSSPGOryR91zvrwdifsoVasTzLzHqvDgxrhXGABWqTypQ5U0PZzpBKLErVMTp3qkM1i8igUJSuZt68l9bMHZuFFMVA5masQ8xRrlITcD0cd52c9BoDWVapXzGBUGDu1c5lGsTrI1R0bmgR5uqmmPZaePAYwKAAVo8AIz4suR5PLOGs1FjVL4lxjrJIr63h4YEupPORJ9hzDHtFn2SxHB2Q2HAVSuDv0d2tZCqpTARFoW1E3LZd_l_dFpaJ-VQnT1w3wbrqQih2aG0J7HXbUX7cZXyZxUjgMnSCifklIYdh5nWiUBpj7d0u78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره اسرائیل: چارلی (کرک) بسیار نگران نفوذ اسرائیل در سیاست‌های آمریکایی بود.
🔴
او همچنین از یهودی‌ستیزی بیزار بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/129200" target="_blank">📅 21:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129199">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e295b5be.mp4?token=HKBu5AUaNiNtdpNZoddDaeC_vydLXEM01y0jeD7Tan5vQarjp2SbNtaczb_uBqDbKU_teorO_Y3HUH3okWBbNR4eXhzNtSRWIbp1HrwV7jTlTuP6RFGQ2o6m02wursE7tkI4BMsf-M_ku9z0xO-XlA6yI0-9UMgZyQtD3A7O8kDzhoWPhkyku0SpSruF6ycfco5Nl34hMuxxjPiQKyPQQpygRE8Z_8_HpsO0RAUkXQnp2jn-XYpCtjr1ZOq8oulBJynPng3DaZ81xHdmGQil_Xv2kyHmLdoOKS-0MGO9RPWCM-QkEzHT1jdAeOTD4Kzp3d4u0k4NloBBpw55MqlqYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e295b5be.mp4?token=HKBu5AUaNiNtdpNZoddDaeC_vydLXEM01y0jeD7Tan5vQarjp2SbNtaczb_uBqDbKU_teorO_Y3HUH3okWBbNR4eXhzNtSRWIbp1HrwV7jTlTuP6RFGQ2o6m02wursE7tkI4BMsf-M_ku9z0xO-XlA6yI0-9UMgZyQtD3A7O8kDzhoWPhkyku0SpSruF6ycfco5Nl34hMuxxjPiQKyPQQpygRE8Z_8_HpsO0RAUkXQnp2jn-XYpCtjr1ZOq8oulBJynPng3DaZ81xHdmGQil_Xv2kyHmLdoOKS-0MGO9RPWCM-QkEzHT1jdAeOTD4Kzp3d4u0k4NloBBpw55MqlqYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره اسرائیل
:
اسرائیل، مانند بسیاری از کشورهای دیگر، سعی در تأثیرگذاری بر سیاست‌های آمریکا دارد. من این را به عنوان یک واقعیت پذیرفته‌شده می‌دانم.
🔴
رهبران آمریکایی باید بسیار محتاط باشند که وقتی کاری را دنبال می‌کنند، این کار را در بهترین منافع آمریکا انجام دهند، نه در منافع هیچ کشور دیگری.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/129199" target="_blank">📅 20:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129198">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc375717ed.mp4?token=oYqIdPa_yDsYw711aevhXpA2Z59VZGZtol_UOI27atNa8U7WgnA7yanMF7si_9nMqYN4B_jyxWg3iDoxHd2G3ahE1wo8pN8PdIUaI8sFkuvRbvR0WEtUtbHk20IYoB5S9-xzSBCBLvvVFzs3recjVmjzbcEs5sEdRcGhcufxx6S1MpnivZj9FE7HaVHhIzkuWR0MytjQGNa86SfokA2AUhZ1JVDQmYg2x95ikROokxYwf19RBL41q94enkCCyjaE2UVtCdhJKZesZXu1fOLA_LDHkBoDQ7czDdE35lpES0C-n5i8_K862BtvHXu-_eYlFUVWQKFricDcfTOAOKKtAL0gZmDdXnS_9wAAmNnjrfP_3G4uYtlmty_XIq8MXG-7eid2IBZuvQsyL4fqipbuhNUjP7z0QLURJL5P-b2YzynOpNUvyhP96HeJnjsXW9rSL330DvlMHmX0OlvIl6EFWTR5uhNz6AhvCwCC5Lq2fL-si--DR_ppvlNBm5eh5oDfmzfO0-mwCdnX0UjlFhC_Kdi76VuZt3f8-4zdUUGhQG9dzZyiHuTucd_j-51uJeB8OuiOp3HFj2cTOEnlZXqIDKtMmnuEb5H5DjgkDoTaQKioL-RHLYJTc2e9C1OytPs8cq0nSkW0gM6eHiQjDeFTg6WrdFksjduoyIAcmFxUb2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc375717ed.mp4?token=oYqIdPa_yDsYw711aevhXpA2Z59VZGZtol_UOI27atNa8U7WgnA7yanMF7si_9nMqYN4B_jyxWg3iDoxHd2G3ahE1wo8pN8PdIUaI8sFkuvRbvR0WEtUtbHk20IYoB5S9-xzSBCBLvvVFzs3recjVmjzbcEs5sEdRcGhcufxx6S1MpnivZj9FE7HaVHhIzkuWR0MytjQGNa86SfokA2AUhZ1JVDQmYg2x95ikROokxYwf19RBL41q94enkCCyjaE2UVtCdhJKZesZXu1fOLA_LDHkBoDQ7czDdE35lpES0C-n5i8_K862BtvHXu-_eYlFUVWQKFricDcfTOAOKKtAL0gZmDdXnS_9wAAmNnjrfP_3G4uYtlmty_XIq8MXG-7eid2IBZuvQsyL4fqipbuhNUjP7z0QLURJL5P-b2YzynOpNUvyhP96HeJnjsXW9rSL330DvlMHmX0OlvIl6EFWTR5uhNz6AhvCwCC5Lq2fL-si--DR_ppvlNBm5eh5oDfmzfO0-mwCdnX0UjlFhC_Kdi76VuZt3f8-4zdUUGhQG9dzZyiHuTucd_j-51uJeB8OuiOp3HFj2cTOEnlZXqIDKtMmnuEb5H5DjgkDoTaQKioL-RHLYJTc2e9C1OytPs8cq0nSkW0gM6eHiQjDeFTg6WrdFksjduoyIAcmFxUb2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: اگر همه چیز کینه‌ورزی به یهودیان باشد، پس هیچ چیز کینه‌ورزی به یهودیان نیست.
🔴
من واقعاً فکر می‌کنم کینه‌ورزی به یهودیان بسیار بد است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/129198" target="_blank">📅 20:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129197">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFA4yPTiuVfjsqp3XViZTtn_UAZlFRhNSdv7xF9yuiu3gESVVqkbSQcA-4ahBvocL-TWyBoODMabdDMhCDcKKd6IT2DdG9GgoGXC80w67wgeyKmdvei9vYVstKYTdA0KLdT3eNs0N3zRiBP7po1o5uoW43VfG2Lxnct85z3LWzytg0L89hFNK_jK-uOwufR9Iy9bFNfrCig2EoUOOLtnP8-yivZElgPGImSft469YHMCNGFYdzf5SYXteQAgpDnYZSVYXU4KK-a_eCNchuQoiippfwaCUhZtjhnKn1AjD6PEVVGujLY8un0GEyzh6VBRMSZRxDgGDCDZd4TUNiPR5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه اسرائیل هیوم به ترامپ: می‌توانستی بزرگترین رئیس جمهور تاریخ آمریکا باشی اما رفوزه شدی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/129197" target="_blank">📅 20:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129196">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
تماس تلفنی ترامپ و نتانیاهو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/129196" target="_blank">📅 20:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129195">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
شبکه NBC: در تماس تلفنی میان ترامپ و نتانیاهو، ترامپ بر توقف حملات اسرائیل به لبنان تاکید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/129195" target="_blank">📅 20:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129193">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ان‌بی‌سی: ترامپ اوایل امروز با اسرائیل صحبت کرد و از مقامات اسرائیلی خواست که آتش‌بس با حزب‌الله را بپذیرند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/129193" target="_blank">📅 20:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129192">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
حمله پهپادی نیروی هوایی اسرائیل علیه یک موتورسیکلت (حزب الله) در حال عبور از جاده‌ای بین زبدین و حروف، غرب النبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/129192" target="_blank">📅 20:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129189">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjiOVd7IXlSyjVTPOd4yp8X0CwQj7M6O31L3wpYNSwCnN5J6Piy2xCiQYSnOmMg6IjFWzePRDJwVb2NtvaofvcA1fEJXTJHfjC6qXmzv_mRD4ZvA4wziHFVViUuaMZnj9Q_ajQeXuIEuSg0EoGUysC3Qw7RvZybdABrp9wwPFieW5QFxb51nm94d7FjD_p4TdKn5iizSmKD6PnmIX9ro1_xLhyN3Bf9F3o9YHbpURN6lz5zdXAfPyebAKOrNRjoEvQCcBOII6YhbmidkKlpoqwFA4fNM1P9B6kdyoygw8hpQBRyR2ZUFo40ASH1uuvjHHmvm9qKWdQfU4Bhls2aZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3lEbRviw3I8_k9Xw7FHmI51lEpZIfnaMqXwaZnWKWGXydza2_AaqZEe9S6vkCbYdBpdPVaS_LIo6IYHXDfivY3V8G5mZhit6joWiU475RXqboSATyBioEXl7rhnI7cyFuodO0KvQEIpfP8km5xEUqBCotCMnzTKbbKQEwNdgzyG_mPLujqmrJXMEAwyIhFXewsZeddBHQ_c1PPYHAi-1RQdLp6rmaAv1U4EpS8Hco-AnZfCGhc7Ar6r8pwELf3vPZ_8XFErz5gmfbHVPciUOM2YD6r27X_274Tj1bzlFRHgNOwzXci7FPmSvtEqTIlrljxvDcouxsg69SNFGU-HbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOC63WLTWU91jg82YPSonRK2n9OAF9bvmO_qWrVyC0LwMzhPwGw1uCxhseyitcUOHEpyU4Nn1twCCcYB2JFduwf0-tqpMMvnkk9WkT6PY8_HrGa4_qkerdD7ThTsjOQh1uPehGaWIJI8bQ_3BhamklFiXkrJIe3dBFA6irceH-SOUS1xc-kxLsrOx8MbgvY20XbC2D_O4xL6jmiI8jeBt5fwjCveSgjg0mvYL5QocyLmv3ydDOc6-SNkOVNAgx98CFKzHZuH2RAKmZ3eF5u82bab4XyMJneLwBkVkhN0hisXHmmCQxhuvJGRb34-LxDZ4qBmfosNXiNNsR4bF07O1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
موج توئیتری راه افتاده که نامه دیروز مجتبی رو خودش ننوشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129189" target="_blank">📅 20:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129188">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزارت خارجه روسیه: با تثبیت اوضاع غرب آسیا، توصیه قبلی برای خودداری از سفر به کشورهای عرب حاشیه خلیج فارس لغو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/129188" target="_blank">📅 20:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129187">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a855bb7c.webm?token=EHEpyTzvGM5VW9GFizp9itoKySq4LAtcGg7lMdUIUagiEIPt3ex7J3biNta2u7K5TTWRLx-Z4PIT8s0fA8_pce3XZUwMnWov_vCiO6mGaj06jrhzJTPL-nQr6fre6S-_AUvxCabbBWOrB6hm0jXYBf7FFPZPi9ZcuxyqQwv6-y_hnP34WWRFHB64Yfb5q2spPcQUFY0epWKI9-NteMCs5syfHFpY0_Qak70HMaGgBCS-_qgNjBtwQHi8c7hkC1XgyyTs067x-snX6ydzyWsAU6tt86EMC2uotqAg7QjFVosylEsrX_y6pg5BUClX6r2-gP-COSAT939jo_VqYUGebg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a855bb7c.webm?token=EHEpyTzvGM5VW9GFizp9itoKySq4LAtcGg7lMdUIUagiEIPt3ex7J3biNta2u7K5TTWRLx-Z4PIT8s0fA8_pce3XZUwMnWov_vCiO6mGaj06jrhzJTPL-nQr6fre6S-_AUvxCabbBWOrB6hm0jXYBf7FFPZPi9ZcuxyqQwv6-y_hnP34WWRFHB64Yfb5q2spPcQUFY0epWKI9-NteMCs5syfHFpY0_Qak70HMaGgBCS-_qgNjBtwQHi8c7hkC1XgyyTs067x-snX6ydzyWsAU6tt86EMC2uotqAg7QjFVosylEsrX_y6pg5BUClX6r2-gP-COSAT939jo_VqYUGebg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/رهبر حزب الله، نعیم قاسم با آتش بس با اسرائیل مخالفت کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129187" target="_blank">📅 20:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129186">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/رهبر حزب الله، نعیم قاسم با آتش بس با اسرائیل مخالفت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129186" target="_blank">📅 20:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129185">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
خطیب‌زاده به الجزیره گفت: بدون پایان دادن به اشغالگری و پایبندی اسرائیل به قوانین بین‌المللی، صلح و ثباتی در لبنان و منطقه برقرار نخواهد شد.
🔴
«هرگونه توافق آتی باید شامل آزادسازی تمام دارایی‌های مسدود شده ایران باشد.»
🔴
«ما پس از ۶۰ روز سازوکار جدیدی برای مدیریت تنگه هرمز اتخاذ خواهیم کرد و ابتکار ویژه‌ای را به کشورهای منطقه ارائه خواهیم داد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129185" target="_blank">📅 20:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129184">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEGmYx_3xuOVFgPAHGPlaqrN-AFiDXlIbO3enGr613yCFFoZQ7K2hGKHEa6DcfNFTFDxbkPo8BGgh8O_PkM-Hr1AwFkjTJBvPuLb5tqBxf-0n83D8lhcSOgkgl165W0GBQiwzTfOA4w6X1TJHE7Cg4_wJO1F4uszida9OGX4gAsEWtN0UJ-8zNmdKGOZ50iFW5eFe-osm7k-MTFEvnnwg8xB1F1yk_szVSe4aKUu1QiyubZ5vZex7-yq01NwvwGaH2FWvaE17x29Zy0q_Ko3HLzaxrY4zMBkHCMXZIRi47bIMmb54Fi-UN3zgV8W9ggpqOVf6eLIC3eWnGQj6EjTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: یک هواپیمای ایر فورس دو سوخت‌گیری شده در فرودگاه مریلند روی باند فرودگاه بود. میزها در یک تفرجگاه مجلل سوئیس چیده شده بودند. تدارکات آماده بود. مطبوعات در راه بودند.
🔴
اما مذاکرات هسته‌ای مورد انتظار بین ایالات متحده و ایران روز جمعه برگزار نشد، که یک شکست زودهنگام برای مرحله بعدی مذاکرات هسته‌ای بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/129184" target="_blank">📅 20:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129183">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ولادمیر زلنسکی: من به لوکاشنکو یک هفته مهلت می‌دهم تا تجهیزات نظامی را از مرز اوکراین که برای تنظیم آتش توپخانه علیه جمعیت اوکراینی استفاده می‌شود، پس بگیرد.
🔴
در غیر این صورت، ما خودمان این کار را انجام خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/129183" target="_blank">📅 20:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129182">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg5b_hoC-o8M6MdZfk9VSZY9fLGDqIPQ38HmFOKeur01_fSB0rIPRFz9GG8YPoPZn_VX5N94STuzOnc5CC5D9eb-Hrx9VMAlGPQYKMTAAHmenmAL-h7BKyYHjChZf8uwhzrubzUU5ZADZ_6YvDx56PQbkOfAEBV2fjMgl9YslQ8q0OybCd6tpdYOmSTer5-wgVCE8J9h_jwG4j1kLkXJwrYRpNe4h57p7vKVCpFo-XujzEP3ep9XvpQYdtafVbzz3j-lLD3jPgglkm24pmHmGRqdlZ3HUfyqNPbWq-BnkMH7nbvmgea9x4cPrzzS1pgB--LsmgfoqLKEznmwotw4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیر استارمر، نخست‌وزیر بریتانیا، پس از افزایش درخواست‌ها از سوی وزرای کابینه و نمایندگان حزب کارگر برای کناره‌گیری، در حال بررسی آینده خود است، طبق گزارش تایمز.
🔴
استارمر فشارهای فزاینده را درک می‌کند و انتظار می‌رود در طول آخر هفته با همسر و خانواده‌اش گزینه‌های خود را بررسی کند و سپس تصمیم بگیرد که در سمت خود باقی بماند یا استعفا دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/129182" target="_blank">📅 19:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129181">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: تماس بین نتانیاهو و روبیو، وزیر خارجه، به زودی، درباره لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/129181" target="_blank">📅 19:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129180">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667c0e662b.mp4?token=e9XJmvLNqip2uitPNmQwpP6OHxEKelj5TL-1KOnYo2efqVxBqpQ4bSKD8s8VSZj2KqLockU0RK2s8elv2q5REX283CUIFvgq0gc-Tfd0c5bYoLZ6e3whd5u2wchFuxFdl0cfn0_TZopxZq-Lws_nKgnja9u_ILSjQEZW1vCVHpEDCDuIDBtq5m8Kgh2FWH6dEa2kqPRsPpwgacIc-ADHbh6Rf_ADezJSvEUEwb9DO-WUQLJDQYVRrQpmPfI4KbAX-aONW9Pe9nEl_wvizpPvihQLHCLFGpDpaZar0YAYC2NwNr6D8IY0dUSpRgjrfUIcXV0j7nOVHaR5pJOhD24gsEw4rNCczSELlPrTS_cH9FqFoZNxbrtWlOJuhqHLMyRh1hhw8KVWEMm2hVUv04Vh4SxDlNhj070gBbnP29jMgguSlKez2Z3U_7ZztlG3VRxUWOGc49LqzxxBnksd1PMrqvbJQECkDoToqV4kjHCMynhB88Q6aubzVl__TjKPzUWt6MevXbhFbNZYSgCxwBDi2vCEHohbX4b5GXUp5Be4NFDcOTrjmk-LCu4-zCEZnPl5z2lP-sfpEl90RkbzPmB76tGe28Vsp7Kt_4gUfYBKZvDSwHu8fhCPzH2DFQsEjAozmSxq1DVYkz5yLs1s8lkrZDhhCJTP35iAG3GF7wqzuzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667c0e662b.mp4?token=e9XJmvLNqip2uitPNmQwpP6OHxEKelj5TL-1KOnYo2efqVxBqpQ4bSKD8s8VSZj2KqLockU0RK2s8elv2q5REX283CUIFvgq0gc-Tfd0c5bYoLZ6e3whd5u2wchFuxFdl0cfn0_TZopxZq-Lws_nKgnja9u_ILSjQEZW1vCVHpEDCDuIDBtq5m8Kgh2FWH6dEa2kqPRsPpwgacIc-ADHbh6Rf_ADezJSvEUEwb9DO-WUQLJDQYVRrQpmPfI4KbAX-aONW9Pe9nEl_wvizpPvihQLHCLFGpDpaZar0YAYC2NwNr6D8IY0dUSpRgjrfUIcXV0j7nOVHaR5pJOhD24gsEw4rNCczSELlPrTS_cH9FqFoZNxbrtWlOJuhqHLMyRh1hhw8KVWEMm2hVUv04Vh4SxDlNhj070gBbnP29jMgguSlKez2Z3U_7ZztlG3VRxUWOGc49LqzxxBnksd1PMrqvbJQECkDoToqV4kjHCMynhB88Q6aubzVl__TjKPzUWt6MevXbhFbNZYSgCxwBDi2vCEHohbX4b5GXUp5Be4NFDcOTrjmk-LCu4-zCEZnPl5z2lP-sfpEl90RkbzPmB76tGe28Vsp7Kt_4gUfYBKZvDSwHu8fhCPzH2DFQsEjAozmSxq1DVYkz5yLs1s8lkrZDhhCJTP35iAG3GF7wqzuzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: آنچه در هر جامعه‌ای جشن می‌گیریم، بازتابی از ارزش‌های ماست و ما زمان زیادی را صرف کلیک‌بیت و خشم‌بیت در مورد فرهنگ سلبریتی‌ها و شایعات می‌کنیم و زمان کافی را به محتوای واقعی اختصاص نمی‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/129180" target="_blank">📅 19:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129179">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نعیم قاسم، دبیرکل حزب‌الله : تلاش برای حذف حزب‌الله شکست خورده و اسرائیل بالاخره مجبور میشه از هر وجب خاکمون عقب‌نشینی کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129179" target="_blank">📅 19:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129178">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18a311e35a.mp4?token=CyhuTtm6QAPOQ7gZDYfPq-Fov12IaD4QIPbk8OOTPzH3uKBoQhDLogOhOGkiO4w5g5hWcZPw5PqsPuhg9RJYv8wLNafbSTMTwT2_mLoO7W86oHIAEtsbUAixtsxJHAUhChi5l4y6WD3DuNzcgvSTBc3wr6Z9wj6xtbkuFdFyR1lyl_LyHCFluYoRsUdPfV_9b-ixHkvzwEH39I7uPNGe1ETtKdCmct1sBK-nE1u9EmsvwRbDN22zU8i20iwTpb9avsA3WAq6pt-shfgKr301VoXCHELgk2afxH0JQK474CfJphf5Mwdvi1qlUL0C848qzlYpSNj_ZmWbVpdQqTuUTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18a311e35a.mp4?token=CyhuTtm6QAPOQ7gZDYfPq-Fov12IaD4QIPbk8OOTPzH3uKBoQhDLogOhOGkiO4w5g5hWcZPw5PqsPuhg9RJYv8wLNafbSTMTwT2_mLoO7W86oHIAEtsbUAixtsxJHAUhChi5l4y6WD3DuNzcgvSTBc3wr6Z9wj6xtbkuFdFyR1lyl_LyHCFluYoRsUdPfV_9b-ixHkvzwEH39I7uPNGe1ETtKdCmct1sBK-nE1u9EmsvwRbDN22zU8i20iwTpb9avsA3WAq6pt-shfgKr301VoXCHELgk2afxH0JQK474CfJphf5Mwdvi1qlUL0C848qzlYpSNj_ZmWbVpdQqTuUTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی: از نگاه بین الملل در ۴۰ سال گذشته یک روز نبوده که ایران بدنبال ساخت بمب اتم نبوده باشد
🔴
اگر ایران به سمت بمب اتم حرکت کند همین چین روبروی ایران خواهد ایستاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129178" target="_blank">📅 19:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129177">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy76vKiZ7rCdzArQwftsCVYZyKKq7BnXTGVQxZsO-uXw9lKQs7_Pzz8TouTb-QieSiKSihyz5z4PtoS1t3XDMK88SSf0loNbZwH5MFMhYr20Lsd2B9Ri4i_jRJufaQ0sqooyJVtV9kIL8fyjK5JV5ORWRsxfinyn8Bvf_dnZP3kDTYqQlsyoTRdvRcrHyFjglCZFKk1gxhUD0_zTec22Xs-T7r--cF3ZGpOd0fgYTcT00Na0_aGS8U14RoCLby-TvGfmWFWTIBS8AvY7pvxtLLO7SoDzWd6y5dsRbJXa8IiiIb48VR7-DzvueOnJEK6fyFVblFzkFNFAgvAMuhcBig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور هیات قطری در سوییس بدون حضور ایران و آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129177" target="_blank">📅 19:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129176">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
واشنگتن پست: سازمان اطلاعات آمریکا اعلام کرده که اسرائیل به طور فعال در تلاش است تا یادداشت تفاهم ایران و آمریکا را بر هم بزند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/129176" target="_blank">📅 19:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129175">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری / هلند: برای تضمین آزادی کشتیرانی ناو جنگی به تنگه هرمز اعزام خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129175" target="_blank">📅 19:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129174">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
امانوئل مکرون: برای مشارکت در اجرای توافق بین آمریکا و ایران آمادگی داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129174" target="_blank">📅 19:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129173">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نتانیاهو: حزب الله بهای سنگینی پرداخت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129173" target="_blank">📅 19:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129172">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سنتکام: بیش از ۲۰ کشتی روز گذشته با امنیت از مسیر تعیین‌شده در تنگه هرمز عبور کردند
🔴
از کشتی‌ها می‌خواهیم دستورالعمل‌های مرکز اطلاعات دریایی مشترک را رعایت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129172" target="_blank">📅 19:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129171">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سی‌بی‌اس: ۴ کشورمیانجی تفاهم ایران و آمریکا یکشنبه آینده در مصر نشست برگزار می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129171" target="_blank">📅 19:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129170">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
گفتگوی قطر و سوئیس درباره حمایت از مذاکرات واشنگتن و تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129170" target="_blank">📅 19:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129169">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزارت امور خارجه ایران: عراقچی به همتای پاکستانی خود در مورد پیامدهای هرگونه نقض تعهدات یادداشت تفاهم هشدار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129169" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129168">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
بلومبرگ گزارش داد که ۱۱ نفتکش حامل مجموعاً ۲۰ میلیون بشکه نفت ایران این هفته بندر چابهار را ترک کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129168" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129167">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فدراسیون فوتبال ایران بابت رد درخواست ورود به آمریکا ۲ روز قبل از بازی با بلژیک به فیفا شکایت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129167" target="_blank">📅 18:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129166">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
مالک شریعتی نماینده تهران: ظاهرا همراه با پیشنهاد جمع‌بندی شده‌ی شعام درباره متن ۱۴ بندی تفاهم‌نامه،
یک متن تفسیری ۶ بندی نیز درباره اقداماتِ طراحی شده‌ی ایران، متناسب و متناظر با بدعهدی‌های احتمالی آمریکا، از سوی رییس‌جمهور محترم برای رهبر حکیم انقلاب ارسال و اجرای آنها تعهد شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129166" target="_blank">📅 18:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129165">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی آمریکا:
جنگنده‌های اف-۱۶ به گشت‌زنی‌های خود در خاورمیانه ادامه می‌دهند و آماده مداخله هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129165" target="_blank">📅 18:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129162">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PEe4SfTK3Y0uI72835emKnoHXE3blDw1aMLtosm08shMnkwP-WVciD-Q-Tbuie3-s_ufPpE05y_CJfrH_bAZi0wcf_jZShewzGuIEErdp-fnUVcGhmtnO2PIHDLPjetac0NEKaGbwElnyz8fB0ikvAzz3Kcww4aur7OuFYX3bopHS5Naa7QqXuUVx4-_-FqqpW-33Yx_S8PmesTOA-8oEcLU52eat9E2at1Y84foNzGCflyEnOVtqpn8LH9RLdTI07b41iodlzdI6zFS6O8T6ohdvw4paqVpa4qZb32DAmhaGZ277lb6AkLRFmd1Di_GX7pUn2etoZ69EB1V1Q0fEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CoTauB6JAG_YIPr1zKi7lpiqq8ZSR9-vF53aKQ0PCmvFt-DmlErnMqJ7cd_p-9o2c-_2bfHx_1E-YmMGnLkheD4euJoYc4PGj55EvGgVtiaaV5NVLwq_dL4Ter92ilRNZn9_qJPxDvkmQvBWeeOkDSN9HNJlQpAqQAKAeZ4Fhu_A880qjlx-7_MzO6Bwo5bxAqwOLFkEG-LQljQF5InRLmkUQANkCZCiYHcsVRpWdrEqcrrE5SzCpaOrCZ31PWgh6_xyCuGfxs5iYBJAEjvADdpekSXuKBQY90uOiZGqXZ_y9TTO4EEtgcuojLHrDRXndxsYya2qtfiCtYcmpzE_zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5245763015.mp4?token=low_ufZIBVx_v2p0PHfoQU30XLPuTL3nLLJabywtSo6186XwAXm_n10KDhG49j9_hlFi0pa5-zsYUYz8_Gmhh-JHX7QLURlxEWQlk0HXjm8SLAf-jpYbdKFI7yjeNHV59ZH9v54b4sJRCUytRrOJcuuClFcYsMlwticaP4eU9JfpLaBJkOp7BGVa8fvaENRVSl2RbO78LKEQntZaSB5kXudEL63piouZzNnQZDfb6LN6yPlqhDkzqYmw_pv0XIC55kd4M-oBGSEThKWlWLuc13JqaIC2AAwr6omtoLOMGetizbK55fidskoe-o0fksO_iCDHXsVCA1dnxQelwfqYsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5245763015.mp4?token=low_ufZIBVx_v2p0PHfoQU30XLPuTL3nLLJabywtSo6186XwAXm_n10KDhG49j9_hlFi0pa5-zsYUYz8_Gmhh-JHX7QLURlxEWQlk0HXjm8SLAf-jpYbdKFI7yjeNHV59ZH9v54b4sJRCUytRrOJcuuClFcYsMlwticaP4eU9JfpLaBJkOp7BGVa8fvaENRVSl2RbO78LKEQntZaSB5kXudEL63piouZzNnQZDfb6LN6yPlqhDkzqYmw_pv0XIC55kd4M-oBGSEThKWlWLuc13JqaIC2AAwr6omtoLOMGetizbK55fidskoe-o0fksO_iCDHXsVCA1dnxQelwfqYsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129162" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129161">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8lefqoJgr0XnHSX57uaCb4oYe8q0wZdvgcUKkTpOFRihJUeZ4XWAWEuMG0Is27GIy1bcSiFwWyIqzP2LJFAtZtUQqk21rnai06DjqeksAQ6p3AMNgeG6k3sKcU4R4D45WcuR5J4U4Yquw4R0D0P7x-FmiLgJ1psUCJmEF_CWqVN6omk8quyA4-Qcadvp5gAxi_zfontji8EAioXfxPkb1M1zgu7KCvp0MSZSBCbH1GeEE9ganChlNuPTUWyCQfgcrEAMbMMO8-_slHzhxJuf2PavmM5BF91WWhSG06zV5lkToS537NU66cPnkOKpAGG6p65s24GIxVmLK_EKg7tcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدمنان رییسی، نماینده مجلس:
خوش‌انصاف‌ها(منظورش قالیباف) مجلس رو باز کنید، رهبرم تنها مونده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129161" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129160">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNpGx2qMqgAvIchwc_vALMlqj8Ij0CY39Yt8LOHFYPz60LPftuINCJ7jp2bthJBonyNeuceGYwePAp9_McKoWM8mp9lm66jLdTom6u47yf6O_olgEsOoDoOILsuq62rLW5DiXxPCZSKKUDped7qsjKGvu_NSfupsrmNMEkMpJWF8H6x6zglBedd4HD81KIBPzDPjOHPjt1PCPvljYnNAl9JYZLa-EN0_ZlB7dp1zbnWXcsUFo8CmX8i-HZ6xAGsgwBafvMq1bwH4ngZXSbjBBQR6bRVFADliOA3XowasSD-DyCwTJeoXvA_UNF3CHFXVzZf974VsUEHFPsm_3XZ1aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
دولت باید همین حالا و از لبنان شروع کند و نباید اجازه دهیم مردم مقاوم جنوب لبنان مورد قتل عام قرار گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129160" target="_blank">📅 17:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129159">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نتانیاهو: به دستور من ، ارتش به 150 هدف حزب الله در لبنان حمله کرد و ده ها خرابکار را کشت‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129159" target="_blank">📅 17:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129158">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmDRrkloM42VtplQ6GrgoeSgdb9jATy2TqgOQMXh5utD7qNt3bny_9J1PwSTLYzVGDpvyOyFlnjL4EC1_ILfZMTWi3RpAdVuW2wBlwJWAVRaBVF6Ount9agrElmdad4S_ceQBeLeDjvJ04_OZ0iwtFVmoDBQ7G_u_Y_w6KsPGx93Lnmer0yevBxzlW0uBvgVboqnFipg-YbM7qxe3MJ_m5BOWphpwZNE0v8C7iWFvuGD8a7ZI-ou8C2dXkTYZfRZ4bYXAaI16mxyLJ8zmjzWMMV_XdUsSsD9XbNv1X7vUwvWpe2M4H2wufBXFGKjVGJ63ePzfi0DeFVCIqQUPJkQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی : تنگه رو ببندید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129158" target="_blank">📅 17:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129157">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: رایزنی‌های لازم از طریق میانجی‌گرها درحال انجام است و در صورت فراهم‌شدن شرایط لازم برای شروع مذاکرات، اطلاع‌رسانی خواهد شد.
🔴
طبق متن یادداشت تفاهم، آغاز مذاکرات توافق نهایی منوط به شروع اجرای مفاد بندهای ۱، ۴، ۵، ۱۰ و ۱۱ یادداشت تفاهم…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129157" target="_blank">📅 17:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129156">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: رایزنی‌های لازم از طریق میانجی‌گرها درحال انجام است و در صورت فراهم‌شدن شرایط لازم برای شروع مذاکرات، اطلاع‌رسانی خواهد شد.
🔴
طبق متن یادداشت تفاهم، آغاز مذاکرات توافق نهایی منوط به شروع اجرای مفاد بندهای ۱، ۴، ۵، ۱۰ و ۱۱ یادداشت تفاهم و تداوم اجرای آن‌هاست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129156" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129155">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی جبل الرفیع، شوکین، الریحان و ادچیت در جنوب لبنان را بمباران کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129155" target="_blank">📅 17:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129154">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
خبرنگار الجزیره:
چهارمین حمله هوایی اسرائیل در اطراف شهرک کفر تبنیت در جنوب لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129154" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129153">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7667710266.mp4?token=WSpaSUNXL3tvvzUYjnUC-mpegE0cKqXOdmTXfrdj_R7JdMQZIE_yYx2tArLZUr-pMu7EATW3mx9LpOPX9Q3IkwCYwQkp4EUVEGHWRcJee1pYSy22YykAPoqcU1-81kl1wtGwAm3HERDnM__HdE3fujhgvbcPuVGw7r2891Jnmw2OiT5eYW1vST6Hgyikj6lr8vwvgQ0KZPIwle-wZLC7V-T_TLI3Ib7kS_oExhj5xXtYz3jX-R77oCrnM1BCAFMkqJe3IUSKrBBQHiCSICBm1GLpCqQHi_F8p_gL4StHgWdUR0zfVVrmzjAZmH_TWR9o_7fvP6jSwM3zfa_o7UZV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7667710266.mp4?token=WSpaSUNXL3tvvzUYjnUC-mpegE0cKqXOdmTXfrdj_R7JdMQZIE_yYx2tArLZUr-pMu7EATW3mx9LpOPX9Q3IkwCYwQkp4EUVEGHWRcJee1pYSy22YykAPoqcU1-81kl1wtGwAm3HERDnM__HdE3fujhgvbcPuVGw7r2891Jnmw2OiT5eYW1vST6Hgyikj6lr8vwvgQ0KZPIwle-wZLC7V-T_TLI3Ib7kS_oExhj5xXtYz3jX-R77oCrnM1BCAFMkqJe3IUSKrBBQHiCSICBm1GLpCqQHi_F8p_gL4StHgWdUR0zfVVrmzjAZmH_TWR9o_7fvP6jSwM3zfa_o7UZV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
با وجود اعلام اتش بس دوباره، اسرائیل همچنان درحال حملات سنگین به جنوب لبنانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129153" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129152">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unSaUbGEOhdvG9GMzMH7gkVup5gUukwpsD1F_ULPVd4bSb8aNkkOaAYccCDFlcPqm7yKIWjtXaVM8-tfz9cl4nUMT1P-6V7JF4WS5tg52Ns0c_5_HLFBKa8o1pclg9_BklIkeG8C47PPCdXMDktPh223qaOtSEEJbUJmrweLHRXX2KiJUx_RAAL0QvxR2bevdQRrN_GwAanzsQx7zPtdSgXzIWrAajGux6dRHAFa2jpPUt2r9LNG-t-sqWpFZOrTSnGl6NQxG-A1gvRgeh1XGHy_Wgyvrdw3VLWb8WL_pxL0eHNGUTdbnuME7e89b85QXyug30EHtgW82HqmSVEWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس به نقل از مقام ارشد کاخ سفید : بی‌بی (نتانیاهو) صددرصد با آتش‌بس دوباره تو لُبنان اوکیه ولی خود نتانیاهو و تیمش فعلاً نه تأییدش کردن نه تکذیب؛ کلاً سکوت گرفتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129152" target="_blank">📅 17:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129151">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7aa6588e.mp4?token=nMY0LhSef7t32UtdYcpxMWSRyjDXskbnNibb0IdbYC9xnOJk_InIhGk3O1QmmAlryKI-LXc0zIBRDXGO5990hPxgu9yaYzafoVbG_CUHoi3h9rBWUWkVZ7XbWQUQ8PXeuccD6IMvVl9_Qn_-0KSgtq8Ii3zlmg-0esjz_O-PNEsoF42HEG1DtjCUBvW0RcOdvb0aNrJdZREAKUOllOY8a9lQbJJGmkdshBEm1IoCsaSWTJq4gS1wIjr2KeeO25NlOBrWY1Yty_nXO9TB9fuefK6g-tEi36-6fx3mxc1zGLeVPRDi1nIwkyYE1L78AxcNMewFOmhRGqAZrxpaff9ltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7aa6588e.mp4?token=nMY0LhSef7t32UtdYcpxMWSRyjDXskbnNibb0IdbYC9xnOJk_InIhGk3O1QmmAlryKI-LXc0zIBRDXGO5990hPxgu9yaYzafoVbG_CUHoi3h9rBWUWkVZ7XbWQUQ8PXeuccD6IMvVl9_Qn_-0KSgtq8Ii3zlmg-0esjz_O-PNEsoF42HEG1DtjCUBvW0RcOdvb0aNrJdZREAKUOllOY8a9lQbJJGmkdshBEm1IoCsaSWTJq4gS1wIjr2KeeO25NlOBrWY1Yty_nXO9TB9fuefK6g-tEi36-6fx3mxc1zGLeVPRDi1nIwkyYE1L78AxcNMewFOmhRGqAZrxpaff9ltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل: از نیمه‌شب گذشته بیش از ۱۵۰ حملهِ هوایی به لُبنان دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129151" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129150">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f118f174c3.mp4?token=aFUGcyoT0nXRu0L8J5aTrTLqA3GRx4kOrNoh0p-37es8n366vgq2LlqCjgn1QrLDXuHaSTm5nCWdqQyiWzoYRNjxWC6aRFIbryxAaQLdS2CTkm3G1M8LFJtaaR_kXVLxvFHsHahz2YhjzN2sW5zxOLmRnZPgyyKFcBBZsYR2W1FBqrHisc1rmZyT9-gY7rfnPBipfPDi7hylq1cfg-8s0cf0q1HhN8qLwguZF04NGHSQu1nD_owQrPN-8N2J6osJq6wYT54dnnVkNfvh5cs9RFVJmqFLtETcm4x_J7ED8t8qIJcrzoZNYRvYX-Mvg1DfOmgolQLq1J5rExpbsb4qsFArOgJkM-lL6_Bv6Wf_lR1o4f0d2eaLVncvSSDQ9zAePTg3RgPqXctTpOIg9Gfzq0znkRiBJmunVzr7R4ieMPL3Vt3dxjbOVWfFs08znpd-3BJ6w0DrWeUdneIqJkP7CAdhQF2ypyAo4zJTgCNTEvof-UE8awW07uUHJAfUTGnLOZ-lTOmwum2O5SX5m0U8fJhwQBS_8zbrI0rbzZU9PVrDgWe13rzYodYmENOcKT_4oMH2c5pD4D0_aD5bHC1GYgRf5hGxKfdgq6ujVAloR-B2Kgg6MELVQLkTi6QaqjHKY8cy2N_i-gda6UI-gITsUBifs311glvZXGiwnGvVb0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f118f174c3.mp4?token=aFUGcyoT0nXRu0L8J5aTrTLqA3GRx4kOrNoh0p-37es8n366vgq2LlqCjgn1QrLDXuHaSTm5nCWdqQyiWzoYRNjxWC6aRFIbryxAaQLdS2CTkm3G1M8LFJtaaR_kXVLxvFHsHahz2YhjzN2sW5zxOLmRnZPgyyKFcBBZsYR2W1FBqrHisc1rmZyT9-gY7rfnPBipfPDi7hylq1cfg-8s0cf0q1HhN8qLwguZF04NGHSQu1nD_owQrPN-8N2J6osJq6wYT54dnnVkNfvh5cs9RFVJmqFLtETcm4x_J7ED8t8qIJcrzoZNYRvYX-Mvg1DfOmgolQLq1J5rExpbsb4qsFArOgJkM-lL6_Bv6Wf_lR1o4f0d2eaLVncvSSDQ9zAePTg3RgPqXctTpOIg9Gfzq0znkRiBJmunVzr7R4ieMPL3Vt3dxjbOVWfFs08znpd-3BJ6w0DrWeUdneIqJkP7CAdhQF2ypyAo4zJTgCNTEvof-UE8awW07uUHJAfUTGnLOZ-lTOmwum2O5SX5m0U8fJhwQBS_8zbrI0rbzZU9PVrDgWe13rzYodYmENOcKT_4oMH2c5pD4D0_aD5bHC1GYgRf5hGxKfdgq6ujVAloR-B2Kgg6MELVQLkTi6QaqjHKY8cy2N_i-gda6UI-gITsUBifs311glvZXGiwnGvVb0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: ارتش اسرائیل آماده و مهیای بازگشت فوری به عملیات‌های شدید رزمی در هر میدان نبرد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129150" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129149">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">محرم عجیبیه
حکومت هیئت‌ها رو کرده میتینگ سیاسی، خیابون‌ها رو کرده فستیوال
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/129149" target="_blank">📅 16:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129148">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213cbd739f.mp4?token=v5MRrTRD8H_R9UsqTrU5sLtZNikCGzN4j1zP-q7tKItXcMicLC_d_7QFIHjHl_-h7fwS028jROgTq0G2NZ-8Vfc-JQltl2xh-28q94ooCl9ZIsBF-2z7qv_Mfmi3gOb8SkjYeVTu5OeuEYvq_4dtWTWBaDsocY2ZmJa0Y0yU8lMntGe4qBdasS4xmbXSZk-TbP1OYSGxqxZHPWIqGprF_wV5gieip8yOmq8MSAlMAjwLbLZohnKR0nwwdXHGiBj3CK2f7lxc4FrzPe5jDIrS9ag-nK1kddqyd1Yo0mxFfhP5hX90uT7Fv2bRz2T1CEUQDY39inZeaAMNXXYjIn4QxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213cbd739f.mp4?token=v5MRrTRD8H_R9UsqTrU5sLtZNikCGzN4j1zP-q7tKItXcMicLC_d_7QFIHjHl_-h7fwS028jROgTq0G2NZ-8Vfc-JQltl2xh-28q94ooCl9ZIsBF-2z7qv_Mfmi3gOb8SkjYeVTu5OeuEYvq_4dtWTWBaDsocY2ZmJa0Y0yU8lMntGe4qBdasS4xmbXSZk-TbP1OYSGxqxZHPWIqGprF_wV5gieip8yOmq8MSAlMAjwLbLZohnKR0nwwdXHGiBj3CK2f7lxc4FrzPe5jDIrS9ag-nK1kddqyd1Yo0mxFfhP5hX90uT7Fv2bRz2T1CEUQDY39inZeaAMNXXYjIn4QxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به نبطیه، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129148" target="_blank">📅 16:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129147">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی گزارش داد: اسرائیل و حزب‌الله پس از مذاکرات با اسرائیل و ایران، با میانجیگری آمریکا و قطر بر سر آتش‌بس به توافق رسیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129147" target="_blank">📅 16:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129146">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
حزب‌الله: هنوز هیچ اطلاعیه‌ای درباره زمان آتش‌بس دریافت نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129146" target="_blank">📅 16:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129145">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNiGPsqOI9HlSrbUSmrGlrPcRERq_tLkBs8FaHVJGmXCtGi7Af7tuEAKKPWbrHNXLDJLEIdXZjkaHbya1Xi0N13PhVZEWbC7wQ2T0mKDi_cdjy3xu5vsm3oFQrk1jDYe4w2u3zegXmbZSKTwiyflWTueA0zVoHNGSf95aim5QoJ5oeKJMpi5aQ7GbF4X3PLDrG-6obn6f_4IzXUhAy2qQmITg_sI_DQxgdCpqCp-NjmppFZSKIKmE4JSZnK3JTUnSvV5CcFZ4O1gIhlE1bp1l201C6iZ38q1E8TdJOenT5UyR28pMUwSW_yPHOA0mAtphEPri6K1CDPU-xs5Ql_lHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش تتر به اعلام آتش‌بس بین اسراییل و حزب الله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129145" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129144">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کانال ۱۳ به نقل از یک مقام اسرائیلی:
ما در حال حاضر در آتش‌بس هستیم و اگر حزب‌الله به ما حمله نکند، زمان جنگ از جانب ما نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129144" target="_blank">📅 16:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129143">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: آتش‌بس شروع شده اما ما توی منطقه میمونیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129143" target="_blank">📅 16:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129142">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری / خبرنگار المیادین در جنوب لبنان: همزمان با اجرایی شدن آتش‌بس ، حملهٔ هوایی اسرائیل به النبطیه صورت گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129142" target="_blank">📅 16:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129141">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری / رویترز به نقل از مقام آمریکایی :   اسرائیل و حزب‌الله توافق کردن که از ساعت ۴ عصر جمعه به وقت محلی، آتش‌بس برقرار بشه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129141" target="_blank">📅 16:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129140">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری / رویترز به نقل از مقام آمریکایی :
اسرائیل و حزب‌الله توافق کردن که از ساعت ۴ عصر جمعه به وقت محلی، آتش‌بس برقرار بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129140" target="_blank">📅 16:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129139">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4030a7e818.mp4?token=ibQT4DVp9xHDlUMHciA0Ge6moc2_aSJT8jyPuSIThq8_mGXa8qHy3DOtzpaOqYyOMZVupvUJdQCRKW2xhFhKdilrccRIzPAbXZNEimq60gzkBPG7XE9m3X1bfDiyL4otQFrIN2Aoe9CHkttj4c2gJ4D01DvBL6aQDer0StHEZWpKmDFeSwHNBkkfbv6njNrn5wHHxz2dY1aM_Br4jxrsT8omYDGkXlMJOEWda7zv4OLj523EhtnBPlo5bS7-SEzKoV-a1O62sktqPK04Z_Ua_4_LL4DDXdFGGZIHodFpZMS30gZFHcrcr2yXn6df2_1dqt25F7JZWhNt7jthjvGRYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4030a7e818.mp4?token=ibQT4DVp9xHDlUMHciA0Ge6moc2_aSJT8jyPuSIThq8_mGXa8qHy3DOtzpaOqYyOMZVupvUJdQCRKW2xhFhKdilrccRIzPAbXZNEimq60gzkBPG7XE9m3X1bfDiyL4otQFrIN2Aoe9CHkttj4c2gJ4D01DvBL6aQDer0StHEZWpKmDFeSwHNBkkfbv6njNrn5wHHxz2dY1aM_Br4jxrsT8omYDGkXlMJOEWda7zv4OLj523EhtnBPlo5bS7-SEzKoV-a1O62sktqPK04Z_Ua_4_LL4DDXdFGGZIHodFpZMS30gZFHcrcr2yXn6df2_1dqt25F7JZWhNt7jthjvGRYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ در طریق Truth Social
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129139" target="_blank">📅 16:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129138">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6PYMwsL6kCM9n4acSr0IyEDAlm2Dlz2CsKovTrDpZqEk5br0eUvecLJpIg_Mcjkw4FZU5Wv-BgDqTVqLQ-XKm6CPmVWV55hsty526XjbtNuWe_LqY8XPggQv91FxF7ebmXFwP7nVR_1nNGSCcDcHVbqGDQVd5K7slUPFcEtWn_kyfx2ZNcl9vaGpKi_PrEkmz5JhIfY8GVYhUFqRIUEJD9p6_uFi2D6Ud94OZ_42KglyGTXmS0D95rz22_DSxIlt-sv8gSPO0zd22a_DqBfXtcU9FiIsw7OLOGY-mGk0OmSbcOg6eJjOQ6IKGhNK-dSybVzxPJt6CNiH9raZYjrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : ما از روی استیصال نرفتیم سراغ مذاکره
🔴
این ایران بود که بهش نیاز داشت، کارشون تمومه!
🔴
همون ۶۰ روزی که گفته بودیم رو جلو می‌بریم، هیچ پولی هم گیرشون نمیاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129138" target="_blank">📅 16:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129137">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgNEXk5tsZ2k2bn4qipDrVYNaXk1UgmFSmcPEOw30n3mAA5g1vWYlkR0PqC7JjfEaj1fGmyom_Qo8aYngi8OAsMTpWaAr1geIE0BCH60M7uKeN-15hgb5cTGAqcqhLtO4rYYpot-LUQNwMyEGTzueyODPisgM4G2qLPZNuwpzZzTu916nUxkg760PRO7aoij5cNduR-N95mqI1fAXPd9lGgGYqSvR6lv8hrFsL9sZYAqKpFa55eUmndTv5uu4zTfM78kmGsIEnErw6YBSMoF8x65OJVtaocEWWTnWCeYsxESr3RZlSY5ZqzKnZQOk2bvmMxaflbNfhLJ2iELBZLvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : این جنگ ایران را به‌شدت ضعیف کرده!
🔴
دیگه نه نیروی هوایی درست‌وحسابی داره، نه نیروی دریایی، نه تجهیزات پدافندی، نه رادار، و تقریباً هیچ‌چیز دیگه‌ای
🔴
با این حال، دموکرات‌ها میگن ایران الآن از چهار ماه پیش وضعیت بهتری داره
🔴
باور می‌کنید همچین حرفی بزنن و ازش هم جون سالم به در ببرن؟ بعضی‌ها چقدر می‌تونن احمق باشن؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129137" target="_blank">📅 16:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129136">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYWvJPchJzzUXbiNVAzlZZeUS8ysTl2IQvaruajyrnRq9DBaH0M2NEqZRvVBMKeJ82v4YFoq7NG7jJiDkk7VXGwEGZ81U5IH3Ycf01lUuj4hQdJA-PiTcBmDBipjXykk3TUt2Wj2BzucUeuq_gJzRhKCDg7Xm1_miJrROaUPk1kBkEntQBpdWp7bPK7PxbaOqpgfY8YeSKIoyh5817svbkGOXeqDHTwb2jGRpI3rNnMQEjMJuIVnZFSso0UYWyJOp1yaR-iKa5F58ztZMfY9X7Hmq1_TC2lwrUJKcVQsF3ObtTbxLtSxNEy-PKv_u3JwNdlV4ZC0iVesH_Z7Nv7dgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش عراقچی به اظهارات وزیر امنیت داخلی اسرائیل:این‌ها رجزخوانی یا اظهارنظر یک دیوانه و نسل‌کشِ بی نام و نشان نیست؛ بلکه گفته‌های علنی وزیر امنیت داخلی رژیم اسرائیل است.
🔴
فرقه مرگِ نسل‌کش که مقر آن در تل‌آویو قرار دارد، تهدیدی برای تمام بشریت است. این جریان همه انسان‌ها را تهدید می‌کند و تنها هدفی که دارد، جنگ دائمی و بی‌پایان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129136" target="_blank">📅 16:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129134">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bao1k54NBMJwqlpSsPKYf8IOL0wOQlbWDgvkY40-Kw-NISnPmgwh3rh54kAjWWW6lM2CUuZofEd_ko_19LLiaK9xasB66_2hbV1RZaW7JIyf5mm8f50DKZlvtqvVkGbklmHcz_ixJ5mrjFDDo3WdxFRaQPtAxgkBD6KWN8eBNkmNs7chBz1YvrqgA3_FvUKgGT0Eh6uiTPKt1uPz3h6ZC4IYvsnbH_lSzGoSZ0h45Woimp_R_FqN0rJyv6pp462g951iz9DP2hHkDDB9LK9kEx_rxwA853lU30ns9HCZw2re09E-9o9mz6g0ksDI2xfTOkCOE0eTU1rk8bEj32T1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syhma0QTTxug9n7ZH8W-KwP6SDbyrlzD7f92ulganc45yGMcUlzbxFQ55v22svLiT5rYOCffmMGMgYemP-EY13pV-iu_stBqcXq_z7VB1jD_3P_oSnLRyBiuEPKPBcBShUDY9UjO9bDn4PTsGkRMJDk4pRTrFxwGk72_IRXL-jqlLxbODNHydueUwbQ8_ME1IfIXYa3CnSpEosoX9orub8zN16gpdSOcX4wTgMCVg5Aj5XSKTZINoK1kjS_H_TethkkjeZFmrfMP09SBfyNKkMVOIcqdghfjTU8uIYu6Mr7WbFq1ulVeJpnFY9nmxAbno0ZvlwZTVCLNoI1SRh7o3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصادف شدید کامیون با پراید و فیدلیتی در مشهد
🔴
۵ نفر دردم جان باختند!
🔴
از پراید چیزی باقی نمانده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129134" target="_blank">📅 15:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129133">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
گزارش سی ان ان، ایالات متحده به ایران «به اطلاع» رسانده است که اسرائیل حملات خود را در لبنان بیشتر نخواهد کرد.
🔴
یک منبع گفت: "حزب‌الله آتش‌بس را نقض کرد. اسرائیل موافقت کرده است که این آتش‌بس را به ایرانی‌ها رسانده است و این وظیفه حزب‌الله است که متوقف شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/129133" target="_blank">📅 15:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129132">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
خبرنگار الجزیره از حملات هوایی مجدد اسرائیل به شهر النبطیه و اطراف آن در جنوب لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/129132" target="_blank">📅 15:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129131">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mb5ICu34TgFV0QC2GUhdgLM3LiY2dnUE9AHPuRkHAGwSPFmFbGI1aYaAmvBRZYG2yA36B3F_ly-EmHMFx63hRfNn6lZjXuyOyvFHKDBpbm52g2_HzZlE_IDh7d5AjV7aCCbV4SNjgK4br5kXqfE3pFvyIHwpJpb2ePULXYjFmPc90Osj8oCKVkXp2iWNqhi-Ba8wlxWG1lI443Y7uSxLP50nsPzvsRX8zcnVxMzhIPSLXxqO6mL1bnjisWhEjT-0Q7b142SNUzvojcCKxr9TVGOGkxI2-z4qOsXeCuNQ_uo49XkjoNXA9gfHiNNVuY1M1BMagc6zUKKVk0qkIbA-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفیر آمریکا در اسرائیل از حملات این کشور به لبنان حمایت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129131" target="_blank">📅 15:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129130">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ در پاسخ به منتقدان توافق با ایران: برخی تندروها دیگر محترم نیستند
🔴
من یک آرزوی اصلی به‌عنوان رئیس‌جمهور دارم؛ هرگز نمی‌خواهم به هربرت هوورِ مرحوم و فقید تبدیل شوم
🔴
بعضی از افرادی که قبلاً به آن‌ها احترام می‌گذاشتم، دیگر برایم محترم نیستند؛ آن‌ها تندرو هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129130" target="_blank">📅 15:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129129">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
خبرگزاری تسنیم :  تنگه هرمز رو تا عقب‌نشینی کامل اسرائیل از لُبنان مسدود کنید - تموم مذاکرات رو لغو کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129129" target="_blank">📅 15:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129128">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
معاون وزیر نیرو: متخصصان اتمی روس به زودی به کشور بازمی‌گردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129128" target="_blank">📅 15:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129127">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_sOUqjVFjUUepv5dqgXaxnk4Go1abYPxIPtBqGZl9xoOB3Wj6O1pFtaB4X6xgGjhRyJxqCOdCvURLVK3sW1LWcy4oaITOO4tb7eu_PQqJFgrkhAx4LVsKFRydQmbSXdHglB1zYa8WKip86LWCv_ubwVdRqtv5NklCcjqTRFGL4ISNaUS8ZYP9cLKHTMXRlB50de8yega6MxdRmR6cU8yuHAcWSBMOngB8hB9q0dwLMyIWtskmHoO1safqBWx1W_d4-pdvqlx5AsM703v7Q3TNTfKFs_q_rDredfcOpRZtpHXMdFQbDbkBlqsGyzbUXQ8RaWA3rjElqxJTj8VofKHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی شورای امنیت ملی: دولت باید همین حالا و از لبنان شروع کند و نباید اجازه دهیم مردم مقاوم جنوب لبنان مورد قتل عام قرار گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/129127" target="_blank">📅 15:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129126">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری/نتانیاهو: دستور داده ام، جنگ در لبنان با تمام قدرت ادامه یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129126" target="_blank">📅 15:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129125">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
خبرنگار العربیه در سوئیس: مذاکرات بین آمریکا و ایران ظرف چند روز آینده آغاز می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129125" target="_blank">📅 14:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129124">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc08f96bc.mp4?token=p-1pbZwSsN0Dz_81KFYR3Om9LFnIUG0P8_ZSJJwz6DP_vGACFyEaf5A0090JecyOZaoQzLRQGQxijVPtW2t_-w9vMcChP0KIelZibqIh6ScWopdeijSvslE53OVW0GeG0zMWOhtUDhvCtskXa5TcYjGiTsvUMV6liBOwx5a8KBoPsVmL4WgINu371VayzfOVf4spQOZzpCE85xGELMrUGn6dhVLlfr0Z7dNP3kpw6GNBiHyK3FBtUkxHiNXw2LA3TqazQtf_5AKdMtQZVqaSNbaXQrgPo7LwWZ4PZiRR-dZdIPobzpVD1OmDb3AHkYtQ2gNN8jC97QFNdFyi5x2CKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc08f96bc.mp4?token=p-1pbZwSsN0Dz_81KFYR3Om9LFnIUG0P8_ZSJJwz6DP_vGACFyEaf5A0090JecyOZaoQzLRQGQxijVPtW2t_-w9vMcChP0KIelZibqIh6ScWopdeijSvslE53OVW0GeG0zMWOhtUDhvCtskXa5TcYjGiTsvUMV6liBOwx5a8KBoPsVmL4WgINu371VayzfOVf4spQOZzpCE85xGELMrUGn6dhVLlfr0Z7dNP3kpw6GNBiHyK3FBtUkxHiNXw2LA3TqazQtf_5AKdMtQZVqaSNbaXQrgPo7LwWZ4PZiRR-dZdIPobzpVD1OmDb3AHkYtQ2gNN8jC97QFNdFyi5x2CKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش صداوسیما از آخرین وضعیت تنگه هرمز
🔴
تردد کشتی های تجاری در بنادر ایران از سر گرفته شده
🔴
در روزهای آینده نفت‌کش های ایران به سمت بازارهای جهانی حرکت خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/129124" target="_blank">📅 14:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129123">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d85acc4b.mp4?token=QjAMwi4JI4JkL-nUWG-iJPBtnbDLJourhvLf574aY1RAKdC__clAEwX0B19iFTgSGDeE8rTgZFU_Zz3NPKFipxekAWtPc1J8mIDm5M_9lL84XXUxl_6fd3Gxjr0JDNbwu6MIzQXqRAmGVdgiBf4d_4DSw64ClJLKI1R3bIgI6WADm60ouMAMcF6xz-uQxUwA8-G_ipvUgCau1v7eq6FxV6gNCvXhhdv3jN4SkIWmYaSlopZTyBf3NLhdXm3LJocGORh9pRgWEkwj41xd2tr0kenQG-riM-OcVx_zbdW7LCvezgCBBlfbWyaBJ5Tq1fqiMVX5Oz4eqzzsFgqQv5Ju4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d85acc4b.mp4?token=QjAMwi4JI4JkL-nUWG-iJPBtnbDLJourhvLf574aY1RAKdC__clAEwX0B19iFTgSGDeE8rTgZFU_Zz3NPKFipxekAWtPc1J8mIDm5M_9lL84XXUxl_6fd3Gxjr0JDNbwu6MIzQXqRAmGVdgiBf4d_4DSw64ClJLKI1R3bIgI6WADm60ouMAMcF6xz-uQxUwA8-G_ipvUgCau1v7eq6FxV6gNCvXhhdv3jN4SkIWmYaSlopZTyBf3NLhdXm3LJocGORh9pRgWEkwj41xd2tr0kenQG-riM-OcVx_zbdW7LCvezgCBBlfbWyaBJ5Tq1fqiMVX5Oz4eqzzsFgqQv5Ju4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهر نبطیه در جنوب لبنان در حال تخلیه شدن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/129123" target="_blank">📅 14:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129122">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
حزب‌الله: دشمن اسرائیلی به نقض آتش بس ادامه داده و با ارتکاب کشتار و تخریب زیرساخت‌های غیرنظامی، آن را تشدید کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/129122" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129121">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / نخست‌وزیر پاکستان امروز در توضیح درباره تماس تلفنی‌اش با همتای ایرانی گفت «رئیس‌جمهور ایران دعوت من برای سفر به پاکستان را پذیرفت».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/129121" target="_blank">📅 14:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129120">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS1nNQ41MxQBJVzaqJczRZ2ZcEC_AxhJGErNzrntd3GZl2ZUZYfNRnelA5bNc4Hjfh9FgDEqX8FK6mVbVoXLGhVVZqaESEn1GMK2o0142uOgsBfz0xY9gjktNPuQLSb_zHnQwh16JxNPUir_Z4uRJWH4pPby9xKUmCopadkfjtmhyuqYTpDckVzgTySY8jNJQ1fxwZFT3A2gFwwsNLHrF97frDEo6HJbWjm0ynkGXxhg5051QHgqTAbuYMEHQM8cRm2fA39eQPo1pm_eXaW4FwXhOO7TLqUysKcoCnZv18p9UgVlG05RNMOfvNz_ti-rP4e53Kads2YmOR8J9FZSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، عضو تیم مذاکره‌کننده: ترامپ به تعهداتش عمل نمی‌کند
🔴
اسرائیل به شدت مجازات خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129120" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129119">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orMRMUsk6HSoUJEcfsQVRlFqUXmJvHcMmDhk9YQMFXCX98SE18dhOeCeqTOWoIh7EWeVbV9Jb3Fj97KzDeUFp1WEquaDKeQDSO_tfmVrJMLHOEOCU4t77jh6oBXZdK6jFQyYsWv3E9Em5KH83SnLeuX5K5uqS2mmxKsMApZLNgUYF6jr_NIPZXM6VgYDdMxDC1_RF-xlV5PU8-gBTcfXdT3kSsnBE3mERVpLipruRU5j3r7l87Rs5jX9VqstwjJFD9XpMbTVnf19vkKUjN-b67X45yxa2yhpCaEc85Mog2rAwQJRLptssWhFbowRuL3UNcMJMVhmXRHXWZn7me6Lgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت آبراه خلیج فارس: با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129119" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129118">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری / گزارش‌های اولیه حاکی از بسته شدن تنگه هرمز و شلیک گلوله‌های هشدار به سمت کشتی‌ها پس از حملات اسرائیل به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129118" target="_blank">📅 14:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129117">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30950fe2bc.mp4?token=Bllp5fO2OWacMjftYHFb7Y3lpSlhRoLaPSqBhqjvzjrs0fZ1ZLjtqcrO8mSsZX1tiXztW2y6c8X_5E-htTDqQiSoGRK9NirFU6oshCdGwc5i7a6oB_FAWmPDENdxDSzZvOcGsPNHDCT0_GSKLNiEtXd58b1Jo4nwddPS_C_Q1JsMZrUWbwzsw6Iq-9FJsiZ3bx_eF4pDWLQ_RNEZY0t1Ev5VUDlmAcT76_wb2-LHluQLCr9z3WP56gvFGB_s_RGYPTyC5S2FKdDhCyzbwJ20Y9beYLSDIzuPJXAPa08ZhrYvO8iAxQUH6f7oL_2Zzh8zy-2Cmo5FeBPbI9EkxIrMJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30950fe2bc.mp4?token=Bllp5fO2OWacMjftYHFb7Y3lpSlhRoLaPSqBhqjvzjrs0fZ1ZLjtqcrO8mSsZX1tiXztW2y6c8X_5E-htTDqQiSoGRK9NirFU6oshCdGwc5i7a6oB_FAWmPDENdxDSzZvOcGsPNHDCT0_GSKLNiEtXd58b1Jo4nwddPS_C_Q1JsMZrUWbwzsw6Iq-9FJsiZ3bx_eF4pDWLQ_RNEZY0t1Ev5VUDlmAcT76_wb2-LHluQLCr9z3WP56gvFGB_s_RGYPTyC5S2FKdDhCyzbwJ20Y9beYLSDIzuPJXAPa08ZhrYvO8iAxQUH6f7oL_2Zzh8zy-2Cmo5FeBPbI9EkxIrMJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اکسیوس: آیا می‌توانید اسرائیل را از حمله به لبنان کنترل کنید؟
🔴
ترامپ: بله. آنها احترام زیادی برای من قائل هستند و همان کاری را انجام می‌دهند که من می‌گویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129117" target="_blank">📅 14:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129116">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نتانیاهو : اسرائیل تا وقتی لازم باشه؛
برای حفاظت از شهرهای شمالی‌اش، تو نوار امنیتی جنوب لُبنان باقی می‌مونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129116" target="_blank">📅 14:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129115">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نتانیاهو: ما حمله به سربازانمان را تحمل نخواهیم کرد و کاری خواهیم کرد که حزب‌الله بهای بسیار سنگینی بپردازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129115" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129114">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr_4NZwKN14uRwPlZ21SS-u8xAhBFy3HWSTif0vj7POCukDATwh3sAv8KU2cKlKcZ3FCw7HbfalcrHyrcwlOE-crM2EV0riNQgy-f2NKkKcAKZg1cBKMCLN2Lxw2_BB3JR7XR6i-62RQFy-Z8wns4TQ8Xdu_8D-BtZw_v71NX3gbEeGbZsU_F_qX-vObOS24pjtxi92kLtIFq3XwqBCpqAia3uXkpDbeIt30uxQhP5OeoR701DMQaAGc1Pzp8yzDl7oQwRprHm6LRUSx_vn8nvVRciS454_tu_8mjdgTnkkKc4sBD3V7XUOfT-7-3arCdsxofHqJaSbjcDh_ebN7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل هیوم خطاب به ترامپ: می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی.
🔴
آقای رئیس‌جمهور، شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد.
🔴
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129114" target="_blank">📅 14:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129113">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سایت ردیابی کشتی ها، کپلر: ترافیک کشتیرانی در تنگه هرمز رو به بهبود است و دیروز ۲۵ کشتی از این تنگه عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129113" target="_blank">📅 14:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129112">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmS-pnEseCgwMGEwlgfhSLoILqUCcLml8kYtP2nMO3ke2mmm0XjCG_O5CKGBWROONIAEBf2o3OYlRnaUqW8-eZw5lLn-QAFlPEUjYmNiISypB5WDvib66LmglQcEMuvMBGuq7WUDFzM9pm81q6ngIyQxtGifZgQh6INIIMrXOIDx6aCZCtOBmQ76G9x9lbnzssijSmXWctDTnDhWFwplVLSZuTNWQmlLA2XUW8kmNlr8hyw0wjmm90TuFBkBibF7Gyhc5ZkSqjOVffFNdimDeAQ0Jd_3C2TvbYHyOAM5E9skt8vi1aJcfC9js1-Ovn64vFpWKD_XD7_3ohJA8w3_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش ثابتی به حملات اسرائیل به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129112" target="_blank">📅 13:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129111">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ به اکسیوس:  اگر مداخله من نبود، اسرائیل له شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/129111" target="_blank">📅 13:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129110">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dT3e2LaqfT3udmNvuLlhFyzuFGH_w69HBFy4_o4R3H-MmWiDwQ-PWGbzvJmp3lPVpn1tTbKD4vPCWddMWrT90VoY3HIxvdE-k7kx83ji_SGfqiBTTVBYPekIuqssT4GFUouRGdDjLvFTIDrzEKldzc4h_OtY7hoVMKxJnQkXawIbmhq7O4rZMNNkDqrlrdfy7bSPdL6iPfs7TFWkDSlFZGFXTzHmo5AE6Z7eq89_eYPLYSGQFB-bVcITGFZdnV7AyOurm5HV5c5c9EaGMqjIPPbUuudhpSg7IUpssKolBQ5T3i8YLkcOmje5M8SuBs4XDNmZQJF2onk1oVFJCZL-VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز نوشت: در طول پنج روز گذشته، جمهوری اسلامی ایران حدود ۱۸ میلیون بشکه نفت خام صادر کرده است که ارزش کل آن بالغ بر ۱٫۴۴ میلیارد دلار برآورد می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129110" target="_blank">📅 13:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129109">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ به اکسیوس: رابطه من با نتانیاهو خوب است، اما باید او را کمی منطقی‌تر نگه داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129109" target="_blank">📅 13:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129108">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر امورخارجه پاکستان: هیچ مانعی برای آغاز مذاکرات سوئیس وجود ندارد و مذاکرات باید ظرف مدت ۶۰ روز به پایان برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129108" target="_blank">📅 13:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129107">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
قالیباف، رئیس تیم مذاکره‌کننده جمهوری اسلامی: مذاکرات با ایالات متحده همچنان در چارچوب «خطوط قرمز» تهران باقی خواهد ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129107" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
