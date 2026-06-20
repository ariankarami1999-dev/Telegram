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
<img src="https://cdn4.telesco.pe/file/SiN9eppKdy9R1kn8dBFFCnM8_cvFJs8HQu-8gEu3qkDx-yCd-lG79BXgGKubec4y05PqcldMyA-n4hXF1KmzpJX_BtSKPNe1XIg9FUxTWdinNI2Io8goKbbJBTPExYwYe_BtW813Yqn1xxs04jSLE626k2GR-sQ9ktsHSkh6yeKGdIHlr00kVGAaZa6Fk99g0HmQ19GcZA8WY8b0_Nt53TTwZjOIjhe2WrMIzt2W-8pHKbJZBrxuX4vratI0b2R-C7ZeD8mfWrziI_JXXCMx-DHzvL4WyQTJiGE2O2gvfpF0-Ikr-b2jwOKMs8XW3_lew2YgakyGvziXKnFCSmms1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 221K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 22:41:32</div>
<hr>

<div class="tg-post" id="msg-66579">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=YsJNtsijSH5HsjAAX-vphUBD_zABDgOHlEghH6fJsx3uUZs5Nf_kcQuIBD0dDADFXos65cx1FYdTcrwOK32eYO-P_Diby5479BKkuSDbZDH4twB9fMaYWzhFWXeRhutxJ7jy1LtcTM7p1YdMambz0rXaSIc8bM1e6tXx0oq_6fDUNEgNcYeQNZcyI7AoJlLlRNA97FFLlRyE_vOyd8-larRf7ohfHZSojYexi3H-xcW3-qFo1WTyXV_a2PbfFbHuxqzrefDOXsZwufaGaRi76-NUw3mTGD_Wh1ReiRU4LR5cq3L1RWnItugAVJ1YQobARNMu9hV1zx_gavpVIYqYew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=YsJNtsijSH5HsjAAX-vphUBD_zABDgOHlEghH6fJsx3uUZs5Nf_kcQuIBD0dDADFXos65cx1FYdTcrwOK32eYO-P_Diby5479BKkuSDbZDH4twB9fMaYWzhFWXeRhutxJ7jy1LtcTM7p1YdMambz0rXaSIc8bM1e6tXx0oq_6fDUNEgNcYeQNZcyI7AoJlLlRNA97FFLlRyE_vOyd8-larRf7ohfHZSojYexi3H-xcW3-qFo1WTyXV_a2PbfFbHuxqzrefDOXsZwufaGaRi76-NUw3mTGD_Wh1ReiRU4LR5cq3L1RWnItugAVJ1YQobARNMu9hV1zx_gavpVIYqYew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
جدید: مقامات آمریکایی ادعاهای سپاه پاسداران ایران مبنی بر بستن تنگه هرمز به دلیل تنش‌های جاری بین اسرائیل و لبنان را رد می‌کنند.
یک مقام ارشد به فاکس نیوز می‌گوید که ایران نمی‌تواند تنگه هرمز را ببندد زیرا "آنها آن را کنترل نمی‌کنند" و به حجم بالای کشتی‌هایی که اکنون از این آبراه حیاتی عبور می‌کنند اشاره می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/news_hut/66579" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66578">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=pWauUwj663Q4TR7N8Jb6V31XaaAjt1DFZ6z0PLWy77S1DJdo0JCL6gcJyBi1FpEAKipa7L3uDqSG1EI7L1wmtqRzWKER2uyghqKWJT8X3Z0N6QdJkZxGPl_pYJDTj28IOhHWCMMJYlJkdCV7Mj351e5YwOhjIq-4jrWyuKeAvM771Jiz1oET4jVOFb5pXKQPFvQvvuWmElcZynMkW3p3P01f5ROmmcaD3BydLmzxr2hO0ggp6b__h61XCFKQY8sF03xxJNXc29h46aGAef4FqLLfjrZ_dLLmsYP22oqaXn8cDka7HuWD4jS7Q-5Flwv8nIqdJKtPn8iB4Co8EiybSnpa98KyGB-cmBn0jxxy-fnpLHLABBScCSL0A9NKbhh21EJPmCqgkPpd7g9tmnNW0d5lgBpVSUcbMYVYs2ZWWkB-Cs8mFBWBbmiRfqQm4uXLkb8O9Jlaoq8XMqDVlR8Lxb1vEZLz9rvuSGTTAtpX33ya8ktP6Vhw5JX5H0W3_1QqsLq_QF2ekbXWbhEstSH8phpsRMYjs-dz5cVSP5KGm9k7jUDpFbgSs3MIJVt8Yh13Jtm_M8oIjHi04jVzlYD3X30eC819GbOk0gVlco9KN9GVVR7tT3kELXxZz-zCtc-wfXTsYBHS1wYO3K9OY1P_lSojfyIcTH0mL-UUrnnm5xY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=pWauUwj663Q4TR7N8Jb6V31XaaAjt1DFZ6z0PLWy77S1DJdo0JCL6gcJyBi1FpEAKipa7L3uDqSG1EI7L1wmtqRzWKER2uyghqKWJT8X3Z0N6QdJkZxGPl_pYJDTj28IOhHWCMMJYlJkdCV7Mj351e5YwOhjIq-4jrWyuKeAvM771Jiz1oET4jVOFb5pXKQPFvQvvuWmElcZynMkW3p3P01f5ROmmcaD3BydLmzxr2hO0ggp6b__h61XCFKQY8sF03xxJNXc29h46aGAef4FqLLfjrZ_dLLmsYP22oqaXn8cDka7HuWD4jS7Q-5Flwv8nIqdJKtPn8iB4Co8EiybSnpa98KyGB-cmBn0jxxy-fnpLHLABBScCSL0A9NKbhh21EJPmCqgkPpd7g9tmnNW0d5lgBpVSUcbMYVYs2ZWWkB-Cs8mFBWBbmiRfqQm4uXLkb8O9Jlaoq8XMqDVlR8Lxb1vEZLz9rvuSGTTAtpX33ya8ktP6Vhw5JX5H0W3_1QqsLq_QF2ekbXWbhEstSH8phpsRMYjs-dz5cVSP5KGm9k7jUDpFbgSs3MIJVt8Yh13Jtm_M8oIjHi04jVzlYD3X30eC819GbOk0gVlco9KN9GVVR7tT3kELXxZz-zCtc-wfXTsYBHS1wYO3K9OY1P_lSojfyIcTH0mL-UUrnnm5xY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره با ترامپ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/news_hut/66578" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66577">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=CePrtrtQgtLbPQdtMA9QZHK6VW2rbdznqX6I4F6vWYkovoNXlE2SFven_kOgrCr9oyPUcO2yj3VL5Elso7Uhum4NycGcRMmHa39CGqQgfyjjw0jvLRZlNc6mGHtV6eP73yMuJJ-XY2sjg4lxYOBWlvGTFpl_CbtW4N2JzPqAN2NAEw-k1ZD8QgaONjKA82xsJRYXCwPMHXC43VaafZVPGhv4jzY7xfV-Nont8sJ9tyr2F3WfmVMfDvF4lBdtrA4bZg47LDDPH8DV2XnWigOBWvyQdxbEJGnQjiMGFLcn6Q3laGk237nCaBTOE97QTC7-jCJQzNFkCAXh80AE3DJ-ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=CePrtrtQgtLbPQdtMA9QZHK6VW2rbdznqX6I4F6vWYkovoNXlE2SFven_kOgrCr9oyPUcO2yj3VL5Elso7Uhum4NycGcRMmHa39CGqQgfyjjw0jvLRZlNc6mGHtV6eP73yMuJJ-XY2sjg4lxYOBWlvGTFpl_CbtW4N2JzPqAN2NAEw-k1ZD8QgaONjKA82xsJRYXCwPMHXC43VaafZVPGhv4jzY7xfV-Nont8sJ9tyr2F3WfmVMfDvF4lBdtrA4bZg47LDDPH8DV2XnWigOBWvyQdxbEJGnQjiMGFLcn6Q3laGk237nCaBTOE97QTC7-jCJQzNFkCAXh80AE3DJ-ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرار موفق یک کامیون روسی از پهباد اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/news_hut/66577" target="_blank">📅 21:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66576">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
منابع پاکستانی به الجزیره:
نخست وزیر و فرمانده ارتش ریاست هیئت پاکستانی را بر عهده خواهند داشت و برای تسهیل مذاکرات تلاش خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/66576" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAlqS6TVlzidGu31QOSJ4Ef151VC2lwZHfyHM6ueoraJ0bdQD2jXTIW7Zo9W8d442JEWmSm6yagfgZ2begJmQgQG5qbJQOpwD5S-8QrVATWBJNV_N5_eXWELLKbmqkHzqpzgQgVwGsoma_7MQzIVj03jIF2nUHEYstEseYVP27t1hll66aBH6rAQfVzad6tF-kyoXQ_xuQOB_b-19590ef-OpB20DJwzkUinkDwi05QRNvvJ9AVZSyZkMaKJEyEXKtHEi3hJjUJoG9P4YseFQoBJfr1h-JZtaQ1glnCxb2o4klYkSP5XpU_wjF2BTcqSGV5_5opWaaELQKQMNkGE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8349099df3.mp4?token=cv1a6MCfHZIdY99mrp_z7HdIkhKoV1iSSJzRw37KGCHluv0-1b5fR4kfAwppZZBgICzbnY0F8xktWjQf9vkod0i2j8-t5GnxgfePqYUv24hXzNnsVhIMekKn8UqFVWnucBbNzjMLg1yAL6GSvMVKwhNju3ldsYcfuTyjH9FerzdCJ5-CGdd_f8NR6J1CwKmd9dcBMMCY9Q-vFxYcfF03Q2wnpcW-NUFbe3IE6ePjbA6qh1e2qFlUlCxE5Zt98W2t7pbAxq7XZuHI0bs9gspdLAX57dJCfp1A5HJpHPCaqfkgCgL_DsDpaI7uA8zClmXvqluk_QIRb68PSw2UwlvZDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8349099df3.mp4?token=cv1a6MCfHZIdY99mrp_z7HdIkhKoV1iSSJzRw37KGCHluv0-1b5fR4kfAwppZZBgICzbnY0F8xktWjQf9vkod0i2j8-t5GnxgfePqYUv24hXzNnsVhIMekKn8UqFVWnucBbNzjMLg1yAL6GSvMVKwhNju3ldsYcfuTyjH9FerzdCJ5-CGdd_f8NR6J1CwKmd9dcBMMCY9Q-vFxYcfF03Q2wnpcW-NUFbe3IE6ePjbA6qh1e2qFlUlCxE5Zt98W2t7pbAxq7XZuHI0bs9gspdLAX57dJCfp1A5HJpHPCaqfkgCgL_DsDpaI7uA8zClmXvqluk_QIRb68PSw2UwlvZDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
امروز در شبکه خبر در مورد چرایی مخالفت رهبری با تفاهم یادداشت ایران و آمریکا مشغول بیان دیدگاه رهبری بودم که به صورت ناقص رها شد. بخش مهم آن بررسی متن یادداشت تفاهم بود که علت مخالفت رهبری را بیشتر آشکار می کرده است. انشاالله خداوند ما را در پیروی از رهبری عزیز ثابت قدم نگهدارد.
«ویدیو هم از لحظه ای هست که آنتن از نبویان گرفته شد»
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/66574" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66573">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66573" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyKxEQTSRYbRNnvfSPps8nUzMOVLTgfDH9QRrzV-1ELTQSgP3dJ3SC471N4ZVL6RASEUMYi_7LPJr85cs5IjYUAyATKq4YGjf5SEfTB6eOfD116iToUqDGk4KSr4athBYwkEFP75TCpCS75wWrt4gtbWvBPMmK-LSrCapql9e0ajxBlB_3oWb-L8skjqIbqWWTFFWzqrvnBzFjhdkD8qCgyO2iStMFb379CU7DxjgS0suQuzxECxYWpTn8-ifO5-pgAaZETQr5ZO9DnCd8gs8WX7MtZH7iglZ5R3mMrkSEaEEtS7GS-8VIVqZh7v_jGovsuM5xcJWn3E_aAW4tlBIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/66572" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
‏به رغم اعلان اخیر سپاه پاسداران ایران مبنی بر بستن مجدد تنگه هرمز، فرماندهی مرکزی نیروهای آمریکا «سنتکام» اعلام کرد تردد کشتی های تجاری در تنگه هرمز امروز افزایش یافته و ۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت به سلامت از این مسیر عبور کردند.
مرکز اطلاعات دریایی مشترک (JMIC) نیز با صدور بیانیه ای بر تأمین امنیت کامل این آبراه بین المللی تاکید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66571" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66570">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jx2UAvyY0mxAROgLu6cO3upEUYkjNQyQXjQQYnFxICr1txAzDhz4FTBIV8DcxzYGzjDluXNK4-fu9fN3C4bIaxmYoU0P8vmwNKqPx4zt9ngpcbDi9wUATIHI0HjRRo7XyFkJO7RAVXiCpZ1s5QQBJaNIruAe5f-1u7DWA4u02IQx-FuefoIG3RW4Pn8wrVv2Cz_9ru7WdFZH4KRBe7TDI65QjrWlOelqIenHEDF-SY4gAu-kOG5PfQi-lywdIXTPRJEt72ddWDckFmbepsr6oJOwi9gEJAcb6sc1_kBsHK606n8xH1sI17RN0BH8fLqdJk_fR8Auv0eIDlx-qTKaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
جی‌دی‌ونس برای شرکت در مذاکرات فردا با ایران به سوئیس سفر خواهد کرد.
قالیباف رئیس مجلس نیز در این مذاکرات حضور دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66570" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66568">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrpLqEEJh2oVGr0GkF9T2GfgbIGgC9ehXVqwKvHPgyqwOP8cAtyqDRkcel5OFNGGdfPkpvmEoDLEHzSgG_FxDmr-fooXqR-R8uZPT7VDBLfqFVvE3depg6rSrGfC68ADtMgUX6pC4pg3E14U3Q50fH7iU6U3e6Rpgvgcfos18OO4Zj8TZxM_LhPlYlURPm_Iap2mnErX59GMpHEHUK2Xk_SkX4DYxT9dwxnqP5rVSlytIVzAeeUD-dIU9gE-TDka9q1gpOPoPEkNODd1nPd3pM9jiSBg2llAitbrbdvF7SNujHE3Gb3lXGY37enHV2ft3fIQZ7DoVDuFx_F4l9bQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=VOl-GvfoibaEE_Njmu9NFXwmOcCXSx7i0QPE0Sx0SSInNF068Cv1Oe98mNY_zSwmvsgsmL_qQfLcnXRKLagdEztXMMviX_lfyz03gWiezbstvH1om0IR64sMRDzZReY9lBVBshjWLj33oKJzoUJxDXJzrOiwiXpEve0ihVL3KlCMgejaPQr52DNse7W79RTltHA5tvBlF2OKsbve7NuXFeUYxaUxCGKUnH-_QJ5P821qFHgo0QVHs-po6yqYNo7QfFn9YLLvR8cOuG6g3L7rsvRmFOUj5fcDP_emCE2RJ3JyVokIvtakS-IuRYqhfeFZ5v4g8XIZwcZipa314b92Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=VOl-GvfoibaEE_Njmu9NFXwmOcCXSx7i0QPE0Sx0SSInNF068Cv1Oe98mNY_zSwmvsgsmL_qQfLcnXRKLagdEztXMMviX_lfyz03gWiezbstvH1om0IR64sMRDzZReY9lBVBshjWLj33oKJzoUJxDXJzrOiwiXpEve0ihVL3KlCMgejaPQr52DNse7W79RTltHA5tvBlF2OKsbve7NuXFeUYxaUxCGKUnH-_QJ5P821qFHgo0QVHs-po6yqYNo7QfFn9YLLvR8cOuG6g3L7rsvRmFOUj5fcDP_emCE2RJ3JyVokIvtakS-IuRYqhfeFZ5v4g8XIZwcZipa314b92Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏پهپادهای دوربرد اوکراینی پالایشگاه نفت تیومن (آنتی‌پینسکی) روسیه در غرب سیبری را در فاصله بیش از 2000 کیلومتری از مرز هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66568" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66567">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB7ELjcqDxXK1CnVtX-OkMBsxpzt40Gasgj2J-d0DNQtVGeQEPUrpTK661JDz5-Y-hjthsWd_QfeDJvd5Srw6foSWbfQE_lup1s_6JUbggOf3oKfxAnPhn2rASisDkho74nXnhyPMPY9NXekBrQmHSEmfqNvAJPdf1Jw-ZJASo48HJLV_BnTjr3l3CYdlHhtUjEF-2ciWMdRFzWzHKpDzitTycN8TUR9DmyIG6Z1UDFP6X4dW0Z2e_9YLO7Chqbt9k3CxgWGxe5sevtz-N9czNJbRI3lvGMON74Cw060HJ0dxVW2gthkKkfmSjWUX03rMAdl3Tg3nI2rXyEQOL1juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛الجزیره به نقل از کانال ۱۲اسرائیل:
نتانیاهو و کاتز به ارتش اسرائیل دستور دادند بدون عقب‌نشینی از مناطق تحت کنترل خود در جنوب لبنان، آتش‌بس برقرار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66567" target="_blank">📅 18:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66566">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUGVl9CLfy37So5sqBBMYbxXLuD9sCzFw6LinaXl-7w3ouprur9EyLxezhCtXSUdbfg2oUjplZ_X0oHAvAtz1UzvIPu9WAmjRLpr3If-1vgdT3-E_4zWN36eSe3jfMstchkkL8s9XV7U0cjWFdnAAM1UhsnFRJ6zPfF6Shy97y5dznAhdujuoQ8Lu3WgE5-8sFyI-JwjQ4CirCk1_OhiMJbEHRmYUIaZ0DDT-qs2V-W7zMeZ8HPlQF0FM8xPoRQnyHYw7q6qwa3qMmYFe_drpJ4nP7UnMvqFvfzHsXY_jRqLs7N2JS1gEdv6msV0803FjUb91Q_PZx-eJJCM9k9lPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی عضو تیم مذاکره کننده:
جبهه‌های نظامی و دیپلماتیک دست در دست هم کار می‌کنند. تفاهم‌نامه باید سریع و به طور کامل اجرا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66566" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66565">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDsTo0FJ0Yci8VQyCiPWwwfyNyX6VRWeYL4zYDoLo7pwhLcPxOCcvnSKBGKktdlGr8_ta_2UG7GCgKU6zMJqxuc51TzPmFMQE7_pTtvSW2ulKX4YJwWGBwATFdGnIh4cQpKDuMNmfgpUrRHkLIdfPFSVXcUIDOIHXjZGPVFTN7btfq4oM8dAXPL9EUVyT1UyYcgYzjojHfHMjTBCjQEcxvlDuQ7Br9e2kW8BQLIQ97-aqbsaHnrjDrJvplKMpe7lBoOdjXprhjbFBFMBRvRMpsJTPwjJ2Slm4HUXzyzH1pqs-dzsMDDQ3mS0G6L5CNg9Xg2beG27tx0ERSdLCq0o5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ دوباره به جورجیا ملونی، نخست‌وزیر ایتالیا، حمله کرده و گفته:
نخست‌وزیر ایتالیا، جورجیا ملونی، در جریان نشست G7 در فرانسه بارها و بارها درخواست عکس با من داشت.
او در ایتالیا وضعیت خوبی ندارد و میزان محبوبیتش پایین است، احتمالا به این دلیل که در موضوع جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران، از ایالات متحده آمریکا  کشوری که واقعاً ایتالیا را دوست دارد و از آن محافظت می‌کند حمایت نکرد (البته ناتو هم همین کار را کرد!)...
حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، او می‌خواهد دوباره دوست شود تا محبوبیتش بالا برود. نه، متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66565" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66564">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه پاکستان اعلام کرد که مذاکرات فنی ایران و آمریکا فردا در بورگنستوک سوئیس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66564" target="_blank">📅 17:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66563">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66563" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66562">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
اسماعیل بقایی:
هیأت مذاکره‌کننده ایران تا ساعاتی دیگر عازم سوئیس می‌شود؛ این سفر در راستای پیگیری اجرای تعهدات طرف مقابل انجام می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66562" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66561">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
بقایی سخنگوی وزارت خارجه:
ما به تعهدات خود پایبند بودیم ولی طرف مقابل به تعهدات خود در موضوع آتش‌بس در لبنان عمل نکرده است
-طرف مقابل موظف بوده اسرائیل را وادار به آتش‌بس کند اما این اقدام را انجام نداده است
-اگر طرف مقابل از ایفای تعهد خود سرباز بزند، ایران نیز مقابله به مثل خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66561" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66560">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
❌
قرارگاه مرکزی خاتم‌الانبیا:
در واکنش به آنچه «نقض تفاهم‌نامه پایان جنگ از سوی آمریکا» و «نقض مداوم آتش‌بس از سوی اسرائیل در جنوب لبنان»  تنگه هرمز به روی تردد شناورها بسته خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66560" target="_blank">📅 17:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66559">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد بسته شدن تنگه هرمز نخستین گام در پاسخ به «عهدشکنی دشمن» است و در صورت ادامه درگیری‌ها، اقدامات بیشتری در دستور کار قرار خواهد گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66559" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66558">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛قرارگاه خاتم‌الانبیا: تنگه هرمز بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66558" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66557">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e32956668.mp4?token=C6GYF2mFf8rGM7bb-t-_F9Ooe2zhlua9pBWf6bsV5dVgI5MwKn5rdAbx8t8ye8NtKxejel1tKQrz8WT5Z295nvBPx8FAm1JdXqKPqwX45PmWJ7323waOKaozMnbn3RuI7GaxVj3OdaMz61bdk91gP7xDzxqEy7jriDtvMePTl9HQypQ5PulGwKit9qxXeeq7WJlVM_BgTSqBL4MzVSCpbqsgwhpUCZM0oxQGtxoRT0zCdbyFjQEh8_h5I1I3SoWoIjtTVTTD9D2QPW0KodQMzCxOsHLDNPYz8g2oL3PLVwQvO7RG4HOTc9CJGq72o8Cg5YIVUGVTutnBKUnZyOFcvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e32956668.mp4?token=C6GYF2mFf8rGM7bb-t-_F9Ooe2zhlua9pBWf6bsV5dVgI5MwKn5rdAbx8t8ye8NtKxejel1tKQrz8WT5Z295nvBPx8FAm1JdXqKPqwX45PmWJ7323waOKaozMnbn3RuI7GaxVj3OdaMz61bdk91gP7xDzxqEy7jriDtvMePTl9HQypQ5PulGwKit9qxXeeq7WJlVM_BgTSqBL4MzVSCpbqsgwhpUCZM0oxQGtxoRT0zCdbyFjQEh8_h5I1I3SoWoIjtTVTTD9D2QPW0KodQMzCxOsHLDNPYz8g2oL3PLVwQvO7RG4HOTc9CJGq72o8Cg5YIVUGVTutnBKUnZyOFcvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چه قیافه‌هاییه که ساختین
😢
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66557" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66556">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">باورم نمیشه ۵۰ سالشه
😐
🔥</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66556" target="_blank">📅 16:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66555">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=czTgNq5bHjXiN6bacMpp_V_JwgfYE8U8Edbwrem5NveMrAG41b1vmiCjAtnUbT0QJy3vuFflQWYQArLpYDNaNgMf3AjcmXq5DMpTRrUwAKm8c4dF6VSo7WXZ1k0QP0Y-d4HTMh2oU1RJlXQ-XC8gByex4PNyyWGXY7xAqz0zdZ1UbWGdv1nqs6mfQKAFcpyNzyT3H9gcHv0NT0f2LaSAYdJt7_XxlLkVqs1MIP4jTjrOCX9uELPmHByIwwqSzBZ-pfFLTCukWqG1rIdWuvYAdt3Tc2JNUde8aHeJkZnuhPfUNrzFmcyvW-nTH4EIg5UvsZXJIDuw_CcbIRVufzUd6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=czTgNq5bHjXiN6bacMpp_V_JwgfYE8U8Edbwrem5NveMrAG41b1vmiCjAtnUbT0QJy3vuFflQWYQArLpYDNaNgMf3AjcmXq5DMpTRrUwAKm8c4dF6VSo7WXZ1k0QP0Y-d4HTMh2oU1RJlXQ-XC8gByex4PNyyWGXY7xAqz0zdZ1UbWGdv1nqs6mfQKAFcpyNzyT3H9gcHv0NT0f2LaSAYdJt7_XxlLkVqs1MIP4jTjrOCX9uELPmHByIwwqSzBZ-pfFLTCukWqG1rIdWuvYAdt3Tc2JNUde8aHeJkZnuhPfUNrzFmcyvW-nTH4EIg5UvsZXJIDuw_CcbIRVufzUd6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
رهبری سه بار در موضوع هسته‌ای به تیم مذاکره کننده تذکر دادن و گفتن «در موضوع هسته‌ای یا باید به پیروزی برسیم یا اینکه برای همیشه از دستور کار مذاکرات خارج شود »
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66555" target="_blank">📅 16:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66554">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=H_CyeK2xd-mK7pOlufVNUFkqlYJ-JD6c2XU4h1XqA1gkRNhP9d4152RDMMr_UsNWYLXdcQ8SJsDtCFLdNvGnA9J49hf3wxcJFt6o3OHrXs7WndcS7WpVzVECmhDhrk-vfcMEjh50wCKZrWt4-BNDSGt7XUBuLAuMpEZISYjFeRbu8ORpRbK47SGRA-RvhfMnSIX-ywIu-ZeBP9Irumq81rgi7Qah68oAqXw37ZHAdSDuw6_1kZm4z3BCNvS85unBgMDmR1uz5ZsiqHtBViaTk4KZ2LevK1u8DPWPNxFAyvcjgXq0aFNlmslZYT0m5n2F458gflXr0VQYD0pFbPAtuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=H_CyeK2xd-mK7pOlufVNUFkqlYJ-JD6c2XU4h1XqA1gkRNhP9d4152RDMMr_UsNWYLXdcQ8SJsDtCFLdNvGnA9J49hf3wxcJFt6o3OHrXs7WndcS7WpVzVECmhDhrk-vfcMEjh50wCKZrWt4-BNDSGt7XUBuLAuMpEZISYjFeRbu8ORpRbK47SGRA-RvhfMnSIX-ywIu-ZeBP9Irumq81rgi7Qah68oAqXw37ZHAdSDuw6_1kZm4z3BCNvS85unBgMDmR1uz5ZsiqHtBViaTk4KZ2LevK1u8DPWPNxFAyvcjgXq0aFNlmslZYT0m5n2F458gflXr0VQYD0pFbPAtuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
فاکس نیوز:
بنا به گزارش‌ها، استیو ویتکاف و جرد کوشنر، فرستادگان کاخ سفید، امروز برای اولین دور مذاکرات در مورد توافق هسته‌ای احتمالی ایران در سوئیس خواهند بود، در حالی که اسرائیل به اهداف حزب‌الله در لبنان حمله می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66554" target="_blank">📅 15:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66553">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=UelRZB1X05LpP_7C0iLp1TUHO_c7r_pip3y12ukVx4Av9qhEQp70KI4xPnOWjWzy_oAfSVNsblKpWetoMtOpIjzfaf1PJ-ElAn8LDNHZzP_fGZBMdYm-ij2I_C5F2ATByylQ82Yrd4iw0gryPX8LXBIXvrYBy6EvM3KoKjjLrIfPPqROtDMZw6bS0xbBUeTOqryGlwUQPYEhFvY8QPvWGxC5DZwhEjQO-3tpTpSqo0I5Aa4Yq3Q8F99jYSmSa9Tdr891KKeA19EbvBIShrd4wA6PpRbMdTJmWm4QhYiFb-5Pa7e8A4a83lHHSLvLiDAKUNQ4x4tiXitN1Buz4OGlaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=UelRZB1X05LpP_7C0iLp1TUHO_c7r_pip3y12ukVx4Av9qhEQp70KI4xPnOWjWzy_oAfSVNsblKpWetoMtOpIjzfaf1PJ-ElAn8LDNHZzP_fGZBMdYm-ij2I_C5F2ATByylQ82Yrd4iw0gryPX8LXBIXvrYBy6EvM3KoKjjLrIfPPqROtDMZw6bS0xbBUeTOqryGlwUQPYEhFvY8QPvWGxC5DZwhEjQO-3tpTpSqo0I5Aa4Yq3Q8F99jYSmSa9Tdr891KKeA19EbvBIShrd4wA6PpRbMdTJmWm4QhYiFb-5Pa7e8A4a83lHHSLvLiDAKUNQ4x4tiXitN1Buz4OGlaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله هوایی اسراییل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66553" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66552">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJQ4Af5l0pM3ufgj31HLyVQ_jNGxixWN0zS4pNncPNXOu2UUqMnMTvIMCOBRHW-IMER7M_FgltX_YmSzrruZlpGHPSJVCK6usrroKMobviM6boe2USlOvl9vMXR-JZIzmK9Ua8nx0IMWTnwxmrUI3W3BuJoeDNmnDNwTRNiA5TyhWYkV0KVFX4juaCtl5r-s2sw7LbuUMdlONmrgRQSz57vuz3hnu9DfqDNmw4LBesw-U1hgSlXx2Iht8gPyIGMDsOUJ6Q2wOrXOgmNLhRxT8TNQoiMh6GExBv9qzlUag9xiMJzqfGLU03dG0hymkuGZsDCeDEMJpiNKPiouVKbnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:
نقض مکرر آتش‌بس: حزب‌الله بیش از ۵۰ موشک به سمت سربازان ارتش اسرائیل که در جنوب لبنان فعالیت می‌کردند، شلیک کرد.
به منظور رفع تهدیدها و در پاسخ به نقض آشکار آتش‌بس توسط حزب‌الله، ارتش اسرائیل در طول شب ده‌ها پایگاه زیرساخت‌های تروریستی حزب‌الله و تروریست‌ها را در جنوب لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66552" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66551">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66551" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66550">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXcpZJbLQOk0_xOofbUe_vgU_TnXZHko3ncC0wljj-inOoBjwX0UNWfOWkoRJXE0YDP4C5whrr1_g2fWHU5HyhIfe5sGP-Z5jxq2tp5YIflZBoG3JIABtUrtsAJOU2fHOP3oiwkQfQa6BE9ZlJwBx-SHf26G1GNshxeGMvkn0obYeNOOKiSHNOP73PdpJ7askMR0KIukiDP1D_vn5HsxwsMjZo655LyeZV46GiF0CdvhW9IBDSSPoBcKWcA1KyABc85YZotHtxF4t0dtHEzTql3wyAhoiHXdpCjKR2WWM7AuHKutbSp_-mp9DCraZK0Ohbdbm213qBMyHyRJ-e1abQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66550" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66549">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7zVc0gmxAdwrdyyzN_PsSHXboTA46w-iQM1jLKSdF872SXn1NehdQV9K93oB0nLC3AeBwhunrRzC3l6dY1PhRHm_PkzznwGG4eJG6iFtJnthIVdfCiNoI_2_kfA9doUARU7cbnQ37QbNJW8UTZeLmeCXUmK-JeTnlXRL44ZpsA0gtzEBZsgpC7xIZB1ccUbr5yGCHckuVTpUVUfxhnYFXHRkgroh_U2DhZBVTFYdzJsXp3QaeLnzCL9kyMx2ZTbEtrJGM9IdvHwwwyi9uF3xm-Ng1kNrgT5JJQosIJAIbyYFu1L5AxJBYyRkvAYWZR_hvgQvv4hmARaF414n_iaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چپ‌های رادیکال احمق و دموکرات‌ها بالاخره فهمیدند که ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد. اوباما فقط به آنها میلیاردها دلار نقدی می‌داد و هرگز از ارتش خسته‌مان در آن زمان برای انجام کاری که باید برای مهار بزرگ‌ترین حامی تروریسم در جهان — ایران — انجام می‌شد، استفاده نکرد.
آنها هیچ احترامی برای آن قائل نبودند. آنها او را، مانند جو خواب‌آلود بایدن، رهبر ضعیف و ناکارآمد می‌دانستند — و در این مورد ۱۰۰٪ حق داشتند.
ایران به مدت ۴۷ سال بدون مجازات باقی مانده بود تا اینکه من آمدم. و سپس همه چیز تغییر کرد. آمریکا بازگشت!!! رئیس‌جمهور دونالد جی ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66549" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66548">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
شناورها در صورت رعایت نکردن مسیر دریایی جنوب جزیره لارک،  ممکن است با «خطراتی» از جمله برخورد با مین، تصادف دریایی یا هدف قرار گرفتن مواجه شوند و مسئولیت آن بر عهده خود آن‌ها خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66548" target="_blank">📅 14:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66547">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXkopTs0BPYS6hFohEBSehhkZGiQQEJ_jej0tHtHqWyZENT7E7DtjAZvopgJKwux4rCiHq8DaPn3PUtB5EUY47z8FURiLsNfZQQCZX7DnXHtjOl4Z3UDGndYeS4d6T-fnEJ0pndAsalVMtRtzArKy3sidtXFuRBpXmLE2M8aCZgOXnK1yeM7ufFQXDAi1grHX9wb0Sk_bGKSvrkMPOPMLz8xpcCADkniuaKJYBP4-VQUB897FF-CoLne-1jfaoD740IGrzF53Jwb98bWilPL4LVzv5wGlwn3IfECImosgMiCUL6TMzurs6vuU6e_QUPAZDImnnLQZP6vjQdx-1_b4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
هیئت ایرانی در مذاکرات این کشور و آمریکا تهدید کرده است اگر حملات اسرائیل به لبنان ادامه داشته باشد، تهران از مذاکره با واشینگتن صرف نظر خواهد کرد.
این منابع تاکید کردند مهم ترین مسئله اختلافی ایران و آمریکا پرونده لبنان است و محسن نقوی، وزیر کشور پاکستان، در این زمینه پیام هایی را به تهران منتقل خواهد کرد. نقوی روز شنبه وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66547" target="_blank">📅 14:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66546">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
نیویورک تایمز:
منابع غربی از نتانیاهو خواستند حمله به لبنان را متوقف کند تا ایران خروجش از مذاکرات را توجیه نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66546" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66545">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8c_sI4bhpD3XlcUC4C3Fm1ONNWynX_9FsHirWI9tlJysgPmAacUXFG0lQnhquIt66zeHGL-GeQ0IglieoMfwg2vSwAMIzPXlwXsDFUOvKFjlj41dAYUeIsWu5x7k01YX4uWNUlzYUem2ELCeJwQCE2sQIrGN3lPUed1dyqMiCpqOX4wnvtnFWoAqLouf4D0Sj60yU24vv4lPkDBPLg-f1jiNRP9RtQ_BdCOQnAUC_C7YKF4ntKSKRLhDvXKPtpoe0_ybSs9vE-ud935cazBLcHcFEABnKpVm28fTmb41fjSefm3HOGUzRFEVWNbv5kkgagXGp0yYQ_wKyLlL5NReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رویترز:
توافق احتمالی ایالات متحده و ایران برای پایان دادن به جنگ و کاهش تحریم‌ها می‌تواند سپاه پاسداران ایران را به طور قابل توجهی تقویت کند.
سپاه یک امپراتوری تجاری گسترده در حوزه‌های نفت، ساخت و ساز، کشتیرانی، مخابرات و زیرساخت‌ها ایجاد کرده است.
سپاه پاسداران در موقعیت خوبی برای به دست آوردن سهم قابل توجهی از مزایای حاصل از صادرات مجدد نفت، سرمایه‌گذاری خارجی و یک صندوق بازسازی ۳۰۰ میلیارد دلاری پیشنهادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66545" target="_blank">📅 13:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66544">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
وزیر کشور پاکستان برای دیدار با مقامات جمهوری اسلامی وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66544" target="_blank">📅 13:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66543">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTFKrpLbsUTt3VrGIUzYrmTaC-3UPhAjoqG4JjvP3V9Xhi-2vOIfOA400zctzFX4-9YyztLlSb-QG4AYv9jpqTQX5vx6wcZBUkj70bQSc_zfkSaAtKquHE0sfWtR9Xgv2mXNbPJau_axV-o-eyQrTXxWL4AZ8JOFmVunYlhnrNoyIfTgmACtSyl7AbBpQXaLCooqdrbmq7HFuHsK0nY6y4ajXUNGxdoP6BHe5phIMu_2FAA-968nyloD42hTBtLGWA5A-CabnKpuS7jANdmtqLT8mGiH1wVgDeX_Bb8HQ0ucDu-lF4MvOEjf3EYOIxbAD7AWxeYbOTMbvA4dh4ZAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابی از حملات صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66543" target="_blank">📅 13:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66542">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrQyu_9bC2V9JG69shEaRJbMN-of0J7fvIYlPWMD1wmsx0F5lvAGwcFiZkI8OaLGyHsSdSfb_g66o-0jws8e-gpIGNLwnUpgnVGV5Uv9Ir-9A3b9EJVcw1lsVjfKNONvsWaVVhmdiGOSPm7rrjjXD4ivvIG5bJwWKlqF1-1TC1z7TMbl9RfUjLzraYneSdTUXWgADd5Yn6G9ErylSk0uHqXqPW0iQS6mPRQ6xAjB46hha0ZvaW473aYzVol16gI6B6HFNvoT7G3rreWku8KNlACvyxPX0fiQV3Jx4dCJ2cynGjVb7NUwspIAofQ9IB14z5NX1WKMGbHJzMyTm357EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتاق جنگ اسرائیل:
نیروی هوایی اسرائیل در واکنش به ادامه شلیک موشک‌های حزب‌الله و نقض مکرر آتش‌بس، اهداف تروریستی حزب‌الله را در سراسر لبنان هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66542" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66541">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417add4a63.mp4?token=P3zHPcDp4y7kSuQqpSOETteZEiaHFpapcbySd5nTztKqeJ4MioYPBYjbmA5GohWPVV-2OkZzOcaZq84mR5u89Czp6-nIbVmH9fTx9UTu9xHBdxSiCu9exf6SjCoLZR5ckH094FAfbG9VXYkWdaaOuwzvXK7T1FC7vLGtUV5L1MFfDbZ2fZaEcMQP44OJhbVLH7jrT00InYA0PpW4SGyG4oH9nnHXWCKovtQ2VGX1k4jgb-52zrQZDEXkDut1CvTqbbrGZguUa7fqxTmTj1aFvUBRaw83XRHJVVggL76yyEKPu9VVLsDv1FVMyoGZer5UgSHKCmjMNIPFJmZC-rorGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417add4a63.mp4?token=P3zHPcDp4y7kSuQqpSOETteZEiaHFpapcbySd5nTztKqeJ4MioYPBYjbmA5GohWPVV-2OkZzOcaZq84mR5u89Czp6-nIbVmH9fTx9UTu9xHBdxSiCu9exf6SjCoLZR5ckH094FAfbG9VXYkWdaaOuwzvXK7T1FC7vLGtUV5L1MFfDbZ2fZaEcMQP44OJhbVLH7jrT00InYA0PpW4SGyG4oH9nnHXWCKovtQ2VGX1k4jgb-52zrQZDEXkDut1CvTqbbrGZguUa7fqxTmTj1aFvUBRaw83XRHJVVggL76yyEKPu9VVLsDv1FVMyoGZer5UgSHKCmjMNIPFJmZC-rorGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوس جواد مینوازد
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66541" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66540">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=pjNHMs9qtLIRlV47A1VXKuHtX83FdvIai1dASQTfKSJU2eaqG0cwn2F-g9F7RoLe_qoDCRIwU-c-pkKbLK7qxiOsxxjkUeRHjrnt3EIQpuI_nZzZgee0ENb66fJbxuC8RX3brxoATdc_l6172qg-qGOubXpcXeUrqZVRH1URu9rxr5ehPTGxbHG3FuwLvILQ90V2EURyDsQpU0CTSyX9_D0jD2BVFYlfum9g9_0ROIzPrsoHovo7lrpEXKv7SnVNKH_Zxb-Co4YmswYalaGJM-5nh3A9N6KBXU7dWJ1N6SX0yJhpCZ6_lPsmWiJ38fEeFZM1EGDHqqquAOwvGAsEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=pjNHMs9qtLIRlV47A1VXKuHtX83FdvIai1dASQTfKSJU2eaqG0cwn2F-g9F7RoLe_qoDCRIwU-c-pkKbLK7qxiOsxxjkUeRHjrnt3EIQpuI_nZzZgee0ENb66fJbxuC8RX3brxoATdc_l6172qg-qGOubXpcXeUrqZVRH1URu9rxr5ehPTGxbHG3FuwLvILQ90V2EURyDsQpU0CTSyX9_D0jD2BVFYlfum9g9_0ROIzPrsoHovo7lrpEXKv7SnVNKH_Zxb-Co4YmswYalaGJM-5nh3A9N6KBXU7dWJ1N6SX0yJhpCZ6_lPsmWiJ38fEeFZM1EGDHqqquAOwvGAsEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66540" target="_blank">📅 11:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66539">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4121482563.mp4?token=somjypIJQkeXmQnY6A21d8xpjQ5rRhWbOqMhtNx9fqa_zeJfVQ_3K1Q_-op8baN7DdjTiC-v7oSDJh72t_Cc-WbrEyiHIBdftHQ6gVQm22bnK0ziLC38BO5-dMBQh3-8ouc3_gZEmi4V3XYDEq-OYYFxD0-kKm_bPK9mTMOcV-7SEwnYnpIsbNGiEAT0zWY01pUQiOkucgzHc4552YomLUMVSQWimRJtbJsCpKJjC5GtSscICr1XlwvN6oXb0FglCqI0htlCFZO2i2ficx0n2sGiinHn4EZq3u98CbOLHDkyoM7_OOCKA1X4pZ58LH9izge6Se9NLQutsQzLRsSD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4121482563.mp4?token=somjypIJQkeXmQnY6A21d8xpjQ5rRhWbOqMhtNx9fqa_zeJfVQ_3K1Q_-op8baN7DdjTiC-v7oSDJh72t_Cc-WbrEyiHIBdftHQ6gVQm22bnK0ziLC38BO5-dMBQh3-8ouc3_gZEmi4V3XYDEq-OYYFxD0-kKm_bPK9mTMOcV-7SEwnYnpIsbNGiEAT0zWY01pUQiOkucgzHc4552YomLUMVSQWimRJtbJsCpKJjC5GtSscICr1XlwvN6oXb0FglCqI0htlCFZO2i2ficx0n2sGiinHn4EZq3u98CbOLHDkyoM7_OOCKA1X4pZ58LH9izge6Se9NLQutsQzLRsSD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
‏ترامپ درباره کشته شدن قاسم سلیمانی:
اسرائیل در آخرین لحظه، زمانی که من سلیمانی را کشتم، از عملیات کنار کشید. قرار بود این کار با اسرائیل انجام شود. یک عملیات مشترک بود.
ما ۳۰ روز روی آن کار کرده بودیم. او فقط با هواپیماهای مسافربری و در میان تعداد زیادی از مردم سفر می‌کرد، چون می‌دانست ما آن هواپیما را سرنگون نخواهیم کرد. می‌دانید، هواپیمای نظامی قضیه‌اش فرق می‌کند.
او سوار هواپیما شد و همه چیز طبق برنامه پیش می‌رفت. اما یک روز قبل از عملیات، اسرائیل به ما گفت که در حمله شرکت نخواهد کرد. من هم این را درک کردم، چون برای آن‌ها چندان مناسب نبود.
اما من سراغ چند ژنرال رفتم؛ نه آدم‌های نادانی مثل میلی و بعضی از این افراد که واقعاً آدم‌های احمقی بودند و تصمیم گرفتند تجهیزات راجا بگذارند. من هیچ‌وقت تجهیزات را جا نمی‌گذارم.
به چند نفر از افراد کاربلد مراجعه کردم و گفتم: “نظر شما چیست؟
آن‌ها گفتند: “می‌توانیم بدون آن‌ها هم این کار را انجام دهیم؛ نیازی به آن‌ها نداریم، قربان.
پرسیدم: “آیا به همان خوبی خواهد بود؟
گفتند: “به همان خوبی یا حتی بهتر.
و آن حمله بدون هیچ نقصی انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66539" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66538">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=WePaD2_p1JFvHSLloG8smPfQA2x2__n2nswpneAelsHMTsl7HxUY1nkcZ-NU0m9Oa8OQPQaKG5BOwy8QUTo7HVM37BO-d3X3ZUyXd5iggZSk417-s9HA_RY3sH7Jml5GwOvaNEGY3jxvWu1FgI1v6imSAWwHUXT-JI0Lqe0OJCclcfJG_kdHZSdHZ-iToiH4ByUrbGXgt3SskEUGOryTiRZiSUBx-eKak4iV_pzefuRPwO3fRxiNync5O239pDqkaUj0WjRGY-QtsI505jGpUzqd0Lvn-Wcs-dWh8VdjiPfJBb-X8tZjoOLz5tifP-WrAE2cmbEC05Y5e8aBzy24ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=WePaD2_p1JFvHSLloG8smPfQA2x2__n2nswpneAelsHMTsl7HxUY1nkcZ-NU0m9Oa8OQPQaKG5BOwy8QUTo7HVM37BO-d3X3ZUyXd5iggZSk417-s9HA_RY3sH7Jml5GwOvaNEGY3jxvWu1FgI1v6imSAWwHUXT-JI0Lqe0OJCclcfJG_kdHZSdHZ-iToiH4ByUrbGXgt3SskEUGOryTiRZiSUBx-eKak4iV_pzefuRPwO3fRxiNync5O239pDqkaUj0WjRGY-QtsI505jGpUzqd0Lvn-Wcs-dWh8VdjiPfJBb-X8tZjoOLz5tifP-WrAE2cmbEC05Y5e8aBzy24ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تهدید به قتل پزشکیان توسط مداح حکومت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66538" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66537">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=tig3XI84VEtWHNUHuPkgbXD0dM3TQDUhiUNLLlxlebu2xfz_gck8L7nXygENKK73iHd6OdhFLRXRLoLw2gnevdl2YR3AqmfQNZB6dnwYPMaZf2MaovffrwWBWEJ38R-XTmIdOzdRdV8fxjlqS1LIAsl5QKS1yQvAJ7Los6h0dGqCz6vgbuCB3Sa_uuIZ3Cv7ojIpbHqyVCGvssCXtPQkRy3ue4MIbcipCuHKhl6qKDnss0JCBhDw5848TFtg2HpPXPgCNTygvKiczrf05tONyu9mtSez5w6y7Y7ozG74pmL6IoGtEh4Gt8FJ50tLs2aixiobjNx2qbUB8riWAi6y9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=tig3XI84VEtWHNUHuPkgbXD0dM3TQDUhiUNLLlxlebu2xfz_gck8L7nXygENKK73iHd6OdhFLRXRLoLw2gnevdl2YR3AqmfQNZB6dnwYPMaZf2MaovffrwWBWEJ38R-XTmIdOzdRdV8fxjlqS1LIAsl5QKS1yQvAJ7Los6h0dGqCz6vgbuCB3Sa_uuIZ3Cv7ojIpbHqyVCGvssCXtPQkRy3ue4MIbcipCuHKhl6qKDnss0JCBhDw5848TFtg2HpPXPgCNTygvKiczrf05tONyu9mtSez5w6y7Y7ozG74pmL6IoGtEh4Gt8FJ50tLs2aixiobjNx2qbUB8riWAi6y9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات اسرائیل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66537" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66536">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=UQ_nzFiHHr9V2-r8i3IdEXPV7MIt_lpvMR5CPXgAm9WO3ahNYiNubbm6gYKWoIwAjy17W3YO_-a7xEpyT9X78i6fAAIB2mkmGV6iENgtUGZ1lHuPs_U1eHACCjIDbRj0U5yqHN_fuRgw6vHZw-m1oR4gxpyQAswU2kEw87OubwdlEGW3b_0lmB3-kvyT_itJchlfA_5snzqHvejmNNH3AAYqJAbg8ego7MEKTJs3_nXCFnFj5u3uYXltX7jTCOl_QuVbI8XXv3FsSfcHk1eE8rsFdcTJbBUySQkRT9hxzEPNSJiiMNZlWFZE6WSXJUV2UnFEXX4yLYKmwG8_INbICA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=UQ_nzFiHHr9V2-r8i3IdEXPV7MIt_lpvMR5CPXgAm9WO3ahNYiNubbm6gYKWoIwAjy17W3YO_-a7xEpyT9X78i6fAAIB2mkmGV6iENgtUGZ1lHuPs_U1eHACCjIDbRj0U5yqHN_fuRgw6vHZw-m1oR4gxpyQAswU2kEw87OubwdlEGW3b_0lmB3-kvyT_itJchlfA_5snzqHvejmNNH3AAYqJAbg8ego7MEKTJs3_nXCFnFj5u3uYXltX7jTCOl_QuVbI8XXv3FsSfcHk1eE8rsFdcTJbBUySQkRT9hxzEPNSJiiMNZlWFZE6WSXJUV2UnFEXX4yLYKmwG8_INbICA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ هواپیمای «ایر فورس وان»را که از قطر به عنوان هدیه دریافت کرده بود معرفی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66536" target="_blank">📅 09:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66535">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a046173b76.mp4?token=FqCm7X4a1BhGKRc-hvfqTqRUiPscgjH7PofGSDyhDsxHI0ldpAC3ooB94BUkeUXKagAxPj7CBGfZAHn5HmzijJa0Pk1YFBcWs7iX_OQpUC3X-84bNOjFXk85esK-tEvN-Q1yM55LoveHgrbRZmKv4BcthF_0HBrV3mmFq38eD2vUUCyg7l29KoLSr2YMyVp-gWCjCRGkfelhnY2L1bV8maTst4Mi010JBBnXMe8yukR5zPPgHoMmAvoD5XBazMVXTnw82RCnOCoKkRMG9LjZVFUHoEtPrXH7lm9Uf3lKY20dsiRvK4RCVZIbNpiFBnxdSNoTU3RumCqjTkWRPRM2EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a046173b76.mp4?token=FqCm7X4a1BhGKRc-hvfqTqRUiPscgjH7PofGSDyhDsxHI0ldpAC3ooB94BUkeUXKagAxPj7CBGfZAHn5HmzijJa0Pk1YFBcWs7iX_OQpUC3X-84bNOjFXk85esK-tEvN-Q1yM55LoveHgrbRZmKv4BcthF_0HBrV3mmFq38eD2vUUCyg7l29KoLSr2YMyVp-gWCjCRGkfelhnY2L1bV8maTst4Mi010JBBnXMe8yukR5zPPgHoMmAvoD5XBazMVXTnw82RCnOCoKkRMG9LjZVFUHoEtPrXH7lm9Uf3lKY20dsiRvK4RCVZIbNpiFBnxdSNoTU3RumCqjTkWRPRM2EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف در حال اهدای تندیس حاج قاسم به نیکلاس مادورو (خرداد۱۴۰۴)
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66535" target="_blank">📅 09:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66534">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66534" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66533">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCq8b-PMk2FO3TZEh2ky8pZfKxTNxojGbswka66moM_sdvMv5ntzuwb65HYjNOumCSK8AgMvTXGPQdd-tzD-qyS7hOdy8Lj7DNxCt-MyeYynhqo1dJDLGhAkfsoLiJtnZ0qwJTpxeo4USbaR1zuKf2hHd1OFyaAgV3IjDlgABg2eOX6mV92i-EF35BNvYj7DikaTVEgKpw1uNdwMVVZC1n9RihoPpgT3hbujPbsfzWU6bfuBe0vmI52b-Kw-eJTn1y4RFvv8dnOEqdNxWWJN2LI6t-5HVmKjRN84kKGpZLh2hW2SVE3B8SfaqB7jLS159YXbeTVmDYygc-fabvRPBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66533" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66532">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=en_Fl5G9Hr6W4esF3sMZp86RxA53LN5BdBs1To9D4AUtdpY7GAGF2YPhLVy2zP_bkzWqyXSZMWBOGJ7lSJU_lFtPSLamjz5rYwKE27QYKGGbDMlMHO6W-_XI7uEoIaV5sQ6OqcZKIlJ_K4JJdTkz8OfQ5kecRmmnlwzhLt9M32gGz1XTjO7iJTSQxkKyfpYDF4hRnSv-WLz-ZBrAbgQFIdkrO1J-af7U8l-AMlHGP9EBQIAochXbK5vrgp7K1XynpthhJ3jHz3LC2XNvlDWBKI6fn6Qlm70f0QMLPqwLD_xnxOPGslADCOsVGNeyvkJmf6m-evpaqFNQiRHJZ7zNqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=en_Fl5G9Hr6W4esF3sMZp86RxA53LN5BdBs1To9D4AUtdpY7GAGF2YPhLVy2zP_bkzWqyXSZMWBOGJ7lSJU_lFtPSLamjz5rYwKE27QYKGGbDMlMHO6W-_XI7uEoIaV5sQ6OqcZKIlJ_K4JJdTkz8OfQ5kecRmmnlwzhLt9M32gGz1XTjO7iJTSQxkKyfpYDF4hRnSv-WLz-ZBrAbgQFIdkrO1J-af7U8l-AMlHGP9EBQIAochXbK5vrgp7K1XynpthhJ3jHz3LC2XNvlDWBKI6fn6Qlm70f0QMLPqwLD_xnxOPGslADCOsVGNeyvkJmf6m-evpaqFNQiRHJZ7zNqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم اکنون شیرینی آتش‌بس در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66532" target="_blank">📅 00:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66531">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=j0lMtOxwOkbi9VmR6tAu_9Q5YVsSXRGSDPamFycvrHBUNmzIVqOdty5jaBW7Mog-8OHE_GM_HFNDgG1Hefb0MA051B6VwdfwWqUSbSCPgVqv0EpjcXjvIrCUnYYreiav4MkHASx95krPeZ9pwEpU_kVQBcvgvxG9M8x_DRHEmVaQ5D5s77MGjn_a0v40_VD14ozJk-bTYR-OM-SeqC4XvxkCITM-1CZY8Xw-KxFRBAmGk6dKJ6Tyl-MJgwLBfYJSPmpINIJ6oOa4sJyWGR_eIB1BA2a6lNt_r0agiLn2MgHT4QIC0jUaD6dZgpg-jCIgIUg2h6hZ8PJDjTfOfajGUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=j0lMtOxwOkbi9VmR6tAu_9Q5YVsSXRGSDPamFycvrHBUNmzIVqOdty5jaBW7Mog-8OHE_GM_HFNDgG1Hefb0MA051B6VwdfwWqUSbSCPgVqv0EpjcXjvIrCUnYYreiav4MkHASx95krPeZ9pwEpU_kVQBcvgvxG9M8x_DRHEmVaQ5D5s77MGjn_a0v40_VD14ozJk-bTYR-OM-SeqC4XvxkCITM-1CZY8Xw-KxFRBAmGk6dKJ6Tyl-MJgwLBfYJSPmpINIJ6oOa4sJyWGR_eIB1BA2a6lNt_r0agiLn2MgHT4QIC0jUaD6dZgpg-jCIgIUg2h6hZ8PJDjTfOfajGUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت پزشکیان
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66531" target="_blank">📅 00:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66530">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=ZLoV0LZG64iVJdS7w4_CiEEfDNY96DE-TRPYG4vK2gMYBA3jsqsG7DYITFr4KJmOSP_wwd8cXapk2qm45STMfAdSh9dwGGut-T2Vqug5SknuerWye9YM1tk3ErfYG0z8dwbIjUB3LGvth2fRdH-M6SKjw6p0o0d2I8N5rgWoiFyQzFAGKOO5AJKVNsNJNDwP1UyCIdYa2vdeQbmnglQ2iY3aofuSKiCg1mWw6TBtwTUivT0HS0LgVZtAmsH_gS5ObHShrYxkXfB-d1h3dOfDc58xu7fVYSGUjctPn5xVa6dL5Nib80AibgbB-OU_5SzKuVN-c4orPPzZOsjLK4dINg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=ZLoV0LZG64iVJdS7w4_CiEEfDNY96DE-TRPYG4vK2gMYBA3jsqsG7DYITFr4KJmOSP_wwd8cXapk2qm45STMfAdSh9dwGGut-T2Vqug5SknuerWye9YM1tk3ErfYG0z8dwbIjUB3LGvth2fRdH-M6SKjw6p0o0d2I8N5rgWoiFyQzFAGKOO5AJKVNsNJNDwP1UyCIdYa2vdeQbmnglQ2iY3aofuSKiCg1mWw6TBtwTUivT0HS0LgVZtAmsH_gS5ObHShrYxkXfB-d1h3dOfDc58xu7fVYSGUjctPn5xVa6dL5Nib80AibgbB-OU_5SzKuVN-c4orPPzZOsjLK4dINg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد بایدن:
ما مردی داشتیم که نمی‌توانست از پله‌ها بالا برود، و من نمی‌خواهم در مورد این صحبت کنم چون اگر کمی زمین بخورم، می‌گویند: «اوه، این وحشتناک است.»
باشه، می‌تواند اتفاق بیفتد.
اما شما نمی‌توانید هر بار که روی صحنه می‌روید، زمین بخورید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66530" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66529">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=eyV78l-CEhlnGlOL7zccpUHxSZWKprlhFtPZ_DHEZPiJsgtC_-hord0gkScS0erTQEDfbdnCTvEM7q256YU8wFFWayEZ4-mDLfDIXvY2bJ6b8j42UhLUwDo2UtSwWVCL0E0Zouyba86Fw6fvppn5OgDrepvDKdGH6zSbH6dtN2oZ0QU8PLfE7m0zhqydNVn_qYQz0hWRkcrS_J-6xSrtddwn8WizLd4Ql2Oq928F1hiDCOhZiBJRhvD-JquZPtQ_lr4JIAmzsljO7PsEwk4UBjxp1Q_6cB4g8Wg7FEBQ0UdCGJlHcsQVclzM97HEzTBoaowKZrX_7EHdwr-7IXkQvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=eyV78l-CEhlnGlOL7zccpUHxSZWKprlhFtPZ_DHEZPiJsgtC_-hord0gkScS0erTQEDfbdnCTvEM7q256YU8wFFWayEZ4-mDLfDIXvY2bJ6b8j42UhLUwDo2UtSwWVCL0E0Zouyba86Fw6fvppn5OgDrepvDKdGH6zSbH6dtN2oZ0QU8PLfE7m0zhqydNVn_qYQz0hWRkcrS_J-6xSrtddwn8WizLd4Ql2Oq928F1hiDCOhZiBJRhvD-JquZPtQ_lr4JIAmzsljO7PsEwk4UBjxp1Q_6cB4g8Wg7FEBQ0UdCGJlHcsQVclzM97HEzTBoaowKZrX_7EHdwr-7IXkQvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ در مورد ایران:
من بزرگترین پل آنها را خراب کردم چون آنها دیر به جلسه آمدند. آنها گفتند که این خیلی خوب نیست.
آن پل، این پل جورج واشنگتن آنهاست. من آن را در سه دقیقه از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66529" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66528">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=tYWtaZR6UC7hmjZif6oCm66tUJeJHIj4WALw7go-Jt7ovdlHFF0V2q7bay0_sxRSGWrCU9ov2h-WyryM1jjSCVnuWqi45tiLpOKAaa1mdty7VTQMrP7DqyWB8uBlVvAgbyTd-D1OKcaWxl-qRz_4hXB14TVa1h_uSSyj6oXaFUtwXn9NuhOCOGvsfoiwuF1VEt4zsvkBONFv62L_6quxjkVFgl328SVUzRVY7xMZj2hrqaJRku3IA42iu9-L5aU4sMrDvztsfzbiCKlgemkhr8uWFU7bhISecNwSCzhRqylV07_uBknzUHE-QzvVcz90jKUqeVnUZtkNop7KA7kqDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=tYWtaZR6UC7hmjZif6oCm66tUJeJHIj4WALw7go-Jt7ovdlHFF0V2q7bay0_sxRSGWrCU9ov2h-WyryM1jjSCVnuWqi45tiLpOKAaa1mdty7VTQMrP7DqyWB8uBlVvAgbyTd-D1OKcaWxl-qRz_4hXB14TVa1h_uSSyj6oXaFUtwXn9NuhOCOGvsfoiwuF1VEt4zsvkBONFv62L_6quxjkVFgl328SVUzRVY7xMZj2hrqaJRku3IA42iu9-L5aU4sMrDvztsfzbiCKlgemkhr8uWFU7bhISecNwSCzhRqylV07_uBknzUHE-QzvVcz90jKUqeVnUZtkNop7KA7kqDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر همین حالا به آن‌ها حمله می‌کردم—در حالی که ما قرار نیست نیروی زمینی بفرستیم، و شما هم نیروی زمینی نمی‌خواهید، درست است؟
اگر نیروی زمینی نفرستیم، احتمالاً همان افراد به اعماق غارها می‌روند. به آن‌ها “غارهای گرانیتی” می‌گویند. آن‌ها بسیار مستحکم هستند.
آن‌ها خیلی عمیق می‌روند، و بعد وقتی ما متوقف شویم، بیرون می‌آیند و احتمالاً همان رهبران قبلی خواهند بود.
در حال حاضر تنگه هرمز کاملاً بسته شده بود.
پر از مین می‌شد و موشک‌ها از بالای کشتی‌های میلیارددلاری عبور می‌کردند. آن کشتی‌ها دیگر هرگز عبور نمی‌کردند.
ما برای ماه‌ها نفت نداشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66528" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66527">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7522060f48.mp4?token=S2v8eKzwCodXpKWJDkaCz6E1ed6gShHl9nsluUaUUa7XZgQEF80U2kt_sBHHauXiGic7wDX5_Aab5WVK4Ik99BtogTpGvrMYbu8iPzjKS59hXS36iSJ0reTN_bQR99tzUiQKY41wPkrPbz0Fh4kYDJCstaMvLZJMr4olfGtJYQQqK_Y_7jubIN6ocvH5wwpLQkgFhAcPex4Md-xrIKM9O1iMcfow4tvoiq0n5ZXNfEMXDitu7a5c6Z9a1QGG4RVcOVqGbpHltZLhiEpwHFL9DI3HB-DAR535pyfLLvqAEPKmM_Mjzbvx-UFfBggE2-oAYHrhs1wGVPrPbe3rPLMeqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7522060f48.mp4?token=S2v8eKzwCodXpKWJDkaCz6E1ed6gShHl9nsluUaUUa7XZgQEF80U2kt_sBHHauXiGic7wDX5_Aab5WVK4Ik99BtogTpGvrMYbu8iPzjKS59hXS36iSJ0reTN_bQR99tzUiQKY41wPkrPbz0Fh4kYDJCstaMvLZJMr4olfGtJYQQqK_Y_7jubIN6ocvH5wwpLQkgFhAcPex4Md-xrIKM9O1iMcfow4tvoiq0n5ZXNfEMXDitu7a5c6Z9a1QGG4RVcOVqGbpHltZLhiEpwHFL9DI3HB-DAR535pyfLLvqAEPKmM_Mjzbvx-UFfBggE2-oAYHrhs1wGVPrPbe3rPLMeqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آتش‌سوزی کلیسا در خیابان بوشویک در بروکلین
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66527" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66526">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=UXZY5AemRHnVJbyJvbgc5doboFntlFcnO3Ma6WraZbEkWAfg0BUTW95SsOxEqiT04nQUjKYCwApI44OpQU3OfN0UB88jfaRy7GPfdg1ZnlG0QTkVTH-eKkBXo_GhuXbgvScptWbmd22Gw4COqUApC59sjvYilaIOB-g4hLB2gFzj1Hga8jSVpYW6P1rU5lSljBkzKolF0wDxHbZBxMSVPW5DE21b4RnjAaBAI6Cj3cjbHf6EkoJemRiHAMPcIJ9B5W0PfAB73iHYH1JK0HEk26LGrER5l_NmykMB52V_-j0YnxVCMiDlfPdGgBZKDjNumEQ-WtDnjTIUY8pMIM1BXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=UXZY5AemRHnVJbyJvbgc5doboFntlFcnO3Ma6WraZbEkWAfg0BUTW95SsOxEqiT04nQUjKYCwApI44OpQU3OfN0UB88jfaRy7GPfdg1ZnlG0QTkVTH-eKkBXo_GhuXbgvScptWbmd22Gw4COqUApC59sjvYilaIOB-g4hLB2gFzj1Hga8jSVpYW6P1rU5lSljBkzKolF0wDxHbZBxMSVPW5DE21b4RnjAaBAI6Cj3cjbHf6EkoJemRiHAMPcIJ9B5W0PfAB73iHYH1JK0HEk26LGrER5l_NmykMB52V_-j0YnxVCMiDlfPdGgBZKDjNumEQ-WtDnjTIUY8pMIM1BXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارک کاپوتو از اکسیوس:
این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
پرزیدنت ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66526" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66525">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=UEmqiB7selplRN6oRl1bIVhbE6htc5577bXcmxDKGzV_oCo52lAIT1Mjv7pVKqEiWhEJY0ern0AoLzb7wbvJryxll-Of9OLLtUdlRGwEtpZxJKQMC5fi_Hl07_vM1DflhQd_UEaMNsZNKkWF1tXJocvXqCXo_BiJmO0aNdnu6EwFKGaOGFtjTYZt6bEAxAYW4igSBJBNH5KNSTtWBimImL-oAZreivABqIfUJJEaEW100Mob5NsvaERSllVVrJ5Q_Bx0tnTR9JOhzAWLuAXWmVC159soz0NNIG80SL7g5jRv3Y895LH50uopoUlt-t_qW-Pg9j2-NFZlTKpDhcRkfbDaC2btJ_mDugAsBsSR6g1GcHTxCSmYbfPQYsL56KB8QxoiTAOgjWY5SPrOKvn4XLUMSpzgiJY0V40tbr9GCjRRsq8l38H56cm-xbEjzSJ5lRud_OsS_E5RJpbSMj7gFJjlem61wLjsi119T0IGDzpn1xWue2ABWiAmcSJXwufqhycG4ESpAGDXbZAsAzL9pJr7Dx8mzb3MHQ4l3V7LkPygFLCj8f_m1sRankRUHPmThRRbOyQ3zOnh_bkb34Z1pcPY3wFUIid_0dDkqfrqQOQRsWzfmS8glghtGDrtbYTke_JDBZb3eEuEyDQkcHNZmctjbQM-yUZYtqL2TjXNEqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=UEmqiB7selplRN6oRl1bIVhbE6htc5577bXcmxDKGzV_oCo52lAIT1Mjv7pVKqEiWhEJY0ern0AoLzb7wbvJryxll-Of9OLLtUdlRGwEtpZxJKQMC5fi_Hl07_vM1DflhQd_UEaMNsZNKkWF1tXJocvXqCXo_BiJmO0aNdnu6EwFKGaOGFtjTYZt6bEAxAYW4igSBJBNH5KNSTtWBimImL-oAZreivABqIfUJJEaEW100Mob5NsvaERSllVVrJ5Q_Bx0tnTR9JOhzAWLuAXWmVC159soz0NNIG80SL7g5jRv3Y895LH50uopoUlt-t_qW-Pg9j2-NFZlTKpDhcRkfbDaC2btJ_mDugAsBsSR6g1GcHTxCSmYbfPQYsL56KB8QxoiTAOgjWY5SPrOKvn4XLUMSpzgiJY0V40tbr9GCjRRsq8l38H56cm-xbEjzSJ5lRud_OsS_E5RJpbSMj7gFJjlem61wLjsi119T0IGDzpn1xWue2ABWiAmcSJXwufqhycG4ESpAGDXbZAsAzL9pJr7Dx8mzb3MHQ4l3V7LkPygFLCj8f_m1sRankRUHPmThRRbOyQ3zOnh_bkb34Z1pcPY3wFUIid_0dDkqfrqQOQRsWzfmS8glghtGDrtbYTke_JDBZb3eEuEyDQkcHNZmctjbQM-yUZYtqL2TjXNEqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66525" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66524">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=UzoOT5bEf6e0APhJD0rb6rRtSpiEy-2EvN5vOvob34voIXZUIaObHQRGsrZvHqe5pmC1DLg0z8BkNScpw31ClNAUXQCDcbBOyWmPvAmCFqrrUjMPiwK7JBKS8Q76ofrsFcXF9SUOMN89vctV2gkq_FECvAaImoE-1UjqVpbp0VqjmkXMVc49qJhKmouf_PPbKbs1xHwPfLBKnR2VgVTQq6LWTrLZ4H_0pzy3hJ808_SBcA5x7j_kZT68p326Ja0zFAUYqpGtftNrO22zEg3b7jrGO0UMooWAKdjiAjr3iHI7bXVHd4OsVDwnRl-KvUVZw1y3xtZoKr8szuwQdqECWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=UzoOT5bEf6e0APhJD0rb6rRtSpiEy-2EvN5vOvob34voIXZUIaObHQRGsrZvHqe5pmC1DLg0z8BkNScpw31ClNAUXQCDcbBOyWmPvAmCFqrrUjMPiwK7JBKS8Q76ofrsFcXF9SUOMN89vctV2gkq_FECvAaImoE-1UjqVpbp0VqjmkXMVc49qJhKmouf_PPbKbs1xHwPfLBKnR2VgVTQq6LWTrLZ4H_0pzy3hJ808_SBcA5x7j_kZT68p326Ja0zFAUYqpGtftNrO22zEg3b7jrGO0UMooWAKdjiAjr3iHI7bXVHd4OsVDwnRl-KvUVZw1y3xtZoKr8szuwQdqECWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره ایران:
این ایده که اماراتی‌ها قرار است یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، اگر ایرانی‌ها رفتار خود را تغییر نداده باشند، پوچ است.
آنها این کار را نخواهند کرد. ما اجازه این کار را نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66524" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66523">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=NvwWJc8DHpMCbMIVdiKHYIY_wgdNXBndDlEkzTjh8MC9Tk02PbW-9GycQOnuWldOUQdAXd9ltH7t9DdczJtqbh-Oa26rmbT_HllwkiArTMqobfBYKaW8Q-XPaq44-kChgNVgLy8JGLexcf8dR_iNb6xWvHvS73nu339UlrYp8jz0JxWgh2_28JnVOHW9GH16NzVGIEjsiyaffr7yadRTVGsqPB6Ck5wBVaVlfa--rjOatSyl1Ii5bS23W3B_qtiO2FCxIjPAZ9DFUpWAuNhXzVIlohT8iRXiMDfjyHkSsYzt6hT7jAbomUO6xFKBbVUF11htMB_kSsXIuQhS7ai4Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=NvwWJc8DHpMCbMIVdiKHYIY_wgdNXBndDlEkzTjh8MC9Tk02PbW-9GycQOnuWldOUQdAXd9ltH7t9DdczJtqbh-Oa26rmbT_HllwkiArTMqobfBYKaW8Q-XPaq44-kChgNVgLy8JGLexcf8dR_iNb6xWvHvS73nu339UlrYp8jz0JxWgh2_28JnVOHW9GH16NzVGIEjsiyaffr7yadRTVGsqPB6Ck5wBVaVlfa--rjOatSyl1Ii5bS23W3B_qtiO2FCxIjPAZ9DFUpWAuNhXzVIlohT8iRXiMDfjyHkSsYzt6hT7jAbomUO6xFKBbVUF11htMB_kSsXIuQhS7ai4Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏پیشنهاد جی‌دی‌ونس به ایران:
گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، که در این صورت به معنای واقعی کلمه هیچ چیزی به دست نمی‌آورید.
گزینه ب این است که شما مانند یک رژیم عادی رفتار کنید، و ایالات متحده، به عنوان مثال، اگر قطری‌ها یا اماراتی‌ها می‌خواستند در کشور شما سرمایه‌گذاری کنند، در واقع به آنها اجازه می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66523" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66522">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f005383e.mp4?token=vxcvuKmrffAPrFAW-oEMR71IbDiHbNzBmXNhwx7Xq3zBRKzOhv9d-pwIH9hUcykaeIEn1BwOe8eIRn6CUYNu-Ps40hgq-1PySBAatLVVbO219n42K52ONaEArmrCDB7lY2cVExXaX6U8nMgBSwk5V7zSn8EHaTILvkCO41WxZz1aVwAVxC2MgmMPrkovM_4UpA6g2Xu-MUmXuepgNLLn2YNWH5-v7zMgo2OTdoBidlObRv9VFdElh_M6f5UUzXtFz_MSFl34cuj7kmJN8DcyPgQTH4A8y4i3X9EDfzG1oKmNoDBmc3ukIhbg-Xm7ajIPJEnitWQO3Egmw6Wc3ovylQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f005383e.mp4?token=vxcvuKmrffAPrFAW-oEMR71IbDiHbNzBmXNhwx7Xq3zBRKzOhv9d-pwIH9hUcykaeIEn1BwOe8eIRn6CUYNu-Ps40hgq-1PySBAatLVVbO219n42K52ONaEArmrCDB7lY2cVExXaX6U8nMgBSwk5V7zSn8EHaTILvkCO41WxZz1aVwAVxC2MgmMPrkovM_4UpA6g2Xu-MUmXuepgNLLn2YNWH5-v7zMgo2OTdoBidlObRv9VFdElh_M6f5UUzXtFz_MSFl34cuj7kmJN8DcyPgQTH4A8y4i3X9EDfzG1oKmNoDBmc3ukIhbg-Xm7ajIPJEnitWQO3Egmw6Wc3ovylQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره اسرائیل:
من از تصمیم ترامپ برای پایان دادن به توافق ایران دفاع کرده‌ام و اغلب متوجه شده‌ام که استدلال‌ها این است که «اسرائیل فکر نمی‌کند این خوب است، بنابراین بد است.»
واکنش من این است: نظرات اسرائیل مهم است، اما اساساً آنها از هم جدا هستند
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66522" target="_blank">📅 21:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66521">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=cSGAl-vjKabuOAyk_RVHSS6aESycim_ObZrZBDqKFuUNSXyH0FHw5xdLr6jWKeTjmA7nTNuW9dHsW8Tg3YpzZe68Ir7Rkt1omJOpXIDzz7ESYhx7tRGkLpIdnpdm_OswCDlXKOuYcI5ODBhVHzfOXXyxmV7SqFp-LolYVn35BzcJ1JZhmw92KgLyuTgCcG9-WdmGGxGcXZ5Yq4_rmbviEyODNlRDac0G35BU24advMOOfTJyrDvVigo9RSp_oXJ308aScVgfBOHvFNWk_wYPiVtpjl7azmIQ4l6162CYplrfwYyknhupLim_twnONOyzQ4RNaDK5ruJSZGG8jw5U0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=cSGAl-vjKabuOAyk_RVHSS6aESycim_ObZrZBDqKFuUNSXyH0FHw5xdLr6jWKeTjmA7nTNuW9dHsW8Tg3YpzZe68Ir7Rkt1omJOpXIDzz7ESYhx7tRGkLpIdnpdm_OswCDlXKOuYcI5ODBhVHzfOXXyxmV7SqFp-LolYVn35BzcJ1JZhmw92KgLyuTgCcG9-WdmGGxGcXZ5Yq4_rmbviEyODNlRDac0G35BU24advMOOfTJyrDvVigo9RSp_oXJ308aScVgfBOHvFNWk_wYPiVtpjl7azmIQ4l6162CYplrfwYyknhupLim_twnONOyzQ4RNaDK5ruJSZGG8jw5U0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره اسرائیل:
اسرائیل شریک خوبی است، همانطور که بریتانیا یا فرانسه شرکای خوبی هستند.
این بدان معنا نیست که ما همیشه منافع همسو خواهیم داشت
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66521" target="_blank">📅 21:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66520">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=s0i9IF85JFY4crZold-Tddx1uBb8ALmmB2R9FU94r_q6RBrU1SawPMPdXCXDvt25ZZ76haJbH8rS4wW7tlsuZQ3Et6Q1Ev39nRL8ryd_-2JksqGaZuGVdv7X-aIKRHmWJMQUvqyzGuPd1cI_UD8k5y95Ytt5hN5veTDgsatsCp4OdzY9Cj-nKbTY30AIwE_cEw9KgBAR7sxBUUiESp2K90a2hJk-oZgG8KmOa5NV9UdRrAAIrDqGJQO7PRzMPQLAPEnA82GJ0VAp_ixU6zayDtWrFeZeGKZW6-IHXY7wDCusWfM-GxOZ1oLAI1z3EFMv1CZ63JvqwqA7gByteVYQLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=s0i9IF85JFY4crZold-Tddx1uBb8ALmmB2R9FU94r_q6RBrU1SawPMPdXCXDvt25ZZ76haJbH8rS4wW7tlsuZQ3Et6Q1Ev39nRL8ryd_-2JksqGaZuGVdv7X-aIKRHmWJMQUvqyzGuPd1cI_UD8k5y95Ytt5hN5veTDgsatsCp4OdzY9Cj-nKbTY30AIwE_cEw9KgBAR7sxBUUiESp2K90a2hJk-oZgG8KmOa5NV9UdRrAAIrDqGJQO7PRzMPQLAPEnA82GJ0VAp_ixU6zayDtWrFeZeGKZW6-IHXY7wDCusWfM-GxOZ1oLAI1z3EFMv1CZ63JvqwqA7gByteVYQLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره ایران:
باز کردن تنگه هرمز دلیل کاهش قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار در امروز است.
و همچنین به همین دلیل است که قیمت بنزین، اکنون که ما صحبت می‌کنیم، برای اولین بار از ماه مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، به زیر ۴ دلار رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66520" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66519">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXB5RkykJhCpTaR4y-bik3jt_tYzj4NKXICxEVGVaDcmk9pH5RJbgOmrx1zS-65uwhM_q_ze9Xs4p7daGpEbl-lrMaDZ9mADNdP0JcMKvLVByZU_hes19Y_pX5C4uCdlFbN_ZsAQ5r3W-_alTjH6nuBeU_CQjxw_AG2SKHGExenA9bCEMpdJtBBrXvSkMWhE5d4OYbxMb54zUFPMbtzcZB7lt3LYh3sQoBSAHGD0h3JLkJKR_XXkHz-5e5-rOHY0U4jzi_Hb2UTnG7s2IwIoZyav3bDC18a6WAeHaufX35Uk-FOGcgkdO-A1rH2fHNNY0keRmaZzDy6xcJ_aqPEwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هیئت قطری رفته سوئیس ولی ایران و آمریکا نرفتن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66519" target="_blank">📅 21:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66518">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4Q4fLhZL7w0RrKisPU6CqgmdMMpAZKPhqjgaukyFQisS7Lxaxw-qWtazIaYWqrCD4MYsYbuyMk2shhP4z-3IgnvT8mqjpqNRNYDRWBrQtp2AKD5CfCURHfKj06rT1wTruel7brp0KyKvdfO4HuVEv18cUSPYAl8fN-MTpQkYFC4g_cxD9ttpzMq5Y954WIESgXBYns90pIUo3WDh9yr0XG-70P9QXPXz-dfH7umdVXCdUxLEd3bjhYlw5MhpRemvhK37fgUSEQGA-ahN9dI-PTYnvFynmYrWBTb6jerxeTj5EnXDpzgf9vinb1oFiklZjcMjjeVQ1e3AApAaLiE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌پست:
آمریکا ادعای «مزخرف» مبنی بر اینکه امارات متحده عربی - یا هر کشور دیگری - دارایی‌های مسدود شده ایران را آزاد کرده است، رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66518" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66517">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1UB0l_XqYTFQwnP3-MxIkQqg6QiBHAhBCmXFvzwrlju8HfawTce-nkZZLunkZedIrvQvb1-ab32-Zccit6kG1re0jFL8ueCUE1G0MPllojVPo1QeGBy7FMaOoGwFu2kKygpOXXMx1wlRZXeuQGq0UYr9w4QGP9cod208RhGnPa0HOYqvR3bM2aLXMx8wcXcXxsQxCNC4ZtRPxfp7xO6CaKuQdT1o5RQ35Q-KPXZQuK3R26aqm0GI6TrddBlwLDoACR6HalVSKF1VFF0kIb-6QVVWtcdDVeT5t7FF88bf7VezapqUtok30oq6nKSmriPRvyO8u5FSX9e-KW5lGgUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌های اطلاعاتی ایالات متحده به دولت ترامپ هشدار دادند که نتانیاهو احتمالاً اقداماتی انجام خواهد داد که می‌تواند توافق صلح جدید ایالات متحده و ایران را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66517" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66516">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=vPLfWy7PL_qXPL9FMq3QZ7TTNiP3L5kzm5QcKGWQVjamUGbLdVVroF-8qW7Q4Xs-9WSu5-jpQ-DHu-_G4ECdWh-JrH5efR6bxYNMBPfsWMH2UNy7zf92AVLXtQlUctyA4YiLUNgetiVCALSR7FDqIPYqmXPQGVf912kt7q2i8ZvhltNbPXgHD21ik5piWgWTHPzXTxcu4b0NfiTkvsBNHPF0cStC_ienDaKPIrYKo_sj4I7tH59nUyrEJBZbqueFRg4GrwNhmSYfaOt7d7K5KyyS5d2w82cnyDwoVmmweMuuAoGPXafgQy0erFFeSwE1LlQI3-9txwH5isBfcVnkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=vPLfWy7PL_qXPL9FMq3QZ7TTNiP3L5kzm5QcKGWQVjamUGbLdVVroF-8qW7Q4Xs-9WSu5-jpQ-DHu-_G4ECdWh-JrH5efR6bxYNMBPfsWMH2UNy7zf92AVLXtQlUctyA4YiLUNgetiVCALSR7FDqIPYqmXPQGVf912kt7q2i8ZvhltNbPXgHD21ik5piWgWTHPzXTxcu4b0NfiTkvsBNHPF0cStC_ienDaKPIrYKo_sj4I7tH59nUyrEJBZbqueFRg4GrwNhmSYfaOt7d7K5KyyS5d2w82cnyDwoVmmweMuuAoGPXafgQy0erFFeSwE1LlQI3-9txwH5isBfcVnkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم، دبیر کل حزب‌الله:
امروز در لبنان، ما با خطرناک‌ترین مرحله تاریخ خود و بزرگترین توطئه مشترک آمریکایی، اسرائیلی و بین‌المللی روبرو هستیم که آینده کشور و فرزندانمان را تهدید می‌کند.
هدف اصلی این طرح، ریشه‌کن کردن و حذف کامل مقاومت و پایگاه مردمی آن در لبنان است.
دشمنان برای دستیابی به این هدف، ابتدا جنگی جنایتکارانه و بی‌حد و حصر را آغاز کردند و با کشتار غیرنظامیان و تخریب گسترده، مقاومت را به زانو درآوردند.
در گام بعدی، ایالات متحده و رژیم صهیونیستی پس از مشاهده تغییرات در معادلات منطقه‌ای پس از تحولات سوریه، توافقات قبلی را نقض کردند تا موازنه قدرت را به نفع خود تغییر دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66516" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66515">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=MVBgmWhYBt1l3_DoVCEQvVDprnXBSFO-aG9Qs_6pz2w7h2qoMcExnKyqvVQlxT75HhytgBVYxPSv_U-BkQDwq1QD2Q7NGr7im7uhWs4Bs7ihQ1oWgYaVD2-KgIHcZQCpRpOQ64SHFSKX4jxM5o30d0w_Jyaw8VSNBUhBvu77jXENhqtFIU4xJ-WXRsi94gERe17n1JtRgijYFm1BFHY030ogEFY-V9FTnaLWt56Af7SC5r6GLXnsa50ydEYZ18NpeM8Sg8e5u-ai7y2YnRI8U-oRnXIU4GBUAwBYq2a6gYVlC4x10ZJi9SYExAC7DD2JyjGsVCWkrFYPIRftAK8sww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=MVBgmWhYBt1l3_DoVCEQvVDprnXBSFO-aG9Qs_6pz2w7h2qoMcExnKyqvVQlxT75HhytgBVYxPSv_U-BkQDwq1QD2Q7NGr7im7uhWs4Bs7ihQ1oWgYaVD2-KgIHcZQCpRpOQ64SHFSKX4jxM5o30d0w_Jyaw8VSNBUhBvu77jXENhqtFIU4xJ-WXRsi94gERe17n1JtRgijYFm1BFHY030ogEFY-V9FTnaLWt56Af7SC5r6GLXnsa50ydEYZ18NpeM8Sg8e5u-ai7y2YnRI8U-oRnXIU4GBUAwBYq2a6gYVlC4x10ZJi9SYExAC7DD2JyjGsVCWkrFYPIRftAK8sww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
پروژه نابودی حزب‌الله شکست خورده است، نقشه‌های اسرائیل به بن‌بست رسیده است و پیروزی نهایی، یعنی اخراج کامل و قطعی اشغالگران از هر وجب از خاک لبنان اجتناب‌ناپذیر است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66515" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66514">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66514" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66514" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66513">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66513" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66512">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
نعیم قاسم، دبیرکل حزب‌الله لبنان:«تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
حزب‌الله خلع سلاح نخواهد شد. این سلاح‌ها برای مقابله با اسرائیل هستند.ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
«ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66512" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66511">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6jXccSYGT3kXSR4Or6wbqXgtYsrdp4wejteuYolYKUmTqynR27KW_5dnQoTEae1sJeX0A-9TFbQXxPHVHbLe_SxCCfCjxgmw073d1Dn1pbmPKpkqw1DlhhqQ_W8b5fBD-LRQKKpGxUGf71V72l5GW6FQsW_mBy3_XbTYTFmpdvFvbwFoPiPkzp5lepvxbJNVmB3io_LNo9KFZH9J-MnUJpf5x6rxa-RJq_o75fGg7AyvZXtIxPkoT-PfGbpLwEq7LBFb4cSIObfkR8PVFz_Eed1mS-P5kz1bth1vVikM6_BAKleRUIC8IFkWb7f8C6uZFDOunm28UKeWir3WhwGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اتاق جنگ اسرائیل:
رژیم تروریستی ایران از نیروی نیابتی خود، حزب‌الله، برای حمله به اسرائیل استفاده می‌کند، به این امید که بتواند وقتی اسرائیل پاسخ می‌دهد، اسرائیل را به خاطر از مسیر خارج کردن مذاکرات سرزنش کند.
ایالات متحده باید به حمایت از حق اسرائیل برای دفاع از خود در برابر رژیم نسل‌کش ایران و نیروهای نیابتی آن ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66511" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66510">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=EYrsMFKFQgeWDkWkRvxbe8I5CiJzrQkIx_S1xw_s2VQtZZXugSGsIOlRmzMEGKIgX3BnXtgkwLt5M-wPFvsrKIY_M4w99xPTZ9moOb233f84x9ZpbKd7_RT9VJWkcxncWt79h-FKNqyBQIZdgIhyDOK13p2TI21k7CX8EDvHiiaF3d3DMwHzovB2RxNCcsPVFrCsErIXKSs9mO-BHt5hf87z0N837KFELt9BLHBGNYMjpilh5UT4by3oVLwNfsS_pSXIUVid6V6Pc1g0TtzgZq6ijQnzXVQlYDKLIuDwtig9164X8A_gJic0o-y-7KhUZPVBJAArWikdt5k0NhyTpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=EYrsMFKFQgeWDkWkRvxbe8I5CiJzrQkIx_S1xw_s2VQtZZXugSGsIOlRmzMEGKIgX3BnXtgkwLt5M-wPFvsrKIY_M4w99xPTZ9moOb233f84x9ZpbKd7_RT9VJWkcxncWt79h-FKNqyBQIZdgIhyDOK13p2TI21k7CX8EDvHiiaF3d3DMwHzovB2RxNCcsPVFrCsErIXKSs9mO-BHt5hf87z0N837KFELt9BLHBGNYMjpilh5UT4by3oVLwNfsS_pSXIUVid6V6Pc1g0TtzgZq6ijQnzXVQlYDKLIuDwtig9164X8A_gJic0o-y-7KhUZPVBJAArWikdt5k0NhyTpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
«هر مشکلی در خاورمیانه مستقیماً به ایران برمی‌گردد. حزب‌الله؟ ایران. شبه‌نظامیان شیعه که عراق را نابود و تهدید می‌کنند؟ ایران. حماس؟ ایران. حوثی‌ها؟ ایران. اسد که در سوریه مردم را قتل عام می‌کند؟ ایران. این رژیم هزاران هزار نفر را کشته است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66510" target="_blank">📅 19:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66509">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJvRHhRySyi9pVRu75kzl7p2cbzkHy6XpnuWEpzcb5clByODjmWJDEVi_Aolo18og3w4V-3ppMnWKJd9BoEAEszM7bFjKwGflrE_hZPt3vTeWgT_TWNQ3HQALn18rGNUXxb-A0aY028XZGmo7Fy4roIt7FC2pVvPjbuUySz7Ek3yhcUZ35issAicLTIMRokl8HqvJKWTp1QHt6ehDaI7Xk2BiaepLcmAL5tifmqBtC5XGaY3RdiqKh7ShEuM-hDWuv8nWV4hPRm9VA6opww79utCY4gckmOqNkiZW5LmQq96mSmn9dBXuRSWqIhARZba3VO3cXvFEED5ymwFdV24Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل هیوم به ترامپ:
می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی
شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66509" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66508">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ:
ما از روی استیصال پای میز مذاکره نرفته ایم.این ایران بود که از سر استیصال آمد. کارشان تمام شده است!
ما این دوره ۶۰ روزه را تا آخر پیش می‌بریم. آن‌ها هیچ پولی دریافت نخواهند کرد؛ حتی یک سنت هم نه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66508" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66507">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=aJJGhpv-ZCLhAXfwJiy6hhtL3_U0bHRavuFh72xCvSfqIlC73PpF3a1qA-DtVHmDEKYkJZmEK3dwTmSjyYy8K6BtYYuy7CsaUdEV3Gi0nyoMGVO__CcJZm8a1_nmY-f72EOcAFK6g_osXFg31k6x_iL99zFO-IwRgttTOY4XZoj9syqIrtXLy1YuMvaARGAC7A4KWRh8xt3jyRQGLIACpxrf1LXzzQwHZslikurtnwFQz8f9zuY9xkhGb2YJy_OTy33Cjrzj0GSjghA_5n-RacAVLu8lOWShYwnx6AZHWUJpfKcqhIu2w3B31NZGcjEna683-Ohs_U46VOCcCO6GbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=aJJGhpv-ZCLhAXfwJiy6hhtL3_U0bHRavuFh72xCvSfqIlC73PpF3a1qA-DtVHmDEKYkJZmEK3dwTmSjyYy8K6BtYYuy7CsaUdEV3Gi0nyoMGVO__CcJZm8a1_nmY-f72EOcAFK6g_osXFg31k6x_iL99zFO-IwRgttTOY4XZoj9syqIrtXLy1YuMvaARGAC7A4KWRh8xt3jyRQGLIACpxrf1LXzzQwHZslikurtnwFQz8f9zuY9xkhGb2YJy_OTy33Cjrzj0GSjghA_5n-RacAVLu8lOWShYwnx6AZHWUJpfKcqhIu2w3B31NZGcjEna683-Ohs_U46VOCcCO6GbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
همانطور که دستور دادم، ارتش اسرائیل با قدرت به ۱۵۰ هدف حزب‌الله در لبنان حمله کرد و ده‌ها تروریست را از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66507" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66506">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66506" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66505">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=F7OKNvjqm7tVeoo7UaXjl0DTwL0o06LSWH6vETmroIkLUSbyZe4F0MxDmh-p5VzFcwubgWViME-YaCR3qCZaLS_1WfklrbJZ2HDNQvmTsXDjxTRkQSfe1D_qx-6sHfiiWRmuKUSmMM9C9Cr62YF0VdZUroX997GrsEKmE82yEPjZ2rpGtgw5D0Oz698YH8eofM2hX6en1c3_jvDt9RlFVKtRlGK88nvVku-KvkFeiYpg62W79TphWsw8ap7U-ZZH0DlUDdxAmfaTdpCu35COuifwXc_oIKMOWlfRhqnlk2ZFQPEcVbIt5jKDnc-u1RLxnIhEcUzv2avZ-BZ7MRUbtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=F7OKNvjqm7tVeoo7UaXjl0DTwL0o06LSWH6vETmroIkLUSbyZe4F0MxDmh-p5VzFcwubgWViME-YaCR3qCZaLS_1WfklrbJZ2HDNQvmTsXDjxTRkQSfe1D_qx-6sHfiiWRmuKUSmMM9C9Cr62YF0VdZUroX997GrsEKmE82yEPjZ2rpGtgw5D0Oz698YH8eofM2hX6en1c3_jvDt9RlFVKtRlGK88nvVku-KvkFeiYpg62W79TphWsw8ap7U-ZZH0DlUDdxAmfaTdpCu35COuifwXc_oIKMOWlfRhqnlk2ZFQPEcVbIt5jKDnc-u1RLxnIhEcUzv2avZ-BZ7MRUbtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محکم تر بززززن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66505" target="_blank">📅 18:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66504">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=WRcxoD-6XHV35ydbt5P5rmFrWgeRp7mmQBrRs6Ro8WmP2TlGcK0CgN7ULUilO4K1Jn1Oy3f2rmkxblqwy6Z8H7Cg_VdLw1vVd94NYBBk_o1Bc5MwdkbT6P80xjjcUyKLLGWvsclJejBDUDDL_4ZPRe_Kuck5rIsiU6G-6OOcYgbGMSl1-uLZvV7_YL3xc54VCDNioTLlc17LI988Kw5BgO7mfpFN2puqUjtFCz9gu_qA4r-59RXIEeArUxp0uYqXltY-BrJ8HHtb7o9Nm4L4odD2gKYewwwYugU5K6xNEcIIbvTlmaZ9nzFwuvIl1SJ66LIIH7v5oYxmP-QrGTY5Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=WRcxoD-6XHV35ydbt5P5rmFrWgeRp7mmQBrRs6Ro8WmP2TlGcK0CgN7ULUilO4K1Jn1Oy3f2rmkxblqwy6Z8H7Cg_VdLw1vVd94NYBBk_o1Bc5MwdkbT6P80xjjcUyKLLGWvsclJejBDUDDL_4ZPRe_Kuck5rIsiU6G-6OOcYgbGMSl1-uLZvV7_YL3xc54VCDNioTLlc17LI988Kw5BgO7mfpFN2puqUjtFCz9gu_qA4r-59RXIEeArUxp0uYqXltY-BrJ8HHtb7o9Nm4L4odD2gKYewwwYugU5K6xNEcIIbvTlmaZ9nzFwuvIl1SJ66LIIH7v5oYxmP-QrGTY5Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از لحظه سوخت‌گیری جت های جنگنده F16در حین انجام عملیات گشت زنی بر فراز خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66504" target="_blank">📅 17:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66503">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=aqxyOCl5cyUN9-QZ3-Y1jpU1zoSOAeDSpUKlo3ZEkSlrGSOgbHiOIqETvsyRZHpmmoQq5VRC1Ce2UkT8aiP3UcjqaMQ0sLQeSrYU462lGqrfHpdpraAB8y0qtDRCL52Y0a03FeLw-PupnOIJCZBSF3kg4g2GcG6Wyhe89hNbcMNZbVVmyQLxHLUcaWZ-5cf5f5nzlD_9IykRBbSJhtt0IFyDyd0Qmc0YkXzXd_-EtWne0VMjqIvArLJE_2NQUF5EO-_ql-dI-7ue6WtCFvftcMlY2d1jC8y5ySQmtayGFxQTEZlv01HE-E9ailxRGhiKZ7DJmzuVGc673aJdrgb0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=aqxyOCl5cyUN9-QZ3-Y1jpU1zoSOAeDSpUKlo3ZEkSlrGSOgbHiOIqETvsyRZHpmmoQq5VRC1Ce2UkT8aiP3UcjqaMQ0sLQeSrYU462lGqrfHpdpraAB8y0qtDRCL52Y0a03FeLw-PupnOIJCZBSF3kg4g2GcG6Wyhe89hNbcMNZbVVmyQLxHLUcaWZ-5cf5f5nzlD_9IykRBbSJhtt0IFyDyd0Qmc0YkXzXd_-EtWne0VMjqIvArLJE_2NQUF5EO-_ql-dI-7ue6WtCFvftcMlY2d1jC8y5ySQmtayGFxQTEZlv01HE-E9ailxRGhiKZ7DJmzuVGc673aJdrgb0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد از نشست G7 پشت سر جرجیا ملونی نخست وزیر ایتالیا گفته:
این زن همش التماس میکرد باهاش عکس بگیرم. حالا جرجیا در جوابش گفته:دروغه، شوکه شده‌‌م. نمی‌دونم چرا ترامپ با متحدانش این‌طور رفتار می‌کنه؟
ولی یک چیز رو به خاطر داشته باش: من و ایتالیا هرگز التماس نمی‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66503" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66502">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
منطقه امنیتی در جنوب لبنان ۱۰ کیلومتر امتداد دارد و ما به تقویت نیروهای خود در آنجا ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66501">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWQsop8T3dA6xJCrf0LyBUplWCeNIrJ1g5orHseGFVZ0e9d4CHFAfEijS-XOrqAyj7-cgkZibLSTu8dIDyll8BwgCY7mabN0BBkDQMhwl8kOecES8i_mlJnHzKbV7hyCAT5Rd1ptsS0x8Y0tMlGXqbInENYtZAXLkYBGDPVTIbpdPEJLoYhWK2amvAuxsJtY7_kjaJ8tSudEwK_3fB_KVIAmKTwmRA6Wlnh0rNVEa66hfnC62oXrdzal-e2St5tyhMgr9zz2PpdvXnbs1eab1SllopO64A4TzoLTyX2oC9XppX3lRMikL1pEdcD-7UnoQUPVL-xCwgmQNaYX4FugCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و حزب‌الله به توافق آتش‌بس جدیدی دست یافته‌اند. حزب‌الله از توقف بمباران اسرائیل و پایبندی به توافق‌های آتش‌بس قبلی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66501" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66500">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgrevXYiXVia1pelV_6t0J8ons9IkSPCk8819tzhFrBIrFtmkesD5f7BER95UCCZDNgPUdZ_fqZV3lqsI7cTEWf1zPkeNSGffci0XxNBA_1sPfSwgb5J7YxdUsL0quoWx6k4TRhUXMIbemVk1ZmS7bGm1MO9aj0tPy5W1Mt4QpwTfHzRdMS8D3-RXuJiGKKukHA2CJJoYE__hOVHNpcpaP1rkEFThfxkHCOiu7DucB87sH9WgdrKE98yl_JRTu5ltUwEssosWX8YPEh_pleTJX4ARGTAPNUfmqPMk5hYIQxIiBElbi8tpqcLxKjKRWQ01EYX6r5Jn77qFpor9b3IFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک مقام ارشد آمریکایی به من گفت: اسرائیل و حزب‌الله بر سر آتش‌بس مجدد از ساعت ۴ بعد از ظهر به وقت اسرائیل توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66500" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66499">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNviqT_GggCR_TlXR45AbWW43b_8wKVRjIxRtbAE1dEawe3SVyJhK1QDiJt5IEc6Fd_GQH-EbZT2qG9breJ-RQX9q3a1uAUz8iT1xUvthB-USvBR966uUH25UcIA7HxKfscvIEzD9RyUeCI9LKLmdhwxdl07VYTbCXRo9xaOaQBvHyAAI9ibM6gHo0zN83t8ke-372FVuaw6ljSY7U9Ll6yF6QGZusF_lVHjl4fPUzyMmPpE6EICyv0hnytOT6FhchVCFQJW4hWJdMZXJ7xkXUX9oj0gT_6DRR9PiX6nMplqD_JXx8pxITiuxeWog1_DFhSaUTmGY4vFiINPzmKvOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما از روی ناچاری ملاقات نکردیم، ایران این کار را کرد. آنها کارشان تمام است! ما 60 روز را بازی خواهیم کرد. آنها نه پولی می‌گیرند، نه ده سنت!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66499" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66498">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWOtXgUJoyPH5Dct5VMFQ3qvuwNC3FGx8025lKNS0i8DKEt6HNiTYDZNsxfVqEKhDwAIms4-bX_I60V6IqfKrQrnqRSyHL0v_esYKaYe-FKsSwU78beZh61JRu96tdrVIxipHkkvLDCxnlQPNe6kWtzg7Zos1iB6f0NeKhFD2WnBTSCZs02jXlV2QmwKJnuSFypO3XAah-DaUMzMdIjlbhXkqJuCjwDD9ipgzquZRsGUTK7LWVQv5PG3wlnHsf9_8Wr6NG6ssny8eXKPy99-w06qc9YfoMgJSbiT6I2RYC_DpZOkSxh_nfjc59DoFG9EwuWWARrvYyiVE5byJwWIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
این جنگ ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات پدافند هوایی، نه رادار، و تقریباً هیچ چیز دیگری. با این حال، دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش وضعیت بهتری دارد.
می‌توانید تصور کنید که کسی چنین حرفی بزند و از آن جان سالم به در ببرد؟ بعضی‌ها واقعاً تا چه حد می‌توانند احمق باشند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66498" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66497">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
‏اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا مسئول حملات اسرائیل به لبنان است. جمهوری اسلامی همه تدابیر لازم را برای صیانت از منافع، امنیت و حقوق خود و متحدانش اتخاذ می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66497" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66496">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERQT2WnMIbS1FxQ-5M6sef_6MyZD1nmhzJpduOqQUDlygI2nClOH2Svxi-pCJm3vizhJXJKvKHjPzwMA69iVBo2jbF_rXE4szcQtNmcbCX2pWBQq160wuBl2X8gxAm71UnfttIFb3tB1w59wBKgDfw0RbRyYmyfmMRLPgLCNHG18GYThi2RkLolgymSHrZVl49Q0fXlboi8xPyxLhrKG25H7awsLBmJStFk9lIdVsDDVxaqLuqlhQZJYQpRWDg8bHvduFXNaAhqBWY9y9miu6SyfFGwcZ6Qmny9FGixR1wXZGXaJVMrylM_Pse6ipEytx__RcVbGGbpqG8KwfGdCag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66496" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66495">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=Xi6vIUza26AlQeyGU-F3Pyjjs7Rw-LToxCqxyUGPHeWSiY__YQtKCqHa5RkprSzHC1pIzJ2F4xt5nG_xHMH-bYtOVsJ95guoxR2iONx-87gSXiYG46kt-8ea_XbC3-Y4Pr3Lx4otLAhIQV6DVicaEI4XJlXK1Coeti8Vdei0NiJARZ0ySescOKt9STy3PFoji7Ur9LhvUT9cA_0KDK9MSxBqbvqiWwZoSLl89c8n4wF_4aKI_EeylOFBfbdsYUdU2_CuMee6kGe3mWCmNXhsiwaQomu6wkRI4u2fmyjUqtJFJMoRwCLfHhmEKIRWsl2sPS1re5iG8yZ0_T0qcsif9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=Xi6vIUza26AlQeyGU-F3Pyjjs7Rw-LToxCqxyUGPHeWSiY__YQtKCqHa5RkprSzHC1pIzJ2F4xt5nG_xHMH-bYtOVsJ95guoxR2iONx-87gSXiYG46kt-8ea_XbC3-Y4Pr3Lx4otLAhIQV6DVicaEI4XJlXK1Coeti8Vdei0NiJARZ0ySescOKt9STy3PFoji7Ur9LhvUT9cA_0KDK9MSxBqbvqiWwZoSLl89c8n4wF_4aKI_EeylOFBfbdsYUdU2_CuMee6kGe3mWCmNXhsiwaQomu6wkRI4u2fmyjUqtJFJMoRwCLfHhmEKIRWsl2sPS1re5iG8yZ0_T0qcsif9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66495" target="_blank">📅 15:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66494">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=RdRBPGYan30_ejBA2tN0irz7Z8jsmNdtU8LDgk-zKRf8o6UMPFwgI9Wl-S6xCzeyGDyLxNwDy8X-LR3lP9cReta73LEhlcOoxYGwikedrxRgJ7RKIkTUnfU3iQpLUJSK8E2P3CzB9q2VmTxHpuEqxXwPxjb7lG4DH6jNgLQ8lQd2-yEMyZtKVED4NKaO6RSf1LCkMFP0-FHDxmcq0G_JRVL1bYzXwiADxOf06zfsRGOh9Atw7NZVc4RY46tocdH2goVAl3fd6QXl8EBlaiSUQcCMaEOrNTV7m5nVjrYpAB0-i455NUHhZYDhRoMO64uOhpDdJLjQTTXPoS34U52bkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=RdRBPGYan30_ejBA2tN0irz7Z8jsmNdtU8LDgk-zKRf8o6UMPFwgI9Wl-S6xCzeyGDyLxNwDy8X-LR3lP9cReta73LEhlcOoxYGwikedrxRgJ7RKIkTUnfU3iQpLUJSK8E2P3CzB9q2VmTxHpuEqxXwPxjb7lG4DH6jNgLQ8lQd2-yEMyZtKVED4NKaO6RSf1LCkMFP0-FHDxmcq0G_JRVL1bYzXwiADxOf06zfsRGOh9Atw7NZVc4RY46tocdH2goVAl3fd6QXl8EBlaiSUQcCMaEOrNTV7m5nVjrYpAB0-i455NUHhZYDhRoMO64uOhpDdJLjQTTXPoS34U52bkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیا می‌توانید جلوی حملهٔ اسرائیل به لبنان را بگیرید؟
ترامپ: «بله. آن‌ها احترام زیادی برای من قائل هستند و هر چه بگویم انجام می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66494" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66493">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66493" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66492">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEaVKFma4d-0DTbzWguEFHZIWMfLp8Hj7GEcrgtDE27zLl5P5jNN-jVlDSOH8U0LAuso5amK0qlxXHfSzv3q3jkkdUTCMvchALibnUD6MuA31oI-NbP--T2qcb2YpgsGjuepfco1kmVPdS5dhd1X-Za_sum2QSm5RanvyyCXRgTGS95pzaB5ZrWAbW0ItfwZxmVDw3_Wlnd8mk7LmWCnJB7ZzGf65_gAv-EPToVu3Ux8vR08BSiGZ6VBDZVZ_SOrB9LUK3SzCfOpW1X8eosgpn2iJ44TKoQfFJrJrv3lptDw0wQhUBo7heuEyxMoDZoKsnY7U7tK8geiSBkQFnsK1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66492" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66491">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jri00LqZARrzJ5z21o-AgxBTNmLtNYJX7ZNv8PD8ZEgjIFoJxfLrrHO_iz3Db-_YZKbRN4mIsbKdA1E4BrlNgUq9kSxdxpMMtwMmpGulNunWsOTHTs09ympNCbbryeN0KgRQ9GHsBAzFaoQxxbnCMayiR-AbTDdzqAuO94AivdW2S_HBXVqFtQYlnpva7z_NVtAT0tuMxlCvNHnMtwonm02uVZ17juJ3iDMrp7dv71aj1hchZcikWA-wPcnwZfOJ9yrct1fPPzz9C6Vn7-M_bW6XF3XTtxazHhXRR_zJhcO4nC-fhpI9oFFMR7JBhUX4LXkCyIBB-HlAk2_qjRVaJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به فارسی؛نخست وزیر نتانیاهو:
پس از حمله جنایتکارانه حزب‌الله که نقض آشکار آتش‌بس است، دیشب به ارتش اسرائیل دستور دادم که با قدرت به حزب‌الله حمله کند.
ارتش اسرائیل به بیش از ۸۰ هدف تروریستی حمله کرد و ده‌ها تروریست را از بین برد. متعاقباً، ارتش اسرائیل امروز صبح به مقر حزب‌الله در بقاع حمله کرد.
امروز صبح با وزیر دفاع و رئیس ستاد کل، ارزیابی وضعیت را انجام دادم.
دستور من واضح است: اسرائیل حمله به سربازان یا خاک ما را تحمل نخواهد کرد و بهای بسیار سنگینی را برای این حملات از حزب‌الله خواهد گرفت.
ارتش اسرائیل برای خنثی کردن هرگونه تهدیدی علیه نیروها و خاک ما اقدام خواهد کرد.
همانطور که به صراحت تاکید کردم: اسرائیل تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهد ماند تا از شهرهای شمالی محافظت کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66491" target="_blank">📅 15:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66490">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=XC00-xAHOtmWxTLp2gD3iHq165XUM-b6jcanw1iJPIUmnn20-8mnlUnitz5Redx0_-QS6OsKpuqCJPakocD-L9t1MOHW-upSCLlSUyJX49mqfd_bzGFsuUaTxi3qV1Yc3dOaVjRg217quY9xXTsqKb6nyUCAFu8Euy2UVYpG8bCYhE0pxld8yUJ3-9DLZte80v6ZAnkIazaRkUTL9mHjDPHrchH7edxhZpu3nKevZo-5djWxhIOgc8Xd-7JAQRcvSVtzS6dWWFHuXbQpE1LTILbY7FDmuIjdHJdJIG9c23KCM6hC7YIURfe1GkHCHqw4Q2TkJQoSorTtdIc4kj4ntQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=XC00-xAHOtmWxTLp2gD3iHq165XUM-b6jcanw1iJPIUmnn20-8mnlUnitz5Redx0_-QS6OsKpuqCJPakocD-L9t1MOHW-upSCLlSUyJX49mqfd_bzGFsuUaTxi3qV1Yc3dOaVjRg217quY9xXTsqKb6nyUCAFu8Euy2UVYpG8bCYhE0pxld8yUJ3-9DLZte80v6ZAnkIazaRkUTL9mHjDPHrchH7edxhZpu3nKevZo-5djWxhIOgc8Xd-7JAQRcvSVtzS6dWWFHuXbQpE1LTILbY7FDmuIjdHJdJIG9c23KCM6hC7YIURfe1GkHCHqw4Q2TkJQoSorTtdIc4kj4ntQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.  @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66490" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66489">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=u7T957BX_7jmPPSvPzzVbUnR5oKexsgK-Ia_tcejk-ulYTWeWgPJAdnakwZCwRsykkBTw7BI1pX7lDzJiBaPbxd-Ae9qF6OmM3nXb68DKG8v8jepu37aGUnUYA1cTdxTPZaxt0E2p4DwUfZpDdTgkBXQqs4kBmeOLEU4FM_g9lx0SEsxaTjVJy_NB59m95pSofQGOvxxlsWwQyOcYTF7ZjlDMd47bIsMxHx4xD4fr6NrAG260hrMa9kgnssMkEuK_1Itlg09Sx7tYI13D_1VDzAHMh71TdvtFkbDuOT4z50Dv64erGrBdj9MheTWjxBY2t6rSfu0WhZpJVzmeS0lFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=u7T957BX_7jmPPSvPzzVbUnR5oKexsgK-Ia_tcejk-ulYTWeWgPJAdnakwZCwRsykkBTw7BI1pX7lDzJiBaPbxd-Ae9qF6OmM3nXb68DKG8v8jepu37aGUnUYA1cTdxTPZaxt0E2p4DwUfZpDdTgkBXQqs4kBmeOLEU4FM_g9lx0SEsxaTjVJy_NB59m95pSofQGOvxxlsWwQyOcYTF7ZjlDMd47bIsMxHx4xD4fr6NrAG260hrMa9kgnssMkEuK_1Itlg09Sx7tYI13D_1VDzAHMh71TdvtFkbDuOT4z50Dv64erGrBdj9MheTWjxBY2t6rSfu0WhZpJVzmeS0lFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66489" target="_blank">📅 15:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66488">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=kzb2AqR-t0uEgTegBu4w_QVsEknD4QWVE-Xq3XqdCPg-kar0k9ndv_Hy5dcaFW7LVgFCSj3LKbkYA5e4fVt7OIHbfs-Jf-ZnfvqJzsvytgqwWQSes1NEjaKemFzZod3Z6JlCh1Ndd-FMf1s3esmPQJslwg-C__ho29DiCZ69k8o1iOVUDqR9rFPYnCUQrITsqa6deS45O12PKrWj8-YaO5NyNSEZ7jQKsePyJyIzKLtb_MPqkSdU040wd0ZQgpRql0jUb7RLMh1E5CfsII7UjQ4Bk7uWDPMd-Wo1F5KCUhIAuttrM0UQW7wXRe1h7XZpAc2y9RIyZVxW3zie0oCq3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=kzb2AqR-t0uEgTegBu4w_QVsEknD4QWVE-Xq3XqdCPg-kar0k9ndv_Hy5dcaFW7LVgFCSj3LKbkYA5e4fVt7OIHbfs-Jf-ZnfvqJzsvytgqwWQSes1NEjaKemFzZod3Z6JlCh1Ndd-FMf1s3esmPQJslwg-C__ho29DiCZ69k8o1iOVUDqR9rFPYnCUQrITsqa6deS45O12PKrWj8-YaO5NyNSEZ7jQKsePyJyIzKLtb_MPqkSdU040wd0ZQgpRql0jUb7RLMh1E5CfsII7UjQ4Bk7uWDPMd-Wo1F5KCUhIAuttrM0UQW7wXRe1h7XZpAc2y9RIyZVxW3zie0oCq3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
هم‌اکنون سپاه در بیسیم کانال ۱۶ دریایی.
“از آنجا که خروج اسرائیل از لبنان و لغو کامل محاصره دریایی و خروج نیروهای تروریستی آمریکایی از خلیج فارس و منطقه از جمله شرایط اصلی توافق بین ایران و ایالات متحده است. تنگه هرمز تا زمان تحقق این دو شرط بسته خواهد ماند، به همه کشتی‌ها دستور داده شده برای امنیت و سلامت خود به تنگه هرمز نزدیک نشود، هر شناوری که از این دستور سرپیچی کند مورد هدف قرار خواهد گرفت.”
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66488" target="_blank">📅 14:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66487">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
مرندی عضو تیم مذاکرات :
ترامپ بار دیگر ثابت کرد به تعهداتش پایبند نیست.
رژیم صهیونیستی مجازات میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66487" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66485">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شعارهای دیشب مداح حکومتی در مراسم محرم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66485" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66484">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=czEBM2wnO9Glv3Hs8XQa5MBjo3Tteu4BP5rGg6gta4usFDrh_l7sjF8sz1nLU2qGIvEUj14O6vif2NGs5zIF_EbtqR9507S-vTftUPjNnmuw-XqdBK7FNNv3NcopWVFvHhKD4a3smJ75oMP-C0NzkjHf9mdUv4BEbDXnS8GaPuG35KSZJbDtr4IGAf7DmKULY9sldAk3Iph-NiC-i8QdOvB4HSESl-sfuDFX5NpGICy9m4oGYUIKGFWTssRoFPuFwQxRgSifQx64YEQbvMkdRD4u1vkV-TGG5j7iTBcvYV-tdW68EoqTe4BVxCxNVjKiVsLF1ny_PcQnkagiNnHzpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=czEBM2wnO9Glv3Hs8XQa5MBjo3Tteu4BP5rGg6gta4usFDrh_l7sjF8sz1nLU2qGIvEUj14O6vif2NGs5zIF_EbtqR9507S-vTftUPjNnmuw-XqdBK7FNNv3NcopWVFvHhKD4a3smJ75oMP-C0NzkjHf9mdUv4BEbDXnS8GaPuG35KSZJbDtr4IGAf7DmKULY9sldAk3Iph-NiC-i8QdOvB4HSESl-sfuDFX5NpGICy9m4oGYUIKGFWTssRoFPuFwQxRgSifQx64YEQbvMkdRD4u1vkV-TGG5j7iTBcvYV-tdW68EoqTe4BVxCxNVjKiVsLF1ny_PcQnkagiNnHzpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکی در مراسم اعطای مدال هرکاری کرد نتونست گیره مدال رو بندازه داخل و گفت میخوام یک مدل دیگه برات ببندم و مدال رو گره زد و نزدیک بود طرف رو خفه کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66484" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66483">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
‼️
وزیر خارجه پاکستان: مذاکرات سوئیس بدلیل مشغله کاری مسئولان ایرانی در ایام محرم به تعویق افتاد
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66483" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66482">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02588050.mp4?token=tVvnUzczL0qlMeEf4FsvZ8DjCkdzjipFHwgtt42fJBtc3xmXo7mSGRdi7raQt8W3b2biX9QwmNzfxy2DlpDEkAKbi2Ip6oUX5Fnvld63cLFis59EirXS5wXBaNGmN5qlnRGjFzUtMxzKSNC0EIcFyMoa2XS9TEiKCdu0fJ-Y576gILPU3wuWWYCMFJYpGVa__iokd3clZyT-OmXNx9lEPCs_RRn0Trm8xJG2wNXKPqGwB6egljeAMXh3dm1iIe50lriPYPD_6E2iTwX3cvTGkFbAi6a2RZHhOn6B_LfyJKxGT0hwmAm1SNzU0gDcKEdBrlXaSBvBbRXJ_OT98Yw1sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02588050.mp4?token=tVvnUzczL0qlMeEf4FsvZ8DjCkdzjipFHwgtt42fJBtc3xmXo7mSGRdi7raQt8W3b2biX9QwmNzfxy2DlpDEkAKbi2Ip6oUX5Fnvld63cLFis59EirXS5wXBaNGmN5qlnRGjFzUtMxzKSNC0EIcFyMoa2XS9TEiKCdu0fJ-Y576gILPU3wuWWYCMFJYpGVa__iokd3clZyT-OmXNx9lEPCs_RRn0Trm8xJG2wNXKPqGwB6egljeAMXh3dm1iIe50lriPYPD_6E2iTwX3cvTGkFbAi6a2RZHhOn6B_LfyJKxGT0hwmAm1SNzU0gDcKEdBrlXaSBvBbRXJ_OT98Yw1sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلاش سربازان روس برای سرنگونی پهبادها
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66482" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66481">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=oLS86y1NCJ4OKNGb3RI7aTnNGSSnPvc5Kbsq-4i0hCzmw44R1d4pzpMRvqHN0de5w_eHJF-ePOqbmgPWujowcoGCWc4uSwTZ4zB1LJz4qtEYd0-WVRP8rf8QCno7GqSGNgXFxJyLGP46kvX-Dq7YIUWrSShJ0PYXkuwR-s0bhKWZ-SMrH3_p6x9loxnfKD1DT6D5UsZYdQOJdSDOuEb2hBySYyEqluhDbGq8aggg7Cc2mBAb-DDqrRZuru1bJ1odr0WAnmubBEBKGiOyi6cgvnV9IczE8YNGJfXuMqU8tEsvUQp9Qt9ScWTja0ozHng2ZYtMhgwDOCVKyn5DNrztfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=oLS86y1NCJ4OKNGb3RI7aTnNGSSnPvc5Kbsq-4i0hCzmw44R1d4pzpMRvqHN0de5w_eHJF-ePOqbmgPWujowcoGCWc4uSwTZ4zB1LJz4qtEYd0-WVRP8rf8QCno7GqSGNgXFxJyLGP46kvX-Dq7YIUWrSShJ0PYXkuwR-s0bhKWZ-SMrH3_p6x9loxnfKD1DT6D5UsZYdQOJdSDOuEb2hBySYyEqluhDbGq8aggg7Cc2mBAb-DDqrRZuru1bJ1odr0WAnmubBEBKGiOyi6cgvnV9IczE8YNGJfXuMqU8tEsvUQp9Qt9ScWTja0ozHng2ZYtMhgwDOCVKyn5DNrztfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتز، وزیر دفاع اسرائیل، درباره سوریه:
ما آنجا می‌جنگیم. ما به الجولانی نیاز نداریم. الجولانی، تروریست کت و شلواری، نیازی ندارد که بیاید و به ما کمک کند.
ما سوریه را خوب می‌شناسیم. او قرار نیست در لبنان به ما کمک کند. او باید در سوریه بماند، در کار ما دخالت نکند و ما را مجبور به دخالت در کار خود نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66481" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66480">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=QIbXGfpkvr0gGRglCBCuQBgDg5AWB5YGeYXMU7FdU8yABZjrV3wgM1zVUbUQd5_TH1P8HSQzjN1VhYaL2tpOkQz5afJOcEpz0XsgxOAnb4GpGFVBVYFjrmpFV73CJhsUkQIDIZDffoqaR_woBDnVX0JdcQSfiAoZuIs0VycZET6Kzk3DmH9-tU9Aj4FFR8-0g7rFkJQtDFoyUik23w1AmvG454L8YDdOlpLqoSiQ0C-8DGjWgKgbd0E96HtsacmnuUCB-fbTMI8zhkpf8366yV_0_wltJAhntKwayfVHh_CrU1RFpEoAW_237Twdu2FGNfxNEpWS9TxqzVkMkugCgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=QIbXGfpkvr0gGRglCBCuQBgDg5AWB5YGeYXMU7FdU8yABZjrV3wgM1zVUbUQd5_TH1P8HSQzjN1VhYaL2tpOkQz5afJOcEpz0XsgxOAnb4GpGFVBVYFjrmpFV73CJhsUkQIDIZDffoqaR_woBDnVX0JdcQSfiAoZuIs0VycZET6Kzk3DmH9-tU9Aj4FFR8-0g7rFkJQtDFoyUik23w1AmvG454L8YDdOlpLqoSiQ0C-8DGjWgKgbd0E96HtsacmnuUCB-fbTMI8zhkpf8366yV_0_wltJAhntKwayfVHh_CrU1RFpEoAW_237Twdu2FGNfxNEpWS9TxqzVkMkugCgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حملات گسترده ارتش اسرائیل به مواضع حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66480" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66479">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=q_gi4052e82K-OgNwHr57FtOCF30ZpDJvHtiRDYzWP3NIksGNs2ThatayBsqZeRuxUHBAMjXiRtoSG3hYHtT9R_ew5s4BoijqrsF8uqrzYW_fZfnPWho88I0y9V4emYw9c8tkxOeGIKYOBJ0hev2bnte71QBd9MgIAN7hJHn76caayr594CssB0DC2PJGVX2HScjqao7psh4kGlxABisWjuvTmaNC4etox9SnRq8poA-IB8j4AAd-FvbUzGeQ-gnt-RoYGmDRyMd8asyFDjmkeyGXbxNCERwHuMsiSzHaOsM3844JXSYg7O5i3fUfgUyhbR80rUJVezZXJv6MTH-DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=q_gi4052e82K-OgNwHr57FtOCF30ZpDJvHtiRDYzWP3NIksGNs2ThatayBsqZeRuxUHBAMjXiRtoSG3hYHtT9R_ew5s4BoijqrsF8uqrzYW_fZfnPWho88I0y9V4emYw9c8tkxOeGIKYOBJ0hev2bnte71QBd9MgIAN7hJHn76caayr594CssB0DC2PJGVX2HScjqao7psh4kGlxABisWjuvTmaNC4etox9SnRq8poA-IB8j4AAd-FvbUzGeQ-gnt-RoYGmDRyMd8asyFDjmkeyGXbxNCERwHuMsiSzHaOsM3844JXSYg7O5i3fUfgUyhbR80rUJVezZXJv6MTH-DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.
ما از «مناطق امنیتی» حرکت نخواهیم کرد، نه در سوریه، نه در غزه و نه در لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66479" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66478">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEu8-sSYyQlhoelaQLx-XjQaPdxdjOZX1udi0eMplLiIUoG6NcmnFzGIe3S_xl8EAYZ16owW4rdTJEAvMHENM77mLQI47GSO5Bg0iYsL-Z7TmwAjbnc7WAQfeDxbk6pd0W1d_XViNW9mgAz2RtSIWW-SB8G_jAo0_BbjfbeR-CMRAsAJuEEYDY93KO21O53krHUF2BHZ5I2NyvxnNSXTWkU_BIsXWKB51va5tAykU9NH83AVCFSp4lD2HbxkPt4LmWP3UfKOZaLTgCgjEhsdvSj_wPxodOLNbzyUcgV9bgp_Ct9UWHgP27Ovpx2mDd-j91kTeof-EenNjSxDtcffdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
گوش‌بفرمانیم، وظیفهٔ محول‌شده به ما توسط مقام معظم رهبری پیگیری تحقق شروط و بندهای تفاهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66478" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66477">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=L4tufn1_Ikteb8lno_LVRg5iwv2xPNyzNVddd5XZxurnAyulk7Px-rBfHaLCVdkDlHeHq-go72GIUtotp79CSxmUiZWf7OD0tWbAOWZ44InPzgFn-8iP9Ssf3Qyzke6h56mo2IVLQ6tHOeyxXw6wJnhjEc20Agq-MCKnxT66f0yEpUcSwtqGzDwXOUDkfoUEF8K1vlRJDBNwFjr6ZCSj1SFNgABJ3h8ERsnBJDr1M269JHIpNvtiBrCzWPWYXHoz6Bmlc6GgVq8aeDPiOhX9_qBYayB3hRB1rNkbLy-TexfLHJ9SN-E8lDvrsT0YxhYQbTMm26BacIByEkmuy7iaZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=L4tufn1_Ikteb8lno_LVRg5iwv2xPNyzNVddd5XZxurnAyulk7Px-rBfHaLCVdkDlHeHq-go72GIUtotp79CSxmUiZWf7OD0tWbAOWZ44InPzgFn-8iP9Ssf3Qyzke6h56mo2IVLQ6tHOeyxXw6wJnhjEc20Agq-MCKnxT66f0yEpUcSwtqGzDwXOUDkfoUEF8K1vlRJDBNwFjr6ZCSj1SFNgABJ3h8ERsnBJDr1M269JHIpNvtiBrCzWPWYXHoz6Bmlc6GgVq8aeDPiOhX9_qBYayB3hRB1rNkbLy-TexfLHJ9SN-E8lDvrsT0YxhYQbTMm26BacIByEkmuy7iaZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بمباران شدید نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66477" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
